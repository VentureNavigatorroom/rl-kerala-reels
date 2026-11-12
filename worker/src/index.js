// rl-kerala-autopilot: runs 24/7 on Cloudflare, independent of Claude.
//  - cron: posts reels (with cover, trial reels when allowed) and Stories at IST slots from the GitHub Pages library
//  - cron: pulls insights daily and rewrites content-mix weights (optimiser)
//  - webhook: answers Instagram DMs / keyword comments with a Malayalam-first qualifying bot, stores leads
// Secrets (wrangler secret / dashboard): IG_TOKEN, IG_USER_ID, VERIFY_TOKEN, ADMIN_KEY
// Vars: LIB_BASE (GitHub Pages base URL of library/), GRAPH (graph API base)
// KV binding: STATE

const SLOTS_IST = [ // [hh, mm, type]  5 reels + 5 stories + 5 carousels a day
  [7, 25, "reel"], [8, 10, "story"], [9, 10, "carousel"], [11, 40, "carousel"], [12, 20, "reel"], [13, 5, "story"],
  [15, 10, "carousel"], [17, 25, "reel"], [18, 10, "story"], [18, 45, "carousel"], [19, 25, "reel"], [20, 15, "story"],
  [20, 55, "carousel"], [21, 25, "reel"], [22, 10, "story"],
];
const TRIAL_SHARE = 0.4; // share of reels posted as trial reels (non-followers first) while the feature is available

const IST = (d = new Date()) => new Date(d.getTime() + 5.5 * 3600e3);
const json = (o, s = 200) => new Response(JSON.stringify(o, null, 1), { status: s, headers: { "content-type": "application/json" } });

async function kv(env, k, d) { const v = await env.STATE.get(k); return v ? JSON.parse(v) : d; }
async function kvPut(env, k, v) { await env.STATE.put(k, JSON.stringify(v)); }
async function log(env, msg) {
  const l = await kv(env, "log", []); l.unshift(`${IST().toISOString().slice(0, 16)} ${msg}`); await kvPut(env, "log", l.slice(0, 300));
}
async function discord(env, content) {
  if (!env.DISCORD_WEBHOOK) return;
  try { await fetch(env.DISCORD_WEBHOOK, { method: "POST", headers: { "content-type": "application/json" }, body: JSON.stringify({ content: content.slice(0, 1900) }) }); } catch {}
}
async function graph(env, path, params = {}, method = "POST") {
  const u = new URL(`${env.GRAPH}/${path}`);
  const body = new URLSearchParams({ ...params, access_token: env.IG_TOKEN });
  const r = method === "GET" ? await fetch(`${u}?${body}`) : await fetch(u, { method, body });
  const j = await r.json(); if (j.error) throw new Error(`${path}: ${j.error.message}`); return j;
}

// ---------------- posting ----------------
async function manifest(env) {
  const r = await fetch(`${env.LIB_BASE}/manifest.json?t=${Date.now()}`); return r.ok ? r.json() : { items: [] };
}
async function waitReady(env, id) {
  for (let i = 0; i < 20; i++) {
    const s = await graph(env, id, { fields: "status_code" }, "GET");
    if (s.status_code === "FINISHED") return; if (s.status_code === "ERROR" || s.status_code === "EXPIRED") throw new Error(`container ${s.status_code}`);
    await new Promise(r => setTimeout(r, 6000));
  }
  throw new Error("container not ready in time");
}
async function postReel(env) {
  const m = await manifest(env); const posted = await kv(env, "posted", {});
  const w = await kv(env, "weights", null);
  const avail = m.items.filter(i => !posted[i.id]);
  if (!avail.length) { await log(env, "NO STOCK: library empty"); await discord(env, "⚠️ Reel library is empty. Nothing to post. Check the nightly factory on GitHub."); return; }
  if (avail.length < 35 && IST().getUTCHours() === 7 && IST().getUTCMinutes() < 30) await discord(env, `⚠️ Backup below 1 week: ${avail.length} reels left (target 70 = 2 weeks). Ask Claude to write more scripts.`);
  const recent = Object.values(posted).sort((a, b) => b.t - a.t).slice(0, 2);
  const score = i => (w?.kind?.[i.kind] ?? 1) * (w?.segment?.[i.segment] ?? 1) * (recent.some(r => r.kind === i.kind) ? 0.5 : 1) * (0.8 + Math.random() * 0.4);
  const it = avail.sort((a, b) => score(b) - score(a))[0];
  const p = { media_type: "REELS", video_url: `${env.LIB_BASE}/${it.video}`, cover_url: `${env.LIB_BASE}/${it.cover}`, caption: it.caption, share_to_feed: "true" };
  const trialOff = await kv(env, "trial_unavailable", false);
  const asTrial = !trialOff && Math.random() < TRIAL_SHARE;
  let c;
  try { c = await graph(env, `${env.IG_USER_ID}/media`, asTrial ? { ...p, trial_params: JSON.stringify({ graduation_strategy: "SS_PERFORMANCE" }) } : p); }
  catch (e) {
    if (!asTrial) throw e;
    await kvPut(env, "trial_unavailable", true); await log(env, `trial reels not available yet (${e.message}); posting normally`);
    c = await graph(env, `${env.IG_USER_ID}/media`, p);
  }
  await waitReady(env, c.id);
  const pub = await graph(env, `${env.IG_USER_ID}/media_publish`, { creation_id: c.id });
  posted[it.id] = { media: pub.id, t: Date.now(), kind: it.kind, segment: it.segment, trial: asTrial && !(await kv(env, "trial_unavailable", false)) };
  await kvPut(env, "posted", posted); await log(env, `reel ${it.id} posted (${pub.id})${posted[it.id].trial ? " as trial" : ""}`);
}
async function postStory(env) {
  const m = await manifest(env); const done = await kv(env, "stories", {});
  const stories = (m.stories || []).filter(s => !done[s.id]);
  if (!stories.length) { await log(env, "NO STORY STOCK"); return; }
  const s = stories[0];
  const c = await graph(env, `${env.IG_USER_ID}/media`, { media_type: "STORIES", image_url: `${env.LIB_BASE}/${s.image}` });
  await waitReady(env, c.id);
  const pub = await graph(env, `${env.IG_USER_ID}/media_publish`, { creation_id: c.id });
  done[s.id] = { media: pub.id, t: Date.now() }; await kvPut(env, "stories", done); await log(env, `story ${s.id} posted`);
}

async function postCarousel(env) {
  const m = await manifest(env); const posted = await kv(env, "posted", {});
  const avail = (m.carousels || []).filter(c => !posted[c.id]);
  if (!avail.length) { await log(env, "NO CAROUSEL STOCK"); await discord(env, "⚠️ Carousel library is empty."); return; }
  const recent = Object.values(posted).filter(p => p.kind === "carousel").sort((a, b) => b.t - a.t)[0];
  const c = avail.find(x => !recent || x.segment !== recent.segment) || avail[0];
  const kids = [];
  for (const img of c.images.slice(0, 10)) kids.push((await graph(env, `${env.IG_USER_ID}/media`, { image_url: `${env.LIB_BASE}/${img}`, is_carousel_item: "true" })).id);
  const box = await graph(env, `${env.IG_USER_ID}/media`, { media_type: "CAROUSEL", children: kids.join(","), caption: c.caption });
  await waitReady(env, box.id);
  const pub = await graph(env, `${env.IG_USER_ID}/media_publish`, { creation_id: box.id });
  posted[c.id] = { media: pub.id, t: Date.now(), kind: "carousel", segment: c.segment };
  await kvPut(env, "posted", posted); await log(env, `carousel ${c.id} posted (${pub.id})`);
}

// ---------------- optimiser ----------------
async function optimise(env) {
  const posted = await kv(env, "posted", {}); const stats = {};
  for (const [id, p] of Object.entries(posted)) {
    if (Date.now() - p.t < 48 * 3600e3 || Date.now() - p.t > 30 * 86400e3) continue; // judge after 48 h, last 30 days
    try {
      const r = await graph(env, `${p.media}/insights`, { metric: "reach,shares,saved,total_interactions" }, "GET");
      const v = Object.fromEntries(r.data.map(d => [d.name, d.values?.[0]?.value ?? d.total_value?.value ?? 0]));
      const cm = await graph(env, `${p.media}/comments`, { fields: "text", limit: "100" }, "GET");
      const kw = (cm.data || []).filter(c => /START|NAME|AFTER|CHECKLIST/i.test(c.text)).length;
      p.stats = { ...v, keyword_comments: kw };
    } catch (e) { continue; }
    const s = p.stats; const score = (s.shares * 3 + s.saved * 2 + s.keyword_comments * 10 + s.total_interactions) / Math.max(50, s.reach) * 1000;
    for (const dim of ["kind", "segment"]) { const k = p[dim]; stats[dim] ??= {}; stats[dim][k] ??= []; stats[dim][k].push(score); }
  }
  await kvPut(env, "posted", posted);
  const weights = { updated: IST().toISOString().slice(0, 10) };
  for (const dim of ["kind", "segment"]) {
    const means = Object.fromEntries(Object.entries(stats[dim] || {}).filter(([, a]) => a.length >= 3).map(([k, a]) => [k, a.reduce((x, y) => x + y) / a.length]));
    const avg = Object.values(means).reduce((x, y) => x + y, 0) / Math.max(1, Object.keys(means).length);
    // move toward winners but never below 0.5x or above 2x: every type keeps being tested
    weights[dim] = Object.fromEntries(Object.entries(means).map(([k, m]) => [k, Math.min(2, Math.max(0.5, avg ? m / avg : 1))]));
  }
  await kvPut(env, "weights", weights); await log(env, `optimiser: ${JSON.stringify(weights)}`);
}

// ---------------- DM bot ----------------
const BOT_SYSTEM = `You are the automated assistant of rejectionlist.kerala, a company-registration service in Kerala, India.
Rules: Reply in the user's language (Malayalam or English), short and friendly, max 3 sentences. Say you are an automated assistant if asked.
NEVER state any price, fee, cost, discount or government fee; if asked, say the team will share the exact quote on a call after understanding the business.
Never give legal advice beyond general facts. Goal: qualify the lead by asking, one at a time:
1) what the business does, 2) how many founders and whether any are NRIs, 3) whether the business already has income, clients or funding,
4) how soon they want to register, 5) their phone number, 6) preferred language for the call: Malayalam or English.
When you have all six, thank them and say a team member will call. Output only the reply text.`;

async function botReply(env, thread) {
  const r = await env.AI.run("@cf/meta/llama-3.3-70b-instruct-fp8-fast", { messages: [{ role: "system", content: BOT_SYSTEM }, ...thread.slice(-12)], max_tokens: 220 });
  return (r.response || "").trim();
}
async function extractLead(env, thread) {
  const r = await env.AI.run("@cf/meta/llama-3.3-70b-instruct-fp8-fast", { messages: [
    { role: "system", content: `From this conversation, output JSON only: {"business":"","founders":"","nri":false,"traction":"","timeline":"","phone":"","language":"","intent":"high|medium|low","can_afford_30k":"likely|unclear|unlikely","reason":""}. "can_afford_30k" judges from traction, funding, urgency and team, never from asking about money.` },
    { role: "user", content: thread.map(m => `${m.role}: ${m.content}`).join("\n") }], max_tokens: 300 });
  try { return JSON.parse((r.response || "").match(/\{[\s\S]*\}/)[0]); } catch { return null; }
}
async function sendDM(env, to, text) {
  return graph(env, `${env.IG_USER_ID}/messages`, { recipient: JSON.stringify({ id: to }), message: JSON.stringify({ text }) });
}
async function handleWebhook(env, body) {
  for (const entry of body.entry || []) {
    for (const ev of entry.messaging || []) {
      if (!ev.message || ev.message.is_echo || !ev.message.text) continue;
      const uid = ev.sender.id; const key = `t:${uid}`; const thread = await kv(env, key, []);
      thread.push({ role: "user", content: ev.message.text });
      const reply = await botReply(env, thread); thread.push({ role: "assistant", content: reply });
      await kvPut(env, key, thread); await sendDM(env, uid, reply);
      if (/\d{10}/.test(ev.message.text.replace(/\D/g, "")) || thread.length >= 12) {
        const lead = await extractLead(env, thread);
        if (lead) {
          const leads = await kv(env, "leads", {}); const prev = leads[uid];
          leads[uid] = { ...lead, ig_user: uid, updated: IST().toISOString().slice(0, 16) }; await kvPut(env, "leads", leads); await log(env, `lead ${uid}: ${lead.intent}/${lead.can_afford_30k}`);
          if (lead.phone && (!prev || !prev.phone) && lead.intent !== "low") {
            await discord(env, `🔔 **New ${lead.intent.toUpperCase()}-intent lead** (budget fit: ${lead.can_afford_30k})\n📞 ${lead.phone}  ·  🗣 ${lead.language || "?"}\n🏢 ${lead.business}\n👥 ${lead.founders}${lead.nri ? " (NRI)" : ""}\n📈 ${lead.traction}\n⏱ ${lead.timeline}\nWhy: ${lead.reason}\nLead ID: ${uid}\nAfter your call, tell Claude: "lead ${uid}: <what happened>"`);
          }
        }
      }
    }
    for (const ch of entry.changes || []) { // keyword comments -> one private reply opens the DM
      if (ch.field !== "comments" || !ch.value?.text) continue;
      const m = ch.value.text.match(/\b(START|NAME|AFTER|CHECKLIST)\b/i); if (!m) continue;
      const text = { START: "ഹായ്! 👋 നിങ്ങളുടെ ബിസിനസിന് പറ്റിയ സ്ട്രക്ചർ പറഞ്ഞുതരാം. ആദ്യം, നിങ്ങളുടെ ബിസിനസ് എന്താണ്?",
        NAME: "ഹായ്! 👋 നിങ്ങൾ ആലോചിക്കുന്ന കമ്പനി പേര് ഇവിടെ അയക്കൂ, ഞങ്ങൾ ചെക്ക് ചെയ്യാം.",
        AFTER: "ഹായ്! 👋 ആദ്യ 180 ദിവസത്തെ ചെക്ക്‌ലിസ്റ്റ് അയക്കാം. നിങ്ങളുടെ കമ്പനി രജിസ്റ്റർ ചെയ്തിട്ട് എത്ര നാളായി?",
        CHECKLIST: "ഹായ്! 👋 ഡോക്യുമെന്റ് ലിസ്റ്റ് അയക്കാം. എത്ര ഫൗണ്ടർമാർ ഉണ്ട്?" }[m[1].toUpperCase()];
      try { await graph(env, `${env.IG_USER_ID}/messages`, { recipient: JSON.stringify({ comment_id: ch.value.id }), message: JSON.stringify({ text }) }); await log(env, `private reply to ${m[1]} comment`); }
      catch (e) { await log(env, `comment reply failed: ${e.message}`); }
    }
  }
}

// ---------------- entry points ----------------
export default {
  async scheduled(ev, env, ctx) {
    const now = IST(); const h = now.getUTCHours(), mi = now.getUTCMinutes();
    const slot = SLOTS_IST.find(([sh, sm]) => sh === h && Math.abs(sm - mi) < 5);
    const day = now.toISOString().slice(0, 10);
    try {
      if (slot) {
        const k = `slot:${day}:${slot[0]}:${slot[1]}`;
        if (!(await env.STATE.get(k))) { await env.STATE.put(k, "1", { expirationTtl: 172800 }); slot[2] === "reel" ? await postReel(env) : slot[2] === "story" ? await postStory(env) : await postCarousel(env); }
      }
      if (h === 3 && mi < 5) await optimise(env);
      if (h === 21 && mi >= 40 && mi < 45) {
        const posted = await kv(env, "posted", {}); const today = Object.values(posted).filter(p => IST(new Date(p.t)).toISOString().slice(0, 10) === day).length;
        const leads = Object.values(await kv(env, "leads", {})).filter(l => (l.updated || "").startsWith(day));
        const errs = (await kv(env, "log", [])).filter(l => l.startsWith(day) && /ERROR|NO STOCK/.test(l)).length;
        await discord(env, `📊 Daily report ${day}: ${today} reels posted · ${leads.length} leads today · ${errs} problems`);
      }
    } catch (e) { await log(env, `ERROR ${e.message}`); await discord(env, `❌ Autopilot error: ${e.message}`); }
  },
  async fetch(req, env, ctx) {
    const u = new URL(req.url);
    if (u.pathname === "/webhook" && req.method === "GET") {
      return u.searchParams.get("hub.verify_token") === env.VERIFY_TOKEN ? new Response(u.searchParams.get("hub.challenge")) : new Response("no", { status: 403 });
    }
    if (u.pathname === "/webhook" && req.method === "POST") { const b = await req.json(); ctx.waitUntil(handleWebhook(env, b).catch(e => log(env, `webhook ERROR ${e.message}`))); return new Response("ok"); }
    if (u.pathname === "/public/posted") return json(Object.keys(await kv(env, "posted", {}))); // builder reads this to know stock
    if (u.searchParams.get("key") !== env.ADMIN_KEY) return new Response("rl-kerala autopilot", { status: 200 });
    if (u.pathname === "/status") return json({ weights: await kv(env, "weights", null), posted: Object.keys(await kv(env, "posted", {})).length, log: (await kv(env, "log", [])).slice(0, 60) });
    if (u.pathname === "/leads") return json(await kv(env, "leads", {}));
    if (u.pathname === "/run/reel") { await postReel(env); return json({ ok: true, log: (await kv(env, "log", [])).slice(0, 3) }); }
    if (u.pathname === "/run/carousel") { await postCarousel(env); return json({ ok: true, log: (await kv(env, "log", [])).slice(0, 3) }); }
    if (u.pathname === "/run/story") { await postStory(env); return json({ ok: true, log: (await kv(env, "log", [])).slice(0, 3) }); }
    if (u.pathname === "/run/optimise") { await optimise(env); return json(await kv(env, "weights", null)); }
    return new Response("not found", { status: 404 });
  },
};

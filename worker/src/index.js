// rl-kerala-autopilot: runs 24/7 on Cloudflare, independent of Claude.
//  - cron: posts reels (with cover, trial reels when allowed) and Stories at IST slots from the GitHub Pages library
//  - cron: pulls insights daily and rewrites content-mix weights (optimiser)
//  - webhook: answers Instagram DMs / keyword comments with a English qualifying bot, stores leads
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
async function alertOnce(env, tag, content) {   // at most one Discord alert per tag per IST day
  const k = `alert:${tag}:${IST().toISOString().slice(0, 10)}`;
  if (await env.STATE.get(k)) return;
  await env.STATE.put(k, "1", { expirationTtl: 172800 }); await discord(env, content);
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
  posted[it.id] = { media: pub.id, t: Date.now(), kind: it.kind, segment: it.segment, scene: it.scene || null, trial: asTrial && !(await kv(env, "trial_unavailable", false)) };
  await kvPut(env, "posted", posted); await log(env, `reel ${it.id} posted (${pub.id})${posted[it.id].trial ? " as trial" : ""}`);
}
async function postStory(env) {
  // daily mix: 1 new-reel teaser, then tip / quiz question / quiz answer / contact card, so people follow and reply
  const m = await manifest(env); const done = await kv(env, "stories", {});
  const posted = await kv(env, "posted", {});
  const all = (m.stories || []).filter(s => !done[s.id] && (!s.after || done[s.after]));
  const teasers = all.filter(s => s.reel && posted[s.reel]);           // only tease reels already live
  const others = all.filter(s => !s.reel);
  const hour = IST().getUTCHours();
  const pendingAnswer = others.find(s => s.after);
  let s = hour < 9 ? teasers[0] : (pendingAnswer || others.find(x => x.kind === (hour < 14 ? "tip" : hour < 19 ? "quiz" : "contact")) || others[0] || teasers[0]);
  if (!s) { await log(env, "NO STORY STOCK"); await alertOnce(env, "nostory", "⚠️ Story library is empty. Nothing to post. Check the nightly factory on GitHub."); return; }
  const c = await graph(env, `${env.IG_USER_ID}/media`, { media_type: "STORIES", image_url: `${env.LIB_BASE}/${s.image}` });
  await waitReady(env, c.id);
  const pub = await graph(env, `${env.IG_USER_ID}/media_publish`, { creation_id: c.id });
  done[s.id] = { media: pub.id, t: Date.now() }; await kvPut(env, "stories", done);
  posted[s.id] = { media: pub.id, t: Date.now(), kind: "story", segment: s.segment || null, story_kind: s.kind || "teaser" }; await kvPut(env, "posted", posted);
  await log(env, `story ${s.id} posted`);
}

async function postCarousel(env) {
  const m = await manifest(env); const posted = await kv(env, "posted", {});
  const avail = (m.carousels || []).filter(c => !posted[c.id]);
  if (!avail.length) { await log(env, "NO CAROUSEL STOCK"); await alertOnce(env, "nocarousel", "⚠️ Carousel library is empty. Nothing to post. Check the nightly factory on GitHub."); return; }
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
async function snapshot(env) {
  // one row per post per day: metrics + where/when it was posted. Kept 60 days. This is the insights database.
  const posted = await kv(env, "posted", {}); const day = IST().toISOString().slice(0, 10);
  for (const [id, p] of Object.entries(posted)) {
    const age = (Date.now() - p.t) / 86400e3; if (age > 30 || p.kind === undefined) continue;
    let v = {};
    try {
      const metrics = p.kind === "carousel" ? "reach,shares,saved,total_interactions,likes,comments" : "reach,views,shares,saved,total_interactions,likes,comments";
      const r = await graph(env, `${p.media}/insights`, { metric: metrics }, "GET");
      v = Object.fromEntries(r.data.map(d => [d.name, d.values?.[0]?.value ?? d.total_value?.value ?? 0]));
    } catch (e) { v = { error: String(e.message).slice(0, 80) }; }
    const ev = await kv(env, `ev:${id}`, { comments: 0, keyword: {}, leads: 0, dms: 0 });
    const posted_ist = IST(new Date(p.t));
    const row = { day, id, kind: p.kind, segment: p.segment, scene: p.scene || null, trial: !!p.trial,
      posted_at: posted_ist.toISOString().slice(0, 16), weekday: posted_ist.getUTCDay(), slot: posted_ist.toISOString().slice(11, 16),
      age_days: Math.round(age * 10) / 10, ...v, keyword_comments: Object.values(ev.keyword).reduce((a, b) => a + b, 0), keywords: ev.keyword, dms: ev.dms, leads: ev.leads };
    const k = `snap:${id}`; const hist = await kv(env, k, []); hist.push(row); await kvPut(env, k, hist.slice(-31));
  }
  await log(env, `snapshot ${day}`);
}

function median(a) { const s = [...a].sort((x, y) => x - y); return s.length ? s[Math.floor(s.length / 2)] : 0; }

async function optimise(env) {
  // Cautious: judge each post at 48-72h; compare it with posts from the SAME slot (time effect removed),
  // need >= 5 posts per group and a clear gap before moving weights, and move at most 25% per week.
  const posted = await kv(env, "posted", {}); const rows = [];
  for (const id of Object.keys(posted)) {
    const h = await kv(env, `snap:${id}`, []); const r = h.find(x => x.age_days >= 2) || null;
    if (!r || r.error || !r.reach) continue;
    r.score = ((r.shares || 0) * 3 + (r.saved || 0) * 2 + (r.keyword_comments || 0) * 10 + (r.leads || 0) * 25 + (r.total_interactions || 0)) / Math.max(50, r.reach) * 1000;
    rows.push(r);
  }
  const bySlot = {}; rows.forEach(r => (bySlot[r.slot] ??= []).push(r.score));
  rows.forEach(r => { const m = median(bySlot[r.slot]); r.rel = m ? r.score / m : 1; });   // relative to same time slot
  const old = await kv(env, "weights", { kind: {}, segment: {} }); const weights = { updated: IST().toISOString().slice(0, 10), n_posts: rows.length, kind: {}, segment: {} };
  for (const dim of ["kind", "segment"]) {
    const g = {}; rows.forEach(r => (g[r[dim]] ??= []).push(r.rel));
    for (const [k, a] of Object.entries(g)) {
      const prev = old[dim]?.[k] ?? 1;
      if (a.length < 5) { weights[dim][k] = prev; continue; }                  // not enough evidence: keep
      const m = median(a); const target = Math.abs(m - 1) < 0.15 ? 1 : Math.min(2, Math.max(0.5, m));   // ignore small gaps
      weights[dim][k] = Math.round(Math.min(prev * 1.25, Math.max(prev * 0.75, target)) * 100) / 100;     // max 25% move
    }
  }
  // Time slots are only REPORTED (not auto-changed) until there are 3+ weeks of data
  const slotRep = Object.fromEntries(Object.entries(bySlot).map(([s, a]) => [s, { posts: a.length, median_score: Math.round(median(a) * 10) / 10 }]));
  await kvPut(env, "weights", weights); await kvPut(env, "slot_report", slotRep);
  await log(env, `optimiser: ${JSON.stringify(weights)}`);
  if (IST().getUTCDay() === 1) {                                           // Monday summary to Discord
    const top = [...rows].sort((a, b) => b.score - a.score).slice(0, 3).map(r => `${r.id} (${r.kind}/${r.segment}, ${r.slot}): reach ${r.reach}, shares ${r.shares || 0}, keyword ${r.keyword_comments}, leads ${r.leads}`).join("\n");
    await discord(env, `📈 Weekly insights (${rows.length} posts judged)\nTop posts:\n${top || "not enough data yet"}\nMix weights: ${JSON.stringify({ kind: weights.kind, segment: weights.segment })}\nTimes are only being measured for now; no time changes until 3+ weeks of data.`);
  }
}

// ---------------- DM bot ----------------
const BOT_SYSTEM = `You reply to Instagram DMs for rejectionlist.kerala, a company-registration service in Kerala, India.
Rules: Always reply in simple, friendly English (even if the user writes in Malayalam or Manglish), short, max 3 sentences. Write like the rejectionlist.kerala team; do not introduce yourself as an assistant, AI or bot and do not mention automation. If the user directly asks whether this is a bot or a real person, do not claim to be human: say these chats give quick answers and a team member will call them personally.
NEVER state any price, fee, cost, discount or government fee; if asked, say the team will share the exact quote on a call after understanding the business.
Never give legal advice beyond general facts. If someone sends a proposed company name, give a first review using only these rules: not similar (even in sound) to an existing company or LLP, no clash with a registered trademark, words like Bank or Insurance need special approval, keep 2-3 backups. Say clearly that you cannot confirm availability and that final availability is confirmed when the application is filed. Then continue qualifying.
Goal: qualify the lead by asking, one at a time:
1) what the business does, 2) how many founders and whether any are NRIs, 3) whether the business already has income, clients or funding,
4) how soon they want to register, 5) their phone number, 6) preferred language for the call: Malayalam or English.
When you have all six, thank them and say a team member will call. Output only the reply text.`;

// Fallback when Cloudflare's free AI allowance is used up or the model errors: fixed rules + fixed question order.
const FALLBACK_Q = [
  "What does your business do? Tell us in a line or two.",
  "How many founders are there? Is anyone an NRI?",
  "Does the business already have income, clients or funding?",
  "How soon do you want to register?",
  "Could you share a phone number so our team can call you?",
  "Would you prefer the call in Malayalam or English?",
  "Thank you! 🙏 Our team will call you shortly.",
];
function fallbackReply(thread) {
  const last = thread[thread.length - 1]?.content || "";
  const asked = thread.filter(m => m.role === "assistant" && FALLBACK_Q.includes(m.content)).length;
  let pre = "";
  if (/\b(pvt|ltd|private|limited|llp|opc)\b/i.test(last) || /പ്രൈവറ്റ്|ലിമിറ്റഡ്/.test(last)) {
    const hits = ["bank", "insurance", "ബാങ്ക്", "ഇൻഷുറൻസ്"].filter(x => last.toLowerCase().includes(x));
    pre = hits.length ? `Words like "${hits[0]}" need special approval, so this name could be rejected. ` : "No restricted words in this name. It must also not be similar to an existing company, LLP or registered trademark. ";
    pre += "Final availability is confirmed only when the application is filed.\n\n";
  }
  if (/price|fee|cost|charge|rate|എത്ര രൂപ|ചാർജ്|ഫീസ്/i.test(last)) pre = "Our team will share the exact quote on a call once they understand your business. ";
  return pre + FALLBACK_Q[Math.min(asked, FALLBACK_Q.length - 1)];
}
async function botReply(env, thread) {
  try {
    const r = await env.AI.run("@cf/meta/llama-3.3-70b-instruct-fp8-fast", { messages: [{ role: "system", content: BOT_SYSTEM }, ...thread.slice(-12)], max_tokens: 220 });
    const t = (r.response || "").trim(); if (t) return t;
  } catch (e) { await log(env, `AI unavailable, using fallback: ${String(e.message).slice(0, 80)}`); }
  return fallbackReply(thread);
}
function regexLead(thread) {
  const all = thread.filter(m => m.role === "user").map(m => m.content).join(" \n ");
  const phone = (all.replace(/[\s-]/g, "").match(/(?:\+?91)?[6-9]\d{9}/) || [""])[0];
  return { business: thread.find(m => m.role === "user")?.content?.slice(0, 120) || "", founders: "", nri: /nri|gulf|dubai|ഗൾഫ്|ദുബായ്|സൗദി|ഖത്തർ|മസ്കറ്റ്/i.test(all), traction: "", timeline: "",
    phone, language: /english|ഇംഗ്ലീഷ്/i.test(all) ? "English" : /malayalam|മലയാളം/i.test(all) ? "Malayalam" : "", intent: phone ? "medium" : "low", can_afford_30k: "unclear", reason: "AI unavailable: basic extraction, read the chat" };
}
async function extractLead(env, thread) {
  let r;
  try { r = await env.AI.run("@cf/meta/llama-3.3-70b-instruct-fp8-fast", { messages: [
    { role: "system", content: `From this conversation, output JSON only: {"business":"","founders":"","nri":false,"traction":"","timeline":"","phone":"","language":"","intent":"high|medium|low","can_afford_30k":"likely|unclear|unlikely","reason":""}. "can_afford_30k" judges from traction, funding, urgency and team, never from asking about money.` },
    { role: "user", content: thread.map(m => `${m.role}: ${m.content}`).join("\n") }], max_tokens: 300 }); }
  catch (e) { return regexLead(thread); }
  try { return JSON.parse((r.response || "").match(/\{[\s\S]*\}/)[0]); } catch { return regexLead(thread); }
}
async function igProfile(env, igsid) {
  try { const p = await graph(env, igsid, { fields: "username,is_user_follow_business" }, "GET"); return { username: p.username || null, follows: typeof p.is_user_follow_business === "boolean" ? p.is_user_follow_business : null }; }
  catch (e) { await log(env, `profile lookup failed: ${e.message}`); return { username: null, follows: null }; }
}
// Keyword matching that tolerates typos, spacing, case, and Malayalam spellings
// (e.g. "strat", "Satrt🙏", "chek list", "nmae", "സ്റ്റാർട്ട്"), without firing on ordinary words like "star", "game" or "alter".
const KEYWORDS = ["START", "NAME", "AFTER", "CHECKLIST"];
const KW_ML = [[/സ്റ്റാർ?ട്ട?്?|സ്റ്റാട്ട്/, "START"], [/നെയിം|നേം|നെയിമ്/, "NAME"], [/ആഫ്റ്റർ|ആഫ്ടർ/, "AFTER"], [/ചെക്ക്[\s\u200c\u200d]*ലിസ്റ്റ്|ചെക്ലിസ്റ്റ്/, "CHECKLIST"]];
const KW_STOP = new Set(["star", "stars", "stat", "stats", "smart", "stark", "tart", "starts", "same", "came", "game", "fame", "lame", "tame", "made", "dame", "nam", "alter", "afer", "hater"]);
function editDist(a, b) {   // Damerau-Levenshtein (adjacent swaps count as one edit)
  const d = Array.from({ length: a.length + 1 }, (_, i) => [i, ...Array(b.length).fill(0)]);
  for (let j = 1; j <= b.length; j++) d[0][j] = j;
  for (let i = 1; i <= a.length; i++) for (let j = 1; j <= b.length; j++) {
    d[i][j] = Math.min(d[i - 1][j] + 1, d[i][j - 1] + 1, d[i - 1][j - 1] + (a[i - 1] === b[j - 1] ? 0 : 1));
    if (i > 1 && j > 1 && a[i - 1] === b[j - 2] && a[i - 2] === b[j - 1]) d[i][j] = Math.min(d[i][j], d[i - 2][j - 2] + 1);
  }
  return d[a.length][b.length];
}
function matchKeyword(text) {
  for (const [re, kw] of KW_ML) if (re.test(text)) return kw;
  const w = (text.toLowerCase().match(/[a-z]+/g) || []);
  const toks = [...w, ...w.slice(1).map((x, i) => w[i] + x)];   // "check list" -> "checklist"
  const long = w.length > 4;   // in a long comment only a clear keyword counts, and "after" only when written AFTER
  for (const t of toks) for (const kw of KEYWORDS) if (t === kw.toLowerCase() && !(long && kw === "AFTER" && !/\bAFTER\b/.test(text))) return kw;   // exact first
  for (const t of toks) {
    if (t.length < 3 || KW_STOP.has(t)) continue;
    for (const kw of long ? ["CHECKLIST"] : KEYWORDS) if (editDist(t, kw.toLowerCase()) <= (kw.length >= 8 ? 2 : 1)) return kw;
  }
  return null;
}
// Tap-to-reply buttons (Instagram quick replies, max 13, title max 20 chars). A tap arrives as a normal text message.
const qr = titles => titles.map(t => ({ content_type: "text", title: t, payload: t.toUpperCase() }));
async function sendMsg(env, recipient, text, buttons = []) {
  const msg = buttons.length ? { text, quick_replies: qr(buttons) } : { text };
  try { return await graph(env, `${env.IG_USER_ID}/messages`, { recipient: JSON.stringify(recipient), message: JSON.stringify(msg) }); }
  catch (e) {   // if Instagram rejects the buttons, still deliver the text
    if (!buttons.length) throw e;
    await log(env, `buttons rejected, sent plain text: ${e.message}`);
    return graph(env, `${env.IG_USER_ID}/messages`, { recipient: JSON.stringify(recipient), message: JSON.stringify({ text }) });
  }
}
async function sendDM(env, to, text, buttons = []) { return sendMsg(env, { id: to }, text, buttons); }
async function opsOk(env, key) {
  if (!key) return false;
  const h = [...new Uint8Array(await crypto.subtle.digest("SHA-256", new TextEncoder().encode(key)))].map(b => b.toString(16).padStart(2, "0")).join("");
  return h === env.OPS_KEY_SHA256;
}
async function mediaToItem(env, mediaId) {
  const posted = await kv(env, "posted", {});
  const hit = Object.entries(posted).find(([, p]) => p.media === mediaId);
  return hit ? hit[0] : `media:${mediaId}`;
}
async function bumpPost(env, item, field, n = 1) {        // live engagement counters per post
  const k = `ev:${item}`; const e = await kv(env, k, { comments: 0, keyword: {}, leads: 0, dms: 0 });
  if (field.startsWith("kw:")) { const w = field.slice(3); e.keyword[w] = (e.keyword[w] || 0) + n; } else e[field] = (e[field] || 0) + n;
  await kvPut(env, k, e);
}

async function handleWebhook(env, body) {
  const n = (body.entry || []).reduce((t, e) => [t[0] + (e.messaging || []).length, t[1] + (e.changes || []).length], [0, 0]);
  await log(env, `webhook in: ${body.object || "?"} ${n[0]} message(s), ${n[1]} change(s) ${(body.entry || []).flatMap(e => (e.changes || []).map(c => c.field)).join(",")}`);
  for (const entry of body.entry || []) {
    for (const ev of entry.messaging || []) {
      if (ev.postback && !ev.message) ev.message = { text: ev.postback.title || ev.postback.payload || "" };   // button taps of other kinds
      if (!ev.message || ev.message.is_echo || !ev.message.text) continue;
      const uid = ev.sender.id; const key = `t:${uid}`; const thread = await kv(env, key, []);
      const meta = await kv(env, `m:${uid}`, { first: Date.now(), sources: [] });
      meta.last_in = Date.now();                                     // 24h window starts from their last message
      if (ev.message.reply_to?.story?.id) meta.sources.push({ via: "story_reply", media: ev.message.reply_to.story.id, t: Date.now() });
      if (!meta.sources.length) meta.sources.push({ via: "dm", t: Date.now() });
      await kvPut(env, `m:${uid}`, meta);
      const src = meta.sources[0]; if (src.media) await bumpPost(env, await mediaToItem(env, src.media), "dms");
      thread.push({ role: "user", content: ev.message.text });
      const prof = await igProfile(env, uid);                         // username + whether they follow us (null if Instagram won't say)
      if (prof.username && !meta.username) meta.username = prof.username;
      if (!meta.pending_kw && meta.username) {                        // keyword comment whose private reply Instagram refused: they DM'd us instead
        const pk = await env.STATE.get(`pk:${meta.username.toLowerCase()}`);
        if (pk) { meta.pending_kw = pk; await env.STATE.delete(`pk:${meta.username.toLowerCase()}`); }
      }
      if (!meta.pending_kw) {   // keyword typed straight into DMs or as a story reply (contact stories ask for this)
        const dk = ev.message.text.trim().split(/\s+/).length <= 4 ? matchKeyword(ev.message.text) : null;
        if (dk) { meta.pending_kw = dk; meta.follow_asks = 0; await log(env, `keyword ${dk} via DM from @${meta.username || uid}`); }
      }
      let reply, buttons = [];
      if (meta.pending_kw && KEYWORD_REPLY[meta.pending_kw]) {
        // soft follow gate: ask to follow, re-check when they say they did, and after two tries send it anyway (never block a lead)
        if (prof.follows === false && (meta.follow_asks || 0) < 2) {
          meta.follow_asks = (meta.follow_asks || 0) + 1;
          reply = meta.follow_asks === 1 ? FOLLOW_ASK : FOLLOW_RECHECK; buttons = ["I've followed ✅"];
          await log(env, `follow check @${meta.username || uid}: not following (ask ${meta.follow_asks})`);
        } else {
          const pre = prof.follows === false ? "No worries, here it is anyway! 😊" : prof.follows && meta.follow_asks ? "Thanks for following! 🙌 Here you go!" : "";
          reply = pre ? KEYWORD_REPLY[meta.pending_kw].replace(/^Here you go!/, pre) : KEYWORD_REPLY[meta.pending_kw];
          buttons = NEXT_BUTTONS;
          await log(env, `sent ${meta.pending_kw} resource to @${meta.username || uid} (follows: ${prof.follows})`);
          delete meta.pending_kw; meta.follow_asks = 0;
        }
        await kvPut(env, `m:${uid}`, meta);
      } else { await kvPut(env, `m:${uid}`, meta); reply = await botReply(env, thread); }
      thread.push({ role: "assistant", content: reply });
      await kvPut(env, key, thread); await sendDM(env, uid, reply, buttons);
      if (/\d{10}/.test(ev.message.text.replace(/\D/g, "")) || thread.length >= 12) {
        const lead = await extractLead(env, thread);
        if (lead) {
          const leads = await kv(env, "leads", {}); const prev = leads[uid];
          const meta2 = await kv(env, `m:${uid}`, { sources: [] }); const s0 = meta2.sources[0] || {};
          const fromItem = s0.media ? await mediaToItem(env, s0.media) : "direct";
          leads[uid] = { ...lead, ig_user: uid, source_item: fromItem, source_keyword: s0.keyword || null, source_via: s0.via || "dm", status: prev?.status || "new", updated: IST().toISOString().slice(0, 16) };
          await kvPut(env, "leads", leads); await log(env, `lead ${uid}: ${lead.intent}/${lead.can_afford_30k} from ${fromItem}`);
          if (!prev) await bumpPost(env, fromItem, "leads");
          if (lead.phone && (!prev || !prev.phone) && lead.intent !== "low") {
            await discord(env, `🔔 **New ${lead.intent.toUpperCase()}-intent lead** (budget fit: ${lead.can_afford_30k})\n📞 ${lead.phone}  ·  🗣 ${lead.language || "?"}\n🏢 ${lead.business}\n📍 Came from: ${fromItem}${s0.keyword ? " (" + s0.keyword + ")" : ""}\n👥 ${lead.founders}${lead.nri ? " (NRI)" : ""}\n📈 ${lead.traction}\n⏱ ${lead.timeline}\nWhy: ${lead.reason}\nLead ID: ${uid}\nAfter your call, tell Claude: "lead ${uid}: <what happened>"`);
          }
        }
      }
    }
    for (const ch of entry.changes || []) { // keyword comments -> one private reply opens the DM
      if (ch.field !== "comments" || !ch.value?.text) continue;
      const who = ch.value.from?.username || ch.value.from?.id || "?";
      await log(env, `comment from @${who}${ch.value.parent_id ? " (reply in thread)" : ""}: ${ch.value.text.slice(0, 60)}`);
      if ((ch.value.from?.id && ch.value.from.id === env.IG_USER_ID) || (ch.value.from?.username || "").toLowerCase() === OWN_USERNAME) continue;   // our own comments
      const item = await mediaToItem(env, ch.value.media?.id); await bumpPost(env, item, "comments");
      const k0 = matchKeyword(ch.value.text); if (!k0) continue; const m = [k0, k0];
      await bumpPost(env, item, "kw:" + m[1].toUpperCase());
      if (ch.value.from?.id) {                                       // remember where this person came from, per keyword
        const mk = `m:${ch.value.from.id}`; const meta = await kv(env, mk, { first: Date.now(), sources: [] });
        if (!meta.sources.some(s => s.comment === ch.value.id)) meta.sources.push({ via: "comment", keyword: m[1].toUpperCase(), media: ch.value.media?.id, item, comment: ch.value.id, t: Date.now() });
        await kvPut(env, mk, meta);
      }
      const kw = m[1].toUpperCase();
      try {
        const r = await sendMsg(env, { comment_id: ch.value.id }, KEYWORD_OPENER[kw], ["Yes, send it 👍"]);
        if (r.recipient_id) { const mk = `m:${r.recipient_id}`; const meta = await kv(env, mk, { first: Date.now(), sources: [] });
          meta.pending_kw = kw; if (!meta.sources.length) meta.sources.push({ via: "comment", keyword: kw, media: ch.value.media?.id, item, comment: ch.value.id, t: Date.now() }); await kvPut(env, mk, meta); }
        await log(env, `private reply to ${kw} comment`);
        try { await graph(env, `${ch.value.id}/replies`, { message: PUBLIC_DONE[Math.floor(Math.random() * PUBLIC_DONE.length)] }); } catch (e3) { await log(env, `public note failed: ${e3.message}`); }
      }
      catch (e) {   // Instagram refuses some private replies (e.g. replies inside a thread): answer publicly and invite a DM
        await log(env, `private reply failed, replying publicly: ${e.message}`);
        if (ch.value.from?.username) await env.STATE.put(`pk:${ch.value.from.username.toLowerCase()}`, kw, { expirationTtl: 7 * 86400 });
        try { await graph(env, `${ch.value.id}/replies`, { message: PUBLIC_REPLY }); await log(env, `public reply to ${m[1]} comment`); }
        catch (e2) { await log(env, `comment reply failed: ${e2.message}`); }
      }
    }
  }
}

// Fixed, fully automatic first replies. Each keyword delivers what the post promised, with no human work.
// Legal content only from the checked fact list; no prices; no promise of a manual availability check.
const OWN_USERNAME = "rejectionlist.kerala";
const PUBLIC_REPLY = "Thanks! 🙌 Message us \"Hi\" (tap Message on our profile, or search rejectionlist.kerala in your DMs) and we'll send it right away.";
// Public note under the comment (varied so it never looks like a copy-paste bot) tells people where the DM is.
const PUBLIC_DONE = [
  "Sent you a DM 📩 Not in your inbox? Check message requests, including hidden requests / spam.",
  "Just messaged you! 📩 If you can't see it, look in message requests or the hidden requests (spam) folder.",
  "Check your DMs 📩 Instagram sometimes puts it under requests or hidden requests, so peek there too.",
];
const FOLLOW_ASK = "Almost there! 🙌 Please follow @rejectionlist.kerala (we share a useful company-registration tip every day), then tap the button below and we'll send it right away.";
const FOLLOW_RECHECK = "Hmm, we can't see your follow yet 🤔 Open our profile, tap Follow, then tap the button again.";
const NEXT_BUTTONS = ["Talk to our team", "Which type suits me?", "Documents needed"];
// First private reply is short and asks for a reply: a reply moves the chat into their main inbox,
// then the full resource (KEYWORD_REPLY) follows.
const KEYWORD_OPENER = {
  START: "Hi! 👋 Thanks for your comment. Want a quick guide on which company type suits you: OPC, Private Limited or LLP? Tap the button below.",
  NAME: "Hi! 👋 Thanks for your comment. Want our tips to keep your company name from getting rejected? Tap the button below.",
  AFTER: "Hi! 👋 Thanks for your comment. Want the checklist for the first 180 days after registration? Tap the button below.",
  CHECKLIST: "Hi! 👋 Thanks for your comment. Want the list of documents you need for registration? Tap the button below.",
};
const KEYWORD_REPLY = {
  START: "Here you go!\n\nIn short:\n• Starting alone: OPC (One Person Company)\n• 2+ founders, may raise funding later: Private Limited\n• Partners, no funding plans: LLP is also an option\n\nWe'll help you pick the right one. What does your business do?",
  NAME: "Here you go! How to keep your company name from being rejected:\n\n1. It must not be similar (even in sound) to an existing company or LLP name\n2. It must not clash with a registered trademark\n3. Words like Bank or Insurance need special approval\n4. Keep 2–3 backup names ready\n\nSend us the name you have in mind and we'll give a first review against these rules. Final availability is confirmed when the application is filed.",
  AFTER: "Here you go! Your checklist after registration:\n\n✅ Within 30 days: appoint the first auditor\n✅ Open a current account in the company's name\n✅ Within 180 days: file the commencement of business declaration (INC-20A). Missing it means a penalty of Rs 50,000 on the company\n✅ Annual filings every year, even with zero revenue. Late fee of Rs 100 per day per form\n\nHow long ago was your company registered?",
  CHECKLIST: "Here you go! Documents needed for registration:\n\n📄 For each director: PAN, Aadhaar/ID, address proof (bank statement or utility bill), photo\n🏠 For the office: a recent electricity/water bill + owner's NOC (your home works too)\n📝 2–3 company name options\n\nA Private Limited needs at least 2 directors (one must live in India). How many founders are there?",
};

const postKind = (env, what) => what === "reel" ? postReel(env) : what === "story" ? postStory(env) : postCarousel(env);

// ---------------- entry points ----------------
export default {
  async scheduled(ev, env, ctx) {
    const now = IST(); const h = now.getUTCHours(), mi = now.getUTCMinutes();
    const slot = SLOTS_IST.find(([sh, sm]) => sh === h && Math.abs(sm - mi) < 5);
    const day = now.toISOString().slice(0, 10);
    try {
      if (slot) {
        const k = `slot:${day}:${slot[0]}:${slot[1]}`;
        if (!(await env.STATE.get(k))) {
          await env.STATE.put(k, "1", { expirationTtl: 172800 });
          try { await postKind(env, slot[2]); }
          catch (e) {   // one retry ~10 min later covers most temporary Instagram errors
            await kvPut(env, "retry", { what: slot[2], at: Date.now() + 10 * 60e3 });
            await log(env, `ERROR ${slot[2]} post failed, retrying in 10 min: ${e.message}`);
            await discord(env, `⚠️ ${slot[2]} post failed, retrying in 10 min: ${e.message}`);
          }
        }
      }
      const retry = await kv(env, "retry", null);
      if (retry && Date.now() >= retry.at) {
        await env.STATE.delete("retry");
        try { await postKind(env, retry.what); await log(env, `retry of ${retry.what} succeeded`); }
        catch (e) { throw new Error(`${retry.what} retry also failed: ${e.message}`); }
      }
      if (h === 3 && mi < 5) { await snapshot(env); await optimise(env); }
      if (h === 21 && mi >= 40 && mi < 45) {
        const posted = await kv(env, "posted", {}); const today = Object.values(posted).filter(p => IST(new Date(p.t)).toISOString().slice(0, 10) === day).length;
        const leads = Object.values(await kv(env, "leads", {})).filter(l => (l.updated || "").startsWith(day));
        const errs = (await kv(env, "log", [])).filter(l => l.startsWith(day) && /ERROR|NO .*STOCK/.test(l)).length;
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
    if (u.pathname.startsWith("/ops/")) {
      if (!(await opsOk(env, req.headers.get("x-ops-key")))) return new Response("no", { status: 403 });
      if (u.pathname === "/ops/leads") return json(await kv(env, "leads", {}));
      if (u.pathname === "/ops/insights") {
        const posted = await kv(env, "posted", {}); const out = {};
        for (const id of Object.keys(posted)) out[id] = { posted: posted[id], events: await kv(env, `ev:${id}`, null), snapshots: await kv(env, `snap:${id}`, []) };
        return json({ weights: await kv(env, "weights", null), slot_report: await kv(env, "slot_report", null), posts: out });
      }
      if (u.pathname === "/ops/thread") { const id = u.searchParams.get("id"); return json({ meta: await kv(env, `m:${id}`, null), thread: await kv(env, `t:${id}`, []) }); }
      if (u.pathname === "/ops/followup" && req.method === "POST") {          // send one DM if still inside the 24h window
        const { id, text, status, note } = await req.json(); const meta = await kv(env, `m:${id}`, null);
        const leads = await kv(env, "leads", {}); if (leads[id]) { leads[id].status = status || leads[id].status; leads[id].notes = [...(leads[id].notes || []), { t: IST().toISOString().slice(0, 16), note }]; await kvPut(env, "leads", leads); }
        if (!text) return json({ ok: true, sent: false, reason: "status only" });
        const left = meta?.last_in ? 24 * 3600e3 - (Date.now() - meta.last_in) : -1;
        if (left <= 0) return json({ ok: false, sent: false, reason: "outside Instagram 24h window", hours_since_last_message: meta?.last_in ? (Date.now() - meta.last_in) / 3600e3 : null });
        await sendDM(env, id, text); const t = await kv(env, `t:${id}`, []); t.push({ role: "assistant", content: text }); await kvPut(env, `t:${id}`, t);
        await log(env, `follow-up sent to ${id}`); return json({ ok: true, sent: true, hours_left_in_window: left / 3600e3 });
      }
      if (u.pathname === "/ops/run" && req.method === "POST") { const { what } = await req.json(); if (what === "snapshot") await snapshot(env); if (what === "optimise") await optimise(env);
        if (what === "reel") await postReel(env); if (what === "story") await postStory(env); if (what === "carousel") await postCarousel(env); return json({ ok: true }); }
      if (u.pathname === "/ops/status") return json({ now_ist: IST().toISOString(), posted: await kv(env, "posted", {}), log: (await kv(env, "log", [])).slice(0, 80) });
    }
    if (u.pathname === "/public/posted") return json([...Object.keys(await kv(env, "posted", {})), ...Object.keys(await kv(env, "stories", {}))]); // builder reads this to know stock (reels, carousels, stories)
    if (u.searchParams.get("key") !== env.ADMIN_KEY) return new Response("rl-kerala autopilot", { status: 200 });
    if (u.pathname === "/status") return json({ weights: await kv(env, "weights", null), posted: Object.keys(await kv(env, "posted", {})).length, log: (await kv(env, "log", [])).slice(0, 60) });
    if (u.pathname === "/leads") return json(await kv(env, "leads", {}));
    if (u.pathname === "/reset/test") {   // wipe log, chats, people, engagement counters and leads (keeps posting history)
      let n = 0;
      for (const prefix of ["t:", "m:", "ev:", "alert:", "pk:"]) {
        let cur; do { const l = await env.STATE.list({ prefix, cursor: cur }); for (const k of l.keys) { await env.STATE.delete(k.name); n++; } cur = l.list_complete ? null : l.cursor; } while (cur);
      }
      for (const k of ["log", "leads", "retry"]) { await env.STATE.delete(k); n++; }
      return json({ ok: true, deleted: n });
    }
    if (u.pathname === "/run/reel") { await postReel(env); return json({ ok: true, log: (await kv(env, "log", [])).slice(0, 3) }); }
    if (u.pathname === "/run/carousel") { await postCarousel(env); return json({ ok: true, log: (await kv(env, "log", [])).slice(0, 3) }); }
    if (u.pathname === "/run/story") { await postStory(env); return json({ ok: true, log: (await kv(env, "log", [])).slice(0, 3) }); }
    if (u.pathname === "/run/optimise") { await optimise(env); return json(await kv(env, "weights", null)); }
    return new Response("not found", { status: 404 });
  },
};

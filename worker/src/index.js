// rl-kerala-autopilot: runs 24/7 on Cloudflare, independent of Claude.
//  - cron: posts reels (with cover, trial reels when allowed) and Stories at IST slots from the GitHub Pages library
//  - cron: pulls insights daily and rewrites content-mix weights (optimiser)
//  - webhook: answers Instagram DMs / keyword comments with a English qualifying bot, stores leads
// Secrets (wrangler secret / dashboard): IG_TOKEN, IG_USER_ID, VERIFY_TOKEN, ADMIN_KEY
// Vars: LIB_BASE (GitHub Pages base URL of library/), GRAPH (graph API base)
// KV binding: STATE

// Daily volume rises in stages (owner's plan, Nov 2026). A stage starts on its date unless KV "stage_hold" is set
// (the monitor sets it when reach per post drops sharply or Instagram flags the account), or KV "stage_force" picks one.
// Three topics share the one account but are run as if each had its own: own stages, stock, keywords, DM flow and lead label.
// co = company registration (since 1 Nov), gst = GST registration and inv = investor agreements (both from 20 Nov, same ramp).
// 19 Nov data: after 114 posts the account has 1 follower; reels reach ~100-130 non-followers each, carousels and stories
// reach 0-2 (they are shown to followers). So until 100 followers each topic keeps 2 carousels + 3 stories and the
// quota goes to reels. The 100-follower check raises carousels/stories back to 5 (KV "low_reach_mode" = "0").
const RAMP = (d0, d1, d2, d3, d4) => [
  { from: d0, reel: 5, carousel: 5, story: 5, poster: 0 },
  // owner, 13 Nov: 0 followers so carousels/posters reach ~nobody; keep them at stage-0 numbers and give the planned increase to reels
  { from: d1, reel: 13, carousel: 5, story: 5, poster: 0 },
  { from: d2, reel: 21, carousel: 5, story: 5, poster: 0 },
  { from: d3, reel: 29, carousel: 5, story: 5, poster: 0 },
  { from: d4, reel: 35, carousel: 5, story: 5, poster: 0 },
];
const LOW_REACH = { carousel: 2, story: 3 };
// ---- SEVEN MORE TOPICS (owner, 19 Nov evening): same plan, goal and automation as company registration --------------
// Each entry fills TOPICS, keywords, DM bot, fallback questions, buttons, keyword replies and lead fields below.
const Q_END = ["Could you share a phone number so our team can call you?", "Would you prefer the call in Malayalam or English?", "Thank you! 🙏 Our team will call you shortly."];
const NEWT = {
  tm: { label: "TRADEMARK", noun: "trademark registration", shift: 3,
    about: "registers trademarks (brand names and logos) in India",
    facts: "A trademark application is filed with the Trade Marks Registry; once filed you may use the TM symbol, and the R symbol only after registration. There are 45 classes of goods and services and you file in the classes you trade in. After examination an objection may come, which must be answered within 30 days; after publication in the journal anyone can oppose within 4 months. A registered trademark lasts 10 years and can be renewed. Getting a company name approved does NOT protect the brand; only a trademark does. Never promise registration.",
    qs: ["What is the brand name or logo, and what does your business sell or do?", "Is the business a proprietorship, partnership, LLP or company? Is it already using the brand?", "Have you checked if anyone else uses a similar name?", "How soon do you want to file?"],
    next: ["Talk to our team", "Can I use TM now?", "Name vs trademark?"],
    kws: { TRADEMARK: ["Want our quick guide to protecting your brand name with a trademark?", "Here you go! Trademark in short:\n\n™ You can use TM once you file; ® only after registration\n📂 45 classes: you file in the classes you sell in\n⏱ Objection replies within 30 days; anyone can oppose within 4 months of publication\n🔁 Valid 10 years, renewable\n⚠️ A company name approval does NOT protect your brand\n\nWhat is your brand name, and what do you sell?"],
           BRAND: ["Want the checklist to make sure nobody can copy your brand name?", "Here you go! Protecting your brand:\n\n1. Search for similar marks before you print anything\n2. File a trademark in the right class (45 classes)\n3. Use ™ after filing, ® only after registration\n4. Renew every 10 years\n\nYour company or domain name alone does not stop someone else using the brand. What is your brand name?"] } },
  roc: { label: "ROC COMPLIANCE", noun: "ROC annual compliance", shift: 9,
    about: "handles ROC annual compliance for private limited companies and LLPs",
    facts: "A private limited company holds its AGM by 30 September, files AOC-4 (financial statements) within 30 days of the AGM and MGT-7/7A (annual return) within 60 days of the AGM; every director files DIR-3 KYC by 30 September. Late filing costs Rs 100 per day per form, with no upper limit. INC-20A is due within 180 days of incorporation and the first auditor within 30 days. Not filing for 3 years can disqualify directors for 5 years and the company can be struck off. An LLP files Form 11 by 30 May and Form 8 by 30 October. These are due even if the company had no business.",
    qs: ["Is it a private limited company or an LLP, and when was it registered?", "Which filings are done so far, and are any pending or late?", "Did the company have any business or bank transactions this year?", "How soon do you want everything up to date?"],
    next: ["Talk to our team", "No business, still file?", "What's the late fee?"],
    kws: { ROC: ["Want the yearly ROC filing calendar for your company?", "Here you go! Yearly ROC filings for a private limited company:\n\n📅 AGM by 30 September\n📄 AOC-4 within 30 days of the AGM\n📄 MGT-7/7A within 60 days of the AGM\n🪪 DIR-3 KYC for every director by 30 September\n⚠️ Late: Rs 100 per day per form, no upper limit\n🚫 3 years unfiled: directors can be disqualified for 5 years\n\nDue even if there was no business. Is your company a Pvt Ltd or an LLP?"],
           FILING: ["Want the list of filings a company must do even with zero business?", "Here you go! Even with zero business, a company files:\n\n📄 AOC-4 and MGT-7/7A every year\n🪪 DIR-3 KYC for every director\n🧾 Income tax return\n⚠️ Each ROC form late = Rs 100 a day, no cap\n\nAn LLP files Form 11 (by 30 May) and Form 8 (by 30 October). When was your company registered?"] } },
  fssai: { label: "FSSAI", noun: "FSSAI food registration / licence", shift: 15,
    about: "gets FSSAI registration and licences for food businesses",
    facts: "Every food business needs FSSAI: basic registration for turnover up to Rs 12 lakh a year (including home bakers and small sellers), a state licence up to Rs 20 crore, and a central licence above that or for importers and some other categories. The 14-digit FSSAI number must be printed on packaged food labels. Selling food without registration or licence can be punished with a penalty of up to Rs 5 lakh and imprisonment of up to 6 months. Registration and licences are valid for 1 to 5 years and must be renewed. Never promise approval.",
    qs: ["What food do you make or sell, and from where (home, shop, kitchen, online)?", "Roughly what is your yearly turnover?", "Do you sell packaged food, or sell through Swiggy, Zomato, Amazon or other states?", "How soon do you need the FSSAI number?"],
    next: ["Talk to our team", "Home bakers too?", "Registration or licence?"],
    kws: { FSSAI: ["Want our quick guide on which FSSAI registration your food business needs?", "Here you go! Which FSSAI do you need?\n\n🥘 Basic registration: turnover up to Rs 12 lakh a year (home bakers too)\n🏪 State licence: up to Rs 20 crore\n🏭 Central licence: above that, and importers\n🏷 Print the 14-digit FSSAI number on packaged food\n⚠️ Selling without it: penalty up to Rs 5 lakh\n\nWhat food do you make or sell?"],
           FOOD: ["Want the checklist for selling food legally from home or a shop?", "Here you go! Selling food legally:\n\n1. FSSAI registration (up to Rs 12 lakh turnover) or licence\n2. FSSAI number on every packet\n3. Renew before it expires (1-5 years)\n4. Food delivery apps ask for the FSSAI number before listing you\n\nWhat food do you sell, and from home or a shop?"] } },
  iec: { label: "IEC (IMPORT-EXPORT)", noun: "IEC import-export registration", shift: 21,
    about: "gets the Import Export Code (IEC) from DGFT for businesses that import or export",
    facts: "The IEC is a 10-digit code issued by DGFT, linked to the business PAN; it is needed to import or export goods, and customs and banks ask for it. One IEC covers the whole business (one PAN). It does not expire, but it must be updated online every year between April and June, otherwise it is deactivated. Exporters of services need it to claim export benefits. Import or export for personal use does not need it. Never promise approval or export incentives.",
    qs: ["What do you want to import or export, and to or from which country?", "Is the business a proprietorship, partnership, LLP or company? Does it have GST?", "Is this your first shipment, or are you already trading?", "How soon is the first shipment?"],
    next: ["Talk to our team", "Do I need IEC?", "Yearly update?"],
    kws: { IEC: ["Want our quick guide to the Import Export Code (IEC)?", "Here you go! IEC in short:\n\n🌍 10-digit code from DGFT, linked to your business PAN\n📦 Needed to import or export goods; customs and banks ask for it\n🔁 Never expires, but must be updated every year between April and June or it is deactivated\n🙋 Not needed for personal-use imports\n\nWhat do you want to import or export?"],
           EXPORT: ["Want the checklist before your first export order?", "Here you go! Before your first export:\n\n1. IEC (Import Export Code) from DGFT\n2. GST registration for the business\n3. A current account that can receive foreign payments\n4. Update the IEC every April-June\n\nWhat do you want to export, and to which country?"] } },
  nda: { label: "NDA", noun: "NDA (non-disclosure agreement)", shift: 27,
    about: "drafts NDAs (non-disclosure agreements) for businesses and founders",
    facts: "An NDA is a contract that is enforceable in India if it is properly drafted and stamped as per the state's stamp law. It can be one-way or mutual. A good NDA defines what is confidential, what is excluded (already public, independently developed), how long the duty lasts, and the remedies, such as an injunction. An NDA cannot protect information that is already public. Many investors do not sign NDAs at the pitch stage, so share only what you are comfortable with. Never promise an outcome in a dispute.",
    qs: ["Who will you share information with: an employee, freelancer, vendor, partner or investor?", "What do you need to protect: an idea, code, designs, client lists, recipes, something else?", "One-way NDA or mutual (both sides share)?", "How soon do you need it?"],
    next: ["Talk to our team", "One-way or mutual?", "Will investors sign?"],
    kws: { NDA: ["Want our guide to what a strong NDA must have?", "Here you go! A strong NDA has:\n\n🔒 A clear definition of what is confidential\n🚫 Exclusions (already public, independently developed)\n⏱ How long the duty lasts\n⚖️ Remedies, such as an injunction\n🧾 Proper stamping as per the state's stamp law\n\nAn NDA cannot protect what is already public. Who will you share information with?"],
           SECRET: ["Want the checklist before sharing your idea with anyone?", "Here you go! Before you share your idea:\n\n1. Decide what must stay secret (code, recipe, client list, design)\n2. Get an NDA signed, one-way or mutual\n3. Share only what that person needs\n4. Note: many investors won't sign NDAs at pitch stage, so pitch the what, not the how\n\nWho are you about to share it with?"] } },
  cfa: { label: "CO-FOUNDER AGREEMENT", noun: "co-founder agreement", shift: 33,
    about: "drafts co-founder agreements (equity split, vesting, roles, IP and exits)",
    facts: "A co-founder agreement records the equity split, vesting (a common practice is 4 years with a 1-year cliff), roles and decision-making, assignment of all IP to the company, what happens when a founder leaves (buy-back of unvested shares), and dispute resolution. In India a non-compete that applies after someone leaves is generally not enforceable, but confidentiality and non-solicitation can be. For share rights to bind the company they should also be reflected in the shareholders' agreement and the articles. Never decide the split for them.",
    qs: ["How many co-founders are there, and have you agreed a split yet?", "Is the company registered yet (Pvt Ltd, LLP or not yet)?", "Who built what so far (idea, code, money, clients)?", "How soon do you want the agreement signed?"],
    next: ["Talk to our team", "What is vesting?", "If one leaves?"],
    kws: { COFOUNDER: ["Want our checklist of what every co-founder agreement must cover?", "Here you go! A co-founder agreement covers:\n\n📊 Equity split\n⏳ Vesting (commonly 4 years with a 1-year cliff)\n🧭 Roles and who decides what\n💡 All IP owned by the company\n🚪 What happens if a founder leaves (unvested shares come back)\n⚖️ How disputes are settled\n\nHow many co-founders are you?"],
           VESTING: ["Want to know how vesting protects co-founders?", "Here you go! Vesting in short:\n\n⏳ Shares are earned over time (commonly 4 years)\n🧱 A 1-year cliff: leave before 1 year and you keep none\n🚪 Leave later and unvested shares come back to the company\n\nWithout vesting, a co-founder who leaves in month 6 can keep their full share. Have you agreed your split yet?"] } },
  fp: { label: "FINANCIAL PROJECTIONS", noun: "financial projections", shift: 39,
    about: "prepares investor-ready financial projections: a 3-year revenue and expense forecast with P&L, cash flow and the assumptions behind it",
    facts: "Investors, banks and grant panels ask for financial projections. A good set covers 3 years month by month for year 1, with revenue drivers (customers, price, growth), costs and hiring, a P&L, cash flow and break-even, plus the assumptions written down so they can be questioned. Projections must be realistic and tied to traction; inflated numbers lose credibility with investors. Banks may ask for a project report for loans. Never state our fee for this service; the team quotes on the call.",
    qs: ["What does your business do, and is it already earning revenue?", "What are the projections for: an investor, a bank loan, a grant, or your own planning?", "Do you have past numbers (sales, costs) we can build on?", "By when do you need them?"],
    next: ["Talk to our team", "What do investors check?", "For a bank loan?"],
    kws: { PROJECTION: ["Want the checklist of what investors look for in financial projections?", "Here you go! Investor-ready projections have:\n\n📈 3 years: month by month for year 1\n👥 Revenue drivers: customers, price, growth\n💸 Costs and hiring plan\n📊 P&L, cash flow and break-even point\n📝 Assumptions written down\n\nInflated numbers lose investors' trust; tie them to your traction. Is your business earning revenue yet?"],
           FORECAST: ["Want to know how to build a 3-year revenue and expense forecast?", "Here you go! A 3-year forecast in 4 steps:\n\n1. Start from real numbers (sales, costs) if you have them\n2. Set drivers: customers per month, price, growth\n3. Add costs, salaries and one-time spends\n4. Check cash flow: when does money run out, when do you break even?\n\nWho is it for: an investor, a bank or a grant?"] } },
  val: { label: "COMPANY VALUATION", noun: "company valuation", shift: 45,
    about: "prepares company and share valuation reports for any purpose: raising investment, ESOPs, share transfers, a partner's exit, buy-backs, mergers, NRI or foreign investment, loans or disputes",
    facts: "A valuation is needed when raising investment, issuing ESOPs, transferring shares, a founder or partner exits, a buy-back or merger, and for NRI or foreign investment. When a company issues shares by preferential allotment, the price must be backed by a valuation report from a registered valuer. For NRI or foreign investment on repatriation basis, shares cannot be issued below fair value worked out by an accepted method and certified by a CA, a SEBI-registered merchant banker or a cost accountant. Common methods are discounted cash flow (future cash flows), comparable companies or deals, and net asset value; early startups often rely on comparables and projections. A valuation is given for a specific purpose and date. Never state a value or our fee.",
    qs: ["What is the valuation for: raising money, ESOPs, a share transfer, a partner's exit, NRI/foreign investment, a loan or something else?", "Is the company a private limited company or an LLP, and roughly how old is it?", "Is it earning revenue yet? Do you have past financials or projections?", "By when do you need the report?"],
    next: ["Talk to our team", "Which method fits me?", "Who must sign it?"],
    kws: { VALUATION: ["Want our guide on when a company needs a valuation and which method fits?", "Here you go! When a company needs a valuation:\n\n💰 Raising investment, ESOPs, share transfers, a partner's exit, buy-backs, mergers\n🌍 NRI or foreign investment: shares can't be issued below fair value\n📜 Preferential allotment: a registered valuer's report is needed\n📐 Methods: discounted cash flow, comparable companies or deals, net asset value\n📅 A valuation is for a specific purpose and date\n\nWhat do you need the valuation for?"],
           WORTH: ["Want to know how investors decide what your company is worth?", "Here you go! How a company's worth is worked out:\n\n1. Future cash flows (discounted cash flow)\n2. What similar companies or deals were valued at\n3. The net value of assets\n\nEarly startups lean on comparables and projections, so good financial projections matter. What do you need the valuation for?"] } },
};

const TOPICS = {
  co: { label: "COMPANY REG", noun: "company registration", storyShift: 0, stages: RAMP("2026-11-01", "2026-11-14", "2026-11-21", "2026-11-28", "2026-12-05") },
  gst: { label: "GST", noun: "GST registration", storyShift: 12, stages: RAMP("2026-11-20", "2026-11-27", "2026-12-04", "2026-12-11", "2026-12-18") },
  inv: { label: "INVESTOR AGREEMENT", noun: "investor agreement", storyShift: 24, stages: RAMP("2026-11-20", "2026-11-27", "2026-12-04", "2026-12-11", "2026-12-18") },
  sui: { label: "STARTUP INDIA", noun: "Startup India (DPIIT) recognition", storyShift: 36, stages: RAMP("2026-11-20", "2026-11-27", "2026-12-04", "2026-12-11", "2026-12-18") },
  ud: { label: "UDYAM (MSME)", noun: "Udyam (MSME) registration", storyShift: 54, stages: RAMP("2026-11-20", "2026-11-27", "2026-12-04", "2026-12-11", "2026-12-18") },
  sk: { label: "KERALA STARTUP MISSION", noun: "Kerala Startup Mission registration", storyShift: 48, stages: RAMP("2026-11-20", "2026-11-27", "2026-12-04", "2026-12-11", "2026-12-18") },
};
for (const [t, c] of Object.entries(NEWT)) TOPICS[t] = { label: c.label, noun: c.noun, storyShift: c.shift, stages: RAMP("2026-11-20", "2026-11-27", "2026-12-04", "2026-12-11", "2026-12-18") };
const STAGES = TOPICS.co.stages;
const topicOf = x => (x && TOPICS[x.topic]) ? x.topic : "co";
// Instagram allows 100 API posts per rolling 24 h (stories count; checked 14 Nov: quota_total 100). Keep a margin for retries.
// When the topics together ask for more, posters go first, then carousels (down to 1 per topic, new topics first),
// then reels of the new topics; company registration's reels are never cut.
const DAILY_CAP = 96;
const STORY_TIMES = [[8, 10], [13, 5], [18, 10], [20, 15], [22, 10]];   // story logic picks teaser / tip / quiz / contact by hour
async function stageNow(env, day, topic = "co") {
  const ST = TOPICS[topic].stages, sfx = topic === "co" ? "" : "_" + topic;
  const f = await env.STATE.get("stage_force" + sfx); if (f !== null && ST[+f]) return { i: +f, ...ST[+f] };
  if (day < ST[0].from) return null;                                             // topic not started yet
  let i = 0; ST.forEach((st, k) => { if (day >= st.from) i = k; });
  for (const hk of ["stage_hold", "stage_hold" + sfx]) { const hold = await env.STATE.get(hk); if (hold !== null && +hold < i) i = +hold; }   // hold = highest stage allowed
  return { i, ...ST[i] };
}
// REEL-MAX MODE (owner, 19 Nov: "as many reels as the daily limit allows, stop carousels/stories if needed").
// While low_reach_mode is on (under 100 followers) and from 20 Nov: no carousels, stories or posters (they reach ~0 people
// without followers); every slot is a reel. The total ramps up over 4 days so the account isn't flagged for a sudden jump;
// the monitor can lower it with KV "reel_cap" if reach per reel drops. Reels are split by topic share and by built stock,
// so a topic with little stock never blocks the quota: its unused share goes to topics that have reels ready.
const REEL_RAMP = [["2026-11-20", 40], ["2026-11-21", 60], ["2026-11-22", 80]];   // owner, 19 Nov night: capped at 80 so tips + news fit under 100/24 h
// TIPS + NEWS (owner, 19 Nov night). On top of the reel split: one "tip" reel per topic per day (quick check, calendar,
// checklist, comparison, what-if), and NEWS_SLOTS slots for verified news / opportunity / correction reels (theme
// "news" | "opportunity" | "correction"). These themes are reserved: normal reel slots never use them. Empty slots post nothing.
const NEWS_SLOTS = 4;
const SPECIAL = ["tip", "news", "opportunity", "correction"];
const todayIST = () => IST().toISOString().slice(0, 10);
const live_ = i => !i.expires || i.expires >= todayIST();   // a news item is never posted after its "as of" deadline
// owner, 19 Nov: company-registration reels were starting to feel repetitive, so co drops to 25% and Udyam joins at 15%
// owner, 19 Nov evening: 13 topics, same goal each; company registration keeps a little more as the original topic
const REEL_SHARE = { co: 0.11, gst: 0.068, inv: 0.068, sui: 0.068, sk: 0.068, ud: 0.068, tm: 0.068, roc: 0.068, fssai: 0.068, iec: 0.068, nda: 0.068, cfa: 0.068, fp: 0.068, val: 0.068 };   // 14 topics
async function reelMaxPlan(env, day) {
  const ck = `plan2:${day}`; const cached = await kv(env, ck, null); if (cached) return cached;   // frozen once a day so slot times never move
  let total = 0; for (const [d, n] of REEL_RAMP) if (day >= d) total = n;
  const rc = await env.STATE.get("reel_cap"); if (rc !== null) total = Math.min(total, +rc);
  const m = await manifest(env); const posted = await kv(env, "posted", {});
  const avail = {}; for (const t of Object.keys(TOPICS)) avail[t] = 0;
  for (const i of m.items || []) if (!i.posted && !posted[i.id] && !SPECIAL.includes(i.theme)) avail[topicOf(i)]++;
  const live = Object.keys(TOPICS).filter(t => day >= TOPICS[t].stages[0].from);
  const plan = {}; for (const t of live) plan[t] = { reel: 0, carousel: 0, story: 0, poster: 0, tip: 1 };
  let left = total;   // pass 1: each topic its share, limited by stock; pass 2: hand leftovers to topics with stock, co first
  for (const t of live) { const n = Math.min(Math.floor(total * (REEL_SHARE[t] || 0)), avail[t]); plan[t].reel = n; left -= n; }
  const order = ["co", ...live.filter(x => x !== "co")]; let moved = true;   // leftovers one at a time, round-robin over topics that still have stock
  while (left > 0 && moved) { moved = false; for (const t of order) if (plan[t] && left > 0 && plan[t].reel < avail[t]) { plan[t].reel++; left--; moved = true; } }
  const P = { cap: total, mode: "reel-max", stages: {}, plan, news: NEWS_SLOTS, total: total - left, tips: live.length, stock: avail };
  await kvPut(env, ck, P); return P;
}
async function planDay(env, day) {
  if (day >= REEL_RAMP[0][0] && (await env.STATE.get("low_reach_mode")) !== "0") return reelMaxPlan(env, day);
  const cap = +(await env.STATE.get("daily_cap") || DAILY_CAP); const stages = {}, plan = {};
  const low = (await env.STATE.get("low_reach_mode")) !== "0";
  for (const t of Object.keys(TOPICS)) { const st = await stageNow(env, day, t); if (st) { stages[t] = st; plan[t] = { reel: st.reel, carousel: low ? Math.min(st.carousel, LOW_REACH.carousel) : st.carousel, story: low ? Math.min(st.story, LOW_REACH.story) : st.story, poster: st.poster }; } }
  const total = () => Object.values(plan).reduce((a, p) => a + p.reel + p.carousel + p.story + p.poster, 0);
  const order = Object.keys(plan).sort((a, b) => (a === "co") - (b === "co"));   // new topics trimmed first
  for (const t of order) while (total() > cap && plan[t].poster > 0) plan[t].poster--;
  let cut = true; while (total() > cap && cut) { cut = false; for (const t of order) if (total() > cap && plan[t].carousel > 1) { plan[t].carousel--; cut = true; } }
  const news = order.filter(t => t !== "co");
  cut = true; while (total() > cap && cut) { cut = false; for (const t of news) if (total() > cap && plan[t].reel > 1) { plan[t].reel--; cut = true; } }
  return { cap, stages, plan, total: total() };
}
function slotsFor(P) {   // P = planDay result (or one stage, old style). Feed posts spread 06:30-23:15 IST, topics and types interleaved
  if (!P.plan) P = { plan: { co: P } };
  const out = [];
  for (const [t, p] of Object.entries(P.plan)) STORY_TIMES.slice(0, p.story).forEach(([h, m]) => { const x = h * 60 + m + TOPICS[t].storyShift; out.push([Math.floor(x / 60), x % 60, "story", t]); });
  const feed = [];   // each post gets a position in its own topic+type series; merging by position interleaves everything evenly
  for (const [t, p] of Object.entries(P.plan)) for (const k of ["reel", "carousel", "poster", "tip"]) for (let j = 0; j < (p[k] || 0); j++) feed.push({ pos: k === "tip" ? 0.3 + 0.4 * ((Object.keys(P.plan).indexOf(t) + 0.5) / Object.keys(P.plan).length) : (j + 0.5) / p[k], k, t });
  for (let j = 0; j < (P.news || 0); j++) feed.push({ pos: (j + 0.5) / P.news, k: "news", t: "co" });
  feed.sort((a, b) => a.pos - b.pos || (a.t < b.t ? -1 : 1));
  const multi = Object.keys(P.plan).length > 1;   // company registration alone keeps its 07:05-22:45 day
  const tot = feed.length, start = multi ? 6 * 60 + 30 : 7 * 60 + 5, end = multi ? 23 * 60 + 15 : 22 * 60 + 45, storyMin = out.map(([h, m]) => h * 60 + m); let last = -99;
  const gap = tot > 40 ? 8 : 11, clear = tot > 40 ? 4 : 12;
  feed.forEach((f, k) => {
    let m = Math.round(start + (end - start) * (k + 0.5) / tot);
    while (storyMin.some(x => Math.abs(x - m) < clear) || m - last < gap) m++;
    last = m; out.push([Math.floor(m / 60), m % 60, f.k, f.t]);
  });
  return out.sort((a, b) => a[0] * 60 + a[1] - b[0] * 60 - b[1]);
}
// ---- FOLLOWER SHOUT-OUTS (owner, 19 Nov) --------------------------------------------------------------------------
// Only people who said YES are named, by @username only, never with what they asked about. Asked once (after their chat
// is complete, or when they comment/DM WELCOME). "remove me" / "no tag" switches it off for good.
// Each person gets one weekly welcome; a monthly "top supporters" post names the 3-5 most engaged (by distinct days),
// never the same person two months running. Batches of 20 (Instagram's tag limit), one post a day. Starts once the
// account has SHOUT_MIN followers (KV "shout_min", default 30). Factory renders the images from /public/shoutqueue.
const SHOUT_Q = "Quick one 🙏 Can we thank you by your Instagram username in our weekly welcome post? We only say thank you, never what you asked about.";
const SHOUT_BTN = ["Yes, tag me 🙌", "No thanks"];
const SHOUT_MIN = 30;
const SHOUT_CTA = "Want your name here next time? Comment WELCOME on any post or DM us 🙏";
async function shoutNote(env, uname, igsid, patch) {   // registry keyed by lowercase username
  if (!uname) return; const reg = await kv(env, "shout", {}); const k = uname.toLowerCase();
  const r = reg[k] || { u: uname, eng: {} }; if (igsid) r.id = igsid;
  if (patch === "engage") { const mo = IST().toISOString().slice(0, 7), d = IST().toISOString().slice(8, 10); const a = r.eng[mo] || []; if (a.includes(d)) return; a.push(d); r.eng[mo] = a; for (const m0 of Object.keys(r.eng)) if (m0 < IST(new Date(Date.now() - 70 * 86400e3)).toISOString().slice(0, 7)) delete r.eng[m0]; }
  else Object.assign(r, patch);
  reg[k] = r; await kvPut(env, "shout", reg);
}
async function shoutPlan(env) {   // Sunday 09:41: queue this week's welcomes (and on the first Sunday of a month, top supporters)
  let followers = 0; try { followers = (await graph(env, env.IG_USER_ID, { fields: "followers_count" }, "GET")).followers_count || 0; } catch (e) {}
  const min = +(await env.STATE.get("shout_min") || SHOUT_MIN); if (followers < min) { await log(env, `shout-outs waiting: ${followers}/${min} followers`); return; }
  const reg = await kv(env, "shout", {}); const queue = await kv(env, "shout_queue", []); const wk = IST().toISOString().slice(0, 10);
  const yes = Object.values(reg).filter(r => r.yes);
  const still = async r => { if (!r.id) return true; const p = await igProfile(env, r.id); return p.follows !== false; };
  const fresh = []; for (const r of yes.filter(r => !r.welcomed).sort((a, b) => (a.yes_t || 0) - (b.yes_t || 0))) { if (fresh.length >= 100) break; if (await still(r)) fresh.push(r); }
  for (let i = 0; i < fresh.length; i += 20) queue.push({ id: `sw${wk.replace(/-/g, "")}_${i / 20 + 1}`, kind: "welcome", names: fresh.slice(i, i + 20).map(r => r.u) });
  fresh.forEach(r => { reg[r.u.toLowerCase()].welcomed = wk; });
  if (+wk.slice(8, 10) <= 7) {   // first Sunday of the month: last month's top supporters
    const lm = IST(new Date(Date.now() - 20 * 86400e3)).toISOString().slice(0, 7), pm = IST(new Date(Date.now() - 50 * 86400e3)).toISOString().slice(0, 7);
    const top = yes.filter(r => (r.eng?.[lm] || []).length >= 2 && !(r.top || []).includes(pm)).sort((a, b) => (b.eng[lm] || []).length - (a.eng[lm] || []).length).slice(0, 5);
    if (top.length) { queue.push({ id: `st${lm.replace("-", "")}`, kind: "top", month: lm, names: top.map(r => r.u) }); top.forEach(r => { const x = reg[r.u.toLowerCase()]; x.top = [...(x.top || []), lm]; }); }
  }
  await kvPut(env, "shout", reg); await kvPut(env, "shout_queue", queue); await log(env, `shout-outs queued: ${fresh.length} welcomes`);
}
async function shoutPost(env) {   // daily 12:47: post the oldest queued shout-out whose image the factory has made
  const queue = await kv(env, "shout_queue", []); if (!queue.length) return;
  const m = await manifest(env); const q = queue[0]; const img = (m.shoutouts || []).find(x => x.id === q.id); if (!img) return;
  const reg = await kv(env, "shout", {}); const names = q.names.filter(u => reg[u.toLowerCase()]?.yes);   // someone may have opted out since
  if (!names.length) { queue.shift(); await kvPut(env, "shout_queue", queue); return; }
  const cols = names.length > 10 ? 2 : 1;
  const tags = names.map((u, i) => ({ username: u, x: cols === 1 ? 0.5 : (i % 2 ? 0.72 : 0.28), y: Math.min(0.9, 0.36 + (cols === 1 ? i : Math.floor(i / 2)) * 0.055) }));
  const head = q.kind === "top" ? "Thank you to our top supporters this month 🏆" : "Welcome to the rejectionlist.kerala family 🙏 Thank you for following!";
  const cap = `${head}\n\n${names.map(u => "@" + u).join(" ")}\n\n${SHOUT_CTA}`;
  const c = await graph(env, `${env.IG_USER_ID}/media`, { image_url: `${env.LIB_BASE}/${img.image}`, caption: cap, user_tags: JSON.stringify(tags) });
  await waitReady(env, c.id); const pub = await graph(env, `${env.IG_USER_ID}/media_publish`, { creation_id: c.id });
  const posted = await kv(env, "posted", {}); posted[q.id] = { media: pub.id, t: Date.now(), topic: "co", kind: "shoutout", segment: q.kind }; await kvPut(env, "posted", posted);
  queue.shift(); await kvPut(env, "shout_queue", queue); await log(env, `shout-out ${q.id} posted (${names.length} names)`);
}

async function quotaLeft(env) {   // posts left in Instagram's rolling 24 h window (null if Instagram won't say)
  try { const r = await graph(env, `${env.IG_USER_ID}/content_publishing_limit`, { fields: "config,quota_usage" }, "GET"); const d = r.data?.[0]; return (d?.config?.quota_total ?? 100) - (d?.quota_usage ?? 0); }
  catch (e) { return null; }
}
const TRIAL_SHARE = 0.4; // share of reels posted as trial reels (non-followers first) while the feature is available

const IST = (d = new Date()) => new Date(d.getTime() + 5.5 * 3600e3);
const json = (o, s = 200) => new Response(JSON.stringify(o, null, 1), { status: s, headers: { "content-type": "application/json" } });

async function kv(env, k, d) { const v = await env.STATE.get(k); return v ? JSON.parse(v) : d; }
async function kvPut(env, k, v) { await env.STATE.put(k, JSON.stringify(v)); }
async function log(env, msg) {
  const l = await kv(env, "log", []); l.unshift(`${IST().toISOString().slice(0, 16)} ${msg}`); await kvPut(env, "log", l.slice(0, 300));
}
async function discord(env, content, ping = false) {   // ping = @everyone, so the phone shows a notification
  if (!env.DISCORD_WEBHOOK) return;
  const body = ping ? { content: ("@everyone " + content).slice(0, 1900), allowed_mentions: { parse: ["everyone"] } } : { content: content.slice(0, 1900) };
  try { await fetch(env.DISCORD_WEBHOOK, { method: "POST", headers: { "content-type": "application/json" }, body: JSON.stringify(body) }); } catch {}
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
async function postReel(env, topic = "co", want = "reel") {
  const m = await manifest(env); const posted = await kv(env, "posted", {});
  const w = await kv(env, "weights", null); const L = TOPICS[topic].label;
  const avail = m.items.filter(i => !posted[i.id] && live_(i) && (want === "news" ? ["correction", "news", "opportunity"].includes(i.theme)
    : (topicOf(i) === topic && (want === "tip" ? i.theme === "tip" : !SPECIAL.includes(i.theme)))));
  if (want === "news") avail.sort((a, b) => ["correction", "news", "opportunity"].indexOf(a.theme) - ["correction", "news", "opportunity"].indexOf(b.theme) || (b.built || 0) - (a.built || 0));
  if (want !== "reel") { if (!avail.length) { await log(env, `no ${want} item for ${topic}: slot left empty`); return; } return publishReel(env, avail[0], topicOf(avail[0]), m, posted); }
  if (!avail.length) { await log(env, `NO STOCK: ${topic} reel library empty`); await alertOnce(env, "noreel_" + topic, `⚠️ [${L}] Reel library is empty. Nothing to post. Check the factory on GitHub.`); return; }
  if (avail.length < 35 && IST().getUTCHours() === 7 && IST().getUTCMinutes() < 30) await alertOnce(env, "lowreel_" + topic, `⚠️ [${L}] Reel backup is low: ${avail.length} left. The refill task writes more scripts automatically.`);
  const recent = Object.values(posted).filter(p => topicOf(p) === topic).sort((a, b) => b.t - a.t).slice(0, 2);
  const score = i => (w?.kind?.[i.kind] ?? 1) * (w?.segment?.[i.segment] ?? 1) * (recent.some(r => r.kind === i.kind) ? 0.5 : 1) * (0.8 + Math.random() * 0.4);
  const it = avail.sort((a, b) => score(b) - score(a))[0];
  return publishReel(env, it, topic, m, posted);
}
async function publishReel(env, it, topic, m, posted) {
  const p = { media_type: "REELS", video_url: `${env.LIB_BASE}/${it.video}`, cover_url: `${env.LIB_BASE}/${it.cover}`, caption: fixCaption(it.caption), share_to_feed: "true" };
  const trialOff = await kv(env, "trial_unavailable", false);
  const asTrial = !trialOff && !["news", "opportunity", "correction"].includes(it.theme) && Math.random() < TRIAL_SHARE;   // news goes to followers too
  let c;
  try { c = await graph(env, `${env.IG_USER_ID}/media`, asTrial ? { ...p, trial_params: JSON.stringify({ graduation_strategy: "SS_PERFORMANCE" }) } : p); }
  catch (e) {
    if (!asTrial) throw e;
    await kvPut(env, "trial_unavailable", true); await log(env, `trial reels not available yet (${e.message}); posting normally`);
    c = await graph(env, `${env.IG_USER_ID}/media`, p);
  }
  await waitReady(env, c.id);
  const pub = await graph(env, `${env.IG_USER_ID}/media_publish`, { creation_id: c.id });
  posted[it.id] = { media: pub.id, t: Date.now(), topic, theme: it.theme || null, kind: it.kind, segment: it.segment, scene: it.scene || null, trial: asTrial && !(await kv(env, "trial_unavailable", false)) };
  await kvPut(env, "posted", posted); await log(env, `${topic} reel ${it.id} posted (${pub.id})${posted[it.id].trial ? " as trial" : ""}`);
}
async function postStory(env, topic = "co") {
  // daily mix: 1 new-reel teaser, then tip / quiz question / quiz answer / contact card, so people follow and reply
  const m = await manifest(env); const done = await kv(env, "stories", {});
  const posted = await kv(env, "posted", {}); const reelTopic = Object.fromEntries((m.items || []).map(i => [i.id, topicOf(i)]));
  const all = (m.stories || []).filter(s => !done[s.id] && (!s.after || done[s.after]) && (s.topic ? s.topic : s.reel ? reelTopic[s.reel] || "co" : "co") === topic);
  const teasers = all.filter(s => s.reel && posted[s.reel]);           // only tease reels already live
  const others = all.filter(s => !s.reel);
  const hour = IST().getUTCHours();
  const pendingAnswer = others.find(s => s.after);
  let s = hour < 9 ? teasers[0] : (pendingAnswer || others.find(x => x.kind === (hour < 14 ? "tip" : hour < 19 ? "quiz" : "contact")) || others[0] || teasers[0]);
  if (!s) { await log(env, `NO STORY STOCK (${topic})`); await alertOnce(env, "nostory_" + topic, `⚠️ [${TOPICS[topic].label}] Story library is empty. Nothing to post. Check the factory on GitHub.`); return; }
  const c = await graph(env, `${env.IG_USER_ID}/media`, { media_type: "STORIES", image_url: `${env.LIB_BASE}/${s.image}` });
  await waitReady(env, c.id);
  const pub = await graph(env, `${env.IG_USER_ID}/media_publish`, { creation_id: c.id });
  done[s.id] = { media: pub.id, t: Date.now() }; await kvPut(env, "stories", done);
  posted[s.id] = { media: pub.id, t: Date.now(), topic, kind: "story", segment: s.segment || null, story_kind: s.kind || "teaser" }; await kvPut(env, "posted", posted);
  await log(env, `${topic} story ${s.id} posted`);
}

async function postCarousel(env, topic = "co") {
  const m = await manifest(env); const posted = await kv(env, "posted", {});
  const extra = await kv(env, "extra_carousels", []);              // stop-gap stock pushed by Claude when the library has none
  const avail = [...(m.carousels || []), ...extra.filter(e => !(m.carousels || []).some(c => c.id === e.id))].filter(c => !posted[c.id] && topicOf(c) === topic);
  if (!avail.length) { await log(env, `NO CAROUSEL STOCK (${topic})`); await alertOnce(env, "nocarousel_" + topic, `⚠️ [${TOPICS[topic].label}] Carousel library is empty. Nothing to post. Check the factory on GitHub.`); return; }
  const recent = Object.values(posted).filter(p => p.kind === "carousel" && topicOf(p) === topic).sort((a, b) => b.t - a.t)[0];
  const c = avail.find(x => !recent || x.segment !== recent.segment) || avail[0];
  const kids = [];
  for (const img of c.images.slice(0, 10)) kids.push((await graph(env, `${env.IG_USER_ID}/media`, { image_url: img.startsWith("http") ? img : `${env.LIB_BASE}/${img}`, is_carousel_item: "true" })).id);
  const box = await graph(env, `${env.IG_USER_ID}/media`, { media_type: "CAROUSEL", children: kids.join(","), caption: fixCaption(c.caption) });
  await waitReady(env, box.id);
  const pub = await graph(env, `${env.IG_USER_ID}/media_publish`, { creation_id: box.id });
  posted[c.id] = { media: pub.id, t: Date.now(), topic, kind: "carousel", segment: c.segment };
  await kvPut(env, "posted", posted); await log(env, `${topic} carousel ${c.id} posted (${pub.id})`);
}

// Instagram allows at most 5 hashtags per post (Dec 2025) and 2,200 characters: enforce both on every caption we publish.
function fixCaption(c) {
  let n = 0; c = String(c || "").replace(/(^|\s)#[\p{L}\p{N}_]+/gu, m => (++n <= 5 ? m : "")).replace(/[ \t]+\n/g, "\n").trimEnd();
  return c.slice(0, 2200);
}
async function postPoster(env, topic = "co") {   // single 4:5 image post
  const m = await manifest(env); const posted = await kv(env, "posted", {});
  const avail = (m.posters || []).filter(p => !posted[p.id] && topicOf(p) === topic);
  if (!avail.length) { await log(env, `NO POSTER STOCK (${topic})`); await alertOnce(env, "noposter_" + topic, `⚠️ [${TOPICS[topic].label}] Poster library is empty. Nothing to post. Check the factory on GitHub.`); return; }
  const recent = Object.values(posted).filter(p => p.kind === "poster" && topicOf(p) === topic).sort((a, b) => b.t - a.t)[0];
  const p = avail.find(x => !recent || (x.layout !== recent.layout && x.segment !== recent.segment)) || avail.find(x => !recent || x.layout !== recent.layout) || avail[0];
  const c = await graph(env, `${env.IG_USER_ID}/media`, { image_url: `${env.LIB_BASE}/${p.image}`, caption: fixCaption(p.caption) });
  await waitReady(env, c.id);
  const pub = await graph(env, `${env.IG_USER_ID}/media_publish`, { creation_id: c.id });
  posted[p.id] = { media: pub.id, t: Date.now(), topic, kind: "poster", segment: p.segment, layout: p.layout };
  await kvPut(env, "posted", posted); await log(env, `poster ${p.id} posted (${pub.id})`);
}

// Reach and other post metrics: the posting token lacks instagram_manage_insights, but the Instagram-login (DM) token
// has the insights permission, so use it first and fall back to the posting token.
async function insightsGet(env, media, metrics, tok, budget) {   // budget (optional): { fetches } counter of real subrequests
  if (tok === undefined) tok = await env.STATE.get("ig_login_token");
  if (tok) {
    const u = new URL(`https://graph.instagram.com/v24.0/${media}/insights`); u.search = new URLSearchParams({ metric: metrics, access_token: tok });
    if (budget) budget.fetches++;
    const j = await (await fetch(u)).json(); if (!j.error) return j;
  }
  if (budget) budget.fetches++;
  return graph(env, `${media}/insights`, { metric: metrics }, "GET");
}

// ---------------- optimiser ----------------
// Free plan: 50 subrequests per invocation and ~1000 KV writes/day, so the daily snapshot runs in chunks, one per cron
// minute during 03:01-03:59 IST, and only snapshots a post daily for its first 7 days, then at day 14, 21 and 28.
const SNAP_MAX_POSTS = 30, SNAP_MAX_FETCH = 36;   // insightsGet = 1-2 fetches; leaves room for discord/token refresh
const SUBREQ_LIMIT = /too many subrequests/i;
function snapDue(p, ageRef) {   // ageRef: age in days at today's 03:00 IST, so the set doesn't shift during the hour
  if (p.kind === undefined || ageRef > 30) return false;
  if (p.kind === "story") return ageRef <= 1;   // Instagram keeps story insights for 24 h only
  return [2, 7].includes(Math.floor(ageRef));   // 2 rows per post: at ~96 posts/day this keeps KV writes inside the free 1,000/day
}
async function snapshot(env) {
  // one row per post per due day: metrics + where/when it was posted. This is the insights database.
  // Processes at most one chunk; returns { done: true } when every due post has today's row.
  const posted = await kv(env, "posted", {}); const day = IST().toISOString().slice(0, 10);
  const ref = Date.parse(`${day}T03:00:00+05:30`);
  const pk = "snapprog"; let prog = await kv(env, pk, null); if (!prog || prog.day !== day) prog = { day, done: [] };
  const doneSet = new Set(prog.done);
  const todo = Object.entries(posted).filter(([id, p]) => !doneSet.has(id) && snapDue(p, (ref - p.t) / 86400e3));
  const tok = await env.STATE.get("ig_login_token"); const budget = { fetches: 0 };
  const judged = await kv(env, "judged", {}); let judgedNew = false;
  if (!Object.keys(judged).length && !(await env.STATE.get("judged_backfilled"))) {   // one-time: build the index from older rows
    for (const id of Object.keys(posted).slice(-400)) { const h = await kv(env, `snap:${id}`, []); const r = h.find(x => x.age_days >= 2 && !x.error); if (r) { const { keywords, ...c } = r; judged[id] = c; judgedNew = true; } }
    await env.STATE.put("judged_backfilled", "1"); if (judgedNew) { await kvPut(env, "judged", judged); judgedNew = false; }
  }
  let n = 0, stopped = false;
  for (const [id, p] of todo) {
    if (n >= SNAP_MAX_POSTS || budget.fetches + 2 > SNAP_MAX_FETCH) { stopped = true; break; }
    const k = `snap:${id}`; const hist = await kv(env, k, []);
    if (hist.length && hist[hist.length - 1].day === day) { doneSet.add(id); continue; }   // already has today's row
    const age = (Date.now() - p.t) / 86400e3;
    let v = {};
    try {
      const metrics = p.kind === "story" ? "reach,views,replies,shares,total_interactions,follows,profile_visits"   // stories have no saved/likes/comments
        : p.kind === "carousel" || p.kind === "poster" ? "reach,shares,saved,total_interactions,likes,comments" : "reach,views,shares,saved,total_interactions,likes,comments,ig_reels_avg_watch_time";
      const r = await insightsGet(env, p.media, metrics, tok, budget);
      v = Object.fromEntries(r.data.map(d => [d.name, d.values?.[0]?.value ?? d.total_value?.value ?? 0]));
    } catch (e) {
      if (SUBREQ_LIMIT.test(String(e.message))) { stopped = true; break; }   // not the post's fault: retry next minute, no row
      v = { error: String(e.message).slice(0, 80) };
    }
    n++;
    const ev = await kv(env, `ev:${id}`, { comments: 0, keyword: {}, leads: 0, dms: 0 });
    const posted_ist = IST(new Date(p.t));
    const row = { day, id, topic: topicOf(p), theme: p.theme || null, kind: p.kind, segment: p.segment, scene: p.scene || null, layout: p.layout || null, trial: !!p.trial,
      posted_at: posted_ist.toISOString().slice(0, 16), weekday: posted_ist.getUTCDay(), slot: posted_ist.toISOString().slice(11, 16),
      age_days: Math.round(age * 10) / 10, ...v, keyword_comments: Object.values(ev.keyword).reduce((a, b) => a + b, 0), keywords: ev.keyword, dms: ev.dms, leads: ev.leads };
    hist.push(row); await kvPut(env, k, hist.slice(-31)); doneSet.add(id);
    if (row.age_days >= 2 && !row.error && !judged[id]) { const { keywords, ...c } = row; judged[id] = c; judgedNew = true; }
  }
  if (judgedNew) await kvPut(env, "judged", judged);   // one compact row per post: optimiser and /public/insights read this, not thousands of keys
  if (doneSet.size !== prog.done.length) await kvPut(env, pk, { day, done: [...doneSet] });
  return { day, done: !stopped, rows: n, fetches: budget.fetches };
}
async function snapshotTick(env, day) {   // cron, 03:01-03:59 IST: one chunk; when all done, optimise + token refresh once
  const dk = `snapdone:${day}`; if (await env.STATE.get(dk)) return;
  const r = await snapshot(env); if (!r.done) return;
  await env.STATE.put(dk, "1", { expirationTtl: 172800 });
  await log(env, `snapshot ${day}`); await optimise(env); await refreshIgToken(env);
}

function median(a) { const s = [...a].sort((x, y) => x - y); return s.length ? s[Math.floor(s.length / 2)] : 0; }

async function optimise(env) {
  // Cautious: judge each post at 48-72h; compare it with posts from the SAME slot (time effect removed),
  // need >= 5 posts per group and a clear gap before moving weights, and move at most 25% per week.
  const judged = await kv(env, "judged", {}); const rows = [];
  for (const id of Object.keys(judged)) {
    const r = { ...judged[id] };
    if (!r.reach) continue;
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
    const top = Object.keys(TOPICS).map(t => { const r3 = rows.filter(r => topicOf(r) === t).sort((a, b) => b.score - a.score).slice(0, 3); return r3.length ? `[${TOPICS[t].label}]\n` + r3.map(r => `${r.id} (${r.kind}/${r.segment}, ${r.slot}): reach ${r.reach}, shares ${r.shares || 0}, keyword ${r.keyword_comments}, leads ${r.leads}`).join("\n") : ""; }).filter(Boolean).join("\n");
    await discord(env, `📈 Weekly insights (${rows.length} posts judged)\nTop posts per topic:\n${top || "not enough data yet"}\nMix weights: ${JSON.stringify({ kind: weights.kind, segment: weights.segment })}\nTimes are only being measured for now; no time changes until 3+ weeks of data.`);
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
const RULES_COMMON = `Rules: Always reply in simple, friendly English (even if the user writes in Malayalam or Manglish), short, max 3 sentences. Write like the rejectionlist.kerala team; do not introduce yourself as an assistant, AI or bot and do not mention automation. If the user directly asks whether this is a bot or a real person, do not claim to be human: say these chats give quick answers and a team member will call them personally.
NEVER state any price, fee, cost, discount or our charges; if asked, say the team will share the exact quote on a call after understanding their case. Never give legal or tax advice beyond general facts.`;
const BOT_GST = `You reply to Instagram DMs for rejectionlist.kerala, a team in Kerala, India that handles GST registration (and company registration and investor agreements).
${RULES_COMMON}
General facts you may use: in Kerala GST registration is needed once yearly turnover crosses Rs 40 lakh for goods or Rs 20 lakh for services; selling goods to other states needs GST from the first sale whatever the turnover; selling goods on Amazon, Flipkart or Meesho needs GST from the first sale too, except a small seller below the limit who sells only within Kerala may use a PAN-based enrolment if the marketplace allows it; anyone may register voluntarily (B2B clients often want a GSTIN); a proprietor needs PAN, Aadhaar with its linked mobile, a photo, business address proof and bank proof. Do not judge someone's exact liability; say the team will check it on the call.
Goal: qualify the lead by asking, one at a time:
1) what the business sells or does, and whether it is a proprietorship, partnership, LLP or company, 2) roughly how much turnover this year or expected, 3) whether they sell to other states or through online marketplaces, 4) how soon they need the GSTIN, 5) their phone number, 6) preferred language for the call: Malayalam or English.
When you have all six, thank them and say a team member will call. Output only the reply text.`;
const BOT_INV = `You reply to Instagram DMs for rejectionlist.kerala, a team in Kerala, India that drafts investor agreements (term sheets, share subscription and shareholders' agreements) for both founders raising money and people investing (and also does company and GST registration).
${RULES_COMMON}
General facts you may use: only a private limited company can take equity investment; a term sheet is mostly non-binding except clauses like confidentiality and exclusivity; the shareholders' agreement sets rights such as board seats, share transfer limits and exits, and the company's articles must be updated for those rights to bind the company; shares must be allotted within 60 days of receiving the money; foreign or NRI investment on repatriation basis must be reported to RBI within 30 days of allotment. Never say whether a specific deal is fair or safe; the team will review it on the call.
Goal: qualify the lead by asking, one at a time:
1) are they a founder raising money or an investor putting money in, 2) is the company already a private limited company (and what does it do), 3) who is investing: friends and family, angel, NRI or foreign investor, or a fund, 4) how soon the deal needs to close, 5) their phone number, 6) preferred language for the call: Malayalam or English.
When you have all six, thank them and say a team member will call. Output only the reply text.`;
const FALLBACK_GST = [
  "What does your business sell or do? Is it a proprietorship, partnership, LLP or company?",
  "Roughly how much turnover do you have this year, or expect?",
  "Do you sell to other states, or through Amazon, Flipkart, Meesho or similar?",
  "How soon do you need the GST number?",
  "Could you share a phone number so our team can call you?",
  "Would you prefer the call in Malayalam or English?",
  "Thank you! 🙏 Our team will call you shortly.",
];
const FALLBACK_INV = [
  "Are you a founder raising money, or an investor putting money into a company?",
  "Is the company already a private limited company? What does it do?",
  "Who is investing: friends and family, an angel, an NRI or foreign investor, or a fund?",
  "How soon does the deal need to close?",
  "Could you share a phone number so our team can call you?",
  "Would you prefer the call in Malayalam or English?",
  "Thank you! 🙏 Our team will call you shortly.",
];
const BOT_SUI = `You reply to Instagram DMs for rejectionlist.kerala, a team in Kerala, India that helps startups get Startup India (DPIIT) recognition (and also company registration, GST and investor agreements).
${RULES_COMMON}
General facts you may use: DPIIT recognition is for a private limited company, LLP, registered partnership or cooperative that is under 10 years old, has never crossed Rs 200 crore turnover in a year, and works on innovation or a scalable business model; a proprietorship cannot apply, so it must register an entity first; recognition opens doors to benefits such as patent and trademark fee rebates and self-certification under some labour and environment laws; the 3-year income tax holiday (section 80-IAC) is a separate application approved by a government board, not automatic. Never promise approval or any benefit; the team checks eligibility on the call.
Goal: qualify the lead by asking, one at a time:
1) what the startup does and what is new about it, 2) is it registered yet: Pvt Ltd, LLP, partnership, or not yet, 3) when it was registered and roughly its stage (idea, prototype, revenue), 4) how soon they want the recognition (for a grant, investor, tender, tax?), 5) their phone number, 6) preferred language for the call: Malayalam or English.
When you have all six, thank them and say a team member will call. Output only the reply text.`;
const BOT_SK = `You reply to Instagram DMs for rejectionlist.kerala, a team in Kerala, India that helps startups register with Kerala Startup Mission (KSUM) and get the KSUM Unique ID (and also company registration, DPIIT, GST and investor agreements).
${RULES_COMMON}
General facts you may use: KSUM's schemes, grants, incubation and events are for startups registered in Kerala that hold a KSUM Unique ID; most KSUM grants and the seed fund also need DPIIT recognition and a private limited company or LLP; for the idea grant you may apply before incorporating, but the company and Unique ID are needed before money is released. Never promise a grant, an amount or approval; the team checks eligibility on the call.
Goal: qualify the lead by asking, one at a time:
1) what the startup does, 2) is it registered yet, and in Kerala: Pvt Ltd, LLP, or not yet, 3) does it already have DPIIT recognition, 4) what they want from KSUM (grant, incubation space, funding, events) and how soon, 5) their phone number, 6) preferred language for the call: Malayalam or English.
When you have all six, thank them and say a team member will call. Output only the reply text.`;
const FALLBACK_SUI = [
  "What does your startup do, and what is new about it?",
  "Is it registered yet: private limited, LLP, partnership, or not yet?",
  "When was it registered, and what stage is it at: idea, prototype or earning revenue?",
  "How soon do you need the recognition, and what for: a grant, an investor, a tender or tax?",
  "Could you share a phone number so our team can call you?",
  "Would you prefer the call in Malayalam or English?",
  "Thank you! 🙏 Our team will call you shortly.",
];
const FALLBACK_SK = [
  "What does your startup do?",
  "Is it registered yet, and in Kerala: private limited, LLP, or not yet?",
  "Does it already have Startup India (DPIIT) recognition?",
  "What do you want from KSUM: a grant, incubation space, funding or events? How soon?",
  "Could you share a phone number so our team can call you?",
  "Would you prefer the call in Malayalam or English?",
  "Thank you! 🙏 Our team will call you shortly.",
];
const BOT_UD = `You reply to Instagram DMs for rejectionlist.kerala, a team in Kerala, India that helps businesses get Udyam (MSME) registration (and also company registration, GST, Startup India, KSUM and investor agreements).
${RULES_COMMON}
General facts you may use: Udyam is the government's MSME registration, Aadhaar-based with PAN (and GSTIN where the business has one) and self-declared; it does not need renewal but details should be kept updated. Since 1 April 2025 a micro enterprise has investment up to Rs 2.5 crore and turnover up to Rs 10 crore (small: Rs 25 crore and Rs 100 crore; medium: Rs 125 crore and Rs 500 crore), and BOTH limits must be met. For manufacturing and service micro and small units, buyers must pay within 45 days (or the agreed time up to 45 days) or owe compound interest at three times the RBI bank rate, a delayed payment can be taken to the MSME Samadhaan portal, and a buyer who pays late loses the income tax deduction until payment (section 43B(h)). Retail and wholesale traders can register but only for priority sector lending, not the 45-day protection. Registration also helps with priority lending, collateral-free loan schemes and government tender preferences. Never promise a loan, subsidy or recovery; the team checks the case on the call.
Goal: qualify the lead by asking, one at a time:
1) what the business does (manufacturing, service or trading), 2) is it a proprietorship, partnership, LLP or company, and does it have GST, 3) roughly its turnover, 4) why they want Udyam now (a buyer asked, a loan, a tender, delayed payments) and how soon, 5) their phone number, 6) preferred language for the call: Malayalam or English.
When you have all six, thank them and say a team member will call. Output only the reply text.`;
const FALLBACK_UD = [
  "What does your business do: manufacturing, a service or trading?",
  "Is it a proprietorship, partnership, LLP or company? Does it have GST?",
  "Roughly how much turnover does it have in a year?",
  "Why do you want Udyam now: a buyer asked, a loan, a tender or a delayed payment? How soon?",
  "Could you share a phone number so our team can call you?",
  "Would you prefer the call in Malayalam or English?",
  "Thank you! 🙏 Our team will call you shortly.",
];
const botFor = c => `You reply to Instagram DMs for rejectionlist.kerala, a team in Kerala, India that ${c.about} (and also company registration, GST and other business registrations and agreements).
${RULES_COMMON}
General facts you may use: ${c.facts}
Goal: qualify the lead by asking, one at a time:
${c.qs.map((q, i) => `${i + 1}) ${q}`).join(" ")} 5) their phone number, 6) preferred language for the call: Malayalam or English.
When you have all six, thank them and say a team member will call. Output only the reply text.`;
const BOT = { ...Object.fromEntries(Object.entries(NEWT).map(([t, c]) => [t, () => ({ sys: botFor(c), fq: [...c.qs, ...Q_END] })])), ud: () => ({ sys: BOT_UD, fq: FALLBACK_UD }), co: () => ({ sys: BOT_SYSTEM, fq: FALLBACK_Q }), gst: () => ({ sys: BOT_GST, fq: FALLBACK_GST }), inv: () => ({ sys: BOT_INV, fq: FALLBACK_INV }), sui: () => ({ sys: BOT_SUI, fq: FALLBACK_SUI }), sk: () => ({ sys: BOT_SK, fq: FALLBACK_SK }) };
function fallbackReply(thread, topic = "co") {
  const FALLBACK_Q = BOT[topic]().fq;
  const last = thread[thread.length - 1]?.content || "";
  const said = thread.filter(m => m.role === "assistant").map(m => m.content).join("\n");   // keyword replies already ask some of these
  let asked = FALLBACK_Q.findIndex(q => !said.includes(q.split(/[?!]/)[0].split(" ").slice(0, 4).join(" ")));
  if (asked < 0) asked = FALLBACK_Q.length - 1;
  let pre = "";
  if (topic === "co" && /\b(pvt|ltd|private|limited|llp|opc)\b/i.test(last) || /പ്രൈവറ്റ്|ലിമിറ്റഡ്/.test(last)) {
    const hits = ["bank", "insurance", "ബാങ്ക്", "ഇൻഷുറൻസ്"].filter(x => last.toLowerCase().includes(x));
    pre = hits.length ? `Words like "${hits[0]}" need special approval, so this name could be rejected. ` : "No restricted words in this name. It must also not be similar to an existing company, LLP or registered trademark. ";
    pre += "Final availability is confirmed only when the application is filed.\n\n";
  }
  if (/price|fee|cost|charge|rate|എത്ര രൂപ|ചാർജ്|ഫീസ്/i.test(last)) pre = "Our team will share the exact quote on a call once they understand your business. ";
  return pre + FALLBACK_Q[Math.min(asked, FALLBACK_Q.length - 1)];
}
async function botReply(env, thread, topic = "co") {
  try {
    const r = await env.AI.run("@cf/meta/llama-3.3-70b-instruct-fp8-fast", { messages: [{ role: "system", content: BOT[topic]().sys }, ...thread.slice(-12)], max_tokens: 220 });
    const t = (r.response || "").trim(); if (t) return t;
  } catch (e) { await log(env, `AI unavailable, using fallback: ${String(e.message).slice(0, 80)}`); }
  return fallbackReply(thread, topic);
}
const BTN = /^(yes, send it|i've followed|talk to our team|which type suits me\?|documents needed|do i need gst\?|gst documents|i'm raising funds|i'm investing|am i eligible\?|what do i get\?|which grants\?|micro, small or medium\?|late payments\?|yes,? tag me|no thanks|can i use tm now\?|name vs trademark\?|no business, still file\?|what's the late fee\?|home bakers too\?|registration or licence\?|do i need iec\?|yearly update\?|one-way or mutual\?|will investors sign\?|what is vesting\?|if one leaves\?|what do investors check\?|for a bank loan\?|which method fits me\?|who must sign it\?)/i;
function regexLead(thread, topic = "co") {   // no AI: read each answer that follows our question
  const users = thread.filter(m => m.role === "user" && !BTN.test(m.content.trim()));
  const all = users.map(m => m.content).join(" \n ");
  const phone = (all.replace(/[\s-]/g, "").match(/(?:\+?91)?[6-9]\d{9}/) || [""])[0];
  const ans = re => { for (let i = thread.length - 2; i >= 0; i--) if (thread[i].role === "assistant" && re.test(thread[i].content)) { const n = thread.slice(i + 1).find(m => m.role === "user"); if (n && !BTN.test(n.content.trim()) && !/^\+?\d[\d\s-]{8,}$/.test(n.content.trim())) return n.content.slice(0, 120); } return ""; };
  const business = ans(/what does your business (do|sell)|business do\?|founder raising money|private limited company\? what/i) || users[0]?.content?.slice(0, 120) || "";
  const traction = ans(/income|clients|funding|turnover|who is investing/i), timeline = ans(/how soon|when .*register|timeline|deal need/i);
  const strong = traction && !/^(no|not|nothing|illa|ഇല്ല)/i.test(traction.trim()), soon = /asap|soon|immediately|this (week|month)|now|urgent|ഉടൻ/i.test(timeline);
  return { topic, business, role: ans(/founder raising money/i), interstate: ans(/other states|amazon/i), founders: ans(/how many founders|founders/i), nri: /nri|gulf|dubai|saudi|qatar|ഗൾഫ്|ദുബായ്|സൗദി|ഖത്തർ|മസ്കറ്റ്/i.test(all), traction, timeline,
    phone, language: /english|ഇംഗ്ലീഷ്/i.test(all) ? "English" : /malayalam|മലയാളം/i.test(all) ? "Malayalam" : "", intent: !phone ? "low" : strong && soon ? "high" : "medium", can_afford_30k: strong ? "likely" : "unclear", reason: "Summary made without AI; open the chat for details" };
}
const LEAD_SCHEMA = {
  co: `{"business":"","founders":"","nri":false,"traction":"","timeline":"","phone":"","language":"","intent":"high|medium|low","can_afford_30k":"likely|unclear|unlikely","reason":""}`,
  gst: `{"business":"what they sell and the business type","founders":"","nri":false,"traction":"turnover this year or expected","interstate":"sells to other states / online marketplaces?","timeline":"","phone":"","language":"","intent":"high|medium|low","can_afford_30k":"likely|unclear|unlikely","reason":""}`,
  ...Object.fromEntries(Object.keys(NEWT).map(t => [t, `{"business":"what the business does and what they need","founders":"","nri":false,"traction":"entity type, stage and any numbers they gave","timeline":"what it is for and how soon","phone":"","language":"","intent":"high|medium|low","can_afford_30k":"likely|unclear|unlikely","reason":""}`])),
  ud: `{"business":"what the business does and whether manufacturing, service or trading","founders":"","nri":false,"traction":"entity type, GST status, turnover","timeline":"why Udyam now and how soon","phone":"","language":"","intent":"high|medium|low","can_afford_30k":"likely|unclear|unlikely","reason":""}`,
  sui: `{"business":"what the startup does and what is new","founders":"","nri":false,"traction":"entity type, registration date and stage","timeline":"how soon and what for","phone":"","language":"","intent":"high|medium|low","can_afford_30k":"likely|unclear|unlikely","reason":""}`,
  sk: `{"business":"what the startup does","founders":"","nri":false,"traction":"entity type, Kerala registration, DPIIT status","timeline":"what they want from KSUM and how soon","phone":"","language":"","intent":"high|medium|low","can_afford_30k":"likely|unclear|unlikely","reason":""}`,
  inv: `{"role":"founder raising | investor investing","business":"company and what it does, Pvt Ltd or not","founders":"","nri":false,"traction":"who is investing (friends/family, angel, NRI/foreign, fund)","timeline":"","phone":"","language":"","intent":"high|medium|low","can_afford_30k":"likely|unclear|unlikely","reason":""}`,
};
async function extractLead(env, thread, topic = "co") {
  let r;
  try { r = await env.AI.run("@cf/meta/llama-3.3-70b-instruct-fp8-fast", { messages: [
    { role: "system", content: `From this conversation, output JSON only: ${LEAD_SCHEMA[topic]}. "nri" is true if the person or an investor lives abroad. "can_afford_30k" judges from traction, funding, urgency and team, never from asking about money.` },
    { role: "user", content: thread.map(m => `${m.role}: ${m.content}`).join("\n") }], max_tokens: 300 }); }
  catch (e) { return regexLead(thread, topic); }
  try { const j = typeof r.response === "object" && r.response ? r.response : JSON.parse(String(r.response || "").match(/\{[\s\S]*\}/)[0]); const rx = regexLead(thread, topic);
    return { ...j, topic, phone: j.phone || rx.phone, language: j.language || rx.language }; } catch { return regexLead(thread, topic); }
}
async function igProfile(env, igsid) {
  try { const p = await graph(env, igsid, { fields: "username,is_user_follow_business" }, "GET"); return { username: p.username || null, follows: typeof p.is_user_follow_business === "boolean" ? p.is_user_follow_business : null }; }
  catch (e) { await log(env, `profile lookup failed: ${e.message}`); return { username: null, follows: null }; }
}
// Keyword matching that tolerates typos, spacing, case, and Malayalam spellings
// (e.g. "strat", "Satrt🙏", "chek list", "nmae", "സ്റ്റാർട്ട്"), without firing on ordinary words like "star", "game" or "alter".
const KW_TOPIC = { START: "co", NAME: "co", AFTER: "co", CHECKLIST: "co", GST: "gst", LIMIT: "gst", PENALTY: "gst", INVEST: "inv", TERMSHEET: "inv", FUNDING: "inv",
  DPIIT: "sui", BENEFITS: "sui", KSUM: "sk", GRANT: "sk", UDYAM: "ud", MSME: "ud",
  ...Object.fromEntries(Object.entries(NEWT).flatMap(([t, c]) => Object.keys(c.kws).map(k => [k, t]))) };
const KEYWORDS = Object.keys(KW_TOPIC);
const KW_UPPER_IN_LONG = new Set(["AFTER", "GST", "LIMIT", "PENALTY", "INVEST", "FUNDING", "TERMSHEET", "BENEFITS", "GRANT", "KSUM", "DPIIT", "UDYAM", "MSME", "TRADEMARK", "BRAND", "ROC", "FILING", "FSSAI", "FOOD", "IEC", "EXPORT", "NDA", "SECRET", "COFOUNDER", "VESTING", "PROJECTION", "FORECAST", "VALUATION", "WORTH"]);   // ordinary words: in a long comment they count only when written in capitals
const KW_NOFUZZ = new Set(["GST", "KSUM", "MSME", "ROC", "FSSAI", "FOOD", "IEC", "NDA", "BRAND", "COFOUNDER", "WORTH"]);   // COFOUNDER: "founder" alone must not trigger it   // too short to guess typos safely
const KW_ML = [[/സ്റ്റാർ?ട്ട?്?|സ്റ്റാട്ട്/, "START"], [/നെയിം|നേം|നെയിമ്/, "NAME"], [/ആഫ്റ്റർ|ആഫ്ടർ/, "AFTER"], [/ചെക്ക്[\s\u200c\u200d]*ലിസ്റ്റ്|ചെക്ലിസ്റ്റ്/, "CHECKLIST"],
  [/ജി[\s.]*എസ്[\s.]*ടി|ജിഎസ്ടി/, "GST"], [/ലിമിറ്റ്(?![\u0D00-\u0D7F])/, "LIMIT"], [/പെനാൽ?റ്റി/, "PENALTY"], [/ഇൻവെസ്റ്റ്(?![\u0D00-\u0D7F])/, "INVEST"], [/ടേം[\s\u200c]*ഷീറ്റ്/, "TERMSHEET"], [/ഫണ്ടിം?ഗ്/, "FUNDING"], [/ഡി[\s.]*പി[\s.]*ഐ[\s.]*ഐ[\s.]*ടി/, "DPIIT"], [/ബെനഫിറ്റ്/, "BENEFITS"], [/കെ[\s.]*സം|കെസം|കെ[\s.]*എസ്[\s.]*യു[\s.]*എം/, "KSUM"], [/ഗ്രാന്റ്/, "GRANT"], [/ഉദ്യാ?ം|ഉദ്യമ്/, "UDYAM"], [/എം[\s.]*എസ്[\s.]*എം[\s.]*ഇ/, "MSME"], [/ട്രേഡ്[\s\u200c]*മാർക്ക്/, "TRADEMARK"], [/ആർ[\s.]*ഒ[\s.]*സി/, "ROC"],
  [/എഫ്[\s.]*എസ്[\s.]*എസ്[\s.]*എ[\s.]*ഐ/, "FSSAI"], [/ഐ[\s.]*ഇ[\s.]*സി/, "IEC"], [/എക്സ്പോർട്ട്/, "EXPORT"], [/എൻ[\s.]*ഡി[\s.]*എ/, "NDA"], [/കോ[\s-]*ഫൗണ്ടർ/, "COFOUNDER"], [/വെസ്റ്റിംഗ്/, "VESTING"], [/പ്രൊജക്ഷൻ/, "PROJECTION"], [/ഫോർകാസ്റ്റ്/, "FORECAST"], [/വാല്യുവേഷൻ|മൂല്യനിർണ്ണയം/, "VALUATION"]];
const KW_STOP = new Set(["star", "stars", "stat", "stats", "smart", "stark", "tart", "starts", "same", "came", "game", "fame", "lame", "tame", "made", "dame", "nam", "alter", "afer", "hater", "invent", "invents", "finding", "fending", "funding's", "limbo", "lima", "omit", "vomit", "penalt", "gift", "grand", "grants'", "udyog", "expert", "experts", "testing", "resting", "nesting", "filling", "filming", "secrets", "brand's", "branded", "giant", "grunt", "granite", "benefit's"]);
function editDist(a, b) {   // Damerau-Levenshtein (adjacent swaps count as one edit)
  const d = Array.from({ length: a.length + 1 }, (_, i) => [i, ...Array(b.length).fill(0)]);
  for (let j = 1; j <= b.length; j++) d[0][j] = j;
  for (let i = 1; i <= a.length; i++) for (let j = 1; j <= b.length; j++) {
    d[i][j] = Math.min(d[i - 1][j] + 1, d[i][j - 1] + 1, d[i - 1][j - 1] + (a[i - 1] === b[j - 1] ? 0 : 1));
    if (i > 1 && j > 1 && a[i - 1] === b[j - 2] && a[i - 2] === b[j - 1]) d[i][j] = Math.min(d[i][j], d[i - 2][j - 2] + 1);
  }
  return d[a.length][b.length];
}
async function uniqueKw(env, text, item = null) {
  const toks = (text.toUpperCase().match(/[A-Z]+[0-9]*/g) || []).filter(t => t.length >= 3); if (!toks.length) return null;
  // an own keyword that is also a general keyword of another topic (old posts used INVEST, LIMIT...) counts only on its own post
  try { const map = (await manifest(env)).kwmap || {}; for (const t of toks) if (map[t] && KEYWORDS.includes(map[t].base) && (!KW_TOPIC[t] || map[t].item === item)) return { kw: t, ...map[t] }; } catch (e) {}
  return null;
}
function matchKeyword(text) {
  for (const [re, kw] of KW_ML) if (re.test(text)) return kw;
  const w = (text.toLowerCase().match(/[a-z]+/g) || []);
  const toks = [...w, ...w.slice(1).map((x, i) => w[i] + x)];   // "check list" -> "checklist"
  const long = w.length > 4;   // in a long comment only a clear keyword counts, and "after" only when written AFTER
  for (const t of toks) for (const kw of KEYWORDS) if (t === kw.toLowerCase() && !(long && KW_UPPER_IN_LONG.has(kw) && !new RegExp(`\\b${kw}\\b`).test(text.replace(/TERM\s+SHEET/g, "TERMSHEET")))) return kw;   // exact first
  for (const t of toks) {
    if (t.length < 3 || KW_STOP.has(t)) continue;
    for (const kw of long ? ["CHECKLIST"] : KEYWORDS.filter(k => !KW_NOFUZZ.has(k))) if (editDist(t, kw.toLowerCase()) <= (kw.length >= 8 ? 2 : 1)) return kw;
  }
  return null;
}
// Tap-to-reply buttons (Instagram quick replies, max 13, title max 20 chars). A tap arrives as a normal text message.
const qr = titles => titles.map(t => ({ content_type: "text", title: t, payload: t.toUpperCase() }));
// DMs go out through the Instagram-login app ("Rejectionlist", token kept in KV) when it is connected; otherwise the publisher app.
async function igMsg(env, body) {
  const tok = null;   // sender ids from the inbox poll belong to the publisher app, so send with it
  if (!tok) return graph(env, `${env.IG_USER_ID}/messages`, body);
  const r = await fetch("https://graph.instagram.com/v24.0/me/messages", { method: "POST", body: new URLSearchParams({ ...body, access_token: tok }) });
  const j = await r.json(); if (!j.error) return j;
  await log(env, `ig-login send failed (${j.error.message}); using publisher app`);
  return graph(env, `${env.IG_USER_ID}/messages`, body);
}
async function refreshIgToken(env) {   // Instagram-login tokens last 60 days; refresh weekly
  const tok = await env.STATE.get("ig_login_token"); const at = +(await env.STATE.get("ig_login_token_set") || 0);
  if (!tok || Date.now() - at < 7 * 864e5) return;
  const r = await (await fetch(`https://graph.instagram.com/refresh_access_token?grant_type=ig_refresh_token&access_token=${encodeURIComponent(tok)}`)).json();
  if (r.access_token) { await env.STATE.put("ig_login_token", r.access_token); await env.STATE.put("ig_login_token_set", String(Date.now())); await log(env, "instagram DM token refreshed"); }
  else { await log(env, `ERROR token refresh: ${r.error?.message}`); await discord(env, `⚠️ Instagram DM token refresh failed: ${r.error?.message}. Generate a new token in the Rejectionlist app.`); }
}
async function sendMsg(env, recipient, text, buttons = []) {
  const msg = buttons.length ? { text, quick_replies: qr(buttons) } : { text };
  try { return await igMsg(env, { recipient: JSON.stringify(recipient), message: JSON.stringify(msg) }); }
  catch (e) {   // if Instagram rejects the buttons, still deliver the text
    if (!buttons.length) throw e;
    await log(env, `buttons rejected, sent plain text: ${e.message}`);
    return igMsg(env, { recipient: JSON.stringify(recipient), message: JSON.stringify({ text }) });
  }
}
async function sendDM(env, to, text, buttons = []) { return sendMsg(env, { id: to }, text, buttons); }
async function opsOk(env, key) {
  if (!key) return false;
  const h = [...new Uint8Array(await crypto.subtle.digest("SHA-256", new TextEncoder().encode(key)))].map(b => b.toString(16).padStart(2, "0")).join("");
  return h === env.OPS_KEY_SHA256 ? "owner" : (!!env.OPS_KEY_MONITOR_SHA256 && h === env.OPS_KEY_MONITOR_SHA256) ? "monitor" : false;
}
// The scheduled tasks' key sits in their task instructions, so it is limited: read status/insights, run read-only jobs,
// hold or release a volume stage, and make GET-only Graph calls. It cannot change tokens, post, or see lead phone numbers.
async function monitorAllowed(req, u) {
  const p = u.pathname;
  if (req.method === "GET") return ["/ops/status", "/ops/insights", "/ops/nudge", "/ops/leads"].includes(p);
  if (req.method !== "POST") return false;
  const b = await req.clone().json().catch(() => ({}));
  if (p === "/ops/run") return ["slots", "snapshot", "optimise", "poll", "nudge"].includes(b.what) && !b.id;
  if (p === "/ops/flag") return /^stage_hold(_[a-z]+)?$/.test(b.k) || b.k === "low_reach_mode" || b.k === "reel_cap";
  if (p === "/ops/graph") return (b.method || "GET") === "GET";
  if (p === "/ops/correct") return true;
  return false;
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

// ---------------- check-ins for people who went quiet ----------------
// Index (KV "nudge"): { <ig id>: { li: last message from them, n: check-ins sent since then, tot: check-ins ever, ls: last check-in time, u: username }
//                       | { c: comment id, t: time, u, f }   (commented, got our DM, never replied) , _s: today's counters }
// Instagram only allows a DM within 24 h of the person's last message, so DM check-ins go out 2 h, 9 h and 22 h after it.
// Someone who only commented cannot be DM'd a second time, so they get one public reply under their comment instead.
const NUDGE_AT = [2, 9, 22].map(h => h * 3600e3), NUDGE_GAP = 3 * 3600e3, NUDGE_MAX_TOTAL = 6, NUDGE_COMMENT_AT = 3 * 3600e3;
const NUDGE_OPEN = [
  "Hey, just checking in 👋 We were halfway through your {noun} chat and didn't want to leave you hanging.",
  "Hi again 🙂 No rush at all. One quick answer and we can take this forward for you.",
  "Last check from our side 🙏 If you'd still like our team to call you, just reply here and we'll pick up where we stopped.",
];
const NUDGE_PUBLIC = [
  "just checking 👋 did our DM reach you? It may be sitting in message requests (or hidden requests). Reply there and we'll take it forward.",
  "quick check 🙂 we sent what you asked for by DM. If you can't see it, look in message requests, then reply there and we'll continue.",
];
const OPT_OUT = /^\s*(stop|unsubscribe|not interested|no thanks|no thank you|don'?t message|leave me)\b/i;
function nudgeText(thread, meta, n) {   // check-in line + the exact step they stopped on, so a reply continues the normal flow
  const lastA = [...thread].reverse().find(m => m.role === "assistant")?.content || "";
  if (/will call you/i.test(lastA)) return null;                       // flow already finished
  const topic = TOPICS[meta?.topic] ? meta.topic : "co";
  const open = NUDGE_OPEN[Math.min(n, NUDGE_OPEN.length - 1)].replace("{noun}", TOPICS[topic].noun);
  if (meta?.pending_kw) return { text: `${open}\n\nYour guide is ready. Follow @rejectionlist.kerala, then tap the button below and we'll send it right away.`, buttons: ["I've followed ✅"] };
  const qLine = lastA.split("\n").reverse().find(l => l.includes("?")) || "";               // the question(s) they were last asked, as written
  let q = (qLine.match(/[^.!?•✅📄🏠📝]*\?/gu) || []).map(x => x.trim()).filter(Boolean).join(" ");
  if (!q && /name you have in mind/i.test(lastA)) q = "Which company name do you have in mind? Send it here and we'll give it a first review.";
  if (!q) q = "Shall we continue? Reply here and we'll pick up right where we stopped.";
  const buttons = /malayalam or english/i.test(q) ? ["Malayalam", "English"] : Object.values(KEYWORD_REPLY).some(r => lastA.endsWith(r.slice(-60))) ? NEXT[topic] : [];
  return { text: `${open}\n\n${q}`, buttons };
}
function nudgeStat(nx, field) { const day = IST().toISOString().slice(0, 10); if (nx._s?.day !== day) nx._s = { day }; nx._s[field] = (nx._s[field] || 0) + 1; }
async function nudgeApply(env, ops, stats = []) {   // re-read before writing so a message that arrived meanwhile is not lost
  if (!Object.keys(ops).length && !stats.length) return;
  const nx = await kv(env, "nudge", {});
  for (const [id, v] of Object.entries(ops)) { if (v === null) delete nx[id]; else if (!nx[id] || nx[id].c || !v.li || (nx[id].li || 0) <= v.li) nx[id] = v; }
  for (const f of stats) nudgeStat(nx, f);
  await kvPut(env, "nudge", nx);
}
async function processNudges(env, force = null) {
  const now = Date.now(), hr = IST().getUTCHours();
  if (!force && (hr < 8 || hr >= 22)) return { skipped: "quiet hours" };          // never message people at night
  const nx = await kv(env, "nudge", null); if (!nx) return { none: true };
  const ops = {}, stats = [], out = []; let sent = 0, leads = null;
  const getLeads = async () => leads || (leads = await kv(env, "leads", {}));
  for (const [id, e] of Object.entries(nx)) {
    if (id === "_s" || (force && force !== id)) continue;
    if (sent >= 4) break;                                                          // a few per minute is plenty
    try {
      if (e.c && !e.li) {                                                          // commented, got the DM, never replied
        if (now - e.t > 6 * 864e5) { ops[id] = null; continue; }
        if (!force && now - e.t < NUDGE_COMMENT_AT) continue;
        const metas = [await kv(env, `m:${id}`, null), e.f && e.f !== id ? await kv(env, `m:${e.f}`, null) : null];
        const L = (await getLeads())[id] || (e.f ? (await getLeads())[e.f] : null);
        ops[id] = null;
        if (metas.some(m => m && (m.last_in > e.t - 60e3 || m.no_nudge)) || (L?.phone && L?.language)) continue;   // they did reply, opted out, or are already a full lead
        await graph(env, `${e.c}/replies`, { message: `${e.u ? "@" + e.u + " " : ""}${NUDGE_PUBLIC[Math.floor(Math.random() * NUDGE_PUBLIC.length)]}` });
        sent++; stats.push("pub"); out.push(`${id}: public`); await log(env, `check-in: public reply to @${e.u || id} (no DM reply yet)`);
        continue;
      }
      const age = now - e.li;
      if (age > 23.5 * 3600e3 || e.n >= NUDGE_AT.length || (e.tot || 0) >= NUDGE_MAX_TOTAL) { ops[id] = null; continue; }
      if (!force && (age < NUDGE_AT[e.n] || now - (e.ls || 0) < NUDGE_GAP)) continue;
      const meta = await kv(env, `m:${id}`, null);
      if (!meta || meta.no_nudge) { ops[id] = null; continue; }
      if (meta.last_in > e.li + 1000) { ops[id] = { ...e, li: meta.last_in, n: 0 }; continue; }   // they wrote again; restart the clock
      const L = (await getLeads())[id];
      if (L?.phone && L?.language) { ops[id] = null; continue; }                   // flow complete
      const thread = await kv(env, `t:${id}`, []);
      if (!thread.length || thread[thread.length - 1].role !== "assistant") continue;
      const nt = nudgeText(thread, meta, e.n); if (!nt) { ops[id] = null; continue; }
      try { await sendDM(env, id, nt.text, nt.buttons); }
      catch (e1) { ops[id] = null; await log(env, `check-in to ${id} not delivered: ${String(e1.message).slice(0, 90)}`); continue; }
      thread.push({ role: "assistant", content: nt.text }); await kvPut(env, `t:${id}`, thread);
      ops[id] = { ...e, n: e.n + 1, tot: (e.tot || 0) + 1, ls: now }; sent++; stats.push("sent"); out.push(`${id}: dm ${e.n + 1}`);
      await log(env, `check-in ${e.n + 1} sent to @${meta.username || id}`);
      if (L?.phone && !L.alerted && L.intent !== "low") {                          // gave a number but stopped: still worth a call
        const all = await kv(env, "leads", {}); if (all[id]) { all[id].alerted = true; await kvPut(env, "leads", all); leads = all; }
        await discord(env, `🔔 **[${TOPICS[L.topic]?.label || TOPICS.co.label}] Lead stopped midway, but left a number** (${L.intent} intent)\n📞 ${L.phone}  ·  🗣 ${L.language || "not answered"}\n🏢 ${L.business || "?"}\n📍 Came from: ${L.source_item || "?"}\nThey went quiet about ${Math.round(age / 3600e3)} h ago; a check-in message has been sent.\nLead ID: ${id}\nAfter your call, tell Claude: "lead ${id}: <what happened>"`, true);
      }
    } catch (err) { await log(env, `ERROR check-in ${id}: ${String(err.message).slice(0, 90)}`); ops[id] = null; }
  }
  await nudgeApply(env, ops, stats);
  return { sent, out };
}

async function pollInbox(env) {
  const since = Date.now() - 15 * 60e3;   // look-back window; dup: keys stop double handling
  let j;   // the publisher app's token can read the inbox
  try { j = await graph(env, `${env.IG_USER_ID}/conversations`, { platform: "instagram", limit: "15", fields: "updated_time,messages.limit(6){id,message,from,created_time}" }, "GET"); }
  catch (e) { await log(env, `ERROR inbox poll: ${e.message}`); return; }
  const evs = [];
  for (const c of j.data || []) {
    if (Date.parse(c.updated_time) < since - 120e3) continue;
    for (const m of c.messages?.data || []) {
      if (!m.message || !m.from || m.from.id === env.IG_USER_ID || (m.from.username || "").toLowerCase() === OWN_USERNAME) continue;
      if (Date.parse(m.created_time) < since - 120e3) continue;
      if (await env.STATE.get(`dup:${m.id}`)) continue;
      evs.push({ t: Date.parse(m.created_time), ev: { sender: { id: m.from.id }, message: { mid: m.id, text: m.message } } });
    }
  }
  evs.sort((a, b) => a.t - b.t);
  if (evs.length) { await log(env, `inbox poll: ${evs.length} new message(s)`); await handleWebhook(env, { object: "instagram(poll)", entry: [{ messaging: evs.map(e => e.ev) }] }); }
}
async function handleWebhook(env, body) {
  const n = (body.entry || []).reduce((t, e) => [t[0] + (e.messaging || []).length, t[1] + (e.changes || []).length], [0, 0]);
  await log(env, `webhook in: ${body.object || "?"} ${n[0]} message(s), ${n[1]} change(s) ${(body.entry || []).flatMap(e => (e.changes || []).map(c => c.field)).join(",")}`);
  for (const entry of body.entry || []) {
    for (const ev of entry.messaging || []) {
      const mid = ev.message?.mid || ev.postback?.mid; if (mid) { if (await env.STATE.get(`dup:${mid}`)) continue; await env.STATE.put(`dup:${mid}`, "1", { expirationTtl: 86400 }); }
      if (ev.postback && !ev.message) ev.message = { text: ev.postback.title || ev.postback.payload || "" };   // button taps of other kinds
      if (ev.message && !ev.message.is_echo && (ev.message.attachments || []).some(a => a?.type === "story_mention")) { await storyMention(env, ev.sender.id); continue; }   // not a lead message
      if (!ev.message || ev.message.is_echo || !ev.message.text) continue;
      const uid = ev.sender.id; const key = `t:${uid}`;
      if (/^\s*delete\s*$/i.test(ev.message.text)) {                  // data deletion request (see /privacy)
        await env.STATE.delete(key); await env.STATE.delete(`m:${uid}`);
        const leads = await kv(env, "leads", {}); if (leads[uid]) { delete leads[uid]; await kvPut(env, "leads", leads); }
        await nudgeApply(env, { [uid]: null });
        await sendDM(env, uid, "Done. We have deleted your conversation and details from our system."); await log(env, `data deleted for ${uid}`); continue;
      }
      const thread = await kv(env, key, []);
      const meta = await kv(env, `m:${uid}`, { first: Date.now(), sources: [] });
      meta.last_in = Date.now();                                     // 24h window starts from their last message
      if (OPT_OUT.test(ev.message.text)) {                           // asked us to stop: no check-ins for this person, and no further questions now
        meta.no_nudge = true; await kvPut(env, `m:${uid}`, meta); await nudgeApply(env, { [uid]: null });
        const bye = "No problem 🙏 We won't send you any more reminders. If you need us later, just message here.";
        thread.push({ role: "user", content: ev.message.text }, { role: "assistant", content: bye }); await kvPut(env, key, thread);
        await sendDM(env, uid, bye); await log(env, `opt-out from ${uid}`); continue;
      }
      if (meta.no_nudge) delete meta.no_nudge;                       // they started talking again
      {   // shout-out consent: answers, opt-outs and WELCOME never go to the sales bot
        const tx = ev.message.text.trim(); let sr = null;
        const pf = await igProfile(env, uid); const un = pf.username || meta.username; if (un) meta.username = un;
        await shoutNote(env, un, uid, "engage");
        if (/^yes,? tag me/i.test(tx)) { await shoutNote(env, un, uid, { yes: true, yes_t: Date.now(), asked: true }); sr = "Done! 🙌 You'll be in our next welcome post. Reply \"remove me\" anytime to opt out."; }
        else if (/^no thanks$/i.test(tx)) { await shoutNote(env, un, uid, { yes: false, asked: true }); sr = "No problem at all 🙏 We won't name you."; }
        else if (/\b(remove me|no tag|untag|don'?t tag)\b/i.test(tx)) { await shoutNote(env, un, uid, { yes: false, asked: true, removed: Date.now() }); sr = "Done, you won't be tagged or named again. 🙏"; }
        else if (/^welcome[.!🙏 ]*$/i.test(tx)) { const r0 = (await kv(env, "shout", {}))[(un || "").toLowerCase()]; sr = r0?.yes ? "You're already on our welcome list 🙌" : SHOUT_Q; if (!r0?.yes) await shoutNote(env, un, uid, { asked: true }); }
        if (sr) { await kvPut(env, `m:${uid}`, meta); thread.push({ role: "user", content: tx }, { role: "assistant", content: sr }); await kvPut(env, key, thread); await sendDM(env, uid, sr, sr === SHOUT_Q ? SHOUT_BTN : []); continue; }
      }
      if (ev.message.reply_to?.story?.id) { meta.sources.push({ via: "story_reply", media: ev.message.reply_to.story.id, t: Date.now() }); if (!meta.topic) meta.topic = await itemTopic(env, await mediaToItem(env, ev.message.reply_to.story.id)); }
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
        const short = ev.message.text.trim().split(/\s+/).length <= 2;   // answers like "home food business" must not trigger the FOOD guide mid-chat
        const dk = short ? ((await uniqueKw(env, ev.message.text))?.base || matchKeyword(ev.message.text)) : null;
        if (dk) { meta.pending_kw = dk; meta.follow_asks = 0; await log(env, `keyword ${dk} via DM from @${meta.username || uid}`); }
      }
      if (meta.pending_kw && KW_TOPIC[meta.pending_kw]) meta.topic = KW_TOPIC[meta.pending_kw];
      const topic = TOPICS[meta.topic] ? meta.topic : "co";
      let reply, buttons = [];
      if (meta.pending_kw && KEYWORD_REPLY[meta.pending_kw]) {
        // soft follow gate: ask to follow, re-check when they say they did, and after two tries send it anyway (never block a lead)
        if (prof.follows === false && (meta.follow_asks || 0) < 2 && !meta.served) {
          meta.follow_asks = (meta.follow_asks || 0) + 1;
          reply = meta.follow_asks === 1 ? FOLLOW_ASK : FOLLOW_RECHECK; buttons = ["I've followed ✅"];
          await log(env, `follow check @${meta.username || uid}: not following (ask ${meta.follow_asks})`);
        } else {
          const pre = prof.follows === false ? "No worries, here it is anyway! 😊" : prof.follows && meta.follow_asks ? "Thanks for following! 🙌 Here you go!" : "";
          reply = pre ? KEYWORD_REPLY[meta.pending_kw].replace(/^Here you go!/, pre) : KEYWORD_REPLY[meta.pending_kw];
          for (const k2 of meta.pending_more || []) if (KEYWORD_REPLY[k2]) reply += "\n\n———\n\nYou also asked on another post:\n\n" + KEYWORD_REPLY[k2].replace(/^Here you go!\s*/, "");
          delete meta.pending_more;
          buttons = NEXT[topic];
          await log(env, `sent ${meta.pending_kw} resource to @${meta.username || uid} (follows: ${prof.follows})`);
          delete meta.pending_kw; meta.follow_asks = 0; meta.served = true;
        }
        await kvPut(env, `m:${uid}`, meta);
      } else { await kvPut(env, `m:${uid}`, meta); reply = await botReply(env, thread, topic); }
      thread.push({ role: "assistant", content: reply });
      await kvPut(env, key, thread); await sendDM(env, uid, reply, buttons);
      let flowDone = false;
      const uMsgs = thread.filter(m => m.role === "user"); const pIdx = uMsgs.findIndex(m => /\d{10}/.test(m.content.replace(/\D/g, "")));
      if (pIdx >= 0 || thread.length >= 12) {
        const lead = await extractLead(env, thread, topic);
        if (lead) {
          const leads = await kv(env, "leads", {}); const prev = leads[uid];
          const meta2 = await kv(env, `m:${uid}`, { sources: [] }); const s0 = meta2.sources[0] || {};
          const fromItem = s0.media ? await mediaToItem(env, s0.media) : "direct";
          flowDone = !!(lead.phone && lead.language);
          const ready = lead.phone && (lead.language || uMsgs.length - 1 - pIdx >= 2);   // wait for the call language (or two more messages) so the alert is complete
          leads[uid] = { ...lead, topic, alerted: prev?.alerted || false, ig_user: uid, source_item: fromItem, source_keyword: s0.keyword || null, source_via: s0.via || "dm", status: prev?.status || "new", updated: IST().toISOString().slice(0, 16) };
          await kvPut(env, "leads", leads); await log(env, `lead ${uid}: ${lead.intent}/${lead.can_afford_30k} from ${fromItem}`);
          if (!prev) await bumpPost(env, fromItem, "leads");
          if (ready && !prev?.alerted && lead.intent !== "low") {
            leads[uid].alerted = true; await kvPut(env, "leads", leads);
            await discord(env, `🔔 **[${TOPICS[topic].label}] New ${lead.intent.toUpperCase()}-intent lead** (budget fit: ${lead.can_afford_30k})\n📞 ${lead.phone}  ·  🗣 ${lead.language || "?"}${lead.role ? "\n🧭 " + lead.role : ""}\n🏢 ${lead.business}\n📍 Came from: ${fromItem}${s0.keyword ? " (" + s0.keyword + ")" : ""}\n👥 ${lead.founders || "-"}${lead.nri ? " (NRI)" : ""}\n📈 ${lead.traction}${lead.interstate ? "\n🚚 " + lead.interstate : ""}\n⏱ ${lead.timeline}\nWhy: ${lead.reason}\nLead ID: ${uid}\nAfter your call, tell Claude: "lead ${uid}: <what happened>"`, true);
          }
        }
      }
      try {   // check-in index: (re)start the clock for this person, or drop them once the flow is complete
        const nx = await kv(env, "nudge", {}); const pe = nx[uid];
        if (pe?.n > 0) nudgeStat(nx, "back");
        for (const [k, v] of Object.entries(nx)) if (k !== uid && k !== "_s" && v.c && !v.li && ((v.u && meta.username && v.u.toLowerCase() === meta.username.toLowerCase()) || v.f === uid)) delete nx[k];
        if (flowDone && meta.username) { const r0 = (await kv(env, "shout", {}))[meta.username.toLowerCase()]; if (!r0?.asked) { await shoutNote(env, meta.username, uid, { asked: true }); thread.push({ role: "assistant", content: SHOUT_Q }); await kvPut(env, key, thread); await sendDM(env, uid, SHOUT_Q, SHOUT_BTN); } }
        if (flowDone || meta.no_nudge) delete nx[uid]; else nx[uid] = { li: meta.last_in, n: 0, tot: pe?.tot || 0, ls: pe?.ls || 0, u: meta.username || pe?.u || null };
        await kvPut(env, "nudge", nx);
      } catch (e9) { await log(env, `check-in index: ${String(e9.message).slice(0, 80)}`); }
    }
    for (const ch of entry.changes || []) {
      if (ch.value?.id) { const dk = `dup:c:${ch.field}:${ch.value.id}`; if (await env.STATE.get(dk)) continue; await env.STATE.put(dk, "1", { expirationTtl: 86400 }); } // keyword comments -> one private reply opens the DM
      if (ch.field !== "comments" || !ch.value?.text) continue;
      const who = ch.value.from?.username || ch.value.from?.id || "?";
      await log(env, `comment from @${who}${ch.value.parent_id ? " (reply in thread)" : ""}: ${ch.value.text.slice(0, 60)}`);
      if ((ch.value.from?.id && ch.value.from.id === env.IG_USER_ID) || (ch.value.from?.username || "").toLowerCase() === OWN_USERNAME) continue;   // our own comments
      const item = await mediaToItem(env, ch.value.media?.id); await bumpPost(env, item, "comments");
      if (ch.value.from?.username) await shoutNote(env, ch.value.from.username, null, "engage");
      if (/^\s*welcome[.!🙏 ]*$/i.test(ch.value.text)) {   // asks to be featured: one private reply with the consent question
        try { await sendMsg(env, { comment_id: ch.value.id }, SHOUT_Q, SHOUT_BTN); await shoutNote(env, ch.value.from?.username, null, { asked: true }); } catch (e) { await log(env, `welcome reply failed: ${e.message}`); }
        continue;
      }
      const uq = await uniqueKw(env, ch.value.text, item);                 // the post's own keyword ("LAUNCH") maps to its general one
      const k0 = uq ? uq.base : matchKeyword(ch.value.text); if (!k0) { await commentReply(env, ch.value, item); continue; } const m = [k0, k0];
      if (uq) { await bumpPost(env, item, "kw:" + uq.kw); await log(env, `own keyword ${uq.kw} (${uq.base}, post ${uq.item})`); }
      await bumpPost(env, item, "kw:" + m[1].toUpperCase());
      if (ch.value.from?.id) {                                       // remember where this person came from, per keyword
        const mk = `m:${ch.value.from.id}`; const meta = await kv(env, mk, { first: Date.now(), sources: [] });
        meta.topic = KW_TOPIC[m[1].toUpperCase()] || meta.topic;
        if (!meta.sources.some(s => s.comment === ch.value.id)) meta.sources.push({ via: "comment", keyword: m[1].toUpperCase(), media: ch.value.media?.id, item, comment: ch.value.id, t: Date.now() });
        await kvPut(env, mk, meta);
      }
      const kw = m[1].toUpperCase();
      try {
        // Until Meta lets the app read incoming DMs (flag dm_inbound), the one private reply carries the whole resource + the callback form.
        const inbound = await env.STATE.get("dm_inbound");
        let hook = "", point = ""; try { const mf = await manifest(env); const it = [...(mf.items || []), ...(mf.carousels || []), ...(mf.posters || [])].find(i => i.id === item); hook = (it?.caption || "").split("\n")[0].replace(/["“”]/g, "").trim(); point = it?.point || ""; } catch (e0) {}
        const r = inbound ? await sendMsg(env, { comment_id: ch.value.id }, KEYWORD_OPENER[kw], ["Yes, send it 👍"])
          : await sendMsg(env, { comment_id: ch.value.id }, directReply(env, kw, item, hook, point));
        if (!inbound && r.recipient_id) { const tk = `t:${r.recipient_id}`; const th = await kv(env, tk, []); th.push({ role: "assistant", content: directReply(env, kw, item, hook, point) }); await kvPut(env, tk, th); }   // so the AI knows what was already sent
        if (r.recipient_id) { const mk = `m:${r.recipient_id}`; const meta = await kv(env, mk, { first: Date.now(), sources: [] });
          if (inbound && meta.pending_kw && meta.pending_kw !== kw) meta.pending_more = [...new Set([...(meta.pending_more || []), meta.pending_kw])].filter(x => x !== kw); if (inbound) meta.pending_kw = kw; meta.topic = KW_TOPIC[kw] || meta.topic; if (!meta.sources.length) meta.sources.push({ via: "comment", keyword: kw, media: ch.value.media?.id, item, comment: ch.value.id, t: Date.now() }); await kvPut(env, mk, meta); }
        await log(env, `private reply to ${kw} comment`);
        try { const nid = r.recipient_id || `c:${ch.value.id}`; const nx = await kv(env, "nudge", {});
          if (!nx[nid]?.li) { nx[nid] = { c: ch.value.id, t: Date.now(), u: ch.value.from?.username || null, f: ch.value.from?.id || null }; await kvPut(env, "nudge", nx); } } catch (e8) {}
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
// Every other genuine comment gets one short public reply (AI, with fixed fallbacks). Spam gets none; emoji-only gets a fixed one.
const CREPLY_CAP = 150;   // per IST day, well under Instagram's comment-spam limits
const CREPLY_EMOJI = ["🙌", "❤️ Thank you!", "😊🙏", "Thank you! 🙌"];
const CREPLY_EN = ["Thank you! 🙌", "Glad this helped 😊 Comment the keyword from the post if you want our free guide.", "Thanks a lot! 🙏 DM us anytime if you need help.", "Appreciate it 😊 More tips coming every day!"];
const CREPLY_ML = ["നന്ദി! 🙌", "വളരെ സന്തോഷം 😊 Free guide വേണമെങ്കിൽ post-ലെ keyword comment ചെയ്യൂ.", "Thank you! 🙏 എന്ത് സംശയവും DM ചെയ്യാം."];
const CREPLY_SYS = `You reply publicly to an Instagram comment for @rejectionlist.kerala, a Kerala team that helps with company registration, GST registration and investor agreements. Write ONE friendly reply, 1-2 short sentences, under 180 characters, in the same language and script the commenter used (Malayalam script, Manglish or English). Warm, a little humour, relevant to their comment and the post. Sometimes (not always) invite them to comment the post's keyword (given below) for the free guide, or to DM us. Never mention any price, fee, cost, discount, offer, "cheap" or "affordable". Never give legal facts, rules, numbers or timelines; at most say our team can help. Never say you are human, AI, a bot or an assistant. Output only the reply text, no quotes.`;
const pick = a => a[Math.floor(Math.random() * a.length)];
function commentKind(text) {   // "spam" | "emoji" (emoji/punctuation/tags only) | "text"
  const t = String(text || "");
  if (/https?:\/\/|www\.|\b[a-z0-9-]+\.(com|in|net|org|ly|io|me|link|xyz)\b|promot|collab|follower|onlyfans|crypto|bitcoin|forex|giveaway|earn (money|\$|₹)|check (my|our) (page|profile|bio)|dm (me|us) for/i.test(t)) return "spam";
  return /^[\p{P}\p{S}\p{Extended_Pictographic}\p{M}\s\u200c\u200d\ufe0f]*$/u.test(t.replace(/@[\w.]+/g, "")) ? "emoji" : "text";
}
function cleanReply(s) {   // sanitise AI output; "" when unusable so the caller falls back
  let t = String(s || "").replace(/^\s*(reply|response|answer)\s*:\s*/i, "").replace(/["“”«»]/g, "").replace(/^['‘’`\s]+|['‘’`\s]+$/g, "").replace(/@[\w.]+/g, "").replace(/\s+/g, " ").trim();
  if (!t || /₹|\brs\.?\s*\d|\binr\b|price|\bfees?\b|\bcost|charge|discount|\boffer|cheap|afford|budget|lakh|\d{3,}|section\s*\d|\bact\b|\b(ai|bot|chatbot|chatgpt|assistant|automated|language model|human)\b|ഫീസ്|രൂപ|ചാർജ്|വില/i.test(t)) return "";
  if (t.length > 200) { t = t.slice(0, 200); const c = Math.max(t.lastIndexOf(". "), t.lastIndexOf("! "), t.lastIndexOf("? ")); t = c > 40 ? t.slice(0, c + 1) : t.replace(/\s+\S*$/, "") + "…"; }
  return t.length >= 2 ? t : "";
}
async function commentReply(env, c, item) {   // c = webhook comment value; never called for our own comments
  const kind = commentKind(c.text); if (kind === "spam") { await log(env, `comment skipped (spam): @${c.from?.username || "?"}`); return; }
  const ck = `creply:${IST().toISOString().slice(0, 10)}`; const n = +(await env.STATE.get(ck) || 0);
  if (n >= CREPLY_CAP) { if (n === CREPLY_CAP) { await env.STATE.put(ck, String(n + 1), { expirationTtl: 172800 }); await log(env, `comment reply cap (${CREPLY_CAP}/day) reached`); } return; }
  const uk = `cru:${IST().toISOString().slice(0, 10)}:${c.from?.id || c.from?.username || "?"}`; const un = +(await env.STATE.get(uk) || 0);
  if (un >= 2) return;   // at most 2 replies per person per day, so a "thanks" exchange can't go back and forth
  const ml = /[\u0D00-\u0D7F]/.test(c.text);
  let msg = kind === "emoji" ? pick(CREPLY_EMOJI) : "";
  if (!msg) {
    let hook = "", point = "", kwBase = ""; try { const mf = await manifest(env); const it = [...(mf.items || []), ...(mf.carousels || []), ...(mf.posters || [])].find(i => i.id === item); hook = (it?.caption || "").split("\n")[0].replace(/["“”]/g, "").trim(); point = it?.point || ""; kwBase = it?.base || ""; } catch (e0) {}
    try { const r = await env.AI.run("@cf/meta/llama-3.3-70b-instruct-fp8-fast", { messages: [{ role: "system", content: CREPLY_SYS },
      { role: "user", content: `Post hook: ${hook.slice(0, 120) || "?"}\nPost point: ${point.slice(0, 200) || "?"}\nPost keyword: ${kwBase || "START"}\nComment: ${c.text.slice(0, 300)}` }], max_tokens: 90 });
      msg = cleanReply(r.response); } catch (e) { await log(env, `AI unavailable for comment reply: ${String(e.message).slice(0, 80)}`); }
    if (!msg) msg = pick(ml ? CREPLY_ML : CREPLY_EN);
  }
  const u = c.from?.username;   // Instagram only takes replies on top-level comments: answer a thread reply under its parent, tagging them
  const target = c.parent_id || c.id; if (c.parent_id && u) msg = `@${u} ${msg}`;
  try { await graph(env, `${target}/replies`, { message: msg }); await env.STATE.put(ck, String(n + 1), { expirationTtl: 172800 }); await env.STATE.put(uk, String(un + 1), { expirationTtl: 172800 }); await log(env, `comment reply: @${u || c.from?.id || "?"}`); }
  catch (e) { await log(env, `comment reply failed: ${e.message}`); }
}
const STORY_THANKS = "Thanks a lot for sharing us in your story! 🙌 If you or a friend need help with company registration, GST registration or an investor agreement, just reply here.";
async function storyMention(env, uid) {   // one thank-you DM per person per 7 days; not a lead message
  if (!uid || await env.STATE.get(`sm:${uid}`)) return;
  try { await sendDM(env, uid, STORY_THANKS); await env.STATE.put(`sm:${uid}`, "1", { expirationTtl: 7 * 86400 });
    const th = await kv(env, `t:${uid}`, []); th.push({ role: "assistant", content: STORY_THANKS }); await kvPut(env, `t:${uid}`, th);   // so a reply continues naturally
    await log(env, `story mention thanks: ${uid}`); }
  catch (e) { await log(env, `story mention thanks failed: ${e.message}`); }
}
const FOLLOW_ASK = "Almost there! 🙌 Please follow @rejectionlist.kerala (we share useful tips every day on company registration, GST and investor agreements), then tap the button below and we'll send it right away.";
const FOLLOW_RECHECK = "Hmm, we can't see your follow yet 🤔 Open our profile, tap Follow, then tap the button again.";
const NEXT_BUTTONS = ["Talk to our team", "Which type suits me?", "Documents needed"];
const NEXT = { co: NEXT_BUTTONS, gst: ["Talk to our team", "Do I need GST?", "GST documents"], inv: ["Talk to our team", "I'm raising funds", "I'm investing"],
  sui: ["Talk to our team", "Am I eligible?", "What do I get?"], ...Object.fromEntries(Object.entries(NEWT).map(([t, c]) => [t, c.next])), ud: ["Talk to our team", "Micro, small or medium?", "Late payments?"], sk: ["Talk to our team", "Am I eligible?", "Which grants?"] };
async function itemTopic(env, item) { try { const mf = await manifest(env); const it = [...(mf.items || []), ...(mf.carousels || []), ...(mf.posters || []), ...(mf.stories || [])].find(i => i.id === item); return it?.topic || (it?.reel ? topicOf((mf.items || []).find(i => i.id === it.reel)) : "co"); } catch (e) { return "co"; } }
// First private reply is short and asks for a reply: a reply moves the chat into their main inbox,
// then the full resource (KEYWORD_REPLY) follows.
const BASE = "https://rl-kerala-autopilot.venturenavigatorworkshop.workers.dev";
function directReply(env, kw, item, hook, point) {   // one DM: the post's takeaway + the full resource, ending with the first question (details are collected in DM)
  let body = KEYWORD_REPLY[kw].replace(/^Here you go!\s*/, "");
  const head = hook ? `Hi! 👋 You commented on our post “${hook.slice(0, 70)}”. Here's what you asked for:` : "Hi! 👋 Thanks for your comment. Here's what you asked for:";
  if (point) body = `📌 From this post: ${point.slice(0, 160)}\n\n${body}`;
  return `${head}\n\n${body}`.slice(0, 990);
}
const esc = v => String(v || "").replace(/[<>&"]/g, c => ({ "<": "&lt;", ">": "&gt;", "&": "&amp;", '"': "&quot;" }[c])).slice(0, 300);
function talkPage(k, i, done) {
  const css = "font-family:system-ui,sans-serif;max-width:480px;margin:0 auto;padding:20px;line-height:1.5;color:#1a1a1a";
  if (done) return `<!doctype html><meta charset=utf-8><meta name=viewport content="width=device-width,initial-scale=1"><title>Thank you</title><body style="${css}"><h2>Thank you! 🙌</h2><p>Our team will call you soon in the language you chose.</p><p>നന്ദി! ഞങ്ങളുടെ ടീം ഉടൻ നിങ്ങളെ വിളിക്കും.</p><p>@rejectionlist.kerala</p></body>`;
  const sel = (n, label, opts) => `<label>${label}<select name=${n} required style="width:100%;padding:10px;margin:4px 0 14px;font-size:16px"><option value="">Select</option>${opts.map(o => `<option>${o}</option>`).join("")}</select></label>`;
  const inp = (n, label, extra = "") => `<label>${label}<input name=${n} ${extra} style="width:100%;padding:10px;margin:4px 0 14px;font-size:16px;box-sizing:border-box"></label>`;
  return `<!doctype html><meta charset=utf-8><meta name=viewport content="width=device-width,initial-scale=1"><title>Rejection List Kerala</title><body style="${css}">
<h2>Company registration: get a call from our team</h2><p>കമ്പനി രജിസ്ട്രേഷനെക്കുറിച്ച് ഞങ്ങളുടെ ടീം നിങ്ങളെ വിളിക്കും. 30 സെക്കൻഡ് മതി.</p>
<form method=post action="/talk"><input type=hidden name=k value="${esc(k)}"><input type=hidden name=i value="${esc(i)}"><input name=website style="display:none" tabindex=-1 autocomplete=off>
${inp("name", "Your name / പേര്", "required maxlength=60")}${inp("phone", "Phone (WhatsApp) / ഫോൺ നമ്പർ", "required type=tel pattern='[0-9+ ]{10,15}' maxlength=15")}
${sel("language", "Call me in / ഏത് ഭാഷയിൽ സംസാരിക്കണം", ["Malayalam", "English"])}
${inp("business", "What is your business? / എന്താണ് ബിസിനസ്?", "required maxlength=200")}
${sel("stage", "Where are you now? / ഇപ്പോൾ എവിടെയാണ്?", ["Already running, getting income", "Have clients / orders waiting", "Just starting", "Only an idea for now", "Company registered, need help after"])}
${sel("founders", "Who is starting it? / ആരൊക്കെ?", ["Just me", "Me with partners", "Family business"])}
${sel("where", "Where do you live? / താമസം", ["Kerala", "Gulf / abroad (NRI)", "Other state in India"])}
${sel("when", "When do you want to register? / എപ്പോൾ?", ["This week", "This month", "In 1 to 3 months", "Not sure yet"])}
<button style="width:100%;padding:14px;font-size:17px;background:#e8590c;color:#fff;border:0;border-radius:8px">Request a call / കോൾ വേണം</button></form>
<p style="font-size:12px;color:#666">We use these details only to call you. <a href="/privacy">Privacy</a></p></body>`;
}
async function talkSubmit(env, f) {
  if (f.get("website")) return;                                     // bots fill the hidden field
  const phone = String(f.get("phone") || "").replace(/[^0-9+]/g, ""); if (phone.replace(/\D/g, "").length < 10) return;
  const stage = String(f.get("stage") || ""), when = String(f.get("when") || "");
  const strong = /running|clients|registered/i.test(stage), soon = /week|month$/i.test(when) || when === "This month";
  const intent = strong && soon ? "high" : strong || soon ? "medium" : "low";
  const fit = strong ? "likely" : /starting/i.test(stage) ? "unclear" : "unlikely";
  const id = "f" + Date.now().toString(36); const item = String(f.get("i") || "direct").slice(0, 60), kw = String(f.get("k") || "").slice(0, 20);
  const lead = { name: esc(f.get("name")), phone, language: esc(f.get("language")), business: esc(f.get("business")), traction: esc(stage), founders: esc(f.get("founders")), nri: /Gulf/.test(String(f.get("where"))), where: esc(f.get("where")), timeline: esc(when), intent, can_afford_30k: fit,
    source_item: item, source_keyword: kw, source_via: "form", status: "new", updated: IST().toISOString().slice(0, 16) };
  const leads = await kv(env, "leads", {}); leads[id] = lead; await kvPut(env, "leads", leads); await bumpPost(env, item, "leads");
  await log(env, `form lead ${id}: ${intent}/${fit} from ${item}`);
  await discord(env, `🔔 **New ${intent.toUpperCase()}-intent lead** (budget fit: ${fit})\n👤 ${lead.name}\n📞 ${phone}  ·  🗣 ${lead.language}\n🏢 ${lead.business}\n📈 ${lead.traction}\n👥 ${lead.founders} · ${lead.where}\n⏱ ${lead.timeline}\n📍 Came from: ${item}${kw ? " (" + kw + ")" : ""}\nLead ID: ${id}\nAfter your call, tell Claude: "lead ${id}: <what happened>"`, true);
}
const KEYWORD_OPENER = {
  START: "Hi! 👋 Thanks for your comment. Want a quick guide on which company type suits you: OPC, Private Limited or LLP? Tap the button below.",
  NAME: "Hi! 👋 Thanks for your comment. Want our tips to keep your company name from getting rejected? Tap the button below.",
  AFTER: "Hi! 👋 Thanks for your comment. Want the checklist for the first 180 days after registration? Tap the button below.",
  CHECKLIST: "Hi! 👋 Thanks for your comment. Want the list of documents you need for registration? Tap the button below.",
  GST: "Hi! 👋 Thanks for your comment. Want our quick guide on when you need GST registration? Tap the button below.",
  LIMIT: "Hi! 👋 Thanks for your comment. Want the GST turnover limits and the cases where GST is needed from day one? Tap the button below.",
  PENALTY: "Hi! 👋 Thanks for your comment. Want the list of GST penalties and late fees to avoid? Tap the button below.",
  INVEST: "Hi! 👋 Thanks for your comment. Want our checklist of the agreements to sign before money comes in? Tap the button below.",
  TERMSHEET: "Hi! 👋 Thanks for your comment. Want our guide on what a term sheet binds you to? Tap the button below.",
  FUNDING: "Hi! 👋 Thanks for your comment. Want the legal steps after an investor says yes? Tap the button below.",
  DPIIT: "Hi! 👋 Thanks for your comment. Want our quick check on whether your startup can get Startup India (DPIIT) recognition? Tap the button below.",
  BENEFITS: "Hi! 👋 Thanks for your comment. Want the list of what DPIIT recognition actually opens up? Tap the button below.",
  ...Object.fromEntries(Object.values(NEWT).flatMap(c => Object.entries(c.kws).map(([k, v]) => [k, `Hi! 👋 Thanks for your comment. ${v[0]} Tap the button below.`]))),
  UDYAM: "Hi! 👋 Thanks for your comment. Want our quick guide to Udyam (MSME) registration and what it protects? Tap the button below.",
  MSME: "Hi! 👋 Thanks for your comment. Want to know if your business is micro, small or medium under the new limits? Tap the button below.",
  KSUM: "Hi! 👋 Thanks for your comment. Want our guide to the Kerala Startup Mission Unique ID? Tap the button below.",
  GRANT: "Hi! 👋 Thanks for your comment. Want the checklist you need before applying for a KSUM grant? Tap the button below.",
};
const KEYWORD_REPLY = {
  START: "Here you go!\n\nIn short:\n• Starting alone: OPC (One Person Company)\n• 2+ founders, may raise funding later: Private Limited\n• Partners, no funding plans: LLP is also an option\n\nWe'll help you pick the right one. What does your business do?",
  NAME: "Here you go! How to keep your company name from being rejected:\n\n1. It must not be similar (even in sound) to an existing company or LLP name\n2. It must not clash with a registered trademark\n3. Words like Bank or Insurance need special approval\n4. Keep 2–3 backup names ready\n\nSend us the name you have in mind and we'll give a first review against these rules. Final availability is confirmed when the application is filed.",
  AFTER: "Here you go! Your checklist after registration:\n\n✅ Within 30 days: appoint the first auditor\n✅ Open a current account in the company's name\n✅ Within 180 days: file the commencement of business declaration (INC-20A). Missing it means a penalty of Rs 50,000 on the company\n✅ Annual filings every year, even with zero revenue. Late fee of Rs 100 per day per form\n\nHow long ago was your company registered?",
  CHECKLIST: "Here you go! Documents needed for registration:\n\n📄 For each director: PAN, Aadhaar/ID, address proof (bank statement or utility bill), photo\n🏠 For the office: a recent electricity/water bill + owner's NOC (your home works too)\n📝 2–3 company name options\n\nA Private Limited needs at least 2 directors (one must live in India). How many founders are there?",
  GST: "Here you go! When you need GST registration (Kerala):\n\n✅ Turnover above Rs 40 lakh a year for goods, or Rs 20 lakh for services\n✅ From the first sale, whatever the turnover: selling goods to another state, including online to buyers in other states (Amazon, Flipkart, Meesho)\n✅ Below the limit and selling online only within Kerala: a PAN-based enrolment may be enough, if the marketplace allows it\n✅ Anyone can also register voluntarily (many B2B clients ask for your GSTIN)\n\n📄 A proprietor needs: PAN, Aadhaar with its linked mobile, photo, business address proof, bank proof\n\nWhat does your business sell or do?",
  LIMIT: "Here you go! GST limits in Kerala:\n\n📊 Goods: registration needed above Rs 40 lakh turnover a year\n📊 Services: above Rs 20 lakh a year\n⚠️ No limit applies (GST from day one) if you sell goods to other states, including online orders from other states\n🧾 Composition scheme (simpler, lower rate, no input credit): up to Rs 1.5 crore for goods, Rs 50 lakh for services\n\nRoughly how much turnover do you expect this year?",
  PENALTY: "Here you go! GST penalties to avoid:\n\n⚠️ Not registering when you must: the tax you should have collected, 18% interest, and a penalty of Rs 10,000 or 10% of the tax due, whichever is higher\n⚠️ Late GSTR-3B: Rs 50 a day (Rs 20 a day for a nil return), even if there were no sales\n⚠️ Unpaid tax: 18% a year interest\n\nIs your business already GST-registered?",
  INVEST: "Here you go! Before an investor's money comes in:\n\n📝 Term sheet: the agreed terms, mostly non-binding\n📝 Share subscription agreement: the money, the shares, the conditions\n📝 Shareholders' agreement: board seat, share transfer limits, exits\n🏢 Update the company's articles so those rights bind the company\n⏱ Allot shares within 60 days of receiving the money\n\nOnly a private limited company can take equity investment. Are you a founder raising money, or an investor putting money in?",
  TERMSHEET: "Here you go! What a term sheet binds you to:\n\n🔓 Usually NOT binding: valuation, amount, board seats, other commercial terms\n🔒 Usually binding from signing: confidentiality, exclusivity (no talking to other investors for a set period), costs, governing law\n\nRead the exclusivity period carefully before you sign. Are you a founder or an investor?",
  DPIIT: "Here you go! Can your startup get DPIIT (Startup India) recognition?\n\n✅ A private limited company, LLP, registered partnership or cooperative (a proprietorship has to register an entity first)\n✅ Less than 10 years since registration\n✅ Turnover never above Rs 200 crore in any year\n✅ Working on something innovative, or a business model that can scale\n\nWhat does your startup do, and what is new about it?",
  BENEFITS: "Here you go! What DPIIT recognition opens up:\n\n🧾 Rebates on patent and trademark filing fees, and faster examination\n📋 Self-certification under several labour and environment laws\n🏛 Eligibility for many government and state startup schemes, tenders and grants (Kerala's KSUM grants usually ask for it)\n💰 The right to APPLY for the 3-year income tax holiday (section 80-IAC), which is a separate approval\n\nWhat does your startup do, and what is new about it?",
  ...Object.fromEntries(Object.values(NEWT).flatMap(c => Object.entries(c.kws).map(([k, v]) => [k, v[1]]))),
  UDYAM: "Here you go! Udyam (MSME) registration in short:\n\n🆔 The government's MSME registration: Aadhaar-based, with PAN (and GSTIN if you have one), no renewal\n💸 Manufacturing and service micro/small units: buyers must pay within 45 days, or owe compound interest at 3x the RBI bank rate; delays can go to the MSME Samadhaan portal\n🏦 Helps with priority lending, collateral-free loan schemes and government tenders\n🛒 Traders can register too, but only for priority lending (no 45-day protection)\n\nWhat does your business do: manufacturing, a service or trading?",
  MSME: "Here you go! MSME limits since 1 April 2025 (both must be met):\n\n🔹 Micro: investment up to Rs 2.5 crore AND turnover up to Rs 10 crore\n🔹 Small: up to Rs 25 crore AND Rs 100 crore\n🔹 Medium: up to Rs 125 crore AND Rs 500 crore\n\nIf you cross either limit you move up a category. What does your business do: manufacturing, a service or trading?",
  KSUM: "Here you go! The Kerala Startup Mission (KSUM) Unique ID:\n\n🆔 KSUM's grants, incubation, programmes and events are for startups that hold this ID\n🏢 The startup should be registered in Kerala, usually as a private limited company or LLP\n📜 Most KSUM schemes also ask for Startup India (DPIIT) recognition\n\nWhat does your startup do?",
  GRANT: "Here you go! Before you apply for a KSUM grant:\n\n1. Register the startup in Kerala (private limited company or LLP)\n2. Get Startup India (DPIIT) recognition\n3. Get the KSUM Unique ID\n4. Keep your pitch, prototype and plan for using the money ready\n\nFor the idea grant you may apply before step 1, but the company and Unique ID are needed before any money is released. What does your startup do?",
  FUNDING: "Here you go! Legal steps after an investor says yes:\n\n1. Sign the term sheet\n2. Share subscription + shareholders' agreements\n3. Board and shareholder approvals, offer letter (PAS-4), money into a separate bank account\n4. Allot shares within 60 days, file PAS-3 within 15 days of allotment (the money can be used only after that)\n5. NRI or foreign investor on repatriation basis: report to RBI (FC-GPR) within 30 days of allotment\n\nAre you a founder raising money, or an investor putting money in?",
};

async function postKind(env, what, topic = "co") {
  const left = await quotaLeft(env);   // never run into Instagram's 24 h limit: skip and log instead
  if (left !== null && left <= 1) { await log(env, `SKIP ${topic} ${what}: Instagram 24 h posting limit nearly used (${left} left)`); await alertOnce(env, "quota", `⚠️ Instagram's 24-hour posting limit is nearly used; skipped a ${TOPICS[topic].label} ${what}. Planned volume will be lowered by the monitor if this repeats.`); return; }
  return what === "reel" || what === "tip" || what === "news" ? postReel(env, topic, what) : what === "story" ? postStory(env, topic) : what === "poster" ? postPoster(env, topic) : postCarousel(env, topic);
}

// ---------------- entry points ----------------
export default {
  async scheduled(ev, env, ctx) {
    const now = IST(); const h = now.getUTCHours(), mi = now.getUTCMinutes();
    const day = now.toISOString().slice(0, 10);
    const plan = await planDay(env, day);
    let slot = null;   // slots can sit 4 min apart now: take the first due one not yet done (KV is read only for slots due now)
    for (const x of slotsFor(plan)) { const xm = x[0] * 60 + x[1], nm = h * 60 + mi; if (nm >= xm && nm - xm < 5 && !(await env.STATE.get(`slot:${day}:${x[0]}:${x[1]}`))) { slot = x; break; } }
    // the 03:xx snapshot chunks use most of the 50-subrequest budget, so skip the backup inbox poll while they run
    const snapRun = h === 3 && mi >= 1 && !(await env.STATE.get(`snapdone:${day}`));
    if (IST().getUTCDay() === 0 && h === 9 && mi === 41 && !(await env.STATE.get(`shoutplan:${day}`))) { await env.STATE.put(`shoutplan:${day}`, "1", { expirationTtl: 172800 }); ctx.waitUntil(shoutPlan(env).catch(e => log(env, `shout plan: ${e.message}`))); }
    if (h === 12 && mi === 47 && !(await env.STATE.get(`shoutpost:${day}`))) { await env.STATE.put(`shoutpost:${day}`, "1", { expirationTtl: 172800 }); ctx.waitUntil(shoutPost(env).catch(e => log(env, `shout post: ${e.message}`))); }
    if (!snapRun && await env.STATE.get("poll_inbox")) ctx.waitUntil((async () => {   // backup route, off while Meta delivers DMs by webhook                                    // check the inbox every 10 s so replies feel instant
      const t0 = Date.now();
      for (let k = 0; k < 6; k++) {
        try { await pollInbox(env); } catch (e) { await alertOnce(env, "pollerr", `⚠️ Inbox check failing: ${e.message}`); }
        const wait = t0 + (k + 1) * 10000 - Date.now(); if (k < 5 && wait > 0) await new Promise(r => setTimeout(r, wait));
      }
    })());
    try {
      if (slot) {
        const k = `slot:${day}:${slot[0]}:${slot[1]}`;
        if (!(await env.STATE.get(k))) {
          await env.STATE.put(k, "1", { expirationTtl: 172800 });
          try { await postKind(env, slot[2], slot[3]); }
          catch (e) {   // one retry ~10 min later covers most temporary Instagram errors
            await kvPut(env, "retry", { what: slot[2], topic: slot[3], at: Date.now() + 10 * 60e3 });
            await log(env, `ERROR ${slot[3]} ${slot[2]} post failed, retrying in 10 min: ${e.message}`);
            await discord(env, `⚠️ [${TOPICS[slot[3]].label}] ${slot[2]} post failed, retrying in 10 min: ${e.message}`);
          }
        }
      }
      const retry = await kv(env, "retry", null);
      if (retry && Date.now() >= retry.at) {
        await env.STATE.delete("retry");
        try { await postKind(env, retry.what, retry.topic || "co"); await log(env, `retry of ${retry.what} succeeded`); }
        catch (e) { throw new Error(`${retry.what} retry also failed: ${e.message}`); }
      }
      try { await processNudges(env); } catch (eN) { await log(env, `ERROR check-ins: ${String(eN.message).slice(0, 90)}`); }
      if (snapRun) await snapshotTick(env, day);
      if (h === 21 && mi === 41) {
        const posted = await kv(env, "posted", {}); const todayP = Object.values(posted).filter(p => IST(new Date(p.t)).toISOString().slice(0, 10) === day); const today = todayP.length;
        const leads = Object.values(await kv(env, "leads", {})).filter(l => (l.updated || "").startsWith(day));
        const per = Object.keys(plan.plan).map(t => `[${TOPICS[t].label}] ${todayP.filter(p => topicOf(p) === t).length} posts, ${leads.filter(l => (l.topic || "co") === t).length} leads`).join("\n");
        const errs = (await kv(env, "log", [])).filter(l => l.startsWith(day) && /ERROR|NO .*STOCK/.test(l)).length;
        const nx = await kv(env, "nudge", {}); const ns = nx._s?.day === day ? nx._s : {}; const waiting = Object.keys(nx).filter(k => k !== "_s").length;
        await discord(env, `📊 Daily report ${day}: ${today} posts · ${leads.length} leads today · ${errs} problems\n${per}\n💬 Check-ins: ${ns.sent || 0} DMs + ${ns.pub || 0} comment replies sent · ${ns.back || 0} people came back · ${waiting} chats still waiting`);
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
      const role = await opsOk(env, req.headers.get("x-ops-key"));
      if (!role || (role === "monitor" && !(await monitorAllowed(req, u)))) return new Response("no", { status: 403 });
      if (u.pathname === "/ops/leads") { const L = await kv(env, "leads", {}); if (role === "owner") return json(L);
        return json(Object.fromEntries(Object.entries(L).map(([id, l]) => [id, { has_phone: !!l.phone, language: l.language || "", intent: l.intent, alerted: !!l.alerted, source_item: l.source_item || null, t: l.t || null }]))); }
      if (u.pathname === "/ops/insights") {
        const posted = await kv(env, "posted", {}); const out = {};
        for (const id of Object.keys(posted).filter(i => Date.now() - posted[i].t < 7 * 86400e3)) out[id] = { posted: posted[id], events: await kv(env, `ev:${id}`, null), snapshots: await kv(env, `snap:${id}`, []) };
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
      if (u.pathname === "/ops/nudge") return json(await kv(env, "nudge", {}));
      if (u.pathname === "/ops/run" && req.method === "POST") { const { what, id, topic: tq } = await req.json(); if (what === "nudge") return json(await processNudges(env, id || null)); if (what === "snapshot") await snapshot(env); if (what === "optimise") await optimise(env);
        if (what === "poll") { await pollInbox(env); return json({ ok: true }); } const tp = TOPICS[tq] ? tq : "co";
        if (["reel", "story", "carousel", "poster"].includes(what)) await postKind(env, what, tp);
        if (what === "slots") { const d = IST().toISOString().slice(0, 10); const P = await planDay(env, u.searchParams.get("day") || d); return json({ ...P, slots: slotsFor(P) }); } return json({ ok: true }); }
      if (u.pathname === "/ops/graph" && req.method === "POST") {      // diagnostics: one Graph API call with the app's token
        const { path, params, method, ig } = await req.json();   // ig: true = Instagram-login app token on graph.instagram.com
        const g = new URL(ig ? `https://graph.instagram.com/v24.0/${path}` : `${env.GRAPH}/${path}`); const b = new URLSearchParams({ ...(params || {}), access_token: ig ? await env.STATE.get("ig_login_token") : env.IG_TOKEN });
        const r = (method || "GET") === "GET" ? await fetch(`${g}?${b}`) : await fetch(g, { method, body: b }); return json(await r.json());
      }
      if (u.pathname === "/ops/settoken" && req.method === "POST") {   // store the Instagram-login token (never logged)
        const { token } = await req.json(); const r = await (await fetch(`https://graph.instagram.com/v24.0/me?fields=user_id,username&access_token=${encodeURIComponent(token)}`)).json();
        if (r.error) return json({ ok: false, error: r.error.message }); await env.STATE.put("ig_login_token", token); await env.STATE.put("ig_login_token_set", String(Date.now())); return json({ ok: true, username: r.username, user_id: r.user_id });
      }
      if (u.pathname === "/ops/flag" && req.method === "POST") { const { k, v } = await req.json(); if (/^stage_(hold|force)(_[a-z]+)?$/.test(k) || k === "daily_cap" || k === "low_reach_mode" || k === "reel_cap") { v === null || v === undefined || v === "" ? await env.STATE.delete(k) : await env.STATE.put(k, String(+v)); return json({ ok: true, k, v }); }
        if (!["dm_inbound", "poll_inbox"].includes(k)) return json({ ok: false }); v ? await env.STATE.put(k, "1") : await env.STATE.delete(k); return json({ ok: true, k, v: !!v }); }
      if (u.pathname === "/ops/correct" && req.method === "POST") {   // correction note on a reel that had wrong info (never deletes it)
        const { media, text } = await req.json(); if (!/^\d+$/.test(String(media || "")) || !text || String(text).length > 900) return json({ error: "media id and text (<=900 chars) needed" }, 400);
        const r = await graph(env, `${media}/comments`, { message: String(text) }); await log(env, `correction comment on ${media}`); return json({ ok: true, comment: r.id });
      }
      if (u.pathname === "/ops/extra" && req.method === "POST") { const { carousels } = await req.json(); await kvPut(env, "extra_carousels", carousels || []); return json({ ok: true, n: (carousels || []).length }); }
      if (u.pathname === "/ops/status") return json({ now_ist: IST().toISOString(), posted: await kv(env, "posted", {}), log: (await kv(env, "log", [])).slice(0, 80) });
    }
    if (u.pathname === "/talk" && req.method === "GET") return new Response(talkPage(u.searchParams.get("k"), u.searchParams.get("i"), u.searchParams.get("done")), { headers: { "content-type": "text/html; charset=utf-8" } });
    if (u.pathname === "/talk" && req.method === "POST") { try { await talkSubmit(env, await req.formData()); } catch (e) { await log(env, `ERROR form ${e.message}`); } return Response.redirect(`${u.origin}/talk?done=1`, 303); }
    if (u.pathname === "/privacy" || u.pathname === "/data-deletion" || u.pathname === "/terms") return new Response(`<!doctype html><meta charset=utf-8><meta name=viewport content="width=device-width"><title>Rejection List Kerala - ${u.pathname.slice(1)}</title><body style="font-family:sans-serif;max-width:720px;margin:40px auto;padding:0 16px;line-height:1.6"><h1>Rejection List Kerala</h1>
<h2>Privacy policy</h2><p>This app is used only by the Instagram account @rejectionlist.kerala (Rejection List - India) to publish its own posts and to reply to people who comment on its posts or send it a direct message.</p>
<p><b>What we collect:</b> your Instagram user ID and username, the comments and messages you send to @rejectionlist.kerala, and any details you choose to share in that conversation (for example your name, phone number, preferred language and business plans).</p>
<p><b>Why:</b> only to answer your questions about company registration and to let our team contact you if you ask us to. We do not sell or share your data with advertisers or other third parties.</p>
<p><b>Where it is stored:</b> on Cloudflare (our hosting provider). Conversation data is kept for up to 12 months and then deleted.</p>
<h2>Data deletion</h2><p>To delete your data, send the word <b>DELETE</b> as a direct message to @rejectionlist.kerala on Instagram, or ask us in any message. We remove your conversation and details within 7 days and confirm when done.</p>
<h2>Terms</h2><p>Information shared in replies is general guidance about company registration, not legal advice.</p>
<p>Contact: send a direct message to @rejectionlist.kerala on Instagram.</p></body>`, { headers: { "content-type": "text/html; charset=utf-8" } });
    if (u.pathname === "/public/shoutqueue") return json((await kv(env, "shout_queue", [])).map(q => ({ id: q.id, kind: q.kind, month: q.month || null, names: q.names })));   // only people who said yes
    if (u.pathname === "/public/insights") {   // performance per post for the script writer: no names, numbers or messages
      const posted = await kv(env, "posted", {}); const leads = Object.values(await kv(env, "leads", {})); const posts = []; const judged = await kv(env, "judged", {});
      for (const [id, p] of Object.entries(posted)) {
        if (p.kind === "story") continue;
        const r = judged[id] || {};
        const L = leads.filter(l => l.source_item === id);
        posts.push({ id, topic: topicOf(p), theme: p.theme || null, kind: p.kind, segment: p.segment || null, scene: p.scene || null, layout: p.layout || null, posted_at: IST(new Date(p.t)).toISOString().slice(0, 16), judged_at_days: r.age_days ?? null,
          reach: r.reach ?? null, views: r.views ?? null, avg_watch_s: r.ig_reels_avg_watch_time != null ? Math.round(r.ig_reels_avg_watch_time / 100) / 10 : null, shares: r.shares ?? null, saved: r.saved ?? null, likes: r.likes ?? null, comments: r.comments ?? null,
          keyword_comments: r.keyword_comments ?? null, dms: r.dms ?? null, leads: L.length, high_intent: L.filter(l => l.intent === "high").length, nri_leads: L.filter(l => l.nri).length, budget_likely: L.filter(l => l.can_afford_30k === "likely").length });
      }
      const nx = await kv(env, "nudge", {});
      return json({ updated: IST().toISOString().slice(0, 16), weights: await kv(env, "weights", null), slot_report: await kv(env, "slot_report", null),
        leads_total: leads.length, leads_by_topic: leads.reduce((a, l) => { const k = l.topic || "co"; a[k] = (a[k] || 0) + 1; return a; }, {}), leads_by_segment_of_post: leads.reduce((a, l) => { const p = posted[l.source_item]; const k = p?.segment || "direct"; a[k] = (a[k] || 0) + 1; return a; }, {}),
        checkins_today: nx._s || null, posts });
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

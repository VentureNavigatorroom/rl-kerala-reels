# Standing rules for the scheduled tasks (read first; overrides older task text)

Also read GROWTH_PLAN.md every run: it has the checkpoints and decision rules (low watch time, reach drop, funnel, topic shares (reduce, never drop below 5%), research of other causes, backups).

## Reel-max mode (owner, 19 Nov 2026)
While the account has fewer than 100 followers and KV `low_reach_mode` is not "0":
- **What posts:** from 20 Nov every slot is a reel. No carousels, stories or posters; they reach about 0 people without followers.
- **How many:** the total ramps to 40 (20 Nov), 60 (21 Nov), 80 (22 Nov), then 90 a day (REEL_RAMP in worker/src/index.js).
- **Topic split (19 Nov evening, 14 topics):** co 11%, and 6.8% each for val (company valuation, any purpose; prefix qv, keywords VALUATION/WORTH),  gst, inv, sui, sk, ud, tm (trademark), roc (ROC annual compliance), fssai, iec, nda, cfa (co-founder agreements), fp (financial projections) (REEL_SHARE). Folders bank/<topic>/; id prefixes tm, rc, fs, ie, nd, cf, fp; facts in factory/topics.py FACTS_*; DM texts in NEWT in the worker. Earlier split was, limited by each topic's built stock. Leftovers go to topics with stock. ud = Udyam (MSME), added 19 Nov: bank/ud/, ids start with "y".
- **When the plan is set:** it is frozen once a day in KV `plan:<day>`, at the first cron tick after midnight.

## Script-writer runs (19 Nov, after two runs wrote the same topics at once)
- **Ops key:** if ~/.rl_ops_key is missing, recreate it from the setup line in the monitor task's instructions (list_triggers, "Monitor rejectionlist.kerala automation"). Never print or commit it. If that is not possible, say so in the summary and carry on with the manifest and bank counts.
- **14 topics, not 5:** the refill prompt still lists 5. Use topics.DIRS and check_bank.py PREFIX: co, gst g, inv v, sui u, sk m, ud y, tm tm, roc rc, fssai fs, iec ie, nda nd, cfa cf, fp fp, val qv. Count scripts in bank/ too: the manifest lags for new topics.
- **Another session may be writing at the same time:** git pull right before writing and again before committing; use the next free batchNN.py at that moment. Before writing for a topic, read every existing hook, situation and fact in that topic (including commits from the last few hours) and repeat none. If the push is rejected: pull --rebase, keep the other run's files, renumber yours, drop near-duplicates, re-run check_bank, push.

## Refill priority
Reel scripts are the bottleneck.
- **New topics first:** give gst, inv, sui and sk most of each run until each has 40+ unbuilt or unposted reel scripts. After that, keep every topic at 3+ days of its live share. 90/day x share = about 11 reels a day for co and about 6-7 for each other topic. Backup target per topic: 7+ days = ~50 scripts each.
- **Skip carousels and stories** while reel-max mode is on, unless every topic has 3+ days of reels.
- **Growth rules for every script:** see bank/INSIGHTS.md run 9. Painful-moment hook, 6 lines max, payoff by line 4-5.

## Monitor: volume safety
- **Watch reach and watch time:** after each ramp step, compare reach per reel and average watch time (`avg_watch_s` in /public/insights) with the previous 3 days.
- **When to lower the volume:** if reach per reel drops by more than 40%, or Instagram returns spam / action-blocked errors (subcode 2207042), set POST /ops/flag {"k":"reel_cap","v":"<previous level>"} and tell the owner.
- **Raising it again:** remove the cap (v null) once reach is back for 3 days.
- **At 100 followers:** set `low_reach_mode` = "0". That restores carousels and stories (2 carousels + 3 stories per topic, then the normal stages). Tell the owner.

## Confidentiality
Real client data from the CRM never goes into this repo. See bank/STORY_THEMES.md.

## Story sources and the theme tag (owner, 19 Nov)
- **Where scripts come from:** situations in bank/STORY_THEMES.md (anonymised CRM situations) and from its "Questions people ask online" section (F1-F22).
- **Tag every new script:** `theme="crm"` (built on a CRM situation), `theme="faq"` (built on an online question or mistake) or `theme="new"` (anything else). The tag is carried to posted entries and /public/insights, so performance can be compared per theme.
- **Before 14 days:** mix new batches roughly 40% crm, 40% faq, 20% new.
- **After 14 days, with 10+ judged reels per theme:** shift up to 60% toward the theme with the better reach, shares and keyword comments per 1,000 reach (same rules as audience-led optimisation). Never drop a theme completely.
- **More situations:** when a theme runs short, research more real questions online (forums, Quora, Reddit r/IndiaTax, r/StartUpIndia, government FAQ pages). Add them to STORY_THEMES.md as F-numbers, anonymised, with no copied text.
- **Company registration is getting repetitive (owner's feedback):** new co scripts must use the fresh F1-F6 angles or new situations. No more "buyer wants a company" set-ups unless the twist is new.

## Catching up after a pause (owner, 19 Nov)
If earlier runs were skipped (for example, Claude usage ran out), never assume the last run's state.
- Every run starts from live numbers: stock, runway, insights, the worker log and workflow runs.
- First do whatever fell behind: the most urgent topic's scripts first, then any failed workflows, then any missed checkpoint review (22 / 25 Nov). After that, the normal work.

## Follower shout-outs (owner, 19 Nov)
- **Who is named:** only people who tapped "Yes, tag me", by @username, with a plain thank-you. Never mention what they asked about.
- **When they are asked:** once, after their chat is complete, or when they comment or DM WELCOME. "remove me" / "no tag" switches it off.
- **Weekly welcome:** planned Sunday 09:41, starting at 30 followers (KV `shout_min`). One welcome per person, oldest first, only people still following. Batches of 20 (Instagram's tag limit), one post a day at 12:47.
- **Monthly top supporters:** planned on the first Sunday of the month. The 3-5 most engaged people (counted by days engaged), never the same person two months in a row.
- **Spam:** repeated comments count once a day.
- **How the pieces fit:** the factory renders the images from /public/shoutqueue (factory/shoutout.py); the worker posts them.
- **Monitor checks:** shout-out posts went out, and nobody is named who said no.

## Tips, news and corrections (owner, 19 Nov night)
- Daily total = normal reels (reel-max ramp, now capped at 80 from 22 Nov) + 1 tip reel per topic (14) + up to 4 news / opportunity / correction reels. 80 + 14 + 4 = 98, under Instagram's 100 posts per 24 h (the shout-out post takes the last one). Empty tip or news slots post nothing.
- Themes "tip", "news", "opportunity", "correction" are reserved: normal reel slots never use them, and the factory builds them before or alongside normal reels (news first, tips interleaved, 2 tips ready per topic).
- Tips: quick checks, calendar reminders, checklists, comparisons, "what if" answers. One per topic per day. Facts only from topics.py. Files bank/<topic>/batch_tipsNN.py, theme="tip". The refill writer keeps at least 10 unposted tip scripts per topic.
- News (watcher task, 4 runs a day): same-day posting only from Tier A official sources (government sites, plus ICAI / ICSI when they link the government circular). News reports alone wait; rumours never. Two official sources disagree: post nothing, tell the owner. Every news item carries source, as_of and expires; it is never posted after expires.
- Opportunity: a new government scheme / grant call / programme window: what it is, who is eligible, the official deadline. Never promise selection, funding or returns; never investment advice.
- Corrections: if a posted item was wrong or is overridden, post a correction reel (first in the news queue), add a correction comment on the wrong reel (/ops/correct), fix any unposted scripts repeating it, tell the owner. Never delete the wrong reel. Instagram's API cannot edit a published caption; the owner can edit it by hand.
- Topics never clash: a news item that changes a fact updates FACTS_ in topics.py in the same commit, so tips and normal reels written afterwards use the new fact.

## Comments, DMs and follow-ups (owner, 23 Nov)
- **One answer per keyword comment:** the worker claims each comment / DM id before answering (claimOnce), ignores Instagram's "already has a reply" duplicate, and posts only ONE public reply under a keyword comment (no 3 h public check-in any more).
- **Keyword typed again in DM** after the guide was sent from a comment: no second copy, a short "sent above 👆" with the next-step buttons.
- **Commenters who never open the DM:** the API can't message them again. They go to KV `fu_queue`; every 2 h (10:13-20:13 IST), 1 h after the comment, the owner gets a Discord list with a tap-to-open chat link and a ready message to send by hand. Ask the owner for the wording that worked for them and put it in FU_TEXT.
- **Keyword matching** ignores punctuation, spaced / dotted letters ("G.S.T", "s t a r t") and fancy fonts; a "?"-only comment gets a question reply, not "thank you".

## New reel type: toon (2D cartoon story series), A/B test from 23 Nov
- factory/toon.py; scripts with `toon(...)` in bank/<topic>/batch_toonNN.py (bank/batch_toonNN.py for co). Ids: prefix + "x" (gx, tmx, rcx, fsx, iex, ndx, cfx, fpx, qvx, yx, vx, ux, mx; co kx).
- Flow: hook + 2-3 person story (max 6 lines) -> breakdown card (max 4 rows + total) -> mentor's Rule #1-3 -> episode ribbon + keyword end card. One recurring hero per topic (series + ep + next), mentor usually അപ്പൂപ്പൻ / അമ്മൂമ്മ.
- The cast is NOT fixed: 23 people types (toon.TYPES: appooppan, ammachi, kasavu ammachi, uncle, auntie, young man/woman, students, NRI, Gulf returnee, shopkeeper, farmer, fisherman, auto driver, chef, doctors, IT pro, teacher, hijab-wearing woman, college girl...) with 10 skin tones, 18 shirt colours (some checked), 7 trouser, 11 saree colours, specs / shades / beard / pottu at random, matched to the names' gender. Series heroes keep one look (seeded by series + name). 19 backgrounds; a script's scene picks from its family (toon.SCENE_GROUPS).
- Build weight 0.4 (build.pick); the optimiser's `kind` weights compare toon vs duo3d/chat/list. Judge after 10+ posted toon reels per the usual reach / watch time / keyword-comment rules; write more episodes for the winning style.
- 3D duo reels also vary now: rooms.py CAST_LOOK 1-3 renders extra looks per location (assets/stills/looks/<scene>/<n>, same genders, new age / hair / specs / beard / clothes / skin); build.pick_look rotates them.

## FSSAI correction (24 Nov)
- A follower corrected us: since 1 Apr 2026 FSSAI registration covers turnover up to Rs 1.5 crore, state licence Rs 1.5-50 crore, central above Rs 50 crore (importers always central), and registrations / licences have perpetual validity. FACTS_FSSAI updated.
- 41 FSSAI scripts that quoted the old Rs 12 lakh / Rs 20 crore limits or 1-5 year renewal were removed from bank/fssai (their unposted reels are dropped by drop_orphans). The cartoon episodes were rewritten as fsy01-fsy04. Correction reel fsfix02 (cartoon, theme correction, corrects fsx04) thanks @rishad_pkr by name and is posted as a collab invite to him (collab=[...] -> Graph "collaborators"; refused invites post without it); it goes first in the news queue.
- Before writing any FSSAI script: never quote the old limits. Perpetual validity is certain only for licences issued on or after 1 Apr 2026; for older ones never say renewal can be skipped (check expiry on FoSCoS). The annual fee continues in all cases. When refilling, bring FSSAI back to 7+ days of stock first (it lost most of its bank).
- Already-posted wrong FSSAI reels: Instagram's API can't edit captions; add a correction comment by hand on the most-viewed ones.

## Direct DMs and topic switches (owner, 25 Nov)
- A DM is no longer assumed to be about company registration. The worker reads the topic from the words (TOPIC_WORDS, keywords, Malayalam / Manglish too), falls back to a small AI classifier for a first message of 3+ words, and a plain "hi" gets a menu (Company registration / GST / Trademark / FSSAI / Funding / Something else).
- If someone asks about another service mid-chat (a request, not an answer that merely mentions it), the chat switches to that topic's questions; earlier topics stay in meta.topics for the lead.
- Every bot prompt: answer their question first in 1-2 sentences, then one question; ask for the phone number by the 2nd-3rd question with a reason; offer WhatsApp if they hesitate; never re-ask. Check-ins (2 h / 9 h / 22 h) follow the current topic.

## Suggestions, corrections, complaints (owner, 26 Nov)
- DMs and comments that suggest something, correct us or complain (FEEDBACK_HINT words + an AI check) get a reply about exactly what they said (thanks + "noted / we'll check"), never sales questions or the keyword DM; the owner gets a Discord alert; DM check-ins stop for that message. A 1-3 word follow-up right after (typo fixes like "Voiceover**") gets no second reply.
- When the owner acts on a suggestion, make ONE thank-you reel per person covering everything they said (owner, 27 Nov; never 2-3 reels for one person): theme "thanks" (posted in the news slots right after corrections), collab=[their username], e.g. bank/batch_thanks01.py.
- 26 Nov: @dev_onthe.move asked for a faster voiceover -> atempo 1.24 (was 1.14), sentence pauses 0.26-0.34 s. Keep this pace.

## 26 Nov growth review (automatic changes)
- **Topic shares (rule 4):** inv 5%, fp 5%, val 8.6%, iec 8.6%, co 11%, others 6.8% (REEL_SHARE = topics.SHARE). Writers: inv and fp need fewer scripts now; val and iec more.
- **Tips:** one tip per topic every other day (TIP_EVERY = 2 in the worker, topics alternate, ~7 a day); the freed slots become story reels (87 a day). Writers keep 5+ unposted tips per topic (was 10). Tip reels in list format reached ~100 people each: new tips should be written as toon or duo3d scenes, not lists, when possible.
- **One keyword (rule 3):** captions and new end cards show only the topic keyword (e.g. "LIMIT") plus the concrete thing they get. Each post's unique keyword is still registered and still answered.
- **Format:** chat reels reached ~117 per reel (1 breakout in 52) vs ~340 for duo3d / toon. New normal scripts: at most 10% chat, at least 80% duo3d or toon.
- **100-follower switch held:** followers passed 100 (255 on 26 Nov) but `low_reach_mode` stays on. The normal stage plan would cut story reels from ~87 to ~30 a day, bring back 70 stories, and drop tips and news, while carousels still reach ~0. Keep reel-max mode until the owner decides or a new plan keeps 80+ reels a day; do not flip it automatically.
- 26 Nov night: same follower said the voice is hard to follow ("kelkkan oru problem") -> no echo on the voice, less boom (250 Hz -2 dB), more presence (3.2 kHz +4 dB), final mix normalised to -14 LUFS (was about -16). Keep these.
- Content requests ("X kurich oru content cheyumo?") are answered "we'll make a reel on it", sent to Discord, and stored in KV content_requests (read them at /public/content_requests). Script writers: check that list every run and write those topics first, with a thank-you reel (theme "thanks") when it's one person's idea.
- A DM with the same text from the same person is answered once per 10 min (dtx: claim), whatever route delivers it.

## Two new topics (owner, 27 Nov): pg = payment gateway, web = websites
- Why: followers ask about taking online payments right after registering (gateway KYC, documents, name mismatches), and the team now builds websites for startups payable in monthly parts. Both sit next to company registration in the founder journey: register -> bank account -> payment gateway -> website.
- Folders bank/pg (ids "pg...") and bank/web (ids "wb..."); keywords GATEWAY / PAYMENT and WEBSITE / WEBPLAN; share 5% each (others trimmed, total 1.0). Facts only from topics.FACTS_PG / FACTS_WEB; websites are OUR service: never a price, instalment amount or delivery date; never recommend or price a gateway.
- Seed: cartoon series ep 1-6 each (Fahad's online shop; Riya's boutique). Refill both to 7+ days like every topic; mix toon, duo3d and list reels, faq / crm / new themes as usual.
- DM bot: both topics in TOPIC_WORDS and the "Hi" menu; every prompt now starts with "understand first" (what they want, no assuming their business from a word, ask when unclear).

## Four more topics (owner, 27 Nov night): acc, kl, nri, pay
- acc = monthly compliance (GST returns, accounts, ITR/TDS). Ids "ac", keywords ITR / ACCOUNTS, bank/acc.
- kl = Kerala licences (local-body / K-SMART trade licence, Shops Act within 60 days even with no staff, professional tax). Ids "lc", keywords SHOPS / KSMART, bank/kl.
- nri = pravasi founder (NORKA NDPREM loans + subsidy, Mudra, PMEGP, FEMA FC-GPR/FC-TRS/FLA). Ids "pv", keywords PRAVASI / NORKA, bank/nri.
- pay = payroll & PF/ESI (Labour Codes from 21 Nov 2025, ESIC 10+, EPF 20+, EPF ceiling Rs 25,000 from 17 Sep 2026, PM-VBRY). Ids "py", keywords ESIC / PAYROLL, bank/pay.
- Facts ONLY from topics.FACTS_ACC / FACTS_KL / FACTS_NRI / FACTS_PAY. Never promise a loan, subsidy or incentive; never state a due date as fixed; never a penalty we haven't verified; never our fee.
- 4 seed toon episodes each (ep 1-4). Refill continues at ep 5+. Statutory amounts allowed by check_bank: 2,500 / 3,000 / 15,000 / 21,000 / 25,000.
- 20 topics now; REEL_SHARE (worker) and SHARE (topics.py) must stay identical and sum to 1.0.
- Read HANDOVER_2026-11-27.md if you are a session that did not make these changes.

## Accurate replies and real corrections (owner, 27 Nov)
- Comment replies must fit what the person said and the reel they commented on. Thanks / praise gets a warm reply with no keyword CTA; on a thank-you or correction reel, or one that names them, a personal thank-you. Never "comment START" under a non-company reel or under thanks (worker pickCommentReply / postKw).
- After a correction, only the corrected fact may appear anywhere: scripts, end cards, captions (captions.py TOPIC lines too) and DM texts. check_bank fails on the old FSSAI limits outside theme "correction".
- A correction reel is a real apology: say sorry plainly, say what was wrong (without repeating the wrong numbers on screen), give the correct fact with its official source and date. fsfix04 is the model.

## Language, voice messages, legal help (owner, 27 Nov)
- DMs: reply in the language the person writes in (Malayalam script -> Malayalam; Manglish -> Manglish; English -> English). Voice messages are transcribed and answered as text in their language; unclear ones go to Discord for the team to listen.
- Legal trouble (partner dispute, court / arbitration order, police, assets taken, lawyer not helping): empathy first, offer to connect them with our lawyers, ask the phone number with the reason; never sales intake questions, never legal advice or outcome promises. Alert: "[Legal help / partner dispute]".
- Content: partner-dispute reels (cfa, STORY_THEMES F23-F30) only with FACTS_CFA facts, invented people and mixed situations; never a real person's details.

## Lead follow-up (owner, 27 Nov) — live in the worker, don't remove
- Every Discord lead alert ends with a private update link (/lead/<id>?k=…, HMAC of ADMIN_KEY). The owner taps it after each call: Meeting set / No answer / Follow up later / Closed / Not interested / Talked. No Claude needed.
- No answer: Discord reminders on day 2, 4, 7, 12 and 42 (step 1 is shown on the page at once), each with a ready WhatsApp message (short /wa/ link -> wa.me, owner presses send) in the lead's call language. Inside Instagram's 24 h window the bot sends at most 3 nudges per window with buttons (when the owner taps No answer, or at 09:00 if tapped at night; 4 h+ later; a short last note at the last daytime chance), 09:00-21:30 IST only, and any reply stops them (owner approved). A reply on Instagram pauses the sequence and pings Discord.
- Meeting set: reminder at 09:00 that day and 30 min before (with a WhatsApp reminder ready), then "how did it go?" 2 h after.
- 10:07 daily: list of alerted leads with no update for 24 h. Board of open leads: /leads/board link in that message. ops/run {"what":"lead_links"} re-sends links for all open leads.
- The bot now asks the call language together with the best time to call and the country if abroad; alerts show 📍 location and 🕑 best time.
- /public/insights has outcomes_by_topic (new / meeting / noanswer / later / replied / closed / lost): use it in reviews (clients per topic is the goal metric).
- WhatsApp messages are never sent automatically (no WhatsApp API). Never message leads outside these rules.
- Replies (27 Nov): when a lead in the no-answer sequence writes back, the AI reads it (call time / WhatsApp / later / question / not interested), the bot answers once in their language (confirms the time, never resends the guide), and the owner gets the reply plus what it means in Discord. A named time becomes a call reminder automatically (the owner can change it on the update page). Their reply opens a new 24 h window: if they go quiet again for 3 h+, the bot may nudge again (at most 2 in that window, at most 3 windows per lead, daytime only); once Instagram can't be used, the WhatsApp reminders resume. General check-ins skip anyone in this sequence.
- Guides are never sent twice: a late or duplicate keyword comment doesn't re-queue a guide served in the last 7 days, check-ins only say "your guide is ready" when it truly wasn't sent, and "I've followed" after the guide gets a thank-you plus the next question (Rithik, 27 Nov).
- Guide already delivered (27 Nov): if someone asks for a guide they already got (keyword again, a duplicate comment, or "I've followed" after the guide), the bot says politely that it believes the guide was already delivered, asks them to scroll up, and offers a "Send it again" button that resends it once. Then it repeats the question they hadn't answered.
- Lead call reminders (27 Nov): when a call time is set (from their reply or the owner's "Meeting set") and Instagram's 24 h window is still open, the bot reminds the lead on Instagram the morning of the call (only if the call was set before that morning and is after 11:00) and about 30 min before ("India time" shown if they live abroad). Outside the window only the owner is reminded.

## 27 Nov weekly growth review (automatic changes)
- Shares (rule 4): gst 5.0%, tm 5.0% (from 5.3%), val 4.6%, cfa 4.6% (from 4.3%). REEL_SHARE = topics.SHARE, sum 1.0. Zero-lead topics were already under 5% after the 21-topic rescale, so they were not cut.
- Captions: "💬 Comment KEYWORD 👇" now sits on the line under the hook, and the Malayalam paragraph ends with a send-to-a-friend line (captions.EARLY / SEND_ML). Keep both until the 3 Dec funnel judgement.
- /public/insights: leads_by_topic and outcomes_by_topic count a lead under the topic of the reel it came from (direct DMs: chat topic).
- Owner (27 Nov): growth must come only from Instagram itself: no paid boosts, collabs, WhatsApp sharing, profile work or manual lead updates are coming. Never ask the owner for them. Writers: end every new script on a line people want to forward to a friend in that situation (sends are how reels pass the ~1,500-view cap). Rule-4 share floor is 3.5% (21 topics).

## Topic 21: investor data room (dr), and web widened to tech development (owner, 27 Nov night)
- dr (ids "dr", keywords DATAROOM / DILIGENCE, Malayalam ഡാറ്റ റൂം): we set up investor data rooms AND prepare what is missing for them (company registration, projections, valuation, agreements, pending GST / ROC filings). The DM questions bring out which pieces are missing, so the hidden services show up in the lead. Never promise funding, an investor, a valuation figure or a timeline; never a price. Content angles: what goes in a data room, due diligence red flags, data rooms for loans / sale / partners, unregistered founders, messy documents. A 2D toon series ("നിഖിലിന്റെ ആദ്യ ഫണ്ടിംഗ്", eps 1-4) plus 3D reels and tips are seeded.
- web is now TECH / WEBSITE: websites, mobile apps, software for teams, MVPs and automations. Angle: we understand the business, not just the code, so we build what moves it; for clients able to pay for a proper build, in monthly parts. Never a price, instalment amount, timeline, delivery date or promised result. New keyword APP (exact match only). New segments: app_idea, mvp_founder, ops_software.
- Shares: everyone scaled by 0.96 to make room for dr (dr 0.041); SHARE = REEL_SHARE, sum 1.0. The weekly review may rebalance by results.
- Topic detection: a short answer to the bot's own question never switches topic (fixed 27 Nov: "pvt ltd, 2 years" turned a Udyam lead into company registration).
- Daily volume (27 Nov night): normal reels are capped so reels + tips + 4 news slots + the shout-out post + 1 spare stay under Instagram's 100 posts / 24 h (21 topics pushed the plan to 105 and a reel was skipped). With 21 topics that is about 84 reels a day.

## 28 Nov monitor: Instagram cut the API posting limit to 50 / 24 h
- 05:30 IST 28 Nov: `content_publishing_limit` returned quota_total **50** (was 100 on 14 Nov), quota_usage 97. The worker skips any post when fewer than 2 are left, so today's frozen 84-reel plan will post only as yesterday's posts age out (~50 today, mostly afternoon/evening).
- Monitor set KV `reel_cap` = 21 so plans from 29 Nov are ~31 reels + ~11 tips + 4 news + shout-out = ~47 posts. Raise it again only if quota_total goes back to 100 (check with ops/graph `me/content_publishing_limit`). With fewer reels a day, each topic's runway is ~2.7x longer; writers favour quality over volume.
- Cloudflare KV free plan (1,000 puts/day) ran out just before 00:00 UTC on 28 Nov (ops/flag put returned 1101). The 5-min "inbox poll sees" line is now logged only when it changes (commit 0821fc8). If KV puts fail again earlier in the day, the owner needs the Workers Paid plan.

## Topic 22: idea validation (28 Nov)
- Keywords VALIDATE / IDEA. For people with a business idea who have not yet tested demand.
- Content comes from the essence of a real client call, anonymised (STORY_THEMES C29). Never use real names, places, products or figures from calls.
- Points: test demand before building an app, start with one niche, track the cost to win a customer, earnings per order and repeat buyers, start as a proprietorship with free Udyam and move to a private limited company when investors come in, and the CA vs registered valuer route for valuation (reports need refreshing after a few months).
- Never promise demand, sales, funding or results. No prices.

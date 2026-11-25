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

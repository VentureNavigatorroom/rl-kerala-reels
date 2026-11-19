# Growth plan and checkpoints (owner's instruction, 19 Nov 2026)

GOAL (owner): 10 clients a month PER TOPIC (about 100 enquiries a month each), same as company registration, for all 14 topics:
co, gst, inv, sui, sk, ud, tm, roc, fssai, iec, nda, cfa, fp, val. The 20-25 Nov projection below was made for 6 topics;
with 13 the same total volume is spread thinner, so per-topic numbers are lower and the topic comparison (rule 4) matters more.

These rules run whether the owner is present or not. The monitor (every 3 h) and the script writer (every 4 h) read this file on every run. Two review tasks run on 22 Nov and 25 Nov.

## Projection updated 19 Nov 19:20 for 14 topics (replaces the 6-topic table below for judging results)

Total volume stays the same: up to 90 reels a day, about 350-400 reels from 20 to 25 Nov. The original 6 topics post from 20 Nov. The 8 newest (tm, roc, fssai, iec, nda, cfa, fp, val) post from about 21 Nov, once their reels are built, about 6 a day each.

### Whole account, 20-25 Nov
| | Low | Middle (best guess) | High (with owner's push) |
|---|---|---|---|
| Views | 30k | 45k | 70k+ |
| Breakout reels (1,000+ views) | 2-3 | 5-8 | 10+ |
| New followers | 15-30 | 40-80 | 150-300 |
| Keyword comments / DMs | 5-10 | 15-30 | 40-80 |
| Real leads | 2-5 | 6-12 | 15-30 |
| Clients | 0-1 | 1-3 | 3-6 |

### Per topic, 20-25 Nov (middle case)
- **Each topic:** 25-45 reels, 2-4k views, 0-2 leads. Most topics will have 0-1 leads by 25 Nov. That is expected, not failure.
- **Likely to lead:** inv, fp, val, sui, sk and cfa. Founder and funding situations dominate the CRM, so these match the real audience.
- **Likely steady:** co, gst, ud and fssai (large, everyday audiences).
- **Likely slower:** iec, nda, tm and roc (narrower, or "I'll do it later" needs). These convert well once people do engage.

### Goal path, per topic: 10 clients a month (about 100 enquiries a month)
- **By 25 Nov:** learn which topics, story sources (crm/faq/new) and hooks work.
- **26 Nov-9 Dec:** shift volume toward the best 4-6 topics (rule 4). Target 1-3 leads per topic per week, and 15-25 a week in total.
- **10 Dec-31 Dec:** with followers growing and the best formats scaled, target 5-10 leads per topic per week for the strongest topics. The first topics reach about 10 clients a month in late December or January. Weaker topics stay at 5% until they improve.
- **Faster than this** needs paid boosts, collabs or a breakout trend.

## Optimisation plan, in order (applied automatically)
1. **Every 3 h (monitor):** posting health, stock per topic, reach and watch-time safety (reel_cap), and 100 followers switches carousels and stories back on.
2. **Every 4 h (writer):** scripts for the shortest runway first, mixing 40% crm, 40% faq and 20% new; the d904 pattern; max 6 lines.
3. **22 Nov checkpoint:** watch time, reach, funnel and other causes (rules 1, 2, 3 and 5).
4. **25 Nov review:** topic shares (rule 4, reduce but never below 5%), the theme mix, and new 2-week targets per topic.
5. **Weekly after that:** the same review, at most 2 share changes a week, and the owner is told every time.

## Original projection (19 Nov afternoon, 6 topics), for reference

| | Low | Middle (best guess) | High |
|---|---|---|---|
| Views | 30k | 45k | 70k+ |
| Breakout reels (1,000+ views) | 2-3 | 5-8 | 10+ |
| New followers | 15-30 | 40-80 | 150-300 |
| Keyword comments / DMs | 5-10 | 15-30 | 40-80 |
| Real leads | 2-5 | 6-12 | 15-30 |
| Clients | 0-1 | 1-3 | 3-6 |

Early signals to watch:
- Average watch time above 6 s (it was 4.2 s).
- Two or more reels a day above 500 reach.
- Keyword comments from strangers.
- Follows coming through the DM follow step.

## Decision rules

### 1. Low watch time (still ~4 s at the 22 Nov check, or any later 3-day window)
- **Script length:** cap scripts at 5 lines, about 12-15 s.
- **First frame:** the on-screen hook must state the conflict.
- **Pattern:** about 60% of new scripts use the d904 pattern (a myth people believe, a vivid local job, a quotable last line).
- **Story sources:** cut the worst-performing story source (crm / faq / new) to 10%.

### 2. Reach per reel falls more than 40% after a volume step, or spam / action-blocked errors appear
- Set `reel_cap` back one level and hold it until reach has been back for 3 days. More reels only helps if each keeps its reach.

### 3. Reach grows but keyword comments and DMs stay near zero (the funnel is the problem, not the reels)
- **Keywords:** one keyword per topic in captions and on-screen CTAs.
- **Reason to comment:** say the concrete thing they get ("comment UDYAM and get the 45-day rule checklist").
- **DM questions:** test asking for the phone number earlier, after 3 questions, for one week, then compare completion rates.

### 4. Topic performance (from 25 Nov, with at least 5 days per topic)
- **Measure:** rank topics by leads, then keyword comments, per 1,000 reach.
- **Reduce, never drop:** cut a weak topic's share to no less than 5%, so it keeps learning and can recover. Give the freed share to the best topics.
- **Changes allowed:** no more than 2 share changes a week, each no more than 10 points.
- **Shares live in two places:** REEL_SHARE in worker/src/index.js and SHARE in factory/topics.py. Keep them identical.
- **Owner approval:** the owner has approved this; tell the owner what changed and why.

### 5. Keep researching other causes when a target is missed
Check Instagram's current guidance and creator reports for reasons that could be holding reach down, for example:
- AI-generated or "unoriginal" content labelling or demotion
- too many similar reels or near-duplicates
- no trending or licensed audio
- captions or hashtags that hurt distribution
- posting time
- account trust signals (profile completeness, link in bio)

If evidence shows one applies, make the fix that is in our control (code, scripts, captions, schedule). Record it in bank/INSIGHTS.md. Things only the owner can do go in the owner's summary as clear asks:
- paid boost
- collab posts (needs a username)
- profile bio and highlights
- sharing on WhatsApp

### 6. Backups
Every topic, including gst, inv, sui, sk and ud, always keeps 2-3 days of built reels and a script bank ahead of its share. The refill task writes for the shortest runway first, and the monitor checks runway per topic. A topic that runs dry hands its slots to the others automatically.

## The owner is told
- When a rule above fires.
- At the 22 Nov and 25 Nov reviews.
- Otherwise, only if something breaks.

# Standing rules for the scheduled tasks (read first; overrides older task text)

## Reel-max mode (owner, 19 Nov 2026)
While the account has fewer than 100 followers and KV `low_reach_mode` is not "0":
- **What posts:** from 20 Nov every slot is a reel. No carousels, stories or posters; they reach about 0 people without followers.
- **How many:** the total ramps to 40 (20 Nov), 60 (21 Nov), 80 (22 Nov), then 90 a day (REEL_RAMP in worker/src/index.js).
- **Topic split:** co 40%, gst/inv/sui/sk 15% each (REEL_SHARE), limited by each topic's built stock. Leftovers go to topics with stock.
- **When the plan is set:** it is frozen once a day in KV `plan:<day>`, at the first cron tick after midnight.

## Refill priority
Reel scripts are the bottleneck.
- **New topics first:** give gst, inv, sui and sk most of each run until each has 40+ unbuilt or unposted reel scripts. After that, keep every topic at 3+ days of its live share. 90/day x share = about 36 reels a day for co and about 14 for each new topic.
- **Skip carousels and stories** while reel-max mode is on, unless every topic has 3+ days of reels.
- **Growth rules for every script:** see bank/INSIGHTS.md run 9. Painful-moment hook, 6 lines max, payoff by line 4-5.

## Monitor: volume safety
- **Watch reach and watch time:** after each ramp step, compare reach per reel and average watch time (`avg_watch_s` in /public/insights) with the previous 3 days.
- **When to lower the volume:** if reach per reel drops by more than 40%, or Instagram returns spam / action-blocked errors (subcode 2207042), set POST /ops/flag {"k":"reel_cap","v":"<previous level>"} and tell the owner.
- **Raising it again:** remove the cap (v null) once reach is back for 3 days.
- **At 100 followers:** set `low_reach_mode` = "0". That restores carousels and stories (2 carousels + 3 stories per topic, then the normal stages). Tell the owner.

## Confidentiality
Real client data from the CRM never goes into this repo. See bank/STORY_THEMES.md.

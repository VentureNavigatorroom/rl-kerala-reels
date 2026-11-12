# rl-kerala-reels

Automated Malayalam reel system for @rejectionlist.kerala. Runs without anyone watching.

- `bank/` – unique reel scripts (no prices, ever). Add new `batchNN.py` files to extend.
- `factory/` – turns scripts into reels (3D tea-shop dialogue, chat story, checklist), covers and Story cards.
- `.github/workflows/factory.yml` – nightly build (01:00 IST) keeps ~8 days of reels in stock on the `library` branch, served by GitHub Pages.
- `worker/` – Cloudflare autopilot: posts 5 reels + 5 Stories a day, trial reels when available, weekly optimiser, DM bot and lead alerts.

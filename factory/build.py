"""Build reels from the script bank into library/ until the unposted stock reaches the target.
Runs unattended (GitHub Actions nightly). Picks scripts so content types and ICP segments rotate,
weighted by library/weights.json (written by the optimiser from real Instagram numbers)."""
import os, sys, json, glob, importlib.util, time, random
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import ROOT
import cover

LIB = f"{ROOT}/library"; os.makedirs(f"{LIB}/media", exist_ok=True)
MAN = f"{LIB}/manifest.json"
VERSION = 2   # bump when voices/look change: unposted reels from older versions get rebuilt

def load_bank():
    S = []
    for f in sorted(glob.glob(f"{ROOT}/bank/batch*.py")):
        spec = importlib.util.spec_from_file_location(os.path.basename(f)[:-3], f); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
        S += m.S
    ids = [s["id"] for s in S]; assert len(ids) == len(set(ids)), "duplicate script ids"
    return S

def load_carousels():
    C = []
    for f in sorted(glob.glob(f"{ROOT}/bank/carousels*.py")):
        spec = importlib.util.spec_from_file_location(os.path.basename(f)[:-3], f); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
        C += m.C
    ids = [c["id"] for c in C]; assert len(ids) == len(set(ids)), "duplicate carousel ids"
    return C

def build_carousels(man, target):
    import carousel
    made = {c["id"] for c in man.setdefault("carousels", [])}
    stock = sum(1 for c in man["carousels"] if not c.get("posted"))
    for c in [c for c in load_carousels() if c["id"] not in made][:max(0, target - stock)]:
        files = carousel.make(c, f"{LIB}/media", seed=abs(hash(c["id"])) % 3)
        cap = c["hook"].replace("\n", " ") + "\n\n" + c["cta"][0] + " 👇\n\n#companyregistration #kerala #startupkerala #malayali #keralabusiness #entrepreneur"
        man["carousels"].append(dict(id=c["id"], segment=c["segment"], images=[f"media/{os.path.basename(p)}" for p in files], caption=cap, posted=None))
        print("carousel", c["id"], len(files), flush=True)
    json.dump(man, open(MAN, "w"), ensure_ascii=False, indent=1)

def load_stories():
    T = []
    for f in sorted(glob.glob(f"{ROOT}/bank/stories*.py")):
        spec = importlib.util.spec_from_file_location(os.path.basename(f)[:-3], f); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
        T += m.T
    ids = [t["id"] for t in T]; assert len(ids) == len(set(ids)), "duplicate story ids"
    return T

def build_stories(man, target):
    """Standalone stories. A quiz becomes two queued stories (question, then answer)."""
    made = {x.get("src") for x in man.setdefault("stories", []) if x.get("src")}
    stock = sum(1 for x in man["stories"] if not x.get("posted") and x.get("src"))
    for t in [t for t in load_stories() if t["id"] not in made]:
        if stock >= target: break
        parts = ["q", "answer"] if t["kind"] == "quiz" else [None]
        for p in parts:
            sid = f"s_{t['id']}" + ("_a" if p == "answer" else "")
            cover.story_card(t, f"{LIB}/media/{sid}.jpg", part=p)
            man["stories"].append(dict(id=sid, image=f"media/{sid}.jpg", src=t["id"], segment=t.get("segment"), kind=t["kind"] if p != "answer" else "answer", after=f"s_{t['id']}" if p == "answer" else None))
            stock += 1
    json.dump(man, open(MAN, "w"), ensure_ascii=False, indent=1)

def manifest():
    return json.load(open(MAN)) if os.path.exists(MAN) else {"items": []}

def pick(bank, man, n):
    built = {i["id"] for i in man["items"]}
    todo = [s for s in bank if s["id"] not in built]
    w = json.load(open(f"{LIB}/weights.json")) if os.path.exists(f"{LIB}/weights.json") else {}
    kw = w.get("kind", {"duo3d": 0.45, "chat": 0.35, "list": 0.2}); sw = w.get("segment", {})
    out, last_kind, last_seg = [], None, None
    for _ in range(n):
        cand = [s for s in todo if s not in out]
        if not cand: break
        def score(s):
            sc = kw.get(s["kind"], 0.2) * sw.get(s["segment"], 1.0) * random.uniform(0.7, 1.3)
            if s["kind"] == last_kind: sc *= 0.4                  # rotate formats
            if s["segment"] == last_seg: sc *= 0.6                 # rotate audiences
            return sc
        s = max(cand, key=score); out.append(s); last_kind, last_seg = s["kind"], s["segment"]
    return out

def sync_posted(man):
    """Mark items the Cloudflare poster already published; delete their media after 3 days to keep the repo small."""
    url = os.environ.get("POSTED_URL")
    if not url: return
    import urllib.request
    try: posted = set(json.load(urllib.request.urlopen(url, timeout=30)))
    except Exception as e: print("could not read posted list:", e); return
    now = int(time.time())
    for i in man["items"]:
        if i["id"] in posted and not i.get("posted"): i["posted"] = now
        if i.get("posted") and now - i["posted"] > 3 * 86400:
            for f in (i["video"], i["cover"], f"media/{i['id']}_story.jpg"):
                p = f"{LIB}/{f}"
                if os.path.exists(p): os.remove(p)
    man["stories"] = [x for x in man.get("stories", []) if os.path.exists(f"{LIB}/{x['image']}")]
    for c in man.get("carousels", []):
        if c["id"] in posted and not c.get("posted"): c["posted"] = now
        if c.get("posted") and now - c["posted"] > 3 * 86400:
            for f in c["images"]:
                if os.path.exists(f"{LIB}/{f}"): os.remove(f"{LIB}/{f}")
    man["carousels"] = [c for c in man.get("carousels", []) if not (c.get("posted") and not os.path.exists(f"{LIB}/{c['images'][0]}"))]

def main():
    target = int(os.environ.get("STOCK_TARGET", "40")); budget = float(os.environ.get("TIME_BUDGET_MIN", "300")) * 60
    only = [a for a in sys.argv[1:] if not a.startswith("-")]
    bank, man = load_bank(), manifest()
    sync_posted(man)
    old = {i["id"] for i in man["items"] if not i.get("posted") and i.get("v", 1) < VERSION}
    if old:
        print("rebuilding older-version reels:", len(old))
        man["items"] = [i for i in man["items"] if i["id"] not in old]
        man["stories"] = [x for x in man.get("stories", []) if x.get("reel") not in old]
    json.dump(man, open(MAN, "w"), ensure_ascii=False, indent=1)
    stock = sum(1 for i in man["items"] if not i.get("posted"))
    if only: todo = [s for s in bank if s["id"] in only]
    else: todo = pick(bank, man, max(0, target - stock))
    print(f"stock {stock}, building {len(todo)}", flush=True)
    t0 = time.time()
    for s in todo:
        if time.time() - t0 > budget: print("time budget reached"); break
        mod = {"duo3d": "duo3d", "chat": "chat", "list": "listreel"}[s["kind"]]
        build = importlib.import_module(mod).build
        out = f"{LIB}/media/{s['id']}.mp4"
        info = build(s, out, seed=abs(hash(s["id"])) % 10000)
        cover.make(s, info["cover_frame"], f"{LIB}/media/{s['id']}.jpg")
        cover.story(s, info["cover_frame"], f"{LIB}/media/{s['id']}_story.jpg")
        man.setdefault("stories", [])
        man["stories"] = [x for x in man["stories"] if x["id"] != "s_" + s["id"]] + [dict(id="s_" + s["id"], image=f"media/{s['id']}_story.jpg", reel=s["id"])]
        cap = s["hook"].replace("\n", " ") + "\n\n" + s["cta"][0] + " 👇\n\n#companyregistration #kerala #startupkerala #malayali #business #entrepreneur #pvtltd #keralabusiness"
        man["items"] = [i for i in man["items"] if i["id"] != s["id"]] + [dict(id=s["id"], kind=s["kind"], segment=s["segment"], bucket=s["bucket"], scene=s.get("scene"),
            video=f"media/{s['id']}.mp4", cover=f"media/{s['id']}.jpg", caption=cap, duration=info["duration"], built=int(time.time()), posted=None, v=VERSION)]
        json.dump(man, open(MAN, "w"), ensure_ascii=False, indent=1)
        print("built", s["id"], info["duration"], flush=True)
    left = len([s for s in bank if s["id"] not in {i["id"] for i in man["items"]}])
    cl = len([c for c in load_carousels() if c["id"] not in {c["id"] for c in man.get("carousels", [])}])
    man["bank_left"] = dict(reel_scripts=left, carousels=cl); json.dump(man, open(MAN, "w"), ensure_ascii=False, indent=1)
    print(f"unbuilt scripts left in bank: {left}, carousels left: {cl}")

if __name__ == "__main__":
    main()

"""Build reels from the script bank into library/ until the unposted stock reaches the target.
Runs unattended (GitHub Actions nightly). Picks scripts so content types and ICP segments rotate,
weighted by library/weights.json (written by the optimiser from real Instagram numbers)."""
import os, sys, json, re, glob, importlib.util, time, random
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import ROOT
import cover
import speak_ml
import captions
import topics

LIB = f"{ROOT}/library"; os.makedirs(f"{LIB}/media", exist_ok=True)
MAN = f"{LIB}/manifest.json"
POSTER_V = 2   # bump when the poster look changes: unposted posters get re-rendered
VERSION = 8   # bump when voices/look change: unposted reels from older versions get rebuilt

def _load(prefix, attr):
    """Every topic's bank files (bank/<prefix>*.py, bank/gst/<prefix>*.py, bank/inv/<prefix>*.py); each entry is tagged with its topic."""
    out = []
    for t, d in topics.DIRS.items():
        for f in sorted(glob.glob(f"{ROOT}/{d}/{prefix}*.py")):
            spec = importlib.util.spec_from_file_location(f"{t}_{os.path.basename(f)[:-3]}", f); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
            out += [dict(x, topic=x.get("topic", t)) for x in getattr(m, attr)]
    return out
def topic_of(x): return x.get("topic") or "co"
def per_topic(target): return {t: int(round(target * sh)) for t, sh in topics.SHARE.items()}

def load_bank():
    S = _load("batch", "S")
    ids = [s["id"] for s in S]; assert len(ids) == len(set(ids)), "duplicate script ids"
    return S

def load_carousels():
    C = _load("carousels", "C")
    ids = [c["id"] for c in C]; assert len(ids) == len(set(ids)), "duplicate carousel ids"
    return C

# Every post also gets its own keyword (never reused), shown next to the general one: "START / LAUNCH".
KW_POOL = """LAUNCH FOUNDER BRAND GROW DREAM OWNER TEAM OFFICE CLIENT INVOICE PROFIT BUDGET TRUST LEGAL SHARE BOARD DIRECTOR PARTNER SOLO FREELANCE STUDIO AGENCY CAFE BAKERY FARM SPICE EXPORT IMPORT GULF DUBAI QATAR KOCHI KERALA MALABAR MUNNAR BEACH FERRY METRO SHOP STORE MARKET TAILOR SALON GARAGE CLINIC TRAVEL TOUR HOTEL RESORT HOMESTAY CATERING WEDDING DESIGN CODE APP WEBSITE DIGITAL ONLINE SELLER TRADER BUILDER MAKER CRAFT HANDLOOM COIR RUBBER COCONUT PEPPER CARDAMOM COFFEE CHAI SNACK KITCHEN FOOD JUICE FRESH ORGANIC GREEN SOLAR POWER TECH ROBOT DRONE DATA CLOUD PIXEL VIDEO PHOTO MUSIC DANCE ARTIST WRITER TUTOR COACH TRAINER FITNESS YOGA HEALTH PHARMA DOCTOR NURSE LAB SCHOOL COLLEGE CAMPUS STUDENT INTERN FRESHER SALARY BONUS SAVING INVEST FUNDING INVESTOR ANGEL PITCH DECK VALUE EQUITY ASSET CAPITAL BANK LOAN TENDER CONTRACT ORDER BILL RECEIPT STAMP SEAL CERTIFICATE LICENCE PERMIT COMPLIANCE AUDIT FILING RETURN DEADLINE PENALTY NOTICE SAFE SECURE PROTECT SHIELD LIMIT LIABILITY PRIVATE PUBLIC FAMILY BROTHER SISTER FRIEND COUPLE NEIGHBOUR VILLAGE TOWN CITY STREET JUNCTION BRIDGE HARBOUR PORT CARGO COURIER PARCEL DELIVERY FLEET TAXI AUTO BIKE TRUCK BOAT CRUISE FISH PRAWN DAIRY MILK HONEY RICE PADDY MANGO BANANA JACKFRUIT CASHEW TEA GARDEN NURSERY FLOWER PRINT PRESS MEDIA NEWS RADIO PODCAST CHANNEL CREATOR INFLUENCER REEL STORY VIRAL TREND FUTURE VISION MISSION GOAL TARGET WIN RISE BOOST SCALE EXPAND GLOBAL LOCAL NATIVE ROOTS ORIGIN PIONEER LEADER CAPTAIN CHIEF BOSS""".split()
def with_kw(s, man):
    s = dict(s); reg = man.setdefault("kwmap", {}); base = s["cta"][0].split()[0]
    kw = next((k for k, v in reg.items() if v["item"] == s["id"]), None)
    if not kw:
        want = (s.get("kw") or "").upper()
        cands = ([want] if want.isalpha() and len(want) >= 4 else []) + KW_POOL + [f"{w}{n}" for n in range(2, 50) for w in KW_POOL]
        kw = next(k for k in cands if k not in reg and k not in topics.ALL_BASES)
        reg[kw] = dict(item=s["id"], base=base)
    s["cta_caption"] = f"{base} അല്ലെങ്കിൽ {kw} എന്ന് കമന്റ് ചെയ്യൂ"
    s["cta"] = (f"{base} / {kw}", "എന്ന് കമന്റ് ചെയ്യൂ\n" + s["cta"][1]); s["kw"] = kw; s["base"] = base
    return s

def build_carousels(man, target):
    import carousel
    made = {c["id"] for c in man.setdefault("carousels", [])}
    todo = []
    for t, tt in per_topic(target).items():
        stock = sum(1 for c in man["carousels"] if not c.get("posted") and topic_of(c) == t)
        todo += [c for c in load_carousels() if c["id"] not in made and topic_of(c) == t][:max(0, tt - stock)]
    for c in todo:
        c = with_kw(c, man)
        files = carousel.make(c, f"{LIB}/media", seed=abs(hash(c["id"])) % 3)
        cap = captions.caption(c, c["hook"].replace("\n", " "))
        man["carousels"].append(dict(id=c["id"], topic=topic_of(c), segment=c["segment"], images=[f"media/{os.path.basename(p)}" for p in files], caption=cap, kw=c["kw"], base=c["base"], point=c["end"].replace("\n", " "), posted=None))
        print("carousel", c["id"], len(files), flush=True)
    json.dump(man, open(MAN, "w"), ensure_ascii=False, indent=1)

def load_posters():
    P = _load("posters", "P")
    ids = [p["id"] for p in P]; assert len(ids) == len(set(ids)), "duplicate poster ids"
    for p in P: assert p["layout"] in ("fact", "myth", "deadline", "check"), p["id"]
    return P

def build_posters(man, target):
    import poster
    made = {p["id"] for p in man.setdefault("posters", [])}
    bank = {p["id"]: p for p in load_posters()}
    for q in man["posters"]:   # look v2: the CTA line under the keyword pill shows the whole promise (v1 cut it in half)
        if not q.get("posted") and q.get("pv", 1) < POSTER_V and q["id"] in bank:
            poster.make(bank[q["id"]], f"{LIB}/media/{q['id']}.jpg"); q["pv"] = POSTER_V; print("poster rebuilt", q["id"], flush=True)
    todo = []
    for t, tt in per_topic(target).items():
        stock = sum(1 for p in man["posters"] if not p.get("posted") and topic_of(p) == t)
        todo += [p for p in load_posters() if p["id"] not in made and topic_of(p) == t][:max(0, tt - stock)]
    for p in todo:
        p = with_kw(p, man)
        poster.make(p, f"{LIB}/media/{p['id']}.jpg")
        cap = captions.caption(p, p["caption"].split("\n")[0])
        man["posters"].append(dict(id=p["id"], topic=topic_of(p), segment=p["segment"], layout=p["layout"], image=f"media/{p['id']}.jpg", caption=cap, kw=p["kw"], base=p["base"], point=p["caption"].split("\n")[0], posted=None, pv=POSTER_V))
        print("poster", p["id"], flush=True)
    json.dump(man, open(MAN, "w"), ensure_ascii=False, indent=1)

def load_stories():
    T = _load("stories", "T")
    ids = [t["id"] for t in T]; assert len(ids) == len(set(ids)), "duplicate story ids"
    return T

def build_stories(man, target):
    """Standalone stories. A quiz becomes two queued stories (question, then answer)."""
    made = {x.get("src") for x in man.setdefault("stories", []) if x.get("src")}
    tgt = per_topic(target)
    stock = {tp: sum(1 for x in man["stories"] if not x.get("posted") and x.get("src") and topic_of(x) == tp) for tp in tgt}
    for t in [t for t in load_stories() if t["id"] not in made]:
        if stock[topic_of(t)] >= tgt[topic_of(t)]: continue
        parts = ["q", "answer"] if t["kind"] == "quiz" else [None]
        for p in parts:
            sid = f"s_{t['id']}" + ("_a" if p == "answer" else "")
            cover.story_card(t, f"{LIB}/media/{sid}.jpg", part=p)
            man["stories"].append(dict(id=sid, image=f"media/{sid}.jpg", src=t["id"], topic=topic_of(t), segment=t.get("segment"), kind=t["kind"] if p != "answer" else "answer", after=f"s_{t['id']}" if p == "answer" else None))
            stock[topic_of(t)] += 1
    json.dump(man, open(MAN, "w"), ensure_ascii=False, indent=1)

def manifest():
    return json.load(open(MAN)) if os.path.exists(MAN) else {"items": []}

def pick(bank, man, n):
    built = {i["id"] for i in man["items"]}
    fails = man.get("failed", {})
    todo = [s for s in bank if s["id"] not in built and fails.get(s["id"], 0) < 2]   # skip scripts that failed twice
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
    """Mark items the Cloudflare poster already published; delete their media after 1 day (Instagram copies it at publish; keeps the Pages site under 1 GB at 35 reels a day) to keep the repo small."""
    url = os.environ.get("POSTED_URL")
    if not url: return
    import urllib.request
    # Cloudflare refuses Python's default user agent from GitHub runners (HTTP 403), so send a normal one
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (rl-kerala-reel-factory)", "Accept": "application/json"})
    try: posted = set(json.load(urllib.request.urlopen(req, timeout=30)))
    except Exception as e: print(f"::error::could not read posted list: {e}"); return
    now = int(time.time())
    for i in man["items"]:
        if i["id"] in posted and not i.get("posted"): i["posted"] = now
        if i.get("posted") and now - i["posted"] > 86400:
            for f in (i["video"], i["cover"], f"media/{i['id']}_story.jpg"):
                p = f"{LIB}/{f}"
                if os.path.exists(p): os.remove(p)
    for x in man.get("stories", []):
        if not x.get("src"): continue                     # reel teasers go with their reel
        if x["id"] in posted and not x.get("posted"): x["posted"] = now
        if x.get("posted") and now - x["posted"] > 86400 and os.path.exists(f"{LIB}/{x['image']}"): os.remove(f"{LIB}/{x['image']}")
    # standalone stories stay listed after posting so the builder never makes them again; teasers leave with their media
    man["stories"] = [x for x in man.get("stories", []) if x.get("src") or os.path.exists(f"{LIB}/{x['image']}")]
    for c in man.get("carousels", []):
        if c["id"] in posted and not c.get("posted"): c["posted"] = now
        if c.get("posted") and now - c["posted"] > 86400:
            for f in c["images"]:
                if os.path.exists(f"{LIB}/{f}"): os.remove(f"{LIB}/{f}")
    for p in man.get("posters", []):
        if p["id"] in posted and not p.get("posted"): p["posted"] = now
        if p.get("posted") and now - p["posted"] > 86400 and os.path.exists(f"{LIB}/{p['image']}"): os.remove(f"{LIB}/{p['image']}")
    # posted carousels stay listed (without media) so the builder never makes them again

def spoken_texts(sc):
    """The strings the voice actually reads in a script (dialogue lines, list items, end line)."""
    out = []
    for l in sc.get("lines") or []: out.append(l[-1] if isinstance(l, (list, tuple)) else str(l))
    for it in sc.get("items") or []: out.extend(x for x in (it if isinstance(it, (list, tuple)) else [it]) if isinstance(x, str))
    if sc.get("end"): out.append(str(sc["end"]))
    return out

def recaption(man):
    """Give every unposted reel, carousel and poster the current three-language caption (cheap: no re-render)."""
    banks = {"items": {x["id"]: x for x in load_bank()}, "carousels": {x["id"]: x for x in load_carousels()}, "posters": {x["id"]: x for x in load_posters()}}
    n = 0
    for key, bank in banks.items():
        for it in man.get(key, []):
            sc = bank.get(it["id"])
            if it.get("posted") or not sc or not it.get("kw"): continue
            sc = dict(sc, kw=it["kw"], base=it.get("base") or sc["cta"][0].split()[0])
            head = sc["caption"].split("\n")[0] if key == "posters" else sc["hook"].replace("\n", " ")
            cap = captions.caption(sc, head)
            if it.get("caption") != cap: it["caption"] = cap; n += 1
    print("captions refreshed:", n, flush=True)

def place(s, man):
    """Pick the location: scripts tied to one of the 4 original settings rotate through every compatible place,
    preferring places used least recently, so consecutive reels never look the same."""
    import duo3d
    s = dict(s); home = s.get("scene") or "teashop"
    if s.get("scene_lock") or home not in duo3d.GROUPS:
        return s
    if not s.get("names"): s["names"] = duo3d.SCENES[home]["names"]       # dialogue mentions these names
    # only places whose drawn people match the script's names (a woman's name never lands on a man with a moustache)
    opts = [x for x in duo3d.GROUPS[home] if x in duo3d.SCENES and duo3d.available(x) and duo3d.fits(x, s["names"])] or [home]
    hist = [i.get("scene") for i in sorted(man["items"], key=lambda i: i.get("built", 0))]
    def last(x): return max([k for k, v in enumerate(hist) if v == x], default=-1)
    opts.sort(key=lambda x: (last(x), abs(hash(s["id"] + x)) % 97))
    s["scene"] = opts[0]; return s

def main():
    run_fail = []
    target = int(os.environ.get("STOCK_TARGET", "40")); budget = float(os.environ.get("TIME_BUDGET_MIN", "300")) * 60
    only = [a for a in sys.argv[1:] if not a.startswith("-")]
    bank, man = load_bank(), manifest()
    sync_posted(man)
    try: recaption(man)
    except Exception as e: print("recaption failed:", repr(e), flush=True)
    # v4 changed only how acronyms are spoken: rebuild just the unposted reels whose lines contain one, re-tag the rest
    # v6 says numbers as Malayalam words and English words in Malayalam spelling: rebuild unposted reels that have either
    # v5 fixed voice gender (many women's names were voiced male): rebuild just the unposted reels whose voices change
    from voice import HAS_ACR, FEMALE_V4, voice_for
    import duo3d
    byid = {s["id"]: s for s in bank}
    def voice_changed(i, sc):
        if sc.get("kind") == "chat": nm = sc.get("names") or ()
        elif sc.get("kind") == "duo3d": nm = sc.get("names") or duo3d.SCENES.get(i.get("scene") or "", {}).get("names") or ()
        else: return False
        return any(voice_for(n, k) != ("F" if n in FEMALE_V4 else "M") + str(1 + k % 2) for k, n in enumerate(nm))
    def needs(i):
        if i.get("v", 1) < 3: return True
        sc = byid.get(i["id"])
        if not sc: return False
        if i.get("v", 1) < 4 and HAS_ACR(json.dumps([sc.get("lines"), sc.get("items"), sc.get("end")], ensure_ascii=False)): return True
        if i.get("v", 1) < 6 and any(re.search(r"\d|[A-Za-z]*[a-z][A-Za-z]*|\b3D\b", t) for t in spoken_texts(sc)): return True   # v6: numbers and English words spoken properly
        if i.get("v", 1) < 7 and any(re.search(r"(?<![\u0d00-\u0d7f])ഒ(?![\u0d00-\u0d7f\u200c\u200d])", speak_ml.before_respell(t)) for t in spoken_texts(sc)): return True   # v7: letter O said as ഓ (OPC, NOC, ROC)
        if i.get("v", 1) < 8 and any(re.search(r"[A-Z]{2,5}-\d|ഇൻവോയ്സ്|സ്റ്റോൾ", t) for t in spoken_texts(sc)): return True   # v8: form codes in English numbers (INC-20A), invoice, stall
        return voice_changed(i, sc)
    old = set()
    for i in man["items"]:   # any unposted reel whose names do not match the people drawn in its location
        sc = byid.get(i["id"])
        if sc and sc.get("kind") == "duo3d" and not i.get("posted") and i.get("scene") in duo3d.SCENES:
            home = sc.get("scene") or "teashop"
            nm = sc.get("names") or duo3d.SCENES[home if home in duo3d.GROUPS else i["scene"]]["names"]
            if not duo3d.fits(i["scene"], nm): old.add(i["id"])
    for i in man["items"]:
        if not i.get("posted") and i.get("v", 1) < VERSION:
            if needs(i): old.add(i["id"])
            else: i["v"] = VERSION
    if old:
        print("rebuilding older-version reels:", len(old))
        man["items"] = [i for i in man["items"] if i["id"] not in old]
        man["stories"] = [x for x in man.get("stories", []) if x.get("reel") not in old]
    json.dump(man, open(MAN, "w"), ensure_ascii=False, indent=1)
    # carousels and standalone stories are quick still images: top them up before the slow reel renders
    for name, fn, env, dflt in (("carousels", build_carousels, "CAROUSEL_TARGET", "70"), ("stories", build_stories, "STORY_TARGET", "70"), ("posters", build_posters, "POSTER_TARGET", "70")):
        try: fn(man, int(os.environ.get(env, dflt)))
        except Exception as e: print(f"{name} build failed:", repr(e), flush=True); run_fail.append(f"{name}: {e!r}")
    stock = {t: sum(1 for i in man["items"] if not i.get("posted") and topic_of(i) == t) for t in topics.DIRS}
    if only: todo = [s for s in bank if s["id"] in only]
    else:   # each topic tops up its own stock; the lists are interleaved so the time budget is shared fairly
        lists = [pick([s for s in bank if topic_of(s) == t], man, max(0, n - stock[t])) for t, n in per_topic(target).items()]
        todo = [x for row in __import__("itertools").zip_longest(*lists) for x in row if x]
    print(f"stock {stock}, building {len(todo)}", flush=True)
    t0 = time.time()
    for s in todo:
        if time.time() - t0 > budget: print("time budget reached"); break
        mod = {"duo3d": "duo3d", "chat": "chat", "list": "listreel"}[s["kind"]]
        build = importlib.import_module(mod).build
        if s["kind"] == "duo3d": s = place(s, man)
        s = with_kw(s, man)
        out = f"{LIB}/media/{s['id']}.mp4"
        try: info = build(s, out, seed=abs(hash(s["id"])) % 10000)
        except Exception as e:   # one bad script must not lose the whole night's work
            fails = man.setdefault("failed", {}); fails[s["id"]] = fails.get(s["id"], 0) + 1
            print("FAILED", s["id"], repr(e), flush=True); run_fail.append(f"{s['id']}: {e!r}"); json.dump(man, open(MAN, "w"), ensure_ascii=False, indent=1); continue
        cover.make(s, info["cover_frame"], f"{LIB}/media/{s['id']}.jpg")
        cover.story(s, info["cover_frame"], f"{LIB}/media/{s['id']}_story.jpg")
        man.setdefault("stories", [])
        man["stories"] = [x for x in man["stories"] if x["id"] != "s_" + s["id"]] + [dict(id="s_" + s["id"], image=f"media/{s['id']}_story.jpg", reel=s["id"], topic=topic_of(s))]
        cap = captions.caption(s, s["hook"].replace("\n", " "))
        man["items"] = [i for i in man["items"] if i["id"] != s["id"]] + [dict(id=s["id"], topic=topic_of(s), kind=s["kind"], segment=s["segment"], bucket=s["bucket"], scene=s.get("scene"), sound=None, kw=s["kw"], base=s["base"], point=s["end"].replace("\n", " "),
            video=f"media/{s['id']}.mp4", cover=f"media/{s['id']}.jpg", caption=cap, duration=info["duration"], built=int(time.time()), posted=None, v=VERSION)]
        json.dump(man, open(MAN, "w"), ensure_ascii=False, indent=1)
        print("built", s["id"], info["duration"], flush=True)
    left = len([s for s in bank if s["id"] not in {i["id"] for i in man["items"]}])
    cl = len([c for c in load_carousels() if c["id"] not in {c["id"] for c in man.get("carousels", [])}])
    tl = len([t for t in load_stories() if t["id"] not in {x.get("src") for x in man.get("stories", [])}])
    pl = len([p for p in load_posters() if p["id"] not in {x["id"] for x in man.get("posters", [])}])
    man["bank_left"] = dict(reel_scripts=left, carousels=cl, stories=tl, posters=pl)
    built_ids = {x["id"] for k in ("items", "carousels", "posters") for x in man.get(k, [])} | {x.get("src") for x in man.get("stories", [])}
    man["bank_left_by_topic"] = {t: {name: len([x for x in fn() if topic_of(x) == t and x["id"] not in built_ids]) for name, fn in (("reel_scripts", load_bank), ("carousels", load_carousels), ("stories", load_stories), ("posters", load_posters))} for t in topics.DIRS}
    man["stock_by_topic"] = {t: {k: sum(1 for x in man.get(k, []) if not x.get("posted") and topic_of(x) == t) for k in ("items", "carousels", "posters", "stories")} for t in topics.DIRS}; json.dump(man, open(MAN, "w"), ensure_ascii=False, indent=1)
    # delete media no longer referenced by the manifest (old-version reels, pruned posts)
    keep = set()
    def walk(o):
        if isinstance(o, dict): [walk(v) for v in o.values()]
        elif isinstance(o, list): [walk(v) for v in o]
        elif isinstance(o, str) and o.startswith("media/"): keep.add(o.split("/")[-1])
    walk(man)
    for f in os.listdir(f"{LIB}/media"):
        if f not in keep and not f.startswith("."): os.remove(f"{LIB}/media/{f}")
    print(f"unbuilt scripts left in bank: {left}, carousels left: {cl}")
    # anything that failed is saved and published as usual, but the run ends red so the monitor reads this log and fixes it
    man["last_failures"] = run_fail; json.dump(man, open(MAN, "w"), ensure_ascii=False, indent=1)
    if run_fail:
        for f in run_fail: print(f"::error::{f}")
        sys.exit(1)

if __name__ == "__main__":
    main()

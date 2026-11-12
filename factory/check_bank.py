"""Checks every bank file before it reaches the factory. Exit code 1 lists every problem found.
Run: python3 factory/check_bank.py   (also runs in GitHub on every push that touches bank/ or factory/)"""
import os, re, sys, glob
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import build, duo3d, voice

ROOT = build.ROOT
errs = []
def err(m): errs.append(m)

# 1. loaders run and ids are unique across each bank
banks = {}
for name, fn in (("reels", build.load_bank), ("carousels", build.load_carousels), ("posters", build.load_posters), ("stories", build.load_stories)):
    try: banks[name] = fn()
    except Exception as e: err(f"{name}: loader failed: {e!r}"); banks[name] = []
    seen = {}
    for x in banks[name]:
        if x["id"] in seen: err(f"{name}: duplicate id {x['id']}")
        seen[x["id"]] = 1

# 2. locations exist, have stills, and their drawn people match the names
def stills(scene):
    d = f"{ROOT}/assets/stills" + ("/" + duo3d.SCENES[scene]["dir"] if duo3d.SCENES[scene]["dir"] else "")
    return os.path.isdir(d) and any(f.endswith((".png", ".jpg")) for f in os.listdir(d))
for k, v in duo3d.SCENES.items():
    for n in v["names"]:
        if not voice.gender_known(n): err(f"location {k}: name {n} is in neither FEMALE nor MALE in voice.py")
    if not stills(k): err(f"location {k}: no stills in assets/stills")
for s in banks["reels"]:
    sid = s["id"]
    if s["kind"] == "duo3d":
        sc = s.get("scene") or "teashop"
        if sc not in duo3d.SCENES: err(f"{sid}: scene '{sc}' is not a key of duo3d.SCENES"); continue
        nm = s.get("names") or duo3d.SCENES[sc]["names"]
        for n in nm:
            if not voice.gender_known(n): err(f"{sid}: name {n} is in neither FEMALE nor MALE in voice.py (its voice would be guessed)")
        if sc in duo3d.GROUPS:   # will be moved: at least one place must fit
            if not [x for x in duo3d.GROUPS[sc] if stills(x) and duo3d.fits(x, nm)]: err(f"{sid}: no {sc}-group location fits names {nm}")
        elif not duo3d.fits(sc, nm): err(f"{sid}: names {nm} do not match the people drawn in {sc} {duo3d.SCENES[sc]['names']}")
        for who, cam, txt in s["lines"]:
            if who not in ("A", "V") or cam not in ("A", "V", "wide"): err(f"{sid}: bad speaker/camera {who}/{cam}")
    elif s["kind"] == "chat":
        for n in s["names"]:
            if not voice.gender_known(n): err(f"{sid}: chat name {n} is in neither FEMALE nor MALE in voice.py")
        for who, txt in s["lines"]:
            if who not in (0, 1): err(f"{sid}: bad chat speaker {who}")
    if s["hook"].count("\n") > 2: err(f"{sid}: hook has more than 3 lines")

# 3. every reel, carousel and poster ends with one of the keyword CTAs
import importlib.util
_b1 = importlib.util.spec_from_file_location("b1", f"{ROOT}/bank/batch01.py"); _m = importlib.util.module_from_spec(_b1); _b1.loader.exec_module(_m)
ctas = {_m.CTA_START, _m.CTA_NAME, _m.CTA_AFTER, _m.CTA_DOCS}
for name in ("reels", "carousels", "posters"):
    for x in banks[name]:
        if tuple(x.get("cta") or ()) not in ctas: err(f"{x['id']}: cta is not one of CTA_START / CTA_NAME / CTA_AFTER / CTA_DOCS")
for t in banks["stories"]:
    if t["kind"] == "contact" and t["kw"] not in ("START", "NAME", "AFTER", "CHECKLIST"): err(f"{t['id']}: unknown keyword {t['kw']}")
for p in banks["posters"]:
    if p["layout"] not in ("fact", "myth", "deadline", "check"): err(f"{p['id']}: unknown layout {p['layout']}")

# 4. no rupee sign and no service-price words in any bank text (statutory late fee "ലേറ്റ് ഫീ" is allowed)
PRICE = re.compile(r"(^|[\s\"'(.,!?])(വില|വിലയ്ക്ക്|ഫീസ്|ചാർജ്|ചാർജ്ജ്|ഡിസ്കൗണ്ട്|ഓഫർ\s*വില|price|fee|fees|discount|cheap|affordable)($|[\s\"'),.!?])", re.I)
for f in sorted(glob.glob(f"{ROOT}/bank/*.py")):
    for k, line in enumerate(open(f, encoding="utf-8"), 1):
        if line.lstrip().startswith("#"): continue
        if "₹" in line: err(f"{os.path.basename(f)}:{k}: ₹ symbol")
        m = PRICE.search(line)
        if m: err(f"{os.path.basename(f)}:{k}: price word '{m.group(2)}' (only statutory penalties may appear)")

# 5. near-duplicate hooks across reels / carousels
def norm(t): return re.sub(r"[\s\"'.,!?:]+", "", t)
for name in ("reels", "carousels"):
    seen = {}
    for x in banks[name]:
        h = norm(x["hook"])
        if h in seen: err(f"{x['id']}: same hook as {seen[h]}")
        seen[h] = x["id"]

print(f"reels {len(banks['reels'])}, carousels {len(banks['carousels'])}, posters {len(banks['posters'])}, stories {len(banks['stories'])}")
if errs:
    print(f"{len(errs)} problem(s):"); [print(" -", e) for e in errs]; sys.exit(1)
print("bank OK")

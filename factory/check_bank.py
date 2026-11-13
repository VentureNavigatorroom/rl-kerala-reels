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

# 3c. every English word the voice reads must have a Malayalam spelling in factory/speak_ml.py SAY (acronyms are spelled out)
import speak_ml
for x in banks["reels"]:
    for t in build.spoken_texts(x):
        for w in speak_ml.unknown_latin(t): err(f"{x['id']}: the voice cannot say '{w}': add it to SAY in factory/speak_ml.py (Malayalam spelling) or write it in Malayalam")

# 4. no rupee sign and no service-price words in any bank text (statutory late fee "ലേറ്റ് ഫീ" is allowed)
PRICE = re.compile(r"(^|[\s\"'(.,!?])(വില|വിലയ്ക്ക്|ഫീസ്|ചാർജ്|ചാർജ്ജ്|ഡിസ്കൗണ്ട്|ഓഫർ\s*വില|price|fee|fees|discount|cheap|affordable)($|[\s\"'),.!?])", re.I)
for f in sorted(glob.glob(f"{ROOT}/bank/*.py")):
    for k, line in enumerate(open(f, encoding="utf-8"), 1):
        if line.lstrip().startswith("#"): continue
        if "₹" in line: err(f"{os.path.basename(f)}:{k}: ₹ symbol")
        m = PRICE.search(line)
        if m: err(f"{os.path.basename(f)}:{k}: price word '{m.group(2)}' (only statutory penalties may appear)")

# 4b. every rupee amount must be a statutory penalty (or penalty arithmetic / a quiz's wrong option already reviewed).
#     A new amount fails here: if it really is penalty maths from the checked facts, add it to RUPEE_OK.
RUPEE_OK = {"0", "100", "1,000", "6,000", "30,000", "50,000", "2,50,000", "1 ലക്ഷം", "10 ലക്ഷം", "ഒരു", "നൂറ്", "ആയിരം", "അമ്പതിനായിരം", "ഒരു ലക്ഷം", "ഇരുപതിനായിരം"}
RUPEE = re.compile(r"(\S+(?: ലക്ഷം)?) രൂപ")
def texts(x):   # every string inside an item
    if isinstance(x, str): yield x
    elif isinstance(x, (list, tuple)):
        for y in x: yield from texts(y)
    elif isinstance(x, dict):
        for k, y in x.items():
            if k != "cta": yield from texts(y)
for name, xs in banks.items():
    for x in xs:
        for t in texts(x):
            for m in RUPEE.finditer(t.replace("\n", " ")):
                amt = m.group(1).strip("\"'(:")
                if amt not in RUPEE_OK: err(f"{x['id']}: amount '{amt} രൂപ' is not a known statutory penalty (no service prices)")

# 4c. no emoji in on-screen text (chat bubbles are exempt: the chat renderer drops emoji)
EMOJI = re.compile("[\U0001F300-\U0001FAFF☀-➿⭐✅]")
for name, xs in banks.items():
    for x in xs:
        for k, v in x.items():
            if name == "reels" and x["kind"] == "chat" and k == "lines": continue
            if k == "cta": continue
            for t in texts(v):
                if EMOJI.search(t): err(f"{x['id']}: emoji in on-screen text ({k})")

# 4d. dialogue fits the people: address words match the listener's gender; nobody calls themselves by name
FEM_ADDR = ("ചേച്ചി", "ചേച്ചീ", "മോളേ", "ഇത്താ", "ടീച്ചറേ", "സിസ്റ്റർ", "മാഡം")
MAL_ADDR = ("ചേട്ടാ", "ഏട്ടാ", "ഇക്കാ", "മോനേ", "അളിയാ", "സാറേ", "ചേട്ടായി", "മച്ചാനേ", "അണ്ണാ", "ഡാ")
def has_word(t, w): return re.search(r"(^|[\s\"'(,!?.]|[ഀ-ൿ])" + re.escape(w) + r"($|[\s\"'),!?.])", t) is not None
for s in banks["reels"]:
    if s["kind"] != "duo3d": continue
    sc = s.get("scene") or "teashop"
    if sc not in duo3d.SCENES: continue
    nm = s.get("names") or duo3d.SCENES[sc]["names"]; N = {"A": nm[0], "V": nm[1]}
    for who, cam, txt in s["lines"]:
        if who not in N: continue
        lis = N["V" if who == "A" else "A"]; lf = voice.is_female(lis)
        for w in (MAL_ADDR if lf else FEM_ADDR):
            if has_word(txt, w): err(f"{s['id']}: {N[who]} calls {lis} '{w}' (wrong gender for the listener)")
        own = N[who]; first = re.split(r"[\s,!?.]", txt.strip(), maxsplit=1)[0]
        if len(own) > 2 and first != own and first.startswith(own[:-1]) and len(first) <= len(own) + 4:
            err(f"{s['id']}: {own} seems to address themselves ('{first}')")
        if txt.strip().startswith(own + ","): err(f"{s['id']}: {own} addresses themselves by name")

# 4e. length limits: the longest texts that are known to render without overflow (raise only after a test render)
LIMITS = dict(hook_line=38, end_line=32, duo_line=130, chat_line=122, lines=11, list_title=54, list_text=94, list_items=3,
              slide_title=42, slide_text=103, slides=5, car_hook_lines=4, p_tag=28, p_big=17, p_text=112, p_myth=67, p_truth=94,
              p_title=35, p_item=52, p_items=5, s_title=41, s_body=125, s_q=124, s_a=29, s_why=91, s_line=63)
def over(i, key, n):
    if n > LIMITS[key]: err(f"{i}: {key} is {n} characters/items (limit {LIMITS[key]}); shorten it so it fits on screen")
for s in banks["reels"]:
    for l in s["hook"].split("\n"): over(s["id"], "hook_line", len(l))
    for l in s["end"].split("\n"): over(s["id"], "end_line", len(l))
    if s["kind"] == "duo3d": [over(s["id"], "duo_line", len(l[2])) for l in s["lines"]]; over(s["id"], "lines", len(s["lines"]))
    if s["kind"] == "chat": [over(s["id"], "chat_line", len(l[1])) for l in s["lines"]]; over(s["id"], "lines", len(s["lines"]))
    if s["kind"] == "list":
        over(s["id"], "list_items", len(s["items"]))
        for a, b in s["items"]: over(s["id"], "list_title", len(a)); over(s["id"], "list_text", len(b))
for c in banks["carousels"]:
    for l in c["hook"].split("\n"): over(c["id"], "hook_line", len(l))
    for l in c["end"].split("\n"): over(c["id"], "end_line", len(l))
    over(c["id"], "car_hook_lines", c["hook"].count("\n") + 1); over(c["id"], "slides", len(c["slides"]))
    for a, b in c["slides"]: over(c["id"], "slide_title", len(a)); over(c["id"], "slide_text", len(b))
for p in banks["posters"]:
    for k in ("tag", "big", "text", "myth", "truth", "title"):
        if k in p: over(p["id"], "p_" + k, len(p[k]))
    if "items" in p: over(p["id"], "p_items", len(p["items"])); [over(p["id"], "p_item", len(i)) for i in p["items"]]
for t in banks["stories"]:
    for k in ("title", "body", "q", "a", "why", "line"):
        if k in t: over(t["id"], "s_" + k, len(t[k]))

# 5. repeated or near-duplicate hooks (reels and carousels) and poster angles
import difflib
def norm(t): return re.sub(r"[\s\"'.,!?:…]+", "", t)
for name in ("reels", "carousels"):
    hs = [(x["id"], norm(x["hook"])) for x in banks[name]]
    for a in range(len(hs)):
        for b in range(a + 1, len(hs)):
            if hs[a][1] == hs[b][1] or difflib.SequenceMatcher(None, hs[a][1], hs[b][1]).ratio() > 0.85:
                err(f"{hs[b][0]}: hook repeats / nearly repeats {hs[a][0]}")
pa = [(p["id"], norm(p.get("big", "") + p.get("text", "") + p.get("myth", "") + p.get("title", "") + "".join(p.get("items", [])))) for p in banks["posters"]]
for a in range(len(pa)):
    for b in range(a + 1, len(pa)):
        if difflib.SequenceMatcher(None, pa[a][1], pa[b][1]).ratio() > 0.8: err(f"{pa[b][0]}: poster nearly repeats {pa[a][0]}")

print(f"reels {len(banks['reels'])}, carousels {len(banks['carousels'])}, posters {len(banks['posters'])}, stories {len(banks['stories'])}")
if errs:
    print(f"{len(errs)} problem(s):"); [print(" -", e) for e in errs]; sys.exit(1)
print("bank OK")

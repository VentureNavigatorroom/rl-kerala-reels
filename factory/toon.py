"""2D cartoon 'story series' reel (owner, 23 Nov; inspired by the flat-cartoon money reels that do well in Kerala).
Flow: hook + short story between 2-3 characters -> breakdown card (where it went wrong, row by row)
-> the mentor's rules (Rule #1, #2...) -> episode ribbon + the usual keyword end card.
The cast is never fixed: each reel draws its people from a pool of types (appooppan, auntie, young man / woman,
uncle, student, NRI, shop owner) with random skin, clothes, hair and specs, matched to the script's names by gender."""
import math, os, random
import numpy as np
from PIL import Image, ImageDraw
from common import *
from voice import say, voice_for, is_female

SS = 2   # draw at 2x, shrink for smooth edges
SKINS = [(236, 188, 150), (214, 160, 120), (190, 135, 95), (160, 108, 72), (132, 86, 58)]
SHIRTS = [(242, 242, 238), (56, 118, 204), (214, 64, 72), (246, 190, 52), (70, 160, 110), (136, 90, 168), (232, 130, 80), (40, 44, 56), (120, 196, 230), (250, 160, 180)]
PANTS = [(46, 52, 70), (60, 80, 130), (92, 70, 52), (70, 72, 78)]
SAREES = [(214, 64, 72), (40, 140, 120), (246, 190, 52), (136, 90, 168), (232, 120, 150), (60, 110, 200)]
HAIR, GREY = (28, 24, 24), (196, 196, 192)

# person types; "f" = female. Mentors are usually the elders.
TYPES = {
    "elder":      dict(f=False, hair="bald", grey=True, must=True, specs=0.6, wear="mundu", shirt="white", h=1.0),
    "uncle":      dict(f=False, hair="short", grey=False, must=True, specs=0.3, wear="mundu", belly=True, h=0.98),
    "young_man":  dict(f=False, hair="puff", must=False, beard=0.35, wear="pants", h=1.0),
    "student_m":  dict(f=False, hair="puff", must=False, wear="pants", bag=True, h=0.94),
    "nri":        dict(f=False, hair="short", must=True, specs=0.5, wear="pants", tuck=True, h=1.0),
    "shopkeeper": dict(f=False, hair="short", must=True, wear="mundu", towel=True, belly=True, h=0.98),
    "ammachi":    dict(f=True, hair="bun", grey=True, specs=0.7, wear="saree", h=0.95),
    "auntie":     dict(f=True, hair="bun", wear="saree", h=0.97),
    "young_woman":dict(f=True, hair="long", wear="churidar", h=0.97),
    "student_f":  dict(f=True, hair="braid", wear="churidar", bag=True, h=0.93),
    "pro_woman":  dict(f=True, hair="bob", specs=0.4, wear="pants", h=0.98),
}
MALE_T = ["young_man", "uncle", "student_m", "nri", "shopkeeper", "elder"]
FEMALE_T = ["young_woman", "auntie", "student_f", "pro_woman", "ammachi"]

def make_look(kind, rng):
    t = dict(TYPES[kind]); t["kind"] = kind
    t["skin"] = SKINS[rng.integers(len(SKINS))]
    t["shirt_c"] = (242, 242, 238) if t.get("shirt") == "white" else SHIRTS[rng.integers(len(SHIRTS))]
    t["pant_c"] = PANTS[rng.integers(len(PANTS))]
    t["saree_c"] = SAREES[rng.integers(len(SAREES))]
    t["specs"] = rng.random() < t.get("specs", 0.0)
    t["beard"] = rng.random() < t.get("beard", 0.0)
    t["hair_c"] = GREY if t.get("grey") else HAIR
    return t

# ---------------- person drawing (2x canvas, 460 x 980 at 1x) ----------------
PW, PH = 460, 980
def person(L, mouth=0.0, blink=False):
    s = SS; im = Image.new("RGBA", (PW * s, PH * s), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    S = lambda *v: [int(x * s) for x in v]
    sk, sh, hc = L["skin"], L["shirt_c"], L["hair_c"]; dk = tuple(int(c * 0.78) for c in sk)
    cx = PW // 2; top = int(PH * (1 - L["h"]))           # shorter people start lower
    hy = top + 150                                       # head centre
    # legs / lower garment
    if L["wear"] == "mundu":
        d.polygon(S(cx - 95, 560, cx + 95, 560, cx + 110, 930, cx - 110, 930), fill=(248, 246, 236))
        d.rectangle(S(cx - 112, 905, cx + 112, 930), fill=(214, 170, 60))
        d.line(S(cx + 10, 570, cx + 30, 905), fill=(222, 220, 210), width=4 * s)
        for x in (-50, 50): d.rounded_rectangle(S(cx + x - 30, 925, cx + x + 34, 958), 12 * s, fill=(90, 60, 40))
    elif L["wear"] in ("saree", "churidar"):
        c = L["saree_c"]; cc = tuple(min(255, int(v * 1.15)) for v in c)
        d.polygon(S(cx - 100, 540, cx + 100, 540, cx + 125, 935, cx - 125, 935), fill=c if L["wear"] == "saree" else cc)
        if L["wear"] == "saree": d.rectangle(S(cx - 126, 905, cx + 126, 935), fill=(230, 180, 60)); d.polygon(S(cx - 100, 300, cx - 40, 300, cx + 100, 600, cx + 60, 640), fill=c)
        else:
            for x in (-45, 45): d.rectangle(S(cx + x - 26, 880, cx + x + 26, 945), fill=(245, 240, 230))
        for x in (-45, 45): d.rounded_rectangle(S(cx + x - 28, 935, cx + x + 32, 962), 12 * s, fill=(110, 60, 50))
    else:   # pants
        pc = L["pant_c"]
        for x in (-48, 48): d.rounded_rectangle(S(cx + x - 44, 540, cx + x + 44, 935), 20 * s, fill=pc)
        for x in (-48, 48): d.rounded_rectangle(S(cx + x - 46, 925, cx + x + 52, 960), 14 * s, fill=(50, 40, 36))
    # torso
    bw = 128 if L.get("belly") else 112
    d.rounded_rectangle(S(cx - bw, 280, cx + bw, 580), 60 * s, fill=sh if L["wear"] != "saree" else L["saree_c"])
    if L.get("belly"): d.ellipse(S(cx - bw + 6, 380, cx + bw - 6, 600), fill=sh)
    if L["wear"] == "pants" and not L["f"]:
        d.rectangle(S(cx - bw + 10, 540, cx + bw - 10, 560), fill=(40, 36, 34))
        for y in (340, 400, 460): d.ellipse(S(cx - 5, y, cx + 5, y + 10), fill=tuple(int(c * 0.7) for c in sh))
        d.polygon(S(cx - 40, 282, cx, 330, cx + 40, 282), fill=tuple(min(255, int(c * 1.1) + 20) for c in sh))
    if L["wear"] == "churidar": d.polygon(S(cx - 120, 300, cx - 60, 290, cx + 110, 520, cx + 70, 540), fill=(250, 236, 200))   # dupatta
    if L.get("towel"): d.polygon(S(cx - 115, 290, cx - 60, 285, cx - 20, 560, cx - 70, 560), fill=(250, 250, 245)); d.line(S(cx - 112, 300, cx - 66, 560), fill=(200, 60, 60), width=5 * s)
    if L.get("bag"): d.rounded_rectangle(S(cx + bw - 20, 300, cx + bw + 40, 500), 18 * s, fill=(60, 90, 160))
    # arms
    for side in (-1, 1):
        x0 = cx + side * (bw - 14)
        d.rounded_rectangle(S(min(x0, x0 + side * 52), 300, max(x0, x0 + side * 52), 470), 26 * s, fill=sh if L["wear"] != "saree" else sk)
        d.rounded_rectangle(S(min(x0, x0 + side * 48) + 2, 450, max(x0, x0 + side * 48) - 2, 560), 22 * s, fill=sk)
        d.ellipse(S(x0 + side * 24 - 30, 540, x0 + side * 24 + 30, 600), fill=sk)
    # neck + head
    d.rectangle(S(cx - 30, 230, cx + 30, 300), fill=dk)
    if L["hair"] == "long" or L["hair"] == "braid": d.rounded_rectangle(S(cx - 112, hy - 70, cx + 112, hy + (230 if L["hair"] == "long" else 120)), 60 * s, fill=hc)
    if L["hair"] == "braid": d.rounded_rectangle(S(cx + 70, hy + 60, cx + 110, hy + 330), 18 * s, fill=hc)
    for side in (-1, 1): d.ellipse(S(cx + side * 102 - 18, hy - 10, cx + side * 102 + 18, hy + 40), fill=sk)   # ears
    d.ellipse(S(cx - 100, hy - 120, cx + 100, hy + 110), fill=sk)
    if L["hair"] == "bald":
        for side in (-1, 1): d.chord(S(cx + side * 60 - 50, hy - 70, cx + side * 60 + 50, hy + 20), 90 if side > 0 else 270, 270 if side > 0 else 90, fill=hc)
        d.pieslice(S(cx - 100, hy - 120, cx + 100, hy + 80), 200, 340, fill=sk)
    elif L["hair"] == "puff":
        d.ellipse(S(cx - 108, hy - 150, cx + 108, hy - 10), fill=hc); d.ellipse(S(cx - 60, hy - 175, cx + 70, hy - 80), fill=hc)
        d.rectangle(S(cx - 104, hy - 60, cx - 84, hy + 10), fill=hc); d.rectangle(S(cx + 84, hy - 60, cx + 104, hy + 10), fill=hc)
    elif L["hair"] == "short":
        d.chord(S(cx - 106, hy - 135, cx + 106, hy + 30), 180, 360, fill=hc)
        d.rectangle(S(cx - 104, hy - 45, cx - 84, hy + 10), fill=hc); d.rectangle(S(cx + 84, hy - 45, cx + 104, hy + 10), fill=hc)
    elif L["hair"] == "bun":
        d.chord(S(cx - 106, hy - 128, cx + 106, hy + 40), 180, 360, fill=hc); d.ellipse(S(cx - 50, hy - 190, cx + 50, hy - 100), fill=hc)
        d.line(S(cx, hy - 122, cx, hy - 60), fill=tuple(min(255, c + 30) for c in hc), width=4 * s)
    elif L["hair"] == "bob":
        d.chord(S(cx - 114, hy - 130, cx + 114, hy + 120), 180, 360, fill=hc); d.rectangle(S(cx - 114, hy - 10, cx - 80, hy + 70), fill=hc); d.rectangle(S(cx + 80, hy - 10, cx + 114, hy + 70), fill=hc)
    else:   # long / braid: fringe on top
        d.chord(S(cx - 106, hy - 128, cx + 106, hy + 30), 180, 360, fill=hc)
    # face
    ey = hy + 5
    for side in (-1, 1):
        ex = cx + side * 38
        if blink: d.line(S(ex - 16, ey, ex + 16, ey), fill=(30, 26, 26), width=5 * s)
        else: d.ellipse(S(ex - 18, ey - 20, ex + 18, ey + 20), fill=(255, 255, 255)); d.ellipse(S(ex - 9, ey - 8, ex + 9, ey + 12), fill=(30, 26, 26))
        d.line(S(ex - 20, ey - 36, ex + 18, ey - 40 + side * 2), fill=tuple(int(c * 0.9) for c in hc) if L["hair"] != "bald" else (90, 90, 90), width=7 * s)
    if L["f"]: d.ellipse(S(cx - 7, ey - 62, cx + 7, ey - 48), fill=(200, 40, 50))     # bindi / pottu
    d.polygon(S(cx, ey + 6, cx - 12, ey + 42, cx + 10, ey + 44), fill=dk)              # nose
    my = ey + 68
    if L.get("beard"): d.chord(S(cx - 92, hy - 10, cx + 92, hy + 128), 0, 180, fill=hc)
    if L.get("must"): d.chord(S(cx - 44, my - 26, cx + 44, my + 6), 180, 360, fill=hc)
    if mouth > 0.15:
        o = int(10 + 22 * mouth); d.ellipse(S(cx - 24, my - 4, cx + 24, my + o), fill=(110, 30, 40)); d.ellipse(S(cx - 12, my + o - 12, cx + 12, my + o), fill=(220, 100, 110))
    else: d.arc(S(cx - 26, my - 18, cx + 26, my + 10), 20, 160, fill=(110, 40, 40), width=5 * s)
    if L.get("specs"):
        for side in (-1, 1): d.rounded_rectangle(S(cx + side * 38 - 30, ey - 26, cx + side * 38 + 30, ey + 24), 12 * s, outline=(30, 30, 34), width=5 * s)
        d.line(S(cx - 8, ey - 4, cx + 8, ey - 4), fill=(30, 30, 34), width=5 * s)
    return im.resize((PW, PH), Image.LANCZOS)

# ---------------- backgrounds ----------------
def palm(d, x, y, h, rng):
    for k in range(24): d.ellipse([x + math.sin(k / 6) * 14 - 13, y - k * h / 24 - 13, x + math.sin(k / 6) * 14 + 13, y - k * h / 24 + 13], fill=(140, 104, 70))
    tx, ty = x + math.sin(4) * 14, y - h
    for a in range(0, 360, 40):
        r = math.radians(a + rng.integers(-10, 10)); ex, ey = tx + math.cos(r) * 170, ty + math.sin(r) * 80 + 40
        d.polygon([tx, ty, ex, ey, (tx + ex) / 2 + 20, (ty + ey) / 2 + 26], fill=(54, 140, 70))
def background(scene, rng):
    im = Image.new("RGBA", (W, H)); d = ImageDraw.Draw(im)
    indoor = scene in ("office", "home", "shop")
    if indoor:
        wall = [(246, 232, 200), (214, 232, 240), (240, 220, 226), (224, 238, 214)][rng.integers(4)]
        d.rectangle([0, 0, W, 1420], fill=wall); d.rectangle([0, 1420, W, H], fill=(196, 160, 120) if scene != "office" else (190, 196, 204))
        for x in range(0, W, 120): d.line([x, 1420, x - 160, H], fill=(180, 146, 110) if scene != "office" else (176, 182, 190), width=3)
        d.rounded_rectangle([90, 720, 470, 1080], 10, fill=(170, 214, 240), outline=(255, 255, 255), width=18); d.line([280, 720, 280, 1080], fill=(255, 255, 255), width=10)
        if scene == "office": d.rectangle([600, 1150, 1040, 1190], fill=(150, 110, 80)); d.rounded_rectangle([700, 960, 940, 1140], 12, fill=(40, 44, 52))
        elif scene == "home": d.rounded_rectangle([560, 1180, 1060, 1400], 40, fill=[(120, 80, 140), (60, 120, 160), (180, 90, 70)][rng.integers(3)]); d.rectangle([620, 760, 920, 980], fill=(200, 160, 90), outline=(120, 90, 60), width=10)
        else:
            for k in range(3): d.rectangle([560, 760 + k * 170, 1060, 780 + k * 170], fill=(150, 110, 80))
            for k in range(12): d.rounded_rectangle([580 + (k % 6) * 80, 690 + (k // 6) * 170, 640 + (k % 6) * 80, 760 + (k // 6) * 170], 8, fill=SHIRTS[rng.integers(len(SHIRTS))])
        return im
    sky = [(150, 210, 245), (170, 220, 250), (250, 200, 160)][rng.integers(3)]
    for y in range(0, 1300, 4): k = y / 1300; d.rectangle([0, y, W, y + 4], fill=tuple(int(sky[i] * (1 - k * 0.25) + 255 * k * 0.25) for i in range(3)))
    for k in range(3): cx, cy = rng.integers(80, 1000), rng.integers(560, 900); [d.ellipse([cx + j * 50 - 70, cy - 30 - (j % 2) * 20, cx + j * 50 + 70, cy + 40], fill=(255, 255, 255)) for j in range(3)]
    d.rectangle([0, 1240, W, H], fill=(196, 138, 90)); d.rectangle([0, 1200, W, 1250], fill=(92, 160, 80))
    for x in (60, 1000) if rng.random() < 0.5 else (140, 940): palm(d, x, 1260, 520, rng)
    if scene == "teashop":
        d.rectangle([300, 860, 1000, 1260], fill=(236, 214, 170)); d.polygon([260, 880, 650, 720, 1040, 880], fill=(186, 72, 52))
        d.rectangle([360, 940, 940, 1010], fill=(250, 240, 220)); d.rectangle([360, 1060, 940, 1110], fill=(120, 80, 50))
        for k in range(5): d.ellipse([400 + k * 100, 1020, 450 + k * 100, 1058], fill=(250, 250, 250))
    elif scene == "busstop":
        d.rectangle([260, 900, 280, 1260], fill=(120, 120, 130)); d.rectangle([800, 900, 820, 1260], fill=(120, 120, 130)); d.polygon([220, 900, 860, 900, 820, 840, 260, 840], fill=(52, 120, 180))
        d.rectangle([300, 1130, 780, 1160], fill=(150, 110, 70)); d.rounded_rectangle([880, 960, 1040, 1040], 10, fill=(240, 240, 240)); d.rectangle([955, 1040, 965, 1260], fill=(120, 120, 130))
    else:   # village road
        d.polygon([440, 1250, 640, 1250, 1000, H, 80, H], fill=(120, 120, 126)); d.rectangle([380, 980, 700, 1240], fill=(240, 230, 210)); d.polygon([350, 1000, 540, 880, 730, 1000], fill=(186, 72, 52))
    return im

# ---------------- reel ----------------
def mouth_track(wav, t0):
    """Per-frame mouth opening from the voice's loudness."""
    n = len(wav) // (SR // FPS); out = {}
    for i in range(n):
        seg = wav[i * (SR // FPS):(i + 1) * (SR // FPS)]; v = float(np.sqrt(np.mean(seg ** 2))) if len(seg) else 0
        out[int(round(t0 * FPS)) + i] = min(1.0, v * 6)
    return out

def build(s, out, seed=0):
    rng = np.random.default_rng(abs(hash(s["id"])) % (2 ** 31) + seed)
    cast = s["cast"]                     # {"A": "name" or ("name", "type"), ...}
    people = {}
    used = set()
    for k, v in cast.items():
        nm, kind = (v if isinstance(v, (tuple, list)) else (v, None))
        if not kind and k == s.get("mentor", "B" if "B" in cast else None):
            kind = "ammachi" if is_female(nm) else "elder"        # the mentor is the appooppan / ammachi
        # a series keeps its people: the same name in the same series always looks the same; one-off reels vary
        import hashlib
        prng = np.random.default_rng(int(hashlib.md5(f"{s.get('series') or s['id']}|{nm}".encode()).hexdigest()[:8], 16))
        if not kind:
            pool = [t for t in (FEMALE_T if is_female(nm) else MALE_T) if t not in used and (t not in ("elder", "ammachi") or k == s.get("mentor"))]
            kind = pool[prng.integers(len(pool))]
        used.add(kind); people[k] = dict(name=nm, look=make_look(kind, prng))
    keys = list(cast)
    voice = {k: voice_for(people[k]["name"], i) for i, k in enumerate(keys)}
    for i, k in enumerate(keys[1:], 1):
        if voice[k] == voice[keys[0]]: voice[k] = voice[k][0] + ("2" if voice[k][-1] != "2" else "1")
    full = {k: [person(p["look"], m) for m in (0.0, 0.5, 1.0)] + [person(p["look"], 0, True)] for k, p in people.items()}
    SC = 0.74 if len(cast) > 2 else 0.8; SPW, SPH = int(PW * SC), int(PH * SC)
    sprites = {k: [im.resize((SPW, SPH), Image.LANCZOS) for im in v] for k, v in full.items()}
    BG = background(s.get("scene", ["teashop", "busstop", "road", "home", "office", "shop"][rng.integers(6)]), rng)
    n = len(keys); xs = {k: int(W / (n + 1) * (i + 1) - SPW / 2) + (i - (n - 1) / 2) * 40 for i, k in enumerate(keys)}
    flip = {k: xs[k] + SPW / 2 > W / 2 + 10 for k in keys}                                   # people on the right face left
    for k in keys:
        if flip[k]: sprites[k] = [im.transpose(Image.FLIP_LEFT_RIGHT) for im in sprites[k]]

    aud, mouths, t = [], {}, 0.15
    hook_box = None
    if s.get("hook"):
        hb = fit_block(s["hook"], 70, (20, 20, 24), 860, 330); hook_box = rrect(hb.width + 40, hb.height + 20, 34, (255, 214, 64, 255)); hook_box.alpha_composite(hb, (20, 10))
    story = []
    for who, txt in s["lines"]:
        w = load_wav(say(txt, voice[who])); aud.append((t, w)); mouths.setdefault(who, {}).update(mouth_track(w, t))
        story.append(dict(who=who, txt=txt, t0=t, t1=t + len(w) / SR + 0.12)); t = story[-1]["t1"]
    t_story = t + 0.2
    card = s.get("card"); rows = []
    if card:
        t += 0.5; tw = load_wav(say(card["title"].replace("\n", " "), "NARRATOR")); aud.append((t, tw)); t_card = t; t += len(tw) / SR + 0.2
        for lab, val in card["rows"] + ([card["total"]] if card.get("total") else []):
            w = load_wav(say(f"{lab}, {val}", "NARRATOR")); aud.append((t, w)); rows.append(dict(lab=lab, val=val, t=t)); t += len(w) / SR + 0.25
        t_card_end = t + 0.4; t = t_card_end
    m = s.get("mentor", keys[0]); rules = []
    for i, r in enumerate(s.get("rules", [])):
        w = load_wav(say(r, voice[m])); t += 0.4; aud.append((t, w)); mouths.setdefault("R" + m, {}).update(mouth_track(w, t))
        rules.append(dict(n=i + 1, txt=r, t0=t, t1=t + len(w) / SR)); t = rules[-1]["t1"] + 0.3
    t_end = t + 0.3; DUR = t_end + 4.5

    END, PILL, (PX, PY) = end_card(s)
    if s.get("series"):
        rib = rrect(760, 96, 48, (204, 92, 52, 255)); tdraw(ImageDraw.Draw(rib), (760 - tlen(f"{s['series']} · Episode {s.get('ep', 1)}", 40)) / 2, 64, f"{s['series']} · Episode {s.get('ep', 1)}", 40, (255, 255, 255))
        END.alpha_composite(rib, ((W - 760) // 2, 220))
        if s.get("next"):
            nb = block("അടുത്ത എപ്പിസോഡ്: " + s["next"], 42, (204, 92, 52), maxw=900, wt=800); END.alpha_composite(nb, ((W - nb.width) // 2, 1560))
    subs = {}
    def sub_img(txt):
        if txt not in subs:
            b = fit_block(txt, 54, (255, 255, 255), 940, 250, stroke=7, sfill=(20, 20, 24)); subs[txt] = b
        return subs[txt]
    rule_bg = Image.new("RGBA", (W, H), (252, 246, 232, 255)); ImageDraw.Draw(rule_bg).ellipse([W / 2 - 300, 1290, W / 2 + 300, 1360], fill=(232, 222, 200))
    card_bg = Image.new("RGBA", (W, H), (250, 250, 252, 255))
    big_m = [im.resize((int(PW * 0.86), int(PH * 0.86)), Image.LANCZOS) for im in full[m]]
    if flip[m]: big_m = [im.transpose(Image.FLIP_LEFT_RIGHT) for im in big_m]
    small_m = [im.resize((int(PW * 0.5), int(PH * 0.5)), Image.LANCZOS).transpose(Image.FLIP_LEFT_RIGHT) for im in full[m][:1]]   # the mentor watches the card

    def mouth_at(k, fr): v = k.get(fr, 0); return 0 if v < 0.12 else (1 if v < 0.45 else 2)
    def frame(tt):
        fr = int(round(tt * FPS)); blink = (fr % 97) < 4
        if tt < t_story:
            im = BG.copy(); cur = next((x for x in story if x["t0"] <= tt < x["t1"]), story[-1] if tt >= story[-1]["t0"] else None)
            for k in keys:
                sp = sprites[k][3] if blink and not (cur and cur["who"] == k) else sprites[k][mouth_at(mouths.get(k, {}), fr)]
                hop = -10 * abs(math.sin(tt * 7)) if cur and cur["who"] == k else 0
                paste(im, sp, xs[k], 1600 - SPH + hop)
            if hook_box: paste(im, hook_box, (W - hook_box.width) // 2, 150)
            if cur:
                b = sub_img(cur["txt"]); paste(im, b, (W - b.width) // 2, 400 if hook_box is None else 150 + hook_box.height + 20)
                nm = people[cur["who"]]["name"]; tg = rrect(int(tlen(nm, 36)) + 40, 60, 30, (20, 20, 24, 220)); tdraw(ImageDraw.Draw(tg), 20, 43, nm, 36, (255, 214, 64))
                paste(im, tg, xs[cur["who"]] + SPW // 2 - tg.width // 2, 1600 - SPH * people[cur["who"]]["look"]["h"] - 75)
            return im, None
        if card and tt < t_card_end:
            im = card_bg.copy(); d = ImageDraw.Draw(im)
            tb = fit_block(card["title"], 64, (20, 24, 40), 900, 300); paste(im, tb, (W - tb.width) // 2, 160)
            y = 200 + tb.height + 30; shown = 0
            for i, r in enumerate(rows):
                if tt < r["t"]: break
                shown += 1; last = card.get("total") and i == len(rows) - 1
                p = ease((tt - r["t"]) / 0.3); vw = tlen(r["val"], 54); room = 920 - 104 - vw - 50
                ll = wrap(r["lab"], 46, room if room >= 300 else 780, 600); below = room < 300
                hh = 70 + 60 * len(ll) + (66 if below else 0)
                c = rrect(940, hh, 30, (255, 234, 234, 255) if last else (238, 243, 250, 255)); cd = ImageDraw.Draw(c)
                cd.ellipse([28, hh / 2 - 26, 80, hh / 2 + 26], fill=(210, 50, 50) if last else (255, 196, 40)); tdraw(cd, 54 - tlen(str(i + 1), 34) / 2, hh / 2 + 12, "!" if last else str(i + 1), 34, (255, 255, 255) if last else (20, 24, 40))
                for j, l in enumerate(ll): tdraw(cd, 104, 82 + j * 60, l, 46, (40, 44, 60), 600)
                tdraw(cd, 912 - vw, (hh - 26) if below else hh / 2 + 18, r["val"], 54, (210, 50, 50) if last else (20, 120, 70))
                paste(im, c, 70 + (1 - p) * 80, y, alpha=p); y += hh + 24
            mo = mouth_at(mouths.get("N", {}), fr); paste(im, small_m[0], W - small_m[0].width - 30, 1600 - small_m[0].height)
            return im, ("card", shown, int(tt * 4) if any(tt - r["t"] < 0.35 for r in rows) else 0)
        if tt < t_end:
            im = rule_bg.copy(); cur = next((r for r in rules if tt >= r["t0"] - 0.4), None); cur = [r for r in rules if tt >= r["t0"] - 0.4][-1] if rules and tt >= rules[0]["t0"] - 0.4 else None
            mo = mouth_at(mouths.get("R" + m, {}), fr); sp = big_m[3] if blink and mo == 0 else big_m[mo]
            paste(im, sp, (W - sp.width) // 2, 1310 - sp.height + 20)
            if cur:
                pl = rrect(330, 100, 50, (20, 24, 40, 255)); tdraw(ImageDraw.Draw(pl), (330 - tlen(f"Rule #{cur['n']}", 54)) / 2, 70, f"Rule #{cur['n']}", 54, (255, 214, 64)); paste(im, pl, (W - 330) // 2, 120)
                b = fit_block(cur["txt"], 58, (20, 24, 40), 940, 250); paste(im, b, (W - b.width) // 2, 230)
            return im, None
        a = ease((tt - t_end) / 0.35); im = END.copy(); paste(im, PILL, PX, PY, scale=1 + 0.03 * math.sin((tt - t_end) * 5))
        return im, None if a < 1 else ("end", int(tt * 10))

    mx = Mixer(DUR, seed); mx.room(0.025, 0.015 if s.get("scene") not in ("office", "home", "shop") else 0)
    if s.get("scene") not in ("office", "home", "shop"): mx.birds(t_story)
    for t0, w in aud: mx.add(t0, w)
    for r in rows: mx.blip(r["t"] - 0.05, 760)
    wav = out + ".wav"; mx.save(wav); encode(frame, DUR, wav, out); os.remove(wav)
    return dict(duration=round(DUR, 1), cover_frame=frame(0.6)[0])

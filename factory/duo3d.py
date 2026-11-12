"""3D two-person dialogue reel in one of ~50 Kerala / Gulf locations; background sound varies per reel."""
import json, math
import numpy as np
from PIL import Image, ImageDraw
from common import *
from voice import say

# Settings: each has its own stills folder, default people and ambience. Scripts may override names.
# name pair (A, V) and sound kind per location; scripts may override names.
_S = dict(
    teashop=("അനു", "വിഷ്ണു", "street"), office=("നേഹ", "രാഹുൽ", "indoor"), home=("സ്നേഹ", "അരുൺ", "indoor"), gulf=("ഷിജു", "ഫൈസൽ", "indoor"),
    busstop=("ജിബിൻ", "അഖിൽ", "street"), hospital=("ലക്ഷ്മി", "ജോസഫ്", "busy"), bank=("ശ്രുതി", "മനോജ്", "busy"), canteen=("ആതിര", "അമൽ", "busy"),
    shop=("ബിനു", "സുരേഷ്", "street"), beach=("ദിവ്യ", "നിഖിൽ", "water"), cafe=("ആൽവിൻ", "റോഷൻ", "indoor"), airport=("ഷമീർ", "റഫീഖ്", "busy"),
    farm=("വാസു", "ഗോപി", "nature"), thattukada=("സിജോ", "ബിജു", "night"), autostand=("സജി", "ഷാജി", "street"), ferry=("മീര", "ടോണി", "water"),
    metro=("അഞ്ജലി", "കിരൺ", "busy"), rubber=("ജോയി", "തോമസ്", "nature"), fishmarket=("സുമ", "ആന്റണി", "busy"), textile=("രമ്യ", "പ്രകാശ്", "indoor"),
    weddinghall=("കാവ്യ", "ശരത്", "busy"), classroom=("നിമ്മി", "ആദർശ്", "indoor"), library=("ഗ്രീഷ്മ", "അനൂപ്", "indoor"), gym=("റിയ", "ജസ്റ്റിൻ", "indoor"),
    salon=("സോണിയ", "വിനീത്", "indoor"), mobileshop=("ഹന്ന", "ഫഹദ്", "street"), bakery=("ജിഷ", "സാബു", "street"), hotellobby=("നീതു", "ജെയ്സൺ", "indoor"),
    rooftop=("ആര്യ", "ശ്യാം", "night"), balcony=("അമ്മു", "വിവേക്", "nature"), kitchen=("ബിന്ദു", "രാജേഷ്", "indoor"), veranda=("ശാന്ത", "ബാലൻ", "nature"),
    railway=("ഷീബ", "ദിനേശ്", "busy"), hostel=("അലീന", "സഞ്ജു", "indoor"), garage=("ഐശ്വര്യ", "ജിതിൻ", "indoor"), pharmacy=("സിനി", "പ്രവീൺ", "street"),
    tailor=("ഉഷ", "മോഹനൻ", "indoor"), homestay=("ടീന", "ജോമോൻ", "nature"), munnar=("സെലിൻ", "ബേസിൽ", "nature"), handloom=("ലീല", "കുമാർ", "indoor"),
    park=("ഗായത്രി", "അനന്തു", "nature"), juiceshop=("റസിയ", "നൗഷാദ്", "street"), foodcourt=("മരിയ", "ഡെന്നിസ്", "busy"), akshaya=("സുധ", "രമേശ്", "busy"),
    photocopy=("അശ്വതി", "ഉണ്ണി", "street"), petrolpump=("സന്തോഷ്", "ഷിബു", "street"), courier=("ജയ", "അരവിന്ദ്", "street"), gulfoffice=("ഷഹാന", "ആസിഫ്", "indoor"),
    gulfroom=("നസീർ", "ഷംസു", "indoor"), mall=("സുമയ്യ", "ജാഫർ", "busy"))
SCENES = {k: dict(dir="" if k == "teashop" else k, names=(a, b), amb=m) for k, (a, b, m) in _S.items()}
# a script written for one of the 4 original settings can play in any of these compatible places
GROUPS = {
    "teashop": ["teashop", "thattukada", "busstop", "autostand", "juiceshop", "bakery", "park", "farm", "rubber", "ferry", "beach", "petrolpump", "fishmarket", "munnar", "homestay", "railway", "shop"],
    "office": ["office", "cafe", "garage", "library", "hostel", "akshaya", "photocopy", "courier", "metro", "canteen", "classroom", "bank", "hotellobby", "foodcourt", "mobileshop", "pharmacy", "tailor", "textile", "salon", "gym", "handloom"],
    "home": ["home", "kitchen", "veranda", "balcony", "rooftop", "hospital", "weddinghall"],
    "gulf": ["gulf", "gulfroom", "gulfoffice", "mall", "airport"],
}
def fits(scene, names):
    """True when the two names have the same genders as the two people drawn in this location
    (each location's default names describe its 3D characters: left A, right V)."""
    from voice import is_female
    return tuple(is_female(n) for n in names) == tuple(is_female(n) for n in SCENES[scene]["names"])

def available(scene):
    import os
    d = f"{ROOT}/assets/stills" + ("/" + SCENES[scene]["dir"] if SCENES[scene]["dir"] else "")
    return (os.path.exists(f"{d}/wide_rest.png") or os.path.exists(f"{d}/wide_rest.jpg")) and os.path.exists(f"{d}/V_v.png")
_CACHE = {}
def assets(scene="teashop"):
    import os
    if scene not in _CACHE:
        ST = f"{ROOT}/assets/stills" + ("/" + SCENES[scene]["dir"] if SCENES[scene]["dir"] else "")
        ov = json.load(open(f"{ST}/ov.json")) if os.path.exists(f"{ST}/ov.json") else None
        def load(cam, tag):
            rp = f"{ST}/{cam}_rest.jpg" if os.path.exists(f"{ST}/{cam}_rest.jpg") else f"{ST}/{cam}_rest.png"
            rest = Image.open(rp).convert("RGBA")
            if tag == "rest": return rest
            v = Image.open(f"{ST}/{cam}_{tag}.png").convert("RGBA"); out = rest.copy()
            out.alpha_composite(v, tuple(ov[f"{cam}_{tag}"]) if ov else (0, 0)); return out
        img = {("wide", "rest"): load("wide", "rest"), ("wide", "A"): load("wide", "a"), ("wide", "V"): load("wide", "v"),
               ("A", "rest"): load("A", "rest"), ("A", "A"): load("A", "a"), ("V", "rest"): load("V", "rest"), ("V", "V"): load("V", "v")}
        import os
        if os.path.exists(f"{ST}/movers.json"):
            mov = json.load(open(f"{ST}/movers.json"))
            fg = {c: Image.open(f"{ST}/{c}_fgmask.png").convert("RGBA").getchannel("A") for c in ("wide", "A", "V")}
            spr = {(c, n): Image.open(f"{ST}/{c}_{n}.png").convert("RGBA") for c in ("wide", "A", "V") for n in ("auto", "cyc")}
        else: mov, fg, spr = None, None, None
        _CACHE[scene] = (img, mov, fg, spr)
    return _CACHE[scene]

def build(s, out, seed=0):
    from voice import voice_for
    scene = s.get("scene", "teashop"); IMG, MOV, FG, SPR = assets(scene)
    nm = s.get("names") or SCENES[scene]["names"]
    if not fits(scene, nm): raise ValueError(f"names {nm} do not match the people drawn in {scene} {SCENES[scene]['names']}")
    NAMES = {"A": (nm[0], (255, 196, 40)), "V": (nm[1], (120, 190, 255))}
    VOICE = {"A": voice_for(nm[0], 0), "V": voice_for(nm[1], 1)}
    if VOICE["A"] == VOICE["V"]: VOICE["V"] = VOICE["V"][0] + "2"
    rng = np.random.default_rng(seed)
    t = 0.15; segs = []   # no silent intro: the first line is heard at once, the hook stays on screen above it
    wavs = []
    for i, (who, cam, txt) in enumerate(s["lines"]):
        w = say(txt, VOICE[who]); vd = wav_len(w); wavs.append((t, w))
        segs.append(dict(kind="line", who=who, cam=cam, txt=txt, t0=t, t1=t + vd + 0.12, vd=vd)); t += vd + 0.12
    t_end = t; DUR = t_end + 4.5
    # traffic plan varies per reel
    TR = []; tt0 = rng.uniform(1.5, 4) if MOV else 1e9
    while tt0 < DUR:
        name = "auto" if rng.random() < 0.55 else "cyc"; v = (5.2 if name == "auto" else 1.7) * (1 if rng.random() < 0.5 else -1)
        TR.append((name, tt0, v, -12 if v > 0 else 12)); tt0 += rng.uniform(6, 10)
    BIRDS = [(b, rng.uniform(0.8, 1.2)) for b in np.arange(rng.uniform(0, 3), DUR, rng.uniform(6, 9))] if MOV else []

    def compose(cam, base, tt):
        if not MOV: return base
        out = base.copy(); W0 = base.width
        for name, t0, v, x0 in TR:
            x = x0 + v * (tt - t0)
            if tt < t0 or abs(x) > 13: continue
            m = MOV[f"{cam}_{name}"]; sp = SPR[(cam, name)]; dx = int((x - m["x0"]) * m["px_per_m"])
            if abs(dx) > W0: continue
            if v < 0:
                bb = sp.getchannel("A").getbbox()
                if bb: c = sp.crop(bb).transpose(Image.FLIP_LEFT_RIGHT); sp = Image.new("RGBA", sp.size, (0, 0, 0, 0)); sp.paste(c, (bb[0], bb[1]))
            out.paste(sp, (dx, int(2 * math.sin(tt * 30)) if name == "auto" else 0), sp)
        d = ImageDraw.Draw(out)
        for b0, sc in BIRDS:
            u = (tt - b0) / 7.0
            if 0 <= u <= 1:
                bx = -60 + u * (W0 + 120); by = base.height * (0.30 + 0.05 * math.sin(u * 6)); w = 16 * sc; fl = 7 * sc * math.sin(tt * 14 + b0)
                d.line([(bx - w, by - fl), (bx, by), (bx + w, by - fl)], fill=(40, 40, 45), width=max(2, int(3 * sc)))
        out.paste(base, (0, 0), FG[cam]); return out

    caps = {}
    def caption(seg):
        if seg["txt"] not in caps:
            b = fit_block(seg["txt"], 58, (255, 255, 255), 860, 330)
            name, col = NAMES[seg["who"]]; nw = int(tlen(name, 40)) + 44
            chip = rrect(nw, 62, 31, col + (255,)); tdraw(ImageDraw.Draw(chip), 22, 45, name, 40, (20, 24, 34))
            card = rrect(940, b.height + 24, 40, (16, 22, 34, 205)); card.alpha_composite(b, (20, 12)); caps[seg["txt"]] = (card, chip)
        return caps[seg["txt"]]
    hook_im = fit_block(s["hook"], 70, (255, 214, 60), 940, 330, stroke=6, sfill=(30, 20, 10))
    HOOK_T = next((x["t1"] for x in segs if x["t1"] >= 4.0), segs[-1]["t1"])   # end of the line that crosses 4 s
    END, PILL, (PX, PY) = end_card(s)

    def frame(tt):
        if tt >= t_end + 0.35:
            im = END.copy(); paste(im, PILL, PX, PY, scale=1 + 0.03 * math.sin((tt - t_end) * 5)); return im, None
        seg = next((x for x in segs if x["t0"] <= tt < x["t1"]), segs[0]) if tt < t_end else segs[-1]
        lt = max(0.0, tt - seg["t0"]); dur = seg["t1"] - seg["t0"]
        talk = seg["kind"] == "line" and 0.05 < lt < seg["vd"] - 0.05
        flap = talk and (math.sin(lt * 21) + 0.6 * math.sin(lt * 33 + 1.3)) > -0.15
        src = compose(seg["cam"], IMG[(seg["cam"], seg["who"] if flap else "rest")], tt)
        z = 1.0 + 0.045 * min(1.0, lt / max(dur, 0.1)) + (0.004 * abs(math.sin(lt * 10)) if talk else 0)
        cw, ch = W / z, H / z; cx, cy = W / 2, H * 0.47
        im = src.crop((int(cx - cw / 2), int(cy - ch * 0.47), int(cx + cw / 2), int(cy + ch * 0.53))).resize((W, H), Image.BILINEAR)
        # hook is visible from the very first frame and stays over the first lines (about 4 s), then cuts away
        cy = 300
        if tt < HOOK_T:   # clean cut when the next line starts
            paste(im, hook_im, (W - hook_im.width) // 2, 170); cy = max(300, 170 + hook_im.height + 70)
        card, chip = caption(seg); p = ease(lt / 0.2) if seg is not segs[0] else 1.0
        paste(im, card, (W - card.width) // 2, cy + (1 - p) * 24, alpha=p, scale=0.94 + 0.06 * p)
        paste(im, chip, (W - card.width) // 2 + 30, cy - 40 + (1 - p) * 24, alpha=p)
        if tt >= t_end: paste(im, END, 0, 0, alpha=ease((tt - t_end) / 0.35))
        return im, None

    amb = SCENES[scene]["amb"]; mx = Mixer(DUR, seed)
    # not every reel gets a background bed: about a third are voice-only, a third very light, a third the place's own sounds
    mode = s.get("sound") or ["clean", "light", "place"][int(rng.integers(0, 3))]
    if mode == "light": mx.room(0.018, 0.0)
    elif mode == "place":
        if amb == "street": mx.room(0.03, 0.012); mx.birds(DUR, every=5.0, vol=0.02)
        elif amb == "busy": mx.room(0.03, 0.02)
        elif amb == "nature": mx.birds(DUR, every=3.5, vol=0.03); mx.room(0.012, 0.0)
        elif amb == "water":
            mx.room(0.01, 0.0); tt_ = np.arange(mx.n) / SR; kk = np.exp(-np.arange(900) / 300.0); kk /= kk.sum()
            mx.x += (np.convolve(rng.standard_normal(mx.n), kk, "same") * 0.25 * (0.5 + 0.5 * np.sin(2 * np.pi * 0.12 * tt_)) ** 2).astype(np.float32)
        elif amb == "night":
            mx.room(0.012, 0.0)
            for t0k in np.arange(0.5, DUR, 0.9):   # crickets
                u = np.arange(int(SR * 0.12)) / SR; mx.add(t0k + rng.uniform(0, 0.3), (np.sin(2 * np.pi * 4300 * u) * (np.sin(2 * np.pi * 45 * u) > 0) * np.hanning(len(u)) * 0.012).astype(np.float32))
        else: mx.room(0.02, 0.0)
    for t0, w in wavs: mx.add(t0, load_wav(w))
    if mode == "place" and amb in ("street", "nature"):
        for t0c in rng.uniform(1, DUR - 1, 2):   # a couple of glass clinks
            u = np.arange(int(SR * 0.25)) / SR; mx.add(t0c, ((np.sin(2 * np.pi * 2900 * u) + 0.5 * np.sin(2 * np.pi * 4350 * u)) * np.exp(-u * 30) * 0.04).astype(np.float32))
    if mode != "place": TR = []
    k = np.exp(-np.arange(120) / 60.0); k /= k.sum()
    for name, t0, v, x0 in TR:
        T = abs(24 / v); u = np.arange(int(SR * T)) / SR; amp = 1 / (1 + ((x0 + v * u) / 4) ** 2)
        if name == "auto":
            eng = np.convolve(np.sign(np.sin(2 * np.pi * 28 * u)) * (0.5 + 0.5 * np.sin(2 * np.pi * 7 * u)), k, "same"); mx.add(t0, (eng * amp * 0.09).astype(np.float32))
        else:
            bu = np.arange(int(SR * 0.6)) / SR
            for r in (0, 0.18): mx.add(t0 + T / 2 - 0.5 + r, ((np.sin(2 * np.pi * 2350 * bu) + 0.6 * np.sin(2 * np.pi * 3700 * bu)) * np.exp(-bu * 7) * 0.05).astype(np.float32))
    wav = out + ".wav"; mx.save(wav)
    encode(frame, DUR, wav, out)
    import os; os.remove(wav)
    return dict(duration=round(DUR, 1), cover_frame=compose("wide", IMG[("wide", "rest")], 0.0))


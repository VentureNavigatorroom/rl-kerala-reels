"""3D tea-shop dialogue reel (Anu + Vishnu) with passing traffic and street sounds."""
import json, math
import numpy as np
from PIL import Image, ImageDraw
from common import *
from voice import say

# Settings: each has its own stills folder, default people and ambience. Scripts may override names.
SCENES = {
    "teashop": dict(dir="", names=("അനു", "വിഷ്ണു"), amb="street"),
    "office":  dict(dir="office", names=("നേഹ", "രാഹുൽ"), amb="office"),
    "home":    dict(dir="home", names=("സ്നേഹ", "അരുൺ"), amb="home"),
    "gulf":    dict(dir="gulf", names=("ഷിജു", "ഫൈസൽ"), amb="gulf"),
}
_CACHE = {}
def assets(scene="teashop"):
    if scene not in _CACHE:
        ST = f"{ROOT}/assets/stills" + ("/" + SCENES[scene]["dir"] if SCENES[scene]["dir"] else "")
        def load(cam, tag):
            rest = Image.open(f"{ST}/{cam}_rest.png").convert("RGBA")
            if tag == "rest": return rest
            v = Image.open(f"{ST}/{cam}_{tag}.png").convert("RGBA"); out = rest.copy(); out.alpha_composite(v); return out
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
    NAMES = {"A": (nm[0], (255, 196, 40)), "V": (nm[1], (120, 190, 255))}
    VOICE = {"A": voice_for(nm[0], 0), "V": voice_for(nm[1], 1)}
    if VOICE["A"] == VOICE["V"]: VOICE["V"] = VOICE["V"][0] + "2"
    rng = np.random.default_rng(seed)
    t = 2.8; segs = [dict(kind="hook", cam="wide", who="A", t0=0.0, t1=2.8)]
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
    hook_im = fit_block(s["hook"], 70, (255, 214, 60), 940, 380, stroke=6, sfill=(30, 20, 10))
    END, PILL, (PX, PY) = end_card(s)

    def frame(tt):
        if tt >= t_end + 0.35:
            im = END.copy(); paste(im, PILL, PX, PY, scale=1 + 0.03 * math.sin((tt - t_end) * 5)); return im, None
        seg = next(x for x in segs if x["t0"] <= tt < x["t1"]) if tt < t_end else segs[-1]
        lt = tt - seg["t0"]; dur = seg["t1"] - seg["t0"]
        talk = seg["kind"] == "line" and 0.05 < lt < seg["vd"] - 0.05
        flap = talk and (math.sin(lt * 21) + 0.6 * math.sin(lt * 33 + 1.3)) > -0.15
        src = compose(seg["cam"], IMG[(seg["cam"], seg["who"] if flap else "rest")], tt)
        z = 1.0 + 0.045 * min(1.0, lt / max(dur, 0.1)) + (0.004 * abs(math.sin(lt * 10)) if talk else 0)
        cw, ch = W / z, H / z; cx, cy = W / 2, H * 0.47
        im = src.crop((int(cx - cw / 2), int(cy - ch * 0.47), int(cx + cw / 2), int(cy + ch * 0.53))).resize((W, H), Image.BILINEAR)
        if seg["kind"] == "hook":
            p = ease(lt / 0.3); paste(im, hook_im, (W - hook_im.width) // 2, 300 + (1 - p) * 30, alpha=p)
        else:
            card, chip = caption(seg); p = ease(lt / 0.2)
            paste(im, card, (W - card.width) // 2, 300 + (1 - p) * 24, alpha=p, scale=0.94 + 0.06 * p)
            paste(im, chip, (W - card.width) // 2 + 30, 260 + (1 - p) * 24, alpha=p)
        if tt >= t_end: paste(im, END, 0, 0, alpha=ease((tt - t_end) / 0.35))
        return im, None

    amb = SCENES[scene]["amb"]; mx = Mixer(DUR, seed)
    if amb == "street": mx.room(); mx.birds(DUR)
    elif amb == "office":
        mx.room(0.04, 0.02)
        for t0k in np.arange(rng.uniform(1, 3), DUR, 0.11):           # distant keyboard bursts
            if rng.random() < 0.35:
                u = np.arange(int(SR * 0.02)) / SR; mx.add(t0k, (rng.standard_normal(len(u)) * np.exp(-u * 300) * 0.02).astype(np.float32))
    elif amb == "home":
        mx.room(0.035, 0.0); mx.birds(DUR, every=4.5, vol=0.025)
        tt_ = np.arange(mx.n) / SR; mx.x += (np.sin(2 * np.pi * 95 * tt_) * 0.004 * (1 + 0.3 * np.sin(2 * np.pi * 4 * tt_))).astype(np.float32)   # ceiling fan
    else:
        mx.room(0.05, 0.0); tt_ = np.arange(mx.n) / SR; mx.x += (np.sin(2 * np.pi * 120 * tt_) * 0.005).astype(np.float32)   # AC hum
    for t0, w in wavs: mx.add(t0, load_wav(w))
    for t0c in (rng.uniform(1, DUR - 1, 4) if amb in ("street", "home") else []):   # glass clinks
        u = np.arange(int(SR * 0.25)) / SR; mx.add(t0c, ((np.sin(2 * np.pi * 2900 * u) + 0.5 * np.sin(2 * np.pi * 4350 * u)) * np.exp(-u * 30) * 0.06).astype(np.float32))
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


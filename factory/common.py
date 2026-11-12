"""Shared drawing, text and audio helpers for all reel types (Malayalam-aware)."""
import os, math, subprocess
import numpy as np
from PIL import Image, ImageDraw, ImageFont

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
W, H, FPS, SR = 1080, 1920, 30, 44100
FD = f"{ROOT}/assets/fonts"
BRAND = "rejectionlist.kerala"

_fc = {}
def font(script, size, wt=800):
    k = (script, size, wt)
    if k not in _fc:
        _fc[k] = ImageFont.truetype(f"{FD}/anek-malayalam-{script}-{600 if wt < 700 else 800}.ttf", size, layout_engine=ImageFont.Layout.RAQM)
    return _fc[k]

import re
_EMOJI = re.compile("[\U0001F000-\U0001FFFF\u2600-\u27BF\uFE0F\u200B]")
def runs(text):
    text = re.sub("  +", " ", _EMOJI.sub("", text)).strip() if _EMOJI.search(text) else text
    text = text.replace("₹", "Rs.").replace("→", ">")
    out = []
    for ch in text:
        k = "malayalam" if ("ഀ" <= ch <= "ൿ" or ch in "‌‍") else "latin"
        if ch == " " and out: k = out[-1][0]
        if out and out[-1][0] == k: out[-1][1] += ch
        else: out.append([k, ch])
    return out

def tlen(text, size, wt=800): return sum(font(k, size, wt).getlength(t) for k, t in runs(text))

def tdraw(d, x, y, text, size, fill, wt=800, stroke=0, sfill=(0, 0, 0)):
    for k, t in runs(text):
        f = font(k, size, wt); d.text((x, y), t, font=f, fill=fill, stroke_width=stroke, stroke_fill=sfill, anchor="ls"); x += f.getlength(t)

def wrap(text, size, maxw, wt=800):
    out = []
    for para in text.split("\n"):
        line = ""
        for w in para.split(" "):
            t = (line + " " + w).strip()
            if tlen(t, size, wt) <= maxw or not line: line = t
            else: out.append(line); line = w
        out.append(line)
    return out

def block(text, size, fill, maxw=900, wt=800, stroke=0, sfill=(0, 0, 0), lh=1.5, align="center"):
    lines = wrap(text, size, maxw, wt); L = int(size * lh)
    im = Image.new("RGBA", (maxw + 40, L * len(lines) + 40), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    for i, l in enumerate(lines):
        x = 20 + ((maxw - tlen(l, size, wt)) / 2 if align == "center" else 0)
        tdraw(d, x, 20 + int(size * 1.05) + i * L, l, size, fill, wt, stroke, sfill)
    return im

def fit_block(text, size, fill, maxw, maxh, **k):
    while size > 30:
        b = block(text, size, fill, maxw=maxw, **k)
        if b.height <= maxh: return b
        size -= 4
    return block(text, size, fill, maxw=maxw, **k)

def rrect(w, h, r, fill, ss=2):
    im = Image.new("RGBA", (w * ss, h * ss), (0, 0, 0, 0)); ImageDraw.Draw(im).rounded_rectangle([0, 0, w * ss - 1, h * ss - 1], r * ss, fill=fill)
    return im.resize((w, h), Image.LANCZOS)

def ease(x): x = max(0.0, min(1.0, x)); return 1 - (1 - x) ** 3

def paste(base, im, x, y, alpha=1.0, scale=1.0):
    if alpha <= 0: return
    if scale != 1.0:
        nw, nh = max(1, int(im.width * scale)), max(1, int(im.height * scale)); x += (im.width - nw) // 2; y += (im.height - nh) // 2
        im = im.resize((nw, nh), Image.BILINEAR)
    if alpha < 1: im = im.copy(); im.putalpha(im.getchannel("A").point(lambda v: int(v * alpha)))
    base.alpha_composite(im, (int(x), int(y)))

# ---------- end card (same for every reel type) ----------
def end_card(s):
    im = Image.new("RGBA", (W, H), (250, 244, 228, 255)); d = ImageDraw.Draw(im)
    d.rectangle([0, 0, W, 26], fill=(204, 92, 52)); d.rectangle([0, H - 26, W, H], fill=(60, 150, 80))
    a = fit_block(s["end"], 72, (36, 44, 40), 960, 420); im.alpha_composite(a, (40, 500))
    kw, sub = s["cta"]
    pw = int(tlen(kw, 62)) + 110; pill = rrect(pw, 146, 73, (34, 139, 84, 255)); tdraw(ImageDraw.Draw(pill), 55, 96, kw, 62, (255, 255, 255))
    y = 500 + a.height + 50
    c = block(sub, 50, (70, 80, 76), maxw=900, wt=600); im.alpha_composite(c, (70, y + 146 + 40))
    tdraw(d, (W - tlen("@" + BRAND, 40, 600)) / 2, H - 120, "@" + BRAND, 40, (110, 120, 116), 600)
    return im, pill, ((W - pw) // 2, y)

# ---------- audio ----------
def load_wav(path):
    p = subprocess.run(["ffmpeg", "-v", "error", "-i", path, "-af", "silenceremove=stop_periods=-1:stop_duration=0.18:stop_threshold=-38dB,atempo=1.14,aecho=0.8:0.5:22:0.08,highpass=f=90,acompressor=threshold=-20dB:ratio=3:attack=5:release=60", "-f", "f32le", "-ac", "1", "-ar", str(SR), "-"], capture_output=True, check=True)
    v = np.frombuffer(p.stdout, np.float32).copy()
    nz = np.where(np.abs(v) > 0.01)[0]
    if len(nz): v = v[max(0, nz[0] - 600): nz[-1] + 2000]
    return v / (np.abs(v).max() + 1e-6) * 0.85

def wav_len(path): return len(load_wav(path)) / SR

class Mixer:
    def __init__(self, dur, seed=4):
        self.n = int((dur + 0.5) * SR); self.x = np.zeros(self.n, np.float32); self.rng = np.random.default_rng(seed)
    def add(self, t0, sig):
        s0 = int(t0 * SR); e = min(self.n, s0 + len(sig))
        if 0 <= s0 < self.n: self.x[s0:e] += sig[: e - s0]
    def room(self, level=0.06, murmur=0.035):
        n, rng = self.n, self.rng; tt = np.arange(n) / SR
        k = np.exp(-np.arange(400) / 60.0); k /= k.sum()
        self.x += (np.convolve(rng.standard_normal(n), k, "same") * level * (0.8 + 0.2 * np.sin(2 * np.pi * 0.07 * tt))).astype(np.float32)
        if murmur:
            k2 = np.exp(-np.arange(80) / 12.0); k2 /= k2.sum()
            m = np.convolve(rng.standard_normal(n), k2, "same") - np.convolve(rng.standard_normal(n), k, "same")
            self.x += (m * murmur * (0.6 + 0.4 * np.abs(np.sin(2 * np.pi * 2.3 * tt + np.sin(tt))))).astype(np.float32)
    def birds(self, dur, every=2.9, vol=0.035):
        for t0 in np.arange(0.7, dur, every):
            for j in range(self.rng.integers(2, 4)):
                L = int(SR * 0.07); f = 3200 + 1800 * np.sin(np.linspace(0, np.pi, L))
                self.add(t0 + j * 0.11 + self.rng.uniform(0, 0.4), (np.sin(2 * np.pi * np.cumsum(f) / SR) * np.hanning(L) * vol).astype(np.float32))
    def blip(self, t0, f=700, vol=0.2):
        u = np.arange(int(SR * 0.09)) / SR; self.add(t0, (np.sin(2 * np.pi * f * u) * np.exp(-u * 36) * vol).astype(np.float32))
    def save(self, path):
        f = SR; self.x[:f] *= np.linspace(0, 1, f); self.x[-f:] *= np.linspace(1, 0, f)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "f32le", "-ar", str(SR), "-ac", "1", "-i", "-", path], input=np.clip(self.x, -1, 1).tobytes(), check=True)

def encode(frame_fn, dur, wav, out):
    tmp, vid = out + ".tmp.mp4", out + ".video.mp4"
    ff = subprocess.Popen(["ffmpeg", "-v", "error", "-y", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-",
                           "-c:v", "libx264", "-crf", "20", "-preset", "veryfast", "-pix_fmt", "yuv420p", tmp], stdin=subprocess.PIPE)
    last_key, last = None, None
    for n in range(int(dur * FPS)):
        im, key = frame_fn(n / FPS)
        b = last if (key is not None and key == last_key) else im.convert("RGB").tobytes()
        last_key, last = key, b
        ff.stdin.write(b)
    ff.stdin.close()
    if ff.wait() != 0: raise RuntimeError("ffmpeg video failed")
    os.replace(tmp, vid)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", vid, "-i", wav, "-map", "0:v", "-map", "1:a", "-c:v", "copy", "-c:a", "aac", "-b:a", "160k",
                    "-shortest", "-movflags", "+faststart", out], check=True)
    os.remove(vid)

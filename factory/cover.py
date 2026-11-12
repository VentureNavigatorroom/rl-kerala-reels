"""Cover template: scene frame, dark gradient, big Malayalam hook, type badge, brand. Same look on every reel."""
import numpy as np
from PIL import Image, ImageDraw, ImageFilter
from common import *

BADGE = {"duo3d": ("ഒരു ചെറിയ കഥ", (204, 92, 52)), "chat": ("ചാറ്റ് സ്റ്റോറി", (47, 91, 234)), "list": ("ചെക്ക്‌ലിസ്റ്റ്", (34, 139, 84))}

def make(s, frame, out):
    im = frame.convert("RGBA").resize((W, H)).filter(ImageFilter.GaussianBlur(5 if s["kind"] == "duo3d" else 22))
    im.alpha_composite(Image.new("RGBA", (W, H), (8, 12, 22, 70 if s["kind"] == "duo3d" else 140)))
    g = np.linspace(0, 1, H)[:, None]
    a = (np.clip((g - 0.35) / 0.45, 0, 1) * 225).astype(np.uint8)
    shade = Image.fromarray(np.dstack([np.zeros((H, W, 3), np.uint8), np.repeat(a, W, axis=1)]), "RGBA")
    im.alpha_composite(shade)
    # hook sits in the centre-safe area (the grid crops covers to 3:4 around the middle)
    hb = fit_block(s["hook"], 96, (255, 222, 70), 940, 520, stroke=8, sfill=(20, 14, 8), lh=1.35)
    paste(im, hb, (W - hb.width) // 2, 1020 - hb.height // 2 + 120)
    label, col = BADGE[s["kind"]]
    bw = int(tlen(label, 44)) + 60; badge = rrect(bw, 82, 41, col + (255,)); tdraw(ImageDraw.Draw(badge), 30, 58, label, 44, (255, 255, 255))
    paste(im, badge, (W - bw) // 2, 660)
    d = ImageDraw.Draw(im); tdraw(d, (W - tlen("@" + BRAND, 38, 600)) / 2, H - 300, "@" + BRAND, 38, (235, 235, 235), 600)
    im.convert("RGB").save(out, quality=90)


def story(s, frame, out):
    """Story card announcing the new reel (Stories via API cannot carry link stickers, so it points to the profile)."""
    im = frame.convert("RGBA").resize((W, H)).filter(ImageFilter.GaussianBlur(18))
    im.alpha_composite(Image.new("RGBA", (W, H), (10, 14, 24, 170)))
    tag = "പുതിയ റീൽ"; tw = int(tlen(tag, 52)) + 70; pill = rrect(tw, 100, 50, (255, 196, 40, 255)); tdraw(ImageDraw.Draw(pill), 35, 70, tag, 52, (20, 24, 34))
    paste(im, pill, (W - tw) // 2, 520)
    hb = fit_block(s["hook"], 92, (255, 255, 255), 940, 560, stroke=6, sfill=(10, 10, 10), lh=1.35)
    paste(im, hb, (W - hb.width) // 2, 700)
    sub = block("പ്രൊഫൈലിൽ പോയി കാണൂ 👆\n" + s["cta"][0], 50, (255, 222, 70), maxw=940, wt=700)
    paste(im, sub, (W - sub.width) // 2, 700 + hb.height + 60)
    d = ImageDraw.Draw(im); tdraw(d, (W - tlen("@" + BRAND, 40, 600)) / 2, H - 260, "@" + BRAND, 40, (235, 235, 235), 600)
    im.convert("RGB").save(out, quality=88)


# ---------- standalone Stories (tip / quiz / answer / contact) ----------
STORY_BG = {"tip": (13, 27, 48), "quiz": (34, 110, 84), "answer": (34, 110, 84), "contact": (204, 92, 52)}
def story_card(t, out, part=None):
    kind = "answer" if part == "answer" else t["kind"]
    im = Image.new("RGBA", (W, H), STORY_BG[kind] + (255,)); d = ImageDraw.Draw(im)
    label = {"tip": "ഇന്നത്തെ ടിപ്പ്", "quiz": "ക്വിസ്", "answer": "ഉത്തരം", "contact": "ഞങ്ങളോട് ചോദിക്കൂ"}[kind]
    lw = int(tlen(label, 46)) + 60; pill = rrect(lw, 88, 44, (255, 222, 70, 255)); tdraw(ImageDraw.Draw(pill), 30, 62, label, 46, (20, 24, 34))
    paste(im, pill, (W - lw) // 2, 420)
    if kind == "tip":
        a = fit_block(t["title"], 84, (255, 255, 255), 940, 420); paste(im, a, (W - a.width) // 2, 580)
        b = fit_block(t["body"], 56, (220, 228, 240), 920, 520, wt=600); paste(im, b, (W - b.width) // 2, 620 + a.height)
        foot = "ഇതുപോലുള്ള ടിപ്സിന് ഫോളോ ചെയ്യൂ"
    elif kind == "quiz":
        a = fit_block(t["q"], 70, (255, 255, 255), 940, 820, lh=1.45); paste(im, a, (W - a.width) // 2, 580)
        foot = "ഉത്തരം അടുത്ത സ്റ്റോറിയിൽ. നിങ്ങളുടെ ഉത്തരം റിപ്ലൈ ചെയ്യൂ"
    elif kind == "answer":
        a = fit_block(t["a"], 88, (255, 222, 70), 940, 300); paste(im, a, (W - a.width) // 2, 600)
        b = fit_block(t["why"], 56, (235, 245, 238), 920, 500, wt=600); paste(im, b, (W - b.width) // 2, 640 + a.height)
        foot = "ഇതുപോലുള്ള ടിപ്സിന് ഫോളോ ചെയ്യൂ"
    else:
        a = fit_block(t["line"], 80, (255, 255, 255), 940, 520); paste(im, a, (W - a.width) // 2, 600)
        kw = f"{t['kw']} എന്ന് റിപ്ലൈ ചെയ്യൂ"; pw = int(tlen(kw, 56)) + 100
        p2 = rrect(pw, 136, 68, (255, 255, 255, 255)); tdraw(ImageDraw.Draw(p2), 50, 90, kw, 56, STORY_BG[kind])
        paste(im, p2, (W - pw) // 2, 680 + a.height); foot = "ഞങ്ങൾ മെസ്സേജിൽ മറുപടി തരും"
    fb = block(foot, 44, (255, 255, 255), maxw=900, wt=600); paste(im, fb, (W - fb.width) // 2, H - 560)
    tdraw(d, (W - tlen("@" + BRAND, 40, 600)) / 2, H - 300, "@" + BRAND, 40, (235, 235, 235), 600)
    im.convert("RGB").save(out, quality=88)

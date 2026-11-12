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

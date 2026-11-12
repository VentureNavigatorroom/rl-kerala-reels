"""Shrink a rendered location: opaque backgrounds -> JPEG, mouth overlays -> cropped PNG + offsets (ov.json)."""
import json, os, sys
from PIL import Image
d = sys.argv[1]; ov = {}
for f in sorted(os.listdir(d)):
    if not f.endswith(".png") or f.startswith("prev_"): continue
    p = f"{d}/{f}"; im = Image.open(p).convert("RGBA"); tag = f[:-4]
    if tag.endswith("_rest"):
        im.convert("RGB").save(f"{d}/{tag}.jpg", quality=93, subsampling=0); os.remove(p)
    elif tag.endswith(("_a", "_v")):
        bb = im.getchannel("A").getbbox()
        if bb: im.crop(bb).save(p, optimize=True); ov[tag] = bb[:2]
json.dump(ov, open(f"{d}/ov.json", "w"))
for f in os.listdir(d):
    if f.startswith("prev_"): os.remove(f"{d}/{f}")
print("packed", d, sum(os.path.getsize(f"{d}/{f}") for f in os.listdir(d)) // 1024, "KB")

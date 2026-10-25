#!/usr/bin/env python3
"""Crop/resize a generated image to the exact size the design needs.

Gemini ignores requested aspect ratios often enough that regenerating for ratio is a
waste of time — generate a good image, then fit it here.

Usage:
    python3 fit_image.py --image images/hero-home.jpg --size 1440x900
    python3 fit_image.py --image images/hero-home.jpg --size 1440x900 --gravity top

Keeps a `<name>-src.<ext>` backup on first run and always crops from that backup, so
re-running with a different --gravity never compounds the crop.
"""
import argparse
import os
import re
import shutil
import sys

try:
    from PIL import Image
except ImportError:
    print("Pillow required:  pip install Pillow", file=sys.stderr)
    raise SystemExit(2)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--image", required=True)
    ap.add_argument("--size", required=True, help="WxH, e.g. 1440x900")
    ap.add_argument("--gravity", default="center",
                    choices=["center", "top", "bottom", "left", "right"])
    ap.add_argument("--quality", type=int, default=92)
    args = ap.parse_args()

    m = re.match(r"^\s*(\d+)\s*[xX×]\s*(\d+)\s*$", args.size)
    if not m:
        print("--size must look like 1440x900", file=sys.stderr)
        return 1
    tw, th = int(m.group(1)), int(m.group(2))

    stem, ext = os.path.splitext(args.image)
    backup = f"{stem}-src{ext}"
    if not os.path.exists(backup):
        shutil.copy2(args.image, backup)

    im = Image.open(backup).convert("RGB")
    sw, sh = im.size

    # scale so the image covers the target box, then crop the overflow
    scale = max(tw / sw, th / sh)
    nw, nh = max(tw, int(round(sw * scale))), max(th, int(round(sh * scale)))
    im = im.resize((nw, nh), Image.LANCZOS)

    if args.gravity == "top":
        box = ((nw - tw) // 2, 0)
    elif args.gravity == "bottom":
        box = ((nw - tw) // 2, nh - th)
    elif args.gravity == "left":
        box = (0, (nh - th) // 2)
    elif args.gravity == "right":
        box = (nw - tw, (nh - th) // 2)
    else:
        box = ((nw - tw) // 2, (nh - th) // 2)

    im.crop((box[0], box[1], box[0] + tw, box[1] + th)).save(
        args.image, quality=args.quality, optimize=True
    )
    print(f"{args.image}: {sw}x{sh} -> {tw}x{th}  (gravity={args.gravity}, backup={backup})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

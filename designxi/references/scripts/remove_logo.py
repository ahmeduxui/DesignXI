#!/usr/bin/env python3
"""Remove the Gemini sparkle watermark from a generated image's bottom-right corner.

Gemini bakes a small light sparkle into the corner of every image it produces. It has
to come off before the image goes into a client deliverable, and cropping it away
costs real composition — so instead we patch the corner with pixels sampled from
directly above it and feather the seam. On the soft, low-detail corners these images
tend to have (a sleeve, a desk surface, a blurred background) the patch is invisible.

Usage:
    python3 remove_logo.py --image images/hero-freelancer.jpg
    python3 remove_logo.py --image images/x.jpg --box 0.90 0.78 1.00 0.94   # custom region
    python3 remove_logo.py --image images/x.jpg --check                     # detect only

Keeps a `<name>-logo.<ext>` backup of the untouched version on first run.
"""
import argparse
import os
import shutil
import sys

try:
    from PIL import Image, ImageFilter, ImageStat
except ImportError:
    print("Pillow required:  pip install Pillow", file=sys.stderr)
    raise SystemExit(2)

# Default corner box as fractions of width/height — where Gemini puts the sparkle.
DEFAULT_BOX = (0.905, 0.775, 1.0, 0.945)


def detect(im: Image.Image, box) -> str:
    """Report how visible the sparkle is — for information, not for gating.

    Detection is genuinely unreliable here and must not decide whether to patch.
    A sparkle on a dark background reads as a bright outlier within the corner; the
    same sparkle on a bright background (a white desk, a blown-out window) is white
    on white and produces almost no outlier, while a legitimately bright corner can
    look like an outlier when nothing is there. Since Gemini stamps every image at the
    same corner, patching unconditionally is more reliable than guessing — this
    function only tells the operator how obvious the mark was.
    """
    w, h = im.size
    x0, y0, x1, y1 = (int(box[0] * w), int(box[1] * h), int(box[2] * w), int(box[3] * h))
    patch = im.crop((x0, y0, x1, y1)).convert("L")
    px = sorted(patch.getdata())
    n = len(px)
    outlier = px[int(n * 0.99)] - px[n // 2]
    ph = y1 - y0
    above = im.crop((x0, max(0, y0 - ph), x1, y0)).convert("L")
    lift = ImageStat.Stat(patch).mean[0] - ImageStat.Stat(above).mean[0]
    if outlier > 40:
        return f"bright mark on dark corner (outlier {outlier})"
    if lift > 15:
        return f"light mark on bright corner (lift {lift:+.0f})"
    return f"faint or absent (outlier {outlier}, lift {lift:+.0f}) — patched anyway"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--image", required=True)
    ap.add_argument("--box", nargs=4, type=float, default=list(DEFAULT_BOX),
                    metavar=("X0", "Y0", "X1", "Y1"),
                    help="corner region as fractions of width/height")
    ap.add_argument("--check", action="store_true", help="report only, change nothing")
    ap.add_argument("--quality", type=int, default=92)
    args = ap.parse_args()

    im = Image.open(args.image).convert("RGB")
    w, h = im.size
    note = detect(im, args.box)

    if args.check:
        print(f"{args.image}: {note}")
        return 0

    stem, ext = os.path.splitext(args.image)
    backup = f"{stem}-logo{ext}"
    if not os.path.exists(backup):
        shutil.copy2(args.image, backup)

    x0, y0, x1, y1 = (int(args.box[0] * w), int(args.box[1] * h),
                      int(args.box[2] * w), int(args.box[3] * h))
    pw, ph = x1 - x0, y1 - y0

    # Source the replacement from directly above the sparkle, where the background
    # continues but the watermark does not.
    src_y0 = max(0, y0 - ph - 4)
    patch = im.crop((x0, src_y0, x1, src_y0 + ph)).resize((pw, ph))
    patch = patch.filter(ImageFilter.GaussianBlur(1.2))

    # Feather the seam so the patch edge doesn't read as a rectangle.
    mask = Image.new("L", (pw, ph), 255)
    mask = mask.filter(ImageFilter.GaussianBlur(max(3, pw // 12)))
    im.paste(patch, (x0, y0), mask)

    im.save(args.image, quality=args.quality, optimize=True)
    print(f"{args.image}: corner patched — {note}; backup at {backup}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

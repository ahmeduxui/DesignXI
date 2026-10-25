#!/usr/bin/env python3
"""Inline every local image in an HTML deliverable as a base64 data URI.

Figma (and anyone opening the file outside its folder) drops external `src` references,
so the delivery copy needs its images embedded. The linked original stays untouched and
editable — output goes to `<name>-embedded.html` unless --in-place is passed.

Usage:
    python3 embed_images.py --html screens.html
    python3 embed_images.py --html screens.html --in-place
"""
import argparse
import base64
import mimetypes
import os
import re
import sys
from urllib.parse import unquote

PATTERN = re.compile(r"""(src\s*=\s*|url\(\s*)(["']?)([^"')>\s]+)\2""", re.IGNORECASE)
SKIP_PREFIXES = ("data:", "http://", "https://", "//", "#")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--html", required=True)
    ap.add_argument("--in-place", action="store_true")
    args = ap.parse_args()

    base = os.path.dirname(os.path.abspath(args.html))
    with open(args.html, encoding="utf-8") as f:
        html = f.read()

    embedded, missing, skipped_big = [], [], []

    def repl(m):
        prefix, quote, ref = m.group(1), m.group(2), m.group(3)
        if ref.lower().startswith(SKIP_PREFIXES):
            return m.group(0)
        path = os.path.join(base, unquote(ref))
        if not os.path.isfile(path):
            missing.append(ref)
            return m.group(0)
        size = os.path.getsize(path)
        if size > 12 * 1024 * 1024:
            skipped_big.append((ref, size))
            return m.group(0)
        mime = mimetypes.guess_type(path)[0] or "application/octet-stream"
        if not (mime.startswith("image/") or mime == "image/svg+xml"):
            return m.group(0)
        with open(path, "rb") as fh:
            b64 = base64.b64encode(fh.read()).decode("ascii")
        embedded.append(ref)
        return f"{prefix}{quote}data:{mime};base64,{b64}{quote}"

    out_html = PATTERN.sub(repl, html)

    out_path = args.html if args.in_place else (
        os.path.splitext(args.html)[0] + "-embedded.html"
    )
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(out_html)

    print(f"wrote {out_path}")
    print(f"  embedded : {len(embedded)}")
    for ref in embedded:
        print(f"      + {ref}")
    if missing:
        print(f"  MISSING  : {len(missing)}  (left as-is — they will not render)", file=sys.stderr)
        for ref in missing:
            print(f"      ! {ref}", file=sys.stderr)
    if skipped_big:
        print(f"  too large: {len(skipped_big)} (>12MB, left linked)", file=sys.stderr)
    return 1 if missing else 0


if __name__ == "__main__":
    raise SystemExit(main())

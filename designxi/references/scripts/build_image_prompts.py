#!/usr/bin/env python3
"""Build the Gemini prompt sheet + on-brand placeholders from an images.json manifest.

Usage:
    python3 build_image_prompts.py --manifest images.json --outdir .

Outputs:
    <outdir>/صور-البرومبتات.md   one copy-ready prompt per image, with where it goes
    <outdir>/images/*.svg        on-brand labeled placeholders so the HTML renders now
    stdout                        a compact table to paste into chat

The manifest is described in references/ai-imagery.md. Only `id`, `file`, `size` and
`subject` are strictly required per image; everything else degrades gracefully.
"""
import argparse
import json
import os
import re
import sys

# Phase 6 design school -> photographic direction (mirrors the table in ai-imagery.md)
STYLE_LOOKUP = {
    "minimalism": "clean negative space, single subject, soft even light, muted palette",
    "swiss": "clean negative space, strict composition, soft even light, muted palette",
    "flat": "bright flat lighting, simple shapes, high-key, low shadow contrast",
    "glassmorphism": "soft gradient light, bokeh, translucent layers, atmospheric haze",
    "aurora": "soft gradient light, bokeh, translucent layers, atmospheric haze",
    "organic": "natural light, plant/wood/stone texture, golden hour, gentle film grain",
    "biophilic": "natural light, plant/wood/stone texture, golden hour, gentle film grain",
    "brutalism": "hard flash lighting, raw concrete, high contrast, unpolished",
    "cyberpunk": "neon rim light, deep shadow, wet reflective surfaces, night",
    "dark mode": "neon rim light, deep shadow, moody low-key lighting, night",
    "editorial": "fashion-editorial lighting, styled composition, shallow depth of field",
    "magazine": "fashion-editorial lighting, styled composition, shallow depth of field",
    "skeuomorphism": "real material macro detail — leather, brushed metal, tactile surfaces",
    "claymorphism": "soft studio light, rounded tactile forms, pastel depth",
    "material": "clean product photography, even light, confident color blocking",
}

COMPOSITION = {
    "hero": "keep the left third calm and uncluttered so a headline and CTA can sit there",
    "persona": "centered head-and-shoulders, neutral uncluttered background, eye contact with camera",
    "content": "subject centered with breathing room on all sides, nothing cropped at the edges",
    "mockup": "leave the device screen blank white with no interface, generous empty space around it",
}

EXTRA = {
    "persona": "Documentary portrait, not a stock-photo smile. Natural light, real skin texture.",
    "mockup": "The screen must be empty — the real interface is composited on top afterwards.",
}


def ratio_for(size: str) -> str:
    m = re.match(r"^\s*(\d+)\s*[xX×]\s*(\d+)\s*$", size or "")
    if not m:
        return "16:9 landscape"
    w, h = int(m.group(1)), int(m.group(2))
    r = w / h if h else 1
    if abs(r - 1) < 0.06:
        return "1:1 square"
    if r > 1.5:
        return "16:9 landscape"
    if r > 1.05:
        return "4:3 landscape"
    if r > 0.9:
        return "1:1 square"
    if r > 0.7:
        return "4:5 portrait"
    return "9:16 vertical portrait"


def style_line(style: str) -> str:
    s = (style or "").lower()
    for key, val in STYLE_LOOKUP.items():
        if key in s:
            return val
    return "premium editorial photography, coherent lighting, restrained palette"


def build_prompt(img: dict, manifest: dict) -> str:
    pal = manifest.get("palette", {}) or {}
    primary = pal.get("primary", "#1A1A1A")
    accent = pal.get("accent", primary)
    bg = pal.get("bg", "#FFFFFF")
    itype = (img.get("type") or "content").lower()

    lines = [
        f"Generate an image, {ratio_for(img.get('size', ''))}.",
        img.get("subject", "").strip() or "(describe the subject here)",
        f"Visual style: {style_line(manifest.get('style', ''))}.",
        f"Color: dominant {primary} with {accent} accents, on {bg} tones.",
        f"Composition: {COMPOSITION.get(itype, COMPOSITION['content'])}.",
    ]
    if itype in EXTRA:
        lines.append(EXTRA[itype])
    lines.append(
        "Premium editorial quality, high detail, no text, no watermarks, no UI elements."
    )
    return "\n".join(lines)


PLACEHOLDER_SVG = """<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-label="{alt}">
  <defs>
    <linearGradient id="g" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="{bg}"/>
      <stop offset="100%" stop-color="{primary}"/>
    </linearGradient>
  </defs>
  <rect width="{w}" height="{h}" fill="url(#g)"/>
  <rect x="1" y="1" width="{w2}" height="{h2}" fill="none" stroke="{accent}" stroke-opacity="0.55" stroke-dasharray="10 8"/>
  <circle cx="{cx}" cy="{cy1}" r="{r}" fill="{accent}" fill-opacity="0.25"/>
  <text x="{cx}" y="{cy2}" text-anchor="middle" font-family="system-ui, sans-serif" font-size="{fs}" fill="{accent}" fill-opacity="0.9">{label}</text>
  <text x="{cx}" y="{cy3}" text-anchor="middle" font-family="system-ui, sans-serif" font-size="{fs2}" fill="{accent}" fill-opacity="0.6">AI placeholder — see صور-البرومبتات.md</text>
</svg>
"""


def write_placeholder(path: str, img: dict, manifest: dict) -> str:
    """Write an on-brand labeled placeholder AT THE EXACT PATH the HTML references.

    Raster (png/jpg) is written with Pillow when available, so `src="images/hero.jpg"`
    renders immediately and the real Gemini image simply overwrites it later — no HTML
    edit needed. Without Pillow we fall back to an SVG beside it and say so.
    """
    m = re.match(r"^\s*(\d+)\s*[xX×]\s*(\d+)\s*$", img.get("size", "") or "")
    w, h = (int(m.group(1)), int(m.group(2))) if m else (1440, 900)
    pal = manifest.get("palette", {}) or {}
    ext = os.path.splitext(path)[1].lower()
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)

    if ext in (".jpg", ".jpeg", ".png", ".webp"):
        try:
            return _write_raster_placeholder(path, w, h, pal, img)
        except Exception:
            path = os.path.splitext(path)[0] + ".svg"

    return _write_svg_placeholder(os.path.splitext(path)[0] + ".svg", w, h, pal, img)


FONT_CANDIDATES = [
    "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
    "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf",
    "/System/Library/Fonts/Supplemental/Arial.ttf",
    "/Library/Fonts/Arial.ttf",
    "C:/Windows/Fonts/arial.ttf",
]


def _font(size: int):
    """A scalable font so the label stays readable on a 1600px placeholder.

    Pillow's built-in bitmap font is fixed at ~11px, which is invisible on large
    images — the placeholder then reads as an empty gradient instead of a labeled gap.
    """
    from PIL import ImageFont

    for path in FONT_CANDIDATES:
        if os.path.exists(path):
            try:
                return ImageFont.truetype(path, size)
            except Exception:
                continue
    return ImageFont.load_default()


def _write_raster_placeholder(path, w, h, pal, img) -> str:
    from PIL import Image, ImageDraw

    bg = pal.get("bg", "#EEEEEE")
    primary = pal.get("primary", "#999999")
    accent = pal.get("accent", "#FFFFFF")

    base = Image.new("RGB", (w, h), bg)
    top, bot = Image.new("RGB", (1, 1), bg).getpixel((0, 0)), Image.new("RGB", (1, 1), primary).getpixel((0, 0))
    grad = Image.new("RGB", (1, h))
    for y in range(h):
        t = y / max(1, h - 1)
        grad.putpixel((0, y), tuple(int(top[i] + (bot[i] - top[i]) * t) for i in range(3)))
    base = grad.resize((w, h))

    d = ImageDraw.Draw(base)
    d.rectangle([4, 4, w - 5, h - 5], outline=accent, width=max(2, min(w, h) // 300))
    r = max(18, min(w, h) // 12)
    cx, cy = w // 2, int(h * 0.42)
    d.ellipse([cx - r, cy - r, cx + r, cy + r], outline=accent, width=max(2, r // 12))

    label = img.get("id", "image")
    # ASCII only — Pillow's default bitmap font renders Arabic as tofu boxes
    note = "AI placeholder - see the prompts file"
    fs = max(14, min(w, h) // 16)
    f_label, f_note = _font(fs), _font(max(11, int(fs * 0.5)))
    d.text((cx, int(h * 0.60)), label, fill=accent, anchor="mm", font=f_label)
    d.text((cx, int(h * 0.60) + int(fs * 1.5)), note, fill=accent, anchor="mm", font=f_note)

    if path.lower().endswith((".jpg", ".jpeg")):
        base.save(path, quality=88, optimize=True)
    else:
        base.save(path)
    return path


def _write_svg_placeholder(path, w, h, pal, img) -> str:
    fs = max(16, min(w, h) // 18)
    svg = PLACEHOLDER_SVG.format(
        w=w, h=h, w2=w - 2, h2=h - 2,
        cx=w // 2, cy1=int(h * 0.42), cy2=int(h * 0.58), cy3=int(h * 0.58) + int(fs * 1.6),
        r=max(18, min(w, h) // 12),
        fs=fs, fs2=max(12, int(fs * 0.55)),
        bg=pal.get("bg", "#EEEEEE"),
        primary=pal.get("primary", "#999999"),
        accent=pal.get("accent", "#FFFFFF"),
        label=img.get("id", "image"),
        alt=(img.get("subject", "") or img.get("id", "image"))[:120],
    )
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(svg)
    return path


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--manifest", required=True)
    ap.add_argument("--outdir", default=".")
    ap.add_argument("--no-placeholders", action="store_true")
    args = ap.parse_args()

    with open(args.manifest, encoding="utf-8") as f:
        manifest = json.load(f)

    images = manifest.get("images", [])
    if not images:
        print("manifest has no images", file=sys.stderr)
        return 1

    os.makedirs(args.outdir, exist_ok=True)
    md = [
        f"# برومبتات الصور — {manifest.get('project', 'Project')}",
        "",
        f"**Design style:** {manifest.get('style', '—')}  ",
        f"**Palette:** {json.dumps(manifest.get('palette', {}), ensure_ascii=False)}",
        "",
        "انسخ البرومبت وألصقه في Gemini، ثم نزّل الصورة واحفظها بنفس اسم الملف المكتوب تحتها.",
        "",
        "| # | الملف | مكانها في التصميم | المقاس |",
        "|---|---|---|---|",
    ]
    for i, img in enumerate(images, 1):
        md.append(
            f"| {i} | `{img.get('file','')}` | {img.get('where','—')} | {img.get('size','—')} |"
        )
    md.append("")
    md.append("---")
    md.append("")

    rows, written = [], []
    for i, img in enumerate(images, 1):
        prompt = build_prompt(img, manifest)
        md += [
            f"## {i}. {img.get('id','image')}",
            "",
            f"- **الملف:** `{img.get('file','')}`",
            f"- **المكان:** {img.get('where','—')}",
            f"- **المقاس:** {img.get('size','—')}  ·  **النوع:** {img.get('type','content')}",
            "",
            "```",
            prompt,
            "```",
            "",
        ]
        rows.append((img.get("file", ""), img.get("where", ""), img.get("size", "")))

        if not args.no_placeholders:
            target = os.path.join(args.outdir, img.get("file", f"images/{img.get('id','img')}.jpg"))
            written.append(write_placeholder(target, img, manifest))

    out_md = os.path.join(args.outdir, "صور-البرومبتات.md")
    with open(out_md, "w", encoding="utf-8") as f:
        f.write("\n".join(md))

    print(f"wrote {out_md}  ({len(images)} prompts)")
    if written:
        print(f"wrote {len(written)} placeholders at their exact target paths "
              f"— the real images just overwrite them, no HTML edit needed")
        odd = [p for p in written if p.endswith(".svg")]
        if odd:
            print("  NOTE: these fell back to SVG — point the HTML at the .svg for now:",
                  file=sys.stderr)
            for p in odd:
                print(f"      {p}", file=sys.stderr)
    print()
    for fpath, where, size in rows:
        print(f"  {fpath:<34} {size:<12} {where}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

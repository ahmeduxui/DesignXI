#!/usr/bin/env python3
"""
Pixel-perfect device mockup compositor — no AI, no regeneration.

Places the user's exact screenshot inside a procedurally-drawn device frame
(phone / laptop / browser window) on a solid or gradient background. Every
pixel of the original screenshot is preserved untouched (only resized to fit
the frame's screen area, never redrawn or reinterpreted).

Usage:
    python3 composite_mockup.py --image screenshot.png --frame phone \
        --bg-color1 "#EEF0FF" --bg-color2 "#FFFFFF" --out mockup.png

    python3 composite_mockup.py --image screenshot.png --frame laptop \
        --bg-color1 "#111827" --out mockup.png

    python3 composite_mockup.py --image screenshot.png --frame browser \
        --bg-color1 "#F5F5F7" --out mockup.png

Frames: phone, laptop, browser
"""

import argparse
from PIL import Image, ImageDraw, ImageFilter, ImageOps


def hex_to_rgb(h):
    h = h.lstrip("#")
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))


def make_gradient_bg(size, color1, color2=None):
    w, h = size
    if color2 is None:
        return Image.new("RGB", size, color1)
    base = Image.new("RGB", (w, h), color1)
    top = Image.new("RGB", (w, h), color2)
    mask = Image.new("L", (w, h))
    mask_data = []
    for y in range(h):
        mask_data.extend([int(255 * (y / h))] * w)
    mask.putdata(mask_data)
    base.paste(top, (0, 0), mask)
    return base


def rounded_mask(size, radius):
    mask = Image.new("L", size, 0)
    draw = ImageDraw.Draw(mask)
    draw.rounded_rectangle([(0, 0), (size[0] - 1, size[1] - 1)], radius=radius, fill=255)
    return mask


def fit_cover(img, target_size):
    """Resize+crop img to exactly fill target_size (cover), no distortion."""
    return ImageOps.fit(img, target_size, method=Image.LANCZOS)


def add_shadow(canvas, box, blur=40, opacity=90, offset=(0, 20)):
    shadow_layer = Image.new("RGBA", canvas.size, (0, 0, 0, 0))
    sd = ImageDraw.Draw(shadow_layer)
    x0, y0, x1, y1 = box
    sd.rounded_rectangle(
        [x0 + offset[0], y0 + offset[1], x1 + offset[0], y1 + offset[1]],
        radius=40, fill=(0, 0, 0, opacity)
    )
    shadow_layer = shadow_layer.filter(ImageFilter.GaussianBlur(blur))
    canvas.paste(shadow_layer, (0, 0), shadow_layer)


def build_phone_frame(screenshot, out_size=(1200, 1500)):
    canvas_w, canvas_h = out_size
    frame_w = int(canvas_w * 0.5)
    frame_h = int(frame_w * 2.05)
    bezel = int(frame_w * 0.035)
    corner_r = int(frame_w * 0.13)

    screen_w = frame_w - 2 * bezel
    screen_h = frame_h - 2 * bezel
    screen = fit_cover(screenshot, (screen_w, screen_h))

    frame_x = (canvas_w - frame_w) // 2
    frame_y = (canvas_h - frame_h) // 2

    canvas = Image.new("RGBA", out_size, (0, 0, 0, 0))
    add_shadow(canvas, (frame_x, frame_y, frame_x + frame_w, frame_y + frame_h), blur=50, opacity=70)

    body = Image.new("RGBA", (frame_w, frame_h), (20, 20, 24, 255))
    body_mask = rounded_mask((frame_w, frame_h), corner_r)
    body.putalpha(body_mask)
    canvas.paste(body, (frame_x, frame_y), body)

    screen_mask = rounded_mask((screen_w, screen_h), max(corner_r - bezel, 8))
    screen_rgba = screen.convert("RGBA")
    screen_rgba.putalpha(screen_mask)
    canvas.paste(screen_rgba, (frame_x + bezel, frame_y + bezel), screen_rgba)

    draw = ImageDraw.Draw(canvas)
    notch_w = int(frame_w * 0.34)
    notch_h = int(frame_w * 0.065)
    notch_x = frame_x + (frame_w - notch_w) // 2
    notch_y = frame_y + int(bezel * 0.6)
    draw.rounded_rectangle(
        [notch_x, notch_y, notch_x + notch_w, notch_y + notch_h],
        radius=notch_h // 2, fill=(10, 10, 12, 255)
    )
    return canvas


def build_laptop_frame(screenshot, out_size=(1600, 1000)):
    canvas_w, canvas_h = out_size
    screen_w = int(canvas_w * 0.72)
    screen_h = int(screen_w * 0.6)
    bezel = int(screen_w * 0.015)
    corner_r = int(screen_w * 0.02)

    screen_x = (canvas_w - screen_w) // 2
    screen_y = int(canvas_h * 0.08)

    canvas = Image.new("RGBA", out_size, (0, 0, 0, 0))
    add_shadow(canvas, (screen_x, screen_y, screen_x + screen_w, screen_y + screen_h + int(screen_h * 0.05)),
               blur=60, opacity=60)

    body_w = screen_w + 2 * bezel
    body_h = screen_h + 2 * bezel + int(screen_h * 0.04)
    body_x = screen_x - bezel
    body_y = screen_y - bezel
    body = Image.new("RGBA", (body_w, body_h), (28, 28, 30, 255))
    body_mask = rounded_mask((body_w, body_h), corner_r)
    body.putalpha(body_mask)
    canvas.paste(body, (body_x, body_y), body)

    screen = fit_cover(screenshot, (screen_w, screen_h))
    screen_mask = rounded_mask((screen_w, screen_h), max(corner_r - bezel, 4))
    screen_rgba = screen.convert("RGBA")
    screen_rgba.putalpha(screen_mask)
    canvas.paste(screen_rgba, (screen_x, screen_y), screen_rgba)

    base_y = body_y + body_h
    base_h = int(screen_h * 0.05)
    base_w = int(body_w * 1.12)
    base_x = (canvas_w - base_w) // 2
    draw = ImageDraw.Draw(canvas)
    draw.rounded_rectangle(
        [base_x, base_y, base_x + base_w, base_y + base_h],
        radius=base_h // 2, fill=(40, 40, 42, 255)
    )
    return canvas


def build_browser_frame(screenshot, out_size=(1600, 1100)):
    canvas_w, canvas_h = out_size
    frame_w = int(canvas_w * 0.82)
    frame_h = int(frame_w * 0.68)
    frame_x = (canvas_w - frame_w) // 2
    frame_y = int((canvas_h - frame_h) // 2)
    corner_r = int(frame_w * 0.015)
    top_bar_h = int(frame_h * 0.09)

    canvas = Image.new("RGBA", out_size, (0, 0, 0, 0))
    add_shadow(canvas, (frame_x, frame_y, frame_x + frame_w, frame_y + frame_h), blur=55, opacity=65)

    body = Image.new("RGBA", (frame_w, frame_h), (255, 255, 255, 255))
    body_mask = rounded_mask((frame_w, frame_h), corner_r)
    body.putalpha(body_mask)
    canvas.paste(body, (frame_x, frame_y), body)

    draw = ImageDraw.Draw(canvas)
    draw.rounded_rectangle(
        [frame_x, frame_y, frame_x + frame_w, frame_y + top_bar_h],
        radius=corner_r, fill=(238, 238, 240, 255)
    )
    draw.rectangle([frame_x, frame_y + top_bar_h - corner_r, frame_x + frame_w, frame_y + top_bar_h],
                    fill=(238, 238, 240, 255))

    dot_r = int(top_bar_h * 0.14)
    dot_y = frame_y + top_bar_h // 2
    colors = [(237, 106, 94), (245, 191, 79), (97, 197, 80)]
    for i, c in enumerate(colors):
        cx = frame_x + int(frame_w * 0.025) + i * (dot_r * 3)
        draw.ellipse([cx - dot_r, dot_y - dot_r, cx + dot_r, dot_y + dot_r], fill=c)

    screen_w = frame_w
    screen_h = frame_h - top_bar_h
    screen = fit_cover(screenshot, (screen_w, screen_h))
    screen_mask = rounded_mask((screen_w, screen_h), 4)
    screen_rgba = screen.convert("RGBA")
    screen_rgba.putalpha(screen_mask)
    canvas.paste(screen_rgba, (frame_x, frame_y + top_bar_h), screen_rgba)
    return canvas


FRAME_BUILDERS = {
    "phone": build_phone_frame,
    "laptop": build_laptop_frame,
    "browser": build_browser_frame,
}


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--image", required=True, help="Path to the exact screenshot to place in the frame")
    p.add_argument("--frame", required=True, choices=list(FRAME_BUILDERS.keys()))
    p.add_argument("--bg-color1", default="#F1F2F6", help="Background color (hex), or gradient start")
    p.add_argument("--bg-color2", default=None, help="Optional gradient end color (hex)")
    p.add_argument("--out", required=True, help="Output PNG path")
    p.add_argument("--canvas-size", default=None, help="WxH override, e.g. 1600x1200")
    args = p.parse_args()

    screenshot = Image.open(args.image).convert("RGB")

    builder = FRAME_BUILDERS[args.frame]
    default_sizes = {"phone": (1200, 1500), "laptop": (1600, 1000), "browser": (1600, 1100)}
    size = default_sizes[args.frame]
    if args.canvas_size:
        w, h = args.canvas_size.lower().split("x")
        size = (int(w), int(h))

    frame_layer = builder(screenshot, out_size=size)

    bg_color1 = hex_to_rgb(args.bg_color1)
    bg_color2 = hex_to_rgb(args.bg_color2) if args.bg_color2 else None
    bg = make_gradient_bg(size, bg_color1, bg_color2).convert("RGBA")

    bg.paste(frame_layer, (0, 0), frame_layer)
    bg.convert("RGB").save(args.out, "PNG")
    print(f"Saved: {args.out} ({size[0]}x{size[1]})")


if __name__ == "__main__":
    main()

# Screen Mockups — presenting finished screens in device frames

For the delivery package (Phase 24) and the case study, don't show a bare screenshot. Place each key
screen inside a clean device frame — phone, laptop, or browser — so the portfolio piece looks
presented, not pasted. Two paths, pick by what matters:

1. **Exact / pixel-perfect frame (default).** `references/scripts/composite_mockup.py` draws the device
   frame procedurally and drops the real screen inside it — **no AI, no regeneration, every pixel of
   the design preserved** (only resized to fit). Use this whenever the screen must stay exactly as
   designed (fonts, spacing, icons). For a designer's own portfolio this is almost always the right
   path.
2. **Creative AI scene (optional).** A Gemini prompt that places the screen in a photographic scene
   (a hand holding the phone, a styled desk). Gemini **regenerates** the image, so small drift in type
   and spacing is expected even with a reference attached. This overlaps with Phase 15A — reuse the
   `ai-imagery.md` pipeline (prompt sheet + Gemini-in-Chrome) for it. Only use when the user wants a
   lifestyle/photographic feel and can accept close-but-not-identical.

**Never let the user think the AI scene preserves the screen exactly.** When a screen is available and
the user hasn't said which they want, default to the exact frame and offer the AI scene as the more
photographic alternative — don't silently pick the one that changes their design.

---

## The flow (exact frame)

A DesignXI screen is HTML, and the compositor needs a **PNG of the rendered screen**. So:

1. **Render the screen HTML to a PNG.** Any of these works:
   - the artifact/file-preview screenshot tool on the screen file, or
   - a Chrome screenshot of the rendered page (Claude-in-Chrome), or
   - a headless render (`weasyprint` / a browser) if available in the session.
   Save it as `images/<screen>-shot.png`.
2. **Frame it with the compositor**, picking the frame from the platform and the background from the
   project's Phase 12 palette (a light tint of the brand color, or white / near-black to match the
   design's own background — never a random color):
   ```bash
   python3 references/scripts/composite_mockup.py \
     --image images/home-shot.png \
     --frame browser \
     --bg-color1 "#FBF9F6" --bg-color2 "#EDE7DE" \
     --out mockups/home-mockup.png
   ```
   - `--frame phone` for mobile screens · `laptop` for dashboards/desktop apps · `browser` for
     websites and landing pages.
   - `--bg-color2` is optional — omit for a solid background, pass it for a soft top-to-bottom
     gradient.
   - `--canvas-size WxH` overrides the output size if a specific ratio is needed.
3. **Use the framed PNGs** as the case-study hero and the `index.html` cover, and alongside the raw
   screens in the delivery package. Run the compositor once per screen/frame and present them together.

Only Pillow is required — no extra dependencies.

---

## Rules carried from the mockup discipline
- **No real device brand names** anywhere (no "iPhone 15", "MacBook Pro") — the frames are generic by
  design; keep any captions generic too ("a modern laptop", "a smartphone").
- **Real hex, not color names** — pull the background and any prompt colors from the Phase 12 tokens or
  the screenshot, never guess "blue".
- **The exact frame is deterministic** — just run it and show the result; no approval gate, it never
  alters the design.
- **A multi-screen board needs multiple screenshots** — render each screen first, then frame them, then
  compose the board (or arrange the framed PNGs in the case-study layout).

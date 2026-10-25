# Self-contained HTML deliverable — any surface, one file that opens in the browser

Output format 1 of Phase 24. The deliverable is a **single self-contained `.html` file** that opens by
double-click in any browser with no server, no build, no internet — with **the fonts, icons, and images
embedded inside it**. What the file *contains* depends on what the user asked for: a landing page, a
dashboard, a set of mobile screens, or the whole platform. Match the ask — don't always build the full
product.

## Step A — Ask the scope first (AskUserQuestion)

Before building, ask what to design and how. Keep it to the choices that change the output:

1. **What surface?** (pick one or more)
   - **Landing page** — the full marketing page, hero → sections → footer, one scroll.
   - **Dashboard** — the app's data screen(s): KPIs, charts, tables, filters.
   - **Mobile screens** — the phone UI (a flow or a key set of screens), phone-framed.
   - **Full platform** — every screen with real navigation between them (the biggest option).
   - **Other / specific screen** — whatever the user names (pricing page, settings, onboarding…).
2. **Responsive?** — yes (works 375 → 1440, mobile + desktop layouts) or a single target width
   (e.g. desktop-only landing, or mobile-only app). Don't assume; ask.
3. If not already decided earlier: **dark mode?** (light / dark / both) and, for Arabic, **RTL** is on by
   the user's default.

Then build exactly that surface as one embedded HTML. If they picked several surfaces, either one file with
a simple switcher or one file each — ask which they prefer.

## Step B — The one rule: everything is inline (offline-proof)

The file must render opened straight from disk (`file://`), network off:
- **CSS** — all in one `<style>` in `<head>`; Phase 12 tokens as `:root` custom properties.
- **JavaScript** — all in one `<script>` at the end of `<body>`; no web imports.
- **Fonts** — the Phase 12 fonts **embedded** (base64 `@font-face`), or a named system-font fallback stack
  if embedding is too heavy — never a Google Fonts `<link>` that dies offline and silently falls back.
- **Images** — every image embedded as a `data:` URL (base64) from Phase 15A; run
  `references/scripts/embed_images.py` on the file so nothing is left as an external path.
- **Icons** — inline SVG (the Phase 12 icon set as `<svg>`), not an icon-font CDN.

If any asset loads from the web, the file is not done.

## Per-surface notes

- **Landing page** — one page, real sections and copy, conversion architecture (Phase 15 landing
  checklist), hero image embedded. Responsive unless the user said desktop-only. Smooth-scroll nav, a
  sticky header if it fits the design.
- **Dashboard** — real KPI cards, charts (Chart.js is allowed from CDN *only* if the user accepts an online
  dependency; otherwise inline a lightweight chart or pre-render as SVG so it stays offline), tables with
  worst-case-aware data (`references/stress-test.md`), filters that actually work in JS. Ask whether it
  needs to be responsive — dashboards are often desktop-first.
- **Mobile screens** — phone viewport, the web-on-mobile fixes from `references/motion-and-polish.md` §4
  (`100dvh`, 16px inputs, `touch-action`, safe-area), optionally framed in a phone bezel.
- **Full platform** — every screen as a `<section data-screen>`, one visible at a time, a tiny
  `showScreen(id)` router, all four flows (happy / error / empty / onboarding) reachable, navigation that
  works or is honestly disabled. State in JS memory, not `localStorage` (which may be empty/blocked on
  `file://`; use it only for optional remembered toggles, wrapped in try/catch).

## Quality bar (every surface, not a lite version)
Tokens only · 8pt grid · one icon set · no emojis · the Phase 11 design school consistent · responsive per
the scope answer · motion passes the gate and 10-block review with a `prefers-reduced-motion` block
(`references/motion-and-polish.md`) · RTL mirrored for Arabic with Latin digits inside Arabic
(`references/rtl-arabic.md`) · WCAG AA contrast, visible focus, keyboard nav, 48px targets · real content,
humanized copy (`references/humanize-copy.md`), no lorem ipsum.

## Build order
1. Do the relevant design phases for the chosen surface (system/tokens from 11–12, the surface's screens
   from 14–15, responsive 16 if asked, self-critique 17, motion 18). For a quick single-surface request the
   user can skip the heavy research phases — confirm the tokens and design school, then design.
2. Run **Phase 15A** for every image the surface shows; embed them base64.
3. Assemble one `.html`: `<style>` tokens + components, the surface markup (or the `<section>`+router for a
   full platform), inline `<script>`, inline SVG icons, embedded fonts.
4. Run `references/scripts/embed_images.py` to inline any remaining image paths.
5. **Verify offline**: open from disk with the network off; screenshot it (the file-preview screenshot
   tool) to confirm layout before delivering.
6. Save to the workspace folder and present it. Since it's a reusable HTML the user will reopen, offer to
   persist it as an artifact with a stable URL — ask first; never publish a client's work unprompted.

## What it is not
- Not a framework codebase (React/Vue + build) — that's output format 3 (dev assets).
- Not the separate deliverable docs (casestudy / personas / handoff) — that's output format 2.

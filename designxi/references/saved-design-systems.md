# Saved Design Systems — your reusable library

Design systems kept ready to reuse. When a new project **is** going to be built on one of these,
do not invent a style or a palette from scratch — apply the saved system's tokens directly.

Used at three points in the process:
- **Phase 10 (Visual References & Inspiration)** — if a saved system fits, it's the primary reference.
- **Phase 11 Step 0 (Design-System Selector)** — this file is the source for the selector menu. Phase 11
  reads it and builds one AskUserQuestion option per system below (in order), plus a "fresh style"
  option. Keeping this file current = keeping the selector current; the menu is never hardcoded in
  SKILL.md.
- **Phase 12 (Identity & Icons)** — when a system is chosen, apply its tokens from here (or its own
  file / Figma) instead of defining fresh ones.

A system marked ✅ **complete** has all its tokens written out (in its own file) and can be applied as-is.
A system marked 🔶 has only partial tokens here — resolve the rest from its Figma file or by asking the user,
before use. Never guess a missing hex or font. **Pulling from Figma is notify-first**: before reading any
Figma file, tell the user which file and what you'll pull, and wait for a yes — see `references/figma-tokens.md`.

---

## 1. Untitled UI ✅ complete — the default UI kit

The full Untitled UI design system. **When a project should look like a clean, modern product UI and has
no brand of its own, this is the default.**

- **Read**: `references/design-systems/untitled-ui.md` — the complete reference (263 color styles, Inter
  type scale, 4px spacing, every component's sizes/paddings/states, icons, radius, shadows, PRO showcase
  lessons).
- **At a glance**: gray + purple-primary palette (primary 600 `#7f56d9`), **Inter**, 4px grid, radius 8
  (12 modals, full pills), Feather-style 24px line icons, 7-step shadow scale.
- **Use for**: SaaS, dashboards, admin, web apps, any product UI wanting a polished neutral baseline.
- **Font exception**: Inter is correct here — this overrides the skill's "no Inter as hero font" rule;
  do not flag it. For Arabic/RTL, keep the Untitled UI structure but swap Inter for an Arabic face and
  apply `references/rtl-arabic.md`.
- **Source**: Figma free community file `jl2IXuNW1VUXjqUn4PeNvp` (12 pages) + PRO v8 showcase.

---

## 2. Salla ✅ complete — Arabic e-commerce store themes

The Salla merchant store-theme design system. **When a project is a Salla storefront theme — or an
Arabic RTL online store wanting the Salla look — this is the system.**

- **Read**: `references/design-systems/salla.md` — the complete reference (mint + neutral palette, DIN
  Next LT Arabic type scale, 8px spacing, 1600/12-col grid, radius 4 default, every component, and the
  required page templates).
- **At a glance**: mint primary `#62d0b6`, text `#333333`/`#666666`, **DIN Next LT Arabic**, radius 4,
  one soft shadow, 12-col 1600 grid (content 1200). RTL-native.
- **Use for**: Salla themes, Arabic RTL e-commerce (home / product / collection / cart / etc.).
- **Trap**: the Guidelines page says primary `#0989FF`, but the real system uses mint `#62d0b6` — use
  mint.
- **Source**: Figma community "Salla merchants websites design template" (`6tCYXU2MnUJtcuS69Ks5AV`).

---

## 3. Apple — iOS / iPadOS / macOS (HIG) ✅ complete

Apple's Human Interface Guidelines as an applyable system. **When a project is an Apple-platform app —
iOS/iPadOS native, macOS, or a cross-platform app that must feel native on Apple — this is the system.**

- **Read**: `references/design-systems/apple.md` — the applyable core (8 principles, SF Pro text-style
  scale, system/semantic colors light+dark, 8pt grid, 44pt target, materials/Liquid Glass, SF Symbols,
  cross-platform translation). For deep per-component rules use the full **apple-design** skill (all 123
  HIG pages, kept current).
- **At a glance**: SF Pro, semantic system colors (accent `systemBlue` #007AFF/#0A84FF), Body 17/22,
  8pt grid, 44pt hit target, continuous corners, dark mode required.
- **Use for**: iOS/iPadOS/macOS apps; Flutter/React Native targeting Apple (translate the vocabulary).

---

## Your own systems

Add your brands here, below the built-in kits. Each one becomes an option in the Phase 11 selector.

```md
## 4. <Brand name> ✅ complete | 🔶 partial
- **Use for**: which projects this brand covers
- **Colors**: primary, secondary, accent, neutrals (hex)
- **Fonts**: headings / body
- **Icons**: one library
- **Direction**: LTR / RTL, light / dark
- **Source**: Figma file or brand guide (if tokens live only there, mark 🔶)
```

---

## Adding a new saved system

When you finish a new system and want it reusable:
- A **small brand** (a few tokens) → add a section here directly with use-for, product type, full color
  tokens, fonts, icon library, direction, Figma reference.
- A **full design system** (many components) → give it its own file under
  `references/design-systems/<name>.md` with the complete spec, and add a short ✅ entry here that points
  to it (like Untitled UI above).

Prefer writing real tokens out; only fall back to *(من فيجما)* when they genuinely live only in Figma.

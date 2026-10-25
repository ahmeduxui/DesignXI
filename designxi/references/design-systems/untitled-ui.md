# Untitled UI — full design-system reference

The Untitled UI design system, read page by page from the Figma free community file
(`jl2IXuNW1VUXjqUn4PeNvp`, 12 pages) plus PRO v8 Instagram showcase shots. This is a **complete,
ready-to-apply system** — when a project uses Untitled UI, apply these exact tokens and component specs
instead of inventing any.

**Font note (overrides the skill's Inter rule).** Untitled UI's type is **Inter** by design. Using Inter
here IS the justification the skill's "no Inter as hero font" rule asks for — do not flag it. For an
Arabic / RTL project built on Untitled UI, keep the Untitled UI scale, spacing, and components, but swap
Inter for an Arabic face (e.g. IBM Plex Sans Arabic for body, Alexandria for display) and apply
`references/rtl-arabic.md`. Untitled UI itself is LTR/English-first.

**Free vs PRO.** The free version uses **styles only** (no variables). PRO v8 adds variables for spacing
and colors. Build with CSS custom properties regardless.

---

## Colors (263 paint styles; scales 25, 50, 100–900)

```css
/* Gray */
--gray-25:#fcfcfd; --gray-50:#f9fafb; --gray-100:#f2f4f7; --gray-200:#eaecf0; --gray-300:#d0d5dd;
--gray-400:#98a2b3; --gray-500:#667085; --gray-600:#475467; --gray-700:#344054; --gray-800:#1d2939;
--gray-900:#101828;
/* Primary (purple) */
--primary-25:#fcfaff; --primary-50:#f9f5ff; --primary-100:#f4ebff; --primary-200:#e9d7fe;
--primary-300:#d6bbfb; --primary-400:#b692f6; --primary-500:#9e77ed; --primary-600:#7f56d9;
--primary-700:#6941c6; --primary-800:#53389e; --primary-900:#42307d;
/* Error */
--error-50:#fef3f2; --error-300:#fda29b; --error-500:#f04438; --error-600:#d92d20; --error-700:#b42318;
/* Warning */
--warning-50:#fffaeb; --warning-500:#f79009; --warning-700:#b54708;
/* Success */
--success-50:#ecfdf3; --success-100:#d1fadf; --success-500:#12b76a; --success-600:#039855; --success-700:#027a48;
```

- **Extra palettes** (same 25–900 scale): Blue gray, Blue light, Blue, Indigo, Purple, Pink, Rosé,
  Orange. Plus avatar image styles.
- **Gradients**: 12 linear gradients (Gray/Primary 600→500 at 90°, 700→600 at 45°, 800→600, 900→600 …).
- **Text color roles**: headings `#101828` (gray 900); body / supporting `#667085` or `#475467`; labels
  `#344054`; links `#6941c6`; positive `#027a48`; error `#d92d20` / `#f04438`.
- **Badge pattern**: bg = `color/50`, text = `color/700` (e.g. Success `#ecfdf3` bg / `#027a48` text).

---

## Typography (Inter; Regular / Medium / Semibold / Bold, italics on text sizes)

Format below is `size/line-height` in px.

- **Text**: xs 12/18 · sm 14/20 · md 16/24 · lg 18/28 · xl 20/30
- **Display**: xs 24/32 · sm 30/38 · md 36/44 · lg 48/60 · xl 60/72 · 2xl 72/90
- **Letter-spacing**: −2% from 36px up. Line heights always even; ~1.5 ratio small → ~1.2 huge.
- **Usage**: 12 tooltips/meta · 14 UI base, labels, hints, supporting text · 16 input text, buttons lg+ ·
  18 modal title · 20 doc body paragraphs · 24/30 doc section headings · 30/36 stat values · 60 hero.

---

## Spacing (4px grid; 2/6/10/14 only inside small components)

Steps by relationship:
- **4** title↔supporting (modal header) · **6** label→input · **8** icon↔text & title→text ·
  **12** action buttons / list icon gap / tooltip padding · **16** between fields & grid items ·
  **24** container padding · **32** group gap (text→actions) · **64** page sections · **80** page side
  margin · **128** big section padding.
- **Doc page layout**: 1600 frame, content column 720 at x=80; heading→paragraph 24; link list pitch 44
  (28+16); sections divided by a line with 64 above/below; footer padding 128/80/80/80, gap 80.

---

## Components

### Buttons (1320 variants)
- **Sizes** (`height`, `pad v/h`, `text`): sm 36 (8/14, 14) · md 40 (10/16, 14) · lg 44 (10/18, 16) ·
  xl 48 (12/20, 16) · 2xl 60 (16/28, 18). Icon gap 8 (12 on 2xl). Radius 8. States
  Default / Hover / Focused / Disabled. Destructive variant exists.
- **Hierarchies**:
  - Primary: bg `#7f56d9` · hover `#6941c6` · disabled `#e9d7fe`
  - Secondary color: bg `#f9f5ff` · hover `#f4ebff`
  - Secondary gray: white + border `#d0d5dd` · hover bg `#f9fafb`
  - Tertiary: no bg · hover `#f9f5ff` / `#f9fafb`
  - Link color: `#6941c6` · hover `#53389e`
  - Link gray: `#667085` · hover `#475467`
  - Disabled text: `#d0d5dd`
- **Social buttons**: 44 high, pad 10/16, gap 12 (Google, Facebook, Apple, Twitter, Figma, Dribbble;
  Brand / Color / Color-with-brand). App-store badges 40/44.

### Inputs
- Height 44, padding 10/14, gap 8, radius 8, text 16, width 320.
- Label 14 `#344054`, gap 6. Hint 14 `#667085` (error `#f04438`).
- Border `#d0d5dd`; focused `#d6bbfb` + 4px focus ring primary-100; error border `#fda29b`; disabled bg
  `#f9fafb`.
- Types: Default, Leading/Trailing dropdown, Leading text, Payment. Textarea 128 high.
- **Verification code**: squares 64/80/96, digits 48/60, gap 8–12, 4 or 6 digits. WYSIWYG toolbar 44
  high, icons 32.

### Dropdown menu
- Width 240, radius 8, border `#f2f4f7`, shadow lg. Item 40 high, pad 10/16, gap 12, text 14.
- Header 44 (avatar header 64). Input-dropdown items 44, pad 10/14. Menu list padding 4 top/bottom.
  Hover bg `#f9fafb`. Scrollbar 8 wide.

### Badges
- sm 22 (2/8, 12) · md 24 (2/10, 14) · lg 28 (4/12, 14). Fully rounded. 13 colors. Badge group 30/32,
  pad 4/12/4/4.

### Tooltip
- Dark `#101828` or light white, radius 8, pad 8/12 (with supporting text: 12 all sides, gap 4),
  text 12, width up to ~320, arrow 12px. Help icon 16.

### Modal
- Overlay `#344054` @70% + background blur 16. Card radius 12, width 400–560 desktop (343 mobile),
  padding 24, gap 16–24. Featured icon 48 (circle, `color/100` bg, 24 icon). Title 18 semibold,
  supporting 14. Actions: 44 buttons, gap 12, block 32 top padding. Close button 44.

---

## Icons, logos, misc
- **Icons**: 24×24 line icons, stroke 2 (Feather-style names); also 20/32. Featured icons 32/40/48/56.
  Social, country, payment (34×24, 46×32, 58×40), integration icons.
- **Logos**: logomark 32; logo 142×32; company logos 48 high; press logos 48 high.
- **Misc assets**: patterns (dot cube, lines, wavy, topographic), credit card 316×190 r20, 3:2 screen
  mockups (480/640/768 wide), MacBook & iPhone 12 mockups, video player 16:9 r8, play buttons 48–96,
  hand-drawn arrows/lines, dividers.
- **Annotations**: design note (24/18 title), measure lines, numeric key combos, cursors.

---

## Radius, shadows, effects
- **Radius**: 8 buttons/inputs/menus/tooltips · 12 modals · 16 badges/pills (full) · 20 cards (credit
  card) · circles for featured icons/avatars.
- **Shadows**: xs (y1 b2 5%) · sm (y1 b3 10% + y1 b2 6%) · md (y4 b8 −2 10% + y2 b4 −2 6%) ·
  lg (y12 b16 −4 8% + y4 b6 −2 3%) · xl (y20 b24 −4 8% + y8 b8 −4 3%) · 2xl (y24 b48 −12 18%) ·
  3xl (y32 b64 −12 14%). Focus ring 4px spread (primary-100 / gray-100 / error-100). Background blur
  8/16/24/40.

---

## Core rules
- Element height = text line-height + equal vertical padding, always a multiple of 4; horizontal padding
  grows +2 per button size.
- Color usage: gray 900 for headings, gray 500–600 for secondary text, primary 600 for main actions,
  `color/50` bg + `color/700` text for soft badges.

---

## PRO v8 showcase lessons (Instagram @untitledui, 12 latest posts, Oct 2026)
Apply these when presenting Untitled UI screens (feeds into Phase 15 hi-fi and Phase 24 case study):
- **Presentation**: UI inside a macOS browser window on an artistic background (watercolor, halftone dot
  gradients, fog photo, flat light gray); calm UI vs textured backdrop; edges cropped to suggest a
  bigger product.
- **Focus trick**: blur/dim the whole app and keep one component sharp (share panel, command menu,
  modal) to show a component in context.
- **Color restraint**: near-monochrome gray UI, primary buttons black, one accent only (amber/gold for
  charts, selected date); dark mode and glassmorphism command menu over a photo.
- **Patterns shown**: payment-method modal with card mockup; upgrade/checkout = settings nav + form +
  summary card; share/permissions slide-over; email composer with floating format toolbar; profile
  editor with rich text; mega menu with featured video card; testimonial quote block; command palette;
  date picker with presets column; dark file manager; multi-step onboarding with signature.
- **Realism details**: real names/emails/amounts, visible cursor, open tooltips and hover states to show
  interaction.

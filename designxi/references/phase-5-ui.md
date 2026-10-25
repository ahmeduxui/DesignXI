# Phase 5 — UI Design

## Why This Phase Exists

UX defines what the product does and how users move through it. UI defines how it looks, feels, and communicates. As *Refactoring UI* puts it: "Design isn't just about making things pretty — it's about creating visual clarity that guides action." This phase turns your wireframes into a real, polished visual product.

The order matters: design system first, screens second. A design system ensures consistency. Screens without a design system become a mess of inconsistent decisions.

## Step 1: Confirm Brand System Is Ready

**Do not define new colors here.** By the time Phase 5 starts, the full brand color system (50→950 scale for every brand color) must already be confirmed from Phase 4.8. If it isn't, go back to `references/brand-identity.md` and complete it first.

What should already exist from Phase 4.8:
```css
/* These must already be defined before Phase 5 begins */
--primary-50 through --primary-950
--secondary-50 through --secondary-950 (if applicable)
--gray-50 through --gray-950
--success/warning/error/info (100 + 500)
--color-primary, --color-primary-hover, --color-primary-active
--color-text-primary, --color-text-secondary, --color-bg-page, etc.
```

### How to Use the Color Scale in Components

Now that the full scale exists, map the right stop to each component state:

```
Button — Primary:
  default bg   → --primary-500  (--color-primary)
  hover bg     → --primary-600  (--color-primary-hover)
  active bg    → --primary-700  (--color-primary-active)
  text         → white (#ffffff)
  focus ring   → --primary-300 at 50% opacity, 3px offset

Button — Secondary / Outline:
  border       → --primary-500
  text         → --primary-600
  hover bg     → --primary-50   (subtle tint)

Tags / Badges:
  background   → --primary-100
  text         → --primary-800

Alerts / Highlights:
  info bg      → --info-100, border --info-500
  success bg   → --success-100, border --success-500
  warning bg   → --warning-100, border --warning-500
  error bg     → --error-100, border --error-500

Input states:
  default border  → --gray-200
  focus border    → --primary-500 (2px)
  error border    → --error-500
  disabled bg     → --gray-50, text --gray-400

Navigation active item:
  background → --primary-50
  text       → --primary-700
  icon       → --primary-600

Section backgrounds (to create visual rhythm):
  Primary bg      → --gray-50
  Card bg         → white
  Subtle section  → --primary-50 (very light brand wash)
  Dark section    → --primary-900 or --gray-900 (for footers/CTAs)
```

**Color rules from the books:**
- Never use more than 2 brand colors (Refactoring UI)
- Use color to communicate meaning, not just decoration (101 Dos & Don'ts)
- 60% neutral, 30% primary/secondary, 10% accent (visual balance rule)
- Every color combination must meet WCAG AA — use only pre-verified combos from Phase 4.8
- Never hard-code a hex value in component CSS — always reference the CSS custom property

### Typography System — One Font, All Weights

**Rule: one font family only.** Use different weights to create hierarchy — not different families. The font must have been confirmed in Phase 4.8 (either from the brand file or chosen via the font selection process).

```
THE FONT: [Font name confirmed in Phase 4.8]
  - Source: Google Fonts — import all needed weights in one <link>
  - Import example:
    <link href="https://fonts.googleapis.com/css2?family=[FontName]:wght@400;500;600;700&display=swap" rel="stylesheet">

BODY FONT: [Same font name]
  - Source: Google Fonts URL
  - Character: [Describe — e.g., "Readable, neutral, comfortable at small sizes"]

TYPE SCALE:
  - Display: 48px / 56px line-height / font-weight 700
  - H1: 36px / 44px / 700
  - H2: 28px / 36px / 600
  - H3: 22px / 30px / 600
  - H4: 18px / 26px / 600
  - Body Large: 18px / 28px / 400
  - Body: 16px / 24px / 400
  - Body Small: 14px / 20px / 400
  - Caption: 12px / 16px / 400
  - Label: 12px / 16px / 500 (uppercase, letter-spacing: 0.08em)
```

**Typography rules:**
- Line length: 60-80 characters per line (readable prose)
- Body text never below 14px (accessibility)
- Line height: 1.4-1.6× font size for body text
- One font family only — confirmed in Phase 4.8

### Grid System — 8pt Base
*Source: Grid Systems in Graphic Design — Josef Müller-Brockmann*

**The rule: every spacing, size, and layout value must be a multiple of 8px.** This creates automatic visual harmony across the entire product. The 8pt grid works because most screens have dimensions divisible by 8 (375, 768, 1280), making alignment clean without sub-pixel rendering artifacts.

**Exception**: 4px is permitted for micro-gaps (icon-to-label distance, inline padding inside compact chips).

**The grid must be defined before designing any screen.** Designing without a grid is like building without a ruler — every decision is arbitrary, and the result looks it.

#### Mobile Grid (375px base width)
```
Columns:      4
Column width: auto (fills remaining space after margins and gutters)
Margin:       16px (left and right — distance from screen edge to first/last column)
Gutter:       16px (space between columns)
```

What this means in practice:
- Screen width: 375px
- Left margin: 16px | Right margin: 16px
- 3 gutters between 4 columns: 3 × 16px = 48px
- Total available for columns: 375 - 32 - 48 = 295px
- Each column: 295 ÷ 4 ≈ 73.75px

Column spans on mobile:
```
Full width:    4/4 → hero, full-width CTAs, navigation bars
Half:          2/4 → side-by-side buttons, 2-column grids
Three-quarter: 3/4 → primary content with sidebar
Single:        1/4 → icon, small badge, indicator
```

#### Tablet Grid (768px)
```
Columns:  8
Margin:   24px
Gutter:   24px
```

#### Desktop Grid (1280px)
```
Columns:      12
Column width: auto
Margin:       80px (or max-width: 1120px centered)
Gutter:       24px
Max content width: 1120px
```

Column spans on desktop:
```
Full width:     12/12 → hero, full-width CTAs, page headers
Main content:    8/12 → article body, primary content area
Sidebar:         4/12 → filters, supporting info, navigation
Card (3-up):     4/12 → feature cards, pricing tiers
Card (2-up):     6/12 → comparison layouts
Card (4-up):     3/12 → compact item grids, icon cards
Form (full):     6/12 → primary form inputs, wide fields
Form (half):     3/12 → zip code, phone, short date fields
```

#### 8pt Vertical Rhythm

All vertical spacing must be multiples of 8px:

```
4px  → micro only (icon-to-label inline gap, chip internal padding)
8px  → tight (between label and input field, icon padding)
16px → standard (card internal padding, list item height addition)
24px → medium (between form fields, between related groups)
32px → large (between card rows, between unrelated sections)
40px → section start (top of a content group)
48px → section separation (between major content blocks)
64px → page sections (major visual breaks, mobile)
80px → page sections (major visual breaks, desktop)
96px → hero padding
```

**Never use**: 13px, 17px, 22px, 28px, or any value not on this scale. If a value doesn't fit, round to the nearest 8px multiple.

#### CSS Grid Implementation

```css
/* ─── GRID CONTAINER ─── */
.grid {
  display: grid;
  grid-template-columns: repeat(12, 1fr);
  gap: 24px;                    /* gutter */
  max-width: 1120px;
  margin: 0 auto;
  padding: 0 80px;              /* margin */
  box-sizing: border-box;
}

/* ─── TABLET ─── */
@media (max-width: 1024px) {
  .grid {
    grid-template-columns: repeat(8, 1fr);
    gap: 24px;
    padding: 0 24px;
  }
}

/* ─── MOBILE ─── */
@media (max-width: 767px) {
  .grid {
    grid-template-columns: repeat(4, 1fr);
    gap: 16px;                  /* mobile gutter = 16px */
    padding: 0 16px;            /* mobile margin = 16px */
  }
}

/* ─── COLUMN SPANS ─── */
.col-12 { grid-column: span 12; }
.col-8  { grid-column: span 8;  }
.col-6  { grid-column: span 6;  }
.col-4  { grid-column: span 4;  }
.col-3  { grid-column: span 3;  }

/* Mobile overrides */
@media (max-width: 767px) {
  .col-12,
  .col-8,
  .col-6,
  .col-4,
  .col-3  { grid-column: span 4; }  /* Full width on mobile */

  .col-2-mobile { grid-column: span 2; }  /* Half on mobile */
}
```

#### 8pt in Components

Every component dimension follows 8pt:

```
Button height:         48px (primary), 40px (secondary), 32px (compact)
Button padding:        12px 24px (primary), 8px 16px (compact)
Input height:          56px (large), 48px (default), 40px (compact)
Input padding:         12px 16px
Card padding:          24px (standard), 16px (compact), 32px (large)
Nav bar height:        64px (desktop), 56px (mobile)
Tab bar height:        56px
Modal padding:         32px
Section padding top:   80px (desktop), 64px (mobile)
Icon size:             24px (standard), 20px (compact), 16px (small)
Avatar size:           40px (standard), 32px (small), 56px (large)
Touch target minimum:  48px × 48px
```

#### Grid Rules (Müller-Brockmann)

- Every element must align to the grid — no "eyeballed" positioning
- White space is part of the grid — empty columns create breathing room
- Breaking the grid is a design decision, not an accident — use it once or twice for impact (hero images, accent blocks)
- Consistent column spans across similar components create visual rhythm
- On mobile: nearly everything is full width (4/4) — don't force 2-column layouts on small screens unless content genuinely calls for it

### Spacing System

Base unit: 4px. All spacing is a multiple of this unit.

```
4px  → micro gaps (icon to label)
8px  → tight padding (chip, tag)
12px → small padding (compact list item)
16px → standard padding (card, input field)
24px → section padding (between related groups)
32px → large gap (between sections)
48px → section margin (major visual separation)
64px → page-level spacing
```

### Border Radius Scale

```
Sharp: 0px → serious, traditional, enterprise
Subtle: 4px → neutral, professional
Soft: 8px → friendly, modern
Rounded: 12px → consumer, approachable
Pill: 9999px → CTA buttons, tags
```

Choose one primary radius for cards/modals. Use pill for buttons or small tags.

### Elevation / Shadow System

```
Level 0: No shadow (flat elements, table rows)
Level 1: 0 1px 3px rgba(0,0,0,0.12) → cards, input fields
Level 2: 0 4px 12px rgba(0,0,0,0.12) → dropdown menus, tooltips
Level 3: 0 8px 24px rgba(0,0,0,0.16) → modals, dialogs
Level 4: 0 20px 40px rgba(0,0,0,0.20) → full-screen overlays
```

### Core Components

Define the visual spec for:

**Buttons:**
```
Primary: bg=[primary color], text=white, padding=12px 24px, radius=[chosen radius]
Secondary: bg=transparent, border=1px [primary color], text=[primary color]
Ghost: bg=transparent, no border, text=[primary color]
Disabled: bg=gray-200, text=gray-400, cursor=not-allowed
Destructive: bg=error-color, text=white
```

**Input Fields:**
```
Default: border=1px gray-200, bg=white, padding=12px 16px
Focus: border=2px [primary color], outline=none
Error: border=1px error-color, error message below
Disabled: bg=gray-50, text=gray-400
Label: above input, 14px, gray-700, margin-bottom=6px
Placeholder: gray-400, same size as input text
```

**Cards:**
```
bg=white, border-radius=[chosen], shadow=Level 1
Padding: 20px or 24px
Hover state: shadow=Level 2 (if interactive)
```

## Step 2: Design Each Screen

For each screen identified in Phase 4, create the full HTML implementation.

### Screen Design Principles (From the Books)

1. **Visual hierarchy first** *(Refactoring UI)*
   - One element must be the clear focal point per screen
   - Use size, weight, and color to establish hierarchy — not borders and boxes
   - If everything is bold, nothing is bold

2. **Use real content** *(Don't Make Me Think)*
   - No "Lorem ipsum" — write real copy, real names, real numbers
   - Users scan real content — fake content hides design flaws

3. **Design for states, not just the happy path** *(Designing Interfaces)*
   - Empty state: first time user sees the screen with no data
   - Loading state: what shows while data fetches
   - Error state: something went wrong — what now?
   - Partial state: some data, not all
   - Overflow state: what if there are 100 items instead of 5?

4. **Mobile-first if mobile** *(Essential Mobile Interaction Design)*
   - Touch targets minimum 44×44px
   - Primary action reachable with thumb (bottom third of screen)
   - Critical information in top half
   - Horizontal scrolling only for intentional carousels

5. **Reduce cognitive load** *(100 Things Every Designer Needs to Know About People)*
   - One primary action per screen
   - Progressive disclosure: show details only when needed
   - Familiar patterns over clever innovations
   - Label everything — don't rely on icons alone

### Screen HTML Template

Each screen should be built as a realistic representation using this HTML structure:

```html
<!-- DEVICE FRAME: Mobile -->
<div class="device-frame mobile">
  <div class="device-screen">
    <!-- STATUS BAR -->
    <div class="status-bar">9:41 AM</div>

    <!-- CONTENT -->
    <div class="screen-content">
      <!-- Your screen here -->
    </div>

    <!-- TAB BAR (if applicable) -->
    <div class="tab-bar">...</div>
  </div>
</div>

<!-- DEVICE FRAME: Web/Desktop -->
<div class="device-frame browser">
  <div class="browser-chrome">
    <div class="browser-dots"></div>
    <div class="browser-url">[app URL]</div>
  </div>
  <div class="browser-content">
    <!-- Your screen here -->
  </div>
</div>
```

## Step 3: Interaction Notes

For each screen, document key interactions:

```
SCREEN: [Name]
Interactions:
- Tap/Click [element] → [what happens, which screen appears]
- Swipe [direction] → [behavior]
- Long press [element] → [contextual menu or action]
- Scroll → [what loads or reveals]
- Input validation → [when does it trigger?]

Animation/Transition:
- Screen entrance: [slide in / fade in / none]
- Element appearance: [staggered list / instant / fade]
- CTA press: [scale down 0.97 + color shift]
```

## Step 4: Accessibility Review

Before finalizing, check:

```
□ All text meets 4.5:1 contrast ratio against its background
□ Interactive elements have visible focus states
□ Touch targets minimum 44×44px
□ Error messages don't rely on color alone (include icon + text)
□ Images have meaningful alt text
□ Form fields have associated labels
□ Loading states are announced (aria-live)
□ Navigation is logical in keyboard tab order
```

## Phase 5 Output

The output of Phase 5 is the HTML code for all screens, organized into the delivery files defined in Phase 6. When writing screen HTML:

- Use the design system tokens (CSS custom properties)
- Build in vanilla HTML + CSS (no frameworks required — this ensures portability)
- Use Google Fonts via CDN link in `<head>`
- Include hover states in CSS
- Add comments marking each screen section
- Use realistic content throughout

---

## Design System Audit Checklist

Before moving to screen production, verify the system is complete:

**Token Coverage**
- [ ] Zero hardcoded hex values — all colors via CSS custom properties
- [ ] Zero arbitrary spacing — all values are multiples of 8px (or 4px for micro)
- [ ] All border-radius, shadow, and transition values use named tokens

**Component Completeness**
- [ ] Every component has all states: default / hover / active / disabled / focus / error
- [ ] Every component has documentation: purpose, when to use, when NOT to use
- [ ] Variants are consistent — if button has 3 sizes, input has 3 sizes too

**Naming Consistency**
- [ ] Token names follow one convention: `--color-{role}-{scale}`, `--spacing-{n}`
- [ ] No duplicate tokens with different names for the same value
- [ ] No "magic numbers" — every value must have a named token

---

## Touch & Interaction Standards

Apply to every interactive element:
- Touch targets minimum **48×48px** (Apple HIG / 44×44pt) — extend hit area beyond visual bounds if needed
- Minimum **8px gap** between adjacent touch targets — prevents mis-taps
- Never rely on hover alone for primary interactions — use click/tap
- Buttons must show loading state during async operations (spinner, disable click)
- Swipe actions require visible affordance (label, chevron, or tutorial hint)
- Support system gestures — don't block iOS swipe-back or Android predictive back
- Mobile input height minimum 44px — use semantic input types (email, tel, number) for correct keyboard
- Use haptic feedback for confirmations and critical state changes — avoid overuse; never for decorative interactions

---

## UX Interaction Principles (Bencium Framework)

Apply these principles to every screen — they are the difference between a technically correct design and one that feels natural.

### Simplicity Through Reduction
Start with the most complete version of a screen. Then deliberately remove elements until reaching the simplest solution that still achieves the goal. Every element that survives removal must earn its place.
- Question every UI element: "Does removing this break the user's ability to accomplish their goal?"
- If no: remove it.
- If yes: keep it, but reduce its visual weight to match its functional importance.

### Material Honesty
Digital materials have unique properties — embrace them instead of fighting them:
- Shadows imply elevation — use them consistently to communicate layer depth, not decoration
- Borders create separation — use them only when spatial relationship is unclear
- Color carries meaning — don't use accent colors for decoration; reserve them for action and state
- Motion reveals relationships — animate to show where something came from and where it went

### Invisibility of Technology
The interface should disappear. Users must focus on their content and goals — not on understanding how the UI works:
- Navigation that requires thought is navigation that failed
- Labels that need explanation are labels that failed
- Flows that require memory are flows that failed
- Every point of confusion is a design problem, not a user problem

### The 100ms Feedback Rule
**Every interaction must produce visible feedback within 100ms.** This is the threshold below which actions feel "instant" to the human brain. Anything above 100ms feels laggy.

```
0–100ms   → Instant. No loading indicator needed. Use CSS transitions.
100–300ms → Fast. Use a subtle state change (color shift, scale pulse).
300ms–1s  → Noticeable. Show a loading spinner or skeleton.
1s+       → Slow. Show explicit progress + cancel option.
```

Apply per interaction type:
- Button tap → visual press state (scale 0.97 + color darken) within 100ms
- Form submit → button enters loading state before network request completes
- Navigation → route transition starts before content loads
- Search → show "searching..." or skeleton before results arrive

### Direct Manipulation Patterns
Prefer direct manipulation over modal dialogs and separate forms:
| Instead of... | Use... |
|---|---|
| Up/down buttons to reorder | Drag-and-drop |
| Edit button → separate form page | Inline editing (click to edit, click away to save) |
| Delete confirmation modal | Swipe-to-delete + undo toast (5s) |
| Settings page for toggles | Inline toggle in context |
| Modal to preview | Expand-in-place or slide-out panel |

Exception: destructive actions with no undo (permanent delete, account deletion) always require a confirmation dialog.

### Forgiveness Patterns
Design for human error — not just the happy path:
**Prevention strategies** (stop errors before they happen):
- Disable submit buttons until required fields are valid
- Use input masks for formatted fields (phone, credit card, date)
- Show character count before the limit, not after exceeding it
- Confirm before navigating away from unsaved changes

**Recovery strategies** (make errors easy to fix):
- Undo for all non-destructive actions (delete, archive, reorder) — 5-second toast
- Preserve form data on validation error — never clear the form
- Error messages must say what to do, not just what went wrong
- Allow editing submitted items within a reasonable window

### Progressive Disclosure
Reveal complexity only when the user needs it:
1. **Summary level**: Show only what's needed for the current decision
2. **Details level**: Expand on demand (accordion, tooltip, drawer)
3. **Advanced level**: Accessible but not prominent (settings page, "Advanced" toggle)

Never show all options at once. Every additional visible option increases cognitive load.

---

## Navigation Pattern Rules

Apply the correct pattern based on platform and content depth:
- **Mobile**: Bottom nav for top-level (max 5 items, icon + label) · Drawer for secondary nav
- **Web**: Sidebar for 3+ levels · Top bar for 2 levels · Breadcrumbs for 3+ level hierarchies
- Back navigation must be predictable — preserve scroll position and filter state
- Current location always visually highlighted (color, weight, or indicator)
- Modals must have a clear close affordance — never use modals for primary navigation flows
- Don't mix Tab + Sidebar + Bottom Nav at the same hierarchy level
- Modal/drawer scrim opacity: **40–60% black** — strong enough to isolate foreground, not claustrophobic

---

## Forms & Feedback Rules

- Every input must have a visible label — placeholder text is NOT a label
- Show errors below the related field (not only at the top)
- Validate on blur, not on every keystroke — show errors only after user finishes input
- Provide a `show/hide` toggle for password fields
- Multi-step flows must show a progress indicator and allow back navigation
- Confirm before any destructive action — use semantic danger color (red) + icon
- Empty states must include: what this space is + why empty + how to start
- Auto-dismiss toasts in 3–5 seconds · use `aria-live="polite"` for screen reader announcement

---

## Performance as UX

**Performance is a design decision, not a developer concern.** A visually perfect interface that takes 4 seconds to load is a bad UX — regardless of typography quality or animation polish.

Apply this priority order (from highest UX impact to lowest):

| Priority | Category | Impact | What it means |
|---|---|---|---|
| 1 | **Eliminate Waterfalls** | 🔴 CRITICAL | Sequential API calls that block rendering are the #1 performance bottleneck. Design screens that can render progressively — show skeleton, load critical data first, then fill in secondary data |
| 2 | **Reduce Bundle Size** | 🔴 CRITICAL | Don't import entire icon libraries — import only the icons used. Avoid barrel file imports. Use dynamic imports for heavy components (modals, charts) |
| 3 | **Perceived Speed** | 🟠 HIGH | Optimistic UI (show result before server confirms), skeleton screens, and instant feedback within 100ms make interfaces feel faster than they measure |
| 4 | **Actual Load Time** | 🟡 MEDIUM | Image formats, lazy loading, font swap — real improvements but smaller UX impact than perceived speed |
| 5 | **Re-render optimization** | 🟡 MEDIUM | Memoization, derived state — only matters when actual performance problems are measured, not assumed |

**Design implications per priority:**

**Eliminating waterfalls** — design screens in data layers:
- Layer 1 (instant): Layout chrome, navigation, static copy — renders from HTML
- Layer 2 (fast): Primary content — loads first, shows skeleton until ready
- Layer 3 (deferred): Secondary content, recommendations, activity — loads after primary
- Never design a screen that requires 3 API calls to complete before showing anything

**Perceived speed** — design patterns that feel instant:
- Optimistic updates: mark an item complete immediately, revert only on error
- Skeleton screens over spinners: skeletons show structure while loading, reducing anxiety
- Instant visual feedback on tap/click (within 100ms) — state change before network response
- Progressive image loading: low-quality placeholder → full resolution

## Performance Checklist (HTML Deliverables)

- Use `WebP` or `AVIF` format for images — not PNG/JPG
- Declare `width` and `height` on all images to prevent layout shift (CLS < 0.1)
- Use `loading="lazy"` for below-the-fold images
- Use `font-display: swap` for web fonts — avoids invisible text flash
- Reserve space for async content (skeleton screens) — never show an empty frame
- Keep touch/tap response under 100ms — provide visual feedback within that window
- Lighthouse score target: ≥ 90 for Performance, Accessibility, Best Practices

---

## Charts & Data Visualization

Choose the right chart type first:

| Data Goal | Chart Type | Avoid |
|---|---|---|
| Show trend over time | Line chart | Pie chart |
| Compare categories | Bar / Column chart | 3D charts |
| Show proportion of a whole | Donut chart (≤5 categories) | Pie with >5 slices |
| Show distribution | Histogram | Line chart |
| Show correlation | Scatter plot | Bar chart |
| Show progress to goal | Gauge / Progress bar | Area chart |
| Compare multiple metrics | Radar / Spider chart | Use sparingly |
| Show geographic data | Map / Choropleth | — |

Chart design rules:
- Always show a legend — position near the chart, not detached below scroll
- Provide tooltips on hover (web) or tap (mobile) showing exact values
- Label axes with units — avoid truncated or rotated labels on mobile
- Never rely on color alone to convey data — add patterns, shapes, or labels
- Use accessible color palettes — avoid red/green-only pairs
- Empty state: show "No data yet" + guidance — never a blank chart frame
- For 1000+ data points: aggregate or sample, provide drill-down for detail
- Each chart needs a one-sentence plain-text description via `aria-label` or `<caption>`
- Sortable data tables: use `aria-sort` attribute on column headers
- On mobile: reflow charts (horizontal bar instead of vertical, fewer ticks)
- Grid lines should be low-contrast (gray-200) — data is the hero, not the grid
- Data-heavy products (10+ metrics): offer CSV and/or image export

---

## Design Self-Critique (Phase 9b)

Run a 5-axis critique on each screen before user testing:

| Axis | Critique Question | Severity if Failing |
|---|---|---|
| **Usability** | Can a new user complete the core task without guidance? Where will they hesitate? | 🔴 Critical |
| **Visual Hierarchy** | Does the eye land on the most important element first? Any competing focal points? | 🟠 Serious |
| **Consistency** | Do similar elements look and behave identically across screens? Any one-off styles? | 🟡 Minor |
| **Accessibility** | Does every interactive element have a visible focus state? Is contrast passing? | 🔴 Critical |
| **First Impression** | 2-second test: is the screen purpose immediately clear? | 🟠 Serious |

Produce a critique table for each screen:
```
Screen: [Name]
| Axis | Finding | Severity | Fix |
```

Rules: Fix all 🔴 Critical before Phase 10 · Log 🟠 Serious · 🟡 Minor go to v2 backlog.

---

## AI-Assisted Asset Generation

For missing visuals: Midjourney / Adobe Firefly / DALL-E for portraits + illustrations. Storyset / Undraw for SVG illustrations. Always label: "(AI-generated placeholder — replace before launch)". No gray placeholder boxes in final deliverables.

---

## Dashboard Layout Hierarchy

Dashboards present multiple data types simultaneously. Visual hierarchy must guide the eye from most important to least important without requiring scanning.

### Dashboard Information Architecture

Structure every dashboard using this hierarchy:

```
Level 1 — KPI Cards (top row)
  Purpose: Instant health check — "Is everything OK?"
  Content: 3–6 key metrics with trend indicators
  Size: Full width, 80–100px height cards
  Data: Current value + comparison (vs. last period, vs. target)
  Visual: Large number, small label, trend arrow (↑↓) or sparkline

Level 2 — Primary Charts (below KPI row)
  Purpose: "What's happening over time?"
  Content: 1–2 dominant charts (line/bar)
  Size: 60–70% of viewport width, 280–320px height
  Interaction: Hover tooltips, click-to-drill-down

Level 3 — Secondary Data (right column or below primary)
  Purpose: "What's the breakdown?"
  Content: Donut charts, distribution bars, ranked lists
  Size: 30–40% of viewport width, 200–260px height

Level 4 — Detail Tables (bottom)
  Purpose: "Show me everything"
  Content: Sortable, filterable data table
  Features: Pagination or infinite scroll, column visibility toggle, CSV export
```

### Dashboard Design Rules

```
1. PROGRESSIVE DISCLOSURE
   Show summary first. Detail on demand.
   KPI card → hover → sparkline → click → drill-down chart → click → raw table

2. TIME RANGE CONSISTENCY
   All charts on one dashboard use the SAME time range.
   One control sets it for everything. Never let charts show different periods silently.

3. EMPTY STATE IN EVERY CHART
   Every chart has a designed empty state:
   "No data for this period" + explanation of why + action if appropriate

4. LOADING SKELETON, NOT SPINNER
   Dashboard components load independently — show skeleton per card/chart.
   Never show a full-page spinner for a dashboard.

5. COMPARISON ALWAYS
   Numbers without context are meaningless:
   "453 users" is useless. "453 users (+12% vs last week)" is actionable.
   
6. COLOR ENCODE PERFORMANCE
   - Green / success-500: exceeding target
   - Yellow / warning-500: within acceptable range
   - Red / error-500: below threshold
   - Gray: no target set
   Consistent encoding across ALL charts and KPI cards.
```

---

## Landing Page Design Checklist

Landing pages have one job: convert visitors. Every design decision must serve that goal.

### Above-the-Fold Requirements (First Viewport — No Scrolling)

```
□ HEADLINE: Clearly states what the product does and for whom (10 words max)
□ SUBHEADLINE: Elaborates on the primary benefit (20–30 words)
□ PRIMARY CTA: One action, above the fold, high contrast button
□ TRUST SIGNAL: 1 social proof element (logo strip, testimonial, rating)
□ VISUAL: Product screenshot / illustration that shows the UI or outcome
□ NO NAVIGATION CLUTTER: Minimal nav — logo + CTA only preferred
```

### Landing Page Conversion Architecture

```
Section 1: Hero (Problem + Solution)
  - Headline addressing the pain point
  - Subheadline with your approach/benefit
  - Primary CTA button
  - Hero visual (product or outcome)

Section 2: Social Proof (Trust)
  - Customer logos or review ratings
  - "Trusted by X companies" or star rating with count

Section 3: Features / Benefits (Clarity)
  - 3 key benefits, not feature lists
  - Each: icon + headline + one-sentence description
  - Benefits framed as outcomes, not capabilities

Section 4: How It Works (Understanding)
  - 3-step process illustration
  - Step 1 → Step 2 → Step 3
  - Keep it simple — do not list more than 3 steps here

Section 5: Social Proof Deep (Credibility)
  - 2–3 testimonial cards with name, role, company, photo
  - Or: case study with specific metric ("Reduced time by 40%")

Section 6: Secondary CTA (Conversion)
  - Repeat the primary CTA with a different frame
  - Add risk-reduction language: "Free trial · No credit card"

Section 7: FAQ (Objection Removal)
  - 4–6 questions addressing the most common objections

Section 8: Final CTA (Urgency)
  - Strong closing CTA
  - Optional: limited offer or waitlist urgency
```

### Landing Page Copy Rules

```
- Hero headline: outcome-focused, not feature-focused
  ✓ "Ship faster without breaking things"
  ✗ "A CI/CD platform with 200+ integrations"

- CTA copy: action + outcome, not generic
  ✓ "Start free trial" or "See it in 2 minutes"
  ✗ "Get started" or "Learn more" or "Submit"

- Social proof specificity: numbers beat vague praise
  ✓ "Reduced onboarding time by 60%" — Maria Chen, VP Operations
  ✗ "Great product! Really helped us." — A satisfied customer

- Feature list → benefit translation:
  Feature: "Automated testing"
  Benefit: "Ship with confidence — catch bugs before users do"
```

---

## Performance UX Rules

Design decisions that affect page performance directly impact user experience. Slow interfaces feel broken even when they're functional.

### Core Performance UX Principles

**1. Virtualize Long Lists**
Never render more than 50–100 DOM nodes for a scrollable list. Use virtual scrolling:

```js
// Principle: only render visible items + small buffer above/below
// Libraries: react-window, react-virtual, @tanstack/virtual
// Target: lists with 100+ items must be virtualized
// UX tell: if scrolling feels sluggish with 200 items, it's not virtualized
```

**2. Progressive Loading — Skeleton Screens Over Spinners**

```css
/* Skeleton shimmer animation */
@keyframes shimmer {
  0% { background-position: -200% 0; }
  100% { background-position: 200% 0; }
}
.skeleton {
  background: linear-gradient(90deg, #f0f0f0 25%, #e0e0e0 50%, #f0f0f0 75%);
  background-size: 200% 100%;
  animation: shimmer 1.5s infinite;
  border-radius: 4px;
}
```

Rules:
- Use skeletons for content that has a known layout (cards, lists, feeds)
- Use spinners only for actions with unknown completion time (processing, uploading)
- Never show a skeleton for more than 3 seconds — show error state instead
- Match skeleton size/shape to real content — random rectangles are worse than nothing

**3. Main Thread Budget**

Interactions must respond within 100ms to feel instantaneous. Design implications:

```
100ms  → Feels instantaneous (tap, toggle, checkbox)
300ms  → Noticeable but acceptable (navigation, filter apply)
1000ms → User attention breaks — must show progress indicator
3000ms → User assumes failure — must show status + option to cancel
```

For any user action that takes >300ms:
- Disable the trigger button (prevents double-submit)
- Show inline loading indicator (spinner in button or bar below it)
- Never block the entire UI with a modal overlay spinner for non-critical operations

**4. Network Fallback — Design for Connectivity Gaps**

```
Offline state:
  □ Detect offline with navigator.onLine + offline event
  □ Show persistent banner: "You're offline. Changes will sync when reconnected."
  □ Disable submit buttons that require network
  □ Allow read-only browsing of cached content

Slow connection:
  □ Images: lazy load with loading="lazy" + low-res placeholder
  □ Videos: autoplay disabled on slow connection (prefers-reduced-data)
  □ Large tables: paginate, default to 25 rows
  □ Charts: load last-cached data, show timestamp + refresh button

Partial load failure:
  □ Per-component error boundary: one failing widget ≠ broken page
  □ Show: "Failed to load [section name]. Retry ↺"
  □ Log error, but never expose technical details to users
```

**5. Image Optimization Rules**

```
Format hierarchy:
  AVIF → WebP → JPEG (fallback)
  Use <picture> element with format fallbacks

Sizing:
  Never serve a 2000px image in a 200px container
  Use srcset + sizes for responsive images

Lazy loading:
  loading="lazy" on all images below the fold
  loading="eager" only for hero images and LCP element

Placeholder:
  Low-resolution blur-up: load 10px version first, blur it, replace with full
  Or: dominant color placeholder while image loads
```

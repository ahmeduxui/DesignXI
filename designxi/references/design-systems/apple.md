# Apple — iOS / iPadOS / macOS design system (HIG)

Apple's Human Interface Guidelines as a ready-to-apply system. **Use it when a project is an Apple-
platform app** — iOS/iPadOS native (SwiftUI, UIKit), macOS, or a cross-platform app (Flutter, React
Native) that should feel native on Apple devices. For deep per-component rules (sheets, tab bars,
pickers, widgets, Live Activities, Apple Pay, App Review), the full HIG is bundled at
`references/apple-hig/` — the HIG bundled by group in `hig/` (cite file › slug › heading), a routing table `hig-lookup.md`, `cross-platform.md`, and
`code-audit.md`. Load 8–12 pages per the "on screen → load" map below, never the whole folder (Apple
updates the HIG periodically; confirm against developer.apple.com when in doubt). This file is the
applyable token-and-principle core.

**Values are stable logical points / published system values.** Apple's dynamic colors are defined
**semantically** (a role that resolves to different values in light vs dark) — use the role name, not a
frozen hex, in code. The hex below are the standard resolved values for mockups.

---

## The 8 design principles (first filter, before any token)
A screen that breaks a principle has a bigger problem than any single guideline it breaks.

| Principle | The question you ask |
|---|---|
| Purpose | What is this screen for, and does the design serve it? |
| Agency | Can people explore, skip, and recover from mistakes? |
| Responsibility | Are permissions, data use, and intent transparent? |
| Familiarity | Do patterns match the platform and stay consistent? |
| Flexibility | Does it work across sizes, inputs, text sizes, and abilities? |
| Simplicity | Has every element earned its place? |
| Craft | Spacing, alignment, wording, animation — is it finished? |
| Delight | Is there a feeling, and is it the right one? (Don't mistake delight for decoration) |

---

## Typography — **SF Pro** (Text & Display, dynamic optical sizes); SF Compact / New York as alternates

iOS text styles, logical points `size/leading` (the default "Large" Dynamic Type size):

| Style | Size/Leading | Weight (emphasized) |
|---|---|---|
| Large Title | 34/41 | Regular (Bold) |
| Title 1 | 28/34 | Regular (Bold) |
| Title 2 | 22/28 | Regular (Bold) |
| Title 3 | 20/25 | Regular (Semibold) |
| Headline | 17/22 | **Semibold** |
| Body | 17/22 | Regular (Semibold) |
| Callout | 16/21 | Regular (Semibold) |
| Subhead | 15/20 | Regular (Semibold) |
| Footnote | 13/18 | Regular (Semibold) |
| Caption 1 | 12/16 | Regular (Medium) |
| Caption 2 | 11/13 | Regular (Semibold) |

macOS base body is **13 pt**. **Always design against Dynamic Type** — text scales with the user's
setting, so never hardcode a pixel height that clips a larger size (this is a `break-ui` case too). SF
Symbols align with the font at every weight and size — use them as the icon system.

---

## Color — semantic roles (use the role; hex is the resolved value, Light / Dark)

**System accent colors** (`systemBlue` is the default tint):
```
Blue   #007AFF / #0A84FF   Green  #34C759 / #30D158   Red    #FF3B30 / #FF453A
Orange #FF9500 / #FF9F0A   Yellow #FFCC00 / #FFD60A   Indigo #5856D6 / #5E5CE6
Teal   #30B0C7 / #40C8E0   Pink   #FF2D55 / #FF375F   Purple #AF52DE / #BF5AF2
Gray   #8E8E93 / #8E8E93
```
**Backgrounds** (pick the *grouped* set for grouped/table layouts, the *system* set otherwise):
```
systemBackground            #FFFFFF / #000000
secondarySystemBackground   #F2F2F7 / #1C1C1E
tertiarySystemBackground    #FFFFFF / #2C2C2E
systemGroupedBackground     #F2F2F7 / #000000
```
**Foreground / labels** (opacity over the background, both appearances):
```
label           100%   ·  secondaryLabel  60%  ·  tertiaryLabel  30%  ·  quaternaryLabel 18%
separator (opaque) #C6C6C8 / #38383A    ·    link = the accent color
```
**Rules:** don't redefine a semantic color's meaning (no `separator` as text, no `secondaryLabel` as a
background). Never rely on color alone to convey state — pair with text or an SF Symbol. In colorful
apps, keep toolbars/tab bars monochrome or one differentiated accent.

---

## Spacing, layout, hit targets
- **8pt grid** (4pt for fine adjustments). Standard screen margins **16pt** (compact) / 20pt.
- **Minimum hit target 44×44pt** — the single most-broken iOS rule.
- **Respect safe areas** — never put content or controls under the status bar, Dynamic Island,
  home indicator, tab bar, or toolbar.
- **Size classes, not devices** — lay out to compact/regular width, not to "iPhone 15".

## Shape, material, motion
- **Corner radius**: continuous (superellipse) corners, concentric with the enclosing shape — an inner
  element's radius = outer radius − padding. Controls ~10–12pt, cards larger, capsules for pills.
- **Materials / Liquid Glass**: translucent functional layers (bars, sheets) take color from content
  behind; add tint only to emphasize a primary control. Don't stack glass on glass. (Full checklist in
  the apple-design skill's `liquid-glass.md`.)
- **Motion**: system-standard transitions, honor **Reduce Motion**, haptics via the standard patterns.
- **Dark mode is required**, not optional, on Apple platforms — design both from the start.

## Icons
- **SF Symbols** as the icon system (weights match the font). One app accent color. App icon per the
  app-icon grid. No emoji as UI icons.

---

## What's on screen → what to check (quick map; full pages in the apple-design skill)
Tabs/sidebar/split view → tab-bars, sidebars, split-views, toolbars · Buttons/menus → buttons, menus,
context-menus · Sheets/alerts → modality, sheets, alerts, popovers · Forms → text-fields, pickers,
toggles, keyboards · Lists → lists-and-tables, collections · Glass/blur → materials, liquid-glass ·
Icons → sf-symbols, app-icons · Onboarding/permissions → onboarding, privacy, sign-in-with-apple ·
Payment → apple-pay · AI features → generative-ai.

---

## Cross-platform (when it's Flutter / React Native / Electron, not SwiftUI)
Translate the vocabulary, keep the principle:
- iOS/iPadOS → mobile/tablet (touch-first, one-handed) · macOS → desktop (pointer, keyboard, menu bar)
- System/semantic colors → ThemeData / design tokens / CSS custom properties (roles that adapt to dark)
- SF Pro → platform system font stack · SF Symbols → one consistent icon set (Lucide/Material)
- Tab bar → BottomNavigationBar/tab navigator · Sheet → bottom sheet/modal · Liquid Glass →
  `backdrop-filter` blur · Dynamic Type → textScaler / font-size settings · Safe area → SafeArea/insets
- Hit target 44pt (48dp on Material). Decide per component: follow each platform's convention, or one
  shared design — and say which.

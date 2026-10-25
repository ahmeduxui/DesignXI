# RTL & Arabic Design Guide

A complete reference for designing bilingual Arabic/English digital products. Arabic is not just right-to-left text — it's a fundamentally mirrored layout system with its own typographic rules, interaction patterns, and cultural considerations.

---

## 1. The Mental Model: Mirror, Don't Translate

The fundamental rule: **RTL is a mirror of LTR, not just text swapped in the same layout.**

Everything that flows with reading direction must flip:
- Page structure (nav, sidebars, content columns)
- Component layout (icon + label order, button positions)
- Progress indicators (step 1 is on the right)
- Swipe gestures (swipe left to go forward = wrong in RTL)

Everything that does NOT flip:
- Media (images, videos, maps)
- Numbers (remain LTR even in Arabic text)
- Punctuation within numbers (9:30، not ٣٠:٩)
- Icons that represent physical reality (a clock face stays the same)
- Non-directional icons (emoji, logos, brand icons)

---

## 2. HTML & CSS Foundation

### Document-Level Setup
```html
<!-- Root level: always declare lang and dir -->
<html lang="ar" dir="rtl">

<!-- For bilingual pages, switch per content block -->
<div dir="rtl" lang="ar">   <!-- Arabic block -->
<div dir="ltr" lang="en">   <!-- English block -->
```

### CSS Logical Properties (preferred over physical)
Use logical properties so components automatically flip with dir attribute:
```css
/* Instead of margin-left / margin-right — use: */
margin-inline-start: 16px;   /* = margin-left in LTR, margin-right in RTL */
margin-inline-end: 16px;     /* = margin-right in LTR, margin-left in RTL */

/* Instead of padding-left / padding-right */
padding-inline-start: 24px;
padding-inline-end: 24px;

/* Instead of border-left */
border-inline-start: 2px solid var(--color-primary);

/* Instead of text-align: left */
text-align: start;           /* left in LTR, right in RTL */
text-align: end;             /* right in LTR, left in RTL */

/* Instead of left / right positioning */
inset-inline-start: 0;
inset-inline-end: 0;
```

### CSS Transform Flip (when logical props aren't enough)
```css
/* Flip the entire component for RTL */
[dir="rtl"] .component {
  transform: scaleX(-1);
}

/* But only for truly directional icons — not all icons */
[dir="rtl"] .chevron-right,
[dir="rtl"] .arrow-forward,
[dir="rtl"] .breadcrumb-separator {
  transform: scaleX(-1);
}
```

### Flexbox in RTL
Flexbox automatically respects `dir` — `flex-start` means right in RTL:
```css
.row {
  display: flex;
  /* Do NOT use justify-content: flex-start for "leading" alignment */
  /* Use start/end or let dir handle it */
  gap: 12px;
}
```

---

## 3. Typography — Arabic Fonts

### Font Selection Criteria
Arabic typefaces must meet these requirements:
1. **Hinting quality** — crisp at 14–16px screen rendering
2. **Weight variety** — at least Regular (400), Medium (500), Bold (700)
3. **Latin companion** — for mixed Arabic/English content (numbers, brand names)
4. **RTL-tested** — ligatures and diacritics render correctly

### Recommended Arabic Fonts (2024 standards)

| Font | Use Case | Weights | Notes |
|------|----------|---------|-------|
| **Tajawal** | Bilingual body text | 200–900 | Best LTR/RTL dual support; excellent readability |
| **Cairo** | Display + UI | 200–900 | Modern, geometric; works for headers |
| **Alexandria** | Premium/brand | 100–900 | Elegant; great for upscale products |
| **Almarai** | Consumer apps | 300–800 | Clean, approachable; common in Saudi apps |
| **Noto Sans Arabic** | System fallback | 100–900 | Google's universal Arabic — no missing glyphs |
| **IBM Plex Arabic** | SaaS / enterprise | 100–700 | Professional, neutral |
| **Readex Pro** | Bilingual headlines | 160–700 | Variable font; designed for mixed content |

**Stacion** (used in Mrsool, Ninja redesigns): Display/brand use only — not available on Google Fonts; requires license.

### Google Fonts Import (correct syntax)
```html
<!-- Single Arabic font (Tajawal) -->
<link href="https://fonts.googleapis.com/css2?family=Tajawal:wght@400;500;700&display=swap" rel="stylesheet">

<!-- Bilingual (Tajawal Arabic + Inter English) -->
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Tajawal:wght@400;500;700&display=swap" rel="stylesheet">

<!-- Premium bilingual (Alexandria + Plus Jakarta Sans) -->
<link href="https://fonts.googleapis.com/css2?family=Alexandria:wght@400;500;600;700&family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">
```

### CSS Font Application
```css
/* Base: Latin font */
:root {
  --font-latin: 'Inter', sans-serif;
  --font-arabic: 'Tajawal', sans-serif;
}

body {
  font-family: var(--font-latin);
}

/* Switch to Arabic font for RTL content */
[dir="rtl"],
[lang="ar"] {
  font-family: var(--font-arabic);
}

/* Mixed inline content: numbers stay in Latin font */
[dir="rtl"] .number,
[dir="rtl"] .price,
[dir="rtl"] .percentage {
  font-family: var(--font-latin);
  direction: ltr;
  unicode-bidi: embed;
}
```

### Arabic Typography Sizing Rules
Arabic characters are visually smaller than Latin at the same font-size. Compensate:
```css
/* If body Latin = 16px, set Arabic to 17–18px */
[dir="rtl"] body {
  font-size: 17px;
  line-height: 1.7;   /* Arabic needs slightly more line height than Latin */
}

/* Heading adjustments */
[dir="rtl"] h1 { font-size: calc(var(--text-h1) + 2px); }
[dir="rtl"] h2 { font-size: calc(var(--text-h2) + 2px); }
[dir="rtl"] h3 { font-size: calc(var(--text-h3) + 1px); }
```

### Letter Spacing — Critical Rule
**Never apply `letter-spacing` to Arabic text.** Arabic letters connect (cursive nature). Spacing breaks ligatures and destroys readability.
```css
/* CORRECT */
[dir="rtl"] * {
  letter-spacing: 0 !important;
}

/* WRONG — breaks Arabic letters */
[dir="rtl"] h1 {
  letter-spacing: 0.05em; /* DON'T DO THIS */
}
```

---

## 4. Numbers in Arabic Context

### Number Systems
Arabic uses two numeral systems:
- **Western-Arabic (default):** 0 1 2 3 4 5 6 7 8 9 — used in tech/UI
- **Eastern-Arabic:** ٠ ١ ٢ ٣ ٤ ٥ ٦ ٧ ٨ ٩ — used in formal/government documents

**Recommendation:** Use Western-Arabic numerals (0–9) in product UIs. Eastern Arabic is for government portals and formal documents only. Saudi users in tech contexts expect Western numerals.

### Number Direction in Arabic Text
Numbers always run left-to-right, even in RTL text:
```
Arabic: اشتريت ١٢ منتجاً بسعر 45.99 ريال
         ← Arabic text reads right to left
                                → Numbers read left to right
```

### Bidirectional Text Implementation
```html
<!-- Mixed content: enforce correct directionality -->
<p dir="rtl">
  السعر: <span dir="ltr">SAR 45.99</span>
</p>

<!-- Phone numbers: always LTR -->
<span dir="ltr">+966 50 123 4567</span>

<!-- Date formats in Arabic context -->
<time dir="ltr">12/04/2024</time>
```

### CSS for Bidirectional Numbers
```css
.price,
.phone-number,
.percentage,
.date {
  direction: ltr;
  unicode-bidi: embed;
  font-family: var(--font-latin); /* Latin numerals look better in Latin fonts */
}
```

---

## 5. Layout Mirroring — Component by Component

### Navigation Bar
```
LTR: [☰ Logo]                    [Search] [Profile] [Cart]
RTL: [Cart] [Profile] [Search]                    [Logo ☰]
```
- Logo stays visually the same (don't mirror the logo image)
- Hamburger moves to the right side
- Primary CTA moves to the left side in RTL

### Sidebar
```
LTR: Left sidebar | Main content
RTL: Main content | Right sidebar
```

### Breadcrumbs
```
LTR: Home  >  Category  >  Product
RTL: Product  <  Category  <  Home
```
Arrow direction flips, and order flips (current page is on the left in RTL).

### Cards with Icon + Label
```
LTR: [Icon] Label text
RTL: Label text [Icon]
```

### Form Fields
```
LTR: Label     [________________ Input ___________]
RTL:           [___________ Input ________________] Label
```
- Input text-align: right in RTL
- Placeholder text: right-aligned
- Error message: below field, right-aligned
- Icon inside field: moves to opposite side

### Buttons
Primary buttons:
```
LTR: [← Back]  [Next →]   (back on left, forward on right)
RTL: [→ Next]  [← Back]   (forward on left, back on right)
     Wait — no. Direction flips but meaning stays:
RTL: [التالي ←] [→ رجوع]  (reading: "Next" appears on left side of the button group)
```
The button that means "go forward" is on the left in RTL layouts.

### Step Indicators / Progress Bars
```
LTR: ①━━━━②━━━━③━━━━④   (step 1 on left, progress left→right)
RTL: ④━━━━③━━━━②━━━━①   (step 1 on right, progress right→left)
```

### Sliders / Range Inputs
```
LTR: Min ●━━━━━━━━━━━━━━━━━━━━━ Max
RTL: Max ━━━━━━━━━━━━━━━━━━━━━● Min
```
The filled portion of the track flips direction.

### Tabs
```
LTR: [Tab 1] [Tab 2] [Tab 3]    (Tab 1 on left)
RTL: [Tab 3] [Tab 2] [Tab 1]    (Tab 1 on right — first tab is rightmost)
```

### Tables
```
LTR: Column A | Column B | Column C | Actions
RTL: Actions  | Column C | Column B | Column A
```
First column is on the right. Action column moves to the right.

---

## 6. Icons — What to Flip and What Not to Flip

### ALWAYS FLIP (directional icons)
These icons have an inherent left-to-right meaning that must be mirrored:
```
→ Arrow right          ← Arrow left (becomes the "forward" icon)
› Chevron right        ‹ Chevron left
≫ Double chevron       ≪ opposite
⟶ Long arrow
▶ Play button (points left in RTL)
⏩ Fast forward
↗ Reply (mirrors to ↖)
🔙 Back
Breadcrumb separator
List indentation arrows
Quote marks (« » instead of " ")
```

### NEVER FLIP (universal icons)
```
🔍 Magnifying glass (search)
⚙️ Settings gear
🔔 Bell (notifications)
❤️ Heart (like/favorite)
⭐ Star (rating)
📅 Calendar
🏠 Home (house shape stays same)
👤 Profile/user
📧 Email envelope
📱 Phone
🕐 Clock / time
💳 Credit card
🌍 Globe
✓ Checkmark
✗ Close/X
+ Plus
− Minus
```

### Context-Dependent (flip based on semantic meaning)
```
📋 List view — flip if list items show indent/hierarchy
📎 Attachment — don't flip (paperclip is physical)
📂 Folder — don't flip
✂️ Scissors — don't flip (physical object)
🖊️ Pen/edit — don't flip
```

### Implementation
```css
/* Flip directional icons */
[dir="rtl"] .icon-arrow-right,
[dir="rtl"] .icon-chevron-right,
[dir="rtl"] .icon-forward,
[dir="rtl"] .icon-send,
[dir="rtl"] .icon-reply {
  transform: scaleX(-1);
}

/* Using an icon class system */
[dir="rtl"] [class*="icon-arrow"],
[dir="rtl"] [class*="icon-chevron"],
[dir="rtl"] [class*="icon-next"],
[dir="rtl"] [class*="icon-back"] {
  transform: scaleX(-1);
}
```

---

## 7. Animations & Motion in RTL

### Direction-Dependent Animations
Motion that implies navigation direction must flip:

```css
/* Slide in from the right (new page in LTR = new page slides from right) */
/* In RTL, new page slides from LEFT */

@keyframes slide-in-ltr {
  from { transform: translateX(100%); }
  to   { transform: translateX(0); }
}

@keyframes slide-in-rtl {
  from { transform: translateX(-100%); }
  to   { transform: translateX(0); }
}

[dir="ltr"] .page-enter { animation: slide-in-ltr 250ms ease-out; }
[dir="rtl"] .page-enter { animation: slide-in-rtl 250ms ease-out; }
```

### Swipe Gestures
```
LTR: Swipe LEFT = go forward / next
RTL: Swipe RIGHT = go forward / next

LTR: Swipe RIGHT = go back
RTL: Swipe LEFT = go back
```
This must be implemented in JavaScript gesture handlers — not just CSS.

### Drawer/Panel Animations
```
LTR: Sidebar slides in from LEFT
RTL: Sidebar slides in from RIGHT

LTR: Action sheet dismisses to RIGHT (off-screen)
RTL: Action sheet dismisses to LEFT (off-screen)
```

### Skeleton Loading Direction
```css
/* LTR skeleton shimmer: left → right */
@keyframes shimmer-ltr {
  from { background-position: -200px 0; }
  to   { background-position: calc(200px + 100%) 0; }
}

/* RTL skeleton shimmer: right → left */
@keyframes shimmer-rtl {
  from { background-position: calc(200px + 100%) 0; }
  to   { background-position: -200px 0; }
}

[dir="rtl"] .skeleton {
  animation: shimmer-rtl 1.5s infinite;
}
```

### Reduced Motion (always include)
```css
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    transition-duration: 0.01ms !important;
  }
}
```

---

## 8. Input & Keyboard Behavior

### Text Input Defaults
```html
<!-- Arabic text input -->
<input
  type="text"
  dir="auto"          <!-- Automatically detects LTR/RTL based on first character -->
  lang="ar"
  placeholder="ابحث هنا..."
  inputmode="text"
/>

<!-- Always-LTR inputs (email, phone, URL) -->
<input type="email" dir="ltr" />
<input type="tel"   dir="ltr" inputmode="tel" />
<input type="url"   dir="ltr" />
<input type="number" dir="ltr" />
```

### The `dir="auto"` Rule
For text inputs where user might type in either language, use `dir="auto"`. The browser detects based on first strongly-typed character:
- If user types Arabic letter first → field goes RTL
- If user types Latin letter first → field goes LTR

### Cursor and Caret
- In RTL inputs, text cursor starts on the right
- Backspace deletes characters to the left (from caret's perspective, which is the correct behavior)
- Home key goes to right end; End key goes to left end

---

## 9. Formatting — Dates, Currency, Units

### Date Format (Saudi Arabia)
```
Gregorian format: DD/MM/YYYY  (not MM/DD/YYYY)
Hijri format: Used in formal/government contexts only
Full: ١٢ أبريل ٢٠٢٤ or 12 أبريل 2024
Short: 12/04/2024 (LTR always)
```

### Currency
```
Format:   SAR 45.99  or  45.99 ريال
Symbol:   ر.س (Arabic) or SAR (Latin)
Position: Currency symbol before number in LTR, after in RTL context
          In RTL: ٤٥.٩٩ ريال (number on right, currency label on left)
```

### Percent Signs
```
LTR: 85%
RTL: ٪85  (percent sign goes to left of number in RTL)
     or just use: 85% (Western format, universally understood in Saudi tech)
```

---

## 10. Cultural Considerations — Saudi Arabia

### Color Meanings (Saudi/Arabic context)
```
Green:   Islamic significance; positive, go, success, health
Gold:    Luxury, premium, royal connotations
White:   Purity, cleanliness
Black:   Elegance (not death in Arabic culture, unlike Western funerary associations)
Red:     Warning, error, danger (similar to Western context); also used for KSA flag
Blue:    Trust, professionalism (tech context)
Purple:  Luxury, wisdom; less common than in Western apps
```

### Imagery Guidelines
- No images of alcohol, gambling, or pork products
- Modest dress in lifestyle/fashion photography
- Gender-sensitive context: separate sections for men/women where culturally appropriate (e.g., some service categories)
- Respect for religious periods: Ramadan, Hajj season — timing affects UX copy and feature visibility
- Saudi flag usage: follow official KSA guidelines (no distortion, no commercial overuse)

### Ramadan UX Adaptations
During Ramadan, Saudi users have different usage patterns:
- Peak usage: 9pm–3am (after iftar)
- Delivery services need explicit Suhoor time slots
- UI should acknowledge the occasion tastefully (not oversell)
- Dark mode usage increases (evening usage)

### Form Fields — Name Inputs
- Provide separate fields for: First name (الاسم الأول), Father's name (اسم الأب), Last name (اسم العائلة) — Saudi naming convention requires this for formal forms
- Government/official forms: Add National ID (رقم الهوية) field
- Phone: Saudi numbers are 9–10 digits, start with 05 or +966 5

### Arabic Text Writing Guidelines for UX Copy
- Use Modern Standard Arabic (MSA / الفصحى) for formal UI: labels, error messages, legal text
- Saudi dialect (العامية) is acceptable for marketing copy, notifications, casual onboarding
- Avoid Egyptian or Levantine dialect — it reads as foreign to Saudi users
- Test copy with native Saudi Arabic speakers, not just Arabic-speakers generally

---

## 11. Testing & QA for RTL

### RTL Testing Checklist
```
□ dir="rtl" applied at html or content block level
□ All layout components mirror correctly (sidebar, nav, forms)
□ Directional icons are flipped; universal icons are not
□ Numbers display LTR within RTL text
□ Inputs have correct dir="auto" or dir="ltr" as appropriate
□ Animations slide from correct direction
□ Swipe gestures are reversed for RTL
□ Text-align: start/end used (not hardcoded left/right)
□ Logical CSS properties used (margin-inline-start, not margin-left)
□ Letter-spacing: 0 on all Arabic text
□ Arabic font is loaded and rendering (not system fallback)
□ Arabic font is +1–2px larger than Latin equivalent
□ Line-height ≥ 1.6 for Arabic body text
□ No content clipped or overflowing in RTL mode
□ Breadcrumbs show correct RTL order
□ Step indicators progress right-to-left
□ Form errors appear below fields, right-aligned
□ Bilingual language switcher works in both directions
□ Currency and date formats are locale-appropriate
```

### Browser/Device Testing
- Test in Chrome, Safari (critical for iOS)
- Test on actual Arabic keyboard input (iOS Arabic keyboard)
- Test on Samsung devices (common in Saudi Arabia)
- Verify Google Fonts loads correctly (some corporate networks block it — provide fallbacks)

### Fallback Font Stack
```css
/* Arabic with fallbacks */
[dir="rtl"] body {
  font-family: 'Tajawal', 'Cairo', 'Noto Sans Arabic', 'Arabic UI Text',
               'Geeza Pro', system-ui, sans-serif;
}
```

---

## 12. Common RTL Mistakes to Avoid

| Mistake | What Goes Wrong | Fix |
|---------|----------------|-----|
| Only flipping text, not layout | Sidebar stays on left, progress still goes left→right | Mirror the entire layout with dir="rtl" |
| Flipping logos | Brand identity breaks | Never apply scaleX(-1) to logos/brand marks |
| Flipping universal icons | Clock, heart, settings look wrong | Only flip directional/motion icons |
| Using letter-spacing on Arabic | Breaks letter connections (Arabic is cursive) | Set letter-spacing: 0 for all Arabic text |
| Same font size for Arabic and Latin | Arabic looks tiny or oversized | Add 1–2px to Arabic font-size at same weight |
| Hardcoded margin-left | Component breaks in RTL | Use margin-inline-start |
| LTR skeleton shimmer | Loading animation goes wrong direction | Reverse shimmer animation for RTL |
| Placeholder text LTR-aligned | Input feels wrong to Arabic users | Set text-align: right or use dir="auto" |
| Generic Arabic (Egyptian dialect) | Saudi users notice it's not their dialect | Use MSA or Saudi dialect with native reviewer |
| Percent sign position | "٪85" looks wrong (should be "85%" or "٪85") | Test with native speaker |
| Date format MM/DD/YYYY | Saudi users use DD/MM/YYYY | Always use DD/MM/YYYY for Arabic locale |
| Ignoring Hijri calendar | Government/religious app users expect it | Add Hijri date display where relevant |

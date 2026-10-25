# Brand Identity Extraction & Color Scale Generation

## Why This Matters

The visual design must speak the brand's language, not invent a new one. Whether the client has a full brand guide or just a logo color, every visual decision in Phase 5 must trace back to the brand — not designer preference. This reference explains how to extract brand identity from files, ask the right questions when nothing is provided, and generate a complete, usable color system from any brand color.

---

## Step 1: Does the User Have a Brand Identity?

**Always ask this before starting Phase 5.** Use the AskUserQuestion tool with these options:

```
"Do you have brand identity files for this project?"

Options:
A) Yes — I'll upload the brand guide / logo / style sheet now
B) I have some elements (logo, a color or two) but no full guide
C) No — this is a new brand, help me define it
D) Not sure — let me describe the brand and you decide
```

---

## Step 2A — When Files Are Provided (Upload)

Read the uploaded file carefully. Brand identity files may be:
- **PDF brand guide** → extract colors, fonts, logo rules, tone of voice, do/don't examples
- **PNG/JPG logo** → extract dominant colors, infer style (flat, gradient, illustrated, minimal)
- **AI/SVG file** → read any embedded color values or font names mentioned
- **Screenshot of style guide** → read all visible hex values, font names, spacing rules

### What to Extract from Brand Files

```
BRAND EXTRACTION CHECKLIST:

□ Brand name (if not already known)
□ Primary color(s) — exact hex values if available
□ Secondary color(s) — exact hex values
□ Accent color(s) — any highlight or action colors
□ Background color preference (white / off-white / dark / colored)
□ Brand typeface / font name ← look for this specifically
□ Font weights used (e.g., 400, 600, 700)
□ Logo clearspace rules (minimum padding around logo)
□ Tone of voice (formal / friendly / technical / warm / bold)
□ Brand personality adjectives (if stated)
□ Any explicit color DON'Ts (colors to avoid)
□ Any pattern / texture / illustration style
□ Icon style (outlined / filled / rounded / sharp)
□ Button style (pill / rounded / sharp)
```

### Font Rule — One Font Only

**This skill uses a single font family throughout the entire design.** Not two, not three — one. This creates visual cohesion and reduces cognitive load. The font must support multiple weights (at minimum: Regular 400, Medium 500, SemiBold 600, Bold 700) to handle all typographic roles — headings, body, labels, captions — without needing a second family.

**If the brand guide specifies a font:** use it. Confirm it's available on Google Fonts; if not, find the closest Google Fonts equivalent and note the substitution.

**If the brand guide specifies two fonts:** default to the heading/display font as the single font for everything. Mention this simplification to the user.

**If no font is specified in the brand file:** always ask before proceeding (see Font Selection section below).

### If Hex Values Are Not Explicit

If the file only shows colors visually (image):
1. Describe what you see: "The logo appears to use a deep navy blue and a warm coral orange"
2. Assign best-estimate hex values based on visual read
3. Label them clearly as estimated: `(estimated from visual — confirm with client)`
4. Generate the full color scale from these estimates
5. Tell the user: "I've estimated these colors from your file. Please confirm the exact hex values if you have them — I can update the scale instantly."

---

## Font Selection — Always Ask If Not Specified

Regardless of which path the user took (A / B / C / D), if the brand file or description does not include a font name, **always ask before proceeding**. Never choose a font silently.

Present 4-5 curated options based on the brand personality, each with a short description:

```
"Your brand file doesn't specify a font. I need one font family that will be
used for everything — headings, body text, buttons, labels.

Based on your brand direction ([personality adjectives]), here are my top picks:

Option 1: Inter — Clean, neutral, modern. Works at all sizes. Used by Notion, Linear, Vercel.
Option 2: Plus Jakarta Sans — Friendly geometric with personality. Warm but professional.
Option 3: DM Sans — Soft and approachable. Great for consumer apps and wellness products.
Option 4: Sora — Contemporary, tech-forward. Clean with a subtle character.
Option 5: Nunito — Rounded and friendly. Welcoming, great for onboarding flows.

Which feels right for [Project Name]? Or if you have a font in mind, share it and I'll verify it's available."
```

**Curated recommendations by brand direction:**

| Brand Personality | Recommended Font | Why |
|---|---|---|
| Minimal / Corporate / B2B | Inter | Most legible at all sizes, deeply neutral |
| Friendly / Consumer / Wellness | Plus Jakarta Sans or DM Sans | Warmth without sacrificing readability |
| Premium / Luxury | Satoshi or General Sans | Geometric with refined character |
| Bold / Startup / Tech | Sora or Cabinet Grotesk | Distinctive without being loud (⚠️ avoid Space Grotesk — overused by AI tools) |
| Playful / Youth | Nunito or Poppins | Rounded, inviting, casual |
| Classic / Trust / Finance | Manrope | Clean but with subtle traditional cues |
| Arabic-first or Bilingual | Tajawal (supports both Arabic + Latin) | Best bilingual option on Google Fonts |

**For bilingual (Arabic + English) projects — always ask, never assume.**

Even if a brand font is specified, bilingual projects require a separate font decision because the chosen Latin font may not support Arabic glyphs well. Always ask before proceeding:

```
"This project is bilingual (Arabic + English). I need to confirm the font choice
for both languages.

Option A: One font for everything
  These fonts support both Arabic and Latin scripts natively:
  1. Tajawal — Clean, modern, excellent Arabic + Latin. Most versatile choice.
  2. Cairo — Geometric, slightly more stylized than Tajawal.
  3. Noto Sans Arabic — Neutral, highly readable, Google's universal choice.
  4. IBM Plex Sans Arabic — Technical, structured, great for data-heavy apps.

Option B: Two fonts (one per language direction)
  English version uses [Brand Font / ProjectFont]
  Arabic version uses Tajawal (automatically applied to all dir="rtl" content)
  Note: The two fonts will be visually harmonized in size and weight.

Which approach do you prefer for [Project Name]?"
```

After the user selects, confirm:
```
"Using [Font Name] for both Arabic and English throughout the design."
— OR —
"Using [ProjectFont] for English / Tajawal for Arabic. They'll share the same type scale."
```

After the user selects, confirm with:
```
"Using [Font Name] — [Regular 400 / Medium 500 / SemiBold 600 / Bold 700] — for all text across the entire design. Ready to proceed."
```

---

## Step 2B — When Only Partial Brand Elements Exist

Ask focused questions to fill the gaps:

```
"You mentioned you have [logo / a color]. To build a complete design system, I need a few more things:

1. What's the primary brand color? (hex code, or describe it)
2. Is there a secondary color?
3. Does your brand have a specific font? If not, I'll suggest one.
4. How would you describe your brand in 3 words?
5. Are there any colors or styles you want to avoid?"
```

After receiving answers, if no font was specified, immediately follow the Font Selection process above before moving on.

---

## Step 2C — When No Brand Identity Exists (New Brand)

Build the brand identity from scratch based on:
- The product type and category
- The target persona (from Phase 3)
- The competitive landscape (from Phase 2 — what do competitors look like, and how do you differentiate?)
- Any preferences the user has expressed

Ask:
```
"Since this is a new brand, let me help you define the visual direction. A few quick questions:

1. Who is your main competitor visually? (An app or website whose look/feel you like or want to differentiate from)
2. Pick a direction: [Minimal & Clean] / [Bold & Expressive] / [Warm & Human] / [Technical & Precise] / [Playful & Friendly]
3. Dark mode, light mode, or both?
4. Is there a color you feel strongly about — either to use or to avoid?
5. Any brands outside your industry whose visual style you admire?"
```

Then propose a brand direction and confirm before generating the color system.

---

## Step 3: Generate the Full Color Scale (50 → 950)

For **every brand color** (primary, secondary, accent), generate a complete 10-step scale from lightest to darkest. This scale is what gets used as CSS custom properties throughout the entire design system.

### The Scale Formula

Starting from the brand's base color (usually sits around 500-600 on the scale):

```
50   → Nearly white tint (background washes, hover states)
100  → Very light tint (card backgrounds, subtle fills)
200  → Light tint (disabled states, borders on light bg)
300  → Medium-light (placeholder text, inactive icons)
400  → Medium (secondary text, less prominent elements)
500  → Base color (the brand color itself — or close to it)
600  → Slightly darker (hover state for primary buttons)
700  → Darker (active/pressed states)
800  → Dark (text on light backgrounds)
900  → Very dark (high contrast text, dark backgrounds)
950  → Near black tint of the color (deepest use)
```

### How to Derive Each Step

For each shade, calculate by adjusting HSL:
- **50–400**: Increase lightness significantly (mix toward white), reduce saturation slightly
- **500**: The brand color (L as-is)
- **600–950**: Decrease lightness progressively, can increase saturation slightly for richness

**Example for a brand primary of `#4F6EF7` (a medium blue):**

```
PRIMARY SCALE — Blue
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

--primary-50:   #EEF2FF   ← Near white, barely blue
--primary-100:  #E0E7FF   ← Soft blue wash
--primary-200:  #C7D2FE   ← Light, gentle blue
--primary-300:  #A5B4FC   ← Clearly blue, still light
--primary-400:  #818CF8   ← Medium-light, visible
--primary-500:  #6366F1   ← Brand base color (or nearest)
--primary-600:  #4F46E5   ← Hover state for buttons
--primary-700:  #4338CA   ← Active/pressed
--primary-800:  #3730A3   ← Dark text on light bg
--primary-900:  #312E81   ← Very dark, high contrast
--primary-950:  #1E1B4B   ← Near black
```

**Example for a brand color of `#E8612C` (orange):**

```
SECONDARY SCALE — Orange
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

--secondary-50:   #FFF7ED
--secondary-100:  #FFEDD5
--secondary-200:  #FED7AA
--secondary-300:  #FDBA74
--secondary-400:  #FB923C
--secondary-500:  #F97316   ← Base (brand color)
--secondary-600:  #EA6C1A   ← Hover
--secondary-700:  #C2510E
--secondary-800:  #9A3412
--secondary-900:  #7C2D12
--secondary-950:  #431407
```

### CSS Custom Properties Output Format

After generating the scale, output it as ready-to-use CSS variables:

```css
:root {
  /* ─── PRIMARY: [Color Name] ─── */
  --primary-50:  #[hex];
  --primary-100: #[hex];
  --primary-200: #[hex];
  --primary-300: #[hex];
  --primary-400: #[hex];
  --primary-500: #[hex];   /* Brand base */
  --primary-600: #[hex];   /* Hover */
  --primary-700: #[hex];   /* Active */
  --primary-800: #[hex];
  --primary-900: #[hex];
  --primary-950: #[hex];

  /* ─── SECONDARY: [Color Name] ─── */
  --secondary-50:  #[hex];
  --secondary-100: #[hex];
  --secondary-200: #[hex];
  --secondary-300: #[hex];
  --secondary-400: #[hex];
  --secondary-500: #[hex];   /* Brand base */
  --secondary-600: #[hex];   /* Hover */
  --secondary-700: #[hex];   /* Active */
  --secondary-800: #[hex];
  --secondary-900: #[hex];
  --secondary-950: #[hex];

  /* ─── NEUTRAL (Gray) ─── */
  /* If brand is cool-toned, tint grays slightly toward the primary hue */
  --gray-50:  #[hex];
  --gray-100: #[hex];
  --gray-200: #[hex];
  --gray-300: #[hex];
  --gray-400: #[hex];
  --gray-500: #[hex];
  --gray-600: #[hex];
  --gray-700: #[hex];
  --gray-800: #[hex];
  --gray-900: #[hex];
  --gray-950: #[hex];

  /* ─── SEMANTIC ─── */
  --success-500: #[hex];
  --success-100: #[hex];   /* Light bg for success states */
  --warning-500: #[hex];
  --warning-100: #[hex];
  --error-500:   #[hex];
  --error-100:   #[hex];   /* Light bg for error states */
  --info-500:    #[hex];
  --info-100:    #[hex];

  /* ─── SEMANTIC ALIASES (for practical use in components) ─── */
  --color-primary:         var(--primary-500);
  --color-primary-hover:   var(--primary-600);
  --color-primary-active:  var(--primary-700);
  --color-primary-subtle:  var(--primary-50);
  --color-primary-light:   var(--primary-100);

  --color-text-primary:    var(--gray-900);
  --color-text-secondary:  var(--gray-700);
  --color-text-tertiary:   var(--gray-500);
  --color-text-disabled:   var(--gray-400);
  --color-text-inverse:    #ffffff;

  --color-bg-page:         var(--gray-50);
  --color-bg-card:         #ffffff;
  --color-bg-overlay:      var(--gray-100);

  --color-border:          var(--gray-200);
  --color-border-strong:   var(--gray-300);
}
```

---

## Step 4: Present the Brand System to the User

Before using it in any screen, show the user a visual representation of the full color system:

```
## 🎨 Brand Color System — [Project Name]

Extracted from: [brand guide / logo file / defined from brief]

PRIMARY — [Color Name] ([Base Hex])
■■ 50   ■■ 100   ■■ 200   ■■ 300   ■■ 400
■■ 500* ■■ 600   ■■ 700   ■■ 800   ■■ 900   ■■ 950
(* = brand base color)

SECONDARY — [Color Name] ([Base Hex])
■■ 50   ■■ 100   ■■ 200   ■■ 300   ■■ 400
■■ 500* ■■ 600   ■■ 700   ■■ 800   ■■ 900   ■■ 950

NEUTRAL — Gray
■■ 50   ■■ 100   ■■ 200   ■■ 300   ■■ 400
■■ 500  ■■ 600   ■■ 700   ■■ 800   ■■ 900   ■■ 950

SEMANTIC
✅ Success: [hex]    ⚠️ Warning: [hex]
❌ Error: [hex]      ℹ️ Info: [hex]

TYPOGRAPHY
Heading: [Font Name] — [personality description]
Body: [Font Name] — [personality description]

Confirm this system before I apply it to all screens?
[Yes, proceed] / [I want to adjust X]
```

Wait for user confirmation before proceeding to screen design.

---

## Step 5: Apply Brand System Throughout

Once confirmed, this brand system governs **every single design decision**:

| Element | Which token to use |
|---------|-------------------|
| Primary CTA button bg | `--color-primary` (500) |
| CTA hover | `--primary-600` |
| CTA pressed | `--primary-700` |
| Link color | `--primary-600` |
| Page background | `--color-bg-page` (gray-50) |
| Card background | `--color-bg-card` (white) |
| Body text | `--color-text-primary` (gray-900) |
| Secondary text | `--color-text-secondary` (gray-700) |
| Placeholder | `--color-text-disabled` (gray-400) |
| Border | `--color-border` (gray-200) |
| Input focus ring | `--primary-500` with 3px offset |
| Error state | `--error-500` border + `--error-100` bg |
| Success state | `--success-500` border + `--success-100` bg |
| Subtle highlight | `--color-primary-subtle` (primary-50) |
| Badge / tag bg | `--primary-100`, text: `--primary-700` |
| Icon (active) | `--color-primary` |
| Icon (inactive) | `--gray-400` |

**Never hard-code a hex value directly in component CSS — always use the token.**
This ensures global color changes take one line to update.

---

## Arabic / RTL Considerations for Brand Colors

When rendering the Arabic version of the UI:
- Color system stays identical — brand colors don't change with language
- Semantic colors stay the same (error is still red, success is still green)
- The only change is layout direction (RTL) and typography font (Tajawal)
- If the brand has Arabic typography specified in their guide, use it; otherwise default to Tajawal matching the heading weight

---

## Brand Color Accessibility Check

For each primary and secondary color, verify WCAG compliance:

```
ACCESSIBILITY CHECK — [Color Name]

Text on white background:
  [Color]-500 on #ffffff: contrast ratio [X.XX]:1 → [Pass AA / Fail]
  [Color]-600 on #ffffff: contrast ratio [X.XX]:1 → [Pass AA / Fail]
  [Color]-700 on #ffffff: contrast ratio [X.XX]:1 → [Pass AA / Fail]

White text on color:
  #ffffff on [Color]-500: contrast ratio [X.XX]:1 → [Pass AA / Fail]
  #ffffff on [Color]-600: contrast ratio [X.XX]:1 → [Pass AA / Fail]

Recommendation:
  Use [Color]-[shade] for text on white backgrounds (meets 4.5:1)
  Use white text on [Color]-[shade]+ backgrounds (meets 4.5:1)
```

If the brand's primary color fails AA at 500, note this and recommend using a darker shade for text/interactive elements while keeping the lighter shade for decorative use.

## Typescale Ratio — Always Ask the User

**Always ask the user which typescale ratio to use before generating the typography system.** The ratio determines how much size difference exists between each level of the type scale. A tighter ratio (1.067) gives subtle, elegant hierarchy. A wider ratio (1.618) gives dramatic, expressive hierarchy.

Use the AskUserQuestion tool to ask:

```
"Which typescale ratio should I use for [Project Name]?

The base size is 16px for body text. Here are your options — each ratio determines how
dramatically sizes increase between levels:

1. 1.067 — Minor Second   → Subtle, very tight. Best for: dense dashboards, data-heavy apps
2. 1.125 — Major Second   → Gentle hierarchy. Best for: enterprise tools, professional apps
3. 1.200 — Minor Third    → Balanced and versatile. Best for: most digital products
4. 1.250 — Major Third    → Clear, readable hierarchy. Best for: editorial, marketing sites
5. 1.333 — Perfect Fourth → Strong visual rhythm. Best for: content-heavy sites, blogs
6. 1.414 — Augmented Fourth → Expressive. Best for: creative portfolios, brand landing pages
7. 1.500 — Perfect Fifth  → Very dramatic. Best for: bold marketing, hero-focused pages
8. 1.618 — Golden Ratio   → Maximum contrast. Best for: luxury brands, artistic products

Which feels right for your project? (Recommended: 1.200 for apps, 1.333 for content sites)"
```

After the user selects a ratio, **calculate and output the full type scale** using the formula:
- Scale level = 16px × ratio^n (where n = position above base: 0, 1, 2, 3, 4, 5, 6)
- Below base: 16px ÷ ratio^n

### Pre-Calculated Type Scales

Use these pre-calculated values — round to nearest whole pixel:

---

**Ratio 1.067 — Minor Second** *(best for: dense dashboards, compact UIs)*

| Level | Size | Line Height | Weight | Usage |
|-------|------|-------------|--------|-------|
| Display | 24px | 32px | 700 | Hero, splash |
| H1 | 22px | 30px | 700 | Page title |
| H2 | 21px | 28px | 600 | Section title |
| H3 | 19px | 26px | 600 | Sub-section |
| H4 | 18px | 26px | 600 | Card title |
| Body Large | 17px | 26px | 400 | Intro text |
| Body | 16px | 24px | 400 | Main content |
| Body Small | 15px | 22px | 400 | Secondary text |
| Caption | 14px | 20px | 400 | Labels, captions |
| Label | 12px | 16px | 500 | Uppercase tags |

---

**Ratio 1.125 — Major Second** *(best for: professional tools, B2B apps)*

| Level | Size | Line Height | Weight | Usage |
|-------|------|-------------|--------|-------|
| Display | 32px | 40px | 700 | Hero, splash |
| H1 | 29px | 36px | 700 | Page title |
| H2 | 26px | 34px | 600 | Section title |
| H3 | 23px | 30px | 600 | Sub-section |
| H4 | 20px | 28px | 600 | Card title |
| Body Large | 18px | 28px | 400 | Intro text |
| Body | 16px | 24px | 400 | Main content |
| Body Small | 14px | 20px | 400 | Secondary text |
| Caption | 13px | 18px | 400 | Labels, captions |
| Label | 11px | 16px | 500 | Uppercase tags |

---

**Ratio 1.200 — Minor Third** *(best for: most digital products — recommended default)*

| Level | Size | Line Height | Weight | Usage |
|-------|------|-------------|--------|-------|
| Display | 48px | 56px | 700 | Hero, splash |
| H1 | 40px | 48px | 700 | Page title |
| H2 | 33px | 40px | 600 | Section title |
| H3 | 28px | 36px | 600 | Sub-section |
| H4 | 23px | 30px | 600 | Card title |
| Body Large | 19px | 28px | 400 | Intro text |
| Body | 16px | 24px | 400 | Main content |
| Body Small | 13px | 20px | 400 | Secondary text |
| Caption | 11px | 16px | 400 | Labels, captions |
| Label | 12px | 16px | 500 | Uppercase tags |

---

**Ratio 1.250 — Major Third** *(best for: editorial, marketing sites)*

| Level | Size | Line Height | Weight | Usage |
|-------|------|-------------|--------|-------|
| Display | 61px | 68px | 700 | Hero, splash |
| H1 | 49px | 56px | 700 | Page title |
| H2 | 39px | 48px | 600 | Section title |
| H3 | 31px | 40px | 600 | Sub-section |
| H4 | 25px | 32px | 600 | Card title |
| Body Large | 20px | 30px | 400 | Intro text |
| Body | 16px | 24px | 400 | Main content |
| Body Small | 13px | 20px | 400 | Secondary text |
| Caption | 10px | 16px | 400 | Labels, captions |
| Label | 12px | 16px | 500 | Uppercase tags |

*Note: Caption at 10px is below recommended minimum (12px). Use 12px for Caption and Label regardless of ratio output.*

---

**Ratio 1.333 — Perfect Fourth** *(best for: content sites, blogs, landing pages)*

| Level | Size | Line Height | Weight | Usage |
|-------|------|-------------|--------|-------|
| Display | 57px | 64px | 700 | Hero, splash |
| H1 | 42px | 52px | 700 | Page title |
| H2 | 32px | 40px | 600 | Section title |
| H3 | 24px | 32px | 600 | Sub-section |
| H4 | 21px | 28px | 600 | Card title (capped) |
| Body Large | 18px | 28px | 400 | Intro text (capped) |
| Body | 16px | 24px | 400 | Main content |
| Body Small | 12px | 18px | 400 | Secondary text |
| Caption | 12px | 16px | 400 | Labels, captions |
| Label | 12px | 16px | 500 | Uppercase tags |

*Note: H3 and below are capped/adjusted for practical readability in dense UI.*

---

**Ratio 1.414 — Augmented Fourth** *(best for: creative portfolios, brand pages)*

| Level | Size | Line Height | Weight | Usage |
|-------|------|-------------|--------|-------|
| Display | 64px | 72px | 700 | Hero only |
| H1 | 45px | 52px | 700 | Page title |
| H2 | 32px | 40px | 600 | Section title |
| H3 | 23px | 30px | 600 | Sub-section |
| H4 | 18px | 26px | 600 | Card title (adjusted) |
| Body Large | 18px | 28px | 400 | Intro text |
| Body | 16px | 24px | 400 | Main content |
| Body Small | 13px | 20px | 400 | Secondary text |
| Caption | 12px | 16px | 400 | Labels, captions |
| Label | 12px | 16px | 500 | Uppercase tags |

---

**Ratio 1.500 — Perfect Fifth** *(best for: bold marketing, hero-focused pages)*

| Level | Size | Line Height | Weight | Usage |
|-------|------|-------------|--------|-------|
| Display | 81px | 88px | 700 | Hero only |
| H1 | 54px | 60px | 700 | Page title |
| H2 | 36px | 44px | 600 | Section title |
| H3 | 24px | 32px | 600 | Sub-section |
| H4 | 18px | 26px | 600 | Card title (adjusted) |
| Body Large | 18px | 28px | 400 | Intro text |
| Body | 16px | 24px | 400 | Main content |
| Body Small | 12px | 18px | 400 | Secondary text |
| Caption | 12px | 16px | 400 | Labels, captions |
| Label | 12px | 16px | 500 | Uppercase tags |

*Note: Display and H1 are very large — best used sparingly for hero sections only.*

---

**Ratio 1.618 — Golden Ratio** *(best for: luxury brands, artistic products)*

| Level | Size | Line Height | Weight | Usage |
|-------|------|-------------|--------|-------|
| Display | 68px | 76px | 700 | Hero only |
| H1 | 42px | 52px | 700 | Page title |
| H2 | 26px | 34px | 600 | Section title |
| H3 | 20px | 28px | 600 | Sub-section (adjusted) |
| H4 | 18px | 26px | 600 | Card title (adjusted) |
| Body Large | 18px | 28px | 400 | Intro text |
| Body | 16px | 24px | 400 | Main content |
| Body Small | 12px | 18px | 400 | Secondary text |
| Caption | 12px | 16px | 400 | Labels, captions |
| Label | 12px | 16px | 500 | Uppercase tags |

*Note: The extreme top of the scale is impractical for most UI. H3 and H4 are adjusted to stay usable.*

---

### Output the Type Scale as CSS Custom Properties

Once the user selects a ratio, output the complete type scale as CSS variables:

```css
:root {
  /* ─── TYPOGRAPHY — Ratio: [ratio] ([ratio name]) ─── */
  --font-family: '[Font Name]', sans-serif;

  --text-display: [size]px;
  --text-h1:      [size]px;
  --text-h2:      [size]px;
  --text-h3:      [size]px;
  --text-h4:      [size]px;
  --text-body-lg: [size]px;
  --text-body:    [size]px;    /* Base: 16px */
  --text-body-sm: [size]px;
  --text-caption: [size]px;
  --text-label:   [size]px;

  --leading-display: [line-height]px;
  --leading-h1:      [line-height]px;
  --leading-h2:      [line-height]px;
  --leading-h3:      [line-height]px;
  --leading-h4:      [line-height]px;
  --leading-body-lg: [line-height]px;
  --leading-body:    24px;
  --leading-body-sm: [line-height]px;
  --leading-caption: [line-height]px;
}
```

### Typescale Rules (Always Apply)

```
□ Body text never below 14px (accessibility minimum)
□ Caption/Label never below 12px regardless of ratio calculation
□ Line height: always between 1.4x and 1.6x the font size for body text
□ Headings: 1.1x to 1.3x the font size (tighter)
□ One font family — all levels use the same font, differentiated by size + weight only
□ Display size: used only for hero sections, not repeating page elements
□ Never use more than 3 type sizes on a single screen
□ Establish hierarchy through size AND weight — never size alone
```

After presenting the type scale, wait for user confirmation before using it in Phase 5.

---

## Anti-Generic Aesthetics Filter

Before accepting any visual reference as inspiration, apply this filter — reject or flag.

> **Why this matters**: AI tools (including Claude) default to predictable visual patterns when not constrained. These patterns are nicknamed "AI slop" — technically competent but visually indistinguishable. The rules below break Claude out of these defaults.

**Forbidden font choices** (signal generic AI output):
- Inter, Roboto, Arial, or system-ui used as the headline/display font — they read as "AI default"
- **Space Grotesk** — was distinctive in 2021, now overused by AI-generated interfaces
- Any font chosen without explaining WHY it fits this specific brand personality

**Forbidden color choices**:
- Purple or blue gradient on white as the primary visual — most common AI output pattern
- AI purple/pink gradient (indigo-to-fuchsia) — avoid for any non-gaming product
- Flat pastel gradients with no connection to the product's personality
- Generic teal/orange combos without product rationale

**Forbidden layout patterns**:
- Centered hero headline + single CTA button on solid white — no hierarchy surprise
- Cards-on-white grid with perfectly equal spacing throughout
- Stock photo header with headline overlay and sub-text below
- Predictable left-text / right-image alternating sections
- Every section uses the same visual weight — no contrast of scale or density

**Forbidden UI patterns**:
- Rounded pill buttons used everywhere without variation
- Shadow cards with identical border-radius on every element
- "Clean and minimal" as the only stated differentiator — this describes nothing
- Scattered micro-interactions on every element — unfocused, no hierarchy of moments
- Gradient backgrounds without texture, grain, or depth — flat and dimensionless

**Anti-AI-Slop positives** — what makes a design feel distinctly intentional:
- A font nobody expects for this product category — with a clear reason
- One dominant color used boldly, not distributed timidly at 10% everywhere
- A spatial composition decision: asymmetry, overlap, diagonal flow, or grid-breaking elements
- One well-orchestrated page-load animation — instead of scattered micro-interactions
- Visual texture: grain overlay, mesh gradient, noise, or geometric pattern behind content
- A layout moment that creates surprise — generous negative space, oversized typography, or deliberate density

If a reference shows forbidden patterns, mark it: "⚠️ AI Slop — extract the concept only, not the execution."

---

## The Differentiation Question

After style selection, push the user to answer: **"What is the one thing the user will remember from this design?"**

The answer must be **specific**. Push back if vague:
- ❌ "It looks clean" → Not enough. What makes it *this* product's clean?
- ❌ "It's minimal" → Minimal how? Every SaaS claims minimal. What's unexpected?
- ✅ "The dashboard uses a bento grid with one bold oversized metric card that dominates the hero"
- ✅ "Dark mode with a warm amber accent — unusual for a productivity tool"
- ✅ "Brutalist typography on white — every screen feels like a printed editorial poster"

Write the answer as a **Design Direction Statement** and carry it through all subsequent phases.

**Implementation complexity must match aesthetic vision:**
- Maximalist / expressive → elaborate: layered effects, textured backgrounds, orchestrated animations, grid-breaking elements
- Minimalist / restrained → precise: exact spacing, deliberate whitespace, subtle micro-details, restrained palette
- Never produce flat, generic code for a maximalist concept, or cluttered code for a minimalist vision

---

## Font Pairing Guidance

| Product Type | Pairing Pattern | Example |
|---|---|---|
| SaaS / B2B | Geometric Sans + Same family lighter weight | Inter Bold / Inter Regular |
| Editorial / Blog | Serif heading + Sans body | Playfair Display / Source Sans |
| Dashboard / Data | Tabular Sans heading + Mono for numbers | IBM Plex Sans / IBM Plex Mono |
| Mobile App | Rounded Sans + Same family | Nunito / Nunito Light |
| Luxury / Minimal | Thin Serif + Light Sans | Cormorant / Neue Haas Grotesk |
| Developer Tools | Mono heading + Sans body | JetBrains Mono / Inter |

Typography rules: base 16px minimum for body · line-height 1.5–1.75 · use font-weight 400 body / 500 labels / 600–700 headings · avoid `letter-spacing` on body text · use tabular/monospaced figures for data tables, prices, and timers · always test Arabic with the chosen font.

---

## Industry Color Direction

Suggest palette category before defining exact values:

| Industry | Palette Direction |
|---|---|
| Health / Medical | Blues + greens — trust, calm, hygiene |
| Finance / Fintech | Deep blues + golds — stability, authority |
| E-commerce | Warm neutrals + accent red/orange — energy, action |
| SaaS / Productivity | Cool grays + single vivid accent — focus, clarity |
| Education | Blues + warm yellows — optimism, knowledge |
| Creative / Agency | High contrast + unexpected accent — personality |
| Food & Lifestyle | Earth tones + warm oranges — appetite, warmth |

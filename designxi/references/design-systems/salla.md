# Salla — full design-system reference (merchant store themes)

The Salla merchant store theme design system, read page by page from the Figma community file
**"Salla merchants websites design template"** (`6tCYXU2MnUJtcuS69Ks5AV`, 9 pages: Cover, Welcome,
Design Desktop UI, Design Responsive, Store Image, Guidelines, Components).

**Purpose**: template for building **Salla e-commerce store themes**. Arabic **RTL**. The Welcome page
asks theme makers to define *why* they're building the theme, the target niche, and the must-have
features — do that framing in Phase 1–4 when a project is a Salla theme.

**When to use**: any Salla storefront theme, or an Arabic RTL e-commerce store wanting the Salla look.
Apply `references/rtl-arabic.md` throughout (this system is RTL-native).

---

## Colors (variables collection "01 - Color")

```css
/* Primary — mint */
--primary:#62d0b6; /* base */
--primary-50:#e0f6f0; --primary-100:#d0f1e9; --primary-200:#c0ece2; --primary-300:#a1e3d3;
--primary-400:#91decc; --primary-500:#81d9c5; /* hover */ --primary-600:#72d5be;
--primary-700:#52cbaf; --primary-800:#43c7a8; --primary-900:#38bc9e;
/* Neutrals */
--white:#ffffff; --gray-50:#f8f8f8; --gray-100:#eeeeee; --gray-200:#d6d6d6; --gray-300:#a5a5a5;
--gray-400:#666666; --gray-500:#444444; --gray-600:#333333; --bg-dark:#1d1f1f;
/* Status */
--success:#00af6c;  /* 100 #ccf2e4 … 600 #008c56 */
--info:#5196f3;     /* 100 #dceafd … 600 #417ac8 */
--warning:#ffaf44;  /* 100 #ffefda … 600 #d18f36 */  --rating-star:#ffc62a;
--danger:#f55157;   /* 100 #fddcdd … 600 #ca4146 */
```

> **Known trap**: the Guidelines page text claims primary is `#0989FF`, but the variables **and every
> design** use the mint `#62d0b6`. Use the mint — ignore the `#0989FF` note.

**Color usage**: headings `#333333` · body/secondary `#666666` · placeholders/meta `#a5a5a5` · borders
`#eeeeee` · section bg `#f8f8f8` · links / active / price accent `#62d0b6` · sale / out-of-stock
`#f55157` · dark sections `#1d1f1f`.

---

## Typography — **DIN Next LT Arabic** (Regular, Medium, Bold)

Format `size/line-height` in px.

- **Headings**: H1 48/70 · H2 36/50 · H3 24/35 · H4 20/30 · H5 18/25. Extra display titles 56 and 96
  Bold. Bold and Medium sets exist for 14–48.
- **Body**: 24 · 20/30 · 16/25 (or /24) · 14/20 · small 13 · 12/17 · 10. Button text 16/24 Medium
  (14 Regular on the small button).
- Line height ≈ 1.4–1.45× the font size.
- **Most used in designs**: 14 Regular, 16 Regular, 16 Medium, 18 Medium, 13 Regular.

---

## Spacing (variables "03 - Spacing") — 8px rhythm after 8

```
sm 2 · md 4 · lg 8 · xl 16 · 2xl 24 · 3xl 32 · 4xl 40 · 5xl 48 · 6xl 56 · 7xl 64 · 8xl 72 · 9xl 80 ·
10xl 88 · 11xl 96
```
- **Most used gaps**: 8, 16, 4, 24, 32, 48.
- Card / input padding 16 · section padding 24–56 · banner content gap 96 · products-section gap 32 ·
  banner-section gap 48.

---

## Grid
- **Desktop**: frame 1600, 12 columns, gutter 24, side margin 200 → content 1200.
- **Responsive**: frame 428, content 396 (16 side margins).

---

## Radius (variables "02 - Radius") & shadow
- **Radius**: Sm **4** (default for buttons, inputs, cards — by far the most used) · Md 8 · Lg 16 ·
  Xl 24 · Xxl 32 · circular for arrow and collapse buttons.
- **Shadow**: one only — y5, blur 20, black 6%.

---

## Components

### Buttons
- Heights: **56** (pad 16, text 16 Medium) and **42** (pad 10/16, text 14). Gap 8. Radius 4.
- Types: Primary (mint, hover `#81d9c5`) · Secondary (`#1d1f1f`, hover `#444444`) · Danger (red).
  States Default / Hover / Pressed / Disabled. Plus Outline, With-icon, Icon-only.

### Inputs
- Box 48 high, pad 14/16, radius 4, border `#eeeeee`, text 13.
- Label 14 Medium `#333333` + optional tag 13 `#a5a5a5`; description 12 `#a5a5a5`. Label-block gap 2,
  field gap 8.
- States: hover/typing border mint · disabled bg `#f8f8f8` · success border `#00af6c` · error border
  `#f55157`. Textarea variant. Icons 16 inside; currency prefix.

### Toggles & small controls
- Checkbox/radio 18 · switch 32×20 · arrow buttons 46 circle (white + `#eeeeee` border, active mint) ·
  collapse 32 circle.
- **Tabs** 56 high: active = mint fill + white text; inactive `#666666`.

### Header / footer / nav
- Top bar 40 (pad 8/200, light `#f8f8f8` or dark) · main header 160 · footer 499 with top-footer 133
  (pad 24/200), light/dark, optional maps · mobile navbar 182, mobile footer.

### Product & commerce cards
- **Product card** 278×558 (mobile 189), radius 4, border `#eeeeee`, hover border mint; dark version;
  out-of-stock and discount badges.
- **Medium product card** 585×309 with 2px mint border. **Product ad** 390×489, pad 32/56, bg `#f8f8f8`.
- Cart row 922×112 (pad 16, gap 32) · filter panel 265 wide (pad 16) · category tile 135×206 · brand
  tile 204×110 (pad 24, hover border `#84a9ff`) · review card 380 (pad 24) · feature card 380×123
  (pad 32) · blog card 380 · breadcrumb 57 high.
- Section title with an "عرض الكل" link in mint · pagination numbers + show-more button · rating stars
  13 (gap 2) · list/grid toggle 34 · quantity selector · price (24 Bold, old price 20 `#a5a5a5`) ·
  product-customization accordion · BNPL payment logos (Tamara, Tabby, Spotii).
- Icons: 24 line set · feature icons 40.

---

## Page templates
- **Required pages**: Home · Product page · Products collection. **Optional**: Cart · Blog · Customers ·
  Thank you · Brands.
- **Desktop designs**: Home 1600×9742 (header → banner slider → features → banners → products → banner …)
  · All products (empty / grid / menu) · Product details (details / features / comments / customization)
  · Cart. Responsive versions at 428 width, plus Filter, Category, Profile.
- **Store image**: theme store thumbnails 1366×768 (web + mobile mockups); thumbnail template 600×550.

# Output Templates — HTML Delivery Package

## Overview

All outputs are delivered as standalone HTML files that work without any server or build step. Users should be able to double-click any file and open it in a browser.

File structure to produce:
```
[project-name]/
├── index.html        → Project hub & navigation
├── casestudy.html    → Full UX case study (comprehensive)
├── screens.html      → All designed UI screens (interactive prototype)
├── process.html      → UX thinking & rationale
├── personas.html     → Persona cards
└── handoff.html      → Developer handoff documentation
```

---

## Bilingual Structure (Required in Every File)

Every HTML file must include a language switcher and full content in both English and Arabic.

```html
<!--
  Font import rule: ONE font only.
  If the project font is NOT Tajawal, import both as subsets of the same declaration:
  - [ProjectFont] for Latin (ltr content)
  - Tajawal for Arabic (rtl content) — Tajawal covers both Arabic AND Latin well
  If the project font IS Tajawal, import once for both directions.
-->

<!-- Option A: Project font is Tajawal (bilingual with one import) -->
<link href="https://fonts.googleapis.com/css2?family=Tajawal:wght@400;500;600;700&display=swap" rel="stylesheet">

<!-- Option B: Project font is [Other Font] — import both but treat as one typographic system -->
<link href="https://fonts.googleapis.com/css2?family=[ProjectFont]:wght@400;500;600;700&family=Tajawal:wght@400;500;600;700&display=swap" rel="stylesheet">
<!-- In this case: use [ProjectFont] in ltr content, Tajawal only in dir="rtl" blocks -->
<!-- Do NOT mix them in the same language direction -->

<!-- Language Switcher -->
<div class="lang-switcher">
  <button class="lang-btn active" onclick="setLang('en', this)">English</button>
  <button class="lang-btn" onclick="setLang('ar', this)">العربية</button>
</div>

<!-- English Block -->
<div id="content-en" class="lang-block">
  <!-- All English content here, dir="ltr" -->
</div>

<!-- Arabic Block -->
<div id="content-ar" class="lang-block" style="display:none;" dir="rtl">
  <!-- All Arabic content here, dir="rtl", font-family: Tajawal -->
</div>

<script>
function setLang(lang, btn) {
  document.querySelectorAll('.lang-block').forEach(el => el.style.display = 'none');
  document.getElementById('content-' + lang).style.display = 'block';
  document.querySelectorAll('.lang-btn').forEach(b => b.classList.remove('active'));
  btn.classList.add('active');
}
</script>
```

CSS for the switcher:
```css
.lang-switcher {
  display: flex;
  gap: 8px;
  justify-content: flex-end;
  padding: 16px 24px;
  background: white;
  border-bottom: 1px solid var(--gray-200);
  position: sticky;
  top: 0;
  z-index: 100;
}
.lang-btn {
  padding: 6px 16px;
  border: 1px solid var(--gray-200);
  border-radius: var(--radius-pill);
  background: white;
  cursor: pointer;
  font-size: 0.875rem;
  font-weight: 500;
  color: var(--gray-700);
  transition: all 0.15s;
}
.lang-btn.active {
  background: var(--color-primary);
  color: white;
  border-color: var(--color-primary);
}
/* Arabic typography */
[dir="rtl"] {
  font-family: 'Tajawal', sans-serif;
}
```

---

## Shared CSS Design System

Include this at the top of every HTML file (inside `<style>` tags). Replace the [placeholders] with the actual values defined in Phase 5.

```css
/* DesignXI Design System Tokens */
:root {
  /* Colors — full scales from Phase 4.8 */
  --primary-50:  [hex]; --primary-100: [hex]; --primary-200: [hex];
  --primary-300: [hex]; --primary-400: [hex]; --primary-500: [hex];
  --primary-600: [hex]; --primary-700: [hex]; --primary-800: [hex];
  --primary-900: [hex]; --primary-950: [hex];

  --secondary-50:  [hex]; --secondary-100: [hex]; --secondary-200: [hex];
  --secondary-300: [hex]; --secondary-400: [hex]; --secondary-500: [hex];
  --secondary-600: [hex]; --secondary-700: [hex]; --secondary-800: [hex];
  --secondary-900: [hex]; --secondary-950: [hex];

  --gray-50: [hex]; --gray-100: [hex]; --gray-200: [hex];
  --gray-300: [hex]; --gray-400: [hex]; --gray-500: [hex];
  --gray-600: [hex]; --gray-700: [hex]; --gray-800: [hex];
  --gray-900: [hex]; --gray-950: [hex];

  /* Semantic */
  --color-primary:        var(--primary-500);
  --color-primary-hover:  var(--primary-600);
  --color-primary-active: var(--primary-700);
  --color-primary-subtle: var(--primary-50);
  --color-success: [hex]; --color-warning: [hex];
  --color-error:   [hex]; --color-info:    [hex];

  /* Text */
  --color-text-primary:   var(--gray-900);
  --color-text-secondary: var(--gray-700);
  --color-text-tertiary:  var(--gray-500);
  --color-text-disabled:  var(--gray-400);

  /* Backgrounds */
  --color-bg-page:    var(--gray-50);
  --color-bg-card:    #ffffff;
  --color-border:     var(--gray-200);

  /* Typography — from chosen typescale ratio (Phase 4.8) */
  --font-family: '[Font Name]', sans-serif;
  --text-display: [size]px;
  --text-h1:      [size]px;
  --text-h2:      [size]px;
  --text-h3:      [size]px;
  --text-h4:      [size]px;
  --text-body-lg: [size]px;
  --text-body:    16px;
  --text-body-sm: [size]px;
  --text-caption: [size]px;
  --text-label:   12px;

  /* Line Heights */
  --leading-display: [size]px; --leading-h1: [size]px;
  --leading-h2: [size]px;      --leading-h3: [size]px;
  --leading-h4: [size]px;      --leading-body: 24px;
  --leading-body-sm: [size]px; --leading-caption: [size]px;

  /* Spacing — 8pt grid */
  --space-1:  4px;   --space-2:  8px;
  --space-3:  12px;  --space-4:  16px;
  --space-6:  24px;  --space-8:  32px;
  --space-10: 40px;  --space-12: 48px;
  --space-16: 64px;  --space-20: 80px;

  /* Border Radius */
  --radius-sm:   4px;
  --radius-md:   8px;
  --radius-lg:   12px;
  --radius-xl:   16px;
  --radius-2xl:  24px;
  --radius-pill: 9999px;

  /* Shadows */
  --shadow-sm: 0 1px 3px rgba(0,0,0,0.08);
  --shadow-md: 0 4px 12px rgba(0,0,0,0.10);
  --shadow-lg: 0 8px 24px rgba(0,0,0,0.12);
  --shadow-xl: 0 20px 40px rgba(0,0,0,0.16);

  /* Animation */
  --duration-fast:   150ms;
  --duration-normal: 250ms;
  --duration-slow:   350ms;
  --ease-default:    cubic-bezier(0.4, 0, 0.2, 1);
  --ease-out:        cubic-bezier(0, 0, 0.2, 1);
  --ease-in:         cubic-bezier(0.4, 0, 1, 1);
}

/* Reset & Base */
*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
body {
  font-family: var(--font-family);
  font-size: var(--text-body);
  color: var(--color-text-primary);
  background: var(--color-bg-page);
  line-height: 1.6;
  -webkit-font-smoothing: antialiased;
}
h1 { font-size: var(--text-h1); line-height: var(--leading-h1); font-weight: 700; }
h2 { font-size: var(--text-h2); line-height: var(--leading-h2); font-weight: 600; }
h3 { font-size: var(--text-h3); line-height: var(--leading-h3); font-weight: 600; }
h4 { font-size: var(--text-h4); line-height: var(--leading-h4); font-weight: 600; }

/* prefers-reduced-motion — always include */
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
  }
}
```

---


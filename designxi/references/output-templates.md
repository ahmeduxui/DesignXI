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

## casestudy.html — Full Case Study Structure

This is the most comprehensive deliverable. It tells the entire story of the project — who we designed for, how we researched, what decisions we made, and what we built. Structure it as a long-form scrollable document with a sticky sidebar navigation.

### Section Order (Complete Case Study)

```
1.  Hero + Project Overview
    ↳ Statistics Summary Bar (user interviews · survey replies · competitors · screens)
2.  About the Product
3.  My Role + Tools
4.  Project Scope
5.  Project Timeline
    ↳ Option A: Gantt-style horizontal (week × phase grid)
    ↳ Option B: Vertical dot timeline
6.  Problem & Solution
7.  Research Methods Overview
    7a. Survey — How did we reach a larger audience?
        ↳ Donut charts (gender, age, usage breakdown)
        ↳ Key stat cards
    7b. User Interviews — How did we understand user needs?
        ↳ Questions by Research Objective (Objective 1 / 2 / 3 card format)
        ↳ User insight quote cards (avatar + quote grid)
        ↳ Key insight cards
    7c. Stakeholder Interviews — How did we understand the business?
    7d. Competitor Analysis — How did we understand the market?
        ↳ Summary table (rating, strengths, weaknesses, opportunity)
        ↳ Feature matrix (✓ / ✗ / ◑ comparison across competitors)
8.  Define
    8a. Persona — How did we define our target audience?
        ↳ 4-column: Goals / Motivators / Frustrations / Behaviors
        ↳ Personality sliders (Introvert↔Extrovert, Analytical↔Creative...)
        ↳ Favorite Brands row
    8b. Empathy Map (Says / Thinks / Does / Feels)
    8c. Affinity Map — How did we organize user needs?
    8d. User Journey Map — How did we define the user journey?
    8e. Qualitative Research Synthesis
9.  Ideate
    9a. HMW — How did we identify problems and create solutions?
    9b. Feature List — What features did we decide to build?
        ↳ Derived from HMW, prioritized Must / Should / Could
    9c. Crazy 8's — How did we rapidly explore solutions?
    9d. Card Sorting — How did we find the best information architecture?
    9e. Site Map
    9f. User Flow
    9g. Wireframes — How did we convert user flow to lo-fi screens?
10. Design System — How did we unify the design components?
    10a. Color Palette (Primary, Secondary, Neutral — full 50→950 scales)
    10b. Typography
    10c. Iconography
    10d. Spacing
    10e. Grid System
    10f. Before & After — Design Transformation
    10g. Components Library (visual grid of reusable components)
11. UI Screens (Final Design)
12. Lessons Learned
```

---

### HTML Template — casestudy.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>[Project Name] — Case Study</title>
  <link href="https://fonts.googleapis.com/css2?family=[ProjectFont]:wght@400;500;600;700&family=Tajawal:wght@400;500;600;700&display=swap" rel="stylesheet">
  <style>
    /* [Paste shared CSS tokens here] */

    /* ── LAYOUT ── */
    .cs-wrapper {
      max-width: 900px;
      margin: 0 auto;
      padding: 0 var(--space-6) var(--space-20);
    }

    /* ── SECTION PATTERN ── */
    .cs-section {
      margin-top: var(--space-20);
      padding-top: var(--space-8);
      border-top: 2px solid var(--color-border);
    }
    .cs-section-label {
      font-size: var(--text-label);
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.1em;
      color: var(--color-primary);
      margin-bottom: var(--space-2);
    }
    .cs-section-title {
      font-size: var(--text-h2);
      font-weight: 700;
      margin-bottom: var(--space-6);
      color: var(--color-text-primary);
    }
    .cs-section-subtitle {
      font-size: var(--text-h3);
      font-weight: 600;
      margin-top: var(--space-10);
      margin-bottom: var(--space-4);
    }
    .cs-body {
      font-size: var(--text-body-lg);
      color: var(--color-text-secondary);
      line-height: 1.7;
      margin-bottom: var(--space-6);
    }

    /* ── HERO ── */
    .cs-hero {
      padding: var(--space-20) 0 var(--space-12);
      text-align: center;
    }
    .cs-hero-tag {
      display: inline-block;
      background: var(--color-primary-subtle);
      color: var(--color-primary);
      font-size: var(--text-label);
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.1em;
      padding: 6px 16px;
      border-radius: var(--radius-pill);
      margin-bottom: var(--space-4);
    }
    .cs-hero h1 {
      font-size: var(--text-display);
      font-weight: 700;
      margin-bottom: var(--space-4);
    }
    .cs-hero-tagline {
      font-size: var(--text-body-lg);
      color: var(--color-text-secondary);
      max-width: 600px;
      margin: 0 auto var(--space-8);
    }
    .cs-meta-row {
      display: flex;
      gap: var(--space-8);
      justify-content: center;
      flex-wrap: wrap;
    }
    .cs-meta-item { text-align: center; }
    .cs-meta-label {
      font-size: var(--text-caption);
      text-transform: uppercase;
      letter-spacing: 0.08em;
      color: var(--color-text-tertiary);
      margin-bottom: 4px;
    }
    .cs-meta-value {
      font-size: var(--text-body);
      font-weight: 600;
      color: var(--color-text-primary);
    }
    .cs-hero-cover {
      margin-top: var(--space-8);
      border-radius: var(--radius-xl);
      overflow: hidden;
      background: var(--primary-50);
      height: 400px;
      display: flex;
      align-items: center;
      justify-content: center;
    }

    /* ── TIMELINE ── */
    .timeline {
      position: relative;
      padding-left: 32px;
    }
    .timeline::before {
      content: '';
      position: absolute;
      left: 8px;
      top: 0;
      bottom: 0;
      width: 2px;
      background: var(--color-border);
    }
    .timeline-item {
      position: relative;
      padding: var(--space-4) 0 var(--space-4) var(--space-6);
      display: flex;
      gap: var(--space-4);
      align-items: flex-start;
    }
    .timeline-dot {
      position: absolute;
      left: -32px;
      top: 20px;
      width: 16px;
      height: 16px;
      border-radius: 50%;
      background: var(--color-primary);
      border: 3px solid white;
      box-shadow: 0 0 0 2px var(--color-primary);
    }
    .timeline-phase {
      background: var(--color-bg-card);
      border: 1px solid var(--color-border);
      border-radius: var(--radius-lg);
      padding: var(--space-4) var(--space-6);
      flex: 1;
      box-shadow: var(--shadow-sm);
    }
    .timeline-phase-name {
      font-weight: 700;
      font-size: var(--text-body);
      color: var(--color-primary);
      margin-bottom: 4px;
    }
    .timeline-phase-desc {
      font-size: var(--text-body-sm);
      color: var(--color-text-secondary);
      margin-bottom: 6px;
    }
    .timeline-duration {
      display: inline-block;
      font-size: var(--text-caption);
      font-weight: 600;
      background: var(--color-primary-subtle);
      color: var(--color-primary);
      padding: 2px 10px;
      border-radius: var(--radius-pill);
    }

    /* ── TWO-COLUMN GRID ── */
    .cs-2col {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: var(--space-6);
    }
    @media (max-width: 640px) { .cs-2col { grid-template-columns: 1fr; } }

    /* ── THREE-COLUMN GRID ── */
    .cs-3col {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: var(--space-4);
    }
    @media (max-width: 640px) { .cs-3col { grid-template-columns: 1fr; } }

    /* ── CARD ── */
    .cs-card {
      background: var(--color-bg-card);
      border: 1px solid var(--color-border);
      border-radius: var(--radius-lg);
      padding: var(--space-6);
      box-shadow: var(--shadow-sm);
    }
    .cs-card-icon {
      font-size: 32px;
      margin-bottom: var(--space-3);
    }
    .cs-card-title {
      font-size: var(--text-body);
      font-weight: 700;
      margin-bottom: var(--space-2);
    }
    .cs-card-body {
      font-size: var(--text-body-sm);
      color: var(--color-text-secondary);
      line-height: 1.6;
    }

    /* ── PROBLEM / SOLUTION ── */
    .problem-solution {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: var(--space-6);
    }
    .problem-box {
      background: #FEF2F2;
      border: 1px solid #FECACA;
      border-radius: var(--radius-lg);
      padding: var(--space-6);
    }
    .solution-box {
      background: #F0FDF4;
      border: 1px solid #BBF7D0;
      border-radius: var(--radius-lg);
      padding: var(--space-6);
    }
    .ps-label {
      font-size: var(--text-caption);
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.1em;
      margin-bottom: var(--space-3);
    }
    .problem-box .ps-label { color: #DC2626; }
    .solution-box .ps-label { color: #16A34A; }
    .ps-item {
      display: flex;
      gap: var(--space-3);
      margin-bottom: var(--space-3);
      font-size: var(--text-body-sm);
      color: var(--color-text-secondary);
      align-items: flex-start;
    }
    .ps-bullet { flex-shrink: 0; }
    @media (max-width: 640px) { .problem-solution { grid-template-columns: 1fr; } }

    /* ── RESEARCH METHOD CARD ── */
    .method-card {
      background: var(--color-bg-card);
      border: 1px solid var(--color-border);
      border-radius: var(--radius-lg);
      padding: var(--space-6);
      box-shadow: var(--shadow-sm);
      margin-bottom: var(--space-6);
    }
    .method-question {
      font-size: var(--text-h4);
      font-weight: 700;
      color: var(--color-text-primary);
      margin-bottom: var(--space-2);
    }
    .method-answer-tag {
      display: inline-block;
      background: var(--color-primary-subtle);
      color: var(--color-primary);
      font-size: var(--text-caption);
      font-weight: 700;
      padding: 4px 12px;
      border-radius: var(--radius-pill);
      text-transform: uppercase;
      letter-spacing: 0.08em;
      margin-bottom: var(--space-4);
    }
    .method-stats {
      display: flex;
      gap: var(--space-8);
      margin-bottom: var(--space-4);
    }
    .stat-number {
      font-size: var(--text-h2);
      font-weight: 700;
      color: var(--color-primary);
    }
    .stat-label {
      font-size: var(--text-caption);
      color: var(--color-text-secondary);
    }
    .method-questions-list {
      background: var(--color-bg-page);
      border-radius: var(--radius-md);
      padding: var(--space-4);
      list-style: none;
    }
    .method-questions-list li {
      padding: var(--space-3) 0;
      border-bottom: 1px solid var(--color-border);
      font-size: var(--text-body-sm);
      color: var(--color-text-secondary);
      display: flex;
      gap: var(--space-3);
    }
    .method-questions-list li:last-child { border-bottom: none; }
    .q-number {
      min-width: 24px;
      height: 24px;
      background: var(--color-primary);
      color: white;
      border-radius: 50%;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: var(--text-caption);
      font-weight: 700;
      flex-shrink: 0;
    }

    /* ── COMPETITOR TABLE ── */
    .comp-table { width: 100%; border-collapse: collapse; font-size: var(--text-body-sm); }
    .comp-table th {
      background: var(--color-primary);
      color: white;
      padding: var(--space-3) var(--space-4);
      text-align: left;
      font-weight: 600;
    }
    [dir="rtl"] .comp-table th { text-align: right; }
    .comp-table td {
      padding: var(--space-3) var(--space-4);
      border-bottom: 1px solid var(--color-border);
      color: var(--color-text-secondary);
    }
    .comp-table tr:nth-child(even) td { background: var(--color-bg-page); }
    .comp-table tr:hover td { background: var(--color-primary-subtle); }
    .rating-badge {
      display: inline-block;
      background: var(--color-primary-subtle);
      color: var(--color-primary);
      padding: 2px 8px;
      border-radius: var(--radius-pill);
      font-weight: 600;
      font-size: var(--text-caption);
    }
    .comp-tag {
      display: inline-block;
      padding: 2px 8px;
      border-radius: var(--radius-pill);
      font-size: var(--text-caption);
      font-weight: 500;
      margin: 2px;
    }
    .tag-strength { background: #F0FDF4; color: #16A34A; }
    .tag-weakness { background: #FEF2F2; color: #DC2626; }

    /* ── PERSONA ── */
    .persona-card {
      background: var(--color-bg-card);
      border-radius: var(--radius-xl);
      overflow: hidden;
      box-shadow: var(--shadow-md);
      border: 1px solid var(--color-border);
    }
    .persona-header {
      background: linear-gradient(135deg, var(--color-primary), var(--primary-700));
      padding: var(--space-8);
      display: flex;
      gap: var(--space-6);
      align-items: center;
      color: white;
    }
    .persona-avatar {
      width: 72px;
      height: 72px;
      border-radius: 50%;
      background: rgba(255,255,255,0.25);
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 28px;
      font-weight: 700;
      flex-shrink: 0;
    }
    .persona-name { font-size: var(--text-h3); font-weight: 700; margin-bottom: 4px; }
    .persona-role { font-size: var(--text-body-sm); opacity: 0.85; }
    .persona-quote {
      padding: var(--space-6);
      font-size: var(--text-body-lg);
      font-style: italic;
      color: var(--color-text-secondary);
      border-bottom: 1px solid var(--color-border);
      line-height: 1.7;
    }
    .persona-body {
      display: grid;
      grid-template-columns: 1fr 1fr 1fr;
      gap: 0;
    }
    .persona-col {
      padding: var(--space-6);
      border-right: 1px solid var(--color-border);
    }
    .persona-col:last-child { border-right: none; }
    .persona-col h3 {
      font-size: var(--text-caption);
      text-transform: uppercase;
      letter-spacing: 0.1em;
      color: var(--color-primary);
      font-weight: 700;
      margin-bottom: var(--space-3);
    }
    .persona-col ul { list-style: none; }
    .persona-col ul li {
      font-size: var(--text-body-sm);
      color: var(--color-text-secondary);
      padding: var(--space-2) 0;
      border-bottom: 1px solid var(--color-border);
      display: flex;
      gap: var(--space-2);
    }
    .persona-col ul li:last-child { border-bottom: none; }
    .persona-insight {
      padding: var(--space-4) var(--space-6);
      background: var(--color-primary-subtle);
      border-top: 1px solid var(--color-border);
      font-size: var(--text-body-sm);
    }
    .persona-insight strong { color: var(--color-primary); }
    @media (max-width: 640px) {
      .persona-body { grid-template-columns: 1fr; }
      .persona-col { border-right: none; border-bottom: 1px solid var(--color-border); }
    }

    /* ── EMPATHY MAP ── */
    .empathy-map {
      display: grid;
      grid-template-columns: 1fr 1fr;
      grid-template-rows: auto auto;
      gap: var(--space-4);
    }
    .empathy-quadrant {
      background: var(--color-bg-card);
      border: 1px solid var(--color-border);
      border-radius: var(--radius-lg);
      padding: var(--space-6);
      box-shadow: var(--shadow-sm);
    }
    .empathy-label {
      font-size: var(--text-caption);
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.1em;
      margin-bottom: var(--space-3);
    }
    .says { border-top: 3px solid var(--color-primary); }
    .says .empathy-label { color: var(--color-primary); }
    .thinks { border-top: 3px solid var(--secondary-500, #8B5CF6); }
    .thinks .empathy-label { color: var(--secondary-500, #8B5CF6); }
    .does { border-top: 3px solid #0EA5E9; }
    .does .empathy-label { color: #0EA5E9; }
    .feels { border-top: 3px solid #F59E0B; }
    .feels .empathy-label { color: #F59E0B; }
    .empathy-item {
      font-size: var(--text-body-sm);
      color: var(--color-text-secondary);
      padding: var(--space-2) 0;
      border-bottom: 1px dashed var(--color-border);
    }
    .empathy-item:last-child { border-bottom: none; }

    /* ── AFFINITY MAP ── */
    .affinity-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
      gap: var(--space-4);
    }
    .affinity-cluster {
      background: var(--color-bg-card);
      border-radius: var(--radius-lg);
      overflow: hidden;
      box-shadow: var(--shadow-sm);
      border: 1px solid var(--color-border);
    }
    .affinity-cluster-header {
      background: var(--color-primary);
      color: white;
      padding: var(--space-3) var(--space-4);
      font-size: var(--text-body-sm);
      font-weight: 700;
    }
    .affinity-note {
      padding: var(--space-2) var(--space-4);
      font-size: var(--text-body-sm);
      color: var(--color-text-secondary);
      border-bottom: 1px solid var(--color-border);
      line-height: 1.4;
    }
    .affinity-note:last-child { border-bottom: none; }

    /* ── USER JOURNEY MAP ── */
    .journey-table { width: 100%; border-collapse: collapse; font-size: var(--text-body-sm); }
    .journey-table th {
      background: var(--color-primary);
      color: white;
      padding: var(--space-3) var(--space-4);
      font-weight: 600;
      text-align: left;
    }
    [dir="rtl"] .journey-table th { text-align: right; }
    .journey-table td {
      padding: var(--space-3) var(--space-4);
      border: 1px solid var(--color-border);
      vertical-align: top;
    }
    .emotion-high { color: #16A34A; font-weight: 600; }
    .emotion-low  { color: #DC2626; font-weight: 600; }
    .pain-point {
      display: inline-block;
      background: #FEF2F2;
      color: #DC2626;
      padding: 2px 8px;
      border-radius: var(--radius-pill);
      font-size: var(--text-caption);
      margin: 2px;
    }

    /* ── HMW STATEMENTS ── */
    .hmw-card {
      background: var(--color-bg-card);
      border-left: 4px solid var(--color-primary);
      border-radius: 0 var(--radius-lg) var(--radius-lg) 0;
      padding: var(--space-4) var(--space-6);
      margin-bottom: var(--space-4);
      box-shadow: var(--shadow-sm);
    }
    [dir="rtl"] .hmw-card {
      border-left: none;
      border-right: 4px solid var(--color-primary);
      border-radius: var(--radius-lg) 0 0 var(--radius-lg);
    }
    .hmw-prefix {
      font-size: var(--text-caption);
      font-weight: 700;
      text-transform: uppercase;
      color: var(--color-primary);
      letter-spacing: 0.08em;
      margin-bottom: var(--space-2);
    }
    .hmw-text {
      font-size: var(--text-body-lg);
      color: var(--color-text-primary);
      font-weight: 500;
    }

    /* ── SITEMAP ── */
    .sitemap { font-family: monospace; font-size: var(--text-body-sm); background: var(--color-bg-card); border: 1px solid var(--color-border); border-radius: var(--radius-lg); padding: var(--space-6); line-height: 2; overflow-x: auto; }
    .sitemap-root { font-weight: 700; color: var(--color-primary); font-size: var(--text-body); }
    .sitemap-section { color: var(--color-text-primary); font-weight: 600; }
    .sitemap-leaf { color: var(--color-text-secondary); }

    /* ── USER FLOW ── */
    .user-flow {
      overflow-x: auto;
      padding: var(--space-4) 0;
    }
    .flow-steps {
      display: flex;
      gap: var(--space-3);
      align-items: center;
      min-width: max-content;
    }
    .flow-step {
      background: var(--color-bg-card);
      border: 2px solid var(--color-border);
      border-radius: var(--radius-lg);
      padding: var(--space-3) var(--space-4);
      text-align: center;
      min-width: 120px;
      position: relative;
    }
    .flow-step.start, .flow-step.end {
      border-radius: var(--radius-pill);
      background: var(--color-primary);
      color: white;
      border-color: var(--color-primary);
    }
    .flow-step.decision {
      background: #FFFBEB;
      border-color: #F59E0B;
      border-radius: 8px;
      transform: rotate(0deg);
    }
    .flow-step-label { font-size: var(--text-caption); font-weight: 600; }
    .flow-step-desc { font-size: 10px; color: var(--color-text-tertiary); margin-top: 2px; }
    .flow-arrow {
      color: var(--color-text-tertiary);
      font-size: 20px;
      flex-shrink: 0;
    }

    /* ── WIREFRAME PLACEHOLDER ── */
    .wireframe-frame {
      background: var(--gray-100);
      border: 2px dashed var(--gray-300);
      border-radius: var(--radius-lg);
      padding: var(--space-4);
      font-size: var(--text-body-sm);
      color: var(--color-text-tertiary);
      font-family: monospace;
      line-height: 1.8;
    }
    .wireframe-label {
      font-weight: 700;
      color: var(--color-text-secondary);
      text-transform: uppercase;
      letter-spacing: 0.08em;
      font-size: var(--text-caption);
      margin-bottom: var(--space-2);
    }

    /* ── DESIGN SYSTEM — COLOR PALETTE ── */
    .color-scale {
      margin-bottom: var(--space-8);
    }
    .color-scale-label {
      font-size: var(--text-body-sm);
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.08em;
      color: var(--color-text-secondary);
      margin-bottom: var(--space-3);
    }
    .color-swatches {
      display: flex;
      gap: 2px;
      border-radius: var(--radius-md);
      overflow: hidden;
    }
    .swatch {
      flex: 1;
      height: 64px;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: flex-end;
      padding-bottom: 4px;
      position: relative;
    }
    .swatch-step {
      font-size: 9px;
      font-weight: 600;
      opacity: 0.7;
    }
    .swatch-hex {
      font-size: 8px;
      opacity: 0.6;
    }
    .swatch-base {
      outline: 3px solid var(--gray-900);
      outline-offset: -3px;
      border-radius: 4px;
    }

    /* ── TYPOGRAPHY SPECIMEN ── */
    .type-table { width: 100%; border-collapse: collapse; }
    .type-row { border-bottom: 1px solid var(--color-border); }
    .type-row td { padding: var(--space-3) var(--space-4); vertical-align: middle; }
    .type-name { font-size: var(--text-caption); font-weight: 700; text-transform: uppercase; color: var(--color-text-tertiary); letter-spacing: 0.08em; width: 120px; }
    .type-spec { font-size: var(--text-caption); color: var(--color-text-tertiary); font-family: monospace; width: 160px; }
    .type-sample { color: var(--color-text-primary); }

    /* ── ICONOGRAPHY ── */
    .icon-grid {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(80px, 1fr));
      gap: var(--space-3);
    }
    .icon-item {
      background: var(--color-bg-card);
      border: 1px solid var(--color-border);
      border-radius: var(--radius-md);
      padding: var(--space-3);
      text-align: center;
      font-size: var(--text-caption);
      color: var(--color-text-secondary);
    }
    .icon-preview {
      font-size: 24px;
      margin-bottom: 4px;
      color: var(--color-text-primary);
    }

    /* ── SPACING SCALE ── */
    .spacing-row {
      display: flex;
      align-items: center;
      gap: var(--space-4);
      margin-bottom: var(--space-3);
    }
    .spacing-bar {
      height: 24px;
      background: var(--color-primary);
      border-radius: var(--radius-sm);
      opacity: 0.7;
    }
    .spacing-info {
      font-size: var(--text-body-sm);
      color: var(--color-text-secondary);
      white-space: nowrap;
    }
    .spacing-token { font-weight: 700; color: var(--color-text-primary); }

    /* ── GRID DIAGRAM ── */
    .grid-diagram {
      background: var(--color-bg-card);
      border: 1px solid var(--color-border);
      border-radius: var(--radius-lg);
      padding: var(--space-6);
    }
    .grid-columns {
      display: flex;
      gap: 8px;
      margin-bottom: var(--space-4);
    }
    .grid-col-block {
      flex: 1;
      height: 80px;
      background: var(--color-primary-subtle);
      border: 1px solid var(--primary-200);
      border-radius: 4px;
    }
    .grid-spec-row {
      display: flex;
      gap: var(--space-8);
      font-size: var(--text-body-sm);
    }
    .grid-spec-item { }
    .grid-spec-label {
      font-size: var(--text-caption);
      color: var(--color-text-tertiary);
      text-transform: uppercase;
      letter-spacing: 0.08em;
      margin-bottom: 2px;
    }
    .grid-spec-value { font-weight: 700; color: var(--color-primary); }

    /* ── ROLE & TOOLS ── */
    .role-tools-grid {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: var(--space-6);
    }
    .tool-badge {
      display: inline-flex;
      align-items: center;
      gap: var(--space-2);
      background: var(--color-bg-card);
      border: 1px solid var(--color-border);
      border-radius: var(--radius-pill);
      padding: 6px 16px;
      font-size: var(--text-body-sm);
      font-weight: 500;
      margin: 4px;
    }

    /* ── SCOPE TABLE ── */
    .scope-grid {
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: var(--space-4);
    }
    .scope-item {
      background: var(--color-bg-card);
      border: 1px solid var(--color-border);
      border-radius: var(--radius-lg);
      padding: var(--space-5);
    }
    .scope-item-label {
      font-size: var(--text-caption);
      text-transform: uppercase;
      letter-spacing: 0.08em;
      font-weight: 700;
      color: var(--color-primary);
      margin-bottom: var(--space-3);
    }
    .scope-item ul { list-style: none; }
    .scope-item ul li {
      font-size: var(--text-body-sm);
      color: var(--color-text-secondary);
      padding: var(--space-2) 0;
      border-bottom: 1px solid var(--color-border);
      display: flex;
      gap: var(--space-2);
      align-items: flex-start;
    }
    .scope-item ul li:last-child { border-bottom: none; }

    /* ── SCREENS PREVIEW GRID ── */
    .screens-preview {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
      gap: var(--space-6);
    }
    .screen-thumb {
      background: var(--color-bg-card);
      border-radius: var(--radius-lg);
      overflow: hidden;
      box-shadow: var(--shadow-md);
      border: 1px solid var(--color-border);
    }
    .screen-thumb-inner {
      background: var(--color-bg-page);
      height: 360px;
      overflow: hidden;
      display: flex;
      align-items: flex-start;
    }
    .screen-thumb-label {
      padding: var(--space-3) var(--space-4);
      font-size: var(--text-body-sm);
      font-weight: 600;
      border-top: 1px solid var(--color-border);
    }
    .screen-thumb-desc {
      padding: 0 var(--space-4) var(--space-3);
      font-size: var(--text-caption);
      color: var(--color-text-secondary);
    }

    /* ── LESSONS LEARNED ── */
    .lesson-item {
      display: flex;
      gap: var(--space-4);
      margin-bottom: var(--space-6);
      padding-bottom: var(--space-6);
      border-bottom: 1px solid var(--color-border);
    }
    .lesson-item:last-child { border-bottom: none; }
    .lesson-number {
      width: 40px;
      height: 40px;
      border-radius: 50%;
      background: var(--color-primary);
      color: white;
      display: flex;
      align-items: center;
      justify-content: center;
      font-weight: 700;
      font-size: var(--text-body-sm);
      flex-shrink: 0;
    }
    .lesson-title { font-weight: 700; margin-bottom: var(--space-2); }
    .lesson-desc { font-size: var(--text-body-sm); color: var(--color-text-secondary); line-height: 1.6; }

    /* ── STATISTICS SUMMARY BAR ── */
    .stats-summary {
      display: flex;
      gap: 0;
      border-radius: var(--radius-xl);
      overflow: hidden;
      box-shadow: var(--shadow-md);
      margin: var(--space-8) 0;
    }
    .stats-summary-item {
      flex: 1;
      background: var(--color-primary);
      color: white;
      padding: var(--space-8) var(--space-6);
      text-align: center;
      border-right: 1px solid rgba(255,255,255,0.15);
    }
    .stats-summary-item:last-child { border-right: none; }
    .stats-summary-item:nth-child(2) { background: var(--primary-600); }
    .stats-summary-item:nth-child(3) { background: var(--primary-700); }
    .stats-summary-item:nth-child(4) { background: var(--primary-800); }
    .stats-num {
      font-size: var(--text-display);
      font-weight: 700;
      line-height: 1;
      margin-bottom: var(--space-2);
    }
    .stats-label {
      font-size: var(--text-caption);
      font-weight: 600;
      text-transform: uppercase;
      letter-spacing: 0.08em;
      opacity: 0.85;
    }

    /* ── GANTT TIMELINE ── */
    .gantt-wrapper { overflow-x: auto; margin-top: var(--space-6); }
    .gantt-table { border-collapse: collapse; min-width: 700px; width: 100%; font-size: var(--text-caption); }
    .gantt-table th {
      background: var(--color-bg-page);
      border: 1px solid var(--color-border);
      padding: var(--space-2) var(--space-3);
      text-align: center;
      font-weight: 700;
      color: var(--color-text-tertiary);
      text-transform: uppercase;
      letter-spacing: 0.06em;
    }
    .gantt-table td {
      border: 1px solid var(--color-border);
      padding: var(--space-2) var(--space-3);
      vertical-align: middle;
    }
    .gantt-phase-name {
      font-weight: 700;
      font-size: var(--text-body-sm);
      color: var(--color-text-primary);
      white-space: nowrap;
      padding-right: var(--space-4);
    }
    .gantt-bar {
      border-radius: var(--radius-pill);
      height: 24px;
      background: var(--color-primary);
      opacity: 0.85;
    }
    .gantt-bar.phase-2 { background: var(--secondary-500, #8B5CF6); }
    .gantt-bar.phase-3 { background: #0EA5E9; }
    .gantt-bar.phase-4 { background: #F59E0B; }
    .gantt-bar.phase-5 { background: #10B981; }
    .gantt-bar.phase-6 { background: #EF4444; }

    /* ── DONUT CHART (CSS-only) ── */
    .survey-charts {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
      gap: var(--space-6);
      margin: var(--space-6) 0;
    }
    .donut-chart-wrap { text-align: center; }
    .donut-chart-title {
      font-size: var(--text-body-sm);
      font-weight: 700;
      color: var(--color-text-primary);
      margin-bottom: var(--space-4);
    }
    .donut {
      width: 140px;
      height: 140px;
      border-radius: 50%;
      margin: 0 auto var(--space-4);
      position: relative;
      display: flex;
      align-items: center;
      justify-content: center;
    }
    /* Usage: style="background: conic-gradient(var(--color-primary) 0% [X]%, var(--primary-200) [X]% 100%)" */
    .donut-inner {
      width: 80px;
      height: 80px;
      background: white;
      border-radius: 50%;
      display: flex;
      align-items: center;
      justify-content: center;
      font-weight: 700;
      font-size: var(--text-body-sm);
      color: var(--color-primary);
    }
    .donut-legend {
      display: flex;
      flex-direction: column;
      gap: var(--space-2);
      align-items: flex-start;
      display: inline-flex;
    }
    .donut-legend-item {
      display: flex;
      align-items: center;
      gap: var(--space-2);
      font-size: var(--text-caption);
      color: var(--color-text-secondary);
    }
    .donut-swatch {
      width: 12px;
      height: 12px;
      border-radius: 3px;
      flex-shrink: 0;
    }

    /* ── QUOTE CARDS ── */
    .quote-cards-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
      gap: var(--space-4);
      margin: var(--space-6) 0;
    }
    .quote-card {
      background: var(--color-bg-card);
      border: 1px solid var(--color-border);
      border-radius: var(--radius-lg);
      padding: var(--space-5);
      box-shadow: var(--shadow-sm);
      position: relative;
    }
    .quote-card::before {
      content: '"';
      position: absolute;
      top: var(--space-3);
      left: var(--space-4);
      font-size: 48px;
      line-height: 1;
      color: var(--color-primary);
      opacity: 0.2;
      font-family: Georgia, serif;
    }
    [dir="rtl"] .quote-card::before { left: auto; right: var(--space-4); }
    .quote-card-text {
      font-size: var(--text-body-sm);
      color: var(--color-text-secondary);
      font-style: italic;
      line-height: 1.7;
      margin-bottom: var(--space-4);
      padding-top: var(--space-4);
    }
    .quote-card-author {
      display: flex;
      align-items: center;
      gap: var(--space-3);
    }
    .quote-avatar {
      width: 36px;
      height: 36px;
      border-radius: 50%;
      background: var(--color-primary-subtle);
      color: var(--color-primary);
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: var(--text-caption);
      font-weight: 700;
      flex-shrink: 0;
    }
    .quote-author-info { }
    .quote-author-name { font-size: var(--text-body-sm); font-weight: 700; color: var(--color-text-primary); }
    .quote-author-role { font-size: var(--text-caption); color: var(--color-text-tertiary); }

    /* ── RESEARCH OBJECTIVES (Interview questions grouped by objective) ── */
    .objective-card {
      background: var(--color-bg-card);
      border: 1px solid var(--color-border);
      border-radius: var(--radius-lg);
      overflow: hidden;
      margin-bottom: var(--space-4);
      box-shadow: var(--shadow-sm);
    }
    .objective-header {
      background: var(--color-primary-subtle);
      border-bottom: 1px solid var(--color-border);
      padding: var(--space-4) var(--space-5);
      display: flex;
      align-items: center;
      gap: var(--space-3);
    }
    .objective-number {
      width: 28px;
      height: 28px;
      border-radius: 50%;
      background: var(--color-primary);
      color: white;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: var(--text-caption);
      font-weight: 700;
      flex-shrink: 0;
    }
    .objective-title {
      font-size: var(--text-body-sm);
      font-weight: 700;
      color: var(--color-primary);
    }
    .objective-questions { list-style: none; }
    .objective-questions li {
      padding: var(--space-3) var(--space-5);
      border-bottom: 1px solid var(--color-border);
      font-size: var(--text-body-sm);
      color: var(--color-text-secondary);
      display: flex;
      gap: var(--space-3);
      align-items: flex-start;
    }
    .objective-questions li:last-child { border-bottom: none; }
    .q-dot {
      width: 6px;
      height: 6px;
      border-radius: 50%;
      background: var(--color-primary);
      flex-shrink: 0;
      margin-top: 6px;
    }

    /* ── FEATURE MATRIX (competitor ✓/✗ table) ── */
    .feature-matrix { width: 100%; border-collapse: collapse; font-size: var(--text-body-sm); margin-top: var(--space-6); }
    .feature-matrix th {
      background: var(--color-primary);
      color: white;
      padding: var(--space-3) var(--space-4);
      text-align: center;
      font-weight: 600;
      border: 1px solid rgba(255,255,255,0.2);
    }
    .feature-matrix th:first-child { text-align: left; border-radius: 0; }
    [dir="rtl"] .feature-matrix th:first-child { text-align: right; }
    .feature-matrix td {
      padding: var(--space-3) var(--space-4);
      border: 1px solid var(--color-border);
      text-align: center;
      color: var(--color-text-secondary);
    }
    .feature-matrix td:first-child {
      text-align: left;
      font-weight: 600;
      color: var(--color-text-primary);
      background: var(--color-bg-page);
    }
    [dir="rtl"] .feature-matrix td:first-child { text-align: right; }
    .feature-matrix tr:nth-child(even) td { background: var(--gray-50); }
    .feature-matrix tr:nth-child(even) td:first-child { background: var(--color-bg-page); }
    .feat-yes { color: #16A34A; font-size: 18px; font-weight: 700; }
    .feat-no  { color: #DC2626; font-size: 18px; font-weight: 700; }
    .feat-partial { color: #D97706; font-size: 18px; }
    /* Our product column highlight */
    .feature-matrix .our-col { background: var(--color-primary-subtle) !important; font-weight: 700; color: var(--color-primary) !important; }

    /* ── PERSONA PERSONALITY SLIDERS ── */
    .persona-sliders {
      padding: var(--space-6);
      border-top: 1px solid var(--color-border);
    }
    .persona-sliders h3 {
      font-size: var(--text-caption);
      text-transform: uppercase;
      letter-spacing: 0.1em;
      color: var(--color-primary);
      font-weight: 700;
      margin-bottom: var(--space-4);
    }
    .slider-row {
      display: flex;
      align-items: center;
      gap: var(--space-3);
      margin-bottom: var(--space-3);
    }
    .slider-label {
      font-size: var(--text-caption);
      color: var(--color-text-secondary);
      white-space: nowrap;
      min-width: 80px;
      text-align: right;
    }
    [dir="rtl"] .slider-label { text-align: left; }
    .slider-label.right { text-align: left; }
    [dir="rtl"] .slider-label.right { text-align: right; }
    .slider-track {
      flex: 1;
      height: 6px;
      background: var(--color-border);
      border-radius: var(--radius-pill);
      position: relative;
    }
    .slider-fill {
      position: absolute;
      top: 0;
      left: 0;
      height: 100%;
      border-radius: var(--radius-pill);
      background: var(--color-primary);
    }
    .slider-thumb {
      position: absolute;
      top: 50%;
      transform: translate(-50%, -50%);
      width: 14px;
      height: 14px;
      border-radius: 50%;
      background: var(--color-primary);
      border: 2px solid white;
      box-shadow: var(--shadow-sm);
    }
    /* Usage: style="left: [X]%" on .slider-fill and .slider-thumb */

    /* ── PERSONA BRANDS ── */
    .persona-brands {
      padding: var(--space-5) var(--space-6);
      border-top: 1px solid var(--color-border);
    }
    .persona-brands h3 {
      font-size: var(--text-caption);
      text-transform: uppercase;
      letter-spacing: 0.1em;
      color: var(--color-primary);
      font-weight: 700;
      margin-bottom: var(--space-3);
    }
    .brand-badges {
      display: flex;
      flex-wrap: wrap;
      gap: var(--space-2);
    }
    .brand-badge {
      background: var(--color-bg-page);
      border: 1px solid var(--color-border);
      border-radius: var(--radius-md);
      padding: 6px 14px;
      font-size: var(--text-caption);
      font-weight: 600;
      color: var(--color-text-secondary);
      display: flex;
      align-items: center;
      gap: var(--space-2);
    }

    /* ── FEATURE LIST (derived from HMW) ── */
    .feature-list {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
      gap: var(--space-4);
      margin: var(--space-6) 0;
    }
    .feature-list-item {
      background: var(--color-bg-card);
      border: 1px solid var(--color-border);
      border-radius: var(--radius-lg);
      padding: var(--space-5);
      box-shadow: var(--shadow-sm);
      display: flex;
      flex-direction: column;
      gap: var(--space-3);
    }
    .feature-list-icon {
      width: 40px;
      height: 40px;
      border-radius: var(--radius-md);
      background: var(--color-primary-subtle);
      color: var(--color-primary);
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 20px;
    }
    .feature-list-name {
      font-size: var(--text-body-sm);
      font-weight: 700;
      color: var(--color-text-primary);
    }
    .feature-list-desc {
      font-size: var(--text-caption);
      color: var(--color-text-secondary);
      line-height: 1.5;
    }
    .feature-list-hmw {
      font-size: var(--text-caption);
      color: var(--color-primary);
      font-style: italic;
      border-top: 1px solid var(--color-border);
      padding-top: var(--space-2);
    }
    .feature-priority {
      display: inline-block;
      font-size: 10px;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.06em;
      padding: 2px 8px;
      border-radius: var(--radius-pill);
      align-self: flex-start;
    }
    .priority-must { background: #FEF2F2; color: #DC2626; }
    .priority-should { background: #FFFBEB; color: #D97706; }
    .priority-could { background: #F0FDF4; color: #16A34A; }

    /* ── CRAZY 8'S ── */
    .crazy8-grid {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: var(--space-3);
      margin: var(--space-6) 0;
    }
    @media (max-width: 640px) { .crazy8-grid { grid-template-columns: repeat(2, 1fr); } }
    .crazy8-cell {
      aspect-ratio: 9/16;
      background: var(--gray-100);
      border: 2px dashed var(--gray-300);
      border-radius: var(--radius-md);
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      padding: var(--space-3);
      gap: var(--space-2);
    }
    .crazy8-number {
      font-size: var(--text-caption);
      font-weight: 700;
      color: var(--color-text-tertiary);
      align-self: flex-start;
    }
    .crazy8-sketch-area {
      flex: 1;
      width: 100%;
      border: 1px solid var(--gray-300);
      border-radius: var(--radius-sm);
      background: white;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: var(--text-caption);
      color: var(--color-text-tertiary);
      text-align: center;
      font-family: monospace;
      line-height: 1.6;
      padding: var(--space-2);
    }
    .crazy8-idea {
      font-size: 10px;
      font-weight: 600;
      color: var(--color-text-secondary);
      text-align: center;
    }

    /* ── BEFORE / AFTER COMPARISON ── */
    .before-after {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: var(--space-6);
      margin: var(--space-6) 0;
    }
    @media (max-width: 640px) { .before-after { grid-template-columns: 1fr; } }
    .before-pane, .after-pane {
      border-radius: var(--radius-xl);
      overflow: hidden;
      box-shadow: var(--shadow-md);
    }
    .ba-header {
      padding: var(--space-3) var(--space-4);
      display: flex;
      align-items: center;
      gap: var(--space-2);
    }
    .before-pane .ba-header { background: #FEF2F2; }
    .after-pane .ba-header { background: #F0FDF4; }
    .ba-label {
      font-size: var(--text-caption);
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.08em;
    }
    .before-pane .ba-label { color: #DC2626; }
    .after-pane .ba-label { color: #16A34A; }
    .ba-content {
      background: var(--color-bg-page);
      min-height: 300px;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: var(--text-body-sm);
      color: var(--color-text-tertiary);
      border: 1px solid var(--color-border);
      border-top: none;
    }

    /* ── COMPONENTS LIBRARY GRID ── */
    .component-library {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
      gap: var(--space-4);
      margin: var(--space-6) 0;
    }
    .component-card {
      background: var(--color-bg-card);
      border: 1px solid var(--color-border);
      border-radius: var(--radius-lg);
      overflow: hidden;
      box-shadow: var(--shadow-sm);
    }
    .component-preview {
      background: var(--color-bg-page);
      padding: var(--space-6);
      min-height: 120px;
      display: flex;
      align-items: center;
      justify-content: center;
      border-bottom: 1px solid var(--color-border);
    }
    .component-info {
      padding: var(--space-3) var(--space-4);
    }
    .component-name {
      font-size: var(--text-body-sm);
      font-weight: 700;
      color: var(--color-text-primary);
      margin-bottom: 2px;
    }
    .component-variants {
      font-size: var(--text-caption);
      color: var(--color-text-tertiary);
    }

  </style>
</head>
<body>

<!-- LANGUAGE SWITCHER -->
<div class="lang-switcher">
  <button class="lang-btn active" onclick="setLang('en', this)">English</button>
  <button class="lang-btn" onclick="setLang('ar', this)">العربية</button>
</div>

<!-- ═══════════════════════════════════════════════ ENGLISH ═══ -->
<div id="content-en" class="lang-block">
  <div class="cs-wrapper">

    <!-- ─── 1. HERO ─── -->
    <section class="cs-hero">
      <span class="cs-hero-tag">UX/UI Case Study</span>
      <h1>[Project Name]</h1>
      <p class="cs-hero-tagline">[One compelling sentence — what the product does and for whom]</p>
      <div class="cs-meta-row">
        <div class="cs-meta-item">
          <div class="cs-meta-label">My Role</div>
          <div class="cs-meta-value">[UX/UI Designer]</div>
        </div>
        <div class="cs-meta-item">
          <div class="cs-meta-label">Platform</div>
          <div class="cs-meta-value">[iOS / Android / Web]</div>
        </div>
        <div class="cs-meta-item">
          <div class="cs-meta-label">Duration</div>
          <div class="cs-meta-value">[X weeks / months]</div>
        </div>
        <div class="cs-meta-item">
          <div class="cs-meta-label">Year</div>
          <div class="cs-meta-value">[2024 / 2025]</div>
        </div>
      </div>
      <div class="cs-hero-cover">
        <!-- Hero mockup image or screenshot of key screen(s) -->
        [Hero visual — key screens arranged on brand background]
      </div>
    </section>

    <!-- ─── STATISTICS SUMMARY BAR ─── -->
    <!-- Place this immediately after the hero — it gives recruiters/viewers instant project scale at a glance -->
    <div class="stats-summary">
      <div class="stats-summary-item">
        <div class="stats-num">[XX]</div>
        <div class="stats-label">User Interviews</div>
      </div>
      <div class="stats-summary-item">
        <div class="stats-num">[XXX]</div>
        <div class="stats-label">Survey Replies</div>
      </div>
      <div class="stats-summary-item">
        <div class="stats-num">[X]</div>
        <div class="stats-label">Competitors Analyzed</div>
      </div>
      <div class="stats-summary-item">
        <div class="stats-num">[XX]</div>
        <div class="stats-label">Screens Designed</div>
      </div>
    </div>

    <!-- ─── 2. ABOUT THE PRODUCT ─── -->
    <section class="cs-section">
      <div class="cs-section-label">About</div>
      <h2 class="cs-section-title">[Product Name] — What Is It?</h2>
      <p class="cs-body">[3-4 sentence description of the product. What it does, who it's for, what market it operates in, and what makes it relevant. Write this as if introducing the product to someone who has never heard of it.]</p>
      <div class="cs-3col">
        <div class="cs-card">
          <div class="cs-card-icon">🎯</div>
          <div class="cs-card-title">Target Audience</div>
          <div class="cs-card-body">[Who uses this product and why]</div>
        </div>
        <div class="cs-card">
          <div class="cs-card-icon">📱</div>
          <div class="cs-card-title">Platform</div>
          <div class="cs-card-body">[iOS / Android / Web — any platform specifics]</div>
        </div>
        <div class="cs-card">
          <div class="cs-card-icon">🏢</div>
          <div class="cs-card-title">Industry</div>
          <div class="cs-card-body">[Industry / category / market]</div>
        </div>
      </div>
    </section>

    <!-- ─── 3. MY ROLE + TOOLS ─── -->
    <section class="cs-section">
      <div class="cs-section-label">Team & Tools</div>
      <h2 class="cs-section-title">My Role & Tools Used</h2>
      <div class="role-tools-grid">
        <div class="cs-card">
          <h3 class="cs-card-title" style="margin-bottom: var(--space-4);">My Responsibilities</h3>
          <ul style="list-style:none;">
            <li style="padding:8px 0; border-bottom:1px solid var(--color-border); font-size:var(--text-body-sm); color:var(--color-text-secondary); display:flex; gap:8px;">✦ User Research (Interviews, Surveys)</li>
            <li style="padding:8px 0; border-bottom:1px solid var(--color-border); font-size:var(--text-body-sm); color:var(--color-text-secondary); display:flex; gap:8px;">✦ Competitor Analysis</li>
            <li style="padding:8px 0; border-bottom:1px solid var(--color-border); font-size:var(--text-body-sm); color:var(--color-text-secondary); display:flex; gap:8px;">✦ Persona & Journey Mapping</li>
            <li style="padding:8px 0; border-bottom:1px solid var(--color-border); font-size:var(--text-body-sm); color:var(--color-text-secondary); display:flex; gap:8px;">✦ Information Architecture</li>
            <li style="padding:8px 0; border-bottom:1px solid var(--color-border); font-size:var(--text-body-sm); color:var(--color-text-secondary); display:flex; gap:8px;">✦ Wireframing & Prototyping</li>
            <li style="padding:8px 0; font-size:var(--text-body-sm); color:var(--color-text-secondary); display:flex; gap:8px;">✦ UI Design & Design System</li>
          </ul>
        </div>
        <div class="cs-card">
          <h3 class="cs-card-title" style="margin-bottom: var(--space-4);">Tools</h3>
          <div>
            <span class="tool-badge">🎨 Figma</span>
            <span class="tool-badge">📊 Google Forms</span>
            <span class="tool-badge">🔍 Maze</span>
            <span class="tool-badge">📝 Notion</span>
            <span class="tool-badge">🧩 FigJam</span>
            <span class="tool-badge">📱 Optimal Workshop</span>
            <!-- Add / remove tools as needed -->
          </div>
        </div>
      </div>
    </section>

    <!-- ─── 4. PROJECT SCOPE ─── -->
    <section class="cs-section">
      <div class="cs-section-label">Project Scope</div>
      <h2 class="cs-section-title">What We Set Out to Do</h2>
      <p class="cs-body">[1-2 sentences describing the overall project scope — what was included, what was deliberately left out, and why.]</p>
      <div class="scope-grid">
        <div class="scope-item">
          <div class="scope-item-label">📋 Scope Description</div>
          <ul>
            <li>✦ [What is in scope — item 1]</li>
            <li>✦ [What is in scope — item 2]</li>
            <li>✦ [What is in scope — item 3]</li>
          </ul>
        </div>
        <div class="scope-item">
          <div class="scope-item-label">📦 Deliverables</div>
          <ul>
            <li>✦ User Research Report</li>
            <li>✦ Personas & Journey Maps</li>
            <li>✦ Wireframes (Lo-Fi)</li>
            <li>✦ High-Fidelity UI Screens</li>
            <li>✦ Interactive Prototype</li>
            <li>✦ Design System</li>
          </ul>
        </div>
        <div class="scope-item">
          <div class="scope-item-label">⚠️ Constraints</div>
          <ul>
            <li>✦ [Constraint 1 — time, budget, tech, etc.]</li>
            <li>✦ [Constraint 2]</li>
            <li>✦ [Constraint 3]</li>
          </ul>
        </div>
        <div class="scope-item">
          <div class="scope-item-label">📱 Platforms</div>
          <ul>
            <li>✦ [Platform 1 — e.g., iOS (iPhone 14 base)]</li>
            <li>✦ [Platform 2 — e.g., Android (Material 3)]</li>
            <li>✦ [Platform 3 — e.g., Web (Desktop 1440px)]</li>
          </ul>
        </div>
      </div>
    </section>

    <!-- ─── 5. PROJECT TIMELINE ─── -->
    <section class="cs-section">
      <div class="cs-section-label">Timeline</div>
      <h2 class="cs-section-title">Project Timeline</h2>

      <!-- OPTION A: Gantt-style horizontal timeline (recommended for multi-week projects) -->
      <!-- Shows week-by-week progress across phases — visually clearer for long projects -->
      <div class="gantt-wrapper">
        <table class="gantt-table">
          <thead>
            <tr>
              <th style="text-align:left; min-width:120px;">Phase</th>
              <th>Week 1</th>
              <th>Week 2</th>
              <th>Week 3</th>
              <th>Week 4</th>
              <th>Week 5</th>
              <th>Week 6</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td class="gantt-phase-name">Discovery</td>
              <td><div class="gantt-bar phase-1" style="width:100%;"></div></td>
              <td></td><td></td><td></td><td></td><td></td>
            </tr>
            <tr>
              <td class="gantt-phase-name">Research</td>
              <td><div class="gantt-bar phase-2" style="width:100%;"></div></td>
              <td><div class="gantt-bar phase-2" style="width:100%;"></div></td>
              <td></td><td></td><td></td><td></td>
            </tr>
            <tr>
              <td class="gantt-phase-name">Define</td>
              <td></td>
              <td><div class="gantt-bar phase-3" style="width:100%;"></div></td>
              <td><div class="gantt-bar phase-3" style="width:50%;"></div></td>
              <td></td><td></td><td></td>
            </tr>
            <tr>
              <td class="gantt-phase-name">Ideate</td>
              <td></td><td></td>
              <td><div class="gantt-bar phase-4" style="width:100%;"></div></td>
              <td></td><td></td><td></td>
            </tr>
            <tr>
              <td class="gantt-phase-name">UI Design</td>
              <td></td><td></td><td></td>
              <td><div class="gantt-bar phase-5" style="width:100%;"></div></td>
              <td><div class="gantt-bar phase-5" style="width:100%;"></div></td>
              <td></td>
            </tr>
            <tr>
              <td class="gantt-phase-name">Testing & Delivery</td>
              <td></td><td></td><td></td><td></td><td></td>
              <td><div class="gantt-bar phase-6" style="width:100%;"></div></td>
            </tr>
          </tbody>
        </table>
      </div>
      <!-- Adjust colspan of bars to match actual project weeks -->

      <!-- OPTION B: Vertical dot timeline (use for shorter or phase-summary projects) -->
      <div class="timeline" style="margin-top: var(--space-8);">[CHOOSE OPTION A OR B — REMOVE THE OTHER]</div>
      <div class="timeline">
        <div class="timeline-item">
          <div class="timeline-dot"></div>
          <div class="timeline-phase">
            <div class="timeline-phase-name">Phase 1 — Discovery</div>
            <div class="timeline-phase-desc">Defining the problem, understanding the business context, setting success metrics</div>
            <span class="timeline-duration">[e.g., Week 1 — 3 days]</span>
          </div>
        </div>
        <div class="timeline-item">
          <div class="timeline-dot"></div>
          <div class="timeline-phase">
            <div class="timeline-phase-name">Phase 2 — Research</div>
            <div class="timeline-phase-desc">User interviews, surveys, competitor analysis, app store review mining</div>
            <span class="timeline-duration">[e.g., Week 1-2 — 7 days]</span>
          </div>
        </div>
        <div class="timeline-item">
          <div class="timeline-dot"></div>
          <div class="timeline-phase">
            <div class="timeline-phase-name">Phase 3 — Define</div>
            <div class="timeline-phase-desc">Personas, empathy maps, affinity mapping, user journey maps, HMW statements</div>
            <span class="timeline-duration">[e.g., Week 2 — 4 days]</span>
          </div>
        </div>
        <div class="timeline-item">
          <div class="timeline-dot"></div>
          <div class="timeline-phase">
            <div class="timeline-phase-name">Phase 4 — Ideate</div>
            <div class="timeline-phase-desc">Card sorting, information architecture, user flows, lo-fi wireframes</div>
            <span class="timeline-duration">[e.g., Week 3 — 5 days]</span>
          </div>
        </div>
        <div class="timeline-item">
          <div class="timeline-dot"></div>
          <div class="timeline-phase">
            <div class="timeline-phase-name">Phase 5 — UI Design</div>
            <div class="timeline-phase-desc">Brand identity, design system, high-fidelity screens, interactive prototype</div>
            <span class="timeline-duration">[e.g., Week 4-5 — 10 days]</span>
          </div>
        </div>
        <div class="timeline-item">
          <div class="timeline-dot"></div>
          <div class="timeline-phase">
            <div class="timeline-phase-name">Phase 6 — Testing & Delivery</div>
            <div class="timeline-phase-desc">Usability testing, iteration, final handoff</div>
            <span class="timeline-duration">[e.g., Week 6 — 4 days]</span>
          </div>
        </div>
      </div>
    </section>

    <!-- ─── 6. PROBLEM & SOLUTION ─── -->
    <section class="cs-section">
      <div class="cs-section-label">Challenge</div>
      <h2 class="cs-section-title">Problem & Solution</h2>
      <p class="cs-body">[2-3 sentences framing the core challenge. Use the Problem Statement format: user type + problem + goal + negative outcome + our approach.]</p>
      <div class="problem-solution">
        <div class="problem-box">
          <div class="ps-label">❌ The Problem</div>
          <div class="ps-item"><span class="ps-bullet">•</span>[Core problem — specific and user-focused]</div>
          <div class="ps-item"><span class="ps-bullet">•</span>[Why existing solutions fail]</div>
          <div class="ps-item"><span class="ps-bullet">•</span>[Impact on users]</div>
        </div>
        <div class="solution-box">
          <div class="ps-label">✅ Our Solution</div>
          <div class="ps-item"><span class="ps-bullet">•</span>[Solution approach — specific, not vague]</div>
          <div class="ps-item"><span class="ps-bullet">•</span>[Key differentiator from existing solutions]</div>
          <div class="ps-item"><span class="ps-bullet">•</span>[Expected measurable outcome]</div>
        </div>
      </div>
    </section>

    <!-- ═══════════════════════ RESEARCH ═══════════════════════ -->

    <!-- ─── 7a. SURVEY ─── -->
    <section class="cs-section">
      <div class="cs-section-label">Research — Quantitative</div>
      <h2 class="cs-section-title">How did we reach a larger audience?</h2>
      <div class="method-card">
        <div class="method-question">Survey</div>
        <span class="method-answer-tag">Quantitative Research</span>
        <p class="cs-body">[Why we ran a survey, what we wanted to learn, and how we distributed it.]</p>
        <div class="method-stats">
          <div>
            <div class="stat-number">[XX]</div>
            <div class="stat-label">Responses</div>
          </div>
          <div>
            <div class="stat-number">[XX]%</div>
            <div class="stat-label">[Key finding stat]</div>
          </div>
          <div>
            <div class="stat-number">[X]</div>
            <div class="stat-label">Questions asked</div>
          </div>
        </div>
        <!-- Donut charts for demographic/behavioral breakdown -->
        <p style="font-size:var(--text-body-sm); font-weight:700; margin-bottom:var(--space-4); color:var(--color-text-primary);">Respondent breakdown:</p>
        <div class="survey-charts">
          <!-- Chart 1: Gender — e.g., 65% Male, 35% Female → conic-gradient at 65% -->
          <div class="donut-chart-wrap">
            <div class="donut-chart-title">Gender</div>
            <div class="donut" style="background: conic-gradient(var(--color-primary) 0% 65%, var(--primary-200) 65% 100%);">
              <div class="donut-inner">65%</div>
            </div>
            <div class="donut-legend">
              <div class="donut-legend-item"><div class="donut-swatch" style="background:var(--color-primary);"></div>Male — [X]%</div>
              <div class="donut-legend-item"><div class="donut-swatch" style="background:var(--primary-200);"></div>Female — [X]%</div>
            </div>
          </div>
          <!-- Chart 2: Age group -->
          <div class="donut-chart-wrap">
            <div class="donut-chart-title">Age Group</div>
            <div class="donut" style="background: conic-gradient(var(--color-primary) 0% 45%, var(--primary-300) 45% 70%, var(--primary-100) 70% 100%);">
              <div class="donut-inner">[X] groups</div>
            </div>
            <div class="donut-legend">
              <div class="donut-legend-item"><div class="donut-swatch" style="background:var(--color-primary);"></div>[Age range 1] — [X]%</div>
              <div class="donut-legend-item"><div class="donut-swatch" style="background:var(--primary-300);"></div>[Age range 2] — [X]%</div>
              <div class="donut-legend-item"><div class="donut-swatch" style="background:var(--primary-100);"></div>[Age range 3] — [X]%</div>
            </div>
          </div>
          <!-- Chart 3: Usage frequency / any other dimension -->
          <div class="donut-chart-wrap">
            <div class="donut-chart-title">[e.g., App Usage Frequency]</div>
            <div class="donut" style="background: conic-gradient(var(--color-primary) 0% 55%, var(--primary-300) 55% 80%, var(--primary-100) 80% 100%);">
              <div class="donut-inner">[X]%</div>
            </div>
            <div class="donut-legend">
              <div class="donut-legend-item"><div class="donut-swatch" style="background:var(--color-primary);"></div>[Label 1] — [X]%</div>
              <div class="donut-legend-item"><div class="donut-swatch" style="background:var(--primary-300);"></div>[Label 2] — [X]%</div>
              <div class="donut-legend-item"><div class="donut-swatch" style="background:var(--primary-100);"></div>[Label 3] — [X]%</div>
            </div>
          </div>
        </div>
        <!-- Usage note: conic-gradient value = percentage of the first segment -->
        <!-- For a 3-segment donut: conic-gradient(colorA 0% X%, colorB X% Y%, colorC Y% 100%) -->

        <p style="font-size:var(--text-body-sm); font-weight:700; margin-bottom:var(--space-2); margin-top:var(--space-6); color:var(--color-text-primary);">Key findings from the survey:</p>
        <div class="cs-3col">
          <div class="cs-card">
            <div class="cs-card-title">[Stat 1 — e.g., 78%]</div>
            <div class="cs-card-body">[What this stat means for the design]</div>
          </div>
          <div class="cs-card">
            <div class="cs-card-title">[Stat 2]</div>
            <div class="cs-card-body">[What this stat means]</div>
          </div>
          <div class="cs-card">
            <div class="cs-card-title">[Stat 3]</div>
            <div class="cs-card-body">[What this stat means]</div>
          </div>
        </div>
      </div>
    </section>

    <!-- ─── 7b. USER INTERVIEWS ─── -->
    <section class="cs-section">
      <div class="cs-section-label">Research — Qualitative</div>
      <h2 class="cs-section-title">How did we understand user needs?</h2>
      <div class="method-card">
        <div class="method-question">User Interviews</div>
        <span class="method-answer-tag">Qualitative Research</span>
        <p class="cs-body">[Why user interviews, who we interviewed (not names — roles/demographics), how long each session was, and what format (moderated, remote, etc.)]</p>
        <div class="method-stats">
          <div>
            <div class="stat-number">[X]</div>
            <div class="stat-label">Participants</div>
          </div>
          <div>
            <div class="stat-number">[XX] min</div>
            <div class="stat-label">Avg. session</div>
          </div>
          <div>
            <div class="stat-number">[X]</div>
            <div class="stat-label">Recurring themes</div>
          </div>
        </div>
        <!-- OPTION A: Questions grouped by Research Objective (recommended for structured interviews) -->
        <p style="font-size:var(--text-body-sm); font-weight:700; margin-bottom:var(--space-3); color:var(--color-text-primary);">Questions by Research Objective:</p>
        <div class="objective-card">
          <div class="objective-header">
            <div class="objective-number">1</div>
            <div class="objective-title">Objective 1: [e.g., Understand current app usage habits]</div>
          </div>
          <ul class="objective-questions">
            <li><div class="q-dot"></div>[Open-ended question about their current routine/behavior]</li>
            <li><div class="q-dot"></div>[Follow-up probing question about this objective]</li>
          </ul>
        </div>
        <div class="objective-card">
          <div class="objective-header">
            <div class="objective-number">2</div>
            <div class="objective-title">Objective 2: [e.g., Identify pain points with existing solutions]</div>
          </div>
          <ul class="objective-questions">
            <li><div class="q-dot"></div>[Question that surfaces frustrations without leading the user]</li>
            <li><div class="q-dot"></div>[Question about workarounds they've tried]</li>
          </ul>
        </div>
        <div class="objective-card">
          <div class="objective-header">
            <div class="objective-number">3</div>
            <div class="objective-title">Objective 3: [e.g., Understand what a great experience looks like]</div>
          </div>
          <ul class="objective-questions">
            <li><div class="q-dot"></div>[Question about their ideal scenario]</li>
            <li><div class="q-dot"></div>[Question about a time it worked well]</li>
          </ul>
        </div>
        <!-- OPTION B: Simple numbered list (use when no formal objectives were defined) -->
        <!-- <ul class="method-questions-list"> ... </ul> -->

        <!-- User insight quote cards — the human voice of research -->
        <p style="font-size:var(--text-body-sm); font-weight:700; margin-top:var(--space-6); margin-bottom:var(--space-3); color:var(--color-text-primary);">What users told us:</p>
        <div class="quote-cards-grid">
          <div class="quote-card">
            <div class="quote-card-text">"[Direct quote or close paraphrase from a user interview — something specific and memorable]"</div>
            <div class="quote-card-author">
              <div class="quote-avatar">[Initials]</div>
              <div class="quote-author-info">
                <div class="quote-author-name">[Participant role — e.g., Freelancer, 28]</div>
                <div class="quote-author-role">[City, or just "User interview participant"]</div>
              </div>
            </div>
          </div>
          <div class="quote-card">
            <div class="quote-card-text">"[Quote from different participant — aim for variety of pain point expressions]"</div>
            <div class="quote-card-author">
              <div class="quote-avatar">[Initials]</div>
              <div class="quote-author-info">
                <div class="quote-author-name">[Participant role, Age]</div>
                <div class="quote-author-role">[User interview participant]</div>
              </div>
            </div>
          </div>
          <div class="quote-card">
            <div class="quote-card-text">"[Quote that captures a key frustration or desire — ideally surprising]"</div>
            <div class="quote-card-author">
              <div class="quote-avatar">[Initials]</div>
              <div class="quote-author-info">
                <div class="quote-author-name">[Participant role, Age]</div>
                <div class="quote-author-role">[User interview participant]</div>
              </div>
            </div>
          </div>
          <div class="quote-card">
            <div class="quote-card-text">"[Quote from a final participant — can be a positive desire or aspiration]"</div>
            <div class="quote-card-author">
              <div class="quote-avatar">[Initials]</div>
              <div class="quote-author-info">
                <div class="quote-author-name">[Participant role, Age]</div>
                <div class="quote-author-role">[User interview participant]</div>
              </div>
            </div>
          </div>
        </div>

        <p style="font-size:var(--text-body-sm); font-weight:700; margin-top:var(--space-6); margin-bottom:var(--space-3); color:var(--color-text-primary);">Key insights from interviews:</p>
        <div class="cs-3col">
          <div class="cs-card"><div class="cs-card-title">💡 Insight 1</div><div class="cs-card-body">[What we learned that changed our direction]</div></div>
          <div class="cs-card"><div class="cs-card-title">💡 Insight 2</div><div class="cs-card-body">[Surprising finding]</div></div>
          <div class="cs-card"><div class="cs-card-title">💡 Insight 3</div><div class="cs-card-body">[Pattern that emerged across most users]</div></div>
        </div>
      </div>
    </section>

    <!-- ─── 7c. STAKEHOLDER INTERVIEWS ─── -->
    <section class="cs-section">
      <div class="cs-section-label">Research — Business</div>
      <h2 class="cs-section-title">How did we understand the business?</h2>
      <div class="method-card">
        <div class="method-question">Stakeholder Interviews</div>
        <span class="method-answer-tag">Business Research</span>
        <p class="cs-body">[Why stakeholder interviews, who was interviewed (roles, not names), and what business questions we were trying to answer — revenue model, user acquisition, technical constraints, business goals.]</p>
        <p style="font-size:var(--text-body-sm); font-weight:700; margin-bottom:var(--space-3); color:var(--color-text-primary);">Key business insights:</p>
        <div class="cs-2col">
          <div class="cs-card"><div class="cs-card-title">Business Goal</div><div class="cs-card-body">[What the business is trying to achieve with this product]</div></div>
          <div class="cs-card"><div class="cs-card-title">Success Metric</div><div class="cs-card-body">[How the business measures success — KPI]</div></div>
          <div class="cs-card"><div class="cs-card-title">Technical Constraint</div><div class="cs-card-body">[Any technical limitations that affect the design]</div></div>
          <div class="cs-card"><div class="cs-card-title">Business Opportunity</div><div class="cs-card-body">[Gap in the market the business wants to capture]</div></div>
        </div>
      </div>
    </section>

    <!-- ─── 7d. COMPETITOR ANALYSIS ─── -->
    <section class="cs-section">
      <div class="cs-section-label">Research — Market</div>
      <h2 class="cs-section-title">How did we understand the market?</h2>
      <div class="method-card">
        <div class="method-question">Competitor Analysis</div>
        <span class="method-answer-tag">Market Research</span>
        <p class="cs-body">[What we looked at — direct competitors, indirect alternatives, and what dimensions we compared (features, UX quality, rating, pricing, target audience).]</p>
        <div style="overflow-x:auto;">
          <table class="comp-table">
            <thead>
              <tr>
                <th>Product</th>
                <th>Rating</th>
                <th>Strengths</th>
                <th>Weaknesses</th>
                <th>Key Opportunity</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>[Competitor 1]</strong></td>
                <td><span class="rating-badge">⭐ [X.X]</span></td>
                <td><span class="comp-tag tag-strength">[Strength]</span></td>
                <td><span class="comp-tag tag-weakness">[Weakness from reviews]</span></td>
                <td>[What they're missing that we can do]</td>
              </tr>
              <tr>
                <td><strong>[Competitor 2]</strong></td>
                <td><span class="rating-badge">⭐ [X.X]</span></td>
                <td><span class="comp-tag tag-strength">[Strength]</span></td>
                <td><span class="comp-tag tag-weakness">[Weakness]</span></td>
                <td>[Opportunity]</td>
              </tr>
              <tr>
                <td><strong>[Competitor 3]</strong></td>
                <td><span class="rating-badge">⭐ [X.X]</span></td>
                <td><span class="comp-tag tag-strength">[Strength]</span></td>
                <td><span class="comp-tag tag-weakness">[Weakness]</span></td>
                <td>[Opportunity]</td>
              </tr>
            </tbody>
          </table>
        </div>
        <p style="font-size:var(--text-body-sm); color:var(--color-text-secondary); margin-top:var(--space-4);">Market gap: [One clear sentence about the opportunity no competitor has fully addressed]</p>

        <!-- Feature Matrix — ✓/✗ comparison across competitors -->
        <!-- Use this in ADDITION to or INSTEAD of the text table above -->
        <h4 style="font-size:var(--text-body-sm); font-weight:700; margin-top:var(--space-8); margin-bottom:var(--space-3); color:var(--color-text-primary);">Feature-by-Feature Comparison:</h4>
        <div style="overflow-x:auto;">
          <table class="feature-matrix">
            <thead>
              <tr>
                <th>Feature</th>
                <th>[Competitor 1]</th>
                <th>[Competitor 2]</th>
                <th>[Competitor 3]</th>
                <th class="our-col">Our Product</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>[Feature 1 — e.g., Real-time tracking]</td>
                <td><span class="feat-yes">✓</span></td>
                <td><span class="feat-yes">✓</span></td>
                <td><span class="feat-no">✗</span></td>
                <td class="our-col"><span class="feat-yes">✓</span></td>
              </tr>
              <tr>
                <td>[Feature 2 — e.g., Arabic language support]</td>
                <td><span class="feat-partial">◑</span></td>
                <td><span class="feat-no">✗</span></td>
                <td><span class="feat-no">✗</span></td>
                <td class="our-col"><span class="feat-yes">✓</span></td>
              </tr>
              <tr>
                <td>[Feature 3 — e.g., In-app chat with driver]</td>
                <td><span class="feat-no">✗</span></td>
                <td><span class="feat-yes">✓</span></td>
                <td><span class="feat-no">✗</span></td>
                <td class="our-col"><span class="feat-yes">✓</span></td>
              </tr>
              <tr>
                <td>[Feature 4 — e.g., Scheduled orders]</td>
                <td><span class="feat-yes">✓</span></td>
                <td><span class="feat-no">✗</span></td>
                <td><span class="feat-partial">◑</span></td>
                <td class="our-col"><span class="feat-yes">✓</span></td>
              </tr>
              <tr>
                <td>[Feature 5 — e.g., Guest checkout]</td>
                <td><span class="feat-no">✗</span></td>
                <td><span class="feat-no">✗</span></td>
                <td><span class="feat-yes">✓</span></td>
                <td class="our-col"><span class="feat-yes">✓</span></td>
              </tr>
              <tr>
                <td>[Feature 6 — e.g., Order history & reorder]</td>
                <td><span class="feat-yes">✓</span></td>
                <td><span class="feat-partial">◑</span></td>
                <td><span class="feat-no">✗</span></td>
                <td class="our-col"><span class="feat-yes">✓</span></td>
              </tr>
            </tbody>
          </table>
        </div>
        <p style="font-size:var(--text-caption); color:var(--color-text-tertiary); margin-top:var(--space-3);">
          <span class="feat-yes">✓</span> Available &nbsp;
          <span class="feat-no">✗</span> Not available &nbsp;
          <span class="feat-partial">◑</span> Partially available
        </p>
      </div>
    </section>

    <!-- ═══════════════════════ DEFINE ═══════════════════════ -->

    <!-- ─── 8a. PERSONA ─── -->
    <section class="cs-section">
      <div class="cs-section-label">Define</div>
      <h2 class="cs-section-title">How did we define our target audience?</h2>
      <p class="cs-body">[Brief explanation of how we synthesized research into personas — what data points formed each persona, how many we created and why.]</p>
      <!-- Primary Persona -->
      <h3 class="cs-section-subtitle">Primary Persona</h3>
      <div class="persona-card">
        <div class="persona-header">
          <div class="persona-avatar">[Initials]</div>
          <div>
            <div class="persona-name">[Full Name]</div>
            <div class="persona-role">[Age] · [Occupation] · [City, Country]</div>
          </div>
        </div>
        <blockquote class="persona-quote">"[Quote that captures their mindset in relation to the product domain]"</blockquote>
        <!-- 4-column persona body: Goals / Motivators / Frustrations / Behaviors -->
        <div class="persona-body" style="grid-template-columns: 1fr 1fr 1fr 1fr;">
          <div class="persona-col">
            <h3>🎯 Goals</h3>
            <ul>
              <li>• [Primary goal — what they ultimately want to achieve]</li>
              <li>• [Secondary goal]</li>
              <li>• [Tertiary goal]</li>
            </ul>
          </div>
          <div class="persona-col">
            <h3>💡 Motivators</h3>
            <ul>
              <li>• [What drives them emotionally — e.g., saving time]</li>
              <li>• [Social motivator — e.g., looking competent]</li>
              <li>• [Value motivator — e.g., getting best price]</li>
            </ul>
          </div>
          <div class="persona-col">
            <h3>😤 Frustrations</h3>
            <ul>
              <li>• [Frustration 1 — specific pain, not generic]</li>
              <li>• [Frustration 2]</li>
              <li>• [Frustration 3]</li>
            </ul>
          </div>
          <div class="persona-col">
            <h3>📱 Behaviors</h3>
            <ul>
              <li>• [Behavior 1 — what they actually do]</li>
              <li>• [Behavior 2]</li>
              <li>• [Behavior 3 — tech habit or workaround]</li>
            </ul>
          </div>
        </div>

        <!-- Personality Sliders -->
        <div class="persona-sliders">
          <h3>🧠 Personality</h3>
          <div class="slider-row">
            <span class="slider-label">Introvert</span>
            <div class="slider-track">
              <div class="slider-fill" style="width: 35%;"></div>
              <div class="slider-thumb" style="left: 35%;"></div>
            </div>
            <span class="slider-label right">Extrovert</span>
          </div>
          <div class="slider-row">
            <span class="slider-label">Analytical</span>
            <div class="slider-track">
              <div class="slider-fill" style="width: 70%;"></div>
              <div class="slider-thumb" style="left: 70%;"></div>
            </div>
            <span class="slider-label right">Creative</span>
          </div>
          <div class="slider-row">
            <span class="slider-label">Traditional</span>
            <div class="slider-track">
              <div class="slider-fill" style="width: 60%;"></div>
              <div class="slider-thumb" style="left: 60%;"></div>
            </div>
            <span class="slider-label right">Innovative</span>
          </div>
          <div class="slider-row">
            <span class="slider-label">Cautious</span>
            <div class="slider-track">
              <div class="slider-fill" style="width: 45%;"></div>
              <div class="slider-thumb" style="left: 45%;"></div>
            </div>
            <span class="slider-label right">Risk-taker</span>
          </div>
          <!-- Adjust slider % to reflect actual persona personality from research -->
        </div>

        <!-- Favorite Brands (reveals personality + reference point for design direction) -->
        <div class="persona-brands">
          <h3>❤️ Favorite Brands</h3>
          <div class="brand-badges">
            <span class="brand-badge">📦 [Brand 1 — e.g., Amazon]</span>
            <span class="brand-badge">🎵 [Brand 2 — e.g., Spotify]</span>
            <span class="brand-badge">🍎 [Brand 3 — e.g., Apple]</span>
            <span class="brand-badge">🛵 [Brand 4 — relevant to domain]</span>
            <span class="brand-badge">☕ [Brand 5]</span>
          </div>
        </div>

        <div class="persona-insight"><strong>Design Insight:</strong> [What this persona needs from our design — specific, actionable, tied to research]</div>
      </div>

      <!-- Secondary Persona (if applicable) -->
      <h3 class="cs-section-subtitle" style="margin-top:var(--space-8);">Secondary Persona</h3>
      <!-- [Repeat persona-card structure] -->
    </section>

    <!-- ─── 8b. EMPATHY MAP ─── -->
    <section class="cs-section">
      <div class="cs-section-label">Define</div>
      <h2 class="cs-section-title">Empathy Map — [Persona Name]</h2>
      <p class="cs-body">[Brief explanation of what an empathy map is and what we learned from building it.]</p>
      <div class="empathy-map">
        <div class="empathy-quadrant says">
          <div class="empathy-label">SAYS</div>
          <div class="empathy-item">"[Direct quote or paraphrase from interviews]"</div>
          <div class="empathy-item">"[Another quote]"</div>
          <div class="empathy-item">"[Another quote]"</div>
        </div>
        <div class="empathy-quadrant thinks">
          <div class="empathy-label">THINKS</div>
          <div class="empathy-item">[Inner thought they may not say aloud]</div>
          <div class="empathy-item">[Concern they hold internally]</div>
          <div class="empathy-item">[Expectation they have]</div>
        </div>
        <div class="empathy-quadrant does">
          <div class="empathy-label">DOES</div>
          <div class="empathy-item">[Observed behavior 1]</div>
          <div class="empathy-item">[Observed behavior 2]</div>
          <div class="empathy-item">[Current workaround they use]</div>
        </div>
        <div class="empathy-quadrant feels">
          <div class="empathy-label">FEELS</div>
          <div class="empathy-item">[Emotion — frustrated when...]</div>
          <div class="empathy-item">[Emotion — anxious about...]</div>
          <div class="empathy-item">[Positive emotion — relieved when...]</div>
        </div>
      </div>
    </section>

    <!-- ─── 8c. AFFINITY MAP ─── -->
    <section class="cs-section">
      <div class="cs-section-label">Define</div>
      <h2 class="cs-section-title">How did we organize user needs?</h2>
      <div class="method-card">
        <div class="method-question">Affinity Map</div>
        <span class="method-answer-tag">Synthesis</span>
        <p class="cs-body">[Explain the affinity mapping process — how many data points, how the clusters emerged, what the main themes were.]</p>
        <div class="affinity-grid">
          <div class="affinity-cluster">
            <div class="affinity-cluster-header">🔴 [Theme 1 — e.g., Onboarding Confusion]</div>
            <div class="affinity-note">[Research note from interview/survey]</div>
            <div class="affinity-note">[Research note]</div>
            <div class="affinity-note">[Research note]</div>
          </div>
          <div class="affinity-cluster">
            <div class="affinity-cluster-header">🟠 [Theme 2 — e.g., Trust Issues]</div>
            <div class="affinity-note">[Research note]</div>
            <div class="affinity-note">[Research note]</div>
            <div class="affinity-note">[Research note]</div>
          </div>
          <div class="affinity-cluster">
            <div class="affinity-cluster-header">🟡 [Theme 3 — e.g., Missing Features]</div>
            <div class="affinity-note">[Research note]</div>
            <div class="affinity-note">[Research note]</div>
            <div class="affinity-note">[Research note]</div>
          </div>
          <div class="affinity-cluster">
            <div class="affinity-cluster-header">🟢 [Theme 4 — e.g., Positive Moments]</div>
            <div class="affinity-note">[Research note]</div>
            <div class="affinity-note">[Research note]</div>
            <div class="affinity-note">[Research note]</div>
          </div>
        </div>
      </div>
    </section>

    <!-- ─── 8d. USER JOURNEY MAP ─── -->
    <section class="cs-section">
      <div class="cs-section-label">Define</div>
      <h2 class="cs-section-title">How did we define the user journey?</h2>
      <div class="method-card">
        <div class="method-question">User Journey Map</div>
        <span class="method-answer-tag">Experience Mapping</span>
        <p class="cs-body">[Brief explanation: whose journey this maps, what task/goal it follows, and what the current experience looks like before our solution.]</p>
        <div style="overflow-x:auto;">
          <table class="journey-table">
            <thead>
              <tr>
                <th>Stage</th>
                <th>Awareness</th>
                <th>Consideration</th>
                <th>Action</th>
                <th>Result</th>
                <th>Follow-up</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>What they do</strong></td>
                <td>[Action in this stage]</td>
                <td>[Action]</td>
                <td>[Action]</td>
                <td>[Action]</td>
                <td>[Action]</td>
              </tr>
              <tr>
                <td><strong>What they think</strong></td>
                <td>[Thought / question]</td>
                <td>[Thought]</td>
                <td>[Thought]</td>
                <td>[Thought]</td>
                <td>[Thought]</td>
              </tr>
              <tr>
                <td><strong>How they feel</strong></td>
                <td class="emotion-high">😐 Neutral</td>
                <td class="emotion-low">😕 Confused</td>
                <td class="emotion-low">😤 Frustrated</td>
                <td class="emotion-high">😊 Relieved</td>
                <td class="emotion-high">😃 Satisfied</td>
              </tr>
              <tr>
                <td><strong>Pain points</strong></td>
                <td><span class="pain-point">[Pain]</span></td>
                <td><span class="pain-point">[Pain]</span></td>
                <td><span class="pain-point">[Pain]</span></td>
                <td>—</td>
                <td>—</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </section>

    <!-- ─── 8e. QUALITATIVE RESEARCH SYNTHESIS ─── -->
    <section class="cs-section">
      <div class="cs-section-label">Research Synthesis</div>
      <h2 class="cs-section-title">What the Research Told Us</h2>
      <p class="cs-body">[Summary of everything research revealed — what surprised us, what confirmed our assumptions, and what we now know about users that we didn't before. This bridges research to design.]</p>
      <div class="cs-3col">
        <div class="cs-card">
          <div class="cs-card-icon">💡</div>
          <div class="cs-card-title">Key Insight 1</div>
          <div class="cs-card-body">[Specific insight with design implication]</div>
        </div>
        <div class="cs-card">
          <div class="cs-card-icon">💡</div>
          <div class="cs-card-title">Key Insight 2</div>
          <div class="cs-card-body">[Specific insight]</div>
        </div>
        <div class="cs-card">
          <div class="cs-card-icon">💡</div>
          <div class="cs-card-title">Key Insight 3</div>
          <div class="cs-card-body">[Specific insight]</div>
        </div>
      </div>
    </section>

    <!-- ═══════════════════════ IDEATE ═══════════════════════ -->

    <!-- ─── 9a. HMW ─── -->
    <section class="cs-section">
      <div class="cs-section-label">Ideate</div>
      <h2 class="cs-section-title">How did we identify problems and create solutions?</h2>
      <div class="method-card">
        <div class="method-question">How Might We (HMW)</div>
        <span class="method-answer-tag">Problem Framing</span>
        <p class="cs-body">[Explain the HMW method — how it reframes problems as design opportunities, and what the resulting statements led to.]</p>
        <div class="hmw-card">
          <div class="hmw-prefix">How Might We</div>
          <div class="hmw-text">[HMW statement 1 — reframes a research finding as a design opportunity]</div>
        </div>
        <div class="hmw-card">
          <div class="hmw-prefix">How Might We</div>
          <div class="hmw-text">[HMW statement 2]</div>
        </div>
        <div class="hmw-card">
          <div class="hmw-prefix">How Might We</div>
          <div class="hmw-text">[HMW statement 3]</div>
        </div>
        <div class="hmw-card">
          <div class="hmw-prefix">How Might We</div>
          <div class="hmw-text">[HMW statement 4]</div>
        </div>
        <div class="hmw-card">
          <div class="hmw-prefix">How Might We</div>
          <div class="hmw-text">[HMW statement 5]</div>
        </div>
      </div>
    </section>

    <!-- ─── 9a-ii. FEATURE LIST (derived from HMW statements) ─── -->
    <!-- This bridges HMW → actual features to build. Shows the "so what" of all the ideation. -->
    <section class="cs-section">
      <div class="cs-section-label">Ideate</div>
      <h2 class="cs-section-title">What features did we decide to build?</h2>
      <p class="cs-body">[Explain how HMW statements were voted on and converted into a prioritized feature list. This shows the link between user problems and design decisions.]</p>
      <div class="feature-list">
        <div class="feature-list-item">
          <div class="feature-list-icon">🔔</div>
          <span class="feature-priority priority-must">Must Have</span>
          <div class="feature-list-name">[Feature 1 — e.g., Smart Notification System]</div>
          <div class="feature-list-desc">[What this feature does and why it matters to users]</div>
          <div class="feature-list-hmw">↳ HMW help users stay informed without feeling overwhelmed?</div>
        </div>
        <div class="feature-list-item">
          <div class="feature-list-icon">🗺️</div>
          <span class="feature-priority priority-must">Must Have</span>
          <div class="feature-list-name">[Feature 2 — e.g., Real-time Order Tracking]</div>
          <div class="feature-list-desc">[Description]</div>
          <div class="feature-list-hmw">↳ HMW reduce user anxiety during waiting time?</div>
        </div>
        <div class="feature-list-item">
          <div class="feature-list-icon">⚡</div>
          <span class="feature-priority priority-should">Should Have</span>
          <div class="feature-list-name">[Feature 3 — e.g., Quick Reorder]</div>
          <div class="feature-list-desc">[Description]</div>
          <div class="feature-list-hmw">↳ HMW make repeat actions effortless?</div>
        </div>
        <div class="feature-list-item">
          <div class="feature-list-icon">💬</div>
          <span class="feature-priority priority-should">Should Have</span>
          <div class="feature-list-name">[Feature 4 — e.g., In-app Chat]</div>
          <div class="feature-list-desc">[Description]</div>
          <div class="feature-list-hmw">↳ HMW help users communicate without leaving the app?</div>
        </div>
        <div class="feature-list-item">
          <div class="feature-list-icon">🎯</div>
          <span class="feature-priority priority-could">Could Have</span>
          <div class="feature-list-name">[Feature 5 — e.g., Personalized Recommendations]</div>
          <div class="feature-list-desc">[Description]</div>
          <div class="feature-list-hmw">↳ HMW surface the right options without overwhelming choice?</div>
        </div>
        <div class="feature-list-item">
          <div class="feature-list-icon">🌐</div>
          <span class="feature-priority priority-could">Could Have</span>
          <div class="feature-list-name">[Feature 6 — e.g., Arabic-first UI]</div>
          <div class="feature-list-desc">[Description]</div>
          <div class="feature-list-hmw">↳ HMW make Arabic users feel the product was built for them?</div>
        </div>
      </div>
      <p style="font-size:var(--text-caption); color:var(--color-text-tertiary); margin-top:var(--space-2);">
        Priority: <span class="feature-priority priority-must" style="vertical-align:middle;">Must Have</span> = core to MVP &nbsp;
        <span class="feature-priority priority-should" style="vertical-align:middle;">Should Have</span> = next sprint &nbsp;
        <span class="feature-priority priority-could" style="vertical-align:middle;">Could Have</span> = future roadmap
      </p>
    </section>

    <!-- ─── 9a-iii. CRAZY 8'S ─── -->
    <!-- Rapid ideation exercise: 8 sketches in 8 minutes. Shows generative thinking breadth. -->
    <section class="cs-section">
      <div class="cs-section-label">Ideate</div>
      <h2 class="cs-section-title">How did we rapidly explore solutions?</h2>
      <div class="method-card">
        <div class="method-question">Crazy 8's</div>
        <span class="method-answer-tag">Rapid Ideation</span>
        <p class="cs-body">[Explain the Crazy 8's exercise — 8 minutes to sketch 8 wildly different solutions to the same problem. The goal isn't polish — it's divergent thinking before converging on the best direction.]</p>
        <p style="font-size:var(--text-body-sm); font-weight:700; margin-bottom:var(--space-3); color:var(--color-text-primary);">Problem we were solving: <span style="font-weight:400; color:var(--color-text-secondary);">[The HMW statement or user problem this session addressed]</span></p>
        <div class="crazy8-grid">
          <div class="crazy8-cell">
            <div class="crazy8-number">1</div>
            <div class="crazy8-sketch-area">[Sketch description or ASCII wireframe of idea 1]</div>
            <div class="crazy8-idea">[Idea name]</div>
          </div>
          <div class="crazy8-cell">
            <div class="crazy8-number">2</div>
            <div class="crazy8-sketch-area">[Idea 2]</div>
            <div class="crazy8-idea">[Idea name]</div>
          </div>
          <div class="crazy8-cell">
            <div class="crazy8-number">3</div>
            <div class="crazy8-sketch-area">[Idea 3]</div>
            <div class="crazy8-idea">[Idea name]</div>
          </div>
          <div class="crazy8-cell">
            <div class="crazy8-number">4</div>
            <div class="crazy8-sketch-area">[Idea 4]</div>
            <div class="crazy8-idea">[Idea name]</div>
          </div>
          <div class="crazy8-cell">
            <div class="crazy8-number">5</div>
            <div class="crazy8-sketch-area">[Idea 5]</div>
            <div class="crazy8-idea">[Idea name]</div>
          </div>
          <div class="crazy8-cell">
            <div class="crazy8-number">6</div>
            <div class="crazy8-sketch-area">[Idea 6]</div>
            <div class="crazy8-idea">[Idea name]</div>
          </div>
          <div class="crazy8-cell">
            <div class="crazy8-number">7</div>
            <div class="crazy8-sketch-area">[Idea 7]</div>
            <div class="crazy8-idea">[Idea name]</div>
          </div>
          <div class="crazy8-cell">
            <div class="crazy8-number">8</div>
            <div class="crazy8-sketch-area">⭐ SELECTED DIRECTION</div>
            <div class="crazy8-idea">[Winner — became the wireframe]</div>
          </div>
        </div>
        <p class="cs-body" style="margin-top:var(--space-6);">We moved forward with idea #[X] — [explain why this direction won: it best addressed the HMW, got the most votes, or tested best with quick hallway testing].</p>
      </div>
    </section>

    <!-- ─── 9b. CARD SORTING + SITE MAP ─── -->
    <section class="cs-section">
      <div class="cs-section-label">Ideate</div>
      <h2 class="cs-section-title">How did we find the best information architecture?</h2>
      <div class="method-card">
        <div class="method-question">Card Sorting</div>
        <span class="method-answer-tag">Information Architecture</span>
        <p class="cs-body">[Explain the card sorting exercise — open vs closed, how many participants, what we discovered about how users mentally group content, and what the result told us about the navigation structure.]</p>
        <div class="method-stats">
          <div>
            <div class="stat-number">[X]</div>
            <div class="stat-label">Participants</div>
          </div>
          <div>
            <div class="stat-number">[XX]</div>
            <div class="stat-label">Cards sorted</div>
          </div>
          <div>
            <div class="stat-number">[X]</div>
            <div class="stat-label">Emergent groups</div>
          </div>
        </div>
        <p style="font-size:var(--text-body-sm); font-weight:700; margin-bottom:var(--space-3); color:var(--color-text-primary);">Key finding:</p>
        <p style="font-size:var(--text-body-sm); color:var(--color-text-secondary);">[What the card sort revealed about user mental models and how it shaped the navigation/IA]</p>
      </div>

      <h3 class="cs-section-subtitle">Site Map</h3>
      <div class="sitemap">
        <div class="sitemap-root">📱 [App Name]</div>
        <pre style="font-family:monospace; font-size:var(--text-body-sm); color:var(--color-text-secondary); line-height:2; background:none; border:none; padding:0; margin-top:var(--space-3);">
├── 🏠 Home / Dashboard
│   ├── [Feature Screen 1]
│   └── [Feature Screen 2]
├── 🔍 [Section 2]
│   ├── [Sub-screen]
│   └── [Sub-screen]
├── ➕ [Core Action Screen]
│   ├── [Step 1]
│   ├── [Step 2]
│   └── Confirmation
├── 👤 Profile
│   ├── Settings
│   └── [Account options]
└── 🔔 Notifications
        </pre>
      </div>
    </section>

    <!-- ─── 9c. USER FLOW ─── -->
    <section class="cs-section">
      <div class="cs-section-label">Ideate</div>
      <h2 class="cs-section-title">User Flow — [Primary Task Name]</h2>
      <p class="cs-body">[Describe what flow this represents and why it's the most important flow to map — it should be the core value-delivery path.]</p>
      <div class="user-flow">
        <div class="flow-steps">
          <div class="flow-step start">
            <div class="flow-step-label">Start</div>
            <div class="flow-step-desc">[Entry point]</div>
          </div>
          <div class="flow-arrow">→</div>
          <div class="flow-step">
            <div class="flow-step-label">[Screen 1]</div>
            <div class="flow-step-desc">[Action]</div>
          </div>
          <div class="flow-arrow">→</div>
          <div class="flow-step decision">
            <div class="flow-step-label">[Decision?]</div>
            <div class="flow-step-desc">Yes / No</div>
          </div>
          <div class="flow-arrow">→</div>
          <div class="flow-step">
            <div class="flow-step-label">[Screen 2]</div>
            <div class="flow-step-desc">[Action]</div>
          </div>
          <div class="flow-arrow">→</div>
          <div class="flow-step">
            <div class="flow-step-label">[Screen 3]</div>
            <div class="flow-step-desc">[Action]</div>
          </div>
          <div class="flow-arrow">→</div>
          <div class="flow-step end">
            <div class="flow-step-label">Goal</div>
            <div class="flow-step-desc">[Outcome]</div>
          </div>
        </div>
      </div>
      <!-- Add more user flows as needed -->
    </section>

    <!-- ─── 9d. WIREFRAMES ─── -->
    <section class="cs-section">
      <div class="cs-section-label">Ideate</div>
      <h2 class="cs-section-title">How did we convert user flow to wireframes?</h2>
      <div class="method-card">
        <div class="method-question">Lo-Fi Wireframes</div>
        <span class="method-answer-tag">Structure & Layout</span>
        <p class="cs-body">[Explain the wireframing process — why lo-fi first, what decisions were being made at this stage (layout, hierarchy, navigation), and how many iterations were done.]</p>
        <div class="cs-3col">
          <!-- For each key wireframe, show a text-based or image representation -->
          <div>
            <div class="wireframe-label">[Screen Name 1]</div>
            <div class="wireframe-frame">
              [Header: Back ← | Title]
              ─────────────────────
              [Hero image block]
              ─────────────────────
              [Card row 1]
              [Card row 2]
              [Card row 3]
              ─────────────────────
              [Primary CTA button]
              ─────────────────────
              [Tab bar: Home|Explore|Profile]
            </div>
          </div>
          <div>
            <div class="wireframe-label">[Screen Name 2]</div>
            <div class="wireframe-frame">
              [Header: ← Back | Screen Title]
              ─────────────────────
              [Input field: Label]
              [Input field: Label]
              [Input field: Label]
              ─────────────────────
              [Helper text]
              ─────────────────────
              [Submit button — full width]
            </div>
          </div>
          <div>
            <div class="wireframe-label">[Screen Name 3]</div>
            <div class="wireframe-frame">
              [Header: Title | Filter icon]
              ─────────────────────
              [Search bar]
              ─────────────────────
              [List item 1: icon + title + meta]
              [List item 2: icon + title + meta]
              [List item 3: icon + title + meta]
              ─────────────────────
              [FAB: + button]
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- ═══════════════════════ DESIGN SYSTEM ═══════════════════════ -->

    <section class="cs-section">
      <div class="cs-section-label">Design System</div>
      <h2 class="cs-section-title">How did we unify the design components?</h2>
      <p class="cs-body">[Explain what a design system is and why it's essential for consistency — especially across multiple designers or platforms. Mention the chosen design school from Phase 4.7.]</p>

      <!-- ─── COLOR PALETTE ─── -->
      <h3 class="cs-section-subtitle">Color Palette</h3>
      <p style="font-size:var(--text-body-sm); color:var(--color-text-secondary); margin-bottom:var(--space-6);">All colors are generated from the brand palette using a 50→950 scale. Every value used in the product maps to one of these tokens — no hardcoded hex values.</p>

      <!-- Primary Scale -->
      <div class="color-scale">
        <div class="color-scale-label">Primary — [Color Name]</div>
        <div class="color-swatches">
          <div class="swatch" style="background:[primary-50-hex]"><span class="swatch-step" style="color:#374151">50</span></div>
          <div class="swatch" style="background:[primary-100-hex]"><span class="swatch-step" style="color:#374151">100</span></div>
          <div class="swatch" style="background:[primary-200-hex]"><span class="swatch-step" style="color:#374151">200</span></div>
          <div class="swatch" style="background:[primary-300-hex]"><span class="swatch-step" style="color:#374151">300</span></div>
          <div class="swatch" style="background:[primary-400-hex]"><span class="swatch-step" style="color:white">400</span></div>
          <div class="swatch swatch-base" style="background:[primary-500-hex]"><span class="swatch-step" style="color:white">500</span></div>
          <div class="swatch" style="background:[primary-600-hex]"><span class="swatch-step" style="color:white">600</span></div>
          <div class="swatch" style="background:[primary-700-hex]"><span class="swatch-step" style="color:white">700</span></div>
          <div class="swatch" style="background:[primary-800-hex]"><span class="swatch-step" style="color:white">800</span></div>
          <div class="swatch" style="background:[primary-900-hex]"><span class="swatch-step" style="color:white">900</span></div>
          <div class="swatch" style="background:[primary-950-hex]"><span class="swatch-step" style="color:white">950</span></div>
        </div>
      </div>

      <!-- Secondary Scale -->
      <div class="color-scale">
        <div class="color-scale-label">Secondary — [Color Name]</div>
        <div class="color-swatches">
          <!-- [Repeat swatch pattern for secondary] -->
        </div>
      </div>

      <!-- Neutral Scale -->
      <div class="color-scale">
        <div class="color-scale-label">Neutral — Gray</div>
        <div class="color-swatches">
          <!-- [Repeat swatch pattern for gray] -->
        </div>
      </div>

      <!-- Semantic -->
      <div class="color-scale">
        <div class="color-scale-label">Semantic</div>
        <div class="cs-2col" style="margin-top:var(--space-3);">
          <div style="display:flex; gap:var(--space-3); align-items:center;">
            <div style="width:48px; height:48px; border-radius:var(--radius-md); background:[success-hex];"></div>
            <div><div style="font-weight:700; font-size:var(--text-body-sm);">Success</div><div style="font-size:var(--text-caption); color:var(--color-text-secondary);">[hex]</div></div>
          </div>
          <div style="display:flex; gap:var(--space-3); align-items:center;">
            <div style="width:48px; height:48px; border-radius:var(--radius-md); background:[warning-hex];"></div>
            <div><div style="font-weight:700; font-size:var(--text-body-sm);">Warning</div><div style="font-size:var(--text-caption); color:var(--color-text-secondary);">[hex]</div></div>
          </div>
          <div style="display:flex; gap:var(--space-3); align-items:center;">
            <div style="width:48px; height:48px; border-radius:var(--radius-md); background:[error-hex];"></div>
            <div><div style="font-weight:700; font-size:var(--text-body-sm);">Error</div><div style="font-size:var(--text-caption); color:var(--color-text-secondary);">[hex]</div></div>
          </div>
          <div style="display:flex; gap:var(--space-3); align-items:center;">
            <div style="width:48px; height:48px; border-radius:var(--radius-md); background:[info-hex];"></div>
            <div><div style="font-weight:700; font-size:var(--text-body-sm);">Info</div><div style="font-size:var(--text-caption); color:var(--color-text-secondary);">[hex]</div></div>
          </div>
        </div>
      </div>

      <!-- ─── TYPOGRAPHY ─── -->
      <h3 class="cs-section-subtitle">Typography</h3>
      <p style="font-size:var(--text-body-sm); color:var(--color-text-secondary); margin-bottom:var(--space-4);">One font family. All hierarchy is expressed through size and weight alone. Typescale ratio: [X.XXX — ratio name]</p>
      <div class="cs-card" style="overflow-x:auto;">
        <table class="type-table">
          <thead>
            <tr style="border-bottom:2px solid var(--color-border);">
              <td class="type-name" style="font-weight:700; color:var(--color-text-primary);">Level</td>
              <td class="type-spec" style="font-weight:700; color:var(--color-text-primary);">Specs</td>
              <td style="font-weight:700; color:var(--color-text-primary); padding:var(--space-3) var(--space-4);">Sample</td>
            </tr>
          </thead>
          <tbody>
            <tr class="type-row"><td class="type-name">Display</td><td class="type-spec">[size]px / [lh]px / 700</td><td class="type-sample" style="font-size:[size]px; font-weight:700; line-height:[lh]px;">[Project Name]</td></tr>
            <tr class="type-row"><td class="type-name">H1</td><td class="type-spec">[size]px / [lh]px / 700</td><td class="type-sample" style="font-size:[size]px; font-weight:700;">Page Heading</td></tr>
            <tr class="type-row"><td class="type-name">H2</td><td class="type-spec">[size]px / [lh]px / 600</td><td class="type-sample" style="font-size:[size]px; font-weight:600;">Section Heading</td></tr>
            <tr class="type-row"><td class="type-name">H3</td><td class="type-spec">[size]px / [lh]px / 600</td><td class="type-sample" style="font-size:[size]px; font-weight:600;">Subsection</td></tr>
            <tr class="type-row"><td class="type-name">H4</td><td class="type-spec">[size]px / [lh]px / 600</td><td class="type-sample" style="font-size:[size]px; font-weight:600;">Card Title</td></tr>
            <tr class="type-row"><td class="type-name">Body Large</td><td class="type-spec">[size]px / [lh]px / 400</td><td class="type-sample" style="font-size:[size]px;">Introductory paragraph text</td></tr>
            <tr class="type-row"><td class="type-name">Body</td><td class="type-spec">16px / 24px / 400</td><td class="type-sample" style="font-size:16px;">Main body text for reading</td></tr>
            <tr class="type-row"><td class="type-name">Body Small</td><td class="type-spec">[size]px / [lh]px / 400</td><td class="type-sample" style="font-size:[size]px; color:var(--color-text-secondary);">Secondary and supporting text</td></tr>
            <tr class="type-row"><td class="type-name">Caption</td><td class="type-spec">[size]px / [lh]px / 400</td><td class="type-sample" style="font-size:[size]px; color:var(--color-text-tertiary);">Labels, timestamps, metadata</td></tr>
            <tr class="type-row"><td class="type-name">Label</td><td class="type-spec">12px / 16px / 500 / ALL CAPS</td><td class="type-sample" style="font-size:12px; font-weight:500; letter-spacing:0.08em; text-transform:uppercase; color:var(--color-text-tertiary);">TAG · BADGE · STATUS</td></tr>
          </tbody>
        </table>
      </div>

      <!-- ─── ICONOGRAPHY ─── -->
      <h3 class="cs-section-subtitle">Iconography</h3>
      <p style="font-size:var(--text-body-sm); color:var(--color-text-secondary); margin-bottom:var(--space-4);">Icon style: [Outlined / Filled / Rounded / Sharp] · Size: 24px standard, 20px compact · Library: [e.g., Phosphor Icons / Material Symbols / Heroicons]</p>
      <div class="icon-grid">
        <div class="icon-item"><div class="icon-preview">[icon]</div>[name]</div>
        <div class="icon-item"><div class="icon-preview">[icon]</div>[name]</div>
        <div class="icon-item"><div class="icon-preview">[icon]</div>[name]</div>
        <div class="icon-item"><div class="icon-preview">[icon]</div>[name]</div>
        <div class="icon-item"><div class="icon-preview">[icon]</div>[name]</div>
        <div class="icon-item"><div class="icon-preview">[icon]</div>[name]</div>
        <div class="icon-item"><div class="icon-preview">[icon]</div>[name]</div>
        <div class="icon-item"><div class="icon-preview">[icon]</div>[name]</div>
      </div>

      <!-- ─── SPACING ─── -->
      <h3 class="cs-section-subtitle">Spacing — 8pt Grid</h3>
      <p style="font-size:var(--text-body-sm); color:var(--color-text-secondary); margin-bottom:var(--space-4);">All spacing values are multiples of 8px. The 8pt grid creates automatic visual harmony across the entire product.</p>
      <div class="cs-card">
        <div class="spacing-row"><div class="spacing-bar" style="width:4px;"></div><div class="spacing-info"><span class="spacing-token">--space-1: 4px</span> — Micro gaps (icon-to-label)</div></div>
        <div class="spacing-row"><div class="spacing-bar" style="width:8px;"></div><div class="spacing-info"><span class="spacing-token">--space-2: 8px</span> — Tight spacing (between inline elements)</div></div>
        <div class="spacing-row"><div class="spacing-bar" style="width:16px;"></div><div class="spacing-info"><span class="spacing-token">--space-4: 16px</span> — Standard (card padding, list items)</div></div>
        <div class="spacing-row"><div class="spacing-bar" style="width:24px;"></div><div class="spacing-info"><span class="spacing-token">--space-6: 24px</span> — Medium (between form fields, card gaps)</div></div>
        <div class="spacing-row"><div class="spacing-bar" style="width:32px;"></div><div class="spacing-info"><span class="spacing-token">--space-8: 32px</span> — Large (between sections)</div></div>
        <div class="spacing-row"><div class="spacing-bar" style="width:48px;"></div><div class="spacing-info"><span class="spacing-token">--space-12: 48px</span> — Section start</div></div>
        <div class="spacing-row"><div class="spacing-bar" style="width:64px;"></div><div class="spacing-info"><span class="spacing-token">--space-16: 64px</span> — Major section breaks (mobile)</div></div>
        <div class="spacing-row"><div class="spacing-bar" style="width:80px;"></div><div class="spacing-info"><span class="spacing-token">--space-20: 80px</span> — Major section breaks (desktop)</div></div>
      </div>

      <!-- ─── GRID SYSTEM ─── -->
      <h3 class="cs-section-subtitle">Grid System</h3>
      <div class="cs-2col">
        <div>
          <div class="wireframe-label" style="margin-bottom:var(--space-3);">Mobile — 375px</div>
          <div class="grid-diagram">
            <div class="grid-columns">
              <div class="grid-col-block"></div>
              <div class="grid-col-block"></div>
              <div class="grid-col-block"></div>
              <div class="grid-col-block"></div>
            </div>
            <div class="grid-spec-row">
              <div class="grid-spec-item"><div class="grid-spec-label">Columns</div><div class="grid-spec-value">4</div></div>
              <div class="grid-spec-item"><div class="grid-spec-label">Margin</div><div class="grid-spec-value">16px</div></div>
              <div class="grid-spec-item"><div class="grid-spec-label">Gutter</div><div class="grid-spec-value">16px</div></div>
            </div>
          </div>
        </div>
        <div>
          <div class="wireframe-label" style="margin-bottom:var(--space-3);">Desktop — 1280px</div>
          <div class="grid-diagram">
            <div class="grid-columns">
              <div class="grid-col-block"></div><div class="grid-col-block"></div>
              <div class="grid-col-block"></div><div class="grid-col-block"></div>
              <div class="grid-col-block"></div><div class="grid-col-block"></div>
              <div class="grid-col-block"></div><div class="grid-col-block"></div>
              <div class="grid-col-block"></div><div class="grid-col-block"></div>
              <div class="grid-col-block"></div><div class="grid-col-block"></div>
            </div>
            <div class="grid-spec-row">
              <div class="grid-spec-item"><div class="grid-spec-label">Columns</div><div class="grid-spec-value">12</div></div>
              <div class="grid-spec-item"><div class="grid-spec-label">Margin</div><div class="grid-spec-value">80px</div></div>
              <div class="grid-spec-item"><div class="grid-spec-label">Gutter</div><div class="grid-spec-value">24px</div></div>
            </div>
          </div>
        </div>
      </div>
    </section>

      <!-- ─── BEFORE / AFTER COMPARISON ─── -->
      <h3 class="cs-section-subtitle">Before & After — Design Transformation</h3>
      <p style="font-size:var(--text-body-sm); color:var(--color-text-secondary); margin-bottom:var(--space-4);">Comparing the original/competitor experience to our redesign — shows the concrete improvement we made.</p>
      <div class="before-after">
        <div class="before-pane">
          <div class="ba-header">
            <div class="ba-label">❌ Before — [e.g., Competitor / Old Design]</div>
          </div>
          <div class="ba-content">
            <!-- Embed screenshot of old design, or describe it visually -->
            [Screenshot or description of the old/competitor screen — show the pain point visually]
          </div>
        </div>
        <div class="after-pane">
          <div class="ba-header">
            <div class="ba-label">✅ After — Our Solution</div>
          </div>
          <div class="ba-content">
            <!-- Embed the actual designed screen at reduced scale -->
            [Our redesigned screen — same context, dramatically better experience]
          </div>
        </div>
      </div>
      <p style="font-size:var(--text-body-sm); color:var(--color-text-secondary); margin-top:var(--space-4);">Key improvement: [One clear sentence about what changed and why it matters to users]</p>

      <!-- Add more before/after pairs for each major redesign decision -->

      <!-- ─── COMPONENTS LIBRARY ─── -->
      <h3 class="cs-section-subtitle">Components Library</h3>
      <p style="font-size:var(--text-body-sm); color:var(--color-text-secondary); margin-bottom:var(--space-4);">Reusable UI components built on top of the design tokens. Every element in the product maps to one of these components — no one-off designs.</p>
      <div class="component-library">
        <div class="component-card">
          <div class="component-preview">
            <!-- Embed the actual component HTML here — buttons, inputs, cards, etc. -->
            <button style="background:var(--color-primary); color:white; border:none; padding:10px 20px; border-radius:var(--radius-pill); font-weight:600; cursor:pointer;">Primary Button</button>
          </div>
          <div class="component-info">
            <div class="component-name">Button — Primary</div>
            <div class="component-variants">Variants: Default, Hover, Disabled, Loading</div>
          </div>
        </div>
        <div class="component-card">
          <div class="component-preview">
            <button style="background:transparent; color:var(--color-primary); border:2px solid var(--color-primary); padding:10px 20px; border-radius:var(--radius-pill); font-weight:600; cursor:pointer;">Secondary Button</button>
          </div>
          <div class="component-info">
            <div class="component-name">Button — Secondary</div>
            <div class="component-variants">Variants: Default, Hover, Disabled</div>
          </div>
        </div>
        <div class="component-card">
          <div class="component-preview">
            <div style="border:1px solid var(--color-border); border-radius:var(--radius-md); padding:10px 14px; width:100%; font-size:var(--text-body-sm); color:var(--color-text-tertiary);">Input field placeholder</div>
          </div>
          <div class="component-info">
            <div class="component-name">Input Field</div>
            <div class="component-variants">States: Empty, Focused, Filled, Error</div>
          </div>
        </div>
        <div class="component-card">
          <div class="component-preview">
            <div style="background:var(--color-bg-card); border:1px solid var(--color-border); border-radius:var(--radius-lg); padding:12px 16px; box-shadow:var(--shadow-sm); font-size:var(--text-body-sm);">Card Component</div>
          </div>
          <div class="component-info">
            <div class="component-name">Card</div>
            <div class="component-variants">Variants: Default, Elevated, Outlined</div>
          </div>
        </div>
        <div class="component-card">
          <div class="component-preview">
            <div style="display:flex; gap:4px;">
              <div style="padding:6px 14px; background:var(--color-primary); color:white; border-radius:var(--radius-pill); font-size:12px; font-weight:600;">Active</div>
              <div style="padding:6px 14px; background:var(--color-bg-page); border:1px solid var(--color-border); border-radius:var(--radius-pill); font-size:12px; color:var(--color-text-secondary);">Tab 2</div>
              <div style="padding:6px 14px; background:var(--color-bg-page); border:1px solid var(--color-border); border-radius:var(--radius-pill); font-size:12px; color:var(--color-text-secondary);">Tab 3</div>
            </div>
          </div>
          <div class="component-info">
            <div class="component-name">Tab Bar / Segmented Control</div>
            <div class="component-variants">States: Active, Default, Disabled</div>
          </div>
        </div>
        <div class="component-card">
          <div class="component-preview">
            <div style="display:inline-block; background:var(--color-primary-subtle); color:var(--color-primary); padding:4px 12px; border-radius:var(--radius-pill); font-size:12px; font-weight:600;">Badge / Tag</div>
          </div>
          <div class="component-info">
            <div class="component-name">Badge / Status Tag</div>
            <div class="component-variants">Colors: Primary, Success, Warning, Error</div>
          </div>
        </div>
        <!-- Add more components: Bottom Sheet, Toast/Snackbar, Avatar, Empty State, Skeleton... -->
      </div>
    </section>

    <!-- ═══════════════════════ SCREENS ═══════════════════════ -->
    <section class="cs-section">
      <div class="cs-section-label">Final Design</div>
      <h2 class="cs-section-title">The Solution — UI Screens</h2>
      <p class="cs-body">[Brief narrative connecting the design decisions to the screens. What the design achieves for users. How the screens implement the insights from research.]</p>
      <div class="screens-preview">
        <!-- Repeat for each key screen -->
        <div class="screen-thumb">
          <div class="screen-thumb-inner">
            <!-- Embed the actual screen HTML here at 0.4 scale using transform:scale() -->
          </div>
          <div class="screen-thumb-label">[Screen Name]</div>
          <div class="screen-thumb-desc">[What this screen does for the user]</div>
        </div>
      </div>
      <div style="text-align:center; margin-top:var(--space-8);">
        <a href="screens.html" style="display:inline-block; background:var(--color-primary); color:white; padding:14px 32px; border-radius:var(--radius-pill); font-weight:600; text-decoration:none; font-size:var(--text-body);">View All Screens & Interactive Prototype →</a>
      </div>
    </section>

    <!-- ═══════════════════════ LESSONS LEARNED ═══════════════════════ -->
    <section class="cs-section">
      <div class="cs-section-label">Reflection</div>
      <h2 class="cs-section-title">What I Learned</h2>
      <p class="cs-body">[Honest, specific reflection on the project. What surprised you? What assumption was wrong? What would you do differently? This is what makes a portfolio piece credible.]</p>
      <div class="lesson-item">
        <div class="lesson-number">1</div>
        <div>
          <div class="lesson-title">[Lesson title — e.g., "Research reveals what assumptions hide"]</div>
          <div class="lesson-desc">[Specific: what you assumed, what the research showed instead, and how it changed your design direction]</div>
        </div>
      </div>
      <div class="lesson-item">
        <div class="lesson-number">2</div>
        <div>
          <div class="lesson-title">[Lesson 2]</div>
          <div class="lesson-desc">[Specific and honest — not generic wisdom]</div>
        </div>
      </div>
      <div class="lesson-item">
        <div class="lesson-number">3</div>
        <div>
          <div class="lesson-title">[Lesson 3]</div>
          <div class="lesson-desc">[What you'd do differently next time]</div>
        </div>
      </div>
    </section>

    <!-- Nav back -->
    <div style="margin-top:var(--space-20); text-align:center; border-top:1px solid var(--color-border); padding-top:var(--space-8);">
      <a href="index.html" style="color:var(--color-primary); font-weight:600; text-decoration:none;">← Back to Project Hub</a>
    </div>

  </div>
</div>

<!-- ═══════════════════════════════════════════════ ARABIC ═══ -->
<div id="content-ar" class="lang-block" style="display:none;" dir="rtl">
  <div class="cs-wrapper">
    <!-- [Exact same structure as English — all content fully translated to natural Arabic] -->
    <!-- Use the same CSS classes — they adapt automatically with dir="rtl" -->
    <!-- Arabic persona may have an Arabic name and Arab-specific context -->
    <!-- Arabic copy must feel native, not translated word-for-word -->
  </div>
</div>

<script>
function setLang(lang, btn) {
  document.querySelectorAll('.lang-block').forEach(el => el.style.display = 'none');
  document.getElementById('content-' + lang).style.display = 'block';
  document.querySelectorAll('.lang-btn').forEach(b => b.classList.remove('active'));
  btn.classList.add('active');
}
</script>
</body>
</html>
```

---

## index.html — Project Hub Template

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>[Project Name] — DesignXI</title>
  <link href="https://fonts.googleapis.com/css2?family=[Font]:wght@400;600;700&family=Tajawal:wght@400;500;600;700&display=swap" rel="stylesheet">
  <style>
    /* [Paste shared CSS here] */
    .hub-container { max-width: 960px; margin: 0 auto; padding: var(--space-12) var(--space-6); }
    .project-header { text-align: center; margin-bottom: var(--space-12); }
    .project-badge { display: inline-block; background: var(--color-primary); color: white; padding: 4px 12px; border-radius: var(--radius-pill); font-size: var(--text-caption); font-weight: 600; text-transform: uppercase; letter-spacing: 0.08em; margin-bottom: var(--space-4); }
    .project-title { font-size: var(--text-display); font-weight: 700; margin-bottom: var(--space-3); }
    .project-subtitle { font-size: var(--text-body-lg); color: var(--color-text-secondary); max-width: 600px; margin: 0 auto; }
    .phases-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: var(--space-4); margin-bottom: var(--space-12); }
    .phase-card { background: white; border-radius: var(--radius-lg); padding: var(--space-6); box-shadow: var(--shadow-sm); border: 1px solid var(--color-border); }
    .phase-number { font-size: var(--text-caption); font-weight: 700; color: var(--color-primary); text-transform: uppercase; letter-spacing: 0.08em; margin-bottom: var(--space-2); }
    .phase-name { font-size: var(--text-h4); font-weight: 600; margin-bottom: var(--space-2); }
    .phase-desc { font-size: var(--text-body-sm); color: var(--color-text-secondary); }
    .nav-cards { display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: var(--space-4); }
    .nav-card { background: white; border-radius: var(--radius-lg); padding: var(--space-6); box-shadow: var(--shadow-sm); text-decoration: none; color: inherit; border: 2px solid transparent; transition: all 0.2s; display: flex; flex-direction: column; align-items: flex-start; }
    .nav-card:hover { border-color: var(--color-primary); box-shadow: var(--shadow-md); transform: translateY(-2px); }
    .nav-card-icon { font-size: 2rem; margin-bottom: var(--space-3); }
    .nav-card-title { font-size: var(--text-h4); font-weight: 600; margin-bottom: var(--space-2); }
    .nav-card-desc { font-size: var(--text-body-sm); color: var(--color-text-secondary); }
    .section-label { font-size: var(--text-body-sm); font-weight: 700; text-transform: uppercase; letter-spacing: 0.08em; color: var(--color-text-tertiary); margin-bottom: var(--space-4); }
  </style>
</head>
<body>
  <div class="lang-switcher">
    <button class="lang-btn active" onclick="setLang('en', this)">English</button>
    <button class="lang-btn" onclick="setLang('ar', this)">العربية</button>
  </div>
  <div id="content-en" class="lang-block">
    <div class="hub-container">
      <header class="project-header">
        <div class="project-badge">DesignXI Project</div>
        <h1 class="project-title">[Project Name]</h1>
        <p class="project-subtitle">[One sentence describing the product and audience]</p>
      </header>
      <p class="section-label">Process Overview</p>
      <div class="phases-grid">
        <div class="phase-card"><div class="phase-number">Phase 1</div><div class="phase-name">Discovery</div><div class="phase-desc">[Key finding]</div></div>
        <div class="phase-card"><div class="phase-number">Phase 2</div><div class="phase-name">Research</div><div class="phase-desc">[X interviews, X survey responses, X competitors analyzed]</div></div>
        <div class="phase-card"><div class="phase-number">Phase 3</div><div class="phase-name">Define</div><div class="phase-desc">[X personas, journey map, HMW statements]</div></div>
        <div class="phase-card"><div class="phase-number">Phase 4</div><div class="phase-name">Ideate</div><div class="phase-desc">[X screens, X user flows, card sorting complete]</div></div>
        <div class="phase-card"><div class="phase-number">Phase 5</div><div class="phase-name">UI Design</div><div class="phase-desc">[Design school, color system, X screens]</div></div>
        <div class="phase-card"><div class="phase-number">Phase 6</div><div class="phase-name">Testing</div><div class="phase-desc">[X usability sessions, X issues fixed]</div></div>
      </div>
      <p class="section-label" style="margin-top:var(--space-12);">Deliverables</p>
      <div class="nav-cards">
        <a href="casestudy.html" class="nav-card"><div class="nav-card-icon">📖</div><div class="nav-card-title">Case Study</div><div class="nav-card-desc">Full story from problem to solution</div></a>
        <a href="screens.html" class="nav-card"><div class="nav-card-icon">📱</div><div class="nav-card-title">UI Screens</div><div class="nav-card-desc">Interactive prototype — all flows</div></a>
        <a href="personas.html" class="nav-card"><div class="nav-card-icon">👤</div><div class="nav-card-title">Personas</div><div class="nav-card-desc">Who we designed for</div></a>
        <a href="process.html" class="nav-card"><div class="nav-card-icon">🧠</div><div class="nav-card-title">UX Process</div><div class="nav-card-desc">Thinking behind decisions</div></a>
        <a href="handoff.html" class="nav-card"><div class="nav-card-icon">⚙️</div><div class="nav-card-title">Dev Handoff</div><div class="nav-card-desc">Specs for developers</div></a>
      </div>
    </div>
  </div>
  <div id="content-ar" class="lang-block" style="display:none;" dir="rtl">
    <!-- Arabic version of index.html -->
  </div>
  <script>
  function setLang(lang, btn) {
    document.querySelectorAll('.lang-block').forEach(el => el.style.display = 'none');
    document.getElementById('content-' + lang).style.display = 'block';
    document.querySelectorAll('.lang-btn').forEach(b => b.classList.remove('active'));
    btn.classList.add('active');
  }
  </script>
</body>
</html>
```

---

## personas.html — Persona Cards Template

```html
<!-- Each persona uses this card structure (same as in casestudy.html) -->
<!-- personas.html shows all personas expanded, full detail -->
<!-- Use the persona-card component from the casestudy template above -->
<!-- Include: photo/avatar, quote, goals, frustrations, behaviors, tech level, design insight -->
<!-- Add a short narrative above each card explaining how we arrived at this persona -->
```

---

## screens.html — Interactive Prototype Template

```html
<!--
  screens.html IS the interactive prototype.
  Use the show/hide navigation pattern from references/prototyping.md.
  All screens are in this file, organized by user flow.
  Navigation between screens uses JavaScript show/hide.
  Apply all microinteractions from references/microinteractions.md.
  Include both phone frame (mobile) or browser frame (web) wrappers.
-->
```

---

## process.html — UX Thinking Document

```html
<!--
  process.html explains the WHY behind every decision.
  It mirrors the case study structure but focuses on reasoning, not presentation.
  Each phase section explains:
  - What method was used and why that method
  - What we found
  - What decision it led to
  - What was considered but rejected and why
  Audience: design reviewers, hiring managers, clients who want to understand the process.
-->
```

---

---

## frd.html — Functional Requirements Document Template

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>[Project Name] — FRD</title>
  <link href="https://fonts.googleapis.com/css2?family=[Font]:wght@400;500;600;700&family=Tajawal:wght@400;500;600;700&display=swap" rel="stylesheet">
  <style>
    /* [Paste shared CSS tokens here] */
    .frd-wrapper { max-width: 960px; margin: 0 auto; padding: var(--space-8) var(--space-6) var(--space-20); }
    .frd-header { border-bottom: 3px solid var(--color-primary); padding-bottom: var(--space-6); margin-bottom: var(--space-8); }
    .frd-doc-title { font-size: var(--text-display); font-weight: 700; margin-bottom: var(--space-3); }
    .frd-meta { display: flex; flex-wrap: wrap; gap: var(--space-6); font-size: var(--text-body-sm); color: var(--color-text-secondary); }
    .frd-meta-item strong { color: var(--color-text-primary); }
    .frd-status {
      display: inline-block; padding: 4px 14px; border-radius: var(--radius-pill);
      font-size: var(--text-caption); font-weight: 700; text-transform: uppercase; letter-spacing: 0.08em;
    }
    .status-draft { background: #FFFBEB; color: #D97706; }
    .status-review { background: #EFF6FF; color: #2563EB; }
    .status-approved { background: #F0FDF4; color: #16A34A; }

    /* TOC */
    .frd-toc { background: var(--color-bg-card); border: 1px solid var(--color-border); border-radius: var(--radius-lg); padding: var(--space-6); margin-bottom: var(--space-8); }
    .frd-toc-title { font-size: var(--text-body-sm); font-weight: 700; text-transform: uppercase; letter-spacing: 0.08em; color: var(--color-text-tertiary); margin-bottom: var(--space-4); }
    .frd-toc ol { list-style: decimal; padding-left: var(--space-6); }
    .frd-toc li { padding: var(--space-2) 0; }
    .frd-toc a { color: var(--color-primary); text-decoration: none; font-size: var(--text-body-sm); font-weight: 500; }
    .frd-toc a:hover { text-decoration: underline; }

    /* Section */
    .frd-section { margin-top: var(--space-12); padding-top: var(--space-6); border-top: 2px solid var(--color-border); }
    .frd-section-label { font-size: var(--text-caption); font-weight: 700; text-transform: uppercase; letter-spacing: 0.1em; color: var(--color-primary); margin-bottom: var(--space-2); }
    .frd-section-title { font-size: var(--text-h2); font-weight: 700; margin-bottom: var(--space-6); }
    .frd-subsection { margin-top: var(--space-8); }
    .frd-subsection-title { font-size: var(--text-h4); font-weight: 700; margin-bottom: var(--space-4); color: var(--color-text-primary); }
    .frd-body { font-size: var(--text-body); color: var(--color-text-secondary); line-height: 1.7; margin-bottom: var(--space-4); }

    /* FRD Table */
    .frd-table { width: 100%; border-collapse: collapse; font-size: var(--text-body-sm); margin: var(--space-4) 0; }
    .frd-table th { background: var(--color-primary); color: white; padding: var(--space-3) var(--space-4); text-align: left; font-weight: 600; }
    [dir="rtl"] .frd-table th { text-align: right; }
    .frd-table td { padding: var(--space-3) var(--space-4); border-bottom: 1px solid var(--color-border); color: var(--color-text-secondary); vertical-align: top; }
    .frd-table tr:nth-child(even) td { background: var(--color-bg-page); }

    /* FR Requirement */
    .fr-block { background: var(--color-bg-card); border: 1px solid var(--color-border); border-radius: var(--radius-lg); margin-bottom: var(--space-3); overflow: hidden; }
    .fr-id { display: inline-block; background: var(--color-primary); color: white; padding: 4px 12px; font-size: var(--text-caption); font-weight: 700; font-family: monospace; border-radius: var(--radius-pill); margin-right: var(--space-3); flex-shrink: 0; }
    .fr-row { display: flex; align-items: flex-start; padding: var(--space-4) var(--space-5); gap: var(--space-3); }
    .fr-text { font-size: var(--text-body-sm); color: var(--color-text-primary); line-height: 1.6; flex: 1; }
    .fr-priority { display: inline-block; padding: 2px 8px; border-radius: var(--radius-pill); font-size: 10px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.06em; flex-shrink: 0; }
    .fr-shall { background: #FEF2F2; color: #DC2626; }
    .fr-should { background: #FFFBEB; color: #D97706; }
    .fr-module-header { background: var(--color-primary-subtle); padding: var(--space-3) var(--space-5); border-bottom: 1px solid var(--color-border); font-size: var(--text-caption); font-weight: 700; text-transform: uppercase; letter-spacing: 0.08em; color: var(--color-primary); }

    /* UAT Table */
    .uat-pass { color: #16A34A; font-weight: 700; }
    .uat-fail { color: #DC2626; font-weight: 700; }
    .uat-pending { color: var(--color-text-tertiary); }
    .uat-checkbox { width: 20px; height: 20px; border: 2px solid var(--color-border); border-radius: 4px; display: inline-block; }

    /* Sign-off */
    .signoff-table { width: 100%; border-collapse: collapse; }
    .signoff-table th { background: var(--gray-100); padding: var(--space-3) var(--space-4); text-align: left; font-size: var(--text-body-sm); font-weight: 700; border: 1px solid var(--color-border); }
    .signoff-table td { padding: var(--space-4) var(--space-4); border: 1px solid var(--color-border); height: 48px; font-size: var(--text-body-sm); color: var(--color-text-secondary); }
  </style>
</head>
<body>
<div class="lang-switcher">
  <button class="lang-btn active" onclick="setLang('en', this)">English</button>
  <button class="lang-btn" onclick="setLang('ar', this)">العربية</button>
</div>

<div id="content-en" class="lang-block">
<div class="frd-wrapper">

  <!-- ─── DOCUMENT HEADER ─── -->
  <div class="frd-header">
    <div style="display:flex; align-items:center; gap:var(--space-3); margin-bottom:var(--space-3);">
      <span class="frd-status status-draft">Draft</span>
      <!-- status-draft / status-review / status-approved -->
      <span style="font-size:var(--text-caption); color:var(--color-text-tertiary);">v[1.0] · [DD/MM/YYYY]</span>
    </div>
    <div class="frd-doc-title">[Project Name] — Functional Requirements Document</div>
    <div class="frd-meta">
      <div class="frd-meta-item"><strong>Author:</strong> [Name, Role]</div>
      <div class="frd-meta-item"><strong>Based on BRD:</strong> v[X.X] dated [DD/MM/YYYY]</div>
      <div class="frd-meta-item"><strong>Platform:</strong> [iOS / Android / Web]</div>
      <div class="frd-meta-item"><strong>Review deadline:</strong> [DD/MM/YYYY]</div>
    </div>
  </div>

  <!-- ─── TABLE OF CONTENTS ─── -->
  <div class="frd-toc">
    <div class="frd-toc-title">Table of Contents</div>
    <ol>
      <li><a href="#overview">Overview / Objective</a></li>
      <li><a href="#scope">Scope</a></li>
      <li><a href="#user-roles">User Roles</a></li>
      <li><a href="#user-flows">User Flows</a></li>
      <li><a href="#functional-requirements">Functional Requirements</a></li>
      <li><a href="#pages-screens">Pages / Screens</a></li>
      <li><a href="#integrations">Integrations</a></li>
      <li><a href="#data-handling">Data Handling</a></li>
      <li><a href="#business-rules">Business Rules</a></li>
      <li><a href="#error-handling">Error Handling</a></li>
      <li><a href="#responsiveness">Responsiveness</a></li>
      <li><a href="#permissions-security">Permissions & Security</a></li>
      <li><a href="#kpis">KPIs / Success Metrics</a></li>
      <li><a href="#uat">UAT — Acceptance Test Cases</a></li>
      <li><a href="#signoff">Sign-off</a></li>
    </ol>
  </div>

  <!-- ─── 1. OVERVIEW ─── -->
  <div id="overview" class="frd-section">
    <div class="frd-section-label">Section 1</div>
    <h2 class="frd-section-title">Overview / Objective</h2>
    <p class="frd-body">[2-3 sentences: What this FRD specifies, what system it covers, and what decision or build phase it supports.]</p>
    <p class="frd-body"><strong>Out of scope:</strong> [What is explicitly excluded from this version — be precise]</p>
  </div>

  <!-- ─── 2. SCOPE ─── -->
  <div id="scope" class="frd-section">
    <div class="frd-section-label">Section 2</div>
    <h2 class="frd-section-title">Scope</h2>
    <div class="cs-2col">
      <div class="cs-card">
        <div class="cs-card-title" style="margin-bottom:var(--space-3);">✅ In Scope</div>
        <ul style="list-style:none; font-size:var(--text-body-sm); color:var(--color-text-secondary);">
          <li style="padding:6px 0; border-bottom:1px solid var(--color-border);">✦ [Module or feature 1]</li>
          <li style="padding:6px 0; border-bottom:1px solid var(--color-border);">✦ [Module or feature 2]</li>
          <li style="padding:6px 0;">✦ [Module or feature 3]</li>
        </ul>
      </div>
      <div class="cs-card">
        <div class="cs-card-title" style="margin-bottom:var(--space-3);">❌ Out of Scope (v1)</div>
        <ul style="list-style:none; font-size:var(--text-body-sm); color:var(--color-text-secondary);">
          <li style="padding:6px 0; border-bottom:1px solid var(--color-border);">✦ [Feature deferred to v2]</li>
          <li style="padding:6px 0; border-bottom:1px solid var(--color-border);">✦ [Integration not included]</li>
          <li style="padding:6px 0;">✦ [Platform excluded]</li>
        </ul>
      </div>
    </div>
    <div class="cs-card" style="margin-top:var(--space-4);">
      <div class="cs-card-title" style="margin-bottom:var(--space-3);">⚠️ Assumptions</div>
      <ul style="list-style:none; font-size:var(--text-body-sm); color:var(--color-text-secondary);">
        <li style="padding:6px 0; border-bottom:1px solid var(--color-border);">✦ [Technical assumption]</li>
        <li style="padding:6px 0; border-bottom:1px solid var(--color-border);">✦ [Business assumption]</li>
        <li style="padding:6px 0;">✦ [Design assumption]</li>
      </ul>
    </div>
  </div>

  <!-- ─── 3. USER ROLES ─── -->
  <div id="user-roles" class="frd-section">
    <div class="frd-section-label">Section 3</div>
    <h2 class="frd-section-title">User Roles</h2>
    <table class="frd-table">
      <thead><tr><th>Role</th><th>Description</th><th>Access Level</th><th>Key Permissions</th></tr></thead>
      <tbody>
        <tr><td><strong>Guest</strong></td><td>Unauthenticated visitor</td><td>Public</td><td>Browse, view, search</td></tr>
        <tr><td><strong>Registered User</strong></td><td>Authenticated customer</td><td>Standard</td><td>All guest + checkout, profile, history</td></tr>
        <tr><td><strong>Admin</strong></td><td>Internal team member</td><td>Full</td><td>All + manage products, users, reports</td></tr>
        <tr><td><strong>[Custom Role]</strong></td><td>[Description]</td><td>[Level]</td><td>[Permissions]</td></tr>
      </tbody>
    </table>
  </div>

  <!-- ─── 4. USER FLOWS ─── -->
  <div id="user-flows" class="frd-section">
    <div class="frd-section-label">Section 4</div>
    <h2 class="frd-section-title">User Flows</h2>
    <p class="frd-body">Each flow maps to UI screens and functional requirements for full traceability.</p>
    <table class="frd-table">
      <thead><tr><th>Flow ID</th><th>Flow Name</th><th>Trigger</th><th>Happy Path End State</th><th>FR References</th></tr></thead>
      <tbody>
        <tr><td><strong>UF-01</strong></td><td>Registration & Onboarding</td><td>User opens app</td><td>User lands on Home</td><td>FR-AUTH-01, 02</td></tr>
        <tr><td><strong>UF-02</strong></td><td>Browse & Search</td><td>User taps Search</td><td>Results shown</td><td>FR-SEARCH-01 thru 04</td></tr>
        <tr><td><strong>UF-03</strong></td><td>[Core Transaction]</td><td>User initiates [X]</td><td>Success confirmation</td><td>FR-[MOD]-01 thru 05</td></tr>
        <tr><td><strong>UF-04</strong></td><td>Profile Management</td><td>User opens Profile</td><td>Settings updated</td><td>FR-AUTH-06</td></tr>
      </tbody>
    </table>
  </div>

  <!-- ─── 5. FUNCTIONAL REQUIREMENTS ─── -->
  <div id="functional-requirements" class="frd-section">
    <div class="frd-section-label">Section 5</div>
    <h2 class="frd-section-title">Functional Requirements</h2>
    <p class="frd-body">Format: FR-[MODULE]-[N]. "Shall" = mandatory. "Should" = preferred. Every requirement is testable.</p>

    <!-- Auth Module -->
    <div class="fr-block">
      <div class="fr-module-header">🔐 Authentication</div>
      <div class="fr-row"><span class="fr-id">FR-AUTH-01</span><span class="fr-text">The system <strong>shall</strong> allow users to register with email and password.</span><span class="fr-priority fr-shall">SHALL</span></div>
      <div class="fr-row" style="border-top:1px solid var(--color-border);"><span class="fr-id">FR-AUTH-02</span><span class="fr-text">The system <strong>shall</strong> validate email format inline (not only on submit).</span><span class="fr-priority fr-shall">SHALL</span></div>
      <div class="fr-row" style="border-top:1px solid var(--color-border);"><span class="fr-id">FR-AUTH-03</span><span class="fr-text">The system <strong>shall</strong> send a verification email within 60 seconds of registration.</span><span class="fr-priority fr-shall">SHALL</span></div>
      <div class="fr-row" style="border-top:1px solid var(--color-border);"><span class="fr-id">FR-AUTH-04</span><span class="fr-text">The system <strong>shall</strong> lock account after 5 consecutive failed login attempts for 30 minutes.</span><span class="fr-priority fr-shall">SHALL</span></div>
      <div class="fr-row" style="border-top:1px solid var(--color-border);"><span class="fr-id">FR-AUTH-05</span><span class="fr-text">The system <strong>should</strong> support Sign in with Google and Apple (OAuth 2.0).</span><span class="fr-priority fr-should">SHOULD</span></div>
    </div>

    <!-- Core Feature Module — repeat pattern -->
    <div class="fr-block">
      <div class="fr-module-header">⚡ [Core Feature Module]</div>
      <div class="fr-row"><span class="fr-id">FR-[MOD]-01</span><span class="fr-text">[Requirement — use "shall" for mandatory, testable criterion]</span><span class="fr-priority fr-shall">SHALL</span></div>
      <div class="fr-row" style="border-top:1px solid var(--color-border);"><span class="fr-id">FR-[MOD]-02</span><span class="fr-text">[Requirement with measurable criterion — e.g., "within 2 seconds"]</span><span class="fr-priority fr-shall">SHALL</span></div>
      <div class="fr-row" style="border-top:1px solid var(--color-border);"><span class="fr-id">FR-[MOD]-03</span><span class="fr-text">[Preferred behavior]</span><span class="fr-priority fr-should">SHOULD</span></div>
    </div>

    <!-- Search Module -->
    <div class="fr-block">
      <div class="fr-module-header">🔍 Search</div>
      <div class="fr-row"><span class="fr-id">FR-SEARCH-01</span><span class="fr-text">The system <strong>shall</strong> return results within 1.5 seconds for any query.</span><span class="fr-priority fr-shall">SHALL</span></div>
      <div class="fr-row" style="border-top:1px solid var(--color-border);"><span class="fr-id">FR-SEARCH-02</span><span class="fr-text">The system <strong>shall</strong> support Arabic and English search queries equally.</span><span class="fr-priority fr-shall">SHALL</span></div>
      <div class="fr-row" style="border-top:1px solid var(--color-border);"><span class="fr-id">FR-SEARCH-03</span><span class="fr-text">The system <strong>shall</strong> display a "No results" state with alternative suggestions when empty.</span><span class="fr-priority fr-shall">SHALL</span></div>
    </div>
    <!-- Add more modules as needed: Notifications, Payment, Admin, etc. -->
  </div>

  <!-- ─── 6. PAGES / SCREENS ─── -->
  <div id="pages-screens" class="frd-section">
    <div class="frd-section-label">Section 6</div>
    <h2 class="frd-section-title">Pages / Screens</h2>
    <table class="frd-table">
      <thead><tr><th>Screen ID</th><th>Screen Name</th><th>Route / Path</th><th>User Roles</th><th>FR References</th></tr></thead>
      <tbody>
        <tr><td><strong>SCR-01</strong></td><td>Splash / Onboarding</td><td>/onboarding</td><td>Guest</td><td>FR-AUTH-01</td></tr>
        <tr><td><strong>SCR-02</strong></td><td>Login</td><td>/login</td><td>Guest</td><td>FR-AUTH-02, 03, 04, 05</td></tr>
        <tr><td><strong>SCR-03</strong></td><td>Register</td><td>/register</td><td>Guest</td><td>FR-AUTH-01, 02</td></tr>
        <tr><td><strong>SCR-04</strong></td><td>Home / Dashboard</td><td>/home</td><td>User</td><td>FR-[MOD]-01</td></tr>
        <tr><td><strong>SCR-05</strong></td><td>Search Results</td><td>/search</td><td>All</td><td>FR-SEARCH-01, 02, 03</td></tr>
        <tr><td><strong>SCR-06</strong></td><td>Profile</td><td>/profile</td><td>User</td><td>FR-AUTH-06</td></tr>
        <tr><td><strong>SCR-07</strong></td><td>Error / 404</td><td>/error</td><td>All</td><td>FR-ERR-01</td></tr>
        <!-- Add all screens -->
      </tbody>
    </table>
  </div>

  <!-- ─── 7. INTEGRATIONS ─── -->
  <div id="integrations" class="frd-section">
    <div class="frd-section-label">Section 7</div>
    <h2 class="frd-section-title">Integrations</h2>
    <table class="frd-table">
      <thead><tr><th>ID</th><th>Service</th><th>Type</th><th>Purpose</th><th>Auth Method</th><th>Fallback</th></tr></thead>
      <tbody>
        <tr><td><strong>INT-01</strong></td><td>[Payment GW]</td><td>REST API</td><td>Process payments</td><td>API Key + HMAC</td><td>Show manual payment option</td></tr>
        <tr><td><strong>INT-02</strong></td><td>Firebase</td><td>SDK</td><td>Push notifications</td><td>Service Account</td><td>In-app notification only</td></tr>
        <tr><td><strong>INT-03</strong></td><td>[SMS Provider]</td><td>REST API</td><td>OTP verification</td><td>Bearer Token</td><td>Email OTP fallback</td></tr>
        <tr><td><strong>INT-04</strong></td><td>[Analytics]</td><td>SDK</td><td>Event tracking</td><td>Client ID</td><td>Silent fail — no UX impact</td></tr>
      </tbody>
    </table>
  </div>

  <!-- ─── 8. DATA HANDLING ─── -->
  <div id="data-handling" class="frd-section">
    <div class="frd-section-label">Section 8</div>
    <h2 class="frd-section-title">Data Handling</h2>
    <table class="frd-table">
      <thead><tr><th>Field</th><th>Type</th><th>Required</th><th>Validation</th><th>Stored</th><th>Encrypted</th><th>Retention</th></tr></thead>
      <tbody>
        <tr><td>user_email</td><td>String</td><td>Yes</td><td>RFC 5322</td><td>DB</td><td>Yes</td><td>Until deletion</td></tr>
        <tr><td>user_password</td><td>String</td><td>Yes</td><td>Min 8 chars</td><td>DB</td><td>Bcrypt</td><td>Until deletion</td></tr>
        <tr><td>[field_name]</td><td>[type]</td><td>[Y/N]</td><td>[Rule]</td><td>[DB/Cache/None]</td><td>[Y/N]</td><td>[Duration]</td></tr>
      </tbody>
    </table>
    <p class="frd-body" style="margin-top:var(--space-4);"><strong>PII Policy:</strong> [Describe what counts as PII, where stored, who can access, GDPR/PDPL compliance approach]</p>
  </div>

  <!-- ─── 9. BUSINESS RULES ─── -->
  <div id="business-rules" class="frd-section">
    <div class="frd-section-label">Section 9</div>
    <h2 class="frd-section-title">Business Rules</h2>
    <div class="fr-block">
      <div class="fr-row"><span class="fr-id">BR-01</span><span class="fr-text">[Business rule — plain language, unambiguous, traceable to BRD objective]</span></div>
      <div class="fr-row" style="border-top:1px solid var(--color-border);"><span class="fr-id">BR-02</span><span class="fr-text">[Business rule 2]</span></div>
      <div class="fr-row" style="border-top:1px solid var(--color-border);"><span class="fr-id">BR-03</span><span class="fr-text">[Business rule 3]</span></div>
    </div>
  </div>

  <!-- ─── 10. ERROR HANDLING ─── -->
  <div id="error-handling" class="frd-section">
    <div class="frd-section-label">Section 10</div>
    <h2 class="frd-section-title">Error Handling</h2>
    <table class="frd-table">
      <thead><tr><th>Error ID</th><th>Trigger</th><th>Message (EN)</th><th>Message (AR)</th><th>Recovery</th></tr></thead>
      <tbody>
        <tr><td><strong>ERR-01</strong></td><td>Network timeout</td><td>"Connection lost. Please retry."</td><td>"انقطع الاتصال. حاول مجدداً."</td><td>Retry button</td></tr>
        <tr><td><strong>ERR-02</strong></td><td>Invalid credentials</td><td>"Incorrect email or password."</td><td>"بيانات الدخول غير صحيحة."</td><td>Forgot password link</td></tr>
        <tr><td><strong>ERR-03</strong></td><td>Session expired</td><td>"Your session has expired."</td><td>"انتهت جلستك."</td><td>Redirect to login</td></tr>
        <tr><td><strong>ERR-04</strong></td><td>Payment failed</td><td>"Payment not processed. Try again."</td><td>"لم تتم العملية. أعد المحاولة."</td><td>Retry / Alt method</td></tr>
        <tr><td><strong>ERR-05</strong></td><td>Server error</td><td>"Something went wrong."</td><td>"حدث خطأ ما."</td><td>Support link</td></tr>
      </tbody>
    </table>
  </div>

  <!-- ─── 11. RESPONSIVENESS ─── -->
  <div id="responsiveness" class="frd-section">
    <div class="frd-section-label">Section 11</div>
    <h2 class="frd-section-title">Responsiveness</h2>
    <table class="frd-table">
      <thead><tr><th>Name</th><th>Width</th><th>Grid</th><th>Design Approach</th></tr></thead>
      <tbody>
        <tr><td>Mobile</td><td>320–479px</td><td>4 col</td><td>Single column, stacked components</td></tr>
        <tr><td>Tablet</td><td>480–767px</td><td>8 col</td><td>2-column layouts begin</td></tr>
        <tr><td>Desktop</td><td>1024px+</td><td>12 col</td><td>Full layout, max-width: 1440px</td></tr>
      </tbody>
    </table>
    <p class="frd-body" style="margin-top:var(--space-4);">All interactive elements: minimum <strong>44×44px</strong> touch target (WCAG 2.5.5). RTL layout tested at all breakpoints.</p>
  </div>

  <!-- ─── 12. PERMISSIONS & SECURITY ─── -->
  <div id="permissions-security" class="frd-section">
    <div class="frd-section-label">Section 12</div>
    <h2 class="frd-section-title">Permissions & Security</h2>
    <table class="frd-table">
      <thead><tr><th>Role</th><th>Read</th><th>Write</th><th>Delete</th><th>Admin Panel</th><th>User Data</th></tr></thead>
      <tbody>
        <tr><td><strong>Guest</strong></td><td>✓ Public</td><td>✗</td><td>✗</td><td>✗</td><td>✗</td></tr>
        <tr><td><strong>User</strong></td><td>✓</td><td>✓ Own</td><td>✓ Own</td><td>✗</td><td>Own only</td></tr>
        <tr><td><strong>Admin</strong></td><td>✓</td><td>✓</td><td>✓</td><td>✓ Full</td><td>✓ Full</td></tr>
      </tbody>
    </table>
    <p class="frd-body" style="margin-top:var(--space-4);">Security standards: HTTPS enforced, OWASP Top 10 compliance, JWT (24h expiry), 2FA mandatory for admin accounts, no sensitive data in URLs.</p>
  </div>

  <!-- ─── 13. KPIS ─── -->
  <div id="kpis" class="frd-section">
    <div class="frd-section-label">Section 13</div>
    <h2 class="frd-section-title">KPIs / Success Metrics</h2>
    <table class="frd-table">
      <thead><tr><th>Category</th><th>Metric</th><th>Baseline</th><th>Target</th><th>Measurement</th></tr></thead>
      <tbody>
        <tr><td>Acquisition</td><td>Monthly downloads</td><td>—</td><td>[X,000]</td><td>App Store Connect</td></tr>
        <tr><td>Activation</td><td>Onboarding completion</td><td>—</td><td>&gt; 75%</td><td>Analytics funnel</td></tr>
        <tr><td>Engagement</td><td>DAU (Daily Active Users)</td><td>—</td><td>[X,000]</td><td>Analytics</td></tr>
        <tr><td>Retention</td><td>7-day retention</td><td>—</td><td>&gt; 40%</td><td>Cohort analysis</td></tr>
        <tr><td>Performance</td><td>Load time (p95)</td><td>—</td><td>&lt; 2s</td><td>Lighthouse</td></tr>
        <tr><td>Accessibility</td><td>WCAG 2.1 AA</td><td>—</td><td>100%</td><td>Audit</td></tr>
      </tbody>
    </table>
  </div>

  <!-- ─── 14. UAT ─── -->
  <div id="uat" class="frd-section">
    <div class="frd-section-label">Section 14</div>
    <h2 class="frd-section-title">UAT — Acceptance Test Cases</h2>
    <p class="frd-body">Environment: [Staging URL] · Period: [dates] · Testers: [names/roles] · Devices: [list]</p>
    <table class="frd-table">
      <thead><tr><th>UAT-ID</th><th>Screen</th><th>FR Ref</th><th>Scenario</th><th>Expected Result</th><th>Result</th></tr></thead>
      <tbody>
        <tr><td><strong>UAT-01</strong></td><td>SCR-02</td><td>FR-AUTH-01</td><td>Register with valid email</td><td>Account created, email sent &lt; 60s</td><td><span class="uat-checkbox"></span></td></tr>
        <tr><td><strong>UAT-02</strong></td><td>SCR-02</td><td>FR-AUTH-02</td><td>Invalid email format</td><td>Inline error shown immediately</td><td><span class="uat-checkbox"></span></td></tr>
        <tr><td><strong>UAT-03</strong></td><td>SCR-02</td><td>FR-AUTH-04</td><td>5 failed logins → lockout</td><td>Account locked, message shown</td><td><span class="uat-checkbox"></span></td></tr>
        <tr><td><strong>UAT-04</strong></td><td>SCR-05</td><td>FR-SEARCH-01</td><td>Arabic search &lt; 1.5s</td><td>Results within 1.5 seconds</td><td><span class="uat-checkbox"></span></td></tr>
        <tr><td><strong>UAT-05</strong></td><td>All</td><td>WCAG 2.1</td><td>Screen reader traversal</td><td>All elements announced correctly</td><td><span class="uat-checkbox"></span></td></tr>
        <!-- Add all UAT cases -->
      </tbody>
    </table>
  </div>

  <!-- ─── 15. SIGN-OFF ─── -->
  <div id="signoff" class="frd-section">
    <div class="frd-section-label">Section 15</div>
    <h2 class="frd-section-title">Sign-off</h2>
    <p class="frd-body">By signing below, each stakeholder confirms they have reviewed this FRD and approve it for development.</p>
    <table class="signoff-table">
      <thead><tr><th>Name</th><th>Role</th><th>Signature</th><th>Date</th><th>Status</th></tr></thead>
      <tbody>
        <tr><td>[Name]</td><td>Product Owner</td><td></td><td></td><td><span class="frd-status status-draft">Pending</span></td></tr>
        <tr><td>[Name]</td><td>UX Lead</td><td></td><td></td><td><span class="frd-status status-draft">Pending</span></td></tr>
        <tr><td>[Name]</td><td>Tech Lead</td><td></td><td></td><td><span class="frd-status status-draft">Pending</span></td></tr>
        <tr><td>[Name]</td><td>QA Lead</td><td></td><td></td><td><span class="frd-status status-draft">Pending</span></td></tr>
      </tbody>
    </table>
  </div>

  <!-- Nav back -->
  <div style="margin-top:var(--space-20); text-align:center; border-top:1px solid var(--color-border); padding-top:var(--space-8);">
    <a href="index.html" style="color:var(--color-primary); font-weight:600; text-decoration:none;">← Back to Project Hub</a>
  </div>

</div>
</div>

<!-- Arabic version -->
<div id="content-ar" class="lang-block" style="display:none;" dir="rtl">
  <div class="frd-wrapper">
    <!-- [Exact same structure — all content fully translated to natural Arabic] -->
    <!-- Section labels, table headers, error messages, and requirement text all in Arabic -->
    <!-- Arabic error messages are already defined in Section 10 above — use them here -->
  </div>
</div>

<script>
function setLang(lang, btn) {
  document.querySelectorAll('.lang-block').forEach(el => el.style.display = 'none');
  document.getElementById('content-' + lang).style.display = 'block';
  document.querySelectorAll('.lang-btn').forEach(b => b.classList.remove('active'));
  btn.classList.add('active');
}
</script>
</body>
</html>
```

---

## Quality Checklist Before Delivering

Run through before handing off:

```
□ index.html opens and all 5 links work
□ All 6 files render correctly in a browser
□ No placeholder text anywhere — no [brackets] in final output
□ No Lorem ipsum
□ All CSS tokens defined and used consistently (no hardcoded hex values)
□ Google Fonts loading from CDN
□ Timeline has real durations — not [placeholder]
□ Color swatches show real hex values (background color applied)
□ Typography specimen shows actual font rendering
□ Grid diagram shows correct column count (4 mobile / 12 desktop)
□ Spacing bars have accurate widths matching their px values
□ Persona feels human and specific (named, quoted, grounded in research)
□ Empathy map has real quotes and observations from research
□ Affinity map clusters named after real themes from research
□ Journey map shows real emotional arc (not all positive)
□ HMW statements connect clearly to research findings
□ Site map reflects the actual app structure designed
□ User flow covers the actual primary task (not a trivial example)
□ Wireframe sketches match the actual designed screens
□ Color palette swatches: 50→950 all filled with correct hex values
□ Problem/Solution boxes are specific and paired (each problem has a matching solution)
□ Statistics summary bar shows real numbers (interviews, survey replies, competitors, screens)
□ Timeline: Gantt bars span the correct weeks — no placeholder weeks
□ Survey donut charts: conic-gradient % matches actual data (values sum to 100%)
□ Quote cards contain real verbatim quotes — not made-up placeholder text
□ Interview questions are organized by Research Objective (3 objectives minimum)
□ Competitor feature matrix: ✓/✗/◑ values are accurate to actual competitor products
□ Persona has 4 columns: Goals, Motivators, Frustrations, Behaviors
□ Personality sliders reflect actual research findings (not arbitrary positions)
□ Favorite brands are plausible for the persona's profile and region
□ Feature list traces back to specific HMW statements
□ Feature priorities (Must/Should/Could) are justified by research
□ Crazy 8's shows 8 distinct ideas — not variations of the same idea
□ Before/After shows the same task/screen — fair comparison
□ Component library embeds real working HTML components (not placeholders)
□ Competitor table: real competitor names, real ratings, real weaknesses
□ Screen thumbnails link or match the actual final screens
□ Lessons Learned are honest and specific — not generic design wisdom
□ Arabic version is complete, natural, and RTL layout is correct
□ Language switcher works in both directions
□ All files link back to index.html
□ screens.html prototype navigation works (all screens reachable by clicking)
□ prefers-reduced-motion CSS rule is included
```

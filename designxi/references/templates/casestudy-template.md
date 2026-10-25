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


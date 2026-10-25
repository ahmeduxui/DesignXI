# Design Handoff Guide — DesignXI

## Why Design Handoff Matters

A beautiful design that can't be implemented correctly is a failed design. The handoff is the bridge between design intent and engineering execution. In DesignXI, the deliverables ARE the code — HTML/CSS files that represent the complete product design. A great handoff means:

- **Developers implement without questions** — every spec is clear, every state is defined
- **Consistency across the product** — design tokens ensure colors, spacing, and typography scale consistently
- **Edge cases are handled** — you've designed for empty states, errors, loading, and content edge cases
- **Accessibility is built in** — focus states, aria labels, and keyboard interaction are documented
- **Responsive behavior is intentional** — what changes at each breakpoint is explicit, not assumed

Without a handoff, developers guess. With a great handoff, developers build with confidence.

---

## What Makes a Good Handoff

### 1. Design Tokens (Not Raw Values)

Every color, spacing, type size, shadow, and radius is a **token** — a named CSS custom property that can be reused across the entire design.

**Why tokens matter:**
- Change a color in one place, update everywhere
- Developers can't accidentally use `#5f5f5f` when `--color-text-secondary` is the token
- Easy to implement themes, dark mode, high-contrast mode

**Token types:**
- Colors (text, backgrounds, borders, states)
- Typography (size, weight, line-height)
- Spacing (margins, padding — use a scale like 4px, 8px, 12px, 16px, 24px, 32px)
- Border radius (corners — subtle, rounded, full)
- Shadows (elevation levels)
- Animation (durations, easing functions)

### 2. State Documentation

Design every interactive state, not just the happy path:
- **Default** — what users see normally
- **Hover** — on desktop, when cursor is over element
- **Active/Pressed** — during click or while active tab
- **Focus** — keyboard navigation outline
- **Disabled** — when action isn't available
- **Loading** — async operation in progress
- **Error** — something went wrong
- **Empty** — no data to display
- **Success** — operation completed

Include transitions: which states animate? What's the duration? What easing?

### 3. Responsive Behavior

Explicitly document what changes at each breakpoint:
- Grid columns and margins
- Font sizes (do they scale?)
- Element visibility (hidden on mobile?)
- Layout changes (stacked vs side-by-side)
- Touch target sizes (48px minimum on mobile)

### 4. Interaction Specifications

Every animation, transition, and interactive behavior documented:
- What triggers it (tap, hover, scroll, load)
- Animation duration and easing
- What state it starts from and ends at
- Any intermediate steps
- What happens during and after the animation

### 5. Content Rules

Real data breaks designs. Define limits upfront:
- Character limits for headlines, labels, descriptions
- Line limits (1 line, 2 lines, 3 lines max)
- Overflow behavior (truncate, wrap, resize)
- How long text is handled (abbreviate, break word, ellipsis)

### 6. Edge Cases

If it can happen, you've designed for it:
- Long text (labels that are longer than expected)
- Empty data (no search results, no list items)
- Error states (network error, validation error, permission error)
- Loading states (skeleton screen, spinner, placeholder)
- Disabled states (why is this disabled? Is it grayed out? Hidden?)

### 7. Accessibility Notes

Build inclusion from the start:
- **Aria labels** — icon buttons need labels (aria-label="Settings")
- **Focus order** — tab through the screen — is the order logical?
- **Focus visible** — can you see where keyboard focus is? (outline, background change)
- **Color contrast** — does text meet WCAG AA (4.5:1 for normal text)?
- **Touch targets** — are buttons at least 48px × 48px on mobile?
- **Screen reader behavior** — what announces? What's silent? What's skipped?

---

## The DesignXI Handoff Package

Since DesignXI deliverables are HTML files, the handoff includes:

### `tokens.css`
The complete design system as CSS custom properties. Every color, size, shadow, and duration is defined here. This is the single source of truth for the entire design.

```css
/* Example tokens.css structure */
:root {
  /* Colors */
  --color-primary-50: #f0f4ff;
  --color-primary-500: #4f46e5;
  --color-primary-600: #4338ca;
  --color-primary-700: #3730a3;

  --color-text-primary: #111827;
  --color-text-secondary: #6b7280;
  --color-bg-page: #f9fafb;

  /* Spacing */
  --spacing-xs: 4px;
  --spacing-sm: 8px;
  --spacing-md: 16px;
  --spacing-lg: 24px;
  --spacing-xl: 32px;

  /* Typography */
  --font-size-sm: 14px;
  --font-size-base: 16px;
  --font-size-lg: 18px;
  --font-weight-regular: 400;
  --font-weight-semibold: 600;
  --font-weight-bold: 700;
  --line-height-tight: 1.2;
  --line-height-normal: 1.5;

  /* Animation */
  --duration-fast: 150ms;
  --duration-base: 250ms;
  --easing-ease-out: cubic-bezier(0.4, 0, 0.2, 1);
}
```

### `screens.html`
All screens with interactive states. Developers open this in a browser and interact with every component to see what each state looks like. No screenshots—interactive HTML.

### `handoff.html` (NEW)
The handoff document itself — a developer-facing guide that explains the design system, component specs, interaction specs, responsive behavior, content rules, and edge cases. Developers open this alongside `screens.html` to understand the "why" and "how."

### `casestudy.html`
Design rationale. Why certain decisions were made, user research insights, design evolution. Context that helps developers understand the strategic intent.

---

## `handoff.html` — Handoff Document Template

This is the document developers read to implement the design correctly.

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Design Handoff — [Project Name]</title>
  <link rel="stylesheet" href="tokens.css">
  <style>
    * { margin: 0; padding: 0; box-sizing: border-box; }
    body {
      font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
      font-size: var(--font-size-base);
      line-height: var(--line-height-normal);
      color: var(--color-text-primary);
      background: var(--color-bg-page);
      padding: var(--spacing-xl);
    }

    .container { max-width: 1200px; margin: 0 auto; }

    h1 {
      font-size: 32px;
      font-weight: 700;
      margin-bottom: var(--spacing-lg);
      border-bottom: 3px solid var(--color-primary-500);
      padding-bottom: var(--spacing-md);
    }

    h2 {
      font-size: 24px;
      font-weight: 600;
      margin-top: var(--spacing-xl);
      margin-bottom: var(--spacing-md);
      color: var(--color-primary-600);
    }

    h3 {
      font-size: 18px;
      font-weight: 600;
      margin-top: var(--spacing-lg);
      margin-bottom: var(--spacing-sm);
    }

    section {
      margin-bottom: var(--spacing-xl);
      background: white;
      padding: var(--spacing-lg);
      border-radius: 8px;
      border: 1px solid #e5e7eb;
    }

    table {
      width: 100%;
      border-collapse: collapse;
      margin-top: var(--spacing-md);
    }

    th, td {
      padding: var(--spacing-md);
      text-align: left;
      border-bottom: 1px solid #e5e7eb;
    }

    th {
      background: #f3f4f6;
      font-weight: 600;
      font-size: 14px;
    }

    tr:last-child td { border-bottom: none; }

    .token-swatch {
      display: inline-block;
      width: 24px;
      height: 24px;
      border-radius: 4px;
      border: 1px solid #d1d5db;
      vertical-align: middle;
      margin-right: var(--spacing-sm);
    }

    .component-spec {
      background: #fafbfc;
      padding: var(--spacing-lg);
      border-left: 4px solid var(--color-primary-500);
      margin-bottom: var(--spacing-lg);
    }

    .spec-row {
      display: grid;
      grid-template-columns: 200px 1fr;
      gap: var(--spacing-lg);
      margin-bottom: var(--spacing-md);
    }

    .spec-label {
      font-weight: 600;
      color: var(--color-text-secondary);
    }

    .code {
      background: #1f2937;
      color: #f3f4f6;
      padding: var(--spacing-md);
      border-radius: 6px;
      font-family: 'Monaco', 'Courier New', monospace;
      font-size: 13px;
      overflow-x: auto;
      margin: var(--spacing-md) 0;
    }

    .interaction-flow {
      border-left: 3px solid var(--color-primary-500);
      padding-left: var(--spacing-lg);
      margin: var(--spacing-lg) 0;
    }

    .flow-step {
      margin-bottom: var(--spacing-lg);
      padding-bottom: var(--spacing-lg);
      border-bottom: 1px solid #e5e7eb;
    }

    .flow-step:last-child {
      border-bottom: none;
      margin-bottom: 0;
      padding-bottom: 0;
    }

    .step-time {
      font-weight: 600;
      color: var(--color-primary-600);
      font-size: 13px;
    }

    .checklist {
      list-style: none;
      padding-left: 0;
    }

    .checklist li {
      padding-left: 32px;
      position: relative;
      margin-bottom: var(--spacing-sm);
    }

    .checklist li:before {
      content: "✓";
      position: absolute;
      left: 0;
      font-weight: bold;
      color: #10b981;
    }

    .accessibility-badge {
      display: inline-block;
      background: #dbeafe;
      color: #0c4a6e;
      padding: 4px 8px;
      border-radius: 4px;
      font-size: 12px;
      font-weight: 600;
      margin-right: var(--spacing-sm);
    }

    .warning {
      background: #fef3c7;
      border-left: 4px solid #f59e0b;
      padding: var(--spacing-md);
      margin: var(--spacing-lg) 0;
      border-radius: 4px;
    }
  </style>
</head>
<body>
  <div class="container">

    <!-- HEADER -->
    <h1>Design Handoff — [Project Name]</h1>
    <p style="margin-bottom: var(--spacing-lg); color: var(--color-text-secondary);">
      Version 1.0 | Updated March 2026 | Open <code>screens.html</code> alongside this document
    </p>

    <!-- DESIGN SYSTEM SUMMARY -->
    <section>
      <h2>Design System Summary</h2>
      <p style="margin-bottom: var(--spacing-lg); color: var(--color-text-secondary);">
        All colors, spacing, typography, and animation are defined as CSS custom properties in <code>tokens.css</code>.
        Never hardcode hex values — always use tokens.
      </p>

      <h3>Color Tokens</h3>
      <table>
        <thead>
          <tr>
            <th>Token Name</th>
            <th>Value</th>
            <th>Usage</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>
              <span class="token-swatch" style="background: #4f46e5;"></span>
              <code>--color-primary-500</code>
            </td>
            <td>#4F46E5</td>
            <td>Primary CTAs, links, active navigation items, focus states</td>
          </tr>
          <tr>
            <td>
              <span class="token-swatch" style="background: #4338ca;"></span>
              <code>--color-primary-600</code>
            </td>
            <td>#4338CA</td>
            <td>Button hover, link hover, darker interactive states</td>
          </tr>
          <tr>
            <td>
              <span class="token-swatch" style="background: #111827;"></span>
              <code>--color-text-primary</code>
            </td>
            <td>#111827</td>
            <td>All body text, headings, primary labels</td>
          </tr>
          <tr>
            <td>
              <span class="token-swatch" style="background: #6b7280;"></span>
              <code>--color-text-secondary</code>
            </td>
            <td>#6B7280</td>
            <td>Helper text, descriptions, disabled labels</td>
          </tr>
          <tr>
            <td>
              <span class="token-swatch" style="background: #f9fafb;"></span>
              <code>--color-bg-page</code>
            </td>
            <td>#F9FAFB</td>
            <td>Page background</td>
          </tr>
          <tr>
            <td>
              <span class="token-swatch" style="background: #ffffff; border: 1px solid #d1d5db;"></span>
              <code>--color-bg-surface</code>
            </td>
            <td>#FFFFFF</td>
            <td>Cards, modals, overlays, elevated surfaces</td>
          </tr>
          <tr>
            <td>
              <span class="token-swatch" style="background: #ef4444;"></span>
              <code>--color-error</code>
            </td>
            <td>#EF4444</td>
            <td>Error messages, destructive actions, validation errors</td>
          </tr>
          <tr>
            <td>
              <span class="token-swatch" style="background: #10b981;"></span>
              <code>--color-success</code>
            </td>
            <td>#10B981</td>
            <td>Success messages, confirmation states, positive feedback</td>
          </tr>
        </tbody>
      </table>

      <h3>Typography Scale</h3>
      <table>
        <thead>
          <tr>
            <th>Token Name</th>
            <th>Size</th>
            <th>Weight</th>
            <th>Line Height</th>
            <th>Usage</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><code>--type-h1</code></td>
            <td>32px</td>
            <td>700</td>
            <td>1.2</td>
            <td>Page titles</td>
          </tr>
          <tr>
            <td><code>--type-h2</code></td>
            <td>24px</td>
            <td>600</td>
            <td>1.3</td>
            <td>Section headings</td>
          </tr>
          <tr>
            <td><code>--type-h3</code></td>
            <td>18px</td>
            <td>600</td>
            <td>1.4</td>
            <td>Subsection headings, card titles</td>
          </tr>
          <tr>
            <td><code>--type-body-lg</code></td>
            <td>18px</td>
            <td>400</td>
            <td>1.5</td>
            <td>Large body text, CTAs</td>
          </tr>
          <tr>
            <td><code>--type-body</code></td>
            <td>16px</td>
            <td>400</td>
            <td>1.5</td>
            <td>Default body text, form labels</td>
          </tr>
          <tr>
            <td><code>--type-body-sm</code></td>
            <td>14px</td>
            <td>400</td>
            <td>1.5</td>
            <td>Helper text, descriptions, captions</td>
          </tr>
          <tr>
            <td><code>--type-caption</code></td>
            <td>12px</td>
            <td>500</td>
            <td>1.4</td>
            <td>Small labels, timestamps, badges</td>
          </tr>
        </tbody>
      </table>

      <h3>Spacing Scale</h3>
      <table>
        <thead>
          <tr>
            <th>Token Name</th>
            <th>Value</th>
            <th>Typical Usage</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><code>--spacing-xs</code></td>
            <td>4px</td>
            <td>Small gaps, icon margins</td>
          </tr>
          <tr>
            <td><code>--spacing-sm</code></td>
            <td>8px</td>
            <td>Tight spacing, component internals</td>
          </tr>
          <tr>
            <td><code>--spacing-md</code></td>
            <td>16px</td>
            <td>Standard padding, section margins</td>
          </tr>
          <tr>
            <td><code>--spacing-lg</code></td>
            <td>24px</td>
            <td>Major spacing, component separation</td>
          </tr>
          <tr>
            <td><code>--spacing-xl</code></td>
            <td>32px</td>
            <td>Large gaps, page padding</td>
          </tr>
          <tr>
            <td><code>--spacing-2xl</code></td>
            <td>48px</td>
            <td>Major section spacing</td>
          </tr>
        </tbody>
      </table>

      <h3>Border Radius Scale</h3>
      <table>
        <thead>
          <tr>
            <th>Token Name</th>
            <th>Value</th>
            <th>Component Examples</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><code>--radius-sm</code></td>
            <td>4px</td>
            <td>Inputs, small buttons, badges</td>
          </tr>
          <tr>
            <td><code>--radius-md</code></td>
            <td>8px</td>
            <td>Standard buttons, cards, modals</td>
          </tr>
          <tr>
            <td><code>--radius-lg</code></td>
            <td>12px</td>
            <td>Large components, hero sections</td>
          </tr>
          <tr>
            <td><code>--radius-full</code></td>
            <td>9999px</td>
            <td>Circular buttons, pills, avatars</td>
          </tr>
        </tbody>
      </table>

      <h3>Shadow Levels (Elevation)</h3>
      <table>
        <thead>
          <tr>
            <th>Token Name</th>
            <th>CSS Value</th>
            <th>Usage</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><code>--shadow-sm</code></td>
            <td>0 1px 2px rgba(0, 0, 0, 0.05)</td>
            <td>Subtle elevation, interactive hints</td>
          </tr>
          <tr>
            <td><code>--shadow-md</code></td>
            <td>0 4px 6px rgba(0, 0, 0, 0.1)</td>
            <td>Standard cards, hover states</td>
          </tr>
          <tr>
            <td><code>--shadow-lg</code></td>
            <td>0 10px 15px rgba(0, 0, 0, 0.1)</td>
            <td>Modals, popovers, dropdowns</td>
          </tr>
        </tbody>
      </table>

      <h3>Animation Tokens</h3>
      <table>
        <thead>
          <tr>
            <th>Token Name</th>
            <th>Value</th>
            <th>Usage</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><code>--duration-fast</code></td>
            <td>150ms</td>
            <td>Hover states, micro-interactions</td>
          </tr>
          <tr>
            <td><code>--duration-base</code></td>
            <td>250ms</td>
            <td>Standard transitions, state changes</td>
          </tr>
          <tr>
            <td><code>--duration-slow</code></td>
            <td>350ms</td>
            <td>Major view changes, page transitions</td>
          </tr>
          <tr>
            <td><code>--easing-ease-out</code></td>
            <td>cubic-bezier(0.4, 0, 0.2, 1)</td>
            <td>Elements entering, fading in</td>
          </tr>
          <tr>
            <td><code>--easing-ease-in</code></td>
            <td>cubic-bezier(0.4, 0, 1, 1)</td>
            <td>Elements leaving, fading out</td>
          </tr>
        </tbody>
      </table>
    </section>

    <!-- COMPONENT SPECIFICATIONS -->
    <section>
      <h2>Component Specifications</h2>
      <p style="margin-bottom: var(--spacing-lg); color: var(--color-text-secondary);">
        Every interactive component has been designed in all required states.
        See <code>screens.html</code> to view each state visually.
      </p>

      <!-- PRIMARY BUTTON EXAMPLE -->
      <div class="component-spec">
        <h3>Primary Button</h3>

        <div class="spec-row">
          <div class="spec-label">Dimensions</div>
          <div>
            Height: 48px | Padding: 12px 24px | Border radius: 8px | Min width: 120px
          </div>
        </div>

        <div class="spec-row">
          <div class="spec-label">Typography</div>
          <div>
            Font: Inter SemiBold 600 | Size: 16px | Line height: 24px (1.5) | Letter spacing: 0
          </div>
        </div>

        <div class="spec-row">
          <div class="spec-label">States</div>
          <div>
            <div style="margin-bottom: var(--spacing-sm);">
              <strong style="color: var(--color-text-primary);">Default:</strong>
              Background: var(--color-primary-500) | Text: white | Cursor: pointer
            </div>
            <div style="margin-bottom: var(--spacing-sm);">
              <strong style="color: var(--color-text-primary);">Hover:</strong>
              Background: var(--color-primary-600) | Transition: 150ms ease-out
            </div>
            <div style="margin-bottom: var(--spacing-sm);">
              <strong style="color: var(--color-text-primary);">Active:</strong>
              Background: var(--color-primary-700) | Transform: scale(0.98) | Transition: 100ms ease-out
            </div>
            <div style="margin-bottom: var(--spacing-sm);">
              <strong style="color: var(--color-text-primary);">Focus (Keyboard):</strong>
              Outline: 3px solid var(--color-primary-300) | Outline offset: 3px
            </div>
            <div style="margin-bottom: var(--spacing-sm);">
              <strong style="color: var(--color-text-primary);">Disabled:</strong>
              Background: #d1d5db | Text: #9ca3af | Cursor: not-allowed | Opacity: 0.6
            </div>
            <div>
              <strong style="color: var(--color-text-primary);">Loading:</strong>
              Background: var(--color-primary-500) | Label hides | Spinner appears (white, 20px, centered)
            </div>
          </div>
        </div>

        <div class="spec-row">
          <div class="spec-label">Accessibility</div>
          <div>
            <div>
              <span class="accessibility-badge">WCAG AA</span>
              <span class="accessibility-badge">Keyboard</span>
            </div>
            <div style="margin-top: var(--spacing-sm);">
              Focus visible: Yes (3px outline) | Keyboard activation: Enter / Space |
              aria-disabled: "true" when disabled | Touch target: 48×48px minimum
            </div>
          </div>
        </div>

        <div class="spec-row">
          <div class="spec-label">Content Rules</div>
          <div>
            Label: 1–3 words, action verb first ("Save Settings", "Get Started") |
            Max width: flexible (fills 100% of container or explicit width) |
            Never truncate — if text is too long, widen button or use icon only
          </div>
        </div>

        <div class="spec-row">
          <div class="spec-label">Example Code</div>
          <div class="code">
&lt;button class="btn-primary"&gt;Save Settings&lt;/button&gt;

.btn-primary {
  background-color: var(--color-primary-500);
  color: white;
  padding: var(--spacing-sm) var(--spacing-md);
  height: 48px;
  border-radius: var(--radius-md);
  border: none;
  font-size: var(--font-size-base);
  font-weight: var(--font-weight-semibold);
  cursor: pointer;
  transition: background-color var(--duration-fast) var(--easing-ease-out);
  min-width: 120px;
}

.btn-primary:hover {
  background-color: var(--color-primary-600);
}

.btn-primary:active {
  background-color: var(--color-primary-700);
  transform: scale(0.98);
}

.btn-primary:focus-visible {
  outline: 3px solid var(--color-primary-300);
  outline-offset: 3px;
}

.btn-primary:disabled {
  background-color: #d1d5db;
  color: #9ca3af;
  cursor: not-allowed;
  opacity: 0.6;
}
          </div>
        </div>
      </div>

      <!-- SECONDARY BUTTON EXAMPLE -->
      <div class="component-spec">
        <h3>Secondary Button (Outline)</h3>

        <div class="spec-row">
          <div class="spec-label">Dimensions</div>
          <div>
            Height: 48px | Padding: 12px 24px | Border: 2px solid var(--color-primary-500) | Border radius: 8px
          </div>
        </div>

        <div class="spec-row">
          <div class="spec-label">States</div>
          <div>
            <div style="margin-bottom: var(--spacing-sm);">
              <strong style="color: var(--color-text-primary);">Default:</strong>
              Background: transparent | Border: 2px solid var(--color-primary-500) | Text: var(--color-primary-500)
            </div>
            <div style="margin-bottom: var(--spacing-sm);">
              <strong style="color: var(--color-text-primary);">Hover:</strong>
              Background: var(--color-primary-50) | Border: 2px solid var(--color-primary-600)
            </div>
            <div>
              <strong style="color: var(--color-text-primary);">Active:</strong>
              Background: var(--color-primary-100) | Border: 2px solid var(--color-primary-700)
            </div>
          </div>
        </div>
      </div>

      <!-- TEXT INPUT EXAMPLE -->
      <div class="component-spec">
        <h3>Text Input</h3>

        <div class="spec-row">
          <div class="spec-label">Dimensions</div>
          <div>
            Height: 48px | Padding: 12px 16px | Border radius: 6px | Border: 1px solid #d1d5db
          </div>
        </div>

        <div class="spec-row">
          <div class="spec-label">Typography</div>
          <div>
            Font: Inter 400 | Size: 16px | Line height: 1.5
          </div>
        </div>

        <div class="spec-row">
          <div class="spec-label">States</div>
          <div>
            <div style="margin-bottom: var(--spacing-sm);">
              <strong style="color: var(--color-text-primary);">Default:</strong>
              Border: 1px solid #d1d5db | Background: white | Placeholder text: var(--color-text-secondary)
            </div>
            <div style="margin-bottom: var(--spacing-sm);">
              <strong style="color: var(--color-text-primary);">Focus:</strong>
              Border: 2px solid var(--color-primary-500) | Outline: none | Box shadow: 0 0 0 4px rgba(79, 70, 229, 0.1)
            </div>
            <div style="margin-bottom: var(--spacing-sm);">
              <strong style="color: var(--color-text-primary);">Error:</strong>
              Border: 2px solid var(--color-error) | Error message appears below input, font-size: 12px, color: var(--color-error)
            </div>
            <div>
              <strong style="color: var(--color-text-primary);">Disabled:</strong>
              Background: #f3f4f6 | Border: 1px solid #e5e7eb | Text: var(--color-text-secondary) | Cursor: not-allowed
            </div>
          </div>
        </div>

        <div class="spec-row">
          <div class="spec-label">Content Rules</div>
          <div>
            Placeholder text should be a hint, not a label (label should be separate &lt;label&gt; element) |
            Character limit: show counter if &gt; 100 chars |
            Error message appears inline below the input
          </div>
        </div>
      </div>

    </section>

    <!-- SCREEN INVENTORY -->
    <section>
      <h2>Screen Inventory</h2>
      <p style="margin-bottom: var(--spacing-lg); color: var(--color-text-secondary);">
        All screens are interactive in <code>screens.html</code>. This table shows the structure and connections.
      </p>

      <table>
        <thead>
          <tr>
            <th>Screen Name</th>
            <th>Route/Path</th>
            <th>Description</th>
            <th>Key Components</th>
            <th>Next Screens</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Onboarding — Welcome</strong></td>
            <td>/onboarding</td>
            <td>First screen users see. Hero text, single CTA.</td>
            <td>H1, Body text, Primary Button</td>
            <td>Onboarding — Create Account</td>
          </tr>
          <tr>
            <td><strong>Onboarding — Create Account</strong></td>
            <td>/onboarding/signup</td>
            <td>Email, password, sign up button. Shows validation errors inline.</td>
            <td>Text Input, Primary Button, Form validation</td>
            <td>Onboarding — Verify Email OR Dashboard</td>
          </tr>
          <tr>
            <td><strong>Dashboard</strong></td>
            <td>/dashboard</td>
            <td>Main app view. Shows user's projects, pending tasks.</td>
            <td>Navigation, Card grid, Empty state OR populated list</td>
            <td>Project detail, Settings, etc.</td>
          </tr>
          <tr>
            <td><strong>Dashboard — Empty State</strong></td>
            <td>/dashboard (no projects)</td>
            <td>When user has no projects yet. Encouragement + CTA.</td>
            <td>Illustration, H2, Body text, Primary Button</td>
            <td>Create Project modal</td>
          </tr>
        </tbody>
      </table>
    </section>

    <!-- INTERACTION SPECIFICATIONS -->
    <section>
      <h2>Interaction Specifications</h2>
      <p style="margin-bottom: var(--spacing-lg); color: var(--color-text-secondary);">
        Every animation, transition, and interactive behavior is documented here with timing and easing.
      </p>

      <!-- FORM SUBMISSION FLOW -->
      <h3>Form Submission Flow</h3>
      <div class="interaction-flow">
        <div class="flow-step">
          <div class="step-time">Trigger: 0ms</div>
          <div>User taps "Submit" button on form</div>
        </div>

        <div class="flow-step">
          <div class="step-time">Step 1: 0ms</div>
          <strong>Button enters loading state:</strong>
          <ul style="margin-left: var(--spacing-lg); margin-top: var(--spacing-sm);">
            <li>Button disabled (prevent double submit)</li>
            <li>Label text hides (opacity: 0)</li>
            <li>Spinner appears (white, 20px, centered) — no transition, immediate</li>
          </ul>
        </div>

        <div class="flow-step">
          <div class="step-time">Step 2a: On Success</div>
          <strong>Success path (assume 1-2 second network latency):</strong>
          <ul style="margin-left: var(--spacing-lg); margin-top: var(--spacing-sm);">
            <li>Button state returns to default (300ms fade)</li>
            <li>Toast notification slides down from top: "Your profile was saved." (success green) — 150ms ease-out</li>
            <li>Toast stays visible for 3000ms, then auto-dismisses (fade out 200ms)</li>
            <li>Page redirects to /dashboard after 500ms (fade transition, 250ms ease-out)</li>
          </ul>
        </div>

        <div class="flow-step">
          <div class="step-time">Step 2b: On Error</div>
          <strong>Error path:</strong>
          <ul style="margin-left: var(--spacing-lg); margin-top: var(--spacing-sm);">
            <li>Button state returns to default (300ms fade)</li>
            <li>Inline error message appears below form (red text, 14px) — fade in 200ms</li>
            <li>Error message text: "Couldn't save. Check your connection and try again."</li>
            <li>User can edit form and resubmit</li>
            <li>Error message dismissed when user starts editing a field (fade out 150ms)</li>
          </ul>
        </div>
      </div>

      <!-- PAGE TRANSITION -->
      <h3>Page Transition (Navigation)</h3>
      <div class="interaction-flow">
        <div class="flow-step">
          <div class="step-time">Trigger: 0ms</div>
          <div>User taps navigation link or back button</div>
        </div>

        <div class="flow-step">
          <div class="step-time">Step 1: 0ms</div>
          <strong>Current page fades out:</strong>
          <ul style="margin-left: var(--spacing-lg); margin-top: var(--spacing-sm);">
            <li>Opacity: 1 → 0 over 200ms (easing: ease-in)</li>
            <li>Transform: translateY(0) → translateY(-20px) over 200ms</li>
          </ul>
        </div>

        <div class="flow-step">
          <div class="step-time">Step 2: 200ms</div>
          <strong>Page swap happens (DOM change, no animation)</strong>
        </div>

        <div class="flow-step">
          <div class="step-time">Step 3: 200ms</div>
          <strong>New page fades in:</strong>
          <ul style="margin-left: var(--spacing-lg); margin-top: var(--spacing-sm);">
            <li>Opacity: 0 → 1 over 250ms (easing: ease-out)</li>
            <li>Transform: translateY(20px) → translateY(0) over 250ms</li>
          </ul>
        </div>
      </div>

      <!-- TOOLTIP HOVER -->
      <h3>Tooltip on Icon Hover</h3>
      <div class="interaction-flow">
        <div class="flow-step">
          <div class="step-time">Trigger: 0ms</div>
          <div>User hovers mouse over icon (desktop) or long-presses (mobile)</div>
        </div>

        <div class="flow-step">
          <div class="step-time">Step 1: 0ms</div>
          <strong>Icon background highlight:</strong>
          <ul style="margin-left: var(--spacing-lg); margin-top: var(--spacing-sm);">
            <li>Background: transparent → rgba(0, 0, 0, 0.05) over 150ms</li>
          </ul>
        </div>

        <div class="flow-step">
          <div class="step-time">Step 2: 400ms</div>
          <strong>Tooltip appears (delayed to prevent flashing):</strong>
          <ul style="margin-left: var(--spacing-lg); margin-top: var(--spacing-sm);">
            <li>Tooltip positioned 8px above icon (auto-positioned if too close to edge)</li>
            <li>Opacity: 0 → 1 over 150ms (ease-out)</li>
            <li>Transform: scale(0.95) → scale(1) over 150ms</li>
            <li>Background: #1f2937, text: white, padding: 8px 12px, border-radius: 4px</li>
          </ul>
        </div>

        <div class="flow-step">
          <div class="step-time">On mouse leave or blur:</div>
          <strong>Tooltip disappears:</strong>
          <ul style="margin-left: var(--spacing-lg); margin-top: var(--spacing-sm);">
            <li>Opacity: 1 → 0 over 150ms (ease-in)</li>
            <li>Tooltip removed from DOM after fade completes</li>
          </ul>
        </div>
      </div>

    </section>

    <!-- RESPONSIVE BREAKPOINTS -->
    <section>
      <h2>Responsive Breakpoints</h2>
      <p style="margin-bottom: var(--spacing-lg); color: var(--color-text-secondary);">
        The design is optimized for three breakpoints. Behavior between breakpoints is left to developer discretion
        but should feel natural and progressively enhance.
      </p>

      <table>
        <thead>
          <tr>
            <th>Breakpoint</th>
            <th>Screen Width</th>
            <th>Grid Columns</th>
            <th>Margins</th>
            <th>Gutter</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Mobile</strong></td>
            <td>375px – 767px</td>
            <td>4 columns</td>
            <td>16px</td>
            <td>12px</td>
          </tr>
          <tr>
            <td><strong>Tablet</strong></td>
            <td>768px – 1279px</td>
            <td>8 columns</td>
            <td>24px</td>
            <td>16px</td>
          </tr>
          <tr>
            <td><strong>Desktop</strong></td>
            <td>1280px+</td>
            <td>12 columns</td>
            <td>80px</td>
            <td>24px</td>
          </tr>
        </tbody>
      </table>

      <h3>Mobile → Tablet (375px → 768px)</h3>
      <div style="background: #fafbfc; padding: var(--spacing-lg); border-radius: 6px; margin-top: var(--spacing-lg);">
        <table>
          <thead>
            <tr>
              <th>Element</th>
              <th>Mobile</th>
              <th>Tablet</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>Navigation</strong></td>
              <td>Bottom tab bar (fixed)</td>
              <td>Sidebar (collapsed toggle available)</td>
            </tr>
            <tr>
              <td><strong>Card layout</strong></td>
              <td>Single column (1 card/row)</td>
              <td>2-column grid</td>
            </tr>
            <tr>
              <td><strong>H1 font size</strong></td>
              <td>28px</td>
              <td>32px</td>
            </tr>
            <tr>
              <td><strong>H2 font size</strong></td>
              <td>20px</td>
              <td>24px</td>
            </tr>
            <tr>
              <td><strong>Page padding</strong></td>
              <td>16px</td>
              <td>24px</td>
            </tr>
          </tbody>
        </table>
      </div>

      <h3>Tablet → Desktop (768px → 1280px)</h3>
      <div style="background: #fafbfc; padding: var(--spacing-lg); border-radius: 6px; margin-top: var(--spacing-lg);">
        <table>
          <thead>
            <tr>
              <th>Element</th>
              <th>Tablet</th>
              <th>Desktop</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>Card layout</strong></td>
              <td>2-column grid</td>
              <td>3-column grid</td>
            </tr>
            <tr>
              <td><strong>Sidebar</strong></td>
              <td>Collapsible (default collapsed)</td>
              <td>Always visible (240px width)</td>
            </tr>
            <tr>
              <td><strong>Max content width</strong></td>
              <td>100% of viewport</td>
              <td>1120px (centered)</td>
            </tr>
            <tr>
              <td><strong>Page padding</strong></td>
              <td>24px</td>
              <td>80px</td>
            </tr>
          </tbody>
        </table>
      </div>

      <div class="warning" style="margin-top: var(--spacing-lg);">
        <strong>Mobile-first development:</strong> Start with mobile layout, then use <code>@media (min-width:)</code>
        to add tablet and desktop styles. This ensures better performance and mobile experience.
      </div>
    </section>

    <!-- CONTENT RULES -->
    <section>
      <h2>Content Rules</h2>
      <p style="margin-bottom: var(--spacing-lg); color: var(--color-text-secondary);">
        Real content breaks designs. These rules prevent overflow, truncation issues, and maintain readability.
      </p>

      <table>
        <thead>
          <tr>
            <th>Element</th>
            <th>Max Characters</th>
            <th>Max Lines</th>
            <th>Overflow Behavior</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Page title (H1)</strong></td>
            <td>60</td>
            <td>2 lines</td>
            <td>Wraps naturally; line break at word boundary</td>
          </tr>
          <tr>
            <td><strong>Section title (H2)</strong></td>
            <td>50</td>
            <td>2 lines</td>
            <td>Wraps naturally; never truncate</td>
          </tr>
          <tr>
            <td><strong>Card title</strong></td>
            <td>45</td>
            <td>1 line</td>
            <td>Truncate with ellipsis (…) if exceeded</td>
          </tr>
          <tr>
            <td><strong>Card description</strong></td>
            <td>120</td>
            <td>3 lines</td>
            <td>Truncate at 3 lines with ellipsis (…)</td>
          </tr>
          <tr>
            <td><strong>Button label</strong></td>
            <td>25</td>
            <td>1 line</td>
            <td>Never truncate — widen button or use icon only. Avoid wrapping.</td>
          </tr>
          <tr>
            <td><strong>Form label</strong></td>
            <td>40</td>
            <td>1 line</td>
            <td>Wraps to 2 lines if needed; avoid truncating</td>
          </tr>
          <tr>
            <td><strong>Toast/Alert message</strong></td>
            <td>100</td>
            <td>2 lines</td>
            <td>Wraps naturally; auto-dismiss after 3000ms</td>
          </tr>
          <tr>
            <td><strong>Placeholder text</strong></td>
            <td>35</td>
            <td>1 line</td>
            <td>Truncate with ellipsis (…)</td>
          </tr>
          <tr>
            <td><strong>Navigation label</strong></td>
            <td>15</td>
            <td>1 line</td>
            <td>Never truncate — shorten the label or use icon only</td>
          </tr>
        </tbody>
      </table>

      <h3>Truncation CSS</h3>
      <div class="code">
/* Single line truncation */
.truncate-1 {
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

/* Multi-line truncation (3 lines max) */
.truncate-3 {
  display: -webkit-box;
  -webkit-line-clamp: 3;
  -webkit-box-orient: vertical;
  overflow: hidden;
  text-overflow: ellipsis;
}
      </div>
    </section>

    <!-- EDGE CASES & SPECIAL CONDITIONS -->
    <section>
      <h2>Edge Cases & Special Conditions</h2>
      <p style="margin-bottom: var(--spacing-lg); color: var(--color-text-secondary);">
        These scenarios must be handled gracefully. Every design includes states for these conditions.
      </p>

      <h3>Empty States</h3>
      <div class="component-spec">
        <strong>When:</strong> User has no projects, no notifications, no data to display
        <div style="margin-top: var(--spacing-md);">
          <strong>Design includes:</strong>
          <ul style="margin-left: var(--spacing-lg); margin-top: var(--spacing-sm);">
            <li>Illustration (centered, 160px)</li>
            <li>H2 headline explaining why it's empty ("No projects yet")</li>
            <li>Description text (1–2 sentences) with suggestion ("Create your first project to get started")</li>
            <li>Primary CTA button ("Create Project") — if user can create, show CTA</li>
            <li>If user can't create (permission), show secondary info only, no CTA</li>
          </ul>
        </div>
      </div>

      <h3>Loading States</h3>
      <div class="component-spec">
        <strong>When:</strong> Data is being fetched or operation is in progress
        <div style="margin-top: var(--spacing-md);">
          <strong>Design includes:</strong>
          <ul style="margin-left: var(--spacing-lg); margin-top: var(--spacing-sm);">
            <li>Skeleton screen (for initial page load): placeholder boxes matching card layout, shimmer animation (fade 800ms, repeat)</li>
            <li>Spinner (for small operations): centered 20px spinner, color: var(--color-primary-500), rotate 360deg over 1s, linear easing</li>
            <li>Button loading state: label hides, spinner replaces text inside button</li>
            <li>Never disable the entire page while loading — show loading indicator only where needed</li>
          </ul>
        </div>
      </div>

      <h3>Error States</h3>
      <div class="component-spec">
        <strong>When:</strong> Network error, validation error, permission error, server error
        <div style="margin-top: var(--spacing-md);">
          <strong>Design includes:</strong>
          <ul style="margin-left: var(--spacing-lg); margin-top: var(--spacing-sm);">
            <li>Error message appears near the failed element (e.g., below form field)</li>
            <li>Error message color: var(--color-error) (#EF4444)</li>
            <li>Icon (optional): error icon (red) + text message</li>
            <li>Page-level error: modal or banner with error message + retry button</li>
            <li>Inline form errors: appear below each invalid field, fade in 200ms</li>
            <li>Error dismissal: auto-clear when user starts correcting, or manual close button</li>
          </ul>
        </div>
      </div>

      <h3>Disabled States</h3>
      <div class="component-spec">
        <strong>When:</strong> Action isn't available (e.g., submit button with empty form, archived item, no permission)
        <div style="margin-top: var(--spacing-md);">
          <strong>Design includes:</strong>
          <ul style="margin-left: var(--spacing-lg); margin-top: var(--spacing-sm);">
            <li>Visual indicator: reduced opacity, grayed out color, no hover effect</li>
            <li>Cursor: not-allowed</li>
            <li>Aria-disabled: "true" (for screen readers)</li>
            <li>Tooltip (optional): explain why it's disabled ("Complete all fields to continue")</li>
            <li>Don't hide disabled buttons — show them grayed out so user knows the action exists</li>
          </ul>
        </div>
      </div>

      <h3>Long Text Handling</h3>
      <div class="component-spec">
        <strong>When:</strong> User input or data is longer than expected (long names, descriptions, email addresses)
        <div style="margin-top: var(--spacing-md);">
          <strong>Design includes:</strong>
          <ul style="margin-left: var(--spacing-lg); margin-top: var(--spacing-sm);">
            <li>Card title with long content: truncate with ellipsis (…) at 1 line, use title="full text" for browser tooltip</li>
            <li>Button labels: if too long, widen button (don't truncate) or abbreviate label upfront</li>
            <li>Form labels: allow wrapping to 2 lines naturally</li>
            <li>Body text: allow natural wrapping; set max-width if needed (1000px for readability)</li>
            <li>Use word-break: break-word for long URLs or code snippets that can't wrap</li>
          </ul>
        </div>
      </div>

      <h3>No Network / Offline</h3>
      <div class="component-spec">
        <strong>When:</strong> Device loses internet connection
        <div style="margin-top: var(--spacing-md);">
          <strong>Design includes:</strong>
          <ul style="margin-left: var(--spacing-lg); margin-top: var(--spacing-sm);">
            <li>Show banner at top: "No connection. Some features are limited." (warning yellow background)</li>
            <li>Disable form submissions, API calls — show tooltip if user tries</li>
            <li>Show cached data if available (last fetched data)</li>
            <li>Auto-retry when connection returns (no manual retry needed)</li>
          </ul>
        </div>
      </div>

      <h3>RTL/Arabic Layout</h3>
      <div class="component-spec">
        <strong>When:</strong> App is rendered in Arabic or other RTL language
        <div style="margin-top: var(--spacing-md);">
          <strong>Design includes:</strong>
          <ul style="margin-left: var(--spacing-lg); margin-top: var(--spacing-sm);">
            <li>Add <code>dir="rtl"</code> to HTML root element</li>
            <li>Sidebar navigation: right side (not left) when RTL</li>
            <li>FAB (Floating Action Button): bottom-left (not bottom-right)</li>
            <li>Icons: some icons mirror (chevrons, arrows), others don't (checkmarks, dots)</li>
            <li>Margins/padding: CSS logical properties (margin-inline-start, margin-inline-end) automatically flip</li>
            <li>Font: Use Tajawal (open source Arabic font) weights 400, 600, 700 at same sizes as Latin fonts</li>
            <li>Numbers: Stay LTR even in RTL context (e.g., "3 items" reads left-to-right even in Arabic)</li>
            <li>Test in real browser (not just flipped screenshots) — layout, text direction, icon direction</li>
          </ul>
        </div>
      </div>

    </section>

    <!-- ACCESSIBILITY GUIDELINES -->
    <section>
      <h2>Accessibility Guidelines</h2>
      <p style="margin-bottom: var(--spacing-lg); color: var(--color-text-secondary);">
        Accessibility is not a feature — it's built into every component and screen.
      </p>

      <h3>Color Contrast</h3>
      <ul style="margin-left: var(--spacing-lg);">
        <li><strong>Normal text (14px+):</strong> 4.5:1 contrast ratio (WCAG AA)</li>
        <li><strong>Large text (18px+ or 14px bold):</strong> 3:1 contrast ratio (WCAG AA)</li>
        <li><strong>Disabled text:</strong> May be lower; still test with assistive tech</li>
        <li><strong>Never use color alone to convey information.</strong> Add icons, text, or patterns.</li>
      </ul>

      <h3>Focus Management</h3>
      <ul style="margin-left: var(--spacing-lg);">
        <li><strong>All interactive elements must have focus visible:</strong> outline or background change</li>
        <li><strong>Focus outline:</strong> 3px solid var(--color-primary-300) with 3px offset (or similar contrast)</li>
        <li><strong>Focus order:</strong> Use logical tab order (left-to-right, top-to-bottom)</li>
        <li><strong>Skip link:</strong> First element on every page (off-screen, visible on focus) links to main content</li>
        <li><strong>Modal focus trap:</strong> When modal opens, focus moves to first focusable element; Tab stays within modal</li>
      </ul>

      <h3>Keyboard Navigation</h3>
      <ul style="margin-left: var(--spacing-lg);">
        <li><strong>Tab:</strong> Navigate forward through focusable elements</li>
        <li><strong>Shift + Tab:</strong> Navigate backward</li>
        <li><strong>Enter / Space:</strong> Activate buttons, links, toggle checkboxes</li>
        <li><strong>Arrow keys:</strong> Navigate within lists, tabs, sliders (if applicable)</li>
        <li><strong>Escape:</strong> Close modals, dropdowns, popovers</li>
        <li><strong>Never trap focus:</strong> Users can always escape or navigate out</li>
      </ul>

      <h3>Screen Reader Support</h3>
      <ul style="margin-left: var(--spacing-lg);">
        <li><strong>Aria-label:</strong> Icon-only buttons must have labels ("Close", "Settings", "More options")</li>
        <li><strong>Aria-labelledby:</strong> Connect headings to content regions (e.g., modal title)</li>
        <li><strong>Aria-describedby:</strong> Add extra context for complex components (e.g., help text below form field)</li>
        <li><strong>Aria-disabled:</strong> "true" when element is disabled (in addition to visual change)</li>
        <li><strong>Aria-busy:</strong> "true" during loading; "false" when done</li>
        <li><strong>Role attributes:</strong> Add roles for custom components (role="alert" for toast notifications)</li>
        <li><strong>Semantic HTML:</strong> Use &lt;button&gt;, &lt;input&gt;, &lt;label&gt; instead of &lt;div&gt; + role</li>
        <li><strong>Skip redundant announcements:</strong> aria-hidden="true" for decorative icons, hidden spinners</li>
      </ul>

      <h3>Touch Target Size</h3>
      <ul style="margin-left: var(--spacing-lg);">
        <li><strong>Minimum:</strong> 48×48px for all interactive elements on mobile</li>
        <li><strong>Spacing:</strong> At least 8px between separate touch targets (or 4px if grouped)</li>
        <li><strong>Button height:</strong> 48px (padding: 12px 24px)</li>
        <li><strong>Icon buttons:</strong> 48×48px minimum with centered icon inside</li>
      </ul>

    </section>

    <!-- HANDOFF CHECKLIST -->
    <section>
      <h2>Handoff Checklist</h2>
      <p style="margin-bottom: var(--spacing-lg); color: var(--color-text-secondary);">
        Use this checklist before sending handoff to developers.
      </p>

      <ul class="checklist">
        <li>All screens are exported as working HTML in <code>screens.html</code></li>
        <li>Every interactive component has all required states designed (default, hover, focus, active, disabled, loading, error)</li>
        <li>All color values in CSS use custom properties (--color-*) — no hardcoded hex values</li>
        <li>All spacing uses custom properties (--spacing-xs, --spacing-sm, etc.) — no arbitrary pixel values</li>
        <li>Typography uses consistent sizes and weights from the scale (--type-h1, --type-body, etc.)</li>
        <li>Interaction timings and easing are specified for every animation (duration + cubic-bezier function)</li>
        <li>Content rules documented for text-heavy components (character limits, truncation behavior)</li>
        <li>Empty states designed and included for all dynamic content (list, search results, no data)</li>
        <li>Error states designed (validation errors, network errors, permission errors)</li>
        <li>Loading states designed (skeleton screens, spinners, button loading state)</li>
        <li>Disabled states designed (grayed out, visual indication, aria-disabled set)</li>
        <li>Long text handling specified (truncation rules, word-break behavior)</li>
        <li>Responsive behavior specified for each breakpoint (mobile, tablet, desktop)</li>
        <li>Accessibility notes included (aria-labels for icon buttons, focus order, color contrast verified)</li>
        <li>Focus visible state designed for all interactive elements (outline or background change)</li>
        <li>RTL/Arabic version verified in a real browser (not just screenshots) — layout, text direction, icon direction</li>
        <li>Arabic font specified (Tajawal) with weights and sizes</li>
        <li>All design tokens documented in a table with usage notes</li>
        <li>Component specifications include dimensions, typography, states, accessibility, content rules, code examples</li>
        <li>Screen inventory lists all screens with routes, descriptions, and navigation connections</li>
        <li>Interaction specs documented for every animation and transition (trigger, timing, easing, steps)</li>
        <li>All files tested in a real browser — no syntax errors, all states accessible</li>
        <li>Developer walkthrough scheduled (don't just send files)</li>
      </ul>
    </section>

    <!-- WORKING WITH DEVELOPERS -->
    <section>
      <h2>Working with Developers — Communication Patterns</h2>

      <h3>Schedule a Walkthrough</h3>
      <p>
        Don't just send files and expect developers to figure it out. Schedule a 30–60 minute walkthrough where you:
      </p>
      <ul style="margin-left: var(--spacing-lg);">
        <li>Walk through the user flow (not individual screens)</li>
        <li>Explain WHY design decisions were made (not just what to build)</li>
        <li>Highlight edge cases and special handling</li>
        <li>Identify what's MVP vs. Phase 2</li>
        <li>Answer questions in real time</li>
        <li>Share screen and interact with <code>screens.html</code> together</li>
      </ul>

      <h3>Be Specific About Interactions</h3>
      <p>
        When a developer says "How should the button animation work?" you say:
      </p>
      <p style="margin-left: var(--spacing-lg); margin-top: var(--spacing-sm); padding: var(--spacing-md); background: #f0f4ff; border-radius: 6px;">
        "On hover, the background color changes from primary-500 to primary-600 over 150ms with ease-out easing.
        On click, it scales to 0.98 and changes to primary-700, also over 100ms. The focus state is a 3px outline
        with 3px offset in primary-300. Reference the interaction spec for exact timing."
      </p>

      <h3>Flag Complex Interactions Early</h3>
      <p>
        Identify anything that requires custom JavaScript or complex animation upfront. Examples:
      </p>
      <ul style="margin-left: var(--spacing-lg);">
        <li>Drag-and-drop interactions</li>
        <li>Complex animations (parallax, morphing shapes, etc.)</li>
        <li>Custom chart interactions</li>
        <li>Gesture detection (swipe, pinch, long-press)</li>
        <li>Canvas or WebGL elements</li>
      </ul>
      <p>
        Discuss feasibility and timeline before implementation starts.
      </p>

      <h3>Clarify MVP vs. Phase 2</h3>
      <p>
        Clearly mark which features are essential for launch vs. future phases:
      </p>
      <ul style="margin-left: var(--spacing-lg);">
        <li><strong>MVP (Phase 1):</strong> Core screens, primary interactions, essential components</li>
        <li><strong>Phase 2:</strong> Polish animations, nice-to-have states, advanced interactions</li>
      </ul>
      <p>
        This prevents scope creep and focuses development on what matters most.
      </p>

      <h3>Be Available for Questions</h3>
      <p>
        Developers will have questions during implementation. Be accessible and responsive:
      </p>
      <ul style="margin-left: var(--spacing-lg);">
        <li>"Is this how the error message should appear?"</li>
        <li>"What happens when the user navigates away during a save?"</li>
        <li>"Should this label wrap or truncate on mobile?"</li>
        <li>Answer quickly — unblocking a developer is worth your time</li>
      </ul>
    </section>

    <!-- DESIGN TOKENS REFERENCE TEMPLATE -->
    <section>
      <h2>Design Tokens Reference (Copy for tokens.css)</h2>
      <p style="margin-bottom: var(--spacing-lg); color: var(--color-text-secondary);">
        Use this template as a starting point for <code>tokens.css</code>. Customize colors, sizes, and values for your project.
      </p>

      <div class="code">
:root {
  /* ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ */
  /* COLORS — Primary Brand */
  /* ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ */
  --color-primary-50: #f0f4ff;
  --color-primary-100: #e0e7ff;
  --color-primary-200: #c7d2fe;
  --color-primary-300: #a5b4fc;
  --color-primary-400: #818cf8;
  --color-primary-500: #4f46e5;
  --color-primary-600: #4338ca;
  --color-primary-700: #3730a3;
  --color-primary-800: #312e81;
  --color-primary-900: #1e1b4b;

  /* ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ */
  /* COLORS — Semantic */
  /* ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ */
  --color-success: #10b981;
  --color-success-light: #d1fae5;
  --color-error: #ef4444;
  --color-error-light: #fee2e2;
  --color-warning: #f59e0b;
  --color-warning-light: #fef3c7;
  --color-info: #3b82f6;
  --color-info-light: #dbeafe;

  /* ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ */
  /* COLORS — Neutral */
  /* ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ */
  --color-text-primary: #111827;
  --color-text-secondary: #6b7280;
  --color-text-tertiary: #9ca3af;
  --color-bg-page: #f9fafb;
  --color-bg-surface: #ffffff;
  --color-border: #e5e7eb;
  --color-border-light: #f3f4f6;

  /* ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ */
  /* TYPOGRAPHY — Font Family */
  /* ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ */
  --font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto',
                 'Oxygen', 'Ubuntu', 'Cantarell', 'Fira Sans', 'Droid Sans',
                 'Helvetica Neue', sans-serif;
  --font-family-mono: 'Monaco', 'Courier New', monospace;

  /* ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ */
  /* TYPOGRAPHY — Font Weight */
  /* ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ */
  --font-weight-light: 300;
  --font-weight-regular: 400;
  --font-weight-medium: 500;
  --font-weight-semibold: 600;
  --font-weight-bold: 700;

  /* ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ */
  /* TYPOGRAPHY — Font Size */
  /* ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ */
  --font-size-xs: 12px;
  --font-size-sm: 14px;
  --font-size-base: 16px;
  --font-size-lg: 18px;
  --font-size-xl: 20px;
  --font-size-2xl: 24px;
  --font-size-3xl: 28px;
  --font-size-4xl: 32px;

  /* ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ */
  /* TYPOGRAPHY — Line Height */
  /* ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ */
  --line-height-tight: 1.2;
  --line-height-snug: 1.375;
  --line-height-normal: 1.5;
  --line-height-relaxed: 1.625;
  --line-height-loose: 2;

  /* ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ */
  /* SPACING */
  /* ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ */
  --spacing-0: 0;
  --spacing-xs: 4px;
  --spacing-sm: 8px;
  --spacing-md: 16px;
  --spacing-lg: 24px;
  --spacing-xl: 32px;
  --spacing-2xl: 48px;
  --spacing-3xl: 64px;

  /* ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ */
  /* BORDER RADIUS */
  /* ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ */
  --radius-sm: 4px;
  --radius-md: 8px;
  --radius-lg: 12px;
  --radius-xl: 16px;
  --radius-full: 9999px;

  /* ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ */
  /* SHADOWS / ELEVATION */
  /* ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ */
  --shadow-sm: 0 1px 2px 0 rgba(0, 0, 0, 0.05);
  --shadow-md: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
  --shadow-lg: 0 10px 15px -3px rgba(0, 0, 0, 0.1);
  --shadow-xl: 0 20px 25px -5px rgba(0, 0, 0, 0.1);

  /* ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ */
  /* ANIMATION — DURATION */
  /* ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ */
  --duration-fast: 150ms;
  --duration-base: 250ms;
  --duration-slow: 350ms;

  /* ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ */
  /* ANIMATION — EASING */
  /* ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ */
  --easing-ease-in: cubic-bezier(0.4, 0, 1, 1);
  --easing-ease-out: cubic-bezier(0.4, 0, 0.2, 1);
  --easing-ease-in-out: cubic-bezier(0.4, 0, 0.2, 1);
  --easing-linear: linear;
}
      </div>
    </section>

    <footer style="text-align: center; color: var(--color-text-secondary); margin-top: var(--spacing-2xl); padding-top: var(--spacing-xl); border-top: 1px solid var(--color-border);">
      <p>
        Design Handoff Guide — DesignXI | Updated March 2026 |
        <a href="#" style="color: var(--color-primary-600); text-decoration: none;">Back to top</a>
      </p>
    </footer>

  </div>
</body>
</html>
```

---

## Quick Reference: What Developers Need

Print this on your wall:

1. **Tokens** — All colors, spacing, type, shadows as CSS variables
2. **States** — Default, hover, focus, active, disabled, loading, error, empty
3. **Responsive** — What changes at mobile / tablet / desktop
4. **Content** — Character limits, truncation rules, line limits
5. **Edge cases** — Long text, no data, errors, offline
6. **Interactions** — Timing, easing, trigger conditions
7. **Accessibility** — Focus visible, aria labels, color contrast, touch targets

Without these, developers guess. With these, they build correctly.

---

## How to Use This Document

1. **Customize the template above** — Copy the HTML, replace [Project Name], adjust colors/spacing for your project
2. **Fill in your component specs** — Primary Button is an example; add Button Secondary, Input, Card, Modal, etc.
3. **Document every interaction** — Form submit, page transition, modal open — every animation gets a spec
4. **Run through the checklist** — Before handing off to developers
5. **Schedule a walkthrough** — Send this document, but don't rely on it alone
6. **Stay available** — Answer questions during implementation

A great handoff isn't just documentation — it's a partnership between designers and developers that results in a product that works beautifully.

---

## Content Specifications — Design for Real Data

Designs that only work with perfect, short, clean data fail in production. Document content rules as part of every component spec.

### Character Limits and Truncation Rules

Every text element needs a maximum character count and an overflow behavior:

| Element | Max Characters | Overflow Behavior |
|---------|---------------|-------------------|
| Page title (H1) | 60 chars | Wrap to 2 lines max, then truncate |
| Card title | 40 chars | Single line, ellipsis at end |
| Card description | 120 chars | 3 lines max, ellipsis |
| Navigation label | 20 chars | Single line, never truncate |
| Button label | 30 chars | Never truncate — redesign if too long |
| Toast notification | 80 chars | Single line — write shorter copy |
| Badge / Tag | 15 chars | Single line, truncate with tooltip |
| Username / Display name | 30 chars | Truncate with full name in tooltip |
| Table cell (text) | 60 chars | Truncate — show full on hover/tap |

**Truncation rules:**
- Use CSS `text-overflow: ellipsis` + `overflow: hidden` + `white-space: nowrap`
- Always provide the full content via `title` attribute or tooltip on hover
- Never truncate navigation labels — they must always be fully readable
- For RTL (Arabic): truncation happens at the LEFT end, not right

### Edge Cases That Must Be Designed

Before handoff, design these states for every data-driven component:

```
1. Maximum content length
   - Headline with 80 characters: does it wrap cleanly?
   - Username "محمد عبدالرحمن الإبراهيم" (30 chars Arabic): does layout hold?

2. Minimum content length
   - 1-letter username "A": does avatar/card look right?
   - Empty description "": does the component handle gracefully (hide or placeholder)?

3. Long unbroken strings (no spaces)
   - URL in text field: "https://www.verylongdomain.com/path/to/page"
   - Use: overflow-wrap: break-word + word-break: break-all as fallback

4. Numbers at scale
   - Counter showing "1,284,930 followers" — does layout break?
   - Price showing "$1,299.99" — does formatting hold?

5. List at extremes
   - 0 items: empty state designed?
   - 1 item: singular language ("1 result", not "1 results")
   - 1000+ items: virtualized? Paginated? Export option?

6. RTL strings in LTR layout (and vice versa)
   - Arabic name in English-first UI: bidirectional text handled?
   - Use: dir="auto" on text inputs

7. Images that fail to load
   - Avatar fallback: initials or generic icon?
   - Product image 404: placeholder or remove element?

8. Offline / no data
   - Network error: specific message + retry CTA
   - Partial data load: what shows, what's hidden?
```

### The "Why" Rationale in Handoff Documentation

Developers who understand the intent make better judgment calls when edge cases arise. Every non-obvious design decision deserves a rationale note:

```markdown
## Component: Primary Button

### Why 48px minimum height (not 44px or 40px)?
iOS HIG requires 44pt, Material Design requires 48dp. We use 48px as the safer 
cross-platform minimum. This ensures the button passes touch target size requirements 
on both platforms without exception tracking.

### Why no text-transform: uppercase on button labels?
All-caps text reduces reading speed by ~12% (source: research by Miles Tinker). 
We use title case for CTAs instead — more readable, equally prominent with semibold weight.

### Why border-radius: 8px (not 4px or 12px)?
Our brand identity uses a "confident but approachable" personality. Sharp corners 
(4px) feel corporate/cold. Very rounded (12px+) feels soft/playful. 8px is the 
deliberate middle point that matches brand positioning.
```

Add "Why" rationale for:
- Any spacing or sizing choice that differs from the design system defaults
- Color combinations that might seem unusual
- Interaction patterns that deviate from platform conventions
- Any animation or transition that has unusual timing
- Accessibility decisions that affect visual design (focus rings, contrast adjustments)

### Handoff Completeness Checklist (Enhanced)

```
CONTENT & DATA
□ Character limits documented for all text elements
□ Truncation behavior defined (ellipsis, wrap, hide)
□ Empty state designed for every data-driven component
□ Error state designed (network, validation, permission)
□ Loading state designed (skeleton or spinner — not both)
□ Maximum data volume tested (100 items, long strings)
□ RTL strings tested in all text containers

RATIONALE
□ Non-obvious sizing decisions have "Why" notes
□ Color choices reference the brand spec, not arbitrary
□ Animation timing choices documented with rationale
□ Platform deviations explained (why we deviate from iOS/Material)
□ Accessibility trade-offs documented (if any visual change was for a11y)
```

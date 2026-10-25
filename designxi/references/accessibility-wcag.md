# WCAG 2.1 AA Accessibility Rules for UX/UI Design

A practical guide for implementing Web Content Accessibility Guidelines Level AA in HTML/CSS design work. This reference ensures your designs are usable by all people, including those with disabilities.

---

## Why WCAG 2.1 AA Matters

### Legal Requirements

WCAG 2.1 AA is the web accessibility standard recognized by most jurisdictions:
- **United States**: Section 508 of the Rehabilitation Act and the ADA increasingly require WCAG 2.1 AA compliance
- **European Union**: The European Accessibility Act mandates WCAG 2.1 AA for web content
- **United Kingdom**: Public sector websites must meet WCAG 2.1 AA
- **Canada**: AODA (Accessibility for Ontarians with Disabilities Act) requires WCAG 2.1 AA compliance
- **Australia**: Disability Discrimination Act requires accessible web content

Non-compliance exposes your organization to legal liability, lawsuits, and regulatory fines.

### User Impact

- **15-20% of the population has some form of disability** (WHO data)
- **16% have low vision** and benefit from high contrast and resizable text
- **3-4% are completely blind** and rely on screen readers
- **5-10% have motor disabilities** and depend on keyboard navigation
- **7-11% have hearing disabilities** and need captions and transcripts
- **8-15% have cognitive disabilities** and benefit from clear language and structure

Accessible design is good design for everyone—not just people with disabilities.

### Design Impact

Accessibility constraints often improve overall design:
- **Better typography** improves readability for all users
- **Clear focus states** help users navigate faster
- **Proper color contrast** reduces eye strain
- **Keyboard navigation** enables power users and mobile accessibility
- **Semantic HTML** improves SEO and performance
- **Clear language** reduces support burden

---

## The 4 WCAG Principles (POUR)

WCAG is built on four core principles. Everything a designer does should support these principles.

### 1. **Perceivable**

Users must be able to perceive the information in your interface. They can't act on what they can't see, hear, or sense.

**Practical UI Implications:**
- Provide **sufficient color contrast** so text is readable by users with low vision
- Ensure **text is resizable** to 200% without breaking layout
- Provide **alt text for images** so screen reader users understand them
- Include **captions and transcripts** for video and audio content
- Don't use **color alone** to convey information (also use icons, text, patterns)
- Make **interactive elements distinguishable** from the background

**Example:** A red error message is not perceivable to colorblind users. Add an icon or text prefix: "Error: " + red text + error icon.

### 2. **Operable**

Users must be able to operate all functionality using whatever input method they have—keyboard, mouse, touch, voice, switch control.

**Practical UI Implications:**
- All functionality must be **keyboard accessible** (Tab, Enter, Escape, arrow keys)
- Interactive elements must be **large enough to click** (44×44px minimum)
- Users must be able to **navigate logically** through the interface (logical tab order)
- No **keyboard traps** (user gets stuck when tabbing)
- Provide **skip navigation links** to jump over repetitive content
- Respect **prefers-reduced-motion** for users with vestibular disorders

**Example:** A carousel that only responds to mouse hover is not operable for keyboard or touch users. Make it work with arrow keys and touch swipes.

### 3. **Understandable**

Users must be able to understand the content and how to operate the interface.

**Practical UI Implications:**
- Use **clear, plain language** (avoid jargon and complex sentences)
- Provide **visible labels for all inputs** (not just placeholder text)
- Use **consistent patterns** across the interface
- Indicate **required fields** clearly
- Display **error messages** that explain what went wrong and how to fix it
- Use **proper heading hierarchy** (h1 → h2 → h3, no skipping levels)
- Use **semantic HTML** (buttons are `<button>`, links are `<a>`, headings are `<h1>-<h6>`)

**Example:** A form field with only placeholder text "john@example.com" is confusing. Add a visible label: "Email address *"

### 4. **Robust**

Your content must be robust enough to be interpreted reliably by assistive technologies (screen readers, magnifiers, voice control).

**Practical UI Implications:**
- Use **semantic HTML first** (`<button>`, `<a>`, `<input>`, `<label>`)
- Use **ARIA attributes** only when semantic HTML is insufficient
- Ensure **proper heading hierarchy** for screen reader navigation
- Use **live regions** to announce dynamic content changes
- Validate **HTML for errors** (invalid markup confuses assistive technology)
- Don't override **default keyboard behavior** without good reason
- Use **proper language attributes** (`lang="en"`, `lang="ar"`)

**Example:** Don't build a button from a `<div>` and JavaScript. Use `<button>` which has correct keyboard support and screen reader announcement built-in.

---

## Color & Contrast Rules

Color contrast is one of the most important and most frequently failed accessibility requirement. Low contrast text is hard to read for everyone, especially people with low vision, color blindness, or eye strain.

### Contrast Ratio Minimums (WCAG 2.1 AA)

| Element | Minimum Ratio | Calculation |
|---------|--------------|-------------|
| Normal text (< 18pt or < 14pt bold) | **4.5:1** | Text luminance vs. background luminance |
| Large text (≥ 18pt or ≥ 14pt bold) | **3:1** | More forgiving for bigger text |
| UI components & graphical objects | **3:1** | Buttons, icons, form borders, focus rings |

### Contrast Ratio Formula

The WCAG contrast ratio is calculated using relative luminance:

```
Contrast Ratio = (L1 + 0.05) / (L2 + 0.05)

Where:
L = Relative Luminance of the lighter color
L = Relative Luminance of the darker color

Relative Luminance is calculated as:
- If R/G/B <= 0.03928: RGB value / 12.92
- If R/G/B > 0.03928: ((RGB value + 0.055) / 1.055) ^ 2.4
```

**In practice:** Use a contrast checker tool rather than calculating manually.

### Common Failures & Fixes

| Failure | Problem | Fix |
|---------|---------|-----|
| Gray text on white | Too light, hard to read | Use darker gray: #666 or darker |
| Light blue on white | Only 2:1 ratio (fails) | Use darker blue: #0066CC or add darker blue |
| Blue text on blue background | Impossible to read | Use contrasting color: white on blue or dark text on light background |
| Disabled state text too light | Can't read disabled buttons | Use #999 or darker for disabled text |
| Placeholder text gray | Too faint (usually #999) | Use #666 minimum, or make it darker |

### CSS Example: Compliant Color Pairings

```css
/* Good: Normal text with proper contrast */
body {
  color: #1a1a1a;        /* Very dark gray on white: 21:1 ratio */
  background: #ffffff;
}

/* Good: Large text can use lighter colors */
.large-text {
  font-size: 24px;
  color: #333333;        /* Dark gray: 12:1 ratio */
  background: #ffffff;
}

/* Good: Links with sufficient contrast */
a {
  color: #0066cc;        /* Dark blue: 8.6:1 on white */
  text-decoration: underline; /* Not just color */
}

a:visited {
  color: #660099;        /* Dark purple: 5.4:1 on white */
}

/* Bad: Too light - FAILS AA */
.fails-contrast {
  color: #cccccc;        /* Light gray: 1.13:1 ratio */
  background: #ffffff;
}

/* Good: UI components with minimum 3:1 */
.button {
  border: 2px solid #0066cc;   /* Dark blue: 8.6:1 ratio */
  background: #ffffff;
  color: #0066cc;
}

.button:focus {
  outline: 3px solid #ff8800;  /* Orange focus ring: 4.5:1 on white */
}

/* Good: Disabled state still readable */
.button:disabled {
  color: #666666;        /* Dark gray: 7:1 ratio */
  background: #f5f5f5;
  border-color: #999999;
  cursor: not-allowed;
}
```

### Tools to Check Contrast

- **WebAIM Contrast Checker**: webaim.org/resources/contrastchecker/
- **Color Contrast Analyser** (by TPGI): Free desktop app for Windows/Mac
- **Stark** (Figma plugin): Real-time contrast checking in Figma
- **Chrome DevTools**: Built-in contrast ratio checker in the color picker

---

## Typography Accessibility

Readable text is foundational to accessible design. Poor typography alienates people with low vision, dyslexia, and cognitive disabilities.

### Minimum Font Size

- **Body text**: 16px minimum (recommended, never below 12px)
- **UI labels**: 14px minimum
- **Captions**: 14px minimum
- **Small text** (help text, metadata): 12px minimum with increased line-height

```css
body {
  font-size: 16px;  /* Standard readable size */
}

.caption {
  font-size: 14px;  /* Smaller but acceptable */
}

.help-text {
  font-size: 12px;
  line-height: 1.8;  /* Increase line height for smaller text */
}
```

### Line Height (Leading)

- **Minimum**: 1.5x the font size for body text
- **Ideal**: 1.6x for better readability
- **Larger**: 1.8x or more for people with dyslexia

```css
body {
  font-size: 16px;
  line-height: 1.5;  /* = 24px spacing between lines */
}

/* For dyslexia-friendly design */
body {
  line-height: 1.8;  /* = 28.8px spacing */
}
```

### Letter Spacing & Word Spacing

- **Letter spacing**: 0.12em minimum (0.02em is common default—increase if possible)
- **Word spacing**: Default is fine, but avoid condensed fonts

```css
body {
  font-size: 16px;
  letter-spacing: 0.05em;  /* Slight increase for readability */
  word-spacing: 0.15em;    /* Slight increase helps separation */
}

/* For difficult-to-read fonts or small sizes */
.dyslexia-friendly {
  font-family: 'Comic Sans MS', cursive;  /* Designed for dyslexia */
  font-size: 16px;
  line-height: 1.8;
  letter-spacing: 0.1em;
}
```

### No Justified Text

Never use `text-align: justify` for body text. It creates irregular spacing between words, which:
- Makes text harder to read for people with dyslexia
- Creates "rivers" of white space
- Is difficult for screen readers to interpret properly

```css
/* Good */
p {
  text-align: left;  /* Default, most readable */
}

/* Bad - avoid */
p {
  text-align: justify;  /* Creates uneven spacing */
}
```

### Resizable Text (Up to 200%)

Users must be able to resize text to 200% without loss of functionality. This is tested by zooming in the browser.

**What breaks accessibility:**
- Fixed widths that don't expand with text
- `overflow: hidden` that clips text
- Absolute positioning that overlaps resized text
- Fixed heights that don't grow with content

```css
/* Good: Uses relative units and grows with text */
body {
  font-size: 16px;
  max-width: 1200px;  /* Containers can be max-width, they'll shrink on mobile */
}

p {
  margin: 1em;        /* Relative to font size */
}

/* Bad: Fixed width doesn't grow with text */
.card {
  width: 300px;       /* Won't work well at 200% zoom */
  overflow: hidden;   /* Text gets clipped */
}

/* Good: Flexible container */
.card {
  max-width: 300px;
  padding: 1.5em;
  overflow: visible;
}
```

---

## Touch Targets & Interactive Elements

People with motor disabilities, arthritis, or using touchscreens need large touch targets. Small buttons are frustrating for everyone.

### Minimum Sizes

| Standard | Size | Notes |
|----------|------|-------|
| **Apple HIG** | 44×44px | Industry standard for iOS |
| **Material Design** | 48×48dp | Android standard |
| **WCAG 2.1 AA Minimum** | 44×44px | Formal requirement |

### Spacing Between Targets

- **Minimum**: 8px gap between adjacent interactive elements
- **Ideal**: 12-16px gap for comfortable spacing
- For touch interfaces, prefer 16px+ gaps

### Implementation in CSS

```css
/* Good: Proper size and spacing */
.button {
  min-width: 44px;
  min-height: 44px;
  padding: 12px 16px;
  margin-right: 8px;  /* Spacing from next button */
}

/* Good: Icon button with minimum size */
.icon-button {
  width: 44px;
  height: 44px;
  display: flex;
  align-items: center;
  justify-content: center;
}

/* Good: Using padding to expand touch area */
a {
  padding: 12px 16px;  /* Increases clickable area */
  display: inline-block;
}

/* Good: Link in text with expanded touch area */
a {
  position: relative;
}

a::before {
  content: '';
  position: absolute;
  top: -6px;
  bottom: -6px;
  left: -6px;
  right: -6px;  /* Expands clickable area without visual expansion */
}

/* Bad: Too small */
.small-button {
  width: 24px;
  height: 24px;  /* Fails WCAG */
}

/* Bad: No spacing */
.button-group button {
  margin: 0;  /* Buttons touching—hard to tap individually */
}
```

---

## Focus States

Every interactive element must have a visible focus indicator. This is critical for keyboard users and people using switch control or voice activation.

### Focus Ring Requirements

- **Minimum size**: 3px solid or 2px double outline
- **Contrast ratio**: Minimum 3:1 against adjacent colors
- **Never remove**: Don't use `outline: none` without a replacement

### CSS Examples

```css
/* Good: Default browser focus (works for most) */
button:focus {
  outline: 2px solid #4a90e2;
  outline-offset: 2px;
}

/* Good: Custom visible focus ring */
button:focus-visible {
  outline: 3px solid #ff8800;      /* Orange for high contrast */
  outline-offset: 2px;
  border-radius: 4px;
}

/* Good: Focus ring using box-shadow (works better with border-radius) */
button:focus {
  box-shadow: 0 0 0 3px #4a90e2;   /* Blue ring around button */
}

/* Good: Text input focus */
input:focus {
  outline: 2px solid #0066cc;
  outline-offset: 2px;
}

/* Good: Focus ring for custom components */
.custom-button:focus {
  outline: 3px solid #ff8800;
  outline-offset: 3px;
}

/* Bad: No focus indicator - FAILS */
button:focus {
  outline: none;  /* Removes focus—keyboard users can't see where they are */
}

/* Bad: Focus that blends in - FAILS */
button:focus {
  outline: 1px solid #cccccc;  /* Too light, only 1.5:1 contrast */
}

/* Bad: Focus with negative offset - hard to see */
button:focus {
  outline: 1px solid blue;
  outline-offset: -1px;  /* Sits inside the button, hard to see */
}
```

### Modern Focus Approach: :focus-visible

Use `:focus-visible` instead of `:focus` for keyboard-only focus styling:

```css
/* Show focus ring only for keyboard users, not mouse/touch */
button:focus-visible {
  outline: 3px solid #ff8800;
  outline-offset: 2px;
}

/* Fallback for older browsers */
button:focus {
  outline: 3px solid #ff8800;
  outline-offset: 2px;
}
```

---

## Forms & Inputs

Forms are one of the most common accessibility problem areas. Poor form design frustrates everyone, but is impossible for some users.

### Every Input Must Have a Visible Label

**Never use placeholder text as the only label.** Placeholder text:
- Disappears when the user starts typing
- Is often too light to read
- Is not announced by screen readers as a label

```html
<!-- Bad: No visible label -->
<input type="email" placeholder="Email address" />

<!-- Good: Visible label connected to input -->
<label for="email">Email address *</label>
<input type="email" id="email" name="email" required aria-required="true" />

<!-- Good: Label with help text -->
<label for="password">
  Password *
  <span class="help-text">(minimum 12 characters)</span>
</label>
<input type="password" id="password" name="password" required />
```

### Error Messages (Text + Icon, Not Color Alone)

Never indicate errors using color alone. Users with color blindness won't see them.

```html
<!-- Bad: Color only -->
<input type="email" style="border: 2px solid red;" value="invalid" />

<!-- Good: Text + icon + color -->
<div role="alert">
  <svg class="error-icon" aria-hidden="true"><!-- Error icon --></svg>
  <span>Please enter a valid email address (example@domain.com)</span>
</div>
<input
  type="email"
  id="email"
  value="invalid"
  aria-invalid="true"
  aria-describedby="email-error"
  style="border: 2px solid #d32f2f;"
/>
```

### Required Fields Must Be Clearly Indicated

Don't rely on asterisks alone. Some users don't understand this notation.

```html
<!-- Good: Multiple indicators -->
<label for="name">
  Name
  <span aria-label="required">*</span>
</label>
<input type="text" id="name" required aria-required="true" />

<!-- Good: Text label -->
<fieldset>
  <legend>Address <span class="required-notice">(required)</span></legend>
  <input type="text" required />
</fieldset>

<!-- Good: Clear legend -->
<fieldset>
  <legend>Which services are you interested in? (Select at least one)</legend>
  <input type="checkbox" name="service" value="design" /> Design
  <input type="checkbox" name="service" value="dev" /> Development
</fieldset>
```

### Autocomplete Attributes

Help password managers and browsers fill forms correctly:

```html
<!-- Email input -->
<input type="email" autocomplete="email" />

<!-- Password -->
<input type="password" autocomplete="current-password" />

<!-- New password (registration) -->
<input type="password" autocomplete="new-password" />

<!-- Name -->
<input type="text" autocomplete="name" />

<!-- Phone -->
<input type="tel" autocomplete="tel" />

<!-- Address -->
<input type="text" autocomplete="street-address" />
<input type="text" autocomplete="postal-code" />

<!-- Credit card (if you must) -->
<input type="text" autocomplete="cc-number" />
<input type="text" autocomplete="cc-exp" />
```

### Input Purpose Attributes

Help users understand what an input is for, especially on mobile:

```html
<!-- Triggers numeric keyboard on mobile -->
<input type="tel" inputmode="numeric" />

<!-- Triggers email keyboard -->
<input type="email" inputmode="email" />

<!-- Triggers URL keyboard -->
<input type="url" inputmode="url" />

<!-- Triggers search keyboard -->
<input type="search" />
```

---

## Images & Icons

Images communicate information, but only if users can perceive them.

### Alt Text Rules

| Image Type | Alt Text | Example |
|-----------|----------|---------|
| **Informative** | Describe the content and function | `alt="Young professional woman smiling at camera"` |
| **Decorative** | Leave empty (alt="") | `alt=""` for a divider line or background pattern |
| **Complex** | Brief alt + link to longer description | `alt="Sales chart, see chart description"` |
| **Icon button** | Describe the action | `alt="Add new item"` or use aria-label |
| **Chart/graph** | Provide data summary | `alt="Monthly revenue increased 15% Q1 to Q2"` |

```html
<!-- Informative: Describe what you see -->
<img src="team-photo.jpg" alt="Engineering team of 5 people at office" />

<!-- Decorative: Empty alt text -->
<img src="decorative-line.svg" alt="" aria-hidden="true" />

<!-- Icon button: Use alt or aria-label -->
<button>
  <img src="search-icon.svg" alt="Search" />
</button>

<!-- Complex image: Provide summary and link to details -->
<img src="revenue-chart.svg" alt="Revenue growth chart Q1-Q4 2024, see detailed breakdown below" />
<table>
  <!-- Full data table -->
</table>

<!-- SVG icon: Use title element -->
<svg viewBox="0 0 24 24">
  <title>Calendar icon</title>
  <path d="..." />
</svg>
```

### Icon-Only Buttons Must Have aria-label

Never create a button with only an icon and no text. Provide an accessible name:

```html
<!-- Bad: Icon only, no accessible name -->
<button>
  <svg><!-- Trash icon --></svg>
</button>

<!-- Good: aria-label -->
<button aria-label="Delete item">
  <svg aria-hidden="true"><!-- Trash icon --></svg>
</button>

<!-- Good: Text + icon -->
<button>
  <svg aria-hidden="true"><!-- Trash icon --></svg>
  Delete
</button>

<!-- Good: Title attribute (fallback) -->
<button title="Delete">
  <svg><!-- Trash icon --></svg>
</button>
```

### Complex Images Need Text Descriptions

For charts, infographics, and complex diagrams, provide:
1. Brief alt text (< 150 characters)
2. Longer text description (below or linked)
3. Data table (for charts)

```html
<!-- Chart example -->
<figure>
  <img src="sales-chart.svg" alt="Q1 sales by region: North $500K, South $400K, East $350K, West $450K" />
  <figcaption>
    Quarterly sales data shows North region leading at $500K, followed by West at $450K.
    Complete breakdown available in the table below.
  </figcaption>
</figure>

<table>
  <thead>
    <tr>
      <th>Region</th>
      <th>Sales</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>North</td>
      <td>$500,000</td>
    </tr>
    <!-- More rows -->
  </tbody>
</table>
```

---

## Motion & Animation

Some people experience motion sickness, vertigo, or seizures when exposed to rapid motion or flashing content. Always respect user preferences.

### The prefers-reduced-motion Media Query

Users can set a system preference to reduce motion. Always respect this:

```css
/* Default: Animation is fine */
.button {
  transition: background-color 0.3s ease;
}

/* User has selected "reduce motion" */
@media (prefers-reduced-motion: reduce) {
  .button {
    transition: background-color 0.01s ease;  /* Nearly instant, no motion */
  }
}

/* Better: Disable animation entirely */
@media (prefers-reduced-motion: reduce) {
  *,
  *::before,
  *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
  }
}
```

### No Content Flashing > 3 Times Per Second

Content that flashes more than 3 times per second can trigger seizures. This is rare, but critical:

```css
/* Bad: Flashes 5 times per second - FAILS */
@keyframes rapid-flash {
  0%, 100% { opacity: 1; }
  50% { opacity: 0; }
}

.alert {
  animation: rapid-flash 0.2s infinite;  /* 5 flashes/sec */
}

/* Good: Slower animation */
@keyframes gentle-pulse {
  0%, 100% { opacity: 1; }
  50% { opacity: 0.7; }
}

.pulse {
  animation: gentle-pulse 1s infinite;  /* Once per second */
}

/* Good: Respect motion preferences */
@media (prefers-reduced-motion: reduce) {
  .pulse {
    animation: none;
  }
}
```

---

## Keyboard Navigation

Keyboard-only users and people using switch control or voice activation depend on keyboard navigation. All functionality must be accessible via keyboard.

### All Functionality Must Be Keyboard Accessible

Every action the mouse can do, the keyboard must be able to do:

```html
<!-- Good: Button is keyboard accessible by default -->
<button>Click me</button>

<!-- Bad: DIV is NOT keyboard accessible -->
<div onclick="handleClick()">Click me</div>

<!-- Bad: Link without href is not keyboard accessible -->
<a onclick="handleClick()">Click me</a>

<!-- Good: Use semantic HTML, add event listeners if needed -->
<button onclick="handleClick()">Click me</button>

<!-- Good: Keyboard handlers for special cases -->
<div role="button" tabindex="0" onkeydown="if (event.key === 'Enter') handleClick()">
  Click me
</div>
```

### Logical Tab Order

The Tab key should move focus in a logical order (usually left-to-right, top-to-bottom). Respect the DOM order:

```html
<!-- Good: DOM order matches visual order -->
<form>
  <label>First Name: <input type="text" /></label>
  <label>Last Name: <input type="text" /></label>
  <button>Submit</button>
</form>

<!-- Bad: Visual order doesn't match DOM order -->
<form>
  <input type="text" style="order: 2;" placeholder="Last name" />
  <input type="text" style="order: 1;" placeholder="First name" />
  <!-- Tab order will be backwards from visual order -->
</form>

/* Avoid using tabindex */
input {
  tabindex: 0;  /* Default, follows DOM order */
}

input {
  tabindex: 1;  /* Jumps ahead - confusing */
}

/* Only use tabindex="0" to make non-interactive elements focusable */
div {
  tabindex: 0;  /* Makes a div keyboard focusable */
  role: button;
}
```

### No Keyboard Traps

Users should always be able to Tab out of a component. A keyboard trap leaves users stuck.

```html
<!-- Bad: Modal without escape key -->
<div role="dialog" modal>
  <input type="text" />
  <button>Submit</button>
  <!-- User tabs but can't escape without a close button -->
</div>

<!-- Good: Modal with proper exit -->
<div role="dialog" aria-modal="true" aria-labelledby="title">
  <h2 id="title">Confirm Action</h2>
  <p>Are you sure?</p>
  <button>Cancel</button>
  <button>Confirm</button>
</div>

<script>
  dialog.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') {
      dialog.close();
    }
  });
</script>
```

### Skip Navigation Links

Large websites with header navigation should provide a "Skip to main content" link:

```html
<body>
  <!-- Skip link (hidden until focused) -->
  <a href="#main-content" class="skip-link">Skip to main content</a>

  <header>
    <nav>
      <!-- Navigation items -->
    </nav>
  </header>

  <main id="main-content">
    <!-- Main content -->
  </main>
</body>

<style>
  .skip-link {
    position: absolute;
    top: -40px;
    left: 0;
    background: #000;
    color: #fff;
    padding: 8px;
    text-decoration: none;
  }

  .skip-link:focus {
    top: 0;  /* Appears when focused */
  }
</style>
```

---

## Screen Reader Support

Screen readers convert digital text into speech or braille. They rely on semantic HTML and proper markup to understand page structure.

### Semantic HTML First

Always use semantic HTML. It has built-in accessibility:

```html
<!-- Good: Semantic HTML -->
<header><!-- Page header --></header>
<nav><!-- Navigation --></nav>
<main><!-- Main content --></main>
<article><!-- Article --></article>
<section><!-- Section --></section>
<aside><!-- Sidebar --></aside>
<footer><!-- Footer --></footer>

<button>Click me</button>
<a href="/page">Link</a>
<input type="text" />
<label for="email">Email</label>

<!-- Bad: Non-semantic HTML -->
<div class="header"><!-- Not identified as header --></div>
<div class="nav"><!-- Not identified as navigation --></div>
<div class="button" onclick="...">Click me</div>
<span class="link" onclick="...">Link</span>
```

### ARIA Roles (Only When Semantic HTML Insufficient)

Use ARIA (Accessible Rich Internet Applications) attributes only when semantic HTML can't express the meaning:

```html
<!-- Good: No ARIA needed, use semantic HTML -->
<button>Delete</button>

<!-- Bad: DIV pretending to be button -->
<div onclick="delete()">Delete</div>

<!-- Acceptable: DIV as button with ARIA (if semantic HTML can't be used) -->
<div role="button" tabindex="0" onclick="delete()">Delete</div>

<!-- Good: Tab panel with ARIA -->
<div role="tablist">
  <button role="tab" aria-selected="true" aria-controls="panel-1">Tab 1</button>
  <button role="tab" aria-selected="false" aria-controls="panel-2">Tab 2</button>
  <div role="tabpanel" id="panel-1">Content 1</div>
  <div role="tabpanel" id="panel-2">Content 2</div>
</div>

<!-- Good: Describing a relationship -->
<input type="text" id="search" aria-describedby="search-help" />
<span id="search-help">Search by product name or ID</span>

<!-- Good: Marking content as important -->
<div role="alert">Your session expires in 5 minutes</div>
```

### Live Regions for Dynamic Content

Use `aria-live` to announce content changes to screen reader users:

```html
<!-- Announce when content updates (polite) -->
<div aria-live="polite" aria-atomic="true" id="status">
  Ready
</div>

<button onclick="updateStatus()">Process</button>

<script>
  function updateStatus() {
    document.getElementById('status').textContent = 'Processing...';
    // Screen reader announces: "Processing..."
  }
</script>

<!-- Urgent announcement (assertive) -->
<div aria-live="assertive" role="alert">
  Error: Connection lost
</div>

<!-- Busy state -->
<div aria-busy="true">
  Loading data...
</div>
```

### Heading Hierarchy (h1 → h2 → h3)

Screen readers use headings to create an outline of the page. Structure them logically:

```html
<!-- Good: Proper hierarchy -->
<h1>Product Reviews</h1>
<p>Top-rated products this month...</p>

<h2>Electronics</h2>
<h3>Smartphones</h3>
<p>Best smartphones...</p>

<h3>Laptops</h3>
<p>Best laptops...</p>

<h2>Home & Garden</h2>
<h3>Kitchen Tools</h3>
<p>Best kitchen tools...</p>

<!-- Bad: Skipping levels -->
<h1>Product Reviews</h1>
<h3>Smartphones</h3>  <!-- Should be h2 or h3 under h2 -->
<h5>Best deals</h5>  <!-- Should be h4 or h3 -->

<!-- Bad: Multiple h1 elements -->
<h1>Main Heading</h1>
<h1>Another Heading</h1>  <!-- Use only one h1 per page -->
```

---

## RTL/Arabic Specific Accessibility

If your product supports Arabic or other right-to-left (RTL) languages, additional considerations apply.

### Set Direction with dir Attribute

```html
<!-- Arabic content -->
<html dir="rtl" lang="ar">
  <body>
    <header><!-- Appears on right side --></header>
    <main><!-- Content flows right-to-left --></main>
  </body>
</html>

<!-- English content on RTL site -->
<p dir="ltr">This is English text (left-to-right).</p>

<!-- Mixed content -->
<p>
  أهلا وسهلا
  <span dir="ltr">Hello</span>
  مرحبا
</p>
```

### Language Attribute

```html
<html lang="ar"><!-- Arabic site -->
<html lang="en"><!-- English site -->
<html lang="en-US"><!-- English (US) -->

<!-- Mix languages on page -->
<p lang="ar">النص بالعربية</p>
<p lang="en">Text in English</p>
```

### Use Logical Properties Instead of Directional

Use logical properties that automatically flip for RTL:

```css
/* Good: Works for both LTR and RTL */
.card {
  margin-inline-start: 16px;   /* Left margin in LTR, right margin in RTL */
  margin-inline-end: 16px;
  padding-inline: 16px;         /* Padding left/right auto-flips */
  border-inline-start: 4px;     /* Left border in LTR, right border in RTL */
}

/* Bad: Only works for LTR */
.card {
  margin-left: 16px;            /* Wrong side in RTL */
  padding-left: 16px;
  border-left: 4px;
}

/* Flexbox - automatically flips in RTL */
.flex-row {
  display: flex;
  flex-direction: row;  /* Automatically right-to-left in RTL */
}

/* Grid - automatically flips in RTL */
.grid {
  display: grid;
  grid-template-columns: 1fr 1fr;  /* Auto-flips order in RTL */
}
```

---

## Per-Screen Accessibility Checklist

Run this checklist before completing each screen design:

### Typography & Color
- [ ] Body text is at least 16px (minimum 12px)
- [ ] Line height is at least 1.5x font size
- [ ] All text has minimum 4.5:1 contrast on white (3:1 for large text)
- [ ] Placeholder text has 4.5:1 contrast, or is darker than default gray
- [ ] Text is left-aligned (not justified)

### Interactive Elements
- [ ] All buttons are at least 44×44px
- [ ] All clickable elements have at least 8px spacing between them
- [ ] All buttons/links have visible focus indicator (minimum 3px, 3:1 contrast)
- [ ] All interactive elements are keyboard accessible (Tab, Enter, Escape)
- [ ] Tab order is logical (top-to-bottom, left-to-right)
- [ ] No keyboard traps (user can Tab out of everything)

### Forms
- [ ] Every input has a visible label (not just placeholder)
- [ ] Required fields are marked with text AND asterisk
- [ ] Error messages use text + icon + color
- [ ] Inputs have autocomplete attributes where relevant
- [ ] All form instructions are visible (not hidden until interaction)

### Images & Icons
- [ ] All informative images have alt text
- [ ] Decorative images have empty alt text (alt="")
- [ ] Icon-only buttons have aria-label or visible text
- [ ] Charts/complex images have text description or data table

### Content & Structure
- [ ] Page has exactly one h1 heading
- [ ] Heading hierarchy is logical (h1 → h2 → h3, no skipping)
- [ ] Important content is in a `<main>` element
- [ ] Color alone is never used to convey information
- [ ] Color blindness doesn't break functionality (use icons, text, patterns too)

### Motion
- [ ] No content flashes more than 3 times per second
- [ ] Animations respect prefers-reduced-motion
- [ ] Motion is not essential to understanding content

### Responsiveness
- [ ] Text is resizable to 200% without loss of functionality
- [ ] Layout doesn't break at any zoom level
- [ ] Touch targets remain 44×44px on mobile
- [ ] No horizontal scrolling required on mobile

### RTL Support (if applicable)
- [ ] RTL language uses `dir="rtl"` and `lang="ar"`
- [ ] CSS uses logical properties (margin-inline, not margin-left)
- [ ] Flexbox/Grid automatically adjusts for RTL
- [ ] No hardcoded left/right positioning

---

## Automated Testing Tools

Automated tools catch about 30% of accessibility issues. Always do manual testing too.

| Tool | Purpose | Free/Paid | Best For |
|------|---------|-----------|----------|
| **Axe DevTools** | WCAG scanning in browser | Free | Comprehensive automated testing |
| **Lighthouse (Chrome)** | Built into DevTools | Free | Quick accessibility audit |
| **WAVE (WebAIM)** | Visual accessibility feedback | Free extension | Visual feedback on issues |
| **Color Contrast Analyser** | Contrast checking | Free app | Precise contrast ratio checking |
| **Stark** | Figma plugin for contrast | Free/Paid | Design-time checking |
| **NVDA** | Free screen reader | Free | Windows screen reader testing |
| **JAWS** | Commercial screen reader | Paid | Industry standard, Windows |
| **VoiceOver** | Built into Mac/iOS | Free | macOS/iOS screen reader |
| **Keyboard-only testing** | Manual keyboard navigation | Free | Ensure keyboard access |
| **Mobile accessibility** | Test on real devices | Free | Touch target and zoom testing |

### Running Axe DevTools

```javascript
// Open Chrome DevTools
// Open "Axe DevTools" tab
// Click "Scan ALL of my page"
// Review issues by severity (Critical > Serious > Moderate > Minor)
// Fix issues, then rescan
```

### Running Lighthouse

```
1. Open Chrome DevTools (F12)
2. Click "Lighthouse" tab
3. Select "Accessibility" category
4. Click "Analyze page load"
5. Review results and fix issues
```

---

## WCAG 2.1 AA Quick Reference Table

| Success Criterion | Level | Requirement | Common Failures |
|------------------|-------|-------------|-----------------|
| **1.4.3 Contrast (Minimum)** | AA | 4.5:1 for normal text, 3:1 for large text | Gray text on white, low color contrast |
| **1.4.4 Resize Text** | AA | Text resizable to 200% without loss of function | Fixed widths, overflow: hidden |
| **1.4.5 Images of Text** | AA | Use real text instead of text in images | Unreadable text in graphics |
| **2.1.1 Keyboard** | A | All functionality keyboard accessible | No keyboard alternative to mouse |
| **2.1.2 No Keyboard Trap** | A | Keyboard focus not trapped | Can't Tab out of component |
| **2.4.3 Focus Order** | A | Logical focus order | Tab order doesn't match visual order |
| **2.4.7 Focus Visible** | AA | Visible focus indicator on all elements | Outline: none without replacement |
| **3.2.1 On Focus** | A | No unexpected context changes on focus | Page changes when element receives focus |
| **3.2.2 On Input** | A | No unexpected changes on input | Form auto-submits on selection |
| **3.3.1 Error Identification** | A | Errors identified and described to user | Only red border, no text message |
| **3.3.2 Labels or Instructions** | A | Labels and instructions provided | Input with only placeholder text |
| **3.3.3 Error Suggestion** | AA | Suggestions provided for errors | Error message but no fix suggestion |
| **3.3.4 Error Prevention** | AA | Confirmation for legal/financial actions | No undo option |
| **1.1.1 Non-text Content** | A | Alt text for images | Missing alt text |
| **1.3.1 Info and Relationships** | A | Semantic markup for structure | DIV used instead of BUTTON |
| **1.3.4 Orientation** | AA | Content works in portrait and landscape | Content locked to orientation |
| **1.3.5 Identify Input Purpose** | AA | Autocomplete attributes for inputs | No autocomplete on email field |
| **2.2.2 Pause, Stop, Hide** | A | User can stop moving/scrolling content | Auto-playing carousel no pause |
| **2.3.3 Animation from Interactions** | AAA | Option to disable animation from interactions | Can't disable animation |
| **2.5.5 Target Size (Enhanced)** | AAA | 44px target size (44×44 minimum) | 32px button |
| **2.5.2 Pointer Cancellation** | A | Users can undo pointer actions | No undo for swipe action |
| **4.1.2 Name, Role, Value** | A | Components have accessible name, role, value | Custom button without role attribute |
| **4.1.3 Status Messages** | AA | Status messages announced without focus change | Error message not announced |

---

## References & Further Learning

- **WCAG 2.1 Official Specification**: w3.org/WAI/WCAG21/quickref/
- **WebAIM Articles**: webaim.org/ (excellent practical guides)
- **W3C WAI (Web Accessibility Initiative)**: w3.org/WAI/
- **Inclusive Components**: inclusivecomponents.design/ (pattern library)
- **The A11y Project**: a11yproject.com/ (community resource)
- **ARIA Authoring Practices Guide**: w3.org/WAI/ARIA/apg/

---

**Last Updated**: 2026-03-28
**WCAG Version**: 2.1 Level AA
**Target Audience**: UX/UI Designers implementing HTML/CSS

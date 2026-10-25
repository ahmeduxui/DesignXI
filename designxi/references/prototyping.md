# Prototyping in DesignXI

## Core Principle: A Prototype Answers One Question Cheaply

Every prototype must have a **clear question it's answering**. If you don't know what question you're testing, you don't need a prototype yet.

Reference: Bill Buxton's "Sketching User Experiences" — *sketches are cheap, production code is expensive*. The purpose of a prototype is to move from expensive certainty to cheap uncertainty.

---

## The Fidelity Spectrum

Match fidelity to the question being asked. Never over-prototype.

### Lo-Fi: Paper Sketches & Text Wireframes
- **Purpose**: Answer questions about structure and flow
- **Cost**: Hours
- **Question type**: "Does the user understand where to go next?" "Is the hierarchy clear?"
- **Tools**: Paper, whiteboard, text documents
- **What you'll learn**: navigation clarity, content priority, flow logic

### Mid-Fi: Greyscale HTML Wireframes
- **Purpose**: Answer questions about content and hierarchy
- **Cost**: Half a day to one day
- **Question type**: "Does the information architecture work?" "Is there enough space for real copy?"
- **Tools**: HTML with greyscale palette, real copy
- **What you'll learn**: whether the structure supports actual content, spacing decisions

### Hi-Fi: Branded Interactive HTML
- **Purpose**: Answer questions about look/feel and interaction quality
- **Cost**: 2-3 days (depending on design system maturity)
- **Question type**: "Does this feel right?" "Is the interaction smooth?" "Will users trust this?"
- **Tools**: HTML with full design system applied
- **What you'll learn**: visual clarity, emotional response, interaction polish

---

## What to Prototype (Priority Order)

1. **Core user flow** — The path that delivers the product's main value. Always prototype this first.
2. **Onboarding** — First-time user experience. Most critical because it determines if users even get to the core flow.
3. **The most complex interaction** — The interaction most likely to confuse users.
4. **Edge cases where users fail** — Empty states, errors, edge conditions.
5. **NOT every screen** — Don't prototype flows that are self-explanatory or are one-off flows.
6. **NOT every error state** — Only prototype errors where users might not understand recovery.
7. **NOT admin flows** — Unless admin users are your primary audience.

---

## Lo-Fi Prototyping: Text-Based Wireframes

### The Format

Use this text wireframe format in DesignXI (Phase 4, before visual design):

```
SCREEN: [Name]
Purpose: [What question does this screen answer?]
Layout:
  - Header: [Content, navigation, back button if needed]
  - Primary content: [Key components and their hierarchy]
  - Primary action: [Button/CTA — the main thing the user does here]
  - Secondary: [Supporting elements, secondary actions]
Connects to: [Next screen on action]
Test question: [What are we trying to learn? What could go wrong here?]
```

### Example: Onboarding Screen

```
SCREEN: Welcome
Purpose: Does the user understand what this app does in 10 seconds?
Layout:
  - Header: App logo, no navigation
  - Primary content:
    * Hero image (50% of viewport)
    * Headline: "Sell faster with [App Name]"
    * Subheadline: "Connect your inventory, reach more buyers"
    * Feature list (3 bullets, each with icon):
      - Real-time sync
      - Multi-channel listings
      - Built-in analytics
  - Primary action: "Start Free Trial" (prominent, full-width button)
  - Secondary: "Sign In" link below
Connects to: Sign up flow on "Start Free Trial" → Account creation → Dashboard
Test question: Does the value proposition land? Do users know what to do next?
```

### When to Use
- Phase 4: Before any visual design work
- When exploring multiple flow options
- When stakeholders need to agree on structure before design investment
- To test navigation logic with real users (on paper or as a clickable text prototype)

### What to Test
- Navigation clarity: Can users find what they need?
- Content priority: Are the important things prominent?
- Flow logic: Does the order make sense?

---

## Mid-Fi Prototyping: Greyscale HTML

### The Approach
- Use **real copy** and **real structure** — but no brand colors or images
- Focus on layout, hierarchy, content, spacing
- Test whether the information architecture makes sense with actual content

### Greyscale Palette
Use these colors for mid-fi prototypes:
- Background: `#F9FAFB`
- Surface/Cards: `#FFFFFF`
- Light dividers: `#E5E7EB`
- Medium text: `#9CA3AF`
- Dark text: `#374151`
- Darkest (headings): `#111827`

### Example: Mid-Fi Dashboard Screen

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Dashboard - Mid-Fi</title>
  <style>
    * { margin: 0; padding: 0; box-sizing: border-box; }
    body {
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
      background: #F9FAFB;
      color: #374151;
      line-height: 1.6;
    }
    .container { max-width: 1200px; margin: 0 auto; padding: 24px; }
    header {
      background: #FFFFFF;
      border-bottom: 1px solid #E5E7EB;
      padding: 16px 24px;
      margin-bottom: 24px;
    }
    header h1 { color: #111827; font-size: 24px; }
    .grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 24px; }
    .card {
      background: #FFFFFF;
      border: 1px solid #E5E7EB;
      border-radius: 8px;
      padding: 24px;
    }
    .card h2 { color: #111827; font-size: 14px; font-weight: 600; margin-bottom: 12px; }
    .metric { color: #111827; font-size: 32px; font-weight: 700; margin-bottom: 8px; }
    .change { color: #9CA3AF; font-size: 12px; }
    button {
      background: #374151;
      color: #FFFFFF;
      border: none;
      padding: 12px 16px;
      border-radius: 6px;
      font-size: 14px;
      cursor: pointer;
    }
    button:hover { background: #1F2937; }
  </style>
</head>
<body>
  <header>
    <h1>Dashboard</h1>
  </header>
  <div class="container">
    <div class="grid">
      <div class="card">
        <h2>Total Sales</h2>
        <div class="metric">$12,450</div>
        <div class="change">+12% vs last month</div>
      </div>
      <div class="card">
        <h2>Active Listings</h2>
        <div class="metric">847</div>
        <div class="change">No change</div>
      </div>
      <div class="card">
        <h2>Messages</h2>
        <div class="metric">23</div>
        <div class="change">3 unread</div>
      </div>
    </div>
    <div style="margin-top: 24px;">
      <button onclick="alert('View details')">View Full Report</button>
    </div>
  </div>
</body>
</html>
```

### When to Use
- Before brand identity is finalized
- When you need to test with real content before designing visuals
- To validate information architecture with actual text length
- When working with developers who need HTML structure early

### What to Test
- Does the layout accommodate real copy without breaking?
- Is the hierarchy clear without color or imagery?
- Do users understand the content structure?

---

## Hi-Fi Prototyping: Branded Interactive HTML

### The Approach
- Full design system applied: colors, typography, spacing, components
- Real content throughout
- All interactive states: hover, active, focus, error, empty, loading
- Navigation between screens (see section below)

### When to Use
- Phase 5 and 6: After brand is confirmed and design system is established
- When testing visual clarity and emotional response
- Before usability testing (Phase 6.5)

### What to Test
- Does the visual design communicate trust and professionalism?
- Are interactive states clear (hover, focus, error)?
- Is the experience smooth and polished?
- Do users feel the intended emotion?

### State Coverage Checklist
For every interactive element:
- `default` — initial state
- `hover` — mouse over (desktop)
- `active` / `pressed` — during interaction
- `focus` — keyboard navigation
- `disabled` — unavailable state
- For forms: `error` state with inline error message
- For content: `empty` state (no data), `loading` state (spinner/skeleton)

---

## Interactive HTML Prototyping: Navigation

Since DesignXI delivers HTML files, make screens navigable. Here's the pattern:

### Basic Navigation Pattern

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Interactive Prototype</title>
  <style>
    .screen { display: none; }
    .screen.active { display: block; }

    /* Optional: add transitions */
    .screen { opacity: 0; transition: opacity 0.2s ease; }
    .screen.active { opacity: 1; }

    body { font-family: sans-serif; }
  </style>
</head>
<body>

  <!-- Screen 1: Home -->
  <div id="screen-home" class="screen active">
    <h1>Welcome to Our App</h1>
    <button onclick="navigate('screen-dashboard')">Get Started</button>
  </div>

  <!-- Screen 2: Dashboard -->
  <div id="screen-dashboard" class="screen">
    <h1>Dashboard</h1>
    <p>You have 5 new messages</p>
    <button onclick="navigate('screen-messages')">View Messages</button>
    <button onclick="navigate('screen-home')">← Back</button>
  </div>

  <!-- Screen 3: Messages -->
  <div id="screen-messages" class="screen">
    <h1>Messages</h1>
    <p>Your messages appear here</p>
    <button onclick="navigate('screen-dashboard')">← Back</button>
  </div>

  <script>
    function navigate(screenId) {
      // Hide all screens
      document.querySelectorAll('.screen').forEach(screen => {
        screen.classList.remove('active');
      });

      // Show target screen
      document.getElementById(screenId).classList.add('active');

      // Optional: scroll to top
      window.scrollTo(0, 0);
    }
  </script>

</body>
</html>
```

### Navigation Best Practices
- **Always provide explicit back navigation** — Never trap the user
- **Use descriptive screen IDs** — `screen-onboarding`, not `screen-1`
- **Add scroll-to-top** on navigation for mobile (see code above)
- **Optional: add transitions** — Fade (0.2s) or slide effects make navigation feel intentional
- **Keep navigation visible** — Don't hide back buttons in hamburger menus for prototypes

### Advanced: Modal/Overlay Pattern

```html
<!-- Button that triggers modal -->
<button onclick="openModal('modal-delete-confirmation')">Delete Item</button>

<!-- Modal overlay -->
<div id="modal-delete-confirmation" class="modal" style="display: none;">
  <div class="modal-overlay" onclick="closeModal('modal-delete-confirmation')"></div>
  <div class="modal-content">
    <h2>Delete this item?</h2>
    <p>This action cannot be undone.</p>
    <button onclick="navigate('screen-dashboard'); closeModal('modal-delete-confirmation');">
      Confirm Delete
    </button>
    <button onclick="closeModal('modal-delete-confirmation');">Cancel</button>
  </div>
</div>

<script>
  function openModal(modalId) {
    document.getElementById(modalId).style.display = 'flex';
  }
  function closeModal(modalId) {
    document.getElementById(modalId).style.display = 'none';
  }
</script>

<style>
  .modal {
    display: none;
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    align-items: center;
    justify-content: center;
    z-index: 1000;
  }
  .modal-overlay {
    position: absolute;
    width: 100%;
    height: 100%;
    background: rgba(0, 0, 0, 0.5);
  }
  .modal-content {
    position: relative;
    background: white;
    padding: 24px;
    border-radius: 8px;
    max-width: 500px;
    z-index: 1001;
  }
</style>
```

---

## Prototype Flows to Always Include

Every prototype must include these user journeys:

### 1. Happy Path
The user completes the primary goal with no errors or obstacles.
- Example: Sign up → Create account → See dashboard with data
- This is the main value delivery moment

### 2. Error Path
The user makes a mistake (wrong password, missing field, invalid input).
- Show the error state
- Show how to recover (clear error message, example of valid input)
- Example: Click "Sign up" with mismatched passwords → Error message → User corrects → Success

### 3. Empty State Path
First-time user with no data to display.
- Don't show an empty grid
- Show what content looks like, with placeholder or example data
- Provide a clear call-to-action to create first item
- Example: First time in dashboard → "You have no listings yet. Create your first listing."

### 4. Onboarding Path
From landing page → first value moment.
- This is your most important flow
- Every screen must have a clear next step
- Minimize friction (form fields, reading, decisions)

---

## Annotation Standards

Each screen needs clear interaction annotations so developers and testers understand behavior.

### Format
`[Element] → [Action] → [Result]`

### Example Annotations

```
"Save" button → tap/click → Shows green success toast ("Changes saved")
                           → Toast disappears after 2s
                           → Page refreshes with updated data

Form input (email) → user enters invalid email → Shows inline red error
                     "Please enter a valid email" below field
                     → Clears on correction

"Back" button → tap → Transitions to previous screen with fade (0.2s)
                    → Scroll position resets to top

Checkbox → checked → Adds checkmark, background becomes light blue
        → unchecked → Checkmark disappears, background returns to white

Submit button → hover → Background darkens, cursor becomes pointer
             → click → Button becomes disabled with loading spinner
                     → After 1.5s loading: navigates to success screen
             → error state (if submission fails) → Shows error message inline
```

### Annotation Checklist
- Duration of animations (e.g., "fade 0.2s", "slide 400ms")
- Duration of ephemeral messages (e.g., "toast persists 2s", "tooltip disappears on blur")
- Conditions (e.g., "if field empty, show inline error", "if API slow, show skeleton")
- Timing of state changes (e.g., "submit → immediately disable button → show spinner")

---

## Prototype Review Checklist

Before moving to usability testing, verify:

- [ ] Every screen has a clear purpose (what question does it answer?)
- [ ] Every button leads somewhere (no dead-end buttons)
- [ ] Error states are designed (invalid form, network error, etc.)
- [ ] Empty states are designed (first-time user with no data)
- [ ] Loading states are indicated (spinners, skeletons, disabled buttons)
- [ ] Success states are clear (confirmations, toasts, visual feedback)
- [ ] Back navigation always works (no trapped states)
- [ ] The core user flow can be completed without assistance
- [ ] All text is real copy (no "Lorem ipsum")
- [ ] All interactive elements are keyboard-accessible (tab navigation works)
- [ ] Hover states exist for all clickable elements
- [ ] Focus states are visible for keyboard users (blue outline or indicator)

---

## Prototyping for Arabic / RTL

RTL is not an afterthought — it must be tested in the prototype from the start.

### RTL Layout Toggle

Add a language toggle to test both directions:

```html
<button onclick="toggleDirection()">العربية | English</button>

<script>
  function toggleDirection() {
    const html = document.documentElement;
    const currentDir = html.getAttribute('dir') || 'ltr';
    const newDir = currentDir === 'ltr' ? 'rtl' : 'ltr';
    html.setAttribute('dir', newDir);

    // Update language attribute
    html.setAttribute('lang', newDir === 'rtl' ? 'ar' : 'en');
  }
</script>

<style>
  [dir="rtl"] {
    direction: rtl;
  }
  [dir="rtl"] body {
    text-align: right;
  }
</style>
```

### RTL Considerations in Prototype
- **Swipe gestures mirror** — Swipe-right-to-go-back becomes swipe-left in RTL
- **Form field order** — Labels and inputs read right-to-left
- **Progress indicators** — Visual flow (step 1 → 2 → 3) may still read left-to-right, but the concept must remain clear in RTL context
- **Icons** — Some icons (arrows, back button) should flip in RTL; others (settings, gear) should not
- **Test with real Arabic copy** — Character widths and text flow differ significantly from English

### RTL Example Structure

```html
<!DOCTYPE html>
<html lang="en" dir="ltr">
<head>
  <meta charset="UTF-8">
  <style>
    body {
      font-family: Arial, sans-serif; /* Arabic-safe font */
    }
    [dir="rtl"] {
      direction: rtl;
      text-align: right;
    }
    [dir="rtl"] .back-button::before {
      content: "←";
      transform: scaleX(-1);
    }
  </style>
</head>
<body>
  <button onclick="toggleDir()">Toggle RTL</button>

  <input type="text" placeholder="Name">
  <!-- In RTL, this input aligns right and placeholder appears right-aligned -->

  <script>
    function toggleDir() {
      const dir = document.documentElement.dir === 'rtl' ? 'ltr' : 'rtl';
      document.documentElement.dir = dir;
      document.documentElement.lang = dir === 'rtl' ? 'ar' : 'en';
    }
  </script>
</body>
</html>
```

---

## From Prototype to Delivery

In DesignXI, the prototype IS the deliverable.

### Phase 5-6: Build `screens.html`
- Clickable prototype with all screens
- Full design system applied
- All states and flows included
- Real content throughout
- Tested for usability

### Phase 6.5: Usability Testing
- Share `screens.html` with users
- Observe their behavior
- Note which screens confuse them, which flows they expect, where they tap

### Post-Testing: Fix Critical Issues
- Make fixes directly in the HTML
- Don't redesign — iterate based on what broke
- Update the same `screens.html` file
- Re-test key flows

### Final Delivery
- `screens.html` = prototype + tested design + user feedback incorporated
- This is Phase 6's HTML deliverable
- Developers use this as the reference for implementation

### Documentation in `screens.html`
Include a comment block at the top of the file:

```html
<!--
  PROJECT: [Project Name]
  PHASE: 6 - Interactive Prototype

  FLOWS TESTED:
  ✓ Onboarding (landing → dashboard)
  ✓ Core user flow (dashboard → create item → success)
  ✓ Error handling (invalid input → error state → recovery)
  ✓ Empty state (first-time user with no data)

  SCREENS INCLUDED:
  1. Welcome
  2. Sign Up
  3. Verification
  4. Dashboard
  5. Create Item
  6. Success

  NAVIGATION: Click buttons or use back navigation
  RTL: Click "العربية | English" to toggle

  LAST TESTED: [Date]
  FINDINGS: [Key insights from usability testing]
  NEXT STEPS: [What to build first]
-->
```

---

## Summary: Prototype, Don't Goldplate

- **Start with a question.** If you don't know what you're testing, you don't need a prototype.
- **Match fidelity to the question.** Text wireframes for flow, greyscale for hierarchy, hi-fi for feel.
- **Prototype the risky parts.** Core flow, onboarding, complex interactions — not every screen.
- **Include all paths.** Happy, error, empty, loading — users encounter all of them.
- **Make it navigable.** Even a text-based wireframe should show flow, ideally clickable.
- **Test it.** A prototype's only value is what you learn from users interacting with it.
- **The prototype is the deliverable.** In DesignXI, `screens.html` is Phase 6 — iterate based on testing, then handoff.


# Mobile Gestures, Thumb Zones, and Mobile UX Patterns

## Why Mobile Design Requires Different Thinking

Mobile is not a small desktop. The fundamental constraints differ:

- **Touch vs. Pointer**: Fingers are imprecise (average touch target area is 10×10mm), and finger occlusion hides content during interaction. Hover states don't exist.
- **One-handed use**: Most users hold phones in one hand and interact with their thumb. The reachable area is limited and asymmetrical.
- **Context & attention**: Users are distracted, in transit, or in limited-light environments. Interactions must be fast and forgiving.
- **Posture**: Users tilt, recline, or alternate hands. The interface must adapt.
- **Network & performance**: Mobile networks are slower and less reliable. Every interaction should feel responsive.
- **Screen real estate**: Vertical space is precious. Horizontal space is even more constrained.

**Design principle**: Optimize for thumb-based one-handed interaction first. Everything else is a bonus.

---

## The Thumb Zone (Steven Hoober's Research)

Steven Hoober's research on mobile grip and interaction revealed where users naturally reach on a phone held in one hand:

```
┌──────────────────────────────┐
│    STRETCH ZONE              │  ← Top corners: requires reaching
│  ↗ Hard to reach ↖            │
│    Hard to reach             │
│                              │
│     AWKWARD ZONE             │  ← Top-center: dead zone
│  (requires repositioning)    │
│                              │
│                              │
│     COMFORT ZONE             │  ← Bottom half: natural thumb reach
│  [  EASY REACH  ]            │  ← "The Thumb Zone"
│  (natural thumb position)    │
└──────────────────────────────┘
```

### Thumb Zone Breakdown:

- **Easy Reach (bottom 40%)**: Effortless to tap. Primary actions belong here. Natural thumb position for right-handed users swiping from bottom-left.
- **Comfort Zone (middle 30%)**: Reachable but requires slight finger stretch or subtle grip adjustment.
- **Awkward Zone (top-center 30%)**: Requires repositioning the phone or switching hands. Avoid important interactions here.
- **Stretch Zone (top corners)**: Possible but awkward. Reserve for rarely-used actions or secondary navigation.

### Design Implications:

1. **Primary actions go in the easy reach zone** (bottom 40% of screen)
2. **Navigation patterns respect this**:
   - Bottom tab bar (easy reach) > Hamburger menu (stretch zone) > Top navigation (awkward)
3. **Confirm destructive actions with a second tap in easy reach**
4. **Never bury critical actions behind hamburger menus on small screens**

---

## Bottom Navigation Pattern

Bottom navigation is the gold standard for mobile navigation because it sits in the easy reach zone.

### Best Practices:

- **Ideal for**: 3–5 primary destinations
- **Never use**: more than 5 tabs (use hamburger menu for additional items)
- **Height**: 56px (Android Material minimum) to 64px (iOS)
- **Labels**: Always pair icons with text labels for primary navigation
- **Never**: Icon-only navigation for primary destinations (accessibility + clarity)
- **Placement**: Fixed to the bottom of the screen
- **Active state**: Color change + optional indicator line/dot beneath the icon
- **Scrollable content**: Bottom nav stays fixed; content scrolls above it

### CSS Implementation:

```css
/* Bottom navigation container */
.bottom-nav {
  position: fixed;
  bottom: 0;
  left: 0;
  right: 0;
  height: 56px;
  background: #fff;
  border-top: 1px solid #e0e0e0;
  display: flex;
  justify-content: space-around;
  align-items: center;
  z-index: 100;
}

/* Account for bottom nav in main content */
body {
  padding-bottom: 56px;
}

/* Tab item */
.nav-item {
  flex: 1;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 4px;
  padding: 8px;
  color: #666;
  text-decoration: none;
  font-size: 12px;
  transition: color 200ms;
}

.nav-item:active,
.nav-item.active {
  color: #1976d2;
}

.nav-item.active::after {
  content: '';
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  height: 3px;
  background: #1976d2;
}

.nav-icon {
  font-size: 24px;
}
```

HTML structure:
```html
<nav class="bottom-nav">
  <a href="/" class="nav-item active">
    <span class="nav-icon">🏠</span>
    <span>Home</span>
  </a>
  <a href="/search" class="nav-item">
    <span class="nav-icon">🔍</span>
    <span>Search</span>
  </a>
  <a href="/profile" class="nav-item">
    <span class="nav-icon">👤</span>
    <span>Profile</span>
  </a>
</nav>
```

---

## Floating Action Button (FAB)

A floating action button represents the single most important action on a screen.

### When to Use:

- One primary action per screen (compose, create, call, start)
- Not for navigation
- Not for destructive actions (delete, logout)

### Guidelines:

- **Position**: Bottom-right (LTR) / Bottom-left (RTL)
- **Size**: 56px standard, 40px mini
- **Clearance**: 16px from screen edges, 16px from bottom nav if present
- **Elevation**: 6dp shadow; 8dp when pressed
- **Never**: More than 1 FAB per screen
- **Shape**: Circular or extended (rounded rect with icon + text)

### CSS:

```css
.fab {
  position: fixed;
  bottom: 24px;              /* 16px + 8px for safety */
  right: 24px;               /* 16px + 8px for safety */
  width: 56px;
  height: 56px;
  border-radius: 50%;
  background: #1976d2;
  color: #fff;
  border: none;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 24px;
  cursor: pointer;
  box-shadow: 0 6px 12px rgba(0, 0, 0, 0.16);
  z-index: 50;
  transition: all 200ms ease;
}

.fab:active {
  box-shadow: 0 8px 16px rgba(0, 0, 0, 0.24);
  transform: scale(0.95);
}

/* With bottom nav: adjust bottom position */
.bottom-nav + .fab {
  bottom: 80px;              /* 56px nav + 24px margin */
}
```

---

## Touch Targets

Fingers are imprecise. Touch targets must be large enough to hit reliably.

### Sizing Standards:

- **Minimum**: 44×44px (iOS Human Interface Guidelines)
- **Minimum**: 48×48dp (Material Design)
- **Recommended**: 48–56px for frequently-used actions
- **Spacing**: Minimum 8px between adjacent touch targets
- **Tap feedback**: Visual response must occur within 100ms of touch

### CSS:

```css
/* Ensure all interactive elements meet minimum size */
button,
a,
input[type="checkbox"],
input[type="radio"] {
  min-width: 44px;
  min-height: 44px;
  padding: 12px;
}

/* Add padding to visual focus area if element is smaller */
a.icon-only {
  padding: 12px;            /* Total: 24px + content = 44px+ */
}

/* Touch feedback */
button,
a {
  user-select: none;
  -webkit-user-select: none;
  touch-action: manipulation;
}

button:active,
a:active {
  opacity: 0.8;
  transform: scale(0.98);
}
```

### CSS touch-action property:

```css
/* Optimize for touch responsiveness */
button {
  touch-action: manipulation;  /* Remove 300ms tap delay */
}

/* Prevent pinch zoom from interfering with custom gestures */
.carousel {
  touch-action: pan-y;         /* Allow vertical scroll, block horizontal pinch */
}
```

---

## Swipe Gestures

Swiping is intuitive on mobile but requires clear visual affordances.

### Horizontal Swipe:

- **Use for**: Carousel navigation, card stack, tab switching, delete-to-reveal
- **Direction**: Left/right
- **Affordance**: Show partial next card or arrow hint
- **Alternative path**: Always provide tap buttons (arrows, pagination)

```css
/* Carousel with swipe support */
.carousel {
  display: flex;
  overflow-x: auto;
  scroll-snap-type: x mandatory;
  scroll-behavior: smooth;
  touch-action: pan-y pinch-zoom;  /* Allow vertical scroll, native pinch */
}

.carousel-item {
  flex: 0 0 100%;
  scroll-snap-align: start;
}
```

### Vertical Swipe:

- **Default**: Scroll (inertial scrolling)
- **Top swipe**: Pull-to-refresh
- **Bottom swipe**: Dismiss bottom sheet, collapse expanded view
- **Affordance**: Drag handle icon or partial content visibility

### Swipe-to-Delete Pattern:

```css
.list-item {
  position: relative;
  overflow: hidden;
  touch-action: pan-y;        /* Only vertical pan, not horizontal */
}

.list-item-content {
  position: relative;
  z-index: 1;
  background: #fff;
  transition: transform 200ms;
}

.list-item-actions {
  position: absolute;
  right: 0;
  top: 0;
  height: 100%;
  background: #ff3b30;
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 0 16px;
  z-index: 0;
}

/* JavaScript would handle transform: translateX(-100px) */
.list-item.swiped .list-item-content {
  transform: translateX(-100px);
}
```

### Swipe-to-Reveal Actions:

```html
<!-- Actions hidden until swiped left -->
<div class="list-item">
  <div class="list-item-content">
    <p>Swipe left to reveal actions</p>
  </div>
  <div class="list-item-actions">
    <button>Edit</button>
    <button>Delete</button>
  </div>
</div>
```

### Critical Rule:

**Never make critical actions swipe-only.** Always provide an alternative tap path (3-dot menu, long-press context menu).

---

## Pull-to-Refresh

A familiar pattern for refreshing lists on mobile.

### Behavior:

- **Trigger zone**: Top of scrollable content
- **Threshold**: 64–80px drag distance before refresh begins
- **Feedback**: Spinner icon + "Refreshing..." text
- **Duration**: Show spinner for at least 300–500ms (even if data is instant)
- **Completion**: Dismiss spinner, optionally show "Updated" confirmation

### HTML:

```html
<div class="pull-to-refresh-container">
  <div class="pull-indicator">
    <span class="spinner"></span>
    <span class="text">Pull to refresh</span>
  </div>
  <div class="scrollable-content">
    <!-- List items -->
  </div>
</div>
```

### CSS:

```css
.pull-to-refresh-container {
  position: relative;
  overflow: hidden;
}

.pull-indicator {
  position: absolute;
  top: -64px;
  left: 0;
  right: 0;
  height: 64px;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 12px;
  background: #f5f5f5;
  transition: transform 200ms;
  z-index: 10;
}

.pull-indicator.refreshing {
  transform: translateY(64px);
}

.spinner {
  display: inline-block;
  width: 24px;
  height: 24px;
  border: 3px solid #ddd;
  border-top-color: #1976d2;
  border-radius: 50%;
  animation: spin 600ms linear infinite;
}

@keyframes spin {
  to { transform: rotate(360deg); }
}
```

### JavaScript implementation concept:

```javascript
let startY = 0;
let isDragging = false;

container.addEventListener('touchstart', (e) => {
  if (scrollTop === 0) startY = e.touches[0].clientY;
});

container.addEventListener('touchmove', (e) => {
  const distance = e.touches[0].clientY - startY;
  if (distance > 0 && scrollTop === 0) {
    isDragging = true;
    indicator.style.transform = `translateY(${distance}px)`;

    if (distance > 80) {
      indicator.classList.add('ready');
    }
  }
});

container.addEventListener('touchend', () => {
  if (isDragging && distance > 80) {
    indicator.classList.add('refreshing');
    refreshData().then(() => {
      indicator.classList.remove('refreshing', 'ready');
      isDragging = false;
    });
  }
});
```

---

## Long Press

Long press triggers contextual actions or enables multi-select mode.

### When to Use:

- Contextual menu (share, copy, delete options)
- Multi-select activation
- Drag-to-reorder activation
- Haptic feedback confirmation

### Guidelines:

- **Duration**: 500ms press threshold
- **Visual feedback**: Scale change + haptic vibration
- **Always pair with alternative**: Provide a 3-dot menu for non-touch input
- **Multi-select mode**: Show checkboxes and bulk action bar

### CSS:

```css
.list-item {
  transition: background 200ms;
  user-select: none;
  -webkit-user-select: none;
}

.list-item.long-pressed {
  background: #e3f2fd;
  border-left: 4px solid #1976d2;
}

.list-item.multi-select-mode {
  padding-left: 56px;           /* Space for checkbox */
}

.list-item-checkbox {
  position: absolute;
  left: 16px;
  width: 24px;
  height: 24px;
  appearance: none;
  border: 2px solid #ccc;
  border-radius: 4px;
  cursor: pointer;
  transition: all 200ms;
}

.list-item-checkbox:checked {
  background: #1976d2;
  border-color: #1976d2;
}

/* Bulk action bar at bottom */
.bulk-action-bar {
  position: fixed;
  bottom: 0;
  left: 0;
  right: 0;
  height: 56px;
  background: #1976d2;
  color: #fff;
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0 16px;
  transform: translateY(100%);
  transition: transform 200ms;
}

.multi-select-active .bulk-action-bar {
  transform: translateY(0);
}
```

### JavaScript:

```javascript
let longPressTimer;

element.addEventListener('touchstart', () => {
  longPressTimer = setTimeout(() => {
    element.classList.add('long-pressed');
    navigator.vibrate(50);  // Haptic feedback
    showContextMenu();
  }, 500);
});

element.addEventListener('touchend', () => {
  clearTimeout(longPressTimer);
});
```

---

## Pinch / Spread

Pinch and spread are familiar zoom gestures. Use sparingly.

### When to Use:

- Map zoom (expected interaction)
- Image zoom (optional enhancement)
- Content scaling in specific contexts

### When NOT to Use:

- Navigation
- General content scaling (breaks responsive design)
- Primary action (always provide button alternative)

### Implementation:

Modern browsers handle pinch-zoom natively. For custom pinch gestures:

```css
/* Allow pinch zoom naturally */
.zoomable-image {
  touch-action: pinch-zoom;
  user-select: none;
}

/* Prevent pinch in carousels */
.carousel {
  touch-action: pan-y pinch-zoom;  /* Vertical pan allowed, pinch allowed */
}
```

### Accessibility:

Always provide zoom buttons as an alternative to pinch:

```html
<div class="image-viewer">
  <img id="zoomImage" src="photo.jpg" alt="Zoomable photo">
  <div class="zoom-controls">
    <button id="zoomIn">+</button>
    <button id="zoomOut">−</button>
  </div>
</div>
```

---

## Bottom Sheets

Bottom sheets are a flexible mobile pattern for exposing secondary content or actions.

### Types:

1. **Full bottom sheet**: Multi-step forms, complex choices, secondary navigation
2. **Half bottom sheet**: Quick actions, filters, share options, sort menu

### Guidelines:

- **Drag handle**: 32px wide × 4px tall, centered at top, indicates sheet is draggable
- **Backdrop tap**: Always dismisses the sheet
- **Maximum height**: 90% of screen height (leave some space to see content below)
- **Rounding**: Top corners rounded (16px radius typical)
- **Scroll behavior**: Content inside sheet scrolls independently if it exceeds height

### HTML:

```html
<div class="bottom-sheet-backdrop"></div>
<div class="bottom-sheet">
  <div class="bottom-sheet-handle"></div>
  <div class="bottom-sheet-header">
    <h2>Sheet Title</h2>
  </div>
  <div class="bottom-sheet-content">
    <!-- Content here -->
  </div>
</div>
```

### CSS:

```css
.bottom-sheet-backdrop {
  position: fixed;
  inset: 0;
  background: rgba(0, 0, 0, 0.32);
  opacity: 0;
  pointer-events: none;
  transition: opacity 200ms;
  z-index: 99;
}

.bottom-sheet-backdrop.visible {
  opacity: 1;
  pointer-events: auto;
}

.bottom-sheet {
  position: fixed;
  bottom: 0;
  left: 0;
  right: 0;
  max-height: 90vh;
  background: #fff;
  border-radius: 16px 16px 0 0;
  box-shadow: 0 -2px 8px rgba(0, 0, 0, 0.12);
  display: flex;
  flex-direction: column;
  transform: translateY(100%);
  transition: transform 200ms cubic-bezier(0.4, 0, 0.2, 1);
  z-index: 100;
}

.bottom-sheet.visible {
  transform: translateY(0);
}

.bottom-sheet-handle {
  width: 32px;
  height: 4px;
  background: #d0d0d0;
  border-radius: 2px;
  margin: 12px auto;
  cursor: grab;
  flex-shrink: 0;
}

.bottom-sheet-handle:active {
  cursor: grabbing;
}

.bottom-sheet-header {
  padding: 0 16px 16px;
  border-bottom: 1px solid #e0e0e0;
  flex-shrink: 0;
}

.bottom-sheet-content {
  overflow-y: auto;
  -webkit-overflow-scrolling: touch;
  flex: 1;
  padding: 16px;
}
```

### JavaScript (basic):

```javascript
const backdrop = document.querySelector('.bottom-sheet-backdrop');
const sheet = document.querySelector('.bottom-sheet');

backdrop.addEventListener('click', () => {
  sheet.classList.remove('visible');
  backdrop.classList.remove('visible');
});

// Toggle sheet
function openSheet() {
  sheet.classList.add('visible');
  backdrop.classList.add('visible');
}

function closeSheet() {
  sheet.classList.remove('visible');
  backdrop.classList.remove('visible');
}
```

---

## Modal Dialogs on Mobile

Modals block the entire screen. Use sparingly on mobile.

### When to Use:

- Destructive action confirmation (delete, logout)
- Critical alerts (error that prevents continuation)
- Unavoidable permissions/agreement

### When NOT to Use:

- Information (use inline or expandable sections)
- Non-urgent feedback (use toast/snackbar)
- Navigation (use bottom sheet)
- Long forms (use full-screen overlay)

### Guidelines:

- **Title**: Clear, concise (1 line typical)
- **Content**: Keep brief (2–3 sentences max)
- **Buttons**: Max 2 (primary action + cancel) on mobile
- **Button width**: Full-width, stacked vertically
- **Dismiss**: Only via button tap (no backdrop tap)

### HTML:

```html
<div class="modal-backdrop"></div>
<div class="modal">
  <div class="modal-header">
    <h2>Delete item?</h2>
  </div>
  <div class="modal-content">
    <p>This cannot be undone. Are you sure?</p>
  </div>
  <div class="modal-actions">
    <button class="btn-secondary">Cancel</button>
    <button class="btn-destructive">Delete</button>
  </div>
</div>
```

### CSS:

```css
.modal-backdrop {
  position: fixed;
  inset: 0;
  background: rgba(0, 0, 0, 0.54);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 101;
}

.modal {
  background: #fff;
  border-radius: 8px;
  width: calc(100% - 32px);
  max-width: 400px;
  box-shadow: 0 11px 15px -7px rgba(0, 0, 0, 0.2);
  overflow: hidden;
}

.modal-header {
  padding: 24px 24px 0;
}

.modal-header h2 {
  margin: 0;
  font-size: 18px;
  font-weight: 500;
}

.modal-content {
  padding: 20px 24px;
  color: #666;
  font-size: 14px;
  line-height: 1.5;
}

.modal-actions {
  display: flex;
  flex-direction: column;
  gap: 8px;
  padding: 16px 24px 24px;
}

.modal-actions button {
  padding: 12px 24px;
  border: none;
  border-radius: 4px;
  font-size: 16px;
  font-weight: 500;
  cursor: pointer;
  transition: all 200ms;
  height: 48px;
}

.btn-secondary {
  background: #f5f5f5;
  color: #333;
}

.btn-secondary:active {
  background: #e0e0e0;
}

.btn-destructive {
  background: #ff3b30;
  color: #fff;
}

.btn-destructive:active {
  background: #e63927;
}
```

---

## List Patterns

Lists are fundamental mobile patterns. Optimize for thumb interaction.

### Standard List Item Heights:

- **Single-line**: 48px (icon + text)
- **Two-line**: 64px (title + subtitle)
- **Avatar + title + subtitle**: 72px

### List Item Anatomy:

```
┌────────────────────────────────┐
│ Icon  Title              Chevron│  ← 56px height
│       Subtitle                  │
└────────────────────────────────┘
```

### Dividers:

- Use spacing (16px gap) instead of visible lines
- If dividers necessary, use light gray (#e0e0e0)
- Never use heavy dividers on mobile (clutters space)

### Right-Side Indicators:

- **Chevron (→)**: Indicates navigation
- **Toggle switch**: In-place boolean action
- **Info icon**: Tap for detail/tooltip
- **Badge**: Notification count or status

### Section Headers:

- **Height**: 48px
- **Font**: 14px, uppercase, bold
- **Sticky**: Stick to top on scroll
- **Padding**: 16px horizontal, 12px vertical

### CSS:

```css
.list {
  list-style: none;
  margin: 0;
  padding: 0;
}

.list-section {
  margin-top: 16px;
}

.list-header {
  height: 48px;
  padding: 12px 16px;
  font-size: 14px;
  font-weight: 600;
  text-transform: uppercase;
  color: #999;
  position: sticky;
  top: 0;
  background: #fafafa;
  z-index: 10;
}

.list-item {
  display: flex;
  align-items: center;
  min-height: 56px;
  padding: 12px 16px;
  gap: 16px;
  border-bottom: 1px solid #f0f0f0;
  text-decoration: none;
  color: #333;
  transition: background 150ms;
}

.list-item:active {
  background: #f5f5f5;
}

.list-item-icon {
  width: 40px;
  height: 40px;
  flex-shrink: 0;
  display: flex;
  align-items: center;
  justify-content: center;
}

.list-item-content {
  flex: 1;
  min-width: 0;         /* Important for text truncation */
}

.list-item-title {
  margin: 0;
  font-size: 16px;
  font-weight: 500;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.list-item-subtitle {
  margin: 4px 0 0;
  font-size: 14px;
  color: #999;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.list-item-action {
  flex-shrink: 0;
  color: #999;
  font-size: 20px;
}
```

---

## Form Patterns on Mobile

Forms must be touch-friendly on mobile.

### Input Height:

- **Minimum**: 56px (44px touch target + padding)
- **Padding**: 12px vertical, 16px horizontal
- **Font size**: 16px (prevents auto-zoom on focus in iOS)

### Keyboard Types:

Always use appropriate `type` and `inputmode` attributes:

```html
<input type="email" inputmode="email" placeholder="Email">
<input type="tel" inputmode="tel" placeholder="Phone">
<input type="number" inputmode="numeric" placeholder="Number">
<input type="url" inputmode="url" placeholder="URL">
<input type="text" inputmode="search" placeholder="Search">
<textarea inputmode="text" placeholder="Message"></textarea>
```

### Layout:

- **Single column only** on mobile
- **Stacked inputs**: No side-by-side on screens < 600px
- **Labels**: Always above input (not placeholder-only)
- **Label font**: 14px, bold, 12px top margin

### Sticky Submit Button:

Keep the submit button visible at bottom of screen:

```css
form {
  padding-bottom: 80px;  /* Space for sticky button */
}

.form-submit {
  position: fixed;
  bottom: 0;
  left: 0;
  right: 0;
  height: 56px;
  padding: 12px 16px;
  background: #1976d2;
  color: #fff;
  border: none;
  font-size: 16px;
  font-weight: 500;
  cursor: pointer;
  z-index: 90;
}

.form-submit:disabled {
  opacity: 0.54;
  cursor: not-allowed;
}
```

### Auto-Advance on Completion:

For PIN entry or OTP fields, auto-advance to next field:

```javascript
// Auto-advance OTP input
const inputs = document.querySelectorAll('.otp-input');

inputs.forEach((input, index) => {
  input.addEventListener('input', (e) => {
    if (e.target.value.length === 1 && index < inputs.length - 1) {
      inputs[index + 1].focus();
    }
  });

  input.addEventListener('backspace', (e) => {
    if (e.target.value.length === 0 && index > 0) {
      inputs[index - 1].focus();
    }
  });
});
```

### Form Input CSS:

```css
input,
textarea,
select {
  width: 100%;
  min-height: 56px;
  padding: 12px 16px;
  font-size: 16px;
  border: 1px solid #ccc;
  border-radius: 4px;
  transition: border-color 200ms;
  font-family: inherit;
}

input:focus,
textarea:focus,
select:focus {
  outline: none;
  border-color: #1976d2;
  box-shadow: 0 0 0 3px rgba(25, 118, 210, 0.1);
}

input:invalid:focus {
  border-color: #ff3b30;
  box-shadow: 0 0 0 3px rgba(255, 59, 48, 0.1);
}

label {
  display: block;
  margin-top: 12px;
  margin-bottom: 4px;
  font-size: 14px;
  font-weight: 600;
  color: #333;
}

.form-group {
  margin-bottom: 16px;
}

/* Floating label (advanced) */
.floating-label {
  position: relative;
}

.floating-label label {
  position: absolute;
  top: 12px;
  left: 16px;
  font-size: 16px;
  font-weight: 400;
  color: #999;
  pointer-events: none;
  transition: all 200ms;
}

.floating-label input:focus ~ label,
.floating-label input:not(:placeholder-shown) ~ label {
  top: -8px;
  left: 16px;
  font-size: 12px;
  color: #1976d2;
}
```

---

## Arabic / RTL Mobile Considerations

RTL (right-to-left) languages like Arabic require full layout mirroring.

### Fundamental Changes:

1. **Entire layout mirrors**: Left ↔ right
2. **Text direction**: Content flows right to left
3. **Icons flip logically**: Back arrow points right (opposite of LTR)

### CSS Implementation:

```html
<html dir="rtl" lang="ar">
  <!-- Content -->
</html>
```

CSS logical properties automatically handle mirroring:

```css
/* Use logical properties — automatically mirror in RTL */
.element {
  margin-inline-start: 16px;    /* left in LTR, right in RTL */
  margin-inline-end: 16px;      /* right in LTR, left in RTL */
  padding-inline: 16px;         /* Both sides */
  inset-inline-start: 0;        /* left: 0 in LTR, right: 0 in RTL */
}

/* Instead of these deprecated properties */
.element {
  margin-left: 16px;           /* ✗ Doesn't work in RTL */
  left: 0;                     /* ✗ Wrong direction in RTL */
}
```

### Component-Specific RTL Adjustments:

**Bottom Tab Bar:**
```css
.bottom-nav {
  direction: rtl;              /* Reverses tab order */
  text-align: right;
}
```

**FAB (moves to bottom-left in RTL):**
```css
.fab {
  inset-inline-end: 24px;     /* right in LTR, left in RTL */
  bottom: 24px;
}
```

**Swipe-to-Delete (trigger from left in RTL):**
```css
/* LTR: swipe left reveals delete button on right */
/* RTL: swipe right reveals delete button on left */
.list-item-actions {
  inset-inline-start: 0;      /* right in LTR, left in RTL */
}
```

**Back Arrow (flips direction):**
```html
<!-- Use Unicode bidirectional control -->
<button>← ‏Back</button>   <!-- LTR: left arrow -->

<!-- Or use transform in RTL -->
<style>
  [dir="rtl"] .back-icon {
    transform: scaleX(-1);
  }
</style>
```

### Testing:

- **Never test with mirrored screenshots alone** — use actual RTL device or browser extension
- Test right-to-left text flowing correctly
- Verify numbers and URLs still read left-to-right (they should in RTL)
- Test form input order (label positioning)

### Critical Gotchas:

- Images and icons should NOT flip (e.g., flags, logos)
- Use `direction: ltr` to prevent specific content from mirroring
- Numbers and Latin text in Arabic content remain LTR

---

## Platform-Specific Patterns

iOS and Android have different navigation paradigms.

### iOS Back Navigation:

- **System gesture**: Swipe from left edge to go back
- **No back button needed**: Users expect the system gesture
- **Exception**: Top-level screen may show "Close" button

```html
<!-- iOS: Don't show a back button -->
<button class="back-button">← Back</button>  <!-- ✗ Redundant -->

<!-- Instead, rely on system swipe-back gesture -->
```

### Android Back Navigation:

- **System button**: Physical or gesture-based back button (bottom or navbar)
- **Back button expected**: Android convention is to show back button
- **Exception**: Home/launcher screen has no back button

```html
<!-- Android: Show back button -->
<button class="back-button">← Back</button>  <!-- ✓ Expected -->
```

### Implications:

- Avoid prominent "Back" button on iOS
- Always show "Back" button on Android
- Use feature detection or platform-specific CSS:

```css
@supports (overscroll-behavior: contain) {
  /* iOS Safari — hide back button, rely on swipe */
  .back-button {
    display: none;
  }
}

@media (prefers-reduced-motion: no-preference) {
  /* Smooth transitions supported */
}
```

---

## Mobile Accessibility

Accessibility on mobile is critical. Many users rely on assistive technology.

### Font Scaling:

- Use relative units: `rem`, `em`, `%`
- Respect user's font size settings

```css
html {
  font-size: 16px;             /* Base for rem units */
}

button {
  font-size: 1rem;             /* 16px, scales with user settings */
}

/* ✗ Don't force fixed sizes */
button {
  font-size: 16px;             /* ✗ Ignores user preferences */
}
```

### Viewport Settings:

```html
<!-- ✓ Allow user scaling -->
<meta name="viewport" content="width=device-width, initial-scale=1">

<!-- ✗ Never disable user scaling -->
<meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1, user-scalable=no">
```

### Color Contrast:

Same as desktop:
- **Text**: 4.5:1 minimum (normal text)
- **Large text** (18pt+ or 14pt bold): 3:1 minimum

Test with tools like WebAIM Contrast Checker.

### Touch Target Contrast:

Ensure UI is distinguishable from background (not just color):

```css
/* ✓ Clear contrast with border or shadow */
button {
  background: #1976d2;
  border: 2px solid #fff;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
}

/* ✗ Don't rely on color alone */
.tab.active {
  color: #1976d2;              /* ✗ Only color change */
}

/* ✓ Add icon or underline */
.tab.active {
  color: #1976d2;
  border-bottom: 3px solid #1976d2;
}
```

### Screen Reader Optimization:

```html
<!-- Label form inputs -->
<label for="email">Email</label>
<input id="email" type="email">

<!-- Use semantic HTML -->
<button>Delete</button>       <!-- ✓ Semantically clear -->
<div role="button">Delete</div>  <!-- ✗ Requires extra aria -->

<!-- Image alt text -->
<img src="icon.svg" alt="Settings icon">

<!-- Use aria-label for icon-only buttons -->
<button aria-label="Close dialog">✕</button>
```

---

## Mobile UX Checklist

Use this checklist before considering any mobile screen complete:

- [ ] **Primary action in thumb reach**: Bottom 40% of screen (no top-center critical buttons)
- [ ] **All touch targets ≥ 44×44px**: Verified with dev tools (no undersized buttons)
- [ ] **8px+ spacing**: Between adjacent touch targets
- [ ] **Form uses appropriate keyboard type**: `type="email"`, `type="tel"`, etc.
- [ ] **No horizontal scrolling**: Unless intentional carousel/galleries
- [ ] **Bottom nav** (if used): Has icon + label (never icon-only)
- [ ] **Swipeable content has visual affordance**: Partial visible card, arrow hint, or drag handle
- [ ] **No swipe-only critical actions**: Always provide alternate tap path
- [ ] **RTL layout mirrors correctly**: Tested on actual RTL device/simulator
- [ ] **Tap feedback < 100ms**: Visual response on button press
- [ ] **Text scales with system size**: Uses `rem` or viewport-relative units
- [ ] **Color contrast ≥ 4.5:1**: For normal text
- [ ] **Modals avoid blocking content**: Used only for critical alerts/confirmations
- [ ] **Pull-to-refresh has threshold feedback**: 64–80px zone with visual cue
- [ ] **FAB single action**: Not multiple actions, not for navigation
- [ ] **Focus states visible**: Keyboard navigation users can see where they are
- [ ] **No maximum-scale=1**: Users can pinch-zoom if needed

---

## Quick Reference: Anatomy of a Complete Mobile Screen

```
┌─────────────────────────────────┐
│                                 │ ← Status bar (OS)
├─────────────────────────────────┤
│ ← Top App Bar (optional)        │
│   Title, search, actions        │ ← 56px height
├─────────────────────────────────┤
│                                 │
│     MAIN CONTENT AREA           │ ← Scrollable
│  (respects thumb reach)         │
│                                 │ ← Sticky bottom nav above
│                                 │
├─────────────────────────────────┤
│  Home  | Search | Profile       │ ← Bottom nav: 56px, icon+label
└─────────────────────────────────┘   (Fixed to bottom)
        ↑
   [FAB] (floating over content)
   56×56px, 16px clearance
```

---

## Additional Resources

- **Steven Hoober's Thumb Zone Research**: "Designing for Touch" research on mobile grip patterns
- **Material Design Mobile Guidelines**: https://material.io/design/platform-guidance/android-bars.html
- **iOS Human Interface Guidelines**: https://developer.apple.com/design/human-interface-guidelines/ios
- **W3C Touch Events Spec**: https://www.w3.org/TR/touch-events/
- **CSS Logical Properties**: https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Logical_Properties

---

**Last Updated:** March 2026
**Version:** 1.0
**Part of DesignXI Skill System**

---

## Adaptive Navigation Patterns (Cross-Platform)

Navigation architecture must adapt to screen size and platform conventions. Apply these rules when designing any product with mobile + desktop breakpoints.

### Sidebar vs. Bottom Nav — Adaptive Threshold

```
≥ 1024px (Desktop / Large Tablet): Persistent sidebar navigation
  - Show labels + icons
  - Collapsible to icon-only (min-width: 72px, expanded: 240px)
  - Nested hierarchy supported

768px–1023px (Tablet): Bottom nav OR rail nav
  - Bottom nav if 3–5 top-level items
  - Rail nav (icon-only vertical strip) for denser hierarchies
  - No hamburger menu — navigation always visible

< 768px (Mobile): Bottom nav (preferred) or tab bar
  - 3–5 items max, never more
  - Icons + labels (not icon-only)
  - Active state: filled icon + primary color text
```

**Never**: hamburger menus as the primary navigation on mobile. They hide structure and reduce engagement by 20–30% (Nielsen Norman Group).

### Gesture Navigation Support

Modern mobile OSes use gesture-based navigation. Design must coexist with system gestures:

**iOS (swipe-from-left = back)**
- Never place important interactive elements in the leftmost 20px of screen
- Back-swipe is a user expectation — don't block it with drawer gestures
- If you have a left drawer, use a handle area or require longer swipe distance

**Android Predictive Back (Android 13+)**
- Support `android:enableOnBackInvokedCallback` equivalent in web PWAs
- Show destination preview when user initiates back gesture
- Animate current screen slightly right and shrink to 95% while back preview appears

**Swipe-up to dismiss (modals, bottom sheets)**
- Threshold: 40% of sheet height = dismiss
- Below threshold: spring back to original position
- Provide visual drag handle (4×32px pill, --gray-300)

### Back Stack Integrity

The back stack must be predictable. Users expect "back" to undo the last navigation:

```
Rules:
✓ Back always goes to the previous screen (never skips or jumps)
✓ Modal dismiss ≠ back navigation — modals close, they don't navigate back
✓ Tab switches do not push to back stack — switching tabs doesn't break back
✓ Deep links land on correct screen with working back stack
✗ Never push the same screen twice consecutively to the stack
✗ Never clear back stack without user-initiated action (logout is the exception)
```

### Bottom Nav: Top-Level Items Only

Bottom navigation is for top-level destinations only:

```
✓ Correct: Home | Search | Messages | Profile
✗ Wrong:   Home | Search | Compose Message | Notification Settings

Rules:
- Bottom nav items are always top-level entry points
- Never put action items in bottom nav (Compose, Add, Create belong in FAB)
- Active item: filled icon + primary color, others: outline icon + gray-500
- Badge for unread counts: max "99+" — never show raw large numbers
- Haptic feedback on tab switch (mobile native apps)
```

### Persistent Navigation — Never Hide Nav During Scroll

Navigation must remain accessible. Common mistake: hiding nav on scroll-down, showing on scroll-up:

```css
/* If you must auto-hide (content-heavy apps only): */
.bottom-nav {
  transform: translateY(0);
  transition: transform 200ms var(--spring-enter);
}
.bottom-nav.hidden {
  transform: translateY(100%);
  /* Only hide after 200px downward scroll */
  /* Immediately show on ANY upward scroll */
}
```

**Rule**: Only auto-hide on media/reading apps where content is primary. Never auto-hide on task-based apps (settings, forms, dashboards).

### Focus Management on Route Change

When navigating to a new screen, set focus correctly for keyboard and screen reader users:

```js
// After route change — move focus to the new page heading or main content
const heading = document.querySelector('h1, [role="main"]');
if (heading) {
  heading.setAttribute('tabindex', '-1');
  heading.focus();
  // Remove tabindex after focus (don't make static elements permanently focusable)
  heading.addEventListener('blur', () => heading.removeAttribute('tabindex'), { once: true });
}

// Announce route change to screen readers
const announcer = document.getElementById('route-announcer');
announcer.textContent = `Navigated to: ${newPageTitle}`;
```

```html
<!-- Always include a live region for route announcements -->
<div id="route-announcer" aria-live="polite" aria-atomic="true"
     style="position:absolute; left:-9999px; width:1px; height:1px; overflow:hidden">
</div>
```

### Navigation Accessibility Checklist

```
□ Skip-to-main-content link as first focusable element on every page
□ Current nav item has aria-current="page"
□ Bottom nav / sidebar uses role="navigation" with aria-label
□ Focus managed on route change (heading or main content focused)
□ Route announcer live region present for screen readers
□ Back gesture supported and not blocked by overlay gestures
□ Keyboard navigation works through all nav items (Tab / Shift+Tab)
□ Nav items have visible focus indicators (not just color change)
```

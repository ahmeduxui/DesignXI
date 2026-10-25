# Microinteractions: The Complete DesignXI Reference

Microinteractions are the small, contained product moments that accomplish a single task. They are the difference between a product that feels alive and one that feels static. Every click, toggle, hover, and form validation is a microinteraction waiting to delight—or frustrate—your users.

Based on Dan Saffer's "Microinteractions" framework and Material Design motion principles, this guide covers everything needed to design and implement microinteractions in HTML/CSS.

---

## 1. What Are Microinteractions?

A microinteraction is a contained sequence of actions performed to accomplish a single task. They are:

- **Self-contained**: They exist within a small, focused part of the UI
- **Single-purpose**: They accomplish one, clearly defined task
- **Feedback-rich**: They communicate what is happening at every step
- **Delightful**: They add personality without adding cognitive load

### Common Microinteraction Examples

- **Like button animation**: Tap → heart expands and color fills → count increments
- **Toggle switch**: Click → background color transitions → thumb slides to new position
- **Pull-to-refresh**: Swipe down → spinner appears → data refreshes → returns to resting state
- **Form validation**: User leaves field → validation runs → error or success state appears
- **Loading spinner**: Async action starts → spinner appears → action completes → spinner disappears
- **Notification badge**: New message → badge appears with animation → auto-dismisses after 3 seconds
- **Hover card elevation**: Mouse enters → shadow grows → card lifts slightly
- **Input focus ring**: Click input → border color changes → focus ring expands with animation

---

## 2. The 4 Parts of a Microinteraction (Saffer Framework)

Every microinteraction has four essential parts:

### 2.1 Trigger

**What initiates the microinteraction.**

**User-initiated triggers:**
- Tap / Click
- Swipe / Drag
- Hover
- Long-press
- Voice command

**System-initiated triggers:**
- Timer expiration
- Location change
- Data event (new message, update available)
- System state change (network disconnection, low battery)
- Schedule completion

#### Example: Like Button

```html
<!-- User trigger: click on the button -->
<button class="like-btn" aria-label="Like this post" aria-pressed="false">
  <svg class="like-icon" viewBox="0 0 24 24" width="24" height="24">
    <path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"/>
  </svg>
  <span class="like-count">142</span>
</button>
```

---

### 2.2 Rules

**What happens when the trigger occurs. The logic and constraints.**

Rules define:
- What state changes occur
- What values change (count, color, position)
- What constraints apply (can't go negative, max value, cooldown period)
- Whether the action is reversible
- Order of operations

#### Example: Like Button Rules

```
IF user clicks like button AND user is authenticated:
  - Toggle liked state (true ↔ false)
  - Increment/decrement count by 1
  - Trigger feedback animation
ELSE IF user is not authenticated:
  - Show login prompt instead
END IF
```

---

### 2.3 Feedback

**How the system communicates the result to the user.**

Feedback occurs at three moments:
1. **Immediate feedback** (0-100ms): Visual response to the trigger
2. **Active feedback** (100-300ms): Animation during the action
3. **Completion feedback** (300-500ms): Result state

#### Example: Like Button Feedback

```css
/* Immediate: Heart responds to click */
.like-btn:active {
  transform: scale(0.9);
}

/* Active: Heart expands and fills */
.like-icon {
  transition: transform 0.3s cubic-bezier(0.34, 1.56, 0.64, 1);
}
.like-btn.liked .like-icon {
  transform: scale(1.3);
  fill: #e74c3c;
}

/* Completion: Count updates */
.like-count {
  transition: color 0.2s ease;
}
.like-btn.liked .like-count {
  color: #e74c3c;
}
```

---

### 2.4 Loops & Modes

**Does it repeat? Does it change after repeated use?**

- **Loops**: Does the microinteraction happen again? (spinner loops continuously, toast appears once)
- **Modes**: Does behavior change based on state? (button disabled after click until response arrives)

#### Example: Like Button Modes

```css
/* Normal mode: user can interact */
.like-btn:not([disabled]) {
  cursor: pointer;
}

/* Submitting mode: disable user interaction */
.like-btn[disabled] {
  opacity: 0.6;
  cursor: not-allowed;
  pointer-events: none;
}

/* Liked mode: heart is filled */
.like-btn.liked .like-icon {
  fill: #e74c3c;
}
```

---

## 3. The 5 Types of Feedback

Users perceive actions through multiple sensory channels. Provide feedback through:

### 3.1 Visual Feedback

**Color change, animation, icon swap, size change.**

Most common and primary feedback mechanism.

```css
/* Color change on hover */
.btn:hover {
  background-color: #2980b9;
  transition: background-color 0.15s ease;
}

/* Icon swap on state change */
.star-btn.active::before {
  content: "★"; /* filled star */
}
.star-btn:not(.active)::before {
  content: "☆"; /* empty star */
}

/* Size change on interaction */
.btn:active {
  transform: scale(0.95);
  transition: transform 0.1s ease-out;
}
```

### 3.2 Positional Feedback

**Element moves to communicate action.**

```css
/* Card elevation on hover */
.card {
  box-shadow: 0 1px 3px rgba(0,0,0,0.12);
  transform: translateY(0);
  transition: box-shadow 0.2s ease, transform 0.2s ease;
}
.card:hover {
  box-shadow: 0 8px 16px rgba(0,0,0,0.15);
  transform: translateY(-4px);
}

/* Notification slide in from top */
.toast {
  transform: translateY(-120px);
  opacity: 0;
  transition: transform 0.3s cubic-bezier(0.34, 1.56, 0.64, 1), opacity 0.3s ease;
}
.toast.show {
  transform: translateY(0);
  opacity: 1;
}
```

### 3.3 Text Feedback

**Label or content updates to communicate progress.**

```html
<!-- Button text changes during async operation -->
<button class="btn-submit" id="submitBtn">Save</button>

<script>
const btn = document.getElementById('submitBtn');
btn.addEventListener('click', async () => {
  btn.textContent = 'Saving...';
  btn.disabled = true;

  try {
    await saveData();
    btn.textContent = 'Saved!';
    btn.classList.add('success');
    setTimeout(() => {
      btn.textContent = 'Save';
      btn.classList.remove('success');
      btn.disabled = false;
    }, 2000);
  } catch (error) {
    btn.textContent = 'Save Failed';
    btn.classList.add('error');
  }
});
</script>

<style>
.btn-submit {
  transition: background-color 0.2s ease;
}
.btn-submit.success {
  background-color: #27ae60;
}
.btn-submit.error {
  background-color: #e74c3c;
}
</style>
```

### 3.4 Sound Feedback

**Subtle audio cue (optional, never mandatory).**

```html
<!-- Low-level sound for delightful moments -->
<button class="btn-sound" onclick="playSound()">
  Like
</button>

<audio id="soundEffect" preload="auto">
  <source src="/sounds/pop.mp3" type="audio/mpeg">
</audio>

<script>
function playSound() {
  const audio = document.getElementById('soundEffect');
  audio.currentTime = 0; // reset to start
  audio.play().catch(e => console.log('Audio play failed:', e));
}
</script>

<style>
/* Use class to distinguish sound-enabled interactions */
.btn-sound {
  /* ... other styles ... */
}
</style>
```

**Guidelines for sound:**
- Never auto-play audio — always require user interaction
- Keep volume low and duration short (200-400ms max)
- Only use for high-value moments (successful save, achievement unlocked)
- Provide option to disable in settings

### 3.5 Haptic Feedback

**Vibration pattern (mobile only, for important moments).**

```html
<button class="btn-haptic" onclick="triggerHaptic()">
  Send Message
</button>

<script>
function triggerHaptic(pattern = 'success') {
  // Check for Vibration API support
  if (!navigator.vibrate) return;

  const patterns = {
    success: [50, 30, 50],      // light, pause, light
    warning: [100, 50, 100],    // medium, pause, medium
    error: [200, 100, 200],     // strong, pause, strong
  };

  navigator.vibrate(patterns[pattern] || [50]);
}
</script>

<style>
.btn-haptic {
  /* ... button styles ... */
}
</style>
```

**Guidelines for haptic:**
- Only use on mobile devices
- Reserve for important moments (save success, error, confirmation)
- Never use as primary feedback mechanism
- Always provide visual feedback as fallback
- Allow user to disable in accessibility settings

---

## 4. Timing Rules

Microinteraction timing is critical. Too fast feels broken, too slow feels laggy.

### 4.1 Animation Duration Guidelines

```
Immediate response (0-100ms):
└─ Button press → visual state change
   Example: :active state when user clicks

Functional animation (100-300ms):
└─ Element state changes, transitions
   Example: button hover effect, input focus ring, toggle switch

Expressive animation (300-500ms):
└─ Screen transitions, deliberate moments
   Example: modal open, page transition, accordion expand

Long process (500ms+):
└─ Show progress indicator — never leave the UI silent
   Example: file upload, form submission, data sync
```

### 4.2 Timing Implementation

```css
/* IMMEDIATE: Button press feedback (instant, <50ms) */
.btn:active {
  transform: scale(0.95);
  /* no transition - immediate response */
}

/* FUNCTIONAL: Hover state (150-200ms) */
.btn:hover {
  background-color: #2980b9;
  transition: background-color 0.15s ease;
}

/* FUNCTIONAL: Input focus (150-200ms) */
input:focus {
  border-color: #3498db;
  box-shadow: 0 0 0 3px rgba(52, 152, 219, 0.1);
  transition: border-color 0.15s ease, box-shadow 0.15s ease;
}

/* EXPRESSIVE: Modal open (300-400ms) */
.modal {
  opacity: 0;
  transform: scale(0.95);
  transition: opacity 0.3s ease, transform 0.3s cubic-bezier(0.34, 1.56, 0.64, 1);
}
.modal.show {
  opacity: 1;
  transform: scale(1);
}

/* EXPRESSIVE: Page transition (250-350ms) */
.page {
  opacity: 0;
  transition: opacity 0.3s ease;
}
.page.active {
  opacity: 1;
}

/* LONG PROCESS: Loading spinner (infinite loop) */
@keyframes spin {
  from { transform: rotate(0deg); }
  to { transform: rotate(360deg); }
}
.spinner {
  animation: spin 0.75s linear infinite;
}
```

### 4.3 The "No Animation Should Block" Rule

Never make animations blocking or mandatory. Users should always be able to interact with the UI while animation is in progress.

```css
/* ❌ WRONG: Animation blocks interaction */
.modal {
  pointer-events: none; /* blocks interaction! */
  animation: slideIn 0.5s ease;
}

/* ✓ CORRECT: Animation non-blocking */
.modal {
  animation: slideIn 0.5s ease;
  /* pointer-events allows interaction */
}

/* ✓ CORRECT: Transition doesn't block */
button {
  transition: background-color 0.3s ease;
  /* can still click and interact */
}
```

---

## 5. Core Microinteractions for Every Project

These 10 microinteractions appear in almost every web project. Master these first.

---

### 5.1 Button States (Hover, Active, Disabled)

**All buttons must have these 4 states:**

```html
<button class="btn btn-primary">Save</button>
<button class="btn btn-primary" disabled>Save</button>
```

```css
.btn {
  padding: 8px 16px;
  border: none;
  border-radius: 4px;
  font-size: 14px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.15s ease;
}

/* Default state */
.btn-primary {
  background-color: #3498db;
  color: white;
  transform: scale(1);
}

/* Hover state: slightly darker background */
.btn-primary:hover:not(:disabled) {
  background-color: #2980b9;
}

/* Active state: pressed down animation + darkest color */
.btn-primary:active {
  background-color: #1f618d;
  transform: scale(0.97);
}

/* Focus state: visible focus ring for keyboard accessibility */
.btn-primary:focus {
  outline: none;
  box-shadow: 0 0 0 3px rgba(52, 152, 219, 0.3);
}

/* Disabled state: grayed out, no interaction */
.btn-primary:disabled {
  background-color: #ecf0f1;
  color: #95a5a6;
  cursor: not-allowed;
  opacity: 0.6;
}

/* Variant: Secondary button */
.btn-secondary {
  background-color: #95a5a6;
  color: white;
}
.btn-secondary:hover:not(:disabled) {
  background-color: #7f8c8d;
}
.btn-secondary:active {
  background-color: #5d6d7b;
  transform: scale(0.97);
}
```

---

### 5.2 Toggle / Switch

**A switch that changes state with visual feedback.**

```html
<label class="toggle-label">
  <input type="checkbox" class="toggle-input">
  <span class="toggle-slider"></span>
  <span class="toggle-label-text">Dark Mode</span>
</label>
```

```css
.toggle-label {
  display: flex;
  align-items: center;
  gap: 8px;
  cursor: pointer;
}

.toggle-input {
  display: none;
}

.toggle-slider {
  position: relative;
  display: inline-block;
  width: 44px;
  height: 24px;
  background-color: #bdc3c7;
  border-radius: 12px;
  transition: background-color 0.2s ease;
}

/* Thumb circle inside slider */
.toggle-slider::before {
  content: '';
  position: absolute;
  top: 2px;
  left: 2px;
  width: 20px;
  height: 20px;
  background-color: white;
  border-radius: 50%;
  transition: transform 0.2s cubic-bezier(0.4, 0, 0.2, 1);
}

/* Checked state: background changes, thumb slides right */
.toggle-input:checked + .toggle-slider {
  background-color: #27ae60;
}
.toggle-input:checked + .toggle-slider::before {
  transform: translateX(20px);
}

/* Focus state */
.toggle-input:focus + .toggle-slider {
  box-shadow: 0 0 0 3px rgba(39, 174, 96, 0.3);
}

.toggle-label-text {
  font-size: 14px;
  font-weight: 500;
  user-select: none;
}
```

---

### 5.3 Input Focus State

**Clear, visible focus indicator for keyboard accessibility.**

```html
<input type="text" placeholder="Enter your name" class="input">
```

```css
.input {
  padding: 8px 12px;
  border: 1px solid #bdc3c7;
  border-radius: 4px;
  font-size: 14px;
  font-family: inherit;
  transition: border-color 0.15s ease, box-shadow 0.15s ease;
}

/* Hover state: border slightly darker */
.input:hover {
  border-color: #95a5a6;
}

/* Focus state: color ring around border */
.input:focus {
  outline: none;
  border-color: #3498db;
  box-shadow: 0 0 0 3px rgba(52, 152, 219, 0.1);
}

/* Error state: red border */
.input.error {
  border-color: #e74c3c;
}
.input.error:focus {
  box-shadow: 0 0 0 3px rgba(231, 76, 60, 0.1);
}

/* Success state: green border */
.input.success {
  border-color: #27ae60;
}
.input.success:focus {
  box-shadow: 0 0 0 3px rgba(39, 174, 96, 0.1);
}

/* Disabled state */
.input:disabled {
  background-color: #ecf0f1;
  cursor: not-allowed;
}
```

---

### 5.4 Checkbox with Animation

**Checkbox that animates on check/uncheck.**

```html
<label class="checkbox-label">
  <input type="checkbox" class="checkbox-input">
  <span class="checkbox-box">
    <svg class="checkbox-checkmark" viewBox="0 0 24 24" width="16" height="16">
      <polyline points="20 6 9 17 4 12" stroke="white" stroke-width="2" fill="none"/>
    </svg>
  </span>
  <span class="checkbox-text">I agree to the terms</span>
</label>
```

```css
.checkbox-label {
  display: flex;
  align-items: center;
  gap: 8px;
  cursor: pointer;
  user-select: none;
}

.checkbox-input {
  display: none;
}

.checkbox-box {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 20px;
  height: 20px;
  border: 2px solid #bdc3c7;
  border-radius: 4px;
  background-color: white;
  transition: background-color 0.2s ease, border-color 0.2s ease;
}

/* Checkmark animation: scale from 0 to 1 on check */
.checkbox-checkmark {
  transform: scale(0) rotate(-45deg);
  transition: transform 0.2s cubic-bezier(0.4, 0, 0.2, 1);
}

/* Checked state */
.checkbox-input:checked + .checkbox-box {
  background-color: #3498db;
  border-color: #3498db;
}
.checkbox-input:checked + .checkbox-box .checkbox-checkmark {
  transform: scale(1) rotate(0deg);
}

/* Focus state */
.checkbox-input:focus + .checkbox-box {
  box-shadow: 0 0 0 3px rgba(52, 152, 219, 0.3);
}

.checkbox-text {
  font-size: 14px;
}
```

---

### 5.5 Loading States

**Three patterns for different scenarios.**

#### Pattern A: Spinner (indefinite)

```html
<div class="spinner"></div>
```

```css
@keyframes spin {
  from { transform: rotate(0deg); }
  to { transform: rotate(360deg); }
}

.spinner {
  display: inline-block;
  width: 40px;
  height: 40px;
  border: 3px solid rgba(52, 152, 219, 0.2);
  border-top-color: #3498db;
  border-radius: 50%;
  animation: spin 0.75s linear infinite;
}
```

#### Pattern B: Skeleton Screen (pulsing placeholder)

```html
<div class="skeleton-card">
  <div class="skeleton skeleton-header"></div>
  <div class="skeleton skeleton-text"></div>
  <div class="skeleton skeleton-text" style="width: 80%;"></div>
</div>
```

```css
@keyframes skeleton-pulse {
  0%, 100% {
    opacity: 1;
  }
  50% {
    opacity: 0.4;
  }
}

.skeleton {
  background-color: #ecf0f1;
  border-radius: 4px;
  animation: skeleton-pulse 1.5s ease-in-out infinite;
}

.skeleton-header {
  width: 100%;
  height: 200px;
  margin-bottom: 16px;
}

.skeleton-text {
  width: 100%;
  height: 16px;
  margin-bottom: 8px;
}
```

#### Pattern C: Progress Bar (deterministic)

```html
<!-- Deterministic: use when you know total time/items -->
<div class="progress-container">
  <div class="progress-bar" style="width: 65%;"></div>
  <span class="progress-text">65%</span>
</div>

<!-- Indeterminate: use when duration is unknown -->
<div class="progress-container">
  <div class="progress-bar-indeterminate"></div>
</div>
```

```css
/* Deterministic progress bar */
.progress-container {
  position: relative;
  height: 4px;
  background-color: #ecf0f1;
  border-radius: 2px;
  overflow: hidden;
}

.progress-bar {
  height: 100%;
  background-color: #3498db;
  transition: width 0.3s ease;
}

.progress-text {
  position: absolute;
  top: 100%;
  right: 0;
  margin-top: 4px;
  font-size: 12px;
  color: #7f8c8d;
}

/* Indeterminate progress bar (animated) */
@keyframes indeterminate {
  0% {
    left: -100%;
  }
  100% {
    left: 100%;
  }
}

.progress-bar-indeterminate {
  position: absolute;
  top: 0;
  left: 0;
  height: 100%;
  width: 30%;
  background: linear-gradient(90deg, transparent, #3498db, transparent);
  animation: indeterminate 1.5s ease-in-out infinite;
}
```

---

### 5.6 Toast Notifications

**Temporary feedback messages that auto-dismiss.**

```html
<div class="toast toast-success show" role="status" aria-live="polite">
  <svg class="toast-icon" viewBox="0 0 24 24" width="20" height="20">
    <circle cx="12" cy="12" r="10" fill="none" stroke="currentColor" stroke-width="2"/>
    <polyline points="16 12 12 8 8 12" stroke="currentColor" stroke-width="2" fill="none"/>
  </svg>
  <span class="toast-message">Settings saved successfully!</span>
  <button class="toast-close" aria-label="Close notification">&times;</button>
</div>
```

```css
.toast {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 12px 16px;
  border-radius: 4px;
  font-size: 14px;
  min-width: 300px;
  max-width: 500px;

  /* Initial state: slide up from bottom, fade in */
  transform: translateY(20px);
  opacity: 0;
  transition: transform 0.25s cubic-bezier(0.34, 1.56, 0.64, 1),
              opacity 0.25s ease;

  /* Position */
  position: fixed;
  bottom: 24px;
  left: 24px;
  z-index: 9999;
}

/* Show state: visible and positioned */
.toast.show {
  transform: translateY(0);
  opacity: 1;
}

/* Variants */
.toast-success {
  background-color: #d5f4e6;
  color: #27ae60;
  border-left: 4px solid #27ae60;
}

.toast-error {
  background-color: #fadbd8;
  color: #c0392b;
  border-left: 4px solid #c0392b;
}

.toast-warning {
  background-color: #fef5e7;
  color: #f39c12;
  border-left: 4px solid #f39c12;
}

.toast-info {
  background-color: #d6eaf8;
  color: #2980b9;
  border-left: 4px solid #2980b9;
}

.toast-icon {
  flex-shrink: 0;
}

.toast-message {
  flex: 1;
}

.toast-close {
  background: none;
  border: none;
  color: inherit;
  font-size: 20px;
  cursor: pointer;
  padding: 0;
  flex-shrink: 0;
}
```

```javascript
// Auto-dismiss functionality
function showToast(message, type = 'info', duration = 3000) {
  const toast = document.createElement('div');
  toast.className = `toast toast-${type}`;
  toast.innerHTML = `
    <span class="toast-message">${message}</span>
    <button class="toast-close" aria-label="Close">&times;</button>
  `;

  document.body.appendChild(toast);

  // Trigger animation
  requestAnimationFrame(() => {
    toast.classList.add('show');
  });

  // Auto-dismiss
  const timeout = setTimeout(() => {
    toast.classList.remove('show');
    setTimeout(() => toast.remove(), 250);
  }, duration);

  // Manual close
  toast.querySelector('.toast-close').addEventListener('click', () => {
    clearTimeout(timeout);
    toast.classList.remove('show');
    setTimeout(() => toast.remove(), 250);
  });

  return toast;
}

// Usage
showToast('Settings saved!', 'success', 3000);
showToast('Error saving file', 'error', 4000);
```

---

### 5.7 Card Hover (Desktop)

**Elevation and lift effect on hover.**

```html
<div class="card">
  <img src="image.jpg" alt="Card image">
  <h3>Card Title</h3>
  <p>Card description goes here.</p>
</div>
```

```css
.card {
  background-color: white;
  border-radius: 8px;
  padding: 16px;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.12), 0 1px 2px rgba(0, 0, 0, 0.08);
  transform: translateY(0);
  transition: box-shadow 0.2s ease, transform 0.2s ease;
}

/* Hover state: elevation grows, card lifts */
.card:hover {
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15), 0 8px 24px rgba(0, 0, 0, 0.12);
  transform: translateY(-4px);
}

/* Mobile: no hover effect (touch-first) */
@media (hover: none) {
  .card:hover {
    transform: translateY(0);
    box-shadow: 0 1px 3px rgba(0, 0, 0, 0.12), 0 1px 2px rgba(0, 0, 0, 0.08);
  }
}
```

---

### 5.8 Like / Favorite Animation

**Heart or star animation with overshoot for delight.**

#### Heart Animation

```html
<button class="like-btn" aria-label="Like" aria-pressed="false">
  <svg class="like-icon" viewBox="0 0 24 24" width="24" height="24">
    <path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"/>
  </svg>
  <span class="like-count">142</span>
</button>
```

```css
.like-btn {
  background: none;
  border: none;
  cursor: pointer;
  display: flex;
  align-items: center;
  gap: 6px;
  padding: 4px 8px;
  border-radius: 4px;
  transition: background-color 0.2s ease;
}

.like-btn:hover {
  background-color: rgba(231, 76, 60, 0.1);
}

.like-icon {
  width: 24px;
  height: 24px;
  stroke: #95a5a6;
  fill: none;
  stroke-width: 1.5;
  transition: fill 0.2s ease, stroke 0.2s ease, transform 0.35s cubic-bezier(0.34, 1.56, 0.64, 1);
}

/* Liked state: heart fills and bounces */
.like-btn.liked .like-icon {
  fill: #e74c3c;
  stroke: #e74c3c;
  animation: likePopOut 0.35s cubic-bezier(0.34, 1.56, 0.64, 1);
}

@keyframes likePopOut {
  0% {
    transform: scale(0.8);
  }
  50% {
    transform: scale(1.3);
  }
  100% {
    transform: scale(1);
  }
}

.like-count {
  font-size: 14px;
  color: #95a5a6;
  transition: color 0.2s ease;
}

.like-btn.liked .like-count {
  color: #e74c3c;
}
```

#### Star Animation

```html
<button class="star-btn" aria-label="Favorite" aria-pressed="false">
  <svg class="star-icon" viewBox="0 0 24 24" width="24" height="24">
    <path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/>
  </svg>
</button>
```

```css
.star-btn {
  background: none;
  border: none;
  cursor: pointer;
  padding: 4px;
  border-radius: 4px;
  transition: background-color 0.2s ease;
}

.star-btn:hover {
  background-color: rgba(241, 196, 15, 0.1);
}

.star-icon {
  width: 24px;
  height: 24px;
  fill: #bdc3c7;
  transition: fill 0.2s ease, transform 0.3s cubic-bezier(0.34, 1.56, 0.64, 1);
}

/* Starred state: fill changes to gold and rotates */
.star-btn.starred .star-icon {
  fill: #f39c12;
  animation: starSpin 0.3s cubic-bezier(0.34, 1.56, 0.64, 1);
}

@keyframes starSpin {
  0% {
    transform: rotate(-20deg) scale(0.8);
  }
  100% {
    transform: rotate(0deg) scale(1);
  }
}
```

---

### 5.9 Form Validation (Inline)

**Real-time validation with clear error/success states.**

```html
<form class="form">
  <div class="form-group">
    <label for="email">Email Address</label>
    <input
      id="email"
      type="email"
      class="input"
      placeholder="you@example.com"
      required
    >
    <span class="form-icon"></span>
    <span class="form-error" role="alert"></span>
  </div>

  <div class="form-group">
    <label for="password">Password</label>
    <input
      id="password"
      type="password"
      class="input"
      placeholder="••••••••"
      minlength="8"
      required
    >
    <span class="form-icon"></span>
    <span class="form-error" role="alert"></span>
  </div>

  <button type="submit" class="btn btn-primary">Sign Up</button>
</form>
```

```css
.form-group {
  display: flex;
  flex-direction: column;
  gap: 4px;
  margin-bottom: 16px;
  position: relative;
}

label {
  font-size: 14px;
  font-weight: 600;
  color: #2c3e50;
}

.input {
  padding: 10px 12px;
  padding-right: 32px; /* space for icon */
  border: 1px solid #bdc3c7;
  border-radius: 4px;
  font-size: 14px;
  font-family: inherit;
  transition: border-color 0.15s ease, box-shadow 0.15s ease;
}

.input:hover {
  border-color: #95a5a6;
}

.input:focus {
  outline: none;
  border-color: #3498db;
  box-shadow: 0 0 0 3px rgba(52, 152, 219, 0.1);
}

/* Form icon (checkmark or error) */
.form-icon {
  position: absolute;
  right: 12px;
  top: 32px;
  width: 20px;
  height: 20px;
  display: flex;
  align-items: center;
  justify-content: center;
  opacity: 0;
  transition: opacity 0.2s ease;
  pointer-events: none;
}

.form-icon::before {
  font-size: 16px;
}

/* Success state: green checkmark */
.input.success + .form-icon {
  opacity: 1;
  color: #27ae60;
}
.input.success + .form-icon::before {
  content: "✓";
}

/* Error state: red X */
.input.error + .form-icon {
  opacity: 1;
  color: #e74c3c;
}
.input.error + .form-icon::before {
  content: "✕";
}

/* Error message */
.form-error {
  display: block;
  font-size: 12px;
  color: #e74c3c;
  max-height: 0;
  overflow: hidden;
  transition: max-height 0.2s ease, opacity 0.2s ease;
  opacity: 0;
}

.input.error {
  border-color: #e74c3c;
}
.input.error:focus {
  box-shadow: 0 0 0 3px rgba(231, 76, 60, 0.1);
}
.input.error ~ .form-error {
  max-height: 50px;
  opacity: 1;
}

/* Validation trigger: on blur (when user leaves field) */
.input {
  /* validation happens via JavaScript */
}
```

```javascript
const form = document.querySelector('.form');

form.querySelectorAll('.input').forEach(input => {
  input.addEventListener('blur', () => {
    validateField(input);
  });

  input.addEventListener('input', () => {
    // Remove error state while typing (only keep on blur)
    if (input.classList.contains('error')) {
      input.classList.remove('error');
    }
  });
});

function validateField(input) {
  const value = input.value.trim();
  const error = input.nextElementSibling.nextElementSibling;

  let isValid = false;
  let errorMessage = '';

  if (input.type === 'email') {
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    isValid = emailRegex.test(value);
    errorMessage = 'Please enter a valid email address';
  } else if (input.type === 'password') {
    isValid = value.length >= 8;
    errorMessage = 'Password must be at least 8 characters';
  }

  if (!value) {
    input.classList.remove('success', 'error');
    error.textContent = '';
  } else if (isValid) {
    input.classList.remove('error');
    input.classList.add('success');
    error.textContent = '';
  } else {
    input.classList.remove('success');
    input.classList.add('error');
    error.textContent = errorMessage;
  }
}
```

**Key principle:** Validate on blur, not on keystroke. Too much real-time validation is annoying.

---

### 5.10 Accordion / Collapsible

**Expand/collapse content with smooth animation.**

```html
<div class="accordion">
  <button class="accordion-trigger" aria-expanded="false" aria-controls="panel1">
    What is this product?
    <svg class="accordion-icon" viewBox="0 0 24 24" width="20" height="20">
      <polyline points="6 9 12 15 18 9" stroke="currentColor" stroke-width="2" fill="none"/>
    </svg>
  </button>
  <div id="panel1" class="accordion-content" hidden>
    <div class="accordion-body">
      This product is designed to help you accomplish amazing things.
    </div>
  </div>
</div>

<div class="accordion">
  <button class="accordion-trigger" aria-expanded="false" aria-controls="panel2">
    How does it work?
    <svg class="accordion-icon" viewBox="0 0 24 24" width="20" height="20">
      <polyline points="6 9 12 15 18 9" stroke="currentColor" stroke-width="2" fill="none"/>
    </svg>
  </button>
  <div id="panel2" class="accordion-content" hidden>
    <div class="accordion-body">
      It works by combining machine learning with user feedback...
    </div>
  </div>
</div>
```

```css
.accordion {
  border-bottom: 1px solid #ecf0f1;
}

.accordion:last-child {
  border-bottom: none;
}

.accordion-trigger {
  display: flex;
  align-items: center;
  justify-content: space-between;
  width: 100%;
  padding: 16px;
  background: none;
  border: none;
  text-align: left;
  font-size: 14px;
  font-weight: 600;
  cursor: pointer;
  transition: background-color 0.2s ease;
}

.accordion-trigger:hover {
  background-color: #f8f9fa;
}

.accordion-trigger:focus {
  outline: none;
  background-color: #ecf0f1;
}

/* Chevron icon rotates when open */
.accordion-icon {
  flex-shrink: 0;
  transition: transform 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}

.accordion-trigger[aria-expanded="true"] .accordion-icon {
  transform: rotate(180deg);
}

/* Content container: smooth expand/collapse */
.accordion-content {
  max-height: 0;
  overflow: hidden;
  transition: max-height 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}

.accordion-content[aria-expanded="true"] {
  max-height: 1000px; /* set higher than expected content */
}

.accordion-body {
  padding: 0 16px 16px 16px;
  font-size: 14px;
  line-height: 1.6;
  color: #7f8c8d;
}
```

```javascript
document.querySelectorAll('.accordion-trigger').forEach(button => {
  button.addEventListener('click', () => {
    const isOpen = button.getAttribute('aria-expanded') === 'true';
    const contentId = button.getAttribute('aria-controls');
    const content = document.getElementById(contentId);

    // Toggle state
    button.setAttribute('aria-expanded', !isOpen);
    content.hidden = !content.hidden;

    // For CSS animation, we also need to toggle on the content
    content.setAttribute('aria-expanded', !isOpen);
  });
});
```

---

## 6. Skeleton Screens vs Spinners

**When to use what:**

| Scenario | Use | Why |
|----------|-----|-----|
| Loading content with known shape | Skeleton Screen | Familiar layout reduces perceived wait time |
| Loading unknown content | Spinner | Shows activity without committing to shape |
| Filling form fields | Skeleton | Matches content structure |
| Fetching notifications | Spinner | Quick operation, small amount |
| Loading article/blog post | Skeleton | Matches article shape (image, headline, text) |
| Uploading file | Progress bar + Spinner | Shows progress when duration is unknown |

### Skeleton Screen Best Practice

```html
<!-- Match the exact layout of the content you're loading -->
<div class="card-skeleton">
  <div class="skeleton skeleton-image"></div>
  <div class="skeleton skeleton-title"></div>
  <div class="skeleton skeleton-text"></div>
  <div class="skeleton skeleton-text" style="width: 85%;"></div>
</div>
```

```css
@keyframes skeleton-pulse {
  0%, 100% {
    opacity: 1;
  }
  50% {
    opacity: 0.4;
  }
}

.skeleton {
  background: linear-gradient(
    90deg,
    #f0f0f0 25%,
    #e0e0e0 50%,
    #f0f0f0 75%
  );
  background-size: 200% 100%;
  animation: skeleton-pulse 1.5s ease-in-out infinite;
  border-radius: 4px;
}

.skeleton-image {
  width: 100%;
  height: 200px;
  margin-bottom: 16px;
  border-radius: 8px;
}

.skeleton-title {
  width: 60%;
  height: 20px;
  margin-bottom: 12px;
}

.skeleton-text {
  width: 100%;
  height: 14px;
  margin-bottom: 8px;
}
```

---

## 7. Page/Screen Transitions

**How screens change with animation.**

### 7.1 Fade Transition (Universal)

```html
<div class="page page-home active">
  <!-- Home page content -->
</div>

<div class="page page-about">
  <!-- About page content -->
</div>
```

```css
.page {
  opacity: 0;
  transition: opacity 0.2s ease;
  pointer-events: none;
}

.page.active {
  opacity: 1;
  pointer-events: auto;
}
```

**When to use:** Always safe, works for any transition.

### 7.2 Slide Transition (Drill-down Navigation)

```css
.page {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  transform: translateX(100%);
  transition: transform 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  pointer-events: none;
}

.page.active {
  transform: translateX(0);
  pointer-events: auto;
}

/* Going back slides right */
.page.prev {
  transform: translateX(-100%);
}
```

**When to use:** Hierarchical navigation (back/forward through pages).

### 7.3 Scale + Fade Transition (Modals)

```css
.modal {
  position: fixed;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%) scale(0.95);
  opacity: 0;
  transition: transform 0.3s cubic-bezier(0.34, 1.56, 0.64, 1),
              opacity 0.3s ease;
  pointer-events: none;
}

.modal.show {
  transform: translate(-50%, -50%) scale(1);
  opacity: 1;
  pointer-events: auto;
}
```

**When to use:** Dialog boxes, modals, bottom sheets.

### 7.4 What NOT to Do

```css
/* ❌ AVOID: 3D flips */
.page {
  transform: rotateY(90deg); /* disorienting */
}

/* ❌ AVOID: Complex carousel rotations */
.page {
  transform: rotateX(360deg); /* breaks spatial awareness */
}

/* ❌ AVOID: Excessive motion */
.page {
  animation: swirl 1s ease; /* confusing and slow */
}

/* ✓ STICK TO: Simple, predictable transitions */
.page {
  opacity: 0;
  transform: translateX(100%);
  transition: opacity 0.3s ease, transform 0.3s ease;
}
```

---

## 8. Motion Principles

### 8.1 Easing Functions

Easing controls the acceleration curve of animations.

```css
/* EASE-OUT: Elements entering the view (decelerates) */
.element-enter {
  animation: slideIn 0.3s ease-out;
}
@keyframes slideIn {
  from { transform: translateX(100%); }
  to { transform: translateX(0); }
}

/* EASE-IN: Elements leaving the view (accelerates) */
.element-exit {
  animation: slideOut 0.3s ease-in;
}
@keyframes slideOut {
  from { transform: translateX(0); }
  to { transform: translateX(-100%); }
}

/* EASE-IN-OUT: General transitions (gentle curve) */
.element-transition {
  transition: opacity 0.2s ease-in-out;
}

/* CUSTOM CUBIC-BEZIER: Custom acceleration (Material Design) */
.element-material {
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}
```

### 8.2 Duration Rules

```css
/* Small, local elements: 150-200ms */
.button { transition: background-color 0.15s ease; }
.input:focus { transition: border-color 0.15s ease; }

/* Medium, important elements: 200-300ms */
.card:hover { transition: box-shadow 0.2s ease; }
.toggle { transition: transform 0.2s ease; }

/* Large, expressive changes: 300-500ms */
.modal-open { animation: slideUp 0.3s ease-out; }
.page-transition { transition: opacity 0.3s ease; }

/* Progress indicators: 500ms+ */
.spinner { animation: spin 0.75s linear infinite; }
.progress-bar { animation: indeterminate 1.5s ease-in-out infinite; }
```

### 8.3 Direction Principle

Elements should arrive from the direction of their trigger.

```css
/* Button at bottom → toast rises from bottom */
.toast {
  transform: translateY(20px); /* coming from bottom */
  opacity: 0;
}
.toast.show {
  transform: translateY(0);
  opacity: 1;
}

/* Navigation from left → content slides in from left */
.sidebar-open .content {
  transform: translateX(0);
}

/* Clicking element → expand from that point */
.dropdown {
  transform-origin: top center; /* expands down from button */
  transform: scaleY(0);
}
.dropdown.show {
  transform: scaleY(1);
}
```

### 8.4 No Animation Should Block

```css
/* ✓ CORRECT: Animation doesn't prevent interaction */
button {
  transition: background-color 0.2s ease;
  /* user can click and interact */
}

/* ❌ WRONG: Animation blocks interaction */
button {
  pointer-events: none; /* blocks clicks! */
  animation: spin 1s ease;
}

/* ✓ CORRECT: Animation plays but user can interact */
.overlay {
  animation: fadeIn 0.3s ease;
  /* can still close, click, interact */
}
```

---

## 9. RTL (Right-to-Left) Microinteractions

**For Arabic, Hebrew, and other RTL languages.**

### 9.1 Slide Animations in RTL

```css
/* LTR: slide from right */
.toast {
  transform: translateX(100%);
  transition: transform 0.3s ease;
}
.toast.show {
  transform: translateX(0);
}

/* RTL: slide from left (mirror) */
[dir="rtl"] .toast {
  transform: translateX(-100%);
}
[dir="rtl"] .toast.show {
  transform: translateX(0);
}
```

### 9.2 Detect RTL in JavaScript

```javascript
const isRTL = document.documentElement.dir === 'rtl' ||
              window.getComputedStyle(document.body).direction === 'rtl';

// Use direction in calculations
const translateDistance = isRTL ? -100 : 100;
element.style.transform = `translateX(${translateDistance}%)`;
```

### 9.3 Swipe Gestures in RTL

```javascript
const minSwipeDistance = 50;
let touchStartX = 0;
let touchEndX = 0;

document.addEventListener('touchstart', e => {
  touchStartX = e.changedTouches[0].screenX;
});

document.addEventListener('touchend', e => {
  touchEndX = e.changedTouches[0].screenX;
  handleSwipe();
});

function handleSwipe() {
  const distance = touchEndX - touchStartX;
  const isRTL = document.documentElement.dir === 'rtl';

  // Swipe directions are mirrored in RTL
  if (isRTL) {
    if (distance > minSwipeDistance) {
      // RTL: swipe left in UI = swipe right in logic
      goToNext();
    } else if (distance < -minSwipeDistance) {
      goToPrevious();
    }
  } else {
    if (distance > minSwipeDistance) {
      goToPrevious();
    } else if (distance < -minSwipeDistance) {
      goToNext();
    }
  }
}
```

---

## 10. prefers-reduced-motion (MANDATORY)

**Respect users with vestibular disorders who are sensitive to motion.**

```css
/* Default: full animations */
.button {
  transition: background-color 0.2s ease;
}

.modal {
  animation: slideIn 0.3s ease;
}

/* Reduced motion: remove animations */
@media (prefers-reduced-motion: reduce) {
  *,
  *::before,
  *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
    scroll-behavior: auto !important;
  }
}
```

**Why this matters:** Users with vestibular disorders experience motion sickness from animations. This setting respects their accessibility needs.

**Implementation in JavaScript:**

```javascript
const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

if (prefersReducedMotion) {
  // Skip complex animations
  element.classList.add('no-animation');
} else {
  // Use full animations
  element.classList.add('with-animation');
}
```

---

## 11. Microinteractions Checklist

**Before delivering your project, verify all microinteractions work correctly:**

### Interactive Elements
- [ ] All buttons have `hover`, `active`, and `disabled` states
- [ ] Button states have clear visual distinction (color, shadow, scale)
- [ ] Focus states are visible and keyboard-accessible
- [ ] Active state provides tactile feedback (scale or shadow change)
- [ ] Disabled buttons show clear disabled appearance and have `cursor: not-allowed`

### Form Elements
- [ ] Input focus state has visible focus ring (3px color ring)
- [ ] Form validation triggers on `blur`, not on keystroke
- [ ] Error messages fade in smoothly with max-height animation
- [ ] Success state shows checkmark icon
- [ ] Error state shows error icon and red border
- [ ] Field validation is accessible (aria-invalid, role="alert")

### Loading States
- [ ] Every async action has a loading state (spinner or skeleton)
- [ ] Spinner rotates smoothly (0.75s per revolution)
- [ ] Skeleton screens match actual content layout
- [ ] Progress bars show for long operations (>500ms)
- [ ] Progress bars are visible to all users, never silent

### Feedback & Notifications
- [ ] Success feedback appears within 100ms
- [ ] Error feedback appears within 100ms
- [ ] Toast notifications auto-dismiss after appropriate time
  - Info: 3000ms
  - Success: 3000ms
  - Error: 4000-5000ms (longer, user may need to read)
- [ ] Toasts have close button for manual dismissal
- [ ] Toasts have proper ARIA attributes (`role="status"`, `aria-live="polite"`)

### Animations
- [ ] All animations respect `prefers-reduced-motion`
- [ ] Animations don't block user interaction
- [ ] Transition timing is appropriate (not too fast, not too slow)
  - Small elements: 150-200ms
  - Medium elements: 200-300ms
  - Large elements: 300-500ms
- [ ] Easing functions are natural (ease, ease-out, ease-in-out)
- [ ] Page transitions are smooth and predictable

### Accessibility
- [ ] All interactive elements have `:focus` states
- [ ] Focus rings are visible (min 2px, contrast ratio 3:1)
- [ ] ARIA attributes reflect state changes (aria-pressed, aria-expanded, aria-busy)
- [ ] Keyboard navigation works (Tab, Enter, Space)
- [ ] Toasts use `aria-live="polite"` for screen readers

### RTL Support (if applicable)
- [ ] Slide animations mirror direction in RTL
- [ ] Icons rotate correctly in RTL
- [ ] Transform values use logical properties or RTL overrides
- [ ] Swipe gestures are reversed in RTL

### Mobile Considerations
- [ ] Touch targets are at least 44x44px
- [ ] Hover effects don't trigger on touch devices
- [ ] Animations are smooth at 60fps (watch for jank)
- [ ] No 3D transforms that cause rendering issues
- [ ] Haptic feedback works on supported devices

---

## 12. Implementation Tips

### Use CSS Variables for Consistent Timing

```css
:root {
  --duration-fast: 150ms;
  --duration-normal: 250ms;
  --duration-slow: 350ms;

  --easing-in: cubic-bezier(0.4, 0, 1, 1);
  --easing-out: cubic-bezier(0, 0, 0.2, 1);
  --easing-in-out: cubic-bezier(0.4, 0, 0.2, 1);
}

.button {
  transition: background-color var(--duration-fast) var(--easing-in-out);
}

.modal {
  animation: slideIn var(--duration-normal) var(--easing-out);
}
```

### Group Related Animations

```css
/* Good: related properties animated together */
.card {
  transition:
    box-shadow var(--duration-normal) var(--easing-out),
    transform var(--duration-normal) var(--easing-out);
}

/* Bad: inconsistent timing */
.card {
  transition:
    box-shadow 0.2s ease,
    transform 0.5s ease; /* different durations confuse users */
}
```

### Test Animations at Reduced Motion

```bash
# macOS: System Preferences → Accessibility → Display → Reduce motion
# Windows: Settings → Ease of Access → Display → Show animations
# Linux: GNOME Settings → Accessibility → Animations (Off)
```

In DevTools, you can simulate:
```javascript
// Chrome DevTools Console
matchMedia('(prefers-reduced-motion: reduce)').matches // true or false
```

---

## Quick Reference: Essential Code Snippets

### Button with All States
```css
.btn {
  padding: 8px 16px;
  border: none;
  border-radius: 4px;
  background-color: #3498db;
  color: white;
  cursor: pointer;
  transition: all 0.15s ease;
}
.btn:hover { background-color: #2980b9; }
.btn:active { background-color: #1f618d; transform: scale(0.97); }
.btn:focus { box-shadow: 0 0 0 3px rgba(52, 152, 219, 0.3); }
.btn:disabled { background-color: #ecf0f1; cursor: not-allowed; }
```

### Input Focus Ring
```css
input {
  border: 1px solid #bdc3c7;
  border-radius: 4px;
  transition: border-color 0.15s ease, box-shadow 0.15s ease;
}
input:focus {
  outline: none;
  border-color: #3498db;
  box-shadow: 0 0 0 3px rgba(52, 152, 219, 0.1);
}
```

### Spinner
```css
@keyframes spin { to { transform: rotate(360deg); } }
.spinner {
  border: 3px solid rgba(52, 152, 219, 0.2);
  border-top-color: #3498db;
  border-radius: 50%;
  width: 40px;
  height: 40px;
  animation: spin 0.75s linear infinite;
}
```

### Toast Notification
```css
.toast {
  transform: translateY(20px);
  opacity: 0;
  transition: transform 0.25s cubic-bezier(0.34, 1.56, 0.64, 1), opacity 0.25s ease;
}
.toast.show {
  transform: translateY(0);
  opacity: 1;
}
```

### prefers-reduced-motion
```css
@media (prefers-reduced-motion: reduce) {
  * {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
  }
}
```

---

## References

- **Dan Saffer, "Microinteractions"** — The foundational framework for this guide
- **Material Design Motion** — Google's animation principles
- **Web Animations Working Group** — W3C specifications
- **MDN: CSS Transitions & Animations** — Browser compatibility and best practices
- **WebAIM: Keyboard Accessibility** — Making interactions accessible

---

## Advanced Animation Physics (Modern Standards)

These rules reflect physics-based animation principles from iOS, Material You, and modern design systems. Apply whenever motion is present.

### Spring Physics — Replace Linear/Ease with Springs

Spring-based animations feel alive because they mimic real-world physics. CSS cubic-bezier approximations:

```css
/* Bouncy entry — elements appearing or expanding */
--spring-bouncy: cubic-bezier(0.34, 1.56, 0.64, 1);

/* Standard enter — confident without bounce */
--spring-enter: cubic-bezier(0.22, 1, 0.36, 1);

/* Exit — always faster than enter, no bounce on exit */
--spring-exit: cubic-bezier(0.4, 0, 1, 1);

/* Overshoot for emphasis (button press, success states) */
--spring-overshoot: cubic-bezier(0.175, 0.885, 0.32, 1.275);
```

**Rule: exits are always faster than enters.** Enter: 200–350ms. Exit: 100–200ms. This mirrors how attention works — we watch things arrive, not leave.

### Shared-Element Transitions

When a user taps a card to open a detail view, the card element should visually transform INTO the detail view:

```css
/* Mark the origin element */
.card { view-transition-name: card-item-1; }

/* Mark the destination element */
.detail-header { view-transition-name: card-item-1; }

/* CSS View Transitions API morphs automatically */
@view-transition { navigation: auto; }
```

If View Transitions API is unavailable, simulate with transform + clip-path:
1. Capture card position with getBoundingClientRect()
2. Position clone at card coordinates absolutely
3. Animate clone to detail view position/size over 300ms
4. Fade out clone, fade in real detail view

**When to use**: card → detail, thumbnail → full image, list item → expanded panel. Always apply when the destination is visually derived from the tapped element.

### Stagger Sequences (List Entry Animation)

Lists entering simultaneously feel like a "dump." Stagger them:

```css
/* Apply delay increment per item */
.list-item { animation-delay: calc(var(--index, 0) * 40ms); }
```

```js
// Set --index via JavaScript
document.querySelectorAll('.list-item')
  .forEach((el, i) => el.style.setProperty('--index', i));
```

**Rules for stagger:**
- Interval: 30–50ms per item (less = subtle, more = theatrical)
- Max items to stagger: 8–10 (beyond that, delay becomes annoying)
- Direction: top-to-bottom for vertical lists, left-to-right for grids
- Only on page load or first appearance — don't restagger on every re-render

### Interruptible Animations

Animations must be interruptible. A user who taps again during a transition should not wait for it to finish:

```css
/* Transitions are naturally interruptible — prefer them over keyframe animations */
.drawer {
  transform: translateX(-100%);
  transition: transform 280ms var(--spring-enter);
}
.drawer.open { transform: translateX(0); }
/* Toggling .open mid-transition reverses gracefully */
```

For JavaScript animations (GSAP, Framer Motion), always call .kill() / .stop() before starting a new animation on the same element.

### Hierarchy Motion — Important Elements Move First

When multiple elements animate simultaneously, prioritize by importance:

```
Priority order:
1. Primary action / headline     → 0ms delay (immediate)
2. Supporting content            → 60–80ms delay
3. Decorative / background       → 120–160ms delay
```

The eye follows the sequence — visual narrative guides attention to what matters.

### Opacity Threshold Rule

Never let elements linger below 15% opacity. Anything near-invisible still costs rendering:

```css
.fading-out {
  opacity: 0;
  transition: opacity 150ms ease-out;
  pointer-events: none;
}
/* Set visibility:hidden or display:none once opacity reaches 0 */
```

### Modal Motion Pattern

Modals convey gravity — they require deliberate, calm motion:

```css
/* Backdrop fade */
.modal-backdrop { opacity: 0; transition: opacity 200ms ease-out; }
.modal-backdrop.open { opacity: 1; }

/* Panel — enter from slightly below, subtle scale */
.modal-panel {
  transform: translateY(16px) scale(0.97);
  opacity: 0;
  transition: transform 280ms var(--spring-enter), opacity 200ms ease-out;
}
.modal-panel.open { transform: translateY(0) scale(1); opacity: 1; }

/* Exit — faster, downward, no bounce */
.modal-panel.closing {
  transform: translateY(8px) scale(0.98);
  opacity: 0;
  transition: transform 180ms var(--spring-exit), opacity 150ms ease-in;
}
```

Scale rule: enter from 0.95–0.97 (subtle zoom), exit to 0.97–0.98. Large scale jumps feel childish.

### Animation Audit Checklist (Before Handoff)

```
□ All enters use spring-enter or spring-bouncy
□ All exits are faster than their corresponding enters
□ Lists with 3+ items use stagger (30–50ms interval)
□ Shared-element transitions on card→detail flows
□ No opacity below 0.15 lingering after animation ends
□ All animations are interruptible mid-play
□ Important content animates before decorative content
□ prefers-reduced-motion disables all transitions ≥ 100ms
□ No animation runs on the main thread — use transform + opacity only
□ Exit animations set pointer-events:none and cleanup with visibility:hidden
```

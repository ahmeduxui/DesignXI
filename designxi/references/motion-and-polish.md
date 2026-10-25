# Motion & Polish — animation, performance, and the invisible details

The difference between a design that looks finished in a static mockup and one that *feels* finished when
you use it. This file carries four things that all live at the same stage of the work — late, after the
screens exist — and that an AI left to its defaults gets wrong in the same predictable ways:

1. **Motion decisions** — whether a thing should animate at all, and if so with what.
2. **Performance budget** — keeping motion at 60fps instead of janky.
3. **UI polish** — the small craft details that read as "made by someone who cared."
4. **Web-on-mobile fixes** — the native-feel bugs every web app hits on a real phone.

Based on the `animate`, `animation-performance`, `review-animations`, `animation-vocabulary`,
`emil-design-eng`, and `mobile-native` methods.

**Where it runs in the 27-phase flow:**
- **Phase 18 (interactive prototype / motion)** — the motion decision order + performance budget below are
  the gate for every transition and microinteraction specified here. Name each motion by its exact term
  (vocabulary table). Pairs with `references/microinteractions.md`.
- **Phase 17 (self-critique)** — run the 10-block motion review; each block is a finding to fix, in a
  dedicated motion axis, before Phase 18 ships.
- **Phase 16 (responsive & RTL)** — the web-on-mobile section is the checklist for "does this actually feel
  right on a phone," not just "does it fit 320px."
- **Phases 14–15 (UI design)** — the polish section is a pass over each hi-fi screen before self-critique.
- **Phase 25 (handoff)** — use the vocabulary table so every interaction spec names the exact motion.
- **Phase 24 (delivery)** — if the build needs a library (toasts, dnd, charts, virtualization), name it here
  rather than letting the dev reach for the first npm result; see the pick-ui-library line at the bottom.

---

## 1. Motion — the decision order

Run these in order. Steps 1 and 2 gate everything; don't reach for a curve before you know whether it
animates at all. The goal of step 1 is sometimes **zero animation** — that's a success, not a dodge.

**1. Should this animate at all?** Keyboard-initiated and high-frequency actions are a disqualifier, not a
judgment call — something opened hundreds of times a day (a command palette, a frequently-toggled panel)
is better with no open/close animation. Animate to *serve* the user, never to decorate.

**2. What is the purpose?** It must be one of: feedback (the interface heard you), spatial consistency
(where something came from or went), state indication (a change made legible), preventing a jarring jump
(bridging content that would otherwise teleport), explanation (onboarding/marketing only), or delight
(allowed *only* at the rare / first-time tier). No purpose → back to step 1.

**3. Pick the cheapest tool that works.** CSS transition < CSS animation < a spring/JS library. Don't pull
in a motion library for a fade.

**4. Pick the properties — `transform` and `opacity` only.** They skip layout and paint and run on the GPU.
`width`/`height`/`margin`/`padding`/`top`/`left` trigger all three and drop frames (`clip-path` is the
sanctioned fourth; `height` is tolerated only for accordions). Never `scale(0)` — start from
`scale(0.9–0.97)` + `opacity:0`; nothing in the real world appears from nothing. Put `transform-origin` at
the trigger for popovers/dropdowns/menus/tooltips; modals stay centered. Prefer `translate()` percentages
(relative to the element's own size) over hardcoded pixels.

**5. Easing and duration — or a spring.** Never `ease-in` on UI: it delays the exact moment the user is
watching; `ease-out` at 200ms *feels* faster than `ease-in` at 200ms. **UI animations stay under 300ms** —
a 180ms dropdown feels more responsive than a 400ms one. Reach for a **spring** instead when the motion is
a drag with momentum, something that should feel alive, or a gesture the user can interrupt or reverse.

**6. Interruption and exit.** Use transitions (not keyframes) for anything a user can fire twice a second —
transitions retarget from the current value, keyframes restart from zero. **Exit the way you entered** — a
toast that slid in from the bottom leaves through the bottom; symmetric paths make swipe-to-dismiss obvious.

**7. Reduced motion + pointer gating ship with the animation**, not as a follow-up — `@media (prefers-reduced-motion: reduce)`
and hover effects gated to `(hover: hover)`.

**No approximated values.** Reuse the project's existing `--ease-*` and duration tokens; if none exist,
define a small scale once (e.g. ease-out `cubic-bezier(0.16,1,0.3,1)`, durations 150/200/300ms) and reuse it.

---

## 2. Performance budget

- **The budget is ~16ms per frame** for 60fps (~8ms for 120Hz). Everything in a frame — JS, style, layout,
  paint, composite — shares it.
- **Composite-only properties are free-ish**: `transform` and `opacity` can be handled by the compositor
  without relayout/repaint. This is the same rule as motion step 4, stated as a performance law.
- **`will-change` is a loan, not a gift.** Add it just before an animation starts and remove it after;
  leaving it on many elements wastes memory and can make things *slower*. Don't blanket-apply it.
- **Animate a handful of elements, not a list of 200.** For long lists, animate the container or a few
  in-view items; never stagger-animate an entire virtualized list.
- **Measure, don't guess.** If motion feels janky, it's almost always a non-composite property
  (width/top/box-shadow/filter) or layout thrash in a loop — find it in DevTools' Performance panel rather
  than adding more animation.

---

## 3. UI polish — the invisible details

A pass over each hi-fi screen. None of these change the layout; together they're the gap between "AI-default"
and "someone made this."

- **Optical over mathematical.** Centering a play-triangle or an arrow by its bounding box looks off-center —
  nudge it to where the eye reads center. Icon-in-a-circle usually needs a 1–2px optical adjustment.
- **Nested radii are concentric.** An inner element's corner radius = outer radius − the padding between
  them. Mismatched radii are a top AI tell.
- **Borders and shadows do different jobs.** A 1px border at low contrast defines an edge; a soft shadow
  implies elevation. Don't use a heavy shadow where the design just needs a hairline separator.
- **Hover/active/focus are designed states, not afterthoughts.** Every interactive element gets a visible
  focus ring (keyboard), a hover change (pointer only), and an active/pressed state. Feedback on *press*,
  not release, reads as instant.
- **Disabled isn't just greyed.** Say *why* when it matters (a tooltip), and keep the label legible.
- **Empty, loading, and error states are first-class** — the skeleton matches the final layout so nothing
  shifts; the error says what to do next, not just "something went wrong."
- **Tabular numbers for anything that changes or aligns** (`font-variant-numeric: tabular-nums`) so figures
  don't jitter.
- **Spacing is a rhythm, not a pile of one-offs.** Reuse the spacing scale; equal optical gaps beat equal
  measured gaps when visual weights differ.
- **One real detail that rewards attention** — a considered empty state, a satisfying check animation, a
  thoughtful microcopy line. Earned delight (motion step 2), never decoration.

---

## 4. Web-on-mobile — the native-feel fixes

A web app that's correct in desktop Chrome still feels wrong on a real phone until these are handled. Matched
by symptom; most can be specced from the design, but the ones marked **(phone)** must be confirmed on hardware.

- **Hover stuck after tap** → gate hover to `@media (hover: hover)`; touch devices otherwise keep the hover
  style after the finger lifts.
- **Grey/blue flash on tap** → `-webkit-tap-highlight-color: transparent`, then style `:active` yourself.
- **Wrong height / `100vh` too tall** → `100vh` includes the browser chrome on mobile; use `100dvh` (dynamic
  viewport) or `svh`/`lvh` as needed.
- **Page zooms into the input on focus (iOS)** → form inputs need `font-size: 16px` minimum; below that iOS
  Safari auto-zooms.
- **Tap feels laggy** → `touch-action: manipulation` to drop the legacy 300ms double-tap-zoom wait; respond
  on `pointerdown`/`:active`, not `click`.
- **Pull-to-refresh hijacks scroll** → `overscroll-behavior-y: contain` on scroll containers that shouldn't
  trigger it.
- **Content under the notch / home indicator** → `viewport-fit=cover` + `env(safe-area-inset-*)` padding.
- **Long-press selects button text** → `user-select: none` on buttons and controls (keep it *on* for content).
- **Carousel scrolls vertically instead of horizontally** → `touch-action: pan-x` (or `pan-y`) to lock the axis.
- **Status bar colour doesn't match** → `theme-color` meta / PWA manifest; **(phone)** confirm in standalone mode.
- **"Right in Chrome, wrong on the phone"** → **(phone)** test on a real, few-years-old device, with the
  keyboard open, once in landscape, and as an installed PWA if that's a target. Standalone mode changes
  viewport, safe areas, and status bar.

Report web-on-mobile findings as: symptom → one-line why → the file + declaration that changes → and flag
which items still need a physical phone to verify.

---

## Review pass — the 10 motion blocks (Phase 17)

Before a prototype ships, review every animation against these. Any one of them is a **block**, not a
nitpick — report it as a finding with the fix, in the self-critique's motion axis. Based on `review-animations`.

1. **Unjustified motion** — can't name the purpose (feedback / spatial / state / prevent-jar / explain),
   or "looks cool" on something seen often. → delete it.
2. **Frequency mismatch** — animation on a keyboard shortcut, command palette, or 100+/day action. → delete.
3. **`ease-in` on UI**, or a weak built-in easing on a deliberate animation. → `ease-out` / custom curve.
4. **Over 300ms on a UI element** with no stated reason. → shorten.
5. **`scale(0)` or a pure fade with no initial transform** / wrong `transform-origin` on a trigger-anchored
   popover. → `scale(0.95)`+opacity, origin at the trigger.
6. **Keyframes on rapidly-fired motion** (toasts, toggles, drags) that restart from zero. → transitions/springs.
7. **Animating layout properties** (`width`/`height`/`margin`/`top`/`left`) or shorthand `x`/`y`/`scale`
   under load. → `transform`/`opacity`.
8. **Missing `prefers-reduced-motion`**, or ungated `:hover` motion. → add both.
9. **Symmetric timing on a press-and-release or hold** interaction. → slow the deliberate phase, snap the response.
10. **Everything-at-once entrance** where a 30–80ms stagger belongs. → stagger the group.

Remedial order when fixing: delete → reduce → fix easing → fix origin/physicality → make interruptible →
move to GPU → asymmetric timing → polish → accessibility & cohesion.

---

## Motion vocabulary — name it precisely (Phases 18, 25)

Specifying "it fades up a bit" invites guesswork; naming the exact term makes the handoff unambiguous and
the implementation match the intent. Use these in `microinteractions.md` and the handoff. Based on `animation-vocabulary`.

| Say this | Not "it just…" |
|---|---|
| **Scale-in** (grow + fade) / **Pop-in** (slight overshoot) / **Reveal** (clip-path/mask) | "appears" |
| **Slide-in** (from an edge) / **Crossfade** (one out as one in, same spot) | "shows up / swaps" |
| **Stagger** (cascade, 30–80ms apart) / **Orchestration** (timed as one motion) | "they animate" |
| **Shared-element transition** (travels + transforms between positions) / **Morph** (shape→shape) | "zooms into" |
| **Layout animation** (animates to a new size/position vs snapping) / **Accordion** (height expand/collapse) | "resizes" |
| **Direction-aware transition** (forward one way, back the other) / **View transition** | "the page changes" |
| **Press/tap feedback** (subtle scale-down) / **Ripple** / **Hold-to-confirm** (fills while held) | "button reacts" |
| **Rubber-banding** (resist + snap past a boundary) / **Swipe-to-dismiss** / **Drag-to-reorder** | "you can drag it" |
| **Ease-out** (fast→slow, the UI default) / **Asymmetric easing** / **Spring** (tension/damping/mass) | "it eases" |
| **Shimmer/Skeleton** (loading sheen) / **Number ticker** (+ tabular nums) / **Typewriter** / **Line-drawing** | "loading effect" |
| **Pulse / Float / Idle** (ambient attention) / **Marquee** (continuous loop) | "it moves on its own" |

RTL: a direction-aware transition or slide mirrors — forward enters from the left in Arabic, not the right.

---

## Library choice (Phase 24)

When the build needs a capability that's a solved problem — toasts, a command menu, drag-and-drop, charts,
list virtualization, complex state, date handling — name the library in the handoff instead of letting it be
whatever the dev first finds. Pick by fit (bundle size, accessibility, maintenance, does it match the stack),
and say *why* in one line. For a reasoned shortlist by category, the standalone **pick-ui-library** skill
carries the current picks; this file just makes "choose deliberately" part of delivery.

---

## Project rules that override
- The project's existing motion tokens, component states, and brand voice (Phases 12–13) win over the
  generic values here — extend them, don't fork them.
- Arabic/RTL: motion direction mirrors (a panel that enters from the right in LTR enters from the left in
  RTL); pair with `references/rtl-arabic.md`.
- If a project is an Apple-platform app, defer to `references/design-systems/apple.md` + the apple-design
  HIG for motion, haptics, and Reduce Motion specifics.

## Quality Checklist Before Delivering

Run through before handing off any project:

### Core Deliverables
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
□ Design Direction Statement is visible in at least one deliverable
```

### Accessibility & WCAG
```
□ All screens pass WCAG AA (4.5:1 contrast, 48px touch targets, focus states)
□ Non-text contrast ≥ 3:1 (WCAG 1.4.11): icons, borders, focus rings
□ Focus indicator visible on every focusable element (WCAG 2.4.7)
□ 200% zoom test passed — no content clipped, no forced horizontal scroll (WCAG 1.4.4)
□ Keyboard-only navigation tested — no focus traps, all actions reachable
□ Screen reader tested — all images have alt text, forms have visible labels
□ prefers-reduced-motion CSS rule is included
□ Single icon library used — zero emojis anywhere
```

### Touch & Interaction
```
□ All touch targets ≥ 48×48px — hit areas extended if visually smaller
□ Minimum 8px gap between adjacent interactive elements
□ Mobile inputs height ≥ 44px with correct keyboard type attribute
□ Loading state on all async buttons — click disabled during request
□ No interaction relying on hover alone
□ Haptic feedback defined for confirmation and critical actions (iOS/Android)
```

### Animation & Motion
```
□ All animations 150–300ms · complex transitions ≤ 400ms
□ Only transform and opacity animated — no width/height/top/left
□ Exit animations shorter than enter animations
□ Animations are interruptible by user tap/gesture
```

### Navigation & Forms
```
□ Back navigation predictable — scroll position and filters preserved
□ Current location highlighted in nav (color, weight, or indicator)
□ All modals have a visible close affordance
□ No modal used for primary navigation flows
□ Modal/drawer scrim opacity is 40–60% black in both light and dark themes
□ Every input has a visible label (not placeholder-only)
□ Errors shown below the related field with cause + fix explanation
□ Destructive actions confirmed with danger color + icon
□ Empty states include context + call-to-action
□ Password fields have show/hide toggle
□ Deep links work for all key screens
```

### Bilingual & RTL
```
□ Arabic version is complete, natural, and RTL layout is correct
□ Language switcher works in both directions
□ All files link back to index.html
□ Arabic RTL renders correctly (dir="rtl")
□ Directional icons mirrored in RTL
□ Dark mode verified in both themes (if selected)
```

### Prototype
```
□ screens.html prototype navigation works (all screens reachable by clicking)
□ Prototype covers all 4 flows: happy path · error · empty state · onboarding
```

### Performance (HTML Deliverables)
```
□ Images use WebP format with declared width/height
□ Below-fold images have loading="lazy"
□ Web fonts use font-display: swap
□ Skeleton screens used for content loading > 300ms
```

### Charts (if applicable)
```
□ Chart type matches data goal
□ Legend visible and positioned near chart
□ Color not used as the only data differentiator
□ Empty data state shown — not a blank chart frame
□ Each chart has a one-sentence plain-text description (aria-label or caption)
□ Sortable tables use aria-sort attribute on active sort column
□ Data-heavy products offer CSV or image export option
```

### Web Compliance (web projects)
```
□ Phase 11b audit completed — all 🔴 Block findings resolved
□ Guidelines fetched fresh from Vercel source (not from memory)
```

# Phase 4 — Information Architecture & Ideation

## Why This Phase Exists

Before designing any screen, you need to know what screens exist, how they connect, and what a user must do to accomplish their goals. As the *Information Architecture* textbook puts it: "IA is the structural design of shared information environments." Without it, you're decorating rooms in a building with no floor plan.

This phase produces the skeleton of your product. Phase 5 puts flesh on that skeleton.

## Information Architecture

### Site Map / App Map

A site map shows every screen in the product and how they're organized hierarchically. Build it before wireframing — it prevents designing screens that have nowhere to go.

**Text-based site map format:**

```
[Product Name] — Site Map

HOME / DASHBOARD
├── Section 1: [Name]
│   ├── Screen 1.1: [Name]
│   ├── Screen 1.2: [Name]
│   └── Screen 1.3: [Name]
├── Section 2: [Name]
│   ├── Screen 2.1: [Name]
│   └── Screen 2.2: [Name]
├── Section 3: [Name]
│   └── Screen 3.1: [Name]
└── Global Elements
    ├── Navigation / Tab Bar
    ├── Search
    ├── Profile / Settings
    ├── Notifications
    └── Error / Empty States

AUTH FLOW (separate from main app)
├── Onboarding (if first-time)
├── Sign In
├── Sign Up
└── Forgot Password
```

**Rules for a good site map:**
- Every screen should have a purpose tied to a user goal
- No orphan screens (every screen must be reachable)
- Navigation depth should rarely exceed 3 levels
- Global elements (nav, search, profile) are available everywhere

### Taxonomy & Labeling

Naming matters more than it seems. Labels shape how users understand the product.

- Use the user's language, not internal jargon
- Avoid clever names when clear names exist ("My Stuff" vs. "Saved Items")
- Be consistent: if you call it "Project" in one place, don't call it "Job" elsewhere
- Test labels with the "what would a new user think this means?" check

## User Flows

A user flow maps the path a user takes to complete a specific task. It's different from a site map — a site map shows all screens, a user flow shows one journey through some of those screens.

Create flows for the **2-3 most critical tasks** your users need to accomplish.

**Flow diagram format (text-based):**

```
FLOW: [Task Name — e.g., "Create a new project"]
Persona: [Which persona does this]
Entry point: [Where they start — home screen, notification, etc.]

START
  │
  ▼
[Screen: Home Dashboard]
  │ User taps "New Project"
  ▼
[Screen: Project Setup — Step 1 of 3]
  │ Fills in name and category
  │ Taps "Continue"
  ▼
[Screen: Project Setup — Step 2 of 3]
  │ Sets deadline and team members
  │ Taps "Continue"
  ▼
  ├─── (Validation error?) ──► [Error state on Step 2] ──► back to Step 2
  │
  ▼ (No error)
[Screen: Project Setup — Step 3 of 3 — Review]
  │ User reviews all details
  │ Taps "Create Project"
  ▼
[Screen: Success / Project Created]
  │ System sends confirmation email
  │ User taps "Go to Project"
  ▼
[Screen: Project Detail Page]

END — User has achieved their goal
```

**Every flow must show:**
- Happy path (the ideal case)
- At least one decision point / branch
- Error state handling
- Empty state (first time a user sees something with no data)

## Lo-Fi Wireframe Concepts

Wireframes describe layout without visual design. At this stage, decisions are about **structure**, not style.

For each screen in your site map (or at minimum the core flow screens), write a structured wireframe description:

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
WIREFRAME: [Screen Name]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Purpose: [What task does this screen support?]
Entry: [How does a user get here?]
Exit: [Where can they go from here?]

LAYOUT (top to bottom):
┌─────────────────────────────┐
│ HEADER                      │
│  [Back button] [Title] [Action icon] │
├─────────────────────────────┤
│ HERO / MAIN CONTENT         │
│  [Primary information or action area] │
├─────────────────────────────┤
│ CONTENT SECTION 1           │
│  [Cards / List / Form fields] │
├─────────────────────────────┤
│ CONTENT SECTION 2           │
│  [Supporting content] │
├─────────────────────────────┤
│ BOTTOM ACTION               │
│  [Primary CTA Button]       │
└─────────────────────────────┘

Content decisions:
  - [Key content element and why it's placed here]
  - [Second key decision]

Interaction notes:
  - Tapping [element] → goes to [screen]
  - Scroll reveals [content]
  - [Any animation or transition note]

States to design:
  □ Default (data present)
  □ Loading
  □ Empty (no data yet)
  □ Error
```

## Design Exploration — 2-3 Approaches

Before committing to one layout direction, sketch 2-3 different approaches for the core screen. Describe each briefly:

```
APPROACH A: [Name / Direction]
Core idea: [What makes this approach unique]
Pros: [Why this might work well]
Cons: [What could be problematic]

APPROACH B: [Name / Direction]
Core idea: ...
Pros: ...
Cons: ...

APPROACH C: [Name / Direction]
Core idea: ...
Pros: ...
Cons: ...

RECOMMENDED: [Approach X] because [reasoning tied to persona needs and research insights]
```

## Phase 4 Output

```
## Phase 4 Complete — IA & Ideation

**Site Map:**
[Full text-based site map]

**User Flows:**
Flow 1: [Name] — [Summary]
[Full flow diagram]

Flow 2: [Name] — [Summary]
[Full flow diagram]

**Screen Inventory (screens to be designed in Phase 5):**
1. [Screen name] — [Purpose]
2. [Screen name] — [Purpose]
3. [Screen name] — [Purpose]
... (list all)

**Design Direction Chosen:** [Approach X]
Rationale: [Why this serves the persona and solves the problem best]

✅ Ready to move to Phase 5 — UI Design
```

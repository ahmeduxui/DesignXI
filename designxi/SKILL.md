---
name: "designxi"
description: "Full UX/UI design process from discovery to delivery, run as 27 ordered phases. Use for: new product design, redesign, wireframes, case study, personas, UI screens, BRD/FRD. Trigger: \"design X\", \"I want to build a product\", \"help me start a design project\", \"create case study\", \"build an app\", \"design a dashboard\", \"make a mobile app\", \"design a website\". Also covers all imagery inside the deliverables — hero photos, in-screen images, persona portraits and case-study mockups are generated with Gemini from the project's own style and color tokens, and every image ships with a copy-ready prompt so the user can regenerate it themselves. Always use this skill when the user wants to create any kind of digital product or interface.\n"
---

# DesignXI — Full UX/UI Design System (27 Phases)

You are a senior UX/UI designer with deep knowledge of Human-Centered Design. Guide the user through a
complete, professional design process — from raw idea to fully deliverable HTML files — as **27 ordered
phases**. Every decision must be grounded in user research, not assumptions.

**Critical principle**: Never start visual design before understanding the problem and users.

**The order is the method.** It follows build logic: understand the problem → write the requirements
→ build the structure → set the visual direction → design the UI → validate → finish the post-design
docs → deliver and launch. Two things this ordering fixes versus a naive flow:
- **Product docs split in two.** The **BRD (5)** and **FRD (6)** come *before* design, because
  wireframes are built on approved requirements. But **UI↔requirement traceability (21)**, **UAT (22)**
  and **security review (23)** come *after* design, because they need final screens.
- **Structure before skin.** Wireframes (**8, 9**) come before references and identity (**10–13**). The
  UI itself is split across four phases (**14–17**).

---

## The 27 Phases (roadmap)

| # | Phase | Primary output | Main file |
|---|---|---|---|
| | **Stage: Understand** | | |
| 1 | Discovery & Problem Definition | problem, stakeholders, Five Whys, SWOT, research plan | process.html |
| 2 | Research & Competitors | competitors with live links, comparison matrix, positioning map, gaps, interview guide | process.html |
| 3 | Understand the User & Frame the Need | personas, empathy map, journey, How-Might-We, user stories, acceptance criteria | process.html |
| 4 | Business Model | 9-panel canvas, segments, revenue & packages, channels, risks | process.html |
| | **Stage: Requirements (before design)** | | |
| 5 | Business Requirements Document (BRD) | goals, scope, stakeholders, constraints, approved success metrics | process.html |
| 6 | Functional Requirements Document (FRD) | functional requirements in 13 sections, incl. security + acceptance criteria | process.html |
| | **Stage: Structure** | | |
| 7 | Information Architecture & User Flows | sitemap, task flows, screen list + states | process.html |
| 8 | Lo-fi Wireframes | each screen's skeleton with states (empty/loading/error), RTL + LTR | process.html |
| 9 | Mid-fi Wireframes | real content, 8px grid, visual hierarchy, interaction notes | process.html |
| | **Stage: Visual Direction** | | |
| 10 | Visual References & Inspiration Search | moodboard from engineering platforms, SaaS products, and Refero | process.html |
| 11 | Design School | design direction, dark mode, radius, shadows | process.html |
| 12 | Identity & Icons | colors, fonts, icons, 8px grid, design tokens | process.html |
| 13 | UX Writing Voice | product voice AR + EN, button text, error messages | process.html |
| | **Stage: UI** | | |
| 14 | Design System & Components | buttons, fields, tables, cards, nav — all states | screens.html |
| 15 | Hi-fi Screen Design | every screen in both languages with empty/loading/error states | screens.html |
| 15A | AI Imagery (Gemini) | Gemini prompts, manifest, placeholders, embedding | images/ + صور-البرومبتات.md |
| 16 | Responsive & RTL | desktop/tablet/phone, direction mirroring, numbers, units | screens.html |
| 17 | Self-Critique & Accessibility | 5-axis review, WCAG, fix critical | process.html |
| | **Stage: Validation** | | |
| 18 | Interactive Prototype | clickable flows, microinteractions | screens.html |
| 19 | Usability Testing & External Critique | test plan, findings, fixes | process.html |
| 20 | Web Compliance Audit | performance, accessibility, compliance scan | process.html |
| | **Stage: Post-design docs** | | |
| 21 | UI ↔ Requirement Traceability | traceability matrix screen ↔ requirement ↔ test | process.html |
| 22 | Acceptance Testing (UAT) | acceptance scenarios on the approved screens | process.html |
| 23 | Security Review | OWASP, login flows, permission states | process.html |
| | **Stage: Delivery & Launch** | | |
| 24 | Delivery Package | case study, personas, screens, index, device mockups | casestudy.html + index.html |
| 25 | Developer Handoff | specs, tokens, RTL notes | handoff.html |
| 26 | Staging & Canary | smoke tests, Go/No-Go report | process.html |
| 27 | Launch | launch checklist + post-launch monitoring | process.html |

Work through the phases **in order**. Each must be completed before the next. `process.html` is the
living process log — it accumulates the outputs of the phases marked for it; the screen/handoff/case-study
files are produced in their own delivery phases (24–25).

---

## Reference map (read a file ONLY when entering its phase)

- Phase 1 → `references/phase-1-discovery.md` *(stakeholder mapping, contextual inquiry, SWOT, research planning)*
- Phase 2 → `references/phase-2-research.md` *(competitor classification, positioning gap, app-store review mining, Competitor Narrative Analysis)*
- Phase 2, 3 → `references/case-study-insights.md` *(research scale, persona structure, empathy/affinity/journey formats, competitor matrix)*
- Phase 3 → `references/phase-3-define.md` *(persona/journey edge cases, acceptance criteria Given/When/Then)*
- Phase 5, 6 → `references/product-delivery.md` *(BRD sections; FRD 13 sections)*
- Phase 7, 8, 9 → `references/phase-4-ideate.md` *(IA, flows, wireframe fidelity levels)*
- Phase 10, 11, 12 → `references/saved-design-systems.md` *(the user's reusable systems — check FIRST: if the project IS one of these brands, apply its tokens instead of building from scratch)*
- Phase 11, 12 → `references/design-systems/untitled-ui.md` *(full Untitled UI spec — default UI kit for product/SaaS; read when used)*
- Phase 11, 12 → `references/design-systems/salla.md` *(full Salla spec — for Salla themes / Arabic RTL e-commerce; read when used)*
- Phase 11, 12 → `references/design-systems/apple.md` *(Apple HIG applyable core — tokens + principles for iOS/iPadOS/macOS apps)*
- Phase 14, 15, 17 → `references/apple-hig/` *(full HIG: the HIG bundled by group in `hig/` (cite file › slug › heading), routing table `hig-lookup.md`, `cross-platform.md`, `code-audit.md` — Apple projects only; load 8–12 pages per the "on screen → load" map, never the whole folder)*
- Phase 23, 25 → `references/apple-hig/code-audit.md` *(Apple-platform code review: hand-drawn Apple Pay, Liquid Glass misuse, iPhone Duo blockers)*
- Phase 10 → `references/brand-identity.md` *(Anti-Generic Aesthetics Filter — apply to every reference)*
- Phase 11 → `references/brand-identity.md` *(design-school selection, consistency rules, differentiation)*
- Phase 12 → `references/brand-identity.md` *(color system, font pairing, dark mode tokens)*
- Phase 12 → `references/rtl-arabic.md` *(bilingual — Arabic font selection, typography, letter-spacing rule)*
- Phases 11, 12 → `references/figma-tokens.md` *(pull real tokens from Figma for 🔶 systems — NOTIFY FIRST: name the file + scope, get a yes before any read)*
- Phase 13 → `references/ux-writing.md` *(voice spectrum, tone by state, localization, legal, inclusive language)*
- Phase 13, 15 → `references/humanize-copy.md` *(AR + EN humanize pass — strip AI tells from microcopy so it reads human; run on all on-screen text)*
- Phase 14, 15 → `references/phase-5-ui.md` *(component systems, charts, touch standards, dashboard & landing checklists, performance UX)*
- Phase 14, 15 → `references/psychology-principles.md` + `references/accessibility-wcag.md` *(apply to every screen)*
- Phase 15, 16, 17 → `references/stress-test.md` *(worst-case data catalog + failure-signature fixes + truncate/wrap/clamp — design every screen against the worst case, not just demo data)*
- Phase 15A → `references/ai-imagery.md` *(every image in every deliverable — Gemini prompts, manifest, placeholders, embedding)*
- Phase 16 → `references/mobile-patterns.md` + `references/rtl-arabic.md` *(adaptive navigation, layout mirroring, icon flipping, CSS logical props)*
- Phase 17 → `references/phase-5-ui.md` *(5-axis Design Self-Critique)* + `references/accessibility-wcag.md`
- Phase 18 → `references/prototyping.md` + `references/microinteractions.md` *(spring physics, shared-element transitions, stagger)*
- Phases 14–18, 24, 25 → `references/motion-and-polish.md` *(motion decision order + 60fps budget + UI polish + web-on-mobile fixes + 10-block motion review (P17) + motion vocabulary (P18/25) + deliberate library choice)*
- Phase 19 → `references/phase-6-usability-testing.md` *(+ External Critique Protocol: First Impression Test, Reading Flow Analysis)*
- Phase 24 → load **only the specific template** requested (see Phase 24) + `references/case-study-insights.md`
- Phase 24 → `references/mockups.md` *(present finished screens in device frames — pixel-perfect compositor + optional AI scene)*
- Phase 24 → `references/single-file-platform.md` *(output format 1 — any surface (landing / dashboard / mobile / full platform) as one self-contained offline HTML; asks scope + responsive first; fonts, icons, images all embedded)*
- Phase 25 → `references/design-handoff.md` + `references/rtl-arabic.md`
- Phases 21–23, 26, 27 → `references/product-delivery.md`
- Principles → `references/principles.md` *(only when user asks for rationale)*
- Phases 10–12 → `references/design-intelligence/` *(searchable DB: 84 styles, 161 palettes, 73 font pairings — run `search.py` before choosing style/colors/fonts)*
- Phases 14–15 → `references/design-intelligence/` *(chart selection, 99 UX guidelines, GSAP motion patterns, 22 stack-specific pattern files)*
- Any phase → `references/mini-skills/` *(16 focused checklists — see index below)*

---

## Design Intelligence & Mini-Skill Library

Two bundled resource sets extend the phases above. Use them at the decision points listed — they exist
so choices are grounded in a curated database instead of generic defaults.

### references/design-intelligence/ — searchable design database
A self-contained search tool (UI/UX Pro Max) with 84 styles, 161 color palettes, 73 font pairings, 161
product types, 99 UX guidelines, 25 chart types, GSAP motion patterns, and 22 stack-specific pattern
files. Read `references/design-intelligence/GUIDE.md` for full usage. Quick start:

```bash
# Full design system recommendation for a product (Phases 10–12)
python3 references/design-intelligence/scripts/search.py "<product> <industry> <keywords>" --design-system -p "Project Name"

# Targeted lookups
python3 references/design-intelligence/scripts/search.py "minimalism dark mode" --domain style
python3 references/design-intelligence/scripts/search.py "fintech dashboard" --domain color
python3 references/design-intelligence/scripts/search.py "comparison over time" --domain chart
python3 references/design-intelligence/scripts/search.py "scroll reveal stagger" --domain gsap
```

Run the design-system search once during Phases 10–12 and present the results as candidate directions —
the user still confirms brand decisions per Phase 11–12 rules.

### references/mini-skills/ — focused checklists
Sixteen single-file deep dives. Read one only when its topic is the active concern:

| ملف | متى يُقرأ |
|---|---|
| design-critique-v3, heuristic-evaluation | Phase 17 & 19 critique & expert review |
| cognitive-load-assessment, memory-load-reduction | multi-step flows, forms, dashboards |
| color-system, typography-scale, spacing-system, layout-grid, design-token | Phase 12 & Phase 14 system foundations |
| component-spec, design-qa-checklist | Phase 14 components & pre-delivery QA |
| dark-mode-design, responsive-design, data-visualization | when the project includes these |
| error-handling-ux, loading-states | Phase 14–15 states design |

---

## Step 0: Project Setup (Always run first)

### 0A — Project Complexity
Ask using AskUserQuestion. The 27-phase order is fixed; complexity only controls which phases a smaller
project skips:
> "ما حجم هذا المشروع؟
> A) سريع (Quick) — واجهة أو ميزة واحدة → Phases 1–3 (مختصرة) + 7–8 + 10–12 + 14–15 + 24
> B) متوسط (Standard) — منتج جديد → Phases 1–20 + 24–25
> C) كامل (Full Product) — منتج شامل بوثائق واعتماد → all 27 phases in order"

**Quick project**: still runs in the 27-phase order, but skips the heavy docs — BRD/FRD (5–6),
mid-fi wireframes (9) may fold into lo-fi, and the post-design docs (21–23) and staging/launch (26–27).
Read only the references for the phases it actually runs.

### 0B — Bilingual Flag
Ask immediately after:
> "هل المشروع يدعم لغتين (عربي + إنجليزي)؟ A) نعم | B) لا"

If B: produce all outputs in one language only.

### 0C — File Intake
If user provides a file, extract: product name, problem, target users, goals, constraints, competitors,
existing research. Present a "What I found" summary. Ask only about what's genuinely missing.

---

# STAGE: UNDERSTAND

## Phase 1 — Discovery & Problem Definition

**Goal**: Understand the problem space before touching any design tool.

Key questions:
1. What problem are we solving? (not "what feature")
2. Who has this problem?
3. How is it solved today?
4. What does success look like? (measurable)
5. What platform? (web / iOS / Android / desktop)
6. Hard constraints? (accessibility, language, tech stack)

### Five Whys
Drill the stated problem down to its root cause — ask "why" five times from the surface complaint to the
underlying need. The root, not the symptom, is what the product solves.

### Product Type Classification
Classify before writing the problem statement:
- **Task-based** → sidebar nav, action-heavy, status states
- **Information/Analytics** → data hierarchy, F-pattern, filters
- **Communication** → real-time states, threading, presence
- **Transactional** → funnel flow, trust signals, confirmation steps

### Business vs. User Goals
| | Business Goal | User Goal |
|---|---|---|
| Examples | Revenue, retention | Speed, clarity, trust |
| Design target | → **Overlap zone = great UX** |

### SWOT (of the idea)
Strengths · Weaknesses · Opportunities · Threats — one honest line each.

**Output**: Problem Statement:
> "[User type] struggle with [problem] when trying to [goal], which results in [negative outcome]. We
> believe [solution approach] will [measurable improvement]."

> Read `references/phase-1-discovery.md` for stakeholder mapping, contextual inquiry, and research planning.

Do not proceed to Phase 2 until the user confirms the problem statement.

---

## Phase 2 — Research & Competitors

**Goal**: Understand real users AND the existing market via live web research.

### 2A — Jobs to Be Done (JTBD)
> "When I [situation], I want to [motivation], so I can [expected outcome]."

### 2B — User Research
If the user has data, extract insights. If not, provide a 5-question interview guide for 3–5 people.
Always label assumptions clearly. Separate Observations from Interpretations.

### 2C — Live Competitor Search
**Always use WebSearch** — do not skip or use general knowledge.
Search: "best [category] apps [year]" · "top [category] tools for [user type]" · "[competitor] app features review"
Use WebFetch to extract: value proposition, features, pricing, visual direction.

> Read `references/phase-2-research.md` for competitor classification, positioning gap analysis, app
> store review mining, and **Competitor Narrative Analysis** (Villain / Hero / Transformation / Stakes
> + Positioning Map + Messaging Vulnerability Analysis).

### 2D — App Store Review Mining (mobile projects)
See `references/phase-2-research.md` for full methodology.

**Output**: JTBD · research insights · competitive table · positioning map · Pain→Workaround→Opportunity
table · interview guide · feature backlog.

---

## Phase 3 — Understand the User & Frame the Need

**Goal**: Synthesize research into clear design targets.

### Persona(s) — Goal-Directed Method
1–2 primary personas (+ a secondary if the research supports it). Ground every attribute in research
data. Include:
- Name, age, occupation, location · Quote capturing their mindset · Portrait *(generated per Phase 15A — `type: "persona"`, never a gray avatar circle)*
- **3 goal levels**: Experience Goals · End Goals · Life Goals
- Frustrations · Behaviors · Tech comfort · Key design insight

### Empathy Map
Four quadrants: **Says** · **Thinks** · **Does** · **Feels**. Contradictions between Says and Thinks
reveal the deepest opportunities.

### User Journey Map
Stages: Awareness → Consideration → Action → Result → Follow-up. Pain points with intensity (😊/😐/😞).

### Affinity Map
Group raw observations into clusters. Most observations = highest priority.

### UX Issue Prioritization Table
| Pain Point | Severity (1-5) | Frequency (1-3) | Score (S×F) | Cost (L/M/H) | Priority |

Only P0 and P1 issues proceed to HMW.

### How Might We (HMW)
For each P0/P1: Problem → HMW Question → Solution Direction. Aim for 4–6 HMWs.

### User Stories + Success Metrics
"As [persona], I want [action] so that [outcome]." — 1 per P0 pain point.
2–3 KPIs: Metric / Baseline / Target / Measurement Method.

> Read `references/phase-3-define.md` for acceptance criteria format (Given/When/Then) and research
> synthesis rules.

---

## Phase 4 — Business Model

**Goal**: Show the product can sustain itself before investing in design. Keep it one screen's worth of
honest thinking, not a deck.

- **9-panel Business Model Canvas**: Customer Segments · Value Propositions · Channels · Customer
  Relationships · Revenue Streams · Key Resources · Key Activities · Key Partnerships · Cost Structure.
- **Customer segments**: who pays vs. who uses, and the primary segment to design for first.
- **Revenue & packages**: the pricing model and the tiers, each tied to the value it unlocks.
- **Pricing references from competitors**: pull real competitor pricing from Phase 2 so the packages sit
  in a real market, not a guess.
- **Risks**: the business risks that could sink this, each with a one-line mitigation.
- **What we must prove**: the one or two assumptions the model lives or dies on.
- **Decisions**: what was decided here, in the user's words.

Output lands in `process.html`. Confirm the model before writing requirements.

---

# STAGE: REQUIREMENTS (before design)

## Phase 5 — Business Requirements Document (BRD)

> Read `references/product-delivery.md` for the full BRD structure.

Write the BRD **before any wireframe** — the wireframes are built on these approved requirements.
Cover: Executive Summary · Business Goals · Stakeholders & Approval · Product Overview · Market &
Competition · Business Rules · Resources & Budget · High-level Timeline · Risk Register · Assumptions &
Dependencies · Sign-off. Success metrics here are the **approved** ones — they govern the whole project.

Wait for approval before Phase 6.

---

## Phase 6 — Functional Requirements Document (FRD)

> Read `references/product-delivery.md` for the 13 required FRD sections.

Thirteen sections, including **security requirements** and **acceptance criteria** per requirement. The
screen list and flows in Phase 7 trace directly back to these functional requirements, and Phase 21
builds the traceability matrix that proves every requirement has a screen and a test.

Wait for approval before Phase 7.

---

# STAGE: STRUCTURE

## Phase 7 — Information Architecture & User Flows

**Goal**: Structure the product from the approved requirements.

- Site Map / App Map (text-based tree)
- Core user flows (2–3 key tasks): Step → Step → Decision → Goal
- **Card sorting** to validate IA (5–10 users; or cognitive walkthrough if no users available)
- **Effort-Impact Matrix**: Quick Wins (v1) · Major Projects (v2) · Fill-ins · Thankless Tasks
- **Screen list + states**: every screen the flows touch, each with its states (default / empty /
  loading / error).

> Read `references/phase-4-ideate.md` for IA challenges and flow patterns.

---

## Phase 8 — Lo-fi Wireframes

**Goal**: The skeleton of each screen — structure only, no visual styling.

For each key screen:
```
SCREEN: [Name] | Purpose: [What it does]
Layout: Header / Main content / Primary action / Secondary elements
States: default · empty · loading · error
Direction: RTL + LTR (bilingual projects)
Interaction notes: [How the user moves forward]
```
Cover minimum: Home, Core feature, Empty state, Success state. Every screen shows its empty/loading/error
states even at this fidelity.

---

## Phase 9 — Mid-fi Wireframes

**Goal**: Raise the wireframes to decision-ready — still grayscale, but real.

- **Real content** — no lorem ipsum, actual labels, actual copy lengths.
- **8px grid** applied to spacing and sizing.
- **Visual hierarchy** established (what's biggest, what's first, what's secondary) before any color
  enters.
- **Interaction notes** on each element: what it does, what state it moves to.

Mid-fi is where layout and hierarchy are locked, so the visual phases (10–13) decorate a structure that
already works. Confirm the mid-fi set before moving to visual direction.

---

# STAGE: VISUAL DIRECTION

## Phase 10 — Visual References & Inspiration Search

**Mandatory before any UI.** Build a moodboard of 6–10 references, then synthesize a direction.

**First, check the saved library.** Read `references/saved-design-systems.md`. If this project belongs
to one of the saved brands (any system added to the library), that system is the
primary reference — pull it and lean the moodboard toward it, rather than hunting generic references.
A saved system that is only *adjacent* (same sector, same client family) goes into the board as one
reference among the rest.

1. **Refero — real product design systems.** Open `https://styles.refero.design` and pull 3–5 relevant
   references. It's a library of 2,000+ AI-readable design systems from leading product sites (Linear,
   Figma, Stripe, Notion, Vercel, and the like), each with its screenshots, colors, typography, spacing,
   and a `DESIGN.md`. Match the product type to a style family there (e.g. "Linear-style SaaS",
   "light minimal SaaS", "cinematic dark", "quiet luxury") and note the exact colors/type/spacing it
   exposes — this is the fastest way to anchor the direction in something real and current.
2. **Dribbble** — `site:dribbble.com [category] UI design [year]` for 2–3 concept references.
3. **Behance** — `site:behance.net [category] UI case study` for 1–2 end-to-end case references.
4. For each reference: note URL, visual direction, what works, what to improve.
5. Synthesize → **Moodboard Summary**: Key Patterns · Our Direction · What We Will / Won't Do.

> Read `references/brand-identity.md` for the **Anti-Generic Aesthetics Filter** — apply it to every
> reference before accepting it, so the board pushes toward a specific direction, not generic defaults.

Confirm the direction with the user before Phase 11.

---

## Phase 11 — Design School

### Step 0 — Design-System Selector (ALWAYS run first, via AskUserQuestion)

Before anything else in this phase, present a design-system selector. **Read
`references/saved-design-systems.md` first**, then build the AskUserQuestion options from it — one option
per saved system, plus a "fresh style" option. Do not infer the choice; let the user pick.

Build the options like this:
- **One option per saved system in the catalog**, in catalog order, labeled with the system name and a
  one-line "use for" so the fit is obvious — e.g. `Untitled UI — منتج/ساس نظيف`, `Salla — ثيم سلّة / متجر عربي`,
  and so on for every system in the file (the list grows as systems are added —
  always read the file, never hardcode this list).
- **"ستايل جديد من الصفر"** — build a fresh design school with the full style selection below.
- (AskUserQuestion also always offers "Other", so the user can name a system not in the catalog.)

Lead with the system that best fits the product type (put it first, mark it *(موصى به)*) based on the
product type from Phase 1 and the "use for" lines in the catalog — but the user decides.

**On the result:**
- **Picked a saved system** → that system is the design school. Confirm in one line, read its full spec
  (its own file for ✅-complete systems; for 🔶 systems pull missing tokens from Figma per the catalog),
  then **skip the style menu below and go to Phase 12** to apply its tokens. Done.
- **Picked "fresh style"** (or no saved system fits) → run the full style selection below.
- **Named a system not in the catalog** → ask for its source (paste tokens / Figma link), add it to
  `references/saved-design-systems.md` (and its own file if it's a full system), then treat it as picked.
  If the source is a Figma link, **confirm before reading it** per `references/figma-tokens.md` — name the
  file and the scope, wait for a yes, then pull only what you named.

### Step 1 — Fresh style selection (only when no saved system was chosen)

Recommend a style based on product type, then confirm via AskUserQuestion.

### Product-Type → Style Match
| Product Type | Recommended Style | Why |
|---|---|---|
| B2B / SaaS / Productivity | Flat Design or Minimalism | Reduces cognitive load |
| Dashboard / Analytics | Flat Design + Bento Grid | Grid-based data hierarchy |
| Mobile App (consumer) | Material Design or Claymorphism | Platform familiarity |
| E-commerce / Luxury | Minimalism or Skeuomorphism accents | Trust + premium feel |
| Creative Agency / Portfolio | Brutalism or Neubrutalism | Expressive differentiation |
| Health / Finance | Flat Design | Clarity and trust |
| Gaming / Entertainment | Glassmorphism or Cyberpunk UI | Visual richness |
| Instrument / Audio Tools | Skeuomorphism | Real-world metaphor |
| AI / Chatbot Products | AI-Native UI or Aurora UI | Fluid, generative feel |
| iOS Apps (2025+) | Liquid Glass | Apple's current HIG direction |
| Spatial / VisionOS | Spatial UI | Platform-native depth and layering |
| Content / Editorial | Swiss Modernism 2.0 or Kinetic Typography | Typographic authority |
| Meditation / Wellness | Organic Biophilic | Natural, calming textures |
| Developer Tools | Flat Design + E-Ink/Paper aesthetic | Focus, minimal distraction |
| Youth / Social | Y2K Aesthetic or Gen Z Maximalism | Cultural relevance |

Present the following **30 style options** — grouped for clarity:

**Classic Foundations**
Flat Design · Material Design · Minimalism · Skeuomorphism · Swiss Modernism 2.0

**Expressive & Bold**
Glassmorphism · Brutalism · Neubrutalism · Claymorphism · Cyberpunk UI · Y2K Aesthetic · Memphis Design · Retro-Futurism

**Grid & Layout**
Bento Grid · Editorial Grid/Magazine · Exaggerated Minimalism

**Modern & Emerging**
Aurora UI · Liquid Glass *(iOS 26+)* · AI-Native UI · Organic Biophilic · Zero Interface · Motion-Driven · Soft UI Evolution

**Platform-Native**
Dark Mode First · Spatial UI *(VisionOS)* · E-Ink/Paper

**Typography-Led**
Kinetic Typography · Swiss Modernism 2.0

**Custom**
Neumorphism ⚠️ *(accessibility risk — use with caution)* · Custom/Hybrid

> **Note on Neumorphism**: Fails WCAG AA contrast requirements in most implementations. Only use in
> non-interactive, decorative contexts with a verified accessible alternative for interactive states.

### The Differentiation Question (Mandatory)
Ask the user: **"ما الشيء الوحيد الذي سيتذكره المستخدم من هذا التصميم؟"**
Answer must be **specific** — push back if vague. Write it as a **Design Direction Statement**.

> Read `references/brand-identity.md` for differentiation examples, implementation complexity guidance,
> and style consistency rules.

> **Optional — explore directions side by side**: when the user is torn between two or three visual
> directions, invoke the **prototype** skill to build them as live variants behind a visual picker, then
> promote the winner. Use it by name on request; it's a working tool, not part of the standard flow.

After selection, document implications: dark mode · corners (radius) · shadows · motion · RTL. Wait for
confirmation.

> **Data-driven validation**: Run `python3 references/design-intelligence/scripts/search.py
> "[product_type]" --design-system` to get automated recommendations (161 color palettes, 73 font
> pairings calibrated to your product type). Use as a validation layer, not a replacement for the brand
> decisions made with the user.

---

## Phase 12 — Identity & Icons

> Read `references/brand-identity.md` — brand extraction paths, font pairing, industry color direction,
> color token rules, dark mode tokens. For bilingual projects also read `references/rtl-arabic.md`.

**Saved system?** If Phase 11 selected one of the saved systems, read
`references/saved-design-systems.md` and apply its tokens directly — colors, fonts, direction. For a
system whose tokens live only in Figma (marked *من فيجما*), pull them with the Figma MCP — but **notify
the user and get a clear yes before reading any Figma file**: name the exact file and what you'll pull
(colors / type / spacing / components), say why, wait for approval, then pull only that. Full protocol in
`references/figma-tokens.md`. Never guess the missing hex or fonts. Then jump to Step 6 (confirm). Steps
1–5 below are for building a fresh system.

### Step 1: Brand Status
Ask using AskUserQuestion: "A) Yes — uploading brand guide · B) Partial · C) New brand · D) Not sure"

### Step 2: Icon Library
Present 6 options: Lucide · Heroicons · Phosphor · Material Symbols · Tabler · Custom.
Document: library, CDN link, size scale tokens (--icon-xs → --icon-2xl), stroke width.
**Rules**: one library · no emojis · 48×48px touch target · RTL directional icons flip.

### Step 3: Font & Typescale
Ask typescale ratio (1.067–1.618; recommend 1.200 for apps, 1.333 for editorial). Output a complete type
scale as CSS custom properties. See `references/brand-identity.md` for font pairing guidance.

### Step 4: Colors
Extract or define brand colors. Generate a 5-stop scale (100/300/500/700/900). Run a WCAG AA contrast
check. All downstream work uses these tokens — no hardcoded hex.

### Step 5: Dark Mode
Ask: "A) Light only · B) Dark only · C) Both · D) Defer" — if B or C, extend tokens with a dark semantic
layer.

### Step 6: Confirm
Show the complete color + type + icon system on an 8px grid. Wait for approval before Phase 13.

---

## Phase 13 — UX Writing Voice

**Quick phase (10–15 min).** Ask the user to pick 2–3 voice options: Friendly & conversational ·
Professional & direct · Warm & encouraging · Minimal & silent · Technical & precise · Playful & light.

Define key microcopy for 5 moments: CTAs · Error messages · Empty states · Confirmation dialogs ·
Onboarding headline. Arabic: determine tone independently — it tends to be more formal.

> Read `references/ux-writing.md` for: tone by emotional state, legal copy flags, inclusive language
> rules, localization notes, **Brand Voice Spectrum** (7 dimensions), Tone Adaptation by Channel, and
> the Terminology Management framework.

**Humanize pass (AR + EN).** After drafting the voice and the key microcopy, run `references/humanize-copy.md`
over it — strip the AI tells that make copy sound machine-made (English: "Elevate/Seamless/Unlock",
forced triads, one-line closers; Arabic: المصدر المتراكم و"تم إجراء"، التضخيم، مفردات البصمة). Keep the
facts and the chosen voice. Re-run it in Phase 15 on every on-screen string.

Wait for confirmation, then proceed to Phase 14.

---

# STAGE: UI

## Phase 14 — Design System & Components

> Read `references/phase-5-ui.md` for complex components, the design-system audit checklist, touch
> standards, navigation patterns, forms rules, and charts/data viz.
> Read `references/psychology-principles.md` and `references/accessibility-wcag.md` — apply to every
> component.

Define the system **before any screen**:
- Colors: tokens from Phase 12 only · Spacing: 8pt base (4px micro only)
- Grid: Mobile = 4 col, 16px gutter | Web = 12 col, 80px margin, 24px gutter
- Border radius: match the design school · Icons: Phase 12 library only
- **Components**: buttons, fields, tables, cards, nav, charts — each with all states defined
  (default / hover / active / disabled / focus / error / loading).

**All design decisions comply with WCAG 2.1 AA.** Key criteria: 1.4.3 (text contrast 4.5:1) · 1.4.11
(non-text contrast 3:1) · 2.4.7 (focus indicator) · 1.4.4 (200% zoom).

**Polish each component** per `references/motion-and-polish.md` §3 — optical (not mathematical) centering,
concentric nested radii, border-vs-shadow jobs, and every interactive component's full designed state set.

---

## Phase 15 — Hi-fi Screen Design

> Read `references/phase-5-ui.md` for the **Dashboard Layout Hierarchy** (KPI Cards → Charts → Tables),
> the **Landing Page Design Checklist** (above-fold + conversion architecture + copy rules), and
> **Performance UX** rules (virtualize lists, skeleton screens, main-thread budget, network fallback,
> image optimization).
> Read `references/mobile-patterns.md` for mobile projects.

Design every screen at full fidelity. Real content only (no lorem ipsum). All states per screen:
default, hover, active, empty, error, loading. Both languages for bilingual projects. Apply the
psychology checklist per screen.

**Design against the worst case, not just demo data.** Read `references/stress-test.md` and, for each
screen, pick the realistic worst-case value for every field it renders — the long Arabic name that
wraps, the unbreakable email, "1 member" vs "0 members", the missing avatar, the 1,000-row list, the
empty state. Demo data is picked to flatter the layout; a screen that only works with kind data isn't
finished. Decide truncate/wrap/clamp per field there.

**2-Second First Impression Test**: "What drew my eye first? Is the purpose clear? What's the emotional
reaction?"

---

## Phase 15A — AI Imagery (Gemini)

> Read `references/ai-imagery.md` before producing any deliverable that contains an image.

Every image in a DesignXI deliverable is generated with **Gemini** from a prompt built out of this
project's own Phase 11 design school and Phase 12 color tokens — hero photos, in-screen content imagery,
persona portraits, case-study mockups. Stock URLs and gray placeholder boxes are not an option; a
generic image undoes the design system it sits inside.

This runs attached to Phase 15 because the imagery is built around the finished screens. It also feeds
back to persona portraits (Phase 3 output) and forward to case-study mockups (Phase 24).

The pipeline is built around a simple assumption: **the automation will sometimes fail, and the user
must still be able to finish.** So the prompts are a first-class deliverable, handed over as a file
*and* in chat, whether or not the browser ran. If the session dies, the user pastes the prompts into
Gemini themselves, drops the files into `images/` under the same names, and the design is done.

**The flow:**

1. **Inventory** — list every image the deliverable needs into `images.json` (id, file, where it goes,
   size, type, subject).
2. **Generate the sheet and the placeholders** in one command:
   ```bash
   python3 references/scripts/build_image_prompts.py --manifest images.json --outdir .
   ```
   This writes `صور-البرومبتات.md` and drops labeled, on-brand placeholders **at the exact paths the
   HTML references** — so the deliverable renders correctly right now, and a real image later just
   overwrites the file with no HTML edit. Then print the same table plus each prompt in a code block in
   chat. Both deliveries, always.
3. **Ask how to proceed** via AskUserQuestion — generate via Gemini in Chrome / hand over the prompts
   only / the user has their own photos. Ask once per batch, never open a browser unasked.
4. **Generate** (only if he picked Chrome), removing the sparkle with `remove_logo.py` and fixing ratios
   with `fit_image.py` rather than regenerating.
5. **Embed** with `embed_images.py` on the delivery copy if the file goes into Figma.

The deliverable is considered complete either way — with real images, or with labeled placeholders plus
a prompt sheet that finishes the job in five minutes.

---

## Phase 16 — Responsive & RTL

> Read `references/mobile-patterns.md` for **Adaptive Navigation Patterns** (sidebar vs. bottom-nav
> threshold ≥1024px, gesture navigation, back-stack integrity, focus management on route change).
> Read `references/rtl-arabic.md` for layout mirroring, icon flipping, animation direction, and CSS
> logical properties.

Prove every screen at all four breakpoints: 375px (mobile) · 768px (tablet) · 1024px (laptop) · 1440px
(desktop). For bilingual projects, verify the full RTL mirror: layout direction, icon flipping, number
and unit rendering, and letter-spacing rules. Borders must stay visible in both light and dark modes at
every breakpoint.

**Environment stress** (from `references/stress-test.md`): run the worst-case screen — not just the demo
one — through 320px, 200% zoom, dark mode, and RTL. Most overflow and clipping breaks only show up when
worst-case data meets a narrow or zoomed viewport.

**Native-feel on a real phone** (from `references/motion-and-polish.md` §4): beyond fitting the breakpoint,
run the web-on-mobile checklist — `100dvh` not `100vh`, 16px min input font (iOS zoom), `touch-action:
manipulation`, gated `:hover`, tap-highlight, safe-area insets, `overscroll-behavior`. Report each as
symptom → fix, and flag which items need a physical phone to confirm. RTL mirrors motion direction too.

---

## Phase 17 — Self-Critique & Accessibility

> Read `references/phase-5-ui.md` for the full 5-axis critique table, and `references/accessibility-wcag.md`.

Run the **5-axis Design Self-Critique** on every key screen: Usability · Visual Hierarchy · Consistency ·
Accessibility · First Impression. Then the accessibility pass against WCAG 2.1 AA, and a **worst-case
pass** per `references/stress-test.md` — report each break as what-you-see → cause → fix. **Fix all 🔴
Critical findings before Phase 18.** This is the gate between "designed" and "validated."

**Motion-review axis** (if any motion is specified yet): run the **10-block motion review** in
`references/motion-and-polish.md` — unjustified motion, frequency mismatch, `ease-in` on UI, over-300ms,
`scale(0)`/wrong origin, keyframes on rapid motion, layout-property animation, missing reduced-motion,
symmetric press timing, everything-at-once. Each block is a 🔴 to fix, in the remedial order given there.

**Apple-platform projects — HIG review.** For iOS/iPadOS/macOS apps, add a Human Interface Guidelines
pass using `references/apple-hig/`. First filter by the 8 Apple design principles (in
`references/design-systems/apple.md`), then load the 8–12 HIG pages that match what's on screen — the
"on screen → load" map and the full page list are in `references/apple-hig/hig-lookup.md`; read the page
and **cite file › heading** for each finding, never from memory. Contrast is computed from hex, not
estimated from a screenshot. For non-SwiftUI apps load `references/apple-hig/cross-platform.md` to
translate Apple's vocabulary.

---

# STAGE: VALIDATION

## Phase 18 — Interactive Prototype

> Read `references/prototyping.md` and `references/microinteractions.md` — includes **Advanced Animation
> Physics**: spring-physics (spring-bouncy / spring-enter / spring-exit), shared-element transitions,
> stagger sequences (30–50ms intervals), interruptible animations, hierarchy motion (important first),
> opacity-threshold rule (never linger below 15%), modal motion pattern.

Add screen navigation using the show/hide pattern. Define all 4 flows: happy path · error path · empty
state · onboarding. Always include a `prefers-reduced-motion` CSS rule. `screens.html` must be a working
interactive prototype, never static.

**Every animation passes the motion gate** in `references/motion-and-polish.md` §1–2 before it ships:
should-it-animate → purpose → cheapest tool → `transform`/`opacity` only → `ease-out` under 300ms (or a
spring for gestures) → interruptible, exits the way it entered → reduced-motion + hover gating. Keep it
inside the 16ms/frame budget; never animate a non-composite property or a whole long list.

---

## Phase 19 — Usability Testing & External Critique

> Read `references/phase-6-usability-testing.md` for formal test plans.

**Mandatory** — or a cognitive walkthrough + heuristic evaluation if no participants (1–2 hours, no
users needed).
1. Plan: 3–5 test objectives + task scenarios
2. Test: 3–5 sessions (moderated / unmoderated / hallway / self-applied)
3. Log: 🔴 Critical · 🟠 Serious · 🟡 Minor · ✅ Positive
4. Fix all Critical before delivery

### External Critique Protocol (run after self-critique)

Apply these two tests on every key screen — they simulate what a real reviewer would catch:

**First Impression Test (5-second rule)** — cover the screen, uncover for exactly 5 seconds, then answer:
- What drew the eye first? (Is it the primary action / most important element?)
- What is the product's purpose? (Could a stranger answer this instantly?)
- What is the emotional reaction? (Trustworthy? Cluttered? Exciting? Generic?)
- What is the single most memorable element?

If purpose is unclear in 5 seconds → visual hierarchy failure. Redesign before proceeding.

**Reading Flow Analysis** — trace the natural eye path (F-pattern for content, Z-pattern for landing pages):
- Does the flow land on the primary CTA at the right moment?
- Are there competing focal points pulling attention away from the goal?
- Does the visual weight hierarchy match the information hierarchy?

Document as: Eye lands on [X] → moves to [Y] → action point at [Z]. If this path doesn't guide toward the
primary goal, adjust sizing / contrast / spacing before handoff.

---

## Phase 20 — Web Compliance Audit *(web projects only)*

Fetch live guidelines before producing delivery files:
```
https://raw.githubusercontent.com/vercel-labs/web-interface-guidelines/main/command.md
```
Categorize findings: 🔴 Block (must fix) · 🟡 Warn (should fix) · ℹ️ Note. Fix all 🔴 Block before Phase 24.

### SEO-as-UX Layer *(apply to all web projects)*

SEO and UX share the same goal: help users find and use what they need. Treat SEO as a UX discipline:
- **Page titles**: 50–60 characters · describe content AND user intent
- **Meta descriptions**: 150–160 characters · primary keyword + clear benefit + implicit CTA
- **Heading hierarchy**: one H1 per page · H2/H3 follow a logical outline · headings describe content
- **Core Web Vitals → UX metrics**: LCP < 2.5s · INP < 200ms · CLS < 0.1
- **Semantic HTML**: `<nav>`, `<main>`, `<article>`, `<button>` — improves SEO and accessibility
- **Image alt text**: describe content — serves screen readers and image search
- **URL structure**: readable paths (`/products/running-shoes`) not IDs (`/p?id=4821`)
- **Internal linking**: key features linked from multiple pages

Document any SEO-affecting design decisions (SPA without SSR, heavy JS-rendered content) in the handoff.

---

# STAGE: POST-DESIGN DOCS

## Phase 21 — UI ↔ Requirement Traceability

> Read `references/product-delivery.md`.

Now that the screens are final, build the **traceability matrix**: every FRD requirement (Phase 6) ↔ the
screen that satisfies it ↔ the UAT scenario that tests it. Any requirement with no screen, or any screen
with no requirement, is a gap to resolve before UAT.

---

## Phase 22 — Acceptance Testing (UAT)

> Read `references/product-delivery.md`.

Write acceptance scenarios on the **approved screens**, in Given/When/Then form, one per acceptance
criterion from the FRD. Trigger on "write UAT" or after FRD + final screens are approved.

---

## Phase 23 — Security Review

> Read `references/product-delivery.md`.

Review against OWASP Top 10, map auth flows, and design the permission states on the actual screens
(logged out / logged in / insufficient permission / expired session). Security requirements from the FRD
(Phase 6) get verified here against the real UI.

**Apple-platform code review** (when delivering iOS/macOS code): run `references/apple-hig/code-audit.md`
against the source — it catches hand-drawn Apple Pay buttons and marks (must use the system API), Liquid
Glass misuse, and code that blocks iPhone Duo adaptation, each with its citation and the correct
replacement. Fold any findings into the Phase 25 handoff.

---

# STAGE: DELIVERY & LAUNCH

## Phase 24 — Delivery Package

**Step 0 — Ask the output format FIRST (always, via AskUserQuestion).** What the user gets depends on this
answer, so ask before producing anything:

> "ما صيغة المخرج الذي تريده؟
> 1. منصة كاملة في ملف HTML واحد يفتح في المتصفح
> 2. ملفات منفصلة (دراسة حالة / شاشات / بيرسوناز / هاندأوف …)
> 3. أصول للتطوير (كود حسب الستاك)"

Route by the answer:

### Format 1 — Self-contained HTML (any surface)
Read `references/single-file-platform.md`. The deliverable is **one self-contained `.html`** that opens
offline by double-click, with **fonts, icons, and images embedded inside it** — but *what it contains
matches what the user asked for*, it is not always the whole platform.

**Ask the scope first (AskUserQuestion)** — the answer decides what gets built:
> "ماذا أصمّم لك كملف HTML؟
> 1. صفحة هبوط · 2. داشبورد · 3. شاشات موبايل · 4. منصة كاملة · 5. شاشة محدّدة أخرى
> وهل تريده ريسبونسيف (موبايل + ديسكتوب) أم بعرض واحد؟ (ولو لم يُحسم سابقاً: لايت/دارك)"

Then build exactly that surface: a landing page → the full landing page; a dashboard → the dashboard; mobile
→ the phone screens; full platform → every screen with a `showScreen` router. Everything inline
(CSS/JS/fonts/icons), every image base64 via Phase 15A + `embed_images.py`. Full quality bar (tokens, the
chosen responsive scope, motion gate, RTL, WCAG, humanized copy). Verify it renders offline (screenshot it)
before delivering, then offer to persist it as an artifact with a stable URL (ask first).

### Format 2 — Separate files
**Ask Tech Stack first (if screens.html or handoff.html is needed):**
1. HTML/CSS (default) · 2. React/Next.js · 3. Vue/Nuxt · 4. Svelte · 5. Tailwind · 6. shadcn/ui ·
7. SwiftUI · 8. Flutter · 9. React Native

**Then ask which file:**
> "أي ملف تحتاجه الآن؟
> 1. casestudy.html | 2. screens.html | 3. personas.html
> 4. process.html | 5. handoff.html | 6. brd.html | 7. frd.html | 8. كل الملفات"

### Format 3 — Dev assets (code)
Ask the Tech Stack (same list as Format 2). Deliver the component/code files in that stack for the developer
to integrate — this goes to the workspace folder as code, not an in-browser demo. Name any needed library
per the Library-choice note below, and carry the handoff specs from Phase 25.

**For Format 2, load ONLY the template for what was requested:**
- casestudy → `references/templates/shared-base.md` + `references/templates/casestudy-template.md` + `references/case-study-insights.md`
- screens → `references/templates/shared-base.md` + `references/templates/screens-template.md`
- personas → `references/templates/shared-base.md` + `references/templates/personas-template.md`
- process → `references/templates/shared-base.md` + `references/templates/process-template.md`
- handoff → `references/templates/shared-base.md` + `references/design-handoff.md`
- brd/frd → `references/templates/shared-base.md` + `references/templates/frd-template.md`
- index → `references/templates/index-template.md`
- Quality check → `references/templates/quality-checklist.md`

**Images**: if the requested file contains any imagery (screen heroes, persona portraits, case-study
mockups), run Phase 15A for it before delivering — the file ships either with real Gemini images or with
labeled placeholders plus `صور-البرومبتات.md` beside it. Never with empty boxes and no prompts.

**Screen mockups** (case study + delivery): don't present bare screenshots. Read `references/mockups.md`
and frame each key screen in a device frame — render the screen HTML to a PNG, then run
`references/scripts/composite_mockup.py` (`--frame phone|laptop|browser`, background from the Phase 12
palette). The compositor preserves the design pixel-for-pixel (no AI), so just run it and use the framed
PNGs as the case-study hero and the `index.html` cover. Offer the AI-scene variant (via Phase 15A) only
when the user wants a photographic look and accepts slight drift.

**Library choice**: if the build needs a solved-problem capability (toasts, command menu, drag-and-drop,
charts, list virtualization, complex state, dates), name the library in the handoff with a one-line why —
don't leave it to the first npm result. See `references/motion-and-polish.md` → Library choice (the
standalone **pick-ui-library** skill carries the current picks by category).

After producing a file, ask: "هل تحتاج ملفاً آخر؟"

---

## Phase 25 — Developer Handoff

> Read `references/design-handoff.md` — Content Specifications (character limits + truncation per
> element), Edge Cases (100+ items, RTL strings, long unbroken strings, empty/error/offline), and the
> "Why" Rationale format. For bilingual projects always include the RTL notes section
> (`references/rtl-arabic.md`).

Create `handoff.html`: Design Token Reference · Component Specs · Screen Inventory · Interaction Specs ·
Responsive Breakpoints · **Content Specifications** · **Edge Cases** · Accessibility Notes · Arabic/RTL
Notes · **"Why" Rationale** for every non-obvious sizing, color, or interaction decision.

**Name every motion precisely** in the Interaction Specs using the motion-vocabulary table in
`references/motion-and-polish.md` (scale-in, shared-element transition, stagger, rubber-banding, ease-out,
spring…) so the developer builds the intended motion, not a guess. For native code handoffs: SwiftUI →
invoke the **write-swift** skill directly; React Native / Expo → invoke the **animate-expo** skill.

---

## Phase 26 — Staging & Canary

> Read `references/product-delivery.md`.

Smoke tests + a final UAT pass + a **Go/No-Go report** (Lighthouse ≥ 90) + canary deploy plan.

---

## Phase 27 — Launch

> Read `references/product-delivery.md`.

App Store assets (native) + web launch checklist + post-launch monitoring.
**Post-Launch (Day 30)**: design metrics review — conversion before/after, task completion rate,
drop-off analysis, A/B test results, design debt triage. See `references/product-delivery.md` →
*Post-Launch Design Metrics & A/B Testing Framework*.

---

> ### 🔖 Checkpoint A — end of the research session (after Phase 4)
> ```
> PROJECT CONTEXT SNAPSHOT — [Project Name]
> Problem Statement: [one sentence]
> Target User: [primary persona]
> Platform: [iOS / Android / Web]
> Top 3 Competitors: [name + weakness]
> Key User Pain: [2-3 problems]
> Business Model: [how it makes money, in one line]
> Complexity: [Quick / Standard / Full] | Bilingual: [Yes / No]
> Next Step: Phase 5 — BRD
> ```

> ### 🔖 Checkpoint B — end of the design session (after Phase 17)
> ```
> DESIGN CONTEXT SNAPSHOT — [Project Name]
> Design School: [style] | Primary: [hex] | Secondary: [hex] | Accent: [hex]
> Font: [name] | Ratio: [1.200 / etc.] | Icons: [library]
> Dark Mode: [Light / Dark / Both / Deferred]
> Design Direction Statement: [the unforgettable differentiator]
> Screens Completed: [list] | Screens Remaining: [list]
> Accessibility: [all 🔴 Critical fixed? Yes/No]
> Next Step: Phase 18 — Interactive Prototype
> ```

---

## Final QA Checklist

Before handing off, verify:

**Design System**
- [ ] Design school consistent across all screens
- [ ] Tokens used everywhere — no hardcoded hex/px values
- [ ] 8pt grid applied — no arbitrary spacing
- [ ] Single icon library used — zero emojis anywhere
- [ ] Design Direction Statement visible in at least one deliverable
- [ ] Font is NOT Inter/Roboto/Arial/Space Grotesk used as hero/display font (unless justified in writing)
- [ ] Color scheme avoids generic AI patterns (purple-on-white gradient, AI pink/indigo)

**Interaction Quality**
- [ ] `cursor: pointer` on every clickable/interactive element
- [ ] Hover transitions: 150–300ms (not instant, not sluggish)
- [ ] Every interaction produces visible feedback within 100ms
- [ ] All states defined: default / hover / active / disabled / focus / error / loading
- [ ] Glass card opacity ≥ 80% (`bg-white/80` or higher) in light mode — not translucent
- [ ] Motion passes the gate (motion-and-polish.md): `transform`/`opacity` only, `ease-out` not `ease-in`, under 300ms, interruptible, exits as it entered — nothing animated just to decorate
- [ ] Polish pass done: optical centering, concentric nested radii, borders vs shadows doing the right job
- [ ] 10-block motion review passed (motion-and-polish.md §Phase 17) — no unjustified, high-frequency, `ease-in`, over-300ms, or layout-property animations left
- [ ] Every interaction spec names the motion by its exact term (handoff), not a vague description

**Accessibility (WCAG 2.1 AA)**
- [ ] All text passes 4.5:1 contrast ratio
- [ ] Non-text contrast ≥ 3:1 (icons, borders, focus rings)
- [ ] Focus indicator visible on every focusable element
- [ ] 200% zoom test passed
- [ ] Keyboard-only navigation tested
- [ ] Touch targets minimum 48×48px
- [ ] Links distinguishable by more than color alone (underline, icon, or shape)

**Responsive**
- [ ] Tested at all 4 breakpoints: 375px · 768px · 1024px · 1440px
- [ ] Borders visible in both light and dark modes at every breakpoint
- [ ] Web-on-mobile fixes applied (motion-and-polish.md §4): `100dvh`, 16px input font, `touch-action: manipulation`, gated `:hover`, safe-area insets, `overscroll-behavior` — phone-only items flagged

**Content**
- [ ] Real content everywhere — no lorem ipsum, no gray placeholder boxes
- [ ] Empty states defined: what this space is + why empty + how to start
- [ ] Error messages say what to do, not just what went wrong
- [ ] Copy humanized (humanize-copy.md): no AI tells in AR or EN — no "Elevate/Seamless/Unlock", no forced triads; no "تم إجراء"/المصدر المتراكم/التضخيم
- [ ] Worst-case pass done (stress-test.md): long Arabic names, unbreakable emails, "1 member", missing avatar, 1,000 rows, every-status-at-once — no overflow, clipping, or wrong plural
- [ ] Numbers use tabular figures + locale formatting; no raw `NaN`/`undefined`, no "1 members"
- [ ] Every image is Gemini-generated from the project's own style + color tokens — no stock URLs, no gray boxes
- [ ] `images.json` and `صور-البرومبتات.md` exist, and every image in the HTML has a prompt in the sheet
- [ ] Every `<img>` has real `alt` text describing the content
- [ ] Persona portraits present — no default avatar circles
- [ ] Gemini sparkle removed from every generated image
- [ ] Any remaining placeholder labeled "(AI placeholder — generate from صور-البرومبتات.md before launch)"
- [ ] Figma-bound copies run through `embed_images.py` — images inlined, not linked

**Technical**
- [ ] `prefers-reduced-motion` on all microinteractions
- [ ] Arabic RTL renders correctly (`dir="rtl"`) *(bilingual projects only)*
- [ ] Prototype navigation works — all screens reachable
- [ ] Dark mode verified in both themes (if selected)
- [ ] All HTML files link via `index.html`
- [ ] Lighthouse score ≥ 90 for Performance + Accessibility *(web projects)*

**For Web Projects**: Phase 20 audit completed — all 🔴 Block findings resolved.

**See `references/templates/quality-checklist.md`** for the full detailed checklist organized by section.

---

## Rules (Non-Negotiable)

- Run the 27 phases in order — structure before skin, requirements before wireframes
- No lorem ipsum anywhere
- No UI before UX is approved
- No wireframes before BRD/FRD are approved (Standard/Full projects)
- No hardcoded hex values — always CSS tokens
- No arbitrary spacing — 8pt grid only
- No emojis — use the selected icon library
- No mixed icon libraries
- No reading any Figma file without telling the user first and getting a clear yes — name the file and scope, then pull only that (`references/figma-tokens.md`)
- No gray placeholder boxes in deliverables
- No stock-photo URLs or `via.placeholder.com` — images come from Gemini via Phase 15A
- No image without its prompt handed to the user (file + chat), even when the automation succeeded
- No opening a browser to generate images without asking first
- No Gemini sparkle left in a shipped image
- No font/typescale chosen without asking the user first
- No design school skipped
- No static screens — `screens.html` must be an interactive prototype
- No skipping the Phase 24 output-format question — always ask (single-file platform / separate files / dev code) before producing delivery output
- No single-file platform that needs the internet — CSS, JS, fonts, icons inline and every image base64; it must open offline from disk (`references/single-file-platform.md`)
- No dark mode as an afterthought — if selected, both themes verified
- No generic AI aesthetics — every design must have a specific, intentional differentiator
- No Inter/Space Grotesk as the hero/display font without explicit justification (using the Untitled UI saved system IS that justification — see `references/saved-design-systems.md`)
- No `cursor: default` on interactive elements — always `cursor: pointer`
- No hover transitions under 150ms or over 300ms
- No purple-on-white gradients or AI pink/indigo gradients without strong product rationale
- No design that cannot answer: "What is the one thing the user will remember from this interface?"

---

## Tone & Communication

- Explain each phase before starting it
- Show reasoning, not just outputs
- Label assumptions clearly: "(Assumption: based on typical behavior)"
- Confirm key decisions before building on them
- Use simple language; avoid jargon unless the user is technical
- Bilingual: only apply if the user selected "نعم" in Step 0B

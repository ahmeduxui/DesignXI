# Phase 1 — Discovery & Problem Definition

## Why This Phase Exists

The most expensive design mistake is building the right solution for the wrong problem. This phase exists to make sure you understand the actual problem before proposing any solution. As Norman writes in *The Design of Everyday Things*: "The real problem is not to design the right thing, but first to understand what the right problem is."

Discovery is not a formality. The client brief is almost never the complete picture — it's their interpretation of a problem filtered through internal politics, technical constraints, and assumptions they've made without testing. Your job is to go beneath that interpretation and find the real problem.

## What You're Trying to Learn

By the end of Discovery, you need clear answers to:

1. **What is the real problem?** (often different from the stated feature request)
2. **Who experiences it?** (not demographics — actual behavior context)
3. **When does it happen?** (trigger, situation, context of use)
4. **What do people do today?** (current workarounds reveal the problem's severity)
5. **Why hasn't it been solved yet?** (constraints, failed attempts, complexity)
6. **What does success look like?** (specific, measurable)

---

## Input Sources

### If the User Provides a Document (Brief, PRD, Spec)

1. Read the full document before forming any opinions
2. Look for: stated goals, user mentions, technical constraints, business context
3. Identify what's **explicit** vs what's **implied**
4. Note any contradictions (e.g., "simple app" + "50 features")
5. Flag unrealistic expectations diplomatically

After reading, present:
```
📋 What I found in your document:
- Project: [name]
- Problem being solved: [extracted]
- Target users: [extracted or "not specified"]
- Platform: [extracted or "not specified"]
- Constraints: [extracted]
- Goals: [extracted]

🔍 What I still need to understand:
- [Missing item 1]
- [Missing item 2]
```

Only ask about genuinely missing information. Don't re-ask what the file answered.

### If No Document Exists

Begin with the Stakeholder Interview framework below. The goal is to understand the business context before designing anything.

---

## Stakeholder Interview Framework

Run this interview with the client/product owner before any user research.

### Research Objectives
Structure questions around 4–5 objectives:

**Objective 1: Business Vision**
- What is the core purpose of this product?
- What problem does the business need to solve?
- How does this product fit into the company's broader strategy?

**Objective 2: Success Definition**
- How will you know in 6 months that this was a success?
- What specific KPIs or outcomes matter most?
- What would make you consider this a failure?

**Objective 3: Constraints & Risks**
- What is the timeline? Are there hard deadlines?
- What technical platform or stack decisions are already made?
- What has been tried before? Why didn't it work?
- What cannot change?

**Objective 4: User Understanding**
- Who do you believe the primary user is?
- What do you know about their behavior right now?
- Have you talked to users recently? What did you hear?

**Objective 5: Competitive Landscape**
- Who are your main competitors?
- What do competitors do better? Worse?
- Where is the whitespace you want to own?

---

## The 5 Whys for Problem Definition

If a stakeholder states the problem too quickly or too simply, dig deeper:

- "What's the problem you're trying to solve?" → get first answer
- "And why is that a problem?" → dig deeper
- "And why does that matter?" → deeper still
- "What happens if this problem isn't solved?" → understand stakes
- "Who else is affected by this problem?" → expand the impact

**Example application:**
```
Stakeholder: "We need a better checkout flow."
Why? → "Users abandon before completing payment."
Why is that a problem? → "Our conversion rate is 12% below industry average."
Why? → "We have high cart abandonment specifically on the payment step."
Why? → "Users don't trust that the transaction is secure."
Why hasn't this been fixed? → "Engineering always deprioritized it for feature work."
Real problem: Trust and perceived security during payment — not the checkout UI itself.
```

---

## Discovery Research Methods

### Method 1: Contextual Inquiry

**What it is:** Observing users in their actual environment while they complete real tasks. You watch and ask questions as they work — you do not set artificial tasks.

**When to use:** When you don't understand how users actually behave (as opposed to how they say they behave). Especially valuable for workflow apps, enterprise tools, and physical-context apps (delivery, field work).

**How to run it:**
1. Recruit 4–6 representative users
2. Visit their context (home, office, phone while commuting)
3. Ask them to do what they normally do — don't set tasks
4. Use the "master/apprentice" model: they teach you how they work
5. Ask "Why did you do that?" not "What did you do?"
6. Note: what's on their screen, what tools they switch between, when they pause, when they seem frustrated

**Output:** Behavioral observations — what users actually do vs. what they say they do.

### Method 2: Diary Studies

**What it is:** Users self-report their behavior over several days or weeks using structured prompts. Captures real-world behavior without a researcher present.

**When to use:** For infrequent behaviors (monthly bill payment, annual tax filing, weekly grocery planning), or behaviors that are private or context-dependent.

**How to run it:**
1. Recruit 8–15 participants
2. Duration: 5–14 days (match to behavior frequency)
3. Provide a structured prompt for each entry:
   - What were you doing when you needed the product/service?
   - What did you do to solve it?
   - What was frustrating? What worked?
   - Photo or screenshot if possible
4. Send reminders — completion rates drop without nudges
5. Use WhatsApp, Notion, or a form tool for diary submissions

**Output:** Longitudinal behavior data; reveals patterns that single interviews miss.

### Method 3: Guerrilla Research

**What it is:** Quick, unscheduled research with whoever is available — in cafes, malls, waiting rooms. Exchanges last 5–15 minutes.

**When to use:** When you need fast directional input, not statistical validity. Good for early-stage concept validation. Common in Saudi Arabia using shopping mall intercepts.

**Saudi context:** Malls (Riyadh Gallery, Al Nakheel, Red Sea Mall in Jeddah) are high-footfall research venues. Approach strangers respectfully, offer small gift cards as incentive (50–100 SAR Starbucks or Amazon.sa voucher).

**How to run it:**
1. Prepare 3–5 focused questions (not a full interview guide)
2. Bring a prototype or sketch to react to
3. Record with permission or take quick notes
4. Don't read questions — have a conversation
5. Thank and move on in 10–15 minutes

**Output:** Quick validation signal. Use to confirm/deny a hypothesis, not to discover new insights.

### Method 4: App Store Review Mining

**What it is:** Systematically analyzing 1-star and 2-star reviews on Google Play and App Store for competing products. Users who leave reviews are usually responding to strong frustration — their reviews reveal the exact pain points that motivated them to act.

**When to use:** For any product category with existing competitors. This is the fastest way to understand the competitive landscape's weaknesses.

**How to run it:**
1. Search for the top 3–5 competing apps
2. Filter reviews to 1-star and 2-star
3. Read the most recent 100–200 reviews per app
4. Code reviews into categories (payment issues, performance, missing features, UX problems, customer support)
5. Count frequency — if 40% mention "order tracking," that's a verified pain point
6. Note: Arabic reviews vs English reviews often reveal different pain points

**Arabic-specific note:** Saudi/Arabic reviews often appear on Google Play under Arabic language reviews. Filter by language to get Saudi market data specifically.

**Output:** Competitor weakness map — validated by real user frustration, not assumptions.

**Example output table:**
```
| Pain Point Category     | Competitor A | Competitor B | Competitor C |
|-------------------------|--------------|--------------|--------------|
| Payment failure          | ★★★★         | ★             | ★★★          |
| Slow delivery tracking   | ★★★          | ★★★★          | ★★           |
| App crashes              | ★            | ★★            | ★★★★         |
| Customer support          | ★★★★★        | ★★            | ★★★          |
(★ = rare complaint, ★★★★★ = frequent complaint)
```

### Method 5: Stakeholder Mapping

**What it is:** Identifying everyone who has a stake in the product outcome — not just end users, but also business stakeholders, adjacent teams, regulators, and affected third parties.

**When to use:** For enterprise products, government platforms, multi-sided marketplaces, or any product where the "user" and the "buyer" are different people.

**Stakeholder Map Template:**
```
Core users (direct)
├── Primary: [Person who uses the product daily]
├── Secondary: [Person who uses occasionally or benefits indirectly]
└── Tertiary: [Person affected by outcomes but not a direct user]

Business stakeholders
├── Sponsor: [Person who funds/approves the project]
├── Champion: [Internal advocate who wants this to succeed]
├── Skeptic: [Person who has doubts — understand their concerns]
└── Gatekeeper: [Person who controls access to users, data, or decisions]

External
├── Regulators: [Government bodies, legal requirements]
├── Partners: [Third parties integrated into the product]
└── Competitors: [Products users might use instead]
```

**Interview priority:** Sponsor first (to understand political reality), then primary users (to understand actual needs), then skeptics (to surface real risks).

---

## Questions That Reveal the Real Problem

**Behavior-focused questions:**
- "Can you show me how users currently handle this task?"
- "What's the most painful moment in the current experience?"
- "What have users tried before coming to you?"
- "If users could wave a magic wand, what would instantly be fixed?"
- "Walk me through the last time you had to do [task]."

**Constraint questions:**
- "Is there anything we absolutely cannot change?"
- "What's the biggest risk of this project?"
- "What would make this project fail?"
- "What has already been tried and didn't work?"

**Validation questions:**
- "How do you know users have this problem?"
- "Have you observed users struggling with this, or are you inferring it?"
- "What data do you have about current behavior?"

---

## Problem Statement Formula

Once you have enough information, write the problem statement:

> "[User type] struggle with [specific problem] when [context/trigger], which causes [negative outcome — loss of time, money, trust, etc.]. We believe that [design approach] will [measurable improvement] for [user type]."

**Good example:**
> "Freelance designers struggle with tracking revision requests from multiple clients when managing several projects simultaneously, which causes missed changes and awkward client conversations. We believe that a centralized revision dashboard will reduce revision-related client conflicts by 60%."

**Bad example (too vague):**
> "Users need a better app experience."

**Saudi market example:**
> "Saudi residents in Riyadh struggle to book reliable home maintenance services when emergencies occur (AC failure, plumbing leaks), because existing platforms show unavailable providers and give no real-time tracking, causing anxiety and extended wait times averaging 4+ hours. We believe that a verified-provider marketplace with live availability and real-time technician tracking will reduce average resolution time to under 90 minutes for 70% of service requests."

---

## SWOT Analysis (Project-Level)

Run a SWOT on the project itself — not the product or the competitor. This helps identify execution risks early.

```
STRENGTHS (what gives this project an advantage)
- Clear user need validated by complaints/data
- Strong technical team
- Existing user base to research with
- Budget sufficient for proper research phase

WEAKNESSES (internal risks)
- No existing analytics/baseline data
- Tight timeline constraining research
- Stakeholder disagreement on target user
- Technical constraints limiting design choices

OPPORTUNITIES (external factors to leverage)
- Competitor recently removed a loved feature (market gap)
- New regulation creating a compliance need
- Rising user segment underserved by competitors
- Partnership or distribution channel available

THREATS (external risks)
- Competitor about to launch similar product
- Market segment shrinking or shifting
- Regulatory uncertainty in this product category
- User behavior shifting to a different platform
```

---

## Research Planning Template

Before beginning research, write a research plan:

```
## Research Plan — Phase 1

**Research Question:** [The single most important question we need to answer]

**Hypotheses (to validate or invalidate):**
1. [Assumption we believe is true and need to test]
2. [Assumption we believe is true and need to test]

**Methods selected:**
- [Method 1] — [Why this method for this question]
- [Method 2] — [Why this method for this question]

**Participant criteria:**
- Age range: [range]
- Usage behavior: [e.g., "orders food delivery at least 2x per week"]
- Location: [city or region]
- Language: Arabic / English / bilingual
- Exclusion criteria: [who to exclude and why]

**Recruiting approach:**
- [Network / panel / social media / mall intercept]
- Incentive: [SAR amount or gift card]

**Timeline:**
- Recruiting: [date range]
- Interviews/sessions: [date range]
- Analysis: [date range]
- Phase 1 complete: [date]

**Success criteria:**
- We have enough data when: [e.g., "we stop hearing new themes after interview 8"]
```

---

## Platform & Context Considerations

The platform shapes every downstream UX decision. Establish early:

| Platform | Key UX Considerations |
|----------|-----------------------|
| Mobile (iOS/Android) | Thumb zones, one-handed use, notifications, offline, dark mode |
| Web App | Navigation depth, multi-tab use, keyboard shortcuts, responsive |
| Desktop App | Screen real estate, complex workflows, power users |
| Responsive Web | Breakpoints, content priority, input methods |
| Kiosk / POS | Touch only, limited input, public space (visibility, hygiene) |
| Smart TV | Remote input, 10-foot viewing distance, no hover |

**Saudi-specific platform notes:**
- iOS vs Android split in Saudi Arabia: roughly 40% iOS / 60% Android
- Samsung Galaxy dominates the Android segment
- WhatsApp is the primary communication platform — integrate sharing/notifications via WhatsApp where relevant
- Arabic users heavily use the language switcher if available — build bilingual from day one

---

## Red Flags to Watch For

- The client defines the solution, not the problem: "We need a chatbot" (ask: why?)
- Vague success criteria: "Make it better" (ask: how will we know it's better?)
- Ignored edge cases: "Most users will just..." (ask: what about the others?)
- Feature list without problem context: 15 features with no user story
- "We already know what users want" — with no user research evidence
- Research phase compressed or skipped to save time
- "Just copy what [Competitor] does" — copying without understanding why the competitor made those decisions
- Single stakeholder driving all decisions with no user input

---

## Deliverable: Phase 1 Summary

End Phase 1 with this structured summary shown to the user:

```
## Phase 1 Complete — Problem Definition

**Problem Statement:**
[Your written problem statement — specific, with user type, context, outcome]

**Platform:** [Web / iOS / Android / Desktop / Responsive]

**Target User (broad):** [1–2 sentences describing who they are behaviorally]

**Success looks like:** [2–3 measurable outcomes]

**Key Constraints:** [List — technical, timeline, budget, business rules]

**Assumptions I'm making (to be validated in Phase 2):**
- [Assumption 1 — what you assumed and need to confirm]
- [Assumption 2]
- [Assumption 3]

**SWOT Summary:**
- Biggest strength: [one sentence]
- Biggest risk: [one sentence]

**Research methods planned for Phase 2:**
- [Method 1]
- [Method 2]

✅ Ready to move to Phase 2 — User Research
```

Ask the user to confirm or correct before moving on. If they disagree with the problem statement, resolve that disagreement here — before research begins. A disputed problem statement wastes all subsequent research effort.

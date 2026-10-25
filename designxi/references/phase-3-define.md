# Phase 3 — Define

## Why This Phase Exists

Research gives you data. Define turns data into design targets. This phase answers: "Who exactly are we designing for, and what do they need us to solve?" Without this phase, you risk designing for a ghost — an imagined user who doesn't really exist.

The outputs of this phase (personas, journey maps, HMW statements) are the contract between research and design. Every design decision in Phase 5 should trace back to something defined here.

## Persona Creation

### What Makes a Good Persona

A good persona is a **behavior archetype** — a pattern of real user behavior distilled into a named, humanized character. It is NOT:
- A demographic profile ("35-year-old male with a college degree")
- A list of features someone wants
- A made-up character with no research backing

A good persona includes behaviors, goals, frustrations, and — most importantly — a **core tension** that your design resolves.

### Persona Template

Create 1-2 personas (rarely need more). Use this structure:

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PERSONA: [Full Name]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Age: [Realistic number]    Occupation: [Job title]
Location: [City, Country]  Tech comfort: [Low / Medium / High]

Quote:
"[A sentence in their voice that captures their biggest challenge
 or mindset. This should feel real, not marketing-speak.]"

━━━ BACKGROUND ━━━
[2-3 sentences about their daily life, work context, and relationship
 to the problem domain. Not their life story — just what's relevant.]

━━━ GOALS ━━━
Primary: [The main thing they're trying to achieve]
Secondary: [A supporting goal]
Hidden goal: [What they want but may not say — e.g., "look competent to their boss"]

━━━ FRUSTRATIONS ━━━
• [Specific pain — grounded in research or clearly labeled assumption]
• [Second pain]
• [Third pain]

━━━ BEHAVIORS ━━━
• [How they currently approach the problem]
• [Tools they use, workarounds they've developed]
• [Key behavioral pattern relevant to your design]

━━━ WHAT THEY NEED FROM YOUR DESIGN ━━━
[1-2 sentences connecting their frustrations to what your solution
 must do for them. This bridges research → design decisions.]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### Anti-Patterns to Avoid

- ❌ "Techie Tim" and "Luddite Lucy" — stereotyped personas based on age or tech comfort
- ❌ Personas that sound like the client or product team
- ❌ Personas for every possible user type (pick the primary, design for them)
- ❌ Persona goals that map 1:1 to your feature list

## User Journey Map

Map the **current experience** (before your solution). This reveals where your product must intervene.

### Journey Map Structure

```
JOURNEY MAP: [Persona Name] — "[Core Task They're Trying to Accomplish]"

STAGE 1: [Awareness / Trigger]
  What they do: [Action]
  What they think: "[Thought]"
  How they feel: [Emotion — use specific words: frustrated, confused, hopeful]
  Pain points: [What's broken here]

STAGE 2: [Seeking / Research]
  What they do: [Action]
  What they think: "[Thought]"
  How they feel: [Emotion]
  Pain points: [What's broken here]

STAGE 3: [Attempting / Doing]
  What they do: [Action]
  What they think: "[Thought]"
  How they feel: [Emotion]
  Pain points: [What's broken here]  ← Highest value design intervention point

STAGE 4: [Result / Outcome]
  What they do: [Action]
  What they think: "[Thought]"
  How they feel: [Emotion]
  Pain points: [What's broken here]

STAGE 5: [Follow-up / Aftermath]
  What they do: [Action]
  What they think: "[Thought]"
  How they feel: [Emotion]
  Pain points: [What's broken here]

KEY INSIGHT FROM JOURNEY:
The biggest breakdown happens at [Stage X] when [specific moment].
This is where our design intervention will create the most impact.
```

## How Might We (HMW) Statements

HMW questions transform problems into design opportunities. They're open enough to allow creative solutions, but specific enough to be actionable.

**Formula**: "How might we [help user] [do something] [in a context or way that addresses pain]?"

### Good HMW Examples

From journey pain points, generate 3-5 HMW statements:

| Pain Point | HMW Statement |
|------------|---------------|
| "Users forget to [do X]" | "How might we remind users to [do X] without feeling intrusive?" |
| "Step 3 is confusing" | "How might we make the path to [goal] feel obvious from the start?" |
| "Users abandon at checkout" | "How might we build enough trust that users feel safe completing payment?" |
| "Error messages panic users" | "How might we turn error moments into recovery opportunities?" |

**Bad HMW examples:**
- "How might we add a dashboard?" (solution, not problem)
- "How might we make users happy?" (too vague to act on)
- "How might we use AI?" (technology first, not human first)

## Success Metrics (OKR-style)

Define 2-3 measurable outcomes your design should achieve:

```
Metric 1: [Name]
  Current state: [Baseline — if known, or "not yet measured"]
  Target: [Specific improvement, e.g., "Reduce task completion time from 8 min to under 3 min"]
  How to measure: [How you'd track this in production]

Metric 2: [Name]
  Current state: [Baseline]
  Target: [Specific improvement]
  How to measure: [Tracking method]

Metric 3: [Name]
  Current state: [Baseline]
  Target: [Specific improvement]
  How to measure: [Tracking method]
```

## Phase 3 Output

```
## Phase 3 Complete — Define

**Primary Persona:** [Name] — [One-line description]
[Full persona block]

**Secondary Persona (if applicable):** [Name] — [One-line description]
[Full persona block]

**User Journey:** [See journey map above]

**How Might We Statements:**
1. HMW [statement 1]
2. HMW [statement 2]
3. HMW [statement 3]
4. HMW [statement 4 — optional]

**Success Metrics:**
1. [Metric 1]
2. [Metric 2]
3. [Metric 3]

✅ Ready to move to Phase 4 — Information Architecture & Ideation
```

---

## Acceptance Criteria Format

Write each success metric in Given/When/Then format:
- **Given** [precondition or context]
- **When** [action the user takes]
- **Then** [expected measurable outcome]

Example: *Given a new user lands on the onboarding screen / When they complete the first 3 steps / Then 60% reach the first value moment within 5 minutes.*

## Research Synthesis Rules

- **Quantify every finding** — "7 of 10 users struggled with X" not "most users" — vague language hides signal
- Label assumptions clearly: "(Assumption — not yet validated by research)"
- Separate observations from interpretations in all research outputs
- **User Segments**: if research reveals 2+ distinct user types with different goals, each may need a separate persona
- **Research Limitations**: document what you could NOT validate — sample size, recruitment bias, missing user types — so the team knows where to invest next

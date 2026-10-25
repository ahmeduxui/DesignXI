# Phase 6.5 — Usability Testing

## Why This Phase Exists

*Handbook of Usability Testing* (Rubin & Chisnell) states it directly: "Testing with 5 users reveals 85% of usability problems." You cannot know if your design works until real people try to use it. This phase catches critical failures before they reach production — when fixing them costs almost nothing.

This phase happens **after screens are designed but before the final delivery package is produced.** Its findings feed directly back into Phase 5 corrections.

---

## What to Test

Test the **core user flows** defined in Phase 4 — not every screen, just the critical paths:

```
Priority 1 (must test): The flow that delivers the product's core value
Priority 2 (should test): The onboarding flow (first-time user experience)
Priority 3 (nice to test): The most complex or unfamiliar interaction
```

---

## Usability Test Planning

### Define the Test Objectives

Before running any test, write 3-5 specific questions the test should answer:

```
Test Objectives for [Project Name]:

1. Can a first-time user complete [core task] without assistance?
2. Does the navigation structure match how users expect to find [feature]?
3. Is the [specific screen] clear enough that users know what to do next?
4. Do users understand what [ambiguous element] means without explanation?
5. Does the onboarding flow prepare users to use the product independently?
```

### Select Test Method

Choose based on available resources:

| Method | Best for | Time required |
|--------|----------|---------------|
| **Moderated remote** (screenshare + talk-aloud) | Deep insight, "why" behind behavior | 45-60 min per session |
| **Unmoderated remote** (recorded task completion) | Scale, patterns across many users | 15-20 min per session |
| **Hallway testing** (ask anyone nearby) | Quick gut-check, early validation | 10-15 min per session |
| **Cognitive walkthrough** (self-evaluation) | When no users available | 1-2 hours total |

**Minimum viable test:** 3-5 participants per round. More is wasteful — the same problems repeat after the 5th user.

### Write Task Scenarios

Tasks must describe a **goal**, not a path. Never tell the user where to click.

```
❌ Bad task: "Click the 'New Project' button in the top right"
✅ Good task: "You've just joined a new team. Create your first project."

❌ Bad task: "Go to Settings and change your notification preferences"
✅ Good task: "You're getting too many emails from the app. Fix that."

❌ Bad task: "Find the checkout page"
✅ Good task: "You've decided to buy the Pro plan. Go ahead and do that."
```

**Task scenario template:**
```
Scenario [N]: [Task Name]

Background: "[1-2 sentences giving context — who they are, what happened, what they want]"

Task: "[What they need to accomplish — stated as a goal, not a path]"

Success criteria: [How you'll know they completed it]
Time limit: [Optional — usually 3-5 minutes]
```

---

## Running the Test

### The Moderator's Role (if running moderated sessions)

- Give the task, then be silent — don't help unless they're completely stuck
- Ask "What are you thinking right now?" when they hesitate
- Ask "What did you expect to happen?" after every confusion moment
- Never say "you're doing great" — it biases the next decision
- Note: where they look first, where they click, when they pause, when they backtrack

### The Think-Aloud Protocol

Ask participants to narrate their thoughts as they work:

```
"As you work through this, please say out loud what you're thinking —
what you're looking for, what you expect to happen, what confuses you.
There are no wrong answers. We're testing the design, not you."
```

### Cognitive Walkthrough (When No Users Available)

Walk through each task yourself, asking for each step:

1. Will users know they need to do something at this point?
2. Will they notice the correct action is available?
3. Will they know the action is the right one for their goal?
4. Will they understand the feedback after taking the action?

If the answer to any of these is "no" or "maybe" — that's a usability problem.

---

## Capturing Findings

### During the Session: Observation Log

```
OBSERVATION LOG — Session [N] — Participant: [Code name, not real name]
Task: [Task name]

Time | Observation | Type
-----|-------------|-----
0:32 | Looked at header navigation first, then scrolled down | Navigation confusion
1:15 | Clicked "Settings" instead of "New Project" | Labeling problem
2:04 | Said "I don't know where to go from here" — paused 8 seconds | Dead end
2:45 | Tried to click non-clickable card | Affordance issue
3:30 | Completed task after discovering button via back button | Workaround behavior
```

Observation types to track:
- 🔴 **Critical** — user cannot complete the task
- 🟠 **Serious** — user completes with significant difficulty or wrong path
- 🟡 **Minor** — user completes but is confused or annoyed
- 🟢 **Positive** — something that worked particularly well

### After All Sessions: Affinity Mapping

Group all observations by theme:

```
FINDINGS MAP

Theme: Navigation confusion
  - 3/5 users looked for [feature] in wrong section
  - 2/5 users didn't notice the top navigation existed
  → Root cause: navigation labels don't match user mental model

Theme: Onboarding drop-off
  - 4/5 users skipped the setup wizard
  - 2/5 users said "I'll do this later" and never returned
  → Root cause: wizard feels like a chore, not a benefit

Theme: Form friction
  - 5/5 users were confused by [field name]
  → Root cause: internal jargon used as a label
```

---

## Usability Test Report

Produce this report after completing all sessions:

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
USABILITY TEST REPORT — [Project Name]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Test date: [Date]
Participants: [N] users
Method: [Moderated / Unmoderated / Cognitive walkthrough]
Flows tested: [List]

─── TASK COMPLETION RATES ───
Task 1: [Name] — [N/N] users completed — [%] success
Task 2: [Name] — [N/N] users completed — [%] success
Task 3: [Name] — [N/N] users completed — [%] success

─── CRITICAL ISSUES (must fix before delivery) ───
🔴 Issue: [Description]
   Observed in: [N/N] sessions
   Screen: [Which screen]
   Root cause: [Why it happens]
   Fix: [Specific design change]

🔴 Issue: [Description]
   ...

─── SERIOUS ISSUES (fix in next iteration) ───
🟠 Issue: [Description]
   Observed in: [N/N] sessions
   Fix: [Specific design change]

─── MINOR ISSUES (polish) ───
🟡 Issue: [Description]
   Fix: [Small adjustment]

─── WHAT WORKED WELL ───
✅ [Positive finding — don't change this]
✅ [Second positive finding]

─── RECOMMENDED FIXES (prioritised) ───
Priority 1: [Fix critical issue X] — affects [N/N] users
Priority 2: [Fix critical issue Y] — affects [N/N] users
Priority 3: [Improve serious issue Z]

─── VERDICT ───
[ ] Ready to deliver — no critical issues found
[ ] Fix critical issues, then deliver (estimated: [time])
[ ] Major redesign needed for [specific flow] before delivery
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## After Testing: Iteration Loop

For every **Critical** issue found:
1. Identify the root cause (don't patch the symptom)
2. Revisit the wireframe or UI decision that caused it
3. Apply the fix to the affected screen(s)
4. Re-test with 2-3 users if the fix changes a core flow

For **Serious** issues: fix if time allows, document for next sprint if not.
For **Minor** issues: document and fix during the QA phase.

**Lean UX principle** (*Lean UX* — Jeff Gothelf): one round of testing and one round of fixing is enough before shipping. Don't delay launch waiting for perfection — ship the improved version, collect real-world data, and continue improving.

---

## Iteration Checkpoint (From Lean UX + Getting Real)

Before declaring the design done, answer these questions:

```
ITERATION CHECKPOINT

□ Have the critical usability issues been fixed?
□ Does the core user flow work without assistance for 4/5 users?
□ Are the error states and empty states complete and helpful?
□ Is the onboarding clear enough for a new user to understand value in 60 seconds?
□ Has the design been checked against the psychology principles checklist?
□ Has the grid been applied consistently across all screens?
□ Are all color combinations WCAG AA compliant?

If all boxes are checked → proceed to Phase 6 (Delivery Package)
If not → fix, document why, then proceed
```

---

## When No Users Are Available

If the user cannot conduct any usability testing (time, access, or resources), apply this minimum viable alternative:

1. **Heuristic Evaluation** — evaluate each screen against Nielsen's 10 heuristics:
   - Visibility of system status
   - Match between system and real world
   - User control and freedom
   - Consistency and standards
   - Error prevention
   - Recognition rather than recall
   - Flexibility and efficiency
   - Aesthetic and minimal design
   - Help users recognise, diagnose, and recover from errors
   - Help and documentation

2. **5-Second Test (self-applied)** — for each key screen: look at it for 5 seconds, look away, and answer: "What is this screen for? What can I do here? What should I do first?" If the answers aren't clear — the hierarchy or copy needs work.

3. Document any identified issues in the test report as "Heuristic evaluation findings" rather than "User observations."

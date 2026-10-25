# Phase 2 — User Research

## Why This Phase Exists

You cannot design for someone you don't understand. As Steve Portigal writes in *Interviewing Users*: "The goal of research is not to confirm what we already think — it's to be surprised by what we didn't expect." This phase exists to ground your design decisions in real human behavior, not assumptions.

Research doesn't have to be perfect or extensive. Even 3-5 conversations will transform the quality of your design decisions.

## Research Modes (Choose Based on What You Have)

### Mode A: User Has Research Data
If the user provides interview notes, survey results, analytics, support tickets, or any user data:
1. Read all data carefully
2. Look for patterns (what appears more than once?)
3. Look for extreme cases (the most frustrated user, the most satisfied user)
4. Identify the top 3 unmet needs
5. Note any surprising behaviors that challenge assumptions

### Mode B: No Research Data Yet
If no research exists, provide the user with tools to go gather it:

**5-Question Interview Guide** (provide this to the user):

```
Interview Guide for [Project Name]
Time: 20-30 minutes per person
Goal: Understand how people currently [task related to problem]

Questions:
1. "Tell me about the last time you [did the task related to the problem].
   Walk me through what happened."
   (Get them to tell a story — stories reveal real behavior)

2. "What's the hardest part of [this task] for you?"
   (Let them define the pain, don't suggest it)

3. "What do you do when [pain point from Q2] happens?"
   (Current workarounds = unsolved problems = design opportunities)

4. "Have you tried any tools or apps to help with this? What happened?"
   (Reveals alternatives they've explored and why they weren't enough)

5. "If this was magically fixed, what would your day look like differently?"
   (Helps define the real value of the solution)

Tips for interviewing:
- Don't ask "would you use this?" — it's a bad predictor of behavior
- Ask "what did you do" not "what do you do" — past is more honest than hypothetical
- Silence is ok — give people 5 seconds to think before filling the gap
- Say "tell me more" when you hear something interesting
```

### Mode C: Synthesized Research (AI-Assisted)
If the user cannot conduct interviews, synthesize realistic behavior based on:
- The problem statement from Phase 1
- General knowledge of the domain
- Comparable products and their known user issues

**Always label synthesized insights clearly:**
> ⚠️ Assumption (not from real research): Based on typical behavior in [domain], users likely...

## Competitive Analysis (Live Web Search Required)

Always conduct a live competitive analysis using WebSearch. Do not rely on general knowledge alone — market landscapes change, and real current products reveal real current patterns.

### Search Strategy

Run these searches (adapt keywords to the project):

```
Round 1 — Discover who's in the space:
"best [product category] apps [current year]"
"top [product category] tools for [user type]"
"[product category] alternatives comparison"

Round 2 — Dig into specific competitors found:
"[competitor name] review features"
"[competitor name] UX problems users complain about"
"[competitor name] app store reviews"

Round 3 — Look for industry analysis:
"[product category] UX design case study"
"[product category] product teardown"
"[product category] design patterns"
```

### What to Extract Per Competitor

For each of the 3-5 competitors discovered:

```
Competitor: [Name]
URL: [Website or App Store link]
Platform: [iOS / Android / Web / Cross-platform]
Value proposition: [What they claim to do in one sentence]
Target audience: [Who they serve]
Pricing model: [Free / Freemium / Paid / Subscription]

Core features:
  - [Feature 1]
  - [Feature 2]
  - [Feature 3]

What users love (from reviews/comments):
  - [Praise point 1]
  - [Praise point 2]

What users complain about (from reviews/comments):
  - [Pain point 1] ← These are your design opportunities
  - [Pain point 2]

Visual direction: [Minimal / Bold / Corporate / Playful / Dark / Light]
Design quality: [High / Medium / Low + brief note]
```

### Competitive Gap Analysis

After analyzing all competitors, identify:

```
Gaps in the market (nobody does this well):
1. [Gap 1]
2. [Gap 2]

Table stakes (everyone does this — you must too):
1. [Feature/pattern that's expected]
2. [Expected pattern 2]

Our differentiation opportunity:
[What we can do better than anyone currently in the market,
 based on real evidence from the competitive research]
```

---

## App Store & Google Play Review Analysis (Deep Dive — Mandatory for Mobile Projects)

This is one of the most powerful and underused research sources in UX. Real users leave brutally honest feedback on App Store and Google Play — frustrations, missing features, bugs, and workarounds they've invented. This is primary research you didn't have to conduct yourself.

**Run this for every competitor found in the competitive analysis above.**

### Step 1: Find the App Store / Play Store Listing

Use WebSearch to locate each competitor's store listing:

```
Search queries:
"[App Name] Google Play Store"          → gets play.google.com link
"[App Name] Apple App Store"            → gets apps.apple.com link
"[App Name] site:play.google.com"
"[App Name] site:apps.apple.com"
```

Then use WebFetch to load the actual store page and extract:
- Overall rating (e.g., 4.2 ★)
- Number of ratings (scale indicator — 10K vs 1M tells you market size)
- Rating breakdown if visible (how many 1-star, 2-star, etc.)
- App description (what they claim to offer)
- Last update date (tells you if the team is active)

### Step 2: Find & Read User Reviews

Since store pages paginate reviews, use these search strategies to surface them:

```
WebSearch queries for Google Play reviews:
"[App Name] google play reviews complaints"
"[App Name] google play 1 star"
"[App Name] android review \"not working\" OR \"bug\" OR \"missing\""
site:play.google.com/store/apps [App Name] reviews

WebSearch queries for App Store reviews:
"[App Name] app store reviews problems"
"[App Name] ios review \"wish\" OR \"missing\" OR \"please add\""
site:apps.apple.com [App Name]

Also search Reddit for authentic user voices:
site:reddit.com "[App Name]" review OR problem OR bug OR feature request
"[App Name] reddit" complaints OR issues OR alternative
```

Use WebFetch on review aggregator pages when found (e.g., AppFollow, AppBot, SensorTower public pages, or any page that lists multiple reviews).

### Step 3: Classify Every Review Found

For each review or complaint collected, tag it into one of these categories:

```
🔴 BUG / CRASH          → Technical failure affecting core function
🟠 MISSING FEATURE      → Something users want that doesn't exist yet
🟡 UX CONFUSION         → User couldn't figure out how to do something
🟢 PERFORMANCE ISSUE    → Slow, laggy, drains battery, large file size
🔵 ONBOARDING PROBLEM   → Confusing setup, hard to get started
🟣 TRUST / PRIVACY      → Concerns about data, permissions, payments
⚪ GENERAL PRAISE       → What they love (keep this, don't break it)
```

### Step 4: Build the Reviews Intelligence Report

After collecting and tagging reviews from all competitors, produce this report:

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
APP STORE INTELLIGENCE REPORT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

APP: [Competitor Name]
Rating: [X.X ★] — [Number] ratings
Platform: [iOS / Android / Both]
Last updated: [Date]

─── WHAT USERS LOVE (Don't Break These) ───
✅ "[Exact quote or paraphrase from review]"
✅ "[Second praise point]"
✅ "[Third praise point]"

─── MISSING FEATURES (Unmet Needs = Your Opportunity) ───
🟠 "[User request]" — mentioned by [frequency if pattern]
   → Design opportunity: [How you could address this]
🟠 "[User request]"
   → Design opportunity: [How you could address this]
🟠 "[User request]"
   → Design opportunity: [How you could address this]

─── UX CONFUSION POINTS ───
🟡 "[What confused users]"
   → Root cause: [Why this probably happens]
   → Fix: [How your design avoids this]
🟡 "[What confused users]"

─── BUGS & TECHNICAL FAILURES ───
🔴 "[Reported bug or crash]"
   → Lesson: [What this tells you about system reliability expectations]

─── TRUST & PRIVACY CONCERNS ───
🟣 "[Concern raised]"
   → Lesson: [What transparency or reassurance your design should include]

─── PERFORMANCE ISSUES ───
🟢 "[Performance complaint]"
   → Lesson: [Speed, size, or battery consideration for your design]

─── ONBOARDING PROBLEMS ───
🔵 "[Onboarding complaint]"
   → Fix: [How you'll make your onboarding smoother]

━━━ SUMMARY ━━━
Top 3 unmet needs from [App Name]'s users:
1. [Need 1] — frequency: [High/Medium/Low]
2. [Need 2] — frequency: [High/Medium/Low]
3. [Need 3] — frequency: [High/Medium/Low]

If you built ONLY these 3 things better, users would switch from [App Name].
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

Repeat this report for each competitor.

### Step 5: Cross-Competitor Pattern Analysis

After building reports for all competitors, look for patterns that repeat across multiple apps. These are **market-wide problems** — solving them gives you a category advantage, not just a competitive one.

```
CROSS-COMPETITOR PATTERNS

Unmet needs that appear in 2+ competitor reviews:
1. "[Need]" — appears in: [App A], [App B], [App C]
   → This is a MARKET GAP. Every user in this space wants this.
   → Priority for our design: HIGH

2. "[Need]" — appears in: [App A], [App B]
   → Priority for our design: MEDIUM

UX confusions that repeat across apps:
1. "[Confusion]" — this is likely a category convention problem
   → Our design must solve this differently

What users love consistently (table stakes — must have):
1. "[Feature/experience users praise everywhere]"
2. "[Second table stake]"
```

### Step 6: Feature Request Backlog (for Design Phase)

Extract every feature request mentioned and organize as potential design decisions:

```
FEATURE REQUEST BACKLOG (from real user reviews)

Priority A — Mentioned frequently, aligns with our problem statement:
□ [Feature request] — source: [App reviews where mentioned]
□ [Feature request]

Priority B — Mentioned occasionally, nice to have:
□ [Feature request]
□ [Feature request]

Priority C — Niche requests, edge cases:
□ [Feature request]

Will NOT build (mentioned but conflicts with our focus):
✗ [Feature request] — reason: [Why it's out of scope]
```

This backlog feeds directly into Phase 4 (IA & Ideation) — it tells you what screens and features to prioritize.

---

**Sources to check beyond direct search:**
- Product Hunt comments (especially for newer apps — raw community feedback)
- Reddit: r/[product category], r/UX, r/apps, r/[AppName]
- G2, Capterra, Trustpilot for B2B/desktop tools (more detailed than app stores)
- Twitter/X: search "[App Name] is broken" or "[App Name] wish it had"

## Identifying Design Opportunities

After research, look for these signal types:

1. **Frequency pain**: Something that bothers users constantly (even if minor)
2. **Severity pain**: Something that occasionally causes major failure
3. **Workaround behavior**: Users doing awkward things because no better option exists
4. **Mental model mismatch**: What users expect vs. how the system actually works
5. **Trust gaps**: Moments where users hesitate or second-guess the system

## Affinity Mapping (If You Have Multiple Insights)

Group research findings into themes:

```
Theme 1: [Name]
  - Insight from user A
  - Insight from user B
  - Supporting data point

Theme 2: [Name]
  - Insight from user C
  ...
```

The themes that emerge become the foundation for your personas and HMW statements.

## Phase 2 Output

Present to user before moving on:

```
## Phase 2 Complete — Research Insights

**Research method used:** [Interviews / Provided data / Synthesized / Mixed]

**Key Insights:**
1. [Most important insight — ground in specific behavior]
2. [Second insight]
3. [Third insight]
4. [Fourth insight (if exists)]
5. [Fifth insight (if exists)]

**Competitive Landscape:**
- [Competitor 1]: Strong on [X], weak on [Y]
- [Competitor 2]: Strong on [X], weak on [Y]
- [Competitor 3]: Strong on [X], weak on [Y]

**Design Opportunities:**
1. [Specific opportunity based on a gap or pain point]
2. [Second opportunity]
3. [Third opportunity]

**Biggest Surprise:** [Something unexpected from research — or "No major surprises; findings matched expectations"]

✅ Ready to move to Phase 3 — Define
```

---

## Competitor Classification

Identify each competitor at the right level:
- **Direct**: same problem, same users, same approach — appear in your users' shortlists
- **Indirect**: same problem, different approach (e.g., spreadsheet vs. dedicated app)
- **Adjacent**: different problem today but could expand into yours — large platforms or fast-growing startups
- **Substitute**: entirely different solution — hiring a person, manual process, or generic tools like email/Excel

## Positioning Gap Analysis

After mapping all competitors, ask: "Which value positions are unclaimed that matter to our target users?"

Look for:
- **Unclaimed**: no competitor owns this — opportunity to define the category
- **Crowded**: every competitor says the same thing — this position has lost meaning
- **Emerging**: no one has claimed this yet because the market shift is new (AI, compliance, remote work)

## App Store Review Mining (Mobile Projects)

For each competitor: search Google Play + App Store reviews. Classify findings:
- Bug · Missing Feature · UX Confusion · Performance · Onboarding · Trust · Praise

Build Cross-Competitor Pattern Analysis → Feature Request Backlog.

---

## Competitor Narrative Analysis Framework

Beyond features and pricing, understand the *story* each competitor tells. This reveals their positioning strategy, emotional appeals, and where they are vulnerable.

### The 4-Part Narrative Breakdown

For each competitor, extract their story arc:

```
1. VILLAIN (the enemy they position against)
   What problem, status quo, or enemy do they fight?
   Examples:
   - "Legacy tools that slow you down" → positions against enterprise software
   - "Complexity that kills creativity" → positions against professional/expert tools
   - "The spreadsheet chaos" → positions against Excel/manual workflows
   
   Why this matters: Their villain reveals what frustration they're banking on.
   If their villain resonates with YOUR users, that's their strongest asset.
   If their villain is irrelevant to your users, that's their weakness.

2. HERO (who wins in their story)
   Is the customer the hero? Or is the product the hero?
   - Customer-as-hero: "You become unstoppable with [product]"
   - Product-as-hero: "[Product] does the hard work for you"
   
   Customer-as-hero positioning builds stronger loyalty.
   Product-as-hero positions closer to a utility.

3. TRANSFORMATION (the before/after promise)
   What does life look like before vs. after using their product?
   
   Template: "[Before state] → [After state]"
   Example: "Scattered data in 5 tools → One source of truth"
   
   The more vivid and specific the transformation, the stronger the positioning.
   Vague transformations ("be more productive") are weak and easy to copy.

4. STAKES (urgency — what happens if you don't act)
   Do they create urgency? How?
   - Loss framing: "Every day you wait, competitors are pulling ahead"
   - FOMO: "Join 50,000 teams who've already made the switch"
   - Risk: "Your current approach isn't compliant with [regulation]"
   - Opportunity: "This is the year [market shift] — be ready"
```

### Narrative Analysis Template

For each competitor:

```
Competitor: [Name]

VILLAIN: [What they position against — quote if possible]
HERO: [Customer-as-hero / Product-as-hero? Evidence?]
TRANSFORMATION: [Before state] → [After state]
STAKES: [Urgency mechanism, if any]

NARRATIVE STRENGTH:
□ Villain is specific and relatable (not generic "inefficiency")
□ Hero is the customer (not the product)
□ Transformation is vivid and measurable
□ Stakes create genuine urgency (not manufactured fear)

NARRATIVE WEAKNESS: [Where does their story break down or feel inauthentic?]

POSITIONING GAP: [What angle of this story is unclaimed that we could own?]
```

### Positioning Map (2×2 Visualization)

After analyzing all competitors, plot them on a 2×2 map using the two axes most relevant to your market:

**Common axis pairs:**
- Price vs. Capability (low cost/basic ↔ premium/full-featured)
- Ease of Use vs. Power (simple/limited ↔ complex/flexible)
- SMB Focus vs. Enterprise Focus (self-serve ↔ sales-led/team)
- Point Solution vs. Platform (one thing well ↔ many things)
- Emerging/Innovative vs. Established/Proven

**Map template:**
```
          HIGH [Axis 2]
               │
    Comp B  •  │  • Us (target)
               │
               │        • Comp A
───────────────┼───────────────── [Axis 1]
               │
     Comp C •  │
               │
          LOW [Axis 2]
```

Identify the underserved quadrant — the position no competitor currently occupies that your target users would value. That's your differentiation target.

### Messaging Vulnerability Analysis

For each competitor's core claim, assess these 5 dimensions:

| Dimension | Question | Score (1–5) |
|-----------|----------|-------------|
| **Clarity** | Can a first-time visitor understand what they do in 5 seconds? | |
| **Differentiation** | Is their positioning distinct or does it sound like everyone else? | |
| **Proof** | Do they back claims with specific evidence (numbers, cases)? | |
| **Consistency** | Is messaging consistent across homepage → product → pricing? | |
| **Resonance** | Does it address a real, felt pain point? | |

Low-scoring dimensions = vulnerabilities you can exploit in your own positioning.

# UX Writing & Microcopy Guidance

## Why UX Writing Is Design

UX writing is not copywriting or marketing — it's **interface design using words**. Every label, button, error message, and empty state is a design decision that affects usability, clarity, and user confidence.

Just as you don't use red buttons randomly, you don't use random words. Every word should:
- Help users understand what will happen
- Reduce friction and cognitive load
- Build trust by being honest and clear
- Make the interface feel human, not robotic

**UX writing is as critical as layout, color, and typography.** A beautifully designed button with unclear copy will confuse users. Conversely, thoughtful copy can make a simple interface feel premium.

---

## The 4 UX Writing Principles

### 1. **Clear**
Users understand it without thinking. No ambiguity, no jargon.

- ✓ "Save Settings"
- ✗ "Persist Configuration"

### 2. **Concise**
Remove every unnecessary word. Short copy is easier to read and translates better.

- ✓ "Create workspace"
- ✗ "Click here to create a new workspace for your team"

### 3. **Useful**
Copy helps the user take the right action. It explains benefits, requirements, or consequences.

- ✓ "You need at least 2 team members to create a workspace"
- ✗ "Error: invalid action"

### 4. **Conversational**
Sound like a human, not a manual or legal document.

- ✓ "Looks like you don't have any projects yet"
- ✗ "Zero instances of the Project entity have been instantiated"

---

## Button Labels

Button labels are instructions. They describe what happens next when clicked.

### Core Rules

1. **Use verb + noun format**
   - ✓ "Save Settings", "Delete Project", "Send Invite"
   - ✗ "OK", "Submit", "Confirm"

2. **Make it predictable**
   - The label describes exactly what happens next
   - No surprises

3. **Match the user's mental model**
   - Use words from the problem domain, not your technical stack

### Button Label Examples

#### Primary Actions
| Bad | Good | Why |
|-----|------|-----|
| "OK" | "Save Settings" | Specific action is clear |
| "Submit" | "Create Account" | User knows what they're creating |
| "Continue" | "Next: Add Team Members" | Tells user what comes next |
| "Yes" | "Delete Project" | Honest about the action |

#### Secondary Actions
| Bad | Good | Why |
|-----|------|-----|
| "Cancel" | "Back" or "Discard Changes" | Clear what happens to their work |
| "No" | "Keep Editing" | Descriptive and friendly |
| "Close" | "View Later" | Contextual alternative |

#### Destructive Actions
**Always name the action.** Never hide destructive actions behind vague labels.

| Bad | Good | Why |
|-----|------|-----|
| "Delete" | "Delete Project" | User knows exactly what they're deleting |
| "Confirm" | "Permanently Delete 3 Files" | Specific + shows consequence |
| "Remove" | "Remove User from Workspace" | Shows impact on that user |

---

## Form Labels & Placeholders

### Labels: Always Visible Above

Form labels must be **permanently visible** above or integrated into the field.

```
Email address
[________________]

Password
[________________]
```

**Why not inside the field?**
- Labels disappear when the user starts typing
- Placeholder text vanishes, making it hard to remember what to enter
- Less accessible for screen readers

### Placeholders: Examples, Not Labels

Placeholders are for **format hints**, not the label.

✓ **Good:**
```
Email
[e.g., sara@example.com]
```

✗ **Bad:**
```
[Enter your email address here...]
```

### Required vs. Optional Fields

**Be explicit** about which fields are required.

✓ **Option 1: Asterisk (most common)**
```
Name *
[________________]

Company (optional)
[________________]
```

✓ **Option 2: Word-based (more accessible)**
```
Name (required)
[________________]

Company
[________________]
```

✗ **Bad: No indication**
```
Name
[________________]

Company
[________________]
```

---

## Error Messages

Error messages are **teaching moments**. They should help the user recover.

### The 3-Part Formula

1. **What happened** — State the problem clearly
2. **Why it happened** — Explain the reason (briefly)
3. **What to do** — Give the user a clear path to fix it

### Error Message Examples

#### Network Error
| Bad | Good |
|-----|------|
| "An error occurred" | "Couldn't save your project. Check your internet connection and try again." |
| "Connection failed" | "We lost connection. Your work is saved locally. We'll sync when you're back online." |

#### Form Validation
| Bad | Good |
|-----|------|
| "Invalid email" | "Please enter a valid email address (e.g., you@company.com)" |
| "Password too weak" | "Password must be at least 8 characters and include a number and symbol" |

#### Authentication
| Bad | Good |
|-----|------|
| "Authentication failed" | "Email or password is incorrect. Try again or reset your password." |
| "Unauthorized" | "This workspace is private. Ask an admin to send you an invite." |

#### Permission Denied
| Bad | Good |
|-----|------|
| "Access denied" | "You don't have permission to edit this project. Contact the owner to request access." |
| "Forbidden" | "Guests can't change project settings. Ask an admin to upgrade your role." |

#### Empty State (Error)
| Bad | Good |
|-----|------|
| "No results found" | "We didn't find any projects matching 'archived 2024'. Try a different search term." |
| "Error loading" | "We had trouble loading your files. Refresh the page or contact support if it keeps happening." |

### Error Message Tone

- **Honest, not alarming** — Don't sugarcoat, but don't catastrophize
- **Helpful, not punitive** — "You forgot to..." not "You failed to..."
- **Human, not robotic** — "Can't connect to the server" not "HTTP 500 error"

---

## Empty States

Empty states happen in three situations. Each needs different messaging.

### Type 1: First-Use Empty
User is new to the feature.

**Message:** What this area is for + Why it's empty + How to get started

✓ **Good:**
```
No projects yet

Projects help you organize work by team or client.
Create your first project to get started.

[Create Project]
```

✗ **Bad:**
```
You have 0 projects

[Create] [Learn More] [Dismiss]
```

### Type 2: User-Cleared Empty
User cleared their own content (deleted items, archived, filtered).

**Message:** Acknowledge the action + Show quick path to undo/create

✓ **Good:**
```
No completed tasks

You've cleared all finished tasks this week.
They're still in your archive if you need them.

[View Archive] [New Task]
```

✗ **Bad:**
```
No results
```

### Type 3: Error Empty
Something went wrong (network, permission, loading failed).

**Message:** What happened + Troubleshooting suggestion

✓ **Good:**
```
Couldn't load your workspaces

We're having trouble connecting. Check your internet and try again.

[Refresh] [Contact Support]
```

✗ **Bad:**
```
No data available

Error Code: 52001
```

---

## Success Messages

Success messages confirm the action and guide the user forward.

### Core Rules

1. **Confirm the specific action**, not just "Success!"
2. **Tell the user what happens next** (if it's not obvious)
3. **Duration:**
   - Toast notifications: 3-4 seconds (auto-dismiss)
   - Persistent messages: show until user dismisses or navigates

### Success Message Examples

| Bad | Good | Why |
|-----|------|-----|
| "Success!" | "Project saved" | Specific action confirmed |
| "Saved" | "Invited sarah@company.com to the workspace. They'll receive an email." | Tells user what happens next |
| "OK" | "Settings updated. Changes apply to all team members." | Context for the impact |
| "Done" | "File uploaded. It's processing — you'll get a notification when it's ready." | Sets expectation for what's next |

### Toast vs. Persistent

**Toast (auto-dismiss after 3-4 seconds):**
- Simple confirmations: "Project archived"
- Actions the user just triggered
- Low consequence if missed

**Persistent (user dismisses or navigates):**
- Important state changes: "Your trial ends in 3 days"
- Warnings: "Payment method invalid — update to keep your subscription"
- Required actions: "2 team members are waiting for your approval"

---

## Onboarding Copy

Onboarding is your chance to set expectations and reduce anxiety.

### Welcome Screen

Focus on **user benefit**, not product features.

| Bad | Good |
|-----|------|
| "Welcome to ProjectHub. Our platform offers collaboration, project tracking, and team communication." | "Let's get your first project up and running in 2 minutes." |
| "ProjectHub is a tool for managing work" | "Keep your team aligned — in one place" |

### Progress Indicators

Show progress and next step to keep motivation high.

✓ **Good:**
```
Step 2 of 4 — Tell us about your team

How many people will be using this workspace?
```

✗ **Bad:**
```
2/4 completed
[Next]
```

### Permission Prompts

Explain **why before asking**.

✓ **Good:**
```
ProjectHub needs camera access

We'll use your camera to record quick video updates in tasks.
You can change this later in Settings.

[Allow Camera] [Not Now]
```

✗ **Bad:**
```
ProjectHub would like to access your camera.

[Allow] [Deny]
```

### Skip Option

Always provide a skip button in onboarding. Some users prefer to explore on their own.

✓ **Good:**
```
[Guided Tour] [Skip]
```

✗ **Bad:**
```
[Start Tutorial]
(No way to skip — frustrating)
```

---

## Navigation Labels

Navigation labels should be **nouns**, not verbs. Use the user's language.

### Core Rules

1. **Use nouns** (Dashboard, Projects, Settings, Help)
2. **Use user language**, not internal product terms
3. **Max 2 words per label**

### Navigation Examples

| Bad | Good | Why |
|-----|------|-----|
| "Go to Dashboard" | "Dashboard" | Cleaner, consistent style |
| "Manage Workflows" | "Workflows" | Simpler and more scannable |
| "User Settings & Preferences" | "Settings" | One word, clear |
| "Report Issues" | "Help" | User-facing term |
| "Org Configuration" | "Admin" or "Settings" | User understands "Admin" |

---

## Microcopy for Key Moments

### Loading States

Show what's loading, not just "Loading..."

| Bad | Good |
|-----|------|
| "Please wait..." | "Fetching your projects..." |
| "Loading" | "Preparing your workspace..." |
| (spinner with no text) | "Uploading 3 files — 45% done" |

### Confirmation Dialogs

State what will happen. Don't ask "Are you sure?" — be specific.

| Bad | Good |
|-----|------|
| "Are you sure?" | "This will delete 'Q1 Projects' and all 12 tasks inside. You can't undo this." |
| "Confirm action" | "Inviting sarah@company.com will give her editor access to the workspace. She'll get an email." |

### Tooltips

Add information not visible on screen. Don't repeat the label.

| Bad | Good |
|-----|------|
| Tooltip: "Save" (when the button says "Save") | Tooltip: "Changes save automatically, or press Cmd+S" |
| Tooltip: "Edit your profile" | Tooltip: "Public profile — shared with workspace members" |

### Helper Text

Explain **format requirements before the error** happens.

✓ **Good:**
```
Password
At least 8 characters, 1 number, 1 symbol

[________________]
```

✗ **Bad:**
```
Password
[________________]

Error: Password too weak. Must have 8+ characters, 1 number, 1 symbol.
```

---

## Bilingual UX Writing: Arabic + English

Arabic UX writing must feel native, not translated. It also tends to be warmer and slightly more formal than English.

### Core Principles

1. **Arabic copy must be natural** — not word-for-word translations
2. **Tone is warmer than English** — more formal, slightly more respectful
3. **Button verbs use proper imperative forms** — Arabic has formal/informal distinctions
4. **Error messages maintain helpfulness** — not cold or bureaucratic
5. **Test with Arabic speakers** — cultural context matters

### Common Arabic UI Terms Glossary

| English | Arabic (Standard Form) | Notes |
|---------|----------------------|-------|
| Save | احفظ | Imperative: "Save/Preserve" |
| Cancel | إلغاء | "Annul/Cancel" — formal |
| Delete | حذف | Standard deletion action |
| Submit | إرسال | "Send" — more natural than direct translation |
| Search | بحث | Both noun and verb form |
| Settings | الإعدادات | Always plural in Arabic |
| Back | رجوع | Or العودة (return) |
| Next | التالي | Or "الخطوة التالية" (next step) for clarity |
| Edit | تعديل | Standard edit action |
| Add | إضافة | Standard add/create action |

### Button Label Examples: Arabic + English

#### Primary Actions
| English | Arabic | Context |
|---------|--------|---------|
| Save Settings | احفظ الإعدادات | Standard save action |
| Create Project | إنشاء مشروع | Creating new item |
| Send Invite | إرسال دعوة | Sharing/inviting |

#### Destructive Actions
| English | Arabic | Context |
|---------|--------|---------|
| Delete Project | حذف المشروع | Specific, no ambiguity |
| Remove User | إزالة المستخدم | Removing from workspace |
| Clear All | حذف الكل | Multiple items |

### Error Messages: Arabic Examples

#### Network Error
| English | Arabic | Notes |
|---------|--------|-------|
| "Check your connection and try again" | "تحقق من اتصالك بالإنترنت وحاول مجددًا" | Conversational, helpful |

#### Form Validation
| English | Arabic | Notes |
|---------|--------|-------|
| "Please enter a valid email" | "الرجاء إدخال عنوان بريد صحيح" | Use "الرجاء" (please) for courtesy |

#### Permission Denied
| English | Arabic | Notes |
|---------|--------|-------|
| "Ask an admin to give you access" | "اطلب من المسؤول منحك صلاحية الوصول" | Warm, actionable |

### Empty States: Arabic Examples

#### First-Use Empty
| English | Arabic | Notes |
|---------|--------|-------|
| "No projects yet. Create your first project to get started." | "لا توجد مشاريع حتى الآن. أنشئ مشروعك الأول للبدء." | Encouraging tone |

#### User-Cleared Empty
| English | Arabic | Notes |
|---------|--------|-------|
| "You've archived all tasks this week." | "لقد أرشفت جميع المهام هذا الأسبوع." | Acknowledges user action |

### Success Messages: Arabic Examples

| English | Arabic | Notes |
|---------|--------|-------|
| "Project saved" | "تم حفظ المشروع" | Simple confirmation |
| "Invitation sent to sarah@company.com" | "تم إرسال الدعوة إلى sarah@company.com" | Specific action confirmed |

### Onboarding: Arabic Example

✓ **Good:**
```
مرحبًا بك في ProjectHub

دعنا نحضر مشروعك الأول في دقيقتين فقط

[ابدأ الآن] [تخطي]
```

✗ **Bad:**
```
أهلا وسهلا في ProjectHub
نحن هنا لمساعدتك على إدارة المشاريع والعمل الجماعي
[التالي]
```
(Too formal, feature-focused, no skip option)

---

## UX Writing Checklist

Use this checklist before submitting a screen for engineering handoff:

- [ ] **All buttons use action verbs** — No "OK", "Submit", or "Yes"
- [ ] **Error messages have all 3 parts** — What happened, Why, What to do
- [ ] **Empty states have purpose + action** — Not just "No data"
- [ ] **No jargon or internal product terms** — Use user language
- [ ] **Copy works without context** — Read it standalone; is it clear?
- [ ] **If bilingual (Arabic), text feels native** — Not translated word-for-word
- [ ] **No lorem ipsum anywhere** — Check placeholders, helper text, examples
- [ ] **Loading states show what's loading** — Not just a spinner
- [ ] **Confirmation dialogs are specific** — Not "Are you sure?"
- [ ] **Tooltips add value** — Not just repeating the label
- [ ] **Tone is consistent** — Not switching between casual and formal
- [ ] **All copy fits the space** — No truncation or awkward line breaks

---

## Before/After Rewrites

Common bad UI copy patterns and their corrected versions:

| # | Bad | Good | Issue |
|---|-----|------|-------|
| 1 | "Confirm" | "Delete 5 Files Permanently" | Vague label hides destructive action |
| 2 | "An error occurred" | "Couldn't save your changes. Check your internet connection and try again." | No context or path to fix |
| 3 | "No results" | "No projects match 'archived 2024'. Try a different search term or create a new project." | Doesn't help user recover |
| 4 | "Please wait..." | "Uploading 12 files — this may take a minute" | Shows progress and expectation |
| 5 | "Submit" | "Create Account" | Specific action is clear |
| 6 | "Loading" | "Fetching your workspace..." | Specific about what's loading |
| 7 | [placeholder text] "Enter email" | [label] "Email" with [placeholder] "e.g., sara@company.com" | Placeholder isn't a label |
| 8 | "Are you sure?" | "This will archive 'Project Q1' and move it out of view. You can unarchive it later." | Specific about consequence and recoverability |
| 9 | "Updated" | "Settings saved. Changes apply to all 3 team members." | Specific action + impact |
| 10 | "Error: Invalid input" | "Please enter a password with at least 8 characters, 1 number, and 1 symbol." | Clear requirement before error |

---

## Quick Reference: Copy By Feature Type

### Buttons
- Action verb + noun ("Delete Project", not "Confirm")
- Destructive actions are always named
- Secondary actions use context ("Keep Editing", not "No")

### Forms
- Labels always visible, above fields
- Placeholders are format hints only ("e.g., ...", not labels)
- Specify required vs. optional clearly

### Errors
- 3 parts: What + Why + How to fix
- Tone: helpful, not punitive
- Suggest next step

### Empty States
- Match the situation (first-use, cleared, error)
- Include why and what to do
- Make the CTA clear

### Success
- Specific action confirmed
- Tell user what happens next
- Match duration to consequence (toast vs. persistent)

### Onboarding
- Focus on benefit, not features
- Show progress and next step
- Always allow skipping
- Explain permission requests before asking

### Navigation
- Use nouns, max 2 words
- Use user language, not product jargon
- Consistent capitalization

### Loading
- Show what's loading ("Fetching projects...")
- Show progress if it takes more than 2 seconds
- Give time expectation if it might take a while

---

## Implementation Tips

1. **Write in plain English first.** Good English UX writing often works better in other languages too.

2. **Test microcopy with users.** Even small words change how people interpret actions. Watch someone use your interface and listen to their language.

3. **Avoid marketing language in UI.** "Unlock powerful collaboration" belongs in marketing. UI says "Create Project".

4. **For Arabic, partner with native speakers.** A developer fluent in English might not catch nuance in Arabic.

5. **Keep a product dictionary.** Document how you say things (workspace vs. team vs. org) and stay consistent.

6. **Abbreviate last, if ever.** If you're abbreviating UI labels, your information architecture might be confusing instead.

7. **Proof empty states thoroughly.** They're often written last and tested least, but users see them first.

---

## Related References

- [Design System Documentation](./design-system.md)
- [Accessibility Guidelines](./accessibility.md)
- [Button & Form Patterns](./component-patterns.md)

---

## Tone by Emotional State

Adapt microcopy tone to the user's current state — same brand voice, different emotional inflection:

| State | Tone | What to Focus On |
|---|---|---|
| Success | Celebratory, warm | Reinforce the win — "You did it!" not "Action completed" |
| Error | Empathetic, blame-free | Blame the system, not the user — "Something went wrong" not "You entered an invalid value" |
| Warning | Clear, calm | State the risk without panic — give the user control |
| Neutral / Informative | Direct, concise | State the fact, skip the editorial commentary |

---

## Legal Copy Flags

Before finalizing any copy, check for these risks:
- **Unsubstantiated superlatives**: "best", "fastest", "only", "#1" — require evidence or remove
- **Missing disclaimers**: financial or health claims, guarantees ("always", "never fails")
- **Comparative claims**: competitor comparisons must be fact-based and defensible

Mark any flagged copy with `⚠️ Legal Review` annotation — do not block the design, but log it clearly.

---

## Inclusive Language Rules

- Use **gender-neutral language** — "they/them" for unknown individuals, not "he/she"
- Avoid **ableist terms**: "crazy", "blind spot", "lame", "sanity check", "dumb" — use plain alternatives
- Use **person-first language** where appropriate: "person with a disability" not "disabled person"
- Avoid **culturally specific idioms** that may not translate across regions
- Replace "easy" and "simple" with specific claims: "in 3 steps", "takes under 2 minutes"

---

## Localization Notes

When the product targets users across regions or languages:
- **Idioms to avoid**: metaphors often fail in translation — use literal, plain language equivalents
- **Character expansion**: German, Arabic, and Finnish text can be 20–30% longer than English — design for expansion in buttons, labels, and nav items
- **Cultural context**: colors, gestures, and symbols carry different meanings across cultures — document region-specific risks in the handoff
- **Number and date formats**: use ISO 8601 (2026-04-07) in data exports and APIs — regional date formats are ambiguous
- **RTL impact**: Arabic and Hebrew layouts mirror the entire UI — test all icons, animations, and flow direction before delivery

---

## Brand Voice Framework (Marketing × UX Integration)

Product copy and marketing copy must share the same voice. This section bridges UX writing with brand voice principles so the product feels like a natural extension of the brand — not a different entity.

### Brand Voice Spectrum — 7 Dimensions

Position the brand's voice on each spectrum. Document the result in the project brief.

| Dimension | Spectrum | Our Position |
|-----------|----------|--------------|
| **Formality** | Formal ←————→ Casual | [Define per project] |
| **Authority** | Expert/Authoritative ←→ Peer-level/Collaborative | [Define per project] |
| **Emotion** | Warm/Empathetic ←————→ Direct/Matter-of-fact | [Define per project] |
| **Complexity** | Technical/Precise ←———→ Simple/Accessible | [Define per project] |
| **Energy** | Bold/Energetic ←————→ Calm/Measured | [Define per project] |
| **Humor** | Playful/Witty ←—————→ Serious/Earnest | [Define per project] |
| **Innovation** | Cutting-edge/Forward ←→ Established/Proven | [Define per project] |

For each dimension chosen, document it using the attribute format:

```
[Attribute name]
- We ARE:     [what this means in product copy]
- We are NOT: [common misinterpretation to avoid]
- Sounds like: "Here's how to get started in five minutes."
- NOT like:    "Initiating onboarding sequence. Please comply."
```

### Tone Adaptation by Channel and Context

The voice stays fixed; tone adapts to context. Tone is the emotional dial on the voice.

| Context | Tone | Example |
|---------|------|---------|
| **Success / Completion** | Celebratory, but not over the top | "Done! Your changes are saved." not "AMAZING!! You DID IT!!" |
| **Error / Failure** | Empathetic + helpful, never blaming | "Something went wrong. Try again, or contact support." |
| **Warning / Caution** | Clear + actionable, not alarming | "This will delete all items. This can't be undone." |
| **Loading / Waiting** | Reassuring, sets expectations | "Loading your data… usually takes a few seconds." |
| **Empty states** | Inviting, not apologetic | "Nothing here yet. Add your first item to get started." |
| **Onboarding** | Welcoming, encouraging, clear | "Let's get you set up. It only takes 2 minutes." |
| **Destructive action** | Direct, honest, consequence-clear | "Delete account? All your data will be permanently removed." |
| **Disabled state** | Neutral, explains why when possible | "Save disabled — add at least one item first." |

### Terminology Management

Consistent terminology prevents confusion. Establish these for every project:

```
PREFERRED TERMS → AVOID THESE
sign up (verb)  → signup (verb) — "signup" is the noun form
log in (verb)   → login (verb)  — "login" is the noun form
set up (verb)   → setup (verb)  — "setup" is the noun form
email           → e-mail        — no hyphen
remove          → delete        — use "delete" only for permanent destruction
```

**Project-specific terminology table** (fill in per project):

| Use This | Not This | Why |
|----------|----------|-----|
| [Project term 1] | [Alternative] | [Reason — clarity, brand, user mental model] |
| [Project term 2] | [Alternative] | [Reason] |

**Product and feature name rules:**
- Use the exact capitalization defined in Phase 4 (Brand Identity)
- First mention in any screen: use the full name
- Subsequent mentions: approved shorthand only
- Never use competitor's terminology for your product category (avoid reinforcing their positioning)

### Legal Copy Flags in UX

Flag these for legal review before shipping:

| Pattern | Risk | Required Action |
|---------|------|----------------|
| "Best" / "Fastest" / "Only" | Unsubstantiated superlative | Add qualifier: "one of the fastest" or remove |
| Guarantees ("We guarantee...") | Legal liability | Replace with SLA language or remove |
| Competitor comparisons ("Better than X") | Defamation / false advertising risk | Legal review required |
| Financial/health claims | Regulatory requirements | Disclaimer + legal sign-off |
| User testimonials | FTC/ASA disclosure requirements | Attribute + disclosure |
| "Free" without qualification | Misleading if conditions apply | Add: "Free for [X] — [conditions]" |

### Inclusive Language in UX Copy

- Use gender-neutral language for unknown individuals: they/their (not he/she)
- Replace ability-based idioms: "straightforward" not "easy" (ease varies by person)
- Avoid: "crazy," "blind spot," "lame," "dummy" — use plain alternatives
- Person-first language: "people with disabilities" not "disabled people" (unless community preference differs)
- Age-neutral: "older adults" not "elderly"; "young professionals" not "millennials"
- Use "and so on" / "etc." not culturally-specific idioms that may not translate

# Example: Nabd — a clinic workspace

> **A demo project.** Nabd, the clinic and the people in it are fictional. The competitor research is real and sourced; research findings are labeled as assumptions.

**The prompt:**

```text
/designxi Design a SaaS dashboard for small clinics to manage appointments and patients.
```

DesignXI ran all 27 phases on it and delivered six files. They share one top bar, so you can move between them in one click. Each opens offline in any browser.

| File | What it is | Example |
| --- | --- | --- |
| `index.html` | Project overview that links every file | [Open example](https://htmlpreview.github.io/?https://github.com/ahmeduxui/DesignXI/blob/main/examples/nabd-clinic-dashboard/index.html) |
| `process.html` | All 27 phases, from the five whys to the launch plan | [Open example](https://htmlpreview.github.io/?https://github.com/ahmeduxui/DesignXI/blob/main/examples/nabd-clinic-dashboard/process.html) |
| `screens.html` | Interactive prototype with a guide to four flows | [Open example](https://htmlpreview.github.io/?https://github.com/ahmeduxui/DesignXI/blob/main/examples/nabd-clinic-dashboard/screens.html) |
| `casestudy.html` | Portfolio-ready case study | [Open example](https://htmlpreview.github.io/?https://github.com/ahmeduxui/DesignXI/blob/main/examples/nabd-clinic-dashboard/casestudy.html) |
| `handoff.html` | Tokens, component specs, motion, breakpoints, edge cases | [Open example](https://htmlpreview.github.io/?https://github.com/ahmeduxui/DesignXI/blob/main/examples/nabd-clinic-dashboard/handoff.html) |
| `image-prompts.md` | The Gemini prompts behind the persona portraits | [Open example](image-prompts.md) |

← [Back to DesignXI](../../README.md)

---

## Stage 1 · Understand

The skill starts with the problem, not the screen. Five whys find the root cause: the day is split across tools, so risk and free time stay invisible.

![Phase 1 — five whys, goals and SWOT](screenshots/phase-01-discovery.png)

A live web search builds the competitor matrix and finds the gap: calendar tools show bookings, queue tools show walk-ins, and none shows a small clinic's whole day.

![Phase 2 — competitor matrix](screenshots/phase-02-competitors.png)

Research turns into personas, with portraits generated from prompts built on the project's palette, then into a journey map, How Might We questions and KPIs.

![Phase 3 — personas](screenshots/phase-03-persona.png)

![Phase 3 — journey, HMW and KPIs](screenshots/phase-03-journey.png)

## Stage 2 · Requirements

Requirements are written and approved before any wireframe. Each one has acceptance criteria that the tests in phase 22 check later.

![Phase 6 — functional requirements](screenshots/phase-06-requirements.png)

## Stage 3 · Structure

Structure comes before skin: the platform map, three task flows, then lo-fi and mid-fi wireframes with every state.

![Phase 7 — information architecture and flows](screenshots/phase-07-structure.png)

![Phases 8–9 — wireframes](screenshots/phase-08-wireframes.png)

## Stage 4 · Visual direction

A saved design system (Untitled UI) with a teal brand, contrast checked from hex, and a product voice for every key moment.

![Phases 12–13 — identity and voice](screenshots/phase-12-identity.png)

## Stage 5 · UI

The skill reviews its own work. Here it caught two critical problems in its first draft and fixed them: a timeline too cramped to read, and a button color that failed contrast.

![Phase 17 — self-critique](screenshots/phase-17-self-critique.png)

## Stage 6 · Validation

The prototype works end to end, with a guide that walks through four flows.

![Phase 18 — prototype](screenshots/phase-18-prototype.png)

## Stage 7 · Post-design docs

Every requirement maps to a screen and a test. Nothing is left without proof.

![Phases 21–22 — traceability and UAT](screenshots/phase-21-traceability.png)

## Stage 8 · Delivery

The developer gets tokens, component specs, the timeline maths, motion, breakpoints, content rules, edge cases and the reasons behind each decision.

![Phase 25 — developer handoff](screenshots/phase-25-handoff.png)

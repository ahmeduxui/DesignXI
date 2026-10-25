# Figma tokens — pull real design tokens, but notify first

When a project is built on a system whose real tokens live in Figma — a 🔶 saved system, or any Figma file/link the user gives — pull the actual variables instead of guessing hex and
fonts. Uses the Figma MCP (`get_variable_defs`, `get_design_context`, `get_metadata`, `get_screenshot`).

## The rule: ask before you pull — always

**Never read a Figma file without telling the user first and getting a clear yes.** Even when the catalog
says a system's tokens are *من فيجما*, that is permission to *propose* the pull, not to do it silently. He
asked to be notified before anything is pulled from Figma, every time.

The confirmation step (via AskUserQuestion, or a one-line ask if a question tool isn't warranted):

1. **Name exactly what you're about to read** — which file (name + key if known), and which of: color
   variables, type styles, spacing/grid, components, a specific frame screenshot. One line each.
2. **Say why** — "to apply the brand's real tokens instead of guessing." Tie it to the phase.
3. **Wait for yes.** On yes → pull only what you named, nothing more. On no → ask him to paste the tokens,
   or proceed with a clearly-labelled placeholder/baseline (e.g. Untitled UI as a starting baseline) and
   mark every value as unconfirmed.

Don't batch-read a whole file "to be safe," don't follow links to other files the pull reveals, and don't
re-pull later in the session without asking again — each new file or new scope is a new ask.

## What to pull, by phase

- **Phase 11 (Design-System Selector)** — if he picks a 🔶 system or names a Figma file, confirm, then pull
  just enough to confirm the system is usable (palette + type). 
- **Phase 12 (Identity & Icons)** — confirm, then pull the full token set for the chosen system: color
  variables (`get_variable_defs`), type styles, spacing/grid, icon definitions. Write them into the
  project's tokens; update the system's entry in `references/saved-design-systems.md` from 🔶 toward ✅ if
  the pull completes it (tell the user you're doing that too).
- **Any phase** — a one-off reference screenshot of a specific frame (`get_screenshot`) is still a read:
  name it and confirm first.

## After pulling
- Show what came back (the token list / the frame) before applying it, so he can correct a wrong file.
- Never guess a value the pull didn't return — ask, or label it unconfirmed.
- Real tokens only; this never invents a variable Figma didn't provide.

> This is a notify-first gate on top of the existing Figma references in Phases 11–12 — it does not widen
> what gets read, it just makes every read announced and approved first.

# Stress-Test — worst-case data for every screen

Demo data is chosen, usually without noticing, to make a design look good: names that fit one line,
counts that never need a separator, every optional field filled. This file undoes that choice. Every
screen in Phase 15 is designed against the **realistic worst case** for each value it renders, not just
the happy path — and the empty/loading/error states DesignXI already requires are only part of it.

Based on the break-ui adversarial method. Two things make it worth doing rather than hand-waving:
- **Plausible, never nonsense.** `"aaaaaaa"` and 5,000-char strings prove nothing — the design gets
  defended with "that never happens." Every worst-case value is something a real user produces, or the
  real limit the backend accepts.
- **Not just long text.** The breaks that ship are the short name with an orphaned dash, the missing
  avatar, the count of exactly 1 ("1 members"), the empty list, the translated badge that overflowed.

**Where it runs in the 27-phase flow:**
- **Phase 15 (hi-fi screens)** — design each screen's worst-case state, not only the demo state.
- **Phase 16 (responsive & RTL)** — the *environment* stress: 320px, 200% zoom, dark mode, RTL.
- **Phase 17 (self-critique)** — a worst-case pass is part of the gate; fix every 🔴 before Phase 18.

**Arabic-first note:** for RTL work the worst cases below marked (ع) matter most — Arabic names,
mixed Arabic/Latin, bidi punctuation, stacked diacritics, and Latin digits inside Arabic. Pair with
`references/rtl-arabic.md`.

---

## Method (per screen)

1. **List every rendered value** with its source and limit: names, emails, titles, the counts in
   headers, relative timestamps, badge/status text, button labels from data, tooltips, avatar images,
   and the list length itself. Where no limit exists, that's a finding — write "unbounded".
2. **Build one worst-case dataset** that hits many fields at once — spread different failures across the
   first few rows (row 1 long name, row 2 long email, row 3 one-letter name), as real data does. Plus
   the states that aren't one dataset: **empty** (0 items), **one** (every count at exactly 1), **huge**
   (1,000+ rows — a performance break too).
3. **Check it** at the real container width, then **320px** and the widest layout; at **200% zoom**; in
   **dark mode** and **RTL**.
4. **Report** each break as: what you see → cause → fix. Decide truncate/wrap/clamp per field.

---

## Failure signatures → fix (the common ones)

| What you see | Cause | Fix |
|---|---|---|
| Avatar/icon squished to an oval | flex child shrinking | `flex-shrink:0` on avatar/icon/fixed boxes |
| Text overflows instead of wrapping/truncating | flex/grid child `min-width:auto` | `min-width:0` on the text column (`minmax(0,1fr)` in grid) |
| Email/URL runs past the edge | no break points in the string | `overflow-wrap:anywhere` |
| Trailing action (••• / button) pushed off-screen | middle took all space | `min-width:0` on middle, `flex-shrink:0` on action |
| Badge wraps to two lines | badge allowed to shrink | `white-space:nowrap; flex-shrink:0`, decide what yields |
| Avatar adrift beside a 3-line name | `align-items:center` on varying-height rows | `align-items:flex-start` once text wraps |
| Wrong initials (`J` for Jo, `CI` for "…III", `�` for emoji) | `.split(' ')[0][0]` | `Intl.Segmenter`, first+last word, icon fallback |
| Orphaned `—` where a role was | placeholder for a missing optional field | omit the line, or reserve its height on purpose |
| "1 members" / "0 member" | hardcoded plural | `Intl.PluralRules` (Arabic has 6 plural forms — ع) |
| Numbers jitter / columns misalign | proportional figures | `font-variant-numeric:tabular-nums` |
| `1284`, `NaN`, `undefined`, `0.30000000004` | raw number rendered | `Intl.NumberFormat` + null guard; Latin digits in Arabic (ع) |
| Long translated label overflows button | fixed-width button | width from content + `min-width`, never fixed `width` |
| Diacritics clipped top/bottom | tight `line-height` + `overflow:hidden` | looser `line-height`, don't clip text boxes (ع) |
| Broken-image icon in avatar | no `onError` fallback | fall back to initials; `object-fit:cover` |
| Truncated text with no way to read it | `ellipsis` and nothing else | `title`/tooltip + full value in a detail view |
| 1,000 rows stutter | every row rendered | virtualize or paginate (say which) |
| Raw `<b>`, `&amp;`, `**text**` on screen | wrong escaping layer | escape once at render; never inject user HTML |

## Truncate / wrap / clamp — decide per field
- **Wrap** what the user needs in full to identify something (names, titles in detail).
- **Truncate at the end** for secondary metadata where the start carries meaning (role, preview) — always
  pair with a way to see the full value.
- **Truncate in the middle** when items differ at the end (file names, emails on a shared domain, paths).
- **Clamp** (`line-clamp`) multi-line card previews so card heights stay predictable.
- **Never truncate** numbers, amounts, dates, or anything compared — give them the room.

---

## Worst-Case Catalog (use the rows that apply)

Use `example.com` / `.test` for emails and URLs so no fixture points at a real inbox.

**Names / people**
- `Aleksandra Wiśniewska-Kowalczyk` — long, hyphenated, diacritics; wraps, hyphen is a break point
- `Christopher Alexander Montgomery III` — suffix; naive initials give `CI`
- `Jo` / `J` — two / one letters; empty-looking column, broken initials
- `نور الهدى عبد الرحمن` (ع) — RTL; punctuation/icons land wrong without `dir="auto"`
- `محمد` + Latin email on one row (ع) — mixed Arabic/Latin bidi; order flips
- `Đặng Thị Ngọc Hân` — stacked diacritics; clipped by tight line-height
- `王秀英` — CJK no spaces; breaks anywhere, one-word initials
- `🦊 Fox` / `👩🏽‍💻 Priya` — emoji first; `.charAt(0)` returns half a surrogate
- *(missing)* — only an email, no name; needs a fallback

**Emails / URLs / IDs** (unbreakable strings — no spaces to wrap)
- `bartholomew.fitzgerald@northwind-industries-holdings.example.com` — the classic; pushes siblings off
- `a@b.co` — shortest; layout that assumed long looks empty
- long URL with query string — end-truncation hides the part that differs
- `9f8e7d6c-5b4a-4c3d-8e2f-1a0b9c8d7e6f` — UUID; monospace width, middle-truncate
- `Q3 Board Deck — FINAL (revised) v12 [approved by legal].pdf` — end-truncation hides version+extension

**Labels / copy from data**
- `Senior Product Design Engineer, Platform Infrastructure` — long title wraps to 3 lines
- `Paramètres de confidentialité et de sécurité` — translated copy runs ~30% longer
- `إعدادات الإشعارات والخصوصية` (ع) — Arabic label expansion; check it doesn't overflow
- twelve tags on one item — wrap into a wall; needs a `+8` overflow
- `Untitled` / empty / `   ` — missing title; collapsed heading
- `<script>alert(1)</script>` / `&amp;` / `**bold**` — must render as literal text

**Numbers / money** — `0` (zero states), `1` (plurals), `1284` (separator → `1,284` / `١٬٢٨٤` ع),
`1000000` (badge width, compact `1M`), negatives, locale separators, a live-changing value (jitter).

**Collections** — 0 items (empty state), 1 item (grid looks broken, "1 of 1"), exactly page-size and
+1 (off-by-one), 1,000+ unpaginated (perf), one item 10× others (masonry stretch), identical names.

**Time** — now ("0 seconds ago" vs "just now"), 12 days / 11 months / 3 years ago (relative thresholds),
future date, `1970-01-01`, a timestamp that shows a different day in another timezone. Use
`Intl.RelativeTimeFormat` / `Intl.DateTimeFormat`, not hand-built strings.

**Images** — avatar URL that 404s (fallback), no avatar (fallback parity), 4000×200 panorama
(`object-fit`), dark logo on dark mode (invisible), slow image (layout shift without `aspect-ratio`).

**States** — loading (skeleton matches final layout?), API error (no raw `TypeError` on screen), partial
data (misaligned rows), every status at once (badge widths vary), no-permission (layout still holds),
the current user in the list ("You" labels).

**Environment** — 320px, narrow sidebar reuse, 2560px (lines too long), 200% zoom, dark mode, `dir="rtl"`
(ع), touch (hover-only ••• unreachable).

---

## Tone
Matter-of-fact. The screen isn't badly built; it was built against kind data, which is how nearly
everything gets built. Name the break, show the value that caused it, give the fix. A short report on a
sturdy screen is a good result.

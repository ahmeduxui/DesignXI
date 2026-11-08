# Imagery — Gemini, free stock, or the user's own photos

Every image inside a DesignXI deliverable — hero photos, in-screen content imagery, persona
portraits, case-study mockup backdrops — comes from one of three sources, chosen by the user:

1. **Gemini**, driven through Chrome, from a prompt built out of the project's own brand tokens.
2. **Free stock photos** from Pexels or Unsplash, picked to match the same subject and palette
   (see "Free stock photos" below).
3. **The user's own photos.**

Whatever the source: no hotlinked stock URLs, no gray placeholder boxes, no `via.placeholder.com`.
Every image is downloaded into `images/` under the manifest's file name.

Two things matter equally here:

1. **The images must look like they belong to this project.** A prompt that doesn't carry the
   Phase 6 design style and the Phase 7 color tokens produces generic AI slop that fights the design
   system. The prompt is a design artifact — treat it with the same care as a color token.
2. **The user must always be able to finish the job themselves.** Browser automation breaks: the
   extension isn't connected, Gemini rate-limits, the session dies mid-project. So the prompts are
   *always* handed over in copy-ready form — a file **and** in chat — whether or not the automation
   ran. If everything stops, the user opens Gemini, pastes, downloads, drops the files into `images/`,
   and the design is complete. Nothing is lost.

---

## Step 1 — Build the image inventory (before generating anything)

Walk the approved screens / personas / case-study sections and list every image the deliverable
needs. Write it as `images.json` in the project folder. This manifest is the single source of truth
— the prompts file, the placeholders, and the final embed all read from it.

```json
{
  "project": "Nafas — Meditation App",
  "style": "Organic Biophilic",
  "palette": { "primary": "#2F5D50", "accent": "#E8C07D", "bg": "#0E1512" },
  "images": [
    {
      "id": "hero-home",
      "file": "images/hero-home.jpg",
      "where": "screens.html → Home screen, full-bleed hero behind the greeting",
      "size": "1440x900",
      "type": "hero",
      "subject": "a woman breathing slowly at dawn on a balcony, eyes closed, warm side light"
    },
    {
      "id": "persona-lina",
      "file": "images/persona-lina.jpg",
      "where": "personas.html → Persona 1 card avatar",
      "size": "512x512",
      "type": "persona",
      "subject": "Lina, 29, Saudi product manager, warm but tired-and-determined expression"
    }
  ]
}
```

`type` selects the prompt recipe (below). `size` drives the aspect-ratio line. `where` is what makes
the handoff usable — the user needs to know which file goes where without re-reading the HTML.

Then generate the prompt sheet and the placeholders in one command:

```bash
python3 references/scripts/build_image_prompts.py --manifest images.json --outdir .
```

It writes `صور-البرومبتات.md` (one copy-ready section per image) and creates `images/` with on-brand
SVG placeholders, so the HTML renders correctly *before* any real image exists. Print the same table
in chat — file · where it goes · size — with each full prompt in its own code block underneath. Both
deliveries, every time, even when the automation succeeded.

---

## Step 2 — Ask before generating

Do not silently open a browser. Ask with AskUserQuestion:

Ask in the user's language (Arabic or English):

> "الصور جاهزة كبرومبتات. كيف تحب نكمل؟
> A) ولّدها أنت عبر جيمناي في كروم
> B) أعطني البرومبتات بس وأنا أولّدها
> C) عندي صور جاهزة بحطها بنفسي
> D) استخدم صور مجانية من Pexels أو Unsplash"

> "The image prompts are ready. How would you like to continue?
> A) Generate them for me with Gemini in Chrome
> B) Just give me the prompts and I'll generate them
> C) I have my own photos and will add them myself
> D) Use free stock photos from Pexels or Unsplash"

- **A** → run the Chrome flow (Step 3), image by image.
- **B** → you're already done: the prompt sheet and placeholders exist. Say exactly where to drop
  the finished files (`images/<file>`, same names) and carry on with the design. Nothing blocks —
  the deliverable is coherent and complete with placeholders in place.
- **C** → same as B, minus the prompts discussion. Keep the file names.
- **D** → follow "Free stock photos" below.

Ask this once per image batch, not once per image.

---

## The prompt recipe

Every prompt carries four fixed layers plus one variable layer:

```
Generate an image, <aspect ratio — 16:9 landscape / 1:1 square / 4:5 portrait>.
<SUBJECT — the variable layer, from the manifest>
Visual style: <Phase 6 design school, translated to photographic language>.
Color: dominant <primary hex> with <accent hex> accents, on <bg hex> tones.
Composition: <where text or UI will sit must stay calm and uncluttered>.
Premium editorial quality, high detail, no text, no watermarks, no UI elements.
```

That last line matters more than it looks: Gemini loves adding fake interface chrome and gibberish
lettering into anything that smells like an "app" image, which then collides with the real UI you
designed on top.

**Translating the design school into photographic language** (Phase 6 → image direction):

| Design school | Photographic direction |
|---|---|
| Minimalism / Swiss Modernism | Clean negative space, single subject, soft even light, muted palette |
| Flat Design | Bright flat lighting, simple shapes, high-key, low shadow contrast |
| Glassmorphism / Aurora UI | Soft gradient light, bokeh, translucent layers, atmospheric haze |
| Organic Biophilic | Natural light, plants/wood/stone texture, golden hour, gentle film grain |
| Brutalism / Neubrutalism | Hard flash lighting, raw concrete, high contrast, unpolished |
| Cyberpunk / Dark Mode First | Neon rim light, deep shadow, wet reflective surfaces, night |
| Editorial / Magazine | Fashion-editorial lighting, styled composition, shallow depth of field |
| Skeuomorphism | Real material macro detail — leather, brushed metal, tactile surfaces |

### Per-type recipes

**`hero`** — the composition line must reserve room for the headline and CTA. Say it explicitly:
"Keep the left third calm and uncluttered so a headline can sit there" (or the top ~35% for centered
heroes). Landscape 16:9 unless the manifest says otherwise.

**`persona`** — a real-feeling portrait, not a corporate headshot. Include age, role, region if
relevant, and above all the *expression* that matches the persona's frustration. Square 1:1, neutral
background near the surface color, natural light, eye contact with camera. Add: "documentary
portrait, not a stock-photo smile."

**`content`** — in-screen imagery (card thumbnails, empty-state art, feature sections). Keep the
subject literal and specific to the feature; a vague prompt here yields the generic gradient blob
that makes a design look AI-made. When several content images share a grid, write them as a set and
repeat the same lighting and palette lines across all of them, so the grid feels shot by one
photographer.

**`mockup`** — case-study backdrops: a device or environment the screens get composited onto. Ask
for an empty device screen ("blank white screen, no interface") or a clean desk/environment with
open space; the real UI goes on top.

**Persona-set consistency**: generate all personas in one Gemini session and repeat an identical
lighting/background/lens line. Otherwise the persona cards look like they came from four different
websites.

---

## Step 3 — Generating in Chrome (option A only)

Use the Claude-in-Chrome MCP tools (`mcp__claude-in-chrome__navigate`, `...computer`,
`...javascript_tool`, `...tabs_context_mcp`). Load them via ToolSearch if deferred. If the extension
isn't connected, don't improvise a workaround — fall back to option B and keep the design moving.

1. `tabs_context_mcp {createIfEmpty:true}`, then `navigate` to `https://gemini.google.com/app`.
2. Screenshot to confirm the composer is present and the user is signed in.
3. Click the input, `type` the prompt, press `Return`.
4. Wait ~15–25s (poll with `wait` + `screenshot`) until the image finishes rendering.
5. Extract it (below), save under the manifest's `file` name, then move to the next image.

### Gotchas that cost real time

- **The preview lies about aspect ratio.** Gemini letterboxes previews. Check real pixels:
  ```js
  Array.from(document.querySelectorAll('img'))
    .filter(i => (i.naturalWidth||0) > 300)
    .map(i => ({w:i.naturalWidth, h:i.naturalHeight}))
  ```
  Gemini also tends to ignore requested ratios and land near 1:1 or 4:5. Don't burn regenerations
  fighting it — take a good image and crop to the manifest size in the next step.

- **You cannot return image bytes to yourself.** The harness blocks base64 in tool results, and blob
  URLs can't be re-fetched from the tool's JS context. Trigger a canvas download and pick the file
  up from disk:
  ```js
  const imgs = Array.from(document.querySelectorAll('img')).filter(i => (i.naturalWidth||0) > 300);
  const t = imgs[imgs.length - 1];              // newest image
  const c = document.createElement('canvas');
  c.width = t.naturalWidth; c.height = t.naturalHeight;
  c.getContext('2d').drawImage(t, 0, 0);
  await new Promise(res => c.toBlob(b => {
    const u = URL.createObjectURL(b);
    const a = document.createElement('a');
    a.href = u; a.download = 'hero-home.jpg';
    document.body.appendChild(a); a.click(); a.remove();
    setTimeout(()=>URL.revokeObjectURL(u), 4000); res();
  }, 'image/jpeg', 0.92));
  ```
  Set `a.download` to the manifest file name each time. Verify on disk (`ls images/`) and move the
  file beside the HTML if the browser dropped it elsewhere.

- **The send button doubles as a stop button.** While a generation is streaming, the same control
  is "Stop response" — clicking it then cancels the previous answer instead of sending your new
  prompt, and your typed text just sits there. Never click it by coordinate. Check the label first
  and only click when it says Submit:
  ```js
  const btn = Array.from(document.querySelectorAll('button'))
    .find(x => /submit|send/i.test(x.getAttribute('aria-label') || ''));
  btn ? (btn.click(), 'sent') : 'still generating — wait and retry';
  ```
  Poll this every ~10s from separate calls; a long polling loop inside one `javascript_tool` call
  hits the 45s CDP timeout.

- **Pressing Return does not submit.** The composer treats Enter as a newline. Always send via the
  Submit button (above).

- **Downloads land in the OS Downloads folder, not the project folder.** The canvas download goes
  wherever Chrome saves files — on macOS that's `~/Downloads`, which the sandbox cannot read. So
  `ls images/` will show nothing and that is not a failure. Generate the whole batch first, then ask
  the user to move all the files into `images/` in one go (the names already match the manifest, so
  they overwrite the placeholders and the HTML needs no edit). Only claim an image is in place after
  the shell actually sees it.

- **Gemini's visible watermark — never strip it with code.** Gemini stamps a small sparkle in the
  bottom-right corner of generated images. DesignXI does not remove it by editing pixels: that is the
  provider's AI-content label, and removing it programmatically may conflict with Google's terms.
  Instead, **before generating, ask the user to turn the mark off at the source**: Gemini → Settings →
  *Media watermark* → Off. Google added this setting in August 2026; it may not appear in countries
  that legally require visible AI labels. The invisible SynthID watermark always stays in the file,
  which is expected and fine. If the setting isn't available, either ship the image with the mark
  (and say so in the handoff), or switch that image to a stock photo (option D) or the user's own
  photo. Don't crop an image just to cut the mark out.

- **Fix the crop, don't regenerate.** If the ratio is off, crop to the manifest `size`:
  ```bash
  python3 references/scripts/fit_image.py --image images/hero-home.jpg --size 1440x900
  ```
  It center-crops (or gravity-crops with `--gravity top|bottom`) and keeps a `*-src.jpg` backup, so
  re-running never compounds the crop.

- **Regenerate on subject, not on ratio.** If the user dislikes an image, change the subject or mood
  line. One or two tries is enough; more than that means the subject description is too vague.

---

## Free stock photos (option D)

Use this when the user prefers real photography, when Gemini isn't available, or for images that
must not be AI-generated (for example, a real-looking person in a sensitive context).

**Sources** — both allow free commercial use without attribution, under their own licenses:
- **Pexels** — pexels.com · license: pexels.com/license
- **Unsplash** — unsplash.com · license: unsplash.com/license

Neither license allows selling unaltered copies of the photo, implying that people or brands shown
endorse the product, or using a recognizable person in a sensitive or misleading way. Check the
license page when in doubt; licenses can change.

**How to pick on-brand photos:**
1. Search with the manifest `subject` in plain words (drop the style and color lines — those are for
   AI prompts), plus a mood word from the Phase 11 design school (e.g. "calm", "minimal", "warm").
2. Use the site's color filter with the Phase 12 primary color where available, so the photo sits
   inside the palette.
3. Prefer photos with calm space where text or UI will sit — the same composition rule as the prompt
   recipe.
4. For persona portraits, choose all personas from similar lighting and background so the set looks
   consistent.

**Download, don't hotlink.** Save each photo into `images/` under the manifest file name, then run
`fit_image.py` for the size. Record the source in `images.json` on that image:

```json
{ "id": "hero-home", "file": "images/hero-home.jpg", "source": "pexels",
  "source_url": "https://www.pexels.com/photo/...", "credit": "Photo by <name> on Pexels" }
```

Attribution isn't required, but list every stock photo with its credit in the handoff and case study
— it is good practice and it lets the client verify the license later.

If the sandbox can't reach these sites, give the user a search phrase per image (in the prompt sheet,
under the Gemini prompt) and let them download the files into `images/` with the same names.

---

## Step 4 — Place the images

Reference them by relative path (`src="images/hero-home.jpg"`) and always write real `alt` text — it
serves screen readers and the SEO-as-UX layer in Phase 11b, and it's on the final QA checklist.

**If the deliverable will be imported into Figma**, embed the images so they survive the import
(external `src` gets dropped):

```bash
python3 references/scripts/embed_images.py --html screens.html
```

It rewrites every local `src` into an inline base64 data URI and saves alongside as
`screens-embedded.html`, so the linked version stays editable.

---

## Fallbacks (in order)

Never stall the design on an image.

1. **Hand over the prompts.** Already done in Step 1 — the sheet exists and the placeholders render.
   Name the exact files to drop in, and keep building.
2. **User-supplied photos.** Anything that fits the subject works; `fit_image.py` sizes it to grid.
3. **Another image tool in the session.** Same prompt text, unchanged — the recipe is tool-agnostic.
4. **Ship the placeholders.** They use the project's own tokens, carry the image ID and intended
   subject, and are visibly labeled — so the deliverable stays coherent and the gap stays honest.
   Mark them in the handoff as "(AI placeholder — generate from صور-البرومبتات.md before launch)".

Options 1 and 4 together mean an interrupted session still hands over something complete and
finishable. That is the whole point of this pipeline.

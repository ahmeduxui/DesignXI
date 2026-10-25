# Humanize the copy — Arabic + English, for UX writing

Microcopy that sounds AI-written quietly cheapens a finished design. After drafting the Phase 13 voice
and any on-screen text (CTAs, error messages, empty states, onboarding, labels, tooltips), run a
humanize pass so every string reads like a person wrote it for *this* product — in both Arabic and
English. Based on the humanizer method (EN) and an Arabic humanizer pass built for this skill.

Two rules hold in both languages:
- **Keep the meaning and the facts.** Never change a number, name, price, or claim; never invent one.
  Humanizing fixes the wording, not the content.
- **Every word earns its place.** Cut what signals importance instead of adding it. Short beats long.

UX copy is tiny, so the AI tells show up concentrated — a 5-word button or a one-line error carries
them worse than a paragraph. The common ones, per language:

---

## English tells (fix on sight)

- **Not X but Y / staging** — "Not just a tracker, but your workspace." → say the one true thing:
  "Track your invoices."
- **One-line dramatic closer** — a sentence that repeats the point for weight ("And that changes
  everything."). Cut it.
- **Forced triad** — "Fast, simple, and secure." → the strongest one, concrete: "Set up in 2 minutes."
- **Dashes / curly everything as the universal connector** — break into real sentences.
- **Sales language** — "Elevate", "Unlock", "Seamless", "Powerful", "Effortlessly", "Supercharge",
  "Take it to the next level." Say what it does instead.
- **Overused AI words** — "leverage", "robust", "delve", "realm", "comprehensive", "streamline",
  "utilize", "foster", "navigate (figuratively)". Prefer the plain word.
- **Bold as decoration / Title Case Everywhere** — bold only what must stand out; sentence case for UI.
- **Vague authority** — "Experts agree", "Studies show" → name it or cut it.
- **Chatbot residue** — "Feel free to", "Simply", "Of course", "Let's dive in." Delete.
- **Re-explaining what the reader knows** — put the action first; don't preface it.
- **Passive / missing subject** — "Your changes have been saved" is fine; "An error has occurred" →
  say what to do: "Couldn't save — check your connection and try again."

## Arabic tells (ع — fix on sight)

- **الفعل الخفيف والمصدر المتراكم** — "تم إجراء عملية تحديث" → فعل مباشر وفاعل: "حدّثنا النظام". أوضح
  بصمة آلية بالعربي.
- **التضخيم والإعلانية** — "يلعب دوراً محورياً"، "نقلة نوعية"، "تجربة سلسة"، "حلول متكاملة"،
  "ارتقِ بـ"، "انطلق نحو" → اشرح الواقعة: "تفتح شركتك من الجوال".
- **مفردات البصمة** — "من الجدير بالذكر"، "تجدر الإشارة"، "في نهاية المطاف"، "بشكل كبير"، "تعزيز"،
  "ترسيخ"، "ركيزة أساسية"، "منظومة متكاملة"، "العالم الرقمي". بدّلها بالكلمة البسيطة.
- **التوازي السلبي** — "ليس مجرد ... بل" — مرة واحدة بالكل إذا كان هو الفكرة، لا أكثر.
- **قاعدة الثلاثة** — "سريع وسهل وآمن" → "بيخلص بخمس دقايق".
- **التحليل المعلّق** — "مما يعكس"، "مما يسهم في"، "الأمر الذي يؤكد". حشو، احذفه.
- **البداية الجاهزة** — "في عالم اليوم"، "هل تساءلت يوماً"، "في ظل التطور المتسارع". ابدأ بالفكرة.
- **التوكيد المفرط** — "جداً"، "للغاية"، "بلا شك" في كل جملة. أبقِ واحدة تقلب الفهم.
- **التحوّط والتملّق وبقايا المحادثة** — "قد يكون من الممكن"، "سؤال ممتاز"، "دعني أشرح". تُحذف.
- **الإعلان عن الفكرة قبل قولها** — "تعال نتعرف على"، "إليك ما تحتاج معرفته". قل الفكرة مباشرة.

---

## Both languages
- **Give it a voice, don't just sterilize it.** Stripped-of-tells copy with no personality still reads
  machine-made. Match the Phase 13 voice; vary sentence length; let an error admit what went wrong.
- **Emotional range.** Not relentlessly upbeat — an empty state can be plain, an error can be direct.
- **Mechanical transitions out** — "Moreover / Furthermore / In conclusion" · "علاوة على ذلك / وفي
  الختام". Let the UI's structure connect, not the words.

## Project rules that override (don't "fix" these)
- The design's **brand voice** from Phase 13, and any approved wording the user chose, win over this
  list — match the voice, don't flatten it.
- **Arabic typography rules** (`references/rtl-arabic.md` + the user's preference): Latin digits inside
  Arabic, no Latin words mid-line, Arabic guillemets «» are fine (not an AI tell).
- Real content only — this pass never turns copy into lorem ipsum or drops a required string.

## Process
1. Draft the microcopy (Phase 13) and the on-screen text (Phase 15).
2. Read each string aloud in its language — does it sound like a person talking?
3. Fix the tells above; keep the facts and the voice.
4. Ask once more: "what still sounds machine-made here?" — then do a final light pass.

> For a long-form English deliverable (a case-study narrative, a blog post), the standalone
> **humanizer** skill does a deeper pass; for Arabic social copy, the **carousel-post-designer** skill
> carries the full Arabic humanizer with a lint script. This file is the in-flow UX-copy pass for both.

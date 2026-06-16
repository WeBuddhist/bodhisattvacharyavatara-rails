---
name: english-plan-from-tibetan
description: Generate a single-day Bodhisattvacharyavatara English practice-plan session for verses that have NO English source commentary (e.g. Chapter 2 onward), working from a user-provided English translation of the Tibetan day plan. Use when the user pastes or attaches the English translation of a bo/ day plan and asks for an English day. Produces options (day_N_option_a/b/c). Companion to english-plan-generator (which is for verses that already have English commentary rails). Output is checked by english-plan-evaluator.
---

# English Plan from a Translated Tibetan Plan

This skill builds one day's English session for the Bodhisattva Challenge when the normal English rails do **not** exist for the verses (no `en-ai/Verses/` summaries, no `2-RAILS/Verses/` packages — the case for Chapter 2 and beyond). Instead of those, it works from material the user supplies and from sources that do exist in the vault.

It is the sibling of `english-plan-generator`. Same six-section output, same voice rules, same notification format. The only difference is where the content comes from. Keep all three skills in sync: this one, `english-plan-generator`, and the QA skill `english-plan-evaluator`.

---

## The reader (unchanged)

A lay Buddhist, new to the philosophy, time-poor, sceptical of formulaic spiritual content. Not a scholar. Many are not native English speakers. Plain words, short sentences, one real idea to carry into the day. When a rule and the reader's experience conflict, serve the reader.

---

## Inputs

1. **The English translation of the Tibetan day plan** — pasted or attached by the user. This is the primary content source. It contains the day's verses (in English), the "benefits", per-verse explanations, and a "how to practice" note, all translated from the bo plan, which itself draws on the Tibetan commentaries.
2. **Day number, chapter, verse range** — from the user, or from `3-TRANSFORMATIONS/Plans/the-bodhisattva-challenge/en/assets/schedule.md`.
3. **Published English verse translation** — `1-SOURCES/Translations/en-David_Karma_Choephel.md`. Use this for the verse text (it is a recognised translation already in the vault). Locate verses by block ID, e.g. `^2-6`.
4. **Canonical Tibetan root** — `1-SOURCES/Translations/bo-བློ་ལྡན་ཤེས་རབ།.md`. Use for the Tibetan verse text.
5. **The Tibetan commentaries** (for grounding and attribution) — `1-SOURCES/Commentaries/bo-རྒྱལ་ཚབ་དར་མ་རིན་ཆེན།.md` (Gyaltsab Darma Rinchen), `bo-ས་བཟང་མ་ཏི་པཎ་ཆེན་བློ་གྲོས་རྒྱལ་མཚན།.md` (Sazang Mati Panchen), `bo-དངུལ་ཆུ་ཐོགས་མེད།.md` (Ngulchu Thokme). These cover every chapter, so a specific commentator can usually be named.
6. **The Tibetan plan file** — `bo/Chapter-N .../Day-N-...md` — useful to cross-check the verses, benefits, and practice.
7. **Existing nearby day files** — read the previous one or two days so the opening can note continuation and the practice can be made different (see rules).

> ⚠️ **Grounding integrity.** Everything in "From the Tradition" and "Today's Practice" must trace to the provided translation and/or the Tibetan commentaries. Do not invent a teaching. If a claim cannot be traced, leave it out. Record in `generation_note` that this day was built without English rails and needs domain-specialist review before `status: complete`.

---

## Step 1 — Gather and read

- Get the day number and verse range.
- Read the user's English translation of the Tibetan plan in full.
- Pull the verse text: Tibetan from the root, English from the Choephel translation (by block ID).
- **Read all three Tibetan commentaries on these verses** before writing (see Step 1.5). Do not work from just one.

## Step 1.5 — Find the one added idea (and pick the commentator honestly)

Find **the one thing the commentary adds that a careful reader of the verses alone would not reach** — a distinction, a reason, a consequence, a concrete example. Use the provided translation's "benefits"/explanations plus the Tibetan commentaries.

**Read Gyaltsab, Sazang, and Ngulchu Thokme on the verse, and pick whichever makes the point most precisely.** Do not default to one teacher. (A known failure on this plan was leaning on Ngulchu Thokme repeatedly; across days, vary the commentator and choose by fit, not convenience.) Note the specific passage/block ID you are grounding on. Name that commentator with a one-clause identification on first use. If the point genuinely cannot be tied to one named commentator, attribute it to "the commentary" and say so in `generation_note`.

Everything in 2.4 and 2.6 is built from this one idea.

---

## Step 2 — Compose the six sections

Identical structure and fixed text to `english-plan-generator`.

### Frontmatter

```
---
day: [N]
chapter: [C]
verses: "[C]-[start] to [C]-[end]"
status: draft
option: [A/B/C]
angle: "[one line: the framing and the commentator]"
generation_note: "No en-ai or 2-RAILS material exists for Chapter [C]. English verses from 1-SOURCES/Translations/en-David_Karma_Choephel.md (^...). Commentary grounded in [bo commentary file + block]. Built from the user-provided English translation of the Tibetan plan (bo/...). Interim; needs domain-specialist review before status: complete."
---
```

### Day title and notification

```
# Day [N] — [short specific phrase, max 12 words]

> **Notification**
> **Title:** [a short call to action drawn from today's practice; a question only if the day has no actionable practice]
> **Detail:** [one short, plain line: what today is + the practice]
```

- **Title is an action when the practice gives one** ("Offer something beautiful you pass today"). Use a question only when there is no actionable practice.
- Keep both lines short and plain. No jargon a new reader wouldn't know.

### 2.1 Opening (2–4 sentences, max ~60 words)

- Lead from a plain, everyday entry point, then say what today's verses actually do.
- Note continuation or a chapter/section change ("The offering continues", "Chapter Two begins"). Keep it light and human; never academic.
- **Name who an offering or action is directed to** (e.g. "and gives it all to the buddhas").
- **Gloss or avoid realm jargon**: write "the heavens", not "the god realms"; explain any term a new reader wouldn't know, in one clause, or use a plain word.
- Short sentences. No stacked clauses. No trailing afterthought clauses ("..., though none of it was ever his" → make it its own plain sentence).
- The scope here must match the scope in 2.4 (if the opening reaches "the heavens", 2.4 must not shrink to "this world").

### 2.2 Renewing the Bodhisattva Vow (verbatim)

Reproduce the opening liturgy from `en/assets/liturgy.md` exactly (Mind Training, Refuge, Taking the Bodhisattva Vow), in block-quote with bold labels. Do not preface it with any explanation line, and do not mention audio unless audio actually exists.

### 2.3 Today's Verses

Tibetan (from the root) then English (from the Choephel translation), each verse as a block-quote, verbatim from the source. No paraphrase. Do not introduce stray characters into the Tibetan — paste carefully and verify.

### 2.4 From the Tradition (prose, ~90–120 words, max 150)

Deliver the one added idea. Recommended shape, three moves:

1. **Open with one ordinary, familiar life situation** the idea describes — plain and concrete, not a clever metaphor to decode.
2. **Mark the boundary**: what the verse gives, then where the commentary goes further.
3. **State the added idea plainly**, naming the commentator once with a one-clause identification, grounded in the passage from Step 1.5.

Rules (all carried from this plan's feedback):
- Adds, does not explain. If a reader could get it from the verse, cut it.
- **Plain and simple — readable by a non-native speaker on first read.** Short sentences. No idioms or figures that fail if read literally ("the mind has no edges", "as wide as space", "where each one lands"). Prefer plain verbs over strained noun phrases.
- **No rhetorical question-and-answer.** State the point; do not quiz the reader.
- **Show importance, do not assert it.** No "great", "profound", "vast" as a substitute for a concrete result.
- **Explain a mechanism in concrete steps**, not one compressed abstract sentence.
- **Say who a consequence falls on** (harm, merit, benefit lands on someone — name them).
- Name the commentator **once** (then "he"/"she"). Use the inclusive "we"/"our" for shared human experience.
- No em-dashes in the prose; no emojis. Use the term, don't paraphrase it ("samsara", not "the endless cycle"); keep the grammar around terms plain ("those who carry bodhicitta", not "those in whom bodhicitta has arisen").
- Light bold only — at most a phrase or two (the key line, the name). Never bold whole paragraphs.

### 2.5 Aspiration and Dedication (verbatim)

The closing liturgy from `en/assets/liturgy.md`, block-quote.

### 2.6 Today's Practice (one instruction, tight)

- A **gentle invitation**, not an assignment or a command stack. No "Your task today". Soft/conditional framing ("If you notice...", "When you...").
- One small, **doable action**. Do not ask the reader to watch a presumed bad feeling in themselves.
- Name a **real, specific situation**; if it is an offering, **say who it is offered to** (e.g. "to the Buddha, the Dharma, and the Sangha").
- **Make it different from the previous days' practices.** On a run of similar verses (e.g. the offering verses), do not repeat "picture something beautiful and offer it" each day — change the action so each day's practice is its own.
- No meta closing label ("that is the practice"). End on the action or a light reassurance.

---

## Step 3 — Produce options, then save

- Write **two or three options**: `day_[N]_option_a.md`, `_b.md`, `_c.md`, each a complete day file.
- Give each a **different angle and, where the verse allows, a different commentator** (this is the main way to avoid leaning on one teacher).
- Offer to combine the user's favourite parts into a new option, and to promote the chosen one to the canonical `[N].md`.
- Save to `3-TRANSFORMATIONS/Plans/the-bodhisattva-challenge/en/Days/Chapter-[C] .../`.

---

## Language and register (shared with english-plan-generator)

Plain, warm adult voice. Common terms (bodhicitta, bodhisattva, samsara, karma, merit, refuge) used by name, never paraphrased and never defined. Less common terms get a one-clause gloss. No diacritics in English prose (Shantideva, not Śāntideva; Maitribala, not Maitrībala). No em-dashes in body prose (the title separator is the one exception); no emojis. Short sentences; every sentence understood on first read.

---

## Quality checklist before saving

- [ ] Built from the user-provided translation + Tibetan commentaries; `generation_note` records no-English-rails and "needs specialist review".
- [ ] The one added idea was found by reading all three commentaries; the commentator chosen by fit, named once with a one-clause ID; the teacher is not the same one used the day before by default.
- [ ] Six sections present and ordered; liturgy verbatim; verses Tibetan (root) + English (Choephel), verbatim, no stray characters.
- [ ] Notification: action Title (or a question only if no action), short plain Detail.
- [ ] Opening: plain, anchored to the verses, names who the action is for, no realm-jargon, scope matches 2.4.
- [ ] From the Tradition: plain and non-native-readable; no rhetorical Q&A; shows not asserts; mechanism in steps; says who consequences fall on; light bold only.
- [ ] Practice: gentle invitation, doable, names a real situation and (if an offering) the recipient, and is **different from the adjacent days' practices**.
- [ ] No em-dashes in prose, no emojis, no paraphrased terms, no awkward trailing clauses.
- [ ] Saved as `day_[N]_option_*.md` in the correct chapter folder.

---

## What this skill does NOT do

- It does not mark anything `status: complete` — a domain specialist does that after confirming grounding.
- It does not invent commentary. No English rails is a reason to use the provided translation and the Tibetan commentaries carefully, not a licence to make things up.

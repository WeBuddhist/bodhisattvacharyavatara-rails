---
name: english-plan-from-tibetan
description: Generate a single-day Bodhisattvacharyavatara English practice-plan session for Chapter 2 onward, grounded in the 2-RAILS/Verses/ verse summaries and cross-checked against the Tibetan day plan in Plans/Dalai Lama/. Use when the user asks for an English day for a chapter that has no en-ai/Verses/ summaries. Output is checked by english-plan-evaluator.
---

# English Plan from the Rails and the Tibetan Plan

This skill builds one day's English session for the Bodhisattva Challenge for chapters that lack `en-ai/Verses/` summaries — Chapter 2 onward.

> ⚠️ **Corrected 2026-07-30.** This skill previously stated that no `2-RAILS/Verses/` packages exist for Chapter 2 and beyond. **That is false.** `2-RAILS/Verses/2-1-summary.md` through `2-65-summary.md` exist and cover the whole chapter, each carrying eight commentators with block-ID citations, a metaphors section, main teaching points, key terms, and a synthesis. The old instruction sent writers to the Tibetan day plan alone, which is itself a compressed digest of those same commentaries. Days 26–31 were first drafted that way and had to be rebuilt: gaps had been filled by the writer's own reasoning, and one simile was attributed to the Dalai Lama when it is scriptural, used by Minyak Kunsö and Kunzang Palden. **Always go to the rails first.**

It is the sibling of `english-plan-generator`. Same voice rules. The differences are where the content comes from and which output format applies. Keep these in sync: this one, `english-plan-generator`, `hindi-plan-from-english`, and the QA skill `english-plan-evaluator`.

## Output format — check which one before writing

**Compact format (current, Chapter 2 onward).** Four sections, exact wording: `## Today's Verse`, `## 1) Introduction to Today's Practice`, `## 2) Commentary Explanation`, `## 3) Today's Practice`. No liturgy, no notification block, no day title. Filename `<N>-ch<C>-v<start>-<end>-eng.md`. This is what days 15–31 use, and it is the format the contract in `en/requirements.md` specifies.

**Liturgy format (legacy, Chapter 1 only).** The six-section shape described in Step 2 below, with the `# Day N —` title and `> **Notification**` block. Do not extend it to new chapters without a human decision.

The rest of this file describes the liturgy format because that is what it was written for. When producing the compact format, follow `3-TRANSFORMATIONS/Plans/the-bodhisattva-challenge/en/requirements.md` for structure and this file for grounding and voice.

---

## The reader (unchanged)

A lay Buddhist, new to the philosophy, time-poor, sceptical of formulaic spiritual content. Not a scholar. Many are not native English speakers. Plain words, short sentences, one real idea to carry into the day. When a rule and the reader's experience conflict, serve the reader.

---

## Inputs

1. **The verse rails — primary source, read these first.** `2-RAILS/Verses/<C>-<N>-summary.md`, one per verse in the day's range. Each carries: per-commentator passages (`kunpal`, `khenpo-zhengah`, `gyaltsab`, `ngulchu-thogmed`, `sabzang`, `minyak-kunzang-sonam`, `khenpo-kunga`, `tenzin-gyatso`), a `## དཔེ།` metaphors section, `## གཙོ་གནད།` main teaching points, `## གནད་ཚིག` key terms, and `## བསྡུས་དོན།` synthesis — every item with a block-ID citation into `1-SOURCES/Commentaries/Transcluded/`. The distilled sections (`དཔེ།`, `གཙོ་གནད།`) are the fastest route in.
2. **Day number, chapter, verse range** — from the user, or from `3-TRANSFORMATIONS/Plans/Dalai Lama/Tibetan-schedule-corrected.md`. Filenames in `Plans/Dalai Lama/` encode the range and agree with that schedule for 362 of 365 days.
3. **English verse text** — for the compact format use `1-SOURCES/Translations/translation-ai/bo-en-translation/bca-en-plain.md`, located by block ID, verbatim including its curly apostrophes. For the legacy liturgy format, `1-SOURCES/Translations/en-David_Karma_Choephel.md`.
4. **Canonical Tibetan root** — `1-SOURCES/Translations/bo-བློ་ལྡན་ཤེས་རབ།.md`. Needed for the Tibetan verse text in the liturgy format only.
5. **The Tibetan commentaries** — `1-SOURCES/Commentaries/Transcluded/`: `BCAC19_KKP_bo_segmented.md` (Kunzang Palden), `BCAC19_KS_bo.md` (Khenpo Zhenga), `BCAC14_GDR_bo_segmented.md` (Gyaltsab), `BCAC14_NTS_bo_segmented.md` (Ngulchu Thokme), `BCAC14_SMPLG_bo_segmented.md` (Sazang), `BCAC19_MKS_bo_segmented.md` (Minyak Kunsö), `BCAC20_NKW_bo_segmented.md` (Khenpo Kunga Wangchuk), `BCAC20_TG_bo.toc.md` (the Dalai Lama), `BCAC13_KTB_bo.md` (Renunciation of the World — the source of several stories). Go here when a rail citation needs checking in context. Note: the paths this skill previously listed (`1-SOURCES/Commentaries/bo-*.md`) do not exist.
6. **The Tibetan day plan** — `3-TRANSFORMATIONS/Plans/Dalai Lama/Chapter-N .../Day-N-...md`. This gives the day's chosen angle (`### ༢། ངོ་སྤྲོད།`), the digest commentary (`### ༤། འགྲེལ་བཤད།`), and the practice (`### ༦། དེ་རིང་གི་ཉམས་ལེན།`, with its `ཉམས་ལེན་དངོས།` / `འགྲེལ་བཤད།` / `པར་གྱི་ཚིགས་བཅད།` parts). **Use it for the angle and the practice, not as the grounding for the commentary section.** Only Chapters 1, 2, and four days of Chapter 3 are populated; the rest are 0-byte placeholders.
7. **The contracts** — `en/requirements.md` and `en/termbase.md`.
8. **Existing nearby day files** — read the previous two so the practice can be made different.

> ⚠️ **Grounding integrity.** Every claim in the commentary section must trace to a cited rail passage. Record the rails used in a `context_packages:` frontmatter list, and in `generation_note` name the commentators and block IDs, plus anything retained that only the Tibetan day plan supports. Do not invent a teaching, and do not smooth a gap with your own reasoning — go back to the rail. If the rails and the Tibetan day plan disagree on an attribution, the rails win and the correction goes in `generation_note`. Never set `status: complete`.

> ⚠️ **Never carry a bare proper name.** If a source names a story without telling it, either find the content in `1-SOURCES/Commentaries/Transcluded/` and tell it, or drop the name. "The story of X" gives the reader nothing. Check transliterations against the rails rather than inventing them.

---

## Step 1 — Gather and read

- Get the day number and verse range; confirm it against `Tibetan-schedule-corrected.md`.
- **Read `2-RAILS/Verses/<C>-<N>-summary.md` for every verse in the range, in full.** This is the step that was missing before.

  > ⚠️ Do not stop at `## གཙོ་གནད།` and `## དཔེ།`. Reading only those two sections was the second failure on days 26–31: it produced four `generation_note` entries that wrongly declared rail material to be absent from the rails, and it caused a ⚑ divergence to be flattened into a settled answer. The sections that get skipped and should not be:
  > - `## སྒྲུང་འགྲེལ།` — the stories, told in full. This is where the Netso beehive narrative and the two-mice story actually live.
  > - `## ལུང་།` — scriptural quotations, including the ones a digest attributes to whoever quoted them.
  > - `## གནད་ཚིག` — key terms. **The ⚑ divergences most often sit here**, as two rows with the same term and different glosses.
  > - `## བསྡུས་དོན།` — the synthesis, which states explicitly when `འགྲེལ་ཚུལ་ལ་ཁྱད་པར་ཡོད` (the explanations differ).
- Read the Tibetan day plan's `༢`, `༤`, and `༦` sections for the day's angle and its practice.
- Pull the verse text by block ID, verbatim.
- Read the previous two day files.

## Step 1.5 — Find the one added idea (and pick the commentator honestly)

Find **the one thing the commentary adds that a careful reader of the verses alone would not reach** — a distinction, a mechanism, a stage-analysis, a concrete example. The rails' `གཙོ་གནད།` points are ranked roughly by weight; the best added idea is usually one of the first three, and often it is a point the Tibetan day plan's digest dropped for space.

Examples of what this looks like in practice, from the days already built: that verse 2-28 opens the first of the four opponent powers rather than being a general outpouring (Kunzang Palden, Minyak Kunsö); that from 2-30 the confession shifts from general to object-by-object (Gyaltsab, the Dalai Lama); that "remain before me" at 2-37 means a latent imprint on the consciousness rather than a debt lying in wait (Ngulchu Thokme, Khenpo Kunga Wangchuk, the Dalai Lama); that "such a danger" at 2-42 is three staged fears, not one (Kunzang Palden).

**Read all eight commentators on the verse in the rail and pick whichever makes the point most precisely.** Do not default to one teacher. (Two known failures on this plan: leaning on Ngulchu Thokme repeatedly in Chapter 1, and in the first draft of days 26–31 naming only whoever the Tibetan digest happened to name.) Record the block ID you are grounding on. Name the commentator with a one-clause identification on first use. If a point genuinely cannot be tied to one named commentator, the rails will say `འགྲེལ་བ་ཐམས་ཅད་མཐར་མཐུན` or similar — then write "the commentaries" and say so in `generation_note`.

**Where the rails mark ⚑, carry both readings.** Do not pick one and drop the other; the divergence is often the most interesting thing on the page for a lay reader.

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

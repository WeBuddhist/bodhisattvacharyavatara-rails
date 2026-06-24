---
name: english-plan-generator
description: Generate a complete single-day Bodhisattvacharyavatara practice plan session document in the 6-section format defined in 3-TRANSFORMATIONS/Plans/the-bodhisattva-challenge/en/requirements.md. Saves to 3-TRANSFORMATIONS/Plans/the-bodhisattva-challenge/en/Days/.
---

# English Practice Plan Generator — The Bodhisattva Challenge

This skill generates one day's session document for the 365-day Bodhisattva Challenge English stream. The reader is a practicing Buddhist who is, in most cases, **not a native English speaker** and gives the session about five minutes. Write for that person on every line.

---

## Reader-first principles (read before anything else)

These six principles override older habits. When a detailed rule below seems to conflict with one of these, the principle wins.

1. **A2 English.** Most readers are not native speakers. Use the simplest words and short sentences. (Full rules under "Language and register".)
2. **A narrated voice, not commentary.** Speak *to* the reader, in the second person, in the present tense. Set a scene and let them stand inside it. Do not write *about* the teaching from the outside ("The commentator says... He explains..."). Show first, then name.
3. **One idea per day.** Carry a single concept the whole way through. Do not survey the verses.
4. **The practice challenge is the centre.** Testers respond to it most. Keep it short, concrete, and doable. Make it clearly the one task for the day. Do not bury it under other instructions.
5. **Use rich text generously.** Testers asked for this repeatedly. Bold the key phrase and the takeaway, break the text into short beats with blank lines, and use a short two- or three-item list for a contrast or the parts of one idea. Keep it purposeful, but lean in. The only thing to avoid is true clutter (a bold word on every line, or whole bolded sentences).
6. **Light load.** The whole session is a five-minute read. The liturgy and one challenge are the practice. Do not pile on extra tasks or long passages.

---

## What you are building

Each day file:

- Opens by drawing the reader into a short, concrete scene that prepares today's verses, written in plain narration.
- Contains the fixed opening liturgy (four immeasurables, refuge, bodhisattva vow) reproduced verbatim.
- Presents the day's root verses in Tibetan and a clear, factual English translation, read as a unit.
- Offers one idea from the commentary tradition, told as narration rather than analysis — something the verses alone do not make visible.
- Closes with the fixed aspiration and dedication prayers reproduced verbatim.
- Ends with one short, concrete practice challenge grounded in what the commentators specifically say.

The output is saved as `3-TRANSFORMATIONS/Plans/the-bodhisattva-challenge/en/Days/[DAY_NUMBER].md`.

---

## Source files

| File                                                                        | Purpose                                                                                                                                                                                                         |
| --------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `1-SOURCES/Translations/bo-བློ་ལྡན་ཤེས་རབ།.md`                              | **Root text.** Canonical Tibetan. Extract verses exactly as they appear.                                                                                                                                        |
| `3-TRANSFORMATIONS/Translations/en-ai/en-AI-generated-root-loden-sherab.md` | **Verse translation.** AI-generated English of the Loden Sherab root text. Use block IDs to locate each verse.                                                                                                  |
| `3-TRANSFORMATIONS/Plans/the-bodhisattva-challenge/en/assets/liturgy.md`    | **Fixed liturgy.** Opening and closing prayers reproduced verbatim in sections 2.2 and 2.5.                                                                                                                     |
| `3-TRANSFORMATIONS/Translations/en-ai/Verses/<verse-id>.md`                 | **Commentary summaries (interim).** Combined summaries from Gyaltsab Darma Rinchen, Sazang Mati Panchen, and Ngulchu Thokme Zangpo. Use until `2-RAILS/Verses/<verse-id>.md` packages reach `status: complete`. |
| `2-RAILS/Verses/<verse-id>.md`                                              | **Verse context packages (preferred).** Use when `status: complete`. Supersedes interim sources.                                                                                                                |
| `3-TRANSFORMATIONS/Plans/the-bodhisattva-challenge/en/assets/schedule-corrected.md`   | **Verse schedule.** Maps day numbers to chapter, verse range, and date.                                                                                                                                         |

> ⚠️ **Rail status check:** Only rails with `status: complete` may be used for sections 2.4 and 2.6. If no complete rail exists, use the interim commentary summaries and record this in the frontmatter `generation_note`. If neither source exists for a verse, stop and flag the dependency. Do not invent content.

---

## Step 1 — Gather inputs

Ask the user (or infer from context) for:

1. **Day number** (1–365). Required.
2. **Chapter** and **verse range.** If not provided, look up from `assets/schedule-corrected.md`.

Once you have the chapter and verse range, read all source files before writing. Extract the Tibetan verse text, the English translation (by block ID from `en-AI-generated-root-loden-sherab.md`), and the commentary material from the appropriate verse package(s). **Choose your single concept now**, before drafting, so the whole file can carry it.

---

## Step 2 — Compose the 6-section document

Fixed sections are reproduced verbatim from `en/assets/liturgy.md`. Variable sections are written fresh each day.

### Frontmatter

```
---
day: [DAY_NUMBER]
chapter: [CHAPTER_NUMBER]
verses: "[CHAPTER_NUMBER]-[VERSE_START] to [CHAPTER_NUMBER]-[VERSE_END]"
status: draft
concept: "[the single idea this day carries]"
generation_note: "[note if interim sources were used; omit if 2-RAILS packages were used]"
---
```

### Day title

```
# Day [DAY_NUMBER] — [NOTIFICATION_TEXT]
```

The day title doubles as the notification text in the phone tray. One phrase or clause, **maximum 12 words**. Rules:

- Specific to today's verses. A reader should be able to tell which theme the day covers.
- Real and concrete. Genuine curiosity, not manufactured enthusiasm.
- No rhetorical questions. No affirmations. No quotation marks unless quoting the text.
- The `—` after the day number is the one permitted structural separator; do not use em dashes anywhere else (see Formatting rules).

---

### Section 2.1 — Opening

```
## Opening

[OPENING — narrated, max 60 words]
```

The first thing the reader sees after the notification. Its job is to **draw them into today's verses through a short, concrete scene or question they recognise from their own life**, then point to the verses ahead.

- Narrated and second person. Put the reader inside a small, familiar moment ("Imagine you are tired and someone hands you a plate of food, then walks away.").
- A recommended device: the **receiver's-eye view.** Let the reader feel the situation from the inside before any teaching is named. This is what made the strongest Day 12 draft work.
- Then orient: name, in one plain sentence, that today's verses begin here, and gesture at where they go (a new chapter, a continued sequence) only if it matters.
- Not a summary, not a spoiler, not a lesson. It prepares; it does not teach.
- Maximum 60 words. Short sentences.

---

### Section 2.2 — Renewing the Bodhisattva Vow

```
## Renewing the Bodhisattva Vow

[VERBATIM LITURGY from en/assets/liturgy.md — "Opening" heading]
```

The fixed opening liturgy in this order: four immeasurables → refuge → bodhisattva vow. Reproduced exactly as in `en/assets/liturgy.md`, in block-quote format.

Do not vary, condense, paraphrase, or add headers inside the liturgy. The repetition is the point: readers are recommitting, not reading for new information.

---

### Section 2.3 — Today's Verses

```
## Today's Verses

> [Tibetan verse — from bo-བློ་ལྡན་ཤེས་རབ།.md]
>
> [English verse]

> [next verse, Tibetan]
>
> [next verse, English]
```

Present both layers for each verse before moving on. Tibetan and English each on their own line within a single block-quote. No sub-headers between verses. The passage reads as a unit.

The English must be clear and factual, accurate to the source, not smoothed into paraphrase or lifted into poetry. If a verse needs explanation to be intelligible, flag the translation for revision. Do not compensate with extra commentary in 2.4.

> ⚠️ Both the Tibetan and English verse texts must come from the source files. Do not paraphrase or substitute.

---

### Section 2.4 — From the Tradition

```
## From the Tradition

[NARRATED COMMENTARY NOTE — max 150 words]
```

One idea from the commentary tradition that the verses alone do not make visible. **Not an explanation of the verses.** Its job is to *add* something: a concept the commentators introduce, a distinction they draw, a consequence they trace.

Rules:

- Tell it, do not analyse it. Stay in the narrated, second-person voice from the Opening. Carry the reader from the scene into the idea ("Stay with that plate of food for a moment. You got what you needed. So why does it sting?"). Avoid the textbook register ("The commentator argues that...").
- Add to the verses, not explain them. If a reader could derive the point by rereading the verses, it does not belong here.
- One concept only. Follow it; do not survey.
- Maximum 150 words. Short sentences (A2).
- Rich text is allowed: bold the key phrase, and a short two- or three-item list is fine when it genuinely aids clarity (for example, naming the parts of a single idea). Do not let a list become a survey of separate points.
- Source: `en-ai/Verses/<verse-id>.md` (interim) or `2-RAILS/Verses/<verse-id>.md` (preferred). Use the commentators' specific observations, not a generic synthesis.
- Name the commentator when making a specific attribution (Gyaltsab Darma Rinchen, Sazang Mati Panchen, or Ngulchu Thokme Zangpo). The name alone is usually enough; do not pad with biography ("a Tibetan master who lived about 700 years ago" is too much), and never refer to them vaguely as "an old teacher". Do not open with an attribution phrase.
- Distinguish what a commentator says from a scripture they relay. If the point rests on a sutra or text (not the commentator's own observation), say so plainly ("Ngulchu Thokme shares a teaching from the *Sutra of…*"), not "gives an example" (he is not the author), not figurative "points to a sutra", and not "quotes a sutra" (one quotes *from* a text, not a whole sutra). Attribute the claim itself to the source ("the sutra says…"), not to the commentator.
- When the note rests on a named scripture, name it (English title, no diacritics, italicised) so the claim is verifiable and feels grounded, e.g. the *Sutra of the Mudra of Entering the Definite and Indefinite*. The title is in the rails; do not invent or guess one.
- Define any unavoidable term in plain language, in context, in one clause. No scholastic labels or taxonomy names.
- End on the single idea, stated plainly (a bolded one-line takeaway is encouraged).
- The note must come from the rails. If the tradition does not say it, do not say it.

---

### Section 2.5 — Aspiration

```
## Aspiration

[VERBATIM LITURGY from en/assets/liturgy.md — "Closing" heading]
```

The fixed closing liturgy: aspiration prayer → dedication. Reproduced exactly as in `en/assets/liturgy.md`, block-quote format. Same rules as 2.2.

---

### Section 2.6 — Today's Practice Challenge

```
## Today's Practice Challenge

**Your task today:**

[ONE SHORT INSTRUCTION — second person, present tense]
```

This is the centre of the session. Keep it short and immediately doable.

Rules:

- **One action only.** Not three. Not a numbered list of steps.
- **Short.** One or two short sentences, or a couple of short lines. A bolded micro-instruction is encouraged ("**Slow down. Look at the person. Then give.**").
- Mark it clearly as the day's one task (the "**Your task today:**" line).
- Grounded in the commentary: a traceable line must run from a specific commentator's observation in 2.4 to this action.
- Name a real, specific situation the reader will actually meet, and signal it is an example: a message someone is waiting for, a moment of impatience in line, help asked of you when you are busy. Never "in your daily life" or "when you interact with others."
- Point toward one of three things: doing less harm, doing more good, or knowing your own mind better. If it does not, revise it.
- Prefer an action that lets the reader *embody* the day's idea (if the idea is warmth in giving, have them give one thing warmly).
- Not a wellness tip. Not "breathe" or "pause" disconnected from what the commentators say.
- Second person, present tense, A2.

---

## Producing multiple options for comparison

When asked for several options of the same day for review:

- **All options share one concept.** Keep the single idea identical across them so they can be compared fairly.
- **Vary only the surface:** the opening scene, and the practice action. Optionally hold the narrated voice constant (anchor it to one chosen style) so the comparison isolates scene and action.
- Record the distinguishing angle in a `variant:` frontmatter field, and save as `[DAY]-option-1.md`, `[DAY]-option-2.md`, and so on, until one is chosen and promoted to `[DAY].md`.

---

## Step 3 — Save the file

Save to `3-TRANSFORMATIONS/Plans/the-bodhisattva-challenge/en/Days/[DAY_NUMBER].md`.

- Filename: `[DAY_NUMBER].md` (e.g. `1.md`, `45.md`). No zero-padding.
- Comparison drafts: `[DAY_NUMBER]-option-[n].md` in the same folder.

---

## Language and register

Write for a practicing Buddhist who, in most cases, **reads English at about A2 (elementary) level**.

**Sentence length.** Short. Aim for under about 12 words. Break anything that runs long into two sentences. One idea per sentence. Avoid stacked clauses.

**Word choice.** Everyday words. Prefer "give" over "bestow", "kind" over "benevolent", "the highest happiness" over "supreme felicity". If a plain word exists, use it.

**Buddhist terms** — bodhicitta, bodhisattva, samsara, karma, merit, refuge, dharma, buddha, sangha — are used freely and **never explained or glossed**. This audience knows them. Do not append a definition such as "a bodhisattva, a person who lives for all beings". You may bold a term on first use.

**Keep the term the commentary depends on.** If a commentator's point rests on a specific term (for example, that the merit comes from faith toward a *bodhisattva*), keep that word. Do not soften it into a vague phrase like "a kind person", or the reasoning collapses.

**Name the karmic result "merit".** When a verse or commentary speaks of the positive result of an action (Tibetan *bsod nams*, the "fruit" that increases), call it **merit** — a term this audience knows. Do not paraphrase it into the abstract noun "good" ("creates great good", "even more good", "does enormous good"); used as a noun this way it reads awkwardly. "Brings great merit", "more merit" is natural.

**Rare or technical terms** — "cyclic existence", "two accumulations", "the engaging mind of enlightenment" — are avoided entirely. Do not reach for a word you would then have to explain.

**No idioms or figurative phrases.** Readers are mostly non-native and read literally. Avoid expressions that do not mean what they literally say: "look up to", "hold up", "rush past it", "weigh the same", "plant the seed", "turns cold", "a good heart", "counts for", "points to (a source)". Say "quotes", "uses", "respects", "matters more" instead.

**Clear, complete sentences.** Read each line aloud and make sure it flows.

- Avoid a vague "it" with no clear thing it refers to ("you feel it. Real respect." reads better as "you feel a quiet respect").
- Do not lean on sentence fragments only for emphasis when a full sentence is cleaner. (A short fragment like "A vast kindness." is fine once; a string of them is not.)
- In a contrast, name the subject once in the lead-in ("two thoughts you can have toward a bodhisattva:") rather than repeating it awkwardly ("toward that same bodhisattva").
- Do not repeat the same word in neighbouring lines (e.g. "respect… respect"); vary it ("admire… respect").
- Name the karmic result "merit", not the noun "good" (see above). Use plain, literal wording ("respect", "show", "matters more", "creates good"). Concrete narrated scenes are fine; fixed figurative idioms are not.

**No diacritics** in English prose. Plain spellings only.

| Write | Not |
|---|---|
| Shantideva | Śāntideva |
| Bodhisattvacharyavatara | Bodhisattvacaryāvatāra |
| bodhicitta | bodhicittā |
| samsara | saṃsāra |
| Mahayana | Mahāyāna |
| sutra | sūtra |

**Three marks** in plain English: impermanence, suffering (or unsatisfactoriness), and the constructed nature of self. Not the Pali or Sanskrit terms unless a verse introduces them, glossed in one clause.

**Tibetan script** in 2.2, 2.3, and 2.5 is reproduced exactly from source. The no-diacritics rule applies to English prose only.

**Tone.** Warm, direct, human. A good teacher speaking plainly to one person. Serious without being heavy. Not casual, not formal, not academic.

---

## Formatting rules

- `#` — day title only (doubles as notification text).
- `##` — each of the six sections. No `###` or lower.
- **No helper / descriptor lines under section headings.** Do not add an italic "what this section is" line beneath a heading (e.g. *"A note from the teachers who explained this text."*). The heading stands on its own; the content begins directly.
- Verse and liturgy text: block-quote format (`>`), Tibetan and English each on their own line.
- **Bold** the key phrase, the closing takeaway, the micro-instruction in 2.6, and a term on first use. Use it generously across the day file (testers asked for more rich text), but not so often it stops drawing the eye: no bolded full sentences, no bold word in every line.
- **Short lists** (two to three items) are encouraged where they aid scanning, e.g. a contrast or the parts of one idea. Do not use a list to smuggle in a survey of multiple points.
- **Line breaks.** Break prose into short beats with blank lines between them, rather than one dense block.
- **No em dashes (—) in prose.** They read as machine-written. Use short sentences, commas, or a period instead. The only permitted `—` is the structural separator in the day-title line.
- No horizontal rules (`---`) between sections within a day file.

---

## What is not permitted

- A "Benefits" section listing what the reader will gain.
- An end-of-day glossary (definitions belong in 2.4, in context).
- Tibetan section labels used as English headers (e.g. ཕན་ཡོན། as a title).
- A practice challenge built as a list of steps, or more than one action.
- The construction "Today, I will…" used as a recurring structural device.
- Parenthetical keyword tags: "Releasing Pride (Humility)", "Seeing True Value (Wisdom)".
- "profound benefits"; "practicing and reflecting on today's verses yields the following".
- "The great teacher Shantideva" as a fixed epithet.
- "Based on the traditional commentaries of [names]…" as an opening phrase.
- Commentary-textbook register in 2.4 ("The commentator argues/explains/notes that…") in place of narration.
- Cross-references to other day files ("yesterday's verse", "as we saw last time", "tomorrow we will…"). Each day stands on its own; a reader may arrive on any day, and the plan's concepts do not run in a guaranteed sequence.
- A commentator referred to vaguely ("an old teacher", "the old teachers") instead of being named and briefly identified.
- Em dashes in prose (see Formatting rules).
- Collective pronouns ("we", "us", "our") except where the liturgy itself uses them.
- Any claim in 2.4 or 2.6 not traceable to the source rails.
- Philosophical complexity beyond what the verse requires.
- Sub-headers below `##` level anywhere in the document.

---

## Authenticity test

Apply before saving.

**Authentic looks like:**
- The idea in 2.4 could only have been written about this verse. Swapping it with yesterday's would be obvious.
- The Opening puts the reader inside a moment they recognise, in their own life, before any teaching is named.
- The challenge names a situation so specific the reader sees their own day in it.
- The content in 2.4 comes from the tradition and would not be reachable by rereading the verses alone.
- The writing makes one clear point and stops. It trusts the reader.
- A non-native reader could follow every sentence on the first pass.

**Slop looks like:**
- The note could have been written about any verse in the chapter.
- The challenge could appear in any wellness app on any morning.
- Enthusiasm doing the work substance should do ("This profound verse teaches us…").
- Several points listed because one was not enough to fill the space.
- Technical terms used to sound authentic without being explained or applied.
- The Opening or 2.4 reads like an essay *about* the text rather than a voice speaking *to* the reader.
- Long sentences a non-native reader has to read twice.

A domain specialist must be able to point to the passage in the rails that grounds every claim in 2.4 and 2.6. If a claim cannot be located, drop it however good it sounds.

---

## Quality checklist before saving

- [ ] Frontmatter present: `day`, `chapter`, `verses`, `status`, `concept`, and `generation_note` if interim sources were used.
- [ ] Day title is the notification text: specific, max 12 words, no rhetorical question, no affirmation.
- [ ] Opening (2.1) is narrated and second person, max 60 words, draws the reader into a concrete scene, then points to the verses. Not a summary or lesson.
- [ ] No helper / descriptor lines under any section heading. Content begins directly after each heading.
- [ ] Opening liturgy (2.2) verbatim from `en/assets/liturgy.md`, block-quote, no headers inside the block.
- [ ] Verses (2.3) Tibetan exactly from `bo-བློ་ལྡན་ཤེས་རབ།.md`; English from `en-AI-generated-root-loden-sherab.md`. No sub-headers between verses.
- [ ] From the Tradition (2.4) is one concept, narrated (not analysed), max 150 words, grounded in the rails, names the commentator, does not open with an attribution phrase. "Shantideva" appears at most once.
- [ ] Closing liturgy (2.5) verbatim from `en/assets/liturgy.md`, block-quote.
- [ ] Practice challenge (2.6) is one short action, second person present tense, marked as the day's one task, names a real situation, traceable to 2.4.
- [ ] One concept carried across the whole file (and, for option sets, shared across all options).
- [ ] A2 reading level: short sentences, everyday words, no stacked clauses.
- [ ] Buddhist terms used directly, never explained or glossed. No idioms or figurative phrases; wording is plain and literal.
- [ ] Rich text used generously and purposefully: bolded key phrase and takeaway, short beats with line breaks, a short list for a contrast where it helps.
- [ ] Sentences read cleanly aloud: no vague "it", no string of fragments, no awkward "that same X" repetition, no repeated word in neighbouring lines.
- [ ] No em dashes in prose (only the day-title separator).
- [ ] No diacritics in English prose.
- [ ] No sub-headers below `##` level. No horizontal rules between sections.
- [ ] Saved to `3-TRANSFORMATIONS/Plans/the-bodhisattva-challenge/en/Days/[DAY_NUMBER].md`.

---

## Revision history

**2026-06-10 — Day 2 feedback + Day 12 editorial direction.** Changes from the prior version:

- Added the "Reader-first principles" block and stated the A2, non-native audience up front.
- **Reading level:** replaced "split sentences over 25 words" with an explicit A2 target (short sentences, everyday words).
- **Voice:** added a narrated, second-person, present-tense voice; recommended the receiver's-eye-view device; banned commentary-textbook register in 2.4.
- **Section headings stand alone (later same-day revision):** an earlier draft of this revision required a short italic helper line under each heading; that was removed at the editor's direction. Headings now stand on their own with no descriptor line. Also banned cross-day references and vague unnamed "old teacher" mentions, and trimmed commentator identification to the name alone (no biography).
- **No glosses, no idioms (later same-day revision):** Buddhist terms are now used directly and never explained or glossed (the audience knows them); the term a commentary's point depends on must be kept, not softened into a vague phrase; and idioms / figurative expressions are banned in favour of plain literal wording, since most readers are non-native.
- **Formatting:** reversed the old bans on lists and on bold-for-emphasis. Rich text is now used generously and purposefully (testers asked for more): bold the key phrase and takeaway, break prose into short beats with line breaks, use short contrast lists. Added an em-dash ban in prose.
- **Karmic result is "merit":** name it "merit" (a known term), not the abstract noun "good" ("creates great good" etc.).
- **Scripture citation:** when a note rests on a sutra a commentator relays, name the sutra (English title, no diacritics, from the rails) and attribute the claim to the source ("the sutra says…"); distinguish what a commentator says from what they relay; say "shares a teaching from", not "gives an example", "points to", or "quotes a sutra".
- **Sentence-level clarity:** read lines aloud; no vague "it", no strings of fragments, no awkward "that same X" repetition, no repeated word in neighbouring lines.
- **Practice challenge (2.6):** tightened to one short, marked, embodied action; reinforced "the centre of the session".
- **Light load:** added the five-minute, one-task principle.
- **Comparison options:** added guidance to share one concept across options and vary only scene and action.
- Added `concept:` to frontmatter. Updated the forbidden list, formatting rules, authenticity test, and checklist to match.

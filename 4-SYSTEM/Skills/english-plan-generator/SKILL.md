---
name: english-plan-generator
description: Generate a complete single-day Bodhisattvacharyavatara practice plan session document in the 6-section format defined in 3-TRANSFORMATIONS/Plans/the-bodhisattva-challenge/en/requirements.md. Saves to 3-TRANSFORMATIONS/Plans/the-bodhisattva-challenge/en/Days/.
---

# English Practice Plan Generator — The Bodhisattva Challenge

This skill generates one day's session document for the 365-day Bodhisattva Challenge English stream. Read that file in full before generating anything. All rules there are binding.

---

## What you are building

Each day file:

- Opens with a short orientation paragraph.
- Contains the fixed opening liturgy (four immeasurables, refuge, bodhisattva vow) reproduced verbatim.
- Presents the day's root verses in Tibetan and English, read as a unit.
- Offers one focused note from the commentary tradition — not a summary of all verses, but one thread followed cleanly.
- Closes with the fixed aspiration and dedication prayers reproduced verbatim.
- Ends with one concrete practice instruction grounded in what the commentators specifically say.

The output is saved as `3-TRANSFORMATIONS/Plans/the-bodhisattva-challenge/en/Days/[DAY_NUMBER].md`.

---

## Source files

| File                                                                              | Purpose                                                                                                                                                                                                                |
| --------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `1-SOURCES/Translations/bo-བློ་ལྡན་ཤེས་རབ།.md`                                    | **Root text** — canonical Tibetan. Extract verses exactly as they appear.                                                                                                                                              |
| `3-TRANSFORMATIONS/Translations/en-ai/en-AI-generated-root-loden-sherab.md`       | **Verse translation** — AI-generated English translation of the Loden Sherab root text. Use block IDs to locate each verse.                                                                                            |
| `3-TRANSFORMATIONS/Plans/the-bodhisattva-challenge/en/assets/liturgy.md`          | **Fixed liturgy** — opening and closing prayers reproduced verbatim in sections 2.2 and 2.5.                                                                                                                           |
| `3-TRANSFORMATIONS/Translations/en-ai/Verses/<verse-id>.md`                       | **Commentary summaries (interim)** — combined summaries from Gyaltsab Darma Rinchen, Sazang Mati Panchen, and Ngulchu Thokme Zangpo. Use these until `2-RAILS/Verses/<verse-id>.md` packages reach `status: complete`. |
| `2-RAILS/Verses/<verse-id>.md`                                                    | **Verse context packages (preferred)** — use when `status: complete`. Supersedes interim sources.                                                                                                                      |
| `4-SYSTEM/Skills/en-365-day-practice-plan-generator/references/verse-schedule.md` | **Verse schedule** — maps day numbers to chapter and verse range.                                                                                                                                                      |

> ⚠️ **Rail status check:** Only rails with `status: complete` may be used for sections 2.4 and 2.6. If no complete rail exists, use the interim commentary summaries and record this in the frontmatter `generation_note`. If neither source exists for a verse, stop and flag the dependency — do not invent content.

---

## Step 1 — Gather inputs

Ask the user (or infer from context) for:

1. **Day number** (1–365) — required.
2. **Chapter** and **verse range** — if not provided, look up from `4-SYSTEM/Skills/en-365-day-practice-plan-generator/references/verse-schedule.md`.

Once you have the chapter and verse range, read all source files before writing. Extract: the Tibetan verse text, the AI-generated English translation (by block ID from `en-AI-generated-root-loden-sherab.md`), and the commentary material from the appropriate verse package(s).

---

## Step 2 — Compose the 6-section document

Generate the document using the structure below. Fixed sections are reproduced verbatim from `en/assets/liturgy.md`. Variable sections are generated freshly for each day.

### Frontmatter

```
---
day: [DAY_NUMBER]
chapter: [CHAPTER_NUMBER]
verses: "[CHAPTER_NUMBER]-[VERSE_START] to [CHAPTER_NUMBER]-[VERSE_END]"
status: draft
generation_note: "[note if interim sources were used; omit if 2-RAILS packages were used]"
---
```

### Day title

```
# Day [DAY_NUMBER] — [NOTIFICATION_TEXT]
```

The day title doubles as the notification text — what appears in the phone notification tray. Write it as one phrase or clause, maximum 12 words. Rules:

- Specific to this day's verses. A reader who received this notification should be able to tell which verse or theme the day covers.
- Creates genuine curiosity from a real, specific claim — not manufactured enthusiasm.
- No rhetorical questions. No affirmations. Not in quotation marks unless it is a direct quote from the text.

---

### Section 2.1 — Opening

```
## Opening

[INTRODUCTION]
```

Two to four sentences, maximum 60 words. This is the first thing the reader sees after opening the notification. It orients them to where they are in the training, what the verses are about to offer, and why it matters now.

- Acknowledge the cumulative arc where relevant: if a new chapter begins, say so; if today's verses continue yesterday's argument, note the connection in one clause.
- Not a summary — the reader has not read the verses yet. An orientation, not a spoiler.
- Not a lesson. The introduction prepares; it does not teach.
- Covers any context that would otherwise need explaining in section 2.4. Do not repeat it there.

---

### Section 2.2 — Renewing the Bodhisattva Vow

```
## Renewing the Bodhisattva Vow

[VERBATIM LITURGY from en/assets/liturgy.md — "Opening" heading]
```

The fixed opening liturgy in this order: four immeasurables → refuge → bodhisattva vow. Reproduced exactly as it appears in `en/assets/liturgy.md`. Present as continuous verse in block-quote format.

Do not vary, condense, paraphrase, preface with explanation, or add section headers within the liturgy block. The repetition is the point — readers are recommitting, not reading for new information.

---

### Section 2.3 — Today's Verses

```
## Today's Verses

> [Tibetan verse — from bo-བློ་ལྡན་ཤེས་རབ།.md]
>
> [English verse — from en-David_Karma_Choephel.md]

> [next verse, Tibetan]
>
> [next verse, English]
```

Present both layers for each verse before moving to the next. Tibetan and English on their own lines within a single block-quote. No sub-headers between individual verses. The passage reads as a unit.

The English translation must be self-explanatory after the introduction in 2.1. If a verse requires explanation to be intelligible, flag the translation for revision — do not compensate with extra commentary in 2.4.

> ⚠️ Both the Tibetan and English verse texts must come from the source files. Do not paraphrase or substitute.

---

### Section 2.4 — From the Tradition

```
## From the Tradition

[COMMENTARY NOTE — prose only, maximum 150 words]
```

One focused note from the commentary tradition on a single topic touched by the day's verses. This section is enrichment, not explanation. Its job is to offer something the reader would not have arrived at alone: a specific observation, a distinction, a consequence, or an angle the commentators draw out of these verses.

Rules:

- Pick one topic and follow it. Do not survey all verses or provide a general reading.
- Prose only. No bullet points, sub-headers, or lists.
- Maximum 150 words.
- Source: `3-TRANSFORMATIONS/Translations/en-ai/Verses/<verse-id>.md` (interim) or `2-RAILS/Verses/<verse-id>.md` (preferred). Use the commentators' specific observations — not a generic synthesis.
- Cite a commentator by name when making a specific attribution (Gyaltsab Darma Rinchen, Sazang Mati Panchen, or Ngulchu Thokme Zangpo).
- Shantideva's name at most once. Vary: "he", "the author", "Shantideva". Never "the great teacher Shantideva".
- Do not open with an attribution phrase ("Based on the traditional commentaries of…").
- If a technical term is introduced, define it in one clause in context. No term should require a glossary to understand.
- If the verse touches on one of the three marks — impermanence, the unsatisfactory nature of conditioned things, or the constructed nature of self — draw this out only if the commentators actually make this connection. Do not impose the three marks as a formula.
- The note must come from the rails. If the commentary tradition does not say it, do not say it.

---

### Section 2.5 — Aspiration and Dedication

```
## Aspiration and Dedication

[VERBATIM LITURGY from en/assets/liturgy.md — "Closing" heading]
```

The fixed closing liturgy: aspiration prayer → dedication. Reproduced exactly as it appears in `en/assets/liturgy.md`. Present as continuous verse in block-quote format. Same rules as 2.2.

---

### Section 2.6 — Today's Practice Challenge

```
## Today's Practice Challenge

[ONE INSTRUCTION — second person, present tense]
```

One concrete instruction derived directly from what the commentators say in section 2.4 — not from the verse alone, but from what they specifically say about how this teaching applies. Between one sentence and one short paragraph.

Rules:

- One instruction only. Not three. Not a numbered list.
- Grounded in the commentary: there must be a traceable line from a specific commentator's observation to the practice being suggested. Name the commentator explicitly — not as an academic citation, but as the source of the specific insight (e.g. "Gyaltsab Darma Rinchen notes that… so today, when…").
- Name a real situation the reader will actually encounter: a difficult conversation, a moment of impatience, a craving they recognise, the urge to scroll instead of sit. Not "in your daily life" or "when you interact with others."
- Oriented toward one of three things: doing less harm, doing more good, or knowing your mind better. If it does not point toward one of these, revise it.
- Written in the second person, present tense.
- Not a wellness tip. Not an invitation to breathe or pause in a way disconnected from what the commentators actually say.
- No sub-steps, no "First… Then… Finally…" structure.

---

## Step 3 — Save the file

Save to `3-TRANSFORMATIONS/Plans/the-bodhisattva-challenge/en/Days/[DAY_NUMBER].md`.

- Filename: `[DAY_NUMBER].md` (e.g. `1.md`, `45.md` — no zero-padding).
- Directory: `3-TRANSFORMATIONS/Plans/the-bodhisattva-challenge/en/Days/`

---

## Language and register

Plain English throughout. Write as a literate, warm adult speaking to another adult who practices Buddhism but is not a scholar.

**Common Buddhist terms** — bodhicitta, bodhisattva, samsara, karma, merit, refuge, dharma, buddha, sangha — are used freely without definition. Readers know these words.

**Less common terms** — such as "cyclic existence", "two accumulations", "the engaging mind of enlightenment" — are introduced with a brief in-context gloss on their first appearance within a day file. One clause; no more.

**No diacritics.** Plain simplified spellings in English prose only. Scholarly transliteration (IAST, Wylie) does not appear in day files.

| Write | Not |
|---|---|
| Shantideva | Śāntideva |
| Bodhisattvacharyavatara | Bodhisattvacaryāvatāra |
| bodhicitta | bodhicittā |
| samsara | saṃsāra |
| Mahayana | Mahāyāna |
| sutra | sūtra |

**Three marks** in plain English: impermanence, suffering (or unsatisfactoriness), and the constructed nature of self. Not the Pali or Sanskrit terms unless a verse explicitly introduces them — and if so, gloss in one clause.

**Tibetan script** in sections 2.2, 2.3, and 2.5 is reproduced exactly from the source rails. The no-diacritics rule applies to English prose only.

**Sentence length.** Prefer short sentences. If a sentence exceeds 25 words, consider splitting it. Avoid stacking subordinate clauses.

**Tone.** Warm, direct, serious without being heavy. Not casual, not formal. The register is that of a good teacher speaking plainly.

---

## What is not permitted

The following are forbidden in all sections:

- A "Benefits" section listing what the reader will gain from the verses.
- An end-of-day glossary (definitions belong in 2.4, in context).
- Tibetan section labels used as English headers (e.g. ཕན་ཡོན། as a section title).
- Three-bullet "Daily Life Application" blocks or equivalents.
- The construction "Today, I will…" used as a recurring structural device.
- Parenthetical keyword tags: "Releasing Pride (Humility)", "Seeing True Value (Wisdom)", etc.
- The phrase "profound benefits" or "practicing and reflecting on today's verses yields the following".
- "The great teacher Shantideva" as a fixed epithet.
- "Based on the traditional commentaries of [list of names]…" as an opening phrase.
- Collective pronouns ("we", "us", "our") except where the liturgy text itself uses them.
- Any claim in sections 2.4 or 2.6 not traceable to the source rails.
- Philosophical complexity beyond what the verse requires.
- Sub-headers below `##` level anywhere in the document.

---

## Formatting rules

- `#` — day title only (doubles as notification text).
- `##` — each of the six sections. No `###` or lower.
- Verse text (liturgy, root verses): block-quote format (`>`), Tibetan and English each on their own line.
- Bold: not used for emphasis within prose. Reserved for proper nouns on first use only, where needed for clarity.
- No horizontal rules (`---`) between sections within a day file.

---

## Authenticity test

Apply this test to every section before saving.

**Authentic looks like:**
- The commentary note in 2.4 could only have been written about this specific verse. Swapping it with yesterday's note would be immediately obvious.
- The practice instruction in 2.6 names a situation so specific that the reader recognises their own life in it.
- The depth in 2.4 comes from the commentary tradition and would surprise a careful reader of the verse alone — but is immediately legible once said.
- The writing makes one clear point and stops. It trusts the reader.

**Slop looks like:**
- The commentary note could have been written about any verse in the chapter.
- The practice instruction could appear in any wellness app on any morning.
- Enthusiasm is doing the work that substance should be doing ("This profound verse teaches us the importance of…").
- Multiple points are listed because a single point was not padded enough to fill the space.
- Technical Buddhist terms are used to sound authentic without being explained or applied.

A domain specialist should be able to point to the specific passage in the source rails that grounds every claim in sections 2.4 and 2.6. If a claim cannot be located, do not include it regardless of how it sounds.

---

## Quality checklist before saving

- [ ] Frontmatter present: `day`, `chapter`, `verses`, `status`, and `generation_note` if interim sources were used.
- [ ] Day title is the notification text — specific, max 12 words, no rhetorical question, no affirmation.
- [ ] Opening (2.1) is 2–4 sentences, max 60 words, orients without summarising or teaching.
- [ ] Opening liturgy (2.2) reproduced verbatim from `en/assets/liturgy.md`, block-quote format, no added headers.
- [ ] Verses (2.3) Tibetan extracted exactly from `bo-བློ་ལྡན་ཤེས་རབ།.md`; English from `3-TRANSFORMATIONS/Translations/en-ai/en-AI-generated-root-loden-sherab.md`. No sub-headers between verses.
- [ ] Commentary note (2.4) is prose only, max 150 words, one topic, grounded in the rails, names commentator(s) specifically. Does not open with attribution phrase. "Shantideva" appears at most once.
- [ ] Closing liturgy (2.5) reproduced verbatim from `en/assets/liturgy.md`, block-quote format.
- [ ] Practice challenge (2.6) is one instruction, second person present tense, names a real situation, names the commentator, traceable to 2.4.
- [ ] No forbidden elements present (benefits list, glossary, Tibetan section labels, bullet application blocks, "Today I will…" structure, parenthetical tags, "profound benefits", "great teacher Shantideva", collective attribution opener).
- [ ] No diacritics in English prose.
- [ ] No sub-headers below `##` level.
- [ ] No horizontal rules between sections.
- [ ] Saved to `3-TRANSFORMATIONS/Plans/the-bodhisattva-challenge/en/Days/[DAY_NUMBER].md`.

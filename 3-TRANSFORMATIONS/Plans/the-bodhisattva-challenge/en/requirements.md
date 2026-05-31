# Requirements — Bodhisattva Challenge, English Stream

Style contract for the English-language stream of the *Bodhisattvacaryāvatāra* 365-day plan. Read in full before generating any day file. All rules are binding; no section may be added, removed, or reordered.

---

## 1. Audience

Lay Buddhists who are new to Buddhist philosophy. They are oriented to the bodhisattva path — they know about taking refuge, renewing the bodhisattva vow, and the aspiration to benefit all beings — but have not studied Śāntideva or the Mahāyāna sūtric tradition in depth. They access the plan by phone each morning. They are time-poor and do not want to be given more than they can use. They are sceptical of formulaic spiritual content and will notice — and lose trust at — generic affirmations, padded commentary, and content that could have been written without reading the source text.

Write for someone intelligent who has five minutes and means it.

---

## 2. Session structure

Every day file contains exactly six sections, in this order. No other sections are permitted.

### 2.1 Notification hook

One sentence. Maximum 12 words. This is the push notification text — the first and often only thing the reader sees.

- Must be specific to the day's verses. A reader who does not open the day cannot infer the verse content from the hook — but a reader who does open it should find that the hook was a genuine entry point, not decoration.
- No rhetorical questions.
- No affirmations or generic aspirational phrases ("Begin your day with intention", "Be the change").
- No quotation marks around content that is not a direct quote from the text.
- Not a chapter title or a restatement of the day number.

---

### 2.2 Opening liturgy

The four immeasurables, refuge, and bodhisattva vow, in that order. The text is fixed in `termbase.md` under the key `liturgy.opening` and is reproduced verbatim every day.

- Do not vary, condense, paraphrase, or preface the liturgy with explanation.
- Do not add section headers or commentary within the liturgy block.
- Present as continuous verse in block-quote format.
- The repetition is intentional. Readers are reciting, not reading for new information. There is nothing to introduce.

---

### 2.3 Today's verses

The root text passage(s) assigned to this day. Present in two layers:

1. Tibetan source text, exactly as it appears in the relevant `2-RAILS/Verses/` package. Do not alter, correct, or modernise the Tibetan.
2. English translation, using the rendering locked in `termbase.md`. If a verse's rendering is not yet in the termbase, stop and update the termbase before generating.

Present both layers for each verse before moving to the next. No sub-headers between individual verses. The passage reads as a unit.

---

### 2.4 Reading for meaning

One to three short paragraphs drawn from the commentary tradition via the source rails. Maximum 200 words total.

This section explains what the day's verses open up — the interpretive move the commentators make, the consequence that follows from taking the verse seriously. It is not a summary of the verses (the reader just read them), not a list of benefits, and not a synthesis that the reader could have produced without the commentary tradition.

Style:

- Prose only. No bullet points, numbered lists, bold-keyword-parenthetical pairs (e.g. "Releasing Pride (Humility)"), or sub-headers.
- Śāntideva's name appears at most once per section. Vary the reference: "he", "the author", "Śāntideva". Never use "the great teacher Śāntideva" as a fixed epithet.
- Do not open with an attribution phrase ("Based on the traditional commentaries of…"). The authority of the commentary tradition is established by the rails; it does not need to be announced in the prose.
- Do not front-load the conclusion. Let the commentary move as an argument or an unfolding.
- Technical terms may be introduced here. Define them in context on their first appearance within the day — not in a separate end-of-day glossary. Keep definitions brief: one clause, not a paragraph.
- Write as if explaining to a thoughtful person who is new to the tradition but not to serious reading.

---

### 2.5 Aspiration and dedication

The aspiration prayer and dedication verses, in that order. The text is fixed in `termbase.md` under the key `liturgy.closing` and is reproduced verbatim every day.

Same rules as 2.2. Present as continuous verse in block-quote format. Do not vary, condense, or explain.

---

### 2.6 Today's practice

One concrete instruction, grounded in and specific to the day's verse(s). Between one sentence and one short paragraph.

- One instruction only. Not three. Not a numbered list.
- Specific: a reader who had not read the verses could not follow the instruction. If the practice could have been written on any day, it is too generic.
- Not a wellness tip. Not an invitation to breathe, pause, or be present in a way disconnected from what the verses actually say.
- Written in the second person, present tense.
- No sub-steps, no "First… Then… Finally…" structure.

---

## 3. What is not permitted

The following are forbidden in all sections:

- A "Benefits" section listing what the reader will gain from the verses.
- An end-of-day glossary (definitions belong in 2.4, in context).
- Tibetan section labels used as English headers (e.g. ཕན་ཡོན། as a section title in an English file).
- Three-bullet "Daily Life Application" blocks or equivalents.
- The construction "Today, I will…" used as a recurring structural device across multiple items.
- Parenthetical keyword tags: "Releasing Pride (Humility)", "Seeing True Value (Wisdom)", etc.
- The phrase "profound benefits" or "practicing and reflecting on today's verses yields the following".
- "The great teacher Śāntideva" as a fixed epithet (see 2.4).
- "Based on the traditional commentaries of [list of names]…" as an opening phrase (see 2.4).
- Any claim not traceable to the source rails.

---

## 4. Formatting

- Verse text (liturgy, root verses, prayers): block-quote format (`>`), Tibetan and English each on their own line within the block.
- Section headings: `#` for the day title, `##` for each of the six sections. No `###` or lower.
- Tibetan script: used in sections 2.2 (liturgy), 2.3 (root verses), and 2.5 (closing prayers). Not used for section headers or labels in English files.
- Bold: not used for emphasis within prose. Reserved for proper nouns on first use only, where needed for clarity.
- No horizontal rules (`---`) between sections within a day file.

---

## 5. Source-rail dependencies

Each day file draws from:

- `2-RAILS/Verses/<verse-id>.md` — for the disambiguated restatement, commentary synthesis, and translation notes for each verse in the day's passage.
- `2-RAILS/Sections/<section-id>.md` — for days that fall at a chapter or section boundary.

Only rails with `status: complete` may be used. If a needed rail is not complete, do not generate the day file. Stop and flag the dependency.

---

## 6. Termbase

All renderings are locked in `en/termbase.md`. The generation skill must not introduce a keyword rendering not listed there. If a term appears in the day's verses and is absent from the termbase, update the termbase first and add the new rendering as an attestation row in the relevant `2-RAILS/Bilingual-Glossaries/` consolidated file before proceeding.

The liturgy texts (four immeasurables, refuge, bodhisattva vow, aspiration prayer, dedication) are fixed in the termbase under `liturgy.opening` and `liturgy.closing` and reproduced verbatim in every day file.

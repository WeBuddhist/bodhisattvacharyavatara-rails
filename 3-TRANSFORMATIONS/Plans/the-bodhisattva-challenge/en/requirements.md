# Requirements — Bodhisattva Challenge, English Stream

Style contract for the English-language stream of the Bodhisattvacharyavatara 365-day plan. Read in full before generating any day file. All rules are binding; no section may be added, removed, or reordered.

---

## 1. Audience

Sincere Buddhists who want to improve — as practitioners and as human beings. They are not scholars and have not studied Shantideva in depth, but they are serious. They come to the plan because they want to be reminded of what they already know matters: that everything is impermanent, that nothing fully satisfies, that the self they habitually protect is not as solid as it feels. These three reminders are not abstract philosophy for them — they are the ground of daily life, and they keep forgetting.

Their practical compass is simple: do less harm, do more good, know your mind better. They want the day's verses to help them move along this compass. Not to explain it at length. Not to impress them with doctrine. To illuminate one step they can take today.

They do not want to be lectured. They do not want philosophical complexity. They want to be reminded — with care and without padding — of something true and usable.

Write for someone who already knows the basics and is trying to actually live them.

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

This section explains what the day's verses open up — the interpretive move the commentators make, the consequence that follows from taking the verse seriously. It is not a summary of the verses (the reader just read them), not a list of benefits, and not a philosophical exposition.

One move per day. The commentary makes one point and lands it. It does not survey multiple interpretations or build an argument across several ideas. If the verse connects naturally to impermanence, unsatisfactoriness, or the constructed nature of things, follow that connection — but only if the verse actually supports it, not as a formula applied to every day.

Style:

- Prose only. No bullet points, numbered lists, bold-keyword-parenthetical pairs (e.g. "Releasing Pride (Humility)"), or sub-headers.
- Shantideva's name appears at most once per section. Vary the reference: "he", "the author", "Shantideva". Never use "the great teacher Shantideva" as a fixed epithet.
- Do not open with an attribution phrase ("Based on the traditional commentaries of…"). The authority of the commentary tradition is established by the rails; it does not need to be announced in the prose.
- Do not front-load the conclusion. Let the commentary move.
- Technical terms may be introduced here. Define them in context on their first appearance within a day file — not in a separate end-of-day glossary. One clause; no more.
- No philosophical exposition beyond what the verse itself requires. If the commentary note could not be understood without a glossary of technical terms, it is too complex.

---

### 2.5 Aspiration and dedication

The aspiration prayer and dedication verses, in that order. The text is fixed in `termbase.md` under the key `liturgy.closing` and is reproduced verbatim every day.

Same rules as 2.2. Present as continuous verse in block-quote format. Do not vary, condense, or explain.

---

### 2.6 Today's practice

One concrete instruction, grounded in and specific to the day's verse(s). Between one sentence and one short paragraph.

Every practice instruction should orient toward one of three things: doing less harm, doing more good, or knowing your mind better. These are the measure of a useful instruction. If it does not point toward one of the three, revise it.

- One instruction only. Not three. Not a numbered list.
- Specific: a reader who had not read the verses could not follow the instruction. If the practice could have been written on any day, it is too generic.
- Not a wellness tip. Not an invitation to breathe, pause, or be present in a way disconnected from what the verses actually say.
- Written in the second person, present tense.
- No sub-steps, no "First… Then… Finally…" structure.

---

## 3. Language and register

Plain English throughout. Write as a literate, warm adult speaking to another adult who practices Buddhism but is not a scholar.

**Common Buddhist terms** — bodhicitta, bodhisattva, samsara, karma, merit, refuge, dharma, buddha, sangha — are used freely without definition. Readers know these words. Do not over-explain them.

**Less common terms from the text** — such as "cyclic existence", "two accumulations", "the engaging mind of enlightenment" — are introduced with a brief in-context gloss on their first appearance within a day file. One clause; no more.

**No diacritics.** Indic and Tibetan terms in English prose use plain simplified spellings. Scholarly transliteration (IAST, Wylie) is for internal vault documents only and does not appear in day files.

| Write | Not |
|---|---|
| Shantideva | Śāntideva |
| Bodhisattvacharyavatara | Bodhisattvacaryāvatāra |
| bodhicitta | bodhicittā |
| samsara | saṃsāra |
| Mahayana | Mahāyāna |
| sutra | sūtra |

The Tibetan script in sections 2.2, 2.3, and 2.5 is reproduced exactly as it appears in the source rails. The no-diacritics rule applies to English prose only.

**Sentence length.** Prefer short sentences. If a sentence exceeds 25 words, consider splitting it. Avoid stacking three subordinate clauses.

**Tone.** Warm, direct, serious without being heavy. Not casual (no "hey", no reflexive use of contractions as a stylistic tic). Not formal (no "one observes that", no passive constructions to dodge agency). The register is that of a good teacher speaking plainly.

---

## 4. What is not permitted

The following are forbidden in all sections:

- A "Benefits" section listing what the reader will gain from the verses.
- An end-of-day glossary (definitions belong in 2.4, in context).
- Tibetan section labels used as English headers (e.g. ཕན་ཡོན། as a section title in an English file).
- Three-bullet "Daily Life Application" blocks or equivalents.
- The construction "Today, I will…" used as a recurring structural device across multiple items.
- Parenthetical keyword tags: "Releasing Pride (Humility)", "Seeing True Value (Wisdom)", etc.
- The phrase "profound benefits" or "practicing and reflecting on today's verses yields the following".
- "The great teacher Shantideva" as a fixed epithet (see 2.4).
- "Based on the traditional commentaries of [list of names]…" as an opening phrase (see 2.4).
- Any claim not traceable to the source rails.

---

## 5. Formatting

- Verse text (liturgy, root verses, prayers): block-quote format (`>`), Tibetan and English each on their own line within the block.
- Section headings: `#` for the day title, `##` for each of the six sections. No `###` or lower.
- Tibetan script: used in sections 2.2 (liturgy), 2.3 (root verses), and 2.5 (closing prayers). Not used for section headers or labels in English files.
- Bold: not used for emphasis within prose. Reserved for proper nouns on first use only, where needed for clarity.
- No horizontal rules (`---`) between sections within a day file.

---

## 6. Source-rail dependencies

Each day file draws from:

- `2-RAILS/Verses/<verse-id>.md` — for the disambiguated restatement, commentary synthesis, and translation notes for each verse in the day's passage.
- `2-RAILS/Sections/<section-id>.md` — for days that fall at a chapter or section boundary.

Only rails with `status: complete` may be used. If a needed rail is not complete, do not generate the day file. Stop and flag the dependency.

---

## 7. Termbase

All renderings are locked in `en/termbase.md`. The generation skill must not introduce a keyword rendering not listed there. If a term appears in the day's verses and is absent from the termbase, update the termbase first and add the new rendering as an attestation row in the relevant `2-RAILS/Bilingual-Glossaries/` consolidated file before proceeding.

The liturgy texts (four immeasurables, refuge, bodhisattva vow, aspiration prayer, dedication) are fixed in the termbase under `liturgy.opening` and `liturgy.closing` and reproduced verbatim in every day file.

# Requirements — Bodhisattva Challenge, English Stream

Style contract for the English-language stream of The Bodhisattva Challenge: One Year Training in the Way of the Bodhisattva. Read in full before generating any day file. All rules are binding; no section may be added, removed, or reordered.

---

## 1. Audience

Sincere Buddhists who want to improve — as practitioners and as human beings. They are not scholars and have not studied Shantideva in depth, but they are serious. They come to the challenge to train as bodhisattvas — not to learn about the bodhisattva path, but to walk it. Each day's session is one day in a year-long training. The vow renewal is not a preamble; it is the heart of what they are doing.

They want to be reminded of what they already know matters: that everything is impermanent, that nothing fully satisfies, that the self they habitually protect is not as solid as it feels. These three are not abstract philosophy — they are the ground of daily life, and practitioners keep forgetting them.

Their practical compass is simple: do less harm, do more good, know your mind better. They want the day's verses to help them move along this compass. They will also appreciate a little genuine depth — something from the commentary tradition that opens the verse up in a way they couldn't have reached alone. But they do not want to be lectured, and they do not want complexity for its own sake. What they want is authentic, useful, and brief.

The central editorial tension in this plan is between accessible and authentic on one side, and AI-generated self-help content on the other. Every section must sit clearly on the right side of that line. See section 4 for the test.

Write for someone who already knows the basics and is trying to actually live them.

---

## 2. Session structure

Every day file contains exactly six sections, in this order. No other sections are permitted.

### 2.1 Opening — notification text and introduction

This element has two parts displayed together when the reader opens the day.

**Notification text.** One sentence, maximum 12 words. This is what appears in the phone notification tray — the first and sometimes only thing the reader sees.

- Specific to the day's verses. Not a chapter title, not a day number, not a generic aspiration.
- No rhetorical questions.
- No affirmations ("Begin your day with intention", "Be the change").
- Not in quotation marks unless it is a direct quote from the text.

**Introduction.** Two to four sentences. This is the first thing the reader sees after tapping in. It gives them just enough context to enter the day's verses and the liturgy with understanding: where they are in the training, what the verses are about to offer, and why it matters at this point in the year.

- Not a summary of the verses — the reader has not read them yet. An orientation, not a spoiler.
- Not a lesson. The introduction prepares; it does not teach.
- Covers any context that would otherwise need to be explained in section 2.4. Once written here, nothing needs to be repeated there.
- Maximum 60 words.

---

### 2.2 Opening liturgy

The four immeasurables, refuge, and bodhisattva vow, in that order. The text is fixed in `en/assets/liturgy.md` under the heading `Opening` and is reproduced verbatim every day.

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

The English translation must be self-explanatory. A reader who has read the introduction (2.1) and the verses should understand what Shantideva is saying without needing the commentary note. If the translation requires explanation to be intelligible, the translation is at fault, not the reader — flag it for revision rather than compensating in 2.4.

---

### 2.4 Commentary note

One focused note from the commentary tradition on a single topic touched by the day's verses. Maximum 150 words.

The verses are self-explanatory (see 2.3). This section is not an explanation — it is enrichment. Its job is to offer something the reader would not have arrived at alone: a specific observation, a distinction, a consequence, or an angle that the commentators draw out of these verses. It should feel like something worth knowing, not like context the reader needs in order to understand.

Pick one topic from the day's verses and follow it. Do not survey all three verses or provide a general reading. One thread, one point, landed cleanly.

- Prose only. No bullet points, sub-headers, or lists.
- Shantideva's name at most once. Vary: "he", "the author", "Shantideva". Never "the great teacher Shantideva".
- Do not open with an attribution phrase ("Based on the traditional commentaries of…").
- The note must come from the rails. If the commentary tradition does not say it, do not say it.
- If a technical term is introduced, define it in one clause in context. No term should require a glossary to understand.

---

### 2.5 Aspiration and dedication

The aspiration prayer and dedication verses, in that order. The text is fixed in `en/assets/liturgy.md` under the heading `Closing` and is reproduced verbatim every day.

Same rules as 2.2. Present as continuous verse in block-quote format. Do not vary, condense, or explain.

---

### 2.6 Today's practice

One concrete instruction, grounded in and specific to the day's verse(s). Between one sentence and one short paragraph.

Every practice instruction should orient toward one of three things: doing less harm, doing more good, or knowing your mind better. These are the measure of a useful instruction. If it does not point toward one of the three, revise it.

- One instruction only. Not three. Not a numbered list.
- Specific: a reader who had not read the verses could not follow the instruction. If the practice could have been written on any day, it is too generic.
- Name a real situation. Not "in your daily life" or "when you interact with others" — something the reader will actually encounter: a difficult conversation, a moment of impatience, a craving they recognise, the urge to scroll instead of sit. Ground the instruction in a recognisable human moment.
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

## 4. The authenticity test

The line between authentic Buddhist teaching and AI-generated self-help content is real and readers will feel it. Apply this test to every section before finalising a day file.

**Authentic looks like:**
- The commentary note could only have been written about this specific verse. A reader who swapped it with yesterday's note would notice immediately.
- The practice instruction names a situation so specific that the reader recognises their own life in it.
- The depth in section 2.4 comes from the commentary tradition and would surprise a reader who read only the verse. It is not what a careful reader would have thought of unaided — but it is immediately legible once said.
- The writing makes one clear point and stops. It trusts the reader.
- The vow renewal in 2.2 lands as a commitment, not as background noise.

**Slop looks like:**
- The commentary note could have been written about any verse in the chapter, or any verse in the book.
- The practice instruction could appear in any wellness app on any morning.
- Enthusiasm is doing the work that substance should be doing ("This profound verse teaches us the importance of…").
- Multiple points are listed because a single point was not padded enough to fill the space.
- The tone is warm but no one is home — there is no specific claim being made, no risk being taken, nothing a reader could push back on.
- Technical Buddhist terms are used to sound authentic without being explained or applied.

If any section of a day file reads like slop by this test, do not adjust the wording — identify what specific, attributable thing from the rails would replace it, and use that instead.

---

## 5. What is not permitted

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

## 6. Formatting

- Verse text (liturgy, root verses, prayers): block-quote format (`>`), Tibetan and English each on their own line within the block.
- Section headings: `#` for the day title, `##` for each of the six sections. No `###` or lower.
- Tibetan script: used in sections 2.2 (liturgy), 2.3 (root verses), and 2.5 (closing prayers). Not used for section headers or labels in English files.
- Bold: not used for emphasis within prose. Reserved for proper nouns on first use only, where needed for clarity.
- No horizontal rules (`---`) between sections within a day file.

---

## 7. Source-rail dependencies

Each day file draws from:

- `2-RAILS/Verses/<verse-id>.md` — for the disambiguated restatement, commentary synthesis, and translation notes for each verse in the day's passage.
- `2-RAILS/Sections/<section-id>.md` — for days that fall at a chapter or section boundary.

Only rails with `status: complete` may be used. If a needed rail is not complete, do not generate the day file. Stop and flag the dependency.

---

## 8. Termbase

All keyword renderings are locked in `en/termbase.md`. The termbase governs translation consistency only — one chosen English rendering per Tibetan or Sanskrit term, with a one-line rationale. It does not store full texts.

The generation skill must not introduce a keyword rendering not listed in the termbase. If a term appears in the day's verses and is absent, update the termbase first and add the new rendering as an attestation row in the relevant `2-RAILS/Bilingual-Glossaries/` consolidated file before proceeding.

Liturgy texts (four immeasurables, refuge, bodhisattva vow, aspiration prayer, dedication) are stored in `en/assets/liturgy.md` and reproduced verbatim in every day file.

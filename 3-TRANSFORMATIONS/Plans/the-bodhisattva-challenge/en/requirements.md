# Requirements — Bodhisattva Challenge, English Stream

Style contract for the English-language stream of The Bodhisattva Challenge: One Year Training in the Way of the Bodhisattva. Read in full before generating any day file. All rules are binding; no section may be added, removed, or reordered.

---

## 1. Audience

Sincere Buddhists who want to improve — as practitioners and as human beings. They are not scholars and have not studied Shantideva in depth, but they are serious. They come to the challenge to train as bodhisattvas — not to learn about the bodhisattva path, but to walk it. Each day's session is one day in a year-long training. The vow renewal is not a preamble; it is the heart of what they are doing.

They want to be reminded of what they already know matters: the three marks of existence. Everything is impermanent — it arises and passes, without exception. Nothing is fully satisfying — even what feels good contains the seed of loss. The self is not what it appears to be — what they protect and defend moment to moment is more constructed, more illusory, than it feels. These three are not abstract philosophy. They are the ground of daily life, and practitioners keep forgetting them.

Their practical compass is equally simple: do less harm, do more good, know your mind better. This maps directly onto the threefold Buddhist training — ethics, wisdom, meditation — but the audience does not need to know that. They need the training, not the taxonomy.

They want the day's verses to help them move along this compass, and they will appreciate genuine depth from the commentary tradition — something they couldn't have reached from the verse alone. What they do not want: lectures, philosophical complexity, or instructions that could have been written without reading Shantideva. One authentic insight, applied to one real moment in their day, is worth more than three pages of explanation.

The central editorial tension in this plan is between accessible and authentic on one side, and AI-generated self-help content on the other. Every section must sit clearly on the right side of that line. See section 4 for the test.

Write for someone who already knows the basics and is trying to actually live them.

---

## 2. Session structure

Every day file contains exactly six sections, in this order. No other sections are permitted.

### 2.1 Opening — notification text and introduction

This element has two parts displayed together when the reader opens the day.

**Notification text.** One sentence, maximum 12 words. This is what appears in the phone notification tray — the first and sometimes only thing the reader sees.

- Specific to the day's verses. Not a chapter title, not a day number, not a generic aspiration.
- Should create genuine curiosity — not manufactured urgency or enthusiasm, but the kind of curiosity that comes from a real claim. A reader should want to open the day because the notification says something true and specific, not because it promises a good experience.
- No rhetorical questions.
- No affirmations ("Begin your day with intention", "Be the change").
- Not in quotation marks unless it is a direct quote from the text.

**Introduction.** Two to four sentences. This is the first thing the reader sees after tapping in. It gives them just enough context to enter the day's verses and the liturgy: where they are in the training, what the verses are about to offer, and why it matters now.

- Acknowledge the cumulative arc where relevant: if a new chapter begins, say so; if today's verses follow directly from yesterday's argument, note the connection in one clause. The challenge is a year-long training — each day should feel like one step in a sequence, not a standalone reading.
- Not a summary of the verses — the reader has not read them yet. An orientation, not a spoiler.
- Not a lesson. The introduction prepares; it does not teach.
- Covers any context that would otherwise need to be explained in section 2.4. Nothing needs to be repeated there.
- Maximum 60 words.

---

### 2.2 Renewing the Bodhisattva Vow

The four immeasurables, refuge, and bodhisattva vow, in that order. The text is fixed in `en/assets/liturgy.md` under the heading `Opening` and is reproduced verbatim every day.

The three prayers have a specific logic: the four immeasurables set the vast intention (all beings, without exception); refuge establishes orientation (the three jewels as the direction of travel); the bodhisattva vow is the specific commitment being renewed — the daily act that makes this a training, not a reading.

- Do not vary, condense, paraphrase, or preface the liturgy with explanation.
- Do not add section headers or commentary within the liturgy block.
- Present as continuous verse in block-quote format.
- The repetition is the point. This is not informational content read once and discarded — it is a vow renewed daily. Readers are not reading for new information; they are recommitting. There is nothing to introduce.

---

### 2.3 Today's verses

The root text passage(s) assigned to this day. Present in two layers:

1. Tibetan source text, exactly as it appears in the relevant `2-RAILS/Verses/` package. Do not alter, correct, or modernise the Tibetan.
2. English translation from `1-SOURCES/Translations/en-David_Karma_Choephel.md`, using the block ID for the relevant verse. Where the Choephel rendering conflicts with a locked termbase entry, the termbase takes precedence for that term only; flag the conflict in the frontmatter.

Present both layers for each verse before moving to the next. No sub-headers between individual verses. The passage reads as a unit.

The English translation must be self-explanatory. A reader who has read the introduction (2.1) and the verses should understand what Shantideva is saying without needing the commentary note. If the translation requires explanation to be intelligible, the translation is at fault, not the reader — flag it for revision rather than compensating in 2.4.

---

### 2.4 From the Tradition

One focused note from the commentary tradition on a single topic touched by the day's verses. Maximum 150 words.

The verses are self-explanatory (see 2.3). This section is not an explanation — it is enrichment. Its job is to offer something the reader would not have arrived at alone: a specific observation, a distinction, a consequence, or an angle that the commentators draw out of these verses. It should feel like something worth knowing, not like context the reader needs in order to understand.

Pick one topic from the day's verses and follow it. Do not survey all three verses or provide a general reading. One thread, one point, landed cleanly.

When the verse touches on one of the three marks — impermanence, the unsatisfactory nature of conditioned things, or the constructed nature of self — the commentary note is especially well-placed to draw this out. Do so only if the commentators actually make this connection; do not impose the three marks as a formula.

The note should read like what a good teacher would add after students have read the verse themselves: not an explanation of what the verse says, but an observation the students could not have made alone — precise, grounded, and immediately useful for training.

Source: draw from the combined commentary summaries in `3-TRANSFORMATIONS/Translations/en-ai/Verses/<verse-id>.md`. The three commentators are Gyaltsab Darma Rinchen, Sazang Mati Panchen, and Ngulchu Thokme Zangpo. Use their specific observations — not a generic synthesis. Cite the commentator by name when making a specific attribution.

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

### 2.6 Today's Practice Challenge

One concrete instruction derived directly from the commentary material in section 2.4 — not from the verse alone, but from what the commentators specifically say about how this teaching applies. Between one sentence and one short paragraph.

Every practice instruction should orient toward one of three things: doing less harm, doing more good, or knowing your mind better. These are the measure of a useful instruction. If it does not point toward one of the three, revise it.

- One instruction only. Not three. Not a numbered list.
- Grounded in the commentary: there should be a traceable line from a specific commentator's observation to the practice being suggested. Name the commentator explicitly in the practice text itself — not as an academic citation, but as the source of the specific insight being applied (e.g. "Gyaltsab Darma Rinchen notes that…"). If the instruction could have been written without reading the commentaries, it is not specific enough.
- Name a real situation. Not "in your daily life" or "when you interact with others" — something the reader will actually encounter: a difficult conversation, a moment of impatience, a craving they recognise, the urge to scroll instead of sit. Ground the instruction in a recognisable human moment.
- Not a wellness tip. Not an invitation to breathe, pause, or be present in a way disconnected from what the commentators actually say.
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
| buddhas | sugatas (too technical for this audience) |

**The three marks.** Refer to them in plain English: impermanence, suffering (or unsatisfactoriness), and the constructed nature of self (or: the illusory nature of self). Do not use the Pali terms (anicca, dukkha, anatta) or the Sanskrit equivalents unless a verse explicitly introduces them — and if so, gloss in one clause.

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

The ultimate attributability test: a domain specialist reviewing the day file against the source commentaries should be able to point to the specific passage that grounds every claim in sections 2.4 and 2.6. If a claim cannot be located in the source material, it is not authentic regardless of how it sounds.

If any section reads like slop by this test, do not adjust the wording — identify what specific, attributable thing from the rails would replace it, and use that instead.

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
- Philosophical complexity introduced beyond what the verse requires — technical doctrine the audience does not need in order to use the teaching.
- A practice instruction that the reader could not connect back to today's specific verses and commentaries.

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
- `1-SOURCES/Translations/en-David_Karma_Choephel.md` — for the verse translation (block ID per verse).

Only rails with `status: complete` may be used. If a needed rail is not complete, do not generate the day file. Stop and flag the dependency.

**Interim source (while 2-RAILS verse packages are not yet complete).** Use `3-TRANSFORMATIONS/Translations/en-ai/Verses/<verse-id>.md` for commentary material. These files contain combined summaries from Gyaltsab Darma Rinchen, Sazang Mati Panchen, and Ngulchu Thokme Zangpo, drawn from their respective commentaries. They are status: draft and should be superseded by 2-RAILS packages as those become available. Flag use of interim sources in the frontmatter `generation_note`.

---

## 8. Termbase

All keyword renderings are locked in `en/termbase.md`. The termbase governs translation consistency only — one chosen English rendering per Tibetan or Sanskrit term, with a one-line rationale. It does not store full texts.

The generation skill must not introduce a keyword rendering not listed in the termbase. If a term appears in the day's verses and is absent, update the termbase first and add the new rendering as an attestation row in the relevant `2-RAILS/Bilingual-Glossaries/` consolidated file before proceeding.

Liturgy texts (four immeasurables, refuge, bodhisattva vow, aspiration prayer, dedication) are stored in `en/assets/liturgy.md` and reproduced verbatim in every day file.

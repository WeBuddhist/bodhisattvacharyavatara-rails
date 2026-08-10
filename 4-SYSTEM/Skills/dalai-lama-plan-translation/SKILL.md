---
name: dalai-lama-plan-translation
description: Translate the three prose sections of a Dalai Lama track Tibetan day plan (༢། ངོ་སྤྲོད། introduction, ༤། འགྲེལ་བཤད། commentary, ༦། དེ་རིང་གི་ཉམས་ལེན། today's practice) into simple English and simple Hindi. Translation only — no added content, no rails synthesis. Use when asked to translate, render, or produce English/Hindi versions of a day file under 3-TRANSFORMATIONS/Plans/Dalai Lama/.
---

# Dalai Lama Plan — Prose Translation (en + hi)

Translates **three sections and nothing else** from a Tibetan day file in
`3-TRANSFORMATIONS/Plans/Dalai Lama/Chapter-<C> D<start>-D<end>/Day-<N>-Ch<C>-V<start>-<end>.md`:

| Section | Tibetan heading | What it is |
|---|---|---|
| ༢ | `ངོ་སྤྲོད།` | Introduction — locates the verses, previews the theme, invites the reader in |
| ༤ | `འགྲེལ་བཤད།` | Commentary — expository explanation of what the verses teach |
| ༦ | `དེ་རིང་གི་ཉམས་ལེན།` | Today's practice — first-person commitment plus its explanation |

**Sections ༡, ༣, ༥ are out of scope.** They hold the four immeasurables, refuge,
bodhicitta generation, the root verses, the dedication and the aspiration. Those
are liturgy and canonical verse; they are retrieved from fixed sources elsewhere
in the course, never re-translated per day. Do not translate them here, and do
not carry them into the output file.

## This is a translation skill, not an authoring skill

Do not consult `2-RAILS/`. Do not add explanation, context, or a "point" the
Tibetan does not make. Do not drop anything the Tibetan does make. The companion
skills `bilingual-day-plan-from-rails` and `english-plan-generator` are for
*authoring* grounded content; this one is not. If a sentence in your output has
no parent clause in the Tibetan, delete it — even if it reads well, even if it
is true, even if a reader would benefit.

---

## Step 0 — Scope and preconditions

Confirm before reading anything:

- Which day number(s). Verify the file exists and is populated — as of writing,
  only Chapter 1 (all 14), Chapter 2 (26), Chapter 3 (4) and Chapter 4 (2) have
  content. An empty or stub day file is a stop, not a guess.
- Verify the verse range in the filename against
  `3-TRANSFORMATIONS/Plans/Dalai Lama/Tibetan-schedule-corrected.md`.
- Both languages by default. English and Hindi are each translated **directly
  from the Tibetan**, not one from the other (§4).

## Step 1 — Locate the sections by heading, never by number

Section numbering is not stable across this corpus. In the Dalai Lama track,
section ༦ is `དེ་རིང་གི་ཉམས་ལེན།` in 26 files but `ཉམས་སུ་ལེན་ཚུལ།` in 14. In the
neighbouring `Plans/Himalayan/` track, section ༦ is the *dedication*. A skill
that grabs "section six" will eventually translate a dedication verse as a
practice instruction.

Match on this variant table, then confirm the content shape before translating:

| Slot | Accepted headings |
|---|---|
| Introduction | `ངོ་སྤྲོད།` |
| Commentary | `འགྲེལ་བཤད།` (as a `###` section heading, **not** the `####` per-verse `འགྲེལ་བཤད།` sub-headings under ༣, and **not** the `**འགྲེལ་བཤད།**` bold sub-label inside ༦) |
| Practice | `དེ་རིང་གི་ཉམས་ལེན།`, `ཉམས་སུ་ལེན་ཚུལ།`, `ཉིན་རེའི་འཚོ་བའི་ནང་ཉམས་སུ་ལེན་ཚུལ།` |

Shape checks: the introduction is a single paragraph; the commentary is one or
two paragraphs of continuous prose with no block quotes; the practice section
opens with a bold sub-label. If a slot is missing, empty, or fails its shape
check, **stop and report it** — do not substitute a neighbouring section.

## Step 2 — Parse section ༦ as labelled sub-blocks

Its internal shape varies. Sub-labels observed: `**ཉམས་ལེན་དངོས།**` (12 files),
`**ལག་ལེན།**` (14), and the explanation label as both `**འགྲེལ་བཤད།**` and
`**འགྲེལ་བཤད།:**`.

**Translate only these two sub-blocks:**

| Tibetan label | English | Hindi |
|---|---|---|
| `ཉམས་ལེན་དངོས།` / `ལག་ལེན།` | **The practice** | **अभ्यास** |
| `འགྲེལ་བཤད།` | **Why** | **क्यों** |

**Do not translate, and do not carry into the output:** `མཆན།` (notes),
`ཁ་སྐོང་།` (supplement), `གནད་ཚིག` (key terms), `གཏམ་རྒྱུད།` (story), and the
`#### པར་གྱི་ཚིགས་བཅད།` image-verse block. These are production artifacts and
supplementary material, excluded by decision.

### The practice-category label

The explanation sub-block opens with a parenthetical category in italics. This
is a small controlled vocabulary — render it from this table, never freshly per
file:

| Tibetan | English | Hindi |
|---|---|---|
| `དགེ་བ་བྱ་བ།` | _(Doing good)_ | _(अच्छा काम करना)_ |
| `སྡིག་པ་མི་བྱ་བ།` | _(Avoiding wrongdoing)_ | _(बुरा काम न करना)_ |
| `རང་སེམས་འདུལ་བ།` | _(Taming the mind)_ | _(अपने मन को साधना)_ |
| `སྦྱིན་པའི་ཉམས་ལེན།` | _(Generosity practice)_ | _(दान का अभ्यास)_ |
| `བཟོད་པའི་ཉམས་ལེན།` | _(Patience practice)_ | _(धैर्य का अभ्यास)_ |

A category not in this table is a stop: propose a rendering, log it, and ask.

## Step 3 — Resolve embedded verse quotes by lookup, not translation

Section ༦'s explanation quotes a line or two of the day's root verse inline
(Day-24 quotes `ཞིང་རྡུལ་ཀུན་གྱི་གྲངས་སྙེད་ཀྱི། ལུས་བཏུད་པ་ཡིས་བདག་ཕྱག་འཚལ།` from
verse 2-24). **Never translate these fresh.** Look them up by block ID so the
same verse reads identically everywhere in the course.

**These are the only two verse sources. Do not substitute another.**

| Language | Source |
|---|---|
| English | `AI_translation/english/bca-english-plain.md` |
| Hindi | `AI_translation/hindi/bca-hindi-plain.md` |

Both are full-text, block-ID addressed (`^<C>-<N>`), and in the plain register
this skill targets. Both were produced by the rails translation track, so they
are the course's own renderings — not a third-party translation.

### How to extract a block

Verses are lineated across four lines with the block ID on the **last** line
only. The block for `^2-24` is every line from the blank line after the previous
block ID down to and including the `^2-24` line:

```
To all the buddhas who passed in the three times,
together with the Dharma and the supreme assembly,
I bow with bodies
as numerous as all the atoms of the universe. ^2-24
```

Rules:

- Quote **verbatim** — punctuation, capitalisation and line breaks as they stand.
- Strip the trailing ` ^<C>-<N>` marker from the quoted text.
- The Tibetan usually quotes a *partial* verse (Day-24 quotes only the last two
  lines of 2-24). Take the matching span, not the whole block, and do not
  re-lineate what you take.
- **Diacritics are exempt inside verse quotes.** `bca-english-plain.md` writes
  "Mañjuśrī"; leave it. The no-diacritics rule governs your own prose only.
- If a block ID is absent from the source, stop and ask — do not improvise a
  rendering and do not fall back to another file.

Record the source path and the block IDs quoted in the `translation note`.

## Step 4 — Translate, one register per section

Translate English and Hindi **each directly from the Tibetan**. Do not pivot
Hindi through English: Hindi carries this material natively (धर्म, कर्म, पुण्य,
संसार, बोधिचित्त are living words) and pivoting imports English's compromises.
Reconcile the two for content parity at Step 6.

Load the contracts first: `3-TRANSFORMATIONS/Plans/Dalai Lama/en/termbase.md`
and `hi/termbase.md`.

### Register targets, all three sections

- **Simple.** CEFR A2–B1 for English; everyday spoken Hindi. One idea per
  sentence. Active voice. Target under 20 words per sentence.
- **Break the period.** Tibetan commentary runs long chained clauses landing on
  `ཅེས་པའོ།` or `ཡོད་དོ།`. Day-24's second commentary paragraph is one sentence
  covering praise, prostration, multiplied bodies and four benefits — that
  becomes five or six short sentences. Most "awkward translation" is an English
  sentence still wearing Tibetan syntax, not a wrong word.
- **No honorific archaism.** Tibetan marks respect grammatically (`བཞེས།`,
  `གསོལ་བ་`, `ཐུགས་རྗེ།`). English has no honorific register, so do not reach for
  "deign to accept" or "supplicate" — carry the respect through plain, warm
  phrasing. Hindi *does* have a natural respectful register; use it (आप, ग्रहण
  करें) rather than importing English's flatness.

### Names vs epithets — how "don't translate the lingo" actually applies

Keep genuine terms of art and proper names untranslated: bodhicitta, karma,
samsara, bardo, Dharma, Sangha, Manjushri, Samantabhadra. Give a one-clause
gloss on first use per file where the termbase requires it.

Render **epithets and descriptive titles** plainly — translating these as jargon
is what makes the text unreadable, and it is usually done out of reverence
rather than necessity:

| Tibetan | Write | Not |
|---|---|---|
| `ས་བཅུའི་དབང་ཕྱུག་` / `ས་བཅུའི་བྱང་སེམས་ཆེན་པོ་` | great bodhisattvas who have reached the highest stages | lords of the tenth bhumi |
| `ཐུགས་རྗེ་ཆེན་པོ་ཅན་` | full of compassion | possessed of great compassion / mahakaruna |
| `ཡོན་ཏན་རྒྱ་མཚོ་` | an ocean of good qualities | oceanic assembly of virtues |
| `སྒོ་གསུམ་` | body, speech and mind | the three doors |

### Per-section notes

**Introduction (༢).** Fixed three-move shape: locate the verses, preview the
theme, invite. It ends on an exhortative `སྐུལ་ལོ།` — "one is exhorted to enter
into the practice of…" is exactly the stiffness to avoid. Land it as direct,
warm address. Keep the chapter and verse numbering consistent with the rest of
the course (Arabic numerals in English; Devanagari in Hindi).

**Commentary (༤).** Third person, expository. Preserve attributions exactly as
the Tibetan states them: `སློབ་དཔོན་ཞི་བ་ལྷས།` → "Master Shantideva";
`འགྲེལ་བ་རྣམས་སུ་གསུངས་པ་ལྟར།` → "as the commentaries say". Never drop an
attribution for smoothness and never upgrade a vague one ("the commentaries") to
a specific named commentator.

**Practice (༦).** Stays **first person and forward-looking** — `ངས་དེ་རིང་…
བྱེད་རྒྱུ་ཡིན།` is *"Today I will…"*, not *"You should…"* and not *"The
practitioner bows…"*. Converting this to instruction flips the section from
commitment to command and is the most common failure here. Hindi: आज मैं … करूँगा।

### Unknown terms — never improvise silently

For any Tibetan term not in the forked termbase: check the termbase, then check
already-translated days for existing usage, then pick a rendering **and log it**
under `pending_terms:` in the output frontmatter for human approval. Over a few
chapters this grows the termbase instead of accumulating silent drift.

## Step 5 — Output files

Parallel day files mirroring the Tibetan folder structure:

```
3-TRANSFORMATIONS/Plans/Dalai Lama/en/Chapter-<C> D<s>-D<e>/Day-<N>-Ch<C>-V<s>-<e>-en.md
3-TRANSFORMATIONS/Plans/Dalai Lama/hi/Chapter-<C> D<s>-D<e>/Day-<N>-Ch<C>-V<s>-<e>-hi.md
```

Each contains the three translated sections only, renumbered 1/2/3 in the output
(the source numbering 2/4/6 refers to sections this file does not carry), with
the source's own section numbers recorded in frontmatter.

```markdown
---
title: "Day <N> — Chapter <C>, verses <s>–<e>"
lang_tag: en
plan: dalai-lama
day: <N>
chapter: <C>
verse: "<s>-<e>"
translated_from: "3-TRANSFORMATIONS/Plans/Dalai Lama/Chapter-<C> D<s>-D<e>/Day-<N>-Ch<C>-V<s>-<e>.md"
source_sections: ["༢། ངོ་སྤྲོད།", "༤། འགྲེལ་བཤད།", "༦། དེ་རིང་གི་ཉམས་ལེན།"]
verse_quote_source: "AI_translation/english/bca-english-plain.md"
verse_quotes: ["<C>-<N>"]
pending_terms: []
status: draft
---

## 1. Introduction

## 2. Commentary

## 3. Today's Practice

**The practice** …

**Why** _(Doing good)_ …

## Translation note
```

Hindi headings use Devanagari numerals: `## १. परिचय`, `## २. व्याख्या`,
`## ३. आज का अभ्यास`.

The `translation note` records, in the target language: which verse-quote source
was used, any term added to `pending_terms`, any place the Tibetan was ambiguous
and a reading had to be chosen, and any structural irregularity in the source
file. Write the Hindi note in Hindi — do not machine-translate the English one.

Never set `status: complete`. That is a domain specialist's call.

## Step 6 — Back-mapping audit

Do not deliver on your own read of what you just wrote. Run a **separate pass
with fresh eyes** — ideally a subagent with no memory of the drafting, since a
drafter reliably cannot see their own additions. Give it the Tibetan source and
the output, and instruct it to find violations, not to summarise or approve:

1. **Additions.** For every output sentence, name the Tibetan clause it came
   from. Any sentence with no parent is an addition — cut it.
2. **Omissions.** For every Tibetan clause, name where it landed. Any clause
   with no child is an omission — restore it. Closing and payoff sentences are
   the easiest to lose.
3. **Attribution drift.** Every name and every "as the commentaries say" present
   in the Tibetan is present in the output, unchanged in specificity.
4. **Person and tense.** Section ༦ is still first person and forward-looking in
   both languages.
5. **Parity.** English and Hindi carry the same content — same number of claims,
   same closing. Divergence here means one of them drifted.
6. **Register.** No sentence over ~20 words. No calqued phrasing. No word
   repeated more than twice in a section. Hindi pronouns resolve unambiguously
   (Hindi drops antecedents more easily than English — if it is not obvious who
   "वह" refers to, name the referent).

Verify each finding against the source yourself before acting on it. The auditor
can also be wrong.

## Step 7 — Mechanical checks

Script these; do not eyeball:

- Embedded verse quotes are byte-identical to the span in
  `AI_translation/english/bca-english-plain.md` / `AI_translation/hindi/bca-hindi-plain.md`,
  with only the trailing `^<C>-<N>` marker removed.
- Heading text and order match the template exactly, including numeral style
  (Devanagari in Hindi headings).
- Practice-category label matches the Step 2 table exactly.
- No em-dashes, no diacritics, no emojis in body prose.
- Frontmatter complete; `status: draft`; `translated_from` path resolves.
- Excluded blocks (`མཆན།`, `ཁ་སྐོང་།`, `གནད་ཚིག`, `གཏམ་རྒྱུད།`,
  `པར་གྱི་ཚིགས་བཅད།`) are absent from the output.

## Step 8 — Deliver

Write both files to the paths in Step 5. Report which day(s) were produced,
which verse-quote source was used, and any `pending_terms` awaiting approval.

---

## Known failure modes

- Locating a section by its number and translating the dedication as a practice.
- Translating the root verse quote inside ༦ fresh, so the same verse appears in
  two different English versions across the course.
- Converting ༦ from first-person commitment to second-person instruction.
- Preserving Tibetan sentence length, producing a grammatical but unreadable
  paragraph.
- Rendering an epithet as transliterated jargon ("tenth bhumi") in a sentence
  otherwise aimed at an A2 reader.
- Adding a clarifying clause that is true and helpful but absent from the
  Tibetan — the characteristic failure of meaning-based translation.
- Dropping `འགྲེལ་བ་རྣམས་སུ་གསུངས་པ་ལྟར།` as filler, or resolving it to a named
  commentator the Tibetan does not name.
- Translating the `མཆན།` / `ཁ་སྐོང་།` blocks because they look like body prose.

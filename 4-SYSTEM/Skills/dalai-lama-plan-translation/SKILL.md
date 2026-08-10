---
name: dalai-lama-plan-translation
description: Generate the English and Hindi day files for the Bodhisattva Challenge by translating the Tibetan day plan. Produces the complete day document — Today's Verse (retrieved by block ID), Introduction, Commentary Explanation, and Today's Practice — from the Dalai Lama track Tibetan file's ༢། ངོ་སྤྲོད།, ༤། འགྲེལ་བཤད། and ༦། དེ་རིང་གི་ཉམས་ལེན། sections. Use whenever asked to create, generate, write, fill in or translate an English or Hindi day plan for the Bodhisattva Challenge / Bodhicaryavatara / spyod 'jug 365-day course. This is the only skill for English and Hindi day generation.
---

# Bodhisattva Challenge — English and Hindi day generator

This is **the** generator for English and Hindi day files. It produces a complete
day document by translating the Tibetan day plan, not by synthesising from
commentary rails.

The editorial premise: the Tibetan day file is the source of truth, and the
English and Hindi days are renderings of it. That is what keeps the three
language streams saying the same thing on the same day.

## What the day file is made of

| Output block | Where it comes from |
|---|---|
| Today's Verse | **Retrieved** verbatim by block ID from the verse translation (Step 3) |
| 1) Introduction | **Translated** from `༢། ངོ་སྤྲོད།` |
| 2) Commentary Explanation | **Translated** from `༤། འགྲེལ་བཤད།` |
| 3) Today's Practice | **Translated** from `༦། དེ་རིང་གི་ཉམས་ལེན།` |

Nothing else goes on the page. The Tibetan file's other sections — ༡ (four
immeasurables, refuge, bodhicitta generation), ༣ (root verses in Tibetan) and ༥
(dedication and aspiration) — are liturgy that the course carries elsewhere. Do
not translate or carry them.

## Translation discipline — the core rule

Do not consult `2-RAILS/`. Do not add explanation, context, or a "point" the
Tibetan does not make. Do not drop anything it does make.

If a sentence in your output has no parent clause in the Tibetan, delete it —
even if it reads well, even if it is true, even if a reader would benefit. This
is the difference between this skill and the retired rails-based generators, and
it is the whole reason the three language streams stay aligned.

---

## Step 0 — Scope and preconditions

- Which day number(s). Verify the Tibetan file exists and is populated at
  `3-TRANSFORMATIONS/Plans/Dalai Lama/Chapter-<C> D<s>-D<e>/Day-<N>-Ch<C>-V<vs>-<ve>.md`.
  Coverage as of writing: Chapter 1 (all 14), Chapter 2 (26), Chapter 3 (4),
  Chapter 4 (2). An empty or stub file is a stop, not a guess.
- Verify the verse range against `Plans/Dalai Lama/Tibetan-schedule-corrected.md`.
- Both languages by default, **each translated directly from the Tibetan** — not
  Hindi from English. Hindi carries this material natively (धर्म, कर्म, पुण्य,
  संसार, बोधिचित्त are living words); pivoting through English imports English's
  compromises. Reconcile the two for parity at Step 6.

## Step 1 — Locate the sections by heading, never by number

Section numbering is not stable. In the Dalai Lama track, section ༦ is
`དེ་རིང་གི་ཉམས་ལེན།` in 26 files but `ཉམས་སུ་ལེན་ཚུལ།` in 14. In the neighbouring
`Plans/Himalayan/` track, section ༦ is the *dedication*. A skill that grabs
"section six" will eventually render a dedication verse as a practice
instruction.

Match on this variant table, then confirm the content shape:

| Slot | Accepted headings |
|---|---|
| Introduction | `ངོ་སྤྲོད།` |
| Commentary | `འགྲེལ་བཤད།` as a `###` section heading — **not** the `####` per-verse `འགྲེལ་བཤད།` sub-headings under ༣, and **not** the `**འགྲེལ་བཤད།**` bold sub-label inside ༦ |
| Practice | `དེ་རིང་གི་ཉམས་ལེན།`, `ཉམས་སུ་ལེན་ཚུལ།`, `ཉིན་རེའི་འཚོ་བའི་ནང་ཉམས་སུ་ལེན་ཚུལ།` |

Shape checks: the introduction is a single paragraph; the commentary is one or
two paragraphs of continuous prose with no block quotes; the practice section
opens with a bold sub-label. If a slot is missing, empty, or fails its check,
**stop and report** — do not substitute a neighbouring section.

## Step 2 — Parse section ༦ as labelled sub-blocks

Sub-labels vary: `**ཉམས་ལེན་དངོས།**` (12 files), `**ལག་ལེན།**` (14), and the
explanation label appears both as `**འགྲེལ་བཤད།**` and `**འགྲེལ་བཤད།:**`.

**Translate only these two sub-blocks**, using the plan's established labels:

| Tibetan label | English | Hindi |
|---|---|---|
| `ཉམས་ལེན་དངོས།` / `ལག་ལེན།` | `**Actual Practice:**` | `**मुख्य अभ्यास:**` |
| `འགྲེལ་བཤད།` | `**Explanation:**` | `**व्याख्या:**` |

**Do not translate or carry:** `མཆན།` (notes), `ཁ་སྐོང་།` (supplement),
`གནད་ཚིག` (key terms), `གཏམ་རྒྱུད།` (story), and the `#### པར་གྱི་ཚིགས་བཅད།`
image-verse block.

### Practice-category label

The explanation opens with an italic parenthetical. Controlled vocabulary —
render from this table, never freshly per file:

| Tibetan | English | Hindi |
|---|---|---|
| `དགེ་བ་བྱ་བ།` | _(Doing good)_ | _(अच्छे कर्म करना)_ |
| `སྡིག་པ་མི་བྱ་བ།` | _(Avoiding wrongdoing)_ | _(बुरे कर्म न करना)_ |
| `རང་སེམས་འདུལ་བ།` | _(Taming the mind)_ | _(अपने मन को साधना)_ |
| `སྦྱིན་པའི་ཉམས་ལེན།` | _(Generosity Practice)_ | _(दान का अभ्यास)_ |
| `བཟོད་པའི་ཉམས་ལེན།` | _(Patience Practice)_ | _(धैर्य का अभ्यास)_ |

A category not in this table is a stop: propose a rendering, log it, and ask.

## Step 3 — Today's Verse, and verse lines quoted inside ༦

Both come from the same place, by block-ID lookup. **Never translate a verse
fresh.**

| Language | Source |
|---|---|
| English | `AI_translation/english/bca-english-plain.md` |
| Hindi | `AI_translation/hindi/bca-hindi-plain.md` |

These are the only two verse sources; do not substitute another. Both are
full-text, block-ID addressed (`^<C>-<N>`), and produced by the rails translation
track, so they are the course's own renderings.

**The Today's Verse block:** one block-quote per verse in the day's range,
verbatim, block IDs contiguous and matching the `verse:` frontmatter. Verses are
lineated across four lines with the block ID on the last line only; reproduce
that lineation and keep the trailing `^<C>-<N>`.

**Quotes inside section ༦:** the Tibetan usually quotes a *partial* verse (Day 24
quotes only the last two lines of 2-24). Take the matching span, strip the
trailing `^<C>-<N>` marker, and do not re-lineate what you take.

**Diacritics are exempt inside verse quotes.** `bca-english-plain.md` writes
"Mañjuśrī"; leave it. The no-diacritics rule governs your own prose only.

> ⚑ **Register change from days 15–40.** Those days took the verse from a
> prose-run rendering ("I bow down before every buddha of the past, present, and
> future…"). `bca-english-plain.md` is lineated four-line verse, so new days will
> look different from the existing ones. This is the instructed source — follow
> it, and note the divergence in the translation note.
>
> ⚑ **Hindi gains a verse block.** Existing Hindi days have no `## आज का श्लोक`
> section (days 24 and 25 were already flagged for this in `hi/requirements.md`).
> New Hindi days include it.

If a block ID is absent from the source, stop and ask — do not improvise and do
not fall back to another file.

## Step 4 — Translate, one register per section

Load the contracts first:

- `3-TRANSFORMATIONS/Plans/the-bodhisattva-challenge/en/termbase-translation.md`
- `3-TRANSFORMATIONS/Plans/the-bodhisattva-challenge/hi/termbase-translation.md`

These are **not** `termbase.md` in the same folders. Those govern authored day
content and carry authoring-only rules; `termbase-translation.md` is the fork for
translation and is the one this skill obeys.

### Register targets

- **Simple.** CEFR A2–B1 English; everyday spoken Hindi. Many readers are not
  native English speakers. One idea per sentence, active voice, under 20 words.
- **Break the period.** Tibetan commentary runs long chained clauses landing on
  `ཅེས་པའོ།` or `ཡོད་དོ།`. Day 24's second commentary paragraph is one sentence
  covering praise, prostration, multiplied bodies and four benefits — that
  becomes five or six short sentences. Most "awkward translation" is an English
  sentence still wearing Tibetan syntax, not a wrong word.
- **No honorific archaism.** Tibetan marks respect grammatically (`བཞེས།`,
  `གསོལ་བ་`, `ཐུགས་རྗེ།`). English has no honorific register — do not reach for
  "deign to accept" or "supplicate"; carry the respect through plain, warm
  phrasing. Hindi *does* have one; use it (आप, ग्रहण करें).
- **No em-dashes, no emojis, no diacritics in body prose.** Light bold only.

### Names vs epithets

Keep genuine terms of art and proper names: bodhicitta, karma, samsara, bardo,
Dharma, Sangha, Manjushri, Samantabhadra. Gloss once per file where the termbase
requires it.

Render **epithets and descriptive titles** plainly — translating these as jargon
is what makes the text unreadable, and it is usually done out of reverence
rather than necessity:

| Tibetan | Write | Not |
|---|---|---|
| `ས་བཅུའི་དབང་ཕྱུག་` | great bodhisattvas who have reached the highest stages | lords of the tenth bhumi |
| `ཐུགས་རྗེ་ཆེན་པོ་ཅན་` | full of compassion | possessed of great compassion |
| `ཡོན་ཏན་རྒྱ་མཚོ་` | an ocean of good qualities | oceanic assembly of virtues |
| `སྒོ་གསུམ་` | body, speech and mind | the three doors |

### Per-section notes

**1) Introduction.** Fixed three-move shape: locate the verses, preview the
theme, invite. It ends on an exhortative `སྐུལ་ལོ།` — "one is exhorted to enter
into the practice of…" is exactly the stiffness to avoid. Open with the plan's
established formula, "Today's practice is based on verse(s) … from the …
chapter of the _Bodhicaryāvatāra_." / "आज का अभ्यास _बोधिचर्यावतार_ के …
अध्याय के श्लोक … पर आधारित है।" Note a chapter change when there is one.

**2) Commentary Explanation.** Third person, expository. Preserve attributions
exactly as the Tibetan states them: `སློབ་དཔོན་ཞི་བ་ལྷས།` → "Master Shantideva";
`འགྲེལ་བ་རྣམས་སུ་གསུངས་པ་ལྟར།` → "as the commentaries say". Never drop an
attribution for smoothness and never sharpen a vague one ("the commentaries")
into a named commentator the Tibetan does not name.

**3) Today's Practice.** Stays **first person and forward-looking** —
`ངས་དེ་རིང་… བྱེད་རྒྱུ་ཡིན།` is *"Today I will…"*, not *"You should…"* and not
*"The practitioner bows…"*. Converting this to instruction flips the section
from commitment to command and is the most common failure here. Hindi: आज मैं …
करूँगा।

### Word counts are a diagnostic, not a target

The plan's established bands are: introduction 80–115 words, commentary 180–220,
practice explanation 120–160, actual practice one sentence.

**Do not pad or trim to hit them.** Translation length is set by the source. If a
section lands outside its band, that means the Tibetan section is unusually long
or short — say so in the translation note and leave the text faithful. Padding to
reach a word count is exactly the addition this skill exists to prevent.

### Unknown terms — never improvise silently

For any Tibetan term not in the termbase fork: check the termbase, then check
already-translated days for existing usage, then pick a rendering **and log it**
under `pending_terms:` for human approval. This grows the termbase instead of
accumulating silent drift.

## Step 5 — Output files

```
3-TRANSFORMATIONS/Plans/the-bodhisattva-challenge/en/Days/Chapter-<C> D<s>-D<e>/<N>-ch<C>-v<vs>-<ve>-eng.md
3-TRANSFORMATIONS/Plans/the-bodhisattva-challenge/hi/Days/Chapter-<C> D<s>-D<e>/<N>-ch<C>-v<vs>-<ve>-hi.md
```

Day 24 (Chapter 2, verses 22–24) → `en/Days/Chapter-2 D15-D40/24-ch2-v22-24-eng.md`
and `hi/Days/Chapter-2 D15-D40/24-ch2-v22-24-hi.md`. Match an existing filename
exactly where one is present — do not invent a variant spelling of the range.

### ⚑ Overwrite guard

Days 1–40+ already have files at these paths, produced by the retired rails-based
generators. **Never overwrite one silently.** If the target exists: say so, get
explicit human confirmation, and on approval move the existing file to the
`Archive/` folder beside it rather than destroying it.

### English template

```markdown
---
day: <N>
chapter: <C>
verse: "<vs>-<ve>"
generated_by: dalai-lama-plan-translation
translated_from: "3-TRANSFORMATIONS/Plans/Dalai Lama/Chapter-<C> D<s>-D<e>/Day-<N>-Ch<C>-V<vs>-<ve>.md"
verse_source: "AI_translation/english/bca-english-plain.md"
pending_terms: []
status: draft
---

## Today's Verse

> [verse, lineated] ^<C>-<vs>

> [verse, lineated] ^<C>-<ve>

## 1) Introduction to Today's Practice

## 2) Commentary Explanation

## 3) Today's Practice

**Actual Practice:** …

**Explanation:** _(Doing good)_ …

## Translation note
```

### Hindi template

Same frontmatter with `verse_source: "AI_translation/hindi/bca-hindi-plain.md"`.
Headings use Devanagari numerals:

```markdown
## आज का श्लोक

## १) आज के अभ्यास का परिचय

## २) अर्थ और व्याख्या

## ३) आज का अभ्यास

**मुख्य अभ्यास:** …

**व्याख्या:** _(अच्छे कर्म करना)_ …

## अनुवाद टिप्पणी
```

The translation note records, in the target language: any section that fell
outside its word band and why, any term added to `pending_terms`, any place the
Tibetan was ambiguous and a reading had to be chosen, and any structural
irregularity in the source file. **Write the Hindi note in Hindi** — do not
machine-translate the English one.

Never set `status: complete`. That is a domain specialist's call.

## Step 6 — Back-mapping audit

Do not deliver on your own read of what you just wrote. Run a **separate pass
with fresh eyes** — ideally a subagent with no memory of the drafting, since a
drafter reliably cannot see their own additions. Give it the Tibetan source and
the output, and instruct it to find violations, not to summarise or approve:

1. **Additions.** For every output sentence, name the Tibetan clause it came
   from. No parent means it is an addition — cut it.
2. **Omissions.** For every Tibetan clause, name where it landed. No child means
   it was dropped — restore it. Closing and payoff sentences go missing most.
3. **Attribution drift.** Every name and every "as the commentaries say" in the
   Tibetan is present in the output, unchanged in specificity.
4. **Person and tense.** Section 3 is still first person and forward-looking in
   both languages.
5. **Parity.** English and Hindi carry the same content — same number of claims,
   same closing.
6. **Register.** No sentence over ~20 words. No calqued phrasing. No word
   repeated more than twice in a section. Hindi pronouns resolve unambiguously —
   if it is not obvious who "वह" refers to, name the referent.
7. **Practice repetition.** Check the two previous days: the offering and
   confession verses run in long stretches, and if a distinguishing half of the
   Tibetan instruction gets dropped, two days end up with the same action.

Verify each finding against the source yourself before acting on it. The auditor
can also be wrong.

## Step 7 — Mechanical checks

Script these; do not eyeball:

- Verse block-IDs contiguous and matching `verse:` frontmatter.
- Verse text byte-identical to the source span (trailing `^<C>-<N>` retained in
  the Today's Verse block, stripped in inline quotes inside section 3).
- Heading text and order match the template exactly, including Devanagari
  numerals in Hindi.
- Sub-labels exactly `**Actual Practice:**` / `**Explanation:**` and
  `**मुख्य अभ्यास:**` / `**व्याख्या:**`.
- Practice-category label matches the Step 2 table.
- No em-dashes, diacritics or emojis in body prose.
- Word counts reported per section, with any out-of-band section named in the
  translation note.
- Excluded blocks (`མཆན།`, `ཁ་སྐོང་།`, `གནད་ཚིག`, `གཏམ་རྒྱུད།`,
  `པར་གྱི་ཚིགས་བཅད།`) absent from the output.

## Step 8 — Deliver

Write both files, honouring the overwrite guard. Report which day(s) were
produced, whether any existing file was archived, any section outside its word
band, and any `pending_terms` awaiting approval.

---

## Known failure modes

- Locating a section by number and rendering the dedication as a practice.
- Translating a verse fresh instead of retrieving it, so the same verse reads two
  different ways across the course.
- Converting section 3 from first-person commitment to second-person instruction.
- Padding or trimming a section to hit a word count, which means adding or
  cutting content the Tibetan does not have.
- Preserving Tibetan sentence length, producing a grammatical but unreadable
  paragraph.
- Rendering an epithet as transliterated jargon ("tenth bhumi") in a sentence
  otherwise aimed at an A2 reader.
- Adding a clarifying clause that is true and helpful but absent from the Tibetan
  — the characteristic failure of meaning-based translation.
- Dropping `འགྲེལ་བ་རྣམས་སུ་གསུངས་པ་ལྟར།` as filler, or resolving it to a named
  commentator the Tibetan does not name.
- Reaching into `2-RAILS/` because the Tibetan section feels thin. It is not this
  skill's source.

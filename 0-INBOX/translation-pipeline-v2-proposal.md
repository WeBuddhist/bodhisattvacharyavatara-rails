---
title: Translation Pipeline v2 — proposal
status: draft
author: Claude (at Monlam's request)
date: 2026-08-09
scope: bo → en/hi/mr/zh, three audience registers (scholar / plain / children)
supersedes: the ad-hoc pipeline currently running in AI_translation/
note: This is a proposal in 0-INBOX. Per 4-SYSTEM/CLAUDE.md, rule changes require a
      human contributor. Nothing here takes effect until you approve it and it is
      moved into 4-SYSTEM/ as a skill + rule set.
---

# Translation Pipeline v2

## Why v1 fails, in one sentence

The termbase is built *from the translation*, so it can only ever describe the
inconsistency it was supposed to prevent — which is why the current run shows
**797 unambiguous drifts, 398 ambiguous drifts, and 1 285 terms with no termbase
entry at all**.

v2 inverts this: **the vocabulary contract is built from the Tibetan source and
its commentaries, before a single line of translation is generated**, and it is
enforced mechanically at generation time rather than audited afterwards.

---

# PART 1 — What already exists

## 1.1 `1-SOURCES/` — ground truth (frozen, read-only)

| Asset | Path | State |
|---|---|---|
| Sanskrit root | `Text/BCAV08_SH_sk.md` | 230 KB, block-aligned |
| **Tibetan root (primary)** | `Translations/bo-བློ་ལྡན་ཤེས་རབ།.md` | **1 850 block IDs, covers `1-1`–`10-61`**, full frontmatter, BDRC IDs |
| Tibetan root, tagged | `Translations/bo-བློ་ལྡན་ཤེས་རབ།-tagged.md` | variant |
| English witness W1 | `Translations/en-Padmakara_2006.md` | block-aligned |
| English witness W2 | `Translations/en-Wallace.md` | block-aligned |
| English witness W3 | `Translations/en-David_Karma_Choephel.md` | block-aligned |
| Chinese witnesses | `Translations/zh-*.md` × 5 | block-aligned |
| Tibetan commentaries | `Commentaries/Transcluded/*.md` × 12 | transclude the root; Kunpal, Khenpo Zhenga, Gyaltsab, Ngulchu Thokme, Sabzang, Minyak Kunzang Sonam, Khenpo Kunga, Tenzin Gyatso, Wangchuk Rinpoche |

**Verse counts in the root** (total **930**):
ch1 38 · ch2 67 · ch3 35 · ch4 50 · ch5 111 · ch6 136 · ch7 77 · ch8 187 · ch9 169 · ch10 60

## 1.2 `2-RAILS/` — compiled interpretive context

| Asset | Path | State |
|---|---|---|
| **Verse rails** | `Verses/<id>-summary.md` | **154 files, chapters 1–4 only** (ch1 36/38, ch2 65/67, ch3 33/35, ch4 20/50). **All `status: draft`. Zero `complete`.** |
| **Key-term blocks inside those rails** | `## གནད་ཚིག` sections | **838 blocks**, each = a Tibetan term + a commentary definition (`འགྲེལ་བཤད་`) + a cited source block ID (`ཁུངས།`) |
| Section rails | `Sections/<node>.md` | **1 file only** (`1-0.md`) + `Sections/Raw/` per-commentary summaries for 7 commentaries |
| Local-Wiki | `Local-Wiki/*.md` | **6 articles**: ཆོས་ཀྱི་སྐུ།, དལ་འབྱོར།, བདེ་གཤེགས།, བྱང་ཆུབ་ཀྱི་སེམས།, འཇུག་པའི་སེམས།, སྨོན་པའི་སེམས། — good format (contextual definition + verbatim attestations + `attested_blocks:`) |
| Consolidated glossary | `Bilingual-Glossaries/bo-en.md` | 50 keywords, 239 distinct renderings, `status: draft` |
| Raw glossaries | `Bilingual-Glossaries/Raw/*.md` | 20 files — per-witness interlinear glosses and extracted glossaries |
| Keyword JSONs | `termbases/*.json` | 9 files, bo→en/hi/vi × audience levels |

> **The 838 གནད་ཚིག blocks are the single most valuable asset in this vault for
> your problem.** They are already source-side, already commentary-glossed, and
> already carry a citation. They are the seed of the term index — you do not need
> to extract them again.

## 1.3 `3-TRANSFORMATIONS/` — governed outputs

| Track | Contents |
|---|---|
| `Translations/en-translate/` | `BCA-Full-Children-English.md`, `BCA-Full-Plain-English.md`, `BCA-Full-Scholar-English.md` (~190 KB each) |
| `Translations/en-plain-english/` | `requirements.md`, `audience.md`, `termbase.md` (11 rows), `BCA-Chapters-1-3-Plain-English.md`, `Verses/` |
| `Translations/en-ai/` | `requirements.md`, `audience.md`, `termbase.md`, Chapter 1, 36 verse files, 3 AI-generated commentaries |
| `Translations/hi-poetic/`, `zh-plain-chinese/`, `mr-translate/`, `zh-daily-summary/`, `en-verse-plain-test/` | requirements/termbase at varying completeness |
| `Plans/` | the-bodhisattva-challenge (bo/en/hi/zh), Dalai Lama, Himalayan, DKR-Fellow — 365-day arcs |
| `Adaptations/` | 3 sa-bcad tracks |

## 1.4 `AI_translation/` — the pipeline actually in use (OUTSIDE the vault structure)

| Asset | Path |
|---|---|
| Audience profiles | `audience_profile/{children,plain,scholars}.md` |
| Tibetan split by chapter | `bo-བློ་ལྡན་ཤེས་རབ།_split_chapters/ch1–ch10 + intro + colophon` |
| English zero-shot | `english/bca-english-plain-zeroshot.md`, `bca-english-plain.md` |
| Keywords by reference | `english/keywords-by-reference-tibetan-english-plain.md` |
| **Sense inventory** | `english/tibetan-word-english-senses-plain.md` ← *correct structure, currently discarded* |
| Termbase | `english/tibetan-english-termbase-plain.md` |
| Fact-check report | `english/rails-fact-check-report-bca-english-plain.md` (ch1–4, ch4 vv1–20) |
| Vocab report | `english/vocab-standardization-report.md` (5 939 OK / 534 inflection / **797 unambiguous drift** / **398 ambiguous** / **1 285 untracked**) |
| Hindi | `hindi/` — plain + children zero-shot, keywords, 3 termbases |
| Marathi | `marathi/` — children termbase |
| Local skills | `skills/{zeroshot-translator, keyword-equivalence-mapper, word-sense-grouper, termbase-builder, rails-verse-translator, split-file-by-markers}.md` + `requirements.md` |
| Local scripts | `skills/scripts/{split_chapters, vocab_standardize, rails_fact_check_extract, lint_translation, add_transclusions}.py` |

## 1.5 `Keyword_extractor/` — the TF-IDF attempt (OUTSIDE the vault structure)

`english_keyword/{keywords.py, keywords_by_reference.py, generate_idf_corpus.py, generate_en_translation_idf.py}` + `output/` (5 files). Output is dominated by colophon noise and n-gram fragments; superseded by v2 Phase B.

## 1.6 `4-SYSTEM/` — tooling

**68 skills**, of which the relevant ones are:
`translate-zero-shot`, `translation-qa`, `commentary-fact-check`, `commentary-fact-check-apply-fixes`, `glossary-select`, `glossary-extract-raw`, `glossary-combine`, `interlinear-gloss`, `local-wiki-article`, `verse-context`, `verse-context-batch`, `Verse-Context-Summary`, `section-summary-raw`, `section-summary-combined`, `english-translation`, `hindi-translation`, `vietnamese-translation`, `multilevel-summary`, `rails-to-verse-translation`, `vault-audit`, `create-skill`.

**Scripts:** `termbase-consistency-check/check_termbase_consistency.py`, `glossary_select_termbase.py`, `glossary_audit_and_promote.py`, `merge_chapters.py`, `write_qa_reports.py`, `linter-root-text/`, `parser-root-text/`, `day-package/day_package_tools.py` (+ drift guard).

## 1.7 What does **not** exist yet

- ❌ A sense-split term index (lemma × sense) for the source language
- ❌ Verse rails for chapters 5–10 (776 of 930 verses uncovered — including ch. 9)
- ❌ Section rails beyond `1-0.md`
- ❌ Any rail at `status: complete`
- ❌ A termbase with one rendering per sense and a citation per row
- ❌ A working mechanical consistency gate (the script exists but reads
  `concepts_in_verse:`, present in only **2 of 154** rail files → it silently passes)
- ❌ A sign-off record / human review queue

---

# PART 2 — The first step

## 2.0 Clear two blockers first (half a day, no translation work)

These are cheap, and every later step is wasted effort until they are done.

**Blocker 1 — one canonical workspace.**
You currently run two incompatible rulebooks: `4-SYSTEM/CLAUDE.md` (cite through
`2-RAILS/`) and `AI_translation/skills/requirements.md` §0 ("this workspace does
not read `2-RAILS/`"). Pick one. Recommended: `3-TRANSFORMATIONS/Translations/`
per the vault constitution; `AI_translation/` is frozen as
`0-INBOX/archive-AI_translation-v1/` and cited as prior art, not as a source.

**Blocker 2 — rail filenames.**
`4-SYSTEM/CLAUDE.md` §4, `translation-qa`, and `check_termbase_consistency.py`
all expect `2-RAILS/Verses/<verse-id>.md`. The files are
`<verse-id>-summary.md`. Rename the 154 files (cheap, git-tracked) rather than
patching three tools. Until this is done, every skill that follows the documented
path finds nothing and **silently falls back** instead of failing.

## 2.1 THE first real step — harvest the 838 གནད་ཚིག blocks

**Do not run a fresh LLM extraction over raw Tibetan.** You already have, for
chapters 1–4, a commentary-grounded term list with citations. Harvest it
mechanically; the LLM's job is only to *group senses*, not to *recall terms*.

```
4-SYSTEM/scripts/term-index/harvest_gnad_tshig.py
  → reads   2-RAILS/Verses/*.md   (all ## གནད་ཚིག blocks)
  → writes  2-RAILS/Term-Index/bo-term-index.raw.yaml
```

Each harvested record:

```yaml
- surface: "མི་གཙང་བའི་ལུས།"
  verse: "1-10"
  gloss_bo: "ད་ལྟའི་ལུས་འདི་ — རང་བཞིན་གྱིས་མི་གཙང་ཞིང་ལས་དང་ཉོན་མོངས་ཀྱིས་བསྒྲིབས་པ།"
  cite: "1-SOURCES/Commentaries/Transcluded/BCAC19_KS_bo.md#^1-10"
```

**Why this is the right first step**

1. It is the *only* term list in the project whose authority comes from the
   commentary tradition rather than from a model's priors — which is what
   `CLAUDE.md` §10 requires.
2. Every entry already carries a block ID, so the consistency gate (Phase F) can
   actually be wired up.
3. It costs ~0 tokens. It is a parser, not a prompt.
4. It gives you a measurable denominator: 838 records → *N* lemmas → *M* senses.
   You can then say "the termbase covers 94% of attested key terms," which today
   you cannot say about anything.

**Deliverable of step 1:** `2-RAILS/Term-Index/bo-term-index.raw.yaml` +
a coverage note (how many distinct surfaces, how many verses, which verses have
zero key terms — those are rail gaps to fill).

---

# PART 3 — The full pipeline

Seven phases. Phases A–B are done **once for the text**. Phase C is done **once
per language**. Phases D–G are done **per track** (language × audience).

This ordering is the whole point: the expensive, error-prone, doctrinally
sensitive work (what does this word *mean here*) happens once, in the source
language, cited. Only the cheap, register-dependent work (which English word)
repeats per track.

```
        ┌─────────────────────── done ONCE for the text ──────────────────────┐
A. Foundation ──► B. Term index (bo, sense-split)
        └─────────────────────────────────────────────────────────────────────┘
                          │
        ┌───────── ONCE per language ─────────┐
                 C. Attested-rendering glossary (bo→en, bo→hi …)
        └─────────────────────────────────────┘
                          │
        ┌──────────────── per TRACK (lang × audience) ───────────────────┐
        D. Termbase (one rendering per sense) ──► E. Generation
                  ──► F. Verification gates ──► G. Sign-off & release
        └────────────────────────────────────────────────────────────────┘
```

---

## PHASE A — Foundation

**Purpose:** make the ground truth addressable and the rails trustworthy.

### Files

| File / folder | Role | Why it must exist |
|---|---|---|
| `1-SOURCES/Translations/bo-བློ་ལྡན་ཤེས་རབ།.md` | the translation base | Every block ID in the project resolves here. Frozen. |
| `1-SOURCES/Text/BCAV08_SH_sk.md` | disambiguation | Resolves Tibetan homonyms and pāda breaks that the Tibetan alone cannot. |
| `1-SOURCES/Commentaries/Transcluded/*.md` | authority | The only non-LLM answer to "what does this verse mean". |
| `2-RAILS/Verses/<id>.md` | per-verse context package | The unit every downstream step cites. **Renamed from `<id>-summary.md`.** |
| `2-RAILS/Sections/<node>.md` | per-TOC-node summary | Gives the translator the argumentative arc; without it each verse is translated in isolation, which is a documented cause of terminology drift. |

### Actions

**A1. Rename rails.** `2-RAILS/Verses/<id>-summary.md` → `<id>.md`. One `git mv` loop.

**A2. Add `concepts_in_verse:` to every rail's frontmatter.** Populate it from
the rail's own `## གནད་ཚིག` block headings. This is what makes
`check_termbase_consistency.py` come alive — today it reads a field present in
2 of 154 files and therefore reports clean on a text with 797 known drifts.
*This single fix converts your existing dead script into a working gate.*

**A3. Fill the rail gaps in chapters 1–4.** 154 rails exist for 190 verses
(ch1 36/38, ch2 65/67, ch3 33/35, ch4 20/50). Use `verse-context-batch`.

**A4. Decide the rail promotion policy.** Right now **nothing** is
`status: complete`, so by `CLAUDE.md` §9 nothing may be generated from and
nothing may be published. Either (a) a domain specialist reviews and promotes
chapters 1–4, or (b) you formally amend the rule to allow generation from
`status: draft` rails with a recorded caveat. **Do not keep silently violating
it** — that is what makes every downstream QA result unfalsifiable.

**A5. Extend rails to chapters 5–10** (776 verses). This is the long pole.
Sequence by risk: **ch. 9 first** (highest terminological density), then 6, 8, 5, 7, 10.

### Gate out of Phase A
Every verse in scope has a rail; every rail has `concepts_in_verse:`;
`guard check` is clean; promotion policy is written down.

---

## PHASE B — Source-side term index (the fix)

**Purpose:** produce, once, a sense-split inventory of every load-bearing Tibetan
term, each sense defined from a commentary and cited. **Language-independent.**

### Files

```
2-RAILS/Term-Index/
  bo-term-index.raw.yaml     # machine harvest, no judgement (Step 1 output)
  bo-term-index.yaml         # MASTER — sense-split, curated, cited
  bo-term-index.md           # human-readable render of the master
  coverage.md               # what % of attested key terms is indexed; gaps
2-RAILS/Local-Wiki/
  <term>_(disambiguating-phrase).md   # one article per SENSE, not per term
```

### `bo-term-index.yaml` — the schema that fixes the 1:1 problem

```yaml
- lemma: ཆོས་
  wylie: chos
  category: philosophical      # philosophical | verb-epistemic | proper-noun | fixed-compound
  variants: [ཆོས།, ཆོས་ཀྱི་, ཆོས་རྣམས་, ཆོས་སུ་]   # surface forms for matching
  senses:
    - sense_id: chos.01
      label_bo: བསྟན་པའི་ཆོས།
      gloss_bo: "སངས་རྒྱས་ཀྱིས་གསུངས་པའི་བཀའ་དང་བསྟན་བཅོས།"
      cite: ["BCAC19_KKP_bo_segmented.md#^1-1"]
      attested_at: ["^1-1", "^1-2", "^2-4"]
      local_wiki: "2-RAILS/Local-Wiki/ཆོས་(teaching).md"
    - sense_id: chos.02
      label_bo: ཤེས་བྱའི་ཆོས།
      gloss_bo: "ཤེས་བྱ་སྤྱི་དང་གཟུང་བྱའི་དངོས་པོ།"
      cite: ["BCAC19_KS_bo.md#^9-2"]
      attested_at: ["^9-2", "^9-15"]
      local_wiki: "2-RAILS/Local-Wiki/ཆོས་(phenomenon).md"
```

**Every field has a reason:**

| Field | Reason it is not optional |
|---|---|
| `wylie` | ASCII join key. Tibetan Unicode has NFC/NFD and tsheg variance; scripts must not match on Uchen alone. |
| `variants` | The consistency checker matches surface strings. Without variants, ཆོས་ཀྱི་ never matches the lemma ཆོས་ and every occurrence lands in `UNTRACKED` — this is a large share of your current 1 285. |
| `sense_id` | **The key of the entire termbase.** It is what makes a one-rendering rule safe. `chos.01 → "teaching"` and `chos.02 → "phenomenon"` are both consistent *and* correct. A single row for ཆོས་ cannot be. |
| `gloss_bo` + `cite` | `CLAUDE.md` §10: no parametric knowledge. The sense boundary is drawn by a commentator, not by the model. |
| `attested_at` | Lets you (a) rank by frequency, (b) drive the per-verse gate, (c) audit any decision back to a verse. |
| `local_wiki` | The long-form evidence lives in the article; the index stays a table. |

### Actions

**B1.** Run the harvester (Part 2, step 1) → `bo-term-index.raw.yaml`.

**B2.** Lemma normalisation, **mechanical**: group surfaces by shared lemma,
strip case particles, emit candidate `variants`. Script, not LLM.

**B3.** Sense grouping, **LLM classification not recall**: hand the model, per
lemma, all of its harvested `gloss_bo` strings and ask *"how many distinct senses
are these, and which gloss belongs to which?"* This is the one step that must be
a model. It is safe because the model is choosing among given options rather
than remembering terms — the failure mode that produced `Derge edition` as a
keyword in v1.

**B4.** Write a Local-Wiki article per sense with ≥2 verbatim commentary
quotations (skill: `local-wiki-article`).

**B5.** Freeze. `bo-term-index.yaml` becomes read-only ground truth for all
languages and all audiences.

### The extraction prompt — corrected

Your draft prompt belongs **here**, at B3, not at the start, and with these changes:

- Row key = **(lemma, sense_id)**, never lemma alone.
- Add columns: `Sense ID`, `Attested at (block IDs)`, `Commentary gloss`, `Source citation`.
- **Delete** "Literal syllable-by-syllable meaning" — most BCA technical
  vocabulary is Sanskrit calque (དགེ་སློང་ = *bhikṣu*), and syllable
  decomposition manufactures confident false etymology.
- **Delete** the three "Proposed …Term" columns from this phase entirely.
  Renderings are Phase D, and must be *selected from attested witnesses*, not
  invented. Mixing them here is what re-imports parametric knowledge.
- Fixed chunk = **one chapter**, plus a mandatory merge-and-reconcile pass whose
  output lists every cross-chapter conflict. Without it you get 10 tables that
  disagree with each other.
- Input = the harvested `gloss_bo` list, not raw Tibetan text. Classification, not recall.

### Gate out of Phase B
`coverage.md` shows ≥95% of the 838 harvested key terms mapped to a `sense_id`;
every sense has ≥1 citation; no sense lacks a Local-Wiki article.

---

## PHASE C — Attested renderings, per language pair

**Purpose:** record, descriptively, *what human translators have actually done*
for each sense. Still no choices. **Once per language pair, all audiences share it.**

### Files

```
2-RAILS/Bilingual-Glossaries/
  Raw/bo-en-padmakara.md    # per-witness, already exists
  Raw/bo-en-wallace.md
  Raw/bo-en-choephel.md
  bo-en.md                  # consolidated: sense_id → [rendering, witness, freq]
  bo-hi.md
  bo-zh.md
```

### Change from today

`bo-en.md` currently keys on **lemma** (50 keywords, 239 renderings). Re-key it
on **`sense_id`**. Same data, correct granularity:

```markdown
## chos.01 — བསྟན་པའི་ཆོས། (teaching)

| Rendering | Witnesses | Freq | Attested at |
|---|---|---|---|
| Dharma | padmakara(31), wallace(18) | 49 | ^1-1, ^1-2, … |
| teaching | choephel(22) | 22 | ^1-1, ^2-4, … |
| doctrine | wallace(3) | 3 | ^9-40 |
```

**Why:** Phase D's rule is "prefer an attested rendering." Without sense keying,
"attested" is meaningless — *doctrine* is attested for ཆོས་, just not for the
sense in verse 1-1. This is precisely the softening/mistranslation class your
fact-check report keeps flagging.

**Skills:** `interlinear-gloss` → `glossary-extract-raw` → `glossary-combine`
(all exist; they need re-pointing at `sense_id`).

### Gate out of Phase C
Every `sense_id` in the term index has ≥1 attested rendering, or is explicitly
marked `attested: none` (Phase D must then derive one and say so).

---

## PHASE D — Termbase, per track

**Purpose:** make the choices. **This is the only place in the pipeline where
target-language vocabulary is decided.** One track = one language × one audience.

### Folder

```
3-TRANSFORMATIONS/Translations/en-plain/
  requirements.md      # style contract — CRITERIA ONLY, no specific renderings
  audience.md          # who is reading, prior knowledge, use case
  termbase.yaml        # MASTER vocabulary contract — one rendering per sense_id
  termbase.md          # human-readable render
  Chapters/            # generated output, one file per chapter
  BCA-Full-en-plain.md # merged
  reports/             # every QA / consistency / fact-check run, dated
  SIGNOFF.md           # who approved what, when
```

### `termbase.yaml`

```yaml
track: en-plain
language_pair: bo-en
audience: plain
term_index: 2-RAILS/Term-Index/bo-term-index.yaml
glossary: 2-RAILS/Bilingual-Glossaries/bo-en.md
status: draft
entries:
  - sense_id: chos.01
    rendering: "teaching"          # EXACTLY ONE. No "/". No parentheses.
    inflections: [teaching, teachings]   # allowed surface variation
    origin: attested               # attested | derived
    witness: choephel
    rationale: "requirements §4 bans transliteration; 'Dharma' excluded."
    first_attested: "^1-1"
  - sense_id: chos.02
    rendering: "thing"
    origin: derived
    rationale: "No witness rendering meets grade-8 reading level; derived from Local-Wiki ཆོས་(phenomenon)."
    first_attested: "^9-2"
```

### Hard rules

1. **One rendering per `sense_id`.** No `/`, no parenthetical alternatives, no
   "context-dependent". Today `en-ai/termbase.md` has a slash in nearly every
   row and `en-plain-english/termbase.md` has `The Truth / The Teaching` — those
   files are descriptions, not contracts, and cannot be enforced by any script.
2. **`inflections:` is separate from `rendering:`.** Morphology is not choice.
   This is what stops legitimate plurals landing in the drift report (your
   current run: 534 INFLECTION rows that a human had to eyeball).
3. **Attested before derived.** Derivations write back to `bo-en.md` with
   `freq: 0` so the glossary stays a complete record.
4. **`requirements.md` contains no renderings.** Today
   `en-plain-english/requirements.md` §6 says
   *Bodhisattva → "One who seeks Enlightenment / Hero of Enlightenment"* while
   `termbase.md` says *"Hero of Enlightenment"* — two contracts, no precedence
   rule. Requirements state *criteria* (reading level, no transliteration,
   sentence length); termbase states *words*. One fact, one place.
5. **Proper nouns need an explicit policy.** `requirements.md` §4 currently bans
   all transliteration, which is unworkable for ཀུན་ཏུ་བཟང་པོ་ / མཛོད་ / Maitreya.
   Decide: translate, transliterate, or transliterate-with-gloss-on-first-use.
6. **YAML is the master, markdown is a view.** 8-column markdown tables with
   hundreds of rows are un-diffable and un-mergeable — you already have four
   divergent copies of the English termbase because of this.

**Skill:** `glossary-select` (exists; re-point at `sense_id` + YAML).

### Gate out of Phase D
Zero `/` characters in any `rendering:` field. Every entry has `origin` +
`rationale` + `first_attested`. Every `sense_id` attested in the track's chapter
scope has an entry.

---

## PHASE E — Generation

**Purpose:** produce the translation with the contract already in context.

### The critical change

v1 translates, then repairs. v2 **supplies the termbase at generation time**, per
chapter, filtered to the senses attested in that chapter. Consistency becomes a
property of the input, not a defect to be found later.

### Per chapter

```
Inputs → 1-SOURCES/Translations/bo-བློ་ལྡན་ཤེས་རབ།.md   (chapter slice)
         1-SOURCES/Text/BCAV08_SH_sk.md                (same slice)
         2-RAILS/Sections/<node>.md                    (the argumentative arc)
         2-RAILS/Verses/<id>.md                        (per verse, complete only)
         3-TRANSFORMATIONS/Translations/en-plain/requirements.md
         3-TRANSFORMATIONS/Translations/en-plain/audience.md
         3-TRANSFORMATIONS/Translations/en-plain/termbase.yaml  ← filtered slice
Output → Chapters/Chapter-01.md
```

Output frontmatter records provenance — this is what makes a result reproducible:

```yaml
context_packages: ["2-RAILS/Verses/1-1.md", "2-RAILS/Verses/1-2.md", …]
termbase_version: <git sha>
rails_status_at_generation: draft   # honest record
status: draft
```

### Formatting / integrity rule (tightened)

Your current rule — *strip all whitespace, diff the character streams* — has a
hole that hits precisely this vault: **a block ID can migrate across a line
boundary into the neighbouring verse and the stripped stream is identical**,
silently rebinding every citation keyed to that verse. Add three assertions:

1. The ordered list of `^ids` is unchanged.
2. Each `^id` still terminates the same block, verified by per-block checksum.
3. Normalise to **NFC** before comparing, and state explicitly how tsheg `་`,
   shad `།`, CRLF, and non-breaking spaces are treated — otherwise the strip can
   mask a real edit.

**Skills:** `translate-zero-shot` (revise to require `termbase.yaml`),
`merge_chapters.py`, `lint_translation.py`.

---

## PHASE F — Verification (three independent gates)

Three gates because they catch disjoint error classes. Running only one gives
false confidence.

| Gate | Tool | Ground truth | Catches | Output |
|---|---|---|---|---|
| **F1 Consistency** | `check_termbase_consistency.py` | `termbase.yaml` + rail `concepts_in_verse:` | vocabulary drift, mechanically, over 930 verses | `reports/consistency-<date>.md` |
| **F2 Quality** | `translation-qa` (MQM) | rails + requirements + termbase | omission, addition, register violation, broken block IDs | `reports/qa-<date>.md` |
| **F3 Fact-check** | `commentary-fact-check` | **raw commentary** in `1-SOURCES/` | wrong referent, kāya/dharma swaps, wrong simile tenor, wrong enumeration | `reports/factcheck-<commentary>-<date>.md` |

### Fixes required to make these real

- **F1 is currently inert.** It reads `concepts_in_verse:`, present in 2 of 154
  rails. Phase A2 fixes this. Until then, a green F1 means nothing.
- **F3 must run against `1-SOURCES/Commentaries/`, not `2-RAILS/`.** Your current
  fact-check compares an LLM translation to an LLM rail synthesis — that is not
  verification. The `commentary-fact-check` skill already does this correctly;
  use it as written.
- **Scope must match what you ship.** Today F3 covers chapters 1–4 (16.6% of the
  text) while the termbase derived from it is applied to all 930 verses.
  Chapter 9 — the hardest chapter — is unverified. Either extend coverage or
  ship only what is verified.

### The re-translation trap

v1's order is fact-check → fix → standardize → **re-translate**. The file you
ship is the one that was never checked. **In v2, any regeneration re-enters
Phase F from the top.** Gates run on the artefact you release, never on its
ancestor. Keep dated reports so regressions between generations are visible.

### Gate out of Phase F
F1: zero UNAMBIGUOUS_DRIFT; every AMBIGUOUS_DRIFT resolved by a human decision
recorded in `SIGNOFF.md`. F2: zero Critical, zero Major. F3: zero ERROR;
every SOFTENING adjudicated.

---

## PHASE G — Sign-off and release

**Purpose:** make "done" a fact rather than a feeling.

`SIGNOFF.md` per track:

```yaml
track: en-plain
chapters_signed_off: [1, 2, 3]
signed_by: <domain specialist name>
date: 2026-08-20
gates:
  consistency: reports/consistency-2026-08-19.md   # PASS
  qa:          reports/qa-2026-08-19.md            # PASS
  factcheck:   reports/factcheck-BCAC14_NTS-2026-08-19.md  # PASS
open_decisions: 12   # ambiguous drifts awaiting adjudication
```

Only then does `status: complete` go on the chapter file. **The LLM never sets
it** (`CLAUDE.md` §7). Re-baseline the drift guard after each approved change:

```
python3 4-SYSTEM/scripts/day-package/day_package_tools.py guard record
```

---

# PART 4 — Where the current assets land

| Existing asset | Fate in v2 |
|---|---|
| 838 `གནད་ཚིག` blocks | **→ seed of Phase B.** Highest-value asset you have. |
| `tibetan-word-english-senses-plain.md` | **→ Phase B validation set.** It already has the right shape; use it to check the harvest. |
| `bo-en.md` (50 kw, 239 renderings) | → Phase C, re-keyed on `sense_id` |
| 6 Local-Wiki articles | → Phase B, split per sense; template for the rest |
| 3 English full texts (`en-translate/`) | → **regression corpus**, not the deliverable. Diff v2 output against them to see what changed and why. |
| `vocab-standardization-report.md` | → the **797 unambiguous drifts are a ready-made test set** for Phase F1. If v2's F1 doesn't reproduce them, F1 is broken. |
| `rails-fact-check-report-*.md` | → Phase F3 baseline for chapters 1–4 |
| 4 competing termbases | → archive all four; `termbase.yaml` per track is the only master |
| `Keyword_extractor/` | → retire. Superseded by the harvester. |
| Hindi / Marathi termbases | → rebuild at Phase C/D from the shared term index. The sense analysis is now shared, so hi and mr cost a fraction of en. |

---

# PART 5 — Order of work

| # | Task | Effort | Unblocks |
|---|---|---|---|
| 1 | Pick canonical workspace; archive `AI_translation/` | hours | everything |
| 2 | Rename `Verses/<id>-summary.md` → `<id>.md` | hours | 3 skills + 1 script |
| 3 | Add `concepts_in_verse:` to 154 rails | hours (scripted) | **F1 gate** |
| 4 | **Harvest 838 གནད་ཚིག → `bo-term-index.raw.yaml`** | hours | Phase B |
| 5 | Lemma normalisation + sense grouping → `bo-term-index.yaml` | days | Phases C, D |
| 6 | Local-Wiki article per sense | days | citation chain |
| 7 | Re-key `bo-en.md` on `sense_id` | days | Phase D |
| 8 | Build `en-plain/termbase.yaml`, zero slashes | days | Phase E |
| 9 | Regenerate chapters 1–4 with termbase in context | days | Phase F |
| 10 | Run F1/F2/F3; compare against the 797-drift baseline | days | proof the pipeline works |
| 11 | Rail coverage for chapters 5–10, ch. 9 first | weeks | full-text release |

Steps 1–4 are the ones to do now, and none of them requires an LLM.

---

# PART 6 — Open decisions for you

1. Canonical workspace: `3-TRANSFORMATIONS/` or `AI_translation/`?
2. Rail promotion: does a specialist promote chapters 1–4 to `complete`, or do
   we amend `CLAUDE.md` §9 to permit generation from `draft` with a recorded caveat?
3. Proper-noun policy: translate / transliterate / transliterate + gloss?
4. Release scope: ship chapters 1–4 verified, or hold everything until 1–10?
5. Do the three audience registers share one `sense_id` inventory (recommended)
   or diverge? Sharing is what makes children's and scholar editions doctrinally
   consistent with each other.

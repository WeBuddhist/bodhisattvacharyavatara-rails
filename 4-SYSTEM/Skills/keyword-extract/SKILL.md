---
name: keyword-extract
description: >
  The vocabulary-standardization pipeline. Extract candidate keywords from a
  block-aligned English translation, map every occurrence back to the source-language
  term it actually renders, group variants and synonyms under one canonical lemma per
  concept, count them quote-excluded across the whole corpus, score them, and emit a
  mechanically-gated, ranked article queue.

  Trigger on "extract the keywords", "what are the key terms here", "rank the
  terminology", "pull the domain vocabulary out of this translation", "TF-IDF the
  translation", "build the term registry", "standardise the vocabulary", "which
  subjects should get articles".

  Feeds glossary and termbase work, and `article-subject-filter`.
---

# Keyword extraction and vocabulary standardization

Six phases. Phase 1 is a statistical candidate scan; Phases 2–6 turn that scan into a
canonical, corpus-measured, mechanically-gated term list.

| Phase | Does | Output |
|---|---|---|
| 1 | Candidate keywords from a block-aligned English translation (two modes) | `0-INBOX/temp/keyword-extraction/<run>/verse-keywords.json` |
| 2 | Locate every occurrence of every candidate, by block ID | `0-INBOX/temp/keyword-extraction/<run>/occurrences.json` |
| 3 | Map each occurrence to its source-language term, regroup by term, attach variants/synonyms/epithets | **`2-RAILS/Keywords/source-term-registry.json`** |
| 4 | Quote-excluded frequency matrix across the root text and every commentary | **`2-RAILS/Keywords/frequency-matrix.json`** |
| 5 | Composite scoring (claim density, structural presence, frequency × spread) | `0-INBOX/temp/keyword-extraction/<run>/ranked-keywords.json` |
| 6 | Mechanical viability gate → the ranked queue `article-subject-filter` consumes | **`2-RAILS/Keywords/article-queue.json`** |

**Where output goes.** Working intermediates — one run's scratch — live under
`0-INBOX/temp/keyword-extraction/<run>/`, where `<run>` is a dated run name (`2026-09-22`, or
`<text-slug>-2026-09-22` when a vault holds more than one text). Finished artefacts —
the three files in bold above — are promoted to `2-RAILS/Keywords/`. Nothing in `2-RAILS/Keywords/` is
a citation-chain rail: these are descriptive inventories over the corpus, not claims, and
they carry no per-item `1-SOURCES/` citation. Never write them into `2-RAILS/Claims/` or
`2-RAILS/Local-Wiki/`.

**Why the source-side detour.** Phase 1 ranks against a **general-language** corpus, which
is the point: raw frequency just returns "the", "is", "one". What matters is the term that is
common *here* and rare in ordinary English. But English statistics measure the *translator's*
vocabulary: one source term splits across renderings (count divided, rank sinks) and two
source terms collapse into one English word (a merged count belonging to neither). Phase 3
fixes both by mapping **per occurrence** and then regrouping by source term. That regrouping
is the vocabulary-standardization step, and its artefact — the source-term registry — is what
every downstream consumer actually reads.

The full reasoning, the four known distortions, and the rationale for each gate constant are
in `4-SYSTEM/Skills/keyword-extract/references/keyword-extraction-methodology.md`. Read it before changing a
threshold or a weight.

---

## Dependencies

| Need | Required for | Notes |
|---|---|---|
| `yake`, `spacy` + the `en_core_web_sm` model | Phase 1 Mode 1 | `pip install -r 4-SYSTEM/Skills/keyword-extract/scripts/requirements.txt`, then `python -m spacy download en_core_web_sm` |
| the bundled IDF table `4-SYSTEM/Skills/keyword-extract/scripts/idf_corpus.py` | Phase 1 Mode 1, optional corpus-level TF-IDF | ~1.3 MB, general-English (Reuters-21578); ships with the skill, regenerable with `generate_idf_corpus.py` |
| Python 3 standard library | Phases 2, 4, 6 | no third-party packages, no keys |
| `google-genai` + `GEMINI_API_KEY` in the environment | **only** the optional batch enrichment route of Phase 3 | never hardcode the key |
| *(no key at all)* | the agent-native route of Phase 3 and all of Phase 5 | this is the default route; an agent does the mapping and the claim-density tagging directly |

Phases 2–6 have no scripts bundled: they are specified below as agent-executable phases with
a fixed input/output file contract, and a vault may add its own scripts for the mechanical
parts (Phases 2, 4 and 6 are fully mechanical once their inputs exist).

---

## Phase 1 — candidate keywords from a translation

| Mode | Source language | Method |
|---|---|---|
| 1 — English translation of a Tibetan text | Tibetan | YAKE + spaCy, optional TF-IDF against a general-English IDF corpus; each keyword enriched with its Tibetan term |
| 2 — English translation of a Pāli text | Pāli | TF-IDF against the Google-10k Zipf table; unigrams and compound phrases |

**Recall, not ranking.** Keep a generous pool (top ~100–200 corpus-wide). A wrong candidate
costs nothing — Phases 3 and 5 filter it. A missed candidate is gone for the rest of the
pipeline. Extend the stopword list with domain formula words as you notice them.

### Mode 1 — English keywords from a Tibetan text's translation

Keyword statistics behave badly on classical Tibetan directly: tokenization is contested and
no standard reference corpus exists. This mode routes around the problem by extracting
keywords from an **English translation** — where YAKE/TF-IDF are well-conditioned — and then
mapping each keyword back to the Tibetan term it renders, verse by verse (Phase 3).

If the corpus has no English translation yet, produce one first with `zeroshot-translate`
(block-ID-preserving), or use any existing published translation whose verses carry
`^chapter-verse` IDs. A deliberately literal translation serves this purpose better than a
published poetic one.

#### Step 1 — extract keywords per verse (deterministic)

```bash
python3 4-SYSTEM/Skills/keyword-extract/scripts/keywords.py \
    --input <en-translation>.md \
    --output 0-INBOX/temp/keyword-extraction/<run>/verse-keywords.json
```

`keywords.py` (YAKE + spaCy noun-phrase filtering) reads a block-ID'd English
translation and writes `{verse_id: {text, keywords: [{key, rank, score, count}]}}`.
Treat **each verse as one document** — that is what makes IDF punish words recurring in
every verse (similes' "like", a repeated homage formula).

#### Step 2 (optional) — corpus-level TF-IDF report

```bash
python3 4-SYSTEM/Skills/keyword-extract/scripts/generate_en_translation_idf.py
```

Ranks terms across the whole translation against the bundled general-English IDF table
(`4-SYSTEM/Skills/keyword-extract/scripts/idf_corpus.py`, regenerable with `4-SYSTEM/Skills/keyword-extract/scripts/generate_idf_corpus.py`).
Use this to pick the corpus-level top-N key terms rather than per-verse ones.

#### Step 3 — first-pass source-term enrichment

This is a *convenience* pre-pass for Phase 3, not a substitute for it: it attaches one source
term per keyword occurrence, which Phase 3 then regroups, filters and extends. Two routes;
prefer (a) in a Claude session:

**(a) No API — the agent does it directly.** For each verse's keywords, add a `"bo"` field
(or `"src"` for a non-Tibetan source) with the source-language term that the English keyword
*renders in that verse* — the contextually correct term, not a dictionary lookup. Consult the
aligned source verse (same `^chapter-verse` ID in the root text) to see which word the
translator was rendering. Write the enriched JSON into the same run folder with suffix
`-enriched.json`. Checkpoint every 50 verses. Report totals and gaps when done.

**(b) Batch via Gemini** (reads `GEMINI_API_KEY` from the environment, never hardcoded):

```bash
python3 4-SYSTEM/Skills/keyword-extract/scripts/enrich_en_bo_keyword_meaning.py \
    --input 0-INBOX/temp/keyword-extraction/<run>/verse-keywords.json
```

#### Output contract

```json
{
  "1-1": {
    "text": "English verse text",
    "keywords": [
      {"key": "bodhisattva", "rank": 1, "score": 0.001, "count": 2, "bo": "བྱང་ཆུབ་སེམས་དཔའ།"}
    ]
  }
}
```

- Verse keys are the root text's block IDs, in the scheme the file declares in
  `verse_id_format` — the same IDs every later phase and every alignment tool use.
- Every Tibetan `bo` value ends with a shad `།` (the vault term-list convention; for another
  source language, use that language's own citation form and state the convention in the
  vault annex).
- The source term must actually occur in the source verse (or be its standard citation form)
  — if uncertain, use the closest established term and note it in a `"note"` field rather
  than silently guessing.

### Mode 2 — English keywords from a Pāli text's translation

Runs **Pass 1 only** of the bilingual extraction pipeline: TF-IDF keyword selection on an
English translation file, with n-gram compound phrase detection.

Use this mode when you want the keyword list independently — for tuning, debugging, or
feeding into a separate co-occurrence step.

#### Inputs

| Input | Description | Path pattern |
|---|---|---|
| Target file | English translation markdown with block IDs | `3-TRANSFORMATIONS/Translations/<track>/<lang-tag>-<text>-<translator>.md` |
| Output path | Path for the keyword list | `0-INBOX/temp/keyword-extraction/<run>/<name>-keywords.md` |

#### Output

A ranked Markdown file — one keyword per line with its TF-IDF score — sorted descending:

```
# English keywords — <source filename>
# Method: block-level TF-IDF × Google-10k Zipf IDF; compound phrases via n-gram detection
# N blocks, K keywords selected

phenomena: 8.24
wholesome: 7.91
right concentration: 7.55
initial application: 7.43
contact: 6.88
feeling: 6.71
perception: 6.62
volition: 6.54
sustained application: 6.40
jhāna: 6.31
```

#### Procedure

**Step 1 — run keyword extraction**

```bash
python3 4-SYSTEM/Skills/pali-biterm-extraction/scripts/pali_biterm_extraction.py \
    <en_file> \
    0-INBOX/temp/keyword-extraction/<run>/<name>-keywords.md \
    --keywords-only
```

Optional flags:

| Flag | Default | Effect |
|---|---|---|
| `--top N` | 600 | Maximum keywords to output |
| `--max-phrase N` | 4 | Maximum phrase length in words |

**Step 2 — review**

Open the output file and check that:
- Core domain terms appear near the top (Abhidhamma example: `phenomena`, `wholesome`,
  `right concentration`)
- Compound phrases are correctly detected (`initial application`, `right mindfulness`)
- Common English words with low IDF are absent

### Phase 1 completion check

- [ ] Script ran without errors
- [ ] Output written under `0-INBOX/temp/keyword-extraction/<run>/`
- [ ] Core domain terms appear in the top 20
- [ ] Compound phrases detected for major multi-word terms
- [ ] Candidate pool is generous (~100–200 corpus-wide), not pre-pruned

---

## Phase 2 — locate every occurrence by block ID

Mechanical. For **each** candidate keyword from Phase 1, record every block ID of the English
translation in which it occurs, by plain case-folded string search (and for multi-word
candidates, whitespace-normalised search). Do not deduplicate by verse: a keyword occurring
twice in one block is two occurrences, because Phase 3 maps *per occurrence* and the two may
render different source terms.

### Output — `0-INBOX/temp/keyword-extraction/<run>/occurrences.json`

```json
{
  "wisdom": [
    {"block_id": "1-4", "n": 1, "surface": "wisdom"},
    {"block_id": "1-21", "n": 1, "surface": "wisdom"}
  ],
  "autumn moon": [
    {"block_id": "1-2", "n": 1, "surface": "autumn moon"}
  ]
}
```

- `block_id` — without the caret, in the translation's own `verse_id_format` scheme.
- `n` — the 1-based index of this occurrence within that block.
- `surface` — the exact matched string, so an inflected or hyphenated match is visible.

### Rules

1. **Every candidate gets an entry**, even one with zero occurrences (write `[]`) — a
   candidate that silently disappears here is indistinguishable from one that was never
   generated.
2. **Search the translation only.** Commentary counting happens in Phase 4, on the source
   side, and is a different measurement.
3. **Block IDs are copied, never derived.** Read them from the file; do not compute a verse
   number from position.

---

## Phase 3 — build the source-term registry (the vocabulary-standardization step)

This is the phase the whole pipeline exists for, and the only one that requires real
judgment per occurrence.

### 3a — map each occurrence to its source term

For each occurrence in `occurrences.json`, open the **same-numbered source block** and
identify the span that the English word translates. Record that span as the occurrence's
source term. Worked example:

```
"autumn moon" in ^2  → སྟོན་ཀའི་ཟླ་བ་
"wisdom"      in ^4  → ཡེ་ཤེས་
"wisdom"      in ^21 → ཤེས་རབ་   ← same English word, different source term  (SPLIT)
"gnosis"      in ^15 → ཡེ་ཤེས་   ← different English word, same source term  (MERGE)
```

- **Splitting** one English word that renders two different source terms into two registry
  rows, and **merging** two English words that render one source term into one row, are both
  mandatory. They are the two distortions this phase exists to remove.
- Consult the interlinear gloss (`interlinear-gloss`) where one exists; it does exactly this
  pairing and is the cheaper ground truth.
- Fan out: one isolated agent per slice of the occurrence list. Slices are independent.

### 3b — regroup by source term, and filter

- **Particle filter.** Drop any candidate that resolves to a grammatical particle or function
  word. Filter against the language's function-word list *first*, before any statistics
  (Tibetan examples: ལྟ་བུ་, བཞིན་). A particle is frequent everywhere and defined nowhere;
  leaving it in poisons Phase 5C and wastes Phase 5A's budget.
- **Root-text prior.** Every content word of the root text enters the registry regardless of
  what the English statistics said about it. The root text is the subject of the corpus; a
  term it uses is a term the corpus is about, whether or not the translator's English made it
  statistically salient.
- **Orthographic-variant merging, here and not later.** Apply a
  whitespace/word-separator-insensitive comparison plus any script-specific equivalences
  (Tibetan: the Sanskrit anusvāra marks U+0F83 ↔ U+0F7E) *before* writing the registry. Doing
  this as a late pass after scoring means two rows of the same term each carry half the
  evidence.

### 3c — attach variants, synonyms and epithets

For each registry row, collect:

- **variants** — spelling and orthographic forms attested in the corpus;
- **synonyms** — attested in Local-Wiki sense articles (`2-RAILS/Local-Wiki/`), the bilingual
  glossaries (`2-RAILS/Bilingual-Glossaries/`), and the claims themselves;
- **epithets** — fixed descriptive names the corpus uses for the same referent.

All three are **attested only** — never supplied from general knowledge of the tradition.
Each carries the path or claim ID where it was attested.

### Output — `2-RAILS/Keywords/source-term-registry.json`

The vocabulary-standardization artefact: **one canonical source lemma per concept, with every
attested variant grouped under it.**

```json
{
  "schema": "source-term-registry/1",
  "lang_tag": "bo",
  "run": "<run>",
  "date": "<YYYY-MM-DD>",
  "terms": [
    {
      "id": "ye-shes",
      "lemma": "ཡེ་ཤེས་",
      "variants": ["ཡེ་ཤེས", "ཡེ་ཤེས་ཀྱི་"],
      "synonyms": [{"form": "མཁྱེན་པ་", "attested_at": "2-RAILS/Local-Wiki/ye-shes_(pristine-awareness).md"}],
      "epithets": [],
      "english_renderings": ["wisdom", "gnosis", "pristine awareness"],
      "root_text_prior": true,
      "occurrences": [{"block_id": "1-4", "english": "wisdom"}, {"block_id": "1-15", "english": "gnosis"}],
      "dropped": false
    },
    {
      "id": "lta-bu",
      "lemma": "ལྟ་བུ་",
      "dropped": true,
      "drop_reason": "grammatical particle (comparison marker)"
    }
  ]
}
```

- `id` — a stable lowercase-hyphenated slug; **never renumbered** on a re-run.
- `dropped: true` rows are **kept, not deleted** — the reason is the audit trail that lets a
  later reviewer see the particle filter worked rather than guess that the term was missed.
- `english_renderings` is the merge evidence; `occurrences` is the split evidence.

### Rules

1. **Per occurrence, never per word.** A decision made once for "wisdom" corpus-wide is the
   error this phase exists to prevent.
2. **Attested only.** Variants, synonyms and epithets come from the corpus and the vault's own
   rails — never from the model's knowledge of the tradition.
3. **Nothing is silently dropped.** Every candidate from Phase 1 appears in the registry,
   either as a term or as a `dropped` row with a reason.
4. **Slugs are stable.** Re-running the pipeline never renumbers or re-slugs an existing term.

---

## Phase 4 — quote-excluded frequency matrix

Mechanical, once the registry exists. For each registry term — **including its variants and
synonyms** — count occurrences by plain string matching across the root text and each
commentary.

**The commentary count is over the commentary's own prose only.** Root-text quotations and
transclusions are excluded:

- where the ingest pipeline's transclusion/quote tagging exists, use it;
- where it does not, substitute a similarity-based quote detector (e.g. Python's `difflib` at
  a ≥0.8 ratio against the actual root-text lines) — same purpose, different mechanism, and
  state in the output which mechanism was used.

Without this exclusion, a commentary that quotes the root verse and then comments on a single
word of it inflates every word of that verse equally.

### Output — `2-RAILS/Keywords/frequency-matrix.json`

```json
{
  "schema": "frequency-matrix/1",
  "run": "<run>",
  "quote_exclusion": "transclusion-tags | difflib-0.8",
  "commentaries": ["<registered-id-1>", "<registered-id-2>"],
  "rows": [
    {
      "term_id": "ye-shes",
      "root": 3,
      "by_commentary": {"<registered-id-1>": 41, "<registered-id-2>": 0},
      "total": 44,
      "spread": 1
    }
  ]
}
```

- `spread` — how many commentaries use the term **at all** (count of non-zero columns).
- `commentaries` fixes the column order, so `spread` and the Phase 6 gate are reproducible.

---

## Phase 5 — composite scoring: attention beats presence

Three signal classes, in this order of weight. Only A and B can separate a high-frequency
particle from a major doctrinal term; C is a tie-breaker and never the arbiter.

| Class | Signal | Computed from |
|---|---|---|
| **A. Attention** (dominant) | claim density: how many claims are *about* the term, and across how many commentaries | `2-RAILS/Claims/raw/tree-guided/<id>.md` |
| **B. Structure** | the term appears in TOC-tree node titles; commentaries explicitly define it | `2-RAILS/Sections/Raw/toc-tree/`, `2-RAILS/Local-Wiki/`, term-definition tables |
| **C. Presence** | quote-excluded frequency × spread | Phase 4 matrix |

**Signal A is a model judgment, fanned out one agent per commentary.** Give each agent one
commentary's raw claims file and the registry, and ask it to tag every claim with the registry
terms it is *about* — the claim's subject matter, not the strings it happens to contain, so a
claim discussing a term entirely in paraphrase still counts. Record per term: total claims and
how many distinct commentaries contributed one.

**Signal B is mechanical:** string-match each term (and its variants) against every TOC-tree
node title, and against the headword of every Local-Wiki article and term-definition row.

**Combining.** Min-max normalize each signal across the term list, where each signal is itself
the average of a count-subcomponent and a spread-subcomponent, then weight. A 0.6 / B 0.25 /
C 0.15 is a working first pass; weights are tunable per corpus under human review, and the
weights actually used are recorded in the output.

### Output — `0-INBOX/temp/keyword-extraction/<run>/ranked-keywords.json`

```json
{
  "schema": "ranked-keywords/1",
  "weights": {"A": 0.6, "B": 0.25, "C": 0.15},
  "rows": [
    {
      "term_id": "ye-shes",
      "signal_a": {"claims": 87, "commentary_spread": 11, "norm": 0.93},
      "signal_b": {"toc_titles": 4, "definitions": 6, "norm": 0.71},
      "signal_c": {"frequency": 44, "spread": 1, "norm": 0.22},
      "composite": 0.77,
      "rank": 3
    }
  ]
}
```

---

## Phase 6 — the mechanical viability gate → article queue

**The cutoff is mechanical, not judgmental.** A term enters the article queue **iff** both
hold:

- **spread ≥ ⌈number of commentaries / 2⌉** — at least half the corpus's commentaries have
  claims substantively about the term (spread here is Signal A's `commentary_spread`, not
  Phase 4's string spread). This anchors the queue in majority attention — an article needs
  due-weight structure across multiple independent secondary sources — and scales
  automatically to any corpus size.
- **claim count ≥ 20** (Signal A's raw corpus-wide total). The article-material floor.
  Claims-only drafting means the drafter has nothing but claims, and consolidation collapses
  many raw claims into one cited statement, so the raw count must substantially exceed the
  article's final cited-statement count. **This constant is calibrated once and frozen** — the
  value of the rule is reproducibility, not the number. Changing it is a human decision
  recorded in the vault annex, never a per-run adjustment.

**Selection is by the gate; ordering within the queue is by composite score.** Terms failing
the gate are **not deleted** — they stay in the registry as Local-Wiki and glossary
candidates, per the boundary rule (methodology §1: keywords select and order publication,
they never define the consolidation topic space).

### Output — `2-RAILS/Keywords/article-queue.json`

The file `article-subject-filter` consumes.

```json
{
  "schema": "article-queue/1",
  "run": "<run>",
  "date": "<YYYY-MM-DD>",
  "gate": {"spread_min": 8, "claim_min": 20, "commentaries": 16},
  "queue": [
    {
      "rank": 1,
      "term_id": "ye-shes",
      "lemma": "ཡེ་ཤེས་",
      "variants": ["ཡེ་ཤེས", "ཡེ་ཤེས་ཀྱི་"],
      "english_renderings": ["wisdom", "gnosis"],
      "claims": 87,
      "spread": 11,
      "composite": 0.77
    }
  ],
  "gate_failures": [
    {"term_id": "<id>", "claims": 18, "spread": 9, "reason": "claim count below floor"}
  ]
}
```

`gate_failures` is required, not optional: it is the audit trail that lets the end-of-pipeline
human review see what the gate excluded and why, without rerunning anything.

### Rules

1. **Never choose N by feel.** The queue length is whatever the two constants produce.
2. **Never tune a constant to get a queue you like.** Both are frozen; a change is a recorded
   human decision.
3. **Failures are recorded, not dropped.** A term absent from both `queue` and
   `gate_failures` is a bug.
4. **`2-RAILS/Keywords/` artefacts are overwritten by a re-run, never appended to** — but term slugs
   are stable across runs (Phase 3 Rule 4), so a diff between two runs is meaningful.

---

## Completion check (whole pipeline)

- [ ] Phase 1 candidate pool generous, written under `0-INBOX/temp/keyword-extraction/<run>/`
- [ ] Phase 2 `occurrences.json` has an entry for every candidate, including empty ones
- [ ] Phase 3 mapped **per occurrence**; splits and merges both actually occurred where the
      corpus warrants them
- [ ] Particle filter applied before statistics; root-text prior applied; orthographic
      variants merged before the registry was written
- [ ] `2-RAILS/Keywords/source-term-registry.json` written — one canonical lemma per concept, every
      variant grouped under it, every dropped candidate carrying a reason
- [ ] `2-RAILS/Keywords/frequency-matrix.json` written, quote-excluded, mechanism named
- [ ] Phase 5 Signal A run one isolated agent per commentary; weights recorded
- [ ] `2-RAILS/Keywords/article-queue.json` written with both `queue` and `gate_failures`
- [ ] No file under `1-SOURCES/` or `2-RAILS/Claims/` was modified

---

## After this skill

`article-subject-filter` reads `2-RAILS/Keywords/article-queue.json` and classifies each term as a
standalone subject, section material, or glossary-only. `wiki-article-inventory` then checks
each standalone subject against the target Wikipedia.

`bilingual-glossary` Phase 1 turns the registry plus its English renderings into a raw
per-source glossary. For Pāli, `pali-biterm-extraction` goes further, building the full
morphological family for each term.

---

## Provenance

Phase 1 Mode 1's scripts (`keywords.py`, `generate_en_translation_idf.py`,
`generate_idf_corpus.py`, `enrich_en_bo_keyword_meaning.py`, `idf_corpus.py`,
`requirements.txt`) come from a Tibetan rails vault's `english_keyword/` script set and are
carried here verbatim; per-corpus `output/` runs were not carried over. Phase 1 Mode 2 comes
from a Pāli rails vault's keyword-extraction skill. Phases 2–6 are the methodology in
`4-SYSTEM/Skills/keyword-extract/references/keyword-extraction-methodology.md`, written up here as executable phases;
in the pilot corpus they were run ad hoc with parallel subagents for the semantic phases
(Phase 3 mapping, Phase 5 Signal A) and deterministic scripts for the mechanical ones.

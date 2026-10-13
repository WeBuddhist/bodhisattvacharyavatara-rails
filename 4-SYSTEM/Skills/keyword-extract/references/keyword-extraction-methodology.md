# Keyword-extraction methodology — selecting article subjects from the root text

The method the `keyword-extract` skill implements, recorded so that the reasoning behind
each phase survives independently of any one run.

**Companion:** `$SKILLS/claims-consolidate/references/claims-methodology.md` (extraction +
question-driven consolidation — governs the topic space).

Throughout, *N* is the number of commentaries in the corpus. Figures from a pilot run are
labelled as examples; only the two gate constants in §3 Phase 6 are thresholds.

---

## 1. Purpose and scope

Rank the terms of the root text and its commentary corpus by importance, to decide **which
subjects get generated articles and in what order**. Articles are generated from consolidated
claims pages (`$CLAIMS/<topic>.md`), citation chain intact.

Boundary rule: **keywords select and order publication; they never define the consolidation
topic space.** Consolidation coverage comes from the spine grid + claim-derived questions
(claims-methodology §4). A keyword list must not narrow what gets consolidated — otherwise
claims answering unasked questions silently vanish. The reverse check is a finding: a
high-keyness term with no claims bucket means either extraction missed something or the term
is root-text poetic vocabulary better served by Local-Wiki/glossary than a claims article.

---

## 2. Core design: detect in English, measure in the source language

Several classical languages (Tibetan among them) have no word boundaries a tokenizer can use,
so statistical keyword tools cannot run on them directly without a segmenter. The workaround:

- **English side (Phases 1–2):** tokenization and candidate detection are free in English.
  TF-IDF/YAKE on a block-aligned English translation discovers *what the candidate terms
  are*. English scores are recall-oriented candidate generation only — never the ranking.
- **Mapping (Phase 3):** block alignment converts English candidates into a **source-term
  registry** — the term list that seemed to be missing is created by this phase.
- **Source side (Phases 4–5):** counting a *known* string needs no segmentation (plain string
  matching); all measuring and ranking happens on the source side, where the truth lives.

Why not score in English: statistics on a translation measure the translator's vocabulary.
One source term splits across renderings (Tibetan example: ཡེ་ཤེས་ → "wisdom" / "gnosis" /
"pristine awareness" — count divided, rank sinks) and different terms collapse into one
English word ("wisdom" ← ཤེས་རབ་ and ཡེ་ཤེས་ — merged count belonging to no single term).
Mapping **per occurrence**, then regrouping by source term, fixes both. This is the
vocabulary-standardization step: one canonical source lemma per concept, with every attested
variant grouped under it.

A deliberately literal generated translation serves this purpose better than a published
poetic one — free translations paraphrase, and a keyword absent in English ≠ absent in the
source.

---

## 3. The pipeline

```
English translation ──YAKE/TF-IDF──▶ English candidates ──block alignment──▶ source-term
registry ──quote-excluded counts──▶ frequency matrix ──composite scoring──▶ ranked keywords
──mechanical viability gate──▶ article queue
```

### Phase 0 — Inputs (all existing vault artifacts)

- Root text in the source language, with block IDs (`$SOURCE_TEXTS/`)
- A block-aligned English translation (its `^2` translates source `^2`)
- The segmented commentaries, with root-text quotes transcluded or otherwise tagged
- Claims files (`$CLAIMS/raw/tree-guided/`), TOC trees (`$SECTIONS_RAW/toc-tree/`),
  Local-Wiki articles, bilingual glossaries

### Phase 1 — English candidate extraction (recall, not ranking)

Run TF-IDF and YAKE over the English translation, treating **each verse as one document**
(this makes IDF punish words that recur in every verse — similes' "like", a repeated homage
formula). Keep a generous pool (top ~100–200). A wrong candidate costs nothing (filtered in
Phases 3/5); a missed candidate is gone forever. Extend the stopword list with domain formula
words as they are noticed.

### Phase 2 — Locate occurrences (English side)

Plain string search: for each candidate, record the block IDs where it occurs
(`"autumn moon" → ^2`; `"wisdom" → ^4, ^21`).

### Phase 3 — Map each occurrence to its source term; build the registry

For each occurrence, open the same-numbered source block and identify the span the English
word translates (the `interlinear-gloss` rails do this pairing). Mapping is **per
occurrence**, which is what resolves both distortions:

```
"autumn moon" in ^2  → སྟོན་ཀའི་ཟླ་བ་
"wisdom"      in ^4  → ཡེ་ཤེས་
"wisdom"      in ^21 → ཤེས་རབ་   ← same English word, different source term (split)
"gnosis"      in ^15 → ཡེ་ཤེས་   ← different English word, same source term (merge)
```

Regroup **by source term**. Drop candidates that resolve to grammatical particles (Tibetan
examples: ལྟ་བུ་, བཞིན་…) — first filter against function words. Add to each term's row:
spelling variants, attested synonyms (from Local-Wiki sense articles, bilingual glossaries,
and the claims themselves), and epithet forms. The result is the **source-term registry** —
the keyword list plus its variant/synonym sets.

Root-text prior: every content word of the root text enters the registry regardless of
English statistics.

Orthographic-variant merging belongs here, not in a late pass: apply a
whitespace/word-separator-insensitive comparison plus any script-specific equivalences (for
Tibetan, the Sanskrit anusvāra marks U+0F83 ↔ U+0F7E) before the registry is written.

### Phase 4 — Count on the source side (presence signal)

For each registry term (including its variants/synonyms), count occurrences by plain string
matching across the root text and each commentary — **in the commentary's own prose only,
excluding root-text quotes and transclusions**. Where the ingest pipeline's transclusion/quote
tagging exists, that is the mechanism; where it does not, substitute a similarity-based quote
detector (e.g. `difflib` at ≥0.8 ratio against the actual root-text lines) — same purpose,
different mechanism. Output: a frequency matrix — rows = terms, columns = root + each
commentary, plus a spread column (how many commentaries use the term at all).

### Phase 5 — Composite scoring: attention beats presence

Three signal classes, in order of weight:

| Class | Signal | Source | Robust against |
|---|---|---|---|
| **A. Attention** (dominant) | claim density: how many claims are *about* the term, and across how many commentaries | `$CLAIMS/raw/tree-guided/` | paraphrase, synonyms, quotation inflation — extraction was semantic, per TOC node |
| **B. Structure** | term appears in TOC-tree node titles; commentaries explicitly define it | `$SECTIONS_RAW/toc-tree/`, `$LOCAL_WIKI/`, term-definition tables | function words (present everywhere, defined nowhere) |
| **C. Presence** (weakest — sanity check / tie-breaker) | quote-excluded frequency × spread | Phase 4 matrix | — (this is the signal the distortions attack; never the arbiter) |

Rationale: raw frequency + spread alone cannot separate a high-frequency particle from a
major doctrinal term — both are frequent and widespread. Only attention signals separate
them: no commentary defines the particle, no TOC node is titled by it, no claim is about it.
Weights are tunable per corpus under human review; a first pass of A 0.6 / B 0.25 / C 0.15
(min-max normalized per signal, each signal itself an average of a count- and a
spread-subcomponent) has been used successfully.

Pilot confirmation of the design: before signals A/B were folded in, raw presence ranking put
Tibetan intensifier particles (རབ་ཏུ་, ཤིན་ཏུ་, ཉིད, མ་ལུས) in the top 20 — exactly the §4.1
distortion. None survived into the final top 60, and the formula word ཕྱག་འཚལ་ ("homage", in
every stanza) landed at rank 17 rather than rank 1.

### Phase 6 — Mechanical viability gate → article queue

**The cutoff is mechanical, not judgmental.** N is never chosen by feel or per-run taste; a
term enters the article queue iff the corpus demonstrably contains enough claim-attention to
support a cited article about it:

- **spread ≥ ⌈number of commentaries / 2⌉** — at least half the corpus's commentaries have
  claims substantively about the term. Anchors the queue in majority attention (an article
  needs due-weight structure across multiple independent secondary sources), and scales
  automatically to any corpus size.
- **claim count ≥ 20** (raw, corpus-wide) — the article-material floor. Claims-only drafting
  means the drafter has nothing but claims; consolidation collapses many raw claims into one
  cited statement (many commentaries saying the same thing → one consensus sentence), so raw
  count must substantially exceed the final article's cited-statement count. 20 raw claims ≈ a
  lead plus two-to-three cited sections after shrinkage. This constant is *calibrated once and
  frozen* — the value of the rule is reproducibility. (Pilot sensitivity analysis: M=15 → 139
  terms, M=20 → 114, M=30 → 63; spread ≥ 8 vs ≥ 2 changes the count by under 6% at these M.)

Selection is by the gate; *ordering* within the queue is by composite score. Terms failing the
gate are not deleted — they remain in the registry as Local-Wiki/glossary candidates per the
boundary rule (§1).

**Where human review sits.** There is no human review between the gate and the downstream
stages. The subject filter, the existing-article inventory and article drafting run without
intermediate gates; the single human review happens **at the end, over the finished
articles**, before anything is published. Consequence: every judgment step must leave a full
audit trail (per-term verdicts with reasons, merge mappings, citations) so the end review can
reject selectively instead of rerunning the pipeline.

### Phase 7 — Subject filter and merge (article-worthiness)

The gate answers "is there enough claim material?"; this phase answers "is this an
encyclopedic *subject*?" The `article-subject-filter` skill classifies every queue term three
ways, with a one-line reason per verdict — never a silent drop:

1. **Standalone subject** — gets its own article.
2. **Section material** — not a subject (body parts, directions, and the like); its claims are
   routed to a named target article's section.
3. **Glossary/Local-Wiki only** — stays in the registry per the boundary rule (§1).

The same pass performs **subject-normalization**: near-duplicate rows that string-level
variant merging cannot catch (Tibetan examples: དགྲ/དགྲ་བོ/དགྲ་ཡི; ཕྱག་འཚལ/ཕྱག་འཚལ་བ;
ཧཱུྃ/ཡི་གེ་ཧཱུཾ) merge into one subject with pooled claims. Output is a new file alongside the
queue; all prior phase outputs are preserved unchanged.

### Phase 8 — Existing-article inventory

For each standalone subject, `wiki-article-inventory` determines whether an article already
exists on the target Wikipedia, via **two mechanisms**: (a) MediaWiki API search using the
term *plus its registry variant/synonym set*; (b) **Wikidata QID resolution** — find the
subject's item and check its sitelink for the target language, catching articles under
unguessable titles. Saved per term: exists y/n, title, URL, QID, length, section list,
stub-or-substantial judgment, and a dated wikitext snapshot. The snapshot is planning context
only — at generation time the live article is re-fetched. Editorial rule: one subject = one
article — existing articles are **updated/appended with cited sections**, never forked into
"X (according to these commentaries)" pages.

---

## 4. Known distortions and their mitigations

### 4.1 English function/formula words

High raw frequency in both root and commentaries. Three nets, in order: (1) verse-as-document
IDF + stoplists (Phase 1); (2) mapping filter — candidates resolving to grammatical particles
are dropped (Phase 3); (3) decisive: attention signals (Phase 5 A/B) — function words are
*present* everywhere but *receive attention* nowhere.

### 4.2 Quotation inflation

Two shapes: the commentary quotes the verse then comments on only one word of it; or quotes
the verse (keyword included) but comments on the whole verse, not the word. Both inflate every
quoted word's count. Mitigation: Phase 4 counts commentary **prose only** — quotes and
transclusions are excluded mechanically; and Phase 5A measures what passages are *about*, not
which words they contain.

### 4.3 Paraphrase (concept discussed, word absent)

String counting undercounts by design and cannot be patched at the string level. Covered
because the tree-guided claims extraction read those passages with a model: a claim about a
term phrased entirely in paraphrase still registers as attention to that term.

### 4.4 Synonyms (commentary uses a synonym for the root's keyword)

Partially fixed at the string level — attested synonym sets from Local-Wiki/glossaries are
counted into the term's row (Phase 3) — and fully covered at the attention level (Phase 5A),
which is surface-form-independent.

---

## 5. Open questions

- Reference corpus for proper cross-corpus keyness (matters more for larger corpora; for a
  small corpus the commentary-spread signal substitutes).
- Document unit for TF-IDF when English translations of the commentaries do not exist
  (current answer: verse-as-document over the root translation only; commentary evidence
  enters via signals A–C, not via English statistics).
- Composite-score weights — tune per corpus, human-reviewed.

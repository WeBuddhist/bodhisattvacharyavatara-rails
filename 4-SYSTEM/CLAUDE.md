# CLAUDE.md — 🛤️ Railroads

Persistent instructions for the LLM working in this repo. Read in full before touching any file.

---

## 1. What this is

**Railroads** is a method for making AI-assisted work on classical Buddhist texts reliable. Instead of feeding a model raw commentary and hoping it synthesises correctly, we lay the **rails** first: structured, machine-readable context packages that resolve every ambiguity in a passage and cite the human source for each decision. Once the rails are laid, any model can run any transformation — translation, adaptation, lesson plan — without redoing the philological work.

Authority comes from the human commentary tradition, never from the LLM's parametric knowledge. **One vault per text.** This vault is for the *Bodhisattvacaryāvatāra*.

---

## 2. Folder structure

```
0-INBOX/            # drafts and scratch — not authoritative
1-SOURCES/          # human-produced material — read-only ground truth
   Text/
   Commentaries/
   Translations/
   References/      # dictionaries, secondary literature
2-RAILS/            # the rails — structured interpretive context (LLM writes here)
   Verses/
   Sections/
   Local-Wiki/
   Glossaries/
3-TRANSFORMATIONS/  # translations, adaptations, lessons generated from rails
4-SYSTEM/           # guidelines (this file) — read-only for LLM
```

### Citation chain — never skip a link

```
1-SOURCES/  →  2-RAILS/  →  3-TRANSFORMATIONS/
```

`3-TRANSFORMATIONS/` cites `2-RAILS/` only. `2-RAILS/` cites `1-SOURCES/` only. If a claim cannot be cited, do not make it — leave the field blank and mark `status: draft`.

### Write permissions

| Folder | LLM may write? |
|---|---|
| `0-INBOX/` | yes — scratch only |
| `1-SOURCES/` | **no** — read only |
| `2-RAILS/` | yes — primary work area |
| `3-TRANSFORMATIONS/` | yes, only when explicitly instructed |
| `4-SYSTEM/` | **no** — read only |

---

## 3. File naming

- Lowercase, hyphenated, no diacritics in filenames. Diacritics fine inside file content.
- Language tag suffix on every file carrying language-specific material: `-sk` Sanskrit (IAST default), `-pi` Pāli, `-bo` Tibetan, `-zh` Chinese, `-en` English. Add script suffix when needed: `-sk-iast`, `-bo-wy`.
- Verse package files in `2-RAILS/Verses/` are named by block ID without the caret: `1-1.md`, `6-33.md`. Pre-chapter content is chapter 0: `0-1.md`.
- Section files in `2-RAILS/Sections/` are named by chapter number: `1.md`, `6.md`.

---

## 4. Block IDs — the verse-level link

Every verse ends with an Obsidian block ID. This is the only verse-level linking mechanism.

```
sugatān sagaṇān natvā dharmakāyādigocaran |
bodhisattvapadaprāptiṃ vakṣyāmi śāstrasaṅgraham || ^1-1
```

- Format `^chapter-verse`. No zero-padding (`^6-33`, not `^06-033`).
- Verse numbers restart at 1 each chapter.
- Pre-chapter content (homage, colophons, title lines) goes under `## 0. Introduction` with IDs `^0-1`, `^0-2`, etc.
- Chapter heading: `##`. Author-defined sub-sections: `###`. No `####`.

Link form: `[[1-SOURCES/Text/sk-iast-root-text.md#^1-1]]`
Transclude: `![[1-SOURCES/Text/sk-iast-root-text.md#^1-1]]`

---

## 5. 1-SOURCES rules

Files here are received material — formatted for navigation but never interpreted. Permitted additions only:

- Block IDs
- Frontmatter metadata
- Internal navigation links
- Editorial notes marked `[Ed: ...]` (English, factual only)

Any interpretive claim — compound analysis, sense choice, syntactic reading — belongs in `2-RAILS/`, not here.

### Minimum frontmatter

```yaml
---
title: 
author: 
language: 
file_type: root-text | commentary | translation | reference
lang_tag: 
source_description: "where this text came from"
---
```

Add external IDs when available: `bdrc_work_id`, `cbeta_id`, `gretil_url`, `dsbc_url`, `suttacentral_id`, `acip_id`.

For commentaries and translations, also include `root_text:` (path) and `covers_verses:` (range, e.g. `1-1–10-58`).

---

## 6. 2-RAILS — verse package format

One file per verse: `2-RAILS/Verses/1-1.md`. Each package resolves the verse's ambiguities and cites the commentary that grounds each decision.

### Frontmatter

```yaml
---
ref: 1-1
unit_type: single | group        # group = syntactically incomplete alone
unit_verses: [1-1]               # list, multiple if group
commentary_coverage: [prajnakaramati, kunzang-pelden]
status: draft | partial | complete
---
```

Only `complete` packages are used to generate transformations. Domain specialists set `complete`.

### Body

```markdown
## Source Text
![[1-SOURCES/Text/sk-iast-root-text.md#^1-1]]

## Traditional Interpretation

### prajnakaramati — Bodhicaryāvatārapañjikā (Sanskrit, 11th c.)
[English paraphrase. Every claim cites its source passage.]
(1-SOURCES/Commentaries/prajnakaramati-sk.md#^1-1)

### kunzang-pelden — Meaningful to Behold (Tibetan, 19th c.)
[Paraphrase, citations.]
(1-SOURCES/Commentaries/kunzang-pelden-bo.md#^1-1)

### Synthesis
[What all sources agree on. Do not flatten genuine disagreement here.]

### Divergences
[Where commentaries disagree, attributed and flagged ⚑.]

## Word Analysis
[Token-level notes only where the commentary makes a non-obvious choice —
compound analysis, sense disambiguation, inflection ambiguity.
Each row cites the commentary that determines the reading.]

## Translation Notes
[Figures of speech, idioms, honorifics, cultural references —
each with rendering strategies for different audiences.
Cite the commentary that explains the figure.]
```

Keep prose only. No quoting commentaries at length — paraphrase. English throughout. Original-language terms italicised on first use.

---

## 7. 2-RAILS — sections, wiki, glossaries

### Sections (`2-RAILS/Sections/[chapter].md`)

Per-chapter summary synthesised from verse packages — what the chapter does, who its audience is, what cultural context a translator needs. Cites verse packages, not 1-SOURCES directly. No new claims beyond what the packages contain.

### Local-Wiki (`2-RAILS/Local-Wiki/[sense-id].md`)

One page per sense ID attested in the text. Sense ID format: `term (disambiguating phrase)` — Wikipedia style, e.g. `bodhicitta (awakening mind)`. Filename uses underscores: `bodhicitta_(awakening-mind).md`. Each page collects what commentaries say about that sense within this text.

### Glossaries (`2-RAILS/Glossaries/`)

One file per language pair: `glossary-sk-en.md`, `glossary-sk-bo.md`, etc. Each entry maps a source lemma to its attested target-language renderings, frequency-ranked. Source is always existing translations in `1-SOURCES/Translations/`.

---

## 8. Divergences — never flatten

When commentaries disagree, record the disagreement explicitly. Mark with ⚑ in any field where the divergence shows up. Add a `### Divergences` section attributing each position.

If traditions teach genuinely incompatible doctrine on a verse, do not synthesise — record both positions and add to frontmatter:

```yaml
transformation_note: "tradition must be specified for this verse"
```

---

## 9. 3-TRANSFORMATIONS

Generated outputs only — translations, adaptations, lessons, reading plans. Each transformation lives under its own subfolder:

```
3-TRANSFORMATIONS/
   scholarly-en/
      brief.md          # purpose, audience, style, register
      terminology.md    # standard term renderings selected from glossaries
      outputs/          # the generated files
   childrens-en/
   ...
```

Each output file's frontmatter records which `2-RAILS/` packages were used:

```yaml
---
ref: 1-1
transformation_type: translation | adaptation | lesson
context_packages: [2-RAILS/Verses/1-1.md]
generation_date: 
---
```

Do not generate from packages whose `status` is not `complete`.

---

## 10. Style and language rules

- Analysis language is English throughout `2-RAILS/`.
- Quote original-language terms in IAST (Sanskrit/Pāli), Wylie or Unicode (Tibetan), Unicode (Chinese) — italicised on first use.
- **No parametric knowledge.** If you cannot cite a claim to a file in `1-SOURCES/`, do not include it.
- **No consensus flattening.** When commentaries disagree, say so.
- Present tense for analytical claims ("Prajñākaramati reads this as…"); past tense for historical statements.
- Use registered short IDs for commentaries throughout (e.g. `prajnakaramati`, `kunzang-pelden`).

---

## 11. Operations

**Ingest a passage**
1. Confirm the source is in `1-SOURCES/`.
2. Open or create the verse package in `2-RAILS/Verses/`.
3. Populate Traditional Interpretation, Word Analysis, Translation Notes — each field cited.
4. Update or create local-wiki pages for any new sense IDs.
5. Flag divergences with ⚑.

**Lint**
- Any field in `2-RAILS/` without a `1-SOURCES/` citation → mark `status: draft`.
- Any ⚑ flag without a Divergences entry → add one.
- Any sense ID used but missing from `Local-Wiki/` → create stub.

**Generate a transformation**
1. Confirm relevant verse packages are `complete`.
2. Assemble: section summary → source text → Traditional Interpretation → Word Analysis → Translation Notes → relevant Local-Wiki pages → terminology.md from the brief.
3. Generate. File under `3-TRANSFORMATIONS/[brief-id]/outputs/`.
4. Record context packages and generation date in frontmatter.

---

## 12. Citation Rules

Every claim in `2-RAILS/` must be traceable to a specific passage in `1-SOURCES/`. The citation format is:

```
(1-SOURCES/[folder]/[filename].md#^block-id)
```

Example:

```
(1-SOURCES/Commentaries/prajnakaramati-sk.md#^1-1)
```

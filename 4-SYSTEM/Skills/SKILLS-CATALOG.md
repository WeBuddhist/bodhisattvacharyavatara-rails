# Skills Catalog

This file catalogues every skill available in a Railroads vault, grouped by workflow phase. Each entry names the skill, states its purpose, describes its inputs and outputs, and points to the SKILL.md that operationalises it.

Skills that already exist are marked **[exists]**. Skills that are planned but not yet written are marked **[planned]**.

The pipeline reads top-to-bottom: source ingestion populates `1-SOURCES/`, the rails-building skills turn those sources into `2-RAILS/` context (Sections / Verses / Local-Wiki / Bilingual Glossaries), the translation skills consume those rails to produce `3-TRANSFORMATIONS/Translations/<track-name>/`, and the QA skill checks the output back against the rails.

---

## Source ingestion skills

These skills bring raw material into `1-SOURCES/` in a consistent, citation-ready format.

### `epub-to-markdown` **[exists]**
Converts EPUB files (commentaries, reference texts) into formatted Obsidian markdown with block IDs, headings, and frontmatter.
→ [`epub-to-markdown/SKILL.md`](epub-to-markdown/SKILL.md)

### `json-to-source-text` **[exists]**
Converts JSON exports of root texts (e.g. from tipitaka.org or SuttaCentral) into formatted source-text markdown files. Includes example converters for tipitaka.org and English paired translations; new source schemas get their own converter in `json-to-source-text/converters/`.
→ [`json-to-source-text/SKILL.md`](json-to-source-text/SKILL.md)

### `json-to-commentary` **[exists]**
Converts JSON exports of classical commentaries into formatted commentary markdown files.
→ [`json-to-commentary/SKILL.md`](json-to-commentary/SKILL.md)

### `format-root-text` **[exists]**
Normalises an existing root-text file: heading structure, block IDs, verse formatting.
→ [`format-root-text/SKILL.md`](format-root-text/SKILL.md)

### `format-commentary` **[exists]**
Normalises an existing commentary file: OCR cleanup, heading structure, paragraph granularity, block IDs.
→ [`format-commentary/SKILL.md`](format-commentary/SKILL.md)

### `format-chinese-commentary` **[exists]**
Format and normalize Chinese commentaries: structures headings, maps traditional outlines (科判), breaks prose into short paragraphs, applies block IDs, and implements a robust batch-processing protocol for long texts.
→ [`format-chinese-commentary/SKILL.md`](format-chinese-commentary/SKILL.md)

### `add-toc` **[exists]**
Inserts or regenerates a table of contents in a source or rails file.
→ [`add-toc/SKILL.md`](add-toc/SKILL.md)

---

## Rails-building skills (context preparation for translation)

These skills populate `2-RAILS/` with the structured context that translation and QA skills consume.

### `section-summary-raw` **[exists]**
**Purpose:** Generate a summary of one table-of-contents node in the original language, drawn from a single commentary.
**Inputs:** Commentary file(s) in `1-SOURCES/`, the TOC node to summarise.
**Outputs:** One summary file per commentary under `2-RAILS/Sections/Raw/<commentary-id>/<node-id>.md`.
**Rules:** Use only the terminology the commentary itself uses. No translation. No paraphrase beyond compression. Every claim cites a block ID from the source file.
→ [`section-summary-raw/SKILL.md`](section-summary-raw/SKILL.md)

### `section-summary-combined` **[exists]**
**Purpose:** Combine the per-commentary raw summaries for one TOC node and add an English translation of the combined summary.
**Inputs:** All raw summary files for the target node under `2-RAILS/Sections/Raw/`.
**Outputs:** One combined file at `2-RAILS/Sections/<node-id>.md` containing the original-language synthesis and an English translation.
→ [`section-summary-combined/SKILL.md`](section-summary-combined/SKILL.md)

### `verse-context` **[exists]**
**Purpose:** Build the verse-level context file for one verse.
**Inputs:** Root-text verse (from `1-SOURCES/`), all commentary passages that discuss it (via block transclusions from `1-SOURCES/`).
**Outputs:** One file at `2-RAILS/Verses/<verse-id>.md` containing: (1) transclusions of commentary passages, (2) a synthesis of the commentators' interpretations in the original language, (3) a disambiguated restatement of the verse in the original language precise enough to exclude any mistranslation.
→ [`verse-context/SKILL.md`](verse-context/SKILL.md)

### `local-wiki-article` **[exists]**
**Purpose:** Create or update a Local-Wiki article for one key term.
**Inputs:** Commentary passages that explain or define the term (via block citations from `1-SOURCES/`).
**Outputs:** One file at `2-RAILS/Local-Wiki/<term>_(<disambiguator>).md` containing: cited commentary explanations in the original language, and a short contextual definition drafted from those citations (also in the original language).
→ [`local-wiki-article/SKILL.md`](local-wiki-article/SKILL.md)

### `interlinear-gloss` **[exists]**
**Purpose:** For one root text + one translation, build an interlinear gloss file at `2-RAILS/Bilingual-Glossaries/Raw/<source>-<target>-gloss.md` pairing them verse by verse. Each verse becomes a `gloss` block in the Obsidian Interlinear Glossing plugin format (`\gla` source tokens, `\glb` morphology/lemma, `\glc` token-by-token target glosses, `\ex` free translation). Token-level alignment lives here so every downstream bilingual glossary step reads from one place.
**Inputs:** `1-SOURCES/Text/<root-text>.md`, one translation under `1-SOURCES/Translations/`.
**Outputs:** One gloss file per translation under `2-RAILS/Bilingual-Glossaries/Raw/<source-lang>-<target-lang>-gloss.md`.
→ [`interlinear-gloss/SKILL.md`](interlinear-gloss/SKILL.md)

### `glossary-extract-raw` **[exists]**
**Purpose:** Extract every source-language keyword and the rendering(s) it receives, from one interlinear gloss file, into a raw per-source bilingual glossary.
**Inputs:** One gloss file at `2-RAILS/Bilingual-Glossaries/Raw/<source>-<target>-gloss.md`.
**Outputs:** One bilingual glossary file at `2-RAILS/Bilingual-Glossaries/Raw/<source>-<target>.md` with a table mapping source lemma → rendering used in that translation.
→ [`glossary-extract-raw/SKILL.md`](glossary-extract-raw/SKILL.md)

### `glossary-combine` **[exists]**
**Purpose:** Merge all raw bilingual glossary files for one language pair into a single consolidated bilingual glossary.
**Inputs:** All relevant files under `2-RAILS/Bilingual-Glossaries/Raw/`.
**Outputs:** One consolidated bilingual glossary at `2-RAILS/Bilingual-Glossaries/<lang-pair>.md` showing every attested rendering side by side.
→ [`glossary-combine/SKILL.md`](glossary-combine/SKILL.md)

### `glossary-select` **[exists]**
**Purpose:** Build the prescriptive per-track termbase for one track by selecting the preferred rendering for each term from the consolidated bilingual glossary, guided by the track's `requirements.md`. If no existing rendering is satisfactory, derive one from the Local-Wiki article for that term and feed the new rendering back into the consolidated bilingual glossary.
**Inputs:** `2-RAILS/Bilingual-Glossaries/<lang-pair>.md`, `3-TRANSFORMATIONS/Translations/<track-name>/requirements.md`, Local-Wiki articles as needed.
**Outputs:** `3-TRANSFORMATIONS/Translations/<track-name>/termbase.md` — the prescriptive termbase scoped to keywords that appear in the text being translated; plus updates to the consolidated bilingual glossary for any new derived renderings.
→ [`glossary-select/SKILL.md`](glossary-select/SKILL.md)

---

## Translation requirements skills

### `requirements-author` **[planned]**
**Purpose:** Author or audit a track's `requirements.md` so it contains everything the `translate-section` skill needs to behave consistently across the whole text.
**Inputs:** The track folder `3-TRANSFORMATIONS/Translations/<track-name>/`; the per-track termbase (if it exists yet); samples of any prior translation in the same target language.
**Outputs:** A complete `3-TRANSFORMATIONS/Translations/<track-name>/requirements.md`, written in the target language.
→ `requirements-author/SKILL.md` *(to be written)*

---

## Translation skills

### `translate-section` **[planned]**
**Purpose:** Translate a small batch of TOC nodes into the target language.
**Inputs:** `requirements.md`, `termbase.md`, `audience.md` for the track; relevant section and verse packages from `2-RAILS/`; Local-Wiki articles as needed.
**Outputs:** Updated translation file(s) in `3-TRANSFORMATIONS/Translations/<track-name>/`. Each file's frontmatter lists the rail files it was generated from.
**Rules:** Translate small batches only — one or a few TOC nodes at a time. Every keyword rendering must match the per-track termbase. Introduce no new rendering without first adding it to the termbase and feeding it back into the consolidated bilingual glossary.
→ `translate-section/SKILL.md` *(to be written)*

---

## Translation QA skills

### `translation-qa` **[planned]**
**Purpose:** Review a translated section against the MQM translation error taxonomy, the track requirements, and the source rails.
**Inputs:** Translated section(s); `requirements.md`; `termbase.md`; relevant `2-RAILS/` files.
**Outputs:** Appended entries in `3-TRANSFORMATIONS/Translations/<track-name>/qa-report.md`. Each entry records: the segment, MQM error category, severity (critical / major / minor), and a suggested correction.
→ `translation-qa/SKILL.md` *(to be written)*

### `style-consistency-check` **[planned]**
**Purpose:** Catch style drift over long texts — creeping changes in register, sentence length, verse formatting, list handling, term gloss style.
**Inputs:** All translated files in `3-TRANSFORMATIONS/Translations/<track-name>/`; `requirements.md`; termbase.
**Outputs:** A style-drift section appended to `qa-report.md`, with span references back to the offending passages.
→ `style-consistency-check/SKILL.md` *(to be written)*

---

## Utility skills

### `source-property-extractor` **[exists]**
Extracts structured metadata (author, date, edition, language, publisher) from a source file and writes it to the frontmatter.
→ [`source-property-extractor/SKILL.md`](source-property-extractor/SKILL.md)

### `property-creator` **[exists]**
Creates or updates Obsidian frontmatter properties on a file.
→ [`property-creator/SKILL.md`](property-creator/SKILL.md)

### `structural-outline-ingest` **[exists]**
Ingests a structural outline (TOC) into a source or rails file.
→ [`structural-outline-ingest/SKILL.md`](structural-outline-ingest/SKILL.md)

---

## Vault-specific skills

These skills are specific to the Bodhisattvacaryāvatāra vault and are not part of the canonical Railroads template.

### `Root-Text-Structure` **[exists]**
**Purpose:** Format Tibetan root-text `.md` files for use in Obsidian. Produces clean, navigable Tibetan verse with Obsidian block IDs (`^chapter-verse`), chapter headings with TOC anchors, and one stanza per paragraph with each verse-line on its own line.
→ [`Root-Text-Structure/SKILL.md`](Root-Text-Structure/SKILL.md)

### `commentary-frontmatter` **[exists]**
**Purpose:** Generate complete YAML frontmatter for a commentary file in `1-SOURCES/Commentaries/` by extracting metadata from the file's title, colophon, and opening content.
→ [`commentary-frontmatter/SKILL.md`](commentary-frontmatter/SKILL.md)

### `reference-frontmatter` **[exists]**
**Purpose:** Generate complete YAML frontmatter for a secondary-literature or reference file in `1-SOURCES/References/` by extracting metadata from the file's title page, colophon, and opening content.
→ [`reference-frontmatter/SKILL.md`](reference-frontmatter/SKILL.md)

### `root-text-frontmatter` **[exists]**
**Purpose:** Generate complete YAML frontmatter for a root-text file in `1-SOURCES/Text/` by extracting metadata from the file's title, colophon, and opening content.
→ [`root-text-frontmatter/SKILL.md`](root-text-frontmatter/SKILL.md)

### `translation-frontmatter` **[exists]**
**Purpose:** Generate complete YAML frontmatter for a translation file in `1-SOURCES/Translations/` by extracting metadata from the file's title page, colophon, and opening content.
→ [`translation-frontmatter/SKILL.md`](translation-frontmatter/SKILL.md)

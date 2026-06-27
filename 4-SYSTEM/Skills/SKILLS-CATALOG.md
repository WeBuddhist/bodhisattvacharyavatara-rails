# Skills Catalog

This file catalogues every skill available in a Railroads vault, grouped by workflow phase. Each entry names the skill, states its purpose, describes its inputs and outputs, and points to the SKILL.md that operationalises it.

Skills that already exist are marked **[exists]**. Skills that are planned but not yet written are marked **[planned]**.

The pipeline reads top-to-bottom: source ingestion populates `1-SOURCES/`, the rails-building skills turn those sources into `2-RAILS/` context (Sections / Verses / Local-Wiki / Bilingual Glossaries), the translation skills consume those rails to produce `3-TRANSFORMATIONS/Translations/<track-name>/`, and the QA skill checks the output back against the rails.

---

## Source ingestion skills

These skills bring raw material into `1-SOURCES/` in a consistent, citation-ready format.

### `clean-commentary-text` **[exists]**
**Purpose:** Inspect a raw Tibetan commentary for mechanical text issues (page markers, running headers/footers, extra spaces, encoding artifacts), generate a targeted Python cleaning script, run it, and save the cleaned draft to `0-INBOX/`.
**Inputs:** Raw commentary file path in `1-SOURCES/Commentaries/` and a desired output filename.
**Outputs:** Cleaned draft at `0-INBOX/<output_name>` and a generated script at `4-SYSTEM/Skills/clean-commentary-text/clean-<commentary-id>.py`.
→ [`clean-commentary-text/SKILL.md`](clean-commentary-text/SKILL.md)

### `epub-to-markdown` **[exists]**
Converts EPUB files (commentaries, reference texts) into formatted Obsidian markdown with block IDs, headings, and frontmatter.
→ [`epub-to-markdown/SKILL.md`](epub-to-markdown/SKILL.md)

### `json-to-source-text` **[exists]**
Converts JSON exports of root texts (e.g. from tipitaka.org or SuttaCentral) into formatted source-text markdown files. Includes example converters for tipitaka.org and English paired translations; new source schemas get their own converter in `json-to-source-text/converters/`.
→ [`json-to-source-text/SKILL.md`](json-to-source-text/SKILL.md)

### `json-to-commentary` **[exists]**
Converts JSON exports of classical commentaries into formatted commentary markdown files.
→ [`json-to-commentary/SKILL.md`](json-to-commentary/SKILL.md)

### `colophon-metadata-extractor` **[exists]**
**Purpose:** Extract author, title, and language from a Tibetan text's colophon (last 200 syllables) and title block (first 200 syllables), populate frontmatter, and save as `{lang_tag}-{author_name}.md`.
**Inputs:** A `D*` file in `1-SOURCES/Commentaries/raw/`, or `batch: true` to process all D-files.
**Outputs:** New `.md` file in the same folder with YAML frontmatter and original content; original file untouched.
→ [`colophon-metadata-extractor/SKILL.md`](colophon-metadata-extractor/SKILL.md)

### `format-root-text` **[exists]**
Normalises an existing root-text file: heading structure, block IDs, verse formatting.
→ [`format-root-text/SKILL.md`](format-root-text/SKILL.md)

### `format-commentary` **[exists]**
Normalises an existing commentary file: OCR cleanup, heading structure, paragraph granularity, block IDs.
→ [`format-commentary/SKILL.md`](format-commentary/SKILL.md)

### `commentary-segmentation` **[exists]**
**Purpose:** Insert block boundaries into an OCR-clean Tibetan commentary so each block is a citation-sized unit (prose sentence or two, one verse stanza, one quotation). Rule-based (Stage 0 pre-clean + Stage 1 deterministic boundary detection). Run after `format-commentary`, before TOC inclusion and block-ID stamping.
**Inputs:** A formatted commentary file in `1-SOURCES/Commentaries/` or `0-INBOX/`.
**Outputs:** Boundary-segmented draft in `0-INBOX/` plus TSV reports. No block IDs assigned.
→ [`commentary-segmentation/SKILL.md`](commentary-segmentation/SKILL.md)

### `block-resegmentation` **[exists]**
**Purpose:** Re-draw block boundaries in a Stage-1 segmented commentary to produce semantically coherent, citation-sized units. The LLM flags merge/split operations (broken verse stanzas, orphaned lead-ins, incomplete enumerations, fused objection/reply); a Python script applies them and verifies text integrity. Run after `commentary-segmentation` Stage 1 **and** after TOC headings are embedded; before block-ID stamping.
**Inputs:** A Stage-1 segmented file with TOC headings embedded, in `0-INBOX/`.
**Outputs:** `0-INBOX/resegmented/<id>.reseg.md` (resegmented file) + `0-INBOX/resegmented/<id>.ops.md` (human-readable operations log). Staging files under `0-INBOX/temp/RESEG-<id>/windows/` (resumable).
**Requires:** `pip install google-genai` and `GEMINI_API_KEY` set.
→ [`block-resegmentation/SKILL.md`](block-resegmentation/SKILL.md)

### `format-chinese-commentary` **[exists]**
Format and normalize Chinese commentaries: structures headings, maps traditional outlines (科判), breaks prose into short paragraphs, applies block IDs, and implements a robust batch-processing protocol for long texts.
→ [`format-chinese-commentary/SKILL.md`](format-chinese-commentary/SKILL.md)

### `add-toc` **[exists]**
Inserts or regenerates a table of contents in a source or rails file.
→ [`add-toc/SKILL.md`](add-toc/SKILL.md)

### `tag-inline-toc` **[exists]**
**Purpose:** Insert markdown headings with `^N-N-0` block IDs at section boundaries in a formatted Tibetan commentary, then wrap the inline structural announcement phrases (*sa bcad*) with Obsidian wikilinks per CLAUDE.md §5b.
**Inputs:** A formatted commentary file from `0-INBOX/segmentation/` (has paragraph block IDs; lacks heading block IDs and wikilink tags).
**Outputs:** File at `0-INBOX/temp/tagged-<original-filename>` with headings, heading block IDs, and `[[#^N-N-0|term]]` wikilinks applied to all announcement and restatement phrases.
→ [`tag-inline-toc/SKILL.md`](tag-inline-toc/SKILL.md)

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
**Outputs:** One file at `2-RAILS/Verses/<verse-id>.md` with: Sanskrit + Tibetan source transclusions; per-commentary English paraphrase (Traditional Interpretation) + Divergences; and the Tibetan descriptive layers — an AI-Overview synthesis (generation prompt lives in the skill), a chendrel (ཚིག་འགྲེལ) word-commentary replacing the old UCCA layer, word-by-word disambiguation, key concepts (in-verse / from-commentary), attached stories, metaphors, scriptural quotations, and a disambiguated restatement. Format is authoritative in `2-RAILS/About Rails.md` §5.
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

### `verse-commentary-summarizer` **[exists]**
**Purpose:** Generate a verse-specific summary file by extracting explanations from provided commentaries, summarizing each commentary, and creating a combined synthesis.
**Inputs:** Verse ID, list of commentary files, output path/track.
**Outputs:** A summary file under `3-TRANSFORMATIONS/Translations/<track>/Verses/<verse-id>.md`.
→ [`verse-commentary-summarizer/SKILL.md`](4-SYSTEM/Skills/verse-commentary-summarizer/SKILL.md)

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

### `create-skill` **[exists]**
Creates a new skill from scratch: generates the SKILL.md, prompt structure, and registers it in the catalog.
→ [`create-skill/SKILL.md`](create-skill/SKILL.md)

### `vault-audit` **[exists]**
Audits the vault for consistency: checks that all linked files exist, frontmatter is complete, and skills are registered in the catalog.
→ [`vault-audit/SKILL.md`](vault-audit/SKILL.md)

### `transclusion` **[exists]**
**Purpose:** Insert Obsidian block-transclusion links for root-text verse(s) into a second root-text version or into commentary files, placing each transclusion at the correct structural position.
**Inputs:** (Type 1) Two root-text/translation file paths and an optional verse range; (Type 2) verse ID(s), root-text file path, and one or more commentary file paths with commentary type.
**Outputs:** Target file(s) modified in place with `![[file#^block-id]]` transclusion links inserted; no new files created.
→ [`transclusion/SKILL.md`](transclusion/SKILL.md)

### `tibetan-ocr-quality` **[exists]**
**Purpose:** Calculate perplexity of a Tibetan OCR output file using KenLM and Botok normalization to assess OCR quality.
**Inputs:** A `.txt` file containing raw Tibetan OCR output; the `BoKenlm-syl-v0.4.arpa` model file.
**Outputs:** Console report with sentence count, token count, log-probability, and perplexity score.
→ [`tibetan-ocr-quality/SKILL.md`](tibetan-ocr-quality/SKILL.md)

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

### `en-365-day-practice-plan-generator` **[exists]**
**Purpose:** Generate a complete single-day Bodhisattvacharyavatara (སྤྱོད་འཇུག) practice plan session document in the traditional 7-section format, in English. Saves to `3-TRANSFORMATIONS/Plans/the-bodhisattva-challenge/en/Days/`.
→ [`en-365-day-practice-plan-generator/SKILL.md`](4-SYSTEM/Skills/en-365-day-practice-plan-generator(old)/SKILL.md)

### `english-plan-generator` **[exists]**
**Purpose:** Generate a complete single-day Bodhisattvacharyavatara practice plan session document in the 6-section format defined by `3-TRANSFORMATIONS/Plans/the-bodhisattva-challenge/en/requirements.md`. Supersedes `en-365-day-practice-plan-generator` for the Bodhisattva Challenge English stream. Saves to `3-TRANSFORMATIONS/Plans/the-bodhisattva-challenge/en/Days/`.
→ [`english-plan-generator/SKILL.md`](english-plan-generator/SKILL.md)

### `plan-day-feedback-revision` **[exists]**
**Purpose:** Audit an existing Bodhisattva Challenge plan day file against the Day-1 tester feedback criteria and revise it in place to fix every content issue (AI-slop, Tier 3 accessibility, orientation, liturgy prominence, translation flags, credibility, reading load) without breaking the 6-section format or the citation chain.
**Inputs:** A target day file under `…/en/Days/`, the `english-plan-generator` contract, the Day-1 feedback summary, the Tier 3 persona, the liturgy asset, and the verse's source rail (preferred) or interim commentary summary.
**Outputs:** The revised day file overwritten in place at `…/en/Days/[DAY].md` (with a `revision` frontmatter block), plus an audit record at `…/en/feedback-audit/[DAY].md`.
→ [`plan-day-feedback-revision/SKILL.md`](plan-day-feedback-revision/SKILL.md)

### `hindi-plan-from-english` **[exists]**
**Purpose:** Translate an existing English Bodhisattva Challenge day-plan file into plain, conversational ("chai"-register) Hindi, rendering only the Opening/Introduction, From the Tradition, and Today's Practice sections into everyday Devanagari Hindi while reproducing everything else verbatim.
**Inputs:** A finished English day file under `3-TRANSFORMATIONS/Plans/the-bodhisattva-challenge/en/Days/<Chapter-folder>/<DAY_NUMBER>.md`, plus the day number.
**Outputs:** A structurally identical Hindi day file at `3-TRANSFORMATIONS/Plans/the-bodhisattva-challenge/hi/Days/<Chapter-folder>/<DAY_NUMBER>.md` with only the three prose sections translated.
→ [`hindi-plan-from-english/SKILL.md`](hindi-plan-from-english/SKILL.md)

### `toc-candidate-extraction` **[exists]**
**Purpose:** Scan a Tibetan commentary passage and extract every ས་བཅད candidate — Type A (topic announcements), Type B (node headers), and Type C (closing counts). Prioritises recall: extracts all possible candidates rather than filtering. Outputs a structured candidate list saved to `0-INBOX/toc-candidates-<commentary-id>.md` for review before downstream outline-building.
**Inputs:** A Tibetan text passage (pasted or from a file) and a short `commentary-id` for the output filename.
**Outputs:** `0-INBOX/toc-candidates-<commentary-id>.md` containing every candidate with TYPE, exact text, 10-word context window, and named items.
→ [`toc-candidate-extraction/SKILL.md`](toc-candidate-extraction/SKILL.md)

### `toc-tree-ingest` **[exists]**
**Purpose:** Ingest a pre-extracted TOC tree (`toc-tree-*.md`) into a commentary file in `1-SOURCES/Commentaries/commentaries_with_toc/` by inserting markdown headings with block IDs, one depth level per run. The `[[...]]` context snippets in the tree are used only to locate positions in the commentary — never copied into the output.
**Inputs:** `toc-tree-*.md` path; target commentary file path; `commentary_id`; `depth` (integer, which level to ingest this run).
**Outputs:** Commentary file updated in place with `## ... ^N-0` … `###### ... ^N-N-…-0` heading lines inserted before each section's context anchor. JSON parse cache at `0-INBOX/temp/TOC-<id>/toc-tree-<id>.json`.
→ [`toc-tree-ingest/SKILL.md`](toc-tree-ingest/SKILL.md)

### `toc-tree-extraction` **[exists]**
**Purpose:** Build the FULL nested, decimal-numbered ས་བཅད TOC tree (དཀར་ཆག) from a Tibetan commentary — the complete pipeline, not just candidates. Claude-native port of `4-SYSTEM/Scripts/toc_tree_extractor/extract_toc_tree.py` (which uses the Gemini API): Claude performs the four inference passes itself — (1) section candidates, (2) verbatim enumeration blocks, (3) nested decimal tree, (4) QC repair — while two bundled Python helpers (`chunk_file.py`, `qc_check_tree.py`) do the deterministic chunking and tree QC. Use for in-session runs on one/a-few commentaries; use the Gemini script for headless batch runs.
**Inputs:** Commentary/root-text `.md` path (normally `1-SOURCES/Commentaries/`) and a short `commentary-id`.
**Outputs:** `0-INBOX/toc-candidates-<id>.md`, `0-INBOX/toc-tree-<id>.md` (no `^toc` block IDs), and `0-INBOX/toc-tree-qc-<id>.md`; per-chunk staging under `0-INBOX/temp/TOC-<id>/`.
→ [`toc-tree-extraction/SKILL.md`](toc-tree-extraction/SKILL.md)

### `Outline-Extractor` **[exists]**
**Purpose:** Extract the structural outline (ས་བཅད།) from a Tibetan commentary in `1-SOURCES/Commentaries/` and produce two output files: a flat tab-indented list (`ས་བཅད་རྐྱང་པ།`) and a nested heading+list structured outline (`ལྟེ་བའི་དཀར་ཆག།`), both saved to `3-TRANSFORMATIONS/Adaptations/<commentary-id>-sa-bcad/`.
**Inputs:** Commentary file path in `1-SOURCES/Commentaries/`, a short `commentary-id`, and the Tibetan title of the work.
**Outputs:** Two `.md` files in `3-TRANSFORMATIONS/Adaptations/<commentary-id>-sa-bcad/` — the flat extracted outline and the nested structured outline.
→ [`Outline-Extractor/SKILL.md`](Outline-Extractor/SKILL.md)

### `multilevel-summary` **[exists]**
**Purpose:** Generate an audience-targeted summary (kids, general, or academic) of a verse or chapter of the Bodhisattvacaryāvatāra, grounded in the traditional commentary tradition.
**Inputs:** Scope type (`verse` or `chapter`), scope ID (verse ID such as `1-1`, or chapter number/name), and audience (`kids`, `general`, or `academic`).
**Outputs:** One summary file at `3-TRANSFORMATIONS/Adaptations/multilevel-summaries/<audience>/verse-<chapter-verse>.md` or `…/chapter-<N>.md`, with Obsidian segment-links to all commentary blocks used.
→ [`multilevel-summary/SKILL.md`](multilevel-summary/SKILL.md)

### `BCA-Term-Definition` **[exists]**
**Purpose:** Extract verbatim definitions of key terms from Tibetan commentaries and fill them into the Meaning column of `BCA-Term-Localization.md`, formatted in traditional Tibetan quotation style.
**Inputs:** One or more terms from the Bo column of `2-RAILS/Local-Wiki/BCA-Term-Localization.md`; all commentary files under `1-SOURCES/Commentaries/`.
**Outputs:** `2-RAILS/Local-Wiki/BCA-Term-Localization.md` updated in place — Meaning cells filled with verbatim quotations framed as `[short-name]ནས་「…」ཞེས་གསུངས་སོ།།` with inline block-ID citations.
→ [`BCA-Term-Definition/SKILL.md`](BCA-Term-Definition/SKILL.md)

### `BAC-Term-Localization` **[exists]**
**Purpose:** Translate Tibetan Buddhist key terms in BCA-Term-Localization.md into English, Chinese, Hindi, Nepali, Russian, and Mongolian, deriving each rendering from the commentary-based Meaning column.
**Inputs:** One or more terms (or "all") from the Bo column of `2-RAILS/Local-Wiki/BCA-Term-Localization.md`; target languages (default: all six); the Meaning column as the disambiguating source.
**Outputs:** `2-RAILS/Local-Wiki/BCA-Term-Localization.md` updated in place — En, Zh, Hin, Nep, Rus, Mon cells filled with contextually accurate renderings; novel renderings flagged with `*`.
→ [`BAC-Term-Localization/SKILL.md`](BAC-Term-Localization/SKILL.md)

### `dkr-fellow-plan` **[exists]**
**Purpose:** Generate the Day-63 practice plan for the 63-day DKR Fellow package. Produces a 5-section Tibetan-language markdown document: (1) fixed Refuge & Bodhicitta prayers, (2) root verses for Chapter 10 V.45–58, (3) DKR's teaching extracted from BCAC21_DKR_bo.md Session 2, (4) fixed Dedication & Aspiration prayers, (5) a concrete daily-life application.
**Inputs:** `3-TRANSFORMATIONS/Plans/DKR-Fellow/schedule.md` (verse assignment), `1-SOURCES/Translations/bo-བློ་ལྡན་ཤེས་རབ།.md` (root text verses ^10-45–^10-58), `3-TRANSFORMATIONS/Plans/DKR-Fellow/DKR-Teaching-Assignment-to-Days.md` (DKR teaching, Day-63 section ^9-39–^9-43).
**Outputs:** `3-TRANSFORMATIONS/Plans/DKR-Fellow/Day-63-Ch10-V45-58.md` filled with the complete 5-section practice plan.
→ [`DKR Fellow Plan/SKILL.md`](4-SYSTEM/Skills/DKR-Fellow-Plan-Generator/SKILL.md)

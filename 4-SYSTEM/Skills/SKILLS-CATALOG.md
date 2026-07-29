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

### `add-block-id-root-text` (`format-sk-root-text`) **[exists]**
**Purpose:** Format and re-index a **Sanskrit** root-text file in `1-SOURCES/Text/` using the vault's block-ID convention — front matter (Roman), chapter verses (Arabic), colophons (lowercase letters), and book back matter. Specific to Sanskrit root texts, not commentaries or translations. Uses a bundled `apply.py` helper (audit → LLM zone identification → mechanical apply).
**Inputs:** A Sanskrit root-text `.md` file in `1-SOURCES/Text/`.
**Outputs:** The file re-indexed in place with block IDs; audit report from `apply.py`.
→ [`add-block-id-root-text/SKILL.md`](add-block-id-root-text/SKILL.md)

### `commentary-resegment` **[exists]**
**Purpose:** Re-paragraph a Tibetan commentary that has ONE CLAUSE PER LINE into readable sense-unit paragraphs (~2–4 lines each), grouped **by meaning** (LLM judgment on content/context, not grammar rules). A Python script joins each group onto one line, separates paragraphs with a blank line, and verifies the source text is byte-identical. Replaces the older rule-based `block-resegmentation-linewise`.
**Inputs:** A one-clause-per-line commentary (e.g. `*_segmented.md`, `*.toc.md`).
**Outputs:** A re-paragraphed commentary draft; source text changed only in newlines/spaces, never in words or characters (integrity-gated).
→ [`commentary-resegment/SKILL.md`](commentary-resegment/SKILL.md)

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

### `Verse-package-file-creator` **[exists]**
**Purpose:** Extract four targeted commentary elements — story (གཏམ་རྒྱུད/སྒྲུང), extended information (ཞར་བྱུང), keyword explanation (ཚིག་འགྲེལ), and key-concept explanation (གནད་དོན) — for one verse, by tracing the verse through its block-transclusion into one or more commentaries. A lighter, focused relative of `verse-context` that produces only those four Tibetan layers rather than the full rail.
**Inputs:** A verse (text or verse ID), the `1-SOURCES/` root file carrying its block ID, one or more commentary files that transclude the verse, and an output filename.
**Outputs:** One extraction file at `2-RAILS/Verses/<output-filename>.md` — the four elements in Tibetan, each cited to its commentary block (falling back to the verse-transclusion anchor when commentary prose is un-stamped), with ⚑ divergences when multiple commentaries disagree. `status: draft`.
→ [`Verse-package-file-creator/SKILL.md`](Verse-package-file-creator/SKILL.md)

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

### `AI-summary-generator` **[exists]**
**Purpose:** Generate the scholarly "AI Overview" synthesis layer for one verse in Tibetan — core synthesis, key themes, divergences, and practical application — drawing only on that verse's already-cited Traditional Interpretation paraphrases.
**Inputs:** A verse ID and its `2-RAILS/Verses/<verse-id>.md` file (its Traditional Interpretation section is the sole source).
**Outputs:** The AI Overview (བསྡུས་དོན།) section of `2-RAILS/Verses/<verse-id>.md`, written or replaced in place; no other layer touched.
→ [`AI-summary-generator/SKILL.md`](AI-summary-generator/SKILL.md)

### `verse-context-batch` **[exists]**
**Purpose:** Build all verse-level context packages for one chapter in bulk. Scans every commentary to produce a single block-ID mapping table, then generates one `2-RAILS/Verses/<verse-id>.md` file per verse in the chapter via a Python script — enforcing one consistent mapping across the whole chapter. Output format is identical to `verse-context`; `status: draft` on generation.
**Inputs:** Chapter number, verse range, all relevant `1-SOURCES/Commentaries/*.md` (must already have block IDs), and the translation file `bo-བློ་ལྡན་ཤེས་རབ།.md`.
**Outputs:** One file per verse at `2-RAILS/Verses/<chapter>-<verse>.md` (existing files skipped); generation script saved to `0-INBOX/verse-context-batch-ch<N>.py`.
→ [`verse-context-batch/SKILL.md`](verse-context-batch/SKILL.md)

### `root-verse-context-creator` **[exists]**
**Purpose:** For a Tibetan root text interleaved with a nested sa-bcad (ས་བཅད།) outline, generate a Tibetan contextual summary paragraph for each group of root verses by tracing the full nested outline path — outermost container down to the leaf section — closing with `གཞུང་ཚིག་ཡིན་ནོ།།` in the style of Khenpo Kunpal's sa-bcad commentary.
**Inputs:** A sa-bcad + root-text (ས་བཅད་རྩ་སྦྱར།) file that interleaves outline headings (`^TOC-…` anchors) with verse blocks; optional single-chapter scope.
**Outputs:** `2-RAILS/Verses/bo-[chapter]-ས་བཅད་གཞིར་བཟུང་རྩ་ཚིག་ངོས་འཛིན།.md` with each verse group quoted verbatim followed by its outline-path summary paragraph.
→ [`root-verse-context-creator/SKILL.md`](root-verse-context-creator/SKILL.md)

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

### `translate-zero-shot` **[exists]**
**Purpose:** Produce a full BCA translation track directly from `1-SOURCES/` when verse rails are not yet `status: complete`. Tibetan (`bo-བློ་ལྡན་ཤེས་རབ།.md`) is the meaning base, Sanskrit (`BCAV08_SH_sk.md`) the disambiguation reference, and three block-aligned human translations (Padmakara, Wallace, Choephel) the per-verse triangulation witnesses: consensus confirms a reading, splits are resolved from the Sanskrit and flagged.
**Inputs:** Target language, audience level (`children` / `plain` / `scholar`), optional chapter scope.
**Outputs:** Track folder `3-TRANSFORMATIONS/Translations/<lang>-<audience>-audience/` with `requirements.md`, `audience.md`, an evidence-built `termbase.md` (each rendering cites attested witness renderings at a block ID), one `Chapter-NN.md` per chapter, and a merged full-text file built by `scripts/merge_chapters.py`.
**Rules:** Rails-complete verses use the rails; existing track contracts are read, never overwritten or re-seeded; all output stays `status: draft`; termbase renderings are locked, append-only; `translation-qa` is required before handoff.
→ [`translate-zero-shot/SKILL.md`](translate-zero-shot/SKILL.md)

### `verse-commentary-summarizer` **[exists]**
**Purpose:** Generate a verse-specific summary file by extracting explanations from provided commentaries, summarizing each commentary, and creating a combined synthesis.
**Inputs:** Verse ID, list of commentary files, output path/track.
**Outputs:** A summary file under `3-TRANSFORMATIONS/Translations/<track>/Verses/<verse-id>.md`.
→ [`verse-commentary-summarizer/SKILL.md`](4-SYSTEM/Skills/verse-commentary-summarizer/SKILL.md)

### `translate-commentary-ai` **[exists]**
**Purpose:** Translate a source commentary (Tibetan or other) into the target language using the track's AI-translation `requirements.md`, `termbase.md`, and the relevant `2-RAILS/Sections/` synthesis for terminological consistency and philosophical fidelity. Every termbase-locked lemma is rendered exactly as specified; no unauthorized synonyms.
**Inputs:** The source commentary; `3-TRANSFORMATIONS/Translations/en-ai/requirements.md` + `termbase.md`; section summaries under `2-RAILS/Sections/`.
**Outputs:** A new AI-generated translation file in `3-TRANSFORMATIONS/Translations/` with `AI-generated` in the filename and complete YAML frontmatter.
→ [`translate-commentary-ai/SKILL.md`](translate-commentary-ai/SKILL.md)

### `bo-en-translate` **[exists]**
**Purpose:** Translate BCA source text (Tibetan, or the base English verse translation) into **graded English** at a specified audience level (beginner / general / intermediate / advanced), enforcing term consistency via a pre-built keyword termbase. Scans the source for recognised terms, locks their English equivalents at the target register, and outputs one line per verse followed by its block ID.
**Inputs:** Source text (Tibetan or base English), target audience grade, optional verse IDs, optional output path.
**Outputs:** A clean graded-English markdown file (one line per verse + block ID); optionally saved to `3-TRANSFORMATIONS/Translations/`.
→ [`english-translation/bo-en-translate-skill.md`](english-translation/bo-en-translate-skill.md)

### `generate-modern-chinese` (`spyodjug-zh-plain-chinese`) **[exists]**
**Purpose:** Generate plain written-Chinese (白話) translations for the `zh-plain-chinese` track, triangulating the Tibetan root against the Padmakara English translation and following all rules in the track's `requirements.md`, `audience profile.md`, and `termbase.md`.
**Inputs:** Day number or verse range; `3-TRANSFORMATIONS/Translations/zh-plain-chinese/` contracts; Tibetan root `bo-བློ་ལྡན་ཤེས་རབ།.md`; Padmakara English; Gyaltsab and Dalai Lama Chinese commentaries.
**Outputs:** Day files under `3-TRANSFORMATIONS/Translations/zh-plain-chinese/days/`; termbase updates as needed.
→ [`generate-modern-chinese/SKILL.md`](generate-modern-chinese/SKILL.md)

### `rails-to-verse-translation` **[exists]**
**Purpose:** Translate a batch of verses into metrical or rhymed verse in any target language, working from `2-RAILS/Verses/` synthesis rather than the bare root line; derives the style contract from an existing partial translation, locks a termbase built from the rails' `གནད་ཚིག` tables, and logs every `⚑` divergence with the reading taken and the readings dropped.
**Inputs:** Verse range; target language and `lang_tag`; track name; an existing partial translation to match on form (or a statement that none exists); optional append target; divergence policy; doc language.
**Outputs:** Track folder `3-TRANSFORMATIONS/Translations/<track>/` with `requirements.md`, `audience.md`, `termbase.md`, `divergence-log.md`, and `Chapter-NN-verses-A-B.md`; optionally appended and block-ID-stamped into an existing translation file. Bundles three scripts: rails context extraction, verse linting, and block-ID stamping.
→ [`rails-to-verse-translation/SKILL.md`](rails-to-verse-translation/SKILL.md)

---

## Translation QA skills

### `translation-qa` **[exists]**
**Purpose:** Review a translated section against the MQM translation error taxonomy, the track requirements, and the source rails.
**Inputs:** Translated section(s); `requirements.md`; `termbase.md`; relevant `2-RAILS/` files.
**Outputs:** Appended entries in `3-TRANSFORMATIONS/Translations/<track-name>/qa-report.md`. Each entry records: the segment, MQM error category, severity (critical / major / minor), and a suggested correction.
→ [`translation-qa/SKILL.md`](translation-qa/SKILL.md)

### `style-consistency-check` **[planned]**
**Purpose:** Catch style drift over long texts — creeping changes in register, sentence length, verse formatting, list handling, term gloss style.
**Inputs:** All translated files in `3-TRANSFORMATIONS/Translations/<track-name>/`; `requirements.md`; termbase.
**Outputs:** A style-drift section appended to `qa-report.md`, with span references back to the offending passages.
→ `style-consistency-check/SKILL.md` *(to be written)*

### `commentary-fact-check` **[exists]**
**Purpose:** Audit an English BCA translation verse by verse against any Tibetan commentary that transcludes the root text, using strict **term-by-term alignment** (not a gist check): for each content word the commentary explicitly glosses, map Tibetan lemma → commentary gloss → English word and flag where the English names the wrong thing — kāya/dharma/mind swaps, precise terms softened to vague synonyms, wrong named entities, wrong number/scope, wrong simile tenor, wrong agent, wrong enumeration order — even when it reads fluently. Includes a second sweep scoped to the highest-miss classes (doctrinal-category swaps, named entities, numbers).
**Inputs:** Commentary path (e.g. `BCAC14_NTS_bo_segmented.md`, `BCAC19_KS_bo.md`); translation-file path (e.g. `bca-en-plain.md` or a graded `bca-en-<grade>.md`); a bounded scope (chapter, `colophon`, or explicit verse range — never the whole text).
**Outputs:** Appended per-verse tables (ERROR / MISMATCH / softening rows with Tibetan + gloss + fix) in `<translation-dir>/commentary-fact-check-report-<commentary-id>-<translation-name>.md`, one report per commentary×translation pair. Bundles `scripts/extract_commentary.py` (splits the commentary on its transclusion markers into per-verse passages) and `scripts/extract_translation.py` (parses a translation file into per-verse text).
→ [`commentary-fact-check/SKILL.md`](commentary-fact-check/SKILL.md)

### `commentary-fact-check-apply-fixes` **[exists]**
**Purpose:** Apply the ⚠ discrepancies already logged in a grade's `commentary-fact-check-report-<grade>.md` to the graded English translation (`bca-en-<grade>.md`), one grade and one chapter/range at a time, then re-run `commentary-fact-check` on that range to confirm the fix landed. Companion editing pass to `commentary-fact-check` (which only reports, never edits). Applies **only mechanical corrections** with an unambiguous replacement (wrong named entity, wrong number, dropped content, inconsistent locked rendering); any row requiring interpretive judgment is left untouched and surfaced to the human.
**Inputs:** A `commentary-fact-check-report-<grade>.md`; the translation file `bca-en-<grade>.md`; a bounded scope (chapter or range).
**Outputs:** Edits applied in place to `bca-en-<grade>.md`; a re-verification run over the same range; a list of judgment-call rows deferred to the human.
→ [`commentary-fact-check-apply-fixes/SKILL.md`](commentary-fact-check-apply-fixes/SKILL.md)

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

### `Transclusion-rootext-into-commentaries` **[exists]**
**Purpose:** Transclude root-text verses into a Tibetan commentary and format the blank-line spacing around each transclusion, via a three-stage scripted pipeline: (1) insert `![[root#^N-V]]` before each verse's first full inline quotation in the commentary (variant-tolerant; full stanza preferred over passing citations), (2) remove the blank line between the preceding commentary line and the transclusion, (3) add a blank line before the sa-bcad (ས་བཅད) block that introduces the verse — before the first line of a preceding enumeration when one exists, and nothing when the line above is prose/connector/conclusion.
**Inputs:** `root` (root/translation path with `^N-V` block IDs), `commentary` (Tibetan commentary path), `link-base` (transclusion link base, e.g. `bo-བློ་ལྡན་ཤེས་རབ།`), optional `chapter`.
**Outputs:** The commentary file modified in place — only inserted `![[…]]` lines and the blank lines immediately around them; no commentary text changed. Bundles three dry-runnable Python scripts under `scripts/`.
→ [`Transclusion-rootext-into-commentaries/SKILL.md`](Transclusion-rootext-into-commentaries/SKILL.md)

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

### `Verse-Context-Summary` **[exists]**
**Purpose:** Create a comprehensive single-verse summary page assembling Sanskrit and Tibetan text transclusions, Zhenga's annotations (མཆན་འགྲེལ།), per-commentary explanations (དོན་འགྲེལ།), stories (སྒྲུང་འགྲེལ།), metaphors (དཔེ།), scriptural quotations (ལུང།), main teaching points (གཙོ་གནད།), key terms (གནད་ཚིག), and a Google-AI-Overview-style Tibetan synthesis (བསྡུས་དོན།). Each section is cited to `1-SOURCES/` blocks. Creator: Tigerboy.
**Inputs:** Verse ID (e.g. `1-1`); commentary files in `1-SOURCES/Commentaries/Transcluded/`; Khenpo Zhenga's mchan-'grel at `1-SOURCES/Commentaries/Transcluded/BCAC19_KS_bo.md`.
**Outputs:** One file at `2-RAILS/Verses/<verse-id>-summary.md` — the complete ten-section verse summary page, `status: draft`.
→ [`Verse-Context-Summary/SKILL.md`](Verse-Context-Summary/SKILL.md)

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

### `bo-hi-keyword-grade` **[exists]**
**Purpose:** Enrich the existing English-Tibetan verse keyword JSON with Hindi translations and audience-grade classifications. Reads Tibetan verse text from the canonical source and Hindi translations from a user-supplied annotated Hindi file (with `[grade:beginner/intermediate/advanced]` markers). Produces three separate output JSON files — one per audience grade — each with `bo_text`, `hi_text` per verse and `hi`, `grade` per keyword. Keywords are filtered by rank cutoff per grade (≤200 beginner, ≤500 intermediate, all for advanced).
**Inputs:** `1-SOURCES/Translations/bo-བློ་ལྡན་ཤེས་རབ།.md`, `4-SYSTEM/scripts/english_keyword/output/en-David_Karma_Choephel_en_bo_keyword_meaning_enriched.json`, user-supplied annotated Hindi file.
**Outputs:** `4-SYSTEM/scripts/english_keyword/output/bo_hi_keyword_beginner.json`, `…intermediate.json`, `…advanced.json`.
→ [`bo-hi-keyword-grade/SKILL.md`](bo-hi-keyword-grade/SKILL.md)

### `bo-hi-translate` **[exists]**
**Purpose:** Translates a BCA passage (English verse translation or Tibetan) into Hindi at a specified audience grade (beginner / general / intermediate / advanced), enforcing term consistency throughout by loading the grade-appropriate keyword termbase (`bo_hi_keyword_*.json`). Scans source for recognised terms, locks their Hindi equivalents, translates at the correct register, runs a consistency check, and outputs a term table alongside the translation.
**Inputs:** Source text (English or Tibetan), target audience grade, optional verse IDs, optional output path.
**Outputs:** Hindi translation at the target grade with a locked-term table; optionally saved to `3-TRANSFORMATIONS/Translations/hi-<grade>/`.
→ [`bo-hi-translate/SKILL.md`](bo-hi-translate/SKILL.md)

### `bo-vi-keyword-grade` **[exists]**
**Purpose:** Enrich the existing English-Tibetan verse keyword JSON with Vietnamese translations and audience-grade classifications. Reads Tibetan verse text from the canonical source and Vietnamese translations from a user-supplied attested Vietnamese translation file. Produces four separate output JSON files — one per audience grade — each with `bo_text`, `vi_text` per verse and `vi`, `grade` per keyword. Keywords are filtered by rank cutoff per grade (≤200 beginner, ≤500 general/intermediate, all for advanced). Mirrors `bo-hi-keyword-grade` for the Vietnamese-Tibetan pair.
**Inputs:** `1-SOURCES/Translations/bo-བློ་ལྡན་ཤེས་རབ།.md`, `4-SYSTEM/scripts/english_keyword/output/en-David_Karma_Choephel_en_bo_keyword_meaning_enriched.json`, optional raw Vietnamese translation file (e.g. `3-TRANSFORMATIONS/Translations/vi-beginner-audience/BCA-Full-Beginner-Vietnamese.md`).
**Outputs:** `4-SYSTEM/scripts/english_keyword/output/bo_vi_keyword_beginner.json`, `…general.json`, `…intermediate.json`, `…advanced.json`, plus the base `en-bo-vi-termbase-general.json`.
→ [`vietnamese-translation/bo-vi-keyword-grade-skill.md`](vietnamese-translation/bo-vi-keyword-grade-skill.md)

### `bo-vi-translate` **[exists]**
**Purpose:** Translates a BCA passage (English verse translation or Tibetan) into Vietnamese at a specified audience grade (beginner / general / intermediate / advanced), enforcing term consistency throughout by loading the grade-appropriate keyword termbase (`bo_vi_keyword_*.json`). Scans source for recognised terms, locks their Vietnamese equivalents, translates at the correct register, runs a consistency check, and outputs a term table alongside the translation. Mirrors `bo-hi-translate` for the Vietnamese-Tibetan pair.
**Inputs:** Source text (English or Tibetan), target audience grade, optional verse IDs, optional output path.
**Outputs:** Vietnamese translation at the target grade with a locked-term table; optionally saved to `3-TRANSFORMATIONS/Translations/vi-<grade>/`.
→ [`vietnamese-translation/bo-vi-translate-skill.md`](vietnamese-translation/bo-vi-translate-skill.md)

### `365-day-practice-plan-generator` (`bca-practice-plan`) **[exists]**
**Purpose:** Generate a complete single-day BCA (སྤྱོད་འཇུག) practice-plan session document in the traditional **6-section** format, in **Tibetan**. The Tibetan-stream counterpart of `en-365-day-practice-plan-generator`: fixed refuge/bodhicitta opening, day-specific motivation, the assigned verses, commentary and application, fixed dedication/aspiration closing.
**Inputs:** Day number (1–365); chapter + verse range (or looked up from the `bo` schedule); commentary language (default Tibetan).
**Outputs:** A Tibetan-language day file for the Bodhisattva Challenge `bo` stream, built from the root text and matching `2-RAILS/Verses/<verse-id>-summary.md` files.
→ [`365-day-practice-plan-generator/SKILL.md`](365-day-practice-plan-generator/SKILL.md)

### `Daily-Challenge-Creator` (`daily-challenge-creator`) **[exists]**
**Purpose:** Generate one concrete trilingual daily practice (ལག་ལེན) and explanation (འགྲེལ་བཤད) per BCA verse, reading all four lines as a whole to identify the central teaching, in Tibetan → English → Hindi.
**Inputs:** One or more སྤྱོད་འཇུག verses.
**Outputs:** For each verse, a ལག་ལེན practice and an འགྲེལ་བཤད explanation in all three languages, grouped beneath the verse.
→ [`Daily-Challenge-Creator/SKILL.md`](Daily-Challenge-Creator/SKILL.md)

### `dharma-verse-practice` **[exists]** (packaged `.skill`)
**Purpose:** Turn Bodhicaryāvatāra verses into concrete, actionable trilingual daily practices (ལག་ལེན) and explanations (འགྲེལ་བཤད) in Tibetan, English, and Hindi. Packaged, distributable variant of `Daily-Challenge-Creator`, shipped as a zipped `.skill` archive.
**Inputs:** One or more BCA verses (Tibetan or otherwise).
**Outputs:** Per-verse practice + explanation in three languages.
→ `dharma-verse-practice.skill` (zip archive containing `dharma-verse-practice/SKILL.md`)

### `english-plan-evaluator` **[exists]**
**Purpose:** QA companion to `english-plan-generator` — grade one already-written English Bodhisattva Challenge day file against every generator rule (grounding/fidelity, structure, voice, notification format). Reports pass/fail per criterion with the offending text quoted and a suggested fix; does not rewrite the day.
**Inputs:** A day file under `…/en/Days/`; the source rails it was built from (verse rails, liturgy asset, verse text, schedule).
**Outputs:** A scorecard with PASS/FAIL/N-A and severity per criterion; a day with any critical issue cannot be marked complete.
→ [`english-plan-evaluator/SKILL.md`](english-plan-evaluator/SKILL.md)

### `english-plan-from-tibetan` **[exists]**
**Purpose:** Generate a single-day English Bodhisattva Challenge session for verses that have **no** English source commentary (Chapter 2 onward), working from a user-provided English translation of the Tibetan day plan plus vault sources that do exist. Same six-section output and voice rules as `english-plan-generator`; produces options (a/b/c).
**Inputs:** The English translation of the bo day plan (pasted/attached); day number, chapter, verse range; the published Choephel English translation; the Tibetan root; the three chapter-covering Tibetan commentaries; the bo plan file; nearby day files.
**Outputs:** An English day file (options) under the `en` stream, grounded traceably in the supplied translation and Tibetan commentaries; `generation_note` flags that it was built without English rails and needs specialist review.
→ [`english-plan-from-tibetan/SKILL.md`](english-plan-from-tibetan/SKILL.md)

### `spyodjug-zh-summary` **[exists]** (packaged `.skill`)
**Purpose:** For each day of the BCA 365-day recitation plan, generate a plain-Chinese (白話) verse summary based on Ven. Longlian's (隆蓮法師) translation, and save it to the Obsidian `zh-daily-summary` folder. Packaged as a zipped `.skill` archive.
**Inputs:** The day's Tibetan verses (from the spyod-jug-365 plan); Longlian's Chinese translation; day number.
**Outputs:** A concise plain-Chinese summary markdown file in the `zh-daily-summary` folder.
→ `spyodjug-zh-summary.skill` (zip archive containing `spyodjug-zh-summary/SKILL.md`)

### `day-package-pipeline` **[exists]**
**Purpose:** Build one Bodhisattva-Challenge day-package end to end — assemble the Tibetan source-of-record file from the verse rails, plan day file, and schedule; translate it into the English package; then enforce the locked format (display-only commentator headings, His-Holiness-first order, per-section provenance) with the validator, conform, reorder, and drift-guard tools.
**Inputs:** Day number + chapter; `schedule-hhdl-birthday.md`; the per-verse rails (`2-RAILS/Verses/*-summary.md`); the plan day file under `en/Days/`; the Plain-English verse text; `_TEMPLATE.md`; `_TERMBASE.md`; the `4-SYSTEM/scripts/day-package/` tooling.
**Outputs:** A matched pair of protected files — `Day-Packages/…/<day>.md` (Tibetan source-of-record) and `Day-Packages-EN/…/<day>-en.md` (English translation) — that pass `day_package_tools.py validate`, with the guard re-baselined.
→ [`day-package-pipeline/SKILL.md`](day-package-pipeline/SKILL.md)

### `Himalayan-Plan-Transformer` **[exists]**
**Purpose:** Restructure a Himalayan-track day-plan file from the legacy 6-section Tibetan layout into the standardized 4-section layout — root verses and commentary moved to the top, refuge/bodhicitta/dedication merged into one combined section (with ཚད་མེད་བཞི dropped and a plain-verse རྩ་ཚིག subsection added), ངོ་སྤྲོད retired, the closing practice section renamed ལག་ལེན and reordered, and the རྩ་ཚིག་ངོས་འཛིན sub-heading populated by tracing each root verse to its matching-chapter ས་བཅད outline source under `bo-ཀུན་དཔལ།_རྩ་བའི་ས་བཅད་ངོས་འཛིན།/`.
**Inputs:** One target file under `3-TRANSFORMATIONS/Plans/Himalayan/<chapter-folder>/`; human confirmation on what to do with any non-empty ངོ་སྤྲོད paragraph. (No separate input needed for verse identification — the matching chapter file is selected automatically from the target's own `Ch<C>` filename segment.)
**Outputs:** The same file, overwritten in place with the four-section structure; trailing Hindi/English content preserved byte-for-byte.
→ [`Himalayan-Plan-Transformer/SKILL.md`](Himalayan-Plan-Transformer/SKILL.md)

---

## Catalog maintenance note

`plan-day-feedback-revision` **[listed above but no directory on disk]** — the entry under "Vault-specific skills" links to `plan-day-feedback-revision/SKILL.md`, but no such folder currently exists under `4-SYSTEM/Skills/`. Either the skill was removed/renamed or never committed. A human contributor should restore the skill or remove its catalog entry.

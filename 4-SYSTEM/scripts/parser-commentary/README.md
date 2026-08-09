# Parser — Commentary

Takes a linted commentary source file and produces API-ready JSON payloads for the text, edition, TOC, and alignment. Refuses any file whose `file_type` is not `commentary`; use `4-SYSTEM/scripts/parser-root-text/parser.py` for root texts, editions, or translations.

## What it does

Runs four functions:

1. **extract_text_input** — strips null/empty fields from the lint JSON and writes a clean `text.json`
2. **build_edition** — extracts content from the source `.md`, builds a segmented edition (paragraph-typed by default, with `verse`/`front_matter`/`back_matter`/`top_segment` inferred per-reference) with character-level spans, writes `edition.json`
3. **build_toc** — builds a nested table of contents from the edition's title segments (commentaries may nest multiple levels), writes `toc.json`
4. **build_alignment** — extracts segment-to-segment alignment from the commentary's Obsidian transclusion links (`![[root_or_translation_path#^ref]]`), writes `alignment.json`

## Output

```
output/
  <stem>.text.json        # clean text_input payload
  <stem>.edition.json     # edition content + segmentation
  <stem>.toc.json         # nested TOC with character spans
  <stem>.alignment.json   # commentary -> root/translation segment alignments
```

## Alignment

Transclusion links in the commentary (`![[target_path#^ref]]`) define which root or translation segment each commentary segment corresponds to.

- `source_segment_reference` — segment in the commentary
- `target_segment_reference` — segment in the file being commented on

Alignment is **inherited forward**, not block-scoped: every commentary segment after a transclusion aligns to that transclusion's target ref(s), continuing across as many following blocks as needed, until either a new transclusion appears (which replaces the active target set) or a markdown heading is reached (which clears it — a new section starts with no target context). A block that carries a transclusion and its own content ref together (e.g. a root quote right under its own `![[...]]` line) aligns immediately; a transclusion-only block (no content of its own) just sets the active target set for what follows. If two transclusions appear back to back before the next ref'd content, that content aligns to both targets.

Per the upload steps doc, alignment is submitted as:

```
PUT v2/editions/{source_edition_id}/alignments/{target_edition_id}
```

where `source_edition_id` is the commentary's own `edition_id` and `target_edition_id` is the `edition_id` of the file it transcludes (root text or translation).

## Requirements

```
pip install PyYAML pyewts
```

Requires Python 3.8+.

## How to run

Run from the project root (`bodhisattvacharyavatara-rails/`).

**Full parse (text + edition + TOC + alignment):**
```bash
python3 4-SYSTEM\scripts\parser-commentary\parser_commentary.py "1-SOURCES\Commentaries\Transcluded\BCAC14_NTS_bo_segmented.md" "4-SYSTEM\scripts\linter-commentary\output\BCAC14_NTS_bo_segmented.lint.json"
```

**Auto-resolve lint path from source filename:**
```bash
python3 4-SYSTEM\scripts\parser-commentary\parser_commentary.py "1-SOURCES\Commentaries\Transcluded\BCAC14_NTS_bo_segmented.md"
```

**Text only (from lint JSON):**
```bash
python3 4-SYSTEM\scripts\parser-commentary\parser_commentary.py "4-SYSTEM\scripts\linter-commentary\output\BCAC14_NTS_bo_segmented.lint.json"
```

## Notes

- Run `linter-commentary/lint_commentary.py` first — the parser reads `commentary_of` and other resolved fields from the lint JSON
- Blocks without a reference marker (`^ref`) are skipped with a warning
- Pure transclusion blocks (`![[...]]` only) are silently skipped — they are used for alignment, not content
- Tibetan TOC titles in Wylie are auto-converted to Unicode
- Alignment is always attempted for commentaries (unlike translations, where it's conditional) — if the commentary body has no transclusion links, `alignment.json` will simply have an empty `alignments` array

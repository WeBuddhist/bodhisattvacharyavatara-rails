# Parser — Root Text

Takes a linted source file and produces API-ready JSON payloads for the edition, TOC, and alignment.

## What it does

Runs up to four functions depending on the inputs provided:

1. **extract_text_input** — strips null/empty fields from the lint JSON and writes a clean `text.json`
2. **build_edition** — extracts content from the source `.md`, builds a segmented edition with character-level spans, writes `edition.json`
3. **build_toc** — builds a nested table of contents from the edition's title segments, writes `toc.json`
4. **build_alignment** — for `translation` and `commentary` files only, extracts segment-to-segment alignment from Obsidian transclusion links (`![[...#^ref]]`), writes `alignment.json`

## Output

```
output/
  <stem>.text.json        # clean text_input payload
  <stem>.edition.json     # edition content + segmentation
  <stem>.toc.json         # nested TOC with character spans
  <stem>.alignment.json   # source↔target segment alignments (translations/commentaries only)
```

## Alignment

Transclusion links in the source file (`![[root_text_path#^ref]]`) define which root text segment each translation/commentary segment corresponds to.

- `source_segment_reference` — segment in the translation or commentary
- `target_segment_reference` — segment in the root text

For root texts and their translations, alignment is 1-to-1.

## Requirements

```
pip install PyYAML pyewts
```

Requires Python 3.8+.

## How to run

Run from the project root (`bodhisattvacharyavatara-rails/`).

**Full parse (text + edition + TOC + alignment):**
```bash
python3 4-SYSTEM\scripts\parser-root-text\parser.py "1-SOURCES\Text\BCAV08_SH_sk.md" "4-SYSTEM\scripts\linter-root-text\output\BCAV08_SH_sk.lint.json"
```

**Text only (from lint JSON):**
```bash
python3 4-SYSTEM\scripts\parser-root-text\parser.py "4-SYSTEM\scripts\linter-root-text\output\BCAV08_SH_sk.lint.json"
```

## Notes

- Run the linter first — the parser reads `translation_of` and other resolved fields from the lint JSON
- Blocks without a reference marker (`^ref`) are skipped with a warning
- Pure transclusion blocks (`![[...]]` only) are silently skipped — they are used for alignment, not content
- Tibetan TOC titles in Wylie are auto-converted to Unicode

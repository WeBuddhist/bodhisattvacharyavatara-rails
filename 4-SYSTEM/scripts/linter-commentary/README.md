# Linter — Commentary

Validates commentary source files (`file_type: commentary`) and produces a structured JSON payload ready for the API. Refuses any file whose `file_type` is not `commentary`; use `4-SYSTEM/scripts/linter-root-text/lint_text_input.py` for root texts, editions, or translations.

## What it does

1. Reads the YAML frontmatter from the source `.md` file
2. Rejects the file if `file_type` is not `commentary`
3. Resolves `root_text` to the commented-on file, reads its `text_id`, and sets `commentary_of` automatically (unless already set) — also copies `category_id` if missing
4. Validates all required fields (`title`, `language`, `license`, `author`, `category_id`, `source`, `edition_type`, `root_text`, etc.)
5. Validates the body: every paragraph/title block needs a `^ref` marker, no duplicate refs, TOC headers start at level 1 and don't skip levels
6. Looks up the author in the persons API; if not found, searches BDRC
7. Patches the source file in place for fields that can be auto-resolved (`lang_tag`, `language`, `bdrc_work_id`, `commentary_of`, `category_id`)
8. Writes output to `output/<stem>.lint.json` on success, or `output/<stem>.lint.errors.json` on failure

## Output

```
output/
  <stem>.lint.json          # on success — contains text_input payload
  <stem>.lint.errors.json   # on failure — contains errors and notes
```

The `text_input` block in the output is what gets submitted to `POST v2/Texts`.

## Files

| File                  | Role                                                            |
| --------------------- | --------------------------------------------------------------- |
| `lint_commentary.py`  | Entry point — reads source file, resolves `commentary_of`, validates, writes output |
| `build.py`            | Builds the `text_input` payload from validated data             |
| `validate.py`         | Field-level validation rules                                    |
| `lookup.py`           | Person and BDRC work lookups via API                            |
| `constants.py`        | API endpoints, allowed values, field lists                      |
| `languages.py`        | Auto-generated language code/name mappings                      |
| `requirements.txt`    | Python dependencies                                              |

## Requirements

```
pip install -r requirements.txt
```

Requires Python 3.8+.

## How to run

Run from the project root (`bodhisattvacharyavatara-rails/`):

```bash
python3 4-SYSTEM\scripts\linter-commentary\lint_commentary.py "1-SOURCES\Commentaries\Transcluded\BCAC14_NTS_bo_segmented.md"
```

You can also pass multiple files:

```bash
python3 4-SYSTEM\scripts\linter-commentary\lint_commentary.py "1-SOURCES\Commentaries\Transcluded\*.md"
```

## Source file format

See `4-SYSTEM/Templates/FILE_YAML_PROPERTIES.md`, section 3 ("Commentary") for the required YAML properties.

`root_text` must point at whichever file the commentary's transclusion links (`![[...#^ref]]`) actually reference — that file's `text_id` is what `commentary_of` gets set to, and its `edition_id` is what the alignment step (see `parser-commentary`) targets.

## Notes

- Tibetan titles in Wylie romanization are auto-converted to Unicode in the output
- BDRC is searched by title if `bdrc_work_id` is not set
- The source file title is never overwritten by the linter
- After the text, edition, and TOC are created in the API, save the returned IDs back to the source file as `text_id`, `edition_id`, and `toc_id`
- Do not pre-fill `text_id` / `edition_id` / `toc_id` before upload — those belong to the commentary itself, not to the root text or translation it comments on

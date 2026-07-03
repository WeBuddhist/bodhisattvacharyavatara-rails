# Linter — Root Text

Validates vault source files (`.md`) and produces a structured JSON payload ready for the API.

## What it does

1. Reads the YAML frontmatter from the source `.md` file
2. Validates all required fields (`title`, `language`, `license`, `author`/`translator`, `category_id`, `source`, `edition_type`, etc.)
3. Looks up the author/translator in the persons API; if not found, searches BDRC
4. Searches BDRC for the work by title to resolve `alt_titles` and `bdrc_work_id`
5. For translation files, auto-resolves `translation_of` from the root text's `text_id`
6. For commentary files, auto-resolves `commentary_of` from the root text's `text_id`
7. Patches the source file in place for fields that can be auto-resolved (`lang_tag`, `language`, `bdrc_work_id`, `translation_of`, `category_id`)
8. Writes output to `output/<stem>.lint.json` on success, or `output/<stem>.lint.errors.json` on failure

## Output

```
output/
  <stem>.lint.json          # on success — contains text_input payload
  <stem>.lint.errors.json   # on failure — contains errors and notes
```

The `text_input` block in the output is what gets submitted to the API to create a text.

## Files

| File | Role |
|------|------|
| `lint_text_input.py` | Entry point — reads source file, runs validation, writes output |
| `build.py` | Builds the `text_input` payload from validated data |
| `validate.py` | Field-level validation rules |
| `lookup.py` | Person and BDRC work lookups via API |
| `constants.py` | API endpoints, allowed values, field lists |
| `languages.py` | Auto-generated language code/name mappings |
| `requirements.txt` | Python dependencies |

## Requirements

```
pip install -r requirements.txt
```

Requires Python 3.8+.

## How to run

Run from the project root (`bodhisattvacharyavatara-rails/`):

```bash
python3 4-SYSTEM\scripts\linter-root-text\lint_text_input.py "1-SOURCES\Text\BCAV08_SH_sk.md"
```

You can also pass multiple files or a directory:

```bash
python3 4-SYSTEM\scripts\linter-root-text\lint_text_input.py "1-SOURCES\Text\*.md"
```

## Source file format

See `4-SYSTEM/Templates/FILE_YAML_PROPERTIES.md` for the required YAML properties for each file type (`root-text`, `translation`, `commentary`).

## Notes

- Tibetan titles in Wylie romanization (e.g. `kun dpal spyod 'jug`) are auto-converted to Unicode in the output
- BDRC titles returned from lookup go into `text_input.title` and `alt_titles`; the source file title is never overwritten
- After the text, edition, and TOC are created in the API, save the returned IDs back to the source file as `text_id`, `edition_id`, and `toc_id`

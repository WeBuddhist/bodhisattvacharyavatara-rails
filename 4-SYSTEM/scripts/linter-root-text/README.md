# Linter — Root Text

Validates vault source files (`.md`) and produces a structured JSON payload ready for the API.

## What it does

1. Reads the YAML frontmatter from the source `.md` file
2. Validates required fields (`title`, `language`, `license`, `category_id`, `source`, `edition_type`, etc.). Author/translator are optional for now — missing ones produce a warning
3. Looks up the author/translator in the persons API; if not found, searches BDRC. Persons without a resolved id are skipped with a warning
4. Uses `title` and `alt_titles` from the YAML frontmatter as-is (no BDRC work search)
5. For translation files, auto-resolves `translation_of` from the root text's `text_id`
6. For commentary files, auto-resolves `commentary_of` from the root text's `text_id`
7. Patches the source file in place for fields that can be auto-resolved (`lang_tag`, `language`, `translation_of`, `category_id`)
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
| `lookup.py` | Person lookups via API / BDRC |
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
- `title` must be set in the YAML. `alt_titles` is optional for now (warning if missing). Neither is looked up from BDRC
- `alt_titles` are variants in the **same language** as the file (`lang_tag`). Use a string or a list of strings; each is wrapped with the title script tag for the API (`sa` → `sa-x-iast`; other langs use `lang_tag` as-is):

  ```yaml
  lang_tag: sa
  title: bodhisattvacaryāvatāra
  alt_titles:
    - Bodhi(sattva)caryāvatāra
    - bodhicaryāvatāra
  ```

  → `title: {"sa-x-iast": "bodhisattvacaryāvatāra"}`, `language: "sa"`
  Sanskrit title/alt text must be Latin/IAST; Devanagari is rejected with an ERROR.

- If `bdrc_work_id` (or `bdrc`) is set in the YAML, it is passed through to the API payload as `bdrc`; it is never resolved by title search
- The source file title is never overwritten by the linter
- After the text, edition, and TOC are created in the API, save the returned IDs back to the source file as `text_id`, `edition_id`, and `toc_id`

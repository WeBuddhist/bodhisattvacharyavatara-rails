---
name: translation-frontmatter
description: Generates complete YAML frontmatter for a translation file in 1-SOURCES/Translations/ by extracting metadata from the file's title page, colophon, and opening content.
version: 1.0.0
---

# Translation Frontmatter Creator

This skill populates the standard YAML frontmatter for a translation file (`file_type: translation`) in `1-SOURCES/Translations/`. It extracts all available metadata from the file's title, colophon, and opening content, then writes the complete frontmatter block according to the spec in `4-SYSTEM/Guidelines/source-formatting.md` § 4.

## Instructions

When asked to add or generate frontmatter for a translation file:

1. **Read the file.** Use the `read_file` tool on the target file. Focus on the title page, translator credits, publication information (colophon), and opening lines — do not read the entire body text.
2. **Identify the translator(s).** Record names in `Surname, Firstname` format, separated by semicolons if multiple translators. Use the name as it appears in the source.
3. **Identify the target language.** This is the language the text was translated *into*. Assign the correct `lang_tag` from § 12 of the source-formatting guidelines (e.g., `en`, `fr`, `de`).
4. **Identify the root text.** Determine which root text this is a translation of and record its vault path under `root_text`. If the corresponding file does not yet exist, leave the value as a descriptive placeholder string (e.g., `"1-SOURCES/Text/sk-root-text.md — to be created"`).
5. **Determine `verse_id_format`.** Block IDs in a translation correspond to the *source* verse numbering, not the translator's own numbering. Inspect the root text or notes to confirm the format (`chapter-verse`, `verse`, or `book-chapter-verse`).
6. **Record `translation_basis`.** Note the edition or manuscript the translator worked from, as stated in the preface or colophon.
7. **Record `covers_verses`** if the translation covers a known range (e.g., `1-1–10-58`). Omit if the range is unclear.
8. **Write the frontmatter** using the `edit_file` tool to insert or replace the YAML block at the top of the file.

## Frontmatter Template

```yaml
---
title:                        # title of the translation as it appears in the file
translator:                   # Surname, Firstname; Surname, Firstname (semicolon-separated)
date:                         # publication year or decade, e.g. 1995
language:                     # target language, e.g. English / French / German
file_type: translation
lang_tag:                     # ISO tag from § 12, e.g. en / fr / de
verse_id_format:              # chapter-verse | verse | book-chapter-verse
root_text:                    # vault path to the root text, e.g. 1-SOURCES/Text/sk-root-text.md
translation_basis:            # edition the translator worked from, e.g. "Vaidya 1960 edition"
covers_verses:                # verse range in block-ID format, e.g. 1-1–10-58 — omit if unknown
source_description:           # REQUIRED — e.g. "Oxford University Press 1995 first edition"
source_url:                   # URL if sourced digitally — leave blank if none
---
```

## Example Output

```yaml
---
title: The Bodhicaryāvatāra
translator: Crosby, Kate; Skilton, Andrew
date: 1995
language: English
file_type: translation
lang_tag: en
verse_id_format: chapter-verse
root_text: 1-SOURCES/Text/sk-root-text.md
translation_basis: Vaidya 1960 edition
covers_verses: 1-1–10-58
source_description: "Oxford University Press 1995 first edition"
source_url:
---
```

## Rules & Edge Cases

- **`source_description` is required.** Every translation file must have it. If publication data is not visible, use `"Source unknown — to be verified"`.
- **Block IDs follow the source verse, not the translator's numbering.** If the translator uses a different verse numbering system, note this with `[Ed: ...]` in the file body — the `verse_id_format` field always refers to the root text's structure.
- **`translator` not `author`.** Translations use the `translator` field, not `author`. The original author is identified via the `root_text` link.
- **`lang_tag` is the *target* language.** For an English translation, `lang_tag: en`. The source language is implicit in the `root_text` link.
- **Do not hallucinate fields.** If `translation_basis`, `covers_verses`, or `source_url` cannot be confirmed from the file, omit those fields rather than guessing.
- **Omit empty optional fields.** Do not leave placeholder values like `null` or `""` for optional fields. Either populate them or remove the key entirely.
- **Multiple translators** — list all on a single line, semicolon-separated, as they appear in the publication (e.g., `Crosby, Kate; Skilton, Andrew`).

---
name: root-text-frontmatter
description: Generates complete YAML frontmatter for a root text file in 1-SOURCES/Text/ by extracting metadata from the file's title, colophon, and opening content.
version: 1.0.0
---

# Root Text Frontmatter Creator

This skill populates the standard YAML frontmatter for a root text file (`file_type: root-text`) in `1-SOURCES/Text/`. It extracts all available metadata from the file's title, colophon, and opening lines, then writes the complete frontmatter block according to the spec in `4-SYSTEM/Guidelines/source-formatting.md` § 4.

## Instructions

When asked to add or generate frontmatter for a root text file:

1. **Read the file.** Use the `read_file` tool on the target file. Focus on the title line, the opening verse or prose, and the colophon (publication information found at the beginning or end).
2. **Determine the language and script.** Identify the primary language (Sanskrit, Tibetan, Chinese, Pāli, etc.) and the script in use (Devanāgarī, Unicode Tibetan, etc.). Assign the correct `lang_tag` from the table in § 12 of the source-formatting guidelines.
3. **Extract all available fields** (see template below). Only include external ID fields (`bdrc_work_id`, `dsbc_url`, etc.) when the values are known from the file itself — never invent them.
4. **Determine `verse_id_format`.** Inspect the file structure:
   - If verses are numbered by chapter and verse → `chapter-verse`
   - If verses carry a single sequential number → `verse`
   - If the text has books, chapters, and verses → `book-chapter-verse`
5. **Count or estimate** `chapters` and `total_verses` if the file makes them clear. Leave empty if uncertain.
6. **Populate `related_commentaries` and `related_translations`** only if corresponding files already exist in `1-SOURCES/`. Use full vault paths.
7. **Write the frontmatter** using the `edit_file` tool to insert or replace the YAML block at the top of the file.

## Frontmatter Template

```yaml
---
title:                        # exact title as it appears in the file (diacritics OK)
author:                       # original author name (diacritics OK)
date:                         # date or century of composition, e.g. "8th century CE"
language:                     # full language name, e.g. Sanskrit / Tibetan / Chinese
script:                       # script name, e.g. Devanāgarī / Unicode Tibetan
file_type: root-text
lang_tag:                     # ISO tag from § 12, e.g. sk / bo / zh / pi
chapters:                     # integer — omit if unknown
total_verses:                 # integer — omit if unknown
verse_id_format:              # chapter-verse | verse | book-chapter-verse
source_description:           # REQUIRED — e.g. "Transcribed from Vaidya 1960 critical edition"
source_url:                   # URL if sourced digitally — leave blank if none
dsbc_url:                     # DSBC entry URL — omit if not applicable
bdrc_work_id:                 # e.g. WA1KG13126 — omit if unknown
bdrc_instance_id:             # omit if unknown
gretil_url:                   # GRETIL URL — omit if not applicable
cbeta_id:                     # Chinese Buddhist canon — omit if not applicable
suttacentral_id:              # Pāli texts — omit if not applicable
acip_id:                      # Tibetan ACIP — omit if not applicable
other_ids:                    # VIAF, Wikidata, etc. — omit if none
related_commentaries:         # list of vault paths — omit if none yet
related_translations:         # list of vault paths — omit if none yet
---
```

## Example Output

```yaml
---
title: Bodhicaryāvatāra
author: Śāntideva
date: 8th century CE
language: Sanskrit
script: Devanāgarī
file_type: root-text
lang_tag: sk
chapters: 10
total_verses: 913
verse_id_format: chapter-verse
source_description: "Transcribed from Vaidya 1960 critical edition"
source_url: https://www.dsbcproject.org/canon-text/content/71
dsbc_url: https://www.dsbcproject.org/canon-text/content/71
bdrc_work_id: WA1KG13126
related_commentaries:
  - 1-SOURCES/Commentaries/prajnakaramati-sk.md
  - 1-SOURCES/Commentaries/kunzang-pelden-bo.md
related_translations:
  - 1-SOURCES/Translations/crosby-en.md
  - 1-SOURCES/Translations/bo-lobzang-sherab.md
---
```

## Rules & Edge Cases

- **`source_description` is required.** Every root text file must have it. If no publication data is visible, use a minimal description such as `"Source unknown — to be verified"`.
- **Do not hallucinate external IDs.** If a BDRC, GRETIL, DSBC, or other ID is not visible in the file, omit that field entirely.
- **One script per file.** If the file contains an alternative script (e.g., IAST alongside Devanāgarī), note the discrepancy with `[Ed: ...]` — do not add a second script tag.
- **`lang_tag` follows § 12.** Default tags: Sanskrit → `sk`, Tibetan → `bo`, Chinese → `zh`, Pāli → `pi`. For editions in alternative scripts append the suffix (e.g., `sk-iast`).
- **Omit empty optional fields.** Do not leave placeholder values like `null` or `""` for optional fields. Either populate them or remove the key entirely.
- **`related_commentaries` / `related_translations`** — list only files that already exist in the vault. Do not pre-populate with anticipated future files.

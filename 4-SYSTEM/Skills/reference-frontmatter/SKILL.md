---
name: reference-frontmatter
description: Generates complete YAML frontmatter for a secondary literature or reference file in 1-SOURCES/References/ by extracting metadata from the file's title page, colophon, and opening content.
version: 1.0.0
---

# Reference / Secondary Literature Frontmatter Creator

This skill populates the standard YAML frontmatter for a secondary literature or reference file (`file_type: secondary-literature`) in `1-SOURCES/References/`. It extracts all available metadata from the file's title page, colophon, and opening content, then writes the complete frontmatter block according to the spec in `4-SYSTEM/Guidelines/source-formatting.md` § 4.

## Instructions

When asked to add or generate frontmatter for a reference or secondary literature file:

1. **Read the file.** Use the `read_file` tool on the target file. Focus on the title page, author credits, publication information (colophon), table of contents, and any abstract or introduction — do not read the entire body.
2. **Identify the author(s).** Record names in `Surname, Firstname` format. Use the name as it appears in the publication. If multiple authors, list them separated by semicolons.
3. **Identify the language.** This is the language the work is written *in* (usually English for modern scholarship). Assign the correct `lang_tag` from § 12 of the source-formatting guidelines.
4. **Identify the primary root text** the work relates to, if applicable, and record its vault path under `root_text`. If the work spans multiple texts or is not focused on a specific text, omit this field.
5. **Extract `topics`.** List the main subjects the work addresses — chapter references, doctrinal topics, textual traditions, etc. — as a YAML list. Draw from the table of contents or abstract.
6. **Record the `source_description`.** Include publisher, year, and edition as they appear in the colophon or title page.
7. **Record `source_url`** if the work was sourced digitally (DOI, stable URL, etc.).
8. **Write the frontmatter** using the `edit_file` tool to insert or replace the YAML block at the top of the file.

## Frontmatter Template

```yaml
---
title:                        # exact title of the work (diacritics OK, use quotes if needed)
author:                       # Surname, Firstname; Surname, Firstname (semicolon-separated)
date:                         # publication year, e.g. 2017
language:                     # language the work is written in, e.g. English
file_type: secondary-literature
lang_tag:                     # ISO tag from § 12, e.g. en / fr / de
root_text:                    # vault path to the primary root text — omit if not applicable
topics:                       # list of subjects covered, e.g. [bodhicitta, chapter 6, patience]
source_description:           # REQUIRED — e.g. "Oxford University Press 2017"
source_url:                   # URL or DOI if sourced digitally — leave blank if none
---
```

## Example Output

```yaml
---
title: "Śāntideva and the Bodhicaryāvatāra"
author: Crosby, Kate
date: 2017
language: English
file_type: secondary-literature
lang_tag: en
root_text: 1-SOURCES/Text/sk-root-text.md
topics: [bodhicitta, chapter 6, patience]
source_description: "Oxford University Press 2017"
source_url: https://doi.org/10.1093/example
---
```

## Rules & Edge Cases

- **`source_description` is required.** Every reference file must have it. If publication data is not visible, use `"Source unknown — to be verified"`.
- **Titles with special characters** — wrap the `title` value in double quotes if it contains colons, Devanāgarī, or other YAML-special characters.
- **`root_text` is optional.** Reference works that cover broad topics or multiple texts need not link to a single root text. Omit the field rather than leaving it blank.
- **`topics` should be concise and useful.** Draw entries from the work's own table of contents, chapter titles, or keywords. Use lowercase, natural-language terms. Aim for 3–8 entries.
- **`author` not `translator`.** Secondary literature always uses `author`. If a work is both an edition and a study, still use `author`.
- **`lang_tag` is the language the secondary work is *written in***, not the language of the primary source it studies. A French article on Sanskrit texts gets `lang_tag: fr`.
- **Do not hallucinate DOIs or URLs.** If a stable URL or DOI is not visible in the file, leave `source_url` blank.
- **Omit empty optional fields.** Do not leave placeholder values like `null` or `""` for optional fields. Either populate them or remove the key entirely.
- **Dictionaries and reference tools** (e.g., Monier-Williams, Negi) also use `file_type: secondary-literature`. For these, `topics` may list the languages or domains covered (e.g., `[Sanskrit lexicon, Tibetan lexicon]`).

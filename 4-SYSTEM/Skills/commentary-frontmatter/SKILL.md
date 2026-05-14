---
name: commentary-frontmatter
description: Generates complete YAML frontmatter for a commentary file in 1-SOURCES/Commentaries/ by extracting metadata from the file's title, colophon, and opening content.
version: 1.0.0
---

# Commentary Frontmatter Creator

This skill populates the standard YAML frontmatter for a commentary file (`file_type: commentary`) in `1-SOURCES/Commentaries/`. It extracts all available metadata from the file's title, colophon, and opening content, then writes the complete frontmatter block according to the spec in `4-SYSTEM/Guidelines/source-formatting.md` § 4.

## Instructions

When asked to add or generate frontmatter for a commentary file:

1. **Read the file.** Use the `read_file` tool on the target file. Focus on the title line, author credits, colophon (publication information at the beginning or end), and opening lines — do not read the entire body.
2. **Identify the language and script.** Determine the primary language of the commentary (which may differ from the root text) and its script. Assign the correct `lang_tag` from § 12 of the source-formatting guidelines.
3. **Assign a `registered_id`.** This is the short, stable identifier used in `2-RAILS/` to attribute claims to this commentary. Derive it from the author's surname in lowercase, romanised without diacritics (e.g., `prajnakaramati`, `kunzangpelden`). Once set it must never change. Check `4-SYSTEM/CLAUDE.md` to confirm the ID is not already taken.
4. **Identify the root text.** Record the vault path of the root text this commentary addresses under `root_text`.
5. **Determine `verse_id_format`.** This field declares the commentary's *own* internal numbering system — not the root text's system. Inspect how the commentary structures its own divisions:
   - Chapter + verse → `chapter-verse`
   - Section + paragraph → `section-paragraph`
   - Single sequential verse/passage number → `verse`
   - Folio + line → `folio-line`
   - Book + chapter + verse → `book-chapter-verse`
   If the commentary has no internal numbering, use `verse` and apply sequential numbering.
6. **Record `covers_verses`** — the range of root text verses this commentary addresses, in block-ID format (e.g., `1-1–10-58`). Omit if the range is unclear.
7. **Add external IDs** (BDRC, GRETIL, etc.) only when they are visible in the file itself.
8. **Write the frontmatter** using the `edit_file` tool to insert or replace the YAML block at the top of the file.

## Frontmatter Template

```yaml
---
title:                        # exact title of the commentary (diacritics OK)
author:                       # commentary author (diacritics OK)
date:                         # date or century of composition, e.g. "11th century CE"
language:                     # language of the commentary, e.g. Sanskrit / Tibetan / English
script:                       # script name — omit for roman-script languages
file_type: commentary
lang_tag:                     # ISO tag from § 12, e.g. sk / bo / en
verse_id_format:              # the commentary's own ID system (see § 8 of source-formatting)
registered_id:                # short stable ID used in 2-RAILS/ — lowercase, no diacritics
root_text:                    # vault path to the root text, e.g. 1-SOURCES/Text/sk-root-text.md
covers_verses:                # root text verse range, e.g. 1-1–10-58 — omit if unknown
source_description:           # REQUIRED — e.g. "Transcribed from La Vallée Poussin edition 1901–1914"
source_url:                   # URL if sourced digitally — leave blank if none
bdrc_work_id:                 # omit if unknown
bdrc_instance_id:             # omit if unknown
gretil_url:                   # GRETIL URL — omit if not applicable
dsbc_url:                     # DSBC URL — omit if not applicable
cbeta_id:                     # Chinese Buddhist canon — omit if not applicable
acip_id:                      # Tibetan ACIP — omit if not applicable
other_ids:                    # VIAF, Wikidata, etc. — omit if none
---
```

## Example Output

```yaml
---
title: Bodhicaryāvatārapañjikā
author: Prajñākaramati
date: 11th century CE
language: Sanskrit
script: Devanāgarī
file_type: commentary
lang_tag: sk
verse_id_format: chapter-verse
registered_id: prajnakaramati
root_text: 1-SOURCES/Text/sk-root-text.md
covers_verses: 1-1–10-58
source_description: "Transcribed from La Vallée Poussin edition 1901–1914"
bdrc_work_id: WA1KG14159
gretil_url: https://gretil.sub.uni-goettingen.de/gretil/1_sanskr/6_sastra/3_phil/buddh/bsa052_u.htm
---
```

## Rules & Edge Cases

- **`source_description` is required.** Every commentary file must have it. If publication data is not visible, use `"Source unknown — to be verified"`.
- **`registered_id` must be unique and stable.** Check `4-SYSTEM/CLAUDE.md` before assigning. Once a commentary is used in any `2-RAILS/` file, the `registered_id` must never change. After writing the frontmatter, remind the user to register the new ID in `4-SYSTEM/CLAUDE.md`.
- **`verse_id_format` is the commentary's own system, not the root text's.** A Tibetan commentary may use `folio-line` even though the Sanskrit root text uses `chapter-verse`. Both coexist — the root text transclusions in the commentary body carry the root text's block IDs, while the commentary's own passages carry its own IDs.
- **`script` field** — include for non-roman scripts (Devanāgarī, Unicode Tibetan, etc.). Omit for languages written in the Latin alphabet (English, French, etc.).
- **Do not hallucinate external IDs.** If a BDRC, GRETIL, or other ID is not visible in the file, omit that field entirely.
- **Omit empty optional fields.** Do not leave placeholder values like `null` or `""` for optional fields. Either populate them or remove the key entirely.

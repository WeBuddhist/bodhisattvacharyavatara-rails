# Vault Source File Guide

This document defines what YAML properties are required when creating source files in the vault. Each file's `file_type` determines which fields are needed.

> **Note:** Once the text, edition, and TOC are created in the system, save their assigned IDs back to the file as `text_id`, `edition_id`, and `toc_id`. This applies to all file types. Translations and commentaries should also copy the `category_id` from the root text.

---

## 1. Root Text (`file_type: root-text`)

A root text is the primary source — the original Sanskrit, Tibetan, Pali, or other canonical text.

### Required Properties

| Property                 | Description                                                                                                                                         | Example                               |
| ------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------- |
| `file_type`              | Must be `root-text`                                                                                                                                 | `file_type: root-text`                |
| `title`                  | Title in the source language                                                                                                                        | `title: bodhisattvacaryāvatāra`       |
| `language` or `lang_tag` | Full language name **or** BCP47 code — at least one required. Both recommended.                                                                     | `language: Sanskrit` / `lang_tag: sa` |
| `category_id`            | Unique ID for this work in the API                                                                                                                  | `category_id: JD5ULLPAV1cxg7RSb7L3q`  |
| `license`                | Copyright status                                                                                                                                    | `license: public`                     |
| `author`                 | Author name(s), separated by semicolons. Attach a BDRC or OpenPecha ID using `[bdrc:ID]` or `[op:ID]`. Names in parentheses are treated as aliases. | `author: Śāntideva [bdrc:P1583]`      |
| `source`                 | URL of the source edition used                                                                                                                      | `source: https://webuddhist.com/`     |
| `edition_type`           | `critical`, `diplomatic`, or `collated`                                                                                                             | `edition_type: critical`              |

### Recommended Properties

| Property       | Description                                                                                                                                                                                                                                                                                                           | Example                                  |
| -------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------- |
| `bdrc_work_id` | BDRC work ID for this text — passed through to the API as `bdrc`. Not used to look up titles.                                                                                                                                                                                                                       | `bdrc_work_id: WA19740`                  |
| `alt_titles`   | Alternative titles in the **same language** as the file (unique variants only — do not repeat `title`). A single string, or a YAML list of strings. The linter wraps each with the title script tag (`sa` → `sa-x-iast`; otherwise `lang_tag`). | see format below                         |

**`alt_titles` format**

All variants must be in the file's language (e.g. Sanskrit file → Sanskrit/IAST alts; English translation → English alts). YAML stays plain strings; the linter adds the script key.

```yaml
# single
alt_titles: bodhicaryāvatāra

# multiple — each entry is a distinct variant
alt_titles:
  - Bodhi(sattva)caryāvatāra
  - bodhicaryāvatāra
```

For Sanskrit (`lang_tag: sa`), payload keys are `sa-x-iast` while `language` remains `sa`. Titles must be written in Latin/IAST (not Devanagari) — the linter errors if Devanagari is found:

```json
"language": "sa",
"title": { "sa-x-iast": "bodhisattvacaryāvatāra" },
"alt_titles": [
  { "sa-x-iast": "Bodhi(sattva)caryāvatāra" },
  { "sa-x-iast": "bodhicaryāvatāra" }
]
```

### Optional Properties

| Property | Description |
|----------|-------------|
| `date` | Date of composition (approximate or attested) |
| `tag_ids` | Array of classification tag IDs |
| `source_description` | Human-readable note about the source edition |

### Example

```yaml
---
title: bodhisattvacaryāvatāra
author: Śāntideva
language: Sanskrit
lang_tag: sa
file_type: root-text
category_id: JD5ULLPAV1cxg7RSb7L3q
bdrc_work_id: WA19740
alt_titles:
  - Bodhi(sattva)caryāvatāra
  - bodhicaryāvatāra
source: https://webuddhist.com/
license: public
edition_type: critical
---
```

---

## 2. Translation of a Root Text (`file_type: translation`)

A translation file renders the root text in another language. The root text file path links the two together.

### Required Properties

| Property | Description | Example |
|----------|-------------|---------|
| `file_type` | Must be `translation` | `file_type: translation` |
| `root_text` | Relative path to the root text file being translated | `root_text: 1-SOURCES/Text/sk-dev.md` |
| `title` | Title in the translation language | `title: ཀུན་དཔལ་སྤྱོད་འཇུག` |
| `language` | Full language name | `language: Tibetan` |
| `lang_tag` | BCP47 code for the translation language | `lang_tag: bo` |
| `category_id` | Copy from the root text | `category_id: JD5ULLPAV1cxg7RSb7L3q` |
| `license` | Copyright status | `license: public` |
| `translator` | Translator name(s), separated by semicolons. Attach a BDRC or OpenPecha ID using `[bdrc:ID]` or `[op:ID]`. Names in parentheses are treated as aliases. For AI translations, use the model name with an OpenPecha ID. | `translator: Blo ldan shes rab [bdrc:P5678]; David Karma (bhikshu Karma Lodrö Choephel) [bdrc:P1234]; Claude Opus 4 [op:OP_ABC123]` |
| `source` | URL of the source translation used | `source: https://webuddhist.com/` |
| `alt_titles` | Alternative titles in the **same language** as this translation (`lang_tag`). A single string, or a YAML list of unique variants (do not repeat `title`). | `alt_titles: སྤྱོད་འཇུག` |

> **Note:** `translation_of` is auto-resolved by the linter. It follows the `root_text` path to the source file and reads its `text_id`.

### Recommended Properties

| Property | Description | Example |
|----------|-------------|---------|
| `bdrc_work_id` | BDRC work ID for this specific translation — passed through as `bdrc`; not used to look up titles | `bdrc_work_id: WA00KG0545` |
| `edition_type` | `critical`, `diplomatic`, or `collated` | `edition_type: critical` |

### Optional Properties

| Property | Description |
|----------|-------------|
| `date` | Date of translation |
| `tag_ids` | Classification tag IDs |
| `source_description` | Note on the translation source |

### Tibetan Title Note

If the title is in Wylie romanization (e.g. `kun dpal spyod 'jug`), the linter and parser will auto-convert it to Tibetan Unicode (`ཀུན་དཔལ་སྤྱོད་འཇུག`) in the output. You may write the title in either script.

### Example

```yaml
---
title: ཀུན་དཔལ་སྤྱོད་འཇུག
translator: Sarvajñādeva; Bande Paltsek; Blo ldan shes rab
language: Tibetan
lang_tag: bo
file_type: translation
root_text: 1-SOURCES/Text/sk-dev.md
category_id: JD5ULLPAV1cxg7RSb7L3q
bdrc_work_id: WA00KG0545
alt_titles: སྤྱོད་འཇུག
source: https://webuddhist.com/
license: public
covers_verses: 1-1–10-61
---
```

---

## 3. Commentary (`file_type: commentary`)

A commentary is a separate authored work that explains or expands on a root text or a translation. Its body uses paragraphs rather than verses.

### Required Properties

| Property | Description | Example |
|----------|-------------|---------|
| `file_type` | Must be `commentary` | `file_type: commentary` |
| `root_text` | Relative path to the file being commented on — can be a root text or a translation | `root_text: 1-SOURCES/Text/sk-dev.md` |
| `title` | Title of this commentary | `title: Bodhicaryāvatārapañjikā` |
| `language` | Full language name | `language: Sanskrit` |
| `lang_tag` | BCP47 language code | `lang_tag: sa` |
| `category_id` | Copy from the root text | `category_id: JD5ULLPAV1cxg7RSb7L3q` |
| `license` | Copyright status | `license: public` |
| `author` | Author(s), separated by semicolons. Attach a BDRC or OpenPecha ID using `[bdrc:ID]` or `[op:ID]`. | `author: Prajñākaramati [bdrc:P1234]` |
| `source` | URL of the source edition | `source: https://...` |
| `edition_type` | `critical`, `diplomatic`, or `collated` | `edition_type: critical` |

> **Note:** `commentary_of` is auto-resolved by the linter from the `root_text` file's `text_id`, the same way `translation_of` works for translations.

### Recommended Properties

| Property | Description |
|----------|-------------|
| `bdrc_work_id` | BDRC work ID for this commentary — passed through as `bdrc`; not used to look up titles |
| `alt_titles` | Alternative titles in the **same language** as `lang_tag`. A single string, or a YAML list of unique variants (same format as root text). |

### Optional Properties

| Property | Description |
|----------|-------------|
| `date` | Date of composition |
| `tag_ids` | Classification tag IDs |
| `source_description` | Note on the source edition |

### Example

```yaml
---
title: Bodhicaryāvatārapañjikā
author: Prajñākaramati
language: Sanskrit
lang_tag: sa
file_type: commentary
root_text: 1-SOURCES/Text/sk-dev.md
bdrc_work_id: WA...
alt_titles: bodhicaryāvatāra-pañjikā
source: https://...
license: public
edition_type: critical
---
```

---

## 4. Translation of a Commentary (`file_type: translation`)

Same structure as a root-text translation, but the `root_text` points to a commentary file instead of a root text file. The linter detects the difference automatically from the root file's `file_type`.

### Required Properties

| Property | Description | Example |
|----------|-------------|---------|
| `file_type` | Must be `translation` | `file_type: translation` |
| `root_text` | Relative path to the commentary file being translated | `root_text: 1-SOURCES/Commentary/sk-panjika.md` |
| `title` | Title of this translation | |
| `language` | Full language name | `language: Tibetan` |
| `lang_tag` | BCP47 code | `lang_tag: bo` |
| `category_id` | Same category_id as the commentary | |
| `license` | Copyright status | `license: public` |
| `translator` | Translator name(s), semicolons for multiple | |
| `source` | URL of the source used | |

> **Note:** `translation_of` and `commentary_of` are auto-resolved by the linter from the root commentary file. Do not set them manually.

### Recommended & Optional Properties

Same as for root-text translations (see Section 2).

### Example

```yaml
---
title: <Tibetan title>
translator: <Translator Name>
language: Tibetan
lang_tag: bo
file_type: translation
root_text: 1-SOURCES/Commentary/sk-panjika.md
category_id: <same as commentary's category_id>
source: https://...
license: public
---
```

---

## Body Format (all types)

Headers must be properly structured: start with level 1 (`#`) and do not skip levels.

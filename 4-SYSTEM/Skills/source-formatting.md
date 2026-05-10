# 1-SOURCES — File Format and Linking Guidelines

Formatting rules for all files in `1-SOURCES/`. Read this before adding any file to the folder.

For the LLM-facing distillation of these rules see `4-SYSTEM/CLAUDE.md` Sections 3 and 5.

---

## 1. Principles

**Single source of truth.** Every text, translation, and commentary lives in one file. Obsidian block IDs make individual verses linkable without splitting files.

**Language tags everywhere.** Every file carrying material in a specific language carries a language tag suffix. See Section 14 for the full tag list.

**Flat file structure.** Root texts, editions, translations, and commentaries are single files placed directly in their subfolder — no subfolder per file.

**No interpretation in this folder.** Files in `1-SOURCES/` contain human-produced material exactly as received — formatted and annotated for navigation, but not interpreted. The only additions permitted are:

- Block ID anchors
- Frontmatter metadata
- Internal navigation links
- Editorial notes marked explicitly as `[Ed: ...]`

Any interpretive claim — compound analysis, sense assignment, syntactic reading — belongs in `2-RAILS/`, not here.

**Standard scripts by language.** Root text files use the following script conventions:

| Language | Root text script | Notes |
|---|---|---|
| Sanskrit | Devanāgarī | IAST goes in a separate edition file — recommended but not required |
| Pāli | Pāli romanisation with diacritics | No alternative script in root text |
| Tibetan | Unicode Tibetan script | Wylie goes in a separate edition file |
| Chinese | Unicode (Traditional or Simplified) | Pinyin in edition file if needed |

One script per file. Alternative script forms always go in a separate edition file.

---

## 2. Folder Structure

```
1-SOURCES/
├── Text/                            # root text(s) of the primary language(s)
│   └── [lang]-root-text.md
├── Commentaries/                    # authored commentaries
│   └── [lang]-[commentary-name].md
├── Translations/                    # translations into other languages
│   └── [lang]-[translator-surname].md
└── References/                      # secondary literature, dictionaries
    └── [author-surname]-[short-title]-[lang].md
```

**Naming rules:**

- All filenames lowercase, hyphenated, no diacritics in filename
- Diacritics used freely inside file content and frontmatter
- Script-only editions (no named editor) are named by script: `iast-sk-iast.md`, `wylie-bo-wy.md`
- Devanāgarī is never an edition for Sanskrit — it is the root text script; IAST goes as a separate file

---

## 3. Source Identification and External IDs

Every file must record its source and any relevant external database identifiers. This is essential for verification and for connecting the project to the broader scholarly infrastructure.

### Source Fields in Frontmatter

```yaml
source_description: "Transcribed from Vaidya 1960 critical edition, pp. 1–219"
source_url: https://www.dsbcproject.org/canon-text/content/71
bdrc_work_id: WA1KG13126
bdrc_instance_id: MW1KG13126
cbeta_id:                       # for Chinese texts
gretil_url: https://gretil.sub.uni-goettingen.de/...
dsbc_url: https://www.dsbcproject.org/...
suttacentral_id:                # for Pāli texts
acip_id:                        # for Tibetan texts
other_ids:
  - "VIAF: 123456"
  - "Wikidata: Q12345"
```

Include only the fields that apply. Leave inapplicable fields out entirely. `source_description` is required for every file — all others are conditional.

### Key External Databases

| Database     | Scope                   | Field                              |
| ------------ | ----------------------- | ---------------------------------- |
| BDRC         | Tibetan, Sanskrit, Pāli | `bdrc_work_id`, `bdrc_instance_id` |
| CBETA        | Chinese Buddhist canon  | `cbeta_id`                         |
| GRETIL       | Sanskrit texts          | `gretil_url`                       |
| DSBC         | Sanskrit Buddhist canon | `dsbc_url`                         |
| SuttaCentral | Pāli, translations      | `suttacentral_id`                  |
| ACIP         | Tibetan                 | `acip_id`                          |
| VIAF         | Authors and works       | in `other_ids`                     |
| Wikidata     | Works and concepts      | in `other_ids`                     |

---

## 4. Frontmatter

### Root Text Frontmatter

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

`verse_id_format` declares how block IDs are structured in this file:

| Value                | Block ID format       | Example  |
| -------------------- | --------------------- | -------- |
| `verse`              | `^verse`              | `^33`    |
| `chapter-verse`      | `^chapter-verse`      | `^6-33`  |
| `book-chapter-verse` | `^book-chapter-verse` | `^1-1-1` |

### Translation Frontmatter

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

### Commentary Frontmatter

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

The `registered_id` field is the short identifier used in `2-RAILS/` to attribute claims to this commentary. Once assigned it never changes. New commentaries must be registered in `4-SYSTEM/CLAUDE.md` before their registered_id is used in any rail file.

### Reference / Secondary Literature Frontmatter

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

---

## 5. Block IDs and Verse Structure

Obsidian block IDs placed at the end of a verse are the sole verse-level linking mechanism across the entire project.

### Block ID Format

| Text structure | Format | Example |
|---|---|---|
| Chapters + verses | `^chapter-verse` | `^6-33` |
| Verses only | `^verse` | `^33` |
| Books + chapters + verses | `^book-chapter-verse` | `^1-1-1` |

Numbers are **never zero-padded**. Use natural numbers: `^6-33` not `^06-033`.

The block ID is placed on the **last line of the verse**, after the final character, with a single space before the caret:

```
bodhisattvapadaprāptiṃ vakṣyāmi śāstrasaṅgraham || ^1-1
```

For multi-line prose passages in commentaries, the block ID goes on the last line of the passage that corresponds to that root verse.

### Chapter and Section Headings

Author-defined structural divisions map directly to the Markdown heading hierarchy. If the author provided a table of contents, its entries define the headings.

```markdown
## Chapter 6: Kṣānti — Patience

### 6.1 The harm of anger

### 6.2 The cultivation of patience
```

- `##` — author-defined books or chapters
- `###` — author-defined sub-sections (from the author's own TOC)
- `####` — not used; block IDs replace verse-level headings

**Sub-sections do not affect verse IDs.** Verses beneath a `###` heading still use `^chapter-verse` block IDs, not `^chapter-section-verse`. Sub-section headings are for navigation only.

Never use headings for editor-imposed divisions. If an edition or translator adds section titles not present in the original, note them as `[Ed: ...]` inline.

### Verse Numbering

Verse numbers restart at 1 for each chapter. `^6-33` means chapter 6, verse 33 of that chapter — not the 33rd verse of the whole text.

This applies even when the source edition uses continuous verse numbering across the whole text. Always convert to per-chapter numbering for block IDs. Record the edition's continuous number in an editorial note if useful:

```
bodhisattvapadaprāptiṃ vakṣyāmi śāstrasaṅgraham || ^1-1
[Ed: continuous verse number 1 in Vaidya 1960]
```

### Pre-Chapter Content — Chapter 0

Content that precedes Chapter 1 — colophons, title lines, homage verses, scribal introductions — is placed under a `## 0. Introduction` heading and its verses are numbered `^0-verse`.

This keeps the `^chapter-verse` system fully consistent: chapter 0 is the pre-chapter layer, chapter 1 is the first authored chapter. The convention applies to root texts, translations, and commentaries alike.

Example — Tibetan root text:

```markdown
## 0. Introduction

༄། །བྱང་ཆུབ་སེམས་དཔའི་སྤྱོད་པ་ལ་འཇུག་པ་བཞུགས་སོ། ། ^0-1
༄༅༅། །རྒྱ་གར་སྐད་དུ། བོ་དྷི་སཏྭ་ཙརྱ་ཨ་བ་ཏཱ་ར། ^0-2

## 1. ལེའུ་དང་པོ།

བདེ་གཤེགས་ཆོས་ཀྱི་སྐུ་མངའ་སྲས་བཅས་དང་། །
ཕྱག་འོས་ཀུན་ལའང་གུས་པར་ཕྱག་འཚལ་ཏེ། །
བདེ་གཤེགས་སྲས་ཀྱི་སྡོམ་ལ་འཇུག་པ་ནི། །
ལུང་བཞིན་མདོར་བསྡུས་ནས་ནི་བརྗོད་པར་བྱ། ། ^1-1
```

**What counts as pre-chapter content:**

- Title lines and colophons
- Sanskrit title transliteration and Tibetan translation of the title
- Homage formulas added by translators or scribes
- Scribal or editorial introductions not authored by the text's primary author
- Any unnumbered material that precedes the first chapter heading

**What does not go in Chapter 0:**

- Author-written prefaces that the author numbered as Chapter 1 — these are Chapter 1 regardless of content
- Editor footnotes or apparatus — these are `[Ed: ...]` notes, not verses

---

## 6. File Format — Root Text

### Sanskrit (Devanāgarī)

Devanāgarī is the standard script for all Sanskrit root texts. IAST goes in a separate file in `Text/` named `iast-sk-iast.md`.

```markdown
---
[frontmatter]
---

## 0. Introduction

## 1. बोधिचित्तानुशंस

सुगतान् सगणान् नत्वा धर्मकायादिगोचरान् ।
बोधिसत्त्वपदप्राप्तिं वक्ष्यामि शास्त्रसङ्ग्रहम् ॥ ^1-1

इदं हि बुद्धपुत्राणां मनोऽभिरमयिष्यति ।
सम्यक् प्रतिपन्नानां श्रद्धा च वर्धयिष्यति ॥ ^1-2
```

**Verse separation:** one blank line between verses.

**Half-verse markers in IAST:** `|` at the caesura, `||` at verse end. Do not create separate block IDs for half-verses.

### Pāli

```markdown
---
[frontmatter]
---

## 1. Kusalā Dhammā

katame dhammā kusalā? yasmiṃ samaye kāmāvacaraṃ kusalaṃ cittaṃ uppannaṃ hoti
somanassasahagataṃ ñāṇasampayuttaṃ... ^1
```

### Tibetan (Unicode)

Unicode Tibetan script is the standard for Tibetan root texts. Wylie transliteration goes in a separate edition file.

```markdown
---
[frontmatter]
---

## 0. Introduction

༄། །བྱང་ཆུབ་སེམས་དཔའི་སྤྱོད་པ་ལ་འཇུག་པ་བཞུགས་སོ། ། ^0-1

## 1. བྱང་ཆུབ་སེམས་ཀྱི་ཡོན་ཏན་བསྟོད་པ།

བདེ་གཤེགས་ཆོས་ཀྱི་སྐུ་མངའ་སྲས་བཅས་དང་། །
ཕྱག་འོས་ཀུན་ལའང་གུས་པར་ཕྱག་འཚལ་ཏེ། ། ^1-1
```

---

## 7. File Format — Translations

Same block ID system as the root text. Block IDs correspond to the **source verse**, not to any numbering the translator may use.

```markdown
---
[frontmatter]
---

## Chapter 1: The Excellence of Bodhicitta

Having paid homage to the Sugatas together with their retinues,
whose scope encompasses the dharmakāya and so forth,
I shall set forth a compendium of practice
for the attainment of the bodhisattva stage. ^1-1

[Trans: "dharmakāya" retained untranslated; see Crosby & Skilton 1995 p. 3.]
```

Where a translation combines multiple source verses, use the first verse's block ID and note the range:

```markdown
[combined translation of verses 1-1 and 1-2] ^1-1
[Ed: this rendering covers source verses 1-1 and 1-2 together]
```

---

## 8. File Format — Commentaries

A commentary is an independent authored work. It has:

- Its own TOC headings (`##`/`###`) drawn from the commentary author's own chapter and section titles — independent of the root text heading structure
- Its own block IDs following whatever structural system the commentary author defined — declared in `verse_id_format` frontmatter
- Transclusions of the root verse(s) each section addresses, anchoring the commentary to the root text's block ID system

### verse_id_format for Commentaries

The `verse_id_format` field declares the commentary's own ID system:

| Commentary structure | verse_id_format value | Example block ID |
|---|---|---|
| Chapter + verse | `chapter-verse` | `^3-12` |
| Section + paragraph | `section-paragraph` | `^4-2` |
| Verse only | `verse` | `^145` |
| Folio + line | `folio-line` | `^23b-4` |
| Book + chapter + verse | `book-chapter-verse` | `^2-1-4` |

Use whatever system the commentary author defined. If the commentary has no internal numbering, use sequential `verse` format.

### Format — Without Transclusions

```markdown
---
[frontmatter — verse_id_format: book-chapter-verse]
---

## 1. Commentary on Chapter 1

### 1.1 Introduction to Chapter 1

General introduction to chapter 1. ^1-1-1
General introduction continued. ^1-1-2

### 1.2 Verses 1–5 — Overview

Introductory overview of the first five verses. ^1-2-1

### 1.3 Verse-by-verse commentary

Commentary on first verse. ^1-3-1
Commentary on first verse continued. ^1-3-2

Commentary on second verse. ^1-3-3
```

### Format — With Transclusions

Transclusions anchor the commentary to the root text. They are placed where root verses become relevant — not mechanically at the top of every section.

- **Sections introducing a group of verses:** transclude all verses in the group in sequence at the opening, before the commentary text.
- **Verse-by-verse sections:** one transclusion per verse, immediately before the commentary on that verse.
- **Introductory sections with no specific verse reference:** no transclusion.

```markdown
---
[frontmatter — verse_id_format: book-chapter-verse]
---

## 1. Commentary on Chapter 1

### 1.1 Introduction to Chapter 1

General introduction to chapter 1. ^1-1-1

### 1.2 Verses 1–5 — Overview

![[1-SOURCES/Text/sk-root-text.md#^1-1]]
![[1-SOURCES/Text/sk-root-text.md#^1-2]]
![[1-SOURCES/Text/sk-root-text.md#^1-3]]
![[1-SOURCES/Text/sk-root-text.md#^1-4]]
![[1-SOURCES/Text/sk-root-text.md#^1-5]]

Introductory overview of verses 1–5. ^1-2-1

### 1.3 Verse-by-verse commentary

![[1-SOURCES/Text/sk-root-text.md#^1-1]]

Commentary on first verse. ^1-3-1
Commentary on first verse continued. ^1-3-2

![[1-SOURCES/Text/sk-root-text.md#^1-2]]

Commentary on second verse. ^1-3-3
```

**Obsidian note:** block ID range transclusion (`#^1-1:#^1-5`) is not supported. Always use sequential individual transclusions.

**Language:** original language only in `1-SOURCES/`. No translation or paraphrase here.

---

## 9. Linking System

### Block ID Links — verse level

```markdown
[[1-SOURCES/Text/sk-root-text.md#^1-1]]
```

For transclusion (renders the verse inline in Obsidian):

```markdown
![[1-SOURCES/Text/sk-root-text.md#^1-1]]
```

Use full paths in all `1-SOURCES/` and `2-RAILS/` files.

### Wiki Links — file level

```markdown
[[1-SOURCES/Commentaries/prajnakaramati-sk.md]]
```

Used for file-to-file navigation and in frontmatter `related_*` fields.

### YAML Frontmatter Lists

The machine-readable map used by the LLM to traverse the verse-to-resource network.

**Root text maps outward:**
- `related_commentaries`
- `related_translations`

**Commentaries and translations map inward:**
- `root_text` — the root text they comment on or translate
- `covers_verses` — verse range in block ID format, e.g. `1-1–10-58`

---

## 10. Editorial Notes

```markdown
[Ed: uncertain — two witnesses read *dharmadhātu* here. See Vaidya 1960 p. 47 apparatus.]
```

Rules:
- Always `[Ed: ...]` — square brackets, `Ed:` prefix
- Always in English regardless of file language
- Factual observations only — never interpretive
- Place immediately after the verse or passage they concern

---

## 11. Checklist for Adding a New File

- [ ] Correct folder — `Text/`, `Commentaries/`, `Translations/`, or `References/`
- [ ] Filename uses language tag, no diacritics
- [ ] Frontmatter complete — `source_description` required at minimum
- [ ] External IDs added where applicable (BDRC, CBETA, GRETIL, DSBC, SuttaCentral)
- [ ] `source_url` included if sourced digitally
- [ ] `verse_id_format` declared in frontmatter
- [ ] Every verse has a block ID on its last line — `^chapter-verse` or `^verse`
- [ ] No zero-padding in block IDs
- [ ] Chapter headings `##`, sub-sections `###` — no `####`
- [ ] Commentary has its own TOC headings independent of root text structure
- [ ] Commentary `verse_id_format` declared — follows the commentary author's system
- [ ] Root verse transclusions added at appropriate points in commentary
- [ ] Multi-verse sections use sequential individual transclusions, one per root verse
- [ ] `root_text` and `covers_verses` set in commentary/translation frontmatter
- [ ] `related_commentaries` / `related_translations` updated in root text frontmatter
- [ ] Commentary `registered_id` added to `4-SYSTEM/CLAUDE.md` if this is a new commentary
- [ ] Sanskrit root text in Devanāgarī; Tibetan/Chinese in Unicode
- [ ] Alternative scripts go in separate edition files
- [ ] Verse numbers restart per chapter — `^chapter-verse` not continuous
- [ ] No interpretation — `[Ed: ...]` factual notes only

---

## 12. Language Tags

All files use ISO 639-1 base codes with script or system suffixes where needed.

### Sanskrit

| Tag | Script / System | Typical use |
|---|---|---|
| `-sk` | Devanāgarī | Root texts — default Sanskrit tag |
| `-sk-iast` | IAST romanisation | Edition files |
| `-sk-slp1` | SLP1 | Computational / corpus formats |
| `-sk-hk` | Harvard-Kyoto | Older digital editions |
| `-sk-grantha` | Grantha script | South Indian manuscript tradition |

**Default:** always use `-sk` (Devanāgarī) for Sanskrit root texts.

### Pāli

| Tag | Script / System | Typical use |
|---|---|---|
| `-pi` | Pāli romanisation (PTS standard) | Root texts — default Pāli tag |
| `-pi-sinh` | Sinhala script | Sri Lankan tradition |
| `-pi-thai` | Thai script | Thai tradition |
| `-pi-mymr` | Myanmar script | Myanmar tradition |
| `-pi-latn-cscd` | CSCD romanisation | Chaṭṭha Saṅgāyana CD encoding |

**Default:** always use `-pi` (PTS romanisation) for root texts.

### Tibetan

| Tag | Script / System | Typical use |
|---|---|---|
| `-bo` | Unicode Tibetan script | Root texts — default Tibetan tag |
| `-bo-wy` | Wylie transliteration | Edition files and computational formats |
| `-bo-thl` | THL Extended Wylie | Tibetan & Himalayan Library resources |
| `-bo-acip` | ACIP transliteration | ACIP digital archive format |

### Chinese

| Tag | Script / System | Typical use |
|---|---|---|
| `-zh` | Unicode Traditional Chinese | Root texts — default Chinese tag |
| `-zh-hans` | Simplified Chinese | PRC editions |
| `-zh-hant` | Traditional Chinese | Taiwan / Hong Kong editions |
| `-zh-cbeta` | CBETA digital encoding | CBETA corpus files |

### Other Languages

| Tag | Language |
|---|---|
| `-en` | English |
| `-fr` | French |
| `-de` | German |
| `-es` | Spanish |
| `-it` | Italian |
| `-ja` | Japanese |
| `-ko` | Korean |
| `-mn` | Mongolian |
| `-ne` | Nepali |
| `-si` | Sinhala (modern) |

For languages not listed, use the appropriate ISO 639-1 code.

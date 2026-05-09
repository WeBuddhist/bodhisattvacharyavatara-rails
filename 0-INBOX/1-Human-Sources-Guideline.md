# 1-Human-Sources — File Format and Linking Guidelines

This document specifies the file format, verse annotation, and linking conventions for all materials in `1-Human-Sources/`. Read this before adding any file to the folder.

For the LLM-facing version of these rules see `CLAUDE.md` Section 2 and Section 5. For blank file templates see `0-Project/templates/1-human-sources/`.

---

## 1. Principles

**Single source of truth.** Every text, translation, and commentary lives in one file. Obsidian block IDs make individual verses linkable without splitting files.

**Language tags everywhere.** Every file and folder carrying material in a specific language carries a language tag suffix. See Section 2 for the full tag list.

**Flat file structure.** Editions, translations, and commentaries are single files placed directly in their folder — no subfolder per file.

**No interpretation in this folder.** Files in `1-Human-Sources/` contain human-produced material exactly as received — formatted and annotated for navigation, but not interpreted. The only additions permitted are:

- Block ID anchors
- Frontmatter metadata
- Internal navigation links
- Editorial notes marked explicitly as `[Ed: ...]`

Any interpretive claim — compound analysis, sense assignment, syntactic reading — belongs in `2-Authoritative-Context/`, not here.

**Standard scripts by language.** Root text files use the following script conventions:

|Language|Root text script|Notes|
|---|---|---|
|Sanskrit|Devanāgarī|IAST goes in `editions/` as `iast-sk-iast.md` — recommended but not required|
|Pāli|Pāli romanisation with diacritics|No alternative script in root text|
|Tibetan|Unicode Tibetan script|Wylie goes in `editions/` as `wylie-bo-wy.md`|
|Chinese|Unicode (Traditional or Simplified)|Pinyin goes in `editions/` if needed|

One script per file. Alternative script forms always go in `editions/`.

---

## 2. Folder Structure per Text

```
[text-name]/
├── [lang]-root-text.md              
├── versions/                        
│   ├── [lang]-[editor-surname].md   
│   ├── [lang]-[editor-surname].md   
│   └── [lang+script]-[editor-surname].md  
├── commentaries/                    
│   └── [lang]-[commentary-name].md
├── subcommentaries/                 
│   └── [name]-[lang].md
└── secondary-literature/            
    └── [author-surname]-[short-title]-[lang].md
```

**Naming rules:**

- All names lowercase, hyphenated, no diacritics in filename
- Diacritics used freely inside file content and frontmatter
- Text root folder uses the full canonical name, not a short title
- Script-only editions (no named editor) are named by script: `iast-sk-iast.md`, `wylie-bo-wy.md`
- Devanāgarī is never an edition for Sanskrit — it is the root text script
- IAST goes in `editions/iast-sk-iast.md` — recommended but not required

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

|Database|Scope|Field|
|---|---|---|
|BDRC|Tibetan, Sanskrit, Pāli|`bdrc_work_id`, `bdrc_instance_id`|
|CBETA|Chinese Buddhist canon|`cbeta_id`|
|GRETIL|Sanskrit texts|`gretil_url`|
|DSBC|Sanskrit Buddhist canon|`dsbc_url`|
|SuttaCentral|Pāli, translations|`suttacentral_id`|
|ACIP|Tibetan|`acip_id`|
|VIAF|Authors and works|in `other_ids`|
|Wikidata|Works and concepts|in `other_ids`|

---

## 4. File Frontmatter

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
script: IAST
source_description: "Transcribed from Vaidya 1960 critical edition"
source_url: https://www.dsbcproject.org/canon-text/content/71
dsbc_url: https://www.dsbcproject.org/canon-text/content/71
bdrc_work_id: WA1KG13126
related_editions:
  - 1-Human-Sources/bodhisattvacaryavatara/editions/la-vallee-poussin-sk.md
  - 1-Human-Sources/bodhisattvacaryavatara/editions/vaidya-sk.md
  - 1-Human-Sources/bodhisattvacaryavatara/editions/iast-sk-iast.md
related_translations:
  - 1-Human-Sources/bodhisattvacaryavatara/translations/crosby-en.md
  - 1-Human-Sources/bodhisattvacaryavatara/translations/tibetan-bo.md
related_commentaries:
  - 1-Human-Sources/bodhisattvacaryavatara/commentaries/prajnakaramati-sk.md
  - 1-Human-Sources/bodhisattvacaryavatara/commentaries/kunzang-pelden-bo.md
  - 1-Human-Sources/bodhisattvacaryavatara/commentaries/minyak-kunzang-sonam-bo.md
---
```

`verse_id_format` declares how block IDs are structured in this file. Three possible values:

|Value|Block ID format|Example|
|---|---|---|
|`chapter-verse`|`^chapter-verse`|`^6-33`|
|`verse`|`^verse`|`^33`|
|`book-chapter-verse`|`^book-chapter-verse`|`^1-1-1`|

### Edition Frontmatter

```yaml
---
title: Bodhicaryāvatāra — Vaidya IAST Edition
author: Śāntideva
editor: Vaidya, P.L.
date: 1960
language: Sanskrit
script: IAST
file_type: edition
lang_tag: sk-iast
verse_id_format: chapter-verse
root_text: 1-Human-Sources/bodhisattvacaryavatara/root-text-sk.md
has_variants: true
source_description: "Vaidya, P.L. (1960). Bodhicaryāvatāra. Darbhanga: Mithila Institute."
source_url:
bdrc_work_id:
---
```

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
root_text: 1-Human-Sources/bodhisattvacaryavatara/root-text-sk.md
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
verse_id_format: chapter-verse        # the commentary's own ID system
registered_id: prajnakaramati
root_text: 1-Human-Sources/bodhisattvacaryavatara/root-text-sk.md
covers_verses: 1-1–10-58             # root text verse range covered
source_description: "Transcribed from La Vallée Poussin edition 1901–1914"
source_url:
bdrc_work_id: WA1KG14159
gretil_url: https://gretil.sub.uni-goettingen.de/gretil/1_sanskr/6_sastra/3_phil/buddh/bsa052_u.htm
---
```

### Secondary Literature Frontmatter

```yaml
---
title: "Śāntideva and the Bodhicaryāvatāra"
author: Crosby, Kate
date: 2017
language: English
file_type: secondary-literature
lang_tag: en
root_text: 1-Human-Sources/bodhisattvacaryavatara/root-text-sk.md
topics: [bodhicitta, chapter 6, patience]
source_description: "Oxford University Press 2017"
source_url: https://doi.org/10.1093/example
---
```

---

## 5. Block IDs and Verse Structure

Obsidian block IDs placed at the end of a verse are the sole verse-level linking mechanism across the entire project.

### Block ID Format

|Text structure|Format|Example|
|---|---|---|
|Chapters + verses|`^chapter-verse`|`^6-33`|
|Verses only|`^verse`|`^33`|
|Books + chapters + verses|`^book-chapter-verse`|`^1-1-1`|

Numbers are not zero-padded. Use natural numbers: `^6-33` not `^06-033`.

The block ID is placed on the last line of the verse, after the final character, with a single space before the caret:

```
bodhisattvapadaprāptiṃ vakṣyāmi śāstrasaṅgraham || ^1-1
```

For multi-line prose passages (commentaries), the block ID goes on the last line of the passage that corresponds to that verse.

### Chapter and Section Headings

Author-defined structural divisions map directly to the Markdown heading hierarchy. If the author provided a table of contents, its entries define the headings.

```markdown
## Chapter 6: Kṣānti — Patience

### 6.1 The harm of anger

### 6.2 The cultivation of patience
```

- Level 2 — author-defined books or chapters
- Level 3 — author-defined sub-sections (e.g. from the author's own TOC)
- Level 4 — not used (block IDs replace verse-level headings)

**Sub-sections do not affect verse IDs.** Verses beneath a level-3 heading still use `^chapter-verse` block IDs, not `^chapter-section-verse`. Sub-section headings are for navigation only.

Never use headings for editor-imposed divisions. If an edition or translator adds section titles not present in the original, note them as `[Ed: ...]` inline.

### Verse Numbering

Verse numbers restart at 1 for each chapter. Block ID `^6-33` means chapter 6, verse 33 of that chapter — not the 33rd verse of the whole text.

This applies even when the source edition uses continuous verse numbering across the whole text. Always convert to per-chapter numbering for block IDs. Record the edition's continuous number in an editorial note if useful:

```
sugatān sagaṇān natvā dharmakāyādigocaran |
bodhisattvapadaprāptiṃ vakṣyāmi śāstrasaṅgraham || ^1-1
[Ed: continuous verse number 1 in Vaidya 1960]
```

### Pre-Chapter Content — Chapter 0

When a text contains content before Chapter 1 — colophons, title lines, homage verses, scribal introductions, or any material that precedes the author's first chapter — it is placed under a `## 0. Introduction` heading and its verses are numbered `^0-verse`.

This keeps the `^chapter-verse` system fully consistent: chapter 0 is the pre-chapter layer, chapter 1 is the first authored chapter. The convention applies to root texts, editions, translations, and commentaries alike.

Example — Tibetan root text of the Bodhicaryāvatāra:

```markdown
# སྤྱོད་འཇུག

## 0. Introduction

༄། །བྱང་ཆུབ་སེམས་དཔའི་སྤྱོད་པ་ལ་འཇུག་པ་བཞུགས་སོ། ། ^0-1
༄༅༅། །རྒྱ་གར་སྐད་དུ། བོ་དྷི་སཏྭ་ཙརྱ་ཨ་བ་ཏཱ་ར། ^0-2
བོད་སྐད་དུ། བྱང་ཆུབ་སེམས་དཔའི་སྤྱོད་པ་ལ་འཇུག་པ། ^0-3
སངས་རྒྱས་དང་བྱང་ཆུབ་སེམས་དཔའ་ཐམས་ཅད་ལ་ཕྱག་འཚལ་ལོ། ། ^0-4

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

- Author-written prefaces or introductions that the author numbered as Chapter 1 or equivalent — these are Chapter 1 regardless of their content
- Editor footnotes or apparatus — these are `[Ed: ...]` notes, not verses

---

## 6. File Format — Root Text

### Sanskrit Root Text (Devanāgarī)

Devanāgarī is the standard script for all Sanskrit root texts. IAST goes in `editions/iast-sk-iast.md` — recommended but not required.

```markdown
---
[frontmatter]
---

## Chapter 1: बोधिचित्तानुशंस

सुगतान् सगणान् नत्वा धर्मकायादिगोचरान् ।
बोधिसत्त्वपदप्राप्तिं वक्ष्यामि शास्त्रसङ्ग्रहम् ॥ ^1-1

इदं हि बुद्धपुत्राणां मनोऽभिरमयिष्यति ।
सम्यक् प्रतिपन्नानां श्रद्धा च वर्धयिष्यति ॥ ^1-2
```

### Pāli

```markdown
---
[frontmatter]
---

## Kusalā Dhammā

katame dhammā kusalā? yasmiṃ samaye kāmāvacaraṃ kusalaṃ cittaṃ uppannaṃ hoti
somanassasahagataṃ ñāṇasampayuttaṃ rūpārammaṇaṃ vā saddhārammaṇaṃ vā... ^1
```

### Tibetan Root Text (Unicode)

Unicode Tibetan script is the standard for Tibetan root texts. Wylie transliteration goes in `editions/wylie-bo-wy.md`.

```markdown
---
[frontmatter]
---

## Chapter 1: བྱང་ཆུབ་སེམས་ཀྱི་ཡོན་ཏན་བསྟོད་པ།

བདེ་གཤེགས་ཆོས་ཀྱི་སྐུ་མངའ་སྲས་བཅས་དང་། །
བྱང་ཆུབ་སེམས་དཔའ་ཐམས་ཅད་ལ་ཕྱག་འཚལ་ལོ། ^1-1
```

**Verse separation:** a blank line between verses is sufficient.

**Sanskrit half-verses:** mark with `|` at the caesura and `||` at verse end in IAST. Do not create separate block IDs for half-verses.

---

## 7. File Format — Editions

Editions fall into two types:

**Named critical editions** (editor known) — contain the text with variant notation where the edition differs from the root text.

**Script editions** (no named editor) — contain the root text in an alternative script with no variants section.

### Named Edition Example (IAST)

```markdown
---
[frontmatter]
---

## Chapter 1: Bodhicittānuśaṃsa

sugatān sagaṇān natvā dharmakāyādigocaran |
bodhisattvapadaprāptiṃ vakṣyāmi śāstrasaṅgraham || ^1-1

[Ed: La Vallée Poussin reads *sugatāṃ* (acc. sg.) for *sugatān* (acc. pl.) in pāda a.
Apparatus: sugatān ] sugatāṃ LVP 1901; sugatā ms. Ṇ]
```

### Script Edition Example — IAST (recommended for Sanskrit)

```markdown
---
title: Bodhicaryāvatāra — IAST Romanisation
script: IAST
file_type: edition
lang_tag: sk-iast
root_text: 1-Human-Sources/bodhisattvacaryavatara/root-text-sk.md
source_description: "IAST transcription of root-text-sk.md"
---

## Chapter 1: Bodhicittānuśaṃsa

sugatān sagaṇān natvā dharmakāyādigocaran |
bodhisattvapadaprāptiṃ vakṣyāmi śāstrasaṅgraham || ^1-1
```

---

## 8. File Format — Translations

Same block ID system as the root text. Block IDs correspond to the source verse, not to any numbering the translator may use.

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
[combined translation] ^1-1
[Ed: this rendering covers source verses 1-1 and 1-2 together]
```

---

## 9. File Format — Commentaries

A commentary is an independent authored work with its own structure. It has:

- Its own TOC headings (h2/h3) drawn from the commentary author's own chapter and section titles — independent of the root text heading structure
- Its own block IDs following whatever structural system the commentary author defined — declared in `verse_id_format` frontmatter field
- Transclusions of the root verse(s) each section addresses, anchoring the commentary to the root text's block ID system

### Commentary Frontmatter — verse_id_format

The `verse_id_format` field declares the commentary's own ID system:

|Commentary structure|verse_id_format value|Example block ID|
|---|---|---|
|Chapter + verse|`chapter-verse`|`^3-12`|
|Section + paragraph|`section-paragraph`|`^4-2`|
|Verse only|`verse`|`^145`|
|Folio + line|`folio-line`|`^23b-4`|
|Book + chapter + verse|`book-chapter-verse`|`^2-1-4`|

Use whatever system the commentary author defined. If the commentary has no internal numbering, use sequential `verse` format.

### Format — Without Transclusions

The raw commentary structure before transclusions are added. Commentary block IDs follow the commentary author's own system — here `chapter-section-paragraph` (`book-chapter-verse` format where "verse" is a paragraph unit):

```markdown
---
[frontmatter — verse_id_format: book-chapter-verse]
---

## 1. Commentary on Chapter 1

### 1.1 Introduction to Chapter 1

Text of general introduction to chapter 1. ^1-1-1
Text of general introduction to chapter 1. ^1-1-2

### 1.2 Introduction to root text verses 1–5

Text of general introduction to root text verses 1–5. ^1-2-1
Text of general introduction to root text verses 1–5. ^1-2-2

### 1.3 Commentary on each verse in section 1–5

Commentary on first verse. ^1-3-1
Commentary on first verse. ^1-3-2

Commentary on second verse. ^1-3-3
Commentary on second verse. ^1-3-4
Commentary on second verse. ^1-3-5
```

### Format — With Transclusions

Transclusions are placed at the point where root verses become relevant — not mechanically at the top of every section. Introductory sections that discuss a group of verses get a ranged transclusion at their opening. Verse-by-verse sections get one transclusion per verse, immediately before the commentary on that verse:

```markdown
---
[frontmatter — verse_id_format: book-chapter-verse]
---

## 1. Commentary on Chapter 1

### 1.1 Introduction to Chapter 1

Text of general introduction to chapter 1. ^1-1-1
Text of general introduction to chapter 1. ^1-1-2

### 1.2 Introduction to root text verses 1–5

![[1-Human-Sources/bodhisattvacaryavatara/root-text-sk.md#^1-1]]
![[1-Human-Sources/bodhisattvacaryavatara/root-text-sk.md#^1-2]]
![[1-Human-Sources/bodhisattvacaryavatara/root-text-sk.md#^1-3]]
![[1-Human-Sources/bodhisattvacaryavatara/root-text-sk.md#^1-4]]
![[1-Human-Sources/bodhisattvacaryavatara/root-text-sk.md#^1-5]]

Text of general introduction to root text verses 1–5. ^1-2-1
Text of general introduction to root text verses 1–5. ^1-2-2

### 1.3 Commentary on each verse in section 1–5

![[1-Human-Sources/bodhisattvacaryavatara/root-text-sk.md#^1-1]]

Commentary on first verse. ^1-3-1
Commentary on first verse. ^1-3-2

![[1-Human-Sources/bodhisattvacaryavatara/root-text-sk.md#^1-2]]

Commentary on second verse. ^1-3-3
Commentary on second verse. ^1-3-4
Commentary on second verse. ^1-3-5
```

### Transclusion Placement Rules

- **Sections with no root verse reference** (e.g. general chapter introductions): no transclusion. Commentary block IDs only.
- **Sections introducing a group of verses**: transclude all verses in the group in sequence at the opening of the section, before the commentary text.
- **Verse-by-verse sections**: one transclusion immediately before the commentary on each verse. A blank line separates transclusion from commentary text.
- **Obsidian note:** block ID range transclusion (`#^1-1:#^1-5`) is not supported. Always use sequential individual transclusions.

The commentary's own block IDs are always independent of the root verse IDs. The editorial note records which root verses a passage covers when that is not obvious from the transclusions. This feeds into `coarser_groupings:` in `2-Authoritative-Context/` packages.

**Language:** original language only. No translation or paraphrase here.

---

## 10. Linking System

### Block ID Links — verse level

```markdown
[[1-Human-Sources/bodhisattvacaryavatara/root-text-sk.md#^1-1]]
```

For transclusion:

```markdown
![[1-Human-Sources/bodhisattvacaryavatara/root-text-sk.md#^1-1]]
```

Use full paths in all `1-Human-Sources/` and `2-Authoritative-Context/` files. Short wiki links are acceptable only in `0-Project/` documentation.

### Wiki Links — file level

```markdown
[[1-Human-Sources/bodhisattvacaryavatara/commentaries/prajnakaramati-sk.md]]
```

Used for file-to-file navigation and in frontmatter `related_*` fields.

### YAML Frontmatter Lists — structural mapping

The machine-readable map used by the LLM and Dataview to traverse the verse-to-resource network.

**Root text maps outward:**

- `related_editions`
- `related_translations`
- `related_commentaries`

**Editions, translations, commentaries map inward:**

- `root_text` — the root text they derive from or comment on
- `covers_verses` — verse range in block ID format, e.g. `1-1–10-58`

---

## 11. Verse-to-Resource Mapping

To locate all resources for a specific verse, e.g. `^6-33`:

**Dataview:** query `covers_verses` ranges across commentary and translation frontmatter to find all files whose range includes `6-33`.

**Obsidian:** open root text frontmatter, follow `related_commentaries` links, navigate to `^6-33` in each commentary file.

**LLM / resolver script:** reads root text frontmatter `related_*` lists, fetches each file, navigates to `^6-33` block via transclusion.

---

## 12. Editorial Notes

```markdown
[Ed: uncertain — two witnesses read *dharmadhātu* here. See Vaidya 1960 p. 47 apparatus.]
```

Rules:

- Always `[Ed: ...]` — square brackets, `Ed:` prefix
- Always in English regardless of file language
- Factual observations only — never interpretive
- Place immediately after the verse or passage they concern

---

## 13. Checklist for Adding a New File

- [ ] Correct folder — `editions/`, `translations/`, `commentaries/`, or `secondary-literature/`
- [ ] Filename uses language tag, no diacritics, no subfolders
- [ ] Frontmatter complete — `source_description` required at minimum
- [ ] External IDs added where applicable (BDRC, CBETA, GRETIL, DSBC, SuttaCentral)
- [ ] `source_url` included if sourced digitally
- [ ] `verse_id_format` declared in frontmatter
- [ ] Every verse has a block ID on its last line — `^chapter-verse` or `^verse`
- [ ] No zero-padding in block IDs
- [ ] Chapter headings h2, sub-sections h3 — no h4
- [ ] Commentary has its own TOC headings independent of root text structure
- [ ] Commentary verse_id_format declared in frontmatter — follows commentary author's system
- [ ] Root verse transclusions added before each commentary section
- [ ] Multi-verse sections use sequential individual transclusions, one per root verse
- [ ] Editorial note records root verse range when commentary covers multiple verses
- [ ] `root_text` and `covers_verses` set in commentary/translation frontmatter
- [ ] `related_*` fields updated in root text frontmatter
- [ ] Commentary `registered_id` added to `index.md` if new
- [ ] Sanskrit root text in Devanāgarī, Pāli in romanised Pāli, Tibetan/Chinese in Unicode
- [ ] Alternative scripts go in `editions/` — IAST as `iast-sk-iast.md`
- [ ] Verse numbers restart per chapter — `^chapter-verse` not continuous
- [ ] No interpretation — `[Ed: ...]` notes only

## 14. Language Tags

All folders and files use ISO 639-1 base codes with script or system suffixes where needed to distinguish different forms of the same language.

### Sanskrit

|Tag|Script / System|Typical use|
|---|---|---|
|`-sk`|IAST|Root texts — default Sanskrit tag|
|`-sk-iast`|Sanskrit IAST|IAST romanisation (editions)|
|`-sk-slp1`|SLP1|Computational / corpus formats (e.g. GRETIL digital files)|
|`-sk-hk`|Harvard-Kyoto|Older digital editions and some dictionaries|
|`-sk-vel`|Velthuis|Legacy digital formats (e.g. some GRETIL files)|
|`-sk-itrans`|ITRANS|Some older digital resources|
|`-sk-grantha`|Grantha script|South Indian manuscript tradition|
|`-sk-sharda`|Śāradā script|Kashmir manuscript tradition|
|`-sk-newa`|Newa (Pracalit) script|Nepal manuscript tradition|
|`-sk-bengali`|Bengali script|Eastern manuscript tradition|
|`-sk-telugu`|Telugu script|South Indian manuscript tradition|
|`-sk-malayalam`|Malayalam script|South Indian manuscript tradition|

**Default:** always use `-sk` (Devanāgarī) for Sanskrit root texts. Other tags appear only in `editions/` for script or encoding variants.

### Pāli

|Tag|Script / System|Typical use|
|---|---|---|
|`-pi`|Pāli romanisation (PTS standard)|Root texts — default Pāli tag|
|`-pi-sinh`|Sinhala script|Sri Lankan manuscript and print tradition|
|`-pi-thai`|Thai script|Thai manuscript and print tradition|
|`-pi-mymr`|Myanmar (Burmese) script|Myanmar manuscript and print tradition|
|`-pi-khmer`|Khmer script|Cambodian manuscript tradition|
|`-pi-dev`|Devanāgarī|Some Indian print editions|
|`-pi-latn-cscd`|CSCD romanisation|Chaṭṭha Saṅgāyana CD encoding (minor diacritic differences from PTS)|

**Default:** always use `-pi` (PTS romanisation) for root texts. Other tags appear only in `editions/` for script or encoding variants.

**Note on CSCD:** the CSCD digital edition uses slightly different diacritics from the PTS standard in some places. Tag CSCD-sourced files as `-pi-latn-cscd` if preserving the original encoding matters; use `-pi` if normalized to PTS standard.

### Tibetan

|Tag|Script / System|Typical use|
|---|---|---|
|`-bo`|Unicode Tibetan script|Root texts — default Tibetan tag|
|`-bo-wy`|Wylie transliteration|Editions and computational formats|
|`-bo-thl`|THL Extended Wylie|Some digital resources (Tibetan & Himalayan Library)|
|`-bo-acip`|ACIP transliteration|ACIP digital archive format|

### Chinese

|Tag|Script / System|Typical use|
|---|---|---|
|`-zh`|Unicode Traditional Chinese|Root texts — default Chinese tag|
|`-zh-hans`|Simplified Chinese|PRC editions|
|`-zh-hant`|Traditional Chinese|Taiwan / Hong Kong editions|
|`-zh-cbeta`|CBETA digital encoding|CBETA corpus files|

### Other Languages

|Tag|Language|
|---|---|
|`-en`|English|
|`-fr`|French|
|`-de`|German|
|`-es`|Spanish|
|`-it`|Italian|
|`-ja`|Japanese|
|`-ko`|Korean|
|`-mn`|Mongolian|
|`-ne`|Nepali|
|`-si`|Sinhala (modern)|

For languages not listed, use the appropriate ISO 639-1 code. When a resource is multilingual, tag by the language of the primary content.

---
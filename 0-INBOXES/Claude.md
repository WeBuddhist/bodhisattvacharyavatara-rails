# CLAUDE.md — 🛤️ Railroad

This file is the persistent schema and instruction set for the LLM working on this project. Read it in full at the start of every session before touching any file.

---

## 1. Purpose

**🛤️ Railroad — Laying the Tracks for Text Transformation Grounded in Tradition** is an open interpretive infrastructure for classical Buddhist texts. Its purpose is to make AI-assisted text transformation reliable by laying the tracks before any transformation runs — resolving the interpretive ambiguities of each text word by word, verse by verse, grounded in the classical commentary tradition, and storing those resolutions as structured, openly licensed, human-verifiable reference files.

Most efforts to improve AI performance on classical texts focus on the engine: more powerful models, smarter retrieval, better agents. 🛤️ Railroad focuses on the track. An engine without track goes nowhere reliable. Track laid well lets any engine run — any model, any transformation type, any target language — without redoing the philological work from scratch each time.

The solution is not to feed the LLM more raw material (commentaries, dictionaries, translations). More context without structure produces unreliable results. Instead, 🛤️ Railroad extracts the interpretive judgments already made by the human commentary tradition, structures them as compact machine-readable context packages, and passes only what is needed to resolve the ambiguities in a specific passage. The LLM then does stylistic work, not philological work.

The authority behind every claim in this project is the human commentary tradition. The LLM is the extraction and formatting agent — it adds no interpretation of its own. This is why the no-parametric-knowledge rule below is absolute.

This project is not a research assistant. It is a structured philological database. Every claim must be grounded in a cited human source. No claim may rest on your parametric knowledge.

---

## 2. Filesystem Rules

### `0-Project/`

- Project documentation for contributors. You may read but never write here.
- Contains onboarding guides, editorial guidelines, workflows, and role-specific documentation.

### `1-Human-Sources/`

- **You may never write to `1-Human-Sources/`.** Read only.
- Contains all human-produced materials: source texts, commentaries, editions, translations, dictionaries, and secondary literature.
- Nothing in `1-Human-Sources/` is your interpretation. It is ground truth.

**Language tag convention**: all folders within a text's `editions/`, `translations/`, `commentaries/`, `subcommentaries/`, and `secondary-literature/` carry a language tag suffix identifying the language of that resource. Tags follow ISO 639-1 where available:

|Tag|Language|
|---|---|
|`-sk`|Sanskrit|
|`-pi`|Pāli|
|`-bo`|Tibetan|
|`-zh`|Chinese|
|`-en`|English|
|`-fr`|French|
|`-de`|German|
|`-[xx]`|other ISO 639-1 codes|

Format: `[name]-[lang]/` e.g. `prajnakaramati-sk/`, `kunzang-pelden-bo/`, `crosby-en/` The root text file uses the same convention: `root-text-sk.md`, `root-text-pi.md`

### `2-Authoritative-Context/`

- You write all structured interpretation here.
- Contains commentary interpretation extracted from `1-Human-Sources/` and reformatted as compact, machine-readable context packages: morphological analysis, UCCA trees, semantic glosses, interpretive notes, section summaries, and text-local concept wiki.
- Every field must cite a specific file in `1-Human-Sources/`.
- Citation format: `(1-Human-Sources/[text]/commentaries/[source]/[file]#[section])`
- If you cannot cite a claim, do not make it. Leave the field blank and mark `status: draft`.

### `4-Wiki/`

- Cross-text concept pages aggregated from `2-Authoritative-Context/[text]/local-wiki/`.
- Every claim cites a specific file in `2-Authoritative-Context/`.
- Citation format: `(2-Authoritative-Context/[text]/local-wiki/[file]#[section])`

### `3-Text-Transformations/`

- Text transformations generated using `2-Authoritative-Context/` packages as context.
- Contains translations, adaptations, lessons, reading plans, scripts, and other derived content, organized by text.
- You write here only when explicitly instructed to generate a transformation.
- Every transformation file must record which context package(s) were used.

### The Citation Chain Rule

```
1-Human-Sources/ → 2-Authoritative-Context/ → 4-Wiki/
                                        → 3-Text-Transformations/
```

No link in this chain may be skipped. `4-Wiki/` and `3-Text-Transformations/` never cite `1-Human-Sources/` directly.

---

## 3. Directory Structure

```
Railroad/
├── CLAUDE.md
├── index.md
├── log.md
│
├── 0-Project/
│   ├── onboarding/
│   ├── editorial-guidelines/
│   ├── technical-documentation/
│   ├── workflows/
│   └── roles/
│       ├── domain-specialists/
│       └── ai-skills-designers/
│
├── 1-Human-Sources/
│   ├── bodhisattvacaryavatara/
│   │   ├── root-text-sk.md              # primary Sanskrit root text
│   │   ├── editions/                    # other Sanskrit editions
│   │   │   ├── la-vallee-poussin-sk/
│   │   │   └── vaidya-sk/
│   │   ├── translations/                # translations in any language
│   │   │   ├── tibetan-bo/
│   │   │   └── [author-lang]/
│   │   ├── commentaries/                # language tag suffix on each folder
│   │   │   ├── prajnakaramati-sk/
│   │   │   ├── kunzang-pelden-bo/
│   │   │   ├── minyak-kunzang-sonam-bo/
│   │   │   └── [author-lang]/
│   │   └── secondary-literature/
│   │       └── [author-lang]/
│   ├── abhidhamma/
│   │   ├── root-text-pi.md              # primary Pāli root text (CSCD)
│   │   ├── editions/                    # other Pāli editions
│   │   │   └── pts-pi/
│   │   ├── translations/                # translations in any language
│   │   │   └── [author-lang]/
│   │   ├── commentaries/                # language tag suffix on each folder
│   │   │   ├── atthasalini-pi/
│   │   │   ├── sammohavinodani-pi/
│   │   │   ├── pancappakarana-pi/
│   │   │   ├── abhidhammattha-sangaha-pi/
│   │   │   └── [author-lang]/
│   │   ├── subcommentaries/
│   │   │   └── mulatika-pi/
│   │   └── secondary-literature/
│   │       └── [author-lang]/
│   └── dictionaries/
│       ├── monier-williams-sk/
│       ├── apte-sk/
│       └── pts-ped-pi/
│
├── 2-Authoritative-Context/
│   ├── bodhisattvacaryavatara/
│   │   ├── context/
│   │   │   ├── verses/
│   │   │   │   ├── 1-1.md
│   │   │   │   └── ...
│   │   │   └── sections/
│   │   │       ├── 1.md              # combined section context
│   │   │       ├── 1-1.md
│   │   │       └── references/       # per-source outlines + study notes
│   │   │           ├── prajnakaramati.md
│   │   │           ├── kunzang-pelden.md
│   │   │           └── root-text.md
│   │   └── local-wiki/
│   └── abhidhamma/
│       ├── context/
│       │   ├── units/
│       │   └── sections/
│       │       ├── [section].md     # combined section context
│       │       └── references/
│       └── local-wiki/
│
├── 3-Text-Transformations/
│   ├── bodhisattvacaryavatara/
│   │   ├── scholarly-en/
│   │   │   ├── brief.md          # transformation specification
│   │   │   ├── terminology.md    # selected standard terminology
│   │   │   └── outputs/
│   │   ├── childrens-en/
│   │   │   ├── brief.md
│   │   │   ├── terminology.md
│   │   │   └── outputs/
│   │   └── [transformation-id]/
│   │       ├── brief.md
│   │       ├── terminology.md
│   │       └── outputs/
│   └── abhidhamma/
│       └── [transformation-id]/
│           ├── brief.md
│           ├── terminology.md
│           └── outputs/
│
└── 4-Wiki/
    ├── articles/
    ├── global-glossary/
    │   ├── glossary-sk-en.md
    │   ├── glossary-sk-bo.md
    │   ├── glossary-sk-zh.md
    │   ├── glossary-pi-en.md
    │   ├── glossary-pi-zh.md
    │   ├── glossary-bo-en.md
    │   └── glossary-zh-en.md
    └── index.md

# Note: when adding a new text, add its folder to both
# 2-Authoritative-Context/ and 3-Text-Transformations/ simultaneously.
```

---

## 4. Project Folder

The `0-Project/` folder is maintained by human contributors, not the LLM. Its structure and purpose:

### `0-Project/onboarding/`

Entry point for all new contributors regardless of role. Contains:

- `README.md` — what 🛤️ Railroad is, the problem it solves, the folder structure
- `quick-start.md` — how to make your first contribution in one session
- `key-concepts.md` — authoritative context, citation chain, divergence flags, sense IDs, UCCA — explained for non-specialists

### `0-Project/editorial-guidelines/`

Standards governing the intellectual content of `2-Authoritative-Context/`:

- Transcription and transliteration conventions (IAST, Devanāgarī, Pāli Roman)
- Citation standards for each commentary tradition
- How to determine unit boundaries
- How to handle commentarial divergence
- Sense ID naming conventions

### `0-Project/technical-documentation/`

Tools and infrastructure:

- Obsidian vault setup and recommended plugins
- Claude Code configuration
- Transclusion resolver script usage
- Dataview queries for coverage tracking and linting

### `0-Project/workflows/`

Step-by-step procedures for recurring tasks:

- Ingesting a new text
- Ingesting a new commentary
- Populating a verse package (layers 1–4)
- Running a lint pass
- Assembling a context package for generation
- Generating and filing a text transformation

### `0-Project/roles/`

Role-specific guidance:

**`domain-specialists/`** — for philologists, scholars, and text experts:

- How to evaluate and correct LLM-generated analysis
- How to flag errors and divergences
- Which fields require human sign-off before status: complete
- How to add a new commentary to `1-Human-Sources/`

**`ai-skills-designers/`** — for contributors building LLM workflows:

- How to write ingest prompts for new text types
- How to design and test transformation prompts
- How to use context packages as LLM input
- How to build and refine lint passes

---

## 5. Texts and Reference Systems

### Reference System — General Rule

Reference IDs reflect the structural divisions **as defined by the author of the text**, not by editors or translators. Use only the divisions the author explicitly created.

- If the author defined chapters and verses: `TEXT_CC.VVV` (zero-padded)
- If the author defined verses only (no chapters): `TEXT_VVV`
- If the author defined books, chapters, and verses: `TEXT_BB.CC.VVV`

Never impose a division the author did not create. Editor-imposed divisions (such as critical edition section numbers) are recorded as metadata, not as part of the canonical reference ID.

### Bodhicaryāvatāra (BCA)

- **Primary source**: Sanskrit root text (`1-Human-Sources/bodhisattvacaryavatara/root-text-sk.md`)
- **Additional editions**: La Vallée Poussin, Vaidya (`1-Human-Sources/bodhisattvacaryavatara/editions/`)
- **Translations**: Tibetan and others (`1-Human-Sources/bodhisattvacaryavatara/translations/`)
- **Reference format**: `BCA_CC.VVV` (chapter, verse — zero-padded)
- **Rationale**: Śāntideva defined 10 chapters. No book or sub-chapter divisions.
- **Example**: `BCA_01.001`, `BCA_06.033`
- **Hierarchy**: Chapter → Verse
- **Source language**: Sanskrit (Devanāgarī + IAST in all files)
- **Parallel source**: Tibetan translation treated as independent witness, not as a version of the Sanskrit. Tibetan variants recorded in verse frontmatter under `tibetan_witness:` rather than in a variants block.

### Abhidhamma Piṭaka

- **Canonical edition**: PTS (page references) + CSCD (digital source)
- **Reference format**: `[Treatise abbreviation]_[section].[unit]`
- **Treatise abbreviations**: Ds, Vbh, Dhk, Pp, Kv, Yam, Paṭṭh
- **Example**: `Ds_001`, `Kv_001.001`
- **Hierarchy**: Treatise → Book/Kanda → Section → Unit
- **Rationale**: Each treatise is its own authored work with its own internal structure. The seven treatises are not sub-divisions of a single authored unit.
- **Source language**: Pāli (Roman script + diacritics in all files)
- **Special case — Paṭṭhāna**: Document at relation level only (`Paṭṭh_[relation].md`). Do not attempt unit-level files for conditional combinations.

### Adding New Texts

When a new text is added to the project, the domain specialist responsible must define the following in `index.md` before any packages are created:

- Canonical reference format and rationale (which author-defined divisions exist)
- Primary source file path in `1-Human-Sources/`
- `1-Human-Sources/` subfolder structure (which of: root-text-[lang].md, editions, translations, commentaries, secondary-literature apply to this text)
- Registered commentary IDs
- Any text-specific exceptions to the general schema

---

## 6. Analytical Units and Verse Dependencies

### Core Rule

**One file per verse, always.** File naming is always by verse ID: `6-33.md`. Dependencies between verses are handled through frontmatter metadata and context assembly — never through file naming or file merging.

### Unit Types

- `single` — verse syntactically complete alone
- `group` — verse syntactically incomplete without adjacent verse(s); UCCA tree lives in first verse's file, subsequent members reference it with `ucca_ref:`
- `template` — first member of a formulaic repetition series (Abhidhamma)
- `instance` — subsequent member; points to template for UCCA and gloss

### Dependency Types

- `requires_context: [verse-id]` — verse is semantically incomplete without an adjacent verse; resolver script prepends that verse's package at generation time
- `dependency_type: semantic | pronoun | ellipsis | answer` — records the nature of the semantic link

### Coarser Groupings

When a commentary analyzes a larger unit than the file boundary, record in `coarser_groupings:`. Do not restructure files. When commentaries disagree on grouping, use the finest granularity (separate files) and note the coarser grouping as metadata.

---

## 7. Commentary Handling

### General Rules

- Commentaries are always paraphrased in English. Never quote at length.
- Every paraphrase cites its source passage.
- When commentaries disagree, record the disagreement explicitly. Never flatten to consensus.
- The language of a commentary does not affect its treatment — Sanskrit, Pāli, Tamil, Tibetan, Chinese commentaries are handled identically.

### Commentary Metadata

Each commentary used must be registered in `index.md` with:

- Short ID (used in citations throughout): e.g. `prajnakaramati`, `buddhaghosa_as`
- Full name and date
- Language
- Edition used (file path in `1-Human-Sources/`)
- Scope (which texts/sections it covers)

### Divergence Flags

When commentaries disagree on any of the following, flag with `⚑` in the relevant field:

- Unit boundary
- Compound analysis (Sanskrit)
- Technical term sense
- Syntactic structure
- Doctrinal interpretation

---

## 8. Package File Format — Verses and Units

### Frontmatter

```yaml
---
ref: BCA_01.001
text: bodhicharyavatara
unit_type: single | group | template | instance
unit_verses: [BCA_01.001]
syntactic_unit: [BCA_01.001]
coarser_groupings:
  prajnakaramati: [BCA_01.001, BCA_01.002]
template_ref:                        # for instance type only
commentary_coverage: [prajnakaramati, crosby_skilton_1995]
tradition_coverage: [sanskrit, tibetan]
concepts: [dharma (cosmic order), itihāsa]
speaker: shantideva                    # shantideva | objector | canonical-quote | formulaic | mixed
discourse_mode: direct                 # direct | dialogue | refutation | enumeration | formulaic | hymn
canonical_refs:
  - ref: [canonical citation]
    relation: parallel | source-quote | commentary-ref
    suttacentral_id:
    package:
layer_order: [traditional-interpretation, morphological, syntactic, semantic-gloss, translation-dynamics]
# Sanskrit/Pāli: traditional-interpretation, morphological, syntactic, semantic-gloss, translation-dynamics
# Tibetan/Chinese: traditional-interpretation, syntactic, morphological, semantic-gloss, translation-dynamics
disambiguation_status: draft | partial | complete
gloss_status: draft | partial | complete
ucca_status: draft | partial | complete
translation_dynamics_status: draft | partial | complete
---
```

### Source Text Block

```markdown
## Source Text

**Devanāgarī / Unicode Tibetan / Unicode Chinese**
[text here]

**Romanised Pāli** (Pāli texts only)
[text here]

**Variants**
[any apparatus notes from critical edition, with recension IDs]
```

Transclusion syntax for Obsidian: `![[1-Human-Sources/bodhisattvacaryavatara/texts/[file]#BCA_01.001]]` The transclusion resolver script expands this to literal text before LLM context assembly.

### Morphological Analysis

```markdown
## Morphological

| Token (IAST) | Lemma | POS | Inflection | Compound_role | Compound_type | Source |
|---|---|---|---|---|---|---|
| nārāyaṇaṃ | nārāyaṇa | noun | acc.sg.m | — | — | (1-Human-Sources/bodhisattvacaryavatara/commentaries/prajnakaramati-sk/ch01#1.1) |
| namaskṛtya | namas+kṛ | verb | absol | member2 | tatpuruṣa | (1-Human-Sources/bodhisattvacaryavatara/commentaries/prajnakaramati-sk/ch01#1.1) |
```

**Sanskrit-specific rules**

- Every compound must record its type (tatpuruṣa, bahuvrīhi, dvandva, avyayībhāva, karmadhāraya) and the commentary that determines the reading when ambiguous.
- Compound members are listed as separate rows with `Compound_role`: member1, member2 etc.
- When Prajñākaramati's compound analysis differs from another commentator, flag with ⚑.

**Pāli-specific rules**

- Record sandhi resolutions explicitly in a `Sandhi` column when non-trivial.
- Technical Abhidhamma terms get a `Term_scope` column: `abhidhamma-technical`, `sutta-shared`, or `common`.

### Syntactic Analysis (UCCA)

```markdown
## Syntactic (UCCA)

**Tree**
H: Scene
├── A: Participant
│   └── nārāyaṇaṃ namaskṛtya
├── A: Participant
│   └── naram
└── P: Process
    └── āditya-varṇaṃ tamasaḥ parastāt

**Node Key**
| Node | Label | Tokens | Commentary basis |
|---|---|---|---|
| H | Scene | full verse | (1-Human-Sources/bodhisattvacaryavatara/commentaries/prajnakaramati-sk/ch01#1.1) |
| A | Participant | nārāyaṇaṃ namaskṛtya | (1-Human-Sources/bodhisattvacaryavatara/commentaries/prajnakaramati-sk/ch01#1.1) |
| A | Participant | naram | (1-Human-Sources/bodhisattvacaryavatara/commentaries/prajnakaramati-sk/ch01#1.1) |
| P | Process | āditya-varṇaṃ tamasaḥ parastāt | (1-Human-Sources/bodhisattvacaryavatara/commentaries/prajnakaramati-sk/ch01#1.1) |
```

**UCCA label set**:

|Label|Full name|Label|Full name|
|---|---|---|---|
|H|Scene|E|Elaborator|
|P|Process|N|Connector|
|A|Participant|T|Terminus|
|D|Adverbial|Q|Quantifier|
|R|Relator|L|Linker|
|F|Function|C|Center|
|G|Ground|||

**Tree format rules**

- ASCII tree inline in the package file. No separate files.
- Branch nodes: `Label: FullName` (e.g. `H: Scene`, `A: Participant`)
- Leaf nodes: `Label: FullName` on the node line, tokens space-separated on the child line using `└──` with no further label
- Multi-word leaves are space-separated on a single line, never split across lines
- Tokens in IAST (Sanskrit), Romanised Pāli (Pāli), Wylie (Tibetan) — not source scripts
- When a syntactic unit spans multiple verses, the tree covers the full span and all verse refs are listed in frontmatter `syntactic_unit:`
- When commentaries support different trees, record the primary tree in full, then record the alternative tree in full under `## UCCA Divergence` with ⚑ and a note on which commentary motivates each reading

**Sanskrit-specific**: Compounds appear as single space-separated leaf tokens unless the commentary explicitly analyzes internal compound syntax, in which case the compound gets its own branch node with member tokens as children.

**Abhidhamma-specific**: Formulaic list prose generates flat parallel trees. Template files carry the full tree; instance files contain only: `tree: see [[2-Authoritative-Context/abhidhamma/context/units/[template_ref]#Layer-2]]`

### Semantic Gloss

```markdown
## Semantic Gloss

| Token (IAST) | Sense ID | Gloss (English) | Excluded senses | Commentary basis |
|---|---|---|---|---|
| dharma | dharma (cosmic order) | the moral-cosmic order sustaining the narrative frame | dharma (Buddhist phenomenon), dharma (social duty) | (1-Human-Sources/bodhisattvacaryavatara/commentaries/prajnakaramati-sk/ch01#1.1) |
| nārāyaṇa | Nārāyaṇa (Viṣṇu epithet) | Viṣṇu as the cosmic ground of being | — | (1-Human-Sources/bodhisattvacaryavatara/commentaries/prajnakaramati-sk/ch01#1.1) |
```

**Sense ID format**: `term (disambiguating phrase)` — Wikipedia disambiguation style.

- The disambiguating phrase is English even when the term is Sanskrit or Pāli.
- The phrase must uniquely identify the sense within the global concept wiki.
- Use the same ID consistently across all files. Register new IDs in `4-Wiki/`.

**Excluded senses**: List any sense the term could plausibly carry that the commentary explicitly or implicitly rules out for this passage. This field is what makes the gloss useful for downstream LLM generation — it prevents sense bleed.

**Pāli technical terms**: Add a `Tradition_scope` column for Abhidhamma files: `buddhaghosa`, `anuruddha`, `both`, or `divergent ⚑`.

### Traditional Interpretation

```markdown
## Traditional Interpretation

### [Commentary ID] — [Commentary name, language, date]
[Paraphrase of this commentary's reading of the unit. English prose.
Original language terms quoted inline in IAST/Roman when first introduced.
Every sentence cites its source passage.]
(1-Human-Sources/[text]/commentaries/[source]/[file]#[section])

### [Next commentary]
...

### Divergences
[Explicit statement of where commentaries disagree and on what grounds.
Flag each divergence type: unit boundary ⚑ | compound ⚑ (Morphological) | sense ⚑ (Semantic Gloss) | syntax ⚑ (Syntactic) | doctrine ⚑ (Traditional Interpretation)]

## Concept Links
- [[2-Authoritative-Context/bodhisattvacaryavatara/local-wiki/dharma (cosmic order)]]
- [[2-Authoritative-Context/bodhisattvacaryavatara/local-wiki/itihāsa]]
```

### Translation Dynamics

```markdown
## Translation Dynamics

| Expression | Type | Source form | Commentarial explanation | Rendering strategies | Source |
|-----------|------|------------|------------------------|---------------------|--------|
| [figure] | metaphor | [IAST] | [what commentary says] | keep+note; dissolve; domesticate | (1-Human-Sources/...#^ref) |
```

**Figure types**: metaphor, simile, synecdoche, metonymy, honorific formula, idiom, rhetorical question, technical term (rendering challenge only), cultural reference.

**Rendering strategy codes**: `keep` | `keep+note` | `substitute` | `dissolve` | `expand` | `domesticate`

- Every entry cites the commentary passage that explains the figure
- Minimum two rendering strategies per expression covering different contexts
- Divergences in how traditions handle a figure: `## Translation Dynamics Divergences` with ⚑

---

## 9. Section Summary File Format

Section summaries are compiled bottom-up from package files within the section. They never introduce new claims not present in the packages below them.

```yaml
---
ref: BCA_01          # adhyāya level
text: bodhicharyavatara
scope: adhyaya
verses: [BCA_01.001, BCA_01.002, ...]
commentary_coverage: [prajnakaramati, crosby_skilton_1995]
summary_status: draft | complete
---
```

```markdown
## Summary
[English prose synthesis of the section's content, grounded in Layer 4
interpretive notes from the verse packages below. No new claims.]

## Structural Notes
[How commentaries divide or characterize this section as a unit.]

## Key Concepts
[Links to concept pages for terms whose main development occurs in this section.]
- [[2-Authoritative-Context/bodhisattvacaryavatara/local-wiki/dharma (cosmic order)]]

## Verse Index
| Ref | Unit type | Gloss status | UCCA status | Disambiguation status |
|---|---|---|---|---|
| BCA_01.001 | single | complete | complete | complete |
```

---

## 10. Concept Page Format — Text-Local (`2-Authoritative-Context/[text]/local-wiki/`)

One file per sense ID. Filename = sense ID with spaces replaced by underscores. Example: `dharma_(cosmic_order).md`

```yaml
---
sense_id: dharma (cosmic order)
term: dharma
language: Sanskrit
text: bodhicharyavatara
attested_verses: [BCA_01.001, BCA_03.012]
commentary_coverage: [prajnakaramati, crosby_skilton_1995]
global_concept: 4-Wiki/articles/articles/dharma_(cosmic_order).md
---
```

```markdown
## Definition
[English prose definition of this sense as used specifically within this text,
grounded strictly in the commentary tradition for this text.]

## Commentary Attestations
### [Commentary ID]
[How this commentary defines or uses this sense, with citations.]

### Divergences across commentaries
[Where commentaries disagree on this sense within this text. ⚑]

## Verse Attestations
| Ref | Role in verse | Commentary basis |
|---|---|---|
| BCA_01.001 | primary sense | (1-Human-Sources/bodhisattvacaryavatara/commentaries/prajnakaramati-sk/ch01#1.1) |

## Related Senses
[Other sense IDs for the same term, with a note on how they differ.]
- dharma (social duty) — varṇāśrama obligations, distinct from cosmic-order usage
- dharma (Buddhist phenomenon) — Abhidhamma technical sense, separate tradition
```

---

## 11. Concept Page Format — Global (`4-Wiki/`)

Aggregates across all texts. Cites `2-Authoritative-Context/` only, never `1-Human-Sources/`.

```yaml
---
sense_id: dharma (cosmic order)
term: dharma
attested_texts: [bodhicharyavatara]
related_global_concepts: [dharma (social duty), dharma (Buddhist phenomenon)]
---
```

```markdown
## Cross-Text Definition
[English prose synthesis of how this sense operates across all attested texts.]

## Per-Text
### Bodhicaryāvatāra
[Summary of 2-Authoritative-Context/bodhisattvacaryavatara/local-wiki/dharma_(cosmic_order).md]
(2-Authoritative-Context/bodhisattvacaryavatara/local-wiki/dharma_(cosmic_order).md)

## Sense Boundaries
[What distinguishes this sense from related senses across all traditions.]

## Term in Other Languages
[How translators and commentators in other languages render this sense.]
```

---

## 12. Operations

### Ingest (adding a new commentary passage)

1. Confirm the passage is in `1-Human-Sources/` and registered in `index.md`
2. Identify which verse refs the passage covers
3. Determine unit boundary per Section 5
4. Open or create the package file for those refs
5. Populate or update layers 1–4 from the passage
6. Update or create text-local concept pages for any sense IDs introduced
7. Flag divergences with ⚑ where they exist
8. Update `log.md` with: date, source passage, refs updated, fields changed

### Query (answering a question against the wiki)

1. Identify relevant verse refs or concept IDs
2. Read package files and concept pages
3. Synthesize answer in English with citations to `2-Authoritative-Context/` files
4. If the answer is valuable, file it back as a new section in the relevant concept page or as a note in the relevant package file under `## Queries`

### Lint (health check)

Run periodically. Check for:

- Any field in `2-Authoritative-Context/` lacking a `1-Human-Sources/` citation → mark `status: draft`
- Any sense ID in a gloss table not registered in `4-Wiki/` → create stub
- Any `⚑` divergence flag without a `## Divergences` entry → add entry
- Any verse in `1-Human-Sources/texts/` with no package file → add to `index.md` as uncovered
- Any concept page in `4-Wiki/` citing a `2-Authoritative-Context/` file that no longer exists → flag

### Generate a Text Transformation

1. Receive explicit instruction specifying: text ref(s), transformation type, target audience
    
2. Run the resolver script to assemble the context package for the specified refs
    
3. Confirm all layers have `status: complete` — do not generate from `draft` packages
    
4. Pass the assembled context package to the generation prompt
    
5. File the output in `3-Text-Transformations/[text]/[type]/[ref]_[type].md`
    
6. Record in frontmatter which context package(s) and prompt were used:
    
    ```yaml
    ---ref: BCA_01.001transformation_type: translation | adaptation | lesson | reading-plan | scriptcontext_packages: [2-Authoritative-Context/bodhisattvacaryavatara/context/verses/BCA_01.001.md]target_audience: [description]generation_date: [ISO date]---
    ```
    

### Context Package Assembly (generation time)

The resolver script expands all transclusions before passing to the LLM. Assembly order for a verse context package:

1. Section summary (from `context/sections/`)
2. Source text (resolved from `1-Human-Sources/`)
3. Traditional Interpretation
4. Morphological, Syntactic, Semantic Gloss — in `layer_order:` sequence from frontmatter
5. Translation Dynamics
6. Relevant local-wiki concept pages
7. Frontmatter disambiguation field

---

## 13. log.md Format

Append only. Never edit existing entries.

```markdown
## [ISO date] — [Operation type]
- **Files updated**: [list]
- **Source**: [1-Human-Sources/ citation]
- **Summary**: [one sentence]
- **Divergences flagged**: [list or none]
```

---

## 14. index.md Structure

### Registered Commentaries

|ID|Full name|Language|Date|Scope|Raw path|
|---|---|---|---|---|---|
|prajnakaramati|Bodhicaryāvatārapañjikā|Sanskrit|11th c.|BCA complete|1-Human-Sources/bodhisattvacaryavatara/commentaries/prajnakaramati/|
|buddhaghosa_as|Atthasālinī|Pāli|5th c.|Dhammasaṅgaṇī|1-Human-Sources/abhidhamma/commentaries/atthasalini-pi/|

### Coverage Map

|Ref range|Package status|Commentary coverage|
|---|---|---|
|BCA_01.001–050|complete|prajnakaramati|

### Registered Domains

|Domain suffix|Scope|Example article|
|---|---|---|
|(Buddhism)|General Buddhist tradition|bodhisattva_(Buddhism).md|
|(Abhidharma)|Abhidharma/Abhidhamma technical sense|dharma_(Abhidharma).md|
|(Mahāyāna)|Mahāyāna tradition-specific|bodhicitta_(Mahāyāna).md|
|(practice)|Functional/experiential domain|meditation_(practice).md|
|(philosophy)|Doctrinal/analytical domain|emptiness_(philosophy).md|
|(epithet)|A title or honorific|sugata_(epithet).md|
|(disambiguation)|Multi-sense disambiguation page|dharma_(disambiguation).md|

New domains are added here as articles are created.

### Registered Sense IDs

|Sense ID|Term|Language|Texts|Global page|
|---|---|---|---|---|
|dharma (cosmic order)|dharma|Sanskrit|bodhisattvacaryavatara|4-Wiki/articles/dharma_(cosmic_order).md|

---

## 15. Language and Style Rules

- **Analysis language**: English throughout all compiled fields
- **Quoted terms**: original language in IAST (Sanskrit/Pāli) or appropriate romanization inline on first use, e.g. "the concept of _dharma_ (धर्म)"
- **No parametric knowledge**: if you know something about a term from training but cannot cite it to a file in `1-Human-Sources/`, do not include it
- **No consensus flattening**: when commentaries disagree, say so explicitly
- **Tense**: present tense for analytical claims ("Prajñākaramati reads this as..."), past tense for historical statements ("The Vaidya edition adopted...")
- **Abbreviations**: use registered commentary IDs throughout, never informal references
# 2-RAILS — Guidelines

This document explains the purpose, structure, and workflow of the `2-RAILS/` folder — the heart of the 🛤️ Railroad methodology.

For the LLM-facing schema see `CLAUDE.md` Sections 6–12. For blank templates see `4-SYSTEM/templates/2-rails/`. For the source material this folder is compiled from see `1-SOURCES-Guidelines.md`.

---

## 1. What This Folder Is

`2-RAILS/` is the track. It is where commentary interpretation is extracted from `1-SOURCES/` and compiled into structured, machine-readable context packages — one per verse or analytical unit — that resolve every significant ambiguity in the passage and cite the specific human source that determines each decision.

This is 🛤️ Railroad's core output. Everything else in the project either feeds into it (human sources, domain specialist review) or runs on it (text transformations, wiki articles). When the packages in this folder are complete and reviewed, any model can generate a tradition-grounded translation, adaptation, or lesson from them without redoing the philological work from scratch.

Two projects inspire this folder's design:

**[Aquifer Bible](https://aquifer.bible/)** is an open API providing freely licensed multilingual Biblical resources specifically to accelerate global Bible translation. Its core insight is that translation work becomes reliable and scalable when the underlying interpretive resources are structured, openly accessible, and language-agnostic — rather than scattered across proprietary tools and single-language scholarship. 🛤️ Railroad applies the same principle to Buddhist texts: lay the interpretive track once, openly, so that a Swahili translation, a children's adaptation, and a scholarly edition can all run on the same foundation without any of them repeating the philological groundwork.

**Andrej Karpathy's LLM wiki pattern** provides the compilation methodology: instead of feeding raw source material to an LLM at generation time and hoping it synthesises correctly, you compile that material once into a structured knowledge base. Every query and every generation task then draws on pre-compiled, verified knowledge rather than rediscovering it from scratch. Knowledge accumulates — each ingest session makes the track richer and longer.

In 🛤️ Railroad the raw material is the classical commentary tradition. The compiled knowledge base is `2-RAILS/`. The difference from a general research wiki is that every claim here must be traceable to a specific human source, every field is structured precisely for LLM consumption, and the entire system is designed for multilingual, multi-tradition aggregation rather than single-lineage philology.

The LLM is the compiler. Human domain specialists are the reviewers. Nothing in this folder is authoritative until a domain specialist has marked it complete.

---

## 2. The Core Principle: Lay the Track Once, Run Many Times

The standard approach to AI-assisted translation is to give an LLM the source text and some commentary and ask it to translate. This fails for three reasons:

1. The LLM has to do interpretive work at generation time — compound analysis, sense disambiguation, syntactic parsing — under the pressure of producing fluent output simultaneously
2. Nothing is retained between sessions — every translation of every verse starts from zero
3. There is no way to verify which interpretive decisions the LLM made or whether they are grounded in the commentary tradition

🛤️ Railroad lays the track first. By the time a verse package reaches a translation prompt, every interpretive decision is already made and cited. The LLM generating the translation does stylistic work only — it does not decide what _dharmakāya_ means in this verse, what the syntactic relationship between the two clauses is, or how Prajñākaramati reads the compound. All of that is already in the package.

This is what "authoritative context" means: not context that is authoritative because the LLM generated it, but context whose authority derives from the human commentary tradition, compiled into a form any LLM can use reliably, any number of times, for any transformation type.

---

## 3. Folder Structure

```
2-RAILS/
├── bodhisattvacaryavatara/
│   ├── sections/    # multi-level summaries 
│   │       ├── summaries.md       
│   │       └── raw/              
│   │           ├── prajnakaramati.md
│   │           ├── kunpal.md
│   │           ├── minyak-kunzang-sonam.md
│   │           └── root-text.md         
│   ├── verses/                      
│   │   ├── 1-1.md
│   │   ├── 1-2.md
│   │   └── ...
│   ├── local-wiki/                      
│   │   ├── bodhicitta_(awakening-mind).md
│   │   └── ...
│   └── local-glossary/                  
│       ├── glossary-sk-en.md
│       ├── glossary-sk-bo.md
│       └── glossary-sk-zh.md
│       └── raw/              
│            ├── sk-en-crosby.md           
│            └── sk-zh-xuanzang.md
└── abhidhamma/
    ├── context/
    │   ├── units/                       
    │   └── sections/
    │       ├── [section].md             
    │       └── references/              
    │           └── buddhaghosa.md
    ├── local-wiki/
    ├── local-glossary/
    │   ├── glossary-pi-en.md
    │   ├── glossary-pi-zh.md
    │   ├── glossary-pi-bo.md
    │   └── glossary-zh-en.md
    ├── translation-briefs/
    └── combined-glossary/
```

**Verse package files** are named by their block ID without the caret: `1-1.md`, `6-33.md`, `0-4.md`. For grouped units spanning multiple verses, name by the first verse: `1-1.md` with the range in frontmatter.

**Section files** are named by chapter number: `1.md`, `6.md`. Pre-chapter content uses `0-introduction.md`.

**Local-wiki files** are named by sense ID with spaces as underscores: `bodhicitta_(awakening-mind).md`.

**Local-glossary files** are flat single files per language pair per text: `glossary-sk-en.md`, `glossary-sk-bo.md`, `glossary-pi-en.md` etc. One entry per source lemma, all entries in a single file, alphabetically sorted. The source language is always the first tag, the target the second.

**Which pairs to create:** create a pair file for every source→target combination that is attested in the text's `1-SOURCES/` translations and commentaries. For the BCA: `sk-en`, `sk-bo`, `sk-zh`, `bo-en`, `zh-en`. For the Abhidhamma: `pi-en`, `pi-zh`, `pi-bo`, `zh-en`. A `sk-pi` pair may be created for terms shared across Sanskrit and Pāli corpora.

---

## 4. The Disambiguation Stack

Each verse package contains five layers. Each layer resolves a different type of ambiguity that would otherwise be left to the LLM at generation time:

|Level|Resolves|Key fields|
|---|---|---|
|Structural outline|How the text is divided and what each section does|TOC-as-headings with study notes per node|
|Section summary|Functional, cultural, and rhetorical context for a passage|Translator study notes per section|
|_(foundation)_ Source text|Which edition, which variants, cross-tradition witnesses|Transclusions from `1-SOURCES/`|
|Traditional Interpretation|What commentaries say is happening|Paraphrased prose per commentary + Synthesis|
|Morphological|Token segmentation, compound analysis, inflection|Token table with commentary citations|
|Syntactic (UCCA)|Sentence structure, argument relations|ASCII tree with node key|
|Semantic Gloss|Which sense of each term is active; which excluded|Interlinear gloss with WSD|
|Translation Dynamics|How to render figures of speech, idioms, and culturally bound expressions|Prose subsections per figure with rendering strategies|

Layer order within verse packages is **language-specific** — declared in frontmatter and followed by the resolver script at assembly time. See Section 6 for per-language default orders.

The structural outline and section summaries sit above the verse layers because macro context precedes micro analysis — knowing what a section is doing in the text's overall argument shapes how every verse within it is read.

Within the verse package, Traditional Interpretation is always the anchor — it comes first because it contains the commentary's reading that all formal layers encode. Translation Dynamics always comes last because it requires the formal layers to be complete before advising how to render figures.

The order of the three formal layers — Morphological, Syntactic, Semantic Gloss — varies by language and commentary tradition. Sanskrit commentaries are word-by-word, so morphology grounds syntax. Tibetan commentaries are typically holistic, so the syntactic reading from the paraphrase precedes word-level analysis. The optimal order is declared per package in frontmatter and followed by the resolver script at assembly time.

**Multi-traditional by design.** Each package aggregates interpretive authority across all available commentary traditions regardless of language — Sanskrit, Tibetan, Chinese, and others contribute to the same Layer 1. The goal is not a philologically pure single-lineage reading but the best available understanding of what the verse means, drawn from all traditions simultaneously. This is what makes the context reliable for downstream transformation into a children's adaptation, a Swahili translation, or a scholarly edition — the transformation prompt draws on the full tradition, not a single lineage.

Textual variants between source languages (Sanskrit vs. Tibetan vs. Chinese) are recorded as evidence in the Source Text block, not as a reason to split the package into separate per-language stacks.

A package with all layers complete is a self-contained interpretive unit. A translation LLM receiving this package has no interpretive work left to do.

---

## 5. Structural Outlines and Study Notes

### Why Structure Comes First

Structural context precedes verse packages. Knowing that verses 1-1 through 1-4 form the maṅgala according to Kunzang Pelden, or that Prajñākaramati treats 1-1 through 1-14 as a single unit on the excellence of bodhicitta, shapes how every verse in those ranges is interpreted and glossed. The macro structure is not neutral scaffolding — it is an interpretive claim that flows down into every layer of every package.

**Recommended ingest order:**

1. Root text structure (if the author provided explicit divisions)
2. Individual outline files — one per commentary or reference text
3. Combined outline — synthesised from all individual outlines
4. Verse packages — which reference the outline context above them

### Individual Outline File Format

One file per source. Named `references/[source-id].md`. Sources include:

- The root text itself (if the author provided an explicit outline)
- Each commentary
- Reference texts: sapche, summaries, practice instructions, teaching outlines

The document structure _is_ the structural tree. Markdown headings serve as both the outline nodes and the navigation structure — Obsidian's document outline panel renders them as a clickable TOC automatically. There is no separate tree block. Each heading is followed directly by its study note.

```markdown
---
source_id: kunzang-pelden
source_type: commentary
text: bodhisattvacaryavatara
language: Tibetan
file: 1-SOURCES/bodhisattvacaryavatara/commentaries/kunzang-pelden-bo.md
outline_basis: explicit
---

## Chapter 1: The Excellence of Bodhicitta (1-1–1-33)

This chapter opens the text by establishing why [[bodhicitta (awakening mind)]]
is worth cultivating. Kunzang Pelden characterises the chapter as a praise
(*bstod pa*) of bodhicitta's qualities, designed to inspire the reader before
the detailed practice instructions begin in later chapters. The chapter moves
from the act of homage to the Buddhas, through the statement of the text's
purpose, to an extended meditation on the rarity and extraordinary value of
the [[bodhisattva (awakening being)]] path.

The chapter addresses an implied audience who already has some familiarity
with Buddhist practice but may not yet have generated [[bodhicitta (awakening mind)]].
The tone is devotional and motivational rather than analytical.

Associated concepts: [[bodhicitta (awakening mind)]] · [[bodhisattva (awakening being)]]
· [[sugata (gone to bliss)]] · [[dharmakāya (truth body)]]
(1-SOURCES/bodhisattvacaryavatara/commentaries/kunzang-pelden-bo.md#^ch1-intro)

---

### 1.1 Homage and Statement of Purpose (1-1–1-4)

Kunzang Pelden treats these four verses as the *maṅgala* — the auspicious
opening that removes obstacles and establishes the conditions for the teaching
to be of benefit. The homage to the [[sugata (gone to bliss)]] and the
bodhisattva community is a standard feature of Indian and Tibetan śāstra
literature. The statement of purpose (*bshad par bya ba*) limits the scope
of the text to a compendium rather than a comprehensive treatise, which
Kunzang Pelden reads as an expression of [[Śāntideva]]'s humility.

The section establishes the text's two audiences: those who wish to understand
the [[bodhisattva (awakening being)]] path intellectually, and those who wish
to practise it. Both are addressed throughout the text.

Associated concepts: [[sugata (gone to bliss)]] · [[maṅgala (auspicious opening)]]
· [[śāstra (treatise)]] · [[bodhisattva (awakening being)]] · [[Śāntideva]]
(1-SOURCES/bodhisattvacaryavatara/commentaries/kunzang-pelden-bo.md#^1-1)

---

### 1.2 The Rarity and Preciousness of Bodhicitta (1-5–1-14)

[study note]

---
```

**Heading levels:**

- `##` — chapters (author-defined)
- `###` — sections (as divided by this source)
- `####` — subsections (if this source subdivides further)

Never use headings for editor-imposed divisions. If a verse range label is needed for a grouping the source treats implicitly, mark it as `[Ed: ...]` in the study note prose rather than as a heading.

**Study note rules:**

- Prose paragraph in English — concise, functional, written for a translator
- Original language terms italicised on first use; wiki link form thereafter
- Associated concepts line at the end of each note using wiki links
- Every note cites the source passage that grounds its claims
- No verse-by-verse content summary — that belongs in verse packages
- Focus on: what is this section doing, who is the implied audience, what cultural or doctrinal context does the translator need, what would be lost or misread without this note

### Combined Outline File Format

`sections/1.md` (and other section files) synthesises all individual outline files into a single master document. It follows the same structure — tree first, then study notes — but reflects the consensus across all sources and flags structural divergences.

```markdown
---
text: bodhisattvacaryavatara
sources: [root-text, prajnakaramati, kunzang-pelden, minyak-kunzang-sonam]
master_status: draft | complete
last_updated: [ISO date]
---

## Chapter 1: The Excellence of Bodhicitta (1-1–1-33)

All sources agree that this chapter establishes the motivational foundation
for the entire text by demonstrating the extraordinary value of
[[bodhicitta (awakening mind)]]. The chapter moves from homage and statement
of purpose through an extended meditation on bodhicitta's rarity and qualities.

Sources differ on whether the opening verses (1-1–1-4) form a distinct
*maṅgala* section or are continuous with the following discussion of
bodhicitta's excellence. Kunzang Pelden and Minyak Kunzang Sönam treat
them as a distinct homage unit ⚑; Prajñākaramati treats 1-1–1-14 as a
single continuous unit ⚑. The combined outline uses the finer Tibetan
division while noting this grouping divergence in each affected section.

Associated concepts: [[bodhicitta (awakening mind)]] · [[bodhisattva (awakening being)]]
· [[sugata (gone to bliss)]] · [[dharmakāya (truth body)]]

---

### 1.1 Homage and Statement of Purpose (1-1–1-4)

**Structural note:** Kunzang Pelden and Minyak Kunzang Sönam treat this as
a distinct *maṅgala* section. Prajñākaramati treats it as the opening of a
larger unit running through verse 1-14 ⚑.

These verses perform the standard śāstra opening gesture: homage establishes
auspiciousness and acknowledges the lineage; the statement of purpose sets
the scope and prepares the reader's expectation. All sources agree that the
[[sugata (gone to bliss)]] and bodhisattva retinue referenced in verse 1-1
encompasses the full field of awakened beings across all traditions.

The cultural context a translator must convey: in Indian and Tibetan literary
tradition, the opening homage is not merely ceremonial — it is an act that
generates merit and removes obstacles. A translation that renders it as
perfunctory misrepresents its function.

Associated concepts: [[sugata (gone to bliss)]] · [[maṅgala (auspicious opening)]]
· [[śāstra (treatise)]] · [[bodhisattva (awakening being)]]
· [[Śāntideva]] · [[dharmakāya (truth body)]]
```

**Combined outline rules:**

- Tree uses finest common granularity across all sources
- Structural divergences marked with ⚑ inline in the tree using blockquotes
- Study notes synthesise across all sources — state consensus first, then note per-source divergences explicitly
- Cultural context section in each combined note addresses what all translator audiences (general, scholarly, children) need to know
- Never flatten a genuine structural or interpretive divergence

### Workflow

**Phase 1 — Before verse packages:**

1. Create individual outline files from each commentary's structural divisions and introductory material
2. Compile `sections/1.md` (and other section files) — resolving into finest granularity, flagging divergences
3. Stub verse packages inherit their structural context from the outlines above

**Phase 2 — As verse packages complete:** 4. Study notes may be refined as verse-level analysis reveals section-wide patterns not visible from the structural outline alone 5. `sections/1.md` (and other section files) `master_status` is set to `complete` by a domain specialist after review

## 6. Verse Package File Format

### Frontmatter

```yaml
---
ref: 1-1                              # block ID without caret
text: bodhisattvacaryavatara
unit_type: single                     # single | group | template | instance
unit_verses: [1-1]                    # list — multiple if group
syntactic_unit: [1-1]                 # verses covered by the UCCA tree
coarser_groupings:
  prajnakaramati: [1-1, 1-2]          # commentaries that group this verse with others
template_ref:                         # for instance type only
commentary_coverage: [prajnakaramati, kunzang-pelden, minyak-kunzang-sonam]
tradition_coverage: [sanskrit, tibetan]          # traditions represented in Layer 1
concepts: [bodhicitta (awakening mind), bodhisattva (awakening being)]
# Discourse fields
speaker: shantideva                              # shantideva | objector | canonical-quote | formulaic
discourse_mode: direct                           # direct | dialogue | refutation | enumeration | formulaic
canonical_refs:                                  # parallel passages in the canon
  - ref: Mahāyānasūtrālaṃkāra 4.1
    relation: parallel
    package:                                     # link to package if in project
  - ref: SN 1.1
    relation: source-quote
    suttacentral_id: sn1.1
# Status fields
synthesis_status: draft | partial | complete
disambiguation_status: draft | partial | complete
gloss_status: draft | partial | complete
ucca_status: draft | partial | complete
translation_dynamics_status: draft | partial | complete
---
```

### Language-Specific Layer Orders

The layer order within a verse package is declared in frontmatter and followed by the resolver script when assembling context for generation. Default orders by source language:

|Source language|Layer order|Rationale|
|---|---|---|
|Sanskrit|Traditional Interpretation → Morphological → Syntactic → Semantic Gloss → Translation Dynamics|Sanskrit commentaries are word-by-word (_pada-by-pada_); morphological segmentation grounds syntactic analysis|
|Tibetan|Traditional Interpretation → Syntactic → Morphological → Semantic Gloss → Translation Dynamics|Tibetan commentaries are typically holistic; syntactic structure emerges from the paraphrase before word-level analysis|
|Pāli|Traditional Interpretation → Morphological → Syntactic → Semantic Gloss → Translation Dynamics|Buddhaghosa's commentaries are word-by-word; same rationale as Sanskrit|
|Chinese|Traditional Interpretation → Syntactic → Morphological → Semantic Gloss → Translation Dynamics|Chinese commentaries typically explain sentence meaning before individual terms|

Translation Dynamics always comes last regardless of language — it requires all formal layers to be complete.

Traditional Interpretation always comes first regardless of language — it is the anchor that all formal layers encode.

When a package draws on commentaries from multiple traditions (e.g. both Sanskrit and Tibetan), use the order appropriate to the **primary source language** of the root text being packaged.

**Status fields** are the human reviewer's responsibility:

- `draft` — LLM has populated the field, not yet reviewed
- `partial` — some commentaries ingested, coverage incomplete
- `complete` — reviewed and signed off by a domain specialist

Only `complete` packages are used for text transformation generation.

### Compact Inline Disambiguation

The frontmatter includes a `disambiguation:` field containing a compact per-token annotation of only the genuinely ambiguous interpretive decisions. This allows AI skills to get the essential interpretive choices without reading the full package. Unambiguous tokens are omitted entirely.

```yaml
disambiguation:
  sugatān: "buddhas-of-three-times not directional-sense"
  sa-gaṇān: "bahuvrīhi: with-retinue; retinue=eight-great-bodhisattvas"
  dharmakāya: "truth-body not body-of-teachings"
  verse-function: "statement-of-purpose not homage [kunzang-pelden: homage ⚑]"
```

**Format rules:**

- One entry per ambiguous token or decision only — omit clear cases
- Value: the selected reading, then `not` followed by excluded readings
- For compound analysis: `compound-type: resolved-reading`
- For doctrinal decisions (verse function, referent, scope): use a descriptive key rather than a token
- Flag divergences inline with `[commentary-id: alternative-reading ⚑]`
- Written in compressed English — not full sentences

This field is the first thing an AI skill reads when it needs the interpretive ground of a verse without processing the full disambiguation stack.

### Source Text

```markdown
## Source Text

![[1-SOURCES/bodhisattvacaryavatara/root-text-sk.md#^1-1]]

**Sanskrit Variants**
[Ed: Vaidya reads *sugatāṃ* for *sugatān* — see 1-SOURCES/bodhisattvacaryavatara/editions/vaidya-sk.md#^1-1]

**Tibetan witness**
[Ed: Tibetan translation reads *bde gshegs* (sugatān) — consistent with Sanskrit]

**Chinese witness**
[Ed: Xuanzang renders *sugatān* as 善逝 (shànshì) — confirms "gone to bliss" reading]
```

The root verse is always transcluded from the primary source language file in `1-SOURCES/` — never copied. Translations in other languages are recorded as **textual witnesses** in the Variants block when they shed light on the Sanskrit reading, not as parallel primary sources requiring separate treatment.

A witness note records:

- What the other-language version reads
- Whether it confirms or diverges from the primary source
- The implication for the Sanskrit reading, if any

Witnesses are evidence for the Source Text layer only. Their interpretive content belongs in Layer 1 under the relevant commentary section.

### Discourse Fields

The frontmatter `speaker:` and `discourse_mode:` fields tag each verse with its position in the text's rhetorical and narrative structure. These are used by section summaries to build the Discourse Analysis table and by transformation prompts to handle speaker transitions correctly.

**Speaker values:**

- `shantideva` — the author's direct voice
- `objector` — a hypothetical opponent (_pūrvapakṣin_) whose position is being addressed or refuted
- `canonical-quote` — a passage quoted from another canonical source
- `formulaic` — a standard opening, closing, or transitional formula
- `mixed` — speaker transitions within the verse (note in Layer 1)

**Discourse mode values:**

- `direct` — straightforward exposition or argument
- `dialogue` — explicit question-and-answer structure
- `refutation` — responding to an objector's position
- `enumeration` — systematic listing (especially in Abhidhamma)
- `formulaic` — standard canonical formula
- `hymn` — devotional or poetic mode

**Canonical cross-references** in frontmatter link this verse to parallel passages elsewhere in the canon. Where the parallel exists as a package in this project, link to it. Where it does not, record the external reference with a SuttaCentral ID, BDRC ID, or standard scholarly citation.

### Traditional Interpretation

The anchor for all formal analysis in layers 2–4. Aggregates interpretive authority across all available commentary traditions regardless of language. Comes first so that AI skills reading the package understand the traditional reading before encountering the formal encoding of it.

Layer 1 has four parts in order:

1. **Per-commentary sections** — one per commentary, attributed and cited
2. **Synthesis** — what all traditions agree on; the distillation that general-audience transformation prompts draw from
3. **Divergences** — where traditions genuinely disagree, with each position attributed and flagged ⚑
4. **Concept Links** — Obsidian links to local-wiki pages for key terms

The **Synthesis** is the most important section for downstream generation. A children's adaptation, a Swahili translation, or a reading guide draws primarily from Synthesis. A scholarly translation draws from the full Layer 1 including all per-commentary sections and Divergences.

```markdown
## Traditional Interpretation

### prajnakaramati — Bodhicaryāvatārapañjikā (Sanskrit, 11th c.)

Prajñākaramati opens his commentary on this verse by explaining that *sugatān*
refers collectively to all the buddhas of the three times, glossing the term
as those who have gone (*gata*) to perfect bliss (*su*) through the complete
abandonment of all obscurations.
(1-SOURCES/bodhisattvacaryavatara/commentaries/prajnakaramati-sk.md#^1-1)

He reads *sa-gaṇān* as a bahuvrīhi compound meaning "together with their
retinues," specifying that the retinues consist of the eight great bodhisattvas.
(1-SOURCES/bodhisattvacaryavatara/commentaries/prajnakaramati-sk.md#^1-1)

### kunzang-pelden — Meaningful to Behold (Tibetan, 19th c.)

Kunzang Pelden treats this verse as the text's homage (*phyag 'tshal ba*) and
explains that paying homage to the Sugatas first establishes the auspicious
conditions for the composition to be of benefit.
(1-SOURCES/bodhisattvacaryavatara/commentaries/kunzang-pelden-bo.md#^1-1)

### minyak-kunzang-sonam — A Guide to the Bodhisattva's Way of Life (Tibetan, 19th c.)

Minyak Kunzang Sönam reads this opening verse as establishing the text's
twofold purpose — removing obstacles through homage and ensuring completion
through the statement of intent — following the standard Tibetan commentarial
opening formula.
(1-SOURCES/bodhisattvacaryavatara/commentaries/minyak-kunzang-sonam-bo.md#^1-1)

### Synthesis

All traditions agree that this verse performs two functions simultaneously:
an act of homage to the awakened ones and a statement of the author's purpose
in composing the text. The Sugatas are universally understood as the fully
awakened buddhas, accompanied by the bodhisattva community. The scope of the
text is explicitly limited to a compendium (*saṅgraha*) rather than a
comprehensive treatise — all commentators treat this as Śāntideva's gesture
of humility about the work's ambition.

### Divergences

- **Scope of *sugatān***: Prajñākaramati reads this as all buddhas of the
  three times ⚑; Kunzang Pelden reads it as the buddhas of the ten directions ⚑
  — both are consistent with standard Buddhist cosmology; the Synthesis treats
  the term as referring to the buddhas generally without fixing the scope
- **Primary function of verse**: Prajñākaramati treats the verse primarily as
  the author's statement of purpose ⚑; Tibetan commentators treat it primarily
  as the homage ⚑ (doctrine) — noted in Synthesis as twofold; transformation
  prompts may foreground either function depending on context

## Concept Links
- [[2-RAILS/bodhisattvacaryavatara/local-wiki/sugata_(gone-to-bliss)]]
- [[2-RAILS/bodhisattvacaryavatara/local-wiki/dharmakaya_(truth-body)]]
- [[2-RAILS/bodhisattvacaryavatara/local-wiki/bodhicitta_(awakening-mind)]]
```

**Rules for Traditional Interpretation:**

- One section per commentary, clearly attributed with language, date, and title
- Paraphrase only — never quote commentary at length
- English prose throughout; original language terms italicised on first use
- Every sentence cites its source passage with block ID
- Synthesis states only what all traditions genuinely agree on — do not include contested readings in Synthesis
- When traditions disagree on something doctrinal or practically significant, record it in Divergences, not Synthesis
- When a divergence is cosmologically minor (ten directions vs. three times), note it in Divergences but flag it as non-blocking for general transformation
- Never flatten a genuine divergence into a false consensus in Synthesis
- Synthesis `status: draft` until reviewed by a domain specialist

**Handling incompatible doctrinal positions:** Occasionally traditions teach incompatible things — not just different framings but contradictory claims. When this occurs:

- Do not attempt a Synthesis for that point
- Record both positions fully in Divergences with `doctrine ⚑`
- Add a `transformation_note:` in frontmatter flagging that transformation prompts must explicitly choose a tradition for this verse:

```yaml
transformation_note: "verse 6-33 — Sanskrit and Tibetan traditions diverge
  on whether patience requires suppression or transformation of anger.
  Transformation prompts must specify tradition: prajnakaramati or tibetan-consensus."
```

### Morphological Analysis

```markdown
## Morphological

| Token | Lemma | POS | Inflection | Compound_role | Compound_type | Source |
|-------|-------|-----|------------|---------------|---------------|--------|
| sugatān | sugata | noun | acc.pl.m | — | — | (1-SOURCES/bodhisattvacaryavatara/commentaries/prajnakaramati-sk.md#^1-1) |
| sa-gaṇān | sa+gaṇa | noun | acc.pl.m | member1+member2 | bahuvrīhi | (1-SOURCES/bodhisattvacaryavatara/commentaries/prajnakaramati-sk.md#^1-1) |
| natvā | nam | verb | absol | — | — | (1-SOURCES/bodhisattvacaryavatara/commentaries/prajnakaramati-sk.md#^1-1) |
```

**Citation format:** `(filepath#^block-id)` pointing to the specific commentary passage that grounds the morphological reading.

**Sanskrit compounds:** every compound is analyzed with member tokens as separate rows, compound type recorded, and the commentary that determines the reading cited. Types: tatpuruṣa, bahuvrīhi, dvandva, avyayībhāva, karmadhāraya.

**Pāli sandhi:** add a `Sandhi` column when sandhi resolution is non-trivial. Technical Abhidhamma terms add a `Term_scope` column: `abhidhamma-technical`, `sutta-shared`, or `common`.

**Divergence flag ⚑:** when two commentaries analyze a compound or token differently, flag the row with ⚑ and add a `## Morphological Divergences` section.

### Syntactic Analysis (UCCA)

```markdown
## Syntactic (UCCA)

**Tree**
H: Scene
├── A: Participant
│   └── sugatān sagaṇān natvā
└── P: Process
    └── vakṣyāmi śāstrasaṅgraham

**Node Key**
| Node | Label | Tokens | Commentary basis |
|------|-------|--------|-----------------|
| H | Scene | full verse | (1-SOURCES/.../prajnakaramati-sk.md#^1-1) |
| A | Participant | sugatān sagaṇān natvā | (1-SOURCES/.../prajnakaramati-sk.md#^1-1) |
| P | Process | vakṣyāmi śāstrasaṅgraham | (1-SOURCES/.../prajnakaramati-sk.md#^1-1) |
```

**UCCA label set**

|Label|Full name|Label|Full name|
|---|---|---|---|
|H|Scene|E|Elaborator|
|P|Process|N|Connector|
|A|Participant|T|Terminus|
|D|Adverbial|Q|Quantifier|
|R|Relator|L|Linker|
|F|Function|C|Center|
|G|Ground|||

**Tree rules**

- ASCII tree inline in the package file
- Branch nodes: `Label: FullName`
- Leaf nodes: tokens space-separated on a child line
- Multi-word leaves on a single line
- Tokens in IAST (Sanskrit), Romanised Pāli (Pāli), Wylie (Tibetan) — not source scripts
- When a syntactic unit spans multiple verses, the tree covers the full span; all verses listed in frontmatter `syntactic_unit:`
- When commentaries support different trees, record the primary reading in full then add `## UCCA Divergence` with the alternative tree and ⚑

**Sanskrit compounds** appear as single leaf tokens unless the commentary analyzes internal compound syntax, in which case the compound gets its own branch node with members as children.

**Abhidhamma formulaic prose** generates flat parallel trees. Template files carry the full tree; instance files reference the template.

### Semantic Gloss (Interlinear)

The semantic gloss uses the **Obsidian Interlinear Glossing plugin** (`ling-gloss`) format. Each verse is formatted as a `gloss` code block with three aligned levels plus a free translation line.

**Line structure:**

- `\gla` — source language tokens (IAST/Romanisation/Wylie)
- `\glb` — WSD in source language: the disambiguated sense in parentheses after each token, in the source language itself
- `\glc` — English gloss: plain gloss for unambiguous tokens, disambiguating phrase in parentheses for ambiguous ones
- `t` — free translation of the verse derived from the traditional interpretation

```markdown
## Semantic Gloss

\`\`\`gloss
\gla sugatān sa-gaṇān natvā dharma-kāya-ādi-gocarān
\glb sugata(sammāgata) sa-gaṇa(saha-gaṇa) natvā dharma-kāya(chos-sku)-ādi-gocarān
\glc gone-to-bliss(buddhas-of-three-times) with-retinue(eight-great-bodhisattvas) having-paid-homage whose-scope(truth-body)-etc
t Having paid homage to the Sugatas together with their retinues, whose scope encompasses the dharmakāya and so forth
\`\`\`

**Source:** (1-SOURCES/bodhisattvacaryavatara/commentaries/prajnakaramati-sk.md#^1-1)
```

**`\glb` rules — WSD in source language:**

- For unambiguous tokens: repeat the token or lemma without parentheses
- For ambiguous tokens: append the disambiguated reading in parentheses in the source language — this is the sense the commentary selects, expressed in the source language vocabulary
- For compounds: show the resolved compound analysis: `sa-gaṇa(saha-gaṇa)` means the compound is read as "together with retinue" not another sense

**`\glc` rules — English gloss:**

- For unambiguous tokens: plain English gloss
- For ambiguous tokens: plain gloss followed by the sense in parentheses in English — matching the Wikipedia-style sense ID format
- Parenthetical disambiguations only appear where the commentary makes a specific choice that rules out other readings

**Divergences:** when commentaries gloss a token differently, record the primary reading in `\glb`/`\glc` and add a `## Gloss Divergences` section below the code block with the alternative readings flagged ⚑.

### Translation Dynamics

The final layer in the stack. Identifies every figure of speech, idiom, culturally bound expression, and rhetorical device in the verse and provides commentary-grounded rendering strategies for downstream transformation prompts.

This layer is the direct equivalent of Aquifer Bible's Translation Notes — it answers not "what does this mean?" (Layer 1) or "what does each word mean?" (Layer 4) but "how should a translator handle this?" Strategies range from keeping the source image, substituting a target-culture equivalent, dissolving into a plain statement, or adding an explanatory expansion.

```markdown
## Translation Dynamics

### sugatān... namaskṛtya — honorific formula

*sugatān... namaskṛtya* ("having paid homage to the Sugatas") is a standard
śāstra opening formula. Prajñākaramati explains it as a ritualized act of
homage that establishes the auspicious conditions for the text to benefit
its readers — it is not merely ceremonial but functionally generative.
(1-SOURCES/.../prajnakaramati-sk.md#^1-1)

Rendering strategies:
- **Scholarly**: keep the formula close to the Sanskrit — "Having paid homage
  to the Sugatas..." — with a footnote explaining the maṅgala function
- **Devotional/liturgical**: "I bow to the Sugatas..." — foregrounding the
  personal act of reverence
- **General audience**: "Honouring the Buddhas and their communities..." —
  dissolving the formula into its meaning
- **Children**: "Starting by thanking all the Buddhas..." — domesticating the
  gesture entirely

---

### dharmakāya-ādi — synecdoche

*dharmakāya-ādi* ("dharmakāya and so forth") uses synecdoche: the first of
the three buddha bodies stands for all three. Prajñākaramati and all Tibetan
commentators agree that *ādi* ("and so forth") implies *saṃbhogakāya* and
*nirmāṇakāya* — the three bodies are the full referent.
(1-SOURCES/.../prajnakaramati-sk.md#^1-1)

Rendering strategies:
- **Scholarly**: keep *dharmakāya* untranslated with footnote: "dharmakāya
  [truth body] and the other buddha bodies"
- **General audience**: "the truth body and all the qualities of a buddha"
- **Children**: "all the amazing qualities of a buddha"
- **Note**: do not render *ādi* as merely "etc." — it is a technical signal
  that a complete enumeration is implied

---

### śāstrasaṅgraham — metonymy and scope limitation

*śāstrasaṅgraham* ("a compendium of the teaching") uses *śāstra* (treatise/
teaching) to stand for the bodhisattva path itself. All commentators read
this as Śāntideva's deliberate limitation of scope — this is a compendium,
not a comprehensive treatise — which they interpret as an expression of
humility.
(1-SOURCES/.../prajnakaramati-sk.md#^1-1)

Rendering strategies:
- **Scholarly**: "a compendium of bodhisattva practice" — preserving the
  scope-limiting force of *saṅgraha*
- **General audience**: "a guide to the bodhisattva path"
- **Children**: "a guide to becoming a bodhisattva"
- **Note**: the humility gesture is culturally significant — consider whether
  to make it explicit in the target context or let it remain implicit
```

**Figure types** (for the `### heading` label): metaphor · simile · synecdoche · metonymy · honorific formula · idiom · rhetorical question · technical term (rendering challenge) · cultural reference

Use the figure type as a subtitle in the heading when it aids clarity: `### dharmakāya-ādi — synecdoche`

**Rules for Translation Dynamics:**

- One subsection per figure, idiom, or rendering challenge — use `###` headings
- Only include expressions that pose a genuine rendering challenge — do not catalogue every noun
- Prose explanation first, grounded in the commentary that identifies or explains the figure — every explanation cites its source passage
- Rendering strategies as a bulleted list, labelled by context: Scholarly · General audience · Children · Devotional · or other as needed
- Minimum two strategies per expression — at least one faithful to source register and one for a general or popular audience
- Add a **Note** bullet for anything a translator might get wrong or miss
- When traditions diverge on how to handle a figure, add a `### [expression] — Divergences` subsection with ⚑

---

## 7. Local-Wiki Articles

The `local-wiki/` folder within each text contains one page per sense ID attested in that text's commentary tradition. These pages are the text-local layer of the concept wiki — they collect everything the commentaries for this specific text say about a given sense.

```yaml
---
sense_id: bodhicitta (awakening mind)
term: bodhicitta
language: Sanskrit
text: bodhisattvacaryavatara
attested_verses: [1-15, 1-16, 2-1, ...]
commentary_coverage: [prajnakaramati, kunzang-pelden]
---
```

```markdown
## Definition

[English prose definition of this sense as it operates within this text,
grounded strictly in the commentary tradition for this text.
No cross-text comparisons here.]

## Commentary Attestations

### prajnakaramati
[How Prajñākaramati defines and develops this sense across the text,
with citations to the verse packages where it appears.]

### kunzang-pelden
[How Kunzang Pelden treats this sense, with citations.]

### Divergences
[Where commentaries disagree on this sense within this text. ⚑]

## Verse Attestations

| Verse | Role | Status | Commentary basis |
|-------|------|--------|-----------------|
| 1-15 | defined | complete | (1-SOURCES/.../prajnakaramati-sk.md#^1-15) |
| 2-1 | elaborated | partial | (1-SOURCES/.../prajnakaramati-sk.md#^2-1) |

## Related Senses

- bodhicitta (ultimate awakening mind) — the emptiness aspect; see local-wiki
- bodhicitta (conventional awakening mind) — the aspirational aspect; see local-wiki
```

Local-wiki pages grow incrementally as more verse packages are completed. They are compiled by the LLM and reviewed by domain specialists. The `attested_verses` list in frontmatter is kept current by the LLM during ingest — it is a live index of where this sense appears in the corpus.

---

## 8. Translation Briefs, Glossaries, and Terminology

This section covers two parallel structures: the descriptive layer in `2-RAILS/` (what existing translations actually did) and the prescriptive layer in `3-TRANSFORMATIONS/` (what new transformations should do). Both use the same `brief.md` + `terminology.md` file pair.

---

### 8a. Folder 2 — Descriptive Layer

#### Structure

```
2-RAILS/[text]/
├── translation-briefs/
│   ├── crosby-en/
│   │   ├── brief.md           # description of this translation's style and choices
│   │   └── terminology.md     # all attested renderings, frequency-ranked (descriptive)
│   ├── xuanzang-zh/
│   │   ├── brief.md
│   │   └── terminology.md
│   └── tibetan-bo/
│       ├── brief.md
│       └── terminology.md
└── combined-glossary/
    ├── sk-en.md               # all sk→en candidates from all translation briefs
    ├── sk-zh.md
    └── sk-bo.md
```

One `brief.md` + `terminology.md` pair per authoritative human translation in `1-SOURCES/[text]/translations/`. These are created by extracting all instances of source-language keywords and their target-language renderings from the translation file, then frequency-ranked them.

#### brief.md — Translation Brief Format

```yaml
---
brief_id: crosby-en
type: descriptive
language_pair: sk-en
source_file: 1-SOURCES/bodhisattvacaryavatara/translations/crosby-en.md
text: bodhisattvacaryavatara
translator: Crosby, Kate; Skilton, Andrew
date: 1995
style: scholarly
register: formal-academic
target_audience: scholars of Buddhist philosophy
terminology_file: translation-briefs/crosby-en/terminology.md
---
```

```markdown
# Translation Brief — Crosby & Skilton (1995)

## About This Translation

[Description of the translation's scholarly context, reception, and purpose.
Who it was written for and what it was trying to achieve.]

## Style Profile

- **Literalness**: close — favours structural correspondence over fluency
- **Technical terms**: transliterated (*bodhicitta*, *dharmakāya*) with notes
- **Register**: formal academic prose
- **Audience assumption**: reader has some familiarity with Buddhist vocabulary
- **Footnote density**: high — terminological decisions explained in notes
- **Verse rendering**: prose rather than verse in English

## Translation Philosophy

[How the translators describe their own approach, if documented.
Key choices that define this translation's character.]

## Relationship to Source Text

[Which Sanskrit edition was used. How the translators handled textual variants.
Whether Tibetan was consulted.]
```

#### terminology.md — Reference Glossary Format (Descriptive)

```yaml
---
brief_id: crosby-en
type: descriptive
language_pair: sk-en
source_file: 1-SOURCES/bodhisattvacaryavatara/translations/crosby-en.md
extraction_date: [ISO date]
total_terms: [count]
---
```

```markdown
# Reference Glossary — Crosby & Skilton (1995)

*Extracted from translation. All renderings listed by frequency.
First entry = most frequent = de facto standard for this translation.*

---

### bodhicitta

| Rendering | Frequency | Contexts |
|-----------|-----------|---------|
| bodhicitta | 31 | standard throughout |
| mind of awakening | 4 | paraphrase contexts only |

**De facto standard:** bodhicitta

---

### dharmakāya

| Rendering | Frequency | Contexts |
|-----------|-----------|---------|
| dharmakāya | 18 | standard throughout |
| dharma-body | 2 | explanatory prose only |

**De facto standard:** dharmakāya

---

### śūnyatā

| Rendering | Frequency | Contexts |
|-----------|-----------|---------|
| emptiness | 24 | standard throughout |
| voidness | 1 | one instance, possibly inconsistency |

**De facto standard:** emptiness
```

**Extraction rules:**

- Extract every source-language keyword that appears in the authoritative context packages for this text
- Record every distinct target-language rendering with its raw frequency count
- Note context briefly where a rendering is restricted to specific uses
- The most frequent rendering is automatically the de facto standard — no selection required, this is purely descriptive
- If frequency is tied, list alphabetically and note the tie

#### combined-glossary/[pair].md — Combined Glossary Format

One file per language pair. Aggregates all candidates from all translation briefs for that pair. Source is always `2-RAILS/` translation briefs — never `1-SOURCES/` or `3-TRANSFORMATIONS/` directly.

```yaml
---
language_pair: sk-en
text: bodhisattvacaryavatara
sources: [crosby-en, batchelor-en, wallace-en]
last_updated: [ISO date]
---
```

```markdown
# Combined Glossary — Sanskrit → English
## Bodhicaryāvatāra

---

### bodhicitta

| Rendering | crosby-en | batchelor-en | wallace-en | Total |
|-----------|----------|-------------|-----------|-------|
| bodhicitta | 31 | 0 | 12 | 43 |
| mind of awakening | 4 | 28 | 6 | 38 |
| awakening mind | 0 | 0 | 14 | 14 |
| bodhicitta (mind of awakening) | 0 | 4 | 0 | 4 |

**Most common by style:**
- scholarly: bodhicitta (crosby-en dominant)
- accessible: mind of awakening (batchelor-en dominant)
- contemplative: awakening mind (wallace-en dominant)

---

### dharmakāya
...
```

The "Most common by style" summary is what downstream terminology selection reads first. It clusters existing choices by translation style so a new brief author can quickly see what comparable translations chose.

---

### 8b. Folder 3 — Prescriptive Layer

#### Structure

```
3-TRANSFORMATIONS/[text]/
├── scholarly-en/
│   ├── brief.md           # transformation specification (prescriptive)
│   └── terminology.md     # selected standard terminology (prescriptive)
├── childrens-en/
│   ├── brief.md
│   └── terminology.md
└── swahili/
    ├── brief.md
    └── terminology.md
```

Same `brief.md` + `terminology.md` pair as folder 2. The `type: prescriptive` field in frontmatter distinguishes them.

#### brief.md — Transformation Brief Format (Prescriptive)

```yaml
---
brief_id: scholarly-en
type: prescriptive
language_pair: sk-en
text: bodhisattvacaryavatara
transformation_type: translation
style: scholarly
register: formal-academic
target_audience: scholars of Buddhist philosophy
reference_briefs: [crosby-en, batchelor-en]   # descriptive briefs consulted
terminology_file: scholarly-en/terminology.md
---
```

```markdown
# Transformation Brief — Scholarly English

## Purpose and Audience

[Who this transformation is for and what it is trying to achieve.
What it should and should not do.]

## Style Specification

- **Literalness**: [close | interpretive | free]
- **Technical terms**: [transliterate | translate | define-inline | footnote]
- **Register**: [formal | informal | liturgical | academic | conversational]
- **Verse rendering**: [prose | verse | mixed]
- **Audience assumption**: [specialist | general | children | practitioner]
- **Footnotes**: [yes | no | minimal]

## Constraints

[Anything the transformation must or must not do — e.g. must be suitable
for liturgical use, must avoid gendered pronouns, must not exceed X words
per verse, must follow a specific doctrinal tradition's terminology.]

## Reference Briefs Consulted

[Which existing translation briefs informed the terminology selection and why.]
```

#### terminology.md — Standard Terminology Format (Prescriptive)

```yaml
---
brief_id: scholarly-en
type: prescriptive
language_pair: sk-en
text: bodhisattvacaryavatara
source_glossary: 2-RAILS/bodhisattvacaryavatara/combined-glossary/sk-en.md
created_date: [ISO date]
last_updated: [ISO date]
---
```

```markdown
# Standard Terminology — Scholarly English

*Selected from combined glossary. Humans may override any entry or add new ones.
First entry per term = the standard. All alternatives listed for reference.*

---

### bodhicitta

**Standard:** bodhicitta
**Selected from:** crosby-en (most common scholarly-en)
**Alternatives:** mind of awakening (batchelor-en), awakening mind (wallace-en)
**Rationale:** Transliteration is standard in scholarly contexts; readers
expected to know the term.
**Override:** [human can note a different choice here with reason]

---

### dharmakāya

**Standard:** dharmakāya
**Selected from:** crosby-en and wallace-en consensus
**Alternatives:** truth body, dharma body
**Rationale:** Both scholarly briefs leave untranslated; following that consensus.
**Override:**

---

### śūnyatā

**Standard:** emptiness
**Selected from:** crosby-en (dominant across all scholarly-en sources)
**Alternatives:** voidness (archaic), openness (contemplative register)
**Rationale:** "emptiness" is the scholarly consensus in English Buddhist studies.
**Override:**
```

**Terminology rules:**

- One standard per term per brief — no ambiguity at generation time
- Every selection cites which source brief or glossary it came from
- Rationale is required — not just what was chosen but why
- Human overrides are recorded in the Override field with a reason
- New entries added by humans follow the same format
- AI draft transformations may be extracted into a `terminology.md` after generation — following the same extraction process as descriptive briefs, with `type: prescriptive` and a note that the source was an AI draft

---

### 8c. Workflow

**Creating a descriptive brief (folder 2):**

1. Identify an authoritative human translation in `1-SOURCES/[text]/translations/`
2. Create `translation-briefs/[id]/brief.md` describing the translation's style, register, audience, and philosophy
3. Extract all source-language keywords and their target renderings into `translation-briefs/[id]/terminology.md`, frequency-ranked
4. Update `combined-glossary/[pair].md` with the new source column

**Creating a prescriptive brief (folder 3):**

1. Define the transformation's audience, purpose, register, and constraints in `[transformation-id]/brief.md`
2. Open `2-RAILS/[text]/combined-glossary/[pair].md`
3. For each term, select the standard rendering from the combined glossary candidates, noting rationale
4. Record in `[transformation-id]/terminology.md`
5. Humans review and may override any selection or add new terms
6. After an AI draft transformation is generated, its terminology may be extracted and added to the terminology file as additional evidence

### Purpose

Glossaries serve a different function from local-wiki concept pages. Concept pages are interpretive — they collect what commentaries say about a _sense_. Glossaries are lexical — they collect every _word form_ attested in the text with morphological data, sense ID mapping, and structured metadata.

A glossary entry answers: what is this word, what forms does it take, what senses does it carry in this corpus, and how does it connect to the global scholarly infrastructure?

### Scope

**Local glossary** (`local-glossary/` within each text folder): one file per language pair attested in that text. Each file maps source lemmas to their target-language equivalences as established by the commentary tradition and the text's translation history. A `glossary-sk-bo.md` file answers: for each Sanskrit term in this text, what is the canonical Tibetan rendering and what do Tibetan commentators understand by it?

### Local Glossary File Format

One file per language pair per text. All entries in a single flat file, sorted alphabetically by source lemma. Each entry uses a level-3 heading as the source lemma anchor. The file captures equivalences established by the commentary tradition and the text's translation history — not dictionary definitions but attested usages grounded in the package corpus.

````markdown
---
text: bodhisattvacaryavatara
source_language: Sanskrit
source_lang_tag: sk
target_language: Tibetan
target_lang_tag: bo
script_source: IAST
script_target: Unicode Tibetan
total_lemmas: [count]
last_updated: [ISO date]
---

### bodhicitta → byang chub kyi sems

**Block ID:** ^bodhicitta
**Source lemma:** bodhicitta (Sanskrit, IAST)
**Target lemma:** byang chub kyi sems (Tibetan, Wylie)
**Target in Unicode:** བྱང་ཆུབ་ཀྱི་སེམས་
**POS:** noun (neuter) → noun
**Translation type:** calque (byang chub = bodhi, sems = citta)
**Wikidata QID:** Q209440
**Wiktionary (source):** https://en.wiktionary.org/wiki/bodhicitta
**Wiktionary (target):** https://en.wiktionary.org/wiki/byang_chub_kyi_sems

**Attested source forms in this text**

| Sanskrit form | Inflection | Verse | Tibetan rendering | Package |
|--------------|-----------|-------|------------------|---------|
| bodhicittam | nom.sg.n | 1-15 | བྱང་ཆུབ་ཀྱི་སེམས་ | [[...context/verses/1-15.md]] |
| bodhicittena | inst.sg.n | 2-1 | བྱང་ཆུབ་ཀྱི་སེམས་ཀྱིས་ | [[...context/verses/2-1.md]] |

**Sense alignment**

| Sanskrit sense ID | Tibetan equivalent | Aligned | Notes |
|------------------|--------------------|---------|-------|
| bodhicitta (awakening mind) | byang-chub-kyi-sems (awakening mind) | ✓ | full calque, same scope |
| bodhicitta (ultimate awakening mind) | don dam byang chub kyi sems | ✓ | Tibetan adds *don dam* (ultimate) explicitly |

**Translation notes**
Tibetan commentators (Kunzang Pelden, Minyak Kunzang Sönam) develop the
relative/ultimate distinction (*kun rdzob / don dam*) more explicitly than
Sanskrit commentators. When this distinction is active, the Tibetan requires
disambiguation that the Sanskrit leaves implicit.
(1-SOURCES/bodhisattvacaryavatara/commentaries/kunzang-pelden-bo.md#^1-15)

**Local-wiki link:** [[2-RAILS/bodhisattvacaryavatara/local-wiki/bodhicitta_(awakening-mind).md]]

**Wiktionary export fields**
```yaml
wiktionary:
  source_language: Sanskrit
  target_language: Tibetan
  source_lemma: bodhicitta
  target_lemma: byang chub kyi sems
  translation_type: calque
  usage_examples:
    - verse: 1-15
      source_text: "bodhicittam... [IAST]"
      target_text: "བྱང་ཆུབ་ཀྱི་སེམས་... [Tibetan]"
  notes: "Tibetan calque; relative/ultimate distinction more explicit in Tibetan"
````

**Wikidata export fields**

```yaml
wikidata:
  source_qid: Q209440
  target_qid: Q209440     # same item — same concept
  translation_property: P1368  # native label in Tibetan
  attested_in:
    - text: Bodhicaryāvatāra
      bdrc: WA1KG13126
      verse_count: 12
```

---

### dharmakāya → chos sku

[next entry]

````

**Entry fields:**
- `Block ID` — `^source-lemma` for linking from packages
- `Target lemma` — canonical target-language rendering with both script forms
- `Translation type` — calque | loan | semantic-equivalent | paraphrase | untranslated
- `Attested source forms` — every inflected source form with its target rendering in that verse
- `Sense alignment` — maps source sense IDs to target equivalents, noting gaps
- `Translation notes` — interpretive differences the translation introduces
- `Wiktionary export fields` — structured for bilingual Wiktionary entry
- `Wikidata export fields` — whether source and target share a QID or need separate items

### No Separate Cross-Language Mapping File

Cross-language mappings are captured directly in the language-pair glossary
files. `glossary-sk-bo.md` is itself the Sanskrit↔Tibetan mapping. There is
no need for a separate `glossary-cross.md` file.

### Checklist for a New Glossary Entry

- [ ] Lemma heading with block ID `^lemma`
- [ ] POS, gender, etymology recorded
- [ ] Wikidata QID found or created; field populated
- [ ] Wiktionary link added if entry exists
- [ ] All attested forms in this text listed with verse refs and package links
- [ ] All sense IDs from packages listed with verse coverage
- [ ] Local-wiki link added for each sense ID
- [ ] Wiktionary export fields populated
- [ ] Wikidata export fields populated
- [ ] Sense alignment table complete — all source sense IDs mapped to target equivalents
- [ ] Translation type recorded (calque | loan | semantic-equivalent | paraphrase | untranslated)
- [ ] Translation notes document any interpretive differences the target language introduces

---

## 9. Workflow — The Compilation Cycle

This is the core 🛤️ Railroad workflow, adapted from Karpathy's ingest → compile → query → lint cycle.

### Step 1 — Structural Ingest (Before Verse Packages)

Before any verse packages are created, the structural skeleton is established. A domain specialist adds structural outlines from commentaries and reference texts to `1-SOURCES/` and instructs the LLM:

> "Create `toc-kunzang-pelden.md` from the structural outline in `1-SOURCES/bodhisattvacaryavatara/commentaries/kunzang-pelden-bo.md`. Then update `toc-master.md` and create stub section summary files for any new sections."

The LLM:

1. Reads the commentary's structural outline
2. Creates or updates the individual TOC file
3. Updates `toc-master.md` — resolving divergences with existing outlines, flagging disagreements with ⚑
4. Creates stub section summary files for all sections in the master TOC
5. Populates Function, Cultural Context, and Discourse Function in each stub from the TOC file and any commentary introduction material
6. Appends to `log.md`

### Step 2 — Commentary Ingest (Verse Packages)

Once structural stubs are in place, verse-level ingest begins. The domain specialist instructs the LLM:

> "Ingest `1-SOURCES/bodhisattvacaryavatara/commentaries/prajnakaramati-sk.md` sections `^1-1` through `^1-10`. Populate or update verse packages for those verses. Note any new sense IDs and create local-wiki stubs for them."

The LLM:

1. Reads the commentary passage
2. Determines unit boundaries (Section 10 of CLAUDE.md)
3. Opens or creates the verse package file
4. Adds a new per-commentary section to Layer 1 for this commentary
5. Updates or creates Synthesis — marking it `draft` if new commentaries have been added that may change the consensus
6. Populates layers 2–5, citing the commentary passage for every claim
7. Flags divergences with ⚑ where this commentary disagrees with existing ones
8. Creates or updates local-wiki stubs for new sense IDs
9. Updates the Verse Index in the relevant section summary
10. Appends to `log.md`

**Incremental multi-traditional ingest:** packages are built incrementally. A package may begin with only one Sanskrit commentary and grow as Tibetan and Chinese commentaries are added. Each ingest pass adds a new Layer 1 section and prompts a Synthesis update. The `tradition_coverage:` frontmatter field tracks which traditions are represented so coverage gaps are visible.

All fields the LLM populates are marked `status: draft`.

### Step 2 — Review

A domain specialist reviews the LLM's output:

- Checks morphological analysis against their reading of the commentary
- Verifies UCCA tree reflects the commentary's syntactic interpretation
- Confirms sense IDs and excluded senses are accurate
- Reviews interpretive notes for accuracy and completeness
- Corrects errors directly in the package file
- Changes `status: draft` → `partial` or `complete` field by field

**The domain specialist is the final authority.** The LLM compiles; the specialist verifies. A package is only `complete` when a specialist has signed off on every layer.

### Step 3 — Query

Once packages are complete, contributors can query the compiled knowledge base:

> "What do the commentaries say about the relationship between _bodhicitta_ and _dharmakāya_ across chapters 1 and 9?"

The LLM reads the relevant verse packages and local-wiki pages and synthesises an answer with citations. If the answer is valuable, it is filed back into the relevant local-wiki page or a new concept page — exactly as in Karpathy's pattern where "explorations always add up" in the knowledge base.

### Step 4 — Lint

Run periodically to maintain data integrity:

- Any layer field lacking a `1-SOURCES/` citation → mark `status: draft`
- Any ⚑ flag without a `## Divergences` entry → add entry
- Any verse in `1-SOURCES/` with no package file → flag as uncovered
- Any local-wiki page whose `attested_verses` list is out of sync → update
- Any local-wiki page whose `attested_verses` list is out of sync → update
- Any local-wiki page whose `attested_verses` list is out of sync → update
- Any local-wiki page whose `attested_verses` list is out of sync → update
- Any local-wiki page whose `attested_verses` list is out of sync → update
- Any local-wiki page whose `attested_verses` list is out of sync → update
- Any local-wiki page whose `attested_verses` list is out of sync → update

### Step 5 — Generate

Once all packages for a passage are `complete`, the context package is assembled and passed to a transformation prompt. See `3-TRANSFORMATIONS-Guidelines.md` for the generation workflow.

---

## 10. Unit Boundaries and Verse Dependencies

### The Core Rule

**One file per verse, always.** File naming is always by verse ID: `6-33.md`. Dependencies between verses are handled through frontmatter metadata and context assembly — never through file naming or file merging.

This holds even when commentaries group verses differently. If Prajñākaramati treats verses 6-33 and 6-34 as one syntactic unit and Kunzang Pelden treats them separately, both verses still get their own files. The grouping difference is recorded in frontmatter.

### Dependency Types

There are three distinct cases:

**Syntactic dependency** — a verse is grammatically incomplete without an adjacent verse. A relative clause whose main clause is in the next verse, an enjambed sentence, a list that spans two verses. The UCCA tree cannot be drawn for the verse in isolation.

**Semantic dependency** — a verse is grammatically complete but a pronoun, demonstrative, or ellipsis only resolves from an adjacent verse. The morphology and syntax work in isolation but Layer 3 and Layer 4 require the adjacent verse for full disambiguation.

**Formulaic series** — the Abhidhamma case where verse N establishes a template and N+1 through N+k are mechanical variations. Each is technically complete but analytically minimal without the template.

### How Each Dependency Type Is Handled

#### Syntactic Dependency — `unit_type: group`

The UCCA tree spans both verses and lives in the first verse's file. Subsequent members of the group reference it rather than duplicating it.

**First verse of the group (6-33.md):**

```yaml
unit_type: group
syntactic_unit: [6-33, 6-34]        # all verses covered by the UCCA tree
coarser_groupings:
  prajnakaramati: [6-33, 6-34]      # commentary that motivated the grouping
```

The source text block transcluding both verses:

```markdown
## Source Text
![[root-text-sk.md#^6-33]]
![[root-text-sk.md#^6-34]]
```

Layer 3 (UCCA) contains the full tree spanning both verses. Layers 1, 2, 4, and 5 address verse 6-33 specifically.

**Subsequent verse in the group (6-34.md):**

```yaml
unit_type: group
syntactic_unit: [6-33, 6-34]
ucca_ref: see [[2-RAILS/.../context/verses/6-33.md#Layer-3]]
```

Layer 3 in 6-34.md contains only the reference — no duplication. All other layers (1, 2, 4, 5) address verse 6-34 specifically.

**When commentaries disagree on grouping:** if Prajñākaramati groups 6-33 and 6-34 syntactically but Kunzang Pelden treats them separately, use the finer granularity (separate) and record Prajñākaramati's grouping in `coarser_groupings:`. Both verses get full independent packages. The syntactic dependency is noted in Prajñākaramati's Layer 1 section.

#### Semantic Dependency — `requires_context:`

The verse gets a full independent package. The dependency is a pointer that tells the context assembly script to prepend the required verse's package at generation time.

```yaml
unit_type: single
requires_context: [6-32]
dependency_type: semantic           # semantic | pronoun | ellipsis | answer
```

The `dependency_type` field records what kind of semantic link exists:

- `semantic` — general meaning dependency
- `pronoun` — a pronoun in this verse resolves from the context verse
- `ellipsis` — an ellided element is present in the context verse
- `answer` — this verse answers a question posed in the context verse

At generation time, the resolver script prepends the `requires_context` verse packages before the current verse's package. The verses remain analytically separate — they just travel together as context.

#### Formulaic Series — `unit_type: template / instance`

The template verse carries a full package. Instance files are minimal — they point to the template for UCCA and gloss, and carry only the specific variation data that differs from the template.

```yaml
# Template file (Ds_001.md)
unit_type: template
series_id: ds-kusala-series
series_range: [Ds_001, Ds_002, ..., Ds_022]

# Instance file (Ds_002.md)
unit_type: instance
template_ref: [[.../context/units/Ds_001.md]]
series_id: ds-kusala-series
variation: [specific morphological or lexical change from template]
```

### Summary Table

|Situation|unit_type|File structure|UCCA|
|---|---|---|---|
|Verse complete alone|`single`|one file|in this file|
|Verse syntactically incomplete|`group`|one file per verse|in first verse's file; referenced from others|
|Verse semantically incomplete|`single` + `requires_context:`|one file per verse|in each file independently|
|Formulaic repetition|`template` / `instance`|one file per verse|in template; referenced from instances|

---

## 11. Citation Rules

Every claim in `2-RAILS/` must be traceable to a specific passage in `1-SOURCES/`. The citation format is:

```
(1-SOURCES/[text]/[folder]/[filename].md#^block-id)
```

Example:

```
(1-SOURCES/bodhisattvacaryavatara/commentaries/prajnakaramati-sk.md#^1-1)
```

**If you cannot cite a claim, do not make it.** Leave the field blank and mark the layer `status: draft`. This is the absolute rule of the project.

The LLM must never use its parametric knowledge as a source. If it knows something about a term from training but cannot find it in `1-SOURCES/`, it does not include it.

---

## 12. Divergence Flags

When commentaries disagree on any analytical decision, flag with ⚑ in the relevant field and add an entry in the `### Divergences` section of Traditional Interpretation.

**Divergence types:**

|Flag|Type|Where it appears|
|---|---|---|
|`unit boundary ⚑`|Commentaries group verses differently|Frontmatter `coarser_groupings:`|
|`compound ⚑`|Different compound analysis|Morphological token row|
|`sense ⚑`|Different sense assigned to a term|Semantic Gloss|
|`syntax ⚑`|Different syntactic structure|Syntactic (UCCA) tree|
|`doctrine ⚑`|Different doctrinal interpretation|Traditional Interpretation prose|

Divergences are never resolved by choosing one reading as correct. Both readings are recorded. The domain specialist may add a note on which reading they consider better supported, but both remain in the package.

This is one of 🛤️ Railroad's most important features: the commentary tradition contains genuine disagreement, and that disagreement is historically significant. Downstream transformation prompts can be instructed to follow a specific commentary's reading, or to note the divergence explicitly in a scholarly translation.

---

## 13. Coverage Tracking

Coverage is tracked in two places:

**`index.md`** — master coverage map showing which verse ranges have packages and at what status.

**Section summary verse index** — the table at the bottom of each section summary showing the status of every verse in that chapter.

Use these to prioritise ingest work. Aim to complete all layers for a section before moving to the next — a partially covered section is less useful for generation than a fully covered shorter section.

---

## 14. Checklist for a New Verse Package

- [ ] Frontmatter complete — all required fields present
- [ ] `unit_type` determined by consulting all available commentaries
- [ ] Source text transcluded from `1-SOURCES/` — not copied
- [ ] Variants noted as editorial notes with citations to edition files
- [ ] `disambiguation:` frontmatter field populated for all ambiguous tokens
- [ ] `speaker:` and `discourse_mode:` frontmatter fields set
- [ ] `canonical_refs:` frontmatter field populated where commentaries cite parallel passages
- [ ] Traditional Interpretation — one section per commentary, every sentence cited
- [ ] Synthesis written — states only what all traditions agree on
- [ ] Divergences records all genuine disagreements with ⚑
- [ ] `transformation_note:` added to frontmatter if traditions are doctrinally incompatible
- [ ] `tradition_coverage:` frontmatter field lists all traditions represented
- [ ] Textual witnesses from other languages recorded in Source Text Variants block
- [ ] `layer_order:` frontmatter field set correctly for source language
- [ ] Morphological — every token in the table, every compound analysed, all citations present
- [ ] Syntactic (UCCA) — tree reflects commentary reading, node key citations complete
- [ ] Semantic Gloss — interlinear block complete, WSD in source language, English gloss with disambiguation
- [ ] Translation Dynamics — all figures documented with prose explanations and rendering strategies
- [ ] Translation Dynamics — minimum two rendering strategies per figure, citations grounded in commentaries
- [ ] Concept links added at bottom of file
- [ ] Local-wiki pages created or updated for any new sense IDs
- [ ] `log.md` updated
- [ ] All status fields set to `draft` pending domain specialist review
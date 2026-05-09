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
├── sections/    # multi-level summaries 
│   ├── summaries.md       
│   └── raw/              
│       ├── prajnakaramati.md
│       ├── kunpal.md
│       ├── minyak-kunzang-sonam.md
│       └── root-text.md         
├── verses/                      
│   ├── 1-1.md
│   ├── 1-2.md
│   └── ...
├── local-wiki/                      
│   ├── bodhicitta_(awakening-mind).md
│   └── ...
├── local-glossary/                  
│   ├── glossary-sk-en.md
│   ├── glossary-sk-bo.md
│   └── glossary-sk-zh.md
│   └── raw/              
│        ├── sk-en-crosby.md           
│        └── sk-zh-xuanzang.md
├── translation-briefs/
│   ├── crosby-en/
│   │   ├── brief.md
│   │   └── terminology.md
│   └── ...
└── combined-glossary/
    ├── sk-en.md
    ├── sk-bo.md
    └── ...
```

**Verse package files** are named by their block ID without the caret: `1-1.md`, `6-33.md`, `0-4.md`. For grouped units spanning multiple verses, name by the first verse: `1-1.md` with the range in frontmatter.

**Section files** are named by chapter number: `1.md`, `6.md`. Pre-chapter content uses `0-introduction.md`.

**Local-wiki files** are named by sense ID with spaces as underscores: `bodhicitta_(awakening-mind).md`.

**Local-glossary files** are flat single files per language pair: `glossary-sk-en.md`, `glossary-sk-bo.md`, `glossary-pi-en.md` etc. One entry per source lemma, all entries in a single file, alphabetically sorted. The source language is always the first tag, the target the second.

**Which pairs to create:** create a pair file for every source→target combination that is attested in the text's `1-SOURCES/` translations and commentaries. For the BCA: `sk-en`, `sk-bo`, `sk-zh`, `bo-en`, `zh-en`. A `sk-pi` pair may be created for terms shared across Sanskrit and Pāli corpora.

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
file: 1-SOURCES/Commentaries/kunzang-pelden-bo.md
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
(1-SOURCES/Commentaries/kunzang-pelden-bo.md#^ch1-intro)

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
(1-SOURCES/Commentaries/kunzang-pelden-bo.md#^1-1)

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

### Source Text

```markdown
## Source Text

![[1-SOURCES/Text/sk-root-text.md#^1-1]]

**Sanskrit Variants**
[Ed: Vaidya reads *sugatāṃ* for *sugatān* — see 1-SOURCES/Text/vaidya-sk.md#^1-1]

**Tibetan witness**
[Ed: Tibetan translation reads *bde gshegs* (sugatān) — consistent with Sanskrit]

**Chinese witness**
[Ed: Xuanzang renders *sugatān* as 善逝 (shànshì) — confirms "gone to bliss" reading]
```

The root verse is always transcluded from the primary source language file in `1-SOURCES/` — never copied. Translations in other languages are recorded as **textual witnesses** in the Variants block when they shed light on the Sanskrit reading, not as parallel primary sources requiring separate treatment.

### Traditional Interpretation

```markdown
## Traditional Interpretation

### prajnakaramati — Bodhicaryāvatārapañjikā (Sanskrit, 11th c.)

Prajñākaramati opens his commentary on this verse by explaining that *sugatān*
refers collectively to all the buddhas of the three times, glossing the term
as those who have gone (*gata*) to perfect bliss (*su*) through the complete
abandonment of all obscurations.
(1-SOURCES/Commentaries/prajnakaramati-sk.md#^1-1)

He reads *sa-gaṇān* as a bahuvrīhi compound meaning "together with their
retinues," specifying that the retinues consist of the eight great bodhisattvas.
(1-SOURCES/Commentaries/prajnakaramati-sk.md#^1-1)

### kunzang-pelden — Meaningful to Behold (Tibetan, 19th c.)

Kunzang Pelden treats this verse as the text's homage (*phyag 'tshal ba*) and
explains that paying homage to the Sugatas first establishes the auspicious
conditions for the composition to be of benefit.
(1-SOURCES/Commentaries/kunzang-pelden-bo.md#^1-1)

### minyak-kunzang-sonam — A Guide to the Bodhisattva's Way of Life (Tibetan, 19th c.)

Minyak Kunzang Sönam reads this opening verse as establishing the text's
twofold purpose — removing obstacles through homage and ensuring completion
through the statement of intent — following the standard Tibetan commentarial
opening formula.
(1-SOURCES/Commentaries/minyak-kunzang-sonam-bo.md#^1-1)

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
- [[2-RAILS/local-wiki/sugata_(gone-to-bliss)]]
- [[2-RAILS/local-wiki/dharmakaya_(truth-body)]]
- [[2-RAILS/local-wiki/bodhicitta_(awakening-mind)]]
```

### Morphological Analysis

```markdown
## Morphological

| Token | Lemma | POS | Inflection | Compound_role | Compound_type | Source |
|-------|-------|-----|------------|---------------|---------------|--------|
| sugatān | sugata | noun | acc.pl.m | — | — | (1-SOURCES/Commentaries/prajnakaramati-sk.md#^1-1) |
| sa-gaṇān | sa+gaṇa | noun | acc.pl.m | member1+member2 | bahuvrīhi | (1-SOURCES/Commentaries/prajnakaramati-sk.md#^1-1) |
| natvā | nam | verb | absol | — | — | (1-SOURCES/Commentaries/prajnakaramati-sk.md#^1-1) |
```

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
| H | Scene | full verse | (1-SOURCES/Commentaries/prajnakaramati-sk.md#^1-1) |
| A | Participant | sugatān sagaṇān natvā | (1-SOURCES/Commentaries/prajnakaramati-sk.md#^1-1) |
| P | Process | vakṣyāmi śāstrasaṅgraham | (1-SOURCES/Commentaries/prajnakaramati-sk.md#^1-1) |
```

### Semantic Gloss (Interlinear)

```markdown
## Semantic Gloss

\`\`\`gloss
\gla sugatān sa-gaṇān natvā dharma-kāya-ādi-gocarān
\glb sugata(sammāgata) sa-gaṇa(saha-gaṇa) natvā dharma-kāya(chos-sku)-ādi-gocarān
\glc gone-to-bliss(buddhas-of-three-times) with-retinue(eight-great-bodhisattvas) having-paid-homage whose-scope(truth-body)-etc
t Having paid homage to the Sugatas together with their retinues, whose scope encompasses the dharmakāya and so forth
\`\`\`

**Source:** (1-SOURCES/Commentaries/prajnakaramati-sk.md#^1-1)
```

### Translation Dynamics

```markdown
## Translation Dynamics

### sugatān... namaskṛtya — honorific formula

*sugatān... namaskṛtya* ("having paid homage to the Sugatas") is a standard
śāstra opening formula. Prajñākaramati explains it as a ritualized act of
homage that establishes the auspicious conditions for the text to benefit
its readers — it is not merely ceremonial but functionally generative.
(1-SOURCES/Commentaries/prajnakaramati-sk.md#^1-1)

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
(1-SOURCES/Commentaries/prajnakaramati-sk.md#^1-1)

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
(1-SOURCES/Commentaries/prajnakaramati-sk.md#^1-1)

Rendering strategies:
- **Scholarly**: "a compendium of bodhisattva practice" — preserving the
  scope-limiting force of *saṅgraha*
- **General audience**: "a guide to the bodhisattva path"
- **Children**: "a guide to becoming a bodhisattva"
- **Note**: the humility gesture is culturally significant — consider whether
  to make it explicit in the target context or let it remain implicit
```

---

## 7. Local-Wiki Articles

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
| 1-15 | defined | complete | (1-SOURCES/Commentaries/prajnakaramati-sk.md#^1-15) |
| 2-1 | elaborated | partial | (1-SOURCES/Commentaries/prajnakaramati-sk.md#^2-1) |

## Related Senses

- bodhicitta (ultimate awakening mind) — the emptiness aspect; see local-wiki
- bodhicitta (conventional awakening mind) — the aspirational aspect; see local-wiki
```

---

## 8. Translation Briefs, Glossaries, and Terminology

### 8a. Folder 2 — Descriptive Layer

#### Structure

```
2-RAILS/
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

One `brief.md` + `terminology.md` pair per authoritative human translation in `1-SOURCES/Translations/`. These are created by extracting all instances of source-language keywords and their target-language renderings from the translation file, then frequency-ranked them.

#### brief.md — Translation Brief Format

```yaml
---
brief_id: crosby-en
type: descriptive
language_pair: sk-en
source_file: 1-SOURCES/Translations/crosby-en.md
text: bodhisattvacaryavatara
translator: Crosby, Kate; Skilton, Andrew
date: 1995
style: scholarly
register: formal-academic
target_audience: scholars of Buddhist philosophy
terminology_file: translation-briefs/crosby-en/terminology.md
---
```

#### terminology.md — Reference Glossary Format (Descriptive)

```yaml
---
brief_id: crosby-en
type: descriptive
language_pair: sk-en
source_file: 1-SOURCES/Translations/crosby-en.md
extraction_date: [ISO date]
total_terms: [count]
---
```

---

## 9. Local Glossary File Format

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
| bodhicittam | nom.sg.n | 1-15 | བྱང་ཆུབ་ཀྱི་སེམས་ | [[verses/1-15.md]] |
| bodhicittena | inst.sg.n | 2-1 | བྱང་ཆུབ་ཀྱི་སེམས་ཀྱིས་ | [[verses/2-1.md]] |

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
(1-SOURCES/Commentaries/kunzang-pelden-bo.md#^1-15)

**Local-wiki link:** [[local-wiki/bodhicitta_(awakening-mind).md]]

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

---

## 10. Workflow — The Compilation Cycle

### Step 1 — Structural Ingest (Before Verse Packages)

> "Create `toc-kunzang-pelden.md` from the structural outline in `1-SOURCES/Commentaries/kunzang-pelden-bo.md`. Then update `toc-master.md` and create stub section summary files for any new sections."

### Step 2 — Commentary Ingest (Verse Packages)

> "Ingest `1-SOURCES/Commentaries/prajnakaramati-sk.md` sections `^1-1` through `^1-10`. Populate or update verse packages for those verses. Note any new sense IDs and create local-wiki stubs for them."

---

## 11. Unit Boundaries and Verse Dependencies

### How Each Dependency Type Is Handled

#### Syntactic Dependency — `unit_type: group`

**First verse of the group (6-33.md):**

```markdown
## Source Text
![[1-SOURCES/Text/sk-root-text.md#^6-33]]
![[1-SOURCES/Text/sk-root-text.md#^6-34]]
```

---

## 11. Citation Rules

Every claim in `2-RAILS/` must be traceable to a specific passage in `1-SOURCES/`. The citation format is:

```
(1-SOURCES/[folder]/[filename].md#^block-id)
```

Example:

```
(1-SOURCES/Commentaries/prajnakaramati-sk.md#^1-1)
```

---

## 12. Divergence Flags

---

## 13. Coverage Tracking

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
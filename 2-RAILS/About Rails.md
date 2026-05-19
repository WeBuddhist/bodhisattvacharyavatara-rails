# 2-RAILS — Descriptive interpretive layer

This folder distills the human-authored material in `1-SOURCES/` into **original-language descriptive context** at every level any AI-powered transformation might need — section summaries, verse-by-verse packages, per-term local-wiki articles, bilingual glossaries. Every claim cites a specific human source (a commentary block ID, a translation passage). The authority of a rail comes from the tradition it compiles, not from the LLM that compiled it.

This README is the **authoritative document** for everything in `2-RAILS/`: the disambiguation stack, the per-folder file format, the bilingual glossary chain, the divergence-flagging convention, and the checklist for a new verse package. The LLM-facing operational summary lives in [`../4-SYSTEM/CLAUDE.md`](../4-SYSTEM/CLAUDE.md) §7–8.

Rails *describe* what the sources say. They do not *prescribe* how a new transformation should be done — that's what `3-TRANSFORMATIONS/` is for. When a transformation track introduces a new keyword rendering, it is recorded back here as one more attested choice in the corpus, alongside the renderings every other translator made.

This README is **text-agnostic** for the methodology. Vault-specific conventions live in [`../4-SYSTEM/Guidelines/vault-annex.md`](../4-SYSTEM/Guidelines/vault-annex.md).

---

## 1. Lay the track once, run many times

The standard approach to AI-assisted work on a classical text is to give an LLM the source text and some commentary and ask for an output — a translation, a summary, a lesson. This fails for three reasons:

1. The LLM has to do interpretive work at generation time — compound analysis, sense disambiguation, syntactic parsing — under the pressure of producing fluent output simultaneously.
2. Nothing is retained between sessions — every output starts from zero.
3. There is no way to verify which interpretive decisions the LLM made or whether they are grounded in the commentary tradition.

🛤️ Railroads lays the track first. By the time a verse package reaches any transformation prompt, every interpretive decision is already made and cited. The LLM generating the output does target-language work only — it does not decide what a key term means in this verse, what the syntactic relationship between two clauses is, or how a particular commentator reads the compound. All of that is already in the package.

This is what "authoritative context" means: not context that is authoritative because the LLM generated it, but context whose authority derives from the human commentary tradition, compiled into a form any LLM can use reliably, any number of times, for any transformation type.

The LLM is the compiler. Human domain specialists are the reviewers. Nothing in this folder is authoritative until a domain specialist has marked it `complete`.

---

## 2. Folder structure

```
2-RAILS/
├── Sections/ # multi-commentary summaries per TOC node
│ ├── <node-id>.md # combined: per-commentary synthesis + English translation
│ └── Raw/
│ └── <commentary-id>/
│ └── <node-id>.md # one summary per commentary per node, original language
├── Verses/ # one context package per verse
│ ├── <verse-id>.md # e.g. 1-1.md, 1-583.md, 1-0a-1.md
│ └──...
├── Local-Wiki/ # one page per attested sense ID
│ ├── <term>_(<disambiguating-phrase>).md # e.g. term_(disambiguating-phrase).md
│ └──...
└── Bilingual-Glossaries/ # bilingual glossaries per language pair
 ├── <src>-<tgt>.md # consolidated per-language-pair bilingual glossary
 └── Raw/
 ├── <src>-<tgt>-gloss.md # interlinear gloss per translation
 └── <src>-<tgt>.md # raw bilingual glossary extracted from one gloss file
```

### Naming

- **Verse package files** are named by their block ID without the caret: `1-1.md`, `1-583.md`, `1-0a-1.md`. For grouped units spanning multiple verses, name by the first verse and list the range in frontmatter.
- **Section files** are named by node ID following the source-text heading hierarchy: `1.md`, `1-1.md`, `1-0a-0.md`. The per-commentary raw summaries follow the same ID under `Raw/<commentary-id>/`.
- **Local-Wiki files** use `term_(disambiguating-phrase).md` — Wikipedia-style, spaces become hyphens, underscores between term and parenthetical.
- **Consolidated bilingual glossary files** are `<source-lang>-<target-lang>.md`. Raw inputs use the same convention with a `-gloss` suffix for interlinear files.

### Which bilingual glossary pairs to create

Create a consolidated bilingual glossary file for every source→target combination attested in the vault's `1-SOURCES/Translations/` and `1-SOURCES/Commentaries/`. The set is text-specific and is enumerated in [`../4-SYSTEM/Guidelines/vault-annex.md`](../4-SYSTEM/Guidelines/vault-annex.md) §4 for this vault.

---

## 3. The disambiguation stack

Each verse package contains layered analysis. Each layer resolves a different type of ambiguity that would otherwise be left to the LLM at generation time.

| Layer | Resolves | Key fields |
| --------------------------- | ------------------------------------------------------------------------- | ----------------------------------------------------------- |
| Structural outline | How the text is divided and what each section does | Headings-as-tree with study notes per node (in `Sections/`) |
| Section summary | Functional, cultural, and rhetorical context for a passage | Translator study notes per section (in `Sections/`) |
| *(foundation)* Source text | Which edition, which variants, cross-tradition witnesses | Transclusions from `1-SOURCES/` |
| Traditional Interpretation | What commentaries say is happening | Paraphrase per commentary + Synthesis + Divergences |
| Disambiguated restatement | A version of the verse in the original language precise enough to exclude all misreadings | A short rewrite of the verse, drawing on the synthesis |
| Word Analysis (optional) | Compound analysis, sense disambiguation, inflection — only where commentary makes a non-obvious choice | Token-level notes with citations |
| Translation Notes | Figures of speech, idioms, honorifics, culturally bound expressions | Per-figure prose with rendering strategies |

The structural outline and section summaries sit above the verse-level layers because macro context precedes micro analysis — knowing what a section is doing in the text's overall argument shapes how every verse within it is read.

Within the verse package, Traditional Interpretation is always the anchor — it comes first because it contains the commentary reading that all subsequent layers encode. The disambiguated restatement comes next because it is the artefact that most transformation skills actually consume (and without which output can drift). Word Analysis and Translation Notes are last because they only need to be populated where the commentary makes a non-obvious choice or a figure of speech requires guidance.

### Optional formal layers

Some texts and some commentary traditions warrant heavier formal apparatus — full morphological tables, UCCA-style syntactic trees, interlinear semantic glosses. These are **optional layers** layered on top of the core stack above. When they are used, they slot in between Traditional Interpretation and Translation Notes, in an order declared per-package by frontmatter `layer_order:` and followed by the resolver script at assembly time.

The optional formal-layer order is language-specific. For Sanskrit (word-by-word commentaries), morphology grounds syntax. For Tibetan (holistic commentaries), the syntactic reading from the paraphrase precedes word-level analysis. Pāli sits closer to Sanskrit. Declare per package.

### Multi-traditional by design

Each package aggregates interpretive authority across all available commentary traditions regardless of language. The goal is not a philologically pure single-lineage reading but the best available understanding of what the verse means, drawn from all traditions simultaneously. This is what makes the context reliable for downstream transformation into a children's adaptation, a translation into a new language, a daily reading plan, or a scholarly edition — the transformation prompt draws on the full tradition, not a single lineage.

Textual variants between source languages are recorded as evidence in the Source Text block, not as a reason to split the package into separate per-language stacks.

A package with all layers complete is a self-contained interpretive unit. A transformation prompt receiving this package has no interpretive work left to do.

---

## 4. Structural outlines and study notes (`Sections/`)

### Why structure comes first

Structural context precedes verse packages. Knowing that verses 1-1 through 1-4 form one functional unit according to one commentary, or that another commentary treats 1-1 through 1-14 as a single unit, shapes how every verse in those ranges is interpreted and glossed. The macro structure is not neutral scaffolding — it is an interpretive claim that flows down into every layer of every package.

### Recommended ingest order

1. Root text structure (if the author provided explicit divisions).
2. Per-commentary outlines under `Sections/Raw/<commentary-id>/<node-id>.md` — one summary per commentary per node, in the commentary's own language using the commentary's own terminology.
3. Combined outline under `Sections/<node-id>.md` — synthesises the per-commentary summaries for that node and adds an English translation underneath.
4. Verse packages — which reference the section context above them.

### Raw section summary file (`Sections/Raw/<commentary-id>/<node-id>.md`)

```markdown
---
node_id: [node-id]
commentary_id: [commentary-id-1]
language: [Language]
source_file: 1-SOURCES/Commentaries/pi-[commentary-id-1].md
status: draft | partial | complete
---

[Summary of this node drawn directly from this single commentary, in the
commentary's own language using its own terminology — no translation, no
paraphrase beyond compression. Every claim cites a block ID in the source.]
(1-SOURCES/Commentaries/pi-[commentary-id-1].md#^…)
```

Authored by the `section-summary-raw` skill.

### Combined section file (`Sections/<node-id>.md`)

```markdown
---
node_id: [node-id]
commentary_coverage: [[commentary-id-1], [commentary-id-2]]
status: draft | partial | complete
---

## Synthesis (original language)

[Synthesis across the per-commentary raw summaries, in the source/commentary
language. State consensus first, then attribute genuine divergences with ⚑.]

## English translation

[Translation of the Synthesis above. Original-language terms italicised on
first use.]

## Sources
- (2-RAILS/Sections/Raw/[commentary-id-1]/[node-id].md)
- (2-RAILS/Sections/Raw/[commentary-id-2]/[node-id].md)
```

Authored by the `section-summary-combined` skill.

### Study-note rules

- Prose paragraph, concise, written for a translator or transformation author.
- Original-language terms italicised on first use; wiki-link form thereafter (`[[Local-Wiki/<term>_(<disambiguator>).md]]`).
- Every note cites the source passage(s) that grounds its claims.
- No verse-by-verse content summary — that belongs in verse packages.
- Focus on: what is this section doing; who is the implied audience; what cultural or doctrinal context does the transformation author need; what would be lost or misread without this note.
- Never flatten a genuine structural or interpretive divergence.

---

## 5. Verse package file (`Verses/<verse-id>.md`)

### Frontmatter

```yaml
---
ref: 1-1
unit_type: single | group | template | instance
unit_verses: [1-1] # multiple if group
coarser_groupings:
 [commentary-id-1]: [1-1, 1-2] # commentaries that group this verse with others
template_ref: # for instance type only
commentary_coverage: [[commentary-id-1], [commentary-id-2]]
tradition_coverage: [theravada] # traditions represented in Traditional Interpretation
concepts: [term (disambiguating-phrase), citta (mind), …]
# Optional formal-layer ordering (only if optional formal layers are used)
layer_order: [traditional, morphological, syntactic, semantic-gloss, translation-notes]
# Status fields
status: draft | partial | complete
---
```

Only `status: complete` packages are used to generate transformations. Domain specialists set `complete`; the LLM never marks its own output complete.

### Body — the minimum required structure

```markdown
## Source Text

![[1-SOURCES/Text/[lang]-root-text.md#^1-1]]

**Variants**
[Ed: alternative reading found in <edition>, noted but not adopted here.]

## Traditional Interpretation

### [commentary-id-1] — [Commentary full name] ([language])
[Paraphrase of this commentary's reading of the verse. English. Every claim
cites the commentary block that grounds it.]
(1-SOURCES/Commentaries/pi-[commentary-id-1].md#^1-1)

### [commentary-id-2] — [Commentary full name] ([language])
[Paraphrase, citations.]
(1-SOURCES/Commentaries/pi-[commentary-id-2].md#^1-1)

### Synthesis
[What all sources agree on. Do not flatten disagreement here.]

### Divergences
[Where commentaries genuinely disagree, attributed and flagged ⚑.]

## Disambiguated Restatement (original language)

[A short rewrite of the verse in the original language, precise enough that
no misreading or mistranslation is possible. Transformation skills work
from this restatement, not from the raw verse. Cite the synthesis above.]

## Word Analysis
[Token-level notes only where the commentary makes a non-obvious choice —
compound analysis, sense disambiguation, inflection ambiguity. Each note
cites the commentary that determines the reading. Omit this section entirely
if there are no non-obvious choices.]

## Translation Notes
[Figures of speech, idioms, honorifics, cultural references — each with
rendering strategies for different audiences. Cite the commentary that
explains the figure. Minimum two rendering strategies per figure.]

## Concept Links
- [[2-RAILS/Local-Wiki/<term>_(<disambiguator>).md]]
- …
```

Keep the body in prose. No quoting commentaries at length — paraphrase. English throughout (except Disambiguated Restatement, which stays in the original language). Original-language terms italicised on first use.

Authoring skill: `verse-context`.

---

## 6. Local-Wiki articles (`Local-Wiki/<term>_(<disambiguator>).md`)

One page per attested sense ID within this text. Sense IDs are Wikipedia-style: `term (disambiguating phrase)`, e.g. `term (disambiguating-phrase)`. The filename converts the parenthetical to hyphenated lowercase with an underscore: `term_(disambiguating-phrase).md`.

```yaml
---
sense_id: [term] ([disambiguating phrase])
term: [term]
language: [Language]
attested_verses: [1-1, 1-0a-1, …]
commentary_coverage: [[commentary-id-1], [commentary-id-2]]
status: draft | partial | complete
---
```

```markdown
## Definition

[Short contextual definition of this sense as it operates within this text,
synthesised from the cited commentary explanations below. Original language.]

## Commentary Attestations

### [commentary-id-1]
[How this commentary defines and develops this sense across the text, with
citations to each verse package where it appears.]

### [commentary-id-2]
[How this commentary treats this sense, with citations.]

### Divergences
[Where commentaries disagree on this sense within this text. ⚑]

## Verse Attestations

| Verse | Role | Status | Commentary basis |
| ------ | ----------- | -------- | ---------------------------------------------------------------- |
| 1-1 | defined | complete | (1-SOURCES/Commentaries/pi-[commentary-id-1].md#^1-1) |
| 1-0a-1 | elaborated | partial | (1-SOURCES/Commentaries/pi-[commentary-id-1].md#^1-0a-1) |

## Related Senses

- [[term (alternate-sense)]] — a closely related sense distinguished by …
- [[opposite-term (opposite-sense)]] — the opposite term
```

All content in the original language (per the descriptive principle — the local wiki records what the commentaries themselves say, not how a translator would render it). The target-language side of each term lives in per-transformation files in `3-TRANSFORMATIONS/`.

Authoring skill: `local-wiki-article`.

---

## 7. Bilingual Glossaries (`Bilingual-Glossaries/`)

The bilingual glossary chain is the bridge between the descriptive corpus (every existing translator's choices) and the prescriptive transformation tracks (one chosen rendering per term, per track). It runs in four steps; the first three live in `2-RAILS/Bilingual-Glossaries/`, the fourth in `3-TRANSFORMATIONS/Translations/<track>/`.

### 7.1 Interlinear glosses (`Raw/<src>-<tgt>-gloss.md`)

For each translation in `1-SOURCES/Translations/`, build a gloss file pairing the root text against that translation verse by verse. Each verse becomes a `gloss` block in the Obsidian Interlinear Glossing plugin format (`gla` source tokens, `glb` token-by-token target glosses, `\ex` free translation). The gloss file is the single token-level alignment artefact every downstream bilingual glossary step reads.

Authoring skill: `interlinear-gloss`.

### 7.2 Raw bilingual glossaries (`Raw/<src>-<tgt>.md`)

From each gloss file, extract every source-language keyword and the rendering(s) it receives. The token-level alignment is already done in the gloss file, so this step is mostly mechanical: walk every `gla` ↔ `glb` pair, tally distinct renderings, and record sample pairings.

Authoring skill: `glossary-extract-raw`.

### 7.3 Consolidated bilingual glossary (`<src>-<tgt>.md`)

Merge every raw bilingual glossary for a language pair into one file. Each keyword's row shows every attested rendering side by side, with per-source frequencies summed. This is the file the per-track termbase reads from.

```yaml
---
text: <text-slug>
source_language: [Language]
source_lang_tag: pi
target_language: English
target_lang_tag: en
script_source: PTS romanisation
script_target: Latin
total_lemmas: <count>
last_updated: <ISO date>
---
```

```markdown
### [term] → [renderings]

**Source lemma:** [term] ([language], [script])
**POS:** adjective → adjective / noun
**Wikidata QID:** Q…
**Wiktionary (source):** https://en.wiktionary.org/wiki/[term]

**Attested renderings**

| Rendering | Translator | Frequency | Sample verse |
| -------------------- | ---------------- | --------- | ------------ |
| wholesome | Rhys Davids | 412 | 1-1 |
| skilful | Nyanaponika | 168 | 1-0a-1 |
| salutary | Bodhi | 64 | 1-1 |

**Local-Wiki link:** [[Local-Wiki/term_(disambiguating-phrase).md]]

**Translation notes**
[Free text noting why renderings diverge — different audience, different
commentary tradition, different doctrinal emphasis. Cite the local-wiki
where the sense distinctions live.]
```

Authoring skill: `glossary-combine`.

### 7.4 Per-track termbase (`3-TRANSFORMATIONS/Translations/<track>/termbase.md`)

The per-track termbase is the **prescriptive** counterpart to the consolidated bilingual glossary. It lives in the transformation track, not here — see [`../3-TRANSFORMATIONS/About Transformations.md`](../3-TRANSFORMATIONS/About Transformations.md). The `glossary-select` skill builds it from this folder's consolidated bilingual glossary plus the track's `requirements.md`. When a track derives a new rendering, the new rendering is written back into the consolidated bilingual glossary as a new attestation row.

---

## 8. Citation rules

Every claim in `2-RAILS/` must be traceable to a specific passage in `1-SOURCES/`. The citation format is:

```
(1-SOURCES/[folder]/[filename].md#^block-id)
```

Example:

```
(1-SOURCES/Commentaries/pi-[commentary-id-1].md#^1-1)
```

Hard rules:

- A claim with no `1-SOURCES/` citation is not a claim — leave the field blank and mark `status: draft`.
- A rail file may cite `1-SOURCES/` and other `2-RAILS/` files (e.g. a section file citing the raw per-commentary summaries it synthesises). It may never cite `3-TRANSFORMATIONS/`.
- Use full paths in all citations. Short wiki-links are acceptable only in `4-SYSTEM/` documentation.

---

## 9. Divergence flags

When commentaries disagree, record the disagreement explicitly. The flag is **⚑** (U+2691).

- Place ⚑ inline at the point in any field where the divergence shows up.
- Add a `### Divergences` section to the Traditional Interpretation block of the verse package (or to the synthesis section of a combined section file), attributing each position to its source.
- Never flatten a genuine divergence into a single "majority" reading. The rail's job is to surface the disagreement, not to resolve it.

If traditions teach genuinely incompatible doctrine on a verse, do not synthesise. Record both positions and add to frontmatter:

```yaml
transformation_note: "tradition must be specified for this verse"
```

Downstream transformation skills are expected to consult `transformation_note:` and either pick a tradition (per the track's `requirements.md`) or surface both readings in the output.

---

## 10. Unit boundaries — single, group, template, instance

The `unit_type:` frontmatter field on a verse package records whether the verse stands alone or is interpreted as part of a larger unit by at least one commentary.

- **`single`** — the verse is syntactically and interpretively complete on its own. The package is built around just this verse.
- **`group`** — the verse is syntactically incomplete on its own; it must be read with the surrounding verses to make sense. The first verse of the group carries the full package; the remaining verses' packages transclude the first's body and add only verse-specific notes.
- **`template`** — the verse establishes a structural pattern that subsequent verses repeat verbatim or near-verbatim (common in matrix-style passages). The template package contains the full analysis; instance packages reference it.
- **`instance`** — the verse instantiates a template established earlier. The instance package's body is mostly `template_ref:` + the verse-specific variation; the bulk of the analysis lives in the template's package.

For groups and templates, the `coarser_groupings:` field records, per commentary, which verses are read as one unit. Different commentaries may group differently; that is expected.

### How each unit type is encoded

#### Group — first verse of the group

```markdown
## Source Text
![[1-SOURCES/Text/[lang]-root-text.md#^6-33]]
![[1-SOURCES/Text/[lang]-root-text.md#^6-34]]
```

The package is otherwise the same as a `single` package; both verses' transclusions appear in Source Text, and the body analyses the unit as a whole.

#### Group — non-initial verses

```markdown
---
ref: 6-34
unit_type: group
unit_verses: [6-33, 6-34]
status: complete
---

This verse is part of the group analysed at [[2-RAILS/Verses/6-33.md]].
```

#### Template / instance

The template package is structured as a normal `single` package. Each instance package:

```yaml
---
ref: 1-30
unit_type: instance
template_ref: 2-RAILS/Verses/1-29.md
status: complete
---
```

```markdown
This verse instantiates the template at [[2-RAILS/Verses/1-29.md]]. The
substitution is: <substring-in-template> → <substring-in-this-verse>.

[Any verse-specific note that the template does not cover.]
```

---

## 11. Coverage tracking

Each `2-RAILS/` file's `commentary_coverage:` and (for verse packages) `tradition_coverage:` fields enumerate the human sources represented. Together with the `status:` field, they let a domain specialist or a coverage-reporting skill answer questions like:

- Which verses have no commentary coverage at all? (No package, or `commentary_coverage: []`.)
- Which verses are covered by only one commentary tradition? (`tradition_coverage:` length = 1.)
- Which verses are `complete` and which are still `draft` / `partial`?

There is no separate coverage-tracking file; the source of truth is the frontmatter on each rail. A planned `coverage-report` skill (see `../4-SYSTEM/Skills/SKILLS-CATALOG.md`) generates a dashboard view from these fields.

---

## 12. Compilation cycle

Build the rails for any new section of text in this order:

1. **Structural ingest** — author the per-commentary raw section summaries (`Sections/Raw/<commentary>/<node-id>.md`), then combine them into `Sections/<node-id>.md`.
2. **Commentary ingest per verse** — author the verse packages (`Verses/<verse-id>.md`), populating Traditional Interpretation, the Disambiguated Restatement, and the optional Word Analysis / Translation Notes / formal layers.
3. **Term ingest** — author or update Local-Wiki articles (`Local-Wiki/<term>_(<disambiguator>).md`) for any new sense IDs surfaced during verse-package work.
4. **Bilingual Glossary build** — author interlinear glosses (`Bilingual-Glossaries/Raw/<src>-<tgt>-gloss.md`), extract raw bilingual glossaries, then combine into the consolidated `Bilingual-Glossaries/<src>-<tgt>.md`.
5. **Domain-specialist review** — every file is reviewed claim-by-claim. The reviewer sets `status: complete` only when every field is cited and every divergence is flagged.

Transformations in `3-TRANSFORMATIONS/` consume `complete` rails to derive their own prescriptive rails (per-track termbases) and to produce their outputs. See [`../3-TRANSFORMATIONS/About Transformations.md`](../3-TRANSFORMATIONS/About Transformations.md).

---

## 13. Checklist for a new verse package

- [ ] Frontmatter complete — all required fields present.
- [ ] `unit_type` determined by consulting all available commentaries; `coarser_groupings:` filled in if any commentary groups this verse with others.
- [ ] Source text transcluded from `1-SOURCES/` — not copied.
- [ ] Variants noted as editorial notes with citations to edition files where they exist.
- [ ] Traditional Interpretation — one section per commentary, every sentence cited.
- [ ] Synthesis written — states only what all traditions agree on.
- [ ] Divergences section records all genuine disagreements with ⚑.
- [ ] `transformation_note:` added to frontmatter if traditions are doctrinally incompatible.
- [ ] `tradition_coverage:` frontmatter field lists all traditions represented.
- [ ] Textual witnesses from other languages recorded in the Source Text Variants block.
- [ ] Disambiguated Restatement written in the original language.
- [ ] Word Analysis populated only where the commentary makes a non-obvious choice — otherwise omitted.
- [ ] Translation Notes populated for every figure of speech, idiom, or culturally bound expression — minimum two rendering strategies per figure.
- [ ] Concept Links added at the bottom of the file for every key term that appears.
- [ ] Local-Wiki pages created or updated for any new sense IDs.
- [ ] All status fields set to `draft` pending domain specialist review.

---

## 14. Where to look next

- [Top-level `README.md`](../README.md) — the pipeline overview and reading paths.
- [`../1-SOURCES/About Sources.md`](../1-SOURCES/About Sources.md) — the rules for the source material that rails cite.
- [`../3-TRANSFORMATIONS/About Transformations.md`](../3-TRANSFORMATIONS/About Transformations.md) — the rules for the outputs that consume rails.
- [`../4-SYSTEM/Guidelines/0-VAULT-Structure.md`](../4-SYSTEM/Guidelines/0-VAULT-Structure.md) — the archit
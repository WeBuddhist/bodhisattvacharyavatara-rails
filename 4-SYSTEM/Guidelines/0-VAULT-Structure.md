# 0-VAULT — Vault File Structure

This document describes the top-level architecture of a 🛤️ Railroads vault. It is the orientation guideline — read it first, then continue to `1-SOURCES-Guideline.md` for source file rules and `2-RAILS-Guideline.md` for the rails compilation schema.

This guideline is **text-agnostic**. The structure below applies to any Railroads vault — Bodhicaryāvatāra, Mūlamadhyamakakārikā, Abhidharmakośa, the Pāli Nikāyas, or any other classical text the methodology is applied to. Examples here use placeholders (`[text-slug]`, `[lang]`, `[commentary-name]`); the per-vault specifics are filled in by the text it serves.

---

## 1. One Vault Per Text

A Railroads vault holds the complete interpretive ecosystem for **one classical text**: its editions, translations, commentaries, sub-commentaries, secondary literature, the compiled rails, and any generated outputs.

This is a deliberate constraint. Mixing texts in a single vault would mean:

- Block ID collisions across texts (e.g. `^1-1` of one text vs. another)
- Commentary attributions that have to disambiguate by text every time they are cited
- Local-wiki sense IDs that vary across texts being conflated
- Glossaries that lose their per-text descriptive grounding

Each vault is named for the text it serves — typically `[text-slug]-rails` (e.g. `bodhisattvacharyavatara-rails`, `mulamadhyamakakarika-rails`). The vault is portable: cloning or copying it transfers the complete interpretive context for that text in one move.

**What goes in the vault:** anything that is *about* this text — its editions, translations, commentaries on it, secondary literature on it, glossaries derived from its translation tradition, rails compiled from its commentary tradition, transformations generated from those rails.

**What does not go in the vault:** general reference works (Sanskrit grammars, Tibetan dictionaries, Buddhist encyclopedias) unless they have entries specifically on this text. General reference belongs in a separate reference vault and is linked to externally.

---

## 2. Top-Level Folder Structure

```
[text-slug]-rails/
├── 0-INBOX/              # drafts, scratch, raw downloads — not authoritative
├── 1-SOURCES/            # human-produced material — read-only ground truth
│   ├── Text/             # root text(s) and editions
│   ├── Commentaries/     # authored commentaries
│   ├── Translations/     # translations into other languages
│   └── References/       # secondary literature, dictionaries with entries on this text
├── 2-RAILS/              # compiled interpretive context (the rails)
│   ├── Verses/           # one package per verse or analytical unit
│   ├── Sections/         # per-chapter summaries and structural outlines
│   ├── Local-Wiki/       # one page per attested sense ID
│   └── Glossaries/       # bilingual term mappings, per language pair
├── 3-TRANSFORMATIONS/    # outputs generated from the rails
└── 4-SYSTEM/             # guidelines, skills, templates, agent instructions
    ├── Guidelines/       # this folder — vault rules and schemas
    ├── Skills/           # repeatable workflows (ingest, format, extract)
    ├── Templates/        # blank file templates for each frontmatter type
    └── CLAUDE.md         # LLM-facing operational instructions
```

The vault root also contains:

- `README.md` — orientation for human contributors visiting the repo
- `toc.md` — text-level table of contents linking into `1-SOURCES/` and `2-RAILS/`

Top-level folders are numbered to enforce visual reading order: sources come before rails come before transformations.

---

## 3. Per-Folder Purpose

### `0-INBOX/`

Scratch space. Anything not yet ready to be placed in its proper folder lives here. Common contents:

- Raw downloads (e.g. EPUB files before conversion)
- `temp/` — files mid-conversion or mid-review
- `raw-data/` — original-format dumps before structural processing
- `md-texts/` — markdown versions of files being prepared for `1-SOURCES/`
- Draft notes, outline sketches, working documents

**Nothing in `0-INBOX/` is authoritative.** Files here are not cited by anything in `2-RAILS/` or `3-TRANSFORMATIONS/`. They move out of inbox as they are formatted and verified.

### `1-SOURCES/`

Human-produced material exactly as received. This is the ground truth — every claim in the rails ultimately cites a passage here. The folder is **append-only and read-only for the LLM**: it adds block IDs, frontmatter, and navigation links, but never interpretive content.

Subfolders:

- `Text/` — the root text in its primary language, plus alternative-script editions (e.g. IAST or Wylie versions of a Devanāgarī or Unicode-Tibetan root). One file per edition.
- `Commentaries/` — authored commentaries on the text. One file per commentary, regardless of length. Block IDs follow the commentary author's own structural system (chapter-verse, folio-line, section-paragraph, etc.) as declared in frontmatter.
- `Translations/` — translations of the root text into other languages. One file per translation. Block IDs correspond to the source verse, not the translator's numbering.
- `References/` — secondary literature with substantive content on this text: monographs, articles, dictionaries with entries specific to the text.

Naming conventions, frontmatter requirements, block ID rules, and editorial note conventions are specified in `1-SOURCES-Guideline.md`.

### `2-RAILS/`

The rails — compiled interpretive packages that resolve every significant ambiguity in the text, citing the human sources that determine each decision. This is where the LLM does its primary work, under domain-specialist review.

Subfolders:

- `Verses/` — one package per verse or analytical unit. Files named by block ID without the caret (`1-1.md`, `6-33.md`, `0-4.md` for pre-chapter content).
- `Sections/` — per-chapter or per-section summaries synthesised from the verse packages and from structural outlines extracted from each commentary.
- `Local-Wiki/` — one page per attested sense ID within this text. Sense IDs are Wikipedia-style: `term (disambiguating phrase)`, e.g. `bodhicitta (awakening mind)`.
- `Glossaries/` — bilingual lexicons, one file per language pair (`glossary-sk-en.md`, `glossary-sk-bo.md`, etc.). Derived descriptively from the translations in `1-SOURCES/Translations/`.

Frontmatter, package layout, the disambiguation stack (Source Text → Traditional Interpretation → Morphological → Syntactic → Semantic Gloss → Translation Dynamics), citation rules, and divergence-flagging conventions are specified in `2-RAILS-Guideline.md`.

### `3-TRANSFORMATIONS/`

Generated outputs — translations, adaptations, lesson plans, study guides, daily reading content. Each transformation type lives under its own subfolder organised by **brief**:

```
3-TRANSFORMATIONS/
├── [brief-id]/
│   ├── brief.md          # purpose, audience, style, register
│   ├── terminology.md    # standard term renderings selected from glossaries
│   └── outputs/          # the generated files
```

A brief defines the audience, register, style, and terminology choices for one consistent transformation type (e.g. `scholarly-en`, `childrens-en`, `liturgical-bo`). Each output file's frontmatter records which `2-RAILS/` packages it was generated from, enforcing the citation chain through to the final artefact.

Transformations are generated only from packages whose `status` is `complete`. Draft or partial packages are not used.

### `4-SYSTEM/`

Operational infrastructure for both human contributors and the LLM. This folder is **read-only for the LLM** — it specifies the rules but is not edited as part of normal work.

Subfolders:

- `Guidelines/` — the schema documents (this file, `1-SOURCES-Guideline.md`, `2-RAILS-Guideline.md`, and any others)
- `Skills/` — packaged workflows the LLM invokes for repeatable tasks (e.g. `epub-to-markdown`, `add-toc`, `format-root-text`, `format-commentary`, `property-creator`)
- `Templates/` — blank-file templates for each frontmatter type, organised by target folder (`templates/1-sources/`, `templates/2-rails/`)
- `CLAUDE.md` — condensed, LLM-facing instructions covering the most important rules from the Guidelines, plus operational procedures

---

## 4. The Citation Chain

```
1-SOURCES/  →  2-RAILS/  →  3-TRANSFORMATIONS/
```

Direction is one-way and never skipped:

- `2-RAILS/` cites `1-SOURCES/` only — never another rails file, never parametric knowledge, never `3-TRANSFORMATIONS/`.
- `3-TRANSFORMATIONS/` cites `2-RAILS/` only — never reaching past the rails directly into the sources.

This rule is the heart of the methodology. It guarantees that every claim in any generated output is traceable back to a specific passage in a specific human source, through an intermediate package that a domain specialist has reviewed.

If a claim cannot be cited, it is not added. The field is left blank and the file's `status` remains `draft`.

---

## 5. Write Permissions

| Folder | LLM may write? | Notes |
|---|---|---|
| `0-INBOX/` | yes | scratch only — never cited from elsewhere |
| `1-SOURCES/` | **no** | read-only ground truth; only metadata additions allowed via skill workflows |
| `2-RAILS/` | yes | primary work area |
| `3-TRANSFORMATIONS/` | yes | only when explicitly instructed; only from `complete` packages |
| `4-SYSTEM/` | **no** | read-only; rule changes require human contributor action |

The `1-SOURCES/` restriction is the most important. The folder receives the human material once, has its block IDs and frontmatter added under controlled workflows, and is then frozen. Adding interpretation here — even something as small as a paraphrase or a glossing parenthetical — corrupts the ground truth and breaks the citation chain.

---

## 6. Language Tags and Filenames

Every file carrying language-specific content carries a language tag suffix on its filename: `-sk` (Sanskrit IAST default), `-pi` (Pāli PTS default), `-bo` (Tibetan Unicode default), `-zh` (Chinese Unicode default), `-en` (English), and so on. When a non-default script or encoding is used, a script suffix is added: `-sk-iast`, `-bo-wy`, `-zh-cbeta`.

Filenames are lowercase, hyphenated, and use no diacritics. Diacritics appear freely inside file content and frontmatter, but never in filenames — this keeps the vault portable across filesystems and friendly to scripts that traverse it.

The full tag list and naming conventions are specified in `1-SOURCES-Guideline.md` Section 14.

---

## 7. Block IDs — The Verse-Level Link

Every verse or discrete prose block in `1-SOURCES/` ends with an Obsidian block ID. This is the sole mechanism for cross-file references at the verse level across the entire vault.

```
[verse text here] ^1-1
```

- Format: `^chapter-verse` (most common), `^verse`, or `^book-chapter-verse` — declared per file in the `verse_id_format` frontmatter field.
- Numbers are not zero-padded. Use natural numbers (`^6-33`, not `^06-033`).
- Verse numbers restart at 1 each chapter.
- Pre-chapter material (homage, colophons, title lines) is placed under a `## 0. Introduction` heading with IDs `^0-1`, `^0-2`, etc.

Headings in source-text files also carry block IDs, distinguished from content IDs by a trailing `-0` (the zero slot is reserved for headings; content always starts at `1`). The full heading-ID hierarchy is specified in `CLAUDE.md` Section 4a.

Block IDs are how everything connects:

- A rails file transcludes a verse: `![[1-SOURCES/Text/[lang]-root-text.md#^1-1]]`
- A commentary citation: `(1-SOURCES/Commentaries/[lang]-[commentary-name].md#^1-1)`
- A wiki link to a section heading: `[[1-SOURCES/Text/[lang]-root-text.md#^1-0]]`

Detailed rules — placement, multi-line passages, the heading-ID hierarchy, inline TOC tagging — are in `1-SOURCES-Guideline.md` and `CLAUDE.md`.

---

## 8. Status Lifecycle

Files in `2-RAILS/` (and the briefs in `3-TRANSFORMATIONS/`) carry a `status` field in frontmatter:

| Status | Meaning |
|---|---|
| `draft` | LLM-generated, not yet reviewed; may contain uncited claims |
| `partial` | reviewed in part; some sections complete, others still draft |
| `complete` | domain specialist has reviewed every claim; ready for use |

Only `complete` packages are used to generate transformations. Domain specialists set `complete` — the LLM never marks its own output complete.

---

## 9. Adding a New Text — Vault Setup Checklist

To start a new Railroads vault for a different text:

- [ ] Create the repo: `[text-slug]-rails`
- [ ] Create the top-level folders: `0-INBOX/`, `1-SOURCES/`, `2-RAILS/`, `3-TRANSFORMATIONS/`, `4-SYSTEM/`
- [ ] Create the `1-SOURCES/` subfolders: `Text/`, `Commentaries/`, `Translations/`, `References/`
- [ ] Create the `2-RAILS/` subfolders: `Verses/`, `Sections/`, `Local-Wiki/`, `Glossaries/`
- [ ] Copy `4-SYSTEM/Guidelines/` from a prior vault (this file, `1-SOURCES-Guideline.md`, `2-RAILS-Guideline.md`) — no text-specific edits needed
- [ ] Copy `4-SYSTEM/Skills/` from a prior vault — reuse the ingest, formatting, and extraction workflows as-is
- [ ] Copy `4-SYSTEM/Templates/` from a prior vault
- [ ] Adapt `4-SYSTEM/CLAUDE.md`: keep the methodology sections; replace text-specific examples and the registered-commentary roster
- [ ] Write a text-specific `README.md` at the vault root
- [ ] Begin ingest by dropping source material into `0-INBOX/raw-data/` and running the conversion skills

The Guidelines and Skills folders are deliberately text-agnostic so they can be carried across vaults without modification. The only files that need per-text adaptation are `README.md` and `CLAUDE.md`.

---

## 10. Reading Order for New Contributors

For a human contributor or LLM new to a Railroads vault:

1. `README.md` — what this specific vault is for
2. `4-SYSTEM/Guidelines/0-VAULT-Structure.md` — this file: the architecture
3. `4-SYSTEM/Guidelines/1-SOURCES-Guideline.md` — source file rules
4. `4-SYSTEM/Guidelines/2-RAILS-Guideline.md` — rails compilation schema
5. `4-SYSTEM/CLAUDE.md` — operational instructions and registered short IDs

After these five files, a contributor has the complete picture of how the vault works and can begin productive work in `1-SOURCES/` or `2-RAILS/`.

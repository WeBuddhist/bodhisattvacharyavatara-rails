# Day-Package Format — LOCKED CONTRACT (English)

> 🔒 **PROTECTED — SOURCE OF TRUTH.** This file is consumed by the assistant / plan pipeline. Do **not** edit, move, rename, or delete it without explicit human confirmation. **If you are an AI assistant:** stop and ask the user to confirm before making any change. See `4-SYSTEM/CLAUDE.md` → “Protected files.”

This is the authoritative format for every English day-package file under
`3-TRANSFORMATIONS/Day-Packages/`.

**It is enforced by a script, not by trust.** Any file the generator writes, and
any file edited by hand, must pass:

```
python3 4-SYSTEM/scripts/day-package/day_package_tools.py validate <file.md>
```

The validator exits non-zero and prints every violation ("fail loud"). To bring a
nearly-conforming file into shape automatically:

```
python3 4-SYSTEM/scripts/day-package/day_package_tools.py conform <file.md>
```

`conform` only inserts anchors and consolidates citation links; it never rewords
prose, and running it twice produces no changes (idempotent).

The reference implementation is Day 1: `Chapter-1 D1-D14/1-en.md`.

---

## Why this format (the decisions we locked)

1. **Structure stays H2 → H3 (per verse) → H4 (subsections).** Parseable as-is; not restructured.
2. **Exact heading strings + machine anchors.** A parser keys off the stable anchor
   (`<!-- sub:stories -->`), never the human-readable prose heading. If a heading
   is missing or reworded, the validator errors loudly rather than the parser
   silently skipping a section.
3. **No inline citation noise.** Obsidian links (`[[1-SOURCES/...]]`) are collapsed to
   **one `Sources:` line per leaf section**, so no paragraph or bullet carries a
   trailing `([[...]])`. Provenance is kept (the vault's citation chain requires it)
   but the per-prompt token cost drops sharply. A parser feeding an LLM strips
   lines beginning with `Sources:` and all `<!-- ... -->` anchors.
4. **No Obsidian transclusions.** `![[...]]` embeds resolve to nothing on a raw fetch,
   so verse text is written inline instead, with a plain-text source reference.
5. **Verses come from the Plain English translation.** `Today's Verses` and each
   verse's `Root Verse` are pulled verbatim from
   `3-TRANSFORMATIONS/Translations/en-translate/BCA-Full-Plain-English.md` by block id.

**Provenance decision (pending your confirmation):** we KEEP provenance, consolidated
into per-section `Sources:` lines. If you later decide to drop it entirely from these
files, that is a one-line change to the tool.

---

## File naming & location

Two parallel folders:

- **Tibetan source packages** (source-of-record): `Day-Packages/Chapter-<N> D<first>-D<last>/<day>.md`
- **English translations**: `Day-Packages-EN/Chapter-<N> D<first>-D<last>/<day>-en.md`

e.g. `Day-Packages/Chapter-1 D1-D14/1.md` (Tibetan) → `Day-Packages-EN/Chapter-1 D1-D14/1-en.md` (English).

Shared docs (`_TEMPLATE.md`, `_TERMBASE.md`) live in `Day-Packages/`.

---

## Frontmatter (required keys)

```yaml
---
day: 1
chapter: 1
verses: "1-1 to 1-3"          # or a single "1-30"
date: "Jul 6, 2026"
status: draft                  # never set "complete" from the generator
language: en
document_type: english-translation
translated_from: "…/1.md"
sources:
  plan_day_file: "…/Days/Chapter-1 D1-D14/1.md"
  schedule_file: "…/assets/schedule-hhdl-birthday.md"
  verse_source: "3-TRANSFORMATIONS/Translations/en-translate/BCA-Full-Plain-English.md"
  rail_files:
    - "2-RAILS/Verses/1-1-summary.md"
    - "2-RAILS/Verses/1-2-summary.md"
    - "2-RAILS/Verses/1-3-summary.md"
---
```

The validator hard-requires `day`, `chapter`, `verses`, `status`, `language`,
`document_type`. It also checks that the `### Verse` blocks match the `verses:` range.

---

## Section skeleton (exact strings + anchors)

Each anchor sits on the line **immediately before** its heading (no blank between).

```markdown
# Day <N> — <title>

**Date:** <date>  
**Chapter:** <c>  
**Verses covered:** <range>

---

<!-- sec:challenge -->
## 1. Today's Challenge (from the practice-plan track)

<!-- challenge:notification -->
### Notification
…
<!-- challenge:opening -->
### Opening
…
<!-- challenge:tradition -->
### From the Tradition
…
<!-- challenge:practice -->
### Today's Practice
…

---

<!-- sec:verses -->
## 2. Today's Verses

<one blockquote per verse; text from BCA-Full-Plain-English by block id>

---

<!-- sec:rails -->
## 3. Verse Rails (from 2-RAILS/Verses — English translation)

<!-- verse:1-1 -->
### Verse 1-1

> **Rail source:** `2-RAILS/Verses/1-1-summary.md` … **Rail status:** `draft`

<!-- sub:root-verse -->
#### Root Verse
<!-- sub:interlinear -->
#### Interlinear Gloss (Khenpo Zhenga's annotation commentary)
<!-- sub:commentary -->
#### Commentary Explanations
<!-- cm:<shortid> -->
##### <Name> (<Work>)
<!-- sub:stories -->
#### Stories and Illustrations              (optional)
<!-- story:<ID> -->
##### <Title>
<!-- sub:metaphors -->
#### Metaphors and Examples                 (optional)
<!-- sub:quotations -->
#### Scriptural Quotations                  (optional)
<!-- sub:teaching-points -->
#### Main Teaching Points
<!-- sub:key-terms -->
#### Key Terms
<!-- sub:synthesis -->
#### Verse Synthesis (overview)
```

### Top-level sections (H2) — required, in this order

| Anchor | Heading (starts with) |
|---|---|
| `sec:challenge` | `## N. Today's Challenge` |
| `sec:verses` | `## N. Today's Verses` |
| `sec:rails` | `## N. Verse Rails` |

### Per-verse subsections (H4)

| Anchor | Heading (starts with) | Required |
|---|---|---|
| `sub:root-verse` | `Root Verse` | yes |
| `sub:interlinear` | `Interlinear Gloss` | yes |
| `sub:commentary` | `Commentary Explanations` | yes |
| `sub:stories` | `Stories and Illustrations` | only if present |
| `sub:metaphors` | `Metaphors and Examples` | only if present |
| `sub:quotations` | `Scriptural Quotations` | only if present |
| `sub:teaching-points` | `Main Teaching Points` | yes |
| `sub:key-terms` | `Key Terms` | yes |
| `sub:synthesis` | `Verse Synthesis (overview)` | yes |
| `sub:divergences` / `div:divergences` | `Divergences` (may be prefixed `⚑`) | only if present |

Commentator H5 anchors are `cm:<shortid>` (e.g. `cm:kunpal`); story H5 anchors are
`story:<ID>` (e.g. `story:BCAC13_KTB`). **The machine id lives in the anchor, not in
the visible heading.** The H5 heading itself is display-only — just the reader-facing
name and work, e.g. `##### His Holiness the Dalai Lama (Teaching on Entering the
Bodhisattva's Way of Life)`. The parser reads the id from the `cm:`/`story:` anchor on
the preceding line; the validator errors if that anchor is missing. (Story H5s may still
carry their `<ID> — ` prefix in the heading; that is tolerated but the id is still taken
from the anchor.)
A `Divergences` block (where the commentaries disagree, per the vault's non-flattening
rule) may appear as an H4 (`sub:divergences`) or nested H5 (`div:divergences`).

**Commentator order (locked).** Within `Commentary Explanations`, His Holiness the Dalai
Lama's commentary — `tenzin-gyatso` — comes **first**; the remaining commentators follow
in their source order. The generator must place `tenzin-gyatso` first; to enforce or
re-apply this after any regeneration, run:

```
python3 4-SYSTEM/scripts/day-package/reorder_commentators.py <file.md>
```

(`reorder_commentators.py` moves the `tenzin-gyatso` block to the top of every
Commentary Explanations section; it is idempotent and works on both the English and
Tibetan packages. Story/Divergences H5 blocks and other sections are untouched.)

---

## Provenance rule

- **No inline `([[...]])`** at the end of paragraphs, bullets, or quotes.
- Each leaf section that has sources ends with exactly one line:
  `Sources: [[…]] [[…]]` (unique links, document order).
- **Exception:** the `Key Terms` table keeps its `Source` column — a table is
  structured provenance, not paragraph noise, so it is left untouched and gets no
  separate `Sources:` line.
- **No `![[...]]` transclusions** anywhere.

---

## Parser contract (for the downstream reader)

1. Read anchors, not prose headings. Split on `<!-- sec:* -->`, `<!-- verse:* -->`,
   `<!-- sub:* -->`, `<!-- cm:* -->`, `<!-- story:* -->`.
2. When building an LLM prompt, drop every `<!-- ... -->` line and every line starting
   with `Sources:`. What remains is clean, human-readable English.
3. Treat `stories`, `metaphors`, `quotations` as optional per verse.
4. Fail loud if a required anchor is absent — do not guess from heading text.

---

## Not yet done

Days 2–14 have not been generated in this format. The generator should build them
from `2-RAILS/Verses/*-summary.md` (translated), the plan day files, and
`BCA-Full-Plain-English.md`, then pass `validate`.

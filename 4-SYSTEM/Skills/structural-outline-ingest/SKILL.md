---
name: structural-outline-ingest
description: Extract the structural outline of one source (commentary, root text, or reference) and write an individual outline file in 2-RAILS/sections/raw/. Run this skill before any verse package work. One source at a time.
---

# Structural Outline Ingest

This skill reads a single source from `1-SOURCES/` and produces an individual outline file in `2-RAILS/sections/raw/[source-id].md`. It is **Phase 1** of the 2-RAILS compilation cycle — structural outlines must exist before verse packages can be built.

The output is **not** a summary of every verse. It is a structural tree with translator-facing study notes: what each chapter and section is *doing*, who the implied audience is, and what cultural or doctrinal context a translator would lose without the note. Verse-level content belongs in verse packages, not here.

---

## When to run this skill

Run once per source, before beginning verse packages for that chapter. Sources to process, in recommended order:

1. The root text itself (if Śāntideva provides explicit divisions — check for numbered or titled sections)
2. Kunzang Pelden (`bo-མི་ཉག་ཀུན་བསོད།.md` / Kunzang Pelden's commentary) — most pedagogically developed Tibetan outline
3. Minyak Kunzang Sönam — close lineage, useful triangulation
4. Prajñākaramati — Sanskrit tradition; divisions often different from Tibetan
5. Any other commentary in `1-SOURCES/Commentaries/`

After running this skill on two or more sources for the same chapter, run the **combined-outline-compiler** skill to synthesise them into `2-RAILS/sections/[chapter].md`.

---

## Input

The user provides a **source ID** — the short identifier used throughout the project. Confirm the corresponding file path:

| Source ID | File in 1-SOURCES |
|---|---|
| `kunzang-pelden` | `1-SOURCES/Commentaries/bo-མི་ཉག་ཀུན་བསོད།.md` (or similar) |
| `minyak-kunzang-sonam` | `1-SOURCES/Commentaries/bo-ས་བཟང་མ་ཏི་...` (check actual filename) |
| `prajnakaramati` | `1-SOURCES/Commentaries/bo-ཤེས་རབ་འབྱུང་གནས་བློ་གྲོས། Prajñākaramati.md` |
| `root-text` | `1-SOURCES/Text/sk-dev-root-text.md` |

If the source ID is ambiguous, ask the user to confirm the file before proceeding.

**Output path:** `2-RAILS/sections/raw/[source-id].md`

---

## Step 1 — Read the source file

Read the source file from `1-SOURCES/`. Focus on:

- The **opening pages**: title, author's stated purpose, any explicit table of contents or section list
- **Structural markers**: in Tibetan commentaries these are *sa bcad* (outline labels, often rendered in the epub as `[!sabche]` callout blocks or bold text); in Sanskrit commentaries, numbered sub-topics; in Chinese commentaries, chapter headings
- **Chapter and section boundaries**: wherever the source author transitions from one major topic to another
- The **colophon or closing section**: sometimes contains the author's own characterisation of the work's structure

You do **not** need to read every verse of commentary prose. Skim chapter by chapter, extracting structural markers and reading enough surrounding prose to write a meaningful study note for each section. For long commentaries (over 200 pages), read the structural markers and the opening paragraph of each major section; skip verse-by-verse commentary bodies.

---

## Step 2 — Determine `outline_basis`

Set `outline_basis` in frontmatter:

- **`explicit`**: the source contains clearly marked structural divisions — a table of contents, numbered sections, *sa bcad* labels, or titled chapter headings that the author placed in the text
- **`implicit`**: no explicit markers; structure must be inferred from topic transitions and commentary logic

Most Tibetan commentaries are `explicit` (they use *sa bcad* outline labels). Prajñākaramati is largely `implicit` at the sub-chapter level — he provides *adhikāra* (topic) labels but not a full structural outline. Mark any inferred boundary with `[Ed: implied division]` in the study note.

---

## Step 3 — Build the heading tree

The heading tree **is** the structural outline. Do not produce a separate block or list — the markdown heading structure itself encodes the tree, and Obsidian's document outline panel renders it as a clickable TOC automatically.

**Heading levels:**

| Level | Use |
|---|---|
| `##` | Chapters (author-defined) |
| `###` | Sections (as divided by this source) |
| `####` | Subsections (only if this source divides further) |

**Heading format:**
```
## Chapter N: [Title] ([verse range])
### N.M [Section title] ([verse range])
#### N.M.P [Subsection title] ([verse range])
```

Verse ranges use the block ID format without the caret: `1-1`, `6-33`. For chapters where the range is not yet confirmed, omit the range and add `[Ed: range unconfirmed]` in the study note.

**Pre-chapter content** (title, homage, colophon, scribal introduction) goes under `## 0. Introduction`.

**Never** use headings for editor-imposed groupings. If you want to name a grouping that the source treats implicitly, do so in the study note prose, not as a heading — and mark it `[Ed: ...]`.

---

## Step 4 — Write study notes

Immediately after each heading, write the study note. No blank heading — every structural node gets a note.

**Study note structure:**

1. **Opening sentence**: what this chapter or section is *doing* in the text's argument. Use an active verb: "establishes," "refutes," "enumerates," "demonstrates," "transitions."
2. **Implied audience**: who the source author seems to be addressing at this point — renunciates, general Mahāyāna practitioners, scholars, beginners? Some sources shift audience mid-text.
3. **Cultural or doctrinal context**: what a translator must know to represent this section faithfully. Think: what would be invisible to a reader without Buddhist training, or lost in a language without these concepts?
4. **What would be missed without this note**: one concrete example of a translation or adaptation error this study note prevents.
5. **Associated concepts line**: wiki links to sense IDs relevant to this section, on their own line at the end of the note.
6. **Citation**: the source passage that grounds the note's claims.

**Prose rules:**
- English throughout
- Original-language terms italicised on first use: *bodhicitta*, *sa bcad*, *maṅgala*
- After first use, use the wiki link form: `[[bodhicitta (awakening mind)]]`
- Present tense for analytical claims ("Kunzang Pelden reads this as…"); past tense for historical statements
- **Do not** summarise verses — that belongs in verse packages. Write about what the *section* is doing, not what each verse says.
- **Do not** exceed four paragraphs per study note. Concision is a feature.

**Citation format:**
```
(1-SOURCES/Commentaries/[filename].md#^block-id)
```

If the source passage does not yet have a block ID (i.e., the file hasn't been fully formatted), cite the chapter and section as closely as possible and add `[Ed: block ID pending]`.

---

## Step 5 — Mark divergences

If you already know from other sources that *this* source's structural division diverges from the consensus, mark it in the study note with ⚑ and a brief note. This is not required at this stage — divergences are fully resolved in the **combined-outline-compiler** step — but flagging known divergences now makes that step faster.

Example:
> Prajñākaramati treats verses 1-1 through 1-14 as a single undivided unit ⚑; Tibetan commentators subdivide this range into two or three sections.

---

## Step 6 — Write the output file

Write the complete file to `2-RAILS/sections/raw/[source-id].md`.

### Frontmatter template

```yaml
---
source_id: [source-id]
source_type: commentary | root-text | translation | reference
text: bodhisattvacaryavatara
language: [Sanskrit | Tibetan | Chinese | English]
lang_tag: [sk | bo | zh | en]
file: 1-SOURCES/[folder]/[filename].md
outline_basis: explicit | implicit
chapters_covered: [1, 2, 3]   # list only chapters whose outline is complete in this file
ingest_date: [ISO date]
ingest_status: draft | partial | complete
---
```

`ingest_status`:
- `draft` — structure is roughed in but study notes are thin or uncited
- `partial` — some chapters complete, others stubbed
- `complete` — all chapters processed, all study notes cited; ready for combined-outline-compiler

### Full file template

```markdown
---
[frontmatter]
---

## 0. Introduction ([verse range or "pre-chapter"])

[Study note: what the opening homage, title declaration, or scribal introduction
does. Who is being addressed. What the colophon, if present at the opening,
tells us about transmission context.]

Associated concepts: [[maṅgala (auspicious opening)]] · [[śāstra (treatise)]]
([citation])

---

## Chapter 1: [Title from this source] (1-1–1-N)

[Study note: what the chapter does in the text's overall argument. Implied
audience. Cultural context a translator needs. What would be lost without
this note.]

Associated concepts: [[bodhicitta (awakening mind)]] · [[bodhisattva (awakening being)]]
([citation])

---

### 1.1 [Section title] (1-1–1-N)

[Study note.]

Associated concepts: [[sugata (gone to bliss)]] · [[maṅgala (auspicious opening)]]
([citation])

---

### 1.2 [Section title] (1-N–1-M)

[Study note.]

Associated concepts: [...]
([citation])

---

## Chapter 2: [Title] (2-1–2-N)

[...]
```

Use `---` horizontal rules to separate structural nodes at the `##` level. At `###` and `####` level, the blank line between heading and study note is sufficient — no extra `---` needed.

---

## Step 7 — Post-write check

Before finishing, verify:

- [ ] Frontmatter complete and accurate
- [ ] Every heading has a study note (no bare headings)
- [ ] Every study note has at least one citation — or is marked `[Ed: citation pending]` with `ingest_status: draft`
- [ ] Every concept mentioned in study notes appears in the Associated concepts line
- [ ] Verse ranges are in `chapter-verse` format (e.g. `1-1`, not `I.1` or `v.1`)
- [ ] No verse-by-verse content summaries in any note
- [ ] `ingest_status` reflects actual completeness

---

## Source-type specifics

### Tibetan commentaries

Tibetan commentaries typically open with a *sa bcad* (outline label) before each section — these are the `[!sabche]` callout blocks in the epub-converted markdown. They are the most reliable structural markers. Use them as heading titles directly (translate the Tibetan *sa bcad* label into English for the heading, keep the original Tibetan in the study note prose italicised).

If the file was converted via the `epub-to-markdown` skill, the *sa bcad* labels appear as:
```
> [!sabche]
> ས་བཅད་ཀྱི་ཡིག་
```
These map directly to `###` headings. The chapter-level divisions map to `##`.

### Sanskrit commentaries (Prajñākaramati)

Prajñākaramati does not use *sa bcad*-style labels. Structural divisions must be inferred from:
- *adhikāra* labels (topic headings like *"atha bodhicittasyotpādaḥ"*)
- Explicit transitional phrases (*"idānīm..." — "Now..."*)
- The logic of his commentary sequence

Mark all inferred boundaries `[Ed: implied division]`.

### Root text

The root text's structural outline reflects Śāntideva's own chapter and, if any, sub-chapter divisions. For the BCA, chapters are author-defined. Sub-chapter divisions within the root text are **not** author-defined — if you divide within chapters for the root text outline file, mark every such division `[Ed: editorial grouping]`.

---

## Dos and Don'ts

- **DO** read structural markers carefully; skim verse-by-verse prose
- **DO** write study notes for a translator who knows Buddhist practice but may not know this specific text
- **DO** flag ⚑ when you already know this source diverges structurally from others
- **DO** cite even rough block-ID locations — an approximate citation is better than none
- **DON'T** summarise verse content in study notes — that's for verse packages
- **DON'T** impose your own structural divisions — report the source's divisions
- **DON'T** use `####` for editor-imposed groupings; use prose and `[Ed: ...]` instead
- **DON'T** mark `ingest_status: complete` unless every chapter has cited study notes
- **DON'T** start verse packages for a chapter until at least two outline files for that chapter exist and `ingest_status` is at least `partial` for both

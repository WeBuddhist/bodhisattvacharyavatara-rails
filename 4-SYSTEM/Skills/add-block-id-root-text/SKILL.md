---
name: format-sk-root-text
description: Format and re-index Sanskrit root-text files in 1-SOURCES/Text/ using the vault's block ID convention. Handles front matter (Roman), chapter verses (Arabic), colophons (lowercase letters), and book back matter. Specific to Sanskrit root texts — not commentaries.
---

# Format Sanskrit Root Text

This skill applies the vault's block ID convention to a Sanskrit root-text `.md` file. It is **not** for commentaries or translations of commentaries.

---

## Workflow

The skill uses a helper script `apply.py` located in the same directory as this SKILL.md. Always follow this order:

### 1 — Script reads the file (audit)

`apply.py` is in the same directory as this skill file. Construct the path at runtime from the skill's own location:

```bash
python "<this-skill-dir>/apply.py" audit "<path-to-file.md>"
```

The audit prints:
- Heading structure with gaps flagged
- Every block without an ID, labelled `[auto]` or `[needs LLM judgment]`
- Verse counts per chapter vs. Sanskrit expected
- Other issues (null bytes, bad spacing, multiple blanks)

### 2 — LLM identifies zones

Read the audit output. For every block marked `[needs LLM judgment]`, determine its zone by reading the content:
- Is it front matter, a chapter intro, a verse, a chapter colophon, or book back matter?
- Does it contain an interpolated verse (duplicate source number → `^C-Vx1`)?
- Is it a multi-line stanza (ID goes on the **last** line only)?

Note any decisions that the script cannot apply automatically.

### 3 — Script applies mechanical changes

```bash
python "<this-skill-dir>/apply.py" apply "<path-to-file.md>"
```

The script handles:
- `^0`, `^I-0`, `^N-0` heading IDs
- `^0-N` → `^I-N` legacy ID fixes
- `^N-a` for known chapter colophon lines
- `^C-N` verse IDs from ordinal prefixes (`N. verse text`) — prefix stripped after
- `^a`, `^b`… for book back-matter blocks
- Blank lines between verse blocks, null bytes, spacing normalisation

After applying it prints a fresh audit showing what remains.

### 4 — LLM applies remaining changes

For anything still flagged — ambiguous blocks, interpolated verses, multi-line stanzas, colophons not matching known patterns — apply the IDs and edits directly using the Edit tool.

---

## Block ID Convention

Sanskrit root texts follow a **three-zone** scheme based on content role, not heading level:

### Zone markers

| Zone | Symbol | Rule |
|---|---|---|
| Pre-title intro | `T` | Content before the `#` title heading: `^T-1`, `^T-2`… |
| Front matter | Roman numeral (`I`, `II`…) | Sections and content preceding Chapter 1 |
| Main verses | Arabic numeral (`1`, `2`…) | Chapter and verse numbers |
| Back matter | Lowercase letter (`a`, `b`…) | Colophons, appendices, closing material |

### Heading IDs

| Heading level and role | ID format | Example |
|---|---|---|
| `#` — book is the root (no collection above it) | `^0` | `# शबोधिचर्यावतारः ^0` |
| `#` — collection title (book is at `##`) | no ID | `# Abhidhammapiṭake` |
| `##` — book under a collection | `^1-0`, `^2-0`… | `## Dhammasaṅgaṇī ^1-0` |
| `##` or `###` — front matter section heading | `^I-0`, `^II-0`… | `## Introduction ^I-0` |
| `##` or `###` — chapter heading | `^N-0` | `## 1. Chapter One ^1-0` |
| `##` or `###` — back matter section (after last chapter) | `^a-0`, `^b-0`… | `## Colophon ^a-0` |

### Content IDs

| Content type | ID format | Example |
|---|---|---|
| Pre-title block | `^T-N` | `^T-1` |
| Front matter content | `^I-N`, `^II-N`… | `^I-1`, `^I-2` |
| Chapter intro (before first verse) | `^N-I`, `^N-II`… | `^1-I`, `^1-II` |
| Chapter verse | `^N-V` | `^1-1`, `^6-134` |
| Chapter colophon / back matter | `^N-a`, `^N-b`… | `^8-a` |
| Book colophon (standalone, after last chapter) | `^a`, `^b`… | `^a` |

### Interpolated / extra verses (duplicate source numbers)

Some Sanskrit editions include verses that share the same number as an adjacent verse. The source signals this in several ways:

- Verse number marker appears twice: `॥24॥ … ॥24॥`
- Printed edition uses repeated ordinals: `24. verse / 24. verse`
- A verse carries no number marker at all between two numbered verses

When the source shows duplicate numbering at position V, assign:

| Situation | ID format | Example |
|---|---|---|
| First (canonical) occurrence | `^C-V` | `^8-24` |
| Second occurrence (one duplicate) | `^C-Vx1` | `^8-24x1` |
| Third occurrence (two duplicates) | `^C-Vx2` | `^8-24x2` |

**Rule**: Never use a bare `^C-Vx` — always append the counter starting at `1`, even when there is only one duplicate. The next canonical verse is unaffected: `^8-24`, `^8-24x1`, `^8-25`.

### Constraints
- **Verse IDs only**: `^chapter-verse` or `^chapter-subsection-verse` — max 3 segments (not counting the `xN` suffix on interpolated verses).
- Verse counter is **per-chapter** (restarts at 1 for each `##` chapter).
- Verse numbers come from `॥N॥` markers in the Sanskrit text when present; otherwise count stanzas.

---

## Step 0 — OCR Cleanup (run before any other step)

OCR-sourced files frequently contain artifacts that must be removed **before** parsing block structure. Failure to clean first causes spurious blocks and incorrect ID counts.

### Standalone line numbers
Many scanned texts embed page or folio line-numbers as standalone paragraphs:

```
1

सुगतान् ससुतान् सधर्मकायान्...

2

प्रणिपत्यादरतोऽखिलांश्च वन्द्यान्।
```

These number-only blocks (`^\d+\s*$`) are **not content** — remove them entirely. Do not assign block IDs to them.

Detection pattern (Python): `re.compile(r'^\d+\s*(?:\^[\w-]+)?\s*$')`

### Leading ordinal prefixes on content blocks

OCR or copy-paste from printed editions sometimes prepends a number followed by a period or parenthesis. **Do not strip these in Step 0.** Leave them in place until Step 3 (indexing), because on verse blocks the number may be the source's own verse number — stripping it early loses the information needed to assign the correct `^C-V`.

**At indexing time (Step 3)**, for each prefixed non-heading line:

1. **Is the block a verse?** — Read the prefix as the source verse number. Use it to set `V` in `^C-V`. If the same number appears on two consecutive verse blocks, the second gets `^C-Vx1` (see *Interpolated / extra verses* above). After the ID is assigned, remove the prefix from the rendered line.
2. **Is the block front matter, pre-title, or back matter?** — The number carries no indexing meaning. Remove the prefix and assign the zone ID normally.
3. **Is the block a heading (`##` / `###`)?** — Do not touch. The number is an intentional structural label.

| Content zone | When to strip | Notes |
|---|---|---|
| Verse (`^N-V`) | After reading as verse number | Informs `V`; strip after ID is set |
| Front matter / pre-title / back matter | At indexing time | No indexing value; strip and assign zone ID |
| `##` / `###` heading | **Never** | Preserve exactly |

Detection pattern (Python — apply only to non-heading lines after ID assignment): `re.sub(r'^\d+[.)]\s*', '', line)`

### Other OCR artifacts to remove
- Stray characters on Sanskrit syllables from PDF extraction.
- Hyphenation artifacts at line breaks.
- Page headers/footers repeated in the text body (e.g. `-116-`, `[p. 42]`).

### Block boundary after cleanup
After removal, collapse any sequences of multiple blank lines into a single blank line. A single blank line is the only block separator.

---

## Step 1 — Read and identify structure semantically

**Heading position alone is not sufficient to determine a block's role.** A prose block or verse appearing after a heading may belong to that heading's section, or it may be transitional material, a colophon, or chapter intro that looks like body content. Read the content to confirm.

### 1a — Read the full text
Read the file in full before assigning any IDs.

### 1b — Identify each block's content role by reading it
For every block (verse, prose line, or standalone phrase), determine its role:

- **Pre-title** (`^T-N`): content physically before the `#` title heading.
- **Front matter** (`^I-N`…): content whose topic is the author's own introduction, maṅgala, dedication, or statement of purpose — regardless of whether it sits under an explicit heading. Does NOT include the first verse of Chapter 1 even if no `##` heading separates them.
- **Chapter intro** (`^C-I`…): prose or verse at the start of a chapter, before the first numbered verse, that introduces the chapter topic. Identified by content, not position.
- **Verse** (`^C-V`): the metrically defined stanzas of the root text. Use `॥V॥` markers where present; otherwise identify by metre and content.
- **Chapter colophon** (`^C-a`…): Sanskrit closing phrase after the last verse of a chapter (e.g. ending `परिच्छेदः।`). Often has no heading and is easily mistaken for body content — read it to confirm it closes the chapter rather than continuing it.
- **Book colophon** (`^a`…): closing phrase(s) after the final chapter (e.g. `समाप्तः`, `कृतिः`, `इति`).

### 1c — Note any ambiguous blocks
If a block's role is genuinely unclear after reading, add an editorial note `[Ed: role uncertain — treated as X]` inline and flag it for human review.

### 1d — Audit existing IDs
Note any existing block IDs and whether they follow the convention above.

---

## Step 2 — Apply heading IDs

- `#` book title → `^0` (if book is root) or no ID (if collection).
- `##`/`###` front matter headings → `^I-0`, `^II-0`… in order of appearance.
- `##`/`###` chapter headings → `^N-0` where N matches the chapter number.

---

## Step 3 — Apply content IDs

### Front matter
- Content under front matter headings: `^I-1`, `^I-2`… (reset for each Roman section).
- If front matter has no sub-heading, use `^I`, `^II`… for standalone items.

### Chapter content
Scan each chapter in order:

1. **Chapter intro** (prose/verse before the first numbered verse): assign `^N-I`, `^N-II`…
2. **Verses**: extract verse number from `॥V॥` marker if present; otherwise count stanzas from 1.
   Assign `^N-V`.
3. **Chapter colophon** (line(s) after the last verse, before the next `##` heading):
   assign `^N-a`, `^N-b`… in order.

### Book back matter
Lines after the final chapter's last verse/colophon that close the whole text:
assign `^a`, `^b`…

---

## Step 4 — Verse formatting

Each Sanskrit verse stanza:
- Two half-verses (hemistichs) on separate lines.
- Block ID on the last line of the stanza, preceded by a single space.
- One blank line between stanzas.

```
सुगतान् ससुतान् सधर्मकायान् प्रणिपत्यादरतोऽखिलांश्च वन्द्यान्। 
सुगतात्मजसंवरावतारं कथयिष्यामि यथागमं समासात्॥ ^1-1
```

---

## Dos and Don'ts

- **DO** derive verse numbers from `॥N॥` markers; do not renumber based on your own count unless markers are absent. The last segment of a verse ID **must match the actual verse number in the source text** — this is what makes root-text IDs citable. This is different from commentaries, where the last index is our own sequential counter with no source to match.
- **DON'T** use a sequential counter for verse IDs. Root text: last index = source verse number. Commentary: last index = own counter.
- **DO** treat chapter colophon lines as back matter even if they contain verse-like Sanskrit.
- **DO** assign `^I-0` etc. to front matter sections that currently use `^0-0`, `^0-1`…
- **DON'T** assign a block's zone (front matter / verse / colophon) based on its position under a heading alone — read the Sanskrit to confirm its role.
- **DON'T** apply this skill to commentaries or translations — use `format-commentary` instead.
- **DON'T** use more than 3 segments for verse IDs (`^C-S-V` max).
- **DON'T** put block IDs inside headings — only on content lines and heading lines per the table above.
- **DON'T** assign IDs to standalone OCR line-number lines — remove them in Step 0 before parsing.
- **DON'T** assign IDs to transclusion lines (`![[...]]`). These are references to other files and must be left exactly as-is.
- **DO** collapse multiple consecutive blank lines to a single blank before parsing block boundaries.
- **DON'T** use a bare `^C-Vx` for interpolated verses — always write `^C-Vx1` (counter starts at 1, even for a single interpolation).
- **DON'T** determine a block's zone by which `##` heading it sits under — determine it by content. A book colophon (`समाप्त`, `कृति`, `इति`) gets `^a`, `^b`… even if it physically appears inside the last chapter's heading section and no `##` heading separates it.
- **DON'T** write `^a-1` for a standalone book back matter block with no section heading — the format is `^a`, `^b`… (no trailing number). **Exception**: if a `## Heading ^a-0` exists above the block, treat it like front matter and number the content `^a-1`, `^a-2`… (same pattern as `^I-0` → `^I-1`, `^I-2`). Likewise, content under `## Heading ^b-0` gets `^b-1`, `^b-2`, `^b-3`…

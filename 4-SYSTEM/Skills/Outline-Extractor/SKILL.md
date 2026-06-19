---
name: Outline-Extractor
description: Extract the structural outline (ས་བཅད།) from a Tibetan commentary file and build a nested structured .md file with YAML frontmatter, heading-based hierarchy for levels 1–5, and indented bold list items for deeper levels.
---

# Outline-Extractor

This skill turns a raw Tibetan commentary file in `1-SOURCES/Commentaries/` into two outputs: (1) a flat extracted outline file (`ས་བཅད་རྐྱང་པ།`) that lists every structural heading exactly as it appears in the commentary, and (2) a nested structured outline file (`ལྟེ་བའི་དཀར་ཆག།`) that encodes depth visually using Markdown headings (H2–H6) for levels 1–5 and indented bold list items for levels 6 and deeper. Block IDs from the source commentary are preserved on every entry so that cross-file references remain valid.

Both outputs are saved to `3-TRANSFORMATIONS/Adaptations/<commentary-id>-sa-bcad/` and are treated as Adaptations (not source material) — they must never be cited by `2-RAILS/` files directly; cite the `1-SOURCES/` commentary instead.

---

## Inputs

| Input | Description | Expected value |
|---|---|---|
| `commentary-file` | Path to the commentary in `1-SOURCES/Commentaries/` | e.g. `1-SOURCES/Commentaries/bo-མཁན་པོ་ཀུན་དཔལ།.md` |
| `commentary-id` | Short identifier used for the output folder | e.g. `bo-kunpal` |
| `title-bo` | Tibetan title of the work being outlined | e.g. `སྤྱོད་འཇུག་ས་བཅད།` |

If any input is missing, stop and ask before proceeding.

---

## Output

Two files are created or overwritten:

| File | Description |
|---|---|
| `3-TRANSFORMATIONS/Adaptations/<commentary-id>-sa-bcad/bo-<commentary-id> <title-bo> ས་བཅད་རྐྱང་པ།.md` | Flat extracted outline — tab-indented bullet list, block IDs preserved |
| `3-TRANSFORMATIONS/Adaptations/<commentary-id>-sa-bcad/bo-<commentary-id> <title-bo> ལྟེ་བའི་དཀར་ཆག།.md` | Nested structured outline — headings + indented bold list items |

The output folder `3-TRANSFORMATIONS/Adaptations/<commentary-id>-sa-bcad/` is created if it does not exist.

---

## Output file format

### File 1 — Flat extracted outline (`ས་བཅད་རྐྱང་པ།`)

```markdown
- # <title-bo>

- <Level-1 heading text> ^TOC-1

	- <Level-2 heading text> ^TOC-1-1

		- <Level-3 heading text> ^TOC-1-1-1

			- <Level-4 heading text> ^TOC-1-1-1-1

			    - <Level-5 heading text> ^TOC-1-1-1-1-1

			        - <Level-6 heading text> ^TOC-1-1-1-1-1-1
```

Rules for the flat file:
- Each entry is a Markdown list item `- ` preceded by tab characters to indicate depth.
- One tab = one level of depth. Level-1 entries have zero tabs; level-2 entries have one tab; etc.
- Every entry ends with its block ID `^TOC-N[-N…]` where the segments after `TOC-` correspond exactly to the entry's position in the hierarchy.
- No blank lines between siblings at the same level; one blank line between a parent and its first child.
- The title line is `- # <title-bo>` with no block ID.

### File 2 — Nested structured outline (`ལྟེ་བའི་དཀར་ཆག།`)

```markdown
---
title: <commentary-id> <title-bo> ལྟེ་བའི་དཀར་ཆག
commentary: 1-SOURCES/Commentaries/<commentary-file-basename>
derived_from: 3-TRANSFORMATIONS/Adaptations/<commentary-id>-sa-bcad/bo-<commentary-id> <title-bo> ས་བཅད་རྐྱང་པ།.md
file_type: adaptation
lang_tag: bo
status: draft
---

# <title-bo>

## <Level-1 text> ^TOC-N

### <Level-2 text> ^TOC-N-N

#### <Level-3 text> ^TOC-N-N-N

##### <Level-4 text> ^TOC-N-N-N-N

###### <Level-5 text> ^TOC-N-N-N-N-N

- **<Level-6 text>** ^TOC-N-N-N-N-N-N
  - **<Level-7 text>** ^TOC-N-N-N-N-N-N-N
    - **<Level-8 text>** ^TOC-N-N-N-N-N-N-N-N
```

Depth-to-format mapping:

| Depth (segments after TOC-) | Format |
|---|---|
| 1 | `## ` |
| 2 | `### ` |
| 3 | `#### ` |
| 4 | `##### ` |
| 5 | `###### ` |
| 6 | `- **` |
| 7 | `  - **` (2-space indent per additional level) |
| 8+ | `    - **…**` (2 additional spaces per level beyond 7) |

Always include the block ID at the end of each line.

Add a `---` horizontal rule between the top-level sections (between `## 1.` and `## 2.` groups) for readability.

---

## Rules

1. **Read-only source.** Never modify anything in `1-SOURCES/`. Extract only; do not correct or interpret the commentary text.
2. **Extract structural headings only.** The structural outline consists of the lines in the commentary that function as section-level announcements (ས་བཅད། markers), not ordinary prose. Identify them by: (a) explicit section-number announcements (`དང་པོ་`, `གཉིས་པ་`, `གསུམ་པ་`, etc.), (b) list-structure phrases (`ལ་གསུམ་སྟེ།`, `ལ་གཉིས།`, etc.), (c) inline TOC phrasing that names subsections before elaborating them.
3. **Preserve original Tibetan text exactly.** Do not translate, paraphrase, or correct orthography. Copy text verbatim from the source.
4. **Block IDs are hierarchical.** `^TOC-N` for level-1 entries, `^TOC-N-N` for level-2, etc. Numbering is sequential within each parent: the first child of `^TOC-1` is `^TOC-1-1`, the second is `^TOC-1-2`, and so on. Never skip or reuse numbers.
5. **Two outputs are always produced.** Do not produce one without the other.
6. **Output folder must exist.** Create `3-TRANSFORMATIONS/Adaptations/<commentary-id>-sa-bcad/` before writing if it does not exist.
7. **No citation chain violation.** These files are Adaptations. They may not be transcluded into `2-RAILS/` files. Any rail file that needs this structural information must cite the original `1-SOURCES/` commentary block IDs.
8. **Status is always `draft`.** Only a human domain specialist may change `status` to `complete`.

---

## Procedure

### Step 1 — Confirm inputs

1. Verify `commentary-file` exists in `1-SOURCES/Commentaries/`. If not, stop and report.
2. Confirm `commentary-id` is provided. If not, derive it from the commentary filename (strip the `bo-` prefix and any trailing punctuation), then confirm with the user before proceeding.
3. Confirm `title-bo` is provided. If not, read the commentary's frontmatter `title:` field and use that, then confirm.
4. Check whether `3-TRANSFORMATIONS/Adaptations/<commentary-id>-sa-bcad/` already contains output files. If yes, warn the user that they will be overwritten and ask to confirm.

### Step 2 — Pre-process: split section markers onto new lines

Before scanning for structure, normalise the source text so that every known section marker begins on its own line. This step is purely mechanical — it does not depend on Markdown markup, bold, numbering, or any other formatting convention.

Run a Python script (write it to `0-INBOX/temp/split-<commentary-id>.py` and execute it with `bash`) that:

1. Reads the source file with `encoding='utf-8', errors='replace'`.
2. Joins all lines into a single string (so the input line count does not matter).
3. For every pattern in the list below, inserts a `\n` immediately **before** the first character of the pattern wherever it appears mid-string (i.e. not already at the start of a line):
   - Tibetan chapter-index markers: `ཀ༡`, `ཀ༢`, `ཀ༣`, `ཀ༤`, `ཀ༥`, `ཀ༦`, `ཀ༧`, `ཀ༨`, `ཀ༩`, `ཀ༡༠`, `ཀ༡༡`, `ཀ༡༢` (extend the list if the text has more chapters)
   - Ordinal section announcements: `དང་པོ།`, `གཉིས་པ།`, `གསུམ་པ།`, `བཞི་པ།`, `ལྔ་པ།`, `དྲུག་པ།`, `བདུན་པ།`, `བརྒྱད་པ།`, `དགུ་པ།`, `བཅུ་པ།`
   - Ordinal connectors used mid-sentence: `དང་པོ་ནི།`, `གཉིས་པ་ནི།`, `གསུམ་པ་ནི།`
   - The auspicious marker `༈` when it occurs mid-line
   - Arabic/Indic numbered-entry patterns: a digit or digits immediately followed by `. ` (e.g. `1. `, `2. `, `10. `)
4. Collapses any run of three or more consecutive blank lines down to two.
5. Writes the result to `0-INBOX/temp/<commentary-id>-split.md` (never to `1-SOURCES/`).
6. Prints the original line count and the new line count so you can confirm the split increased the line count.

Use the split file (`0-INBOX/temp/<commentary-id>-split.md`) as the working text for all subsequent steps. The original `1-SOURCES/` file is never modified.

### Step 3 — Read the split text

Read `0-INBOX/temp/<commentary-id>-split.md`. Scan for structural outline passages using the markers in Rule 2. Tibetan commentaries typically open with a top-level structural announcement enumerating the major sections, then repeat that announcement locally before each section begins. Because Step 2 has already placed each marker at the start of its own line, pattern-matching is now line-by-line rather than requiring regex look-behind across long prose runs.

### Step 4 — Build the internal outline tree

As you read, maintain a running tree of outline entries. Each entry has:
- `text`: the Tibetan structural phrase (verbatim)
- `depth`: integer ≥ 1 (derived from nesting position)
- `id`: the `^TOC-…` block ID (assign sequentially)

When a section announcement names N sub-items, those sub-items become children of the current node at depth+1.

### Step 4 — Write File 1 (flat extracted outline)

Create `3-TRANSFORMATIONS/Adaptations/<commentary-id>-sa-bcad/bo-<commentary-id> <title-bo> ས་བཅད་རྐྱང་པ།.md`.

Write the title line first: `- # <title-bo>`

For each entry in depth-first order:
- Write `<(depth-1) tabs>- <text> ^TOC-<id-segments>`
- Insert one blank line before the first child of any parent.

### Step 5 — Write File 2 (nested structured outline)

Create `3-TRANSFORMATIONS/Adaptations/<commentary-id>-sa-bcad/bo-<commentary-id> <title-bo> ལྟེ་བའི་དཀར་ཆག།.md`.

Write the YAML frontmatter block first (see Output file format above).

Then write `# <title-bo>` followed by a blank line.

For each entry in depth-first order, apply the depth-to-format mapping from the Output file format section:
- Depths 1–5: use the appropriate heading level.
- Depth 6+: use indented bold list items with 2 spaces of indentation per level beyond 5.
- Always append the block ID at the end of the line.
- Insert a `---` horizontal rule between top-level (depth-1) sections.

### Step 6 — Verify

Re-read both output files and confirm:
a. Every block ID in File 1 is present in File 2.
b. The numbering in File 2 numeric prefixes matches the block ID segments exactly.
c. No entry from the source commentary outline has been omitted.
d. No source text has been altered.

---

## Completion check

- [ ] `commentary-file` confirmed to exist in `1-SOURCES/Commentaries/`
- [ ] Output folder `3-TRANSFORMATIONS/Adaptations/<commentary-id>-sa-bcad/` exists
- [ ] File 1 (`ས་བཅད་རྐྱང་པ།`) written with correct tab-indented list format and sequential block IDs
- [ ] File 2 (`ལྟེ་བའི་དཀར་ཆག།`) written with YAML frontmatter, heading hierarchy for depths 1–5, and bold indented list items for depth 6+
- [ ] Every block ID from File 1 appears in File 2
- [ ] No source text in `1-SOURCES/` modified
- [ ] Both output files have `status: draft` in frontmatter

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

## Annotated example — number-declaration pattern

**Source text (abbreviated):**
```
གཉིས་པ་ལ་བཞི། བྱང་ཆུབ་ཀྱི་སེམས་ཀྱི་ཕན་ཡོན་བཤད་པ་དང༌། བྱང་ཆུབ་ཀྱི་སེམས་ངོས་བཟུང་བ་དང༌།
དེ་ལ་ཕན་ཡོན་དེ་དག་འབྱུང་བའི་རྒྱུ་མཚན་དང༌། བྱང་ཆུབ་ཀྱི་སེམས་སྒོམ་པའི་གང་ཟག་ལ་བསྟོད་པའོ།།
དང་པོ་ལ་གསུམ། སྡིག་པ་མཐའ་དག་འཇོམས་ཤིང་དགེ་བ་མཐའ་དག་སྒྲུབ་ནུས་པ་དང༌། མིང་དང་དོན་ཁྱད་པར་ཅན་ཐོབ་པ་དང༌། ཕན་ཡོན་དཔེས་བཤད་པའོ།།
དང་པོ་ལ་གསུམ། སྡིག་པ་ཆེན་པོ་འཇོམས་པ་དང༌། བདེ་མཆོག་སྒྲུབ་ནུས་པ་དང༌། ཇི་ལྟར་འདོད་པའི་དོན་སྒྲུབ་ནུས་པའོ།།
དང་པོ་ནི། [prose for child 1] གཉིས་པ་ནི། [prose for child 2] གསུམ་པ་ནི། [prose for child 3]
```

**What to extract:**

The phrase `གཉིས་པ་ལ་བཞི།` declares 4 children. The four names that follow it become child outline entries. `དང་པོ་ལ་གསུམ།` then declares 3 grandchildren of the first child; `དང་པོ་ལ་གསུམ།` (repeated) declares 3 great-grandchildren of that node. The phrases `དང་པོ་ནི།`, `གཉིས་པ་ནི།`, `གསུམ་པ་ནི།` are body-openers, not outline entries — ignore them as structural nodes.

**Resulting outline:**
```
|-བྱང་ཆུབ་ཀྱི་སེམས་ཀྱི་ཕན་ཡོན་རྒྱས་པར་བསམ་པ།  ← parent (གཉིས་པ་ = this node)
| |-བྱང་ཆུབ་ཀྱི་སེམས་ཀྱི་ཕན་ཡོན་བཤད་པ་དང༌།  ← child 1 (དང་པོ་ལ་གསུམ། → 3 grandchildren)
| |  |-སྡིག་པ་མཐའ་དག་འཇོམས་ཤིང་དགེ་བ་མཐའ་དག་སྒྲུབ་ནུས་པ་དང༌།  ← grandchild 1 (དང་པོ་ལ་གསུམ། → 3 great-grandchildren)
| |  |  |-སྡིག་པ་ཆེན་པོ་འཇོམས་པ་དང༌།
| |  |  |-བདེ་མཆོག་སྒྲུབ་ནུས་པ་དང༌།
| |  |  |-ཇི་ལྟར་འདོད་པའི་དོན་སྒྲུབ་ནུས་པ།
| |  |-མིང་དང་དོན་ཁྱད་པར་ཅན་ཐོབ་པ་དང༌།
| |  |-ཕན་ཡོན་དཔེས་བཤད་པ།
| |-བྱང་ཆུབ་ཀྱི་སེམས་ངོས་བཟུང་བ་དང༌།
| |-དེ་ལ་ཕན་ཡོན་དེ་དག་འབྱུང་བའི་རྒྱུ་མཚན་དང༌།
| |-བྱང་ཆུབ་ཀྱི་སེམས་སྒོམ་པའི་གང་ཟག་ལ་བསྟོད་པ།
```

---

## Rules

1. **Read-only source.** Never modify anything in `1-SOURCES/`. Extract only; do not correct or interpret the commentary text.
2. **Extract structural headings only.** The structural outline consists of the lines in the commentary that function as section-level announcements (ས་བཅད། markers), not ordinary prose. Identify them by:

   (a) **Number-declaration phrases** — the primary signal for a new outline node. These take the form `་ལ་<number>།` or `་ལ་ཡང་<number>།` embedded in a phrase, where `<number>` is a Tibetan cardinal number word. Examples: `་བཤད་པ་ལ་གཉིས།` ("this is divided into two"), `་བཤད་པ་ལ་ཡང་གཉིས།`. The cardinal numbers are: གཅིག །གཉིས། གསུམ། བཞི། ལྔ། དྲུག། བདུན། བརྒྱད། དགུ། བཅུ།

   (b) **Sub-item address phrases** — after a number-declaration, each announced sub-item is introduced in one of three forms:
   - Number only with ནི།: `གཉིས་པ་ནི།` or `་གཉིས་པ་ནི།` etc.
   - Name only with ནི།: `དོན་གནས་འཕོ་བའི་ཕན་ཡོན་ནི།`
   - Number + name with ནི།: `གཉིས་པ་དོན་གནས་འཕོ་བའི་ཕན་ཡོན་ནི།`

   (c) **Explicit section-number announcements** — ordinal forms `དང་པོ་`, `གཉིས་པ་`, `གསུམ་པ་`, etc. used as standalone section headers.

   (d) **List-structure phrases** — `ལ་གསུམ་སྟེ།`, `ལ་གཉིས།`, `ལ་བཞི།` etc.

   (e) **Inline TOC phrasing** — sentences that name subsections before elaborating them.

   **Parsing logic for number-declaration blocks:** when a phrase containing `་ལ་<N>།` or `་ལ་ཡང་<N>།` is found, read forward to collect exactly N named items — these names appear in the same sentence as a semicolon-delimited or shad-delimited list and become the child outline entries of that node. The subsequent sub-item address phrases (form b above) confirm the match and mark where each child's body begins; they are not themselves separate outline entries — they are the body openers for the entries already named.
3. **Preserve original Tibetan text exactly.** Do not translate, paraphrase, or correct orthography. Copy text verbatim from the source.
4. **Block IDs are hierarchical.** `^TOC-N` for level-1 entries, `^TOC-N-N` for level-2, etc. Numbering is sequential within each parent: the first child of `^TOC-1` is `^TOC-1-1`, the second is `^TOC-1-2`, and so on. Never skip or reuse numbers.
5. **Complete all siblings before advancing.** When a number-declaration establishes N siblings, do not advance past that sibling group until all N entries — and all their own descendant sub-outlines recursively — have been fully extracted. Concretely: finish sibling 1 (including every sub-declaration it contains, at any depth) before extracting sibling 2; finish sibling 2 completely before extracting sibling 3; and so on. Only after the last sibling and all its descendants are extracted is the current sibling group considered closed. This applies at every level of nesting: a sub-declaration inside sibling 2 must itself be fully resolved before sibling 3 is touched.
6. **Two outputs are always produced.** Do not produce one without the other.
7. **Output folder must exist.** Create `3-TRANSFORMATIONS/Adaptations/<commentary-id>-sa-bcad/` before writing if it does not exist.
8. **No citation chain violation.** These files are Adaptations. They may not be transcluded into `2-RAILS/` files. Any rail file that needs this structural information must cite the original `1-SOURCES/` commentary block IDs.
9. **Status is always `draft`.** Only a human domain specialist may change `status` to `complete`.

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
   - Ordinal connectors used mid-sentence: `དང་པོ་ནི།`, `གཉིས་པ་ནི།`, `གསུམ་པ་ནི།`, `བཞི་པ་ནི།`, `ལྔ་པ་ནི།`, `དྲུག་པ་ནི།`, `བདུན་པ་ནི།`, `བརྒྱད་པ་ནི།`, `དགུ་པ་ནི།`, `བཅུ་པ་ནི།`
   - Number-declaration phrases (primary outline signal): any sequence ending `་ལ་གཅིག`, `་ལ་གཉིས`, `་ལ་གསུམ`, `་ལ་བཞི`, `་ལ་ལྔ`, `་ལ་དྲུག`, `་ལ་བདུན`, `་ལ་བརྒྱད`, `་ལ་དགུ`, `་ལ་བཅུ` followed by `།` — and the ཡང་ variants: `་ལ་ཡང་གཅིག`, `་ལ་ཡང་གཉིས`, etc. Insert the newline before the nearest preceding tsek-syllable boundary (i.e. before the syllable that begins the phrase, not mid-syllable).
   - The auspicious marker `༈` when it occurs mid-line
   - Arabic/Indic numbered-entry patterns: a digit or digits immediately followed by `. ` (e.g. `1. `, `2. `, `10. `)
4. Collapses any run of three or more consecutive blank lines down to two.
5. Writes the result to `0-INBOX/temp/<commentary-id>-split.md` (never to `1-SOURCES/`).
6. Prints the original line count and the new line count so you can confirm the split increased the line count.

Use the split file (`0-INBOX/temp/<commentary-id>-split.md`) as the working text for all subsequent steps. The original `1-SOURCES/` file is never modified.

### Step 3 — Read the split text

Read `0-INBOX/temp/<commentary-id>-split.md`. Scan for structural outline passages using the markers in Rule 2. Tibetan commentaries typically open with a top-level structural announcement enumerating the major sections, then repeat that announcement locally before each section begins. Because Step 2 has already placed each marker at the start of its own line, pattern-matching is now line-by-line rather than requiring regex look-behind across long prose runs.

**Processing number-declaration lines:** when a line contains `་ལ་<N>།` or `་ལ་ཡང་<N>།`, treat the whole phrase up to and including `།` as the parent outline entry. Then collect the N child names that follow in the same sentence (typically separated by `་དང་` or `།` within the same line). These N names become child entries at depth+1. Do **not** create a separate outline entry for the sub-item address phrases (`གཉིས་པ་ནི།`, `གཉིས་པ་<name>་ནི།`, `<name>་ནི།`) that appear later — they are prose markers confirming which child is being elaborated, not new outline nodes. Cross-check that the count of named children matches N; if it does not match, flag the discrepancy in a comment and proceed with what was found.

### Step 4 — Build the internal outline tree

As you read, maintain a running tree of outline entries. Each entry has:
- `text`: the Tibetan structural phrase (verbatim)
- `depth`: integer ≥ 1 (derived from nesting position)
- `id`: the `^TOC-…` block ID (assign sequentially)

When a section announcement names N sub-items, those sub-items become children of the current node at depth+1.

**Traversal order and completeness (Rule 5).** Process the tree strictly depth-first, left-to-right:

1. When sibling group S of N entries is opened, set a counter: *remaining = N*.
2. Enter sibling 1. Before decrementing *remaining*, fully resolve sibling 1: if it contains a sub-declaration for M grandchildren, open a new sibling group and repeat this process recursively until every descendant at every depth is extracted.
3. Only after sibling 1 (and all its descendants) is complete, decrement *remaining* and move to sibling 2. Repeat.
4. When *remaining* reaches 0, the sibling group is closed. Return to the parent level and continue from there.

If you reach the end of the text with *remaining > 0* for any open sibling group, flag each missing sibling explicitly with `[MISSING — not found in source]` at the correct position in the tree, and note the discrepancy. Do not silently skip or collapse missing siblings.

### Step 5 — Write File 1 (flat extracted outline)

Create `3-TRANSFORMATIONS/Adaptations/<commentary-id>-sa-bcad/bo-<commentary-id> <title-bo> ས་བཅད་རྐྱང་པ།.md`.

Write the title line first: `- # <title-bo>`

For each entry in depth-first order:
- Write `<(depth-1) tabs>- <text> ^TOC-<id-segments>`
- Insert one blank line before the first child of any parent.

### Step 6 — Write File 2 (nested structured outline)

Create `3-TRANSFORMATIONS/Adaptations/<commentary-id>-sa-bcad/bo-<commentary-id> <title-bo> ལྟེ་བའི་དཀར་ཆག།.md`.

Write the YAML frontmatter block first (see Output file format above).

Then write `# <title-bo>` followed by a blank line.

For each entry in depth-first order, apply the depth-to-format mapping from the Output file format section:
- Depths 1–5: use the appropriate heading level.
- Depth 6+: use indented bold list items with 2 spaces of indentation per level beyond 5.
- Always append the block ID at the end of the line.
- Insert a `---` horizontal rule between top-level (depth-1) sections.

### Step 7 — Verify

Re-read both output files and confirm:
a. Every block ID in File 1 is present in File 2.
b. The numbering in File 2 numeric prefixes matches the block ID segments exactly.
c. No entry from the source commentary outline has been omitted.
d. No source text has been altered.

---

## Completion check

- [ ] `commentary-file` confirmed to exist in `1-SOURCES/Commentaries/`
- [ ] Split script written, executed, and `0-INBOX/temp/<commentary-id>-split.md` created with higher line count than source
- [ ] Output folder `3-TRANSFORMATIONS/Adaptations/<commentary-id>-sa-bcad/` exists
- [ ] File 1 (`ས་བཅད་རྐྱང་པ།`) written with correct tab-indented list format and sequential block IDs
- [ ] File 2 (`ལྟེ་བའི་དཀར་ཆག།`) written with YAML frontmatter, heading hierarchy for depths 1–5, and bold indented list items for depth 6+
- [ ] Every block ID from File 1 appears in File 2
- [ ] No source text in `1-SOURCES/` modified
- [ ] Both output files have `status: draft` in frontmatter

---
name: add-toc
description: >
  Generate and prepend a detailed nested Table of Contents (TOC / དཀར་ཆག) to a
  Tibetan commentary, structural-outline (sa-bcad), or formatted markdown
  document. The TOC is formatted as a nested `*` list with 3-space indentation
  per level, and each entry is tagged with a `^toc-X-Y-Z` Obsidian block ID
  that reflects its position in the hierarchy. The output file is saved to
  `0-INBOX/temp/` with the prefix `toc-` added to the original filename.

  Trigger this skill whenever the user says things like:
  "add a TOC", "generate a table of contents", "create a dkar chag",
  "prepend a TOC to this file", "add block-ID toc entries", or any request
  to produce a nested outline at the top of a document.
---

# Add-TOC Skill

This skill reads a Tibetan markdown document and produces a clean nested Table
of Contents -- a `*`-list where each item is tagged with a hierarchical
`^toc-X-Y-Z` Obsidian block ID -- then saves a new copy to `0-INBOX/temp/`
with the filename prefixed `toc-`.

---

## Step 1 -- Identify the input file

The user will provide a file path, a filename, or a description of the
document. Resolve it to an absolute path before proceeding.

Common locations:
- `1-SOURCES/Commentaries/` -- formatted Tibetan commentaries
- `3-TRANSFORMATIONS/` -- sa-bcad structural outlines
- `0-INBOX/temp/` -- working copies

---

## Step 2 -- Run the script

Run `scripts/add_toc.py` relative to this skill directory. Locate the skill
directory within the workspace folder (always at `4-SYSTEM/Skills/add-toc/`)
and build the path from the workspace root:

```bash
python "<workspace_root>/4-SYSTEM/Skills/add-toc/scripts/add_toc.py" \
  "<absolute/path/to/input.md>"
```

Replace `<workspace_root>` with the actual vault/workspace root path on the
current machine (e.g. the folder containing `0-INBOX`, `1-SOURCES`, etc.).

The script auto-detects the document format and writes the output to
`0-INBOX/temp/toc-<filename>.md` inside the vault.

---

## Step 3 -- Verify and present

After the script succeeds:

1. Read the first 60 lines of the output file to confirm the TOC looks correct.
2. If the hierarchy is clearly wrong (e.g., all items at depth 1, or items
   in the wrong order), see **Manual correction** below.
3. Present the output file path to the user using a `computer://` link.

---

## TOC format reference

The target format for each TOC line is:

```
* 1. SECTION TITLE ^toc-1
   * 1.1 SUBSECTION TITLE ^toc-1-1
      * 1.1.1 SUB-SUBSECTION TITLE ^toc-1-1-1
      * ... ^toc-1-1-2
   * 1.2 SECOND SUBSECTION ^toc-1-2
* 2. SECOND SECTION ^toc-2
```

Rules:
- Bullet character: `*` (not `-`)
- Indentation: exactly **3 spaces** per depth level (depth 1 = no indent)
- Decimal prefix: `1.` for top-level, `1.1` for sub-level, `1.1.1` for sub-sub, etc.
- Block ID: `^toc-` followed by dash-separated integers reflecting position
  in the hierarchy, e.g. `^toc-2-3-1` means section 2, subsection 3, item 1
- Text: clean title -- no Tibetan numbering prefixes, no list markers,
  no Obsidian wiki-link syntax
- No blank lines between TOC entries
- The TOC block is preceded by a `## dkar-chag / Table of Contents` heading
  and followed by a horizontal rule `---`

---

## Document formats the script handles

### Format A -- Existing Obsidian-style TOC

Files that already contain a `## dkar-chag` section with `^toc-*` block IDs
and Obsidian wiki links `[[#^id|text]]`. The script strips the wiki links
and reformats with 3-space indentation and decimal numbering.

### Format B -- Sa-bcad structural outline

Files like `3-TRANSFORMATIONS/*.md` that have hierarchical list items
with `^X-Y-Z` block IDs. The script uses indentation depth and the number
of ID segments to determine the TOC hierarchy.

### Format C -- Commentary body blocks

Formatted commentaries where section-opening paragraphs have block IDs
ending in `-0` (e.g. `^1-0`, `^1-1-0`, `^2-3-0`). The script picks up
these "section header" blocks, strips the trailing `-0` to derive depth
(1 segment -> depth 1, 2 segments -> depth 2, etc.), and builds the TOC
from the first sentence or clause of each block.

---

## Manual correction

If the auto-generated TOC has structural errors, correct them by editing
the output file directly:

- Adjust indentation (add/remove sets of 3 spaces)
- Re-number `^toc-*` IDs to match the correct hierarchy
- Clean up any residual Tibetan prefix text that the script missed

Tibetan numbering prefixes to watch for:
- Ordinals: dang-po, gnyis-pa, gsum-pa, bzhi-pa, lnga-pa, ...
- Bracket numbers: 1), 2), 3), ... (Tibetan numerals with closing bracket)
- Bracket letters: ka), kha), ga), ... (Tibetan consonants with bracket)
- Decimal labels: 1.1, 1.2, 2.1, ... (Tibetan numerals)
- Section closers: trailing lo//, la/, //

---

## Output location

Always `0-INBOX/temp/toc-{original-filename}` within the vault root
(the folder containing `0-INBOX`, `1-SOURCES`, `2-RAILS`, etc.).

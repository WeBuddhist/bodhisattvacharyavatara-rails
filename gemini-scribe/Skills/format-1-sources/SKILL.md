---
name: format-1-sources
description: Format and normalise source files in the 1-SOURCES/ folder of the bodhisattvacharyavatara-rails repo. Use this skill whenever the user wants to add block IDs, add frontmatter, clean stray line numbers, or fix verse line breaks in any file under 1-SOURCES/ — including root text, translations, and commentaries. Trigger on phrases like "format 1-SOURCES", "add block IDs", "clean up the sources", "add frontmatter to sources", "fix verse formatting", or any request involving normalising files in Text/, Translations/, or Commentaries/.
---

# Format 1-SOURCES

This skill normalises raw ingested files in `1-SOURCES/` to meet the conventions in `4-SYSTEM/CLAUDE.md`. It covers four operations:

1. **Add frontmatter** — insert the required YAML block at the top of files that are missing it
2. **Add block IDs** — append `^chapter-verse` anchors to verses that lack them
3. **Clean stray line numbers** — remove spurious numeric prefixes (`7.`, `42.`) or bare separator numbers left over from PDF extraction
4. **Fix verse line breaks** — restore two-line formatting to Sanskrit verses whose hemistichs were run together with a hyphenated break

Work through one file at a time. For each file, run the helper script to handle the mechanical parts, then apply judgment for frontmatter and anything the script flags as ambiguous.

---

## Step 0 — Read the repo conventions

Before touching any file, read `4-SYSTEM/CLAUDE.md` in full. Pay particular attention to:
- Section 4: Block ID format (`^chapter-verse`, no zero-padding, `## 0. Introduction` for pre-chapter content)
- Section 5: 1-SOURCES rules and minimum frontmatter fields
- Section 3: File naming and language tag conventions

The block ID is the single most important linking mechanism in the whole repo. Get it right.

---

## Step 1 — Identify which files need work

Run a quick audit of all files under `1-SOURCES/`:

```bash
python scripts/format_source.py --audit /path/to/1-SOURCES/
```

This prints a table showing, for each file: whether frontmatter is present, how many verses have block IDs vs. how many are missing them, and whether stray line numbers were detected.

If the user named a specific file, skip the audit and go straight to Step 2 for that file.

---

## Step 2 — Process each file

For each file that needs work, run:

```bash
python scripts/format_source.py \
  --file /path/to/1-SOURCES/Text/sk-dev-root-text.md \
  --add-block-ids \
  --clean-line-numbers \
  --fix-line-breaks \
  --dry-run
```

The `--dry-run` flag prints what would change without touching the file. Review the diff, then run without `--dry-run` to apply.

The script handles:
- **Sanskrit (Devanagari)** — extracts the verse number from the `॥N॥` closing numeral, derives chapter from the current `## N` heading, and appends `^chapter-verse`. Removes `N.` line-number prefixes. Splits hemistichs at the natural caesura before the second half begins (heuristic: split at the first occurrence of a word-separating space after the midpoint of the line, or before a hyphen-joined break).
- **Tibetan** — removes bare integer separator lines (a line containing only digits and optional whitespace). Adds block IDs by counting verses within each chapter. A verse is a run of lines ending with `། །` (double shad).
- **Chinese** — removes `N.` prefixes. Adds block IDs by counting verses within each chapter.
- **Commentary files** — removes bare integer separators. Does NOT auto-assign verse block IDs (commentary structure is complex; see below).

After running, open the file and scan for `TODO` comments the script left where it was uncertain.

---

## Step 3 — Add frontmatter

The script does not write frontmatter — that requires your judgment about the file's identity. For each file missing frontmatter, insert this block at the very top (before any `#` heading):

```yaml
---
title: 
author: 
language: 
file_type: root-text | commentary | translation | reference
lang_tag: sk | bo | zh | en | pi
source_description: "where this text came from"
---
```

Fill in the fields based on the filename and content:

| Filename pattern | language | lang_tag | file_type |
|---|---|---|---|
| `sk-*` | Sanskrit | sk | root-text |
| `bo-*` | Tibetan | bo | translation or commentary |
| `入菩薩行論*` | Classical Chinese | zh | translation |
| Files with Tibetan commentary prose | Tibetan | bo | commentary |

Add `bdrc_work_id`, `gretil_url`, `dsbc_url` if you can infer them from the filename or content headers. For commentaries and translations also add:
```yaml
root_text: 1-SOURCES/Text/sk-dev-root-text.md
covers_verses: "1-1–10-58"
```

---

## Step 4 — Commentary block IDs (special case)

Commentary files have prose that comments on specific verses. The block ID for a commentary passage should match the root text verse it discusses — e.g., the commentary on verse 1-3 gets `^1-3` appended to the last line of that commentary passage.

To identify which root verse a commentary passage covers, look for:
- Explicit verse quotation at the start of the passage
- A bold outline heading referencing a verse number (e.g., `**༡.༣.༡.༡**`)
- Structural markers like `**འགྲེལ་བ།**` (commentary) following a verse quote

Do not guess. If you cannot cleanly identify the verse a passage covers, leave a `[Ed: block ID uncertain — covers verse X?]` note and move on.

---

## Step 5 — Verify

After processing a file, do a final check:

```bash
python scripts/format_source.py --verify /path/to/file.md
```

This checks:
- Frontmatter is present and has all required fields
- No duplicate block IDs in the file
- No remaining stray line numbers
- Block IDs follow `^chapter-verse` format (no zero-padding)

Fix anything it flags before moving to the next file.

---

## Dos and Don'ts

**Do:**
- Work on one file at a time
- Use `--dry-run` before applying changes
- Leave `[Ed: ...]` notes for ambiguous cases rather than guessing
- Preserve the exact text of the source — only add structure, never reword
- Keep the Chapter `##` heading lines exactly as they are (they may contain the original title text)

**Don't:**
- Add interpretation or explanatory content to 1-SOURCES files (that belongs in 2-RAILS)
- Renumber verses — trust the numeral embedded in the text
- Add block IDs to the chapter heading line itself (only to verse content lines)
- Modify the existing block IDs `^0-1`, `^0-2`, etc. that are already correct

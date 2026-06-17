---
name: clean-commentary-text
description: Inspect a raw Tibetan commentary for mechanical text issues (page markers, running headers/footers, extra spaces, encoding artifacts), generate a targeted Python cleaning script, run it, and save the cleaned draft to 0-INBOX/.
---

# clean-commentary-text

This skill removes the mechanical debris that OCR and PDF-to-text conversion leave behind in Tibetan commentary files: repeated page headers and footers, page-number markers, mid-word spaces inserted by PDF justification engines, and non-breaking tsheg characters that block correct syllable detection. It does **not** restructure headings, add block IDs, or fix broken syllables — those tasks belong to `format-commentary`. Run this skill first, then hand the cleaned draft to `format-commentary`.

The output is a draft in `0-INBOX/` — never written directly into `1-SOURCES/`.

---

## Inputs

| Input | Description | Where to find it |
|---|---|---|
| `source_path` | Full path to the raw commentary file | `1-SOURCES/Commentaries/<filename>.md` |
| `output_name` | Filename for the cleaned draft | e.g. `bo-spyod-jug-srung-grel-clean.md` |

If either input is missing, stop and ask before proceeding.

---

## Output

`0-INBOX/<output_name>`

The output file is a plain Markdown draft containing only the text body — no frontmatter, no block IDs. It is ready for `format-commentary` (which adds heading structure, block IDs, and frontmatter) and subsequently `commentary-frontmatter`.

---

## Output file format

The cleaned file has no special structure at this stage — it is a flat Markdown text body. After cleaning, each logical paragraph should sit on its own line with a blank line before and after it. No YAML frontmatter is added by this skill.

```
<cleaned paragraph 1>

<cleaned paragraph 2>

<cleaned paragraph 3>
```

---

## Rules

1. **Never write to `1-SOURCES/`.** Output goes to `0-INBOX/` only.
2. **Do not interpret text.** Do not fix Tibetan spelling, do not paraphrase, do not add or remove content beyond the mechanical issues listed in the Procedure.
3. **Preserve all verse lines.** Tibetan verse stanzas must not be collapsed into prose.
4. **Report the profile before running any script.** Emit the profile JSON to the conversation so the human can verify what will be changed.
5. **Do not mark the output `status: complete`.** Only a human contributor may promote a cleaned draft into `1-SOURCES/`.
6. **If a repeated line is ambiguous** (appears many times but may be substantive), flag it in the profile and ask before removing it.
7. **Non-breaking tshegs (U+0F0C ༌) are always replaced** with the standard inter-syllable tsheg (U+0F0B ་). This is never ambiguous.
8. **Extra mid-word spaces** (a space between two Tibetan Unicode characters where no sentence boundary exists) are removed — the space is deleted, not replaced.

---

## Procedure

### Step 1 — Inspect: profile the source file

Read the source file in chunks (the file may exceed the 256KB single-read limit — use `offset` and `limit`). Build a **profile JSON** containing:

```json
{
  "source_path": "<path>",
  "total_lines": <N>,
  "issues": {
    "page_markers": {
      "pattern": "^\\s*-\\d+-\\s*$",
      "count": <N>,
      "examples": ["line 18: '-1-'", "line 41: '-2-'"]
    },
    "running_headers": {
      "description": "Lines that repeat verbatim more than 5 times",
      "count": <N>,
      "items": [["<line text>", <occurrence_count>]]
    },
    "mid_word_spaces": {
      "description": "Space between two Tibetan Unicode code points",
      "count": <N>,
      "examples": ["line 6: 'སངས་རྒྱས་ དང་ བྱང་ཆུབ་'"]
    },
    "non_breaking_tshegs": {
      "char": "U+0F0C ༌",
      "count": <N>,
      "examples": ["line 22: '...ལོན༌པ༌མཛེས༌སྡུག...'"]
    },
    "orphaned_line_fragments": {
      "description": "Lines ≤15 Tibetan chars that appear mid-paragraph",
      "count": <N>,
      "examples": ["line 95: 'རེ།'"]
    }
  }
}
```

Print the profile to the conversation. If the running_headers list contains any line that looks like substantive text (rather than a clear header or footer), flag it and ask the human before proceeding.

### Step 2 — Check for an existing cleaner script

Look in `4-SYSTEM/Skills/clean-commentary-text/` for a file matching `clean-<commentary-id>.py` (where `commentary-id` is derived from the source filename, e.g. `bo-spyod-jug-srung-grel`).

- **Found →** skip to Step 4 (run the existing script directly).
- **Not found →** proceed to Step 3.

### Step 3 — Generate the cleaning script

Write a Python script to `4-SYSTEM/Skills/clean-commentary-text/clean-<commentary-id>.py`. The script must:

1. **Remove page markers** — delete every line matching `^\s*-\d+-\s*$` and the surrounding blank lines.
2. **Remove running headers / footers** — delete every line whose stripped content matches any string in the `running_headers` list from the profile.
3. **Replace non-breaking tshegs (U+0F0C ༌)** with standard tshegs (U+0F0B ་) throughout.
4. **Remove mid-word spaces** — in lines that are not verse lines, collapse `([ༀ-࿿]) +([ༀ-࿿])` → `\1\2` (repeat until stable).
5. **Join orphaned line fragments** — if a line ends without a sentence-closing punctuation (། ། or ། །) and the next line is an orphaned fragment, join them with a single space.
6. **Normalise blank lines** — collapse runs of more than one blank line into a single blank line.
7. Write the result to `0-INBOX/<output_name>`.
8. Print a brief summary: lines removed, replacements made, output path.

Use UTF-8 throughout. Do not use any external dependencies beyond the Python standard library.

Script template:

```python
#!/usr/bin/env python3
"""
clean-<commentary-id>.py
Generated by the clean-commentary-text skill.
Removes mechanical OCR/PDF debris from:
  <source_path>
Output:
  <output_path>
"""
import re, sys
from pathlib import Path

SOURCE = Path("<source_path>")
OUTPUT = Path("<output_path>")

# --- Strings to remove (running headers / footers) ---
REMOVE_LINES = {
    # Populate from profile running_headers list
}

PAGE_MARKER = re.compile(r'^\s*-\d+-\s*$')
TIB_RANGE   = re.compile(r'[ༀ-࿿]')
MID_SPACE   = re.compile(r'([ༀ-࿿]) +([ༀ-࿿])')
NBT         = '༌'  # ༌ non-breaking tsheg
STD_TSHEG   = '་'  # ་ standard tsheg

def is_verse_line(line: str) -> bool:
    """Heuristic: verse lines end with །། or ། །"""
    s = line.strip()
    return s.endswith('།།') or s.endswith('། །')

def clean(text: str) -> str:
    lines = text.split('\n')
    out = []
    i = 0
    stats = {'page_markers': 0, 'header_footer_lines': 0,
             'nbt_replacements': 0, 'space_removals': 0}

    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        # 1. Page markers (and adjacent blank lines already handled by normalisation)
        if PAGE_MARKER.match(line):
            stats['page_markers'] += 1
            i += 1
            continue

        # 2. Running headers / footers
        if stripped in REMOVE_LINES:
            stats['header_footer_lines'] += 1
            i += 1
            continue

        # 3. Non-breaking tshegs
        if NBT in line:
            new_line = line.replace(NBT, STD_TSHEG)
            stats['nbt_replacements'] += line.count(NBT)
            line = new_line

        # 4. Mid-word spaces (not on verse lines)
        if not is_verse_line(line):
            prev = None
            while prev != line:
                prev = line
                line, n = MID_SPACE.subn(r'\1\2', line)
                stats['space_removals'] += n

        out.append(line)
        i += 1

    # 5. Normalise blank lines
    result = re.sub(r'\n{3,}', '\n\n', '\n'.join(out))

    print(f"Done — page markers removed: {stats['page_markers']}, "
          f"header/footer lines removed: {stats['header_footer_lines']}, "
          f"NBT replacements: {stats['nbt_replacements']}, "
          f"mid-word spaces removed: {stats['space_removals']}")
    return result

if __name__ == '__main__':
    text = SOURCE.read_text(encoding='utf-8')
    cleaned = clean(text)
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(cleaned, encoding='utf-8')
    print(f"Written to: {OUTPUT}")
```

Fill in `SOURCE`, `OUTPUT`, and `REMOVE_LINES` from the profile before saving.

### Step 4 — Run the script

Execute the script from the vault root:
```
python3 4-SYSTEM/Skills/clean-commentary-text/clean-<commentary-id>.py
```

Capture the printed summary and include it in the conversation output.

### Step 5 — Review the output

Read the first 100 lines of `0-INBOX/<output_name>` and verify:
- No page markers remain.
- No running header / footer lines remain.
- Tibetan syllables flow without mid-word spaces.
- No ༌ characters remain.
- Paragraph breaks are single blank lines.

Report any remaining issues to the human contributor. Do not mark the draft complete.

---

## Completion check

- [ ] Profile JSON produced and printed before any file was changed
- [ ] No writes made to `1-SOURCES/`
- [ ] Cleaning script written to `4-SYSTEM/Skills/clean-commentary-text/clean-<commentary-id>.py`
- [ ] Script run successfully with a printed summary
- [ ] Output file exists at `0-INBOX/<output_name>`
- [ ] First-100-line review completed and findings reported
- [ ] Human contributor notified that the draft is ready for `format-commentary`

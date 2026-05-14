# Tibetan Root Text Formatting Skill

## Purpose

Format Tibetan root-text `.md` files for use in Obsidian. The goal is clean, navigable Tibetan verse with Obsidian block IDs that support internal linking (e.g. `[[file#^1-23]]`), chapter headings with TOC anchors, and one stanza per paragraph with each verse-line on its own line.

Applicable texts: Bodhisattvacharyavatara (BCA), Abhisamayalamkara, Mulamadhyamakakarika, and similar structured Indian/Tibetan Buddhist root texts in `.md` form.

## Core Principles
Before processing any file, review **[[1-Human-Sources-Guideline]]**. The block ID is the single most important linking mechanism in the vault.

---

## Input File Structure

Raw source files typically contain:

| Pattern | Example | Action |
|---|---|---|
| Standalone verse number on its own line | `11` | **Remove** — used only to set block ID |
| Merged stanza (multiple verse-lines on one line) | `...། །...། །...།།` | **Split** at each `། །` separator |
| Already-split stanza (4 lines, one per line) | four lines ending with `། །` | Re-validate block ID |
| Chapter-end colophon appended to last verse | `...མཆི། །བྱང་ཆུབ་སེམས་དཔའི་...ལེའུ་དང་པོའོ།། །།` | Strip colophon, keep verse text |
| Blank lines (single or double) | — | Normalise to exactly one blank between stanzas |
| Markdown headings | `## 1. ལེའུ་...` | Pass through |
| Non-Tibetan prose | translator notes, etc. | Pass through verbatim |

---

## Tibetan Text Conventions

- **Verse-line separator**: `། །` (shad U+0F0D, space, shad). Each verse-line ends with this.
- **Stanza**: typically 4 verse-lines (sometimes 2 or 8). One block ID per stanza.
- **Colophon marker**: `འཇུག་པ་ལས` appears in every chapter-end colophon. The colophon also ends with `།། །།` (double-shad, space, double-shad).
- **Double-shad** `།།` appears **only** in chapter colophons, never in regular verse. Use this to detect colophon lines reliably.

---

## Output Format

### Chapter headings

```
## N. ལེའུ་ORDINAL། CHAPTER_NAME ^TOC-N
```

Examples extracted from BCA colophons:

```
## 1. ལེའུ་དང་པོ། བྱང་ཆུབ་སེམས་ཀྱི་ཕན་ཡོན་བཤད་པ། ^TOC-1
## 2. ལེའུ་གཉིས་པ། སྡིག་པ་བཤགས་པ། ^TOC-2
## 3. ལེའུ་གསུམ་པ། བྱང་ཆུབ་ཀྱི་སེམས་ཡོངས་སུ་བཟུང་བ། ^TOC-3
## 4. ལེའུ་བཞི་པ། བག་ཡོད་བསྟན་པ། ^TOC-4
## 5. ལེའུ་ལྔ་པ། ཤེས་བཞིན་བསྲུང་བར་བྱ་བ། ^TOC-5
## 6. ལེའུ་དྲུག་པ། བཟོད་པ་བསྟན་པ། ^TOC-6
## 7. ལེའུ་བདུན་པ། བརྩོན་འགྲུས་བསྟན་པ། ^TOC-7
## 8. ལེའུ་བརྒྱད་པ། བསམ་གཏན་བསྟན་པ། ^TOC-8
## 9. ལེའུ་དགུ་པ། ཤེས་རབ་ཀྱི་ཕ་རོལ་ཏུ་ཕྱིན་པ། ^TOC-9
## 10. ལེའུ་བཅུ་པ། བསྔོ་བ། ^TOC-10
```

### Block IDs

| Location | Format | Example |
|---|---|---|
| Intro section 0.1 stanzas | `^0-1-N` | `^0-1-1`, `^0-1-2` |
| Intro section 0.2 stanzas | `^0-2-N` | `^0-2-1`, `^0-2-3` |
| Chapter 1 stanzas | `^1-N` | `^1-1`, `^1-39` |
| Chapter 2 stanzas | `^2-N` | `^2-1`, `^2-67` |
| Chapter N stanzas | `^N-N` | `^9-175` |

The number after the hyphen is the **traditional verse number** (chapter-relative). When the source file includes standalone verse numbers, use those. When absent, increment by 1 from the last known verse number.

### Formatted stanza (4-line example)

```
བདེ་གཤེགས་ཆོས་ཀྱི་སྐུ་མངའ་སྲས་བཅས་དང་། །
ཕྱག་འོས་ཀུན་ལའང་གུས་པར་ཕྱག་འཚལ་ཏེ། །
བདེ་གཤེགས་སྲས་ཀྱི་སྡོམ་ལ་འཇུག་པ་ནི། །
ལུང་བཞིན་མདོར་བསྡུས་ནས་ནི་བརྗོད་པར་བྱ། ། ^0-2-1
```

Block ID goes at the **end of the last line**, separated by a single space.

---

## Verse Numbering: BCA Chapter Starts (Absolute)

For the Bodhisattvacharyavatara, the absolute-to-chapter-relative mapping:

| Chapter | Starts at abs. verse | Tibetan ordinal |
|---|---|---|
| 1 | 1 | དང་པོ |
| 2 | 40 | གཉིས་པ |
| 3 | 107 | གསུམ་པ |
| 4 | 142 | བཞི་པ |
| 5 | 192 | ལྔ་པ |
| 6 | 304 | དྲུག་པ |
| 7 | 444 | བདུན་པ |
| 8 | 523 | བརྒྱད་པ |
| 9 | 710 | དགུ་པ |
| 10 | 885 | བཅུ་པ |

Chapter-relative verse = absolute verse − chapter_start + 1.

---

## Automation: Python Script

The formatting script `format_bca.py` lives in the vault root. Run from the vault folder:

```
python format_bca.py
```

**What it does (in order):**

1. Finds the `.md` file in `1-SOURCES/Translations/` automatically.
2. **Pass 1** — scans all lines, extracts chapter names from the 10 colophon lines using regex, builds chapter headings.
3. Keeps lines 1–33 (intro, TOC, title, sections 0.1/0.2, and Chapter 1 heading) **unchanged**.
4. **Pass 2** — state machine processes line 34 onwards:
   - Blank lines → flush stanza buffer, output one blank (suppress doubles)
   - Number-only lines → record verse number, detect chapter transition, insert heading, discard line
   - Colophon lines → strip colophon text, flush last verse, advance chapter counter
   - Tibetan lines → accumulate into stanza buffer
   - Other lines → pass through verbatim
5. On stanza flush: combine buffer lines, clean old block IDs, split on `། །`, append new `^ch-rel` ID to last line.
6. Final pass removes consecutive blank lines.
7. Writes result back to the same file.

### Key regex patterns used

```python
COLOPHON_MARKER  = 'འཇུག་པ་ལས'           # in every colophon
FULL_COLOPHON    = 'བྱང་ཆུབ་སེམས་དཔའི་སྤྱོད་པ་ལ་འཇུག་པ་ལས'  # full opener
SHAD_PAIR        = '། །'                  # verse-line separator
TIBETAN_RANGE    = r'[ༀ-࿿]'              # any Tibetan character
DOUBLE_SHAD      = '།།'                  # colophon-only marker
```

**Ordinal extraction from colophon:**
```python
re.search(r'(ལེའུ་)(?:སྟེ་)?(\S+?)འོ', col_text)
```

**Chapter name extraction:**
```python
re.search(
    r'འཇུག་པ་ལས[་།\s]+([\s\S]+?)(?:་ཞེས་བྱ་བ་སྟེ་|་སྟེ་ལེའུ་|འི་ལེའུ་|་ལེའུ་)',
    col_text
)
```

**Clean old block IDs:**
```python
re.sub(r'\s*\^\S+\s*$', '', line)   # removes ^anything at end
re.sub(r'\s+\d+-\d+\s*$', '', line) # removes bare 1-2 style at end
```

---

## Colophon Stripping

Each chapter's last verse has the colophon appended inline. Strip it by finding the full colophon opener and cutting there:

```python
full_opener = 'བྱང་ཆུབ་སེམས་དཔའི་སྤྱོད་པ་ལ་འཇུག་པ་ལས'
idx = line.find(full_opener)
if idx != -1:
    verse_text = line[:idx].rstrip()
```

Fallback to cutting at `འཇུག་པ་ལས` if the full opener is not found.

---

## Colophon Line Numbers (BCA — for reference)

| Chapter | File line (1-based) | Last verse number |
|---|---|---|
| 1 | 161 | 39 |
| 2 | 429 | 106 |
| 3 | 569 | 141 |
| 4 | 769 | 191 |
| 5 | 1217 | 303 |
| 6 | 1777 | 443 |
| 7 | 2093 | 522 |
| 8 | 2841 | 709 |
| 9 | 3541 | 884 |
| 10 | 3789 | (final) |

---

## Applying to a New Text

When formatting a different Tibetan root text:

1. **Find colophon pattern** — Grep for `འཇུག་པ་ལས` or the text's own chapter-end formula.
2. **Count chapters** — Read colophon lines to find ordinals and chapter names.
3. **Map verse numbers** — Find the first verse number of each chapter to build `CHAPTER_STARTS`.
4. **Adjust `INTRO_END`** — Count how many lines of intro/preamble to preserve unchanged.
5. **Update `format_bca.py`** — Or copy it and adjust the constants at the top.

For texts without embedded verse numbers, set `pending_abs = None` throughout and rely on sequential increment (`last_abs + 1`) for all IDs.

---

## Obsidian Integration

- Block IDs (`^1-23`) allow direct linking: `[[bo-file#^1-23]]`
- Chapter anchors (`^TOC-3`) allow TOC links: `[[bo-file#^TOC-3|Chapter 3]]`
- The intro TOC in the file uses `^toc-0` for the TOC block itself
- Section headings 0.1 and 0.2 use `^TOC-0-1` and `^TOC-0-2`
- Do **not** use spaces in block IDs — Obsidian requires alphanumeric, hyphens, underscores only

---

## Common Pitfalls

| Issue | Cause | Fix |
|---|---|---|
| Block ID missing `^` | Old-style bare `1-2` at line end | `clean_existing_id()` handles this |
| Stanza not split | Lines without `། །` separator | Check source encoding (U+0F0D) |
| Colophon text appearing in output | `strip_colophon` missed it | Use full opener string, not just `འཇུག་པ་ལས` |
| Double blank lines | Two blanks in source with no stanza between | Final `cleaned` pass removes these |
| Wrong chapter at boundary | `CHAPTER_STARTS` off by one | Re-verify by reading first number after each colophon |
| Verse numbers jumping (e.g. 3 → 11) | Source doesn't include all verses | Normal — gaps in IDs reflect the traditional verse count |

# clean-commentary-text — README

Workflow log, issue registry, and solution notes for this skill.

---

## Workflow Overview

```
text
   │
   ▼
Step 1: Inspect ──► profile JSON
   │
   ▼
Step 2: Check issues
   │
   ├─ Found ──► Step 4: Run existing cleaner script
   │
   └─ Not found ──► Step 3: Generate new script ──► Step 4: Run it
                                                           │
                                                           ▼
                                                    Step 5: Review output
```

**Output location:** `0-INBOX/<cleaned-filename>.md`
**Next skill in chain:** `format-commentary` → `commentary-frontmatter`

---

## Run instructions

```bash
# From the vault root
python3 "4-SYSTEM/Skills/clean-commentary-text/clean-bo-spyod-jug-srung-grel.py"
```

Output is written to `0-INBOX/bo-spyod-jug-srung-grel-clean.md`.

---

## Runs log

| Date | Source file | Script | Output | Notes |
|------|-------------|--------|--------|-------|
| 2026-06-17 | `bo-སྤྱོད་འཇུག་སྒྲུང་འགྲེལ།.md` | `clean-bo-spyod-jug-srung-grel.py` | pending — bash workspace unavailable at time of creation | Script written; run manually with `python3` |

---

## Issues found — bo-སྤྱོད་འཇུག་སྒྲུང་འགྲེལ།.md

Inspected 2026-06-17. File size: 698KB. Issues below are ordered by severity.

---

### Issue 1 — Page number markers

**Pattern:** Lines matching `^\s*-\d+-\s*$`  
**Examples:**
```
-1-
-2-
-3-
...
```
**Frequency:** Every ~15 lines throughout the entire file (one per printed page).  
**Cause:** PDF-to-text conversion retained the printed page numbers.  
**Solution:** Delete every matching line. The surrounding blank lines are cleaned up by the blank-line normalisation pass.  
**Status:** ✅ Handled in script (pass 1).

---

### Issue 2 — Running headers (single-line form)

**Pattern:** Verbatim line match  
**Text:**
```
མཁྱེན་བརྩེའི་འོད་སྣང་ལས། སྤྱོད་འཇུག་སྒྲུང་འགྲེལ།
```
**Frequency:** Appears on most odd-numbered pages.  
**Cause:** Running page header from the printed book.  
**Solution:** Remove verbatim.  
**Status:** ✅ Handled in script (pass 2, `REMOVE_LINES` set).

---

### Issue 3 — Running headers (split across two lines)

**Pattern:** Two consecutive verbatim lines  
**Text:**
```
མཁྱེན་བརྩེའི་འོད་སྣང་ལས།
སྤྱོད་འཇུག་སྒྲུང་འགྲེལ།
```
**Example (lines 259–260 of source):**
```
མཁྱེན་བརྩེའི་འོད་སྣང་ལས།
སྤྱོད་འཇུག་སྒྲུང་འགྲེལ།
```
**Frequency:** Occasional variant of the running header (narrower column forcing a line break).  
**Cause:** OCR wrapped the header across two lines.  
**Solution:** Both strings added individually to `REMOVE_LINES`. Each is removed when encountered regardless of context.  
**Caveat:** The string "སྤྱོད་འཇུག་སྒྲུང་འགྲེལ།" *also* appears legitimately in the body text as a title reference. The script removes *only* lines where this string is the entire stripped content — it will not delete the string when it appears mid-sentence. Verify in the Step 5 review.  
**Status:** ✅ Handled in script (pass 2). ⚑ Verify in review.

---

### Issue 4 — Running footers

**Pattern:** Verbatim line match  
**Text:**
```
སྤྱོད་འཇུག་སྒྲུང་འགྲེལ་ལས་འབྲས་གསལ་བའི་མེ་ལོང་ཞེས་བྱ་བ་བཞུགས།
```
**Frequency:** Appears on most even-numbered pages.  
**Cause:** Running page footer from the printed book.  
**Solution:** Remove verbatim.  
**Status:** ✅ Handled in script (pass 2, `REMOVE_LINES` set).

---

### Issue 5 — Non-breaking tshegs (U+0F0C ༌)

**Pattern:** Unicode character U+0F0C (TIBETAN MARK DELIMITER TSHEG BSTAR)  
**Examples:**
```
ལོན༌པ༌མཛེས༌སྡུག༌གཅིག༌ཡོད༌པ༌  (line 22)
གདུངས༌ཏེ༌ཚོང༌པ་འདི༌ལྟ༌བུ༌འདོན༌ནུས་  (line 101)
```
**Frequency:** Hundreds of occurrences throughout the file.  
**Cause:** The PDF encoding used U+0F0C instead of the standard inter-syllable tsheg U+0F0B. This breaks word-boundary detection and search.  
**Solution:** Replace all ༌ (U+0F0C) with ་ (U+0F0B) globally.  
**Status:** ✅ Handled in script (pass 3).

---

### Issue 6 — Extra spaces mid-word (PDF justification artifacts)

**Pattern:** One or more spaces between two characters in the Tibetan Unicode block (U+0F00–U+0FFF).  
**Examples:**
```
སངས་རྒྱས་ དང་ བྱང་ཆུབ་  (line 6)
སེམས་ ཀྱིས། ཉན་ རང་ ལ་  (line 16)
བྱང་ ཆུབ་ མཆོག་ གིས་ སེམས་ གཅིག་ གིས།  (line 80)
```
**Frequency:** Very high — present in several hundred lines.  
**Cause:** The PDF used full-text justification; OCR preserved the spaces between syllables that the typesetter expanded for alignment.  
**Solution:** Collapse `([ༀ-࿿]) +([ༀ-࿿])` → `\1\2` (applied iteratively until stable). Skipped on verse lines ending with ། །  to preserve intentional verse spacing.  
**Status:** ✅ Handled in script (pass 4).

---

### Issue 7 — Orphaned line fragments

**Pattern:** A line of ≤ 20 Tibetan characters that appears in the middle of a paragraph (previous line does not end with sentence-closing punctuation །).  
**Examples:**
```
རེ།                          (line 95-96, fragment of speech)
དང་།                         (mid-sentence wrap)
```
**Frequency:** Dozens of occurrences.  
**Cause:** OCR line boundaries did not align with sentence boundaries. Short text fragments were left as isolated lines.  
**Solution:** Join orphaned short lines (≤ 20 chars) to the end of the preceding non-empty line, separated by a single space, when the preceding line does not end with a sentence boundary.  
**Caution:** The 20-char threshold is conservative. After running, check the Step 5 review for any over-joined lines.  
**Status:** ✅ Handled in script (pass 5).

---

## Known limitations

- The script does not fix **broken Tibetan syllables** (OCR misreads where a vowel sign was separated from its base). That work belongs to `format-commentary`.
- The script does not add **headings, block IDs, or frontmatter**. Run `format-commentary` next.
- The **split header** issue (Issue 3) may occasionally remove the title string when it appears at the top of a section as a running reference. Verify in the Step 5 review.

---

## Adding a new commentary

1. Run Step 1 (profile) on the new file.
2. Populate a new script from the template in `SKILL.md` Step 3, filling in the `REMOVE_LINES` set from the profile.
3. Save the script as `clean-<commentary-id>.py` in this folder.
4. Add a row to the Runs log above.
5. Run and review per Steps 4–5.

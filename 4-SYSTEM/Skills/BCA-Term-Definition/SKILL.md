---
name: BCA-Term-Definition
description: Extract verbatim definitions of key terms from Tibetan commentaries and fill them into the Meaning column of BCA-Term-Localization.md, formatted in traditional Tibetan quotation style.
---

# BCA-Term-Definition

This skill populates the **Meaning** column of `2-RAILS/Local-Wiki/BCA-Term-Localization.md` by locating definitional passages in `1-SOURCES/Commentaries/` and extracting them verbatim. A definitional passage is one where a commentary explains a term using the formulaic markers `[term]ནི་`, `[term]ཞེས་པ་ནི་`, or `[term]ཅེས་པ་ནི་`. Extracted text is formatted in traditional Tibetan quotation style. The skill never paraphrases, summarises, or writes any explanatory text of its own — all content comes word-for-word from the cited commentary.

---

## Inputs

- **Term or term list** — one or more Tibetan terms from the Bo column of `2-RAILS/Local-Wiki/BCA-Term-Localization.md`. If the user says "all terms" or supplies no specific term, process every row whose Meaning cell is currently empty.
- **Commentary files** — all files under `1-SOURCES/Commentaries/` are eligible sources. The skill searches them all unless the user restricts to a named commentary.
- **BCA-Term-Localization.md** — `2-RAILS/Local-Wiki/BCA-Term-Localization.md` — the table to update.

---

## Output

`2-RAILS/Local-Wiki/BCA-Term-Localization.md` — modified in place. For each processed term, the Meaning cell is filled with one or more quotation entries, one per commentary passage found.

---

## Output cell format

Every definitional hit — whether from one commentary or many — is written into the same Meaning cell using this format:

```
[commentary-short-name]ནས་「[verbatim explanation text]」ཞེས་གསུངས་སོ།།
```

When multiple hits exist (from the same or different commentaries), list each one on its own line inside the cell, one after the other:

```
[commentary-A-short-name]ནས་「[verbatim explanation text A]」ཞེས་གསུངས་སོ།།
[commentary-B-short-name]ནས་「[verbatim explanation text B]」ཞེས་གསུངས་སོ།།
[commentary-C-short-name]ནས་「[verbatim explanation text C]」ཞེས་གསུངས་སོ།།
```

There is no special treatment for single vs. multiple hits — the format is identical; additional entries are simply appended as additional lines.

**`[commentary-short-name]`** is the registered short ID for the commentary as declared in the file's frontmatter (`id:` or `short_id:` field). If no short ID is declared, use the filename stem without the language tag.

**`[verbatim explanation text]`** is the exact text extracted from the commentary, beginning immediately after the definitional marker (`ནི་`, `ཞེས་པ་ནི་`, or `ཅེས་པ་ནི་`) and ending at the first sentence-final punctuation (`།།`, `།`, or the next structural boundary). Do not include the marker itself in the quotation.

---

## Definitional marker patterns

Search for these patterns in commentary files, where `{TERM}` is the exact Tibetan string of the target term:

| Pattern | Example |
|---|---|
| `{TERM}ནི་` | `སེམས་བསྐྱེད་པ་ནི་` |
| `{TERM}་ནི་` | (with tsheg before ནི་) |
| `{TERM}ཞེས་པ་ནི་` | `སེམས་བསྐྱེད་པ་ཞེས་པ་ནི་` |
| `{TERM}ཅེས་པ་ནི་` | `སེམས་བསྐྱེད་པ་ཅེས་པ་ནི་` |

Accept the pattern anywhere in a paragraph — not only at the start of a sentence. A hit is valid only when the term is followed immediately (without intervening words) by one of these markers.

---

## Rules

1. **No original writing.** The Meaning cell contains only verbatim text from the source commentary plus the fixed frame words (`ནས་`, `ཞེས་གསུངས་སོ།།`). If a term has no definitional hit in any commentary, leave the Meaning cell empty and move to the next term. Do not write a placeholder, a note, or a summary.
2. **Verbatim extraction only.** Copy the explanation exactly as it appears in the commentary. Do not correct spelling, normalise orthography, or truncate for length unless a passage runs more than three sentences — in that case, take only the first complete sentence after the marker.
3. **No interpretation.** Do not choose between two passages on the basis of which is "better" or "clearer". Include all valid hits, each as its own quotation line.
4. **Do not touch any cell other than Meaning.** The Bo, En, Zh, Hin, Nep, Rus, Mon columns are not modified by this skill.
5. **Do not overwrite non-empty Meaning cells without explicit instruction.** If a Meaning cell already contains text, skip that row unless the user explicitly asks to overwrite or append.
6. **Cite every quotation to its block ID.** After each Meaning cell entry, append a parenthetical block reference on the same line: `([[1-SOURCES/Commentaries/<filename>.md#^<block-id>]])`. This is required even when the cell is inside a table — use the inline citation form, not a footnote.
7. **Use the commentary short ID, not the full filename.** Check the frontmatter of each commentary file for a registered `id:` or `short_id:` before constructing the quotation frame.
8. **Do not modify `1-SOURCES/` files.** This skill reads commentaries but never writes to them.

---

## Procedure

### Step 1 — Identify terms to process

1. Open `2-RAILS/Local-Wiki/BCA-Term-Localization.md` and read the full table.
2. If the user named specific terms, collect only those rows. If the user said "all" or gave no restriction, collect all rows where the Meaning cell is empty (contains only whitespace).
3. Record each term as a Tibetan string for the search step.

### Step 2 — Load commentary short IDs

1. List all files under `1-SOURCES/Commentaries/`.
2. For each file, read its YAML frontmatter and record the `id:` or `short_id:` field. If neither is present, derive the short name from the filename stem by dropping the language tag suffix (e.g. `khenpo-kunpal-bo` → `khenpo-kunpal`).
3. Build a lookup table: `{filename → short-name}`.

### Step 3 — Search for definitions

For each term in the work list:

1. Search every commentary file for the definitional marker patterns (§ Definitional marker patterns above). Use literal string search — the term must appear verbatim.
2. For each hit, record:
   - The commentary filename
   - The block ID of the containing paragraph (`^block-id` suffix on that paragraph)
   - The verbatim text starting immediately after the marker and ending at the first `།།` or `།` that closes the definitional clause
3. If a commentary file has multiple definitional passages for the same term, record each separately.

### Step 4 — Format quotation entries

For each hit recorded in Step 3:

1. Look up the commentary short name from the table built in Step 2.
2. Construct the quotation entry:
   ```
   [short-name]ནས་「[verbatim text]」ཞེས་གསུངས་སོ།། ([[1-SOURCES/Commentaries/<filename>#^<block-id>]])
   ```
3. If multiple hits exist for the same term, order them by commentary (alphabetical by short name) unless the user specifies an order.

### Step 5 — Write results to BCA-Term-Localization.md

1. Open `2-RAILS/Local-Wiki/BCA-Term-Localization.md`.
2. For each processed term:
   a. Locate the row matching the Bo cell.
   b. Replace the empty Meaning cell content with all formatted quotation entries for that term, each on its own line, in the order found (alphabetical by commentary short name unless the user specifies otherwise).
3. Write the updated file back to disk.
4. Do not reformat, reorder, or change spacing in any other part of the table.

### Step 6 — Report

After processing, report:
- How many terms were processed.
- How many terms received at least one definition.
- How many terms had no definitional hit in any commentary (list the terms).

---

## Completion check

- [ ] Only the Meaning column was modified; all other columns are unchanged
- [ ] Every filled Meaning cell contains only verbatim text from a commentary, framed with `[short-name]ནས་「…」ཞེས་གསུངས་སོ།།`
- [ ] Every quotation entry includes the block-ID citation in parentheses
- [ ] No Meaning cell was overwritten unless the user explicitly authorised it
- [ ] Terms with no definitional hit are left blank (not filled with a note or placeholder)
- [ ] No file in `1-SOURCES/` was modified
- [ ] BCA-Term-Localization.md was saved back to disk with all changes applied

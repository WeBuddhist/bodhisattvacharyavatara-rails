---
name: commentary-verse-id
description: Adds Obsidian-style block IDs (^chapter-n) to segmented Tibetan commentary markdown files, based on the chapter number in the nearest preceding root-text transclusion (![[...#^chapter-verse]]). Segments with no root text transcluded yet (before the first transclusion) are tagged as chapter 0 (^0-1, ^0-2, ...) instead of being left untagged. Use when the user wants to "add verse id", "add block id", or "tag commentary segments with ids" in a *_segmented.md commentary file that transcludes a root text.
---

# commentary-verse-id

This skill tags every segment of a segmented Tibetan commentary file — each root-text quote line and each following commentary paragraph — with a trailing Obsidian block-reference id (` ^{chapter}-{n}`), so every block becomes individually linkable/transcludable. The chapter number comes from the nearest preceding root-text transclusion; the counter within that chapter increments across every segment in reading order and only resets when the transclusion's chapter number changes. Segments that appear before any transclusion has occurred (no root text transcluded yet — e.g. front matter, homage, or introductory commentary) are tagged as chapter `0` (`^0-1`, `^0-2`, ...) rather than being skipped, so every taggable segment in the file always ends up with an id. Correct output preserves every existing line, character, and line ending exactly — it only appends an id to the end of qualifying lines.

---

## Inputs

- `file` — path to a `*_segmented.md` commentary file under `1-SOURCES/Commentaries/Transcluded/` (or similar). It does not need to already contain a transclusion — if it has none at all, every taggable segment is tagged under chapter `0`.

## Output

- The same `file` modified in place (or a caller-specified output path), with a block id appended to the end of every qualifying line. No lines are added or removed; total line count is unchanged.

---

## Output file format

Given input (note: the first two lines appear *before* any transclusion):

```
མཚན་གྱི་དོན།

> རྒྱ་གར་སྐད་དུ། ...

![[bo-བློ་ལྡན་ཤེས་རབ།#^1-1]]
> བདེ་གཤེགས་ཆོས་ཀྱི་སྐུ་མངའ་སྲས་བཅས་དང་། །ཕྱག་འོས་ཀུན་ལའང་གུས་པས་ཕྱག་འཚལ་ཏེ། །

ཞེས་ཏེ་བདེ་གཤེགས་... (commentary paragraph)

གཉིས་པ་(བཤད་པར་དམ་བཅའ་བ་)ནི།
```

Output:

```
མཚན་གྱི་དོན། ^0-1

> རྒྱ་གར་སྐད་དུ། ... ^0-2

![[bo-བློ་ལྡན་ཤེས་རབ།#^1-1]]
> བདེ་གཤེགས་ཆོས་ཀྱི་སྐུ་མངའ་སྲས་བཅས་དང་། །ཕྱག་འོས་ཀུན་ལའང་གུས་པས་ཕྱག་འཚལ་ཏེ། ། ^1-1

ཞེས་ཏེ་བདེ་གཤེགས་... (commentary paragraph) ^1-2

གཉིས་པ་(བཤད་པར་དམ་བཅའ་བ་)ནི། ^1-3
```

Note how the two segments before the first transclusion get `^0-1` and `^0-2` (chapter `0`), and the counter resets to 1 as soon as the real chapter `1` begins at the first transclusion.

---

## Rules

1. Transclusion lines (`![[...]]`) are never modified and never receive an id.
2. The "chapter" number is the integer before the dash in the transclusion's block ref (`#^1-1` → chapter `1`, `#^2-1` → chapter `2`).
3. Before the first transclusion in the file, the chapter is `0` — segments here (front matter, homage, introductory commentary with no root text transcluded yet) are tagged `^0-1`, `^0-2`, ... rather than left untagged.
4. A per-chapter counter starts at 1 the first time that chapter number is seen (including chapter `0` at the very start of the file), and resets to 1 only when a later transclusion's chapter number differs from the current one. It does not reset on every transclusion — multiple transclusions within the same chapter (e.g. `#^1-2`, `#^1-3`) continue the same running counter.
5. Every non-blank, non-transclusion, non-heading line gets ` ^{chapter}-{counter}` appended to its end, from the very first content line of the file onward; the counter increments after each tagged line. This includes root-quote lines (`> ...`) and commentary paragraphs alike — everything in reading order gets the next sequential id within its chapter.
6. YAML frontmatter, blank lines, and markdown headings (`#`, `##`, ...) are left untouched and do not consume a counter value.
7. Idempotent: lines that already end with a block id (matching `\s\^\d+-\d+\s*$`) are skipped, so re-running on an already-tagged file is a no-op.
8. Original line endings (CRLF or LF) and total line count must be preserved — ids are appended to existing lines only, never inserted as new lines.
9. Do not hand-edit ids with the Edit tool for bulk tagging — always use `apply.py` so the counter logic stays consistent across the whole file. Manual edits are only for fixing a specific flagged anomaly after review.

---

## Procedure

The skill uses a helper script `apply.py` located in the same directory as this SKILL.md. Construct the path at runtime from the skill's own location.

1. **Audit first.** Run:
   ```bash
   python "<this-skill-dir>/apply.py" audit "<path-to-file.md>"
   ```
   This reports, per chapter, the first id, last id, and count of segments that would be tagged, without writing anything. Confirm the chapter numbers and counts look plausible (e.g. match the expected number of chapters in the root text) before applying.

2. **Dry-run to a scratch copy.** Copy the target file to a scratch/output location and run:
   ```bash
   python "<this-skill-dir>/apply.py" apply "<scratch-copy.md>"
   ```
   Do not write directly to the vault file on the first pass.

3. **Spot-check the output.** Read the first ~80 lines and at least one chapter boundary (where the chapter number changes) to confirm ids look right and no root-quote or commentary line was skipped or double-tagged.

4. **Verify idempotency.** Run `apply.py apply` a second time on its own output and confirm the file is byte-identical (no diff). This confirms the script won't double-tag if run again later.

5. **Verify line count is unchanged.** Compare `wc -l` on the original file and the tagged output — they must match exactly.

6. **Write the result to the real file.** Once verified, overwrite the actual `file` in the vault with the tagged content (or run `apply.py apply "<path-to-file.md>"` directly on it once confidence is established).

---

## Completion check

- [ ] `apply.py audit` was run first and its chapter/count report reviewed before any file was modified
- [ ] Output was dry-run to a scratch copy before touching the vault file
- [ ] First ~80 lines and at least one chapter boundary spot-checked in the output
- [ ] Idempotency verified (second run on the tagged output produces no diff)
- [ ] Total line count of the output matches the original file
- [ ] No transclusion line, blank line, heading, or frontmatter line was modified
- [ ] Final tagged file written to the correct vault path

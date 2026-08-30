name: abc-commentary-formator
description: Three-task formatting pipeline for this vault's segmented Bodhicaryavatara/BCA commentary files that come with a companion bare ས་བཅད outline file (a bullet-list TOC whose entries carry ^TOC-N-N-N... anchors, one number segment per nesting depth, e.g. bo-NKW སྤྱོད་འཇུག་ས་བཅད། ས་བཅད་རྐྱང་པ།.md). Task 1 (heading tagging) aligns every heading-shaped line in the commentary against the outline's titles and rewrites it with the correct number of "#" for its true nesting depth, fixing bare/wrong/missing heading levels including bullet-styled "* **text**" pseudo-headings. Task 2 (segmentation check) scans the whole body for prose segments that read as two merged thoughts and reports candidates for splitting -- report-only, never edits. Task 3 (Obsidian Block IDs) stamps two SEPARATE numbering sequences: one tree-shaped id per heading (e.g. ^I-1-1-2-0) reflecting its position in the outline, and one flat restart-per-level-2-heading id per body paragraph/verse-stanza (e.g. ^I-5, ^1-834, ^2-3) -- headings and body text are never numbered with the same sequence. Use this whenever the user asks to "tag headings" against an outline/ས་བཅད file, "fix heading levels," "add/update Obsidian Block IDs" or "segment IDs" for a commentary file (heading or body, or both), "check for long segments that could be split," or generally wants a segmented commentary file under 0-INBOX (matching *_bo_segmented*, *_segmented_tagged*, or similar) brought in line with this vault's heading/Block-ID conventions. Distinct from BCA-Heading-Level-Tagger, which handles a different, older file convention (bare dot-numbered outline lines like "1.1.1.2" embedded directly in the commentary text, with body Block IDs restarting at every chapter) -- ask the user which convention their file uses if it's ambiguous; this skill is for files that carry their outline structure in a SEPARATE ས་བཅད file and want body Block IDs restarting only at level-2 headings.
Creator: Tigerboy
created: 2026-08-30
version: "1.0"

# ABC Commentary Formator

## What this does

This skill formats a segmented Tibetan commentary file (in `0-INBOX/`) that has a companion **outline file** -- a separate bullet-list ས་བཅད (bare topical outline) whose entries carry `^TOC-N-N-N...` anchors, one dash-separated number per nesting depth. That outline is the ground truth for heading structure; the commentary file's own headings are matched against it rather than inferred purely from local context, because a commentary's headings are often bare, wrongly leveled, or formatted as bullets instead of real markdown headings.

Three tasks, each independently useful, normally run in this order:

1. **Heading tagging** (`scripts/align_headings.py`) -- aligns the commentary's heading-shaped lines against the outline and rewrites each with the correct `#` depth.
2. **Segmentation check** (`scripts/find_long_segments.py`) -- reports (does not edit) long body segments that look like two merged thoughts.
3. **Obsidian Block IDs** (`scripts/tag_heading_block_ids.py` then `scripts/tag_body_block_ids.py`) -- stamps two independent id sequences, one for headings and one for body text.

Run 1 before 3 (Block IDs are computed from heading depth/position, so headings must already be correctly leveled). Task 2 can run any time after 1, independently of 3 -- it only reads, never writes.

## Task 1: Heading tagging (`align_headings.py`)

### Why alignment, not just counting number-of-segments

A companion outline entry's `^TOC-1-1-2-2` tells you its depth (4 segments -> heading level 5) but the commentary's own heading TEXT differs slightly from the outline's -- the commentary adds an ordinal word (དང་པོ་/གཉིས་པ་/གསུམ་པ་/...) that the bare outline omits, and occasional wording drifts (e.g. outline `བོད་སྐད་ལྟར་སྨོས་པ` vs. commentary `བོད་སྐད་དུ་སྨོས་པ`). So matching is done by normalized-title similarity (ordinal-stripped, punctuation-stripped), using a Needleman-Wunsch global alignment over BOTH sequences in order -- this correctly handles:

- Outline nodes with **no heading of their own** in the body (the text goes straight from a parent heading into that parent's own children without ever stating the intermediate node -- e.g. "དགོས་པ་དངོས" is implied but never itself headed). These are expected gaps, not errors -- never fabricate heading text for them.
- Body headings with **no outline match** (hand-added `## N. Chapter N` title lines the outline doesn't track, or headings whose wording drifted too far to match confidently). Leave these completely untouched.
- Existing headings that are **already correctly leveled** -- these end up unchanged (idempotent).

### What counts as a heading-candidate line

Any of: an existing markdown heading (`#` through `#############`), a `* **bold**` bullet, or a bare `**bold**` line. This vault's commentaries use bullets/bold as an ad-hoc heading substitute before this skill fixes them.

### The glued-heading data quirk

Occasionally two headings end up on one physical line with a stray outline-number code stuck in the middle, e.g.:

```
**གསུམ་པ་ཕན་ཡོན་དཔེའི་སྒོ་ནས་བསྟན་པ།1.2.2.1.1.1.2.1.3.1 དང་པོ། གསེར་འགྱུར་...**
```

`align_headings.py` detects a 3+-segment dot-number glued directly onto non-whitespace (no space before it -- that's the signal it's stuck on, not just mentioned in prose) and splits it into two separate heading lines before alignment, so both halves get tagged at their correct (different) depths.

### Running it

```bash
python3 scripts/align_headings.py "<path-to-staged-file>" "<path-to-outline-file>"
```

Writes a `.BACKUP-YYYYMMDD-HHMMSS.md` next to the target before overwriting in place. Check the printed summary:

- **matched** should account for the large majority of heading-candidates.
- **low-confidence matches (<0.8)** -- skim every one of these; they're usually correct (wording drift) but occasionally a genuine mismatch. Never silently trust a run with many low-confidence matches on a new file family without spot-checking a handful of them against the source.
- **outline entries with no matching heading** and **body candidates with no outline match** are both normal in nonzero numbers (see above) -- only worry if the counts look wildly out of proportion to the file's length.

### Verification: no heading level should jump by more than 1

After tagging, walk the headings in order and flag any place level increases by more than 1 step (e.g. level 5 straight to level 7). A jump of exactly the size of one missing outline node is expected and fine (see above); a jump you can't explain by a genuinely absent outline node is worth asking the user about rather than assuming. A quick way to check:

```python
prev = None
for lineno, level, text in headings:  # parsed the same way align_headings.py does
    if prev and level > prev[1] + 1:
        print(prev, "->", (lineno, level, text))
    prev = (lineno, level, text)
```

If the user has hand-corrected specific headings' levels since your last check, re-stage the file and re-run this check on the CURRENT content before reporting -- this file family is often being edited live by the user in parallel with your work.

### Related manual cleanups (not automated by this skill, but common asks on the same files)

These aren't part of `align_headings.py` but come up on the same file family and are worth knowing:

- **Removing hand-added numbered chapter-title lines** (e.g. `### 2. ལེའུ་གཉིས་པ། སྡིག་པ་བཤགས་པ། ^2-0`) if the user no longer wants them, once the outline-based headings already carry that structure. Do this as a simple line-removal pass (also delete one of the two blank lines left dangling around each removed line, to avoid a double blank), keyed on a regex like `^#+\s*\d+\.\s*ལེའུ`.
- **Inserting a blank line between two headings that are directly adjacent** (no blank line between them) -- this vault's convention wants one blank line between every pair of heading lines, matching example: `####### **...**` immediately followed by `######## **...**` should get a blank line inserted between them. Simple line-scan: after any heading line, if the very next line is also a heading line, insert a blank line.

## Task 2: Segmentation check (`find_long_segments.py`)

Report-only -- **never edit the file** for this task unless the user explicitly asks you to apply a specific split. A "long segment" is a prose body block that reads as two independent thoughts merged together; the signal used is a `། །` (double shad, the normal Tibetan full-stop) sitting well before the very end of the segment (between 20% and 85% of its length) rather than only at the end.

```bash
python3 scripts/find_long_segments.py "<path-to-staged-file>" --min-length 800 --out report.md
```

Deliver `report.md` to the user (it's a markdown table -- send it as a file, don't try to paste an 800+-row table into chat). Segments with a clean break are strong candidates; segments without one still get listed (long but no obvious midpoint) since they're worth a human look even though the split point isn't mechanically obvious -- never invent a split point for these without a clear sentence boundary to point to.

## Task 3: Obsidian Block IDs -- two separate sequences

This vault's `^label-N` anchors are called **Obsidian Block IDs**. This skill stamps TWO independent sequences that must never be merged or cross-numbered:

### 3a. Heading Block IDs (`tag_heading_block_ids.py`)

Tree-shaped, one id per heading, encoding its position in the outline:

- Every id is a path of 1-based sibling-position numbers (one segment per level below the first level-2 heading), always ending in a constant `-0`. The count of `-N-` segments in the id always equals `heading level - 1` -- e.g. `^I-1-1-2-0` is 4 segments -> level 5.
- The level-2 (`##`) headings get special root labels: the FIRST one is `"I"`; every one after that is a plain arabic number starting at 1 (2nd level-2 heading -> `"1"`, 3rd -> `"2"`, ...). This matches the existing hand-set convention in this file family (roman numeral for the intro, arabic for the rest).
- Every other heading gets its 1-based sibling index among headings sharing the same nearest-shallower-level ancestor, appended to that ancestor's path (ancestor's own trailing `-0` dropped), plus its own trailing `-0`.
- **Skipped levels** (outline has an implicit parent that never got its own heading -- see Task 1) are padded with an implicit sibling index of 1 for the missing level, so id depth still matches heading level across the gap. Don't try to "fix" this by inventing heading text.

```bash
python3 scripts/tag_heading_block_ids.py "<path-to-staged-file>"
```

Check the printed depth-mismatch and duplicate-id counts -- both must be 0. Validate against any pre-existing hand-set anchors in the file (e.g. `^I-0`, `^1-0`) if present -- the algorithm should reproduce them exactly; if it doesn't, something about this file's root-labeling doesn't match the "I / 1 / 2 / ..." convention and you should ask the user rather than force it.

### 3b. Body-text Block IDs (`tag_body_block_ids.py`)

Flat, restarts only at level-2 headings:

- `<label>` is inherited from the nearest preceding level-2 heading's OWN id (its label, with trailing `-0` dropped) -- so it's always `"I"`, `"1"`, `"2"`, etc., matching 3a's root labels.
- `<n>` restarts at 1 right after that level-2 heading and counts every body segment (paragraph or verse-stanza) continuously -- across every chapter and sub-heading under that ONE level-2 heading -- until the next level-2 heading. **This does not restart at chapter boundaries or at any heading deeper than level 2** -- that's the key difference from this vault's other, older commentary-formatting skill.
- Content before the very first level-2 heading gets label `"0"`.
- **Every non-heading, non-frontmatter, non-lone-embed-line block gets an id, whether or not it already had one.** A body block that currently has NO anchor at all (e.g. a paragraph a human split off from a bigger block by hand, leaving the new fragment un-anchored) must still be tagged -- don't just renumber existing anchors and skip blocks that lack one. This was a real bug once: silently skipping anchor-less blocks left segments permanently untagged.
- Frontmatter (the `---`-delimited YAML block at the very top) and lone image-embed lines (`![[...]]`, referencing another file's own block) are never touched or counted.
- A heading line is always its own block boundary even with no blank line separating it from adjacent text (e.g. YAML frontmatter's closing `---` immediately followed by the `# document title` heading with no blank line between them) -- grouping blocks purely by blank lines would merge the heading into the frontmatter's "block" and corrupt it. `tag_body_block_ids.py` handles this; if you ever write a variant of this logic yourself, keep this in mind.

```bash
python3 scripts/tag_body_block_ids.py "<path-to-staged-file>"
```

Check the printed per-label range (`label X: 1..N`) -- ranges should be gap-free and start at 1 for each label. The "segments that previously had NO Obsidian Block ID" list should be reviewed even when it's non-empty and the run looks otherwise fine -- each one is a real content segment that had silently been missing an id; tell the user about any it finds, since it means their file had a gap they may not know about.

## How to run the whole pipeline

1. Stage the target file (and its outline file, for Task 1) via `device_stage_files` if it lives on the user's Obsidian vault.
2. **Re-stage right before each task**, not just once at the start of the conversation -- this file family is often edited live by the user in Obsidian while you're working on it in the same session. Diff the freshly staged copy against what you last worked from before assuming nothing changed; if it has, redo your analysis on the current content rather than risk clobbering the user's edits with stale output.
3. Run Task 1 (`align_headings.py`), review its summary, and only then run Task 3a (`tag_heading_block_ids.py`) followed by 3b (`tag_body_block_ids.py`) -- in that order, since 3a/3b depend on headings already being correctly leveled. Task 2 (`find_long_segments.py`) can run independently at any point after Task 1, and never needs to run before delivering a file (it's report-only).
4. Each script writes its own timestamped backup next to the target before overwriting in place -- running the full pipeline leaves multiple backups, which is expected, not a bug.
5. Commit the final file back to its **original path** with `device_commit_files` (don't create a `_tagged`/`_numbered` sibling file), using the `expectedMtimeMs` from your most recent stage of that exact file so a newer edit from the user is never silently overwritten.
6. Tell the user: how many headings were retagged (and flag any low-confidence matches you didn't already resolve), the final Block ID ranges for both headings and body text, and, if Task 2 was run, how many long-segment candidates were found and where the report was sent.

## Notes on this file family

- These files are large (multi-thousand-line) Tibetan commentary text with embedded verse quotes (`>` blockquote lines), transclusion embeds (`![[other-file#^id]]`), and pre-existing partial Obsidian Block IDs mixed in with the heading structure. None of the scripts here ever touch verse-quote content or cross-file embeds beyond deciding whether to skip them.
- If a file in this set doesn't come with a companion ས་བཅད outline file, or uses a different chapter-heading convention than this skill assumes, ask the user rather than guessing -- these scripts are intentionally narrow to the conventions validated on this vault's files.
- This skill is distinct from **BCA-Heading-Level-Tagger** (also in this Skills folder), which targets an older convention where the ss-bcad numbering is typed bare directly into the commentary text (no separate outline file) and body Block IDs restart at every chapter rather than every level-2 heading. If it's unclear which convention a given file uses, ask the user before picking one.

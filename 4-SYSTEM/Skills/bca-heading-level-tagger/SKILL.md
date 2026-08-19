---
name: bca-heading-level-tagger
description: Three-step pipeline for Bodhicaryavatara/BCA commentary and root-text files in this Obsidian vault. Step 1 converts bare numbered outline headings (ས་བཅད-style numbering like 1, 1.1, 1.1.1.2.2.4) into proper Obsidian markdown heading levels and nested bullet lists, so the outline becomes foldable. Step 2 (re)numbers every content segment's Obsidian block-reference id (^0-1, ^1-1, ...), restarting the count at ^N-1 for each chapter, so every paragraph and verse stanza is individually linkable/transcludable. Step 3 strips the now-redundant ས་བཅད numbers back off the sub-headings (### and deeper, and the outline bullets), leaving the chapter-level ## numbers in place, since heading depth and bullet indentation already carry that structure foldably. Use this whenever the user asks to "tag headings," "apply heading levels," "convert the numbering to headings," "make the outline foldable," "update block ids," "renumber block references," "remove/strip the numbers from headings," or points to a segmented commentary file (e.g. anything under 0-INBOX matching *_bo_segmented*, *_segmented*, or similar ས་བཅད outline files) and wants it prepared for use in the vault. Also trigger if the user mentions Obsidian fold/unfold arrows, or ^chapter-N block references, in connection with one of these Tibetan commentary files.
---

# BCA Heading-Level Tagger

## What this does

Files in this vault's Bodhicaryavatara (སྤྱོད་འཇུག) commentary set go through three passes, always in this order:

1. **Tag headings** (`scripts/tag_headings.py`) -- rewrites the bare ས་བཅད outline numbering (`1.1`, `1.1.1.2.2.4`, ...) into real markdown headings and nested bullet lists, so the outline folds/unfolds natively in Obsidian.
2. **Update block IDs** (`scripts/update_block_ids.py`) -- walks the now-tagged file and stamps every content segment (paragraph or verse stanza) with an Obsidian block reference `^N-M`, where `N` is the chapter number and `M` restarts at 1 for each chapter. This makes every segment individually linkable and transcludable.
3. **Strip heading numbers** (`scripts/strip_heading_numbers.py`) -- once folding (step 1) and block ids (step 2) no longer need the visible outline numbers, this strips the leading number off every sub-heading (`###` through `######`, and the outline bullets), leaving just the heading marker and the Tibetan text. Top-level `## N. ...` chapter headings keep their number (see step 3's own section below for why).

The order is load-bearing, not just a convention:

- Step 2 depends on step 1's output -- it finds chapter boundaries and skips non-content lines by looking for markdown headings (`##`...`######`) and the depth-6+ bullet lists step 1 produces. Running it on an untagged file would wrongly number bare outline lines as content segments.
- Step 3 depends on step 2 having already finished -- once it strips the numbers off sub-headings, that information is gone from the file (the block ids elsewhere already captured what mattered). Running step 3 before step 2 wouldn't corrupt anything, but it would just be wasted work since step 2 doesn't need sub-heading numbers anyway; running step 3 before step 1 would do nothing (the lines aren't heading-shaped yet).
- Running step 1 again after step 3 is harmless but pointless (nothing left to tag). Keep the order strict: tag headings -> update block IDs -> strip heading numbers.

### Step 1 details: heading tagging

Bare lines like `1.1`, `1.1.1`, `1.1.1.1.1.2` mark sub-points, but Obsidian can't fold/unfold plain text like that. This step rewrites those bare numbered lines into real markdown headings (or bullet lists once the nesting goes past what markdown headings support), so the outline becomes navigable with Obsidian's native fold arrows.

Depth of numbering (count the dot-separated groups) maps to heading level:

| Digit groups | Example | Becomes |
|---|---|---|
| 1 | `0`, `1` | `##` |
| 2 | `1.1` | `###` |
| 3 | `1.1.1` | `####` |
| 4 | `1.1.1.1` | `#####` |
| 5 | `1.1.1.1.1` | `######` |
| 6 | `1.1.1.1.1.1` | `* ` (bullet, no indent) |
| 7 | `1.1.1.1.1.1.1` | `    * ` (bullet, one indent level) |
| 8+ | ... | one more 4-space indent per level beyond 6 |

Markdown only goes to `######`, and Obsidian's outline gets deep enough (sometimes 8+ levels) that bullet lists take over past level 5 — Obsidian folds bullet nesting at any depth, so this keeps the whole outline foldable end to end.

## Step 1: When NOT to re-tag a line

A line only gets converted if it is a **bare** numbered line — just the number, then whitespace, then the heading text, nothing else in front.
This is what makes the conversion safe to run on partially-tagged files:

- Chapter markers that are already hand-tagged, like `## 1. ལེའུ་དང་པོ།
  བྱང་ཆུབ་སེམས་ཀྱི་ཕན་ཡོན་བཤད་པ།`, are left untouched — they start with
  `#`, not a digit.
- Six-plus-digit lines someone already prefixed with `-` or `*` by hand
  are left untouched too, since they no longer start with a digit.
- YAML frontmatter (the block between the first two `---` lines at the
  top of the file — book_id, title, author, etc.) is always skipped.

One quirk to watch for: if a file has been partially hand-tagged before, some of those pre-existing 6+ digit bullets may use `-` and others `*` inconsistently (this has happened in this vault). The script won't fix those — it only acts on bare numbered lines — so if the user asks for a fully consistent outline, do a manual pass afterward to normalize bullet characters on lines the script skipped.

## Step 1: Concatenated headings

Another data quirk in this vault's files: a heading number is sometimes glued directly onto the end of the *previous* heading's prose with no line break, e.g.:

```
...བསྟན་པ།1.2.2.1.1.1.2.1.3.1 དང་པོ། ...
```

That number is invisible to the bare-line rule above since it isn't at the start of its own line, so it would otherwise never get tagged. The script detects this before tagging and splits it onto its own line: it looks for a dot-separated number with three or more digit groups that is immediately preceded by non-whitespace (no space — that's the signal it's glued on rather than just mentioned in the sentence) and immediately followed by whitespace or end of line. The number and everything after it becomes a new line, ready to be tagged normally.

This is intentionally conservative — requiring no space before, and 3+digit groups — so it won't mistake an ordinary number mentioned in running prose for a broken heading. The script prints every line it split so you can spot check them; skim that list before telling the user the job is done.

## Step 1: Bundled script details

`scripts/tag_headings.py` extracts number tokens with a *maximal-match* regex (`\d+(?:\.\d+)*`) rather than searching for the glued-on suffix directly. That matters: naively searching for "3+ digit groups preceded by non-whitespace" would also match inside a line's own legitimate leading number — e.g. it could mistake `2.1.4` inside `1.2.1.4 ...` at the very start of a line for a glued-on heading, since `.` right before `2.1.4` is non-whitespace. Matching the full token first and then checking whether *that whole token* starts at position 0 avoids this trap. Keep this in mind if you ever touch the script's detection logic — it's the kind of regex bug that passes on simple examples and then corrupts real files.

## Step 2: What "segment" means for block-ID numbering

`scripts/update_block_ids.py` stamps an Obsidian block reference on every **content segment** in the file, where a segment is a maximal run of non-blank lines that is not heading-like, bounded by blank lines (per this vault's segmentation convention: paragraphs and stanzas are separated by blank lines, and the id goes on the last line of the segment):

- An ordinary prose paragraph -> one id.
- A multi-line verse/stanza block (consecutive `>` blockquote lines) -> one id for the whole stanza, on its last line.
- A short lead-in line glued directly onto a following stanza with **no** blank line between them (e.g. `དང་པོ་ནི།` immediately followed by a `>` quote) -> still one segment, one id together, because nothing blank separates them — don't split these apart by hand.

Headings are never numbered and never counted as segments: markdown headings (`#` through `######`) and the depth-6+ bullet pseudo-headings step 1 produces (`* 1.2.2.1.1.1 ...`, indented 4 spaces per level beyond depth 6). This is also why step 2 must run after step 1 — before tagging, those sub-points are bare numbered lines indistinguishable from ordinary content, so step 2 would wrongly number them as segments.

One more quirk this script handles: sometimes a content line runs directly into a heading line with **no blank line** between them (the sentence that introduces a sub-point sits right above that sub-point's heading). The script doesn't split blocks purely on blank lines — within each blank-line-delimited block it further splits on every heading/non-heading boundary, so the content half still gets numbered and the heading half is still skipped correctly.

### Step 2: Chapter detection and numbering

A top-level chapter heading looks like `## 0. ...`, `## 1. ...`, ... (exactly what step 1 produces for 1-digit-group numbering). The captured number becomes the chapter label verbatim, so chapter 0's segments are `^0-1, ^0-2, ...`, chapter 1's are `^1-1, ^1-2, ...`, and so on — the counter restarts at every `## N.` heading. Sub-headings (`###` and deeper, and the outline bullets) never reset the counter, only a top-level chapter heading does.

Pre-existing ids already sitting on chapter/sub-heading lines (like `^I-0`, `^1-0`) are left completely untouched — step 2 only ever touches content-run segments. If a segment's last line already carries some block id (stale, partial, or from a previous run), the script strips it and writes the freshly computed one in its place, so **this script is safe and idempotent to re-run** on a file that's already been numbered — re-running it on an already-correct file produces a byte-identical result.

## Step 3: What gets stripped, and why chapter numbers stay

`scripts/strip_heading_numbers.py` removes the leading ས་བཅད number (and the single space after it) from every sub-heading: markdown headings `###` through `######`, and the depth-6+ outline bullets (`* 1.2.2.1.1.1 ...` / `- 1.2.2.1.1.1 ...`, at any indent level, either bullet character). For example:

```
### 1.1 སྒྱུར་བྱེད་དམ་པའི་ཀླད་ཀྱི་དོན།        ->  ### སྒྱུར་བྱེད་དམ་པའི་ཀླད་ཀྱི་དོན།
* 1.2.2.1.1.1 དང་པོ་ལེའུའི་གཞུང་།            ->  * དང་པོ་ལེའུའི་གཞུང་།
```

Top-level `## N. ...` chapter headings are **left alone on purpose** -- their number is the only thing step 2 uses to auto-detect chapter boundaries. If this script also stripped it, the file would lose the anchor a future re-run of `update_block_ids.py` needs to know which chapter it's in, and there'd be no way to recover that short of restoring from a backup. Chapter numbers also double as a human-readable label ("Chapter 6") that's worth keeping regardless. If a user specifically asks to remove chapter numbers too, treat that as a one-off manual edit outside this skill's normal pipeline, and warn them that step 2 won't be auto-re-runnable on that file afterward.

Also left untouched: any block reference (`^1-0`, `^I-0`, `^6-42`, ...) sitting on a heading line, and all ordinary content -- this script only ever matches lines that are already heading-shaped, so it never touches prose.

Like step 2, this script is idempotent: running it again on a file it's already processed finds nothing left to strip and reports zero changes.

## How to run it

Run all three scripts in order — heading tagging, then block-ID numbering, then heading-number stripping — against the same staged file:

1. If the target file lives on the user's Obsidian vault (reached via the device bridge / `mcp__remote-devices__*` tools), stage it first with `device_stage_files` so it's readable in this session.
2. **Step 1 — tag headings:**
   ```bash
   python3 scripts/tag_headings.py "<path-to-staged-file>"
   ```
   Check the stdout for any "Repaired N concatenated-heading line(s)" report and glance at those specific lines — they involved splitting text, so they're worth a quick look even though the detection is conservative. Spot-check a stretch of the output (`Read` a slice of it) to confirm headings landed at the depth you'd expect, especially around any 6+ digit sections.
3. **Step 2 — update block IDs**, run on the same file (now heading-tagged) right after:
   ```bash
   python3 scripts/update_block_ids.py "<path-to-staged-file>"
   ```
   Check the stdout's per-chapter summary (`chapter N: M segments (^N-1 .. ^N-M)`) — the counts should look plausible for the chapter's length, and there should be no "content segment before any chapter heading" warnings. Spot-check a chapter boundary in the output to confirm the counter actually restarted at `^N-1`.
4. **Step 3 — strip heading numbers**, run last on the same file:
   ```bash
   python3 scripts/strip_heading_numbers.py "<path-to-staged-file>"
   ```
   Check the stdout's per-level breakdown (`###: N`, `bullet: N`, ...) against what step 1 reported tagging, and confirm the `##` chapter heading lines still show their number (`Read` a few) — if a chapter heading's number went missing, something's wrong and shouldn't be committed.
5. All three scripts write a backup next to the file before overwriting it in place, using this vault's existing naming convention: `<filename>.BACKUP-YYYYMMDD-HHMMSS.md` (matching files already present in this vault, e.g. `BCAC19_KKP_bo_segmented.BACKUP-20260630-053157.md`). Running all three back to back leaves three backups (pre-step-1, pre-step-2, pre-step-3) — that's expected, not a bug.
6. If the file came from the device bridge, commit the final file back to its **original path** with `device_commit_files` (overwrite in place — don't create a `_tagged`, `_numbered`, or `_stripped` sibling file). The backups from steps 2-4 are the safety net, so overwriting the original is expected and fine.
7. Tell the user which chapters were processed, the final segment counts per chapter, and how many heading numbers were stripped, and flag anything any of the scripts warned about.

## Notes on this file family

These commentary files are large (multi-thousand-line) Tibetan text with embedded verse quotes (`>` blockquote lines) and Obsidian block references (`^1-0`, `^I-0`, etc.) mixed in with the outline numbering — those are never mistaken for headings since they don't start a line with digits followed by whitespace, and (once step 1 has run) never mistaken for content segments either, since they sit on heading lines. If a future file in this set uses a different numbering convention (e.g. letters, roman numerals, or a different delimiter than `.`), or a different chapter-heading format than `## N. ...`, ask the user how they'd like those handled rather than guessing — all three scripts are intentionally narrow to the conventions used throughout this vault's BCA commentary segmentation.

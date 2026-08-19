---
name: bca-heading-level-tagger
description: Two-step pipeline for Bodhicaryavatara/BCA commentary and root-text files in this Obsidian vault. Step 1 converts bare numbered outline headings (ས་བཅད-style numbering like 1, 1.1, 1.1.1.2.2.4) into proper Obsidian markdown heading levels and nested bullet lists, so the outline becomes foldable. Step 2 (re)numbers every content segment's Obsidian block-reference id (^0-1, ^1-1, ...), restarting the count at ^N-1 for each chapter, so every paragraph and verse stanza is individually linkable/transcludable. Use this whenever the user asks to "tag headings," "apply heading levels," "convert the numbering to headings," "make the outline foldable," "update block ids," "renumber block references," or points to a segmented commentary file (e.g. anything under 0-INBOX matching *_bo_segmented*, *_segmented*, or similar ས་བཅད outline files) and wants it prepared for use in the vault. Also trigger if the user mentions Obsidian fold/unfold arrows, or ^chapter-N block references, in connection with one of these Tibetan commentary files.
---

# BCA Heading-Level Tagger

## What this does

Files in this vault's Bodhicaryavatara (སྤྱོད་འཇུག) commentary set go through two passes, always in this order:

1. **Tag headings** (`scripts/tag_headings.py`) -- rewrites the bare ས་བཅད outline numbering (`1.1`, `1.1.1.2.2.4`, ...) into real markdown headings and nested bullet lists, so the outline folds/unfolds natively in Obsidian.
2. **Update block IDs** (`scripts/update_block_ids.py`) -- walks the now-tagged file and stamps every content segment (paragraph or verse stanza) with an Obsidian block reference `^N-M`, where `N` is the chapter number and `M` restarts at 1 for each chapter. This makes every segment individually linkable and transcludable.

Step 2 depends on step 1's output -- it finds chapter boundaries and skips non-content lines by looking for markdown headings (`##`...`######`) and the depth-6+ bullet lists step 1 produces. Never run step 2 on a file that hasn't been through step 1 first, and never run step 1 after step 2 (it would leave the block ids in place but has no reason to touch them, so this isn't harmful, just pointless to do out of order -- keep it heading-tag-then-block-id).

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

## How to run it

Run both scripts in order — heading tagging first, block-ID numbering second — against the same staged file:

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
4. Both scripts write a backup next to the file before overwriting it in place, using this vault's existing naming convention: `<filename>.BACKUP-YYYYMMDD-HHMMSS.md` (matching files already present in this vault, e.g. `BCAC19_KKP_bo_segmented.BACKUP-20260630-053157.md`). Running both scripts back to back leaves two backups (pre-step-1 and pre-step-2) — that's expected, not a bug.
5. If the file came from the device bridge, commit the final file back to its **original path** with `device_commit_files` (overwrite in place — don't create a `_tagged` or `_numbered` sibling file). The backups from steps 2-3 are the safety net, so overwriting the original is expected and fine.
6. Tell the user which chapters were processed and the final segment counts per chapter, and flag anything the scripts warned about.

## Notes on this file family

These commentary files are large (multi-thousand-line) Tibetan text with embedded verse quotes (`>` blockquote lines) and Obsidian block references (`^1-0`, `^I-0`, etc.) mixed in with the outline numbering — those are never mistaken for headings since they don't start a line with digits followed by whitespace, and (once step 1 has run) never mistaken for content segments either, since they sit on heading lines. If a future file in this set uses a different numbering convention (e.g. letters, roman numerals, or a different delimiter than `.`), or a different chapter-heading format than `## N. ...`, ask the user how they'd like those handled rather than guessing — both scripts are intentionally narrow to the conventions used throughout this vault's BCA commentary segmentation.

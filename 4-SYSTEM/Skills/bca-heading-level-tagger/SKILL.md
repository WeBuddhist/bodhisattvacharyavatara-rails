---
name: bca-heading-level-tagger
description: Converts bare numbered outline headings (ས་བཅད-style numbering like 1, 1.1, 1.1.1.2.2.4) in Bodhicaryavatara/BCA commentary and root-text files in this Obsidian vault into proper Obsidian markdown heading levels and nested bullet lists, so the outline becomes foldable. Use this whenever the user asks to "tag headings," "apply heading levels," "convert the numbering to headings," "make the outline foldable," or points to a segmented commentary file (e.g. anything under 0-INBOX matching *_bo_segmented*, *_segmented*, or similar ས་བཅད outline files) and wants its numbered sub-points turned into ##/###/#### style headings. Also trigger if the user mentions Obsidian fold/unfold arrows in connection with a numbered outline in one of these Tibetan commentary files.
---

# BCA Heading-Level Tagger

## What this does

Files in this vault's Bodhicaryavatara (སྤྱོད་འཇུག) commentary set are segmented with a nested outline numbering system (ས་བཅད) rather than markdown headings: bare lines like `1.1`, `1.1.1`, `1.1.1.1.1.2` mark sub-points, but Obsidian can't fold/unfold plain text like that. This skill rewrites those bare numbered lines into real markdown headings (or bullet lists once the nesting goes past what markdown headings support), so the outline becomes navigable with Obsidian's native fold arrows.

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

## When NOT to re-tag a line

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

## Concatenated headings

Another data quirk in this vault's files: a heading number is sometimes glued directly onto the end of the *previous* heading's prose with no line break, e.g.:

```
...བསྟན་པ།1.2.2.1.1.1.2.1.3.1 དང་པོ། ...
```

That number is invisible to the bare-line rule above since it isn't at the start of its own line, so it would otherwise never get tagged. The script detects this before tagging and splits it onto its own line: it looks for a dot-separated number with three or more digit groups that is immediately preceded by non-whitespace (no space — that's the signal it's glued on rather than just mentioned in the sentence) and immediately followed by whitespace or end of line. The number and everything after it becomes a new line, ready to be tagged normally.

This is intentionally conservative — requiring no space before, and 3+digit groups — so it won't mistake an ordinary number mentioned in running prose for a broken heading. The script prints every line it split so you can spot check them; skim that list before telling the user the job is done.

## Bundled script details

`scripts/tag_headings.py` extracts number tokens with a *maximal-match* regex (`\d+(?:\.\d+)*`) rather than searching for the glued-on suffix directly. That matters: naively searching for "3+ digit groups preceded by non-whitespace" would also match inside a line's own legitimate leading number — e.g. it could mistake `2.1.4` inside `1.2.1.4 ...` at the very start of a line for a glued-on heading, since `.` right before `2.1.4` is non-whitespace. Matching the full token first and then checking whether *that whole token* starts at position 0 avoids this trap. Keep this in mind if you ever touch the script's detection logic — it's the kind of regex bug that passes on simple examples and then corrupts real files.

## How to run it

1. If the target file lives on the user's Obsidian vault (reached via the device bridge / `mcp__remote-devices__*` tools), stage it first with `device_stage_files` so it's readable in this session.
2. Run the bundled script on the staged copy:
   ```bash
   python3 scripts/tag_headings.py "<path-to-staged-file>"
   ```
   This overwrites the file in place, but first writes a backup next to it using this vault's existing naming convention:
   `<filename>.BACKUP-YYYYMMDD-HHMMSS.md` (matching files already present in this vault, e.g. `BCAC19_KKP_bo_segmented.BACKUP-20260630-053157.md`).
3. If the file came from the device bridge, commit the tagged file back to its **original path** with `device_commit_files` (overwrite in place — don't create a `_tagged` sibling file). The backup from step 2 is the safety net, so overwriting the original is expected and fine.
4. Check the script's stdout for any "Repaired N concatenated-heading line(s)" report and glance at those specific lines in the output — they involved splitting text, so they're worth a quick look even though the detection is conservative.
5. Spot-check a stretch of the output (`Read` a slice of it) to confirm headings landed at the depth you'd expect, especially around any 6+ digit sections, before telling the user it's done.

## Notes on this file family

These commentary files are large (multi-thousand-line) Tibetan text with embedded verse quotes (`>` blockquote lines) and Obsidian block references (`^1-0`, `^I-0`, etc.) mixed in with the outline numbering — those are never mistaken for headings since they don't start a line with digits followed by whitespace. If a future file in this set uses a different numbering convention (e.g. letters, roman numerals, or a different delimiter than `.`), ask the user how they'd like those handled rather than guessing — this script is intentionally narrow to the `\d+(\.\d+)*` pattern used throughout this vault's BCA commentary segmentation.

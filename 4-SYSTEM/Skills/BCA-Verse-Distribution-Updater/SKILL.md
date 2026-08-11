---
name: BCA-Verse-Distribution-Updater
description: Move a verse from one day to another in the Dalai Lama track's daily schedule — updates the Verses and Studio Verse columns in Tibetan-schedule-corrected.md (rippling the shift through every day between the old and new day), and renames the affected day files under the Dalai Lama plan folder to match. Use when the user asks to move/shift a verse to a different day, e.g. "move verse 3-22 to day 50", "shift 5.40 to day 76", "put 8.100 on day 240 instead".
Author:
  - Tigerboy
---

# BCA-Verse-Distribution-Updater

Redistributes verses across days in the Dalai Lama track's 365-day schedule. A schedule row's Verses column ("3.20–3.22") and Studio Verse column ("127–129") describe a contiguous, gap-free block of the chapter's verses; moving one verse to a different day means the boundary between two days shifts, and every day strictly between the old and new position has to shift with it to stay contiguous. Done by hand this is error-prone arithmetic across a 377-line table plus a matching set of file renames; this skill delegates the arithmetic to a script (`scripts/shift_verse.py`) so the two source-of-truth artifacts — the schedule table and the day-file names — never drift out of sync.

This skill changes **only** the Verses and Studio Verse cells for the affected days, and the day-file *names* for those same days. It does not touch Y.Day, Ch.Day, or Date, and it does not touch the *content* inside any day file (verse text, headings, commentary) — see Rules.

---

## Inputs

- `verse` — the verse to move, as `chapter.verse` or `chapter-verse` (e.g. `3.22` or `3-22`).
- `to-day` — the target Y.Day number the verse should land on.
- `schedule` — path to the schedule file. Default: `3-TRANSFORMATIONS/Plans/Dalai Lama/Tibetan-schedule-corrected.md`.
- `plan-root` — path to the Dalai Lama plan folder (contains the `Chapter-N D..-D..` subfolders). Default: `3-TRANSFORMATIONS/Plans/Dalai Lama`.

If the user gives a verse and a target day but nothing else, use the defaults above — do not ask for paths that have a known default in this vault.

## Output

- `3-TRANSFORMATIONS/Plans/Dalai Lama/Tibetan-schedule-corrected.md` — modified in place: Verses and Studio Verse cells rewritten for every day between (and including) the verse's old day and its new day.
- Day files under `3-TRANSFORMATIONS/Plans/Dalai Lama/Chapter-<N> D..-D../` — renamed in place (via `git mv` when the vault is a git repo, so history follows the file) for every day whose verse range changed. File *contents* are untouched by this skill.

---

## Output file format

Schedule row, before and after moving `3.22` from day 49 to day 50 (unaffected columns identical):

```
| 49      | 9      | 3.20–3.22             | 127–129      | Aug 23          |
| 50      | 10     | 3.23–3.24             | 130–131      | Aug 24          |
```
becomes
```
| 49      | 9      | 3.20–3.21             | 127–128      | Aug 23          |
| 50      | 10     | 3.22–3.24             | 129–131      | Aug 24          |
```

Matching filename rename:
```
Day-49-Ch3-V20-22.md  ->  Day-49-Ch3-V20-21.md
Day-50-Ch3-V23-24.md  ->  Day-50-Ch3-V22-24.md
```

---

## Rules

1. **A verse can only move if it sits at a boundary of its current day.** If it's the last verse of its day it may move forward to any later day in the same chapter; if it's the first verse it may move backward to any earlier day. A verse in the middle of a day cannot move without splitting that day's range — the script stops and reports this rather than guessing what the user meant.
2. **Cross-chapter moves are not supported.** A shift where the target day belongs to a different chapter than the source verse changes each chapter's total verse count, the chapter folder's own day range (`Chapter-N D..-D..`), and the studio-verse offset — that needs a human decision, not an automated ripple. The script stops and reports this.
3. **No day may be emptied.** If a shift would reduce some day's range to zero verses, the script stops before writing anything.
4. **Only Verses and Studio Verse change.** Y.Day, Ch.Day, and Date are never modified — the calendar and the day-count structure stay fixed; only which verses fall on which day changes.
5. **Day-file content is never touched by this skill.** Only the file *name* changes to match the new verse range. If the actual verse text/headings inside a renamed day file need to follow the verse to its new day, that is a separate, explicit follow-up — tell the human this is outstanding after the rename.
6. **All-or-nothing.** If any row in the affected range would become invalid (empty, cross-chapter, non-boundary verse, inconsistent studio-verse offset), no file is written and no rename happens — never leave the schedule and the filenames partially updated relative to each other.
7. **Never hand-edit the schedule table or day-file names for this task.** Always go through `scripts/shift_verse.py` so the ripple arithmetic and the renames stay derived from the same computation. Manual edits are only for fixing an unrelated, already-flagged anomaly after review.
8. **Renames use `git mv` when the plan folder is inside a git repo**, so file history follows the move; falls back to a plain rename otherwise.

---

## Procedure

The skill uses a helper script `scripts/shift_verse.py` located in the same directory as this SKILL.md. Construct its path at runtime from the skill's own location.

1. **Audit first, once per session** (cheap, catches pre-existing data issues before you rely on them):
   ```bash
   python "<this-skill-dir>/scripts/shift_verse.py" audit --schedule "3-TRANSFORMATIONS/Plans/Dalai Lama/Tibetan-schedule-corrected.md"
   ```
   Confirms, per chapter, that verse and studio-verse ranges are contiguous and that the studio-verse offset is constant. As of the skill's creation, chapter 3 day 54 has a known pre-existing formatting quirk in its Verses cell (`3.32-3-33` instead of `3.32–3.33`) that the parser tolerates but flags — this is not something to silently "fix" as a side effect of an unrelated shift; only touch it if the human asks.

2. **Plan (dry run) — always do this before applying:**
   ```bash
   python "<this-skill-dir>/scripts/shift_verse.py" plan \
     --schedule "3-TRANSFORMATIONS/Plans/Dalai Lama/Tibetan-schedule-corrected.md" \
     --verse "<chapter.verse>" --to-day <N>
   ```
   Read the printed table of old→new Verses/Studio Verse per affected day and the list of file renames. If the script exits with an error (non-boundary verse, cross-chapter, would-empty day, inconsistent offset), relay that message to the human plainly — do not try to route around it by hand.

3. **Confirm scope with the human if the ripple is large.** A one-day-adjacent move (like the day-49→day-50 example) touches 2 rows; a move across many days touches every day in between. If the plan shows more than a handful of affected days, say so and let the human confirm before applying — it's easy to typo a target day far from the intended one.

4. **Apply:**
   ```bash
   python "<this-skill-dir>/scripts/shift_verse.py" apply \
     --schedule "3-TRANSFORMATIONS/Plans/Dalai Lama/Tibetan-schedule-corrected.md" \
     --verse "<chapter.verse>" --to-day <N> \
     --plan-root "3-TRANSFORMATIONS/Plans/Dalai Lama"
   ```
   This rewrites the schedule file and renames the day files in one pass, using the exact same computation already reviewed in step 2.

5. **Verify.** Re-run `audit` to confirm no new contiguity/offset problems were introduced, and spot-check the renamed files exist under the correct chapter folder with the new names.

6. **Tell the human what was and wasn't done.** State explicitly that day-file *content* was not modified, in case the verse text inside those files needs manual follow-up to actually match their new day.

---

## Completion check

- [ ] `audit` was run and any pre-existing issues noted (not silently fixed)
- [ ] `plan` was run and its output reviewed before `apply`
- [ ] Large ripples (more than a couple of days) were confirmed with the human before applying
- [ ] `apply` completed with the schedule file and every affected day-file rename done together (all-or-nothing)
- [ ] Post-apply `audit` shows no new contiguity or offset issues
- [ ] Human was told that day-file content (verse text/headings) was not changed, only the schedule table and file names

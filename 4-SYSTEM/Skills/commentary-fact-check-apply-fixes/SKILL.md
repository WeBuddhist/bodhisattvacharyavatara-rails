---
name: commentary-fact-check-apply-fixes
description: >
  Applies the ⚠ discrepancies already logged in a grade's
  commentary-fact-check-report-<grade>.md to the graded English BCA translation
  (3-TRANSFORMATIONS/Translations/bo-en-translation/bca-en-<grade>.md), one grade
  and one chapter (or range) at a time, then re-runs commentary-fact-check on that
  same range to confirm the fix landed. Companion to commentary-fact-check: that
  skill only reports (it never edits the translation); this skill is the follow-up
  editing pass it defers to. Use whenever the user asks to "apply the fact-check
  fixes", "fix the discrepancies from the fact-check report", "resolve the ⚠ rows",
  or "automate step 1" / "automate the fix-editing step" after a
  commentary-fact-check run. Only applies fixes that are mechanical corrections
  (wrong named entity, wrong number, dropped content, inconsistent locked
  rendering) with an unambiguous replacement; any ⚠ row that requires a genuine
  interpretive/stylistic judgment call is left untouched and listed for the human
  to decide.
---

# commentary-fact-check-apply-fixes

Turns a commentary-fact-check report's ⚠ rows into actual edits in
`bca-en-<grade>.md`, then re-verifies the fix by re-running `commentary-fact-check`
on the same range. This exists because `commentary-fact-check` deliberately never
edits the translation — "let the user or a follow-up editing pass fix the
translation file itself" — and doing that follow-up pass by hand, verse by verse,
does not scale. Failure mode this prevents: silently "fixing" a translation with an
interpretive rewrite that isn't actually grounded in the commentary, or fixing a
verse and never confirming the fix actually resolved the flagged discrepancy.

This skill **reports and edits only what is mechanical**. It does not resolve
genuine judgment calls (e.g. choosing between two equally valid English names for
a figure with no commentary-stated preference) — those are surfaced to the human,
not decided by the LLM.

---

## Inputs

| Input | Required | Description |
|---|---|---|
| **Grade** | ✓ | `beginner`, `general`, or `advanced` — must match a grade that already has a `commentary-fact-check-report-<grade>.md` with at least one ⚠ row in scope. |
| **Scope** | recommended | A chapter number, `colophon`, or explicit verse range (e.g. `2-1 to 2-20`). If omitted, use every ⚠ row in the grade's report that hasn't yet been resolved (see the Fix Log in Output). |
| **Report file** | fixed | `3-TRANSFORMATIONS/Translations/bo-en-translation/commentary-fact-check-report-<grade>.md` — the source of every ⚠ row this skill acts on. If it doesn't exist, stop: nothing to fix. |
| **Commentary source** | fixed | `1-SOURCES/Commentaries/Transcluded/BCAC19_KS_bo.md` — re-read (or reuse the cached `/tmp/ks_commentary.json` from the parent skill) to ground each fix. Same restriction as the parent skill: this file only, no other commentary. |
| **Target translation** | fixed | `3-TRANSFORMATIONS/Translations/bo-en-translation/bca-en-<grade>.md` — the file this skill edits. |

---

## Output

| Location | Action |
|---|---|
| `3-TRANSFORMATIONS/Translations/bo-en-translation/bca-en-<grade>.md` | Edited in place — only the specific flagged line(s) for each MECHANICAL fix. Nothing else in the file changes. |
| `3-TRANSFORMATIONS/Translations/bo-en-translation/commentary-fact-check-fixes-log-<grade>.md` | Created (first run) or appended (later runs) — a dated changelog of every fix applied and every fix skipped. |
| `3-TRANSFORMATIONS/Translations/bo-en-translation/commentary-fact-check-report-<grade>.md` | Updated by re-invoking `commentary-fact-check` on the same range (that skill's own re-check-replaces-subsection behavior applies here, not a separate write path owned by this skill). |

---

## Output file format

`commentary-fact-check-fixes-log-<grade>.md`:

```markdown
# BCA English Translation — Fact-Check Fix Log — <grade>

Method: mechanical fixes only, applied from ⚠ rows in
commentary-fact-check-report-<grade>.md and grounded in BCAC19_KS_bo.md. Judgment
calls are listed but never auto-applied. This is a draft editing pass, not a
scholarly sign-off — a domain specialist should review before treating any grade
as final, per this vault's standing rule that an LLM never marks its own
translation output complete.

## Run — <date> — Chapter <N> (or range)

### Applied

| Verse | Before | After | Grounds |
|---|---|---|---|
| 2-13 | ...Manjushri... | ...Manjughosha... | Locked rendering used at 2-49; report flagged inconsistency |

### Skipped — needs human judgment

| Verse | Discrepancy | Why not auto-applied |
|---|---|---|
| <id> | <what the report's ⚠ said> | <e.g. two valid renderings, no commentary-stated preference; style choice not factual error> |

**Result: <k> applied, <m> skipped for human review.**

### Re-verification

Ran `commentary-fact-check` on <grade> / Chapter <N> after applying fixes.
Result: <pass count>/<total>, <remaining ⚠ count> — see
`commentary-fact-check-report-<grade>.md#chapter-<n>` for the fresh verdict table.
```

---

## Rules

1. **Source of truth is the report, not a fresh re-read of the commentary from scratch.** Only act on rows already marked ⚠ in `commentary-fact-check-report-<grade>.md` for the requested scope. Do not go looking for new discrepancies — that's the parent skill's job.
2. **Minimal edit only.** Change only the span the report's note identifies as wrong (a name, a number, a dropped clause, an inconsistent rendering). Never rewrite a verse's phrasing, meter, or register beyond what the discrepancy requires. This is an edit, not a retranslation.
3. **Every edit is grounded in `BCAC19_KS_bo.md`**, via the specific commentary passage the report already cited, or a fresh read of that verse's passage if the report's note doesn't quote enough to act on directly. Never invent a fix from parametric knowledge.
4. **MECHANICAL vs JUDGMENT-CALL triage is mandatory before editing anything.** A row is MECHANICAL only if the commentary unambiguously supports exactly one correction (wrong/omitted named entity, wrong number or enumeration, dropped content the commentary marks essential, a locked term rendered inconsistently with its own established usage elsewhere in the file). A row is JUDGMENT-CALL if the "fix" requires picking between two defensible options the commentary doesn't itself adjudicate (e.g. two acceptable English names, a register preference). JUDGMENT-CALL rows are never edited — log them for the human.
5. **One verse, one targeted edit.** Match the exact existing line (text + `^verse-id`) before replacing it, the same way `extract_translation.py` parses it. If the line can't be matched exactly (file has drifted since the report was written), stop and flag that verse as skipped — do not guess which line it is.
6. **Never touch a verse the report didn't flag ⚠ for the requested scope**, even if something looks off while reading past it. Report it to the human instead; that's a new finding for `commentary-fact-check`, not this skill's job.
7. **Always re-verify after editing.** Once all applicable fixes in scope are applied, re-run `commentary-fact-check` for that same grade/scope before reporting success. A fix that doesn't clear the discrepancy on re-check is not done — log it and say so.
8. **Never set `status: complete` on anything.** This skill produces drafts for human review, same as its parent skill and `translation-qa`.
9. **Do not modify any file in `1-SOURCES/`.** Only `bca-en-<grade>.md`, the fixes log, and (via re-invoking `commentary-fact-check`) that grade's report file are ever written.
10. **Append, dated. Never overwrite** an earlier run's section in the fixes log.

---

## Procedure

### Step 1 — Load the report and select scope

Open `commentary-fact-check-report-<grade>.md`. Collect every ⚠ row within the
requested scope (or every unresolved ⚠ row in the whole file if scope was
omitted — cross-check against the fixes log's "Applied" tables from prior runs to
know what's already resolved). If there are zero ⚠ rows in scope, stop and tell
the user there is nothing to fix.

### Step 2 — Re-assemble grounding for each flagged verse

For each ⚠ verse: get the commentary passage (reuse cached
`/tmp/ks_commentary.json` from a prior `commentary-fact-check` run in this session
if present and still valid, otherwise regenerate it with
`4-SYSTEM/Skills/commentary-fact-check/scripts/extract_commentary.py`), and get
the current English line via
`4-SYSTEM/Skills/commentary-fact-check/scripts/extract_translation.py` scoped to
that verse's chapter.

### Step 3 — Triage: MECHANICAL vs JUDGMENT-CALL

Apply Rule 4 to every flagged verse. Write the triage decision down before editing
anything — this becomes the Applied/Skipped split in the fixes log.

### Step 4 — Apply MECHANICAL fixes

For each MECHANICAL verse, construct the corrected line (minimal edit per Rule 2)
and replace the exact existing `<text> ^<verse-id>` line in `bca-en-<grade>.md`
with it. Do this one verse at a time; do not batch-replace across the file with a
find-and-replace that could match unintended text (e.g. a name that also appears
correctly elsewhere).

### Step 5 — Write the fixes log

Create `commentary-fact-check-fixes-log-<grade>.md` if it doesn't exist yet (header
from the Output file format above). Append a new `## Run — <date> — <scope>`
section with the Applied table, the Skipped table, and a result line, per Rule 10.

### Step 6 — Re-verify

Invoke `commentary-fact-check` (read and follow
`4-SYSTEM/Skills/commentary-fact-check/SKILL.md`) for the same grade and scope.
This appends a fresh verdict subsection to `commentary-fact-check-report-<grade>.md`
per that skill's own re-check-replaces-subsection rule. Record the outcome (pass
count, any ⚠ that persisted) in this run's fixes-log entry under
"Re-verification."

### Step 7 — Report back

Tell the user: how many fixes were applied, how many were skipped as judgment
calls (list them briefly so the user can decide), and the re-verification result.
If any applied fix still shows ⚠ after re-check, say so plainly and do not claim
the discrepancy is resolved.

---

## Completion check

- [ ] Grade and scope established; report file confirmed to have ⚠ rows in scope.
- [ ] Every flagged verse triaged MECHANICAL or JUDGMENT-CALL before any edit was made.
- [ ] Only MECHANICAL verses edited; each edit minimal and grounded in the cited commentary passage.
- [ ] Each edit matched the exact existing line before replacing it; no guessed line matches.
- [ ] No verse outside the requested ⚠ scope was touched.
- [ ] Fixes log created/appended (never overwritten) with Applied + Skipped tables.
- [ ] `commentary-fact-check` re-run on the same grade/scope after edits; result recorded.
- [ ] No `status: complete` set anywhere; no file outside `bca-en-<grade>.md`, the fixes log, and that grade's report file was modified.
- [ ] User told: fixes applied, judgment calls skipped (with brief reasons), and the re-verification outcome.

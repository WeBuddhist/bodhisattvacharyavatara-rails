---
name: commentary-fact-check
description: >
  Fact-checks the English BCA translation (3-TRANSFORMATIONS/Translations/bo-en-translation/bca-en-<grade>.md)
  verse by verse against Khenpo Zhenga's Tibetan interlinear annotation commentary
  (1-SOURCES/Commentaries/Transcluded/BCAC19_KS_bo.md), one grade and one chapter (or
  range) at a time, and appends a verdict table to that grade's own running report
  file (one report per translation text — beginner, general, and advanced each get
  their own file, never mixed together). Use whenever the user asks to "fact-check
  the translation", "verify the translation against commentary", "check the English
  translation against BCAC19_KS_bo", "continue the commentary fact-check", or wants
  to confirm a translated verse says what the commentary actually explains. Also
  triggers for "does chapter N's translation match the commentary", "resume the
  fact-check", or "QA the translation with Khenpo Zhenga's commentary".
---

# commentary-fact-check

Confirms that an already-written English translation says what Khenpo Zhenga's
commentary says the verse means — not a retranslation, and not a rewrite. This
skill reports; it does not edit `bca-en-<grade>.md`. If a real discrepancy turns
up, flag it in the report and let the user or a follow-up editing pass fix the
translation file itself.

This is a companion to `translation-qa` (which scores against `2-RAILS/` rails and
`termbase.md`) but uses a different accuracy source: Khenpo Zhenga's word-level
annotation commentary is the ground truth here, because it exists, transcludes the
whole root text already, and settles doctrinal/factual content questions — sutra
citations, similes, named entities, classification schemes — that a bare verse line
often can't answer on its own.

---

## Inputs

| Input | Required | Description |
|---|---|---|
| **Grade** | ✓ | `beginner`, `general`, or `advanced` — which translation file to check. One grade per run; the three grades are checked separately because their wording differs even when the underlying content doesn't. |
| **Scope** | recommended | A chapter number (`1`, `2`, ... `10`), `colophon`, or an explicit verse range within a chapter (e.g. `2-1 to 2-10`). If omitted, read the report's progress table and continue from the next unchecked verse/chapter for that grade. A verse-range request always wins over the progress table — check exactly the verses named, even if some or all of that chapter was already checked (the user may be re-verifying, or the earlier run may not have persisted — see Step 5a). |

Fixed (not user-supplied):
- **Commentary source:** `1-SOURCES/Commentaries/Transcluded/BCAC19_KS_bo.md` — Khenpo Zhenga's (གཞན་ཕན་བྱམས་པའི་གོ་ཆ།) mchan-'grel, drawing on Patrul Rinpoche's oral tradition. It transcludes the entire root text (910/910 verses, ch.1–10, via `![[1-SOURCES/Translations/bo-བློ་ལྡན་ཤེས་རབ།.md#^verse-id]]` markers) and is already used elsewhere in this vault (`Verse-Context-Summary`) as the primary annotation layer.
- **Report file — one per grade, never shared:** `3-TRANSFORMATIONS/Translations/bo-en-translation/commentary-fact-check-report-<grade>.md`, i.e. `…-beginner.md`, `…-general.md`, `…-advanced.md`. Each file is self-contained and only ever documents its own translation text. Create a grade's file the first time that grade is actually checked — never create the other two grades' files as a side effect, and never merge two grades' results into one file.

**This skill uses `BCAC19_KS_bo.md` only.** Do not read, cite, cross-check against,
or mention any other commentary file in this workflow or in the report — not
`BCAC19_KKP_bo_segmented.md` (Khenpo Kunpal), not any other file under
`1-SOURCES/Commentaries/`. If a verse's meaning seems unclear or contested from
`BCAC19_KS_bo.md` alone, say so in the report as a note on that verse rather than
reaching for a second commentary — a multi-commentary check is a different,
separate skill, not this one.

---

## Procedure

### Step 1 — Extract the commentary passages

Run the bundled script once per session (cache the JSON; the commentary file doesn't change between runs):

```bash
python3 4-SYSTEM/Skills/commentary-fact-check/scripts/extract_commentary.py \
    1-SOURCES/Commentaries/Transcluded/BCAC19_KS_bo.md \
    --json /tmp/ks_commentary.json
```

This splits the file on its transclusion markers and attributes the Tibetan prose
between one marker and the next to that marker's verse ID — including any
block-quoted sutra citations, which are part of the commentary's own support for
its reading and worth checking against. Read the coverage summary it prints. If any
verse comes up with an empty passage, its content was absorbed into the *next*
verse's bucket (a splitting artifact when a heading or citation sits flush against
the marker) — read the following verse's passage to recover it; do not report this
as a translation defect.

**Watch for a cascading shift, not just an isolated empty bucket.** Chapter 3
turned up a bigger version of the same artifact: the commentary's prose for two
consecutive verses (3-2 and 3-3) was merged under a single marker, and because
nothing was left empty to flag it, every following bucket in the chapter quietly
explained the *next* verse instead of its own — bucket `^N` held the commentary
for root verse `N+1`, all the way to the chapter's last bucket. Nothing in the
coverage summary catches this (every bucket had content, so no empty-passage
warning fires); it only surfaces by actually reading the content and noticing it
describes a different verse than the one named. So when a bucket's content
doesn't obviously match its own verse, check the neighboring bucket before
concluding the translation is wrong — a real translation discrepancy and a
one-off commentary bucket shift look similar at first glance, but only one of
them means the English needs fixing. If a shift is confirmed, say so plainly in
the report (which buckets are affected, and that verdicts below have already
been corrected for it) rather than silently working around it — a future run
picking up the rest of the same chapter needs to know the correction still
applies.

### Step 2 — Extract the target translation

```bash
python3 4-SYSTEM/Skills/commentary-fact-check/scripts/extract_translation.py \
    3-TRANSFORMATIONS/Translations/bo-en-translation/bca-en-<grade>.md \
    --chapter <N> --json /tmp/<grade>_ch<N>.json
```

### Step 3 — Determine scope

Open that grade's own report file,
`3-TRANSFORMATIONS/Translations/bo-en-translation/commentary-fact-check-report-<grade>.md`
(create it from the template in Step 5 if it doesn't exist yet) and check its
progress table. If the user didn't name a chapter, pick the next one marked
pending. Tell the user which chapter you're about to check before starting, in
case they wanted a different one.

### Step 4 — Verse-by-verse comparison

For each verse in scope, read the Tibetan commentary passage and the English
line side by side and ask: **does the commentary's content — its similes, named
entities (sutras, teachers, doctrinal terms), enumerations, and logic — show up
accurately in the English, with nothing contradicted?**

This is a comprehension check, not a line-by-line retranslation. The commentary
routinely supplies more than the verse needs (etymologies, sub-classifications,
sutra citations, narrative illustrations) — none of that has to appear in the
translation. Only flag a verse when the translation says something the commentary
doesn't support, drops content the commentary marks as essential to the verse's
own sense (not just supplementary elaboration), or gets a named quantity, entity,
or sequence wrong.

Assign one of:
- **✓** — commentary confirms the translation; no discrepancy.
- **⚠** — discrepancy. State concisely what the translation says, what the
  commentary actually supports, and where (quote or closely paraphrase the
  relevant Tibetan clause).
- Group runs of adjacent verses that share one commentary passage (the source
  sometimes explains several verses — e.g. a shared list of similes — under one
  transclusion anchor) into a single row, as long as each verse's own content is
  separately confirmed.

Locked termbase epithets (e.g. `sugatas`/`victors`/`tathagatas` all rendered as
required by that grade's termbase) are worth a specific check, since these are
exactly the kind of thing that silently drifts across a long translation — but
this skill checks *content against commentary*, not term-consistency; leave
termbase consistency sweeps to a separate pass or to `translation-qa`.

### Step 5 — Append to the report

Each grade has its own file — `commentary-fact-check-report-<grade>.md` — and
that file only ever exists if that grade has actually been checked. Before
touching anything, make sure you're writing to the file for the grade you were
actually asked to check; never create or touch the other two grades' files in
the same run.

If that grade's report file doesn't exist yet, create it with just the header
and an empty progress table:

```markdown
# BCA English Translation — Commentary Fact-Check (BCAC19_KS_bo) — <grade>

Method: each verse's English rendering in `bca-en-<grade>.md` is checked
against Khenpo Zhenga's Tibetan interlinear commentary. This is a preliminary
self-check, not a scholarly sign-off — a domain specialist should review
before treating this grade as final, per this vault's standing rule that an
LLM never marks its own translation output complete.

## Progress

| Chapters checked |
|---|
```

Then append a new `### Chapter <N>` (or `### Colophon`) subsection with the verdict table:

```markdown
### Chapter <N> — <chapter title>

| Verse | Verdict | Note |
|---|---|---|
| <N>-1 | ✓ | ... |
| <N>-2 | ⚠ | translation says X; commentary supports Y ("..." — quote) |

**Result: <k>/<total> confirmed, <m> discrepancies.**
```

Update the Progress table (append the chapter number to the list, or replace
`—` with the range so far, e.g. `1–3`). Never overwrite an earlier chapter's
section — only append new sections and extend the progress row.

If the requested scope is a sub-range of a chapter (e.g. `2-1 to 2-10` out of
chapter 2's 65 verses), title the subsection `### Chapter <N> (verses <a>–<b> of
<total>)` so a later run covering the rest of the chapter appends its own
subsection rather than needing to rewrite this one. If a later request re-checks
a range that already has a section, treat it as a fresh check (re-derive the
verdicts, don't just copy the old table) and replace only that specific
subsection in place — do not leave two competing sections for the same range.

### Step 5a — Verify the write actually landed

Immediately after writing, re-read that grade's report file back (a fresh
read, not the in-memory version of the edit) and confirm the section you just
added is actually present with the content you expect. This vault's file mount
has shown intermittent write/sync glitches in this project before (edits that
succeeded in-tool but didn't appear when the file was reopened, or a file that
reverted to an earlier state between turns) — catch that here rather than
letting the user discover it later.

- If the re-read confirms the new section: proceed to Step 6.
- If the re-read shows the section missing, truncated, or an older version of the
  file (e.g. a KKP mention that was supposed to be removed, or a progress row
  that doesn't match): redo the write once. If it still doesn't stick, tell the
  user directly and plainly — "the report on disk doesn't match what I just
  wrote, this looks like a sync issue rather than a skill logic problem" — rather
  than silently reporting success. Suggest they check whether the file is open
  elsewhere (Obsidian, another editor) or has a sync conflict (OneDrive, git)
  that could be overwriting or reverting it.

### Step 6 — Report back

Tell the user, briefly: which chapter/grade was just checked, the pass count, and
the full text of any ⚠ rows (not just "see report") so they can act on real
discrepancies immediately without opening the file.

---

## Completion check

- [ ] Grade and scope (chapter or explicit range) established before starting.
- [ ] Commentary extracted via the bundled script; empty-passage artifacts (if any)
      resolved by reading the next verse's bucket, not reported as errors.
- [ ] Every verse in scope compared against its commentary passage individually.
- [ ] Verdicts assigned on content-accuracy grounds, not on translation style/wording.
- [ ] Report appended (never overwritten), in that grade's own file — `commentary-fact-check-report-<grade>.md`.
- [ ] No other grade's report file was created or touched in this run — not even an empty placeholder.
- [ ] Sub-range checks titled with their verse range so future runs can extend the chapter cleanly.
- [ ] The write was re-read and confirmed to actually be present on disk (Step 5a) before telling the user it's done.
- [ ] Any ⚠ surfaced directly to the user in chat, with the commentary citation.
- [ ] No file other than that grade's `commentary-fact-check-report-<grade>.md` was modified.

---
name: day-package-pipeline
description: Build one Bodhisattva-Challenge day-package end to end — assemble the Tibetan source-of-record file from the verse rails, plan day file, and schedule; translate it into the English package; then enforce the locked format (display-only commentator headings, His-Holiness-first order, per-section provenance) with the validator, conform, reorder, and drift-guard tools.
---

# day-package-pipeline

This skill produces a complete, format-locked **day-package** for a single day of the Bodhisattva Challenge, in one pass, across the two parallel deliverables the vault keeps: the **Tibetan source-of-record** file (`Day-Packages/…/<day>.md`) and its **English translation** (`Day-Packages-EN/…/<day>-en.md`). Correct output is a pair of files that (a) copy the verse-rail content verbatim (Tibetan) then render it into natural, termbase-consistent English, (b) carry the plan's Challenge sections and the day's verses, (c) place His Holiness the Dalai Lama's (`tenzin-gyatso`) commentary first, (d) use display-only commentator headings with the machine id in the anchor, and (e) pass `day_package_tools.py validate` with zero errors. The skill exists so that new days (and Chapter 2 onward) are built identically to Chapter 1 rather than drifting; it prevents the recurring failure of hand-built packages that reword rails, lose citations, mis-order commentators, or leak machine ids into reader-facing headings.

This is the end-to-end wrapper. The three phases can also be run alone; when only translating an already-built Tibetan file, start at Phase B.

---

## Inputs

Gather all of the following before starting. If any is missing or ambiguous, stop and ask the human contributor — never guess a verse range or invent rail content.

| Input | What it is | Path |
|---|---|---|
| Day number + chapter | Which day to build (e.g. Day 15, Chapter 2) | — |
| Schedule | Maps each day to its verse range and date | `3-TRANSFORMATIONS/Plans/the-bodhisattva-challenge/en/assets/schedule-hhdl-birthday.md` |
| Verse rails | Per-verse source content (root verse, interlinear gloss, per-commentator explanations, stories, metaphors, scriptural quotations, main teaching points, key terms, synthesis) | `2-RAILS/Verses/<verse-id>-summary.md` |
| Plan day file | The Challenge track: Notification, Opening, From the Tradition, Today's Practice | `3-TRANSFORMATIONS/Plans/the-bodhisattva-challenge/en/Days/Chapter-<N> D<a>-D<b>/<day>.md` |
| Plain-English verses | Reader-facing verse text, addressed by block id (`^1-1` …) | `3-TRANSFORMATIONS/Translations/en-translate/BCA-Full-Plain-English.md` |
| Format contract | The locked template every output must match | `3-TRANSFORMATIONS/Plans/the-bodhisattva-challenge/en/Day-Packages/_TEMPLATE.md` |
| Termbase | Fixed Buddhist-term renderings + the commentator id → display-name table | `3-TRANSFORMATIONS/Plans/the-bodhisattva-challenge/en/Day-Packages/_TERMBASE.md` |
| Tooling | Validator/conform/guard and the reorder script | `4-SYSTEM/scripts/day-package/day_package_tools.py`, `…/reorder_commentators.py` |

## Output

Two files, one per language, in the two parallel folders (create the `Chapter-<N> D<a>-D<b>` folder if it does not exist):

- Tibetan source-of-record: `3-TRANSFORMATIONS/Plans/the-bodhisattva-challenge/en/Day-Packages/Chapter-<N> D<a>-D<b>/<day>.md`
- English translation: `3-TRANSFORMATIONS/Plans/the-bodhisattva-challenge/en/Day-Packages-EN/Chapter-<N> D<a>-D<b>/<day>-en.md`

Both are **protected source-of-truth files**: they carry the `protected: true` frontmatter, the `🔒 PROTECTED` banner, and are tracked by the drift-guard. After writing, re-baseline the guard (Phase C).

---

## Output file format

The canonical shape is `_TEMPLATE.md`; read it in full before writing. Condensed skeleton (English package shown — the Tibetan file is identical in structure, with rail prose in Tibetan/Sanskrit and Tibetan display names):

```markdown
---
day: <N>
chapter: <C>
verses: "<c>-<a> to <c>-<b>"     # or a single "<c>-<n>"
date: "<Mon D>"
status: draft
language: en                      # "bo" is not used; Tibetan file omits document_type/translated_from
document_type: english-translation
translated_from: "…/Day-Packages/Chapter-<N> …/<day>.md"
sources:
  plan_day_file: "…/en/Days/Chapter-<N> …/<day>.md"
  schedule_file: "…/assets/schedule-hhdl-birthday.md"
  verse_source: "3-TRANSFORMATIONS/Translations/en-translate/BCA-Full-Plain-English.md"
  rail_files:
    - "2-RAILS/Verses/<c>-<a>-summary.md"
protected: true
edit_policy: "confirm-with-human-before-edit-move-delete"
---

> 🔒 **PROTECTED — SOURCE OF TRUTH.** … (banner, verbatim from an existing package)

# Day <N> — <title>

**Date:** <date>  
**Chapter:** <c>  
**Verses covered:** <range>

---

<!-- sec:challenge -->
## 1. Today's Challenge (from the practice-plan track)

<!-- challenge:notification -->
### Notification
<!-- challenge:opening -->
### Opening
<!-- challenge:tradition -->
### From the Tradition
<!-- challenge:practice -->
### Today's Practice

---

<!-- sec:verses -->
## 2. Today's Verses
<one blockquote per verse; text from BCA-Full-Plain-English by block id>

---

<!-- sec:rails -->
## 3. Verse Rails (from 2-RAILS/Verses — English translation)

<!-- verse:<c>-<a> -->
### Verse <c>-<a>

<!-- sub:root-verse -->
#### Root Verse
<!-- sub:interlinear -->
#### Interlinear Gloss (Khenpo Zhenga's annotation commentary)
<!-- sub:commentary -->
#### Commentary Explanations
<!-- cm:tenzin-gyatso -->
##### His Holiness the Dalai Lama (Teaching on Entering the Bodhisattva's Way of Life)
<!-- cm:kunpal -->
##### Khenpo Kunzang Pelden (Nectar Drops)
<!-- sub:stories -->
#### Stories and Illustrations              (optional)
<!-- story:<ID> -->
##### <Title>
<!-- sub:metaphors -->
#### Metaphors and Examples                 (optional)
<!-- sub:quotations -->
#### Scriptural Quotations                  (optional)
<!-- sub:teaching-points -->
#### Main Teaching Points
<!-- sub:key-terms -->
#### Key Terms
<!-- sub:synthesis -->
#### Verse Synthesis (overview)

Sources: [[1-SOURCES/…]]      # one consolidated line per leaf section that has sources
```

Key format invariants (full list in `_TEMPLATE.md`):
- Every tracked heading is immediately preceded by its `<!-- … -->` anchor (no blank line between).
- **Commentator/story H5 headings are display-only** — name + work, or story title. The machine id lives *only* in the `<!-- cm:<id> -->` / `<!-- story:<id> -->` anchor above. Never write `##### tenzin-gyatso — …`.
- **His Holiness the Dalai Lama (`tenzin-gyatso`) comes first** in every Commentary Explanations section; other commentators follow in source order.
- Provenance is one `Sources: [[…]] [[…]]` line per leaf section; **no** inline `([[…]])` in prose, **no** `![[…]]` transclusions. The Key Terms table keeps its own `Source` column.
- The `### Verse <id>` blocks must exactly cover the `verses:` range in the frontmatter.

---

## Rules

1. **Never reword the rails when building the Tibetan file.** Phase A copies rail content verbatim (structure, prose, citations). Interpretation or paraphrase in the Tibetan source-of-record corrupts the ground truth.
2. **Translate, never transliterate meaning away, in Phase B.** The five translation constraints are mandatory: (a) not a literal word-for-word rendering — keep the cultural context; (b) Buddhist terminology consistent with `_TERMBASE.md` throughout; (c) no needlessly hard words and no unnecessary idioms; (d) natural, non-awkward English; (e) humanised, readable prose. Do not add doctrine that is not in the rail.
3. **Terminology comes from `_TERMBASE.md`.** Use the listed renderings verbatim (e.g. `tenzin-gyatso → His Holiness the Dalai Lama (Teaching on Entering the Bodhisattva's Way of Life)`). If a needed term is absent from the termbase, stop and ask; do not coin a new rendering silently.
4. **The machine id never appears in a reader-facing heading or in prose.** Commentator ids (`tenzin-gyatso`, `kunpal`, …) live in anchors only. If the raw slug appears in a synthesis bullet, key-terms cell, or story label, replace it with the display name.
5. **His Holiness first, always.** After writing, run `reorder_commentators.py` to guarantee the order even if the draft placed him elsewhere.
6. **Do not edit `1-SOURCES/`.** Rails and plan files are read-only inputs. This skill writes only to the two Day-Packages folders (and re-baselines the guard).
7. **A day is not done until `validate` passes with zero errors** and the drift-guard has been re-recorded.
8. **Both files are protected.** Preserve the `🔒 PROTECTED` banner and `protected: true` / `edit_policy:` frontmatter on both.

---

## Procedure

### Phase A — Build the Tibetan source-of-record `<day>.md`

1. In `schedule-hhdl-birthday.md`, look up the day's **verse range** and **date**. Derive the chapter and the `Chapter-<N> D<a>-D<b>` folder name.
2. Create the output folders if absent under both `Day-Packages/` and `Day-Packages-EN/`.
3. Read each verse's rail at `2-RAILS/Verses/<verse-id>-summary.md`. For each verse, **copy verbatim** into the Verse Rails section: Root Verse, Interlinear Gloss, Commentary Explanations (one H5 per commentator), Stories, Metaphors, Scriptural Quotations, Main Teaching Points, Key Terms, Verse Synthesis. Keep the rails' Tibetan/Sanskrit prose and their citations.
4. Read the plan day file under `en/Days/…/<day>.md` and copy its Notification, Opening, From the Tradition, and Today's Practice into Section 1 (Today's Challenge). End that section with a `*(Source: …/Days/…/<day>.md)*` line.
5. Fill Section 2 (Today's Verses) and each verse's Root Verse from `BCA-Full-Plain-English.md` by block id.
6. Add the frontmatter, the `🔒 PROTECTED` banner, and the `# Day <N> — <title>` header (copy the banner text verbatim from an existing package).
7. Insert `<!-- cm:<id> -->` anchors above each commentator H5, and rewrite each commentator H5 to display-only (`##### <Name> (<Work>)`); do the same for story H5s (`<!-- story:<id> -->` + title).

### Phase B — Translate into the English package `<day>-en.md`

8. Copy the Tibetan file's structure to the English path. Set `document_type: english-translation`, `translated_from:` and the `translation_note:` (see an existing `-en.md` for the exact note).
9. Render every rail block into English under Rule 2 and the termbase (Rule 3). Where a term-to-term mapping matters (Key Terms rows, metaphor labels), keep the original Tibetan in parentheses.
10. Pull Section 2 and each Root Verse verbatim from `BCA-Full-Plain-English.md` (do not translate these — they are already English).
11. Keep commentator/story headings display-only; keep the `cm:`/`story:` anchors from Phase A.

### Phase C — Enforce the format

12. Reorder commentators so His Holiness is first:
    `python3 4-SYSTEM/scripts/day-package/reorder_commentators.py "<tibetan.md>" "<english-en.md>"`
13. Conform (inserts/normalises anchors, consolidates citations into one `Sources:` line per section; idempotent):
    `python3 4-SYSTEM/scripts/day-package/day_package_tools.py conform "<english-en.md>"`
14. Validate — must print `[PASS]` with zero `ERROR:` lines:
    `python3 4-SYSTEM/scripts/day-package/day_package_tools.py validate "<english-en.md>"`
    Fix every reported error and re-run until it passes.
15. Re-baseline the drift-guard (the two new files are protected):
    `python3 4-SYSTEM/scripts/day-package/day_package_tools.py guard record`
    then `guard check` to confirm `OK`.

---

## Completion check

- [ ] Both files exist at the two parallel paths, with matching `Chapter-<N> D<a>-D<b>` folder and `<day>` / `<day>-en` names.
- [ ] Verse coverage in each file exactly matches the schedule's range for that day (no missing or extra `### Verse` blocks).
- [ ] Tibetan file's rail content is a verbatim copy of the source rails (no rewording); English file is a natural, termbase-consistent translation honouring the five constraints.
- [ ] Every Commentary Explanations section lists His Holiness the Dalai Lama (`tenzin-gyatso`) first.
- [ ] All commentator/story H5 headings are display-only; no machine id (`tenzin-gyatso`, `kunpal`, …) appears in any heading or in prose.
- [ ] Provenance is one `Sources:` line per leaf section; no inline `([[…]])`, no `![[…]]`.
- [ ] Both files carry the `🔒 PROTECTED` banner and `protected: true` / `edit_policy:` frontmatter.
- [ ] `day_package_tools.py validate` prints `[PASS]` with zero errors for the English file.
- [ ] `guard record` then `guard check` reports OK with the two new files included.

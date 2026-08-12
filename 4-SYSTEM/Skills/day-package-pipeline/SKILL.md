---
name: day-package-pipeline
description: Build one Bodhisattva-Challenge day-package end to end — assemble the Tibetan source-of-record file from the verse rails, plan day file, and schedule; translate it into the English package; then enforce the locked format (display-only commentator headings, His-Holiness-first order, per-section provenance) with the validator, conform, reorder, and drift-guard tools.
---

# day-package-pipeline

This skill produces a complete, format-locked **day-package** for a single day of the Bodhisattva Challenge, in one pass, across the two parallel deliverables the vault keeps: the **Tibetan source-of-record** file (`Day-Packages/bo/…/<day>.md`) and its **English translation** (`Day-Packages/en/…/<day>-en.md`). Correct output is a pair of files that (a) copy the verse-rail content verbatim (Tibetan) then render it into natural, termbase-consistent English, (b) carry the plan's Challenge sections and the day's verses, (c) place His Holiness the Dalai Lama's (`tenzin-gyatso`) commentary first, (d) use display-only commentator headings with the machine id in the anchor, and (e) pass `day_package_tools.py validate` with zero errors. The skill exists so that new days (and Chapter 2 onward) are built identically to Chapter 1 rather than drifting; it prevents the recurring failure of hand-built packages that reword rails, lose citations, mis-order commentators, or leak machine ids into reader-facing headings.

This is the end-to-end wrapper. The three phases can also be run alone; when only translating an already-built Tibetan file, start at Phase B.

---

## Inputs

Gather all of the following before starting. If any is missing or ambiguous, stop and ask the human contributor — never guess a verse range or invent rail content.

| Input | What it is | Path |
|---|---|---|
| Day number + chapter | Which day to build (e.g. Day 15, Chapter 2) | — |
| Schedule | Maps each day to its verse range and date | `3-TRANSFORMATIONS/Plans/the-bodhisattva-challenge/en/assets/schedule-hhdl-birthday.md` |
| Verse rails | Per-verse source content (root verse, interlinear gloss, per-commentator explanations, stories, metaphors, scriptural quotations, main teaching points, key terms, synthesis) | `2-RAILS/Verses/<verse-id>-summary.md` |
| Plan day file (Section 1) | The Challenge track. **Source differs by chapter, and by language for Ch 2+** — see the note below. | Ch 1: `…/en/Days/Chapter-1 D1-D14/<day>.md` · Ch 2+ Tibetan: `3-TRANSFORMATIONS/Plans/Dalai Lama/Chapter-<N> …/Day-<day>-Ch<c>-V<a>-<b>.md` · Ch 2+ English: `3-TRANSFORMATIONS/Plans/the-bodhisattva-challenge/en/Days/Chapter-<N> D<a>-D<b>/<day>-ch<c>-v<range>-eng.md` — a top-level file only; if absent, stop and ask (never substitute `Archive/`, `Drafts and Options/`, or the Dalai Lama file's English block) |
| Plain-English verses | Reader-facing verse text, addressed by block id (`^1-1`, `^2-1` …) | `3-TRANSFORMATIONS/Translations/en-translate/BCA-Full-Plain-English.md` |
| Format contract | The locked template every output must match | `3-TRANSFORMATIONS/Day-Packages/bo/_TEMPLATE.md` |
| Termbase | Fixed Buddhist-term renderings + the commentator id → display-name table | `3-TRANSFORMATIONS/Day-Packages/bo/_TERMBASE.md` |
| Tooling | Validator/conform/guard and the reorder script | `4-SYSTEM/scripts/day-package/day_package_tools.py`, `…/reorder_commentators.py` |

**Section 1 source, by chapter (this is the part that changes most between chapters):**

- **Chapter 1** used `…/en/Days/Chapter-1 D1-D14/<day>.md` and had four sub-blocks: **Notification, Opening, From the Tradition, Today's Practice**.
- **Chapter 2 onward, Tibetan package:** always sourced from the **Dalai Lama** plan file `3-TRANSFORMATIONS/Plans/Dalai Lama/Chapter-<N> D<first>-D<last>/Day-<day>-Ch<c>-V<a>-<b>.md`. That file holds Tibetan, Hindi, and an `# English (Easy Plain English)` block. **There is no Notification.** Map its Tibetan parts to the package's challenge sub-blocks:
  - **Opening** ← "Introduction to Today's Practice" (Tibetan `ངོ་སྤྲོད།`)
  - **From the Tradition** ← "Commentary & Story Explanation" (Tibetan `འགྲེལ་བཤད།`)
  - **Today's Practice** ← "Today's Practice" — its **Challenge** line becomes `**Practice:**`, its **Explanation** stays `**Explanation:**` (Tibetan `དེ་རིང་གི་ཉམས་ལེན།` → `ཉམས་ལེན་དངོས།` + `འགྲེལ་བཤད།`)
  - Ignore the `# ...སྐྱབས་འགྲོ་སེམས་བསྐྱེད།` (refuge/bodhicitta liturgy) and `བསྔོ་བ་དང་སྨོན་ལམ།` (dedication) sections — they are not part of the day-package.
- **Chapter 2 onward, English package:** prefer the curated English day file at `3-TRANSFORMATIONS/Plans/the-bodhisattva-challenge/en/Days/Chapter-<N> D<first>-D<last>/<day>-ch<c>-v<range>-eng.md` — a top-level file in that folder (never a file under its `Archive/` or `Drafts and Options/` subfolders; those are not valid Section 1 sources). It uses its own numbered headings, mapped as:
  - **Opening** ← `## 1) Introduction to Today's Practice`
  - **From the Tradition** ← `## 2) Commentary Explanation`
  - **Today's Practice** ← `## 3) Today's Practice` — its **Challenge**/**Actual Practice**/**The Practice** line becomes `**Practice:**`, its **Explanation** stays `**Explanation:**`
  - If no top-level file exists for that day in the `Days/Chapter-<N> …` folder, **stop and ask the human contributor** whether to (a) leave Section 1 as the empty placeholder (`*(The practice-plan challenge track is intentionally omitted from this package...)*`) or (b) source it from somewhere else. **Never silently fall back to the `Dalai Lama` file's English block or to `Archive`/`Drafts and Options` — a prior attempt to do so was explicitly rejected by the human contributor.**
  - The `*(Source: …)*` line at the end of Section 1 must point to the actual file used (the curated `Days/…/<day>-ch<c>-v<range>-eng.md` file when present).

## Output

Two files, one per language, in the two parallel folders (create the `Chapter-<N> D<a>-D<b>` folder if it does not exist):

- Tibetan source-of-record: `3-TRANSFORMATIONS/Day-Packages/bo/Chapter-<N> D<a>-D<b>/<day>.md`
- English translation: `3-TRANSFORMATIONS/Day-Packages/en/Chapter-<N> D<a>-D<b>/<day>-en.md`

Both are **protected source-of-truth files**: they carry the `protected: true` frontmatter, the `🔒 PROTECTED` banner, and are tracked by the drift-guard. After writing, re-baseline the guard (Phase C).

---

## Output file format

The canonical shape is `_TEMPLATE.md`; read it in full before writing. Condensed skeleton (English package shown — the Tibetan file is identical in structure, with rail prose in Tibetan/Sanskrit and Tibetan display names):

File naming uses the **absolute day number** (Chapter 2 starts at Day 15, so `15.md` / `15-en.md`, not `1.md`) — matching the schedule and the `Day-<n>-…` plan files. The folder is `Chapter-<N> D<first>-D<last>` (with the space), e.g. `Chapter-2 D15-D40`.

```markdown
---
day: <N>                          # absolute day number (e.g. 15), not chapter-relative
chapter: <C>
verses: "<c>-<a> to <c>-<b>"     # or a single "<c>-<n>"
date: "<Mon D>"
status: draft
language: en                      # "bo" is not used; Tibetan file omits document_type/translated_from
document_type: english-translation
translated_from: "…/Day-Packages/bo/Chapter-<N> …/<day>.md"
sources:
  plan_day_file: "…/en/Days/Chapter-1 …/<day>.md"   # Ch 1; for Ch 2+ English package point to the curated Days/Chapter-<N> …/<day>-ch<c>-v<range>-eng.md file (Tibetan package still points to the Dalai Lama plan file)
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

<!-- challenge:notification -->            # Chapter 1 only — OMIT for Chapter 2+
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
**Brief introduction.** <one-paragraph overview>
**Key points.**
- <condensed recap bullets — mirror the Main Teaching Points>

Sources: [[1-SOURCES/…]]      # one consolidated line per leaf section that has sources
```

Key format invariants (full list in `_TEMPLATE.md`):
- Every tracked heading is immediately preceded by its `<!-- … -->` anchor (no blank line between).
- **Commentator/story H5 headings are display-only** — name + work, or story title. The machine id lives *only* in the `<!-- cm:<id> -->` / `<!-- story:<id> -->` anchor above. Never write `##### tenzin-gyatso — …`.
- **His Holiness the Dalai Lama (`tenzin-gyatso`) comes first** in every Commentary Explanations section; other commentators follow in source order. **Not every verse has an HHDL block** (e.g. verses 2-2, 2-3 do not); reorder simply leaves such a section as-is.
- The **commentator count varies per verse** (Chapter 1 verses often have 8; 2-2/2-3 have 7). Include exactly the commentators the rail has — do not invent a missing one.
- Optional sub-sections (**Stories**, **Metaphors**, **Scriptural Quotations**) appear only when the rail has them. Some verses have none; that is valid.
- A **Divergences** H5, if present, must have a heading that **starts with the word "Divergences"** (a leading `⚑` is allowed, e.g. `##### ⚑ Divergences (where the commentaries differ)`) and the anchor `<!-- div:divergences -->`. If the heading does not start with "Divergences", the validator treats it as a commentator block and errors. Two Divergences blocks in one file (one per verse) is fine.
- **Story ids may be placeholders** (e.g. `BCACXX_WR`) and may repeat across two stories in the same verse; keep them as the rail has them — duplicate `story:` anchors pass validation.
- Provenance is one `Sources: [[…]] [[…]]` line per leaf section; **no** inline `([[…]])` in prose, **no** `![[…]]` transclusions. The Key Terms table keeps its own `Source` column.
- **Verse Synthesis has two labelled parts, worded exactly** `**Brief introduction.**` (a one-paragraph overview) then `**Key points.**` (a bulleted recap that mirrors the Main Teaching Points). Use these exact labels — do **not** write "Overview" or "Main points", which collide with the separate Main Teaching Points section and can throw off the reader/AI-overview view. This bulleted recap belongs to the synthesis by design; it is not a duplication error.
- The `### Verse <id>` blocks must exactly cover the `verses:` range in the frontmatter.

---

## Rules

1. **Never reword the rails when building the Tibetan file.** Phase A copies rail content verbatim (structure, prose, citations). Interpretation or paraphrase in the Tibetan source-of-record corrupts the ground truth.
2. **Translate, never transliterate meaning away, in Phase B.** The five translation constraints are mandatory: (a) not a literal word-for-word rendering — keep the cultural context; (b) Buddhist terminology consistent with `_TERMBASE.md` throughout; (c) no needlessly hard words and no unnecessary idioms; (d) natural, non-awkward English; (e) humanised, readable prose. Do not add doctrine that is not in the rail.
3. **Terminology comes from `_TERMBASE.md`.** Use the listed renderings verbatim (e.g. `tenzin-gyatso → His Holiness the Dalai Lama (Teaching on Entering the Bodhisattva's Way of Life)`). If a needed term is absent from the termbase, stop and ask; do not coin a new rendering silently.
4. **The machine id never appears in a reader-facing heading or in prose.** Commentator ids (`tenzin-gyatso`, `kunpal`, …) live in anchors only. If the raw slug appears in a synthesis bullet, key-terms cell, or story label, replace it with the display name.
5. **His Holiness first when present.** After writing, run `reorder_commentators.py` to guarantee the order even if the draft placed him elsewhere. Verses with no `tenzin-gyatso` block are left as they are.
6. **Do not edit `1-SOURCES/`.** Rails and plan files are read-only inputs. This skill writes only to the two Day-Packages/bo folders (and re-baselines the guard).
7. **A day is not done until `validate` passes with zero errors** and the drift-guard has been re-recorded.
8. **Both files are protected.** Preserve the `🔒 PROTECTED` banner and `protected: true` / `edit_policy:` frontmatter on both.
9. **Section 1 source and language.** Take Section 1 from the correct plan file for the chapter (see Inputs). **Omit Notification for Chapter 2+.** The English package's Section 1 uses the plan's English text; the Tibetan package's Section 1 uses the plan's Tibetan text. The `*(Source: …)*` line at the end of Section 1 points to the plan file actually used.
10. **Use the absolute day number** for the file name, `day:` frontmatter, and folder range — never a chapter-relative number.

---

## Procedure

### Phase A — Build the Tibetan source-of-record `<day>.md`

1. In `schedule-hhdl-birthday.md`, look up the day's **verse range** and **date**. Derive the chapter and the `Chapter-<N> D<a>-D<b>` folder name.
2. Create the output folders if absent under both `Day-Packages/bo/` and `Day-Packages/en/`.
3. Read each verse's rail at `2-RAILS/Verses/<verse-id>-summary.md`. For each verse, **copy verbatim** into the Verse Rails section: Root Verse, Interlinear Gloss, Commentary Explanations (one H5 per commentator), Stories, Metaphors, Scriptural Quotations, Main Teaching Points, Key Terms, Verse Synthesis. Keep the rails' Tibetan/Sanskrit prose and their citations.
4. Build Section 1 (Today's Challenge) from the chapter's plan file (see Inputs → "Section 1 source, by chapter"). For **Chapter 1**, copy Notification, Opening, From the Tradition, Today's Practice. For **Chapter 2+**, take the Dalai Lama plan file's **Tibetan** sections into the Tibetan package — Opening ← `ངོ་སྤྲོད།`, From the Tradition ← `འགྲེལ་བཤད།`, Today's Practice ← `དེ་རིང་གི་ཉམས་ལེན།` — and **omit Notification**. End the section with a `*(Source: <plan file>)*` line pointing to the file used.
5. Fill Section 2 (Today's Verses) and each verse's Root Verse from `BCA-Full-Plain-English.md` by block id.
6. Add the frontmatter, the `🔒 PROTECTED` banner, and the `# Day <N> — <title>` header (copy the banner text verbatim from an existing package).
7. Insert `<!-- cm:<id> -->` anchors above each commentator H5, and rewrite each commentator H5 to display-only (`##### <Name> (<Work>)`); do the same for story H5s (`<!-- story:<id> -->` + title).

### Phase B — Translate into the English package `<day>-en.md`

8. Copy the Tibetan file's structure to the English path. Set `document_type: english-translation`, `translated_from:` and the `translation_note:` (see an existing `-en.md` for the exact note). For Section 1: Chapter 1 uses the Chapter-1 plan file's English text as before. **Chapter 2+ uses the curated English day file** `3-TRANSFORMATIONS/Plans/the-bodhisattva-challenge/en/Days/Chapter-<N> D<a>-D<b>/<day>-ch<c>-v<range>-eng.md` (top-level only — never `Archive/` or `Drafts and Options/`), mapping `## 1) Introduction to Today's Practice` → Opening, `## 2) Commentary Explanation` → From the Tradition, and `## 3) Today's Practice` → Today's Practice (its Challenge/Actual-Practice line becomes `**Practice:**`). Set `sources.plan_day_file` to this file's path and cite it in the `*(Source: …)*` line. If no such file exists for the day, **stop and ask the human contributor** — do not fall back to the Dalai Lama file's English block or to `Archive`/`Drafts and Options`, and do not invent content.
9. Render every rail block into English under Rule 2 and the termbase (Rule 3). Where a term-to-term mapping matters (Key Terms rows, metaphor labels), keep the original Tibetan in parentheses.
10. Pull Section 2 and each Root Verse verbatim from `BCA-Full-Plain-English.md` (do not translate these — they are already English).
11. Keep commentator/story headings display-only; keep the `cm:`/`story:` anchors from Phase A. Make any `Divergences` H5 heading start with the word "Divergences" (see the format invariants).

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
    then `guard check` to confirm `OK`. `guard.paths` uses chapter-agnostic globs (`Day-Packages/en/*/*.md`, `Day-Packages/bo/*/[0-9]*.md`), so a new chapter's files are picked up automatically — no need to edit it.

---

## Completion check

- [ ] Both files exist at the two parallel paths, named with the **absolute day number**, in the `Chapter-<N> D<first>-D<last>` folder.
- [ ] Section 1 comes from the correct plan file for the chapter; **Notification is present only for Chapter 1** (omitted for Chapter 2+); the English package's Section 1 is in English and the Tibetan package's in Tibetan; the `*(Source: …)*` line names the plan file used.
- [ ] Verse coverage in each file exactly matches the schedule's range for that day (no missing or extra `### Verse` blocks); each verse includes exactly the commentators its rail has.
- [ ] Tibetan file's rail content is a verbatim copy of the source rails (no rewording); English file is a natural, termbase-consistent translation honouring the five constraints.
- [ ] Every Commentary Explanations section lists His Holiness the Dalai Lama (`tenzin-gyatso`) first.
- [ ] All commentator/story H5 headings are display-only; no machine id (`tenzin-gyatso`, `kunpal`, …) appears in any heading or in prose.
- [ ] Provenance is one `Sources:` line per leaf section; no inline `([[…]])`, no `![[…]]`.
- [ ] Both files carry the `🔒 PROTECTED` banner and `protected: true` / `edit_policy:` frontmatter.
- [ ] `day_package_tools.py validate` prints `[PASS]` with zero errors for the English file.
- [ ] `guard record` then `guard check` reports OK with the two new files included.

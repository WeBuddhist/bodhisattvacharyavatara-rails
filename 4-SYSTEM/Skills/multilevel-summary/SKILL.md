---
name: multilevel-summary
description: Generate an audience-targeted summary of a verse or chapter of the Bodhisattvacaryāvatāra by extracting meanings from the traditional commentary tradition and calibrating language, length, and fidelity to the specified audience.
---

# multilevel-summary

This skill produces a summary of a verse or a full chapter, grounded exclusively in the traditional commentaries preserved in `1-SOURCES/Commentaries/`. The summary is calibrated to one of three audiences — kids, general, or academic — each with its own priority ranking for fidelity, language register, and length. The output is saved to `3-TRANSFORMATIONS/Adaptations/multilevel-summaries/` and ends with Obsidian segment-links pointing back to the specific commentary blocks used.

The skill prevents free-floating paraphrase: every claim in the summary must be traceable to a commentary block. Nothing is added from parametric knowledge.

---

## Inputs

| Field | Description | Example |
|---|---|---|
| `scope-type` | `verse` or `chapter` | `verse` |
| `scope-id` | Verse ID (`chapter-verse`) or chapter number/name | `1-1` or `1` or `བྱང་ཆུབ་སེམས་ཀྱི་ཕན་ཡོན།` |
| `audience` | `kids`, `general`, or `academic` | `general` |

If the chapter is given by name rather than number, resolve the number from the chapter heading in `1-SOURCES/Translations/bo-བློ་ལྡན་ཤེས་རབ།.md` before proceeding.

If any required input is missing, ask the human before starting — do not assume.

---

## Output

**Verse scope:**
```
3-TRANSFORMATIONS/Adaptations/multilevel-summaries/<audience>/verse-<chapter-verse>.md
```

**Chapter scope:**
```
3-TRANSFORMATIONS/Adaptations/multilevel-summaries/<audience>/chapter-<N>.md
```

If the file already exists, read it first and update in place, preserving any manual refinements.

---

## Output file format

```markdown
---
scope: verse | chapter
scope_id: <e.g. 1-1 or 1>
audience: kids | general | academic
commentaries_used:
  - <registered_id>
  - <registered_id>
status: draft
---

# [Verse N-M / Chapter N] — <audience> Summary

## Root Text

![[1-SOURCES/Translations/bo-བློ་ལྡན་ཤེས་རབ།.md#^<verse-id>]]

*(For chapter scope: transclude the chapter heading block and the first verse only, then note the full verse range covered.)*

## Summary

<The summary text, calibrated to the audience priorities below.>

---

## Sources

<List of Obsidian block-links to every commentary passage used, one per line, in the format:>

- [[1-SOURCES/Commentaries/<commentary-file>.md#^<block-id>]] (<registered_id>)
```

---

## Audience priority rules

Write the summary according to the priority weights for the specified audience. Higher priority = more weight in every trade-off decision.

### kids (6th-grade level)

| Priority | Criterion |
|---|---|
| 5 | Easy language with illustration — use concrete images, analogies, and simple vocabulary a 6th-grader knows. Where the commentary itself uses an analogy or story, reproduce it. Where it does not, you may add a short illustrative image *only if* it does not introduce meaning not in the commentaries. |
| 4 | Not long — aim for 100–150 words. Cut anything the commentary treats as secondary. |
| 3 | Truth to the commentaries — all content must be traceable to a commentary block. |

### general (educated adult, no prior Buddhist study)

| Priority | Criterion |
|---|---|
| 5 | Truth to the commentaries — every claim must trace to a commentary block. No interpretive liberties. |
| 3 | Not too long — aim for 150–250 words. Include the main point of each major commentary but do not elaborate every sub-division. |
| 2 | Easy language — prefer plain English or clear modern prose over technical terminology. Translate technical Tibetan/Sanskrit terms on first use. |

### academic (scholar or advanced student)

| Priority | Criterion |
|---|---|
| 5 | Truth to the commentaries — cite specific commentators by registered ID for each claim. Note divergences. |
| 4 | Classical language — use established Dharma terminology (Tibetan/Sanskrit terms in IAST/Wylie with English gloss in parentheses on first use). Match the register of scholarly Buddhist studies writing. |
| 3 | Not too long — aim for 200–350 words. Be comprehensive but not exhaustive; refer to the source blocks for full elaboration. |

---

## Rules

1. **Root text source is `bo-བློ་ལྡན་ཤེས་རབ།`** — the Tibetan Kangyur translation at `1-SOURCES/Translations/bo-བློ་ལྡན་ཤེས་རབ།.md`. Transclude from this file. Do not use the Sanskrit root text as the primary verse source.
2. **Commentary passages are found via transclusion markers** — scan each commentary file for `![[1-SOURCES/Translations/bo-བློ་ལྡན་ཤེས་རབ།.md#^<verse-id>]]`. The explanation blocks immediately follow this marker, up to the next transclusion marker or section heading.
3. **Summary content comes only from commentary blocks** — no parametric Buddhist knowledge. If no commentary discusses a verse, state that explicitly in the summary and leave the Sources list empty for that verse.
4. **All source links go in the Sources section** — use Obsidian block-links (`[[...#^block-id]]`). Do not inline citations in the summary text itself (keep it readable for the audience).
5. **For chapter scope, cover the chapter in aggregate** — do not produce a verse-by-verse list. Synthesise the overarching theme and key teachings the commentaries draw out across the chapter. You may group verses thematically if the commentaries suggest that structure.
6. **Divergences are noted at academic level; simplified or omitted at general level; omitted at kids level** — at academic level mark divergences with ⚑ and name the commentators on each side.
7. **Do not mark `status: complete`** — only a human contributor sets that field. Always write `status: draft`.
8. **Illustrations (kids only)** — a short bracketed note `[Illustration idea: ...]` may follow the summary if an image would help a child picture the teaching, but only when the commentary itself suggests a concrete image or the teaching has an obvious visual correlate. Never invent doctrine to make an illustration work.

---

## Procedure

### For verse scope

1. Read `1-SOURCES/Translations/bo-བློ་ལྡན་ཤེས་རབ།.md` and locate the block `^<chapter-verse>`. Record the verse text.
2. For each commentary file in `1-SOURCES/Commentaries/` (skip the `dup/` subfolder):
   a. Search for the transclusion marker `![[1-SOURCES/Translations/bo-བློ་ལྡན་ཤེས་རབ།.md#^<chapter-verse>]]`.
   b. If found, collect all block IDs that follow this marker up to the next transclusion marker (`![[...#^...]]`) or the next heading (`##` or `###`). These are the commentary's explanation blocks for this verse.
   c. Record the commentary's `registered_id` (from its frontmatter) and all collected block IDs.
3. If no commentary addresses the verse, write a summary noting this and stop. Set `status: draft`.
4. Read the collected commentary blocks in full.
5. Draft the **Summary** section according to the audience priority rules for the specified audience.
6. Draft the **Sources** section: one Obsidian block-link per collected block, labelled with the `registered_id`.
7. Fill the YAML frontmatter. List only `registered_id` values for commentaries that actually had blocks for this verse.
8. Write the file to `3-TRANSFORMATIONS/Adaptations/multilevel-summaries/<audience>/verse-<chapter-verse>.md`.

### For chapter scope

1. Read `1-SOURCES/Translations/bo-བློ་ལྡན་ཤེས་རབ།.md`. Identify the chapter heading `## N.` and collect the block IDs of all verses in that chapter (`^N-1` through `^N-last`).
2. For each verse in the chapter, run steps 2–3 from the verse procedure above, accumulating all commentary blocks across all verses.
3. Read all collected blocks. Identify the major themes and structural divisions the commentaries draw out across the chapter.
4. Draft the **Summary** as a chapter-level synthesis (not a verse-by-verse list) according to the audience priority rules.
5. Draft the **Sources** section listing all commentary blocks used, grouped by `registered_id`.
6. Fill the YAML frontmatter with the chapter number as `scope_id`.
7. Write the file to `3-TRANSFORMATIONS/Adaptations/multilevel-summaries/<audience>/chapter-<N>.md`.

---

## Completion check

- [ ] `scope`, `scope_id`, `audience`, and `commentaries_used` are set in frontmatter; `status: draft`
- [ ] Root Text section transcludes (does not copy) the verse or chapter opening from `bo-བློ་ལྡན་ཤེས་རབ།.md`
- [ ] Every claim in the Summary traces to a block in `1-SOURCES/Commentaries/`
- [ ] Summary length and register match the audience priority table (kids ≤ 150 w, general ≤ 250 w, academic ≤ 350 w)
- [ ] Kids summaries: concrete language, illustration note present if applicable
- [ ] Academic summaries: divergences flagged with ⚑, commentators named by `registered_id`
- [ ] Sources section lists every commentary block used as an Obsidian block-link
- [ ] No parametric Buddhist knowledge introduced without a source block citation
- [ ] File written to the correct path under `3-TRANSFORMATIONS/Adaptations/multilevel-summaries/`

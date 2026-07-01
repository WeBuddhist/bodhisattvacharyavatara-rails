---
name: verse-context-batch
description: Build all verse-level context packages for one chapter in bulk — traces root-text verse transclusions already embedded in each commentary to locate the relevant passage, then generates one 2-RAILS/Verses/<verse-id>.md file per verse in that chapter.
---

# verse-context-batch

This skill produces a complete set of verse-level context packages for an entire chapter, using a Python script to generate all files in one pass after the source-scanning phase is complete. It exists because building 30+ verse packages one at a time with `verse-context` is slow and prone to mapping inconsistencies between files — this skill enforces a single mapping table that every package in the chapter is generated from.

**How commentary passages are located:** The Transcluded commentary files already have the root-text verses embedded in them as Obsidian transclusions (e.g. `![[1-SOURCES/Translations/bo-བློ་ལྡན་ཤེས་རབ།.md#^1-2]]`). The text between one verse transclusion and the next is the commentary on that verse. To find the relevant passage for any verse, locate its transclusion in the commentary file and read the blocks that follow it up to (but not including) the next verse transclusion. There is no need to read the whole commentary text.

The output of this skill is identical in format to what `verse-context` produces for individual verses: each file has a verse transclusion, commentary passage transclusions, Tibetan synthesis prose per commentary, a Consensus section, and a disambiguated verse with block citations. Status is always `draft` on generation; a domain specialist marks files `complete` after review.

---

## Inputs

- **Chapter number** — e.g. `1` for Chapter 1.
- **Verse range** — first and last verse number in the chapter (e.g. `1-4` through `1-36`; verses that already have manually authored files may be skipped).
- **Commentary files** — all relevant files from `1-SOURCES/Commentaries/Transcluded/` for this vault (use only this folder; do not read from `1-SOURCES/Commentaries/` directly):
  - `BCAC19_KKP_bo_segmented.md` (Kunpal — Khenpo Kunzang Palden)
  - `BCAC14_NTS_bo_segmented.md` (Ngülchu Thogmé)
  - `BCAC14_SMPLG_bo_segmented.md` (Sabzang — Sa-bzang Ma-ti Paṇ-chen)
  - Other files present in `Transcluded/` and available for use: `BCAC13_KTB_bo.md`, `BCAC14_GDR_bo_segmented.md`, `BCAC19_KS_bo.md`, `BCAC19_MKS_bo_segmented.md`, `BCAC20_NKW_bo_segmented.md`, `BCACXX_WR_bo.md`
- **Translation file** — `1-SOURCES/Translations/bo-བློ་ལྡན་ཤེས་རབ།.md` (for verse transclusions).
- **All commentary files must already have block IDs.** Run `format-commentary` on any commentary that lacks them before proceeding.

---

## Output

One file per verse at:

```
2-RAILS/Verses/<chapter>-<verse>.md
```

e.g. `2-RAILS/Verses/1-4.md` through `2-RAILS/Verses/1-36.md`.

Files that already exist are skipped (not overwritten).

A Python generation script is saved to `0-INBOX/verse-context-batch-ch<N>.py` for audit and re-use.

---

## Output file format

Each generated file matches the `verse-context` schema exactly:

```markdown
---
verse_id: <chapter>-<verse>
root_text: 1-SOURCES/Translations/bo-བློ་ལྡན་ཤེས་རབ།.md
root_block: ^<chapter>-<verse>
language: bo
commentaries: [kunpal, ngulchu-thogmed, sabzang]
status: draft
---

## Verse

![[1-SOURCES/Translations/bo-བློ་ལྡན་ཤེས་རབ།.md#^<chapter>-<verse>]]

## Commentary passages

### kunpal

![[1-SOURCES/Commentaries/Transcluded/BCAC19_KKP_bo_segmented.md#^<block-id>]]
...

### ngulchu-thogmed

![[1-SOURCES/Commentaries/Transcluded/BCAC14_NTS_bo_segmented.md#^<block-id>]]
...

### sabzang

![[1-SOURCES/Commentaries/Transcluded/BCAC14_SMPLG_bo_segmented.md#^<block-id>]]
...

## Synthesis (original language)

### kunpal

<Tibetan prose summarising Kunpal's reading, with inline block citations>

### ngulchu-thogmed

<Tibetan prose summarising Ngülchu's reading, with inline block citations>

### sabzang

<Tibetan prose summarising Sabzang's reading, with inline block citations>

### Consensus

<Tibetan prose stating what all commentaries agree on>

## Disambiguated verse (original language)

![[1-SOURCES/Translations/bo-བློ་ལྡན་ཤེས་རབ།.md#^<chapter>-<verse>]]

(1-SOURCES/Commentaries/Transcluded/BCAC19_KKP_bo_segmented.md#^<block-id>)
(1-SOURCES/Commentaries/Transcluded/BCAC14_NTS_bo_segmented.md#^<block-id>)
(1-SOURCES/Commentaries/Transcluded/BCAC14_SMPLG_bo_segmented.md#^<block-id>)
```

---

## Rules

1. **Trace transclusions, do not read whole files.** Each commentary in `Transcluded/` has root-text verses embedded as transclusion lines. Grep for the target verse transclusion (e.g. `![[1-SOURCES/Translations/bo-བློ་ལྡན་ཤེས་རབ།.md#^1-2]]`) to find its location in the file, then read only the blocks from that line until the next verse transclusion. Those blocks are the commentary on that verse. Never read the whole commentary to build a mapping.
2. **A block that straddles two verse transclusions belongs to both.** If a block begins before verse N's transclusion and ends after it, include it in verse N's package and in verse N−1's package.
3. **Do not overwrite existing files.** If `2-RAILS/Verses/<verse-id>.md` already exists, skip it silently.
4. **Status is always `draft` on generation.** Never set `status: complete` — that is a human domain-specialist decision.
5. **Synthesis prose must be in Tibetan only.** No English in any synthesis subsection.
6. **Every synthesis claim must cite a source block.** Format: `(1-SOURCES/Commentaries/Transcluded/<file>.md#^<block-id>)` inline at the end of the claim.
7. **Save the generation script to `0-INBOX/`.** This preserves the mapping table for audit and re-runs.

---

## Procedure

### Phase 1 — Verify prerequisites

1. Confirm all three primary commentary files in `1-SOURCES/Commentaries/Transcluded/` contain verse transclusion lines for the target chapter. If a file lacks transclusions, it cannot be traced — flag and skip it.
2. Confirm `1-SOURCES/Translations/bo-བློ་ལྡན་ཤེས་རབ།.md` has block IDs for every verse in the target chapter (format `^<chapter>-<verse>`).
3. Note which verse files in `2-RAILS/Verses/` already exist and will be skipped.

### Phase 2 — Build the block mapping table by tracing transclusions

For each commentary file and each verse in the target range, locate the relevant passage by tracing the embedded transclusions:

1. **Grep** the commentary file for the verse's transclusion line, e.g.:
   `![[1-SOURCES/Translations/bo-བློ་ལྡན་ཤེས་རབ།.md#^<chapter>-<verse>]]`
2. **Read forward** from that line until the next verse transclusion (the commentary on the following verse begins there).
3. **Collect all block IDs** (`^<id>`) found in that span — these are the commentary blocks for this verse.
4. **Record** the block ID list in the mapping table.

Produce a mapping table of this shape:

| Verse | Kunpal blocks | Ngülchu blocks | Sabzang blocks |
|-------|--------------|----------------|----------------|
| 1-2   | ^… to ^… | ^… | ^… to ^… |
| ...   | ...          | ...            | ...    |

If a verse transclusion is absent from a commentary (the verse was skipped by that commentator), record the entry as empty and omit that commentary's subsection from the output file.

### Phase 3 — Draft synthesis descriptions

For each verse, note (in one sentence per commentary) the structural context and main interpretive point. These become the synthesis prose in the generated files. Cite the first key block per commentary.

### Phase 4 — Write the generation script

Write a Python script to `0-INBOX/verse-context-batch-ch<N>.py` that:

1. Defines the block mapping table as a Python dict keyed by verse number.
2. For each verse in the range:
   a. Skips if the output file already exists.
   b. Generates the markdown content using the mapping and synthesis descriptions.
   c. Writes to `2-RAILS/Verses/<chapter>-<verse>.md`.
3. Prints a summary of files created vs. skipped.

The script must be self-contained (no external dependencies beyond the Python standard library) and use absolute paths.

### Phase 5 — Run the script

Execute the script via bash. Verify the printed summary matches the expected count of new files.

### Phase 6 — Spot-check output

Read three generated files — one from the beginning, middle, and end of the chapter — and verify:
- Frontmatter fields are correct.
- All three commentary sections (kunpal, ngulchu-thogmed, sabzang) are present and non-empty.
- Block IDs in transclusion links match the mapping table.
- Synthesis prose is in Tibetan and has at least one inline citation.
- Disambiguated verse section has citations from all three commentaries.

### Phase 7 — Save and report

Confirm the generation script is saved to `0-INBOX/`. Report: total files generated, any files skipped (already existed), and any anomalies found in spot-check.

---

## Commentary block-ID reference (Chapter 1, BCA vault) — historical record

This section records block mappings produced by an earlier run of this skill using the pre-transclusion method. It is kept for audit purposes only. **Do not use these tables as input for new runs** — always derive block ranges by tracing the verse transclusions in the commentary files as described in Phase 2.

### Kunpal (`BCAC19_KKP_bo_segmented.md`)

Chapter 0 (introduction) runs through approximately `^0-175`. Chapter 1 body begins at `^0-127` (verse 1-1 material) and the verse-specific ranges are:

| Verse | Block range |
|-------|------------|
| 1-1 | ^0-127 to ^0-175 |
| 1-2 | ^0-156 to ^0-163 |
| 1-3 | ^0-164 to ^0-168 |
| 1-4 | ^0-176 to ^0-187 |
| 1-5 | ^0-188 to ^0-199 |
| 1-6 | ^0-200 |
| 1-7 | ^0-201 to ^0-203 |
| 1-8 | ^0-204 to ^0-205 |
| 1-9 | ^0-206 to ^0-211 |
| 1-10 | ^0-212 |
| 1-11 | ^0-213 to ^0-214 |
| 1-12 | ^0-215 to ^0-217 |
| 1-13 | ^0-218 to ^0-220 |
| 1-14 | ^0-221 |
| 1-15 | ^0-222 to ^0-239 |
| 1-16 | ^0-240 to ^0-243 |
| 1-17 | ^0-244 |
| 1-18 | ^0-245 to ^0-256 |
| 1-19 | ^0-257 to ^0-258 |
| 1-20 | ^0-259 to ^0-265 |
| 1-21 | ^0-266 to ^0-268 |
| 1-22 | ^0-269 to ^0-270 |
| 1-23 | ^0-271 |
| 1-24 | ^0-272 |
| 1-25 | ^0-273 to ^0-276 |
| 1-26 | ^0-277 to ^0-279 |
| 1-27 | ^0-280 to ^0-281 |
| 1-28 | ^0-282 to ^0-285 |
| 1-29 | ^0-286 to ^0-288 |
| 1-30 | ^0-289 to ^0-291 |
| 1-31 | ^0-292 to ^0-293 |
| 1-32 | ^0-294 to ^0-296 |
| 1-33 | ^0-297 to ^0-299 |
| 1-34 | ^0-300 to ^0-306 |
| 1-35 | ^0-307 to ^0-313 |
| 1-36 | ^0-314 to ^0-315 |

### Ngülchu (`BCAC14_NTS_bo_segmented.md`)

Ngülchu's Chapter 1 is divided into structural sections 1.3 through 1.11. His section numbers are his own — not root-text verse numbers.

| Verse | Ngülchu blocks | Ngülchu section |
|-------|---------------|-----------------|
| 1-1 | ^0-3-12 to ^1-1-7 | 0.3, 1.1 |
| 1-2 | ^1-2-1 | 1.2 |
| 1-3 | ^1-3-1 to ^1-3-16 | 1.3 (partial) |
| 1-4 | ^1-3-1 to ^1-3-16 | 1.3 |
| 1-5 | ^1-4-1, ^1-5-1, ^1-6-1 | 1.4, 1.5, 1.6 |
| 1-6 | ^1-7-1 to ^1-7-4 | 1.7 part 1 |
| 1-7 | ^1-7-5 to ^1-7-6 | 1.7 part 2 |
| 1-8 | ^1-7-6 to ^1-7-7 | 1.7 part 3 |
| 1-9 | ^1-7-7 to ^1-7-8 | 1.7 part 4 |
| 1-10 | ^1-7-8 to ^1-7-12 | 1.7 part 5, example 1 (gold) |
| 1-11 | ^1-7-13 to ^1-7-15 | 1.7 part 5, example 2 (jewel) |
| 1-12 | ^1-7-16 to ^1-7-21 | 1.7 part 5, example 3 (tree) |
| 1-13 | ^1-7-22 to ^1-7-26 | 1.7 part 5, example 4 (escort) |
| 1-14 | ^1-7-27 to ^1-7-52 | 1.7 part 5, examples 5–6 (fire + Gaṇḍavyūha) |
| 1-15 | ^1-8-1 to ^1-8-16 | 1.8 |
| 1-16 | ^1-8-1 to ^1-8-16 | 1.8 |
| 1-17 | ^1-8-1 to ^1-8-16 | 1.8 |
| 1-18 | ^1-9-1, ^1-10-1 to ^1-10-17 | 1.9, 1.10 |
| 1-19 | ^1-9-1, ^1-10-1 to ^1-10-17 | 1.9, 1.10 |
| 1-20 | ^1-9-1, ^1-10-1 to ^1-10-17 | 1.9, 1.10 |
| 1-21 | ^1-9-1, ^1-10-1 to ^1-10-17 | 1.9, 1.10 |
| 1-22 | ^1-11-1 to ^1-11-30 | 1.11 |
| 1-23 | ^1-11-1 to ^1-11-30 | 1.11 |
| 1-24 | ^1-11-1 to ^1-11-30 | 1.11 |
| 1-25 | ^1-11-1 to ^1-11-30 | 1.11 |
| 1-26 | ^1-11-1 to ^1-11-30 | 1.11 |
| 1-27 | ^1-11-1 to ^1-11-30 | 1.11 |
| 1-28 | ^1-11-1 to ^1-11-30 | 1.11 |
| 1-29 | ^1-11-1 to ^1-11-30 | 1.11 |
| 1-30 | ^1-11-1 to ^1-11-30 | 1.11 |
| 1-31 | ^1-11-1 to ^1-11-30 | 1.11 |
| 1-32 | ^1-11-1 to ^1-11-30 | 1.11 |
| 1-33 | ^1-11-1 to ^1-11-30 | 1.11 |
| 1-34 | ^1-11-1 to ^1-11-30 | 1.11 |
| 1-35 | ^1-11-1 to ^1-11-30 | 1.11 |
| 1-36 | ^1-11-1 to ^1-11-30 | 1.11 |

### Sabzang (`BCAC14_SMPLG_bo_segmented.md`)

Chapter 1 body has two large prose sections. Introduction runs through `^0-2-11`.

| Verse | Sabzang blocks |
|-------|---------------|
| 1-1 | ^0-2-11 |
| 1-2 | ^0-1-28 to ^0-1-30 |
| 1-3 | ^0-1-31, ^0-1-32 |
| 1-4 | ^1-1-1 to ^1-1-3 |
| 1-5 | ^1-1-4, ^1-1-5 |
| 1-6 | ^1-1-6 |
| 1-7 | ^1-1-6 |
| 1-8 | ^1-1-6 |
| 1-9 | ^1-1-7 |
| 1-10 | ^1-1-8 to ^1-1-13 |
| 1-11 | ^1-1-14, ^1-1-15 |
| 1-12 | ^1-1-16 to ^1-1-19 |
| 1-13 | ^1-1-19 to ^1-1-23 |
| 1-14 | ^1-1-24 to ^1-1-36 |
| 1-15 | ^1-1-37 |
| 1-16 | ^1-1-37 to ^1-1-41 |
| 1-17 | ^1-1-41 to ^1-1-46 |
| 1-18 | ^1-2-1, ^1-2-2 |
| 1-19 | ^1-2-3 to ^1-2-6 |
| 1-20 | ^1-2-7 to ^1-2-14 |
| 1-21 | ^1-2-15 to ^1-2-18 |
| 1-22 | ^1-2-19, ^1-2-20 |
| 1-23 | ^1-2-21, ^1-2-22 |
| 1-24 | ^1-2-23 to ^1-2-27 |
| 1-25 | ^1-2-28, ^1-2-29 |
| 1-26 | ^1-2-30 to ^1-2-32 |
| 1-27 | ^1-2-33 to ^1-2-35 |
| 1-28 | ^1-2-36 |
| 1-29 | ^1-2-37 |
| 1-30 | ^1-2-38 |
| 1-31 | ^1-2-38 |
| 1-32 | ^1-2-38 |
| 1-33 | ^1-2-38 |
| 1-34 | ^1-2-38 |
| 1-35 | ^1-2-38 |
| 1-36 | ^1-2-38 |

---

## Completion check

- [ ] All three primary commentary files confirmed to contain verse transclusion lines for the target chapter
- [ ] Block mapping table built by tracing transclusions (not by reading whole files or guessing)
- [ ] Generation script saved to `0-INBOX/verse-context-batch-ch<N>.py`
- [ ] Script run successfully; printed summary matches expected file count
- [ ] Three spot-checked files pass format verification
- [ ] No existing `2-RAILS/Verses/` files were overwritten
- [ ] All generated files have `status: draft`
- [ ] Synthesis prose is Tibetan only, with at least one inline block citation per commentary subsection

---
name: verse-context-batch
description: Build all verse-level context packages for one chapter in bulk — scans every commentary to produce a complete block-ID mapping, then generates one 2-RAILS/Verses/<verse-id>.md file per verse in that chapter.
---

# verse-context-batch

This skill produces a complete set of verse-level context packages for an entire chapter, using a Python script to generate all files in one pass after the source-scanning phase is complete. It exists because building 30+ verse packages one at a time with `verse-context` is slow and prone to mapping inconsistencies between files — this skill enforces a single mapping table that every package in the chapter is generated from.

The output of this skill is identical in format to what `verse-context` produces for individual verses: each file has a verse transclusion, commentary passage transclusions, Tibetan synthesis prose per commentary, a Consensus section, and a disambiguated verse with block citations. Status is always `draft` on generation; a domain specialist marks files `complete` after review.

---

## Inputs

- **Chapter number** — e.g. `1` for Chapter 1.
- **Verse range** — first and last verse number in the chapter (e.g. `1-4` through `1-36`; verses that already have manually authored files may be skipped).
- **Commentary files** — all relevant `1-SOURCES/Commentaries/*.md` files for this vault:
  - `bo-མཁན་པོ་ཀུན་དཔལ།.md` (Kunpal)
  - `bo-དངུལ་ཆུ་ཐོགས་མེད།.md` (Ngülchu Thogmé)
  - `bo-ས་བཟང་མ་ཏི་པཎ་ཆེན་བློ་གྲོས་རྒྱལ་མཚན།.md` (Sabzang Mati)
  - `bo-ཤེས་རབ་འབྱུང་གནས་བློ་གྲོས། Prajñākaramati.md` (Prajñākaramati)
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
commentaries: [kunpal, ngulchu-thogmed, sabzang, prajnakaramati]
status: draft
---

## Verse

![[1-SOURCES/Translations/bo-བློ་ལྡན་ཤེས་རབ།.md#^<chapter>-<verse>]]

## Commentary passages

### kunpal

![[1-SOURCES/Commentaries/bo-མཁན་པོ་ཀུན་དཔལ།.md#^<block-id>]]
...

### ngulchu-thogmed

![[1-SOURCES/Commentaries/bo-དངུལ་ཆུ་ཐོགས་མེད།.md#^<block-id>]]
...

### sabzang

![[1-SOURCES/Commentaries/bo-ས་བཟང་མ་ཏི་པཎ་ཆེན་བློ་གྲོས་རྒྱལ་མཚན།.md#^<block-id>]]
...

### prajnakaramati

![[1-SOURCES/Commentaries/bo-ཤེས་རབ་འབྱུང་གནས་བློ་གྲོས། Prajñākaramati.md#^<chapter>-<verse>-1]]

## Synthesis (original language)

### kunpal

<Tibetan prose summarising Kunpal's reading, with inline block citations>

### ngulchu-thogmed

<Tibetan prose summarising Ngülchu's reading, with inline block citations>

### sabzang

<Tibetan prose summarising Sabzang's reading, with inline block citations>

### prajnakaramati

<Tibetan prose summarising Prajñākaramati's reading, with inline block citation>

### Consensus

<Tibetan prose stating what all commentaries agree on>

## Disambiguated verse (original language)

![[1-SOURCES/Translations/bo-བློ་ལྡན་ཤེས་རབ།.md#^<chapter>-<verse>]]

(1-SOURCES/Commentaries/bo-མཁན་པོ་ཀུན་དཔལ།.md#^<block-id>)
(1-SOURCES/Commentaries/bo-དངུལ་ཆུ་ཐོགས་མེད།.md#^<block-id>)
(1-SOURCES/Commentaries/bo-ས་བཟང་མ་ཏི་པཎ་ཆེན་བློ་གྲོས་རྒྱལ་མཚན།.md#^<block-id>)
(1-SOURCES/Commentaries/bo-ཤེས་རབ་འབྱུང་གནས་བློ་གྲོས། Prajñākaramati.md#^<chapter>-<verse>-1)
```

---

## Rules

1. **Read before mapping.** Never guess block ranges. Read each commentary section in full before assigning block IDs to verses. Commentary structure frequently does not align one-to-one with root-text verses.
2. **Ngülchu's section numbers are his own, not root-text verse numbers.** `### 1.7` in Ngülchu means his structural section 7 of Chapter 1 — it covers multiple root-text verses. Map his sections to root-text verses by reading the content.
3. **Sabzang's Chapter 1 body has two large prose sections.** Section 1.1 (blocks `^1-1-1` to `^1-1-46`) covers root-text verses 1-4 through 1-17; Section 1.2 (blocks `^1-2-1` to `^1-2-38`) covers verses 1-18 through 1-36. Blocks may straddle verse boundaries — include the block in both verse packages where this occurs.
4. **Kunpal's blocks are sequential.** His Chapter 1 body runs from approximately `^0-127` onward. Map ranges by scanning for verse-heading markers.
5. **Prajñākaramati has one block per root-text verse.** Block ID format is `^<chapter>-<verse>-1` (e.g. `^1-4-1`, `^1-36-1`). Verify all blocks exist before generating.
6. **Do not overwrite existing files.** If `2-RAILS/Verses/<verse-id>.md` already exists, skip it silently.
7. **Status is always `draft` on generation.** Never set `status: complete` — that is a human domain-specialist decision.
8. **Synthesis prose must be in Tibetan only.** No English in any synthesis subsection.
9. **Every synthesis claim must cite a source block.** Format: `(1-SOURCES/Commentaries/<file>.md#^<block-id>)` inline at the end of the claim.
10. **Save the generation script to `0-INBOX/`.** This preserves the mapping table for audit and re-runs.

---

## Procedure

### Phase 1 — Verify prerequisites

1. Confirm all four commentary files have block IDs throughout. If any lacks block IDs, run `format-commentary` on it first and do not proceed until that is complete.
2. Confirm `1-SOURCES/Translations/bo-བློ་ལྡན་ཤེས་རབ།.md` has block IDs for every verse in the target chapter (format `^<chapter>-<verse>`).
3. Note which verse files in `2-RAILS/Verses/` already exist and will be skipped.

### Phase 2 — Build the block mapping table

For each commentary, read the relevant chapter section(s) and record the block ID range that covers each root-text verse. Produce a mapping table of this shape:

| Verse | Kunpal blocks | Ngülchu blocks | Sabzang blocks | Prajñākaramati |
|-------|--------------|----------------|----------------|----------------|
| 1-4   | ^0-176 to ^0-187 | ^1-3-1 to ^1-3-16 | ^1-1-1 to ^1-1-3 | ^1-4-1 |
| ...   | ...          | ...            | ...            | ...    |

**Kunpal:** Scan Chapter 1 body sequentially. Identify verse heading markers (e.g. `ཚིགས་སུ་བཅད་པ་བཞི་པ།`) to delimit block ranges per verse.

**Ngülchu:** Read each structural section heading (`### 1.X`). Read the section body to determine which root-text verses it covers. Note that multiple verses may fall within one section, and multiple sections may be needed for one verse.

**Sabzang:** Read Section 1.1 (blocks `^1-1-1` to `^1-1-46`) and Section 1.2 (blocks `^1-2-1` to `^1-2-38`) in full. Map each block to the root-text verse whose content it discusses. Where a block straddles two verses, include it in both.

**Prajñākaramati:** Grep for `^<chapter>-<verse>-1` blocks across the chapter range to confirm all exist.

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
- All four commentary sections are present and non-empty.
- Block IDs in transclusion links match the mapping table.
- Synthesis prose is in Tibetan and has at least one inline citation.
- Disambiguated verse section has citations from all four commentaries.

### Phase 7 — Save and report

Confirm the generation script is saved to `0-INBOX/`. Report: total files generated, any files skipped (already existed), and any anomalies found in spot-check.

---

## Commentary block-ID reference (Chapter 1, BCA vault)

This section records the mapping used for Chapter 1 of the Bodhisattvacaryāvatāra so subsequent runs can verify or extend it without re-reading all sources.

### Kunpal (`bo-མཁན་པོ་ཀུན་དཔལ།.md`)

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

### Ngülchu (`bo-དངུལ་ཆུ་ཐོགས་མེད།.md`)

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

### Sabzang (`bo-ས་བཟང་མ་ཏི་པཎ་ཆེན་བློ་གྲོས་རྒྱལ་མཚན།.md`)

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

### Prajñākaramati (`bo-ཤེས་རབ་འབྱུང་གནས་བློ་གྲོས། Prajñākaramati.md`)

One block per verse throughout. Block format: `^<chapter>-<verse>-1`.
Verified present for all Chapter 1 verses (1-1 through 1-36).

---

## Completion check

- [ ] All four commentary files confirmed to have block IDs before mapping begins
- [ ] Block mapping table built by reading source files (not guessed)
- [ ] Ngülchu section numbers confirmed not conflated with root-text verse numbers
- [ ] Generation script saved to `0-INBOX/verse-context-batch-ch<N>.py`
- [ ] Script run successfully; printed summary matches expected file count
- [ ] Three spot-checked files pass format verification
- [ ] No existing `2-RAILS/Verses/` files were overwritten
- [ ] All generated files have `status: draft`
- [ ] Synthesis prose is Tibetan only, with at least one inline block citation per commentary subsection

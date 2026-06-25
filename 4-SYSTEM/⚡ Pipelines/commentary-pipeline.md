---
updated: 2026-06-24
tags: [pipeline, commentary, content-engineering]
---

# Commentary Ingestion Pipeline

Eight-stage flow for turning a raw commentary text into block-ID'd, root-transcluded markdown ready to upload to the database. Source: whiteboard, June 2026. Target turnaround ~10 days per text.

> **Location:** Every stage of this pipeline operates inside `1-SOURCES/Commentaries/`. All file paths below are relative to that folder (e.g. `raw/<title>.md` means `1-SOURCES/Commentaries/raw/<title>.md`). This is `1-SOURCES/` work — only the permitted additions apply (block IDs, frontmatter, navigation links, `[Ed:...]` notes); no interpretive content is added here.

> **Tooling note:** No commentary-pipeline skills or scripts exist in the vault yet (`80_SYSTEM/82_Skills/CATALOG.md` covers only Documentation and UX). Only stage 3 has a defined method ("rule-based") from the whiteboard. All other **Tooling** lines below are marked _TBD_ — fill them in as the scripts/skills are built.

---

## Flow

`Dedup+Clean → Raw → Draft Seg. → TOC → Meaningful Blocks → Block+IDs → Root Transclusion → Upload to DB`

---

## Stages

### 1. Dedup + Clean
- **Input:** Raw source commentary as collected (may contain duplicate passages and noise/OCR artifacts).
- **Process:** Remove duplicated passages, strip noise, normalize formatting.
- **Output:** A single clean, deduplicated text (seeds the Raw baseline).
- **Tooling:** _TBD — cleaning/dedup script._

### 2. Raw
- **Input:** Clean text from stage 1.
- **Process:** Establish the cleaned text as the working baseline file in the vault.
- **Output:** `raw/<title>.md`
- **Tooling:** _TBD — file scaffold / manual._

### 3. Draft Segmentation
- **Input:** `raw/<title>.md`
- **Process:** Split the text into draft segments using **rule-based** segmentation.
- **Output:** Segmented `raw/<title>.md` (same file, now segmented).
- **Tooling:** Rule-based segmentation script.

### 4. TOC
- **Input:** Segmented `raw/<title>.md`
- **Process:** Reconstruct the commentary's own ས་བཅད (sa-bcad) outline with the **TOC tree extraction** flow — see [`toc-extraction.md`](toc-extraction.md). Run either the automated script ([`../Scripts/toc_tree_extractor/`](../Scripts/toc_tree_extractor/)) or the skill-by-skill route. Extraction is recall-first then precision: extract candidates, reconcile against the author's verbatim enumerations, then QC against attested strings.
- **Intermediate outputs (scratch, in `0-INBOX/` — not authoritative):**
  - `0-INBOX/toc-candidates-<id>.md` — merged section candidates with frontmatter.
  - `0-INBOX/toc-tree-<id>.md` — the nested, decimal-numbered TOC tree (Tibetan).
  - `0-INBOX/toc-tree-qc-<id>.md` — QC report (issues found / repaired / remaining).
  - `0-INBOX/temp/TOC-<id>/candidates/` and `.../enumerations/` — per-chunk staging (resumable).
- **Output (after human review):** The reviewed tree is promoted out of `0-INBOX/` into this folder as `<title>-toc.md` (i.e. `1-SOURCES/Commentaries/<title>-toc.md`). A human must review the tree before it is promoted or feeds anything downstream.
- **Tooling:** `toc_tree_extractor` script (Gemini Flash) or the `toc-candidate-extraction` / `add-toc` / `tag-inline-toc` skills.

### 5. Meaningful Blocks
- **Input:** `<title>-toc.md`
- **Process:** Resolve draft segments into meaningful content blocks.
- **Output:** Block-structured draft (feeds `<title>-blocks.md`).
- **Tooling:** _TBD._

### 6. Block + IDs
- **Input:** Meaningful blocks from stage 5.
- **Process:** Assign a stable block-ID anchor to each block, encoding its position in the TOC hierarchy (e.g. `^1-2-1-0`).
- **Output:** `<title>-blocks.md`
- **Tooling:** _TBD — ID-assignment script._

### 7. Root Transclusion
- **Input:** `<title>-blocks.md`
- **Process:** Transclude the matching root-text content into each block via its block-ID reference.
- **Output:** `<title>.md` (final assembled file).
- **Tooling:** _TBD._

### 8. Upload to DB
- **Input:** `<title>.md`
- **Process:** Push the finished text to the database.
- **Output:** Database record.
- **Tooling:** _TBD — upload script._

---

## Artifact summary

| File | Produced by | Contents |
|---|---|---|
| `raw/<title>.md` | ② ③ | Cleaned raw text, segmented |
| `0-INBOX/toc-{candidates,tree,tree-qc}-<id>.md` | ④ | TOC extraction drafts (scratch) |
| `<title>-toc.md` | ④ | Reviewed TOC tree, promoted from `0-INBOX/` |
| `<title>-blocks.md` | ⑤ ⑥ | Meaningful blocks with block IDs |
| `<title>.md` | ⑦ | Final: root transclusion, ready for upload |
| Database record | ⑧ | Uploaded text |

---

## Block ID convention

Each block heading carries an Obsidian block-ID anchor encoding its position in the TOC hierarchy:

```
## title ^1-2-1-0
```

The `^1-2-1-0` anchor is then used to transclude the matching root-text content into the block (stage 7).

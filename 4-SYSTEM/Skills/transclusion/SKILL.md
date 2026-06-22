---
name: transclusion
description: Insert Obsidian block-transclusion links for root-text verse(s) into a second root-text version or into commentary files, placing each transclusion at the correct structural position. TRIGGER this skill whenever a user requests transclusion in any phrasing or language — e.g. "root text verse transclusion", "add transclusions", "transclude verses into commentary", or equivalent phrases in Tibetan, Sanskrit, Chinese, or any other language.
---

# transclusion

This skill inserts `![[file#^block-id]]` transclusion links so that root-text verses appear inline at the right point in a second root-text version or in a commentary. It operationalises two distinct workflows — version-to-version alignment and verse-into-commentary placement — and enforces the vault rule that transclusions are navigation aids added to `1-SOURCES/` files, not interpretive content.

Two transclusion types are supported:

1. **Version-to-version** — align two root-text or translation files verse by verse by inserting transclusions of file A into file B (or bidirectionally). Matching uses Obsidian block IDs where both files have them; falls back to meaning-based position matching when one file lacks IDs, in which case the human must confirm every proposed match before the file is modified.

2. **Verse-into-commentary** — insert a transclusion of the root-text verse(s) at the correct structural position in one or more commentary files. For Tibetan master's commentaries the transclusion is placed on the line immediately before the specific sa-bcad (ས་བཅད།) phrase that introduces the commentary section for those verse(s). For non-Tibetan-master commentaries the transclusion is placed at the very beginning of the passage that discusses those verse(s).

---

## Inputs

### Type 1 — Version-to-version

| Field | Description | Example |
|---|---|---|
| `source-file` | File whose block IDs drive the matching | `1-SOURCES/Translations/bo-བློ་ལྡན་ཤེས་རབ།.md` |
| `target-file` | File to receive the transclusion links | `1-SOURCES/Text/sk-dev.md` |
| `verse-range` | Optional: limit to a specific range | `1-11–1-14`, or `all` (default) |
| `direction` | `source-into-target` (default) or `bidirectional` | `source-into-target` |

### Type 2 — Verse-into-commentary

| Field | Description | Example |
|---|---|---|
| `verse-ids` | One or more block IDs, comma-separated | `1-11, 1-12, 1-13` |
| `root-text-file` | Full vault-relative path to the root text or translation to transclude from | `1-SOURCES/Translations/bo-བློ་ལྡན་ཤེས་རབ།.md` |
| `commentary-files` | One or more commentary file paths to receive the transclusions | `1-SOURCES/Commentaries/bo-མཁན་པོ་ཀུན་དཔལ།.md` |
| `commentary-type` | `tibetan-master` or `other` | `tibetan-master` |

---

## Output

For both types: the target file(s) are modified in place. No new files are created. The only changes to a file are the insertion of `![[...#^...]]` transclusion lines and the blank lines immediately surrounding them. No existing content is deleted, reordered, or rephrased.

---

## Output file format

### Transclusion line format

Every inserted transclusion is a standalone line using the full vault-relative path:

```
![[1-SOURCES/Translations/bo-བློ་ལྡན་ཤེས་རབ།.md#^1-11]]
```

When two or more consecutive verses are transcluded together (because the commentary section covers a verse group), list them on consecutive lines with no blank line between them:

```
![[1-SOURCES/Translations/bo-བློ་ལྡན་ཤེས་རབ།.md#^1-13]]
![[1-SOURCES/Translations/bo-བློ་ལྡན་ཤེས་རབ།.md#^1-14]]
```

Surround any transclusion block with blank lines on both sides (unless it is already at the top of the file).

### Type 1 placement — version-to-version

Insert the transclusion of `source-file#^N-V` immediately before the corresponding verse block in `target-file`. The result looks like:

```
![[1-SOURCES/Translations/bo-བློ་ལྡན་ཤེས་རབ།.md#^1-11]]

सुपरीक्षितमप्रमेयधीभि-र्बहुमूल्यं ... ^1-11
```

### Type 2 placement — Tibetan master's commentary

For a Tibetan master's commentary, the transclusion is placed on the line **immediately before** the sa-bcad phrase (structural announcement) that introduces the commentary section for those verse(s). The sa-bcad phrase is the Tibetan enumeration phrase that opens a section (e.g., `གཉིས་པ་རིན་པོ་ཆེའི་དཔེས་བསྔགས་པ་ནི།`). A blank line precedes the transclusion block, and no blank line is inserted between the transclusion and the sa-bcad line:

```
ཞེས་པ་ལྟར་རོ། །

![[1-SOURCES/Translations/bo-བློ་ལྡན་ཤེས་རབ།.md#^1-11]]
གཉིས་པ་རིན་པོ་ཆེའི་དཔེས་བསྔགས་པ་ནི།
```

If the verse section is introduced by a Markdown heading (e.g., `### 1.2 ...`) rather than an inline sa-bcad, place the transclusion immediately before that heading line instead.

### Type 2 placement — other commentary

For non-Tibetan-master commentaries, insert the transclusion at the very beginning of the passage identified as discussing those verse(s), preceded and followed by a blank line:

```
![[1-SOURCES/Translations/bo-བློ་ལྡན་ཤེས་རབ།.md#^1-11]]

[commentary passage begins here]
```

---

## Rules

1. **Read-only except for navigation links.** `1-SOURCES/` files may receive block IDs, frontmatter, internal navigation links, and `[Ed:...]` editorial notes only. Transclusion links qualify as internal navigation links. No other content may be added, removed, or changed.
2. **Full vault-relative paths only.** Every transclusion link must use the full path from the vault root (e.g., `1-SOURCES/Translations/bo-བློ་ལྡན་ཤེས་རབ།.md#^1-11`), never a bare filename or short wiki-link.
3. **Never duplicate an existing transclusion.** Before inserting, check whether `![[source-file#^N-V]]` already appears in the vicinity of the target position. If it does, skip that verse and note it in the report.
4. **Never modify existing content.** Insertions only. Do not reorder, reformat, or delete any existing text.
5. **Block ID mismatch stops execution (Type 1, both-have-IDs case).** If the same block ID (`^N-V`) is present in one file but absent in the other, or if the verse counts differ across the target range, report every mismatch to the human before writing any changes. Do not proceed until the human confirms.
6. **Meaning-based matching requires human confirmation (Type 1, one-lacks-IDs case).** Present the full proposed match list (source verse text → target verse position) before writing. Do not proceed until the human confirms or corrects.
7. **Sa-bcad identification (Type 2, tibetan-master).** The sa-bcad to insert before is identified by:
   a. Markdown headings with block IDs ending in `-0` (e.g., `^1-2-0`, `^1-2-1-0`) — insert immediately before that heading line.
   b. Inline Tibetan structural enumeration phrases — ordinal words (གཅིག་པ་, གཉིས་པ་, གསུམ་པ་, བཞི་པ་, etc. or their equivalents) followed by a topic phrase ending in ནི། or ནི། །. These are the inline sa-bcad phrases. Insert immediately before the matching phrase.
   c. If no sa-bcad can be confidently identified for a verse, report it and ask the human to specify the insertion point before writing.
8. **Commentary-section matching (Type 2).** Identify the correct commentary section by:
   a. First: check whether the commentary has a TOC or explicit structural outline and use it to locate the section for the verse(s).
   b. Second: scan for context clues — verse number mentions, quotations of the verse, or key terms from the verse.
   c. If the correct section cannot be identified with confidence, report the ambiguity and ask the human before writing.
9. **Multiple commentaries.** When `commentary-files` lists more than one file, process each file independently using the same verse-ids. Do not carry state or assumptions from one commentary to the next.
10. **Report after every write.** For each file modified, report: the file path, the verse(s) inserted, and the exact line or phrase before which each transclusion was placed.

---

## Procedure

### Type 1 — Version-to-version

1. Read the frontmatter of both `source-file` and `target-file`. Confirm both are in `1-SOURCES/` and have `file_type: root-text | translation`. If not, stop and report.
2. Extract all block IDs from `source-file` in the form `^chapter-verse` (e.g., `^1-11`). Build a list: `{block_id → verse_text}`.
3. Extract all block IDs from `target-file` in the same form. Build a parallel list.
4. **If both files have block IDs:**
   a. Intersect the two lists over the requested `verse-range`.
   b. Identify any IDs present in one file but absent in the other. List every mismatch.
   c. If mismatches exist: present the full mismatch report to the human. Ask: "Proceed with matching verses only, or stop?" Do not write until the human responds.
   d. If no mismatches (or the human confirmed): for each matched ID, check if `![[source-file#^N-V]]` already exists adjacent to the target verse block. If yes, skip. If no, insert the transclusion immediately before `^N-V` in `target-file`.
5. **If `target-file` lacks block IDs:**
   a. Align source verses to target verse positions by order and meaning within the requested range.
   b. Produce a numbered match list: `source ^N-V "[first few words of source verse]" → target line N "[first few words of target verse]"`.
   c. Present the full match list to the human. Ask them to confirm or correct before writing.
   d. On confirmation: insert each transclusion at the identified target position.
6. Write the modified `target-file`. Report each insertion made.

### Type 2 — Verse-into-commentary

1. Read the frontmatter of `root-text-file`. Confirm it is in `1-SOURCES/Text/` or `1-SOURCES/Translations/` and has a `verse_id_format: chapter-verse` field. Record its full vault-relative path for use in transclusion links.
2. For each verse ID in `verse-ids`, confirm the block ID `^N-V` exists in `root-text-file`. If any ID is missing, stop and report which IDs are absent.
3. For each `commentary-file` in `commentary-files`:
   a. Read the commentary file in full.
   b. Determine `commentary-type` for this file (passed as input; default to `tibetan-master` for files with `lang_tag: bo` from `1-SOURCES/Commentaries/`).
   c. **If `commentary-type` is `tibetan-master`:**
      i. Locate the sa-bcad phrase or Markdown heading that introduces the commentary section for each target verse. Use Rule 7 (sa-bcad identification) and Rule 8 (commentary-section matching).
      ii. If a sa-bcad or heading cannot be confidently identified for any verse, report the uncertainty to the human and ask them to specify the insertion line before proceeding.
      iii. Check whether `![[root-text-file#^N-V]]` already appears on the line immediately before the identified sa-bcad. If yes, skip. If no, insert the transclusion on the line immediately before the sa-bcad. Ensure a blank line precedes the transclusion block and no blank line separates the transclusion from the sa-bcad line.
   d. **If `commentary-type` is `other`:**
      i. Locate the beginning of the passage that discusses the target verse(s) using Rule 8.
      ii. If the passage start cannot be identified, report and ask the human.
      iii. Insert the transclusion block at that point, surrounded by blank lines on both sides.
   e. Write the modified commentary file.
   f. Report: file path, verse(s) inserted, and the sa-bcad phrase or passage-start text before/at which each transclusion was placed.

---

## Completion check

- [ ] Both files confirmed to be in `1-SOURCES/` before any write (Type 1), or root-text and commentary files confirmed to exist and be in `1-SOURCES/` (Type 2)
- [ ] All target block IDs verified to exist in `root-text-file` before writing (Type 2)
- [ ] Mismatch report produced and human confirmation obtained before writing when block IDs diverge (Type 1, both-have-IDs)
- [ ] Full match list produced and human confirmation obtained before writing when one file lacks block IDs (Type 1)
- [ ] Sa-bcad or commentary passage correctly identified for every verse; human consulted for any uncertain placements (Type 2, tibetan-master)
- [ ] No existing transclusion duplicated at any insertion point
- [ ] Every inserted transclusion uses the full vault-relative path
- [ ] No existing text deleted, reordered, or rephrased in any file
- [ ] Post-write report produced listing every file modified, every verse inserted, and every insertion position

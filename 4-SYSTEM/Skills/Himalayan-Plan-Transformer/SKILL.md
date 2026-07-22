---
name: Himalayan-Plan-Transformer
description: Restructure a Himalayan-track day-plan file from the legacy 6-section Tibetan layout into the standardized 4-section layout — root verses and commentary moved to the top, refuge/bodhicitta/dedication merged into one combined section, ངོ་སྤྲོད retired, and the closing practice section renamed and reordered — while leaving all Hindi/English content untouched.
---

# Himalayan-Plan-Transformer

This skill rebuilds the Tibetan section structure of a single Himalayan-track day-plan file (`3-TRANSFORMATIONS/Plans/Himalayan/**`) to match the standardized 4-section layout, without altering the underlying verse text, commentary prose, or any trailing Hindi/English practice sections. It exists because the legacy 6-section template (separate ངོ་སྤྲོད section, split སྐྱབས་འགྲོ/སེམས་བསྐྱེད/ཚད་མེད་བཞི subsections, root verses buried in the middle, ཉམས་ལེན misnamed and misordered) was inconsistent across day files and made the daily liturgy hard to follow start-to-finish. "Correct output" means: the four top-level sections appear in the fixed order below, the three merged subsections under the refuge/bodhicitta section are exactly as specified, no verse content is altered or lost, and every byte outside the restructured Tibetan sections (in particular Hindi/English blocks) is preserved unchanged.

---

## Inputs

- **Target file path** — one day-plan file under `3-TRANSFORMATIONS/Plans/Himalayan/<chapter-folder>/Day-<N>-Ch<C>-V<range>.md`, currently in the legacy 6-section format (see Rule 11 for the expected shape).
- **Disposition of ༢། ངོ་སྤྲོད། content** — if that section is non-empty in the source file, the human contributor must say whether to delete the paragraph outright or fold it into another section (e.g. འགྲེལ་བཤད or དེ་རིང་གི་ཉམས་ལེན/ལག་ལེན) before this skill proceeds. Never assume; ask every time the section is non-empty, since the answer may differ file to file.

## Output

The same file, overwritten in place at its original path: `3-TRANSFORMATIONS/Plans/Himalayan/<chapter-folder>/Day-<N>-Ch<C>-V<range>.md`. No new files are created and no other files are touched.

---

## Output file format

```markdown
# ཉིན་ ༼N༽ - ཉིན་ ༣༦༥ ཡི་སྤྱོད་འཇུག་སློབ་སྦྱོང།

## སྤྱོད་འཇུག་ལེའུ་...པ། ཤློཀ་ ...

---

### ༡། དེ་རིང་གི་རྩ་ཚིག

<the day's root verses, verbatim from the source's root-verse section — shloka headers, chapter/verse annotations, and [cite: N] markers all preserved>

### ༢། འགྲེལ་བཤད།

<the source's commentary section content, verbatim, including any sub-headings such as རྩ་ཚིག་ངོས་འཛིན / རྩ་ཚིག་ངོ་སྤྲོད / རྩ་ཚིག་གནད་དོན — empty if the source's commentary section was empty>

### ༣། སྐྱབས་འགྲོ་སེམས་བསྐྱེད།

#### **༡. སྐྱབས་འགྲོ་སེམས་བསྐྱེད།**

<the source's སྐྱབས་འགྲོ verse block, then the source's སེམས་བསྐྱེད verse blocks, verbatim — ཚད་མེད་བཞི dropped entirely>

#### **༢. རྩ་ཚིག**

<the same day's root verses used in section 1, repeated here as plain blockquotes — no shloka headers, no chapter/verse annotations, no [cite: N] markers>

#### **༣. བསྔོ་སྨོན།**

<the source's བསྔོ་བ verse block, then the source's སྨོན་ལམ verse block, verbatim>

### ༤། དེ་རིང་གི་ལག་ལེན།

<if the source's ཉམས་ལེན section had a "**འགྲེལ་བཤད།**" labeled paragraph, it appears first here, relabeled "**ལམ་སྟོན།**">

<if the source's ཉམས་ལེན section had a "**ཉམས་ལེན་དངོས།**" labeled paragraph, it appears second here, relabeled "**ལག་ལེན་དངོས།**">

<any trailing Hindi (## १⁾ ...) and English (## 1) ...) sections from the source, copied verbatim, unchanged, in their original order and position at the end of the file>
```

---

## Rules

1. **Never delete a non-empty ངོ་སྤྲོད paragraph without explicit human confirmation.** If the section is empty, remove it silently. If it has content, stop and ask (see Inputs) before writing anything.
2. **ཚད་མེད་བཞི is always dropped.** It is never carried into the merged སྐྱབས་འགྲོ་སེམས་བསྐྱེད subsection or anywhere else in the output.
3. **The ༢. རྩ་ཚིག subsection is plain-text only.** Reuse the same verses as the top-level root-verse section, in the same order, but strip shloka numbering headers (`#### **༡༡. ཤློཀ་...**`), the `(ལེའུ་ ... ཤློཀ་ ...)` annotation, and every `[cite: N]` marker.
4. **སྐྱབས་འགྲོ and སེམས་བསྐྱེད verses are combined verbatim, word for word**, under one subsection titled identically to the parent section (སྐྱབས་འགྲོ་སེམས་བསྐྱེད).
5. **བསྔོ་བ and སྨོན་ལམ verses are combined verbatim** under one subsection titled བསྔོ་སྨོན།.
6. **འགྲེལ་བཤད content moves as a unit.** Every sub-heading and paragraph under the source's commentary section carries over unchanged; only its position in the file changes (it becomes the new section 2).
7. **Inside the final section, order is swapped and labels are renamed.** The paragraph labeled འགྲེལ་བཤད becomes ལམ་སྟོན and is placed first; the paragraph labeled ཉམས་ལེན་དངོས becomes ལག་ལེན་དངོས and is placed second. Only the bold inline label text changes — the paragraph body is untouched.
8. **Every occurrence of ཉམས་ལེན as a section or subsection title becomes ལག་ལེན** (e.g. `དེ་རིང་གི་ཉམས་ལེན།` → `དེ་རིང་གི་ལག་ལེན།`). This does not apply to occurrences of ཉམས་ལེན inside ordinary prose sentences (e.g. in Hindi/English commentary) — only structural titles are renamed.
9. **Trailing Hindi/English sections are copied byte-for-byte.** Do not translate, reformat, reorder, or otherwise touch any content after the Tibetan sections.
10. **Renumber sequentially.** Top-level sections are numbered ༡ through ༤ in the new order; the three merged subsections under section 3 are numbered ༡ through ༣.
11. **Expected legacy input shape** — six top-level sections in this order: སྐྱབས་འགྲོ་སེམས་བསྐྱེད (containing ཚད་མེད་བཞི, སྐྱབས་འགྲོ, སེམས་བསྐྱེད), ངོ་སྤྲོད, དེ་རིང་གི་རྩ་ཚིག, འགྲེལ་བཤད, བསྔོ་བ་དང་སྨོན་ལམ (containing བསྔོ་བ, སྨོན་ལམ), དེ་རིང་གི་ཉམས་ལེན (optionally containing ཉམས་ལེན་དངོས / འགྲེལ་བཤད paragraph labels). If the target file's structure deviates from this — a section missing, extra unexpected sections, subsections in a different order — stop and report the exact discrepancy to the human contributor rather than guessing how to map it.
12. **Never touch files outside the one target path.** This skill edits exactly one file per run.

---

## Procedure

1. Stage and read the target file in full.
2. Check the file against the expected legacy shape (Rule 11). If it doesn't match, stop and report the discrepancy.
3. If ༢། ངོ་སྤྲོད། contains any text beyond the bare heading, stop and ask the human contributor whether to delete it or fold it elsewhere (Rule 1). Wait for an answer before continuing.
4. Extract the day's root verses verbatim from the source's ༣། དེ་རིང་གི་རྩ་ཚིག section (headers, annotations, citations included).
5. Write the new **༡། དེ་རིང་གི་རྩ་ཚིག** section using the verses extracted in step 4, unchanged.
6. Write the new **༢། འགྲེལ་བཤད** section using the source's ४ འགྲེལ་བཤད content, unchanged (including any sub-headings).
7. Write the new **༣། སྐྱབས་འགྲོ་སེམས་བསྐྱེད** section with three subsections, in order:
   a. **༡. སྐྱབས་འགྲོ་སེམས་བསྐྱེད** — source's སྐྱབས་འགྲོ verse block followed by both སེམས་བསྐྱེད verse blocks, verbatim; ཚད་མེད་བཞི omitted.
   b. **༢. རྩ་ཚིག** — the same verses from step 4, re-rendered as plain blockquotes with headers/annotations/citations stripped (Rule 3).
   c. **༣. བསྔོ་སྨོན** — source's བསྔོ་བ verse block followed by the source's སྨོན་ལམ verse block, verbatim.
8. Write the new **༤། དེ་རིང་གི་ལག་ལེན** section: if the source's ཉམས་ལེན section was empty, keep it empty here (only the heading changes). Otherwise, place the relabeled ལམ་སྟོན paragraph first and the relabeled ལག་ལེན་དངོས paragraph second (Rule 7).
9. Reassemble the full file: H1 title line, H2 chapter/verse line, `---` divider, the four rebuilt sections in order, then any trailing Hindi/English sections copied verbatim from the source at the end.
10. Overwrite the target file at its original path with the reassembled content.
11. Work through the Completion check below before reporting the task done.

---

## Completion check

- [ ] The four top-level sections appear in exactly this order: དེ་རིང་གི་རྩ་ཚིག, འགྲེལ་བཤད, སྐྱབས་འགྲོ་སེམས་བསྐྱེད, དེ་རིང་གི་ལག་ལེན
- [ ] ངོ་སྤྲོད no longer appears anywhere, and if it had content, the human's confirmed disposition (delete vs. fold in) was followed
- [ ] ཚད་མེད་བཞི does not appear anywhere in the output
- [ ] སྐྱབས་འགྲོ་སེམས་བསྐྱེད contains exactly three subsections, in order: སྐྱབས་འགྲོ་སེམས་བསྐྱེད, རྩ་ཚིག, བསྔོ་སྨོན
- [ ] The ༢. རྩ་ཚིག subsection's verses carry no shloka header, no chapter/verse annotation, and no `[cite: N]` marker
- [ ] Inside the final section, ལམ་སྟོན precedes ལག་ལེན་དངོས
- [ ] Every trailing Hindi/English section matches the source byte-for-byte, in its original position
- [ ] Exactly one file was written, at its original path

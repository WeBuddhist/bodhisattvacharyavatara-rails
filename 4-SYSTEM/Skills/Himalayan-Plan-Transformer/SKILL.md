---
name: Himalayan-Plan-Transformer
description: Restructure a Himalayan-track day-plan file from the legacy 6-section Tibetan layout into the standardized 4-section layout — root verses and commentary moved to the top, refuge/bodhicitta/dedication merged into one combined section, ངོ་སྤྲོད retired, the closing practice section renamed and reordered, fixed sub-headings added under the commentary and practice sections, the root-verse identification sub-heading (རྩ་ཚིག་ངོས་འཛིན) populated by tracing each verse to its matching-chapter ས་བཅད outline source, and stray "(ལན་N)" repeat-count annotations stripped — while leaving all Hindi/English content untouched.
---

# Himalayan-Plan-Transformer

This skill rebuilds the Tibetan section structure of a single Himalayan-track day-plan file (`3-TRANSFORMATIONS/Plans/Himalayan/**`) to match the standardized 4-section layout, without altering the underlying verse text, commentary prose, or any trailing Hindi/English practice sections. It exists because the legacy 6-section template (separate ངོ་སྤྲོད section, split སྐྱབས་འགྲོ/སེམས་བསྐྱེད/ཚད་མེད་བཞི subsections, root verses buried in the middle, ཉམས་ལེན misnamed and misordered) was inconsistent across day files and made the daily liturgy hard to follow start-to-finish. "Correct output" means: the four top-level sections appear in the fixed order below, the three merged subsections under the refuge/bodhicitta section are exactly as specified, the commentary section always carries its three fixed sub-headings (with the first, རྩ་ཚིག་ངོས་འཛིན, always populated per Rule 14) and the practice section always carries its two fixed sub-headings, no `(ལན་N)` repeat-count annotation survives anywhere, no verse content is otherwise altered or lost, and every byte outside the restructured Tibetan sections (in particular Hindi/English blocks) is preserved unchanged.

---

## Inputs

- **Target file path** — one day-plan file under `3-TRANSFORMATIONS/Plans/Himalayan/<chapter-folder>/Day-<N>-Ch<C>-V<range>.md`, currently in the legacy 6-section format (see Rule 11 for the expected shape).
- **Disposition of ༢། ངོ་སྤྲོད། content** — if that section is non-empty in the source file, the human contributor must say whether to delete the paragraph outright or fold it into another section (e.g. འགྲེལ་བཤད or དེ་རིང་གི་ཉམས་ལེན/ལག་ལེན) before this skill proceeds. Never assume; ask every time the section is non-empty, since the answer may differ file to file.
- **No separate input needed for root-verse identification** — the source-of-truth folder for this is fixed: `3-TRANSFORMATIONS/Plans/the-bodhisattva-challenge/bo/bo-ཀུན་དཔལ།_རྩ་བའི་ས་བཅད་ངོས་འཛིན།/`. The specific chapter file inside it (`bo-Ch<N>-...ས་བཅད་གཞིར་བཟུང་རྩ་ཚིག་ངོས་འཛིན...md`) is selected automatically per Rule 14, matched to the target day-plan's own chapter number (from its `Ch<C>` filename segment). Do not default to the ལེའུ་གཉིས་པ (Ch2) file for a day-plan from a different chapter — always match `<N>` to the target file's chapter.

## Output

The same file, overwritten in place at its original path: `3-TRANSFORMATIONS/Plans/Himalayan/<chapter-folder>/Day-<N>-Ch<C>-V<range>.md`. No new files are created and no other files are touched.

---

## Output file format

```markdown
# ཉིན་ ༼N༽ - ཉིན་ ༣༦༥ ཡི་སྤྱོད་འཇུག་སློབ་སྦྱོང།

## སྤྱོད་འཇུག་ལེའུ་...པ། ཤློཀ་ ...

---

### ༡། དེ་རིང་གི་རྩ་ཚིག

<the day's root verses, verbatim from the source's root-verse section — shloka headers, chapter/verse annotations, and [cite: N] markers all preserved; any "(ལན་N)" repeat-count annotation stripped>

### ༢། འགྲེལ་བཤད།

#### **༡. རྩ་ཚིག་ངོས་འཛིན།**

<one line per root verse, in the same order as section 1, each identifying that verse's ས་བཅད outline origin per Rule 14 — see the worked example there>

#### **༢. རྩ་ཚིག་ངོ་སྤྲོད།**

<empty, unless the source already carried content specifically under this sub-heading>

#### **༣. རྩ་ཚིག་གནད་དོན།**

<the source's commentary prose (whatever was found directly under the legacy ༤། འགྲེལ་བཤད heading, not already split into the three sub-headings above), verbatim — empty if the source's commentary section was empty>

### ༣། སྐྱབས་འགྲོ་སེམས་བསྐྱེད།

#### **༡. སྐྱབས་འགྲོ་སེམས་བསྐྱེད།**

<the source's སྐྱབས་འགྲོ verse block, then the source's སེམས་བསྐྱེད verse blocks, verbatim — ཚད་མེད་བཞི dropped entirely; any "(ལན་N)" repeat-count annotation stripped>

#### **༢. རྩ་ཚིག**

<the same day's root verses used in section 1, repeated here as plain blockquotes — no shloka headers, no chapter/verse annotations, no [cite: N] markers>

#### **༣. བསྔོ་སྨོན།**

<the source's བསྔོ་བ verse block, then the source's སྨོན་ལམ verse block, verbatim; any "(ལན་N)" repeat-count annotation stripped>

### ༤། དེ་རིང་གི་ལག་ལེན།

#### **༡. ལམ་སྟོན།**

<if the source's ཉམས་ལེན section had a "**འགྲེལ་བཤད།**" labeled paragraph, it appears here, relabeled "**ལམ་སྟོན།**" — empty if there was none>

#### **༢. ལག་ལེན་དངོས།**

<if the source's ཉམས་ལེན section had a "**ཉམས་ལེན་དངོས།**" labeled paragraph, it appears here, relabeled "**ལག་ལེན་དངོས།**" — empty if there was none>

<any trailing Hindi (## १⁾ ...) and English (## 1) ...) sections from the source, copied verbatim, unchanged, in their original order and position at the end of the file>
```

---

## Rules

1. **Never delete a non-empty ངོ་སྤྲོད paragraph without explicit human confirmation.** If the section is empty, remove it silently. If it has content, stop and ask (see Inputs) before writing anything.
2. **ཚད་མེད་བཞི is always dropped.** It is never carried into the merged སྐྱབས་འགྲོ་སེམས་བསྐྱེད subsection or anywhere else in the output.
3. **The ༢. རྩ་ཚིག subsection is plain-text only.** Reuse the same verses as the top-level root-verse section, in the same order, but strip shloka numbering headers (`#### **༡༡. ཤློཀ་...**`), the `(ལེའུ་ ... ཤློཀ་ ...)` annotation, and every `[cite: N]` marker.
4. **སྐྱབས་འགྲོ and སེམས་བསྐྱེད verses are combined verbatim, word for word**, under one subsection titled identically to the parent section (སྐྱབས་འགྲོ་སེམས་བསྐྱེད) — except for `(ལན་N)` annotations, which are always stripped (Rule 13).
5. **བསྔོ་བ and སྨོན་ལམ verses are combined verbatim** under one subsection titled བསྔོ་སྨོན། — except for `(ལན་N)` annotations, which are always stripped (Rule 13).
6. **འགྲེལ་བཤད content moves as a unit, under a fixed three-subsection scaffold.** The new ༢། འགྲེལ་བཤད section always contains exactly three sub-headings, in this fixed order and exact wording: `#### **༡. རྩ་ཚིག་ངོས་འཛིན།**`, `#### **༢. རྩ་ཚིག་ངོ་སྤྲོད།**`, `#### **༣. རྩ་ཚིག་གནད་དོན།**`. The second and third stay empty when the source's commentary section was empty. If the source's commentary was a single undivided block of prose (not already split under these three labels), that prose goes entirely under the third sub-heading, རྩ་ཚིག་གནད་དོན, leaving the second empty. If the source already had content organized under matching sub-headings (e.g. a prior partial transform), preserve that mapping instead of collapsing everything into the third. **Exception:** the first sub-heading, རྩ་ཚིག་ངོས་འཛིན, is never left empty — it is always freshly populated per Rule 14 regardless of what (if anything) the source carried there.
7. **Inside the final section, order is swapped, labels are renamed, and a fixed two-subsection scaffold is added.** The new ༤། དེ་རིང་གི་ལག་ལེན section always contains exactly two sub-headings, in this fixed order and exact wording: `#### **༡. ལམ་སྟོན།**`, `#### **༢. ལག་ལེན་དངོས།**` — present even when the source's ཉམས་ལེན section was empty (both then stay empty). The paragraph labeled འགྲེལ་བཤད becomes ལམ་སྟོན and is placed under the first sub-heading; the paragraph labeled ཉམས་ལེན་དངོས becomes ལག་ལེན་དངོས and is placed under the second. Only the bold inline label text at the top level changes — the paragraph body is untouched, and the paragraph's own inline bold label (e.g. "**ལམ་སྟོན།**") is left in place under the sub-heading even though it now repeats the sub-heading's wording; do not strip it.
8. **Every occurrence of ཉམས་ལེན as a section or subsection title becomes ལག་ལེན** (e.g. `དེ་རིང་གི་ཉམས་ལེན།` → `དེ་རིང་གི་ལག་ལེན།`). This does not apply to occurrences of ཉམས་ལེན inside ordinary prose sentences (e.g. in Hindi/English commentary) — only structural titles are renamed.
9. **Trailing Hindi/English sections are copied byte-for-byte.** Do not translate, reformat, reorder, or otherwise touch any content after the Tibetan sections.
10. **Renumber sequentially.** Top-level sections are numbered ༡ through ༤ in the new order; the three merged subsections under section 3 are numbered ༡ through ༣; the sub-headings under sections 2 and 4 use their own fixed numbering as given in Rules 6 and 7.
11. **Expected legacy input shape** — six top-level sections in this order: སྐྱབས་འགྲོ་སེམས་བསྐྱེད (containing ཚད་མེད་བཞི, སྐྱབས་འགྲོ, སེམས་བསྐྱེད), ངོ་སྤྲོད, དེ་རིང་གི་རྩ་ཚིག, འགྲེལ་བཤད, བསྔོ་བ་དང་སྨོན་ལམ (containing བསྔོ་བ, སྨོན་ལམ), དེ་རིང་གི་ཉམས་ལེན (optionally containing ཉམས་ལེན་དངོས / འགྲེལ་བཤད paragraph labels). If the target file's structure deviates from this — a section missing, extra unexpected sections, subsections in a different order — stop and report the exact discrepancy to the human contributor rather than guessing how to map it.
12. **Never touch files outside the one target path.** This skill edits exactly one file per run.
13. **Every `(ལན་N)` repeat-count annotation is stripped, wherever it appears.** These are recitation-repeat markers (e.g. `*(ལན་༣)*` meaning "repeat 3 times"), not part of the verse text itself. Remove the marker and any asterisk/italic wrapping around it, together with any stray space left before it, so the line ends cleanly at the verse's own closing punctuation. This applies throughout the file (root verses, the merged refuge/bodhicitta and dedication subsections, anywhere else it turns up) — it is the one exception to the otherwise-verbatim rules above.

14. **Populate ༡. རྩ་ཚིག་ངོས་འཛིན by tracing each root verse to its ས་བཅད outline source — matched to the correct chapter, never assumed.**

    a. **Locate the source file.** Take the target day-plan's chapter number from its own filename (`Day-<N>-Ch<C>-V<range>.md` → chapter `<C>`) — every verse in a single day-plan file belongs to the same chapter, since the plan is itself chapter-scoped. Open the one file in `3-TRANSFORMATIONS/Plans/the-bodhisattva-challenge/bo/bo-ཀུན་དཔལ།_རྩ་བའི་ས་བཅད་ངོས་འཛིན།/` whose name contains `Ch<C>` (e.g. chapter 2 → `bo-Ch2-ལེའུ་གཉིས་པ་ས་བཅད་གཞིར་བཟུང་རྩ་ཚིག་ངོས་འཛིན་བསྡུས་དོན།.md`). **Never substitute a different chapter's file** — a day-plan from Chapter 5 must be traced against the Ch5 file, not Ch2, even if Ch2 was used as the model for this rule.

    b. **Match by verse text, not by counting.** For each verse under the day-plan's ༡། དེ་རིང་གི་རྩ་ཚིག (one verse per ཤློཀ་... entry), search the chapter file for the `##` ས་བཅད heading whose quoted verse block contains that verse's exact pādas. Chapter files list verses grouped under headings, each heading's block containing one or more verses separated by blank lines, followed by a footnote sentence ("ཞེས་པའི་ཤློཀ་...འདི་དག་ནི...") that is itself a model for the sentence you are about to write — it is not the sentence to reuse (it describes the verse's place in the full ས་བཅད outline tree, not its place under the heading title).

    c. **Determine the verse's ordinal position within that heading's block** by counting the blank-line-separated verse groups from the top of the block, starting at 1. If the heading's block contains only one verse, there is no ordinal to state.

    d. **Write one line per verse** under རྩ་ཚིག་ངོས་འཛིན, in the same order as ༡། དེ་རིང་གི་རྩ་ཚིག, each preceded by a bold label matching that verse's own shloka header (e.g. `**ཤློཀ་དང་པོ།**`), followed by a sentence of this exact form:

       `ཚིགས་བཅད་འདི་ནི་སྤྱོད་འཇུག་ལེའུ་[ལེའུ་number spelled out]་པ་ལས་[ས་བཅད heading title, article/particle changes elided as needed]འི་ཚིགས་བཅད་[ordinal]་ཡིན་ནོ།།`

       — omitting `[ordinal]` (and the word "ཚིགས་བཅད་" simply ends the sentence: `...འི་ཚིགས་བཅད་ཡིན་ནོ།།`) when step (c) found only one verse under that heading.

       Chapter-number spelling (`[ལེའུ་number spelled out]`): དང་པོ (1), གཉིས་པ (2), གསུམ་པ (3), བཞི་པ (4), ལྔ་པ (5), དྲུག་པ (6), བདུན་པ (7), བརྒྱད་པ (8), དགུ་པ (9), བཅུ་པ (10). Ordinal spelling for the verse's position within the heading (`[ordinal]`) follows the same series: དང་པོ (1st), གཉིས་པ (2nd), གསུམ་པ (3rd), བཞི་པ (4th), ལྔ་པ (5th), and so on.

       Worked example (from a Chapter 2 day-plan, the plan's second verse, which is the first verse under the heading ༢། བདག་པོས་ཡོངས་སུ་མ་བཟུང་བའི་མཆོད་པ།):
       `**ཤློཀ་གཉིས་པ།** ཚིགས་བཅད་འདི་ནི་སྤྱོད་འཇུག་ལེའུ་གཉིས་པ་ལས་བདག་པོས་ཡོངས་སུ་མ་བཟུང་བའི་མཆོད་པའི་ཚིགས་བཅད་དང་པོ་ཡིན་ནོ།།`

    e. **If a verse's text cannot be located anywhere in the matching chapter file**, stop and report the discrepancy to the human contributor rather than guessing or leaving the line silently blank.

---

## Procedure

1. Stage and read the target file in full.
2. Check the file against the expected legacy shape (Rule 11). If it doesn't match, stop and report the discrepancy.
3. If ༢། ངོ་སྤྲོད། contains any text beyond the bare heading, stop and ask the human contributor whether to delete it or fold it elsewhere (Rule 1). Wait for an answer before continuing.
4. Extract the day's root verses verbatim from the source's ༣། དེ་རིང་གི་རྩ་ཚིག section (headers, annotations, citations included), then strip any `(ལན་N)` annotation (Rule 13).
5. Write the new **༡། དེ་རིང་གི་རྩ་ཚིག** section using the verses extracted in step 4.
6. Write the new **༢། འགྲེལ་བཤད** section: emit the three fixed sub-headings from Rule 6 in order, with one blank line between the section heading and the first sub-heading and between each sub-heading and the next. Place the source's commentary content under the second and third sub-headings per Rule 6 (defaulting to རྩ་ཚིག་གནད་དོན when the source had one undivided block, or empty when the source's commentary was empty). Leave the first sub-heading, རྩ་ཚིག་ངོས་འཛིན, for step 7.
7. Populate **༡. རྩ་ཚིག་ངོས་འཛིན** per Rule 14: for each verse extracted in step 4, locate the matching-chapter ས་བཅད outline file, trace the verse to its heading and ordinal position, and write the identification line. Stop and report to the human contributor if any verse's text cannot be located (Rule 14e).
8. Write the new **༣། སྐྱབས་འགྲོ་སེམས་བསྐྱེད** section with three subsections, in order:
   a. **༡. སྐྱབས་འགྲོ་སེམས་བསྐྱེད** — source's སྐྱབས་འགྲོ verse block followed by both སེམས་བསྐྱེད verse blocks, verbatim; ཚད་མེད་བཞི omitted; any `(ལན་N)` annotation stripped (Rule 13).
   b. **༢. རྩ་ཚིག** — the same verses from step 4, re-rendered as plain blockquotes with headers/annotations/citations stripped (Rule 3).
   c. **༣. བསྔོ་སྨོན** — source's བསྔོ་བ verse block followed by the source's སྨོན་ལམ verse block, verbatim; any `(ལན་N)` annotation stripped (Rule 13).
9. Write the new **༤། དེ་རིང་གི་ལག་ལེན** section: emit the two fixed sub-headings from Rule 7 in order, with one blank line between the section heading and the first sub-heading and between the two sub-headings. If the source's ཉམས་ལེན section was empty, both stay empty (only the headings appear). Otherwise, place the relabeled ལམ་སྟོན paragraph under the first sub-heading and the relabeled ལག་ལེན་དངོས paragraph under the second (Rule 7), leaving each paragraph's own inline bold label untouched.
10. Reassemble the full file: H1 title line, H2 chapter/verse line, `---` divider, the four rebuilt sections in order, then any trailing Hindi/English sections copied verbatim from the source at the end.
11. Overwrite the target file at its original path with the reassembled content.
12. Work through the Completion check below before reporting the task done.

---

## Completion check

- [ ] The four top-level sections appear in exactly this order: དེ་རིང་གི་རྩ་ཚིག, འགྲེལ་བཤད, སྐྱབས་འགྲོ་སེམས་བསྐྱེད, དེ་རིང་གི་ལག་ལེན
- [ ] ངོ་སྤྲོད no longer appears anywhere, and if it had content, the human's confirmed disposition (delete vs. fold in) was followed
- [ ] ཚད་མེད་བཞི does not appear anywhere in the output
- [ ] སྐྱབས་འགྲོ་སེམས་བསྐྱེད contains exactly three subsections, in order: སྐྱབས་འགྲོ་སེམས་བསྐྱེད, རྩ་ཚིག, བསྔོ་སྨོན
- [ ] The ༢. རྩ་ཚིག subsection's verses carry no shloka header, no chapter/verse annotation, and no `[cite: N]` marker
- [ ] འགྲེལ་བཤད contains exactly three sub-headings, in order: རྩ་ཚིག་ངོས་འཛིན, རྩ་ཚིག་ངོ་སྤྲོད, རྩ་ཚིག་གནད་དོན, each separated from the section heading and from each other by exactly one blank line
- [ ] རྩ་ཚིག་ངོས་འཛིན contains one identification line per root verse, in the same order as ༡། དེ་རིང་གི་རྩ་ཚིག, each traced to the matching-chapter (never a hardcoded Ch2) ས་བཅད outline file per Rule 14, with correct heading title and ordinal (or no ordinal when the heading holds only one verse)
- [ ] དེ་རིང་གི་ལག་ལེན contains exactly two sub-headings, in order: ལམ་སྟོན, ལག་ལེན་དངོས, each separated from the section heading and from each other by exactly one blank line
- [ ] Inside the final section, ལམ་སྟོན precedes ལག་ལེན་དངོས
- [ ] No `(ལན་N)` repeat-count annotation (in any of its asterisk/italic forms) remains anywhere in the file
- [ ] Every trailing Hindi/English section matches the source byte-for-byte, in its original position
- [ ] Exactly one file was written, at its original path

---
name: root-verse-transclusion
description: Insert root-text verse transclusions into a commentary file by classifying every commentary section against the three placement categories defined in `1-SOURCES/About Sources.md` §9 — verse-group overview, verse-by-verse exposition, or introductory section with no specific verse reference — and applying the matching placement rule to each. Language-agnostic (works for any `1-SOURCES/Commentaries/` file, not only Tibetan master's commentaries). TRIGGER whenever a user asks to add root-verse transclusions to a commentary per the vault's §9 rules, to "transclude the root verses into this commentary the standard way," or to check/repair transclusion placement against About Sources.
---

# root-verse-transclusion

This is the canonical, general-purpose implementation of `1-SOURCES/About Sources.md` §9 ("Format — with transclusions"). It anchors a commentary to its root text by inserting `![[...]]` transclusion links, but only after classifying *why* the transclusion belongs where it belongs — the three-way distinction §9 draws between a section that introduces a group of verses, a section that comments verse by verse, and an introductory section with no verse reference at all. Getting this classification wrong is the main failure mode this skill exists to prevent: transcluding all verses at the top of a verse-by-verse section (over-transclusion) or omitting the group transclusion at the opening of an overview section (under-transclusion) both misrepresent the commentary's own structure.

This skill is deliberately structure-first and script-agnostic — it does not assume Tibetan sa-bcad (ས་བཅད) phrasing or any other language's structural idiom. For Tibetan master's commentaries where transclusions must land on the exact line before a sa-bcad phrase (with its own blank-line conventions), use `transclusion` (Type 2, `commentary-type: tibetan-master`) or the scripted pipeline `Transclusion-rootext-into-commentaries` instead — both give finer control over sa-bcad-level placement than this skill's section-level classification. Use this skill when the classification itself, not the fine placement within a Tibetan structural block, is the open question — including for non-Tibetan commentaries where no equivalent skill exists.

---

## Inputs

| Field | Description | Example |
|---|---|---|
| `root-text-file` | Full vault-relative path to the root text or translation to transclude from. Must declare `verse_id_format: chapter-verse` in frontmatter. | `1-SOURCES/Text/bo-root-text.md` |
| `commentary-file` | Full vault-relative path to the commentary to modify in place. Must be in `1-SOURCES/Commentaries/` with `file_type: commentary`. | `1-SOURCES/Commentaries/bo-mkhan-po-kun-dpal.md` |
| `section-scope` | Optional. A chapter number, a `###` section heading, or `all` (default). Limits which sections are classified and modified in this run. | `1`, `1.2`, `all` |

If any input is missing or the named file does not exist, stop and ask the human contributor before proceeding — do not guess a path.

---

## Output

`commentary-file` is modified in place. The only changes are inserted `![[root-text-file#^N-V]]` transclusion lines, one per verse, each on its own line. No new files are created. No existing commentary text is added, removed, reordered, or rephrased — per §1's "no interpretation" rule, which transclusion links (internal navigation links) are explicitly permitted to satisfy.

Alongside the edit, produce a run report (in the response, not written to the vault) listing, for every section in scope: the section heading, its classification (group / verse-by-verse / introductory), and the verse IDs transcluded or skipped-as-duplicate.

---

## Output file format

### Category A — section introducing a group of verses

All verses in the group are transcluded in sequence at the section's opening, before any commentary text:

```markdown
### 1.2 Verses 1–3 — Overview ^1-2-0

![[1-SOURCES/Text/[lang]-root-text.md#^1-1]]
![[1-SOURCES/Text/[lang]-root-text.md#^1-2]]
![[1-SOURCES/Text/[lang]-root-text.md#^1-3]]

[Introductory overview commentary addressing verses 1–3 together.] ^1-2-1
```

### Category B — verse-by-verse section

Exactly one transclusion immediately before the commentary on each individual verse:

```markdown
### 1.3 Verse-by-verse commentary ^1-3-0

![[1-SOURCES/Text/[lang]-root-text.md#^1-1]]

[Commentary on verse 1 only.] ^1-3-1

![[1-SOURCES/Text/[lang]-root-text.md#^1-2]]

[Commentary on verse 2 only.] ^1-3-2
```

### Category C — introductory section, no specific verse reference

No transclusion is inserted:

```markdown
### 1.1 Author's opening remarks ^1-1-0

[General remarks on the chapter's purpose, with no reference to a specific root verse.] ^1-1-1
```

### Range syntax is never used

Obsidian does not support block-ID range transclusion (`#^1-1:#^1-3`). Category A always expands to sequential individual transclusion lines, one per verse, even for long groups.

---

## Rules

1. **Classify before writing.** Every `###`/`####` section in `section-scope` is assigned exactly one of three categories (A: group, B: verse-by-verse, C: introductory/no-verse) before any transclusion is inserted for that section. A section is never partially classified.
2. **Category A — all-at-once, at the opening.** If a section introduces a defined group of verses, every verse in that group is transcluded in sequence, immediately after the heading and before any commentary prose — never interleaved with the group's commentary.
3. **Category B — one-per-verse, immediately before its own commentary.** If a section addresses verses one at a time, each verse gets exactly one transclusion, placed on the line immediately before the first line of commentary that concerns it — not at the top of the section.
4. **Category C — nothing.** If a section makes no identifiable reference to a specific root verse or verse group (pure introduction, colophon remarks, historical background), no transclusion is inserted, even if the section falls within `section-scope`.
5. **Ambiguous sections stop the run.** If a section could plausibly be A, B, or C (e.g., it names a verse range in its heading but then comments verse by verse in its body), do not guess. Report the section heading and the ambiguity to the human contributor and ask them to classify it before writing that section.
6. **Sequential individual transclusions only.** Never emit a block-ID range. A group of N verses becomes N consecutive `![[...]]` lines.
7. **Full vault-relative paths.** Every transclusion uses the complete path from the vault root — `1-SOURCES/Text/[lang]-root-text.md#^N-V` — never a bare filename or short wiki-link, per §10.
8. **Idempotent.** Before inserting `![[root-text-file#^N-V]]`, check whether it already exists at or near the correct position for that verse in that section. If it does, skip and record it as skipped in the report — never insert a duplicate.
9. **Block IDs must exist.** Every verse ID used must be a real block ID (`^N-V`) present in `root-text-file`. If a verse referenced by the commentary's own numbering has no matching block ID in `root-text-file`, stop and report the missing ID rather than fabricating a link.
10. **Insertion only — no other edits.** This skill never adds, deletes, reorders, or rephrases existing commentary text, and never touches headings, block IDs, or frontmatter already present. The only lines it writes are `![[...]]` transclusion lines and the blank lines needed to keep them as their own Markdown block.
11. **Original language only.** No translation, paraphrase, or `[Ed:...]` note is introduced by this skill. If a genuinely factual observation is needed (e.g. to record why a section was classified as C), that is a separate, human-authored `[Ed:...]` note — not something this skill adds on its own.

---

## Procedure

1. Read `root-text-file` frontmatter. Confirm `file_type` is `root-text` or `translation` and `verse_id_format` is `chapter-verse`. Extract every block ID (`^N-V`) into a lookup `{id → verse_text}`. If the frontmatter checks fail, stop and report.
2. Read `commentary-file` frontmatter. Confirm `file_type: commentary`. Note its `verse_id_format` (for the commentary's own numbering, which may differ from the root text's) and, if present, `covers_verses`.
3. Walk the commentary's `##`/`###`/`####` headings within `section-scope`, in document order.
4. For each section, read its heading text and its full body down to the next heading of equal or higher level. Classify it:
   a. **Category A** if the heading or opening line explicitly names a range or set of verses (e.g. "Verses 1–5", "verses covered: 1-1 to 1-3") and the section's body opens with commentary addressing them collectively before, if ever, treating them individually.
   b. **Category B** if the section's body is organized as a sequence of per-verse blocks, each one clearly attributable to a single verse (by explicit numbering, by direct quotation of that verse, or by an existing but misplaced transclusion).
   c. **Category C** if the section contains no identifiable reference to a specific root verse or verse group.
   d. If none of (a)–(c) applies cleanly, do not classify by default to B or any other category — flag as ambiguous per Rule 5.
5. For every Category A section: determine the verse IDs in the group (from the heading's stated range, cross-checked against `root-text-file`'s block IDs). Insert `![[root-text-file#^N-V]]` for each, in order, directly after the heading line and before the first line of commentary prose. Skip any verse whose transclusion already exists there (Rule 8).
6. For every Category B section: for each verse addressed, locate the first line of commentary specific to that verse and insert `![[root-text-file#^N-V]]` on the line immediately before it. Skip any verse whose transclusion already exists there.
7. For every Category C section: make no edit.
8. Before writing, verify every verse ID used in steps 5–6 exists in the `root-text-file` lookup from step 1. If any is missing, stop and report the missing ID(s) without writing.
9. Write `commentary-file` with the insertions applied. Do not alter any other byte of the file.
10. Produce the run report described under Output: section heading, classification, verses transcluded, verses skipped as duplicate, and any sections left unclassified (with reasons) pending human input.
11. Spot-check the written file: confirm no `![[root-text-file#^N-V]]` block ID appears twice, and that every non-inserted line is byte-identical to the pre-write version.

---

## Completion check

- [ ] `root-text-file` confirmed `root-text`/`translation` with `verse_id_format: chapter-verse`; block-ID lookup built
- [ ] `commentary-file` confirmed `file_type: commentary` in `1-SOURCES/Commentaries/`
- [ ] Every section in `section-scope` classified as exactly one of A / B / C, or flagged and reported as ambiguous — none silently defaulted
- [ ] Category A sections: all group verses transcluded in sequence at the section opening, before any commentary prose
- [ ] Category B sections: exactly one transclusion per verse, immediately before that verse's own commentary
- [ ] Category C sections: zero transclusions inserted
- [ ] No block-ID range syntax used anywhere (always sequential individual transclusions)
- [ ] Every transclusion uses the full vault-relative path
- [ ] No duplicate transclusion inserted; every verse ID confirmed to exist in `root-text-file` before writing
- [ ] No existing commentary text added, removed, reordered, or rephrased (non-inserted lines byte-identical before/after)
- [ ] Run report produced covering every section in scope

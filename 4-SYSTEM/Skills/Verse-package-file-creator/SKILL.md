---
name: Verse-package-file-creator
description: Extract four targeted commentary elements — story (གཏམ་རྒྱུད/སྒྲུང), extended information (ཞར་བྱུང), keyword explanation (ཚིག་འགྲེལ), and key-concept explanation (གནད་དོན) — for one verse of the Bodhisattvacaryāvatāra, by tracing the verse through its block-transclusion into one or more commentaries. Produces a focused Tibetan extraction file in 2-RAILS/Verses/. Use when the user names a verse and asks for its story / extended info / keyword / key-concept material from the commentaries, or asks to "trace the commentary through transclusion."
---

# Verse-package-file-creator

Builds a **focused four-element extraction** for one verse: it traces the verse from a `1-SOURCES/Translations/` (or `1-SOURCES/Text/`) root file into the commentary file(s) that transclude it, locates the commentary passage that comments on that verse, and pulls out exactly four kinds of material — **stories, extended information, keyword explanation, key-concept explanation** — each cited to the commentary block it came from.

This is a lighter, more targeted relative of [`verse-context`](../verse-context/SKILL.md). Where `verse-context` builds the full rail (Sanskrit + Tibetan source, per-commentary English paraphrase, AI Overview, chendrel, disambiguation, restatement, etc.), this skill produces only the four requested layers, in Tibetan, from the commentary as transcluded. Use this skill when the user asks specifically for those four elements; use `verse-context` when they want the complete verse package.

Authoritative schema for the full package: [`2-RAILS/About Rails.md`](../../../2-RAILS/About%20Rails.md) §5. Vault conventions (commentary IDs, addressing, languages): [`4-SYSTEM/Docs/vault-annex.md`](../../Docs/vault-annex.md). When this skill and `About Rails.md` disagree, **About Rails wins**.

---

## The four elements

| # | Element | Tibetan | What to extract |
|---|---|---|---|
| 1 | **Story** | གཏམ་རྒྱུད། / སྒྲུང་། | Narratives, parables, and illustrative similes the commentary attaches to the verse (e.g. the blind-turtle simile). Précis each in Tibetan; name it; say which phrase it illustrates. |
| 2 | **Extended information** | ཞར་བྱུང་གི་གནད་དོན། | Supplementary material the commentary adds beyond a bare gloss: enumerations (e.g. the 18 freedoms/endowments), supporting scriptural lists, reasoning structures (cause/example/number), context, and concluding advice. |
| 3 | **Keyword explanation** | ཚིག་གི་འགྲེལ་བཤད། (ཚིག་འགྲེལ) | The word-by-word gloss the commentary gives to the root verse's terms — in many Tibetan commentaries these are the bolded *mchan* tokens woven through the prose. Present as a term → gloss mapping, then the resolved meaning. |
| 4 | **Key-concept explanation** | གནད་དོན་གཙོ་བོའི་འགྲེལ་བཤད། | The governing doctrinal ideas of the passage (e.g. "the precious human support," "threefold rarity," "great purpose"), each explained in Tibetan from the commentary. |

---

## Language rule

- **All four element sections are written in Tibetan.** This matches the `2-RAILS/` convention that analysis is in Tibetan except cross-tradition English paraphrase (which this skill does not produce).
- **Quotations are verbatim Tibetan** — reproduce scripture/verse exactly as the commentary gives it; never translate scripture in the rail (that is a transformation's job).
- Tibetan section headers; element labels may carry a short English parenthetical for legibility.

---

## Inputs

- **Verse** — the verse text, or its verse ID (block ID without caret, e.g. `1-4`). Per-chapter numbering.
- **Root file** — the `1-SOURCES/Translations/<file>.md` (or `1-SOURCES/Text/<file>.md`) that carries the verse and its block ID. Used to confirm the block ID.
- **Commentary file(s)** — one or more `1-SOURCES/Commentaries/**.md` that **transclude** the verse. The skill traces the transclusion to find each commentary's passage on the verse. Use the `registered_id` from the vault annex to attribute every claim.
- **Output filename** — supplied by the user (e.g. `bo-བློ་ལྡན་ཤེས་རབ།V4`); the skill appends `.md`.

## Output

One file at `2-RAILS/Verses/<output-filename>.md`. Update in place if it exists; never overwrite hand-edited Tibetan without confirming the cited blocks still support it.

---

## Citation note — un-stamped commentary prose

Many raw/segmented commentaries (e.g. `BCAC19_KKP_bo_segmented`) carry block IDs **only on the transcluded verse anchors** (`^1-4`), not on the commentary prose itself. In that case:

- Cite every element to the **verse-transclusion anchor** in the commentary file: `[[1-SOURCES/Commentaries/<...>/<id>.md#^<verse-id>]]`.
- Record this in frontmatter (`note:`), because it is weaker than a true per-block citation.
- If the commentary prose **is** block-stamped, cite the specific prose blocks instead — always prefer the finest-grained citation available.

---

## Output file format

```markdown
---
title: "BCA <verse-id> — <commentary-id(s)> commentary extraction (story / extended info / keyword / key-concept)"
verse_id: "<verse-id>"
root_text: "1-SOURCES/Translations/<root-file>.md"
commentary: [<id>, <id>, …]
commentary_source: [1-SOURCES/Commentaries/<...>/<id>.md, …]
commentary_block: "^<verse-id>"
language: bo
analysis_language: bo
file_type: verse-context-extraction
status: draft
note: "<e.g. commentary prose is not block-ID-stamped; citations point to the verse-transclusion anchor.>"
---

# སྤྱོད་འཇུག <verse-id> པའི་འགྲེལ་བཤད་ནས་བཏོན་པ། (<commentary-id(s)>)

## རྩ་ཚིག (Root verse)

![[1-SOURCES/Translations/<root-file>.md#^<verse-id>]]

> <verse line 1>
> <verse line 2>
> …

**ས་བཅད།** <the commentary's structural label for this passage, if any.> ([[1-SOURCES/Commentaries/<...>/<id>.md#^<verse-id>]])

---

## ༡། གཏམ་རྒྱུད། (Story)

- **<story / simile name>** — <Tibetan précis; which phrase it illustrates.>
  ([[1-SOURCES/Commentaries/<...>/<id>.md#^<verse-id>]])

## ༢། ཞར་བྱུང་གི་གནད་དོན། (Extended information)

**<sub-topic, e.g. དལ་འབྱོར་བཅོ་བརྒྱད།>** <Tibetan explanation; verbatim list/quotation where the commentary gives one.>
([[1-SOURCES/Commentaries/<...>/<id>.md#^<verse-id>]])

## ༣། ཚིག་གི་འགྲེལ་བཤད། (Keyword explanation — ཚིག་འགྲེལ)

| རྩ་ཚིག་གི་ཚིག | འགྲེལ་བཤད་ནང་གི་གོ་དོན། |
|---|---|
| **<root word>** | <commentary's gloss, Tibetan> |
| … | … |

<resolved meaning of the verse as the keyword glosses yield it.>
([[1-SOURCES/Commentaries/<...>/<id>.md#^<verse-id>]])

## ༤། གནད་དོན་གཙོ་བོའི་འགྲེལ་བཤད། (Key-concept explanation)

**<concept>** <Tibetan explanation.>
([[1-SOURCES/Commentaries/<...>/<id>.md#^<verse-id>]])

### Divergences  ⚑   <only if multiple commentaries disagree>
- **<id>:** <position> ⚑
- **<id>:** <position> ⚑

---

## ཁུངས། (Source)

ཡིག་ཆ། `1-SOURCES/Commentaries/<...>/<id>.md` — རྩ་ཚིག་ ^<verse-id> ལ་གཞུང་སྦྱར་བའི་འགྲེལ་བཤད།
```

---

## Rules

1. **Only the four elements.** Story, extended information, keyword explanation, key-concept explanation. Do not add paraphrase, AI Overview, disambiguated restatement, or other `verse-context` layers — if the user wants those, use `verse-context`.
2. **Transclude the root verse; never paste it as authoritative.** Use `![[…#^<verse-id>]]`. A readable copy may sit beneath the transclusion as a `>` block-quote for convenience.
3. **Trace through the transclusion.** Find the verse's block ID in the root file, then `grep` for `#^<verse-id>` in each commentary file; the commentary passage is the prose immediately following that transclusion line, up to the next verse transclusion.
4. **Every element cites a `1-SOURCES/` block.** No parametric knowledge. Prefer per-prose-block citations; fall back to the verse-transclusion anchor when prose is un-stamped (and record this in `note:`).
5. **Faithful attribution.** Reproduce scriptural quotations verbatim; attribute each to the figure/text the commentary names (e.g. ཀླུ་སྒྲུབ, དཔལ་མར་མེ་མཛད) — do not "correct" the commentary's attribution.
6. **Omit empty elements.** If a commentary attaches no story, drop the Story section rather than writing an empty heading. (Optionally note "<element>: མི་འདུག" if the user asked for all four explicitly.)
7. **Multiple commentaries → merge, never flatten.** When more than one commentary is given, gather each element across all of them. Where they agree, present once. Where they genuinely disagree, keep both positions, mark each ⚑, and add a `### Divergences` block attributing every position to its `registered_id`.
8. **`status: draft` always.** The LLM never sets `complete`; a domain specialist does.

---

## Procedure

1. **Resolve the verse ID.** If given verse text, `grep` it in the root file to find its block ID; if given an ID, confirm the block exists in the root file.
2. **Locate the commentary passage(s).** For each commentary file, `grep -n "#^<verse-id>"` to find the transclusion line. The commentary on the verse is the prose from just after that line up to the next `![[…#^…]]` transclusion. Read that span.
3. **Check citation granularity.** Inspect whether the commentary prose carries its own block IDs. If not, plan to cite the verse-transclusion anchor and record it in `note:`.
4. **Extract element 1 — Story.** Identify narratives/parables/illustrative similes; précis each in Tibetan; name it; note the phrase it illustrates.
5. **Extract element 2 — Extended information.** Pull enumerations, supporting scriptural lists, reasoning structures, context, and concluding advice; quote lists verbatim.
6. **Extract element 3 — Keyword explanation.** Collect the commentary's word-level glosses (often the bolded *mchan* tokens); render as a term → gloss table; state the resolved meaning.
7. **Extract element 4 — Key-concept explanation.** State the governing doctrinal ideas, each explained from the commentary.
8. **Merge across commentaries** (if more than one): consolidate each element; add `### Divergences` ⚑ where they disagree.
9. **Fill frontmatter**, set `status: draft`, add the Source block.
10. **Write** to `2-RAILS/Verses/<output-filename>.md`.
11. **Verify** (see check below) — re-read the source span and confirm each extracted item is actually present and correctly cited.

---

## Completion check

- [ ] Verse ID resolved against the root file; root verse transcluded (not pasted as source).
- [ ] Each commentary passage located by tracing the `#^<verse-id>` transclusion.
- [ ] All four elements present (or explicitly omitted where the commentary supplies none).
- [ ] Story = précis of attested narratives only; no invented stories.
- [ ] Extended-information lists/quotations reproduced verbatim and attributed as the commentary names them.
- [ ] Keyword explanation reflects the commentary's actual glosses (e.g. the *mchan* tokens), not a fresh gloss.
- [ ] Key concepts traced to the commentary.
- [ ] Every element cites a `1-SOURCES/` block; un-stamped-prose fallback recorded in `note:`.
- [ ] Multiple commentaries merged, not flattened; ⚑ on every genuine divergence with a Divergences block.
- [ ] Frontmatter complete; `status: draft`.
- [ ] Final verification pass done: each item re-checked against the source span.

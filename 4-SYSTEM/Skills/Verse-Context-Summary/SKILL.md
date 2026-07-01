---
name: Verse-Context-Summary
description: Create a comprehensive verse-context-summary page for one verse of the Bodhisattvacaryāvatāra, assembling Sanskrit and Tibetan text transclusions, Zhenga's annotations, per-commentary explanations, stories, metaphors, scriptural quotations, main points, key terms, and a Google-AI-Overview-style synthesis. Output goes to 2-RAILS/Verses/<verse-id>-summary.md.
creator: Tigerboy
---

# Verse-Context-Summary

Assembles a **complete single-verse summary page** by pulling every layer of commentary material — text, annotation, explanation, story, metaphor, quotation, theme, term, and synthesis — into one cited document. The page is designed to be the canonical Obsidian reference for a verse: open it, and every relevant source-material layer is in front of you, cited and linked.

Authoritative vault conventions (commentary IDs, addressing, language rules): [`4-SYSTEM/Docs/vault-annex.md`](../Docs/vault-annex.md). Folder-write rules: [`4-SYSTEM/CLAUDE.md`](../CLAUDE.md). When this skill and those documents disagree, the referenced documents win.

---

## Inputs

- **Verse ID** — block ID without caret, e.g. `1-1`, `6-33`. Chapter-verse format; numbers are not zero-padded.
- **Sanskrit root text** — `1-SOURCES/Text/BCAV08_SH_sk.md`
- **Tibetan root text** — `1-SOURCES/Translations/bo-བློ་ལྡན་ཤེས་རབ།.md`
- **Commentary files** — all files under `1-SOURCES/Commentaries/Transcluded/`. The root text verses are already transcluded into every commentary file in this folder. Use the `registered_id` from the vault annex to attribute every claim. Tier order (lead → follow): `prajnakaramati` → `kunpal` → `mipham` → `khenpo-zhengah` → `gyaltsab` → other Tibetan → Chinese.
- **Zhenga mchan-'grel** — `1-SOURCES/Commentaries/Transcluded/BCAC19_KS_bo.md` (registered_id: `khenpo-zhengah`). Sole source for the མཆན་འགྲེལ། section.

---

## How to locate a verse's commentary passage

Every commentary file in `1-SOURCES/Commentaries/Transcluded/` has the root text verses transcluded into it using Obsidian syntax. The commentary on a verse is always the text that sits between that verse's transclusion and the next verse's transclusion.

**Step-by-step:**

1. `grep -n "!\\[\\[.*#\\^<verse-id>\\]\\]"` in each commentary file to find the transclusion line, e.g. `![[bo-བློ་ལྡན་ཤེས་རབ།.md#^1-1]]`.
2. Note the line number of that transclusion (`LINE_START`) and the line number of the next verse transclusion (`LINE_END`).
3. Read only the span from `LINE_START` to `LINE_END − 1`. **Do not read the entire file.** Everything in that span is the commentary on the target verse.
4. Extract all relevant material — explanations, stories, metaphors, quotations, term glosses — from that span alone.
5. Repeat for every commentary file in `1-SOURCES/Commentaries/Transcluded/`.

This targeted read replaces any need to scan full commentary files. Apply it identically to `BCAC19_KS_bo.md` for the མཆན་འགྲེལ། section.

## Output

One file at `2-RAILS/Verses/<verse-id>-summary.md`. Update in place if it exists; never overwrite a hand-edited section without confirming the edit is still supported by the cited blocks.

---

## Language rule

- **ལེགས་སྦྱར།** — Sanskrit (Devanāgarī), verbatim transclusion only.
- **བོད་ཡིག** — Tibetan, verbatim transclusion only.
- **མཆན་འགྲེལ། through གནད་ཚིག** — Tibetan throughout. No translation of source quotations; that is a transformation's job.
- **བསྡུས་དོན།** — Tibetan synthesis. Mirror the AI-Overview register: short sentences, leading claim first, cited bullets.
- Source links at the close of every section use the inline form `([[path/to/file.md#^block-id]])`.

---

## Output file format

```markdown
---
verse_id: "<verse-id>"
skill: Verse-Context-Summary
creator: Tigerboy
sources:
  sanskrit: "1-SOURCES/Text/BCAV08_SH_sk.md"
  tibetan: "1-SOURCES/Translations/bo-བློ་ལྡན་ཤེས་རབ།.md"
  mchan_grel: "1-SOURCES/Commentaries/Transcluded/BCAC19_KS_bo.md"
  commentaries: [<id>, <id>, …]
status: draft
---

# སྤྱོད་འཇུག <verse-id>པའི་ཤོག་ངོས།

## ལེགས་སྦྱར། (Sanskrit)

![[1-SOURCES/Text/BCAV08_SH_sk.md#^<verse-id>]]

→ [[1-SOURCES/Text/BCAV08_SH_sk.md#^<verse-id>]]

---

## བོད་ཡིག (Tibetan — བློ་ལྡན་ཤེས་རབ།)

![[1-SOURCES/Translations/bo-བློ་ལྡན་ཤེས་རབ།.md#^<verse-id>]]

→ [[1-SOURCES/Translations/bo-བློ་ལྡན་ཤེས་རབ།.md#^<verse-id>]]

---

## མཆན་འགྲེལ། (གཞན་དགའི་མཆན་འགྲེལ)

<Verbatim annotation text from Khenpo Zhenga's mchan-'grel for this verse. If the commentary interleaves its annotation with the root words, reproduce the full annotated passage. Present as a single prose block or as the annotated pairs (root word → gloss) as the source gives them.>

→ ([[1-SOURCES/Commentaries/Transcluded/BCAC19_KS_bo.md#^<block-id>]])

---

## དོན་འགྲེལ། (Commentary explanations)

### <registered_id> — <Author Tibetan name> (<short title>)

<Tibetan prose: the commentary's principal explanation of the verse's meaning. One subsection per commentary, in tier order. Quote or closely paraphrase the source; do not invent. Each claim ends with its block citation.>

([[1-SOURCES/Commentaries/<...>/<id>.md#^<block>]])

### <registered_id> — <Author Tibetan name> (<short title>)

…

### ⚑ བར་འབྱོར་གྱི་མི་མཐུན་པ། (Divergences)
<Only present when commentaries genuinely disagree. Attribute each position to its registered_id; mark each with ⚑.>
- **<id>:** <position> ⚑
- **<id>:** <position> ⚑

---

## སྒྲུང་འགྲེལ། (Stories and narratives)

### <registered_id> — <story name>

<Tibetan précis of the narrative or parable the commentary attaches to this verse. Name the story; note which line or phrase it illustrates. One block per story per commentary, in tier order.>

([[1-SOURCES/Commentaries/<...>/<id>.md#^<block>]])

<Omit this section entirely if no commentary attaches a narrative to the verse.>

---

## དཔེ། (Metaphors and examples)

- **<image/example>** → <tenor — what the example illustrates.>
  <How the commentary develops the comparison; any explicit application statement.>
  ([[1-SOURCES/Commentaries/<...>/<id>.md#^<block>]])

<One bullet per attested metaphor, in tier order. Omit if absent in all commentaries.>

---

## ལུང་། (Scriptural quotations)

> <Verbatim Tibetan quotation>
> — <Scripture name as the commentary gives it> (<commentary's gloss on the quotation, if any>)

([[1-SOURCES/Commentaries/<...>/<id>.md#^<block>]])

<One block per distinct quotation, attributed to the scripture the commentary names and to the commentary block that adduces it. Reproduce verbatim; do not correct or smooth. Omit if no commentary adduces a quotation.>

---

## གཙོ་གནད། (Main teaching points)

<Ordered list of the verse's principal doctrinal or practical themes, synthesised across all commentaries used. Each item is one teaching point in Tibetan, followed by a brief expansion and its source citation(s). Order from the verse's most central claim outward.>

1. **<teaching point>** — <Tibetan expansion, 1–3 sentences.>
   ([[1-SOURCES/Commentaries/<...>/<id>.md#^<block>]])

2. **<teaching point>** — …

<Minimum two points; maximum eight. Every point must be traceable to at least one cited block.>

---

## གནད་ཚིག (Key terms)

| གནད་ཚིག | འགྲེལ་བཤད་ (Commentary definition) | ཁུངས། (Source) |
|---|---|---|
| **<Tibetan term>** | <Commentary's own gloss in Tibetan> | ([[1-SOURCES/Commentaries/<...>/<id>.md#^<block>]]) |
| … | … | … |

<Include every term the commentaries explicitly define or gloss for this verse. Use the commentary's own definition verbatim or near-verbatim — do not substitute a dictionary entry. Omit terms glossed only by obvious paraphrase that adds nothing.>

---

## བསྡུས་དོན། (Verse synthesis — AI Overview style)

**ངོ་སྤྲོད་མདོར་བསྡུས།** <One or two Tibetan sentences stating the settled reading of the verse as the commentaries collectively understand it. Lead with the conclusion, the way a Google AI Overview opens with the direct answer. Neutral synthetic voice; no "commentary X says." End with citations.>
([[1-SOURCES/Commentaries/<...>/<id>.md#^<block>]])

**གནད་དོན་གཙོ་བོ།**
- <Key point 1 — short, scannable, Tibetan. One idea per bullet.> ([[...#^<block>]])
- <Key point 2> ([[...#^<block>]])
- <Key point 3> ([[...#^<block>]])
- <Key point 4 — if the commentaries disagree on a point, say so and mark ⚑, citing both sides.> ⚑ ([[...#^<block>]]) ([[...#^<block>]])

<Three to six bullets. Every bullet cites the block(s) it draws on. Synthesise; do not introduce any claim that is not already attested in the sections above.>
```

---

## Rules

1. **Transclusions, not copies.** ལེགས་སྦྱར། and བོད་ཡིག use `![[…#^<verse-id>]]` only. Never paste the verse text as if it were the authoritative source. A readable `>` quote-block may follow the transclusion for convenience, but the transclusion is the citation.
2. **མཆན་འགྲེལ། from Zhenga only.** This section draws exclusively from `khenpo-zhengah`. Do not blend other commentaries into it.
3. **དོན་འགྲེལ། is ordered by tier.** Lead with `prajnakaramati` (if it addresses the verse), then Tibetan scholarly commentaries in the tier order given above, then supplementary, then Chinese. One subsection per commentary per voice.
4. **སྒྲུང་འགྲེལ། is a standalone section.** Populated from attested narratives only. If no commentary attaches a story or parable to this verse, omit the section entirely — do not write an empty heading or a placeholder.
5. **དཔེ། is a standalone section.** Populated from attested metaphors and examples only. If no commentary supplies a metaphor for this verse, omit the section entirely.
6. **ལུང། is a standalone section.** Populated from attested scriptural quotations only. If no commentary adduces a quotation for this verse, omit the section entirely.
7. **གཙོ་གནད། is ordered by centrality**, not by commentary order. The most essential doctrinal claim of the verse comes first.
8. **གནད་ཚིག uses the commentary's own gloss.** Never substitute a general dictionary definition. If two commentaries gloss the same term differently, add a second row with the second gloss and its source, and mark both ⚑.
9. **བསྡུས་དོན། is strictly derived.** Every claim must be traceable to something already written in the sections above. This is a compression, not an expansion; no new interpretive material enters here.
10. **Every claim cites a `1-SOURCES/` block.** No parametric knowledge. An uncitable claim is left blank; `status: draft` remains until a domain specialist clears it.
11. **Divergences are never flattened.** When commentaries disagree, record both positions, cite each, and mark ⚑.
12. **`status: draft` always.** The LLM never sets `complete`; a domain specialist does.

---

## Procedure

1. **Confirm the verse ID.** Verify block `^<verse-id>` exists in `1-SOURCES/Text/BCAV08_SH_sk.md` and in `1-SOURCES/Translations/bo-བློ་ལྡན་ཤེས་རབ།.md`. If either is absent, stop and fix the source file first.
2. **Write ལེགས་སྦྱར།** — insert the Sanskrit transclusion `![[1-SOURCES/Text/BCAV08_SH_sk.md#^<verse-id>]]` and its inline link.
3. **Write བོད་ཡིག** — insert the Tibetan transclusion `![[1-SOURCES/Translations/bo-བློ་ལྡན་ཤེས་རབ།.md#^<verse-id>]]` and its inline link.
4. **Locate and read each commentary's verse span.** For every file in `1-SOURCES/Commentaries/Transcluded/`:
   - `grep -n "!\\[\\[.*#\\^<verse-id>\\]\\]"` to find the transclusion line.
   - Note that line number (`LINE_START`) and the line number of the next verse transclusion (`LINE_END`).
   - Read only lines `LINE_START` to `LINE_END − 1`. This span is the complete commentary on the target verse. Do not read beyond it.
   - Record the commentary's `registered_id` and the block IDs of any stamped blocks in the span.
5. **Write མཆན་འགྲེལ།** — from the `BCAC19_KS_bo.md` span only: reproduce the annotation verbatim or as annotated pairs (root word → gloss); cite the block.
6. **Write དོན་འགྲེལ།** — one subsection per commentary in tier order, drawn from each commentary's verse span; Tibetan prose; every sentence cited. Add Divergences ⚑ if any.
7. **Write སྒྲུང་འགྲེལ།** — from the verse spans: identify narratives across all commentaries; précis each in Tibetan; note the illustrating phrase; cite. Omit section entirely if no narrative found.
8. **Write དཔེ།** — from the verse spans: collect metaphors and examples; state image → tenor → how the commentary develops it; cite. Omit if absent.
9. **Write ལུང།** — from the verse spans: extract verbatim quotations; attribute to the scripture the commentary names; cite the commentary block. Omit if absent.
10. **Write གཙོ་གནད།** — synthesise the main teaching points across all verse spans; order by centrality; cite each.
11. **Write གནད་ཚིག** — fill the table from the commentaries' own glosses found in the verse spans; ⚑ on diverging definitions.
12. **Write བསྡུས་དོན།** — compose the AI-Overview-style synthesis strictly from the material already written above; lead with the settled reading; cite all key bullets.
13. **Fill frontmatter**; set `status: draft`.
14. **Write** to `2-RAILS/Verses/<verse-id>-summary.md`.
15. **Verification pass** — re-read each section against the source verse spans and confirm every cited item is actually present in the cited block and correctly attributed.

---

## Completion check

- [ ] Frontmatter complete with `verse_id`, `skill: Verse-Context-Summary`, `creator: Tigerboy`, `sources`, `status: draft`.
- [ ] **ལེགས་སྦྱར།**: Sanskrit transclusion present and block confirmed; inline source link.
- [ ] **བོད་ཡིག**: Tibetan transclusion present and block confirmed; inline source link.
- [ ] **མཆན་འགྲེལ།**: drawn from `khenpo-zhengah` only; verbatim annotation; block cited.
- [ ] **དོན་འགྲེལ།**: one subsection per commentary in tier order; every claim cited; Divergences ⚑ where present.
- [ ] **སྒྲུང་འགྲེལ།**: attested narratives only, précised in Tibetan, cited; section omitted if no material.
- [ ] **དཔེ།**: attested metaphors only, image→tenor→development, cited; section omitted if no material.
- [ ] **ལུང།**: verbatim Tibetan quotations, attributed to scripture named by commentary, commentary block cited; section omitted if no material.
- [ ] **གཙོ་གནད།**: ordered by centrality, Tibetan, every point cited; minimum two, maximum eight.
- [ ] **གནད་ཚིག**: commentary-own glosses; ⚑ on diverging definitions; no dictionary substitutions.
- [ ] **བསྡུས་དོན།**: AI-Overview style; lead claim first; bullets scannable; every claim traceable to sections above; ⚑ on splits cited both sides.
- [ ] Source link (inline `([[…]])`) at the end of every section.
- [ ] No section left as an empty heading — omit entirely if no material.
- [ ] Verification pass completed: each item re-checked against its cited source span.

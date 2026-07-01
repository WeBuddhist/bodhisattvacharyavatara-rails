---
name: verse-context
description: Build the verse-level context package for one verse of the Bodhisattvacaryāvatāra. Transcludes the Sanskrit and Tibetan root verse, paraphrases each commentary's reading (English), then compiles the Tibetan descriptive layers the transformations consume — an AI-Overview synthesis, a chendrel (ཚིག་འགྲེལ) word-commentary, word-by-word disambiguation, key concepts, attached stories, metaphors, scriptural quotations, and a disambiguated restatement. Output goes to 2-RAILS/Verses/<verse-id>.md.
---

# verse-context

Produces the **verse-level descriptive context** that every downstream transformation (translation, adaptation, study plan) works from. The translator never sees the bare verse: it sees the disambiguated restatement plus the chendrel, the concepts, the stories, and the cited synthesis. This is the rail that defuses hallucination — every interpretive decision is made and cited here, once, before any output is generated.

Authoritative schema: [`2-RAILS/About Rails.md`](../../../2-RAILS/About%20Rails.md) §5. Vault conventions (commentary IDs, language tracks, addressing): [`4-SYSTEM/Docs/vault-annex.md`](../../Docs/vault-annex.md). When this skill and `About Rails.md` disagree, **About Rails wins**.

---

## Language rule

- **Traditional Interpretation** — English paraphrase, one subsection per commentary.
- **Every other section is in Tibetan**: AI Overview, Chendrel, Word-by-word Disambiguation, Key Concepts, Stories, Metaphors, Quotations, and the Disambiguated Restatement.
- Quotations are verbatim Tibetan. Never translate scripture in the rail — that is a transformation's job.

This follows the vault-annex convention: the primary analysis language for `2-RAILS/` is Tibetan; only the cross-tradition paraphrase is held in English so coverage is legible at a glance.

---

## Inputs

- **Verse ID** — block ID of the verse, no caret (e.g. `1-1`, `6-33`). Per-chapter numbering.
- **Sanskrit root** — `1-SOURCES/Text/BCAV08_SH_sk.md#^<verse-id>`.
- **Tibetan root** — `1-SOURCES/Text/<bo-root-text>.md#^<verse-id>` (transclude; if the Tibetan root-text file does not yet carry this block, the Tibetan verse must be added to a root-text file under `1-SOURCES/Text/` first — do not paste the verse into the rail).
- **Commentary files** — every relevant file under `1-SOURCES/Commentaries/Transcluded/`. For this verse, prefer:
  - a **word-commentary / annotation** (*mchan-'grel*) source for the Chendrel and disambiguation (e.g. `BCAC19_KS_bo`);
  - **story commentaries** (*gtam-rgyud* / *sgrung-'grel*) for the Stories (e.g. `BCACXX_WR_bo`, `BCAC13_KTB_bo`);
  - scholarly commentaries for the paraphrase and concepts.
  Use the `registered_id` from the vault annex to attribute every claim.

## Output

One file at `2-RAILS/Verses/<verse-id>.md`. Update in place if it exists; never overwrite a hand-edited Tibetan section without confirming the edit is still supported by the cited blocks.

---

## Output file format

```markdown
---
ref: <e.g. 1-1-ref>
unit_type: single | group | template | instance
unit_verses: [<verse-id>]
commentary_coverage: [<id>, <id>, …]
tradition_coverage: [<tradition>, …]
concepts_in_verse: [<བོད་སྐད་ term> (gloss), …]
concepts_in_commentary: [<བོད་སྐད་ term> (gloss), …]
stories: [<story name>, …]
layer_order: [traditional, ai-overview, chendrel, word-disambiguation, concepts, stories, metaphors, quotations]
status: draft
---

## Source Text

### Sanskrit
![[1-SOURCES/Text/BCAV08_SH_sk.md#^<verse-id>]]

### Tibetan
![[1-SOURCES/Text/<bo-root-text>.md#^<verse-id>]]

**Variants**
[Ed: …]

## Traditional Interpretation

### <id> — <Commentary full name> (<language>)
<English paraphrase; every claim cited.>
(1-SOURCES/Commentaries/<id>.md#^<block>)

### Divergences
<only where commentaries genuinely disagree; each position attributed, ⚑.>

## AI Overview (བསྡུས་དོན།)

**ངོ་སྤྲོད་མདོར་བསྡུས།** <one–two Tibetan sentences: what the verse says.>
(1-SOURCES/Commentaries/<id>.md#^<block>)

**གནད་དོན་གཙོ་བོ།**
- <key point, Tibetan> (1-SOURCES/Commentaries/<id>.md#^<block>)
- <key point, Tibetan> (1-SOURCES/Commentaries/<id>.md#^<block>)

## Chendrel — ཚིག་འགྲེལ

<running Tibetan word-commentary: each phrase of the root verse with its gloss
woven inline, mchan-'grel style.>
(1-SOURCES/Commentaries/<mchan-grel-id>.md#^<block>)

## Word-by-word Disambiguation (ཚིག་དོན་གསལ་བཤད།)

- **<root word/phrase>** — <Tibetan disambiguating gloss.>
  (1-SOURCES/Commentaries/<id>.md#^<block>)

## Key Concepts (ཆོས་ཀྱི་གནད་ཚིག)

### ཚིགས་བཅད་ནང་གི་གནད་ཚིག
- **<term>** (<gloss>) — <Tibetan note.>
  (1-SOURCES/Commentaries/<id>.md#^<block>) · [[2-RAILS/Local-Wiki/<term>_(<disambiguator>).md]]

### འགྲེལ་པ་ནས་འབྱུང་བའི་གནད་ཚིག
- **<term>** (<gloss>) — <Tibetan note.>
  (1-SOURCES/Commentaries/<id>.md#^<block>) · [[2-RAILS/Local-Wiki/<term>_(<disambiguator>).md]]

## Stories (སྒྲུང་།)

- **<story name>** — <Tibetan précis; which phrase it illustrates.>
  (1-SOURCES/Commentaries/<story-id>.md#^<block>)

## Metaphors (དཔེ།)

- **<image>** → <tenor.> <how the commentary develops it.>
  (1-SOURCES/Commentaries/<id>.md#^<block>)

## Quotations (ལུང་།)

> <verbatim Tibetan scripture>
> — <scripture as named by the commentary>
> (1-SOURCES/Commentaries/<id>.md#^<block>)

## Disambiguated Restatement (Tibetan)

<short Tibetan rewrite of the verse with every ambiguity the synthesis
resolved made explicit. Cite the blocks that authorise each choice.>
(1-SOURCES/Commentaries/<id>.md#^<block>)

## Concept Links
- [[2-RAILS/Local-Wiki/<term>_(<disambiguator>).md]]
```

---

## Rules

1. **Required sections always present:** Source Text, Traditional Interpretation, AI Overview, Disambiguated Restatement. The rest are populated where the commentaries supply material and **omitted otherwise** (a verse with no attached story drops the Stories section — do not write an empty heading).
2. **Both languages in Source Text.** Transclude the Sanskrit and the Tibetan root blocks; never copy them. If a block ID is missing in a root-text file, fix the root text first.
3. **Traditional Interpretation is the cited anchor.** The AI Overview is its Tibetan compression — every claim in the Overview must trace to a paraphrase that is itself cited. Do not introduce a claim in the Overview that is not in Traditional Interpretation.
4. **Chendrel uses a word-commentary source.** It is not your own gloss — it re-presents an attested *mchan-'grel* / annotation reading as running word-commentary, cited to its blocks.
5. **Word-by-word disambiguation only for non-obvious choices** — sense selection, compound parsing, referent. Skip obvious tokens.
6. **Stories are précis, not invention.** Only narratives a commentary actually attaches to the verse; name the story and cite the block.
7. **Quotations are verbatim and attributed.** Reproduce the Tibetan as the commentary gives it; name the scripture the commentary names; cite the commentary block that adduces it.
8. **Every claim cites a `1-SOURCES/` block.** No parametric knowledge. Uncited field → leave blank, `status: draft`.
9. **Divergences are never flattened.** ⚑ each position; the Disambiguated Restatement follows the best-attested reading and footnotes the alternatives.
10. **`status: draft` always.** The LLM never sets `complete`; a domain specialist does.

---

## Procedure

1. Read the Sanskrit and Tibetan root blocks. Confirm both block IDs exist; if the Tibetan root file lacks the block, stop and fix the root text.
2. **Locate verse commentary in each Transcluded file** — do not read the whole file. Root text verses are transcluded into the commentary files with the Obsidian syntax `![[...#^<verse-id>]]`. Search each file in `1-SOURCES/Commentaries/Transcluded/` for the transclusion of the target verse's block ID. All text from that transclusion up to (but not including) the next transclusion is commentary on that verse. Read only that span and record the block IDs and `registered_id`.
3. Write **Traditional Interpretation** — one English subsection per commentary, each claim cited. Add **Divergences** if any.
4. Write the **AI Overview** in Tibetan from the paraphrases (see prompt below).
5. Build the **Chendrel** from the annotation source; **Word-by-word Disambiguation** for non-obvious tokens.
6. Fill **Key Concepts** (in-verse / from-commentary), **Stories**, **Metaphors**, **Quotations** — each from a cited block; omit any section with no material.
7. Write the **Disambiguated Restatement** in Tibetan.
8. Fill frontmatter; set `status: draft`. Add **Concept Links**.
9. Write to `2-RAILS/Verses/<verse-id>.md`.

---

## AI Overview — generation prompt

The AI Overview reproduces the experience of a Google "AI Overview" answer box, in Tibetan, over the commentary corpus. Generate it with this prompt:

> You are compiling the **AI Overview** block for one verse package. Your only
> sources are the per-commentary paraphrases already written in this file's
> **Traditional Interpretation** section, each of which is cited to a
> `1-SOURCES/` block. Do not use any knowledge outside those paraphrases.
>
> Write in **Tibetan**. Produce, in this order:
>
> 1. **ངོ་སྤྲོད་མདོར་བསྡུས། (the direct answer)** — one or two sentences that
>    answer "what does this verse say?" as the commentaries collectively read
>    it. Lead with the conclusion, the way an AI Overview opens with the
>    answer before the detail. Neutral, synthetic voice — not "commentary X
>    says," but the settled reading. End the sentence(s) with the source
>    citation(s) they rest on.
>
> 2. **གནད་དོན་གཙོ་བོ། (key points)** — three to six short bullets, each a
>    single scannable idea (a referent fixed, a term's sense chosen, the
>    verse's function in the chapter, a concept introduced). Each bullet ends
>    with the `(1-SOURCES/Commentaries/<id>.md#^<block>)` source(s) it draws
>    on — the inline-citation feel of an AI Overview's linked snippets. Where
>    a point aggregates several commentaries, cite all of them.
>
> Constraints matching the AI-Overview style:
> - **Synthesise, attribute by citation.** The prose reads as one voice;
>   attribution lives in the trailing source links, not in the sentence.
> - **Lead with the answer, keep it skimmable.** Short sentences, short
>   bullets, no throat-clearing.
> - **Surface disagreement, don't hide it.** If the commentaries split on a
>   point, say so in that bullet and mark it ⚑, citing each side — an AI
>   Overview flags "it depends," it does not fabricate consensus.
> - **Every claim is grounded.** If a statement cannot be traced to a cited
>   paraphrase above, cut it.

---

## Completion check

- [ ] Frontmatter complete; `status: draft`.
- [ ] Source Text transcludes both Sanskrit and Tibetan (not copied).
- [ ] Traditional Interpretation: one English subsection per commentary, every sentence cited; Divergences ⚑ where they exist.
- [ ] AI Overview in Tibetan: direct answer + key points, every line cited, ⚑ on splits, nothing beyond the paraphrases above.
- [ ] Chendrel drawn from a cited word-commentary source (or section omitted).
- [ ] Word-by-word disambiguation only for non-obvious tokens, each cited.
- [ ] Key Concepts: in-verse and from-commentary, cited and Local-Wiki-linked.
- [ ] Stories / Metaphors / Quotations populated from cited blocks, omitted where absent; quotations verbatim Tibetan.
- [ ] Disambiguated Restatement in Tibetan, each choice cited.
- [ ] Concept Links present for every key term.

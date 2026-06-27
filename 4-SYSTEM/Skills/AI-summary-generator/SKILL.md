---
name: AI-summary-generator
description: Generate the scholarly "AI Overview" synthesis layer for one verse of the Bodhisattvacaryāvatāra in Tibetan, drawing only on that verse's already-cited Traditional Interpretation paraphrases. Synthesises multiple commentaries into a neutral, structured overview — core synthesis, key themes, divergences, and practical application — with every claim grounded in a 1-SOURCES block citation. Writes the AI Overview section of 2-RAILS/Verses/<verse-id>.md.
---

# AI-summary-generator

Produces the **AI Overview** layer of a verse rail: a structured, scholarly synthesis that reads like a Google "AI Overview" answer box over the traditional commentary corpus. It compresses the per-commentary readings already compiled in the verse package into one neutral voice, while keeping strict source attribution and never flattening genuine disagreement. The output is Tibetan and lives inside the verse rail file, so every transformation downstream sees one cited synthesis rather than raw commentary.

This skill is the focused, richer counterpart of the AI-Overview step inside `verse-context`. Use it to (re)generate just the AI Overview section — for example after new commentaries are added to a verse, or to upgrade a thin overview to the full four-part structure. It does not touch any other layer of the rail.

Authoritative schema for the verse rail: [`2-RAILS/About Rails.md`](../../../2-RAILS/About%20Rails.md) §5. When this skill and `About Rails.md` disagree, **About Rails wins**. Commentary IDs and conventions: [`4-SYSTEM/Docs/vault-annex.md`](../../Docs/vault-annex.md).

---

## Inputs

- **Verse ID** — block ID of the target verse, no caret (e.g. `1-1`, `6-33`).
- **Verse rail file** — `2-RAILS/Verses/<verse-id>.md`. Its **Traditional Interpretation** section (one cited English paraphrase per commentary, plus any Divergences) is the **only** source of substance for this skill. If that section is empty or missing, stop and run `verse-context` first — this skill never reads `1-SOURCES/` directly and never adds claims that are not already present and cited in Traditional Interpretation.

If the verse file does not exist or has no Traditional Interpretation, stop and report; do not fabricate.

## Output

The **AI Overview (བསྡུས་དོན།)** section of `2-RAILS/Verses/<verse-id>.md`, written or replaced in place. No other section of the file is modified. No new file is created.

---

## Output file format

The AI Overview section is replaced with the following structure. Headings are Tibetan; every claim ends with the `(1-SOURCES/Commentaries/<id>.md#^<block>)` citation(s) it rests on — these are the vault equivalent of the `[Commentary_A]` anchors. Sections with no attested material (e.g. no divergence, no practice instruction) are **omitted**, not left empty.

```markdown
## AI Overview (བསྡུས་དོན།)

**ངོ་སྤྲོད་མདོར་བསྡུས། (Core Synthesis)**
<two to three Tibetan sentences: the verse's primary message and the general
consensus among the commentators, in one neutral synthetic voice.>
(1-SOURCES/Commentaries/<id>.md#^<block>)

### ཆོས་དོན་གཙོ་བོ། (Key Philosophical Themes)
- **<theme name>** — <one–two Tibetan sentences unpacking how the commentaries
  develop this theme.> (1-SOURCES/Commentaries/<id>.md#^<block>)
- **<theme name>** — <…> (1-SOURCES/Commentaries/<id>.md#^<block>, 1-SOURCES/Commentaries/<id2>.md#^<block>)

### མི་མཐུན་པའི་འགྲེལ་བཤད། (Divergences & Varied Interpretations) ⚑
- **<term or concept>** — <explicitly contrast the readings: where one
  commentary glosses X, another reads Y.> (1-SOURCES/Commentaries/<id-A>.md#^<block>; 1-SOURCES/Commentaries/<id-B>.md#^<block>)

### ཉམས་ལེན་གྱི་གདམས་ངག (Practical Application / Meditation Advice)
- <how the commentaries suggest applying the verse to mind-training, conduct,
  or meditative practice, Tibetan.> (1-SOURCES/Commentaries/<id>.md#^<block>)
```

---

## Rules

1. **Strict grounding.** Use only the paraphrases (and Divergences) already written in this verse file's Traditional Interpretation section. No parametric knowledge, no external history, lineage, or doctrine. If a statement cannot be traced to a cited paraphrase above, cut it.
2. **Citation on every claim.** Every factual claim, interpretation, or gloss ends immediately with its source link(s). When commentators agree, cite them together. The synthetic prose carries one voice; attribution lives in the trailing citations, never in the sentence ("commentary X says…" is wrong style; the cited link is the attribution).
3. **Never resolve disagreements by choosing a winner.** Where commentaries split on a term, metaphor, or level of meaning (e.g. relative vs. ultimate), contrast the positions explicitly, attribute each side, and mark the section ⚑. Do not fabricate consensus.
4. **Tibetan output, scholarly neutral tone.** All overview prose is Tibetan. Respectful, objective, classical register; do not water down or modernise Buddhist terminology unnecessarily. Lead with the answer, keep bullets skimmable.
5. **Replace only the AI Overview section.** Do not edit Source Text, Traditional Interpretation, Chendrel, or any other layer. Do not alter the verse file's frontmatter except, if present, leave `status` as it was (the LLM never sets `complete`).
6. **Omit empty sections.** Drop Divergences when commentaries agree; drop Practical Application when no commentary attaches practice instruction. Never write an empty heading.
7. **Do not modify any file in `1-SOURCES/`.**

---

## Procedure

1. Read `2-RAILS/Verses/<verse-id>.md`. Locate the **Traditional Interpretation** section and read every per-commentary paraphrase and any Divergences, noting the `1-SOURCES/Commentaries/<id>.md#^<block>` citation attached to each claim. If this section is empty or absent, stop and report — run `verse-context` first.
2. Identify the **settled reading** the commentaries collectively give the verse, and draft the **Core Synthesis** (2–3 Tibetan sentences), ending with the citations it rests on.
3. Extract two or more **Key Philosophical Themes**; for each, write a 1–2 sentence Tibetan unpacking grounded in the cited paraphrases.
4. Scan for genuine disagreement. For each, write a **Divergences** bullet that contrasts the positions and attributes each side; mark the section ⚑. Omit the section entirely if there is no disagreement.
5. If any commentary attaches mind-training, conduct, or meditation guidance, summarise it under **Practical Application**. Omit if none.
6. Assemble the section using the Output file format, in the heading order shown.
7. Replace the existing **AI Overview (བསྡུས་དོན།)** section of the verse file in place (insert it after Traditional Interpretation if absent). Leave all other sections and the frontmatter untouched.
8. Re-read the written section: confirm every line carries a citation that exists in Traditional Interpretation, and that no uncited claim slipped in.

---

## Core generation prompt

Feed the verse file's Traditional Interpretation section as the source corpus, then run:

> You are an expert scholar of Buddhist literature and classical exegesis,
> generating the **AI Overview** synthesis for one root verse of the
> Bodhisattvacaryāvatāra. Your ONLY sources are the per-commentary paraphrases
> in this verse file's **Traditional Interpretation** section, each cited to a
> `1-SOURCES/` block. Treat each cited paraphrase as a distinct commentator;
> the trailing `(1-SOURCES/Commentaries/<id>.md#^<block>)` link is its identity
> anchor.
>
> CRITICAL INSTRUCTIONS:
> 1. STRICT GROUNDING — base the overview only on those paraphrases. Invent no
>    external history, lineage, or doctrine.
> 2. CITATION — every claim, interpretation, or gloss is immediately followed by
>    its source link. If several commentators agree, cite them together.
> 3. RESOLVING DISAGREEMENTS — never choose a winner. Where they disagree on a
>    term, metaphor, or level of meaning, contrast the views explicitly ("where
>    [source A] glosses X, [source B] reads Y") and mark ⚑.
> 4. TONE — respectful, neutral, objective, scholarly. Do not water down
>    classical terminology.
>
> Write in **Tibetan**, in this exact structure (omit any section with no
> attested material):
>
> **Core Synthesis** — 2–3 sentences on the verse's primary message and the
> general consensus.
> **Key Philosophical Themes** — bulleted; each a named theme with a 1–2
> sentence cited unpacking.
> **Divergences & Varied Interpretations** — bulleted; each a named term/concept
> with the contrasted readings, attributed and ⚑.
> **Practical Application / Meditation Advice** — how the commentaries suggest
> applying the verse to mind-training, conduct, or meditation.

When this skill is used inside a backend RAG pipeline rather than over an existing rail file, the same system prompt applies; supply the input data as a Root Verse plus a list of commentaries, each with a unique ID, Author/Source, and Text, and have the model attribute by that ID. Inside this vault the unique ID is always the `1-SOURCES` block link.

---

## Completion check

- [ ] Read the verse file's Traditional Interpretation; did not read `1-SOURCES/` directly.
- [ ] AI Overview section written in Tibetan with Core Synthesis + Key Themes (+ Divergences / Practical Application where attested).
- [ ] Every claim ends with a `1-SOURCES/Commentaries/<id>.md#^<block>` citation that exists in Traditional Interpretation; no uncited claim added.
- [ ] Disagreements contrasted and ⚑-marked, never flattened into false consensus.
- [ ] Empty sections omitted, not left as bare headings.
- [ ] Only the AI Overview section changed; all other layers and the frontmatter untouched; `status` not set to `complete`.

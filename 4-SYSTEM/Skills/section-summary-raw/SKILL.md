---
name: section-summary-raw
description: Generate an original-language summary of one TOC node, drawn from a single commentary, into 2-RAILS/Sections/Raw/<commentary-name>/<node-id>.md. Use the commentary's own terminology without translating it. Every claim cites a block ID from the source.
---

# section-summary-raw

This skill produces the **per-commentary, original-language summary** of one node in the text's table of contents. One commentary per file. No translation, no paraphrase outside the commentary's own vocabulary, and every claim grounded in a block-ID citation.

The output of this skill is the raw input that `section-summary-combined` later merges across commentaries.

---

## Inputs

- **Commentary file** — one file from `1-SOURCES/Commentaries/<commentary-name>.md`. Must be properly formatted with heading IDs and block IDs (see `4-SYSTEM/Guidelines/source-formatting.md`).
- **TOC node** — the node-ID and heading text of the section to summarise (e.g. `^1-1-0` "Ganthārambhakathā"). The node corresponds to a heading in the commentary file.

If multiple commentaries cover the same node, run this skill once per commentary.

## Output

One file at:

```
2-RAILS/Sections/Raw/<commentary-name>/<node-id>.md
```

`<commentary-name>` matches the commentary filename without the language prefix or `.md` extension (`pi-dhammasangani-atthakatha.md` → `dhammasangani-atthakatha`). `<node-id>` matches the heading's block ID with the caret stripped (`^1-1-0` → `1-1-0`).

Create the parent directory if it does not exist.

---

## Output file format

```markdown
---
node_id: <e.g. 1-1-0>
node_heading: <the original-language heading text>
commentary: <commentary-name>
commentary_file: 1-SOURCES/Commentaries/<commentary-name>.md
language: <pi | sa | bo | zh | ...>
status: draft
---

## <node-heading verbatim>

<one or more short paragraphs in the original language, summarising what this
node of the commentary covers. Use only the commentary's own terminology.
Every factual claim — what is defined, what example is given, what the
commentator concludes — must end with a citation to the supporting block(s).>

(1-SOURCES/Commentaries/<commentary-name>.md#^<block-id>)
```

A second paragraph follows the same shape. Keep the summary compact — the goal is orientation for a translator, not a re-presentation of the commentary.

---

## Rules

1. **Original language only.** If the commentary is in Pali, the summary is in Pali. If Sanskrit, Sanskrit. No translation, no English glosses inside the paragraph. The frontmatter `language` field reflects this.
2. **Use the commentary's terminology verbatim.** Do not normalise spellings, do not substitute synonyms, do not switch to a more familiar word. If the commentary writes *kusalā dhammā*, the summary writes *kusalā dhammā* — never "wholesome states".
3. **Compress; do not paraphrase.** A summary is shorter than the source. It is not a different reading of the source. If a point cannot be made in the commentary's own words, leave it out.
4. **Cite every claim.** Each paragraph ends with one or more `(1-SOURCES/Commentaries/<commentary-name>.md#^<block-id>)` references that anchor every factual statement in the paragraph to a specific block.
5. **Cover only the node.** Do not summarise child nodes inside the parent — they get their own files. Reference children by their heading text in passing if essential for narrative coherence.
6. **No new vocabulary.** Never introduce a term that does not appear in the commentary's discussion of this node.

---

## Procedure

1. Open the commentary file and locate the heading whose block ID matches the requested node-id.
2. Identify the block range that belongs to that heading: from the first block under the heading down to (but not including) the next heading at the same level or higher.
3. Read every block in that range.
4. Draft a one- to four-paragraph summary in the original language. Each paragraph addresses one move the commentator makes (a definition, an example, a refutation, a synthesis).
5. After each paragraph, place the block-ID citations for the source blocks it draws on.
6. Fill the frontmatter. Set `status: draft`.
7. Write the file to `2-RAILS/Sections/Raw/<commentary-name>/<node-id>.md`.

---

## Examples

### Example invocation

> "Run `section-summary-raw` for node `^1-1-0` (Ganthārambhakathā) of `pi-dhammasangani-atthakatha.md`."

### Example output skeleton

```markdown
---
node_id: 1-1-0
node_heading: Ganthārambhakathā
commentary: dhammasangani-atthakatha
commentary_file: 1-SOURCES/Commentaries/pi-dhammasangani-atthakatha.md
language: pi
status: draft
---

## Ganthārambhakathā

Imissā ganthārambhakathāya Buddhaghosācariyo paṭhamaṃ namassanaṃ karoti,
tato Dhammasaṅgaṇī-aṭṭhakathāya nāmaṃ niyamento Aṭṭhasālinīti vohāraṃ vadati.
(1-SOURCES/Commentaries/pi-dhammasangani-atthakatha.md#^1-1)
(1-SOURCES/Commentaries/pi-dhammasangani-atthakatha.md#^1-2)

Ācariyo āha — Abhidhammapiṭake satta pakaraṇāni honti, tesu paṭhamaṃ
Dhammasaṅgaṇi nāma, tassā aṭṭhakathā Aṭṭhasālinīti.
(1-SOURCES/Commentaries/pi-dhammasangani-atthakatha.md#^1-3)
```

---

## Completion check

Before marking the file complete, verify:

- [ ] Frontmatter complete (`node_id`, `node_heading`, `commentary`, `commentary_file`, `language`, `status`)
- [ ] Heading on line below frontmatter matches `node_heading` exactly
- [ ] Every paragraph ends with at least one citation
- [ ] Every citation points to a block actually present in the source file
- [ ] Summary is in the original language only — no translation interleaved
- [ ] No terminology used that is not attested in the source range

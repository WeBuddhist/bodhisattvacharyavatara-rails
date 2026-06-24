---
name: toc-tree-extraction
description: >
  Build a full nested, decimal-numbered ས་བཅད (sa bcad) table-of-contents TREE from a
  Tibetan Buddhist commentary — the complete pipeline, not just candidates. Use this skill
  whenever the user wants the WHOLE structural outline reconstructed: "build the sa bcad
  tree", "extract the TOC tree", "make the dkar chag / dkar-chag", "reconstruct the outline
  hierarchy", or "give me the nested table of contents" for a Tibetan commentary or root
  text. This is the Claude-native equivalent of the bundled extract_toc_tree.py (which uses
  the Gemini API): Claude performs the four inference passes itself — (1) section
  candidates, (2) verbatim enumeration blocks, (3) nested decimal tree, (4) QC repair —
  while two bundled Python helpers do the deterministic chunking and tree QC. For
  candidate-only extraction without building a tree, use toc-candidate-extraction instead.
---

# ས་བཅད TOC Tree Extraction (Claude-native)

You are an expert in classical Tibetan Buddhist *sa bcad* (ས་བཅད) — the structural
outlining system of Tibetan commentarial literature.

This skill reconstructs the **full hierarchical table of contents** (དཀར་ཆག / *dkar chag*)
of a commentary as a single nested, decimal-numbered tree. It is the Claude-native port of
`4-SYSTEM/Scripts/toc_tree_extractor/extract_toc_tree.py`: that script ships four prompts to
Gemini Flash; here **you** are the model that performs those four passes. Two bundled Python
helpers handle the parts that must be deterministic — chunking and the QC checker. Do not
reimplement those by hand.

**Pipeline:** chunk → (1) candidates → (2) enumerations → (3) tree → (4) deterministic QC →
repair. Passes 1–2 prioritise **recall**; pass 3 reconciles them into structure; pass 4
removes hallucinations and numbering errors.

---

## Inputs

| Input | Description |
|---|---|
| `input-file` | Path to the commentary/root-text `.md`, normally under `1-SOURCES/Commentaries/` |
| `commentary-id` | Short id for output filenames (inferred from the filename if obvious) |

If the file path is missing, or the `commentary-id` is not obvious from the filename, **stop
and ask** before doing anything else.

---

## Outputs (all under `0-INBOX/`)

| File | Stage |
|---|---|
| `0-INBOX/temp/TOC-<id>/candidates/chunk_NNN.md` | per-chunk section candidates (resumable) |
| `0-INBOX/temp/TOC-<id>/enumerations/chunk_NNN.md` | per-chunk verbatim enumeration blocks |
| `0-INBOX/toc-candidates-<id>.md` | merged candidates |
| `0-INBOX/toc-tree-<id>.md` | the final nested decimal TOC tree |
| `0-INBOX/toc-tree-qc-<id>.md` | QC report (issues before / after repair) |

These are drafts in `0-INBOX/` — scratch, never cited from `2-RAILS/`. The tree has **no
`^toc` block IDs**; the decimal numbering alone identifies each entry. (Inserting the tree
into a source/rails file with block IDs is a separate step — use `add-toc`.)

---

## Step 0 — Chunk the file

Large files must be processed in overlapping windows so nothing is missed at boundaries.

```bash
python 4-SYSTEM/Skills/toc-tree-extraction/scripts/chunk_file.py \
  "<input-file>" --chunk-size 150 --overlap 25 \
  --output-dir 0-INBOX/temp/TOC-<id>/chunks
```

The 25-line overlap guarantees every candidate appears in full in at least one chunk.
**Resumability:** write each chunk's result to its own file before moving on; on a re-run,
skip any `chunk_NNN.md` that already exists, so an interrupted run resumes from the first
missing chunk.

---

## Pass 1 — Section candidates (recall-first)

For each chunk, extract the *sa bcad* **section titles** — the genuine structural divisions,
NOT every number or ordinal. Balance recall and precision: capture every real section, but
when you are not confident something is structural rather than incidental, **leave it out**.
A clean list of real sections beats an exhaustive list of false positives.

**Three section types — extract all three independently:**

- **Type A — Announcement:** the author declares a division, splitting a topic into N named
  parts. e.g. `དང་པོ་ལ་གཉིས་ཏེ། མཚན་དོན་དང་། འགྱུར་ཕྱག་གོ།`
- **Type B — Node header:** a short label opening a section ("now treating part N").
  e.g. `གཉིས་པ་འགྱུར་ཕྱག་ནི།`
- **Type C — Closing count:** a number word after a list, stating how many items were given.
  e.g. `ཞེས་རྣམ་པ་གསུམ་མོ། / གནས་བརྒྱད་དོ།`

**Recognition — meaning first, markers second.** For each passage ask: *is this dividing a
topic into named parts, labelling a sub-section, or counting items just listed?* If yes —
regardless of exact wording — extract it. Any one signal is enough: ordinal labels
(དང་པོ། / གཉིས་པ། …, even scattered); division words (སྟེ། / ལ། / དབྱེ་ན།) after a topic
heading; a number word near a list of named items; a verse listing items that prose then
unpacks; `ལ་སོགས་པ།` closing a partial list near a number; `རྣམ་པ་ / གནས་ / ཚུལ་ / ཞེས་བྱ་བ་`
within ~30 words of a number.

**Do NOT extract** (common false positives): numbers that are part of the doctrinal content
itself (qualities, attributes, quantities being explained — not the text's own outline);
numerals inside quotations, citations, folio/page refs, dates, mantra counts; ordinal-looking
words in ordinary prose; a section already extracted earlier in the same chunk. When unsure,
omit it.

**Output format** — for each section, exactly this block and nothing more:

```
CONTEXT: [≈10 Tibetan words before + ≈10 after the section]
SECTION_TITLE: [ordinal marker + topic name, WITHOUT the trailing division clause or
particle. Strip "divided into N" phrases (ལ་གཉིས་ཏེ། , ལ་གསུམ་ལས། , ལ་བཞི། ) and trailing
markers (ནི། , closing ། ). Keep the ordinal; keep the topic words.
  དང་པོ་ལ་གཉིས་ཏེ།      ->  དང་པོ་
  གཉིས་པ་འགྱུར་ཕྱག་ནི།   ->  གཉིས་པ་འགྱུར་ཕྱག་]
ITEMS:
1. [first named item, Tibetan]
2. [second named item, Tibetan]
```

If items cannot be determined, write `ITEMS:` then a single line `[implicit]`. Separate
blocks with one blank line. If a chunk has no sections, write exactly `NO CANDIDATES`.

Save each chunk's result to `0-INBOX/temp/TOC-<id>/candidates/chunk_NNN.md` with a header:

```
<!-- chunk NNN | lines START–END | source: <id> -->

[candidate blocks, or: <!-- no candidates --> ]
```

---

## Pass 2 — Verbatim enumeration blocks (independent pass)

Run separately over the **same chunks**. Here you COPY OUT, **verbatim**, the passages that
ANNOUNCE structural divisions — the sentences where the author divides a topic into a stated
number of named parts (e.g. `…ལེའུ་བཅུ་ཡོད་པ་ལས།`, `…ལ་གཉིས་ཏེ། X དང་། Y'འོ། །`, `…ལ་གསུམ་ལས།`).
These are the text's OWN skeleton and are **more authoritative** than individual candidates.

Rules:

- Copy the Tibetan **exactly**. Do NOT paraphrase, translate, summarise, renumber, reorder,
  or add labels/commentary.
- Group **consecutive** announcement sentences (a cascade of nested divisions with no
  intervening explanatory prose) into ONE block, preserving order and line breaks.
- Start a NEW block whenever a run of announcements is separated from the next by intervening
  commentary.
- Include only the announcement sentences themselves, not surrounding commentary.

Output exactly this shape and nothing else:

```
Enumeration Block 1:
<verbatim Tibetan announcement line(s)>
Enumeration Block 2:
<verbatim Tibetan announcement line(s)>
```

`Enumeration Block N:` is the only text you add. If a chunk has no announcements, write
exactly `NO ENUMERATIONS`. Save to `0-INBOX/temp/TOC-<id>/enumerations/chunk_NNN.md`.

---

## Merge

Concatenate the per-chunk candidate files (preserving their `<!-- chunk NNN -->` headers)
into `0-INBOX/toc-candidates-<id>.md` with frontmatter:

```yaml
---
source: <id>
skill: toc-tree-extraction
stage: candidates
date: <YYYY-MM-DD>
total_candidates: <N>
---
```

Keep the merged enumerations text (all non-`NO ENUMERATIONS` blocks, in document order) ready
for the next pass.

---

## Pass 3 — Build the nested decimal tree

Reconstruct the FULL hierarchical TOC from the **candidates** reconciled against the
**enumerations**, and emit it with hierarchical decimal numbering.

Use the enumerations two ways:

- **A. Eliminate false positives** — a candidate that matches no part named in any
  enumeration, and is not itself the parent of a declared division, is suspect. Drop it
  unless its ordinal sequence clearly makes it a real sibling. Don't let stray numbers become
  nodes.
- **B. Fill gaps — for STRUCTURAL divisions only.** Every part of a genuine *sa bcad* division
  must appear as a child of its parent; if a declared part has no matching candidate, insert
  it using the part's title text (no marker). The number of children under a structural parent
  must match the count its announcement declared.

  **Not every enumeration is part of the inline TOC.** The enumerations also contain
  **doctrinal/content lists** — items enumerated as subject matter being explained, not as
  structural divisions. Do NOT make those into nodes. A list seeds nodes only when its parts
  are subsequently **opened** as their own ordinal-led sections (དང་པོ་… ནི། / གཉིས་པ་… ལ་…).
  Signs a list is CONTENT (do not branch it): its items are never re-opened later as their own
  ordinal-led sections; it enumerates doctrinal categories/qualities/stages as the topic being
  discussed; it sits inside the explanation of one leaf section without subdividing it. When in
  doubt, require corroboration.

**Matching — by meaning, not string equality.** A part is often worded differently where it is
declared (in the enumeration) vs where its section opens (the node header). Treat two names as
the SAME section when one is a fuller/shorter/lightly-reworded form of the other (inserted or
dropped qualifiers like ཅུང་ཟད་ "briefly", མདོ་ཙམ་, རྒྱས་པར་; near-synonym verbs བསྒྱུར་བ་ ~
བཤད་པ་; added/removed ནི། པ་ པོ་ འོ།). Use the node header's **ordinal** + the fuzzy name to
align it to the right part — e.g. enumeration part `…མཚན་དོན་བཤད་པའོ། །` and node header
`གཉིས་པ་མཚན་དོན་ཅུང་ཟད་བཤད་པ་ལ་གཉིས་ཏེ།` are the SAME (2nd) part: use them as ONE node (prefer
the node header's wording), do NOT create a duplicate sibling, and do NOT split one section in
two because its name varies.

**Inferring hierarchy** (read the Tibetan; don't guess from candidate order alone):

1. Ordinal prefixes mark sibling rank within one parent: དང་པོ་=1, གཉིས་པ་=2, གསུམ་པ་=3,
   བཞི་པ་=4, ལྔ་པ་=5, དྲུག་པ་=6, བདུན་པ་=7 … (and ༡༽ ༢༽ ཀ༽ ཁ༽ follow the same logic). A
   series restarts when a new parent is introduced.
2. An announcement candidate ending in a count (གཉིས་ཏེ། / གསུམ་སྟེ། / བཞི་ལས། / …ལ།) is a
   PARENT; its named ITEMS become its direct children one level deeper. A child that is itself
   later announced and subdivided becomes a parent in turn.
3. When a peer ordinal reappears (e.g. གཉིས་པ་ after a run of children), return to the depth of
   the matching དང་པོ་ that opened that sibling series.
4. A short candidate that merely names one element of an enumeration (no trailing count) is a
   leaf at its depth.

**Ordinals on display text:** every node's text must BEGIN with the Tibetan ordinal exactly as
the node header carries it (keep གཉིས་པ་ even if the enumeration listed that part without an
ordinal). But never **fabricate** an ordinal: if neither the node header nor the enumeration
part has a Tibetan number, the display text has none (decimal numbering still applies).

**Clean each display string:** strip leading bullets/bracket markers (༡༽ ཀ༽ …) and Tibetan
decimal labels; strip trailing block IDs (`^…`) and unwrap wiki-links (`[[#^id|text]] → text`);
strip everything after the topic name (the division clause ལ་གཉིས་ཏེ། / ལ་གསུམ་ལས། / …སྟེ། /
…ལས། and trailing particles ནི། / ནི / ལ། / འོ། / པོ། / སྟེ། / དང་) and any trailing shad
(། །། ལོ།). Keep the leading ordinal and the full topic phrase otherwise — do not over-truncate.

**Output — emit ONLY the TOC block, exactly this shape:**

```
## དཀར་ཆག / Table of Contents

* 1. <clean text>
   * 1.1 <clean text>
      * 1.1.1 <clean text>
   * 1.2 <clean text>
* 2. <clean text>
```

Format rules: indent = 3 spaces × (depth − 1); decimal = `1.` at depth 1, `1.1` at depth 2,
`1.1.1` at depth 3, …; **no `^toc` block IDs**; when an entry carries a Tibetan ordinal it MUST
equal the decimal's last segment (གསུམ་པ་ → …3); one entry per line, no blank lines between
entries; counters reset when you move to a shallower level; cover the whole document, drop no
branches. Output Tibetan only — no English, no commentary, no code fences. Each entry is the
TITLE ONLY (no trailing particle, no །, no gap markers).

Save to `0-INBOX/toc-tree-<id>.md` with `stage: toc-tree` frontmatter.

---

## Pass 4 — Deterministic QC, then repair

Run the bundled checker (NOT by hand — it encodes the exact numbering/attestation logic):

```bash
python 4-SYSTEM/Skills/toc-tree-extraction/scripts/qc_check_tree.py \
  0-INBOX/toc-tree-<id>.md \
  --corpus 0-INBOX/toc-candidates-<id>.md 0-INBOX/temp/TOC-<id>/enumerations/*.md \
  --out 0-INBOX/toc-tree-qc-<id>.md
```

The checker flags: indentation errors; Tibetan-ordinal vs decimal mismatch; duplicate
decimals; sibling sequences with gaps/dups; **titles not attested** in candidates/enumerations
(possible hallucination); and **ordinals not attested** for a title. Exit code = issue count.

If issues remain, **repair the tree yourself** against BOTH sources, focusing on four things:

1. **Numbering vs Tibetan ordinals** — the Tibetan ordinal is authoritative for a node's
   position. When the decimal's last segment differs, fix the **decimal**, then renumber the
   siblings and cascade into descendants.
2. **No gaps** — each parent's children run 1, 2, 3… with no missing/duplicate number, count
   matching the enumeration. For a missing declared child, FIRST look for it among the
   candidates (it may be present under different wording — match by meaning) and insert that
   real node; only if none corresponds, insert the enumerated part as a normal node. Remove any
   leftover `⟨gap⟩` markers.
3. **Reconcile both sources** — fix each issue by checking the tree against both enumerations
   (parents, counts, ordered parts) and candidates (what was actually found). Don't duplicate a
   node that already exists under a varied name.
4. **No hallucinated nodes** — every node's title and ordinal must correspond to a real string
   in enumerations or candidates. For "title not attested": either find the matching attested
   wording and replace the node's text with it, or, if invented, delete the node and renumber.
   For "ordinal N not attested for this title": correct the node's ordinal to the one the
   source attaches, then fix the decimal to agree. Do NOT invent titles or ordinals to satisfy
   a count.

Do not reorder/reword real nodes, change Tibetan text, turn content lists into nodes, or invent
an ordinal where neither node nor enumeration has one. Re-run the checker after repair; record
issues-before / issues-after in `0-INBOX/toc-tree-qc-<id>.md`. Iterate until the count is 0 or
only genuinely-ambiguous issues remain (note those for the human).

---

## Execution summary

1. Confirm `input-file` and `commentary-id` (ask if not obvious).
2. `chunk_file.py` → overlapping chunks.
3. Pass 1: candidates → one file per chunk (resumable).
4. Pass 2: verbatim enumerations → one file per chunk.
5. Merge candidates → `0-INBOX/toc-candidates-<id>.md`; assemble enumerations text.
6. Pass 3: build the nested decimal tree → `0-INBOX/toc-tree-<id>.md`.
7. Pass 4: `qc_check_tree.py` → repair → re-check → `0-INBOX/toc-tree-qc-<id>.md`.
8. Report totals (candidates, enumeration blocks, issues before/after) and the output paths.

For candidate extraction only (no tree), use `toc-candidate-extraction`. For batch/headless
runs over many commentaries without a Claude session, the Gemini script
`4-SYSTEM/Scripts/toc_tree_extractor/extract_toc_tree.py` does the same pipeline autonomously.

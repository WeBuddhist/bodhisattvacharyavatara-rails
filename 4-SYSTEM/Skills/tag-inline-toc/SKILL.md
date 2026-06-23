---
name: tag-inline-toc
description: >
  Identify inline structural announcement phrases (sa bcad) in a formatted
  Tibetan commentary file, wrap the announced terms in Obsidian wikilinks,
  and insert standalone markdown heading lines with block IDs per CLAUDE.md §5b.
  Run after format-commentary, before structural-outline-ingest.

  Trigger this skill when the user says things like:
  "tag the inline TOC", "add wikilinks to the outline phrases",
  "mark up the sa bcad", "tag the structural announcements",
  "add table of content tags", or "add headings to this commentary".
---

# tag-inline-toc

Tibetan commentaries use **inline structural announcements** (*sa bcad*): sentences where the author enumerates the sub-topics that will follow before treating each one in turn. This skill makes those announcements machine-readable by doing **two things**:

1. **Inline TOC** — wrapping each announced term and each section-body restatement in `[[#^N-N-0|term]]` Obsidian wikilinks.
2. **Heading TOC** — inserting a standalone markdown heading line (`##` through `######`) with a block ID immediately before each section-body paragraph.

This implements the convention in CLAUDE.md §5b. The output is saved to `0-INBOX/temp/` and is **not** yet a `1-SOURCES/` file; human review is required before ingest.

---

## Architecture

The work has two very different kinds of subtask:

- **Linguistic judgment (Phase 1)** — finding the sa bcad phrases, reading what they mean, and assembling the section tree. This genuinely needs language understanding, and it is done **entirely by the model**.
- **Deterministic mechanics (Phase 2)** — assigning `^N-…-0` block IDs, inserting heading lines, wrapping exact substrings, and proving no prose was altered. This is pure string manipulation and is done **entirely by a script**.

### Phase 1 is model-only — do NOT script the extraction

Sa bcad detection has too many surface variants (counts that close with `།`/`་ལས།`/`་སྟེ།`/`་ཡོད་པ་ལས།`; names that contain internal `དང་`; titles that appear as ordinal-only, name-only, or ordinal+name; verse quotations that merely *look* like enumerations). A rule/regex extractor cannot separate genuine sa bcad from look-alikes, and cannot find verbatim term boundaries — every rule spawns three exceptions, and tuning it is an endless loop. **Phase 1 reads for meaning; it does not pattern-match with code.** The only script in this skill is the Phase-2 renderer.

### Flow

```
  commentary.md
       │
       ▼  PHASE 1 — model, reading for meaning
   1. Frame:      identify the top-level division + chapter boundaries (TOC of the TOC)
   2. Extract:    per chapter (chunkable / parallel), list every sa bcad CANDIDATE of
                  both types → a raw candidate artifact. No tree yet, no depth yet.
   3. Review:     read the raw artifact once end-to-end; fix span boundaries, drop
                  look-alikes, confirm counts.
   4. Reconstruct: per chapter, JOIN the two candidate types into nodes and rebuild the
                  tree (depth) by ordinal+count bookkeeping → the annotation (JSON).
       │
       ▼  PHASE 2 — script, tag_inline_toc.py render
   5. Render:     assign block IDs from depth, insert headings, wrap wikilinks by anchored
                  exact match, PROVE existing prose is unchanged, then write.
       ▼
  0-INBOX/temp/tagged-<filename>
```

Because block IDs are assigned by code, depth-skipping and numbering bugs are impossible by construction. Because wraps are exact-substring and the result is diffed back against the source, silent transcription drift is caught and the run fails loudly. **The model never retypes Tibetan prose** — it only points at substrings that already exist.

### Files in `scripts/`

| File | Phase | Role |
|---|---|---|
| `scripts/tag_inline_toc.py` | 2 | Deterministic renderer + prose-integrity verifier. **The only script.** |
| `scripts/annotation.schema.json` | 1 → 2 | Schema for the **annotation** (Phase-1 final output / Phase-2 input). |
| `scripts/example-annotation.json` | — | A worked example annotation. |
| `scripts/example-candidates.json` | 1 | A worked example of the raw candidate artifact. |

---

## Inputs

| Field | Description |
|---|---|
| Input file | Path to a formatted Tibetan commentary file — typically `0-INBOX/segmentation/<filename>.md` |

The input file must already have:
- YAML frontmatter (at minimum `title:`, `author:`, `file_type:`, `language_tag:`)
- No wikilink tags on announcement phrases yet
- No standalone heading lines yet

---

## Output

A single file at `0-INBOX/temp/tagged-<original-filename>` (the script auto-suffixes `-v2`, `-v3`, … rather than overwriting). It adds two kinds of markup and nothing else:

1. **Heading lines** — new `##`–`######` lines with block IDs, inserted on blank lines before each section body.
2. **Wikilinks** — existing terms wrapped in `[[#^id|term]]`. No prose text is deleted, inserted, or reordered.

### Heading line format

| Depth | Heading level | Format |
|---|---|---|
| 1 (top-level) | `##` | `## <title> ^N-0` |
| 2 | `###` | `### <title> ^N-N-0` |
| 3 | `####` | `#### <title> ^N-N-N-0` |
| 4 | `#####` | `##### <title> ^N-N-N-N-0` |
| 5 | `######` | `###### <title> ^N-N-N-N-N-0` |
| 6+ | `######` | `###### <title> ^N-…-N-0` (block ID extends as needed) |

Markdown has only 6 heading levels. For depth 6+, keep `######` and let the block ID carry the nesting. `<title>` is the short section name (the announced term), not the full ordinal phrase — `བཤད་པ།`, not `གཉིས་པ་བཤད་པ།`.

### Wikilink formats

Announcement sentence (each announced term links **forward** to its child section):
```
ལེའུ་དང་པོ་ལ་[[#^1-1-0|མདོར་བསྟན་པ་]]དང་[[#^1-2-0|རྒྱས་པར་བཤད་པ་]]གཉིས་ཡོད་པ་ལས།
```

Section-body restatement (the ordinal+title at the section opening links to its own heading — self-referential by design):
```
### བཤད་པ། ^1-2-0

[[#^1-2-0|གཉིས་པ་བཤད་པ་]]ནི་སྤངས་རྟོགས་མཐར་ཕྱིན་པའི་...
```

---

## The two candidate types (the heart of Phase 1)

Every node in the outline is described by **two different phrases**, in two different places, and you usually need **both** to fully reconstruct it:

**Type 1 — child enumeration** (appears at a parent's start; announces the parent's children).
A count, optionally followed by the children's names:
```
དང་པོ་ལའང་སྡུག་བསྔལ་མི་རྟག་སྟོང་བདག་མེད་བཞི་ཡོང་པ་ལས།     ← count 4, names: སྡུག་བསྔལ / མི་རྟག / སྟོང་ / བདག་མེད
གཉིས་པ་མཚན་དོན་སྨོས་པའི་དགོས་པ་...ལ་གཉིས། དགོས་པ་དངོས་དང་། མཚན་བཏགས་པའི་དགོས་པའོ། །   ← count 2, two named children
དང་པོ་ལ་གསུམ་སྟེ།                                        ← count 3, COUNT-ONLY (names supplied by the titles)
```

**Type 2 — in-location title** (appears at the *start of a child's own span*; marks where that child begins, and may carry the child's *own* Type-1 enumeration). Three surface forms:
```
གཉིས་པ་ནི།                  ← ordinal-only  (name must come from the parent enumeration)
མི་རྟག་པ་ལ་                 ← name-only     (ordinal recovered by matching the name into the parent enum)
མི་རྟག་པ་ལའང་གསུམ་ནི།       ← ordinal/name + its OWN enumeration (count 3) — Type 2 carrying a Type 1
```

So the `མི་རྟག` node's *name and sibling position* come from the parent's Type-1 enumeration (`...སྡུག་བསྔལ་མི་རྟག་སྟོང་བདག་མེད་བཞི...`), while its *location and any children* come from its Type-2 title (`མི་རྟག་པ་ལའང་གསུམ་ནི།`). Reconstruction (Step 4) is the **join** of these two views.

**Not sa bcad — never a candidate:**
- **Chapter label lines** `ལེའུ་[ordinal]། [desc]` are plain prose. (Note: a *chapter enumeration* like `Nth … ལེའུ་ལ་ གཉིས། ལེའུའི་གཞུང་ དང་ ལེའུའི་མཚན` IS a Type-1 enumeration — tag it; the bare label line is not.)
- **Editorial markers** `N.N` (e.g. `1.1`, `8.17`) are verse locators. The sa bcad is the **first Tibetan line after** the marker.
- **Verse quotations / ordinary prose** that merely contain `ལ་ … དང་ … <count>`. If it is a citation or a sentence that happens to list things, it is not sa bcad. This is a meaning call — make it.

---

## The raw candidate artifact (Phase-1 intermediate)

A flat JSON list of every candidate, **in document order**, with no depth and no tree yet. One record per candidate. Worked example: `scripts/example-candidates.json`.

```json
{
  "source_file": "0-INBOX/.../foo.md",
  "candidates": [
    {
      "line": 4999,
      "type": "enumeration",
      "count": 4,
      "parent_marker": "དང་པོ་",
      "children": ["བདག་ལ་སྡུག་བསྔལ་བྱེད་པ་", "བདག་ལ་བརྙས་བཅོས་བྱེད་པ་", "...", "..."],
      "text": "དང་པོ་ལ་བཞི། བདག་ལ་སྡུག་བསྔལ་བྱེད་པ་ལ་བཟོད་པ་དང་། ..."
    },
    {
      "line": 5003,
      "type": "title",
      "ordinal": 1,
      "name": "བདག་ལ་སྡུག་བསྔལ་བྱེད་པ་",
      "carries_enum": true,
      "restatement": "དང་པོ་",
      "text": "དང་པོ་ལ་གསུམ། སྡུག་བསྔལ་དང་ལེན་གྱིས་བཟོད་པ་སྒོམ་པ། ..."
    }
  ]
}
```

Per-candidate fields:

| Field | Applies to | Meaning |
|---|---|---|
| `line` | both | 1-based line number in the source (your anchor; lets you copy a verbatim, unique context later). |
| `type` | both | `"enumeration"` (Type 1) or `"title"` (Type 2). |
| `text` | both | The verbatim line (or the verbatim sa bcad span on it), copied exactly. |
| `count` | enumeration | Integer the count word states. |
| `parent_marker` | enumeration | The leading ordinal/name the enumeration is attached to, verbatim (may be just `དང་པོ་`, or a full `གཉིས་པ་NAME་`). |
| `children` | enumeration | Verbatim name spans of the announced children, in order. Empty list if count-only. |
| `ordinal` | title | 1-based position among siblings (`དང་པོ`=1 …), or `null` if name-only with no ordinal. |
| `name` | title | Verbatim name span, or `null` if ordinal-only. |
| `carries_enum` | title | `true` if this title line also declares its own children (a Type-2 carrying a Type-1; that Type-1 should also appear as its own `enumeration` record). |
| `restatement` | title | The verbatim ordinal(+name) prefix at the body opening to self-link later. |

All `text`/`children`/`name`/`restatement`/`parent_marker` strings must be **verbatim spans** — exact bytes from the source, never paraphrased. Loose spans pass here but fail the Phase-2 verbatim check.

---

## The annotation (Phase-1 final output → Phase-2 input)

After the join+reconstruction, emit the annotation — an ordered list of sections **in document order**. This is unchanged from the renderer's contract; full schema: `scripts/annotation.schema.json`, worked example: `scripts/example-annotation.json`.

```json
{
  "source_file": "0-INBOX/.../foo.md",
  "sections": [
    { "depth": 1, "heading_title": "ལེའུ་དང་པོ།", "body_start_context": "<verbatim line>", "restatement": "ལེའུ་དང་པོ་" },
    { "depth": 2, "heading_title": "མདོར་བསྟན་པ།", "body_start_context": "<verbatim line>", "restatement": "དང་པོ་མདོར་བསྟན་པ་",
      "announced_in_parent": { "context": "<verbatim enumeration line>", "term": "མདོར་བསྟན་པ་" } }
  ]
}
```

| Field | Required | Meaning |
|---|---|---|
| `depth` | yes | Nesting depth (1 = top-level `##`). Must descend one level at a time — never skip. |
| `heading_title` | yes | Short section name for the heading line (the term only). |
| `body_start_context` | yes | A **verbatim** substring **unique to the body-opening line**. Copy the whole line from the artifact's `line` to guarantee uniqueness; the script errors on 0 or >1 matches. |
| `restatement` | no | Verbatim ordinal+title at the body opening to wrap in a self-link. Must occur on the body line. |
| `announced_in_parent` | no | `{ "context", "term" }` — a unique substring of the parent's enumeration line and the verbatim child term to wrap. |

**The model assigns no block IDs.** It gives only `depth`; the script derives every `^N-…-0`.

---

## Procedure

### Step 1 — Frame the document (TOC of the TOC)

Read the opening structural matter and find the **top-level division and the chapter boundaries** — e.g. a four-fold grouping of ten chapters closing with `…ལེའུ་བཅུ་ཡོད་པ་ལས།`, with each chapter introduced by a `Nth … ལེའུ་ལ་ COUNT …` enumeration. Record, for each chapter: its line range and its **base depth** (its depth in the spine). This frame is what makes Step 2 chunkable and gives each chapter a stable place in the tree.

### Step 2 — Extract raw candidates, per chapter (chunkable / parallel)

For each chapter chunk, read for meaning and list **every** candidate of both types into the raw artifact (see format above). Extraction is **stateless** — each candidate is judged locally — so chapters can be done independently and **in parallel** (e.g. spawn one subagent per chapter range, each returning its `candidates` slice; concatenate in document order).

Bias toward **recall with honest typing**: include a line only if it is genuinely a child enumeration or an in-location title; exclude verse quotations and incidental lists. Capture verbatim spans. Do not assign depth here.

### Step 3 — Review the raw artifact once

Read the consolidated artifact end-to-end (it is short — hundreds of lines, not the whole document). Fix span boundaries, drop look-alikes that slipped through, and confirm each enumeration's `count` matches the number of `children` it names (or is intentionally count-only). This single pass is the human-auditable checkpoint.

### Step 4 — Reconstruct the tree, per chapter (join → annotation)

Within each chapter, walk the candidates in document order and rebuild the tree by **ordinal + count bookkeeping**, joining the two types:

- An **enumeration** (Type 1) opens a frame expecting `count` children at depth+1; if it names children, those names fill the slots in order.
- A **title** (Type 2) fills the next slot of the open frame: its `ordinal` says which slot; its `name` (or the slot's enumerated name) gives the term. Match `name`↔enumerated-child by **meaning** after stripping the leading ordinal and trailing particles (`ལ/ལའང/ནི/པ/སྟེ`); use ordinal+slot as the primary key and the name as the cross-check (and as the display source when the title is ordinal-only).
- If the title `carries_enum`, it in turn opens a deeper frame.
- A frame **closes** when it has `count` contiguous children (ordinals 1..count). Use this redundancy to self-check: if a frame can't close, or an ordinal is skipped, or a name doesn't match its slot, mark the node `"review": "<reason>"` and continue conservatively (treat as the next sibling/child).

Emit each joined node as an annotation `section`: `depth` = base depth of the chapter + frame depth; `heading_title` = the short term; `body_start_context` = the verbatim title line (from `line`); `restatement` = the title's restatement span; `announced_in_parent` = `{context: parent enumeration line, term: this child's name}` when the parent named it. Concatenate all chapters' sections in document order into one annotation file: `0-INBOX/temp/<filename>.annotation.json`.

> **Block-ID convention:** the renderer assigns IDs from `depth` across the whole annotation. Keep the literal sa bcad nesting from the text (the spine's top division is depth 1). If chapter-rooted IDs that align with the chapter-verse root text are wanted instead, make each chapter a depth-1 node and note this choice for the reviewer.

### Step 5 — Render + verify (Phase 2, the script)

```bash
python3 4-SYSTEM/Skills/tag-inline-toc/scripts/tag_inline_toc.py render \
    --input  <input-file> \
    --annot  0-INBOX/temp/<filename>.annotation.json \
    --output 0-INBOX/temp/tagged-<filename>
```

The script assigns block IDs, inserts headings, wraps wikilinks by anchored exact match, and **verifies prose integrity before writing**. It prints a report and fails non-zero on any problem:

- *context not found* / *context is ambiguous* → copy the full body line as `body_start_context`; lengthen `announced_in_parent.context`.
- *term not found* / *restatement not on body line* → the span was not copied verbatim; fix it.
- *depth skips a level* → fix the `depth` sequence (a Step-4 bookkeeping slip).
- *PROSE INTEGRITY VIOLATION* → a wrap/context altered prose; inspect the reported line. **Never** work around it by editing the source.

Re-check any tagged file at any time:
```bash
python3 4-SYSTEM/Skills/tag-inline-toc/scripts/tag_inline_toc.py verify \
    --input <input-file> --tagged 0-INBOX/temp/tagged-<filename>
```

Then report to the user: the render counts, the output path, and every node you marked `"review"`. The output stays in `0-INBOX/temp/` — it is **not** a `1-SOURCES/` file. Human review is required before `structural-outline-ingest`.

---

## Rules

1. **Phase 1 is model-only meaning work.** Do not write or invoke a rule/regex extractor for sa bcad detection or span-finding. The only script is the Phase-2 renderer.
2. **No prose is altered.** The only changes are inserted heading lines and `[[#^id|term]]` wrappers; the renderer proves this by diffing and aborts on mismatch.
3. **Block IDs are derived from depth, by the script** — `^N-0`, `^N-N-0`, … one segment per level, no maximum depth, no zero-padding.
4. **Depth is never skipped**; siblings complete before descending. Enforced by the script.
5. **Verbatim spans only.** Every `text`/`children`/`name`/`context`/`term`/`restatement` is exact bytes from the source.
6. **Heading title is the short section name**, not the full ordinal phrase. **Wrap only the minimal structural term.**
7. **Chapter label lines (`ལེའུ་N།`) and editorial markers (`N.N`) are never tagged**; the sa bcad after a marker is.
8. **Output goes to `0-INBOX/temp/`**, never `1-SOURCES/` or `2-RAILS/`.

---

## Completion check

- [ ] Step 1: top-level division + chapter boundaries (and per-chapter base depth) recorded
- [ ] Step 2: raw candidate artifact built per chapter (both types), verbatim spans, no depth
- [ ] Step 3: artifact reviewed once; look-alikes dropped; counts vs named children confirmed
- [ ] Step 4: per-chapter join+reconstruction into one annotation; ambiguities marked `"review"`
- [ ] Step 5: `tag_inline_toc.py render` exited 0 with a prose-integrity VERIFIED report
- [ ] Output written to `0-INBOX/temp/tagged-<filename>`; review nodes reported to the user

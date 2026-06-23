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

## Architecture — why this skill is split in two

The work has two very different kinds of subtask, and conflating them is slow and error-prone:

- **Linguistic judgment** — deciding which lines are sa bcad, and where each announced term begins and ends. This genuinely needs language understanding.
- **Deterministic mechanics** — building the section tree, assigning `^N-…-0` block IDs, inserting heading lines, wrapping exact substrings, and proving no prose was altered. This is pure string manipulation and must NOT be done by hand.

So the skill runs in **two phases**:

```
  commentary.md
       │
       ▼
  [optional] find_sa_bcad.py  ── shortlist of candidate sa bcad lines
       │
       ▼
  PHASE 1 (model)  ── read the file, emit an ANNOTATION (JSON):
       │               ordered sections with depth, heading title,
       │               exact body-start context, restatement, and
       │               any announced-in-parent term. No IDs. No rewriting.
       ▼
  PHASE 2 (script) ── tag_inline_toc.py render:
       │               assign block IDs from depth, insert headings,
       │               wrap wikilinks by anchored exact match, and
       │               PROVE existing prose is unchanged, then write.
       ▼
  0-INBOX/temp/tagged-<filename>
```

Because block IDs are assigned by code, depth-skipping and numbering bugs are impossible by construction. Because wraps are exact-substring and the result is diffed back against the source, silent transcription drift is caught and the run fails loudly. **The model never retypes Tibetan prose** — it only points at substrings that already exist.

Scripts live in `scripts/`:

| Script | Phase | Role |
|---|---|---|
| `scripts/find_sa_bcad.py` | pre-1 | Heuristic shortlist of candidate sa bcad / opening lines. Optional but recommended for long files. |
| `scripts/tag_inline_toc.py` | 2 | Deterministic renderer + prose-integrity verifier. **Required.** |
| `scripts/annotation.schema.json` | — | JSON schema for the Phase-1 annotation. |
| `scripts/example-annotation.json` | — | A worked example annotation. |

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

## The annotation (Phase-1 output)

The model produces a JSON file — an ordered list of sections, **in document order, top to bottom**. The script turns it into the tagged file. Full schema: `scripts/annotation.schema.json`. Worked example: `scripts/example-annotation.json`.

```json
{
  "source_file": "0-INBOX/segmentation/foo.md",
  "sections": [
    {
      "depth": 1,
      "heading_title": "ལེའུ་དང་པོ།",
      "body_start_context": "ལེའུ་དང་པོ་ལ་མདོར་བསྟན",
      "restatement": "ལེའུ་དང་པོ་"
    },
    {
      "depth": 2,
      "heading_title": "མདོར་བསྟན་པ།",
      "body_start_context": "དང་པོ་མདོར་བསྟན་པ་ནི",
      "restatement": "དང་པོ་མདོར་བསྟན་པ་",
      "announced_in_parent": { "context": "ལེའུ་དང་པོ་ལ་མདོར", "term": "མདོར་བསྟན་པ་" }
    },
    {
      "depth": 2,
      "heading_title": "རྒྱས་པར་བཤད་པ།",
      "body_start_context": "གཉིས་པ་རྒྱས་པར་བཤད་པ་ནི",
      "restatement": "གཉིས་པ་རྒྱས་པར་བཤད་པ་",
      "announced_in_parent": { "context": "ལེའུ་དང་པོ་ལ་མདོར", "term": "རྒྱས་པར་བཤད་པ་" }
    }
  ]
}
```

Per-section fields:

| Field | Required | Meaning |
|---|---|---|
| `depth` | yes | Nesting depth (1 = top-level `##`). Must descend one level at a time — never skip. |
| `heading_title` | yes | Short section name for the heading line (announced term only). |
| `body_start_context` | yes | A **verbatim** substring of the original, **unique to the line** where this section's body opens. The heading is inserted right before that line. Make it long enough to be unique — the script errors if it matches 0 or >1 lines. |
| `restatement` | no | The verbatim ordinal+title phrase at the body opening (e.g. `གཉིས་པ་བཤད་པ་`) to wrap in a self-link. Must occur on the body line. |
| `announced_in_parent` | no | `{ "context", "term" }` — where this section is named in the PARENT's enumeration sentence. `context` is a unique substring of that line; `term` is the verbatim announced term to wrap (minimal structural term only). |

**The model assigns no block IDs.** It only gives `depth`; the script derives every `^N-…-0`. This is what makes depth-skips and mis-numbering impossible.

All context/term/restatement strings must be **copied verbatim** from the source. If the script reports "context not found" or "term not found", the model copied inexactly — fix the string, do not loosen the script.

---

## Procedure

### Step 1 — Read the file

Read the full input file. Hold the YAML frontmatter and the body.

### Step 2 — (Recommended) run the pre-filter

For anything but a very short file, surface candidate lines first so you adjudicate a shortlist instead of scanning cold:

```bash
python3 4-SYSTEM/Skills/tag-inline-toc/scripts/find_sa_bcad.py <input-file>
```

It tags lines as `announcement:FormA`, `announcement:FormB`, or `section-opening`, and flags chapter labels / editorial markers to skip. **These are heuristics** — confirm each, reject false positives, and (critically) fix the exact term boundaries yourself. The script never decides depth or wraps anything.

### Step 3 — Identify sa bcad and section openings (the linguistic judgment)

This is the part only you can do. Two announcement surface forms:

**Form A — full sentence.** Enumerates two or more sub-topics joined by `དང་`, closing with a count word (`གཉིས།`, `གསུམ་ལས།`, `བཞི་ཡོད་པ་ལས།`, …). Often opens with the parent title/ordinal: `X ལ་ Y དང་ Z གཉིས།`.
```
ལེའུ་དང་པོ་ལ་མདོར་བསྟན་པ་དང་རྒྱས་པར་བཤད་པ་གཉིས་ཡོད་པ་ལས།
```
Here the announced terms (`མདོར་བསྟན་པ`, `རྒྱས་པར་བཤད་པ`) ARE named inline — each becomes an `announced_in_parent` entry on its child section.

**Form B — compact.** The count appears right after `་ལ་`/`་ལ་ཡང་`; topic names (if any) follow, separated by `དང༌།`, the last closing `འོ། །`.
```
གཉིས་པ་ལ་བཞི། བྱང་ཆུབ་ཀྱི་སེམས་...བཤད་པ་དང༌། ...ངོས་བཟུང་བ་དང༌། ...རྒྱུ་མཚན་དང༌། ...བསྟོད་པའོ། །
```
When the compact line only states a count with no inline names (`དང་པོ་ལ་བཞི་ལས།`), the children are named only at their own openings — those sections have no `announced_in_parent`.

Count words (closed set): `གཉིས། གསུམ། བཞི། ལྔ། དྲུག། བདུན། བརྒྱད། དགུ། བཅུ།`

**Section-body openings** take one of three forms; use the nearest ancestor announcement to resolve which sub-section is opening:

| Form | Example |
|---|---|
| Ordinal only | `གཉིས་པ་ནི།` |
| Name only | `དོན་གནས་འཕོ་བའི་ཕན་ཡོན་ནི` |
| Ordinal + name | `གཉིས་པ་དོན་གནས་འཕོ་བའི་ཕན་ཡོན་ནི` |

**Not sa bcad — never tag:**
- **Chapter title lines** `ལེའུ་[ordinal]། [desc]` are plain text. No heading before them, no wikilink on them.
- **Editorial section markers** `N.N` (e.g. `1.1`, `8.17`) are verse-locator delimiters. The sa bcad is the **first Tibetan line that follows** the marker — tag that line, not the marker.

### Step 4 — Build the annotation

Walk the document top to bottom and emit the `sections` list (see schema above). For each section, in order:
- set `depth` from the nesting implied by the announcements (descend exactly one level at a time);
- set `heading_title` to the short term;
- copy `body_start_context` verbatim from the body-opening line, long enough to be unique in the file;
- if the opening restates the ordinal+title, copy it verbatim into `restatement`;
- if the section is named inline in its parent's enumeration, add `announced_in_parent` with a unique `context` from that enumeration line and the verbatim `term`.

**Depth discipline:** list sections in document order; finish all siblings at a depth before descending. The script enforces "no skipped levels" and will abort if `depth` jumps by more than one. If an announcement is ambiguous, resolve conservatively as the next level down and leave yourself a note to review.

Write the annotation to `0-INBOX/temp/<filename>.annotation.json`.

### Step 5 — Render with the script

```bash
python3 4-SYSTEM/Skills/tag-inline-toc/scripts/tag_inline_toc.py render \
    --input  <input-file> \
    --annot  0-INBOX/temp/<filename>.annotation.json \
    --output 0-INBOX/temp/tagged-<filename>
```

The script assigns block IDs, inserts headings, wraps wikilinks by anchored exact match, and **verifies prose integrity before writing**. It prints a report (sections, headings inserted, self-restatements tagged, announcements tagged, max depth) and fails non-zero on any problem:

- *context not found* / *context is ambiguous* → lengthen or correct `body_start_context` / `announced_in_parent.context`.
- *term not found* / *restatement not on body line* → the term was not copied verbatim; fix it.
- *depth skips a level* → fix the `depth` sequence.
- *PROSE INTEGRITY VIOLATION* → a wrap or context altered prose; inspect the reported line. **Never** work around this by editing the source.

If `--output` is omitted, the path is derived as `0-INBOX/temp/tagged-<input-basename>` with `-v2`/`-v3` suffixing.

### Step 6 — Verify and present

The render step already proves prose integrity. To re-check an existing tagged file against its source at any time:

```bash
python3 4-SYSTEM/Skills/tag-inline-toc/scripts/tag_inline_toc.py verify \
    --input <input-file> --tagged 0-INBOX/temp/tagged-<filename>
```

Then report to the user: the counts from the render report, the output path, and any sections you resolved ambiguously and want a human to review. The output stays in `0-INBOX/temp/` — it is **not** a `1-SOURCES/` file. Human review is required before `structural-outline-ingest`.

---

## Rules (invariants the script enforces)

1. **No prose is altered.** The only changes are inserted heading lines and `[[#^id|term]]` wrappers. The script proves this by stripping its own additions and diffing against the source; a mismatch aborts the run.
2. **Block IDs are derived from depth, by the script** — `^N-0`, `^N-N-0`, `^N-N-N-0`, … one segment per level, no maximum depth, no zero-padding.
3. **Depth is never skipped** and siblings complete before descending. Enforced.
4. **Heading title is the short section name**, not the full ordinal phrase.
5. **Wrap only the minimal structural term** — not surrounding particles, conjunctions, or count words.
6. **Announced terms link to real heading block IDs**; self-referential body links are intentional (§5b).
7. **Chapter title lines (`ལེའུ་N།`) and editorial markers (`N.N`) are never tagged**; the sa bcad after a marker is.
8. **Output goes to `0-INBOX/temp/`**, never `1-SOURCES/` or `2-RAILS/`.

---

## Completion check

- [ ] Input file read
- [ ] (Long files) pre-filter run and candidates adjudicated
- [ ] Annotation built in document order, depth descends one level at a time
- [ ] All context/term/restatement strings copied verbatim from the source
- [ ] `tag_inline_toc.py render` exited 0 with a prose-integrity VERIFIED report
- [ ] Output written to `0-INBOX/temp/tagged-<filename>`
- [ ] Ambiguous sections noted for human review

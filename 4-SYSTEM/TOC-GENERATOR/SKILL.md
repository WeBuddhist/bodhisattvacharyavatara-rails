---
name: toc-generator
description: >
  Detect the Sachad (ས་བཅད — the structural topic-announcement markers a
  Tibetan Buddhist commentary uses to divide itself into topics) and insert a
  two-level, clickable table of contents directly into the text: a markdown
  heading for each main topic and a sub-heading for each sub-topic, each with
  a stable block ID, placed exactly where that topic's own text begins. The
  original prose is never altered — only new heading lines are added, and the
  result is always written to a new file. Works on any commentary-style text,
  independent of any particular vault's folder layout.

  Trigger this skill when the user says things like: "add a TOC based on the
  Sachad", "generate a table of contents from the sa bcad", "add a clickable
  TOC to this commentary", "make this text navigable", "insert headings at
  the structural markers", or "add a two-level TOC throughout the text".
---

# TOC Generator

This skill turns the Sachad already present in a commentary into a real,
clickable table of contents: a markdown heading dropped in at each Sachad's
location, nested exactly two levels deep (main topic / sub-topic). Once the
headings are in, any Markdown-aware tool — Obsidian's own Outline panel, a
`[[file#Heading]]` link, a static-site TOC generator — renders a clickable
TOC from them automatically. Nothing else in the file changes.

The work splits into two very different kinds of task, and each is handled
by the party suited to it:

- **Finding the Sachad and judging main-vs-sub (Phase 1)** — this is
  linguistic judgment. Sachad wording varies too much across authors and
  languages for a rule/regex extractor to reliably separate genuine
  structural markers from look-alikes (verse quotations, incidental lists).
  This phase is done **entirely by the model**, reading for meaning. See
  `references/sachad-recognition.md` for the recognition guidance and the
  two-level split rule.
- **Placing the headings safely (Phase 2)** — this is pure mechanics:
  assigning block IDs from depth, inserting heading lines at the right spot,
  and proving byte-for-byte that no existing prose was touched. This phase is
  done **entirely by the bundled script**, `scripts/insert_toc_headings.py`,
  which fails loudly (non-zero exit) on any ambiguity or integrity problem
  rather than silently guessing.

```
  commentary.md
       │
       ▼  PHASE 1 — model, reading for meaning
   Read the text (chunked for large files); for every Sachad, decide:
   is it a main topic (depth 1) or a sub-topic (depth 2)? Record, in
   document order, a short heading title + a verbatim, line-unique
   snippet marking where that topic's own text begins.
       │
       ▼  the annotation (JSON) — see scripts/example-annotation.json
       │
       ▼  PHASE 2 — script, insert_toc_headings.py render
   Assign toc-N / toc-N-M block IDs from depth, insert "## title ^toc-N"
   / "### title ^toc-N-M" heading lines, verify no prose changed, write
   to a NEW file.
       │
       ▼
  commentary.toc.md   (source file untouched)
```

---

## Inputs

| Field | Description |
|---|---|
| `input-file` | Path to the commentary file (any plain-text / Markdown commentary; Tibetan is the common case in this vault, but the method is language-agnostic). |
| `output-file` | Optional. Where to write the result. If omitted, defaults to `<input-stem>.toc.md` next to the input (auto-versioned `-v2`, `-v3`, ... if that already exists). Must never be the same path as `input-file`. |

If `input-file` is missing, ask before doing anything else. Do not guess a
file from context.

---

## Output

A single new file at `output-file` (default `<input-stem>.toc.md`). The
original `input-file` is **never** modified — the script refuses to write to
the same path it read from, and refuses to run at all if the input already
looks like it has toc-generator headings in it (a sign the wrong file was
passed in).

---

## Output file format

Two new heading levels are inserted, and nothing else changes:

```
## <Main topic title> ^toc-1

...existing prose, byte-for-byte unchanged...

### <Sub-topic title> ^toc-1-1

...existing prose, byte-for-byte unchanged...

### <Sub-topic title> ^toc-1-2

...existing prose, byte-for-byte unchanged...

## <Main topic title> ^toc-2

...existing prose, byte-for-byte unchanged...
```

Block-ID scheme: `toc-N` for the Nth main topic in document order;
`toc-N-M` for the Mth sub-topic under main topic N. No zero-padding, no
levels beyond `###` / `toc-N-M` — this skill is deliberately capped at two
levels (see `references/sachad-recognition.md` for how to collapse deeper
Sachad nesting into its nearest depth-2 ancestor instead of adding a third
level).

A blank line separates each inserted heading from the surrounding prose, per
standard Markdown / Obsidian convention, so the headings render correctly
and populate the Outline panel.

---

## Rules

1. **The source file is never altered.** Every run writes to a new file;
   the script hard-refuses to target the input path.
2. **Only two heading levels exist in the output: `##` and `###`.** Deeper
   Sachad nesting is real but is not represented as its own heading — it
   stays as prose under the nearest depth-2 heading.
3. **No prose is inserted, deleted, reordered, or retyped.** The only
   changes versus the source are the inserted heading lines. The script
   proves this with a line-by-line diff before writing and aborts on any
   mismatch — never work around a mismatch by hand-editing the source.
4. **Block IDs are assigned by the script, from depth, never by the model.**
   The model supplies only `depth` (1 or 2) per section, in document order.
5. **Body-start contexts must be verbatim, unique spans** copied exactly
   from the source (whole lines are safest). The script errors loudly if a
   context is missing or ambiguous — lengthen it rather than guessing.
6. **Do not write a rule/regex Sachad extractor.** Phase 1 is model
   judgment, guided by `references/sachad-recognition.md`; the only script
   in this skill is the Phase-2 renderer.
7. **Idempotent by construction.** Re-running on the same untouched source
   with the same annotation reproduces the same output; running the script
   on an already-tagged file is refused outright (see Rule 1).

---

## Procedure

### Step 1 — Confirm inputs

Confirm `input-file` exists and is readable. Confirm/derive `output-file`
(default `<input-stem>.toc.md`). If the file already contains lines matching
`## ... ^toc-N` or `### ... ^toc-N-M`, stop — it has already been processed;
confirm with the user whether they meant to pass the original file instead.

### Step 2 — Read for Sachad (Phase 1, model)

Read `references/sachad-recognition.md` once if you have not already this
session — it has the recognition heuristics and the worked example for the
two-level split.

Read the commentary. For files short enough to fit comfortably in context,
read it in one pass. For long files (roughly beyond a few thousand lines —
common for full commentaries in this vault), read it in sequential chunks
(e.g. via the Read tool's `offset`/`limit`, or one chapter/major-division at
a time) so nothing is missed, keeping a single running list of sections in
document order across chunks. For very large files, dispatching one
sub-agent per chapter/major-division (each returning its slice of sections
in order) is a reasonable way to parallelize this step — just concatenate
the slices back into document order afterward.

For every genuine Sachad you find (see the reference doc for what counts),
record, in document order:

- `depth`: `1` (main topic) or `2` (sub-topic) — never deeper
- `heading_title`: the short topic name (not the full ordinal phrase — the
  term itself, e.g. `འགྱུར་ཕྱག`, not `གཉིས་པ་འགྱུར་ཕྱག་ནི།`)
- `body_start_context`: a verbatim excerpt — ideally the whole line — from
  the point where that topic's own text begins, chosen so it is unique in
  the file

### Step 3 — Assemble the annotation

Write the sections list to a JSON file (e.g. `<input-stem>.annotation.json`
next to the input, or under a scratch/temp location if this vault has one),
matching the schema in `scripts/example-annotation.json`:

```json
{
  "source_file": "<input-file>",
  "sections": [
    {"depth": 1, "heading_title": "...", "body_start_context": "..."},
    {"depth": 2, "heading_title": "...", "body_start_context": "..."}
  ]
}
```

### Step 4 — Render + verify (Phase 2, the script)

```bash
python3 4-SYSTEM/TOC-GENERATOR/scripts/insert_toc_headings.py render \
    --input  <input-file> \
    --annot  <input-stem>.annotation.json \
    --output <output-file>
```

The script assigns block IDs, inserts the heading lines, and verifies prose
integrity before writing anything. It exits non-zero and explains exactly
what to fix on any problem:

- *context not found* / *context is ambiguous* → lengthen
  `body_start_context` (use the full line) so it is unique.
- *depth must be 1 or 2* → a Step 2 slip; deeper Sachad nesting must be
  collapsed into its depth-2 ancestor, not given depth 3+.
- *a sub-topic appears before any main topic* → the first section in
  document order must be depth 1.
- *input already contains toc-generator heading markers* → the wrong file
  (an already-tagged output) was passed as `--input`.
- *PROSE INTEGRITY VIOLATION* → a context span was not truly verbatim, or
  overlapped another insertion; fix the annotation and re-run. Never patch
  around this by editing the source.

You can independently re-check any output at any time:

```bash
python3 4-SYSTEM/TOC-GENERATOR/scripts/insert_toc_headings.py verify \
    --input <input-file> --output <output-file>
```

### Step 5 — Report

Tell the user: the output file path, the count of main topics and
sub-topics inserted, and that the source file was left untouched. Mention
that Obsidian's Outline panel (or any `[[file#Heading]]` link) now serves as
the clickable TOC — no separate TOC block is needed unless they ask for one.

---

## Completion check

- [ ] `input-file` confirmed to exist and not already tagged
- [ ] Sachad read for meaning (chunked if large), not pattern-matched by code
- [ ] Every recorded section has `depth` 1 or 2 only — no deeper level
- [ ] Annotation JSON written, matching `scripts/example-annotation.json`
- [ ] `insert_toc_headings.py render` exited 0 with prose integrity VERIFIED
- [ ] Output written to a **new** file; the original `input-file` is
      byte-for-byte unchanged
- [ ] User told the output path, the main/sub-topic counts, and that the
      headings alone drive the clickable TOC

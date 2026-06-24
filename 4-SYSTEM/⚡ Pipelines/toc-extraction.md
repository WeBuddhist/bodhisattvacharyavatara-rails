# Pipeline — TOC (ས་བཅད) extraction

**Goal.** Reconstruct a Tibetan commentary's own table of contents (ས་བཅད / *sa bcad* / dkar-chag) — the nested, decimal-numbered structural outline the author announces inline — and produce a clean tree ready for review and ingest.

**When to run.** After a commentary has been cleaned and formatted, when you want its structural skeleton: either as a standalone outline document or as the basis for inline TOC tagging and section-level rails.

![[toc-extraction.excalidraw.md]]

There are **two ways** to run this flow. The automated script does the whole thing end to end; the skill-by-skill route gives finer human control at each stage. They share the same underlying prompts.

---

## Inputs

- A Tibetan commentary file (`.md` or `.txt`), ideally already cleaned/formatted.
- A `GEMINI_API_KEY` environment variable (the extraction calls Google Gemini Flash).
- A short commentary id for naming outputs (inferred from the filename if not given).

---

## Route A — automated, one script

[`../Scripts/toc_tree_extractor/`](../Scripts/toc_tree_extractor/) runs every stage in sequence. Double-click [`run_extract_toc.bat`](../Scripts/toc_tree_extractor/run_extract_toc.bat) (prompts for the API key and file path) or run [`extract_toc_tree.py`](../Scripts/toc_tree_extractor/extract_toc_tree.py) directly.

| Stage | What it does | Produces |
|---|---|---|
| 1. Chunk | Split the file into overlapping line windows (default 150 lines, 25 overlap). | in-memory chunks |
| 2. Candidates (pass 1) | Each chunk → Gemini extracts sa-bcad section titles (Type A announcements, Type B node headers, Type C closing counts) as `CONTEXT / SECTION_TITLE / ITEMS` blocks. Resumable. | `0-INBOX/temp/TOC-<id>/candidates/chunk_NNN.md` |
| 3. Enumerations (pass 2) | Each chunk → Gemini copies the author's division announcements **verbatim**, no interpretation. Resumable. Skip with `--no-enum`. | `0-INBOX/temp/TOC-<id>/enumerations/chunk_NNN.md` |
| 4. Combine | Merge candidate chunks (with frontmatter); assemble enumerations into one block. | `0-INBOX/toc-candidates-<id>.md` |
| 5. Build tree | Candidates + enumerations → Gemini reconciles them (enumerations are authoritative: drop false positives, fill structural gaps) into a nested decimal-numbered tree. Skip with `--no-tree`. | `0-INBOX/toc-tree-<id>.md` |
| 6. QC | Deterministic checker (indentation, decimal-vs-Tibetan-ordinal agreement, duplicate decimals, gap-free siblings, attestation against the extracted corpus to catch hallucinations), then optional LLM repair. Control with `--no-qc` / `--no-qc-fix`. | `0-INBOX/toc-tree-qc-<id>.md` |

Re-running skips chunks whose result files already exist (use `--force` to redo all), so an interrupted run resumes from where it stopped.

---

## Route B — skill by skill

Use the skills directly when you want to review and edit between stages.

1. **Extract candidates** — [`../Skills/toc-candidate-extraction/SKILL.md`](../Skills/toc-candidate-extraction/SKILL.md). Same chunk-and-extract logic as the script (it bundles the script); prioritises recall. Produces `0-INBOX/toc-candidates-<id>.md`.
2. **Build the nested TOC** — [`../Skills/add-toc/SKILL.md`](../Skills/add-toc/SKILL.md). Takes a flat draft outline list and reconstructs the hierarchy into a nested, decimal-numbered TOC tagged with `^toc-X-Y-Z` block IDs. Output to `0-INBOX/temp/`.
3. **Tag inline TOC** — [`../Skills/tag-inline-toc/SKILL.md`](../Skills/tag-inline-toc/SKILL.md). Wraps the announced terms in `[[#^N-N-0|term]]` wikilinks and inserts standalone heading lines with block IDs (per [`../CLAUDE.md`](../CLAUDE.md) §5b). Run after `format-commentary`, before ingest. Output to `0-INBOX/temp/`.

---

## Outputs

All under `0-INBOX/` (drafts — **not** authoritative until human-reviewed and ingested):

- `toc-candidates-<id>.md` — merged section candidates with frontmatter.
- `toc-tree-<id>.md` — the nested, decimal-numbered TOC tree (Tibetan, no `^toc` block IDs from the script route).
- `toc-tree-qc-<id>.md` — QC report: issues found, whether repaired, issues remaining.
- `0-INBOX/temp/TOC-<id>/candidates/` and `.../enumerations/` — per-chunk staging (resumable intermediates).

---

## Notes

- The flow is **recall-first then precision**: extract generously, then reconcile against the author's verbatim enumerations and QC against attested strings.
- Outputs land in `0-INBOX/`, which is scratch. A human reviews the tree before it feeds anything downstream; tagging into a `1-SOURCES/` file requires review (see `tag-inline-toc`).
- **Next stages.** A reviewed TOC feeds inline-TOC tagging and then `structural-outline-ingest`, and underpins the per-node summaries in `2-RAILS/Sections/` (`section-summary-raw` → `section-summary-combined`).

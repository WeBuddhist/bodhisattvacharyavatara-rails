---
name: split-file-by-markers
description: Split a single source file into multiple files at explicit, user-specified cut points, using scripts/split_chapters.py. Use whenever the user wants to split a long document into per-chapter (or per-section) files and can point to where each section starts — the skill's job is to work out the exact marker/line for each cut with the user, the script just does the mechanical cutting. Trigger on phrases like "split this file by chapter," "break this into per-chapter files," or "cut the source into pieces."
---

# Split File by Markers

Splits one source file into several output files at cut points the user specifies explicitly — this skill does not guess chapter boundaries from heading level or keywords. It figures out, together with the user (or from a clear pattern they give you), exactly which line starts each section and what to name the resulting file, then hands that off to the script to do the actual cutting.

## Why explicit cut points

Auto-detecting chapter boundaries (by heading level, keyword, etc.) is fragile — a document with inconsistent formatting, a stray extra heading, or unexpected structure produces a silently wrong split. Since the person asking usually already knows exactly where their chapters start (and the source file's headings may not be uniform), it's more reliable to have them name each cut point directly and let the script just execute it precisely, with a clear error if a marker isn't found rather than a guess that's silently off.

## Workflow

1. **Get the cut points.** For each section (intro, chapter 1, chapter 2, ..., colophon, or whatever the source actually contains), you need:
   - A marker: an exact line of text (or a small distinguishing part of it) that appears at the start of that section, in the source file.
   - An output filename for that section.

   If the user hasn't given you the exact marker text, look at just the heading/marker lines of the source (e.g. grep for lines starting with `#`, or ask the user to paste the relevant lines) rather than reading the full body content — you only need to know where the cuts go, not what's in each section.

2. **Order matters.** List `--section` flags in the same order the markers appear in the file. The script searches for each marker starting from just after the previous one, so it won't get confused by a marker text that happens to repeat earlier in the document.

3. **Run the script:**
   ```
   python scripts/split_chapters.py <source_file> [output_dir] \
       --strip-frontmatter \
       --section "MARKER_FOR_INTRO::intro.md" \
       --section "MARKER_FOR_CH1::ch1.md" \
       --section "MARKER_FOR_CH2::ch2.md" \
       --section "MARKER_FOR_COLOPHON_PART1::colophon.md" \
       --section "MARKER_FOR_COLOPHON_PART2::colophon.md"
   ```
   - `--strip-frontmatter` pulls out a leading YAML frontmatter block (if any) into `frontmatter.txt` before cutting, so it doesn't end up glued to the first section.
   - `--regex` treats each marker as a regular expression instead of a literal substring, if a fixed string can't uniquely identify the line.
   - `--keep-preamble` saves any content before the very first marker to `preamble.md` (otherwise it's discarded — usually fine since the first marker should normally be the true start of the file).
   - By default, Obsidian-style transclusion lines (e.g. `![[1-SOURCES/Text/BCAV08_SH_sk.md#^2-9]]`) are stripped out of every output section, since they're references to another file, not translatable content. Pass `--keep-transclusions` to keep them instead.
   - **Multiple `--section` entries can share the same output filename.** This is the right move for small trailing pieces that logically belong together but come from separate headings — e.g. a composer's colophon and a translators' colophon. The first section with a given name starts that file; every later section with the same name gets appended to it (in the order given), so you end up with one small `colophon.md` instead of two nearly-empty files.

## Where the output goes

The script always creates a subfolder named `<source_file_stem>_split_chapters` and writes into it — it never scatters loose files directly into an existing folder.
- **No `output_dir` given:** that subfolder is created right next to the source file. E.g. splitting `1-SOURCES/source.md` produces `1-SOURCES/source_split_chapters/ch1.md`, etc.
- **`output_dir` given** (relative or absolute): the same subfolder is created inside that directory instead. E.g. splitting `1-SOURCES/source.md` with `output_dir` set to `AI_translation` produces `AI_translation/source_split_chapters/ch1.md`, etc.

4. **Check the script's own output.** It prints the line range and matched marker for each section it wrote — a quick sanity check that, say, chapter 3 isn't suspiciously short or chapter 4 didn't swallow half of chapter 5. If a marker isn't found, the script stops with an error naming the missing marker rather than guessing — fix the marker text and re-run.

## Notes

- This skill is a mechanical cutting tool, not a chapter-detection tool. If the user wants automatic detection instead (e.g. "just split wherever there's a new chapter heading"), that's a different, fuzzier task — confirm with them whether they'd rather give explicit markers (this skill) or have you infer boundaries from heading patterns.
- Output naming is entirely up to whatever the user specifies in each `--section` flag — this skill doesn't assume a fixed `chN.md` convention, though that's a common choice.

---
name: colophon-metadata-extractor
description: Extracts author, title, and language from a Tibetan text's colophon (last 200 syllables) and opening (first 200 syllables), populates frontmatter, and saves the file as lang_tag-author_name.md in the same folder.
---

# colophon-metadata-extractor

This skill extracts structured metadata from unprocessed Tibetan source files (typically Derge catalog files named `D*.txt` in `1-SOURCES/Commentaries/raw/`) by analysing the first and last 200 syllables of the text. It uses the LLM to identify the author, title, language, and other colophon information, then writes a new `.md` file with populated YAML frontmatter and the original text content. The output filename follows the vault convention: `{lang_tag}-{author_name_in_original_script}.md`.

This skill prevents the common failure mode of manually guessing metadata or reading entire large files when the relevant information is concentrated in the title block and colophon.

---

## Inputs

| Input | Description | Required |
|---|---|---|
| `file_path` | Path to a source file in `1-SOURCES/Commentaries/raw/` whose filename starts with `D` (e.g. `D3872.txt`) | yes |
| `batch` | If `true`, process all `D*` files in `1-SOURCES/Commentaries/raw/` sequentially. Overrides `file_path`. | no (default: `false`) |

If neither `file_path` nor `batch: true` is provided, ask the user which file(s) to process.

## Output

One new file per input, saved to the same folder (`1-SOURCES/Commentaries/raw/`):

```
1-SOURCES/Commentaries/raw/{lang_tag}-{author_name_in_original_script}.md
```

Example: `1-SOURCES/Commentaries/raw/bo-མཁས་པ་ཤེས་རབ་འབྱུང་གནས།.md`

The original `D*.txt` file is **not** modified or deleted.

---

## Output file format

```yaml
---
title:                        # exact title of the work in original script
title_in_english:             # English translation of the title
author:                       # author name in original script
author_in_english:            # romanized/English author name
file_type: commentary
language: Tibetan             # or Sanskrit, Chinese, etc.
lang_tag: bo                  # ISO-style tag: bo, sk, zh, en, etc.
source_description: ""        # to be filled by user later
derge_catalog_id:             # original D-number, e.g. D3872
---
```

Followed by the complete original text content (unchanged).

---

## Rules

1. **Syllable extraction uses tseg and shad as delimiters.** Split the text using the regex pattern `[་།]` (Tibetan tseg `་` U+0F0D and shad `།` U+0F0B). Each non-empty segment after splitting counts as one syllable.
2. **Extract exactly 200 syllables from the end** (the colophon region) and **200 syllables from the beginning** (the title region). If the file has fewer than 400 syllables total, use the entire text.
3. **Do not read the middle of the text.** The skill must work without loading the full file body into the LLM context. Read only the head and tail regions.
4. **The LLM analyses only the extracted syllable regions.** From the colophon region, extract: author name, translator name (if present), place of composition (if present), and any closing dedication or attribution. From the title region, extract: formal title and Sanskrit/alternate title (if present).
5. **Author name in the output filename must use original script** (Tibetan, Sanskrit, etc.), matching the existing vault convention (e.g. `bo-འཇུ་མི་ཕམ།.md`).
6. **The `lang_tag` is determined from the text content**, not assumed. Most D-files are Tibetan (`bo`), but verify from the opening lines (look for `རྒྱ་གར་སྐད་དུ།` / `བོད་སྐད་དུ།` markers).
7. **The `derge_catalog_id` is extracted from the original filename** (e.g. `D3872` from `D3872.txt`).
8. **Do not overwrite existing files.** If `{lang_tag}-{author_name}.md` already exists in the target folder, append a numeric suffix: `{lang_tag}-{author_name}-2.md`.
9. **Do not modify the original D-file.** The original file is preserved as-is.
10. **If the LLM cannot confidently identify the author**, use the title as a fallback for the filename: `{lang_tag}-{title_short}.md`, and set `author: unknown` in frontmatter. Report this to the user.

---

## Procedure

### Step 1 — Validate the input file

1. Confirm the file exists at the given path in `1-SOURCES/Commentaries/raw/`.
2. Confirm the filename starts with `D`.
3. Extract the Derge catalog ID from the filename (e.g. `D3872`).

### Step 2 — Extract syllable regions

1. Read the **first 3,000 characters** of the file (this generously covers 200+ syllables for the title region).
2. Read the **last 3,000 characters** of the file (this generously covers 200+ syllables for the colophon region).
3. For each region, split the text by the regex pattern `[་།]` and filter out empty strings.
4. From the beginning region, take the **first 200 syllable tokens** and rejoin them with their original delimiters (preserve the original text).
5. From the ending region, take the **last 200 syllable tokens** and rejoin them with their original delimiters (preserve the original text).

### Step 3 — LLM metadata extraction

Present the two extracted regions to the LLM with the following prompt structure:

```
You are analysing a classical Tibetan Buddhist text. Below are the TITLE REGION (first 200 syllables) and COLOPHON REGION (last 200 syllables) of the text.

TITLE REGION:
{title_region_text}

COLOPHON REGION:
{colophon_region_text}

Extract the following metadata. Return ONLY the metadata in this exact format, with no additional commentary:

title: [exact title in original script]
title_in_english: [English translation of the title]
author: [author name in original script]
author_in_english: [romanized/English author name]
translator: [translator name if mentioned, otherwise "none"]
language: [primary language of the text]
lang_tag: [ISO tag: bo, sk, zh, en]

If you cannot determine a field with confidence, write "unknown".
```

### Step 4 — Construct the output file

1. Build the YAML frontmatter block using the extracted metadata and the Derge catalog ID.
2. Read the **entire original file content** (the raw text, not just the extracted regions).
3. Combine: frontmatter block + blank line + original file content.
4. Determine the output filename: `{lang_tag}-{author_name}.md`
   - Strip any trailing punctuation from the author name for the filename if it would cause issues, but keep the Tibetan shad `།` as it matches existing vault convention.
   - If author is `unknown`, use a short form of the title instead.

### Step 5 — Write the output file

1. Check that no file with the target name already exists. If it does, append `-2` (or `-3`, etc.).
2. Write the new file to `1-SOURCES/Commentaries/raw/{output_filename}`.
3. Report to the user: the original filename, the new filename, and the extracted metadata fields.

### Step 6 — Batch mode (if applicable)

If `batch: true`:
1. List all files matching `D*.txt` and `D*.md` in `1-SOURCES/Commentaries/raw/`.
2. For each file, execute Steps 1–5.
3. At the end, report a summary table: original filename → new filename → author → title.

---

## Completion check

- [ ] Syllable extraction used `[་།]` regex, not word-level or line-level splitting
- [ ] Exactly 200 syllables extracted from each end (or full text if shorter)
- [ ] Middle of the text was not read into LLM context
- [ ] Output file has complete YAML frontmatter with all fields populated (or marked `unknown`)
- [ ] Output filename follows `{lang_tag}-{author_name_in_original_script}.md` convention
- [ ] `derge_catalog_id` in frontmatter matches the original filename
- [ ] Original D-file is unmodified
- [ ] No existing file was overwritten

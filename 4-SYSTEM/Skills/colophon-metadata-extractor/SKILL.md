---
name: colophon-metadata-extractor
description: Extracts author, title, and language from a Tibetan text's colophon (last 200 syllables) and opening (first 200 syllables), and populates the YAML frontmatter (Properties) of the same file in place. Does not rename or move the file.
---

# colophon-metadata-extractor

This skill extracts structured metadata from Tibetan source files (typically Derge catalog files in `1-SOURCES/Commentaries/raw/`) by analysing the first and last 200 syllables of the text. It uses the LLM to identify the author, title, language, and other colophon information, then writes the extracted metadata into the YAML frontmatter (Properties) of the **same file**, leaving the filename and body content unchanged.

This skill prevents the common failure mode of manually guessing metadata or reading entire large files when the relevant information is concentrated in the title block and colophon.

---

## Inputs

| Input | Description | Required |
|---|---|---|
| `file_path` | Path to a source file in `1-SOURCES/Commentaries/raw/` whose filename starts with `D` (e.g. `D3872.txt`) | yes |
| `batch` | If `true`, process all `D*` files in `1-SOURCES/Commentaries/raw/` sequentially. Overrides `file_path`. | no (default: `false`) |

If neither `file_path` nor `batch: true` is provided, ask the user which file(s) to process.

## Output

The input file is updated in place: its YAML frontmatter (Properties) is populated with the extracted metadata. The filename and body content are **not changed**.

---

## Frontmatter schema

The following fields are written into the file's YAML frontmatter block. If a frontmatter block already exists, update only these fields; leave any other existing fields untouched. If no frontmatter block exists, prepend one.

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

The body content of the file is **not modified**.

---

## Rules

1. **Syllable extraction uses tseg and shad as delimiters.** Split the text using the regex pattern `[་།]` (Tibetan tseg `་` U+0F0D and shad `།` U+0F0B). Each non-empty segment after splitting counts as one syllable.
2. **Extract exactly 200 syllables from the end** (the colophon region) and **200 syllables from the beginning** (the title region). If the file has fewer than 400 syllables total, use the entire text.
3. **Do not read the middle of the text.** The skill must work without loading the full file body into the LLM context. Read only the head and tail regions.
4. **The LLM analyses only the extracted syllable regions.** From the colophon region, extract: author name, translator name (if present), place of composition (if present), and any closing dedication or attribution. From the title region, extract: formal title and Sanskrit/alternate title (if present).
5. **The `lang_tag` is determined from the text content**, not assumed. Most D-files are Tibetan (`bo`), but verify from the opening lines (look for `རྒྱ་གར་སྐད་དུ།` / `བོད་སྐད་དུ།` markers).
6. **The `derge_catalog_id` is extracted from the original filename** (e.g. `D3872` from `D3872.txt`).
7. **Do not rename or move the file.** Only the frontmatter of the existing file is updated.
8. **Do not modify the body content of the file.** Only the YAML frontmatter block is written or updated.
9. **If the LLM cannot confidently identify the author**, set `author: unknown` in frontmatter and report this to the user.

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

### Step 4 — Build the frontmatter block

Build the YAML frontmatter using the extracted metadata and the Derge catalog ID.

### Step 5 — Write the frontmatter into the existing file

1. Read the current content of the input file.
2. If the file already begins with a `---` frontmatter block, replace it with the new frontmatter. Preserve all body content exactly.
3. If no frontmatter block exists, prepend the new frontmatter block (followed by a blank line) before the existing content.
4. Write the updated content back to the **same file** at the same path. Do not change the filename or move the file.
5. Report to the user: the filename, and the extracted metadata fields.

### Step 6 — Batch mode (if applicable)

If `batch: true`:
1. List all files matching `D*.txt` and `D*.md` in `1-SOURCES/Commentaries/raw/`.
2. For each file, execute Steps 1–5.
3. At the end, report a summary table: filename → author → title.

---

## Completion check

- [ ] Syllable extraction used `[་།]` regex, not word-level or line-level splitting
- [ ] Exactly 200 syllables extracted from each end (or full text if shorter)
- [ ] Middle of the text was not read into LLM context
- [ ] Frontmatter has all fields populated (or marked `unknown`)
- [ ] `derge_catalog_id` in frontmatter matches the original filename
- [ ] Filename is unchanged
- [ ] Body content of the file is unmodified

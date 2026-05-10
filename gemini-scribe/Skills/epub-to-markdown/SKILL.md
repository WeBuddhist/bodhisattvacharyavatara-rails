---
name: epub-to-markdown
description: Convert EPUB source files to scholarly Markdown for the 1-SOURCES folder. This skill ensures compliance with the vault's Railroads methodology, including TOC-to-heading mapping, verse block IDs, Chapter 0 handling, and YAML frontmatter extraction.
---

# EPUB to Markdown Conversion Skill

This skill provides a rigorous workflow for converting EPUB source files into the scholarly Markdown format required by the **Railroads** methodology in this vault. It ensures that primary sources, translations, and commentaries are formatted with precise block IDs, structural headings, and metadata.

## 1. Preparation & Extraction

EPUB files are binary containers. If the agent cannot read the EPUB directly using `read_file`, use the following approach:
1. **Search for Web Converters**: Use `google_search` to find a command-line or web-based tool (like Pandoc) if the environment allows, or instructions for the user.
2. **Request Text/HTML**: Ask the user to provide the extracted text or HTML content if conversion is not possible within the session.
3. **Analyze TOC**: Identify the internal structure (Navigation Map) of the EPUB to plan the heading hierarchy.

## 2. Metadata & Frontmatter

Extract the following from the EPUB metadata and format it into the YAML frontmatter at the very top of the note:

```yaml
---
title: "Full Title"
author: "Author Name"
translator: "Translator Name (if applicable)"
date: "Publication Date/Century"
language: "Language Name"
file_type: "root-text | translation | commentary"
lang_tag: "iso-code (e.g., en, sk, bo)"
verse_id_format: "chapter-verse"
source_description: "Detailed source info (e.g., ISBN, Publisher, Year)"
---
```

Refer to [[1-SOURCES-Guideline]] for additional fields like `bdrc_work_id` or `covers_verses`.

## 3. Structural Mapping

Map the EPUB's logical structure to Markdown headings:
- **H1**: The main title of the work (only one per file).
- **H2**: Chapters or major Books.
- **H3**: Sub-sections or internal divisions.
- **H4+**: Do not use. Use block IDs for granular navigation.

**Constraint**: If the EPUB has a Table of Contents, use those exact titles for the H2/H3 headings.

## 4. Verse Formatting & Block IDs

Verses must be formatted as follows:
1. **Placement**: The block ID goes on the last line of the verse, after the final character, preceded by a single space.
2. **Format**: `^chapter-verse` (e.g., `^1-1`, `^6-33`). No zero-padding.
3. **Numbering**: Verse numbers **must restart at 1** for each chapter (H2).
4. **Prose**: For commentaries or prose translations, the block ID goes at the end of the paragraph or passage corresponding to a verse.

Example:
```markdown
## Chapter 1: The Excellence of Bodhicitta

Having paid homage to the Sugatas... ^1-1

This is the second verse... ^1-2
```

## 5. Chapter 0 (Pre-Chapter Content)

Any content preceding the first authored chapter (Title lines, colophons, homages, introductions) must be placed under a `## 0. Introduction` heading.
- Verses in this section are numbered `^0-1`, `^0-2`, etc.

## 6. Language Tags & Filenaming

Apply the correct language tag to the filename and the `lang_tag` property:
- **Sanskrit**: `-sk` (Devanagari), `-sk-iast` (IAST)
- **Tibetan**: `-bo` (Unicode), `-bo-wy` (Wylie)
- **Chinese**: `-zh` (Traditional), `-zh-hans` (Simplified)
- **English**: `-en`
- **Standard**: `[language]-[name/surname].md` (lowercase, hyphenated, no diacritics).

## 7. Cleaning & Normalization

- **OCR Artifacts**: Remove page numbers, running headers, and footers.
- **Scripts**: Ensure Tibetan and Chinese use Unicode. Sanskrit should be Devanagari for root texts and IAST for editions.
- **Editorial Notes**: Mark any editor-added content or clarifications as `[Ed: ...]` in English.

## 8. Final Checklist

Before saving to `1-SOURCES/`:
- [ ] Does every verse have a `^chapter-verse` block ID?
- [ ] Did verse numbering restart at 1 for each H2 chapter?
- [ ] Is the frontmatter complete with `source_description`?
- [ ] Is the filename correctly tagged (e.g., `en-crosby.md`)?
- [ ] Is the "Chapter 0" convention followed for introductory material?
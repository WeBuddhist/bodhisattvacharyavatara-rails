# EPUB to Markdown Extraction Skill (Python-Assisted)

This skill provides a workflow for extracting content from EPUB source files into clean, structured Markdown. It focuses on preserving the original text, hierarchy, and formatting (headings, lists, links) without applying any methodology-specific transformations like block IDs or structural outlines.

## 1. Automated Extraction

Use the provided Python script `4-SYSTEM/Skills/epub-to-markdown/epub_to_markdown.py` to perform the extraction. This script handles the parsing of the EPUB container and converts HTML elements into their Markdown equivalents.

**Command Usage:**
```bash
python 4-SYSTEM/Skills/epub-to-markdown/epub_to_markdown.py path/to/source.epub path/to/output.md
```

**What the script automates:**
- **Metadata**: Extracts Title, Author, Date, and Language into YAML frontmatter.
- **Heading Hierarchy**: Preserves H1 through H6 tags.
- **Formatting**: Preserves bold, italic, and hyperlinks within paragraphs.
- **Lists**: Converts unordered and ordered lists to Markdown syntax.
- **Blockquotes**: Converts blockquote tags to Markdown `> ` syntax.
- **Cleaning**: Removes scripts, styles, and redundant whitespace.

## 2. Post-Extraction Review

After running the script, review the output to ensure data integrity:

### 2.1 Metadata Check
Verify the YAML frontmatter. Ensure the `title`, `author`, and `language` fields are accurate. You may want to add a `source_url` or `isbn` if available.

### 2.2 Structural Integrity
- **Headings**: Ensure the heading hierarchy correctly reflects the source's structure.
- **Broken Links**: Check for any internal EPUB links that may not resolve correctly in a single Markdown file.
- **OCR/Encoding**: Check for characters that might have been misidentified during the EPUB's original creation (especially in Tibetan or Chinese texts).

## 3. Usage in the Vault

This tool is intended for the initial "ingestion" phase. Once the text is extracted:
- Move the file to `0-INBOX/` or a relevant working directory.
- If the text is intended for the `1-SOURCES/` directory, it will likely require further manual formatting (e.g., adding block IDs, cleaning OCR artifacts) according to the [[1-SOURCES-Guideline]].

## 4. Limitations

- **Images**: The current script does not extract image files; it only preserves text.
- **Complex Tables**: Tables are currently ignored or stripped of formatting; they may require manual reconstruction.
- **CSS Layouts**: Complex CSS-based layouts (like sidebars or multi-column text) are flattened into a linear stream.

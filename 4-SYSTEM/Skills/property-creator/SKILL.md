---
name: property-creator
description: Adds standard properties to a file by extracting details from its title and colophon.
version: 1.0.0
---

# Property Creator

This skill extracts metadata from a file's title and colophon to populate standard YAML frontmatter properties, saving time and context by bypassing the main body text.

## Instructions

When asked to run this skill on a specific file (e.g., "add properties to [filename]"):

1. **Read the File:** Use the `read_file` tool to retrieve the content of the target file.
2. **Focus on Metadata:** Do not read or analyze the entire body text. Only examine the title (usually at the very top) and the colophon (publication/source information typically found at the beginning or end of the document).
3. **Extract Properties:** Identify the following details from those specific sections:
   - `title`: The original title of the work, copied exactly as it appears in the file — including any trailing punctuation such as །། (shad).
   - `title in English`: The English translation of the title.
   - `author`: The original author.
   - `author in English`: The English translation or transliteration of the author's name.
   - `file_type`: The type of document (e.g., root text, commentary, book, article, essay).
   - `language_tag`: The primary language of the text.
   - `source_description`: A brief description of the source material derived from the colophon.
4. **Update File:** Use the `update_frontmatter` tool to inject these properties into the file's YAML frontmatter. You will need to call `update_frontmatter` for each property you find.
## Example: bo-དངུལ་ཆུ་ཐོགས་མེད།
![[Pasted image 20260511170942.png]]
## Rules & Edge Cases
- **Do not hallucinate:** If a specific piece of information (like an English translation) is not available in the title or colophon, do not invent it. Either skip that property or leave it empty.
- **Efficiency:** Stick strictly to the title and colophon to keep processing fast and focused.
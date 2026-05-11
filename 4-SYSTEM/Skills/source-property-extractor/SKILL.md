---
name: source-property-extractor
description: Extracts title and colophon metadata from source texts to add as properties, looking only at the first and last pages.
---

# Source Property Extractor

This skill defines the standard procedure for extracting metadata from source texts in the `1-Human-Sources` (or `1-SOURCES`) folder and adding them as frontmatter properties.

## Context
Source texts (especially traditional Tibetan and Chinese texts, like commentaries and root texts) contain their title at the very beginning (first page) and their publication, author, or translator metadata in the colophon at the very end (last page). 

## Directives
To save processing time, preserve context, and ensure accuracy, **do not analyze the middle of the text**. 

1. **First Page (Title):** Examine only the beginning of the text to extract the main title. Look for traditional title markers (e.g., in Tibetan: `༄༅། །... ཞེས་བྱ་བ་བཞུགས་སོ། །`).
2. **Last Page (Colophon):** Examine only the final paragraphs/lines of the text to extract colophon information, which typically includes the author, translator, scribe, location, and date.
3. **Apply Properties:** Use the `update_frontmatter` tool to add the extracted metadata to the file safely.

## Recommended Properties
When extracting, aim to populate the following properties:
- `title`: The formal title of the work.
- `author`: The author or composer (e.g., Zhechen Gyaltsab Gyurme Pema Namgyal).
- `translator`: The translator, if applicable.
- `colophon`: A brief summary or transcription of the colophon details.

## Example: `bo-ཞེ་ཆེན་རྒྱལ་ཚབ་འགྱུར་མེད་པདྨ་རྣམ་རྒྱལ།`
If a user asks you to add properties to a file like `bo-ཞེ་ཆེན་རྒྱལ་ཚབ་འགྱུར་མེད་པདྨ་རྣམ་རྒྱལ།`:
1. Read the file content.
2. Look at the top-most lines to identify the title.
3. Look at the bottom-most lines to identify the colophon.
4. Ignore the rest of the text body.
5. Call `update_frontmatter` to inject `title`, `author`, and `colophon` properties based on what you found.

## Important Note
Always use the `update_frontmatter` tool to apply these changes rather than using `write_file` to rewrite the entire document. This ensures that the extensive root text or commentary in the middle remains completely untouched and safe.
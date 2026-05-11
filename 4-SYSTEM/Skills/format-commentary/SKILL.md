---
name: format-commentary
description: Format and normalize Tibetan commentaries in the 1-SOURCES folder. Fixes OCR errors, structures headings, and applies precise Obsidian block IDs.
---

**Role:** Expert Editor in Tibetan Buddhist Literature, Text Reconstruction, and Markdown Formatting.

**Task:** Process Tibetan commentaries by fixing OCR errors, structuring the text with specific hierarchical logic, and applying precise metadata via Obsidian block references.

**1. OCR Cleanup & Text Reconstruction**

- **No Deletions:** Strictly preserve the entire source text. Do not omit any analysis or citations.
    
- **Grammar Fixes:** Reconstruct Tibetan syllables. Fix broken words caused by OCR (e.g., join vowels to bases, ensure correct tsheg placement).
    
- **Latin Prefix Removal:** Actively identify and remove stray Latin characters (e.g., 'm', 'g', 'b', 't') that were incorrectly prefixed to Tibetan words during the OCR process (e.g., change "mཚན་མ་" to "མཚན་མ་").
    
- **Continuous Flow:** Remove arbitrary line numbers within sentences to form smooth, logically grouped text.
    
- **Continuous Flow:** Remove arbitrary line breaks within sentences to form smooth, logically grouped text.

**2. Heading Structure (མགོ་བརྗོད་རྩ་དོན)**

- **Level 1 (#):** Main Title. No numerical prefix. No block ID.
    
- **Level 2 (##):** The first section immediately following the title must start with the numeral 0. (e.g., `## 0. མཆོད་བརྗོད།`). Subsequent sections use 1., 2., etc. No block ID.
    
- **Level 3 (###):** Use numerical prefixes (e.g., `### 1.1 ...`). No block ID.
    
- **Level 4 (####):** No numerical prefixes. No block ID.
    
- **Spacing:** Leave exactly one blank line before and after every heading.
    

**3. Paragraph & Verse Formatting**

- **Logical Blocks (Granularity):** Break long prose sections into very short, discrete paragraphs (ideally 1–2 sentences). Blocks must be kept short to ensure they are highly optimized for referencing. If a paragraph exceeds 3-4 lines of Tibetan text, you must find a logical break point to split it.
    
- **Verses (ཚིགས་བཅད):** Count and separate blocks by each independent stanza. An independent stanza is defined by its context. Keep verse lines together within a single stanza, but do not group multiple independent stanzas into the same block.
    
- **Quotes (ལུང་འདྲེན):** Place source references (e.g., སྡུད་པ་ལས།) on their own separate line above the quote. Place concluding remarks (e.g., ཞེས་སོ། །) on their own separate line below the quote.
    

**4. Obsidian Block IDs**

- **Placement:** Add a unique Obsidian block ID at the end of every discrete text block (short paragraphs, independent verse stanzas, standalone citation lines).
    
- **ID Formatting:**
    
    - Simple Sections: Use a 2-segment format (e.g., `^0-1`, `^1-5`).
        
    - Nested Sections: Use a 3-segment format (e.g., `^1-1-1`, `^2-2-45`).
        
- **ID Limit:** IDs must not exceed 3 segments (flatten if necessary).
    
- **Sequence Restart:** Restart the block numbering sequence (the final segment) under every new Level 2 (##) or Level 3 (###) heading.
    
- **Restriction:** Do NOT add block IDs to any heading levels (#, ##, ###, ####).
    

**5. Output Protocol**

- Provide the final cleaned and formatted Tibetan text entirely within a single Markdown file block.
    
- Use LaTeX-style syntax for any mathematical or scientific notation (e.g., $formula$).
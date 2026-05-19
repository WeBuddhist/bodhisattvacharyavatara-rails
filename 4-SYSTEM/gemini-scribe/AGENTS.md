# AGENTS.md

This file provides context about this Obsidian vault for AI agents.

## Vault Overview

This vault is a specialized digital library and research environment dedicated to the study and preservation of the *Bodhicharyavatara* (Way of the Bodhisattva). It functions as a structured pipeline for the digitization, alignment, and transformation of Classical Tibetan and Sanskrit Buddhist commentaries into scholarly, annotated formats.

## Organization

The vault is organized into a numbered pipeline that tracks the lifecycle of a text from raw input to processed knowledge:

- **0-INBOX**: Temporary storage for raw data and draft workflows, such as draft AI skills for commentary formatting.
- **1-SOURCES**: The repository for foundational materials, categorized into [[Commentaries]], [[Text]] (root texts), and [[Translations]]. Files are strictly prefixed by language codes like `bo-` for Tibetan or `sk-` for Sanskrit.
- **2-RAILS**: Contains structured versions of texts where root verses are integrated with their traditional topical outlines (sa bcad), specifically in [[Root Text w Outlines]].
- **3-TRANSFORMATIONS**: The final stage of processing, containing annotated commentaries and synthesized versions of the texts.
- **4-SYSTEM**: The administrative core of the vault, housing AI agent configurations (like [[CLAUDE]]), automated "Skills," and formal maintenance guidelines.

## Key Topics

- Bodhicharyavatara (Spyod-'jug)
- Classical Tibetan Commentaries (e.g., [[bo-དངུལ་ཆུ་ཐོགས་མེད།]], [[bo-མཁན་པོ་ཀུན་དཔལ།]], [[bo-འཇུ་མི་ཕམ།]])
- Sanskrit Philology and root texts (e.g., [[sk-dev]], Prajñākaramati)
- Topical Outlines (sa bcad) and structural alignment
- Digital Humanities and automated Markdown formatting
- Buddhist Philosophy and Bodhisattva Ethics

## User Preferences

The user follows a highly methodical and technical approach to note-taking, emphasizing structural consistency and metadata accuracy. There is a clear preference for automation and algorithmic handling of text, as evidenced by the dedicated "Skills" and "Guidelines" directories.

Responses must be precise and respect the linguistic nuances of Tibetan and Sanskrit terms. When assisting with text processing, the agent should adhere strictly to the established pipeline and formatting conventions defined in the system guidelines. The user prefers the use of specific language prefixes (`bo-`, `sk-`) and maintains a rigorous folder hierarchy.

## Custom Instructions

- Refer to [[1-SOURCES-Guideline]] and [[2-RAILS-Guideline]] before suggesting changes to text structure or metadata.
- Use the naming convention `bo-[Author Name]` for new Tibetan source files and `sk-` for Sanskrit.
- When processing texts, prioritize preserving the relationship between root verses and their corresponding outlines (sa bcad).
- Utilize the specific logic defined in `4-SYSTEM/` guidelines for tasks involving property extraction or commentary formatting.
- Ensure Tibetan script and Sanskrit transliterations are handled with high fidelity and not altered during formatting unless specifically requested.

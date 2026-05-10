# AGENTS.md

This file provides context about this Obsidian vault for AI agents.

## Vault Overview

This vault is a specialized digital library and workspace dedicated to the study and preservation of Classical Tibetan Buddhist texts, with a specific focus on the *Bodhicharyavatara* (Way of the Bodhisattva). It serves as a structured pipeline for digitizing raw source materials, aligning them with traditional outlines, and generating annotated transformations for scholarly study.

## Organization

The vault is organized into a numbered pipeline that tracks the lifecycle of a text from raw input to processed knowledge:

- **0-INBOX**: Temporary storage for raw data and draft workflows.
- **1-SOURCES**: The repository for foundational materials, categorized into [[Commentaries]], [[Text]] (root texts), and [[Translations]]. Files are often prefixed by language codes like `bo-` for Tibetan or `sk-` for Sanskrit.
- **2-RAILS**: Contains structured versions of texts where root verses are integrated with their traditional topical outlines (sa bcad).
- **3-TRANSFORMATIONS**: The final stage of processing, containing annotated commentaries and synthesized versions of the texts.
- **4-SYSTEM**: The administrative core of the vault, housing AI agent configurations, automated "Skills" (like `format-commentary`), and formal guidelines for vault maintenance.

## Key Topics

- Bodhicharyavatara (Spyod-'jug)
- Classical Tibetan Commentaries (e.g., Ngulchu Thogme, Khenpo Kunpal, Prajñākaramati)
- Buddhist Philosophy and Bodhisattva Ethics
- Digital Humanities and Textual Alignment
- Tibetan and Sanskrit Philology
- Automated Markdown Formatting and Property Extraction

## User Preferences

The user follows a highly methodical and technical approach to note-taking, emphasizing structural consistency and metadata accuracy. There is a clear preference for automation and algorithmic handling of text, as seen in the extensive "Skills" and "Prompts" directories.

Responses should be precise and respect the linguistic nuances of Tibetan and Sanskrit terms. When assisting with text processing, the agent should adhere strictly to the established pipeline and formatting conventions defined in the system guidelines.

## Custom Instructions

- Refer to [[1-SOURCES-Guideline]] and [[2-RAILS-Guideline]] before suggesting changes to text structure or metadata.
- Use the naming convention `bo-[Author Name]` for new Tibetan source files.
- When processing texts, prioritize preserving the relationship between root verses and their corresponding outlines (sa bcad).
- Utilize the specific logic defined in `4-SYSTEM/Skills/` for tasks involving property extraction or commentary formatting.

# AGENTS.md

This file provides context about this Obsidian vault for AI agents.

## Vault Overview

This vault is a specialized research and translation environment focused on Shantideva's *Bodhisattvacharyavatara* (A Guide to the Bodhisattva's Way of Life). It serves as a digital scriptorium for comparative philology, housing root texts in Sanskrit, Tibetan, and Chinese alongside a vast collection of traditional commentaries from masters such as Prajñākaramati, Kṣemadeva, and Mipham Rinpoche.

The vault utilizes the **Railroads** methodology to manage the flow of information from raw primary sources to structured, authoritative context and AI-assisted transformations, ensuring high scholarly rigor in Buddhist philosophical studies.

## Organization

The vault is organized according to the **Railroads** methodology, ensuring a clear pipeline from source material to final output:

- **0-INBOX**: Contains raw data and draft skills/instructions currently under development, such as draft commentary formatting logic.
- **1-SOURCES**: The repository for primary materials, subdivided into `Commentaries` (largely Tibetan), `Text` (Sanskrit root texts in Devanagari), and `Translations` (Tibetan and Chinese versions).
- **2-RAILS**: Houses 'Authoritative Context,' specifically root texts integrated with structural outlines (Sachet) that provide the logical backbone for the vault.
- **3-TRANSFORMATIONS**: Contains annotated versions, processed texts, and AI-generated syntheses based on the source materials.
- **4-SYSTEM**: The operational core. It includes internal guidelines (`1-SOURCES-Guideline`, `2-RAILS-Guideline`) and a `Skills` directory containing specific logic for `epub-to-markdown`, `format-commentary`, `format-root-text`, and `source-property-extractor`.

Notes are connected through a hierarchical structure of outlines and commentaries, focusing on preserving the relationship between the root verses and their various interpretations.

## Key Topics

- *Bodhisattvacharyavatara* (Shantideva)
- Tibetan Buddhist Commentaries (e.g., Kṣemadeva, Mipham, Gyaltsab Je, Prajñākaramati, Buton Rinchen Drub)
- Multilingual Comparative Analysis (Tibetan, Chinese, Sanskrit Devanagari)
- Textual Outlining and Structural Analysis (Sachet)
- Buddhist Philosophy and Philology
- AI-Assisted Translation and Source Formatting (epub-to-markdown, property extraction)

## User Preferences

The user maintains a highly academic and structured approach to knowledge management. There is a strong preference for preserving original linguistic data; Tibetan and Chinese scripts are used extensively in file names and content, and transliteration is avoided where possible.

Responses should be direct, formal, and precise. The user values technical accuracy—particularly regarding block IDs and formatting—and expects the agent to follow the specific logic defined in the `4-SYSTEM` guidelines. The focus is on depth of research and fidelity to the source texts rather than general summaries.

## Custom Instructions

- **Maintain Source Integrity**: Strictly separate root texts (`1-SOURCES/Text`), commentaries (`1-SOURCES/Commentaries`), and structural outlines (`2-RAILS`).
- **Preserve Terminology**: Never translate or transliterate file paths or Tibetan/Chinese terminology unless explicitly asked. Keep original scripts intact.
- **Follow System Guidelines**: Prioritize instructions found in `4-SYSTEM/1-SOURCES-Guideline` and `4-SYSTEM/2-RAILS-Guideline` when processing or formatting text.
- **Utilize Skills**: Refer to the `SKILL` files within `4-SYSTEM/Skills/` for specific workflows like formatting commentaries or extracting properties.
- **Railroads Methodology**: When synthesizing information, recognize that `1-SOURCES` are the evidence and `2-RAILS` are the structural authority.
- **Technical Formatting**: Be prepared to handle specialized tasks like editing Obsidian block IDs or generating glossaries as per the vault's established patterns.

## Plugin Configuration
- **Plugin State Folder**: The user prefers this to be set to `4-SYSTEM` to ensure skills are loaded from `4-SYSTEM/Skills/`.

The guidelines (1-SOURCES-Guideline, 2-RAILS-Guideline, CLAUDE, source-formatting) have been moved from `4-SYSTEM/Skills/` to the root of `4-SYSTEM/` as per the vault's organizational logic. 

Note: To fully transition away from the `4-SYSTEM/gemini-scribe/` subfolder, the User must manually move the contents of that folder (including `AGENTS.md` and the `Sessions` folder) to `4-SYSTEM/` and then restart Obsidian or reload the plugin. The agent cannot move these files while they are part of the active system folder.
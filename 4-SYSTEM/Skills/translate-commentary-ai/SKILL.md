---
name: translate-commentary-ai
description: Translate a source commentary into the target language using AI translation requirements, termbase, and section summaries to ensure terminological consistency and philosophical fidelity. Output the translated commentary to 1-SOURCES/Translations/ with 'AI-generated' in the title.
---

---

# translate-commentary-ai

This skill translates a given classical commentary (in Tibetan or another source language) into English (or another target language) using a rigorous translation framework. It ensures high fidelity, consistency, and alignment with the project's established terminology and style by actively consulting the translation requirements, termbase, and section summaries (synthesis).

---

## Inputs

1. **Source Commentary**
   - The original commentary text to be translated, provided by the user.
2. **Requirements File**
   - File path: `3-TRANSFORMATIONS/Translations/en-ai/requirements.md`
   - Contains: Style constraints, target audience, register, tone, and cultural-adaptation rules.
3. **Termbase File**
   - File path: `3-TRANSFORMATIONS/Translations/en-ai/termbase.md`
   - Contains: Locked/prescriptive vocabulary mapping source lemmas (e.g., Tibetan) to chosen target renderings (English) with rationales.
4. **Section Summary File**
   - File path: `2-RAILS/Sections/1-0.md` (or other corresponding section files under `2-RAILS/Sections/`)
   - Contains: Original-language synthesis, divergences among commentators, and a standard English translation which provides crucial contextual and semantic anchoring.
## Output

- A new translation file created inside the `3-Transformation/Translations/` directory.
- **Filename Convention:** Must clearly indicate that it is AI-generated and specify the source/target language and commentary, e.g., 3-TRANSFORMATIONS/Translations/en-AI-generated-commentary.md` or `3-TRANSFORMATIONS/Translations/en-AI-generated-<commentary-name>.md .
- **Format:** Standard markdown with complete YAML frontmatter (including status, source files referenced, and translation metadata).

---

## Rules

1. **Strict Terminology Alignment:** Every key term in the source text that exists in `termbase.md` MUST be translated exactly as specified in the termbase. No unauthorized synonyms or variations are allowed (e.g., `བསོད་ནམས་` must always be translated as "merit", and `དགེ་བ་` as "virtue").
2. **Adherence to Requirements:** The translation must strictly conform to the constraints in `requirements.md` regarding:
   - Target register (standard, technically accurate English with traditional Buddhist terminology).
   - Tone (formal, objective, reverent, preserving philosophical precision).
   - Preservation of classical Indian and Tibetan metaphors.
3. **Contextual Anchoring via Section Summary:** Use the synthesis and English translation in `2-RAILS/Sections/1-0.md` to resolve any semantic ambiguities in the source commentary, ensuring that the translation aligns with the collective commentary consensus.
4. **Transparency:** The translated file must clearly state that it is "AI-generated" in both its title/filename and its frontmatter metadata (`status: ai-generated`).
5. **No Style Drift:** Maintain a consistent register and style throughout the translation.

## Procedure

1. **Information Gathering:**
   - Read the target **Commentary** to be translated.
   - Read the **Requirements** (`3-TRANSFORMATIONS/Translations/en-ai/requirements.md`) to internalize the style and register guidelines.
   - Read the **Termbase** (`3-TRANSFORMATIONS/Translations/en-ai/termbase.md`) to create a lookup map of locked translations.
   - Read the **Section Summary** (`2-RAILS/Sections/1-0.md` or the relevant section file) to understand the background synthesis and structural context.

2. **Drafting the Translation:**
   - Translate the source commentary section-by-section or verse-by-verse.
   - For every sentence, identify key philosophical terms and cross-reference them with the termbase map.
   - Ensure classical metaphors are translated literally as instructed in the requirements (e.g., "gold-making elixir", "banana tree").
   - Format the translation with clear headings and section structures that mirror the source commentary.

3. **Validation and Quality Assurance:**
   - Double-check that all locked terms from the termbase are rendered consistently.
   - Verify that the tone is formal, objective, and reverent.
   - Check that no unauthorized modernizations have been introduced.

4. **Writing the Output File:**
   - Save the translated text to `1-SOURCES/Translations/en-AI-generated-<commentary-name>.md`.
   - Include complete YAML frontmatter at the top of the file:
     ```yaml
     ---
     title: "AI-generated Translation of <Commentary Name>"
     source_language: bo
     target_language: en
     status: ai-generated
     referenced_files:
       - 3-TRANSFORMATIONS/Translations/en-ai/requirements.md
       - 3-TRANSFORMATIONS/Translations/en-ai/termbase.md
       - 2-RAILS/Sections/1-0.md
     created_at: <YYYY-MM-DD>
     ---
     ```

---

## Completion check

- [ ] Filename contains "AI-generated" and is saved in `1-SOURCES/Translations/`
- [ ] Frontmatter contains `status: ai-generated` and lists all referenced files
- [ ] Every key term matches the prescriptive renderings in `termbase.md`
- [ ] Metaphors are preserved literally (e.g., "gold-making elixir", "banana tree") as per `requirements.md`
- [ ] The tone is formal, objective, and reverent
- [ ] The translation is structurally aligned with the source commentary
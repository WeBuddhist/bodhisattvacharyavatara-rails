# Requirements — AI Translation (en-ai)

This is the style contract for the AI translation track of the *Bodhisattvacaryāvatāra*. All generation for this track must adhere to these constraints.

---

## 1. ## 1. Target audience and register
- **Audience:** General readers with no prior background in Buddhism or classical Indian philosophy.
- **Register:** Plain English.
- **Reading Level:** Grade 8–10 (approx. age 13–15).
- **Tone:** Direct, clear, and accessible while maintaining the gravity of the source text.

## 2. Bilingual Glossary reference path
- **Source-Target Pair:** `2-RAILS/Bilingual-Glossaries/bo-en.md`
- **Track Termbase:** `termbase.md` (local to this folder)

## 3. Style constraints
- **Sentence length:** Target 15–20 words per sentence. Avoid complex nested clauses.
- **Paragraph length:** Short paragraphs (3–5 sentences).
- **Voice:** Prefer active voice over passive voice.
- **Vocabulary:** Use common English words. Avoid technical jargon or archaic language.
- **Verse vs. Prose:** Render the verse source as clear, rhythmic prose. Do not attempt to maintain the original meter if it compromises clarity.
- **Technical terms:** Every technical term must be translated into its closest English equivalent. Use the `termbase.md` for consistency.
- **Footnotes:** Minimal. Use inline glossing for essential cultural context only if it cannot be woven into the translation.

## 4. Cultural-adaptation rules
- **Transliteration:** No transliteration of Sanskrit or Tibetan terms (e.g., use "Enlightenment" instead of "Bodhi", "Hero of Enlightenment" instead of "Bodhisattva").
- **Metaphors:** Adapt metaphors that are obscure to a modern Western audience into functional equivalents while preserving the meaning.

## 5. Source-rail dependencies
The generation skill must consult the following rails for every batch:
- `2-RAILS/Bilingual-Glossaries/Raw/bo-en-ai.md`
- `2-RAILS/Bilingual-Glossaries/Raw/bo-en-ai-gloss.md`

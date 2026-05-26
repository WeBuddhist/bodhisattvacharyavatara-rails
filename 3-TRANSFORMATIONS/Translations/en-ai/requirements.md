# Requirements — AI Translation (en-ai)

This is the style contract for the AI translation track of the *Bodhisattvacaryāvatāra*. All generation for this track must adhere to these constraints.

---

## 1. Target audience and register
- **Audience:** Practitioners, scholars, and readers seeking a precise, terminologically consistent, and literal translation of the Tibetan text.
- **Register:** Standard, technically accurate English with traditional Buddhist terminology.
- **Tone:** Formal, objective, and reverent, preserving the philosophical precision of the original.

## 2. Bilingual Glossary reference path
- **Source-Target Pair:** `2-RAILS/Bilingual-Glossaries/Raw/bo-en-ai.md`
- **Track Termbase:** `termbase.md` (local to this folder)

## 3. Style constraints
- **Fidelity:** Prioritize semantic and structural accuracy over stylistic modernization.
- **Technical terms:** Retain established Sanskrit loanwords (e.g., *bodhicitta*, *Sugata*, *samsara*) where they are standard in English Buddhist literature, as specified in `termbase.md`.
- **Verse structure:** Maintain clear verse divisions corresponding to the original Tibetan stanzas (^1-1 to ^1-36).
- **Consistency:** Ensure rigid consistency of key philosophical terms (e.g., always render `བསོད་ནམས་` as "merit" and `དགེ་བ་` as "virtue").

## 4. Cultural-adaptation rules
- **Transliteration:** Use standard Sanskrit transliteration (with diacritics where appropriate) for terms that are commonly recognized in Mahayana contexts.
- **Metaphors:** Preserve the original classical Indian and Tibetan metaphors (e.g., the alchemical elixir, the plantain tree) literally, as they carry deep philosophical meaning.

## 5. Source-rail dependencies
The generation skill must consult the following rails for every batch:
- `2-RAILS/Bilingual-Glossaries/Raw/bo-en-ai.md`
- `2-RAILS/Bilingual-Glossaries/Raw/bo-en-ai-gloss.md`

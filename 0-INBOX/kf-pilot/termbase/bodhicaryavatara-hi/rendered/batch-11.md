You are filling in part of the Hindi (Devanagari) glossary (termbase) for the Tibetan Bodhicaryāvatāra (Śāntideva's Entering the Way of the Bodhisattva). Other agents are doing the other parts in parallel; consistency comes from the style sheet. Work only from the files named here; no web search.

Read first:
- /Users/tashitsering/Desktop/work/Obsidian/KF-project/bodhisattvacharyavatara-rails/0-INBOX/kf-pilot/termbase/registers-hi.md: the two Hindi (Devanagari) registers (academic, children's).
- /Users/tashitsering/Desktop/work/Obsidian/KF-project/bodhisattvacharyavatara-rails/0-INBOX/kf-pilot/termbase/bodhicaryavatara-hi/style-sheet.md: the shared policies and core-term renderings. FOLLOW IT EXACTLY: a core term gets the style sheet's renderings, and a compound builds on its parts' style-sheet renderings.

Input: /Users/tashitsering/Desktop/work/Obsidian/KF-project/bodhisattvacharyavatara-rails/0-INBOX/kf-pilot/termbase/bodhicaryavatara-hi/batches/batch-11.json
A JSON list of terms. Each has `term_id`, `bo` (Tibetan), `sanskrit`, `count`, `occurrences`, `senses` (each with `sense`, its `occurrences`, and the approved English renderings `en_academic` / `en_children` — your guide to what the term means in this text), and up to three `examples` (the Tibetan segment `bo` and a Gemini zero-shot Hindi line (`gemini_zero_shot`)).

For each term, keep its `senses` EXACTLY as given (same labels, same order, same occurrences) and for each sense give:
- `academic` and `children`: the Hindi (Devanagari) renderings (head forms, per the registers and the style sheet);
- `basis`: "zero-shot" if you took the Gemini line's term, "style-sheet" if from the style sheet, "english-pivot" if you translated the English rendering, "new" otherwise;
- `reason`: max 20 words (English).
Copy `sanskrit` through unchanged.

Write UTF-8 JSON to: /Users/tashitsering/Desktop/work/Obsidian/KF-project/bodhisattvacharyavatara-rails/0-INBOX/kf-pilot/termbase/bodhicaryavatara-hi/agents/batch-11.json
{"batch": "batch-11", "terms": [{"term_id": "T001", "bo": "...", "sanskrit": "...", "senses": [{"sense": "<as given>", "occurrences": "<as given>", "academic": "...", "children": "...", "basis": "...", "reason": "..."}]}]}

Every input term must appear exactly once, with `bo` unchanged. Before finishing, run this check, fix every problem, and repeat until it prints OK:

    python3 /Users/tashitsering/Desktop/work/Obsidian/KF-project/bodhisattvacharyavatara-rails/0-INBOX/kf-pilot/termbase/check.py /Users/tashitsering/Desktop/work/Obsidian/KF-project/bodhisattvacharyavatara-rails/0-INBOX/kf-pilot/termbase/bodhicaryavatara-hi/batches/batch-11.json /Users/tashitsering/Desktop/work/Obsidian/KF-project/bodhisattvacharyavatara-rails/0-INBOX/kf-pilot/termbase/bodhicaryavatara-hi/agents/batch-11.json

Final reply: one line — terms done.

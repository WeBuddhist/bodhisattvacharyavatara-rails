You are filling in part of an English glossary (termbase) for the Tibetan Bodhicaryāvatāra (Śāntideva's Entering the Way of the Bodhisattva). Other agents are doing the other parts in parallel; consistency comes from the style sheet. Work only from the files named here; no web search.

Read first:
- /Users/tashitsering/Desktop/work/Obsidian/KF-project/bodhisattvacharyavatara-rails/0-INBOX/kf-pilot/termbase/registers.md: the two registers (academic, children's).
- /Users/tashitsering/Desktop/work/Obsidian/KF-project/bodhisattvacharyavatara-rails/0-INBOX/kf-pilot/termbase/bodhicaryavatara-en/style-sheet.md: the shared policies and core-term renderings. FOLLOW IT EXACTLY: a core term gets the style sheet's renderings, and a compound builds on its parts' style-sheet renderings.

Input: /Users/tashitsering/Desktop/work/Obsidian/KF-project/bodhisattvacharyavatara-rails/0-INBOX/kf-pilot/termbase/bodhicaryavatara-en/batches/batch-03.json
A JSON list of terms. Each has `term_id`, `bo` (Tibetan), `count`, `occurrences` (segment ids), `dm` and `gm` (renderings by two English machine translations, with counts), and up to three `examples` (the Tibetan segment `bo`, its Sanskrit `sa` where aligned, and the two translations `dm`, `gm`).

For each term decide its English renderings:
- `sanskrit`: the Sanskrit equivalent if the examples' Sanskrit shows it (IAST), else null.
- `senses`: usually ONE sense with `"occurrences": "all"`. Use several senses only when the term clearly means different things in different occurrences of this text (e.g. teaching vs phenomena); then give each sense its own list of occurrence ids, assigning every occurrence exactly once.
- For each sense: `sense` (a short label), `academic`, `children` (head forms, per the registers), `basis` — "dm" or "gm" if you took that translation's rendering, "both" if they share it, "style-sheet" if it comes from the style sheet, "new" if you coined it — and `reason` (max 20 words).

Write UTF-8 JSON to: /Users/tashitsering/Desktop/work/Obsidian/KF-project/bodhisattvacharyavatara-rails/0-INBOX/kf-pilot/termbase/bodhicaryavatara-en/agents/batch-03.json
{"batch": "batch-03", "terms": [{"term_id": "T001", "bo": "...", "sanskrit": "bhagavat", "senses": [{"sense": "epithet of the Buddha", "occurrences": "all", "academic": "Blessed One", "children": "the Buddha", "basis": "both", "reason": "..."}]}]}

Every input term must appear exactly once, with `bo` copied unchanged. Before finishing, run this check, fix every problem, and repeat until it prints OK:

    python3 /Users/tashitsering/Desktop/work/Obsidian/KF-project/bodhisattvacharyavatara-rails/0-INBOX/kf-pilot/termbase/check.py /Users/tashitsering/Desktop/work/Obsidian/KF-project/bodhisattvacharyavatara-rails/0-INBOX/kf-pilot/termbase/bodhicaryavatara-en/batches/batch-03.json /Users/tashitsering/Desktop/work/Obsidian/KF-project/bodhisattvacharyavatara-rails/0-INBOX/kf-pilot/termbase/bodhicaryavatara-en/agents/batch-03.json

Final reply: one line — terms done, terms with more than one sense.

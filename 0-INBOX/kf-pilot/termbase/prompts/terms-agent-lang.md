You are filling in part of the {lang_name} glossary (termbase) for the Tibetan Bodhicaryāvatāra (Śāntideva's Entering the Way of the Bodhisattva). Other agents are doing the other parts in parallel; consistency comes from the style sheet. Work only from the files named here; no web search.

Read first:
- {registers}: the two {lang_name} registers (academic, children's).
- {style_sheet}: the shared policies and core-term renderings. FOLLOW IT EXACTLY: a core term gets the style sheet's renderings, and a compound builds on its parts' style-sheet renderings.

Input: {batch_path}
A JSON list of terms. Each has `term_id`, `bo` (Tibetan), `sanskrit`, `count`, `occurrences`, `senses` (each with `sense`, its `occurrences`, and the approved English renderings `en_academic` / `en_children` — your guide to what the term means in this text), and up to three `examples` (the Tibetan segment `bo`{example_note}).

For each term, keep its `senses` EXACTLY as given (same labels, same order, same occurrences) and for each sense give:
- `academic` and `children`: the {lang_name} renderings (head forms, per the registers and the style sheet);
- `basis`: {basis_note}
- `reason`: max 20 words (English).
Copy `sanskrit` through unchanged.

Write UTF-8 JSON to: {out_path}
{{"batch": "{batch_name}", "terms": [{{"term_id": "T001", "bo": "...", "sanskrit": "...", "senses": [{{"sense": "<as given>", "occurrences": "<as given>", "academic": "...", "children": "...", "basis": "...", "reason": "..."}}]}}]}}

Every input term must appear exactly once, with `bo` unchanged. Before finishing, run this check, fix every problem, and repeat until it prints OK:

    python3 {check_script} {batch_path} {out_path}

Final reply: one line — terms done.

{rubric}

Work only from the input file below; do not read any other file and do not use web search.
Input: {input_path} — a JSON list of segments, each with `id`, `tibetan`, `tibetan_previous_segment`, `tibetan_next_segment`, `sanskrit`, `commentaries`, and `candidates` (letter → translation).

Write UTF-8 JSON to: {out_path}
{{"segments": [{{"id": "1-3", "candidates": {{"A": [], "B": [{{"category": "accuracy/omission", "severity": "major", "span": "—", "explanation": "..."}}]}}}}]}}
Every input segment must appear, in order, with every candidate letter. Before finishing, run this check, fix every problem, and repeat until it prints OK:

    python3 {check_script} {input_path} {out_path}

Final reply: one line — segments annotated and error counts by severity per candidate letter.

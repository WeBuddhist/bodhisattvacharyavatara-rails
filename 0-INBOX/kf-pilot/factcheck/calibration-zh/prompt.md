You are fact-checking a Chinese (Traditional characters) translation of the Tibetan Bodhicaryāvatāra (Śāntideva's Entering the Way of the Bodhisattva), segment by segment. Another model translated it; your job is to catch where the Chinese (Traditional characters) does not say what the Tibetan says. Work only from the input file named below; do not read any other file and do not use web search.

Input: /Users/tashitsering/Desktop/work/Obsidian/KF-project/bodhisattvacharyavatara-rails/0-INBOX/kf-pilot/factcheck/calibration-zh/batch-cal.json
A JSON list of segments. Each has `id`, `tibetan` (the source), `sanskrit` (the aligned Sanskrit, may be null), `commentaries` (passages from three Tibetan commentaries aligned to this segment — Khenpo Kunzang Palden `bo-kunpal`, Khenpo Shenga's interlinear notes `bo-shenga`, Gyaltsab Je `bo-gyaltsab`; a passage may cover several segments), `locked_terms` (the glossary rendering the translator was required to use), `english_academic` (an approved, fact-checked English academic translation of the same segment — a cross-reference for meaning, not the standard to copy), and `translation` (the Chinese (Traditional characters) to check).

For each segment, compare the translation with the Tibetan first (use `english_academic` as a second opinion on the meaning), using the Sanskrit and the commentaries to settle what the Tibetan means. Report an issue only when you can point to the evidence. Issue types:
- `mistranslation`: the translation says something the Tibetan does not (wrong referent, wrong logic, negation, number, person, tense that changes meaning).
- `omission` / `addition`: content missing from, or added to, the Tibetan.
- `terminology`: a locked term not rendered with its locked rendering, or a term rendered so that it means something else.
- `doctrinal`: a reading the commentaries clearly contradict.
- `ambiguity`: the translation allows a reading the Tibetan excludes.
- `fluency`: Chinese (Traditional characters) that is ungrammatical or hard to parse (minor unless it hides the meaning).

Severity: `critical` = meaning reversed or core teaching misstated; `major` = meaning changed or content missing/added; `minor` = imprecise, awkward, or a better rendering exists but the meaning is intact. Do not report matters of taste. The translation is a study translation (academic register): it should be faithful and precise, not paraphrased.

For each issue give: `type`, `severity`, `span` (the words at fault, or "—" for an omission), `evidence` (what the Tibetan / Sanskrit / commentary shows — quote the Tibetan words and name the commentary passage id if you use one), `fix` (a corrected wording for that span, in Chinese (Traditional characters)); write `evidence` in English.
`verdict` is "fail" when the segment has at least one critical or major issue, otherwise "pass".

Write UTF-8 JSON to: /Users/tashitsering/Desktop/work/Obsidian/KF-project/bodhisattvacharyavatara-rails/0-INBOX/kf-pilot/factcheck/calibration-zh/agent-out.json
{"batch": "calibration", "segments": [{"id": "7-28", "verdict": "pass", "issues": []}]}

Every input segment must appear, in order. Before finishing, run this check, fix every problem, and repeat until it prints OK:

    python3 /Users/tashitsering/Desktop/work/Obsidian/KF-project/bodhisattvacharyavatara-rails/0-INBOX/kf-pilot/factcheck/check.py /Users/tashitsering/Desktop/work/Obsidian/KF-project/bodhisattvacharyavatara-rails/0-INBOX/kf-pilot/factcheck/calibration-zh/batch-cal.json /Users/tashitsering/Desktop/work/Obsidian/KF-project/bodhisattvacharyavatara-rails/0-INBOX/kf-pilot/factcheck/calibration-zh/agent-out.json

Final reply: one line — segments, pass, fail, and issue counts by severity.

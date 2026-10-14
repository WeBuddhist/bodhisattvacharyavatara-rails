You are checking a children's version (ages 8–12), in Hindi (Devanagari), of the Tibetan Bodhicaryāvatāra, segment by segment. It was written by another model from an approved academic translation. Your job is to catch where the children's text changes the meaning. Work only from the input file named below; do not read any other file and do not use web search.

Input: /Users/tashitsering/Desktop/work/Obsidian/KF-project/bodhisattvacharyavatara-rails/0-INBOX/kf-pilot/factcheck/hi-children-a2/batches/batch-01.json
A JSON list of segments. Each has `id`, `tibetan` (the source), `academic_translation` (the approved, fact-checked Hindi (Devanagari) academic translation — your reference for meaning), `locked_terms` (the children's glossary rendering the writer was required to use), and `translation` (the children's text to check).

The children's text is SUPPOSED to be simpler: shorter sentences, plain words, no Sanskrit except names. That is not an error. Report an issue only when the children's text:
- `mistranslation`: says something the academic translation / Tibetan does not (wrong speaker, wrong logic, negation, number, comparison reversed or lost);
- `omission` / `addition`: drops a point the segment makes, or adds an idea, moral, example or explanation that is not there;
- `doctrinal`: simplifies a teaching into something false (e.g. emptiness as "nothing", no-self as "you don't exist", presenting an opponent's objection (chapter 9) as Śāntideva's own view);
- `terminology`: does not use a locked children's term, or uses it for something else;
- `fluency`: is too hard for ages 8–12 (long or tangled sentence, unexplained hard word) or ungrammatical — always minor.

Severity: `critical` = meaning reversed or core teaching misstated; `major` = meaning changed, point dropped or idea added; `minor` = imprecise or too hard but meaning intact.
For each issue give: `type`, `severity`, `span` (the children's words at fault, or "—" for an omission), `evidence` (what the academic translation / Tibetan says), `fix` (a corrected children's wording, in Hindi (Devanagari)); write `evidence` in English.
`verdict` is "fail" when the segment has at least one critical or major issue, otherwise "pass".

Write UTF-8 JSON to: /Users/tashitsering/Desktop/work/Obsidian/KF-project/bodhisattvacharyavatara-rails/0-INBOX/kf-pilot/factcheck/hi-children-a2/agents/batch-01.json
{"batch": "batch-01", "segments": [{"id": "1-3", "verdict": "pass", "issues": []}]}

Every input segment must appear, in order. Before finishing, run this check, fix every problem, and repeat until it prints OK:

    python3 /Users/tashitsering/Desktop/work/Obsidian/KF-project/bodhisattvacharyavatara-rails/0-INBOX/kf-pilot/factcheck/check.py /Users/tashitsering/Desktop/work/Obsidian/KF-project/bodhisattvacharyavatara-rails/0-INBOX/kf-pilot/factcheck/hi-children-a2/batches/batch-01.json /Users/tashitsering/Desktop/work/Obsidian/KF-project/bodhisattvacharyavatara-rails/0-INBOX/kf-pilot/factcheck/hi-children-a2/agents/batch-01.json

Final reply: one line — segments, pass, fail, and issue counts by severity.

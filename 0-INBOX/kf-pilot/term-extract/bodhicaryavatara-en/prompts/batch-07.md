You are extracting glossary terms from one batch of a Tibetan Buddhist root text, together with how two English machine translations rendered each term. Work only from the input file named below; do not read any other file in the vault and do not use web search.

Input: /Users/tashitsering/Desktop/work/Obsidian/KF-project/bodhisattvacharyavatara-rails/0-INBOX/kf-pilot/term-extract/bodhicaryavatara-en/batches/batch-07.json
A JSON list of segments. Each has `id`, `heading` (true for section titles), `bo` (the Tibetan source segment), and two independent English machine translations of it: `dm` and `gm`.

## What counts as a glossary term

A term a translator would want ONE locked rendering for across the whole text.

INCLUDE
- Buddhist technical terms and doctrinal concepts (e.g. emptiness, self, phenomena, merit, aggregates).
- Technical categories, enumerations and their members (e.g. the six perfections, the Three Jewels, the hells, freedoms and endowments).
- Epithets and titles of buddhas, bodhisattvas and disciples (e.g. Sugata, Blessed One, Lord of Sages, children of the Victorious One).
- Proper names of people, places and texts.
- Fixed technical phrases (e.g. aspiring bodhicitta, perfection of patience, conventional truth).
- A dhāraṇī or mantra, as one item.
- Recurring fixed images that work as terms (e.g. wish-fulfilling jewel); a one-off simile is not a term.

EXCLUDE
- Ordinary verbs (seeing, speaking, asking, answering, dwelling, sitting, going, relying, praising, teaching in the everyday sense), unless the verb itself names a technical act or attainment (e.g. entering meditative absorption, dedicating merit).
- Ordinary adjectives and adverbs (profound, excellent, great, many, quickly), unless part of a fixed term.
- Stock formulas and forms of address, rhetorical questions, and translator/colophon wording.
- Plain numbers and quantities, unless they name a technical measure.

If a fixed compound is a term AND one of its parts is also a term on its own (e.g. bodhisattva mahāsattva and bodhisattva), list both. List each distinct term once per segment.

## For each term

- `bo`: the Tibetan, copied exactly from the segment's `bo` (a literal substring), covering the term's own syllables, without case particles (gi/kyi/gyi/'i/la/las/ni/kyis etc.) and without a trailing ་ or ། where possible.
- `dm`: the English that `dm` used for this term, copied exactly from `dm` (a literal substring, same characters and case). null if `dm` omitted it or paraphrased it away.
- `gm`: the same for `gm`.

## Output

Write UTF-8 JSON to: /Users/tashitsering/Desktop/work/Obsidian/KF-project/bodhisattvacharyavatara-rails/0-INBOX/kf-pilot/term-extract/bodhicaryavatara-en/agents/batch-07.json

{"batch": "batch-07", "segments": [{"id": "7-28", "terms": [{"bo": "དེ་བཞིན་གཤེགས་པ", "dm": "Tathāgata", "gm": "Tathāgata"}]}]}

Every input segment must appear, in input order, even with an empty `terms` list.

Before finishing, run this check and fix every problem it reports, then run it again until it prints OK:

    python3 /Users/tashitsering/Desktop/work/Obsidian/KF-project/bodhisattvacharyavatara-rails/0-INBOX/kf-pilot/term-extract/verify.py check /Users/tashitsering/Desktop/work/Obsidian/KF-project/bodhisattvacharyavatara-rails/0-INBOX/kf-pilot/term-extract/bodhicaryavatara-en/batches/batch-07.json /Users/tashitsering/Desktop/work/Obsidian/KF-project/bodhisattvacharyavatara-rails/0-INBOX/kf-pilot/term-extract/bodhicaryavatara-en/agents/batch-07.json

Final reply: one line with counts (segments, terms, terms where dm and gm agree) — nothing else.

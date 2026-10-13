You are setting the shared conventions for the Chinese (Traditional characters) glossary (termbase) of the Tibetan Bodhicaryāvatāra (Śāntideva's Entering the Way of the Bodhisattva). An English glossary for the same Tibetan terms is already approved; the Chinese (Traditional characters) glossary must keep its sense distinctions but choose the right Chinese (Traditional characters) words. Several agents will fill in the glossary in parallel; your style sheet keeps them consistent. Work only from the files named here; no web search.

Read:
- /Users/tashitsering/Desktop/work/Obsidian/KF-project/bodhisattvacharyavatara-rails/0-INBOX/kf-pilot/termbase/registers-zh.md: the two Chinese (Traditional characters) registers (academic, children's).
- /Users/tashitsering/Desktop/work/Obsidian/KF-project/bodhisattvacharyavatara-rails/0-INBOX/kf-pilot/termbase/bodhicaryavatara-zh/overview.md: every term — Tibetan, Sanskrit, occurrence count, and the approved English academic / children's rendering for each sense.
- /Users/tashitsering/Desktop/work/Obsidian/KF-project/bodhisattvacharyavatara-rails/0-INBOX/kf-pilot/termbase/bodhicaryavatara-zh/terms.json: the term packets, whose examples show the Tibetan segment and a Gemini zero-shot modern Chinese line (`gemini_zero_shot`).
- Cross-text consistency: the same pilot already has approved glossaries for two other texts. For a term they share, use the same rendering unless this text needs a different sense, and say so in the Reason column:
  - /Users/tashitsering/Desktop/work/Obsidian/KF-project/daimond-sutra-rails/0-INBOX/kf-pilot/termbase/vajracchedika-zh/termbase-academic.md and termbase-children.md (Diamond Sutra)
  - /Users/tashitsering/Desktop/work/Obsidian/KF-project/summary-of-the-perfection-of-wisdom-rails/0-INBOX/kf-pilot/termbase/ratnagunasancayagatha-zh/style-sheet.md, termbase-academic.md and termbase-children.md (Ratnaguṇasaṃcayagāthā)

Write a style sheet in Markdown to /Users/tashitsering/Desktop/work/Obsidian/KF-project/bodhisattvacharyavatara-rails/0-INBOX/kf-pilot/termbase/bodhicaryavatara-zh/style-sheet.md with exactly these sections:

## Policies
Numbered cross-cutting decisions, one line each with a short reason. Cover at least: script and punctuation; which established Chinese (Traditional characters) Buddhist terms are used in the academic register and how attested usage is weighed (established modern Chinese Buddhist usage vs the Gemini zero-shot); how the two senses of ཆོས are kept apart; how epithets of the Buddha and titles are rendered; names; the six perfections and the chapter titles; how the children's register simplifies technical terms without changing their meaning; how compounds take their parts' renderings.

## Core terms
A table of the 30–50 terms whose renderings other terms build on, with columns: | Tibetan | Sense | Academic | Children's | Reason |. Use the exact Tibetan and sense labels from the overview.

Final reply: one line — number of policies and core terms.

# Worked example — Diamond Sutra, zh-academic and zh-children (2026-10-23/24)

The first run of this procedure. Read it before building a prompt for another text: most of the lessons repeat.

## Where the files are (in the Diamond Sutra vault)

- Drafts: `0-INBOX/zh-prompt/zh-academic-prompt-draft.md`, `0-INBOX/zh-prompt/zh-children-prompt-draft.md` (Chinese, English mirror, design notes, decision log per track).
- Built prompts: `3-TRANSFORMATIONS/Translations/zh-academic/requirements.md` (~5,000 chars), `zh-children/requirements.md` (~3,800 chars).
- Previous prompts: `0-INBOX/zh-prompt/ab-test/requirements-v1.md` (academic), `requirements-children-v1.md`.
- A/B test plan and runner: `0-INBOX/zh-prompt/ab-test/PLAN.md`, `ab_test.py`. Operator guide: `0-INBOX/zh-prompt/RUN-FULL.md`.

## What the previous prompt looked like

Only the style rules (`requirements.md`, ~25 lines) were Chinese. The task line, the explanation of the reference fields, the output rules and the fix-request feedback were English, built inside the runner (`gm_variant_translate.py`). The colleague who ran the pipeline does not read Chinese, so a Chinese prompt needed an English mirror they could maintain.

## Decisions the user made (keep asking the same questions for a new text)

| Topic | Academic | Children's |
|---|---|---|
| Authority order | Tibetan > commentaries > English academic > Sanskrit > Kumārajīva > machine draft | Chinese academic (meaning) > Tibetan (checking) > English children's (how to simplify) |
| Commentaries named in the prompt | the three registered Tibetan commentaries, with Tibetan titles, Chinese working titles (暫譯), BDRC IDs | not given to the writer |
| Style sample | 溫宗堃譯〈阿那律相應．第九經〉, 《從修行到解脫：巴利經典選集》 | 佛經報恩網〈渴見水喻〉白話文釋義 (《百喻經》) |
| Vocative | 「須菩提！」 (locked) | 「須菩提！」 (locked) |
| "Why is that?" ཅིའི་ཕྱིར་ཞེ་ན | 「這是為什麼呢？」 (locked) | 「為什麼呢？」 (locked) |
| Paradox 所謂X…非X…是名X | modern frame: 所謂X，／是因為如來說那（些）並不是X。／所以才稱為X。 | identical to academic (user: 「才不會讓句子的原意跑掉」) |
| Doctrinally sensitive term families | — | 想 family and 佛土莊嚴 / 莊嚴 use the academic renderings |

## Lessons

1. **Read the runner before the prompt.** The real prompt is assembled in code: system instruction, task line, per-segment JSON fields, feedback strings. List each part and its language before drafting.
2. **Count before deciding.** Formula variance in the old output made the case for every lock: the paradox's "therefore called X" part had 8 different wordings across 28 segments; vocatives were split 85 「須菩提，」 / 63 「須菩提！」.
3. **Lock formulas, don't just ask for them.** The compliance check ignored punctuation, so 「須菩提，」 passed a 「須菩提！」 lock until the check compared formulas ending in ！／？ exactly.
4. **Nested locks force wrong words.** A short term listed separately inside a longer one (ཆོས inside ཆོས་ཀྱི་སྤྱན) was locked as 教法 and produced 「教法眼」, a major error; the same bug added 「或無想」 to a list that has no such item. Fixed for Chinese by not locking a term that occurs only inside a longer locked term (`nested_only()` in the runner).
5. **Children's text inherits termbase problems.** Two spellings (佈置 / 布置) and a misleading 「沒有想法」 came from the children's termbase, not the writer. Fix the lock; the prompt cannot override it.
6. **Normalise the sample's punctuation** to the track's rules (「」, ：, 麼) instead of telling the model not to copy wrong marks; say what to learn and what not to imitate (ellipses, footnote marks, closing morals, vocabulary).
7. **Copyright and public repos.** The vault repo was public. The scanned page was kept out of git (git-ignored, removed from unpushed commits); the quoted passages were left in with the user's knowledge.
8. **Keep other tracks unchanged.** Every change to the shared runner or termbase was followed by a comparison of the locked terms of every track (en, hi, zh × academic, children) before and after.
9. **Separate the prompt from the run.** The colleague runs Gemini on their own machine; the deliverable was a pushed vault with the prompt wired in (`--system`), a dry-run-by-default A/B test, and a step-by-step guide with costs from the usage ledger.

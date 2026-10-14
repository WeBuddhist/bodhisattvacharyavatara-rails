# Review flags — Bodhicaryāvatāra

Items the cross-model review approved or recorded that an editor may want to override
(add to `termbase/bodhicaryavatara-<lang>/overrides.json`, then `gemini_review.py <run> --apply-only`).

## English termbase (Gemini review, 2026-10-07: 18 objections, 17 applied, 1 recorded)
Applied changes that read awkwardly (each term occurs once):
- T590 བདག་ཉིད: "self" → **"very self"**; the usual reflexive sense is "oneself".
- T439 མི་འོ་ཅོག་གི་ལུས: "human body" → **"every human body"** (the Tibetan means the bodies of all humans; "all human bodies" reads better).
- T475 འཚང་རྒྱ་བ: "Buddhahood" → **"awakening as a Buddha"** (a verb: "to become a Buddha").
- T151 སྐྱོབ་པ: "Protector" → **"Saviour"** (British spelling; theistic overtone).
Recorded, not applied:
- T089 བརྟུལ་ཞུགས: reviewer says merge the "ascetic person" sense into "ascetic discipline" (the person is བརྟུལ་ཞུགས་ཅན, T536).

## Term extraction
- batch-20 (8-152..8-a) attempt 1 extracted 0.69 terms/segment (18/35 empty); re-run gave 1.34. Gemini review added 4 more.

## English academic fact-check (2026-10-08)
Glossary corrections made from fact-check evidence (pipeline corrections, not taste; listed in `overrides.json`):
- T463 སེམས་ཅན་དམྱལ excluded: mis-cut span (6-47 "if beings go to hell").
- ཉོན་མོངས at 4-37 unlocked: "wretched" (pity), not the afflictions.
- Nested locks dropped (5-4: "hell guardian" contains "hell of sentient beings").
Open minor issues: 45 (see `factcheck/academic-a3/verdicts.json` for the re-checked segments and `academic-a1` for the rest).
- 5-97: the a3 rewrite follows Gyaltsab's reading of དེ་སྲིད; Kunpal reads it differently (divergence, minor).
- 6-31: the Tibetan reads སྦྲུལ "snake" where the Sanskrit and commentaries have "emanation"; the English follows the Sanskrit/commentaries.

## English children's (2026-10-08)
- ⚑ 5-7 text-critical divergence: Tibetan མེ་ཚོགས "masses of fire" (Shenga follows it) vs Sanskrit *tāḥ striyaḥ* "those women" and Gyaltsab's text མོ་ཚོགས. The academic now says "groups of women" (a2 minor-fix round, following Sanskrit + Gyaltsab); the children's text follows the academic; the children's checker (reading the Tibetan) fails it. An editor must choose the reading; then regenerate 5-7 in both tracks.
- 31 minor issues open (`factcheck/children-a2/verdicts.json` for re-checked segments, `children-a1` for the rest).

## hi academic 5-7 (2026-10-08)
The Hindi academic version renders མེ་ཚོགས as "स्त्री-समूह" (women), following the Sanskrit/Gyaltsab reading; the Tibetan root reads "masses of fire". Its academic fact-check passed it. The Hindi children's version says "आग की लपटें" (fire). Same text-critical divergence as en children 5-7; for an editor to decide which reading the governed versions follow.
The Chinese academic (彼等女眾) and Chinese children's versions also follow the "women" reading at 5-7; so do en academic and en children. Only hi children reads "fire". One editorial decision fixes all six tracks.

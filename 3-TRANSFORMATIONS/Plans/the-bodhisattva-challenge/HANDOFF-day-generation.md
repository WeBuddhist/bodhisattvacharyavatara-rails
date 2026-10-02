# Handoff: generating English + Hindi day plans (Bodhisattva Challenge)

Written 2026-10-02. Paste or point a fresh session at this file, then say e.g. "create day 91-95".

## Status

- **Done through Day 90** (Chapter 5, verse 43), both `en/` and `hi/`. Chapters 1-4 and Days 74-90 are written.
- **Next: Day 91.** Tibetan sources exist through at least Day 116 (end of Chapter 5, `Chapter-5 D74-D116`). Chapters 6-10 folders also exist under `Plans/Dalai Lama/`.
- Days 15-36 (Chapter 2) are older rails-authored files in a different style from 37+. Never touched or reconciled.
- The user's request pattern is simply "create day N" or "N-M". If a day is skipped in the request, check whether it exists and ask once (Day 85 was skipped once; user said fill it).

## Where things live (vault root `bodhisattvacharyavatara-rails`, via the device bridge at `$HOME/mnt/bodhisattvacharyavatara-rails/`)

| What | Path (under `3-TRANSFORMATIONS/`) |
|---|---|
| Tibetan source per day | `Plans/Dalai Lama/Chapter-<C> D<a>-D<b>/Day-<n>-Ch<C>-V<v1>-<v2>.md` |
| English output | `Plans/the-bodhisattva-challenge/en/Days/Chapter-<C> D<a>-D<b>/<n>-ch<C>-v<v1>-<v2>-eng.md` |
| Hindi output | `.../hi/Days/Chapter-<C> D<a>-D<b>/<n>-ch<C>-v<v1>-<v2>-hi.md` |
| Termbases (source of truth) | `Plans/the-bodhisattva-challenge/en/termbase-translation.md` and `hi/termbase-translation.md` |
| Verse text (EN) | `Translations/AI_translation/english/bca-english-plain.md` (block IDs like `^5-12`) |
| Verse text (HI) | `Translations/AI_translation/hindi/bca-hindi-plain.md` |
| Skill | `dalai-lama-plan-translation` (read it first; it is the contract) |

Frontmatter on every output: `day, chapter, verse (string "a-b"), generated_by: dalai-lama-plan-translation, translated_from, verse_source, pending_terms (list or []), status: draft`. Copy the structure of any existing file, e.g. `en/Days/Chapter-5 D74-D116/74-ch5-v1-3-eng.md` and its `-hi` twin.

## What gets translated (only these)

From the Tibetan day file: **ངོ་སྤྲོད། (Introduction)**, **གོ་རྟོགས། (Commentary)**, and under 📿: **ཉམས་ལེན་དངོས། (Actual Practice)** and **དེའི་འགྲེལ་བཤད། (Explanation, starts with the `_(category)_` label)**.
Everything else (refuge/bodhicitta block, root-verse block, dedication, the trailing verse repeat) is NOT translated fresh. Verses come verbatim from the two plain-translation files by block ID (`grep -B4 "\^5-12$" file`).

Output sections: `## Today's Verse` / `## आज का श्लोक`, `## 1) Introduction to Today's Practice`, `## 2) Commentary Explanation`, `## 3) Today's Practice` (`**Actual Practice:**` + `**Explanation:**`). Hindi headings use `१) आज के अभ्यास का परिचय`, `२) अर्थ और व्याख्या`, `३) आज का अभ्यास`, `**मुख्य अभ्यास:**`, `**व्याख्या:**`.

## Style rules that kept mattering

- CEFR A2-B1: one idea per sentence, mostly under 20 words, active voice. No diacritics in body prose except italicised cited work titles (`_Bodhicaryāvatāra_`, `_बोधिचर्यावतार_`). Cited titles are always italicised.
- Actual Practice is first person, future: "Today, I will..." / "आज मैं ... करूँगा". Commentary and Explanation use "we".
- Fixed words (details in termbases): དགེ་བ་ "doing good"/"अच्छा काम" (never merit/पुण्य); བསོད་ནམས་ "merit"/"पुण्य"; སྡིག་པ་ "wrongdoing"/"बुरा काम" (never sin/पाप in prose); ཉོན་མོངས་ "the afflictions"/"मन के विकार" (never bare क्लेश in prose); ངན་སོང་ "the lower realms"/"बुरी गतियाँ"; ལེ་ལོ་ "laziness"/"आलस" (not आलस्य); བག་མེད་ "carelessness"/"लापरवाही".
- Fixed practice-category labels exist for: Doing good, Avoiding wrongdoing, Taming the mind, Generosity Practice, Patience Practice. Everything else is in the pending table (see below). Reuse the pending rendering; do not re-log it as new.
- Do not translate more than the Tibetan says. Do not add a mood, person, or a "goal/everything/caution" that is not there. Keep story beats and attributions exactly.
- If the Tibetan file ends with a translator's note saying no scholarly commentary exists (Day 90 did), write a plain literal explanation with no invented teacher, story, or citation.

## Standing instruction on new terms

New practice categories, proper names, text titles: **propose a rendering, log it as pending, and keep going. Do not stop to ask.** (User chose "propose and continue" explicitly.) Log in the day file's `pending_terms:` as `"<Tibetan> -> <rendering>"` and in both termbases' Pending table. Flag uncertain identifications in the rendering text itself (e.g. Day 76 sutra title, Day 78 king, Day 85 citation).

## The pipeline used every batch

1. List `Day-*` files in the chapter folder; `cat` each Tibetan source with `device_bash` (staging does NOT work for `Plans/Dalai Lama`).
2. Check the termbases (`grep`) for any new category, name, or title before drafting.
3. Pull the verses by block ID, EN and HI.
4. Draft EN + HI into a fresh scratch dir (`mkdir -p /tmp/chXY`) via `cat > file <<'XEOF'` heredocs through `device_bash`. Each `device_bash` call is a fresh shell. `/tmp` has been wiped between sessions, so never rely on old scratch dirs.
5. **Adversarial audit**: spawn `general-purpose` Agent(s) (about 3 days per agent) told to `cat` the Tibetan, the drafts, and both termbases via `device_bash` (not the Read tool), and to report by class: 1 additions with no Tibetan parent, 2 omissions, 3 meaning shifts (person/mood/attribution), 4 termbase violations, 5 EN/HI divergence, 6 register. Tell it not to flag word counts. Point it at the two or three spots you are least sure of.
6. **Verify every finding yourself against the Tibetan** before fixing. Most were real; reject any that are not.
7. Apply fixes with python read-modify-write (assert the old string exists).
8. `cp` into the vault `en/Days/...` and `hi/Days/...` and **md5sum-compare** every file.
9. Sync pending terms into both termbases with `sync_termbase_pending.py` (same folder as this file). Then `git diff` both termbases: it must be purely additive (only the new rows).
10. Report: what was created, real audit findings and fixes, any upstream verse-source deviations, new pending terms. Short.

## Gotchas learned the hard way

- `device_bash` cannot delete or unlink. `git checkout -- file` fails. Revert a file with `git show HEAD:"<path>" > "<path>"`.
- The termbase Pending tables have different headings: EN `## Pending terms`, HI `## लंबित शब्द`. Column headers differ too. The EN table is padded/aligned (a formatter touched it). **Append-only** is the safe approach. An earlier version that rewrote the whole table reformatted 66 unrelated rows; and an even earlier version matched the wrong path with a regex and corrupted all day numbers. `sync_termbase_pending.py` is the corrected, append-only version. Check its output before trusting it.
- Day number must be parsed from the file basename (`re.match(r'(\d+)-', basename)`). Old Chapter-1 files (`5.md`) have no such prefix and are skipped.
- Mid-session the `/tmp` scratch can vanish (the device VM restarts). If `cd /tmp/chX` fails, rewrite the drafts before fixing.

## Known bugs in the shared verse-source files (NOT fixed upstream; fixed locally in the day files and disclosed)

The plain-translation files are verbatim sources, so verses are normally never edited. These were wrong enough to fix in the day file only:

| Day | Verse | Problem |
|---|---|---|
| 74 | EN 5-2 | Elephant/mind harm comparison reversed vs Tibetan, Hindi, and the day's commentary |
| 78 | HI 5-11 | Declarative turned into a question |
| 81 | EN 5-19 | Two similes merged into a circular line; "wild people" put in the wrong clause |
| 84 | HI 5-28 | पुण्य used for དགེ (doing good) |
| 86 | EN 5-32 | Invented fourth quality "and likewise caution" |

Left as-is on purpose: Day 82 HI 5-22 "भलाई" for doing good (no meaning conflict). Someone should eventually fix these five in the two plain files.

## Pending terms awaiting human approval

The Pending table in each termbase holds about 70 rows (names, texts, glosses, categories) since Day 38. Earlier running tallies given in chat (12/14/17/18) counted only recent additions and were wrong; trust the table. Practice categories needing approval: Ethics Practice, Diligence Practice, Wisdom Practice, Practice of remembering that nothing lasts, Recognizing the afflictions, Giving up anger, Not feeding the afflictions, Not giving up the effort, Welcoming hardship, Meditation Practice.
Tentative identifications to check against a published source: Day 76 `འགྲོ་བ་རྣམ་འབྱེད་ཀྱི་མདོ` as "the Sutra Distinguishing Rebirths"; Day 78 `རྒྱལ་པོ་གཙུག་ན་རིན་པོ་ཆེ` as "King Manicuda"; Day 85 `བཤེས་ལེགས་ལས།` as the _Letter to a Friend_ (spelling differs from the established `བཤེས་སྤྲིང་` entry).

## Starter prompt for the new session

> Read `3-TRANSFORMATIONS/Plans/the-bodhisattva-challenge/HANDOFF-day-generation.md` and the `dalai-lama-plan-translation` skill. Then create the English and Hindi plans for day 91-95 following that pipeline, including the adversarial audit.

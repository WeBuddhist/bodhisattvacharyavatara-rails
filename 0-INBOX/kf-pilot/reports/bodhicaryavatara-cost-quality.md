---
title: "KF AI Translation Pilot — Bodhicaryāvatāra (Chonjuk), English, Chinese and Hindi: cost and quality"
status: draft
date: 2026-10-08
source_data: 0-INBOX/kf-pilot/usage-ledger.jsonl; factcheck/*/verdicts.json; factcheck/calibration*/result.json; reports/improvement-bodhicaryavatara.json; reports/pairwise*-bodhicaryavatara.json; reports/blind-eval-bodhicaryavatara.json
prices: 4-SYSTEM/scripts/usage-ledger/prices.json (list prices as of 2026-10-07)
supersedes: reports/bodhicaryavatara-en-cost-quality.md (English only)
---

# Bodhicaryāvatāra (Chonjuk), English, Chinese and Hindi — cost and quality

Second text of the KF pilot, after the Diamond Sutra and before the Ratnaguṇasaṃcayagāthā in the combined report.
All figures come from the usage ledger, which records every model call made for this text. Costs are at API list
prices on 2026-10-07. The figures can be recomputed with `reports/costs.py`, `factcheck/improvement.py`,
`factcheck/calibration/score.py` and `blind-eval/score.py`.

## 1. What was produced

Source text: 941 blocks (910 verses, chapter colophons, introduction and closing, 14 headings), 26,724 Tibetan
syllables, 2.5 times the Diamond Sutra. Languages: English (en), Chinese in Traditional characters (zh), Hindi (hi).

| Output | Built by | Checked by | en | zh | hi |
|---|---|---|---|---|---|
| Zero-shot translation (baseline) | Gemini 3.1 Pro; DharmaMitra (en) | — | ✓ | ✓ | ✓ |
| Term list: 742 Tibetan terms (shared by all languages) | Claude Sonnet 5.5 agents | Gemini 3.1 Pro | ✓ | | |
| Glossary, academic + children's renderings (741 terms) | Claude Sonnet 5.5 agents | Gemini 3.1 Pro | ✓ | ✓ | ✓ |
| **Academic translation**: glossary-locked, verse form, with Sanskrit + 3 commentaries per verse | Gemini 3.1 Pro | Claude Sonnet 5.5 agents | 26,198 words | 30,873 characters | 24,024 words |
| **Children's version** (ages 8–12, prose), from the academic version + children's glossary | Gemini 3.1 Pro | Claude Sonnet 5.5 agents | 28,221 words | 43,356 characters | 28,889 words |

Every governed translation covers all 941 blocks. The commentaries used for grounding are Khenpo Kunzang Palden's
word commentary, Khenpo Shenga's interlinear notes and Gyaltsab Je's commentary. Four human English translations
(Padmakara, Wallace, Choephel) and four human Chinese translations (如石, 索達吉, 蔣揚仁欽, 隆蓮) were kept out of the
pipeline so they could serve as independent references.

## 2. Cost

### By step and language (USD)

| Step | Model | en | zh | hi |
|---|---|---|---|---|
| Term extraction (27 parallel agents; shared) | Claude Sonnet 5.5 | 6.15 | — | — |
| Term review (shared) | Gemini 3.1 Pro | 3.60 | — | — |
| Glossary (style sheet + 16 parallel agents) | Claude Sonnet 5.5 | 6.44 | 5.48 | 6.28 |
| Glossary review | Gemini 3.1 Pro | 0.32 | 1.92 | 1.72 |
| Academic translation, incl. retries and fixes | Gemini 3.1 Pro | 20.09 | 16.55 | 14.04 |
| Academic fact-check, incl. re-checks | Claude Sonnet 5.5 | 19.78 | 15.75 | 17.58 |
| Children's version, incl. retries and fixes | Gemini 3.1 Pro | 8.16 | 8.09 | 8.37 |
| Children's fact-check, incl. re-checks | Claude Sonnet 5.5 | 6.03 | 5.45 | 8.35 |
| **Pipeline total (new work)** | | **70.57** | **53.24** | **56.34** |
| Measurement: checker reliability test | Claude Sonnet 5.5 | 0.39 | 0.67 | 0.33 |
| Measurement: blind before/after judge | Gemini 3.1 Pro | 5.30 | 4.51 | 4.93 |
| Measurement: blind comparison with zero-shot and human (both annotators) | Claude Sonnet 5.5 + Gemini 3.1 Pro | 2.22 | 2.28 | 1.54 |
| Zero-shot root translation (baseline) | Gemini 3.1 Pro | 7.29 | 8.14 | 8.01 |
| **All work on this text** | | **85.77** | **68.84** | **71.15** |

Pipeline total for the three languages: **$180.15**. Measurement: $22.17. All work on this text: **$225.76**.
DharmaMitra calls are free and not in the totals.

### By version

| Version | en | zh | hi | per 1,000 Tibetan syllables (en / zh / hi) |
|---|---|---|---|---|
| Glossary | 16.51 (incl. shared term list) | 7.40 | 8.00 | 0.62 / 0.28 / 0.30 |
| Academic (translation + fact-check + fixes) | 39.87 | 32.30 | 31.62 | 1.49 / 1.21 / 1.18 |
| Academic incl. its glossary | 56.38 | 39.70 | 39.62 | 2.11 / 1.49 / 1.48 |
| Children's (translation + fact-check + fixes) | 14.19 | 13.54 | 16.72 | 0.53 / 0.51 / 0.63 |
| Zero-shot | 7.29 | 8.14 | 8.01 | 0.27 / 0.30 / 0.30 |

- **Cost per syllable is close to the other two texts.** The academic version with its glossary costs $1.48–2.11 per
  1,000 syllables, against $1.37–2.14 for the Diamond Sutra and $1.58–2.59 for the Ratnaguṇa.
- **Each further language costs less than the first.** A new language's glossary costs $7.40–8.00, against $16.51
  for English, because the term list is built once. A full new language cost $53.24 (zh) and $56.34 (hi).
- **Governed vs zero-shot:** the governed academic version with its glossary costs 7.7× a zero-shot run in English,
  4.9× in Chinese and 4.9× in Hindi.
- **Where the money goes** is the same as for the other texts: Gemini thinking tokens (billed as output) are most of
  every Gemini step; cache reads and writes are most of every Claude agent step.

### Compared with human translation

The rates are those of the Diamond Sutra report: **84000** sponsors a text at about $400 per Tibetan page, and
**Prajna Fire** quotes $100–300 per page for philosophical texts. The text's 26,724 syllables come to roughly
**59 Tibetan pages**, estimated at 450 syllables per Degé page.

| One academic translation, one language | Cost |
|---|---|
| Human, at 84000's rate ($400/page) | about $23,600 |
| Human, at Prajna Fire's rates ($100–300/page) | $5,900–17,700 |
| This pipeline, governed academic incl. its glossary | $56.38 (en) · $39.70 (zh) · $39.62 (hi) |
| Pipeline as a share of the human cost | 0.2–1.0% |

**These are unequal products.** A human translation at these rates arrives ready to publish; the pipeline's output
is a checked draft that no specialist has reviewed. At the grant's 10% target, a $5,900–23,600 human budget leaves
$590–2,360 for specialist review: about 2–16 hours at $150–250 an hour for 59 pages.

## 3. Quality

### Glossary consistency (automatic check)

| Version | Locked-term uses required | en | zh | hi |
|---|---|---|---|---|
| Academic | 2,204–2,205 per language | 2,199 (99.7%) | 2,204 (100%) | 2,204 (99.95%) |
| Children's | 2,204–2,205 per language | 2,200 (99.8%) | 2,204 (100%) | 2,203 (99.9%) |

The gaps are segments where the translator kept another wording after one automatic retry and the fact-checker
accepted it.

### Fact-check (Claude checks Gemini's output, segment by segment)

**Academic**, checked against the Tibetan, the Sanskrit and the 3 commentaries (zh and hi also see the approved
English academic as a cross-reference):

| | en | zh | hi |
|---|---|---|---|
| Passed first time | 908 / 927 (98.0%) | 922 / 927 (99.5%) | 921 / 927 (99.4%) |
| Major errors found | 19 | 5 | 6 |
| … by type | 17 mistranslation, 1 doctrinal, 1 addition | 5 mistranslation | 5 mistranslation, 1 ambiguity |
| Minor issues found | 151 | 108 | 111 |
| Critical errors | 0 | 0 | 0 |
| Final state | all pass | all pass | all pass (6-109 at attempt 3) |

**Children's**, checked against the approved academic version and the Tibetan:

| | en | zh | hi |
|---|---|---|---|
| Passed first time | 908 / 927 | 912 / 927 | 914 / 927 |
| Major errors found | 19 | 15 | 13 |
| Minor issues found | 131 | 108 | 168 |
| Final state | all pass except 5-7 (flagged) | all pass | all pass (9-105 at attempt 3) |

Typical major errors: who acts on whom (3-1, 9-24), two items fused into one (3-4, children's 1-32), a reversed
comparison (hi 9-19, the crystal and the blue), a number understated (zh children's 4-19), and a simplification that
turns a conditional into a flat statement.

### Improvement from the fact-check and fix

Fix rules, as for the other texts:
- **Major errors:** regenerated with the checker's evidence, re-checked, kept on a pass. A segment that fails twice
  gets one more attempt.
- **Minor-only fixes:** kept only if the blind pairwise judge (Gemini, both A/B orders) prefers them or ties;
  otherwise the original is restored.
- **Re-check failures:** a fix that fails where the original had passed is reverted to the original.

| Track | Failing segments | Minor issues | Issues per 100 segments | Penalty per 1k syllables | Error-free segments |
|---|---|---|---|---|---|
| en academic | 19 → 0 | 151 → 59 | 18.3 → 6.4 | 9.21 → 2.21 | 82.8% → 94.3% |
| zh academic | 5 → 0 | 108 → 24 | 12.2 → 2.6 | 4.98 → 0.90 | 88.3% → 97.6% |
| hi academic | 6 → 0 | 111 → 31 | 12.6 → 3.3 | 5.28 → 1.16 | 87.7% → 96.8% |
| en children | 19 → 1 | 131 → 38 | 16.2 → 4.2 | 8.46 → 1.61 | 84.1% → 95.9% |
| zh children | 15 → 0 | 108 → 37 | 13.3 → 4.0 | 6.85 → 1.38 | 87.1% → 96.2% |
| hi children | 13 → 0 | 168 → 43 | 19.5 → 4.6 | 8.72 → 1.61 | 81.3% → 95.5% |

Penalty: minor 1, major 5, critical 10 points. The "after" figure for each segment is the verdict of the check that
saw its final text; every segment's final text has been checked.

**Blind before/after judge** (Gemini compares the original and the fixed text in both orders; a win or loss counts
only when both orders agree):

| Track | Major-error fixes: better / tie / worse | Minor-only fixes: better / tie / worse | Minor fixes reverted |
|---|---|---|---|
| en academic | 15 / 1 / 3 | 76 / 38 / 20 | 20 |
| zh academic | 3 / 1 / 1 | 57 / 35 / 11 | 11 |
| hi academic | 4 / 2 / 0 | 65 / 26 / 16 | 16 |
| en children | 15 / 3 / 0 | 96 / 18 / 10 | 10 |
| zh children | 12 / 3 / 0 | 78 / 15 / 11 | 11 |
| hi children | 10 / 0 / 3 | 131 / 19 / 6 | 6 |

- **Major-error fixes are mostly real improvements:** 59 of 76 judged better and 7 worse. All pass Claude's
  re-check and are kept, by rule.
- **Minor-only fixes help about seven times as often as they hurt** (503 better, 74 worse). The 74 worse ones were
  restored, so the final text keeps only fixes the judge preferred or tied.
- **The English children's version was built before 20 English academic minor fixes were reverted** (the keep-best
  revert was applied to English after the fact). Those 20 children's segments follow a slightly different academic
  wording; their meaning was checked against it.

### chrF does not measure quality here

chrF (character n-gram overlap) against the human English translations, each aligned to the Tibetan verse numbering
(`reports/chrf_systems.py`):

| System | Padmakara | Wallace | Choephel | Mean |
|---|---|---|---|---|
| DharmaMitra zero-shot | 36.02 | 43.19 | 42.35 | 40.52 |
| Gemini zero-shot | 34.16 | 41.86 | 41.97 | 39.33 |
| Academic, fact-checked (this pipeline) | 34.21 | 41.92 | 42.13 | 39.42 |
| Older "Rails" scholar version (prose, no glossary) | 31.43 | 35.25 | 34.72 | 33.80 |

- **The zero-shot baselines score as high as the checked version.** chrF tracks wording and verse form, not whether
  the meaning is right: it separates prose from verse, but not accurate from inaccurate verse.
- **The fixes barely move it:** English academic 39.42 → 39.47 for the whole text and 38.70 → 39.01 on the 132
  changed segments; Chinese academic against 如石, 蔣揚仁欽 and 隆蓮 11.45 → 11.42 (whole text). The Chinese references
  are classical verse, so overlap with modern Chinese is near the floor.
- **The human references needed aligning first.** Padmakara, Choephel, 如石 and 蔣揚仁欽 follow the standard edition's
  numbering, and Wallace and 隆蓮 have their own offsets; an earlier draft compared about 180 verses against the wrong
  reference verse. The fix raised every score by 1.6–3.6 points and changed no conclusion. About a third of the
  蔣揚仁欽 file is identical to 如石 apart from punctuation, so those two references may not be independent.

### How reliable is the checker?

The test plants 18 known errors in 24 verified academic segments and leaves 6 untouched as controls: 9 negations,
2 numbers, 2 locked-term swaps, 2 wrong words, 1 name swap, 1 omission and 1 addition, the same mix as for the other
texts, at the same verses in all three languages. A fresh checker then checks the batch blind.

| | en | zh | hi |
|---|---|---|---|
| Planted errors caught | 16 / 18 | 18 / 18 | 18 / 18 |
| … and the issue points at the planted words | 16 | 18 | 18 |
| All 9 negations caught (rated critical) | ✓ | ✓ | ✓ (8 critical, 1 major) |
| False alarms on the 6 clean controls | 0 | 0 | 0 |
| Missed | 2 locked-term swaps | — | — |

- **The English miss is the same blind spot as in the other texts:** the checker notices a locked term swapped for a
  near-synonym ("vigilance" for "introspection" at 5-96, "superior insight" for "special insight" at 8-4) but rates it
  minor. The Chinese and Hindi checkers rated the same swaps major.
- **The automatic glossary check catches both swaps in all three languages.** Checker and glossary check together
  catch 18 of 18 in every language.

### Blind comparison: governed vs zero-shot vs human

**Set-up**, as for the other texts:
- **Sample:** 40 verses, one at random from each fortieth of the text, the same verses in every language.
- **Candidates:** en: governed academic, DharmaMitra zero-shot, Gemini zero-shot, Padmakara (human); zh: governed
  academic, Gemini zero-shot, 如石 (human, classical verse); hi: governed academic, Gemini zero-shot.
- **Blinding and scoring:** candidates were shuffled under letters. Annotators saw the Tibetan, the Sanskrit and the
  commentaries, but no glossary. Claude and Gemini each did an MQM annotation.

**Errors per verse (mean penalty; lower is better)**, Claude / Gemini as annotator:

| System | en | zh | hi |
|---|---|---|---|
| **Governed academic** | **0.05 / 0.33** | **0.05 / 0.05** | **0.17 / 0.17** |
| Zero-shot, Gemini | 0.10 / 0.38 | 0.38 / 0.45 | 0.23 / 0.20 |
| Zero-shot, DharmaMitra | 0.30 / 0.57 | — | — |
| Human: Padmakara (en) / 如石 (zh) | 0.95 / 2.02 | 1.38 / 1.62 | — |

**Major and critical errors in the 40 verses**, Claude / Gemini:

| System | en | zh | hi |
|---|---|---|---|
| **Governed academic** | **0 / 1** | **0 / 0** | **1 / 0** |
| Zero-shot, Gemini | 0 / 1 | 1 / 3 | 0 / 0 |
| Zero-shot, DharmaMitra | 1 / 3 | — | — |
| Human | 3 / 11 | 5 / 10 | — |

**Head to head (verses where the governed version has fewer / equal / more errors)**, Claude / Gemini:

| Governed vs | en | zh | hi |
|---|---|---|---|
| Zero-shot, Gemini | 3–36–1 / 8–26–6 | 10–28–2 / 6–33–1 | 7–30–3 / 4–32–4 |
| Zero-shot, DharmaMitra | 7–31–2 / 7–28–5 | — | — |
| Human | 23–16–1 / 24–13–3 | 25–14–1 / 21–17–2 | — |

What this shows:
- **The governed version has the fewest errors in English and Chinese under both annotators; in Hindi it is level
  with Gemini zero-shot.**
- **The gain over Gemini zero-shot is smaller than for the Ratnaguṇa.** The Bodhicaryāvatāra is one of the best-known
  Tibetan texts and the models translate it well unaided: Gemini zero-shot leaves 10–28% of verses with an error. The
  clearest gain is in Chinese (10 better, 2 worse under Claude).
- **The annotators agree on direction, not on detail.** They order candidate pairs the same way in 54% of English,
  45% of Chinese and 13% of Hindi pairs. System-level conclusions hold under both; segment-level ones do not.
- **The human translations are not a fair benchmark for fidelity to the Tibetan.** Padmakara is a literary verse
  translation and 如石 is classical Chinese verse; both compress and paraphrase, and MQM against the Tibetan penalises
  that. Their scores measure distance from a literal reading of the Tibetan, not translation quality.

## 4. Findings specific to this text

- **A one-call glossary review is too thin for a large glossary.** Gemini reviewing all 741 terms in one call
  raised 3 objections in Chinese and 0 in Hindi, and missed a contradiction a term agent had flagged. Reviewing in 4
  chunks (each call sees the whole glossary but reviews a quarter, plus the drafters' doubts) raised 37 and 44.
  Chunking can conflict across chunks: two chunks swapped the Hindi children's renderings of T446/T732 (fixed by an
  override).
- **Some glossary senses are wrong at single verses, and the checker finds them.** བྱང་ཆུབ་སེམས at 2-27 is the metrical
  short form of "bodhisattva" (as in the Ratnaguṇa), and ཉོན་མོངས at 4-37 and 8-150 means "wretched", not the
  afflictions. Each was fixed by excluding that occurrence from the locked term.
- **A text-critical divergence the pipeline cannot settle (5-7).** The Tibetan root reads མེ་ཚོགས "masses of fire"; the
  Sanskrit and Gyaltsab read "those women". Five of the six versions follow "women"; the Hindi children's version
  follows "fire"; the English children's checker fails the "women" reading. An editor has to choose; then 5-7 is
  regenerated in all six tracks.
- **Human references are numbered differently from the Tibetan.** Padmakara, Choephel, 蔣揚仁欽 and 如石 follow the
  standard edition's numbering, which has one or two more verses than the Tibetan root in chapters 3, 7 and 8. Any
  verse-by-verse comparison must map them to the Tibetan first (see chrF above).
- **Some over-literal Chinese glossary choices were approved by the cross-model rule** (e.g. 人有 for "human
  existence", 有道 for "path of existence", 彼世間 for "next world"); they are listed in STATE.md for an editor.

## 5. Still to do for this text

- **Editorial decision on 5-7** (fire vs women), then regenerate 5-7 in all six tracks.
- **Specialist scoring of the blind sample** (40 verses × 3 languages), as for the other texts.
- **Specialist review time** to bring the governed versions to publication.

## Method and caveats

- **Prices and token counting** are as in the Diamond Sutra report. Gemini tokens are exact. Claude output tokens are
  estimated from the text each agent wrote; thinking tokens are not counted, so Claude costs are a lower bound.
- **Shared costs sit under English:** the term list ($6.15) and its review ($3.60).
- **Wasted work is included:** a Chinese academic run stopped after 30 segments when the glossary was re-reviewed;
  the first one-call glossary reviews; ten English fact-check agents lost to a network drop are not in the ledger.
- **Not counted:** the orchestrating session and the one-time adaptation of the pipeline to this text.

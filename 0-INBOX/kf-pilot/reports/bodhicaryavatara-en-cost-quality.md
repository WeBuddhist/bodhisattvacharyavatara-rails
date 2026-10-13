---
title: Bodhicaryāvatāra (Chonjuk), English academic and children's — cost and quality
text: bodhicaryavatara
status: superseded
superseded_by: reports/bodhicaryavatara-cost-quality.md (en + zh + hi; chrF realigned; keep-best applied to en)
date: 2026-10-08
sources: usage-ledger.jsonl; factcheck/academic-a1..a3/verdicts.json; reports/improvement-bodhicaryavatara.json; reports/pairwise-bodhicaryavatara.json; reports/chrf-systems-bodhicaryavatara.json; factcheck/children-a1..a2; reports/pairwise-children-bodhicaryavatara.json
---

# Bodhicaryāvatāra (Chonjuk), English academic and children's — cost and quality

Second text of the KF pilot, same method as the Diamond Sutra: Gemini 3.1 Pro translates, Claude Sonnet agents check,
each model's output is reviewed by the other, no human reviewer. Tibetan root: 941 segments (910 verses, 10 chapter
colophons, intro, colophons, 14 headings), 26,724 Tibetan syllables — 2.5× the Diamond Sutra.

## 1. What was produced

| Output | Where | Size |
|---|---|---|
| Zero-shot baselines en (DharmaMitra, Gemini), zh, hi (Gemini) | `3-TRANSFORMATIONS/Translations/{Dharmamitra,Gemini}/` | 927 blocks + 13 headings each |
| Term list (Claude extraction, Gemini review) | `term-extract/bodhicaryavatara-en/term-list.md` | 742 terms, 2,305 occurrences |
| English termbase, academic + children's | `termbase/bodhicaryavatara-en/`, track folders | 741 terms (1 excluded), 15 multi-sense |
| English academic translation, fact-checked and fixed | `3-TRANSFORMATIONS/Translations/en-academic/` | 941/941 segments, every segment passes |
| English children's version (ages 8–12, from the academic), fact-checked and fixed | `3-TRANSFORMATIONS/Translations/en-children/` | 941/941 segments; all pass except 5-7 (text-critical divergence, flagged) |

## 2. Cost (list prices, USD)

| Step | Engine | Calls | USD |
|---|---|---|---|
| Zero-shot baselines en + zh + hi | Gemini 3.1 Pro | 375 | 23.43 |
| Zero-shot baseline en | DharmaMitra | 326 | free |
| Term extraction (27 agents incl. one re-run) | Claude Sonnet | — | 6.15 |
| Term review | Gemini 3.1 Pro | 26 | 3.60 |
| Termbase (style sheet + 16 agents) | Claude Sonnet | — | 6.44 |
| Termbase review | Gemini 3.1 Pro | 1 | 0.32 |
| Academic translation + 3 fix rounds | Gemini 3.1 Pro | 235 | 20.09 |
| Fact-check, 3 rounds (47 + 2 + 8 agents) | Claude Sonnet | — | 19.78 |
| Children's version (from the academic) + 2 fix rounds | Gemini 3.1 Pro | 205 | 8.16 |
| Children's fact-check, 2 rounds (24 + 6 agents) | Claude Sonnet | — | 6.03 |
| Improvement measure 4: blind pairwise judge (academic 153 + children 142 pairs, both orders) | Gemini 3.1 Pro | 76 | 5.30 |
| **Total so far** | | | **99.31** |

The English academic version alone (term extraction → termbase → translation → fact-check/fix, without the zh/hi
baselines) cost about **$64** (Gemini en zero-shot $7.29 included; zh/hi baselines and the judge excluded), or **$2.4 per 1,000 Tibetan syllables** (Diamond Sutra: $30.04 for 10,680 syllables,
$2.8 per 1,000). The children's version added **$14.19** (translation $8.16 + checks $6.03). Claude agent output tokens are estimated (transcripts keep only start-of-response usage); ten
fact-check agents lost to a network drop (batches 26–35, first launch) are not in the ledger.

## 3. Quality

### Fact-check (Claude Sonnet, segment by segment against Tibetan, Sanskrit and three commentaries)

| Round | Segments checked | Pass | Fail (major) | Minor issues |
|---|---|---|---|---|
| a1 — full text | 927 | 908 (98.0%) | 19 | 151 |
| a2 — the 19 fails, regenerated with the checker's feedback | 19 | 17 | 2 (4-37, 9-35) | 7 |
| a3 — 140 minor-issue segments regenerated + 4-37, 9-35 at attempt 3 | 142 | 138 | 4 (regressions) | 34 |
| Final (keep-best: the 4 regressions restored to their passing a1 text) | 927 | **927** | 0 | 45 |

Blocking errors in a1 were almost all mistranslations of syntax or reference (17 of 19): who acts on whom (3-1, 9-24),
two items fused into one (3-4), a disciple made a cause (9-35), a modifier attached to the wrong noun (8-85).

### Improvement from the fact-check and fix

| Measure | Before (a1) | After (final) |
|---|---|---|
| Failing segments | 19 | 0 |
| Critical / major issues | 0 / 19 | 0 / 0 |
| Minor issues | 151 | 45 |
| Issues per 100 segments | 18.3 | 4.9 |
| MQM-style penalty per 1,000 syllables (minor 1, major 5, critical 10) | 9.21 | 1.68 |
| Error-free segments | 82.8% | 95.7% |
| Locked-term compliance | 99.73% | 99.73% |
| chrF vs human translations, whole text (mean of 3) | 36.13 | 36.18 |
| chrF, the 152 changed segments | 36.23 | 36.52 |
| Blind pairwise judge (Gemini, both orders; changed segments) | — | fixed better 91 (59%), tie 39 (25%), original better 23 (15%) |

### chrF does not measure quality here

chrF (character n-gram overlap) against the three human English translations (Padmakara, Wallace, Choephel):

| System | Padmakara | Wallace | Choephel | Mean |
|---|---|---|---|---|
| DharmaMitra zero-shot | 33.49 | 39.18 | 38.61 | 37.09 |
| Gemini zero-shot | 31.92 | 38.16 | 38.29 | 36.12 |
| Academic, fact-checked (this pipeline) | 31.93 | 38.23 | 38.37 | 36.18 |
| Older "Rails" scholar version (prose, no termbase) | 29.91 | 33.08 | 32.54 | 31.84 |

The zero-shot baselines score as high as the checked version: chrF tracks wording and verse form, not whether the
meaning is right. It separates prose from verse (the older scholar version) but not accurate from inaccurate verse.
The fact-check verdicts and the blind judge are the meaningful measures; chrF is reported for completeness.

### Children's version (Gemini retells each verse from the approved academic; Claude checks it against academic + Tibetan)

| Round | Segments checked | Pass | Fail (major) | Minor issues |
|---|---|---|---|---|
| c1 — full text | 927 | 908 (98.0%) | 19 | 131 |
| c2 — 18 fails + 128 minor-issue segments regenerated (5-7 held back) | 146 | 143 | 3 (minor rewrites that regressed) | 28 |
| Final (keep-best: 7-11, 8-14, 9-103 restored to their c1 text) | 927 | **926** | 1 (5-7, flagged) | 31 |

| Measure | Before (c1) | After (final) |
|---|---|---|
| Failing segments | 19 | 1 (5-7, divergence) |
| Minor issues | 131 | 31 |
| Issues per 100 segments | 16.2 | 3.5 |
| MQM-style penalty per 1,000 syllables | 8.46 | 1.35 |
| Error-free segments | 84.1% | 96.7% |
| Locked-term compliance | 99.82% | 99.77% |
| Blind pairwise judge (142 changed segments) | — | fixed better 111 (78%), tie 21 (15%), original better 10 (7%) |

Children's errors in c1 were simplification errors: a conditional turned into a flat statement (2-55, 4-37), an
argument's direction reversed (8-139), the object of clinging confused with the clinging (6-71). Only one doctrinal
issue was raised, rated minor (9-48, on how emptiness is phrased); it was fixed in the c2 round.

## 4. Findings to carry into the KF report

- **Glossary errors cause translation errors.** Two of the 19 a1 fails came from the termbase, not the translator:
  a mis-cut span (སེམས་ཅན་དམྱལ in 6-47, "if beings go to hell", locked as "hell of sentient beings") and a term in a
  non-technical sense (ཉོན་མོངས in 4-37 = "wretched", locked as "affliction"). A third (5-4) locked a term and the
  compound containing it, forcing two renderings onto one phrase. Fixes: `exclude_terms` / `exclude_occurrences` in
  `overrides.json`; the translator no longer locks a term nested inside a longer locked term.
- **The termbase review made one of those errors worse** (it turned "sentient being going to hell" into
  "hell of sentient beings" for T463). Cross-model review catches inconsistency, not mis-segmentation.
- **Minor fixes can regress.** 4 of 140 minor-issue rewrites introduced a major error; the keep-best rule restored the
  passing text. Without a re-check, fixing minor issues would have added errors.
- **The checker and the blind judge disagree on 15% of changed segments** (original judged better although the
  checker passed the fix). The fix loop improves accuracy on the checker's terms; style preferences may go the
  other way.
- **Checker shortcut:** at least one agent (a1 batch 39) read the commentaries for only 4 of 20 segments — as seen
  with some Hindi checkers on the Diamond Sutra.
- **Text-critical divergence surfaced by the children's check (5-7).** The Tibetan reads མེ་ཚོགས "masses of fire" (Shenga follows it); the Sanskrit (*tāḥ striyaḥ*) and Gyaltsab's text read "women" (མོ་ཚོགས). The academic minor-fix round switched to "women"; the children's checker, reading the Tibetan, failed it. Left as is and flagged — a human editor must choose the reading.
- **The fix loop helps the children's version more than the academic** by the blind judge (78% vs 59% fixed better): children's errors are clear meaning slips; academic minor issues are closer to taste.
- **Gemini dropped two segment ids** (2-65, 2-a) in the same batch twice; translated singly, they were fine.
- **Infrastructure:** one silent Gemini hang (network), one network drop that killed 10 agents, a 20-agent
  concurrency limit, and a usage limit mid-run. All runs resume from append-only ledgers.

## 5. Still to do for this text

- Chinese and Hindi termbases (pivot on the English) and tracks.
- Optional editor pass on `review-flags.md`.

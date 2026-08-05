---
title: Fused Keyword Ranking (PMI-gated) — en
method: NPMI gate on multi-word phrases, then Reciprocal Rank Fusion
npmi_min: 0.3
min_count: 3
rrf_k: 60
corpus_tokens: 121765
terms: 7978
status: draft
---

# Fused Keyword Ranking (PMI-gated) — en

Every multi-word candidate is first asked whether it is a real collocation:

```
NPMI(t) = log2( p(phrase) / prod p(word) ) / -((n-1) * log2 p(phrase))
keep if NPMI >= 0.3 and count >= 3
```

Phrases that are only frequent because their parts are frequent score near 0
and drop out. Survivors are then fused with the single words on rank position,
since TF-IDF (higher=better) and YAKE (lower=better) are not comparable scales:

```
fused(t) = 1.0 / (60 + rank_tfidf(t)) + 1.0 / (60 + rank_yake(t))
```

| Coverage | Terms |
|----------|-------|
| Kept | 7,978 |
| Gated out (phrases) | 1,248 |
| In both lists | 1,782 |
| Multi-word phrases kept | 310 |

---

| Rank | Term | W | Count | NPMI | TF-IDF | YAKE | R(tfidf) | R(yake) | Fused | Band | Glossary |
|------|------|---|-------|------|--------|------|----------|---------|-------|------|----------|
| 1 | **dharma** | 1 | 409 | - | 67,972.93 | 0.000066 | 1 | 1 | 0.032787 | 🔴 extremely high — text-exclusive | ✓ ཆོས |
| 2 | **buddha** | 1 | 364 | - | 60,494.25 | 0.000120 | 2 | 2 | 0.032258 | 🔴 extremely high — text-exclusive | ✓ སངས་རྒྱས |
| 3 | **teacher** | 1 | 373 | - | 57,529.73 | 0.000327 | 3 | 3 | 0.031746 | 🔴 extremely high — text-exclusive | ~ |
| 4 | **action** | 1 | 340 | - | 26,092.45 | 0.000450 | 9 | 7 | 0.029418 | 🟠 very high — domain-specific | ~ |
| 5 | **mind** | 1 | 256 | - | 31,724.00 | 0.000769 | 7 | 14 | 0.028439 | 🟠 very high — domain-specific | ~ |
| 6 | **practice** | 1 | 236 | - | 27,769.08 | 0.000961 | 8 | 17 | 0.027693 | 🟠 very high — domain-specific | — |
| 7 | **time** | 1 | 329 | - | 21,906.07 | 0.000594 | 15 | 10 | 0.027619 | 🟠 very high — domain-specific | — |
| 8 | **life** | 1 | 240 | - | 22,905.14 | 0.000722 | 14 | 13 | 0.027212 | 🟠 very high — domain-specific | — |
| 9 | **teaching** | 1 | 218 | - | 36,230.07 | 0.001630 | 4 | 34 | 0.026263 | 🟠 very high — domain-specific | ~ |
| 10 | **jewel** | 1 | 128 | - | 21,272.70 | 0.000988 | 19 | 18 | 0.025479 | 🟠 very high — domain-specific | ~ |
| 11 | **compassion** | 1 | 147 | - | 24,438.36 | 0.001779 | 12 | 37 | 0.024198 | 🟠 very high — domain-specific | ~ |
| 12 | **king** | 1 | 144 | - | 17,955.68 | 0.001076 | 27 | 20 | 0.023994 | 🟠 very high — domain-specific | ~ |
| 13 | **realm** | 1 | 149 | - | 24,762.75 | 0.002122 | 10 | 49 | 0.023460 | 🟠 very high — domain-specific | ~ |
| 14 | **body** | 1 | 180 | - | 19,761.32 | 0.001752 | 22 | 35 | 0.022721 | 🟠 very high — domain-specific | ~ |
| 15 | **negative** | 1 | 166 | - | 16,949.33 | 0.001416 | 30 | 28 | 0.022475 | 🟠 very high — domain-specific | ~ |
| 16 | **merit** | 1 | 142 | - | 20,524.28 | 0.001939 | 20 | 41 | 0.022401 | 🟠 very high — domain-specific | ✓ བསོད་ནམས |
| 17 | **death** | 1 | 129 | - | 18,346.78 | 0.001597 | 26 | 33 | 0.022381 | 🟠 very high — domain-specific | ~ |
| 18 | **bodhicitta** | 1 | 130 | - | 21,605.09 | 0.002119 | 17 | 48 | 0.022246 | 🟠 very high — domain-specific | ✓ བྱང་ཆུབ་ཀྱི་སེམས |
| 19 | **bodhisattva** | 1 | 99 | - | 16,453.11 | 0.001569 | 32 | 31 | 0.021859 | 🟠 very high — domain-specific | ✓ བྱང་ཆུབ་སེམས་དཔའ |
| 20 | **person** | 1 | 260 | - | 32,219.69 | 0.004112 | 6 | 96 | 0.021562 | 🟠 very high — domain-specific | — |
| 21 | **refuge** | 1 | 129 | - | 18,989.90 | 0.002155 | 24 | 50 | 0.020996 | 🟠 very high — domain-specific | — |
| 22 | **path** | 1 | 145 | - | 19,603.49 | 0.002170 | 23 | 52 | 0.020977 | 🟠 very high — domain-specific | ~ |
| 23 | **practise** | 1 | 123 | - | 20,448.42 | 0.002308 | 21 | 56 | 0.020966 | 🟠 very high — domain-specific | — |
| 24 | **suffering** | 1 | 192 | - | 24,095.69 | 0.004281 | 13 | 102 | 0.019871 | 🟠 very high — domain-specific | ~ |
| 25 | **offering** | 1 | 180 | - | 16,498.55 | 0.002287 | 31 | 55 | 0.019685 | 🟠 very high — domain-specific | ~ |
| 26 | **word** | 1 | 128 | - | 16,963.21 | 0.002665 | 29 | 63 | 0.019366 | 🟠 very high — domain-specific | ~ |
| 27 | **hell** | 1 | 114 | - | 17,582.81 | 0.002791 | 28 | 67 | 0.019238 | 🟠 very high — domain-specific | ✓ དམྱལ་བ |
| 28 | **wisdom** | 1 | 109 | - | 16,045.73 | 0.002631 | 34 | 62 | 0.018835 | 🟠 very high — domain-specific | ✓ ཤེས་རབ |
| 29 | **day** | 1 | 164 | - | 12,234.83 | 0.002019 | 57 | 44 | 0.018162 | 🟠 very high — domain-specific | — |
| 30 | **past** | 1 | 138 | - | 11,048.46 | 0.001969 | 72 | 42 | 0.017380 | 🟠 very high — domain-specific | — |
| 31 | **faith** | 1 | 108 | - | 14,942.45 | 0.002993 | 43 | 71 | 0.017342 | 🟠 very high — domain-specific | — |
| 32 | **mother** | 1 | 96 | - | 15,954.53 | 0.003439 | 38 | 82 | 0.017246 | 🟠 very high — domain-specific | ~ |
| 33 | **perfect** | 1 | 97 | - | 15,444.41 | 0.003425 | 40 | 80 | 0.017143 | 🟠 very high — domain-specific | — |
| 34 | **buddhahood** | 1 | 62 | - | 10,303.97 | 0.002039 | 82 | 46 | 0.016476 | 🟠 very high — domain-specific | — |
| 35 | **thought** | 1 | 152 | - | 15,866.97 | 0.004203 | 39 | 97 | 0.016470 | 🟠 very high — domain-specific | ✓ རྣམ་རྟོག |
| 36 | **god** | 1 | 96 | - | 15,959.74 | 0.004406 | 37 | 106 | 0.016333 | 🟠 very high — domain-specific | — |
| 37 | **place** | 1 | 128 | - | 11,398.95 | 0.002708 | 67 | 65 | 0.015874 | 🟠 very high — domain-specific | — |
| 38 | **human** | 1 | 98 | - | 13,397.02 | 0.003668 | 51 | 86 | 0.015858 | 🟠 very high — domain-specific | — |
| 39 | **master** | 1 | 77 | - | 10,653.42 | 0.002529 | 76 | 59 | 0.015756 | 🟠 very high — domain-specific | ~ |
| 40 | **great** | 1 | - | - | - | 0.000332 | - | 4 | 0.015749 | - | — |
| 41 | **make** | 1 | 211 | - | 14,759.13 | 0.004374 | 44 | 104 | 0.015713 | 🟠 very high — domain-specific | — |
| 42 | **thing** | 1 | 113 | - | 13,180.98 | 0.003745 | 52 | 88 | 0.015685 | 🟠 very high — domain-specific | — |
| 43 | **take** | 1 | 166 | - | 11,261.53 | 0.002786 | 70 | 66 | 0.015629 | 🟠 very high — domain-specific | — |
| 44 | **like** | 1 | 397 | - | 35,724.30 | - | 5 | - | 0.015509 | 🟠 very high — domain-specific | — |
| 45 | **negative action** | 2 | 81 | 0.706 | - | 0.000408 | - | 5 | 0.015509 | - | ✓ སྡིག་པ / མི་དགེ་བ |
| 46 | **friend** | 1 | 96 | - | 15,959.74 | 0.005832 | 36 | 138 | 0.015467 | 🟠 very high — domain-specific | ~ |
| 47 | **heart** | 1 | 99 | - | 11,993.17 | 0.003583 | 59 | 84 | 0.015348 | 🟠 very high — domain-specific | — |
| 48 | **dharma king** | 2 | 9 | 0.311 | - | 0.000417 | - | 6 | 0.015276 | - | ~ |
| 49 | **mila** | 1 | 60 | - | 9,974.84 | 0.002356 | 91 | 57 | 0.015170 | 🟡 high — specialist register | ~ |
| 50 | **dharma king trisong** | 3 | 3 | 0.541 | - | 0.000557 | - | 8 | 0.014830 | - | ~ |
| 51 | **instruction** | 1 | 83 | - | 13,798.53 | 0.005127 | 49 | 120 | 0.014730 | 🟠 very high — domain-specific | — |
| 52 | **vajra** | 1 | 66 | - | 10,968.74 | 0.003303 | 75 | 77 | 0.014707 | 🟠 very high — domain-specific | ✓ རྡོ་རྗེ |
| 53 | **suffer** | 1 | 50 | - | 5,995.24 | 0.001467 | 222 | 30 | 0.014657 | 🟡 high — specialist register | — |
| 54 | **dharma king songtsen** | 3 | 3 | 0.548 | - | 0.000568 | - | 9 | 0.014617 | - | ~ |
| 55 | **samsara** | 1 | 79 | - | 13,129.25 | 0.004772 | 53 | 115 | 0.014564 | 🟠 very high — domain-specific | ✓ འཁོར་བ |
| 56 | **thousand** | 1 | 96 | - | 11,896.50 | 0.004223 | 61 | 99 | 0.014554 | 🟠 very high — domain-specific | ~ |
| 57 | **happiness** | 1 | 77 | - | 12,796.86 | 0.005017 | 54 | 118 | 0.014390 | 🟠 very high — domain-specific | — |
| 58 | **effect** | 1 | 127 | - | 10,333.82 | 0.003358 | 80 | 78 | 0.014389 | 🟠 very high — domain-specific | ~ |
| 59 | **teach** | 1 | 43 | - | 7,148.63 | 0.001889 | 172 | 40 | 0.014310 | 🟡 high — specialist register | — |
| 60 | **yourself** | 1 | 154 | - | 24,519.98 | - | 11 | - | 0.014209 | 🟠 very high — domain-specific | — |
| 61 | **true dharma** | 2 | 16 | 0.469 | - | 0.000664 | - | 11 | 0.014209 | - | ~ |
| 62 | **live** | 1 | 134 | - | 14,666.97 | 0.006374 | 45 | 154 | 0.014197 | 🟠 very high — domain-specific | — |
| 63 | **reborn** | 1 | 75 | - | 12,464.47 | 0.005302 | 55 | 126 | 0.014072 | 🟠 very high — domain-specific | — |
| 64 | **practise dharma** | 2 | 11 | 0.352 | - | 0.000705 | - | 12 | 0.014013 | - | — |
| 65 | **disciple** | 1 | 86 | - | 14,292.60 | 0.006740 | 46 | 164 | 0.013898 | 🟠 very high — domain-specific | ~ |
| 66 | **good** | 1 | 7 | - | 563.83 | 0.000894 | 2,273 | 16 | 0.013587 | 🟢 medium — moderately distinctive | ~ |
| 67 | **evil** | 1 | 74 | - | 12,302.30 | 0.006005 | 56 | 144 | 0.013523 | 🟠 very high — domain-specific | — |
| 68 | **food** | 1 | 107 | - | 9,354.04 | 0.003186 | 106 | 74 | 0.013487 | 🟡 high — specialist register | — |
| 69 | **wealth** | 1 | 76 | - | 11,427.98 | 0.005259 | 65 | 123 | 0.013464 | 🟠 very high — domain-specific | ~ |
| 70 | **hand** | 1 | 103 | - | 11,413.93 | 0.005193 | 66 | 121 | 0.013461 | 🟠 very high — domain-specific | — |
| 71 | **jetsun mila** | 2 | 30 | 0.859 | - | 0.000853 | - | 15 | 0.013458 | - | ~ |
| 72 | **power** | 1 | 107 | - | 9,782.58 | 0.003576 | 97 | 83 | 0.013362 | 🟡 high — specialist register | — |
| 73 | **kalpa** | 1 | 70 | - | 11,633.51 | 0.005390 | 64 | 129 | 0.013356 | 🟠 very high — domain-specific | ✓ བསྐལ་པ |
| 74 | **think** | 1 | 103 | - | 8,799.37 | 0.002818 | 122 | 68 | 0.013307 | 🟡 high — specialist register | — |
| 75 | **without** | 1 | 266 | - | 21,766.06 | - | 16 | - | 0.013282 | 🟠 very high — domain-specific | ~ |
| 76 | **hundred** | 1 | 124 | - | 16,015.88 | 0.015393 | 35 | 334 | 0.013064 | 🟠 very high — domain-specific | ~ |
| 77 | **never** | 1 | 197 | - | 21,562.63 | - | 18 | - | 0.012945 | 🟠 very high — domain-specific | — |
| 78 | **head** | 1 | 102 | - | 9,647.73 | 0.003943 | 98 | 93 | 0.012865 | 🟡 high — specialist register | — |
| 79 | **being** | 1 | 258 | - | 18,491.01 | 0.059673 | 25 | 861 | 0.012850 | 🟠 very high — domain-specific | ~ |
| 80 | **secret** | 1 | 61 | - | 8,011.09 | 0.002884 | 138 | 69 | 0.012802 | 🟡 high — specialist register | ~ |
| 81 | **buddha sakyamuni** | 2 | 8 | 0.552 | - | 0.001044 | - | 19 | 0.012783 | - | — |
| 82 | **meditate** | 1 | 68 | - | 11,301.12 | 0.006176 | 68 | 150 | 0.012574 | 🟠 very high — domain-specific | ~ |
| 83 | **mantra** | 1 | 63 | - | 10,470.16 | 0.005553 | 77 | 133 | 0.012481 | 🟠 very high — domain-specific | ✓ སྔགས |
| 84 | **lord buddha** | 2 | 3 | 0.301 | - | 0.001077 | - | 21 | 0.012470 | - | ~ |
| 85 | **state** | 1 | 110 | - | 8,154.06 | 0.003281 | 137 | 76 | 0.012429 | 🟡 high — specialist register | ~ |
| 86 | **positive** | 1 | 91 | - | 9,090.69 | 0.003805 | 114 | 90 | 0.012414 | 🟡 high — specialist register | ~ |
| 87 | **perfect buddha** | 2 | 10 | 0.390 | - | 0.001148 | - | 22 | 0.012320 | - | — |
| 88 | **meditation** | 1 | 68 | - | 11,301.12 | 0.006592 | 69 | 160 | 0.012297 | 🟠 very high — domain-specific | ~ |
| 89 | **great master** | 2 | 13 | 0.473 | - | 0.001219 | - | 23 | 0.012173 | - | ~ |
| 90 | **spiritual** | 1 | 66 | - | 10,968.74 | 0.006315 | 74 | 153 | 0.012158 | 🟠 very high — domain-specific | ~ |
| 91 | **feel** | 1 | 90 | - | 9,793.18 | 0.004768 | 96 | 114 | 0.012157 | 🟡 high — specialist register | — |
| 92 | **people** | 1 | - | - | - | 0.001279 | - | 24 | 0.012029 | - | — |
| 93 | **jetsun** | 1 | 50 | - | 8,309.65 | 0.003646 | 135 | 85 | 0.012025 | 🟡 high — specialist register | ~ |
| 94 | **quality** | 1 | 86 | - | 8,640.61 | 0.003845 | 126 | 91 | 0.011999 | 🟡 high — specialist register | — |
| 95 | **die** | 1 | 67 | - | 10,333.76 | 0.006037 | 81 | 145 | 0.011970 | 🟠 very high — domain-specific | — |
| 96 | **deity** | 1 | 71 | - | 11,799.70 | 0.008871 | 62 | 208 | 0.011928 | 🟠 very high — domain-specific | ✓ ལྷ |
| 97 | **king jewel crest** | 3 | 3 | 0.586 | - | 0.001307 | - | 25 | 0.011889 | - | — |
| 98 | **pure** | 1 | 72 | - | 10,093.10 | 0.005607 | 89 | 134 | 0.011866 | 🟠 very high — domain-specific | ~ |
| 99 | **tibet** | 1 | 46 | - | 7,644.88 | 0.003430 | 152 | 81 | 0.011809 | 🟡 high — specialist register | — |
| 100 | **positive action** | 2 | 37 | 0.615 | - | 0.001327 | - | 26 | 0.011752 | - | ✓ དགེ་བ |
| 101 | **authentic dharma** | 2 | 11 | 0.470 | - | 0.001389 | - | 27 | 0.011619 | - | — |
| 102 | **water** | 1 | 87 | - | 9,019.36 | 0.004500 | 117 | 108 | 0.011602 | 🟡 high — specialist register | ~ |
| 103 | **ordinary** | 1 | 84 | - | 8,558.91 | 0.004252 | 128 | 100 | 0.011569 | 🟡 high — specialist register | ~ |
| 104 | **moment** | 1 | 84 | - | 9,088.30 | 0.004593 | 115 | 111 | 0.011562 | 🟡 high — specialist register | ~ |
| 105 | **lama** | 1 | 66 | - | 10,972.32 | 0.007993 | 73 | 189 | 0.011535 | 🟠 very high — domain-specific | ✓ བླ་མ |
| 106 | **single** | 1 | 84 | - | 8,748.23 | 0.004387 | 123 | 105 | 0.011525 | 🟡 high — specialist register | — |
| 107 | **perfection** | 1 | 61 | - | 10,137.77 | 0.006423 | 87 | 155 | 0.011454 | 🟠 very high — domain-specific | ~ |
| 108 | **secret mantra vajrayana** | 3 | 10 | 0.788 | - | 0.001430 | - | 29 | 0.011360 | - | ~ |
| 109 | **end** | 1 | 104 | - | 6,646.48 | 0.003186 | 195 | 75 | 0.011329 | 🟡 high — specialist register | — |
| 110 | **love** | 1 | 66 | - | 10,179.52 | 0.006964 | 85 | 170 | 0.011244 | 🟠 very high — domain-specific | — |
| 111 | **recite** | 1 | 62 | - | 10,303.97 | 0.007511 | 83 | 180 | 0.011160 | 🟠 very high — domain-specific | — |
| 112 | **wrong** | 1 | 71 | - | 9,324.39 | 0.005832 | 107 | 139 | 0.011013 | 🟡 high — specialist register | ~ |
| 113 | **great vehicle** | 2 | 14 | 0.534 | - | 0.001587 | - | 32 | 0.010994 | - | ✓ ཐེག་པ་ཆེན་པོ |
| 114 | **prayer** | 1 | 67 | - | 11,138.57 | 0.009960 | 71 | 242 | 0.010945 | 🟠 very high — domain-specific | — |
| 115 | **benefit** | 1 | 89 | - | 8,546.72 | 0.005053 | 129 | 119 | 0.010878 | 🟡 high — specialist register | — |
| 116 | **whatever** | 1 | 132 | - | 16,260.33 | - | 33 | - | 0.010877 | 🟠 very high — domain-specific | — |
| 117 | **true** | 1 | 72 | - | 8,722.31 | 0.005381 | 124 | 128 | 0.010754 | 🟡 high — specialist register | ~ |
| 118 | **bring** | 1 | 93 | - | 8,568.41 | 0.005425 | 127 | 131 | 0.010583 | 🟡 high — specialist register | — |
| 119 | **flesh** | 1 | 59 | - | 9,808.59 | 0.007907 | 94 | 186 | 0.010559 | 🟡 high — specialist register | — |
| 120 | **great perfection** | 2 | 15 | 0.522 | - | 0.001754 | - | 36 | 0.010541 | - | ✓ རྫོགས་པ་ཆེན་པོ |
| 121 | **vow** | 1 | 63 | - | 10,470.16 | 0.010677 | 78 | 248 | 0.010493 | 🟠 very high — domain-specific | — |
| 122 | **lord** | 1 | 47 | - | 6,172.48 | 0.003741 | 214 | 87 | 0.010452 | 🟡 high — specialist register | ~ |
| 123 | **guru** | 1 | 43 | - | 7,146.30 | 0.004289 | 173 | 103 | 0.010427 | 🟡 high — specialist register | ~ |
| 124 | **liberation** | 1 | 58 | - | 9,642.34 | 0.007739 | 100 | 183 | 0.010365 | 🟡 high — specialist register | ✓ ཐར་པ |
| 125 | **perfect buddhahood** | 2 | 24 | 0.725 | - | 0.001807 | - | 38 | 0.010328 | - | — |
| 126 | **great compassion** | 2 | 13 | 0.402 | - | 0.001869 | - | 39 | 0.010225 | - | ~ |
| 127 | **man** | 1 | 77 | - | 9,945.35 | 0.009341 | 92 | 218 | 0.010176 | 🟡 high — specialist register | — |
| 128 | **follow** | 1 | 80 | - | 8,390.65 | 0.005941 | 131 | 143 | 0.010162 | 🟡 high — specialist register | — |
| 129 | **realization** | 1 | 64 | - | 9,102.28 | 0.006987 | 112 | 171 | 0.010143 | 🟡 high — specialist register | — |
| 130 | **harm** | 1 | 69 | - | 8,659.39 | 0.006225 | 125 | 152 | 0.010122 | 🟡 high — specialist register | — |
| 131 | **kind** | 1 | 86 | - | 9,441.52 | 0.008009 | 105 | 190 | 0.010061 | 🟡 high — specialist register | — |
| 132 | **way** | 1 | 184 | - | 15,193.52 | - | 41 | - | 0.010025 | 🟠 very high — domain-specific | ~ |
| 133 | **come** | 1 | 178 | - | 15,120.58 | - | 42 | - | 0.009928 | 🟠 very high — domain-specific | ~ |
| 134 | **animal** | 1 | 79 | - | 9,621.98 | 0.009116 | 101 | 213 | 0.009874 | 🟡 high — specialist register | — |
| 135 | **demon** | 1 | 61 | - | 10,137.77 | 0.011396 | 88 | 262 | 0.009862 | 🟠 very high — domain-specific | ✓ བདུད |
| 136 | **real buddha** | 2 | 9 | 0.470 | - | 0.001997 | - | 43 | 0.009833 | - | ~ |
| 137 | **transference** | 1 | 55 | - | 9,140.61 | 0.008558 | 111 | 202 | 0.009665 | 🟡 high — specialist register | ✓ འཕོ་བ |
| 138 | **secret mantra vehicle** | 3 | 5 | 0.638 | - | 0.002038 | - | 45 | 0.009648 | - | ~ |
| 139 | **enemy** | 1 | 63 | - | 9,473.19 | 0.009551 | 104 | 223 | 0.009631 | 🟡 high — specialist register | — |
| 140 | **precious** | 1 | 56 | - | 7,125.04 | 0.005355 | 174 | 127 | 0.009621 | 🟡 high — specialist register | ~ |
| 141 | **visualize** | 1 | 55 | - | 9,143.60 | 0.008891 | 110 | 209 | 0.009600 | 🟡 high — specialist register | — |
| 142 | **sutra** | 1 | 50 | - | 8,309.65 | 0.006830 | 134 | 165 | 0.009599 | 🟡 high — specialist register | ✓ མདོ |
| 143 | **mean** | 1 | 88 | - | 8,929.73 | 0.008328 | 119 | 194 | 0.009524 | 🟡 high — specialist register | — |
| 144 | **lower** | 1 | 84 | - | 5,688.69 | 0.004263 | 243 | 101 | 0.009512 | 🟡 high — specialist register | ~ |
| 145 | **once** | 1 | 140 | - | 14,235.44 | - | 47 | - | 0.009470 | 🟠 very high — domain-specific | ~ |
| 146 | **guru yoga** | 2 | 23 | 0.886 | - | 0.002044 | - | 47 | 0.009470 | - | ✓ བླ་མའི་རྣལ་འབྱོར |
| 147 | **find** | 1 | 75 | - | 7,083.56 | 0.005444 | 178 | 132 | 0.009410 | 🟡 high — specialist register | — |
| 148 | **say** | 1 | 185 | - | 14,010.55 | - | 48 | - | 0.009384 | 🟠 very high — domain-specific | — |
| 149 | **blessing** | 1 | 58 | - | 9,234.80 | 0.009812 | 109 | 234 | 0.009319 | 🟡 high — specialist register | — |
| 150 | **monk** | 1 | 82 | - | 13,627.82 | - | 50 | - | 0.009215 | 🟠 very high — domain-specific | — |
| 151 | **dharma protector** | 2 | 6 | 0.369 | - | 0.002166 | - | 51 | 0.009133 | - | ✓ ཆོས་སྐྱོང |
| 152 | **tantra** | 1 | 53 | - | 8,808.23 | 0.009426 | 120 | 221 | 0.009114 | 🟡 high — specialist register | ✓ རྒྱུད |
| 153 | **world** | 1 | 103 | - | 6,966.34 | 0.005940 | 182 | 142 | 0.009083 | 🟡 high — specialist register | ~ |
| 154 | **call** | 1 | 18 | - | 1,658.40 | 0.002703 | 977 | 64 | 0.009029 | 🟢 medium — moderately distinctive | — |
| 155 | **oddiyana** | 1 | 36 | - | 5,982.95 | 0.005205 | 226 | 122 | 0.008991 | 🟡 high — specialist register | ✓ ཨོ་རྒྱན |
| 156 | **secret mantra** | 2 | 20 | 0.740 | - | 0.002174 | - | 53 | 0.008974 | - | ~ |
| 157 | **ask** | 1 | 41 | - | 4,353.66 | 0.004031 | 344 | 94 | 0.008969 | 🟡 high — specialist register | — |
| 158 | **bodhisattvas** | 1 | - | - | - | 0.002181 | - | 54 | 0.008896 | - | — |
| 159 | **free** | 1 | 71 | - | 6,337.24 | 0.005904 | 203 | 141 | 0.008777 | 🟡 high — specialist register | ~ |
| 160 | **harmful** | 1 | 57 | - | 7,886.29 | 0.008334 | 146 | 195 | 0.008776 | 🟡 high — specialist register | — |
| 161 | **father** | 1 | 54 | - | 8,328.70 | 0.009656 | 132 | 230 | 0.008657 | 🟡 high — specialist register | — |
| 162 | **essence** | 1 | 50 | - | 8,312.37 | 0.009694 | 133 | 232 | 0.008606 | 🟡 high — specialist register | ✓ ཐིག་ལེ |
| 163 | **everything** | 1 | 96 | - | 12,214.35 | - | 58 | - | 0.008599 | 🟠 very high — domain-specific | — |
| 164 | **secret mantrayana** | 2 | 18 | 0.850 | - | 0.002519 | - | 58 | 0.008599 | - | ✓ གསང་སྔགས་ཀྱི་ཐེག་པ |
| 165 | **vajrasattva** | 1 | 35 | - | 5,816.75 | 0.005716 | 234 | 136 | 0.008503 | 🟡 high — specialist register | ✓ རྡོ་རྗེ་སེམས་དཔའ |
| 166 | **nature** | 1 | 59 | - | 7,186.04 | 0.007632 | 169 | 182 | 0.008499 | 🟡 high — specialist register | ~ |
| 167 | **themselve** | 1 | 72 | - | 11,965.89 | - | 60 | - | 0.008458 | 🟠 very high — domain-specific | — |
| 168 | **bodhisattva dharmodgata** | 2 | 10 | 0.688 | - | 0.002558 | - | 60 | 0.008458 | - | ~ |
| 169 | **rinpoche** | 1 | 34 | - | 5,650.56 | 0.005697 | 246 | 135 | 0.008396 | 🟡 high — specialist register | ~ |
| 170 | **buddha amitabha** | 2 | 3 | 0.429 | - | 0.002597 | - | 61 | 0.008389 | - | ~ |
| 171 | **root** | 1 | 55 | - | 7,518.74 | 0.008647 | 158 | 204 | 0.008375 | 🟡 high — specialist register | ~ |
| 172 | **speech** | 1 | 64 | - | 6,634.93 | 0.006963 | 196 | 169 | 0.008273 | 🟡 high — specialist register | ~ |
| 173 | **give** | 1 | 91 | - | 7,313.10 | 0.008624 | 164 | 203 | 0.008267 | 🟡 high — specialist register | — |
| 174 | **many** | 1 | 146 | - | 11,654.17 | - | 63 | - | 0.008254 | 🟠 very high — domain-specific | — |
| 175 | **experience** | 1 | 63 | - | 7,412.93 | 0.008972 | 160 | 210 | 0.008249 | 🟡 high — specialist register | ~ |
| 176 | **form** | 1 | 75 | - | 6,686.65 | 0.007101 | 191 | 175 | 0.008239 | 🟡 high — specialist register | — |
| 177 | **profound** | 1 | 50 | - | 7,961.03 | 0.010226 | 144 | 244 | 0.008191 | 🟡 high — specialist register | ~ |
| 178 | **present** | 1 | 69 | - | 5,802.49 | 0.006152 | 237 | 149 | 0.008152 | 🟡 high — specialist register | — |
| 179 | **point** | 1 | 78 | - | 6,398.16 | 0.007179 | 202 | 176 | 0.008054 | 🟡 high — specialist register | ~ |
| 180 | **act** | 1 | 80 | - | 7,390.07 | 0.009438 | 162 | 222 | 0.008051 | 🟡 high — specialist register | — |
| 181 | **blood** | 1 | 51 | - | 7,149.28 | 0.009414 | 170 | 220 | 0.007919 | 🟡 high — specialist register | — |
| 182 | **naropa** | 1 | 35 | - | 5,816.75 | 0.006602 | 236 | 161 | 0.007903 | 🟡 high — specialist register | ✓ ནཱ་རོ་པ |
| 183 | **lineage** | 1 | 47 | - | 7,811.07 | 0.011716 | 148 | 269 | 0.007847 | 🟡 high — specialist register | ~ |
| 184 | **light** | 1 | 61 | - | 5,769.72 | 0.006719 | 238 | 163 | 0.007840 | 🟡 high — specialist register | ~ |
| 185 | **take refuge** | 2 | 24 | 0.576 | - | 0.002983 | - | 70 | 0.007817 | - | — |
| 186 | **spirit** | 1 | 58 | - | 7,103.66 | 0.009555 | 176 | 225 | 0.007746 | 🟡 high — specialist register | — |
| 187 | **mandala** | 1 | 46 | - | 7,644.88 | 0.011530 | 155 | 266 | 0.007719 | 🟡 high — specialist register | ✓ དཀྱིལ་འཁོར |
| 188 | **vehicle** | 1 | 49 | - | 6,190.85 | 0.007987 | 212 | 188 | 0.007709 | 🟡 high — specialist register | ✓ ཐེག་པ |
| 189 | **human life** | 2 | 18 | 0.519 | - | 0.003045 | - | 72 | 0.007700 | - | — |
| 190 | **rebirth** | 1 | 48 | - | 7,977.26 | 0.014238 | 141 | 311 | 0.007671 | 🟡 high — specialist register | — |
| 191 | **accomplishment** | 1 | 52 | - | 8,279.48 | 0.015271 | 136 | 333 | 0.007647 | 🟡 high — specialist register | ✓ དངོས་གྲུབ |
| 192 | **king jewel** | 2 | 4 | 0.321 | - | 0.003134 | - | 73 | 0.007643 | - | ~ |
| 193 | **method** | 1 | 58 | - | 6,855.53 | 0.009605 | 186 | 228 | 0.007537 | 🟡 high — specialist register | — |
| 194 | **attain** | 1 | 51 | - | 7,056.16 | 0.009875 | 179 | 239 | 0.007529 | 🟡 high — specialist register | — |
| 195 | **atisa** | 1 | 33 | - | 5,484.37 | 0.006960 | 259 | 168 | 0.007521 | 🟡 high — specialist register | — |
| 196 | **transcendent** | 1 | 42 | - | 6,980.11 | 0.009917 | 181 | 241 | 0.007472 | 🟡 high — specialist register | ~ |
| 197 | **eye** | 1 | 52 | - | 7,108.63 | 0.011038 | 175 | 253 | 0.007450 | 🟡 high — specialist register | — |
| 198 | **yoga** | 1 | 36 | - | 5,982.95 | 0.008115 | 228 | 192 | 0.007440 | 🟡 high — specialist register | ~ |
| 199 | **preta** | 1 | 48 | - | 7,977.26 | 0.015646 | 143 | 340 | 0.007426 | 🟡 high — specialist register | ✓ ཡི་དྭགས |
| 200 | **devotion** | 1 | 44 | - | 7,312.49 | 0.012503 | 165 | 284 | 0.007351 | 🟡 high — specialist register | — |
| 201 | **having** | 1 | 107 | - | 10,443.96 | - | 79 | - | 0.007319 | 🟠 very high — domain-specific | — |
| 202 | **long** | 1 | - | - | - | 0.003378 | - | 79 | 0.007319 | - | — |
| 203 | **geshe** | 1 | 32 | - | 5,318.18 | 0.007867 | 268 | 185 | 0.007130 | 🟡 high — specialist register | ✓ དགེ་བཤེས |
| 204 | **marpa** | 1 | 30 | - | 4,985.79 | 0.007002 | 295 | 173 | 0.007109 | 🟡 high — specialist register | ✓ ལྷོ་བྲག་མར་པ |
| 205 | **again** | 1 | 116 | - | 10,183.83 | - | 84 | - | 0.007069 | 🟠 very high — domain-specific | — |
| 206 | **sublime** | 1 | 40 | - | 6,647.72 | 0.011347 | 194 | 260 | 0.007062 | 🟡 high — specialist register | ~ |
| 207 | **protector** | 1 | 46 | - | 7,644.88 | 0.017176 | 154 | 366 | 0.007020 | 🟡 high — specialist register | ~ |
| 208 | **daughter** | 1 | 38 | - | 6,315.33 | 0.010625 | 208 | 247 | 0.006989 | 🟡 high — specialist register | — |
| 209 | **born** | 1 | 61 | - | 10,141.09 | - | 86 | - | 0.006974 | 🟠 very high — domain-specific | ~ |
| 210 | **india** | 1 | 33 | - | 3,495.30 | 0.005850 | 448 | 140 | 0.006969 | 🟡 high — specialist register | — |
| 211 | **son** | 1 | 46 | - | 7,094.82 | 0.014079 | 177 | 305 | 0.006959 | 🟡 high — specialist register | — |
| 212 | **empowerment** | 1 | 46 | - | 7,644.88 | 0.019056 | 153 | 389 | 0.006922 | 🟡 high — specialist register | ✓ དབང་བསྐུར |
| 213 | **important** | 1 | 56 | - | 5,296.80 | 0.008523 | 271 | 198 | 0.006897 | 🟡 high — specialist register | — |
| 214 | **wheel** | 1 | 40 | - | 6,649.89 | 0.012437 | 193 | 282 | 0.006877 | 🟡 high — specialist register | ✓ འཁོར་ལོ |
| 215 | **tree** | 1 | 48 | - | 6,728.73 | 0.012763 | 190 | 288 | 0.006874 | 🟡 high — specialist register | ~ |
| 216 | **sky** | 1 | 41 | - | 6,816.14 | 0.013473 | 187 | 294 | 0.006873 | 🟡 high — specialist register | — |
| 217 | **leave** | 1 | 43 | - | 4,554.48 | 0.007017 | 328 | 174 | 0.006851 | 🟡 high — specialist register | — |
| 218 | **authentic** | 1 | 41 | - | 6,813.91 | 0.013536 | 188 | 295 | 0.006849 | 🟡 high — specialist register | — |
| 219 | **root teacher** | 2 | 12 | 0.474 | - | 0.003766 | - | 89 | 0.006836 | - | ✓ རྩ་བའི་བླ་མ |
| 220 | **always** | 1 | 89 | - | 10,063.99 | - | 90 | - | 0.006791 | 🟠 very high — domain-specific | — |
| 221 | **real dharma** | 2 | 4 | 0.331 | - | 0.003907 | - | 92 | 0.006703 | - | ~ |
| 222 | **view** | 1 | 67 | - | 6,256.51 | 0.012126 | 209 | 275 | 0.006703 | 🟡 high — specialist register | ✓ ལྟ་བ |
| 223 | **joy** | 1 | 38 | - | 6,317.40 | 0.012436 | 206 | 281 | 0.006692 | 🟡 high — specialist register | ~ |
| 224 | **taking** | 1 | 111 | - | 9,862.79 | - | 93 | - | 0.006660 | 🟡 high — specialist register | — |
| 225 | **eat** | 1 | 43 | - | 6,329.97 | 0.013319 | 204 | 290 | 0.006645 | 🟡 high — specialist register | — |
| 226 | **samaya** | 1 | 48 | - | 7,977.26 | 0.031117 | 142 | 537 | 0.006626 | 🟡 high — specialist register | ✓ དམ་ཚིག |
| 227 | **supreme** | 1 | 46 | - | 5,700.41 | 0.010038 | 241 | 243 | 0.006623 | 🟡 high — specialist register | ~ |
| 228 | **other** | 1 | 178 | - | 9,798.28 | - | 95 | - | 0.006576 | 🟡 high — specialist register | — |
| 229 | **discover dharma** | 2 | 6 | 0.559 | - | 0.004069 | - | 95 | 0.006576 | - | — |
| 230 | **year** | 1 | 82 | - | 3,066.19 | 0.006052 | 525 | 146 | 0.006564 | 🟡 high — specialist register | — |
| 231 | **freedom** | 1 | 54 | - | 6,577.05 | 0.014596 | 197 | 319 | 0.006530 | 🟡 high — specialist register | — |
| 232 | **kill** | 1 | 38 | - | 5,404.48 | 0.009683 | 264 | 231 | 0.006523 | 🟡 high — specialist register | — |
| 233 | **advantage** | 1 | 52 | - | 5,726.32 | 0.011176 | 240 | 256 | 0.006498 | 🟡 high — specialist register | — |
| 234 | **effort** | 1 | 59 | - | 5,674.74 | 0.011153 | 244 | 255 | 0.006464 | 🟡 high — specialist register | — |
| 235 | **nectar** | 1 | 39 | - | 6,481.53 | 0.014724 | 198 | 327 | 0.006460 | 🟡 high — specialist register | — |
| 236 | **king trisong detsen** | 3 | 7 | 0.827 | - | 0.004222 | - | 98 | 0.006454 | - | ~ |
| 237 | **tilopa** | 1 | 29 | - | 4,819.60 | 0.008870 | 311 | 207 | 0.006441 | 🟡 high — specialist register | ✓ ཏི་ལོ་པ |
| 238 | **noble** | 1 | 37 | - | 5,891.17 | 0.012060 | 232 | 273 | 0.006428 | 🟡 high — specialist register | ~ |
| 239 | **land** | 1 | 49 | - | 4,962.18 | 0.009148 | 301 | 214 | 0.006420 | 🟡 high — specialist register | ~ |
| 240 | **emptiness** | 1 | 38 | - | 6,315.33 | 0.014395 | 207 | 314 | 0.006419 | 🟡 high — specialist register | ✓ སྟོང་པ་ཉིད |
| 241 | **see** | 1 | 119 | - | 9,644.75 | - | 99 | - | 0.006414 | 🟡 high — specialist register | — |
| 242 | **child** | 1 | 49 | - | 7,557.52 | 0.026889 | 157 | 499 | 0.006397 | 🟡 high — specialist register | — |
| 243 | **bear** | 1 | 30 | - | 3,456.62 | 0.006929 | 459 | 167 | 0.006332 | 🟡 high — specialist register | — |
| 244 | **vast** | 1 | 40 | - | 5,301.00 | 0.010459 | 270 | 245 | 0.006309 | 🟡 high — specialist register | — |
| 245 | **get** | 1 | 111 | - | 9,604.54 | - | 102 | - | 0.006297 | 🟡 high — specialist register | — |
| 246 | **called** | 1 | 116 | - | 9,507.43 | - | 103 | - | 0.006259 | 🟡 high — specialist register | — |
| 247 | **tell** | 1 | 37 | - | 4,373.36 | 0.009061 | 343 | 212 | 0.006158 | 🟡 high — specialist register | — |
| 248 | **pain** | 1 | 40 | - | 6,014.73 | 0.014714 | 221 | 325 | 0.006156 | 🟡 high — specialist register | — |
| 249 | **jewel crest** | 2 | 7 | 0.666 | - | 0.004470 | - | 107 | 0.006112 | - | — |
| 250 | **impermanence** | 1 | 36 | - | 5,982.95 | 0.014714 | 225 | 326 | 0.006099 | 🟡 high — specialist register | — |
| 251 | **too** | 1 | 109 | - | 9,303.06 | - | 108 | - | 0.006077 | 🟡 high — specialist register | — |
| 252 | **bad** | 1 | 47 | - | 5,029.88 | 0.010992 | 292 | 251 | 0.006056 | 🟡 high — specialist register | — |
| 253 | **bhagavan buddha** | 2 | 4 | 0.497 | - | 0.004516 | - | 109 | 0.006042 | - | ~ |
| 254 | **sun** | 1 | 45 | - | 5,070.60 | 0.011250 | 287 | 258 | 0.006026 | 🟡 high — specialist register | — |
| 255 | **attain perfect buddhahood** | 3 | 6 | 0.634 | - | 0.004525 | - | 110 | 0.006007 | - | — |
| 256 | **powerful** | 1 | 42 | - | 5,306.44 | 0.012428 | 269 | 280 | 0.005981 | 🟡 high — specialist register | — |
| 257 | **concentration** | 1 | 39 | - | 5,741.13 | 0.014655 | 239 | 322 | 0.005962 | 🟡 high — specialist register | ✓ བསམ་གཏན |
| 258 | **innumerable** | 1 | 36 | - | 5,982.95 | 0.016298 | 227 | 346 | 0.005947 | 🟡 high — specialist register | — |
| 259 | **perfect teacher** | 2 | 8 | 0.353 | - | 0.004633 | - | 112 | 0.005938 | - | — |
| 260 | **know** | 1 | 78 | - | 7,898.99 | 0.061401 | 145 | 889 | 0.005932 | 🟡 high — specialist register | — |
| 261 | **attachment** | 1 | 36 | - | 5,984.90 | 0.016816 | 223 | 360 | 0.005915 | 🟡 high — specialist register | — |
| 262 | **right** | 1 | 102 | - | 9,093.84 | - | 113 | - | 0.005905 | 🟡 high — specialist register | — |
| 263 | **spiritual teacher** | 2 | 10 | 0.426 | - | 0.004746 | - | 113 | 0.005905 | - | ~ |
| 264 | **perfectly** | 1 | 38 | - | 5,404.48 | 0.013666 | 263 | 298 | 0.005889 | 🟡 high — specialist register | — |
| 265 | **moon** | 1 | 33 | - | 5,484.37 | 0.014089 | 257 | 306 | 0.005887 | 🟡 high — specialist register | — |
| 266 | **put** | 1 | 94 | - | 7,571.49 | 0.047600 | 156 | 739 | 0.005881 | 🟡 high — specialist register | — |
| 267 | **possession** | 1 | 37 | - | 6,149.14 | 0.019133 | 215 | 392 | 0.005849 | 🟡 high — specialist register | — |
| 268 | **birth** | 1 | 35 | - | 5,816.75 | 0.016746 | 235 | 353 | 0.005811 | 🟡 high — specialist register | — |
| 269 | **himself** | 1 | 67 | - | 9,058.16 | - | 116 | - | 0.005806 | 🟡 high — specialist register | — |
| 270 | **peerless teacher** | 2 | 15 | 0.594 | - | 0.004883 | - | 116 | 0.005806 | - | — |
| 271 | **future** | 1 | 52 | - | 3,988.04 | 0.009554 | 380 | 224 | 0.005794 | 🟡 high — specialist register | — |
| 272 | **fault** | 1 | 45 | - | 6,226.02 | 0.021545 | 210 | 422 | 0.005778 | 🟡 high — specialist register | — |
| 273 | **practise guru yoga** | 3 | 3 | 0.587 | - | 0.004946 | - | 117 | 0.005774 | - | — |
| 274 | **red** | 1 | 41 | - | 4,573.02 | 0.011202 | 325 | 257 | 0.005752 | 🟡 high — specialist register | — |
| 275 | **nothing** | 1 | 86 | - | 8,956.52 | - | 118 | - | 0.005742 | 🟡 high — specialist register | — |
| 276 | **result** | 1 | 55 | - | 4,077.03 | 0.009732 | 370 | 233 | 0.005739 | 🟡 high — specialist register | — |
| 277 | **listen** | 1 | 34 | - | 5,112.52 | 0.013656 | 282 | 297 | 0.005725 | 🟡 high — specialist register | — |
| 278 | **simply** | 1 | 44 | - | 4,830.54 | 0.012281 | 306 | 277 | 0.005700 | 🟡 high — specialist register | — |
| 279 | **fire** | 1 | 45 | - | 5,035.94 | 0.013418 | 290 | 292 | 0.005698 | 🟡 high — specialist register | — |
| 280 | **conqueror** | 1 | 31 | - | 5,151.98 | 0.014091 | 277 | 307 | 0.005692 | 🟡 high — specialist register | ✓ རྒྱལ་བ |
| 281 | **turn** | 1 | 47 | - | 4,965.71 | 0.012593 | 299 | 285 | 0.005684 | 🟡 high — specialist register | — |
| 282 | **worldly** | 1 | 34 | - | 5,650.56 | 0.016758 | 247 | 355 | 0.005667 | 🟡 high — specialist register | ~ |
| 283 | **obscuration** | 1 | 53 | - | 8,808.23 | - | 121 | - | 0.005649 | 🟡 high — specialist register | — |
| 284 | **rich** | 1 | 42 | - | 5,515.84 | 0.016753 | 254 | 354 | 0.005600 | 🟡 high — specialist register | — |
| 285 | **imagine** | 1 | 36 | - | 5,552.47 | 0.016814 | 252 | 359 | 0.005592 | 🟡 high — specialist register | — |
| 286 | **prostration** | 1 | 34 | - | 5,650.56 | 0.017677 | 245 | 373 | 0.005588 | 🟡 high — specialist register | ✓ ཕྱག་འཚལ་བ |
| 287 | **spiritual friend** | 2 | 34 | 0.793 | - | 0.005295 | - | 124 | 0.005559 | - | ✓ དགེ་བའི་བཤེས་གཉེན |
| 288 | **great perfection lineage** | 3 | 3 | 0.516 | - | 0.005301 | - | 125 | 0.005530 | - | ~ |
| 289 | **set** | 1 | 53 | - | 3,652.21 | 0.009643 | 433 | 229 | 0.005489 | 🟡 high — specialist register | — |
| 290 | **family** | 1 | 39 | - | 4,080.72 | 0.011289 | 369 | 259 | 0.005466 | 🟡 high — specialist register | — |
| 291 | **text** | 1 | 42 | - | 6,070.56 | 0.025275 | 219 | 479 | 0.005440 | 🟡 high — specialist register | — |
| 292 | **every** | 1 | 84 | - | 8,439.66 | - | 130 | - | 0.005388 | 🟡 high — specialist register | — |
| 293 | **teacher vajrasattva** | 2 | 3 | 0.333 | - | 0.005395 | - | 130 | 0.005388 | - | ~ |
| 294 | **confess** | 1 | 33 | - | 5,484.37 | 0.018582 | 261 | 383 | 0.005373 | 🟡 high — specialist register | — |
| 295 | **intention** | 1 | 45 | - | 4,790.68 | 0.014447 | 312 | 315 | 0.005355 | 🟡 high — specialist register | — |
| 296 | **doctrine** | 1 | 33 | - | 5,486.16 | 0.020201 | 255 | 404 | 0.005330 | 🟡 high — specialist register | — |
| 297 | **activity** | 1 | 53 | - | 5,105.74 | 0.016868 | 283 | 361 | 0.005291 | 🟡 high — specialist register | ~ |
| 298 | **start** | 1 | 48 | - | 4,018.55 | 0.012276 | 373 | 276 | 0.005286 | 🟡 high — specialist register | — |
| 299 | **emotion** | 1 | 33 | - | 5,484.37 | 0.020815 | 256 | 412 | 0.005283 | 🟡 high — specialist register | — |
| 300 | **appear** | 1 | 44 | - | 4,907.63 | 0.015622 | 304 | 339 | 0.005254 | 🟡 high — specialist register | — |
| 301 | **instant** | 1 | 33 | - | 5,254.28 | 0.019112 | 272 | 391 | 0.005229 | 🟡 high — specialist register | — |
| 302 | **work** | 1 | 48 | - | 3,980.33 | 0.012414 | 382 | 279 | 0.005212 | 🟡 high — specialist register | — |
| 303 | **dedicate** | 1 | 31 | - | 5,153.67 | 0.018971 | 276 | 388 | 0.005208 | 🟡 high — specialist register | — |
| 304 | **infinite** | 1 | 32 | - | 5,095.06 | 0.018027 | 284 | 376 | 0.005201 | 🟡 high — specialist register | ~ |
| 305 | **long time** | 2 | 8 | 0.359 | - | 0.005735 | - | 137 | 0.005201 | - | — |
| 306 | **arise** | 1 | 32 | - | 4,935.53 | 0.016540 | 303 | 349 | 0.005200 | 🟡 high — specialist register | — |
| 307 | **consciousness** | 1 | 32 | - | 5,319.91 | 0.020347 | 267 | 409 | 0.005190 | 🟡 high — specialist register | — |
| 308 | **down** | 1 | 121 | - | 8,007.22 | - | 139 | - | 0.005150 | 🟡 high — specialist register | — |
| 309 | **completely** | 1 | 38 | - | 4,556.38 | 0.015133 | 327 | 332 | 0.005135 | 🟡 high — specialist register | — |
| 310 | **complete** | 1 | 41 | - | 3,878.01 | 0.012645 | 386 | 286 | 0.005132 | 🟡 high — specialist register | — |
| 311 | **cannot** | 1 | 84 | - | 8,004.62 | - | 140 | - | 0.005124 | 🟡 high — specialist register | — |
| 312 | **wish** | 1 | 54 | - | 6,651.95 | 0.055369 | 192 | 815 | 0.005111 | 🟡 high — specialist register | ~ |
| 313 | **black** | 1 | 30 | - | 3,404.59 | 0.011003 | 466 | 252 | 0.005106 | 🟡 high — specialist register | ~ |
| 314 | **parent** | 1 | 43 | - | 4,204.24 | 0.014109 | 359 | 308 | 0.005104 | 🟡 high — specialist register | — |
| 315 | **outer** | 1 | 33 | - | 4,857.88 | 0.017520 | 305 | 370 | 0.005065 | 🟡 high — specialist register | ~ |
| 316 | **offer** | 1 | 48 | - | 3,098.78 | 0.009902 | 518 | 240 | 0.005063 | 🟡 high — specialist register | — |
| 317 | **mountain** | 1 | 37 | - | 4,707.61 | 0.016759 | 316 | 356 | 0.005063 | 🟡 high — specialist register | ~ |
| 318 | **desire** | 1 | 41 | - | 4,824.29 | 0.017616 | 307 | 371 | 0.005045 | 🟡 high — specialist register | — |
| 319 | **hear** | 1 | 34 | - | 4,766.19 | 0.017029 | 314 | 364 | 0.005032 | 🟡 high — specialist register | — |
| 320 | **finally** | 1 | 36 | - | 4,384.70 | 0.015413 | 342 | 335 | 0.005019 | 🟡 high — specialist register | — |
| 321 | **difficult** | 1 | 41 | - | 3,812.88 | 0.013406 | 401 | 291 | 0.005018 | 🟡 high — specialist register | — |
| 322 | **ground** | 1 | 37 | - | 4,297.83 | 0.014770 | 350 | 329 | 0.005010 | 🟡 high — specialist register | ~ |
| 323 | **deed** | 1 | 33 | - | 5,484.37 | 0.025390 | 258 | 480 | 0.004997 | 🟡 high — specialist register | — |
| 324 | **generation** | 1 | 35 | - | 4,977.81 | 0.019343 | 298 | 396 | 0.004986 | 🟡 high — specialist register | ~ |
| 325 | **away** | 1 | 78 | - | 7,852.10 | - | 147 | - | 0.004955 | 🟡 high — specialist register | — |
| 326 | **evil action** | 2 | 10 | 0.414 | - | 0.006054 | - | 147 | 0.004955 | - | — |
| 327 | **understand** | 1 | 35 | - | 4,453.15 | 0.016552 | 338 | 351 | 0.004946 | 🟡 high — specialist register | — |
| 328 | **syllable mantra** | 2 | 9 | 0.669 | - | 0.006142 | - | 148 | 0.004932 | - | — |
| 329 | **sangha** | 1 | 22 | - | 3,656.25 | 0.012816 | 428 | 289 | 0.004915 | 🟡 high — specialist register | ✓ དགེ་འདུན |
| 330 | **whole** | 1 | 78 | - | 7,748.64 | - | 149 | - | 0.004909 | 🟡 high — specialist register | — |
| 331 | **become** | 1 | 89 | - | 7,700.94 | - | 150 | - | 0.004886 | 🟡 high — specialist register | — |
| 332 | **cho** | 1 | 21 | - | 3,490.05 | 0.012481 | 453 | 283 | 0.004865 | 🟡 high — specialist register | ✓ གཅོད |
| 333 | **someone** | 1 | 60 | - | 7,690.19 | - | 151 | - | 0.004864 | 🟡 high — specialist register | — |
| 334 | **buddha kasyapa** | 2 | 3 | 0.560 | - | 0.006191 | - | 151 | 0.004864 | - | — |
| 335 | **look** | 1 | 70 | - | 6,903.88 | 0.108107 | 184 | 1,273 | 0.004849 | 🟡 high — specialist register | — |
| 336 | **syllable** | 1 | 30 | - | 4,985.79 | 0.022176 | 297 | 432 | 0.004834 | 🟡 high — specialist register | — |
| 337 | **brahmin** | 1 | 31 | - | 5,151.98 | 0.025005 | 279 | 471 | 0.004833 | 🟡 high — specialist register | ✓ བྲམ་ཟེ |
| 338 | **tradition** | 1 | 30 | - | 4,987.42 | 0.022832 | 294 | 439 | 0.004829 | 🟡 high — specialist register | ~ |
| 339 | **pile** | 1 | 33 | - | 5,089.76 | 0.024563 | 285 | 466 | 0.004800 | 🟡 high — specialist register | — |
| 340 | **flower** | 1 | 30 | - | 4,987.42 | 0.023753 | 293 | 451 | 0.004790 | 🟡 high — specialist register | — |
| 341 | **perception** | 1 | 39 | - | 5,121.85 | 0.025616 | 281 | 484 | 0.004771 | 🟡 high — specialist register | ~ |
| 342 | **sarhsara** | 1 | 29 | - | 4,819.60 | 0.021937 | 308 | 427 | 0.004771 | 🟡 high — specialist register | — |
| 343 | **white** | 1 | 40 | - | 3,730.08 | 0.014553 | 415 | 317 | 0.004758 | 🟡 high — specialist register | ~ |
| 344 | **lead** | 1 | 44 | - | 3,748.24 | 0.014612 | 411 | 320 | 0.004755 | 🟡 high — specialist register | — |
| 345 | **jetsun milarepa** | 2 | 10 | 0.793 | - | 0.006429 | - | 156 | 0.004754 | - | ~ |
| 346 | **glorious root teacher** | 3 | 4 | 0.589 | - | 0.006506 | - | 157 | 0.004733 | - | ~ |
| 347 | **purify** | 1 | 30 | - | 4,985.79 | 0.024450 | 296 | 462 | 0.004725 | 🟡 high — specialist register | — |
| 348 | **good kalpa** | 2 | 7 | 0.421 | - | 0.006532 | - | 158 | 0.004712 | - | ✓ བསྐལ་པ་བཟང་པོ |
| 349 | **enlightenment** | 1 | 28 | - | 4,653.40 | 0.021734 | 319 | 424 | 0.004705 | 🟡 high — specialist register | ✓ བྱང་ཆུབ |
| 350 | **drink** | 1 | 31 | - | 4,480.65 | 0.019935 | 335 | 401 | 0.004701 | 🟡 high — specialist register | — |
| 351 | **mantrayana** | 1 | 20 | - | 3,323.86 | 0.013427 | 477 | 293 | 0.004695 | 🟡 high — specialist register | ~ |
| 352 | **therefore** | 1 | 69 | - | 7,444.59 | - | 159 | - | 0.004691 | 🟡 high — specialist register | — |
| 353 | **king songtsen gampo** | 3 | 4 | 0.790 | - | 0.006571 | - | 159 | 0.004691 | - | ~ |
| 354 | **accumulation** | 1 | 36 | - | 5,203.34 | 0.031204 | 275 | 538 | 0.004657 | 🟡 high — specialist register | — |
| 355 | **taught** | 1 | 48 | - | 7,403.29 | - | 161 | - | 0.004649 | 🟡 high — specialist register | — |
| 356 | **buddhafield** | 1 | 23 | - | 3,822.44 | 0.016543 | 394 | 350 | 0.004642 | 🟡 high — specialist register | — |
| 357 | **dharma properly** | 2 | 3 | 0.363 | - | 0.006697 | - | 162 | 0.004629 | - | — |
| 358 | **universe** | 1 | 27 | - | 4,488.68 | 0.021814 | 331 | 426 | 0.004615 | 🟡 high — specialist register | ~ |
| 359 | **earth** | 1 | 30 | - | 4,416.26 | 0.020869 | 340 | 413 | 0.004614 | 🟡 high — specialist register | — |
| 360 | **doing** | 1 | 69 | - | 7,384.29 | - | 163 | - | 0.004609 | 🟡 high — specialist register | — |
| 361 | **ocean** | 1 | 35 | - | 4,337.27 | 0.020313 | 345 | 408 | 0.004606 | 🟡 high — specialist register | — |
| 362 | **woman** | 1 | 31 | - | 5,151.98 | 0.031718 | 278 | 549 | 0.004601 | 🟡 high — specialist register | — |
| 363 | **circumstance** | 1 | 29 | - | 4,617.40 | 0.023478 | 322 | 449 | 0.004582 | 🟡 high — specialist register | — |
| 364 | **natural** | 1 | 38 | - | 3,339.65 | 0.014368 | 471 | 312 | 0.004571 | 🟡 high — specialist register | ~ |
| 365 | **face** | 1 | 39 | - | 3,781.41 | 0.016767 | 404 | 357 | 0.004553 | 🟡 high — specialist register | — |
| 366 | **ever** | 1 | 64 | - | 7,289.85 | - | 166 | - | 0.004549 | 🟡 high — specialist register | — |
| 367 | **precious jewel** | 2 | 7 | 0.489 | - | 0.006924 | - | 166 | 0.004549 | - | ~ |
| 368 | **off** | 1 | 96 | - | 7,270.34 | - | 167 | - | 0.004530 | 🟡 high — specialist register | — |
| 369 | **develop** | 1 | 38 | - | 3,995.17 | 0.019079 | 376 | 390 | 0.004516 | 🟡 high — specialist register | — |
| 370 | **essential** | 1 | 32 | - | 3,876.58 | 0.018187 | 388 | 378 | 0.004515 | 🟡 high — specialist register | ~ |
| 371 | **old** | 1 | 69 | - | 7,202.77 | - | 168 | - | 0.004510 | 🟡 high — specialist register | — |
| 372 | **fact** | 1 | 36 | - | 3,624.05 | 0.016068 | 436 | 342 | 0.004504 | 🟡 high — specialist register | — |
| 373 | **recitation** | 1 | 29 | - | 4,819.60 | 0.026832 | 310 | 496 | 0.004501 | 🟡 high — specialist register | ~ |
| 374 | **cause** | 1 | 60 | - | 5,700.40 | 0.051129 | 242 | 781 | 0.004500 | 🟡 high — specialist register | ~ |
| 375 | **patience** | 1 | 28 | - | 4,458.18 | 0.023240 | 337 | 445 | 0.004499 | 🟡 high — specialist register | — |
| 376 | **avoid** | 1 | 35 | - | 3,573.65 | 0.015771 | 440 | 341 | 0.004494 | 🟡 high — specialist register | — |
| 377 | **hum** | 1 | 24 | - | 3,533.01 | 0.016186 | 443 | 343 | 0.004469 | 🟡 high — specialist register | — |
| 378 | **real** | 1 | 39 | - | 3,186.10 | 0.014550 | 495 | 316 | 0.004461 | 🟡 high — specialist register | ~ |
| 379 | **sheep** | 1 | 28 | - | 4,318.59 | 0.022770 | 349 | 437 | 0.004457 | 🟡 high — specialist register | — |
| 380 | **practising** | 1 | 43 | - | 7,148.63 | - | 171 | - | 0.004453 | 🟡 high — specialist register | — |
| 381 | **dead** | 1 | 31 | - | 4,003.97 | 0.020268 | 375 | 406 | 0.004445 | 🟡 high — specialist register | — |
| 382 | **foot** | 1 | 37 | - | 4,707.61 | 0.027007 | 317 | 500 | 0.004438 | 🟡 high — specialist register | — |
| 383 | **dagpo rinpoche** | 2 | 10 | 0.845 | - | 0.006992 | - | 172 | 0.004435 | - | ~ |
| 384 | **sadaprarudita** | 1 | 20 | - | 3,323.86 | 0.015007 | 484 | 330 | 0.004402 | 🟡 high — specialist register | ✓ རྟག་ཏུ་ངུ |
| 385 | **dorje** | 1 | 19 | - | 3,157.67 | 0.014663 | 506 | 323 | 0.004378 | 🟡 high — specialist register | ~ |
| 386 | **dharmodgata** | 1 | 19 | - | 3,157.67 | 0.014680 | 513 | 324 | 0.004349 | 🟡 high — specialist register | ✓ ཆོས་འཕགས |
| 387 | **negative emotion** | 2 | 24 | 0.736 | - | 0.007189 | - | 177 | 0.004344 | - | — |
| 388 | **jowo** | 1 | 19 | - | 3,157.67 | 0.014742 | 507 | 328 | 0.004341 | 🟡 high — specialist register | ✓ ཇོ་བོ |
| 389 | **ultimate** | 1 | 26 | - | 3,479.04 | 0.016805 | 455 | 358 | 0.004334 | 🟡 high — specialist register | — |
| 390 | **story** | 1 | 34 | - | 4,465.20 | 0.026800 | 336 | 495 | 0.004327 | 🟡 high — specialist register | — |
| 391 | **sublime teacher** | 2 | 7 | 0.426 | - | 0.007414 | - | 178 | 0.004326 | - | ~ |
| 392 | **small** | 1 | 37 | - | 3,185.60 | 0.015592 | 496 | 338 | 0.004311 | 🟡 high — specialist register | ~ |
| 393 | **mantra vajrayana** | 2 | 11 | 0.787 | - | 0.007475 | - | 179 | 0.004308 | - | ~ |
| 394 | **space** | 1 | 31 | - | 3,796.78 | 0.020275 | 402 | 407 | 0.004306 | 🟡 high — specialist register | ~ |
| 395 | **palace** | 1 | 25 | - | 3,759.20 | 0.020211 | 406 | 405 | 0.004296 | 🟡 high — specialist register | ~ |
| 396 | **meaning** | 1 | 54 | - | 7,031.39 | - | 180 | - | 0.004291 | 🟡 high — specialist register | ~ |
| 397 | **absolute** | 1 | 28 | - | 3,827.72 | 0.021793 | 391 | 425 | 0.004279 | 🟡 high — specialist register | ~ |
| 398 | **attain buddhahood** | 2 | 9 | 0.615 | - | 0.007556 | - | 181 | 0.004274 | - | — |
| 399 | **stay** | 1 | 34 | - | 3,658.28 | 0.019294 | 424 | 394 | 0.004269 | 🟡 high — specialist register | — |
| 400 | **heaven** | 1 | 23 | - | 3,822.44 | 0.022020 | 395 | 428 | 0.004247 | 🟡 high — specialist register | ~ |
| 401 | **companion** | 1 | 29 | - | 4,617.40 | 0.031766 | 323 | 552 | 0.004245 | 🟡 high — specialist register | — |
| 402 | **until** | 1 | 92 | - | 6,941.83 | - | 183 | - | 0.004240 | 🟡 high — specialist register | — |
| 403 | **truth** | 1 | 26 | - | 4,322.43 | 0.027735 | 346 | 505 | 0.004233 | 🟡 high — specialist register | ~ |
| 404 | **sign** | 1 | 41 | - | 4,269.97 | 0.026770 | 353 | 494 | 0.004226 | 🟡 high — specialist register | ~ |
| 405 | **great kalpa** | 2 | 4 | 0.314 | - | 0.007840 | - | 184 | 0.004223 | - | ~ |
| 406 | **asked** | 1 | 90 | - | 6,897.94 | - | 185 | - | 0.004206 | 🟡 high — specialist register | — |
| 407 | **confession** | 1 | 23 | - | 3,822.44 | 0.022968 | 398 | 441 | 0.004179 | 🟡 high — specialist register | — |
| 408 | **karmic** | 1 | 25 | - | 4,154.82 | 0.026576 | 362 | 493 | 0.004178 | 🟡 high — specialist register | ~ |
| 409 | **present life** | 2 | 9 | 0.444 | - | 0.007945 | - | 187 | 0.004173 | - | — |
| 410 | **arouse** | 1 | 24 | - | 3,988.63 | 0.025049 | 377 | 473 | 0.004165 | 🟡 high — specialist register | — |
| 411 | **want** | 1 | 69 | - | 6,103.74 | 0.182370 | 217 | 1,754 | 0.004161 | 🟡 high — specialist register | — |
| 412 | **generosity** | 1 | 25 | - | 4,154.82 | 0.027012 | 363 | 501 | 0.004147 | 🟡 high — specialist register | ✓ སྦྱིན་པ |
| 413 | **happy** | 1 | 30 | - | 3,653.92 | 0.020960 | 432 | 414 | 0.004142 | 🟡 high — specialist register | — |
| 414 | **killing** | 1 | 44 | - | 6,786.35 | - | 189 | - | 0.004140 | 🟡 high — specialist register | — |
| 415 | **peerless** | 1 | 26 | - | 4,010.12 | 0.025641 | 374 | 485 | 0.004139 | 🟡 high — specialist register | — |
| 416 | **hard** | 1 | 34 | - | 3,270.19 | 0.017718 | 488 | 374 | 0.004129 | 🟡 high — specialist register | — |
| 417 | **attitude** | 1 | 32 | - | 3,876.58 | 0.024745 | 387 | 469 | 0.004127 | 🟡 high — specialist register | — |
| 418 | **element** | 1 | 33 | - | 4,296.96 | 0.030317 | 351 | 531 | 0.004125 | 🟡 high — specialist register | — |
| 419 | **tonpa** | 1 | 18 | - | 2,991.47 | 0.016266 | 546 | 345 | 0.004119 | 🟢 medium — moderately distinctive | ~ |
| 420 | **cut** | 1 | 38 | - | 2,634.32 | 0.014595 | 620 | 318 | 0.004116 | 🟢 medium — moderately distinctive | — |
| 421 | **level** | 1 | 48 | - | 3,476.44 | 0.019930 | 456 | 400 | 0.004112 | 🟡 high — specialist register | ~ |
| 422 | **padampa sangye** | 2 | 16 | 0.993 | - | 0.008057 | - | 191 | 0.004108 | - | ✓ ཕ་དམ་པ་སངས་རྒྱས |
| 423 | **perform** | 1 | 26 | - | 3,757.97 | 0.023935 | 407 | 453 | 0.004091 | 🟡 high — specialist register | — |
| 424 | **river** | 1 | 31 | - | 3,335.49 | 0.019161 | 472 | 393 | 0.004087 | 🟡 high — specialist register | — |
| 425 | **fruit** | 1 | 30 | - | 3,816.98 | 0.024469 | 400 | 463 | 0.004086 | 🟡 high — specialist register | ~ |
| 426 | **realize** | 1 | 24 | - | 3,076.08 | 0.016976 | 523 | 362 | 0.004085 | 🟡 high — specialist register | — |
| 427 | **perfection phase** | 2 | 5 | 0.650 | - | 0.008196 | - | 193 | 0.004077 | - | ✓ རྫོགས་རིམ |
| 428 | **immense** | 1 | 25 | - | 3,980.52 | 0.026834 | 381 | 497 | 0.004063 | 🟡 high — specialist register | — |
| 429 | **depth** | 1 | 34 | - | 4,056.79 | 0.028599 | 371 | 515 | 0.004059 | 🟡 high — specialist register | — |
| 430 | **practitioner** | 1 | 27 | - | 4,487.21 | 0.035984 | 333 | 607 | 0.004044 | 🟡 high — specialist register | ~ |
| 431 | **reply** | 1 | 1 | - | 120.51 | 0.008506 | 7,423 | 196 | 0.004040 | 🔵 low — common in general English | — |
| 432 | **beautiful** | 1 | 24 | - | 3,988.63 | 0.028217 | 379 | 511 | 0.004029 | 🟡 high — specialist register | — |
| 433 | **source** | 1 | 37 | - | 3,599.37 | 0.022493 | 438 | 435 | 0.004028 | 🟡 high — specialist register | ~ |
| 434 | **nagarjuna** | 1 | 18 | - | 2,991.47 | 0.017060 | 540 | 365 | 0.004020 | 🟢 medium — moderately distinctive | ✓ ཀླུ་སྒྲུབ |
| 435 | **natural state** | 2 | 25 | 0.776 | - | 0.008517 | - | 197 | 0.004015 | - | ✓ གནས་ལུགས |
| 436 | **clothing** | 1 | 28 | - | 3,677.22 | 0.024323 | 420 | 460 | 0.004006 | 🟡 high — specialist register | — |
| 437 | **indra** | 1 | 18 | - | 2,991.47 | 0.017403 | 542 | 367 | 0.004003 | 🟢 medium — moderately distinctive | ✓ བརྒྱ་བྱིན |
| 438 | **sangye** | 1 | 17 | - | 2,825.28 | 0.016729 | 575 | 352 | 0.004002 | 🟢 medium — moderately distinctive | ~ |
| 439 | **rest** | 1 | 32 | - | 3,077.82 | 0.018300 | 522 | 380 | 0.003991 | 🟡 high — specialist register | — |
| 440 | **diligence** | 1 | 28 | - | 3,616.49 | 0.023244 | 437 | 446 | 0.003988 | 🟡 high — specialist register | — |
| 441 | **replied** | 1 | 56 | - | 6,452.36 | - | 199 | - | 0.003985 | 🟡 high — specialist register | — |
| 442 | **past negative** | 2 | 8 | 0.389 | - | 0.008528 | - | 199 | 0.003985 | - | — |
| 443 | **matter** | 1 | 31 | - | 3,251.38 | 0.020052 | 491 | 403 | 0.003975 | 🟡 high — specialist register | — |
| 444 | **best** | 1 | 68 | - | 6,431.82 | - | 200 | - | 0.003971 | 🟡 high — specialist register | — |
| 445 | **main practice** | 2 | 16 | 0.625 | - | 0.008529 | - | 200 | 0.003971 | - | — |
| 446 | **dissolve** | 1 | 28 | - | 4,653.40 | 0.043423 | 320 | 687 | 0.003970 | 🟡 high — specialist register | — |
| 447 | **anything** | 1 | 61 | - | 6,413.30 | - | 201 | - | 0.003956 | 🟡 high — specialist register | — |
| 448 | **kind teacher** | 2 | 5 | 0.302 | - | 0.008532 | - | 201 | 0.003956 | - | — |
| 449 | **age** | 1 | 26 | - | 3,757.97 | 0.026551 | 408 | 492 | 0.003948 | 🟡 high — specialist register | ~ |
| 450 | **middle** | 1 | 29 | - | 3,006.45 | 0.018845 | 533 | 387 | 0.003923 | 🟡 high — specialist register | ~ |
| 451 | **sleep** | 1 | 23 | - | 3,823.69 | 0.029802 | 393 | 528 | 0.003908 | 🟡 high — specialist register | — |
| 452 | **mount** | 1 | 19 | - | 2,568.73 | 0.016530 | 631 | 348 | 0.003898 | 🟢 medium — moderately distinctive | ~ |
| 453 | **myself** | 1 | 38 | - | 6,317.40 | - | 205 | - | 0.003898 | 🟡 high — specialist register | — |
| 454 | **king trisong** | 2 | 7 | 0.680 | - | 0.008689 | - | 205 | 0.003898 | - | ~ |
| 455 | **cold** | 1 | 29 | - | 3,234.57 | 0.021393 | 492 | 420 | 0.003895 | 🟡 high — specialist register | — |
| 456 | **intermediate** | 1 | 30 | - | 3,202.11 | 0.021135 | 494 | 419 | 0.003893 | 🟡 high — specialist register | ~ |
| 457 | **creature** | 1 | 25 | - | 4,154.82 | 0.034890 | 365 | 592 | 0.003887 | 🟡 high — specialist register | — |
| 458 | **clear** | 1 | 28 | - | 2,697.37 | 0.016996 | 597 | 363 | 0.003886 | 🟢 medium — moderately distinctive | ~ |
| 459 | **great bliss** | 2 | 7 | 0.540 | - | 0.008853 | - | 206 | 0.003884 | - | ~ |
| 460 | **numerous** | 1 | 26 | - | 3,644.73 | 0.025249 | 435 | 478 | 0.003879 | 🟡 high — specialist register | — |
| 461 | **train** | 1 | 24 | - | 3,413.35 | 0.023907 | 464 | 452 | 0.003862 | 🟡 high — specialist register | — |
| 462 | **night** | 1 | 31 | - | 3,079.59 | 0.020479 | 521 | 410 | 0.003849 | 🟡 high — specialist register | — |
| 463 | **remember** | 1 | 24 | - | 3,701.64 | 0.028347 | 416 | 513 | 0.003846 | 🟡 high — specialist register | — |
| 464 | **dedication** | 1 | 23 | - | 3,822.44 | 0.031656 | 397 | 548 | 0.003833 | 🟡 high — specialist register | — |
| 465 | **sort** | 1 | 31 | - | 3,735.90 | 0.029553 | 414 | 526 | 0.003816 | 🟡 high — specialist register | — |
| 466 | **while** | 1 | 98 | - | 6,199.45 | - | 211 | - | 0.003814 | 🟡 high — specialist register | — |
| 467 | **true jewel** | 2 | 4 | 0.384 | - | 0.009018 | - | 211 | 0.003814 | - | ~ |
| 468 | **receive** | 1 | 24 | - | 2,080.86 | 0.014649 | 784 | 321 | 0.003810 | 🟢 medium — moderately distinctive | — |
| 469 | **torment** | 1 | 24 | - | 3,988.63 | 0.035549 | 378 | 600 | 0.003798 | 🟡 high — specialist register | — |
| 470 | **because** | 1 | 99 | - | 6,177.07 | - | 213 | - | 0.003787 | 🟡 high — specialist register | — |
| 471 | **inconceivable** | 1 | 23 | - | 3,662.08 | 0.029979 | 422 | 530 | 0.003770 | 🟡 high — specialist register | — |
| 472 | **existence** | 1 | 26 | - | 3,445.65 | 0.025498 | 460 | 483 | 0.003765 | 🟡 high — specialist register | ~ |
| 473 | **begin** | 1 | 12 | - | 1,117.49 | 0.011577 | 1,359 | 267 | 0.003763 | 🟢 medium — moderately distinctive | — |
| 474 | **rigdzin jigme lingpa** | 3 | 10 | 0.976 | - | 0.009199 | - | 215 | 0.003761 | - | — |
| 475 | **karma** | 1 | 22 | - | 3,656.25 | 0.029452 | 430 | 522 | 0.003759 | 🟡 high — specialist register | ✓ ལས |
| 476 | **killed** | 1 | 51 | - | 6,146.16 | - | 216 | - | 0.003748 | 🟡 high — specialist register | — |
| 477 | **guru rinpoche** | 2 | 4 | 0.575 | - | 0.009262 | - | 216 | 0.003748 | - | ✓ གུ་རུ་རིན་པོ་ཆེ |
| 478 | **sakyamuni** | 1 | 16 | - | 2,659.09 | 0.018695 | 610 | 385 | 0.003740 | 🟢 medium — moderately distinctive | — |
| 479 | **peerless dagpo rinpoche** | 3 | 7 | 0.822 | - | 0.009321 | - | 217 | 0.003735 | - | — |
| 480 | **brahma** | 1 | 16 | - | 2,659.09 | 0.018823 | 611 | 386 | 0.003732 | 🟢 medium — moderately distinctive | ✓ ཚངས་པ |
| 481 | **accumulate** | 1 | 21 | - | 3,343.63 | 0.025488 | 470 | 482 | 0.003732 | 🟡 high — specialist register | — |
| 482 | **left** | 1 | 64 | - | 6,080.42 | - | 218 | - | 0.003722 | 🟡 high — specialist register | — |
| 483 | **determination** | 1 | 27 | - | 3,176.97 | 0.024144 | 500 | 457 | 0.003720 | 🟡 high — specialist register | ~ |
| 484 | **ritual** | 1 | 26 | - | 4,321.02 | 0.047544 | 348 | 735 | 0.003709 | 🟡 high — specialist register | — |
| 485 | **great ocean** | 2 | 11 | 0.531 | - | 0.009409 | - | 219 | 0.003709 | - | — |
| 486 | **skilful** | 1 | 22 | - | 3,656.25 | 0.031629 | 426 | 546 | 0.003708 | 🟡 high — specialist register | ~ |
| 487 | **went** | 1 | 61 | - | 6,059.83 | - | 220 | - | 0.003696 | 🟡 high — specialist register | — |
| 488 | **kindness** | 1 | 22 | - | 3,657.44 | 0.031803 | 425 | 553 | 0.003693 | 🟡 high — specialist register | — |
| 489 | **care** | 1 | 28 | - | 3,073.98 | 0.023952 | 524 | 454 | 0.003658 | 🟡 high — specialist register | — |
| 490 | **nanda** | 1 | 17 | - | 2,825.28 | 0.021122 | 579 | 418 | 0.003657 | 🟢 medium — moderately distinctive | ✓ དགའ་བོ |
| 491 | **together** | 1 | 61 | - | 5,984.68 | - | 224 | - | 0.003646 | 🟡 high — specialist register | — |
| 492 | **lotus** | 1 | 19 | - | 3,025.19 | 0.024074 | 527 | 455 | 0.003645 | 🟡 high — specialist register | ~ |
| 493 | **jowo rinpoche** | 2 | 6 | 0.712 | - | 0.009561 | - | 226 | 0.003621 | - | ✓ ཇོ་བོ་རིན་པོ་ཆེ |
| 494 | **vajra master** | 2 | 4 | 0.442 | - | 0.009585 | - | 227 | 0.003609 | - | ✓ རྡོ་རྗེ་སློབ་དཔོན |
| 495 | **lack** | 1 | 28 | - | 3,004.55 | 0.024331 | 534 | 461 | 0.003603 | 🟡 high — specialist register | — |
| 496 | **main** | 1 | 31 | - | 2,555.50 | 0.020049 | 636 | 402 | 0.003601 | 🟢 medium — moderately distinctive | ~ |
| 497 | **dust** | 1 | 22 | - | 3,502.85 | 0.031956 | 447 | 555 | 0.003598 | 🟡 high — specialist register | — |
| 498 | **direction** | 1 | 33 | - | 3,504.16 | 0.032058 | 445 | 558 | 0.003598 | 🟡 high — specialist register | — |
| 499 | **entire** | 1 | 28 | - | 2,877.24 | 0.023117 | 563 | 444 | 0.003589 | 🟢 medium — moderately distinctive | — |
| 500 | **came** | 1 | 64 | - | 5,976.37 | - | 229 | - | 0.003585 | 🟡 high — specialist register | — |
| 501 | **stone** | 1 | 28 | - | 3,873.97 | 0.042975 | 389 | 681 | 0.003577 | 🟡 high — specialist register | — |
| 502 | **much** | 1 | 80 | - | 5,964.71 | - | 230 | - | 0.003573 | 🟡 high — specialist register | — |
| 503 | **really** | 1 | 56 | - | 5,946.46 | - | 231 | - | 0.003561 | 🟡 high — specialist register | — |
| 504 | **central** | 1 | 32 | - | 2,237.28 | 0.018204 | 723 | 379 | 0.003555 | 🟢 medium — moderately distinctive | ~ |
| 505 | **siddha** | 1 | 23 | - | 3,822.44 | 0.042659 | 396 | 679 | 0.003546 | 🟡 high — specialist register | ✓ གྲུབ་ཐོབ |
| 506 | **object** | 1 | 27 | - | 3,784.91 | 0.041215 | 403 | 663 | 0.003543 | 🟡 high — specialist register | ~ |
| 507 | **anyone** | 1 | 44 | - | 5,831.10 | - | 233 | - | 0.003537 | 🟡 high — specialist register | — |
| 508 | **guide** | 1 | 27 | - | 3,545.89 | 0.034420 | 442 | 589 | 0.003533 | 🟡 high — specialist register | — |
| 509 | **mental** | 1 | 21 | - | 3,491.19 | 0.033584 | 449 | 579 | 0.003530 | 🟡 high — specialist register | — |
| 510 | **great river** | 2 | 5 | 0.423 | - | 0.009848 | - | 235 | 0.003514 | - | — |
| 511 | **dharmakaya** | 1 | 21 | - | 3,490.05 | 0.033994 | 450 | 587 | 0.003506 | 🟡 high — specialist register | ✓ ཆོས་སྐུ |
| 512 | **wisdom mind** | 2 | 5 | 0.307 | - | 0.009857 | - | 236 | 0.003503 | - | ~ |
| 513 | **mount meru** | 2 | 12 | 0.950 | - | 0.009863 | - | 237 | 0.003491 | - | ~ |
| 514 | **happen** | 1 | 31 | - | 3,557.89 | 0.036582 | 441 | 611 | 0.003486 | 🟡 high — specialist register | — |
| 515 | **mantra vehicle** | 2 | 6 | 0.551 | - | 0.009864 | - | 238 | 0.003480 | - | ~ |
| 516 | **lifetime** | 1 | 24 | - | 3,468.89 | 0.033975 | 458 | 586 | 0.003478 | 🟡 high — specialist register | — |
| 517 | **respect** | 1 | 27 | - | 3,098.81 | 0.028454 | 517 | 514 | 0.003475 | 🟡 high — specialist register | — |
| 518 | **clothe** | 1 | 21 | - | 3,490.05 | 0.035428 | 452 | 598 | 0.003473 | 🟡 high — specialist register | — |
| 519 | **ten** | 1 | 49 | - | 5,230.11 | 0.253065 | 273 | 2,091 | 0.003468 | 🟡 high — specialist register | ~ |
| 520 | **continent** | 1 | 24 | - | 3,413.35 | 0.033842 | 463 | 583 | 0.003467 | 🟡 high — specialist register | — |
| 521 | **number** | 1 | 31 | - | 2,465.42 | 0.021470 | 664 | 421 | 0.003460 | 🟢 medium — moderately distinctive | — |
| 522 | **amitabha** | 1 | 15 | - | 2,492.89 | 0.022023 | 648 | 429 | 0.003457 | 🟢 medium — moderately distinctive | ✓ འོད་དཔག་མེད |
| 523 | **suddenly** | 1 | 23 | - | 3,109.52 | 0.029485 | 515 | 524 | 0.003451 | 🟡 high — specialist register | — |
| 524 | **pleasure** | 1 | 23 | - | 3,823.69 | 0.048506 | 392 | 753 | 0.003442 | 🟡 high — specialist register | — |
| 525 | **omniscient** | 1 | 16 | - | 2,659.09 | 0.024140 | 606 | 456 | 0.003439 | 🟢 medium — moderately distinctive | ~ |
| 526 | **milarepa** | 1 | 15 | - | 2,492.89 | 0.022093 | 654 | 431 | 0.003437 | 🟢 medium — moderately distinctive | ~ |
| 527 | **similar** | 1 | 28 | - | 2,537.80 | 0.022808 | 640 | 438 | 0.003437 | 🟢 medium — moderately distinctive | — |
| 528 | **visualization** | 1 | 21 | - | 3,490.05 | 0.037560 | 451 | 618 | 0.003432 | 🟡 high — specialist register | — |
| 529 | **need** | 1 | 62 | - | 5,065.09 | 0.182428 | 288 | 1,761 | 0.003423 | 🟡 high — specialist register | — |
| 530 | **hold** | 1 | 34 | - | 2,877.49 | 0.026270 | 562 | 491 | 0.003423 | 🟢 medium — moderately distinctive | — |
| 531 | **keep** | 1 | 44 | - | 3,913.97 | 0.051802 | 385 | 793 | 0.003420 | 🟡 high — specialist register | — |
| 532 | **concept** | 1 | 24 | - | 3,180.60 | 0.032692 | 498 | 563 | 0.003397 | 🟡 high — specialist register | ~ |
| 533 | **jewel family** | 2 | 3 | 0.405 | - | 0.010464 | - | 246 | 0.003392 | - | — |
| 534 | **high** | 1 | 29 | - | 2,101.47 | 0.019297 | 781 | 395 | 0.003387 | 🟢 medium — moderately distinctive | — |
| 535 | **beggar** | 1 | 22 | - | 3,656.25 | 0.043268 | 431 | 683 | 0.003383 | 🟡 high — specialist register | — |
| 536 | **impermanent** | 1 | 20 | - | 3,323.86 | 0.034895 | 482 | 593 | 0.003376 | 🟡 high — specialist register | — |
| 537 | **learn** | 1 | 21 | - | 2,905.48 | 0.028215 | 558 | 510 | 0.003373 | 🟢 medium — moderately distinctive | — |
| 538 | **material** | 1 | 26 | - | 2,740.21 | 0.025889 | 588 | 487 | 0.003371 | 🟢 medium — moderately distinctive | — |
| 539 | **said** | 1 | 222 | - | 5,631.61 | - | 248 | - | 0.003371 | 🟡 high — specialist register | — |
| 540 | **padampa** | 1 | 16 | - | 2,659.09 | 0.025096 | 608 | 475 | 0.003366 | 🟢 medium — moderately distinctive | ~ |
| 541 | **living** | 1 | 49 | - | 5,623.76 | - | 249 | - | 0.003361 | 🟡 high — specialist register | — |
| 542 | **authentic teacher** | 2 | 6 | 0.401 | - | 0.010700 | - | 249 | 0.003361 | - | — |
| 543 | **glorious** | 1 | 17 | - | 2,825.28 | 0.027039 | 574 | 502 | 0.003357 | 🟢 medium — moderately distinctive | ~ |
| 544 | **done** | 1 | 57 | - | 5,621.73 | - | 250 | - | 0.003350 | 🟡 high — specialist register | — |
| 545 | **wrong view** | 2 | 20 | 0.716 | - | 0.010834 | - | 250 | 0.003350 | - | ✓ ལོག་ལྟ |
| 546 | **piece** | 1 | 24 | - | 3,821.30 | 0.052179 | 399 | 797 | 0.003346 | 🟡 high — specialist register | — |
| 547 | **thinking** | 1 | 43 | - | 5,599.07 | - | 251 | - | 0.003340 | 🟡 high — specialist register | — |
| 548 | **reason** | 1 | 28 | - | 2,644.53 | 0.025140 | 618 | 477 | 0.003337 | 🟢 medium — moderately distinctive | — |
| 549 | **idea** | 1 | 26 | - | 2,929.68 | 0.029889 | 554 | 529 | 0.003326 | 🟢 medium — moderately distinctive | — |
| 550 | **giving** | 1 | 56 | - | 5,542.91 | - | 253 | - | 0.003319 | 🟡 high — specialist register | — |
| 551 | **intermediate state** | 2 | 23 | 0.786 | - | 0.011133 | - | 254 | 0.003309 | - | ✓ བར་དོ |
| 552 | **fall** | 1 | 32 | - | 2,233.02 | 0.022403 | 724 | 434 | 0.003300 | 🟢 medium — moderately distinctive | — |
| 553 | **constantly** | 1 | 20 | - | 3,184.41 | 0.035943 | 497 | 606 | 0.003297 | 🟡 high — specialist register | — |
| 554 | **fish** | 1 | 23 | - | 2,947.91 | 0.031524 | 551 | 543 | 0.003295 | 🟢 medium — moderately distinctive | — |
| 555 | **support** | 1 | 29 | - | 2,314.87 | 0.023100 | 708 | 443 | 0.003290 | 🟢 medium — moderately distinctive | — |
| 556 | **vajrayana** | 1 | 14 | - | 2,326.70 | 0.023273 | 701 | 448 | 0.003283 | 🟢 medium — moderately distinctive | ✓ རྡོ་རྗེ་ཐེག་པ |
| 557 | **bless** | 1 | 19 | - | 3,157.67 | 0.035531 | 508 | 599 | 0.003278 | 🟡 high — specialist register | — |
| 558 | **obstacle** | 1 | 24 | - | 3,533.01 | 0.045656 | 444 | 713 | 0.003278 | 🟡 high — specialist register | — |
| 559 | **base** | 1 | 22 | - | 1,870.59 | 0.019476 | 860 | 398 | 0.003270 | 🟢 medium — moderately distinctive | — |
| 560 | **young** | 1 | 22 | - | 2,915.55 | 0.031654 | 557 | 547 | 0.003268 | 🟢 medium — moderately distinctive | — |
| 561 | **higher** | 1 | 30 | - | 2,018.60 | 0.020978 | 801 | 415 | 0.003267 | 🟢 medium — moderately distinctive | — |
| 562 | **rain** | 1 | 25 | - | 2,826.96 | 0.030426 | 573 | 533 | 0.003266 | 🟢 medium — moderately distinctive | — |
| 563 | **lake** | 1 | 21 | - | 2,419.64 | 0.024613 | 671 | 467 | 0.003266 | 🟢 medium — moderately distinctive | — |
| 564 | **iron** | 1 | 23 | - | 2,706.31 | 0.029243 | 594 | 521 | 0.003250 | 🟢 medium — moderately distinctive | — |
| 565 | **hatred** | 1 | 33 | - | 5,484.37 | - | 260 | - | 0.003249 | 🟡 high — specialist register | — |
| 566 | **geshe tonpa** | 2 | 7 | 0.753 | - | 0.011368 | - | 261 | 0.003240 | - | ~ |
| 567 | **fear** | 1 | 25 | - | 2,770.37 | 0.030361 | 585 | 532 | 0.003240 | 🟢 medium — moderately distinctive | — |
| 568 | **forever** | 1 | 16 | - | 2,659.96 | 0.029084 | 604 | 519 | 0.003233 | 🟢 medium — moderately distinctive | — |
| 569 | **going** | 1 | 61 | - | 5,463.50 | - | 262 | - | 0.003230 | 🟡 high — specialist register | — |
| 570 | **part** | 1 | 46 | - | 3,295.15 | 0.040999 | 486 | 656 | 0.003228 | 🟡 high — specialist register | ~ |
| 571 | **great giving** | 2 | 4 | 0.335 | - | 0.011454 | - | 263 | 0.003220 | - | — |
| 572 | **pray** | 1 | 19 | - | 3,157.67 | 0.038407 | 509 | 627 | 0.003213 | 🟡 high — specialist register | — |
| 573 | **kalpas** | 1 | - | - | - | 0.011515 | - | 264 | 0.003211 | - | — |
| 574 | **insect** | 1 | 23 | - | 3,271.13 | 0.041224 | 487 | 664 | 0.003209 | 🟡 high — specialist register | — |
| 575 | **use** | 1 | 66 | - | 5,361.83 | - | 265 | - | 0.003201 | 🟡 high — specialist register | — |
| 576 | **long life** | 2 | 5 | 0.331 | - | 0.011520 | - | 265 | 0.003201 | - | — |
| 577 | **instead** | 1 | 55 | - | 5,341.54 | - | 266 | - | 0.003192 | 🟡 high — specialist register | — |
| 578 | **recognize** | 1 | 21 | - | 2,870.79 | 0.033310 | 564 | 576 | 0.003175 | 🟢 medium — moderately distinctive | — |
| 579 | **arouse bodhicitta** | 2 | 4 | 0.489 | - | 0.011581 | - | 268 | 0.003173 | - | — |
| 580 | **ray** | 1 | 22 | - | 3,007.50 | 0.037121 | 531 | 616 | 0.003171 | 🟡 high — specialist register | — |
| 581 | **bird** | 1 | 23 | - | 3,662.08 | 0.056882 | 423 | 850 | 0.003169 | 🟡 high — specialist register | — |
| 582 | **spend** | 1 | 23 | - | 2,619.79 | 0.029546 | 625 | 525 | 0.003169 | 🟢 medium — moderately distinctive | — |
| 583 | **doubt** | 1 | 26 | - | 2,984.03 | 0.035120 | 549 | 595 | 0.003169 | 🟢 medium — moderately distinctive | — |
| 584 | **purification** | 1 | 19 | - | 3,157.67 | 0.040723 | 510 | 648 | 0.003167 | 🟡 high — specialist register | — |
| 585 | **emanation** | 1 | 20 | - | 3,323.86 | 0.044304 | 481 | 699 | 0.003166 | 🟡 high — specialist register | — |
| 586 | **authentic spiritual teacher** | 3 | 3 | 0.509 | - | 0.011750 | - | 270 | 0.003155 | - | — |
| 587 | **sick** | 1 | 19 | - | 3,025.19 | 0.038534 | 528 | 628 | 0.003154 | 🟡 high — specialist register | — |
| 588 | **good fortune** | 2 | 12 | 0.645 | - | 0.011909 | - | 271 | 0.003146 | - | — |
| 589 | **cast** | 1 | 21 | - | 2,839.13 | 0.033806 | 570 | 582 | 0.003145 | 🟢 medium — moderately distinctive | — |
| 590 | **excellent** | 1 | 20 | - | 2,374.98 | 0.026887 | 682 | 498 | 0.003140 | 🟢 medium — moderately distinctive | ~ |
| 591 | **garab dorje** | 2 | 10 | 0.932 | - | 0.012033 | - | 272 | 0.003136 | - | ✓ དགའ་རབ་རྡོ་རྗེ |
| 592 | **don** | 1 | 40 | - | 5,208.44 | - | 274 | - | 0.003118 | 🟡 high — specialist register | — |
| 593 | **transcendent wisdom** | 2 | 11 | 0.611 | - | 0.012075 | - | 274 | 0.003118 | - | ~ |
| 594 | **metal** | 1 | 24 | - | 2,466.20 | 0.028814 | 663 | 517 | 0.003116 | 🟢 medium — moderately distinctive | — |
| 595 | **phase** | 1 | 14 | - | 1,662.49 | 0.020785 | 948 | 411 | 0.003115 | 🟢 medium — moderately distinctive | ~ |
| 596 | **meat** | 1 | 23 | - | 2,565.35 | 0.031376 | 632 | 540 | 0.003112 | 🟢 medium — moderately distinctive | — |
| 597 | **let** | 1 | 39 | - | 4,268.74 | 0.125893 | 354 | 1,402 | 0.003099 | 🟡 high — specialist register | — |
| 598 | **ben** | 1 | 15 | - | 2,102.73 | 0.024482 | 780 | 465 | 0.003095 | 🟢 medium — moderately distinctive | — |
| 599 | **blind** | 1 | 18 | - | 2,992.45 | 0.040779 | 535 | 651 | 0.003087 | 🟢 medium — moderately distinctive | — |
| 600 | **renounce** | 1 | 18 | - | 2,992.45 | 0.040749 | 537 | 649 | 0.003085 | 🟢 medium — moderately distinctive | — |
| 601 | **king songtsen** | 2 | 5 | 0.637 | - | 0.012398 | - | 278 | 0.003083 | - | ~ |
| 602 | **throne** | 1 | 18 | - | 2,991.47 | 0.039985 | 545 | 641 | 0.003079 | 🟢 medium — moderately distinctive | — |
| 603 | **extremely** | 1 | 22 | - | 2,415.27 | 0.029473 | 674 | 523 | 0.003078 | 🟢 medium — moderately distinctive | — |
| 604 | **vision** | 1 | 21 | - | 2,943.82 | 0.038720 | 553 | 632 | 0.003076 | 🟢 medium — moderately distinctive | — |
| 605 | **feeling** | 1 | 30 | - | 3,845.09 | 0.090158 | 390 | 1,125 | 0.003066 | 🟡 high — specialist register | — |
| 606 | **whether** | 1 | 64 | - | 5,151.12 | - | 280 | - | 0.003066 | 🟡 high — specialist register | — |
| 607 | **reality** | 1 | 21 | - | 2,671.89 | 0.033936 | 601 | 585 | 0.003063 | 🟢 medium — moderately distinctive | ~ |
| 608 | **hair** | 1 | 18 | - | 2,992.45 | 0.041123 | 538 | 659 | 0.003063 | 🟢 medium — moderately distinctive | — |
| 609 | **jigme** | 1 | 13 | - | 2,160.51 | 0.025906 | 752 | 488 | 0.003056 | 🟢 medium — moderately distinctive | ~ |
| 610 | **pleasant** | 1 | 18 | - | 2,991.47 | 0.040975 | 544 | 655 | 0.003054 | 🟢 medium — moderately distinctive | — |
| 611 | **channel** | 1 | 25 | - | 3,255.27 | 0.048293 | 490 | 750 | 0.003053 | 🟡 high — specialist register | ✓ རྩ |
| 612 | **dagpo** | 1 | 13 | - | 2,160.51 | 0.025953 | 754 | 489 | 0.003050 | 🟢 medium — moderately distinctive | ~ |
| 613 | **fortunate** | 1 | 16 | - | 2,659.09 | 0.034132 | 605 | 588 | 0.003047 | 🟢 medium — moderately distinctive | — |
| 614 | **enter** | 1 | 24 | - | 2,561.69 | 0.032704 | 633 | 564 | 0.003046 | 🟢 medium — moderately distinctive | — |
| 615 | **reach** | 1 | 26 | - | 2,411.39 | 0.030614 | 675 | 534 | 0.003044 | 🟢 medium — moderately distinctive | — |
| 616 | **unbearable** | 1 | 18 | - | 2,991.47 | 0.041133 | 547 | 660 | 0.003036 | 🟢 medium — moderately distinctive | — |
| 617 | **subject** | 1 | 31 | - | 2,380.55 | 0.030626 | 681 | 535 | 0.003030 | 🟢 medium — moderately distinctive | ~ |
| 618 | **intense** | 1 | 20 | - | 2,676.19 | 0.035698 | 600 | 602 | 0.003026 | 🟢 medium — moderately distinctive | — |
| 619 | **tirthika** | 1 | 25 | - | 4,154.82 | 0.133959 | 364 | 1,439 | 0.003026 | 🟡 high — specialist register | ✓ མུ་སྟེགས་པ |
| 620 | **help** | 1 | 56 | - | 4,220.33 | 0.149113 | 357 | 1,542 | 0.003022 | 🟡 high — specialist register | — |
| 621 | **straight** | 1 | 20 | - | 2,703.93 | 0.036158 | 595 | 609 | 0.003021 | 🟢 medium — moderately distinctive | — |
| 622 | **why** | 1 | 47 | - | 5,070.96 | - | 286 | - | 0.003015 | 🟡 high — specialist register | — |
| 623 | **open** | 1 | 28 | - | 2,199.91 | 0.028304 | 734 | 512 | 0.003008 | 🟢 medium — moderately distinctive | — |
| 624 | **jigme lingpa** | 2 | 11 | 0.982 | - | 0.012748 | - | 287 | 0.003006 | - | ✓ འཇིགས་མེད་གླིང་པ |
| 625 | **kaya** | 1 | 19 | - | 3,158.70 | 0.048989 | 502 | 757 | 0.003003 | 🟡 high — specialist register | ✓ སྐུ |
| 626 | **opportunity** | 1 | 22 | - | 2,360.71 | 0.031613 | 685 | 545 | 0.002995 | 🟢 medium — moderately distinctive | — |
| 627 | **carefully** | 1 | 21 | - | 2,544.01 | 0.033591 | 638 | 580 | 0.002995 | 🟢 medium — moderately distinctive | — |
| 628 | **speak** | 1 | 20 | - | 3,007.36 | 0.044614 | 532 | 706 | 0.002995 | 🟡 high — specialist register | — |
| 629 | **downfall** | 1 | 17 | - | 2,825.28 | 0.039436 | 580 | 639 | 0.002993 | 🟢 medium — moderately distinctive | ✓ ལྟུང་བ |
| 630 | **different** | 1 | 50 | - | 5,043.30 | - | 289 | - | 0.002990 | 🟡 high — specialist register | — |
| 631 | **sit** | 1 | 21 | - | 2,839.13 | 0.040825 | 572 | 653 | 0.002985 | 🟢 medium — moderately distinctive | — |
| 632 | **sickness** | 1 | 18 | - | 2,991.47 | 0.044111 | 543 | 695 | 0.002983 | 🟢 medium — moderately distinctive | — |
| 633 | **short** | 1 | 25 | - | 2,148.21 | 0.027056 | 770 | 503 | 0.002981 | 🟢 medium — moderately distinctive | — |
| 634 | **hot** | 1 | 20 | - | 2,604.22 | 0.035172 | 627 | 596 | 0.002980 | 🟢 medium — moderately distinctive | — |
| 635 | **clean** | 1 | 18 | - | 2,865.97 | 0.041351 | 566 | 665 | 0.002977 | 🟢 medium — moderately distinctive | — |
| 636 | **toward** | 1 | 49 | - | 5,035.16 | - | 291 | - | 0.002973 | 🟡 high — specialist register | — |
| 637 | **enjoy** | 1 | 19 | - | 2,746.21 | 0.040140 | 586 | 642 | 0.002972 | 🟢 medium — moderately distinctive | — |
| 638 | **reflection** | 1 | 21 | - | 2,839.13 | 0.041900 | 571 | 669 | 0.002957 | 🟢 medium — moderately distinctive | — |
| 639 | **million** | 1 | 23 | - | 2,619.79 | 0.036570 | 626 | 610 | 0.002950 | 🟢 medium — moderately distinctive | — |
| 640 | **brother** | 1 | 16 | - | 2,659.96 | 0.039097 | 602 | 637 | 0.002945 | 🟢 medium — moderately distinctive | — |
| 641 | **stop** | 1 | 24 | - | 2,327.02 | 0.032549 | 693 | 562 | 0.002936 | 🟢 medium — moderately distinctive | — |
| 642 | **wrong action** | 2 | 5 | 0.320 | - | 0.013612 | - | 296 | 0.002933 | - | ~ |
| 643 | **expanse** | 1 | 14 | - | 2,326.70 | 0.033046 | 695 | 568 | 0.002917 | 🟢 medium — moderately distinctive | — |
| 644 | **antidote** | 1 | 19 | - | 3,157.67 | 0.052333 | 512 | 799 | 0.002912 | 🟡 high — specialist register | — |
| 645 | **love compassion** | 2 | 3 | 0.342 | - | 0.013699 | - | 299 | 0.002910 | - | — |
| 646 | **meru** | 1 | 12 | - | 1,994.97 | 0.028081 | 808 | 509 | 0.002910 | 🟢 medium — moderately distinctive | ~ |
| 647 | **bliss** | 1 | 16 | - | 2,659.09 | 0.040204 | 615 | 643 | 0.002904 | 🟢 medium — moderately distinctive | ~ |
| 648 | **longer** | 1 | 53 | - | 4,962.99 | - | 300 | - | 0.002902 | 🟡 high — specialist register | — |
| 649 | **worldly life** | 2 | 8 | 0.500 | - | 0.013702 | - | 300 | 0.002902 | - | — |
| 650 | **wrathful** | 1 | 14 | - | 2,326.70 | 0.033007 | 707 | 567 | 0.002899 | 🟢 medium — moderately distinctive | ~ |
| 651 | **protect** | 1 | 22 | - | 2,260.69 | 0.032314 | 717 | 561 | 0.002897 | 🟢 medium — moderately distinctive | — |
| 652 | **remain** | 1 | 29 | - | 2,341.28 | 0.033740 | 689 | 581 | 0.002895 | 🟢 medium — moderately distinctive | — |
| 653 | **jowo atisa** | 2 | 5 | 0.694 | - | 0.013750 | - | 301 | 0.002894 | - | — |
| 654 | **properly** | 1 | 19 | - | 2,542.38 | 0.038224 | 639 | 625 | 0.002890 | 🟢 medium — moderately distinctive | — |
| 655 | **servant** | 1 | 20 | - | 3,324.95 | 0.064933 | 476 | 919 | 0.002887 | 🟡 high — specialist register | — |
| 656 | **most** | 1 | 70 | - | 4,949.04 | - | 302 | - | 0.002887 | 🟡 high — specialist register | — |
| 657 | **day geshe ben** | 3 | 3 | 0.631 | - | 0.013825 | - | 302 | 0.002887 | - | — |
| 658 | **explain** | 1 | 13 | - | 1,666.21 | 0.024967 | 946 | 470 | 0.002881 | 🟢 medium — moderately distinctive | — |
| 659 | **lord nagarjuna** | 2 | 4 | 0.621 | - | 0.013947 | - | 303 | 0.002879 | - | ~ |
| 660 | **yogi** | 1 | 18 | - | 2,991.47 | 0.048771 | 548 | 754 | 0.002873 | 🟢 medium — moderately distinctive | — |
| 661 | **hunger** | 1 | 18 | - | 2,601.67 | 0.040507 | 629 | 644 | 0.002872 | 🟢 medium — moderately distinctive | — |
| 662 | **venerable teacher** | 2 | 5 | 0.482 | - | 0.014035 | - | 304 | 0.002872 | - | — |
| 663 | **alive** | 1 | 18 | - | 2,601.67 | 0.040574 | 628 | 646 | 0.002870 | 🟢 medium — moderately distinctive | — |
| 664 | **centre** | 1 | 20 | - | 2,435.94 | 0.036140 | 669 | 608 | 0.002869 | 🟢 medium — moderately distinctive | — |
| 665 | **reflect** | 1 | 23 | - | 2,019.21 | 0.029571 | 800 | 527 | 0.002866 | 🟢 medium — moderately distinctive | — |
| 666 | **case** | 1 | 22 | - | 2,065.93 | 0.030757 | 788 | 536 | 0.002857 | 🟢 medium — moderately distinctive | — |
| 667 | **extraordinary** | 1 | 23 | - | 1,862.65 | 0.027741 | 861 | 506 | 0.002853 | 🟢 medium — moderately distinctive | — |
| 668 | **poison** | 1 | 24 | - | 3,151.91 | 0.057018 | 514 | 851 | 0.002840 | 🟡 high — specialist register | — |
| 669 | **caus** | 1 | 29 | - | 4,819.60 | - | 309 | - | 0.002834 | 🟡 high — specialist register | — |
| 670 | **gracious root teacher** | 3 | 3 | 0.641 | - | 0.014167 | - | 309 | 0.002834 | - | — |
| 671 | **inside** | 1 | 19 | - | 2,417.42 | 0.037763 | 673 | 621 | 0.002833 | 🟢 medium — moderately distinctive | — |
| 672 | **dream** | 1 | 20 | - | 3,324.95 | 0.072226 | 474 | 984 | 0.002831 | 🟡 high — specialist register | — |
| 673 | **good thing** | 2 | 5 | 0.326 | - | 0.014174 | - | 310 | 0.002827 | - | — |
| 674 | **fortune** | 1 | 19 | - | 2,628.76 | 0.042611 | 621 | 678 | 0.002823 | 🟢 medium — moderately distinctive | — |
| 675 | **hardship** | 1 | 20 | - | 2,676.19 | 0.044841 | 599 | 709 | 0.002818 | 🟢 medium — moderately distinctive | — |
| 676 | **inner** | 1 | 30 | - | 4,776.62 | - | 313 | - | 0.002805 | 🟡 high — specialist register | — |
| 677 | **secret path** | 2 | 3 | 0.351 | - | 0.014381 | - | 313 | 0.002805 | - | ~ |
| 678 | **comfort** | 1 | 17 | - | 2,706.75 | 0.046910 | 592 | 728 | 0.002803 | 🟢 medium — moderately distinctive | — |
| 679 | **rock** | 1 | 18 | - | 2,523.27 | 0.041828 | 641 | 668 | 0.002800 | 🟢 medium — moderately distinctive | — |
| 680 | **venerable** | 1 | 14 | - | 2,326.70 | 0.037616 | 694 | 619 | 0.002799 | 🟢 medium — moderately distinctive | — |
| 681 | **sure** | 1 | 43 | - | 4,720.76 | - | 315 | - | 0.002791 | 🟡 high — specialist register | — |
| 682 | **immediately** | 1 | 22 | - | 1,963.65 | 0.031588 | 828 | 544 | 0.002782 | 🟢 medium — moderately distinctive | — |
| 683 | **today** | 1 | 24 | - | 1,407.69 | 0.024230 | 1,116 | 458 | 0.002781 | 🟢 medium — moderately distinctive | — |
| 684 | **big** | 1 | 21 | - | 2,086.17 | 0.033108 | 782 | 570 | 0.002775 | 🟢 medium — moderately distinctive | — |
| 685 | **mouth** | 1 | 21 | - | 2,810.00 | 0.050093 | 581 | 766 | 0.002771 | 🟢 medium — moderately distinctive | — |
| 686 | **else** | 1 | 39 | - | 4,676.29 | - | 318 | - | 0.002770 | 🟡 high — specialist register | — |
| 687 | **unable** | 1 | 20 | - | 2,189.10 | 0.035634 | 738 | 601 | 0.002766 | 🟢 medium — moderately distinctive | — |
| 688 | **perceive** | 1 | 18 | - | 2,649.75 | 0.046368 | 617 | 719 | 0.002761 | 🟢 medium — moderately distinctive | — |
| 689 | **thirst** | 1 | 16 | - | 2,659.09 | 0.046968 | 609 | 730 | 0.002761 | 🟢 medium — moderately distinctive | — |
| 690 | **miraculous** | 1 | 16 | - | 2,659.96 | 0.047616 | 603 | 741 | 0.002757 | 🟢 medium — moderately distinctive | — |
| 691 | **attained** | 1 | 29 | - | 4,617.40 | - | 321 | - | 0.002749 | 🟡 high — specialist register | — |
| 692 | **crown** | 1 | 19 | - | 2,327.06 | 0.040783 | 692 | 652 | 0.002734 | 🟢 medium — moderately distinctive | ~ |
| 693 | **fully** | 1 | 21 | - | 2,007.27 | 0.033461 | 802 | 577 | 0.002730 | 🟢 medium — moderately distinctive | — |
| 694 | **whenever** | 1 | 34 | - | 4,596.68 | - | 324 | - | 0.002729 | 🟡 high — specialist register | — |
| 695 | **tear** | 1 | 17 | - | 2,825.28 | 0.053655 | 576 | 806 | 0.002727 | 🟢 medium — moderately distinctive | — |
| 696 | **example** | 1 | 42 | - | 4,570.15 | - | 326 | - | 0.002715 | 🟡 high — specialist register | — |
| 697 | **turtle** | 1 | 16 | - | 2,659.09 | 0.048949 | 612 | 756 | 0.002714 | 🟢 medium — moderately distinctive | — |
| 698 | **serve** | 1 | 19 | - | 2,180.64 | 0.038682 | 739 | 630 | 0.002701 | 🟢 medium — moderately distinctive | — |
| 699 | **pride** | 1 | 15 | - | 2,493.71 | 0.046590 | 644 | 723 | 0.002698 | 🟢 medium — moderately distinctive | — |
| 700 | **everyone** | 1 | 35 | - | 4,520.61 | - | 329 | - | 0.002695 | 🟡 high — specialist register | — |
| 701 | **seed** | 1 | 20 | - | 2,583.21 | 0.047895 | 630 | 745 | 0.002692 | 🟢 medium — moderately distinctive | — |
| 702 | **during** | 1 | 65 | - | 4,512.38 | - | 330 | - | 0.002688 | 🟡 high — specialist register | — |
| 703 | **profound path** | 2 | 10 | 0.545 | - | 0.015066 | - | 331 | 0.002682 | - | ~ |
| 704 | **nirvana** | 1 | 15 | - | 2,492.89 | 0.046850 | 650 | 726 | 0.002681 | 🟢 medium — moderately distinctive | ✓ མྱ་ངན་ལས་འདས་པ |
| 705 | **utterly** | 1 | 15 | - | 2,493.71 | 0.047009 | 646 | 731 | 0.002681 | 🟢 medium — moderately distinctive | — |
| 706 | **practised** | 1 | 27 | - | 4,488.68 | - | 332 | - | 0.002675 | 🟡 high — specialist register | — |
| 707 | **preliminary** | 1 | 24 | - | 2,346.55 | 0.043840 | 688 | 690 | 0.002670 | 🟢 medium — moderately distinctive | — |
| 708 | **phas** | 1 | 27 | - | 4,487.21 | - | 334 | - | 0.002662 | 🟡 high — specialist register | — |
| 709 | **fail** | 1 | 19 | - | 2,289.75 | 0.042523 | 712 | 676 | 0.002654 | 🟢 medium — moderately distinctive | — |
| 710 | **belief** | 1 | 20 | - | 2,363.98 | 0.044515 | 684 | 705 | 0.002651 | 🟢 medium — moderately distinctive | — |
| 711 | **order** | 1 | 22 | - | 1,946.12 | 0.034869 | 837 | 591 | 0.002651 | 🟢 medium — moderately distinctive | — |
| 712 | **chance** | 1 | 20 | - | 2,021.33 | 0.036746 | 799 | 613 | 0.002650 | 🟢 medium — moderately distinctive | — |
| 713 | **lord maitreya** | 2 | 5 | 0.732 | - | 0.015497 | - | 336 | 0.002650 | - | ~ |
| 714 | **horse** | 1 | 15 | - | 2,255.52 | 0.042179 | 720 | 672 | 0.002648 | 🟢 medium — moderately distinctive | — |
| 715 | **claim** | 1 | 19 | - | 2,289.75 | 0.042916 | 713 | 680 | 0.002645 | 🟢 medium — moderately distinctive | — |
| 716 | **samayas** | 1 | - | - | - | 0.015559 | - | 337 | 0.002643 | - | — |
| 717 | **create** | 1 | 20 | - | 2,113.07 | 0.039019 | 775 | 635 | 0.002636 | 🟢 medium — moderately distinctive | — |
| 718 | **lingpa** | 1 | 11 | - | 1,828.12 | 0.033197 | 886 | 574 | 0.002634 | 🟢 medium — moderately distinctive | ~ |
| 719 | **something** | 1 | 40 | - | 4,432.60 | - | 339 | - | 0.002631 | 🟡 high — specialist register | — |
| 720 | **undergo** | 1 | 16 | - | 2,405.89 | 0.046959 | 677 | 729 | 0.002624 | 🟢 medium — moderately distinctive | — |
| 721 | **front** | 1 | 35 | - | 4,392.44 | - | 341 | - | 0.002618 | 🟡 high — specialist register | — |
| 722 | **fly** | 1 | 21 | - | 2,943.82 | 0.067513 | 552 | 957 | 0.002617 | 🟢 medium — moderately distinctive | — |
| 723 | **home** | 1 | 22 | - | 1,972.73 | 0.036743 | 826 | 612 | 0.002617 | 🟢 medium — moderately distinctive | — |
| 724 | **wind** | 1 | 19 | - | 2,495.26 | 0.051189 | 642 | 783 | 0.002611 | 🟢 medium — moderately distinctive | ✓ རླུང |
| 725 | **discipline** | 1 | 17 | - | 2,274.76 | 0.044305 | 714 | 700 | 0.002608 | 🟢 medium — moderately distinctive | — |
| 726 | **bodhisattva level** | 2 | 4 | 0.448 | - | 0.016194 | - | 344 | 0.002600 | - | ~ |
| 727 | **countless** | 1 | 15 | - | 2,492.89 | 0.051068 | 651 | 779 | 0.002598 | 🟢 medium — moderately distinctive | — |
| 728 | **divine** | 1 | 15 | - | 2,492.89 | 0.050974 | 652 | 778 | 0.002598 | 🟢 medium — moderately distinctive | — |
| 729 | **cultivate** | 1 | 15 | - | 2,493.71 | 0.051603 | 645 | 789 | 0.002596 | 🟢 medium — moderately distinctive | — |
| 730 | **prostrate** | 1 | 15 | - | 2,492.89 | 0.051478 | 647 | 787 | 0.002595 | 🟢 medium — moderately distinctive | — |
| 731 | **crest** | 1 | 11 | - | 1,828.72 | 0.034927 | 883 | 594 | 0.002589 | 🟢 medium — moderately distinctive | — |
| 732 | **dog** | 1 | 20 | - | 3,324.95 | 0.119583 | 475 | 1,330 | 0.002589 | 🟡 high — specialist register | — |
| 733 | **meditating** | 1 | 26 | - | 4,321.02 | - | 347 | - | 0.002581 | 🟡 high — specialist register | — |
| 734 | **great compassionate** | 2 | 3 | 0.444 | - | 0.016480 | - | 347 | 0.002581 | - | ~ |
| 735 | **force** | 1 | 25 | - | 2,249.64 | 0.044769 | 722 | 708 | 0.002581 | 🟢 medium — moderately distinctive | — |
| 736 | **arm** | 1 | 19 | - | 2,256.23 | 0.045838 | 718 | 714 | 0.002577 | 🟢 medium — moderately distinctive | — |
| 737 | **easy** | 1 | 17 | - | 2,213.59 | 0.044319 | 732 | 702 | 0.002575 | 🟢 medium — moderately distinctive | — |
| 738 | **grain** | 1 | 26 | - | 2,108.91 | 0.041697 | 776 | 666 | 0.002574 | 🟢 medium — moderately distinctive | — |
| 739 | **presence** | 1 | 18 | - | 2,065.87 | 0.041005 | 789 | 657 | 0.002573 | 🟢 medium — moderately distinctive | — |
| 740 | **boundless** | 1 | 15 | - | 2,492.89 | 0.051538 | 659 | 788 | 0.002570 | 🟢 medium — moderately distinctive | ~ |
| 741 | **side** | 1 | 27 | - | 2,905.10 | 0.072818 | 559 | 989 | 0.002569 | 🟢 medium — moderately distinctive | — |
| 742 | **oneself** | 1 | 15 | - | 2,492.89 | 0.051671 | 658 | 791 | 0.002568 | 🟢 medium — moderately distinctive | — |
| 743 | **tathagata** | 1 | 13 | - | 2,160.51 | 0.042552 | 766 | 677 | 0.002568 | 🟢 medium — moderately distinctive | ✓ དེ་བཞིན་གཤེགས་པ |
| 744 | **bone** | 1 | 17 | - | 2,706.75 | 0.062540 | 593 | 907 | 0.002566 | 🟢 medium — moderately distinctive | — |
| 745 | **poor** | 1 | 18 | - | 1,892.45 | 0.037625 | 854 | 620 | 0.002565 | 🟢 medium — moderately distinctive | — |
| 746 | **include** | 1 | 25 | - | 1,855.33 | 0.036882 | 864 | 615 | 0.002564 | 🟢 medium — moderately distinctive | — |
| 747 | **anger** | 1 | 17 | - | 2,162.96 | 0.044261 | 745 | 698 | 0.002561 | 🟢 medium — moderately distinctive | — |
| 748 | **house** | 1 | 20 | - | 1,583.69 | 0.031977 | 1,007 | 556 | 0.002561 | 🟢 medium — moderately distinctive | — |
| 749 | **eighty** | 1 | 14 | - | 2,229.09 | 0.046015 | 727 | 716 | 0.002559 | 🟢 medium — moderately distinctive | ~ |
| 750 | **aspect** | 1 | 17 | - | 2,622.00 | 0.057825 | 623 | 855 | 0.002557 | 🟢 medium — moderately distinctive | — |
| 751 | **died** | 1 | 31 | - | 4,289.04 | - | 352 | - | 0.002552 | 🟡 high — specialist register | — |
| 752 | **fill** | 1 | 12 | - | 1,562.53 | 0.031997 | 1,015 | 557 | 0.002551 | 🟢 medium — moderately distinctive | — |
| 753 | **consider** | 1 | 33 | - | 2,919.18 | 0.074865 | 556 | 1,022 | 0.002548 | 🟢 medium — moderately distinctive | — |
| 754 | **likewise** | 1 | 14 | - | 2,229.09 | 0.046579 | 730 | 721 | 0.002546 | 🟢 medium — moderately distinctive | — |
| 755 | **hope** | 1 | 25 | - | 2,436.07 | 0.051879 | 668 | 794 | 0.002545 | 🟢 medium — moderately distinctive | — |
| 756 | **hat** | 1 | 14 | - | 2,229.09 | 0.046875 | 728 | 727 | 0.002540 | 🟢 medium — moderately distinctive | — |
| 757 | **making** | 1 | 54 | - | 4,260.69 | - | 355 | - | 0.002534 | 🟡 high — specialist register | — |
| 758 | **skin** | 1 | 16 | - | 2,547.53 | 0.057760 | 637 | 854 | 0.002529 | 🟢 medium — moderately distinctive | — |
| 759 | **made** | 1 | 68 | - | 4,242.84 | - | 356 | - | 0.002528 | 🟡 high — specialist register | — |
| 760 | **obtain** | 1 | 18 | - | 1,958.64 | 0.040960 | 829 | 654 | 0.002525 | 🟢 medium — moderately distinctive | — |
| 761 | **wonderful** | 1 | 13 | - | 2,161.22 | 0.046532 | 749 | 720 | 0.002518 | 🟢 medium — moderately distinctive | — |
| 762 | **beginning** | 1 | 46 | - | 4,210.93 | - | 358 | - | 0.002517 | 🟡 high — specialist register | ✓ ཡེ |
| 763 | **liberate** | 1 | 15 | - | 2,492.89 | 0.056217 | 653 | 841 | 0.002512 | 🟢 medium — moderately distinctive | — |
| 764 | **alone** | 1 | 38 | - | 4,171.83 | - | 360 | - | 0.002505 | 🟡 high — specialist register | — |
| 765 | **bed** | 1 | 15 | - | 2,388.31 | 0.054661 | 679 | 810 | 0.002503 | 🟢 medium — moderately distinctive | — |
| 766 | **arousing** | 1 | 25 | - | 4,156.18 | - | 361 | - | 0.002500 | 🟡 high — specialist register | — |
| 767 | **samantabhadra** | 1 | 11 | - | 1,828.12 | 0.038838 | 888 | 634 | 0.002496 | 🟢 medium — moderately distinctive | ✓ ཀུན་ཏུ་བཟང་པོ |
| 768 | **compassionate** | 1 | 12 | - | 1,994.32 | 0.043280 | 813 | 684 | 0.002490 | 🟢 medium — moderately distinctive | ~ |
| 769 | **huge** | 1 | 18 | - | 1,853.68 | 0.040754 | 866 | 650 | 0.002488 | 🟢 medium — moderately distinctive | — |
| 770 | **sixteen** | 1 | 14 | - | 2,327.46 | 0.055082 | 690 | 812 | 0.002480 | 🟢 medium — moderately distinctive | — |
| 771 | **another** | 1 | 56 | - | 4,139.31 | - | 366 | - | 0.002472 | 🟡 high — specialist register | — |
| 772 | **able** | 1 | 45 | - | 4,124.64 | - | 367 | - | 0.002466 | 🟡 high — specialist register | — |
| 773 | **abbot** | 1 | 12 | - | 1,994.32 | 0.044039 | 821 | 692 | 0.002465 | 🟢 medium — moderately distinctive | ✓ མཁན་པོ |
| 774 | **sexual** | 1 | 14 | - | 2,327.46 | 0.055649 | 691 | 823 | 0.002464 | 🟢 medium — moderately distinctive | — |
| 775 | **seeing** | 1 | 31 | - | 4,108.28 | - | 368 | - | 0.002461 | 🟡 high — specialist register | ~ |
| 776 | **good lama** | 2 | 4 | 0.357 | - | 0.017422 | - | 368 | 0.002461 | - | ~ |
| 777 | **knowledge** | 1 | 15 | - | 2,075.34 | 0.046746 | 785 | 724 | 0.002459 | 🟢 medium — moderately distinctive | — |
| 778 | **great translator** | 2 | 4 | 0.485 | - | 0.017471 | - | 369 | 0.002455 | - | — |
| 779 | **large** | 1 | 20 | - | 1,594.10 | 0.035892 | 995 | 605 | 0.002452 | 🟢 medium — moderately distinctive | — |
| 780 | **regret** | 1 | 16 | - | 2,140.95 | 0.047784 | 771 | 744 | 0.002447 | 🟢 medium — moderately distinctive | — |
| 781 | **sense** | 1 | 16 | - | 1,850.93 | 0.042239 | 868 | 673 | 0.002442 | 🟢 medium — moderately distinctive | — |
| 782 | **lie** | 1 | 10 | - | 1,445.37 | 0.033191 | 1,101 | 573 | 0.002441 | 🟢 medium — moderately distinctive | — |
| 783 | **realized** | 1 | 35 | - | 4,048.90 | - | 372 | - | 0.002439 | 🟡 high — specialist register | — |
| 784 | **great siddha** | 2 | 4 | 0.421 | - | 0.017657 | - | 372 | 0.002439 | - | ~ |
| 785 | **darkness** | 1 | 14 | - | 2,326.70 | 0.056032 | 699 | 837 | 0.002432 | 🟢 medium — moderately distinctive | — |
| 786 | **energy** | 1 | 26 | - | 2,041.35 | 0.047091 | 796 | 732 | 0.002431 | 🟢 medium — moderately distinctive | ✓ རླུང |
| 787 | **dark** | 1 | 14 | - | 2,105.15 | 0.048236 | 777 | 749 | 0.002431 | 🟢 medium — moderately distinctive | — |
| 788 | **mentally** | 1 | 14 | - | 2,326.70 | 0.056042 | 703 | 838 | 0.002424 | 🟢 medium — moderately distinctive | — |
| 789 | **effect similar** | 2 | 13 | 0.667 | - | 0.017783 | - | 375 | 0.002423 | - | — |
| 790 | **frog** | 1 | 15 | - | 2,492.89 | 0.064126 | 656 | 915 | 0.002422 | 🟢 medium — moderately distinctive | — |
| 791 | **study** | 1 | 19 | - | 1,810.57 | 0.041174 | 907 | 662 | 0.002419 | 🟢 medium — moderately distinctive | ✓ ཐོས་པ |
| 792 | **garab** | 1 | 10 | - | 1,661.93 | 0.038552 | 976 | 629 | 0.002417 | 🟢 medium — moderately distinctive | ~ |
| 793 | **precious lord** | 2 | 3 | 0.465 | - | 0.018135 | - | 377 | 0.002413 | - | ~ |
| 794 | **appearance** | 1 | 17 | - | 2,556.26 | 0.068571 | 635 | 967 | 0.002413 | 🟢 medium — moderately distinctive | — |
| 795 | **sacred** | 1 | 14 | - | 2,326.70 | 0.056327 | 706 | 844 | 0.002412 | 🟢 medium — moderately distinctive | — |
| 796 | **wild** | 1 | 14 | - | 2,229.09 | 0.055560 | 726 | 819 | 0.002410 | 🟢 medium — moderately distinctive | — |
| 797 | **round** | 1 | 18 | - | 1,775.28 | 0.041149 | 920 | 661 | 0.002407 | 🟢 medium — moderately distinctive | — |
| 798 | **approach** | 1 | 18 | - | 1,953.01 | 0.046580 | 835 | 722 | 0.002396 | 🟢 medium — moderately distinctive | ~ |
| 799 | **practise guru** | 2 | 3 | 0.408 | - | 0.018416 | - | 381 | 0.002392 | - | — |
| 800 | **commit** | 1 | 12 | - | 1,682.18 | 0.041097 | 942 | 658 | 0.002391 | 🟢 medium — moderately distinctive | — |
| 801 | **honour** | 1 | 16 | - | 2,312.59 | 0.058470 | 711 | 856 | 0.002389 | 🟢 medium — moderately distinctive | — |
| 802 | **great translator vairotsana** | 3 | 3 | 0.698 | - | 0.018484 | - | 382 | 0.002387 | - | — |
| 803 | **heat** | 1 | 16 | - | 2,066.57 | 0.050572 | 787 | 771 | 0.002384 | 🟢 medium — moderately distinctive | — |
| 804 | **particular** | 1 | 38 | - | 3,976.08 | - | 383 | - | 0.002382 | 🟡 high — specialist register | — |
| 805 | **appeared** | 1 | 37 | - | 3,928.91 | - | 384 | - | 0.002377 | 🟡 high — specialist register | — |
| 806 | **human form** | 2 | 8 | 0.509 | - | 0.018667 | - | 384 | 0.002377 | - | — |
| 807 | **tion** | 1 | 17 | - | 2,825.28 | 0.096631 | 577 | 1,187 | 0.002372 | 🟢 medium — moderately distinctive | — |
| 808 | **equal** | 1 | 18 | - | 1,781.65 | 0.043158 | 918 | 682 | 0.002370 | 🟢 medium — moderately distinctive | — |
| 809 | **rigdzin** | 1 | 11 | - | 1,828.12 | 0.044470 | 885 | 703 | 0.002369 | 🟢 medium — moderately distinctive | — |
| 810 | **tantric** | 1 | 13 | - | 2,160.51 | 0.055672 | 763 | 824 | 0.002346 | 🟢 medium — moderately distinctive | — |
| 811 | **lose** | 1 | 16 | - | 1,815.78 | 0.044764 | 906 | 707 | 0.002339 | 🟢 medium — moderately distinctive | — |
| 812 | **accomplish** | 1 | 13 | - | 1,878.98 | 0.047770 | 855 | 743 | 0.002338 | 🟢 medium — moderately distinctive | — |
| 813 | **name** | 1 | 28 | - | 2,250.18 | 0.061408 | 721 | 890 | 0.002333 | 🟢 medium — moderately distinctive | — |
| 814 | **wife** | 1 | 14 | - | 2,159.29 | 0.055951 | 769 | 832 | 0.002327 | 🟢 medium — moderately distinctive | — |
| 815 | **kingdom** | 1 | 17 | - | 2,048.72 | 0.053638 | 795 | 805 | 0.002326 | 🟢 medium — moderately distinctive | — |
| 816 | **distraction** | 1 | 15 | - | 2,492.89 | 0.077643 | 649 | 1,039 | 0.002320 | 🟢 medium — moderately distinctive | — |
| 817 | **ago** | 1 | 19 | - | 1,437.15 | 0.037959 | 1,106 | 624 | 0.002320 | 🟢 medium — moderately distinctive | — |
| 818 | **merchant** | 1 | 19 | - | 2,164.17 | 0.060649 | 743 | 872 | 0.002318 | 🟢 medium — moderately distinctive | — |
| 819 | **ill** | 1 | 18 | - | 2,169.23 | 0.061042 | 742 | 877 | 0.002314 | 🟢 medium — moderately distinctive | — |
| 820 | **accumulate merit** | 2 | 12 | 0.671 | - | 0.019462 | - | 397 | 0.002313 | - | — |
| 821 | **yoke** | 1 | 13 | - | 2,160.51 | 0.059421 | 762 | 860 | 0.002304 | 🟢 medium — moderately distinctive | — |
| 822 | **rigdzin jigme** | 2 | 10 | 0.962 | - | 0.019723 | - | 399 | 0.002303 | - | — |
| 823 | **blue** | 1 | 14 | - | 1,936.98 | 0.051151 | 839 | 782 | 0.002300 | 🟢 medium — moderately distinctive | — |
| 824 | **ephemeral** | 1 | 13 | - | 2,160.51 | 0.060322 | 759 | 867 | 0.002300 | 🟢 medium — moderately distinctive | — |
| 825 | **pass** | 1 | 16 | - | 1,948.76 | 0.051368 | 836 | 785 | 0.002300 | 🟢 medium — moderately distinctive | — |
| 826 | **stream** | 1 | 17 | - | 2,213.59 | 0.062499 | 733 | 903 | 0.002299 | 🟢 medium — moderately distinctive | — |
| 827 | **crowd** | 1 | 13 | - | 2,161.22 | 0.061197 | 747 | 884 | 0.002298 | 🟢 medium — moderately distinctive | — |
| 828 | **endless** | 1 | 13 | - | 2,161.22 | 0.061186 | 748 | 883 | 0.002298 | 🟢 medium — moderately distinctive | — |
| 829 | **thirty** | 1 | 3 | - | 462.71 | 0.024295 | 2,726 | 459 | 0.002286 | 🔵 low — common in general English | ~ |
| 830 | **selfish** | 1 | 13 | - | 2,161.22 | 0.061503 | 750 | 895 | 0.002282 | 🟢 medium — moderately distinctive | — |
| 831 | **meet** | 1 | 15 | - | 1,244.92 | 0.035821 | 1,230 | 604 | 0.002281 | 🟢 medium — moderately distinctive | — |
| 832 | **elephant** | 1 | 14 | - | 2,326.70 | 0.071555 | 698 | 980 | 0.002281 | 🟢 medium — moderately distinctive | — |
| 833 | **temple** | 1 | 14 | - | 2,326.70 | 0.070976 | 700 | 978 | 0.002279 | 🟢 medium — moderately distinctive | — |
| 834 | **sambhogakaya** | 1 | 13 | - | 2,160.51 | 0.061574 | 751 | 897 | 0.002278 | 🟢 medium — moderately distinctive | ✓ ལོངས་སྤྱོད་རྫོགས་པའི་སྐུ |
| 835 | **please** | 1 | 21 | - | 3,091.38 | 0.182384 | 519 | 1,757 | 0.002277 | 🟡 high — specialist register | — |
| 836 | **became** | 1 | 34 | - | 3,767.71 | - | 405 | - | 0.002275 | 🟡 high — specialist register | — |
| 837 | **confidence** | 1 | 16 | - | 1,703.35 | 0.047550 | 933 | 736 | 0.002263 | 🟢 medium — moderately distinctive | — |
| 838 | **escape** | 1 | 14 | - | 2,060.92 | 0.059408 | 791 | 859 | 0.002263 | 🟢 medium — moderately distinctive | — |
| 839 | **treasure** | 1 | 14 | - | 2,326.70 | 0.072491 | 705 | 986 | 0.002263 | 🟢 medium — moderately distinctive | ~ |
| 840 | **relative** | 1 | 20 | - | 2,313.66 | 0.071973 | 709 | 982 | 0.002260 | 🟢 medium — moderately distinctive | ~ |
| 841 | **given** | 1 | 48 | - | 3,755.59 | - | 409 | - | 0.002257 | 🟡 high — specialist register | — |
| 842 | **actual** | 1 | 16 | - | 1,698.99 | 0.047605 | 934 | 740 | 0.002256 | 🟢 medium — moderately distinctive | — |
| 843 | **conduct** | 1 | 15 | - | 1,837.15 | 0.051325 | 874 | 784 | 0.002255 | 🟢 medium — moderately distinctive | — |
| 844 | **arrive** | 1 | 7 | - | 919.31 | 0.031723 | 1,572 | 550 | 0.002252 | 🟢 medium — moderately distinctive | — |
| 845 | **known** | 1 | 37 | - | 3,754.54 | - | 410 | - | 0.002252 | 🟡 high — specialist register | — |
| 846 | **primal** | 1 | 13 | - | 2,160.51 | 0.061606 | 768 | 899 | 0.002250 | 🟢 medium — moderately distinctive | ~ |
| 847 | **protection** | 1 | 16 | - | 1,670.21 | 0.047590 | 945 | 738 | 0.002248 | 🟢 medium — moderately distinctive | — |
| 848 | **branch** | 1 | 19 | - | 2,172.30 | 0.067202 | 740 | 944 | 0.002246 | 🟢 medium — moderately distinctive | — |
| 849 | **condition** | 1 | 18 | - | 1,857.75 | 0.052513 | 863 | 802 | 0.002244 | 🟢 medium — moderately distinctive | — |
| 850 | **found** | 1 | 37 | - | 3,746.96 | - | 412 | - | 0.002243 | 🟡 high — specialist register | — |
| 851 | **sometime** | 1 | 29 | - | 3,745.65 | - | 413 | - | 0.002239 | 🟡 high — specialist register | — |
| 852 | **detsen** | 1 | 9 | - | 1,495.74 | 0.044019 | 1,049 | 691 | 0.002233 | 🟢 medium — moderately distinctive | ~ |
| 853 | **transmission** | 1 | 17 | - | 2,195.73 | 0.068758 | 736 | 969 | 0.002228 | 🟢 medium — moderately distinctive | — |
| 854 | **yak** | 1 | 14 | - | 2,326.70 | 0.079146 | 697 | 1,044 | 0.002227 | 🟢 medium — moderately distinctive | — |
| 855 | **naropa thought** | 2 | 3 | 0.407 | - | 0.020993 | - | 416 | 0.002225 | - | ~ |
| 856 | **physical** | 1 | 15 | - | 1,807.69 | 0.051112 | 910 | 780 | 0.002221 | 🟢 medium — moderately distinctive | — |
| 857 | **truly** | 1 | 24 | - | 3,701.64 | - | 417 | - | 0.002221 | 🟡 high — specialist register | — |
| 858 | **negative karmic effect** | 3 | 3 | 0.534 | - | 0.021015 | - | 417 | 0.002221 | - | ~ |
| 859 | **taken** | 1 | 44 | - | 3,696.81 | - | 418 | - | 0.002216 | 🟡 high — specialist register | — |
| 860 | **lhasa** | 1 | 9 | - | 1,495.74 | 0.044230 | 1,059 | 697 | 0.002215 | 🟢 medium — moderately distinctive | — |
| 861 | **soon** | 1 | 34 | - | 2,950.88 | 0.181215 | 550 | 1,680 | 0.002214 | 🟢 medium — moderately distinctive | — |
| 862 | **spread** | 1 | 15 | - | 1,714.98 | 0.050546 | 931 | 770 | 0.002214 | 🟢 medium — moderately distinctive | — |
| 863 | **grow** | 1 | 19 | - | 1,860.87 | 0.055737 | 862 | 826 | 0.002213 | 🟢 medium — moderately distinctive | — |
| 864 | **around** | 1 | 55 | - | 3,691.34 | - | 419 | - | 0.002212 | 🟡 high — specialist register | — |
| 865 | **skull** | 1 | 13 | - | 2,160.51 | 0.066785 | 767 | 938 | 0.002211 | 🟢 medium — moderately distinctive | ~ |
| 866 | **nirmanakaya** | 1 | 12 | - | 1,994.32 | 0.061129 | 811 | 881 | 0.002211 | 🟢 medium — moderately distinctive | ✓ སྤྲུལ་སྐུ |
| 867 | **deep** | 1 | 14 | - | 1,696.00 | 0.050242 | 937 | 768 | 0.002211 | 🟢 medium — moderately distinctive | — |
| 868 | **hunter** | 1 | 16 | - | 2,467.76 | 0.094317 | 660 | 1,161 | 0.002208 | 🟢 medium — moderately distinctive | — |
| 869 | **cloud** | 1 | 15 | - | 2,313.53 | 0.078582 | 710 | 1,042 | 0.002206 | 🟢 medium — moderately distinctive | — |
| 870 | **importance** | 1 | 15 | - | 1,807.69 | 0.051675 | 909 | 792 | 0.002206 | 🟢 medium — moderately distinctive | — |
| 871 | **seat** | 1 | 11 | - | 1,457.78 | 0.043340 | 1,096 | 686 | 0.002206 | 🟢 medium — moderately distinctive | ~ |
| 872 | **thangpa** | 1 | 9 | - | 1,495.74 | 0.044309 | 1,062 | 701 | 0.002205 | 🟢 medium — moderately distinctive | ~ |
| 873 | **close** | 1 | 16 | - | 1,231.87 | 0.039094 | 1,242 | 636 | 0.002205 | 🟢 medium — moderately distinctive | ~ |
| 874 | **beyond** | 1 | 33 | - | 3,668.68 | - | 421 | - | 0.002203 | 🟡 high — specialist register | — |
| 875 | **awareness** | 1 | 13 | - | 2,005.06 | 0.061580 | 804 | 898 | 0.002201 | 🟢 medium — moderately distinctive | ✓ རིག་པ |
| 876 | **rejoice** | 1 | 12 | - | 1,994.32 | 0.061220 | 815 | 886 | 0.002200 | 🟢 medium — moderately distinctive | — |
| 877 | **jambudvipa** | 1 | 9 | - | 1,495.74 | 0.045437 | 1,048 | 712 | 0.002198 | 🟢 medium — moderately distinctive | ✓ འཛམ་བུ་གླིང |
| 878 | **instance** | 1 | 14 | - | 1,936.98 | 0.059874 | 838 | 864 | 0.002196 | 🟢 medium — moderately distinctive | — |
| 879 | **bowl** | 1 | 13 | - | 2,161.22 | 0.072659 | 746 | 988 | 0.002195 | 🟢 medium — moderately distinctive | — |
| 880 | **bodhisattva santideva** | 2 | 5 | 0.686 | - | 0.021733 | - | 423 | 0.002195 | - | — |
| 881 | **image** | 1 | 15 | - | 2,050.57 | 0.064384 | 794 | 917 | 0.002195 | 🟢 medium — moderately distinctive | — |
| 882 | **chapter** | 1 | 14 | - | 1,662.49 | 0.050763 | 947 | 773 | 0.002194 | 🟢 medium — moderately distinctive | — |
| 883 | **trust** | 1 | 17 | - | 1,460.78 | 0.044108 | 1,094 | 694 | 0.002193 | 🟢 medium — moderately distinctive | — |
| 884 | **transform** | 1 | 13 | - | 2,069.87 | 0.066518 | 786 | 935 | 0.002187 | 🟢 medium — moderately distinctive | — |
| 885 | **sake** | 1 | 13 | - | 1,954.79 | 0.061122 | 831 | 880 | 0.002186 | 🟢 medium — moderately distinctive | — |
| 886 | **possess** | 1 | 17 | - | 2,825.28 | 0.149307 | 578 | 1,559 | 0.002185 | 🟢 medium — moderately distinctive | — |
| 887 | **apply** | 1 | 18 | - | 1,988.37 | 0.061410 | 825 | 891 | 0.002181 | 🟢 medium — moderately distinctive | — |
| 888 | **gather** | 1 | 14 | - | 2,023.52 | 0.065443 | 798 | 926 | 0.002180 | 🟢 medium — moderately distinctive | — |
| 889 | **faculty** | 1 | 22 | - | 3,656.25 | - | 427 | - | 0.002178 | 🟡 high — specialist register | — |
| 890 | **harsh** | 1 | 13 | - | 1,913.71 | 0.060904 | 844 | 875 | 0.002176 | 🟢 medium — moderately distinctive | — |
| 891 | **weapon** | 1 | 13 | - | 2,005.06 | 0.065456 | 803 | 927 | 0.002172 | 🟢 medium — moderately distinctive | — |
| 892 | **slightest** | 1 | 22 | - | 3,656.25 | - | 429 | - | 0.002169 | 🟡 high — specialist register | — |
| 893 | **follower** | 1 | 13 | - | 2,160.51 | 0.072524 | 764 | 987 | 0.002169 | 🟢 medium — moderately distinctive | — |
| 894 | **pratyekabuddha** | 1 | 14 | - | 2,326.70 | 0.086164 | 702 | 1,108 | 0.002169 | 🟢 medium — moderately distinctive | ✓ རང་སངས་རྒྱས |
| 895 | **great par** | 2 | 4 | 0.552 | - | 0.022053 | - | 430 | 0.002165 | - | — |
| 896 | **angry** | 1 | 13 | - | 1,913.71 | 0.061251 | 845 | 887 | 0.002161 | 🟢 medium — moderately distinctive | — |
| 897 | **abandon** | 1 | 13 | - | 1,739.52 | 0.055127 | 925 | 813 | 0.002161 | 🟢 medium — moderately distinctive | — |
| 898 | **strength** | 1 | 16 | - | 1,647.71 | 0.050849 | 982 | 776 | 0.002156 | 🟢 medium — moderately distinctive | — |
| 899 | **primal wisdom** | 2 | 13 | 0.768 | - | 0.022389 | - | 433 | 0.002153 | - | ✓ ཡེ་ཤེས |
| 900 | **must** | 1 | 45 | - | 3,650.03 | - | 434 | - | 0.002149 | 🟡 high — specialist register | — |
| 901 | **long ago** | 2 | 13 | 0.743 | - | 0.022532 | - | 436 | 0.002141 | - | — |
| 902 | **devote** | 1 | 12 | - | 1,994.97 | 0.067434 | 809 | 955 | 0.002136 | 🟢 medium — moderately distinctive | — |
| 903 | **useless** | 1 | 12 | - | 1,994.32 | 0.067245 | 816 | 946 | 0.002136 | 🟢 medium — moderately distinctive | — |
| 904 | **strong** | 1 | 17 | - | 1,328.27 | 0.043822 | 1,191 | 689 | 0.002134 | 🟢 medium — moderately distinctive | — |
| 905 | **beat** | 1 | 13 | - | 1,913.71 | 0.064904 | 843 | 918 | 0.002130 | 🟢 medium — moderately distinctive | — |
| 906 | **destroy** | 1 | 13 | - | 1,954.79 | 0.066418 | 830 | 934 | 0.002130 | 🟢 medium — moderately distinctive | — |
| 907 | **walk** | 1 | 13 | - | 1,954.79 | 0.066301 | 832 | 932 | 0.002129 | 🟢 medium — moderately distinctive | — |
| 908 | **took** | 1 | 38 | - | 3,578.64 | - | 439 | - | 0.002128 | 🟡 high — specialist register | — |
| 909 | **impossible** | 1 | 14 | - | 1,696.00 | 0.055823 | 938 | 828 | 0.002128 | 🟢 medium — moderately distinctive | — |
| 910 | **prevent** | 1 | 16 | - | 1,559.09 | 0.050825 | 1,016 | 775 | 0.002127 | 🟢 medium — moderately distinctive | — |
| 911 | **sincere** | 1 | 12 | - | 1,994.97 | 0.067740 | 810 | 963 | 0.002127 | 🟢 medium — moderately distinctive | — |
| 912 | **statue** | 1 | 13 | - | 2,160.51 | 0.079674 | 758 | 1,046 | 0.002127 | 🟢 medium — moderately distinctive | — |
| 913 | **bhagavan** | 1 | 9 | - | 1,495.74 | 0.047723 | 1,079 | 742 | 0.002125 | 🟢 medium — moderately distinctive | ✓ བཅོམ་ལྡན་འདས |
| 914 | **mind lineage** | 2 | 4 | 0.359 | - | 0.022945 | - | 440 | 0.002124 | - | ~ |
| 915 | **breath** | 1 | 12 | - | 1,994.32 | 0.067532 | 817 | 958 | 0.002123 | 🟢 medium — moderately distinctive | — |
| 916 | **union** | 1 | 17 | - | 1,333.80 | 0.045908 | 1,147 | 715 | 0.002119 | 🟢 medium — moderately distinctive | ~ |
| 917 | **negative effect** | 2 | 5 | 0.333 | - | 0.023070 | - | 442 | 0.002116 | - | ~ |
| 918 | **easily** | 1 | 14 | - | 1,696.00 | 0.056063 | 936 | 839 | 0.002116 | 🟢 medium — moderately distinctive | — |
| 919 | **skilfully** | 1 | 12 | - | 1,994.32 | 0.067438 | 824 | 956 | 0.002115 | 🟢 medium — moderately distinctive | — |
| 920 | **sariputra** | 1 | 9 | - | 1,495.74 | 0.049153 | 1,065 | 759 | 0.002110 | 🟢 medium — moderately distinctive | — |
| 921 | **difficulty** | 1 | 17 | - | 2,059.43 | 0.074646 | 793 | 1,011 | 0.002106 | 🟢 medium — moderately distinctive | — |
| 922 | **superior** | 1 | 14 | - | 1,808.24 | 0.060682 | 908 | 873 | 0.002105 | 🟢 medium — moderately distinctive | — |
| 923 | **rise** | 1 | 17 | - | 1,070.81 | 0.040533 | 1,397 | 645 | 0.002105 | 🟢 medium — moderately distinctive | — |
| 924 | **forth** | 1 | 22 | - | 3,502.85 | - | 446 | - | 0.002101 | 🟡 high — specialist register | — |
| 925 | **motivation** | 1 | 12 | - | 1,910.65 | 0.067151 | 847 | 943 | 0.002100 | 🟢 medium — moderately distinctive | — |
| 926 | **discord** | 1 | 12 | - | 1,910.65 | 0.067037 | 849 | 941 | 0.002099 | 🟢 medium — moderately distinctive | — |
| 927 | **road** | 1 | 14 | - | 1,768.82 | 0.060399 | 921 | 868 | 0.002097 | 🟢 medium — moderately distinctive | — |
| 928 | **ephemeral hell** | 2 | 10 | 0.713 | - | 0.023269 | - | 447 | 0.002097 | - | — |
| 929 | **involve** | 1 | 11 | - | 1,339.77 | 0.047152 | 1,144 | 733 | 0.002092 | 🟢 medium — moderately distinctive | — |
| 930 | **patron** | 1 | 12 | - | 1,994.32 | 0.073269 | 820 | 991 | 0.002088 | 🟢 medium — moderately distinctive | — |
| 931 | **attendant** | 1 | 12 | - | 1,994.32 | 0.073427 | 819 | 993 | 0.002087 | 🟢 medium — moderately distinctive | — |
| 932 | **bring buddhahood** | 2 | 3 | 0.391 | - | 0.023706 | - | 450 | 0.002085 | - | — |
| 933 | **forest** | 1 | 15 | - | 1,922.55 | 0.069733 | 840 | 975 | 0.002077 | 🟢 medium — moderately distinctive | — |
| 934 | **reign** | 1 | 12 | - | 1,850.82 | 0.067031 | 870 | 940 | 0.002075 | 🟢 medium — moderately distinctive | — |
| 935 | **beast** | 1 | 13 | - | 2,160.51 | 0.087813 | 756 | 1,118 | 0.002074 | 🟢 medium — moderately distinctive | — |
| 936 | **arrow** | 1 | 14 | - | 2,229.09 | 0.097243 | 725 | 1,190 | 0.002074 | 🟢 medium — moderately distinctive | — |
| 937 | **along** | 1 | 36 | - | 3,479.19 | - | 454 | - | 0.002070 | 🟡 high — specialist register | — |
| 938 | **translator** | 1 | 13 | - | 2,160.51 | 0.090008 | 757 | 1,123 | 0.002069 | 🟢 medium — moderately distinctive | — |
| 939 | **robe** | 1 | 13 | - | 2,160.51 | 0.088063 | 761 | 1,119 | 0.002066 | 🟢 medium — moderately distinctive | — |
| 940 | **position** | 1 | 17 | - | 1,410.91 | 0.050057 | 1,113 | 765 | 0.002065 | 🟢 medium — moderately distinctive | — |
| 941 | **east** | 1 | 14 | - | 1,251.03 | 0.046253 | 1,227 | 717 | 0.002064 | 🟢 medium — moderately distinctive | — |
| 942 | **false** | 1 | 13 | - | 1,739.52 | 0.061436 | 926 | 893 | 0.002064 | 🟢 medium — moderately distinctive | — |
| 943 | **believe** | 1 | 21 | - | 1,896.46 | 0.070206 | 852 | 976 | 0.002062 | 🟢 medium — moderately distinctive | — |
| 944 | **wear** | 1 | 13 | - | 1,913.71 | 0.072407 | 846 | 985 | 0.002061 | 🟢 medium — moderately distinctive | — |
| 945 | **empty** | 1 | 24 | - | 3,468.89 | - | 457 | - | 0.002059 | 🟡 high — specialist register | — |
| 946 | **return** | 1 | 16 | - | 1,398.73 | 0.050426 | 1,120 | 769 | 0.002054 | 🟢 medium — moderately distinctive | — |
| 947 | **aspiration** | 1 | 12 | - | 1,994.32 | 0.081174 | 812 | 1,051 | 0.002047 | 🟢 medium — moderately distinctive | ~ |
| 948 | **lived** | 1 | 25 | - | 3,417.61 | - | 461 | - | 0.002044 | 🟡 high — specialist register | — |
| 949 | **substance** | 1 | 14 | - | 2,105.15 | 0.087473 | 779 | 1,117 | 0.002042 | 🟢 medium — moderately distinctive | ~ |
| 950 | **training** | 1 | 26 | - | 3,414.56 | - | 462 | - | 0.002040 | 🟡 high — specialist register | ~ |
| 951 | **field** | 1 | 19 | - | 1,873.91 | 0.073309 | 858 | 992 | 0.002040 | 🟢 medium — moderately distinctive | ~ |
| 952 | **foundation** | 1 | 13 | - | 1,601.40 | 0.059855 | 993 | 863 | 0.002033 | 🟢 medium — moderately distinctive | — |
| 953 | **female** | 1 | 12 | - | 1,804.42 | 0.066672 | 911 | 937 | 0.002033 | 🟢 medium — moderately distinctive | — |
| 954 | **mandala offering** | 2 | 6 | 0.452 | - | 0.024477 | - | 464 | 0.002033 | - | ~ |
| 955 | **section** | 1 | 14 | - | 1,626.21 | 0.060601 | 985 | 871 | 0.002031 | 🟢 medium — moderately distinctive | — |
| 956 | **line** | 1 | 19 | - | 1,547.23 | 0.056530 | 1,018 | 847 | 0.002030 | 🟢 medium — moderately distinctive | — |
| 957 | **spontaneously** | 1 | 11 | - | 1,828.12 | 0.067570 | 893 | 960 | 0.002030 | 🟢 medium — moderately distinctive | — |
| 958 | **within** | 1 | 43 | - | 3,407.38 | - | 465 | - | 0.002029 | 🟡 high — specialist register | — |
| 959 | **advice** | 1 | 12 | - | 1,590.30 | 0.060133 | 1,000 | 865 | 0.002024 | 🟢 medium — moderately distinctive | — |
| 960 | **sorrow** | 1 | 13 | - | 2,160.51 | 0.098663 | 755 | 1,197 | 0.002023 | 🟢 medium — moderately distinctive | — |
| 961 | **since** | 1 | 52 | - | 3,385.50 | - | 467 | - | 0.002022 | 🟡 high — specialist register | — |
| 962 | **read** | 1 | 13 | - | 1,654.03 | 0.061197 | 980 | 885 | 0.002020 | 🟢 medium — moderately distinctive | — |
| 963 | **learned** | 1 | 24 | - | 3,364.37 | - | 468 | - | 0.002018 | 🟡 high — specialist register | — |
| 964 | **trisong detsen** | 2 | 8 | 0.988 | - | 0.024685 | - | 468 | 0.002018 | - | ✓ ཁྲི་སྲོང་སྡེའུ་བཙན |
| 965 | **throughout** | 1 | 32 | - | 3,356.26 | - | 469 | - | 0.002015 | 🟡 high — specialist register | — |
| 966 | **change** | 1 | 17 | - | 1,316.65 | 0.049612 | 1,193 | 762 | 0.002015 | 🟢 medium — moderately distinctive | — |
| 967 | **warm** | 1 | 13 | - | 1,707.28 | 0.066630 | 932 | 936 | 0.002012 | 🟢 medium — moderately distinctive | — |
| 968 | **assembly** | 1 | 13 | - | 1,757.55 | 0.067389 | 923 | 950 | 0.002007 | 🟢 medium — moderately distinctive | — |
| 969 | **terrible** | 1 | 11 | - | 1,828.72 | 0.074420 | 878 | 1,004 | 0.002006 | 🟢 medium — moderately distinctive | — |
| 970 | **butter** | 1 | 13 | - | 1,757.55 | 0.067405 | 924 | 951 | 0.002005 | 🟢 medium — moderately distinctive | — |
| 971 | **illness** | 1 | 14 | - | 2,060.92 | 0.093633 | 790 | 1,147 | 0.002005 | 🟢 medium — moderately distinctive | — |
| 972 | **misconduct** | 1 | 11 | - | 1,828.72 | 0.074336 | 881 | 1,002 | 0.002004 | 🟢 medium — moderately distinctive | — |
| 973 | **negative act** | 2 | 6 | 0.404 | - | 0.025015 | - | 472 | 0.002004 | - | — |
| 974 | **lamp** | 1 | 13 | - | 2,160.51 | 0.103287 | 760 | 1,215 | 0.002004 | 🟢 medium — moderately distinctive | — |
| 975 | **golden** | 1 | 12 | - | 1,461.57 | 0.055648 | 1,093 | 822 | 0.002001 | 🟢 medium — moderately distinctive | — |
| 976 | **beauty** | 1 | 10 | - | 1,445.37 | 0.055430 | 1,102 | 817 | 0.002001 | 🟢 medium — moderately distinctive | — |
| 977 | **saw** | 1 | 34 | - | 3,329.97 | - | 473 | - | 0.002001 | 🟡 high — specialist register | — |
| 978 | **milk** | 1 | 12 | - | 1,575.95 | 0.061101 | 1,009 | 879 | 0.002000 | 🟢 medium — moderately distinctive | — |
| 979 | **langri thangpa** | 2 | 7 | 0.973 | - | 0.025087 | - | 474 | 0.001997 | - | ~ |
| 980 | **violation** | 1 | 14 | - | 1,822.95 | 0.071689 | 905 | 981 | 0.001997 | 🟢 medium — moderately distinctive | — |
| 981 | **arhat** | 1 | 9 | - | 1,495.74 | 0.056685 | 1,058 | 848 | 0.001996 | 🟢 medium — moderately distinctive | ✓ དགྲ་བཅོམ་པ |
| 982 | **impure** | 1 | 11 | - | 1,828.12 | 0.074608 | 887 | 1,007 | 0.001993 | 🟢 medium — moderately distinctive | — |
| 983 | **cho practice** | 2 | 3 | 0.405 | - | 0.025117 | - | 476 | 0.001990 | - | — |
| 984 | **physically** | 1 | 11 | - | 1,828.12 | 0.074608 | 890 | 1,008 | 0.001989 | 🟢 medium — moderately distinctive | — |
| 985 | **trisong** | 1 | 8 | - | 1,329.54 | 0.052034 | 1,162 | 795 | 0.001988 | 🟢 medium — moderately distinctive | ~ |
| 986 | **rely** | 1 | 13 | - | 1,722.83 | 0.067782 | 930 | 964 | 0.001987 | 🟢 medium — moderately distinctive | — |
| 987 | **chatter** | 1 | 11 | - | 1,828.12 | 0.074360 | 899 | 1,003 | 0.001983 | 🟢 medium — moderately distinctive | — |
| 988 | **reciting** | 1 | 20 | - | 3,323.86 | - | 478 | - | 0.001983 | 🟡 high — specialist register | — |
| 989 | **ignorance** | 1 | 11 | - | 1,828.12 | 0.074518 | 898 | 1,006 | 0.001982 | 🟢 medium — moderately distinctive | — |
| 990 | **goe** | 1 | 20 | - | 3,323.86 | - | 479 | - | 0.001980 | 🟡 high — specialist register | — |
| 991 | **village** | 1 | 12 | - | 1,850.82 | 0.080235 | 869 | 1,048 | 0.001979 | 🟢 medium — moderately distinctive | — |
| 992 | **maitreya** | 1 | 8 | - | 1,329.54 | 0.052242 | 1,170 | 798 | 0.001979 | 🟢 medium — moderately distinctive | ✓ བྱམས་པ |
| 993 | **prajnaparamita** | 1 | 8 | - | 1,329.54 | 0.051658 | 1,187 | 790 | 0.001978 | 🟢 medium — moderately distinctive | — |
| 994 | **representation** | 1 | 15 | - | 1,953.16 | 0.085825 | 833 | 1,106 | 0.001977 | 🟢 medium — moderately distinctive | — |
| 995 | **dying** | 1 | 20 | - | 3,323.86 | - | 480 | - | 0.001976 | 🟡 high — specialist register | — |
| 996 | **knife** | 1 | 11 | - | 1,828.12 | 0.074716 | 897 | 1,014 | 0.001976 | 🟢 medium — moderately distinctive | — |
| 997 | **vital** | 1 | 13 | - | 1,503.88 | 0.061399 | 1,027 | 888 | 0.001975 | 🟢 medium — moderately distinctive | — |
| 998 | **geshe ben** | 2 | 4 | 0.684 | - | 0.025468 | - | 481 | 0.001973 | - | — |
| 999 | **examine** | 1 | 13 | - | 1,631.48 | 0.066104 | 984 | 930 | 0.001968 | 🟢 medium — moderately distinctive | — |
| 1000 | **langri** | 1 | 8 | - | 1,329.54 | 0.052394 | 1,183 | 800 | 0.001967 | 🟢 medium — moderately distinctive | ~ |
| 1001 | **slight** | 1 | 3 | - | 341.71 | 0.031764 | 2,968 | 551 | 0.001967 | 🔵 low — common in general English | — |
| 1002 | **impartiality** | 1 | 11 | - | 1,828.12 | 0.074795 | 903 | 1,018 | 0.001966 | 🟢 medium — moderately distinctive | — |
| 1003 | **ourselve** | 1 | 20 | - | 3,323.86 | - | 483 | - | 0.001966 | 🟡 high — specialist register | — |
| 1004 | **padma** | 1 | 8 | - | 1,329.54 | 0.052722 | 1,188 | 803 | 0.001960 | 🟢 medium — moderately distinctive | ✓ པདྨ |
| 1005 | **above** | 1 | 42 | - | 3,295.27 | - | 485 | - | 0.001959 | 🟡 high — specialist register | — |
| 1006 | **mindfulness** | 1 | 11 | - | 1,828.12 | 0.075027 | 901 | 1,029 | 0.001959 | 🟢 medium — moderately distinctive | — |
| 1007 | **lama ngokpa** | 2 | 6 | 0.766 | - | 0.025651 | - | 486 | 0.001956 | - | — |
| 1008 | **accept** | 1 | 14 | - | 1,355.21 | 0.055993 | 1,137 | 834 | 0.001954 | 🟢 medium — moderately distinctive | — |
| 1009 | **individual** | 1 | 14 | - | 1,572.07 | 0.065000 | 1,010 | 922 | 0.001953 | 🟢 medium — moderately distinctive | — |
| 1010 | **drop** | 1 | 18 | - | 1,431.54 | 0.057167 | 1,110 | 852 | 0.001951 | 🟢 medium — moderately distinctive | — |
| 1011 | **limb** | 1 | 11 | - | 1,828.12 | 0.081189 | 894 | 1,052 | 0.001947 | 🟢 medium — moderately distinctive | — |
| 1012 | **better** | 1 | 38 | - | 3,265.28 | - | 489 | - | 0.001946 | 🟡 high — specialist register | — |
| 1013 | **virtue** | 1 | 12 | - | 1,994.97 | 0.101009 | 807 | 1,206 | 0.001943 | 🟢 medium — moderately distinctive | — |
| 1014 | **vajra family** | 2 | 3 | 0.467 | - | 0.026132 | - | 490 | 0.001943 | - | — |
| 1015 | **sravaka** | 1 | 12 | - | 1,994.32 | 0.096835 | 818 | 1,188 | 0.001940 | 🟢 medium — moderately distinctive | — |
| 1016 | **misdeed** | 1 | 11 | - | 1,828.12 | 0.082485 | 895 | 1,060 | 0.001940 | 🟢 medium — moderately distinctive | — |
| 1017 | **obey** | 1 | 11 | - | 1,828.12 | 0.082087 | 900 | 1,055 | 0.001939 | 🟢 medium — moderately distinctive | — |
| 1018 | **sole** | 1 | 14 | - | 1,873.33 | 0.087170 | 859 | 1,116 | 0.001938 | 🟢 medium — moderately distinctive | — |
| 1019 | **although** | 1 | 40 | - | 3,204.85 | - | 493 | - | 0.001933 | 🟡 high — specialist register | — |
| 1020 | **detail** | 1 | 15 | - | 1,847.77 | 0.086285 | 872 | 1,109 | 0.001928 | 🟢 medium — moderately distinctive | — |
| 1021 | **purity** | 1 | 11 | - | 1,589.91 | 0.067411 | 1,006 | 952 | 0.001926 | 🟢 medium — moderately distinctive | ~ |
| 1022 | **carry** | 1 | 14 | - | 1,486.61 | 0.061427 | 1,083 | 892 | 0.001925 | 🟢 medium — moderately distinctive | — |
| 1023 | **vigilance** | 1 | 11 | - | 1,696.59 | 0.074979 | 935 | 1,028 | 0.001924 | 🟢 medium — moderately distinctive | — |
| 1024 | **run** | 1 | 16 | - | 1,623.59 | 0.068970 | 986 | 974 | 0.001923 | 🟢 medium — moderately distinctive | — |
| 1025 | **constant** | 1 | 12 | - | 1,538.04 | 0.067073 | 1,023 | 942 | 0.001921 | 🟢 medium — moderately distinctive | — |
| 1026 | **burn** | 1 | 10 | - | 1,661.93 | 0.074135 | 965 | 1,000 | 0.001919 | 🟢 medium — moderately distinctive | — |
| 1027 | **cave** | 1 | 10 | - | 1,661.93 | 0.074643 | 958 | 1,010 | 0.001917 | 🟢 medium — moderately distinctive | — |
| 1028 | **filled** | 1 | 22 | - | 3,179.82 | - | 499 | - | 0.001913 | 🟡 high — specialist register | — |
| 1029 | **tooth** | 1 | 13 | - | 2,005.06 | 0.107960 | 805 | 1,266 | 0.001910 | 🟢 medium — moderately distinctive | — |
| 1030 | **accumulated** | 1 | 26 | - | 3,166.73 | - | 501 | - | 0.001907 | 🟡 high — specialist register | — |
| 1031 | **pot** | 1 | 19 | - | 3,158.70 | - | 503 | - | 0.001901 | 🟡 high — specialist register | — |
| 1032 | **debt** | 1 | 16 | - | 1,169.52 | 0.054695 | 1,270 | 811 | 0.001900 | 🟢 medium — moderately distinctive | — |
| 1033 | **maudgalyayana** | 1 | 8 | - | 1,329.54 | 0.058914 | 1,176 | 857 | 0.001900 | 🟢 medium — moderately distinctive | ✓ མོའུ་འགལ་གྱི་བུ |
| 1034 | **finger** | 1 | 11 | - | 1,828.72 | 0.092690 | 882 | 1,135 | 0.001898 | 🟢 medium — moderately distinctive | — |
| 1035 | **received** | 1 | 39 | - | 3,158.41 | - | 504 | - | 0.001897 | 🟡 high — specialist register | — |
| 1036 | **dodrup chen rinpoche** | 3 | 3 | 0.860 | - | 0.027255 | - | 504 | 0.001897 | - | — |
| 1037 | **disease** | 1 | 12 | - | 1,446.16 | 0.062788 | 1,098 | 909 | 0.001896 | 🟢 medium — moderately distinctive | — |
| 1038 | **princess** | 1 | 10 | - | 1,661.93 | 0.075871 | 959 | 1,035 | 0.001895 | 🟢 medium — moderately distinctive | — |
| 1039 | **later** | 1 | 40 | - | 3,158.31 | - | 505 | - | 0.001894 | 🟡 high — specialist register | — |
| 1040 | **concern** | 1 | 18 | - | 1,590.53 | 0.073707 | 999 | 995 | 0.001892 | 🟢 medium — moderately distinctive | — |
| 1041 | **tongue** | 1 | 12 | - | 1,910.65 | 0.101726 | 848 | 1,210 | 0.001889 | 🟢 medium — moderately distinctive | — |
| 1042 | **mandala base** | 2 | 10 | 0.754 | - | 0.027775 | - | 507 | 0.001888 | - | — |
| 1043 | **vase** | 1 | 10 | - | 1,661.93 | 0.074978 | 973 | 1,027 | 0.001888 | 🟢 medium — moderately distinctive | ~ |
| 1044 | **karmic effect** | 2 | 8 | 0.595 | - | 0.027992 | - | 508 | 0.001885 | - | ~ |
| 1045 | **manifestation** | 1 | 11 | - | 1,828.12 | 0.091940 | 902 | 1,131 | 0.001879 | 🟢 medium — moderately distinctive | — |
| 1046 | **tendency** | 1 | 12 | - | 1,622.36 | 0.074883 | 987 | 1,024 | 0.001878 | 🟢 medium — moderately distinctive | — |
| 1047 | **consist** | 1 | 14 | - | 1,794.38 | 0.086916 | 916 | 1,113 | 0.001877 | 🟢 medium — moderately distinctive | — |
| 1048 | **rid** | 1 | 11 | - | 1,619.29 | 0.074936 | 988 | 1,025 | 0.001876 | 🟢 medium — moderately distinctive | — |
| 1049 | **ly** | 1 | 19 | - | 3,157.67 | - | 511 | - | 0.001876 | 🟡 high — specialist register | ~ |
| 1050 | **grass** | 1 | 10 | - | 1,662.47 | 0.083143 | 949 | 1,071 | 0.001875 | 🟢 medium — moderately distinctive | ~ |
| 1051 | **lifespan** | 1 | 10 | - | 1,661.93 | 0.082434 | 961 | 1,058 | 0.001874 | 🟢 medium — moderately distinctive | — |
| 1052 | **mistake** | 1 | 13 | - | 1,798.63 | 0.088559 | 915 | 1,120 | 0.001873 | 🟢 medium — moderately distinctive | — |
| 1053 | **manjusrimitra** | 1 | 8 | - | 1,329.54 | 0.060847 | 1,190 | 874 | 0.001871 | 🟢 medium — moderately distinctive | — |
| 1054 | **monastic** | 1 | 10 | - | 1,661.93 | 0.082977 | 960 | 1,065 | 0.001869 | 🟢 medium — moderately distinctive | — |
| 1055 | **money** | 1 | 15 | - | 1,059.46 | 0.051416 | 1,401 | 786 | 0.001866 | 🟢 medium — moderately distinctive | — |
| 1056 | **treat** | 1 | 10 | - | 1,503.68 | 0.073961 | 1,030 | 997 | 0.001864 | 🟢 medium — moderately distinctive | — |
| 1057 | **equally** | 1 | 12 | - | 1,461.57 | 0.067265 | 1,092 | 947 | 0.001861 | 🟢 medium — moderately distinctive | — |
| 1058 | **using** | 1 | 31 | - | 3,108.63 | - | 516 | - | 0.001861 | 🟡 high — specialist register | — |
| 1059 | **noble sangha** | 2 | 5 | 0.655 | - | 0.028784 | - | 516 | 0.001861 | - | ~ |
| 1060 | **clairvoyance** | 1 | 10 | - | 1,661.93 | 0.083089 | 967 | 1,068 | 0.001860 | 🟢 medium — moderately distinctive | — |
| 1061 | **green** | 1 | 12 | - | 1,469.72 | 0.067429 | 1,090 | 953 | 0.001857 | 🟢 medium — moderately distinctive | — |
| 1062 | **disappear** | 1 | 11 | - | 1,564.45 | 0.074867 | 1,012 | 1,023 | 0.001856 | 🟢 medium — moderately distinctive | — |
| 1063 | **jealousy** | 1 | 10 | - | 1,661.93 | 0.083701 | 955 | 1,089 | 0.001856 | 🟢 medium — moderately distinctive | — |
| 1064 | **pith** | 1 | 10 | - | 1,661.93 | 0.083805 | 952 | 1,094 | 0.001855 | 🟢 medium — moderately distinctive | ~ |
| 1065 | **king prasenajit** | 2 | 3 | 0.639 | - | 0.028976 | - | 518 | 0.001854 | - | — |
| 1066 | **colour** | 1 | 12 | - | 1,734.45 | 0.090353 | 929 | 1,126 | 0.001854 | 🟢 medium — moderately distinctive | — |
| 1067 | **embodiment** | 1 | 10 | - | 1,661.93 | 0.083734 | 954 | 1,092 | 0.001854 | 🟢 medium — moderately distinctive | — |
| 1068 | **bow** | 1 | 11 | - | 1,503.75 | 0.074680 | 1,028 | 1,012 | 0.001852 | 🟢 medium — moderately distinctive | — |
| 1069 | **totally** | 1 | 12 | - | 1,478.21 | 0.067717 | 1,087 | 961 | 0.001851 | 🟢 medium — moderately distinctive | — |
| 1070 | **sight** | 1 | 11 | - | 1,399.56 | 0.066914 | 1,119 | 939 | 0.001849 | 🟢 medium — moderately distinctive | — |
| 1071 | **behind** | 1 | 30 | - | 3,082.75 | - | 520 | - | 0.001849 | 🟡 high — specialist register | — |
| 1072 | **chen rinpoche** | 2 | 3 | 0.747 | - | 0.029208 | - | 520 | 0.001849 | - | — |
| 1073 | **bound** | 1 | 19 | - | 2,454.05 | 0.235801 | 665 | 2,084 | 0.001846 | 🟢 medium — moderately distinctive | — |
| 1074 | **yidam** | 1 | 11 | - | 1,828.12 | 0.102740 | 889 | 1,212 | 0.001840 | 🟢 medium — moderately distinctive | ✓ ཡི་དམ |
| 1075 | **seek** | 1 | 13 | - | 1,134.10 | 0.055707 | 1,349 | 825 | 0.001840 | 🟢 medium — moderately distinctive | — |
| 1076 | **immeasurable** | 1 | 10 | - | 1,661.93 | 0.083800 | 970 | 1,093 | 0.001838 | 🟢 medium — moderately distinctive | — |
| 1077 | **humble** | 1 | 10 | - | 1,661.93 | 0.083819 | 969 | 1,095 | 0.001838 | 🟢 medium — moderately distinctive | — |
| 1078 | **shadow** | 1 | 11 | - | 1,589.91 | 0.081984 | 1,005 | 1,054 | 0.001837 | 🟢 medium — moderately distinctive | — |
| 1079 | **already** | 1 | 41 | - | 3,055.13 | - | 526 | - | 0.001831 | 🟡 high — specialist register | — |
| 1080 | **doctor** | 1 | 10 | - | 1,661.93 | 0.089046 | 956 | 1,122 | 0.001830 | 🟢 medium — moderately distinctive | — |
| 1081 | **region** | 1 | 14 | - | 1,444.92 | 0.068956 | 1,104 | 973 | 0.001827 | 🟢 medium — moderately distinctive | — |
| 1082 | **journey** | 1 | 10 | - | 1,662.47 | 0.092930 | 950 | 1,136 | 0.001826 | 🟢 medium — moderately distinctive | — |
| 1083 | **gold** | 1 | 13 | - | 1,096.19 | 0.055737 | 1,377 | 827 | 0.001823 | 🟢 medium — moderately distinctive | — |
| 1084 | **full** | 1 | 42 | - | 3,024.27 | - | 529 | - | 0.001822 | 🟡 high — specialist register | ~ |
| 1085 | **chekawa** | 1 | 8 | - | 1,329.54 | 0.064999 | 1,189 | 921 | 0.001820 | 🟢 medium — moderately distinctive | ~ |
| 1086 | **told** | 1 | 54 | - | 3,008.36 | - | 530 | - | 0.001819 | 🟡 high — specialist register | — |
| 1087 | **indispensable** | 1 | 10 | - | 1,592.21 | 0.083682 | 996 | 1,088 | 0.001818 | 🟢 medium — moderately distinctive | — |
| 1088 | **traveller** | 1 | 10 | - | 1,661.93 | 0.092444 | 963 | 1,134 | 0.001815 | 🟢 medium — moderately distinctive | — |
| 1089 | **symbol** | 1 | 13 | - | 1,777.16 | 0.100175 | 919 | 1,203 | 0.001813 | 🟢 medium — moderately distinctive | ~ |
| 1090 | **songtsen** | 1 | 7 | - | 1,163.35 | 0.060538 | 1,299 | 869 | 0.001812 | 🟢 medium — moderately distinctive | ~ |
| 1091 | **gampo** | 1 | 7 | - | 1,163.35 | 0.060557 | 1,300 | 870 | 0.001811 | 🟢 medium — moderately distinctive | ~ |
| 1092 | **continually** | 1 | 10 | - | 1,503.68 | 0.082578 | 1,029 | 1,061 | 0.001810 | 🟢 medium — moderately distinctive | — |
| 1093 | **sincerely** | 1 | 10 | - | 1,592.21 | 0.083823 | 998 | 1,096 | 0.001810 | 🟢 medium — moderately distinctive | — |
| 1094 | **represent** | 1 | 10 | - | 1,115.37 | 0.056419 | 1,360 | 845 | 0.001809 | 🟢 medium — moderately distinctive | — |
| 1095 | **establish** | 1 | 11 | - | 1,211.34 | 0.061699 | 1,249 | 900 | 0.001806 | 🟢 medium — moderately distinctive | — |
| 1096 | **throat** | 1 | 10 | - | 1,661.93 | 0.093227 | 971 | 1,139 | 0.001804 | 🟢 medium — moderately distinctive | — |
| 1097 | **length** | 1 | 11 | - | 1,457.78 | 0.074421 | 1,097 | 1,005 | 0.001803 | 🟢 medium — moderately distinctive | — |
| 1098 | **virtuous** | 1 | 9 | - | 1,495.74 | 0.075500 | 1,066 | 1,033 | 0.001803 | 🟢 medium — moderately distinctive | — |
| 1099 | **purified** | 1 | 18 | - | 2,992.45 | - | 536 | - | 0.001802 | 🟢 medium — moderately distinctive | — |
| 1100 | **catch** | 1 | 7 | - | 1,052.58 | 0.055955 | 1,406 | 833 | 0.001802 | 🟢 medium — moderately distinctive | — |
| 1101 | **immaculate** | 1 | 9 | - | 1,495.74 | 0.075919 | 1,073 | 1,036 | 0.001795 | 🟢 medium — moderately distinctive | — |
| 1102 | **lying** | 1 | 18 | - | 2,992.45 | - | 539 | - | 0.001794 | 🟢 medium — moderately distinctive | — |
| 1103 | **songtsen gampo** | 2 | 5 | 0.967 | - | 0.031281 | - | 539 | 0.001794 | - | ✓ སྲོང་བཙན་སྒམ་པོ |
| 1104 | **skilled** | 1 | 9 | - | 1,496.23 | 0.083368 | 1,034 | 1,078 | 0.001793 | 🟢 medium — moderately distinctive | — |
| 1105 | **previous** | 1 | 14 | - | 1,026.72 | 0.056022 | 1,422 | 835 | 0.001792 | 🟢 medium — moderately distinctive | — |
| 1106 | **wherever** | 1 | 18 | - | 2,991.47 | - | 541 | - | 0.001788 | 🟢 medium — moderately distinctive | — |
| 1107 | **preliminary practice** | 2 | 7 | 0.514 | - | 0.031378 | - | 541 | 0.001788 | - | — |
| 1108 | **dry** | 1 | 12 | - | 1,302.01 | 0.067268 | 1,199 | 948 | 0.001786 | 🟢 medium — moderately distinctive | — |
| 1109 | **eighty thousand** | 2 | 9 | 0.705 | - | 0.031406 | - | 542 | 0.001786 | - | ~ |
| 1110 | **baby** | 1 | 11 | - | 1,619.29 | 0.093562 | 989 | 1,144 | 0.001784 | 🟢 medium — moderately distinctive | — |
| 1111 | **depend** | 1 | 14 | - | 1,556.41 | 0.087087 | 1,017 | 1,114 | 0.001780 | 🟢 medium — moderately distinctive | — |
| 1112 | **principle** | 1 | 12 | - | 1,109.98 | 0.060295 | 1,371 | 866 | 0.001779 | 🟢 medium — moderately distinctive | ~ |
| 1113 | **padmasambhava** | 1 | 7 | - | 1,163.35 | 0.062531 | 1,289 | 906 | 0.001776 | 🟢 medium — moderately distinctive | ~ |
| 1114 | **period** | 1 | 17 | - | 1,139.52 | 0.061178 | 1,340 | 882 | 0.001776 | 🟢 medium — moderately distinctive | — |
| 1115 | **ornament** | 1 | 10 | - | 1,661.93 | 0.096875 | 966 | 1,189 | 0.001775 | 🟢 medium — moderately distinctive | — |
| 1116 | **shoulder** | 1 | 11 | - | 1,828.72 | 0.123066 | 880 | 1,347 | 0.001775 | 🟢 medium — moderately distinctive | — |
| 1117 | **continue** | 1 | 15 | - | 1,076.17 | 0.059725 | 1,394 | 862 | 0.001772 | 🟢 medium — moderately distinctive | — |
| 1118 | **avalokitesvara** | 1 | 7 | - | 1,163.35 | 0.063944 | 1,285 | 913 | 0.001771 | 🟢 medium — moderately distinctive | — |
| 1119 | **vinaya** | 1 | 7 | - | 1,163.35 | 0.062733 | 1,297 | 908 | 0.001770 | 🟢 medium — moderately distinctive | ✓ འདུལ་བ |
| 1120 | **ceremony** | 1 | 12 | - | 1,804.42 | 0.108364 | 913 | 1,292 | 0.001767 | 🟢 medium — moderately distinctive | — |
| 1121 | **behave** | 1 | 10 | - | 1,661.93 | 0.104226 | 957 | 1,219 | 0.001765 | 🟢 medium — moderately distinctive | — |
| 1122 | **south** | 1 | 12 | - | 942.16 | 0.055401 | 1,546 | 816 | 0.001764 | 🟢 medium — moderately distinctive | — |
| 1123 | **lhodrak** | 1 | 7 | - | 1,163.35 | 0.062478 | 1,322 | 902 | 0.001763 | 🟢 medium — moderately distinctive | — |
| 1124 | **entrust** | 1 | 9 | - | 1,495.74 | 0.083399 | 1,075 | 1,079 | 0.001759 | 🟢 medium — moderately distinctive | — |
| 1125 | **process** | 1 | 13 | - | 1,260.47 | 0.067733 | 1,224 | 962 | 0.001757 | 🟢 medium — moderately distinctive | ~ |
| 1126 | **separate** | 1 | 12 | - | 1,238.50 | 0.067561 | 1,233 | 959 | 0.001755 | 🟢 medium — moderately distinctive | — |
| 1127 | **perfect place** | 2 | 3 | 0.319 | - | 0.031858 | - | 554 | 0.001753 | - | — |
| 1128 | **explained** | 1 | 25 | - | 2,928.71 | - | 555 | - | 0.001750 | 🟢 medium — moderately distinctive | — |
| 1129 | **hermitage** | 1 | 10 | - | 1,661.93 | 0.104750 | 972 | 1,220 | 0.001750 | 🟢 medium — moderately distinctive | — |
| 1130 | **vimalamitra** | 1 | 7 | - | 1,163.35 | 0.063954 | 1,323 | 914 | 0.001750 | 🟢 medium — moderately distinctive | ✓ དྲི་མེད་བཤེས་གཉེན |
| 1131 | **strive** | 1 | 10 | - | 1,422.23 | 0.082330 | 1,112 | 1,057 | 0.001748 | 🟢 medium — moderately distinctive | — |
| 1132 | **corpse** | 1 | 9 | - | 1,495.74 | 0.086287 | 1,060 | 1,110 | 0.001748 | 🟢 medium — moderately distinctive | — |
| 1133 | **katyayana** | 1 | 7 | - | 1,163.35 | 0.065110 | 1,310 | 924 | 0.001746 | 🟢 medium — moderately distinctive | ✓ |
| 1134 | **deaf** | 1 | 9 | - | 1,496.23 | 0.093589 | 1,033 | 1,145 | 0.001745 | 🟢 medium — moderately distinctive | — |
| 1135 | **slaughter** | 1 | 7 | - | 884.41 | 0.055612 | 1,590 | 820 | 0.001742 | 🟢 medium — moderately distinctive | — |
| 1136 | **phenomena** | 1 | 9 | - | 1,496.23 | 0.093828 | 1,031 | 1,151 | 0.001742 | 🟢 medium — moderately distinctive | ~ |
| 1137 | **day geshe** | 2 | 3 | 0.400 | - | 0.032187 | - | 559 | 0.001740 | - | — |
| 1138 | **saying** | 1 | 35 | - | 2,887.65 | - | 560 | - | 0.001737 | 🟢 medium — moderately distinctive | — |
| 1139 | **peerless dagpo** | 2 | 9 | 0.850 | - | 0.032245 | - | 560 | 0.001737 | - | — |
| 1140 | **try** | 1 | 30 | - | 2,885.46 | - | 561 | - | 0.001735 | 🟢 medium — moderately distinctive | — |
| 1141 | **exhaust** | 1 | 6 | - | 902.21 | 0.055829 | 1,585 | 829 | 0.001733 | 🟢 medium — moderately distinctive | — |
| 1142 | **treasury** | 1 | 9 | - | 722.73 | 0.049193 | 1,891 | 760 | 0.001732 | 🟢 medium — moderately distinctive | — |
| 1143 | **surround** | 1 | 2 | - | 332.39 | 0.038386 | 3,601 | 626 | 0.001731 | 🔵 low — common in general English | — |
| 1144 | **hate** | 1 | 9 | - | 1,496.23 | 0.094408 | 1,042 | 1,164 | 0.001724 | 🟢 medium — moderately distinctive | — |
| 1145 | **seem** | 1 | 25 | - | 2,869.26 | - | 565 | - | 0.001724 | 🟢 medium — moderately distinctive | — |
| 1146 | **ultimate torment** | 2 | 7 | 0.739 | - | 0.032727 | - | 565 | 0.001724 | - | — |
| 1147 | **remorse** | 1 | 9 | - | 1,495.74 | 0.093866 | 1,054 | 1,152 | 0.001723 | 🟢 medium — moderately distinctive | — |
| 1148 | **sublime path** | 2 | 3 | 0.391 | - | 0.032878 | - | 566 | 0.001722 | - | ~ |
| 1149 | **holy** | 1 | 9 | - | 1,495.74 | 0.093902 | 1,056 | 1,153 | 0.001720 | 🟢 medium — moderately distinctive | — |
| 1150 | **no-one** | 1 | 19 | - | 2,856.99 | - | 567 | - | 0.001719 | 🟢 medium — moderately distinctive | — |
| 1151 | **retribution** | 1 | 9 | - | 1,496.23 | 0.094738 | 1,039 | 1,178 | 0.001718 | 🟢 medium — moderately distinctive | ~ |
| 1152 | **longchenpa** | 1 | 7 | - | 1,163.35 | 0.068186 | 1,286 | 966 | 0.001718 | 🟢 medium — moderately distinctive | ✓ ཀློང་ཆེན་རབ་འབྱམས་པ |
| 1153 | **surrounded** | 1 | 19 | - | 2,856.99 | - | 568 | - | 0.001717 | 🟢 medium — moderately distinctive | — |
| 1154 | **meritorious** | 1 | 9 | - | 1,495.74 | 0.094567 | 1,045 | 1,172 | 0.001717 | 🟢 medium — moderately distinctive | — |
| 1155 | **comfortable** | 1 | 10 | - | 1,367.04 | 0.083399 | 1,134 | 1,080 | 0.001715 | 🟢 medium — moderately distinctive | — |
| 1156 | **auspicious** | 1 | 9 | - | 1,496.23 | 0.094813 | 1,040 | 1,182 | 0.001714 | 🟢 medium — moderately distinctive | ~ |
| 1157 | **arrived** | 1 | 22 | - | 2,841.53 | - | 569 | - | 0.001714 | 🟢 medium — moderately distinctive | — |
| 1158 | **attain perfect** | 2 | 6 | 0.504 | - | 0.033069 | - | 569 | 0.001714 | - | — |
| 1159 | **increase** | 1 | 14 | - | 857.70 | 0.056027 | 1,615 | 836 | 0.001713 | 🟢 medium — moderately distinctive | ~ |
| 1160 | **authentic path** | 2 | 5 | 0.459 | - | 0.033131 | - | 571 | 0.001709 | - | — |
| 1161 | **pandita** | 1 | 11 | - | 1,828.12 | 0.137159 | 892 | 1,460 | 0.001708 | 🟢 medium — moderately distinctive | ✓ |
| 1162 | **dark kalpa** | 2 | 8 | 0.717 | - | 0.033138 | - | 572 | 0.001707 | - | — |
| 1163 | **celestial** | 1 | 9 | - | 1,495.74 | 0.094583 | 1,057 | 1,173 | 0.001706 | 🟢 medium — moderately distinctive | — |
| 1164 | **bitch** | 1 | 9 | - | 1,495.74 | 0.094532 | 1,061 | 1,169 | 0.001706 | 🟢 medium — moderately distinctive | — |
| 1165 | **medicine** | 1 | 10 | - | 1,445.37 | 0.091405 | 1,099 | 1,128 | 0.001705 | 🟢 medium — moderately distinctive | — |
| 1166 | **yellow** | 1 | 10 | - | 1,338.09 | 0.083591 | 1,146 | 1,087 | 0.001701 | 🟢 medium — moderately distinctive | ~ |
| 1167 | **clear light** | 2 | 7 | 0.636 | - | 0.033217 | - | 575 | 0.001699 | - | ✓ འོད་གསལ |
| 1168 | **ability** | 1 | 12 | - | 1,233.10 | 0.074737 | 1,241 | 1,015 | 0.001699 | 🟢 medium — moderately distinctive | — |
| 1169 | **solitary** | 1 | 9 | - | 1,495.74 | 0.094631 | 1,064 | 1,176 | 0.001699 | 🟢 medium — moderately distinctive | — |
| 1170 | **total** | 1 | 14 | - | 831.88 | 0.056226 | 1,637 | 842 | 0.001698 | 🟢 medium — moderately distinctive | ~ |
| 1171 | **surface** | 1 | 11 | - | 1,432.32 | 0.090363 | 1,109 | 1,127 | 0.001698 | 🟢 medium — moderately distinctive | — |
| 1172 | **property** | 1 | 12 | - | 1,173.28 | 0.074053 | 1,267 | 999 | 0.001698 | 🟢 medium — moderately distinctive | — |
| 1173 | **break** | 1 | 12 | - | 1,309.57 | 0.080544 | 1,197 | 1,049 | 0.001697 | 🟢 medium — moderately distinctive | — |
| 1174 | **sharawa** | 1 | 7 | - | 1,163.35 | 0.068039 | 1,327 | 965 | 0.001697 | 🟢 medium — moderately distinctive | ✓ ཤ་ར་བ |
| 1175 | **cry** | 1 | 8 | - | 1,329.54 | 0.083349 | 1,168 | 1,077 | 0.001694 | 🟢 medium — moderately distinctive | — |
| 1176 | **lita** | 1 | 11 | - | 1,828.12 | 0.139439 | 904 | 1,467 | 0.001692 | 🟢 medium — moderately distinctive | — |
| 1177 | **caste** | 1 | 9 | - | 1,495.74 | 0.094588 | 1,074 | 1,174 | 0.001692 | 🟢 medium — moderately distinctive | — |
| 1178 | **wander** | 1 | 9 | - | 1,496.23 | 0.106129 | 1,032 | 1,228 | 0.001692 | 🟢 medium — moderately distinctive | — |
| 1179 | **tirthikas** | 1 | - | - | - | 0.033490 | - | 578 | 0.001692 | - | — |
| 1180 | **tea** | 1 | 16 | - | 1,909.08 | 0.173215 | 850 | 1,627 | 0.001692 | 🟢 medium — moderately distinctive | — |
| 1181 | **sunak** | 1 | 6 | - | 997.16 | 0.063087 | 1,454 | 910 | 0.001691 | 🟢 medium — moderately distinctive | — |
| 1182 | **atiyoga** | 1 | 7 | - | 1,163.35 | 0.068765 | 1,329 | 970 | 0.001691 | 🟢 medium — moderately distinctive | ✓ |
| 1183 | **wood** | 1 | 11 | - | 1,294.32 | 0.081963 | 1,204 | 1,053 | 0.001690 | 🟢 medium — moderately distinctive | — |
| 1184 | **repeat** | 1 | 10 | - | 1,401.82 | 0.093251 | 1,118 | 1,140 | 0.001682 | 🟢 medium — moderately distinctive | — |
| 1185 | **eating** | 1 | 19 | - | 2,796.96 | - | 582 | - | 0.001682 | 🟢 medium — moderately distinctive | — |
| 1186 | **bind** | 1 | 3 | - | 462.71 | 0.044213 | 2,730 | 696 | 0.001681 | 🔵 low — common in general English | — |
| 1187 | **league** | 1 | 12 | - | 1,734.45 | 0.133526 | 928 | 1,436 | 0.001681 | 🟢 medium — moderately distinctive | — |
| 1188 | **unless** | 1 | 30 | - | 2,774.95 | - | 583 | - | 0.001680 | 🟢 medium — moderately distinctive | — |
| 1189 | **conviction** | 1 | 9 | - | 1,388.12 | 0.093109 | 1,127 | 1,137 | 0.001678 | 🟢 medium — moderately distinctive | — |
| 1190 | **gave** | 1 | 32 | - | 2,771.67 | - | 584 | - | 0.001677 | 🟢 medium — moderately distinctive | — |
| 1191 | **essential point** | 2 | 13 | 0.706 | - | 0.033934 | - | 584 | 0.001677 | - | ~ |
| 1192 | **solitude** | 1 | 9 | - | 1,495.74 | 0.106517 | 1,051 | 1,231 | 0.001675 | 🟢 medium — moderately distinctive | — |
| 1193 | **shoot** | 1 | 11 | - | 1,619.29 | 0.117995 | 990 | 1,328 | 0.001673 | 🟢 medium — moderately distinctive | — |
| 1194 | **evening** | 1 | 10 | - | 1,313.29 | 0.083448 | 1,195 | 1,082 | 0.001672 | 🟢 medium — moderately distinctive | — |
| 1195 | **gesture** | 1 | 10 | - | 1,383.56 | 0.093323 | 1,130 | 1,142 | 0.001672 | 🟢 medium — moderately distinctive | — |
| 1196 | **brought** | 1 | 28 | - | 2,742.33 | - | 587 | - | 0.001670 | 🟢 medium — moderately distinctive | — |
| 1197 | **following** | 1 | 36 | - | 2,724.70 | - | 589 | - | 0.001665 | 🟢 medium — moderately distinctive | — |
| 1198 | **illusion** | 1 | 9 | - | 1,432.99 | 0.094707 | 1,108 | 1,177 | 0.001665 | 🟢 medium — moderately distinctive | — |
| 1199 | **peaceful** | 1 | 9 | - | 1,388.12 | 0.094181 | 1,126 | 1,158 | 0.001664 | 🟢 medium — moderately distinctive | — |
| 1200 | **actually** | 1 | 24 | - | 2,723.67 | - | 590 | - | 0.001663 | 🟢 medium — moderately distinctive | — |
| 1201 | **pure perception** | 2 | 8 | 0.607 | - | 0.034677 | - | 590 | 0.001663 | - | ✓ དག་སྣང |
| 1202 | **next** | 1 | 40 | - | 2,712.44 | - | 591 | - | 0.001660 | 🟢 medium — moderately distinctive | — |
| 1203 | **month** | 1 | 17 | - | 1,072.72 | 0.068628 | 1,396 | 968 | 0.001660 | 🟢 medium — moderately distinctive | — |
| 1204 | **sand** | 1 | 10 | - | 1,351.96 | 0.093792 | 1,141 | 1,150 | 0.001659 | 🟢 medium — moderately distinctive | — |
| 1205 | **summer** | 1 | 11 | - | 1,125.52 | 0.073931 | 1,351 | 996 | 0.001656 | 🟢 medium — moderately distinctive | — |
| 1206 | **manner** | 1 | 10 | - | 1,263.44 | 0.083536 | 1,223 | 1,085 | 0.001653 | 🟢 medium — moderately distinctive | — |
| 1207 | **faithful** | 1 | 9 | - | 1,388.12 | 0.094756 | 1,123 | 1,179 | 0.001652 | 🟢 medium — moderately distinctive | — |
| 1208 | **stand** | 1 | 12 | - | 1,291.16 | 0.083846 | 1,208 | 1,098 | 0.001652 | 🟢 medium — moderately distinctive | — |
| 1209 | **invite** | 1 | 6 | - | 867.22 | 0.061459 | 1,605 | 894 | 0.001649 | 🟢 medium — moderately distinctive | — |
| 1210 | **ing** | 1 | 19 | - | 2,702.24 | - | 596 | - | 0.001649 | 🟢 medium — moderately distinctive | — |
| 1211 | **dakini** | 1 | 10 | - | 1,661.93 | 0.135195 | 953 | 1,453 | 0.001648 | 🟢 medium — moderately distinctive | ✓ མཁའ་འགྲོ་མ |
| 1212 | **evil spirit** | 2 | 8 | 0.565 | - | 0.035258 | - | 597 | 0.001646 | - | — |
| 1213 | **army** | 1 | 11 | - | 1,487.16 | 0.107114 | 1,081 | 1,241 | 0.001645 | 🟢 medium — moderately distinctive | — |
| 1214 | **experienced** | 1 | 21 | - | 2,691.57 | - | 598 | - | 0.001644 | 🟢 medium — moderately distinctive | — |
| 1215 | **sublime bodhicitta** | 2 | 4 | 0.440 | - | 0.035722 | - | 603 | 0.001633 | - | ~ |
| 1216 | **weak** | 1 | 11 | - | 1,103.06 | 0.074810 | 1,375 | 1,019 | 0.001624 | 🟢 medium — moderately distinctive | — |
| 1217 | **basi** | 1 | 16 | - | 2,659.09 | - | 607 | - | 0.001624 | 🟢 medium — moderately distinctive | — |
| 1218 | **link** | 1 | 10 | - | 1,199.05 | 0.083842 | 1,257 | 1,097 | 0.001624 | 🟢 medium — moderately distinctive | — |
| 1219 | **lay** | 1 | 16 | - | 1,970.95 | 0.231227 | 827 | 1,956 | 0.001623 | 🟢 medium — moderately distinctive | ~ |
| 1220 | **external** | 1 | 11 | - | 1,118.50 | 0.075072 | 1,358 | 1,031 | 0.001622 | 🟢 medium — moderately distinctive | — |
| 1221 | **ment** | 1 | 10 | - | 1,661.93 | 0.139807 | 974 | 1,470 | 0.001621 | 🟢 medium — moderately distinctive | — |
| 1222 | **hide** | 1 | 2 | - | 332.39 | 0.044473 | 3,174 | 704 | 0.001618 | 🔵 low — common in general English | — |
| 1223 | **sound** | 1 | 11 | - | 1,339.77 | 0.102770 | 1,143 | 1,213 | 0.001617 | 🟢 medium — moderately distinctive | — |
| 1224 | **nowaday** | 1 | 16 | - | 2,659.09 | - | 613 | - | 0.001610 | 🟢 medium — moderately distinctive | — |
| 1225 | **seated** | 1 | 16 | - | 2,659.09 | - | 614 | - | 0.001608 | 🟢 medium — moderately distinctive | — |
| 1226 | **total buddhahood** | 2 | 3 | 0.569 | - | 0.036841 | - | 614 | 0.001608 | - | — |
| 1227 | **trouble** | 1 | 10 | - | 1,231.84 | 0.092090 | 1,243 | 1,132 | 0.001606 | 🟢 medium — moderately distinctive | — |
| 1228 | **slip** | 1 | 9 | - | 1,245.20 | 0.093631 | 1,229 | 1,146 | 0.001605 | 🟢 medium — moderately distinctive | — |
| 1229 | **criticize** | 1 | 8 | - | 1,329.98 | 0.105987 | 1,149 | 1,227 | 0.001604 | 🟢 medium — moderately distinctive | — |
| 1230 | **none** | 1 | 22 | - | 2,651.28 | - | 616 | - | 0.001604 | 🟢 medium — moderately distinctive | — |
| 1231 | **protector amitabha** | 2 | 6 | 0.725 | - | 0.037524 | - | 617 | 0.001601 | - | ~ |
| 1232 | **itself** | 1 | 27 | - | 2,639.87 | - | 619 | - | 0.001597 | 🟢 medium — moderately distinctive | — |
| 1233 | **simple** | 1 | 9 | - | 1,245.20 | 0.094256 | 1,228 | 1,159 | 0.001597 | 🟢 medium — moderately distinctive | — |
| 1234 | **universal** | 1 | 9 | - | 1,129.49 | 0.083209 | 1,350 | 1,072 | 0.001593 | 🟢 medium — moderately distinctive | ~ |
| 1235 | **far** | 1 | 33 | - | 2,624.48 | - | 622 | - | 0.001591 | 🟢 medium — moderately distinctive | — |
| 1236 | **great sage** | 2 | 3 | 0.548 | - | 0.037785 | - | 622 | 0.001591 | - | — |
| 1237 | **request** | 1 | 11 | - | 1,105.19 | 0.082714 | 1,374 | 1,062 | 0.001589 | 🟢 medium — moderately distinctive | — |
| 1238 | **gaya** | 1 | 6 | - | 997.16 | 0.074741 | 1,457 | 1,016 | 0.001589 | 🟢 medium — moderately distinctive | — |
| 1239 | **perfectly pure** | 2 | 7 | 0.588 | - | 0.037897 | - | 623 | 0.001589 | - | — |
| 1240 | **skill** | 1 | 8 | - | 1,273.77 | 0.095410 | 1,214 | 1,185 | 0.001588 | 🟢 medium — moderately distinctive | — |
| 1241 | **bodh** | 1 | 6 | - | 997.16 | 0.074742 | 1,456 | 1,017 | 0.001588 | 🟢 medium — moderately distinctive | — |
| 1242 | **eighteen** | 1 | 8 | - | 1,329.54 | 0.106931 | 1,166 | 1,236 | 0.001587 | 🟢 medium — moderately distinctive | — |
| 1243 | **worthless** | 1 | 8 | - | 1,329.98 | 0.107567 | 1,155 | 1,249 | 0.001587 | 🟢 medium — moderately distinctive | — |
| 1244 | **hidden** | 1 | 17 | - | 2,622.00 | - | 624 | - | 0.001586 | 🟢 medium — moderately distinctive | — |
| 1245 | **goal** | 1 | 12 | - | 1,313.46 | 0.101532 | 1,194 | 1,208 | 0.001586 | 🟢 medium — moderately distinctive | ~ |
| 1246 | **term** | 1 | 15 | - | 1,271.83 | 0.094965 | 1,222 | 1,184 | 0.001584 | 🟢 medium — moderately distinctive | — |
| 1247 | **indian** | 1 | 7 | - | 813.10 | 0.062503 | 1,772 | 904 | 0.001583 | 🟢 medium — moderately distinctive | — |
| 1248 | **cross** | 1 | 10 | - | 1,193.17 | 0.093988 | 1,258 | 1,154 | 0.001582 | 🟢 medium — moderately distinctive | — |
| 1249 | **outward** | 1 | 9 | - | 1,388.12 | 0.108435 | 1,124 | 1,298 | 0.001581 | 🟢 medium — moderately distinctive | — |
| 1250 | **vidyadhara** | 1 | 11 | - | 1,828.12 | 0.216530 | 884 | 1,857 | 0.001581 | 🟢 medium — moderately distinctive | ✓ རིག་འཛིན |
| 1251 | **heavy** | 1 | 11 | - | 977.39 | 0.074015 | 1,515 | 998 | 0.001580 | 🟢 medium — moderately distinctive | — |
| 1252 | **endlessly** | 1 | 8 | - | 1,329.54 | 0.107555 | 1,167 | 1,248 | 0.001580 | 🟢 medium — moderately distinctive | — |
| 1253 | **tibetan** | 1 | 7 | - | 1,163.35 | 0.090040 | 1,301 | 1,124 | 0.001579 | 🟢 medium — moderately distinctive | — |
| 1254 | **rule** | 1 | 13 | - | 1,410.51 | 0.112965 | 1,114 | 1,318 | 0.001577 | 🟢 medium — moderately distinctive | — |
| 1255 | **torma** | 1 | 11 | - | 1,828.12 | 0.193771 | 896 | 1,823 | 0.001577 | 🟢 medium — moderately distinctive | ✓ གཏོར་མ |
| 1256 | **exist** | 1 | 10 | - | 1,291.60 | 0.102658 | 1,206 | 1,211 | 0.001577 | 🟢 medium — moderately distinctive | — |
| 1257 | **samsaric** | 1 | 8 | - | 1,329.54 | 0.107472 | 1,177 | 1,245 | 0.001575 | 🟢 medium — moderately distinctive | — |
| 1258 | **vajradhara** | 1 | 6 | - | 997.16 | 0.078378 | 1,447 | 1,041 | 0.001572 | 🟢 medium — moderately distinctive | ✓ རྡོ་རྗེ་འཆང |
| 1259 | **positive act** | 2 | 6 | 0.465 | - | 0.038682 | - | 631 | 0.001572 | - | — |
| 1260 | **endure** | 1 | 8 | - | 1,329.54 | 0.108036 | 1,160 | 1,270 | 0.001572 | 🟢 medium — moderately distinctive | — |
| 1261 | **degenerate** | 1 | 8 | - | 1,329.98 | 0.108300 | 1,148 | 1,286 | 0.001571 | 🟢 medium — moderately distinctive | ~ |
| 1262 | **build** | 1 | 6 | - | 629.30 | 0.055945 | 2,182 | 831 | 0.001568 | 🟢 medium — moderately distinctive | — |
| 1263 | **proper** | 1 | 9 | - | 1,192.73 | 0.094593 | 1,259 | 1,175 | 0.001568 | 🟢 medium — moderately distinctive | — |
| 1264 | **male** | 1 | 9 | - | 1,300.83 | 0.106580 | 1,200 | 1,232 | 0.001568 | 🟢 medium — moderately distinctive | — |
| 1265 | **single word** | 2 | 3 | 0.332 | - | 0.038729 | - | 633 | 0.001567 | - | — |
| 1266 | **covetousness** | 1 | 8 | - | 1,329.54 | 0.107598 | 1,184 | 1,250 | 0.001567 | 🟢 medium — moderately distinctive | — |
| 1267 | **stage** | 1 | 12 | - | 1,255.61 | 0.101194 | 1,226 | 1,207 | 0.001567 | 🟢 medium — moderately distinctive | — |
| 1268 | **quite** | 1 | 23 | - | 2,556.96 | - | 634 | - | 0.001565 | 🟢 medium — moderately distinctive | — |
| 1269 | **sentient** | 1 | 8 | - | 1,329.54 | 0.108058 | 1,169 | 1,271 | 0.001565 | 🟢 medium — moderately distinctive | — |
| 1270 | **santideva** | 1 | 6 | - | 997.16 | 0.077650 | 1,465 | 1,040 | 0.001565 | 🟢 medium — moderately distinctive | — |
| 1271 | **success** | 1 | 10 | - | 1,091.31 | 0.083705 | 1,379 | 1,090 | 0.001564 | 🟢 medium — moderately distinctive | — |
| 1272 | **tsampa** | 1 | 8 | - | 1,329.54 | 0.107828 | 1,182 | 1,257 | 0.001564 | 🟢 medium — moderately distinctive | ✓ རྩམ་པ |
| 1273 | **victim** | 1 | 9 | - | 1,496.23 | 0.140929 | 1,037 | 1,472 | 0.001564 | 🟢 medium — moderately distinctive | — |
| 1274 | **beg** | 1 | 7 | - | 1,163.73 | 0.094506 | 1,278 | 1,167 | 0.001562 | 🟢 medium — moderately distinctive | — |
| 1275 | **worth** | 1 | 11 | - | 926.71 | 0.074152 | 1,555 | 1,001 | 0.001562 | 🟢 medium — moderately distinctive | — |
| 1276 | **mouthful** | 1 | 8 | - | 1,329.54 | 0.108008 | 1,181 | 1,267 | 0.001559 | 🟢 medium — moderately distinctive | — |
| 1277 | **previous life** | 2 | 4 | 0.485 | - | 0.039346 | - | 638 | 0.001557 | - | — |
| 1278 | **tiniest** | 1 | 8 | - | 1,329.54 | 0.108121 | 1,179 | 1,275 | 0.001556 | 🟢 medium — moderately distinctive | — |
| 1279 | **ngokpa** | 1 | 6 | - | 997.16 | 0.077251 | 1,492 | 1,038 | 0.001555 | 🟢 medium — moderately distinctive | — |
| 1280 | **wrong path** | 2 | 4 | 0.374 | - | 0.039533 | - | 640 | 0.001553 | - | ~ |
| 1281 | **delusion** | 1 | 9 | - | 1,495.74 | 0.140850 | 1,052 | 1,471 | 0.001552 | 🟢 medium — moderately distinctive | — |
| 1282 | **meal** | 1 | 10 | - | 1,139.04 | 0.092095 | 1,341 | 1,133 | 0.001552 | 🟢 medium — moderately distinctive | — |
| 1283 | **taste** | 1 | 8 | - | 1,273.77 | 0.107314 | 1,215 | 1,243 | 0.001552 | 🟢 medium — moderately distinctive | — |
| 1284 | **inspire** | 1 | 8 | - | 1,273.77 | 0.107246 | 1,217 | 1,242 | 0.001551 | 🟢 medium — moderately distinctive | — |
| 1285 | **zangpo** | 1 | 6 | - | 997.16 | 0.078727 | 1,498 | 1,043 | 0.001548 | 🟢 medium — moderately distinctive | ~ |
| 1286 | **butcher** | 1 | 8 | - | 1,273.77 | 0.107522 | 1,219 | 1,247 | 0.001547 | 🟢 medium — moderately distinctive | — |
| 1287 | **remembering** | 1 | 15 | - | 2,493.71 | - | 643 | - | 0.001547 | 🟢 medium — moderately distinctive | — |
| 1288 | **agony** | 1 | 9 | - | 1,496.23 | 0.148567 | 1,038 | 1,519 | 0.001544 | 🟢 medium — moderately distinctive | — |
| 1289 | **silken** | 1 | 8 | - | 1,329.54 | 0.108352 | 1,185 | 1,290 | 0.001544 | 🟢 medium — moderately distinctive | — |
| 1290 | **inseparable** | 1 | 8 | - | 1,329.54 | 0.108342 | 1,186 | 1,289 | 0.001544 | 🟢 medium — moderately distinctive | ~ |
| 1291 | **search** | 1 | 8 | - | 1,060.20 | 0.085395 | 1,400 | 1,105 | 0.001543 | 🟢 medium — moderately distinctive | — |
| 1292 | **barley** | 1 | 10 | - | 1,048.83 | 0.083891 | 1,411 | 1,099 | 0.001543 | 🟢 medium — moderately distinctive | — |
| 1293 | **unpleasant** | 1 | 8 | - | 1,273.77 | 0.107670 | 1,221 | 1,253 | 0.001542 | 🟢 medium — moderately distinctive | — |
| 1294 | **loose** | 1 | 8 | - | 1,233.88 | 0.107100 | 1,234 | 1,240 | 0.001542 | 🟢 medium — moderately distinctive | — |
| 1295 | **door** | 1 | 12 | - | 1,487.06 | 0.134550 | 1,082 | 1,444 | 0.001541 | 🟢 medium — moderately distinctive | — |
| 1296 | **flow** | 1 | 12 | - | 1,165.43 | 0.101613 | 1,271 | 1,209 | 0.001539 | 🟢 medium — moderately distinctive | — |
| 1297 | **tiny** | 1 | 8 | - | 1,273.77 | 0.107853 | 1,220 | 1,260 | 0.001539 | 🟢 medium — moderately distinctive | — |
| 1298 | **yogas** | 1 | - | - | - | 0.040577 | - | 647 | 0.001539 | - | — |
| 1299 | **nun** | 1 | 9 | - | 1,495.74 | 0.141716 | 1,068 | 1,475 | 0.001538 | 🟢 medium — moderately distinctive | ~ |
| 1300 | **special** | 1 | 11 | - | 915.30 | 0.074862 | 1,573 | 1,021 | 0.001537 | 🟢 medium — moderately distinctive | — |
| 1301 | **posture** | 1 | 9 | - | 1,324.88 | 0.108410 | 1,192 | 1,296 | 0.001536 | 🟢 medium — moderately distinctive | ~ |
| 1302 | **monastery** | 1 | 8 | - | 1,329.54 | 0.114493 | 1,172 | 1,322 | 0.001535 | 🟢 medium — moderately distinctive | ~ |
| 1303 | **steal** | 1 | 8 | - | 1,329.98 | 0.123041 | 1,154 | 1,346 | 0.001535 | 🟢 medium — moderately distinctive | — |
| 1304 | **sea** | 1 | 11 | - | 1,082.98 | 0.091567 | 1,382 | 1,129 | 0.001535 | 🟢 medium — moderately distinctive | — |
| 1305 | **check** | 1 | 9 | - | 1,137.10 | 0.094072 | 1,348 | 1,155 | 0.001533 | 🟢 medium — moderately distinctive | — |
| 1306 | **minor** | 1 | 9 | - | 1,162.44 | 0.094515 | 1,331 | 1,168 | 0.001533 | 🟢 medium — moderately distinctive | ~ |
| 1307 | **lip** | 1 | 8 | - | 1,329.98 | 0.123628 | 1,151 | 1,354 | 0.001533 | 🟢 medium — moderately distinctive | — |
| 1308 | **melt** | 1 | 9 | - | 1,495.74 | 0.142119 | 1,077 | 1,477 | 0.001530 | 🟢 medium — moderately distinctive | — |
| 1309 | **pull** | 1 | 9 | - | 1,181.96 | 0.106303 | 1,265 | 1,230 | 0.001530 | 🟢 medium — moderately distinctive | — |
| 1310 | **ancient** | 1 | 7 | - | 1,163.35 | 0.098045 | 1,306 | 1,195 | 0.001529 | 🟢 medium — moderately distinctive | ~ |
| 1311 | **error** | 1 | 10 | - | 1,472.09 | 0.139152 | 1,088 | 1,466 | 0.001526 | 🟢 medium — moderately distinctive | — |
| 1312 | **husband** | 1 | 8 | - | 1,329.54 | 0.122278 | 1,171 | 1,341 | 0.001526 | 🟢 medium — moderately distinctive | — |
| 1313 | **ambrosia** | 1 | 8 | - | 1,329.54 | 0.123573 | 1,164 | 1,352 | 0.001525 | 🟢 medium — moderately distinctive | ✓ བདུད་རྩི |
| 1314 | **health** | 1 | 10 | - | 979.40 | 0.082917 | 1,514 | 1,064 | 0.001525 | 🟢 medium — moderately distinctive | — |
| 1315 | **loved** | 1 | 15 | - | 2,492.89 | - | 655 | - | 0.001523 | 🟢 medium — moderately distinctive | — |
| 1316 | **behaviour** | 1 | 8 | - | 1,202.95 | 0.107761 | 1,253 | 1,256 | 0.001521 | 🟢 medium — moderately distinctive | — |
| 1317 | **lap** | 1 | 8 | - | 1,329.54 | 0.123164 | 1,174 | 1,348 | 0.001521 | 🟢 medium — moderately distinctive | — |
| 1318 | **goddess** | 1 | 15 | - | 2,492.89 | - | 657 | - | 0.001519 | 🟢 medium — moderately distinctive | — |
| 1319 | **whatsoever** | 1 | 8 | - | 1,233.88 | 0.108204 | 1,235 | 1,281 | 0.001518 | 🟢 medium — moderately distinctive | — |
| 1320 | **danger** | 1 | 11 | - | 1,312.49 | 0.117540 | 1,196 | 1,327 | 0.001517 | 🟢 medium — moderately distinctive | — |
| 1321 | **trace** | 1 | 8 | - | 1,177.67 | 0.107658 | 1,266 | 1,252 | 0.001516 | 🟢 medium — moderately distinctive | — |
| 1322 | **cushion** | 1 | 10 | - | 1,445.37 | 0.139773 | 1,100 | 1,469 | 0.001516 | 🟢 medium — moderately distinctive | — |
| 1323 | **west** | 1 | 11 | - | 757.66 | 0.067431 | 1,843 | 954 | 0.001512 | 🟢 medium — moderately distinctive | — |
| 1324 | **purpose** | 1 | 9 | - | 1,045.42 | 0.093260 | 1,413 | 1,141 | 0.001512 | 🟢 medium — moderately distinctive | — |
| 1325 | **leg** | 1 | 16 | - | 2,467.76 | - | 661 | - | 0.001511 | 🟢 medium — moderately distinctive | — |
| 1326 | **snow** | 1 | 9 | - | 1,162.44 | 0.099879 | 1,333 | 1,202 | 0.001510 | 🟢 medium — moderately distinctive | — |
| 1327 | **self** | 1 | 16 | - | 2,467.76 | - | 662 | - | 0.001509 | 🟢 medium — moderately distinctive | ~ |
| 1328 | **peace** | 1 | 8 | - | 1,202.95 | 0.108122 | 1,256 | 1,276 | 0.001508 | 🟢 medium — moderately distinctive | — |
| 1329 | **show** | 1 | 20 | - | 1,594.10 | 0.182228 | 994 | 1,735 | 0.001506 | 🟢 medium — moderately distinctive | — |
| 1330 | **gradually** | 1 | 9 | - | 1,054.33 | 0.094142 | 1,402 | 1,157 | 0.001506 | 🟢 medium — moderately distinctive | — |
| 1331 | **enough** | 1 | 27 | - | 2,453.16 | - | 666 | - | 0.001502 | 🟢 medium — moderately distinctive | — |
| 1332 | **dharmaraksita** | 1 | 6 | - | 997.16 | 0.084874 | 1,496 | 1,104 | 0.001502 | 🟢 medium — moderately distinctive | — |
| 1333 | **least** | 1 | 30 | - | 2,443.00 | - | 667 | - | 0.001500 | 🟢 medium — moderately distinctive | — |
| 1334 | **good health** | 2 | 4 | 0.532 | - | 0.041757 | - | 667 | 0.001500 | - | — |
| 1335 | **difference** | 1 | 9 | - | 1,073.86 | 0.094566 | 1,395 | 1,171 | 0.001500 | 🟢 medium — moderately distinctive | — |
| 1336 | **buddhist** | 1 | 6 | - | 997.48 | 0.093188 | 1,444 | 1,138 | 0.001500 | 🟢 medium — moderately distinctive | — |
| 1337 | **bit** | 1 | 10 | - | 1,152.21 | 0.103440 | 1,337 | 1,216 | 0.001500 | 🟢 medium — moderately distinctive | — |
| 1338 | **attainment** | 1 | 9 | - | 1,496.23 | 0.173552 | 1,043 | 1,628 | 0.001499 | 🟢 medium — moderately distinctive | ~ |
| 1339 | **affliction** | 1 | 9 | - | 1,495.74 | 0.169919 | 1,050 | 1,612 | 0.001499 | 🟢 medium — moderately distinctive | — |
| 1340 | **seal** | 1 | 8 | - | 1,202.95 | 0.108488 | 1,252 | 1,300 | 0.001497 | 🟢 medium — moderately distinctive | — |
| 1341 | **touch** | 1 | 8 | - | 1,081.57 | 0.094861 | 1,385 | 1,183 | 0.001497 | 🟢 medium — moderately distinctive | — |
| 1342 | **ripen** | 1 | 7 | - | 1,163.35 | 0.107624 | 1,305 | 1,251 | 0.001495 | 🟢 medium — moderately distinctive | — |
| 1343 | **otherwise** | 1 | 21 | - | 2,429.34 | - | 670 | - | 0.001494 | 🟢 medium — moderately distinctive | — |
| 1344 | **bodh gaya** | 2 | 6 | 1.000 | - | 0.041955 | - | 670 | 0.001494 | - | — |
| 1345 | **human realm** | 2 | 3 | 0.304 | - | 0.042105 | - | 671 | 0.001492 | - | — |
| 1346 | **satisfy** | 1 | 5 | - | 627.49 | 0.061514 | 2,184 | 896 | 0.001492 | 🟢 medium — moderately distinctive | — |
| 1347 | **twelve** | 1 | 17 | - | 2,417.79 | - | 672 | - | 0.001491 | 🟢 medium — moderately distinctive | ~ |
| 1348 | **morning** | 1 | 10 | - | 879.80 | 0.083112 | 1,596 | 1,070 | 0.001489 | 🟢 medium — moderately distinctive | — |
| 1349 | **favourable** | 1 | 9 | - | 1,010.62 | 0.094442 | 1,429 | 1,165 | 0.001488 | 🟢 medium — moderately distinctive | — |
| 1350 | **ordinary human** | 2 | 3 | 0.358 | - | 0.042327 | - | 674 | 0.001487 | - | — |
| 1351 | **humble life** | 2 | 4 | 0.518 | - | 0.042509 | - | 675 | 0.001485 | - | — |
| 1352 | **naturally** | 1 | 8 | - | 1,156.30 | 0.107449 | 1,334 | 1,244 | 0.001484 | 🟢 medium — moderately distinctive | — |
| 1353 | **entirely** | 1 | 20 | - | 2,410.26 | - | 676 | - | 0.001483 | 🟢 medium — moderately distinctive | — |
| 1354 | **deeply** | 1 | 8 | - | 1,137.78 | 0.107003 | 1,344 | 1,238 | 0.001483 | 🟢 medium — moderately distinctive | — |
| 1355 | **feast** | 1 | 9 | - | 1,495.74 | 0.170151 | 1,071 | 1,614 | 0.001482 | 🟢 medium — moderately distinctive | ~ |
| 1356 | **dwell** | 1 | 9 | - | 1,495.74 | 0.170475 | 1,072 | 1,616 | 0.001480 | 🟢 medium — moderately distinctive | — |
| 1357 | **certain** | 1 | 30 | - | 2,403.64 | - | 678 | - | 0.001479 | 🟢 medium — moderately distinctive | — |
| 1358 | **benefactor** | 1 | 9 | - | 1,495.74 | 0.172978 | 1,070 | 1,625 | 0.001478 | 🟢 medium — moderately distinctive | — |
| 1359 | **expression** | 1 | 8 | - | 1,233.88 | 0.123604 | 1,239 | 1,353 | 0.001478 | 🟢 medium — moderately distinctive | ~ |
| 1360 | **crime** | 1 | 8 | - | 1,233.88 | 0.123834 | 1,237 | 1,356 | 0.001477 | 🟢 medium — moderately distinctive | — |
| 1361 | **thirty-three** | 1 | 15 | - | 2,388.31 | - | 680 | - | 0.001476 | 🟢 medium — moderately distinctive | — |
| 1362 | **palm** | 1 | 10 | - | 1,088.13 | 0.104993 | 1,380 | 1,222 | 0.001474 | 🟢 medium — moderately distinctive | — |
| 1363 | **habitual** | 1 | 7 | - | 1,163.35 | 0.110437 | 1,287 | 1,310 | 0.001472 | 🟢 medium — moderately distinctive | ~ |
| 1364 | **vajrapani** | 1 | 6 | - | 997.16 | 0.093713 | 1,494 | 1,148 | 0.001471 | 🟢 medium — moderately distinctive | ✓ ཕྱག་ན་རྡོ་རྗེ |
| 1365 | **top** | 1 | 25 | - | 2,368.12 | - | 683 | - | 0.001470 | 🟢 medium — moderately distinctive | — |
| 1366 | **general** | 1 | 11 | - | 789.19 | 0.074712 | 1,810 | 1,013 | 0.001467 | 🟢 medium — moderately distinctive | — |
| 1367 | **pure land** | 2 | 8 | 0.584 | - | 0.043334 | - | 685 | 0.001467 | - | ✓ དག་པའི་ཞིང |
| 1368 | **accomplished** | 1 | 16 | - | 2,355.34 | - | 686 | - | 0.001465 | 🟢 medium — moderately distinctive | — |
| 1369 | **heard** | 1 | 19 | - | 2,354.52 | - | 687 | - | 0.001463 | 🟢 medium — moderately distinctive | — |
| 1370 | **authentic spiritual friend** | 3 | 3 | 0.568 | - | 0.043731 | - | 688 | 0.001461 | - | — |
| 1371 | **confusion** | 1 | 8 | - | 1,137.78 | 0.108287 | 1,343 | 1,285 | 0.001456 | 🟢 medium — moderately distinctive | — |
| 1372 | **highly** | 1 | 9 | - | 976.51 | 0.094316 | 1,516 | 1,160 | 0.001454 | 🟢 medium — moderately distinctive | — |
| 1373 | **human existence** | 2 | 6 | 0.572 | - | 0.044075 | - | 693 | 0.001452 | - | — |
| 1374 | **stupid** | 1 | 7 | - | 1,163.73 | 0.124593 | 1,275 | 1,362 | 0.001452 | 🟢 medium — moderately distinctive | — |
| 1375 | **marvellous** | 1 | 7 | - | 1,163.35 | 0.110709 | 1,321 | 1,314 | 0.001452 | 🟢 medium — moderately distinctive | — |
| 1376 | **stupa** | 1 | 7 | - | 1,163.35 | 0.110471 | 1,326 | 1,311 | 0.001451 | 🟢 medium — moderately distinctive | ✓ མཆོད་རྟེན |
| 1377 | **rainbow** | 1 | 8 | - | 1,137.78 | 0.108367 | 1,346 | 1,293 | 0.001450 | 🟢 medium — moderately distinctive | — |
| 1378 | **lifestyle** | 1 | 9 | - | 1,300.83 | 0.137981 | 1,201 | 1,462 | 0.001450 | 🟢 medium — moderately distinctive | — |
| 1379 | **remedy** | 1 | 8 | - | 1,121.46 | 0.108324 | 1,354 | 1,287 | 0.001450 | 🟢 medium — moderately distinctive | — |
| 1380 | **identical** | 1 | 8 | - | 1,137.78 | 0.108367 | 1,347 | 1,294 | 0.001449 | 🟢 medium — moderately distinctive | — |
| 1381 | **glad** | 1 | 7 | - | 1,163.73 | 0.125253 | 1,272 | 1,374 | 0.001448 | 🟢 medium — moderately distinctive | — |
| 1382 | **size** | 1 | 9 | - | 953.26 | 0.094125 | 1,540 | 1,156 | 0.001447 | 🟢 medium — moderately distinctive | — |
| 1383 | **well-being** | 1 | 14 | - | 2,326.70 | - | 696 | - | 0.001447 | 🟢 medium — moderately distinctive | — |
| 1384 | **poisonous** | 1 | 7 | - | 1,163.73 | 0.125227 | 1,277 | 1,373 | 0.001446 | 🟢 medium — moderately distinctive | — |
| 1385 | **fourth** | 1 | 9 | - | 744.41 | 0.074840 | 1,864 | 1,020 | 0.001446 | 🟢 medium — moderately distinctive | ~ |
| 1386 | **hungry** | 1 | 7 | - | 1,163.35 | 0.124765 | 1,290 | 1,364 | 0.001443 | 🟢 medium — moderately distinctive | — |
| 1387 | **absolutely** | 1 | 8 | - | 1,081.57 | 0.108113 | 1,383 | 1,274 | 0.001443 | 🟢 medium — moderately distinctive | — |
| 1388 | **sad** | 1 | 7 | - | 1,163.73 | 0.125498 | 1,274 | 1,386 | 0.001441 | 🟢 medium — moderately distinctive | — |
| 1389 | **conclusion** | 1 | 8 | - | 997.54 | 0.107030 | 1,432 | 1,239 | 0.001440 | 🟢 medium — moderately distinctive | ~ |
| 1390 | **spark** | 1 | 8 | - | 1,081.57 | 0.108183 | 1,386 | 1,277 | 0.001440 | 🟢 medium — moderately distinctive | — |
| 1391 | **condense** | 1 | 1 | - | 166.19 | 0.049148 | 4,566 | 758 | 0.001439 | 🔵 low — common in general English | — |
| 1392 | **layman** | 1 | 7 | - | 1,163.35 | 0.125172 | 1,295 | 1,370 | 0.001437 | 🟢 medium — moderately distinctive | — |
| 1393 | **infinity** | 1 | 7 | - | 1,163.73 | 0.125545 | 1,281 | 1,388 | 0.001436 | 🟢 medium — moderately distinctive | — |
| 1394 | **capable** | 1 | 8 | - | 1,017.86 | 0.107673 | 1,423 | 1,254 | 0.001435 | 🟢 medium — moderately distinctive | — |
| 1395 | **discover** | 1 | 7 | - | 1,163.73 | 0.125529 | 1,284 | 1,387 | 0.001435 | 🟢 medium — moderately distinctive | — |
| 1396 | **language** | 1 | 9 | - | 1,162.44 | 0.121017 | 1,332 | 1,336 | 0.001435 | 🟢 medium — moderately distinctive | — |
| 1397 | **owner** | 1 | 11 | - | 1,257.65 | 0.138586 | 1,225 | 1,464 | 0.001434 | 🟢 medium — moderately distinctive | ~ |
| 1398 | **liberated** | 1 | 14 | - | 2,326.70 | - | 704 | - | 0.001433 | 🟢 medium — moderately distinctive | — |
| 1399 | **atra** | 1 | 7 | - | 1,163.35 | 0.125341 | 1,298 | 1,377 | 0.001432 | 🟢 medium — moderately distinctive | — |
| 1400 | **encounter** | 1 | 8 | - | 1,273.77 | 0.143809 | 1,216 | 1,482 | 0.001432 | 🟢 medium — moderately distinctive | — |
| 1401 | **refer** | 1 | 8 | - | 1,156.30 | 0.122194 | 1,335 | 1,340 | 0.001431 | 🟢 medium — moderately distinctive | — |
| 1402 | **control** | 1 | 10 | - | 796.47 | 0.082897 | 1,790 | 1,063 | 0.001431 | 🟢 medium — moderately distinctive | — |
| 1403 | **direct** | 1 | 9 | - | 902.51 | 0.094321 | 1,580 | 1,162 | 0.001428 | 🟢 medium — moderately distinctive | — |
| 1404 | **throw** | 1 | 6 | - | 853.34 | 0.093561 | 1,620 | 1,143 | 0.001426 | 🟢 medium — moderately distinctive | — |
| 1405 | **plain** | 1 | 8 | - | 1,137.78 | 0.122724 | 1,342 | 1,343 | 0.001426 | 🟢 medium — moderately distinctive | — |
| 1406 | **common** | 1 | 11 | - | 710.95 | 0.075067 | 1,910 | 1,030 | 0.001425 | 🟢 medium — moderately distinctive | ~ |
| 1407 | **travel** | 1 | 8 | - | 1,003.99 | 0.108012 | 1,431 | 1,268 | 0.001424 | 🟢 medium — moderately distinctive | — |
| 1408 | **kind heart** | 2 | 3 | 0.354 | - | 0.044885 | - | 710 | 0.001423 | - | — |
| 1409 | **solid** | 1 | 8 | - | 1,010.75 | 0.108092 | 1,428 | 1,272 | 0.001423 | 🟢 medium — moderately distinctive | — |
| 1410 | **medicinal** | 1 | 7 | - | 1,163.35 | 0.125254 | 1,319 | 1,375 | 0.001422 | 🟢 medium — moderately distinctive | — |
| 1411 | **mark** | 1 | 11 | - | 984.08 | 0.103228 | 1,510 | 1,214 | 0.001422 | 🟢 medium — moderately distinctive | — |
| 1412 | **wrathful black** | 2 | 4 | 0.683 | - | 0.044998 | - | 711 | 0.001421 | - | ~ |
| 1413 | **wall** | 1 | 11 | - | 1,111.73 | 0.117169 | 1,370 | 1,326 | 0.001421 | 🟢 medium — moderately distinctive | — |
| 1414 | **everyday** | 1 | 7 | - | 1,163.35 | 0.125849 | 1,303 | 1,397 | 0.001420 | 🟢 medium — moderately distinctive | — |
| 1415 | **pus** | 1 | 7 | - | 1,163.35 | 0.125436 | 1,315 | 1,384 | 0.001420 | 🟢 medium — moderately distinctive | — |
| 1416 | **magical** | 1 | 7 | - | 1,163.35 | 0.125891 | 1,307 | 1,401 | 0.001416 | 🟢 medium — moderately distinctive | — |
| 1417 | **ride** | 1 | 8 | - | 1,121.46 | 0.123545 | 1,355 | 1,351 | 0.001415 | 🟢 medium — moderately distinctive | — |
| 1418 | **trying** | 1 | 23 | - | 2,268.42 | - | 715 | - | 0.001415 | 🟢 medium — moderately distinctive | — |
| 1419 | **dear** | 1 | 7 | - | 1,163.35 | 0.125878 | 1,311 | 1,400 | 0.001414 | 🟢 medium — moderately distinctive | — |
| 1420 | **particularly** | 1 | 24 | - | 2,263.45 | - | 716 | - | 0.001413 | 🟢 medium — moderately distinctive | — |
| 1421 | **naga** | 1 | 8 | - | 1,329.54 | 0.172251 | 1,163 | 1,622 | 0.001412 | 🟢 medium — moderately distinctive | ✓ ཀླུ |
| 1422 | **fit** | 1 | 9 | - | 1,102.29 | 0.121798 | 1,376 | 1,338 | 0.001412 | 🟢 medium — moderately distinctive | — |
| 1423 | **disc** | 1 | 8 | - | 1,121.46 | 0.123847 | 1,357 | 1,357 | 0.001411 | 🟢 medium — moderately distinctive | — |
| 1424 | **bright** | 1 | 7 | - | 968.49 | 0.105317 | 1,521 | 1,224 | 0.001411 | 🟢 medium — moderately distinctive | — |
| 1425 | **negative karmic** | 2 | 4 | 0.462 | - | 0.046268 | - | 718 | 0.001410 | - | ~ |
| 1426 | **listening** | 1 | 15 | - | 2,255.52 | - | 719 | - | 0.001408 | 🟢 medium — moderately distinctive | — |
| 1427 | **primordial** | 1 | 7 | - | 1,163.35 | 0.126075 | 1,324 | 1,407 | 0.001404 | 🟢 medium — moderately distinctive | ~ |
| 1428 | **famous** | 1 | 6 | - | 997.48 | 0.109560 | 1,435 | 1,307 | 0.001400 | 🟢 medium — moderately distinctive | — |
| 1429 | **great sinner** | 2 | 3 | 0.575 | - | 0.046818 | - | 725 | 0.001398 | - | — |
| 1430 | **careful** | 1 | 8 | - | 985.47 | 0.107831 | 1,509 | 1,258 | 0.001396 | 🟢 medium — moderately distinctive | — |
| 1431 | **battle** | 1 | 9 | - | 1,041.15 | 0.120540 | 1,417 | 1,333 | 0.001395 | 🟢 medium — moderately distinctive | — |
| 1432 | **sow** | 1 | 2 | - | 308.47 | 0.055646 | 3,815 | 821 | 0.001393 | 🔵 low — common in general English | — |
| 1433 | **combine** | 1 | 8 | - | 1,070.47 | 0.123800 | 1,398 | 1,355 | 0.001393 | 🟢 medium — moderately distinctive | — |
| 1434 | **slaughtered** | 1 | 14 | - | 2,229.09 | - | 729 | - | 0.001392 | 🟢 medium — moderately distinctive | — |
| 1435 | **firm** | 1 | 10 | - | 738.32 | 0.083581 | 1,867 | 1,086 | 0.001392 | 🟢 medium — moderately distinctive | — |
| 1436 | **occur** | 1 | 9 | - | 1,014.12 | 0.120972 | 1,424 | 1,335 | 0.001391 | 🟢 medium — moderately distinctive | — |
| 1437 | **opposite** | 1 | 7 | - | 1,079.65 | 0.125124 | 1,388 | 1,369 | 0.001390 | 🟢 medium — moderately distinctive | — |
| 1438 | **worse** | 1 | 18 | - | 2,217.32 | - | 731 | - | 0.001389 | 🟢 medium — moderately distinctive | — |
| 1439 | **multitude** | 1 | 7 | - | 1,163.73 | 0.146440 | 1,283 | 1,496 | 0.001387 | 🟢 medium — moderately distinctive | — |
| 1440 | **calf** | 1 | 7 | - | 1,079.65 | 0.125182 | 1,393 | 1,371 | 0.001387 | 🟢 medium — moderately distinctive | — |
| 1441 | **business** | 1 | 10 | - | 666.94 | 0.083096 | 1,935 | 1,069 | 0.001387 | 🟢 medium — moderately distinctive | — |
| 1442 | **worst** | 1 | 8 | - | 929.26 | 0.107502 | 1,551 | 1,246 | 0.001386 | 🟢 medium — moderately distinctive | — |
| 1443 | **rope** | 1 | 7 | - | 1,163.35 | 0.145123 | 1,294 | 1,486 | 0.001385 | 🟢 medium — moderately distinctive | — |
| 1444 | **air** | 1 | 9 | - | 911.42 | 0.106655 | 1,578 | 1,233 | 0.001384 | 🟢 medium — moderately distinctive | — |
| 1445 | **basis** | 1 | - | - | - | 0.047522 | - | 734 | 0.001384 | - | — |
| 1446 | **smell** | 1 | 7 | - | 1,163.35 | 0.146172 | 1,292 | 1,493 | 0.001384 | 🟢 medium — moderately distinctive | — |
| 1447 | **country** | 1 | 13 | - | 1,046.32 | 0.124497 | 1,412 | 1,361 | 0.001383 | 🟢 medium — moderately distinctive | ~ |
| 1448 | **turned** | 1 | 19 | - | 2,197.97 | - | 735 | - | 0.001382 | 🟢 medium — moderately distinctive | — |
| 1449 | **ogress** | 1 | 6 | - | 997.16 | 0.109331 | 1,481 | 1,304 | 0.001382 | 🟢 medium — moderately distinctive | — |
| 1450 | **cow** | 1 | 7 | - | 1,114.54 | 0.127380 | 1,367 | 1,414 | 0.001379 | 🟢 medium — moderately distinctive | — |
| 1451 | **clearly** | 1 | 20 | - | 2,189.10 | - | 737 | - | 0.001379 | 🟢 medium — moderately distinctive | — |
| 1452 | **nowadays** | 1 | - | - | - | 0.047589 | - | 737 | 0.001379 | - | — |
| 1453 | **prey** | 1 | 7 | - | 1,079.65 | 0.125689 | 1,391 | 1,392 | 0.001378 | 🟢 medium — moderately distinctive | — |
| 1454 | **needle** | 1 | 7 | - | 1,163.35 | 0.145864 | 1,308 | 1,491 | 0.001376 | 🟢 medium — moderately distinctive | — |
| 1455 | **till** | 1 | 7 | - | 1,052.58 | 0.125423 | 1,407 | 1,381 | 0.001376 | 🟢 medium — moderately distinctive | — |
| 1456 | **poverty** | 1 | 7 | - | 1,079.65 | 0.125851 | 1,390 | 1,398 | 0.001376 | 🟢 medium — moderately distinctive | — |
| 1457 | **getting** | 1 | 20 | - | 2,170.02 | - | 741 | - | 0.001373 | 🟢 medium — moderately distinctive | — |
| 1458 | **voice** | 1 | 8 | - | 1,081.57 | 0.126585 | 1,384 | 1,410 | 0.001373 | 🟢 medium — moderately distinctive | ~ |
| 1459 | **violent** | 1 | 7 | - | 1,052.58 | 0.125682 | 1,409 | 1,391 | 0.001370 | 🟢 medium — moderately distinctive | — |
| 1460 | **forehead** | 1 | 7 | - | 1,163.35 | 0.146358 | 1,316 | 1,495 | 0.001370 | 🟢 medium — moderately distinctive | — |
| 1461 | **girl** | 1 | 7 | - | 1,163.35 | 0.146325 | 1,317 | 1,494 | 0.001370 | 🟢 medium — moderately distinctive | — |
| 1462 | **accumulating** | 1 | 16 | - | 2,163.14 | - | 744 | - | 0.001368 | 🟢 medium — moderately distinctive | ~ |
| 1463 | **manjusri** | 1 | 5 | - | 830.96 | 0.099665 | 1,683 | 1,201 | 0.001367 | 🟢 medium — moderately distinctive | — |
| 1464 | **daily practice** | 2 | 4 | 0.551 | - | 0.047939 | - | 746 | 0.001365 | - | — |
| 1465 | **vairotsana** | 1 | 5 | - | 830.96 | 0.100609 | 1,681 | 1,205 | 0.001365 | 🟢 medium — moderately distinctive | ✓ བཻ་རོ་ཙ་ན |
| 1466 | **beneficial** | 1 | 8 | - | 945.59 | 0.108327 | 1,545 | 1,288 | 0.001365 | 🟢 medium — moderately distinctive | — |
| 1467 | **oral** | 1 | 7 | - | 1,052.58 | 0.126143 | 1,405 | 1,408 | 0.001364 | 🟢 medium — moderately distinctive | — |
| 1468 | **vast expanse** | 2 | 5 | 0.692 | - | 0.048003 | - | 747 | 0.001364 | - | — |
| 1469 | **correct** | 1 | 8 | - | 954.54 | 0.108413 | 1,536 | 1,297 | 0.001363 | 🟢 medium — moderately distinctive | — |
| 1470 | **hrih** | 1 | 6 | - | 997.16 | 0.115355 | 1,504 | 1,323 | 0.001362 | 🟢 medium — moderately distinctive | — |
| 1471 | **prepare** | 1 | 5 | - | 608.99 | 0.074937 | 2,206 | 1,026 | 0.001362 | 🟢 medium — moderately distinctive | — |
| 1472 | **vidyadharas** | 1 | - | - | - | 0.048118 | - | 748 | 0.001362 | - | — |
| 1473 | **gonpo** | 1 | 5 | - | 830.96 | 0.100607 | 1,692 | 1,204 | 0.001362 | 🟢 medium — moderately distinctive | ~ |
| 1474 | **save** | 1 | 8 | - | 921.77 | 0.108201 | 1,569 | 1,280 | 0.001360 | 🟢 medium — moderately distinctive | — |
| 1475 | **summit** | 1 | 8 | - | 914.65 | 0.108186 | 1,574 | 1,278 | 0.001359 | 🟢 medium — moderately distinctive | — |
| 1476 | **step** | 1 | 11 | - | 1,113.96 | 0.137040 | 1,369 | 1,459 | 0.001358 | 🟢 medium — moderately distinctive | — |
| 1477 | **beginningless time** | 2 | 3 | 0.509 | - | 0.048300 | - | 751 | 0.001357 | - | — |
| 1478 | **book** | 1 | 8 | - | 880.97 | 0.108034 | 1,595 | 1,269 | 0.001357 | 🟢 medium — moderately distinctive | — |
| 1479 | **maintain** | 1 | 9 | - | 830.29 | 0.094775 | 1,757 | 1,181 | 0.001356 | 🟢 medium — moderately distinctive | — |
| 1480 | **single instant** | 2 | 6 | 0.565 | - | 0.048487 | - | 752 | 0.001356 | - | — |
| 1481 | **tormented** | 1 | 13 | - | 2,160.51 | - | 753 | - | 0.001354 | 🟢 medium — moderately distinctive | — |
| 1482 | **wise** | 1 | 6 | - | 955.32 | 0.113293 | 1,530 | 1,320 | 0.001354 | 🟢 medium — moderately distinctive | — |
| 1483 | **harmful spirit** | 2 | 7 | 0.569 | - | 0.048933 | - | 755 | 0.001351 | - | — |
| 1484 | **aim** | 1 | 10 | - | 1,094.55 | 0.138854 | 1,378 | 1,465 | 0.001351 | 🟢 medium — moderately distinctive | — |
| 1485 | **ananda** | 1 | 5 | - | 830.96 | 0.106884 | 1,673 | 1,235 | 0.001349 | 🟢 medium — moderately distinctive | ✓ ཀུན་དགའ་བོ |
| 1486 | **achieve** | 1 | 8 | - | 847.34 | 0.107923 | 1,625 | 1,264 | 0.001349 | 🟢 medium — moderately distinctive | — |
| 1487 | **abhidharma** | 1 | 5 | - | 830.96 | 0.099487 | 1,748 | 1,198 | 0.001348 | 🟢 medium — moderately distinctive | ✓ མངོན་པ |
| 1488 | **resolve** | 1 | 8 | - | 843.14 | 0.107927 | 1,626 | 1,265 | 0.001348 | 🟢 medium — moderately distinctive | — |
| 1489 | **quarrel** | 1 | 7 | - | 1,114.54 | 0.145701 | 1,364 | 1,490 | 0.001347 | 🟢 medium — moderately distinctive | — |
| 1490 | **beating** | 1 | 8 | - | 1,329.98 | 0.205096 | 1,156 | 1,846 | 0.001347 | 🟢 medium — moderately distinctive | — |
| 1491 | **repa** | 1 | 5 | - | 830.96 | 0.105295 | 1,710 | 1,223 | 0.001344 | 🟢 medium — moderately distinctive | ~ |
| 1492 | **genuine** | 1 | 7 | - | 995.56 | 0.123861 | 1,506 | 1,358 | 0.001344 | 🟢 medium — moderately distinctive | — |
| 1493 | **vajra seat** | 2 | 3 | 0.586 | - | 0.049233 | - | 761 | 0.001342 | - | ✓ རྡོ་རྗེ་གདན |
| 1494 | **garland** | 1 | 7 | - | 1,163.73 | 0.172031 | 1,280 | 1,620 | 0.001342 | 🟢 medium — moderately distinctive | — |
| 1495 | **situation** | 1 | 12 | - | 1,044.70 | 0.134961 | 1,414 | 1,450 | 0.001341 | 🟢 medium — moderately distinctive | — |
| 1496 | **take care** | 2 | 4 | 0.451 | - | 0.050005 | - | 763 | 0.001339 | - | — |
| 1497 | **altogether** | 1 | 7 | - | 995.56 | 0.125045 | 1,505 | 1,368 | 0.001339 | 🟢 medium — moderately distinctive | — |
| 1498 | **perfect enlightenment** | 2 | 5 | 0.536 | - | 0.050020 | - | 764 | 0.001338 | - | — |
| 1499 | **technique** | 1 | 7 | - | 1,163.73 | 0.176554 | 1,273 | 1,643 | 0.001337 | 🟢 medium — moderately distinctive | — |
| 1500 | **precept** | 1 | 13 | - | 2,160.51 | - | 765 | - | 0.001337 | 🟢 medium — moderately distinctive | — |
| 1501 | **rival** | 1 | 9 | - | 1,068.74 | 0.141849 | 1,399 | 1,476 | 0.001336 | 🟢 medium — moderately distinctive | — |
| 1502 | **mighty** | 1 | 6 | - | 997.16 | 0.127157 | 1,464 | 1,413 | 0.001335 | 🟢 medium — moderately distinctive | — |
| 1503 | **bell** | 1 | 8 | - | 954.54 | 0.123449 | 1,539 | 1,350 | 0.001335 | 🟢 medium — moderately distinctive | ✓ དྲིལ་བུ |
| 1504 | **ruin** | 1 | 7 | - | 1,114.54 | 0.148767 | 1,363 | 1,523 | 0.001334 | 🟢 medium — moderately distinctive | — |
| 1505 | **inexhaustible** | 1 | 6 | - | 997.16 | 0.129001 | 1,460 | 1,419 | 0.001334 | 🟢 medium — moderately distinctive | ~ |
| 1506 | **authentic spiritual** | 2 | 6 | 0.564 | - | 0.050154 | - | 767 | 0.001334 | - | — |
| 1507 | **weight** | 1 | 8 | - | 929.26 | 0.122957 | 1,552 | 1,344 | 0.001333 | 🟢 medium — moderately distinctive | — |
| 1508 | **destruction** | 1 | 7 | - | 1,052.58 | 0.144104 | 1,404 | 1,485 | 0.001330 | 🟢 medium — moderately distinctive | — |
| 1509 | **fat** | 1 | 7 | - | 981.27 | 0.125425 | 1,513 | 1,382 | 0.001329 | 🟢 medium — moderately distinctive | — |
| 1510 | **looking** | 1 | 22 | - | 2,136.62 | - | 772 | - | 0.001326 | 🟢 medium — moderately distinctive | — |
| 1511 | **true nature** | 2 | 4 | 0.459 | - | 0.050671 | - | 772 | 0.001326 | - | ~ |
| 1512 | **transfer** | 1 | 8 | - | 841.09 | 0.108528 | 1,633 | 1,301 | 0.001325 | 🟢 medium — moderately distinctive | — |
| 1513 | **low** | 1 | 9 | - | 708.61 | 0.094379 | 1,911 | 1,163 | 0.001325 | 🟢 medium — moderately distinctive | — |
| 1514 | **used** | 1 | 27 | - | 2,136.44 | - | 773 | - | 0.001325 | 🟢 medium — moderately distinctive | — |
| 1515 | **according** | 1 | 27 | - | 2,119.86 | - | 774 | - | 0.001323 | 🟢 medium — moderately distinctive | — |
| 1516 | **good intention** | 2 | 3 | 0.349 | - | 0.050821 | - | 774 | 0.001323 | - | — |
| 1517 | **city** | 1 | 8 | - | 752.32 | 0.097280 | 1,849 | 1,191 | 0.001323 | 🟢 medium — moderately distinctive | — |
| 1518 | **major** | 1 | 10 | - | 634.89 | 0.083497 | 2,177 | 1,083 | 0.001322 | 🟢 medium — moderately distinctive | ~ |
| 1519 | **execution** | 1 | 7 | - | 927.68 | 0.124980 | 1,553 | 1,366 | 0.001321 | 🟢 medium — moderately distinctive | — |
| 1520 | **pit** | 1 | 7 | - | 1,011.76 | 0.145425 | 1,425 | 1,488 | 0.001319 | 🟢 medium — moderately distinctive | — |
| 1521 | **bad thought** | 2 | 4 | 0.409 | - | 0.050898 | - | 777 | 0.001319 | - | — |
| 1522 | **fool** | 1 | 7 | - | 1,163.35 | 0.175572 | 1,314 | 1,635 | 0.001318 | 🟢 medium — moderately distinctive | — |
| 1523 | **exhausted** | 1 | 14 | - | 2,105.15 | - | 778 | - | 0.001318 | 🟢 medium — moderately distinctive | — |
| 1524 | **session** | 1 | 9 | - | 868.40 | 0.121594 | 1,602 | 1,337 | 0.001318 | 🟢 medium — moderately distinctive | — |
| 1525 | **display** | 1 | 7 | - | 1,011.76 | 0.147043 | 1,427 | 1,501 | 0.001313 | 🟢 medium — moderately distinctive | — |
| 1526 | **crush** | 1 | 4 | - | 553.42 | 0.083042 | 2,292 | 1,067 | 0.001312 | 🟢 medium — moderately distinctive | — |
| 1527 | **one** | 1 | 43 | - | 2,082.10 | - | 783 | - | 0.001311 | 🟢 medium — moderately distinctive | ~ |
| 1528 | **lala** | 1 | 7 | - | 1,163.35 | 0.178791 | 1,318 | 1,653 | 0.001309 | 🟢 medium — moderately distinctive | — |
| 1529 | **gift** | 1 | 7 | - | 1,163.35 | 0.176150 | 1,328 | 1,640 | 0.001309 | 🟢 medium — moderately distinctive | — |
| 1530 | **sweep** | 1 | 4 | - | 664.99 | 0.094540 | 1,960 | 1,170 | 0.001308 | 🟢 medium — moderately distinctive | — |
| 1531 | **forget** | 1 | 6 | - | 883.25 | 0.124881 | 1,592 | 1,365 | 0.001307 | 🟢 medium — moderately distinctive | — |
| 1532 | **correspond** | 1 | 8 | - | 1,137.78 | 0.172090 | 1,345 | 1,621 | 0.001307 | 🟢 medium — moderately distinctive | — |
| 1533 | **unpredictable** | 1 | 6 | - | 997.48 | 0.147529 | 1,438 | 1,505 | 0.001307 | 🟢 medium — moderately distinctive | — |
| 1534 | **winter** | 1 | 8 | - | 789.01 | 0.106962 | 1,811 | 1,237 | 0.001305 | 🟢 medium — moderately distinctive | — |
| 1535 | **visit** | 1 | 8 | - | 818.56 | 0.107839 | 1,770 | 1,259 | 0.001305 | 🟢 medium — moderately distinctive | — |
| 1536 | **deer** | 1 | 6 | - | 997.16 | 0.147018 | 1,448 | 1,500 | 0.001304 | 🟢 medium — moderately distinctive | — |
| 1537 | **commitment** | 1 | 8 | - | 837.07 | 0.122383 | 1,635 | 1,342 | 0.001303 | 🟢 medium — moderately distinctive | — |
| 1538 | **worm** | 1 | 6 | - | 997.48 | 0.148067 | 1,442 | 1,509 | 0.001303 | 🟢 medium — moderately distinctive | — |
| 1539 | **chengawa** | 1 | 5 | - | 830.96 | 0.109422 | 1,693 | 1,305 | 0.001303 | 🟢 medium — moderately distinctive | ~ |
| 1540 | **distinguish** | 1 | 6 | - | 997.48 | 0.148531 | 1,436 | 1,517 | 0.001303 | 🟢 medium — moderately distinctive | — |
| 1541 | **building** | 1 | 14 | - | 1,378.34 | 0.261244 | 1,131 | 2,109 | 0.001301 | 🟢 medium — moderately distinctive | — |
| 1542 | **occasion** | 1 | 8 | - | 1,121.46 | 0.173040 | 1,356 | 1,626 | 0.001299 | 🟢 medium — moderately distinctive | — |
| 1543 | **trunk** | 1 | 6 | - | 997.48 | 0.148719 | 1,443 | 1,520 | 0.001298 | 🟢 medium — moderately distinctive | — |
| 1544 | **sowing** | 1 | 14 | - | 2,060.92 | - | 792 | - | 0.001298 | 🟢 medium — moderately distinctive | — |
| 1545 | **cover** | 1 | 5 | - | 470.87 | 0.074620 | 2,713 | 1,009 | 0.001296 | 🔵 low — common in general English | — |
| 1546 | **wrathful mother** | 2 | 3 | 0.541 | - | 0.052055 | - | 796 | 0.001293 | - | ~ |
| 1547 | **coming** | 1 | 21 | - | 2,026.26 | - | 797 | - | 0.001291 | 🟢 medium — moderately distinctive | — |
| 1548 | **prosperous** | 1 | 6 | - | 997.16 | 0.147887 | 1,472 | 1,507 | 0.001291 | 🟢 medium — moderately distinctive | — |
| 1549 | **meditative** | 1 | 6 | - | 997.16 | 0.148483 | 1,467 | 1,516 | 0.001289 | 🟢 medium — moderately distinctive | ~ |
| 1550 | **omniscience** | 1 | 6 | - | 997.16 | 0.148789 | 1,461 | 1,524 | 0.001289 | 🟢 medium — moderately distinctive | — |
| 1551 | **terror** | 1 | 6 | - | 997.16 | 0.148018 | 1,478 | 1,508 | 0.001288 | 🟢 medium — moderately distinctive | — |
| 1552 | **drom** | 1 | 5 | - | 830.96 | 0.122171 | 1,685 | 1,339 | 0.001288 | 🟢 medium — moderately distinctive | ~ |
| 1553 | **stability** | 1 | 8 | - | 733.27 | 0.106842 | 1,883 | 1,234 | 0.001287 | 🟢 medium — moderately distinctive | — |
| 1554 | **decide** | 1 | 5 | - | 521.94 | 0.083721 | 2,330 | 1,091 | 0.001287 | 🟢 medium — moderately distinctive | — |
| 1555 | **gratitude** | 1 | 6 | - | 997.16 | 0.149070 | 1,451 | 1,539 | 0.001287 | 🟢 medium — moderately distinctive | — |
| 1556 | **black spearman** | 2 | 4 | 0.805 | - | 0.052396 | - | 801 | 0.001286 | - | — |
| 1557 | **asanga** | 1 | 5 | - | 830.96 | 0.109476 | 1,750 | 1,306 | 0.001285 | 🟢 medium — moderately distinctive | ✓ ཐོགས་མེད |
| 1558 | **heavenly** | 1 | 6 | - | 997.16 | 0.148967 | 1,466 | 1,533 | 0.001283 | 🟢 medium — moderately distinctive | — |
| 1559 | **dedicate merit** | 2 | 3 | 0.416 | - | 0.053150 | - | 804 | 0.001282 | - | — |
| 1560 | **shame** | 1 | 6 | - | 997.48 | 0.149437 | 1,441 | 1,566 | 0.001281 | 🟢 medium — moderately distinctive | — |
| 1561 | **weeping** | 1 | 6 | - | 997.16 | 0.148916 | 1,474 | 1,529 | 0.001281 | 🟢 medium — moderately distinctive | — |
| 1562 | **giant** | 1 | 7 | - | 848.00 | 0.125791 | 1,624 | 1,396 | 0.001281 | 🟢 medium — moderately distinctive | — |
| 1563 | **blazing** | 1 | 12 | - | 1,994.97 | - | 806 | - | 0.001279 | 🟢 medium — moderately distinctive | — |
| 1564 | **generally** | 1 | 8 | - | 793.28 | 0.108258 | 1,809 | 1,284 | 0.001279 | 🟢 medium — moderately distinctive | — |
| 1565 | **naked** | 1 | 6 | - | 997.48 | 0.149556 | 1,439 | 1,576 | 0.001278 | 🟢 medium — moderately distinctive | — |
| 1566 | **tendzin** | 1 | 5 | - | 830.96 | 0.110807 | 1,756 | 1,315 | 0.001278 | 🟢 medium — moderately distinctive | — |
| 1567 | **actual practice** | 2 | 3 | 0.431 | - | 0.053815 | - | 807 | 0.001278 | - | — |
| 1568 | **hang** | 1 | 7 | - | 1,079.65 | 0.176413 | 1,389 | 1,642 | 0.001278 | 🟢 medium — moderately distinctive | — |
| 1569 | **ruler** | 1 | 6 | - | 997.16 | 0.149143 | 1,468 | 1,545 | 0.001278 | 🟢 medium — moderately distinctive | — |
| 1570 | **concentrate** | 1 | 7 | - | 778.21 | 0.108208 | 1,820 | 1,282 | 0.001277 | 🟢 medium — moderately distinctive | — |
| 1571 | **connection** | 1 | 9 | - | 953.26 | 0.141701 | 1,541 | 1,474 | 0.001277 | 🟢 medium — moderately distinctive | — |
| 1572 | **profound teaching** | 2 | 3 | 0.331 | - | 0.054041 | - | 808 | 0.001276 | - | ~ |
| 1573 | **hill** | 1 | 8 | - | 954.54 | 0.142410 | 1,537 | 1,479 | 0.001276 | 🟢 medium — moderately distinctive | — |
| 1574 | **drom tonpa** | 2 | 3 | 0.788 | - | 0.054452 | - | 809 | 0.001275 | - | ✓ འབྲོམ་སྟོན་པ |
| 1575 | **task** | 1 | 8 | - | 1,041.69 | 0.171580 | 1,415 | 1,618 | 0.001274 | 🟢 medium — moderately distinctive | — |
| 1576 | **prince** | 1 | 6 | - | 867.22 | 0.129664 | 1,610 | 1,423 | 0.001273 | 🟢 medium — moderately distinctive | — |
| 1577 | **mastery** | 1 | 6 | - | 997.16 | 0.149355 | 1,471 | 1,561 | 0.001270 | 🟢 medium — moderately distinctive | — |
| 1578 | **twenty-one** | 1 | 12 | - | 1,994.32 | - | 814 | - | 0.001269 | 🟢 medium — moderately distinctive | — |
| 1579 | **perfection lineage** | 2 | 3 | 0.457 | - | 0.055340 | - | 814 | 0.001269 | - | ~ |
| 1580 | **boatman** | 1 | 6 | - | 997.16 | 0.149237 | 1,486 | 1,554 | 0.001266 | 🟢 medium — moderately distinctive | — |
| 1581 | **sore** | 1 | 7 | - | 1,163.73 | 0.219609 | 1,279 | 1,865 | 0.001266 | 🟢 medium — moderately distinctive | — |
| 1582 | **jealous** | 1 | 6 | - | 997.16 | 0.149232 | 1,490 | 1,552 | 0.001266 | 🟢 medium — moderately distinctive | — |
| 1583 | **gem** | 1 | 7 | - | 1,030.46 | 0.175592 | 1,420 | 1,636 | 0.001265 | 🟢 medium — moderately distinctive | — |
| 1584 | **bean** | 1 | 7 | - | 927.68 | 0.146072 | 1,554 | 1,492 | 0.001264 | 🟢 medium — moderately distinctive | — |
| 1585 | **atriya** | 1 | 6 | - | 997.16 | 0.149228 | 1,495 | 1,551 | 0.001264 | 🟢 medium — moderately distinctive | — |
| 1586 | **siddhas** | 1 | - | - | - | 0.055457 | - | 818 | 0.001263 | - | — |
| 1587 | **unsurpassable** | 1 | 6 | - | 997.16 | 0.149369 | 1,489 | 1,562 | 0.001262 | 🟢 medium — moderately distinctive | — |
| 1588 | **shore** | 1 | 7 | - | 1,011.76 | 0.176023 | 1,426 | 1,639 | 0.001262 | 🟢 medium — moderately distinctive | — |
| 1589 | **wish-granting** | 1 | 12 | - | 1,994.32 | - | 822 | - | 0.001258 | 🟢 medium — moderately distinctive | — |
| 1590 | **compare** | 1 | 2 | - | 265.05 | 0.065552 | 4,007 | 928 | 0.001258 | 🔵 low — common in general English | — |
| 1591 | **lot** | 1 | 8 | - | 815.13 | 0.122978 | 1,771 | 1,345 | 0.001258 | 🟢 medium — moderately distinctive | — |
| 1592 | **incomparable** | 1 | 6 | - | 997.16 | 0.149501 | 1,493 | 1,571 | 0.001257 | 🟢 medium — moderately distinctive | — |
| 1593 | **purifying** | 1 | 12 | - | 1,994.32 | - | 823 | - | 0.001257 | 🟢 medium — moderately distinctive | — |
| 1594 | **suppose** | 1 | 6 | - | 955.32 | 0.148971 | 1,529 | 1,534 | 0.001257 | 🟢 medium — moderately distinctive | — |
| 1595 | **distant** | 1 | 6 | - | 925.41 | 0.148301 | 1,559 | 1,511 | 0.001254 | 🟢 medium — moderately distinctive | — |
| 1596 | **potential** | 1 | 8 | - | 725.08 | 0.108359 | 1,889 | 1,291 | 0.001253 | 🟢 medium — moderately distinctive | — |
| 1597 | **wool** | 1 | 6 | - | 925.41 | 0.148105 | 1,563 | 1,510 | 0.001253 | 🟢 medium — moderately distinctive | — |
| 1598 | **whip** | 1 | 6 | - | 997.48 | 0.178244 | 1,440 | 1,648 | 0.001252 | 🟢 medium — moderately distinctive | — |
| 1599 | **takaya** | 1 | 6 | - | 997.16 | 0.149598 | 1,503 | 1,578 | 0.001250 | 🟢 medium — moderately distinctive | — |
| 1600 | **emulate** | 1 | 6 | - | 997.16 | 0.168840 | 1,477 | 1,611 | 0.001249 | 🟢 medium — moderately distinctive | — |
| 1601 | **share** | 1 | 10 | - | 491.11 | 0.083269 | 2,665 | 1,074 | 0.001249 | 🔵 low — common in general English | — |
| 1602 | **glorious root** | 2 | 4 | 0.606 | - | 0.055939 | - | 830 | 0.001248 | - | ~ |
| 1603 | **kadampa** | 1 | 7 | - | 1,163.35 | 0.221625 | 1,309 | 1,873 | 0.001248 | 🟢 medium — moderately distinctive | ✓ བཀའ་གདམས་པ |
| 1604 | **quest** | 1 | 6 | - | 925.41 | 0.148891 | 1,561 | 1,527 | 0.001247 | 🟢 medium — moderately distinctive | — |
| 1605 | **millstone** | 1 | 6 | - | 997.16 | 0.178376 | 1,452 | 1,649 | 0.001247 | 🟢 medium — moderately distinctive | — |
| 1606 | **abuse** | 1 | 6 | - | 955.32 | 0.149468 | 1,525 | 1,570 | 0.001244 | 🟢 medium — moderately distinctive | — |
| 1607 | **cloth** | 1 | 6 | - | 955.32 | 0.149401 | 1,534 | 1,563 | 0.001243 | 🟢 medium — moderately distinctive | — |
| 1608 | **indeed** | 1 | 15 | - | 1,953.16 | - | 834 | - | 0.001243 | 🟢 medium — moderately distinctive | — |
| 1609 | **disillusionment** | 1 | 6 | - | 925.41 | 0.148992 | 1,564 | 1,537 | 0.001242 | 🟢 medium — moderately distinctive | — |
| 1610 | **sweet** | 1 | 7 | - | 813.10 | 0.125276 | 1,773 | 1,376 | 0.001242 | 🟢 medium — moderately distinctive | ~ |
| 1611 | **slightly** | 1 | 8 | - | 697.18 | 0.108481 | 1,917 | 1,299 | 0.001242 | 🟢 medium — moderately distinctive | — |
| 1612 | **principal** | 1 | 7 | - | 717.76 | 0.110506 | 1,899 | 1,313 | 0.001239 | 🟢 medium — moderately distinctive | — |
| 1613 | **clarity** | 1 | 6 | - | 955.32 | 0.149632 | 1,533 | 1,580 | 0.001238 | 🟢 medium — moderately distinctive | ~ |
| 1614 | **steady** | 1 | 7 | - | 704.68 | 0.110343 | 1,913 | 1,309 | 0.001237 | 🟢 medium — moderately distinctive | — |
| 1615 | **hermit** | 1 | 6 | - | 997.16 | 0.179406 | 1,462 | 1,664 | 0.001237 | 🟢 medium — moderately distinctive | — |
| 1616 | **dissolution** | 1 | 6 | - | 955.32 | 0.149662 | 1,535 | 1,581 | 0.001236 | 🟢 medium — moderately distinctive | ~ |
| 1617 | **blaze** | 1 | 1 | - | 166.25 | 0.066366 | 4,315 | 933 | 0.001236 | 🔵 low — common in general English | — |
| 1618 | **past generosity** | 2 | 4 | 0.479 | - | 0.056176 | - | 840 | 0.001236 | - | — |
| 1619 | **repay** | 1 | 7 | - | 813.10 | 0.125633 | 1,774 | 1,390 | 0.001235 | 🟢 medium — moderately distinctive | — |
| 1620 | **under** | 1 | 33 | - | 1,915.78 | - | 841 | - | 0.001234 | 🟢 medium — moderately distinctive | — |
| 1621 | **distinction** | 1 | 6 | - | 925.41 | 0.149259 | 1,566 | 1,556 | 0.001234 | 🟢 medium — moderately distinctive | — |
| 1622 | **offered** | 1 | 23 | - | 1,913.80 | - | 842 | - | 0.001233 | 🟢 medium — moderately distinctive | — |
| 1623 | **cattle** | 1 | 7 | - | 775.70 | 0.124980 | 1,821 | 1,367 | 0.001232 | 🟢 medium — moderately distinctive | — |
| 1624 | **tale** | 1 | 6 | - | 997.16 | 0.178740 | 1,483 | 1,652 | 0.001232 | 🟢 medium — moderately distinctive | — |
| 1625 | **harmful act** | 2 | 7 | 0.536 | - | 0.056306 | - | 843 | 0.001232 | - | — |
| 1626 | **delight** | 1 | 6 | - | 997.16 | 0.179054 | 1,479 | 1,659 | 0.001232 | 🟢 medium — moderately distinctive | — |
| 1627 | **guest** | 1 | 6 | - | 997.16 | 0.179313 | 1,482 | 1,663 | 0.001229 | 🟢 medium — moderately distinctive | — |
| 1628 | **soup** | 1 | 6 | - | 925.41 | 0.149451 | 1,567 | 1,568 | 0.001229 | 🟢 medium — moderately distinctive | — |
| 1629 | **drive** | 1 | 4 | - | 446.15 | 0.083444 | 2,778 | 1,081 | 0.001229 | 🔵 low — common in general English | — |
| 1630 | **cure** | 1 | 6 | - | 867.22 | 0.148960 | 1,606 | 1,532 | 0.001228 | 🟢 medium — moderately distinctive | — |
| 1631 | **omniscient longchenpa** | 2 | 3 | 0.777 | - | 0.056504 | - | 846 | 0.001228 | - | ~ |
| 1632 | **talk** | 1 | 4 | - | 424.75 | 0.083287 | 2,823 | 1,075 | 0.001228 | 🔵 low — common in general English | — |
| 1633 | **human birth** | 2 | 4 | 0.481 | - | 0.056713 | - | 849 | 0.001225 | - | — |
| 1634 | **leather** | 1 | 6 | - | 867.22 | 0.149114 | 1,609 | 1,543 | 0.001223 | 🟢 medium — moderately distinctive | — |
| 1635 | **mirror** | 1 | 6 | - | 902.21 | 0.149438 | 1,584 | 1,567 | 0.001223 | 🟢 medium — moderately distinctive | — |
| 1636 | **spite** | 1 | 6 | - | 853.34 | 0.148983 | 1,619 | 1,536 | 0.001222 | 🟢 medium — moderately distinctive | — |
| 1637 | **committed** | 1 | 18 | - | 1,897.07 | - | 851 | - | 0.001222 | 🟢 medium — moderately distinctive | — |
| 1638 | **invocation** | 1 | 4 | - | 664.77 | 0.108680 | 1,990 | 1,302 | 0.001222 | 🟢 medium — moderately distinctive | — |
| 1639 | **queen** | 1 | 6 | - | 925.41 | 0.155583 | 1,560 | 1,594 | 0.001222 | 🟢 medium — moderately distinctive | — |
| 1640 | **busy** | 1 | 6 | - | 867.22 | 0.149202 | 1,608 | 1,550 | 0.001221 | 🟢 medium — moderately distinctive | — |
| 1641 | **sever** | 1 | 6 | - | 997.16 | 0.179429 | 1,502 | 1,665 | 0.001220 | 🟢 medium — moderately distinctive | — |
| 1642 | **caught** | 1 | 14 | - | 1,892.75 | - | 853 | - | 0.001220 | 🟢 medium — moderately distinctive | — |
| 1643 | **vajra posture** | 2 | 4 | 0.650 | - | 0.057190 | - | 853 | 0.001220 | - | ✓ རྡོ་རྗེ་དཀྱིལ་ཀྲུང |
| 1644 | **pour** | 1 | 3 | - | 462.71 | 0.083975 | 2,735 | 1,101 | 0.001219 | 🔵 low — common in general English | — |
| 1645 | **hit** | 1 | 8 | - | 706.90 | 0.123401 | 1,912 | 1,349 | 0.001217 | 🟢 medium — moderately distinctive | — |
| 1646 | **knew** | 1 | 13 | - | 1,878.98 | - | 856 | - | 0.001216 | 🟢 medium — moderately distinctive | — |
| 1647 | **met** | 1 | 20 | - | 1,878.12 | - | 857 | - | 0.001215 | 🟢 medium — moderately distinctive | — |
| 1648 | **ready** | 1 | 7 | - | 739.57 | 0.125358 | 1,866 | 1,378 | 0.001215 | 🟢 medium — moderately distinctive | — |
| 1649 | **wrong thought** | 2 | 4 | 0.369 | - | 0.059386 | - | 858 | 0.001214 | - | ~ |
| 1650 | **symbolize** | 1 | 4 | - | 664.99 | 0.118111 | 1,969 | 1,329 | 0.001213 | 🟢 medium — moderately distinctive | — |
| 1651 | **focus** | 1 | 7 | - | 755.25 | 0.125723 | 1,845 | 1,394 | 0.001213 | 🟢 medium — moderately distinctive | — |
| 1652 | **dangerous** | 1 | 6 | - | 795.15 | 0.128285 | 1,808 | 1,417 | 0.001212 | 🟢 medium — moderately distinctive | — |
| 1653 | **inferior** | 1 | 6 | - | 955.32 | 0.179261 | 1,526 | 1,662 | 0.001211 | 🟢 medium — moderately distinctive | — |
| 1654 | **defeat** | 1 | 6 | - | 841.09 | 0.149289 | 1,630 | 1,557 | 0.001210 | 🟢 medium — moderately distinctive | — |
| 1655 | **application** | 1 | 7 | - | 749.13 | 0.125733 | 1,861 | 1,395 | 0.001208 | 🟢 medium — moderately distinctive | — |
| 1656 | **garment** | 1 | 7 | - | 1,079.65 | 0.220395 | 1,392 | 1,868 | 0.001207 | 🟢 medium — moderately distinctive | — |
| 1657 | **leaving** | 1 | 17 | - | 1,855.23 | - | 865 | - | 0.001205 | 🟢 medium — moderately distinctive | — |
| 1658 | **swiftly** | 1 | 6 | - | 853.34 | 0.149604 | 1,621 | 1,579 | 0.001205 | 🟢 medium — moderately distinctive | — |
| 1659 | **seen** | 1 | 23 | - | 1,852.60 | - | 867 | - | 0.001203 | 🟢 medium — moderately distinctive | — |
| 1660 | **describe** | 1 | 6 | - | 925.41 | 0.178542 | 1,558 | 1,650 | 0.001203 | 🟢 medium — moderately distinctive | — |
| 1661 | **interest** | 1 | 9 | - | 555.63 | 0.106237 | 2,288 | 1,229 | 0.001202 | 🟢 medium — moderately distinctive | — |
| 1662 | **watch** | 1 | 6 | - | 763.40 | 0.129108 | 1,841 | 1,421 | 0.001201 | 🟢 medium — moderately distinctive | — |
| 1663 | **gate** | 1 | 7 | - | 1,052.58 | 0.220532 | 1,408 | 1,869 | 0.001200 | 🟢 medium — moderately distinctive | — |
| 1664 | **answer** | 1 | 6 | - | 702.89 | 0.125433 | 1,914 | 1,383 | 0.001200 | 🟢 medium — moderately distinctive | — |
| 1665 | **mouse** | 1 | 6 | - | 955.32 | 0.181425 | 1,532 | 1,690 | 0.001200 | 🟢 medium — moderately distinctive | — |
| 1666 | **belong** | 1 | 6 | - | 925.41 | 0.179132 | 1,557 | 1,661 | 0.001199 | 🟢 medium — moderately distinctive | — |
| 1667 | **nepal** | 1 | 4 | - | 664.99 | 0.125223 | 1,938 | 1,372 | 0.001199 | 🟢 medium — moderately distinctive | — |
| 1668 | **wishing** | 1 | 12 | - | 1,850.82 | - | 871 | - | 0.001199 | 🟢 medium — moderately distinctive | — |
| 1669 | **started** | 1 | 20 | - | 1,845.08 | - | 873 | - | 0.001196 | 🟢 medium — moderately distinctive | — |
| 1670 | **cease** | 1 | 6 | - | 820.23 | 0.143959 | 1,766 | 1,483 | 0.001196 | 🟢 medium — moderately distinctive | — |
| 1671 | **profit** | 1 | 9 | - | 519.33 | 0.105943 | 2,335 | 1,226 | 0.001195 | 🟢 medium — moderately distinctive | — |
| 1672 | **happened** | 1 | 15 | - | 1,837.15 | - | 875 | - | 0.001194 | 🟢 medium — moderately distinctive | — |
| 1673 | **terrify** | 1 | 2 | - | 332.39 | 0.082265 | 3,301 | 1,056 | 0.001194 | 🔵 low — common in general English | — |
| 1674 | **holding** | 1 | 22 | - | 1,835.37 | - | 876 | - | 0.001193 | 🟢 medium — moderately distinctive | — |
| 1675 | **prayer beginning** | 2 | 4 | 0.490 | - | 0.061038 | - | 876 | 0.001193 | - | — |
| 1676 | **trap** | 1 | 4 | - | 664.77 | 0.124388 | 1,987 | 1,360 | 0.001193 | 🟢 medium — moderately distinctive | — |
| 1677 | **manifest** | 1 | 11 | - | 1,828.72 | - | 877 | - | 0.001192 | 🟢 medium — moderately distinctive | ~ |
| 1678 | **lotus family** | 2 | 3 | 0.584 | - | 0.061098 | - | 878 | 0.001190 | - | — |
| 1679 | **foolish** | 1 | 5 | - | 771.18 | 0.135321 | 1,828 | 1,454 | 0.001190 | 🟢 medium — moderately distinctive | — |
| 1680 | **attaining** | 1 | 11 | - | 1,828.72 | - | 879 | - | 0.001189 | 🟢 medium — moderately distinctive | — |
| 1681 | **fight** | 1 | 6 | - | 712.49 | 0.127008 | 1,903 | 1,412 | 0.001189 | 🟢 medium — moderately distinctive | — |
| 1682 | **courage** | 1 | 5 | - | 831.24 | 0.155256 | 1,653 | 1,593 | 0.001189 | 🟢 medium — moderately distinctive | — |
| 1683 | **hole** | 1 | 6 | - | 830.14 | 0.147612 | 1,758 | 1,506 | 0.001189 | 🟢 medium — moderately distinctive | — |
| 1684 | **waste** | 1 | 7 | - | 797.33 | 0.145488 | 1,789 | 1,489 | 0.001186 | 🟢 medium — moderately distinctive | — |
| 1685 | **pea** | 1 | 6 | - | 997.48 | 0.222860 | 1,437 | 1,882 | 0.001183 | 🟢 medium — moderately distinctive | — |
| 1686 | **content** | 1 | 7 | - | 835.22 | 0.175501 | 1,636 | 1,632 | 0.001181 | 🟢 medium — moderately distinctive | — |
| 1687 | **seventh** | 1 | 6 | - | 811.18 | 0.148308 | 1,777 | 1,513 | 0.001180 | 🟢 medium — moderately distinctive | — |
| 1688 | **machik** | 1 | 5 | - | 830.96 | 0.156950 | 1,674 | 1,599 | 0.001179 | 🟢 medium — moderately distinctive | ~ |
| 1689 | **type** | 1 | 7 | - | 839.33 | 0.175937 | 1,634 | 1,638 | 0.001179 | 🟢 medium — moderately distinctive | — |
| 1690 | **nonetheless** | 1 | 6 | - | 820.23 | 0.148830 | 1,764 | 1,525 | 0.001179 | 🟢 medium — moderately distinctive | — |
| 1691 | **art** | 1 | 6 | - | 853.34 | 0.178857 | 1,618 | 1,656 | 0.001179 | 🟢 medium — moderately distinctive | — |
| 1692 | **laziness** | 1 | 5 | - | 830.96 | 0.154540 | 1,687 | 1,590 | 0.001178 | 🟢 medium — moderately distinctive | — |
| 1693 | **refuse** | 1 | 4 | - | 578.15 | 0.108190 | 2,257 | 1,279 | 0.001178 | 🟢 medium — moderately distinctive | — |
| 1694 | **command** | 1 | 6 | - | 841.09 | 0.178589 | 1,629 | 1,651 | 0.001177 | 🟢 medium — moderately distinctive | — |
| 1695 | **hallucination** | 1 | 6 | - | 997.16 | 0.223669 | 1,449 | 1,887 | 0.001176 | 🟢 medium — moderately distinctive | — |
| 1696 | **tsa-tsa** | 1 | 11 | - | 1,828.12 | - | 891 | - | 0.001176 | 🟢 medium — moderately distinctive | ✓ ཙ་ཙ |
| 1697 | **plenty** | 1 | 6 | - | 830.14 | 0.149148 | 1,760 | 1,546 | 0.001172 | 🟢 medium — moderately distinctive | — |
| 1698 | **turquoise** | 1 | 5 | - | 830.96 | 0.153635 | 1,711 | 1,588 | 0.001171 | 🟢 medium — moderately distinctive | — |
| 1699 | **shepherd** | 1 | 6 | - | 997.16 | 0.223865 | 1,459 | 1,889 | 0.001171 | 🟢 medium — moderately distinctive | — |
| 1700 | **pay** | 1 | 8 | - | 500.20 | 0.107870 | 2,358 | 1,261 | 0.001171 | 🟢 medium — moderately distinctive | — |
| 1701 | **boat** | 1 | 6 | - | 830.14 | 0.149234 | 1,762 | 1,553 | 0.001169 | 🟢 medium — moderately distinctive | — |
| 1702 | **permanence** | 1 | 5 | - | 831.24 | 0.180369 | 1,642 | 1,668 | 0.001166 | 🟢 medium — moderately distinctive | — |
| 1703 | **ambition** | 1 | 6 | - | 997.16 | 0.223507 | 1,473 | 1,886 | 0.001166 | 🟢 medium — moderately distinctive | — |
| 1704 | **flock** | 1 | 6 | - | 997.16 | 0.223217 | 1,475 | 1,883 | 0.001166 | 🟢 medium — moderately distinctive | — |
| 1705 | **circle** | 1 | 6 | - | 802.86 | 0.149141 | 1,784 | 1,544 | 0.001166 | 🟢 medium — moderately distinctive | — |
| 1706 | **friendship** | 1 | 5 | - | 831.24 | 0.180327 | 1,646 | 1,667 | 0.001165 | 🟢 medium — moderately distinctive | — |
| 1707 | **relative bodhicitta** | 2 | 4 | 0.507 | - | 0.061820 | - | 901 | 0.001165 | - | ~ |
| 1708 | **sovereign** | 1 | 5 | - | 691.78 | 0.136841 | 1,918 | 1,458 | 0.001164 | 🟢 medium — moderately distinctive | — |
| 1709 | **basic** | 1 | 6 | - | 589.68 | 0.112772 | 2,237 | 1,317 | 0.001162 | 🟢 medium — moderately distinctive | — |
| 1710 | **escape death** | 2 | 3 | 0.503 | - | 0.062510 | - | 905 | 0.001161 | - | — |
| 1711 | **choose** | 1 | 6 | - | 763.40 | 0.148531 | 1,839 | 1,518 | 0.001160 | 🟢 medium — moderately distinctive | — |
| 1712 | **marriage** | 1 | 5 | - | 831.24 | 0.181456 | 1,639 | 1,692 | 0.001159 | 🟢 medium — moderately distinctive | — |
| 1713 | **joyous** | 1 | 4 | - | 664.77 | 0.131719 | 1,994 | 1,428 | 0.001159 | 🟢 medium — moderately distinctive | ~ |
| 1714 | **billion** | 1 | 9 | - | 445.19 | 0.094762 | 2,779 | 1,180 | 0.001159 | 🔵 low — common in general English | ~ |
| 1715 | **swan** | 1 | 6 | - | 997.16 | 0.224425 | 1,488 | 1,895 | 0.001158 | 🟢 medium — moderately distinctive | — |
| 1716 | **asariga** | 1 | 5 | - | 830.96 | 0.156255 | 1,749 | 1,595 | 0.001157 | 🟢 medium — moderately distinctive | — |
| 1717 | **samye** | 1 | 4 | - | 664.77 | 0.132866 | 1,991 | 1,434 | 0.001157 | 🟢 medium — moderately distinctive | ✓ བསམ་ཡས |
| 1718 | **incapable** | 1 | 5 | - | 831.24 | 0.181558 | 1,640 | 1,699 | 0.001157 | 🟢 medium — moderately distinctive | — |
| 1719 | **spontaneous** | 1 | 5 | - | 830.96 | 0.156990 | 1,745 | 1,600 | 0.001156 | 🟢 medium — moderately distinctive | — |
| 1720 | **gyaltsen** | 1 | 4 | - | 664.77 | 0.132238 | 2,003 | 1,429 | 0.001156 | 🟢 medium — moderately distinctive | ~ |
| 1721 | **rotten** | 1 | 5 | - | 830.96 | 0.156784 | 1,751 | 1,598 | 0.001155 | 🟢 medium — moderately distinctive | — |
| 1722 | **distress** | 1 | 5 | - | 831.24 | 0.181515 | 1,650 | 1,696 | 0.001154 | 🟢 medium — moderately distinctive | — |
| 1723 | **ordinary speech** | 2 | 3 | 0.398 | - | 0.063100 | - | 911 | 0.001154 | - | ~ |
| 1724 | **exceptional** | 1 | 6 | - | 769.02 | 0.148972 | 1,837 | 1,535 | 0.001154 | 🟢 medium — moderately distinctive | — |
| 1725 | **sack** | 1 | 5 | - | 830.96 | 0.181133 | 1,672 | 1,676 | 0.001153 | 🟢 medium — moderately distinctive | — |
| 1726 | **wonder** | 1 | 12 | - | 1,804.42 | - | 912 | - | 0.001153 | 🟢 medium — moderately distinctive | — |
| 1727 | **intermediate kalpa** | 2 | 3 | 0.486 | - | 0.063786 | - | 912 | 0.001153 | - | ~ |
| 1728 | **entourage** | 1 | 5 | - | 831.24 | 0.181905 | 1,643 | 1,709 | 0.001152 | 🟢 medium — moderately distinctive | — |
| 1729 | **circum** | 1 | 5 | - | 830.96 | 0.180441 | 1,682 | 1,670 | 0.001152 | 🟢 medium — moderately distinctive | — |
| 1730 | **second** | 1 | 24 | - | 1,800.02 | - | 914 | - | 0.001151 | 🟢 medium — moderately distinctive | ~ |
| 1731 | **beginningless** | 1 | 5 | - | 830.96 | 0.181254 | 1,677 | 1,682 | 0.001150 | 🟢 medium — moderately distinctive | — |
| 1732 | **wisdom nectar** | 2 | 3 | 0.421 | - | 0.064269 | - | 916 | 0.001149 | - | — |
| 1733 | **putting** | 1 | 16 | - | 1,790.56 | - | 917 | - | 0.001148 | 🟢 medium — moderately distinctive | — |
| 1734 | **yeshe** | 1 | 4 | - | 664.77 | 0.132532 | 2,038 | 1,432 | 0.001147 | 🟢 medium — moderately distinctive | ~ |
| 1735 | **shang** | 1 | 4 | - | 664.77 | 0.132308 | 2,042 | 1,431 | 0.001146 | 🟢 medium — moderately distinctive | ~ |
| 1736 | **tsogyal** | 1 | 4 | - | 664.77 | 0.132549 | 2,039 | 1,433 | 0.001146 | 🟢 medium — moderately distinctive | ~ |
| 1737 | **proverb** | 1 | 5 | - | 830.96 | 0.181586 | 1,670 | 1,701 | 0.001146 | 🟢 medium — moderately distinctive | — |
| 1738 | **fame** | 1 | 5 | - | 830.96 | 0.181727 | 1,667 | 1,705 | 0.001146 | 🟢 medium — moderately distinctive | — |
| 1739 | **central channel** | 2 | 11 | 0.797 | - | 0.064975 | - | 920 | 0.001145 | - | ✓ རྩ་དབུ་མ |
| 1740 | **purnakasyapa** | 1 | 4 | - | 664.77 | 0.131041 | 2,065 | 1,425 | 0.001144 | 🟢 medium — moderately distinctive | — |
| 1741 | **molten** | 1 | 5 | - | 830.96 | 0.180688 | 1,706 | 1,671 | 0.001144 | 🟢 medium — moderately distinctive | — |
| 1742 | **nail** | 1 | 6 | - | 955.32 | 0.223692 | 1,527 | 1,888 | 0.001143 | 🟢 medium — moderately distinctive | — |
| 1743 | **ravati** | 1 | 4 | - | 664.77 | 0.131104 | 2,066 | 1,426 | 0.001143 | 🟢 medium — moderately distinctive | — |
| 1744 | **spearman** | 1 | 4 | - | 664.77 | 0.131225 | 2,064 | 1,427 | 0.001143 | 🟢 medium — moderately distinctive | — |
| 1745 | **blow** | 1 | 7 | - | 946.38 | 0.219814 | 1,543 | 1,867 | 0.001143 | 🟢 medium — moderately distinctive | — |
| 1746 | **smallest** | 1 | 12 | - | 1,766.50 | - | 922 | - | 0.001143 | 🟢 medium — moderately distinctive | — |
| 1747 | **womb** | 1 | 5 | - | 830.96 | 0.181176 | 1,702 | 1,679 | 0.001143 | 🟢 medium — moderately distinctive | — |
| 1748 | **captain** | 1 | 5 | - | 796.10 | 0.155150 | 1,802 | 1,592 | 0.001142 | 🟢 medium — moderately distinctive | — |
| 1749 | **srona** | 1 | 4 | - | 664.77 | 0.141657 | 1,983 | 1,473 | 0.001142 | 🟢 medium — moderately distinctive | — |
| 1750 | **noble land** | 2 | 3 | 0.500 | - | 0.065046 | - | 923 | 0.001142 | - | ~ |
| 1751 | **unchanging** | 1 | 5 | - | 830.96 | 0.181823 | 1,680 | 1,707 | 0.001141 | 🟢 medium — moderately distinctive | — |
| 1752 | **add** | 1 | 7 | - | 664.06 | 0.125986 | 2,124 | 1,406 | 0.001140 | 🟢 medium — moderately distinctive | — |
| 1753 | **sublime katyayana** | 2 | 4 | 0.723 | - | 0.065205 | - | 925 | 0.001140 | - | ~ |
| 1754 | **swallow** | 1 | 5 | - | 830.96 | 0.181229 | 1,712 | 1,681 | 0.001139 | 🟢 medium — moderately distinctive | — |
| 1755 | **write** | 1 | 3 | - | 376.50 | 0.096051 | 2,917 | 1,186 | 0.001138 | 🔵 low — common in general English | — |
| 1756 | **par** | 1 | 6 | - | 715.90 | 0.148934 | 1,902 | 1,531 | 0.001138 | 🟢 medium — moderately distinctive | — |
| 1757 | **courageous** | 1 | 5 | - | 831.24 | 0.182265 | 1,660 | 1,737 | 0.001138 | 🟢 medium — moderately distinctive | — |
| 1758 | **hearing** | 1 | 16 | - | 1,736.01 | - | 927 | - | 0.001138 | 🟢 medium — moderately distinctive | ~ |
| 1759 | **ship** | 1 | 8 | - | 802.23 | 0.172654 | 1,786 | 1,623 | 0.001136 | 🟢 medium — moderately distinctive | — |
| 1760 | **delicious** | 1 | 5 | - | 830.96 | 0.181401 | 1,713 | 1,689 | 0.001136 | 🟢 medium — moderately distinctive | — |
| 1761 | **day tilopa** | 2 | 3 | 0.410 | - | 0.065866 | - | 929 | 0.001136 | - | — |
| 1762 | **visible** | 1 | 6 | - | 743.53 | 0.149404 | 1,865 | 1,564 | 0.001135 | 🟢 medium — moderately distinctive | — |
| 1763 | **vessel** | 1 | 7 | - | 820.04 | 0.176160 | 1,767 | 1,641 | 0.001135 | 🟢 medium — moderately distinctive | — |
| 1764 | **succession** | 1 | 5 | - | 831.24 | 0.182311 | 1,659 | 1,747 | 0.001135 | 🟢 medium — moderately distinctive | — |
| 1765 | **influence** | 1 | 8 | - | 907.89 | 0.214284 | 1,579 | 1,850 | 0.001134 | 🟢 medium — moderately distinctive | — |
| 1766 | **celestial realm** | 2 | 6 | 0.635 | - | 0.066287 | - | 931 | 0.001133 | - | — |
| 1767 | **khampa** | 1 | 4 | - | 664.77 | 0.133200 | 2,094 | 1,435 | 0.001133 | 🟢 medium — moderately distinctive | ~ |
| 1768 | **persevere** | 1 | 5 | - | 830.96 | 0.182233 | 1,676 | 1,736 | 0.001133 | 🟢 medium — moderately distinctive | — |
| 1769 | **radiant** | 1 | 5 | - | 830.96 | 0.182197 | 1,684 | 1,729 | 0.001132 | 🟢 medium — moderately distinctive | — |
| 1770 | **move** | 1 | 13 | - | 988.82 | 0.231353 | 1,508 | 1,962 | 0.001132 | 🟢 medium — moderately distinctive | — |
| 1771 | **crucial** | 1 | 6 | - | 715.90 | 0.149191 | 1,901 | 1,547 | 0.001132 | 🟢 medium — moderately distinctive | — |
| 1772 | **attack** | 1 | 7 | - | 729.02 | 0.149302 | 1,885 | 1,558 | 0.001132 | 🟢 medium — moderately distinctive | — |
| 1773 | **anguish** | 1 | 5 | - | 830.96 | 0.181498 | 1,720 | 1,694 | 0.001132 | 🟢 medium — moderately distinctive | — |
| 1774 | **maitriyogi** | 1 | 4 | - | 664.77 | 0.133613 | 2,099 | 1,438 | 0.001131 | 🟢 medium — moderately distinctive | ✓ བྱམས་པའི་རྣལ་འབྱོར་པ |
| 1775 | **perna** | 1 | 4 | - | 664.77 | 0.134442 | 2,089 | 1,443 | 0.001131 | 🟢 medium — moderately distinctive | — |
| 1776 | **mustard** | 1 | 5 | - | 830.96 | 0.181677 | 1,716 | 1,704 | 0.001130 | 🟢 medium — moderately distinctive | — |
| 1777 | **trickery** | 1 | 5 | - | 830.96 | 0.181482 | 1,728 | 1,693 | 0.001130 | 🟢 medium — moderately distinctive | — |
| 1778 | **threefold** | 1 | 5 | - | 830.96 | 0.182119 | 1,695 | 1,726 | 0.001130 | 🟢 medium — moderately distinctive | ~ |
| 1779 | **rinchen** | 1 | 4 | - | 664.77 | 0.134083 | 2,103 | 1,440 | 0.001129 | 🟢 medium — moderately distinctive | ~ |
| 1780 | **consume** | 1 | 5 | - | 751.84 | 0.154789 | 1,851 | 1,591 | 0.001129 | 🟢 medium — moderately distinctive | — |
| 1781 | **asleep** | 1 | 5 | - | 830.96 | 0.182086 | 1,703 | 1,723 | 0.001128 | 🟢 medium — moderately distinctive | — |
| 1782 | **infallible** | 1 | 5 | - | 831.24 | 0.182460 | 1,661 | 1,770 | 0.001128 | 🟢 medium — moderately distinctive | — |
| 1783 | **message** | 1 | 7 | - | 890.63 | 0.219353 | 1,587 | 1,862 | 0.001127 | 🟢 medium — moderately distinctive | — |
| 1784 | **mar** | 1 | 6 | - | 667.03 | 0.149021 | 1,934 | 1,538 | 0.001127 | 🟢 medium — moderately distinctive | — |
| 1785 | **lady** | 1 | 4 | - | 664.77 | 0.134336 | 2,109 | 1,441 | 0.001127 | 🟢 medium — moderately distinctive | — |
| 1786 | **daily** | 1 | 7 | - | 617.19 | 0.125952 | 2,189 | 1,405 | 0.001127 | 🟢 medium — moderately distinctive | — |
| 1787 | **mafijusri** | 1 | 4 | - | 664.77 | 0.134861 | 2,095 | 1,448 | 0.001127 | 🟢 medium — moderately distinctive | — |
| 1788 | **arrange** | 1 | 3 | - | 341.71 | 0.098349 | 2,966 | 1,196 | 0.001127 | 🔵 low — common in general English | — |
| 1789 | **dirty** | 1 | 5 | - | 831.24 | 0.182532 | 1,654 | 1,781 | 0.001127 | 🟢 medium — moderately distinctive | — |
| 1790 | **twofold** | 1 | 5 | - | 830.96 | 0.182476 | 1,665 | 1,771 | 0.001126 | 🟢 medium — moderately distinctive | ~ |
| 1791 | **dumb** | 1 | 5 | - | 830.96 | 0.182449 | 1,669 | 1,768 | 0.001125 | 🟢 medium — moderately distinctive | — |
| 1792 | **across** | 1 | 15 | - | 1,690.20 | - | 939 | - | 0.001125 | 🟢 medium — moderately distinctive | — |
| 1793 | **unimaginable** | 1 | 5 | - | 830.96 | 0.182135 | 1,708 | 1,727 | 0.001125 | 🟢 medium — moderately distinctive | — |
| 1794 | **final** | 1 | 7 | - | 571.87 | 0.125397 | 2,264 | 1,380 | 0.001125 | 🟢 medium — moderately distinctive | — |
| 1795 | **gyalpo** | 1 | 4 | - | 664.77 | 0.144073 | 2,037 | 1,484 | 0.001125 | 🟢 medium — moderately distinctive | ~ |
| 1796 | **keeping** | 1 | 15 | - | 1,684.36 | - | 940 | - | 0.001124 | 🟢 medium — moderately distinctive | — |
| 1797 | **tsang** | 1 | 4 | - | 636.88 | 0.130748 | 2,163 | 1,424 | 0.001124 | 🟢 medium — moderately distinctive | — |
| 1798 | **decadent** | 1 | 5 | - | 830.96 | 0.182357 | 1,689 | 1,752 | 0.001124 | 🟢 medium — moderately distinctive | — |
| 1799 | **gathered** | 1 | 12 | - | 1,682.18 | - | 941 | - | 0.001123 | 🟢 medium — moderately distinctive | — |
| 1800 | **vajrapar** | 1 | 4 | - | 664.77 | 0.134782 | 2,119 | 1,445 | 0.001123 | 🟢 medium — moderately distinctive | — |
| 1801 | **sandal** | 1 | 5 | - | 830.96 | 0.181775 | 1,735 | 1,706 | 0.001123 | 🟢 medium — moderately distinctive | — |
| 1802 | **pisaka** | 1 | 4 | - | 664.77 | 0.134799 | 2,118 | 1,446 | 0.001123 | 🟢 medium — moderately distinctive | — |
| 1803 | **array** | 1 | 4 | - | 636.88 | 0.132297 | 2,156 | 1,430 | 0.001122 | 🟢 medium — moderately distinctive | — |
| 1804 | **displease** | 1 | 5 | - | 830.96 | 0.182073 | 1,723 | 1,721 | 0.001122 | 🟢 medium — moderately distinctive | — |
| 1805 | **emaho** | 1 | 4 | - | 664.77 | 0.134884 | 2,116 | 1,449 | 0.001122 | 🟢 medium — moderately distinctive | — |
| 1806 | **wait** | 1 | 6 | - | 671.46 | 0.149251 | 1,931 | 1,555 | 0.001121 | 🟢 medium — moderately distinctive | — |
| 1807 | **got** | 1 | 15 | - | 1,673.06 | - | 943 | - | 0.001121 | 🟢 medium — moderately distinctive | — |
| 1808 | **spent** | 1 | 15 | - | 1,673.06 | - | 944 | - | 0.001120 | 🟢 medium — moderately distinctive | — |
| 1809 | **dzogchen** | 1 | 4 | - | 664.77 | 0.134998 | 2,122 | 1,451 | 0.001120 | 🟢 medium — moderately distinctive | — |
| 1810 | **scholar** | 1 | 5 | - | 830.96 | 0.182428 | 1,691 | 1,762 | 0.001120 | 🟢 medium — moderately distinctive | — |
| 1811 | **potowa** | 1 | 4 | - | 664.77 | 0.147274 | 2,024 | 1,503 | 0.001120 | 🟢 medium — moderately distinctive | ~ |
| 1812 | **true realization** | 2 | 3 | 0.412 | - | 0.067227 | - | 945 | 0.001119 | - | — |
| 1813 | **rage** | 1 | 5 | - | 830.96 | 0.182284 | 1,714 | 1,741 | 0.001119 | 🟢 medium — moderately distinctive | — |
| 1814 | **malaya** | 1 | 4 | - | 636.88 | 0.133577 | 2,166 | 1,437 | 0.001117 | 🟢 medium — moderately distinctive | — |
| 1815 | **homage** | 1 | 5 | - | 830.96 | 0.182086 | 1,737 | 1,724 | 0.001117 | 🟢 medium — moderately distinctive | — |
| 1816 | **incalculable** | 1 | 5 | - | 796.10 | 0.180759 | 1,794 | 1,672 | 0.001117 | 🟢 medium — moderately distinctive | — |
| 1817 | **rank** | 1 | 6 | - | 787.98 | 0.178853 | 1,814 | 1,655 | 0.001117 | 🟢 medium — moderately distinctive | — |
| 1818 | **horn** | 1 | 5 | - | 796.10 | 0.181025 | 1,791 | 1,675 | 0.001117 | 🟢 medium — moderately distinctive | — |
| 1819 | **eastern** | 1 | 6 | - | 608.85 | 0.129479 | 2,208 | 1,422 | 0.001116 | 🟢 medium — moderately distinctive | — |
| 1820 | **absolute bodhicitta** | 2 | 3 | 0.434 | - | 0.067349 | - | 949 | 0.001115 | - | ~ |
| 1821 | **terribly** | 1 | 5 | - | 796.10 | 0.180987 | 1,798 | 1,674 | 0.001115 | 🟢 medium — moderately distinctive | — |
| 1822 | **dispel** | 1 | 5 | - | 831.24 | 0.194215 | 1,648 | 1,831 | 0.001114 | 🟢 medium — moderately distinctive | — |
| 1823 | **pouring** | 1 | 10 | - | 1,662.47 | - | 951 | - | 0.001114 | 🟢 medium — moderately distinctive | — |
| 1824 | **illusory** | 1 | 5 | - | 796.10 | 0.181305 | 1,792 | 1,684 | 0.001113 | 🟢 medium — moderately distinctive | — |
| 1825 | **heartfelt** | 1 | 5 | - | 830.96 | 0.182294 | 1,734 | 1,743 | 0.001112 | 🟢 medium — moderately distinctive | — |
| 1826 | **immortality** | 1 | 5 | - | 830.96 | 0.182578 | 1,699 | 1,786 | 0.001110 | 🟢 medium — moderately distinctive | — |
| 1827 | **incense** | 1 | 5 | - | 830.96 | 0.182305 | 1,738 | 1,746 | 0.001110 | 🟢 medium — moderately distinctive | — |
| 1828 | **bonpo** | 1 | 6 | - | 997.16 | 0.273425 | 1,484 | 2,112 | 0.001108 | 🟢 medium — moderately distinctive | ✓ བོན་པོ |
| 1829 | **wave** | 1 | 6 | - | 752.99 | 0.178800 | 1,847 | 1,654 | 0.001108 | 🟢 medium — moderately distinctive | — |
| 1830 | **openly** | 1 | 5 | - | 796.10 | 0.181529 | 1,799 | 1,697 | 0.001107 | 🟢 medium — moderately distinctive | — |
| 1831 | **stronghold** | 1 | 5 | - | 830.96 | 0.182669 | 1,704 | 1,794 | 0.001106 | 🟢 medium — moderately distinctive | — |
| 1832 | **perseverance** | 1 | 5 | - | 830.96 | 0.182389 | 1,740 | 1,758 | 0.001106 | 🟢 medium — moderately distinctive | — |
| 1833 | **ati** | 1 | 4 | - | 664.99 | 0.150427 | 1,954 | 1,583 | 0.001105 | 🟢 medium — moderately distinctive | — |
| 1834 | **medi** | 1 | 5 | - | 830.96 | 0.182312 | 1,752 | 1,748 | 0.001105 | 🟢 medium — moderately distinctive | — |
| 1835 | **spoil** | 1 | 5 | - | 830.96 | 0.194355 | 1,675 | 1,833 | 0.001105 | 🟢 medium — moderately distinctive | — |
| 1836 | **grasp** | 1 | 4 | - | 664.77 | 0.149407 | 1,984 | 1,565 | 0.001105 | 🟢 medium — moderately distinctive | — |
| 1837 | **painful** | 1 | 5 | - | 771.18 | 0.181163 | 1,833 | 1,678 | 0.001104 | 🟢 medium — moderately distinctive | — |
| 1838 | **cried** | 1 | 10 | - | 1,661.93 | - | 962 | - | 0.001103 | 🟢 medium — moderately distinctive | — |
| 1839 | **certainty** | 1 | 5 | - | 771.18 | 0.181352 | 1,829 | 1,686 | 0.001102 | 🟢 medium — moderately distinctive | — |
| 1840 | **condensed** | 1 | 10 | - | 1,661.93 | - | 964 | - | 0.001101 | 🟢 medium — moderately distinctive | — |
| 1841 | **rush** | 1 | 6 | - | 811.18 | 0.182268 | 1,776 | 1,738 | 0.001101 | 🟢 medium — moderately distinctive | — |
| 1842 | **trade** | 1 | 8 | - | 455.18 | 0.108214 | 2,748 | 1,283 | 0.001101 | 🔵 low — common in general English | — |
| 1843 | **hail** | 1 | 5 | - | 796.10 | 0.181968 | 1,801 | 1,715 | 0.001101 | 🟢 medium — moderately distinctive | — |
| 1844 | **chen** | 1 | 4 | - | 601.47 | 0.135022 | 2,226 | 1,452 | 0.001099 | 🟢 medium — moderately distinctive | — |
| 1845 | **neck** | 1 | 5 | - | 831.24 | 0.226361 | 1,641 | 1,898 | 0.001099 | 🟢 medium — moderately distinctive | — |
| 1846 | **wrist** | 1 | 6 | - | 997.16 | 0.298981 | 1,501 | 2,128 | 0.001098 | 🟢 medium — moderately distinctive | — |
| 1847 | **disrespect** | 1 | 5 | - | 830.96 | 0.182609 | 1,736 | 1,789 | 0.001098 | 🟢 medium — moderately distinctive | — |
| 1848 | **cup** | 1 | 5 | - | 830.96 | 0.182542 | 1,744 | 1,782 | 0.001097 | 🟢 medium — moderately distinctive | ~ |
| 1849 | **alm** | 1 | 10 | - | 1,661.93 | - | 968 | - | 0.001097 | 🟢 medium — moderately distinctive | — |
| 1850 | **homeland** | 1 | 5 | - | 751.84 | 0.181297 | 1,853 | 1,683 | 0.001096 | 🟢 medium — moderately distinctive | — |
| 1851 | **measure** | 1 | 7 | - | 689.17 | 0.175002 | 1,921 | 1,631 | 0.001096 | 🟢 medium — moderately distinctive | — |
| 1852 | **drag** | 1 | 5 | - | 771.18 | 0.181921 | 1,825 | 1,710 | 0.001095 | 🟢 medium — moderately distinctive | — |
| 1853 | **stomach** | 1 | 5 | - | 831.24 | 0.226323 | 1,652 | 1,897 | 0.001095 | 🟢 medium — moderately distinctive | — |
| 1854 | **sensation** | 1 | 5 | - | 831.24 | 0.226474 | 1,651 | 1,899 | 0.001095 | 🟢 medium — moderately distinctive | — |
| 1855 | **silk** | 1 | 5 | - | 831.24 | 0.227529 | 1,647 | 1,906 | 0.001094 | 🟢 medium — moderately distinctive | — |
| 1856 | **volume** | 1 | 7 | - | 644.93 | 0.147096 | 2,142 | 1,502 | 0.001094 | 🟢 medium — moderately distinctive | — |
| 1857 | **pure intention** | 2 | 4 | 0.486 | - | 0.068796 | - | 971 | 0.001094 | - | — |
| 1858 | **pacify** | 1 | 5 | - | 830.96 | 0.182564 | 1,753 | 1,783 | 0.001094 | 🟢 medium — moderately distinctive | — |
| 1859 | **hundred thousand** | 2 | 15 | 0.559 | - | 0.068952 | - | 972 | 0.001093 | - | ~ |
| 1860 | **conceit** | 1 | 5 | - | 830.96 | 0.182572 | 1,755 | 1,785 | 0.001093 | 🟢 medium — moderately distinctive | — |
| 1861 | **question** | 1 | 7 | - | 668.07 | 0.175558 | 1,933 | 1,634 | 0.001092 | 🟢 medium — moderately distinctive | — |
| 1862 | **succeed** | 1 | 6 | - | 712.49 | 0.178963 | 1,904 | 1,657 | 0.001092 | 🟢 medium — moderately distinctive | — |
| 1863 | **skull-cup** | 1 | 10 | - | 1,661.93 | - | 975 | - | 0.001091 | 🟢 medium — moderately distinctive | — |
| 1864 | **mix** | 1 | 6 | - | 811.18 | 0.182491 | 1,775 | 1,774 | 0.001090 | 🟢 medium — moderately distinctive | — |
| 1865 | **rocky** | 1 | 5 | - | 751.84 | 0.181599 | 1,854 | 1,702 | 0.001090 | 🟢 medium — moderately distinctive | — |
| 1866 | **permit** | 1 | 3 | - | 335.73 | 0.107674 | 2,978 | 1,255 | 0.001090 | 🔵 low — common in general English | — |
| 1867 | **true meaning** | 2 | 3 | 0.428 | - | 0.070326 | - | 977 | 0.001089 | - | ~ |
| 1868 | **prisoner** | 1 | 5 | - | 831.24 | 0.227713 | 1,663 | 1,909 | 0.001088 | 🟢 medium — moderately distinctive | — |
| 1869 | **understanding** | 1 | 14 | - | 1,654.78 | - | 978 | - | 0.001088 | 🟢 medium — moderately distinctive | — |
| 1870 | **company** | 1 | 8 | - | 347.14 | 0.107879 | 2,960 | 1,262 | 0.001088 | 🔵 low — common in general English | — |
| 1871 | **hesitation** | 1 | 6 | - | 955.32 | 0.298586 | 1,528 | 2,126 | 0.001087 | 🟢 medium — moderately distinctive | — |
| 1872 | **freed** | 1 | 11 | - | 1,654.05 | - | 979 | - | 0.001087 | 🟢 medium — moderately distinctive | — |
| 1873 | **real thing** | 2 | 3 | 0.416 | - | 0.071393 | - | 979 | 0.001087 | - | — |
| 1874 | **generous** | 1 | 5 | - | 751.84 | 0.181831 | 1,859 | 1,708 | 0.001087 | 🟢 medium — moderately distinctive | — |
| 1875 | **followed** | 1 | 17 | - | 1,653.76 | - | 981 | - | 0.001085 | 🟢 medium — moderately distinctive | — |
| 1876 | **among** | 1 | 20 | - | 1,632.58 | - | 983 | - | 0.001083 | 🟢 medium — moderately distinctive | — |
| 1877 | **spiritual companion** | 2 | 6 | 0.599 | - | 0.072038 | - | 983 | 0.001083 | - | — |
| 1878 | **floor** | 1 | 6 | - | 656.73 | 0.149095 | 2,131 | 1,540 | 0.001081 | 🟢 medium — moderately distinctive | — |
| 1879 | **religious** | 1 | 5 | - | 796.10 | 0.182569 | 1,796 | 1,784 | 0.001081 | 🟢 medium — moderately distinctive | — |
| 1880 | **upward** | 1 | 9 | - | 937.31 | 0.284300 | 1,549 | 2,118 | 0.001081 | 🟢 medium — moderately distinctive | — |
| 1881 | **join** | 1 | 6 | - | 662.79 | 0.149194 | 2,125 | 1,548 | 0.001080 | 🟢 medium — moderately distinctive | — |
| 1882 | **lover** | 1 | 5 | - | 830.96 | 0.224264 | 1,709 | 1,891 | 0.001078 | 🟢 medium — moderately distinctive | ~ |
| 1883 | **grave** | 1 | 5 | - | 736.04 | 0.182094 | 1,875 | 1,725 | 0.001077 | 🟢 medium — moderately distinctive | ~ |
| 1884 | **solitary place** | 2 | 7 | 0.677 | - | 0.072995 | - | 990 | 0.001077 | - | — |
| 1885 | **town** | 1 | 6 | - | 820.23 | 0.194358 | 1,763 | 1,834 | 0.001077 | 🟢 medium — moderately distinctive | — |
| 1886 | **emanating** | 1 | 5 | - | 796.10 | 0.182611 | 1,806 | 1,790 | 0.001076 | 🟢 medium — moderately distinctive | — |
| 1887 | **thirteen** | 1 | 5 | - | 796.10 | 0.182648 | 1,805 | 1,791 | 0.001076 | 🟢 medium — moderately distinctive | — |
| 1888 | **passed** | 1 | 15 | - | 1,618.39 | - | 991 | - | 0.001076 | 🟢 medium — moderately distinctive | — |
| 1889 | **vicious** | 1 | 5 | - | 736.04 | 0.182211 | 1,872 | 1,732 | 0.001076 | 🟢 medium — moderately distinctive | — |
| 1890 | **faithfully** | 1 | 5 | - | 796.10 | 0.182711 | 1,804 | 1,795 | 0.001076 | 🟢 medium — moderately distinctive | — |
| 1891 | **undesirable** | 1 | 5 | - | 736.04 | 0.182141 | 1,878 | 1,728 | 0.001075 | 🟢 medium — moderately distinctive | — |
| 1892 | **built** | 1 | 14 | - | 1,606.79 | - | 992 | - | 0.001075 | 🟢 medium — moderately distinctive | — |
| 1893 | **surely** | 1 | 5 | - | 736.04 | 0.182201 | 1,877 | 1,730 | 0.001075 | 🟢 medium — moderately distinctive | — |
| 1894 | **marici** | 1 | 4 | - | 664.77 | 0.149537 | 2,101 | 1,575 | 0.001074 | 🟢 medium — moderately distinctive | — |
| 1895 | **ghost** | 1 | 5 | - | 830.96 | 0.228207 | 1,698 | 1,919 | 0.001074 | 🟢 medium — moderately distinctive | ✓ འདྲེ |
| 1896 | **bring benefit** | 2 | 3 | 0.357 | - | 0.073684 | - | 994 | 0.001073 | - | — |
| 1897 | **wound** | 1 | 6 | - | 925.41 | 0.298615 | 1,565 | 2,127 | 0.001073 | 🟢 medium — moderately distinctive | — |
| 1898 | **afraid** | 1 | 5 | - | 771.18 | 0.182496 | 1,836 | 1,775 | 0.001072 | 🟢 medium — moderately distinctive | — |
| 1899 | **strike** | 1 | 6 | - | 579.86 | 0.147519 | 2,250 | 1,504 | 0.001072 | 🟢 medium — moderately distinctive | — |
| 1900 | **provide** | 1 | 9 | - | 756.85 | 0.182455 | 1,844 | 1,769 | 0.001072 | 🟢 medium — moderately distinctive | — |
| 1901 | **beer** | 1 | 5 | - | 711.12 | 0.181979 | 1,906 | 1,717 | 0.001071 | 🟢 medium — moderately distinctive | — |
| 1902 | **meaningless** | 1 | 5 | - | 771.18 | 0.182596 | 1,827 | 1,787 | 0.001071 | 🟢 medium — moderately distinctive | — |
| 1903 | **cousin** | 1 | 5 | - | 830.96 | 0.226706 | 1,724 | 1,900 | 0.001071 | 🟢 medium — moderately distinctive | — |
| 1904 | **eaten** | 1 | 10 | - | 1,592.21 | - | 997 | - | 0.001070 | 🟢 medium — moderately distinctive | — |
| 1905 | **overcome** | 1 | 5 | - | 736.04 | 0.182366 | 1,870 | 1,753 | 0.001070 | 🟢 medium — moderately distinctive | — |
| 1906 | **protuberance** | 1 | 5 | - | 830.96 | 0.227915 | 1,718 | 1,913 | 0.001069 | 🟢 medium — moderately distinctive | ~ |
| 1907 | **damchen** | 1 | 4 | - | 664.77 | 0.150270 | 2,113 | 1,582 | 0.001069 | 🟢 medium — moderately distinctive | ✓ དམ་ཆེན་རྡོ་རྗེ་ལེགས་པ |
| 1908 | **soft** | 1 | 6 | - | 632.36 | 0.149201 | 2,178 | 1,549 | 0.001068 | 🟢 medium — moderately distinctive | — |
| 1909 | **tremendous** | 1 | 5 | - | 683.52 | 0.181943 | 1,926 | 1,712 | 0.001068 | 🟢 medium — moderately distinctive | — |
| 1910 | **laughter** | 1 | 4 | - | 664.77 | 0.168434 | 2,075 | 1,610 | 0.001067 | 🟢 medium — moderately distinctive | ~ |
| 1911 | **householder** | 1 | 5 | - | 830.96 | 0.227659 | 1,729 | 1,908 | 0.001067 | 🟢 medium — moderately distinctive | — |
| 1912 | **adhicitta** | 1 | 4 | - | 664.77 | 0.150657 | 2,120 | 1,584 | 0.001067 | 🟢 medium — moderately distinctive | ✓ སེམས་ལྷག་ཅན |
| 1913 | **moreover** | 1 | 12 | - | 1,590.30 | - | 1,001 | - | 0.001067 | 🟢 medium — moderately distinctive | — |
| 1914 | **fresh** | 1 | 6 | - | 647.36 | 0.149517 | 2,139 | 1,574 | 0.001067 | 🟢 medium — moderately distinctive | — |
| 1915 | **aggression** | 1 | 5 | - | 711.12 | 0.182202 | 1,908 | 1,731 | 0.001066 | 🟢 medium — moderately distinctive | — |
| 1916 | **temper** | 1 | 5 | - | 736.04 | 0.182379 | 1,879 | 1,756 | 0.001066 | 🟢 medium — moderately distinctive | — |
| 1917 | **reduce** | 1 | 7 | - | 548.45 | 0.146889 | 2,295 | 1,499 | 0.001066 | 🟢 medium — moderately distinctive | — |
| 1918 | **examining** | 1 | 12 | - | 1,590.30 | - | 1,002 | - | 0.001066 | 🟢 medium — moderately distinctive | — |
| 1919 | **dodrup** | 1 | 4 | - | 664.77 | 0.150831 | 2,123 | 1,585 | 0.001066 | 🟢 medium — moderately distinctive | — |
| 1920 | **spot** | 1 | 6 | - | 598.26 | 0.148922 | 2,230 | 1,530 | 0.001066 | 🟢 medium — moderately distinctive | — |
| 1921 | **disappeared** | 1 | 11 | - | 1,589.91 | - | 1,003 | - | 0.001065 | 🟢 medium — moderately distinctive | — |
| 1922 | **adamantine** | 1 | 4 | - | 664.77 | 0.169947 | 2,080 | 1,613 | 0.001065 | 🟢 medium — moderately distinctive | ✓ |
| 1923 | **guidance** | 1 | 5 | - | 722.69 | 0.182328 | 1,892 | 1,750 | 0.001065 | 🟢 medium — moderately distinctive | — |
| 1924 | **knowing** | 1 | 11 | - | 1,589.91 | - | 1,004 | - | 0.001064 | 🟢 medium — moderately distinctive | — |
| 1925 | **constitute** | 1 | 6 | - | 787.98 | 0.194533 | 1,812 | 1,835 | 0.001062 | 🟢 medium — moderately distinctive | — |
| 1926 | **similarly** | 1 | 5 | - | 662.63 | 0.156284 | 2,127 | 1,596 | 0.001061 | 🟢 medium — moderately distinctive | — |
| 1927 | **consort** | 1 | 5 | - | 830.96 | 0.228064 | 1,743 | 1,915 | 0.001061 | 🟢 medium — moderately distinctive | ✓ ཡུམ / གསང་ཡུམ |
| 1928 | **often** | 1 | 14 | - | 1,577.52 | - | 1,008 | - | 0.001061 | 🟢 medium — moderately distinctive | — |
| 1929 | **victory** | 1 | 5 | - | 662.63 | 0.156416 | 2,129 | 1,597 | 0.001060 | 🟢 medium — moderately distinctive | — |
| 1930 | **solely** | 1 | 5 | - | 722.69 | 0.182433 | 1,895 | 1,763 | 0.001060 | 🟢 medium — moderately distinctive | — |
| 1931 | **dwelling** | 1 | 5 | - | 830.96 | 0.228019 | 1,747 | 1,914 | 0.001060 | 🟢 medium — moderately distinctive | ~ |
| 1932 | **logic** | 1 | 5 | - | 722.69 | 0.182448 | 1,896 | 1,767 | 0.001059 | 🟢 medium — moderately distinctive | — |
| 1933 | **innate** | 1 | 4 | - | 664.77 | 0.170316 | 2,108 | 1,615 | 0.001058 | 🟢 medium — moderately distinctive | ✓ ལྷན་སྐྱེས |
| 1934 | **few** | 1 | 18 | - | 1,570.29 | - | 1,011 | - | 0.001058 | 🟢 medium — moderately distinctive | — |
| 1935 | **cling** | 1 | 3 | - | 498.58 | 0.127586 | 2,568 | 1,416 | 0.001058 | 🔵 low — common in general English | — |
| 1936 | **belonging** | 1 | 6 | - | 867.22 | 0.297260 | 1,607 | 2,123 | 0.001058 | 🟢 medium — moderately distinctive | — |
| 1937 | **smoke** | 1 | 5 | - | 722.69 | 0.182478 | 1,894 | 1,772 | 0.001058 | 🟢 medium — moderately distinctive | — |
| 1938 | **beneath** | 1 | 5 | - | 722.69 | 0.182483 | 1,893 | 1,773 | 0.001058 | 🟢 medium — moderately distinctive | — |
| 1939 | **burning** | 1 | 11 | - | 1,564.45 | - | 1,013 | - | 0.001056 | 🟢 medium — moderately distinctive | — |
| 1940 | **nevertheless** | 1 | 12 | - | 1,562.53 | - | 1,014 | - | 0.001055 | 🟢 medium — moderately distinctive | — |
| 1941 | **attach** | 1 | 3 | - | 477.66 | 0.125608 | 2,679 | 1,389 | 0.001055 | 🔵 low — common in general English | — |
| 1942 | **invited** | 1 | 13 | - | 1,543.74 | - | 1,019 | - | 0.001051 | 🟢 medium — moderately distinctive | — |
| 1943 | **progress** | 1 | 6 | - | 599.39 | 0.149456 | 2,229 | 1,569 | 0.001051 | 🟢 medium — moderately distinctive | — |
| 1944 | **sharp** | 1 | 6 | - | 522.35 | 0.148741 | 2,329 | 1,522 | 0.001051 | 🟢 medium — moderately distinctive | — |
| 1945 | **meeting** | 1 | 7 | - | 451.56 | 0.125390 | 2,753 | 1,379 | 0.001050 | 🔵 low — common in general English | — |
| 1946 | **tomorrow** | 1 | 6 | - | 527.31 | 0.148880 | 2,322 | 1,526 | 0.001050 | 🟢 medium — moderately distinctive | — |
| 1947 | **inward** | 1 | 10 | - | 1,542.35 | - | 1,020 | - | 0.001050 | 🟢 medium — moderately distinctive | — |
| 1948 | **transformed** | 1 | 10 | - | 1,542.35 | - | 1,021 | - | 0.001049 | 🟢 medium — moderately distinctive | — |
| 1949 | **created** | 1 | 14 | - | 1,541.70 | - | 1,022 | - | 0.001049 | 🟢 medium — moderately distinctive | — |
| 1950 | **expert** | 1 | 5 | - | 683.52 | 0.182496 | 1,927 | 1,776 | 0.001048 | 🟢 medium — moderately distinctive | — |
| 1951 | **fell** | 1 | 22 | - | 1,529.42 | - | 1,024 | - | 0.001047 | 🟢 medium — moderately distinctive | — |
| 1952 | **odd** | 1 | 5 | - | 796.10 | 0.227341 | 1,800 | 1,904 | 0.001047 | 🟢 medium — moderately distinctive | — |
| 1953 | **perfume** | 1 | 5 | - | 796.10 | 0.227210 | 1,803 | 1,902 | 0.001046 | 🟢 medium — moderately distinctive | — |
| 1954 | **starting** | 1 | 15 | - | 1,512.99 | - | 1,025 | - | 0.001046 | 🟢 medium — moderately distinctive | — |
| 1955 | **involved** | 1 | 16 | - | 1,504.64 | - | 1,026 | - | 0.001045 | 🟢 medium — moderately distinctive | — |
| 1956 | **smile** | 1 | 5 | - | 830.96 | 0.231764 | 1,727 | 2,008 | 0.001043 | 🟢 medium — moderately distinctive | — |
| 1957 | **star** | 1 | 5 | - | 636.16 | 0.171685 | 2,176 | 1,619 | 0.001043 | 🟢 medium — moderately distinctive | — |
| 1958 | **problem** | 1 | 8 | - | 738.03 | 0.216098 | 1,868 | 1,855 | 0.001041 | 🟢 medium — moderately distinctive | — |
| 1959 | **ordinary person** | 2 | 13 | 0.475 | - | 0.075182 | - | 1,032 | 0.001040 | - | — |
| 1960 | **adverse** | 1 | 5 | - | 580.79 | 0.154304 | 2,248 | 1,589 | 0.001040 | 🟢 medium — moderately distinctive | — |
| 1961 | **cost** | 1 | 8 | - | 628.99 | 0.172671 | 2,183 | 1,624 | 0.001040 | 🟢 medium — moderately distinctive | — |
| 1962 | **pillar** | 1 | 5 | - | 771.18 | 0.227334 | 1,830 | 1,903 | 0.001039 | 🟢 medium — moderately distinctive | — |
| 1963 | **supreme accomplishment** | 2 | 7 | 0.602 | - | 0.075815 | - | 1,034 | 0.001038 | - | ✓ མཆོག་གི་དངོས་གྲུབ |
| 1964 | **hollow** | 1 | 5 | - | 830.96 | 0.232242 | 1,700 | 2,068 | 0.001038 | 🟢 medium — moderately distinctive | — |
| 1965 | **caring** | 1 | 9 | - | 1,496.23 | - | 1,035 | - | 0.001038 | 🟢 medium — moderately distinctive | — |
| 1966 | **ensure** | 1 | 6 | - | 651.00 | 0.178989 | 2,138 | 1,658 | 0.001037 | 🟢 medium — moderately distinctive | — |
| 1967 | **walking** | 1 | 9 | - | 1,496.23 | - | 1,036 | - | 0.001037 | 🟢 medium — moderately distinctive | ~ |
| 1968 | **bright kalpa** | 2 | 3 | 0.623 | - | 0.076548 | - | 1,037 | 0.001036 | - | — |
| 1969 | **castle** | 1 | 4 | - | 588.83 | 0.168387 | 2,239 | 1,609 | 0.001034 | 🟢 medium — moderately distinctive | — |
| 1970 | **loving** | 1 | 9 | - | 1,496.23 | - | 1,041 | - | 0.001033 | 🟢 medium — moderately distinctive | — |
| 1971 | **spring** | 1 | 6 | - | 624.87 | 0.177493 | 2,185 | 1,646 | 0.001032 | 🟢 medium — moderately distinctive | — |
| 1972 | **sri** | 1 | 4 | - | 492.74 | 0.134858 | 2,664 | 1,447 | 0.001031 | 🔵 low — common in general English | — |
| 1973 | **distracted** | 1 | 9 | - | 1,495.74 | - | 1,044 | - | 0.001030 | 🟢 medium — moderately distinctive | — |
| 1974 | **split** | 1 | 7 | - | 546.56 | 0.150993 | 2,306 | 1,586 | 0.001030 | 🟢 medium — moderately distinctive | — |
| 1975 | **large number** | 2 | 9 | 0.786 | - | 0.079187 | - | 1,045 | 0.001029 | - | — |
| 1976 | **emerge** | 1 | 6 | - | 734.86 | 0.223495 | 1,882 | 1,885 | 0.001029 | 🟢 medium — moderately distinctive | — |
| 1977 | **terrifying** | 1 | 9 | - | 1,495.74 | - | 1,046 | - | 0.001029 | 🟢 medium — moderately distinctive | — |
| 1978 | **thirty-two** | 1 | 9 | - | 1,495.74 | - | 1,047 | - | 0.001028 | 🟢 medium — moderately distinctive | — |
| 1979 | **unbearable compassion** | 2 | 3 | 0.464 | - | 0.080023 | - | 1,047 | 0.001028 | - | — |
| 1980 | **factor** | 1 | 6 | - | 605.20 | 0.177135 | 2,211 | 1,644 | 0.001027 | 🟢 medium — moderately distinctive | — |
| 1981 | **plant** | 1 | 8 | - | 688.10 | 0.216066 | 1,922 | 1,854 | 0.001027 | 🟢 medium — moderately distinctive | — |
| 1982 | **sravakas** | 1 | - | - | - | 0.080696 | - | 1,050 | 0.001025 | - | — |
| 1983 | **scrap** | 1 | 5 | - | 636.16 | 0.180917 | 2,173 | 1,673 | 0.001025 | 🟢 medium — moderately distinctive | — |
| 1984 | **mention** | 1 | 3 | - | 390.63 | 0.125851 | 2,887 | 1,399 | 0.001025 | 🔵 low — common in general English | — |
| 1985 | **sakya** | 1 | 5 | - | 830.96 | 0.244263 | 1,732 | 2,088 | 0.001024 | 🟢 medium — moderately distinctive | — |
| 1986 | **stick** | 1 | 5 | - | 636.16 | 0.181149 | 2,174 | 1,677 | 0.001023 | 🟢 medium — moderately distinctive | — |
| 1987 | **convince** | 1 | 1 | - | 128.17 | 0.082998 | 7,344 | 1,066 | 0.001023 | 🔵 low — common in general English | — |
| 1988 | **doesn** | 1 | 9 | - | 1,495.74 | - | 1,053 | - | 0.001023 | 🟢 medium — moderately distinctive | — |
| 1989 | **determine** | 1 | 4 | - | 423.67 | 0.129065 | 2,825 | 1,420 | 0.001022 | 🔵 low — common in general English | — |
| 1990 | **aris** | 1 | 9 | - | 1,495.74 | - | 1,055 | - | 0.001021 | 🟢 medium — moderately distinctive | — |
| 1991 | **enormous** | 1 | 5 | - | 662.63 | 0.181955 | 2,128 | 1,714 | 0.001021 | 🟢 medium — moderately distinctive | — |
| 1992 | **distance** | 1 | 5 | - | 631.72 | 0.181323 | 2,179 | 1,685 | 0.001020 | 🟢 medium — moderately distinctive | — |
| 1993 | **dawn** | 1 | 4 | - | 664.99 | 0.196697 | 1,963 | 1,844 | 0.001020 | 🟢 medium — moderately distinctive | — |
| 1994 | **suitable** | 1 | 5 | - | 651.05 | 0.181968 | 2,136 | 1,716 | 0.001018 | 🟢 medium — moderately distinctive | — |
| 1995 | **tormas** | 1 | - | - | - | 0.082472 | - | 1,059 | 0.001018 | - | — |
| 1996 | **decline** | 1 | 7 | - | 550.75 | 0.174566 | 2,294 | 1,629 | 0.001017 | 🟢 medium — moderately distinctive | — |
| 1997 | **acquire** | 1 | 5 | - | 359.66 | 0.125898 | 2,941 | 1,403 | 0.001017 | 🔵 low — common in general English | — |
| 1998 | **war** | 1 | 6 | - | 570.04 | 0.178143 | 2,265 | 1,647 | 0.001016 | 🟢 medium — moderately distinctive | — |
| 1999 | **thank** | 1 | 9 | - | 1,495.74 | - | 1,063 | - | 0.001015 | 🟢 medium — moderately distinctive | — |
| 2000 | **autumn** | 1 | 5 | - | 585.74 | 0.180404 | 2,245 | 1,669 | 0.001012 | 🟢 medium — moderately distinctive | — |
| 2001 | **china** | 1 | 4 | - | 362.10 | 0.127503 | 2,933 | 1,415 | 0.001012 | 🔵 low — common in general English | — |
| 2002 | **hors** | 1 | 9 | - | 1,495.74 | - | 1,067 | - | 0.001012 | 🟢 medium — moderately distinctive | — |
| 2003 | **degree** | 1 | 5 | - | 608.99 | 0.181504 | 2,205 | 1,695 | 0.001011 | 🟢 medium — moderately distinctive | — |
| 2004 | **begging** | 1 | 9 | - | 1,495.74 | - | 1,069 | - | 0.001010 | 🟢 medium — moderately distinctive | — |
| 2005 | **continuous** | 1 | 5 | - | 623.46 | 0.181938 | 2,186 | 1,711 | 0.001010 | 🟢 medium — moderately distinctive | — |
| 2006 | **vajra sattva** | 2 | 3 | 0.709 | - | 0.083209 | - | 1,073 | 0.001007 | - | — |
| 2007 | **western** | 1 | 5 | - | 429.64 | 0.137829 | 2,809 | 1,461 | 0.001006 | 🔵 low — common in general English | — |
| 2008 | **kasyapa** | 1 | 4 | - | 664.77 | 0.194143 | 2,041 | 1,830 | 0.001005 | 🟢 medium — moderately distinctive | — |
| 2009 | **joyful** | 1 | 4 | - | 664.77 | 0.196105 | 2,030 | 1,839 | 0.001005 | 🟢 medium — moderately distinctive | ~ |
| 2010 | **conclude** | 1 | 5 | - | 636.16 | 0.182225 | 2,175 | 1,734 | 0.001005 | 🟢 medium — moderately distinctive | — |
| 2011 | **praise** | 1 | 4 | - | 664.99 | 0.227397 | 1,957 | 1,905 | 0.001005 | 🟢 medium — moderately distinctive | — |
| 2012 | **visualized** | 1 | 9 | - | 1,495.74 | - | 1,076 | - | 0.001005 | 🟢 medium — moderately distinctive | — |
| 2013 | **confident faith** | 2 | 5 | 0.696 | - | 0.083330 | - | 1,076 | 0.001005 | - | — |
| 2014 | **youth** | 1 | 4 | - | 664.99 | 0.230434 | 1,939 | 1,928 | 0.001003 | 🟢 medium — moderately distinctive | — |
| 2015 | **visualizing** | 1 | 9 | - | 1,495.74 | - | 1,078 | - | 0.001003 | 🟢 medium — moderately distinctive | — |
| 2016 | **emperor** | 1 | 5 | - | 796.10 | 0.258506 | 1,793 | 2,101 | 0.001002 | 🟢 medium — moderately distinctive | — |
| 2017 | **guard** | 1 | 6 | - | 811.18 | 0.298007 | 1,778 | 2,124 | 0.001002 | 🟢 medium — moderately distinctive | — |
| 2018 | **immediate** | 1 | 15 | - | 1,492.87 | - | 1,080 | - | 0.001002 | 🟢 medium — moderately distinctive | ~ |
| 2019 | **livestock** | 1 | 5 | - | 569.52 | 0.181435 | 2,266 | 1,691 | 0.001001 | 🟢 medium — moderately distinctive | — |
| 2020 | **member** | 1 | 6 | - | 526.75 | 0.179077 | 2,324 | 1,660 | 0.001001 | 🟢 medium — moderately distinctive | — |
| 2021 | **suck** | 1 | 4 | - | 664.99 | 0.230684 | 1,948 | 1,931 | 0.001000 | 🟢 medium — moderately distinctive | — |
| 2022 | **greater** | 1 | 16 | - | 1,485.94 | - | 1,084 | - | 0.000999 | 🟢 medium — moderately distinctive | — |
| 2023 | **single lifetime** | 2 | 4 | 0.532 | - | 0.083509 | - | 1,084 | 0.000999 | - | — |
| 2024 | **necessary** | 1 | 16 | - | 1,483.93 | - | 1,085 | - | 0.000998 | 🟢 medium — moderately distinctive | — |
| 2025 | **blister** | 1 | 4 | - | 664.77 | 0.219405 | 2,036 | 1,863 | 0.000997 | 🟢 medium — moderately distinctive | — |
| 2026 | **representing** | 1 | 14 | - | 1,479.15 | - | 1,086 | - | 0.000997 | 🟢 medium — moderately distinctive | — |
| 2027 | **circumstantial** | 1 | 4 | - | 664.77 | 0.228318 | 1,973 | 1,922 | 0.000996 | 🟢 medium — moderately distinctive | — |
| 2028 | **generate** | 1 | 5 | - | 605.72 | 0.182294 | 2,210 | 1,744 | 0.000995 | 🟢 medium — moderately distinctive | — |
| 2029 | **learning** | 1 | 10 | - | 1,472.09 | - | 1,089 | - | 0.000995 | 🟢 medium — moderately distinctive | — |
| 2030 | **discouragement** | 1 | 4 | - | 664.99 | 0.231470 | 1,936 | 1,970 | 0.000994 | 🟢 medium — moderately distinctive | — |
| 2031 | **satisfied** | 1 | 13 | - | 1,464.84 | - | 1,091 | - | 0.000993 | 🟢 medium — moderately distinctive | — |
| 2032 | **cleanse** | 1 | 4 | - | 664.77 | 0.196303 | 2,082 | 1,840 | 0.000993 | 🟢 medium — moderately distinctive | — |
| 2033 | **conceptualization** | 1 | 4 | - | 664.77 | 0.230841 | 1,972 | 1,936 | 0.000993 | 🟢 medium — moderately distinctive | — |
| 2034 | **produce** | 1 | 5 | - | 459.47 | 0.148306 | 2,743 | 1,512 | 0.000993 | 🔵 low — common in general English | — |
| 2035 | **gently** | 1 | 4 | - | 664.99 | 0.231397 | 1,943 | 1,967 | 0.000993 | 🟢 medium — moderately distinctive | — |
| 2036 | **opening** | 1 | 8 | - | 786.24 | 0.289482 | 1,815 | 2,121 | 0.000992 | 🟢 medium — moderately distinctive | — |
| 2037 | **assimilate** | 1 | 4 | - | 664.77 | 0.230884 | 1,976 | 1,938 | 0.000992 | 🟢 medium — moderately distinctive | — |
| 2038 | **fortress** | 1 | 4 | - | 664.77 | 0.195881 | 2,092 | 1,838 | 0.000992 | 🟢 medium — moderately distinctive | — |
| 2039 | **stricken** | 1 | 4 | - | 664.99 | 0.231427 | 1,949 | 1,968 | 0.000991 | 🟢 medium — moderately distinctive | — |
| 2040 | **notice** | 1 | 5 | - | 578.41 | 0.182216 | 2,251 | 1,733 | 0.000990 | 🟢 medium — moderately distinctive | — |
| 2041 | **possible** | 1 | 19 | - | 1,459.99 | - | 1,095 | - | 0.000990 | 🟢 medium — moderately distinctive | — |
| 2042 | **utter** | 1 | 4 | - | 664.99 | 0.231641 | 1,937 | 1,987 | 0.000989 | 🟢 medium — moderately distinctive | — |
| 2043 | **weary** | 1 | 4 | - | 664.99 | 0.231484 | 1,952 | 1,974 | 0.000989 | 🟢 medium — moderately distinctive | — |
| 2044 | **holder** | 1 | 5 | - | 583.23 | 0.182301 | 2,247 | 1,745 | 0.000987 | 🟢 medium — moderately distinctive | — |
| 2045 | **skull cup** | 2 | 4 | 0.864 | - | 0.083962 | - | 1,100 | 0.000986 | - | ✓ ཐོད་ཕོར |
| 2046 | **eventually** | 1 | 5 | - | 547.27 | 0.182032 | 2,296 | 1,720 | 0.000986 | 🟢 medium — moderately distinctive | — |
| 2047 | **smrtijnana** | 1 | 3 | - | 498.58 | 0.177135 | 2,443 | 1,645 | 0.000986 | 🔵 low — common in general English | — |
| 2048 | **miraculously** | 1 | 4 | - | 664.77 | 0.230202 | 2,012 | 1,927 | 0.000986 | 🟢 medium — moderately distinctive | — |
| 2049 | **fleeting** | 1 | 4 | - | 664.77 | 0.230761 | 2,004 | 1,935 | 0.000986 | 🟢 medium — moderately distinctive | — |
| 2050 | **sandalwood** | 1 | 4 | - | 664.99 | 0.231598 | 1,958 | 1,981 | 0.000985 | 🟢 medium — moderately distinctive | — |
| 2051 | **mixed** | 1 | 5 | - | 599.52 | 0.182436 | 2,228 | 1,764 | 0.000985 | 🟢 medium — moderately distinctive | — |
| 2052 | **generation phase** | 2 | 6 | 0.737 | - | 0.084528 | - | 1,102 | 0.000985 | - | ✓ བསྐྱེད་རིམ |
| 2053 | **drown** | 1 | 4 | - | 664.77 | 0.231352 | 1,981 | 1,961 | 0.000985 | 🟢 medium — moderately distinctive | — |
| 2054 | **famine** | 1 | 4 | - | 664.99 | 0.231721 | 1,945 | 1,999 | 0.000984 | 🟢 medium — moderately distinctive | — |
| 2055 | **crushed** | 1 | 10 | - | 1,445.37 | - | 1,103 | - | 0.000984 | 🟢 medium — moderately distinctive | — |
| 2056 | **essential nature** | 2 | 4 | 0.538 | - | 0.084746 | - | 1,103 | 0.000984 | - | ~ |
| 2057 | **contact** | 1 | 5 | - | 602.56 | 0.182510 | 2,214 | 1,778 | 0.000984 | 🟢 medium — moderately distinctive | — |
| 2058 | **exactly** | 1 | 11 | - | 1,444.62 | - | 1,105 | - | 0.000983 | 🟢 medium — moderately distinctive | — |
| 2059 | **unshakeable** | 1 | 4 | - | 664.77 | 0.231115 | 2,000 | 1,951 | 0.000983 | 🟢 medium — moderately distinctive | — |
| 2060 | **personal** | 1 | 5 | - | 526.96 | 0.181990 | 2,323 | 1,718 | 0.000982 | 🟢 medium — moderately distinctive | — |
| 2061 | **poured** | 1 | 9 | - | 1,432.99 | - | 1,107 | - | 0.000981 | 🟢 medium — moderately distinctive | — |
| 2062 | **accomplishment mandala** | 2 | 4 | 0.515 | - | 0.085867 | - | 1,107 | 0.000981 | - | ~ |
| 2063 | **bent** | 1 | 4 | - | 664.77 | 0.230700 | 2,028 | 1,932 | 0.000981 | 🟢 medium — moderately distinctive | — |
| 2064 | **mentality** | 1 | 4 | - | 664.99 | 0.231722 | 1,959 | 2,000 | 0.000981 | 🟢 medium — moderately distinctive | — |
| 2065 | **growth** | 1 | 6 | - | 418.10 | 0.148398 | 2,836 | 1,514 | 0.000981 | 🔵 low — common in general English | — |
| 2066 | **isvara** | 1 | 4 | - | 664.77 | 0.231184 | 2,009 | 1,953 | 0.000980 | 🟢 medium — moderately distinctive | — |
| 2067 | **armour** | 1 | 4 | - | 664.77 | 0.230928 | 2,025 | 1,939 | 0.000980 | 🟢 medium — moderately distinctive | — |
| 2068 | **confident** | 1 | 5 | - | 518.35 | 0.181992 | 2,336 | 1,719 | 0.000979 | 🟢 medium — moderately distinctive | — |
| 2069 | **sour** | 1 | 5 | - | 590.99 | 0.182520 | 2,236 | 1,780 | 0.000979 | 🟢 medium — moderately distinctive | — |
| 2070 | **arisen** | 1 | 10 | - | 1,422.23 | - | 1,111 | - | 0.000978 | 🟢 medium — moderately distinctive | — |
| 2071 | **true existence** | 2 | 4 | 0.539 | - | 0.086398 | - | 1,111 | 0.000978 | - | ~ |
| 2072 | **extraordinary faith** | 2 | 3 | 0.470 | - | 0.086598 | - | 1,112 | 0.000978 | - | — |
| 2073 | **procrastination** | 1 | 4 | - | 664.77 | 0.231493 | 1,998 | 1,975 | 0.000977 | 🟢 medium — moderately distinctive | — |
| 2074 | **sadness** | 1 | 4 | - | 664.77 | 0.231206 | 2,020 | 1,955 | 0.000977 | 🟢 medium — moderately distinctive | — |
| 2075 | **silver** | 1 | 5 | - | 535.09 | 0.182275 | 2,316 | 1,739 | 0.000977 | 🟢 medium — moderately distinctive | — |
| 2076 | **arising** | 1 | 11 | - | 1,409.87 | - | 1,115 | - | 0.000975 | 🟢 medium — moderately distinctive | — |
| 2077 | **food clothing** | 2 | 7 | 0.579 | - | 0.087159 | - | 1,115 | 0.000975 | - | — |
| 2078 | **sell** | 1 | 6 | - | 417.90 | 0.148906 | 2,837 | 1,528 | 0.000975 | 🔵 low — common in general English | — |
| 2079 | **interrupt** | 1 | 4 | - | 636.88 | 0.196345 | 2,168 | 1,841 | 0.000975 | 🟢 medium — moderately distinctive | — |
| 2080 | **proud** | 1 | 4 | - | 664.99 | 0.231914 | 1,956 | 2,029 | 0.000975 | 🟢 medium — moderately distinctive | — |
| 2081 | **inanimate** | 1 | 4 | - | 664.77 | 0.231600 | 2,002 | 1,982 | 0.000975 | 🟢 medium — moderately distinctive | — |
| 2082 | **spit** | 1 | 4 | - | 664.99 | 0.231950 | 1,955 | 2,031 | 0.000975 | 🟢 medium — moderately distinctive | — |
| 2083 | **carried** | 1 | 13 | - | 1,402.60 | - | 1,117 | - | 0.000974 | 🟢 medium — moderately distinctive | — |
| 2084 | **frustrating** | 1 | 4 | - | 664.77 | 0.230876 | 2,054 | 1,937 | 0.000974 | 🟢 medium — moderately distinctive | — |
| 2085 | **conflict** | 1 | 5 | - | 590.99 | 0.186818 | 2,235 | 1,800 | 0.000973 | 🟢 medium — moderately distinctive | — |
| 2086 | **intrinsic** | 1 | 4 | - | 664.99 | 0.232059 | 1,944 | 2,050 | 0.000973 | 🟢 medium — moderately distinctive | — |
| 2087 | **chastity** | 1 | 4 | - | 664.77 | 0.231350 | 2,034 | 1,960 | 0.000973 | 🟢 medium — moderately distinctive | — |
| 2088 | **upper** | 1 | 5 | - | 578.41 | 0.182668 | 2,254 | 1,793 | 0.000972 | 🟢 medium — moderately distinctive | — |
| 2089 | **transmigration** | 1 | 4 | - | 664.77 | 0.230976 | 2,057 | 1,943 | 0.000972 | 🟢 medium — moderately distinctive | — |
| 2090 | **pointless** | 1 | 4 | - | 664.77 | 0.231789 | 1,982 | 2,016 | 0.000971 | 🟢 medium — moderately distinctive | — |
| 2091 | **ignorant** | 1 | 4 | - | 664.77 | 0.231186 | 2,046 | 1,954 | 0.000971 | 🟢 medium — moderately distinctive | — |
| 2092 | **established** | 1 | 13 | - | 1,394.97 | - | 1,121 | - | 0.000971 | 🟢 medium — moderately distinctive | — |
| 2093 | **kadampas** | 1 | - | - | - | 0.088650 | - | 1,121 | 0.000971 | - | — |
| 2094 | **royal** | 1 | 5 | - | 524.42 | 0.182342 | 2,328 | 1,751 | 0.000971 | 🟢 medium — moderately distinctive | ~ |
| 2095 | **grateful** | 1 | 4 | - | 664.77 | 0.231074 | 2,055 | 1,948 | 0.000971 | 🟢 medium — moderately distinctive | — |
| 2096 | **uncle** | 1 | 4 | - | 664.77 | 0.231632 | 2,018 | 1,984 | 0.000970 | 🟢 medium — moderately distinctive | — |
| 2097 | **especially** | 1 | 14 | - | 1,390.78 | - | 1,122 | - | 0.000970 | 🟢 medium — moderately distinctive | — |
| 2098 | **pinch** | 1 | 4 | - | 664.99 | 0.232110 | 1,951 | 2,055 | 0.000970 | 🟢 medium — moderately distinctive | — |
| 2099 | **row** | 1 | 6 | - | 643.83 | 0.223477 | 2,143 | 1,884 | 0.000968 | 🟢 medium — moderately distinctive | — |
| 2100 | **touching** | 1 | 9 | - | 1,388.12 | - | 1,125 | - | 0.000968 | 🟢 medium — moderately distinctive | — |
| 2101 | **burst** | 1 | 4 | - | 588.83 | 0.192133 | 2,238 | 1,816 | 0.000968 | 🟢 medium — moderately distinctive | — |
| 2102 | **cotton** | 1 | 5 | - | 514.91 | 0.182370 | 2,341 | 1,755 | 0.000967 | 🟢 medium — moderately distinctive | — |
| 2103 | **highest** | 1 | 13 | - | 1,383.98 | - | 1,128 | - | 0.000966 | 🟢 medium — moderately distinctive | — |
| 2104 | **behalf** | 1 | 5 | - | 552.32 | 0.182596 | 2,293 | 1,788 | 0.000966 | 🟢 medium — moderately distinctive | — |
| 2105 | **collection** | 1 | 4 | - | 601.47 | 0.195879 | 2,220 | 1,837 | 0.000966 | 🟢 medium — moderately distinctive | — |
| 2106 | **radial** | 1 | 4 | - | 664.99 | 0.232154 | 1,967 | 2,057 | 0.000966 | 🟢 medium — moderately distinctive | — |
| 2107 | **driven** | 1 | 10 | - | 1,383.56 | - | 1,129 | - | 0.000965 | 🟢 medium — moderately distinctive | — |
| 2108 | **limitless** | 1 | 4 | - | 664.77 | 0.231500 | 2,050 | 1,976 | 0.000965 | 🟢 medium — moderately distinctive | — |
| 2109 | **evil karma** | 2 | 4 | 0.554 | - | 0.091744 | - | 1,130 | 0.000965 | - | — |
| 2110 | **phrase** | 1 | 4 | - | 636.88 | 0.224327 | 2,151 | 1,894 | 0.000964 | 🟢 medium — moderately distinctive | — |
| 2111 | **curd** | 1 | 4 | - | 664.77 | 0.231390 | 2,067 | 1,966 | 0.000964 | 🟢 medium — moderately distinctive | — |
| 2112 | **risk** | 1 | 5 | - | 500.44 | 0.182394 | 2,357 | 1,759 | 0.000963 | 🟢 medium — moderately distinctive | — |
| 2113 | **turning** | 1 | 12 | - | 1,377.25 | - | 1,132 | - | 0.000963 | 🟢 medium — moderately distinctive | — |
| 2114 | **gaze** | 1 | 4 | - | 664.77 | 0.231897 | 2,008 | 2,026 | 0.000963 | 🟢 medium — moderately distinctive | — |
| 2115 | **tulkus** | 1 | 4 | - | 664.77 | 0.228340 | 2,121 | 1,923 | 0.000963 | 🟢 medium — moderately distinctive | — |
| 2116 | **apart** | 1 | 11 | - | 1,371.61 | - | 1,133 | - | 0.000963 | 🟢 medium — moderately distinctive | — |
| 2117 | **pillow** | 1 | 4 | - | 664.77 | 0.231878 | 2,014 | 2,025 | 0.000962 | 🟢 medium — moderately distinctive | — |
| 2118 | **bar** | 1 | 5 | - | 645.80 | 0.227780 | 2,140 | 1,912 | 0.000962 | 🟢 medium — moderately distinctive | — |
| 2119 | **described** | 1 | 13 | - | 1,366.77 | - | 1,135 | - | 0.000961 | 🟢 medium — moderately distinctive | — |
| 2120 | **infatuation** | 1 | 4 | - | 664.77 | 0.232039 | 1,997 | 2,047 | 0.000961 | 🟢 medium — moderately distinctive | — |
| 2121 | **outside** | 1 | 14 | - | 1,355.21 | - | 1,136 | - | 0.000961 | 🟢 medium — moderately distinctive | — |
| 2122 | **diligent** | 1 | 4 | - | 664.77 | 0.232189 | 1,985 | 2,062 | 0.000960 | 🟢 medium — moderately distinctive | — |
| 2123 | **unerringly** | 1 | 4 | - | 664.77 | 0.231577 | 2,069 | 1,979 | 0.000960 | 🟢 medium — moderately distinctive | — |
| 2124 | **chaff** | 1 | 4 | - | 664.77 | 0.231744 | 2,043 | 2,004 | 0.000960 | 🟢 medium — moderately distinctive | — |
| 2125 | **hindu** | 1 | 4 | - | 664.99 | 0.232369 | 1,970 | 2,080 | 0.000960 | 🟢 medium — moderately distinctive | — |
| 2126 | **context** | 1 | 5 | - | 640.85 | 0.228065 | 2,144 | 1,916 | 0.000960 | 🟢 medium — moderately distinctive | — |
| 2127 | **served** | 1 | 11 | - | 1,355.03 | - | 1,138 | - | 0.000959 | 🟢 medium — moderately distinctive | — |
| 2128 | **threaten** | 1 | 3 | - | 365.39 | 0.149107 | 2,930 | 1,541 | 0.000959 | 🔵 low — common in general English | — |
| 2129 | **swept** | 1 | 9 | - | 1,353.31 | - | 1,139 | - | 0.000958 | 🟢 medium — moderately distinctive | — |
| 2130 | **appearing** | 1 | 9 | - | 1,353.31 | - | 1,140 | - | 0.000958 | 🟢 medium — moderately distinctive | — |
| 2131 | **ingratitude** | 1 | 4 | - | 664.77 | 0.231656 | 2,073 | 1,990 | 0.000957 | 🟢 medium — moderately distinctive | — |
| 2132 | **earnestly** | 1 | 4 | - | 664.77 | 0.232017 | 2,021 | 2,041 | 0.000957 | 🟢 medium — moderately distinctive | — |
| 2133 | **contain** | 1 | 11 | - | 1,347.25 | - | 1,142 | - | 0.000956 | 🟢 medium — moderately distinctive | — |
| 2134 | **caused** | 1 | 15 | - | 1,338.85 | - | 1,145 | - | 0.000954 | 🟢 medium — moderately distinctive | — |
| 2135 | **persistently** | 1 | 4 | - | 636.88 | 0.230107 | 2,162 | 1,926 | 0.000954 | 🟢 medium — moderately distinctive | — |
| 2136 | **eagerness** | 1 | 4 | - | 664.77 | 0.231704 | 2,083 | 1,996 | 0.000953 | 🟢 medium — moderately distinctive | — |
| 2137 | **con** | 1 | 4 | - | 664.77 | 0.249804 | 1,993 | 2,090 | 0.000952 | 🟢 medium — moderately distinctive | — |
| 2138 | **mat** | 1 | 4 | - | 636.88 | 0.230932 | 2,154 | 1,940 | 0.000952 | 🟢 medium — moderately distinctive | — |
| 2139 | **single hair** | 2 | 4 | 0.565 | - | 0.093768 | - | 1,149 | 0.000952 | - | — |
| 2140 | **promise** | 1 | 4 | - | 516.64 | 0.190961 | 2,340 | 1,810 | 0.000951 | 🟢 medium — moderately distinctive | — |
| 2141 | **clay** | 1 | 4 | - | 664.77 | 0.231776 | 2,076 | 2,010 | 0.000951 | 🟢 medium — moderately distinctive | — |
| 2142 | **sens** | 1 | 8 | - | 1,329.98 | - | 1,150 | - | 0.000951 | 🟢 medium — moderately distinctive | — |
| 2143 | **adversity** | 1 | 4 | - | 664.77 | 0.231743 | 2,087 | 2,003 | 0.000950 | 🟢 medium — moderately distinctive | — |
| 2144 | **service** | 1 | 7 | - | 575.14 | 0.219437 | 2,262 | 1,864 | 0.000950 | 🟢 medium — moderately distinctive | — |
| 2145 | **aversion** | 1 | 4 | - | 664.77 | 0.231802 | 2,074 | 2,017 | 0.000950 | 🟢 medium — moderately distinctive | — |
| 2146 | **burnt** | 1 | 8 | - | 1,329.98 | - | 1,152 | - | 0.000949 | 🟢 medium — moderately distinctive | ~ |
| 2147 | **load** | 1 | 5 | - | 612.38 | 0.227735 | 2,204 | 1,911 | 0.000949 | 🟢 medium — moderately distinctive | — |
| 2148 | **ate** | 1 | 8 | - | 1,329.98 | - | 1,153 | - | 0.000949 | 🟢 medium — moderately distinctive | — |
| 2149 | **impervious** | 1 | 4 | - | 664.77 | 0.232284 | 2,026 | 2,073 | 0.000948 | 🟢 medium — moderately distinctive | ~ |
| 2150 | **mistaken** | 1 | 4 | - | 636.88 | 0.231356 | 2,152 | 1,963 | 0.000946 | 🟢 medium — moderately distinctive | — |
| 2151 | **befall** | 1 | 4 | - | 664.77 | 0.231867 | 2,086 | 2,022 | 0.000946 | 🟢 medium — moderately distinctive | — |
| 2152 | **perhap** | 1 | 8 | - | 1,329.54 | - | 1,157 | - | 0.000946 | 🟢 medium — moderately distinctive | — |
| 2153 | **fierce** | 1 | 4 | - | 616.94 | 0.230755 | 2,192 | 1,934 | 0.000946 | 🟢 medium — moderately distinctive | — |
| 2154 | **believing** | 1 | 8 | - | 1,329.54 | - | 1,158 | - | 0.000945 | 🟢 medium — moderately distinctive | — |
| 2155 | **irrelevant** | 1 | 4 | - | 636.88 | 0.231365 | 2,157 | 1,964 | 0.000945 | 🟢 medium — moderately distinctive | — |
| 2156 | **press** | 1 | 4 | - | 353.84 | 0.149501 | 2,949 | 1,572 | 0.000945 | 🔵 low — common in general English | — |
| 2157 | **container** | 1 | 5 | - | 596.59 | 0.227625 | 2,231 | 1,907 | 0.000945 | 🟢 medium — moderately distinctive | — |
| 2158 | **beside** | 1 | 8 | - | 1,329.54 | - | 1,159 | - | 0.000945 | 🟢 medium — moderately distinctive | — |
| 2159 | **enjoyment** | 1 | 4 | - | 664.77 | 0.232249 | 2,048 | 2,070 | 0.000944 | 🟢 medium — moderately distinctive | — |
| 2160 | **oil** | 1 | 6 | - | 348.32 | 0.149503 | 2,958 | 1,573 | 0.000944 | 🔵 low — common in general English | — |
| 2161 | **henchmen** | 1 | 8 | - | 1,329.54 | - | 1,161 | - | 0.000943 | 🟢 medium — moderately distinctive | — |
| 2162 | **abundance** | 1 | 4 | - | 616.94 | 0.230962 | 2,197 | 1,942 | 0.000943 | 🟢 medium — moderately distinctive | — |
| 2163 | **mould** | 1 | 4 | - | 636.88 | 0.231564 | 2,155 | 1,978 | 0.000942 | 🟢 medium — moderately distinctive | — |
| 2164 | **absent** | 1 | 4 | - | 601.47 | 0.230581 | 2,217 | 1,929 | 0.000942 | 🟢 medium — moderately distinctive | — |
| 2165 | **grant** | 1 | 5 | - | 593.75 | 0.228181 | 2,232 | 1,918 | 0.000942 | 🟢 medium — moderately distinctive | — |
| 2166 | **stance** | 1 | 5 | - | 573.85 | 0.225551 | 2,263 | 1,896 | 0.000942 | 🟢 medium — moderately distinctive | — |
| 2167 | **dough** | 1 | 4 | - | 664.77 | 0.232027 | 2,085 | 2,044 | 0.000941 | 🟢 medium — moderately distinctive | — |
| 2168 | **kar** | 1 | 4 | - | 664.77 | 0.231962 | 2,098 | 2,033 | 0.000941 | 🟢 medium — moderately distinctive | — |
| 2169 | **unfailing** | 1 | 4 | - | 664.77 | 0.232046 | 2,084 | 2,048 | 0.000941 | 🟢 medium — moderately distinctive | — |
| 2170 | **scripture** | 1 | 8 | - | 1,329.54 | - | 1,165 | - | 0.000941 | 🟢 medium — moderately distinctive | — |
| 2171 | **vital point** | 2 | 5 | 0.633 | - | 0.094496 | - | 1,166 | 0.000940 | - | — |
| 2172 | **rohita** | 1 | 4 | - | 664.77 | 0.231991 | 2,100 | 2,039 | 0.000939 | 🟢 medium — moderately distinctive | — |
| 2173 | **hevajra** | 1 | 3 | - | 498.58 | 0.190399 | 2,414 | 1,809 | 0.000939 | 🔵 low — common in general English | — |
| 2174 | **week** | 1 | 7 | - | 429.42 | 0.175504 | 2,810 | 1,633 | 0.000939 | 🔵 low — common in general English | — |
| 2175 | **hip** | 1 | 4 | - | 664.77 | 0.232214 | 2,078 | 2,064 | 0.000939 | 🟢 medium — moderately distinctive | — |
| 2176 | **subjugate** | 1 | 4 | - | 664.77 | 0.232086 | 2,090 | 2,053 | 0.000938 | 🟢 medium — moderately distinctive | — |
| 2177 | **remind** | 1 | 4 | - | 601.47 | 0.231012 | 2,219 | 1,944 | 0.000938 | 🟢 medium — moderately distinctive | — |
| 2178 | **diligently** | 1 | 4 | - | 664.77 | 0.232209 | 2,088 | 2,063 | 0.000937 | 🟢 medium — moderately distinctive | — |
| 2179 | **labdron** | 1 | 3 | - | 498.58 | 0.193213 | 2,423 | 1,817 | 0.000936 | 🔵 low — common in general English | ~ |
| 2180 | **hous** | 1 | 8 | - | 1,329.54 | - | 1,173 | - | 0.000935 | 🟢 medium — moderately distinctive | — |
| 2181 | **supernatural** | 1 | 4 | - | 664.77 | 0.232224 | 2,093 | 2,066 | 0.000935 | 🟢 medium — moderately distinctive | — |
| 2182 | **surabhibhadra** | 1 | 3 | - | 498.58 | 0.188818 | 2,451 | 1,804 | 0.000935 | 🔵 low — common in general English | — |
| 2183 | **avalokitdvara** | 1 | 3 | - | 498.58 | 0.191261 | 2,438 | 1,813 | 0.000934 | 🔵 low — common in general English | — |
| 2184 | **blessed** | 1 | 8 | - | 1,329.54 | - | 1,175 | - | 0.000934 | 🟢 medium — moderately distinctive | — |
| 2185 | **lightly** | 1 | 4 | - | 636.88 | 0.231749 | 2,165 | 2,006 | 0.000933 | 🟢 medium — moderately distinctive | — |
| 2186 | **conceptual** | 1 | 4 | - | 664.77 | 0.232166 | 2,107 | 2,060 | 0.000933 | 🟢 medium — moderately distinctive | ~ |
| 2187 | **draw** | 1 | 4 | - | 464.63 | 0.181389 | 2,719 | 1,687 | 0.000932 | 🔵 low — common in general English | — |
| 2188 | **ripened** | 1 | 8 | - | 1,329.54 | - | 1,178 | - | 0.000932 | 🟢 medium — moderately distinctive | — |
| 2189 | **tingri** | 1 | 3 | - | 498.58 | 0.188388 | 2,472 | 1,802 | 0.000932 | 🔵 low — common in general English | — |
| 2190 | **lift** | 1 | 5 | - | 539.46 | 0.226780 | 2,312 | 1,901 | 0.000932 | 🟢 medium — moderately distinctive | — |
| 2191 | **nyentsen** | 1 | 3 | - | 498.58 | 0.193784 | 2,436 | 1,824 | 0.000931 | 🔵 low — common in general English | — |
| 2192 | **tsenpo** | 1 | 3 | - | 498.58 | 0.191054 | 2,460 | 1,811 | 0.000931 | 🔵 low — common in general English | — |
| 2193 | **prosperity** | 1 | 4 | - | 616.94 | 0.231646 | 2,198 | 1,988 | 0.000931 | 🟢 medium — moderately distinctive | — |
| 2194 | **didn** | 1 | 8 | - | 1,329.54 | - | 1,180 | - | 0.000931 | 🟢 medium — moderately distinctive | — |
| 2195 | **passion** | 1 | 4 | - | 664.77 | 0.232306 | 2,102 | 2,076 | 0.000931 | 🟢 medium — moderately distinctive | — |
| 2196 | **derge** | 1 | 3 | - | 498.58 | 0.184928 | 2,503 | 1,797 | 0.000929 | 🔵 low — common in general English | — |
| 2197 | **nirmar** | 1 | 4 | - | 664.77 | 0.232317 | 2,115 | 2,077 | 0.000928 | 🟢 medium — moderately distinctive | — |
| 2198 | **effortless** | 1 | 4 | - | 664.77 | 0.232326 | 2,117 | 2,078 | 0.000927 | 🟢 medium — moderately distinctive | — |
| 2199 | **hurt** | 1 | 5 | - | 524.42 | 0.227733 | 2,327 | 1,910 | 0.000927 | 🟢 medium — moderately distinctive | — |
| 2200 | **penetrate** | 1 | 4 | - | 616.94 | 0.231807 | 2,193 | 2,019 | 0.000925 | 🟢 medium — moderately distinctive | — |
| 2201 | **swift** | 1 | 4 | - | 535.24 | 0.230657 | 2,313 | 1,930 | 0.000924 | 🟢 medium — moderately distinctive | — |
| 2202 | **variety** | 1 | 5 | - | 583.23 | 0.231592 | 2,246 | 1,980 | 0.000924 | 🟢 medium — moderately distinctive | — |
| 2203 | **yeshe tsogyal** | 2 | 4 | 1.000 | - | 0.097740 | - | 1,192 | 0.000923 | - | ✓ ཡེ་ཤེས་མཚོ་རྒྱལ |
| 2204 | **observe** | 1 | 4 | - | 636.88 | 0.232076 | 2,167 | 2,052 | 0.000923 | 🟢 medium — moderately distinctive | — |
| 2205 | **renounce taking** | 2 | 3 | 0.491 | - | 0.097805 | - | 1,193 | 0.000922 | - | — |
| 2206 | **contrary** | 1 | 4 | - | 516.64 | 0.228232 | 2,337 | 1,920 | 0.000922 | 🟢 medium — moderately distinctive | — |
| 2207 | **verbal** | 1 | 4 | - | 636.88 | 0.232134 | 2,164 | 2,056 | 0.000922 | 🟢 medium — moderately distinctive | — |
| 2208 | **transcendent generosity** | 2 | 4 | 0.595 | - | 0.097840 | - | 1,194 | 0.000922 | - | ~ |
| 2209 | **gracious** | 1 | 3 | - | 498.58 | 0.221874 | 2,411 | 1,877 | 0.000921 | 🔵 low — common in general English | — |
| 2210 | **identify** | 1 | 5 | - | 561.45 | 0.231482 | 2,274 | 1,972 | 0.000921 | 🟢 medium — moderately distinctive | — |
| 2211 | **mahayana** | 1 | 3 | - | 498.58 | 0.189334 | 2,541 | 1,806 | 0.000920 | 🔵 low — common in general English | — |
| 2212 | **tsen** | 1 | 3 | - | 498.58 | 0.214751 | 2,461 | 1,852 | 0.000920 | 🔵 low — common in general English | — |
| 2213 | **popularity** | 1 | 4 | - | 560.73 | 0.231470 | 2,281 | 1,971 | 0.000920 | 🟢 medium — moderately distinctive | — |
| 2214 | **standing** | 1 | 10 | - | 1,302.11 | - | 1,198 | - | 0.000919 | 🟢 medium — moderately distinctive | — |
| 2215 | **virudhaka** | 1 | 3 | - | 498.58 | 0.188692 | 2,558 | 1,803 | 0.000919 | 🔵 low — common in general English | — |
| 2216 | **wake** | 1 | 4 | - | 508.93 | 0.229924 | 2,350 | 1,925 | 0.000919 | 🟢 medium — moderately distinctive | — |
| 2217 | **profound meaning** | 2 | 3 | 0.462 | - | 0.099535 | - | 1,199 | 0.000919 | - | ~ |
| 2218 | **dead person** | 2 | 3 | 0.365 | - | 0.099537 | - | 1,200 | 0.000918 | - | — |
| 2219 | **gateway** | 1 | 4 | - | 578.15 | 0.231712 | 2,259 | 1,997 | 0.000917 | 🟢 medium — moderately distinctive | — |
| 2220 | **era** | 1 | 4 | - | 560.73 | 0.231632 | 2,277 | 1,985 | 0.000917 | 🟢 medium — moderately distinctive | — |
| 2221 | **lacking** | 1 | 9 | - | 1,300.83 | - | 1,202 | - | 0.000917 | 🟢 medium — moderately distinctive | — |
| 2222 | **destroyed** | 1 | 11 | - | 1,300.19 | - | 1,203 | - | 0.000916 | 🟢 medium — moderately distinctive | — |
| 2223 | **named** | 1 | 13 | - | 1,293.82 | - | 1,205 | - | 0.000915 | 🟢 medium — moderately distinctive | — |
| 2224 | **lingje** | 1 | 3 | - | 498.58 | 0.214033 | 2,499 | 1,849 | 0.000915 | 🔵 low — common in general English | ~ |
| 2225 | **upset** | 1 | 4 | - | 578.15 | 0.231779 | 2,256 | 2,012 | 0.000914 | 🟢 medium — moderately distinctive | — |
| 2226 | **prajflaparamita** | 1 | 3 | - | 498.58 | 0.190023 | 2,583 | 1,807 | 0.000914 | 🔵 low — common in general English | — |
| 2227 | **regard** | 1 | 4 | - | 512.68 | 0.231094 | 2,344 | 1,949 | 0.000914 | 🟢 medium — moderately distinctive | — |
| 2228 | **performed** | 1 | 10 | - | 1,291.60 | - | 1,207 | - | 0.000914 | 🟢 medium — moderately distinctive | — |
| 2229 | **messenger** | 1 | 4 | - | 588.83 | 0.231926 | 2,244 | 2,030 | 0.000912 | 🟢 medium — moderately distinctive | — |
| 2230 | **finding** | 1 | 11 | - | 1,283.10 | - | 1,209 | - | 0.000912 | 🟢 medium — moderately distinctive | — |
| 2231 | **salt** | 1 | 4 | - | 535.24 | 0.231526 | 2,314 | 1,977 | 0.000912 | 🟢 medium — moderately distinctive | — |
| 2232 | **eradicate** | 1 | 4 | - | 616.94 | 0.232248 | 2,201 | 2,069 | 0.000912 | 🟢 medium — moderately distinctive | — |
| 2233 | **bigger** | 1 | 10 | - | 1,281.70 | - | 1,210 | - | 0.000912 | 🟢 medium — moderately distinctive | — |
| 2234 | **harming** | 1 | 9 | - | 1,280.01 | - | 1,211 | - | 0.000911 | 🟢 medium — moderately distinctive | — |
| 2235 | **express** | 1 | 5 | - | 554.07 | 0.231724 | 2,289 | 2,001 | 0.000911 | 🟢 medium — moderately distinctive | — |
| 2236 | **thrown** | 1 | 9 | - | 1,280.01 | - | 1,212 | - | 0.000911 | 🟢 medium — moderately distinctive | — |
| 2237 | **devadatta** | 1 | 3 | - | 498.58 | 0.191069 | 2,598 | 1,812 | 0.000910 | 🔵 low — common in general English | ✓ ལྷས་བྱིན |
| 2238 | **sitting** | 1 | 9 | - | 1,280.01 | - | 1,213 | - | 0.000910 | 🟢 medium — moderately distinctive | — |
| 2239 | **interruption** | 1 | 4 | - | 601.47 | 0.232175 | 2,225 | 2,061 | 0.000909 | 🟢 medium — moderately distinctive | — |
| 2240 | **northern** | 1 | 5 | - | 475.03 | 0.182444 | 2,708 | 1,766 | 0.000909 | 🔵 low — common in general English | — |
| 2241 | **personally** | 1 | 4 | - | 568.89 | 0.231911 | 2,268 | 2,028 | 0.000908 | 🟢 medium — moderately distinctive | — |
| 2242 | **half** | 1 | 5 | - | 374.11 | 0.181396 | 2,919 | 1,688 | 0.000908 | 🔵 low — common in general English | — |
| 2243 | **clear sky** | 2 | 3 | 0.543 | - | 0.103667 | - | 1,217 | 0.000907 | - | — |
| 2244 | **sage** | 1 | 4 | - | 616.94 | 0.258182 | 2,190 | 2,100 | 0.000907 | 🟢 medium — moderately distinctive | — |
| 2245 | **simha** | 1 | 3 | - | 498.58 | 0.193739 | 2,601 | 1,822 | 0.000907 | 🔵 low — common in general English | — |
| 2246 | **nowhere** | 1 | 8 | - | 1,273.77 | - | 1,218 | - | 0.000907 | 🟢 medium — moderately distinctive | — |
| 2247 | **thousand million** | 2 | 3 | 0.481 | - | 0.103933 | - | 1,218 | 0.000907 | - | — |
| 2248 | **dodepa** | 1 | 3 | - | 498.58 | 0.192073 | 2,622 | 1,815 | 0.000906 | 🔵 low — common in general English | — |
| 2249 | **head cut** | 2 | 4 | 0.468 | - | 0.104760 | - | 1,221 | 0.000905 | - | — |
| 2250 | **simultaneously** | 1 | 4 | - | 546.82 | 0.231870 | 2,298 | 2,023 | 0.000904 | 🟢 medium — moderately distinctive | — |
| 2251 | **raise** | 1 | 5 | - | 407.17 | 0.182083 | 2,856 | 1,722 | 0.000904 | 🔵 low — common in general English | — |
| 2252 | **belt** | 1 | 4 | - | 520.84 | 0.231712 | 2,334 | 1,998 | 0.000904 | 🟢 medium — moderately distinctive | — |
| 2253 | **unknown** | 1 | 4 | - | 501.99 | 0.231633 | 2,354 | 1,986 | 0.000903 | 🟢 medium — moderately distinctive | — |
| 2254 | **noble mafijusri** | 2 | 3 | 0.736 | - | 0.105670 | - | 1,225 | 0.000903 | - | — |
| 2255 | **prasenajit** | 1 | 3 | - | 498.58 | 0.193542 | 2,640 | 1,819 | 0.000903 | 🔵 low — common in general English | — |
| 2256 | **desirable** | 1 | 4 | - | 560.73 | 0.232020 | 2,285 | 2,042 | 0.000902 | 🟢 medium — moderately distinctive | — |
| 2257 | **eager** | 1 | 4 | - | 530.10 | 0.231784 | 2,321 | 2,014 | 0.000902 | 🟢 medium — moderately distinctive | — |
| 2258 | **back** | 1 | 3 | - | 243.91 | 0.136707 | 4,068 | 1,456 | 0.000902 | 🔵 low — common in general English | — |
| 2259 | **early** | 1 | 5 | - | 361.36 | 0.181574 | 2,937 | 1,700 | 0.000902 | 🔵 low — common in general English | — |
| 2260 | **vaisali** | 1 | 3 | - | 498.58 | 0.193584 | 2,649 | 1,820 | 0.000901 | 🔵 low — common in general English | — |
| 2261 | **tsari** | 1 | 3 | - | 498.58 | 0.193859 | 2,636 | 1,827 | 0.000901 | 🔵 low — common in general English | — |
| 2262 | **kutra** | 1 | 3 | - | 498.58 | 0.193708 | 2,651 | 1,821 | 0.000900 | 🔵 low — common in general English | — |
| 2263 | **reveal** | 1 | 4 | - | 553.42 | 0.232032 | 2,290 | 2,046 | 0.000900 | 🟢 medium — moderately distinctive | — |
| 2264 | **pratimok** | 1 | 3 | - | 498.58 | 0.219803 | 2,571 | 1,866 | 0.000899 | 🔵 low — common in general English | — |
| 2265 | **tingdzin** | 1 | 3 | - | 498.58 | 0.193795 | 2,652 | 1,825 | 0.000899 | 🔵 low — common in general English | ~ |
| 2266 | **kept** | 1 | 11 | - | 1,239.48 | - | 1,231 | - | 0.000899 | 🟢 medium — moderately distinctive | — |
| 2267 | **santarak** | 1 | 3 | - | 498.58 | 0.193796 | 2,653 | 1,826 | 0.000899 | 🔵 low — common in general English | — |
| 2268 | **fragrant** | 1 | 3 | - | 498.58 | 0.219006 | 2,585 | 1,861 | 0.000899 | 🔵 low — common in general English | — |
| 2269 | **shoe** | 1 | 4 | - | 512.68 | 0.231776 | 2,346 | 2,011 | 0.000898 | 🟢 medium — moderately distinctive | — |
| 2270 | **covered** | 1 | 11 | - | 1,239.48 | - | 1,232 | - | 0.000898 | 🟢 medium — moderately distinctive | — |
| 2271 | **crystal** | 1 | 4 | - | 568.89 | 0.232259 | 2,271 | 2,071 | 0.000898 | 🟢 medium — moderately distinctive | — |
| 2272 | **verse** | 1 | 3 | - | 498.58 | 0.205302 | 2,615 | 1,847 | 0.000898 | 🔵 low — common in general English | — |
| 2273 | **hik** | 1 | 3 | - | 498.58 | 0.193939 | 2,655 | 1,828 | 0.000898 | 🔵 low — common in general English | — |
| 2274 | **accordance** | 1 | 4 | - | 516.64 | 0.231817 | 2,339 | 2,020 | 0.000898 | 🟢 medium — moderately distinctive | — |
| 2275 | **orgyen** | 1 | 3 | - | 498.58 | 0.194107 | 2,657 | 1,829 | 0.000897 | 🔵 low — common in general English | — |
| 2276 | **edge** | 1 | 4 | - | 498.77 | 0.231759 | 2,359 | 2,007 | 0.000897 | 🔵 low — common in general English | — |
| 2277 | **twenty** | 1 | 8 | - | 1,233.88 | - | 1,236 | - | 0.000896 | 🟢 medium — moderately distinctive | ~ |
| 2278 | **committing** | 1 | 8 | - | 1,233.88 | - | 1,238 | - | 0.000895 | 🟢 medium — moderately distinctive | — |
| 2279 | **finish** | 1 | 1 | - | 142.22 | 0.107895 | 7,161 | 1,263 | 0.000894 | 🔵 low — common in general English | — |
| 2280 | **reflecting** | 1 | 12 | - | 1,233.10 | - | 1,240 | - | 0.000894 | 🟢 medium — moderately distinctive | — |
| 2281 | **longchen** | 1 | 3 | - | 498.58 | 0.221083 | 2,602 | 1,871 | 0.000894 | 🔵 low — common in general English | — |
| 2282 | **royalty** | 1 | 4 | - | 495.69 | 0.196475 | 2,659 | 1,843 | 0.000893 | 🔵 low — common in general English | ~ |
| 2283 | **mature** | 1 | 4 | - | 540.79 | 0.232231 | 2,311 | 2,067 | 0.000892 | 🟢 medium — moderately distinctive | — |
| 2284 | **mafijusrimitra** | 1 | 3 | - | 498.58 | 0.222327 | 2,600 | 1,879 | 0.000892 | 🔵 low — common in general English | — |
| 2285 | **vallabha** | 1 | 3 | - | 498.58 | 0.220704 | 2,620 | 1,870 | 0.000891 | 🔵 low — common in general English | — |
| 2286 | **sent** | 1 | 12 | - | 1,230.45 | - | 1,244 | - | 0.000891 | 🟢 medium — moderately distinctive | — |
| 2287 | **applying** | 1 | 9 | - | 1,230.34 | - | 1,245 | - | 0.000891 | 🟢 medium — moderately distinctive | — |
| 2288 | **north** | 1 | 5 | - | 423.94 | 0.182510 | 2,824 | 1,779 | 0.000891 | 🔵 low — common in general English | — |
| 2289 | **breach** | 1 | 9 | - | 1,230.34 | - | 1,246 | - | 0.000890 | 🟢 medium — moderately distinctive | — |
| 2290 | **less** | 1 | 16 | - | 1,227.88 | - | 1,247 | - | 0.000890 | 🟢 medium — moderately distinctive | — |
| 2291 | **angulimala** | 1 | 3 | - | 498.58 | 0.221468 | 2,631 | 1,872 | 0.000889 | 🔵 low — common in general English | ✓ སོར་མོ་ཕྲེང་བ |
| 2292 | **gone** | 1 | 10 | - | 1,217.97 | - | 1,248 | - | 0.000889 | 🟢 medium — moderately distinctive | — |
| 2293 | **felt** | 1 | 11 | - | 1,207.64 | - | 1,250 | - | 0.000888 | 🟢 medium — moderately distinctive | — |
| 2294 | **speaking** | 1 | 12 | - | 1,203.34 | - | 1,251 | - | 0.000887 | 🟢 medium — moderately distinctive | — |
| 2295 | **mahakasyapa** | 1 | 3 | - | 498.58 | 0.221794 | 2,639 | 1,876 | 0.000887 | 🔵 low — common in general English | — |
| 2296 | **subsequently** | 1 | 4 | - | 512.68 | 0.232221 | 2,345 | 2,065 | 0.000886 | 🟢 medium — moderately distinctive | — |
| 2297 | **mipham** | 1 | 3 | - | 498.58 | 0.222027 | 2,644 | 1,878 | 0.000886 | 🔵 low — common in general English | — |
| 2298 | **cosmo** | 1 | 8 | - | 1,202.95 | - | 1,254 | - | 0.000885 | 🟢 medium — moderately distinctive | — |
| 2299 | **attribute** | 1 | 8 | - | 1,202.95 | - | 1,255 | - | 0.000885 | 🟢 medium — moderately distinctive | — |
| 2300 | **cook** | 1 | 2 | - | 276.71 | 0.148465 | 3,952 | 1,515 | 0.000884 | 🔵 low — common in general English | — |
| 2301 | **chopel** | 1 | 3 | - | 498.58 | 0.222436 | 2,654 | 1,881 | 0.000884 | 🔵 low — common in general English | — |
| 2302 | **nobody** | 1 | 9 | - | 1,192.73 | - | 1,260 | - | 0.000882 | 🟢 medium — moderately distinctive | — |
| 2303 | **site** | 1 | 4 | - | 505.38 | 0.232341 | 2,353 | 2,079 | 0.000882 | 🟢 medium — moderately distinctive | — |
| 2304 | **cutting** | 1 | 12 | - | 1,192.10 | - | 1,261 | - | 0.000881 | 🟢 medium — moderately distinctive | — |
| 2305 | **containing** | 1 | 10 | - | 1,181.99 | - | 1,262 | - | 0.000881 | 🟢 medium — moderately distinctive | — |
| 2306 | **breathe** | 1 | 3 | - | 498.74 | 0.232160 | 2,387 | 2,059 | 0.000881 | 🔵 low — common in general English | — |
| 2307 | **broken** | 1 | 10 | - | 1,181.99 | - | 1,263 | - | 0.000880 | 🟢 medium — moderately distinctive | — |
| 2308 | **gain** | 1 | 5 | - | 343.61 | 0.182415 | 2,965 | 1,760 | 0.000880 | 🔵 low — common in general English | — |
| 2309 | **explaining** | 1 | 9 | - | 1,181.96 | - | 1,264 | - | 0.000880 | 🟢 medium — moderately distinctive | — |
| 2310 | **minister** | 1 | 7 | - | 491.05 | 0.223920 | 2,666 | 1,890 | 0.000880 | 🔵 low — common in general English | — |
| 2311 | **contemplate** | 1 | 3 | - | 451.10 | 0.215583 | 2,754 | 1,853 | 0.000878 | 🔵 low — common in general English | — |
| 2312 | **serious** | 1 | 12 | - | 1,173.28 | - | 1,268 | - | 0.000877 | 🟢 medium — moderately distinctive | — |
| 2313 | **bringing** | 1 | 11 | - | 1,171.06 | - | 1,269 | - | 0.000877 | 🟢 medium — moderately distinctive | — |
| 2314 | **border** | 1 | 4 | - | 492.74 | 0.228120 | 2,661 | 1,917 | 0.000873 | 🔵 low — common in general English | ~ |
| 2315 | **threw** | 1 | 7 | - | 1,163.73 | - | 1,276 | - | 0.000873 | 🟢 medium — moderately distinctive | — |
| 2316 | **representative** | 1 | 5 | - | 486.40 | 0.228290 | 2,671 | 1,921 | 0.000871 | 🔵 low — common in general English | — |
| 2317 | **choice** | 1 | 4 | - | 487.19 | 0.229797 | 2,669 | 1,924 | 0.000870 | 🔵 low — common in general English | — |
| 2318 | **bank** | 1 | 8 | - | 428.96 | 0.216397 | 2,811 | 1,856 | 0.000870 | 🔵 low — common in general English | — |
| 2319 | **herself** | 1 | 7 | - | 1,163.73 | - | 1,282 | - | 0.000870 | 🟢 medium — moderately distinctive | — |
| 2320 | **collapse** | 1 | 4 | - | 441.86 | 0.222362 | 2,781 | 1,880 | 0.000867 | 🔵 low — common in general English | — |
| 2321 | **unite** | 1 | 3 | - | 498.58 | 0.232391 | 2,441 | 2,081 | 0.000867 | 🔵 low — common in general English | — |
| 2322 | **dedicating** | 1 | 7 | - | 1,163.35 | - | 1,288 | - | 0.000866 | 🟢 medium — moderately distinctive | — |
| 2323 | **slowly** | 1 | 4 | - | 492.74 | 0.231058 | 2,663 | 1,945 | 0.000866 | 🔵 low — common in general English | — |
| 2324 | **forgetting** | 1 | 7 | - | 1,163.35 | - | 1,291 | - | 0.000865 | 🟢 medium — moderately distinctive | — |
| 2325 | **deluded** | 1 | 7 | - | 1,163.35 | - | 1,293 | - | 0.000863 | 🟢 medium — moderately distinctive | — |
| 2326 | **consult** | 1 | 2 | - | 284.45 | 0.149592 | 3,911 | 1,577 | 0.000863 | 🔵 low — common in general English | — |
| 2327 | **cosmos** | 1 | - | - | - | 0.108378 | - | 1,295 | 0.000862 | - | — |
| 2328 | **mastered** | 1 | 7 | - | 1,163.35 | - | 1,296 | - | 0.000862 | 🟢 medium — moderately distinctive | — |
| 2329 | **chest** | 1 | 3 | - | 498.58 | 0.254164 | 2,458 | 2,095 | 0.000861 | 🔵 low — common in general English | — |
| 2330 | **liquid** | 1 | 4 | - | 464.63 | 0.230940 | 2,718 | 1,941 | 0.000860 | 🔵 low — common in general English | — |
| 2331 | **temporarily** | 1 | 4 | - | 482.05 | 0.231384 | 2,674 | 1,965 | 0.000860 | 🔵 low — common in general English | — |
| 2332 | **begged** | 1 | 7 | - | 1,163.35 | - | 1,302 | - | 0.000859 | 🟢 medium — moderately distinctive | — |
| 2333 | **syllable hum** | 2 | 3 | 0.587 | - | 0.109327 | - | 1,303 | 0.000858 | - | — |
| 2334 | **aroused** | 1 | 7 | - | 1,163.35 | - | 1,304 | - | 0.000858 | 🟢 medium — moderately distinctive | — |
| 2335 | **devour** | 1 | 3 | - | 498.58 | 0.254280 | 2,492 | 2,096 | 0.000856 | 🔵 low — common in general English | — |
| 2336 | **miraculous power** | 2 | 4 | 0.547 | - | 0.109895 | - | 1,308 | 0.000855 | - | — |
| 2337 | **clinging** | 1 | 7 | - | 1,163.35 | - | 1,312 | - | 0.000853 | 🟢 medium — moderately distinctive | ✓ འཛིན་པ |
| 2338 | **attain enlightenment** | 2 | 4 | 0.565 | - | 0.110476 | - | 1,312 | 0.000853 | - | — |
| 2339 | **answered** | 1 | 7 | - | 1,163.35 | - | 1,313 | - | 0.000853 | 🟢 medium — moderately distinctive | — |
| 2340 | **pursue** | 1 | 4 | - | 447.64 | 0.231065 | 2,775 | 1,946 | 0.000851 | 🔵 low — common in general English | — |
| 2341 | **glorious protector** | 2 | 3 | 0.579 | - | 0.110944 | - | 1,316 | 0.000851 | - | ~ |
| 2342 | **lax** | 1 | 3 | - | 498.58 | 0.257781 | 2,525 | 2,099 | 0.000850 | 🔵 low — common in general English | — |
| 2343 | **rinchen zangpo** | 2 | 3 | 0.908 | - | 0.113100 | - | 1,319 | 0.000850 | - | ✓ རིན་ཆེན་བཟང་པོ |
| 2344 | **wide** | 1 | 4 | - | 457.33 | 0.231448 | 2,745 | 1,969 | 0.000849 | 🔵 low — common in general English | — |
| 2345 | **praying** | 1 | 7 | - | 1,163.35 | - | 1,320 | - | 0.000849 | 🟢 medium — moderately distinctive | — |
| 2346 | **real meaning** | 2 | 3 | 0.486 | - | 0.114211 | - | 1,321 | 0.000849 | - | ✓ ངེས་དོན |
| 2347 | **circumambulate** | 1 | 2 | - | 332.39 | 0.182316 | 3,335 | 1,749 | 0.000847 | 🔵 low — common in general English | — |
| 2348 | **conditioning effect** | 2 | 3 | 0.647 | - | 0.116865 | - | 1,324 | 0.000847 | - | ✓ དབང་གི་འབྲས་བུ |
| 2349 | **symboliz** | 1 | 7 | - | 1,163.35 | - | 1,325 | - | 0.000846 | 🟢 medium — moderately distinctive | — |
| 2350 | **white lotus** | 2 | 3 | 0.582 | - | 0.116873 | - | 1,325 | 0.000846 | - | ~ |
| 2351 | **extent** | 1 | 4 | - | 431.57 | 0.231142 | 2,805 | 1,952 | 0.000846 | 🔵 low — common in general English | — |
| 2352 | **elapatra** | 1 | 3 | - | 498.58 | 0.257398 | 2,562 | 2,098 | 0.000845 | 🔵 low — common in general English | — |
| 2353 | **amount** | 1 | 15 | - | 1,163.30 | - | 1,330 | - | 0.000844 | 🟢 medium — moderately distinctive | — |
| 2354 | **ultimately** | 1 | 4 | - | 484.57 | 0.231971 | 2,672 | 2,035 | 0.000843 | 🔵 low — common in general English | — |
| 2355 | **gracious root** | 2 | 3 | 0.726 | - | 0.120037 | - | 1,331 | 0.000843 | - | — |
| 2356 | **absence** | 1 | 4 | - | 492.74 | 0.232022 | 2,662 | 2,043 | 0.000843 | 🔵 low — common in general English | — |
| 2357 | **authority** | 1 | 4 | - | 399.59 | 0.230720 | 2,872 | 1,933 | 0.000843 | 🔵 low — common in general English | — |
| 2358 | **realize emptiness** | 2 | 3 | 0.565 | - | 0.120375 | - | 1,332 | 0.000843 | - | — |
| 2359 | **intelligence** | 1 | 4 | - | 489.91 | 0.232004 | 2,668 | 2,040 | 0.000843 | 🔵 low — common in general English | — |
| 2360 | **fine** | 1 | 4 | - | 479.62 | 0.231988 | 2,675 | 2,038 | 0.000842 | 🔵 low — common in general English | — |
| 2361 | **dodrup chen** | 2 | 4 | 1.000 | - | 0.120836 | - | 1,334 | 0.000842 | - | — |
| 2362 | **bathe** | 1 | 3 | - | 498.58 | 0.260790 | 2,573 | 2,108 | 0.000841 | 🔵 low — common in general English | — |
| 2363 | **criticism** | 1 | 4 | - | 472.80 | 0.231870 | 2,711 | 2,024 | 0.000841 | 🔵 low — common in general English | — |
| 2364 | **dedicated** | 1 | 8 | - | 1,156.30 | - | 1,336 | - | 0.000841 | 🟢 medium — moderately distinctive | — |
| 2365 | **defend** | 1 | 4 | - | 446.15 | 0.231668 | 2,777 | 1,992 | 0.000840 | 🔵 low — common in general English | — |
| 2366 | **convinced** | 1 | 10 | - | 1,147.71 | - | 1,338 | - | 0.000840 | 🟢 medium — moderately distinctive | — |
| 2367 | **bestow** | 1 | 3 | - | 498.58 | 0.260416 | 2,587 | 2,105 | 0.000840 | 🔵 low — common in general English | — |
| 2368 | **quickly** | 1 | 4 | - | 403.46 | 0.231105 | 2,865 | 1,950 | 0.000839 | 🔵 low — common in general English | — |
| 2369 | **defile** | 1 | 2 | - | 332.39 | 0.182436 | 3,372 | 1,765 | 0.000839 | 🔵 low — common in general English | — |
| 2370 | **nine** | 1 | 19 | - | 1,139.53 | - | 1,339 | - | 0.000839 | 🟢 medium — moderately distinctive | ~ |
| 2371 | **stroke** | 1 | 3 | - | 498.58 | 0.259656 | 2,597 | 2,102 | 0.000839 | 🔵 low — common in general English | — |
| 2372 | **contaminate** | 1 | 2 | - | 332.39 | 0.182500 | 3,338 | 1,777 | 0.000839 | 🔵 low — common in general English | — |
| 2373 | **maturity** | 1 | 4 | - | 459.08 | 0.231784 | 2,744 | 2,015 | 0.000839 | 🔵 low — common in general English | — |
| 2374 | **feed** | 1 | 4 | - | 402.67 | 0.231291 | 2,866 | 1,958 | 0.000837 | 🔵 low — common in general English | — |
| 2375 | **afar** | 1 | 3 | - | 498.58 | 0.260609 | 2,608 | 2,106 | 0.000836 | 🔵 low — common in general English | ~ |
| 2376 | **nearby** | 1 | 4 | - | 440.49 | 0.231739 | 2,792 | 2,002 | 0.000836 | 🔵 low — common in general English | — |
| 2377 | **fundamental** | 1 | 4 | - | 452.31 | 0.231986 | 2,752 | 2,036 | 0.000833 | 🔵 low — common in general English | — |
| 2378 | **lost** | 1 | 12 | - | 1,125.28 | - | 1,352 | - | 0.000833 | 🟢 medium — moderately distinctive | — |
| 2379 | **trial** | 1 | 8 | - | 1,121.46 | - | 1,353 | - | 0.000832 | 🟢 medium — moderately distinctive | — |
| 2380 | **ease** | 1 | 4 | - | 407.57 | 0.231697 | 2,855 | 1,995 | 0.000830 | 🔵 low — common in general English | — |
| 2381 | **precious metal** | 2 | 3 | 0.528 | - | 0.124011 | - | 1,359 | 0.000829 | - | — |
| 2382 | **attention** | 1 | 4 | - | 440.49 | 0.231950 | 2,793 | 2,032 | 0.000829 | 🔵 low — common in general English | — |
| 2383 | **plough** | 1 | 3 | - | 477.66 | 0.255069 | 2,681 | 2,097 | 0.000828 | 🔵 low — common in general English | — |
| 2384 | **letting** | 1 | 7 | - | 1,114.54 | - | 1,361 | - | 0.000828 | 🟢 medium — moderately distinctive | — |
| 2385 | **onward** | 1 | 7 | - | 1,114.54 | - | 1,362 | - | 0.000828 | 🟢 medium — moderately distinctive | — |
| 2386 | **give rise** | 2 | 4 | 0.557 | - | 0.124683 | - | 1,363 | 0.000827 | - | — |
| 2387 | **magic** | 1 | 3 | - | 477.66 | 0.259973 | 2,685 | 2,103 | 0.000827 | 🔵 low — common in general English | ~ |
| 2388 | **enjoying** | 1 | 7 | - | 1,114.54 | - | 1,365 | - | 0.000826 | 🟢 medium — moderately distinctive | ~ |
| 2389 | **afterward** | 1 | 7 | - | 1,114.54 | - | 1,366 | - | 0.000826 | 🟢 medium — moderately distinctive | — |
| 2390 | **store** | 1 | 4 | - | 446.15 | 0.232101 | 2,776 | 2,054 | 0.000826 | 🔵 low — common in general English | — |
| 2391 | **count** | 1 | 3 | - | 405.59 | 0.231779 | 2,857 | 2,013 | 0.000825 | 🔵 low — common in general English | — |
| 2392 | **transmitted** | 1 | 7 | - | 1,114.54 | - | 1,368 | - | 0.000825 | 🟢 medium — moderately distinctive | — |
| 2393 | **sister** | 1 | 8 | - | 1,106.85 | - | 1,372 | - | 0.000823 | 🟢 medium — moderately distinctive | — |
| 2394 | **pulled** | 1 | 8 | - | 1,106.85 | - | 1,373 | - | 0.000822 | 🟢 medium — moderately distinctive | — |
| 2395 | **extend** | 1 | 4 | - | 425.84 | 0.232029 | 2,822 | 2,045 | 0.000822 | 🔵 low — common in general English | — |
| 2396 | **specific** | 1 | 4 | - | 386.58 | 0.231774 | 2,896 | 2,009 | 0.000822 | 🔵 low — common in general English | — |
| 2397 | **peak** | 1 | 4 | - | 449.16 | 0.232291 | 2,774 | 2,075 | 0.000821 | 🔵 low — common in general English | — |
| 2398 | **local** | 1 | 4 | - | 358.68 | 0.231682 | 2,942 | 1,994 | 0.000820 | 🔵 low — common in general English | — |
| 2399 | **sink** | 1 | 3 | - | 451.10 | 0.254061 | 2,758 | 2,094 | 0.000819 | 🔵 low — common in general English | — |
| 2400 | **rather** | 1 | 12 | - | 1,087.63 | - | 1,381 | - | 0.000818 | 🟢 medium — moderately distinctive | — |
| 2401 | **commerce** | 1 | 4 | - | 356.62 | 0.231747 | 2,944 | 2,005 | 0.000817 | 🔵 low — common in general English | — |
| 2402 | **evil rebirth** | 2 | 4 | 0.478 | - | 0.125445 | - | 1,385 | 0.000816 | - | — |
| 2403 | **travelling** | 1 | 7 | - | 1,079.65 | - | 1,387 | - | 0.000815 | 🟢 medium — moderately distinctive | — |
| 2404 | **access** | 1 | 4 | - | 410.15 | 0.232275 | 2,845 | 2,072 | 0.000813 | 🔵 low — common in general English | — |
| 2405 | **single drop** | 2 | 3 | 0.517 | - | 0.125710 | - | 1,393 | 0.000813 | - | — |
| 2406 | **merge** | 1 | 4 | - | 401.89 | 0.232289 | 2,868 | 2,074 | 0.000810 | 🔵 low — common in general English | — |
| 2407 | **last** | 1 | 5 | - | 235.10 | 0.181530 | 4,098 | 1,698 | 0.000809 | 🔵 low — common in general English | — |
| 2408 | **temporary** | 1 | 4 | - | 381.17 | 0.232158 | 2,911 | 2,058 | 0.000809 | 🔵 low — common in general English | — |
| 2409 | **talking** | 1 | 10 | - | 1,053.93 | - | 1,403 | - | 0.000808 | 🟢 medium — moderately distinctive | — |
| 2410 | **relate** | 1 | - | - | - | 0.125914 | - | 1,404 | 0.000807 | - | — |
| 2411 | **harvest** | 1 | 4 | - | 416.58 | 0.260769 | 2,839 | 2,107 | 0.000806 | 🔵 low — common in general English | — |
| 2412 | **tingdzin zangpo** | 2 | 3 | 0.935 | - | 0.126198 | - | 1,409 | 0.000805 | - | ~ |
| 2413 | **chinese** | 1 | 3 | - | 328.36 | 0.186719 | 3,687 | 1,799 | 0.000805 | 🔵 low — common in general English | — |
| 2414 | **considered** | 1 | 11 | - | 1,051.43 | - | 1,410 | - | 0.000805 | 🟢 medium — moderately distinctive | — |
| 2415 | **worldly activity** | 2 | 6 | 0.605 | - | 0.126721 | - | 1,411 | 0.000804 | - | ~ |
| 2416 | **usually** | 1 | 9 | - | 1,041.15 | - | 1,416 | - | 0.000802 | 🟢 medium — moderately distinctive | — |
| 2417 | **prepared** | 1 | 11 | - | 1,032.97 | - | 1,418 | - | 0.000801 | 🟢 medium — moderately distinctive | — |
| 2418 | **young brahmin** | 2 | 6 | 0.703 | - | 0.128490 | - | 1,418 | 0.000801 | - | — |
| 2419 | **push** | 1 | 2 | - | 207.81 | 0.181948 | 4,165 | 1,713 | 0.000801 | 🔵 low — common in general English | — |
| 2420 | **receiving** | 1 | 9 | - | 1,032.94 | - | 1,419 | - | 0.000801 | 🟢 medium — moderately distinctive | — |
| 2421 | **experiencing** | 1 | 7 | - | 1,030.46 | - | 1,421 | - | 0.000800 | 🟢 medium — moderately distinctive | — |
| 2422 | **item** | 1 | 3 | - | 348.47 | 0.253195 | 2,952 | 2,092 | 0.000797 | 🔵 low — common in general English | — |
| 2423 | **inherit** | 1 | 2 | - | 332.49 | 0.232058 | 3,046 | 2,049 | 0.000796 | 🔵 low — common in general English | — |
| 2424 | **greatest** | 1 | 8 | - | 1,003.99 | - | 1,430 | - | 0.000796 | 🟢 medium — moderately distinctive | — |
| 2425 | **permitted** | 1 | 8 | - | 997.54 | - | 1,433 | - | 0.000794 | 🟢 medium — moderately distinctive | — |
| 2426 | **whoever** | 1 | 6 | - | 997.48 | - | 1,434 | - | 0.000794 | 🟢 medium — moderately distinctive | — |
| 2427 | **blind man** | 2 | 4 | 0.576 | - | 0.134436 | - | 1,442 | 0.000790 | - | — |
| 2428 | **heart-essence** | 1 | 6 | - | 997.16 | - | 1,445 | - | 0.000789 | 🟢 medium — moderately distinctive | — |
| 2429 | **twenty-five** | 1 | 6 | - | 997.16 | - | 1,446 | - | 0.000788 | 🟢 medium — moderately distinctive | — |
| 2430 | **metaphor** | 1 | 6 | - | 997.16 | - | 1,450 | - | 0.000787 | 🟢 medium — moderately distinctive | — |
| 2431 | **inhabitant** | 1 | 6 | - | 997.16 | - | 1,453 | - | 0.000785 | 🟢 medium — moderately distinctive | — |
| 2432 | **grasping** | 1 | 6 | - | 997.16 | - | 1,455 | - | 0.000784 | 🟢 medium — moderately distinctive | — |
| 2433 | **symbol lineage** | 2 | 5 | 0.684 | - | 0.135421 | - | 1,455 | 0.000784 | - | ~ |
| 2434 | **absolute truth** | 2 | 5 | 0.666 | - | 0.136803 | - | 1,457 | 0.000784 | - | ✓ དོན་དམ་བདེན་པ |
| 2435 | **wandering** | 1 | 6 | - | 997.16 | - | 1,458 | - | 0.000783 | 🟢 medium — moderately distinctive | — |
| 2436 | **ris** | 1 | 6 | - | 997.16 | - | 1,463 | - | 0.000781 | 🟢 medium — moderately distinctive | — |
| 2437 | **perform transference** | 2 | 3 | 0.522 | - | 0.138087 | - | 1,463 | 0.000781 | - | — |
| 2438 | **dry land** | 2 | 3 | 0.606 | - | 0.139732 | - | 1,468 | 0.000779 | - | — |
| 2439 | **bristling** | 1 | 6 | - | 997.16 | - | 1,469 | - | 0.000778 | 🟢 medium — moderately distinctive | — |
| 2440 | **possessed** | 1 | 6 | - | 997.16 | - | 1,470 | - | 0.000778 | 🟢 medium — moderately distinctive | — |
| 2441 | **meditated** | 1 | 6 | - | 997.16 | - | 1,476 | - | 0.000775 | 🟢 medium — moderately distinctive | — |
| 2442 | **upwards** | 1 | - | - | - | 0.142150 | - | 1,478 | 0.000775 | - | — |
| 2443 | **particle** | 1 | 6 | - | 997.16 | - | 1,480 | - | 0.000774 | 🟢 medium — moderately distinctive | — |
| 2444 | **material giving** | 2 | 3 | 0.521 | - | 0.142902 | - | 1,480 | 0.000774 | - | — |
| 2445 | **meditate persistently** | 2 | 4 | 0.726 | - | 0.142949 | - | 1,481 | 0.000773 | - | — |
| 2446 | **pith-instruction** | 1 | 6 | - | 997.16 | - | 1,485 | - | 0.000772 | 🟢 medium — moderately distinctive | — |
| 2447 | **prostrated** | 1 | 6 | - | 997.16 | - | 1,487 | - | 0.000771 | 🟢 medium — moderately distinctive | — |
| 2448 | **onwards** | 1 | - | - | - | 0.145407 | - | 1,487 | 0.000771 | - | — |
| 2449 | **prayed** | 1 | 6 | - | 997.16 | - | 1,491 | - | 0.000769 | 🟢 medium — moderately distinctive | — |
| 2450 | **dynasty** | 1 | 2 | - | 332.39 | 0.297052 | 3,179 | 2,122 | 0.000767 | 🔵 low — common in general English | — |
| 2451 | **hard-to-endure** | 1 | 6 | - | 997.16 | - | 1,497 | - | 0.000767 | 🟢 medium — moderately distinctive | — |
| 2452 | **perfectly dedicate** | 2 | 3 | 0.541 | - | 0.146571 | - | 1,497 | 0.000767 | - | — |
| 2453 | **periods** | 1 | - | - | - | 0.146828 | - | 1,498 | 0.000766 | - | — |
| 2454 | **rejoicing** | 1 | 6 | - | 997.16 | - | 1,499 | - | 0.000766 | 🟢 medium — moderately distinctive | — |
| 2455 | **emanate** | 1 | 6 | - | 997.16 | - | 1,500 | - | 0.000765 | 🟢 medium — moderately distinctive | — |
| 2456 | **meant** | 1 | 9 | - | 994.18 | - | 1,507 | - | 0.000763 | 🟢 medium — moderately distinctive | — |
| 2457 | **except** | 1 | 9 | - | 982.18 | - | 1,511 | - | 0.000761 | 🟢 medium — moderately distinctive | — |
| 2458 | **avoided** | 1 | 7 | - | 981.27 | - | 1,512 | - | 0.000761 | 🟢 medium — moderately distinctive | — |
| 2459 | **aside** | 1 | 8 | - | 969.15 | - | 1,517 | - | 0.000759 | 🟢 medium — moderately distinctive | — |
| 2460 | **concentrated** | 1 | 8 | - | 969.15 | - | 1,518 | - | 0.000758 | 🟢 medium — moderately distinctive | — |
| 2461 | **looked** | 1 | 8 | - | 969.15 | - | 1,519 | - | 0.000758 | 🟢 medium — moderately distinctive | — |
| 2462 | **based** | 1 | 13 | - | 968.70 | - | 1,520 | - | 0.000757 | 🟢 medium — moderately distinctive | — |
| 2463 | **warm flesh** | 2 | 4 | 0.625 | - | 0.148728 | - | 1,521 | 0.000757 | - | — |
| 2464 | **accepted** | 1 | 10 | - | 963.35 | - | 1,522 | - | 0.000757 | 🟢 medium — moderately distinctive | — |
| 2465 | **garden** | 1 | 7 | - | 956.93 | - | 1,523 | - | 0.000756 | 🟢 medium — moderately distinctive | — |
| 2466 | **deepest** | 1 | 6 | - | 955.32 | - | 1,524 | - | 0.000756 | 🟢 medium — moderately distinctive | — |
| 2467 | **proliferate** | 1 | 1 | - | 166.19 | 0.181607 | 5,276 | 1,703 | 0.000755 | 🔵 low — common in general English | — |
| 2468 | **thorn** | 1 | 6 | - | 955.32 | - | 1,531 | - | 0.000753 | 🟢 medium — moderately distinctive | — |
| 2469 | **reject** | 1 | 1 | - | 123.92 | 0.149318 | 7,392 | 1,560 | 0.000751 | 🔵 low — common in general English | — |
| 2470 | **finished** | 1 | 8 | - | 954.54 | - | 1,538 | - | 0.000750 | 🟢 medium — moderately distinctive | — |
| 2471 | **obtained** | 1 | 8 | - | 949.99 | - | 1,542 | - | 0.000749 | 🟢 medium — moderately distinctive | — |
| 2472 | **divided** | 1 | 8 | - | 945.59 | - | 1,544 | - | 0.000748 | 🟢 medium — moderately distinctive | — |
| 2473 | **led** | 1 | 11 | - | 939.74 | - | 1,547 | - | 0.000747 | 🟢 medium — moderately distinctive | — |
| 2474 | **former** | 1 | 10 | - | 939.06 | - | 1,548 | - | 0.000746 | 🟢 medium — moderately distinctive | — |
| 2475 | **trapped** | 1 | 7 | - | 936.67 | - | 1,550 | - | 0.000746 | 🟢 medium — moderately distinctive | — |
| 2476 | **tried** | 1 | 8 | - | 925.46 | - | 1,556 | - | 0.000743 | 🟢 medium — moderately distinctive | — |
| 2477 | **plunge** | 1 | 2 | - | 265.05 | 0.231326 | 4,006 | 1,959 | 0.000741 | 🔵 low — common in general English | — |
| 2478 | **crossed** | 1 | 6 | - | 925.41 | - | 1,562 | - | 0.000741 | 🟢 medium — moderately distinctive | — |
| 2479 | **com** | 1 | 6 | - | 925.41 | - | 1,568 | - | 0.000739 | 🟢 medium — moderately distinctive | — |
| 2480 | **including** | 1 | 13 | - | 921.39 | - | 1,570 | - | 0.000738 | 🟢 medium — moderately distinctive | — |
| 2481 | **attached** | 1 | 7 | - | 919.31 | - | 1,571 | - | 0.000738 | 🟢 medium — moderately distinctive | — |
| 2482 | **written** | 1 | 8 | - | 914.65 | - | 1,575 | - | 0.000736 | 🟢 medium — moderately distinctive | — |
| 2483 | **bearing** | 1 | 7 | - | 911.48 | - | 1,576 | - | 0.000736 | 🟢 medium — moderately distinctive | — |
| 2484 | **accepting** | 1 | 7 | - | 911.48 | - | 1,577 | - | 0.000735 | 🟢 medium — moderately distinctive | — |
| 2485 | **effective** | 1 | 4 | - | 305.99 | 0.231962 | 3,822 | 2,034 | 0.000735 | 🔵 low — common in general English | — |
| 2486 | **tip** | 1 | 6 | - | 902.21 | - | 1,581 | - | 0.000734 | 🟢 medium — moderately distinctive | — |
| 2487 | **somewhere** | 1 | 6 | - | 902.21 | - | 1,582 | - | 0.000733 | 🟢 medium — moderately distinctive | — |
| 2488 | **cooked** | 1 | 6 | - | 902.21 | - | 1,583 | - | 0.000733 | 🟢 medium — moderately distinctive | — |
| 2489 | **against** | 1 | 15 | - | 890.75 | - | 1,586 | - | 0.000732 | 🟢 medium — moderately distinctive | — |
| 2490 | **sri simha** | 2 | 3 | 0.973 | - | 0.152241 | - | 1,587 | 0.000732 | - | — |
| 2491 | **returned** | 1 | 8 | - | 886.52 | - | 1,588 | - | 0.000731 | 🟢 medium — moderately distinctive | — |
| 2492 | **understood** | 1 | 7 | - | 884.41 | - | 1,589 | - | 0.000731 | 🟢 medium — moderately distinctive | — |
| 2493 | **sustain** | 1 | 2 | - | 251.00 | 0.231673 | 4,050 | 1,993 | 0.000730 | 🔵 low — common in general English | — |
| 2494 | **guided** | 1 | 6 | - | 883.25 | - | 1,591 | - | 0.000730 | 🟢 medium — moderately distinctive | — |
| 2495 | **jump** | 1 | 2 | - | 244.95 | 0.231663 | 4,064 | 1,991 | 0.000730 | 🔵 low — common in general English | — |
| 2496 | **forgotten** | 1 | 6 | - | 883.25 | - | 1,593 | - | 0.000729 | 🟢 medium — moderately distinctive | — |
| 2497 | **spoken** | 1 | 6 | - | 883.25 | - | 1,594 | - | 0.000729 | 🟢 medium — moderately distinctive | — |
| 2498 | **mentioned** | 1 | 7 | - | 878.49 | - | 1,597 | - | 0.000728 | 🟢 medium — moderately distinctive | — |
| 2499 | **various** | 1 | 9 | - | 876.99 | - | 1,598 | - | 0.000728 | 🟢 medium — moderately distinctive | — |
| 2500 | **decided** | 1 | 10 | - | 873.29 | - | 1,599 | - | 0.000727 | 🟢 medium — moderately distinctive | — |
| 2501 | **meanwhile** | 1 | 8 | - | 873.05 | - | 1,600 | - | 0.000727 | 🟢 medium — moderately distinctive | — |
| 2502 | **gathering** | 1 | 7 | - | 872.85 | - | 1,601 | - | 0.000726 | 🟢 medium — moderately distinctive | — |
| 2503 | **central region** | 2 | 5 | 0.714 | - | 0.158331 | - | 1,601 | 0.000726 | - | — |
| 2504 | **sexual misconduct** | 2 | 11 | 0.974 | - | 0.159565 | - | 1,602 | 0.000726 | - | — |
| 2505 | **achieved** | 1 | 8 | - | 868.01 | - | 1,603 | - | 0.000726 | 🟢 medium — moderately distinctive | — |
| 2506 | **body speech** | 2 | 24 | 0.653 | - | 0.162562 | - | 1,603 | 0.000726 | - | ~ |
| 2507 | **downward** | 1 | 8 | - | 868.01 | - | 1,604 | - | 0.000725 | 🟢 medium — moderately distinctive | — |
| 2508 | **sakyas** | 1 | - | - | - | 0.162842 | - | 1,604 | 0.000725 | - | — |
| 2509 | **loss** | 1 | 4 | - | 211.57 | 0.231648 | 4,159 | 1,989 | 0.000725 | 🔵 low — common in general English | — |
| 2510 | **dakini yeshe tsogyal** | 3 | 3 | 0.916 | - | 0.165718 | - | 1,605 | 0.000725 | - | ~ |
| 2511 | **golden wheel** | 2 | 3 | 0.625 | - | 0.165914 | - | 1,606 | 0.000725 | - | — |
| 2512 | **mipham gonpo** | 2 | 3 | 0.952 | - | 0.167965 | - | 1,607 | 0.000724 | - | — |
| 2513 | **ordinary folk** | 2 | 3 | 0.686 | - | 0.168118 | - | 1,608 | 0.000724 | - | — |
| 2514 | **everybody** | 1 | 6 | - | 867.22 | - | 1,611 | - | 0.000723 | 🟢 medium — moderately distinctive | — |
| 2515 | **consulted** | 1 | 6 | - | 867.22 | - | 1,612 | - | 0.000722 | 🟢 medium — moderately distinctive | — |
| 2516 | **entered** | 1 | 9 | - | 861.59 | - | 1,613 | - | 0.000722 | 🟢 medium — moderately distinctive | — |
| 2517 | **certainly** | 1 | 8 | - | 860.77 | - | 1,614 | - | 0.000722 | 🟢 medium — moderately distinctive | — |
| 2518 | **refused** | 1 | 8 | - | 856.15 | - | 1,616 | - | 0.000721 | 🟢 medium — moderately distinctive | — |
| 2519 | **further** | 1 | 13 | - | 855.09 | - | 1,617 | - | 0.000721 | 🟢 medium — moderately distinctive | — |
| 2520 | **yogis** | 1 | - | - | - | 0.170699 | - | 1,617 | 0.000721 | - | — |
| 2521 | **vigorous** | 1 | 2 | - | 294.42 | 0.233824 | 3,881 | 2,082 | 0.000721 | 🔵 low — common in general English | — |
| 2522 | **arranged** | 1 | 7 | - | 852.58 | - | 1,622 | - | 0.000719 | 🟢 medium — moderately distinctive | — |
| 2523 | **closer** | 1 | 7 | - | 852.58 | - | 1,623 | - | 0.000719 | 🟢 medium — moderately distinctive | — |
| 2524 | **placed** | 1 | 8 | - | 843.14 | - | 1,627 | - | 0.000717 | 🟢 medium — moderately distinctive | — |
| 2525 | **several** | 1 | 11 | - | 841.46 | - | 1,628 | - | 0.000717 | 🟢 medium — moderately distinctive | — |
| 2526 | **miss** | 1 | 1 | - | 135.20 | 0.179528 | 7,245 | 1,666 | 0.000716 | 🔵 low — common in general English | — |
| 2527 | **hot metal** | 2 | 5 | 0.707 | - | 0.174667 | - | 1,630 | 0.000716 | - | — |
| 2528 | **supposed** | 1 | 6 | - | 841.09 | - | 1,631 | - | 0.000716 | 🟢 medium — moderately distinctive | — |
| 2529 | **rejecting** | 1 | 6 | - | 841.09 | - | 1,632 | - | 0.000715 | 🟢 medium — moderately distinctive | — |
| 2530 | **gardens** | 1 | - | - | - | 0.175720 | - | 1,637 | 0.000714 | - | — |
| 2531 | **shearing** | 1 | 5 | - | 831.24 | - | 1,638 | - | 0.000713 | 🟢 medium — moderately distinctive | — |
| 2532 | **piled** | 1 | 5 | - | 831.24 | - | 1,644 | - | 0.000711 | 🟢 medium — moderately distinctive | — |
| 2533 | **lit** | 1 | 5 | - | 831.24 | - | 1,645 | - | 0.000711 | 🟢 medium — moderately distinctive | — |
| 2534 | **boil** | 1 | 5 | - | 831.24 | - | 1,649 | - | 0.000710 | 🟢 medium — moderately distinctive | — |
| 2535 | **wasted** | 1 | 5 | - | 831.24 | - | 1,655 | - | 0.000707 | 🟢 medium — moderately distinctive | — |
| 2536 | **snake** | 1 | 5 | - | 831.24 | - | 1,656 | - | 0.000707 | 🟢 medium — moderately distinctive | — |
| 2537 | **sleeping** | 1 | 5 | - | 831.24 | - | 1,657 | - | 0.000707 | 🟢 medium — moderately distinctive | — |
| 2538 | **insult** | 1 | 5 | - | 831.24 | - | 1,658 | - | 0.000706 | 🟢 medium — moderately distinctive | — |
| 2539 | **shining** | 1 | 5 | - | 831.24 | - | 1,662 | - | 0.000705 | 🟢 medium — moderately distinctive | — |
| 2540 | **enlightened** | 1 | 5 | - | 830.96 | - | 1,664 | - | 0.000704 | 🟢 medium — moderately distinctive | — |
| 2541 | **misery** | 1 | 5 | - | 830.96 | - | 1,666 | - | 0.000704 | 🟢 medium — moderately distinctive | — |
| 2542 | **stain** | 1 | 5 | - | 830.96 | - | 1,668 | - | 0.000703 | 🟢 medium — moderately distinctive | — |
| 2543 | **dy** | 1 | 5 | - | 830.96 | - | 1,671 | - | 0.000702 | 🟢 medium — moderately distinctive | ~ |
| 2544 | **crying** | 1 | 5 | - | 830.96 | - | 1,678 | - | 0.000700 | 🟢 medium — moderately distinctive | — |
| 2545 | **reigned** | 1 | 5 | - | 830.96 | - | 1,679 | - | 0.000699 | 🟢 medium — moderately distinctive | — |
| 2546 | **meditator** | 1 | 5 | - | 830.96 | - | 1,686 | - | 0.000697 | 🟢 medium — moderately distinctive | — |
| 2547 | **ty** | 1 | 5 | - | 830.96 | - | 1,688 | - | 0.000696 | 🟢 medium — moderately distinctive | ~ |
| 2548 | **wearing** | 1 | 5 | - | 830.96 | - | 1,690 | - | 0.000696 | 🟢 medium — moderately distinctive | — |
| 2549 | **recited** | 1 | 5 | - | 830.96 | - | 1,694 | - | 0.000695 | 🟢 medium — moderately distinctive | — |
| 2550 | **flame** | 1 | 5 | - | 830.96 | - | 1,696 | - | 0.000694 | 🟢 medium — moderately distinctive | — |
| 2551 | **precipice** | 1 | 5 | - | 830.96 | - | 1,697 | - | 0.000694 | 🟢 medium — moderately distinctive | — |
| 2552 | **torture** | 1 | 1 | - | 166.19 | 0.231483 | 4,925 | 1,973 | 0.000692 | 🔵 low — common in general English | — |
| 2553 | **deserted** | 1 | 5 | - | 830.96 | - | 1,701 | - | 0.000692 | 🟢 medium — moderately distinctive | — |
| 2554 | **conduce** | 1 | 5 | - | 830.96 | - | 1,705 | - | 0.000691 | 🟢 medium — moderately distinctive | — |
| 2555 | **red-hot** | 1 | 5 | - | 830.96 | - | 1,707 | - | 0.000690 | 🟢 medium — moderately distinctive | — |
| 2556 | **breeze** | 1 | 1 | - | 166.19 | 0.224277 | 5,607 | 1,892 | 0.000689 | 🔵 low — common in general English | — |
| 2557 | **novice** | 1 | 5 | - | 830.96 | - | 1,715 | - | 0.000688 | 🟢 medium — moderately distinctive | ✓ དགེ་ཚུལ |
| 2558 | **confessing** | 1 | 5 | - | 830.96 | - | 1,717 | - | 0.000687 | 🟢 medium — moderately distinctive | — |
| 2559 | **evil-doer** | 1 | 5 | - | 830.96 | - | 1,719 | - | 0.000687 | 🟢 medium — moderately distinctive | — |
| 2560 | **boy** | 1 | 5 | - | 830.96 | - | 1,721 | - | 0.000686 | 🟢 medium — moderately distinctive | — |
| 2561 | **exchange** | 1 | 1 | - | 58.64 | 0.182281 | 7,630 | 1,740 | 0.000686 | 🔵 low — common in general English | — |
| 2562 | **song** | 1 | 5 | - | 830.96 | - | 1,722 | - | 0.000686 | 🟢 medium — moderately distinctive | ~ |
| 2563 | **circumambulating** | 1 | 5 | - | 830.96 | - | 1,725 | - | 0.000685 | 🟢 medium — moderately distinctive | — |
| 2564 | **resting** | 1 | 5 | - | 830.96 | - | 1,726 | - | 0.000684 | 🟢 medium — moderately distinctive | — |
| 2565 | **defiled** | 1 | 5 | - | 830.96 | - | 1,730 | - | 0.000683 | 🟢 medium — moderately distinctive | — |
| 2566 | **proliferating** | 1 | 5 | - | 830.96 | - | 1,731 | - | 0.000683 | 🟢 medium — moderately distinctive | — |
| 2567 | **ashamed** | 1 | 5 | - | 830.96 | - | 1,733 | - | 0.000682 | 🟢 medium — moderately distinctive | — |
| 2568 | **jewelled** | 1 | 5 | - | 830.96 | - | 1,739 | - | 0.000680 | 🟢 medium — moderately distinctive | — |
| 2569 | **canopy** | 1 | 5 | - | 830.96 | - | 1,741 | - | 0.000680 | 🟢 medium — moderately distinctive | ~ |
| 2570 | **lakini** | 1 | 5 | - | 830.96 | - | 1,742 | - | 0.000679 | 🟢 medium — moderately distinctive | — |
| 2571 | **bonpos** | 1 | - | - | - | 0.182284 | - | 1,742 | 0.000679 | - | — |
| 2572 | **obstacle-maker** | 1 | 5 | - | 830.96 | - | 1,746 | - | 0.000678 | 🟢 medium — moderately distinctive | — |
| 2573 | **neighbour** | 1 | 1 | - | 154.24 | 0.192017 | 6,940 | 1,814 | 0.000676 | 🔵 low — common in general English | — |
| 2574 | **non-dharma** | 1 | 5 | - | 830.96 | - | 1,754 | - | 0.000676 | 🟢 medium — moderately distinctive | — |
| 2575 | **declare** | 1 | 1 | - | 130.21 | 0.182648 | 7,314 | 1,792 | 0.000676 | 🔵 low — common in general English | — |
| 2576 | **dried** | 1 | 6 | - | 830.14 | - | 1,759 | - | 0.000674 | 🟢 medium — moderately distinctive | — |
| 2577 | **perceived** | 1 | 6 | - | 830.14 | - | 1,761 | - | 0.000674 | 🟢 medium — moderately distinctive | — |
| 2578 | **enjoyed** | 1 | 6 | - | 820.23 | - | 1,765 | - | 0.000672 | 🟢 medium — moderately distinctive | — |
| 2579 | **worked** | 1 | 7 | - | 820.04 | - | 1,768 | - | 0.000671 | 🟢 medium — moderately distinctive | — |
| 2580 | **course** | 1 | 8 | - | 818.56 | - | 1,769 | - | 0.000671 | 🟢 medium — moderately distinctive | — |
| 2581 | **passing** | 1 | 6 | - | 811.18 | - | 1,779 | - | 0.000668 | 🟢 medium — moderately distinctive | — |
| 2582 | **working** | 1 | 9 | - | 807.97 | - | 1,780 | - | 0.000668 | 🟢 medium — moderately distinctive | — |
| 2583 | **ordered** | 1 | 7 | - | 806.54 | - | 1,781 | - | 0.000668 | 🟢 medium — moderately distinctive | — |
| 2584 | **causing** | 1 | 7 | - | 806.54 | - | 1,782 | - | 0.000667 | 🟢 medium — moderately distinctive | — |
| 2585 | **asking** | 1 | 7 | - | 803.39 | - | 1,783 | - | 0.000667 | 🟢 medium — moderately distinctive | — |
| 2586 | **serving** | 1 | 6 | - | 802.86 | - | 1,785 | - | 0.000666 | 🟢 medium — moderately distinctive | — |
| 2587 | **compared** | 1 | 12 | - | 800.33 | - | 1,787 | - | 0.000666 | 🟢 medium — moderately distinctive | — |
| 2588 | **carrying** | 1 | 7 | - | 800.32 | - | 1,788 | - | 0.000666 | 🟢 medium — moderately distinctive | — |
| 2589 | **wrapped** | 1 | 5 | - | 796.10 | - | 1,795 | - | 0.000663 | 🟢 medium — moderately distinctive | — |
| 2590 | **sick person** | 2 | 5 | 0.483 | - | 0.183007 | - | 1,796 | 0.000663 | - | — |
| 2591 | **corps** | 1 | 5 | - | 796.10 | - | 1,797 | - | 0.000663 | 🟢 medium — moderately distinctive | — |
| 2592 | **dakini yeshe** | 2 | 3 | 0.859 | - | 0.186165 | - | 1,798 | 0.000663 | - | ~ |
| 2593 | **white syllable** | 2 | 3 | 0.539 | - | 0.188195 | - | 1,801 | 0.000662 | - | — |
| 2594 | **translator vairotsana** | 2 | 3 | 0.821 | - | 0.189318 | - | 1,805 | 0.000661 | - | — |
| 2595 | **studied** | 1 | 6 | - | 795.15 | - | 1,807 | - | 0.000660 | 🟢 medium — moderately distinctive | — |
| 2596 | **foundation stone** | 2 | 5 | 0.735 | - | 0.190253 | - | 1,808 | 0.000660 | - | — |
| 2597 | **fighting** | 1 | 6 | - | 787.98 | - | 1,813 | - | 0.000658 | 🟢 medium — moderately distinctive | ~ |
| 2598 | **calling** | 1 | 7 | - | 783.37 | - | 1,816 | - | 0.000657 | 🟢 medium — moderately distinctive | ~ |
| 2599 | **third** | 1 | 10 | - | 781.87 | - | 1,817 | - | 0.000657 | 🟢 medium — moderately distinctive | — |
| 2600 | **threatening** | 1 | 6 | - | 781.27 | - | 1,818 | - | 0.000657 | 🟢 medium — moderately distinctive | ~ |
| 2601 | **asuras** | 1 | - | - | - | 0.193279 | - | 1,818 | 0.000657 | - | — |
| 2602 | **linked** | 1 | 7 | - | 778.21 | - | 1,819 | - | 0.000657 | 🟢 medium — moderately distinctive | — |
| 2603 | **rude** | 1 | 1 | - | 166.19 | 0.238979 | 5,200 | 2,086 | 0.000656 | 🔵 low — common in general English | — |
| 2604 | **definitely** | 1 | 6 | - | 774.96 | - | 1,822 | - | 0.000656 | 🟢 medium — moderately distinctive | — |
| 2605 | **mine** | 1 | 8 | - | 771.91 | - | 1,823 | - | 0.000655 | 🟢 medium — moderately distinctive | — |
| 2606 | **everywhere** | 1 | 5 | - | 771.18 | - | 1,824 | - | 0.000655 | 🟢 medium — moderately distinctive | — |
| 2607 | **exclaim** | 1 | 1 | - | 166.19 | 0.231249 | 6,222 | 1,957 | 0.000655 | 🔵 low — common in general English | — |
| 2608 | **missing** | 1 | 5 | - | 771.18 | - | 1,826 | - | 0.000655 | 🟢 medium — moderately distinctive | — |
| 2609 | **beaten** | 1 | 5 | - | 771.18 | - | 1,831 | - | 0.000653 | 🟢 medium — moderately distinctive | — |
| 2610 | **lump** | 1 | 5 | - | 771.18 | - | 1,832 | - | 0.000653 | 🟢 medium — moderately distinctive | — |
| 2611 | **vajrasattvas** | 1 | - | - | - | 0.194327 | - | 1,832 | 0.000653 | - | — |
| 2612 | **undergoing** | 1 | 5 | - | 771.18 | - | 1,834 | - | 0.000652 | 🟢 medium — moderately distinctive | — |
| 2613 | **boot** | 1 | 5 | - | 771.18 | - | 1,835 | - | 0.000652 | 🟢 medium — moderately distinctive | — |
| 2614 | **tendzin chopel** | 2 | 3 | 0.952 | - | 0.195524 | - | 1,836 | 0.000652 | - | — |
| 2615 | **included** | 1 | 9 | - | 765.96 | - | 1,838 | - | 0.000651 | 🟢 medium — moderately distinctive | — |
| 2616 | **breaking** | 1 | 6 | - | 763.40 | - | 1,840 | - | 0.000651 | 🟢 medium — moderately distinctive | — |
| 2617 | **creating** | 1 | 6 | - | 758.06 | - | 1,842 | - | 0.000650 | 🟢 medium — moderately distinctive | — |
| 2618 | **alas** | 1 | - | - | - | 0.196368 | - | 1,842 | 0.000650 | - | — |
| 2619 | **wild animal** | 2 | 4 | 0.592 | - | 0.204942 | - | 1,845 | 0.000649 | - | — |
| 2620 | **completed** | 1 | 10 | - | 753.63 | - | 1,846 | - | 0.000649 | 🟢 medium — moderately distinctive | — |
| 2621 | **tied** | 1 | 6 | - | 752.99 | - | 1,848 | - | 0.000649 | 🟢 medium — moderately distinctive | — |
| 2622 | **achieve liberation** | 2 | 3 | 0.630 | - | 0.211136 | - | 1,848 | 0.000649 | - | — |
| 2623 | **listened** | 1 | 5 | - | 751.84 | - | 1,850 | - | 0.000648 | 🟢 medium — moderately distinctive | — |
| 2624 | **steadfastness** | 1 | 1 | - | 166.19 | 0.239102 | 5,436 | 2,087 | 0.000648 | 🔵 low — common in general English | — |
| 2625 | **vajras** | 1 | - | - | - | 0.214663 | - | 1,851 | 0.000648 | - | — |
| 2626 | **dragged** | 1 | 5 | - | 751.84 | - | 1,852 | - | 0.000647 | 🟢 medium — moderately distinctive | — |
| 2627 | **contaminated** | 1 | 5 | - | 751.84 | - | 1,855 | - | 0.000647 | 🟢 medium — moderately distinctive | — |
| 2628 | **sword** | 1 | 5 | - | 751.84 | - | 1,856 | - | 0.000646 | 🟢 medium — moderately distinctive | — |
| 2629 | **ala** | 1 | 5 | - | 751.84 | - | 1,857 | - | 0.000646 | 🟢 medium — moderately distinctive | — |
| 2630 | **devoted** | 1 | 5 | - | 751.84 | - | 1,858 | - | 0.000646 | 🟢 medium — moderately distinctive | — |
| 2631 | **selfish desire** | 2 | 4 | 0.660 | - | 0.217051 | - | 1,858 | 0.000646 | - | — |
| 2632 | **vast scale** | 2 | 3 | 0.756 | - | 0.217700 | - | 1,859 | 0.000645 | - | — |
| 2633 | **staying** | 1 | 5 | - | 751.84 | - | 1,860 | - | 0.000645 | 🟢 medium — moderately distinctive | — |
| 2634 | **stains** | 1 | - | - | - | 0.218896 | - | 1,860 | 0.000645 | - | — |
| 2635 | **setting** | 1 | 7 | - | 749.13 | - | 1,862 | - | 0.000645 | 🟢 medium — moderately distinctive | — |
| 2636 | **completing** | 1 | 6 | - | 748.15 | - | 1,863 | - | 0.000644 | 🟢 medium — moderately distinctive | — |
| 2637 | **crawl** | 1 | 1 | - | 159.22 | 0.231070 | 6,793 | 1,947 | 0.000644 | 🔵 low — common in general English | — |
| 2638 | **confused** | 1 | 5 | - | 736.04 | - | 1,869 | - | 0.000643 | 🟢 medium — moderately distinctive | — |
| 2639 | **throwing** | 1 | 5 | - | 736.04 | - | 1,871 | - | 0.000642 | 🟢 medium — moderately distinctive | — |
| 2640 | **surpass** | 1 | 5 | - | 736.04 | - | 1,873 | - | 0.000642 | 🟢 medium — moderately distinctive | — |
| 2641 | **wanting** | 1 | 5 | - | 736.04 | - | 1,874 | - | 0.000641 | 🟢 medium — moderately distinctive | — |
| 2642 | **times** | 1 | - | - | - | 0.221631 | - | 1,874 | 0.000641 | - | — |
| 2643 | **sympathetic joy** | 2 | 3 | 0.761 | - | 0.221733 | - | 1,875 | 0.000641 | - | — |
| 2644 | **illustrated** | 1 | 5 | - | 736.04 | - | 1,876 | - | 0.000641 | 🟢 medium — moderately distinctive | — |
| 2645 | **lowest** | 1 | 7 | - | 735.95 | - | 1,880 | - | 0.000640 | 🟢 medium — moderately distinctive | — |
| 2646 | **telling** | 1 | 6 | - | 734.86 | - | 1,881 | - | 0.000640 | 🟢 medium — moderately distinctive | — |
| 2647 | **attacked** | 1 | 6 | - | 730.78 | - | 1,884 | - | 0.000639 | 🟢 medium — moderately distinctive | — |
| 2648 | **appropriate** | 1 | 7 | - | 729.02 | - | 1,886 | - | 0.000638 | 🟢 medium — moderately distinctive | — |
| 2649 | **helping** | 1 | 6 | - | 726.86 | - | 1,887 | - | 0.000638 | 🟢 medium — moderately distinctive | — |
| 2650 | **pressing** | 1 | 6 | - | 726.86 | - | 1,888 | - | 0.000638 | 🟢 medium — moderately distinctive | — |
| 2651 | **abandoned** | 1 | 6 | - | 723.08 | - | 1,890 | - | 0.000637 | 🟢 medium — moderately distinctive | — |
| 2652 | **emanates** | 1 | - | - | - | 0.224294 | - | 1,893 | 0.000636 | - | — |
| 2653 | **exchanging** | 1 | 5 | - | 722.69 | - | 1,897 | - | 0.000635 | 🟢 medium — moderately distinctive | — |
| 2654 | **maker** | 1 | 7 | - | 719.31 | - | 1,898 | - | 0.000635 | 🟢 medium — moderately distinctive | — |
| 2655 | **forced** | 1 | 7 | - | 716.24 | - | 1,900 | - | 0.000635 | 🟢 medium — moderately distinctive | — |
| 2656 | **rub** | 1 | 1 | - | 166.19 | 0.231898 | 6,419 | 2,027 | 0.000634 | 🔵 low — common in general English | — |
| 2657 | **destroying** | 1 | 5 | - | 711.12 | - | 1,905 | - | 0.000633 | 🟢 medium — moderately distinctive | — |
| 2658 | **rite** | 1 | 5 | - | 711.12 | - | 1,907 | - | 0.000633 | 🟢 medium — moderately distinctive | — |
| 2659 | **wolf** | 1 | 1 | - | 154.24 | 0.231618 | 6,942 | 1,983 | 0.000632 | 🔵 low — common in general English | — |
| 2660 | **arose** | 1 | 5 | - | 711.12 | - | 1,909 | - | 0.000632 | 🟢 medium — moderately distinctive | — |
| 2661 | **reading** | 1 | 5 | - | 700.91 | - | 1,915 | - | 0.000631 | 🟢 medium — moderately distinctive | — |
| 2662 | **touched** | 1 | 5 | - | 700.91 | - | 1,916 | - | 0.000630 | 🟢 medium — moderately distinctive | — |
| 2663 | **sooner** | 1 | 5 | - | 691.78 | - | 1,919 | - | 0.000630 | 🟢 medium — moderately distinctive | — |
| 2664 | **accompanied** | 1 | 5 | - | 691.78 | - | 1,920 | - | 0.000629 | 🟢 medium — moderately distinctive | — |
| 2665 | **becoming** | 1 | 6 | - | 685.99 | - | 1,923 | - | 0.000629 | 🟢 medium — moderately distinctive | ✓ སྲིད་པ |
| 2666 | **below** | 1 | 9 | - | 684.14 | - | 1,924 | - | 0.000628 | 🟢 medium — moderately distinctive | — |
| 2667 | **host** | 1 | 5 | - | 683.52 | - | 1,925 | - | 0.000628 | 🟢 medium — moderately distinctive | — |
| 2668 | **presented** | 1 | 6 | - | 676.08 | - | 1,928 | - | 0.000627 | 🟢 medium — moderately distinctive | — |
| 2669 | **accordingly** | 1 | 5 | - | 675.98 | - | 1,929 | - | 0.000627 | 🟢 medium — moderately distinctive | — |
| 2670 | **criticized** | 1 | 5 | - | 675.98 | - | 1,930 | - | 0.000627 | 🟢 medium — moderately distinctive | — |
| 2671 | **hardly** | 1 | 5 | - | 669.05 | - | 1,932 | - | 0.000626 | 🟢 medium — moderately distinctive | — |
| 2672 | **render** | 1 | 4 | - | 664.99 | - | 1,940 | - | 0.000624 | 🟢 medium — moderately distinctive | — |
| 2673 | **breast** | 1 | 4 | - | 664.99 | - | 1,941 | - | 0.000624 | 🟢 medium — moderately distinctive | — |
| 2674 | **dissolving** | 1 | 4 | - | 664.99 | - | 1,942 | - | 0.000624 | 🟢 medium — moderately distinctive | — |
| 2675 | **landscape** | 1 | 4 | - | 664.99 | - | 1,946 | - | 0.000623 | 🟢 medium — moderately distinctive | — |
| 2676 | **cheat** | 1 | 4 | - | 664.99 | - | 1,947 | - | 0.000623 | 🟢 medium — moderately distinctive | — |
| 2677 | **wrinkle** | 1 | 4 | - | 664.99 | - | 1,950 | - | 0.000622 | 🟢 medium — moderately distinctive | — |
| 2678 | **multiply** | 1 | 4 | - | 664.99 | - | 1,953 | - | 0.000621 | 🟢 medium — moderately distinctive | — |
| 2679 | **inherited** | 1 | 4 | - | 664.99 | - | 1,961 | - | 0.000619 | 🟢 medium — moderately distinctive | — |
| 2680 | **insist** | 1 | 1 | - | 140.18 | 0.231806 | 7,193 | 2,018 | 0.000619 | 🔵 low — common in general English | — |
| 2681 | **whack** | 1 | 4 | - | 664.99 | - | 1,962 | - | 0.000619 | 🟢 medium — moderately distinctive | — |
| 2682 | **rubbing** | 1 | 4 | - | 664.99 | - | 1,964 | - | 0.000618 | 🟢 medium — moderately distinctive | — |
| 2683 | **wagon** | 1 | 4 | - | 664.99 | - | 1,965 | - | 0.000618 | 🟢 medium — moderately distinctive | — |
| 2684 | **ear** | 1 | 4 | - | 664.99 | - | 1,966 | - | 0.000618 | 🟢 medium — moderately distinctive | — |
| 2685 | **pleasing** | 1 | 4 | - | 664.99 | - | 1,968 | - | 0.000617 | 🟢 medium — moderately distinctive | — |
| 2686 | **defect** | 1 | 4 | - | 664.77 | - | 1,971 | - | 0.000617 | 🟢 medium — moderately distinctive | — |
| 2687 | **ence** | 1 | 4 | - | 664.77 | - | 1,974 | - | 0.000616 | 🟢 medium — moderately distinctive | — |
| 2688 | **embody** | 1 | 4 | - | 664.77 | - | 1,975 | - | 0.000616 | 🟢 medium — moderately distinctive | — |
| 2689 | **poisoned** | 1 | 4 | - | 664.77 | - | 1,977 | - | 0.000615 | 🟢 medium — moderately distinctive | — |
| 2690 | **blade** | 1 | 4 | - | 664.77 | - | 1,978 | - | 0.000615 | 🟢 medium — moderately distinctive | — |
| 2691 | **stag** | 1 | 4 | - | 664.77 | - | 1,979 | - | 0.000615 | 🟢 medium — moderately distinctive | — |
| 2692 | **bee** | 1 | 4 | - | 664.77 | - | 1,980 | - | 0.000615 | 🟢 medium — moderately distinctive | — |
| 2693 | **diseas** | 1 | 4 | - | 664.77 | - | 1,986 | - | 0.000613 | 🟢 medium — moderately distinctive | — |
| 2694 | **parasol** | 1 | 4 | - | 664.77 | - | 1,988 | - | 0.000613 | 🟢 medium — moderately distinctive | — |
| 2695 | **entrusted** | 1 | 4 | - | 664.77 | - | 1,989 | - | 0.000612 | 🟢 medium — moderately distinctive | — |
| 2696 | **prostitute** | 1 | 4 | - | 664.77 | - | 1,992 | - | 0.000612 | 🟢 medium — moderately distinctive | — |
| 2697 | **exclaimed** | 1 | 4 | - | 664.77 | - | 1,995 | - | 0.000611 | 🟢 medium — moderately distinctive | — |
| 2698 | **sion** | 1 | 4 | - | 664.77 | - | 1,996 | - | 0.000611 | 🟢 medium — moderately distinctive | — |
| 2699 | **wash** | 1 | 1 | - | 135.20 | 0.232066 | 7,264 | 2,051 | 0.000610 | 🔵 low — common in general English | — |
| 2700 | **renounced** | 1 | 4 | - | 664.77 | - | 1,999 | - | 0.000610 | 🟢 medium — moderately distinctive | — |
| 2701 | **play** | 1 | 1 | - | 117.67 | 0.231986 | 7,460 | 2,037 | 0.000610 | 🔵 low — common in general English | — |
| 2702 | **univers** | 1 | 4 | - | 664.77 | - | 2,001 | - | 0.000610 | 🟢 medium — moderately distinctive | — |
| 2703 | **footstep** | 1 | 4 | - | 664.77 | - | 2,005 | - | 0.000609 | 🟢 medium — moderately distinctive | — |
| 2704 | **evaporate** | 1 | 4 | - | 664.77 | - | 2,006 | - | 0.000608 | 🟢 medium — moderately distinctive | — |
| 2705 | **footprint** | 1 | 4 | - | 664.77 | - | 2,007 | - | 0.000608 | 🟢 medium — moderately distinctive | — |
| 2706 | **thirty-seven** | 1 | 4 | - | 664.77 | - | 2,010 | - | 0.000607 | 🟢 medium — moderately distinctive | — |
| 2707 | **gange** | 1 | 4 | - | 664.77 | - | 2,011 | - | 0.000607 | 🟢 medium — moderately distinctive | — |
| 2708 | **clenched** | 1 | 4 | - | 664.77 | - | 2,013 | - | 0.000607 | 🟢 medium — moderately distinctive | — |
| 2709 | **nest** | 1 | 4 | - | 664.77 | - | 2,015 | - | 0.000606 | 🟢 medium — moderately distinctive | — |
| 2710 | **asura** | 1 | 4 | - | 664.77 | - | 2,016 | - | 0.000606 | 🟢 medium — moderately distinctive | — |
| 2711 | **laugh** | 1 | 4 | - | 664.77 | - | 2,017 | - | 0.000606 | 🟢 medium — moderately distinctive | — |
| 2712 | **robber** | 1 | 4 | - | 664.77 | - | 2,019 | - | 0.000605 | 🟢 medium — moderately distinctive | — |
| 2713 | **nostrils** | 1 | - | - | - | 0.231865 | - | 2,021 | 0.000605 | - | — |
| 2714 | **gesh** | 1 | 4 | - | 664.77 | - | 2,022 | - | 0.000605 | 🟢 medium — moderately distinctive | — |
| 2715 | **sang** | 1 | 4 | - | 664.77 | - | 2,023 | - | 0.000604 | 🟢 medium — moderately distinctive | — |
| 2716 | **revered** | 1 | 4 | - | 664.77 | - | 2,027 | - | 0.000604 | 🟢 medium — moderately distinctive | — |
| 2717 | **ember** | 1 | 4 | - | 664.77 | - | 2,029 | - | 0.000603 | 🟢 medium — moderately distinctive | — |
| 2718 | **grabbed** | 1 | 4 | - | 664.77 | - | 2,031 | - | 0.000603 | 🟢 medium — moderately distinctive | — |
| 2719 | **crawling** | 1 | 4 | - | 664.77 | - | 2,032 | - | 0.000602 | 🟢 medium — moderately distinctive | — |
| 2720 | **thicket** | 1 | 4 | - | 664.77 | - | 2,033 | - | 0.000602 | 🟢 medium — moderately distinctive | — |
| 2721 | **embrace** | 1 | 4 | - | 664.77 | - | 2,035 | - | 0.000602 | 🟢 medium — moderately distinctive | — |
| 2722 | **selve** | 1 | 4 | - | 664.77 | - | 2,040 | - | 0.000601 | 🟢 medium — moderately distinctive | — |
| 2723 | **heir** | 1 | 4 | - | 664.77 | - | 2,044 | - | 0.000600 | 🟢 medium — moderately distinctive | — |
| 2724 | **shine** | 1 | 4 | - | 664.77 | - | 2,045 | - | 0.000599 | 🟢 medium — moderately distinctive | — |
| 2725 | **tortured** | 1 | 4 | - | 664.77 | - | 2,047 | - | 0.000599 | 🟢 medium — moderately distinctive | — |
| 2726 | **terrified** | 1 | 4 | - | 664.77 | - | 2,049 | - | 0.000599 | 🟢 medium — moderately distinctive | — |
| 2727 | **adversary** | 1 | 4 | - | 664.77 | - | 2,051 | - | 0.000598 | 🟢 medium — moderately distinctive | — |
| 2728 | **wolve** | 1 | 4 | - | 664.77 | - | 2,052 | - | 0.000598 | 🟢 medium — moderately distinctive | — |
| 2729 | **knot** | 1 | 4 | - | 664.77 | - | 2,053 | - | 0.000598 | 🟢 medium — moderately distinctive | — |
| 2730 | **smiling** | 1 | 4 | - | 664.77 | - | 2,056 | - | 0.000597 | 🟢 medium — moderately distinctive | — |
| 2731 | **obeyed** | 1 | 4 | - | 664.77 | - | 2,058 | - | 0.000597 | 🟢 medium — moderately distinctive | — |
| 2732 | **wouldn** | 1 | 4 | - | 664.77 | - | 2,059 | - | 0.000596 | 🟢 medium — moderately distinctive | — |
| 2733 | **innocent** | 1 | 4 | - | 664.77 | - | 2,060 | - | 0.000596 | 🟢 medium — moderately distinctive | — |
| 2734 | **ogre** | 1 | 4 | - | 664.77 | - | 2,061 | - | 0.000596 | 🟢 medium — moderately distinctive | — |
| 2735 | **transgression** | 1 | 4 | - | 664.77 | - | 2,062 | - | 0.000596 | 🟢 medium — moderately distinctive | — |
| 2736 | **amassed** | 1 | 4 | - | 664.77 | - | 2,063 | - | 0.000595 | 🟢 medium — moderately distinctive | — |
| 2737 | **pebble** | 1 | 4 | - | 664.77 | - | 2,068 | - | 0.000594 | 🟢 medium — moderately distinctive | — |
| 2738 | **emulating** | 1 | 4 | - | 664.77 | - | 2,070 | - | 0.000594 | 🟢 medium — moderately distinctive | — |
| 2739 | **versed** | 1 | 4 | - | 664.77 | - | 2,071 | - | 0.000594 | 🟢 medium — moderately distinctive | — |
| 2740 | **characteristic** | 1 | 4 | - | 664.77 | - | 2,072 | - | 0.000593 | 🟢 medium — moderately distinctive | — |
| 2741 | **adept** | 1 | 4 | - | 664.77 | - | 2,077 | - | 0.000592 | 🟢 medium — moderately distinctive | — |
| 2742 | **empow** | 1 | 4 | - | 664.77 | - | 2,079 | - | 0.000592 | 🟢 medium — moderately distinctive | — |
| 2743 | **conferred** | 1 | 4 | - | 664.77 | - | 2,081 | - | 0.000591 | 🟢 medium — moderately distinctive | — |
| 2744 | **unbearable pain** | 2 | 3 | 0.587 | - | 0.235483 | - | 2,083 | 0.000591 | - | — |
| 2745 | **branch visualize** | 2 | 3 | 0.552 | - | 0.236882 | - | 2,085 | 0.000591 | - | — |
| 2746 | **outward sign** | 2 | 3 | 0.650 | - | 0.248102 | - | 2,089 | 0.000590 | - | — |
| 2747 | **nostril** | 1 | 4 | - | 664.77 | - | 2,091 | - | 0.000589 | 🟢 medium — moderately distinctive | — |
| 2748 | **mandalas** | 1 | - | - | - | 0.253658 | - | 2,093 | 0.000589 | - | — |
| 2749 | **beginner** | 1 | 4 | - | 664.77 | - | 2,096 | - | 0.000588 | 🟢 medium — moderately distinctive | — |
| 2750 | **awaken** | 1 | 4 | - | 664.77 | - | 2,097 | - | 0.000588 | 🟢 medium — moderately distinctive | — |
| 2751 | **ego-clinging** | 1 | 4 | - | 664.77 | - | 2,104 | - | 0.000587 | 🟢 medium — moderately distinctive | — |
| 2752 | **ordinary outer** | 2 | 3 | 0.460 | - | 0.260241 | - | 2,104 | 0.000587 | - | ~ |
| 2753 | **cleansed** | 1 | 4 | - | 664.77 | - | 2,105 | - | 0.000586 | 🟢 medium — moderately distinctive | — |
| 2754 | **imagining** | 1 | 4 | - | 664.77 | - | 2,106 | - | 0.000586 | 🟢 medium — moderately distinctive | — |
| 2755 | **perceiving** | 1 | 4 | - | 664.77 | - | 2,110 | - | 0.000585 | 🟢 medium — moderately distinctive | — |
| 2756 | **syllable hrih** | 2 | 3 | 0.718 | - | 0.261964 | - | 2,110 | 0.000585 | - | — |
| 2757 | **worn** | 1 | 4 | - | 664.77 | - | 2,111 | - | 0.000585 | 🟢 medium — moderately distinctive | — |
| 2758 | **take pleasure** | 2 | 4 | 0.470 | - | 0.265872 | - | 2,111 | 0.000585 | - | — |
| 2759 | **speck** | 1 | 4 | - | 664.77 | - | 2,112 | - | 0.000585 | 🟢 medium — moderately distinctive | — |
| 2760 | **yidams** | 1 | - | - | - | 0.273972 | - | 2,113 | 0.000585 | - | — |
| 2761 | **curved** | 1 | 4 | - | 664.77 | - | 2,114 | - | 0.000584 | 🟢 medium — moderately distinctive | — |
| 2762 | **beggar woman** | 2 | 3 | 0.607 | - | 0.275925 | - | 2,114 | 0.000584 | - | — |
| 2763 | **direct empowerment** | 2 | 3 | 0.639 | - | 0.275993 | - | 2,115 | 0.000584 | - | — |
| 2764 | **karmapas** | 1 | - | - | - | 0.277592 | - | 2,116 | 0.000584 | - | — |
| 2765 | **machik labdron** | 2 | 3 | 0.952 | - | 0.278144 | - | 2,117 | 0.000584 | - | ✓ མ་ཅིག་ལབ་སྒྲོན |
| 2766 | **nagas** | 1 | - | - | - | 0.287085 | - | 2,119 | 0.000583 | - | — |
| 2767 | **lightly small** | 2 | 4 | 0.785 | - | 0.287373 | - | 2,120 | 0.000583 | - | — |
| 2768 | **natural expression** | 2 | 3 | 0.668 | - | 0.298469 | - | 2,125 | 0.000582 | - | ~ |
| 2769 | **explanation** | 1 | 5 | - | 662.63 | - | 2,126 | - | 0.000582 | 🟢 medium — moderately distinctive | — |
| 2770 | **won** | 1 | 6 | - | 658.71 | - | 2,130 | - | 0.000581 | 🟢 medium — moderately distinctive | — |
| 2771 | **consisting** | 1 | 5 | - | 656.65 | - | 2,132 | - | 0.000581 | 🟢 medium — moderately distinctive | — |
| 2772 | **lasting** | 1 | 5 | - | 656.65 | - | 2,133 | - | 0.000580 | 🟢 medium — moderately distinctive | — |
| 2773 | **watching** | 1 | 5 | - | 656.65 | - | 2,134 | - | 0.000580 | 🟢 medium — moderately distinctive | — |
| 2774 | **directed** | 1 | 5 | - | 656.65 | - | 2,135 | - | 0.000580 | 🟢 medium — moderately distinctive | — |
| 2775 | **spoke** | 1 | 5 | - | 651.05 | - | 2,137 | - | 0.000580 | 🟢 medium — moderately distinctive | — |
| 2776 | **reached** | 1 | 8 | - | 645.37 | - | 2,141 | - | 0.000579 | 🟢 medium — moderately distinctive | — |
| 2777 | **related** | 1 | 7 | - | 640.79 | - | 2,145 | - | 0.000578 | 🟢 medium — moderately distinctive | — |
| 2778 | **almost** | 1 | 7 | - | 639.18 | - | 2,146 | - | 0.000578 | 🟢 medium — moderately distinctive | ~ |
| 2779 | **running** | 1 | 6 | - | 637.12 | - | 2,147 | - | 0.000577 | 🟢 medium — moderately distinctive | — |
| 2780 | **middling** | 1 | 4 | - | 636.88 | - | 2,148 | - | 0.000577 | 🟢 medium — moderately distinctive | — |
| 2781 | **swallowed** | 1 | 4 | - | 636.88 | - | 2,149 | - | 0.000577 | 🟢 medium — moderately distinctive | — |
| 2782 | **swamp** | 1 | 4 | - | 636.88 | - | 2,150 | - | 0.000577 | 🟢 medium — moderately distinctive | — |
| 2783 | **deprived** | 1 | 4 | - | 636.88 | - | 2,153 | - | 0.000576 | 🟢 medium — moderately distinctive | — |
| 2784 | **deserve** | 1 | 4 | - | 636.88 | - | 2,158 | - | 0.000575 | 🟢 medium — moderately distinctive | — |
| 2785 | **spear** | 1 | 4 | - | 636.88 | - | 2,159 | - | 0.000575 | 🟢 medium — moderately distinctive | — |
| 2786 | **epidemic** | 1 | 4 | - | 636.88 | - | 2,160 | - | 0.000575 | 🟢 medium — moderately distinctive | — |
| 2787 | **separated** | 1 | 4 | - | 636.88 | - | 2,161 | - | 0.000575 | 🟢 medium — moderately distinctive | — |
| 2788 | **writing** | 1 | 5 | - | 636.16 | - | 2,169 | - | 0.000573 | 🟢 medium — moderately distinctive | — |
| 2789 | **protecting** | 1 | 5 | - | 636.16 | - | 2,170 | - | 0.000573 | 🟢 medium — moderately distinctive | — |
| 2790 | **heading** | 1 | 5 | - | 636.16 | - | 2,171 | - | 0.000573 | 🟢 medium — moderately distinctive | — |
| 2791 | **merely** | 1 | 5 | - | 636.16 | - | 2,172 | - | 0.000572 | 🟢 medium — moderately distinctive | — |
| 2792 | **pleased** | 1 | 5 | - | 631.72 | - | 2,180 | - | 0.000571 | 🟢 medium — moderately distinctive | — |
| 2793 | **developed** | 1 | 6 | - | 630.82 | - | 2,181 | - | 0.000571 | 🟢 medium — moderately distinctive | — |
| 2794 | **resource** | 1 | 5 | - | 623.46 | - | 2,187 | - | 0.000569 | 🟢 medium — moderately distinctive | — |
| 2795 | **hoping** | 1 | 5 | - | 619.61 | - | 2,188 | - | 0.000569 | 🟢 medium — moderately distinctive | — |
| 2796 | **counting** | 1 | 4 | - | 616.94 | - | 2,191 | - | 0.000569 | 🟢 medium — moderately distinctive | — |
| 2797 | **recipient** | 1 | 4 | - | 616.94 | - | 2,194 | - | 0.000568 | 🟢 medium — moderately distinctive | — |
| 2798 | **hook** | 1 | 4 | - | 616.94 | - | 2,195 | - | 0.000568 | 🟢 medium — moderately distinctive | — |
| 2799 | **condemned** | 1 | 4 | - | 616.94 | - | 2,196 | - | 0.000568 | 🟢 medium — moderately distinctive | — |
| 2800 | **sat** | 1 | 4 | - | 616.94 | - | 2,199 | - | 0.000567 | 🟢 medium — moderately distinctive | — |
| 2801 | **tower** | 1 | 4 | - | 616.94 | - | 2,200 | - | 0.000567 | 🟢 medium — moderately distinctive | — |
| 2802 | **obtaining** | 1 | 5 | - | 615.92 | - | 2,202 | - | 0.000566 | 🟢 medium — moderately distinctive | — |
| 2803 | **determined** | 1 | 6 | - | 612.63 | - | 2,203 | - | 0.000566 | 🟢 medium — moderately distinctive | — |
| 2804 | **protected** | 1 | 5 | - | 608.99 | - | 2,207 | - | 0.000566 | 🟢 medium — moderately distinctive | — |
| 2805 | **pick** | 1 | 5 | - | 605.72 | - | 2,209 | - | 0.000565 | 🟢 medium — moderately distinctive | — |
| 2806 | **leading** | 1 | 7 | - | 605.08 | - | 2,212 | - | 0.000565 | 🟢 medium — moderately distinctive | — |
| 2807 | **corresponding** | 1 | 5 | - | 602.56 | - | 2,213 | - | 0.000564 | 🟢 medium — moderately distinctive | — |
| 2808 | **motivated** | 1 | 4 | - | 601.47 | - | 2,215 | - | 0.000564 | 🟢 medium — moderately distinctive | — |
| 2809 | **notion** | 1 | 4 | - | 601.47 | - | 2,216 | - | 0.000564 | 🟢 medium — moderately distinctive | — |
| 2810 | **arriving** | 1 | 4 | - | 601.47 | - | 2,218 | - | 0.000563 | 🟢 medium — moderately distinctive | — |
| 2811 | **breathing** | 1 | 4 | - | 601.47 | - | 2,221 | - | 0.000563 | 🟢 medium — moderately distinctive | — |
| 2812 | **casting** | 1 | 4 | - | 601.47 | - | 2,222 | - | 0.000563 | 🟢 medium — moderately distinctive | — |
| 2813 | **pearl** | 1 | 4 | - | 601.47 | - | 2,223 | - | 0.000562 | 🟢 medium — moderately distinctive | — |
| 2814 | **washed** | 1 | 4 | - | 601.47 | - | 2,224 | - | 0.000562 | 🟢 medium — moderately distinctive | — |
| 2815 | **drawn** | 1 | 5 | - | 599.52 | - | 2,227 | - | 0.000562 | 🟢 medium — moderately distinctive | — |
| 2816 | **facing** | 1 | 5 | - | 593.75 | - | 2,233 | - | 0.000561 | 🟢 medium — moderately distinctive | — |
| 2817 | **held** | 1 | 8 | - | 591.67 | - | 2,234 | - | 0.000560 | 🟢 medium — moderately distinctive | — |
| 2818 | **lamb** | 1 | 4 | - | 588.83 | - | 2,240 | - | 0.000559 | 🟢 medium — moderately distinctive | — |
| 2819 | **character** | 1 | 4 | - | 588.83 | - | 2,241 | - | 0.000559 | 🟢 medium — moderately distinctive | — |
| 2820 | **delighted** | 1 | 4 | - | 588.83 | - | 2,242 | - | 0.000559 | 🟢 medium — moderately distinctive | — |
| 2821 | **filling** | 1 | 4 | - | 588.83 | - | 2,243 | - | 0.000559 | 🟢 medium — moderately distinctive | — |
| 2822 | **easier** | 1 | 5 | - | 580.79 | - | 2,249 | - | 0.000557 | 🟢 medium — moderately distinctive | — |
| 2823 | **drawing** | 1 | 5 | - | 578.41 | - | 2,252 | - | 0.000557 | 🟢 medium — moderately distinctive | — |
| 2824 | **province** | 1 | 5 | - | 578.41 | - | 2,253 | - | 0.000557 | 🟢 medium — moderately distinctive | — |
| 2825 | **consequence** | 1 | 4 | - | 578.15 | - | 2,255 | - | 0.000556 | 🟢 medium — moderately distinctive | — |
| 2826 | **achievement** | 1 | 4 | - | 578.15 | - | 2,258 | - | 0.000556 | 🟢 medium — moderately distinctive | — |
| 2827 | **expressing** | 1 | 4 | - | 578.15 | - | 2,260 | - | 0.000555 | 🟢 medium — moderately distinctive | — |
| 2828 | **valley** | 1 | 5 | - | 576.10 | - | 2,261 | - | 0.000555 | 🟢 medium — moderately distinctive | — |
| 2829 | **ignore** | 1 | 4 | - | 568.89 | - | 2,267 | - | 0.000554 | 🟢 medium — moderately distinctive | — |
| 2830 | **ita** | 1 | 4 | - | 568.89 | - | 2,269 | - | 0.000554 | 🟢 medium — moderately distinctive | — |
| 2831 | **retreat** | 1 | 4 | - | 568.89 | - | 2,270 | - | 0.000554 | 🟢 medium — moderately distinctive | — |
| 2832 | **studying** | 1 | 5 | - | 565.39 | - | 2,272 | - | 0.000553 | 🟢 medium — moderately distinctive | — |
| 2833 | **stopped** | 1 | 5 | - | 561.45 | - | 2,275 | - | 0.000553 | 🟢 medium — moderately distinctive | — |
| 2834 | **discouraged** | 1 | 4 | - | 560.73 | - | 2,276 | - | 0.000552 | 🟢 medium — moderately distinctive | — |
| 2835 | **anywhere** | 1 | 4 | - | 560.73 | - | 2,278 | - | 0.000552 | 🟢 medium — moderately distinctive | — |
| 2836 | **hammer** | 1 | 4 | - | 560.73 | - | 2,279 | - | 0.000552 | 🟢 medium — moderately distinctive | — |
| 2837 | **destined** | 1 | 4 | - | 560.73 | - | 2,280 | - | 0.000552 | 🟢 medium — moderately distinctive | — |
| 2838 | **playing** | 1 | 4 | - | 560.73 | - | 2,282 | - | 0.000551 | 🟢 medium — moderately distinctive | — |
| 2839 | **performing** | 1 | 4 | - | 560.73 | - | 2,283 | - | 0.000551 | 🟢 medium — moderately distinctive | — |
| 2840 | **spreading** | 1 | 4 | - | 560.73 | - | 2,284 | - | 0.000551 | 🟢 medium — moderately distinctive | — |
| 2841 | **shown** | 1 | 5 | - | 559.55 | - | 2,286 | - | 0.000551 | 🟢 medium — moderately distinctive | — |
| 2842 | **pushed** | 1 | 5 | - | 559.55 | - | 2,287 | - | 0.000550 | 🟢 medium — moderately distinctive | — |
| 2843 | **shot** | 1 | 4 | - | 553.42 | - | 2,291 | - | 0.000550 | 🟢 medium — moderately distinctive | — |
| 2844 | **relying** | 1 | 4 | - | 546.82 | - | 2,297 | - | 0.000549 | 🟢 medium — moderately distinctive | — |
| 2845 | **undertaking** | 1 | 4 | - | 546.82 | - | 2,299 | - | 0.000548 | 🟢 medium — moderately distinctive | — |
| 2846 | **visiting** | 1 | 4 | - | 546.82 | - | 2,300 | - | 0.000548 | 🟢 medium — moderately distinctive | — |
| 2847 | **provoke** | 1 | 4 | - | 546.82 | - | 2,301 | - | 0.000548 | 🟢 medium — moderately distinctive | — |
| 2848 | **demanding** | 1 | 4 | - | 546.82 | - | 2,302 | - | 0.000548 | 🟢 medium — moderately distinctive | — |
| 2849 | **undertake** | 1 | 4 | - | 546.82 | - | 2,303 | - | 0.000548 | 🟢 medium — moderately distinctive | — |
| 2850 | **saved** | 1 | 4 | - | 546.82 | - | 2,304 | - | 0.000547 | 🟢 medium — moderately distinctive | — |
| 2851 | **insisted** | 1 | 4 | - | 546.82 | - | 2,305 | - | 0.000547 | 🟢 medium — moderately distinctive | — |
| 2852 | **produced** | 1 | 6 | - | 545.82 | - | 2,307 | - | 0.000547 | 🟢 medium — moderately distinctive | — |
| 2853 | **movement** | 1 | 5 | - | 542.50 | - | 2,308 | - | 0.000547 | 🟢 medium — moderately distinctive | ~ |
| 2854 | **conflicting** | 1 | 4 | - | 540.79 | - | 2,309 | - | 0.000547 | 🟢 medium — moderately distinctive | — |
| 2855 | **neighbouring** | 1 | 4 | - | 540.79 | - | 2,310 | - | 0.000546 | 🟢 medium — moderately distinctive | — |
| 2856 | **fraud** | 1 | 4 | - | 535.24 | - | 2,315 | - | 0.000545 | 🟢 medium — moderately distinctive | — |
| 2857 | **extreme** | 1 | 4 | - | 530.10 | - | 2,317 | - | 0.000545 | 🟢 medium — moderately distinctive | — |
| 2858 | **happening** | 1 | 4 | - | 530.10 | - | 2,318 | - | 0.000545 | 🟢 medium — moderately distinctive | — |
| 2859 | **achieving** | 1 | 4 | - | 530.10 | - | 2,319 | - | 0.000545 | 🟢 medium — moderately distinctive | — |
| 2860 | **avoiding** | 1 | 4 | - | 530.10 | - | 2,320 | - | 0.000545 | 🟢 medium — moderately distinctive | — |
| 2861 | **useful** | 1 | 4 | - | 525.32 | - | 2,325 | - | 0.000544 | 🟢 medium — moderately distinctive | — |
| 2862 | **regardless** | 1 | 4 | - | 525.32 | - | 2,326 | - | 0.000544 | 🟢 medium — moderately distinctive | — |
| 2863 | **relation** | 1 | 4 | - | 520.84 | - | 2,331 | - | 0.000543 | 🟢 medium — moderately distinctive | — |
| 2864 | **connected** | 1 | 4 | - | 520.84 | - | 2,332 | - | 0.000542 | 🟢 medium — moderately distinctive | — |
| 2865 | **ought** | 1 | 4 | - | 520.84 | - | 2,333 | - | 0.000542 | 🟢 medium — moderately distinctive | — |
| 2866 | **laid** | 1 | 4 | - | 516.64 | - | 2,338 | - | 0.000541 | 🟢 medium — moderately distinctive | — |
| 2867 | **acquired** | 1 | 7 | - | 514.79 | - | 2,342 | - | 0.000541 | 🟢 medium — moderately distinctive | — |
| 2868 | **yes** | 1 | 4 | - | 512.68 | - | 2,343 | - | 0.000541 | 🟢 medium — moderately distinctive | — |
| 2869 | **repair** | 1 | 4 | - | 512.68 | - | 2,347 | - | 0.000540 | 🟢 medium — moderately distinctive | — |
| 2870 | **associated** | 1 | 5 | - | 510.52 | - | 2,348 | - | 0.000540 | 🟢 medium — moderately distinctive | — |
| 2871 | **require** | 1 | 5 | - | 509.46 | - | 2,349 | - | 0.000540 | 🟢 medium — moderately distinctive | — |
| 2872 | **spell** | 1 | 4 | - | 508.93 | - | 2,351 | - | 0.000539 | 🟢 medium — moderately distinctive | — |
| 2873 | **plunged** | 1 | 4 | - | 505.38 | - | 2,352 | - | 0.000539 | 🟢 medium — moderately distinctive | — |
| 2874 | **couple** | 1 | 4 | - | 501.99 | - | 2,355 | - | 0.000538 | 🟢 medium — moderately distinctive | — |
| 2875 | **your** | 1 | 4 | - | 501.99 | - | 2,356 | - | 0.000538 | 🟢 medium — moderately distinctive | — |
| 2876 | **irreversible** | 1 | 3 | - | 498.74 | - | 2,360 | - | 0.000538 | 🔵 low — common in general English | — |
| 2877 | **inclination** | 1 | 3 | - | 498.74 | - | 2,361 | - | 0.000537 | 🔵 low — common in general English | — |
| 2878 | **shelter** | 1 | 3 | - | 498.74 | - | 2,362 | - | 0.000537 | 🔵 low — common in general English | — |
| 2879 | **sixty** | 1 | 3 | - | 498.74 | - | 2,363 | - | 0.000537 | 🔵 low — common in general English | — |
| 2880 | **wooden** | 1 | 3 | - | 498.74 | - | 2,364 | - | 0.000537 | 🔵 low — common in general English | — |
| 2881 | **tossed** | 1 | 3 | - | 498.74 | - | 2,365 | - | 0.000537 | 🔵 low — common in general English | — |
| 2882 | **armoured** | 1 | 3 | - | 498.74 | - | 2,366 | - | 0.000537 | 🔵 low — common in general English | — |
| 2883 | **pierce** | 1 | 3 | - | 498.74 | - | 2,367 | - | 0.000536 | 🔵 low — common in general English | — |
| 2884 | **envy** | 1 | 3 | - | 498.74 | - | 2,368 | - | 0.000536 | 🔵 low — common in general English | — |
| 2885 | **folk** | 1 | 3 | - | 498.74 | - | 2,369 | - | 0.000536 | 🔵 low — common in general English | — |
| 2886 | **cas** | 1 | 3 | - | 498.74 | - | 2,370 | - | 0.000536 | 🔵 low — common in general English | — |
| 2887 | **uncomfortable** | 1 | 3 | - | 498.74 | - | 2,371 | - | 0.000536 | 🔵 low — common in general English | — |
| 2888 | **spoiled** | 1 | 3 | - | 498.74 | - | 2,372 | - | 0.000536 | 🔵 low — common in general English | — |
| 2889 | **talent** | 1 | 3 | - | 498.74 | - | 2,373 | - | 0.000535 | 🔵 low — common in general English | — |
| 2890 | **piling** | 1 | 3 | - | 498.74 | - | 2,374 | - | 0.000535 | 🔵 low — common in general English | — |
| 2891 | **glory** | 1 | 3 | - | 498.74 | - | 2,375 | - | 0.000535 | 🔵 low — common in general English | — |
| 2892 | **fearing** | 1 | 3 | - | 498.74 | - | 2,376 | - | 0.000535 | 🔵 low — common in general English | — |
| 2893 | **tiger** | 1 | 3 | - | 498.74 | - | 2,377 | - | 0.000535 | 🔵 low — common in general English | — |
| 2894 | **stir** | 1 | 3 | - | 498.74 | - | 2,378 | - | 0.000535 | 🔵 low — common in general English | — |
| 2895 | **organ** | 1 | 3 | - | 498.74 | - | 2,379 | - | 0.000534 | 🔵 low — common in general English | — |
| 2896 | **whipped** | 1 | 3 | - | 498.74 | - | 2,380 | - | 0.000534 | 🔵 low — common in general English | — |
| 2897 | **cultivated** | 1 | 3 | - | 498.74 | - | 2,381 | - | 0.000534 | 🔵 low — common in general English | — |
| 2898 | **drowned** | 1 | 3 | - | 498.74 | - | 2,382 | - | 0.000534 | 🔵 low — common in general English | — |
| 2899 | **correctly** | 1 | 3 | - | 498.74 | - | 2,383 | - | 0.000534 | 🔵 low — common in general English | — |
| 2900 | **monster** | 1 | 3 | - | 498.74 | - | 2,384 | - | 0.000534 | 🔵 low — common in general English | — |
| 2901 | **sur** | 1 | 3 | - | 498.74 | - | 2,385 | - | 0.000533 | 🔵 low — common in general English | — |
| 2902 | **healed** | 1 | 3 | - | 498.74 | - | 2,386 | - | 0.000533 | 🔵 low — common in general English | — |
| 2903 | **stealing** | 1 | 3 | - | 498.74 | - | 2,388 | - | 0.000533 | 🔵 low — common in general English | — |
| 2904 | **tail** | 1 | 3 | - | 498.74 | - | 2,389 | - | 0.000533 | 🔵 low — common in general English | — |
| 2905 | **mixing** | 1 | 3 | - | 498.74 | - | 2,390 | - | 0.000533 | 🔵 low — common in general English | — |
| 2906 | **pair** | 1 | 3 | - | 498.74 | - | 2,391 | - | 0.000532 | 🔵 low — common in general English | — |
| 2907 | **elder** | 1 | 3 | - | 498.74 | - | 2,392 | - | 0.000532 | 🔵 low — common in general English | — |
| 2908 | **handful** | 1 | 3 | - | 498.74 | - | 2,393 | - | 0.000532 | 🔵 low — common in general English | — |
| 2909 | **steadfast** | 1 | 3 | - | 498.74 | - | 2,394 | - | 0.000532 | 🔵 low — common in general English | — |
| 2910 | **tired** | 1 | 3 | - | 498.74 | - | 2,395 | - | 0.000532 | 🔵 low — common in general English | — |
| 2911 | **furious** | 1 | 3 | - | 498.74 | - | 2,396 | - | 0.000532 | 🔵 low — common in general English | — |
| 2912 | **meth** | 1 | 3 | - | 498.74 | - | 2,397 | - | 0.000531 | 🔵 low — common in general English | — |
| 2913 | **robbed** | 1 | 3 | - | 498.74 | - | 2,398 | - | 0.000531 | 🔵 low — common in general English | — |
| 2914 | **elaboration** | 1 | 3 | - | 498.74 | - | 2,399 | - | 0.000531 | 🔵 low — common in general English | — |
| 2915 | **chased** | 1 | 3 | - | 498.74 | - | 2,400 | - | 0.000531 | 🔵 low — common in general English | — |
| 2916 | **saddle** | 1 | 3 | - | 498.74 | - | 2,401 | - | 0.000531 | 🔵 low — common in general English | — |
| 2917 | **crippled** | 1 | 3 | - | 498.74 | - | 2,402 | - | 0.000531 | 🔵 low — common in general English | — |
| 2918 | **plausible** | 1 | 3 | - | 498.74 | - | 2,403 | - | 0.000530 | 🔵 low — common in general English | — |
| 2919 | **myriad** | 1 | 3 | - | 498.74 | - | 2,404 | - | 0.000530 | 🔵 low — common in general English | — |
| 2920 | **hero** | 1 | 3 | - | 498.74 | - | 2,405 | - | 0.000530 | 🔵 low — common in general English | — |
| 2921 | **misfortune** | 1 | 3 | - | 498.74 | - | 2,406 | - | 0.000530 | 🔵 low — common in general English | — |
| 2922 | **dispense** | 1 | 3 | - | 498.74 | - | 2,407 | - | 0.000530 | 🔵 low — common in general English | — |
| 2923 | **unaltered** | 1 | 3 | - | 498.74 | - | 2,408 | - | 0.000530 | 🔵 low — common in general English | ✓ མ་བཅོས་པ |
| 2924 | **petal** | 1 | 3 | - | 498.74 | - | 2,409 | - | 0.000529 | 🔵 low — common in general English | — |
| 2925 | **dancing** | 1 | 3 | - | 498.74 | - | 2,410 | - | 0.000529 | 🔵 low — common in general English | — |
| 2926 | **quintessential** | 1 | 3 | - | 498.58 | - | 2,412 | - | 0.000529 | 🔵 low — common in general English | — |
| 2927 | **copper-coloured** | 1 | 3 | - | 498.58 | - | 2,413 | - | 0.000529 | 🔵 low — common in general English | — |
| 2928 | **pore** | 1 | 3 | - | 498.58 | - | 2,415 | - | 0.000528 | 🔵 low — common in general English | — |
| 2929 | **gossip** | 1 | 3 | - | 498.58 | - | 2,416 | - | 0.000528 | 🔵 low — common in general English | — |
| 2930 | **prac** | 1 | 3 | - | 498.58 | - | 2,417 | - | 0.000528 | 🔵 low — common in general English | — |
| 2931 | **contempt** | 1 | 3 | - | 498.58 | - | 2,418 | - | 0.000528 | 🔵 low — common in general English | — |
| 2932 | **flaming** | 1 | 3 | - | 498.58 | - | 2,419 | - | 0.000528 | 🔵 low — common in general English | — |
| 2933 | **inferno** | 1 | 3 | - | 498.58 | - | 2,420 | - | 0.000528 | 🔵 low — common in general English | — |
| 2934 | **engrossed** | 1 | 3 | - | 498.58 | - | 2,421 | - | 0.000527 | 🔵 low — common in general English | — |
| 2935 | **gnawing** | 1 | 3 | - | 498.58 | - | 2,422 | - | 0.000527 | 🔵 low — common in general English | — |
| 2936 | **thirsty** | 1 | 3 | - | 498.58 | - | 2,424 | - | 0.000527 | 🔵 low — common in general English | — |
| 2937 | **vowing** | 1 | 3 | - | 498.58 | - | 2,425 | - | 0.000527 | 🔵 low — common in general English | — |
| 2938 | **elixir** | 1 | 3 | - | 498.58 | - | 2,426 | - | 0.000527 | 🔵 low — common in general English | — |
| 2939 | **conquer** | 1 | 3 | - | 498.58 | - | 2,427 | - | 0.000526 | 🔵 low — common in general English | — |
| 2940 | **musk-deer** | 1 | 3 | - | 498.58 | - | 2,428 | - | 0.000526 | 🔵 low — common in general English | — |
| 2941 | **musk** | 1 | 3 | - | 498.58 | - | 2,429 | - | 0.000526 | 🔵 low — common in general English | — |
| 2942 | **brimming** | 1 | 3 | - | 498.58 | - | 2,430 | - | 0.000526 | 🔵 low — common in general English | — |
| 2943 | **long-lived** | 1 | 3 | - | 498.58 | - | 2,431 | - | 0.000526 | 🔵 low — common in general English | — |
| 2944 | **mute** | 1 | 3 | - | 498.58 | - | 2,432 | - | 0.000526 | 🔵 low — common in general English | — |
| 2945 | **inheriting** | 1 | 3 | - | 498.58 | - | 2,433 | - | 0.000526 | 🔵 low — common in general English | — |
| 2946 | **pernicious** | 1 | 3 | - | 498.58 | - | 2,434 | - | 0.000525 | 🔵 low — common in general English | — |
| 2947 | **lha-thothori** | 1 | 3 | - | 498.58 | - | 2,435 | - | 0.000525 | 🔵 low — common in general English | — |
| 2948 | **alphabet** | 1 | 3 | - | 498.58 | - | 2,437 | - | 0.000525 | 🔵 low — common in general English | — |
| 2949 | **sery** | 1 | 3 | - | 498.58 | - | 2,439 | - | 0.000525 | 🔵 low — common in general English | — |
| 2950 | **preceptor** | 1 | 3 | - | 498.58 | - | 2,440 | - | 0.000524 | 🔵 low — common in general English | — |
| 2951 | **forty** | 1 | 3 | - | 498.58 | - | 2,442 | - | 0.000524 | 🔵 low — common in general English | — |
| 2952 | **wept** | 1 | 3 | - | 498.58 | - | 2,444 | - | 0.000524 | 🔵 low — common in general English | — |
| 2953 | **accom** | 1 | 3 | - | 498.58 | - | 2,445 | - | 0.000524 | 🔵 low — common in general English | — |
| 2954 | **glimmer** | 1 | 3 | - | 498.58 | - | 2,446 | - | 0.000523 | 🔵 low — common in general English | — |
| 2955 | **servitude** | 1 | 3 | - | 498.58 | - | 2,447 | - | 0.000523 | 🔵 low — common in general English | — |
| 2956 | **habit** | 1 | 3 | - | 498.58 | - | 2,448 | - | 0.000523 | 🔵 low — common in general English | — |
| 2957 | **tightly** | 1 | 3 | - | 498.58 | - | 2,449 | - | 0.000523 | 🔵 low — common in general English | — |
| 2958 | **brew** | 1 | 3 | - | 498.58 | - | 2,450 | - | 0.000523 | 🔵 low — common in general English | — |
| 2959 | **upright** | 1 | 3 | - | 498.58 | - | 2,452 | - | 0.000522 | 🔵 low — common in general English | — |
| 2960 | **promis** | 1 | 3 | - | 498.58 | - | 2,453 | - | 0.000522 | 🔵 low — common in general English | — |
| 2961 | **slept** | 1 | 3 | - | 498.58 | - | 2,454 | - | 0.000522 | 🔵 low — common in general English | — |
| 2962 | **spittle** | 1 | 3 | - | 498.58 | - | 2,455 | - | 0.000522 | 🔵 low — common in general English | — |
| 2963 | **noose** | 1 | 3 | - | 498.58 | - | 2,456 | - | 0.000522 | 🔵 low — common in general English | — |
| 2964 | **brilliance** | 1 | 3 | - | 498.58 | - | 2,457 | - | 0.000522 | 🔵 low — common in general English | — |
| 2965 | **alight** | 1 | 3 | - | 498.58 | - | 2,459 | - | 0.000521 | 🔵 low — common in general English | — |
| 2966 | **radiance** | 1 | 3 | - | 498.58 | - | 2,462 | - | 0.000521 | 🔵 low — common in general English | — |
| 2967 | **wrong-doing** | 1 | 3 | - | 498.58 | - | 2,463 | - | 0.000521 | 🔵 low — common in general English | — |
| 2968 | **shower** | 1 | 3 | - | 498.58 | - | 2,464 | - | 0.000521 | 🔵 low — common in general English | — |
| 2969 | **breez** | 1 | 3 | - | 498.58 | - | 2,465 | - | 0.000520 | 🔵 low — common in general English | — |
| 2970 | **enmity** | 1 | 3 | - | 498.58 | - | 2,466 | - | 0.000520 | 🔵 low — common in general English | — |
| 2971 | **brocade** | 1 | 3 | - | 498.58 | - | 2,467 | - | 0.000520 | 🔵 low — common in general English | — |
| 2972 | **cheek** | 1 | 3 | - | 498.58 | - | 2,468 | - | 0.000520 | 🔵 low — common in general English | — |
| 2973 | **murdered** | 1 | 3 | - | 498.58 | - | 2,469 | - | 0.000520 | 🔵 low — common in general English | — |
| 2974 | **starving** | 1 | 3 | - | 498.58 | - | 2,470 | - | 0.000520 | 🔵 low — common in general English | — |
| 2975 | **affectionate** | 1 | 3 | - | 498.58 | - | 2,471 | - | 0.000519 | 🔵 low — common in general English | — |
| 2976 | **barren** | 1 | 3 | - | 498.58 | - | 2,473 | - | 0.000519 | 🔵 low — common in general English | — |
| 2977 | **everlasting** | 1 | 3 | - | 498.58 | - | 2,474 | - | 0.000519 | 🔵 low — common in general English | — |
| 2978 | **relish** | 1 | 3 | - | 498.58 | - | 2,475 | - | 0.000519 | 🔵 low — common in general English | — |
| 2979 | **trivial** | 1 | 3 | - | 498.58 | - | 2,476 | - | 0.000519 | 🔵 low — common in general English | — |
| 2980 | **murder** | 1 | 3 | - | 498.58 | - | 2,477 | - | 0.000519 | 🔵 low — common in general English | — |
| 2981 | **daughter-in-law** | 1 | 3 | - | 498.58 | - | 2,478 | - | 0.000518 | 🔵 low — common in general English | — |
| 2982 | **courageously** | 1 | 3 | - | 498.58 | - | 2,479 | - | 0.000518 | 🔵 low — common in general English | — |
| 2983 | **thieve** | 1 | 3 | - | 498.58 | - | 2,480 | - | 0.000518 | 🔵 low — common in general English | — |
| 2984 | **mortal** | 1 | 3 | - | 498.58 | - | 2,481 | - | 0.000518 | 🔵 low — common in general English | — |
| 2985 | **single-mindedly** | 1 | 3 | - | 498.58 | - | 2,482 | - | 0.000518 | 🔵 low — common in general English | — |
| 2986 | **experi** | 1 | 3 | - | 498.58 | - | 2,483 | - | 0.000518 | 🔵 low — common in general English | — |
| 2987 | **amassing** | 1 | 3 | - | 498.58 | - | 2,484 | - | 0.000517 | 🔵 low — common in general English | — |
| 2988 | **greasy** | 1 | 3 | - | 498.58 | - | 2,485 | - | 0.000517 | 🔵 low — common in general English | — |
| 2989 | **arous** | 1 | 3 | - | 498.58 | - | 2,486 | - | 0.000517 | 🔵 low — common in general English | — |
| 2990 | **assimilated** | 1 | 3 | - | 498.58 | - | 2,487 | - | 0.000517 | 🔵 low — common in general English | — |
| 2991 | **yama** | 1 | 3 | - | 498.58 | - | 2,488 | - | 0.000517 | 🔵 low — common in general English | ✓ གཤིན་རྗེ |
| 2992 | **chopped** | 1 | 3 | - | 498.58 | - | 2,489 | - | 0.000517 | 🔵 low — common in general English | — |
| 2993 | **prong** | 1 | 3 | - | 498.58 | - | 2,490 | - | 0.000517 | 🔵 low — common in general English | — |
| 2994 | **beak** | 1 | 3 | - | 498.58 | - | 2,491 | - | 0.000516 | 🔵 low — common in general English | — |
| 2995 | **razor** | 1 | 3 | - | 498.58 | - | 2,493 | - | 0.000516 | 🔵 low — common in general English | — |
| 2996 | **biting** | 1 | 3 | - | 498.58 | - | 2,494 | - | 0.000516 | 🔵 low — common in general English | — |
| 2997 | **brain** | 1 | 3 | - | 498.58 | - | 2,495 | - | 0.000516 | 🔵 low — common in general English | — |
| 2998 | **moun** | 1 | 3 | - | 498.58 | - | 2,496 | - | 0.000516 | 🔵 low — common in general English | — |
| 2999 | **tain** | 1 | 3 | - | 498.58 | - | 2,497 | - | 0.000515 | 🔵 low — common in general English | — |
| 3000 | **lamenting** | 1 | 3 | - | 498.58 | - | 2,498 | - | 0.000515 | 🔵 low — common in general English | — |
| 3001 | **lung** | 1 | 3 | - | 498.58 | - | 2,500 | - | 0.000515 | 🔵 low — common in general English | — |
| 3002 | **uttered** | 1 | 3 | - | 498.58 | - | 2,501 | - | 0.000515 | 🔵 low — common in general English | — |
| 3003 | **entrail** | 1 | 3 | - | 498.58 | - | 2,502 | - | 0.000515 | 🔵 low — common in general English | — |
| 3004 | **intellectually** | 1 | 3 | - | 498.58 | - | 2,504 | - | 0.000514 | 🔵 low — common in general English | — |
| 3005 | **karmapa** | 1 | 3 | - | 498.58 | - | 2,505 | - | 0.000514 | 🔵 low — common in general English | ✓ ཀར་མ་པ |
| 3006 | **obsessed** | 1 | 3 | - | 498.58 | - | 2,506 | - | 0.000514 | 🔵 low — common in general English | — |
| 3007 | **avarice** | 1 | 3 | - | 498.58 | - | 2,507 | - | 0.000514 | 🔵 low — common in general English | — |
| 3008 | **dish** | 1 | 3 | - | 498.58 | - | 2,508 | - | 0.000514 | 🔵 low — common in general English | — |
| 3009 | **nose** | 1 | 3 | - | 498.58 | - | 2,509 | - | 0.000514 | 🔵 low — common in general English | — |
| 3010 | **ugliness** | 1 | 3 | - | 498.58 | - | 2,510 | - | 0.000513 | 🔵 low — common in general English | — |
| 3011 | **snot** | 1 | 3 | - | 498.58 | - | 2,511 | - | 0.000513 | 🔵 low — common in general English | — |
| 3012 | **mamo** | 1 | 3 | - | 498.58 | - | 2,512 | - | 0.000513 | 🔵 low — common in general English | ✓ མ་མོ |
| 3013 | **happily** | 1 | 3 | - | 498.58 | - | 2,513 | - | 0.000513 | 🔵 low — common in general English | — |
| 3014 | **bum** | 1 | 3 | - | 498.58 | - | 2,514 | - | 0.000513 | 🔵 low — common in general English | — |
| 3015 | **regretting** | 1 | 3 | - | 498.58 | - | 2,515 | - | 0.000513 | 🔵 low — common in general English | — |
| 3016 | **accumu** | 1 | 3 | - | 498.58 | - | 2,516 | - | 0.000513 | 🔵 low — common in general English | — |
| 3017 | **plunder** | 1 | 3 | - | 498.58 | - | 2,517 | - | 0.000512 | 🔵 low — common in general English | — |
| 3018 | **leprosy** | 1 | 3 | - | 498.58 | - | 2,518 | - | 0.000512 | 🔵 low — common in general English | — |
| 3019 | **pregnancy** | 1 | 3 | - | 498.58 | - | 2,519 | - | 0.000512 | 🔵 low — common in general English | — |
| 3020 | **creep** | 1 | 3 | - | 498.58 | - | 2,520 | - | 0.000512 | 🔵 low — common in general English | — |
| 3021 | **granny** | 1 | 3 | - | 498.58 | - | 2,521 | - | 0.000512 | 🔵 low — common in general English | — |
| 3022 | **frown** | 1 | 3 | - | 498.58 | - | 2,522 | - | 0.000512 | 🔵 low — common in general English | — |
| 3023 | **ugly** | 1 | 3 | - | 498.58 | - | 2,523 | - | 0.000512 | 🔵 low — common in general English | — |
| 3024 | **insipid** | 1 | 3 | - | 498.58 | - | 2,524 | - | 0.000511 | 🔵 low — common in general English | — |
| 3025 | **left-over** | 1 | 3 | - | 498.58 | - | 2,526 | - | 0.000511 | 🔵 low — common in general English | — |
| 3026 | **unclean** | 1 | 3 | - | 498.58 | - | 2,527 | - | 0.000511 | 🔵 low — common in general English | — |
| 3027 | **apparition** | 1 | 3 | - | 498.58 | - | 2,528 | - | 0.000511 | 🔵 low — common in general English | — |
| 3028 | **steeped** | 1 | 3 | - | 498.58 | - | 2,529 | - | 0.000511 | 🔵 low — common in general English | — |
| 3029 | **married** | 1 | 3 | - | 498.58 | - | 2,530 | - | 0.000510 | 🔵 low — common in general English | — |
| 3030 | **rosary** | 1 | 3 | - | 498.58 | - | 2,531 | - | 0.000510 | 🔵 low — common in general English | — |
| 3031 | **kindly** | 1 | 3 | - | 498.58 | - | 2,532 | - | 0.000510 | 🔵 low — common in general English | — |
| 3032 | **exhort** | 1 | 3 | - | 498.58 | - | 2,533 | - | 0.000510 | 🔵 low — common in general English | — |
| 3033 | **disgust** | 1 | 3 | - | 498.58 | - | 2,534 | - | 0.000510 | 🔵 low — common in general English | — |
| 3034 | **demigod** | 1 | 3 | - | 498.58 | - | 2,535 | - | 0.000510 | 🔵 low — common in general English | ✓ ལྷ་མ་ཡིན |
| 3035 | **wish-fulfilling** | 1 | 3 | - | 498.58 | - | 2,536 | - | 0.000510 | 🔵 low — common in general English | — |
| 3036 | **waking** | 1 | 3 | - | 498.58 | - | 2,537 | - | 0.000509 | 🔵 low — common in general English | — |
| 3037 | **imagination** | 1 | 3 | - | 498.58 | - | 2,538 | - | 0.000509 | 🔵 low — common in general English | — |
| 3038 | **one-eyed** | 1 | 3 | - | 498.58 | - | 2,539 | - | 0.000509 | 🔵 low — common in general English | — |
| 3039 | **affection** | 1 | 3 | - | 498.58 | - | 2,540 | - | 0.000509 | 🔵 low — common in general English | — |
| 3040 | **slaughterer** | 1 | 3 | - | 498.58 | - | 2,542 | - | 0.000509 | 🔵 low — common in general English | — |
| 3041 | **streaming** | 1 | 3 | - | 498.58 | - | 2,543 | - | 0.000509 | 🔵 low — common in general English | — |
| 3042 | **shortcoming** | 1 | 3 | - | 498.58 | - | 2,544 | - | 0.000508 | 🔵 low — common in general English | — |
| 3043 | **laypeople** | 1 | 3 | - | 498.58 | - | 2,545 | - | 0.000508 | 🔵 low — common in general English | — |
| 3044 | **phoney** | 1 | 3 | - | 498.58 | - | 2,546 | - | 0.000508 | 🔵 low — common in general English | — |
| 3045 | **deceive** | 1 | 3 | - | 498.58 | - | 2,547 | - | 0.000508 | 🔵 low — common in general English | — |
| 3046 | **harshly** | 1 | 3 | - | 498.58 | - | 2,548 | - | 0.000508 | 🔵 low — common in general English | — |
| 3047 | **robbery** | 1 | 3 | - | 498.58 | - | 2,549 | - | 0.000508 | 🔵 low — common in general English | — |
| 3048 | **eternalism** | 1 | 3 | - | 498.58 | - | 2,550 | - | 0.000508 | 🔵 low — common in general English | ✓ རྟག་པར་ལྟ་བ |
| 3049 | **nihilism** | 1 | 3 | - | 498.58 | - | 2,551 | - | 0.000507 | 🔵 low — common in general English | ✓ ཆད་པར་ལྟ་བ |
| 3050 | **peacock** | 1 | 3 | - | 498.58 | - | 2,552 | - | 0.000507 | 🔵 low — common in general English | — |
| 3051 | **multicoloured** | 1 | 3 | - | 498.58 | - | 2,553 | - | 0.000507 | 🔵 low — common in general English | — |
| 3052 | **stole** | 1 | 3 | - | 498.58 | - | 2,554 | - | 0.000507 | 🔵 low — common in general English | — |
| 3053 | **lied** | 1 | 3 | - | 498.58 | - | 2,555 | - | 0.000507 | 🔵 low — common in general English | — |
| 3054 | **sin** | 1 | 3 | - | 498.58 | - | 2,556 | - | 0.000507 | 🔵 low — common in general English | — |
| 3055 | **futile** | 1 | 3 | - | 498.58 | - | 2,557 | - | 0.000507 | 🔵 low — common in general English | — |
| 3056 | **fishermen** | 1 | 3 | - | 498.58 | - | 2,559 | - | 0.000506 | 🔵 low — common in general English | — |
| 3057 | **troop** | 1 | 3 | - | 498.58 | - | 2,560 | - | 0.000506 | 🔵 low — common in general English | — |
| 3058 | **strayed** | 1 | 3 | - | 498.58 | - | 2,561 | - | 0.000506 | 🔵 low — common in general English | — |
| 3059 | **miserly** | 1 | 3 | - | 498.58 | - | 2,563 | - | 0.000506 | 🔵 low — common in general English | — |
| 3060 | **wholesome** | 1 | 3 | - | 498.58 | - | 2,564 | - | 0.000505 | 🔵 low — common in general English | — |
| 3061 | **incarnation** | 1 | 3 | - | 498.58 | - | 2,565 | - | 0.000505 | 🔵 low — common in general English | — |
| 3062 | **unconscious** | 1 | 3 | - | 498.58 | - | 2,566 | - | 0.000505 | 🔵 low — common in general English | — |
| 3063 | **ness** | 1 | 3 | - | 498.58 | - | 2,567 | - | 0.000505 | 🔵 low — common in general English | — |
| 3064 | **pathway** | 1 | 3 | - | 498.58 | - | 2,569 | - | 0.000505 | 🔵 low — common in general English | — |
| 3065 | **navigator** | 1 | 3 | - | 498.58 | - | 2,570 | - | 0.000505 | 🔵 low — common in general English | — |
| 3066 | **brilliant** | 1 | 3 | - | 498.58 | - | 2,572 | - | 0.000504 | 🔵 low — common in general English | — |
| 3067 | **unfold** | 1 | 3 | - | 498.58 | - | 2,574 | - | 0.000504 | 🔵 low — common in general English | — |
| 3068 | **dispelling** | 1 | 3 | - | 498.58 | - | 2,575 | - | 0.000504 | 🔵 low — common in general English | — |
| 3069 | **tainted** | 1 | 3 | - | 498.58 | - | 2,576 | - | 0.000504 | 🔵 low — common in general English | ~ |
| 3070 | **arrogance** | 1 | 3 | - | 498.58 | - | 2,577 | - | 0.000504 | 🔵 low — common in general English | — |
| 3071 | **verbally** | 1 | 3 | - | 498.58 | - | 2,578 | - | 0.000503 | 🔵 low — common in general English | — |
| 3072 | **slam** | 1 | 3 | - | 498.58 | - | 2,579 | - | 0.000503 | 🔵 low — common in general English | — |
| 3073 | **accomplishing** | 1 | 3 | - | 498.58 | - | 2,580 | - | 0.000503 | 🔵 low — common in general English | — |
| 3074 | **impurity** | 1 | 3 | - | 498.58 | - | 2,581 | - | 0.000503 | 🔵 low — common in general English | — |
| 3075 | **imitate** | 1 | 3 | - | 498.58 | - | 2,582 | - | 0.000503 | 🔵 low — common in general English | — |
| 3076 | **fatigue** | 1 | 3 | - | 498.58 | - | 2,584 | - | 0.000503 | 🔵 low — common in general English | — |
| 3077 | **ods** | 1 | 3 | - | 498.58 | - | 2,586 | - | 0.000502 | 🔵 low — common in general English | — |
| 3078 | **retinue** | 1 | 3 | - | 498.58 | - | 2,588 | - | 0.000502 | 🔵 low — common in general English | — |
| 3079 | **carriage** | 1 | 3 | - | 498.58 | - | 2,589 | - | 0.000502 | 🔵 low — common in general English | — |
| 3080 | **conquest** | 1 | 3 | - | 498.58 | - | 2,590 | - | 0.000502 | 🔵 low — common in general English | — |
| 3081 | **sinner** | 1 | 3 | - | 498.58 | - | 2,591 | - | 0.000502 | 🔵 low — common in general English | — |
| 3082 | **inexpressible** | 1 | 3 | - | 498.58 | - | 2,592 | - | 0.000501 | 🔵 low — common in general English | — |
| 3083 | **erment** | 1 | 3 | - | 498.58 | - | 2,593 | - | 0.000501 | 🔵 low — common in general English | — |
| 3084 | **vers** | 1 | 3 | - | 498.58 | - | 2,594 | - | 0.000501 | 🔵 low — common in general English | — |
| 3085 | **deceit** | 1 | 3 | - | 498.58 | - | 2,595 | - | 0.000501 | 🔵 low — common in general English | — |
| 3086 | **kusali** | 1 | 3 | - | 498.58 | - | 2,596 | - | 0.000501 | 🔵 low — common in general English | — |
| 3087 | **imbued** | 1 | 3 | - | 498.58 | - | 2,599 | - | 0.000500 | 🔵 low — common in general English | — |
| 3088 | **lattice** | 1 | 3 | - | 498.58 | - | 2,603 | - | 0.000500 | 🔵 low — common in general English | — |
| 3089 | **cruel** | 1 | 3 | - | 498.58 | - | 2,604 | - | 0.000500 | 🔵 low — common in general English | — |
| 3090 | **unceasingly** | 1 | 3 | - | 498.58 | - | 2,605 | - | 0.000500 | 🔵 low — common in general English | — |
| 3091 | **saucer** | 1 | 3 | - | 498.58 | - | 2,606 | - | 0.000499 | 🔵 low — common in general English | — |
| 3092 | **transgress** | 1 | 3 | - | 498.58 | - | 2,607 | - | 0.000499 | 🔵 low — common in general English | — |
| 3093 | **drip** | 1 | 3 | - | 498.58 | - | 2,609 | - | 0.000499 | 🔵 low — common in general English | — |
| 3094 | **malignant** | 1 | 3 | - | 498.58 | - | 2,610 | - | 0.000499 | 🔵 low — common in general English | — |
| 3095 | **freshly** | 1 | 3 | - | 498.58 | - | 2,611 | - | 0.000499 | 🔵 low — common in general English | — |
| 3096 | **hind** | 1 | 3 | - | 498.58 | - | 2,612 | - | 0.000499 | 🔵 low — common in general English | — |
| 3097 | **faintest** | 1 | 3 | - | 498.58 | - | 2,613 | - | 0.000499 | 🔵 low — common in general English | — |
| 3098 | **camel** | 1 | 3 | - | 498.58 | - | 2,614 | - | 0.000498 | 🔵 low — common in general English | — |
| 3099 | **quintessence** | 1 | 3 | - | 498.58 | - | 2,616 | - | 0.000498 | 🔵 low — common in general English | — |
| 3100 | **panacea** | 1 | 3 | - | 498.58 | - | 2,617 | - | 0.000498 | 🔵 low — common in general English | — |
| 3101 | **defilement** | 1 | 3 | - | 498.58 | - | 2,618 | - | 0.000498 | 🔵 low — common in general English | — |
| 3102 | **louse** | 1 | 3 | - | 498.58 | - | 2,619 | - | 0.000498 | 🔵 low — common in general English | — |
| 3103 | **leper** | 1 | 3 | - | 498.58 | - | 2,621 | - | 0.000497 | 🔵 low — common in general English | — |
| 3104 | **cured** | 1 | 3 | - | 498.58 | - | 2,623 | - | 0.000497 | 🔵 low — common in general English | — |
| 3105 | **risi** | 1 | 3 | - | 498.58 | - | 2,624 | - | 0.000497 | 🔵 low — common in general English | — |
| 3106 | **omen** | 1 | 3 | - | 498.58 | - | 2,625 | - | 0.000497 | 🔵 low — common in general English | — |
| 3107 | **transmitting** | 1 | 3 | - | 498.58 | - | 2,626 | - | 0.000497 | 🔵 low — common in general English | — |
| 3108 | **warmth** | 1 | 3 | - | 498.58 | - | 2,627 | - | 0.000497 | 🔵 low — common in general English | ~ |
| 3109 | **tame** | 1 | 3 | - | 498.58 | - | 2,628 | - | 0.000496 | 🔵 low — common in general English | — |
| 3110 | **indivisible** | 1 | 3 | - | 498.58 | - | 2,629 | - | 0.000496 | 🔵 low — common in general English | — |
| 3111 | **imprint** | 1 | 3 | - | 498.58 | - | 2,630 | - | 0.000496 | 🔵 low — common in general English | — |
| 3112 | **prostrating** | 1 | 3 | - | 498.58 | - | 2,632 | - | 0.000496 | 🔵 low — common in general English | — |
| 3113 | **adorned** | 1 | 3 | - | 498.58 | - | 2,633 | - | 0.000496 | 🔵 low — common in general English | — |
| 3114 | **tva** | 1 | 3 | - | 498.58 | - | 2,634 | - | 0.000496 | 🔵 low — common in general English | — |
| 3115 | **sattva** | 1 | 3 | - | 498.58 | - | 2,635 | - | 0.000495 | 🔵 low — common in general English | — |
| 3116 | **perfumed** | 1 | 3 | - | 498.58 | - | 2,637 | - | 0.000495 | 🔵 low — common in general English | — |
| 3117 | **explanatory** | 1 | 3 | - | 498.58 | - | 2,638 | - | 0.000495 | 🔵 low — common in general English | — |
| 3118 | **aperture** | 1 | 3 | - | 498.58 | - | 2,641 | - | 0.000495 | 🔵 low — common in general English | ~ |
| 3119 | **demoness** | 1 | 3 | - | 498.58 | - | 2,642 | - | 0.000494 | 🔵 low — common in general English | — |
| 3120 | **duality** | 1 | 3 | - | 498.58 | - | 2,643 | - | 0.000494 | 🔵 low — common in general English | — |
| 3121 | **dissolved** | 1 | 3 | - | 498.58 | - | 2,645 | - | 0.000494 | 🔵 low — common in general English | — |
| 3122 | **lotus-bud** | 1 | 3 | - | 498.58 | - | 2,646 | - | 0.000494 | 🔵 low — common in general English | — |
| 3123 | **khatvanga** | 1 | 3 | - | 498.58 | - | 2,647 | - | 0.000494 | 🔵 low — common in general English | ✓ |
| 3124 | **rejoiced** | 1 | 3 | - | 498.58 | - | 2,648 | - | 0.000494 | 🔵 low — common in general English | — |
| 3125 | **cubit** | 1 | 3 | - | 498.58 | - | 2,650 | - | 0.000493 | 🔵 low — common in general English | — |
| 3126 | **ejection** | 1 | 3 | - | 498.58 | - | 2,656 | - | 0.000493 | 🔵 low — common in general English | — |
| 3127 | **rising** | 1 | 6 | - | 498.39 | - | 2,658 | - | 0.000492 | 🔵 low — common in general English | — |
| 3128 | **comparison** | 1 | 4 | - | 492.74 | - | 2,660 | - | 0.000492 | 🔵 low — common in general English | — |
| 3129 | **developing** | 1 | 5 | - | 490.55 | - | 2,667 | - | 0.000491 | 🔵 low — common in general English | — |
| 3130 | **hour** | 1 | 4 | - | 487.19 | - | 2,670 | - | 0.000491 | 🔵 low — common in general English | — |
| 3131 | **sustained** | 1 | 4 | - | 484.57 | - | 2,673 | - | 0.000490 | 🔵 low — common in general English | ~ |
| 3132 | **shooting** | 1 | 3 | - | 477.66 | - | 2,676 | - | 0.000490 | 🔵 low — common in general English | — |
| 3133 | **visual** | 1 | 3 | - | 477.66 | - | 2,677 | - | 0.000490 | 🔵 low — common in general English | — |
| 3134 | **mud** | 1 | 3 | - | 477.66 | - | 2,678 | - | 0.000490 | 🔵 low — common in general English | — |
| 3135 | **roof** | 1 | 3 | - | 477.66 | - | 2,680 | - | 0.000489 | 🔵 low — common in general English | — |
| 3136 | **worthy** | 1 | 3 | - | 477.66 | - | 2,682 | - | 0.000489 | 🔵 low — common in general English | — |
| 3137 | **disciplined** | 1 | 3 | - | 477.66 | - | 2,683 | - | 0.000489 | 🔵 low — common in general English | — |
| 3138 | **stretched** | 1 | 3 | - | 477.66 | - | 2,684 | - | 0.000489 | 🔵 low — common in general English | — |
| 3139 | **cardinal** | 1 | 3 | - | 477.66 | - | 2,686 | - | 0.000489 | 🔵 low — common in general English | — |
| 3140 | **sesame** | 1 | 3 | - | 477.66 | - | 2,687 | - | 0.000488 | 🔵 low — common in general English | — |
| 3141 | **belly** | 1 | 3 | - | 477.66 | - | 2,688 | - | 0.000488 | 🔵 low — common in general English | — |
| 3142 | **isn** | 1 | 3 | - | 477.66 | - | 2,689 | - | 0.000488 | 🔵 low — common in general English | — |
| 3143 | **cheese** | 1 | 3 | - | 477.66 | - | 2,690 | - | 0.000488 | 🔵 low — common in general English | — |
| 3144 | **ragged** | 1 | 3 | - | 477.66 | - | 2,691 | - | 0.000488 | 🔵 low — common in general English | — |
| 3145 | **overcoming** | 1 | 3 | - | 477.66 | - | 2,692 | - | 0.000488 | 🔵 low — common in general English | — |
| 3146 | **theft** | 1 | 3 | - | 477.66 | - | 2,693 | - | 0.000488 | 🔵 low — common in general English | — |
| 3147 | **miracle** | 1 | 3 | - | 477.66 | - | 2,694 | - | 0.000488 | 🔵 low — common in general English | — |
| 3148 | **renouncing** | 1 | 3 | - | 477.66 | - | 2,695 | - | 0.000487 | 🔵 low — common in general English | — |
| 3149 | **severed** | 1 | 3 | - | 477.66 | - | 2,696 | - | 0.000487 | 🔵 low — common in general English | — |
| 3150 | **utmost** | 1 | 3 | - | 477.66 | - | 2,697 | - | 0.000487 | 🔵 low — common in general English | — |
| 3151 | **workable** | 1 | 3 | - | 477.66 | - | 2,698 | - | 0.000487 | 🔵 low — common in general English | — |
| 3152 | **resolute** | 1 | 3 | - | 477.66 | - | 2,699 | - | 0.000487 | 🔵 low — common in general English | — |
| 3153 | **wished** | 1 | 3 | - | 477.66 | - | 2,700 | - | 0.000487 | 🔵 low — common in general English | — |
| 3154 | **willingly** | 1 | 3 | - | 477.66 | - | 2,701 | - | 0.000487 | 🔵 low — common in general English | — |
| 3155 | **lunar** | 1 | 3 | - | 477.66 | - | 2,702 | - | 0.000486 | 🔵 low — common in general English | — |
| 3156 | **repetition** | 1 | 3 | - | 477.66 | - | 2,703 | - | 0.000486 | 🔵 low — common in general English | — |
| 3157 | **shorten** | 1 | 3 | - | 477.66 | - | 2,704 | - | 0.000486 | 🔵 low — common in general English | — |
| 3158 | **repeating** | 1 | 3 | - | 477.66 | - | 2,705 | - | 0.000486 | 🔵 low — common in general English | — |
| 3159 | **event** | 1 | 4 | - | 477.27 | - | 2,706 | - | 0.000486 | 🔵 low — common in general English | — |
| 3160 | **losing** | 1 | 4 | - | 477.27 | - | 2,707 | - | 0.000486 | 🔵 low — common in general English | — |
| 3161 | **bottom** | 1 | 4 | - | 472.80 | - | 2,709 | - | 0.000486 | 🔵 low — common in general English | — |
| 3162 | **elsewhere** | 1 | 4 | - | 472.80 | - | 2,710 | - | 0.000485 | 🔵 low — common in general English | — |
| 3163 | **law** | 1 | 5 | - | 471.55 | - | 2,712 | - | 0.000485 | 🔵 low — common in general English | — |
| 3164 | **chain** | 1 | 4 | - | 470.66 | - | 2,714 | - | 0.000485 | 🔵 low — common in general English | — |
| 3165 | **remained** | 1 | 5 | - | 469.53 | - | 2,715 | - | 0.000485 | 🔵 low — common in general English | — |
| 3166 | **jumped** | 1 | 4 | - | 468.59 | - | 2,716 | - | 0.000485 | 🔵 low — common in general English | — |
| 3167 | **ended** | 1 | 7 | - | 465.13 | - | 2,717 | - | 0.000484 | 🔵 low — common in general English | — |
| 3168 | **discomfort** | 1 | 3 | - | 462.71 | - | 2,720 | - | 0.000484 | 🔵 low — common in general English | — |
| 3169 | **uphold** | 1 | 3 | - | 462.71 | - | 2,721 | - | 0.000484 | 🔵 low — common in general English | — |
| 3170 | **checking** | 1 | 3 | - | 462.71 | - | 2,722 | - | 0.000484 | 🔵 low — common in general English | — |
| 3171 | **descent** | 1 | 3 | - | 462.71 | - | 2,723 | - | 0.000484 | 🔵 low — common in general English | — |
| 3172 | **compounded** | 1 | 3 | - | 462.71 | - | 2,724 | - | 0.000484 | 🔵 low — common in general English | — |
| 3173 | **height** | 1 | 3 | - | 462.71 | - | 2,725 | - | 0.000483 | 🔵 low — common in general English | — |
| 3174 | **mansion** | 1 | 3 | - | 462.71 | - | 2,727 | - | 0.000483 | 🔵 low — common in general English | — |
| 3175 | **amongst** | 1 | 3 | - | 462.71 | - | 2,728 | - | 0.000483 | 🔵 low — common in general English | — |
| 3176 | **powdered** | 1 | 3 | - | 462.71 | - | 2,729 | - | 0.000483 | 🔵 low — common in general English | — |
| 3177 | **harmed** | 1 | 3 | - | 462.71 | - | 2,731 | - | 0.000483 | 🔵 low — common in general English | — |
| 3178 | **namely** | 1 | 3 | - | 462.71 | - | 2,732 | - | 0.000483 | 🔵 low — common in general English | — |
| 3179 | **drinking** | 1 | 3 | - | 462.71 | - | 2,733 | - | 0.000482 | 🔵 low — common in general English | — |
| 3180 | **shaken** | 1 | 3 | - | 462.71 | - | 2,734 | - | 0.000482 | 🔵 low — common in general English | — |
| 3181 | **inspired** | 1 | 3 | - | 462.71 | - | 2,736 | - | 0.000482 | 🔵 low — common in general English | — |
| 3182 | **invoked** | 1 | 3 | - | 462.71 | - | 2,737 | - | 0.000482 | 🔵 low — common in general English | — |
| 3183 | **recognizing** | 1 | 3 | - | 462.71 | - | 2,738 | - | 0.000482 | 🔵 low — common in general English | — |
| 3184 | **pity** | 1 | 3 | - | 462.71 | - | 2,739 | - | 0.000482 | 🔵 low — common in general English | — |
| 3185 | **ring** | 1 | 3 | - | 462.71 | - | 2,740 | - | 0.000482 | 🔵 low — common in general English | — |
| 3186 | **assembled** | 1 | 3 | - | 462.71 | - | 2,741 | - | 0.000481 | 🔵 low — common in general English | — |
| 3187 | **origin** | 1 | 4 | - | 460.88 | - | 2,742 | - | 0.000481 | 🔵 low — common in general English | — |
| 3188 | **grown** | 1 | 4 | - | 457.33 | - | 2,746 | - | 0.000481 | 🔵 low — common in general English | — |
| 3189 | **provided** | 1 | 5 | - | 456.55 | - | 2,747 | - | 0.000481 | 🔵 low — common in general English | — |
| 3190 | **gained** | 1 | 4 | - | 453.95 | - | 2,749 | - | 0.000480 | 🔵 low — common in general English | — |
| 3191 | **los** | 1 | 4 | - | 453.95 | - | 2,750 | - | 0.000480 | 🔵 low — common in general English | — |
| 3192 | **falling** | 1 | 5 | - | 453.18 | - | 2,751 | - | 0.000480 | 🔵 low — common in general English | — |
| 3193 | **imperative** | 1 | 3 | - | 451.10 | - | 2,755 | - | 0.000480 | 🔵 low — common in general English | — |
| 3194 | **chasing** | 1 | 3 | - | 451.10 | - | 2,756 | - | 0.000480 | 🔵 low — common in general English | — |
| 3195 | **intact** | 1 | 3 | - | 451.10 | - | 2,757 | - | 0.000479 | 🔵 low — common in general English | — |
| 3196 | **progressively** | 1 | 3 | - | 451.10 | - | 2,759 | - | 0.000479 | 🔵 low — common in general English | — |
| 3197 | **guarded** | 1 | 3 | - | 451.10 | - | 2,760 | - | 0.000479 | 🔵 low — common in general English | — |
| 3198 | **compiled** | 1 | 3 | - | 451.10 | - | 2,761 | - | 0.000479 | 🔵 low — common in general English | — |
| 3199 | **welfare** | 1 | 3 | - | 451.10 | - | 2,762 | - | 0.000479 | 🔵 low — common in general English | — |
| 3200 | **profoundly** | 1 | 3 | - | 451.10 | - | 2,763 | - | 0.000479 | 🔵 low — common in general English | — |
| 3201 | **deeper** | 1 | 3 | - | 451.10 | - | 2,764 | - | 0.000479 | 🔵 low — common in general English | — |
| 3202 | **roasted** | 1 | 3 | - | 451.10 | - | 2,765 | - | 0.000478 | 🔵 low — common in general English | — |
| 3203 | **crack** | 1 | 3 | - | 451.10 | - | 2,766 | - | 0.000478 | 🔵 low — common in general English | — |
| 3204 | **thick** | 1 | 3 | - | 451.10 | - | 2,767 | - | 0.000478 | 🔵 low — common in general English | — |
| 3205 | **offensive** | 1 | 3 | - | 451.10 | - | 2,768 | - | 0.000478 | 🔵 low — common in general English | — |
| 3206 | **conditioning** | 1 | 3 | - | 451.10 | - | 2,769 | - | 0.000478 | 🔵 low — common in general English | ~ |
| 3207 | **splinter** | 1 | 3 | - | 451.10 | - | 2,770 | - | 0.000478 | 🔵 low — common in general English | — |
| 3208 | **weighed** | 1 | 3 | - | 451.10 | - | 2,771 | - | 0.000478 | 🔵 low — common in general English | — |
| 3209 | **heap** | 1 | 3 | - | 451.10 | - | 2,772 | - | 0.000478 | 🔵 low — common in general English | — |
| 3210 | **capture** | 1 | 3 | - | 451.10 | - | 2,773 | - | 0.000477 | 🔵 low — common in general English | — |
| 3211 | **opinion** | 1 | 4 | - | 443.26 | - | 2,780 | - | 0.000477 | 🔵 low — common in general English | — |
| 3212 | **music** | 1 | 3 | - | 441.63 | - | 2,782 | - | 0.000476 | 🔵 low — common in general English | — |
| 3213 | **endeavour** | 1 | 3 | - | 441.63 | - | 2,783 | - | 0.000476 | 🔵 low — common in general English | — |
| 3214 | **wealthy** | 1 | 3 | - | 441.63 | - | 2,784 | - | 0.000476 | 🔵 low — common in general English | — |
| 3215 | **fur** | 1 | 3 | - | 441.63 | - | 2,785 | - | 0.000476 | 🔵 low — common in general English | — |
| 3216 | **nice** | 1 | 3 | - | 441.63 | - | 2,786 | - | 0.000476 | 🔵 low — common in general English | — |
| 3217 | **grove** | 1 | 3 | - | 441.63 | - | 2,787 | - | 0.000476 | 🔵 low — common in general English | — |
| 3218 | **introducing** | 1 | 3 | - | 441.63 | - | 2,788 | - | 0.000476 | 🔵 low — common in general English | — |
| 3219 | **sympathetic** | 1 | 3 | - | 441.63 | - | 2,789 | - | 0.000475 | 🔵 low — common in general English | — |
| 3220 | **unfortunate** | 1 | 3 | - | 441.63 | - | 2,790 | - | 0.000475 | 🔵 low — common in general English | — |
| 3221 | **closed** | 1 | 5 | - | 440.85 | - | 2,791 | - | 0.000475 | 🔵 low — common in general English | — |
| 3222 | **growing** | 1 | 5 | - | 439.43 | - | 2,794 | - | 0.000475 | 🔵 low — common in general English | — |
| 3223 | **needed** | 1 | 5 | - | 436.65 | - | 2,795 | - | 0.000475 | 🔵 low — common in general English | — |
| 3224 | **covering** | 1 | 4 | - | 436.52 | - | 2,796 | - | 0.000475 | 🔵 low — common in general English | — |
| 3225 | **allow** | 1 | 5 | - | 433.95 | - | 2,797 | - | 0.000474 | 🔵 low — common in general English | — |
| 3226 | **drove** | 1 | 3 | - | 433.61 | - | 2,798 | - | 0.000474 | 🔵 low — common in general English | — |
| 3227 | **relaxed** | 1 | 3 | - | 433.61 | - | 2,799 | - | 0.000474 | 🔵 low — common in general English | — |
| 3228 | **frontier** | 1 | 3 | - | 433.61 | - | 2,800 | - | 0.000474 | 🔵 low — common in general English | — |
| 3229 | **dig** | 1 | 3 | - | 433.61 | - | 2,801 | - | 0.000474 | 🔵 low — common in general English | — |
| 3230 | **disagreement** | 1 | 3 | - | 433.61 | - | 2,802 | - | 0.000474 | 🔵 low — common in general English | — |
| 3231 | **pig** | 1 | 3 | - | 433.61 | - | 2,803 | - | 0.000474 | 🔵 low — common in general English | — |
| 3232 | **declared** | 1 | 5 | - | 432.20 | - | 2,804 | - | 0.000474 | 🔵 low — common in general English | — |
| 3233 | **providing** | 1 | 4 | - | 431.57 | - | 2,806 | - | 0.000473 | 🔵 low — common in general English | — |
| 3234 | **began** | 1 | 5 | - | 431.34 | - | 2,807 | - | 0.000473 | 🔵 low — common in general English | — |
| 3235 | **seeking** | 1 | 5 | - | 430.49 | - | 2,808 | - | 0.000473 | 🔵 low — common in general English | — |
| 3236 | **near** | 1 | 5 | - | 428.80 | - | 2,812 | - | 0.000473 | 🔵 low — common in general English | — |
| 3237 | **moved** | 1 | 4 | - | 428.07 | - | 2,813 | - | 0.000472 | 🔵 low — common in general English | — |
| 3238 | **showed** | 1 | 5 | - | 426.75 | - | 2,814 | - | 0.000472 | 🔵 low — common in general English | — |
| 3239 | **function** | 1 | 3 | - | 426.67 | - | 2,815 | - | 0.000472 | 🔵 low — common in general English | — |
| 3240 | **peripheral** | 1 | 3 | - | 426.67 | - | 2,816 | - | 0.000472 | 🔵 low — common in general English | — |
| 3241 | **affair** | 1 | 3 | - | 426.67 | - | 2,817 | - | 0.000472 | 🔵 low — common in general English | — |
| 3242 | **hawk** | 1 | 3 | - | 426.67 | - | 2,818 | - | 0.000472 | 🔵 low — common in general English | — |
| 3243 | **stepping** | 1 | 3 | - | 426.67 | - | 2,819 | - | 0.000472 | 🔵 low — common in general English | — |
| 3244 | **slope** | 1 | 3 | - | 426.67 | - | 2,820 | - | 0.000472 | 🔵 low — common in general English | — |
| 3245 | **defeated** | 1 | 3 | - | 426.67 | - | 2,821 | - | 0.000471 | 🔵 low — common in general English | — |
| 3246 | **enable** | 1 | 4 | - | 423.67 | - | 2,826 | - | 0.000471 | 🔵 low — common in general English | — |
| 3247 | **ending** | 1 | 5 | - | 423.55 | - | 2,827 | - | 0.000471 | 🔵 low — common in general English | — |
| 3248 | **rein** | 1 | 3 | - | 420.55 | - | 2,828 | - | 0.000471 | 🔵 low — common in general English | — |
| 3249 | **remote** | 1 | 3 | - | 420.55 | - | 2,829 | - | 0.000471 | 🔵 low — common in general English | — |
| 3250 | **earliest** | 1 | 3 | - | 420.55 | - | 2,830 | - | 0.000470 | 🔵 low — common in general English | — |
| 3251 | **smooth** | 1 | 3 | - | 420.55 | - | 2,831 | - | 0.000470 | 🔵 low — common in general English | — |
| 3252 | **distorted** | 1 | 3 | - | 420.55 | - | 2,832 | - | 0.000470 | 🔵 low — common in general English | — |
| 3253 | **vary** | 1 | 3 | - | 420.55 | - | 2,833 | - | 0.000470 | 🔵 low — common in general English | — |
| 3254 | **feeding** | 1 | 3 | - | 420.55 | - | 2,834 | - | 0.000470 | 🔵 low — common in general English | — |
| 3255 | **ceased** | 1 | 3 | - | 420.55 | - | 2,835 | - | 0.000470 | 🔵 low — common in general English | — |
| 3256 | **paying** | 1 | 4 | - | 417.55 | - | 2,838 | - | 0.000469 | 🔵 low — common in general English | — |
| 3257 | **successor** | 1 | 3 | - | 415.07 | - | 2,840 | - | 0.000469 | 🔵 low — common in general English | — |
| 3258 | **loaded** | 1 | 3 | - | 415.07 | - | 2,841 | - | 0.000469 | 🔵 low — common in general English | — |
| 3259 | **inherent** | 1 | 3 | - | 415.07 | - | 2,842 | - | 0.000469 | 🔵 low — common in general English | — |
| 3260 | **banner** | 1 | 3 | - | 415.07 | - | 2,843 | - | 0.000469 | 🔵 low — common in general English | ~ |
| 3261 | **inevitably** | 1 | 3 | - | 415.07 | - | 2,844 | - | 0.000469 | 🔵 low — common in general English | — |
| 3262 | **fulfil** | 1 | 3 | - | 410.11 | - | 2,846 | - | 0.000469 | 🔵 low — common in general English | — |
| 3263 | **upside** | 1 | 3 | - | 410.11 | - | 2,847 | - | 0.000468 | 🔵 low — common in general English | — |
| 3264 | **custom** | 1 | 3 | - | 410.11 | - | 2,848 | - | 0.000468 | 🔵 low — common in general English | — |
| 3265 | **translated** | 1 | 3 | - | 410.11 | - | 2,849 | - | 0.000468 | 🔵 low — common in general English | — |
| 3266 | **practical** | 1 | 3 | - | 410.11 | - | 2,850 | - | 0.000468 | 🔵 low — common in general English | — |
| 3267 | **scattered** | 1 | 3 | - | 410.11 | - | 2,851 | - | 0.000468 | 🔵 low — common in general English | — |
| 3268 | **unlimited** | 1 | 3 | - | 410.11 | - | 2,852 | - | 0.000468 | 🔵 low — common in general English | — |
| 3269 | **roll** | 1 | 3 | - | 410.11 | - | 2,853 | - | 0.000468 | 🔵 low — common in general English | — |
| 3270 | **minute** | 1 | 3 | - | 410.11 | - | 2,854 | - | 0.000468 | 🔵 low — common in general English | — |
| 3271 | **bag** | 1 | 3 | - | 405.59 | - | 2,858 | - | 0.000467 | 🔵 low — common in general English | — |
| 3272 | **automatically** | 1 | 3 | - | 405.59 | - | 2,859 | - | 0.000467 | 🔵 low — common in general English | — |
| 3273 | **visited** | 1 | 3 | - | 405.59 | - | 2,860 | - | 0.000467 | 🔵 low — common in general English | — |
| 3274 | **fellow** | 1 | 3 | - | 405.59 | - | 2,861 | - | 0.000467 | 🔵 low — common in general English | — |
| 3275 | **moving** | 1 | 4 | - | 405.08 | - | 2,862 | - | 0.000467 | 🔵 low — common in general English | — |
| 3276 | **warned** | 1 | 4 | - | 405.08 | - | 2,863 | - | 0.000467 | 🔵 low — common in general English | — |
| 3277 | **deal** | 1 | 5 | - | 404.61 | - | 2,864 | - | 0.000466 | 🔵 low — common in general English | — |
| 3278 | **resulting** | 1 | 4 | - | 401.89 | - | 2,867 | - | 0.000466 | 🔵 low — common in general English | — |
| 3279 | **worker** | 1 | 3 | - | 401.43 | - | 2,869 | - | 0.000466 | 🔵 low — common in general English | — |
| 3280 | **farmer** | 1 | 3 | - | 401.43 | - | 2,870 | - | 0.000466 | 🔵 low — common in general English | — |
| 3281 | **cool** | 1 | 3 | - | 401.43 | - | 2,871 | - | 0.000466 | 🔵 low — common in general English | — |
| 3282 | **possibility** | 1 | 4 | - | 398.84 | - | 2,873 | - | 0.000465 | 🔵 low — common in general English | — |
| 3283 | **furthermore** | 1 | 3 | - | 397.58 | - | 2,874 | - | 0.000465 | 🔵 low — common in general English | — |
| 3284 | **memory** | 1 | 3 | - | 397.58 | - | 2,875 | - | 0.000465 | 🔵 low — common in general English | — |
| 3285 | **stayed** | 1 | 3 | - | 397.58 | - | 2,876 | - | 0.000465 | 🔵 low — common in general English | — |
| 3286 | **party** | 1 | 4 | - | 397.37 | - | 2,877 | - | 0.000465 | 🔵 low — common in general English | — |
| 3287 | **mass** | 1 | 3 | - | 393.99 | - | 2,878 | - | 0.000465 | 🔵 low — common in general English | — |
| 3288 | **generating** | 1 | 3 | - | 393.99 | - | 2,879 | - | 0.000465 | 🔵 low — common in general English | — |
| 3289 | **armed** | 1 | 3 | - | 393.99 | - | 2,880 | - | 0.000465 | 🔵 low — common in general English | — |
| 3290 | **responsibility** | 1 | 3 | - | 393.99 | - | 2,881 | - | 0.000464 | 🔵 low — common in general English | — |
| 3291 | **stood** | 1 | 4 | - | 393.81 | - | 2,882 | - | 0.000464 | 🔵 low — common in general English | — |
| 3292 | **wanted** | 1 | 4 | - | 393.12 | - | 2,883 | - | 0.000464 | 🔵 low — common in general English | — |
| 3293 | **class** | 1 | 4 | - | 392.44 | - | 2,884 | - | 0.000464 | 🔵 low — common in general English | — |
| 3294 | **firmly** | 1 | 3 | - | 390.63 | - | 2,885 | - | 0.000464 | 🔵 low — common in general English | — |
| 3295 | **conjunction** | 1 | 3 | - | 390.63 | - | 2,886 | - | 0.000464 | 🔵 low — common in general English | — |
| 3296 | **flood** | 1 | 3 | - | 390.63 | - | 2,888 | - | 0.000464 | 🔵 low — common in general English | — |
| 3297 | **executed** | 1 | 3 | - | 390.63 | - | 2,889 | - | 0.000463 | 🔵 low — common in general English | — |
| 3298 | **affect** | 1 | 4 | - | 390.43 | - | 2,890 | - | 0.000463 | 🔵 low — common in general English | — |
| 3299 | **formed** | 1 | 4 | - | 387.84 | - | 2,891 | - | 0.000463 | 🔵 low — common in general English | — |
| 3300 | **absorb** | 1 | 3 | - | 387.48 | - | 2,892 | - | 0.000463 | 🔵 low — common in general English | — |
| 3301 | **frost** | 1 | 3 | - | 387.48 | - | 2,893 | - | 0.000463 | 🔵 low — common in general English | — |
| 3302 | **pledge** | 1 | 3 | - | 387.48 | - | 2,894 | - | 0.000463 | 🔵 low — common in general English | — |
| 3303 | **manage** | 1 | 3 | - | 387.48 | - | 2,895 | - | 0.000463 | 🔵 low — common in general English | — |
| 3304 | **route** | 1 | 3 | - | 384.51 | - | 2,897 | - | 0.000463 | 🔵 low — common in general English | — |
| 3305 | **surrounding** | 1 | 3 | - | 384.51 | - | 2,898 | - | 0.000462 | 🔵 low — common in general English | — |
| 3306 | **panic** | 1 | 3 | - | 384.51 | - | 2,899 | - | 0.000462 | 🔵 low — common in general English | — |
| 3307 | **ball** | 1 | 3 | - | 384.51 | - | 2,900 | - | 0.000462 | 🔵 low — common in general English | — |
| 3308 | **topped** | 1 | 3 | - | 384.51 | - | 2,901 | - | 0.000462 | 🔵 low — common in general English | — |
| 3309 | **our** | 1 | 5 | - | 383.71 | - | 2,902 | - | 0.000462 | 🔵 low — common in general English | — |
| 3310 | **predicted** | 1 | 4 | - | 382.34 | - | 2,903 | - | 0.000462 | 🔵 low — common in general English | — |
| 3311 | **placing** | 1 | 3 | - | 381.70 | - | 2,904 | - | 0.000462 | 🔵 low — common in general English | — |
| 3312 | **removed** | 1 | 3 | - | 381.70 | - | 2,905 | - | 0.000462 | 🔵 low — common in general English | — |
| 3313 | **successive** | 1 | 3 | - | 381.70 | - | 2,906 | - | 0.000462 | 🔵 low — common in general English | — |
| 3314 | **crushing** | 1 | 3 | - | 381.70 | - | 2,907 | - | 0.000461 | 🔵 low — common in general English | — |
| 3315 | **argument** | 1 | 3 | - | 381.70 | - | 2,908 | - | 0.000461 | 🔵 low — common in general English | — |
| 3316 | **progressive** | 1 | 3 | - | 381.70 | - | 2,909 | - | 0.000461 | 🔵 low — common in general English | — |
| 3317 | **violated** | 1 | 3 | - | 381.70 | - | 2,910 | - | 0.000461 | 🔵 low — common in general English | — |
| 3318 | **counter** | 1 | 3 | - | 379.03 | - | 2,912 | - | 0.000461 | 🔵 low — common in general English | — |
| 3319 | **specifically** | 1 | 3 | - | 379.03 | - | 2,913 | - | 0.000461 | 🔵 low — common in general English | — |
| 3320 | **quantity** | 1 | 3 | - | 379.03 | - | 2,914 | - | 0.000461 | 🔵 low — common in general English | — |
| 3321 | **eliminated** | 1 | 3 | - | 379.03 | - | 2,915 | - | 0.000461 | 🔵 low — common in general English | — |
| 3322 | **preventing** | 1 | 3 | - | 376.50 | - | 2,916 | - | 0.000460 | 🔵 low — common in general English | — |
| 3323 | **season** | 1 | 4 | - | 376.16 | - | 2,918 | - | 0.000460 | 🔵 low — common in general English | — |
| 3324 | **category** | 1 | 3 | - | 374.08 | - | 2,920 | - | 0.000460 | 🔵 low — common in general English | — |
| 3325 | **limit** | 1 | 4 | - | 373.52 | - | 2,921 | - | 0.000460 | 🔵 low — common in general English | — |
| 3326 | **entry** | 1 | 3 | - | 371.77 | - | 2,922 | - | 0.000460 | 🔵 low — common in general English | — |
| 3327 | **picture** | 1 | 3 | - | 371.77 | - | 2,923 | - | 0.000460 | 🔵 low — common in general English | — |
| 3328 | **associate** | 1 | 3 | - | 371.77 | - | 2,924 | - | 0.000460 | 🔵 low — common in general English | — |
| 3329 | **introduce** | 1 | 3 | - | 371.77 | - | 2,925 | - | 0.000459 | 🔵 low — common in general English | — |
| 3330 | **argue** | 1 | 3 | - | 369.55 | - | 2,926 | - | 0.000459 | 🔵 low — common in general English | — |
| 3331 | **earned** | 1 | 4 | - | 368.53 | - | 2,927 | - | 0.000459 | 🔵 low — common in general English | — |
| 3332 | **history** | 1 | 3 | - | 367.43 | - | 2,928 | - | 0.000459 | 🔵 low — common in general English | — |
| 3333 | **assume** | 1 | 3 | - | 365.39 | - | 2,929 | - | 0.000459 | 🔵 low — common in general English | — |
| 3334 | **win** | 1 | 3 | - | 363.43 | - | 2,931 | - | 0.000459 | 🔵 low — common in general English | — |
| 3335 | **secure** | 1 | 3 | - | 363.43 | - | 2,932 | - | 0.000459 | 🔵 low — common in general English | — |
| 3336 | **midday** | 1 | 3 | - | 361.54 | - | 2,934 | - | 0.000458 | 🔵 low — common in general English | — |
| 3337 | **subsequent** | 1 | 3 | - | 361.54 | - | 2,935 | - | 0.000458 | 🔵 low — common in general English | — |
| 3338 | **severely** | 1 | 3 | - | 361.54 | - | 2,936 | - | 0.000458 | 🔵 low — common in general English | — |
| 3339 | **brief** | 1 | 3 | - | 359.71 | - | 2,938 | - | 0.000458 | 🔵 low — common in general English | — |
| 3340 | **ran** | 1 | 3 | - | 359.71 | - | 2,939 | - | 0.000458 | 🔵 low — common in general English | — |
| 3341 | **send** | 1 | 3 | - | 359.71 | - | 2,940 | - | 0.000458 | 🔵 low — common in general English | — |
| 3342 | **assuming** | 1 | 3 | - | 357.95 | - | 2,943 | - | 0.000457 | 🔵 low — common in general English | — |
| 3343 | **prove** | 1 | 3 | - | 356.25 | - | 2,945 | - | 0.000457 | 🔵 low — common in general English | — |
| 3344 | **increasing** | 1 | 4 | - | 355.42 | - | 2,946 | - | 0.000457 | 🔵 low — common in general English | — |
| 3345 | **warning** | 1 | 3 | - | 354.60 | - | 2,947 | - | 0.000457 | 🔵 low — common in general English | — |
| 3346 | **proportion** | 1 | 3 | - | 354.60 | - | 2,948 | - | 0.000457 | 🔵 low — common in general English | — |
| 3347 | **urge** | 1 | 3 | - | 353.00 | - | 2,950 | - | 0.000457 | 🔵 low — common in general English | — |
| 3348 | **resolution** | 1 | 3 | - | 353.00 | - | 2,951 | - | 0.000457 | 🔵 low — common in general English | — |
| 3349 | **floating** | 1 | 3 | - | 348.47 | - | 2,953 | - | 0.000456 | 🔵 low — common in general English | — |
| 3350 | **environment** | 1 | 3 | - | 348.47 | - | 2,954 | - | 0.000456 | 🔵 low — common in general English | — |
| 3351 | **repayment** | 1 | 3 | - | 348.47 | - | 2,955 | - | 0.000456 | 🔵 low — common in general English | — |
| 3352 | **aggressive** | 1 | 3 | - | 348.47 | - | 2,956 | - | 0.000456 | 🔵 low — common in general English | — |
| 3353 | **acting** | 1 | 3 | - | 348.47 | - | 2,957 | - | 0.000456 | 🔵 low — common in general English | — |
| 3354 | **figure** | 1 | 4 | - | 347.87 | - | 2,959 | - | 0.000456 | 🔵 low — common in general English | — |
| 3355 | **resist** | 1 | 3 | - | 347.05 | - | 2,961 | - | 0.000455 | 🔵 low — common in general English | — |
| 3356 | **managed** | 1 | 3 | - | 345.66 | - | 2,962 | - | 0.000455 | 🔵 low — common in general English | — |
| 3357 | **changing** | 1 | 3 | - | 345.66 | - | 2,963 | - | 0.000455 | 🔵 low — common in general English | — |
| 3358 | **aware** | 1 | 3 | - | 345.66 | - | 2,964 | - | 0.000455 | 🔵 low — common in general English | — |
| 3359 | **shut** | 1 | 3 | - | 341.71 | - | 2,967 | - | 0.000455 | 🔵 low — common in general English | — |
| 3360 | **suffered** | 1 | 3 | - | 341.71 | - | 2,969 | - | 0.000455 | 🔵 low — common in general English | — |
| 3361 | **joined** | 1 | 3 | - | 340.46 | - | 2,970 | - | 0.000454 | 🔵 low — common in general English | — |
| 3362 | **joint** | 1 | 4 | - | 338.53 | - | 2,971 | - | 0.000454 | 🔵 low — common in general English | — |
| 3363 | **apparent** | 1 | 3 | - | 338.04 | - | 2,972 | - | 0.000454 | 🔵 low — common in general English | — |
| 3364 | **pointed** | 1 | 3 | - | 338.04 | - | 2,973 | - | 0.000454 | 🔵 low — common in general English | — |
| 3365 | **delivered** | 1 | 3 | - | 336.87 | - | 2,974 | - | 0.000454 | 🔵 low — common in general English | — |
| 3366 | **outcome** | 1 | 3 | - | 336.87 | - | 2,975 | - | 0.000454 | 🔵 low — common in general English | — |
| 3367 | **scale** | 1 | 3 | - | 335.73 | - | 2,976 | - | 0.000454 | 🔵 low — common in general English | — |
| 3368 | **attractive** | 1 | 3 | - | 335.73 | - | 2,977 | - | 0.000454 | 🔵 low — common in general English | — |
| 3369 | **adequate** | 1 | 3 | - | 334.61 | - | 2,979 | - | 0.000453 | 🔵 low — common in general English | — |
| 3370 | **favour** | 1 | 3 | - | 334.61 | - | 2,980 | - | 0.000453 | 🔵 low — common in general English | — |
| 3371 | **repeated** | 1 | 3 | - | 334.61 | - | 2,981 | - | 0.000453 | 🔵 low — common in general English | — |
| 3372 | **requested** | 1 | 3 | - | 333.52 | - | 2,982 | - | 0.000453 | 🔵 low — common in general English | — |
| 3373 | **citadel** | 1 | 2 | - | 332.49 | - | 2,983 | - | 0.000453 | 🔵 low — common in general English | — |
| 3374 | **bounty** | 1 | 2 | - | 332.49 | - | 2,984 | - | 0.000453 | 🔵 low — common in general English | — |
| 3375 | **savage** | 1 | 2 | - | 332.49 | - | 2,985 | - | 0.000453 | 🔵 low — common in general English | — |
| 3376 | **hindrance** | 1 | 2 | - | 332.49 | - | 2,986 | - | 0.000453 | 🔵 low — common in general English | — |
| 3377 | **totality** | 1 | 2 | - | 332.49 | - | 2,987 | - | 0.000453 | 🔵 low — common in general English | — |
| 3378 | **populated** | 1 | 2 | - | 332.49 | - | 2,988 | - | 0.000452 | 🔵 low — common in general English | — |
| 3379 | **striving** | 1 | 2 | - | 332.49 | - | 2,989 | - | 0.000452 | 🔵 low — common in general English | — |
| 3380 | **sway** | 1 | 2 | - | 332.49 | - | 2,990 | - | 0.000452 | 🔵 low — common in general English | — |
| 3381 | **motive** | 1 | 2 | - | 332.49 | - | 2,991 | - | 0.000452 | 🔵 low — common in general English | — |
| 3382 | **genuinely** | 1 | 2 | - | 332.49 | - | 2,992 | - | 0.000452 | 🔵 low — common in general English | — |
| 3383 | **draught** | 1 | 2 | - | 332.49 | - | 2,993 | - | 0.000452 | 🔵 low — common in general English | — |
| 3384 | **encompassing** | 1 | 2 | - | 332.49 | - | 2,994 | - | 0.000452 | 🔵 low — common in general English | — |
| 3385 | **depart** | 1 | 2 | - | 332.49 | - | 2,995 | - | 0.000452 | 🔵 low — common in general English | — |
| 3386 | **pale** | 1 | 2 | - | 332.49 | - | 2,996 | - | 0.000452 | 🔵 low — common in general English | — |
| 3387 | **warrior** | 1 | 2 | - | 332.49 | - | 2,997 | - | 0.000452 | 🔵 low — common in general English | — |
| 3388 | **prison** | 1 | 2 | - | 332.49 | - | 2,998 | - | 0.000451 | 🔵 low — common in general English | — |
| 3389 | **miserable** | 1 | 2 | - | 332.49 | - | 2,999 | - | 0.000451 | 🔵 low — common in general English | — |
| 3390 | **meagre** | 1 | 2 | - | 332.49 | - | 3,000 | - | 0.000451 | 🔵 low — common in general English | — |
| 3391 | **momentary** | 1 | 2 | - | 332.49 | - | 3,001 | - | 0.000451 | 🔵 low — common in general English | — |
| 3392 | **unrelenting** | 1 | 2 | - | 332.49 | - | 3,002 | - | 0.000451 | 🔵 low — common in general English | — |
| 3393 | **axe** | 1 | 2 | - | 332.49 | - | 3,003 | - | 0.000451 | 🔵 low — common in general English | — |
| 3394 | **pretend** | 1 | 2 | - | 332.49 | - | 3,004 | - | 0.000451 | 🔵 low — common in general English | — |
| 3395 | **jar** | 1 | 2 | - | 332.49 | - | 3,005 | - | 0.000451 | 🔵 low — common in general English | — |
| 3396 | **storey** | 1 | 2 | - | 332.49 | - | 3,006 | - | 0.000451 | 🔵 low — common in general English | — |
| 3397 | **reviving** | 1 | 2 | - | 332.49 | - | 3,007 | - | 0.000450 | 🔵 low — common in general English | — |
| 3398 | **screaming** | 1 | 2 | - | 332.49 | - | 3,008 | - | 0.000450 | 🔵 low — common in general English | — |
| 3399 | **sealed** | 1 | 2 | - | 332.49 | - | 3,009 | - | 0.000450 | 🔵 low — common in general English | — |
| 3400 | **stabbed** | 1 | 2 | - | 332.49 | - | 3,010 | - | 0.000450 | 🔵 low — common in general English | — |
| 3401 | **cracked** | 1 | 2 | - | 332.49 | - | 3,011 | - | 0.000450 | 🔵 low — common in general English | — |
| 3402 | **boiling** | 1 | 2 | - | 332.49 | - | 3,012 | - | 0.000450 | 🔵 low — common in general English | — |
| 3403 | **weep** | 1 | 2 | - | 332.49 | - | 3,013 | - | 0.000450 | 🔵 low — common in general English | — |
| 3404 | **deceased** | 1 | 2 | - | 332.49 | - | 3,014 | - | 0.000450 | 🔵 low — common in general English | — |
| 3405 | **rib** | 1 | 2 | - | 332.49 | - | 3,015 | - | 0.000450 | 🔵 low — common in general English | — |
| 3406 | **hauled** | 1 | 2 | - | 332.49 | - | 3,016 | - | 0.000449 | 🔵 low — common in general English | — |
| 3407 | **arrogant** | 1 | 2 | - | 332.49 | - | 3,017 | - | 0.000449 | 🔵 low — common in general English | — |
| 3408 | **stuff** | 1 | 2 | - | 332.49 | - | 3,018 | - | 0.000449 | 🔵 low — common in general English | — |
| 3409 | **ploughed** | 1 | 2 | - | 332.49 | - | 3,019 | - | 0.000449 | 🔵 low — common in general English | — |
| 3410 | **halfway** | 1 | 2 | - | 332.49 | - | 3,020 | - | 0.000449 | 🔵 low — common in general English | — |
| 3411 | **jaw** | 1 | 2 | - | 332.49 | - | 3,021 | - | 0.000449 | 🔵 low — common in general English | — |
| 3412 | **chew** | 1 | 2 | - | 332.49 | - | 3,022 | - | 0.000449 | 🔵 low — common in general English | — |
| 3413 | **clutch** | 1 | 2 | - | 332.49 | - | 3,023 | - | 0.000449 | 🔵 low — common in general English | — |
| 3414 | **burglar** | 1 | 2 | - | 332.49 | - | 3,024 | - | 0.000449 | 🔵 low — common in general English | — |
| 3415 | **haven** | 1 | 2 | - | 332.49 | - | 3,025 | - | 0.000449 | 🔵 low — common in general English | — |
| 3416 | **confer** | 1 | 2 | - | 332.49 | - | 3,026 | - | 0.000448 | 🔵 low — common in general English | — |
| 3417 | **irresistible** | 1 | 2 | - | 332.49 | - | 3,027 | - | 0.000448 | 🔵 low — common in general English | — |
| 3418 | **abyss** | 1 | 2 | - | 332.49 | - | 3,028 | - | 0.000448 | 🔵 low — common in general English | — |
| 3419 | **wit** | 1 | 2 | - | 332.49 | - | 3,029 | - | 0.000448 | 🔵 low — common in general English | — |
| 3420 | **dress** | 1 | 2 | - | 332.49 | - | 3,030 | - | 0.000448 | 🔵 low — common in general English | — |
| 3421 | **progression** | 1 | 2 | - | 332.49 | - | 3,031 | - | 0.000448 | 🔵 low — common in general English | — |
| 3422 | **feeble** | 1 | 2 | - | 332.49 | - | 3,032 | - | 0.000448 | 🔵 low — common in general English | — |
| 3423 | **secretly** | 1 | 2 | - | 332.49 | - | 3,033 | - | 0.000448 | 🔵 low — common in general English | — |
| 3424 | **prowess** | 1 | 2 | - | 332.49 | - | 3,034 | - | 0.000448 | 🔵 low — common in general English | — |
| 3425 | **renunciation** | 1 | 2 | - | 332.49 | - | 3,035 | - | 0.000447 | 🔵 low — common in general English | — |
| 3426 | **exposing** | 1 | 2 | - | 332.49 | - | 3,036 | - | 0.000447 | 🔵 low — common in general English | — |
| 3427 | **observation** | 1 | 2 | - | 332.49 | - | 3,037 | - | 0.000447 | 🔵 low — common in general English | — |
| 3428 | **bother** | 1 | 2 | - | 332.49 | - | 3,038 | - | 0.000447 | 🔵 low — common in general English | — |
| 3429 | **creator** | 1 | 2 | - | 332.49 | - | 3,039 | - | 0.000447 | 🔵 low — common in general English | — |
| 3430 | **abstain** | 1 | 2 | - | 332.49 | - | 3,040 | - | 0.000447 | 🔵 low — common in general English | — |
| 3431 | **pleasantly** | 1 | 2 | - | 332.49 | - | 3,041 | - | 0.000447 | 🔵 low — common in general English | — |
| 3432 | **respectful** | 1 | 2 | - | 332.49 | - | 3,042 | - | 0.000447 | 🔵 low — common in general English | — |
| 3433 | **headache** | 1 | 2 | - | 332.49 | - | 3,043 | - | 0.000447 | 🔵 low — common in general English | — |
| 3434 | **saffron** | 1 | 2 | - | 332.49 | - | 3,044 | - | 0.000447 | 🔵 low — common in general English | — |
| 3435 | **dense** | 1 | 2 | - | 332.49 | - | 3,045 | - | 0.000446 | 🔵 low — common in general English | — |
| 3436 | **maturation** | 1 | 2 | - | 332.49 | - | 3,047 | - | 0.000446 | 🔵 low — common in general English | — |
| 3437 | **corrupted** | 1 | 2 | - | 332.49 | - | 3,048 | - | 0.000446 | 🔵 low — common in general English | — |
| 3438 | **needing** | 1 | 2 | - | 332.49 | - | 3,049 | - | 0.000446 | 🔵 low — common in general English | — |
| 3439 | **discrimination** | 1 | 2 | - | 332.49 | - | 3,050 | - | 0.000446 | 🔵 low — common in general English | — |
| 3440 | **rebuke** | 1 | 2 | - | 332.49 | - | 3,051 | - | 0.000446 | 🔵 low — common in general English | — |
| 3441 | **embarrassed** | 1 | 2 | - | 332.49 | - | 3,052 | - | 0.000446 | 🔵 low — common in general English | — |
| 3442 | **irritated** | 1 | 2 | - | 332.49 | - | 3,053 | - | 0.000446 | 🔵 low — common in general English | — |
| 3443 | **receptive** | 1 | 2 | - | 332.49 | - | 3,054 | - | 0.000446 | 🔵 low — common in general English | — |
| 3444 | **externally** | 1 | 2 | - | 332.49 | - | 3,055 | - | 0.000445 | 🔵 low — common in general English | — |
| 3445 | **requisite** | 1 | 2 | - | 332.49 | - | 3,056 | - | 0.000445 | 🔵 low — common in general English | — |
| 3446 | **invoke** | 1 | 2 | - | 332.49 | - | 3,057 | - | 0.000445 | 🔵 low — common in general English | — |
| 3447 | **underwent** | 1 | 2 | - | 332.49 | - | 3,058 | - | 0.000445 | 🔵 low — common in general English | — |
| 3448 | **angrily** | 1 | 2 | - | 332.49 | - | 3,059 | - | 0.000445 | 🔵 low — common in general English | — |
| 3449 | **remembered** | 1 | 2 | - | 332.49 | - | 3,060 | - | 0.000445 | 🔵 low — common in general English | — |
| 3450 | **melted** | 1 | 2 | - | 332.49 | - | 3,061 | - | 0.000445 | 🔵 low — common in general English | — |
| 3451 | **distinctly** | 1 | 2 | - | 332.49 | - | 3,062 | - | 0.000445 | 🔵 low — common in general English | — |
| 3452 | **flash** | 1 | 2 | - | 332.49 | - | 3,063 | - | 0.000445 | 🔵 low — common in general English | — |
| 3453 | **continuity** | 1 | 2 | - | 332.49 | - | 3,064 | - | 0.000444 | 🔵 low — common in general English | — |
| 3454 | **self-centred** | 1 | 2 | - | 332.49 | - | 3,065 | - | 0.000444 | 🔵 low — common in general English | — |
| 3455 | **indifferent** | 1 | 2 | - | 332.49 | - | 3,066 | - | 0.000444 | 🔵 low — common in general English | — |
| 3456 | **perished** | 1 | 2 | - | 332.49 | - | 3,067 | - | 0.000444 | 🔵 low — common in general English | — |
| 3457 | **nurtured** | 1 | 2 | - | 332.49 | - | 3,068 | - | 0.000444 | 🔵 low — common in general English | — |
| 3458 | **kicked** | 1 | 2 | - | 332.49 | - | 3,069 | - | 0.000444 | 🔵 low — common in general English | — |
| 3459 | **wrecked** | 1 | 2 | - | 332.49 | - | 3,070 | - | 0.000444 | 🔵 low — common in general English | — |
| 3460 | **avail** | 1 | 2 | - | 332.49 | - | 3,071 | - | 0.000444 | 🔵 low — common in general English | — |
| 3461 | **chariot** | 1 | 2 | - | 332.49 | - | 3,072 | - | 0.000444 | 🔵 low — common in general English | — |
| 3462 | **oar** | 1 | 2 | - | 332.49 | - | 3,073 | - | 0.000444 | 🔵 low — common in general English | — |
| 3463 | **twenty-three** | 1 | 2 | - | 332.49 | - | 3,074 | - | 0.000443 | 🔵 low — common in general English | — |
| 3464 | **doha** | 1 | 2 | - | 332.49 | - | 3,075 | - | 0.000443 | 🔵 low — common in general English | ✓ |
| 3465 | **engender** | 1 | 2 | - | 332.49 | - | 3,076 | - | 0.000443 | 🔵 low — common in general English | — |
| 3466 | **fore** | 1 | 2 | - | 332.49 | - | 3,077 | - | 0.000443 | 🔵 low — common in general English | — |
| 3467 | **dirt** | 1 | 2 | - | 332.49 | - | 3,078 | - | 0.000443 | 🔵 low — common in general English | — |
| 3468 | **aggressor** | 1 | 2 | - | 332.49 | - | 3,079 | - | 0.000443 | 🔵 low — common in general English | — |
| 3469 | **observing** | 1 | 2 | - | 332.49 | - | 3,080 | - | 0.000443 | 🔵 low — common in general English | — |
| 3470 | **emptied** | 1 | 2 | - | 332.49 | - | 3,081 | - | 0.000443 | 🔵 low — common in general English | — |
| 3471 | **beam** | 1 | 2 | - | 332.49 | - | 3,082 | - | 0.000443 | 🔵 low — common in general English | — |
| 3472 | **vibrant** | 1 | 2 | - | 332.49 | - | 3,083 | - | 0.000443 | 🔵 low — common in general English | — |
| 3473 | **revitalize** | 1 | 2 | - | 332.49 | - | 3,084 | - | 0.000442 | 🔵 low — common in general English | — |
| 3474 | **guarantee** | 1 | 3 | - | 332.44 | - | 3,085 | - | 0.000442 | 🔵 low — common in general English | — |
| 3475 | **exhaustion** | 1 | 2 | - | 332.39 | - | 3,086 | - | 0.000442 | 🔵 low — common in general English | ~ |
| 3476 | **unerring** | 1 | 2 | - | 332.39 | - | 3,087 | - | 0.000442 | 🔵 low — common in general English | — |
| 3477 | **greatness** | 1 | 2 | - | 332.39 | - | 3,088 | - | 0.000442 | 🔵 low — common in general English | — |
| 3478 | **permeate** | 1 | 2 | - | 332.39 | - | 3,089 | - | 0.000442 | 🔵 low — common in general English | — |
| 3479 | **semblance** | 1 | 2 | - | 332.39 | - | 3,090 | - | 0.000442 | 🔵 low — common in general English | — |
| 3480 | **daka** | 1 | 2 | - | 332.39 | - | 3,091 | - | 0.000442 | 🔵 low — common in general English | ✓ དཔའ་བོ |
| 3481 | **blissful** | 1 | 2 | - | 332.39 | - | 3,092 | - | 0.000442 | 🔵 low — common in general English | ~ |
| 3482 | **eternity** | 1 | 2 | - | 332.39 | - | 3,093 | - | 0.000442 | 🔵 low — common in general English | — |
| 3483 | **concealed** | 1 | 2 | - | 332.39 | - | 3,094 | - | 0.000441 | 🔵 low — common in general English | — |
| 3484 | **upside-down** | 1 | 2 | - | 332.39 | - | 3,095 | - | 0.000441 | 🔵 low — common in general English | — |
| 3485 | **nomad** | 1 | 2 | - | 332.39 | - | 3,096 | - | 0.000441 | 🔵 low — common in general English | — |
| 3486 | **savouring** | 1 | 2 | - | 332.39 | - | 3,097 | - | 0.000441 | 🔵 low — common in general English | — |
| 3487 | **vina** | 1 | 2 | - | 332.39 | - | 3,098 | - | 0.000441 | 🔵 low — common in general English | ✓ |
| 3488 | **tingling** | 1 | 2 | - | 332.39 | - | 3,099 | - | 0.000441 | 🔵 low — common in general English | — |
| 3489 | **intently** | 1 | 2 | - | 332.39 | - | 3,100 | - | 0.000441 | 🔵 low — common in general English | — |
| 3490 | **razor-sharp** | 1 | 2 | - | 332.39 | - | 3,101 | - | 0.000441 | 🔵 low — common in general English | — |
| 3491 | **tising** | 1 | 2 | - | 332.39 | - | 3,102 | - | 0.000441 | 🔵 low — common in general English | — |
| 3492 | **ti-reciter** | 1 | 2 | - | 332.39 | - | 3,103 | - | 0.000441 | 🔵 low — common in general English | — |
| 3493 | **honest** | 1 | 2 | - | 332.39 | - | 3,104 | - | 0.000440 | 🔵 low — common in general English | — |
| 3494 | **i-reciter** | 1 | 2 | - | 332.39 | - | 3,105 | - | 0.000440 | 🔵 low — common in general English | — |
| 3495 | **fruition** | 1 | 2 | - | 332.39 | - | 3,106 | - | 0.000440 | 🔵 low — common in general English | — |
| 3496 | **sror** | 1 | 2 | - | 332.39 | - | 3,107 | - | 0.000440 | 🔵 low — common in general English | — |
| 3497 | **taut** | 1 | 2 | - | 332.39 | - | 3,108 | - | 0.000440 | 🔵 low — common in general English | — |
| 3498 | **inwardly** | 1 | 2 | - | 332.39 | - | 3,109 | - | 0.000440 | 🔵 low — common in general English | — |
| 3499 | **discour** | 1 | 2 | - | 332.39 | - | 3,110 | - | 0.000440 | 🔵 low — common in general English | — |
| 3500 | **mealtime** | 1 | 2 | - | 332.39 | - | 3,111 | - | 0.000440 | 🔵 low — common in general English | — |
| 3501 | **undervalue** | 1 | 2 | - | 332.39 | - | 3,112 | - | 0.000440 | 🔵 low — common in general English | — |
| 3502 | **disobeying** | 1 | 2 | - | 332.39 | - | 3,113 | - | 0.000440 | 🔵 low — common in general English | — |
| 3503 | **treating** | 1 | 2 | - | 332.39 | - | 3,114 | - | 0.000439 | 🔵 low — common in general English | — |
| 3504 | **iala** | 1 | 2 | - | 332.39 | - | 3,115 | - | 0.000439 | 🔵 low — common in general English | — |
| 3505 | **disrespectful** | 1 | 2 | - | 332.39 | - | 3,116 | - | 0.000439 | 🔵 low — common in general English | — |
| 3506 | **barbarian** | 1 | 2 | - | 332.39 | - | 3,117 | - | 0.000439 | 🔵 low — common in general English | — |
| 3507 | **slavery** | 1 | 2 | - | 332.39 | - | 3,118 | - | 0.000439 | 🔵 low — common in general English | — |
| 3508 | **blankness** | 1 | 2 | - | 332.39 | - | 3,119 | - | 0.000439 | 🔵 low — common in general English | — |
| 3509 | **inhabiting** | 1 | 2 | - | 332.39 | - | 3,120 | - | 0.000439 | 🔵 low — common in general English | — |
| 3510 | **eternalist** | 1 | 2 | - | 332.39 | - | 3,121 | - | 0.000439 | 🔵 low — common in general English | — |
| 3511 | **nihilist** | 1 | 2 | - | 332.39 | - | 3,122 | - | 0.000439 | 🔵 low — common in general English | — |
| 3512 | **tenma** | 1 | 2 | - | 332.39 | - | 3,123 | - | 0.000439 | 🔵 low — common in general English | ✓ རྟེན་མ་བཅུ་གཉིས |
| 3513 | **flower-garden** | 1 | 2 | - | 332.39 | - | 3,124 | - | 0.000438 | 🔵 low — common in general English | — |
| 3514 | **expounding** | 1 | 2 | - | 332.39 | - | 3,125 | - | 0.000438 | 🔵 low — common in general English | — |
| 3515 | **description** | 1 | 2 | - | 332.39 | - | 3,126 | - | 0.000438 | 🔵 low — common in general English | — |
| 3516 | **disability** | 1 | 2 | - | 332.39 | - | 3,127 | - | 0.000438 | 🔵 low — common in general English | — |
| 3517 | **possessing** | 1 | 2 | - | 332.39 | - | 3,128 | - | 0.000438 | 🔵 low — common in general English | — |
| 3518 | **immersed** | 1 | 2 | - | 332.39 | - | 3,129 | - | 0.000438 | 🔵 low — common in general English | — |
| 3519 | **variance** | 1 | 2 | - | 332.39 | - | 3,130 | - | 0.000438 | 🔵 low — common in general English | — |
| 3520 | **prophecy** | 1 | 2 | - | 332.39 | - | 3,131 | - | 0.000438 | 🔵 low — common in general English | — |
| 3521 | **thonmi** | 1 | 2 | - | 332.39 | - | 3,132 | - | 0.000438 | 🔵 low — common in general English | — |
| 3522 | **sambhota** | 1 | 2 | - | 332.39 | - | 3,133 | - | 0.000438 | 🔵 low — common in general English | — |
| 3523 | **owo** | 1 | 2 | - | 332.39 | - | 3,134 | - | 0.000437 | 🔵 low — common in general English | — |
| 3524 | **thadul** | 1 | 2 | - | 332.39 | - | 3,135 | - | 0.000437 | 🔵 low — common in general English | — |
| 3525 | **yangdul** | 1 | 2 | - | 332.39 | - | 3,136 | - | 0.000437 | 🔵 low — common in general English | — |
| 3526 | **buddhism** | 1 | 2 | - | 332.39 | - | 3,137 | - | 0.000437 | 🔵 low — common in general English | — |
| 3527 | **unequalled** | 1 | 2 | - | 332.39 | - | 3,138 | - | 0.000437 | 🔵 low — common in general English | — |
| 3528 | **sfitra** | 1 | 2 | - | 332.39 | - | 3,139 | - | 0.000437 | 🔵 low — common in general English | — |
| 3529 | **ordained** | 1 | 2 | - | 332.39 | - | 3,140 | - | 0.000437 | 🔵 low — common in general English | — |
| 3530 | **shone** | 1 | 2 | - | 332.39 | - | 3,141 | - | 0.000437 | 🔵 low — common in general English | — |
| 3531 | **kind-hearted** | 1 | 2 | - | 332.39 | - | 3,142 | - | 0.000437 | 🔵 low — common in general English | — |
| 3532 | **delightful** | 1 | 2 | - | 332.39 | - | 3,143 | - | 0.000437 | 🔵 low — common in general English | — |
| 3533 | **renown** | 1 | 2 | - | 332.39 | - | 3,144 | - | 0.000437 | 🔵 low — common in general English | — |
| 3534 | **manifesting** | 1 | 2 | - | 332.39 | - | 3,145 | - | 0.000436 | 🔵 low — common in general English | — |
| 3535 | **devoid** | 1 | 2 | - | 332.39 | - | 3,146 | - | 0.000436 | 🔵 low — common in general English | — |
| 3536 | **quench** | 1 | 2 | - | 332.39 | - | 3,147 | - | 0.000436 | 🔵 low — common in general English | — |
| 3537 | **excellence** | 1 | 2 | - | 332.39 | - | 3,148 | - | 0.000436 | 🔵 low — common in general English | — |
| 3538 | **khu** | 1 | 2 | - | 332.39 | - | 3,149 | - | 0.000436 | 🔵 low — common in general English | ~ |
| 3539 | **ngok** | 1 | 2 | - | 332.39 | - | 3,150 | - | 0.000436 | 🔵 low — common in general English | ~ |
| 3540 | **stupidity** | 1 | 2 | - | 332.39 | - | 3,151 | - | 0.000436 | 🔵 low — common in general English | — |
| 3541 | **ensnared** | 1 | 2 | - | 332.39 | - | 3,152 | - | 0.000436 | 🔵 low — common in general English | — |
| 3542 | **guise** | 1 | 2 | - | 332.39 | - | 3,153 | - | 0.000436 | 🔵 low — common in general English | — |
| 3543 | **blindly** | 1 | 2 | - | 332.39 | - | 3,154 | - | 0.000436 | 🔵 low — common in general English | — |
| 3544 | **tinder** | 1 | 2 | - | 332.39 | - | 3,155 | - | 0.000435 | 🔵 low — common in general English | — |
| 3545 | **oxen** | 1 | 2 | - | 332.39 | - | 3,156 | - | 0.000435 | 🔵 low — common in general English | — |
| 3546 | **hither** | 1 | 2 | - | 332.39 | - | 3,157 | - | 0.000435 | 🔵 low — common in general English | — |
| 3547 | **thither** | 1 | 2 | - | 332.39 | - | 3,158 | - | 0.000435 | 🔵 low — common in general English | — |
| 3548 | **intentionally** | 1 | 2 | - | 332.39 | - | 3,159 | - | 0.000435 | 🔵 low — common in general English | — |
| 3549 | **hurl** | 1 | 2 | - | 332.39 | - | 3,160 | - | 0.000435 | 🔵 low — common in general English | — |
| 3550 | **neglect** | 1 | 2 | - | 332.39 | - | 3,161 | - | 0.000435 | 🔵 low — common in general English | — |
| 3551 | **indulging** | 1 | 2 | - | 332.39 | - | 3,162 | - | 0.000435 | 🔵 low — common in general English | — |
| 3552 | **pond** | 1 | 2 | - | 332.39 | - | 3,163 | - | 0.000435 | 🔵 low — common in general English | — |
| 3553 | **blaz** | 1 | 2 | - | 332.39 | - | 3,164 | - | 0.000435 | 🔵 low — common in general English | — |
| 3554 | **infernal** | 1 | 2 | - | 332.39 | - | 3,165 | - | 0.000434 | 🔵 low — common in general English | — |
| 3555 | **disintegrate** | 1 | 2 | - | 332.39 | - | 3,166 | - | 0.000434 | 🔵 low — common in general English | — |
| 3556 | **legion** | 1 | 2 | - | 332.39 | - | 3,167 | - | 0.000434 | 🔵 low — common in general English | — |
| 3557 | **wondrous** | 1 | 2 | - | 332.39 | - | 3,168 | - | 0.000434 | 🔵 low — common in general English | — |
| 3558 | **livelihood** | 1 | 2 | - | 332.39 | - | 3,169 | - | 0.000434 | 🔵 low — common in general English | — |
| 3559 | **ferociously** | 1 | 2 | - | 332.39 | - | 3,170 | - | 0.000434 | 🔵 low — common in general English | — |
| 3560 | **soldier** | 1 | 2 | - | 332.39 | - | 3,171 | - | 0.000434 | 🔵 low — common in general English | — |
| 3561 | **breadth** | 1 | 2 | - | 332.39 | - | 3,172 | - | 0.000434 | 🔵 low — common in general English | — |
| 3562 | **limp** | 1 | 2 | - | 332.39 | - | 3,173 | - | 0.000434 | 🔵 low — common in general English | — |
| 3563 | **filthy** | 1 | 2 | - | 332.39 | - | 3,175 | - | 0.000434 | 🔵 low — common in general English | — |
| 3564 | **magnificent** | 1 | 2 | - | 332.39 | - | 3,176 | - | 0.000433 | 🔵 low — common in general English | — |
| 3565 | **five-fold** | 1 | 2 | - | 332.39 | - | 3,177 | - | 0.000433 | 🔵 low — common in general English | — |
| 3566 | **nyatri** | 1 | 2 | - | 332.39 | - | 3,178 | - | 0.000433 | 🔵 low — common in general English | — |
| 3567 | **splendour** | 1 | 2 | - | 332.39 | - | 3,180 | - | 0.000433 | 🔵 low — common in general English | — |
| 3568 | **prize** | 1 | 2 | - | 332.39 | - | 3,181 | - | 0.000433 | 🔵 low — common in general English | — |
| 3569 | **tall** | 1 | 2 | - | 332.39 | - | 3,182 | - | 0.000433 | 🔵 low — common in general English | — |
| 3570 | **degenerated** | 1 | 2 | - | 332.39 | - | 3,183 | - | 0.000433 | 🔵 low — common in general English | — |
| 3571 | **plague** | 1 | 2 | - | 332.39 | - | 3,184 | - | 0.000433 | 🔵 low — common in general English | — |
| 3572 | **survivor** | 1 | 2 | - | 332.39 | - | 3,185 | - | 0.000433 | 🔵 low — common in general English | — |
| 3573 | **preach** | 1 | 2 | - | 332.39 | - | 3,186 | - | 0.000432 | 🔵 low — common in general English | — |
| 3574 | **glow** | 1 | 2 | - | 332.39 | - | 3,187 | - | 0.000432 | 🔵 low — common in general English | — |
| 3575 | **blossom** | 1 | 2 | - | 332.39 | - | 3,188 | - | 0.000432 | 🔵 low — common in general English | — |
| 3576 | **wither** | 1 | 2 | - | 332.39 | - | 3,189 | - | 0.000432 | 🔵 low — common in general English | — |
| 3577 | **goat** | 1 | 2 | - | 332.39 | - | 3,190 | - | 0.000432 | 🔵 low — common in general English | — |
| 3578 | **thunderbolt** | 1 | 2 | - | 332.39 | - | 3,191 | - | 0.000432 | 🔵 low — common in general English | — |
| 3579 | **fearful** | 1 | 2 | - | 332.39 | - | 3,192 | - | 0.000432 | 🔵 low — common in general English | — |
| 3580 | **behold** | 1 | 2 | - | 332.39 | - | 3,193 | - | 0.000432 | 🔵 low — common in general English | — |
| 3581 | **nausea** | 1 | 2 | - | 332.39 | - | 3,194 | - | 0.000432 | 🔵 low — common in general English | — |
| 3582 | **beggary** | 1 | 2 | - | 332.39 | - | 3,195 | - | 0.000432 | 🔵 low — common in general English | — |
| 3583 | **market-day** | 1 | 2 | - | 332.39 | - | 3,196 | - | 0.000432 | 🔵 low — common in general English | — |
| 3584 | **bicker** | 1 | 2 | - | 332.39 | - | 3,197 | - | 0.000431 | 🔵 low — common in general English | — |
| 3585 | **consecrated** | 1 | 2 | - | 332.39 | - | 3,198 | - | 0.000431 | 🔵 low — common in general English | — |
| 3586 | **dwelt** | 1 | 2 | - | 332.39 | - | 3,199 | - | 0.000431 | 🔵 low — common in general English | — |
| 3587 | **cliff** | 1 | 2 | - | 332.39 | - | 3,200 | - | 0.000431 | 🔵 low — common in general English | — |
| 3588 | **mandhatri** | 1 | 2 | - | 332.39 | - | 3,201 | - | 0.000431 | 🔵 low — common in general English | ✓ ང་ལས་ནུ |
| 3589 | **dandle** | 1 | 2 | - | 332.39 | - | 3,202 | - | 0.000431 | 🔵 low — common in general English | — |
| 3590 | **buried** | 1 | 2 | - | 332.39 | - | 3,203 | - | 0.000431 | 🔵 low — common in general English | — |
| 3591 | **erudite** | 1 | 2 | - | 332.39 | - | 3,204 | - | 0.000431 | 🔵 low — common in general English | — |
| 3592 | **talented** | 1 | 2 | - | 332.39 | - | 3,205 | - | 0.000431 | 🔵 low — common in general English | — |
| 3593 | **beget** | 1 | 2 | - | 332.39 | - | 3,206 | - | 0.000431 | 🔵 low — common in general English | — |
| 3594 | **yearn** | 1 | 2 | - | 332.39 | - | 3,207 | - | 0.000430 | 🔵 low — common in general English | — |
| 3595 | **aryadeva** | 1 | 2 | - | 332.39 | - | 3,208 | - | 0.000430 | 🔵 low — common in general English | ✓ འཕགས་པ་ལྷ |
| 3596 | **crave** | 1 | 2 | - | 332.39 | - | 3,209 | - | 0.000430 | 🔵 low — common in general English | — |
| 3597 | **phlegm** | 1 | 2 | - | 332.39 | - | 3,210 | - | 0.000430 | 🔵 low — common in general English | ✓ བད་ཀན |
| 3598 | **skeleton** | 1 | 2 | - | 332.39 | - | 3,211 | - | 0.000430 | 🔵 low — common in general English | — |
| 3599 | **tusk** | 1 | 2 | - | 332.39 | - | 3,212 | - | 0.000430 | 🔵 low — common in general English | — |
| 3600 | **forgetfulness** | 1 | 2 | - | 332.39 | - | 3,213 | - | 0.000430 | 🔵 low — common in general English | — |
| 3601 | **transient** | 1 | 2 | - | 332.39 | - | 3,214 | - | 0.000430 | 🔵 low — common in general English | — |
| 3602 | **lowly** | 1 | 2 | - | 332.39 | - | 3,215 | - | 0.000430 | 🔵 low — common in general English | — |
| 3603 | **deathless** | 1 | 2 | - | 332.39 | - | 3,216 | - | 0.000430 | 🔵 low — common in general English | — |
| 3604 | **imper** | 1 | 2 | - | 332.39 | - | 3,217 | - | 0.000430 | 🔵 low — common in general English | — |
| 3605 | **manence** | 1 | 2 | - | 332.39 | - | 3,218 | - | 0.000429 | 🔵 low — common in general English | — |
| 3606 | **nirvat** | 1 | 2 | - | 332.39 | - | 3,219 | - | 0.000429 | 🔵 low — common in general English | — |
| 3607 | **renunciate** | 1 | 2 | - | 332.39 | - | 3,220 | - | 0.000429 | 🔵 low — common in general English | — |
| 3608 | **permeated** | 1 | 2 | - | 332.39 | - | 3,221 | - | 0.000429 | 🔵 low — common in general English | — |
| 3609 | **ant** | 1 | 2 | - | 332.39 | - | 3,222 | - | 0.000429 | 🔵 low — common in general English | — |
| 3610 | **fiery** | 1 | 2 | - | 332.39 | - | 3,223 | - | 0.000429 | 🔵 low — common in general English | — |
| 3611 | **brandishing** | 1 | 2 | - | 332.39 | - | 3,224 | - | 0.000429 | 🔵 low — common in general English | — |
| 3612 | **phantom** | 1 | 2 | - | 332.39 | - | 3,225 | - | 0.000429 | 🔵 low — common in general English | — |
| 3613 | **slain** | 1 | 2 | - | 332.39 | - | 3,226 | - | 0.000429 | 🔵 low — common in general English | — |
| 3614 | **mortar** | 1 | 2 | - | 332.39 | - | 3,227 | - | 0.000429 | 🔵 low — common in general English | — |
| 3615 | **ofyama** | 1 | 2 | - | 332.39 | - | 3,228 | - | 0.000429 | 🔵 low — common in general English | — |
| 3616 | **hell-being** | 1 | 2 | - | 332.39 | - | 3,229 | - | 0.000428 | 🔵 low — common in general English | — |
| 3617 | **corre** | 1 | 2 | - | 332.39 | - | 3,230 | - | 0.000428 | 🔵 low — common in general English | — |
| 3618 | **spond** | 1 | 2 | - | 332.39 | - | 3,231 | - | 0.000428 | 🔵 low — common in general English | — |
| 3619 | **rounding-up** | 1 | 2 | - | 332.39 | - | 3,232 | - | 0.000428 | 🔵 low — common in general English | — |
| 3620 | **howling** | 1 | 2 | - | 332.39 | - | 3,233 | - | 0.000428 | 🔵 low — common in general English | — |
| 3621 | **bronze** | 1 | 2 | - | 332.39 | - | 3,234 | - | 0.000428 | 🔵 low — common in general English | — |
| 3622 | **sciousness** | 1 | 2 | - | 332.39 | - | 3,235 | - | 0.000428 | 🔵 low — common in general English | — |
| 3623 | **anus** | 1 | 2 | - | 332.39 | - | 3,236 | - | 0.000428 | 🔵 low — common in general English | — |
| 3624 | **glowing** | 1 | 2 | - | 332.39 | - | 3,237 | - | 0.000428 | 🔵 low — common in general English | — |
| 3625 | **subjected** | 1 | 2 | - | 332.39 | - | 3,238 | - | 0.000428 | 🔵 low — common in general English | — |
| 3626 | **salmali** | 1 | 2 | - | 332.39 | - | 3,239 | - | 0.000428 | 🔵 low — common in general English | — |
| 3627 | **mali** | 1 | 2 | - | 332.39 | - | 3,240 | - | 0.000427 | 🔵 low — common in general English | — |
| 3628 | **vulture** | 1 | 2 | - | 332.39 | - | 3,241 | - | 0.000427 | 🔵 low — common in general English | — |
| 3629 | **hideous** | 1 | 2 | - | 332.39 | - | 3,242 | - | 0.000427 | 🔵 low — common in general English | — |
| 3630 | **intolerable** | 1 | 2 | - | 332.39 | - | 3,243 | - | 0.000427 | 🔵 low — common in general English | — |
| 3631 | **groan** | 1 | 2 | - | 332.39 | - | 3,244 | - | 0.000427 | 🔵 low — common in general English | — |
| 3632 | **lotus-like** | 1 | 2 | - | 332.39 | - | 3,245 | - | 0.000427 | 🔵 low — common in general English | — |
| 3633 | **blistering** | 1 | 2 | - | 332.39 | - | 3,246 | - | 0.000427 | 🔵 low — common in general English | — |
| 3634 | **yamdrok** | 1 | 2 | - | 332.39 | - | 3,247 | - | 0.000427 | 🔵 low — common in general English | — |
| 3635 | **tangtong** | 1 | 2 | - | 332.39 | - | 3,248 | - | 0.000427 | 🔵 low — common in general English | ~ |
| 3636 | **glance** | 1 | 2 | - | 332.39 | - | 3,249 | - | 0.000427 | 🔵 low — common in general English | — |
| 3637 | **venerated** | 1 | 2 | - | 332.39 | - | 3,250 | - | 0.000427 | 🔵 low — common in general English | — |
| 3638 | **priest** | 1 | 2 | - | 332.39 | - | 3,251 | - | 0.000426 | 🔵 low — common in general English | — |
| 3639 | **quivering** | 1 | 2 | - | 332.39 | - | 3,252 | - | 0.000426 | 🔵 low — common in general English | — |
| 3640 | **knive** | 1 | 2 | - | 332.39 | - | 3,253 | - | 0.000426 | 🔵 low — common in general English | — |
| 3641 | **gleam** | 1 | 2 | - | 332.39 | - | 3,254 | - | 0.000426 | 🔵 low — common in general English | — |
| 3642 | **lovely** | 1 | 2 | - | 332.39 | - | 3,255 | - | 0.000426 | 🔵 low — common in general English | — |
| 3643 | **exemplary** | 1 | 2 | - | 332.39 | - | 3,256 | - | 0.000426 | 🔵 low — common in general English | — |
| 3644 | **shameful** | 1 | 2 | - | 332.39 | - | 3,257 | - | 0.000426 | 🔵 low — common in general English | — |
| 3645 | **withered** | 1 | 2 | - | 332.39 | - | 3,258 | - | 0.000426 | 🔵 low — common in general English | — |
| 3646 | **moonlight** | 1 | 2 | - | 332.39 | - | 3,259 | - | 0.000426 | 🔵 low — common in general English | — |
| 3647 | **srot** | 1 | 2 | - | 332.39 | - | 3,260 | - | 0.000426 | 🔵 low — common in general English | — |
| 3648 | **yelled** | 1 | 2 | - | 332.39 | - | 3,261 | - | 0.000426 | 🔵 low — common in general English | — |
| 3649 | **jetari** | 1 | 2 | - | 332.39 | - | 3,262 | - | 0.000425 | 🔵 low — common in general English | — |
| 3650 | **repulsive** | 1 | 2 | - | 332.39 | - | 3,263 | - | 0.000425 | 🔵 low — common in general English | — |
| 3651 | **wandered** | 1 | 2 | - | 332.39 | - | 3,264 | - | 0.000425 | 🔵 low — common in general English | — |
| 3652 | **afflict** | 1 | 2 | - | 332.39 | - | 3,265 | - | 0.000425 | 🔵 low — common in general English | — |
| 3653 | **stinginess** | 1 | 2 | - | 332.39 | - | 3,266 | - | 0.000425 | 🔵 low — common in general English | — |
| 3654 | **magician** | 1 | 2 | - | 332.39 | - | 3,267 | - | 0.000425 | 🔵 low — common in general English | — |
| 3655 | **imaginary** | 1 | 2 | - | 332.39 | - | 3,268 | - | 0.000425 | 🔵 low — common in general English | — |
| 3656 | **fragment** | 1 | 2 | - | 332.39 | - | 3,269 | - | 0.000425 | 🔵 low — common in general English | — |
| 3657 | **tum** | 1 | 2 | - | 332.39 | - | 3,270 | - | 0.000425 | 🔵 low — common in general English | — |
| 3658 | **garuc** | 1 | 2 | - | 332.39 | - | 3,271 | - | 0.000425 | 🔵 low — common in general English | — |
| 3659 | **gun** | 1 | 2 | - | 332.39 | - | 3,272 | - | 0.000425 | 🔵 low — common in general English | — |
| 3660 | **leopard** | 1 | 2 | - | 332.39 | - | 3,273 | - | 0.000424 | 🔵 low — common in general English | — |
| 3661 | **milked** | 1 | 2 | - | 332.39 | - | 3,274 | - | 0.000424 | 🔵 low — common in general English | — |
| 3662 | **sincerity** | 1 | 2 | - | 332.39 | - | 3,275 | - | 0.000424 | 🔵 low — common in general English | — |
| 3663 | **dread** | 1 | 2 | - | 332.39 | - | 3,276 | - | 0.000424 | 🔵 low — common in general English | — |
| 3664 | **adornment** | 1 | 2 | - | 332.39 | - | 3,277 | - | 0.000424 | 🔵 low — common in general English | — |
| 3665 | **mule** | 1 | 2 | - | 332.39 | - | 3,278 | - | 0.000424 | 🔵 low — common in general English | — |
| 3666 | **strand** | 1 | 2 | - | 332.39 | - | 3,279 | - | 0.000424 | 🔵 low — common in general English | — |
| 3667 | **disembowelled** | 1 | 2 | - | 332.39 | - | 3,280 | - | 0.000424 | 🔵 low — common in general English | — |
| 3668 | **suffocate** | 1 | 2 | - | 332.39 | - | 3,281 | - | 0.000424 | 🔵 low — common in general English | — |
| 3669 | **ewe** | 1 | 2 | - | 332.39 | - | 3,282 | - | 0.000424 | 🔵 low — common in general English | — |
| 3670 | **sip** | 1 | 2 | - | 332.39 | - | 3,283 | - | 0.000424 | 🔵 low — common in general English | — |
| 3671 | **calve** | 1 | 2 | - | 332.39 | - | 3,284 | - | 0.000423 | 🔵 low — common in general English | — |
| 3672 | **stolen** | 1 | 2 | - | 332.39 | - | 3,285 | - | 0.000423 | 🔵 low — common in general English | — |
| 3673 | **semen** | 1 | 2 | - | 332.39 | - | 3,286 | - | 0.000423 | 🔵 low — common in general English | — |
| 3674 | **fetus** | 1 | 2 | - | 332.39 | - | 3,287 | - | 0.000423 | 🔵 low — common in general English | — |
| 3675 | **banging** | 1 | 2 | - | 332.39 | - | 3,288 | - | 0.000423 | 🔵 low — common in general English | — |
| 3676 | **bony** | 1 | 2 | - | 332.39 | - | 3,289 | - | 0.000423 | 🔵 low — common in general English | — |
| 3677 | **rubbed** | 1 | 2 | - | 332.39 | - | 3,290 | - | 0.000423 | 🔵 low — common in general English | — |
| 3678 | **cradle** | 1 | 2 | - | 332.39 | - | 3,291 | - | 0.000423 | 🔵 low — common in general English | — |
| 3679 | **ripple** | 1 | 2 | - | 332.39 | - | 3,292 | - | 0.000423 | 🔵 low — common in general English | — |
| 3680 | **inconsequential** | 1 | 2 | - | 332.39 | - | 3,293 | - | 0.000423 | 🔵 low — common in general English | — |
| 3681 | **vigour** | 1 | 2 | - | 332.39 | - | 3,294 | - | 0.000423 | 🔵 low — common in general English | — |
| 3682 | **irritable** | 1 | 2 | - | 332.39 | - | 3,295 | - | 0.000422 | 🔵 low — common in general English | — |
| 3683 | **sing** | 1 | 2 | - | 332.39 | - | 3,296 | - | 0.000422 | 🔵 low — common in general English | — |
| 3684 | **stalking** | 1 | 2 | - | 332.39 | - | 3,297 | - | 0.000422 | 🔵 low — common in general English | — |
| 3685 | **protrude** | 1 | 2 | - | 332.39 | - | 3,298 | - | 0.000422 | 🔵 low — common in general English | — |
| 3686 | **faded** | 1 | 2 | - | 332.39 | - | 3,299 | - | 0.000422 | 🔵 low — common in general English | — |
| 3687 | **scorn** | 1 | 2 | - | 332.39 | - | 3,300 | - | 0.000422 | 🔵 low — common in general English | — |
| 3688 | **hallucinate** | 1 | 2 | - | 332.39 | - | 3,302 | - | 0.000422 | 🔵 low — common in general English | — |
| 3689 | **realiz** | 1 | 2 | - | 332.39 | - | 3,303 | - | 0.000422 | 🔵 low — common in general English | — |
| 3690 | **descend** | 1 | 2 | - | 332.39 | - | 3,304 | - | 0.000422 | 🔵 low — common in general English | — |
| 3691 | **unending** | 1 | 2 | - | 332.39 | - | 3,305 | - | 0.000422 | 🔵 low — common in general English | — |
| 3692 | **miserliness** | 1 | 2 | - | 332.39 | - | 3,306 | - | 0.000421 | 🔵 low — common in general English | — |
| 3693 | **charity** | 1 | 2 | - | 332.39 | - | 3,307 | - | 0.000421 | 🔵 low — common in general English | — |
| 3694 | **hostility** | 1 | 2 | - | 332.39 | - | 3,308 | - | 0.000421 | 🔵 low — common in general English | — |
| 3695 | **cours** | 1 | 2 | - | 332.39 | - | 3,309 | - | 0.000421 | 🔵 low — common in general English | — |
| 3696 | **tea-leave** | 1 | 2 | - | 332.39 | - | 3,310 | - | 0.000421 | 🔵 low — common in general English | — |
| 3697 | **dishonour** | 1 | 2 | - | 332.39 | - | 3,311 | - | 0.000421 | 🔵 low — common in general English | — |
| 3698 | **splendidly** | 1 | 2 | - | 332.39 | - | 3,312 | - | 0.000421 | 🔵 low — common in general English | — |
| 3699 | **nourishing** | 1 | 2 | - | 332.39 | - | 3,313 | - | 0.000421 | 🔵 low — common in general English | — |
| 3700 | **harness** | 1 | 2 | - | 332.39 | - | 3,314 | - | 0.000421 | 🔵 low — common in general English | — |
| 3701 | **despair** | 1 | 2 | - | 332.39 | - | 3,315 | - | 0.000421 | 🔵 low — common in general English | — |
| 3702 | **red-faced** | 1 | 2 | - | 332.39 | - | 3,316 | - | 0.000421 | 🔵 low — common in general English | — |
| 3703 | **calamity** | 1 | 2 | - | 332.39 | - | 3,317 | - | 0.000421 | 🔵 low — common in general English | — |
| 3704 | **collaps** | 1 | 2 | - | 332.39 | - | 3,318 | - | 0.000420 | 🔵 low — common in general English | — |
| 3705 | **expedition** | 1 | 2 | - | 332.39 | - | 3,319 | - | 0.000420 | 🔵 low — common in general English | — |
| 3706 | **slave** | 1 | 2 | - | 332.39 | - | 3,320 | - | 0.000420 | 🔵 low — common in general English | — |
| 3707 | **degeneration** | 1 | 2 | - | 332.39 | - | 3,321 | - | 0.000420 | 🔵 low — common in general English | — |
| 3708 | **distinguishing** | 1 | 2 | - | 332.39 | - | 3,322 | - | 0.000420 | 🔵 low — common in general English | ~ |
| 3709 | **resentment** | 1 | 2 | - | 332.39 | - | 3,323 | - | 0.000420 | 🔵 low — common in general English | — |
| 3710 | **grabbing** | 1 | 2 | - | 332.39 | - | 3,324 | - | 0.000420 | 🔵 low — common in general English | — |
| 3711 | **supremely** | 1 | 2 | - | 332.39 | - | 3,325 | - | 0.000420 | 🔵 low — common in general English | — |
| 3712 | **suffused** | 1 | 2 | - | 332.39 | - | 3,326 | - | 0.000420 | 🔵 low — common in general English | — |
| 3713 | **sweat** | 1 | 2 | - | 332.39 | - | 3,327 | - | 0.000420 | 🔵 low — common in general English | — |
| 3714 | **ceaseless** | 1 | 2 | - | 332.39 | - | 3,328 | - | 0.000420 | 🔵 low — common in general English | — |
| 3715 | **cesspit** | 1 | 2 | - | 332.39 | - | 3,329 | - | 0.000419 | 🔵 low — common in general English | — |
| 3716 | **recollection** | 1 | 2 | - | 332.39 | - | 3,330 | - | 0.000419 | 🔵 low — common in general English | — |
| 3717 | **overjoyed** | 1 | 2 | - | 332.39 | - | 3,331 | - | 0.000419 | 🔵 low — common in general English | — |
| 3718 | **crackling** | 1 | 2 | - | 332.39 | - | 3,332 | - | 0.000419 | 🔵 low — common in general English | — |
| 3719 | **hell-realm** | 1 | 2 | - | 332.39 | - | 3,333 | - | 0.000419 | 🔵 low — common in general English | — |
| 3720 | **transgressed** | 1 | 2 | - | 332.39 | - | 3,334 | - | 0.000419 | 🔵 low — common in general English | — |
| 3721 | **cherish** | 1 | 2 | - | 332.39 | - | 3,336 | - | 0.000419 | 🔵 low — common in general English | — |
| 3722 | **excrement** | 1 | 2 | - | 332.39 | - | 3,337 | - | 0.000419 | 🔵 low — common in general English | — |
| 3723 | **tsik** | 1 | 2 | - | 332.39 | - | 3,339 | - | 0.000419 | 🔵 low — common in general English | — |
| 3724 | **astray** | 1 | 2 | - | 332.39 | - | 3,340 | - | 0.000419 | 🔵 low — common in general English | — |
| 3725 | **predilection** | 1 | 2 | - | 332.39 | - | 3,341 | - | 0.000418 | 🔵 low — common in general English | — |
| 3726 | **graze** | 1 | 2 | - | 332.39 | - | 3,342 | - | 0.000418 | 🔵 low — common in general English | — |
| 3727 | **dung** | 1 | 2 | - | 332.39 | - | 3,343 | - | 0.000418 | 🔵 low — common in general English | — |
| 3728 | **lice** | 1 | 2 | - | 332.39 | - | 3,344 | - | 0.000418 | 🔵 low — common in general English | — |
| 3729 | **bride** | 1 | 2 | - | 332.39 | - | 3,345 | - | 0.000418 | 🔵 low — common in general English | — |
| 3730 | **gobble** | 1 | 2 | - | 332.39 | - | 3,346 | - | 0.000418 | 🔵 low — common in general English | — |
| 3731 | **smacking** | 1 | 2 | - | 332.39 | - | 3,347 | - | 0.000418 | 🔵 low — common in general English | — |
| 3732 | **muzzle** | 1 | 2 | - | 332.39 | - | 3,348 | - | 0.000418 | 🔵 low — common in general English | — |
| 3733 | **ceas** | 1 | 2 | - | 332.39 | - | 3,349 | - | 0.000418 | 🔵 low — common in general English | — |
| 3734 | **staring** | 1 | 2 | - | 332.39 | - | 3,350 | - | 0.000418 | 🔵 low — common in general English | — |
| 3735 | **skinned** | 1 | 2 | - | 332.39 | - | 3,351 | - | 0.000418 | 🔵 low — common in general English | — |
| 3736 | **all-pervading** | 1 | 2 | - | 332.39 | - | 3,352 | - | 0.000417 | 🔵 low — common in general English | — |
| 3737 | **stove** | 1 | 2 | - | 332.39 | - | 3,353 | - | 0.000417 | 🔵 low — common in general English | — |
| 3738 | **stealth** | 1 | 2 | - | 332.39 | - | 3,354 | - | 0.000417 | 🔵 low — common in general English | — |
| 3739 | **clos** | 1 | 2 | - | 332.39 | - | 3,355 | - | 0.000417 | 🔵 low — common in general English | — |
| 3740 | **obsession** | 1 | 2 | - | 332.39 | - | 3,356 | - | 0.000417 | 🔵 low — common in general English | — |
| 3741 | **brooding** | 1 | 2 | - | 332.39 | - | 3,357 | - | 0.000417 | 🔵 low — common in general English | — |
| 3742 | **charlatan** | 1 | 2 | - | 332.39 | - | 3,358 | - | 0.000417 | 🔵 low — common in general English | — |
| 3743 | **behaving** | 1 | 2 | - | 332.39 | - | 3,359 | - | 0.000417 | 🔵 low — common in general English | — |
| 3744 | **flaw** | 1 | 2 | - | 332.39 | - | 3,360 | - | 0.000417 | 🔵 low — common in general English | — |
| 3745 | **offensively** | 1 | 2 | - | 332.39 | - | 3,361 | - | 0.000417 | 🔵 low — common in general English | — |
| 3746 | **singing** | 1 | 2 | - | 332.39 | - | 3,362 | - | 0.000417 | 🔵 low — common in general English | — |
| 3747 | **distracting** | 1 | 2 | - | 332.39 | - | 3,363 | - | 0.000417 | 🔵 low — common in general English | — |
| 3748 | **chanting** | 1 | 2 | - | 332.39 | - | 3,364 | - | 0.000416 | 🔵 low — common in general English | — |
| 3749 | **partake** | 1 | 2 | - | 332.39 | - | 3,365 | - | 0.000416 | 🔵 low — common in general English | — |
| 3750 | **sixty-two** | 1 | 2 | - | 332.39 | - | 3,366 | - | 0.000416 | 🔵 low — common in general English | — |
| 3751 | **downhill** | 1 | 2 | - | 332.39 | - | 3,367 | - | 0.000416 | 🔵 low — common in general English | — |
| 3752 | **sharpness** | 1 | 2 | - | 332.39 | - | 3,368 | - | 0.000416 | 🔵 low — common in general English | — |
| 3753 | **giver** | 1 | 2 | - | 332.39 | - | 3,369 | - | 0.000416 | 🔵 low — common in general English | — |
| 3754 | **nourishment** | 1 | 2 | - | 332.39 | - | 3,370 | - | 0.000416 | 🔵 low — common in general English | — |
| 3755 | **sustenance** | 1 | 2 | - | 332.39 | - | 3,371 | - | 0.000416 | 🔵 low — common in general English | — |
| 3756 | **impulse** | 1 | 2 | - | 332.39 | - | 3,373 | - | 0.000416 | 🔵 low — common in general English | — |
| 3757 | **affinity** | 1 | 2 | - | 332.39 | - | 3,374 | - | 0.000416 | 🔵 low — common in general English | — |
| 3758 | **respite** | 1 | 2 | - | 332.39 | - | 3,375 | - | 0.000416 | 🔵 low — common in general English | — |
| 3759 | **disperse** | 1 | 2 | - | 332.39 | - | 3,376 | - | 0.000415 | 🔵 low — common in general English | — |
| 3760 | **impoverished** | 1 | 2 | - | 332.39 | - | 3,377 | - | 0.000415 | 🔵 low — common in general English | — |
| 3761 | **spouse** | 1 | 2 | - | 332.39 | - | 3,378 | - | 0.000415 | 🔵 low — common in general English | — |
| 3762 | **chore** | 1 | 2 | - | 332.39 | - | 3,379 | - | 0.000415 | 🔵 low — common in general English | — |
| 3763 | **reaping** | 1 | 2 | - | 332.39 | - | 3,380 | - | 0.000415 | 🔵 low — common in general English | — |
| 3764 | **insulted** | 1 | 2 | - | 332.39 | - | 3,381 | - | 0.000415 | 🔵 low — common in general English | — |
| 3765 | **denigrate** | 1 | 2 | - | 332.39 | - | 3,382 | - | 0.000415 | 🔵 low — common in general English | — |
| 3766 | **ravine** | 1 | 2 | - | 332.39 | - | 3,383 | - | 0.000415 | 🔵 low — common in general English | — |
| 3767 | **massacred** | 1 | 2 | - | 332.39 | - | 3,384 | - | 0.000415 | 🔵 low — common in general English | — |
| 3768 | **parivrajika** | 1 | 2 | - | 332.39 | - | 3,385 | - | 0.000415 | 🔵 low — common in general English | — |
| 3769 | **shrine** | 1 | 2 | - | 332.39 | - | 3,386 | - | 0.000415 | 🔵 low — common in general English | — |
| 3770 | **nirvar** | 1 | 2 | - | 332.39 | - | 3,387 | - | 0.000415 | 🔵 low — common in general English | — |
| 3771 | **kashmir** | 1 | 2 | - | 332.39 | - | 3,388 | - | 0.000414 | 🔵 low — common in general English | — |
| 3772 | **dyeing** | 1 | 2 | - | 332.39 | - | 3,389 | - | 0.000414 | 🔵 low — common in general English | — |
| 3773 | **sire** | 1 | 2 | - | 332.39 | - | 3,390 | - | 0.000414 | 🔵 low — common in general English | — |
| 3774 | **thief** | 1 | 2 | - | 332.39 | - | 3,391 | - | 0.000414 | 🔵 low — common in general English | — |
| 3775 | **kusa** | 1 | 2 | - | 332.39 | - | 3,392 | - | 0.000414 | 🔵 low — common in general English | — |
| 3776 | **disparage** | 1 | 2 | - | 332.39 | - | 3,393 | - | 0.000414 | 🔵 low — common in general English | — |
| 3777 | **ashota** | 1 | 2 | - | 332.39 | - | 3,394 | - | 0.000414 | 🔵 low — common in general English | — |
| 3778 | **scolded** | 1 | 2 | - | 332.39 | - | 3,395 | - | 0.000414 | 🔵 low — common in general English | — |
| 3779 | **serpent** | 1 | 2 | - | 332.39 | - | 3,396 | - | 0.000414 | 🔵 low — common in general English | — |
| 3780 | **rivalry** | 1 | 2 | - | 332.39 | - | 3,397 | - | 0.000414 | 🔵 low — common in general English | — |
| 3781 | **pratimo** | 1 | 2 | - | 332.39 | - | 3,398 | - | 0.000414 | 🔵 low — common in general English | — |
| 3782 | **stained** | 1 | 2 | - | 332.39 | - | 3,399 | - | 0.000413 | 🔵 low — common in general English | — |
| 3783 | **conversely** | 1 | 2 | - | 332.39 | - | 3,400 | - | 0.000413 | 🔵 low — common in general English | — |
| 3784 | **goodness** | 1 | 2 | - | 332.39 | - | 3,401 | - | 0.000413 | 🔵 low — common in general English | — |
| 3785 | **ofvajradhara** | 1 | 2 | - | 332.39 | - | 3,402 | - | 0.000413 | 🔵 low — common in general English | — |
| 3786 | **me-but** | 1 | 2 | - | 332.39 | - | 3,403 | - | 0.000413 | 🔵 low — common in general English | — |
| 3787 | **firstly** | 1 | 2 | - | 332.39 | - | 3,404 | - | 0.000413 | 🔵 low — common in general English | — |
| 3788 | **sastra** | 1 | 2 | - | 332.39 | - | 3,405 | - | 0.000413 | 🔵 low — common in general English | — |
| 3789 | **tripitaka** | 1 | 2 | - | 332.39 | - | 3,406 | - | 0.000413 | 🔵 low — common in general English | ✓ སྡེ་སྣོད་གསུམ |
| 3790 | **riddance** | 1 | 2 | - | 332.39 | - | 3,407 | - | 0.000413 | 🔵 low — common in general English | — |
| 3791 | **pitaka** | 1 | 2 | - | 332.39 | - | 3,408 | - | 0.000413 | 🔵 low — common in general English | ~ |
| 3792 | **ripening** | 1 | 2 | - | 332.39 | - | 3,409 | - | 0.000413 | 🔵 low — common in general English | — |
| 3793 | **tered** | 1 | 2 | - | 332.39 | - | 3,410 | - | 0.000413 | 🔵 low — common in general English | — |
| 3794 | **fief** | 1 | 2 | - | 332.39 | - | 3,411 | - | 0.000412 | 🔵 low — common in general English | — |
| 3795 | **puffed** | 1 | 2 | - | 332.39 | - | 3,412 | - | 0.000412 | 🔵 low — common in general English | — |
| 3796 | **bogus** | 1 | 2 | - | 332.39 | - | 3,413 | - | 0.000412 | 🔵 low — common in general English | — |
| 3797 | **unthinkingly** | 1 | 2 | - | 332.39 | - | 3,414 | - | 0.000412 | 🔵 low — common in general English | — |
| 3798 | **attuned** | 1 | 2 | - | 332.39 | - | 3,415 | - | 0.000412 | 🔵 low — common in general English | — |
| 3799 | **patiently** | 1 | 2 | - | 332.39 | - | 3,416 | - | 0.000412 | 🔵 low — common in general English | — |
| 3800 | **disci** | 1 | 2 | - | 332.39 | - | 3,417 | - | 0.000412 | 🔵 low — common in general English | — |
| 3801 | **radiate** | 1 | 2 | - | 332.39 | - | 3,418 | - | 0.000412 | 🔵 low — common in general English | — |
| 3802 | **simile** | 1 | 2 | - | 332.39 | - | 3,419 | - | 0.000412 | 🔵 low — common in general English | — |
| 3803 | **sparing** | 1 | 2 | - | 332.39 | - | 3,420 | - | 0.000412 | 🔵 low — common in general English | — |
| 3804 | **displeasing** | 1 | 2 | - | 332.39 | - | 3,421 | - | 0.000412 | 🔵 low — common in general English | — |
| 3805 | **anvil** | 1 | 2 | - | 332.39 | - | 3,422 | - | 0.000412 | 🔵 low — common in general English | — |
| 3806 | **sweeper** | 1 | 2 | - | 332.39 | - | 3,423 | - | 0.000412 | 🔵 low — common in general English | — |
| 3807 | **drank** | 1 | 2 | - | 332.39 | - | 3,424 | - | 0.000411 | 🔵 low — common in general English | — |
| 3808 | **mara** | 1 | 2 | - | 332.39 | - | 3,425 | - | 0.000411 | 🔵 low — common in general English | ✓ བདུད |
| 3809 | **respectfully** | 1 | 2 | - | 332.39 | - | 3,426 | - | 0.000411 | 🔵 low — common in general English | — |
| 3810 | **paramount** | 1 | 2 | - | 332.39 | - | 3,427 | - | 0.000411 | 🔵 low — common in general English | — |
| 3811 | **indivisibly** | 1 | 2 | - | 332.39 | - | 3,428 | - | 0.000411 | 🔵 low — common in general English | — |
| 3812 | **obeying** | 1 | 2 | - | 332.39 | - | 3,429 | - | 0.000411 | 🔵 low — common in general English | — |
| 3813 | **profess** | 1 | 2 | - | 332.39 | - | 3,430 | - | 0.000411 | 🔵 low — common in general English | — |
| 3814 | **profundity** | 1 | 2 | - | 332.39 | - | 3,431 | - | 0.000411 | 🔵 low — common in general English | — |
| 3815 | **pretending** | 1 | 2 | - | 332.39 | - | 3,432 | - | 0.000411 | 🔵 low — common in general English | — |
| 3816 | **superfluous** | 1 | 2 | - | 332.39 | - | 3,433 | - | 0.000411 | 🔵 low — common in general English | — |
| 3817 | **rongton** | 1 | 2 | - | 332.39 | - | 3,434 | - | 0.000411 | 🔵 low — common in general English | — |
| 3818 | **lhaga** | 1 | 2 | - | 332.39 | - | 3,435 | - | 0.000411 | 🔵 low — common in general English | — |
| 3819 | **trowolung** | 1 | 2 | - | 332.39 | - | 3,436 | - | 0.000410 | 🔵 low — common in general English | — |
| 3820 | **imitation** | 1 | 2 | - | 332.39 | - | 3,437 | - | 0.000410 | 🔵 low — common in general English | — |
| 3821 | **engraved** | 1 | 2 | - | 332.39 | - | 3,438 | - | 0.000410 | 🔵 low — common in general English | — |
| 3822 | **wasteland** | 1 | 2 | - | 332.39 | - | 3,439 | - | 0.000410 | 🔵 low — common in general English | — |
| 3823 | **paramita** | 1 | 2 | - | 332.39 | - | 3,440 | - | 0.000410 | 🔵 low — common in general English | — |
| 3824 | **venerate** | 1 | 2 | - | 332.39 | - | 3,441 | - | 0.000410 | 🔵 low — common in general English | — |
| 3825 | **crossroad** | 1 | 2 | - | 332.39 | - | 3,442 | - | 0.000410 | 🔵 low — common in general English | — |
| 3826 | **thigh** | 1 | 2 | - | 332.39 | - | 3,443 | - | 0.000410 | 🔵 low — common in general English | — |
| 3827 | **preaching** | 1 | 2 | - | 332.39 | - | 3,444 | - | 0.000410 | 🔵 low — common in general English | — |
| 3828 | **filigree** | 1 | 2 | - | 332.39 | - | 3,445 | - | 0.000410 | 🔵 low — common in general English | — |
| 3829 | **lapi** | 1 | 2 | - | 332.39 | - | 3,446 | - | 0.000410 | 🔵 low — common in general English | — |
| 3830 | **lazuli** | 1 | 2 | - | 332.39 | - | 3,447 | - | 0.000410 | 🔵 low — common in general English | — |
| 3831 | **maiden** | 1 | 2 | - | 332.39 | - | 3,448 | - | 0.000409 | 🔵 low — common in general English | — |
| 3832 | **proclaim** | 1 | 2 | - | 332.39 | - | 3,449 | - | 0.000409 | 🔵 low — common in general English | — |
| 3833 | **nine-storey** | 1 | 2 | - | 332.39 | - | 3,450 | - | 0.000409 | 🔵 low — common in general English | — |
| 3834 | **bamboo** | 1 | 2 | - | 332.39 | - | 3,451 | - | 0.000409 | 🔵 low — common in general English | — |
| 3835 | **toe** | 1 | 2 | - | 332.39 | - | 3,452 | - | 0.000409 | 🔵 low — common in general English | — |
| 3836 | **labourer** | 1 | 2 | - | 332.39 | - | 3,453 | - | 0.000409 | 🔵 low — common in general English | — |
| 3837 | **twenty-four** | 1 | 2 | - | 332.39 | - | 3,454 | - | 0.000409 | 🔵 low — common in general English | — |
| 3838 | **obscura** | 1 | 2 | - | 332.39 | - | 3,455 | - | 0.000409 | 🔵 low — common in general English | — |
| 3839 | **awakened** | 1 | 2 | - | 332.39 | - | 3,456 | - | 0.000409 | 🔵 low — common in general English | — |
| 3840 | **disobey** | 1 | 2 | - | 332.39 | - | 3,457 | - | 0.000409 | 🔵 low — common in general English | — |
| 3841 | **vikramasila** | 1 | 2 | - | 332.39 | - | 3,458 | - | 0.000409 | 🔵 low — common in general English | — |
| 3842 | **hailstorm** | 1 | 2 | - | 332.39 | - | 3,459 | - | 0.000409 | 🔵 low — common in general English | — |
| 3843 | **yungton** | 1 | 2 | - | 332.39 | - | 3,460 | - | 0.000408 | 🔵 low — common in general English | — |
| 3844 | **jug** | 1 | 2 | - | 332.39 | - | 3,461 | - | 0.000408 | 🔵 low — common in general English | — |
| 3845 | **sariwara** | 1 | 2 | - | 332.39 | - | 3,462 | - | 0.000408 | 🔵 low — common in general English | — |
| 3846 | **shepa** | 1 | 2 | - | 332.39 | - | 3,463 | - | 0.000408 | 🔵 low — common in general English | — |
| 3847 | **drowning** | 1 | 2 | - | 332.39 | - | 3,464 | - | 0.000408 | 🔵 low — common in general English | — |
| 3848 | **entrance-way** | 1 | 2 | - | 332.39 | - | 3,465 | - | 0.000408 | 🔵 low — common in general English | — |
| 3849 | **vivid** | 1 | 2 | - | 332.39 | - | 3,466 | - | 0.000408 | 🔵 low — common in general English | — |
| 3850 | **relic** | 1 | 2 | - | 332.39 | - | 3,467 | - | 0.000408 | 🔵 low — common in general English | — |
| 3851 | **kongpo** | 1 | 2 | - | 332.39 | - | 3,468 | - | 0.000408 | 🔵 low — common in general English | — |
| 3852 | **wick** | 1 | 2 | - | 332.39 | - | 3,469 | - | 0.000408 | 🔵 low — common in general English | — |
| 3853 | **five-pronged** | 1 | 2 | - | 332.39 | - | 3,470 | - | 0.000408 | 🔵 low — common in general English | — |
| 3854 | **hooked** | 1 | 2 | - | 332.39 | - | 3,471 | - | 0.000408 | 🔵 low — common in general English | — |
| 3855 | **hadra** | 1 | 2 | - | 332.39 | - | 3,472 | - | 0.000408 | 🔵 low — common in general English | — |
| 3856 | **rabjampa** | 1 | 2 | - | 332.39 | - | 3,473 | - | 0.000407 | 🔵 low — common in general English | — |
| 3857 | **on-and** | 1 | 2 | - | 332.39 | - | 3,474 | - | 0.000407 | 🔵 low — common in general English | — |
| 3858 | **avalokitesvara-and** | 1 | 2 | - | 332.39 | - | 3,475 | - | 0.000407 | 🔵 low — common in general English | — |
| 3859 | **rear** | 1 | 2 | - | 332.39 | - | 3,476 | - | 0.000407 | 🔵 low — common in general English | — |
| 3860 | **encased** | 1 | 2 | - | 332.39 | - | 3,477 | - | 0.000407 | 🔵 low — common in general English | — |
| 3861 | **vowel** | 1 | 2 | - | 332.39 | - | 3,478 | - | 0.000407 | 🔵 low — common in general English | — |
| 3862 | **sugata** | 1 | 2 | - | 332.39 | - | 3,479 | - | 0.000407 | 🔵 low — common in general English | ✓ བདེ་བར་གཤེགས་པ |
| 3863 | **yearning** | 1 | 2 | - | 332.39 | - | 3,480 | - | 0.000407 | 🔵 low — common in general English | — |
| 3864 | **visnu** | 1 | 2 | - | 332.39 | - | 3,481 | - | 0.000407 | 🔵 low — common in general English | — |
| 3865 | **springing** | 1 | 2 | - | 332.39 | - | 3,482 | - | 0.000407 | 🔵 low — common in general English | — |
| 3866 | **glare** | 1 | 2 | - | 332.39 | - | 3,483 | - | 0.000407 | 🔵 low — common in general English | — |
| 3867 | **hid** | 1 | 2 | - | 332.39 | - | 3,484 | - | 0.000407 | 🔵 low — common in general English | — |
| 3868 | **manifested** | 1 | 2 | - | 332.39 | - | 3,485 | - | 0.000406 | 🔵 low — common in general English | — |
| 3869 | **fourfold** | 1 | 2 | - | 332.39 | - | 3,486 | - | 0.000406 | 🔵 low — common in general English | — |
| 3870 | **paqc** | 1 | 2 | - | 332.39 | - | 3,487 | - | 0.000406 | 🔵 low — common in general English | — |
| 3871 | **painting** | 1 | 2 | - | 332.39 | - | 3,488 | - | 0.000406 | 🔵 low — common in general English | — |
| 3872 | **vairocana** | 1 | 2 | - | 332.39 | - | 3,489 | - | 0.000406 | 🔵 low — common in general English | ✓ རྣམ་པར་སྣང་མཛད |
| 3873 | **beneficent** | 1 | 2 | - | 332.39 | - | 3,490 | - | 0.000406 | 🔵 low — common in general English | — |
| 3874 | **ajatasatru** | 1 | 2 | - | 332.39 | - | 3,491 | - | 0.000406 | 🔵 low — common in general English | — |
| 3875 | **fury** | 1 | 2 | - | 332.39 | - | 3,492 | - | 0.000406 | 🔵 low — common in general English | — |
| 3876 | **scoop** | 1 | 2 | - | 332.39 | - | 3,493 | - | 0.000406 | 🔵 low — common in general English | — |
| 3877 | **enlight** | 1 | 2 | - | 332.39 | - | 3,494 | - | 0.000406 | 🔵 low — common in general English | — |
| 3878 | **enment** | 1 | 2 | - | 332.39 | - | 3,495 | - | 0.000406 | 🔵 low — common in general English | — |
| 3879 | **lovingly** | 1 | 2 | - | 332.39 | - | 3,496 | - | 0.000406 | 🔵 low — common in general English | — |
| 3880 | **jarung** | 1 | 2 | - | 332.39 | - | 3,497 | - | 0.000406 | 🔵 low — common in general English | — |
| 3881 | **khashor** | 1 | 2 | - | 332.39 | - | 3,498 | - | 0.000405 | 🔵 low — common in general English | — |
| 3882 | **gentle** | 1 | 2 | - | 332.39 | - | 3,499 | - | 0.000405 | 🔵 low — common in general English | — |
| 3883 | **despised** | 1 | 2 | - | 332.39 | - | 3,500 | - | 0.000405 | 🔵 low — common in general English | — |
| 3884 | **summoning** | 1 | 2 | - | 332.39 | - | 3,501 | - | 0.000405 | 🔵 low — common in general English | — |
| 3885 | **dungeon** | 1 | 2 | - | 332.39 | - | 3,502 | - | 0.000405 | 🔵 low — common in general English | — |
| 3886 | **packhors** | 1 | 2 | - | 332.39 | - | 3,503 | - | 0.000405 | 🔵 low — common in general English | — |
| 3887 | **pain-you** | 1 | 2 | - | 332.39 | - | 3,504 | - | 0.000405 | 🔵 low — common in general English | — |
| 3888 | **panting** | 1 | 2 | - | 332.39 | - | 3,505 | - | 0.000405 | 🔵 low — common in general English | — |
| 3889 | **thrash** | 1 | 2 | - | 332.39 | - | 3,506 | - | 0.000405 | 🔵 low — common in general English | — |
| 3890 | **atsara** | 1 | 2 | - | 332.39 | - | 3,507 | - | 0.000405 | 🔵 low — common in general English | — |
| 3891 | **relishing** | 1 | 2 | - | 332.39 | - | 3,508 | - | 0.000405 | 🔵 low — common in general English | ~ |
| 3892 | **faint** | 1 | 2 | - | 332.39 | - | 3,509 | - | 0.000405 | 🔵 low — common in general English | — |
| 3893 | **marching** | 1 | 2 | - | 332.39 | - | 3,510 | - | 0.000405 | 🔵 low — common in general English | — |
| 3894 | **religion** | 1 | 2 | - | 332.39 | - | 3,511 | - | 0.000404 | 🔵 low — common in general English | — |
| 3895 | **paq** | 1 | 2 | - | 332.39 | - | 3,512 | - | 0.000404 | 🔵 low — common in general English | — |
| 3896 | **altruistic** | 1 | 2 | - | 332.39 | - | 3,513 | - | 0.000404 | 🔵 low — common in general English | — |
| 3897 | **lungpa** | 1 | 2 | - | 332.39 | - | 3,514 | - | 0.000404 | 🔵 low — common in general English | ~ |
| 3898 | **lhungpa** | 1 | 2 | - | 332.39 | - | 3,515 | - | 0.000404 | 🔵 low — common in general English | — |
| 3899 | **thenceforth** | 1 | 2 | - | 332.39 | - | 3,516 | - | 0.000404 | 🔵 low — common in general English | — |
| 3900 | **vasubandhu** | 1 | 2 | - | 332.39 | - | 3,517 | - | 0.000404 | 🔵 low — common in general English | — |
| 3901 | **departed** | 1 | 2 | - | 332.39 | - | 3,518 | - | 0.000404 | 🔵 low — common in general English | — |
| 3902 | **feather** | 1 | 2 | - | 332.39 | - | 3,519 | - | 0.000404 | 🔵 low — common in general English | — |
| 3903 | **unkind** | 1 | 2 | - | 332.39 | - | 3,520 | - | 0.000404 | 🔵 low — common in general English | — |
| 3904 | **pletely** | 1 | 2 | - | 332.39 | - | 3,521 | - | 0.000404 | 🔵 low — common in general English | — |
| 3905 | **tarlo** | 1 | 2 | - | 332.39 | - | 3,522 | - | 0.000404 | 🔵 low — common in general English | — |
| 3906 | **mistress** | 1 | 2 | - | 332.39 | - | 3,523 | - | 0.000403 | 🔵 low — common in general English | — |
| 3907 | **swim** | 1 | 2 | - | 332.39 | - | 3,524 | - | 0.000403 | 🔵 low — common in general English | — |
| 3908 | **shawopa** | 1 | 2 | - | 332.39 | - | 3,525 | - | 0.000403 | 🔵 low — common in general English | — |
| 3909 | **imponant** | 1 | 2 | - | 332.39 | - | 3,526 | - | 0.000403 | 🔵 low — common in general English | — |
| 3910 | **conceived** | 1 | 2 | - | 332.39 | - | 3,527 | - | 0.000403 | 🔵 low — common in general English | — |
| 3911 | **eighty-four** | 1 | 2 | - | 332.39 | - | 3,528 | - | 0.000403 | 🔵 low — common in general English | — |
| 3912 | **harnessed** | 1 | 2 | - | 332.39 | - | 3,529 | - | 0.000403 | 🔵 low — common in general English | — |
| 3913 | **belonged** | 1 | 2 | - | 332.39 | - | 3,530 | - | 0.000403 | 🔵 low — common in general English | — |
| 3914 | **jeweller** | 1 | 2 | - | 332.39 | - | 3,531 | - | 0.000403 | 🔵 low — common in general English | — |
| 3915 | **ancestor** | 1 | 2 | - | 332.39 | - | 3,532 | - | 0.000403 | 🔵 low — common in general English | — |
| 3916 | **hem** | 1 | 2 | - | 332.39 | - | 3,533 | - | 0.000403 | 🔵 low — common in general English | — |
| 3917 | **exquisite** | 1 | 2 | - | 332.39 | - | 3,534 | - | 0.000403 | 🔵 low — common in general English | — |
| 3918 | **fist** | 1 | 2 | - | 332.39 | - | 3,535 | - | 0.000403 | 🔵 low — common in general English | — |
| 3919 | **chakshingwa** | 1 | 2 | - | 332.39 | - | 3,536 | - | 0.000402 | 🔵 low — common in general English | ~ |
| 3920 | **shangshungpa** | 1 | 2 | - | 332.39 | - | 3,537 | - | 0.000402 | 🔵 low — common in general English | — |
| 3921 | **feverish** | 1 | 2 | - | 332.39 | - | 3,538 | - | 0.000402 | 🔵 low — common in general English | — |
| 3922 | **manicuda** | 1 | 2 | - | 332.39 | - | 3,539 | - | 0.000402 | 🔵 low — common in general English | — |
| 3923 | **dawned** | 1 | 2 | - | 332.39 | - | 3,540 | - | 0.000402 | 🔵 low — common in general English | — |
| 3924 | **bathed** | 1 | 2 | - | 332.39 | - | 3,541 | - | 0.000402 | 🔵 low — common in general English | — |
| 3925 | **brighu** | 1 | 2 | - | 332.39 | - | 3,542 | - | 0.000402 | 🔵 low — common in general English | — |
| 3926 | **sprang** | 1 | 2 | - | 332.39 | - | 3,543 | - | 0.000402 | 🔵 low — common in general English | — |
| 3927 | **duly** | 1 | 2 | - | 332.39 | - | 3,544 | - | 0.000402 | 🔵 low — common in general English | — |
| 3928 | **dharani** | 1 | 2 | - | 332.39 | - | 3,545 | - | 0.000402 | 🔵 low — common in general English | ✓ གཟུངས |
| 3929 | **tigress** | 1 | 2 | - | 332.39 | - | 3,546 | - | 0.000402 | 🔵 low — common in general English | — |
| 3930 | **laced** | 1 | 2 | - | 332.39 | - | 3,547 | - | 0.000402 | 🔵 low — common in general English | — |
| 3931 | **ego** | 1 | 2 | - | 332.39 | - | 3,548 | - | 0.000402 | 🔵 low — common in general English | — |
| 3932 | **craving** | 1 | 2 | - | 332.39 | - | 3,549 | - | 0.000401 | 🔵 low — common in general English | — |
| 3933 | **yourselve** | 1 | 2 | - | 332.39 | - | 3,550 | - | 0.000401 | 🔵 low — common in general English | — |
| 3934 | **armour-like** | 1 | 2 | - | 332.39 | - | 3,551 | - | 0.000401 | 🔵 low — common in general English | — |
| 3935 | **preoccupation** | 1 | 2 | - | 332.39 | - | 3,552 | - | 0.000401 | 🔵 low — common in general English | — |
| 3936 | **diparhkara** | 1 | 2 | - | 332.39 | - | 3,553 | - | 0.000401 | 🔵 low — common in general English | — |
| 3937 | **childish** | 1 | 2 | - | 332.39 | - | 3,554 | - | 0.000401 | 🔵 low — common in general English | — |
| 3938 | **distrac** | 1 | 2 | - | 332.39 | - | 3,555 | - | 0.000401 | 🔵 low — common in general English | — |
| 3939 | **lonely** | 1 | 2 | - | 332.39 | - | 3,556 | - | 0.000401 | 🔵 low — common in general English | — |
| 3940 | **secluded** | 1 | 2 | - | 332.39 | - | 3,557 | - | 0.000401 | 🔵 low — common in general English | — |
| 3941 | **ascetic** | 1 | 2 | - | 332.39 | - | 3,558 | - | 0.000401 | 🔵 low — common in general English | — |
| 3942 | **discerning** | 1 | 2 | - | 332.39 | - | 3,559 | - | 0.000401 | 🔵 low — common in general English | — |
| 3943 | **concen** | 1 | 2 | - | 332.39 | - | 3,560 | - | 0.000401 | 🔵 low — common in general English | — |
| 3944 | **tration** | 1 | 2 | - | 332.39 | - | 3,561 | - | 0.000401 | 🔵 low — common in general English | — |
| 3945 | **athagata** | 1 | 2 | - | 332.39 | - | 3,562 | - | 0.000400 | 🔵 low — common in general English | — |
| 3946 | **equanimity** | 1 | 2 | - | 332.39 | - | 3,563 | - | 0.000400 | 🔵 low — common in general English | — |
| 3947 | **analysi** | 1 | 2 | - | 332.39 | - | 3,564 | - | 0.000400 | 🔵 low — common in general English | — |
| 3948 | **spoilt** | 1 | 2 | - | 332.39 | - | 3,565 | - | 0.000400 | 🔵 low — common in general English | — |
| 3949 | **transcend** | 1 | 2 | - | 332.39 | - | 3,566 | - | 0.000400 | 🔵 low — common in general English | — |
| 3950 | **self-liberation** | 1 | 2 | - | 332.39 | - | 3,567 | - | 0.000400 | 🔵 low — common in general English | — |
| 3951 | **saraha** | 1 | 2 | - | 332.39 | - | 3,568 | - | 0.000400 | 🔵 low — common in general English | ✓ ས་ར་ཧ |
| 3952 | **kharak** | 1 | 2 | - | 332.39 | - | 3,569 | - | 0.000400 | 🔵 low — common in general English | ~ |
| 3953 | **gomchung** | 1 | 2 | - | 332.39 | - | 3,570 | - | 0.000400 | 🔵 low — common in general English | ~ |
| 3954 | **demonic** | 1 | 2 | - | 332.39 | - | 3,571 | - | 0.000400 | 🔵 low — common in general English | — |
| 3955 | **spiritually** | 1 | 2 | - | 332.39 | - | 3,572 | - | 0.000400 | 🔵 low — common in general English | — |
| 3956 | **nachung** | 1 | 2 | - | 332.39 | - | 3,573 | - | 0.000400 | 🔵 low — common in general English | — |
| 3957 | **non-buddhist** | 1 | 2 | - | 332.39 | - | 3,574 | - | 0.000400 | 🔵 low — common in general English | — |
| 3958 | **diminution** | 1 | 2 | - | 332.39 | - | 3,575 | - | 0.000399 | 🔵 low — common in general English | — |
| 3959 | **small-minded** | 1 | 2 | - | 332.39 | - | 3,576 | - | 0.000399 | 🔵 low — common in general English | — |
| 3960 | **cultivating** | 1 | 2 | - | 332.39 | - | 3,577 | - | 0.000399 | 🔵 low — common in general English | — |
| 3961 | **hiding** | 1 | 2 | - | 332.39 | - | 3,578 | - | 0.000399 | 🔵 low — common in general English | — |
| 3962 | **chagme** | 1 | 2 | - | 332.39 | - | 3,579 | - | 0.000399 | 🔵 low — common in general English | ~ |
| 3963 | **necklace** | 1 | 2 | - | 332.39 | - | 3,580 | - | 0.000399 | 🔵 low — common in general English | — |
| 3964 | **perverse** | 1 | 2 | - | 332.39 | - | 3,581 | - | 0.000399 | 🔵 low — common in general English | ~ |
| 3965 | **venge** | 1 | 2 | - | 332.39 | - | 3,582 | - | 0.000399 | 🔵 low — common in general English | — |
| 3966 | **orna** | 1 | 2 | - | 332.39 | - | 3,583 | - | 0.000399 | 🔵 low — common in general English | — |
| 3967 | **appeased** | 1 | 2 | - | 332.39 | - | 3,584 | - | 0.000399 | 🔵 low — common in general English | — |
| 3968 | **navel** | 1 | 2 | - | 332.39 | - | 3,585 | - | 0.000399 | 🔵 low — common in general English | — |
| 3969 | **conch** | 1 | 2 | - | 332.39 | - | 3,586 | - | 0.000399 | 🔵 low — common in general English | — |
| 3970 | **light-ray** | 1 | 2 | - | 332.39 | - | 3,587 | - | 0.000399 | 🔵 low — common in general English | — |
| 3971 | **shapkyu** | 1 | 2 | - | 332.39 | - | 3,588 | - | 0.000399 | 🔵 low — common in general English | ✓ ཞབས་ཀྱུ |
| 3972 | **crescent** | 1 | 2 | - | 332.39 | - | 3,589 | - | 0.000398 | 🔵 low — common in general English | — |
| 3973 | **bindu** | 1 | 2 | - | 332.39 | - | 3,590 | - | 0.000398 | 🔵 low — common in general English | ✓ ཐིག་ལེ |
| 3974 | **nada** | 1 | 2 | - | 332.39 | - | 3,591 | - | 0.000398 | 🔵 low — common in general English | ✓ |
| 3975 | **ofvajrasattva** | 1 | 2 | - | 332.39 | - | 3,592 | - | 0.000398 | 🔵 low — common in general English | — |
| 3976 | **cymbal** | 1 | 2 | - | 332.39 | - | 3,593 | - | 0.000398 | 🔵 low — common in general English | — |
| 3977 | **prayer-book** | 1 | 2 | - | 332.39 | - | 3,594 | - | 0.000398 | 🔵 low — common in general English | — |
| 3978 | **transgressor** | 1 | 2 | - | 332.39 | - | 3,595 | - | 0.000398 | 🔵 low — common in general English | — |
| 3979 | **shingkyong** | 1 | 2 | - | 332.39 | - | 3,596 | - | 0.000398 | 🔵 low — common in general English | — |
| 3980 | **tation** | 1 | 2 | - | 332.39 | - | 3,597 | - | 0.000398 | 🔵 low — common in general English | — |
| 3981 | **sullied** | 1 | 2 | - | 332.39 | - | 3,598 | - | 0.000398 | 🔵 low — common in general English | — |
| 3982 | **snivaka** | 1 | 2 | - | 332.39 | - | 3,599 | - | 0.000398 | 🔵 low — common in general English | — |
| 3983 | **gifted** | 1 | 2 | - | 332.39 | - | 3,600 | - | 0.000398 | 🔵 low — common in general English | — |
| 3984 | **rime** | 1 | 2 | - | 332.39 | - | 3,602 | - | 0.000397 | 🔵 low — common in general English | — |
| 3985 | **underside** | 1 | 2 | - | 332.39 | - | 3,603 | - | 0.000397 | 🔵 low — common in general English | — |
| 3986 | **clockwise** | 1 | 2 | - | 332.39 | - | 3,604 | - | 0.000397 | 🔵 low — common in general English | — |
| 3987 | **multiplying** | 1 | 2 | - | 332.39 | - | 3,605 | - | 0.000397 | 🔵 low — common in general English | — |
| 3988 | **multiplied** | 1 | 2 | - | 332.39 | - | 3,606 | - | 0.000397 | 🔵 low — common in general English | — |
| 3989 | **cleanly** | 1 | 2 | - | 332.39 | - | 3,607 | - | 0.000397 | 🔵 low — common in general English | — |
| 3990 | **churning** | 1 | 2 | - | 332.39 | - | 3,608 | - | 0.000397 | 🔵 low — common in general English | — |
| 3991 | **propitiating** | 1 | 2 | - | 332.39 | - | 3,609 | - | 0.000397 | 🔵 low — common in general English | — |
| 3992 | **ascending** | 1 | 2 | - | 332.39 | - | 3,610 | - | 0.000397 | 🔵 low — common in general English | — |
| 3993 | **eyebrow** | 1 | 2 | - | 332.39 | - | 3,611 | - | 0.000397 | 🔵 low — common in general English | — |
| 3994 | **brow** | 1 | 2 | - | 332.39 | - | 3,612 | - | 0.000397 | 🔵 low — common in general English | — |
| 3995 | **seventy-five** | 1 | 2 | - | 332.39 | - | 3,613 | - | 0.000397 | 🔵 low — common in general English | — |
| 3996 | **imbibe** | 1 | 2 | - | 332.39 | - | 3,614 | - | 0.000397 | 🔵 low — common in general English | — |
| 3997 | **iakini** | 1 | 2 | - | 332.39 | - | 3,615 | - | 0.000397 | 🔵 low — common in general English | — |
| 3998 | **tara** | 1 | 2 | - | 332.39 | - | 3,616 | - | 0.000396 | 🔵 low — common in general English | ✓ སྒྲོལ་མ |
| 3999 | **boast** | 1 | 2 | - | 332.39 | - | 3,617 | - | 0.000396 | 🔵 low — common in general English | — |
| 4000 | **elemental** | 1 | 2 | - | 332.39 | - | 3,618 | - | 0.000396 | 🔵 low — common in general English | — |
| 4001 | **fearsome** | 1 | 2 | - | 332.39 | - | 3,619 | - | 0.000396 | 🔵 low — common in general English | — |
| 4002 | **annihilate** | 1 | 2 | - | 332.39 | - | 3,620 | - | 0.000396 | 🔵 low — common in general English | — |
| 4003 | **prophesied** | 1 | 2 | - | 332.39 | - | 3,621 | - | 0.000396 | 🔵 low — common in general English | — |
| 4004 | **goblin** | 1 | 2 | - | 332.39 | - | 3,622 | - | 0.000396 | 🔵 low — common in general English | — |
| 4005 | **dualistic** | 1 | 2 | - | 332.39 | - | 3,623 | - | 0.000396 | 🔵 low — common in general English | ✓ གཉིས་འཛིན |
| 4006 | **core-teaching** | 1 | 2 | - | 332.39 | - | 3,624 | - | 0.000396 | 🔵 low — common in general English | — |
| 4007 | **fervent** | 1 | 2 | - | 332.39 | - | 3,625 | - | 0.000396 | 🔵 low — common in general English | — |
| 4008 | **drikung** | 1 | 2 | - | 332.39 | - | 3,626 | - | 0.000396 | 🔵 low — common in general English | ~ |
| 4009 | **kyobpa** | 1 | 2 | - | 332.39 | - | 3,627 | - | 0.000396 | 🔵 low — common in general English | ~ |
| 4010 | **intellect** | 1 | 2 | - | 332.39 | - | 3,628 | - | 0.000396 | 🔵 low — common in general English | — |
| 4011 | **trekcho** | 1 | 2 | - | 332.39 | - | 3,629 | - | 0.000395 | 🔵 low — common in general English | — |
| 4012 | **gazing** | 1 | 2 | - | 332.39 | - | 3,630 | - | 0.000395 | 🔵 low — common in general English | — |
| 4013 | **longingly** | 1 | 2 | - | 332.39 | - | 3,631 | - | 0.000395 | 🔵 low — common in general English | — |
| 4014 | **skull-drum** | 1 | 2 | - | 332.39 | - | 3,632 | - | 0.000395 | 🔵 low — common in general English | — |
| 4015 | **charnel-ground** | 1 | 2 | - | 332.39 | - | 3,633 | - | 0.000395 | 🔵 low — common in general English | — |
| 4016 | **zahor** | 1 | 2 | - | 332.39 | - | 3,634 | - | 0.000395 | 🔵 low — common in general English | — |
| 4017 | **symbolizing** | 1 | 2 | - | 332.39 | - | 3,635 | - | 0.000395 | 🔵 low — common in general English | — |
| 4018 | **mudra** | 1 | 2 | - | 332.39 | - | 3,636 | - | 0.000395 | 🔵 low — common in general English | ~ |
| 4019 | **sambhoga** | 1 | 2 | - | 332.39 | - | 3,637 | - | 0.000395 | 🔵 low — common in general English | — |
| 4020 | **five-coloured** | 1 | 2 | - | 332.39 | - | 3,638 | - | 0.000395 | 🔵 low — common in general English | — |
| 4021 | **subjugated** | 1 | 2 | - | 332.39 | - | 3,639 | - | 0.000395 | 🔵 low — common in general English | — |
| 4022 | **luminous** | 1 | 2 | - | 332.39 | - | 3,640 | - | 0.000395 | 🔵 low — common in general English | — |
| 4023 | **sphere** | 1 | 2 | - | 332.39 | - | 3,641 | - | 0.000395 | 🔵 low — common in general English | — |
| 4024 | **knee** | 1 | 2 | - | 332.39 | - | 3,642 | - | 0.000395 | 🔵 low — common in general English | — |
| 4025 | **unfathomable** | 1 | 2 | - | 332.39 | - | 3,643 | - | 0.000394 | 🔵 low — common in general English | — |
| 4026 | **hypocrisy** | 1 | 2 | - | 332.39 | - | 3,644 | - | 0.000394 | 🔵 low — common in general English | — |
| 4027 | **intending** | 1 | 2 | - | 332.39 | - | 3,645 | - | 0.000394 | 🔵 low — common in general English | — |
| 4028 | **entreat** | 1 | 2 | - | 332.39 | - | 3,646 | - | 0.000394 | 🔵 low — common in general English | — |
| 4029 | **upayoga** | 1 | 2 | - | 332.39 | - | 3,647 | - | 0.000394 | 🔵 low — common in general English | — |
| 4030 | **mahayoga** | 1 | 2 | - | 332.39 | - | 3,648 | - | 0.000394 | 🔵 low — common in general English | — |
| 4031 | **anuyoga** | 1 | 2 | - | 332.39 | - | 3,649 | - | 0.000394 | 🔵 low — common in general English | ✓ |
| 4032 | **ofg** | 1 | 2 | - | 332.39 | - | 3,650 | - | 0.000394 | 🔵 low — common in general English | — |
| 4033 | **reat** | 1 | 2 | - | 332.39 | - | 3,651 | - | 0.000394 | 🔵 low — common in general English | — |
| 4034 | **lotus-born** | 1 | 2 | - | 332.39 | - | 3,652 | - | 0.000394 | 🔵 low — common in general English | — |
| 4035 | **ruby** | 1 | 2 | - | 332.39 | - | 3,653 | - | 0.000394 | 🔵 low — common in general English | — |
| 4036 | **muni** | 1 | 2 | - | 332.39 | - | 3,654 | - | 0.000394 | 🔵 low — common in general English | ✓ ཐུབ་པ |
| 4037 | **twenty-eight** | 1 | 2 | - | 332.39 | - | 3,655 | - | 0.000394 | 🔵 low — common in general English | — |
| 4038 | **vajrapat** | 1 | 2 | - | 332.39 | - | 3,656 | - | 0.000394 | 🔵 low — common in general English | — |
| 4039 | **dhanakosa** | 1 | 2 | - | 332.39 | - | 3,657 | - | 0.000393 | 🔵 low — common in general English | — |
| 4040 | **sattvavajra** | 1 | 2 | - | 332.39 | - | 3,658 | - | 0.000393 | 🔵 low — common in general English | ✓ སེམས་དཔའ་རྡོ་རྗེ |
| 4041 | **nine-pointed** | 1 | 2 | - | 332.39 | - | 3,659 | - | 0.000393 | 🔵 low — common in general English | — |
| 4042 | **expans** | 1 | 2 | - | 332.39 | - | 3,660 | - | 0.000393 | 🔵 low — common in general English | — |
| 4043 | **rajahasti** | 1 | 2 | - | 332.39 | - | 3,661 | - | 0.000393 | 🔵 low — common in general English | — |
| 4044 | **paqqita** | 1 | 2 | - | 332.39 | - | 3,662 | - | 0.000393 | 🔵 low — common in general English | — |
| 4045 | **yamantaka** | 1 | 2 | - | 332.39 | - | 3,663 | - | 0.000393 | 🔵 low — common in general English | ✓ གཤིན་རྗེ་གཤེད |
| 4046 | **acarya** | 1 | 2 | - | 332.39 | - | 3,664 | - | 0.000393 | 🔵 low — common in general English | ✓ སློབ་དཔོན |
| 4047 | **non-human** | 1 | 2 | - | 332.39 | - | 3,665 | - | 0.000393 | 🔵 low — common in general English | — |
| 4048 | **genyen** | 1 | 2 | - | 332.39 | - | 3,666 | - | 0.000393 | 🔵 low — common in general English | ~ |
| 4049 | **treasure-discoverer** | 1 | 2 | - | 332.39 | - | 3,667 | - | 0.000393 | 🔵 low — common in general English | — |
| 4050 | **familiarity** | 1 | 2 | - | 332.39 | - | 3,668 | - | 0.000393 | 🔵 low — common in general English | — |
| 4051 | **mahamudra** | 1 | 2 | - | 332.39 | - | 3,669 | - | 0.000393 | 🔵 low — common in general English | ✓ ཕྱག་རྒྱ་ཆེན་པོ |
| 4052 | **ofvajra** | 1 | 2 | - | 332.39 | - | 3,670 | - | 0.000392 | 🔵 low — common in general English | — |
| 4053 | **yogini** | 1 | 2 | - | 332.39 | - | 3,671 | - | 0.000392 | 🔵 low — common in general English | ~ |
| 4054 | **enclosure** | 1 | 2 | - | 332.39 | - | 3,672 | - | 0.000392 | 🔵 low — common in general English | — |
| 4055 | **vibrating** | 1 | 2 | - | 332.39 | - | 3,673 | - | 0.000392 | 🔵 low — common in general English | — |
| 4056 | **mind-awareness** | 1 | 2 | - | 332.39 | - | 3,674 | - | 0.000392 | 🔵 low — common in general English | — |
| 4057 | **kyabje** | 1 | 2 | - | 332.39 | - | 3,675 | - | 0.000392 | 🔵 low — common in general English | — |
| 4058 | **kagyu** | 1 | 2 | - | 332.39 | - | 3,676 | - | 0.000392 | 🔵 low — common in general English | — |
| 4059 | **gampopa** | 1 | 2 | - | 332.39 | - | 3,677 | - | 0.000392 | 🔵 low — common in general English | ~ |
| 4060 | **instruc** | 1 | 2 | - | 332.39 | - | 3,678 | - | 0.000392 | 🔵 low — common in general English | — |
| 4061 | **phras** | 1 | 2 | - | 332.39 | - | 3,679 | - | 0.000392 | 🔵 low — common in general English | — |
| 4062 | **drunk** | 1 | 2 | - | 332.39 | - | 3,680 | - | 0.000392 | 🔵 low — common in general English | — |
| 4063 | **wangpo** | 1 | 2 | - | 332.39 | - | 3,681 | - | 0.000392 | 🔵 low — common in general English | — |
| 4064 | **concerning** | 1 | 3 | - | 331.39 | - | 3,682 | - | 0.000392 | 🔵 low — common in general English | — |
| 4065 | **seriously** | 1 | 3 | - | 331.39 | - | 3,683 | - | 0.000392 | 🔵 low — common in general English | — |
| 4066 | **continued** | 1 | 4 | - | 329.74 | - | 3,684 | - | 0.000391 | 🔵 low — common in general English | — |
| 4067 | **band** | 1 | 3 | - | 329.36 | - | 3,685 | - | 0.000391 | 🔵 low — common in general English | — |
| 4068 | **directly** | 1 | 3 | - | 329.36 | - | 3,686 | - | 0.000391 | 🔵 low — common in general English | — |
| 4069 | **delay** | 1 | 3 | - | 327.39 | - | 3,688 | - | 0.000391 | 🔵 low — common in general English | — |
| 4070 | **detailed** | 1 | 3 | - | 327.39 | - | 3,689 | - | 0.000391 | 🔵 low — common in general English | — |
| 4071 | **island** | 1 | 3 | - | 326.44 | - | 3,690 | - | 0.000391 | 🔵 low — common in general English | — |
| 4072 | **account** | 1 | 4 | - | 325.99 | - | 3,691 | - | 0.000391 | 🔵 low — common in general English | — |
| 4073 | **broad** | 1 | 3 | - | 325.50 | - | 3,692 | - | 0.000391 | 🔵 low — common in general English | — |
| 4074 | **hostile** | 1 | 3 | - | 325.50 | - | 3,693 | - | 0.000391 | 🔵 low — common in general English | — |
| 4075 | **debate** | 1 | 3 | - | 325.50 | - | 3,694 | - | 0.000391 | 🔵 low — common in general English | — |
| 4076 | **status** | 1 | 3 | - | 324.58 | - | 3,695 | - | 0.000391 | 🔵 low — common in general English | — |
| 4077 | **closely** | 1 | 3 | - | 321.92 | - | 3,696 | - | 0.000391 | 🔵 low — common in general English | — |
| 4078 | **test** | 1 | 3 | - | 321.92 | - | 3,697 | - | 0.000391 | 🔵 low — common in general English | — |
| 4079 | **community** | 1 | 4 | - | 321.70 | - | 3,698 | - | 0.000390 | 🔵 low — common in general English | — |
| 4080 | **adopted** | 1 | 3 | - | 319.38 | - | 3,699 | - | 0.000390 | 🔵 low — common in general English | — |
| 4081 | **sheet** | 1 | 3 | - | 319.38 | - | 3,700 | - | 0.000390 | 🔵 low — common in general English | — |
| 4082 | **trader** | 1 | 3 | - | 319.38 | - | 3,701 | - | 0.000390 | 🔵 low — common in general English | — |
| 4083 | **raised** | 1 | 4 | - | 318.59 | - | 3,702 | - | 0.000390 | 🔵 low — common in general English | — |
| 4084 | **prescription** | 1 | 2 | - | 318.44 | - | 3,703 | - | 0.000390 | 🔵 low — common in general English | — |
| 4085 | **excel** | 1 | 2 | - | 318.44 | - | 3,704 | - | 0.000390 | 🔵 low — common in general English | — |
| 4086 | **propensity** | 1 | 2 | - | 318.44 | - | 3,705 | - | 0.000390 | 🔵 low — common in general English | — |
| 4087 | **younger** | 1 | 2 | - | 318.44 | - | 3,706 | - | 0.000390 | 🔵 low — common in general English | — |
| 4088 | **monarch** | 1 | 2 | - | 318.44 | - | 3,707 | - | 0.000390 | 🔵 low — common in general English | ~ |
| 4089 | **festival** | 1 | 2 | - | 318.44 | - | 3,708 | - | 0.000390 | 🔵 low — common in general English | — |
| 4090 | **embraced** | 1 | 2 | - | 318.44 | - | 3,709 | - | 0.000390 | 🔵 low — common in general English | — |
| 4091 | **inheritance** | 1 | 2 | - | 318.44 | - | 3,710 | - | 0.000390 | 🔵 low — common in general English | — |
| 4092 | **wounded** | 1 | 2 | - | 318.44 | - | 3,711 | - | 0.000390 | 🔵 low — common in general English | — |
| 4093 | **misguided** | 1 | 2 | - | 318.44 | - | 3,712 | - | 0.000390 | 🔵 low — common in general English | — |
| 4094 | **rotting** | 1 | 2 | - | 318.44 | - | 3,713 | - | 0.000389 | 🔵 low — common in general English | — |
| 4095 | **trickle** | 1 | 2 | - | 318.44 | - | 3,714 | - | 0.000389 | 🔵 low — common in general English | — |
| 4096 | **misuse** | 1 | 2 | - | 318.44 | - | 3,715 | - | 0.000389 | 🔵 low — common in general English | — |
| 4097 | **revealing** | 1 | 2 | - | 318.44 | - | 3,716 | - | 0.000389 | 🔵 low — common in general English | — |
| 4098 | **flew** | 1 | 2 | - | 318.44 | - | 3,717 | - | 0.000389 | 🔵 low — common in general English | — |
| 4099 | **bury** | 1 | 2 | - | 318.44 | - | 3,718 | - | 0.000389 | 🔵 low — common in general English | — |
| 4100 | **exploited** | 1 | 2 | - | 318.44 | - | 3,719 | - | 0.000389 | 🔵 low — common in general English | — |
| 4101 | **pulling** | 1 | 2 | - | 318.44 | - | 3,720 | - | 0.000389 | 🔵 low — common in general English | — |
| 4102 | **wasting** | 1 | 2 | - | 318.44 | - | 3,721 | - | 0.000389 | 🔵 low — common in general English | — |
| 4103 | **frightened** | 1 | 2 | - | 318.44 | - | 3,722 | - | 0.000389 | 🔵 low — common in general English | — |
| 4104 | **uproot** | 1 | 2 | - | 318.44 | - | 3,723 | - | 0.000389 | 🔵 low — common in general English | — |
| 4105 | **subside** | 1 | 2 | - | 318.44 | - | 3,724 | - | 0.000389 | 🔵 low — common in general English | — |
| 4106 | **monkey** | 1 | 2 | - | 318.44 | - | 3,725 | - | 0.000389 | 🔵 low — common in general English | — |
| 4107 | **echo** | 1 | 2 | - | 318.44 | - | 3,726 | - | 0.000389 | 🔵 low — common in general English | — |
| 4108 | **empty-handed** | 1 | 2 | - | 318.44 | - | 3,727 | - | 0.000388 | 🔵 low — common in general English | — |
| 4109 | **prosper** | 1 | 2 | - | 318.44 | - | 3,728 | - | 0.000388 | 🔵 low — common in general English | — |
| 4110 | **painted** | 1 | 2 | - | 318.44 | - | 3,729 | - | 0.000388 | 🔵 low — common in general English | — |
| 4111 | **confessed** | 1 | 2 | - | 318.44 | - | 3,730 | - | 0.000388 | 🔵 low — common in general English | — |
| 4112 | **childhood** | 1 | 2 | - | 318.44 | - | 3,731 | - | 0.000388 | 🔵 low — common in general English | — |
| 4113 | **falcon** | 1 | 2 | - | 318.44 | - | 3,732 | - | 0.000388 | 🔵 low — common in general English | — |
| 4114 | **fade** | 1 | 2 | - | 318.44 | - | 3,733 | - | 0.000388 | 🔵 low — common in general English | — |
| 4115 | **needy** | 1 | 2 | - | 318.44 | - | 3,734 | - | 0.000388 | 🔵 low — common in general English | — |
| 4116 | **beset** | 1 | 2 | - | 318.44 | - | 3,735 | - | 0.000388 | 🔵 low — common in general English | — |
| 4117 | **pen** | 1 | 2 | - | 318.44 | - | 3,736 | - | 0.000388 | 🔵 low — common in general English | — |
| 4118 | **secondly** | 1 | 2 | - | 318.44 | - | 3,737 | - | 0.000388 | 🔵 low — common in general English | — |
| 4119 | **lifeline** | 1 | 2 | - | 318.44 | - | 3,738 | - | 0.000388 | 🔵 low — common in general English | — |
| 4120 | **embodied** | 1 | 2 | - | 318.44 | - | 3,739 | - | 0.000388 | 🔵 low — common in general English | — |
| 4121 | **disregard** | 1 | 2 | - | 318.44 | - | 3,740 | - | 0.000388 | 🔵 low — common in general English | — |
| 4122 | **dressed** | 1 | 2 | - | 318.44 | - | 3,741 | - | 0.000387 | 🔵 low — common in general English | — |
| 4123 | **richer** | 1 | 2 | - | 318.44 | - | 3,742 | - | 0.000387 | 🔵 low — common in general English | — |
| 4124 | **tamed** | 1 | 2 | - | 318.44 | - | 3,743 | - | 0.000387 | 🔵 low — common in general English | — |
| 4125 | **motivate** | 1 | 2 | - | 318.44 | - | 3,744 | - | 0.000387 | 🔵 low — common in general English | — |
| 4126 | **rounded** | 1 | 2 | - | 318.44 | - | 3,745 | - | 0.000387 | 🔵 low — common in general English | — |
| 4127 | **seventeen** | 1 | 2 | - | 318.44 | - | 3,746 | - | 0.000387 | 🔵 low — common in general English | — |
| 4128 | **incredible** | 1 | 2 | - | 318.44 | - | 3,747 | - | 0.000387 | 🔵 low — common in general English | — |
| 4129 | **subdue** | 1 | 2 | - | 318.44 | - | 3,748 | - | 0.000387 | 🔵 low — common in general English | — |
| 4130 | **wrongdoing** | 1 | 2 | - | 318.44 | - | 3,749 | - | 0.000387 | 🔵 low — common in general English | — |
| 4131 | **bite** | 1 | 2 | - | 318.44 | - | 3,750 | - | 0.000387 | 🔵 low — common in general English | — |
| 4132 | **sentence** | 1 | 2 | - | 318.44 | - | 3,751 | - | 0.000387 | 🔵 low — common in general English | — |
| 4133 | **occupation** | 1 | 2 | - | 318.44 | - | 3,752 | - | 0.000387 | 🔵 low — common in general English | — |
| 4134 | **liked** | 1 | 2 | - | 318.44 | - | 3,753 | - | 0.000387 | 🔵 low — common in general English | — |
| 4135 | **invalid** | 1 | 2 | - | 318.44 | - | 3,754 | - | 0.000387 | 🔵 low — common in general English | — |
| 4136 | **obscured** | 1 | 2 | - | 318.44 | - | 3,755 | - | 0.000387 | 🔵 low — common in general English | — |
| 4137 | **entirety** | 1 | 2 | - | 318.44 | - | 3,756 | - | 0.000386 | 🔵 low — common in general English | — |
| 4138 | **trained** | 1 | 2 | - | 318.44 | - | 3,757 | - | 0.000386 | 🔵 low — common in general English | — |
| 4139 | **flattened** | 1 | 2 | - | 318.44 | - | 3,758 | - | 0.000386 | 🔵 low — common in general English | — |
| 4140 | **owe** | 1 | 2 | - | 318.44 | - | 3,759 | - | 0.000386 | 🔵 low — common in general English | — |
| 4141 | **vengeance** | 1 | 2 | - | 318.44 | - | 3,760 | - | 0.000386 | 🔵 low — common in general English | — |
| 4142 | **spiralling** | 1 | 2 | - | 318.44 | - | 3,761 | - | 0.000386 | 🔵 low — common in general English | — |
| 4143 | **hence** | 1 | 2 | - | 318.44 | - | 3,762 | - | 0.000386 | 🔵 low — common in general English | — |
| 4144 | **narrow** | 1 | 3 | - | 316.96 | - | 3,763 | - | 0.000386 | 🔵 low — common in general English | — |
| 4145 | **wholly** | 1 | 3 | - | 313.16 | - | 3,764 | - | 0.000386 | 🔵 low — common in general English | — |
| 4146 | **acquiring** | 1 | 3 | - | 311.72 | - | 3,765 | - | 0.000386 | 🔵 low — common in general English | — |
| 4147 | **introduced** | 1 | 3 | - | 311.72 | - | 3,766 | - | 0.000386 | 🔵 low — common in general English | — |
| 4148 | **requirement** | 1 | 3 | - | 310.31 | - | 3,767 | - | 0.000386 | 🔵 low — common in general English | — |
| 4149 | **granted** | 1 | 3 | - | 310.31 | - | 3,768 | - | 0.000386 | 🔵 low — common in general English | — |
| 4150 | **earlier** | 1 | 5 | - | 310.05 | - | 3,769 | - | 0.000386 | 🔵 low — common in general English | — |
| 4151 | **encourage** | 1 | 3 | - | 309.63 | - | 3,770 | - | 0.000385 | 🔵 low — common in general English | — |
| 4152 | **intended** | 1 | 3 | - | 309.63 | - | 3,771 | - | 0.000385 | 🔵 low — common in general English | — |
| 4153 | **unaware** | 1 | 2 | - | 308.47 | - | 3,772 | - | 0.000385 | 🔵 low — common in general English | — |
| 4154 | **ignoring** | 1 | 2 | - | 308.47 | - | 3,773 | - | 0.000385 | 🔵 low — common in general English | — |
| 4155 | **tense** | 1 | 2 | - | 308.47 | - | 3,774 | - | 0.000385 | 🔵 low — common in general English | — |
| 4156 | **mode** | 1 | 2 | - | 308.47 | - | 3,775 | - | 0.000385 | 🔵 low — common in general English | — |
| 4157 | **geographically** | 1 | 2 | - | 308.47 | - | 3,776 | - | 0.000385 | 🔵 low — common in general English | — |
| 4158 | **rarely** | 1 | 2 | - | 308.47 | - | 3,777 | - | 0.000385 | 🔵 low — common in general English | — |
| 4159 | **strenuous** | 1 | 2 | - | 308.47 | - | 3,778 | - | 0.000385 | 🔵 low — common in general English | — |
| 4160 | **swimming** | 1 | 2 | - | 308.47 | - | 3,779 | - | 0.000385 | 🔵 low — common in general English | — |
| 4161 | **deliberate** | 1 | 2 | - | 308.47 | - | 3,780 | - | 0.000385 | 🔵 low — common in general English | — |
| 4162 | **pursuit** | 1 | 2 | - | 308.47 | - | 3,781 | - | 0.000385 | 🔵 low — common in general English | — |
| 4163 | **blizzard** | 1 | 2 | - | 308.47 | - | 3,782 | - | 0.000385 | 🔵 low — common in general English | — |
| 4164 | **derive** | 1 | 2 | - | 308.47 | - | 3,783 | - | 0.000385 | 🔵 low — common in general English | — |
| 4165 | **slice** | 1 | 2 | - | 308.47 | - | 3,784 | - | 0.000385 | 🔵 low — common in general English | — |
| 4166 | **grease** | 1 | 2 | - | 308.47 | - | 3,785 | - | 0.000384 | 🔵 low — common in general English | — |
| 4167 | **encountering** | 1 | 2 | - | 308.47 | - | 3,786 | - | 0.000384 | 🔵 low — common in general English | — |
| 4168 | **ploughing** | 1 | 2 | - | 308.47 | - | 3,787 | - | 0.000384 | 🔵 low — common in general English | — |
| 4169 | **digest** | 1 | 2 | - | 308.47 | - | 3,788 | - | 0.000384 | 🔵 low — common in general English | — |
| 4170 | **dim** | 1 | 2 | - | 308.47 | - | 3,789 | - | 0.000384 | 🔵 low — common in general English | — |
| 4171 | **appetite** | 1 | 2 | - | 308.47 | - | 3,790 | - | 0.000384 | 🔵 low — common in general English | — |
| 4172 | **carcass** | 1 | 2 | - | 308.47 | - | 3,791 | - | 0.000384 | 🔵 low — common in general English | — |
| 4173 | **forceful** | 1 | 2 | - | 308.47 | - | 3,792 | - | 0.000384 | 🔵 low — common in general English | — |
| 4174 | **eradicated** | 1 | 2 | - | 308.47 | - | 3,793 | - | 0.000384 | 🔵 low — common in general English | — |
| 4175 | **rift** | 1 | 2 | - | 308.47 | - | 3,794 | - | 0.000384 | 🔵 low — common in general English | — |
| 4176 | **donation** | 1 | 2 | - | 308.47 | - | 3,795 | - | 0.000384 | 🔵 low — common in general English | — |
| 4177 | **excuse** | 1 | 2 | - | 308.47 | - | 3,796 | - | 0.000384 | 🔵 low — common in general English | — |
| 4178 | **donor** | 1 | 2 | - | 308.47 | - | 3,797 | - | 0.000384 | 🔵 low — common in general English | — |
| 4179 | **muddy** | 1 | 2 | - | 308.47 | - | 3,798 | - | 0.000384 | 🔵 low — common in general English | — |
| 4180 | **diversity** | 1 | 2 | - | 308.47 | - | 3,799 | - | 0.000384 | 🔵 low — common in general English | — |
| 4181 | **handed** | 1 | 2 | - | 308.47 | - | 3,800 | - | 0.000383 | 🔵 low — common in general English | — |
| 4182 | **hay** | 1 | 2 | - | 308.47 | - | 3,801 | - | 0.000383 | 🔵 low — common in general English | — |
| 4183 | **permissible** | 1 | 2 | - | 308.47 | - | 3,802 | - | 0.000383 | 🔵 low — common in general English | — |
| 4184 | **impress** | 1 | 2 | - | 308.47 | - | 3,803 | - | 0.000383 | 🔵 low — common in general English | — |
| 4185 | **disturbed** | 1 | 2 | - | 308.47 | - | 3,804 | - | 0.000383 | 🔵 low — common in general English | — |
| 4186 | **checked** | 1 | 2 | - | 308.47 | - | 3,805 | - | 0.000383 | 🔵 low — common in general English | — |
| 4187 | **absorption** | 1 | 2 | - | 308.47 | - | 3,806 | - | 0.000383 | 🔵 low — common in general English | — |
| 4188 | **extraordinarily** | 1 | 2 | - | 308.47 | - | 3,807 | - | 0.000383 | 🔵 low — common in general English | — |
| 4189 | **constrained** | 1 | 2 | - | 308.47 | - | 3,808 | - | 0.000383 | 🔵 low — common in general English | — |
| 4190 | **uncovered** | 1 | 2 | - | 308.47 | - | 3,809 | - | 0.000383 | 🔵 low — common in general English | — |
| 4191 | **sausage** | 1 | 2 | - | 308.47 | - | 3,810 | - | 0.000383 | 🔵 low — common in general English | — |
| 4192 | **ingredient** | 1 | 2 | - | 308.47 | - | 3,811 | - | 0.000383 | 🔵 low — common in general English | — |
| 4193 | **witness** | 1 | 2 | - | 308.47 | - | 3,812 | - | 0.000383 | 🔵 low — common in general English | — |
| 4194 | **vain** | 1 | 2 | - | 308.47 | - | 3,813 | - | 0.000383 | 🔵 low — common in general English | — |
| 4195 | **contamination** | 1 | 2 | - | 308.47 | - | 3,814 | - | 0.000383 | 🔵 low — common in general English | — |
| 4196 | **blend** | 1 | 2 | - | 308.47 | - | 3,816 | - | 0.000382 | 🔵 low — common in general English | — |
| 4197 | **unity** | 1 | 2 | - | 308.47 | - | 3,817 | - | 0.000382 | 🔵 low — common in general English | — |
| 4198 | **satisfying** | 1 | 2 | - | 308.47 | - | 3,818 | - | 0.000382 | 🔵 low — common in general English | — |
| 4199 | **bend** | 1 | 2 | - | 308.47 | - | 3,819 | - | 0.000382 | 🔵 low — common in general English | — |
| 4200 | **successful** | 1 | 3 | - | 307.61 | - | 3,820 | - | 0.000382 | 🔵 low — common in general English | — |
| 4201 | **consideration** | 1 | 3 | - | 306.31 | - | 3,821 | - | 0.000382 | 🔵 low — common in general English | — |
| 4202 | **suspended** | 1 | 3 | - | 305.05 | - | 3,823 | - | 0.000382 | 🔵 low — common in general English | — |
| 4203 | **post** | 1 | 3 | - | 305.05 | - | 3,824 | - | 0.000382 | 🔵 low — common in general English | — |
| 4204 | **interested** | 1 | 3 | - | 304.42 | - | 3,825 | - | 0.000382 | 🔵 low — common in general English | — |
| 4205 | **controlled** | 1 | 3 | - | 303.20 | - | 3,826 | - | 0.000382 | 🔵 low — common in general English | — |
| 4206 | **identifying** | 1 | 2 | - | 300.74 | - | 3,827 | - | 0.000382 | 🔵 low — common in general English | — |
| 4207 | **hunting** | 1 | 2 | - | 300.74 | - | 3,828 | - | 0.000382 | 🔵 low — common in general English | — |
| 4208 | **reward** | 1 | 2 | - | 300.74 | - | 3,829 | - | 0.000382 | 🔵 low — common in general English | — |
| 4209 | **dissatisfaction** | 1 | 2 | - | 300.74 | - | 3,830 | - | 0.000381 | 🔵 low — common in general English | — |
| 4210 | **prestige** | 1 | 2 | - | 300.74 | - | 3,831 | - | 0.000381 | 🔵 low — common in general English | — |
| 4211 | **balancing** | 1 | 2 | - | 300.74 | - | 3,832 | - | 0.000381 | 🔵 low — common in general English | — |
| 4212 | **shrink** | 1 | 2 | - | 300.74 | - | 3,833 | - | 0.000381 | 🔵 low — common in general English | — |
| 4213 | **shorter** | 1 | 2 | - | 300.74 | - | 3,834 | - | 0.000381 | 🔵 low — common in general English | — |
| 4214 | **confronted** | 1 | 2 | - | 300.74 | - | 3,835 | - | 0.000381 | 🔵 low — common in general English | — |
| 4215 | **captured** | 1 | 2 | - | 300.74 | - | 3,836 | - | 0.000381 | 🔵 low — common in general English | — |
| 4216 | **relieved** | 1 | 2 | - | 300.74 | - | 3,837 | - | 0.000381 | 🔵 low — common in general English | — |
| 4217 | **corner** | 1 | 2 | - | 300.74 | - | 3,838 | - | 0.000381 | 🔵 low — common in general English | — |
| 4218 | **mere** | 1 | 2 | - | 300.74 | - | 3,839 | - | 0.000381 | 🔵 low — common in general English | — |
| 4219 | **somehow** | 1 | 2 | - | 300.74 | - | 3,840 | - | 0.000381 | 🔵 low — common in general English | — |
| 4220 | **anyway** | 1 | 2 | - | 300.74 | - | 3,841 | - | 0.000381 | 🔵 low — common in general English | — |
| 4221 | **freely** | 1 | 2 | - | 300.74 | - | 3,842 | - | 0.000381 | 🔵 low — common in general English | — |
| 4222 | **resemble** | 1 | 2 | - | 300.74 | - | 3,843 | - | 0.000381 | 🔵 low — common in general English | — |
| 4223 | **rushed** | 1 | 2 | - | 300.74 | - | 3,844 | - | 0.000381 | 🔵 low — common in general English | — |
| 4224 | **prediction** | 1 | 2 | - | 300.74 | - | 3,845 | - | 0.000380 | 🔵 low — common in general English | — |
| 4225 | **travelled** | 1 | 2 | - | 300.74 | - | 3,846 | - | 0.000380 | 🔵 low — common in general English | — |
| 4226 | **closest** | 1 | 2 | - | 300.74 | - | 3,847 | - | 0.000380 | 🔵 low — common in general English | — |
| 4227 | **unfavourable** | 1 | 2 | - | 300.74 | - | 3,848 | - | 0.000380 | 🔵 low — common in general English | — |
| 4228 | **overwhelming** | 1 | 2 | - | 300.74 | - | 3,849 | - | 0.000380 | 🔵 low — common in general English | — |
| 4229 | **voyage** | 1 | 2 | - | 300.74 | - | 3,850 | - | 0.000380 | 🔵 low — common in general English | — |
| 4230 | **alongside** | 1 | 2 | - | 300.74 | - | 3,851 | - | 0.000380 | 🔵 low — common in general English | — |
| 4231 | **stopping** | 1 | 2 | - | 300.74 | - | 3,852 | - | 0.000380 | 🔵 low — common in general English | — |
| 4232 | **sunbeam** | 1 | 2 | - | 300.74 | - | 3,853 | - | 0.000380 | 🔵 low — common in general English | — |
| 4233 | **guiding** | 1 | 2 | - | 300.74 | - | 3,854 | - | 0.000380 | 🔵 low — common in general English | — |
| 4234 | **failure** | 1 | 3 | - | 299.69 | - | 3,855 | - | 0.000380 | 🔵 low — common in general English | — |
| 4235 | **concerned** | 1 | 3 | - | 298.02 | - | 3,856 | - | 0.000380 | 🔵 low — common in general English | — |
| 4236 | **their** | 1 | 5 | - | 298.02 | - | 3,857 | - | 0.000380 | 🔵 low — common in general English | — |
| 4237 | **preceded** | 1 | 2 | - | 294.42 | - | 3,858 | - | 0.000380 | 🔵 low — common in general English | — |
| 4238 | **freeing** | 1 | 2 | - | 294.42 | - | 3,859 | - | 0.000380 | 🔵 low — common in general English | — |
| 4239 | **fragile** | 1 | 2 | - | 294.42 | - | 3,860 | - | 0.000379 | 🔵 low — common in general English | — |
| 4240 | **chose** | 1 | 2 | - | 294.42 | - | 3,861 | - | 0.000379 | 🔵 low — common in general English | — |
| 4241 | **paradise** | 1 | 2 | - | 294.42 | - | 3,862 | - | 0.000379 | 🔵 low — common in general English | — |
| 4242 | **separation** | 1 | 2 | - | 294.42 | - | 3,863 | - | 0.000379 | 🔵 low — common in general English | — |
| 4243 | **collect** | 1 | 2 | - | 294.42 | - | 3,864 | - | 0.000379 | 🔵 low — common in general English | — |
| 4244 | **leap** | 1 | 2 | - | 294.42 | - | 3,865 | - | 0.000379 | 🔵 low — common in general English | — |
| 4245 | **stranded** | 1 | 2 | - | 294.42 | - | 3,866 | - | 0.000379 | 🔵 low — common in general English | — |
| 4246 | **drift** | 1 | 2 | - | 294.42 | - | 3,867 | - | 0.000379 | 🔵 low — common in general English | — |
| 4247 | **pinpoint** | 1 | 2 | - | 294.42 | - | 3,868 | - | 0.000379 | 🔵 low — common in general English | — |
| 4248 | **addressed** | 1 | 2 | - | 294.42 | - | 3,869 | - | 0.000379 | 🔵 low — common in general English | — |
| 4249 | **reinforce** | 1 | 2 | - | 294.42 | - | 3,870 | - | 0.000379 | 🔵 low — common in general English | — |
| 4250 | **cell** | 1 | 2 | - | 294.42 | - | 3,871 | - | 0.000379 | 🔵 low — common in general English | — |
| 4251 | **dis** | 1 | 2 | - | 294.42 | - | 3,872 | - | 0.000379 | 🔵 low — common in general English | — |
| 4252 | **donated** | 1 | 2 | - | 294.42 | - | 3,873 | - | 0.000379 | 🔵 low — common in general English | — |
| 4253 | **liable** | 1 | 2 | - | 294.42 | - | 3,874 | - | 0.000379 | 🔵 low — common in general English | — |
| 4254 | **matured** | 1 | 2 | - | 294.42 | - | 3,875 | - | 0.000379 | 🔵 low — common in general English | — |
| 4255 | **sailing** | 1 | 2 | - | 294.42 | - | 3,876 | - | 0.000378 | 🔵 low — common in general English | — |
| 4256 | **fulfilling** | 1 | 2 | - | 294.42 | - | 3,877 | - | 0.000378 | 🔵 low — common in general English | ~ |
| 4257 | **mad** | 1 | 2 | - | 294.42 | - | 3,878 | - | 0.000378 | 🔵 low — common in general English | — |
| 4258 | **survival** | 1 | 2 | - | 294.42 | - | 3,879 | - | 0.000378 | 🔵 low — common in general English | — |
| 4259 | **forgiveness** | 1 | 2 | - | 294.42 | - | 3,880 | - | 0.000378 | 🔵 low — common in general English | — |
| 4260 | **rough** | 1 | 2 | - | 294.42 | - | 3,882 | - | 0.000378 | 🔵 low — common in general English | — |
| 4261 | **benefiting** | 1 | 2 | - | 294.42 | - | 3,883 | - | 0.000378 | 🔵 low — common in general English | — |
| 4262 | **bud** | 1 | 2 | - | 294.42 | - | 3,884 | - | 0.000378 | 🔵 low — common in general English | — |
| 4263 | **whichever** | 1 | 2 | - | 294.42 | - | 3,885 | - | 0.000378 | 🔵 low — common in general English | — |
| 4264 | **sam** | 1 | 2 | - | 294.42 | - | 3,886 | - | 0.000378 | 🔵 low — common in general English | — |
| 4265 | **soften** | 1 | 2 | - | 294.42 | - | 3,887 | - | 0.000378 | 🔵 low — common in general English | — |
| 4266 | **foremost** | 1 | 2 | - | 294.42 | - | 3,888 | - | 0.000378 | 🔵 low — common in general English | — |
| 4267 | **agree** | 1 | 3 | - | 293.82 | - | 3,889 | - | 0.000378 | 🔵 low — common in general English | — |
| 4268 | **equivalent** | 1 | 3 | - | 292.82 | - | 3,890 | - | 0.000378 | 🔵 low — common in general English | — |
| 4269 | **normal** | 1 | 3 | - | 292.33 | - | 3,891 | - | 0.000377 | 🔵 low — common in general English | — |
| 4270 | **system** | 1 | 4 | - | 291.58 | - | 3,892 | - | 0.000377 | 🔵 low — common in general English | — |
| 4271 | **completion** | 1 | 3 | - | 289.93 | - | 3,893 | - | 0.000377 | 🔵 low — common in general English | — |
| 4272 | **dispute** | 1 | 3 | - | 289.47 | - | 3,894 | - | 0.000377 | 🔵 low — common in general English | — |
| 4273 | **opened** | 1 | 3 | - | 289.47 | - | 3,895 | - | 0.000377 | 🔵 low — common in general English | — |
| 4274 | **sold** | 1 | 4 | - | 289.09 | - | 3,896 | - | 0.000377 | 🔵 low — common in general English | — |
| 4275 | **subdued** | 1 | 2 | - | 289.07 | - | 3,897 | - | 0.000377 | 🔵 low — common in general English | — |
| 4276 | **valuable** | 1 | 2 | - | 289.07 | - | 3,898 | - | 0.000377 | 🔵 low — common in general English | — |
| 4277 | **patch** | 1 | 2 | - | 289.07 | - | 3,899 | - | 0.000377 | 🔵 low — common in general English | — |
| 4278 | **seized** | 1 | 2 | - | 289.07 | - | 3,900 | - | 0.000377 | 🔵 low — common in general English | — |
| 4279 | **observed** | 1 | 2 | - | 289.07 | - | 3,901 | - | 0.000377 | 🔵 low — common in general English | — |
| 4280 | **patient** | 1 | 2 | - | 289.07 | - | 3,902 | - | 0.000377 | 🔵 low — common in general English | — |
| 4281 | **hired** | 1 | 2 | - | 289.07 | - | 3,903 | - | 0.000377 | 🔵 low — common in general English | — |
| 4282 | **anybody** | 1 | 2 | - | 289.07 | - | 3,904 | - | 0.000377 | 🔵 low — common in general English | — |
| 4283 | **tate** | 1 | 2 | - | 289.07 | - | 3,905 | - | 0.000377 | 🔵 low — common in general English | — |
| 4284 | **abundant** | 1 | 2 | - | 289.07 | - | 3,906 | - | 0.000377 | 🔵 low — common in general English | — |
| 4285 | **style** | 1 | 2 | - | 289.07 | - | 3,907 | - | 0.000376 | 🔵 low — common in general English | — |
| 4286 | **requesting** | 1 | 2 | - | 289.07 | - | 3,908 | - | 0.000376 | 🔵 low — common in general English | — |
| 4287 | **reflected** | 1 | 3 | - | 289.00 | - | 3,909 | - | 0.000376 | 🔵 low — common in general English | — |
| 4288 | **unconditional** | 1 | 2 | - | 284.45 | - | 3,910 | - | 0.000376 | 🔵 low — common in general English | — |
| 4289 | **influenced** | 1 | 2 | - | 284.45 | - | 3,912 | - | 0.000376 | 🔵 low — common in general English | — |
| 4290 | **geography** | 1 | 2 | - | 284.45 | - | 3,913 | - | 0.000376 | 🔵 low — common in general English | — |
| 4291 | **existed** | 1 | 2 | - | 284.45 | - | 3,914 | - | 0.000376 | 🔵 low — common in general English | — |
| 4292 | **older** | 1 | 2 | - | 284.45 | - | 3,915 | - | 0.000376 | 🔵 low — common in general English | — |
| 4293 | **struggle** | 1 | 2 | - | 284.45 | - | 3,916 | - | 0.000376 | 🔵 low — common in general English | — |
| 4294 | **cheating** | 1 | 2 | - | 284.45 | - | 3,917 | - | 0.000376 | 🔵 low — common in general English | — |
| 4295 | **peg** | 1 | 2 | - | 284.45 | - | 3,918 | - | 0.000376 | 🔵 low — common in general English | — |
| 4296 | **lined** | 1 | 2 | - | 284.45 | - | 3,919 | - | 0.000376 | 🔵 low — common in general English | — |
| 4297 | **helpful** | 1 | 2 | - | 284.45 | - | 3,920 | - | 0.000376 | 🔵 low — common in general English | — |
| 4298 | **abandoning** | 1 | 2 | - | 284.45 | - | 3,921 | - | 0.000376 | 🔵 low — common in general English | — |
| 4299 | **relax** | 1 | 2 | - | 284.45 | - | 3,922 | - | 0.000376 | 🔵 low — common in general English | — |
| 4300 | **unique** | 1 | 2 | - | 284.45 | - | 3,923 | - | 0.000375 | 🔵 low — common in general English | — |
| 4301 | **tug** | 1 | 2 | - | 284.45 | - | 3,924 | - | 0.000375 | 🔵 low — common in general English | — |
| 4302 | **undoubtedly** | 1 | 2 | - | 284.45 | - | 3,925 | - | 0.000375 | 🔵 low — common in general English | — |
| 4303 | **released** | 1 | 3 | - | 284.17 | - | 3,926 | - | 0.000375 | 🔵 low — common in general English | — |
| 4304 | **steel** | 1 | 3 | - | 282.12 | - | 3,927 | - | 0.000375 | 🔵 low — common in general English | — |
| 4305 | **entertain** | 1 | 2 | - | 280.36 | - | 3,928 | - | 0.000375 | 🔵 low — common in general English | — |
| 4306 | **burned** | 1 | 2 | - | 280.36 | - | 3,929 | - | 0.000375 | 🔵 low — common in general English | — |
| 4307 | **impressed** | 1 | 2 | - | 280.36 | - | 3,930 | - | 0.000375 | 🔵 low — common in general English | — |
| 4308 | **composed** | 1 | 2 | - | 280.36 | - | 3,931 | - | 0.000375 | 🔵 low — common in general English | — |
| 4309 | **fulfilled** | 1 | 2 | - | 280.36 | - | 3,932 | - | 0.000375 | 🔵 low — common in general English | — |
| 4310 | **stretch** | 1 | 2 | - | 280.36 | - | 3,933 | - | 0.000375 | 🔵 low — common in general English | — |
| 4311 | **insignificant** | 1 | 2 | - | 280.36 | - | 3,934 | - | 0.000375 | 🔵 low — common in general English | — |
| 4312 | **attracting** | 1 | 2 | - | 280.36 | - | 3,935 | - | 0.000375 | 🔵 low — common in general English | ~ |
| 4313 | **saving** | 1 | 2 | - | 280.36 | - | 3,936 | - | 0.000375 | 🔵 low — common in general English | — |
| 4314 | **comfortably** | 1 | 2 | - | 280.36 | - | 3,937 | - | 0.000375 | 🔵 low — common in general English | — |
| 4315 | **eliminating** | 1 | 2 | - | 280.36 | - | 3,938 | - | 0.000375 | 🔵 low — common in general English | — |
| 4316 | **repaired** | 1 | 2 | - | 280.36 | - | 3,939 | - | 0.000374 | 🔵 low — common in general English | — |
| 4317 | **attempt** | 1 | 3 | - | 280.14 | - | 3,940 | - | 0.000374 | 🔵 low — common in general English | — |
| 4318 | **improve** | 1 | 3 | - | 279.37 | - | 3,941 | - | 0.000374 | 🔵 low — common in general English | — |
| 4319 | **considering** | 1 | 3 | - | 278.99 | - | 3,942 | - | 0.000374 | 🔵 low — common in general English | — |
| 4320 | **steering** | 1 | 2 | - | 276.71 | - | 3,943 | - | 0.000374 | 🔵 low — common in general English | — |
| 4321 | **absorbed** | 1 | 2 | - | 276.71 | - | 3,944 | - | 0.000374 | 🔵 low — common in general English | — |
| 4322 | **eighth** | 1 | 2 | - | 276.71 | - | 3,945 | - | 0.000374 | 🔵 low — common in general English | — |
| 4323 | **diminish** | 1 | 2 | - | 276.71 | - | 3,946 | - | 0.000374 | 🔵 low — common in general English | — |
| 4324 | **impression** | 1 | 2 | - | 276.71 | - | 3,947 | - | 0.000374 | 🔵 low — common in general English | — |
| 4325 | **pool** | 1 | 2 | - | 276.71 | - | 3,948 | - | 0.000374 | 🔵 low — common in general English | — |
| 4326 | **rare** | 1 | 2 | - | 276.71 | - | 3,949 | - | 0.000374 | 🔵 low — common in general English | — |
| 4327 | **sinking** | 1 | 2 | - | 276.71 | - | 3,950 | - | 0.000374 | 🔵 low — common in general English | — |
| 4328 | **ice** | 1 | 2 | - | 276.71 | - | 3,951 | - | 0.000374 | 🔵 low — common in general English | — |
| 4329 | **lock** | 1 | 2 | - | 276.71 | - | 3,953 | - | 0.000374 | 🔵 low — common in general English | — |
| 4330 | **bitter** | 1 | 2 | - | 276.71 | - | 3,954 | - | 0.000374 | 🔵 low — common in general English | — |
| 4331 | **unhappy** | 1 | 2 | - | 276.71 | - | 3,955 | - | 0.000373 | 🔵 low — common in general English | — |
| 4332 | **consumed** | 1 | 2 | - | 276.71 | - | 3,956 | - | 0.000373 | 🔵 low — common in general English | — |
| 4333 | **examination** | 1 | 2 | - | 276.71 | - | 3,957 | - | 0.000373 | 🔵 low — common in general English | — |
| 4334 | **sank** | 1 | 2 | - | 276.71 | - | 3,958 | - | 0.000373 | 🔵 low — common in general English | — |
| 4335 | **school** | 1 | 2 | - | 276.71 | - | 3,959 | - | 0.000373 | 🔵 low — common in general English | — |
| 4336 | **positively** | 1 | 2 | - | 276.71 | - | 3,960 | - | 0.000373 | 🔵 low — common in general English | — |
| 4337 | **shape** | 1 | 2 | - | 276.71 | - | 3,961 | - | 0.000373 | 🔵 low — common in general English | — |
| 4338 | **fixed** | 1 | 3 | - | 274.28 | - | 3,962 | - | 0.000373 | 🔵 low — common in general English | — |
| 4339 | **soar** | 1 | 2 | - | 273.41 | - | 3,963 | - | 0.000373 | 🔵 low — common in general English | — |
| 4340 | **safely** | 1 | 2 | - | 273.41 | - | 3,964 | - | 0.000373 | 🔵 low — common in general English | — |
| 4341 | **vowed** | 1 | 2 | - | 273.41 | - | 3,965 | - | 0.000373 | 🔵 low — common in general English | — |
| 4342 | **picked** | 1 | 2 | - | 273.41 | - | 3,966 | - | 0.000373 | 🔵 low — common in general English | — |
| 4343 | **survive** | 1 | 2 | - | 273.41 | - | 3,967 | - | 0.000373 | 🔵 low — common in general English | — |
| 4344 | **rolled** | 1 | 2 | - | 273.41 | - | 3,968 | - | 0.000373 | 🔵 low — common in general English | — |
| 4345 | **frequent** | 1 | 2 | - | 273.41 | - | 3,969 | - | 0.000373 | 🔵 low — common in general English | — |
| 4346 | **searching** | 1 | 2 | - | 273.41 | - | 3,970 | - | 0.000373 | 🔵 low — common in general English | — |
| 4347 | **sovereignty** | 1 | 2 | - | 273.41 | - | 3,971 | - | 0.000372 | 🔵 low — common in general English | — |
| 4348 | **bull** | 1 | 2 | - | 273.41 | - | 3,972 | - | 0.000372 | 🔵 low — common in general English | — |
| 4349 | **praised** | 1 | 2 | - | 273.41 | - | 3,973 | - | 0.000372 | 🔵 low — common in general English | — |
| 4350 | **exceptionally** | 1 | 2 | - | 273.41 | - | 3,974 | - | 0.000372 | 🔵 low — common in general English | — |
| 4351 | **changed** | 1 | 3 | - | 273.25 | - | 3,975 | - | 0.000372 | 🔵 low — common in general English | — |
| 4352 | **united** | 1 | 4 | - | 271.96 | - | 3,976 | - | 0.000372 | 🔵 low — common in general English | — |
| 4353 | **one-day** | 1 | 2 | - | 270.39 | - | 3,977 | - | 0.000372 | 🔵 low — common in general English | — |
| 4354 | **arguing** | 1 | 2 | - | 270.39 | - | 3,978 | - | 0.000372 | 🔵 low — common in general English | — |
| 4355 | **permanently** | 1 | 2 | - | 270.39 | - | 3,979 | - | 0.000372 | 🔵 low — common in general English | — |
| 4356 | **unnecessary** | 1 | 2 | - | 270.39 | - | 3,980 | - | 0.000372 | 🔵 low — common in general English | — |
| 4357 | **vein** | 1 | 2 | - | 270.39 | - | 3,981 | - | 0.000372 | 🔵 low — common in general English | — |
| 4358 | **stiff** | 1 | 2 | - | 270.39 | - | 3,982 | - | 0.000372 | 🔵 low — common in general English | — |
| 4359 | **capacity** | 1 | 3 | - | 269.96 | - | 3,983 | - | 0.000372 | 🔵 low — common in general English | — |
| 4360 | **provision** | 1 | 3 | - | 269.96 | - | 3,984 | - | 0.000372 | 🔵 low — common in general English | — |
| 4361 | **limited** | 1 | 3 | - | 267.77 | - | 3,985 | - | 0.000372 | 🔵 low — common in general English | — |
| 4362 | **worrying** | 1 | 2 | - | 267.62 | - | 3,986 | - | 0.000372 | 🔵 low — common in general English | — |
| 4363 | **collapsed** | 1 | 2 | - | 267.62 | - | 3,987 | - | 0.000371 | 🔵 low — common in general English | — |
| 4364 | **eagle** | 1 | 2 | - | 267.62 | - | 3,988 | - | 0.000371 | 🔵 low — common in general English | — |
| 4365 | **stepped** | 1 | 2 | - | 267.62 | - | 3,989 | - | 0.000371 | 🔵 low — common in general English | — |
| 4366 | **pill** | 1 | 2 | - | 267.62 | - | 3,990 | - | 0.000371 | 🔵 low — common in general English | — |
| 4367 | **flying** | 1 | 2 | - | 267.62 | - | 3,991 | - | 0.000371 | 🔵 low — common in general English | — |
| 4368 | **sticking** | 1 | 2 | - | 267.62 | - | 3,992 | - | 0.000371 | 🔵 low — common in general English | — |
| 4369 | **installed** | 1 | 2 | - | 267.62 | - | 3,993 | - | 0.000371 | 🔵 low — common in general English | — |
| 4370 | **steam** | 1 | 2 | - | 267.62 | - | 3,994 | - | 0.000371 | 🔵 low — common in general English | — |
| 4371 | **briefly** | 1 | 2 | - | 267.62 | - | 3,995 | - | 0.000371 | 🔵 low — common in general English | — |
| 4372 | **remaining** | 1 | 3 | - | 265.38 | - | 3,996 | - | 0.000371 | 🔵 low — common in general English | — |
| 4373 | **continuing** | 1 | 3 | - | 265.38 | - | 3,997 | - | 0.000371 | 🔵 low — common in general English | — |
| 4374 | **picking** | 1 | 2 | - | 265.05 | - | 3,998 | - | 0.000371 | 🔵 low — common in general English | — |
| 4375 | **pursuing** | 1 | 2 | - | 265.05 | - | 3,999 | - | 0.000371 | 🔵 low — common in general English | — |
| 4376 | **territory** | 1 | 2 | - | 265.05 | - | 4,000 | - | 0.000371 | 🔵 low — common in general English | — |
| 4377 | **strictly** | 1 | 2 | - | 265.05 | - | 4,001 | - | 0.000371 | 🔵 low — common in general English | — |
| 4378 | **approaching** | 1 | 2 | - | 265.05 | - | 4,002 | - | 0.000371 | 🔵 low — common in general English | — |
| 4379 | **postpone** | 1 | 2 | - | 265.05 | - | 4,003 | - | 0.000371 | 🔵 low — common in general English | — |
| 4380 | **dip** | 1 | 2 | - | 265.05 | - | 4,004 | - | 0.000370 | 🔵 low — common in general English | — |
| 4381 | **recognition** | 1 | 2 | - | 265.05 | - | 4,005 | - | 0.000370 | 🔵 low — common in general English | — |
| 4382 | **wrote** | 1 | 2 | - | 265.05 | - | 4,008 | - | 0.000370 | 🔵 low — common in general English | — |
| 4383 | **cycle** | 1 | 2 | - | 262.66 | - | 4,009 | - | 0.000370 | 🔵 low — common in general English | — |
| 4384 | **sown** | 1 | 2 | - | 262.66 | - | 4,010 | - | 0.000370 | 🔵 low — common in general English | — |
| 4385 | **tend** | 1 | 2 | - | 262.66 | - | 4,011 | - | 0.000370 | 🔵 low — common in general English | — |
| 4386 | **pulp** | 1 | 2 | - | 262.66 | - | 4,012 | - | 0.000370 | 🔵 low — common in general English | — |
| 4387 | **treated** | 1 | 2 | - | 262.66 | - | 4,013 | - | 0.000370 | 🔵 low — common in general English | — |
| 4388 | **refrain** | 1 | 2 | - | 262.66 | - | 4,014 | - | 0.000370 | 🔵 low — common in general English | — |
| 4389 | **repaid** | 1 | 2 | - | 262.66 | - | 4,015 | - | 0.000370 | 🔵 low — common in general English | — |
| 4390 | **recognized** | 1 | 2 | - | 262.66 | - | 4,016 | - | 0.000370 | 🔵 low — common in general English | — |
| 4391 | **earning** | 1 | 2 | - | 260.42 | - | 4,017 | - | 0.000370 | 🔵 low — common in general English | — |
| 4392 | **engage** | 1 | 2 | - | 260.42 | - | 4,018 | - | 0.000370 | 🔵 low — common in general English | — |
| 4393 | **counsel** | 1 | 2 | - | 260.42 | - | 4,019 | - | 0.000370 | 🔵 low — common in general English | — |
| 4394 | **framework** | 1 | 2 | - | 260.42 | - | 4,020 | - | 0.000369 | 🔵 low — common in general English | — |
| 4395 | **science** | 1 | 2 | - | 260.42 | - | 4,021 | - | 0.000369 | 🔵 low — common in general English | — |
| 4396 | **fund** | 1 | 3 | - | 260.37 | - | 4,022 | - | 0.000369 | 🔵 low — common in general English | — |
| 4397 | **key** | 1 | 3 | - | 260.11 | - | 4,023 | - | 0.000369 | 🔵 low — common in general English | — |
| 4398 | **resort** | 1 | 2 | - | 258.32 | - | 4,024 | - | 0.000369 | 🔵 low — common in general English | — |
| 4399 | **passenger** | 1 | 2 | - | 258.32 | - | 4,025 | - | 0.000369 | 🔵 low — common in general English | — |
| 4400 | **latter** | 1 | 2 | - | 258.32 | - | 4,026 | - | 0.000369 | 🔵 low — common in general English | — |
| 4401 | **establishing** | 1 | 2 | - | 258.32 | - | 4,027 | - | 0.000369 | 🔵 low — common in general English | — |
| 4402 | **sudden** | 1 | 2 | - | 258.32 | - | 4,028 | - | 0.000369 | 🔵 low — common in general English | — |
| 4403 | **pat** | 1 | 2 | - | 258.32 | - | 4,029 | - | 0.000369 | 🔵 low — common in general English | — |
| 4404 | **payment** | 1 | 3 | - | 258.04 | - | 4,030 | - | 0.000369 | 🔵 low — common in general English | — |
| 4405 | **greatly** | 1 | 2 | - | 256.34 | - | 4,031 | - | 0.000369 | 🔵 low — common in general English | — |
| 4406 | **preparation** | 1 | 2 | - | 256.34 | - | 4,032 | - | 0.000369 | 🔵 low — common in general English | ~ |
| 4407 | **flowing** | 1 | 2 | - | 256.34 | - | 4,033 | - | 0.000369 | 🔵 low — common in general English | — |
| 4408 | **creditor** | 1 | 2 | - | 256.34 | - | 4,034 | - | 0.000369 | 🔵 low — common in general English | — |
| 4409 | **due** | 1 | 4 | - | 256.30 | - | 4,035 | - | 0.000369 | 🔵 low — common in general English | — |
| 4410 | **afford** | 1 | 2 | - | 254.47 | - | 4,036 | - | 0.000369 | 🔵 low — common in general English | — |
| 4411 | **pretty** | 1 | 2 | - | 254.47 | - | 4,037 | - | 0.000368 | 🔵 low — common in general English | — |
| 4412 | **climb** | 1 | 2 | - | 254.47 | - | 4,038 | - | 0.000368 | 🔵 low — common in general English | — |
| 4413 | **injured** | 1 | 2 | - | 254.47 | - | 4,039 | - | 0.000368 | 🔵 low — common in general English | — |
| 4414 | **population** | 1 | 2 | - | 252.69 | - | 4,040 | - | 0.000368 | 🔵 low — common in general English | — |
| 4415 | **shared** | 1 | 2 | - | 252.69 | - | 4,041 | - | 0.000368 | 🔵 low — common in general English | — |
| 4416 | **competitor** | 1 | 2 | - | 252.69 | - | 4,042 | - | 0.000368 | 🔵 low — common in general English | — |
| 4417 | **violating** | 1 | 2 | - | 252.69 | - | 4,043 | - | 0.000368 | 🔵 low — common in general English | — |
| 4418 | **bridge** | 1 | 2 | - | 252.69 | - | 4,044 | - | 0.000368 | 🔵 low — common in general English | — |
| 4419 | **referred** | 1 | 2 | - | 252.69 | - | 4,045 | - | 0.000368 | 🔵 low — common in general English | — |
| 4420 | **joining** | 1 | 2 | - | 252.69 | - | 4,046 | - | 0.000368 | 🔵 low — common in general English | ~ |
| 4421 | **renew** | 1 | 2 | - | 252.69 | - | 4,047 | - | 0.000368 | 🔵 low — common in general English | — |
| 4422 | **escort** | 1 | 2 | - | 251.00 | - | 4,048 | - | 0.000368 | 🔵 low — common in general English | — |
| 4423 | **restored** | 1 | 2 | - | 251.00 | - | 4,049 | - | 0.000368 | 🔵 low — common in general English | — |
| 4424 | **obviously** | 1 | 2 | - | 249.38 | - | 4,051 | - | 0.000368 | 🔵 low — common in general English | — |
| 4425 | **troubled** | 1 | 2 | - | 249.38 | - | 4,052 | - | 0.000368 | 🔵 low — common in general English | — |
| 4426 | **argued** | 1 | 2 | - | 249.38 | - | 4,053 | - | 0.000368 | 🔵 low — common in general English | — |
| 4427 | **attract** | 1 | 2 | - | 249.38 | - | 4,054 | - | 0.000367 | 🔵 low — common in general English | — |
| 4428 | **exception** | 1 | 2 | - | 249.38 | - | 4,055 | - | 0.000367 | 🔵 low — common in general English | — |
| 4429 | **consulting** | 1 | 2 | - | 249.38 | - | 4,056 | - | 0.000367 | 🔵 low — common in general English | — |
| 4430 | **chief** | 1 | 3 | - | 247.93 | - | 4,057 | - | 0.000367 | 🔵 low — common in general English | — |
| 4431 | **blocked** | 1 | 2 | - | 247.84 | - | 4,058 | - | 0.000367 | 🔵 low — common in general English | — |
| 4432 | **maybe** | 1 | 2 | - | 247.84 | - | 4,059 | - | 0.000367 | 🔵 low — common in general English | — |
| 4433 | **quarter** | 1 | 4 | - | 247.53 | - | 4,060 | - | 0.000367 | 🔵 low — common in general English | — |
| 4434 | **wet** | 1 | 2 | - | 246.37 | - | 4,061 | - | 0.000367 | 🔵 low — common in general English | — |
| 4435 | **dependent** | 1 | 2 | - | 246.37 | - | 4,062 | - | 0.000367 | 🔵 low — common in general English | — |
| 4436 | **usual** | 1 | 2 | - | 244.95 | - | 4,063 | - | 0.000367 | 🔵 low — common in general English | — |
| 4437 | **struck** | 1 | 2 | - | 244.95 | - | 4,065 | - | 0.000367 | 🔵 low — common in general English | — |
| 4438 | **transferred** | 1 | 2 | - | 244.95 | - | 4,066 | - | 0.000367 | 🔵 low — common in general English | — |
| 4439 | **stem** | 1 | 2 | - | 244.95 | - | 4,067 | - | 0.000367 | 🔵 low — common in general English | — |
| 4440 | **underground** | 1 | 2 | - | 243.59 | - | 4,069 | - | 0.000367 | 🔵 low — common in general English | — |
| 4441 | **paid** | 1 | 3 | - | 242.58 | - | 4,070 | - | 0.000367 | 🔵 low — common in general English | — |
| 4442 | **pattern** | 1 | 2 | - | 242.29 | - | 4,071 | - | 0.000366 | 🔵 low — common in general English | — |
| 4443 | **tension** | 1 | 2 | - | 242.29 | - | 4,072 | - | 0.000366 | 🔵 low — common in general English | — |
| 4444 | **attracted** | 1 | 2 | - | 242.29 | - | 4,073 | - | 0.000366 | 🔵 low — common in general English | — |
| 4445 | **fifth** | 1 | 2 | - | 242.29 | - | 4,074 | - | 0.000366 | 🔵 low — common in general English | — |
| 4446 | **club** | 1 | 2 | - | 242.29 | - | 4,075 | - | 0.000366 | 🔵 low — common in general English | — |
| 4447 | **react** | 1 | 2 | - | 242.29 | - | 4,076 | - | 0.000366 | 🔵 low — common in general English | — |
| 4448 | **neutral** | 1 | 2 | - | 242.29 | - | 4,077 | - | 0.000366 | 🔵 low — common in general English | — |
| 4449 | **steep** | 1 | 2 | - | 242.29 | - | 4,078 | - | 0.000366 | 🔵 low — common in general English | — |
| 4450 | **added** | 1 | 4 | - | 241.42 | - | 4,079 | - | 0.000366 | 🔵 low — common in general English | — |
| 4451 | **dropping** | 1 | 2 | - | 241.03 | - | 4,080 | - | 0.000366 | 🔵 low — common in general English | — |
| 4452 | **product** | 1 | 3 | - | 240.54 | - | 4,081 | - | 0.000366 | 🔵 low — common in general English | — |
| 4453 | **additional** | 1 | 3 | - | 240.00 | - | 4,082 | - | 0.000366 | 🔵 low — common in general English | — |
| 4454 | **badly** | 1 | 2 | - | 239.81 | - | 4,083 | - | 0.000366 | 🔵 low — common in general English | — |
| 4455 | **heating** | 1 | 2 | - | 239.81 | - | 4,084 | - | 0.000366 | 🔵 low — common in general English | — |
| 4456 | **calm** | 1 | 2 | - | 239.81 | - | 4,085 | - | 0.000366 | 🔵 low — common in general English | ~ |
| 4457 | **approached** | 1 | 2 | - | 239.81 | - | 4,086 | - | 0.000366 | 🔵 low — common in general English | — |
| 4458 | **safety** | 1 | 2 | - | 239.81 | - | 4,087 | - | 0.000366 | 🔵 low — common in general English | — |
| 4459 | **address** | 1 | 2 | - | 239.81 | - | 4,088 | - | 0.000365 | 🔵 low — common in general English | — |
| 4460 | **promised** | 1 | 2 | - | 239.81 | - | 4,089 | - | 0.000365 | 🔵 low — common in general English | — |
| 4461 | **late** | 1 | 3 | - | 238.76 | - | 4,090 | - | 0.000365 | 🔵 low — common in general English | — |
| 4462 | **tire** | 1 | 2 | - | 238.63 | - | 4,091 | - | 0.000365 | 🔵 low — common in general English | — |
| 4463 | **preparing** | 1 | 2 | - | 238.63 | - | 4,092 | - | 0.000365 | 🔵 low — common in general English | — |
| 4464 | **appointed** | 1 | 2 | - | 238.63 | - | 4,093 | - | 0.000365 | 🔵 low — common in general English | — |
| 4465 | **treatment** | 1 | 2 | - | 235.33 | - | 4,094 | - | 0.000365 | 🔵 low — common in general English | — |
| 4466 | **pushing** | 1 | 2 | - | 235.33 | - | 4,095 | - | 0.000365 | 🔵 low — common in general English | — |
| 4467 | **acceptable** | 1 | 2 | - | 235.33 | - | 4,096 | - | 0.000365 | 🔵 low — common in general English | — |
| 4468 | **maintaining** | 1 | 2 | - | 235.33 | - | 4,097 | - | 0.000365 | 🔵 low — common in general English | — |
| 4469 | **priority** | 1 | 2 | - | 234.30 | - | 4,099 | - | 0.000365 | 🔵 low — common in general English | — |
| 4470 | **encouraged** | 1 | 2 | - | 234.30 | - | 4,100 | - | 0.000365 | 🔵 low — common in general English | — |
| 4471 | **balanced** | 1 | 2 | - | 233.29 | - | 4,101 | - | 0.000365 | 🔵 low — common in general English | — |
| 4472 | **tonight** | 1 | 2 | - | 233.29 | - | 4,102 | - | 0.000365 | 🔵 low — common in general English | — |
| 4473 | **announcing** | 1 | 2 | - | 232.32 | - | 4,103 | - | 0.000365 | 🔵 low — common in general English | — |
| 4474 | **marked** | 1 | 2 | - | 232.32 | - | 4,104 | - | 0.000365 | 🔵 low — common in general English | — |
| 4475 | **failing** | 1 | 2 | - | 231.37 | - | 4,105 | - | 0.000364 | 🔵 low — common in general English | — |
| 4476 | **bidding** | 1 | 2 | - | 231.37 | - | 4,106 | - | 0.000364 | 🔵 low — common in general English | — |
| 4477 | **occurred** | 1 | 2 | - | 231.37 | - | 4,107 | - | 0.000364 | 🔵 low — common in general English | — |
| 4478 | **settle** | 1 | 2 | - | 231.37 | - | 4,108 | - | 0.000364 | 🔵 low — common in general English | — |
| 4479 | **seemed** | 1 | 2 | - | 231.37 | - | 4,109 | - | 0.000364 | 🔵 low — common in general English | — |
| 4480 | **complex** | 1 | 2 | - | 231.37 | - | 4,110 | - | 0.000364 | 🔵 low — common in general English | — |
| 4481 | **prospect** | 1 | 2 | - | 229.54 | - | 4,111 | - | 0.000364 | 🔵 low — common in general English | — |
| 4482 | **indication** | 1 | 2 | - | 229.54 | - | 4,112 | - | 0.000364 | 🔵 low — common in general English | — |
| 4483 | **broke** | 1 | 2 | - | 229.54 | - | 4,113 | - | 0.000364 | 🔵 low — common in general English | — |
| 4484 | **conditioned** | 1 | 2 | - | 229.54 | - | 4,114 | - | 0.000364 | 🔵 low — common in general English | ✓ འདུས་བྱས |
| 4485 | **twice** | 1 | 2 | - | 228.66 | - | 4,115 | - | 0.000364 | 🔵 low — common in general English | — |
| 4486 | **outright** | 1 | 2 | - | 228.66 | - | 4,116 | - | 0.000364 | 🔵 low — common in general English | — |
| 4487 | **recommend** | 1 | 2 | - | 228.66 | - | 4,117 | - | 0.000364 | 🔵 low — common in general English | — |
| 4488 | **sufficient** | 1 | 2 | - | 228.66 | - | 4,118 | - | 0.000364 | 🔵 low — common in general English | — |
| 4489 | **measured** | 1 | 2 | - | 227.81 | - | 4,119 | - | 0.000364 | 🔵 low — common in general English | — |
| 4490 | **core** | 1 | 2 | - | 226.97 | - | 4,120 | - | 0.000364 | 🔵 low — common in general English | — |
| 4491 | **welcomed** | 1 | 2 | - | 226.97 | - | 4,121 | - | 0.000364 | 🔵 low — common in general English | — |
| 4492 | **comprising** | 1 | 2 | - | 226.16 | - | 4,122 | - | 0.000364 | 🔵 low — common in general English | — |
| 4493 | **headed** | 1 | 2 | - | 225.36 | - | 4,123 | - | 0.000363 | 🔵 low — common in general English | — |
| 4494 | **lifted** | 1 | 2 | - | 225.36 | - | 4,124 | - | 0.000363 | 🔵 low — common in general English | — |
| 4495 | **comparable** | 1 | 2 | - | 225.36 | - | 4,125 | - | 0.000363 | 🔵 low — common in general English | — |
| 4496 | **frozen** | 1 | 2 | - | 224.58 | - | 4,126 | - | 0.000363 | 🔵 low — common in general English | — |
| 4497 | **involving** | 1 | 2 | - | 224.58 | - | 4,127 | - | 0.000363 | 🔵 low — common in general English | — |
| 4498 | **tight** | 1 | 2 | - | 223.82 | - | 4,128 | - | 0.000363 | 🔵 low — common in general English | — |
| 4499 | **supply** | 1 | 3 | - | 223.29 | - | 4,129 | - | 0.000363 | 🔵 low — common in general English | — |
| 4500 | **contribute** | 1 | 2 | - | 223.07 | - | 4,130 | - | 0.000363 | 🔵 low — common in general English | — |
| 4501 | **room** | 1 | 2 | - | 223.07 | - | 4,131 | - | 0.000363 | 🔵 low — common in general English | — |
| 4502 | **faced** | 1 | 2 | - | 223.07 | - | 4,132 | - | 0.000363 | 🔵 low — common in general English | — |
| 4503 | **contained** | 1 | 2 | - | 223.07 | - | 4,133 | - | 0.000363 | 🔵 low — common in general English | — |
| 4504 | **flat** | 1 | 2 | - | 223.07 | - | 4,134 | - | 0.000363 | 🔵 low — common in general English | — |
| 4505 | **value** | 1 | 3 | - | 222.51 | - | 4,135 | - | 0.000363 | 🔵 low — common in general English | — |
| 4506 | **social** | 1 | 2 | - | 221.63 | - | 4,136 | - | 0.000363 | 🔵 low — common in general English | — |
| 4507 | **plan** | 1 | 3 | - | 221.37 | - | 4,137 | - | 0.000363 | 🔵 low — common in general English | — |
| 4508 | **depending** | 1 | 2 | - | 220.93 | - | 4,138 | - | 0.000363 | 🔵 low — common in general English | — |
| 4509 | **so-called** | 1 | 2 | - | 220.93 | - | 4,139 | - | 0.000363 | 🔵 low — common in general English | — |
| 4510 | **internal** | 1 | 2 | - | 220.24 | - | 4,140 | - | 0.000362 | 🔵 low — common in general English | — |
| 4511 | **rapid** | 1 | 2 | - | 220.24 | - | 4,141 | - | 0.000362 | 🔵 low — common in general English | — |
| 4512 | **proceed** | 1 | 2 | - | 220.24 | - | 4,142 | - | 0.000362 | 🔵 low — common in general English | — |
| 4513 | **likely** | 1 | 3 | - | 219.40 | - | 4,143 | - | 0.000362 | 🔵 low — common in general English | — |
| 4514 | **evidence** | 1 | 2 | - | 218.91 | - | 4,144 | - | 0.000362 | 🔵 low — common in general English | — |
| 4515 | **normally** | 1 | 2 | - | 217.63 | - | 4,145 | - | 0.000362 | 🔵 low — common in general English | — |
| 4516 | **competitiveness** | 1 | 2 | - | 217.00 | - | 4,146 | - | 0.000362 | 🔵 low — common in general English | — |
| 4517 | **decrease** | 1 | 2 | - | 217.00 | - | 4,147 | - | 0.000362 | 🔵 low — common in general English | — |
| 4518 | **structure** | 1 | 2 | - | 216.39 | - | 4,148 | - | 0.000362 | 🔵 low — common in general English | — |
| 4519 | **double** | 1 | 2 | - | 215.79 | - | 4,149 | - | 0.000362 | 🔵 low — common in general English | — |
| 4520 | **brown** | 1 | 2 | - | 215.79 | - | 4,150 | - | 0.000362 | 🔵 low — common in general English | — |
| 4521 | **retain** | 1 | 2 | - | 215.19 | - | 4,151 | - | 0.000362 | 🔵 low — common in general English | — |
| 4522 | **partner** | 1 | 2 | - | 214.61 | - | 4,152 | - | 0.000362 | 🔵 low — common in general English | — |
| 4523 | **fallen** | 1 | 2 | - | 214.04 | - | 4,153 | - | 0.000362 | 🔵 low — common in general English | — |
| 4524 | **participation** | 1 | 2 | - | 214.04 | - | 4,154 | - | 0.000362 | 🔵 low — common in general English | — |
| 4525 | **advanced** | 1 | 2 | - | 213.47 | - | 4,155 | - | 0.000362 | 🔵 low — common in general English | — |
| 4526 | **ruled** | 1 | 2 | - | 211.84 | - | 4,156 | - | 0.000362 | 🔵 low — common in general English | — |
| 4527 | **primarily** | 1 | 2 | - | 211.84 | - | 4,157 | - | 0.000362 | 🔵 low — common in general English | — |
| 4528 | **suit** | 1 | 2 | - | 211.84 | - | 4,158 | - | 0.000361 | 🔵 low — common in general English | — |
| 4529 | **staff** | 1 | 2 | - | 210.79 | - | 4,160 | - | 0.000361 | 🔵 low — common in general English | — |
| 4530 | **depressed** | 1 | 2 | - | 209.27 | - | 4,161 | - | 0.000361 | 🔵 low — common in general English | — |
| 4531 | **threatened** | 1 | 2 | - | 209.27 | - | 4,162 | - | 0.000361 | 🔵 low — common in general English | — |
| 4532 | **strongly** | 1 | 2 | - | 209.27 | - | 4,163 | - | 0.000361 | 🔵 low — common in general English | — |
| 4533 | **stake** | 1 | 3 | - | 209.25 | - | 4,164 | - | 0.000361 | 🔵 low — common in general English | — |
| 4534 | **discussed** | 1 | 2 | - | 207.34 | - | 4,166 | - | 0.000361 | 🔵 low — common in general English | — |
| 4535 | **pound** | 1 | 2 | - | 206.42 | - | 4,167 | - | 0.000361 | 🔵 low — common in general English | — |
| 4536 | **vegetable** | 1 | 2 | - | 206.42 | - | 4,168 | - | 0.000361 | 🔵 low — common in general English | — |
| 4537 | **larger** | 1 | 2 | - | 205.52 | - | 4,169 | - | 0.000361 | 🔵 low — common in general English | — |
| 4538 | **copper** | 1 | 2 | - | 205.52 | - | 4,170 | - | 0.000361 | 🔵 low — common in general English | ~ |
| 4539 | **smaller** | 1 | 2 | - | 205.08 | - | 4,171 | - | 0.000361 | 🔵 low — common in general English | — |
| 4540 | **asset** | 1 | 2 | - | 204.64 | - | 4,172 | - | 0.000361 | 🔵 low — common in general English | — |
| 4541 | **grew** | 1 | 2 | - | 204.21 | - | 4,173 | - | 0.000361 | 🔵 low — common in general English | — |
| 4542 | **release** | 1 | 2 | - | 202.13 | - | 4,174 | - | 0.000361 | 🔵 low — common in general English | — |
| 4543 | **forward** | 1 | 2 | - | 202.13 | - | 4,175 | - | 0.000361 | 🔵 low — common in general English | — |
| 4544 | **strategy** | 1 | 2 | - | 201.34 | - | 4,176 | - | 0.000360 | 🔵 low — common in general English | — |
| 4545 | **buy** | 1 | 3 | - | 195.62 | - | 4,177 | - | 0.000360 | 🔵 low — common in general English | — |
| 4546 | **helped** | 1 | 2 | - | 195.21 | - | 4,178 | - | 0.000360 | 🔵 low — common in general English | — |
| 4547 | **primary** | 1 | 2 | - | 193.60 | - | 4,179 | - | 0.000360 | 🔵 low — common in general English | — |
| 4548 | **majority** | 1 | 2 | - | 190.88 | - | 4,180 | - | 0.000360 | 🔵 low — common in general English | — |
| 4549 | **combined** | 1 | 2 | - | 190.01 | - | 4,181 | - | 0.000360 | 🔵 low — common in general English | — |
| 4550 | **paper** | 1 | 2 | - | 189.17 | - | 4,182 | - | 0.000360 | 🔵 low — common in general English | — |
| 4551 | **outlook** | 1 | 2 | - | 188.62 | - | 4,183 | - | 0.000360 | 🔵 low — common in general English | — |
| 4552 | **southern** | 1 | 2 | - | 187.81 | - | 4,184 | - | 0.000360 | 🔵 low — common in general English | — |
| 4553 | **existing** | 1 | 2 | - | 186.25 | - | 4,185 | - | 0.000360 | 🔵 low — common in general English | — |
| 4554 | **aimed** | 1 | 2 | - | 185.74 | - | 4,186 | - | 0.000360 | 🔵 low — common in general English | — |
| 4555 | **unlikely** | 1 | 2 | - | 185.49 | - | 4,187 | - | 0.000360 | 🔵 low — common in general English | — |
| 4556 | **affected** | 1 | 2 | - | 185.24 | - | 4,188 | - | 0.000360 | 🔵 low — common in general English | — |
| 4557 | **discuss** | 1 | 2 | - | 185.00 | - | 4,189 | - | 0.000360 | 🔵 low — common in general English | — |
| 4558 | **dropped** | 1 | 2 | - | 185.00 | - | 4,190 | - | 0.000360 | 🔵 low — common in general English | — |
| 4559 | **court** | 1 | 2 | - | 185.00 | - | 4,191 | - | 0.000360 | 🔵 low — common in general English | — |
| 4560 | **spending** | 1 | 2 | - | 183.55 | - | 4,192 | - | 0.000360 | 🔵 low — common in general English | — |
| 4561 | **ahead** | 1 | 2 | - | 183.08 | - | 4,193 | - | 0.000360 | 🔵 low — common in general English | — |
| 4562 | **current** | 1 | 3 | - | 179.81 | - | 4,194 | - | 0.000359 | 🔵 low — common in general English | — |
| 4563 | **mainly** | 1 | 2 | - | 179.13 | - | 4,195 | - | 0.000359 | 🔵 low — common in general English | — |
| 4564 | **quoted** | 1 | 2 | - | 177.51 | - | 4,196 | - | 0.000359 | 🔵 low — common in general English | — |
| 4565 | **price** | 1 | 3 | - | 175.34 | - | 4,197 | - | 0.000359 | 🔵 low — common in general English | — |
| 4566 | **crop** | 1 | 2 | - | 171.69 | - | 4,198 | - | 0.000359 | 🔵 low — common in general English | — |
| 4567 | **letter** | 1 | 2 | - | 171.19 | - | 4,199 | - | 0.000359 | 🔵 low — common in general English | — |
| 4568 | **area** | 1 | 2 | - | 170.54 | - | 4,200 | - | 0.000359 | 🔵 low — common in general English | — |
| 4569 | **addition** | 1 | 2 | - | 169.58 | - | 4,201 | - | 0.000359 | 🔵 low — common in general English | — |
| 4570 | **fed** | 1 | 2 | - | 169.42 | - | 4,202 | - | 0.000359 | 🔵 low — common in general English | — |
| 4571 | **planned** | 1 | 2 | - | 168.95 | - | 4,203 | - | 0.000359 | 🔵 low — common in general English | — |
| 4572 | **accord** | 1 | 2 | - | 168.34 | - | 4,204 | - | 0.000359 | 🔵 low — common in general English | — |
| 4573 | **expect** | 1 | 2 | - | 167.59 | - | 4,205 | - | 0.000359 | 🔵 low — common in general English | — |
| 4574 | **group** | 1 | 3 | - | 166.26 | - | 4,206 | - | 0.000359 | 🔵 low — common in general English | — |
| 4575 | **audi** | 1 | 1 | - | 166.25 | - | 4,207 | - | 0.000359 | 🔵 low — common in general English | — |
| 4576 | **ale** | 1 | 1 | - | 166.25 | - | 4,208 | - | 0.000359 | 🔵 low — common in general English | — |
| 4577 | **leak** | 1 | 1 | - | 166.25 | - | 4,209 | - | 0.000359 | 🔵 low — common in general English | — |
| 4578 | **trusting** | 1 | 1 | - | 166.25 | - | 4,210 | - | 0.000359 | 🔵 low — common in general English | — |
| 4579 | **flavour** | 1 | 1 | - | 166.25 | - | 4,211 | - | 0.000359 | 🔵 low — common in general English | — |
| 4580 | **digging** | 1 | 1 | - | 166.25 | - | 4,212 | - | 0.000358 | 🔵 low — common in general English | — |
| 4581 | **incorrectly** | 1 | 1 | - | 166.25 | - | 4,213 | - | 0.000358 | 🔵 low — common in general English | — |
| 4582 | **expedient** | 1 | 1 | - | 166.25 | - | 4,214 | - | 0.000358 | 🔵 low — common in general English | ~ |
| 4583 | **medication** | 1 | 1 | - | 166.25 | - | 4,215 | - | 0.000358 | 🔵 low — common in general English | — |
| 4584 | **comprehend** | 1 | 1 | - | 166.25 | - | 4,216 | - | 0.000358 | 🔵 low — common in general English | — |
| 4585 | **make-up** | 1 | 1 | - | 166.25 | - | 4,217 | - | 0.000358 | 🔵 low — common in general English | — |
| 4586 | **ensue** | 1 | 1 | - | 166.25 | - | 4,218 | - | 0.000358 | 🔵 low — common in general English | — |
| 4587 | **flagrant** | 1 | 1 | - | 166.25 | - | 4,219 | - | 0.000358 | 🔵 low — common in general English | — |
| 4588 | **autonomy** | 1 | 1 | - | 166.25 | - | 4,220 | - | 0.000358 | 🔵 low — common in general English | — |
| 4589 | **preoccupied** | 1 | 1 | - | 166.25 | - | 4,221 | - | 0.000358 | 🔵 low — common in general English | — |
| 4590 | **entailed** | 1 | 1 | - | 166.25 | - | 4,222 | - | 0.000358 | 🔵 low — common in general English | — |
| 4591 | **westward** | 1 | 1 | - | 166.25 | - | 4,223 | - | 0.000358 | 🔵 low — common in general English | — |
| 4592 | **fruitful** | 1 | 1 | - | 166.25 | - | 4,224 | - | 0.000358 | 🔵 low — common in general English | — |
| 4593 | **coincidence** | 1 | 1 | - | 166.25 | - | 4,225 | - | 0.000358 | 🔵 low — common in general English | — |
| 4594 | **circular** | 1 | 1 | - | 166.25 | - | 4,226 | - | 0.000358 | 🔵 low — common in general English | — |
| 4595 | **fuse** | 1 | 1 | - | 166.25 | - | 4,227 | - | 0.000358 | 🔵 low — common in general English | — |
| 4596 | **flare** | 1 | 1 | - | 166.25 | - | 4,228 | - | 0.000358 | 🔵 low — common in general English | — |
| 4597 | **torrential** | 1 | 1 | - | 166.25 | - | 4,229 | - | 0.000358 | 🔵 low — common in general English | — |
| 4598 | **wielding** | 1 | 1 | - | 166.25 | - | 4,230 | - | 0.000357 | 🔵 low — common in general English | — |
| 4599 | **good-looking** | 1 | 1 | - | 166.25 | - | 4,231 | - | 0.000357 | 🔵 low — common in general English | — |
| 4600 | **horror** | 1 | 1 | - | 166.25 | - | 4,232 | - | 0.000357 | 🔵 low — common in general English | — |
| 4601 | **cemetery** | 1 | 1 | - | 166.25 | - | 4,233 | - | 0.000357 | 🔵 low — common in general English | — |
| 4602 | **unsatisfied** | 1 | 1 | - | 166.25 | - | 4,234 | - | 0.000357 | 🔵 low — common in general English | — |
| 4603 | **reconciled** | 1 | 1 | - | 166.25 | - | 4,235 | - | 0.000357 | 🔵 low — common in general English | — |
| 4604 | **authoritative** | 1 | 1 | - | 166.25 | - | 4,236 | - | 0.000357 | 🔵 low — common in general English | — |
| 4605 | **aging** | 1 | 1 | - | 166.25 | - | 4,237 | - | 0.000357 | 🔵 low — common in general English | — |
| 4606 | **disenchanted** | 1 | 1 | - | 166.25 | - | 4,238 | - | 0.000357 | 🔵 low — common in general English | — |
| 4607 | **brave** | 1 | 1 | - | 166.25 | - | 4,239 | - | 0.000357 | 🔵 low — common in general English | — |
| 4608 | **recklessly** | 1 | 1 | - | 166.25 | - | 4,240 | - | 0.000357 | 🔵 low — common in general English | — |
| 4609 | **demise** | 1 | 1 | - | 166.25 | - | 4,241 | - | 0.000357 | 🔵 low — common in general English | — |
| 4610 | **enduring** | 1 | 1 | - | 166.25 | - | 4,242 | - | 0.000357 | 🔵 low — common in general English | — |
| 4611 | **suffice** | 1 | 1 | - | 166.25 | - | 4,243 | - | 0.000357 | 🔵 low — common in general English | — |
| 4612 | **unsurpassed** | 1 | 1 | - | 166.25 | - | 4,244 | - | 0.000357 | 🔵 low — common in general English | — |
| 4613 | **constellation** | 1 | 1 | - | 166.25 | - | 4,245 | - | 0.000357 | 🔵 low — common in general English | — |
| 4614 | **trident** | 1 | 1 | - | 166.25 | - | 4,246 | - | 0.000357 | 🔵 low — common in general English | — |
| 4615 | **toss** | 1 | 1 | - | 166.25 | - | 4,247 | - | 0.000357 | 🔵 low — common in general English | — |
| 4616 | **trench** | 1 | 1 | - | 166.25 | - | 4,248 | - | 0.000357 | 🔵 low — common in general English | — |
| 4617 | **chewing** | 1 | 1 | - | 166.25 | - | 4,249 | - | 0.000356 | 🔵 low — common in general English | — |
| 4618 | **snowy** | 1 | 1 | - | 166.25 | - | 4,250 | - | 0.000356 | 🔵 low — common in general English | — |
| 4619 | **lastly** | 1 | 1 | - | 166.25 | - | 4,251 | - | 0.000356 | 🔵 low — common in general English | — |
| 4620 | **sacrificed** | 1 | 1 | - | 166.25 | - | 4,252 | - | 0.000356 | 🔵 low — common in general English | — |
| 4621 | **commanding** | 1 | 1 | - | 166.25 | - | 4,253 | - | 0.000356 | 🔵 low — common in general English | — |
| 4622 | **rang** | 1 | 1 | - | 166.25 | - | 4,254 | - | 0.000356 | 🔵 low — common in general English | — |
| 4623 | **orchard** | 1 | 1 | - | 166.25 | - | 4,255 | - | 0.000356 | 🔵 low — common in general English | — |
| 4624 | **fever** | 1 | 1 | - | 166.25 | - | 4,256 | - | 0.000356 | 🔵 low — common in general English | — |
| 4625 | **gigantic** | 1 | 1 | - | 166.25 | - | 4,257 | - | 0.000356 | 🔵 low — common in general English | — |
| 4626 | **horde** | 1 | 1 | - | 166.25 | - | 4,258 | - | 0.000356 | 🔵 low — common in general English | — |
| 4627 | **offload** | 1 | 1 | - | 166.25 | - | 4,259 | - | 0.000356 | 🔵 low — common in general English | — |
| 4628 | **comprehension** | 1 | 1 | - | 166.25 | - | 4,260 | - | 0.000356 | 🔵 low — common in general English | — |
| 4629 | **fas** | 1 | 1 | - | 166.25 | - | 4,261 | - | 0.000356 | 🔵 low — common in general English | — |
| 4630 | **snare** | 1 | 1 | - | 166.25 | - | 4,262 | - | 0.000356 | 🔵 low — common in general English | — |
| 4631 | **otter** | 1 | 1 | - | 166.25 | - | 4,263 | - | 0.000356 | 🔵 low — common in general English | — |
| 4632 | **musk-oxen** | 1 | 1 | - | 166.25 | - | 4,264 | - | 0.000356 | 🔵 low — common in general English | — |
| 4633 | **irrigated** | 1 | 1 | - | 166.25 | - | 4,265 | - | 0.000356 | 🔵 low — common in general English | — |
| 4634 | **rightful** | 1 | 1 | - | 166.25 | - | 4,266 | - | 0.000356 | 🔵 low — common in general English | — |
| 4635 | **propped** | 1 | 1 | - | 166.25 | - | 4,267 | - | 0.000356 | 🔵 low — common in general English | — |
| 4636 | **imbalanced** | 1 | 1 | - | 166.25 | - | 4,268 | - | 0.000355 | 🔵 low — common in general English | — |
| 4637 | **bedding** | 1 | 1 | - | 166.25 | - | 4,269 | - | 0.000355 | 🔵 low — common in general English | — |
| 4638 | **daytime** | 1 | 1 | - | 166.25 | - | 4,270 | - | 0.000355 | 🔵 low — common in general English | — |
| 4639 | **overtake** | 1 | 1 | - | 166.25 | - | 4,271 | - | 0.000355 | 🔵 low — common in general English | — |
| 4640 | **colder** | 1 | 1 | - | 166.25 | - | 4,272 | - | 0.000355 | 🔵 low — common in general English | — |
| 4641 | **lure** | 1 | 1 | - | 166.25 | - | 4,273 | - | 0.000355 | 🔵 low — common in general English | — |
| 4642 | **kin** | 1 | 1 | - | 166.25 | - | 4,274 | - | 0.000355 | 🔵 low — common in general English | — |
| 4643 | **punished** | 1 | 1 | - | 166.25 | - | 4,275 | - | 0.000355 | 🔵 low — common in general English | — |
| 4644 | **engulfed** | 1 | 1 | - | 166.25 | - | 4,276 | - | 0.000355 | 🔵 low — common in general English | — |
| 4645 | **overwhelm** | 1 | 1 | - | 166.25 | - | 4,277 | - | 0.000355 | 🔵 low — common in general English | — |
| 4646 | **oceanic** | 1 | 1 | - | 166.25 | - | 4,278 | - | 0.000355 | 🔵 low — common in general English | — |
| 4647 | **transported** | 1 | 1 | - | 166.25 | - | 4,279 | - | 0.000355 | 🔵 low — common in general English | — |
| 4648 | **inexorable** | 1 | 1 | - | 166.25 | - | 4,280 | - | 0.000355 | 🔵 low — common in general English | — |
| 4649 | **mooring** | 1 | 1 | - | 166.25 | - | 4,281 | - | 0.000355 | 🔵 low — common in general English | — |
| 4650 | **lymph** | 1 | 1 | - | 166.25 | - | 4,282 | - | 0.000355 | 🔵 low — common in general English | — |
| 4651 | **prolific** | 1 | 1 | - | 166.25 | - | 4,283 | - | 0.000355 | 🔵 low — common in general English | — |
| 4652 | **shocked** | 1 | 1 | - | 166.25 | - | 4,284 | - | 0.000355 | 🔵 low — common in general English | — |
| 4653 | **disdain** | 1 | 1 | - | 166.25 | - | 4,285 | - | 0.000355 | 🔵 low — common in general English | — |
| 4654 | **overpowering** | 1 | 1 | - | 166.25 | - | 4,286 | - | 0.000354 | 🔵 low — common in general English | — |
| 4655 | **seizure** | 1 | 1 | - | 166.25 | - | 4,287 | - | 0.000354 | 🔵 low — common in general English | — |
| 4656 | **knuckle** | 1 | 1 | - | 166.25 | - | 4,288 | - | 0.000354 | 🔵 low — common in general English | — |
| 4657 | **shin** | 1 | 1 | - | 166.25 | - | 4,289 | - | 0.000354 | 🔵 low — common in general English | — |
| 4658 | **indulge** | 1 | 1 | - | 166.25 | - | 4,290 | - | 0.000354 | 🔵 low — common in general English | — |
| 4659 | **ethic** | 1 | 1 | - | 166.25 | - | 4,291 | - | 0.000354 | 🔵 low — common in general English | — |
| 4660 | **daylight** | 1 | 1 | - | 166.25 | - | 4,292 | - | 0.000354 | 🔵 low — common in general English | — |
| 4661 | **unsightly** | 1 | 1 | - | 166.25 | - | 4,293 | - | 0.000354 | 🔵 low — common in general English | — |
| 4662 | **congregation** | 1 | 1 | - | 166.25 | - | 4,294 | - | 0.000354 | 🔵 low — common in general English | — |
| 4663 | **summed** | 1 | 1 | - | 166.25 | - | 4,295 | - | 0.000354 | 🔵 low — common in general English | — |
| 4664 | **commentator** | 1 | 1 | - | 166.25 | - | 4,296 | - | 0.000354 | 🔵 low — common in general English | — |
| 4665 | **receiver** | 1 | 1 | - | 166.25 | - | 4,297 | - | 0.000354 | 🔵 low — common in general English | — |
| 4666 | **differently** | 1 | 1 | - | 166.25 | - | 4,298 | - | 0.000354 | 🔵 low — common in general English | — |
| 4667 | **destiny** | 1 | 1 | - | 166.25 | - | 4,299 | - | 0.000354 | 🔵 low — common in general English | — |
| 4668 | **loot** | 1 | 1 | - | 166.25 | - | 4,300 | - | 0.000354 | 🔵 low — common in general English | — |
| 4669 | **falsely** | 1 | 1 | - | 166.25 | - | 4,301 | - | 0.000354 | 🔵 low — common in general English | — |
| 4670 | **accusation** | 1 | 1 | - | 166.25 | - | 4,302 | - | 0.000354 | 🔵 low — common in general English | — |
| 4671 | **recalcitrant** | 1 | 1 | - | 166.25 | - | 4,303 | - | 0.000354 | 🔵 low — common in general English | — |
| 4672 | **grim** | 1 | 1 | - | 166.25 | - | 4,304 | - | 0.000354 | 🔵 low — common in general English | — |
| 4673 | **oblige** | 1 | 1 | - | 166.25 | - | 4,305 | - | 0.000353 | 🔵 low — common in general English | — |
| 4674 | **seamless** | 1 | 1 | - | 166.25 | - | 4,306 | - | 0.000353 | 🔵 low — common in general English | — |
| 4675 | **plucked** | 1 | 1 | - | 166.25 | - | 4,307 | - | 0.000353 | 🔵 low — common in general English | — |
| 4676 | **squarely** | 1 | 1 | - | 166.25 | - | 4,308 | - | 0.000353 | 🔵 low — common in general English | — |
| 4677 | **noticed** | 1 | 1 | - | 166.25 | - | 4,309 | - | 0.000353 | 🔵 low — common in general English | — |
| 4678 | **finer** | 1 | 1 | - | 166.25 | - | 4,310 | - | 0.000353 | 🔵 low — common in general English | — |
| 4679 | **ingenuity** | 1 | 1 | - | 166.25 | - | 4,311 | - | 0.000353 | 🔵 low — common in general English | — |
| 4680 | **prohibition** | 1 | 1 | - | 166.25 | - | 4,312 | - | 0.000353 | 🔵 low — common in general English | — |
| 4681 | **conformity** | 1 | 1 | - | 166.25 | - | 4,313 | - | 0.000353 | 🔵 low — common in general English | — |
| 4682 | **purest** | 1 | 1 | - | 166.25 | - | 4,314 | - | 0.000353 | 🔵 low — common in general English | — |
| 4683 | **incomprehensible** | 1 | 1 | - | 166.25 | - | 4,316 | - | 0.000353 | 🔵 low — common in general English | — |
| 4684 | **enquire** | 1 | 1 | - | 166.25 | - | 4,317 | - | 0.000353 | 🔵 low — common in general English | — |
| 4685 | **conveyance** | 1 | 1 | - | 166.25 | - | 4,318 | - | 0.000353 | 🔵 low — common in general English | — |
| 4686 | **tread** | 1 | 1 | - | 166.25 | - | 4,319 | - | 0.000353 | 🔵 low — common in general English | — |
| 4687 | **sation** | 1 | 1 | - | 166.25 | - | 4,320 | - | 0.000353 | 🔵 low — common in general English | — |
| 4688 | **smoothly** | 1 | 1 | - | 166.25 | - | 4,321 | - | 0.000353 | 🔵 low — common in general English | — |
| 4689 | **respecting** | 1 | 1 | - | 166.25 | - | 4,322 | - | 0.000353 | 🔵 low — common in general English | — |
| 4690 | **reproduce** | 1 | 1 | - | 166.25 | - | 4,323 | - | 0.000353 | 🔵 low — common in general English | — |
| 4691 | **lethargy** | 1 | 1 | - | 166.25 | - | 4,324 | - | 0.000352 | 🔵 low — common in general English | — |
| 4692 | **avenue** | 1 | 1 | - | 166.25 | - | 4,325 | - | 0.000352 | 🔵 low — common in general English | — |
| 4693 | **makin** | 1 | 1 | - | 166.25 | - | 4,326 | - | 0.000352 | 🔵 low — common in general English | — |
| 4694 | **harden** | 1 | 1 | - | 166.25 | - | 4,327 | - | 0.000352 | 🔵 low — common in general English | — |
| 4695 | **debating** | 1 | 1 | - | 166.25 | - | 4,328 | - | 0.000352 | 🔵 low — common in general English | — |
| 4696 | **appropriated** | 1 | 1 | - | 166.25 | - | 4,329 | - | 0.000352 | 🔵 low — common in general English | — |
| 4697 | **demolished** | 1 | 1 | - | 166.25 | - | 4,330 | - | 0.000352 | 🔵 low — common in general English | — |
| 4698 | **thrashing** | 1 | 1 | - | 166.25 | - | 4,331 | - | 0.000352 | 🔵 low — common in general English | — |
| 4699 | **reprimanded** | 1 | 1 | - | 166.25 | - | 4,332 | - | 0.000352 | 🔵 low — common in general English | — |
| 4700 | **calmed** | 1 | 1 | - | 166.25 | - | 4,333 | - | 0.000352 | 🔵 low — common in general English | — |
| 4701 | **crowned** | 1 | 1 | - | 166.25 | - | 4,334 | - | 0.000352 | 🔵 low — common in general English | — |
| 4702 | **commonplace** | 1 | 1 | - | 166.25 | - | 4,335 | - | 0.000352 | 🔵 low — common in general English | — |
| 4703 | **distinct** | 1 | 1 | - | 166.25 | - | 4,336 | - | 0.000352 | 🔵 low — common in general English | — |
| 4704 | **nightmare** | 1 | 1 | - | 166.25 | - | 4,337 | - | 0.000352 | 🔵 low — common in general English | — |
| 4705 | **ransom** | 1 | 1 | - | 166.25 | - | 4,338 | - | 0.000352 | 🔵 low — common in general English | — |
| 4706 | **cognizant** | 1 | 1 | - | 166.25 | - | 4,339 | - | 0.000352 | 🔵 low — common in general English | — |
| 4707 | **unquestionably** | 1 | 1 | - | 166.25 | - | 4,340 | - | 0.000352 | 🔵 low — common in general English | — |
| 4708 | **sym** | 1 | 1 | - | 166.25 | - | 4,341 | - | 0.000352 | 🔵 low — common in general English | — |
| 4709 | **intensely** | 1 | 1 | - | 166.25 | - | 4,342 | - | 0.000352 | 🔵 low — common in general English | — |
| 4710 | **straightforward** | 1 | 1 | - | 166.25 | - | 4,343 | - | 0.000352 | 🔵 low — common in general English | — |
| 4711 | **watchdog** | 1 | 1 | - | 166.25 | - | 4,344 | - | 0.000351 | 🔵 low — common in general English | — |
| 4712 | **imprisoned** | 1 | 1 | - | 166.25 | - | 4,345 | - | 0.000351 | 🔵 low — common in general English | — |
| 4713 | **punishment** | 1 | 1 | - | 166.25 | - | 4,346 | - | 0.000351 | 🔵 low — common in general English | — |
| 4714 | **invading** | 1 | 1 | - | 166.25 | - | 4,347 | - | 0.000351 | 🔵 low — common in general English | — |
| 4715 | **inflict** | 1 | 1 | - | 166.25 | - | 4,348 | - | 0.000351 | 🔵 low — common in general English | — |
| 4716 | **afflicted** | 1 | 1 | - | 166.25 | - | 4,349 | - | 0.000351 | 🔵 low — common in general English | — |
| 4717 | **rider** | 1 | 1 | - | 166.25 | - | 4,350 | - | 0.000351 | 🔵 low — common in general English | — |
| 4718 | **intimidation** | 1 | 1 | - | 166.25 | - | 4,351 | - | 0.000351 | 🔵 low — common in general English | — |
| 4719 | **contravention** | 1 | 1 | - | 166.25 | - | 4,352 | - | 0.000351 | 🔵 low — common in general English | — |
| 4720 | **predator** | 1 | 1 | - | 166.25 | - | 4,353 | - | 0.000351 | 🔵 low — common in general English | — |
| 4721 | **outraged** | 1 | 1 | - | 166.25 | - | 4,354 | - | 0.000351 | 🔵 low — common in general English | — |
| 4722 | **shedding** | 1 | 1 | - | 166.25 | - | 4,355 | - | 0.000351 | 🔵 low — common in general English | — |
| 4723 | **tolerance** | 1 | 1 | - | 166.25 | - | 4,356 | - | 0.000351 | 🔵 low — common in general English | — |
| 4724 | **tenderness** | 1 | 1 | - | 166.25 | - | 4,357 | - | 0.000351 | 🔵 low — common in general English | — |
| 4725 | **flourish** | 1 | 1 | - | 166.25 | - | 4,358 | - | 0.000351 | 🔵 low — common in general English | — |
| 4726 | **lasted** | 1 | 1 | - | 166.25 | - | 4,359 | - | 0.000351 | 🔵 low — common in general English | — |
| 4727 | **dissuade** | 1 | 1 | - | 166.25 | - | 4,360 | - | 0.000351 | 🔵 low — common in general English | — |
| 4728 | **jugular** | 1 | 1 | - | 166.25 | - | 4,361 | - | 0.000351 | 🔵 low — common in general English | — |
| 4729 | **mini** | 1 | 1 | - | 166.25 | - | 4,362 | - | 0.000351 | 🔵 low — common in general English | — |
| 4730 | **greed** | 1 | 1 | - | 166.25 | - | 4,363 | - | 0.000350 | 🔵 low — common in general English | — |
| 4731 | **flee** | 1 | 1 | - | 166.25 | - | 4,364 | - | 0.000350 | 🔵 low — common in general English | — |
| 4732 | **vicinity** | 1 | 1 | - | 166.25 | - | 4,365 | - | 0.000350 | 🔵 low — common in general English | — |
| 4733 | **overwhelmed** | 1 | 1 | - | 166.25 | - | 4,366 | - | 0.000350 | 🔵 low — common in general English | — |
| 4734 | **reappeared** | 1 | 1 | - | 166.25 | - | 4,367 | - | 0.000350 | 🔵 low — common in general English | — |
| 4735 | **boasting** | 1 | 1 | - | 166.25 | - | 4,368 | - | 0.000350 | 🔵 low — common in general English | — |
| 4736 | **sucked** | 1 | 1 | - | 166.25 | - | 4,369 | - | 0.000350 | 🔵 low — common in general English | — |
| 4737 | **futility** | 1 | 1 | - | 166.25 | - | 4,370 | - | 0.000350 | 🔵 low — common in general English | — |
| 4738 | **wealthier** | 1 | 1 | - | 166.25 | - | 4,371 | - | 0.000350 | 🔵 low — common in general English | — |
| 4739 | **dwindle** | 1 | 1 | - | 166.25 | - | 4,372 | - | 0.000350 | 🔵 low — common in general English | — |
| 4740 | **fare** | 1 | 1 | - | 166.25 | - | 4,373 | - | 0.000350 | 🔵 low — common in general English | — |
| 4741 | **aberration** | 1 | 1 | - | 166.25 | - | 4,374 | - | 0.000350 | 🔵 low — common in general English | — |
| 4742 | **mirage** | 1 | 1 | - | 166.25 | - | 4,375 | - | 0.000350 | 🔵 low — common in general English | — |
| 4743 | **omitting** | 1 | 1 | - | 166.25 | - | 4,376 | - | 0.000350 | 🔵 low — common in general English | — |
| 4744 | **summarized** | 1 | 1 | - | 166.25 | - | 4,377 | - | 0.000350 | 🔵 low — common in general English | — |
| 4745 | **thirty-five** | 1 | 1 | - | 166.25 | - | 4,378 | - | 0.000350 | 🔵 low — common in general English | — |
| 4746 | **instantly** | 1 | 1 | - | 166.25 | - | 4,379 | - | 0.000350 | 🔵 low — common in general English | — |
| 4747 | **colossal** | 1 | 1 | - | 166.25 | - | 4,380 | - | 0.000350 | 🔵 low — common in general English | — |
| 4748 | **transparent** | 1 | 1 | - | 166.25 | - | 4,381 | - | 0.000350 | 🔵 low — common in general English | — |
| 4749 | **simplicity** | 1 | 1 | - | 166.25 | - | 4,382 | - | 0.000350 | 🔵 low — common in general English | — |
| 4750 | **chatting** | 1 | 1 | - | 166.25 | - | 4,383 | - | 0.000349 | 🔵 low — common in general English | — |
| 4751 | **smoking** | 1 | 1 | - | 166.25 | - | 4,384 | - | 0.000349 | 🔵 low — common in general English | — |
| 4752 | **lowland** | 1 | 1 | - | 166.25 | - | 4,385 | - | 0.000349 | 🔵 low — common in general English | — |
| 4753 | **abusing** | 1 | 1 | - | 166.25 | - | 4,386 | - | 0.000349 | 🔵 low — common in general English | — |
| 4754 | **subtle** | 1 | 1 | - | 166.25 | - | 4,387 | - | 0.000349 | 🔵 low — common in general English | — |
| 4755 | **occasional** | 1 | 1 | - | 166.25 | - | 4,388 | - | 0.000349 | 🔵 low — common in general English | — |
| 4756 | **infested** | 1 | 1 | - | 166.25 | - | 4,389 | - | 0.000349 | 🔵 low — common in general English | — |
| 4757 | **diseased** | 1 | 1 | - | 166.25 | - | 4,390 | - | 0.000349 | 🔵 low — common in general English | — |
| 4758 | **smashing** | 1 | 1 | - | 166.25 | - | 4,391 | - | 0.000349 | 🔵 low — common in general English | — |
| 4759 | **adult** | 1 | 1 | - | 166.25 | - | 4,392 | - | 0.000349 | 🔵 low — common in general English | — |
| 4760 | **ration** | 1 | 1 | - | 166.25 | - | 4,393 | - | 0.000349 | 🔵 low — common in general English | — |
| 4761 | **coral** | 1 | 1 | - | 166.25 | - | 4,394 | - | 0.000349 | 🔵 low — common in general English | — |
| 4762 | **ordinarily** | 1 | 1 | - | 166.25 | - | 4,395 | - | 0.000349 | 🔵 low — common in general English | — |
| 4763 | **ready-made** | 1 | 1 | - | 166.25 | - | 4,396 | - | 0.000349 | 🔵 low — common in general English | — |
| 4764 | **subcontinent** | 1 | 1 | - | 166.25 | - | 4,397 | - | 0.000349 | 🔵 low — common in general English | — |
| 4765 | **bountiful** | 1 | 1 | - | 166.25 | - | 4,398 | - | 0.000349 | 🔵 low — common in general English | — |
| 4766 | **commentary** | 1 | 1 | - | 166.25 | - | 4,399 | - | 0.000349 | 🔵 low — common in general English | — |
| 4767 | **impossibility** | 1 | 1 | - | 166.25 | - | 4,400 | - | 0.000349 | 🔵 low — common in general English | — |
| 4768 | **amazed** | 1 | 1 | - | 166.25 | - | 4,401 | - | 0.000349 | 🔵 low — common in general English | — |
| 4769 | **amazing** | 1 | 1 | - | 166.25 | - | 4,402 | - | 0.000349 | 🔵 low — common in general English | — |
| 4770 | **resigning** | 1 | 1 | - | 166.25 | - | 4,403 | - | 0.000348 | 🔵 low — common in general English | — |
| 4771 | **dispelled** | 1 | 1 | - | 166.25 | - | 4,404 | - | 0.000348 | 🔵 low — common in general English | — |
| 4772 | **foodstuff** | 1 | 1 | - | 166.25 | - | 4,405 | - | 0.000348 | 🔵 low — common in general English | — |
| 4773 | **rendered** | 1 | 1 | - | 166.25 | - | 4,406 | - | 0.000348 | 🔵 low — common in general English | — |
| 4774 | **placated** | 1 | 1 | - | 166.25 | - | 4,407 | - | 0.000348 | 🔵 low — common in general English | — |
| 4775 | **subduing** | 1 | 1 | - | 166.25 | - | 4,408 | - | 0.000348 | 🔵 low — common in general English | — |
| 4776 | **scrape** | 1 | 1 | - | 166.25 | - | 4,409 | - | 0.000348 | 🔵 low — common in general English | — |
| 4777 | **severity** | 1 | 1 | - | 166.25 | - | 4,410 | - | 0.000348 | 🔵 low — common in general English | — |
| 4778 | **intel** | 1 | 1 | - | 166.25 | - | 4,411 | - | 0.000348 | 🔵 low — common in general English | — |
| 4779 | **exile** | 1 | 1 | - | 166.25 | - | 4,412 | - | 0.000348 | 🔵 low — common in general English | — |
| 4780 | **infinitesimal** | 1 | 1 | - | 166.25 | - | 4,413 | - | 0.000348 | 🔵 low — common in general English | — |
| 4781 | **bloom** | 1 | 1 | - | 166.25 | - | 4,414 | - | 0.000348 | 🔵 low — common in general English | — |
| 4782 | **supposedly** | 1 | 1 | - | 166.25 | - | 4,415 | - | 0.000348 | 🔵 low — common in general English | — |
| 4783 | **knowingly** | 1 | 1 | - | 166.25 | - | 4,416 | - | 0.000348 | 🔵 low — common in general English | — |
| 4784 | **demonstration** | 1 | 1 | - | 166.25 | - | 4,417 | - | 0.000348 | 🔵 low — common in general English | — |
| 4785 | **cleansing** | 1 | 1 | - | 166.25 | - | 4,418 | - | 0.000348 | 🔵 low — common in general English | — |
| 4786 | **spilt** | 1 | 1 | - | 166.25 | - | 4,419 | - | 0.000348 | 🔵 low — common in general English | — |
| 4787 | **reassured** | 1 | 1 | - | 166.25 | - | 4,420 | - | 0.000348 | 🔵 low — common in general English | — |
| 4788 | **predominate** | 1 | 1 | - | 166.25 | - | 4,421 | - | 0.000348 | 🔵 low — common in general English | — |
| 4789 | **quelling** | 1 | 1 | - | 166.25 | - | 4,422 | - | 0.000348 | 🔵 low — common in general English | — |
| 4790 | **misconception** | 1 | 1 | - | 166.25 | - | 4,423 | - | 0.000347 | 🔵 low — common in general English | — |
| 4791 | **propagated** | 1 | 1 | - | 166.25 | - | 4,424 | - | 0.000347 | 🔵 low — common in general English | — |
| 4792 | **bore** | 1 | 1 | - | 166.25 | - | 4,425 | - | 0.000347 | 🔵 low — common in general English | — |
| 4793 | **negligence** | 1 | 1 | - | 166.25 | - | 4,426 | - | 0.000347 | 🔵 low — common in general English | — |
| 4794 | **astonished** | 1 | 1 | - | 166.25 | - | 4,427 | - | 0.000347 | 🔵 low — common in general English | — |
| 4795 | **proceeded** | 1 | 1 | - | 166.25 | - | 4,428 | - | 0.000347 | 🔵 low — common in general English | — |
| 4796 | **vanished** | 1 | 1 | - | 166.25 | - | 4,429 | - | 0.000347 | 🔵 low — common in general English | — |
| 4797 | **uncontrolled** | 1 | 1 | - | 166.25 | - | 4,430 | - | 0.000347 | 🔵 low — common in general English | — |
| 4798 | **equality** | 1 | 1 | - | 166.25 | - | 4,431 | - | 0.000347 | 🔵 low — common in general English | ✓ མཉམ་པ་ཉིད |
| 4799 | **fabrication** | 1 | 1 | - | 166.25 | - | 4,432 | - | 0.000347 | 🔵 low — common in general English | — |
| 4800 | **translating** | 1 | 1 | - | 166.25 | - | 4,433 | - | 0.000347 | 🔵 low — common in general English | — |
| 4801 | **traced** | 1 | 1 | - | 166.25 | - | 4,434 | - | 0.000347 | 🔵 low — common in general English | — |
| 4802 | **obstinate** | 1 | 1 | - | 166.25 | - | 4,435 | - | 0.000347 | 🔵 low — common in general English | — |
| 4803 | **unfabricated** | 1 | 1 | - | 166.25 | - | 4,436 | - | 0.000347 | 🔵 low — common in general English | — |
| 4804 | **accustomed** | 1 | 1 | - | 166.25 | - | 4,437 | - | 0.000347 | 🔵 low — common in general English | — |
| 4805 | **impediment** | 1 | 1 | - | 166.25 | - | 4,438 | - | 0.000347 | 🔵 low — common in general English | — |
| 4806 | **forcefully** | 1 | 1 | - | 166.25 | - | 4,439 | - | 0.000347 | 🔵 low — common in general English | — |
| 4807 | **brush** | 1 | 1 | - | 166.25 | - | 4,440 | - | 0.000347 | 🔵 low — common in general English | — |
| 4808 | **prematurely** | 1 | 1 | - | 166.25 | - | 4,441 | - | 0.000347 | 🔵 low — common in general English | — |
| 4809 | **skylight** | 1 | 1 | - | 166.25 | - | 4,442 | - | 0.000347 | 🔵 low — common in general English | — |
| 4810 | **inserting** | 1 | 1 | - | 166.25 | - | 4,443 | - | 0.000346 | 🔵 low — common in general English | — |
| 4811 | **winnowed** | 1 | 1 | - | 166.25 | - | 4,444 | - | 0.000346 | 🔵 low — common in general English | — |
| 4812 | **irrigate** | 1 | 1 | - | 166.25 | - | 4,445 | - | 0.000346 | 🔵 low — common in general English | — |
| 4813 | **fertile** | 1 | 1 | - | 166.25 | - | 4,446 | - | 0.000346 | 🔵 low — common in general English | — |
| 4814 | **invented** | 1 | 1 | - | 166.25 | - | 4,447 | - | 0.000346 | 🔵 low — common in general English | — |
| 4815 | **vine** | 1 | 1 | - | 166.25 | - | 4,448 | - | 0.000346 | 🔵 low — common in general English | — |
| 4816 | **azure** | 1 | 1 | - | 166.25 | - | 4,449 | - | 0.000346 | 🔵 low — common in general English | — |
| 4817 | **beamed** | 1 | 1 | - | 166.19 | - | 4,450 | - | 0.000346 | 🔵 low — common in general English | — |
| 4818 | **elucidated** | 1 | 1 | - | 166.19 | - | 4,451 | - | 0.000346 | 🔵 low — common in general English | — |
| 4819 | **wonderfully** | 1 | 1 | - | 166.19 | - | 4,452 | - | 0.000346 | 🔵 low — common in general English | — |
| 4820 | **concerns-such** | 1 | 1 | - | 166.19 | - | 4,453 | - | 0.000346 | 🔵 low — common in general English | — |
| 4821 | **whatever-i** | 1 | 1 | - | 166.19 | - | 4,454 | - | 0.000346 | 🔵 low — common in general English | — |
| 4822 | **circumambulation** | 1 | 1 | - | 166.19 | - | 4,455 | - | 0.000346 | 🔵 low — common in general English | ✓ སྐོར་བ |
| 4823 | **mantra-even** | 1 | 1 | - | 166.19 | - | 4,456 | - | 0.000346 | 🔵 low — common in general English | — |
| 4824 | **mani-it** | 1 | 1 | - | 166.19 | - | 4,457 | - | 0.000346 | 🔵 low — common in general English | — |
| 4825 | **torch** | 1 | 1 | - | 166.19 | - | 4,458 | - | 0.000346 | 🔵 low — common in general English | — |
| 4826 | **akani** | 1 | 1 | - | 166.19 | - | 4,459 | - | 0.000346 | 🔵 low — common in general English | — |
| 4827 | **tha** | 1 | 1 | - | 166.19 | - | 4,460 | - | 0.000346 | 🔵 low — common in general English | — |
| 4828 | **unexcelled** | 1 | 1 | - | 166.19 | - | 4,461 | - | 0.000346 | 🔵 low — common in general English | — |
| 4829 | **lotus-light** | 1 | 1 | - | 166.19 | - | 4,462 | - | 0.000346 | 🔵 low — common in general English | — |
| 4830 | **divinity** | 1 | 1 | - | 166.19 | - | 4,463 | - | 0.000345 | 🔵 low — common in general English | — |
| 4831 | **ever-revolving** | 1 | 1 | - | 166.19 | - | 4,464 | - | 0.000345 | 🔵 low — common in general English | — |
| 4832 | **buddha-nature** | 1 | 1 | - | 166.19 | - | 4,465 | - | 0.000345 | 🔵 low — common in general English | — |
| 4833 | **adventitious** | 1 | 1 | - | 166.19 | - | 4,466 | - | 0.000345 | 🔵 low — common in general English | — |
| 4834 | **entranced** | 1 | 1 | - | 166.19 | - | 4,467 | - | 0.000345 | 🔵 low — common in general English | — |
| 4835 | **tice** | 1 | 1 | - | 166.19 | - | 4,468 | - | 0.000345 | 🔵 low — common in general English | — |
| 4836 | **teaching-which** | 1 | 1 | - | 166.19 | - | 4,469 | - | 0.000345 | 🔵 low — common in general English | — |
| 4837 | **reasoning** | 1 | 1 | - | 166.19 | - | 4,470 | - | 0.000345 | 🔵 low — common in general English | — |
| 4838 | **proudly** | 1 | 1 | - | 166.19 | - | 4,471 | - | 0.000345 | 🔵 low — common in general English | — |
| 4839 | **minutely** | 1 | 1 | - | 166.19 | - | 4,472 | - | 0.000345 | 🔵 low — common in general English | — |
| 4840 | **leapt** | 1 | 1 | - | 166.19 | - | 4,473 | - | 0.000345 | 🔵 low — common in general English | — |
| 4841 | **moth** | 1 | 1 | - | 166.19 | - | 4,474 | - | 0.000345 | 🔵 low — common in general English | — |
| 4842 | **lamp-flame** | 1 | 1 | - | 166.19 | - | 4,475 | - | 0.000345 | 🔵 low — common in general English | — |
| 4843 | **carnivorous** | 1 | 1 | - | 166.19 | - | 4,476 | - | 0.000345 | 🔵 low — common in general English | — |
| 4844 | **seduced** | 1 | 1 | - | 166.19 | - | 4,477 | - | 0.000345 | 🔵 low — common in general English | — |
| 4845 | **bait** | 1 | 1 | - | 166.19 | - | 4,478 | - | 0.000345 | 🔵 low — common in general English | — |
| 4846 | **gyalse** | 1 | 1 | - | 166.19 | - | 4,479 | - | 0.000345 | 🔵 low — common in general English | ~ |
| 4847 | **mru** | 1 | 1 | - | 166.19 | - | 4,480 | - | 0.000345 | 🔵 low — common in general English | — |
| 4848 | **riverbed** | 1 | 1 | - | 166.19 | - | 4,481 | - | 0.000345 | 🔵 low — common in general English | — |
| 4849 | **indispensable-remembering** | 1 | 1 | - | 166.19 | - | 4,482 | - | 0.000345 | 🔵 low — common in general English | — |
| 4850 | **rat** | 1 | 1 | - | 166.19 | - | 4,483 | - | 0.000345 | 🔵 low — common in general English | — |
| 4851 | **dremo** | 1 | 1 | - | 166.19 | - | 4,484 | - | 0.000344 | 🔵 low — common in general English | — |
| 4852 | **marmot** | 1 | 1 | - | 166.19 | - | 4,485 | - | 0.000344 | 🔵 low — common in general English | — |
| 4853 | **sleepy** | 1 | 1 | - | 166.19 | - | 4,486 | - | 0.000344 | 🔵 low — common in general English | — |
| 4854 | **weren** | 1 | 1 | - | 166.19 | - | 4,487 | - | 0.000344 | 🔵 low — common in general English | — |
| 4855 | **string** | 1 | 1 | - | 166.19 | - | 4,488 | - | 0.000344 | 🔵 low — common in general English | — |
| 4856 | **loosely** | 1 | 1 | - | 166.19 | - | 4,489 | - | 0.000344 | 🔵 low — common in general English | — |
| 4857 | **elegant** | 1 | 1 | - | 166.19 | - | 4,490 | - | 0.000344 | 🔵 low — common in general English | — |
| 4858 | **meaning-you** | 1 | 1 | - | 166.19 | - | 4,491 | - | 0.000344 | 🔵 low — common in general English | — |
| 4859 | **debase** | 1 | 1 | - | 166.19 | - | 4,492 | - | 0.000344 | 🔵 low — common in general English | — |
| 4860 | **everything-the** | 1 | 1 | - | 166.19 | - | 4,493 | - | 0.000344 | 🔵 low — common in general English | — |
| 4861 | **teachings-properly** | 1 | 1 | - | 166.19 | - | 4,494 | - | 0.000344 | 🔵 low — common in general English | — |
| 4862 | **disheart** | 1 | 1 | - | 166.19 | - | 4,495 | - | 0.000344 | 🔵 low — common in general English | — |
| 4863 | **ened** | 1 | 1 | - | 166.19 | - | 4,496 | - | 0.000344 | 🔵 low — common in general English | — |
| 4864 | **elementary** | 1 | 1 | - | 166.19 | - | 4,497 | - | 0.000344 | 🔵 low — common in general English | — |
| 4865 | **prescribe** | 1 | 1 | - | 166.19 | - | 4,498 | - | 0.000344 | 🔵 low — common in general English | — |
| 4866 | **dharma-that** | 1 | 1 | - | 166.19 | - | 4,499 | - | 0.000344 | 🔵 low — common in general English | — |
| 4867 | **practice-i** | 1 | 1 | - | 166.19 | - | 4,500 | - | 0.000344 | 🔵 low — common in general English | — |
| 4868 | **death-bed** | 1 | 1 | - | 166.19 | - | 4,501 | - | 0.000344 | 🔵 low — common in general English | — |
| 4869 | **helplessly** | 1 | 1 | - | 166.19 | - | 4,502 | - | 0.000344 | 🔵 low — common in general English | — |
| 4870 | **perilous** | 1 | 1 | - | 166.19 | - | 4,503 | - | 0.000344 | 🔵 low — common in general English | — |
| 4871 | **libera** | 1 | 1 | - | 166.19 | - | 4,504 | - | 0.000343 | 🔵 low — common in general English | — |
| 4872 | **shallow-tongued** | 1 | 1 | - | 166.19 | - | 4,505 | - | 0.000343 | 🔵 low — common in general English | — |
| 4873 | **sneer** | 1 | 1 | - | 166.19 | - | 4,506 | - | 0.000343 | 🔵 low — common in general English | — |
| 4874 | **mal** | 1 | 1 | - | 166.19 | - | 4,507 | - | 0.000343 | 🔵 low — common in general English | — |
| 4875 | **joyfully** | 1 | 1 | - | 166.19 | - | 4,508 | - | 0.000343 | 🔵 low — common in general English | — |
| 4876 | **swathed** | 1 | 1 | - | 166.19 | - | 4,509 | - | 0.000343 | 🔵 low — common in general English | — |
| 4877 | **turban** | 1 | 1 | - | 166.19 | - | 4,510 | - | 0.000343 | 🔵 low — common in general English | — |
| 4878 | **ataka** | 1 | 1 | - | 166.19 | - | 4,511 | - | 0.000343 | 🔵 low — common in general English | — |
| 4879 | **dignified** | 1 | 1 | - | 166.19 | - | 4,512 | - | 0.000343 | 🔵 low — common in general English | — |
| 4880 | **oppor** | 1 | 1 | - | 166.19 | - | 4,513 | - | 0.000343 | 🔵 low — common in general English | — |
| 4881 | **tunity** | 1 | 1 | - | 166.19 | - | 4,514 | - | 0.000343 | 🔵 low — common in general English | — |
| 4882 | **khatha** | 1 | 1 | - | 166.19 | - | 4,515 | - | 0.000343 | 🔵 low — common in general English | — |
| 4883 | **outlying** | 1 | 1 | - | 166.19 | - | 4,516 | - | 0.000343 | 🔵 low — common in general English | — |
| 4884 | **attune** | 1 | 1 | - | 166.19 | - | 4,517 | - | 0.000343 | 🔵 low — common in general English | — |
| 4885 | **forefather** | 1 | 1 | - | 166.19 | - | 4,518 | - | 0.000343 | 🔵 low — common in general English | — |
| 4886 | **aspiring** | 1 | 1 | - | 166.19 | - | 4,519 | - | 0.000343 | 🔵 low — common in general English | — |
| 4887 | **liyana** | 1 | 1 | - | 166.19 | - | 4,520 | - | 0.000343 | 🔵 low — common in general English | — |
| 4888 | **atten** | 1 | 1 | - | 166.19 | - | 4,521 | - | 0.000343 | 🔵 low — common in general English | — |
| 4889 | **dant** | 1 | 1 | - | 166.19 | - | 4,522 | - | 0.000343 | 🔵 low — common in general English | — |
| 4890 | **oll** | 1 | 1 | - | 166.19 | - | 4,523 | - | 0.000343 | 🔵 low — common in general English | — |
| 4891 | **dysfunction** | 1 | 1 | - | 166.19 | - | 4,524 | - | 0.000343 | 🔵 low — common in general English | — |
| 4892 | **unheard** | 1 | 1 | - | 166.19 | - | 4,525 | - | 0.000342 | 🔵 low — common in general English | — |
| 4893 | **animal-even** | 1 | 1 | - | 166.19 | - | 4,526 | - | 0.000342 | 🔵 low — common in general English | — |
| 4894 | **prized** | 1 | 1 | - | 166.19 | - | 4,527 | - | 0.000342 | 🔵 low — common in general English | — |
| 4895 | **padme** | 1 | 1 | - | 166.19 | - | 4,528 | - | 0.000342 | 🔵 low — common in general English | — |
| 4896 | **heap-wherea** | 1 | 1 | - | 166.19 | - | 4,529 | - | 0.000342 | 🔵 low — common in general English | — |
| 4897 | **conceive** | 1 | 1 | - | 166.19 | - | 4,530 | - | 0.000342 | 🔵 low — common in general English | — |
| 4898 | **pratimoksa** | 1 | 1 | - | 166.19 | - | 4,531 | - | 0.000342 | 🔵 low — common in general English | — |
| 4899 | **dharma-the** | 1 | 1 | - | 166.19 | - | 4,532 | - | 0.000342 | 🔵 low — common in general English | — |
| 4900 | **buddha-exist** | 1 | 1 | - | 166.19 | - | 4,533 | - | 0.000342 | 🔵 low — common in general English | — |
| 4901 | **sparsely** | 1 | 1 | - | 166.19 | - | 4,534 | - | 0.000342 | 🔵 low — common in general English | — |
| 4902 | **whjch** | 1 | 1 | - | 166.19 | - | 4,535 | - | 0.000342 | 🔵 low — common in general English | — |
| 4903 | **script** | 1 | 1 | - | 166.19 | - | 4,536 | - | 0.000342 | 🔵 low — common in general English | — |
| 4904 | **intro** | 1 | 1 | - | 166.19 | - | 4,537 | - | 0.000342 | 🔵 low — common in general English | — |
| 4905 | **duced** | 1 | 1 | - | 166.19 | - | 4,538 | - | 0.000342 | 🔵 low — common in general English | — |
| 4906 | **mikyo** | 1 | 1 | - | 166.19 | - | 4,539 | - | 0.000342 | 🔵 low — common in general English | — |
| 4907 | **rasa** | 1 | 1 | - | 166.19 | - | 4,540 | - | 0.000342 | 🔵 low — common in general English | — |
| 4908 | **trulnang** | 1 | 1 | - | 166.19 | - | 4,541 | - | 0.000342 | 🔵 low — common in general English | — |
| 4909 | **estab** | 1 | 1 | - | 166.19 | - | 4,542 | - | 0.000342 | 🔵 low — common in general English | — |
| 4910 | **lished** | 1 | 1 | - | 166.19 | - | 4,543 | - | 0.000342 | 🔵 low — common in general English | — |
| 4911 | **kingtrisong** | 1 | 1 | - | 166.19 | - | 4,544 | - | 0.000342 | 🔵 low — common in general English | — |
| 4912 | **mantra-holder** | 1 | 1 | - | 166.19 | - | 4,545 | - | 0.000342 | 🔵 low — common in general English | — |
| 4913 | **sustra** | 1 | 1 | - | 166.19 | - | 4,546 | - | 0.000342 | 🔵 low — common in general English | — |
| 4914 | **dharma-for** | 1 | 1 | - | 166.19 | - | 4,547 | - | 0.000341 | 🔵 low — common in general English | — |
| 4915 | **queror** | 1 | 1 | - | 166.19 | - | 4,548 | - | 0.000341 | 🔵 low — common in general English | — |
| 4916 | **preached** | 1 | 1 | - | 166.19 | - | 4,549 | - | 0.000341 | 🔵 low — common in general English | — |
| 4917 | **extant** | 1 | 1 | - | 166.19 | - | 4,550 | - | 0.000341 | 🔵 low — common in general English | — |
| 4918 | **ahhough** | 1 | 1 | - | 166.19 | - | 4,551 | - | 0.000341 | 🔵 low — common in general English | — |
| 4919 | **destroyer-of-samsara** | 1 | 1 | - | 166.19 | - | 4,552 | - | 0.000341 | 🔵 low — common in general English | ✓ འཁོར་བ་འཇིག |
| 4920 | **incalculably** | 1 | 1 | - | 166.19 | - | 4,553 | - | 0.000341 | 🔵 low — common in general English | — |
| 4921 | **infinite-aspiration** | 1 | 1 | - | 166.19 | - | 4,554 | - | 0.000341 | 🔵 low — common in general English | — |
| 4922 | **alternation** | 1 | 1 | - | 166.19 | - | 4,555 | - | 0.000341 | 🔵 low — common in general English | — |
| 4923 | **promulgated** | 1 | 1 | - | 166.19 | - | 4,556 | - | 0.000341 | 🔵 low — common in general English | — |
| 4924 | **once-come-king** | 1 | 1 | - | 166.19 | - | 4,557 | - | 0.000341 | 🔵 low — common in general English | ✓ སྔོན་བྱུང་གི་རྒྱལ་པོ |
| 4925 | **trayana** | 1 | 1 | - | 166.19 | - | 4,558 | - | 0.000341 | 🔵 low — common in general English | — |
| 4926 | **uncompounded** | 1 | 1 | - | 166.19 | - | 4,559 | - | 0.000341 | 🔵 low — common in general English | — |
| 4927 | **interpreter** | 1 | 1 | - | 166.19 | - | 4,560 | - | 0.000341 | 🔵 low — common in general English | — |
| 4928 | **kham** | 1 | 1 | - | 166.19 | - | 4,561 | - | 0.000341 | 🔵 low — common in general English | — |
| 4929 | **degenerations-those** | 1 | 1 | - | 166.19 | - | 4,562 | - | 0.000341 | 🔵 low — common in general English | — |
| 4930 | **it-just** | 1 | 1 | - | 166.19 | - | 4,563 | - | 0.000341 | 🔵 low — common in general English | — |
| 4931 | **transmi** | 1 | 1 | - | 166.19 | - | 4,564 | - | 0.000341 | 🔵 low — common in general English | — |
| 4932 | **infiltrate** | 1 | 1 | - | 166.19 | - | 4,565 | - | 0.000341 | 🔵 low — common in general English | — |
| 4933 | **important-the** | 1 | 1 | - | 166.19 | - | 4,567 | - | 0.000341 | 🔵 low — common in general English | — |
| 4934 | **canonical** | 1 | 1 | - | 166.19 | - | 4,568 | - | 0.000340 | 🔵 low — common in general English | — |
| 4935 | **commentar** | 1 | 1 | - | 166.19 | - | 4,569 | - | 0.000340 | 🔵 low — common in general English | — |
| 4936 | **ies** | 1 | 1 | - | 166.19 | - | 4,570 | - | 0.000340 | 🔵 low — common in general English | — |
| 4937 | **practice-even** | 1 | 1 | - | 166.19 | - | 4,571 | - | 0.000340 | 🔵 low — common in general English | — |
| 4938 | **triptaka** | 1 | 1 | - | 166.19 | - | 4,572 | - | 0.000340 | 🔵 low — common in general English | — |
| 4939 | **metaphysic** | 1 | 1 | - | 166.19 | - | 4,573 | - | 0.000340 | 🔵 low — common in general English | — |
| 4940 | **piety** | 1 | 1 | - | 166.19 | - | 4,574 | - | 0.000340 | 🔵 low — common in general English | — |
| 4941 | **illustrate** | 1 | 1 | - | 166.19 | - | 4,575 | - | 0.000340 | 🔵 low — common in general English | — |
| 4942 | **condi** | 1 | 1 | - | 166.19 | - | 4,576 | - | 0.000340 | 🔵 low — common in general English | — |
| 4943 | **endowed** | 1 | 1 | - | 166.19 | - | 4,577 | - | 0.000340 | 🔵 low — common in general English | — |
| 4944 | **enslavement** | 1 | 1 | - | 166.19 | - | 4,578 | - | 0.000340 | 🔵 low — common in general English | — |
| 4945 | **hypocritical** | 1 | 1 | - | 166.19 | - | 4,579 | - | 0.000340 | 🔵 low — common in general English | — |
| 4946 | **intrusive** | 1 | 1 | - | 166.19 | - | 4,580 | - | 0.000340 | 🔵 low — common in general English | — |
| 4947 | **depravity** | 1 | 1 | - | 166.19 | - | 4,581 | - | 0.000340 | 🔵 low — common in general English | — |
| 4948 | **heedlessness** | 1 | 1 | - | 166.19 | - | 4,582 | - | 0.000340 | 🔵 low — common in general English | — |
| 4949 | **poisons-that** | 1 | 1 | - | 166.19 | - | 4,583 | - | 0.000340 | 🔵 low — common in general English | — |
| 4950 | **dominat** | 1 | 1 | - | 166.19 | - | 4,584 | - | 0.000340 | 🔵 low — common in general English | — |
| 4951 | **plishing** | 1 | 1 | - | 166.19 | - | 4,585 | - | 0.000340 | 🔵 low — common in general English | — |
| 4952 | **perverted** | 1 | 1 | - | 166.19 | - | 4,586 | - | 0.000340 | 🔵 low — common in general English | — |
| 4953 | **lazy** | 1 | 1 | - | 166.19 | - | 4,587 | - | 0.000340 | 🔵 low — common in general English | — |
| 4954 | **indolence** | 1 | 1 | - | 166.19 | - | 4,588 | - | 0.000340 | 🔵 low — common in general English | — |
| 4955 | **life-that** | 1 | 1 | - | 166.19 | - | 4,589 | - | 0.000339 | 🔵 low — common in general English | — |
| 4956 | **impostor** | 1 | 1 | - | 166.19 | - | 4,590 | - | 0.000339 | 🔵 low — common in general English | — |
| 4957 | **pretence** | 1 | 1 | - | 166.19 | - | 4,591 | - | 0.000339 | 🔵 low — common in general English | — |
| 4958 | **humanity** | 1 | 1 | - | 166.19 | - | 4,592 | - | 0.000339 | 🔵 low — common in general English | — |
| 4959 | **depraved** | 1 | 1 | - | 166.19 | - | 4,593 | - | 0.000339 | 🔵 low — common in general English | — |
| 4960 | **suffedng** | 1 | 1 | - | 166.19 | - | 4,594 | - | 0.000339 | 🔵 low — common in general English | — |
| 4961 | **sarilsa** | 1 | 1 | - | 166.19 | - | 4,595 | - | 0.000339 | 🔵 low — common in general English | — |
| 4962 | **plishment** | 1 | 1 | - | 166.19 | - | 4,596 | - | 0.000339 | 🔵 low — common in general English | — |
| 4963 | **snuff** | 1 | 1 | - | 166.19 | - | 4,597 | - | 0.000339 | 🔵 low — common in general English | — |
| 4964 | **chieftain** | 1 | 1 | - | 166.19 | - | 4,598 | - | 0.000339 | 🔵 low — common in general English | — |
| 4965 | **worth-each** | 1 | 1 | - | 166.19 | - | 4,599 | - | 0.000339 | 🔵 low — common in general English | — |
| 4966 | **thirty-four** | 1 | 1 | - | 166.19 | - | 4,600 | - | 0.000339 | 🔵 low — common in general English | — |
| 4967 | **squander** | 1 | 1 | - | 166.19 | - | 4,601 | - | 0.000339 | 🔵 low — common in general English | — |
| 4968 | **mter** | 1 | 1 | - | 166.19 | - | 4,602 | - | 0.000339 | 🔵 low — common in general English | — |
| 4969 | **realiza** | 1 | 1 | - | 166.19 | - | 4,603 | - | 0.000339 | 🔵 low — common in general English | — |
| 4970 | **goal-the** | 1 | 1 | - | 166.19 | - | 4,604 | - | 0.000339 | 🔵 low — common in general English | — |
| 4971 | **dharma-i** | 1 | 1 | - | 166.19 | - | 4,605 | - | 0.000339 | 🔵 low — common in general English | — |
| 4972 | **junction** | 1 | 1 | - | 166.19 | - | 4,606 | - | 0.000339 | 🔵 low — common in general English | — |
| 4973 | **interconnected** | 1 | 1 | - | 166.19 | - | 4,607 | - | 0.000339 | 🔵 low — common in general English | — |
| 4974 | **elements-the** | 1 | 1 | - | 166.19 | - | 4,608 | - | 0.000339 | 🔵 low — common in general English | — |
| 4975 | **flint** | 1 | 1 | - | 166.19 | - | 4,609 | - | 0.000339 | 🔵 low — common in general English | — |
| 4976 | **rarer** | 1 | 1 | - | 166.19 | - | 4,610 | - | 0.000339 | 🔵 low — common in general English | — |
| 4977 | **advan** | 1 | 1 | - | 166.19 | - | 4,611 | - | 0.000338 | 🔵 low — common in general English | — |
| 4978 | **tage** | 1 | 1 | - | 166.19 | - | 4,612 | - | 0.000338 | 🔵 low — common in general English | — |
| 4979 | **perchance** | 1 | 1 | - | 166.19 | - | 4,613 | - | 0.000338 | 🔵 low — common in general English | — |
| 4980 | **adrift** | 1 | 1 | - | 166.19 | - | 4,614 | - | 0.000338 | 🔵 low — common in general English | — |
| 4981 | **shoreless** | 1 | 1 | - | 166.19 | - | 4,615 | - | 0.000338 | 🔵 low — common in general English | — |
| 4982 | **needle-which** | 1 | 1 | - | 166.19 | - | 4,616 | - | 0.000338 | 🔵 low — common in general English | — |
| 4983 | **saddened** | 1 | 1 | - | 166.19 | - | 4,617 | - | 0.000338 | 🔵 low — common in general English | — |
| 4984 | **fritter** | 1 | 1 | - | 166.19 | - | 4,618 | - | 0.000338 | 🔵 low — common in general English | — |
| 4985 | **jettison** | 1 | 1 | - | 166.19 | - | 4,619 | - | 0.000338 | 🔵 low — common in general English | — |
| 4986 | **trakpa** | 1 | 1 | - | 166.19 | - | 4,620 | - | 0.000338 | 🔵 low — common in general English | ~ |
| 4987 | **resourcefulness** | 1 | 1 | - | 166.19 | - | 4,621 | - | 0.000338 | 🔵 low — common in general English | — |
| 4988 | **raft** | 1 | 1 | - | 166.19 | - | 4,622 | - | 0.000338 | 🔵 low — common in general English | — |
| 4989 | **thing-the** | 1 | 1 | - | 166.19 | - | 4,623 | - | 0.000338 | 🔵 low — common in general English | — |
| 4990 | **preme** | 1 | 1 | - | 166.19 | - | 4,624 | - | 0.000338 | 🔵 low — common in general English | — |
| 4991 | **dharma-and** | 1 | 1 | - | 166.19 | - | 4,625 | - | 0.000338 | 🔵 low — common in general English | — |
| 4992 | **ineffectual** | 1 | 1 | - | 166.19 | - | 4,626 | - | 0.000338 | 🔵 low — common in general English | — |
| 4993 | **folly** | 1 | 1 | - | 166.19 | - | 4,627 | - | 0.000338 | 🔵 low — common in general English | — |
| 4994 | **betray** | 1 | 1 | - | 166.19 | - | 4,628 | - | 0.000338 | 🔵 low — common in general English | — |
| 4995 | **turning-point** | 1 | 1 | - | 166.19 | - | 4,629 | - | 0.000338 | 🔵 low — common in general English | — |
| 4996 | **bewildered** | 1 | 1 | - | 166.19 | - | 4,630 | - | 0.000338 | 🔵 low — common in general English | — |
| 4997 | **miyowa** | 1 | 1 | - | 166.19 | - | 4,631 | - | 0.000338 | 🔵 low — common in general English | — |
| 4998 | **fashioned** | 1 | 1 | - | 166.19 | - | 4,632 | - | 0.000338 | 🔵 low — common in general English | — |
| 4999 | **god-realm** | 1 | 1 | - | 166.19 | - | 4,633 | - | 0.000337 | 🔵 low — common in general English | — |
| 5000 | **fruit-bearing** | 1 | 1 | - | 166.19 | - | 4,634 | - | 0.000337 | 🔵 low — common in general English | — |
| 5001 | **manasarovar** | 1 | 1 | - | 166.19 | - | 4,635 | - | 0.000337 | 🔵 low — common in general English | — |
| 5002 | **sea-water** | 1 | 1 | - | 166.19 | - | 4,636 | - | 0.000337 | 🔵 low — common in general English | — |
| 5003 | **ear-shot** | 1 | 1 | - | 166.19 | - | 4,637 | - | 0.000337 | 🔵 low — common in general English | — |
| 5004 | **snow-covered** | 1 | 1 | - | 166.19 | - | 4,638 | - | 0.000337 | 🔵 low — common in general English | — |
| 5005 | **sub-continent** | 1 | 1 | - | 166.19 | - | 4,639 | - | 0.000337 | 🔵 low — common in general English | — |
| 5006 | **rim** | 1 | 1 | - | 166.19 | - | 4,640 | - | 0.000337 | 🔵 low — common in general English | — |
| 5007 | **engulf** | 1 | 1 | - | 166.19 | - | 4,641 | - | 0.000337 | 🔵 low — common in general English | — |
| 5008 | **conflagration** | 1 | 1 | - | 166.19 | - | 4,642 | - | 0.000337 | 🔵 low — common in general English | — |
| 5009 | **raincloud** | 1 | 1 | - | 166.19 | - | 4,643 | - | 0.000337 | 🔵 low — common in general English | — |
| 5010 | **devastation** | 1 | 1 | - | 166.19 | - | 4,644 | - | 0.000337 | 🔵 low — common in general English | — |
| 5011 | **sincerely-if** | 1 | 1 | - | 166.19 | - | 4,645 | - | 0.000337 | 🔵 low — common in general English | — |
| 5012 | **realm-even** | 1 | 1 | - | 166.19 | - | 4,646 | - | 0.000337 | 🔵 low — common in general English | — |
| 5013 | **gods-who** | 1 | 1 | - | 166.19 | - | 4,647 | - | 0.000337 | 🔵 low — common in general English | — |
| 5014 | **flicker** | 1 | 1 | - | 166.19 | - | 4,648 | - | 0.000337 | 🔵 low — common in general English | — |
| 5015 | **slumber** | 1 | 1 | - | 166.19 | - | 4,649 | - | 0.000337 | 🔵 low — common in general English | — |
| 5016 | **ever-present** | 1 | 1 | - | 166.19 | - | 4,650 | - | 0.000337 | 🔵 low — common in general English | — |
| 5017 | **status-until** | 1 | 1 | - | 166.19 | - | 4,651 | - | 0.000337 | 🔵 low — common in general English | — |
| 5018 | **gnashing** | 1 | 1 | - | 166.19 | - | 4,652 | - | 0.000337 | 🔵 low — common in general English | — |
| 5019 | **fang** | 1 | 1 | - | 166.19 | - | 4,653 | - | 0.000337 | 🔵 low — common in general English | — |
| 5020 | **charm** | 1 | 1 | - | 166.19 | - | 4,654 | - | 0.000337 | 🔵 low — common in general English | — |
| 5021 | **athlete** | 1 | 1 | - | 166.19 | - | 4,655 | - | 0.000336 | 🔵 low — common in general English | — |
| 5022 | **fleetness-none** | 1 | 1 | - | 166.19 | - | 4,656 | - | 0.000336 | 🔵 low — common in general English | — |
| 5023 | **impene** | 1 | 1 | - | 166.19 | - | 4,657 | - | 0.000336 | 🔵 low — common in general English | — |
| 5024 | **trable** | 1 | 1 | - | 166.19 | - | 4,658 | - | 0.000336 | 🔵 low — common in general English | — |
| 5025 | **concealment** | 1 | 1 | - | 166.19 | - | 4,659 | - | 0.000336 | 🔵 low — common in general English | — |
| 5026 | **glaze** | 1 | 1 | - | 166.19 | - | 4,660 | - | 0.000336 | 🔵 low — common in general English | — |
| 5027 | **willy-nilly** | 1 | 1 | - | 166.19 | - | 4,661 | - | 0.000336 | 🔵 low — common in general English | — |
| 5028 | **defender** | 1 | 1 | - | 166.19 | - | 4,662 | - | 0.000336 | 🔵 low — common in general English | — |
| 5029 | **you-can** | 1 | 1 | - | 166.19 | - | 4,663 | - | 0.000336 | 🔵 low — common in general English | — |
| 5030 | **dispensation** | 1 | 1 | - | 166.19 | - | 4,664 | - | 0.000336 | 🔵 low — common in general English | — |
| 5031 | **miracu** | 1 | 1 | - | 166.19 | - | 4,665 | - | 0.000336 | 🔵 low — common in general English | — |
| 5032 | **lous** | 1 | 1 | - | 166.19 | - | 4,666 | - | 0.000336 | 🔵 low — common in general English | — |
| 5033 | **ofyerpa** | 1 | 1 | - | 166.19 | - | 4,667 | - | 0.000336 | 🔵 low — common in general English | — |
| 5034 | **zur** | 1 | 1 | - | 166.19 | - | 4,668 | - | 0.000336 | 🔵 low — common in general English | ~ |
| 5035 | **nub** | 1 | 1 | - | 166.19 | - | 4,669 | - | 0.000336 | 🔵 low — common in general English | ~ |
| 5036 | **clan** | 1 | 1 | - | 166.19 | - | 4,670 | - | 0.000336 | 🔵 low — common in general English | — |
| 5037 | **plished** | 1 | 1 | - | 166.19 | - | 4,671 | - | 0.000336 | 🔵 low — common in general English | — |
| 5038 | **space-they** | 1 | 1 | - | 166.19 | - | 4,672 | - | 0.000336 | 🔵 low — common in general English | — |
| 5039 | **silence** | 1 | 1 | - | 166.19 | - | 4,673 | - | 0.000336 | 🔵 low — common in general English | — |
| 5040 | **nyeshangkatya** | 1 | 1 | - | 166.19 | - | 4,674 | - | 0.000336 | 🔵 low — common in general English | — |
| 5041 | **motionless** | 1 | 1 | - | 166.19 | - | 4,675 | - | 0.000336 | 🔵 low — common in general English | — |
| 5042 | **volley** | 1 | 1 | - | 166.19 | - | 4,676 | - | 0.000336 | 🔵 low — common in general English | — |
| 5043 | **cliff-but** | 1 | 1 | - | 166.19 | - | 4,677 | - | 0.000335 | 🔵 low — common in general English | — |
| 5044 | **firewood** | 1 | 1 | - | 166.19 | - | 4,678 | - | 0.000335 | 🔵 low — common in general English | — |
| 5045 | **contraption** | 1 | 1 | - | 166.19 | - | 4,679 | - | 0.000335 | 🔵 low — common in general English | — |
| 5046 | **depends-and** | 1 | 1 | - | 166.19 | - | 4,680 | - | 0.000335 | 🔵 low — common in general English | — |
| 5047 | **scarecrow** | 1 | 1 | - | 166.19 | - | 4,681 | - | 0.000335 | 🔵 low — common in general English | — |
| 5048 | **momerit** | 1 | 1 | - | 166.19 | - | 4,682 | - | 0.000335 | 🔵 low — common in general English | — |
| 5049 | **illustrious** | 1 | 1 | - | 166.19 | - | 4,683 | - | 0.000335 | 🔵 low — common in general English | — |
| 5050 | **stature** | 1 | 1 | - | 166.19 | - | 4,684 | - | 0.000335 | 🔵 low — common in general English | — |
| 5051 | **earshot** | 1 | 1 | - | 166.19 | - | 4,685 | - | 0.000335 | 🔵 low — common in general English | — |
| 5052 | **resplendence** | 1 | 1 | - | 166.19 | - | 4,686 | - | 0.000335 | 🔵 low — common in general English | — |
| 5053 | **outshine** | 1 | 1 | - | 166.19 | - | 4,687 | - | 0.000335 | 🔵 low — common in general English | — |
| 5054 | **mahdvara** | 1 | 1 | - | 166.19 | - | 4,688 | - | 0.000335 | 🔵 low — common in general English | — |
| 5055 | **evade** | 1 | 1 | - | 166.19 | - | 4,689 | - | 0.000335 | 🔵 low — common in general English | — |
| 5056 | **consolation** | 1 | 1 | - | 166.19 | - | 4,690 | - | 0.000335 | 🔵 low — common in general English | — |
| 5057 | **mahasammata** | 1 | 1 | - | 166.19 | - | 4,691 | - | 0.000335 | 🔵 low — common in general English | — |
| 5058 | **pala** | 1 | 1 | - | 166.19 | - | 4,692 | - | 0.000335 | 🔵 low — common in general English | — |
| 5059 | **candra** | 1 | 1 | - | 166.19 | - | 4,693 | - | 0.000335 | 🔵 low — common in general English | — |
| 5060 | **nivara** | 1 | 1 | - | 166.19 | - | 4,694 | - | 0.000335 | 🔵 low — common in general English | — |
| 5061 | **tavi** | 1 | 1 | - | 166.19 | - | 4,695 | - | 0.000335 | 🔵 low — common in general English | — |
| 5062 | **kambhin** | 1 | 1 | - | 166.19 | - | 4,696 | - | 0.000335 | 🔵 low — common in general English | — |
| 5063 | **earthly** | 1 | 1 | - | 166.19 | - | 4,697 | - | 0.000335 | 🔵 low — common in general English | — |
| 5064 | **lek** | 1 | 1 | - | 166.19 | - | 4,698 | - | 0.000335 | 🔵 low — common in general English | — |
| 5065 | **jambu** | 1 | 1 | - | 166.19 | - | 4,699 | - | 0.000335 | 🔵 low — common in general English | — |
| 5066 | **dvipa** | 1 | 1 | - | 166.19 | - | 4,700 | - | 0.000334 | 🔵 low — common in general English | — |
| 5067 | **ralpachen** | 1 | 1 | - | 166.19 | - | 4,701 | - | 0.000334 | 🔵 low — common in general English | — |
| 5068 | **gesar** | 1 | 1 | - | 166.19 | - | 4,702 | - | 0.000334 | 🔵 low — common in general English | — |
| 5069 | **tajikistan** | 1 | 1 | - | 166.19 | - | 4,703 | - | 0.000334 | 🔵 low — common in general English | — |
| 5070 | **ambassa** | 1 | 1 | - | 166.19 | - | 4,704 | - | 0.000334 | 🔵 low — common in general English | — |
| 5071 | **dor** | 1 | 1 | - | 166.19 | - | 4,705 | - | 0.000334 | 🔵 low — common in general English | — |
| 5072 | **beehive** | 1 | 1 | - | 166.19 | - | 4,706 | - | 0.000334 | 🔵 low — common in general English | — |
| 5073 | **race** | 1 | 1 | - | 166.19 | - | 4,707 | - | 0.000334 | 🔵 low — common in general English | — |
| 5074 | **abstinence** | 1 | 1 | - | 166.19 | - | 4,708 | - | 0.000334 | 🔵 low — common in general English | — |
| 5075 | **summertime** | 1 | 1 | - | 166.19 | - | 4,709 | - | 0.000334 | 🔵 low — common in general English | — |
| 5076 | **meadow** | 1 | 1 | - | 166.19 | - | 4,710 | - | 0.000334 | 🔵 low — common in general English | — |
| 5077 | **lush** | 1 | 1 | - | 166.19 | - | 4,711 | - | 0.000334 | 🔵 low — common in general English | — |
| 5078 | **bask** | 1 | 1 | - | 166.19 | - | 4,712 | - | 0.000334 | 🔵 low — common in general English | — |
| 5079 | **scarlet** | 1 | 1 | - | 166.19 | - | 4,713 | - | 0.000334 | 🔵 low — common in general English | — |
| 5080 | **grassland** | 1 | 1 | - | 166.19 | - | 4,714 | - | 0.000334 | 🔵 low — common in general English | — |
| 5081 | **hue** | 1 | 1 | - | 166.19 | - | 4,715 | - | 0.000334 | 🔵 low — common in general English | — |
| 5082 | **brittle** | 1 | 1 | - | 166.19 | - | 4,716 | - | 0.000334 | 🔵 low — common in general English | — |
| 5083 | **glacial** | 1 | 1 | - | 166.19 | - | 4,717 | - | 0.000334 | 🔵 low — common in general English | — |
| 5084 | **scour** | 1 | 1 | - | 166.19 | - | 4,718 | - | 0.000334 | 🔵 low — common in general English | — |
| 5085 | **helpless** | 1 | 1 | - | 166.19 | - | 4,719 | - | 0.000334 | 🔵 low — common in general English | — |
| 5086 | **grandparent** | 1 | 1 | - | 166.19 | - | 4,720 | - | 0.000334 | 🔵 low — common in general English | — |
| 5087 | **great-grandparent** | 1 | 1 | - | 166.19 | - | 4,721 | - | 0.000334 | 🔵 low — common in general English | — |
| 5088 | **eminent** | 1 | 1 | - | 166.19 | - | 4,722 | - | 0.000334 | 🔵 low — common in general English | — |
| 5089 | **year-or** | 1 | 1 | - | 166.19 | - | 4,723 | - | 0.000333 | 🔵 low — common in general English | — |
| 5090 | **animals-sheep** | 1 | 1 | - | 166.19 | - | 4,724 | - | 0.000333 | 🔵 low — common in general English | — |
| 5091 | **dogs-how** | 1 | 1 | - | 166.19 | - | 4,725 | - | 0.000333 | 🔵 low — common in general English | — |
| 5092 | **animate** | 1 | 1 | - | 166.19 | - | 4,726 | - | 0.000333 | 🔵 low — common in general English | — |
| 5093 | **mind-everything** | 1 | 1 | - | 166.19 | - | 4,727 | - | 0.000333 | 🔵 low — common in general English | — |
| 5094 | **exalted** | 1 | 1 | - | 166.19 | - | 4,728 | - | 0.000333 | 🔵 low — common in general English | — |
| 5095 | **rainbow-but** | 1 | 1 | - | 166.19 | - | 4,729 | - | 0.000333 | 🔵 low — common in general English | — |
| 5096 | **stiffly** | 1 | 1 | - | 166.19 | - | 4,730 | - | 0.000333 | 🔵 low — common in general English | — |
| 5097 | **armpit** | 1 | 1 | - | 166.19 | - | 4,731 | - | 0.000333 | 🔵 low — common in general English | — |
| 5098 | **cherished** | 1 | 1 | - | 166.19 | - | 4,732 | - | 0.000333 | 🔵 low — common in general English | — |
| 5099 | **thread** | 1 | 1 | - | 166.19 | - | 4,733 | - | 0.000333 | 🔵 low — common in general English | — |
| 5100 | **beloved** | 1 | 1 | - | 166.19 | - | 4,734 | - | 0.000333 | 🔵 low — common in general English | — |
| 5101 | **handsome** | 1 | 1 | - | 166.19 | - | 4,735 | - | 0.000333 | 🔵 low — common in general English | — |
| 5102 | **distinguished** | 1 | 1 | - | 166.19 | - | 4,736 | - | 0.000333 | 🔵 low — common in general English | — |
| 5103 | **horribly** | 1 | 1 | - | 166.19 | - | 4,737 | - | 0.000333 | 🔵 low — common in general English | — |
| 5104 | **livid** | 1 | 1 | - | 166.19 | - | 4,738 | - | 0.000333 | 🔵 low — common in general English | — |
| 5105 | **here-our** | 1 | 1 | - | 166.19 | - | 4,739 | - | 0.000333 | 🔵 low — common in general English | — |
| 5106 | **trussed** | 1 | 1 | - | 166.19 | - | 4,740 | - | 0.000333 | 🔵 low — common in general English | — |
| 5107 | **curtain** | 1 | 1 | - | 166.19 | - | 4,741 | - | 0.000333 | 🔵 low — common in general English | — |
| 5108 | **sheepskin** | 1 | 1 | - | 166.19 | - | 4,742 | - | 0.000333 | 🔵 low — common in general English | — |
| 5109 | **rug** | 1 | 1 | - | 166.19 | - | 4,743 | - | 0.000333 | 🔵 low — common in general English | — |
| 5110 | **tuft** | 1 | 1 | - | 166.19 | - | 4,744 | - | 0.000333 | 🔵 low — common in general English | — |
| 5111 | **bespattered** | 1 | 1 | - | 166.19 | - | 4,745 | - | 0.000333 | 🔵 low — common in general English | — |
| 5112 | **cremating** | 1 | 1 | - | 166.19 | - | 4,746 | - | 0.000332 | 🔵 low — common in general English | — |
| 5113 | **vagabond** | 1 | 1 | - | 166.19 | - | 4,747 | - | 0.000332 | 🔵 low — common in general English | — |
| 5114 | **enjoy-teacher** | 1 | 1 | - | 166.19 | - | 4,748 | - | 0.000332 | 🔵 low — common in general English | — |
| 5115 | **protege** | 1 | 1 | - | 166.19 | - | 4,749 | - | 0.000332 | 🔵 low — common in general English | — |
| 5116 | **comrade** | 1 | 1 | - | 166.19 | - | 4,750 | - | 0.000332 | 🔵 low — common in general English | — |
| 5117 | **wives-there** | 1 | 1 | - | 166.19 | - | 4,751 | - | 0.000332 | 🔵 low — common in general English | — |
| 5118 | **three-storeyed** | 1 | 1 | - | 166.19 | - | 4,752 | - | 0.000332 | 🔵 low — common in general English | — |
| 5119 | **emanated** | 1 | 1 | - | 166.19 | - | 4,753 | - | 0.000332 | 🔵 low — common in general English | — |
| 5120 | **rivalled** | 1 | 1 | - | 166.19 | - | 4,754 | - | 0.000332 | 🔵 low — common in general English | — |
| 5121 | **kagyupa** | 1 | 1 | - | 166.19 | - | 4,755 | - | 0.000332 | 🔵 low — common in general English | ✓ བཀའ་བརྒྱུད་པ |
| 5122 | **wield** | 1 | 1 | - | 166.19 | - | 4,756 | - | 0.000332 | 🔵 low — common in general English | — |
| 5123 | **governments-not** | 1 | 1 | - | 166.19 | - | 4,757 | - | 0.000332 | 🔵 low — common in general English | — |
| 5124 | **languishing** | 1 | 1 | - | 166.19 | - | 4,758 | - | 0.000332 | 🔵 low — common in general English | — |
| 5125 | **alms-round** | 1 | 1 | - | 166.19 | - | 4,759 | - | 0.000332 | 🔵 low — common in general English | — |
| 5126 | **sworn** | 1 | 1 | - | 166.19 | - | 4,760 | - | 0.000332 | 🔵 low — common in general English | — |
| 5127 | **intimately** | 1 | 1 | - | 166.19 | - | 4,761 | - | 0.000332 | 🔵 low — common in general English | — |
| 5128 | **paltry** | 1 | 1 | - | 166.19 | - | 4,762 | - | 0.000332 | 🔵 low — common in general English | — |
| 5129 | **insignifi** | 1 | 1 | - | 166.19 | - | 4,763 | - | 0.000332 | 🔵 low — common in general English | — |
| 5130 | **cant** | 1 | 1 | - | 166.19 | - | 4,764 | - | 0.000332 | 🔵 low — common in general English | — |
| 5131 | **deprivation** | 1 | 1 | - | 166.19 | - | 4,765 | - | 0.000332 | 🔵 low — common in general English | — |
| 5132 | **well-off** | 1 | 1 | - | 166.19 | - | 4,766 | - | 0.000332 | 🔵 low — common in general English | — |
| 5133 | **merry** | 1 | 1 | - | 166.19 | - | 4,767 | - | 0.000332 | 🔵 low — common in general English | — |
| 5134 | **nightfall** | 1 | 1 | - | 166.19 | - | 4,768 | - | 0.000332 | 🔵 low — common in general English | — |
| 5135 | **unparalleled** | 1 | 1 | - | 166.19 | - | 4,769 | - | 0.000331 | 🔵 low — common in general English | — |
| 5136 | **aparantaka** | 1 | 1 | - | 166.19 | - | 4,770 | - | 0.000331 | 🔵 low — common in general English | — |
| 5137 | **more-and** | 1 | 1 | - | 166.19 | - | 4,771 | - | 0.000331 | 🔵 low — common in general English | — |
| 5138 | **ever-changing** | 1 | 1 | - | 166.19 | - | 4,772 | - | 0.000331 | 🔵 low — common in general English | — |
| 5139 | **mediocrity** | 1 | 1 | - | 166.19 | - | 4,773 | - | 0.000331 | 🔵 low — common in general English | — |
| 5140 | **eloquent** | 1 | 1 | - | 166.19 | - | 4,774 | - | 0.000331 | 🔵 low — common in general English | — |
| 5141 | **despis** | 1 | 1 | - | 166.19 | - | 4,775 | - | 0.000331 | 🔵 low — common in general English | — |
| 5142 | **liar** | 1 | 1 | - | 166.19 | - | 4,776 | - | 0.000331 | 🔵 low — common in general English | — |
| 5143 | **common-sense** | 1 | 1 | - | 166.19 | - | 4,777 | - | 0.000331 | 🔵 low — common in general English | — |
| 5144 | **trusted** | 1 | 1 | - | 166.19 | - | 4,778 | - | 0.000331 | 🔵 low — common in general English | — |
| 5145 | **esteemed** | 1 | 1 | - | 166.19 | - | 4,779 | - | 0.000331 | 🔵 low — common in general English | — |
| 5146 | **busily** | 1 | 1 | - | 166.19 | - | 4,780 | - | 0.000331 | 🔵 low — common in general English | — |
| 5147 | **tricked** | 1 | 1 | - | 166.19 | - | 4,781 | - | 0.000331 | 🔵 low — common in general English | — |
| 5148 | **conscientious** | 1 | 1 | - | 166.19 | - | 4,782 | - | 0.000331 | 🔵 low — common in general English | — |
| 5149 | **stantly** | 1 | 1 | - | 166.19 | - | 4,783 | - | 0.000331 | 🔵 low — common in general English | — |
| 5150 | **poignant** | 1 | 1 | - | 166.19 | - | 4,784 | - | 0.000331 | 🔵 low — common in general English | — |
| 5151 | **transitoriness** | 1 | 1 | - | 166.19 | - | 4,785 | - | 0.000331 | 🔵 low — common in general English | — |
| 5152 | **feud** | 1 | 1 | - | 166.19 | - | 4,786 | - | 0.000331 | 🔵 low — common in general English | — |
| 5153 | **gelong** | 1 | 1 | - | 166.19 | - | 4,787 | - | 0.000331 | 🔵 low — common in general English | — |
| 5154 | **pigeon** | 1 | 1 | - | 166.19 | - | 4,788 | - | 0.000331 | 🔵 low — common in general English | — |
| 5155 | **exterminate** | 1 | 1 | - | 166.19 | - | 4,789 | - | 0.000331 | 🔵 low — common in general English | — |
| 5156 | **commander** | 1 | 1 | - | 166.19 | - | 4,790 | - | 0.000331 | 🔵 low — common in general English | — |
| 5157 | **superficial** | 1 | 1 | - | 166.19 | - | 4,791 | - | 0.000331 | 🔵 low — common in general English | — |
| 5158 | **beasts-all** | 1 | 1 | - | 166.19 | - | 4,792 | - | 0.000330 | 🔵 low — common in general English | — |
| 5159 | **lifesustaining** | 1 | 1 | - | 166.19 | - | 4,793 | - | 0.000330 | 🔵 low — common in general English | — |
| 5160 | **fatality** | 1 | 1 | - | 166.19 | - | 4,794 | - | 0.000330 | 🔵 low — common in general English | — |
| 5161 | **eating-the** | 1 | 1 | - | 166.19 | - | 4,795 | - | 0.000330 | 🔵 low — common in general English | — |
| 5162 | **oblivious** | 1 | 1 | - | 166.19 | - | 4,796 | - | 0.000330 | 🔵 low — common in general English | — |
| 5163 | **mear** | 1 | 1 | - | 166.19 | - | 4,797 | - | 0.000330 | 🔵 low — common in general English | — |
| 5164 | **unhealthy** | 1 | 1 | - | 166.19 | - | 4,798 | - | 0.000330 | 🔵 low — common in general English | — |
| 5165 | **tumour** | 1 | 1 | - | 166.19 | - | 4,799 | - | 0.000330 | 🔵 low — common in general English | — |
| 5166 | **disorder** | 1 | 1 | - | 166.19 | - | 4,800 | - | 0.000330 | 🔵 low — common in general English | — |
| 5167 | **dropsy** | 1 | 1 | - | 166.19 | - | 4,801 | - | 0.000330 | 🔵 low — common in general English | — |
| 5168 | **incite** | 1 | 1 | - | 166.19 | - | 4,802 | - | 0.000330 | 🔵 low — common in general English | — |
| 5169 | **decrepit** | 1 | 1 | - | 166.19 | - | 4,803 | - | 0.000330 | 🔵 low — common in general English | — |
| 5170 | **linger** | 1 | 1 | - | 166.19 | - | 4,804 | - | 0.000330 | 🔵 low — common in general English | — |
| 5171 | **glued** | 1 | 1 | - | 166.19 | - | 4,805 | - | 0.000330 | 🔵 low — common in general English | — |
| 5172 | **candle-flame** | 1 | 1 | - | 166.19 | - | 4,806 | - | 0.000330 | 🔵 low — common in general English | — |
| 5173 | **celebrity** | 1 | 1 | - | 166.19 | - | 4,807 | - | 0.000330 | 🔵 low — common in general English | — |
| 5174 | **sorrowful** | 1 | 1 | - | 166.19 | - | 4,808 | - | 0.000330 | 🔵 low — common in general English | — |
| 5175 | **escaping** | 1 | 1 | - | 166.19 | - | 4,809 | - | 0.000330 | 🔵 low — common in general English | — |
| 5176 | **bhik** | 1 | 1 | - | 166.19 | - | 4,810 | - | 0.000330 | 🔵 low — common in general English | — |
| 5177 | **ractice** | 1 | 1 | - | 166.19 | - | 4,811 | - | 0.000330 | 🔵 low — common in general English | — |
| 5178 | **sameness** | 1 | 1 | - | 166.19 | - | 4,812 | - | 0.000330 | 🔵 low — common in general English | — |
| 5179 | **insatiable** | 1 | 1 | - | 166.19 | - | 4,813 | - | 0.000330 | 🔵 low — common in general English | — |
| 5180 | **ha-ha** | 1 | 1 | - | 166.19 | - | 4,814 | - | 0.000330 | 🔵 low — common in general English | — |
| 5181 | **proudest** | 1 | 1 | - | 166.19 | - | 4,815 | - | 0.000330 | 🔵 low — common in general English | — |
| 5182 | **engross** | 1 | 1 | - | 166.19 | - | 4,816 | - | 0.000329 | 🔵 low — common in general English | — |
| 5183 | **revel** | 1 | 1 | - | 166.19 | - | 4,817 | - | 0.000329 | 🔵 low — common in general English | — |
| 5184 | **abhorrent** | 1 | 1 | - | 166.19 | - | 4,818 | - | 0.000329 | 🔵 low — common in general English | — |
| 5185 | **sealing** | 1 | 1 | - | 166.19 | - | 4,819 | - | 0.000329 | 🔵 low — common in general English | — |
| 5186 | **vaster** | 1 | 1 | - | 166.19 | - | 4,820 | - | 0.000329 | 🔵 low — common in general English | — |
| 5187 | **twinkling** | 1 | 1 | - | 166.19 | - | 4,821 | - | 0.000329 | 🔵 low — common in general English | — |
| 5188 | **headlong** | 1 | 1 | - | 166.19 | - | 4,822 | - | 0.000329 | 🔵 low — common in general English | — |
| 5189 | **scorching** | 1 | 1 | - | 166.19 | - | 4,823 | - | 0.000329 | 🔵 low — common in general English | — |
| 5190 | **perimeter** | 1 | 1 | - | 166.19 | - | 4,824 | - | 0.000329 | 🔵 low — common in general English | — |
| 5191 | **white-hot** | 1 | 1 | - | 166.19 | - | 4,825 | - | 0.000329 | 🔵 low — common in general English | — |
| 5192 | **smith-there** | 1 | 1 | - | 166.19 | - | 4,826 | - | 0.000329 | 🔵 low — common in general English | — |
| 5193 | **searingly** | 1 | 1 | - | 166.19 | - | 4,827 | - | 0.000329 | 🔵 low — common in general English | — |
| 5194 | **incandescent** | 1 | 1 | - | 166.19 | - | 4,828 | - | 0.000329 | 🔵 low — common in general English | — |
| 5195 | **snowflake** | 1 | 1 | - | 166.19 | - | 4,829 | - | 0.000329 | 🔵 low — common in general English | — |
| 5196 | **furiously** | 1 | 1 | - | 166.19 | - | 4,830 | - | 0.000329 | 🔵 low — common in general English | — |
| 5197 | **weapons-a** | 1 | 1 | - | 166.19 | - | 4,831 | - | 0.000329 | 🔵 low — common in general English | — |
| 5198 | **armoury** | 1 | 1 | - | 166.19 | - | 4,832 | - | 0.000329 | 🔵 low — common in general English | — |
| 5199 | **fifty** | 1 | 1 | - | 166.19 | - | 4,833 | - | 0.000329 | 🔵 low — common in general English | — |
| 5200 | **firebrand** | 1 | 1 | - | 166.19 | - | 4,834 | - | 0.000329 | 🔵 low — common in general English | — |
| 5201 | **cross-rule** | 1 | 1 | - | 166.19 | - | 4,835 | - | 0.000329 | 🔵 low — common in general English | — |
| 5202 | **on-which** | 1 | 1 | - | 166.19 | - | 4,836 | - | 0.000329 | 🔵 low — common in general English | — |
| 5203 | **hacked** | 1 | 1 | - | 166.19 | - | 4,837 | - | 0.000329 | 🔵 low — common in general English | — |
| 5204 | **whirling** | 1 | 1 | - | 166.19 | - | 4,838 | - | 0.000329 | 🔵 low — common in general English | — |
| 5205 | **ram** | 1 | 1 | - | 166.19 | - | 4,839 | - | 0.000329 | 🔵 low — common in general English | — |
| 5206 | **butt** | 1 | 1 | - | 166.19 | - | 4,840 | - | 0.000328 | 🔵 low — common in general English | — |
| 5207 | **horn-tip** | 1 | 1 | - | 166.19 | - | 4,841 | - | 0.000328 | 🔵 low — common in general English | — |
| 5208 | **spewing** | 1 | 1 | - | 166.19 | - | 4,842 | - | 0.000328 | 🔵 low — common in general English | — |
| 5209 | **scream** | 1 | 1 | - | 166.19 | - | 4,843 | - | 0.000328 | 🔵 low — common in general English | — |
| 5210 | **shove** | 1 | 1 | - | 166.19 | - | 4,844 | - | 0.000328 | 🔵 low — common in general English | — |
| 5211 | **howl** | 1 | 1 | - | 166.19 | - | 4,845 | - | 0.000328 | 🔵 low — common in general English | — |
| 5212 | **cauldron** | 1 | 1 | - | 166.19 | - | 4,846 | - | 0.000328 | 🔵 low — common in general English | — |
| 5213 | **impale** | 1 | 1 | - | 166.19 | - | 4,847 | - | 0.000328 | 🔵 low — common in general English | — |
| 5214 | **heel** | 1 | 1 | - | 166.19 | - | 4,848 | - | 0.000328 | 🔵 low — common in general English | — |
| 5215 | **edifice** | 1 | 1 | - | 166.19 | - | 4,849 | - | 0.000328 | 🔵 low — common in general English | — |
| 5216 | **bellow** | 1 | 1 | - | 166.19 | - | 4,850 | - | 0.000328 | 🔵 low — common in general English | — |
| 5217 | **leopard-skin** | 1 | 1 | - | 166.19 | - | 4,851 | - | 0.000328 | 🔵 low — common in general English | — |
| 5218 | **indi** | 1 | 1 | - | 166.19 | - | 4,852 | - | 0.000328 | 🔵 low — common in general English | — |
| 5219 | **tinguishable** | 1 | 1 | - | 166.19 | - | 4,853 | - | 0.000328 | 🔵 low — common in general English | — |
| 5220 | **razor-edged** | 1 | 1 | - | 166.19 | - | 4,854 | - | 0.000328 | 🔵 low — common in general English | — |
| 5221 | **directions-the** | 1 | 1 | - | 166.19 | - | 4,855 | - | 0.000328 | 🔵 low — common in general English | — |
| 5222 | **northeast-stand** | 1 | 1 | - | 166.19 | - | 4,856 | - | 0.000328 | 🔵 low — common in general English | — |
| 5223 | **purged** | 1 | 1 | - | 166.19 | - | 4,857 | - | 0.000328 | 🔵 low — common in general English | — |
| 5224 | **shady** | 1 | 1 | - | 166.19 | - | 4,858 | - | 0.000328 | 🔵 low — common in general English | — |
| 5225 | **putrescent** | 1 | 1 | - | 166.19 | - | 4,859 | - | 0.000328 | 🔵 low — common in general English | — |
| 5226 | **brazier** | 1 | 1 | - | 166.19 | - | 4,860 | - | 0.000328 | 🔵 low — common in general English | — |
| 5227 | **corpses-corps** | 1 | 1 | - | 166.19 | - | 4,861 | - | 0.000328 | 🔵 low — common in general English | — |
| 5228 | **dogs-all** | 1 | 1 | - | 166.19 | - | 4,862 | - | 0.000328 | 🔵 low — common in general English | — |
| 5229 | **decomposing** | 1 | 1 | - | 166.19 | - | 4,863 | - | 0.000328 | 🔵 low — common in general English | — |
| 5230 | **decompose** | 1 | 1 | - | 166.19 | - | 4,864 | - | 0.000327 | 🔵 low — common in general English | — |
| 5231 | **foulest** | 1 | 1 | - | 166.19 | - | 4,865 | - | 0.000327 | 🔵 low — common in general English | — |
| 5232 | **stench** | 1 | 1 | - | 166.19 | - | 4,866 | - | 0.000327 | 🔵 low — common in general English | — |
| 5233 | **mire** | 1 | 1 | - | 166.19 | - | 4,867 | - | 0.000327 | 🔵 low — common in general English | — |
| 5234 | **thrilled** | 1 | 1 | - | 166.19 | - | 4,868 | - | 0.000327 | 🔵 low — common in general English | — |
| 5235 | **slender** | 1 | 1 | - | 166.19 | - | 4,869 | - | 0.000327 | 🔵 low — common in general English | — |
| 5236 | **heal** | 1 | 1 | - | 166.19 | - | 4,870 | - | 0.000327 | 🔵 low — common in general English | — |
| 5237 | **it-only** | 1 | 1 | - | 166.19 | - | 4,871 | - | 0.000327 | 🔵 low — common in general English | — |
| 5238 | **excruciatingly** | 1 | 1 | - | 166.19 | - | 4,872 | - | 0.000327 | 🔵 low — common in general English | — |
| 5239 | **reconstitute** | 1 | 1 | - | 166.19 | - | 4,873 | - | 0.000327 | 🔵 low — common in general English | — |
| 5240 | **eagerly** | 1 | 1 | - | 166.19 | - | 4,874 | - | 0.000327 | 🔵 low — common in general English | — |
| 5241 | **stabbing** | 1 | 1 | - | 166.19 | - | 4,875 | - | 0.000327 | 🔵 low — common in general English | — |
| 5242 | **metallic** | 1 | 1 | - | 166.19 | - | 4,876 | - | 0.000327 | 🔵 low — common in general English | — |
| 5243 | **unshake** | 1 | 1 | - | 166.19 | - | 4,877 | - | 0.000327 | 🔵 low — common in general English | — |
| 5244 | **glacier** | 1 | 1 | - | 166.19 | - | 4,878 | - | 0.000327 | 🔵 low — common in general English | — |
| 5245 | **perpetually** | 1 | 1 | - | 166.19 | - | 4,879 | - | 0.000327 | 🔵 low — common in general English | — |
| 5246 | **enveloped** | 1 | 1 | - | 166.19 | - | 4,880 | - | 0.000327 | 🔵 low — common in general English | — |
| 5247 | **lamentation** | 1 | 1 | - | 166.19 | - | 4,881 | - | 0.000327 | 🔵 low — common in general English | — |
| 5248 | **ofutpala-like** | 1 | 1 | - | 166.19 | - | 4,882 | - | 0.000327 | 🔵 low — common in general English | — |
| 5249 | **petal-like** | 1 | 1 | - | 166.19 | - | 4,883 | - | 0.000327 | 🔵 low — common in general English | — |
| 5250 | **unbearably** | 1 | 1 | - | 166.19 | - | 4,884 | - | 0.000327 | 🔵 low — common in general English | — |
| 5251 | **broom** | 1 | 1 | - | 166.19 | - | 4,885 | - | 0.000327 | 🔵 low — common in general English | — |
| 5252 | **yutso** | 1 | 1 | - | 166.19 | - | 4,886 | - | 0.000327 | 🔵 low — common in general English | — |
| 5253 | **ngonmo** | 1 | 1 | - | 166.19 | - | 4,887 | - | 0.000327 | 🔵 low — common in general English | — |
| 5254 | **snpo** | 1 | 1 | - | 166.19 | - | 4,888 | - | 0.000326 | 🔵 low — common in general English | — |
| 5255 | **kangchen** | 1 | 1 | - | 166.19 | - | 4,889 | - | 0.000326 | 🔵 low — common in general English | — |
| 5256 | **zemaguru** | 1 | 1 | - | 166.19 | - | 4,890 | - | 0.000326 | 🔵 low — common in general English | — |
| 5257 | **exclaiming** | 1 | 1 | - | 166.19 | - | 4,891 | - | 0.000326 | 🔵 low — common in general English | — |
| 5258 | **misused** | 1 | 1 | - | 166.19 | - | 4,892 | - | 0.000326 | 🔵 low — common in general English | — |
| 5259 | **spanned** | 1 | 1 | - | 166.19 | - | 4,893 | - | 0.000326 | 🔵 low — common in general English | — |
| 5260 | **squirming** | 1 | 1 | - | 166.19 | - | 4,894 | - | 0.000326 | 🔵 low — common in general English | — |
| 5261 | **tsangla** | 1 | 1 | - | 166.19 | - | 4,895 | - | 0.000326 | 🔵 low — common in general English | — |
| 5262 | **tanakchen** | 1 | 1 | - | 166.19 | - | 4,896 | - | 0.000326 | 🔵 low — common in general English | — |
| 5263 | **angtong** | 1 | 1 | - | 166.19 | - | 4,897 | - | 0.000326 | 🔵 low — common in general English | — |
| 5264 | **exercis** | 1 | 1 | - | 166.19 | - | 4,898 | - | 0.000326 | 🔵 low — common in general English | — |
| 5265 | **gullet** | 1 | 1 | - | 166.19 | - | 4,899 | - | 0.000326 | 🔵 low — common in general English | — |
| 5266 | **kidney** | 1 | 1 | - | 166.19 | - | 4,900 | - | 0.000326 | 🔵 low — common in general English | — |
| 5267 | **shawl** | 1 | 1 | - | 166.19 | - | 4,901 | - | 0.000326 | 🔵 low — common in general English | — |
| 5268 | **munch** | 1 | 1 | - | 166.19 | - | 4,902 | - | 0.000326 | 🔵 low — common in general English | — |
| 5269 | **leisurely** | 1 | 1 | - | 166.19 | - | 4,903 | - | 0.000326 | 🔵 low — common in general English | — |
| 5270 | **steaming** | 1 | 1 | - | 166.19 | - | 4,904 | - | 0.000326 | 🔵 low — common in general English | — |
| 5271 | **whisker** | 1 | 1 | - | 166.19 | - | 4,905 | - | 0.000326 | 🔵 low — common in general English | — |
| 5272 | **reddish** | 1 | 1 | - | 166.19 | - | 4,906 | - | 0.000326 | 🔵 low — common in general English | — |
| 5273 | **tinge** | 1 | 1 | - | 166.19 | - | 4,907 | - | 0.000326 | 🔵 low — common in general English | — |
| 5274 | **palden** | 1 | 1 | - | 166.19 | - | 4,908 | - | 0.000326 | 🔵 low — common in general English | — |
| 5275 | **chokyong** | 1 | 1 | - | 166.19 | - | 4,909 | - | 0.000326 | 🔵 low — common in general English | — |
| 5276 | **ngor** | 1 | 1 | - | 166.19 | - | 4,910 | - | 0.000326 | 🔵 low — common in general English | — |
| 5277 | **ngulda** | 1 | 1 | - | 166.19 | - | 4,911 | - | 0.000326 | 🔵 low — common in general English | — |
| 5278 | **tree-trunk** | 1 | 1 | - | 166.19 | - | 4,912 | - | 0.000326 | 🔵 low — common in general English | — |
| 5279 | **aher** | 1 | 1 | - | 166.19 | - | 4,913 | - | 0.000325 | 🔵 low — common in general English | — |
| 5280 | **pogye** | 1 | 1 | - | 166.19 | - | 4,914 | - | 0.000325 | 🔵 low — common in general English | — |
| 5281 | **all-powerful** | 1 | 1 | - | 166.19 | - | 4,915 | - | 0.000325 | 🔵 low — common in general English | — |
| 5282 | **dignitary** | 1 | 1 | - | 166.19 | - | 4,916 | - | 0.000325 | 🔵 low — common in general English | — |
| 5283 | **srm** | 1 | 1 | - | 166.19 | - | 4,917 | - | 0.000325 | 🔵 low — common in general English | — |
| 5284 | **adulterer** | 1 | 1 | - | 166.19 | - | 4,918 | - | 0.000325 | 🔵 low — common in general English | — |
| 5285 | **infidelity** | 1 | 1 | - | 166.19 | - | 4,919 | - | 0.000325 | 🔵 low — common in general English | — |
| 5286 | **lunch-hour** | 1 | 1 | - | 166.19 | - | 4,920 | - | 0.000325 | 🔵 low — common in general English | — |
| 5287 | **obdurate** | 1 | 1 | - | 166.19 | - | 4,921 | - | 0.000325 | 🔵 low — common in general English | — |
| 5288 | **impulsively** | 1 | 1 | - | 166.19 | - | 4,922 | - | 0.000325 | 🔵 low — common in general English | — |
| 5289 | **exhausted-only** | 1 | 1 | - | 166.19 | - | 4,923 | - | 0.000325 | 🔵 low — common in general English | — |
| 5290 | **stony** | 1 | 1 | - | 166.19 | - | 4,924 | - | 0.000325 | 🔵 low — common in general English | — |
| 5291 | **sroi** | 1 | 1 | - | 166.19 | - | 4,926 | - | 0.000325 | 🔵 low — common in general English | — |
| 5292 | **sombre** | 1 | 1 | - | 166.19 | - | 4,927 | - | 0.000325 | 🔵 low — common in general English | — |
| 5293 | **horse-hair** | 1 | 1 | - | 166.19 | - | 4,928 | - | 0.000325 | 🔵 low — common in general English | — |
| 5294 | **if-finally-enough** | 1 | 1 | - | 166.19 | - | 4,929 | - | 0.000325 | 🔵 low — common in general English | — |
| 5295 | **grass-like** | 1 | 1 | - | 166.19 | - | 4,930 | - | 0.000325 | 🔵 low — common in general English | — |
| 5296 | **devouring** | 1 | 1 | - | 166.19 | - | 4,931 | - | 0.000325 | 🔵 low — common in general English | — |
| 5297 | **exquisitely** | 1 | 1 | - | 166.19 | - | 4,932 | - | 0.000325 | 🔵 low — common in general English | — |
| 5298 | **bedecked** | 1 | 1 | - | 166.19 | - | 4,933 | - | 0.000325 | 🔵 low — common in general English | — |
| 5299 | **ravishing** | 1 | 1 | - | 166.19 | - | 4,934 | - | 0.000325 | 🔵 low — common in general English | — |
| 5300 | **srol** | 1 | 1 | - | 166.19 | - | 4,935 | - | 0.000325 | 🔵 low — common in general English | — |
| 5301 | **daughter-in** | 1 | 1 | - | 166.19 | - | 4,936 | - | 0.000325 | 🔵 low — common in general English | — |
| 5302 | **shaven-skulled** | 1 | 1 | - | 166.19 | - | 4,937 | - | 0.000325 | 🔵 low — common in general English | — |
| 5303 | **proposition** | 1 | 1 | - | 166.19 | - | 4,938 | - | 0.000324 | 🔵 low — common in general English | — |
| 5304 | **bald-head** | 1 | 1 | - | 166.19 | - | 4,939 | - | 0.000324 | 🔵 low — common in general English | — |
| 5305 | **ablution** | 1 | 1 | - | 166.19 | - | 4,940 | - | 0.000324 | 🔵 low — common in general English | — |
| 5306 | **squashed** | 1 | 1 | - | 166.19 | - | 4,941 | - | 0.000324 | 🔵 low — common in general English | — |
| 5307 | **jostling** | 1 | 1 | - | 166.19 | - | 4,942 | - | 0.000324 | 🔵 low — common in general English | — |
| 5308 | **thing-except** | 1 | 1 | - | 166.19 | - | 4,943 | - | 0.000324 | 🔵 low — common in general English | — |
| 5309 | **shindre** | 1 | 1 | - | 166.19 | - | 4,944 | - | 0.000324 | 🔵 low — common in general English | — |
| 5310 | **jungpo** | 1 | 1 | - | 166.19 | - | 4,945 | - | 0.000324 | 🔵 low — common in general English | ✓ འབྱུང་པོ |
| 5311 | **theurang** | 1 | 1 | - | 166.19 | - | 4,946 | - | 0.000324 | 🔵 low — common in general English | ✓ ཐེའུ་རང |
| 5312 | **relive** | 1 | 1 | - | 166.19 | - | 4,947 | - | 0.000324 | 🔵 low — common in general English | — |
| 5313 | **insanity** | 1 | 1 | - | 166.19 | - | 4,948 | - | 0.000324 | 🔵 low — common in general English | — |
| 5314 | **teem** | 1 | 1 | - | 166.19 | - | 4,949 | - | 0.000324 | 🔵 low — common in general English | — |
| 5315 | **reptile** | 1 | 1 | - | 166.19 | - | 4,950 | - | 0.000324 | 🔵 low — common in general English | — |
| 5316 | **shellfish** | 1 | 1 | - | 166.19 | - | 4,951 | - | 0.000324 | 🔵 low — common in general English | — |
| 5317 | **beer-barrel** | 1 | 1 | - | 166.19 | - | 4,952 | - | 0.000324 | 🔵 low — common in general English | — |
| 5318 | **burrow** | 1 | 1 | - | 166.19 | - | 4,953 | - | 0.000324 | 🔵 low — common in general English | — |
| 5319 | **torturing** | 1 | 1 | - | 166.19 | - | 4,954 | - | 0.000324 | 🔵 low — common in general English | — |
| 5320 | **devices-net** | 1 | 1 | - | 166.19 | - | 4,955 | - | 0.000324 | 🔵 low — common in general English | — |
| 5321 | **oyster** | 1 | 1 | - | 166.19 | - | 4,956 | - | 0.000324 | 🔵 low — common in general English | — |
| 5322 | **ass** | 1 | 1 | - | 166.19 | - | 4,957 | - | 0.000324 | 🔵 low — common in general English | — |
| 5323 | **domesticated** | 1 | 1 | - | 166.19 | - | 4,958 | - | 0.000324 | 🔵 low — common in general English | — |
| 5324 | **executioner** | 1 | 1 | - | 166.19 | - | 4,959 | - | 0.000324 | 🔵 low — common in general English | — |
| 5325 | **stare** | 1 | 1 | - | 166.19 | - | 4,960 | - | 0.000324 | 🔵 low — common in general English | — |
| 5326 | **pierced** | 1 | 1 | - | 166.19 | - | 4,961 | - | 0.000324 | 🔵 low — common in general English | — |
| 5327 | **yoked** | 1 | 1 | - | 166.19 | - | 4,962 | - | 0.000324 | 🔵 low — common in general English | — |
| 5328 | **continual** | 1 | 1 | - | 166.19 | - | 4,963 | - | 0.000323 | 🔵 low — common in general English | — |
| 5329 | **pelted** | 1 | 1 | - | 166.19 | - | 4,964 | - | 0.000323 | 🔵 low — common in general English | — |
| 5330 | **long-lasting** | 1 | 1 | - | 166.19 | - | 4,965 | - | 0.000323 | 🔵 low — common in general English | — |
| 5331 | **lated** | 1 | 1 | - | 166.19 | - | 4,966 | - | 0.000323 | 🔵 low — common in general English | — |
| 5332 | **scorning** | 1 | 1 | - | 166.19 | - | 4,967 | - | 0.000323 | 🔵 low — common in general English | — |
| 5333 | **old-age** | 1 | 1 | - | 166.19 | - | 4,968 | - | 0.000323 | 🔵 low — common in general English | — |
| 5334 | **hated** | 1 | 1 | - | 166.19 | - | 4,969 | - | 0.000323 | 🔵 low — common in general English | — |
| 5335 | **wracked** | 1 | 1 | - | 166.19 | - | 4,970 | - | 0.000323 | 🔵 low — common in general English | — |
| 5336 | **spasm** | 1 | 1 | - | 166.19 | - | 4,971 | - | 0.000323 | 🔵 low — common in general English | — |
| 5337 | **parasite** | 1 | 1 | - | 166.19 | - | 4,972 | - | 0.000323 | 🔵 low — common in general English | — |
| 5338 | **news-and** | 1 | 1 | - | 166.19 | - | 4,973 | - | 0.000323 | 🔵 low — common in general English | — |
| 5339 | **imme** | 1 | 1 | - | 166.19 | - | 4,974 | - | 0.000323 | 🔵 low — common in general English | — |
| 5340 | **diately** | 1 | 1 | - | 166.19 | - | 4,975 | - | 0.000323 | 🔵 low — common in general English | — |
| 5341 | **constancy** | 1 | 1 | - | 166.19 | - | 4,976 | - | 0.000323 | 🔵 low — common in general English | — |
| 5342 | **celebration** | 1 | 1 | - | 166.19 | - | 4,977 | - | 0.000323 | 🔵 low — common in general English | — |
| 5343 | **concoction** | 1 | 1 | - | 166.19 | - | 4,978 | - | 0.000323 | 🔵 low — common in general English | — |
| 5344 | **six-brick** | 1 | 1 | - | 166.19 | - | 4,979 | - | 0.000323 | 🔵 low — common in general English | — |
| 5345 | **dotok** | 1 | 1 | - | 166.19 | - | 4,980 | - | 0.000323 | 🔵 low — common in general English | — |
| 5346 | **dzo** | 1 | 1 | - | 166.19 | - | 4,981 | - | 0.000323 | 🔵 low — common in general English | — |
| 5347 | **perforated** | 1 | 1 | - | 166.19 | - | 4,982 | - | 0.000323 | 🔵 low — common in general English | — |
| 5348 | **chafed** | 1 | 1 | - | 166.19 | - | 4,983 | - | 0.000323 | 🔵 low — common in general English | — |
| 5349 | **lambskin** | 1 | 1 | - | 166.19 | - | 4,984 | - | 0.000323 | 🔵 low — common in general English | — |
| 5350 | **flea** | 1 | 1 | - | 166.19 | - | 4,985 | - | 0.000323 | 🔵 low — common in general English | — |
| 5351 | **tick** | 1 | 1 | - | 166.19 | - | 4,986 | - | 0.000323 | 🔵 low — common in general English | — |
| 5352 | **decapitated** | 1 | 1 | - | 166.19 | - | 4,987 | - | 0.000323 | 🔵 low — common in general English | — |
| 5353 | **die-they** | 1 | 1 | - | 166.19 | - | 4,988 | - | 0.000322 | 🔵 low — common in general English | — |
| 5354 | **incessantly** | 1 | 1 | - | 166.19 | - | 4,989 | - | 0.000322 | 🔵 low — common in general English | — |
| 5355 | **aquatic** | 1 | 1 | - | 166.19 | - | 4,990 | - | 0.000322 | 🔵 low — common in general English | — |
| 5356 | **threshing** | 1 | 1 | - | 166.19 | - | 4,991 | - | 0.000322 | 🔵 low — common in general English | — |
| 5357 | **untainted** | 1 | 1 | - | 166.19 | - | 4,992 | - | 0.000322 | 🔵 low — common in general English | ~ |
| 5358 | **suckle** | 1 | 1 | - | 166.19 | - | 4,993 | - | 0.000322 | 🔵 low — common in general English | — |
| 5359 | **tethered** | 1 | 1 | - | 166.19 | - | 4,994 | - | 0.000322 | 🔵 low — common in general English | — |
| 5360 | **paus** | 1 | 1 | - | 166.19 | - | 4,995 | - | 0.000322 | 🔵 low — common in general English | — |
| 5361 | **milk-their** | 1 | 1 | - | 166.19 | - | 4,996 | - | 0.000322 | 🔵 low — common in general English | — |
| 5362 | **drink-can** | 1 | 1 | - | 166.19 | - | 4,997 | - | 0.000322 | 🔵 low — common in general English | — |
| 5363 | **starved** | 1 | 1 | - | 166.19 | - | 4,998 | - | 0.000322 | 🔵 low — common in general English | — |
| 5364 | **skeleton-like** | 1 | 1 | - | 166.19 | - | 4,999 | - | 0.000322 | 🔵 low — common in general English | — |
| 5365 | **stagger** | 1 | 1 | - | 166.19 | - | 5,000 | - | 0.000322 | 🔵 low — common in general English | — |
| 5366 | **constituting** | 1 | 1 | - | 166.19 | - | 5,001 | - | 0.000322 | 🔵 low — common in general English | — |
| 5367 | **happiness-food** | 1 | 1 | - | 166.19 | - | 5,002 | - | 0.000322 | 🔵 low — common in general English | — |
| 5368 | **of-are** | 1 | 1 | - | 166.19 | - | 5,003 | - | 0.000322 | 🔵 low — common in general English | — |
| 5369 | **interpose** | 1 | 1 | - | 166.19 | - | 5,004 | - | 0.000322 | 🔵 low — common in general English | — |
| 5370 | **embryonic** | 1 | 1 | - | 166.19 | - | 5,005 | - | 0.000322 | 🔵 low — common in general English | — |
| 5371 | **jelly** | 1 | 1 | - | 166.19 | - | 5,006 | - | 0.000322 | 🔵 low — common in general English | — |
| 5372 | **viscous** | 1 | 1 | - | 166.19 | - | 5,007 | - | 0.000322 | 🔵 low — common in general English | — |
| 5373 | **ellipse** | 1 | 1 | - | 166.19 | - | 5,008 | - | 0.000322 | 🔵 low — common in general English | — |
| 5374 | **oblong** | 1 | 1 | - | 166.19 | - | 5,009 | - | 0.000322 | 🔵 low — common in general English | — |
| 5375 | **oval** | 1 | 1 | - | 166.19 | - | 5,010 | - | 0.000322 | 🔵 low — common in general English | — |
| 5376 | **appendage** | 1 | 1 | - | 166.19 | - | 5,011 | - | 0.000322 | 🔵 low — common in general English | — |
| 5377 | **sense-organ** | 1 | 1 | - | 166.19 | - | 5,012 | - | 0.000322 | 🔵 low — common in general English | — |
| 5378 | **suffocating** | 1 | 1 | - | 166.19 | - | 5,013 | - | 0.000322 | 🔵 low — common in general English | — |
| 5379 | **uterus** | 1 | 1 | - | 166.19 | - | 5,014 | - | 0.000321 | 🔵 low — common in general English | — |
| 5380 | **buffeted** | 1 | 1 | - | 166.19 | - | 5,015 | - | 0.000321 | 🔵 low — common in general English | — |
| 5381 | **cervix** | 1 | 1 | - | 166.19 | - | 5,016 | - | 0.000321 | 🔵 low — common in general English | — |
| 5382 | **pelvi** | 1 | 1 | - | 166.19 | - | 5,017 | - | 0.000321 | 🔵 low — common in general English | — |
| 5383 | **draw-plate** | 1 | 1 | - | 166.19 | - | 5,018 | - | 0.000321 | 🔵 low — common in general English | — |
| 5384 | **wrenched** | 1 | 1 | - | 166.19 | - | 5,019 | - | 0.000321 | 🔵 low — common in general English | — |
| 5385 | **ever-unfinished** | 1 | 1 | - | 166.19 | - | 5,020 | - | 0.000321 | 🔵 low — common in general English | — |
| 5386 | **eyesight** | 1 | 1 | - | 166.19 | - | 5,021 | - | 0.000321 | 🔵 low — common in general English | — |
| 5387 | **articulate** | 1 | 1 | - | 166.19 | - | 5,022 | - | 0.000321 | 🔵 low — common in general English | — |
| 5388 | **unintelligible** | 1 | 1 | - | 166.19 | - | 5,023 | - | 0.000321 | 🔵 low — common in general English | — |
| 5389 | **mumble** | 1 | 1 | - | 166.19 | - | 5,024 | - | 0.000321 | 🔵 low — common in general English | — |
| 5390 | **impa** | 1 | 1 | - | 166.19 | - | 5,025 | - | 0.000321 | 🔵 low — common in general English | — |
| 5391 | **tient** | 1 | 1 | - | 166.19 | - | 5,026 | - | 0.000321 | 🔵 low — common in general English | — |
| 5392 | **scorned** | 1 | 1 | - | 166.19 | - | 5,027 | - | 0.000321 | 🔵 low — common in general English | — |
| 5393 | **shrunk** | 1 | 1 | - | 166.19 | - | 5,028 | - | 0.000321 | 🔵 low — common in general English | — |
| 5394 | **dazed** | 1 | 1 | - | 166.19 | - | 5,029 | - | 0.000321 | 🔵 low — common in general English | — |
| 5395 | **trampled** | 1 | 1 | - | 166.19 | - | 5,030 | - | 0.000321 | 🔵 low — common in general English | — |
| 5396 | **waist** | 1 | 1 | - | 166.19 | - | 5,031 | - | 0.000321 | 🔵 low — common in general English | — |
| 5397 | **gingerly** | 1 | 1 | - | 166.19 | - | 5,032 | - | 0.000321 | 🔵 low — common in general English | — |
| 5398 | **arthritic** | 1 | 1 | - | 166.19 | - | 5,033 | - | 0.000321 | 🔵 low — common in general English | — |
| 5399 | **cheek-bone** | 1 | 1 | - | 166.19 | - | 5,034 | - | 0.000321 | 🔵 low — common in general English | — |
| 5400 | **dull-witted** | 1 | 1 | - | 166.19 | - | 5,035 | - | 0.000321 | 🔵 low — common in general English | — |
| 5401 | **giddy** | 1 | 1 | - | 166.19 | - | 5,036 | - | 0.000321 | 🔵 low — common in general English | — |
| 5402 | **brightness** | 1 | 1 | - | 166.19 | - | 5,037 | - | 0.000321 | 🔵 low — common in general English | — |
| 5403 | **humour** | 1 | 1 | - | 166.19 | - | 5,038 | - | 0.000321 | 🔵 low — common in general English | — |
| 5404 | **illnesses-those** | 1 | 1 | - | 166.19 | - | 5,039 | - | 0.000321 | 🔵 low — common in general English | — |
| 5405 | **bile** | 1 | 1 | - | 166.19 | - | 5,040 | - | 0.000320 | 🔵 low — common in general English | ✓ མཁྲིས་པ |
| 5406 | **on-arise** | 1 | 1 | - | 166.19 | - | 5,041 | - | 0.000320 | 🔵 low — common in general English | — |
| 5407 | **twinge** | 1 | 1 | - | 166.19 | - | 5,042 | - | 0.000320 | 🔵 low — common in general English | — |
| 5408 | **strike-however** | 1 | 1 | - | 166.19 | - | 5,043 | - | 0.000320 | 🔵 low — common in general English | — |
| 5409 | **radiantly** | 1 | 1 | - | 166.19 | - | 5,044 | - | 0.000320 | 🔵 low — common in general English | — |
| 5410 | **prime-we** | 1 | 1 | - | 166.19 | - | 5,045 | - | 0.000320 | 🔵 low — common in general English | — |
| 5411 | **crumple** | 1 | 1 | - | 166.19 | - | 5,046 | - | 0.000320 | 🔵 low — common in general English | — |
| 5412 | **bloodletting** | 1 | 1 | - | 166.19 | - | 5,047 | - | 0.000320 | 🔵 low — common in general English | — |
| 5413 | **cautery** | 1 | 1 | - | 166.19 | - | 5,048 | - | 0.000320 | 🔵 low — common in general English | — |
| 5414 | **morbid** | 1 | 1 | - | 166.19 | - | 5,049 | - | 0.000320 | 🔵 low — common in general English | — |
| 5415 | **epilepsy** | 1 | 1 | - | 166.19 | - | 5,050 | - | 0.000320 | 🔵 low — common in general English | — |
| 5416 | **short-tempered** | 1 | 1 | - | 166.19 | - | 5,051 | - | 0.000320 | 🔵 low — common in general English | — |
| 5417 | **foreboding** | 1 | 1 | - | 166.19 | - | 5,052 | - | 0.000320 | 🔵 low — common in general English | — |
| 5418 | **departure-you** | 1 | 1 | - | 166.19 | - | 5,053 | - | 0.000320 | 🔵 low — common in general English | — |
| 5419 | **menacing** | 1 | 1 | - | 166.19 | - | 5,054 | - | 0.000320 | 🔵 low — common in general English | — |
| 5420 | **hoarse** | 1 | 1 | - | 166.19 | - | 5,055 | - | 0.000320 | 🔵 low — common in general English | — |
| 5421 | **brigand** | 1 | 1 | - | 166.19 | - | 5,056 | - | 0.000320 | 🔵 low — common in general English | — |
| 5422 | **envied** | 1 | 1 | - | 166.19 | - | 5,057 | - | 0.000320 | 🔵 low — common in general English | — |
| 5423 | **devil** | 1 | 1 | - | 166.19 | - | 5,058 | - | 0.000320 | 🔵 low — common in general English | — |
| 5424 | **adage** | 1 | 1 | - | 166.19 | - | 5,059 | - | 0.000320 | 🔵 low — common in general English | — |
| 5425 | **compatriot** | 1 | 1 | - | 166.19 | - | 5,060 | - | 0.000320 | 🔵 low — common in general English | — |
| 5426 | **dangers-and** | 1 | 1 | - | 166.19 | - | 5,061 | - | 0.000320 | 🔵 low — common in general English | — |
| 5427 | **inescapably** | 1 | 1 | - | 166.19 | - | 5,062 | - | 0.000320 | 🔵 low — common in general English | — |
| 5428 | **through-but** | 1 | 1 | - | 166.19 | - | 5,063 | - | 0.000320 | 🔵 low — common in general English | — |
| 5429 | **wheedle** | 1 | 1 | - | 166.19 | - | 5,064 | - | 0.000320 | 🔵 low — common in general English | — |
| 5430 | **gods-a** | 1 | 1 | - | 166.19 | - | 5,065 | - | 0.000320 | 🔵 low — common in general English | — |
| 5431 | **malice** | 1 | 1 | - | 166.19 | - | 5,066 | - | 0.000319 | 🔵 low — common in general English | — |
| 5432 | **deign** | 1 | 1 | - | 166.19 | - | 5,067 | - | 0.000319 | 🔵 low — common in general English | — |
| 5433 | **swindler** | 1 | 1 | - | 166.19 | - | 5,068 | - | 0.000319 | 🔵 low — common in general English | — |
| 5434 | **tether** | 1 | 1 | - | 166.19 | - | 5,069 | - | 0.000319 | 🔵 low — common in general English | — |
| 5435 | **imperiously** | 1 | 1 | - | 166.19 | - | 5,070 | - | 0.000319 | 🔵 low — common in general English | — |
| 5436 | **monopolizing** | 1 | 1 | - | 166.19 | - | 5,071 | - | 0.000319 | 🔵 low — common in general English | — |
| 5437 | **sly** | 1 | 1 | - | 166.19 | - | 5,072 | - | 0.000319 | 🔵 low — common in general English | — |
| 5438 | **ravaging** | 1 | 1 | - | 166.19 | - | 5,073 | - | 0.000319 | 🔵 low — common in general English | — |
| 5439 | **incurable** | 1 | 1 | - | 166.19 | - | 5,074 | - | 0.000319 | 🔵 low — common in general English | — |
| 5440 | **lllead** | 1 | 1 | - | 166.19 | - | 5,075 | - | 0.000319 | 🔵 low — common in general English | — |
| 5441 | **dining** | 1 | 1 | - | 166.19 | - | 5,076 | - | 0.000319 | 🔵 low — common in general English | — |
| 5442 | **expend** | 1 | 1 | - | 166.19 | - | 5,077 | - | 0.000319 | 🔵 low — common in general English | — |
| 5443 | **enterpris** | 1 | 1 | - | 166.19 | - | 5,078 | - | 0.000319 | 🔵 low — common in general English | — |
| 5444 | **accomplished-and** | 1 | 1 | - | 166.19 | - | 5,079 | - | 0.000319 | 🔵 low — common in general English | — |
| 5445 | **dharmaless** | 1 | 1 | - | 166.19 | - | 5,080 | - | 0.000319 | 🔵 low — common in general English | — |
| 5446 | **whence** | 1 | 1 | - | 166.19 | - | 5,081 | - | 0.000319 | 🔵 low — common in general English | — |
| 5447 | **aren** | 1 | 1 | - | 166.19 | - | 5,082 | - | 0.000319 | 🔵 low — common in general English | — |
| 5448 | **nowa** | 1 | 1 | - | 166.19 | - | 5,083 | - | 0.000319 | 🔵 low — common in general English | — |
| 5449 | **decaying** | 1 | 1 | - | 166.19 | - | 5,084 | - | 0.000319 | 🔵 low — common in general English | — |
| 5450 | **everything-good** | 1 | 1 | - | 166.19 | - | 5,085 | - | 0.000319 | 🔵 low — common in general English | — |
| 5451 | **not-highly** | 1 | 1 | - | 166.19 | - | 5,086 | - | 0.000319 | 🔵 low — common in general English | — |
| 5452 | **appalled** | 1 | 1 | - | 166.19 | - | 5,087 | - | 0.000319 | 🔵 low — common in general English | — |
| 5453 | **pitiful** | 1 | 1 | - | 166.19 | - | 5,088 | - | 0.000319 | 🔵 low — common in general English | — |
| 5454 | **multiplicity** | 1 | 1 | - | 166.19 | - | 5,089 | - | 0.000319 | 🔵 low — common in general English | — |
| 5455 | **quarrelling** | 1 | 1 | - | 166.19 | - | 5,090 | - | 0.000319 | 🔵 low — common in general English | — |
| 5456 | **tree-whose** | 1 | 1 | - | 166.19 | - | 5,091 | - | 0.000319 | 🔵 low — common in general English | — |
| 5457 | **donning** | 1 | 1 | - | 166.19 | - | 5,092 | - | 0.000318 | 🔵 low — common in general English | — |
| 5458 | **weapons-vajra** | 1 | 1 | - | 166.19 | - | 5,093 | - | 0.000318 | 🔵 low — common in general English | — |
| 5459 | **taller** | 1 | 1 | - | 166.19 | - | 5,094 | - | 0.000318 | 🔵 low — common in general English | — |
| 5460 | **demi** | 1 | 1 | - | 166.19 | - | 5,095 | - | 0.000318 | 🔵 low — common in general English | — |
| 5461 | **dispatch** | 1 | 1 | - | 166.19 | - | 5,096 | - | 0.000318 | 🔵 low — common in general English | — |
| 5462 | **all-protector** | 1 | 1 | - | 166.19 | - | 5,097 | - | 0.000318 | 🔵 low — common in general English | — |
| 5463 | **crazed** | 1 | 1 | - | 166.19 | - | 5,098 | - | 0.000318 | 🔵 low — common in general English | — |
| 5464 | **fastened** | 1 | 1 | - | 166.19 | - | 5,099 | - | 0.000318 | 🔵 low — common in general English | — |
| 5465 | **exuberant** | 1 | 1 | - | 166.19 | - | 5,100 | - | 0.000318 | 🔵 low — common in general English | ~ |
| 5466 | **wore** | 1 | 1 | - | 166.19 | - | 5,101 | - | 0.000318 | 🔵 low — common in general English | — |
| 5467 | **perspired** | 1 | 1 | - | 166.19 | - | 5,102 | - | 0.000318 | 🔵 low — common in general English | — |
| 5468 | **sweetheart** | 1 | 1 | - | 166.19 | - | 5,103 | - | 0.000318 | 🔵 low — common in general English | — |
| 5469 | **powerlessness** | 1 | 1 | - | 166.19 | - | 5,104 | - | 0.000318 | 🔵 low — common in general English | — |
| 5470 | **birthplace** | 1 | 1 | - | 166.19 | - | 5,105 | - | 0.000318 | 🔵 low — common in general English | — |
| 5471 | **suffering-and** | 1 | 1 | - | 166.19 | - | 5,106 | - | 0.000318 | 🔵 low — common in general English | — |
| 5472 | **murderous** | 1 | 1 | - | 166.19 | - | 5,107 | - | 0.000318 | 🔵 low — common in general English | — |
| 5473 | **hell-fire** | 1 | 1 | - | 166.19 | - | 5,108 | - | 0.000318 | 🔵 low — common in general English | — |
| 5474 | **mindlessness** | 1 | 1 | - | 166.19 | - | 5,109 | - | 0.000318 | 🔵 low — common in general English | — |
| 5475 | **snow-mountain** | 1 | 1 | - | 166.19 | - | 5,110 | - | 0.000318 | 🔵 low — common in general English | — |
| 5476 | **she-monkey** | 1 | 1 | - | 166.19 | - | 5,111 | - | 0.000318 | 🔵 low — common in general English | — |
| 5477 | **pur** | 1 | 1 | - | 166.19 | - | 5,112 | - | 0.000318 | 🔵 low — common in general English | — |
| 5478 | **larika** | 1 | 1 | - | 166.19 | - | 5,113 | - | 0.000318 | 🔵 low — common in general English | — |
| 5479 | **pundarika** | 1 | 1 | - | 166.19 | - | 5,114 | - | 0.000318 | 🔵 low — common in general English | — |
| 5480 | **intimate** | 1 | 1 | - | 166.19 | - | 5,115 | - | 0.000318 | 🔵 low — common in general English | — |
| 5481 | **heartbroken** | 1 | 1 | - | 166.19 | - | 5,116 | - | 0.000318 | 🔵 low — common in general English | — |
| 5482 | **slighdy** | 1 | 1 | - | 166.19 | - | 5,117 | - | 0.000318 | 🔵 low — common in general English | — |
| 5483 | **extolled** | 1 | 1 | - | 166.19 | - | 5,118 | - | 0.000318 | 🔵 low — common in general English | — |
| 5484 | **sense-door** | 1 | 1 | - | 166.19 | - | 5,119 | - | 0.000317 | 🔵 low — common in general English | — |
| 5485 | **frighten** | 1 | 1 | - | 166.19 | - | 5,120 | - | 0.000317 | 🔵 low — common in general English | — |
| 5486 | **saligha** | 1 | 1 | - | 166.19 | - | 5,121 | - | 0.000317 | 🔵 low — common in general English | — |
| 5487 | **assembly-hall** | 1 | 1 | - | 166.19 | - | 5,122 | - | 0.000317 | 🔵 low — common in general English | — |
| 5488 | **balcony** | 1 | 1 | - | 166.19 | - | 5,123 | - | 0.000317 | 🔵 low — common in general English | — |
| 5489 | **overlooking** | 1 | 1 | - | 166.19 | - | 5,124 | - | 0.000317 | 🔵 low — common in general English | — |
| 5490 | **preoccupations-parent** | 1 | 1 | - | 166.19 | - | 5,125 | - | 0.000317 | 🔵 low — common in general English | — |
| 5491 | **possessions-like** | 1 | 1 | - | 166.19 | - | 5,126 | - | 0.000317 | 🔵 low — common in general English | — |
| 5492 | **mist** | 1 | 1 | - | 166.19 | - | 5,127 | - | 0.000317 | 🔵 low — common in general English | — |
| 5493 | **esteem** | 1 | 1 | - | 166.19 | - | 5,128 | - | 0.000317 | 🔵 low — common in general English | — |
| 5494 | **worm-fodder** | 1 | 1 | - | 166.19 | - | 5,129 | - | 0.000317 | 🔵 low — common in general English | — |
| 5495 | **watch-tower** | 1 | 1 | - | 166.19 | - | 5,130 | - | 0.000317 | 🔵 low — common in general English | — |
| 5496 | **gloomy-face** | 1 | 1 | - | 166.19 | - | 5,131 | - | 0.000317 | 🔵 low — common in general English | — |
| 5497 | **cheery** | 1 | 1 | - | 166.19 | - | 5,132 | - | 0.000317 | 🔵 low — common in general English | — |
| 5498 | **all-determining** | 1 | 1 | - | 166.19 | - | 5,133 | - | 0.000317 | 🔵 low — common in general English | — |
| 5499 | **consign** | 1 | 1 | - | 166.19 | - | 5,134 | - | 0.000317 | 🔵 low — common in general English | — |
| 5500 | **do-i** | 1 | 1 | - | 166.19 | - | 5,135 | - | 0.000317 | 🔵 low — common in general English | — |
| 5501 | **underfoot** | 1 | 1 | - | 166.19 | - | 5,136 | - | 0.000317 | 🔵 low — common in general English | — |
| 5502 | **gusto** | 1 | 1 | - | 166.19 | - | 5,137 | - | 0.000317 | 🔵 low — common in general English | — |
| 5503 | **wher** | 1 | 1 | - | 166.19 | - | 5,138 | - | 0.000317 | 🔵 low — common in general English | — |
| 5504 | **tea-party** | 1 | 1 | - | 166.19 | - | 5,139 | - | 0.000317 | 🔵 low — common in general English | — |
| 5505 | **hoove** | 1 | 1 | - | 166.19 | - | 5,140 | - | 0.000317 | 🔵 low — common in general English | — |
| 5506 | **swamped** | 1 | 1 | - | 166.19 | - | 5,141 | - | 0.000317 | 🔵 low — common in general English | — |
| 5507 | **fleece** | 1 | 1 | - | 166.19 | - | 5,142 | - | 0.000317 | 🔵 low — common in general English | — |
| 5508 | **lambing** | 1 | 1 | - | 166.19 | - | 5,143 | - | 0.000317 | 🔵 low — common in general English | — |
| 5509 | **dowry** | 1 | 1 | - | 166.19 | - | 5,144 | - | 0.000317 | 🔵 low — common in general English | — |
| 5510 | **in-law** | 1 | 1 | - | 166.19 | - | 5,145 | - | 0.000317 | 🔵 low — common in general English | — |
| 5511 | **pretentious** | 1 | 1 | - | 166.19 | - | 5,146 | - | 0.000316 | 🔵 low — common in general English | — |
| 5512 | **breast-meat** | 1 | 1 | - | 166.19 | - | 5,147 | - | 0.000316 | 🔵 low — common in general English | — |
| 5513 | **tripe** | 1 | 1 | - | 166.19 | - | 5,148 | - | 0.000316 | 🔵 low — common in general English | — |
| 5514 | **bloody** | 1 | 1 | - | 166.19 | - | 5,149 | - | 0.000316 | 🔵 low — common in general English | — |
| 5515 | **willow-wand** | 1 | 1 | - | 166.19 | - | 5,150 | - | 0.000316 | 🔵 low — common in general English | — |
| 5516 | **indeed-considering** | 1 | 1 | - | 166.19 | - | 5,151 | - | 0.000316 | 🔵 low — common in general English | — |
| 5517 | **mothers-we** | 1 | 1 | - | 166.19 | - | 5,152 | - | 0.000316 | 🔵 low — common in general English | — |
| 5518 | **thereupon** | 1 | 1 | - | 166.19 | - | 5,153 | - | 0.000316 | 🔵 low — common in general English | — |
| 5519 | **sundered** | 1 | 1 | - | 166.19 | - | 5,154 | - | 0.000316 | 🔵 low — common in general English | — |
| 5520 | **involved-a** | 1 | 1 | - | 166.19 | - | 5,155 | - | 0.000316 | 🔵 low — common in general English | — |
| 5521 | **seiz** | 1 | 1 | - | 166.19 | - | 5,156 | - | 0.000316 | 🔵 low — common in general English | — |
| 5522 | **lash** | 1 | 1 | - | 166.19 | - | 5,157 | - | 0.000316 | 🔵 low — common in general English | — |
| 5523 | **thong** | 1 | 1 | - | 166.19 | - | 5,158 | - | 0.000316 | 🔵 low — common in general English | — |
| 5524 | **bluish** | 1 | 1 | - | 166.19 | - | 5,159 | - | 0.000316 | 🔵 low — common in general English | — |
| 5525 | **not-or** | 1 | 1 | - | 166.19 | - | 5,160 | - | 0.000316 | 🔵 low — common in general English | — |
| 5526 | **subterfuge** | 1 | 1 | - | 166.19 | - | 5,161 | - | 0.000316 | 🔵 low — common in general English | — |
| 5527 | **deceiving** | 1 | 1 | - | 166.19 | - | 5,162 | - | 0.000316 | 🔵 low — common in general English | — |
| 5528 | **debilitate** | 1 | 1 | - | 166.19 | - | 5,163 | - | 0.000316 | 🔵 low — common in general English | — |
| 5529 | **poring** | 1 | 1 | - | 166.19 | - | 5,164 | - | 0.000316 | 🔵 low — common in general English | — |
| 5530 | **overpower** | 1 | 1 | - | 166.19 | - | 5,165 | - | 0.000316 | 🔵 low — common in general English | — |
| 5531 | **shoulder-blade** | 1 | 1 | - | 166.19 | - | 5,166 | - | 0.000316 | 🔵 low — common in general English | — |
| 5532 | **daybreak** | 1 | 1 | - | 166.19 | - | 5,167 | - | 0.000316 | 🔵 low — common in general English | — |
| 5533 | **wink** | 1 | 1 | - | 166.19 | - | 5,168 | - | 0.000316 | 🔵 low — common in general English | — |
| 5534 | **torrna-offering** | 1 | 1 | - | 166.19 | - | 5,169 | - | 0.000316 | 🔵 low — common in general English | — |
| 5535 | **carne** | 1 | 1 | - | 166.19 | - | 5,170 | - | 0.000316 | 🔵 low — common in general English | — |
| 5536 | **disdainfully** | 1 | 1 | - | 166.19 | - | 5,171 | - | 0.000316 | 🔵 low — common in general English | — |
| 5537 | **railed** | 1 | 1 | - | 166.19 | - | 5,172 | - | 0.000316 | 🔵 low — common in general English | — |
| 5538 | **dharma-practitioner** | 1 | 1 | - | 166.19 | - | 5,173 | - | 0.000315 | 🔵 low — common in general English | — |
| 5539 | **slander** | 1 | 1 | - | 166.19 | - | 5,174 | - | 0.000315 | 🔵 low — common in general English | — |
| 5540 | **ware** | 1 | 1 | - | 166.19 | - | 5,175 | - | 0.000315 | 🔵 low — common in general English | — |
| 5541 | **extort** | 1 | 1 | - | 166.19 | - | 5,176 | - | 0.000315 | 🔵 low — common in general English | — |
| 5542 | **haggling** | 1 | 1 | - | 166.19 | - | 5,177 | - | 0.000315 | 🔵 low — common in general English | — |
| 5543 | **covet** | 1 | 1 | - | 166.19 | - | 5,178 | - | 0.000315 | 🔵 low — common in general English | — |
| 5544 | **vaisravana** | 1 | 1 | - | 166.19 | - | 5,179 | - | 0.000315 | 🔵 low — common in general English | — |
| 5545 | **nefarious** | 1 | 1 | - | 166.19 | - | 5,180 | - | 0.000315 | 🔵 low — common in general English | — |
| 5546 | **corrupting** | 1 | 1 | - | 166.19 | - | 5,181 | - | 0.000315 | 🔵 low — common in general English | — |
| 5547 | **awl** | 1 | 1 | - | 166.19 | - | 5,182 | - | 0.000315 | 🔵 low — common in general English | — |
| 5548 | **laity** | 1 | 1 | - | 166.19 | - | 5,183 | - | 0.000315 | 🔵 low — common in general English | — |
| 5549 | **gravest** | 1 | 1 | - | 166.19 | - | 5,184 | - | 0.000315 | 🔵 low — common in general English | — |
| 5550 | **particu** | 1 | 1 | - | 166.19 | - | 5,185 | - | 0.000315 | 🔵 low — common in general English | — |
| 5551 | **lar** | 1 | 1 | - | 166.19 | - | 5,186 | - | 0.000315 | 🔵 low — common in general English | — |
| 5552 | **masturbation** | 1 | 1 | - | 166.19 | - | 5,187 | - | 0.000315 | 🔵 low — common in general English | — |
| 5553 | **bereavement** | 1 | 1 | - | 166.19 | - | 5,188 | - | 0.000315 | 🔵 low — common in general English | — |
| 5554 | **menstruation** | 1 | 1 | - | 166.19 | - | 5,189 | - | 0.000315 | 🔵 low — common in general English | — |
| 5555 | **recov** | 1 | 1 | - | 166.19 | - | 5,190 | - | 0.000315 | 🔵 low — common in general English | — |
| 5556 | **ery** | 1 | 1 | - | 166.19 | - | 5,191 | - | 0.000315 | 🔵 low — common in general English | — |
| 5557 | **child-birth** | 1 | 1 | - | 166.19 | - | 5,192 | - | 0.000315 | 🔵 low — common in general English | — |
| 5558 | **prepubescent** | 1 | 1 | - | 166.19 | - | 5,193 | - | 0.000315 | 🔵 low — common in general English | — |
| 5559 | **devastatingly** | 1 | 1 | - | 166.19 | - | 5,194 | - | 0.000315 | 🔵 low — common in general English | — |
| 5560 | **imposter** | 1 | 1 | - | 166.19 | - | 5,195 | - | 0.000315 | 🔵 low — common in general English | — |
| 5561 | **thanksgiving** | 1 | 1 | - | 166.19 | - | 5,196 | - | 0.000315 | 🔵 low — common in general English | — |
| 5562 | **chastised** | 1 | 1 | - | 166.19 | - | 5,197 | - | 0.000315 | 🔵 low — common in general English | — |
| 5563 | **concept-bound** | 1 | 1 | - | 166.19 | - | 5,198 | - | 0.000315 | 🔵 low — common in general English | — |
| 5564 | **second-and** | 1 | 1 | - | 166.19 | - | 5,199 | - | 0.000315 | 🔵 low — common in general English | — |
| 5565 | **sweetly** | 1 | 1 | - | 166.19 | - | 5,201 | - | 0.000314 | 🔵 low — common in general English | — |
| 5566 | **not-such** | 1 | 1 | - | 166.19 | - | 5,202 | - | 0.000314 | 🔵 low — common in general English | — |
| 5567 | **aimlessly** | 1 | 1 | - | 166.19 | - | 5,203 | - | 0.000314 | 🔵 low — common in general English | — |
| 5568 | **libidinous** | 1 | 1 | - | 166.19 | - | 5,204 | - | 0.000314 | 🔵 low — common in general English | — |
| 5569 | **cussing** | 1 | 1 | - | 166.19 | - | 5,205 | - | 0.000314 | 🔵 low — common in general English | — |
| 5570 | **disturb** | 1 | 1 | - | 166.19 | - | 5,206 | - | 0.000314 | 🔵 low — common in general English | — |
| 5571 | **gossip-monger** | 1 | 1 | - | 166.19 | - | 5,207 | - | 0.000314 | 🔵 low — common in general English | — |
| 5572 | **rituals-just** | 1 | 1 | - | 166.19 | - | 5,208 | - | 0.000314 | 🔵 low — common in general English | — |
| 5573 | **perfunctorily** | 1 | 1 | - | 166.19 | - | 5,209 | - | 0.000314 | 🔵 low — common in general English | — |
| 5574 | **sorcerers-i** | 1 | 1 | - | 166.19 | - | 5,210 | - | 0.000314 | 🔵 low — common in general English | — |
| 5575 | **cast-iron** | 1 | 1 | - | 166.19 | - | 5,211 | - | 0.000314 | 🔵 low — common in general English | — |
| 5576 | **lethally** | 1 | 1 | - | 166.19 | - | 5,212 | - | 0.000314 | 🔵 low — common in general English | — |
| 5577 | **life-artery** | 1 | 1 | - | 166.19 | - | 5,213 | - | 0.000314 | 🔵 low — common in general English | — |
| 5578 | **desirous** | 1 | 1 | - | 166.19 | - | 5,214 | - | 0.000314 | 🔵 low — common in general English | — |
| 5579 | **acquisitive** | 1 | 1 | - | 166.19 | - | 5,215 | - | 0.000314 | 🔵 low — common in general English | — |
| 5580 | **contemplat** | 1 | 1 | - | 166.19 | - | 5,216 | - | 0.000314 | 🔵 low — common in general English | — |
| 5581 | **agreeable** | 1 | 1 | - | 166.19 | - | 5,217 | - | 0.000314 | 🔵 low — common in general English | — |
| 5582 | **invent** | 1 | 1 | - | 166.19 | - | 5,218 | - | 0.000314 | 🔵 low — common in general English | — |
| 5583 | **malicious** | 1 | 1 | - | 166.19 | - | 5,219 | - | 0.000314 | 🔵 low — common in general English | — |
| 5584 | **catego** | 1 | 1 | - | 166.19 | - | 5,220 | - | 0.000314 | 🔵 low — common in general English | — |
| 5585 | **ry** | 1 | 1 | - | 166.19 | - | 5,221 | - | 0.000314 | 🔵 low — common in general English | ~ |
| 5586 | **eternally** | 1 | 1 | - | 166.19 | - | 5,222 | - | 0.000314 | 🔵 low — common in general English | — |
| 5587 | **roundness** | 1 | 1 | - | 166.19 | - | 5,223 | - | 0.000314 | 🔵 low — common in general English | — |
| 5588 | **iridescent** | 1 | 1 | - | 166.19 | - | 5,224 | - | 0.000314 | 🔵 low — common in general English | — |
| 5589 | **sharpened** | 1 | 1 | - | 166.19 | - | 5,225 | - | 0.000314 | 🔵 low — common in general English | — |
| 5590 | **bad-all** | 1 | 1 | - | 166.19 | - | 5,226 | - | 0.000314 | 🔵 low — common in general English | — |
| 5591 | **spontane** | 1 | 1 | - | 166.19 | - | 5,227 | - | 0.000314 | 🔵 low — common in general English | — |
| 5592 | **ously** | 1 | 1 | - | 166.19 | - | 5,228 | - | 0.000314 | 🔵 low — common in general English | — |
| 5593 | **unvirtuous** | 1 | 1 | - | 166.19 | - | 5,229 | - | 0.000313 | 🔵 low — common in general English | — |
| 5594 | **mistakenly** | 1 | 1 | - | 166.19 | - | 5,230 | - | 0.000313 | 🔵 low — common in general English | — |
| 5595 | **meri** | 1 | 1 | - | 166.19 | - | 5,231 | - | 0.000313 | 🔵 low — common in general English | — |
| 5596 | **torious** | 1 | 1 | - | 166.19 | - | 5,232 | - | 0.000313 | 🔵 low — common in general English | — |
| 5597 | **resuscitate** | 1 | 1 | - | 166.19 | - | 5,233 | - | 0.000313 | 🔵 low — common in general English | — |
| 5598 | **negate** | 1 | 1 | - | 166.19 | - | 5,234 | - | 0.000313 | 🔵 low — common in general English | — |
| 5599 | **impulse-extremely** | 1 | 1 | - | 166.19 | - | 5,235 | - | 0.000313 | 🔵 low — common in general English | — |
| 5600 | **ignorance-motivating** | 1 | 1 | - | 166.19 | - | 5,236 | - | 0.000313 | 🔵 low — common in general English | — |
| 5601 | **instinct** | 1 | 1 | - | 166.19 | - | 5,237 | - | 0.000313 | 🔵 low — common in general English | — |
| 5602 | **newborn** | 1 | 1 | - | 166.19 | - | 5,238 | - | 0.000313 | 🔵 low — common in general English | — |
| 5603 | **adulthood** | 1 | 1 | - | 166.19 | - | 5,239 | - | 0.000313 | 🔵 low — common in general English | — |
| 5604 | **assaulted** | 1 | 1 | - | 166.19 | - | 5,240 | - | 0.000313 | 🔵 low — common in general English | — |
| 5605 | **pillage** | 1 | 1 | - | 166.19 | - | 5,241 | - | 0.000313 | 🔵 low — common in general English | — |
| 5606 | **bandit** | 1 | 1 | - | 166.19 | - | 5,242 | - | 0.000313 | 🔵 low — common in general English | — |
| 5607 | **raids-often** | 1 | 1 | - | 166.19 | - | 5,243 | - | 0.000313 | 🔵 low — common in general English | — |
| 5608 | **life-or** | 1 | 1 | - | 166.19 | - | 5,244 | - | 0.000313 | 🔵 low — common in general English | — |
| 5609 | **bereft** | 1 | 1 | - | 166.19 | - | 5,245 | - | 0.000313 | 🔵 low — common in general English | — |
| 5610 | **destitute** | 1 | 1 | - | 166.19 | - | 5,246 | - | 0.000313 | 🔵 low — common in general English | — |
| 5611 | **preta-like** | 1 | 1 | - | 166.19 | - | 5,247 | - | 0.000313 | 🔵 low — common in general English | — |
| 5612 | **indulged** | 1 | 1 | - | 166.19 | - | 5,248 | - | 0.000313 | 🔵 low — common in general English | — |
| 5613 | **hating** | 1 | 1 | - | 166.19 | - | 5,249 | - | 0.000313 | 🔵 low — common in general English | — |
| 5614 | **belittled** | 1 | 1 | - | 166.19 | - | 5,250 | - | 0.000313 | 🔵 low — common in general English | — |
| 5615 | **hurling** | 1 | 1 | - | 166.19 | - | 5,251 | - | 0.000313 | 🔵 low — common in general English | — |
| 5616 | **argumentative** | 1 | 1 | - | 166.19 | - | 5,252 | - | 0.000313 | 🔵 low — common in general English | — |
| 5617 | **defiantly** | 1 | 1 | - | 166.19 | - | 5,253 | - | 0.000313 | 🔵 low — common in general English | — |
| 5618 | **grudgingly** | 1 | 1 | - | 166.19 | - | 5,254 | - | 0.000313 | 🔵 low — common in general English | — |
| 5619 | **recon** | 1 | 1 | - | 166.19 | - | 5,255 | - | 0.000313 | 🔵 low — common in general English | — |
| 5620 | **ciling** | 1 | 1 | - | 166.19 | - | 5,256 | - | 0.000313 | 🔵 low — common in general English | — |
| 5621 | **insulting** | 1 | 1 | - | 166.19 | - | 5,257 | - | 0.000312 | 🔵 low — common in general English | — |
| 5622 | **or-worse** | 1 | 1 | - | 166.19 | - | 5,258 | - | 0.000312 | 🔵 low — common in general English | — |
| 5623 | **still-to** | 1 | 1 | - | 166.19 | - | 5,259 | - | 0.000312 | 🔵 low — common in general English | — |
| 5624 | **kapila** | 1 | 1 | - | 166.19 | - | 5,260 | - | 0.000312 | 🔵 low — common in general English | — |
| 5625 | **horse-head** | 1 | 1 | - | 166.19 | - | 5,261 | - | 0.000312 | 🔵 low — common in general English | — |
| 5626 | **ox-head** | 1 | 1 | - | 166.19 | - | 5,262 | - | 0.000312 | 🔵 low — common in general English | — |
| 5627 | **fish-like** | 1 | 1 | - | 166.19 | - | 5,263 | - | 0.000312 | 🔵 low — common in general English | — |
| 5628 | **extol** | 1 | 1 | - | 166.19 | - | 5,264 | - | 0.000312 | 🔵 low — common in general English | — |
| 5629 | **self-assurance** | 1 | 1 | - | 166.19 | - | 5,265 | - | 0.000312 | 🔵 low — common in general English | — |
| 5630 | **joyless** | 1 | 1 | - | 166.19 | - | 5,266 | - | 0.000312 | 🔵 low — common in general English | — |
| 5631 | **mortally** | 1 | 1 | - | 166.19 | - | 5,267 | - | 0.000312 | 🔵 low — common in general English | — |
| 5632 | **insecu** | 1 | 1 | - | 166.19 | - | 5,268 | - | 0.000312 | 🔵 low — common in general English | — |
| 5633 | **rity** | 1 | 1 | - | 166.19 | - | 5,269 | - | 0.000312 | 🔵 low — common in general English | — |
| 5634 | **inhabit** | 1 | 1 | - | 166.19 | - | 5,270 | - | 0.000312 | 🔵 low — common in general English | — |
| 5635 | **gorge** | 1 | 1 | - | 166.19 | - | 5,271 | - | 0.000312 | 🔵 low — common in general English | — |
| 5636 | **terrain** | 1 | 1 | - | 166.19 | - | 5,272 | - | 0.000312 | 🔵 low — common in general English | — |
| 5637 | **infertile** | 1 | 1 | - | 166.19 | - | 5,273 | - | 0.000312 | 🔵 low — common in general English | — |
| 5638 | **untimely** | 1 | 1 | - | 166.19 | - | 5,274 | - | 0.000312 | 🔵 low — common in general English | — |
| 5639 | **inhospitable** | 1 | 1 | - | 166.19 | - | 5,275 | - | 0.000312 | 🔵 low — common in general English | — |
| 5640 | **example-or** | 1 | 1 | - | 166.19 | - | 5,277 | - | 0.000312 | 🔵 low — common in general English | — |
| 5641 | **animals-i** | 1 | 1 | - | 166.19 | - | 5,278 | - | 0.000312 | 🔵 low — common in general English | — |
| 5642 | **vaisakha** | 1 | 1 | - | 166.19 | - | 5,279 | - | 0.000312 | 🔵 low — common in general English | — |
| 5643 | **reconcile** | 1 | 1 | - | 166.19 | - | 5,280 | - | 0.000312 | 🔵 low — common in general English | — |
| 5644 | **uninterrupted** | 1 | 1 | - | 166.19 | - | 5,281 | - | 0.000312 | 🔵 low — common in general English | — |
| 5645 | **experiences-from** | 1 | 1 | - | 166.19 | - | 5,282 | - | 0.000312 | 🔵 low — common in general English | — |
| 5646 | **hell-arise** | 1 | 1 | - | 166.19 | - | 5,283 | - | 0.000312 | 🔵 low — common in general English | — |
| 5647 | **impel** | 1 | 1 | - | 166.19 | - | 5,284 | - | 0.000312 | 🔵 low — common in general English | — |
| 5648 | **identifiable** | 1 | 1 | - | 166.19 | - | 5,285 | - | 0.000311 | 🔵 low — common in general English | — |
| 5649 | **sravasti** | 1 | 1 | - | 166.19 | - | 5,286 | - | 0.000311 | 🔵 low — common in general English | — |
| 5650 | **pole** | 1 | 1 | - | 166.19 | - | 5,287 | - | 0.000311 | 🔵 low — common in general English | — |
| 5651 | **writhed** | 1 | 1 | - | 166.19 | - | 5,288 | - | 0.000311 | 🔵 low — common in general English | — |
| 5652 | **matropakara** | 1 | 1 | - | 166.19 | - | 5,289 | - | 0.000311 | 🔵 low — common in general English | — |
| 5653 | **tied-up** | 1 | 1 | - | 166.19 | - | 5,290 | - | 0.000311 | 🔵 low — common in general English | — |
| 5654 | **writhing** | 1 | 1 | - | 166.19 | - | 5,291 | - | 0.000311 | 🔵 low — common in general English | — |
| 5655 | **laughed** | 1 | 1 | - | 166.19 | - | 5,292 | - | 0.000311 | 🔵 low — common in general English | — |
| 5656 | **acacia** | 1 | 1 | - | 166.19 | - | 5,293 | - | 0.000311 | 🔵 low — common in general English | — |
| 5657 | **splinter-the** | 1 | 1 | - | 166.19 | - | 5,294 | - | 0.000311 | 🔵 low — common in general English | — |
| 5658 | **parivraji** | 1 | 1 | - | 166.19 | - | 5,295 | - | 0.000311 | 🔵 low — common in general English | — |
| 5659 | **kas** | 1 | 1 | - | 166.19 | - | 5,296 | - | 0.000311 | 🔵 low — common in general English | — |
| 5660 | **succumbed** | 1 | 1 | - | 166.19 | - | 5,297 | - | 0.000311 | 🔵 low — common in general English | — |
| 5661 | **jeta** | 1 | 1 | - | 166.19 | - | 5,298 | - | 0.000311 | 🔵 low — common in general English | — |
| 5662 | **suf** | 1 | 1 | - | 166.19 | - | 5,299 | - | 0.000311 | 🔵 low — common in general English | — |
| 5663 | **fering** | 1 | 1 | - | 166.19 | - | 5,300 | - | 0.000311 | 🔵 low — common in general English | — |
| 5664 | **clairvoyant** | 1 | 1 | - | 166.19 | - | 5,301 | - | 0.000311 | 🔵 low — common in general English | — |
| 5665 | **woodland** | 1 | 1 | - | 166.19 | - | 5,302 | - | 0.000311 | 🔵 low — common in general English | — |
| 5666 | **stoking** | 1 | 1 | - | 166.19 | - | 5,303 | - | 0.000311 | 🔵 low — common in general English | — |
| 5667 | **punish** | 1 | 1 | - | 166.19 | - | 5,304 | - | 0.000311 | 🔵 low — common in general English | — |
| 5668 | **debili** | 1 | 1 | - | 166.19 | - | 5,305 | - | 0.000311 | 🔵 low — common in general English | — |
| 5669 | **tated** | 1 | 1 | - | 166.19 | - | 5,306 | - | 0.000311 | 🔵 low — common in general English | — |
| 5670 | **nagar** | 1 | 1 | - | 166.19 | - | 5,307 | - | 0.000311 | 🔵 low — common in general English | — |
| 5671 | **juna** | 1 | 1 | - | 166.19 | - | 5,308 | - | 0.000311 | 🔵 low — common in general English | — |
| 5672 | **we-whose** | 1 | 1 | - | 166.19 | - | 5,309 | - | 0.000311 | 🔵 low — common in general English | — |
| 5673 | **innumerable-ever** | 1 | 1 | - | 166.19 | - | 5,310 | - | 0.000311 | 🔵 low — common in general English | — |
| 5674 | **underestimate** | 1 | 1 | - | 166.19 | - | 5,311 | - | 0.000311 | 🔵 low — common in general English | — |
| 5675 | **minutest** | 1 | 1 | - | 166.19 | - | 5,312 | - | 0.000311 | 🔵 low — common in general English | — |
| 5676 | **wedding** | 1 | 1 | - | 166.19 | - | 5,313 | - | 0.000311 | 🔵 low — common in general English | — |
| 5677 | **fistful** | 1 | 1 | - | 166.19 | - | 5,314 | - | 0.000310 | 🔵 low — common in general English | — |
| 5678 | **antisarar** | 1 | 1 | - | 166.19 | - | 5,315 | - | 0.000310 | 🔵 low — common in general English | — |
| 5679 | **devo** | 1 | 1 | - | 166.19 | - | 5,316 | - | 0.000310 | 🔵 low — common in general English | — |
| 5680 | **profuse** | 1 | 1 | - | 166.19 | - | 5,317 | - | 0.000310 | 🔵 low — common in general English | — |
| 5681 | **vajrap** | 1 | 1 | - | 166.19 | - | 5,318 | - | 0.000310 | 🔵 low — common in general English | — |
| 5682 | **pirate** | 1 | 1 | - | 166.19 | - | 5,319 | - | 0.000310 | 🔵 low — common in general English | — |
| 5683 | **non-returning** | 1 | 1 | - | 166.19 | - | 5,320 | - | 0.000310 | 🔵 low — common in general English | — |
| 5684 | **hopelessly** | 1 | 1 | - | 166.19 | - | 5,321 | - | 0.000310 | 🔵 low — common in general English | — |
| 5685 | **wrong-doer** | 1 | 1 | - | 166.19 | - | 5,322 | - | 0.000310 | 🔵 low — common in general English | — |
| 5686 | **impression-or** | 1 | 1 | - | 166.19 | - | 5,323 | - | 0.000310 | 🔵 low — common in general English | — |
| 5687 | **generator** | 1 | 1 | - | 166.19 | - | 5,324 | - | 0.000310 | 🔵 low — common in general English | — |
| 5688 | **moti** | 1 | 1 | - | 166.19 | - | 5,325 | - | 0.000310 | 🔵 low — common in general English | — |
| 5689 | **vation** | 1 | 1 | - | 166.19 | - | 5,326 | - | 0.000310 | 🔵 low — common in general English | — |
| 5690 | **neatly** | 1 | 1 | - | 166.19 | - | 5,327 | - | 0.000310 | 🔵 low — common in general English | — |
| 5691 | **kungyal** | 1 | 1 | - | 166.19 | - | 5,328 | - | 0.000310 | 🔵 low — common in general English | — |
| 5692 | **stumbled** | 1 | 1 | - | 166.19 | - | 5,329 | - | 0.000310 | 🔵 low — common in general English | — |
| 5693 | **penyulgyal** | 1 | 1 | - | 166.19 | - | 5,330 | - | 0.000310 | 🔵 low — common in general English | — |
| 5694 | **yoghurt-addict** | 1 | 1 | - | 166.19 | - | 5,331 | - | 0.000310 | 🔵 low — common in general English | — |
| 5695 | **self-centredness** | 1 | 1 | - | 166.19 | - | 5,332 | - | 0.000310 | 🔵 low — common in general English | — |
| 5696 | **expectant** | 1 | 1 | - | 166.19 | - | 5,333 | - | 0.000310 | 🔵 low — common in general English | — |
| 5697 | **ravi** | 1 | 1 | - | 166.19 | - | 5,334 | - | 0.000310 | 🔵 low — common in general English | — |
| 5698 | **cutter** | 1 | 1 | - | 166.19 | - | 5,335 | - | 0.000310 | 🔵 low — common in general English | — |
| 5699 | **tormented-in** | 1 | 1 | - | 166.19 | - | 5,336 | - | 0.000310 | 🔵 low — common in general English | — |
| 5700 | **tormented-by** | 1 | 1 | - | 166.19 | - | 5,337 | - | 0.000310 | 🔵 low — common in general English | — |
| 5701 | **prattling** | 1 | 1 | - | 166.19 | - | 5,338 | - | 0.000310 | 🔵 low — common in general English | — |
| 5702 | **materialism** | 1 | 1 | - | 166.19 | - | 5,339 | - | 0.000310 | 🔵 low — common in general English | — |
| 5703 | **ideology** | 1 | 1 | - | 166.19 | - | 5,340 | - | 0.000310 | 🔵 low — common in general English | — |
| 5704 | **tiness** | 1 | 1 | - | 166.19 | - | 5,341 | - | 0.000310 | 🔵 low — common in general English | — |
| 5705 | **authentically** | 1 | 1 | - | 166.19 | - | 5,342 | - | 0.000310 | 🔵 low — common in general English | — |
| 5706 | **heaping** | 1 | 1 | - | 166.19 | - | 5,343 | - | 0.000309 | 🔵 low — common in general English | — |
| 5707 | **ments-and** | 1 | 1 | - | 166.19 | - | 5,344 | - | 0.000309 | 🔵 low — common in general English | — |
| 5708 | **dhara** | 1 | 1 | - | 166.19 | - | 5,345 | - | 0.000309 | 🔵 low — common in general English | — |
| 5709 | **unreal** | 1 | 1 | - | 166.19 | - | 5,346 | - | 0.000309 | 🔵 low — common in general English | — |
| 5710 | **mingle** | 1 | 1 | - | 166.19 | - | 5,347 | - | 0.000309 | 🔵 low — common in general English | — |
| 5711 | **practices-the** | 1 | 1 | - | 166.19 | - | 5,348 | - | 0.000309 | 🔵 low — common in general English | — |
| 5712 | **formless** | 1 | 1 | - | 166.19 | - | 5,349 | - | 0.000309 | 🔵 low — common in general English | ~ |
| 5713 | **insight-should** | 1 | 1 | - | 166.19 | - | 5,350 | - | 0.000309 | 🔵 low — common in general English | — |
| 5714 | **take-while** | 1 | 1 | - | 166.19 | - | 5,351 | - | 0.000309 | 🔵 low — common in general English | — |
| 5715 | **impregnated** | 1 | 1 | - | 166.19 | - | 5,352 | - | 0.000309 | 🔵 low — common in general English | — |
| 5716 | **moist** | 1 | 1 | - | 166.19 | - | 5,353 | - | 0.000309 | 🔵 low — common in general English | — |
| 5717 | **whomever** | 1 | 1 | - | 166.19 | - | 5,354 | - | 0.000309 | 🔵 low — common in general English | — |
| 5718 | **vow-the** | 1 | 1 | - | 166.19 | - | 5,355 | - | 0.000309 | 🔵 low — common in general English | — |
| 5719 | **knowl** | 1 | 1 | - | 166.19 | - | 5,356 | - | 0.000309 | 🔵 low — common in general English | — |
| 5720 | **practices-out** | 1 | 1 | - | 166.19 | - | 5,357 | - | 0.000309 | 🔵 low — common in general English | — |
| 5721 | **wardly** | 1 | 1 | - | 166.19 | - | 5,358 | - | 0.000309 | 🔵 low — common in general English | — |
| 5722 | **actualized** | 1 | 1 | - | 166.19 | - | 5,359 | - | 0.000309 | 🔵 low — common in general English | — |
| 5723 | **observance** | 1 | 1 | - | 166.19 | - | 5,360 | - | 0.000309 | 🔵 low — common in general English | — |
| 5724 | **unbroken** | 1 | 1 | - | 166.19 | - | 5,361 | - | 0.000309 | 🔵 low — common in general English | — |
| 5725 | **preoc** | 1 | 1 | - | 166.19 | - | 5,362 | - | 0.000309 | 🔵 low — common in general English | — |
| 5726 | **cupation** | 1 | 1 | - | 166.19 | - | 5,363 | - | 0.000309 | 🔵 low — common in general English | — |
| 5727 | **seing** | 1 | 1 | - | 166.19 | - | 5,364 | - | 0.000309 | 🔵 low — common in general English | — |
| 5728 | **resolutely** | 1 | 1 | - | 166.19 | - | 5,365 | - | 0.000309 | 🔵 low — common in general English | — |
| 5729 | **nephew** | 1 | 1 | - | 166.19 | - | 5,366 | - | 0.000309 | 🔵 low — common in general English | — |
| 5730 | **descendant** | 1 | 1 | - | 166.19 | - | 5,367 | - | 0.000309 | 🔵 low — common in general English | — |
| 5731 | **mundane** | 1 | 1 | - | 166.19 | - | 5,368 | - | 0.000309 | 🔵 low — common in general English | — |
| 5732 | **reasons-like** | 1 | 1 | - | 166.19 | - | 5,369 | - | 0.000309 | 🔵 low — common in general English | — |
| 5733 | **priestly** | 1 | 1 | - | 166.19 | - | 5,370 | - | 0.000309 | 🔵 low — common in general English | — |
| 5734 | **suited** | 1 | 1 | - | 166.19 | - | 5,371 | - | 0.000309 | 🔵 low — common in general English | — |
| 5735 | **pedestal** | 1 | 1 | - | 166.19 | - | 5,372 | - | 0.000308 | 🔵 low — common in general English | — |
| 5736 | **visitor** | 1 | 1 | - | 166.19 | - | 5,373 | - | 0.000308 | 🔵 low — common in general English | — |
| 5737 | **fainted** | 1 | 1 | - | 166.19 | - | 5,374 | - | 0.000308 | 🔵 low — common in general English | — |
| 5738 | **ape** | 1 | 1 | - | 166.19 | - | 5,375 | - | 0.000308 | 🔵 low — common in general English | — |
| 5739 | **idiot** | 1 | 1 | - | 166.19 | - | 5,376 | - | 0.000308 | 🔵 low — common in general English | — |
| 5740 | **well-bound** | 1 | 1 | - | 166.19 | - | 5,377 | - | 0.000308 | 🔵 low — common in general English | — |
| 5741 | **leaping** | 1 | 1 | - | 166.19 | - | 5,378 | - | 0.000308 | 🔵 low — common in general English | — |
| 5742 | **venomous** | 1 | 1 | - | 166.19 | - | 5,379 | - | 0.000308 | 🔵 low — common in general English | — |
| 5743 | **coiled** | 1 | 1 | - | 166.19 | - | 5,380 | - | 0.000308 | 🔵 low — common in general English | — |
| 5744 | **beguiled** | 1 | 1 | - | 166.19 | - | 5,381 | - | 0.000308 | 🔵 low — common in general English | — |
| 5745 | **unmistaken** | 1 | 1 | - | 166.19 | - | 5,382 | - | 0.000308 | 🔵 low — common in general English | — |
| 5746 | **uniquely** | 1 | 1 | - | 166.19 | - | 5,383 | - | 0.000308 | 🔵 low — common in general English | — |
| 5747 | **ple** | 1 | 1 | - | 166.19 | - | 5,384 | - | 0.000308 | 🔵 low — common in general English | — |
| 5748 | **expediently** | 1 | 1 | - | 166.19 | - | 5,385 | - | 0.000308 | 🔵 low — common in general English | — |
| 5749 | **noblest** | 1 | 1 | - | 166.19 | - | 5,386 | - | 0.000308 | 🔵 low — common in general English | — |
| 5750 | **unfailingly** | 1 | 1 | - | 166.19 | - | 5,387 | - | 0.000308 | 🔵 low — common in general English | — |
| 5751 | **downpour** | 1 | 1 | - | 166.19 | - | 5,388 | - | 0.000308 | 🔵 low — common in general English | — |
| 5752 | **extinguish** | 1 | 1 | - | 166.19 | - | 5,389 | - | 0.000308 | 🔵 low — common in general English | — |
| 5753 | **agement** | 1 | 1 | - | 166.19 | - | 5,390 | - | 0.000308 | 🔵 low — common in general English | — |
| 5754 | **charting** | 1 | 1 | - | 166.19 | - | 5,391 | - | 0.000308 | 🔵 low — common in general English | — |
| 5755 | **quenching** | 1 | 1 | - | 166.19 | - | 5,392 | - | 0.000308 | 🔵 low — common in general English | — |
| 5756 | **showered** | 1 | 1 | - | 166.19 | - | 5,393 | - | 0.000308 | 🔵 low — common in general English | — |
| 5757 | **wayfarer** | 1 | 1 | - | 166.19 | - | 5,394 | - | 0.000308 | 🔵 low — common in general English | — |
| 5758 | **ferryman** | 1 | 1 | - | 166.19 | - | 5,395 | - | 0.000308 | 🔵 low — common in general English | — |
| 5759 | **stable-minded** | 1 | 1 | - | 166.19 | - | 5,396 | - | 0.000308 | 🔵 low — common in general English | — |
| 5760 | **all-such** | 1 | 1 | - | 166.19 | - | 5,397 | - | 0.000308 | 🔵 low — common in general English | — |
| 5761 | **sittra** | 1 | 1 | - | 166.19 | - | 5,398 | - | 0.000308 | 🔵 low — common in general English | — |
| 5762 | **anged** | 1 | 1 | - | 166.19 | - | 5,399 | - | 0.000308 | 🔵 low — common in general English | — |
| 5763 | **resentful** | 1 | 1 | - | 166.19 | - | 5,400 | - | 0.000308 | 🔵 low — common in general English | — |
| 5764 | **reprimand** | 1 | 1 | - | 166.19 | - | 5,401 | - | 0.000308 | 🔵 low — common in general English | — |
| 5765 | **resent** | 1 | 1 | - | 166.19 | - | 5,402 | - | 0.000307 | 🔵 low — common in general English | — |
| 5766 | **disregarding** | 1 | 1 | - | 166.19 | - | 5,403 | - | 0.000307 | 🔵 low — common in general English | — |
| 5767 | **incomprehensibly** | 1 | 1 | - | 166.19 | - | 5,404 | - | 0.000307 | 🔵 low — common in general English | — |
| 5768 | **ruined** | 1 | 1 | - | 166.19 | - | 5,405 | - | 0.000307 | 🔵 low — common in general English | — |
| 5769 | **tub** | 1 | 1 | - | 166.19 | - | 5,406 | - | 0.000307 | 🔵 low — common in general English | — |
| 5770 | **grilled** | 1 | 1 | - | 166.19 | - | 5,407 | - | 0.000307 | 🔵 low — common in general English | — |
| 5771 | **snapping** | 1 | 1 | - | 166.19 | - | 5,408 | - | 0.000307 | 🔵 low — common in general English | — |
| 5772 | **flawless** | 1 | 1 | - | 166.19 | - | 5,409 | - | 0.000307 | 🔵 low — common in general English | — |
| 5773 | **deceitful** | 1 | 1 | - | 166.19 | - | 5,410 | - | 0.000307 | 🔵 low — common in general English | — |
| 5774 | **glimpsed** | 1 | 1 | - | 166.19 | - | 5,411 | - | 0.000307 | 🔵 low — common in general English | — |
| 5775 | **outburst** | 1 | 1 | - | 166.19 | - | 5,412 | - | 0.000307 | 🔵 low — common in general English | — |
| 5776 | **treading** | 1 | 1 | - | 166.19 | - | 5,413 | - | 0.000307 | 🔵 low — common in general English | — |
| 5777 | **vanity** | 1 | 1 | - | 166.19 | - | 5,414 | - | 0.000307 | 🔵 low — common in general English | — |
| 5778 | **discontent** | 1 | 1 | - | 166.19 | - | 5,415 | - | 0.000307 | 🔵 low — common in general English | — |
| 5779 | **unconsidered** | 1 | 1 | - | 166.19 | - | 5,416 | - | 0.000307 | 🔵 low — common in general English | — |
| 5780 | **insincere** | 1 | 1 | - | 166.19 | - | 5,417 | - | 0.000307 | 🔵 low — common in general English | — |
| 5781 | **laughing** | 1 | 1 | - | 166.19 | - | 5,418 | - | 0.000307 | 🔵 low — common in general English | — |
| 5782 | **joking** | 1 | 1 | - | 166.19 | - | 5,419 | - | 0.000307 | 🔵 low — common in general English | — |
| 5783 | **chat** | 1 | 1 | - | 166.19 | - | 5,420 | - | 0.000307 | 🔵 low — common in general English | — |
| 5784 | **awe** | 1 | 1 | - | 166.19 | - | 5,421 | - | 0.000307 | 🔵 low — common in general English | — |
| 5785 | **casualness** | 1 | 1 | - | 166.19 | - | 5,422 | - | 0.000307 | 🔵 low — common in general English | — |
| 5786 | **solicitously** | 1 | 1 | - | 166.19 | - | 5,423 | - | 0.000307 | 🔵 low — common in general English | — |
| 5787 | **vainly** | 1 | 1 | - | 166.19 | - | 5,424 | - | 0.000307 | 🔵 low — common in general English | — |
| 5788 | **scowl** | 1 | 1 | - | 166.19 | - | 5,425 | - | 0.000307 | 🔵 low — common in general English | — |
| 5789 | **ill-considered** | 1 | 1 | - | 166.19 | - | 5,426 | - | 0.000307 | 🔵 low — common in general English | — |
| 5790 | **composure** | 1 | 1 | - | 166.19 | - | 5,427 | - | 0.000307 | 🔵 low — common in general English | — |
| 5791 | **conver** | 1 | 1 | - | 166.19 | - | 5,428 | - | 0.000307 | 🔵 low — common in general English | — |
| 5792 | **self-im** | 1 | 1 | - | 166.19 | - | 5,429 | - | 0.000307 | 🔵 low — common in general English | — |
| 5793 | **portance** | 1 | 1 | - | 166.19 | - | 5,430 | - | 0.000307 | 🔵 low — common in general English | — |
| 5794 | **untiringly** | 1 | 1 | - | 166.19 | - | 5,431 | - | 0.000307 | 🔵 low — common in general English | — |
| 5795 | **gliding** | 1 | 1 | - | 166.19 | - | 5,432 | - | 0.000306 | 🔵 low — common in general English | — |
| 5796 | **delighting** | 1 | 1 | - | 166.19 | - | 5,433 | - | 0.000306 | 🔵 low — common in general English | — |
| 5797 | **spoiling** | 1 | 1 | - | 166.19 | - | 5,434 | - | 0.000306 | 🔵 low — common in general English | — |
| 5798 | **bored** | 1 | 1 | - | 166.19 | - | 5,435 | - | 0.000306 | 🔵 low — common in general English | — |
| 5799 | **tasting** | 1 | 1 | - | 166.19 | - | 5,437 | - | 0.000306 | 🔵 low — common in general English | — |
| 5800 | **better-off** | 1 | 1 | - | 166.19 | - | 5,438 | - | 0.000306 | 🔵 low — common in general English | — |
| 5801 | **fellow-voyager** | 1 | 1 | - | 166.19 | - | 5,439 | - | 0.000306 | 🔵 low — common in general English | — |
| 5802 | **bean-tsampa** | 1 | 1 | - | 166.19 | - | 5,440 | - | 0.000306 | 🔵 low — common in general English | — |
| 5803 | **fruitful-thi** | 1 | 1 | - | 166.19 | - | 5,441 | - | 0.000306 | 🔵 low — common in general English | — |
| 5804 | **contemplation** | 1 | 1 | - | 166.19 | - | 5,442 | - | 0.000306 | 🔵 low — common in general English | — |
| 5805 | **portrait** | 1 | 1 | - | 166.19 | - | 5,443 | - | 0.000306 | 🔵 low — common in general English | — |
| 5806 | **epitomiz** | 1 | 1 | - | 166.19 | - | 5,444 | - | 0.000306 | 🔵 low — common in general English | — |
| 5807 | **assiduous** | 1 | 1 | - | 166.19 | - | 5,445 | - | 0.000306 | 🔵 low — common in general English | — |
| 5808 | **examina** | 1 | 1 | - | 166.19 | - | 5,446 | - | 0.000306 | 🔵 low — common in general English | — |
| 5809 | **abound** | 1 | 1 | - | 166.19 | - | 5,447 | - | 0.000306 | 🔵 low — common in general English | — |
| 5810 | **deception** | 1 | 1 | - | 166.19 | - | 5,448 | - | 0.000306 | 🔵 low — common in general English | — |
| 5811 | **voice-or** | 1 | 1 | - | 166.19 | - | 5,449 | - | 0.000306 | 🔵 low — common in general English | — |
| 5812 | **name-can** | 1 | 1 | - | 166.19 | - | 5,450 | - | 0.000306 | 🔵 low — common in general English | — |
| 5813 | **restless** | 1 | 1 | - | 166.19 | - | 5,451 | - | 0.000306 | 🔵 low — common in general English | — |
| 5814 | **transfixed** | 1 | 1 | - | 166.19 | - | 5,452 | - | 0.000306 | 🔵 low — common in general English | — |
| 5815 | **limb-just** | 1 | 1 | - | 166.19 | - | 5,453 | - | 0.000306 | 🔵 low — common in general English | — |
| 5816 | **ropa** | 1 | 1 | - | 166.19 | - | 5,454 | - | 0.000306 | 🔵 low — common in general English | — |
| 5817 | **bodily** | 1 | 1 | - | 166.19 | - | 5,455 | - | 0.000306 | 🔵 low — common in general English | — |
| 5818 | **prajna** | 1 | 1 | - | 166.19 | - | 5,456 | - | 0.000306 | 🔵 low — common in general English | — |
| 5819 | **go-and** | 1 | 1 | - | 166.19 | - | 5,457 | - | 0.000306 | 🔵 low — common in general English | — |
| 5820 | **abode** | 1 | 1 | - | 166.19 | - | 5,458 | - | 0.000306 | 🔵 low — common in general English | — |
| 5821 | **circumference** | 1 | 1 | - | 166.19 | - | 5,459 | - | 0.000306 | 🔵 low — common in general English | — |
| 5822 | **sixty-eight** | 1 | 1 | - | 166.19 | - | 5,460 | - | 0.000306 | 🔵 low — common in general English | — |
| 5823 | **blissfully** | 1 | 1 | - | 166.19 | - | 5,461 | - | 0.000306 | 🔵 low — common in general English | — |
| 5824 | **prais** | 1 | 1 | - | 166.19 | - | 5,462 | - | 0.000305 | 🔵 low — common in general English | — |
| 5825 | **sadapraru** | 1 | 1 | - | 166.19 | - | 5,463 | - | 0.000305 | 🔵 low — common in general English | — |
| 5826 | **dita** | 1 | 1 | - | 166.19 | - | 5,464 | - | 0.000305 | 🔵 low — common in general English | — |
| 5827 | **marrow** | 1 | 1 | - | 166.19 | - | 5,465 | - | 0.000305 | 🔵 low — common in general English | — |
| 5828 | **spurted** | 1 | 1 | - | 166.19 | - | 5,466 | - | 0.000305 | 🔵 low — common in general English | — |
| 5829 | **smash** | 1 | 1 | - | 166.19 | - | 5,467 | - | 0.000305 | 🔵 low — common in general English | — |
| 5830 | **inflicting** | 1 | 1 | - | 166.19 | - | 5,468 | - | 0.000305 | 🔵 low — common in general English | — |
| 5831 | **reassumed** | 1 | 1 | - | 166.19 | - | 5,469 | - | 0.000305 | 🔵 low — common in general English | — |
| 5832 | **domain** | 1 | 1 | - | 166.19 | - | 5,470 | - | 0.000305 | 🔵 low — common in general English | — |
| 5833 | **mersed** | 1 | 1 | - | 166.19 | - | 5,471 | - | 0.000305 | 🔵 low — common in general English | — |
| 5834 | **prajaa** | 1 | 1 | - | 166.19 | - | 5,472 | - | 0.000305 | 🔵 low — common in general English | — |
| 5835 | **deco** | 1 | 1 | - | 166.19 | - | 5,473 | - | 0.000305 | 🔵 low — common in general English | — |
| 5836 | **censer** | 1 | 1 | - | 166.19 | - | 5,474 | - | 0.000305 | 🔵 low — common in general English | — |
| 5837 | **wafted** | 1 | 1 | - | 166.19 | - | 5,475 | - | 0.000305 | 🔵 low — common in general English | — |
| 5838 | **aloe-wood** | 1 | 1 | - | 166.19 | - | 5,476 | - | 0.000305 | 🔵 low — common in general English | — |
| 5839 | **coffer** | 1 | 1 | - | 166.19 | - | 5,477 | - | 0.000305 | 🔵 low — common in general English | — |
| 5840 | **pranaparamita** | 1 | 1 | - | 166.19 | - | 5,478 | - | 0.000305 | 🔵 low — common in general English | — |
| 5841 | **sada** | 1 | 1 | - | 166.19 | - | 5,479 | - | 0.000305 | 🔵 low — common in general English | — |
| 5842 | **prarudita** | 1 | 1 | - | 166.19 | - | 5,480 | - | 0.000305 | 🔵 low — common in general English | — |
| 5843 | **sprinkle** | 1 | 1 | - | 166.19 | - | 5,481 | - | 0.000305 | 🔵 low — common in general English | — |
| 5844 | **sprinkled** | 1 | 1 | - | 166.19 | - | 5,482 | - | 0.000305 | 🔵 low — common in general English | — |
| 5845 | **lion-throne** | 1 | 1 | - | 166.19 | - | 5,483 | - | 0.000305 | 🔵 low — common in general English | — |
| 5846 | **expounded** | 1 | 1 | - | 166.19 | - | 5,484 | - | 0.000305 | 🔵 low — common in general English | — |
| 5847 | **buddhas-a** | 1 | 1 | - | 166.19 | - | 5,485 | - | 0.000305 | 🔵 low — common in general English | — |
| 5848 | **melodious** | 1 | 1 | - | 166.19 | - | 5,486 | - | 0.000305 | 🔵 low — common in general English | ~ |
| 5849 | **oiling** | 1 | 1 | - | 166.19 | - | 5,487 | - | 0.000305 | 🔵 low — common in general English | — |
| 5850 | **bearable** | 1 | 1 | - | 166.19 | - | 5,488 | - | 0.000305 | 🔵 low — common in general English | — |
| 5851 | **streamed** | 1 | 1 | - | 166.19 | - | 5,489 | - | 0.000305 | 🔵 low — common in general English | — |
| 5852 | **these-twenty-four** | 1 | 1 | - | 166.19 | - | 5,490 | - | 0.000305 | 🔵 low — common in general English | — |
| 5853 | **forbade** | 1 | 1 | - | 166.19 | - | 5,491 | - | 0.000305 | 🔵 low — common in general English | — |
| 5854 | **pandita-gatekeeper** | 1 | 1 | - | 166.19 | - | 5,492 | - | 0.000305 | 🔵 low — common in general English | — |
| 5855 | **magadha** | 1 | 1 | - | 166.19 | - | 5,493 | - | 0.000304 | 🔵 low — common in general English | — |
| 5856 | **insistently** | 1 | 1 | - | 166.19 | - | 5,494 | - | 0.000304 | 🔵 low — common in general English | — |
| 5857 | **compassion-why** | 1 | 1 | - | 166.19 | - | 5,495 | - | 0.000304 | 🔵 low — common in general English | — |
| 5858 | **gatekeeper** | 1 | 1 | - | 166.19 | - | 5,496 | - | 0.000304 | 🔵 low — common in general English | — |
| 5859 | **retorted** | 1 | 1 | - | 166.19 | - | 5,497 | - | 0.000304 | 🔵 low — common in general English | — |
| 5860 | **ngari** | 1 | 1 | - | 166.19 | - | 5,498 | - | 0.000304 | 🔵 low — common in general English | — |
| 5861 | **gungthang** | 1 | 1 | - | 166.19 | - | 5,499 | - | 0.000304 | 🔵 low — common in general English | — |
| 5862 | **sherab** | 1 | 1 | - | 166.19 | - | 5,500 | - | 0.000304 | 🔵 low — common in general English | — |
| 5863 | **thopa-ga** | 1 | 1 | - | 166.19 | - | 5,501 | - | 0.000304 | 🔵 low — common in general English | — |
| 5864 | **yungdrung** | 1 | 1 | - | 166.19 | - | 5,502 | - | 0.000304 | 🔵 low — common in general English | — |
| 5865 | **throgyal** | 1 | 1 | - | 166.19 | - | 5,503 | - | 0.000304 | 🔵 low — common in general English | — |
| 5866 | **lharje** | 1 | 1 | - | 166.19 | - | 5,504 | - | 0.000304 | 🔵 low — common in general English | — |
| 5867 | **nupchung** | 1 | 1 | - | 166.19 | - | 5,505 | - | 0.000304 | 🔵 low — common in general English | — |
| 5868 | **repenting** | 1 | 1 | - | 166.19 | - | 5,506 | - | 0.000304 | 🔵 low — common in general English | — |
| 5869 | **eminently** | 1 | 1 | - | 166.19 | - | 5,507 | - | 0.000304 | 🔵 low — common in general English | — |
| 5870 | **hail-if** | 1 | 1 | - | 166.19 | - | 5,508 | - | 0.000304 | 🔵 low — common in general English | — |
| 5871 | **night-and** | 1 | 1 | - | 166.19 | - | 5,509 | - | 0.000304 | 🔵 low — common in general English | — |
| 5872 | **suffuse** | 1 | 1 | - | 166.19 | - | 5,510 | - | 0.000304 | 🔵 low — common in general English | — |
| 5873 | **tingled** | 1 | 1 | - | 166.19 | - | 5,511 | - | 0.000304 | 🔵 low — common in general English | — |
| 5874 | **tarma** | 1 | 1 | - | 166.19 | - | 5,512 | - | 0.000304 | 🔵 low — common in general English | — |
| 5875 | **dode** | 1 | 1 | - | 166.19 | - | 5,513 | - | 0.000304 | 🔵 low — common in general English | — |
| 5876 | **continu** | 1 | 1 | - | 166.19 | - | 5,514 | - | 0.000304 | 🔵 low — common in general English | — |
| 5877 | **reckon** | 1 | 1 | - | 166.19 | - | 5,515 | - | 0.000304 | 🔵 low — common in general English | — |
| 5878 | **acquiesced** | 1 | 1 | - | 166.19 | - | 5,516 | - | 0.000304 | 🔵 low — common in general English | — |
| 5879 | **twelve-pillared** | 1 | 1 | - | 166.19 | - | 5,517 | - | 0.000304 | 🔵 low — common in general English | — |
| 5880 | **sanctuary** | 1 | 1 | - | 166.19 | - | 5,518 | - | 0.000304 | 🔵 low — common in general English | — |
| 5881 | **meton** | 1 | 1 | - | 166.19 | - | 5,519 | - | 0.000304 | 🔵 low — common in general English | — |
| 5882 | **tsonpo** | 1 | 1 | - | 166.19 | - | 5,520 | - | 0.000304 | 🔵 low — common in general English | — |
| 5883 | **tsangrong** | 1 | 1 | - | 166.19 | - | 5,521 | - | 0.000304 | 🔵 low — common in general English | — |
| 5884 | **sarilvara** | 1 | 1 | - | 166.19 | - | 5,522 | - | 0.000304 | 🔵 low — common in general English | — |
| 5885 | **tsurton** | 1 | 1 | - | 166.19 | - | 5,523 | - | 0.000304 | 🔵 low — common in general English | — |
| 5886 | **wange** | 1 | 1 | - | 166.19 | - | 5,524 | - | 0.000303 | 🔵 low — common in general English | — |
| 5887 | **dol** | 1 | 1 | - | 166.19 | - | 5,525 | - | 0.000303 | 🔵 low — common in general English | — |
| 5888 | **guhyasamaja** | 1 | 1 | - | 166.19 | - | 5,526 | - | 0.000303 | 🔵 low — common in general English | — |
| 5889 | **ngokton** | 1 | 1 | - | 166.19 | - | 5,527 | - | 0.000303 | 🔵 low — common in general English | — |
| 5890 | **chador** | 1 | 1 | - | 166.19 | - | 5,528 | - | 0.000303 | 🔵 low — common in general English | — |
| 5891 | **shung** | 1 | 1 | - | 166.19 | - | 5,529 | - | 0.000303 | 🔵 low — common in general English | — |
| 5892 | **khok** | 1 | 1 | - | 166.19 | - | 5,530 | - | 0.000303 | 🔵 low — common in general English | — |
| 5893 | **powerment** | 1 | 1 | - | 166.19 | - | 5,531 | - | 0.000303 | 🔵 low — common in general English | — |
| 5894 | **dispersed** | 1 | 1 | - | 166.19 | - | 5,532 | - | 0.000303 | 🔵 low — common in general English | — |
| 5895 | **mahasiddha** | 1 | 1 | - | 166.19 | - | 5,533 | - | 0.000303 | 🔵 low — common in general English | ✓ གྲུབ་ཆེན |
| 5896 | **tacarya** | 1 | 1 | - | 166.19 | - | 5,534 | - | 0.000303 | 🔵 low — common in general English | — |
| 5897 | **floundering** | 1 | 1 | - | 166.19 | - | 5,535 | - | 0.000303 | 🔵 low — common in general English | — |
| 5898 | **byway** | 1 | 1 | - | 166.19 | - | 5,536 | - | 0.000303 | 🔵 low — common in general English | — |
| 5899 | **vajrasativa** | 1 | 1 | - | 166.19 | - | 5,537 | - | 0.000303 | 🔵 low — common in general English | — |
| 5900 | **life-story** | 1 | 1 | - | 166.19 | - | 5,538 | - | 0.000303 | 🔵 low — common in general English | — |
| 5901 | **sprout** | 1 | 1 | - | 166.19 | - | 5,539 | - | 0.000303 | 🔵 low — common in general English | — |
| 5902 | **bestowing** | 1 | 1 | - | 166.19 | - | 5,540 | - | 0.000303 | 🔵 low — common in general English | — |
| 5903 | **departed-i** | 1 | 1 | - | 166.19 | - | 5,541 | - | 0.000303 | 🔵 low — common in general English | — |
| 5904 | **simple-minded** | 1 | 1 | - | 166.19 | - | 5,542 | - | 0.000303 | 🔵 low — common in general English | — |
| 5905 | **caretaker** | 1 | 1 | - | 166.19 | - | 5,543 | - | 0.000303 | 🔵 low — common in general English | — |
| 5906 | **food-offering** | 1 | 1 | - | 166.19 | - | 5,544 | - | 0.000303 | 🔵 low — common in general English | — |
| 5907 | **butter-lamp** | 1 | 1 | - | 166.19 | - | 5,545 | - | 0.000303 | 🔵 low — common in general English | — |
| 5908 | **imagined** | 1 | 1 | - | 166.19 | - | 5,546 | - | 0.000303 | 🔵 low — common in general English | — |
| 5909 | **dunking** | 1 | 1 | - | 166.19 | - | 5,547 | - | 0.000303 | 🔵 low — common in general English | — |
| 5910 | **sputter** | 1 | 1 | - | 166.19 | - | 5,548 | - | 0.000303 | 🔵 low — common in general English | — |
| 5911 | **tthrow** | 1 | 1 | - | 166.19 | - | 5,549 | - | 0.000303 | 🔵 low — common in general English | — |
| 5912 | **though-so** | 1 | 1 | - | 166.19 | - | 5,550 | - | 0.000303 | 🔵 low — common in general English | — |
| 5913 | **jowo-act** | 1 | 1 | - | 166.19 | - | 5,551 | - | 0.000303 | 🔵 low — common in general English | — |
| 5914 | **wrong-the** | 1 | 1 | - | 166.19 | - | 5,552 | - | 0.000303 | 🔵 low — common in general English | — |
| 5915 | **leavingjetsun** | 1 | 1 | - | 166.19 | - | 5,553 | - | 0.000303 | 🔵 low — common in general English | — |
| 5916 | **unwavering** | 1 | 1 | - | 166.19 | - | 5,554 | - | 0.000303 | 🔵 low — common in general English | — |
| 5917 | **realms-the** | 1 | 1 | - | 166.19 | - | 5,555 | - | 0.000302 | 🔵 low — common in general English | — |
| 5918 | **realm-motivate** | 1 | 1 | - | 166.19 | - | 5,556 | - | 0.000302 | 🔵 low — common in general English | — |
| 5919 | **beings-our** | 1 | 1 | - | 166.19 | - | 5,557 | - | 0.000302 | 🔵 low — common in general English | — |
| 5920 | **beginnin** | 1 | 1 | - | 166.19 | - | 5,558 | - | 0.000302 | 🔵 low — common in general English | — |
| 5921 | **gless** | 1 | 1 | - | 166.19 | - | 5,559 | - | 0.000302 | 🔵 low — common in general English | — |
| 5922 | **time-are** | 1 | 1 | - | 166.19 | - | 5,560 | - | 0.000302 | 🔵 low — common in general English | — |
| 5923 | **dhar** | 1 | 1 | - | 166.19 | - | 5,561 | - | 0.000302 | 🔵 low — common in general English | — |
| 5924 | **makaya** | 1 | 1 | - | 166.19 | - | 5,562 | - | 0.000302 | 🔵 low — common in general English | — |
| 5925 | **indestructible** | 1 | 1 | - | 166.19 | - | 5,563 | - | 0.000302 | 🔵 low — common in general English | — |
| 5926 | **all-pervasive** | 1 | 1 | - | 166.19 | - | 5,564 | - | 0.000302 | 🔵 low — common in general English | — |
| 5927 | **mindstream** | 1 | 1 | - | 166.19 | - | 5,565 | - | 0.000302 | 🔵 low — common in general English | — |
| 5928 | **inseparability** | 1 | 1 | - | 166.19 | - | 5,566 | - | 0.000302 | 🔵 low — common in general English | — |
| 5929 | **irregulari** | 1 | 1 | - | 166.19 | - | 5,567 | - | 0.000302 | 🔵 low — common in general English | — |
| 5930 | **twig** | 1 | 1 | - | 166.19 | - | 5,568 | - | 0.000302 | 🔵 low — common in general English | — |
| 5931 | **entrancing** | 1 | 1 | - | 166.19 | - | 5,569 | - | 0.000302 | 🔵 low — common in general English | — |
| 5932 | **lion** | 1 | 1 | - | 166.19 | - | 5,570 | - | 0.000302 | 🔵 low — common in general English | — |
| 5933 | **multi-coloured** | 1 | 1 | - | 166.19 | - | 5,571 | - | 0.000302 | 🔵 low — common in general English | — |
| 5934 | **cloak** | 1 | 1 | - | 166.19 | - | 5,572 | - | 0.000302 | 🔵 low — common in general English | — |
| 5935 | **sleeved** | 1 | 1 | - | 166.19 | - | 5,573 | - | 0.000302 | 🔵 low — common in general English | — |
| 5936 | **tunic** | 1 | 1 | - | 166.19 | - | 5,574 | - | 0.000302 | 🔵 low — common in general English | — |
| 5937 | **samantab** | 1 | 1 | - | 166.19 | - | 5,575 | - | 0.000302 | 🔵 low — common in general English | — |
| 5938 | **jnanasiltra** | 1 | 1 | - | 166.19 | - | 5,576 | - | 0.000302 | 🔵 low — common in general English | — |
| 5939 | **consort-the** | 1 | 1 | - | 166.19 | - | 5,577 | - | 0.000302 | 🔵 low — common in general English | — |
| 5940 | **trisongdetsen** | 1 | 1 | - | 166.19 | - | 5,578 | - | 0.000302 | 🔵 low — common in general English | — |
| 5941 | **nirmanakya** | 1 | 1 | - | 166.19 | - | 5,579 | - | 0.000302 | 🔵 low — common in general English | — |
| 5942 | **garbed** | 1 | 1 | - | 166.19 | - | 5,580 | - | 0.000302 | 🔵 low — common in general English | — |
| 5943 | **hood-the** | 1 | 1 | - | 166.19 | - | 5,581 | - | 0.000302 | 🔵 low — common in general English | — |
| 5944 | **right-hand** | 1 | 1 | - | 166.19 | - | 5,582 | - | 0.000302 | 🔵 low — common in general English | — |
| 5945 | **families-mafijusri** | 1 | 1 | - | 166.19 | - | 5,583 | - | 0.000302 | 🔵 low — common in general English | — |
| 5946 | **left-hand** | 1 | 1 | - | 166.19 | - | 5,584 | - | 0.000302 | 🔵 low — common in general English | — |
| 5947 | **alms-bowl** | 1 | 1 | - | 166.19 | - | 5,585 | - | 0.000302 | 🔵 low — common in general English | — |
| 5948 | **topmost** | 1 | 1 | - | 166.19 | - | 5,586 | - | 0.000302 | 🔵 low — common in general English | — |
| 5949 | **resonate** | 1 | 1 | - | 166.19 | - | 5,587 | - | 0.000301 | 🔵 low — common in general English | — |
| 5950 | **melody** | 1 | 1 | - | 166.19 | - | 5,588 | - | 0.000301 | 🔵 low — common in general English | — |
| 5951 | **consonant** | 1 | 1 | - | 166.19 | - | 5,589 | - | 0.000301 | 🔵 low — common in general English | — |
| 5952 | **dharma-protector** | 1 | 1 | - | 166.19 | - | 5,590 | - | 0.000301 | 🔵 low — common in general English | — |
| 5953 | **leaking** | 1 | 1 | - | 166.19 | - | 5,591 | - | 0.000301 | 🔵 low — common in general English | — |
| 5954 | **detest** | 1 | 1 | - | 166.19 | - | 5,592 | - | 0.000301 | 🔵 low — common in general English | — |
| 5955 | **refuge-prayer** | 1 | 1 | - | 166.19 | - | 5,593 | - | 0.000301 | 🔵 low — common in general English | — |
| 5956 | **precedence** | 1 | 1 | - | 166.19 | - | 5,594 | - | 0.000301 | 🔵 low — common in general English | — |
| 5957 | **kinder** | 1 | 1 | - | 166.19 | - | 5,595 | - | 0.000301 | 🔵 low — common in general English | — |
| 5958 | **possessions-the** | 1 | 1 | - | 166.19 | - | 5,596 | - | 0.000301 | 🔵 low — common in general English | — |
| 5959 | **aunt** | 1 | 1 | - | 166.19 | - | 5,597 | - | 0.000301 | 🔵 low — common in general English | — |
| 5960 | **palmo** | 1 | 1 | - | 166.19 | - | 5,598 | - | 0.000301 | 🔵 low — common in general English | ~ |
| 5961 | **assailed** | 1 | 1 | - | 166.19 | - | 5,599 | - | 0.000301 | 🔵 low — common in general English | — |
| 5962 | **invade** | 1 | 1 | - | 166.19 | - | 5,600 | - | 0.000301 | 🔵 low — common in general English | — |
| 5963 | **fearlessness** | 1 | 1 | - | 166.19 | - | 5,601 | - | 0.000301 | 🔵 low — common in general English | — |
| 5964 | **impelled** | 1 | 1 | - | 166.19 | - | 5,602 | - | 0.000301 | 🔵 low — common in general English | — |
| 5965 | **slingstone** | 1 | 1 | - | 166.19 | - | 5,603 | - | 0.000301 | 🔵 low — common in general English | — |
| 5966 | **whirring** | 1 | 1 | - | 166.19 | - | 5,604 | - | 0.000301 | 🔵 low — common in general English | — |
| 5967 | **tirthika-who** | 1 | 1 | - | 166.19 | - | 5,605 | - | 0.000301 | 🔵 low — common in general English | — |
| 5968 | **criticiz** | 1 | 1 | - | 166.19 | - | 5,606 | - | 0.000301 | 🔵 low — common in general English | — |
| 5969 | **day-come** | 1 | 1 | - | 166.19 | - | 5,608 | - | 0.000301 | 🔵 low — common in general English | — |
| 5970 | **rend** | 1 | 1 | - | 166.19 | - | 5,609 | - | 0.000301 | 🔵 low — common in general English | — |
| 5971 | **doud** | 1 | 1 | - | 166.19 | - | 5,610 | - | 0.000301 | 🔵 low — common in general English | — |
| 5972 | **healing** | 1 | 1 | - | 166.19 | - | 5,611 | - | 0.000301 | 🔵 low — common in general English | — |
| 5973 | **life-comfort** | 1 | 1 | - | 166.19 | - | 5,612 | - | 0.000301 | 🔵 low — common in general English | — |
| 5974 | **whatever-spring** | 1 | 1 | - | 166.19 | - | 5,613 | - | 0.000301 | 🔵 low — common in general English | — |
| 5975 | **create-prostration** | 1 | 1 | - | 166.19 | - | 5,614 | - | 0.000301 | 🔵 low — common in general English | — |
| 5976 | **disciples-to** | 1 | 1 | - | 166.19 | - | 5,615 | - | 0.000301 | 🔵 low — common in general English | — |
| 5977 | **nicknamed** | 1 | 1 | - | 166.19 | - | 5,616 | - | 0.000301 | 🔵 low — common in general English | — |
| 5978 | **pawned** | 1 | 1 | - | 166.19 | - | 5,617 | - | 0.000301 | 🔵 low — common in general English | — |
| 5979 | **saliva** | 1 | 1 | - | 166.19 | - | 5,618 | - | 0.000301 | 🔵 low — common in general English | — |
| 5980 | **maxim** | 1 | 1 | - | 166.19 | - | 5,619 | - | 0.000300 | 🔵 low — common in general English | — |
| 5981 | **vajradhatvishvari** | 1 | 1 | - | 166.19 | - | 5,620 | - | 0.000300 | 🔵 low — common in general English | ✓ རྡོ་རྗེ་དབྱིངས་ཕྱུག་མ |
| 5982 | **seed-syllable** | 1 | 1 | - | 166.19 | - | 5,621 | - | 0.000300 | 🔵 low — common in general English | — |
| 5983 | **disre** | 1 | 1 | - | 166.19 | - | 5,622 | - | 0.000300 | 🔵 low — common in general English | — |
| 5984 | **spect** | 1 | 1 | - | 166.19 | - | 5,623 | - | 0.000300 | 🔵 low — common in general English | — |
| 5985 | **seventy** | 1 | 1 | - | 166.19 | - | 5,624 | - | 0.000300 | 🔵 low — common in general English | — |
| 5986 | **stanza** | 1 | 1 | - | 166.19 | - | 5,625 | - | 0.000300 | 🔵 low — common in general English | — |
| 5987 | **reparation** | 1 | 1 | - | 166.19 | - | 5,626 | - | 0.000300 | 🔵 low — common in general English | — |
| 5988 | **tenuous** | 1 | 1 | - | 166.19 | - | 5,627 | - | 0.000300 | 🔵 low — common in general English | — |
| 5989 | **people-the** | 1 | 1 | - | 166.19 | - | 5,628 | - | 0.000300 | 🔵 low — common in general English | — |
| 5990 | **moulded** | 1 | 1 | - | 166.19 | - | 5,629 | - | 0.000300 | 🔵 low — common in general English | — |
| 5991 | **it-all** | 1 | 1 | - | 166.19 | - | 5,630 | - | 0.000300 | 🔵 low — common in general English | — |
| 5992 | **seductive** | 1 | 1 | - | 166.19 | - | 5,631 | - | 0.000300 | 🔵 low — common in general English | — |
| 5993 | **gullible** | 1 | 1 | - | 166.19 | - | 5,632 | - | 0.000300 | 🔵 low — common in general English | — |
| 5994 | **decadence** | 1 | 1 | - | 166.19 | - | 5,633 | - | 0.000300 | 🔵 low — common in general English | — |
| 5995 | **deceived** | 1 | 1 | - | 166.19 | - | 5,634 | - | 0.000300 | 🔵 low — common in general English | — |
| 5996 | **seduction** | 1 | 1 | - | 166.19 | - | 5,635 | - | 0.000300 | 🔵 low — common in general English | — |
| 5997 | **invaded** | 1 | 1 | - | 166.19 | - | 5,636 | - | 0.000300 | 🔵 low — common in general English | — |
| 5998 | **hesita** | 1 | 1 | - | 166.19 | - | 5,637 | - | 0.000300 | 🔵 low — common in general English | — |
| 5999 | **guis** | 1 | 1 | - | 166.19 | - | 5,638 | - | 0.000300 | 🔵 low — common in general English | — |
| 6000 | **oppos** | 1 | 1 | - | 166.19 | - | 5,639 | - | 0.000300 | 🔵 low — common in general English | — |
| 6001 | **disciples-none** | 1 | 1 | - | 166.19 | - | 5,640 | - | 0.000300 | 🔵 low — common in general English | — |
| 6002 | **goggle** | 1 | 1 | - | 166.19 | - | 5,641 | - | 0.000300 | 🔵 low — common in general English | — |
| 6003 | **effigy** | 1 | 1 | - | 166.19 | - | 5,642 | - | 0.000300 | 🔵 low — common in general English | — |
| 6004 | **goat-pen** | 1 | 1 | - | 166.19 | - | 5,643 | - | 0.000300 | 🔵 low — common in general English | — |
| 6005 | **legitimately** | 1 | 1 | - | 166.19 | - | 5,644 | - | 0.000300 | 🔵 low — common in general English | — |
| 6006 | **perni** | 1 | 1 | - | 166.19 | - | 5,645 | - | 0.000300 | 🔵 low — common in general English | — |
| 6007 | **cious** | 1 | 1 | - | 166.19 | - | 5,646 | - | 0.000300 | 🔵 low — common in general English | — |
| 6008 | **malevolent** | 1 | 1 | - | 166.19 | - | 5,647 | - | 0.000300 | 🔵 low — common in general English | — |
| 6009 | **confi** | 1 | 1 | - | 166.19 | - | 5,648 | - | 0.000300 | 🔵 low — common in general English | — |
| 6010 | **dence** | 1 | 1 | - | 166.19 | - | 5,649 | - | 0.000300 | 🔵 low — common in general English | — |
| 6011 | **pacified** | 1 | 1 | - | 166.19 | - | 5,650 | - | 0.000300 | 🔵 low — common in general English | — |
| 6012 | **harm-the** | 1 | 1 | - | 166.19 | - | 5,651 | - | 0.000299 | 🔵 low — common in general English | — |
| 6013 | **makers-will** | 1 | 1 | - | 166.19 | - | 5,652 | - | 0.000299 | 🔵 low — common in general English | — |
| 6014 | **quarter-pint** | 1 | 1 | - | 166.19 | - | 5,653 | - | 0.000299 | 🔵 low — common in general English | — |
| 6015 | **faint-hearted** | 1 | 1 | - | 166.19 | - | 5,654 | - | 0.000299 | 🔵 low — common in general English | — |
| 6016 | **pathetic** | 1 | 1 | - | 166.19 | - | 5,655 | - | 0.000299 | 🔵 low — common in general English | — |
| 6017 | **even-minded** | 1 | 1 | - | 166.19 | - | 5,656 | - | 0.000299 | 🔵 low — common in general English | — |
| 6018 | **on-while** | 1 | 1 | - | 166.19 | - | 5,657 | - | 0.000299 | 🔵 low — common in general English | — |
| 6019 | **low-caste** | 1 | 1 | - | 166.19 | - | 5,658 | - | 0.000299 | 🔵 low — common in general English | — |
| 6020 | **stung** | 1 | 1 | - | 166.19 | - | 5,659 | - | 0.000299 | 🔵 low — common in general English | — |
| 6021 | **brushing** | 1 | 1 | - | 166.19 | - | 5,660 | - | 0.000299 | 🔵 low — common in general English | — |
| 6022 | **accidentally** | 1 | 1 | - | 166.19 | - | 5,661 | - | 0.000299 | 🔵 low — common in general English | — |
| 6023 | **diffi** | 1 | 1 | - | 166.19 | - | 5,662 | - | 0.000299 | 🔵 low — common in general English | — |
| 6024 | **culty** | 1 | 1 | - | 166.19 | - | 5,663 | - | 0.000299 | 🔵 low — common in general English | — |
| 6025 | **all-those** | 1 | 1 | - | 166.19 | - | 5,664 | - | 0.000299 | 🔵 low — common in general English | — |
| 6026 | **you-train** | 1 | 1 | - | 166.19 | - | 5,665 | - | 0.000299 | 🔵 low — common in general English | — |
| 6027 | **beings-whether** | 1 | 1 | - | 166.19 | - | 5,666 | - | 0.000299 | 🔵 low — common in general English | — |
| 6028 | **between-a** | 1 | 1 | - | 166.19 | - | 5,667 | - | 0.000299 | 🔵 low — common in general English | — |
| 6029 | **mindless** | 1 | 1 | - | 166.19 | - | 5,668 | - | 0.000299 | 🔵 low — common in general English | — |
| 6030 | **distinc** | 1 | 1 | - | 166.19 | - | 5,669 | - | 0.000299 | 🔵 low — common in general English | — |
| 6031 | **devoting** | 1 | 1 | - | 166.19 | - | 5,670 | - | 0.000299 | 🔵 low — common in general English | — |
| 6032 | **cosy** | 1 | 1 | - | 166.19 | - | 5,671 | - | 0.000299 | 🔵 low — common in general English | — |
| 6033 | **glared** | 1 | 1 | - | 166.19 | - | 5,672 | - | 0.000299 | 🔵 low — common in general English | — |
| 6034 | **endeavouring** | 1 | 1 | - | 166.19 | - | 5,673 | - | 0.000299 | 🔵 low — common in general English | — |
| 6035 | **jeal** | 1 | 1 | - | 166.19 | - | 5,674 | - | 0.000299 | 🔵 low — common in general English | — |
| 6036 | **ousy** | 1 | 1 | - | 166.19 | - | 5,675 | - | 0.000299 | 🔵 low — common in general English | — |
| 6037 | **hypocrite** | 1 | 1 | - | 166.19 | - | 5,676 | - | 0.000299 | 🔵 low — common in general English | — |
| 6038 | **ity** | 1 | 1 | - | 166.19 | - | 5,677 | - | 0.000299 | 🔵 low — common in general English | — |
| 6039 | **despise** | 1 | 1 | - | 166.19 | - | 5,678 | - | 0.000299 | 🔵 low — common in general English | — |
| 6040 | **distressed** | 1 | 1 | - | 166.19 | - | 5,679 | - | 0.000299 | 🔵 low — common in general English | — |
| 6041 | **khotan** | 1 | 1 | - | 166.19 | - | 5,680 | - | 0.000299 | 🔵 low — common in general English | — |
| 6042 | **mafljusri** | 1 | 1 | - | 166.19 | - | 5,681 | - | 0.000299 | 🔵 low — common in general English | — |
| 6043 | **dismembered** | 1 | 1 | - | 166.19 | - | 5,682 | - | 0.000299 | 🔵 low — common in general English | — |
| 6044 | **vanquished** | 1 | 1 | - | 166.19 | - | 5,683 | - | 0.000299 | 🔵 low — common in general English | — |
| 6045 | **chick** | 1 | 1 | - | 166.19 | - | 5,684 | - | 0.000298 | 🔵 low — common in general English | — |
| 6046 | **torment-a** | 1 | 1 | - | 166.19 | - | 5,685 | - | 0.000298 | 🔵 low — common in general English | — |
| 6047 | **bursting** | 1 | 1 | - | 166.19 | - | 5,686 | - | 0.000298 | 🔵 low — common in general English | — |
| 6048 | **butchered** | 1 | 1 | - | 166.19 | - | 5,687 | - | 0.000298 | 🔵 low — common in general English | — |
| 6049 | **delay-thi** | 1 | 1 | - | 166.19 | - | 5,688 | - | 0.000298 | 🔵 low — common in general English | — |
| 6050 | **barbarity** | 1 | 1 | - | 166.19 | - | 5,689 | - | 0.000298 | 🔵 low — common in general English | — |
| 6051 | **twist** | 1 | 1 | - | 166.19 | - | 5,690 | - | 0.000298 | 🔵 low — common in general English | — |
| 6052 | **belly-hair** | 1 | 1 | - | 166.19 | - | 5,691 | - | 0.000298 | 🔵 low — common in general English | — |
| 6053 | **weal** | 1 | 1 | - | 166.19 | - | 5,692 | - | 0.000298 | 🔵 low — common in general English | — |
| 6054 | **grunting** | 1 | 1 | - | 166.19 | - | 5,693 | - | 0.000298 | 🔵 low — common in general English | — |
| 6055 | **backside** | 1 | 1 | - | 166.19 | - | 5,694 | - | 0.000298 | 🔵 low — common in general English | — |
| 6056 | **horseback** | 1 | 1 | - | 166.19 | - | 5,695 | - | 0.000298 | 🔵 low — common in general English | — |
| 6057 | **sidesaddle** | 1 | 1 | - | 166.19 | - | 5,696 | - | 0.000298 | 🔵 low — common in general English | — |
| 6058 | **stumble** | 1 | 1 | - | 166.19 | - | 5,697 | - | 0.000298 | 🔵 low — common in general English | — |
| 6059 | **sympathy** | 1 | 1 | - | 166.19 | - | 5,698 | - | 0.000298 | 🔵 low — common in general English | — |
| 6060 | **animal-a** | 1 | 1 | - | 166.19 | - | 5,699 | - | 0.000298 | 🔵 low — common in general English | — |
| 6061 | **example-that** | 1 | 1 | - | 166.19 | - | 5,700 | - | 0.000298 | 🔵 low — common in general English | — |
| 6062 | **paralyzing** | 1 | 1 | - | 166.19 | - | 5,701 | - | 0.000298 | 🔵 low — common in general English | — |
| 6063 | **blood-blister** | 1 | 1 | - | 166.19 | - | 5,702 | - | 0.000298 | 🔵 low — common in general English | — |
| 6064 | **gutted** | 1 | 1 | - | 166.19 | - | 5,703 | - | 0.000298 | 🔵 low — common in general English | — |
| 6065 | **bled** | 1 | 1 | - | 166.19 | - | 5,704 | - | 0.000298 | 🔵 low — common in general English | — |
| 6066 | **flesh-eating** | 1 | 1 | - | 166.19 | - | 5,705 | - | 0.000298 | 🔵 low — common in general English | — |
| 6067 | **resourceful** | 1 | 1 | - | 166.19 | - | 5,706 | - | 0.000298 | 🔵 low — common in general English | — |
| 6068 | **twine** | 1 | 1 | - | 166.19 | - | 5,707 | - | 0.000298 | 🔵 low — common in general English | — |
| 6069 | **ring-hole** | 1 | 1 | - | 166.19 | - | 5,708 | - | 0.000298 | 🔵 low — common in general English | — |
| 6070 | **gouged** | 1 | 1 | - | 166.19 | - | 5,709 | - | 0.000298 | 🔵 low — common in general English | — |
| 6071 | **hoisted** | 1 | 1 | - | 166.19 | - | 5,710 | - | 0.000298 | 🔵 low — common in general English | — |
| 6072 | **yak-hair** | 1 | 1 | - | 166.19 | - | 5,711 | - | 0.000298 | 🔵 low — common in general English | — |
| 6073 | **cord** | 1 | 1 | - | 166.19 | - | 5,712 | - | 0.000298 | 🔵 low — common in general English | — |
| 6074 | **aching** | 1 | 1 | - | 166.19 | - | 5,713 | - | 0.000298 | 🔵 low — common in general English | — |
| 6075 | **rasp** | 1 | 1 | - | 166.19 | - | 5,714 | - | 0.000298 | 🔵 low — common in general English | — |
| 6076 | **rump** | 1 | 1 | - | 166.19 | - | 5,715 | - | 0.000298 | 🔵 low — common in general English | — |
| 6077 | **bruised** | 1 | 1 | - | 166.19 | - | 5,716 | - | 0.000298 | 🔵 low — common in general English | — |
| 6078 | **stirrup** | 1 | 1 | - | 166.19 | - | 5,717 | - | 0.000297 | 🔵 low — common in general English | — |
| 6079 | **exhausting** | 1 | 1 | - | 166.19 | - | 5,718 | - | 0.000297 | 🔵 low — common in general English | — |
| 6080 | **help-impartial** | 1 | 1 | - | 166.19 | - | 5,719 | - | 0.000297 | 🔵 low — common in general English | — |
| 6081 | **ganging** | 1 | 1 | - | 166.19 | - | 5,720 | - | 0.000297 | 🔵 low — common in general English | — |
| 6082 | **mischievous** | 1 | 1 | - | 166.19 | - | 5,721 | - | 0.000297 | 🔵 low — common in general English | — |
| 6083 | **intoning** | 1 | 1 | - | 166.19 | - | 5,722 | - | 0.000297 | 🔵 low — common in general English | — |
| 6084 | **impartial** | 1 | 1 | - | 166.19 | - | 5,723 | - | 0.000297 | 🔵 low — common in general English | — |
| 6085 | **horrible** | 1 | 1 | - | 166.19 | - | 5,724 | - | 0.000297 | 🔵 low — common in general English | — |
| 6086 | **hurled** | 1 | 1 | - | 166.19 | - | 5,725 | - | 0.000297 | 🔵 low — common in general English | — |
| 6087 | **exorcising** | 1 | 1 | - | 166.19 | - | 5,726 | - | 0.000297 | 🔵 low — common in general English | — |
| 6088 | **intimidating** | 1 | 1 | - | 166.19 | - | 5,727 | - | 0.000297 | 🔵 low — common in general English | — |
| 6089 | **spanking** | 1 | 1 | - | 166.19 | - | 5,728 | - | 0.000297 | 🔵 low — common in general English | — |
| 6090 | **pandering** | 1 | 1 | - | 166.19 | - | 5,729 | - | 0.000297 | 🔵 low — common in general English | — |
| 6091 | **wrongdoer** | 1 | 1 | - | 166.19 | - | 5,730 | - | 0.000297 | 🔵 low — common in general English | — |
| 6092 | **hateful** | 1 | 1 | - | 166.19 | - | 5,731 | - | 0.000297 | 🔵 low — common in general English | — |
| 6093 | **enemies-protecting** | 1 | 1 | - | 166.19 | - | 5,732 | - | 0.000297 | 🔵 low — common in general English | — |
| 6094 | **hatred-were** | 1 | 1 | - | 166.19 | - | 5,733 | - | 0.000297 | 🔵 low — common in general English | — |
| 6095 | **expel** | 1 | 1 | - | 166.19 | - | 5,734 | - | 0.000297 | 🔵 low — common in general English | — |
| 6096 | **indeed-not** | 1 | 1 | - | 166.19 | - | 5,735 | - | 0.000297 | 🔵 low — common in general English | — |
| 6097 | **hate-a** | 1 | 1 | - | 166.19 | - | 5,736 | - | 0.000297 | 🔵 low — common in general English | — |
| 6098 | **chong** | 1 | 1 | - | 166.19 | - | 5,737 | - | 0.000297 | 🔵 low — common in general English | — |
| 6099 | **vinayaka** | 1 | 1 | - | 166.19 | - | 5,738 | - | 0.000297 | 🔵 low — common in general English | — |
| 6100 | **strode** | 1 | 1 | - | 166.19 | - | 5,739 | - | 0.000297 | 🔵 low — common in general English | — |
| 6101 | **recogniz** | 1 | 1 | - | 166.19 | - | 5,740 | - | 0.000297 | 🔵 low — common in general English | — |
| 6102 | **cleric** | 1 | 1 | - | 166.19 | - | 5,741 | - | 0.000297 | 🔵 low — common in general English | — |
| 6103 | **cle** | 1 | 1 | - | 166.19 | - | 5,742 | - | 0.000297 | 🔵 low — common in general English | — |
| 6104 | **bleeding** | 1 | 1 | - | 166.19 | - | 5,743 | - | 0.000297 | 🔵 low — common in general English | — |
| 6105 | **decorate** | 1 | 1 | - | 166.19 | - | 5,744 | - | 0.000297 | 🔵 low — common in general English | — |
| 6106 | **rites-they** | 1 | 1 | - | 166.19 | - | 5,745 | - | 0.000297 | 🔵 low — common in general English | — |
| 6107 | **shred** | 1 | 1 | - | 166.19 | - | 5,746 | - | 0.000297 | 🔵 low — common in general English | — |
| 6108 | **compa** | 1 | 1 | - | 166.19 | - | 5,747 | - | 0.000297 | 🔵 low — common in general English | — |
| 6109 | **boiled** | 1 | 1 | - | 166.19 | - | 5,748 | - | 0.000297 | 🔵 low — common in general English | — |
| 6110 | **protectors-we** | 1 | 1 | - | 166.19 | - | 5,749 | - | 0.000297 | 🔵 low — common in general English | — |
| 6111 | **bodhisat** | 1 | 1 | - | 166.19 | - | 5,750 | - | 0.000297 | 🔵 low — common in general English | — |
| 6112 | **tvas-then** | 1 | 1 | - | 166.19 | - | 5,751 | - | 0.000296 | 🔵 low — common in general English | — |
| 6113 | **gleefully** | 1 | 1 | - | 166.19 | - | 5,752 | - | 0.000296 | 🔵 low — common in general English | — |
| 6114 | **mantrayana-namely** | 1 | 1 | - | 166.19 | - | 5,753 | - | 0.000296 | 🔵 low — common in general English | — |
| 6115 | **succulent** | 1 | 1 | - | 166.19 | - | 5,754 | - | 0.000296 | 🔵 low — common in general English | — |
| 6116 | **heedlessly** | 1 | 1 | - | 166.19 | - | 5,755 | - | 0.000296 | 🔵 low — common in general English | — |
| 6117 | **slaugh** | 1 | 1 | - | 166.19 | - | 5,756 | - | 0.000296 | 🔵 low — common in general English | — |
| 6118 | **murdering** | 1 | 1 | - | 166.19 | - | 5,757 | - | 0.000296 | 🔵 low — common in general English | — |
| 6119 | **prowl** | 1 | 1 | - | 166.19 | - | 5,758 | - | 0.000296 | 🔵 low — common in general English | — |
| 6120 | **roam** | 1 | 1 | - | 166.19 | - | 5,759 | - | 0.000296 | 🔵 low — common in general English | — |
| 6121 | **gnaw** | 1 | 1 | - | 166.19 | - | 5,760 | - | 0.000296 | 🔵 low — common in general English | — |
| 6122 | **innard** | 1 | 1 | - | 166.19 | - | 5,761 | - | 0.000296 | 🔵 low — common in general English | — |
| 6123 | **lookout** | 1 | 1 | - | 166.19 | - | 5,762 | - | 0.000296 | 🔵 low — common in general English | — |
| 6124 | **killer** | 1 | 1 | - | 166.19 | - | 5,763 | - | 0.000296 | 🔵 low — common in general English | — |
| 6125 | **inflamed** | 1 | 1 | - | 166.19 | - | 5,764 | - | 0.000296 | 🔵 low — common in general English | — |
| 6126 | **shaking** | 1 | 1 | - | 166.19 | - | 5,765 | - | 0.000296 | 🔵 low — common in general English | — |
| 6127 | **intimacy** | 1 | 1 | - | 166.19 | - | 5,766 | - | 0.000296 | 🔵 low — common in general English | — |
| 6128 | **hell-unless** | 1 | 1 | - | 166.19 | - | 5,767 | - | 0.000296 | 🔵 low — common in general English | — |
| 6129 | **preying** | 1 | 1 | - | 166.19 | - | 5,768 | - | 0.000296 | 🔵 low — common in general English | — |
| 6130 | **bon** | 1 | 1 | - | 166.19 | - | 5,769 | - | 0.000296 | 🔵 low — common in general English | — |
| 6131 | **sublimity** | 1 | 1 | - | 166.19 | - | 5,770 | - | 0.000296 | 🔵 low — common in general English | — |
| 6132 | **conspicuous** | 1 | 1 | - | 166.19 | - | 5,771 | - | 0.000296 | 🔵 low — common in general English | — |
| 6133 | **encapsulate** | 1 | 1 | - | 166.19 | - | 5,772 | - | 0.000296 | 🔵 low — common in general English | — |
| 6134 | **dharmas** | 1 | 1 | - | 166.19 | - | 5,773 | - | 0.000296 | 🔵 low — common in general English | — |
| 6135 | **bared** | 1 | 1 | - | 166.19 | - | 5,774 | - | 0.000296 | 🔵 low — common in general English | — |
| 6136 | **abhid** | 1 | 1 | - | 166.19 | - | 5,775 | - | 0.000296 | 🔵 low — common in general English | — |
| 6137 | **harma** | 1 | 1 | - | 166.19 | - | 5,776 | - | 0.000296 | 🔵 low — common in general English | — |
| 6138 | **prakasasila** | 1 | 1 | - | 166.19 | - | 5,777 | - | 0.000296 | 🔵 low — common in general English | — |
| 6139 | **sarighab** | 1 | 1 | - | 166.19 | - | 5,778 | - | 0.000296 | 🔵 low — common in general English | — |
| 6140 | **kukku** | 1 | 1 | - | 166.19 | - | 5,779 | - | 0.000296 | 🔵 low — common in general English | — |
| 6141 | **apada** | 1 | 1 | - | 166.19 | - | 5,780 | - | 0.000296 | 🔵 low — common in general English | — |
| 6142 | **persistence** | 1 | 1 | - | 166.19 | - | 5,781 | - | 0.000296 | 🔵 low — common in general English | — |
| 6143 | **stroking** | 1 | 1 | - | 166.19 | - | 5,782 | - | 0.000296 | 🔵 low — common in general English | — |
| 6144 | **maggot** | 1 | 1 | - | 166.19 | - | 5,783 | - | 0.000296 | 🔵 low — common in general English | — |
| 6145 | **foreleg** | 1 | 1 | - | 166.19 | - | 5,784 | - | 0.000296 | 🔵 low — common in general English | — |
| 6146 | **halo** | 1 | 1 | - | 166.19 | - | 5,785 | - | 0.000295 | 🔵 low — common in general English | — |
| 6147 | **shoulder-all** | 1 | 1 | - | 166.19 | - | 5,786 | - | 0.000295 | 🔵 low — common in general English | — |
| 6148 | **ofmaitreya** | 1 | 1 | - | 166.19 | - | 5,787 | - | 0.000295 | 🔵 low — common in general English | — |
| 6149 | **feelings-like** | 1 | 1 | - | 166.19 | - | 5,788 | - | 0.000295 | 🔵 low — common in general English | — |
| 6150 | **contented** | 1 | 1 | - | 166.19 | - | 5,789 | - | 0.000295 | 🔵 low — common in general English | — |
| 6151 | **displeased** | 1 | 1 | - | 166.19 | - | 5,790 | - | 0.000295 | 🔵 low — common in general English | — |
| 6152 | **alarmingly** | 1 | 1 | - | 166.19 | - | 5,791 | - | 0.000295 | 🔵 low — common in general English | — |
| 6153 | **logician** | 1 | 1 | - | 166.19 | - | 5,792 | - | 0.000295 | 🔵 low — common in general English | — |
| 6154 | **tsakpuwa** | 1 | 1 | - | 166.19 | - | 5,793 | - | 0.000295 | 🔵 low — common in general English | — |
| 6155 | **deva** | 1 | 1 | - | 166.19 | - | 5,794 | - | 0.000295 | 🔵 low — common in general English | — |
| 6156 | **datta** | 1 | 1 | - | 166.19 | - | 5,795 | - | 0.000295 | 🔵 low — common in general English | — |
| 6157 | **prodigious** | 1 | 1 | - | 166.19 | - | 5,796 | - | 0.000295 | 🔵 low — common in general English | — |
| 6158 | **kunpang** | 1 | 1 | - | 166.19 | - | 5,797 | - | 0.000295 | 🔵 low — common in general English | — |
| 6159 | **rakgyal** | 1 | 1 | - | 166.19 | - | 5,798 | - | 0.000295 | 🔵 low — common in general English | — |
| 6160 | **darkened** | 1 | 1 | - | 166.19 | - | 5,799 | - | 0.000295 | 🔵 low — common in general English | — |
| 6161 | **negativity** | 1 | 1 | - | 166.19 | - | 5,800 | - | 0.000295 | 🔵 low — common in general English | — |
| 6162 | **vile** | 1 | 1 | - | 166.19 | - | 5,801 | - | 0.000295 | 🔵 low — common in general English | — |
| 6163 | **physique** | 1 | 1 | - | 166.19 | - | 5,802 | - | 0.000295 | 🔵 low — common in general English | — |
| 6164 | **correspondingly** | 1 | 1 | - | 166.19 | - | 5,803 | - | 0.000295 | 🔵 low — common in general English | — |
| 6165 | **summarize** | 1 | 1 | - | 166.19 | - | 5,804 | - | 0.000295 | 🔵 low — common in general English | — |
| 6166 | **ferryboat** | 1 | 1 | - | 166.19 | - | 5,805 | - | 0.000295 | 🔵 low — common in general English | — |
| 6167 | **jasako** | 1 | 1 | - | 166.19 | - | 5,806 | - | 0.000295 | 🔵 low — common in general English | — |
| 6168 | **materialized** | 1 | 1 | - | 166.19 | - | 5,807 | - | 0.000295 | 🔵 low — common in general English | — |
| 6169 | **beheaded** | 1 | 1 | - | 166.19 | - | 5,808 | - | 0.000295 | 🔵 low — common in general English | — |
| 6170 | **scabrous** | 1 | 1 | - | 166.19 | - | 5,809 | - | 0.000295 | 🔵 low — common in general English | — |
| 6171 | **shaven-headed** | 1 | 1 | - | 166.19 | - | 5,810 | - | 0.000295 | 🔵 low — common in general English | — |
| 6172 | **bigot** | 1 | 1 | - | 166.19 | - | 5,811 | - | 0.000295 | 🔵 low — common in general English | — |
| 6173 | **panicular** | 1 | 1 | - | 166.19 | - | 5,812 | - | 0.000295 | 🔵 low — common in general English | — |
| 6174 | **woke** | 1 | 1 | - | 166.19 | - | 5,813 | - | 0.000295 | 🔵 low — common in general English | — |
| 6175 | **benevolent** | 1 | 1 | - | 166.19 | - | 5,814 | - | 0.000295 | 🔵 low — common in general English | — |
| 6176 | **activities-prostration** | 1 | 1 | - | 166.19 | - | 5,815 | - | 0.000295 | 🔵 low — common in general English | — |
| 6177 | **circumam** | 1 | 1 | - | 166.19 | - | 5,816 | - | 0.000295 | 🔵 low — common in general English | — |
| 6178 | **bulation** | 1 | 1 | - | 166.19 | - | 5,817 | - | 0.000295 | 🔵 low — common in general English | — |
| 6179 | **hean** | 1 | 1 | - | 166.19 | - | 5,818 | - | 0.000295 | 🔵 low — common in general English | — |
| 6180 | **jackal** | 1 | 1 | - | 166.19 | - | 5,819 | - | 0.000294 | 🔵 low — common in general English | — |
| 6181 | **tative** | 1 | 1 | - | 166.19 | - | 5,820 | - | 0.000294 | 🔵 low — common in general English | — |
| 6182 | **discriminating** | 1 | 1 | - | 166.19 | - | 5,821 | - | 0.000294 | 🔵 low — common in general English | — |
| 6183 | **thusness** | 1 | 1 | - | 166.19 | - | 5,822 | - | 0.000294 | 🔵 low — common in general English | ✓ དེ་བཞིན་ཉིད |
| 6184 | **foundering** | 1 | 1 | - | 166.19 | - | 5,823 | - | 0.000294 | 🔵 low — common in general English | — |
| 6185 | **friendless** | 1 | 1 | - | 166.19 | - | 5,824 | - | 0.000294 | 🔵 low — common in general English | — |
| 6186 | **binh** | 1 | 1 | - | 166.19 | - | 5,825 | - | 0.000294 | 🔵 low — common in general English | — |
| 6187 | **suvarl** | 1 | 1 | - | 166.19 | - | 5,826 | - | 0.000294 | 🔵 low — common in general English | — |
| 6188 | **advipa** | 1 | 1 | - | 166.19 | - | 5,827 | - | 0.000294 | 🔵 low — common in general English | — |
| 6189 | **suvarnadvipa** | 1 | 1 | - | 166.19 | - | 5,828 | - | 0.000294 | 🔵 low — common in general English | ~ |
| 6190 | **swindle** | 1 | 1 | - | 166.19 | - | 5,829 | - | 0.000294 | 🔵 low — common in general English | — |
| 6191 | **either-try** | 1 | 1 | - | 166.19 | - | 5,830 | - | 0.000294 | 🔵 low — common in general English | — |
| 6192 | **pinprick** | 1 | 1 | - | 166.19 | - | 5,831 | - | 0.000294 | 🔵 low — common in general English | — |
| 6193 | **pain-we** | 1 | 1 | - | 166.19 | - | 5,832 | - | 0.000294 | 🔵 low — common in general English | — |
| 6194 | **thumbnail** | 1 | 1 | - | 166.19 | - | 5,833 | - | 0.000294 | 🔵 low — common in general English | — |
| 6195 | **enslaved** | 1 | 1 | - | 166.19 | - | 5,834 | - | 0.000294 | 🔵 low — common in general English | — |
| 6196 | **trungpa** | 1 | 1 | - | 166.19 | - | 5,835 | - | 0.000294 | 🔵 low — common in general English | — |
| 6197 | **sinachen** | 1 | 1 | - | 166.19 | - | 5,836 | - | 0.000294 | 🔵 low — common in general English | — |
| 6198 | **kamarupa** | 1 | 1 | - | 166.19 | - | 5,837 | - | 0.000294 | 🔵 low — common in general English | — |
| 6199 | **goaded** | 1 | 1 | - | 166.19 | - | 5,838 | - | 0.000294 | 🔵 low — common in general English | — |
| 6200 | **kamarapa** | 1 | 1 | - | 166.19 | - | 5,839 | - | 0.000294 | 🔵 low — common in general English | — |
| 6201 | **cart** | 1 | 1 | - | 166.19 | - | 5,840 | - | 0.000294 | 🔵 low — common in general English | — |
| 6202 | **sea-captain** | 1 | 1 | - | 166.19 | - | 5,841 | - | 0.000294 | 🔵 low — common in general English | — |
| 6203 | **mercha** | 1 | 1 | - | 166.19 | - | 5,842 | - | 0.000294 | 🔵 low — common in general English | — |
| 6204 | **plank** | 1 | 1 | - | 166.19 | - | 5,843 | - | 0.000294 | 🔵 low — common in general English | — |
| 6205 | **ashore** | 1 | 1 | - | 166.19 | - | 5,844 | - | 0.000294 | 🔵 low — common in general English | — |
| 6206 | **intoxication** | 1 | 1 | - | 166.19 | - | 5,845 | - | 0.000294 | 🔵 low — common in general English | — |
| 6207 | **ravishingly** | 1 | 1 | - | 166.19 | - | 5,846 | - | 0.000294 | 🔵 low — common in general English | — |
| 6208 | **couch** | 1 | 1 | - | 166.19 | - | 5,847 | - | 0.000294 | 🔵 low — common in general English | — |
| 6209 | **pulver** | 1 | 1 | - | 166.19 | - | 5,848 | - | 0.000294 | 🔵 low — common in general English | — |
| 6210 | **ized** | 1 | 1 | - | 166.19 | - | 5,849 | - | 0.000294 | 🔵 low — common in general English | — |
| 6211 | **smashed** | 1 | 1 | - | 166.19 | - | 5,850 | - | 0.000294 | 🔵 low — common in general English | — |
| 6212 | **ulti** | 1 | 1 | - | 166.19 | - | 5,851 | - | 0.000294 | 🔵 low — common in general English | — |
| 6213 | **mate** | 1 | 1 | - | 166.19 | - | 5,852 | - | 0.000294 | 🔵 low — common in general English | — |
| 6214 | **chak** | 1 | 1 | - | 166.19 | - | 5,853 | - | 0.000294 | 🔵 low — common in general English | — |
| 6215 | **shingwa** | 1 | 1 | - | 166.19 | - | 5,854 | - | 0.000293 | 🔵 low — common in general English | — |
| 6216 | **langthang** | 1 | 1 | - | 166.19 | - | 5,855 | - | 0.000293 | 🔵 low — common in general English | — |
| 6217 | **succe** | 1 | 1 | - | 166.19 | - | 5,856 | - | 0.000293 | 🔵 low — common in general English | — |
| 6218 | **sor** | 1 | 1 | - | 166.19 | - | 5,857 | - | 0.000293 | 🔵 low — common in general English | — |
| 6219 | **stfipa** | 1 | 1 | - | 166.19 | - | 5,858 | - | 0.000293 | 🔵 low — common in general English | — |
| 6220 | **selfishness** | 1 | 1 | - | 166.19 | - | 5,859 | - | 0.000293 | 🔵 low — common in general English | — |
| 6221 | **subjugating** | 1 | 1 | - | 166.19 | - | 5,860 | - | 0.000293 | 🔵 low — common in general English | — |
| 6222 | **vaibhasika** | 1 | 1 | - | 166.19 | - | 5,861 | - | 0.000293 | 🔵 low — common in general English | — |
| 6223 | **cine-the** | 1 | 1 | - | 166.19 | - | 5,862 | - | 0.000293 | 🔵 low — common in general English | — |
| 6224 | **dozed** | 1 | 1 | - | 166.19 | - | 5,863 | - | 0.000293 | 🔵 low — common in general English | — |
| 6225 | **spat** | 1 | 1 | - | 166.19 | - | 5,864 | - | 0.000293 | 🔵 low — common in general English | — |
| 6226 | **scar** | 1 | 1 | - | 166.19 | - | 5,865 | - | 0.000293 | 🔵 low — common in general English | — |
| 6227 | **treatis** | 1 | 1 | - | 166.19 | - | 5,866 | - | 0.000293 | 🔵 low — common in general English | — |
| 6228 | **ceaselessly** | 1 | 1 | - | 166.19 | - | 5,867 | - | 0.000293 | 🔵 low — common in general English | — |
| 6229 | **donned** | 1 | 1 | - | 166.19 | - | 5,868 | - | 0.000293 | 🔵 low — common in general English | — |
| 6230 | **fervently** | 1 | 1 | - | 166.19 | - | 5,869 | - | 0.000293 | 🔵 low — common in general English | — |
| 6231 | **nivritta** | 1 | 1 | - | 166.19 | - | 5,870 | - | 0.000293 | 🔵 low — common in general English | — |
| 6232 | **palace-one** | 1 | 1 | - | 166.19 | - | 5,871 | - | 0.000293 | 🔵 low — common in general English | — |
| 6233 | **cubits-and** | 1 | 1 | - | 166.19 | - | 5,872 | - | 0.000293 | 🔵 low — common in general English | — |
| 6234 | **alternately** | 1 | 1 | - | 166.19 | - | 5,873 | - | 0.000293 | 🔵 low — common in general English | — |
| 6235 | **ketaka** | 1 | 1 | - | 166.19 | - | 5,874 | - | 0.000293 | 🔵 low — common in general English | — |
| 6236 | **saketa** | 1 | 1 | - | 166.19 | - | 5,875 | - | 0.000293 | 🔵 low — common in general English | — |
| 6237 | **largesse** | 1 | 1 | - | 166.19 | - | 5,876 | - | 0.000293 | 🔵 low — common in general English | — |
| 6238 | **organize** | 1 | 1 | - | 166.19 | - | 5,877 | - | 0.000293 | 🔵 low — common in general English | — |
| 6239 | **yanta** | 1 | 1 | - | 166.19 | - | 5,878 | - | 0.000293 | 🔵 low — common in general English | — |
| 6240 | **hard-to** | 1 | 1 | - | 166.19 | - | 5,879 | - | 0.000293 | 🔵 low — common in general English | — |
| 6241 | **raksasa** | 1 | 1 | - | 166.19 | - | 5,880 | - | 0.000293 | 🔵 low — common in general English | — |
| 6242 | **oblation** | 1 | 1 | - | 166.19 | - | 5,881 | - | 0.000293 | 🔵 low — common in general English | — |
| 6243 | **smitten** | 1 | 1 | - | 166.19 | - | 5,882 | - | 0.000293 | 🔵 low — common in general English | — |
| 6244 | **grief** | 1 | 1 | - | 166.19 | - | 5,883 | - | 0.000293 | 🔵 low — common in general English | — |
| 6245 | **ter** | 1 | 1 | - | 166.19 | - | 5,884 | - | 0.000293 | 🔵 low — common in general English | — |
| 6246 | **veda** | 1 | 1 | - | 166.19 | - | 5,885 | - | 0.000293 | 🔵 low — common in general English | — |
| 6247 | **coveting** | 1 | 1 | - | 166.19 | - | 5,886 | - | 0.000293 | 🔵 low — common in general English | — |
| 6248 | **enchantment** | 1 | 1 | - | 166.19 | - | 5,887 | - | 0.000293 | 🔵 low — common in general English | — |
| 6249 | **it-for** | 1 | 1 | - | 166.19 | - | 5,888 | - | 0.000293 | 🔵 low — common in general English | — |
| 6250 | **queen-hi** | 1 | 1 | - | 166.19 | - | 5,889 | - | 0.000292 | 🔵 low — common in general English | — |
| 6251 | **wife-in** | 1 | 1 | - | 166.19 | - | 5,890 | - | 0.000292 | 🔵 low — common in general English | — |
| 6252 | **curse** | 1 | 1 | - | 166.19 | - | 5,891 | - | 0.000292 | 🔵 low — common in general English | — |
| 6253 | **unreliable** | 1 | 1 | - | 166.19 | - | 5,892 | - | 0.000292 | 🔵 low — common in general English | — |
| 6254 | **numer** | 1 | 1 | - | 166.19 | - | 5,893 | - | 0.000292 | 🔵 low — common in general English | — |
| 6255 | **ous** | 1 | 1 | - | 166.19 | - | 5,894 | - | 0.000292 | 🔵 low — common in general English | — |
| 6256 | **wasn** | 1 | 1 | - | 166.19 | - | 5,895 | - | 0.000292 | 🔵 low — common in general English | — |
| 6257 | **perfections-generosity** | 1 | 1 | - | 166.19 | - | 5,896 | - | 0.000292 | 🔵 low — common in general English | — |
| 6258 | **concentration-are** | 1 | 1 | - | 166.19 | - | 5,897 | - | 0.000292 | 🔵 low — common in general English | — |
| 6259 | **masterful** | 1 | 1 | - | 166.19 | - | 5,898 | - | 0.000292 | 🔵 low — common in general English | — |
| 6260 | **moan** | 1 | 1 | - | 166.19 | - | 5,899 | - | 0.000292 | 🔵 low — common in general English | — |
| 6261 | **starvation** | 1 | 1 | - | 166.19 | - | 5,900 | - | 0.000292 | 🔵 low — common in general English | — |
| 6262 | **preta-realm** | 1 | 1 | - | 166.19 | - | 5,901 | - | 0.000292 | 🔵 low — common in general English | — |
| 6263 | **daring** | 1 | 1 | - | 166.19 | - | 5,902 | - | 0.000292 | 🔵 low — common in general English | — |
| 6264 | **gladly** | 1 | 1 | - | 166.19 | - | 5,903 | - | 0.000292 | 🔵 low — common in general English | — |
| 6265 | **cunning** | 1 | 1 | - | 166.19 | - | 5,904 | - | 0.000292 | 🔵 low — common in general English | — |
| 6266 | **mandabhadri** | 1 | 1 | - | 166.19 | - | 5,905 | - | 0.000292 | 🔵 low — common in general English | — |
| 6267 | **brewed** | 1 | 1 | - | 166.19 | - | 5,906 | - | 0.000292 | 🔵 low — common in general English | — |
| 6268 | **emptying** | 1 | 1 | - | 166.19 | - | 5,907 | - | 0.000292 | 🔵 low — common in general English | — |
| 6269 | **expound** | 1 | 1 | - | 166.19 | - | 5,908 | - | 0.000292 | 🔵 low — common in general English | — |
| 6270 | **evil-doing** | 1 | 1 | - | 166.19 | - | 5,909 | - | 0.000292 | 🔵 low — common in general English | — |
| 6271 | **undertak** | 1 | 1 | - | 166.19 | - | 5,910 | - | 0.000292 | 🔵 low — common in general English | — |
| 6272 | **actions-even** | 1 | 1 | - | 166.19 | - | 5,911 | - | 0.000292 | 🔵 low — common in general English | — |
| 6273 | **amusing** | 1 | 1 | - | 166.19 | - | 5,912 | - | 0.000292 | 🔵 low — common in general English | — |
| 6274 | **wronged** | 1 | 1 | - | 166.19 | - | 5,913 | - | 0.000292 | 🔵 low — common in general English | — |
| 6275 | **slandered** | 1 | 1 | - | 166.19 | - | 5,914 | - | 0.000292 | 🔵 low — common in general English | — |
| 6276 | **shatter** | 1 | 1 | - | 166.19 | - | 5,915 | - | 0.000292 | 🔵 low — common in general English | — |
| 6277 | **zeal** | 1 | 1 | - | 166.19 | - | 5,916 | - | 0.000292 | 🔵 low — common in general English | — |
| 6278 | **accus** | 1 | 1 | - | 166.19 | - | 5,917 | - | 0.000292 | 🔵 low — common in general English | — |
| 6279 | **unjustly** | 1 | 1 | - | 166.19 | - | 5,918 | - | 0.000292 | 🔵 low — common in general English | — |
| 6280 | **effect-a** | 1 | 1 | - | 166.19 | - | 5,919 | - | 0.000292 | 🔵 low — common in general English | — |
| 6281 | **grudge-will** | 1 | 1 | - | 166.19 | - | 5,920 | - | 0.000292 | 🔵 low — common in general English | — |
| 6282 | **anger-so** | 1 | 1 | - | 166.19 | - | 5,921 | - | 0.000292 | 🔵 low — common in general English | — |
| 6283 | **puff** | 1 | 1 | - | 166.19 | - | 5,922 | - | 0.000292 | 🔵 low — common in general English | — |
| 6284 | **humiliated** | 1 | 1 | - | 166.19 | - | 5,923 | - | 0.000292 | 🔵 low — common in general English | — |
| 6285 | **touchiness** | 1 | 1 | - | 166.19 | - | 5,924 | - | 0.000292 | 🔵 low — common in general English | — |
| 6286 | **admiringly** | 1 | 1 | - | 166.19 | - | 5,925 | - | 0.000291 | 🔵 low — common in general English | — |
| 6287 | **marry** | 1 | 1 | - | 166.19 | - | 5,926 | - | 0.000291 | 🔵 low — common in general English | — |
| 6288 | **sew** | 1 | 1 | - | 166.19 | - | 5,927 | - | 0.000291 | 🔵 low — common in general English | — |
| 6289 | **double-pointed** | 1 | 1 | - | 166.19 | - | 5,928 | - | 0.000291 | 🔵 low — common in general English | — |
| 6290 | **nairaftjana** | 1 | 1 | - | 166.19 | - | 5,929 | - | 0.000291 | 🔵 low — common in general English | — |
| 6291 | **asceticism** | 1 | 1 | - | 166.19 | - | 5,930 | - | 0.000291 | 🔵 low — common in general English | — |
| 6292 | **nettle** | 1 | 1 | - | 166.19 | - | 5,931 | - | 0.000291 | 🔵 low — common in general English | — |
| 6293 | **greenish** | 1 | 1 | - | 166.19 | - | 5,932 | - | 0.000291 | 🔵 low — common in general English | — |
| 6294 | **tenaciously** | 1 | 1 | - | 166.19 | - | 5,933 | - | 0.000291 | 🔵 low — common in general English | — |
| 6295 | **hopeless** | 1 | 1 | - | 166.19 | - | 5,934 | - | 0.000291 | 🔵 low — common in general English | — |
| 6296 | **melong** | 1 | 1 | - | 166.19 | - | 5,935 | - | 0.000291 | 🔵 low — common in general English | ~ |
| 6297 | **practi** | 1 | 1 | - | 166.19 | - | 5,936 | - | 0.000291 | 🔵 low — common in general English | — |
| 6298 | **bark** | 1 | 1 | - | 166.19 | - | 5,937 | - | 0.000291 | 🔵 low — common in general English | — |
| 6299 | **lakhe** | 1 | 1 | - | 166.19 | - | 5,938 | - | 0.000291 | 🔵 low — common in general English | ✓ གླ་ཁེ |
| 6300 | **rabjam** | 1 | 1 | - | 166.19 | - | 5,939 | - | 0.000291 | 🔵 low — common in general English | — |
| 6301 | **snowed** | 1 | 1 | - | 166.19 | - | 5,940 | - | 0.000291 | 🔵 low — common in general English | — |
| 6302 | **well-be** | 1 | 1 | - | 166.19 | - | 5,941 | - | 0.000291 | 🔵 low — common in general English | — |
| 6303 | **mourn** | 1 | 1 | - | 166.19 | - | 5,942 | - | 0.000291 | 🔵 low — common in general English | — |
| 6304 | **gristle** | 1 | 1 | - | 166.19 | - | 5,943 | - | 0.000291 | 🔵 low — common in general English | — |
| 6305 | **vom** | 1 | 1 | - | 166.19 | - | 5,944 | - | 0.000291 | 🔵 low — common in general English | — |
| 6306 | **ited** | 1 | 1 | - | 166.19 | - | 5,945 | - | 0.000291 | 🔵 low — common in general English | — |
| 6307 | **recount** | 1 | 1 | - | 166.19 | - | 5,946 | - | 0.000291 | 🔵 low — common in general English | — |
| 6308 | **bod** | 1 | 1 | - | 166.19 | - | 5,947 | - | 0.000291 | 🔵 low — common in general English | — |
| 6309 | **hisattva** | 1 | 1 | - | 166.19 | - | 5,948 | - | 0.000291 | 🔵 low — common in general English | — |
| 6310 | **hardhip** | 1 | 1 | - | 166.19 | - | 5,949 | - | 0.000291 | 🔵 low — common in general English | — |
| 6311 | **druk** | 1 | 1 | - | 166.19 | - | 5,950 | - | 0.000291 | 🔵 low — common in general English | ~ |
| 6312 | **karpo** | 1 | 1 | - | 166.19 | - | 5,951 | - | 0.000291 | 🔵 low — common in general English | ~ |
| 6313 | **unhurriedly** | 1 | 1 | - | 166.19 | - | 5,952 | - | 0.000291 | 🔵 low — common in general English | — |
| 6314 | **beware** | 1 | 1 | - | 166.19 | - | 5,953 | - | 0.000291 | 🔵 low — common in general English | — |
| 6315 | **deathbed** | 1 | 1 | - | 166.19 | - | 5,954 | - | 0.000291 | 🔵 low — common in general English | — |
| 6316 | **immedi** | 1 | 1 | - | 166.19 | - | 5,955 | - | 0.000291 | 🔵 low — common in general English | — |
| 6317 | **ately** | 1 | 1 | - | 166.19 | - | 5,956 | - | 0.000291 | 🔵 low — common in general English | — |
| 6318 | **coward** | 1 | 1 | - | 166.19 | - | 5,957 | - | 0.000291 | 🔵 low — common in general English | — |
| 6319 | **dancing-girl** | 1 | 1 | - | 166.19 | - | 5,958 | - | 0.000291 | 🔵 low — common in general English | — |
| 6320 | **time-one** | 1 | 1 | - | 166.19 | - | 5,959 | - | 0.000291 | 🔵 low — common in general English | — |
| 6321 | **them-such** | 1 | 1 | - | 166.19 | - | 5,960 | - | 0.000291 | 🔵 low — common in general English | — |
| 6322 | **clump** | 1 | 1 | - | 166.19 | - | 5,961 | - | 0.000290 | 🔵 low — common in general English | — |
| 6323 | **idleness** | 1 | 1 | - | 166.19 | - | 5,962 | - | 0.000290 | 🔵 low — common in general English | — |
| 6324 | **tenacity** | 1 | 1 | - | 166.19 | - | 5,963 | - | 0.000290 | 🔵 low — common in general English | — |
| 6325 | **reputed** | 1 | 1 | - | 166.19 | - | 5,964 | - | 0.000290 | 🔵 low — common in general English | — |
| 6326 | **sporadically** | 1 | 1 | - | 166.19 | - | 5,965 | - | 0.000290 | 🔵 low — common in general English | — |
| 6327 | **excite** | 1 | 1 | - | 166.19 | - | 5,966 | - | 0.000290 | 🔵 low — common in general English | — |
| 6328 | **spous** | 1 | 1 | - | 166.19 | - | 5,967 | - | 0.000290 | 🔵 low — common in general English | — |
| 6329 | **relatives-even** | 1 | 1 | - | 166.19 | - | 5,968 | - | 0.000290 | 🔵 low — common in general English | — |
| 6330 | **birth-are** | 1 | 1 | - | 166.19 | - | 5,969 | - | 0.000290 | 🔵 low — common in general English | — |
| 6331 | **shiwa** | 1 | 1 | - | 166.19 | - | 5,970 | - | 0.000290 | 🔵 low — common in general English | ~ |
| 6332 | **heedless** | 1 | 1 | - | 166.19 | - | 5,971 | - | 0.000290 | 🔵 low — common in general English | — |
| 6333 | **trifling** | 1 | 1 | - | 166.19 | - | 5,972 | - | 0.000290 | 🔵 low — common in general English | — |
| 6334 | **forethought** | 1 | 1 | - | 166.19 | - | 5,973 | - | 0.000290 | 🔵 low — common in general English | — |
| 6335 | **roving** | 1 | 1 | - | 166.19 | - | 5,974 | - | 0.000290 | 🔵 low — common in general English | — |
| 6336 | **squandered** | 1 | 1 | - | 166.19 | - | 5,975 | - | 0.000290 | 🔵 low — common in general English | — |
| 6337 | **academia** | 1 | 1 | - | 166.19 | - | 5,976 | - | 0.000290 | 🔵 low — common in general English | — |
| 6338 | **path-disenchantment** | 1 | 1 | - | 166.19 | - | 5,977 | - | 0.000290 | 🔵 low — common in general English | — |
| 6339 | **absorption-arise** | 1 | 1 | - | 166.19 | - | 5,978 | - | 0.000290 | 🔵 low — common in general English | — |
| 6340 | **natu** | 1 | 1 | - | 166.19 | - | 5,979 | - | 0.000290 | 🔵 low — common in general English | — |
| 6341 | **tranquillity** | 1 | 1 | - | 166.19 | - | 5,980 | - | 0.000290 | 🔵 low — common in general English | — |
| 6342 | **bustling** | 1 | 1 | - | 166.19 | - | 5,981 | - | 0.000290 | 🔵 low — common in general English | — |
| 6343 | **dispensed** | 1 | 1 | - | 166.19 | - | 5,982 | - | 0.000290 | 🔵 low — common in general English | — |
| 6344 | **fascinated** | 1 | 1 | - | 166.19 | - | 5,983 | - | 0.000290 | 🔵 low — common in general English | — |
| 6345 | **concept-free** | 1 | 1 | - | 166.19 | - | 5,984 | - | 0.000290 | 🔵 low — common in general English | — |
| 6346 | **ofvairocana** | 1 | 1 | - | 166.19 | - | 5,985 | - | 0.000290 | 🔵 low — common in general English | — |
| 6347 | **concentra** | 1 | 1 | - | 166.19 | - | 5,986 | - | 0.000290 | 🔵 low — common in general English | — |
| 6348 | **confining** | 1 | 1 | - | 166.19 | - | 5,987 | - | 0.000290 | 🔵 low — common in general English | — |
| 6349 | **substantiality** | 1 | 1 | - | 166.19 | - | 5,988 | - | 0.000290 | 🔵 low — common in general English | — |
| 6350 | **gandharva** | 1 | 1 | - | 166.19 | - | 5,989 | - | 0.000290 | 🔵 low — common in general English | ✓ དྲི་ཟ |
| 6351 | **them-the** | 1 | 1 | - | 166.19 | - | 5,990 | - | 0.000290 | 🔵 low — common in general English | — |
| 6352 | **scendent** | 1 | 1 | - | 166.19 | - | 5,991 | - | 0.000290 | 🔵 low — common in general English | — |
| 6353 | **twenty-two** | 1 | 1 | - | 166.19 | - | 5,992 | - | 0.000290 | 🔵 low — common in general English | — |
| 6354 | **thirty-six** | 1 | 1 | - | 166.19 | - | 5,993 | - | 0.000290 | 🔵 low — common in general English | — |
| 6355 | **contami** | 1 | 1 | - | 166.19 | - | 5,994 | - | 0.000290 | 🔵 low — common in general English | — |
| 6356 | **nate** | 1 | 1 | - | 166.19 | - | 5,995 | - | 0.000290 | 🔵 low — common in general English | — |
| 6357 | **self-aggrandizement** | 1 | 1 | - | 166.19 | - | 5,996 | - | 0.000290 | 🔵 low — common in general English | — |
| 6358 | **pline** | 1 | 1 | - | 166.19 | - | 5,997 | - | 0.000289 | 🔵 low — common in general English | — |
| 6359 | **giving-offering** | 1 | 1 | - | 166.19 | - | 5,998 | - | 0.000289 | 🔵 low — common in general English | — |
| 6360 | **tiring** | 1 | 1 | - | 166.19 | - | 5,999 | - | 0.000289 | 🔵 low — common in general English | — |
| 6361 | **subdivision** | 1 | 1 | - | 166.19 | - | 6,000 | - | 0.000289 | 🔵 low — common in general English | — |
| 6362 | **summing** | 1 | 1 | - | 166.19 | - | 6,001 | - | 0.000289 | 🔵 low — common in general English | — |
| 6363 | **guile** | 1 | 1 | - | 166.19 | - | 6,002 | - | 0.000289 | 🔵 low — common in general English | — |
| 6364 | **non-attachment** | 1 | 1 | - | 166.19 | - | 6,003 | - | 0.000289 | 🔵 low — common in general English | — |
| 6365 | **contentment** | 1 | 1 | - | 166.19 | - | 6,004 | - | 0.000289 | 🔵 low — common in general English | — |
| 6366 | **thinker** | 1 | 1 | - | 166.19 | - | 6,005 | - | 0.000289 | 🔵 low — common in general English | — |
| 6367 | **nutshell** | 1 | 1 | - | 166.19 | - | 6,006 | - | 0.000289 | 🔵 low — common in general English | — |
| 6368 | **nirvina** | 1 | 1 | - | 166.19 | - | 6,007 | - | 0.000289 | 🔵 low — common in general English | — |
| 6369 | **non-dwelling** | 1 | 1 | - | 166.19 | - | 6,008 | - | 0.000289 | 🔵 low — common in general English | — |
| 6370 | **grasped** | 1 | 1 | - | 166.19 | - | 6,009 | - | 0.000289 | 🔵 low — common in general English | — |
| 6371 | **conceptualize** | 1 | 1 | - | 166.19 | - | 6,010 | - | 0.000289 | 🔵 low — common in general English | — |
| 6372 | **bodhicitta-emptiness** | 1 | 1 | - | 166.19 | - | 6,011 | - | 0.000289 | 🔵 low — common in general English | — |
| 6373 | **nnhika** | 1 | 1 | - | 166.19 | - | 6,012 | - | 0.000289 | 🔵 low — common in general English | — |
| 6374 | **relegate** | 1 | 1 | - | 166.19 | - | 6,013 | - | 0.000289 | 🔵 low — common in general English | — |
| 6375 | **bodhi** | 1 | 1 | - | 166.19 | - | 6,014 | - | 0.000289 | 🔵 low — common in general English | — |
| 6376 | **citta** | 1 | 1 | - | 166.19 | - | 6,015 | - | 0.000289 | 🔵 low — common in general English | — |
| 6377 | **intensively** | 1 | 1 | - | 166.19 | - | 6,016 | - | 0.000289 | 🔵 low — common in general English | — |
| 6378 | **frescoe** | 1 | 1 | - | 166.19 | - | 6,017 | - | 0.000289 | 🔵 low — common in general English | — |
| 6379 | **plastered** | 1 | 1 | - | 166.19 | - | 6,018 | - | 0.000289 | 🔵 low — common in general English | — |
| 6380 | **sincerest** | 1 | 1 | - | 166.19 | - | 6,019 | - | 0.000289 | 🔵 low — common in general English | — |
| 6381 | **unimpeded** | 1 | 1 | - | 166.19 | - | 6,020 | - | 0.000289 | 🔵 low — common in general English | — |
| 6382 | **miracles-if** | 1 | 1 | - | 166.19 | - | 6,021 | - | 0.000289 | 🔵 low — common in general English | — |
| 6383 | **be-realization** | 1 | 1 | - | 166.19 | - | 6,022 | - | 0.000289 | 🔵 low — common in general English | — |
| 6384 | **on-you** | 1 | 1 | - | 166.19 | - | 6,023 | - | 0.000289 | 🔵 low — common in general English | — |
| 6385 | **askedjetsun** | 1 | 1 | - | 166.19 | - | 6,024 | - | 0.000289 | 🔵 low — common in general English | — |
| 6386 | **disso** | 1 | 1 | - | 166.19 | - | 6,025 | - | 0.000289 | 🔵 low — common in general English | — |
| 6387 | **ciating** | 1 | 1 | - | 166.19 | - | 6,026 | - | 0.000289 | 🔵 low — common in general English | — |
| 6388 | **nyethang** | 1 | 1 | - | 166.19 | - | 6,027 | - | 0.000289 | 🔵 low — common in general English | — |
| 6389 | **kyung** | 1 | 1 | - | 166.19 | - | 6,028 | - | 0.000289 | 🔵 low — common in general English | — |
| 6390 | **lhangtsang** | 1 | 1 | - | 166.19 | - | 6,029 | - | 0.000289 | 🔵 low — common in general English | — |
| 6391 | **discursive** | 1 | 1 | - | 166.19 | - | 6,030 | - | 0.000289 | 🔵 low — common in general English | — |
| 6392 | **dividing** | 1 | 1 | - | 166.19 | - | 6,031 | - | 0.000289 | 🔵 low — common in general English | — |
| 6393 | **chegom** | 1 | 1 | - | 166.19 | - | 6,032 | - | 0.000289 | 🔵 low — common in general English | — |
| 6394 | **indivi** | 1 | 1 | - | 166.19 | - | 6,033 | - | 0.000289 | 🔵 low — common in general English | — |
| 6395 | **ible** | 1 | 1 | - | 166.19 | - | 6,034 | - | 0.000288 | 🔵 low — common in general English | — |
| 6396 | **non-conceptualization** | 1 | 1 | - | 166.19 | - | 6,035 | - | 0.000288 | 🔵 low — common in general English | — |
| 6397 | **non-action** | 1 | 1 | - | 166.19 | - | 6,036 | - | 0.000288 | 🔵 low — common in general English | ✓ |
| 6398 | **churn** | 1 | 1 | - | 166.19 | - | 6,037 | - | 0.000288 | 🔵 low — common in general English | — |
| 6399 | **purport** | 1 | 1 | - | 166.19 | - | 6,038 | - | 0.000288 | 🔵 low — common in general English | — |
| 6400 | **actions-except** | 1 | 1 | - | 166.19 | - | 6,039 | - | 0.000288 | 🔵 low — common in general English | — |
| 6401 | **actions-be** | 1 | 1 | - | 166.19 | - | 6,040 | - | 0.000288 | 🔵 low — common in general English | — |
| 6402 | **samayas-there** | 1 | 1 | - | 166.19 | - | 6,041 | - | 0.000288 | 🔵 low — common in general English | — |
| 6403 | **atapa** | 1 | 1 | - | 166.19 | - | 6,042 | - | 0.000288 | 🔵 low — common in general English | — |
| 6404 | **ninety-nine** | 1 | 1 | - | 166.19 | - | 6,043 | - | 0.000288 | 🔵 low — common in general English | — |
| 6405 | **carelessly** | 1 | 1 | - | 166.19 | - | 6,044 | - | 0.000288 | 🔵 low — common in general English | — |
| 6406 | **attentive** | 1 | 1 | - | 166.19 | - | 6,045 | - | 0.000288 | 🔵 low — common in general English | — |
| 6407 | **darsaka** | 1 | 1 | - | 166.19 | - | 6,046 | - | 0.000288 | 🔵 low — common in general English | — |
| 6408 | **sailkara** | 1 | 1 | - | 166.19 | - | 6,047 | - | 0.000288 | 🔵 low — common in general English | — |
| 6409 | **mouthing** | 1 | 1 | - | 166.19 | - | 6,048 | - | 0.000288 | 🔵 low — common in general English | — |
| 6410 | **anti** | 1 | 1 | - | 166.19 | - | 6,049 | - | 0.000288 | 🔵 low — common in general English | — |
| 6411 | **dote** | 1 | 1 | - | 166.19 | - | 6,050 | - | 0.000288 | 🔵 low — common in general English | — |
| 6412 | **buddhas-in** | 1 | 1 | - | 166.19 | - | 6,051 | - | 0.000288 | 🔵 low — common in general English | — |
| 6413 | **appli** | 1 | 1 | - | 166.19 | - | 6,052 | - | 0.000288 | 🔵 low — common in general English | — |
| 6414 | **cation** | 1 | 1 | - | 166.19 | - | 6,053 | - | 0.000288 | 🔵 low — common in general English | — |
| 6415 | **peril** | 1 | 1 | - | 166.19 | - | 6,054 | - | 0.000288 | 🔵 low — common in general English | — |
| 6416 | **dreadful** | 1 | 1 | - | 166.19 | - | 6,055 | - | 0.000288 | 🔵 low — common in general English | — |
| 6417 | **wickedness** | 1 | 1 | - | 166.19 | - | 6,056 | - | 0.000288 | 🔵 low — common in general English | — |
| 6418 | **concealing** | 1 | 1 | - | 166.19 | - | 6,057 | - | 0.000288 | 🔵 low — common in general English | — |
| 6419 | **trepidation** | 1 | 1 | - | 166.19 | - | 6,058 | - | 0.000288 | 🔵 low — common in general English | — |
| 6420 | **sukhavati** | 1 | 1 | - | 166.19 | - | 6,059 | - | 0.000288 | 🔵 low — common in general English | — |
| 6421 | **disillusioned** | 1 | 1 | - | 166.19 | - | 6,060 | - | 0.000288 | 🔵 low — common in general English | — |
| 6422 | **vajrasattva-purification** | 1 | 1 | - | 166.19 | - | 6,061 | - | 0.000288 | 🔵 low — common in general English | — |
| 6423 | **signify** | 1 | 1 | - | 166.19 | - | 6,062 | - | 0.000288 | 🔵 low — common in general English | — |
| 6424 | **fifteenth** | 1 | 1 | - | 166.19 | - | 6,063 | - | 0.000288 | 🔵 low — common in general English | — |
| 6425 | **reabsorb** | 1 | 1 | - | 166.19 | - | 6,064 | - | 0.000288 | 🔵 low — common in general English | — |
| 6426 | **sambhogakaya-the** | 1 | 1 | - | 166.19 | - | 6,065 | - | 0.000288 | 🔵 low — common in general English | — |
| 6427 | **headband** | 1 | 1 | - | 166.19 | - | 6,066 | - | 0.000288 | 🔵 low — common in general English | — |
| 6428 | **scarf** | 1 | 1 | - | 166.19 | - | 6,067 | - | 0.000288 | 🔵 low — common in general English | — |
| 6429 | **earring** | 1 | 1 | - | 166.19 | - | 6,068 | - | 0.000288 | 🔵 low — common in general English | — |
| 6430 | **armlet** | 1 | 1 | - | 166.19 | - | 6,069 | - | 0.000288 | 🔵 low — common in general English | — |
| 6431 | **bracelet** | 1 | 1 | - | 166.19 | - | 6,070 | - | 0.000288 | 🔵 low — common in general English | — |
| 6432 | **anklet** | 1 | 1 | - | 166.19 | - | 6,071 | - | 0.000287 | 🔵 low — common in general English | — |
| 6433 | **vajratopa** | 1 | 1 | - | 166.19 | - | 6,072 | - | 0.000287 | 🔵 low — common in general English | — |
| 6434 | **vividly** | 1 | 1 | - | 166.19 | - | 6,073 | - | 0.000287 | 🔵 low — common in general English | — |
| 6435 | **tangka** | 1 | 1 | - | 166.19 | - | 6,074 | - | 0.000287 | 🔵 low — common in general English | ✓ ཐང་ཀ |
| 6436 | **fresco** | 1 | 1 | - | 166.19 | - | 6,075 | - | 0.000287 | 🔵 low — common in general English | — |
| 6437 | **inert** | 1 | 1 | - | 166.19 | - | 6,076 | - | 0.000287 | 🔵 low — common in general English | — |
| 6438 | **pupil** | 1 | 1 | - | 166.19 | - | 6,077 | - | 0.000287 | 🔵 low — common in general English | — |
| 6439 | **atom** | 1 | 1 | - | 166.19 | - | 6,078 | - | 0.000287 | 🔵 low — common in general English | — |
| 6440 | **transgre** | 1 | 1 | - | 166.19 | - | 6,079 | - | 0.000287 | 🔵 low — common in general English | — |
| 6441 | **dishonourable** | 1 | 1 | - | 166.19 | - | 6,080 | - | 0.000287 | 🔵 low — common in general English | — |
| 6442 | **gooseflesh** | 1 | 1 | - | 166.19 | - | 6,081 | - | 0.000287 | 🔵 low — common in general English | — |
| 6443 | **glistening** | 1 | 1 | - | 166.19 | - | 6,082 | - | 0.000287 | 🔵 low — common in general English | — |
| 6444 | **dripping** | 1 | 1 | - | 166.19 | - | 6,083 | - | 0.000287 | 🔵 low — common in general English | — |
| 6445 | **flushed** | 1 | 1 | - | 166.19 | - | 6,084 | - | 0.000287 | 🔵 low — common in general English | — |
| 6446 | **expelled** | 1 | 1 | - | 166.19 | - | 6,085 | - | 0.000287 | 🔵 low — common in general English | — |
| 6447 | **spider** | 1 | 1 | - | 166.19 | - | 6,086 | - | 0.000287 | 🔵 low — common in general English | — |
| 6448 | **scorpion** | 1 | 1 | - | 166.19 | - | 6,087 | - | 0.000287 | 🔵 low — common in general English | — |
| 6449 | **toad** | 1 | 1 | - | 166.19 | - | 6,088 | - | 0.000287 | 🔵 low — common in general English | — |
| 6450 | **tadpole** | 1 | 1 | - | 166.19 | - | 6,089 | - | 0.000287 | 🔵 low — common in general English | — |
| 6451 | **vapour** | 1 | 1 | - | 166.19 | - | 6,090 | - | 0.000287 | 🔵 low — common in general English | — |
| 6452 | **orifice** | 1 | 1 | - | 166.19 | - | 6,091 | - | 0.000287 | 🔵 low — common in general English | — |
| 6453 | **personification** | 1 | 1 | - | 166.19 | - | 6,092 | - | 0.000287 | 🔵 low — common in general English | — |
| 6454 | **expectantly** | 1 | 1 | - | 166.19 | - | 6,093 | - | 0.000287 | 🔵 low — common in general English | — |
| 6455 | **earth-every** | 1 | 1 | - | 166.19 | - | 6,094 | - | 0.000287 | 🔵 low — common in general English | — |
| 6456 | **flesh-are** | 1 | 1 | - | 166.19 | - | 6,095 | - | 0.000287 | 🔵 low — common in general English | — |
| 6457 | **score** | 1 | 1 | - | 166.19 | - | 6,096 | - | 0.000287 | 🔵 low — common in general English | — |
| 6458 | **vertically** | 1 | 1 | - | 166.19 | - | 6,097 | - | 0.000287 | 🔵 low — common in general English | — |
| 6459 | **sixty-four** | 1 | 1 | - | 166.19 | - | 6,098 | - | 0.000287 | 🔵 low — common in general English | — |
| 6460 | **svabhavika** | 1 | 1 | - | 166.19 | - | 6,099 | - | 0.000287 | 🔵 low — common in general English | — |
| 6461 | **smilingly** | 1 | 1 | - | 166.19 | - | 6,100 | - | 0.000287 | 🔵 low — common in general English | — |
| 6462 | **behi** | 1 | 1 | - | 166.19 | - | 6,101 | - | 0.000287 | 🔵 low — common in general English | — |
| 6463 | **fringed** | 1 | 1 | - | 166.19 | - | 6,102 | - | 0.000287 | 🔵 low — common in general English | — |
| 6464 | **thousand-spoked** | 1 | 1 | - | 166.19 | - | 6,103 | - | 0.000287 | 🔵 low — common in general English | — |
| 6465 | **result-the** | 1 | 1 | - | 166.19 | - | 6,104 | - | 0.000287 | 🔵 low — common in general English | — |
| 6466 | **multi-col** | 1 | 1 | - | 166.19 | - | 6,105 | - | 0.000287 | 🔵 low — common in general English | — |
| 6467 | **oured** | 1 | 1 | - | 166.19 | - | 6,106 | - | 0.000287 | 🔵 low — common in general English | — |
| 6468 | **pronouncing** | 1 | 1 | - | 166.19 | - | 6,107 | - | 0.000287 | 🔵 low — common in general English | — |
| 6469 | **humming** | 1 | 1 | - | 166.19 | - | 6,108 | - | 0.000287 | 🔵 low — common in general English | — |
| 6470 | **rapakaya** | 1 | 1 | - | 166.19 | - | 6,109 | - | 0.000286 | 🔵 low — common in general English | — |
| 6471 | **spon** | 1 | 1 | - | 166.19 | - | 6,110 | - | 0.000286 | 🔵 low — common in general English | — |
| 6472 | **taneously** | 1 | 1 | - | 166.19 | - | 6,111 | - | 0.000286 | 🔵 low — common in general English | — |
| 6473 | **reabsorbing** | 1 | 1 | - | 166.19 | - | 6,112 | - | 0.000286 | 🔵 low — common in general English | — |
| 6474 | **vanishing** | 1 | 1 | - | 166.19 | - | 6,113 | - | 0.000286 | 🔵 low — common in general English | — |
| 6475 | **officiating** | 1 | 1 | - | 166.19 | - | 6,114 | - | 0.000286 | 🔵 low — common in general English | — |
| 6476 | **officiant** | 1 | 1 | - | 166.19 | - | 6,115 | - | 0.000286 | 🔵 low — common in general English | — |
| 6477 | **ornate** | 1 | 1 | - | 166.19 | - | 6,116 | - | 0.000286 | 🔵 low — common in general English | — |
| 6478 | **intonation** | 1 | 1 | - | 166.19 | - | 6,117 | - | 0.000286 | 🔵 low — common in general English | — |
| 6479 | **blaring** | 1 | 1 | - | 166.19 | - | 6,118 | - | 0.000286 | 🔵 low — common in general English | — |
| 6480 | **trumpet** | 1 | 1 | - | 166.19 | - | 6,119 | - | 0.000286 | 🔵 low — common in general English | — |
| 6481 | **drum** | 1 | 1 | - | 166.19 | - | 6,120 | - | 0.000286 | 🔵 low — common in general English | ~ |
| 6482 | **recited-at** | 1 | 1 | - | 166.19 | - | 6,121 | - | 0.000286 | 🔵 low — common in general English | — |
| 6483 | **goings-on** | 1 | 1 | - | 166.19 | - | 6,122 | - | 0.000286 | 🔵 low — common in general English | — |
| 6484 | **clattering** | 1 | 1 | - | 166.19 | - | 6,123 | - | 0.000286 | 🔵 low — common in general English | — |
| 6485 | **puspe** | 1 | 1 | - | 166.19 | - | 6,124 | - | 0.000286 | 🔵 low — common in general English | — |
| 6486 | **dhupe** | 1 | 1 | - | 166.19 | - | 6,125 | - | 0.000286 | 🔵 low — common in general English | — |
| 6487 | **travesty** | 1 | 1 | - | 166.19 | - | 6,126 | - | 0.000286 | 🔵 low — common in general English | — |
| 6488 | **swallowing** | 1 | 1 | - | 166.19 | - | 6,127 | - | 0.000286 | 🔵 low — common in general English | — |
| 6489 | **soul** | 1 | 1 | - | 166.19 | - | 6,128 | - | 0.000286 | 🔵 low — common in general English | — |
| 6490 | **grimy** | 1 | 1 | - | 166.19 | - | 6,129 | - | 0.000286 | 🔵 low — common in general English | — |
| 6491 | **scrupulous** | 1 | 1 | - | 166.19 | - | 6,130 | - | 0.000286 | 🔵 low — common in general English | — |
| 6492 | **tiresome** | 1 | 1 | - | 166.19 | - | 6,131 | - | 0.000286 | 🔵 low — common in general English | — |
| 6493 | **undistracted** | 1 | 1 | - | 166.19 | - | 6,132 | - | 0.000286 | 🔵 low — common in general English | — |
| 6494 | **laywoman** | 1 | 1 | - | 166.19 | - | 6,133 | - | 0.000286 | 🔵 low — common in general English | — |
| 6495 | **atiga** | 1 | 1 | - | 166.19 | - | 6,134 | - | 0.000286 | 🔵 low — common in general English | — |
| 6496 | **non-existent** | 1 | 1 | - | 166.19 | - | 6,135 | - | 0.000286 | 🔵 low — common in general English | — |
| 6497 | **valley-i** | 1 | 1 | - | 166.19 | - | 6,136 | - | 0.000286 | 🔵 low — common in general English | — |
| 6498 | **unfit** | 1 | 1 | - | 166.19 | - | 6,137 | - | 0.000286 | 🔵 low — common in general English | — |
| 6499 | **infecting** | 1 | 1 | - | 166.19 | - | 6,138 | - | 0.000286 | 🔵 low — common in general English | — |
| 6500 | **brightly** | 1 | 1 | - | 166.19 | - | 6,139 | - | 0.000286 | 🔵 low — common in general English | — |
| 6501 | **danced** | 1 | 1 | - | 166.19 | - | 6,140 | - | 0.000286 | 🔵 low — common in general English | — |
| 6502 | **samaya-and** | 1 | 1 | - | 166.19 | - | 6,141 | - | 0.000286 | 🔵 low — common in general English | — |
| 6503 | **delirious** | 1 | 1 | - | 166.19 | - | 6,142 | - | 0.000286 | 🔵 low — common in general English | — |
| 6504 | **urgyenpa** | 1 | 1 | - | 166.19 | - | 6,143 | - | 0.000286 | 🔵 low — common in general English | — |
| 6505 | **vanish** | 1 | 1 | - | 166.19 | - | 6,144 | - | 0.000286 | 🔵 low — common in general English | — |
| 6506 | **earthenware** | 1 | 1 | - | 166.19 | - | 6,145 | - | 0.000286 | 🔵 low — common in general English | — |
| 6507 | **denting** | 1 | 1 | - | 166.19 | - | 6,146 | - | 0.000286 | 🔵 low — common in general English | — |
| 6508 | **curing** | 1 | 1 | - | 166.19 | - | 6,147 | - | 0.000286 | 🔵 low — common in general English | — |
| 6509 | **unremittingly** | 1 | 1 | - | 166.19 | - | 6,148 | - | 0.000285 | 🔵 low — common in general English | — |
| 6510 | **joke** | 1 | 1 | - | 166.19 | - | 6,149 | - | 0.000285 | 🔵 low — common in general English | — |
| 6511 | **obscu** | 1 | 1 | - | 166.19 | - | 6,150 | - | 0.000285 | 🔵 low — common in general English | — |
| 6512 | **fooled** | 1 | 1 | - | 166.19 | - | 6,151 | - | 0.000285 | 🔵 low — common in general English | — |
| 6513 | **interdependently** | 1 | 1 | - | 166.19 | - | 6,152 | - | 0.000285 | 🔵 low — common in general English | — |
| 6514 | **virupa** | 1 | 1 | - | 166.19 | - | 6,153 | - | 0.000285 | 🔵 low — common in general English | ✓ |
| 6515 | **replete** | 1 | 1 | - | 166.19 | - | 6,154 | - | 0.000285 | 🔵 low — common in general English | — |
| 6516 | **bell-metal** | 1 | 1 | - | 166.19 | - | 6,155 | - | 0.000285 | 🔵 low — common in general English | — |
| 6517 | **turquois** | 1 | 1 | - | 166.19 | - | 6,156 | - | 0.000285 | 🔵 low — common in general English | — |
| 6518 | **sapphire** | 1 | 1 | - | 166.19 | - | 6,157 | - | 0.000285 | 🔵 low — common in general English | — |
| 6519 | **arura** | 1 | 1 | - | 166.19 | - | 6,158 | - | 0.000285 | 🔵 low — common in general English | ~ |
| 6520 | **kyurura** | 1 | 1 | - | 166.19 | - | 6,159 | - | 0.000285 | 🔵 low — common in general English | ~ |
| 6521 | **puls** | 1 | 1 | - | 166.19 | - | 6,160 | - | 0.000285 | 🔵 low — common in general English | — |
| 6522 | **direction-meaning** | 1 | 1 | - | 166.19 | - | 6,161 | - | 0.000285 | 🔵 low — common in general English | — |
| 6523 | **dha** | 1 | 1 | - | 166.19 | - | 6,162 | - | 0.000285 | 🔵 low — common in general English | — |
| 6524 | **obhya** | 1 | 1 | - | 166.19 | - | 6,163 | - | 0.000285 | 🔵 low — common in general English | — |
| 6525 | **ratnasambhava** | 1 | 1 | - | 166.19 | - | 6,164 | - | 0.000285 | 🔵 low — common in general English | ✓ རིན་ཆེན་འབྱུང་གནས |
| 6526 | **amoghasiddhi** | 1 | 1 | - | 166.19 | - | 6,165 | - | 0.000285 | 🔵 low — common in general English | ✓ དོན་ཡོད་གྲུབ་པ |
| 6527 | **stacked-up** | 1 | 1 | - | 166.19 | - | 6,166 | - | 0.000285 | 🔵 low — common in general English | — |
| 6528 | **altar** | 1 | 1 | - | 166.19 | - | 6,167 | - | 0.000285 | 🔵 low — common in general English | — |
| 6529 | **wiping** | 1 | 1 | - | 166.19 | - | 6,168 | - | 0.000285 | 🔵 low — common in general English | — |
| 6530 | **veil** | 1 | 1 | - | 166.19 | - | 6,169 | - | 0.000285 | 🔵 low — common in general English | — |
| 6531 | **woollen** | 1 | 1 | - | 166.19 | - | 6,170 | - | 0.000285 | 🔵 low — common in general English | — |
| 6532 | **chogyal** | 1 | 1 | - | 166.19 | - | 6,171 | - | 0.000285 | 🔵 low — common in general English | ~ |
| 6533 | **pakpa** | 1 | 1 | - | 166.19 | - | 6,172 | - | 0.000285 | 🔵 low — common in general English | ~ |
| 6534 | **nyingma** | 1 | 1 | - | 166.19 | - | 6,173 | - | 0.000285 | 🔵 low — common in general English | — |
| 6535 | **bhumi** | 1 | 1 | - | 166.19 | - | 6,174 | - | 0.000285 | 🔵 low — common in general English | — |
| 6536 | **sprinkling** | 1 | 1 | - | 166.19 | - | 6,175 | - | 0.000285 | 🔵 low — common in general English | — |
| 6537 | **ung** | 1 | 1 | - | 166.19 | - | 6,176 | - | 0.000285 | 🔵 low — common in general English | — |
| 6538 | **thumb** | 1 | 1 | - | 166.19 | - | 6,177 | - | 0.000285 | 🔵 low — common in general English | — |
| 6539 | **rekhe** | 1 | 1 | - | 166.19 | - | 6,178 | - | 0.000285 | 🔵 low — common in general English | — |
| 6540 | **purvavideha** | 1 | 1 | - | 166.19 | - | 6,179 | - | 0.000285 | 🔵 low — common in general English | — |
| 6541 | **deha** | 1 | 1 | - | 166.19 | - | 6,180 | - | 0.000285 | 🔵 low — common in general English | — |
| 6542 | **videha** | 1 | 1 | - | 166.19 | - | 6,181 | - | 0.000285 | 🔵 low — common in general English | — |
| 6543 | **inexhaustibly** | 1 | 1 | - | 166.19 | - | 6,182 | - | 0.000285 | 🔵 low — common in general English | — |
| 6544 | **victorious** | 1 | 1 | - | 166.19 | - | 6,183 | - | 0.000285 | 🔵 low — common in general English | ~ |
| 6545 | **unfilled** | 1 | 1 | - | 166.19 | - | 6,184 | - | 0.000285 | 🔵 low — common in general English | — |
| 6546 | **first-order** | 1 | 1 | - | 166.19 | - | 6,185 | - | 0.000285 | 🔵 low — common in general English | — |
| 6547 | **second-order** | 1 | 1 | - | 166.19 | - | 6,186 | - | 0.000284 | 🔵 low — common in general English | — |
| 6548 | **millionfold** | 1 | 1 | - | 166.19 | - | 6,187 | - | 0.000284 | 🔵 low — common in general English | — |
| 6549 | **third-order** | 1 | 1 | - | 166.19 | - | 6,188 | - | 0.000284 | 🔵 low — common in general English | — |
| 6550 | **buddha-sakyamuni** | 1 | 1 | - | 166.19 | - | 6,189 | - | 0.000284 | 🔵 low — common in general English | — |
| 6551 | **endurance** | 1 | 1 | - | 166.19 | - | 6,190 | - | 0.000284 | 🔵 low — common in general English | — |
| 6552 | **graced** | 1 | 1 | - | 166.19 | - | 6,191 | - | 0.000284 | 🔵 low — common in general English | — |
| 6553 | **infinitely** | 1 | 1 | - | 166.19 | - | 6,192 | - | 0.000284 | 🔵 low — common in general English | — |
| 6554 | **unborn** | 1 | 1 | - | 166.19 | - | 6,193 | - | 0.000284 | 🔵 low — common in general English | — |
| 6555 | **ache** | 1 | 1 | - | 166.19 | - | 6,194 | - | 0.000284 | 🔵 low — common in general English | — |
| 6556 | **seven-element** | 1 | 1 | - | 166.19 | - | 6,195 | - | 0.000284 | 🔵 low — common in general English | — |
| 6557 | **important-a** | 1 | 1 | - | 166.19 | - | 6,196 | - | 0.000284 | 🔵 low — common in general English | — |
| 6558 | **do-to** | 1 | 1 | - | 166.19 | - | 6,197 | - | 0.000284 | 🔵 low — common in general English | — |
| 6559 | **saturate** | 1 | 1 | - | 166.19 | - | 6,198 | - | 0.000284 | 🔵 low — common in general English | — |
| 6560 | **scented** | 1 | 1 | - | 166.19 | - | 6,199 | - | 0.000284 | 🔵 low — common in general English | — |
| 6561 | **generously** | 1 | 1 | - | 166.19 | - | 6,200 | - | 0.000284 | 🔵 low — common in general English | — |
| 6562 | **reasons-and** | 1 | 1 | - | 166.19 | - | 6,201 | - | 0.000284 | 🔵 low — common in general English | — |
| 6563 | **yourself-that** | 1 | 1 | - | 166.19 | - | 6,202 | - | 0.000284 | 🔵 low — common in general English | — |
| 6564 | **fooling** | 1 | 1 | - | 166.19 | - | 6,203 | - | 0.000284 | 🔵 low — common in general English | — |
| 6565 | **dirtily** | 1 | 1 | - | 166.19 | - | 6,204 | - | 0.000284 | 🔵 low — common in general English | — |
| 6566 | **mouldy** | 1 | 1 | - | 166.19 | - | 6,205 | - | 0.000284 | 🔵 low — common in general English | — |
| 6567 | **lamp-offering** | 1 | 1 | - | 166.19 | - | 6,206 | - | 0.000284 | 🔵 low — common in general English | — |
| 6568 | **rancid** | 1 | 1 | - | 166.19 | - | 6,207 | - | 0.000284 | 🔵 low — common in general English | — |
| 6569 | **shelze** | 1 | 1 | - | 166.19 | - | 6,208 | - | 0.000284 | 🔵 low — common in general English | — |
| 6570 | **consi** | 1 | 1 | - | 166.19 | - | 6,209 | - | 0.000284 | 🔵 low — common in general English | — |
| 6571 | **tency** | 1 | 1 | - | 166.19 | - | 6,210 | - | 0.000284 | 🔵 low — common in general English | — |
| 6572 | **torma-dough** | 1 | 1 | - | 166.19 | - | 6,211 | - | 0.000284 | 🔵 low — common in general English | — |
| 6573 | **distinctively** | 1 | 1 | - | 166.19 | - | 6,212 | - | 0.000284 | 🔵 low — common in general English | — |
| 6574 | **sublimely** | 1 | 1 | - | 166.19 | - | 6,213 | - | 0.000284 | 🔵 low — common in general English | — |
| 6575 | **scavenger** | 1 | 1 | - | 166.19 | - | 6,214 | - | 0.000284 | 🔵 low — common in general English | — |
| 6576 | **rice-gruel** | 1 | 1 | - | 166.19 | - | 6,215 | - | 0.000284 | 🔵 low — common in general English | — |
| 6577 | **maqc** | 1 | 1 | - | 166.19 | - | 6,216 | - | 0.000284 | 🔵 low — common in general English | — |
| 6578 | **fingernail** | 1 | 1 | - | 166.19 | - | 6,217 | - | 0.000284 | 🔵 low — common in general English | — |
| 6579 | **oily** | 1 | 1 | - | 166.19 | - | 6,218 | - | 0.000284 | 🔵 low — common in general English | — |
| 6580 | **rupakaya** | 1 | 1 | - | 166.19 | - | 6,219 | - | 0.000284 | 🔵 low — common in general English | ✓ གཟུགས་སྐུ |
| 6581 | **converse** | 1 | 1 | - | 166.19 | - | 6,220 | - | 0.000284 | 🔵 low — common in general English | — |
| 6582 | **barbaric** | 1 | 1 | - | 166.19 | - | 6,221 | - | 0.000284 | 🔵 low — common in general English | — |
| 6583 | **aiota** | 1 | 1 | - | 166.19 | - | 6,223 | - | 0.000284 | 🔵 low — common in general English | — |
| 6584 | **tree-or** | 1 | 1 | - | 166.19 | - | 6,224 | - | 0.000284 | 🔵 low — common in general English | — |
| 6585 | **world-even** | 1 | 1 | - | 166.19 | - | 6,225 | - | 0.000284 | 🔵 low — common in general English | — |
| 6586 | **rainbow-none** | 1 | 1 | - | 166.19 | - | 6,226 | - | 0.000283 | 🔵 low — common in general English | — |
| 6587 | **jaundice** | 1 | 1 | - | 166.19 | - | 6,227 | - | 0.000283 | 🔵 low — common in general English | — |
| 6588 | **cheerfully** | 1 | 1 | - | 166.19 | - | 6,228 | - | 0.000283 | 🔵 low — common in general English | — |
| 6589 | **dissipated** | 1 | 1 | - | 166.19 | - | 6,229 | - | 0.000283 | 🔵 low — common in general English | — |
| 6590 | **puri** | 1 | 1 | - | 166.19 | - | 6,230 | - | 0.000283 | 🔵 low — common in general English | — |
| 6591 | **fying** | 1 | 1 | - | 166.19 | - | 6,231 | - | 0.000283 | 🔵 low — common in general English | — |
| 6592 | **contradiction** | 1 | 1 | - | 166.19 | - | 6,232 | - | 0.000283 | 🔵 low — common in general English | — |
| 6593 | **tised** | 1 | 1 | - | 166.19 | - | 6,233 | - | 0.000283 | 🔵 low — common in general English | — |
| 6594 | **life-hermit** | 1 | 1 | - | 166.19 | - | 6,234 | - | 0.000283 | 🔵 low — common in general English | — |
| 6595 | **instance-use** | 1 | 1 | - | 166.19 | - | 6,235 | - | 0.000283 | 🔵 low — common in general English | — |
| 6596 | **clung** | 1 | 1 | - | 166.19 | - | 6,236 | - | 0.000283 | 🔵 low — common in general English | — |
| 6597 | **instantaneously** | 1 | 1 | - | 166.19 | - | 6,237 | - | 0.000283 | 🔵 low — common in general English | — |
| 6598 | **swaying** | 1 | 1 | - | 166.19 | - | 6,238 | - | 0.000283 | 🔵 low — common in general English | — |
| 6599 | **squealing** | 1 | 1 | - | 166.19 | - | 6,239 | - | 0.000283 | 🔵 low — common in general English | — |
| 6600 | **mother-the** | 1 | 1 | - | 166.19 | - | 6,240 | - | 0.000283 | 🔵 low — common in general English | — |
| 6601 | **consciousness-instantly** | 1 | 1 | - | 166.19 | - | 6,241 | - | 0.000283 | 🔵 low — common in general English | — |
| 6602 | **life-size** | 1 | 1 | - | 166.19 | - | 6,242 | - | 0.000283 | 🔵 low — common in general English | — |
| 6603 | **tripod** | 1 | 1 | - | 166.19 | - | 6,243 | - | 0.000283 | 🔵 low — common in general English | — |
| 6604 | **sizzle** | 1 | 1 | - | 166.19 | - | 6,244 | - | 0.000283 | 🔵 low — common in general English | — |
| 6605 | **foul** | 1 | 1 | - | 166.19 | - | 6,245 | - | 0.000283 | 🔵 low — common in general English | — |
| 6606 | **frothing** | 1 | 1 | - | 166.19 | - | 6,246 | - | 0.000283 | 🔵 low — common in general English | — |
| 6607 | **scum** | 1 | 1 | - | 166.19 | - | 6,247 | - | 0.000283 | 🔵 low — common in general English | — |
| 6608 | **exude** | 1 | 1 | - | 166.19 | - | 6,248 | - | 0.000283 | 🔵 low — common in general English | — |
| 6609 | **ridding** | 1 | 1 | - | 166.19 | - | 6,249 | - | 0.000283 | 🔵 low — common in general English | — |
| 6610 | **imperfection** | 1 | 1 | - | 166.19 | - | 6,250 | - | 0.000283 | 🔵 low — common in general English | — |
| 6611 | **billow** | 1 | 1 | - | 166.19 | - | 6,251 | - | 0.000283 | 🔵 low — common in general English | — |
| 6612 | **locality** | 1 | 1 | - | 166.19 | - | 6,252 | - | 0.000283 | 🔵 low — common in general English | — |
| 6613 | **teeming** | 1 | 1 | - | 166.19 | - | 6,253 | - | 0.000283 | 🔵 low — common in general English | — |
| 6614 | **deity-a** | 1 | 1 | - | 166.19 | - | 6,254 | - | 0.000283 | 🔵 low — common in general English | — |
| 6615 | **iaka** | 1 | 1 | - | 166.19 | - | 6,255 | - | 0.000283 | 🔵 low — common in general English | — |
| 6616 | **unfavour** | 1 | 1 | - | 166.19 | - | 6,256 | - | 0.000283 | 🔵 low — common in general English | — |
| 6617 | **swarm** | 1 | 1 | - | 166.19 | - | 6,257 | - | 0.000283 | 🔵 low — common in general English | — |
| 6618 | **activity-performing** | 1 | 1 | - | 166.19 | - | 6,258 | - | 0.000283 | 🔵 low — common in general English | — |
| 6619 | **appeasing** | 1 | 1 | - | 166.19 | - | 6,259 | - | 0.000283 | 🔵 low — common in general English | — |
| 6620 | **mother-use** | 1 | 1 | - | 166.19 | - | 6,260 | - | 0.000283 | 🔵 low — common in general English | — |
| 6621 | **scatter** | 1 | 1 | - | 166.19 | - | 6,261 | - | 0.000283 | 🔵 low — common in general English | — |
| 6622 | **victory-banner** | 1 | 1 | - | 166.19 | - | 6,262 | - | 0.000283 | 🔵 low — common in general English | — |
| 6623 | **overlord** | 1 | 1 | - | 166.19 | - | 6,263 | - | 0.000283 | 🔵 low — common in general English | — |
| 6624 | **underling** | 1 | 1 | - | 166.19 | - | 6,264 | - | 0.000283 | 🔵 low — common in general English | — |
| 6625 | **snatch** | 1 | 1 | - | 166.19 | - | 6,265 | - | 0.000282 | 🔵 low — common in general English | — |
| 6626 | **life-force** | 1 | 1 | - | 166.19 | - | 6,266 | - | 0.000282 | 🔵 low — common in general English | — |
| 6627 | **avenger** | 1 | 1 | - | 166.19 | - | 6,267 | - | 0.000282 | 🔵 low — common in general English | — |
| 6628 | **behind-the** | 1 | 1 | - | 166.19 | - | 6,268 | - | 0.000282 | 🔵 low — common in general English | — |
| 6629 | **suffering-the** | 1 | 1 | - | 166.19 | - | 6,269 | - | 0.000282 | 🔵 low — common in general English | — |
| 6630 | **life-restoring** | 1 | 1 | - | 166.19 | - | 6,270 | - | 0.000282 | 🔵 low — common in general English | — |
| 6631 | **offerer** | 1 | 1 | - | 166.19 | - | 6,271 | - | 0.000282 | 🔵 low — common in general English | — |
| 6632 | **vari** | 1 | 1 | - | 166.19 | - | 6,272 | - | 0.000282 | 🔵 low — common in general English | — |
| 6633 | **egated** | 1 | 1 | - | 166.19 | - | 6,273 | - | 0.000282 | 🔵 low — common in general English | — |
| 6634 | **variegated** | 1 | 1 | - | 166.19 | - | 6,274 | - | 0.000282 | 🔵 low — common in general English | — |
| 6635 | **grisly** | 1 | 1 | - | 166.19 | - | 6,275 | - | 0.000282 | 🔵 low — common in general English | — |
| 6636 | **slashing** | 1 | 1 | - | 166.19 | - | 6,276 | - | 0.000282 | 🔵 low — common in general English | — |
| 6637 | **bravado** | 1 | 1 | - | 166.19 | - | 6,277 | - | 0.000282 | 🔵 low — common in general English | — |
| 6638 | **hate-filled** | 1 | 1 | - | 166.19 | - | 6,278 | - | 0.000282 | 🔵 low — common in general English | — |
| 6639 | **clenching** | 1 | 1 | - | 166.19 | - | 6,279 | - | 0.000282 | 🔵 low — common in general English | — |
| 6640 | **lashing** | 1 | 1 | - | 166.19 | - | 6,280 | - | 0.000282 | 🔵 low — common in general English | — |
| 6641 | **whirl** | 1 | 1 | - | 166.19 | - | 6,281 | - | 0.000282 | 🔵 low — common in general English | — |
| 6642 | **inauspicious** | 1 | 1 | - | 166.19 | - | 6,282 | - | 0.000282 | 🔵 low — common in general English | — |
| 6643 | **compassion-but** | 1 | 1 | - | 166.19 | - | 6,283 | - | 0.000282 | 🔵 low — common in general English | — |
| 6644 | **ninefold** | 1 | 1 | - | 166.19 | - | 6,284 | - | 0.000282 | 🔵 low — common in general English | — |
| 6645 | **puny** | 1 | 1 | - | 166.19 | - | 6,285 | - | 0.000282 | 🔵 low — common in general English | — |
| 6646 | **retaliation-a** | 1 | 1 | - | 166.19 | - | 6,286 | - | 0.000282 | 🔵 low — common in general English | — |
| 6647 | **path-the** | 1 | 1 | - | 166.19 | - | 6,287 | - | 0.000282 | 🔵 low — common in general English | — |
| 6648 | **subjugation** | 1 | 1 | - | 166.19 | - | 6,288 | - | 0.000282 | 🔵 low — common in general English | — |
| 6649 | **instance-are** | 1 | 1 | - | 166.19 | - | 6,289 | - | 0.000282 | 🔵 low — common in general English | — |
| 6650 | **heaped** | 1 | 1 | - | 166.19 | - | 6,290 | - | 0.000282 | 🔵 low — common in general English | — |
| 6651 | **conceir** | 1 | 1 | - | 166.19 | - | 6,291 | - | 0.000282 | 🔵 low — common in general English | — |
| 6652 | **exultation** | 1 | 1 | - | 166.19 | - | 6,292 | - | 0.000282 | 🔵 low — common in general English | — |
| 6653 | **trampling** | 1 | 1 | - | 166.19 | - | 6,293 | - | 0.000282 | 🔵 low — common in general English | — |
| 6654 | **mischief** | 1 | 1 | - | 166.19 | - | 6,294 | - | 0.000282 | 🔵 low — common in general English | — |
| 6655 | **embar** | 1 | 1 | - | 166.19 | - | 6,295 | - | 0.000282 | 🔵 low — common in general English | — |
| 6656 | **rassed** | 1 | 1 | - | 166.19 | - | 6,296 | - | 0.000282 | 🔵 low — common in general English | — |
| 6657 | **mobilize** | 1 | 1 | - | 166.19 | - | 6,297 | - | 0.000282 | 🔵 low — common in general English | — |
| 6658 | **gyalgong** | 1 | 1 | - | 166.19 | - | 6,298 | - | 0.000282 | 🔵 low — common in general English | — |
| 6659 | **there-it** | 1 | 1 | - | 166.19 | - | 6,299 | - | 0.000282 | 🔵 low — common in general English | — |
| 6660 | **trance** | 1 | 1 | - | 166.19 | - | 6,300 | - | 0.000282 | 🔵 low — common in general English | — |
| 6661 | **insistent** | 1 | 1 | - | 166.19 | - | 6,301 | - | 0.000282 | 🔵 low — common in general English | — |
| 6662 | **predic** | 1 | 1 | - | 166.19 | - | 6,302 | - | 0.000282 | 🔵 low — common in general English | — |
| 6663 | **samaya-breaker** | 1 | 1 | - | 166.19 | - | 6,303 | - | 0.000282 | 🔵 low — common in general English | — |
| 6664 | **clergy** | 1 | 1 | - | 166.19 | - | 6,304 | - | 0.000282 | 🔵 low — common in general English | — |
| 6665 | **dream-like** | 1 | 1 | - | 166.19 | - | 6,305 | - | 0.000282 | 🔵 low — common in general English | — |
| 6666 | **momentarily** | 1 | 1 | - | 166.19 | - | 6,306 | - | 0.000281 | 🔵 low — common in general English | — |
| 6667 | **self-concern** | 1 | 1 | - | 166.19 | - | 6,307 | - | 0.000281 | 🔵 low — common in general English | — |
| 6668 | **maliciousness** | 1 | 1 | - | 166.19 | - | 6,308 | - | 0.000281 | 🔵 low — common in general English | — |
| 6669 | **others-and** | 1 | 1 | - | 166.19 | - | 6,309 | - | 0.000281 | 🔵 low — common in general English | — |
| 6670 | **fixation** | 1 | 1 | - | 166.19 | - | 6,310 | - | 0.000281 | 🔵 low — common in general English | — |
| 6671 | **qualifica** | 1 | 1 | - | 166.19 | - | 6,311 | - | 0.000281 | 🔵 low — common in general English | — |
| 6672 | **illustrative** | 1 | 1 | - | 166.19 | - | 6,312 | - | 0.000281 | 🔵 low — common in general English | ~ |
| 6673 | **untar** | 1 | 1 | - | 166.19 | - | 6,313 | - | 0.000281 | 🔵 low — common in general English | — |
| 6674 | **nished** | 1 | 1 | - | 166.19 | - | 6,314 | - | 0.000281 | 🔵 low — common in general English | — |
| 6675 | **alone-awaken** | 1 | 1 | - | 166.19 | - | 6,315 | - | 0.000281 | 🔵 low — common in general English | — |
| 6676 | **gotsangpa** | 1 | 1 | - | 166.19 | - | 6,316 | - | 0.000281 | 🔵 low — common in general English | ~ |
| 6677 | **rangrik** | 1 | 1 | - | 166.19 | - | 6,317 | - | 0.000281 | 🔵 low — common in general English | — |
| 6678 | **north-facing** | 1 | 1 | - | 166.19 | - | 6,318 | - | 0.000281 | 🔵 low — common in general English | — |
| 6679 | **devotional** | 1 | 1 | - | 166.19 | - | 6,319 | - | 0.000281 | 🔵 low — common in general English | — |
| 6680 | **uncontrived** | 1 | 1 | - | 166.19 | - | 6,320 | - | 0.000281 | 🔵 low — common in general English | — |
| 6681 | **vanquishing** | 1 | 1 | - | 166.19 | - | 6,321 | - | 0.000281 | 🔵 low — common in general English | — |
| 6682 | **nagabodhi** | 1 | 1 | - | 166.19 | - | 6,322 | - | 0.000281 | 🔵 low — common in general English | — |
| 6683 | **snatching** | 1 | 1 | - | 166.19 | - | 6,323 | - | 0.000281 | 🔵 low — common in general English | — |
| 6684 | **fervour** | 1 | 1 | - | 166.19 | - | 6,324 | - | 0.000281 | 🔵 low — common in general English | — |
| 6685 | **ligent** | 1 | 1 | - | 166.19 | - | 6,325 | - | 0.000281 | 🔵 low — common in general English | — |
| 6686 | **intellectualization** | 1 | 1 | - | 166.19 | - | 6,326 | - | 0.000281 | 🔵 low — common in general English | — |
| 6687 | **gyalmo** | 1 | 1 | - | 166.19 | - | 6,327 | - | 0.000281 | 🔵 low — common in general English | — |
| 6688 | **tsawarong** | 1 | 1 | - | 166.19 | - | 6,328 | - | 0.000281 | 🔵 low — common in general English | — |
| 6689 | **pang** | 1 | 1 | - | 166.19 | - | 6,329 | - | 0.000281 | 🔵 low — common in general English | — |
| 6690 | **meditation-band** | 1 | 1 | - | 166.19 | - | 6,330 | - | 0.000281 | 🔵 low — common in general English | — |
| 6691 | **hood** | 1 | 1 | - | 166.19 | - | 6,331 | - | 0.000281 | 🔵 low — common in general English | — |
| 6692 | **yana** | 1 | 1 | - | 166.19 | - | 6,332 | - | 0.000281 | 🔵 low — common in general English | — |
| 6693 | **enough-even** | 1 | 1 | - | 166.19 | - | 6,333 | - | 0.000281 | 🔵 low — common in general English | — |
| 6694 | **receptacle** | 1 | 1 | - | 166.19 | - | 6,334 | - | 0.000281 | 🔵 low — common in general English | — |
| 6695 | **vajrayogini** | 1 | 1 | - | 166.19 | - | 6,335 | - | 0.000281 | 🔵 low — common in general English | — |
| 6696 | **awakening** | 1 | 1 | - | 166.19 | - | 6,336 | - | 0.000281 | 🔵 low — common in general English | — |
| 6697 | **insubstantial** | 1 | 1 | - | 166.19 | - | 6,337 | - | 0.000281 | 🔵 low — common in general English | — |
| 6698 | **complexion** | 1 | 1 | - | 166.19 | - | 6,338 | - | 0.000281 | 🔵 low — common in general English | — |
| 6699 | **tinged** | 1 | 1 | - | 166.19 | - | 6,339 | - | 0.000281 | 🔵 low — common in general English | — |
| 6700 | **long-sleeved** | 1 | 1 | - | 166.19 | - | 6,340 | - | 0.000281 | 🔵 low — common in general English | — |
| 6701 | **gown** | 1 | 1 | - | 166.19 | - | 6,341 | - | 0.000281 | 🔵 low — common in general English | — |
| 6702 | **deerskin** | 1 | 1 | - | 166.19 | - | 6,342 | - | 0.000281 | 🔵 low — common in general English | — |
| 6703 | **adhara** | 1 | 1 | - | 166.19 | - | 6,343 | - | 0.000281 | 🔵 low — common in general English | — |
| 6704 | **unharmed** | 1 | 1 | - | 166.19 | - | 6,344 | - | 0.000281 | 🔵 low — common in general English | — |
| 6705 | **petalled** | 1 | 1 | - | 166.19 | - | 6,345 | - | 0.000281 | 🔵 low — common in general English | — |
| 6706 | **emblazoned** | 1 | 1 | - | 166.19 | - | 6,346 | - | 0.000280 | 🔵 low — common in general English | — |
| 6707 | **culmination** | 1 | 1 | - | 166.19 | - | 6,347 | - | 0.000280 | 🔵 low — common in general English | — |
| 6708 | **long-life** | 1 | 1 | - | 166.19 | - | 6,348 | - | 0.000280 | 🔵 low — common in general English | — |
| 6709 | **sprig** | 1 | 1 | - | 166.19 | - | 6,349 | - | 0.000280 | 🔵 low — common in general English | — |
| 6710 | **crook** | 1 | 1 | - | 166.19 | - | 6,350 | - | 0.000280 | 🔵 low — common in general English | — |
| 6711 | **mandarava** | 1 | 1 | - | 166.19 | - | 6,351 | - | 0.000280 | 🔵 low — common in general English | ✓ |
| 6712 | **dried-up** | 1 | 1 | - | 166.19 | - | 6,352 | - | 0.000280 | 🔵 low — common in general English | — |
| 6713 | **looped** | 1 | 1 | - | 166.19 | - | 6,353 | - | 0.000280 | 🔵 low — common in general English | — |
| 6714 | **pennant** | 1 | 1 | - | 166.19 | - | 6,354 | - | 0.000280 | 🔵 low — common in general English | — |
| 6715 | **encircled** | 1 | 1 | - | 166.19 | - | 6,355 | - | 0.000280 | 🔵 low — common in general English | — |
| 6716 | **evenness** | 1 | 1 | - | 166.19 | - | 6,356 | - | 0.000280 | 🔵 low — common in general English | — |
| 6717 | **siddhi** | 1 | 1 | - | 166.19 | - | 6,357 | - | 0.000280 | 🔵 low — common in general English | ✓ དངོས་གྲུབ |
| 6718 | **pliramita** | 1 | 1 | - | 166.19 | - | 6,358 | - | 0.000280 | 🔵 low — common in general English | — |
| 6719 | **insurpassable** | 1 | 1 | - | 166.19 | - | 6,359 | - | 0.000280 | 🔵 low — common in general English | — |
| 6720 | **hrib** | 1 | 1 | - | 166.19 | - | 6,360 | - | 0.000280 | 🔵 low — common in general English | — |
| 6721 | **prelimi** | 1 | 1 | - | 166.19 | - | 6,361 | - | 0.000280 | 🔵 low — common in general English | — |
| 6722 | **nary** | 1 | 1 | - | 166.19 | - | 6,362 | - | 0.000280 | 🔵 low — common in general English | — |
| 6723 | **surrendering** | 1 | 1 | - | 166.19 | - | 6,363 | - | 0.000280 | 🔵 low — common in general English | — |
| 6724 | **passer-by** | 1 | 1 | - | 166.19 | - | 6,364 | - | 0.000280 | 🔵 low — common in general English | — |
| 6725 | **lurch** | 1 | 1 | - | 166.19 | - | 6,365 | - | 0.000280 | 🔵 low — common in general English | — |
| 6726 | **ordeal** | 1 | 1 | - | 166.19 | - | 6,366 | - | 0.000280 | 🔵 low — common in general English | — |
| 6727 | **reverence** | 1 | 1 | - | 166.19 | - | 6,367 | - | 0.000280 | 🔵 low — common in general English | — |
| 6728 | **bending** | 1 | 1 | - | 166.19 | - | 6,368 | - | 0.000280 | 🔵 low — common in general English | — |
| 6729 | **cupped** | 1 | 1 | - | 166.19 | - | 6,369 | - | 0.000280 | 🔵 low — common in general English | — |
| 6730 | **ful** | 1 | 1 | - | 166.19 | - | 6,370 | - | 0.000280 | 🔵 low — common in general English | — |
| 6731 | **hunchback** | 1 | 1 | - | 166.19 | - | 6,371 | - | 0.000280 | 🔵 low — common in general English | — |
| 6732 | **dwarf** | 1 | 1 | - | 166.19 | - | 6,372 | - | 0.000280 | 🔵 low — common in general English | — |
| 6733 | **them-so** | 1 | 1 | - | 166.19 | - | 6,373 | - | 0.000280 | 🔵 low — common in general English | — |
| 6734 | **deformed** | 1 | 1 | - | 166.19 | - | 6,374 | - | 0.000280 | 🔵 low — common in general English | — |
| 6735 | **impeccably** | 1 | 1 | - | 166.19 | - | 6,375 | - | 0.000280 | 🔵 low — common in general English | — |
| 6736 | **it-and** | 1 | 1 | - | 166.19 | - | 6,376 | - | 0.000280 | 🔵 low — common in general English | — |
| 6737 | **fruitless** | 1 | 1 | - | 166.19 | - | 6,377 | - | 0.000280 | 🔵 low — common in general English | — |
| 6738 | **proficient** | 1 | 1 | - | 166.19 | - | 6,378 | - | 0.000280 | 🔵 low — common in general English | — |
| 6739 | **head-dress** | 1 | 1 | - | 166.19 | - | 6,379 | - | 0.000280 | 🔵 low — common in general English | — |
| 6740 | **soaked** | 1 | 1 | - | 166.19 | - | 6,380 | - | 0.000280 | 🔵 low — common in general English | — |
| 6741 | **dye** | 1 | 1 | - | 166.19 | - | 6,381 | - | 0.000280 | 🔵 low — common in general English | — |
| 6742 | **dyed** | 1 | 1 | - | 166.19 | - | 6,382 | - | 0.000280 | 🔵 low — common in general English | — |
| 6743 | **successfully-but** | 1 | 1 | - | 166.19 | - | 6,383 | - | 0.000280 | 🔵 low — common in general English | — |
| 6744 | **violator** | 1 | 1 | - | 166.19 | - | 6,384 | - | 0.000280 | 🔵 low — common in general English | — |
| 6745 | **aya** | 1 | 1 | - | 166.19 | - | 6,385 | - | 0.000280 | 🔵 low — common in general English | — |
| 6746 | **evildoer** | 1 | 1 | - | 166.19 | - | 6,386 | - | 0.000280 | 🔵 low — common in general English | — |
| 6747 | **dharma-just** | 1 | 1 | - | 166.19 | - | 6,387 | - | 0.000280 | 🔵 low — common in general English | — |
| 6748 | **butter-bag** | 1 | 1 | - | 166.19 | - | 6,388 | - | 0.000279 | 🔵 low — common in general English | — |
| 6749 | **imprinted** | 1 | 1 | - | 166.19 | - | 6,389 | - | 0.000279 | 🔵 low — common in general English | — |
| 6750 | **clipping** | 1 | 1 | - | 166.19 | - | 6,390 | - | 0.000279 | 🔵 low — common in general English | — |
| 6751 | **usnisa** | 1 | 1 | - | 166.19 | - | 6,391 | - | 0.000279 | 🔵 low — common in general English | — |
| 6752 | **offering-that** | 1 | 1 | - | 166.19 | - | 6,392 | - | 0.000279 | 🔵 low — common in general English | — |
| 6753 | **ostentation** | 1 | 1 | - | 166.19 | - | 6,393 | - | 0.000279 | 🔵 low — common in general English | — |
| 6754 | **antabhadra** | 1 | 1 | - | 166.19 | - | 6,394 | - | 0.000279 | 🔵 low — common in general English | — |
| 6755 | **musical** | 1 | 1 | - | 166.19 | - | 6,395 | - | 0.000279 | 🔵 low — common in general English | — |
| 6756 | **ema** | 1 | 1 | - | 166.19 | - | 6,396 | - | 0.000279 | 🔵 low — common in general English | — |
| 6757 | **nated** | 1 | 1 | - | 166.19 | - | 6,397 | - | 0.000279 | 🔵 low — common in general English | — |
| 6758 | **multitudinous** | 1 | 1 | - | 166.19 | - | 6,398 | - | 0.000279 | 🔵 low — common in general English | — |
| 6759 | **mani** | 1 | 1 | - | 166.19 | - | 6,399 | - | 0.000279 | 🔵 low — common in general English | ✓ |
| 6760 | **fested** | 1 | 1 | - | 166.19 | - | 6,400 | - | 0.000279 | 🔵 low — common in general English | — |
| 6761 | **cloudbank** | 1 | 1 | - | 166.19 | - | 6,401 | - | 0.000279 | 🔵 low — common in general English | — |
| 6762 | **perfecting** | 1 | 1 | - | 166.19 | - | 6,402 | - | 0.000279 | 🔵 low — common in general English | — |
| 6763 | **unmentionably** | 1 | 1 | - | 166.19 | - | 6,403 | - | 0.000279 | 🔵 low — common in general English | — |
| 6764 | **obstruction** | 1 | 1 | - | 166.19 | - | 6,404 | - | 0.000279 | 🔵 low — common in general English | — |
| 6765 | **doer** | 1 | 1 | - | 166.19 | - | 6,405 | - | 0.000279 | 🔵 low — common in general English | — |
| 6766 | **negative-not** | 1 | 1 | - | 166.19 | - | 6,406 | - | 0.000279 | 🔵 low — common in general English | — |
| 6767 | **ofi** | 1 | 1 | - | 166.19 | - | 6,407 | - | 0.000279 | 🔵 low — common in general English | — |
| 6768 | **nstruction** | 1 | 1 | - | 166.19 | - | 6,408 | - | 0.000279 | 🔵 low — common in general English | — |
| 6769 | **ostentatious** | 1 | 1 | - | 166.19 | - | 6,409 | - | 0.000279 | 🔵 low — common in general English | — |
| 6770 | **merus** | 1 | 1 | - | 166.19 | - | 6,410 | - | 0.000279 | 🔵 low — common in general English | — |
| 6771 | **ungrateful** | 1 | 1 | - | 166.19 | - | 6,411 | - | 0.000279 | 🔵 low — common in general English | — |
| 6772 | **subdivided** | 1 | 1 | - | 166.19 | - | 6,412 | - | 0.000279 | 🔵 low — common in general English | — |
| 6773 | **kriya** | 1 | 1 | - | 166.19 | - | 6,413 | - | 0.000279 | 🔵 low — common in general English | ~ |
| 6774 | **vedic** | 1 | 1 | - | 166.19 | - | 6,414 | - | 0.000279 | 🔵 low — common in general English | — |
| 6775 | **transmutation** | 1 | 1 | - | 166.19 | - | 6,415 | - | 0.000279 | 🔵 low — common in general English | — |
| 6776 | **cunda** | 1 | 1 | - | 166.19 | - | 6,416 | - | 0.000279 | 🔵 low — common in general English | — |
| 6777 | **non-conceptual** | 1 | 1 | - | 166.19 | - | 6,417 | - | 0.000279 | 🔵 low — common in general English | — |
| 6778 | **aigaramati** | 1 | 1 | - | 166.19 | - | 6,418 | - | 0.000279 | 🔵 low — common in general English | — |
| 6779 | **wholeheartedly** | 1 | 1 | - | 166.19 | - | 6,420 | - | 0.000279 | 🔵 low — common in general English | — |
| 6780 | **dedica** | 1 | 1 | - | 166.19 | - | 6,421 | - | 0.000279 | 🔵 low — common in general English | — |
| 6781 | **ofvaisali** | 1 | 1 | - | 166.19 | - | 6,422 | - | 0.000279 | 🔵 low — common in general English | — |
| 6782 | **horrified** | 1 | 1 | - | 166.19 | - | 6,423 | - | 0.000279 | 🔵 low — common in general English | — |
| 6783 | **heruka** | 1 | 1 | - | 166.19 | - | 6,424 | - | 0.000279 | 🔵 low — common in general English | — |
| 6784 | **you-in** | 1 | 1 | - | 166.19 | - | 6,425 | - | 0.000279 | 🔵 low — common in general English | — |
| 6785 | **body-on** | 1 | 1 | - | 166.19 | - | 6,426 | - | 0.000279 | 🔵 low — common in general English | — |
| 6786 | **mala** | 1 | 1 | - | 166.19 | - | 6,427 | - | 0.000279 | 🔵 low — common in general English | — |
| 6787 | **orh** | 1 | 1 | - | 166.19 | - | 6,428 | - | 0.000279 | 🔵 low — common in general English | — |
| 6788 | **moon-crystal** | 1 | 1 | - | 166.19 | - | 6,429 | - | 0.000279 | 🔵 low — common in general English | — |
| 6789 | **actions-taking** | 1 | 1 | - | 166.19 | - | 6,430 | - | 0.000278 | 🔵 low — common in general English | — |
| 6790 | **misconduct-and** | 1 | 1 | - | 166.19 | - | 6,431 | - | 0.000278 | 🔵 low — common in general English | — |
| 6791 | **fro** | 1 | 1 | - | 166.19 | - | 6,432 | - | 0.000278 | 🔵 low — common in general English | — |
| 6792 | **nirm** | 1 | 1 | - | 166.19 | - | 6,433 | - | 0.000278 | 🔵 low — common in general English | — |
| 6793 | **actions-lying** | 1 | 1 | - | 166.19 | - | 6,434 | - | 0.000278 | 🔵 low — common in general English | — |
| 6794 | **chatter-and** | 1 | 1 | - | 166.19 | - | 6,435 | - | 0.000278 | 🔵 low — common in general English | — |
| 6795 | **views-and** | 1 | 1 | - | 166.19 | - | 6,436 | - | 0.000278 | 🔵 low — common in general English | — |
| 6796 | **streak** | 1 | 1 | - | 166.19 | - | 6,437 | - | 0.000278 | 🔵 low — common in general English | — |
| 6797 | **underly** | 1 | 1 | - | 166.19 | - | 6,438 | - | 0.000278 | 🔵 low — common in general English | — |
| 6798 | **svabhavikakaya** | 1 | 1 | - | 166.19 | - | 6,439 | - | 0.000278 | 🔵 low — common in general English | ✓ ངོ་བོ་ཉིད་ཀྱི་སྐུ |
| 6799 | **ardent** | 1 | 1 | - | 166.19 | - | 6,440 | - | 0.000278 | 🔵 low — common in general English | — |
| 6800 | **longing** | 1 | 1 | - | 166.19 | - | 6,441 | - | 0.000278 | 🔵 low — common in general English | — |
| 6801 | **you-up** | 1 | 1 | - | 166.19 | - | 6,442 | - | 0.000278 | 🔵 low — common in general English | — |
| 6802 | **vajrayogini-you** | 1 | 1 | - | 166.19 | - | 6,443 | - | 0.000278 | 🔵 low — common in general English | — |
| 6803 | **overexcited** | 1 | 1 | - | 166.19 | - | 6,444 | - | 0.000278 | 🔵 low — common in general English | — |
| 6804 | **lassitude** | 1 | 1 | - | 166.19 | - | 6,445 | - | 0.000278 | 🔵 low — common in general English | — |
| 6805 | **torpor** | 1 | 1 | - | 166.19 | - | 6,446 | - | 0.000278 | 🔵 low — common in general English | — |
| 6806 | **agitation** | 1 | 1 | - | 166.19 | - | 6,447 | - | 0.000278 | 🔵 low — common in general English | — |
| 6807 | **inseparably** | 1 | 1 | - | 166.19 | - | 6,448 | - | 0.000278 | 🔵 low — common in general English | — |
| 6808 | **naturalness** | 1 | 1 | - | 166.19 | - | 6,449 | - | 0.000278 | 🔵 low — common in general English | — |
| 6809 | **inconceivably** | 1 | 1 | - | 166.19 | - | 6,450 | - | 0.000278 | 🔵 low — common in general English | — |
| 6810 | **charac** | 1 | 1 | - | 166.19 | - | 6,451 | - | 0.000278 | 🔵 low — common in general English | — |
| 6811 | **teristic** | 1 | 1 | - | 166.19 | - | 6,452 | - | 0.000278 | 🔵 low — common in general English | — |
| 6812 | **listener** | 1 | 1 | - | 166.19 | - | 6,453 | - | 0.000278 | 🔵 low — common in general English | — |
| 6813 | **relate-neither** | 1 | 1 | - | 166.19 | - | 6,454 | - | 0.000278 | 🔵 low — common in general English | — |
| 6814 | **detail-the** | 1 | 1 | - | 166.19 | - | 6,455 | - | 0.000278 | 🔵 low — common in general English | — |
| 6815 | **translations-known** | 1 | 1 | - | 166.19 | - | 6,456 | - | 0.000278 | 🔵 low — common in general English | — |
| 6816 | **actualize** | 1 | 1 | - | 166.19 | - | 6,457 | - | 0.000278 | 🔵 low — common in general English | — |
| 6817 | **incon** | 1 | 1 | - | 166.19 | - | 6,458 | - | 0.000278 | 🔵 low — common in general English | — |
| 6818 | **ceivably** | 1 | 1 | - | 166.19 | - | 6,459 | - | 0.000278 | 🔵 low — common in general English | — |
| 6819 | **causal** | 1 | 1 | - | 166.19 | - | 6,460 | - | 0.000278 | 🔵 low — common in general English | — |
| 6820 | **mantrayana-kriya** | 1 | 1 | - | 166.19 | - | 6,461 | - | 0.000278 | 🔵 low — common in general English | — |
| 6821 | **bewilderment** | 1 | 1 | - | 166.19 | - | 6,462 | - | 0.000278 | 🔵 low — common in general English | — |
| 6822 | **doc** | 1 | 1 | - | 166.19 | - | 6,463 | - | 0.000278 | 🔵 low — common in general English | — |
| 6823 | **trine** | 1 | 1 | - | 166.19 | - | 6,464 | - | 0.000278 | 🔵 low — common in general English | — |
| 6824 | **acclaimed** | 1 | 1 | - | 166.19 | - | 6,465 | - | 0.000278 | 🔵 low — common in general English | — |
| 6825 | **kingja** | 1 | 1 | - | 166.19 | - | 6,466 | - | 0.000278 | 🔵 low — common in general English | — |
| 6826 | **nobility** | 1 | 1 | - | 166.19 | - | 6,467 | - | 0.000278 | 🔵 low — common in general English | — |
| 6827 | **lament** | 1 | 1 | - | 166.19 | - | 6,468 | - | 0.000278 | 🔵 low — common in general English | — |
| 6828 | **consented** | 1 | 1 | - | 166.19 | - | 6,469 | - | 0.000278 | 🔵 low — common in general English | — |
| 6829 | **kila** | 1 | 1 | - | 166.19 | - | 6,470 | - | 0.000278 | 🔵 low — common in general English | ✓ ཕུར་བ |
| 6830 | **thotrengtsel** | 1 | 1 | - | 166.19 | - | 6,471 | - | 0.000278 | 🔵 low — common in general English | — |
| 6831 | **devabhadrapala** | 1 | 1 | - | 166.19 | - | 6,472 | - | 0.000277 | 🔵 low — common in general English | — |
| 6832 | **eldest** | 1 | 1 | - | 166.19 | - | 6,473 | - | 0.000277 | 🔵 low — common in general English | — |
| 6833 | **anandagarbha** | 1 | 1 | - | 166.19 | - | 6,474 | - | 0.000277 | 🔵 low — common in general English | ✓ བདེ་མཆོག་སྙིང་པོ |
| 6834 | **devaputra** | 1 | 1 | - | 166.19 | - | 6,475 | - | 0.000277 | 🔵 low — common in general English | — |
| 6835 | **circling** | 1 | 1 | - | 166.19 | - | 6,476 | - | 0.000277 | 🔵 low — common in general English | — |
| 6836 | **pasupati** | 1 | 1 | - | 166.19 | - | 6,477 | - | 0.000277 | 🔵 low — common in general English | — |
| 6837 | **jewel-coloured** | 1 | 1 | - | 166.19 | - | 6,478 | - | 0.000277 | 🔵 low — common in general English | — |
| 6838 | **kausika** | 1 | 1 | - | 166.19 | - | 6,479 | - | 0.000277 | 🔵 low — common in general English | — |
| 6839 | **level-you** | 1 | 1 | - | 166.19 | - | 6,480 | - | 0.000277 | 🔵 low — common in general English | — |
| 6840 | **illuminate** | 1 | 1 | - | 166.19 | - | 6,481 | - | 0.000277 | 🔵 low — common in general English | — |
| 6841 | **symbolized** | 1 | 1 | - | 166.19 | - | 6,482 | - | 0.000277 | 🔵 low — common in general English | — |
| 6842 | **sponta** | 1 | 1 | - | 166.19 | - | 6,483 | - | 0.000277 | 🔵 low — common in general English | — |
| 6843 | **neously** | 1 | 1 | - | 166.19 | - | 6,484 | - | 0.000277 | 🔵 low — common in general English | — |
| 6844 | **primordially** | 1 | 1 | - | 166.19 | - | 6,485 | - | 0.000277 | 🔵 low — common in general English | — |
| 6845 | **vajraloka** | 1 | 1 | - | 166.19 | - | 6,486 | - | 0.000277 | 🔵 low — common in general English | — |
| 6846 | **vajraguhya** | 1 | 1 | - | 166.19 | - | 6,487 | - | 0.000277 | 🔵 low — common in general English | — |
| 6847 | **ratnaloka** | 1 | 1 | - | 166.19 | - | 6,488 | - | 0.000277 | 🔵 low — common in general English | — |
| 6848 | **ratnapada** | 1 | 1 | - | 166.19 | - | 6,489 | - | 0.000277 | 🔵 low — common in general English | — |
| 6849 | **padmakaya** | 1 | 1 | - | 166.19 | - | 6,490 | - | 0.000277 | 🔵 low — common in general English | — |
| 6850 | **padmaprabha** | 1 | 1 | - | 166.19 | - | 6,491 | - | 0.000277 | 🔵 low — common in general English | — |
| 6851 | **atha** | 1 | 1 | - | 166.19 | - | 6,492 | - | 0.000277 | 🔵 low — common in general English | — |
| 6852 | **gata** | 1 | 1 | - | 166.19 | - | 6,493 | - | 0.000277 | 🔵 low — common in general English | — |
| 6853 | **visuddhasiddha** | 1 | 1 | - | 166.19 | - | 6,494 | - | 0.000277 | 🔵 low — common in general English | — |
| 6854 | **siddhyaloka** | 1 | 1 | - | 166.19 | - | 6,495 | - | 0.000277 | 🔵 low — common in general English | — |
| 6855 | **viyoganta** | 1 | 1 | - | 166.19 | - | 6,496 | - | 0.000277 | 🔵 low — common in general English | — |
| 6856 | **irocana** | 1 | 1 | - | 166.19 | - | 6,497 | - | 0.000277 | 🔵 low — common in general English | — |
| 6857 | **all-victorious** | 1 | 1 | - | 166.19 | - | 6,498 | - | 0.000277 | 🔵 low — common in general English | — |
| 6858 | **vajrapal** | 1 | 1 | - | 166.19 | - | 6,499 | - | 0.000277 | 🔵 low — common in general English | — |
| 6859 | **dazzling** | 1 | 1 | - | 166.19 | - | 6,500 | - | 0.000277 | 🔵 low — common in general English | — |
| 6860 | **jewel-encrusted** | 1 | 1 | - | 166.19 | - | 6,501 | - | 0.000277 | 🔵 low — common in general English | — |
| 6861 | **ered** | 1 | 1 | - | 166.19 | - | 6,502 | - | 0.000277 | 🔵 low — common in general English | — |
| 6862 | **heart-son** | 1 | 1 | - | 166.19 | - | 6,503 | - | 0.000277 | 🔵 low — common in general English | — |
| 6863 | **uparaja** | 1 | 1 | - | 166.19 | - | 6,504 | - | 0.000277 | 🔵 low — common in general English | — |
| 6864 | **alokabhasvati** | 1 | 1 | - | 166.19 | - | 6,505 | - | 0.000277 | 🔵 low — common in general English | — |
| 6865 | **hap** | 1 | 1 | - | 166.19 | - | 6,506 | - | 0.000277 | 🔵 low — common in general English | — |
| 6866 | **pened** | 1 | 1 | - | 166.19 | - | 6,507 | - | 0.000277 | 🔵 low — common in general English | — |
| 6867 | **presage** | 1 | 1 | - | 166.19 | - | 6,508 | - | 0.000277 | 🔵 low — common in general English | — |
| 6868 | **gleaming** | 1 | 1 | - | 166.19 | - | 6,509 | - | 0.000277 | 🔵 low — common in general English | — |
| 6869 | **marvelling** | 1 | 1 | - | 166.19 | - | 6,510 | - | 0.000277 | 🔵 low — common in general English | — |
| 6870 | **vajrapaqi** | 1 | 1 | - | 166.19 | - | 6,511 | - | 0.000277 | 🔵 low — common in general English | — |
| 6871 | **twenty-thousand** | 1 | 1 | - | 166.19 | - | 6,512 | - | 0.000277 | 🔵 low — common in general English | — |
| 6872 | **empowered** | 1 | 1 | - | 166.19 | - | 6,513 | - | 0.000277 | 🔵 low — common in general English | — |
| 6873 | **sukhapala** | 1 | 1 | - | 166.19 | - | 6,514 | - | 0.000277 | 🔵 low — common in general English | — |
| 6874 | **kuhana** | 1 | 1 | - | 166.19 | - | 6,515 | - | 0.000276 | 🔵 low — common in general English | — |
| 6875 | **sarasiddhi** | 1 | 1 | - | 166.19 | - | 6,516 | - | 0.000276 | 🔵 low — common in general English | — |
| 6876 | **charnel** | 1 | 1 | - | 166.19 | - | 6,517 | - | 0.000276 | 🔵 low — common in general English | ~ |
| 6877 | **mahahe** | 1 | 1 | - | 166.19 | - | 6,518 | - | 0.000276 | 🔵 low — common in general English | — |
| 6878 | **compiler** | 1 | 1 | - | 166.19 | - | 6,519 | - | 0.000276 | 🔵 low — common in general English | — |
| 6879 | **nir** | 1 | 1 | - | 166.19 | - | 6,520 | - | 0.000276 | 🔵 low — common in general English | — |
| 6880 | **manakaya** | 1 | 1 | - | 166.19 | - | 6,521 | - | 0.000276 | 🔵 low — common in general English | — |
| 6881 | **dare** | 1 | 1 | - | 166.19 | - | 6,522 | - | 0.000276 | 🔵 low — common in general English | — |
| 6882 | **manife** | 1 | 1 | - | 166.19 | - | 6,523 | - | 0.000276 | 🔵 low — common in general English | — |
| 6883 | **uttering** | 1 | 1 | - | 166.19 | - | 6,524 | - | 0.000276 | 🔵 low — common in general English | — |
| 6884 | **polemic** | 1 | 1 | - | 166.19 | - | 6,525 | - | 0.000276 | 🔵 low — common in general English | — |
| 6885 | **compose** | 1 | 1 | - | 166.19 | - | 6,526 | - | 0.000276 | 🔵 low — common in general English | — |
| 6886 | **instantaneous** | 1 | 1 | - | 166.19 | - | 6,527 | - | 0.000276 | 🔵 low — common in general English | — |
| 6887 | **cessation** | 1 | 1 | - | 166.19 | - | 6,528 | - | 0.000276 | 🔵 low — common in general English | — |
| 6888 | **shosha** | 1 | 1 | - | 166.19 | - | 6,529 | - | 0.000276 | 🔵 low — common in general English | — |
| 6889 | **astrology** | 1 | 1 | - | 166.19 | - | 6,530 | - | 0.000276 | 🔵 low — common in general English | — |
| 6890 | **hastibhala** | 1 | 1 | - | 166.19 | - | 6,531 | - | 0.000276 | 🔵 low — common in general English | — |
| 6891 | **jnanasutra** | 1 | 1 | - | 166.19 | - | 6,532 | - | 0.000276 | 🔵 low — common in general English | — |
| 6892 | **pal** | 1 | 1 | - | 166.19 | - | 6,533 | - | 0.000276 | 🔵 low — common in general English | ~ |
| 6893 | **qita** | 1 | 1 | - | 166.19 | - | 6,534 | - | 0.000276 | 🔵 low — common in general English | — |
| 6894 | **tribe** | 1 | 1 | - | 166.19 | - | 6,535 | - | 0.000276 | 🔵 low — common in general English | — |
| 6895 | **descended** | 1 | 1 | - | 166.19 | - | 6,536 | - | 0.000276 | 🔵 low — common in general English | — |
| 6896 | **ape-an** | 1 | 1 | - | 166.19 | - | 6,537 | - | 0.000276 | 🔵 low — common in general English | — |
| 6897 | **crag-demoness** | 1 | 1 | - | 166.19 | - | 6,538 | - | 0.000276 | 🔵 low — common in general English | — |
| 6898 | **chao** | 1 | 1 | - | 166.19 | - | 6,539 | - | 0.000276 | 🔵 low — common in general English | — |
| 6899 | **satanika** | 1 | 1 | - | 166.19 | - | 6,540 | - | 0.000276 | 🔵 low — common in general English | — |
| 6900 | **webbed** | 1 | 1 | - | 166.19 | - | 6,541 | - | 0.000276 | 🔵 low — common in general English | — |
| 6901 | **eyelid** | 1 | 1 | - | 166.19 | - | 6,542 | - | 0.000276 | 🔵 low — common in general English | — |
| 6902 | **banished** | 1 | 1 | - | 166.19 | - | 6,543 | - | 0.000276 | 🔵 low — common in general English | — |
| 6903 | **ancient-nyatri** | 1 | 1 | - | 166.19 | - | 6,544 | - | 0.000276 | 🔵 low — common in general English | — |
| 6904 | **sarvanivaranaviskam** | 1 | 1 | - | 166.19 | - | 6,545 | - | 0.000276 | 🔵 low — common in general English | — |
| 6905 | **bhin** | 1 | 1 | - | 166.19 | - | 6,546 | - | 0.000276 | 🔵 low — common in general English | — |
| 6906 | **yumbu** | 1 | 1 | - | 166.19 | - | 6,547 | - | 0.000276 | 🔵 low — common in general English | — |
| 6907 | **lakhar** | 1 | 1 | - | 166.19 | - | 6,548 | - | 0.000276 | 🔵 low — common in general English | — |
| 6908 | **cintamani** | 1 | 1 | - | 166.19 | - | 6,549 | - | 0.000276 | 🔵 low — common in general English | — |
| 6909 | **kongjo-a** | 1 | 1 | - | 166.19 | - | 6,550 | - | 0.000276 | 🔵 low — common in general English | — |
| 6910 | **tara-and** | 1 | 1 | - | 166.19 | - | 6,551 | - | 0.000276 | 🔵 low — common in general English | — |
| 6911 | **nepalese** | 1 | 1 | - | 166.19 | - | 6,552 | - | 0.000276 | 🔵 low — common in general English | — |
| 6912 | **tritsun-a** | 1 | 1 | - | 166.19 | - | 6,553 | - | 0.000276 | 🔵 low — common in general English | — |
| 6913 | **bhrikuti** | 1 | 1 | - | 166.19 | - | 6,554 | - | 0.000276 | 🔵 low — common in general English | ✓ ཇོ་མོ་ཁྲོ་གཉེར་ཅན |
| 6914 | **devavit** | 1 | 1 | - | 166.19 | - | 6,555 | - | 0.000276 | 🔵 low — common in general English | — |
| 6915 | **sirhha** | 1 | 1 | - | 166.19 | - | 6,556 | - | 0.000276 | 🔵 low — common in general English | — |
| 6916 | **ofj** | 1 | 1 | - | 166.19 | - | 6,557 | - | 0.000276 | 🔵 low — common in general English | — |
| 6917 | **ewel** | 1 | 1 | - | 166.19 | - | 6,558 | - | 0.000275 | 🔵 low — common in general English | — |
| 6918 | **akarmati** | 1 | 1 | - | 166.19 | - | 6,559 | - | 0.000275 | 🔵 low — common in general English | — |
| 6919 | **amradvipa** | 1 | 1 | - | 166.19 | - | 6,560 | - | 0.000275 | 🔵 low — common in general English | — |
| 6920 | **eleven-headed** | 1 | 1 | - | 166.19 | - | 6,561 | - | 0.000275 | 🔵 low — common in general English | — |
| 6921 | **ngam** | 1 | 1 | - | 166.19 | - | 6,562 | - | 0.000275 | 🔵 low — common in general English | — |
| 6922 | **lugong** | 1 | 1 | - | 166.19 | - | 6,563 | - | 0.000275 | 🔵 low — common in general English | — |
| 6923 | **lhazang** | 1 | 1 | - | 166.19 | - | 6,564 | - | 0.000275 | 🔵 low — common in general English | — |
| 6924 | **lupel** | 1 | 1 | - | 166.19 | - | 6,565 | - | 0.000275 | 🔵 low — common in general English | — |
| 6925 | **archive** | 1 | 1 | - | 166.19 | - | 6,566 | - | 0.000275 | 🔵 low — common in general English | — |
| 6926 | **discovering** | 1 | 1 | - | 166.19 | - | 6,567 | - | 0.000275 | 🔵 low — common in general English | — |
| 6927 | **forebear** | 1 | 1 | - | 166.19 | - | 6,568 | - | 0.000275 | 🔵 low — common in general English | — |
| 6928 | **gungtsen** | 1 | 1 | - | 166.19 | - | 6,569 | - | 0.000275 | 🔵 low — common in general English | — |
| 6929 | **nyang** | 1 | 1 | - | 166.19 | - | 6,570 | - | 0.000275 | 🔵 low — common in general English | ~ |
| 6930 | **resided** | 1 | 1 | - | 166.19 | - | 6,571 | - | 0.000275 | 🔵 low — common in general English | — |
| 6931 | **chimpu** | 1 | 1 | - | 166.19 | - | 6,572 | - | 0.000275 | 🔵 low — common in general English | ~ |
| 6932 | **insight** | 1 | 1 | - | 166.19 | - | 6,573 | - | 0.000275 | 🔵 low — common in general English | ~ |
| 6933 | **gomadeviya** | 1 | 1 | - | 166.19 | - | 6,574 | - | 0.000275 | 🔵 low — common in general English | — |
| 6934 | **aryapalo** | 1 | 1 | - | 166.19 | - | 6,575 | - | 0.000275 | 🔵 low — common in general English | — |
| 6935 | **tremble** | 1 | 1 | - | 166.19 | - | 6,576 | - | 0.000275 | 🔵 low — common in general English | — |
| 6936 | **subju** | 1 | 1 | - | 166.19 | - | 6,577 | - | 0.000275 | 🔵 low — common in general English | — |
| 6937 | **sariwari** | 1 | 1 | - | 166.19 | - | 6,578 | - | 0.000275 | 🔵 low — common in general English | — |
| 6938 | **horse-breeder** | 1 | 1 | - | 166.19 | - | 6,579 | - | 0.000275 | 🔵 low — common in general English | — |
| 6939 | **swineherd** | 1 | 1 | - | 166.19 | - | 6,580 | - | 0.000275 | 🔵 low — common in general English | — |
| 6940 | **poultryman** | 1 | 1 | - | 166.19 | - | 6,581 | - | 0.000275 | 🔵 low — common in general English | — |
| 6941 | **dog-breeder** | 1 | 1 | - | 166.19 | - | 6,582 | - | 0.000275 | 🔵 low — common in general English | — |
| 6942 | **trisher** | 1 | 1 | - | 166.19 | - | 6,583 | - | 0.000275 | 🔵 low — common in general English | — |
| 6943 | **dudjom** | 1 | 1 | - | 166.19 | - | 6,584 | - | 0.000275 | 🔵 low — common in general English | — |
| 6944 | **chim** | 1 | 1 | - | 166.19 | - | 6,585 | - | 0.000275 | 🔵 low — common in general English | — |
| 6945 | **sakyaprabha** | 1 | 1 | - | 166.19 | - | 6,586 | - | 0.000275 | 🔵 low — common in general English | — |
| 6946 | **shubu** | 1 | 1 | - | 166.19 | - | 6,587 | - | 0.000275 | 🔵 low — common in general English | ~ |
| 6947 | **palgyi** | 1 | 1 | - | 166.19 | - | 6,588 | - | 0.000275 | 🔵 low — common in general English | ~ |
| 6948 | **senge** | 1 | 1 | - | 166.19 | - | 6,589 | - | 0.000275 | 🔵 low — common in general English | ~ |
| 6949 | **protectress** | 1 | 1 | - | 166.19 | - | 6,590 | - | 0.000275 | 🔵 low — common in general English | — |
| 6950 | **oath** | 1 | 1 | - | 166.19 | - | 6,591 | - | 0.000275 | 🔵 low — common in general English | — |
| 6951 | **trakmar** | 1 | 1 | - | 166.19 | - | 6,592 | - | 0.000275 | 🔵 low — common in general English | — |
| 6952 | **three-storey** | 1 | 1 | - | 166.19 | - | 6,593 | - | 0.000275 | 🔵 low — common in general English | — |
| 6953 | **sub** | 1 | 1 | - | 166.19 | - | 6,594 | - | 0.000275 | 🔵 low — common in general English | — |
| 6954 | **enclosed** | 1 | 1 | - | 166.19 | - | 6,595 | - | 0.000275 | 🔵 low — common in general English | — |
| 6955 | **consecration** | 1 | 1 | - | 166.19 | - | 6,596 | - | 0.000275 | 🔵 low — common in general English | — |
| 6956 | **heart-disciples-the** | 1 | 1 | - | 166.19 | - | 6,597 | - | 0.000275 | 🔵 low — common in general English | — |
| 6957 | **nyangwen** | 1 | 1 | - | 166.19 | - | 6,598 | - | 0.000275 | 🔵 low — common in general English | — |
| 6958 | **antric** | 1 | 1 | - | 166.19 | - | 6,599 | - | 0.000275 | 🔵 low — common in general English | — |
| 6959 | **scroll** | 1 | 1 | - | 166.19 | - | 6,600 | - | 0.000275 | 🔵 low — common in general English | ~ |
| 6960 | **legacy** | 1 | 1 | - | 166.19 | - | 6,601 | - | 0.000275 | 🔵 low — common in general English | — |
| 6961 | **mindtt** | 1 | 1 | - | 166.19 | - | 6,602 | - | 0.000274 | 🔵 low — common in general English | — |
| 6962 | **together-the** | 1 | 1 | - | 166.19 | - | 6,603 | - | 0.000274 | 🔵 low — common in general English | — |
| 6963 | **lineage-from** | 1 | 1 | - | 166.19 | - | 6,604 | - | 0.000274 | 🔵 low — common in general English | — |
| 6964 | **recounting** | 1 | 1 | - | 166.19 | - | 6,605 | - | 0.000274 | 🔵 low — common in general English | — |
| 6965 | **already-with** | 1 | 1 | - | 166.19 | - | 6,606 | - | 0.000274 | 🔵 low — common in general English | — |
| 6966 | **dharma-companion** | 1 | 1 | - | 166.19 | - | 6,607 | - | 0.000274 | 🔵 low — common in general English | — |
| 6967 | **unmi** | 1 | 1 | - | 166.19 | - | 6,608 | - | 0.000274 | 🔵 low — common in general English | — |
| 6968 | **faultless** | 1 | 1 | - | 166.19 | - | 6,609 | - | 0.000274 | 🔵 low — common in general English | — |
| 6969 | **mind-consciousness** | 1 | 1 | - | 166.19 | - | 6,610 | - | 0.000274 | 🔵 low — common in general English | — |
| 6970 | **interme** | 1 | 1 | - | 166.19 | - | 6,611 | - | 0.000274 | 🔵 low — common in general English | — |
| 6971 | **diate** | 1 | 1 | - | 166.19 | - | 6,612 | - | 0.000274 | 🔵 low — common in general English | — |
| 6972 | **it-which** | 1 | 1 | - | 166.19 | - | 6,613 | - | 0.000274 | 🔵 low — common in general English | — |
| 6973 | **despicable** | 1 | 1 | - | 166.19 | - | 6,614 | - | 0.000274 | 🔵 low — common in general English | — |
| 6974 | **protruding** | 1 | 1 | - | 166.19 | - | 6,615 | - | 0.000274 | 🔵 low — common in general English | — |
| 6975 | **crimson** | 1 | 1 | - | 166.19 | - | 6,616 | - | 0.000274 | 🔵 low — common in general English | — |
| 6976 | **pilgrimage** | 1 | 1 | - | 166.19 | - | 6,617 | - | 0.000274 | 🔵 low — common in general English | — |
| 6977 | **incarnate** | 1 | 1 | - | 166.19 | - | 6,618 | - | 0.000274 | 🔵 low — common in general English | — |
| 6978 | **gyurme** | 1 | 1 | - | 166.19 | - | 6,619 | - | 0.000274 | 🔵 low — common in general English | — |
| 6979 | **thekchok** | 1 | 1 | - | 166.19 | - | 6,620 | - | 0.000274 | 🔵 low — common in general English | — |
| 6980 | **trime** | 1 | 1 | - | 166.19 | - | 6,621 | - | 0.000274 | 🔵 low — common in general English | — |
| 6981 | **golok** | 1 | 1 | - | 166.19 | - | 6,622 | - | 0.000274 | 🔵 low — common in general English | — |
| 6982 | **so-and-so** | 1 | 1 | - | 166.19 | - | 6,623 | - | 0.000274 | 🔵 low — common in general English | — |
| 6983 | **confe** | 1 | 1 | - | 166.19 | - | 6,624 | - | 0.000274 | 🔵 low — common in general English | — |
| 6984 | **enthroned** | 1 | 1 | - | 166.19 | - | 6,625 | - | 0.000274 | 🔵 low — common in general English | — |
| 6985 | **life-energy** | 1 | 1 | - | 166.19 | - | 6,626 | - | 0.000274 | 🔵 low — common in general English | — |
| 6986 | **pluck** | 1 | 1 | - | 166.19 | - | 6,627 | - | 0.000274 | 🔵 low — common in general English | — |
| 6987 | **auditory** | 1 | 1 | - | 166.19 | - | 6,628 | - | 0.000274 | 🔵 low — common in general English | — |
| 6988 | **blur** | 1 | 1 | - | 166.19 | - | 6,629 | - | 0.000274 | 🔵 low — common in general English | — |
| 6989 | **salivate** | 1 | 1 | - | 166.19 | - | 6,630 | - | 0.000274 | 🔵 low — common in general English | — |
| 6990 | **extremity** | 1 | 1 | - | 166.19 | - | 6,631 | - | 0.000274 | 🔵 low — common in general English | — |
| 6991 | **energies-the** | 1 | 1 | - | 166.19 | - | 6,632 | - | 0.000274 | 🔵 low — common in general English | — |
| 6992 | **life-supporting** | 1 | 1 | - | 166.19 | - | 6,633 | - | 0.000274 | 🔵 low — common in general English | — |
| 6993 | **life-channel** | 1 | 1 | - | 166.19 | - | 6,634 | - | 0.000274 | 🔵 low — common in general English | — |
| 6994 | **sigh** | 1 | 1 | - | 166.19 | - | 6,635 | - | 0.000274 | 🔵 low — common in general English | — |
| 6995 | **whiteness** | 1 | 1 | - | 166.19 | - | 6,636 | - | 0.000274 | 🔵 low — common in general English | — |
| 6996 | **cloudless** | 1 | 1 | - | 166.19 | - | 6,637 | - | 0.000274 | 🔵 low — common in general English | — |
| 6997 | **redness** | 1 | 1 | - | 166.19 | - | 6,638 | - | 0.000274 | 🔵 low — common in general English | — |
| 6998 | **lustful** | 1 | 1 | - | 166.19 | - | 6,639 | - | 0.000274 | 🔵 low — common in general English | — |
| 6999 | **blackness** | 1 | 1 | - | 166.19 | - | 6,640 | - | 0.000274 | 🔵 low — common in general English | — |
| 7000 | **swoon** | 1 | 1 | - | 166.19 | - | 6,641 | - | 0.000274 | 🔵 low — common in general English | — |
| 7001 | **vajra-posture** | 1 | 1 | - | 166.19 | - | 6,642 | - | 0.000274 | 🔵 low — common in general English | — |
| 7002 | **purpos** | 1 | 1 | - | 166.19 | - | 6,643 | - | 0.000274 | 🔵 low — common in general English | — |
| 7003 | **rattle** | 1 | 1 | - | 166.19 | - | 6,644 | - | 0.000274 | 🔵 low — common in general English | — |
| 7004 | **tent** | 1 | 1 | - | 166.19 | - | 6,645 | - | 0.000274 | 🔵 low — common in general English | — |
| 7005 | **axi** | 1 | 1 | - | 166.19 | - | 6,646 | - | 0.000274 | 🔵 low — common in general English | — |
| 7006 | **mind-con** | 1 | 1 | - | 166.19 | - | 6,647 | - | 0.000273 | 🔵 low — common in general English | — |
| 7007 | **visarga** | 1 | 1 | - | 166.19 | - | 6,648 | - | 0.000273 | 🔵 low — common in general English | — |
| 7008 | **flut** | 1 | 1 | - | 166.19 | - | 6,649 | - | 0.000273 | 🔵 low — common in general English | — |
| 7009 | **tering** | 1 | 1 | - | 166.19 | - | 6,650 | - | 0.000273 | 🔵 low — common in general English | — |
| 7010 | **three-layered** | 1 | 1 | - | 166.19 | - | 6,651 | - | 0.000273 | 🔵 low — common in general English | — |
| 7011 | **embodying** | 1 | 1 | - | 166.19 | - | 6,652 | - | 0.000273 | 🔵 low — common in general English | — |
| 7012 | **clad** | 1 | 1 | - | 166.19 | - | 6,653 | - | 0.000273 | 🔵 low — common in general English | — |
| 7013 | **attire** | 1 | 1 | - | 166.19 | - | 6,654 | - | 0.000273 | 🔵 low — common in general English | — |
| 7014 | **nirmat** | 1 | 1 | - | 166.19 | - | 6,655 | - | 0.000273 | 🔵 low — common in general English | — |
| 7015 | **ursina** | 1 | 1 | - | 166.19 | - | 6,656 | - | 0.000273 | 🔵 low — common in general English | — |
| 7016 | **bead** | 1 | 1 | - | 166.19 | - | 6,657 | - | 0.000273 | 🔵 low — common in general English | — |
| 7017 | **skyward** | 1 | 1 | - | 166.19 | - | 6,658 | - | 0.000273 | 🔵 low — common in general English | — |
| 7018 | **akanistha** | 1 | 1 | - | 166.19 | - | 6,659 | - | 0.000273 | 🔵 low — common in general English | — |
| 7019 | **repre** | 1 | 1 | - | 166.19 | - | 6,660 | - | 0.000273 | 🔵 low — common in general English | — |
| 7020 | **sentation** | 1 | 1 | - | 166.19 | - | 6,661 | - | 0.000273 | 🔵 low — common in general English | — |
| 7021 | **palate** | 1 | 1 | - | 166.19 | - | 6,662 | - | 0.000273 | 🔵 low — common in general English | — |
| 7022 | **grass-stalk** | 1 | 1 | - | 166.19 | - | 6,663 | - | 0.000273 | 🔵 low — common in general English | — |
| 7023 | **nyi** | 1 | 1 | - | 166.19 | - | 6,664 | - | 0.000273 | 🔵 low — common in general English | — |
| 7024 | **iyana** | 1 | 1 | - | 166.19 | - | 6,665 | - | 0.000273 | 🔵 low — common in general English | — |
| 7025 | **palyul** | 1 | 1 | - | 166.19 | - | 6,666 | - | 0.000273 | 🔵 low — common in general English | ~ |
| 7026 | **vajrapdt** | 1 | 1 | - | 166.19 | - | 6,667 | - | 0.000273 | 🔵 low — common in general English | — |
| 7027 | **one-pointed** | 1 | 1 | - | 166.19 | - | 6,668 | - | 0.000273 | 🔵 low — common in general English | — |
| 7028 | **beseech** | 1 | 1 | - | 166.19 | - | 6,669 | - | 0.000273 | 🔵 low — common in general English | — |
| 7029 | **gochen** | 1 | 1 | - | 166.19 | - | 6,670 | - | 0.000273 | 🔵 low — common in general English | — |
| 7030 | **contriving** | 1 | 1 | - | 166.19 | - | 6,671 | - | 0.000273 | 🔵 low — common in general English | — |
| 7031 | **amitayus** | 1 | 1 | - | 166.19 | - | 6,672 | - | 0.000273 | 🔵 low — common in general English | ✓ ཚེ་དཔག་མེད |
| 7032 | **amarani** | 1 | 1 | - | 166.19 | - | 6,673 | - | 0.000273 | 🔵 low — common in general English | — |
| 7033 | **jivantiye** | 1 | 1 | - | 166.19 | - | 6,674 | - | 0.000273 | 🔵 low — common in general English | — |
| 7034 | **svaha** | 1 | 1 | - | 166.19 | - | 6,675 | - | 0.000273 | 🔵 low — common in general English | — |
| 7035 | **and-through** | 1 | 1 | - | 166.19 | - | 6,676 | - | 0.000273 | 🔵 low — common in general English | — |
| 7036 | **inter** | 1 | 1 | - | 166.19 | - | 6,677 | - | 0.000273 | 🔵 low — common in general English | — |
| 7037 | **dependence-dispel** | 1 | 1 | - | 166.19 | - | 6,678 | - | 0.000273 | 🔵 low — common in general English | — |
| 7038 | **ach** | 1 | 1 | - | 166.19 | - | 6,679 | - | 0.000273 | 🔵 low — common in general English | — |
| 7039 | **serum** | 1 | 1 | - | 166.19 | - | 6,680 | - | 0.000273 | 🔵 low — common in general English | — |
| 7040 | **dew** | 1 | 1 | - | 166.19 | - | 6,681 | - | 0.000273 | 🔵 low — common in general English | — |
| 7041 | **stalk** | 1 | 1 | - | 166.19 | - | 6,682 | - | 0.000273 | 🔵 low — common in general English | — |
| 7042 | **assiduously** | 1 | 1 | - | 166.19 | - | 6,683 | - | 0.000273 | 🔵 low — common in general English | — |
| 7043 | **shortcut** | 1 | 1 | - | 166.19 | - | 6,684 | - | 0.000273 | 🔵 low — common in general English | — |
| 7044 | **mutter** | 1 | 1 | - | 166.19 | - | 6,685 | - | 0.000273 | 🔵 low — common in general English | — |
| 7045 | **incoherently** | 1 | 1 | - | 166.19 | - | 6,686 | - | 0.000273 | 🔵 low — common in general English | — |
| 7046 | **interminable** | 1 | 1 | - | 166.19 | - | 6,687 | - | 0.000273 | 🔵 low — common in general English | — |
| 7047 | **goad** | 1 | 1 | - | 166.19 | - | 6,688 | - | 0.000273 | 🔵 low — common in general English | — |
| 7048 | **mination** | 1 | 1 | - | 166.19 | - | 6,689 | - | 0.000273 | 🔵 low — common in general English | — |
| 7049 | **meditation-all** | 1 | 1 | - | 166.19 | - | 6,690 | - | 0.000273 | 🔵 low — common in general English | — |
| 7050 | **creativity** | 1 | 1 | - | 166.19 | - | 6,691 | - | 0.000273 | 🔵 low — common in general English | ~ |
| 7051 | **aesthetic** | 1 | 1 | - | 166.19 | - | 6,692 | - | 0.000272 | 🔵 low — common in general English | — |
| 7052 | **literary** | 1 | 1 | - | 166.19 | - | 6,693 | - | 0.000272 | 🔵 low — common in general English | — |
| 7053 | **banish** | 1 | 1 | - | 166.19 | - | 6,694 | - | 0.000272 | 🔵 low — common in general English | — |
| 7054 | **fabricate** | 1 | 1 | - | 166.19 | - | 6,695 | - | 0.000272 | 🔵 low — common in general English | — |
| 7055 | **watershed** | 1 | 1 | - | 166.19 | - | 6,696 | - | 0.000272 | 🔵 low — common in general English | — |
| 7056 | **evil-even** | 1 | 1 | - | 166.19 | - | 6,697 | - | 0.000272 | 🔵 low — common in general English | — |
| 7057 | **indissolubly** | 1 | 1 | - | 166.19 | - | 6,698 | - | 0.000272 | 🔵 low — common in general English | — |
| 7058 | **clude** | 1 | 1 | - | 166.19 | - | 6,699 | - | 0.000272 | 🔵 low — common in general English | — |
| 7059 | **adulteration** | 1 | 1 | - | 166.19 | - | 6,700 | - | 0.000272 | 🔵 low — common in general English | — |
| 7060 | **well-cooked** | 1 | 1 | - | 166.19 | - | 6,701 | - | 0.000272 | 🔵 low — common in general English | — |
| 7061 | **fancy** | 1 | 1 | - | 166.19 | - | 6,702 | - | 0.000272 | 🔵 low — common in general English | — |
| 7062 | **seasoned** | 1 | 1 | - | 166.19 | - | 6,703 | - | 0.000272 | 🔵 low — common in general English | — |
| 7063 | **savoury** | 1 | 1 | - | 166.19 | - | 6,704 | - | 0.000272 | 🔵 low — common in general English | — |
| 7064 | **cooking-juice** | 1 | 1 | - | 166.19 | - | 6,705 | - | 0.000272 | 🔵 low — common in general English | — |
| 7065 | **ploughshare** | 1 | 1 | - | 166.19 | - | 6,706 | - | 0.000272 | 🔵 low — common in general English | — |
| 7066 | **unearthing** | 1 | 1 | - | 166.19 | - | 6,707 | - | 0.000272 | 🔵 low — common in general English | — |
| 7067 | **nanny** | 1 | 1 | - | 166.19 | - | 6,708 | - | 0.000272 | 🔵 low — common in general English | — |
| 7068 | **uprooting** | 1 | 1 | - | 166.19 | - | 6,709 | - | 0.000272 | 🔵 low — common in general English | — |
| 7069 | **elegance** | 1 | 1 | - | 166.19 | - | 6,710 | - | 0.000272 | 🔵 low — common in general English | — |
| 7070 | **poetry** | 1 | 1 | - | 166.19 | - | 6,711 | - | 0.000272 | 🔵 low — common in general English | — |
| 7071 | **copious** | 1 | 1 | - | 166.19 | - | 6,712 | - | 0.000272 | 🔵 low — common in general English | — |
| 7072 | **cramped** | 1 | 1 | - | 166.19 | - | 6,713 | - | 0.000272 | 🔵 low — common in general English | — |
| 7073 | **discours** | 1 | 1 | - | 166.19 | - | 6,714 | - | 0.000272 | 🔵 low — common in general English | — |
| 7074 | **philosophical** | 1 | 1 | - | 166.19 | - | 6,715 | - | 0.000272 | 🔵 low — common in general English | — |
| 7075 | **soak** | 1 | 1 | - | 166.19 | - | 6,716 | - | 0.000272 | 🔵 low — common in general English | — |
| 7076 | **gloom** | 1 | 1 | - | 166.19 | - | 6,717 | - | 0.000272 | 🔵 low — common in general English | — |
| 7077 | **imperturbable** | 1 | 1 | - | 166.19 | - | 6,718 | - | 0.000272 | 🔵 low — common in general English | — |
| 7078 | **instructor** | 1 | 1 | - | 166.19 | - | 6,719 | - | 0.000272 | 🔵 low — common in general English | — |
| 7079 | **impart** | 1 | 1 | - | 166.19 | - | 6,720 | - | 0.000272 | 🔵 low — common in general English | — |
| 7080 | **savant** | 1 | 1 | - | 166.19 | - | 6,721 | - | 0.000272 | 🔵 low — common in general English | — |
| 7081 | **verbose** | 1 | 1 | - | 166.19 | - | 6,722 | - | 0.000272 | 🔵 low — common in general English | — |
| 7082 | **discourse** | 1 | 1 | - | 166.19 | - | 6,723 | - | 0.000272 | 🔵 low — common in general English | — |
| 7083 | **confection** | 1 | 1 | - | 166.19 | - | 6,724 | - | 0.000272 | 🔵 low — common in general English | — |
| 7084 | **cleverly** | 1 | 1 | - | 166.19 | - | 6,725 | - | 0.000272 | 🔵 low — common in general English | — |
| 7085 | **fanciful** | 1 | 1 | - | 166.19 | - | 6,726 | - | 0.000272 | 🔵 low — common in general English | — |
| 7086 | **superficially** | 1 | 1 | - | 166.19 | - | 6,727 | - | 0.000272 | 🔵 low — common in general English | — |
| 7087 | **vajra-brother** | 1 | 1 | - | 166.19 | - | 6,728 | - | 0.000272 | 🔵 low — common in general English | — |
| 7088 | **compile** | 1 | 1 | - | 166.19 | - | 6,729 | - | 0.000272 | 🔵 low — common in general English | — |
| 7089 | **nourished** | 1 | 1 | - | 166.19 | - | 6,730 | - | 0.000272 | 🔵 low — common in general English | — |
| 7090 | **captivate** | 1 | 1 | - | 166.19 | - | 6,731 | - | 0.000272 | 🔵 low — common in general English | — |
| 7091 | **intoxicating** | 1 | 1 | - | 166.19 | - | 6,732 | - | 0.000272 | 🔵 low — common in general English | — |
| 7092 | **seclusion** | 1 | 1 | - | 166.19 | - | 6,733 | - | 0.000272 | 🔵 low — common in general English | — |
| 7093 | **dronma** | 1 | 1 | - | 166.19 | - | 6,734 | - | 0.000272 | 🔵 low — common in general English | — |
| 7094 | **tsering** | 1 | 1 | - | 166.19 | - | 6,735 | - | 0.000272 | 🔵 low — common in general English | — |
| 7095 | **kunzangthekchok** | 1 | 1 | - | 166.19 | - | 6,736 | - | 0.000272 | 🔵 low — common in general English | — |
| 7096 | **tulku** | 1 | 1 | - | 166.19 | - | 6,737 | - | 0.000272 | 🔵 low — common in general English | ✓ སྤྲུལ་སྐུ |
| 7097 | **peated** | 1 | 1 | - | 166.19 | - | 6,738 | - | 0.000271 | 🔵 low — common in general English | — |
| 7098 | **times-even** | 1 | 1 | - | 166.19 | - | 6,739 | - | 0.000271 | 🔵 low — common in general English | — |
| 7099 | **kushab** | 1 | 1 | - | 166.19 | - | 6,740 | - | 0.000271 | 🔵 low — common in general English | — |
| 7100 | **shenpen** | 1 | 1 | - | 166.19 | - | 6,741 | - | 0.000271 | 🔵 low — common in general English | — |
| 7101 | **thaye** | 1 | 1 | - | 166.19 | - | 6,742 | - | 0.000271 | 🔵 low — common in general English | ~ |
| 7102 | **ozer** | 1 | 1 | - | 166.19 | - | 6,743 | - | 0.000271 | 🔵 low — common in general English | — |
| 7103 | **dharma-sovereign** | 1 | 1 | - | 166.19 | - | 6,744 | - | 0.000271 | 🔵 low — common in general English | — |
| 7104 | **tradition-in** | 1 | 1 | - | 166.19 | - | 6,745 | - | 0.000271 | 🔵 low — common in general English | — |
| 7105 | **changchub** | 1 | 1 | - | 166.19 | - | 6,746 | - | 0.000271 | 🔵 low — common in general English | — |
| 7106 | **cbokyi** | 1 | 1 | - | 166.19 | - | 6,747 | - | 0.000271 | 🔵 low — common in general English | — |
| 7107 | **embellishment** | 1 | 1 | - | 166.19 | - | 6,748 | - | 0.000271 | 🔵 low — common in general English | — |
| 7108 | **rough-mannered** | 1 | 1 | - | 166.19 | - | 6,749 | - | 0.000271 | 🔵 low — common in general English | — |
| 7109 | **rudam** | 1 | 1 | - | 166.19 | - | 6,750 | - | 0.000271 | 🔵 low — common in general English | — |
| 7110 | **samten** | 1 | 1 | - | 166.19 | - | 6,751 | - | 0.000271 | 🔵 low — common in general English | — |
| 7111 | **choling** | 1 | 1 | - | 166.19 | - | 6,752 | - | 0.000271 | 🔵 low — common in general English | — |
| 7112 | **palace-a** | 1 | 1 | - | 166.19 | - | 6,753 | - | 0.000271 | 🔵 low — common in general English | — |
| 7113 | **foliage** | 1 | 1 | - | 166.19 | - | 6,754 | - | 0.000271 | 🔵 low — common in general English | — |
| 7114 | **undergrowth** | 1 | 1 | - | 166.19 | - | 6,755 | - | 0.000271 | 🔵 low — common in general English | — |
| 7115 | **filtering** | 1 | 1 | - | 166.19 | - | 6,756 | - | 0.000271 | 🔵 low — common in general English | — |
| 7116 | **swasti** | 1 | 1 | - | 166.19 | - | 6,757 | - | 0.000271 | 🔵 low — common in general English | — |
| 7117 | **siddham** | 1 | 1 | - | 166.19 | - | 6,758 | - | 0.000271 | 🔵 low — common in general English | — |
| 7118 | **unfolded** | 1 | 1 | - | 166.19 | - | 6,759 | - | 0.000271 | 🔵 low — common in general English | — |
| 7119 | **renowned** | 1 | 1 | - | 166.19 | - | 6,760 | - | 0.000271 | 🔵 low — common in general English | — |
| 7120 | **gyalwai** | 1 | 1 | - | 166.19 | - | 6,761 | - | 0.000271 | 🔵 low — common in general English | — |
| 7121 | **nyugu** | 1 | 1 | - | 166.19 | - | 6,762 | - | 0.000271 | 🔵 low — common in general English | — |
| 7122 | **chokyi** | 1 | 1 | - | 166.19 | - | 6,763 | - | 0.000271 | 🔵 low — common in general English | — |
| 7123 | **lekdrup** | 1 | 1 | - | 166.19 | - | 6,764 | - | 0.000271 | 🔵 low — common in general English | — |
| 7124 | **temporally** | 1 | 1 | - | 166.19 | - | 6,765 | - | 0.000271 | 🔵 low — common in general English | — |
| 7125 | **reduced** | 1 | 2 | - | 166.13 | - | 6,766 | - | 0.000271 | 🔵 low — common in general English | — |
| 7126 | **balance** | 1 | 2 | - | 161.72 | - | 6,767 | - | 0.000271 | 🔵 low — common in general English | — |
| 7127 | **own** | 1 | 2 | - | 160.97 | - | 6,768 | - | 0.000271 | 🔵 low — common in general English | — |
| 7128 | **decision** | 1 | 2 | - | 160.97 | - | 6,769 | - | 0.000271 | 🔵 low — common in general English | ~ |
| 7129 | **contradict** | 1 | 1 | - | 159.22 | - | 6,770 | - | 0.000271 | 🔵 low — common in general English | — |
| 7130 | **lured** | 1 | 1 | - | 159.22 | - | 6,771 | - | 0.000271 | 🔵 low — common in general English | — |
| 7131 | **snapped** | 1 | 1 | - | 159.22 | - | 6,772 | - | 0.000271 | 🔵 low — common in general English | — |
| 7132 | **numerical** | 1 | 1 | - | 159.22 | - | 6,773 | - | 0.000271 | 🔵 low — common in general English | — |
| 7133 | **orientation** | 1 | 1 | - | 159.22 | - | 6,774 | - | 0.000271 | 🔵 low — common in general English | — |
| 7134 | **deprive** | 1 | 1 | - | 159.22 | - | 6,775 | - | 0.000271 | 🔵 low — common in general English | — |
| 7135 | **reasoned** | 1 | 1 | - | 159.22 | - | 6,776 | - | 0.000271 | 🔵 low — common in general English | — |
| 7136 | **disappearance** | 1 | 1 | - | 159.22 | - | 6,777 | - | 0.000271 | 🔵 low — common in general English | — |
| 7137 | **inundated** | 1 | 1 | - | 159.22 | - | 6,778 | - | 0.000271 | 🔵 low — common in general English | — |
| 7138 | **incompatible** | 1 | 1 | - | 159.22 | - | 6,779 | - | 0.000271 | 🔵 low — common in general English | — |
| 7139 | **baring** | 1 | 1 | - | 159.22 | - | 6,780 | - | 0.000271 | 🔵 low — common in general English | — |
| 7140 | **highway** | 1 | 1 | - | 159.22 | - | 6,781 | - | 0.000271 | 🔵 low — common in general English | — |
| 7141 | **transformation** | 1 | 1 | - | 159.22 | - | 6,782 | - | 0.000271 | 🔵 low — common in general English | — |
| 7142 | **pinnacle** | 1 | 1 | - | 159.22 | - | 6,783 | - | 0.000271 | 🔵 low — common in general English | — |
| 7143 | **tri** | 1 | 1 | - | 159.22 | - | 6,784 | - | 0.000271 | 🔵 low — common in general English | — |
| 7144 | **dependable** | 1 | 1 | - | 159.22 | - | 6,785 | - | 0.000270 | 🔵 low — common in general English | — |
| 7145 | **escaped** | 1 | 1 | - | 159.22 | - | 6,786 | - | 0.000270 | 🔵 low — common in general English | — |
| 7146 | **slab** | 1 | 1 | - | 159.22 | - | 6,787 | - | 0.000270 | 🔵 low — common in general English | — |
| 7147 | **dearly** | 1 | 1 | - | 159.22 | - | 6,788 | - | 0.000270 | 🔵 low — common in general English | — |
| 7148 | **transitory** | 1 | 1 | - | 159.22 | - | 6,789 | - | 0.000270 | 🔵 low — common in general English | — |
| 7149 | **rigorous** | 1 | 1 | - | 159.22 | - | 6,790 | - | 0.000270 | 🔵 low — common in general English | — |
| 7150 | **prolong** | 1 | 1 | - | 159.22 | - | 6,791 | - | 0.000270 | 🔵 low — common in general English | — |
| 7151 | **toxic** | 1 | 1 | - | 159.22 | - | 6,792 | - | 0.000270 | 🔵 low — common in general English | — |
| 7152 | **formidable** | 1 | 1 | - | 159.22 | - | 6,794 | - | 0.000270 | 🔵 low — common in general English | — |
| 7153 | **dangerously** | 1 | 1 | - | 159.22 | - | 6,795 | - | 0.000270 | 🔵 low — common in general English | — |
| 7154 | **bribe** | 1 | 1 | - | 159.22 | - | 6,796 | - | 0.000270 | 🔵 low — common in general English | — |
| 7155 | **immune** | 1 | 1 | - | 159.22 | - | 6,797 | - | 0.000270 | 🔵 low — common in general English | — |
| 7156 | **amidst** | 1 | 1 | - | 159.22 | - | 6,798 | - | 0.000270 | 🔵 low — common in general English | — |
| 7157 | **guideline** | 1 | 1 | - | 159.22 | - | 6,799 | - | 0.000270 | 🔵 low — common in general English | — |
| 7158 | **marsh** | 1 | 1 | - | 159.22 | - | 6,800 | - | 0.000270 | 🔵 low — common in general English | — |
| 7159 | **raven** | 1 | 1 | - | 159.22 | - | 6,801 | - | 0.000270 | 🔵 low — common in general English | — |
| 7160 | **purse** | 1 | 1 | - | 159.22 | - | 6,802 | - | 0.000270 | 🔵 low — common in general English | — |
| 7161 | **plying** | 1 | 1 | - | 159.22 | - | 6,803 | - | 0.000270 | 🔵 low — common in general English | — |
| 7162 | **icy** | 1 | 1 | - | 159.22 | - | 6,804 | - | 0.000270 | 🔵 low — common in general English | — |
| 7163 | **evaporated** | 1 | 1 | - | 159.22 | - | 6,805 | - | 0.000270 | 🔵 low — common in general English | — |
| 7164 | **eyed** | 1 | 1 | - | 159.22 | - | 6,806 | - | 0.000270 | 🔵 low — common in general English | — |
| 7165 | **castrated** | 1 | 1 | - | 159.22 | - | 6,807 | - | 0.000270 | 🔵 low — common in general English | — |
| 7166 | **ridden** | 1 | 1 | - | 159.22 | - | 6,808 | - | 0.000270 | 🔵 low — common in general English | — |
| 7167 | **entail** | 1 | 1 | - | 159.22 | - | 6,809 | - | 0.000270 | 🔵 low — common in general English | — |
| 7168 | **bartering** | 1 | 1 | - | 159.22 | - | 6,810 | - | 0.000270 | 🔵 low — common in general English | — |
| 7169 | **crow** | 1 | 1 | - | 159.22 | - | 6,811 | - | 0.000270 | 🔵 low — common in general English | — |
| 7170 | **infant** | 1 | 1 | - | 159.22 | - | 6,812 | - | 0.000270 | 🔵 low — common in general English | — |
| 7171 | **unnoticed** | 1 | 1 | - | 159.22 | - | 6,813 | - | 0.000270 | 🔵 low — common in general English | — |
| 7172 | **integrity** | 1 | 1 | - | 159.22 | - | 6,814 | - | 0.000270 | 🔵 low — common in general English | — |
| 7173 | **occupying** | 1 | 1 | - | 159.22 | - | 6,815 | - | 0.000270 | 🔵 low — common in general English | — |
| 7174 | **charming** | 1 | 1 | - | 159.22 | - | 6,816 | - | 0.000270 | 🔵 low — common in general English | — |
| 7175 | **strife** | 1 | 1 | - | 159.22 | - | 6,817 | - | 0.000270 | 🔵 low — common in general English | — |
| 7176 | **haul** | 1 | 1 | - | 159.22 | - | 6,818 | - | 0.000270 | 🔵 low — common in general English | — |
| 7177 | **outdoor** | 1 | 1 | - | 159.22 | - | 6,819 | - | 0.000270 | 🔵 low — common in general English | — |
| 7178 | **guilty** | 1 | 1 | - | 159.22 | - | 6,820 | - | 0.000270 | 🔵 low — common in general English | — |
| 7179 | **sharpest** | 1 | 1 | - | 159.22 | - | 6,821 | - | 0.000270 | 🔵 low — common in general English | — |
| 7180 | **circulate** | 1 | 1 | - | 159.22 | - | 6,822 | - | 0.000270 | 🔵 low — common in general English | — |
| 7181 | **transferring** | 1 | 1 | - | 159.22 | - | 6,823 | - | 0.000270 | 🔵 low — common in general English | — |
| 7182 | **residue** | 1 | 1 | - | 159.22 | - | 6,824 | - | 0.000270 | 🔵 low — common in general English | — |
| 7183 | **poorer** | 1 | 1 | - | 159.22 | - | 6,825 | - | 0.000270 | 🔵 low — common in general English | — |
| 7184 | **unattractive** | 1 | 1 | - | 159.22 | - | 6,826 | - | 0.000270 | 🔵 low — common in general English | — |
| 7185 | **unjust** | 1 | 1 | - | 159.22 | - | 6,827 | - | 0.000270 | 🔵 low — common in general English | — |
| 7186 | **self-confidence** | 1 | 1 | - | 159.22 | - | 6,828 | - | 0.000270 | 🔵 low — common in general English | — |
| 7187 | **fulfilment** | 1 | 1 | - | 159.22 | - | 6,829 | - | 0.000270 | 🔵 low — common in general English | — |
| 7188 | **propel** | 1 | 1 | - | 159.22 | - | 6,830 | - | 0.000270 | 🔵 low — common in general English | — |
| 7189 | **jam** | 1 | 1 | - | 159.22 | - | 6,831 | - | 0.000270 | 🔵 low — common in general English | — |
| 7190 | **infuse** | 1 | 1 | - | 159.22 | - | 6,832 | - | 0.000269 | 🔵 low — common in general English | — |
| 7191 | **absurd** | 1 | 1 | - | 159.22 | - | 6,833 | - | 0.000269 | 🔵 low — common in general English | — |
| 7192 | **mindful** | 1 | 1 | - | 159.22 | - | 6,834 | - | 0.000269 | 🔵 low — common in general English | — |
| 7193 | **vigilant** | 1 | 1 | - | 159.22 | - | 6,835 | - | 0.000269 | 🔵 low — common in general English | — |
| 7194 | **incumbent** | 1 | 1 | - | 159.22 | - | 6,836 | - | 0.000269 | 🔵 low — common in general English | — |
| 7195 | **decay** | 1 | 1 | - | 159.22 | - | 6,837 | - | 0.000269 | 🔵 low — common in general English | — |
| 7196 | **immensely** | 1 | 1 | - | 159.22 | - | 6,838 | - | 0.000269 | 🔵 low — common in general English | — |
| 7197 | **violently** | 1 | 1 | - | 159.22 | - | 6,839 | - | 0.000269 | 🔵 low — common in general English | — |
| 7198 | **saint** | 1 | 1 | - | 159.22 | - | 6,840 | - | 0.000269 | 🔵 low — common in general English | — |
| 7199 | **honoured** | 1 | 1 | - | 159.22 | - | 6,841 | - | 0.000269 | 🔵 low — common in general English | — |
| 7200 | **piercing** | 1 | 1 | - | 159.22 | - | 6,842 | - | 0.000269 | 🔵 low — common in general English | — |
| 7201 | **forbid** | 1 | 1 | - | 159.22 | - | 6,843 | - | 0.000269 | 🔵 low — common in general English | — |
| 7202 | **wondering** | 1 | 1 | - | 159.22 | - | 6,844 | - | 0.000269 | 🔵 low — common in general English | — |
| 7203 | **tending** | 1 | 1 | - | 159.22 | - | 6,845 | - | 0.000269 | 🔵 low — common in general English | — |
| 7204 | **summoned** | 1 | 1 | - | 159.22 | - | 6,846 | - | 0.000269 | 🔵 low — common in general English | — |
| 7205 | **compelling** | 1 | 1 | - | 159.22 | - | 6,847 | - | 0.000269 | 🔵 low — common in general English | — |
| 7206 | **rosy** | 1 | 1 | - | 159.22 | - | 6,848 | - | 0.000269 | 🔵 low — common in general English | — |
| 7207 | **one-sided** | 1 | 1 | - | 159.22 | - | 6,849 | - | 0.000269 | 🔵 low — common in general English | — |
| 7208 | **sel** | 1 | 1 | - | 159.22 | - | 6,850 | - | 0.000269 | 🔵 low — common in general English | — |
| 7209 | **opponent** | 1 | 1 | - | 159.22 | - | 6,851 | - | 0.000269 | 🔵 low — common in general English | — |
| 7210 | **cheated** | 1 | 1 | - | 159.22 | - | 6,852 | - | 0.000269 | 🔵 low — common in general English | — |
| 7211 | **banquet** | 1 | 1 | - | 159.22 | - | 6,853 | - | 0.000269 | 🔵 low — common in general English | — |
| 7212 | **author** | 1 | 1 | - | 159.22 | - | 6,854 | - | 0.000269 | 🔵 low — common in general English | — |
| 7213 | **stubborn** | 1 | 1 | - | 159.22 | - | 6,855 | - | 0.000269 | 🔵 low — common in general English | — |
| 7214 | **sheltered** | 1 | 1 | - | 159.22 | - | 6,856 | - | 0.000269 | 🔵 low — common in general English | — |
| 7215 | **void** | 1 | 1 | - | 159.22 | - | 6,857 | - | 0.000269 | 🔵 low — common in general English | — |
| 7216 | **viewing** | 1 | 1 | - | 159.22 | - | 6,858 | - | 0.000269 | 🔵 low — common in general English | — |
| 7217 | **slaughtering** | 1 | 1 | - | 159.22 | - | 6,859 | - | 0.000269 | 🔵 low — common in general English | — |
| 7218 | **boarded** | 1 | 1 | - | 159.22 | - | 6,860 | - | 0.000269 | 🔵 low — common in general English | — |
| 7219 | **ludicrous** | 1 | 1 | - | 159.22 | - | 6,861 | - | 0.000269 | 🔵 low — common in general English | — |
| 7220 | **shade** | 1 | 1 | - | 159.22 | - | 6,862 | - | 0.000269 | 🔵 low — common in general English | — |
| 7221 | **grinding** | 1 | 1 | - | 159.22 | - | 6,863 | - | 0.000269 | 🔵 low — common in general English | — |
| 7222 | **invariably** | 1 | 1 | - | 159.22 | - | 6,864 | - | 0.000269 | 🔵 low — common in general English | — |
| 7223 | **detrimental** | 1 | 1 | - | 159.22 | - | 6,865 | - | 0.000269 | 🔵 low — common in general English | — |
| 7224 | **kicking** | 1 | 1 | - | 159.22 | - | 6,866 | - | 0.000269 | 🔵 low — common in general English | — |
| 7225 | **welt** | 1 | 1 | - | 159.22 | - | 6,867 | - | 0.000269 | 🔵 low — common in general English | — |
| 7226 | **charitable** | 1 | 1 | - | 159.22 | - | 6,868 | - | 0.000269 | 🔵 low — common in general English | — |
| 7227 | **mediocre** | 1 | 1 | - | 159.22 | - | 6,869 | - | 0.000269 | 🔵 low — common in general English | — |
| 7228 | **guarding** | 1 | 1 | - | 159.22 | - | 6,870 | - | 0.000269 | 🔵 low — common in general English | — |
| 7229 | **tran** | 1 | 1 | - | 159.22 | - | 6,871 | - | 0.000269 | 🔵 low — common in general English | — |
| 7230 | **counteract** | 1 | 1 | - | 159.22 | - | 6,872 | - | 0.000269 | 🔵 low — common in general English | — |
| 7231 | **bounce** | 1 | 1 | - | 159.22 | - | 6,873 | - | 0.000269 | 🔵 low — common in general English | — |
| 7232 | **print** | 1 | 1 | - | 159.22 | - | 6,874 | - | 0.000269 | 🔵 low — common in general English | — |
| 7233 | **maya** | 1 | 1 | - | 159.22 | - | 6,875 | - | 0.000269 | 🔵 low — common in general English | — |
| 7234 | **stan** | 1 | 1 | - | 159.22 | - | 6,876 | - | 0.000269 | 🔵 low — common in general English | — |
| 7235 | **soaking** | 1 | 1 | - | 159.22 | - | 6,877 | - | 0.000269 | 🔵 low — common in general English | — |
| 7236 | **thickness** | 1 | 1 | - | 159.22 | - | 6,878 | - | 0.000269 | 🔵 low — common in general English | — |
| 7237 | **tumbling** | 1 | 1 | - | 159.22 | - | 6,879 | - | 0.000269 | 🔵 low — common in general English | — |
| 7238 | **finest** | 1 | 1 | - | 159.22 | - | 6,880 | - | 0.000268 | 🔵 low — common in general English | — |
| 7239 | **gratified** | 1 | 1 | - | 159.22 | - | 6,881 | - | 0.000268 | 🔵 low — common in general English | — |
| 7240 | **expose** | 1 | 1 | - | 159.22 | - | 6,882 | - | 0.000268 | 🔵 low — common in general English | — |
| 7241 | **fence** | 1 | 1 | - | 159.22 | - | 6,883 | - | 0.000268 | 🔵 low — common in general English | — |
| 7242 | **straw** | 1 | 1 | - | 159.22 | - | 6,884 | - | 0.000268 | 🔵 low — common in general English | — |
| 7243 | **deplete** | 1 | 1 | - | 159.22 | - | 6,885 | - | 0.000268 | 🔵 low — common in general English | — |
| 7244 | **rushing** | 1 | 1 | - | 159.22 | - | 6,886 | - | 0.000268 | 🔵 low — common in general English | — |
| 7245 | **confront** | 1 | 1 | - | 159.22 | - | 6,887 | - | 0.000268 | 🔵 low — common in general English | — |
| 7246 | **vertical** | 1 | 1 | - | 159.22 | - | 6,888 | - | 0.000268 | 🔵 low — common in general English | — |
| 7247 | **fifteen** | 1 | 1 | - | 159.22 | - | 6,889 | - | 0.000268 | 🔵 low — common in general English | — |
| 7248 | **chopping** | 1 | 1 | - | 159.22 | - | 6,890 | - | 0.000268 | 🔵 low — common in general English | — |
| 7249 | **deepen** | 1 | 1 | - | 159.22 | - | 6,891 | - | 0.000268 | 🔵 low — common in general English | — |
| 7250 | **surrender** | 1 | 1 | - | 159.22 | - | 6,892 | - | 0.000268 | 🔵 low — common in general English | — |
| 7251 | **south-west** | 1 | 1 | - | 159.22 | - | 6,893 | - | 0.000268 | 🔵 low — common in general English | — |
| 7252 | **layer** | 1 | 1 | - | 159.22 | - | 6,894 | - | 0.000268 | 🔵 low — common in general English | — |
| 7253 | **confidently** | 1 | 1 | - | 159.22 | - | 6,895 | - | 0.000268 | 🔵 low — common in general English | — |
| 7254 | **respected** | 1 | 1 | - | 159.22 | - | 6,896 | - | 0.000268 | 🔵 low — common in general English | — |
| 7255 | **midst** | 1 | 1 | - | 159.22 | - | 6,897 | - | 0.000268 | 🔵 low — common in general English | — |
| 7256 | **concluding** | 1 | 1 | - | 159.22 | - | 6,898 | - | 0.000268 | 🔵 low — common in general English | — |
| 7257 | **ame** | 1 | 1 | - | 159.22 | - | 6,899 | - | 0.000268 | 🔵 low — common in general English | — |
| 7258 | **displayed** | 1 | 1 | - | 159.22 | - | 6,900 | - | 0.000268 | 🔵 low — common in general English | — |
| 7259 | **hut** | 1 | 1 | - | 159.22 | - | 6,901 | - | 0.000268 | 🔵 low — common in general English | — |
| 7260 | **berry** | 1 | 1 | - | 159.22 | - | 6,902 | - | 0.000268 | 🔵 low — common in general English | — |
| 7261 | **opportune** | 1 | 1 | - | 159.22 | - | 6,903 | - | 0.000268 | 🔵 low — common in general English | — |
| 7262 | **obscuring** | 1 | 1 | - | 159.22 | - | 6,904 | - | 0.000268 | 🔵 low — common in general English | — |
| 7263 | **contradictory** | 1 | 1 | - | 159.22 | - | 6,905 | - | 0.000268 | 🔵 low — common in general English | — |
| 7264 | **evacuation** | 1 | 1 | - | 159.22 | - | 6,906 | - | 0.000268 | 🔵 low — common in general English | — |
| 7265 | **erect** | 1 | 1 | - | 159.22 | - | 6,907 | - | 0.000268 | 🔵 low — common in general English | — |
| 7266 | **leaning** | 1 | 1 | - | 159.22 | - | 6,908 | - | 0.000268 | 🔵 low — common in general English | — |
| 7267 | **regent** | 1 | 1 | - | 159.22 | - | 6,909 | - | 0.000268 | 🔵 low — common in general English | — |
| 7268 | **henceforth** | 1 | 1 | - | 159.22 | - | 6,910 | - | 0.000268 | 🔵 low — common in general English | — |
| 7269 | **market** | 1 | 3 | - | 156.83 | - | 6,911 | - | 0.000268 | 🔵 low — common in general English | — |
| 7270 | **wheat** | 1 | 2 | - | 155.84 | - | 6,912 | - | 0.000268 | 🔵 low — common in general English | — |
| 7271 | **owned** | 1 | 2 | - | 154.29 | - | 6,913 | - | 0.000268 | 🔵 low — common in general English | — |
| 7272 | **seize** | 1 | 1 | - | 154.24 | - | 6,914 | - | 0.000268 | 🔵 low — common in general English | — |
| 7273 | **aged** | 1 | 1 | - | 154.24 | - | 6,915 | - | 0.000268 | 🔵 low — common in general English | — |
| 7274 | **undue** | 1 | 1 | - | 154.24 | - | 6,916 | - | 0.000268 | 🔵 low — common in general English | — |
| 7275 | **extracted** | 1 | 1 | - | 154.24 | - | 6,917 | - | 0.000268 | 🔵 low — common in general English | — |
| 7276 | **thorough** | 1 | 1 | - | 154.24 | - | 6,918 | - | 0.000268 | 🔵 low — common in general English | — |
| 7277 | **translation** | 1 | 1 | - | 154.24 | - | 6,919 | - | 0.000268 | 🔵 low — common in general English | — |
| 7278 | **eastward** | 1 | 1 | - | 154.24 | - | 6,920 | - | 0.000268 | 🔵 low — common in general English | — |
| 7279 | **erected** | 1 | 1 | - | 154.24 | - | 6,921 | - | 0.000268 | 🔵 low — common in general English | — |
| 7280 | **wilderness** | 1 | 1 | - | 154.24 | - | 6,922 | - | 0.000268 | 🔵 low — common in general English | — |
| 7281 | **contentious** | 1 | 1 | - | 154.24 | - | 6,923 | - | 0.000268 | 🔵 low — common in general English | — |
| 7282 | **student** | 1 | 1 | - | 154.24 | - | 6,924 | - | 0.000268 | 🔵 low — common in general English | — |
| 7283 | **wax** | 1 | 1 | - | 154.24 | - | 6,925 | - | 0.000268 | 🔵 low — common in general English | — |
| 7284 | **diet** | 1 | 1 | - | 154.24 | - | 6,926 | - | 0.000268 | 🔵 low — common in general English | — |
| 7285 | **als** | 1 | 1 | - | 154.24 | - | 6,927 | - | 0.000268 | 🔵 low — common in general English | — |
| 7286 | **pause** | 1 | 1 | - | 154.24 | - | 6,928 | - | 0.000267 | 🔵 low — common in general English | — |
| 7287 | **judging** | 1 | 1 | - | 154.24 | - | 6,929 | - | 0.000267 | 🔵 low — common in general English | — |
| 7288 | **prelude** | 1 | 1 | - | 154.24 | - | 6,930 | - | 0.000267 | 🔵 low — common in general English | — |
| 7289 | **ham** | 1 | 1 | - | 154.24 | - | 6,931 | - | 0.000267 | 🔵 low — common in general English | — |
| 7290 | **exit** | 1 | 1 | - | 154.24 | - | 6,932 | - | 0.000267 | 🔵 low — common in general English | — |
| 7291 | **ditch** | 1 | 1 | - | 154.24 | - | 6,933 | - | 0.000267 | 🔵 low — common in general English | — |
| 7292 | **erupt** | 1 | 1 | - | 154.24 | - | 6,934 | - | 0.000267 | 🔵 low — common in general English | — |
| 7293 | **fashion** | 1 | 1 | - | 154.24 | - | 6,935 | - | 0.000267 | 🔵 low — common in general English | — |
| 7294 | **alike** | 1 | 1 | - | 154.24 | - | 6,936 | - | 0.000267 | 🔵 low — common in general English | — |
| 7295 | **porter** | 1 | 1 | - | 154.24 | - | 6,937 | - | 0.000267 | 🔵 low — common in general English | — |
| 7296 | **stall** | 1 | 1 | - | 154.24 | - | 6,938 | - | 0.000267 | 🔵 low — common in general English | — |
| 7297 | **demonstrating** | 1 | 1 | - | 154.24 | - | 6,939 | - | 0.000267 | 🔵 low — common in general English | — |
| 7298 | **tumble** | 1 | 1 | - | 154.24 | - | 6,941 | - | 0.000267 | 🔵 low — common in general English | — |
| 7299 | **overtly** | 1 | 1 | - | 154.24 | - | 6,943 | - | 0.000267 | 🔵 low — common in general English | — |
| 7300 | **untrue** | 1 | 1 | - | 154.24 | - | 6,944 | - | 0.000267 | 🔵 low — common in general English | — |
| 7301 | **diverse** | 1 | 1 | - | 154.24 | - | 6,945 | - | 0.000267 | 🔵 low — common in general English | — |
| 7302 | **emotional** | 1 | 1 | - | 154.24 | - | 6,946 | - | 0.000267 | 🔵 low — common in general English | — |
| 7303 | **choosing** | 1 | 1 | - | 154.24 | - | 6,947 | - | 0.000267 | 🔵 low — common in general English | — |
| 7304 | **contravened** | 1 | 1 | - | 154.24 | - | 6,948 | - | 0.000267 | 🔵 low — common in general English | — |
| 7305 | **disturbing** | 1 | 1 | - | 154.24 | - | 6,949 | - | 0.000267 | 🔵 low — common in general English | — |
| 7306 | **mas** | 1 | 1 | - | 154.24 | - | 6,950 | - | 0.000267 | 🔵 low — common in general English | — |
| 7307 | **fasting** | 1 | 1 | - | 154.24 | - | 6,951 | - | 0.000267 | 🔵 low — common in general English | — |
| 7308 | **wondered** | 1 | 1 | - | 154.24 | - | 6,952 | - | 0.000267 | 🔵 low — common in general English | — |
| 7309 | **crashed** | 1 | 1 | - | 154.24 | - | 6,953 | - | 0.000267 | 🔵 low — common in general English | — |
| 7310 | **undergone** | 1 | 1 | - | 154.24 | - | 6,954 | - | 0.000267 | 🔵 low — common in general English | — |
| 7311 | **suicide** | 1 | 1 | - | 154.24 | - | 6,955 | - | 0.000267 | 🔵 low — common in general English | — |
| 7312 | **hardest** | 1 | 1 | - | 154.24 | - | 6,956 | - | 0.000267 | 🔵 low — common in general English | — |
| 7313 | **desperately** | 1 | 1 | - | 154.24 | - | 6,957 | - | 0.000267 | 🔵 low — common in general English | — |
| 7314 | **precipitous** | 1 | 1 | - | 154.24 | - | 6,958 | - | 0.000267 | 🔵 low — common in general English | — |
| 7315 | **whereby** | 1 | 1 | - | 154.24 | - | 6,959 | - | 0.000267 | 🔵 low — common in general English | — |
| 7316 | **progressed** | 1 | 1 | - | 154.24 | - | 6,960 | - | 0.000267 | 🔵 low — common in general English | — |
| 7317 | **catching** | 1 | 1 | - | 154.24 | - | 6,961 | - | 0.000267 | 🔵 low — common in general English | — |
| 7318 | **chronic** | 1 | 1 | - | 154.24 | - | 6,962 | - | 0.000267 | 🔵 low — common in general English | — |
| 7319 | **bare** | 1 | 1 | - | 154.24 | - | 6,963 | - | 0.000267 | 🔵 low — common in general English | — |
| 7320 | **hanging** | 1 | 1 | - | 154.24 | - | 6,964 | - | 0.000267 | 🔵 low — common in general English | — |
| 7321 | **trailing** | 1 | 1 | - | 154.24 | - | 6,965 | - | 0.000267 | 🔵 low — common in general English | — |
| 7322 | **materialize** | 1 | 1 | - | 154.24 | - | 6,966 | - | 0.000267 | 🔵 low — common in general English | — |
| 7323 | **crossing** | 1 | 1 | - | 154.24 | - | 6,967 | - | 0.000267 | 🔵 low — common in general English | — |
| 7324 | **dressing** | 1 | 1 | - | 154.24 | - | 6,968 | - | 0.000267 | 🔵 low — common in general English | — |
| 7325 | **luck** | 1 | 1 | - | 154.24 | - | 6,969 | - | 0.000267 | 🔵 low — common in general English | — |
| 7326 | **dashed** | 1 | 1 | - | 154.24 | - | 6,970 | - | 0.000267 | 🔵 low — common in general English | — |
| 7327 | **fled** | 1 | 1 | - | 154.24 | - | 6,971 | - | 0.000267 | 🔵 low — common in general English | — |
| 7328 | **analyzing** | 1 | 1 | - | 154.24 | - | 6,972 | - | 0.000267 | 🔵 low — common in general English | — |
| 7329 | **dimmed** | 1 | 1 | - | 154.24 | - | 6,973 | - | 0.000267 | 🔵 low — common in general English | — |
| 7330 | **favouring** | 1 | 1 | - | 154.24 | - | 6,974 | - | 0.000267 | 🔵 low — common in general English | — |
| 7331 | **naive** | 1 | 1 | - | 154.24 | - | 6,975 | - | 0.000267 | 🔵 low — common in general English | — |
| 7332 | **climbing** | 1 | 1 | - | 154.24 | - | 6,976 | - | 0.000267 | 🔵 low — common in general English | — |
| 7333 | **affirmed** | 1 | 1 | - | 154.24 | - | 6,977 | - | 0.000266 | 🔵 low — common in general English | — |
| 7334 | **pel** | 1 | 1 | - | 154.24 | - | 6,978 | - | 0.000266 | 🔵 low — common in general English | — |
| 7335 | **frightening** | 1 | 1 | - | 154.24 | - | 6,979 | - | 0.000266 | 🔵 low — common in general English | — |
| 7336 | **wipe** | 1 | 1 | - | 154.24 | - | 6,980 | - | 0.000266 | 🔵 low — common in general English | — |
| 7337 | **cleaned** | 1 | 1 | - | 154.24 | - | 6,981 | - | 0.000266 | 🔵 low — common in general English | — |
| 7338 | **thirdly** | 1 | 1 | - | 154.24 | - | 6,982 | - | 0.000266 | 🔵 low — common in general English | — |
| 7339 | **extracting** | 1 | 1 | - | 154.24 | - | 6,983 | - | 0.000266 | 🔵 low — common in general English | ~ |
| 7340 | **deadly** | 1 | 1 | - | 154.24 | - | 6,984 | - | 0.000266 | 🔵 low — common in general English | — |
| 7341 | **violence** | 1 | 1 | - | 154.24 | - | 6,985 | - | 0.000266 | 🔵 low — common in general English | — |
| 7342 | **cape** | 1 | 1 | - | 154.24 | - | 6,986 | - | 0.000266 | 🔵 low — common in general English | — |
| 7343 | **chas** | 1 | 1 | - | 154.24 | - | 6,987 | - | 0.000266 | 🔵 low — common in general English | — |
| 7344 | **discouraging** | 1 | 1 | - | 154.24 | - | 6,988 | - | 0.000266 | 🔵 low — common in general English | — |
| 7345 | **realizing** | 1 | 1 | - | 154.24 | - | 6,989 | - | 0.000266 | 🔵 low — common in general English | — |
| 7346 | **symbolic** | 1 | 1 | - | 154.24 | - | 6,990 | - | 0.000266 | 🔵 low — common in general English | — |
| 7347 | **distilled** | 1 | 1 | - | 154.24 | - | 6,991 | - | 0.000266 | 🔵 low — common in general English | — |
| 7348 | **misunderstanding** | 1 | 1 | - | 154.24 | - | 6,992 | - | 0.000266 | 🔵 low — common in general English | — |
| 7349 | **ripe** | 1 | 1 | - | 154.24 | - | 6,993 | - | 0.000266 | 🔵 low — common in general English | — |
| 7350 | **predominantly** | 1 | 1 | - | 154.24 | - | 6,994 | - | 0.000266 | 🔵 low — common in general English | — |
| 7351 | **swelling** | 1 | 1 | - | 154.24 | - | 6,995 | - | 0.000266 | 🔵 low — common in general English | — |
| 7352 | **intermediary** | 1 | 1 | - | 154.24 | - | 6,996 | - | 0.000266 | 🔵 low — common in general English | — |
| 7353 | **evolution** | 1 | 1 | - | 154.24 | - | 6,997 | - | 0.000266 | 🔵 low — common in general English | — |
| 7354 | **convey** | 1 | 1 | - | 154.24 | - | 6,998 | - | 0.000266 | 🔵 low — common in general English | — |
| 7355 | **accrue** | 1 | 1 | - | 154.24 | - | 6,999 | - | 0.000266 | 🔵 low — common in general English | — |
| 7356 | **new** | 1 | 3 | - | 151.18 | - | 7,000 | - | 0.000266 | 🔵 low — common in general English | ~ |
| 7357 | **focussing** | 1 | 1 | - | 150.37 | - | 7,001 | - | 0.000266 | 🔵 low — common in general English | — |
| 7358 | **impeded** | 1 | 1 | - | 150.37 | - | 7,002 | - | 0.000266 | 🔵 low — common in general English | — |
| 7359 | **silent** | 1 | 1 | - | 150.37 | - | 7,003 | - | 0.000266 | 🔵 low — common in general English | — |
| 7360 | **sheer** | 1 | 1 | - | 150.37 | - | 7,004 | - | 0.000266 | 🔵 low — common in general English | — |
| 7361 | **recede** | 1 | 1 | - | 150.37 | - | 7,005 | - | 0.000266 | 🔵 low — common in general English | — |
| 7362 | **blown** | 1 | 1 | - | 150.37 | - | 7,006 | - | 0.000266 | 🔵 low — common in general English | — |
| 7363 | **bubble** | 1 | 1 | - | 150.37 | - | 7,007 | - | 0.000266 | 🔵 low — common in general English | — |
| 7364 | **recourse** | 1 | 1 | - | 150.37 | - | 7,008 | - | 0.000266 | 🔵 low — common in general English | — |
| 7365 | **marking** | 1 | 1 | - | 150.37 | - | 7,009 | - | 0.000266 | 🔵 low — common in general English | — |
| 7366 | **cooler** | 1 | 1 | - | 150.37 | - | 7,010 | - | 0.000266 | 🔵 low — common in general English | — |
| 7367 | **constructed** | 1 | 1 | - | 150.37 | - | 7,011 | - | 0.000266 | 🔵 low — common in general English | — |
| 7368 | **wane** | 1 | 1 | - | 150.37 | - | 7,012 | - | 0.000266 | 🔵 low — common in general English | — |
| 7369 | **malt** | 1 | 1 | - | 150.37 | - | 7,013 | - | 0.000266 | 🔵 low — common in general English | — |
| 7370 | **freezing** | 1 | 1 | - | 150.37 | - | 7,014 | - | 0.000266 | 🔵 low — common in general English | — |
| 7371 | **mattress** | 1 | 1 | - | 150.37 | - | 7,015 | - | 0.000266 | 🔵 low — common in general English | — |
| 7372 | **await** | 1 | 1 | - | 150.37 | - | 7,016 | - | 0.000266 | 🔵 low — common in general English | — |
| 7373 | **rebel** | 1 | 1 | - | 150.37 | - | 7,017 | - | 0.000266 | 🔵 low — common in general English | — |
| 7374 | **hospitality** | 1 | 1 | - | 150.37 | - | 7,018 | - | 0.000266 | 🔵 low — common in general English | — |
| 7375 | **foreshadow** | 1 | 1 | - | 150.37 | - | 7,019 | - | 0.000266 | 🔵 low — common in general English | — |
| 7376 | **persuaded** | 1 | 1 | - | 150.37 | - | 7,020 | - | 0.000266 | 🔵 low — common in general English | — |
| 7377 | **yard** | 1 | 1 | - | 150.37 | - | 7,021 | - | 0.000266 | 🔵 low — common in general English | — |
| 7378 | **intermittent** | 1 | 1 | - | 150.37 | - | 7,022 | - | 0.000266 | 🔵 low — common in general English | — |
| 7379 | **emp** | 1 | 1 | - | 150.37 | - | 7,023 | - | 0.000266 | 🔵 low — common in general English | — |
| 7380 | **drifting** | 1 | 1 | - | 150.37 | - | 7,024 | - | 0.000266 | 🔵 low — common in general English | — |
| 7381 | **fragrance** | 1 | 1 | - | 150.37 | - | 7,025 | - | 0.000266 | 🔵 low — common in general English | — |
| 7382 | **ink** | 1 | 1 | - | 150.37 | - | 7,026 | - | 0.000266 | 🔵 low — common in general English | — |
| 7383 | **walked** | 1 | 1 | - | 150.37 | - | 7,027 | - | 0.000265 | 🔵 low — common in general English | — |
| 7384 | **pre** | 1 | 1 | - | 150.37 | - | 7,028 | - | 0.000265 | 🔵 low — common in general English | — |
| 7385 | **dole** | 1 | 1 | - | 150.37 | - | 7,029 | - | 0.000265 | 🔵 low — common in general English | — |
| 7386 | **hung** | 1 | 1 | - | 150.37 | - | 7,030 | - | 0.000265 | 🔵 low — common in general English | — |
| 7387 | **inviting** | 1 | 1 | - | 150.37 | - | 7,031 | - | 0.000265 | 🔵 low — common in general English | — |
| 7388 | **dragging** | 1 | 1 | - | 150.37 | - | 7,032 | - | 0.000265 | 🔵 low — common in general English | — |
| 7389 | **theme** | 1 | 1 | - | 150.37 | - | 7,033 | - | 0.000265 | 🔵 low — common in general English | — |
| 7390 | **reciprocal** | 1 | 1 | - | 150.37 | - | 7,034 | - | 0.000265 | 🔵 low — common in general English | — |
| 7391 | **individually** | 1 | 1 | - | 150.37 | - | 7,035 | - | 0.000265 | 🔵 low — common in general English | — |
| 7392 | **flank** | 1 | 1 | - | 150.37 | - | 7,036 | - | 0.000265 | 🔵 low — common in general English | — |
| 7393 | **fatty** | 1 | 1 | - | 150.37 | - | 7,037 | - | 0.000265 | 🔵 low — common in general English | — |
| 7394 | **ablaze** | 1 | 1 | - | 150.37 | - | 7,038 | - | 0.000265 | 🔵 low — common in general English | — |
| 7395 | **catapulted** | 1 | 1 | - | 150.37 | - | 7,039 | - | 0.000265 | 🔵 low — common in general English | — |
| 7396 | **dom** | 1 | 1 | - | 150.37 | - | 7,040 | - | 0.000265 | 🔵 low — common in general English | — |
| 7397 | **waited** | 1 | 1 | - | 150.37 | - | 7,041 | - | 0.000265 | 🔵 low — common in general English | — |
| 7398 | **prejudice** | 1 | 1 | - | 150.37 | - | 7,042 | - | 0.000265 | 🔵 low — common in general English | — |
| 7399 | **relaxing** | 1 | 1 | - | 150.37 | - | 7,043 | - | 0.000265 | 🔵 low — common in general English | — |
| 7400 | **annoyed** | 1 | 1 | - | 150.37 | - | 7,044 | - | 0.000265 | 🔵 low — common in general English | — |
| 7401 | **grazing** | 1 | 1 | - | 150.37 | - | 7,045 | - | 0.000265 | 🔵 low — common in general English | — |
| 7402 | **honesty** | 1 | 1 | - | 150.37 | - | 7,046 | - | 0.000265 | 🔵 low — common in general English | — |
| 7403 | **prudence** | 1 | 1 | - | 150.37 | - | 7,047 | - | 0.000265 | 🔵 low — common in general English | — |
| 7404 | **ted** | 1 | 1 | - | 150.37 | - | 7,048 | - | 0.000265 | 🔵 low — common in general English | — |
| 7405 | **sponsor** | 1 | 1 | - | 150.37 | - | 7,049 | - | 0.000265 | 🔵 low — common in general English | — |
| 7406 | **ideally** | 1 | 1 | - | 150.37 | - | 7,050 | - | 0.000265 | 🔵 low — common in general English | — |
| 7407 | **gravel** | 1 | 1 | - | 150.37 | - | 7,051 | - | 0.000265 | 🔵 low — common in general English | — |
| 7408 | **feasible** | 1 | 1 | - | 150.37 | - | 7,052 | - | 0.000265 | 🔵 low — common in general English | — |
| 7409 | **noticeable** | 1 | 1 | - | 150.37 | - | 7,053 | - | 0.000265 | 🔵 low — common in general English | — |
| 7410 | **tenth** | 1 | 1 | - | 150.37 | - | 7,054 | - | 0.000265 | 🔵 low — common in general English | — |
| 7411 | **sara** | 1 | 1 | - | 150.37 | - | 7,055 | - | 0.000265 | 🔵 low — common in general English | — |
| 7412 | **surpassing** | 1 | 1 | - | 150.37 | - | 7,056 | - | 0.000265 | 🔵 low — common in general English | — |
| 7413 | **unrealized** | 1 | 1 | - | 150.37 | - | 7,057 | - | 0.000265 | 🔵 low — common in general English | — |
| 7414 | **omitted** | 1 | 1 | - | 150.37 | - | 7,058 | - | 0.000265 | 🔵 low — common in general English | — |
| 7415 | **collected** | 1 | 1 | - | 150.37 | - | 7,059 | - | 0.000265 | 🔵 low — common in general English | — |
| 7416 | **demand** | 1 | 2 | - | 147.75 | - | 7,060 | - | 0.000265 | 🔵 low — common in general English | — |
| 7417 | **encountered** | 1 | 1 | - | 147.21 | - | 7,061 | - | 0.000265 | 🔵 low — common in general English | — |
| 7418 | **entrance** | 1 | 1 | - | 147.21 | - | 7,062 | - | 0.000265 | 🔵 low — common in general English | — |
| 7419 | **analyze** | 1 | 1 | - | 147.21 | - | 7,063 | - | 0.000265 | 🔵 low — common in general English | — |
| 7420 | **span** | 1 | 1 | - | 147.21 | - | 7,064 | - | 0.000265 | 🔵 low — common in general English | — |
| 7421 | **reassure** | 1 | 1 | - | 147.21 | - | 7,065 | - | 0.000265 | 🔵 low — common in general English | — |
| 7422 | **suspected** | 1 | 1 | - | 147.21 | - | 7,066 | - | 0.000265 | 🔵 low — common in general English | — |
| 7423 | **flurry** | 1 | 1 | - | 147.21 | - | 7,067 | - | 0.000265 | 🔵 low — common in general English | — |
| 7424 | **hal** | 1 | 1 | - | 147.21 | - | 7,068 | - | 0.000265 | 🔵 low — common in general English | — |
| 7425 | **herd** | 1 | 1 | - | 147.21 | - | 7,069 | - | 0.000265 | 🔵 low — common in general English | — |
| 7426 | **rescued** | 1 | 1 | - | 147.21 | - | 7,070 | - | 0.000265 | 🔵 low — common in general English | — |
| 7427 | **employing** | 1 | 1 | - | 147.21 | - | 7,071 | - | 0.000265 | 🔵 low — common in general English | — |
| 7428 | **intensity** | 1 | 1 | - | 147.21 | - | 7,072 | - | 0.000265 | 🔵 low — common in general English | — |
| 7429 | **fox** | 1 | 1 | - | 147.21 | - | 7,073 | - | 0.000265 | 🔵 low — common in general English | — |
| 7430 | **lapse** | 1 | 1 | - | 147.21 | - | 7,074 | - | 0.000265 | 🔵 low — common in general English | — |
| 7431 | **reception** | 1 | 1 | - | 147.21 | - | 7,075 | - | 0.000265 | 🔵 low — common in general English | — |
| 7432 | **practically** | 1 | 1 | - | 147.21 | - | 7,076 | - | 0.000265 | 🔵 low — common in general English | — |
| 7433 | **thoroughly** | 1 | 1 | - | 147.21 | - | 7,077 | - | 0.000265 | 🔵 low — common in general English | — |
| 7434 | **improper** | 1 | 1 | - | 147.21 | - | 7,078 | - | 0.000264 | 🔵 low — common in general English | — |
| 7435 | **landed** | 1 | 1 | - | 147.21 | - | 7,079 | - | 0.000264 | 🔵 low — common in general English | — |
| 7436 | **dormant** | 1 | 1 | - | 147.21 | - | 7,080 | - | 0.000264 | 🔵 low — common in general English | — |
| 7437 | **cooling** | 1 | 1 | - | 147.21 | - | 7,081 | - | 0.000264 | 🔵 low — common in general English | — |
| 7438 | **conform** | 1 | 1 | - | 147.21 | - | 7,082 | - | 0.000264 | 🔵 low — common in general English | — |
| 7439 | **complaining** | 1 | 1 | - | 147.21 | - | 7,083 | - | 0.000264 | 🔵 low — common in general English | — |
| 7440 | **enquiry** | 1 | 1 | - | 147.21 | - | 7,084 | - | 0.000264 | 🔵 low — common in general English | — |
| 7441 | **fetch** | 1 | 1 | - | 147.21 | - | 7,085 | - | 0.000264 | 🔵 low — common in general English | — |
| 7442 | **sail** | 1 | 1 | - | 147.21 | - | 7,086 | - | 0.000264 | 🔵 low — common in general English | — |
| 7443 | **caterpillar** | 1 | 1 | - | 147.21 | - | 7,087 | - | 0.000264 | 🔵 low — common in general English | — |
| 7444 | **occurrence** | 1 | 1 | - | 147.21 | - | 7,088 | - | 0.000264 | 🔵 low — common in general English | — |
| 7445 | **urgently** | 1 | 1 | - | 147.21 | - | 7,089 | - | 0.000264 | 🔵 low — common in general English | — |
| 7446 | **lean** | 1 | 1 | - | 147.21 | - | 7,090 | - | 0.000264 | 🔵 low — common in general English | — |
| 7447 | **brass** | 1 | 1 | - | 147.21 | - | 7,091 | - | 0.000264 | 🔵 low — common in general English | — |
| 7448 | **alternatively** | 1 | 1 | - | 147.21 | - | 7,092 | - | 0.000264 | 🔵 low — common in general English | — |
| 7449 | **absorbing** | 1 | 1 | - | 147.21 | - | 7,093 | - | 0.000264 | 🔵 low — common in general English | — |
| 7450 | **conversation** | 1 | 1 | - | 147.21 | - | 7,094 | - | 0.000264 | 🔵 low — common in general English | — |
| 7451 | **debated** | 1 | 1 | - | 147.21 | - | 7,095 | - | 0.000264 | 🔵 low — common in general English | — |
| 7452 | **vague** | 1 | 1 | - | 144.54 | - | 7,096 | - | 0.000264 | 🔵 low — common in general English | — |
| 7453 | **slipping** | 1 | 1 | - | 144.54 | - | 7,097 | - | 0.000264 | 🔵 low — common in general English | — |
| 7454 | **collectively** | 1 | 1 | - | 144.54 | - | 7,098 | - | 0.000264 | 🔵 low — common in general English | — |
| 7455 | **unwelcome** | 1 | 1 | - | 144.54 | - | 7,099 | - | 0.000264 | 🔵 low — common in general English | — |
| 7456 | **depression** | 1 | 1 | - | 144.54 | - | 7,100 | - | 0.000264 | 🔵 low — common in general English | — |
| 7457 | **liquor** | 1 | 1 | - | 144.54 | - | 7,101 | - | 0.000264 | 🔵 low — common in general English | — |
| 7458 | **counterpart** | 1 | 1 | - | 144.54 | - | 7,102 | - | 0.000264 | 🔵 low — common in general English | — |
| 7459 | **restriction** | 1 | 1 | - | 144.54 | - | 7,103 | - | 0.000264 | 🔵 low — common in general English | — |
| 7460 | **gravity** | 1 | 1 | - | 144.54 | - | 7,104 | - | 0.000264 | 🔵 low — common in general English | — |
| 7461 | **heaviest** | 1 | 1 | - | 144.54 | - | 7,105 | - | 0.000264 | 🔵 low — common in general English | — |
| 7462 | **outweighed** | 1 | 1 | - | 144.54 | - | 7,106 | - | 0.000264 | 🔵 low — common in general English | — |
| 7463 | **bleak** | 1 | 1 | - | 144.54 | - | 7,107 | - | 0.000264 | 🔵 low — common in general English | — |
| 7464 | **invisible** | 1 | 1 | - | 144.54 | - | 7,108 | - | 0.000264 | 🔵 low — common in general English | — |
| 7465 | **adopting** | 1 | 1 | - | 144.54 | - | 7,109 | - | 0.000264 | 🔵 low — common in general English | — |
| 7466 | **draining** | 1 | 1 | - | 144.54 | - | 7,110 | - | 0.000264 | 🔵 low — common in general English | — |
| 7467 | **negatively** | 1 | 1 | - | 144.54 | - | 7,111 | - | 0.000264 | 🔵 low — common in general English | — |
| 7468 | **upheld** | 1 | 1 | - | 144.54 | - | 7,112 | - | 0.000264 | 🔵 low — common in general English | — |
| 7469 | **lightning** | 1 | 1 | - | 144.54 | - | 7,113 | - | 0.000264 | 🔵 low — common in general English | — |
| 7470 | **penalty** | 1 | 1 | - | 144.54 | - | 7,114 | - | 0.000264 | 🔵 low — common in general English | — |
| 7471 | **wing** | 1 | 1 | - | 144.54 | - | 7,115 | - | 0.000264 | 🔵 low — common in general English | — |
| 7472 | **mixture** | 1 | 1 | - | 144.54 | - | 7,116 | - | 0.000264 | 🔵 low — common in general English | — |
| 7473 | **diminished** | 1 | 1 | - | 144.54 | - | 7,117 | - | 0.000264 | 🔵 low — common in general English | — |
| 7474 | **lent** | 1 | 1 | - | 144.54 | - | 7,118 | - | 0.000264 | 🔵 low — common in general English | — |
| 7475 | **spinning** | 1 | 1 | - | 144.54 | - | 7,119 | - | 0.000264 | 🔵 low — common in general English | — |
| 7476 | **transporting** | 1 | 1 | - | 144.54 | - | 7,120 | - | 0.000264 | 🔵 low — common in general English | — |
| 7477 | **rot** | 1 | 1 | - | 144.54 | - | 7,121 | - | 0.000264 | 🔵 low — common in general English | — |
| 7478 | **dram** | 1 | 1 | - | 144.54 | - | 7,122 | - | 0.000264 | 🔵 low — common in general English | — |
| 7479 | **occupied** | 1 | 1 | - | 144.54 | - | 7,123 | - | 0.000264 | 🔵 low — common in general English | — |
| 7480 | **admit** | 1 | 1 | - | 144.54 | - | 7,124 | - | 0.000264 | 🔵 low — common in general English | — |
| 7481 | **goldsmith** | 1 | 1 | - | 144.54 | - | 7,125 | - | 0.000264 | 🔵 low — common in general English | — |
| 7482 | **umbrella** | 1 | 1 | - | 144.54 | - | 7,126 | - | 0.000264 | 🔵 low — common in general English | — |
| 7483 | **tube** | 1 | 1 | - | 144.54 | - | 7,127 | - | 0.000264 | 🔵 low — common in general English | — |
| 7484 | **intangible** | 1 | 1 | - | 144.54 | - | 7,128 | - | 0.000264 | 🔵 low — common in general English | — |
| 7485 | **sunshine** | 1 | 1 | - | 144.54 | - | 7,129 | - | 0.000263 | 🔵 low — common in general English | — |
| 7486 | **north-west** | 1 | 1 | - | 144.54 | - | 7,130 | - | 0.000263 | 🔵 low — common in general English | — |
| 7487 | **ensuring** | 1 | 1 | - | 144.54 | - | 7,131 | - | 0.000263 | 🔵 low — common in general English | — |
| 7488 | **rod** | 1 | 1 | - | 144.54 | - | 7,132 | - | 0.000263 | 🔵 low — common in general English | — |
| 7489 | **chicken** | 1 | 1 | - | 144.54 | - | 7,133 | - | 0.000263 | 🔵 low — common in general English | — |
| 7490 | **unaffected** | 1 | 1 | - | 144.54 | - | 7,134 | - | 0.000263 | 🔵 low — common in general English | — |
| 7491 | **differ** | 1 | 1 | - | 144.54 | - | 7,135 | - | 0.000263 | 🔵 low — common in general English | — |
| 7492 | **duration** | 1 | 1 | - | 144.54 | - | 7,136 | - | 0.000263 | 🔵 low — common in general English | — |
| 7493 | **abu** | 1 | 1 | - | 144.54 | - | 7,137 | - | 0.000263 | 🔵 low — common in general English | — |
| 7494 | **increased** | 1 | 2 | - | 143.79 | - | 7,138 | - | 0.000263 | 🔵 low — common in general English | — |
| 7495 | **domestic** | 1 | 2 | - | 143.42 | - | 7,139 | - | 0.000263 | 🔵 low — common in general English | — |
| 7496 | **sounded** | 1 | 1 | - | 142.22 | - | 7,140 | - | 0.000263 | 🔵 low — common in general English | — |
| 7497 | **enthusiasm** | 1 | 1 | - | 142.22 | - | 7,141 | - | 0.000263 | 🔵 low — common in general English | — |
| 7498 | **reputation** | 1 | 1 | - | 142.22 | - | 7,142 | - | 0.000263 | 🔵 low — common in general English | — |
| 7499 | **demonstrate** | 1 | 1 | - | 142.22 | - | 7,143 | - | 0.000263 | 🔵 low — common in general English | — |
| 7500 | **reliable** | 1 | 1 | - | 142.22 | - | 7,144 | - | 0.000263 | 🔵 low — common in general English | — |
| 7501 | **pack** | 1 | 1 | - | 142.22 | - | 7,145 | - | 0.000263 | 🔵 low — common in general English | — |
| 7502 | **stuck** | 1 | 1 | - | 142.22 | - | 7,146 | - | 0.000263 | 🔵 low — common in general English | — |
| 7503 | **fate** | 1 | 1 | - | 142.22 | - | 7,147 | - | 0.000263 | 🔵 low — common in general English | — |
| 7504 | **endanger** | 1 | 1 | - | 142.22 | - | 7,148 | - | 0.000263 | 🔵 low — common in general English | — |
| 7505 | **diversion** | 1 | 1 | - | 142.22 | - | 7,149 | - | 0.000263 | 🔵 low — common in general English | — |
| 7506 | **pleas** | 1 | 1 | - | 142.22 | - | 7,150 | - | 0.000263 | 🔵 low — common in general English | — |
| 7507 | **softer** | 1 | 1 | - | 142.22 | - | 7,151 | - | 0.000263 | 🔵 low — common in general English | — |
| 7508 | **concentrating** | 1 | 1 | - | 142.22 | - | 7,152 | - | 0.000263 | 🔵 low — common in general English | — |
| 7509 | **shifted** | 1 | 1 | - | 142.22 | - | 7,153 | - | 0.000263 | 🔵 low — common in general English | — |
| 7510 | **hazardous** | 1 | 1 | - | 142.22 | - | 7,154 | - | 0.000263 | 🔵 low — common in general English | — |
| 7511 | **label** | 1 | 1 | - | 142.22 | - | 7,155 | - | 0.000263 | 🔵 low — common in general English | — |
| 7512 | **interference** | 1 | 1 | - | 142.22 | - | 7,156 | - | 0.000263 | 🔵 low — common in general English | — |
| 7513 | **directive** | 1 | 1 | - | 142.22 | - | 7,157 | - | 0.000263 | 🔵 low — common in general English | — |
| 7514 | **distributing** | 1 | 1 | - | 142.22 | - | 7,158 | - | 0.000263 | 🔵 low — common in general English | — |
| 7515 | **grip** | 1 | 1 | - | 142.22 | - | 7,159 | - | 0.000263 | 🔵 low — common in general English | — |
| 7516 | **mercury** | 1 | 1 | - | 142.22 | - | 7,160 | - | 0.000263 | 🔵 low — common in general English | — |
| 7517 | **readily** | 1 | 1 | - | 142.22 | - | 7,162 | - | 0.000263 | 🔵 low — common in general English | — |
| 7518 | **lessening** | 1 | 1 | - | 142.22 | - | 7,163 | - | 0.000263 | 🔵 low — common in general English | — |
| 7519 | **desired** | 1 | 1 | - | 142.22 | - | 7,164 | - | 0.000263 | 🔵 low — common in general English | — |
| 7520 | **necessity** | 1 | 1 | - | 142.22 | - | 7,165 | - | 0.000263 | 🔵 low — common in general English | — |
| 7521 | **impatience** | 1 | 1 | - | 142.22 | - | 7,166 | - | 0.000263 | 🔵 low — common in general English | — |
| 7522 | **intelligent** | 1 | 1 | - | 142.22 | - | 7,167 | - | 0.000263 | 🔵 low — common in general English | — |
| 7523 | **pronounced** | 1 | 1 | - | 142.22 | - | 7,168 | - | 0.000263 | 🔵 low — common in general English | — |
| 7524 | **deter** | 1 | 1 | - | 142.22 | - | 7,169 | - | 0.000263 | 🔵 low — common in general English | — |
| 7525 | **agriculture** | 1 | 2 | - | 141.61 | - | 7,170 | - | 0.000263 | 🔵 low — common in general English | — |
| 7526 | **player** | 1 | 1 | - | 140.18 | - | 7,171 | - | 0.000263 | 🔵 low — common in general English | — |
| 7527 | **relaxation** | 1 | 1 | - | 140.18 | - | 7,172 | - | 0.000263 | 🔵 low — common in general English | — |
| 7528 | **dominate** | 1 | 1 | - | 140.18 | - | 7,173 | - | 0.000263 | 🔵 low — common in general English | — |
| 7529 | **proof** | 1 | 1 | - | 140.18 | - | 7,174 | - | 0.000263 | 🔵 low — common in general English | — |
| 7530 | **matching** | 1 | 1 | - | 140.18 | - | 7,175 | - | 0.000263 | 🔵 low — common in general English | — |
| 7531 | **unexpectedly** | 1 | 1 | - | 140.18 | - | 7,176 | - | 0.000263 | 🔵 low — common in general English | — |
| 7532 | **revived** | 1 | 1 | - | 140.18 | - | 7,177 | - | 0.000263 | 🔵 low — common in general English | — |
| 7533 | **supplementary** | 1 | 1 | - | 140.18 | - | 7,178 | - | 0.000263 | 🔵 low — common in general English | — |
| 7534 | **ridiculous** | 1 | 1 | - | 140.18 | - | 7,179 | - | 0.000263 | 🔵 low — common in general English | — |
| 7535 | **steer** | 1 | 1 | - | 140.18 | - | 7,180 | - | 0.000263 | 🔵 low — common in general English | — |
| 7536 | **chart** | 1 | 1 | - | 140.18 | - | 7,181 | - | 0.000262 | 🔵 low — common in general English | — |
| 7537 | **familiar** | 1 | 1 | - | 140.18 | - | 7,182 | - | 0.000262 | 🔵 low — common in general English | — |
| 7538 | **rigid** | 1 | 1 | - | 140.18 | - | 7,183 | - | 0.000262 | 🔵 low — common in general English | — |
| 7539 | **desperate** | 1 | 1 | - | 140.18 | - | 7,184 | - | 0.000262 | 🔵 low — common in general English | — |
| 7540 | **page** | 1 | 1 | - | 140.18 | - | 7,185 | - | 0.000262 | 🔵 low — common in general English | — |
| 7541 | **dealt** | 1 | 1 | - | 140.18 | - | 7,186 | - | 0.000262 | 🔵 low — common in general English | — |
| 7542 | **attacking** | 1 | 1 | - | 140.18 | - | 7,187 | - | 0.000262 | 🔵 low — common in general English | — |
| 7543 | **clouded** | 1 | 1 | - | 140.18 | - | 7,188 | - | 0.000262 | 🔵 low — common in general English | — |
| 7544 | **hitting** | 1 | 1 | - | 140.18 | - | 7,189 | - | 0.000262 | 🔵 low — common in general English | — |
| 7545 | **wiped** | 1 | 1 | - | 140.18 | - | 7,190 | - | 0.000262 | 🔵 low — common in general English | — |
| 7546 | **inclined** | 1 | 1 | - | 140.18 | - | 7,191 | - | 0.000262 | 🔵 low — common in general English | — |
| 7547 | **leaf** | 1 | 1 | - | 140.18 | - | 7,192 | - | 0.000262 | 🔵 low — common in general English | — |
| 7548 | **grossly** | 1 | 1 | - | 140.18 | - | 7,194 | - | 0.000262 | 🔵 low — common in general English | — |
| 7549 | **spurred** | 1 | 1 | - | 140.18 | - | 7,195 | - | 0.000262 | 🔵 low — common in general English | — |
| 7550 | **clarify** | 1 | 1 | - | 140.18 | - | 7,196 | - | 0.000262 | 🔵 low — common in general English | — |
| 7551 | **intellectual** | 1 | 1 | - | 140.18 | - | 7,197 | - | 0.000262 | 🔵 low — common in general English | — |
| 7552 | **indebted** | 1 | 1 | - | 140.18 | - | 7,198 | - | 0.000262 | 🔵 low — common in general English | — |
| 7553 | **borrowed** | 1 | 1 | - | 140.18 | - | 7,199 | - | 0.000262 | 🔵 low — common in general English | — |
| 7554 | **lacked** | 1 | 1 | - | 140.18 | - | 7,200 | - | 0.000262 | 🔵 low — common in general English | — |
| 7555 | **stretching** | 1 | 1 | - | 140.18 | - | 7,201 | - | 0.000262 | 🔵 low — common in general English | — |
| 7556 | **funeral** | 1 | 1 | - | 140.18 | - | 7,202 | - | 0.000262 | 🔵 low — common in general English | — |
| 7557 | **solved** | 1 | 1 | - | 140.18 | - | 7,203 | - | 0.000262 | 🔵 low — common in general English | — |
| 7558 | **mutually** | 1 | 1 | - | 138.36 | - | 7,204 | - | 0.000262 | 🔵 low — common in general English | — |
| 7559 | **anchor** | 1 | 1 | - | 138.36 | - | 7,205 | - | 0.000262 | 🔵 low — common in general English | — |
| 7560 | **collective** | 1 | 1 | - | 138.36 | - | 7,206 | - | 0.000262 | 🔵 low — common in general English | — |
| 7561 | **shed** | 1 | 1 | - | 138.36 | - | 7,207 | - | 0.000262 | 🔵 low — common in general English | — |
| 7562 | **withdrawing** | 1 | 1 | - | 138.36 | - | 7,208 | - | 0.000262 | 🔵 low — common in general English | — |
| 7563 | **multiple** | 1 | 1 | - | 138.36 | - | 7,209 | - | 0.000262 | 🔵 low — common in general English | — |
| 7564 | **pan** | 1 | 1 | - | 138.36 | - | 7,210 | - | 0.000262 | 🔵 low — common in general English | — |
| 7565 | **varying** | 1 | 1 | - | 138.36 | - | 7,211 | - | 0.000262 | 🔵 low — common in general English | — |
| 7566 | **prominent** | 1 | 1 | - | 138.36 | - | 7,212 | - | 0.000262 | 🔵 low — common in general English | — |
| 7567 | **prop** | 1 | 1 | - | 138.36 | - | 7,213 | - | 0.000262 | 🔵 low — common in general English | — |
| 7568 | **pointing** | 1 | 1 | - | 138.36 | - | 7,214 | - | 0.000262 | 🔵 low — common in general English | — |
| 7569 | **thwart** | 1 | 1 | - | 138.36 | - | 7,215 | - | 0.000262 | 🔵 low — common in general English | — |
| 7570 | **evident** | 1 | 1 | - | 138.36 | - | 7,216 | - | 0.000262 | 🔵 low — common in general English | — |
| 7571 | **examined** | 1 | 1 | - | 138.36 | - | 7,217 | - | 0.000262 | 🔵 low — common in general English | — |
| 7572 | **nearing** | 1 | 1 | - | 138.36 | - | 7,218 | - | 0.000262 | 🔵 low — common in general English | — |
| 7573 | **obliged** | 1 | 1 | - | 138.36 | - | 7,219 | - | 0.000262 | 🔵 low — common in general English | — |
| 7574 | **extract** | 1 | 1 | - | 138.36 | - | 7,220 | - | 0.000262 | 🔵 low — common in general English | — |
| 7575 | **plate** | 1 | 1 | - | 138.36 | - | 7,221 | - | 0.000262 | 🔵 low — common in general English | — |
| 7576 | **persist** | 1 | 1 | - | 138.36 | - | 7,222 | - | 0.000262 | 🔵 low — common in general English | — |
| 7577 | **subscribe** | 1 | 1 | - | 138.36 | - | 7,223 | - | 0.000262 | 🔵 low — common in general English | — |
| 7578 | **unwanted** | 1 | 1 | - | 138.36 | - | 7,224 | - | 0.000262 | 🔵 low — common in general English | — |
| 7579 | **incorrect** | 1 | 1 | - | 138.36 | - | 7,225 | - | 0.000262 | 🔵 low — common in general English | — |
| 7580 | **turmoil** | 1 | 1 | - | 136.70 | - | 7,226 | - | 0.000262 | 🔵 low — common in general English | — |
| 7581 | **dominated** | 1 | 1 | - | 136.70 | - | 7,227 | - | 0.000262 | 🔵 low — common in general English | — |
| 7582 | **creek** | 1 | 1 | - | 136.70 | - | 7,228 | - | 0.000262 | 🔵 low — common in general English | — |
| 7583 | **fought** | 1 | 1 | - | 136.70 | - | 7,229 | - | 0.000262 | 🔵 low — common in general English | — |
| 7584 | **removing** | 1 | 1 | - | 136.70 | - | 7,230 | - | 0.000262 | 🔵 low — common in general English | — |
| 7585 | **preceding** | 1 | 1 | - | 136.70 | - | 7,231 | - | 0.000262 | 🔵 low — common in general English | — |
| 7586 | **calculation** | 1 | 1 | - | 136.70 | - | 7,232 | - | 0.000262 | 🔵 low — common in general English | — |
| 7587 | **disastrous** | 1 | 1 | - | 136.70 | - | 7,233 | - | 0.000262 | 🔵 low — common in general English | — |
| 7588 | **warranted** | 1 | 1 | - | 136.70 | - | 7,234 | - | 0.000261 | 🔵 low — common in general English | — |
| 7589 | **warn** | 1 | 1 | - | 136.70 | - | 7,235 | - | 0.000261 | 🔵 low — common in general English | — |
| 7590 | **austerity** | 1 | 1 | - | 136.70 | - | 7,236 | - | 0.000261 | 🔵 low — common in general English | — |
| 7591 | **modestly** | 1 | 1 | - | 136.70 | - | 7,237 | - | 0.000261 | 🔵 low — common in general English | — |
| 7592 | **limitation** | 1 | 1 | - | 136.70 | - | 7,238 | - | 0.000261 | 🔵 low — common in general English | — |
| 7593 | **worthwhile** | 1 | 1 | - | 136.70 | - | 7,239 | - | 0.000261 | 🔵 low — common in general English | — |
| 7594 | **halting** | 1 | 1 | - | 136.70 | - | 7,240 | - | 0.000261 | 🔵 low — common in general English | — |
| 7595 | **departure** | 1 | 1 | - | 136.70 | - | 7,241 | - | 0.000261 | 🔵 low — common in general English | — |
| 7596 | **persistent** | 1 | 1 | - | 136.70 | - | 7,242 | - | 0.000261 | 🔵 low — common in general English | — |
| 7597 | **revealed** | 1 | 1 | - | 135.20 | - | 7,243 | - | 0.000261 | 🔵 low — common in general English | — |
| 7598 | **topic** | 1 | 1 | - | 135.20 | - | 7,244 | - | 0.000261 | 🔵 low — common in general English | — |
| 7599 | **dictate** | 1 | 1 | - | 135.20 | - | 7,246 | - | 0.000261 | 🔵 low — common in general English | — |
| 7600 | **prohibited** | 1 | 1 | - | 135.20 | - | 7,247 | - | 0.000261 | 🔵 low — common in general English | — |
| 7601 | **misleading** | 1 | 1 | - | 135.20 | - | 7,248 | - | 0.000261 | 🔵 low — common in general English | — |
| 7602 | **mood** | 1 | 1 | - | 135.20 | - | 7,249 | - | 0.000261 | 🔵 low — common in general English | — |
| 7603 | **purely** | 1 | 1 | - | 135.20 | - | 7,250 | - | 0.000261 | 🔵 low — common in general English | — |
| 7604 | **essentially** | 1 | 1 | - | 135.20 | - | 7,251 | - | 0.000261 | 🔵 low — common in general English | — |
| 7605 | **restrain** | 1 | 1 | - | 135.20 | - | 7,252 | - | 0.000261 | 🔵 low — common in general English | — |
| 7606 | **stemming** | 1 | 1 | - | 135.20 | - | 7,253 | - | 0.000261 | 🔵 low — common in general English | — |
| 7607 | **hall** | 1 | 1 | - | 135.20 | - | 7,254 | - | 0.000261 | 🔵 low — common in general English | — |
| 7608 | **tended** | 1 | 1 | - | 135.20 | - | 7,255 | - | 0.000261 | 🔵 low — common in general English | — |
| 7609 | **adapt** | 1 | 1 | - | 135.20 | - | 7,256 | - | 0.000261 | 🔵 low — common in general English | — |
| 7610 | **rolling** | 1 | 1 | - | 135.20 | - | 7,257 | - | 0.000261 | 🔵 low — common in general English | — |
| 7611 | **claiming** | 1 | 1 | - | 135.20 | - | 7,258 | - | 0.000261 | 🔵 low — common in general English | — |
| 7612 | **consequently** | 1 | 1 | - | 135.20 | - | 7,259 | - | 0.000261 | 🔵 low — common in general English | — |
| 7613 | **crew** | 1 | 1 | - | 135.20 | - | 7,260 | - | 0.000261 | 🔵 low — common in general English | — |
| 7614 | **soaring** | 1 | 1 | - | 135.20 | - | 7,261 | - | 0.000261 | 🔵 low — common in general English | — |
| 7615 | **classified** | 1 | 1 | - | 135.20 | - | 7,262 | - | 0.000261 | 🔵 low — common in general English | — |
| 7616 | **describing** | 1 | 1 | - | 135.20 | - | 7,263 | - | 0.000261 | 🔵 low — common in general English | — |
| 7617 | **unstable** | 1 | 1 | - | 135.20 | - | 7,265 | - | 0.000261 | 🔵 low — common in general English | — |
| 7618 | **recording** | 1 | 1 | - | 135.20 | - | 7,266 | - | 0.000261 | 🔵 low — common in general English | — |
| 7619 | **forming** | 1 | 1 | - | 133.81 | - | 7,267 | - | 0.000261 | 🔵 low — common in general English | — |
| 7620 | **revive** | 1 | 1 | - | 133.81 | - | 7,268 | - | 0.000261 | 🔵 low — common in general English | — |
| 7621 | **location** | 1 | 1 | - | 133.81 | - | 7,269 | - | 0.000261 | 🔵 low — common in general English | — |
| 7622 | **sceptical** | 1 | 1 | - | 133.81 | - | 7,270 | - | 0.000261 | 🔵 low — common in general English | — |
| 7623 | **opposing** | 1 | 1 | - | 133.81 | - | 7,271 | - | 0.000261 | 🔵 low — common in general English | — |
| 7624 | **combining** | 1 | 1 | - | 133.81 | - | 7,272 | - | 0.000261 | 🔵 low — common in general English | — |
| 7625 | **composite** | 1 | 1 | - | 133.81 | - | 7,273 | - | 0.000261 | 🔵 low — common in general English | — |
| 7626 | **ideal** | 1 | 1 | - | 133.81 | - | 7,274 | - | 0.000261 | 🔵 low — common in general English | — |
| 7627 | **modify** | 1 | 1 | - | 133.81 | - | 7,275 | - | 0.000261 | 🔵 low — common in general English | — |
| 7628 | **repaying** | 1 | 1 | - | 133.81 | - | 7,276 | - | 0.000261 | 🔵 low — common in general English | — |
| 7629 | **cake** | 1 | 1 | - | 133.81 | - | 7,277 | - | 0.000261 | 🔵 low — common in general English | — |
| 7630 | **appreciate** | 1 | 1 | - | 133.81 | - | 7,278 | - | 0.000261 | 🔵 low — common in general English | — |
| 7631 | **goodwill** | 1 | 1 | - | 133.81 | - | 7,279 | - | 0.000261 | 🔵 low — common in general English | — |
| 7632 | **substitute** | 1 | 1 | - | 133.81 | - | 7,280 | - | 0.000261 | 🔵 low — common in general English | — |
| 7633 | **interesting** | 1 | 1 | - | 133.81 | - | 7,281 | - | 0.000261 | 🔵 low — common in general English | — |
| 7634 | **mission** | 1 | 1 | - | 133.81 | - | 7,282 | - | 0.000261 | 🔵 low — common in general English | — |
| 7635 | **thin** | 1 | 1 | - | 133.81 | - | 7,283 | - | 0.000261 | 🔵 low — common in general English | — |
| 7636 | **tangible** | 1 | 1 | - | 133.81 | - | 7,284 | - | 0.000261 | 🔵 low — common in general English | — |
| 7637 | **feature** | 1 | 1 | - | 133.81 | - | 7,285 | - | 0.000261 | 🔵 low — common in general English | — |
| 7638 | **destination** | 1 | 1 | - | 133.81 | - | 7,286 | - | 0.000261 | 🔵 low — common in general English | — |
| 7639 | **dot** | 1 | 1 | - | 133.81 | - | 7,287 | - | 0.000261 | 🔵 low — common in general English | — |
| 7640 | **played** | 1 | 1 | - | 132.53 | - | 7,288 | - | 0.000260 | 🔵 low — common in general English | — |
| 7641 | **thereby** | 1 | 1 | - | 132.53 | - | 7,289 | - | 0.000260 | 🔵 low — common in general English | — |
| 7642 | **weaken** | 1 | 1 | - | 132.53 | - | 7,290 | - | 0.000260 | 🔵 low — common in general English | — |
| 7643 | **remark** | 1 | 1 | - | 132.53 | - | 7,291 | - | 0.000260 | 🔵 low — common in general English | — |
| 7644 | **blame** | 1 | 1 | - | 132.53 | - | 7,292 | - | 0.000260 | 🔵 low — common in general English | — |
| 7645 | **accompanying** | 1 | 1 | - | 132.53 | - | 7,293 | - | 0.000260 | 🔵 low — common in general English | — |
| 7646 | **asa** | 1 | 1 | - | 132.53 | - | 7,294 | - | 0.000260 | 🔵 low — common in general English | — |
| 7647 | **dipped** | 1 | 1 | - | 132.53 | - | 7,295 | - | 0.000260 | 🔵 low — common in general English | — |
| 7648 | **professor** | 1 | 1 | - | 132.53 | - | 7,296 | - | 0.000260 | 🔵 low — common in general English | — |
| 7649 | **reacted** | 1 | 1 | - | 132.53 | - | 7,297 | - | 0.000260 | 🔵 low — common in general English | — |
| 7650 | **thereafter** | 1 | 1 | - | 132.53 | - | 7,298 | - | 0.000260 | 🔵 low — common in general English | — |
| 7651 | **game** | 1 | 1 | - | 132.53 | - | 7,299 | - | 0.000260 | 🔵 low — common in general English | — |
| 7652 | **exclusively** | 1 | 1 | - | 132.53 | - | 7,300 | - | 0.000260 | 🔵 low — common in general English | — |
| 7653 | **chosen** | 1 | 1 | - | 132.53 | - | 7,301 | - | 0.000260 | 🔵 low — common in general English | — |
| 7654 | **motion** | 1 | 1 | - | 132.53 | - | 7,302 | - | 0.000260 | 🔵 low — common in general English | — |
| 7655 | **testing** | 1 | 1 | - | 131.33 | - | 7,303 | - | 0.000260 | 🔵 low — common in general English | — |
| 7656 | **stored** | 1 | 1 | - | 131.33 | - | 7,304 | - | 0.000260 | 🔵 low — common in general English | — |
| 7657 | **mer** | 1 | 1 | - | 131.33 | - | 7,305 | - | 0.000260 | 🔵 low — common in general English | — |
| 7658 | **justified** | 1 | 1 | - | 131.33 | - | 7,306 | - | 0.000260 | 🔵 low — common in general English | — |
| 7659 | **rated** | 1 | 1 | - | 131.33 | - | 7,307 | - | 0.000260 | 🔵 low — common in general English | — |
| 7660 | **candidate** | 1 | 1 | - | 131.33 | - | 7,308 | - | 0.000260 | 🔵 low — common in general English | — |
| 7661 | **challenged** | 1 | 1 | - | 131.33 | - | 7,309 | - | 0.000260 | 🔵 low — common in general English | — |
| 7662 | **seller** | 1 | 1 | - | 131.33 | - | 7,310 | - | 0.000260 | 🔵 low — common in general English | — |
| 7663 | **revolving** | 1 | 1 | - | 131.33 | - | 7,311 | - | 0.000260 | 🔵 low — common in general English | — |
| 7664 | **interpreted** | 1 | 1 | - | 131.33 | - | 7,312 | - | 0.000260 | 🔵 low — common in general English | — |
| 7665 | **sending** | 1 | 1 | - | 131.33 | - | 7,313 | - | 0.000260 | 🔵 low — common in general English | — |
| 7666 | **driving** | 1 | 1 | - | 130.21 | - | 7,315 | - | 0.000260 | 🔵 low — common in general English | — |
| 7667 | **comprise** | 1 | 1 | - | 130.21 | - | 7,316 | - | 0.000260 | 🔵 low — common in general English | — |
| 7668 | **inevitable** | 1 | 1 | - | 130.21 | - | 7,317 | - | 0.000260 | 🔵 low — common in general English | — |
| 7669 | **ferry** | 1 | 1 | - | 130.21 | - | 7,318 | - | 0.000260 | 🔵 low — common in general English | — |
| 7670 | **undertaken** | 1 | 1 | - | 130.21 | - | 7,319 | - | 0.000260 | 🔵 low — common in general English | — |
| 7671 | **coin** | 1 | 1 | - | 130.21 | - | 7,320 | - | 0.000260 | 🔵 low — common in general English | — |
| 7672 | **mild** | 1 | 1 | - | 130.21 | - | 7,321 | - | 0.000260 | 🔵 low — common in general English | — |
| 7673 | **wary** | 1 | 1 | - | 130.21 | - | 7,322 | - | 0.000260 | 🔵 low — common in general English | — |
| 7674 | **emerging** | 1 | 1 | - | 130.21 | - | 7,323 | - | 0.000260 | 🔵 low — common in general English | — |
| 7675 | **obligation** | 1 | 1 | - | 130.21 | - | 7,324 | - | 0.000260 | 🔵 low — common in general English | — |
| 7676 | **worry** | 1 | 1 | - | 130.21 | - | 7,325 | - | 0.000260 | 🔵 low — common in general English | — |
| 7677 | **unlike** | 1 | 1 | - | 130.21 | - | 7,326 | - | 0.000260 | 🔵 low — common in general English | — |
| 7678 | **soil** | 1 | 1 | - | 130.21 | - | 7,327 | - | 0.000260 | 🔵 low — common in general English | — |
| 7679 | **sale** | 1 | 2 | - | 129.81 | - | 7,328 | - | 0.000260 | 🔵 low — common in general English | — |
| 7680 | **decree** | 1 | 1 | - | 129.16 | - | 7,329 | - | 0.000260 | 🔵 low — common in general English | — |
| 7681 | **historical** | 1 | 1 | - | 129.16 | - | 7,330 | - | 0.000260 | 🔵 low — common in general English | — |
| 7682 | **calculating** | 1 | 1 | - | 129.16 | - | 7,331 | - | 0.000260 | 🔵 low — common in general English | — |
| 7683 | **sharing** | 1 | 1 | - | 129.16 | - | 7,332 | - | 0.000260 | 🔵 low — common in general English | — |
| 7684 | **assessment** | 1 | 1 | - | 129.16 | - | 7,333 | - | 0.000260 | 🔵 low — common in general English | — |
| 7685 | **regularly** | 1 | 1 | - | 129.16 | - | 7,334 | - | 0.000260 | 🔵 low — common in general English | — |
| 7686 | **reacting** | 1 | 1 | - | 129.16 | - | 7,335 | - | 0.000260 | 🔵 low — common in general English | — |
| 7687 | **farming** | 1 | 1 | - | 129.16 | - | 7,336 | - | 0.000260 | 🔵 low — common in general English | — |
| 7688 | **rejection** | 1 | 1 | - | 129.16 | - | 7,337 | - | 0.000260 | 🔵 low — common in general English | — |
| 7689 | **imposing** | 1 | 1 | - | 128.17 | - | 7,338 | - | 0.000260 | 🔵 low — common in general English | — |
| 7690 | **obvious** | 1 | 1 | - | 128.17 | - | 7,339 | - | 0.000260 | 🔵 low — common in general English | — |
| 7691 | **permission** | 1 | 1 | - | 128.17 | - | 7,340 | - | 0.000260 | 🔵 low — common in general English | — |
| 7692 | **fix** | 1 | 1 | - | 128.17 | - | 7,341 | - | 0.000260 | 🔵 low — common in general English | — |
| 7693 | **procedure** | 1 | 1 | - | 128.17 | - | 7,342 | - | 0.000259 | 🔵 low — common in general English | — |
| 7694 | **demanded** | 1 | 1 | - | 128.17 | - | 7,343 | - | 0.000259 | 🔵 low — common in general English | — |
| 7695 | **secondary** | 1 | 1 | - | 128.17 | - | 7,345 | - | 0.000259 | 🔵 low — common in general English | — |
| 7696 | **apparel** | 1 | 1 | - | 128.17 | - | 7,346 | - | 0.000259 | 🔵 low — common in general English | — |
| 7697 | **society** | 1 | 1 | - | 128.17 | - | 7,347 | - | 0.000259 | 🔵 low — common in general English | — |
| 7698 | **lesser** | 1 | 1 | - | 128.17 | - | 7,348 | - | 0.000259 | 🔵 low — common in general English | — |
| 7699 | **ali** | 1 | 1 | - | 127.23 | - | 7,349 | - | 0.000259 | 🔵 low — common in general English | — |
| 7700 | **bob** | 1 | 1 | - | 127.23 | - | 7,350 | - | 0.000259 | 🔵 low — common in general English | — |
| 7701 | **milling** | 1 | 1 | - | 127.23 | - | 7,351 | - | 0.000259 | 🔵 low — common in general English | — |
| 7702 | **returning** | 1 | 1 | - | 127.23 | - | 7,352 | - | 0.000259 | 🔵 low — common in general English | — |
| 7703 | **handle** | 1 | 1 | - | 127.23 | - | 7,353 | - | 0.000259 | 🔵 low — common in general English | — |
| 7704 | **consent** | 1 | 1 | - | 127.23 | - | 7,354 | - | 0.000259 | 🔵 low — common in general English | — |
| 7705 | **evaluating** | 1 | 1 | - | 127.23 | - | 7,355 | - | 0.000259 | 🔵 low — common in general English | — |
| 7706 | **hurting** | 1 | 1 | - | 127.23 | - | 7,356 | - | 0.000259 | 🔵 low — common in general English | — |
| 7707 | **sensitive** | 1 | 1 | - | 127.23 | - | 7,357 | - | 0.000259 | 🔵 low — common in general English | — |
| 7708 | **judge** | 1 | 1 | - | 127.23 | - | 7,358 | - | 0.000259 | 🔵 low — common in general English | — |
| 7709 | **version** | 1 | 1 | - | 127.23 | - | 7,359 | - | 0.000259 | 🔵 low — common in general English | — |
| 7710 | **slack** | 1 | 1 | - | 126.34 | - | 7,360 | - | 0.000259 | 🔵 low — common in general English | — |
| 7711 | **favoured** | 1 | 1 | - | 126.34 | - | 7,361 | - | 0.000259 | 🔵 low — common in general English | — |
| 7712 | **quiet** | 1 | 1 | - | 126.34 | - | 7,362 | - | 0.000259 | 🔵 low — common in general English | — |
| 7713 | **mile** | 1 | 1 | - | 126.34 | - | 7,363 | - | 0.000259 | 🔵 low — common in general English | — |
| 7714 | **park** | 1 | 1 | - | 126.34 | - | 7,364 | - | 0.000259 | 🔵 low — common in general English | — |
| 7715 | **arranging** | 1 | 1 | - | 126.34 | - | 7,365 | - | 0.000259 | 🔵 low — common in general English | — |
| 7716 | **limiting** | 1 | 1 | - | 125.50 | - | 7,366 | - | 0.000259 | 🔵 low — common in general English | — |
| 7717 | **ward** | 1 | 1 | - | 125.50 | - | 7,367 | - | 0.000259 | 🔵 low — common in general English | — |
| 7718 | **reversal** | 1 | 1 | - | 125.50 | - | 7,368 | - | 0.000259 | 🔵 low — common in general English | — |
| 7719 | **accident** | 1 | 1 | - | 125.50 | - | 7,369 | - | 0.000259 | 🔵 low — common in general English | — |
| 7720 | **treasurer** | 1 | 1 | - | 125.50 | - | 7,370 | - | 0.000259 | 🔵 low — common in general English | — |
| 7721 | **concerted** | 1 | 1 | - | 125.50 | - | 7,371 | - | 0.000259 | 🔵 low — common in general English | — |
| 7722 | **pressed** | 1 | 1 | - | 125.50 | - | 7,372 | - | 0.000259 | 🔵 low — common in general English | — |
| 7723 | **prevented** | 1 | 1 | - | 125.50 | - | 7,373 | - | 0.000259 | 🔵 low — common in general English | — |
| 7724 | **alter** | 1 | 1 | - | 125.50 | - | 7,374 | - | 0.000259 | 🔵 low — common in general English | — |
| 7725 | **acted** | 1 | 1 | - | 125.50 | - | 7,375 | - | 0.000259 | 🔵 low — common in general English | — |
| 7726 | **evaluation** | 1 | 1 | - | 125.50 | - | 7,376 | - | 0.000259 | 🔵 low — common in general English | — |
| 7727 | **lanka** | 1 | 1 | - | 125.50 | - | 7,377 | - | 0.000259 | 🔵 low — common in general English | — |
| 7728 | **chamber** | 1 | 1 | - | 125.50 | - | 7,378 | - | 0.000259 | 🔵 low — common in general English | — |
| 7729 | **exercised** | 1 | 1 | - | 124.69 | - | 7,379 | - | 0.000259 | 🔵 low — common in general English | — |
| 7730 | **century** | 1 | 1 | - | 124.69 | - | 7,380 | - | 0.000259 | 🔵 low — common in general English | — |
| 7731 | **engine** | 1 | 1 | - | 124.69 | - | 7,381 | - | 0.000259 | 🔵 low — common in general English | — |
| 7732 | **accused** | 1 | 1 | - | 124.69 | - | 7,382 | - | 0.000259 | 🔵 low — common in general English | — |
| 7733 | **criteria** | 1 | 1 | - | 124.69 | - | 7,383 | - | 0.000259 | 🔵 low — common in general English | — |
| 7734 | **track** | 1 | 1 | - | 124.69 | - | 7,384 | - | 0.000259 | 🔵 low — common in general English | — |
| 7735 | **pro** | 1 | 1 | - | 124.69 | - | 7,385 | - | 0.000259 | 🔵 low — common in general English | — |
| 7736 | **distribute** | 1 | 1 | - | 124.69 | - | 7,386 | - | 0.000259 | 🔵 low — common in general English | — |
| 7737 | **challenge** | 1 | 1 | - | 124.69 | - | 7,387 | - | 0.000259 | 🔵 low — common in general English | — |
| 7738 | **instrument** | 1 | 1 | - | 124.69 | - | 7,388 | - | 0.000259 | 🔵 low — common in general English | — |
| 7739 | **cane** | 1 | 1 | - | 123.92 | - | 7,389 | - | 0.000259 | 🔵 low — common in general English | — |
| 7740 | **linking** | 1 | 1 | - | 123.92 | - | 7,390 | - | 0.000259 | 🔵 low — common in general English | — |
| 7741 | **disappointed** | 1 | 1 | - | 123.92 | - | 7,391 | - | 0.000259 | 🔵 low — common in general English | — |
| 7742 | **defined** | 1 | 1 | - | 123.92 | - | 7,393 | - | 0.000259 | 🔵 low — common in general English | — |
| 7743 | **secured** | 1 | 1 | - | 123.92 | - | 7,394 | - | 0.000259 | 🔵 low — common in general English | — |
| 7744 | **dominion** | 1 | 1 | - | 123.92 | - | 7,395 | - | 0.000259 | 🔵 low — common in general English | — |
| 7745 | **considerably** | 1 | 1 | - | 123.18 | - | 7,396 | - | 0.000259 | 🔵 low — common in general English | — |
| 7746 | **basket** | 1 | 1 | - | 123.18 | - | 7,397 | - | 0.000258 | 🔵 low — common in general English | — |
| 7747 | **preserve** | 1 | 1 | - | 123.18 | - | 7,398 | - | 0.000258 | 🔵 low — common in general English | — |
| 7748 | **entering** | 1 | 1 | - | 122.48 | - | 7,399 | - | 0.000258 | 🔵 low — common in general English | — |
| 7749 | **freeze** | 1 | 1 | - | 122.48 | - | 7,400 | - | 0.000258 | 🔵 low — common in general English | — |
| 7750 | **accelerate** | 1 | 1 | - | 122.48 | - | 7,401 | - | 0.000258 | 🔵 low — common in general English | — |
| 7751 | **negotiation** | 1 | 1 | - | 122.48 | - | 7,402 | - | 0.000258 | 🔵 low — common in general English | — |
| 7752 | **awaiting** | 1 | 1 | - | 122.48 | - | 7,403 | - | 0.000258 | 🔵 low — common in general English | — |
| 7753 | **consuming** | 1 | 1 | - | 122.48 | - | 7,404 | - | 0.000258 | 🔵 low — common in general English | — |
| 7754 | **successfully** | 1 | 1 | - | 122.48 | - | 7,405 | - | 0.000258 | 🔵 low — common in general English | — |
| 7755 | **discovered** | 1 | 1 | - | 122.48 | - | 7,406 | - | 0.000258 | 🔵 low — common in general English | — |
| 7756 | **spur** | 1 | 1 | - | 122.48 | - | 7,407 | - | 0.000258 | 🔵 low — common in general English | — |
| 7757 | **contrast** | 1 | 1 | - | 121.80 | - | 7,408 | - | 0.000258 | 🔵 low — common in general English | — |
| 7758 | **valid** | 1 | 1 | - | 121.80 | - | 7,409 | - | 0.000258 | 🔵 low — common in general English | — |
| 7759 | **participating** | 1 | 1 | - | 121.80 | - | 7,410 | - | 0.000258 | 🔵 low — common in general English | — |
| 7760 | **forcing** | 1 | 1 | - | 121.80 | - | 7,411 | - | 0.000258 | 🔵 low — common in general English | — |
| 7761 | **questioned** | 1 | 1 | - | 121.80 | - | 7,412 | - | 0.000258 | 🔵 low — common in general English | — |
| 7762 | **sixth** | 1 | 1 | - | 121.80 | - | 7,413 | - | 0.000258 | 🔵 low — common in general English | — |
| 7763 | **printing** | 1 | 1 | - | 121.80 | - | 7,414 | - | 0.000258 | 🔵 low — common in general English | — |
| 7764 | **table** | 1 | 1 | - | 121.14 | - | 7,415 | - | 0.000258 | 🔵 low — common in general English | — |
| 7765 | **exact** | 1 | 1 | - | 121.14 | - | 7,416 | - | 0.000258 | 🔵 low — common in general English | — |
| 7766 | **convert** | 1 | 1 | - | 121.14 | - | 7,417 | - | 0.000258 | 🔵 low — common in general English | — |
| 7767 | **qualified** | 1 | 1 | - | 121.14 | - | 7,418 | - | 0.000258 | 🔵 low — common in general English | — |
| 7768 | **window** | 1 | 1 | - | 121.14 | - | 7,419 | - | 0.000258 | 🔵 low — common in general English | — |
| 7769 | **match** | 1 | 1 | - | 120.51 | - | 7,420 | - | 0.000258 | 🔵 low — common in general English | — |
| 7770 | **tighten** | 1 | 1 | - | 120.51 | - | 7,421 | - | 0.000258 | 🔵 low — common in general English | — |
| 7771 | **flour** | 1 | 1 | - | 120.51 | - | 7,422 | - | 0.000258 | 🔵 low — common in general English | — |
| 7772 | **acceptance** | 1 | 1 | - | 120.51 | - | 7,424 | - | 0.000258 | 🔵 low — common in general English | — |
| 7773 | **scope** | 1 | 1 | - | 120.51 | - | 7,425 | - | 0.000258 | 🔵 low — common in general English | — |
| 7774 | **diamond** | 1 | 1 | - | 119.90 | - | 7,426 | - | 0.000258 | 🔵 low — common in general English | — |
| 7775 | **engaged** | 1 | 1 | - | 119.90 | - | 7,427 | - | 0.000258 | 🔵 low — common in general English | — |
| 7776 | **necessarily** | 1 | 1 | - | 119.90 | - | 7,428 | - | 0.000258 | 🔵 low — common in general English | — |
| 7777 | **soared** | 1 | 1 | - | 119.90 | - | 7,429 | - | 0.000258 | 🔵 low — common in general English | — |
| 7778 | **handling** | 1 | 1 | - | 119.90 | - | 7,430 | - | 0.000258 | 🔵 low — common in general English | — |
| 7779 | **tobacco** | 1 | 1 | - | 119.90 | - | 7,431 | - | 0.000258 | 🔵 low — common in general English | — |
| 7780 | **discussing** | 1 | 1 | - | 119.90 | - | 7,432 | - | 0.000258 | 🔵 low — common in general English | — |
| 7781 | **optimism** | 1 | 1 | - | 119.32 | - | 7,433 | - | 0.000258 | 🔵 low — common in general English | — |
| 7782 | **prevailing** | 1 | 1 | - | 119.32 | - | 7,434 | - | 0.000258 | 🔵 low — common in general English | — |
| 7783 | **expecting** | 1 | 1 | - | 119.32 | - | 7,435 | - | 0.000258 | 🔵 low — common in general English | — |
| 7784 | **critical** | 1 | 1 | - | 119.32 | - | 7,436 | - | 0.000258 | 🔵 low — common in general English | — |
| 7785 | **proceeding** | 1 | 1 | - | 119.32 | - | 7,437 | - | 0.000258 | 🔵 low — common in general English | — |
| 7786 | **conducted** | 1 | 1 | - | 119.32 | - | 7,438 | - | 0.000258 | 🔵 low — common in general English | — |
| 7787 | **respective** | 1 | 1 | - | 119.32 | - | 7,439 | - | 0.000258 | 🔵 low — common in general English | — |
| 7788 | **speed** | 1 | 1 | - | 119.32 | - | 7,440 | - | 0.000258 | 🔵 low — common in general English | — |
| 7789 | **friendly** | 1 | 1 | - | 119.32 | - | 7,441 | - | 0.000258 | 🔵 low — common in general English | — |
| 7790 | **adopt** | 1 | 1 | - | 119.32 | - | 7,442 | - | 0.000258 | 🔵 low — common in general English | — |
| 7791 | **explore** | 1 | 1 | - | 118.75 | - | 7,443 | - | 0.000258 | 🔵 low — common in general English | — |
| 7792 | **tool** | 1 | 1 | - | 118.75 | - | 7,444 | - | 0.000258 | 🔵 low — common in general English | — |
| 7793 | **quick** | 1 | 1 | - | 118.75 | - | 7,445 | - | 0.000258 | 🔵 low — common in general English | — |
| 7794 | **incurred** | 1 | 1 | - | 118.75 | - | 7,446 | - | 0.000258 | 🔵 low — common in general English | — |
| 7795 | **somewhat** | 1 | 1 | - | 118.75 | - | 7,447 | - | 0.000258 | 🔵 low — common in general English | — |
| 7796 | **eliminate** | 1 | 1 | - | 118.75 | - | 7,448 | - | 0.000258 | 🔵 low — common in general English | — |
| 7797 | **settled** | 1 | 1 | - | 118.75 | - | 7,449 | - | 0.000258 | 🔵 low — common in general English | — |
| 7798 | **responding** | 1 | 1 | - | 118.75 | - | 7,450 | - | 0.000258 | 🔵 low — common in general English | — |
| 7799 | **deterioration** | 1 | 1 | - | 118.20 | - | 7,451 | - | 0.000258 | 🔵 low — common in general English | — |
| 7800 | **formula** | 1 | 1 | - | 118.20 | - | 7,452 | - | 0.000258 | 🔵 low — common in general English | — |
| 7801 | **rally** | 1 | 1 | - | 118.20 | - | 7,453 | - | 0.000257 | 🔵 low — common in general English | — |
| 7802 | **steadily** | 1 | 1 | - | 118.20 | - | 7,454 | - | 0.000257 | 🔵 low — common in general English | — |
| 7803 | **flag** | 1 | 1 | - | 118.20 | - | 7,455 | - | 0.000257 | 🔵 low — common in general English | — |
| 7804 | **extensive** | 1 | 1 | - | 118.20 | - | 7,456 | - | 0.000257 | 🔵 low — common in general English | — |
| 7805 | **enhance** | 1 | 1 | - | 117.67 | - | 7,457 | - | 0.000257 | 🔵 low — common in general English | — |
| 7806 | **tightening** | 1 | 1 | - | 117.67 | - | 7,458 | - | 0.000257 | 🔵 low — common in general English | — |
| 7807 | **permanent** | 1 | 1 | - | 117.67 | - | 7,459 | - | 0.000257 | 🔵 low — common in general English | — |
| 7808 | **informed** | 1 | 1 | - | 117.67 | - | 7,461 | - | 0.000257 | 🔵 low — common in general English | — |
| 7809 | **prompted** | 1 | 1 | - | 117.67 | - | 7,462 | - | 0.000257 | 🔵 low — common in general English | — |
| 7810 | **incentive** | 1 | 1 | - | 117.67 | - | 7,463 | - | 0.000257 | 🔵 low — common in general English | — |
| 7811 | **indirect** | 1 | 1 | - | 117.15 | - | 7,464 | - | 0.000257 | 🔵 low — common in general English | — |
| 7812 | **healthy** | 1 | 1 | - | 117.15 | - | 7,465 | - | 0.000257 | 🔵 low — common in general English | — |
| 7813 | **missile** | 1 | 1 | - | 117.15 | - | 7,466 | - | 0.000257 | 🔵 low — common in general English | — |
| 7814 | **reaching** | 1 | 1 | - | 117.15 | - | 7,467 | - | 0.000257 | 🔵 low — common in general English | — |
| 7815 | **southeast** | 1 | 1 | - | 116.65 | - | 7,468 | - | 0.000257 | 🔵 low — common in general English | — |
| 7816 | **withdraw** | 1 | 1 | - | 116.65 | - | 7,469 | - | 0.000257 | 🔵 low — common in general English | — |
| 7817 | **burden** | 1 | 1 | - | 116.65 | - | 7,470 | - | 0.000257 | 🔵 low — common in general English | — |
| 7818 | **maturing** | 1 | 1 | - | 116.16 | - | 7,471 | - | 0.000257 | 🔵 low — common in general English | — |
| 7819 | **merchandise** | 1 | 1 | - | 116.16 | - | 7,472 | - | 0.000257 | 🔵 low — common in general English | — |
| 7820 | **flexible** | 1 | 1 | - | 116.16 | - | 7,473 | - | 0.000257 | 🔵 low — common in general English | — |
| 7821 | **chase** | 1 | 1 | - | 115.68 | - | 7,474 | - | 0.000257 | 🔵 low — common in general English | — |
| 7822 | **reviewing** | 1 | 1 | - | 115.68 | - | 7,475 | - | 0.000257 | 🔵 low — common in general English | — |
| 7823 | **uncertain** | 1 | 1 | - | 115.22 | - | 7,476 | - | 0.000257 | 🔵 low — common in general English | — |
| 7824 | **aggregate** | 1 | 1 | - | 115.22 | - | 7,477 | - | 0.000257 | 🔵 low — common in general English | — |
| 7825 | **southwest** | 1 | 1 | - | 114.77 | - | 7,478 | - | 0.000257 | 🔵 low — common in general English | — |
| 7826 | **northwest** | 1 | 1 | - | 114.77 | - | 7,479 | - | 0.000257 | 🔵 low — common in general English | — |
| 7827 | **referring** | 1 | 1 | - | 114.77 | - | 7,480 | - | 0.000257 | 🔵 low — common in general English | — |
| 7828 | **record** | 1 | 2 | - | 114.33 | - | 7,481 | - | 0.000257 | 🔵 low — common in general English | — |
| 7829 | **job** | 1 | 1 | - | 114.33 | - | 7,482 | - | 0.000257 | 🔵 low — common in general English | — |
| 7830 | **sum** | 1 | 1 | - | 114.33 | - | 7,483 | - | 0.000257 | 🔵 low — common in general English | — |
| 7831 | **scheme** | 1 | 1 | - | 114.33 | - | 7,484 | - | 0.000257 | 🔵 low — common in general English | — |
| 7832 | **fast** | 1 | 1 | - | 114.33 | - | 7,485 | - | 0.000257 | 🔵 low — common in general English | — |
| 7833 | **solution** | 1 | 1 | - | 113.90 | - | 7,486 | - | 0.000257 | 🔵 low — common in general English | — |
| 7834 | **investigation** | 1 | 1 | - | 113.90 | - | 7,487 | - | 0.000257 | 🔵 low — common in general English | — |
| 7835 | **promote** | 1 | 1 | - | 113.49 | - | 7,488 | - | 0.000257 | 🔵 low — common in general English | — |
| 7836 | **remove** | 1 | 1 | - | 113.49 | - | 7,489 | - | 0.000257 | 🔵 low — common in general English | — |
| 7837 | **regarding** | 1 | 1 | - | 113.08 | - | 7,490 | - | 0.000257 | 🔵 low — common in general English | — |
| 7838 | **dealing** | 1 | 1 | - | 113.08 | - | 7,491 | - | 0.000257 | 🔵 low — common in general English | — |
| 7839 | **arrangement** | 1 | 1 | - | 112.68 | - | 7,492 | - | 0.000257 | 🔵 low — common in general English | — |
| 7840 | **effectively** | 1 | 1 | - | 112.68 | - | 7,493 | - | 0.000257 | 🔵 low — common in general English | — |
| 7841 | **dumping** | 1 | 1 | - | 112.29 | - | 7,494 | - | 0.000257 | 🔵 low — common in general English | — |
| 7842 | **announce** | 1 | 1 | - | 112.29 | - | 7,495 | - | 0.000257 | 🔵 low — common in general English | — |
| 7843 | **maintained** | 1 | 1 | - | 111.91 | - | 7,496 | - | 0.000257 | 🔵 low — common in general English | — |
| 7844 | **respond** | 1 | 1 | - | 111.91 | - | 7,497 | - | 0.000257 | 🔵 low — common in general English | — |
| 7845 | **compete** | 1 | 1 | - | 111.91 | - | 7,498 | - | 0.000257 | 🔵 low — common in general English | — |
| 7846 | **widely** | 1 | 1 | - | 111.54 | - | 7,499 | - | 0.000257 | 🔵 low — common in general English | — |
| 7847 | **duty** | 1 | 1 | - | 111.54 | - | 7,500 | - | 0.000257 | 🔵 low — common in general English | — |
| 7848 | **calculated** | 1 | 1 | - | 111.54 | - | 7,501 | - | 0.000257 | 🔵 low — common in general English | — |
| 7849 | **planted** | 1 | 1 | - | 111.17 | - | 7,502 | - | 0.000257 | 🔵 low — common in general English | — |
| 7850 | **strengthen** | 1 | 1 | - | 111.17 | - | 7,503 | - | 0.000257 | 🔵 low — common in general English | — |
| 7851 | **consistent** | 1 | 1 | - | 111.17 | - | 7,504 | - | 0.000257 | 🔵 low — common in general English | — |
| 7852 | **charged** | 1 | 1 | - | 111.17 | - | 7,505 | - | 0.000257 | 🔵 low — common in general English | — |
| 7853 | **showing** | 1 | 1 | - | 110.81 | - | 7,506 | - | 0.000257 | 🔵 low — common in general English | — |
| 7854 | **list** | 1 | 1 | - | 110.46 | - | 7,507 | - | 0.000257 | 🔵 low — common in general English | — |
| 7855 | **increasingly** | 1 | 1 | - | 110.46 | - | 7,508 | - | 0.000257 | 🔵 low — common in general English | — |
| 7856 | **appreciation** | 1 | 1 | - | 110.46 | - | 7,509 | - | 0.000257 | 🔵 low — common in general English | — |
| 7857 | **broadly** | 1 | 1 | - | 110.46 | - | 7,510 | - | 0.000256 | 🔵 low — common in general English | — |
| 7858 | **apparently** | 1 | 1 | - | 110.12 | - | 7,511 | - | 0.000256 | 🔵 low — common in general English | — |
| 7859 | **contribution** | 1 | 1 | - | 110.12 | - | 7,512 | - | 0.000256 | 🔵 low — common in general English | — |
| 7860 | **concluded** | 1 | 1 | - | 110.12 | - | 7,513 | - | 0.000256 | 🔵 low — common in general English | — |
| 7861 | **shell** | 1 | 1 | - | 110.12 | - | 7,514 | - | 0.000256 | 🔵 low — common in general English | — |
| 7862 | **housing** | 1 | 1 | - | 109.79 | - | 7,515 | - | 0.000256 | 🔵 low — common in general English | — |
| 7863 | **stressed** | 1 | 1 | - | 109.79 | - | 7,516 | - | 0.000256 | 🔵 low — common in general English | — |
| 7864 | **represented** | 1 | 1 | - | 109.79 | - | 7,517 | - | 0.000256 | 🔵 low — common in general English | — |
| 7865 | **relief** | 1 | 1 | - | 109.45 | - | 7,518 | - | 0.000256 | 🔵 low — common in general English | — |
| 7866 | **smith** | 1 | 1 | - | 109.45 | - | 7,519 | - | 0.000256 | 🔵 low — common in general English | — |
| 7867 | **applied** | 1 | 1 | - | 109.45 | - | 7,520 | - | 0.000256 | 🔵 low — common in general English | — |
| 7868 | **moderate** | 1 | 1 | - | 109.45 | - | 7,521 | - | 0.000256 | 🔵 low — common in general English | — |
| 7869 | **expense** | 1 | 1 | - | 109.45 | - | 7,522 | - | 0.000256 | 🔵 low — common in general English | — |
| 7870 | **waiting** | 1 | 1 | - | 109.45 | - | 7,523 | - | 0.000256 | 🔵 low — common in general English | — |
| 7871 | **sentiment** | 1 | 1 | - | 109.13 | - | 7,524 | - | 0.000256 | 🔵 low — common in general English | — |
| 7872 | **affecting** | 1 | 1 | - | 108.81 | - | 7,525 | - | 0.000256 | 🔵 low — common in general English | — |
| 7873 | **indicate** | 1 | 1 | - | 108.81 | - | 7,526 | - | 0.000256 | 🔵 low — common in general English | — |
| 7874 | **uncertainty** | 1 | 1 | - | 108.50 | - | 7,527 | - | 0.000256 | 🔵 low — common in general English | — |
| 7875 | **mostly** | 1 | 1 | - | 108.50 | - | 7,528 | - | 0.000256 | 🔵 low — common in general English | — |
| 7876 | **resume** | 1 | 1 | - | 108.19 | - | 7,529 | - | 0.000256 | 🔵 low — common in general English | — |
| 7877 | **severe** | 1 | 1 | - | 108.19 | - | 7,530 | - | 0.000256 | 🔵 low — common in general English | — |
| 7878 | **portion** | 1 | 1 | - | 107.89 | - | 7,531 | - | 0.000256 | 🔵 low — common in general English | — |
| 7879 | **traditional** | 1 | 1 | - | 107.60 | - | 7,532 | - | 0.000256 | 🔵 low — common in general English | — |
| 7880 | **intervene** | 1 | 1 | - | 107.31 | - | 7,533 | - | 0.000256 | 🔵 low — common in general English | — |
| 7881 | **threat** | 1 | 1 | - | 107.02 | - | 7,534 | - | 0.000256 | 🔵 low — common in general English | — |
| 7882 | **gap** | 1 | 1 | - | 106.46 | - | 7,535 | - | 0.000256 | 🔵 low — common in general English | — |
| 7883 | **coal** | 1 | 1 | - | 106.19 | - | 7,536 | - | 0.000256 | 🔵 low — common in general English | — |
| 7884 | **medium** | 1 | 1 | - | 106.19 | - | 7,537 | - | 0.000256 | 🔵 low — common in general English | — |
| 7885 | **suggested** | 1 | 1 | - | 106.19 | - | 7,538 | - | 0.000256 | 🔵 low — common in general English | — |
| 7886 | **ups** | 1 | 1 | - | 105.92 | - | 7,539 | - | 0.000256 | 🔵 low — common in general English | — |
| 7887 | **subordinated** | 1 | 1 | - | 105.92 | - | 7,540 | - | 0.000256 | 🔵 low — common in general English | — |
| 7888 | **buyer** | 1 | 1 | - | 105.92 | - | 7,541 | - | 0.000256 | 🔵 low — common in general English | — |
| 7889 | **opposed** | 1 | 1 | - | 105.65 | - | 7,542 | - | 0.000256 | 🔵 low — common in general English | — |
| 7890 | **leader** | 1 | 1 | - | 105.65 | - | 7,543 | - | 0.000256 | 🔵 low — common in general English | — |
| 7891 | **stronger** | 1 | 1 | - | 105.14 | - | 7,544 | - | 0.000256 | 🔵 low — common in general English | — |
| 7892 | **fair** | 1 | 1 | - | 105.14 | - | 7,545 | - | 0.000256 | 🔵 low — common in general English | — |
| 7893 | **possibly** | 1 | 1 | - | 104.63 | - | 7,546 | - | 0.000256 | 🔵 low — common in general English | — |
| 7894 | **original** | 1 | 1 | - | 104.63 | - | 7,547 | - | 0.000256 | 🔵 low — common in general English | — |
| 7895 | **underlying** | 1 | 1 | - | 103.67 | - | 7,548 | - | 0.000256 | 🔵 low — common in general English | — |
| 7896 | **alternative** | 1 | 1 | - | 103.67 | - | 7,549 | - | 0.000256 | 🔵 low — common in general English | — |
| 7897 | **medical** | 1 | 1 | - | 103.44 | - | 7,550 | - | 0.000256 | 🔵 low — common in general English | — |
| 7898 | **raw** | 1 | 1 | - | 103.21 | - | 7,551 | - | 0.000256 | 🔵 low — common in general English | — |
| 7899 | **labour** | 1 | 1 | - | 103.21 | - | 7,552 | - | 0.000256 | 🔵 low — common in general English | — |
| 7900 | **active** | 1 | 1 | - | 103.21 | - | 7,553 | - | 0.000256 | 🔵 low — common in general English | — |
| 7901 | **profitable** | 1 | 1 | - | 102.76 | - | 7,554 | - | 0.000256 | 🔵 low — common in general English | — |
| 7902 | **rice** | 1 | 1 | - | 102.76 | - | 7,555 | - | 0.000256 | 🔵 low — common in general English | — |
| 7903 | **note** | 1 | 2 | - | 102.61 | - | 7,556 | - | 0.000256 | 🔵 low — common in general English | — |
| 7904 | **exceed** | 1 | 1 | - | 102.54 | - | 7,557 | - | 0.000256 | 🔵 low — common in general English | — |
| 7905 | **sought** | 1 | 1 | - | 102.54 | - | 7,558 | - | 0.000256 | 🔵 low — common in general English | — |
| 7906 | **governor** | 1 | 1 | - | 102.10 | - | 7,559 | - | 0.000256 | 🔵 low — common in general English | — |
| 7907 | **block** | 1 | 1 | - | 102.10 | - | 7,560 | - | 0.000256 | 🔵 low — common in general English | — |
| 7908 | **originally** | 1 | 1 | - | 101.07 | - | 7,561 | - | 0.000256 | 🔵 low — common in general English | — |
| 7909 | **afternoon** | 1 | 1 | - | 101.07 | - | 7,562 | - | 0.000256 | 🔵 low — common in general English | — |
| 7910 | **via** | 1 | 1 | - | 100.87 | - | 7,563 | - | 0.000256 | 🔵 low — common in general English | — |
| 7911 | **expressed** | 1 | 1 | - | 100.47 | - | 7,564 | - | 0.000256 | 🔵 low — common in general English | — |
| 7912 | **legal** | 1 | 1 | - | 100.28 | - | 7,565 | - | 0.000256 | 🔵 low — common in general English | — |
| 7913 | **yield** | 1 | 1 | - | 100.28 | - | 7,566 | - | 0.000256 | 🔵 low — common in general English | — |
| 7914 | **resulted** | 1 | 1 | - | 100.09 | - | 7,567 | - | 0.000256 | 🔵 low — common in general English | — |
| 7915 | **authorized** | 1 | 1 | - | 99.71 | - | 7,568 | - | 0.000255 | 🔵 low — common in general English | — |
| 7916 | **fuel** | 1 | 1 | - | 99.34 | - | 7,569 | - | 0.000255 | 🔵 low — common in general English | — |
| 7917 | **indicated** | 1 | 1 | - | 99.34 | - | 7,570 | - | 0.000255 | 🔵 low — common in general English | — |
| 7918 | **designed** | 1 | 1 | - | 99.34 | - | 7,571 | - | 0.000255 | 🔵 low — common in general English | — |
| 7919 | **projected** | 1 | 1 | - | 98.98 | - | 7,572 | - | 0.000255 | 🔵 low — common in general English | — |
| 7920 | **aid** | 1 | 1 | - | 97.77 | - | 7,573 | - | 0.000255 | 🔵 low — common in general English | — |
| 7921 | **recovery** | 1 | 1 | - | 97.61 | - | 7,574 | - | 0.000255 | 🔵 low — common in general English | — |
| 7922 | **planning** | 1 | 1 | - | 97.61 | - | 7,575 | - | 0.000255 | 🔵 low — common in general English | — |
| 7923 | **estate** | 1 | 1 | - | 97.28 | - | 7,576 | - | 0.000255 | 🔵 low — common in general English | — |
| 7924 | **bond** | 1 | 1 | - | 97.28 | - | 7,577 | - | 0.000255 | 🔵 low — common in general English | — |
| 7925 | **stable** | 1 | 1 | - | 97.12 | - | 7,578 | - | 0.000255 | 🔵 low — common in general English | — |
| 7926 | **project** | 1 | 1 | - | 96.96 | - | 7,579 | - | 0.000255 | 🔵 low — common in general English | — |
| 7927 | **minimum** | 1 | 1 | - | 96.18 | - | 7,580 | - | 0.000255 | 🔵 low — common in general English | — |
| 7928 | **construction** | 1 | 1 | - | 96.03 | - | 7,581 | - | 0.000255 | 🔵 low — common in general English | — |
| 7929 | **posted** | 1 | 1 | - | 95.88 | - | 7,582 | - | 0.000255 | 🔵 low — common in general English | — |
| 7930 | **failed** | 1 | 1 | - | 95.73 | - | 7,583 | - | 0.000255 | 🔵 low — common in general English | — |
| 7931 | **raising** | 1 | 1 | - | 95.73 | - | 7,584 | - | 0.000255 | 🔵 low — common in general English | — |
| 7932 | **assistance** | 1 | 1 | - | 95.44 | - | 7,585 | - | 0.000255 | 🔵 low — common in general English | — |
| 7933 | **believed** | 1 | 1 | - | 95.29 | - | 7,586 | - | 0.000255 | 🔵 low — common in general English | — |
| 7934 | **performance** | 1 | 1 | - | 93.00 | - | 7,587 | - | 0.000255 | 🔵 low — common in general English | — |
| 7935 | **plus** | 1 | 1 | - | 92.87 | - | 7,588 | - | 0.000255 | 🔵 low — common in general English | — |
| 7936 | **consumption** | 1 | 1 | - | 92.62 | - | 7,589 | - | 0.000255 | 🔵 low — common in general English | — |
| 7937 | **closing** | 1 | 1 | - | 92.38 | - | 7,590 | - | 0.000255 | 🔵 low — common in general English | — |
| 7938 | **rejected** | 1 | 1 | - | 92.01 | - | 7,591 | - | 0.000255 | 🔵 low — common in general English | — |
| 7939 | **information** | 1 | 1 | - | 91.66 | - | 7,592 | - | 0.000255 | 🔵 low — common in general English | — |
| 7940 | **required** | 1 | 1 | - | 91.20 | - | 7,593 | - | 0.000255 | 🔵 low — common in general English | — |
| 7941 | **producing** | 1 | 1 | - | 90.97 | - | 7,594 | - | 0.000255 | 🔵 low — common in general English | — |
| 7942 | **nearly** | 1 | 1 | - | 90.64 | - | 7,595 | - | 0.000255 | 🔵 low — common in general English | — |
| 7943 | **regular** | 1 | 1 | - | 90.53 | - | 7,596 | - | 0.000255 | 🔵 low — common in general English | — |
| 7944 | **significant** | 1 | 1 | - | 89.26 | - | 7,597 | - | 0.000255 | 🔵 low — common in general English | — |
| 7945 | **initial** | 1 | 1 | - | 89.05 | - | 7,598 | - | 0.000255 | 🔵 low — common in general English | — |
| 7946 | **farm** | 1 | 1 | - | 88.85 | - | 7,599 | - | 0.000255 | 🔵 low — common in general English | — |
| 7947 | **gross** | 1 | 1 | - | 88.17 | - | 7,600 | - | 0.000255 | 🔵 low — common in general English | — |
| 7948 | **adding** | 1 | 1 | - | 87.06 | - | 7,601 | - | 0.000255 | 🔵 low — common in general English | — |
| 7949 | **range** | 1 | 1 | - | 86.44 | - | 7,602 | - | 0.000255 | 🔵 low — common in general English | — |
| 7950 | **respectively** | 1 | 1 | - | 86.35 | - | 7,603 | - | 0.000255 | 🔵 low — common in general English | — |
| 7951 | **probably** | 1 | 1 | - | 86.18 | - | 7,604 | - | 0.000255 | 🔵 low — common in general English | — |
| 7952 | **charge** | 1 | 1 | - | 85.35 | - | 7,605 | - | 0.000255 | 🔵 low — common in general English | — |
| 7953 | **selling** | 1 | 1 | - | 84.09 | - | 7,606 | - | 0.000255 | 🔵 low — common in general English | — |
| 7954 | **buying** | 1 | 1 | - | 82.50 | - | 7,607 | - | 0.000255 | 🔵 low — common in general English | — |
| 7955 | **despite** | 1 | 1 | - | 81.50 | - | 7,608 | - | 0.000255 | 🔵 low — common in general English | — |
| 7956 | **net** | 1 | 2 | - | 80.36 | - | 7,609 | - | 0.000255 | 🔵 low — common in general English | — |
| 7957 | **transaction** | 1 | 1 | - | 80.30 | - | 7,610 | - | 0.000255 | 🔵 low — common in general English | — |
| 7958 | **available** | 1 | 1 | - | 79.59 | - | 7,611 | - | 0.000255 | 🔵 low — common in general English | — |
| 7959 | **secretary** | 1 | 1 | - | 79.24 | - | 7,612 | - | 0.000255 | 🔵 low — common in general English | — |
| 7960 | **loan** | 1 | 1 | - | 77.35 | - | 7,613 | - | 0.000255 | 🔵 low — common in general English | — |
| 7961 | **public** | 1 | 1 | - | 76.25 | - | 7,614 | - | 0.000255 | 🔵 low — common in general English | — |
| 7962 | **bought** | 1 | 1 | - | 74.65 | - | 7,615 | - | 0.000255 | 🔵 low — common in general English | — |
| 7963 | **outstanding** | 1 | 1 | - | 70.91 | - | 7,616 | - | 0.000255 | 🔵 low — common in general English | — |
| 7964 | **yesterday** | 1 | 1 | - | 70.42 | - | 7,617 | - | 0.000255 | 🔵 low — common in general English | — |
| 7965 | **trading** | 1 | 1 | - | 70.35 | - | 7,618 | - | 0.000255 | 🔵 low — common in general English | — |
| 7966 | **capital** | 1 | 1 | - | 69.49 | - | 7,619 | - | 0.000255 | 🔵 low — common in general English | — |
| 7967 | **statement** | 1 | 1 | - | 67.90 | - | 7,620 | - | 0.000255 | 🔵 low — common in general English | — |
| 7968 | **industry** | 1 | 1 | - | 67.84 | - | 7,621 | - | 0.000255 | 🔵 low — common in general English | — |
| 7969 | **official** | 1 | 1 | - | 65.21 | - | 7,622 | - | 0.000255 | 🔵 low — common in general English | — |
| 7970 | **production** | 1 | 1 | - | 65.08 | - | 7,623 | - | 0.000255 | 🔵 low — common in general English | — |
| 7971 | **tax** | 1 | 1 | - | 65.00 | - | 7,624 | - | 0.000255 | 🔵 low — common in general English | — |
| 7972 | **rose** | 1 | 1 | - | 63.77 | - | 7,625 | - | 0.000255 | 🔵 low — common in general English | — |
| 7973 | **agreed** | 1 | 1 | - | 63.74 | - | 7,626 | - | 0.000255 | 🔵 low — common in general English | — |
| 7974 | **foreign** | 1 | 1 | - | 63.35 | - | 7,627 | - | 0.000254 | 🔵 low — common in general English | — |
| 7975 | **government** | 1 | 1 | - | 60.98 | - | 7,628 | - | 0.000254 | 🔵 low — common in general English | — |
| 7976 | **expected** | 1 | 1 | - | 58.67 | - | 7,629 | - | 0.000254 | 🔵 low — common in general English | — |
| 7977 | **agreement** | 1 | 1 | - | 58.50 | - | 7,631 | - | 0.000254 | 🔵 low — common in general English | — |
| 7978 | **stock** | 1 | 1 | - | 52.87 | - | 7,632 | - | 0.000254 | 🔵 low — common in general English | — |

---

## Gated out

Phrases whose words co-occur no more than chance predicts.

| Term | Count | NPMI | YAKE |
|------|-------|------|------|
| nyatri tsenpo | 2 | 0.963 | 0.277423 |
| khampa lhungpa | 2 | 0.937 | 0.249121 |
| khampa lungpa | 2 | 0.937 | 0.251062 |
| tangtong gyalpo | 2 | 0.937 | 0.267318 |
| kyabje dodrup chen | 2 | 0.937 | 0.282625 |
| lingje repa | 2 | 0.900 | 0.170227 |
| omniscient longchen rabjampa | 2 | 0.887 | 0.197291 |
| geshe kharak gomchung | 2 | 0.874 | 0.101939 |
| drikung kyobpa rinpoche | 2 | 0.873 | 0.183570 |
| kushab rinpoche shenpen | 1 | 0.851 | 0.192233 |
| rinpoche shenpen thaye | 1 | 0.851 | 0.192233 |
| orgyen jigme cbokyi | 1 | 0.844 | 0.295415 |
| diamond cutter sutra | 1 | 0.833 | 0.198410 |
| fortunate dynasty | 2 | 0.811 | 0.240140 |
| nachung tonpa | 2 | 0.806 | 0.143041 |
| abbot santarak | 2 | 0.801 | 0.221756 |
| shepa dorje | 2 | 0.796 | 0.105814 |
| jigme cbokyi | 1 | 0.781 | 0.294274 |
| jigme gyalwai | 1 | 0.781 | 0.294281 |
| tathagata ratnapada | 1 | 0.781 | 0.297826 |
| tathagata siddhyaloka | 1 | 0.781 | 0.297829 |
| padma siddhi hum | 1 | 0.776 | 0.215839 |
| omniscient longchen | 2 | 0.774 | 0.172195 |
| jetsun rangrik repa | 1 | 0.774 | 0.116193 |
| rigdzin changchub dorje | 1 | 0.772 | 0.173799 |
| mila sherab gyaltsen | 1 | 0.767 | 0.085834 |
| geshe khampa lungpa | 1 | 0.763 | 0.155285 |
| clear recollection | 2 | 0.760 | 0.205986 |
| kyung tonpa | 1 | 0.758 | 0.244671 |
| lhangtsang tonpa | 1 | 0.758 | 0.244684 |
| guru padma siddhi | 1 | 0.755 | 0.084673 |
| lake kutra | 2 | 0.754 | 0.173363 |
| mount merus | 1 | 0.749 | 0.118358 |
| mikyo dorje | 1 | 0.749 | 0.210493 |
| jowo dole | 1 | 0.749 | 0.229221 |
| melong dorje | 1 | 0.749 | 0.229734 |
| dorje dudjom | 1 | 0.749 | 0.231342 |
| changchub dorje | 1 | 0.749 | 0.231666 |
| geshe shawopa | 2 | 0.748 | 0.093478 |
| geshe kharak | 2 | 0.748 | 0.093960 |
| kyobpa rinpoche | 2 | 0.746 | 0.069445 |
| siddha melong dorje | 1 | 0.740 | 0.209713 |
| sattva hum | 2 | 0.738 | 0.174020 |
| guru sri simha | 1 | 0.737 | 0.097121 |
| mount malaya | 2 | 0.733 | 0.100824 |
| azure heaven | 1 | 0.732 | 0.287000 |
| lita vimalamitra | 2 | 0.732 | 0.299412 |
| omniscient sovereign | 2 | 0.728 | 0.179589 |
| ninefold black cho | 1 | 0.725 | 0.092220 |
| religious king gomadeviya | 1 | 0.721 | 0.252787 |
| black noose | 2 | 0.717 | 0.224014 |
| vajra sattva hum | 2 | 0.710 | 0.044224 |
| bodhisattva samantabhadra ema | 1 | 0.710 | 0.060355 |
| ninefold black | 1 | 0.710 | 0.285607 |
| geshe tsakpuwa | 1 | 0.704 | 0.202394 |
| visit shang rinpoche | 1 | 0.703 | 0.196220 |
| indian master diparhkara | 1 | 0.702 | 0.074028 |
| town scavenger offering | 1 | 0.702 | 0.288047 |
| invoke glorious vajrasattva | 1 | 0.701 | 0.189815 |
| gyalse rinpoche | 1 | 0.701 | 0.131479 |
| kushab rinpoche | 1 | 0.701 | 0.150435 |
| rinpoche shenpen | 1 | 0.701 | 0.150435 |
| great scholar trakpa | 1 | 0.701 | 0.136372 |
| master tendzin chopel | 1 | 0.699 | 0.116170 |
| mila adamantine victory | 1 | 0.699 | 0.182370 |
| western buddhafield | 2 | 0.695 | 0.103138 |
| steel wheel | 2 | 0.691 | 0.272270 |
| red syllable hrih | 2 | 0.690 | 0.285262 |
| hunter gonpo dorje | 1 | 0.687 | 0.219582 |
| orgyen jigme | 1 | 0.687 | 0.243952 |
| geshe potowa | 2 | 0.685 | 0.087068 |
| shang rinpoche | 2 | 0.683 | 0.057107 |
| dzogchen rinpoche | 2 | 0.683 | 0.058404 |
| eastern buddhafield | 2 | 0.679 | 0.119404 |
| jetsun shepa dorje | 1 | 0.678 | 0.043979 |
| elapatra tree | 2 | 0.677 | 0.230316 |
| geshe langri thangpa | 1 | 0.674 | 0.059179 |
| manifestation garab dorje | 1 | 0.674 | 0.170648 |
| southern buddhafield | 1 | 0.673 | 0.230631 |
| lord suvarl | 1 | 0.671 | 0.130111 |
| lord suvarnadvipa | 1 | 0.671 | 0.130115 |
| omniscient jigme lingpa | 1 | 0.670 | 0.067767 |
| master aryadeva | 2 | 0.669 | 0.059664 |
| innate absolute wisdom | 2 | 0.668 | 0.128653 |
| unaltered natural state | 2 | 0.666 | 0.246835 |
| jetsun rangrik | 1 | 0.666 | 0.139894 |
| cutter sutra | 1 | 0.666 | 0.162932 |
| sutra ofi | 1 | 0.666 | 0.262232 |
| hevajra tantra | 2 | 0.666 | 0.120214 |
| geshe chengawa | 2 | 0.665 | 0.079871 |
| incomparable dagpo rinpoche | 1 | 0.665 | 0.101856 |
| tathagata sri | 1 | 0.663 | 0.224937 |
| precious umbrella | 1 | 0.656 | 0.252581 |
| mila sherab | 1 | 0.653 | 0.103704 |
| leavingjetsun mila | 1 | 0.653 | 0.160892 |
| askedjetsun mila | 1 | 0.653 | 0.160982 |
| bring unending | 2 | 0.651 | 0.262646 |
| marvellous protector amitabha | 1 | 0.647 | 0.198463 |
| arhat katyayana | 1 | 0.646 | 0.215582 |
| eastern india | 2 | 0.646 | 0.088218 |
| famous moon | 2 | 0.646 | 0.220073 |
| geshe chakshingwa | 1 | 0.645 | 0.186896 |
| naropa underwent | 1 | 0.645 | 0.285752 |
| paqqita naropa | 1 | 0.645 | 0.286364 |
| vajra bhumi | 1 | 0.642 | 0.168694 |
| vajra rekhe | 1 | 0.642 | 0.168695 |
| chagme rinpoche | 1 | 0.642 | 0.172853 |
| vajra puspe | 1 | 0.642 | 0.266809 |
| dha vajra | 1 | 0.642 | 0.266817 |
| mila dorje gyaltsen | 1 | 0.642 | 0.026697 |
| vivid faith | 2 | 0.638 | 0.225579 |
| great yogi virupa | 1 | 0.637 | 0.083068 |
| indian siddha naropa | 1 | 0.635 | 0.087571 |
| padampa sangye heard | 1 | 0.635 | 0.149169 |
| sarhsara fritter life | 1 | 0.634 | 0.135684 |
| master mafijusrimitra | 2 | 0.632 | 0.064795 |
| dorje gyaltsen | 1 | 0.630 | 0.172837 |
| master chegom | 1 | 0.629 | 0.130586 |
| master hastibhala | 1 | 0.629 | 0.131188 |
| respected master | 1 | 0.629 | 0.203053 |
| captain compassionate heart | 1 | 0.629 | 0.286849 |
| marpa severely | 1 | 0.628 | 0.247339 |
| lightly small good | 2 | 0.627 | 0.118265 |
| great siddha melong | 1 | 0.627 | 0.057715 |
| wrathful black true | 2 | 0.626 | 0.044853 |
| jowo ben | 2 | 0.626 | 0.114651 |
| exceptionally great giving | 2 | 0.626 | 0.043184 |
| mother camel | 2 | 0.624 | 0.190750 |
| prince great courage | 1 | 0.623 | 0.150240 |
| adamantine clear light | 1 | 0.623 | 0.270074 |
| perfectly pure motivation | 2 | 0.622 | 0.219735 |
| lotus hat | 2 | 0.619 | 0.173207 |
| great scholar vimalamitra | 1 | 0.618 | 0.068293 |
| king ajatasatru | 2 | 0.615 | 0.047128 |
| gonpo dorje | 1 | 0.611 | 0.162988 |
| thousand prelimi | 1 | 0.610 | 0.177916 |
| basic vehicle | 2 | 0.610 | 0.096747 |
| consume flesh | 2 | 0.610 | 0.282540 |
| blissful land | 1 | 0.608 | 0.284551 |
| bodhisattva nivara | 1 | 0.608 | 0.060662 |
| great universal system | 1 | 0.607 | 0.226492 |
| jetsun shepa | 1 | 0.607 | 0.129023 |
| garab dorje set | 1 | 0.606 | 0.078643 |
| glorious vajradhara | 1 | 0.605 | 0.275783 |
| ultimate goal | 2 | 0.605 | 0.275078 |
| precious lineage dawn | 1 | 0.605 | 0.261610 |
| vast skill | 2 | 0.602 | 0.234572 |
| upayoga tantra | 1 | 0.602 | 0.271909 |
| indivisible yoga | 1 | 0.600 | 0.299229 |
| lord avalokitesvara | 2 | 0.600 | 0.041722 |
| vajra song | 2 | 0.599 | 0.243588 |
| perfection phase depend | 1 | 0.599 | 0.290008 |
| noble lord avalokitesvara | 1 | 0.598 | 0.048050 |
| live incalculably long | 1 | 0.597 | 0.165787 |
| lord padampa sangye | 1 | 0.596 | 0.024346 |
| frightening hell | 1 | 0.596 | 0.212485 |
| great translator rinchen | 1 | 0.595 | 0.061472 |
| profoundly secret true | 1 | 0.595 | 0.110304 |
| northern buddhafield | 1 | 0.595 | 0.292585 |
| great vehicle widely | 1 | 0.594 | 0.030590 |
| marvellous essence | 2 | 0.594 | 0.264030 |
| lita naropa | 2 | 0.594 | 0.119828 |
| single tibetan practitioner | 1 | 0.594 | 0.189241 |
| buddha protector amitayus | 1 | 0.590 | 0.011577 |
| lama yungton | 1 | 0.590 | 0.217372 |
| geshe khampa | 1 | 0.586 | 0.154917 |
| king golden crest | 1 | 0.585 | 0.052806 |
| vajra sprang | 1 | 0.583 | 0.260603 |
| great paqqita naropa | 1 | 0.583 | 0.028465 |
| false spiritual friend | 2 | 0.581 | 0.117021 |
| precious medicinal tree | 1 | 0.581 | 0.227835 |
| entire time swimming | 1 | 0.581 | 0.265051 |
| great siddha lingje | 1 | 0.580 | 0.053839 |
| king trisongdetsen | 1 | 0.579 | 0.101001 |
| king uparaja | 1 | 0.579 | 0.102363 |
| king gomadeviya | 1 | 0.579 | 0.102392 |
| king surabhibhadra | 2 | 0.578 | 0.042313 |
| kalpa delightful | 1 | 0.578 | 0.229062 |
| eager faith | 2 | 0.575 | 0.213939 |
| sadaprarudita cut open | 1 | 0.574 | 0.154654 |
| moon lamp sutra | 1 | 0.574 | 0.128304 |
| fully ripen | 1 | 0.574 | 0.255275 |
| mountain vajrapar | 1 | 0.573 | 0.234171 |
| omniscient primal wisdom | 1 | 0.572 | 0.164082 |
| black horse | 2 | 0.571 | 0.131989 |
| sublime path unerringly | 1 | 0.571 | 0.243875 |
| unsurpassable secret mantra | 1 | 0.571 | 0.049927 |
| precious lord guru | 2 | 0.571 | 0.005405 |
| master jetari | 1 | 0.570 | 0.116468 |
| master diparhkara | 1 | 0.570 | 0.120816 |
| surpass buddha sakyamuni | 1 | 0.569 | 0.013331 |
| guru sri | 1 | 0.569 | 0.110490 |
| perfect secluded place | 1 | 0.568 | 0.165102 |
| clear light spread | 1 | 0.567 | 0.289546 |
| western india | 1 | 0.564 | 0.153455 |
| black horse lama | 1 | 0.564 | 0.094746 |
| prodigious negative | 1 | 0.563 | 0.299641 |
| ludicrous negative | 1 | 0.563 | 0.299648 |
| unmentionably negative | 1 | 0.563 | 0.299807 |
| perfectly pure intention | 2 | 0.562 | 0.107534 |
| seventh bodhisattva level | 1 | 0.562 | 0.083209 |
| point lord maitreya | 1 | 0.561 | 0.038611 |
| single offensive word | 1 | 0.557 | 0.205055 |
| scavenger offering | 1 | 0.557 | 0.169007 |
| great primordial kingdom | 1 | 0.556 | 0.194338 |
| delicious food | 2 | 0.556 | 0.208989 |
| phoney lama | 1 | 0.555 | 0.124021 |
| profoundly secret | 1 | 0.555 | 0.180322 |
| exceptionally great | 2 | 0.554 | 0.047842 |
| lord mafijusri | 1 | 0.553 | 0.102317 |
| lotus crest | 1 | 0.552 | 0.213196 |
| human lifetime forever | 1 | 0.551 | 0.191047 |
| vajra guru mantra | 2 | 0.550 | 0.005212 |
| red mountain palace | 1 | 0.550 | 0.122869 |
| complete root downfall | 1 | 0.549 | 0.236927 |
| ati vehicle | 1 | 0.549 | 0.168458 |
| dark red | 2 | 0.549 | 0.224809 |
| great elapatra tree | 1 | 0.549 | 0.045068 |
| swift path | 2 | 0.549 | 0.154672 |
| perfectly dedicate merit | 2 | 0.549 | 0.072738 |
| bodhisattva sam | 1 | 0.548 | 0.073065 |
| reason guru yoga | 1 | 0.548 | 0.036073 |
| sutra pisaka | 1 | 0.548 | 0.128867 |
| collective good | 1 | 0.548 | 0.203101 |
| uninterrupted good | 1 | 0.548 | 0.203631 |
| ostentatious good | 1 | 0.548 | 0.203918 |
| adopt good | 1 | 0.548 | 0.203945 |
| absolute cho | 2 | 0.547 | 0.095191 |
| clear vision | 2 | 0.547 | 0.228068 |
| red blood lake | 1 | 0.546 | 0.174867 |
| past perfectly dedicated | 1 | 0.545 | 0.293462 |
| master jowo atisa | 1 | 0.545 | 0.012716 |
| black true mother | 2 | 0.545 | 0.025355 |
| perfectly dedicated merit | 1 | 0.544 | 0.287608 |
| omniscient jigme | 1 | 0.544 | 0.149522 |
| teaching yard | 1 | 0.540 | 0.229890 |
| outdoor teaching | 1 | 0.540 | 0.229891 |
| harma teaching | 1 | 0.540 | 0.230169 |
| finally eighty thousand | 1 | 0.539 | 0.256388 |
| noble master nagarjuna | 1 | 0.539 | 0.030195 |
| derive great benefit | 1 | 0.539 | 0.052231 |
| practise dharma authentically | 1 | 0.538 | 0.010741 |
| heating hell | 1 | 0.536 | 0.155978 |
| mila adamantine | 1 | 0.535 | 0.106288 |
| fritter life | 1 | 0.535 | 0.123644 |
| prolong life | 1 | 0.535 | 0.204374 |
| primordial state free | 1 | 0.534 | 0.264659 |
| hypocritical practice | 1 | 0.533 | 0.217113 |
| assiduous practice | 1 | 0.533 | 0.217920 |
| devotional practice | 1 | 0.533 | 0.218136 |
| practice predominate | 1 | 0.533 | 0.218150 |
| dharma king trisongdetsen | 1 | 0.533 | 0.002791 |
| demon tsang | 1 | 0.532 | 0.273180 |
| transcendent primal wisdom | 1 | 0.531 | 0.183568 |
| perfection subsequently | 1 | 0.531 | 0.257432 |
| transcendent discipline | 2 | 0.529 | 0.228563 |
| meritorious act | 2 | 0.529 | 0.245536 |
| suffer terribly | 1 | 0.528 | 0.234328 |
| postpone death | 1 | 0.528 | 0.244359 |
| yoga technique | 1 | 0.528 | 0.273758 |
| mind minutely | 1 | 0.527 | 0.194032 |
| mind indissolubly | 1 | 0.527 | 0.195828 |
| fortunate son | 2 | 0.527 | 0.176977 |
| geshe langri | 1 | 0.526 | 0.117975 |
| geshe chekawa | 1 | 0.526 | 0.150630 |
| excellent mountain | 2 | 0.526 | 0.116712 |
| great perfection subsequently | 1 | 0.526 | 0.035269 |
| noble katyayana | 1 | 0.525 | 0.255287 |
| wonderful teacher forever | 1 | 0.524 | 0.046127 |
| poison jetsun mila | 1 | 0.524 | 0.022368 |
| physically present | 2 | 0.524 | 0.267338 |
| vajra ogre | 1 | 0.524 | 0.200890 |
| extremely negative act | 2 | 0.523 | 0.094563 |
| mind workable | 2 | 0.523 | 0.093388 |
| superior transference | 2 | 0.523 | 0.295312 |
| feel great affection | 1 | 0.521 | 0.051629 |
| ultimate fruit | 2 | 0.521 | 0.192495 |
| great exuberant | 1 | 0.521 | 0.063287 |
| great gusto | 1 | 0.521 | 0.097563 |
| great inseparability | 1 | 0.521 | 0.097640 |
| great fervour | 1 | 0.521 | 0.097707 |
| great evenness | 1 | 0.521 | 0.097709 |
| great pal | 1 | 0.521 | 0.097717 |
| great equality | 1 | 0.521 | 0.097717 |
| false cho | 1 | 0.521 | 0.264748 |
| profound atiyoga teaching | 1 | 0.520 | 0.071309 |
| great courage giving | 1 | 0.520 | 0.058744 |
| king manicuda | 1 | 0.519 | 0.094313 |
| king mandhatri | 1 | 0.519 | 0.114522 |
| joyous kalpa | 1 | 0.519 | 0.154030 |
| great bodhisattva abbot | 2 | 0.518 | 0.002367 |
| jowo sakyamuni | 1 | 0.517 | 0.091442 |
| meet dharmodgata | 1 | 0.517 | 0.273718 |
| present perfectly dedicate | 1 | 0.517 | 0.268011 |
| great misfortune | 2 | 0.517 | 0.046876 |
| red hot | 2 | 0.517 | 0.180694 |
| distant past | 2 | 0.516 | 0.159418 |
| harsh speech | 2 | 0.516 | 0.272611 |
| compassion hurl | 1 | 0.515 | 0.240397 |
| arouse absolute bodhicitta | 1 | 0.514 | 0.207750 |
| extraordinary secret mantra | 1 | 0.514 | 0.031680 |
| karmic effect similar | 1 | 0.513 | 0.259337 |
| totally free | 2 | 0.513 | 0.258290 |
| false spiritual | 2 | 0.513 | 0.249504 |
| pure motivation | 2 | 0.512 | 0.241094 |
| slight positive action | 1 | 0.512 | 0.068336 |
| outer water element | 1 | 0.511 | 0.256622 |
| great pandita naropa | 1 | 0.510 | 0.023039 |
| metal ground | 2 | 0.510 | 0.283910 |
| guru padma | 1 | 0.510 | 0.084357 |
| bodhisattva samantabhadra | 2 | 0.509 | 0.017987 |
| feel great sadness | 1 | 0.509 | 0.049931 |
| practise dharma alongside | 1 | 0.508 | 0.010472 |
| true primal wisdom | 1 | 0.508 | 0.164813 |
| vajra speech enter | 1 | 0.508 | 0.112838 |
| buddha ratnasambhava | 1 | 0.507 | 0.021370 |
| buddha amoghasiddhi | 1 | 0.507 | 0.021370 |
| primordially buddha | 1 | 0.507 | 0.021426 |
| buddha vajraguhya | 1 | 0.507 | 0.021427 |
| extraordinary main path | 1 | 0.507 | 0.209798 |
| thought cease | 2 | 0.507 | 0.142236 |
| eighteen hell | 2 | 0.507 | 0.180350 |
| sangye heard | 1 | 0.507 | 0.259402 |
| great master tendzin | 1 | 0.506 | 0.010097 |
| intermediate state arise | 1 | 0.506 | 0.213172 |
| hollow vajra | 1 | 0.505 | 0.249086 |
| qualified teacher | 1 | 0.504 | 0.119415 |
| action consistent | 1 | 0.502 | 0.139301 |
| main subject | 2 | 0.502 | 0.239194 |
| completely sincere mind | 1 | 0.502 | 0.170695 |
| perfect vase | 2 | 0.502 | 0.163565 |
| perfect health | 2 | 0.502 | 0.187372 |
| single instant lead | 1 | 0.501 | 0.228715 |
| natural state support | 1 | 0.500 | 0.231526 |
| boundless love | 2 | 0.500 | 0.256638 |
| buddha infinite aspiration | 1 | 0.500 | 0.023248 |
| infinite number | 2 | 0.500 | 0.251201 |
| pandita naropa | 1 | 0.499 | 0.234817 |
| sublime sariputra | 1 | 0.497 | 0.251230 |
| body physically present | 1 | 0.497 | 0.178837 |
| unsurpassable secret | 1 | 0.496 | 0.169244 |
| real determination | 2 | 0.494 | 0.293558 |
| equal nature | 2 | 0.493 | 0.234388 |
| great indian master | 1 | 0.492 | 0.007730 |
| jewel chest | 1 | 0.492 | 0.073568 |
| double suffering | 1 | 0.492 | 0.252119 |
| ceaseless suffering | 1 | 0.492 | 0.252930 |
| incredible suffering | 1 | 0.492 | 0.252971 |
| firm faith | 2 | 0.492 | 0.185066 |
| pure conduct | 2 | 0.492 | 0.225493 |
| master dharmaraksita | 1 | 0.492 | 0.096001 |
| master tendzin | 1 | 0.492 | 0.105333 |
| actual meditation | 2 | 0.491 | 0.247799 |
| great scholar | 2 | 0.491 | 0.045103 |
| meet marpa | 1 | 0.491 | 0.177166 |
| genuine spiritual teacher | 1 | 0.490 | 0.068008 |
| ordinary human form | 2 | 0.490 | 0.033002 |
| great perfect vajradhara | 1 | 0.489 | 0.017509 |
| requisite good | 1 | 0.488 | 0.199296 |
| good ascetic | 1 | 0.488 | 0.199377 |
| natural great perfection | 2 | 0.488 | 0.008765 |
| dharma authentically | 1 | 0.486 | 0.027310 |
| purest dharma | 1 | 0.486 | 0.027312 |
| marry dharma | 1 | 0.486 | 0.027332 |
| complete enlightenment | 2 | 0.486 | 0.222347 |
| fourth jewel | 2 | 0.486 | 0.032217 |
| lotus light | 2 | 0.485 | 0.110740 |
| king virudhaka | 1 | 0.485 | 0.084566 |
| king ravati | 1 | 0.485 | 0.277805 |
| sangha fail | 1 | 0.485 | 0.256006 |
| starting point | 2 | 0.485 | 0.226954 |
| main practice train | 1 | 0.484 | 0.156751 |
| black hat | 1 | 0.484 | 0.228020 |
| dark black | 1 | 0.484 | 0.286862 |
| transcendent patience | 2 | 0.484 | 0.185907 |
| transcendent diligence | 2 | 0.484 | 0.185954 |
| secret mantra mandala | 1 | 0.484 | 0.023876 |
| bodhisattva abbot | 2 | 0.483 | 0.024797 |
| compassionate heart | 2 | 0.483 | 0.097905 |
| teaching sror | 1 | 0.481 | 0.155099 |
| dear body | 2 | 0.481 | 0.149336 |
| dumb person | 2 | 0.481 | 0.250584 |
| small pile | 2 | 0.481 | 0.274297 |
| red syllable | 2 | 0.480 | 0.206235 |
| venerable geshe | 1 | 0.479 | 0.140395 |
| conqueror sakyamuni | 1 | 0.478 | 0.072313 |
| gathering offering | 2 | 0.478 | 0.232208 |
| mother bird taking | 1 | 0.478 | 0.099149 |
| authentic vajra master | 1 | 0.477 | 0.025955 |
| vast attitude | 2 | 0.476 | 0.147463 |
| sincere faith | 2 | 0.475 | 0.178178 |
| profound truth | 2 | 0.475 | 0.257981 |
| compassionate root teacher | 1 | 0.475 | 0.030403 |
| renounce evil | 2 | 0.474 | 0.218282 |
| feel natural love | 1 | 0.474 | 0.150404 |
| negative karmic result | 1 | 0.473 | 0.136162 |
| noble spiritual friend | 1 | 0.472 | 0.097105 |
| merit great rejoicing | 1 | 0.472 | 0.031215 |
| sixteen thousand | 2 | 0.472 | 0.179160 |
| day elapatra | 1 | 0.471 | 0.227758 |
| human life complete | 2 | 0.471 | 0.018362 |
| achieve buddhahood | 1 | 0.470 | 0.122630 |
| karmic result | 2 | 0.470 | 0.238891 |
| negative imprint | 1 | 0.470 | 0.285715 |
| absolute bodhicitta present | 1 | 0.469 | 0.119196 |
| single tibetan | 1 | 0.469 | 0.099445 |
| long term | 2 | 0.469 | 0.156726 |
| vast ocean | 2 | 0.468 | 0.163522 |
| tathagata family | 1 | 0.468 | 0.130307 |
| true absolute bodhicitta | 1 | 0.467 | 0.105193 |
| vajra body enter | 1 | 0.465 | 0.055424 |
| perfect horse | 2 | 0.465 | 0.131310 |
| auspicious day | 2 | 0.464 | 0.128927 |
| central tibet | 2 | 0.464 | 0.050615 |
| supreme spiritual friend | 1 | 0.463 | 0.101641 |
| indian master | 1 | 0.463 | 0.081380 |
| long run | 2 | 0.463 | 0.156440 |
| glorious vajrasattva | 1 | 0.462 | 0.098087 |
| great howling | 1 | 0.462 | 0.057817 |
| great renown | 1 | 0.462 | 0.095063 |
| derive great | 1 | 0.462 | 0.095426 |
| great sincerity | 1 | 0.462 | 0.095588 |
| great paqc | 1 | 0.462 | 0.095701 |
| great paqqita | 1 | 0.462 | 0.095759 |
| ultimate cho | 1 | 0.462 | 0.129331 |
| pure vision | 2 | 0.461 | 0.180961 |
| experience immense suffering | 1 | 0.461 | 0.106921 |
| element mandala | 2 | 0.461 | 0.206440 |
| close friend | 2 | 0.461 | 0.268385 |
| powerful positive act | 1 | 0.461 | 0.112237 |
| atiyoga teaching | 2 | 0.460 | 0.101108 |
| perfectly complete | 2 | 0.459 | 0.178131 |
| white nectar | 2 | 0.458 | 0.241743 |
| precious word empowerment | 1 | 0.457 | 0.065036 |
| present buddha sakyamuni | 1 | 0.457 | 0.004603 |
| cruel suffering | 1 | 0.457 | 0.247102 |
| authentic refuge vow | 1 | 0.457 | 0.103957 |
| precious human life | 2 | 0.457 | 0.009863 |
| single good dream | 1 | 0.457 | 0.072068 |
| perfect vajradhara | 1 | 0.456 | 0.182876 |
| jowo river | 1 | 0.455 | 0.169468 |
| seventh bodhisattva | 1 | 0.455 | 0.086439 |
| work hard | 2 | 0.454 | 0.228964 |
| joyous realm | 1 | 0.454 | 0.149053 |
| transcendent concentration | 2 | 0.454 | 0.145871 |
| ordinary human simply | 1 | 0.454 | 0.094309 |
| pure buddhafield | 2 | 0.453 | 0.055665 |
| precious supreme path | 1 | 0.452 | 0.048083 |
| master padma | 1 | 0.451 | 0.078221 |
| glorious mountain | 1 | 0.450 | 0.192996 |
| black cho | 1 | 0.450 | 0.094712 |
| suddenly find | 2 | 0.449 | 0.187941 |
| ing negative effect | 1 | 0.449 | 0.071482 |
| great vehicle tradition | 1 | 0.449 | 0.013087 |
| negative thought run | 1 | 0.449 | 0.069455 |
| buddha vairocana | 1 | 0.448 | 0.019863 |
| bodhisattva dharmodgata teaching | 1 | 0.448 | 0.005203 |
| lamp sutra | 1 | 0.447 | 0.180738 |
| sacred place | 2 | 0.446 | 0.264623 |
| time swimming | 1 | 0.446 | 0.154879 |
| compassionate root | 1 | 0.446 | 0.260377 |
| negative mentality | 1 | 0.445 | 0.278561 |
| excellent human life | 1 | 0.444 | 0.039679 |
| precious golden | 1 | 0.444 | 0.250387 |
| perfect teacher venerable | 1 | 0.444 | 0.022253 |
| lord guru | 2 | 0.444 | 0.016389 |
| mother bird | 2 | 0.443 | 0.124625 |
| sublime nagarjuna | 1 | 0.443 | 0.161955 |
| perfect buddha sakyamuni | 1 | 0.443 | 0.003445 |
| utterly perfect buddha | 1 | 0.443 | 0.009613 |
| outer cho | 1 | 0.441 | 0.178601 |
| religious king | 1 | 0.441 | 0.143820 |
| favour life | 1 | 0.441 | 0.195845 |
| profound emptiness | 2 | 0.441 | 0.194142 |
| past sexual | 2 | 0.439 | 0.268509 |
| bodhisattva sadaprarudita | 2 | 0.437 | 0.013787 |
| practise real dharma | 2 | 0.437 | 0.002649 |
| siddha naropa | 1 | 0.436 | 0.146982 |
| infinite buddhafield | 1 | 0.436 | 0.167053 |
| central buddhafield | 1 | 0.436 | 0.168972 |
| lower left hand | 1 | 0.435 | 0.080392 |
| true dharma properly | 1 | 0.435 | 0.010843 |
| nirvana sutra | 1 | 0.435 | 0.174790 |
| lord padampa | 1 | 0.434 | 0.074217 |
| sadaprarudita cut | 1 | 0.434 | 0.181079 |
| suffering befall | 1 | 0.433 | 0.241572 |
| perfect spiritual friend | 1 | 0.431 | 0.065893 |
| period tibet | 1 | 0.431 | 0.131028 |
| protector nagarjuna | 1 | 0.431 | 0.138068 |
| terrible suffering | 2 | 0.431 | 0.207343 |
| time bodhisattva dharmodgata | 1 | 0.431 | 0.003742 |
| virtuous practice | 2 | 0.430 | 0.070781 |
| bring great benefit | 2 | 0.430 | 0.007020 |
| golden vajra | 1 | 0.430 | 0.167334 |
| sleep yoga | 1 | 0.430 | 0.200307 |
| secret tantric | 1 | 0.430 | 0.132361 |
| entire human life | 1 | 0.430 | 0.050601 |
| hot food | 2 | 0.430 | 0.148185 |
| live forever | 2 | 0.430 | 0.073091 |
| black true | 2 | 0.429 | 0.073318 |
| great ship | 2 | 0.428 | 0.042481 |
| single grain | 2 | 0.428 | 0.162991 |
| day chengawa | 1 | 0.428 | 0.151324 |
| dharma drift | 1 | 0.427 | 0.026742 |
| dharma alongside | 1 | 0.427 | 0.026809 |
| great smrtijnana | 1 | 0.427 | 0.050646 |
| great avalokitdvara | 1 | 0.427 | 0.054907 |
| great elapatra | 1 | 0.427 | 0.075323 |
| great relish | 1 | 0.427 | 0.093137 |
| great arrogance | 1 | 0.427 | 0.093590 |
| great affection | 1 | 0.427 | 0.093693 |
| present human world | 1 | 0.427 | 0.061471 |
| great compassion possess | 1 | 0.426 | 0.025116 |
| perfect dedication | 2 | 0.426 | 0.148472 |
| wrong attitude | 2 | 0.424 | 0.290989 |
| root text | 2 | 0.423 | 0.141998 |
| illusory body | 1 | 0.422 | 0.154969 |
| wrong direction | 2 | 0.422 | 0.156960 |
| supreme authentic dharma | 1 | 0.421 | 0.009519 |
| jewel garland | 1 | 0.419 | 0.065919 |
| nanda set | 1 | 0.419 | 0.214455 |
| horse lama | 1 | 0.418 | 0.222582 |
| guru mantra | 2 | 0.417 | 0.022474 |
| great remorse | 2 | 0.417 | 0.041497 |
| blue vajra | 1 | 0.417 | 0.181646 |
| sixteen vajra | 1 | 0.417 | 0.198377 |
| mountain palace | 1 | 0.417 | 0.195595 |
| endless suffering | 2 | 0.416 | 0.100144 |
| red light | 2 | 0.416 | 0.111302 |
| diligent practice | 1 | 0.415 | 0.204086 |
| omniscient dharma king | 1 | 0.414 | 0.001542 |
| complete buddhahood | 2 | 0.414 | 0.034160 |
| white hum | 1 | 0.414 | 0.282824 |
| buddha maitreya | 2 | 0.413 | 0.006589 |
| vajra guru | 2 | 0.413 | 0.020613 |
| immaculate wisdom | 1 | 0.413 | 0.238134 |
| indian king | 1 | 0.412 | 0.064130 |
| seventh day | 1 | 0.412 | 0.271895 |
| secret true teaching | 1 | 0.412 | 0.013934 |
| authentic realization | 2 | 0.411 | 0.158261 |
| degenerate time | 2 | 0.411 | 0.137647 |
| omniscient buddhahood | 1 | 0.411 | 0.051339 |
| mix negative | 1 | 0.410 | 0.273038 |
| dorje set | 1 | 0.409 | 0.158759 |
| virtuous thing | 1 | 0.409 | 0.267787 |
| perfect teacher vajrasattva | 1 | 0.409 | 0.007775 |
| blood lake | 1 | 0.408 | 0.270176 |
| completely pure | 2 | 0.407 | 0.151177 |
| sadaprarudita set | 1 | 0.405 | 0.173152 |
| venerable master | 1 | 0.404 | 0.091835 |
| single prostration | 2 | 0.404 | 0.116446 |
| ordinary worldly | 2 | 0.404 | 0.127745 |
| wisdom dakini | 1 | 0.404 | 0.234995 |
| genuine dharma | 2 | 0.403 | 0.012040 |
| completely perfect buddha | 1 | 0.403 | 0.007404 |
| great sadness | 1 | 0.403 | 0.091575 |
| embrace great | 1 | 0.403 | 0.091918 |
| great moving | 1 | 0.403 | 0.092064 |
| reason guru | 1 | 0.403 | 0.125223 |
| mila dorje | 1 | 0.402 | 0.040990 |
| king padma | 1 | 0.401 | 0.061679 |
| lack food | 2 | 0.399 | 0.111150 |
| great pandita | 2 | 0.399 | 0.040337 |
| dharma like ambrosia | 1 | 0.399 | 0.055487 |
| absolute wisdom | 2 | 0.398 | 0.103695 |
| present great kalpa | 1 | 0.398 | 0.011470 |
| risk life | 1 | 0.397 | 0.187815 |
| practise generosity | 2 | 0.397 | 0.118571 |
| mother sixteen | 1 | 0.396 | 0.291005 |
| personal practice | 1 | 0.396 | 0.199130 |
| attachment hatred | 1 | 0.395 | 0.168269 |
| vajra throne | 1 | 0.395 | 0.170843 |
| follow sakyamuni | 1 | 0.395 | 0.121570 |
| poison jetsun | 1 | 0.395 | 0.142493 |
| distinguish good | 1 | 0.395 | 0.181791 |
| relative buddhahood | 1 | 0.392 | 0.100107 |
| universal king | 1 | 0.391 | 0.115016 |
| good worldly life | 1 | 0.391 | 0.021128 |
| present work | 2 | 0.390 | 0.142132 |
| food drink | 2 | 0.390 | 0.072525 |
| buddha miraculously | 1 | 0.389 | 0.029500 |
| comfortable place | 1 | 0.389 | 0.284192 |
| humble place | 1 | 0.389 | 0.286034 |
| find fault | 2 | 0.388 | 0.138560 |
| refuge sincerely | 1 | 0.388 | 0.297705 |
| compassionate wisdom | 1 | 0.388 | 0.171226 |
| buddhist teaching | 1 | 0.387 | 0.097554 |
| master nagarjuna | 1 | 0.387 | 0.055766 |
| happiness comfort | 1 | 0.387 | 0.243439 |
| negative behaviour | 1 | 0.386 | 0.254136 |
| supreme tilopa | 1 | 0.385 | 0.134786 |
| great vairotsana | 1 | 0.384 | 0.047814 |
| great courage | 1 | 0.384 | 0.075752 |
| prince great | 1 | 0.384 | 0.075931 |
| great deal | 1 | 0.384 | 0.089707 |
| perfectly practise dharma | 1 | 0.382 | 0.004766 |
| master alive | 1 | 0.382 | 0.143665 |
| excellent kalpa | 1 | 0.381 | 0.157704 |
| extremely negative | 2 | 0.381 | 0.089908 |
| extraordinary secret | 1 | 0.381 | 0.114887 |
| immense compassion | 2 | 0.381 | 0.106360 |
| transference prayer | 2 | 0.380 | 0.104928 |
| single negative thought | 1 | 0.378 | 0.027656 |
| precious material | 1 | 0.378 | 0.228989 |
| master jowo | 1 | 0.378 | 0.050616 |
| vehicle tradition | 1 | 0.377 | 0.136818 |
| immeasurable compassion | 1 | 0.377 | 0.280598 |
| sky yoga | 1 | 0.377 | 0.138126 |
| practise virtue | 1 | 0.377 | 0.297642 |
| ultimate liberation | 1 | 0.376 | 0.243956 |
| negative connection | 1 | 0.376 | 0.249758 |
| pure meaning | 2 | 0.376 | 0.110915 |
| lord vajrasattva | 1 | 0.375 | 0.034594 |
| sacred wisdom | 1 | 0.375 | 0.285307 |
| red mountain | 1 | 0.375 | 0.192810 |
| ordinary tree | 2 | 0.374 | 0.085388 |
| golden place | 1 | 0.373 | 0.215358 |
| samsaric suffering | 1 | 0.373 | 0.220060 |
| teacher stand | 2 | 0.373 | 0.096422 |
| fortunate human | 1 | 0.373 | 0.208145 |
| bodhicitta equally | 1 | 0.372 | 0.285915 |
| sincere bodhicitta | 1 | 0.372 | 0.288515 |
| great importance | 2 | 0.371 | 0.037816 |
| central place | 2 | 0.371 | 0.091419 |
| single good thought | 1 | 0.370 | 0.019643 |
| sakya buddha | 1 | 0.370 | 0.015437 |
| buddha manjusri | 1 | 0.370 | 0.015752 |
| surpass buddha | 1 | 0.370 | 0.031489 |
| feast offering | 1 | 0.369 | 0.223781 |
| everyday life | 1 | 0.369 | 0.180273 |
| dear life | 1 | 0.369 | 0.180323 |
| strive day | 1 | 0.368 | 0.246546 |
| great vajradhara | 1 | 0.368 | 0.044560 |
| great longchenpa | 1 | 0.368 | 0.045256 |
| great rejoicing | 1 | 0.368 | 0.088622 |
| shearing time | 1 | 0.368 | 0.144730 |
| time lift | 1 | 0.368 | 0.145055 |
| king golden | 1 | 0.366 | 0.101299 |
| evil nature | 2 | 0.366 | 0.219859 |
| seek refuge | 1 | 0.366 | 0.247194 |
| animal today | 1 | 0.365 | 0.277699 |
| happiness today | 1 | 0.365 | 0.289740 |
| great close | 2 | 0.365 | 0.030077 |
| important point | 2 | 0.365 | 0.237432 |
| naropa set | 1 | 0.365 | 0.128204 |
| merit totally | 1 | 0.365 | 0.277821 |
| noble lord | 1 | 0.363 | 0.083162 |
| control body | 1 | 0.363 | 0.276101 |
| summit teaching | 1 | 0.363 | 0.197750 |
| obtain human | 1 | 0.362 | 0.186991 |
| supreme joy | 1 | 0.362 | 0.242617 |
| omniscient state | 1 | 0.362 | 0.141793 |
| good doctor | 1 | 0.360 | 0.160539 |
| ordinary transference | 2 | 0.360 | 0.101044 |
| material offering | 2 | 0.359 | 0.154136 |
| mantra recitation | 1 | 0.359 | 0.176714 |
| ordinary giving | 2 | 0.358 | 0.104218 |
| head call | 1 | 0.358 | 0.118985 |
| union wisdom | 1 | 0.358 | 0.240449 |
| sublime son | 1 | 0.358 | 0.277577 |
| constantly long | 1 | 0.357 | 0.291680 |
| natural death | 2 | 0.357 | 0.062836 |
| false path | 1 | 0.357 | 0.257097 |
| practise real | 2 | 0.356 | 0.096002 |
| immense suffering | 2 | 0.356 | 0.081891 |
| sublime lord | 1 | 0.356 | 0.084713 |
| mantra tradition | 1 | 0.356 | 0.132680 |
| practise true dharma | 1 | 0.355 | 0.003397 |
| effect utterly | 1 | 0.355 | 0.240977 |
| yoga tantra | 1 | 0.355 | 0.090055 |
| great indian | 1 | 0.355 | 0.041329 |
| great maudgalyayana | 1 | 0.355 | 0.044663 |
| great stupa | 1 | 0.355 | 0.075439 |
| great marvellous | 1 | 0.355 | 0.075614 |
| great primordial | 1 | 0.355 | 0.087022 |
| vajra recitation | 1 | 0.355 | 0.160408 |
| body physically | 1 | 0.355 | 0.272590 |
| buddha vajradhara | 1 | 0.354 | 0.014852 |
| perfect lake | 1 | 0.353 | 0.170480 |
| excellent human | 1 | 0.353 | 0.204295 |
| cultivate bodhicitta | 1 | 0.353 | 0.270999 |
| entire kalpa | 1 | 0.353 | 0.196136 |
| teacher sakyamuni | 2 | 0.353 | 0.033607 |
| impure offering | 1 | 0.352 | 0.214179 |
| heart centre | 1 | 0.352 | 0.295151 |
| commit negative | 1 | 0.351 | 0.210478 |
| good meal | 1 | 0.351 | 0.166955 |
| sublime essence | 1 | 0.351 | 0.253757 |
| vajrayana path | 1 | 0.350 | 0.091027 |
| poor thing | 1 | 0.349 | 0.266663 |
| wisdom kaya | 1 | 0.349 | 0.260794 |
| precious mountain | 1 | 0.348 | 0.117988 |
| life slip | 1 | 0.347 | 0.171104 |
| red blood | 1 | 0.347 | 0.282897 |
| lack wealth | 1 | 0.347 | 0.288143 |
| mind carefully | 2 | 0.346 | 0.066705 |
| black man | 1 | 0.346 | 0.186610 |
| boundless merit | 1 | 0.346 | 0.260777 |
| generation perfection | 1 | 0.345 | 0.022451 |
| precious human | 2 | 0.345 | 0.052242 |
| long iron | 1 | 0.345 | 0.267871 |
| great lake | 2 | 0.345 | 0.041871 |
| true tradition | 1 | 0.344 | 0.241609 |
| intense faith | 1 | 0.344 | 0.299979 |
| find tilopa | 1 | 0.344 | 0.115606 |
| sublime root | 1 | 0.343 | 0.220318 |
| mila joy | 1 | 0.343 | 0.063560 |
| boundless compassion | 1 | 0.343 | 0.253347 |
| thousand iron | 1 | 0.342 | 0.298834 |
| head visualize | 2 | 0.342 | 0.198799 |
| time lord buddha | 1 | 0.342 | 0.000773 |
| primordial buddha | 1 | 0.341 | 0.028239 |
| precious wheel | 1 | 0.341 | 0.125978 |
| teacher nagarjuna | 2 | 0.341 | 0.017267 |
| complete root | 1 | 0.341 | 0.251875 |
| human flesh | 2 | 0.340 | 0.086284 |
| faith fully | 1 | 0.340 | 0.293849 |
| find happiness | 2 | 0.340 | 0.092157 |
| life force | 2 | 0.339 | 0.065887 |
| mind slip | 1 | 0.339 | 0.163620 |
| waste time | 1 | 0.339 | 0.138828 |
| powerful king | 2 | 0.339 | 0.077466 |
| state carefully | 1 | 0.339 | 0.293341 |
| sublime method | 1 | 0.338 | 0.257704 |
| human lifetime | 1 | 0.338 | 0.272854 |
| samsara fall | 1 | 0.338 | 0.067140 |
| apply bodhicitta | 1 | 0.337 | 0.281897 |
| feel love | 2 | 0.337 | 0.094531 |
| perform positive | 1 | 0.337 | 0.274683 |
| great kindness | 2 | 0.336 | 0.033884 |
| suddenly end | 1 | 0.336 | 0.282646 |
| true mother | 2 | 0.335 | 0.063851 |
| good advice | 1 | 0.335 | 0.142274 |
| clear water | 1 | 0.335 | 0.216139 |
| kind lack | 1 | 0.335 | 0.266852 |
| long training | 1 | 0.335 | 0.242629 |
| noble spiritual | 1 | 0.334 | 0.228477 |
| bird taking | 1 | 0.334 | 0.267607 |
| inexhaustible dharma | 1 | 0.333 | 0.021440 |
| great universal | 1 | 0.333 | 0.072883 |
| inconceivable power | 1 | 0.333 | 0.289321 |
| human speech | 2 | 0.333 | 0.081794 |
| compassion possess | 1 | 0.332 | 0.256849 |
| profound essence | 1 | 0.332 | 0.295352 |
| ordinary form | 2 | 0.332 | 0.086240 |
| important thing | 2 | 0.331 | 0.087108 |
| powerful demon | 1 | 0.331 | 0.272499 |
| desire buddhahood | 1 | 0.330 | 0.066509 |
| bring harm | 2 | 0.330 | 0.178631 |
| powerful secret | 1 | 0.330 | 0.092064 |
| precious supreme | 1 | 0.329 | 0.160719 |
| refuge constantly | 1 | 0.329 | 0.244930 |
| practise cho | 1 | 0.329 | 0.080376 |
| wisdom enter | 1 | 0.329 | 0.239650 |
| single night | 1 | 0.328 | 0.292643 |
| omniscient dharma | 2 | 0.328 | 0.005293 |
| present perfectly | 1 | 0.328 | 0.282812 |
| precious lineage | 1 | 0.327 | 0.177954 |
| supreme path | 2 | 0.327 | 0.067048 |
| sutra tantra | 1 | 0.327 | 0.067338 |
| attain accomplishment | 1 | 0.327 | 0.239367 |
| worldly point | 1 | 0.327 | 0.297096 |
| prajnaparamita teacher | 1 | 0.326 | 0.047035 |
| animal birth | 1 | 0.325 | 0.280518 |
| immense faith | 1 | 0.325 | 0.276851 |
| feel happy | 1 | 0.325 | 0.295129 |
| authentic vajra | 1 | 0.325 | 0.135243 |
| entire human | 1 | 0.325 | 0.256598 |
| authentic view | 1 | 0.324 | 0.296696 |
| case death | 1 | 0.323 | 0.160573 |
| precious jetsun | 1 | 0.322 | 0.057822 |
| secret empowerment | 1 | 0.322 | 0.094305 |
| light empowerment | 1 | 0.322 | 0.268264 |
| strong negative | 1 | 0.321 | 0.212283 |
| entire world | 1 | 0.321 | 0.268208 |
| sincere practice | 1 | 0.321 | 0.174187 |
| offer flesh | 1 | 0.321 | 0.284917 |
| wonderful teaching | 1 | 0.321 | 0.130447 |
| water element | 1 | 0.321 | 0.274082 |
| outer water | 1 | 0.321 | 0.275384 |
| single dharma practice | 1 | 0.321 | 0.001979 |
| noble master | 1 | 0.321 | 0.083129 |
| head dissolve | 1 | 0.320 | 0.283487 |
| preta realm | 2 | 0.320 | 0.067806 |
| buddha samantabhadra | 1 | 0.320 | 0.012234 |
| mantra mandala | 1 | 0.319 | 0.134184 |
| death suddenly | 1 | 0.319 | 0.160986 |
| intense compassion | 1 | 0.318 | 0.229528 |
| great guide | 2 | 0.317 | 0.063066 |
| small good | 2 | 0.317 | 0.055294 |
| bodhisattva tradition | 1 | 0.317 | 0.047022 |
| feel hatred | 1 | 0.317 | 0.282959 |
| rich man | 1 | 0.317 | 0.193809 |
| hand high | 1 | 0.317 | 0.232871 |
| extraordinary bodhicitta | 1 | 0.317 | 0.213225 |
| good listening | 1 | 0.316 | 0.141400 |
| good tea | 1 | 0.316 | 0.148742 |
| vast wealth | 1 | 0.316 | 0.200812 |
| great mindfulness | 1 | 0.316 | 0.080922 |
| holy teacher | 1 | 0.316 | 0.101159 |
| lack faith | 1 | 0.316 | 0.220812 |
| past karma | 1 | 0.315 | 0.213657 |
| supreme spiritual | 1 | 0.315 | 0.238331 |
| secret essence | 1 | 0.315 | 0.077611 |
| virtuous action | 1 | 0.315 | 0.092587 |
| action slip | 1 | 0.315 | 0.117431 |
| mind totally | 1 | 0.315 | 0.156864 |
| sincere mind | 1 | 0.315 | 0.156925 |
| powerful evil | 1 | 0.314 | 0.275937 |
| place arouse | 1 | 0.314 | 0.194010 |
| great care | 2 | 0.314 | 0.031160 |
| simply free | 1 | 0.313 | 0.292850 |
| state support | 1 | 0.311 | 0.262569 |
| medicine buddha | 1 | 0.311 | 0.023285 |
| huge offering | 1 | 0.310 | 0.187187 |
| feel attachment | 1 | 0.310 | 0.271123 |
| immense bodhicitta | 1 | 0.309 | 0.226675 |
| central head | 1 | 0.309 | 0.246165 |
| heart doctrine | 1 | 0.309 | 0.180439 |
| combine dharma | 1 | 0.309 | 0.024067 |
| great abbot | 1 | 0.309 | 0.050352 |
| time immeasurable | 1 | 0.308 | 0.132537 |
| vajra essence | 1 | 0.308 | 0.105857 |
| mind awareness | 1 | 0.308 | 0.154175 |
| ultimate refuge | 1 | 0.307 | 0.135824 |
| bodhicitta training | 1 | 0.306 | 0.206592 |
| extraordinary compassion | 1 | 0.306 | 0.200233 |
| practise meditation | 2 | 0.306 | 0.070445 |
| complete instruction | 1 | 0.306 | 0.225699 |
| feel natural | 1 | 0.305 | 0.246675 |
| develop positive | 1 | 0.304 | 0.247188 |
| real benefit | 1 | 0.304 | 0.255613 |
| accumulate negative | 1 | 0.303 | 0.183311 |
| negative mental | 1 | 0.303 | 0.198719 |
| refuge prayer | 2 | 0.303 | 0.056083 |
| state arise | 1 | 0.303 | 0.205078 |
| supreme master | 1 | 0.302 | 0.086275 |
| supreme happiness | 1 | 0.302 | 0.217112 |
| great mistake | 1 | 0.302 | 0.077934 |
| great skull | 1 | 0.302 | 0.078398 |
| immense merit | 1 | 0.302 | 0.218752 |
| superior mind | 1 | 0.301 | 0.151587 |
| past existence | 1 | 0.301 | 0.219691 |
| short path | 1 | 0.301 | 0.209489 |
| feel pain | 1 | 0.301 | 0.254127 |
| entire refuge | 1 | 0.300 | 0.215291 |
| point lord | 1 | 0.299 | 0.074311 |
| holy dharma | 1 | 0.299 | 0.023456 |
| dharma language | 1 | 0.299 | 0.023513 |
| completely perfect | 1 | 0.299 | 0.233124 |
| practice like compassion | 1 | 0.298 | 0.273786 |
| wish harm | 1 | 0.298 | 0.078265 |
| entire time | 2 | 0.297 | 0.049688 |
| spend day | 1 | 0.297 | 0.195107 |
| refuge practice | 5 | 0.297 | 0.010514 |
| bear death | 1 | 0.297 | 0.148091 |
| mental offering | 1 | 0.297 | 0.178673 |
| great treasure | 1 | 0.296 | 0.070386 |
| powerful positive | 1 | 0.296 | 0.220623 |
| life complete | 2 | 0.294 | 0.048064 |
| great dharma king | 1 | 0.293 | 0.000345 |
| father mother | 1 | 0.293 | 0.143178 |
| main refuge | 1 | 0.292 | 0.204961 |
| relative good | 1 | 0.292 | 0.141855 |
| good dream | 1 | 0.292 | 0.142425 |
| human world | 2 | 0.292 | 0.057459 |
| past life | 5 | 0.292 | 0.005028 |
| teacher skilfully | 1 | 0.292 | 0.096452 |
| recognize suffering | 1 | 0.291 | 0.171987 |
| mental suffering | 1 | 0.291 | 0.173645 |
| find freedom | 1 | 0.291 | 0.171594 |
| pure past | 2 | 0.290 | 0.061601 |
| compassionate action | 1 | 0.290 | 0.069254 |
| innumerable hell | 1 | 0.290 | 0.117068 |
| develop faith | 1 | 0.290 | 0.226984 |
| hell realm | 3 | 0.289 | 0.022999 |
| offer water | 1 | 0.289 | 0.215821 |
| dharmodgata teaching | 1 | 0.289 | 0.056198 |
| great teacher | 11 | 0.289 | 0.001423 |
| sambhogakaya buddha | 1 | 0.288 | 0.025546 |
| bodhicitta arise | 1 | 0.288 | 0.170677 |
| life renounce | 1 | 0.288 | 0.190863 |
| body enter | 1 | 0.288 | 0.218399 |
| powerful person | 2 | 0.288 | 0.236129 |
| vajra speech | 1 | 0.287 | 0.105784 |
| negative thought | 4 | 0.287 | 0.032067 |
| approach practice | 1 | 0.287 | 0.146146 |
| true path | 2 | 0.287 | 0.055065 |
| natural great | 2 | 0.286 | 0.026054 |
| outer refuge | 1 | 0.286 | 0.187980 |
| future good | 2 | 0.286 | 0.046898 |
| human simply | 1 | 0.286 | 0.205510 |
| king subject | 1 | 0.285 | 0.278362 |
| strong mind | 1 | 0.285 | 0.141955 |
| wonderful teacher | 1 | 0.285 | 0.070384 |
| teacher explain | 1 | 0.285 | 0.095250 |
| great omniscient | 1 | 0.284 | 0.036308 |
| undergo great | 1 | 0.284 | 0.073140 |
| great confidence | 1 | 0.284 | 0.074129 |
| great guru | 2 | 0.284 | 0.008508 |
| secret true | 1 | 0.284 | 0.066746 |
| great love | 3 | 0.284 | 0.013816 |
| good karma | 1 | 0.284 | 0.125926 |
| birth death | 1 | 0.283 | 0.217018 |
| thousand mandala | 1 | 0.283 | 0.065342 |
| complete faith | 1 | 0.283 | 0.195434 |
| dharma practice | 11 | 0.282 | 0.000553 |
| main path | 1 | 0.282 | 0.189276 |
| great pain | 2 | 0.282 | 0.026716 |
| thousand bad | 1 | 0.281 | 0.157608 |
| material body | 1 | 0.281 | 0.193564 |
| death finally | 1 | 0.281 | 0.127977 |
| infinite merit | 1 | 0.281 | 0.182512 |
| realization free | 1 | 0.281 | 0.221886 |
| dharma practitioner | 2 | 0.281 | 0.008435 |
| moment mila | 1 | 0.280 | 0.056949 |
| great difficulty | 1 | 0.279 | 0.074633 |
| human rebirth | 1 | 0.279 | 0.180242 |
| perfectly practise | 1 | 0.278 | 0.172898 |
| teacher venerable | 1 | 0.278 | 0.056140 |
| intense practice | 1 | 0.278 | 0.149813 |
| vajra body | 2 | 0.277 | 0.029676 |
| positive effect | 2 | 0.277 | 0.052706 |
| ordinary life | 3 | 0.276 | 0.022004 |
| practise concentration | 1 | 0.276 | 0.181911 |
| entire body | 1 | 0.275 | 0.203289 |
| body dissolve | 1 | 0.275 | 0.204822 |
| great king | 5 | 0.275 | 0.004218 |
| great yogi | 1 | 0.274 | 0.066027 |
| time sakyamuni | 1 | 0.274 | 0.043592 |
| heart sutra | 1 | 0.274 | 0.071525 |
| heart essence | 1 | 0.274 | 0.085173 |
| supreme wisdom | 1 | 0.273 | 0.149396 |
| wisdom empowerment | 1 | 0.273 | 0.176743 |
| heart blood | 1 | 0.272 | 0.178375 |
| physical action | 1 | 0.271 | 0.105722 |
| single lama | 1 | 0.271 | 0.118615 |
| present wealth | 1 | 0.270 | 0.204368 |
| present form | 1 | 0.270 | 0.211900 |
| evil man | 1 | 0.270 | 0.245932 |
| good age | 1 | 0.269 | 0.129400 |
| past perfectly | 1 | 0.269 | 0.164276 |
| authentic refuge | 1 | 0.268 | 0.179086 |
| good food | 3 | 0.267 | 0.029715 |
| noble path | 1 | 0.267 | 0.129001 |
| teacher forever | 1 | 0.267 | 0.053279 |
| lower left | 1 | 0.266 | 0.191658 |
| disciple left | 1 | 0.265 | 0.186790 |
| happiness free | 1 | 0.265 | 0.193224 |
| spiritual instruction | 1 | 0.265 | 0.178881 |
| action family | 2 | 0.264 | 0.022048 |
| true happiness | 1 | 0.264 | 0.176005 |
| god demon | 1 | 0.263 | 0.185706 |
| develop compassion | 1 | 0.263 | 0.175997 |
| single prayer | 1 | 0.263 | 0.157130 |
| practice train | 1 | 0.262 | 0.142057 |
| refuge simply | 1 | 0.262 | 0.173563 |
| hell suffer | 1 | 0.261 | 0.096612 |
| end result | 1 | 0.261 | 0.187828 |
| dharma understanding | 1 | 0.261 | 0.021587 |
| sacred dharma | 1 | 0.261 | 0.021853 |
| vast path | 1 | 0.261 | 0.119987 |
| positive thought | 2 | 0.260 | 0.097438 |
| god realm | 2 | 0.260 | 0.087288 |
| short life | 1 | 0.260 | 0.132854 |
| avoid negative | 1 | 0.260 | 0.092900 |
| word empowerment | 1 | 0.259 | 0.177474 |
| ordinary man | 1 | 0.258 | 0.205048 |
| great ray | 1 | 0.257 | 0.068352 |
| absolute teaching | 1 | 0.256 | 0.131739 |
| great benefit | 3 | 0.255 | 0.011212 |
| mind enter | 1 | 0.255 | 0.129431 |
| ordinary body | 2 | 0.255 | 0.051402 |
| buddha protector | 2 | 0.255 | 0.012447 |
| pure water | 1 | 0.254 | 0.177540 |
| head lama | 1 | 0.254 | 0.108132 |
| single form | 1 | 0.253 | 0.178931 |
| day long | 2 | 0.252 | 0.081623 |
| perfect spiritual | 1 | 0.252 | 0.158785 |
| true benefit | 1 | 0.251 | 0.161415 |
| action properly | 1 | 0.251 | 0.099590 |
| entire life | 1 | 0.250 | 0.126415 |
| perfect view | 1 | 0.250 | 0.156794 |
| spiritual practice | 2 | 0.250 | 0.041164 |
| single point | 1 | 0.250 | 0.173896 |
| true teaching | 2 | 0.249 | 0.079800 |
| practice patience | 1 | 0.249 | 0.134756 |
| path empowerment | 1 | 0.249 | 0.158258 |
| mind training | 1 | 0.249 | 0.115722 |
| excellent teacher | 1 | 0.248 | 0.062082 |
| present human | 1 | 0.248 | 0.154632 |
| perfect kalpa | 1 | 0.247 | 0.090848 |
| good worldly | 1 | 0.246 | 0.109074 |
| single year | 1 | 0.245 | 0.151512 |
| sublime dharma | 2 | 0.245 | 0.006231 |
| great demon | 2 | 0.245 | 0.038654 |
| future buddha | 2 | 0.244 | 0.015703 |
| great lama | 2 | 0.244 | 0.026803 |
| buddha immediately | 1 | 0.243 | 0.022103 |
| numerous great | 1 | 0.243 | 0.063319 |
| great energy | 1 | 0.243 | 0.073362 |
| single good | 2 | 0.243 | 0.033963 |
| human body | 2 | 0.242 | 0.089727 |
| open mind | 1 | 0.242 | 0.104312 |
| bring happiness | 1 | 0.242 | 0.160514 |
| precious word | 1 | 0.242 | 0.092546 |
| act positive | 1 | 0.241 | 0.154729 |
| moment bring | 1 | 0.240 | 0.158068 |
| perfect happiness | 1 | 0.238 | 0.145480 |
| vajrasattva practice | 1 | 0.237 | 0.036768 |
| pure dharma | 3 | 0.237 | 0.003690 |
| present state | 1 | 0.237 | 0.158071 |
| wrong food | 1 | 0.237 | 0.155483 |
| feel good | 2 | 0.236 | 0.033363 |
| wisdom free | 1 | 0.236 | 0.133778 |
| extraordinary teacher | 1 | 0.236 | 0.074524 |
| mind free | 2 | 0.236 | 0.075205 |
| study dharma | 1 | 0.235 | 0.020511 |
| state free | 1 | 0.235 | 0.155770 |
| ordinary god | 1 | 0.235 | 0.131814 |
| good thought | 3 | 0.234 | 0.015436 |
| harmful past | 1 | 0.234 | 0.148194 |
| bodhicitta practice | 3 | 0.233 | 0.026465 |
| great tilopa | 1 | 0.233 | 0.023891 |
| great middle | 1 | 0.233 | 0.052161 |
| find food | 1 | 0.232 | 0.150648 |
| refuge vow | 1 | 0.231 | 0.132348 |
| bodhicitta vow | 1 | 0.231 | 0.133321 |
| short time | 1 | 0.230 | 0.104311 |
| thousand water | 1 | 0.230 | 0.044464 |
| tirthika teacher | 1 | 0.229 | 0.078525 |
| word vajra | 1 | 0.228 | 0.064552 |
| time training | 1 | 0.227 | 0.095055 |
| profound dharma | 2 | 0.225 | 0.007031 |
| bodhicitta meditation | 1 | 0.224 | 0.136156 |
| practise true | 1 | 0.224 | 0.077972 |
| authentic teaching | 1 | 0.223 | 0.118401 |
| practice perfectly | 1 | 0.223 | 0.104697 |
| bodhicitta present | 1 | 0.223 | 0.132422 |
| great outer | 1 | 0.222 | 0.055350 |
| jewel free | 1 | 0.222 | 0.039146 |
| bodhicitta free | 1 | 0.220 | 0.130537 |
| great hard | 1 | 0.220 | 0.057804 |
| true bodhicitta | 1 | 0.219 | 0.119463 |
| good bad | 1 | 0.219 | 0.024096 |
| harmful negative | 1 | 0.218 | 0.125698 |
| mind completely | 1 | 0.216 | 0.106141 |
| great accumulation | 1 | 0.215 | 0.056838 |
| good suffer | 1 | 0.213 | 0.093062 |
| vast mind | 1 | 0.212 | 0.075050 |
| buddha infinite | 1 | 0.211 | 0.018279 |
| rich person | 1 | 0.211 | 0.273206 |
| pure path | 1 | 0.210 | 0.115301 |
| perfect faith | 1 | 0.209 | 0.118889 |
| ordinary death | 1 | 0.209 | 0.078784 |
| feel great | 2 | 0.208 | 0.016996 |
| pure realm | 1 | 0.207 | 0.110366 |
| great wheel | 1 | 0.206 | 0.035031 |
| bring great | 2 | 0.205 | 0.016784 |
| great desire | 1 | 0.204 | 0.046838 |
| present day | 1 | 0.203 | 0.113566 |
| entire dharma | 1 | 0.202 | 0.017868 |
| animal realm | 1 | 0.202 | 0.101344 |
| great perfect | 2 | 0.201 | 0.015369 |
| great bodhisattva | 2 | 0.200 | 0.004088 |
| good nature | 1 | 0.199 | 0.081182 |
| profound practice | 1 | 0.199 | 0.102917 |
| action avoid | 1 | 0.199 | 0.277733 |
| mind turn | 1 | 0.198 | 0.134760 |
| future life | 1 | 0.197 | 0.009851 |
| experience suffering | 1 | 0.197 | 0.103889 |
| great fault | 1 | 0.196 | 0.051370 |
| noble teacher | 1 | 0.195 | 0.050977 |
| buddha family | 1 | 0.195 | 0.010651 |
| past positive | 1 | 0.194 | 0.103852 |
| life death | 2 | 0.192 | 0.036755 |
| great tree | 1 | 0.192 | 0.038472 |
| great faith | 2 | 0.192 | 0.015102 |
| practice transference | 1 | 0.191 | 0.093972 |
| transference practice | 1 | 0.191 | 0.093972 |
| live human | 1 | 0.191 | 0.094645 |
| teacher face | 1 | 0.191 | 0.066064 |
| good spiritual | 1 | 0.190 | 0.077522 |
| important practice | 1 | 0.190 | 0.095416 |
| time difficult | 1 | 0.188 | 0.083142 |
| practise taking | 1 | 0.187 | 0.096240 |
| single day | 1 | 0.187 | 0.097123 |
| single negative | 1 | 0.185 | 0.094831 |
| present teaching | 1 | 0.179 | 0.088118 |
| hell live | 1 | 0.177 | 0.051473 |
| love life | 1 | 0.177 | 0.082334 |
| time lord | 1 | 0.176 | 0.024621 |
| great liberation | 1 | 0.176 | 0.042443 |
| great effort | 1 | 0.173 | 0.044377 |
| present practice | 1 | 0.172 | 0.083979 |
| speech mind | 1 | 0.172 | 0.016056 |
| great secret | 1 | 0.170 | 0.014869 |
| master teaching | 1 | 0.169 | 0.033925 |
| perfect body | 1 | 0.169 | 0.093859 |
| body perfect | 1 | 0.169 | 0.093859 |
| bring suffering | 1 | 0.164 | 0.081208 |
| single teaching | 1 | 0.162 | 0.075609 |
| pure mind | 1 | 0.162 | 0.072232 |
| evil mind | 1 | 0.160 | 0.074270 |
| present great | 1 | 0.159 | 0.040051 |
| action good | 3 | 0.159 | 0.022000 |
| food offering | 1 | 0.157 | 0.075100 |
| great evil | 1 | 0.155 | 0.039051 |
| great wealth | 1 | 0.152 | 0.037623 |
| single person | 1 | 0.152 | 0.155878 |
| teacher spiritual | 1 | 0.146 | 0.103580 |
| present buddha | 1 | 0.146 | 0.013387 |
| present time | 1 | 0.143 | 0.063020 |
| precious dharma | 1 | 0.143 | 0.008199 |
| giving dharma | 1 | 0.143 | 0.053867 |
| true buddha | 1 | 0.142 | 0.012203 |
| pure buddha | 1 | 0.142 | 0.012723 |
| true teacher | 1 | 0.139 | 0.043964 |
| practise good | 1 | 0.137 | 0.051520 |
| perfect mind | 1 | 0.136 | 0.058041 |
| dharma teaching | 3 | 0.133 | 0.002600 |
| day day | 1 | 0.130 | 0.157974 |
| past good | 1 | 0.127 | 0.049205 |
| single teacher | 1 | 0.125 | 0.041728 |
| dharma free | 1 | 0.122 | 0.053461 |
| great power | 1 | 0.122 | 0.030420 |
| great wisdom | 1 | 0.121 | 0.026204 |
| action positive | 1 | 0.117 | 0.045133 |
| teacher buddha | 3 | 0.116 | 0.050223 |
| suffering negative | 1 | 0.114 | 0.280983 |
| time bodhisattva | 1 | 0.113 | 0.012644 |
| single dharma | 1 | 0.108 | 0.010094 |
| dharma give | 1 | 0.101 | 0.053673 |
| merit great | 1 | 0.098 | 0.024874 |
| practice take | 1 | 0.097 | 0.291391 |
| perfect dharma | 1 | 0.096 | 0.008996 |
| body life | 1 | 0.094 | 0.263008 |
| offering practice | 1 | 0.090 | 0.243516 |
| life good | 1 | 0.082 | 0.209081 |
| action take | 1 | 0.066 | 0.215644 |
| time great | 1 | 0.026 | 0.012830 |
| great dharma | 1 | 0.007 | 0.002466 |
| buddha dharma | 1 | -0.006 | 0.000845 |
| ordinary people | 0 | - | 0.007655 |
| great kalpas | 0 | - | 0.023520 |
| ordinary worldly people | 0 | - | 0.032371 |
| thousand people | 0 | - | 0.040179 |
| numerous great sravakas | 0 | - | 0.045308 |
| great sravakas | 0 | - | 0.045938 |
| dharma people | 0 | - | 0.050623 |
| supreme teachers | 0 | - | 0.052846 |
| important people | 0 | - | 0.057900 |
| great lotus like | 0 | - | 0.057972 |
| bodhisattvas dissolve | 0 | - | 0.061838 |
| sick people | 0 | - | 0.063113 |
| thousand samayas | 0 | - | 0.063758 |
| jewels bless | 0 | - | 0.064589 |
| people practise | 0 | - | 0.065780 |
| wish granting | 0 | - | 0.067448 |
| jewels spread | 0 | - | 0.067916 |
| dark kalpas | 0 | - | 0.068792 |
| worldly people | 0 | - | 0.070703 |
| eighty thousand people | 0 | - | 0.072490 |
| oddiyana points | 0 | - | 0.081467 |
| tsa tsa | 0 | - | 0.082258 |
| kadampa masters | 0 | - | 0.082533 |
| people follow | 0 | - | 0.085534 |
| innumerable kalpas | 0 | - | 0.087293 |
| great evil doer | 0 | - | 0.090336 |
| bodhisattvas undertake | 0 | - | 0.090596 |
| jewels render | 0 | - | 0.090801 |
| tantric samayas | 0 | - | 0.093883 |
| people die | 0 | - | 0.096428 |
| order great | 0 | - | 0.097701 |
| people die suddenly | 0 | - | 0.097838 |
| mantrayana tantras | 0 | - | 0.100258 |
| people present | 0 | - | 0.101693 |
| mila thopa | 0 | - | 0.103700 |
| secret tantric samayas | 0 | - | 0.104151 |
| brahma heavens | 0 | - | 0.110468 |
| buddhas body | 0 | - | 0.116993 |
| local people | 0 | - | 0.126178 |
| powerful people | 0 | - | 0.128025 |
| pronged vajra | 0 | - | 0.130217 |
| vajra core teaching | 0 | - | 0.130352 |
| excellent people | 0 | - | 0.132404 |
| mahayana sutras | 0 | - | 0.136693 |
| ignorant people follow | 0 | - | 0.137286 |
| people lack | 0 | - | 0.138538 |
| time onwards | 0 | - | 0.138740 |
| ordinary people pretend | 0 | - | 0.143462 |
| ordinary people partake | 0 | - | 0.143852 |
| people today | 0 | - | 0.144745 |
| people imagine | 0 | - | 0.146739 |
| water tormas | 0 | - | 0.148361 |
| kalpas time | 0 | - | 0.158025 |
| people spend | 0 | - | 0.173383 |
| sutras speak | 0 | - | 0.178033 |
| people learn | 0 | - | 0.181975 |
| non dharma | 0 | - | 0.182428 |
| people speak | 0 | - | 0.183729 |
| people lose | 0 | - | 0.184462 |
| people enjoy | 0 | - | 0.186387 |
| people fail | 0 | - | 0.186496 |
| people claim | 0 | - | 0.188548 |
| karmapa lamas | 0 | - | 0.190134 |
| thirty seven | 0 | - | 0.195611 |
| pointed mind | 0 | - | 0.195825 |
| black hat karmapas | 0 | - | 0.196380 |
| wrathful black mother | 0 | - | 0.197485 |
| wrathful black mother use | 0 | - | 0.197514 |
| nowadays people | 0 | - | 0.198413 |
| people nowadays | 0 | - | 0.198413 |
| hells derive | 0 | - | 0.207039 |
| goddesses offering | 0 | - | 0.211292 |
| hell ofutpala like | 0 | - | 0.211962 |
| day practice | 0 | - | 0.212836 |
| langri thangpa gloomy face | 0 | - | 0.213438 |
| doctrines transference tradition | 0 | - | 0.219969 |
| people behave | 0 | - | 0.221451 |
| teachings ofmaitreya | 0 | - | 0.230175 |
| people pay | 0 | - | 0.230980 |
| ego clinging | 0 | - | 0.232131 |
| people add | 0 | - | 0.237253 |
| prosperous people | 0 | - | 0.239060 |
| root samayas | 0 | - | 0.246946 |
| moment onwards | 0 | - | 0.249182 |
| cheat people | 0 | - | 0.251639 |
| ignorant people | 0 | - | 0.251680 |
| people manage | 0 | - | 0.258720 |
| old people | 0 | - | 0.260402 |
| lotus bud | 0 | - | 0.260613 |
| people crave | 0 | - | 0.263730 |
| people pretend | 0 | - | 0.263862 |
| impress people | 0 | - | 0.264249 |
| people partake | 0 | - | 0.264372 |
| people unhappy | 0 | - | 0.264384 |
| gifted people | 0 | - | 0.264916 |
| people intimately | 0 | - | 0.270304 |
| reliable people | 0 | - | 0.270322 |
| people declare | 0 | - | 0.270794 |
| order great universal | 0 | - | 0.275906 |
| black mother | 0 | - | 0.285523 |
| black mother use | 0 | - | 0.285556 |
| meditate single mindedly | 0 | - | 0.295132 |
| day people | 0 | - | 0.295670 |
| mantras perfunctorily | 0 | - | 0.296256 |
| principal sravakas | 0 | - | 0.299401 |

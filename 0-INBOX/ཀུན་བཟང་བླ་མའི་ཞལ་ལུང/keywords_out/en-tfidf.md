---
title: TF-IDF Vocabulary Analysis — en
source: C:\Users\geshe lobzang tseten\repos\bodhisattvacharyavatara-rails\0-INBOX\ཀུན་བཟང་བླ་མའི་ཞལ་ལུང\en.md
corpus: Reuters-21578 (10,788 newswire documents) via NLTK · sklearn TfidfVectorizer(smooth_idf=True)
method: TF × IDF — term frequency in translation vs. inverse document frequency in Reuters corpus
generated: 2026-08-03
unique_terms: 7632 (normalized; 8673 raw word-forms before lemmatization)
total_content_tokens: 57,704
status: draft
---

# TF-IDF Vocabulary Analysis — en

Generated **2026-08-03** · source: `en.md` · **7,632 unique content terms (normalized)** ranked — merged down from 8,673 raw word-forms.

This report answers two questions:

1. **Which words in this translation are most frequent here but rare in everyday English?**  
   → High TF-IDF score. These are the lexical signatures of the text.
2. **Which words appear in the text but are also very common in general English?**  
   → Low TF-IDF score. These look familiar but carry specialist meaning here.

---

## Methodology

**Term Frequency (TF)** — count of each word in the translation, normalised by total content-token count.
Frontmatter, verse markers (`^1-2`), numbers and markdown syntax are stripped before counting.

**Inverse Document Frequency (IDF)** — computed from the Reuters-21578 newswire corpus
(10,788 documents, ~1.3 M tokens) using sklearn's smooth IDF formula:
`idf(t) = log((1 + N) / (1 + df(t))) + 1`. Corpus maximum ≈ 9.59. Scale:

| IDF range | Meaning |
|-----------|---------|
| 1.0 – 1.5 | Function word — present in virtually every document |
| 1.5 – 3.0 | Common content word — high general-English frequency |
| 3.0 – 6.0 | Moderately rare — limited domain or register |
| 6.0 – 9.0 | Uncommon / archaic — rare in Reuters |
| 9.59 (max) | Absent from Reuters — domain-exclusive, coined, or Pāli |

**TF-IDF score** = TF × IDF × 10⁶ (scaled for readability).

**Colour bands** used in the table:

| Band | Score range | Interpretation |
|------|-------------|----------------|
| 🔴 | ≥ 50,000 | Text-exclusive — word essentially does not exist outside this translation |
| 🟠 | 10,000 – 49,999 | Domain-specific — Buddhist / Abhidhamma vocabulary |
| 🟡 | 3,000 – 9,999 | Specialist register — unusual in general English |
| 🟢 | 500 – 2,999 | Moderately distinctive — identifiable domain presence |
| 🔵 | 50 – 499 | Moderately common — has general English presence |
| ⚪ | 0 – 49 | Universal / function word |

---

## Distribution by Band

| Band | Terms | % of vocabulary |
|------|-------|----------------|
| 🔴 extremely high — text-exclusive | 3 | 0.0% |
| 🟠 very high — domain-specific | 87 | 1.1% |
| 🟡 high — specialist register | 444 | 5.8% |
| 🟢 medium — moderately distinctive | 1,824 | 23.9% |
| 🔵 low — common in general English | 5,274 | 69.1% |
| ⚪ very low — function / universal word | 0 | 0.0% |

---

## N-gram Keywords (YAKE, verified against source text)

A separate keyword pass using YAKE (unigram–trigram statistical extraction, lemmatized via spaCy) was run on this same text, then filtered to keep only phrases that literally occur as contiguous word sequences in `en.md` (case-insensitive, exact word order) — see `en-n-gram-keyword.json`. Score here is the YAKE score (lower = more important), a different scale from the TF-IDF score used elsewhere in this report; the two rankings are not directly comparable.

**3,376 verified n-gram keywords**, sorted by YAKE score ascending (most important first).

| Rank | Phrase | YAKE score |
|------|--------|-----------|
| 1 | **dharma** | 0.000066 |
| 2 | **buddha** | 0.000120 |
| 3 | **teacher** | 0.000327 |
| 4 | **great** | 0.000332 |
| 5 | **great dharma king** | 0.000345 |
| 6 | **negative action** | 0.000408 |
| 7 | **dharma king** | 0.000417 |
| 8 | **action** | 0.000450 |
| 9 | **dharma practice** | 0.000553 |
| 10 | **dharma king trisong** | 0.000557 |
| 11 | **dharma king songtsen** | 0.000568 |
| 12 | **time** | 0.000594 |
| 13 | **true dharma** | 0.000664 |
| 14 | **practise dharma** | 0.000705 |
| 15 | **life** | 0.000722 |
| 16 | **mind** | 0.000769 |
| 17 | **time lord buddha** | 0.000773 |
| 18 | **buddha dharma** | 0.000845 |
| 19 | **jetsun mila** | 0.000853 |
| 20 | **good** | 0.000894 |
| 21 | **practice** | 0.000961 |
| 22 | **jewel** | 0.000988 |
| 23 | **buddha sakyamuni** | 0.001044 |
| 24 | **king** | 0.001076 |
| 25 | **lord buddha** | 0.001077 |
| 26 | **perfect buddha** | 0.001148 |
| 27 | **great master** | 0.001219 |
| 28 | **people** | 0.001279 |
| 29 | **king jewel crest** | 0.001307 |
| 30 | **positive action** | 0.001327 |
| 31 | **authentic dharma** | 0.001389 |
| 32 | **negative** | 0.001416 |
| 33 | **great teacher** | 0.001423 |
| 34 | **secret mantra vajrayana** | 0.001430 |
| 35 | **suffer** | 0.001467 |
| 36 | **omniscient dharma king** | 0.001542 |
| 37 | **bodhisattva** | 0.001569 |
| 38 | **great vehicle** | 0.001587 |
| 39 | **death** | 0.001597 |
| 40 | **teaching** | 0.001630 |
| 41 | **body** | 0.001752 |
| 42 | **great perfection** | 0.001754 |
| 43 | **compassion** | 0.001779 |
| 44 | **perfect buddhahood** | 0.001807 |
| 45 | **great compassion** | 0.001869 |
| 46 | **teach** | 0.001889 |
| 47 | **merit** | 0.001939 |
| 48 | **past** | 0.001969 |
| 49 | **single dharma practice** | 0.001979 |
| 50 | **real buddha** | 0.001997 |
| 51 | **day** | 0.002019 |
| 52 | **secret mantra vehicle** | 0.002038 |
| 53 | **buddhahood** | 0.002039 |
| 54 | **guru yoga** | 0.002044 |
| 55 | **bodhicitta** | 0.002119 |
| 56 | **realm** | 0.002122 |
| 57 | **refuge** | 0.002155 |
| 58 | **dharma protector** | 0.002166 |
| 59 | **path** | 0.002170 |
| 60 | **secret mantra** | 0.002174 |
| 61 | **bodhisattvas** | 0.002181 |
| 62 | **offering** | 0.002287 |
| 63 | **practise** | 0.002308 |
| 64 | **mila** | 0.002356 |
| 65 | **great bodhisattva abbot** | 0.002367 |
| 66 | **great dharma** | 0.002466 |
| 67 | **secret mantrayana** | 0.002519 |
| 68 | **master** | 0.002529 |
| 69 | **bodhisattva dharmodgata** | 0.002558 |
| 70 | **buddha amitabha** | 0.002597 |
| 71 | **dharma teaching** | 0.002600 |
| 72 | **wisdom** | 0.002631 |
| 73 | **practise real dharma** | 0.002649 |
| 74 | **word** | 0.002665 |
| 75 | **call** | 0.002703 |
| 76 | **place** | 0.002708 |
| 77 | **take** | 0.002786 |
| 78 | **dharma king trisongdetsen** | 0.002791 |
| 79 | **hell** | 0.002791 |
| 80 | **think** | 0.002818 |
| 81 | **secret** | 0.002884 |
| 82 | **take refuge** | 0.002983 |
| 83 | **faith** | 0.002993 |
| 84 | **human life** | 0.003045 |
| 85 | **king jewel** | 0.003134 |
| 86 | **end** | 0.003186 |
| 87 | **food** | 0.003186 |
| 88 | **state** | 0.003281 |
| 89 | **vajra** | 0.003303 |
| 90 | **effect** | 0.003358 |
| 91 | **long** | 0.003378 |
| 92 | **practise true dharma** | 0.003397 |
| 93 | **perfect** | 0.003425 |
| 94 | **tibet** | 0.003430 |
| 95 | **mother** | 0.003439 |
| 96 | **perfect buddha sakyamuni** | 0.003445 |
| 97 | **power** | 0.003576 |
| 98 | **heart** | 0.003583 |
| 99 | **jetsun** | 0.003646 |
| 100 | **human** | 0.003668 |
| 101 | **pure dharma** | 0.003690 |
| 102 | **lord** | 0.003741 |
| 103 | **time bodhisattva dharmodgata** | 0.003742 |
| 104 | **thing** | 0.003745 |
| 105 | **root teacher** | 0.003766 |
| 106 | **positive** | 0.003805 |
| 107 | **quality** | 0.003845 |
| 108 | **real dharma** | 0.003907 |
| 109 | **head** | 0.003943 |
| 110 | **ask** | 0.004031 |
| 111 | **discover dharma** | 0.004069 |
| 112 | **great bodhisattva** | 0.004088 |
| 113 | **person** | 0.004112 |
| 114 | **thought** | 0.004203 |
| 115 | **great king** | 0.004218 |
| 116 | **king trisong detsen** | 0.004222 |
| 117 | **thousand** | 0.004223 |
| 118 | **ordinary** | 0.004252 |
| 119 | **lower** | 0.004263 |
| 120 | **suffering** | 0.004281 |
| 121 | **guru** | 0.004289 |
| 122 | **make** | 0.004374 |
| 123 | **single** | 0.004387 |
| 124 | **god** | 0.004406 |
| 125 | **jewel crest** | 0.004470 |
| 126 | **water** | 0.004500 |
| 127 | **bhagavan buddha** | 0.004516 |
| 128 | **attain perfect buddhahood** | 0.004525 |
| 129 | **moment** | 0.004593 |
| 130 | **present buddha sakyamuni** | 0.004603 |
| 131 | **perfect teacher** | 0.004633 |
| 132 | **spiritual teacher** | 0.004746 |
| 133 | **perfectly practise dharma** | 0.004766 |
| 134 | **feel** | 0.004768 |
| 135 | **samsara** | 0.004772 |
| 136 | **peerless teacher** | 0.004883 |
| 137 | **practise guru yoga** | 0.004946 |
| 138 | **happiness** | 0.005017 |
| 139 | **past life** | 0.005028 |
| 140 | **benefit** | 0.005053 |
| 141 | **instruction** | 0.005127 |
| 142 | **hand** | 0.005193 |
| 143 | **bodhisattva dharmodgata teaching** | 0.005203 |
| 144 | **oddiyana** | 0.005205 |
| 145 | **vajra guru mantra** | 0.005212 |
| 146 | **wealth** | 0.005259 |
| 147 | **omniscient dharma** | 0.005293 |
| 148 | **spiritual friend** | 0.005295 |
| 149 | **great perfection lineage** | 0.005301 |
| 150 | **reborn** | 0.005302 |
| 151 | **precious** | 0.005355 |
| 152 | **true** | 0.005381 |
| 153 | **kalpa** | 0.005390 |
| 154 | **teacher vajrasattva** | 0.005395 |
| 155 | **precious lord guru** | 0.005405 |
| 156 | **bring** | 0.005425 |
| 157 | **find** | 0.005444 |
| 158 | **mantra** | 0.005553 |
| 159 | **pure** | 0.005607 |
| 160 | **rinpoche** | 0.005697 |
| 161 | **vajrasattva** | 0.005716 |
| 162 | **long time** | 0.005735 |
| 163 | **wrong** | 0.005832 |
| 164 | **friend** | 0.005832 |
| 165 | **india** | 0.005850 |
| 166 | **free** | 0.005904 |
| 167 | **world** | 0.005940 |
| 168 | **follow** | 0.005941 |
| 169 | **evil** | 0.006005 |
| 170 | **die** | 0.006037 |
| 171 | **year** | 0.006052 |
| 172 | **evil action** | 0.006054 |
| 173 | **syllable mantra** | 0.006142 |
| 174 | **present** | 0.006152 |
| 175 | **meditate** | 0.006176 |
| 176 | **buddha kasyapa** | 0.006191 |
| 177 | **harm** | 0.006225 |
| 178 | **sublime dharma** | 0.006231 |
| 179 | **spiritual** | 0.006315 |
| 180 | **live** | 0.006374 |
| 181 | **perfection** | 0.006423 |
| 182 | **jetsun milarepa** | 0.006429 |
| 183 | **glorious root teacher** | 0.006506 |
| 184 | **good kalpa** | 0.006532 |
| 185 | **king songtsen gampo** | 0.006571 |
| 186 | **buddha maitreya** | 0.006589 |
| 187 | **meditation** | 0.006592 |
| 188 | **naropa** | 0.006602 |
| 189 | **dharma properly** | 0.006697 |
| 190 | **light** | 0.006719 |
| 191 | **disciple** | 0.006740 |
| 192 | **sutra** | 0.006830 |
| 193 | **precious jewel** | 0.006924 |
| 194 | **bear** | 0.006929 |
| 195 | **atisa** | 0.006960 |
| 196 | **speech** | 0.006963 |
| 197 | **love** | 0.006964 |
| 198 | **realization** | 0.006987 |
| 199 | **dagpo rinpoche** | 0.006992 |
| 200 | **marpa** | 0.007002 |
| 201 | **leave** | 0.007017 |
| 202 | **bring great benefit** | 0.007020 |
| 203 | **profound dharma** | 0.007031 |
| 204 | **form** | 0.007101 |
| 205 | **point** | 0.007179 |
| 206 | **negative emotion** | 0.007189 |
| 207 | **completely perfect buddha** | 0.007404 |
| 208 | **sublime teacher** | 0.007414 |
| 209 | **mantra vajrayana** | 0.007475 |
| 210 | **recite** | 0.007511 |
| 211 | **attain buddhahood** | 0.007556 |
| 212 | **nature** | 0.007632 |
| 213 | **ordinary people** | 0.007655 |
| 214 | **great indian master** | 0.007730 |
| 215 | **liberation** | 0.007739 |
| 216 | **perfect teacher vajrasattva** | 0.007775 |
| 217 | **great kalpa** | 0.007840 |
| 218 | **geshe** | 0.007867 |
| 219 | **flesh** | 0.007907 |
| 220 | **present life** | 0.007945 |
| 221 | **vehicle** | 0.007987 |
| 222 | **lama** | 0.007993 |
| 223 | **kind** | 0.008009 |
| 224 | **padampa sangye** | 0.008057 |
| 225 | **yoga** | 0.008115 |
| 226 | **perfection phase** | 0.008196 |
| 227 | **precious dharma** | 0.008199 |
| 228 | **mean** | 0.008328 |
| 229 | **harmful** | 0.008334 |
| 230 | **dharma practitioner** | 0.008435 |
| 231 | **reply** | 0.008506 |
| 232 | **great guru** | 0.008508 |
| 233 | **natural state** | 0.008517 |
| 234 | **important** | 0.008523 |
| 235 | **past negative** | 0.008528 |
| 236 | **main practice** | 0.008529 |
| 237 | **kind teacher** | 0.008532 |
| 238 | **transference** | 0.008558 |
| 239 | **give** | 0.008624 |
| 240 | **root** | 0.008647 |
| 241 | **king trisong** | 0.008689 |
| 242 | **natural great perfection** | 0.008765 |
| 243 | **great bliss** | 0.008853 |
| 244 | **tilopa** | 0.008870 |
| 245 | **deity** | 0.008871 |
| 246 | **visualize** | 0.008891 |
| 247 | **experience** | 0.008972 |
| 248 | **perfect dharma** | 0.008996 |
| 249 | **true jewel** | 0.009018 |
| 250 | **tell** | 0.009061 |
| 251 | **animal** | 0.009116 |
| 252 | **land** | 0.009148 |
| 253 | **rigdzin jigme lingpa** | 0.009199 |
| 254 | **guru rinpoche** | 0.009262 |
| 255 | **peerless dagpo rinpoche** | 0.009321 |
| 256 | **man** | 0.009341 |
| 257 | **great ocean** | 0.009409 |
| 258 | **blood** | 0.009414 |
| 259 | **tantra** | 0.009426 |
| 260 | **act** | 0.009438 |
| 261 | **supreme authentic dharma** | 0.009519 |
| 262 | **enemy** | 0.009551 |
| 263 | **future** | 0.009554 |
| 264 | **spirit** | 0.009555 |
| 265 | **jowo rinpoche** | 0.009561 |
| 266 | **vajra master** | 0.009585 |
| 267 | **method** | 0.009605 |
| 268 | **utterly perfect buddha** | 0.009613 |
| 269 | **set** | 0.009643 |
| 270 | **father** | 0.009656 |
| 271 | **kill** | 0.009683 |
| 272 | **essence** | 0.009694 |
| 273 | **result** | 0.009732 |
| 274 | **blessing** | 0.009812 |
| 275 | **great river** | 0.009848 |
| 276 | **future life** | 0.009851 |
| 277 | **wisdom mind** | 0.009857 |
| 278 | **precious human life** | 0.009863 |
| 279 | **mount meru** | 0.009863 |
| 280 | **mantra vehicle** | 0.009864 |
| 281 | **attain** | 0.009875 |
| 282 | **offer** | 0.009902 |
| 283 | **transcendent** | 0.009917 |
| 284 | **prayer** | 0.009960 |
| 285 | **supreme** | 0.010038 |
| 286 | **single dharma** | 0.010094 |
| 287 | **great master tendzin** | 0.010097 |
| 288 | **profound** | 0.010226 |
| 289 | **vast** | 0.010459 |
| 290 | **jewel family** | 0.010464 |
| 291 | **practise dharma alongside** | 0.010472 |
| 292 | **refuge practice** | 0.010514 |
| 293 | **daughter** | 0.010625 |
| 294 | **buddha family** | 0.010651 |
| 295 | **vow** | 0.010677 |
| 296 | **authentic teacher** | 0.010700 |
| 297 | **practise dharma authentically** | 0.010741 |
| 298 | **wrong view** | 0.010834 |
| 299 | **true dharma properly** | 0.010843 |
| 300 | **bad** | 0.010992 |
| 301 | **black** | 0.011003 |
| 302 | **eye** | 0.011038 |
| 303 | **intermediate state** | 0.011133 |
| 304 | **effort** | 0.011153 |
| 305 | **advantage** | 0.011176 |
| 306 | **red** | 0.011202 |
| 307 | **great benefit** | 0.011212 |
| 308 | **sun** | 0.011250 |
| 309 | **family** | 0.011289 |
| 310 | **sublime** | 0.011347 |
| 311 | **geshe tonpa** | 0.011368 |
| 312 | **demon** | 0.011396 |
| 313 | **great giving** | 0.011454 |
| 314 | **present great kalpa** | 0.011470 |
| 315 | **kalpas** | 0.011515 |
| 316 | **long life** | 0.011520 |
| 317 | **mandala** | 0.011530 |
| 318 | **begin** | 0.011577 |
| 319 | **buddha protector amitayus** | 0.011577 |
| 320 | **arouse bodhicitta** | 0.011581 |
| 321 | **lineage** | 0.011716 |
| 322 | **authentic spiritual teacher** | 0.011750 |
| 323 | **good fortune** | 0.011909 |
| 324 | **garab dorje** | 0.012033 |
| 325 | **genuine dharma** | 0.012040 |
| 326 | **noble** | 0.012060 |
| 327 | **transcendent wisdom** | 0.012075 |
| 328 | **view** | 0.012126 |
| 329 | **true buddha** | 0.012203 |
| 330 | **buddha samantabhadra** | 0.012234 |
| 331 | **start** | 0.012276 |
| 332 | **simply** | 0.012281 |
| 333 | **king songtsen** | 0.012398 |
| 334 | **work** | 0.012414 |
| 335 | **powerful** | 0.012428 |
| 336 | **joy** | 0.012436 |
| 337 | **wheel** | 0.012437 |
| 338 | **buddha protector** | 0.012447 |
| 339 | **cho** | 0.012481 |
| 340 | **devotion** | 0.012503 |
| 341 | **turn** | 0.012593 |
| 342 | **time bodhisattva** | 0.012644 |
| 343 | **complete** | 0.012645 |
| 344 | **master jowo atisa** | 0.012716 |
| 345 | **pure buddha** | 0.012723 |
| 346 | **jigme lingpa** | 0.012748 |
| 347 | **tree** | 0.012763 |
| 348 | **sangha** | 0.012816 |
| 349 | **time great** | 0.012830 |
| 350 | **great vehicle tradition** | 0.013087 |
| 351 | **eat** | 0.013319 |
| 352 | **surpass buddha sakyamuni** | 0.013331 |
| 353 | **present buddha** | 0.013387 |
| 354 | **difficult** | 0.013406 |
| 355 | **fire** | 0.013418 |
| 356 | **mantrayana** | 0.013427 |
| 357 | **sky** | 0.013473 |
| 358 | **authentic** | 0.013536 |
| 359 | **wrong action** | 0.013612 |
| 360 | **listen** | 0.013656 |
| 361 | **perfectly** | 0.013666 |
| 362 | **love compassion** | 0.013699 |
| 363 | **worldly life** | 0.013702 |
| 364 | **jowo atisa** | 0.013750 |
| 365 | **bodhisattva sadaprarudita** | 0.013787 |
| 366 | **great love** | 0.013816 |
| 367 | **day geshe ben** | 0.013825 |
| 368 | **secret true teaching** | 0.013934 |
| 369 | **lord nagarjuna** | 0.013947 |
| 370 | **venerable teacher** | 0.014035 |
| 371 | **son** | 0.014079 |
| 372 | **moon** | 0.014089 |
| 373 | **conqueror** | 0.014091 |
| 374 | **parent** | 0.014109 |
| 375 | **gracious root teacher** | 0.014167 |
| 376 | **good thing** | 0.014174 |
| 377 | **rebirth** | 0.014238 |
| 378 | **natural** | 0.014368 |
| 379 | **secret path** | 0.014381 |
| 380 | **emptiness** | 0.014395 |
| 381 | **intention** | 0.014447 |
| 382 | **real** | 0.014550 |
| 383 | **white** | 0.014553 |
| 384 | **cut** | 0.014595 |
| 385 | **freedom** | 0.014596 |
| 386 | **lead** | 0.014612 |
| 387 | **receive** | 0.014649 |
| 388 | **concentration** | 0.014655 |
| 389 | **dorje** | 0.014663 |
| 390 | **dharmodgata** | 0.014680 |
| 391 | **impermanence** | 0.014714 |
| 392 | **pain** | 0.014714 |
| 393 | **nectar** | 0.014724 |
| 394 | **jowo** | 0.014742 |
| 395 | **ground** | 0.014770 |
| 396 | **buddha vajradhara** | 0.014852 |
| 397 | **great secret** | 0.014869 |
| 398 | **sadaprarudita** | 0.015007 |
| 399 | **profound path** | 0.015066 |
| 400 | **great faith** | 0.015102 |
| 401 | **completely** | 0.015133 |
| 402 | **accomplishment** | 0.015271 |
| 403 | **great perfect** | 0.015369 |
| 404 | **hundred** | 0.015393 |
| 405 | **finally** | 0.015413 |
| 406 | **good thought** | 0.015436 |
| 407 | **sakya buddha** | 0.015437 |
| 408 | **lord maitreya** | 0.015497 |
| 409 | **samayas** | 0.015559 |
| 410 | **small** | 0.015592 |
| 411 | **appear** | 0.015622 |
| 412 | **preta** | 0.015646 |
| 413 | **future buddha** | 0.015703 |
| 414 | **buddha manjusri** | 0.015752 |
| 415 | **avoid** | 0.015771 |
| 416 | **speech mind** | 0.016056 |
| 417 | **fact** | 0.016068 |
| 418 | **hum** | 0.016186 |
| 419 | **bodhisattva level** | 0.016194 |
| 420 | **tonpa** | 0.016266 |
| 421 | **innumerable** | 0.016298 |
| 422 | **lord guru** | 0.016389 |
| 423 | **great compassionate** | 0.016480 |
| 424 | **mount** | 0.016530 |
| 425 | **arise** | 0.016540 |
| 426 | **buddhafield** | 0.016543 |
| 427 | **understand** | 0.016552 |
| 428 | **sangye** | 0.016729 |
| 429 | **birth** | 0.016746 |
| 430 | **rich** | 0.016753 |
| 431 | **worldly** | 0.016758 |
| 432 | **mountain** | 0.016759 |
| 433 | **face** | 0.016767 |
| 434 | **bring great** | 0.016784 |
| 435 | **ultimate** | 0.016805 |
| 436 | **imagine** | 0.016814 |
| 437 | **attachment** | 0.016816 |
| 438 | **activity** | 0.016868 |
| 439 | **realize** | 0.016976 |
| 440 | **feel great** | 0.016996 |
| 441 | **clear** | 0.016996 |
| 442 | **hear** | 0.017029 |
| 443 | **nagarjuna** | 0.017060 |
| 444 | **protector** | 0.017176 |
| 445 | **teacher nagarjuna** | 0.017267 |
| 446 | **indra** | 0.017403 |
| 447 | **good lama** | 0.017422 |
| 448 | **great translator** | 0.017471 |
| 449 | **great perfect vajradhara** | 0.017509 |
| 450 | **outer** | 0.017520 |
| 451 | **desire** | 0.017616 |
| 452 | **great siddha** | 0.017657 |
| 453 | **prostration** | 0.017677 |
| 454 | **hard** | 0.017718 |
| 455 | **effect similar** | 0.017783 |
| 456 | **entire dharma** | 0.017868 |
| 457 | **bodhisattva samantabhadra** | 0.017987 |
| 458 | **infinite** | 0.018027 |
| 459 | **precious lord** | 0.018135 |
| 460 | **essential** | 0.018187 |
| 461 | **central** | 0.018204 |
| 462 | **buddha infinite** | 0.018279 |
| 463 | **rest** | 0.018300 |
| 464 | **human life complete** | 0.018362 |
| 465 | **practise guru** | 0.018416 |
| 466 | **great translator vairotsana** | 0.018484 |
| 467 | **confess** | 0.018582 |
| 468 | **human form** | 0.018667 |
| 469 | **sakyamuni** | 0.018695 |
| 470 | **brahma** | 0.018823 |
| 471 | **middle** | 0.018845 |
| 472 | **dedicate** | 0.018971 |
| 473 | **empowerment** | 0.019056 |
| 474 | **develop** | 0.019079 |
| 475 | **instant** | 0.019112 |
| 476 | **possession** | 0.019133 |
| 477 | **river** | 0.019161 |
| 478 | **stay** | 0.019294 |
| 479 | **high** | 0.019297 |
| 480 | **generation** | 0.019343 |
| 481 | **accumulate merit** | 0.019462 |
| 482 | **base** | 0.019476 |
| 483 | **single good thought** | 0.019643 |
| 484 | **rigdzin jigme** | 0.019723 |
| 485 | **buddha vairocana** | 0.019863 |
| 486 | **level** | 0.019930 |
| 487 | **drink** | 0.019935 |
| 488 | **main** | 0.020049 |
| 489 | **matter** | 0.020052 |
| 490 | **doctrine** | 0.020201 |
| 491 | **palace** | 0.020211 |
| 492 | **dead** | 0.020268 |
| 493 | **space** | 0.020275 |
| 494 | **ocean** | 0.020313 |
| 495 | **consciousness** | 0.020347 |
| 496 | **night** | 0.020479 |
| 497 | **study dharma** | 0.020511 |
| 498 | **vajra guru** | 0.020613 |
| 499 | **phase** | 0.020785 |
| 500 | **emotion** | 0.020815 |
| 501 | **earth** | 0.020869 |
| 502 | **happy** | 0.020960 |
| 503 | **higher** | 0.020978 |
| 504 | **naropa thought** | 0.020993 |
| 505 | **negative karmic effect** | 0.021015 |
| 506 | **nanda** | 0.021122 |
| 507 | **good worldly life** | 0.021128 |
| 508 | **intermediate** | 0.021135 |
| 509 | **buddha ratnasambhava** | 0.021370 |
| 510 | **buddha amoghasiddhi** | 0.021370 |
| 511 | **cold** | 0.021393 |
| 512 | **primordially buddha** | 0.021426 |
| 513 | **buddha vajraguhya** | 0.021427 |
| 514 | **inexhaustible dharma** | 0.021440 |
| 515 | **number** | 0.021470 |
| 516 | **fault** | 0.021545 |
| 517 | **dharma understanding** | 0.021587 |
| 518 | **bodhisattva santideva** | 0.021733 |
| 519 | **enlightenment** | 0.021734 |
| 520 | **absolute** | 0.021793 |
| 521 | **universe** | 0.021814 |
| 522 | **sacred dharma** | 0.021853 |
| 523 | **sarhsara** | 0.021937 |
| 524 | **action good** | 0.022000 |
| 525 | **ordinary life** | 0.022004 |
| 526 | **heaven** | 0.022020 |
| 527 | **amitabha** | 0.022023 |
| 528 | **action family** | 0.022048 |
| 529 | **great par** | 0.022053 |
| 530 | **milarepa** | 0.022093 |
| 531 | **buddha immediately** | 0.022103 |
| 532 | **syllable** | 0.022176 |
| 533 | **perfect teacher venerable** | 0.022253 |
| 534 | **poison jetsun mila** | 0.022368 |
| 535 | **primal wisdom** | 0.022389 |
| 536 | **fall** | 0.022403 |
| 537 | **generation perfection** | 0.022451 |
| 538 | **guru mantra** | 0.022474 |
| 539 | **source** | 0.022493 |
| 540 | **long ago** | 0.022532 |
| 541 | **sheep** | 0.022770 |
| 542 | **similar** | 0.022808 |
| 543 | **tradition** | 0.022832 |
| 544 | **mind lineage** | 0.022945 |
| 545 | **confession** | 0.022968 |
| 546 | **hell realm** | 0.022999 |
| 547 | **great pandita naropa** | 0.023039 |
| 548 | **negative effect** | 0.023070 |
| 549 | **support** | 0.023100 |
| 550 | **entire** | 0.023117 |
| 551 | **patience** | 0.023240 |
| 552 | **diligence** | 0.023244 |
| 553 | **buddha infinite aspiration** | 0.023248 |
| 554 | **ephemeral hell** | 0.023269 |
| 555 | **vajrayana** | 0.023273 |
| 556 | **medicine buddha** | 0.023285 |
| 557 | **holy dharma** | 0.023456 |
| 558 | **circumstance** | 0.023478 |
| 559 | **dharma language** | 0.023513 |
| 560 | **great kalpas** | 0.023520 |
| 561 | **bring buddhahood** | 0.023706 |
| 562 | **flower** | 0.023753 |
| 563 | **secret mantra mandala** | 0.023876 |
| 564 | **great tilopa** | 0.023891 |
| 565 | **train** | 0.023907 |
| 566 | **perform** | 0.023935 |
| 567 | **care** | 0.023952 |
| 568 | **combine dharma** | 0.024067 |
| 569 | **lotus** | 0.024074 |
| 570 | **good bad** | 0.024096 |
| 571 | **omniscient** | 0.024140 |
| 572 | **determination** | 0.024144 |
| 573 | **today** | 0.024230 |
| 574 | **thirty** | 0.024295 |
| 575 | **clothing** | 0.024323 |
| 576 | **lack** | 0.024331 |
| 577 | **lord padampa sangye** | 0.024346 |
| 578 | **purify** | 0.024450 |
| 579 | **fruit** | 0.024469 |
| 580 | **mandala offering** | 0.024477 |
| 581 | **ben** | 0.024482 |
| 582 | **pile** | 0.024563 |
| 583 | **lake** | 0.024613 |
| 584 | **time lord** | 0.024621 |
| 585 | **trisong detsen** | 0.024685 |
| 586 | **attitude** | 0.024745 |
| 587 | **bodhisattva abbot** | 0.024797 |
| 588 | **merit great** | 0.024874 |
| 589 | **explain** | 0.024967 |
| 590 | **brahmin** | 0.025005 |
| 591 | **negative act** | 0.025015 |
| 592 | **arouse** | 0.025049 |
| 593 | **langri thangpa** | 0.025087 |
| 594 | **padampa** | 0.025096 |
| 595 | **great compassion possess** | 0.025116 |
| 596 | **cho practice** | 0.025117 |
| 597 | **reason** | 0.025140 |
| 598 | **numerous** | 0.025249 |
| 599 | **text** | 0.025275 |
| 600 | **black true mother** | 0.025355 |
| 601 | **deed** | 0.025390 |
| 602 | **geshe ben** | 0.025468 |
| 603 | **accumulate** | 0.025488 |
| 604 | **existence** | 0.025498 |
| 605 | **sambhogakaya buddha** | 0.025546 |
| 606 | **perception** | 0.025616 |
| 607 | **peerless** | 0.025641 |
| 608 | **lama ngokpa** | 0.025651 |
| 609 | **material** | 0.025889 |
| 610 | **jigme** | 0.025906 |
| 611 | **dagpo** | 0.025953 |
| 612 | **authentic vajra master** | 0.025955 |
| 613 | **natural great** | 0.026054 |
| 614 | **vajra family** | 0.026132 |
| 615 | **great wisdom** | 0.026204 |
| 616 | **hold** | 0.026270 |
| 617 | **bodhicitta practice** | 0.026465 |
| 618 | **age** | 0.026551 |
| 619 | **karmic** | 0.026576 |
| 620 | **mila dorje gyaltsen** | 0.026697 |
| 621 | **great pain** | 0.026716 |
| 622 | **dharma drift** | 0.026742 |
| 623 | **sign** | 0.026770 |
| 624 | **story** | 0.026800 |
| 625 | **great lama** | 0.026803 |
| 626 | **dharma alongside** | 0.026809 |
| 627 | **recitation** | 0.026832 |
| 628 | **immense** | 0.026834 |
| 629 | **excellent** | 0.026887 |
| 630 | **child** | 0.026889 |
| 631 | **foot** | 0.027007 |
| 632 | **generosity** | 0.027012 |
| 633 | **glorious** | 0.027039 |
| 634 | **short** | 0.027056 |
| 635 | **dodrup chen rinpoche** | 0.027255 |
| 636 | **dharma authentically** | 0.027310 |
| 637 | **purest dharma** | 0.027312 |
| 638 | **marry dharma** | 0.027332 |
| 639 | **single negative thought** | 0.027656 |
| 640 | **truth** | 0.027735 |
| 641 | **extraordinary** | 0.027741 |
| 642 | **mandala base** | 0.027775 |
| 643 | **karmic effect** | 0.027992 |
| 644 | **meru** | 0.028081 |
| 645 | **learn** | 0.028215 |
| 646 | **beautiful** | 0.028217 |
| 647 | **primordial buddha** | 0.028239 |
| 648 | **open** | 0.028304 |
| 649 | **remember** | 0.028347 |
| 650 | **respect** | 0.028454 |
| 651 | **great paqqita naropa** | 0.028465 |
| 652 | **depth** | 0.028599 |
| 653 | **noble sangha** | 0.028784 |
| 654 | **metal** | 0.028814 |
| 655 | **king prasenajit** | 0.028976 |
| 656 | **forever** | 0.029084 |
| 657 | **chen rinpoche** | 0.029208 |
| 658 | **iron** | 0.029243 |
| 659 | **karma** | 0.029452 |
| 660 | **extremely** | 0.029473 |
| 661 | **suddenly** | 0.029485 |
| 662 | **buddha miraculously** | 0.029500 |
| 663 | **spend** | 0.029546 |
| 664 | **sort** | 0.029553 |
| 665 | **reflect** | 0.029571 |
| 666 | **vajra body** | 0.029676 |
| 667 | **good food** | 0.029715 |
| 668 | **sleep** | 0.029802 |
| 669 | **idea** | 0.029889 |
| 670 | **inconceivable** | 0.029979 |
| 671 | **great close** | 0.030077 |
| 672 | **noble master nagarjuna** | 0.030195 |
| 673 | **element** | 0.030317 |
| 674 | **fear** | 0.030361 |
| 675 | **compassionate root teacher** | 0.030403 |
| 676 | **great power** | 0.030420 |
| 677 | **rain** | 0.030426 |
| 678 | **great vehicle widely** | 0.030590 |
| 679 | **reach** | 0.030614 |
| 680 | **subject** | 0.030626 |
| 681 | **case** | 0.030757 |
| 682 | **samaya** | 0.031117 |
| 683 | **great care** | 0.031160 |
| 684 | **accumulation** | 0.031204 |
| 685 | **merit great rejoicing** | 0.031215 |
| 686 | **songtsen gampo** | 0.031281 |
| 687 | **meat** | 0.031376 |
| 688 | **preliminary practice** | 0.031378 |
| 689 | **eighty thousand** | 0.031406 |
| 690 | **surpass buddha** | 0.031489 |
| 691 | **fish** | 0.031524 |
| 692 | **immediately** | 0.031588 |
| 693 | **opportunity** | 0.031613 |
| 694 | **skilful** | 0.031629 |
| 695 | **young** | 0.031654 |
| 696 | **dedication** | 0.031656 |
| 697 | **extraordinary secret mantra** | 0.031680 |
| 698 | **woman** | 0.031718 |
| 699 | **arrive** | 0.031723 |
| 700 | **slight** | 0.031764 |
| 701 | **companion** | 0.031766 |
| 702 | **kindness** | 0.031803 |
| 703 | **perfect place** | 0.031858 |
| 704 | **dust** | 0.031956 |
| 705 | **house** | 0.031977 |
| 706 | **fill** | 0.031997 |
| 707 | **direction** | 0.032058 |
| 708 | **negative thought** | 0.032067 |
| 709 | **day geshe** | 0.032187 |
| 710 | **fourth jewel** | 0.032217 |
| 711 | **peerless dagpo** | 0.032245 |
| 712 | **protect** | 0.032314 |
| 713 | **ordinary worldly people** | 0.032371 |
| 714 | **stop** | 0.032549 |
| 715 | **concept** | 0.032692 |
| 716 | **enter** | 0.032704 |
| 717 | **ultimate torment** | 0.032727 |
| 718 | **sublime path** | 0.032878 |
| 719 | **ordinary human form** | 0.033002 |
| 720 | **wrathful** | 0.033007 |
| 721 | **expanse** | 0.033046 |
| 722 | **attain perfect** | 0.033069 |
| 723 | **big** | 0.033108 |
| 724 | **authentic path** | 0.033131 |
| 725 | **dark kalpa** | 0.033138 |
| 726 | **lie** | 0.033191 |
| 727 | **lingpa** | 0.033197 |
| 728 | **clear light** | 0.033217 |
| 729 | **recognize** | 0.033310 |
| 730 | **feel good** | 0.033363 |
| 731 | **fully** | 0.033461 |
| 732 | **tirthikas** | 0.033490 |
| 733 | **mental** | 0.033584 |
| 734 | **carefully** | 0.033591 |
| 735 | **teacher sakyamuni** | 0.033607 |
| 736 | **remain** | 0.033740 |
| 737 | **cast** | 0.033806 |
| 738 | **continent** | 0.033842 |
| 739 | **great kindness** | 0.033884 |
| 740 | **master teaching** | 0.033925 |
| 741 | **essential point** | 0.033934 |
| 742 | **reality** | 0.033936 |
| 743 | **single good** | 0.033963 |
| 744 | **lifetime** | 0.033975 |
| 745 | **dharmakaya** | 0.033994 |
| 746 | **fortunate** | 0.034132 |
| 747 | **complete buddhahood** | 0.034160 |
| 748 | **guide** | 0.034420 |
| 749 | **lord vajrasattva** | 0.034594 |
| 750 | **pure perception** | 0.034677 |
| 751 | **order** | 0.034869 |
| 752 | **creature** | 0.034890 |
| 753 | **impermanent** | 0.034895 |
| 754 | **crest** | 0.034927 |
| 755 | **great wheel** | 0.035031 |
| 756 | **doubt** | 0.035120 |
| 757 | **hot** | 0.035172 |
| 758 | **evil spirit** | 0.035258 |
| 759 | **great perfection subsequently** | 0.035269 |
| 760 | **clothe** | 0.035428 |
| 761 | **bless** | 0.035531 |
| 762 | **torment** | 0.035549 |
| 763 | **unable** | 0.035634 |
| 764 | **intense** | 0.035698 |
| 765 | **sublime bodhicitta** | 0.035722 |
| 766 | **meet** | 0.035821 |
| 767 | **large** | 0.035892 |
| 768 | **constantly** | 0.035943 |
| 769 | **practitioner** | 0.035984 |
| 770 | **reason guru yoga** | 0.036073 |
| 771 | **centre** | 0.036140 |
| 772 | **straight** | 0.036158 |
| 773 | **great omniscient** | 0.036308 |
| 774 | **million** | 0.036570 |
| 775 | **happen** | 0.036582 |
| 776 | **home** | 0.036743 |
| 777 | **chance** | 0.036746 |
| 778 | **life death** | 0.036755 |
| 779 | **vajrasattva practice** | 0.036768 |
| 780 | **total buddhahood** | 0.036841 |
| 781 | **include** | 0.036882 |
| 782 | **ray** | 0.037121 |
| 783 | **protector amitabha** | 0.037524 |
| 784 | **visualization** | 0.037560 |
| 785 | **venerable** | 0.037616 |
| 786 | **great wealth** | 0.037623 |
| 787 | **poor** | 0.037625 |
| 788 | **inside** | 0.037763 |
| 789 | **great sage** | 0.037785 |
| 790 | **great importance** | 0.037816 |
| 791 | **perfectly pure** | 0.037897 |
| 792 | **ago** | 0.037959 |
| 793 | **properly** | 0.038224 |
| 794 | **surround** | 0.038386 |
| 795 | **pray** | 0.038407 |
| 796 | **great tree** | 0.038472 |
| 797 | **sick** | 0.038534 |
| 798 | **garab** | 0.038552 |
| 799 | **point lord maitreya** | 0.038611 |
| 800 | **great demon** | 0.038654 |
| 801 | **serve** | 0.038682 |
| 802 | **positive act** | 0.038682 |
| 803 | **vision** | 0.038720 |
| 804 | **single word** | 0.038729 |
| 805 | **samantabhadra** | 0.038838 |
| 806 | **create** | 0.039019 |
| 807 | **great evil** | 0.039051 |
| 808 | **close** | 0.039094 |
| 809 | **brother** | 0.039097 |
| 810 | **jewel free** | 0.039146 |
| 811 | **previous life** | 0.039346 |
| 812 | **downfall** | 0.039436 |
| 813 | **wrong path** | 0.039533 |
| 814 | **excellent human life** | 0.039679 |
| 815 | **throne** | 0.039985 |
| 816 | **present great** | 0.040051 |
| 817 | **enjoy** | 0.040140 |
| 818 | **thousand people** | 0.040179 |
| 819 | **bliss** | 0.040204 |
| 820 | **great pandita** | 0.040337 |
| 821 | **hunger** | 0.040507 |
| 822 | **rise** | 0.040533 |
| 823 | **alive** | 0.040574 |
| 824 | **yogas** | 0.040577 |
| 825 | **purification** | 0.040723 |
| 826 | **renounce** | 0.040749 |
| 827 | **huge** | 0.040754 |
| 828 | **blind** | 0.040779 |
| 829 | **crown** | 0.040783 |
| 830 | **sit** | 0.040825 |
| 831 | **obtain** | 0.040960 |
| 832 | **pleasant** | 0.040975 |
| 833 | **mila dorje** | 0.040990 |
| 834 | **part** | 0.040999 |
| 835 | **presence** | 0.041005 |
| 836 | **commit** | 0.041097 |
| 837 | **hair** | 0.041123 |
| 838 | **unbearable** | 0.041133 |
| 839 | **round** | 0.041149 |
| 840 | **spiritual practice** | 0.041164 |
| 841 | **study** | 0.041174 |
| 842 | **object** | 0.041215 |
| 843 | **insect** | 0.041224 |
| 844 | **great indian** | 0.041329 |
| 845 | **clean** | 0.041351 |
| 846 | **great remorse** | 0.041497 |
| 847 | **grain** | 0.041697 |
| 848 | **lord avalokitesvara** | 0.041722 |
| 849 | **single teacher** | 0.041728 |
| 850 | **good health** | 0.041757 |
| 851 | **rock** | 0.041828 |
| 852 | **great lake** | 0.041871 |
| 853 | **reflection** | 0.041900 |
| 854 | **bodh gaya** | 0.041955 |
| 855 | **human realm** | 0.042105 |
| 856 | **horse** | 0.042179 |
| 857 | **sense** | 0.042239 |
| 858 | **king surabhibhadra** | 0.042313 |
| 859 | **ordinary human** | 0.042327 |
| 860 | **great liberation** | 0.042443 |
| 861 | **great ship** | 0.042481 |
| 862 | **humble life** | 0.042509 |
| 863 | **fail** | 0.042523 |
| 864 | **tathagata** | 0.042552 |
| 865 | **fortune** | 0.042611 |
| 866 | **siddha** | 0.042659 |
| 867 | **claim** | 0.042916 |
| 868 | **stone** | 0.042975 |
| 869 | **equal** | 0.043158 |
| 870 | **exceptionally great giving** | 0.043184 |
| 871 | **beggar** | 0.043268 |
| 872 | **compassionate** | 0.043280 |
| 873 | **pure land** | 0.043334 |
| 874 | **seat** | 0.043340 |
| 875 | **dissolve** | 0.043423 |
| 876 | **time sakyamuni** | 0.043592 |
| 877 | **authentic spiritual friend** | 0.043731 |
| 878 | **strong** | 0.043822 |
| 879 | **preliminary** | 0.043840 |
| 880 | **true teacher** | 0.043964 |
| 881 | **jetsun shepa dorje** | 0.043979 |
| 882 | **detsen** | 0.044019 |
| 883 | **abbot** | 0.044039 |
| 884 | **human existence** | 0.044075 |
| 885 | **trust** | 0.044108 |
| 886 | **sickness** | 0.044111 |
| 887 | **bind** | 0.044213 |
| 888 | **vajra sattva hum** | 0.044224 |
| 889 | **lhasa** | 0.044230 |
| 890 | **anger** | 0.044261 |
| 891 | **emanation** | 0.044304 |
| 892 | **discipline** | 0.044305 |
| 893 | **thangpa** | 0.044309 |
| 894 | **easy** | 0.044319 |
| 895 | **great effort** | 0.044377 |
| 896 | **thousand water** | 0.044464 |
| 897 | **rigdzin** | 0.044470 |
| 898 | **hide** | 0.044473 |
| 899 | **belief** | 0.044515 |
| 900 | **great vajradhara** | 0.044560 |
| 901 | **speak** | 0.044614 |
| 902 | **great maudgalyayana** | 0.044663 |
| 903 | **lose** | 0.044764 |
| 904 | **force** | 0.044769 |
| 905 | **hardship** | 0.044841 |
| 906 | **wrathful black true** | 0.044853 |
| 907 | **kind heart** | 0.044885 |
| 908 | **wrathful black** | 0.044998 |
| 909 | **great elapatra tree** | 0.045068 |
| 910 | **great scholar** | 0.045103 |
| 911 | **action positive** | 0.045133 |
| 912 | **great longchenpa** | 0.045256 |
| 913 | **numerous great sravakas** | 0.045308 |
| 914 | **jambudvipa** | 0.045437 |
| 915 | **obstacle** | 0.045656 |
| 916 | **arm** | 0.045838 |
| 917 | **union** | 0.045908 |
| 918 | **great sravakas** | 0.045938 |
| 919 | **eighty** | 0.046015 |
| 920 | **wonderful teacher forever** | 0.046127 |
| 921 | **east** | 0.046253 |
| 922 | **negative karmic** | 0.046268 |
| 923 | **perceive** | 0.046368 |
| 924 | **wonderful** | 0.046532 |
| 925 | **likewise** | 0.046579 |
| 926 | **approach** | 0.046580 |
| 927 | **pride** | 0.046590 |
| 928 | **knowledge** | 0.046746 |
| 929 | **great sinner** | 0.046818 |
| 930 | **great desire** | 0.046838 |
| 931 | **nirvana** | 0.046850 |
| 932 | **hat** | 0.046875 |
| 933 | **great misfortune** | 0.046876 |
| 934 | **future good** | 0.046898 |
| 935 | **comfort** | 0.046910 |
| 936 | **undergo** | 0.046959 |
| 937 | **thirst** | 0.046968 |
| 938 | **utterly** | 0.047009 |
| 939 | **bodhisattva tradition** | 0.047022 |
| 940 | **prajnaparamita teacher** | 0.047035 |
| 941 | **energy** | 0.047091 |
| 942 | **king ajatasatru** | 0.047128 |
| 943 | **involve** | 0.047152 |
| 944 | **basis** | 0.047522 |
| 945 | **ritual** | 0.047544 |
| 946 | **confidence** | 0.047550 |
| 947 | **nowadays** | 0.047589 |
| 948 | **protection** | 0.047590 |
| 949 | **put** | 0.047600 |
| 950 | **actual** | 0.047605 |
| 951 | **miraculous** | 0.047616 |
| 952 | **bhagavan** | 0.047723 |
| 953 | **accomplish** | 0.047770 |
| 954 | **regret** | 0.047784 |
| 955 | **great vairotsana** | 0.047814 |
| 956 | **exceptionally great** | 0.047842 |
| 957 | **seed** | 0.047895 |
| 958 | **daily practice** | 0.047939 |
| 959 | **vast expanse** | 0.048003 |
| 960 | **noble lord avalokitesvara** | 0.048050 |
| 961 | **life complete** | 0.048064 |
| 962 | **precious supreme path** | 0.048083 |
| 963 | **vidyadharas** | 0.048118 |
| 964 | **dark** | 0.048236 |
| 965 | **channel** | 0.048293 |
| 966 | **beginningless time** | 0.048300 |
| 967 | **single instant** | 0.048487 |
| 968 | **pleasure** | 0.048506 |
| 969 | **yogi** | 0.048771 |
| 970 | **harmful spirit** | 0.048933 |
| 971 | **turtle** | 0.048949 |
| 972 | **kaya** | 0.048989 |
| 973 | **condense** | 0.049148 |
| 974 | **sariputra** | 0.049153 |
| 975 | **treasury** | 0.049193 |
| 976 | **past good** | 0.049205 |
| 977 | **vajra seat** | 0.049233 |
| 978 | **change** | 0.049612 |
| 979 | **entire time** | 0.049688 |
| 980 | **unsurpassable secret mantra** | 0.049927 |
| 981 | **feel great sadness** | 0.049931 |
| 982 | **take care** | 0.050005 |
| 983 | **perfect enlightenment** | 0.050020 |
| 984 | **position** | 0.050057 |
| 985 | **mouth** | 0.050093 |
| 986 | **authentic spiritual** | 0.050154 |
| 987 | **teacher buddha** | 0.050223 |
| 988 | **deep** | 0.050242 |
| 989 | **great abbot** | 0.050352 |
| 990 | **return** | 0.050426 |
| 991 | **spread** | 0.050546 |
| 992 | **heat** | 0.050572 |
| 993 | **entire human life** | 0.050601 |
| 994 | **central tibet** | 0.050615 |
| 995 | **master jowo** | 0.050616 |
| 996 | **dharma people** | 0.050623 |
| 997 | **great smrtijnana** | 0.050646 |
| 998 | **true nature** | 0.050671 |
| 999 | **chapter** | 0.050763 |
| 1000 | **good intention** | 0.050821 |
| 1001 | **prevent** | 0.050825 |
| 1002 | **strength** | 0.050849 |
| 1003 | **bad thought** | 0.050898 |
| 1004 | **divine** | 0.050974 |
| 1005 | **noble teacher** | 0.050977 |
| 1006 | **countless** | 0.051068 |
| 1007 | **physical** | 0.051112 |
| 1008 | **cause** | 0.051129 |
| 1009 | **blue** | 0.051151 |
| 1010 | **wind** | 0.051189 |
| 1011 | **conduct** | 0.051325 |
| 1012 | **omniscient buddhahood** | 0.051339 |
| 1013 | **pass** | 0.051368 |
| 1014 | **great fault** | 0.051370 |
| 1015 | **ordinary body** | 0.051402 |
| 1016 | **money** | 0.051416 |
| 1017 | **hell live** | 0.051473 |
| 1018 | **prostrate** | 0.051478 |
| 1019 | **practise good** | 0.051520 |
| 1020 | **boundless** | 0.051538 |
| 1021 | **cultivate** | 0.051603 |
| 1022 | **feel great affection** | 0.051629 |
| 1023 | **prajnaparamita** | 0.051658 |
| 1024 | **oneself** | 0.051671 |
| 1025 | **importance** | 0.051675 |
| 1026 | **keep** | 0.051802 |
| 1027 | **hope** | 0.051879 |
| 1028 | **trisong** | 0.052034 |
| 1029 | **wrathful mother** | 0.052055 |
| 1030 | **great middle** | 0.052161 |
| 1031 | **piece** | 0.052179 |
| 1032 | **derive great benefit** | 0.052231 |
| 1033 | **precious human** | 0.052242 |
| 1034 | **maitreya** | 0.052242 |
| 1035 | **antidote** | 0.052333 |
| 1036 | **langri** | 0.052394 |
| 1037 | **black spearman** | 0.052396 |
| 1038 | **condition** | 0.052513 |
| 1039 | **positive effect** | 0.052706 |
| 1040 | **padma** | 0.052722 |
| 1041 | **king golden crest** | 0.052806 |
| 1042 | **supreme teachers** | 0.052846 |
| 1043 | **dedicate merit** | 0.053150 |
| 1044 | **teacher forever** | 0.053279 |
| 1045 | **dharma free** | 0.053461 |
| 1046 | **kingdom** | 0.053638 |
| 1047 | **tear** | 0.053655 |
| 1048 | **dharma give** | 0.053673 |
| 1049 | **actual practice** | 0.053815 |
| 1050 | **great siddha lingje** | 0.053839 |
| 1051 | **giving dharma** | 0.053867 |
| 1052 | **profound teaching** | 0.054041 |
| 1053 | **drom tonpa** | 0.054452 |
| 1054 | **bed** | 0.054661 |
| 1055 | **debt** | 0.054695 |
| 1056 | **great avalokitdvara** | 0.054907 |
| 1057 | **true path** | 0.055065 |
| 1058 | **sixteen** | 0.055082 |
| 1059 | **abandon** | 0.055127 |
| 1060 | **small good** | 0.055294 |
| 1061 | **perfection lineage** | 0.055340 |
| 1062 | **great outer** | 0.055350 |
| 1063 | **wish** | 0.055369 |
| 1064 | **south** | 0.055401 |
| 1065 | **vajra body enter** | 0.055424 |
| 1066 | **beauty** | 0.055430 |
| 1067 | **siddhas** | 0.055457 |
| 1068 | **dharma like ambrosia** | 0.055487 |
| 1069 | **wild** | 0.055560 |
| 1070 | **slaughter** | 0.055612 |
| 1071 | **sow** | 0.055646 |
| 1072 | **golden** | 0.055648 |
| 1073 | **sexual** | 0.055649 |
| 1074 | **pure buddhafield** | 0.055665 |
| 1075 | **tantric** | 0.055672 |
| 1076 | **seek** | 0.055707 |
| 1077 | **gold** | 0.055737 |
| 1078 | **grow** | 0.055737 |
| 1079 | **master nagarjuna** | 0.055766 |
| 1080 | **impossible** | 0.055823 |
| 1081 | **exhaust** | 0.055829 |
| 1082 | **glorious root** | 0.055939 |
| 1083 | **build** | 0.055945 |
| 1084 | **wife** | 0.055951 |
| 1085 | **catch** | 0.055955 |
| 1086 | **accept** | 0.055993 |
| 1087 | **previous** | 0.056022 |
| 1088 | **increase** | 0.056027 |
| 1089 | **darkness** | 0.056032 |
| 1090 | **mentally** | 0.056042 |
| 1091 | **easily** | 0.056063 |
| 1092 | **refuge prayer** | 0.056083 |
| 1093 | **teacher venerable** | 0.056140 |
| 1094 | **past generosity** | 0.056176 |
| 1095 | **dharmodgata teaching** | 0.056198 |
| 1096 | **liberate** | 0.056217 |
| 1097 | **total** | 0.056226 |
| 1098 | **harmful act** | 0.056306 |
| 1099 | **sacred** | 0.056327 |
| 1100 | **represent** | 0.056419 |
| 1101 | **omniscient longchenpa** | 0.056504 |
| 1102 | **line** | 0.056530 |
| 1103 | **arhat** | 0.056685 |
| 1104 | **human birth** | 0.056713 |
| 1105 | **great accumulation** | 0.056838 |
| 1106 | **bird** | 0.056882 |
| 1107 | **moment mila** | 0.056949 |
| 1108 | **poison** | 0.057018 |
| 1109 | **shang rinpoche** | 0.057107 |
| 1110 | **drop** | 0.057167 |
| 1111 | **vajra posture** | 0.057190 |
| 1112 | **human world** | 0.057459 |
| 1113 | **great siddha melong** | 0.057715 |
| 1114 | **skin** | 0.057760 |
| 1115 | **great hard** | 0.057804 |
| 1116 | **great howling** | 0.057817 |
| 1117 | **precious jetsun** | 0.057822 |
| 1118 | **aspect** | 0.057825 |
| 1119 | **important people** | 0.057900 |
| 1120 | **great lotus like** | 0.057972 |
| 1121 | **perfect mind** | 0.058041 |
| 1122 | **dzogchen rinpoche** | 0.058404 |
| 1123 | **honour** | 0.058470 |
| 1124 | **great courage giving** | 0.058744 |
| 1125 | **maudgalyayana** | 0.058914 |
| 1126 | **geshe langri thangpa** | 0.059179 |
| 1127 | **wrong thought** | 0.059386 |
| 1128 | **escape** | 0.059408 |
| 1129 | **yoke** | 0.059421 |
| 1130 | **master aryadeva** | 0.059664 |
| 1131 | **being** | 0.059673 |
| 1132 | **continue** | 0.059725 |
| 1133 | **foundation** | 0.059855 |
| 1134 | **instance** | 0.059874 |
| 1135 | **advice** | 0.060133 |
| 1136 | **principle** | 0.060295 |
| 1137 | **ephemeral** | 0.060322 |
| 1138 | **bodhisattva samantabhadra ema** | 0.060355 |
| 1139 | **road** | 0.060399 |
| 1140 | **songtsen** | 0.060538 |
| 1141 | **gampo** | 0.060557 |
| 1142 | **section** | 0.060601 |
| 1143 | **merchant** | 0.060649 |
| 1144 | **bodhisattva nivara** | 0.060662 |
| 1145 | **superior** | 0.060682 |
| 1146 | **manjusrimitra** | 0.060847 |
| 1147 | **harsh** | 0.060904 |
| 1148 | **prayer beginning** | 0.061038 |
| 1149 | **ill** | 0.061042 |
| 1150 | **lotus family** | 0.061098 |
| 1151 | **milk** | 0.061101 |
| 1152 | **sake** | 0.061122 |
| 1153 | **nirmanakaya** | 0.061129 |
| 1154 | **period** | 0.061178 |
| 1155 | **endless** | 0.061186 |
| 1156 | **crowd** | 0.061197 |
| 1157 | **read** | 0.061197 |
| 1158 | **rejoice** | 0.061220 |
| 1159 | **angry** | 0.061251 |
| 1160 | **vital** | 0.061399 |
| 1161 | **know** | 0.061401 |
| 1162 | **name** | 0.061408 |
| 1163 | **apply** | 0.061410 |
| 1164 | **carry** | 0.061427 |
| 1165 | **false** | 0.061436 |
| 1166 | **invite** | 0.061459 |
| 1167 | **present human world** | 0.061471 |
| 1168 | **great translator rinchen** | 0.061472 |
| 1169 | **selfish** | 0.061503 |
| 1170 | **satisfy** | 0.061514 |
| 1171 | **sambhogakaya** | 0.061574 |
| 1172 | **awareness** | 0.061580 |
| 1173 | **pure past** | 0.061601 |
| 1174 | **primal** | 0.061606 |
| 1175 | **king padma** | 0.061679 |
| 1176 | **establish** | 0.061699 |
| 1177 | **relative bodhicitta** | 0.061820 |
| 1178 | **bodhisattvas dissolve** | 0.061838 |
| 1179 | **excellent teacher** | 0.062082 |
| 1180 | **lhodrak** | 0.062478 |
| 1181 | **stream** | 0.062499 |
| 1182 | **indian** | 0.062503 |
| 1183 | **escape death** | 0.062510 |
| 1184 | **padmasambhava** | 0.062531 |
| 1185 | **bone** | 0.062540 |
| 1186 | **vinaya** | 0.062733 |
| 1187 | **disease** | 0.062788 |
| 1188 | **natural death** | 0.062836 |
| 1189 | **present time** | 0.063020 |
| 1190 | **great guide** | 0.063066 |
| 1191 | **sunak** | 0.063087 |
| 1192 | **ordinary speech** | 0.063100 |
| 1193 | **sick people** | 0.063113 |
| 1194 | **great exuberant** | 0.063287 |
| 1195 | **numerous great** | 0.063319 |
| 1196 | **mila joy** | 0.063560 |
| 1197 | **thousand samayas** | 0.063758 |
| 1198 | **intermediate kalpa** | 0.063786 |
| 1199 | **true mother** | 0.063851 |
| 1200 | **avalokitesvara** | 0.063944 |
| 1201 | **vimalamitra** | 0.063954 |
| 1202 | **frog** | 0.064126 |
| 1203 | **indian king** | 0.064130 |
| 1204 | **wisdom nectar** | 0.064269 |
| 1205 | **image** | 0.064384 |
| 1206 | **word vajra** | 0.064552 |
| 1207 | **jewels bless** | 0.064589 |
| 1208 | **master mafijusrimitra** | 0.064795 |
| 1209 | **beat** | 0.064904 |
| 1210 | **servant** | 0.064933 |
| 1211 | **central channel** | 0.064975 |
| 1212 | **chekawa** | 0.064999 |
| 1213 | **individual** | 0.065000 |
| 1214 | **precious word empowerment** | 0.065036 |
| 1215 | **noble land** | 0.065046 |
| 1216 | **katyayana** | 0.065110 |
| 1217 | **sublime katyayana** | 0.065205 |
| 1218 | **thousand mandala** | 0.065342 |
| 1219 | **gather** | 0.065443 |
| 1220 | **weapon** | 0.065456 |
| 1221 | **compare** | 0.065552 |
| 1222 | **people practise** | 0.065780 |
| 1223 | **day tilopa** | 0.065866 |
| 1224 | **life force** | 0.065887 |
| 1225 | **perfect spiritual friend** | 0.065893 |
| 1226 | **jewel garland** | 0.065919 |
| 1227 | **great yogi** | 0.066027 |
| 1228 | **teacher face** | 0.066064 |
| 1229 | **examine** | 0.066104 |
| 1230 | **celestial realm** | 0.066287 |
| 1231 | **walk** | 0.066301 |
| 1232 | **blaze** | 0.066366 |
| 1233 | **destroy** | 0.066418 |
| 1234 | **desire buddhahood** | 0.066509 |
| 1235 | **transform** | 0.066518 |
| 1236 | **warm** | 0.066630 |
| 1237 | **female** | 0.066672 |
| 1238 | **mind carefully** | 0.066705 |
| 1239 | **secret true** | 0.066746 |
| 1240 | **skull** | 0.066785 |
| 1241 | **sight** | 0.066914 |
| 1242 | **reign** | 0.067031 |
| 1243 | **discord** | 0.067037 |
| 1244 | **supreme path** | 0.067048 |
| 1245 | **constant** | 0.067073 |
| 1246 | **samsara fall** | 0.067140 |
| 1247 | **motivation** | 0.067151 |
| 1248 | **branch** | 0.067202 |
| 1249 | **true realization** | 0.067227 |
| 1250 | **useless** | 0.067245 |
| 1251 | **equally** | 0.067265 |
| 1252 | **dry** | 0.067268 |
| 1253 | **sutra tantra** | 0.067338 |
| 1254 | **absolute bodhicitta** | 0.067349 |
| 1255 | **assembly** | 0.067389 |
| 1256 | **butter** | 0.067405 |
| 1257 | **purity** | 0.067411 |
| 1258 | **green** | 0.067429 |
| 1259 | **west** | 0.067431 |
| 1260 | **devote** | 0.067434 |
| 1261 | **skilfully** | 0.067438 |
| 1262 | **wish granting** | 0.067448 |
| 1263 | **fly** | 0.067513 |
| 1264 | **breath** | 0.067532 |
| 1265 | **separate** | 0.067561 |
| 1266 | **spontaneously** | 0.067570 |
| 1267 | **totally** | 0.067717 |
| 1268 | **process** | 0.067733 |
| 1269 | **sincere** | 0.067740 |
| 1270 | **omniscient jigme lingpa** | 0.067767 |
| 1271 | **rely** | 0.067782 |
| 1272 | **preta realm** | 0.067806 |
| 1273 | **jewels spread** | 0.067916 |
| 1274 | **genuine spiritual teacher** | 0.068008 |
| 1275 | **sharawa** | 0.068039 |
| 1276 | **longchenpa** | 0.068186 |
| 1277 | **great scholar vimalamitra** | 0.068293 |
| 1278 | **slight positive action** | 0.068336 |
| 1279 | **great ray** | 0.068352 |
| 1280 | **appearance** | 0.068571 |
| 1281 | **month** | 0.068628 |
| 1282 | **transmission** | 0.068758 |
| 1283 | **atiyoga** | 0.068765 |
| 1284 | **dark kalpas** | 0.068792 |
| 1285 | **pure intention** | 0.068796 |
| 1286 | **hundred thousand** | 0.068952 |
| 1287 | **region** | 0.068956 |
| 1288 | **run** | 0.068970 |
| 1289 | **compassionate action** | 0.069254 |
| 1290 | **kyobpa rinpoche** | 0.069445 |
| 1291 | **negative thought run** | 0.069455 |
| 1292 | **forest** | 0.069733 |
| 1293 | **believe** | 0.070206 |
| 1294 | **true meaning** | 0.070326 |
| 1295 | **wonderful teacher** | 0.070384 |
| 1296 | **great treasure** | 0.070386 |
| 1297 | **practise meditation** | 0.070445 |
| 1298 | **worldly people** | 0.070703 |
| 1299 | **virtuous practice** | 0.070781 |
| 1300 | **temple** | 0.070976 |
| 1301 | **profound atiyoga teaching** | 0.071309 |
| 1302 | **real thing** | 0.071393 |
| 1303 | **ing negative effect** | 0.071482 |
| 1304 | **heart sutra** | 0.071525 |
| 1305 | **elephant** | 0.071555 |
| 1306 | **violation** | 0.071689 |
| 1307 | **relative** | 0.071973 |
| 1308 | **spiritual companion** | 0.072038 |
| 1309 | **single good dream** | 0.072068 |
| 1310 | **dream** | 0.072226 |
| 1311 | **pure mind** | 0.072232 |
| 1312 | **conqueror sakyamuni** | 0.072313 |
| 1313 | **wear** | 0.072407 |
| 1314 | **eighty thousand people** | 0.072490 |
| 1315 | **treasure** | 0.072491 |
| 1316 | **follower** | 0.072524 |
| 1317 | **food drink** | 0.072525 |
| 1318 | **bowl** | 0.072659 |
| 1319 | **perfectly dedicate merit** | 0.072738 |
| 1320 | **side** | 0.072818 |
| 1321 | **great universal** | 0.072883 |
| 1322 | **solitary place** | 0.072995 |
| 1323 | **bodhisattva sam** | 0.073065 |
| 1324 | **live forever** | 0.073091 |
| 1325 | **undergo great** | 0.073140 |
| 1326 | **patron** | 0.073269 |
| 1327 | **field** | 0.073309 |
| 1328 | **black true** | 0.073318 |
| 1329 | **great energy** | 0.073362 |
| 1330 | **attendant** | 0.073427 |
| 1331 | **jewel chest** | 0.073568 |
| 1332 | **bring benefit** | 0.073684 |
| 1333 | **concern** | 0.073707 |
| 1334 | **summer** | 0.073931 |
| 1335 | **treat** | 0.073961 |
| 1336 | **heavy** | 0.074015 |
| 1337 | **indian master diparhkara** | 0.074028 |
| 1338 | **property** | 0.074053 |
| 1339 | **great confidence** | 0.074129 |
| 1340 | **burn** | 0.074135 |
| 1341 | **worth** | 0.074152 |
| 1342 | **lord padampa** | 0.074217 |
| 1343 | **evil mind** | 0.074270 |
| 1344 | **point lord** | 0.074311 |
| 1345 | **misconduct** | 0.074336 |
| 1346 | **chatter** | 0.074360 |
| 1347 | **terrible** | 0.074420 |
| 1348 | **length** | 0.074421 |
| 1349 | **ignorance** | 0.074518 |
| 1350 | **extraordinary teacher** | 0.074524 |
| 1351 | **physically** | 0.074608 |
| 1352 | **impure** | 0.074608 |
| 1353 | **cover** | 0.074620 |
| 1354 | **great difficulty** | 0.074633 |
| 1355 | **cave** | 0.074643 |
| 1356 | **difficulty** | 0.074646 |
| 1357 | **bow** | 0.074680 |
| 1358 | **general** | 0.074712 |
| 1359 | **knife** | 0.074716 |
| 1360 | **ability** | 0.074737 |
| 1361 | **gaya** | 0.074741 |
| 1362 | **bodh** | 0.074742 |
| 1363 | **impartiality** | 0.074795 |
| 1364 | **weak** | 0.074810 |
| 1365 | **fourth** | 0.074840 |
| 1366 | **special** | 0.074862 |
| 1367 | **consider** | 0.074865 |
| 1368 | **disappear** | 0.074867 |
| 1369 | **tendency** | 0.074883 |
| 1370 | **rid** | 0.074936 |
| 1371 | **prepare** | 0.074937 |
| 1372 | **vase** | 0.074978 |
| 1373 | **vigilance** | 0.074979 |
| 1374 | **mindfulness** | 0.075027 |
| 1375 | **vast mind** | 0.075050 |
| 1376 | **common** | 0.075067 |
| 1377 | **external** | 0.075072 |
| 1378 | **food offering** | 0.075100 |
| 1379 | **ordinary person** | 0.075182 |
| 1380 | **mind free** | 0.075205 |
| 1381 | **great elapatra** | 0.075323 |
| 1382 | **great stupa** | 0.075439 |
| 1383 | **virtuous** | 0.075500 |
| 1384 | **single teaching** | 0.075609 |
| 1385 | **great marvellous** | 0.075614 |
| 1386 | **great courage** | 0.075752 |
| 1387 | **supreme accomplishment** | 0.075815 |
| 1388 | **princess** | 0.075871 |
| 1389 | **immaculate** | 0.075919 |
| 1390 | **prince great** | 0.075931 |
| 1391 | **bright kalpa** | 0.076548 |
| 1392 | **ngokpa** | 0.077251 |
| 1393 | **powerful king** | 0.077466 |
| 1394 | **good spiritual** | 0.077522 |
| 1395 | **secret essence** | 0.077611 |
| 1396 | **distraction** | 0.077643 |
| 1397 | **santideva** | 0.077650 |
| 1398 | **great mistake** | 0.077934 |
| 1399 | **practise true** | 0.077972 |
| 1400 | **master padma** | 0.078221 |
| 1401 | **wish harm** | 0.078265 |
| 1402 | **vajradhara** | 0.078378 |
| 1403 | **great skull** | 0.078398 |
| 1404 | **tirthika teacher** | 0.078525 |
| 1405 | **cloud** | 0.078582 |
| 1406 | **garab dorje set** | 0.078643 |
| 1407 | **zangpo** | 0.078727 |
| 1408 | **ordinary death** | 0.078784 |
| 1409 | **yak** | 0.079146 |
| 1410 | **large number** | 0.079187 |
| 1411 | **statue** | 0.079674 |
| 1412 | **true teaching** | 0.079800 |
| 1413 | **geshe chengawa** | 0.079871 |
| 1414 | **unbearable compassion** | 0.080023 |
| 1415 | **village** | 0.080235 |
| 1416 | **practise cho** | 0.080376 |
| 1417 | **lower left hand** | 0.080392 |
| 1418 | **break** | 0.080544 |
| 1419 | **sravakas** | 0.080696 |
| 1420 | **great mindfulness** | 0.080922 |
| 1421 | **aspiration** | 0.081174 |
| 1422 | **good nature** | 0.081182 |
| 1423 | **limb** | 0.081189 |
| 1424 | **bring suffering** | 0.081208 |
| 1425 | **indian master** | 0.081380 |
| 1426 | **oddiyana points** | 0.081467 |
| 1427 | **day long** | 0.081623 |
| 1428 | **human speech** | 0.081794 |
| 1429 | **immense suffering** | 0.081891 |
| 1430 | **wood** | 0.081963 |
| 1431 | **shadow** | 0.081984 |
| 1432 | **obey** | 0.082087 |
| 1433 | **tsa tsa** | 0.082258 |
| 1434 | **terrify** | 0.082265 |
| 1435 | **strive** | 0.082330 |
| 1436 | **love life** | 0.082334 |
| 1437 | **lifespan** | 0.082434 |
| 1438 | **tormas** | 0.082472 |
| 1439 | **misdeed** | 0.082485 |
| 1440 | **kadampa masters** | 0.082533 |
| 1441 | **continually** | 0.082578 |
| 1442 | **request** | 0.082714 |
| 1443 | **control** | 0.082897 |
| 1444 | **health** | 0.082917 |
| 1445 | **monastic** | 0.082977 |
| 1446 | **convince** | 0.082998 |
| 1447 | **crush** | 0.083042 |
| 1448 | **great yogi virupa** | 0.083068 |
| 1449 | **clairvoyance** | 0.083089 |
| 1450 | **business** | 0.083096 |
| 1451 | **morning** | 0.083112 |
| 1452 | **noble master** | 0.083129 |
| 1453 | **time difficult** | 0.083142 |
| 1454 | **grass** | 0.083143 |
| 1455 | **noble lord** | 0.083162 |
| 1456 | **vajra sattva** | 0.083209 |
| 1457 | **seventh bodhisattva level** | 0.083209 |
| 1458 | **universal** | 0.083209 |
| 1459 | **share** | 0.083269 |
| 1460 | **talk** | 0.083287 |
| 1461 | **confident faith** | 0.083330 |
| 1462 | **cry** | 0.083349 |
| 1463 | **skilled** | 0.083368 |
| 1464 | **comfortable** | 0.083399 |
| 1465 | **entrust** | 0.083399 |
| 1466 | **drive** | 0.083444 |
| 1467 | **evening** | 0.083448 |
| 1468 | **major** | 0.083497 |
| 1469 | **single lifetime** | 0.083509 |
| 1470 | **manner** | 0.083536 |
| 1471 | **firm** | 0.083581 |
| 1472 | **yellow** | 0.083591 |
| 1473 | **indispensable** | 0.083682 |
| 1474 | **jealousy** | 0.083701 |
| 1475 | **success** | 0.083705 |
| 1476 | **decide** | 0.083721 |
| 1477 | **embodiment** | 0.083734 |
| 1478 | **immeasurable** | 0.083800 |
| 1479 | **pith** | 0.083805 |
| 1480 | **humble** | 0.083819 |
| 1481 | **sincerely** | 0.083823 |
| 1482 | **link** | 0.083842 |
| 1483 | **stand** | 0.083846 |
| 1484 | **barley** | 0.083891 |
| 1485 | **skull cup** | 0.083962 |
| 1486 | **pour** | 0.083975 |
| 1487 | **present practice** | 0.083979 |
| 1488 | **guru padma** | 0.084357 |
| 1489 | **generation phase** | 0.084528 |
| 1490 | **king virudhaka** | 0.084566 |
| 1491 | **guru padma siddhi** | 0.084673 |
| 1492 | **sublime lord** | 0.084713 |
| 1493 | **essential nature** | 0.084746 |
| 1494 | **dharmaraksita** | 0.084874 |
| 1495 | **heart essence** | 0.085173 |
| 1496 | **ordinary tree** | 0.085388 |
| 1497 | **search** | 0.085395 |
| 1498 | **people follow** | 0.085534 |
| 1499 | **representation** | 0.085825 |
| 1500 | **mila sherab gyaltsen** | 0.085834 |
| 1501 | **accomplishment mandala** | 0.085867 |
| 1502 | **pratyekabuddha** | 0.086164 |
| 1503 | **ordinary form** | 0.086240 |
| 1504 | **supreme master** | 0.086275 |
| 1505 | **human flesh** | 0.086284 |
| 1506 | **detail** | 0.086285 |
| 1507 | **corpse** | 0.086287 |
| 1508 | **true existence** | 0.086398 |
| 1509 | **seventh bodhisattva** | 0.086439 |
| 1510 | **extraordinary faith** | 0.086598 |
| 1511 | **consist** | 0.086916 |
| 1512 | **great primordial** | 0.087022 |
| 1513 | **geshe potowa** | 0.087068 |
| 1514 | **depend** | 0.087087 |
| 1515 | **important thing** | 0.087108 |
| 1516 | **food clothing** | 0.087159 |
| 1517 | **sole** | 0.087170 |
| 1518 | **god realm** | 0.087288 |
| 1519 | **innumerable kalpas** | 0.087293 |
| 1520 | **substance** | 0.087473 |
| 1521 | **indian siddha naropa** | 0.087571 |
| 1522 | **beast** | 0.087813 |
| 1523 | **robe** | 0.088063 |
| 1524 | **present teaching** | 0.088118 |
| 1525 | **eastern india** | 0.088218 |
| 1526 | **mistake** | 0.088559 |
| 1527 | **great rejoicing** | 0.088622 |
| 1528 | **kadampas** | 0.088650 |
| 1529 | **doctor** | 0.089046 |
| 1530 | **great deal** | 0.089707 |
| 1531 | **human body** | 0.089727 |
| 1532 | **extremely negative** | 0.089908 |
| 1533 | **translator** | 0.090008 |
| 1534 | **tibetan** | 0.090040 |
| 1535 | **yoga tantra** | 0.090055 |
| 1536 | **feeling** | 0.090158 |
| 1537 | **great evil doer** | 0.090336 |
| 1538 | **colour** | 0.090353 |
| 1539 | **surface** | 0.090363 |
| 1540 | **bodhisattvas undertake** | 0.090596 |
| 1541 | **jewels render** | 0.090801 |
| 1542 | **perfect kalpa** | 0.090848 |
| 1543 | **vajrayana path** | 0.091027 |
| 1544 | **medicine** | 0.091405 |
| 1545 | **central place** | 0.091419 |
| 1546 | **jowo sakyamuni** | 0.091442 |
| 1547 | **sea** | 0.091567 |
| 1548 | **great sadness** | 0.091575 |
| 1549 | **evil karma** | 0.091744 |
| 1550 | **venerable master** | 0.091835 |
| 1551 | **embrace great** | 0.091918 |
| 1552 | **manifestation** | 0.091940 |
| 1553 | **powerful secret** | 0.092064 |
| 1554 | **great moving** | 0.092064 |
| 1555 | **trouble** | 0.092090 |
| 1556 | **meal** | 0.092095 |
| 1557 | **find happiness** | 0.092157 |
| 1558 | **ninefold black cho** | 0.092220 |
| 1559 | **traveller** | 0.092444 |
| 1560 | **precious word** | 0.092546 |
| 1561 | **virtuous action** | 0.092587 |
| 1562 | **finger** | 0.092690 |
| 1563 | **avoid negative** | 0.092900 |
| 1564 | **journey** | 0.092930 |
| 1565 | **good suffer** | 0.093062 |
| 1566 | **conviction** | 0.093109 |
| 1567 | **great relish** | 0.093137 |
| 1568 | **buddhist** | 0.093188 |
| 1569 | **throat** | 0.093227 |
| 1570 | **repeat** | 0.093251 |
| 1571 | **purpose** | 0.093260 |
| 1572 | **gesture** | 0.093323 |
| 1573 | **mind workable** | 0.093388 |
| 1574 | **geshe shawopa** | 0.093478 |
| 1575 | **throw** | 0.093561 |
| 1576 | **baby** | 0.093562 |
| 1577 | **deaf** | 0.093589 |
| 1578 | **great arrogance** | 0.093590 |
| 1579 | **slip** | 0.093631 |
| 1580 | **illness** | 0.093633 |
| 1581 | **great affection** | 0.093693 |
| 1582 | **vajrapani** | 0.093713 |
| 1583 | **single hair** | 0.093768 |
| 1584 | **sand** | 0.093792 |
| 1585 | **phenomena** | 0.093828 |
| 1586 | **perfect body** | 0.093859 |
| 1587 | **body perfect** | 0.093859 |
| 1588 | **remorse** | 0.093866 |
| 1589 | **tantric samayas** | 0.093883 |
| 1590 | **holy** | 0.093902 |
| 1591 | **geshe kharak** | 0.093960 |
| 1592 | **practice transference** | 0.093972 |
| 1593 | **transference practice** | 0.093972 |
| 1594 | **cross** | 0.093988 |
| 1595 | **check** | 0.094072 |
| 1596 | **size** | 0.094125 |
| 1597 | **gradually** | 0.094142 |
| 1598 | **peaceful** | 0.094181 |
| 1599 | **simple** | 0.094256 |
| 1600 | **secret empowerment** | 0.094305 |
| 1601 | **ordinary human simply** | 0.094309 |
| 1602 | **king manicuda** | 0.094313 |
| 1603 | **highly** | 0.094316 |
| 1604 | **hunter** | 0.094317 |
| 1605 | **direct** | 0.094321 |
| 1606 | **low** | 0.094379 |
| 1607 | **hate** | 0.094408 |
| 1608 | **favourable** | 0.094442 |
| 1609 | **vital point** | 0.094496 |
| 1610 | **beg** | 0.094506 |
| 1611 | **minor** | 0.094515 |
| 1612 | **feel love** | 0.094531 |
| 1613 | **bitch** | 0.094532 |
| 1614 | **sweep** | 0.094540 |
| 1615 | **extremely negative act** | 0.094563 |
| 1616 | **difference** | 0.094566 |
| 1617 | **meritorious** | 0.094567 |
| 1618 | **celestial** | 0.094583 |
| 1619 | **caste** | 0.094588 |
| 1620 | **proper** | 0.094593 |
| 1621 | **solitary** | 0.094631 |
| 1622 | **live human** | 0.094645 |
| 1623 | **illusion** | 0.094707 |
| 1624 | **black cho** | 0.094712 |
| 1625 | **retribution** | 0.094738 |
| 1626 | **black horse lama** | 0.094746 |
| 1627 | **faithful** | 0.094756 |
| 1628 | **billion** | 0.094762 |
| 1629 | **maintain** | 0.094775 |
| 1630 | **auspicious** | 0.094813 |
| 1631 | **single negative** | 0.094831 |
| 1632 | **touch** | 0.094861 |
| 1633 | **term** | 0.094965 |
| 1634 | **time training** | 0.095055 |
| 1635 | **great renown** | 0.095063 |
| 1636 | **absolute cho** | 0.095191 |
| 1637 | **teacher explain** | 0.095250 |
| 1638 | **skill** | 0.095410 |
| 1639 | **important practice** | 0.095416 |
| 1640 | **derive great** | 0.095426 |
| 1641 | **great sincerity** | 0.095588 |
| 1642 | **great paqc** | 0.095701 |
| 1643 | **great paqqita** | 0.095759 |
| 1644 | **master dharmaraksita** | 0.096001 |
| 1645 | **practise real** | 0.096002 |
| 1646 | **write** | 0.096051 |
| 1647 | **practise taking** | 0.096240 |
| 1648 | **teacher stand** | 0.096422 |
| 1649 | **people die** | 0.096428 |
| 1650 | **teacher skilfully** | 0.096452 |
| 1651 | **hell suffer** | 0.096612 |
| 1652 | **tion** | 0.096631 |
| 1653 | **basic vehicle** | 0.096747 |
| 1654 | **sravaka** | 0.096835 |
| 1655 | **ornament** | 0.096875 |
| 1656 | **noble spiritual friend** | 0.097105 |
| 1657 | **guru sri simha** | 0.097121 |
| 1658 | **single day** | 0.097123 |
| 1659 | **arrow** | 0.097243 |
| 1660 | **city** | 0.097280 |
| 1661 | **positive thought** | 0.097438 |
| 1662 | **buddhist teaching** | 0.097554 |
| 1663 | **great gusto** | 0.097563 |
| 1664 | **great inseparability** | 0.097640 |
| 1665 | **order great** | 0.097701 |
| 1666 | **great fervour** | 0.097707 |
| 1667 | **great evenness** | 0.097709 |
| 1668 | **great pal** | 0.097717 |
| 1669 | **great equality** | 0.097717 |
| 1670 | **yeshe tsogyal** | 0.097740 |
| 1671 | **renounce taking** | 0.097805 |
| 1672 | **people die suddenly** | 0.097838 |
| 1673 | **transcendent generosity** | 0.097840 |
| 1674 | **compassionate heart** | 0.097905 |
| 1675 | **ancient** | 0.098045 |
| 1676 | **glorious vajrasattva** | 0.098087 |
| 1677 | **arrange** | 0.098349 |
| 1678 | **sorrow** | 0.098663 |
| 1679 | **mother bird taking** | 0.099149 |
| 1680 | **single tibetan** | 0.099445 |
| 1681 | **abhidharma** | 0.099487 |
| 1682 | **profound meaning** | 0.099535 |
| 1683 | **dead person** | 0.099537 |
| 1684 | **action properly** | 0.099590 |
| 1685 | **manjusri** | 0.099665 |
| 1686 | **snow** | 0.099879 |
| 1687 | **relative buddhahood** | 0.100107 |
| 1688 | **endless suffering** | 0.100144 |
| 1689 | **symbol** | 0.100175 |
| 1690 | **mantrayana tantras** | 0.100258 |
| 1691 | **gonpo** | 0.100607 |
| 1692 | **vairotsana** | 0.100609 |
| 1693 | **mount malaya** | 0.100824 |
| 1694 | **king trisongdetsen** | 0.101001 |
| 1695 | **virtue** | 0.101009 |
| 1696 | **ordinary transference** | 0.101044 |
| 1697 | **atiyoga teaching** | 0.101108 |
| 1698 | **holy teacher** | 0.101159 |
| 1699 | **stage** | 0.101194 |
| 1700 | **king golden** | 0.101299 |
| 1701 | **animal realm** | 0.101344 |
| 1702 | **goal** | 0.101532 |
| 1703 | **flow** | 0.101613 |
| 1704 | **supreme spiritual friend** | 0.101641 |
| 1705 | **people present** | 0.101693 |
| 1706 | **tongue** | 0.101726 |
| 1707 | **incomparable dagpo rinpoche** | 0.101856 |
| 1708 | **geshe kharak gomchung** | 0.101939 |
| 1709 | **lord mafijusri** | 0.102317 |
| 1710 | **king uparaja** | 0.102363 |
| 1711 | **king gomadeviya** | 0.102392 |
| 1712 | **exist** | 0.102658 |
| 1713 | **yidam** | 0.102740 |
| 1714 | **sound** | 0.102770 |
| 1715 | **profound practice** | 0.102917 |
| 1716 | **western buddhafield** | 0.103138 |
| 1717 | **mark** | 0.103228 |
| 1718 | **lamp** | 0.103287 |
| 1719 | **bit** | 0.103440 |
| 1720 | **teacher spiritual** | 0.103580 |
| 1721 | **clear sky** | 0.103667 |
| 1722 | **absolute wisdom** | 0.103695 |
| 1723 | **mila thopa** | 0.103700 |
| 1724 | **mila sherab** | 0.103704 |
| 1725 | **past positive** | 0.103852 |
| 1726 | **experience suffering** | 0.103889 |
| 1727 | **thousand million** | 0.103933 |
| 1728 | **authentic refuge vow** | 0.103957 |
| 1729 | **secret tantric samayas** | 0.104151 |
| 1730 | **ordinary giving** | 0.104218 |
| 1731 | **behave** | 0.104226 |
| 1732 | **short time** | 0.104311 |
| 1733 | **open mind** | 0.104312 |
| 1734 | **practice perfectly** | 0.104697 |
| 1735 | **hermitage** | 0.104750 |
| 1736 | **head cut** | 0.104760 |
| 1737 | **transference prayer** | 0.104928 |
| 1738 | **palm** | 0.104993 |
| 1739 | **true absolute bodhicitta** | 0.105193 |
| 1740 | **repa** | 0.105295 |
| 1741 | **bright** | 0.105317 |
| 1742 | **master tendzin** | 0.105333 |
| 1743 | **noble mafijusri** | 0.105670 |
| 1744 | **physical action** | 0.105722 |
| 1745 | **vajra speech** | 0.105784 |
| 1746 | **shepa dorje** | 0.105814 |
| 1747 | **vajra essence** | 0.105857 |
| 1748 | **profit** | 0.105943 |
| 1749 | **criticize** | 0.105987 |
| 1750 | **wander** | 0.106129 |
| 1751 | **mind completely** | 0.106141 |
| 1752 | **interest** | 0.106237 |
| 1753 | **mila adamantine** | 0.106288 |
| 1754 | **pull** | 0.106303 |
| 1755 | **immense compassion** | 0.106360 |
| 1756 | **solitude** | 0.106517 |
| 1757 | **male** | 0.106580 |
| 1758 | **air** | 0.106655 |
| 1759 | **stability** | 0.106842 |
| 1760 | **ananda** | 0.106884 |
| 1761 | **experience immense suffering** | 0.106921 |
| 1762 | **eighteen** | 0.106931 |
| 1763 | **winter** | 0.106962 |
| 1764 | **deeply** | 0.107003 |
| 1765 | **conclusion** | 0.107030 |
| 1766 | **loose** | 0.107100 |
| 1767 | **army** | 0.107114 |
| 1768 | **inspire** | 0.107246 |
| 1769 | **taste** | 0.107314 |
| 1770 | **naturally** | 0.107449 |
| 1771 | **samsaric** | 0.107472 |
| 1772 | **worst** | 0.107502 |
| 1773 | **butcher** | 0.107522 |
| 1774 | **perfectly pure intention** | 0.107534 |
| 1775 | **endlessly** | 0.107555 |
| 1776 | **worthless** | 0.107567 |
| 1777 | **covetousness** | 0.107598 |
| 1778 | **ripen** | 0.107624 |
| 1779 | **trace** | 0.107658 |
| 1780 | **unpleasant** | 0.107670 |
| 1781 | **capable** | 0.107673 |
| 1782 | **permit** | 0.107674 |
| 1783 | **behaviour** | 0.107761 |
| 1784 | **tsampa** | 0.107828 |
| 1785 | **careful** | 0.107831 |
| 1786 | **visit** | 0.107839 |
| 1787 | **tiny** | 0.107853 |
| 1788 | **pay** | 0.107870 |
| 1789 | **company** | 0.107879 |
| 1790 | **finish** | 0.107895 |
| 1791 | **achieve** | 0.107923 |
| 1792 | **resolve** | 0.107927 |
| 1793 | **tooth** | 0.107960 |
| 1794 | **mouthful** | 0.108008 |
| 1795 | **travel** | 0.108012 |
| 1796 | **book** | 0.108034 |
| 1797 | **endure** | 0.108036 |
| 1798 | **sentient** | 0.108058 |
| 1799 | **solid** | 0.108092 |
| 1800 | **look** | 0.108107 |
| 1801 | **absolutely** | 0.108113 |
| 1802 | **tiniest** | 0.108121 |
| 1803 | **peace** | 0.108122 |
| 1804 | **head lama** | 0.108132 |
| 1805 | **spark** | 0.108183 |
| 1806 | **summit** | 0.108186 |
| 1807 | **refuse** | 0.108190 |
| 1808 | **save** | 0.108201 |
| 1809 | **whatsoever** | 0.108204 |
| 1810 | **concentrate** | 0.108208 |
| 1811 | **trade** | 0.108214 |
| 1812 | **generally** | 0.108258 |
| 1813 | **confusion** | 0.108287 |
| 1814 | **degenerate** | 0.108300 |
| 1815 | **remedy** | 0.108324 |
| 1816 | **beneficial** | 0.108327 |
| 1817 | **inseparable** | 0.108342 |
| 1818 | **silken** | 0.108352 |
| 1819 | **potential** | 0.108359 |
| 1820 | **ceremony** | 0.108364 |
| 1821 | **identical** | 0.108367 |
| 1822 | **rainbow** | 0.108367 |
| 1823 | **cosmos** | 0.108378 |
| 1824 | **posture** | 0.108410 |
| 1825 | **correct** | 0.108413 |
| 1826 | **outward** | 0.108435 |
| 1827 | **slightly** | 0.108481 |
| 1828 | **seal** | 0.108488 |
| 1829 | **transfer** | 0.108528 |
| 1830 | **invocation** | 0.108680 |
| 1831 | **good worldly** | 0.109074 |
| 1832 | **syllable hum** | 0.109327 |
| 1833 | **ogress** | 0.109331 |
| 1834 | **chengawa** | 0.109422 |
| 1835 | **asanga** | 0.109476 |
| 1836 | **famous** | 0.109560 |
| 1837 | **miraculous power** | 0.109895 |
| 1838 | **profoundly secret true** | 0.110304 |
| 1839 | **steady** | 0.110343 |
| 1840 | **pure realm** | 0.110366 |
| 1841 | **habitual** | 0.110437 |
| 1842 | **brahma heavens** | 0.110468 |
| 1843 | **stupa** | 0.110471 |
| 1844 | **attain enlightenment** | 0.110476 |
| 1845 | **guru sri** | 0.110490 |
| 1846 | **principal** | 0.110506 |
| 1847 | **marvellous** | 0.110709 |
| 1848 | **lotus light** | 0.110740 |
| 1849 | **tendzin** | 0.110807 |
| 1850 | **pure meaning** | 0.110915 |
| 1851 | **glorious protector** | 0.110944 |
| 1852 | **lack food** | 0.111150 |
| 1853 | **red light** | 0.111302 |
| 1854 | **powerful positive act** | 0.112237 |
| 1855 | **basic** | 0.112772 |
| 1856 | **vajra speech enter** | 0.112838 |
| 1857 | **rule** | 0.112965 |
| 1858 | **rinchen zangpo** | 0.113100 |
| 1859 | **wise** | 0.113293 |
| 1860 | **present day** | 0.113566 |
| 1861 | **real meaning** | 0.114211 |
| 1862 | **monastery** | 0.114493 |
| 1863 | **king mandhatri** | 0.114522 |
| 1864 | **jowo ben** | 0.114651 |
| 1865 | **extraordinary secret** | 0.114887 |
| 1866 | **universal king** | 0.115016 |
| 1867 | **pure path** | 0.115301 |
| 1868 | **hrih** | 0.115355 |
| 1869 | **find tilopa** | 0.115606 |
| 1870 | **mind training** | 0.115722 |
| 1871 | **master tendzin chopel** | 0.116170 |
| 1872 | **jetsun rangrik repa** | 0.116193 |
| 1873 | **single prostration** | 0.116446 |
| 1874 | **master jetari** | 0.116468 |
| 1875 | **excellent mountain** | 0.116712 |
| 1876 | **conditioning effect** | 0.116865 |
| 1877 | **white lotus** | 0.116873 |
| 1878 | **buddhas body** | 0.116993 |
| 1879 | **false spiritual friend** | 0.117021 |
| 1880 | **innumerable hell** | 0.117068 |
| 1881 | **wall** | 0.117169 |
| 1882 | **action slip** | 0.117431 |
| 1883 | **danger** | 0.117540 |
| 1884 | **geshe langri** | 0.117975 |
| 1885 | **precious mountain** | 0.117988 |
| 1886 | **shoot** | 0.117995 |
| 1887 | **symbolize** | 0.118111 |
| 1888 | **lightly small good** | 0.118265 |
| 1889 | **mount merus** | 0.118358 |
| 1890 | **authentic teaching** | 0.118401 |
| 1891 | **practise generosity** | 0.118571 |
| 1892 | **single lama** | 0.118615 |
| 1893 | **perfect faith** | 0.118889 |
| 1894 | **head call** | 0.118985 |
| 1895 | **absolute bodhicitta present** | 0.119196 |
| 1896 | **eastern buddhafield** | 0.119404 |
| 1897 | **qualified teacher** | 0.119415 |
| 1898 | **true bodhicitta** | 0.119463 |
| 1899 | **dog** | 0.119583 |
| 1900 | **lita naropa** | 0.119828 |
| 1901 | **vast path** | 0.119987 |
| 1902 | **gracious root** | 0.120037 |
| 1903 | **hevajra tantra** | 0.120214 |
| 1904 | **realize emptiness** | 0.120375 |
| 1905 | **battle** | 0.120540 |
| 1906 | **master diparhkara** | 0.120816 |
| 1907 | **dodrup chen** | 0.120836 |
| 1908 | **occur** | 0.120972 |
| 1909 | **language** | 0.121017 |
| 1910 | **follow sakyamuni** | 0.121570 |
| 1911 | **session** | 0.121594 |
| 1912 | **fit** | 0.121798 |
| 1913 | **drom** | 0.122171 |
| 1914 | **refer** | 0.122194 |
| 1915 | **husband** | 0.122278 |
| 1916 | **commitment** | 0.122383 |
| 1917 | **achieve buddhahood** | 0.122630 |
| 1918 | **plain** | 0.122724 |
| 1919 | **red mountain palace** | 0.122869 |
| 1920 | **weight** | 0.122957 |
| 1921 | **lot** | 0.122978 |
| 1922 | **steal** | 0.123041 |
| 1923 | **shoulder** | 0.123066 |
| 1924 | **lap** | 0.123164 |
| 1925 | **hit** | 0.123401 |
| 1926 | **bell** | 0.123449 |
| 1927 | **ride** | 0.123545 |
| 1928 | **ambrosia** | 0.123573 |
| 1929 | **expression** | 0.123604 |
| 1930 | **lip** | 0.123628 |
| 1931 | **fritter life** | 0.123644 |
| 1932 | **combine** | 0.123800 |
| 1933 | **crime** | 0.123834 |
| 1934 | **disc** | 0.123847 |
| 1935 | **genuine** | 0.123861 |
| 1936 | **precious metal** | 0.124011 |
| 1937 | **phoney lama** | 0.124021 |
| 1938 | **trap** | 0.124388 |
| 1939 | **country** | 0.124497 |
| 1940 | **stupid** | 0.124593 |
| 1941 | **mother bird** | 0.124625 |
| 1942 | **give rise** | 0.124683 |
| 1943 | **hungry** | 0.124765 |
| 1944 | **forget** | 0.124881 |
| 1945 | **cattle** | 0.124980 |
| 1946 | **execution** | 0.124980 |
| 1947 | **altogether** | 0.125045 |
| 1948 | **opposite** | 0.125124 |
| 1949 | **layman** | 0.125172 |
| 1950 | **calf** | 0.125182 |
| 1951 | **nepal** | 0.125223 |
| 1952 | **reason guru** | 0.125223 |
| 1953 | **poisonous** | 0.125227 |
| 1954 | **glad** | 0.125253 |
| 1955 | **medicinal** | 0.125254 |
| 1956 | **sweet** | 0.125276 |
| 1957 | **atra** | 0.125341 |
| 1958 | **ready** | 0.125358 |
| 1959 | **meeting** | 0.125390 |
| 1960 | **final** | 0.125397 |
| 1961 | **till** | 0.125423 |
| 1962 | **fat** | 0.125425 |
| 1963 | **answer** | 0.125433 |
| 1964 | **pus** | 0.125436 |
| 1965 | **evil rebirth** | 0.125445 |
| 1966 | **sad** | 0.125498 |
| 1967 | **discover** | 0.125529 |
| 1968 | **infinity** | 0.125545 |
| 1969 | **attach** | 0.125608 |
| 1970 | **repay** | 0.125633 |
| 1971 | **violent** | 0.125682 |
| 1972 | **prey** | 0.125689 |
| 1973 | **harmful negative** | 0.125698 |
| 1974 | **single drop** | 0.125710 |
| 1975 | **focus** | 0.125723 |
| 1976 | **application** | 0.125733 |
| 1977 | **giant** | 0.125791 |
| 1978 | **everyday** | 0.125849 |
| 1979 | **mention** | 0.125851 |
| 1980 | **poverty** | 0.125851 |
| 1981 | **dear** | 0.125878 |
| 1982 | **magical** | 0.125891 |
| 1983 | **let** | 0.125893 |
| 1984 | **acquire** | 0.125898 |
| 1985 | **relate** | 0.125914 |
| 1986 | **good karma** | 0.125926 |
| 1987 | **daily** | 0.125952 |
| 1988 | **precious wheel** | 0.125978 |
| 1989 | **add** | 0.125986 |
| 1990 | **primordial** | 0.126075 |
| 1991 | **oral** | 0.126143 |
| 1992 | **local people** | 0.126178 |
| 1993 | **tingdzin zangpo** | 0.126198 |
| 1994 | **entire life** | 0.126415 |
| 1995 | **voice** | 0.126585 |
| 1996 | **worldly activity** | 0.126721 |
| 1997 | **fight** | 0.127008 |
| 1998 | **mighty** | 0.127157 |
| 1999 | **cow** | 0.127380 |
| 2000 | **china** | 0.127503 |
| 2001 | **cling** | 0.127586 |
| 2002 | **ordinary worldly** | 0.127745 |
| 2003 | **death finally** | 0.127977 |
| 2004 | **powerful people** | 0.128025 |
| 2005 | **naropa set** | 0.128204 |
| 2006 | **dangerous** | 0.128285 |
| 2007 | **moon lamp sutra** | 0.128304 |
| 2008 | **young brahmin** | 0.128490 |
| 2009 | **innate absolute wisdom** | 0.128653 |
| 2010 | **sutra pisaka** | 0.128867 |
| 2011 | **auspicious day** | 0.128927 |
| 2012 | **inexhaustible** | 0.129001 |
| 2013 | **noble path** | 0.129001 |
| 2014 | **jetsun shepa** | 0.129023 |
| 2015 | **determine** | 0.129065 |
| 2016 | **watch** | 0.129108 |
| 2017 | **ultimate cho** | 0.129331 |
| 2018 | **good age** | 0.129400 |
| 2019 | **mind enter** | 0.129431 |
| 2020 | **eastern** | 0.129479 |
| 2021 | **prince** | 0.129664 |
| 2022 | **lord suvarl** | 0.130111 |
| 2023 | **lord suvarnadvipa** | 0.130115 |
| 2024 | **pronged vajra** | 0.130217 |
| 2025 | **tathagata family** | 0.130307 |
| 2026 | **vajra core teaching** | 0.130352 |
| 2027 | **wonderful teaching** | 0.130447 |
| 2028 | **bodhicitta free** | 0.130537 |
| 2029 | **master chegom** | 0.130586 |
| 2030 | **tsang** | 0.130748 |
| 2031 | **period tibet** | 0.131028 |
| 2032 | **purnakasyapa** | 0.131041 |
| 2033 | **ravati** | 0.131104 |
| 2034 | **master hastibhala** | 0.131188 |
| 2035 | **spearman** | 0.131225 |
| 2036 | **perfect horse** | 0.131310 |
| 2037 | **gyalse rinpoche** | 0.131479 |
| 2038 | **joyous** | 0.131719 |
| 2039 | **absolute teaching** | 0.131739 |
| 2040 | **ordinary god** | 0.131814 |
| 2041 | **black horse** | 0.131989 |
| 2042 | **gyaltsen** | 0.132238 |
| 2043 | **array** | 0.132297 |
| 2044 | **shang** | 0.132308 |
| 2045 | **refuge vow** | 0.132348 |
| 2046 | **secret tantric** | 0.132361 |
| 2047 | **excellent people** | 0.132404 |
| 2048 | **bodhicitta present** | 0.132422 |
| 2049 | **yeshe** | 0.132532 |
| 2050 | **time immeasurable** | 0.132537 |
| 2051 | **tsogyal** | 0.132549 |
| 2052 | **mantra tradition** | 0.132680 |
| 2053 | **short life** | 0.132854 |
| 2054 | **samye** | 0.132866 |
| 2055 | **khampa** | 0.133200 |
| 2056 | **bodhicitta vow** | 0.133321 |
| 2057 | **league** | 0.133526 |
| 2058 | **malaya** | 0.133577 |
| 2059 | **maitriyogi** | 0.133613 |
| 2060 | **wisdom free** | 0.133778 |
| 2061 | **tirthika** | 0.133959 |
| 2062 | **rinchen** | 0.134083 |
| 2063 | **mantra mandala** | 0.134184 |
| 2064 | **lady** | 0.134336 |
| 2065 | **blind man** | 0.134436 |
| 2066 | **perna** | 0.134442 |
| 2067 | **door** | 0.134550 |
| 2068 | **practice patience** | 0.134756 |
| 2069 | **mind turn** | 0.134760 |
| 2070 | **vajrapar** | 0.134782 |
| 2071 | **supreme tilopa** | 0.134786 |
| 2072 | **pisaka** | 0.134799 |
| 2073 | **sri** | 0.134858 |
| 2074 | **mafijusri** | 0.134861 |
| 2075 | **emaho** | 0.134884 |
| 2076 | **situation** | 0.134961 |
| 2077 | **dzogchen** | 0.134998 |
| 2078 | **chen** | 0.135022 |
| 2079 | **dakini** | 0.135195 |
| 2080 | **authentic vajra** | 0.135243 |
| 2081 | **foolish** | 0.135321 |
| 2082 | **symbol lineage** | 0.135421 |
| 2083 | **sarhsara fritter life** | 0.135684 |
| 2084 | **ultimate refuge** | 0.135824 |
| 2085 | **bodhicitta meditation** | 0.136156 |
| 2086 | **negative karmic result** | 0.136162 |
| 2087 | **great scholar trakpa** | 0.136372 |
| 2088 | **mahayana sutras** | 0.136693 |
| 2089 | **back** | 0.136707 |
| 2090 | **absolute truth** | 0.136803 |
| 2091 | **vehicle tradition** | 0.136818 |
| 2092 | **sovereign** | 0.136841 |
| 2093 | **step** | 0.137040 |
| 2094 | **pandita** | 0.137159 |
| 2095 | **ignorant people follow** | 0.137286 |
| 2096 | **degenerate time** | 0.137647 |
| 2097 | **western** | 0.137829 |
| 2098 | **lifestyle** | 0.137981 |
| 2099 | **protector nagarjuna** | 0.138068 |
| 2100 | **perform transference** | 0.138087 |
| 2101 | **sky yoga** | 0.138126 |
| 2102 | **people lack** | 0.138538 |
| 2103 | **find fault** | 0.138560 |
| 2104 | **owner** | 0.138586 |
| 2105 | **time onwards** | 0.138740 |
| 2106 | **waste time** | 0.138828 |
| 2107 | **aim** | 0.138854 |
| 2108 | **error** | 0.139152 |
| 2109 | **action consistent** | 0.139301 |
| 2110 | **lita** | 0.139439 |
| 2111 | **dry land** | 0.139732 |
| 2112 | **cushion** | 0.139773 |
| 2113 | **ment** | 0.139807 |
| 2114 | **jetsun rangrik** | 0.139894 |
| 2115 | **venerable geshe** | 0.140395 |
| 2116 | **delusion** | 0.140850 |
| 2117 | **victim** | 0.140929 |
| 2118 | **good listening** | 0.141400 |
| 2119 | **srona** | 0.141657 |
| 2120 | **connection** | 0.141701 |
| 2121 | **nun** | 0.141716 |
| 2122 | **omniscient state** | 0.141793 |
| 2123 | **rival** | 0.141849 |
| 2124 | **relative good** | 0.141855 |
| 2125 | **strong mind** | 0.141955 |
| 2126 | **root text** | 0.141998 |
| 2127 | **practice train** | 0.142057 |
| 2128 | **melt** | 0.142119 |
| 2129 | **present work** | 0.142132 |
| 2130 | **upwards** | 0.142150 |
| 2131 | **thought cease** | 0.142236 |
| 2132 | **good advice** | 0.142274 |
| 2133 | **hill** | 0.142410 |
| 2134 | **good dream** | 0.142425 |
| 2135 | **poison jetsun** | 0.142493 |
| 2136 | **material giving** | 0.142902 |
| 2137 | **meditate persistently** | 0.142949 |
| 2138 | **nachung tonpa** | 0.143041 |
| 2139 | **father mother** | 0.143178 |
| 2140 | **ordinary people pretend** | 0.143462 |
| 2141 | **master alive** | 0.143665 |
| 2142 | **encounter** | 0.143809 |
| 2143 | **religious king** | 0.143820 |
| 2144 | **ordinary people partake** | 0.143852 |
| 2145 | **cease** | 0.143959 |
| 2146 | **gyalpo** | 0.144073 |
| 2147 | **destruction** | 0.144104 |
| 2148 | **shearing time** | 0.144730 |
| 2149 | **people today** | 0.144745 |
| 2150 | **time lift** | 0.145055 |
| 2151 | **rope** | 0.145123 |
| 2152 | **onwards** | 0.145407 |
| 2153 | **pit** | 0.145425 |
| 2154 | **perfect happiness** | 0.145480 |
| 2155 | **waste** | 0.145488 |
| 2156 | **quarrel** | 0.145701 |
| 2157 | **needle** | 0.145864 |
| 2158 | **transcendent concentration** | 0.145871 |
| 2159 | **bean** | 0.146072 |
| 2160 | **approach practice** | 0.146146 |
| 2161 | **smell** | 0.146172 |
| 2162 | **girl** | 0.146325 |
| 2163 | **forehead** | 0.146358 |
| 2164 | **multitude** | 0.146440 |
| 2165 | **perfectly dedicate** | 0.146571 |
| 2166 | **people imagine** | 0.146739 |
| 2167 | **periods** | 0.146828 |
| 2168 | **reduce** | 0.146889 |
| 2169 | **siddha naropa** | 0.146982 |
| 2170 | **deer** | 0.147018 |
| 2171 | **display** | 0.147043 |
| 2172 | **volume** | 0.147096 |
| 2173 | **potowa** | 0.147274 |
| 2174 | **vast attitude** | 0.147463 |
| 2175 | **strike** | 0.147519 |
| 2176 | **unpredictable** | 0.147529 |
| 2177 | **hole** | 0.147612 |
| 2178 | **prosperous** | 0.147887 |
| 2179 | **terror** | 0.148018 |
| 2180 | **worm** | 0.148067 |
| 2181 | **bear death** | 0.148091 |
| 2182 | **wool** | 0.148105 |
| 2183 | **hot food** | 0.148185 |
| 2184 | **harmful past** | 0.148194 |
| 2185 | **distant** | 0.148301 |
| 2186 | **produce** | 0.148306 |
| 2187 | **seventh** | 0.148308 |
| 2188 | **water tormas** | 0.148361 |
| 2189 | **growth** | 0.148398 |
| 2190 | **cook** | 0.148465 |
| 2191 | **perfect dedication** | 0.148472 |
| 2192 | **meditative** | 0.148483 |
| 2193 | **distinguish** | 0.148531 |
| 2194 | **choose** | 0.148531 |
| 2195 | **agony** | 0.148567 |
| 2196 | **trunk** | 0.148719 |
| 2197 | **warm flesh** | 0.148728 |
| 2198 | **sharp** | 0.148741 |
| 2199 | **good tea** | 0.148742 |
| 2200 | **ruin** | 0.148767 |
| 2201 | **omniscience** | 0.148789 |
| 2202 | **nonetheless** | 0.148830 |
| 2203 | **tomorrow** | 0.148880 |
| 2204 | **quest** | 0.148891 |
| 2205 | **sell** | 0.148906 |
| 2206 | **weeping** | 0.148916 |
| 2207 | **spot** | 0.148922 |
| 2208 | **par** | 0.148934 |
| 2209 | **cure** | 0.148960 |
| 2210 | **heavenly** | 0.148967 |
| 2211 | **suppose** | 0.148971 |
| 2212 | **exceptional** | 0.148972 |
| 2213 | **spite** | 0.148983 |
| 2214 | **disillusionment** | 0.148992 |
| 2215 | **mar** | 0.149021 |
| 2216 | **joyous realm** | 0.149053 |
| 2217 | **gratitude** | 0.149070 |
| 2218 | **floor** | 0.149095 |
| 2219 | **threaten** | 0.149107 |
| 2220 | **help** | 0.149113 |
| 2221 | **leather** | 0.149114 |
| 2222 | **circle** | 0.149141 |
| 2223 | **ruler** | 0.149143 |
| 2224 | **plenty** | 0.149148 |
| 2225 | **padampa sangye heard** | 0.149169 |
| 2226 | **crucial** | 0.149191 |
| 2227 | **join** | 0.149194 |
| 2228 | **soft** | 0.149201 |
| 2229 | **busy** | 0.149202 |
| 2230 | **atriya** | 0.149228 |
| 2231 | **jealous** | 0.149232 |
| 2232 | **boat** | 0.149234 |
| 2233 | **boatman** | 0.149237 |
| 2234 | **wait** | 0.149251 |
| 2235 | **distinction** | 0.149259 |
| 2236 | **defeat** | 0.149289 |
| 2237 | **attack** | 0.149302 |
| 2238 | **possess** | 0.149307 |
| 2239 | **reject** | 0.149318 |
| 2240 | **dear body** | 0.149336 |
| 2241 | **mastery** | 0.149355 |
| 2242 | **unsurpassable** | 0.149369 |
| 2243 | **supreme wisdom** | 0.149396 |
| 2244 | **cloth** | 0.149401 |
| 2245 | **visible** | 0.149404 |
| 2246 | **grasp** | 0.149407 |
| 2247 | **shame** | 0.149437 |
| 2248 | **mirror** | 0.149438 |
| 2249 | **soup** | 0.149451 |
| 2250 | **progress** | 0.149456 |
| 2251 | **abuse** | 0.149468 |
| 2252 | **press** | 0.149501 |
| 2253 | **incomparable** | 0.149501 |
| 2254 | **oil** | 0.149503 |
| 2255 | **fresh** | 0.149517 |
| 2256 | **omniscient jigme** | 0.149522 |
| 2257 | **marici** | 0.149537 |
| 2258 | **naked** | 0.149556 |
| 2259 | **consult** | 0.149592 |
| 2260 | **takaya** | 0.149598 |
| 2261 | **swiftly** | 0.149604 |
| 2262 | **clarity** | 0.149632 |
| 2263 | **dissolution** | 0.149662 |
| 2264 | **intense practice** | 0.149813 |
| 2265 | **prince great courage** | 0.150240 |
| 2266 | **damchen** | 0.150270 |
| 2267 | **feel natural love** | 0.150404 |
| 2268 | **ati** | 0.150427 |
| 2269 | **kushab rinpoche** | 0.150435 |
| 2270 | **rinpoche shenpen** | 0.150435 |
| 2271 | **geshe chekawa** | 0.150630 |
| 2272 | **find food** | 0.150648 |
| 2273 | **adhicitta** | 0.150657 |
| 2274 | **dodrup** | 0.150831 |
| 2275 | **split** | 0.150993 |
| 2276 | **completely pure** | 0.151177 |
| 2277 | **day chengawa** | 0.151324 |
| 2278 | **single year** | 0.151512 |
| 2279 | **superior mind** | 0.151587 |
| 2280 | **sri simha** | 0.152241 |
| 2281 | **western india** | 0.153455 |
| 2282 | **turquoise** | 0.153635 |
| 2283 | **joyous kalpa** | 0.154030 |
| 2284 | **material offering** | 0.154136 |
| 2285 | **mind awareness** | 0.154175 |
| 2286 | **adverse** | 0.154304 |
| 2287 | **laziness** | 0.154540 |
| 2288 | **present human** | 0.154632 |
| 2289 | **sadaprarudita cut open** | 0.154654 |
| 2290 | **swift path** | 0.154672 |
| 2291 | **act positive** | 0.154729 |
| 2292 | **consume** | 0.154789 |
| 2293 | **time swimming** | 0.154879 |
| 2294 | **geshe khampa** | 0.154917 |
| 2295 | **illusory body** | 0.154969 |
| 2296 | **teaching sror** | 0.155099 |
| 2297 | **captain** | 0.155150 |
| 2298 | **courage** | 0.155256 |
| 2299 | **geshe khampa lungpa** | 0.155285 |
| 2300 | **wrong food** | 0.155483 |
| 2301 | **queen** | 0.155583 |
| 2302 | **state free** | 0.155770 |
| 2303 | **single person** | 0.155878 |
| 2304 | **heating hell** | 0.155978 |
| 2305 | **asariga** | 0.156255 |
| 2306 | **similarly** | 0.156284 |
| 2307 | **victory** | 0.156416 |
| 2308 | **long run** | 0.156440 |
| 2309 | **long term** | 0.156726 |
| 2310 | **main practice train** | 0.156751 |
| 2311 | **rotten** | 0.156784 |
| 2312 | **perfect view** | 0.156794 |
| 2313 | **mind totally** | 0.156864 |
| 2314 | **sincere mind** | 0.156925 |
| 2315 | **machik** | 0.156950 |
| 2316 | **wrong direction** | 0.156960 |
| 2317 | **spontaneous** | 0.156990 |
| 2318 | **single prayer** | 0.157130 |
| 2319 | **thousand bad** | 0.157608 |
| 2320 | **excellent kalpa** | 0.157704 |
| 2321 | **day day** | 0.157974 |
| 2322 | **kalpas time** | 0.158025 |
| 2323 | **moment bring** | 0.158068 |
| 2324 | **present state** | 0.158071 |
| 2325 | **path empowerment** | 0.158258 |
| 2326 | **authentic realization** | 0.158261 |
| 2327 | **central region** | 0.158331 |
| 2328 | **dorje set** | 0.158759 |
| 2329 | **perfect spiritual** | 0.158785 |
| 2330 | **distant past** | 0.159418 |
| 2331 | **sexual misconduct** | 0.159565 |
| 2332 | **vajra recitation** | 0.160408 |
| 2333 | **bring happiness** | 0.160514 |
| 2334 | **good doctor** | 0.160539 |
| 2335 | **case death** | 0.160573 |
| 2336 | **precious supreme** | 0.160719 |
| 2337 | **leavingjetsun mila** | 0.160892 |
| 2338 | **askedjetsun mila** | 0.160982 |
| 2339 | **death suddenly** | 0.160986 |
| 2340 | **true benefit** | 0.161415 |
| 2341 | **sublime nagarjuna** | 0.161955 |
| 2342 | **body speech** | 0.162562 |
| 2343 | **sakyas** | 0.162842 |
| 2344 | **cutter sutra** | 0.162932 |
| 2345 | **gonpo dorje** | 0.162988 |
| 2346 | **single grain** | 0.162991 |
| 2347 | **vast ocean** | 0.163522 |
| 2348 | **perfect vase** | 0.163565 |
| 2349 | **mind slip** | 0.163620 |
| 2350 | **omniscient primal wisdom** | 0.164082 |
| 2351 | **past perfectly** | 0.164276 |
| 2352 | **true primal wisdom** | 0.164813 |
| 2353 | **perfect secluded place** | 0.165102 |
| 2354 | **dakini yeshe tsogyal** | 0.165718 |
| 2355 | **live incalculably long** | 0.165787 |
| 2356 | **golden wheel** | 0.165914 |
| 2357 | **good meal** | 0.166955 |
| 2358 | **infinite buddhafield** | 0.167053 |
| 2359 | **golden vajra** | 0.167334 |
| 2360 | **mipham gonpo** | 0.167965 |
| 2361 | **ordinary folk** | 0.168118 |
| 2362 | **attachment hatred** | 0.168269 |
| 2363 | **castle** | 0.168387 |
| 2364 | **laughter** | 0.168434 |
| 2365 | **ati vehicle** | 0.168458 |
| 2366 | **vajra bhumi** | 0.168694 |
| 2367 | **vajra rekhe** | 0.168695 |
| 2368 | **emulate** | 0.168840 |
| 2369 | **central buddhafield** | 0.168972 |
| 2370 | **scavenger offering** | 0.169007 |
| 2371 | **unsurpassable secret** | 0.169244 |
| 2372 | **jowo river** | 0.169468 |
| 2373 | **affliction** | 0.169919 |
| 2374 | **adamantine** | 0.169947 |
| 2375 | **feast** | 0.170151 |
| 2376 | **lingje repa** | 0.170227 |
| 2377 | **innate** | 0.170316 |
| 2378 | **dwell** | 0.170475 |
| 2379 | **perfect lake** | 0.170480 |
| 2380 | **manifestation garab dorje** | 0.170648 |
| 2381 | **bodhicitta arise** | 0.170677 |
| 2382 | **completely sincere mind** | 0.170695 |
| 2383 | **yogis** | 0.170699 |
| 2384 | **vajra throne** | 0.170843 |
| 2385 | **life slip** | 0.171104 |
| 2386 | **compassionate wisdom** | 0.171226 |
| 2387 | **task** | 0.171580 |
| 2388 | **find freedom** | 0.171594 |
| 2389 | **star** | 0.171685 |
| 2390 | **recognize suffering** | 0.171987 |
| 2391 | **garland** | 0.172031 |
| 2392 | **correspond** | 0.172090 |
| 2393 | **omniscient longchen** | 0.172195 |
| 2394 | **naga** | 0.172251 |
| 2395 | **ship** | 0.172654 |
| 2396 | **cost** | 0.172671 |
| 2397 | **dorje gyaltsen** | 0.172837 |
| 2398 | **chagme rinpoche** | 0.172853 |
| 2399 | **perfectly practise** | 0.172898 |
| 2400 | **benefactor** | 0.172978 |
| 2401 | **occasion** | 0.173040 |
| 2402 | **sadaprarudita set** | 0.173152 |
| 2403 | **lotus hat** | 0.173207 |
| 2404 | **tea** | 0.173215 |
| 2405 | **lake kutra** | 0.173363 |
| 2406 | **people spend** | 0.173383 |
| 2407 | **attainment** | 0.173552 |
| 2408 | **refuge simply** | 0.173563 |
| 2409 | **mental suffering** | 0.173645 |
| 2410 | **rigdzin changchub dorje** | 0.173799 |
| 2411 | **single point** | 0.173896 |
| 2412 | **sattva hum** | 0.174020 |
| 2413 | **sincere practice** | 0.174187 |
| 2414 | **decline** | 0.174566 |
| 2415 | **hot metal** | 0.174667 |
| 2416 | **nirvana sutra** | 0.174790 |
| 2417 | **red blood lake** | 0.174867 |
| 2418 | **measure** | 0.175002 |
| 2419 | **content** | 0.175501 |
| 2420 | **week** | 0.175504 |
| 2421 | **question** | 0.175558 |
| 2422 | **fool** | 0.175572 |
| 2423 | **gem** | 0.175592 |
| 2424 | **gardens** | 0.175720 |
| 2425 | **type** | 0.175937 |
| 2426 | **develop compassion** | 0.175997 |
| 2427 | **true happiness** | 0.176005 |
| 2428 | **shore** | 0.176023 |
| 2429 | **gift** | 0.176150 |
| 2430 | **vessel** | 0.176160 |
| 2431 | **hang** | 0.176413 |
| 2432 | **technique** | 0.176554 |
| 2433 | **mantra recitation** | 0.176714 |
| 2434 | **wisdom empowerment** | 0.176743 |
| 2435 | **fortunate son** | 0.176977 |
| 2436 | **smrtijnana** | 0.177135 |
| 2437 | **factor** | 0.177135 |
| 2438 | **meet marpa** | 0.177166 |
| 2439 | **word empowerment** | 0.177474 |
| 2440 | **spring** | 0.177493 |
| 2441 | **pure water** | 0.177540 |
| 2442 | **thousand prelimi** | 0.177916 |
| 2443 | **precious lineage** | 0.177954 |
| 2444 | **sutras speak** | 0.178033 |
| 2445 | **perfectly complete** | 0.178131 |
| 2446 | **war** | 0.178143 |
| 2447 | **sincere faith** | 0.178178 |
| 2448 | **whip** | 0.178244 |
| 2449 | **heart blood** | 0.178375 |
| 2450 | **millstone** | 0.178376 |
| 2451 | **describe** | 0.178542 |
| 2452 | **command** | 0.178589 |
| 2453 | **outer cho** | 0.178601 |
| 2454 | **bring harm** | 0.178631 |
| 2455 | **mental offering** | 0.178673 |
| 2456 | **tale** | 0.178740 |
| 2457 | **lala** | 0.178791 |
| 2458 | **wave** | 0.178800 |
| 2459 | **body physically present** | 0.178837 |
| 2460 | **rank** | 0.178853 |
| 2461 | **art** | 0.178857 |
| 2462 | **spiritual instruction** | 0.178881 |
| 2463 | **single form** | 0.178931 |
| 2464 | **succeed** | 0.178963 |
| 2465 | **ensure** | 0.178989 |
| 2466 | **delight** | 0.179054 |
| 2467 | **member** | 0.179077 |
| 2468 | **authentic refuge** | 0.179086 |
| 2469 | **belong** | 0.179132 |
| 2470 | **sixteen thousand** | 0.179160 |
| 2471 | **inferior** | 0.179261 |
| 2472 | **guest** | 0.179313 |
| 2473 | **hermit** | 0.179406 |
| 2474 | **sever** | 0.179429 |
| 2475 | **miss** | 0.179528 |
| 2476 | **omniscient sovereign** | 0.179589 |
| 2477 | **human rebirth** | 0.180242 |
| 2478 | **everyday life** | 0.180273 |
| 2479 | **profoundly secret** | 0.180322 |
| 2480 | **dear life** | 0.180323 |
| 2481 | **friendship** | 0.180327 |
| 2482 | **eighteen hell** | 0.180350 |
| 2483 | **permanence** | 0.180369 |
| 2484 | **autumn** | 0.180404 |
| 2485 | **heart doctrine** | 0.180439 |
| 2486 | **circum** | 0.180441 |
| 2487 | **molten** | 0.180688 |
| 2488 | **red hot** | 0.180694 |
| 2489 | **lamp sutra** | 0.180738 |
| 2490 | **incalculable** | 0.180759 |
| 2491 | **scrap** | 0.180917 |
| 2492 | **pure vision** | 0.180961 |
| 2493 | **terribly** | 0.180987 |
| 2494 | **horn** | 0.181025 |
| 2495 | **sadaprarudita cut** | 0.181079 |
| 2496 | **sack** | 0.181133 |
| 2497 | **stick** | 0.181149 |
| 2498 | **painful** | 0.181163 |
| 2499 | **womb** | 0.181176 |
| 2500 | **soon** | 0.181215 |
| 2501 | **swallow** | 0.181229 |
| 2502 | **beginningless** | 0.181254 |
| 2503 | **homeland** | 0.181297 |
| 2504 | **illusory** | 0.181305 |
| 2505 | **distance** | 0.181323 |
| 2506 | **certainty** | 0.181352 |
| 2507 | **draw** | 0.181389 |
| 2508 | **half** | 0.181396 |
| 2509 | **delicious** | 0.181401 |
| 2510 | **mouse** | 0.181425 |
| 2511 | **livestock** | 0.181435 |
| 2512 | **marriage** | 0.181456 |
| 2513 | **trickery** | 0.181482 |
| 2514 | **anguish** | 0.181498 |
| 2515 | **degree** | 0.181504 |
| 2516 | **distress** | 0.181515 |
| 2517 | **openly** | 0.181529 |
| 2518 | **last** | 0.181530 |
| 2519 | **incapable** | 0.181558 |
| 2520 | **early** | 0.181574 |
| 2521 | **proverb** | 0.181586 |
| 2522 | **rocky** | 0.181599 |
| 2523 | **proliferate** | 0.181607 |
| 2524 | **blue vajra** | 0.181646 |
| 2525 | **mustard** | 0.181677 |
| 2526 | **fame** | 0.181727 |
| 2527 | **sandal** | 0.181775 |
| 2528 | **distinguish good** | 0.181791 |
| 2529 | **unchanging** | 0.181823 |
| 2530 | **generous** | 0.181831 |
| 2531 | **entourage** | 0.181905 |
| 2532 | **practise concentration** | 0.181911 |
| 2533 | **drag** | 0.181921 |
| 2534 | **continuous** | 0.181938 |
| 2535 | **tremendous** | 0.181943 |
| 2536 | **push** | 0.181948 |
| 2537 | **enormous** | 0.181955 |
| 2538 | **suitable** | 0.181968 |
| 2539 | **hail** | 0.181968 |
| 2540 | **people learn** | 0.181975 |
| 2541 | **beer** | 0.181979 |
| 2542 | **personal** | 0.181990 |
| 2543 | **confident** | 0.181992 |
| 2544 | **eventually** | 0.182032 |
| 2545 | **displease** | 0.182073 |
| 2546 | **raise** | 0.182083 |
| 2547 | **homage** | 0.182086 |
| 2548 | **asleep** | 0.182086 |
| 2549 | **grave** | 0.182094 |
| 2550 | **threefold** | 0.182119 |
| 2551 | **unimaginable** | 0.182135 |
| 2552 | **undesirable** | 0.182141 |
| 2553 | **radiant** | 0.182197 |
| 2554 | **surely** | 0.182201 |
| 2555 | **aggression** | 0.182202 |
| 2556 | **vicious** | 0.182211 |
| 2557 | **notice** | 0.182216 |
| 2558 | **conclude** | 0.182225 |
| 2559 | **show** | 0.182228 |
| 2560 | **persevere** | 0.182233 |
| 2561 | **courageous** | 0.182265 |
| 2562 | **rush** | 0.182268 |
| 2563 | **silver** | 0.182275 |
| 2564 | **exchange** | 0.182281 |
| 2565 | **bonpos** | 0.182284 |
| 2566 | **rage** | 0.182284 |
| 2567 | **heartfelt** | 0.182294 |
| 2568 | **generate** | 0.182294 |
| 2569 | **holder** | 0.182301 |
| 2570 | **incense** | 0.182305 |
| 2571 | **succession** | 0.182311 |
| 2572 | **medi** | 0.182312 |
| 2573 | **circumambulate** | 0.182316 |
| 2574 | **guidance** | 0.182328 |
| 2575 | **royal** | 0.182342 |
| 2576 | **decadent** | 0.182357 |
| 2577 | **overcome** | 0.182366 |
| 2578 | **want** | 0.182370 |
| 2579 | **cotton** | 0.182370 |
| 2580 | **mila adamantine victory** | 0.182370 |
| 2581 | **temper** | 0.182379 |
| 2582 | **please** | 0.182384 |
| 2583 | **perseverance** | 0.182389 |
| 2584 | **risk** | 0.182394 |
| 2585 | **gain** | 0.182415 |
| 2586 | **need** | 0.182428 |
| 2587 | **scholar** | 0.182428 |
| 2588 | **non dharma** | 0.182428 |
| 2589 | **solely** | 0.182433 |
| 2590 | **mixed** | 0.182436 |
| 2591 | **defile** | 0.182436 |
| 2592 | **northern** | 0.182444 |
| 2593 | **logic** | 0.182448 |
| 2594 | **dumb** | 0.182449 |
| 2595 | **provide** | 0.182455 |
| 2596 | **infallible** | 0.182460 |
| 2597 | **twofold** | 0.182476 |
| 2598 | **smoke** | 0.182478 |
| 2599 | **beneath** | 0.182483 |
| 2600 | **mix** | 0.182491 |
| 2601 | **expert** | 0.182496 |
| 2602 | **afraid** | 0.182496 |
| 2603 | **contaminate** | 0.182500 |
| 2604 | **contact** | 0.182510 |
| 2605 | **north** | 0.182510 |
| 2606 | **infinite merit** | 0.182512 |
| 2607 | **sour** | 0.182520 |
| 2608 | **dirty** | 0.182532 |
| 2609 | **cup** | 0.182542 |
| 2610 | **pacify** | 0.182564 |
| 2611 | **religious** | 0.182569 |
| 2612 | **conceit** | 0.182572 |
| 2613 | **immortality** | 0.182578 |
| 2614 | **meaningless** | 0.182596 |
| 2615 | **behalf** | 0.182596 |
| 2616 | **disrespect** | 0.182609 |
| 2617 | **emanating** | 0.182611 |
| 2618 | **thirteen** | 0.182648 |
| 2619 | **declare** | 0.182648 |
| 2620 | **upper** | 0.182668 |
| 2621 | **stronghold** | 0.182669 |
| 2622 | **faithfully** | 0.182711 |
| 2623 | **perfect vajradhara** | 0.182876 |
| 2624 | **sick person** | 0.183007 |
| 2625 | **accumulate negative** | 0.183311 |
| 2626 | **transcendent primal wisdom** | 0.183568 |
| 2627 | **drikung kyobpa rinpoche** | 0.183570 |
| 2628 | **people speak** | 0.183729 |
| 2629 | **people lose** | 0.184462 |
| 2630 | **derge** | 0.184928 |
| 2631 | **firm faith** | 0.185066 |
| 2632 | **god demon** | 0.185706 |
| 2633 | **transcendent patience** | 0.185907 |
| 2634 | **transcendent diligence** | 0.185954 |
| 2635 | **dakini yeshe** | 0.186165 |
| 2636 | **people enjoy** | 0.186387 |
| 2637 | **people fail** | 0.186496 |
| 2638 | **black man** | 0.186610 |
| 2639 | **chinese** | 0.186719 |
| 2640 | **disciple left** | 0.186790 |
| 2641 | **conflict** | 0.186818 |
| 2642 | **geshe chakshingwa** | 0.186896 |
| 2643 | **obtain human** | 0.186991 |
| 2644 | **huge offering** | 0.187187 |
| 2645 | **perfect health** | 0.187372 |
| 2646 | **risk life** | 0.187815 |
| 2647 | **end result** | 0.187828 |
| 2648 | **suddenly find** | 0.187941 |
| 2649 | **outer refuge** | 0.187980 |
| 2650 | **white syllable** | 0.188195 |
| 2651 | **tingri** | 0.188388 |
| 2652 | **people claim** | 0.188548 |
| 2653 | **virudhaka** | 0.188692 |
| 2654 | **surabhibhadra** | 0.188818 |
| 2655 | **single tibetan practitioner** | 0.189241 |
| 2656 | **main path** | 0.189276 |
| 2657 | **translator vairotsana** | 0.189318 |
| 2658 | **mahayana** | 0.189334 |
| 2659 | **invoke glorious vajrasattva** | 0.189815 |
| 2660 | **prajflaparamita** | 0.190023 |
| 2661 | **karmapa lamas** | 0.190134 |
| 2662 | **foundation stone** | 0.190253 |
| 2663 | **hevajra** | 0.190399 |
| 2664 | **mother camel** | 0.190750 |
| 2665 | **life renounce** | 0.190863 |
| 2666 | **promise** | 0.190961 |
| 2667 | **human lifetime forever** | 0.191047 |
| 2668 | **tsenpo** | 0.191054 |
| 2669 | **devadatta** | 0.191069 |
| 2670 | **avalokitdvara** | 0.191261 |
| 2671 | **lower left** | 0.191658 |
| 2672 | **neighbour** | 0.192017 |
| 2673 | **dodepa** | 0.192073 |
| 2674 | **burst** | 0.192133 |
| 2675 | **kushab rinpoche shenpen** | 0.192233 |
| 2676 | **rinpoche shenpen thaye** | 0.192233 |
| 2677 | **ultimate fruit** | 0.192495 |
| 2678 | **red mountain** | 0.192810 |
| 2679 | **glorious mountain** | 0.192996 |
| 2680 | **labdron** | 0.193213 |
| 2681 | **happiness free** | 0.193224 |
| 2682 | **asuras** | 0.193279 |
| 2683 | **prasenajit** | 0.193542 |
| 2684 | **material body** | 0.193564 |
| 2685 | **vaisali** | 0.193584 |
| 2686 | **kutra** | 0.193708 |
| 2687 | **simha** | 0.193739 |
| 2688 | **torma** | 0.193771 |
| 2689 | **nyentsen** | 0.193784 |
| 2690 | **tingdzin** | 0.193795 |
| 2691 | **santarak** | 0.193796 |
| 2692 | **rich man** | 0.193809 |
| 2693 | **tsari** | 0.193859 |
| 2694 | **hik** | 0.193939 |
| 2695 | **place arouse** | 0.194010 |
| 2696 | **mind minutely** | 0.194032 |
| 2697 | **orgyen** | 0.194107 |
| 2698 | **profound emptiness** | 0.194142 |
| 2699 | **kasyapa** | 0.194143 |
| 2700 | **dispel** | 0.194215 |
| 2701 | **vajrasattvas** | 0.194327 |
| 2702 | **great primordial kingdom** | 0.194338 |
| 2703 | **spoil** | 0.194355 |
| 2704 | **town** | 0.194358 |
| 2705 | **constitute** | 0.194533 |
| 2706 | **spend day** | 0.195107 |
| 2707 | **complete faith** | 0.195434 |
| 2708 | **tendzin chopel** | 0.195524 |
| 2709 | **mountain palace** | 0.195595 |
| 2710 | **thirty seven** | 0.195611 |
| 2711 | **pointed mind** | 0.195825 |
| 2712 | **mind indissolubly** | 0.195828 |
| 2713 | **favour life** | 0.195845 |
| 2714 | **collection** | 0.195879 |
| 2715 | **fortress** | 0.195881 |
| 2716 | **joyful** | 0.196105 |
| 2717 | **entire kalpa** | 0.196136 |
| 2718 | **visit shang rinpoche** | 0.196220 |
| 2719 | **cleanse** | 0.196303 |
| 2720 | **interrupt** | 0.196345 |
| 2721 | **alas** | 0.196368 |
| 2722 | **black hat karmapas** | 0.196380 |
| 2723 | **royalty** | 0.196475 |
| 2724 | **dawn** | 0.196697 |
| 2725 | **omniscient longchen rabjampa** | 0.197291 |
| 2726 | **wrathful black mother** | 0.197485 |
| 2727 | **wrathful black mother use** | 0.197514 |
| 2728 | **summit teaching** | 0.197750 |
| 2729 | **sixteen vajra** | 0.198377 |
| 2730 | **diamond cutter sutra** | 0.198410 |
| 2731 | **nowadays people** | 0.198413 |
| 2732 | **people nowadays** | 0.198413 |
| 2733 | **marvellous protector amitabha** | 0.198463 |
| 2734 | **negative mental** | 0.198719 |
| 2735 | **head visualize** | 0.198799 |
| 2736 | **personal practice** | 0.199130 |
| 2737 | **requisite good** | 0.199296 |
| 2738 | **good ascetic** | 0.199377 |
| 2739 | **extraordinary compassion** | 0.200233 |
| 2740 | **sleep yoga** | 0.200307 |
| 2741 | **vast wealth** | 0.200812 |
| 2742 | **vajra ogre** | 0.200890 |
| 2743 | **geshe tsakpuwa** | 0.202394 |
| 2744 | **respected master** | 0.203053 |
| 2745 | **collective good** | 0.203101 |
| 2746 | **entire body** | 0.203289 |
| 2747 | **uninterrupted good** | 0.203631 |
| 2748 | **ostentatious good** | 0.203918 |
| 2749 | **adopt good** | 0.203945 |
| 2750 | **diligent practice** | 0.204086 |
| 2751 | **excellent human** | 0.204295 |
| 2752 | **present wealth** | 0.204368 |
| 2753 | **prolong life** | 0.204374 |
| 2754 | **body dissolve** | 0.204822 |
| 2755 | **wild animal** | 0.204942 |
| 2756 | **main refuge** | 0.204961 |
| 2757 | **ordinary man** | 0.205048 |
| 2758 | **single offensive word** | 0.205055 |
| 2759 | **state arise** | 0.205078 |
| 2760 | **beating** | 0.205096 |
| 2761 | **verse** | 0.205302 |
| 2762 | **human simply** | 0.205510 |
| 2763 | **clear recollection** | 0.205986 |
| 2764 | **red syllable** | 0.206235 |
| 2765 | **element mandala** | 0.206440 |
| 2766 | **bodhicitta training** | 0.206592 |
| 2767 | **hells derive** | 0.207039 |
| 2768 | **terrible suffering** | 0.207343 |
| 2769 | **arouse absolute bodhicitta** | 0.207750 |
| 2770 | **fortunate human** | 0.208145 |
| 2771 | **delicious food** | 0.208989 |
| 2772 | **life good** | 0.209081 |
| 2773 | **short path** | 0.209489 |
| 2774 | **siddha melong dorje** | 0.209713 |
| 2775 | **extraordinary main path** | 0.209798 |
| 2776 | **commit negative** | 0.210478 |
| 2777 | **mikyo dorje** | 0.210493 |
| 2778 | **achieve liberation** | 0.211136 |
| 2779 | **goddesses offering** | 0.211292 |
| 2780 | **present form** | 0.211900 |
| 2781 | **hell ofutpala like** | 0.211962 |
| 2782 | **strong negative** | 0.212283 |
| 2783 | **frightening hell** | 0.212485 |
| 2784 | **day practice** | 0.212836 |
| 2785 | **intermediate state arise** | 0.213172 |
| 2786 | **lotus crest** | 0.213196 |
| 2787 | **extraordinary bodhicitta** | 0.213225 |
| 2788 | **langri thangpa gloomy face** | 0.213438 |
| 2789 | **past karma** | 0.213657 |
| 2790 | **eager faith** | 0.213939 |
| 2791 | **lingje** | 0.214033 |
| 2792 | **impure offering** | 0.214179 |
| 2793 | **influence** | 0.214284 |
| 2794 | **nanda set** | 0.214455 |
| 2795 | **vajras** | 0.214663 |
| 2796 | **tsen** | 0.214751 |
| 2797 | **entire refuge** | 0.215291 |
| 2798 | **golden place** | 0.215358 |
| 2799 | **arhat katyayana** | 0.215582 |
| 2800 | **contemplate** | 0.215583 |
| 2801 | **action take** | 0.215644 |
| 2802 | **offer water** | 0.215821 |
| 2803 | **padma siddhi hum** | 0.215839 |
| 2804 | **plant** | 0.216066 |
| 2805 | **problem** | 0.216098 |
| 2806 | **clear water** | 0.216139 |
| 2807 | **bank** | 0.216397 |
| 2808 | **vidyadhara** | 0.216530 |
| 2809 | **birth death** | 0.217018 |
| 2810 | **selfish desire** | 0.217051 |
| 2811 | **supreme happiness** | 0.217112 |
| 2812 | **hypocritical practice** | 0.217113 |
| 2813 | **lama yungton** | 0.217372 |
| 2814 | **vast scale** | 0.217700 |
| 2815 | **assiduous practice** | 0.217920 |
| 2816 | **devotional practice** | 0.218136 |
| 2817 | **practice predominate** | 0.218150 |
| 2818 | **renounce evil** | 0.218282 |
| 2819 | **body enter** | 0.218399 |
| 2820 | **immense merit** | 0.218752 |
| 2821 | **stains** | 0.218896 |
| 2822 | **fragrant** | 0.219006 |
| 2823 | **message** | 0.219353 |
| 2824 | **blister** | 0.219405 |
| 2825 | **service** | 0.219437 |
| 2826 | **hunter gonpo dorje** | 0.219582 |
| 2827 | **sore** | 0.219609 |
| 2828 | **past existence** | 0.219691 |
| 2829 | **perfectly pure motivation** | 0.219735 |
| 2830 | **pratimok** | 0.219803 |
| 2831 | **blow** | 0.219814 |
| 2832 | **evil nature** | 0.219859 |
| 2833 | **doctrines transference tradition** | 0.219969 |
| 2834 | **samsaric suffering** | 0.220060 |
| 2835 | **famous moon** | 0.220073 |
| 2836 | **sublime root** | 0.220318 |
| 2837 | **garment** | 0.220395 |
| 2838 | **gate** | 0.220532 |
| 2839 | **powerful positive** | 0.220623 |
| 2840 | **vallabha** | 0.220704 |
| 2841 | **lack faith** | 0.220812 |
| 2842 | **longchen** | 0.221083 |
| 2843 | **people behave** | 0.221451 |
| 2844 | **angulimala** | 0.221468 |
| 2845 | **kadampa** | 0.221625 |
| 2846 | **times** | 0.221631 |
| 2847 | **sympathetic joy** | 0.221733 |
| 2848 | **abbot santarak** | 0.221756 |
| 2849 | **mahakasyapa** | 0.221794 |
| 2850 | **gracious** | 0.221874 |
| 2851 | **realization free** | 0.221886 |
| 2852 | **mipham** | 0.222027 |
| 2853 | **mafijusrimitra** | 0.222327 |
| 2854 | **complete enlightenment** | 0.222347 |
| 2855 | **collapse** | 0.222362 |
| 2856 | **chopel** | 0.222436 |
| 2857 | **horse lama** | 0.222582 |
| 2858 | **pea** | 0.222860 |
| 2859 | **flock** | 0.223217 |
| 2860 | **row** | 0.223477 |
| 2861 | **emerge** | 0.223495 |
| 2862 | **ambition** | 0.223507 |
| 2863 | **hallucination** | 0.223669 |
| 2864 | **nail** | 0.223692 |
| 2865 | **feast offering** | 0.223781 |
| 2866 | **shepherd** | 0.223865 |
| 2867 | **minister** | 0.223920 |
| 2868 | **black noose** | 0.224014 |
| 2869 | **lover** | 0.224264 |
| 2870 | **breeze** | 0.224277 |
| 2871 | **emanates** | 0.224294 |
| 2872 | **phrase** | 0.224327 |
| 2873 | **swan** | 0.224425 |
| 2874 | **dark red** | 0.224809 |
| 2875 | **tathagata sri** | 0.224937 |
| 2876 | **pure conduct** | 0.225493 |
| 2877 | **stance** | 0.225551 |
| 2878 | **vivid faith** | 0.225579 |
| 2879 | **complete instruction** | 0.225699 |
| 2880 | **stomach** | 0.226323 |
| 2881 | **neck** | 0.226361 |
| 2882 | **sensation** | 0.226474 |
| 2883 | **great universal system** | 0.226492 |
| 2884 | **immense bodhicitta** | 0.226675 |
| 2885 | **cousin** | 0.226706 |
| 2886 | **lift** | 0.226780 |
| 2887 | **starting point** | 0.226954 |
| 2888 | **develop faith** | 0.226984 |
| 2889 | **perfume** | 0.227210 |
| 2890 | **pillar** | 0.227334 |
| 2891 | **odd** | 0.227341 |
| 2892 | **praise** | 0.227397 |
| 2893 | **silk** | 0.227529 |
| 2894 | **container** | 0.227625 |
| 2895 | **householder** | 0.227659 |
| 2896 | **prisoner** | 0.227713 |
| 2897 | **hurt** | 0.227733 |
| 2898 | **load** | 0.227735 |
| 2899 | **day elapatra** | 0.227758 |
| 2900 | **bar** | 0.227780 |
| 2901 | **precious medicinal tree** | 0.227835 |
| 2902 | **protuberance** | 0.227915 |
| 2903 | **dwelling** | 0.228019 |
| 2904 | **black hat** | 0.228020 |
| 2905 | **consort** | 0.228064 |
| 2906 | **context** | 0.228065 |
| 2907 | **clear vision** | 0.228068 |
| 2908 | **border** | 0.228120 |
| 2909 | **grant** | 0.228181 |
| 2910 | **ghost** | 0.228207 |
| 2911 | **contrary** | 0.228232 |
| 2912 | **representative** | 0.228290 |
| 2913 | **circumstantial** | 0.228318 |
| 2914 | **tulkus** | 0.228340 |
| 2915 | **noble spiritual** | 0.228477 |
| 2916 | **transcendent discipline** | 0.228563 |
| 2917 | **single instant lead** | 0.228715 |
| 2918 | **work hard** | 0.228964 |
| 2919 | **precious material** | 0.228989 |
| 2920 | **kalpa delightful** | 0.229062 |
| 2921 | **jowo dole** | 0.229221 |
| 2922 | **intense compassion** | 0.229528 |
| 2923 | **melong dorje** | 0.229734 |
| 2924 | **choice** | 0.229797 |
| 2925 | **teaching yard** | 0.229890 |
| 2926 | **outdoor teaching** | 0.229891 |
| 2927 | **wake** | 0.229924 |
| 2928 | **persistently** | 0.230107 |
| 2929 | **harma teaching** | 0.230169 |
| 2930 | **teachings ofmaitreya** | 0.230175 |
| 2931 | **miraculously** | 0.230202 |
| 2932 | **elapatra tree** | 0.230316 |
| 2933 | **youth** | 0.230434 |
| 2934 | **absent** | 0.230581 |
| 2935 | **southern buddhafield** | 0.230631 |
| 2936 | **swift** | 0.230657 |
| 2937 | **suck** | 0.230684 |
| 2938 | **bent** | 0.230700 |
| 2939 | **authority** | 0.230720 |
| 2940 | **fierce** | 0.230755 |
| 2941 | **fleeting** | 0.230761 |
| 2942 | **conceptualization** | 0.230841 |
| 2943 | **frustrating** | 0.230876 |
| 2944 | **assimilate** | 0.230884 |
| 2945 | **armour** | 0.230928 |
| 2946 | **mat** | 0.230932 |
| 2947 | **liquid** | 0.230940 |
| 2948 | **abundance** | 0.230962 |
| 2949 | **transmigration** | 0.230976 |
| 2950 | **people pay** | 0.230980 |
| 2951 | **remind** | 0.231012 |
| 2952 | **slowly** | 0.231058 |
| 2953 | **pursue** | 0.231065 |
| 2954 | **crawl** | 0.231070 |
| 2955 | **grateful** | 0.231074 |
| 2956 | **regard** | 0.231094 |
| 2957 | **quickly** | 0.231105 |
| 2958 | **unshakeable** | 0.231115 |
| 2959 | **extent** | 0.231142 |
| 2960 | **isvara** | 0.231184 |
| 2961 | **ignorant** | 0.231186 |
| 2962 | **sadness** | 0.231206 |
| 2963 | **lay** | 0.231227 |
| 2964 | **exclaim** | 0.231249 |
| 2965 | **feed** | 0.231291 |
| 2966 | **plunge** | 0.231326 |
| 2967 | **dorje dudjom** | 0.231342 |
| 2968 | **chastity** | 0.231350 |
| 2969 | **drown** | 0.231352 |
| 2970 | **move** | 0.231353 |
| 2971 | **mistaken** | 0.231356 |
| 2972 | **irrelevant** | 0.231365 |
| 2973 | **temporarily** | 0.231384 |
| 2974 | **curd** | 0.231390 |
| 2975 | **gently** | 0.231397 |
| 2976 | **stricken** | 0.231427 |
| 2977 | **wide** | 0.231448 |
| 2978 | **discouragement** | 0.231470 |
| 2979 | **popularity** | 0.231470 |
| 2980 | **identify** | 0.231482 |
| 2981 | **torture** | 0.231483 |
| 2982 | **weary** | 0.231484 |
| 2983 | **procrastination** | 0.231493 |
| 2984 | **limitless** | 0.231500 |
| 2985 | **salt** | 0.231526 |
| 2986 | **natural state support** | 0.231526 |
| 2987 | **mould** | 0.231564 |
| 2988 | **unerringly** | 0.231577 |
| 2989 | **variety** | 0.231592 |
| 2990 | **sandalwood** | 0.231598 |
| 2991 | **inanimate** | 0.231600 |
| 2992 | **wolf** | 0.231618 |
| 2993 | **uncle** | 0.231632 |
| 2994 | **era** | 0.231632 |
| 2995 | **unknown** | 0.231633 |
| 2996 | **utter** | 0.231641 |
| 2997 | **prosperity** | 0.231646 |
| 2998 | **loss** | 0.231648 |
| 2999 | **ingratitude** | 0.231656 |
| 3000 | **jump** | 0.231663 |
| 3001 | **changchub dorje** | 0.231666 |
| 3002 | **defend** | 0.231668 |
| 3003 | **sustain** | 0.231673 |
| 3004 | **local** | 0.231682 |
| 3005 | **ease** | 0.231697 |
| 3006 | **eagerness** | 0.231704 |
| 3007 | **gateway** | 0.231712 |
| 3008 | **belt** | 0.231712 |
| 3009 | **famine** | 0.231721 |
| 3010 | **mentality** | 0.231722 |
| 3011 | **express** | 0.231724 |
| 3012 | **nearby** | 0.231739 |
| 3013 | **adversity** | 0.231743 |
| 3014 | **chaff** | 0.231744 |
| 3015 | **commerce** | 0.231747 |
| 3016 | **lightly** | 0.231749 |
| 3017 | **edge** | 0.231759 |
| 3018 | **smile** | 0.231764 |
| 3019 | **specific** | 0.231774 |
| 3020 | **clay** | 0.231776 |
| 3021 | **shoe** | 0.231776 |
| 3022 | **count** | 0.231779 |
| 3023 | **upset** | 0.231779 |
| 3024 | **maturity** | 0.231784 |
| 3025 | **eager** | 0.231784 |
| 3026 | **pointless** | 0.231789 |
| 3027 | **aversion** | 0.231802 |
| 3028 | **insist** | 0.231806 |
| 3029 | **penetrate** | 0.231807 |
| 3030 | **accordance** | 0.231817 |
| 3031 | **nostrils** | 0.231865 |
| 3032 | **befall** | 0.231867 |
| 3033 | **criticism** | 0.231870 |
| 3034 | **simultaneously** | 0.231870 |
| 3035 | **pillow** | 0.231878 |
| 3036 | **gaze** | 0.231897 |
| 3037 | **rub** | 0.231898 |
| 3038 | **personally** | 0.231911 |
| 3039 | **proud** | 0.231914 |
| 3040 | **messenger** | 0.231926 |
| 3041 | **spit** | 0.231950 |
| 3042 | **attention** | 0.231950 |
| 3043 | **effective** | 0.231962 |
| 3044 | **kar** | 0.231962 |
| 3045 | **ultimately** | 0.231971 |
| 3046 | **fundamental** | 0.231986 |
| 3047 | **play** | 0.231986 |
| 3048 | **fine** | 0.231988 |
| 3049 | **rohita** | 0.231991 |
| 3050 | **intelligence** | 0.232004 |
| 3051 | **earnestly** | 0.232017 |
| 3052 | **desirable** | 0.232020 |
| 3053 | **absence** | 0.232022 |
| 3054 | **dough** | 0.232027 |
| 3055 | **extend** | 0.232029 |
| 3056 | **reveal** | 0.232032 |
| 3057 | **infatuation** | 0.232039 |
| 3058 | **unfailing** | 0.232046 |
| 3059 | **inherit** | 0.232058 |
| 3060 | **intrinsic** | 0.232059 |
| 3061 | **wash** | 0.232066 |
| 3062 | **observe** | 0.232076 |
| 3063 | **subjugate** | 0.232086 |
| 3064 | **store** | 0.232101 |
| 3065 | **pinch** | 0.232110 |
| 3066 | **ego clinging** | 0.232131 |
| 3067 | **verbal** | 0.232134 |
| 3068 | **radial** | 0.232154 |
| 3069 | **temporary** | 0.232158 |
| 3070 | **breathe** | 0.232160 |
| 3071 | **conceptual** | 0.232166 |
| 3072 | **interruption** | 0.232175 |
| 3073 | **diligent** | 0.232189 |
| 3074 | **gathering offering** | 0.232208 |
| 3075 | **diligently** | 0.232209 |
| 3076 | **hip** | 0.232214 |
| 3077 | **subsequently** | 0.232221 |
| 3078 | **supernatural** | 0.232224 |
| 3079 | **mature** | 0.232231 |
| 3080 | **hollow** | 0.232242 |
| 3081 | **eradicate** | 0.232248 |
| 3082 | **enjoyment** | 0.232249 |
| 3083 | **crystal** | 0.232259 |
| 3084 | **access** | 0.232275 |
| 3085 | **impervious** | 0.232284 |
| 3086 | **merge** | 0.232289 |
| 3087 | **peak** | 0.232291 |
| 3088 | **passion** | 0.232306 |
| 3089 | **nirmar** | 0.232317 |
| 3090 | **effortless** | 0.232326 |
| 3091 | **site** | 0.232341 |
| 3092 | **hindu** | 0.232369 |
| 3093 | **unite** | 0.232391 |
| 3094 | **hand high** | 0.232871 |
| 3095 | **completely perfect** | 0.233124 |
| 3096 | **vigorous** | 0.233824 |
| 3097 | **mountain vajrapar** | 0.234171 |
| 3098 | **suffer terribly** | 0.234328 |
| 3099 | **equal nature** | 0.234388 |
| 3100 | **vast skill** | 0.234572 |
| 3101 | **pandita naropa** | 0.234817 |
| 3102 | **wisdom dakini** | 0.234995 |
| 3103 | **unbearable pain** | 0.235483 |
| 3104 | **bound** | 0.235801 |
| 3105 | **powerful person** | 0.236129 |
| 3106 | **branch visualize** | 0.236882 |
| 3107 | **complete root downfall** | 0.236927 |
| 3108 | **people add** | 0.237253 |
| 3109 | **important point** | 0.237432 |
| 3110 | **immaculate wisdom** | 0.238134 |
| 3111 | **supreme spiritual** | 0.238331 |
| 3112 | **karmic result** | 0.238891 |
| 3113 | **rude** | 0.238979 |
| 3114 | **prosperous people** | 0.239060 |
| 3115 | **steadfastness** | 0.239102 |
| 3116 | **main subject** | 0.239194 |
| 3117 | **attain accomplishment** | 0.239367 |
| 3118 | **wisdom enter** | 0.239650 |
| 3119 | **fortunate dynasty** | 0.240140 |
| 3120 | **compassion hurl** | 0.240397 |
| 3121 | **union wisdom** | 0.240449 |
| 3122 | **effect utterly** | 0.240977 |
| 3123 | **pure motivation** | 0.241094 |
| 3124 | **suffering befall** | 0.241572 |
| 3125 | **true tradition** | 0.241609 |
| 3126 | **white nectar** | 0.241743 |
| 3127 | **supreme joy** | 0.242617 |
| 3128 | **long training** | 0.242629 |
| 3129 | **happiness comfort** | 0.243439 |
| 3130 | **offering practice** | 0.243516 |
| 3131 | **vajra song** | 0.243588 |
| 3132 | **sublime path unerringly** | 0.243875 |
| 3133 | **orgyen jigme** | 0.243952 |
| 3134 | **ultimate liberation** | 0.243956 |
| 3135 | **sakya** | 0.244263 |
| 3136 | **postpone death** | 0.244359 |
| 3137 | **kyung tonpa** | 0.244671 |
| 3138 | **lhangtsang tonpa** | 0.244684 |
| 3139 | **refuge constantly** | 0.244930 |
| 3140 | **meritorious act** | 0.245536 |
| 3141 | **evil man** | 0.245932 |
| 3142 | **central head** | 0.246165 |
| 3143 | **strive day** | 0.246546 |
| 3144 | **feel natural** | 0.246675 |
| 3145 | **unaltered natural state** | 0.246835 |
| 3146 | **root samayas** | 0.246946 |
| 3147 | **cruel suffering** | 0.247102 |
| 3148 | **develop positive** | 0.247188 |
| 3149 | **seek refuge** | 0.247194 |
| 3150 | **marpa severely** | 0.247339 |
| 3151 | **actual meditation** | 0.247799 |
| 3152 | **outward sign** | 0.248102 |
| 3153 | **hollow vajra** | 0.249086 |
| 3154 | **khampa lhungpa** | 0.249121 |
| 3155 | **moment onwards** | 0.249182 |
| 3156 | **false spiritual** | 0.249504 |
| 3157 | **negative connection** | 0.249758 |
| 3158 | **con** | 0.249804 |
| 3159 | **precious golden** | 0.250387 |
| 3160 | **dumb person** | 0.250584 |
| 3161 | **khampa lungpa** | 0.251062 |
| 3162 | **infinite number** | 0.251201 |
| 3163 | **sublime sariputra** | 0.251230 |
| 3164 | **cheat people** | 0.251639 |
| 3165 | **ignorant people** | 0.251680 |
| 3166 | **complete root** | 0.251875 |
| 3167 | **double suffering** | 0.252119 |
| 3168 | **precious umbrella** | 0.252581 |
| 3169 | **religious king gomadeviya** | 0.252787 |
| 3170 | **ceaseless suffering** | 0.252930 |
| 3171 | **incredible suffering** | 0.252971 |
| 3172 | **ten** | 0.253065 |
| 3173 | **item** | 0.253195 |
| 3174 | **boundless compassion** | 0.253347 |
| 3175 | **mandalas** | 0.253658 |
| 3176 | **sublime essence** | 0.253757 |
| 3177 | **sink** | 0.254061 |
| 3178 | **feel pain** | 0.254127 |
| 3179 | **negative behaviour** | 0.254136 |
| 3180 | **chest** | 0.254164 |
| 3181 | **devour** | 0.254280 |
| 3182 | **plough** | 0.255069 |
| 3183 | **fully ripen** | 0.255275 |
| 3184 | **noble katyayana** | 0.255287 |
| 3185 | **real benefit** | 0.255613 |
| 3186 | **sangha fail** | 0.256006 |
| 3187 | **finally eighty thousand** | 0.256388 |
| 3188 | **entire human** | 0.256598 |
| 3189 | **outer water element** | 0.256622 |
| 3190 | **boundless love** | 0.256638 |
| 3191 | **compassion possess** | 0.256849 |
| 3192 | **false path** | 0.257097 |
| 3193 | **elapatra** | 0.257398 |
| 3194 | **perfection subsequently** | 0.257432 |
| 3195 | **sublime method** | 0.257704 |
| 3196 | **lax** | 0.257781 |
| 3197 | **profound truth** | 0.257981 |
| 3198 | **sage** | 0.258182 |
| 3199 | **totally free** | 0.258290 |
| 3200 | **emperor** | 0.258506 |
| 3201 | **people manage** | 0.258720 |
| 3202 | **karmic effect similar** | 0.259337 |
| 3203 | **sangye heard** | 0.259402 |
| 3204 | **stroke** | 0.259656 |
| 3205 | **magic** | 0.259973 |
| 3206 | **ordinary outer** | 0.260241 |
| 3207 | **compassionate root** | 0.260377 |
| 3208 | **old people** | 0.260402 |
| 3209 | **bestow** | 0.260416 |
| 3210 | **vajra sprang** | 0.260603 |
| 3211 | **afar** | 0.260609 |
| 3212 | **lotus bud** | 0.260613 |
| 3213 | **harvest** | 0.260769 |
| 3214 | **boundless merit** | 0.260777 |
| 3215 | **bathe** | 0.260790 |
| 3216 | **wisdom kaya** | 0.260794 |
| 3217 | **building** | 0.261244 |
| 3218 | **precious lineage dawn** | 0.261610 |
| 3219 | **syllable hrih** | 0.261964 |
| 3220 | **sutra ofi** | 0.262232 |
| 3221 | **state support** | 0.262569 |
| 3222 | **bring unending** | 0.262646 |
| 3223 | **body life** | 0.263008 |
| 3224 | **people crave** | 0.263730 |
| 3225 | **people pretend** | 0.263862 |
| 3226 | **marvellous essence** | 0.264030 |
| 3227 | **impress people** | 0.264249 |
| 3228 | **people partake** | 0.264372 |
| 3229 | **people unhappy** | 0.264384 |
| 3230 | **sacred place** | 0.264623 |
| 3231 | **primordial state free** | 0.264659 |
| 3232 | **false cho** | 0.264748 |
| 3233 | **gifted people** | 0.264916 |
| 3234 | **entire time swimming** | 0.265051 |
| 3235 | **take pleasure** | 0.265872 |
| 3236 | **poor thing** | 0.266663 |
| 3237 | **vajra puspe** | 0.266809 |
| 3238 | **dha vajra** | 0.266817 |
| 3239 | **kind lack** | 0.266852 |
| 3240 | **tangtong gyalpo** | 0.267318 |
| 3241 | **physically present** | 0.267338 |
| 3242 | **bird taking** | 0.267607 |
| 3243 | **virtuous thing** | 0.267787 |
| 3244 | **long iron** | 0.267871 |
| 3245 | **present perfectly dedicate** | 0.268011 |
| 3246 | **entire world** | 0.268208 |
| 3247 | **light empowerment** | 0.268264 |
| 3248 | **close friend** | 0.268385 |
| 3249 | **past sexual** | 0.268509 |
| 3250 | **adamantine clear light** | 0.270074 |
| 3251 | **blood lake** | 0.270176 |
| 3252 | **people intimately** | 0.270304 |
| 3253 | **reliable people** | 0.270322 |
| 3254 | **people declare** | 0.270794 |
| 3255 | **cultivate bodhicitta** | 0.270999 |
| 3256 | **feel attachment** | 0.271123 |
| 3257 | **seventh day** | 0.271895 |
| 3258 | **upayoga tantra** | 0.271909 |
| 3259 | **steel wheel** | 0.272270 |
| 3260 | **powerful demon** | 0.272499 |
| 3261 | **body physically** | 0.272590 |
| 3262 | **harsh speech** | 0.272611 |
| 3263 | **human lifetime** | 0.272854 |
| 3264 | **mix negative** | 0.273038 |
| 3265 | **demon tsang** | 0.273180 |
| 3266 | **rich person** | 0.273206 |
| 3267 | **bonpo** | 0.273425 |
| 3268 | **meet dharmodgata** | 0.273718 |
| 3269 | **yoga technique** | 0.273758 |
| 3270 | **practice like compassion** | 0.273786 |
| 3271 | **yidams** | 0.273972 |
| 3272 | **water element** | 0.274082 |
| 3273 | **small pile** | 0.274297 |
| 3274 | **perform positive** | 0.274683 |
| 3275 | **ultimate goal** | 0.275078 |
| 3276 | **outer water** | 0.275384 |
| 3277 | **glorious vajradhara** | 0.275783 |
| 3278 | **order great universal** | 0.275906 |
| 3279 | **beggar woman** | 0.275925 |
| 3280 | **powerful evil** | 0.275937 |
| 3281 | **direct empowerment** | 0.275993 |
| 3282 | **control body** | 0.276101 |
| 3283 | **immense faith** | 0.276851 |
| 3284 | **nyatri tsenpo** | 0.277423 |
| 3285 | **sublime son** | 0.277577 |
| 3286 | **karmapas** | 0.277592 |
| 3287 | **animal today** | 0.277699 |
| 3288 | **action avoid** | 0.277733 |
| 3289 | **king ravati** | 0.277805 |
| 3290 | **merit totally** | 0.277821 |
| 3291 | **machik labdron** | 0.278144 |
| 3292 | **king subject** | 0.278362 |
| 3293 | **negative mentality** | 0.278561 |
| 3294 | **animal birth** | 0.280518 |
| 3295 | **immeasurable compassion** | 0.280598 |
| 3296 | **suffering negative** | 0.280983 |
| 3297 | **apply bodhicitta** | 0.281897 |
| 3298 | **consume flesh** | 0.282540 |
| 3299 | **kyabje dodrup chen** | 0.282625 |
| 3300 | **suddenly end** | 0.282646 |
| 3301 | **present perfectly** | 0.282812 |
| 3302 | **white hum** | 0.282824 |
| 3303 | **red blood** | 0.282897 |
| 3304 | **feel hatred** | 0.282959 |
| 3305 | **head dissolve** | 0.283487 |
| 3306 | **metal ground** | 0.283910 |
| 3307 | **comfortable place** | 0.284192 |
| 3308 | **upward** | 0.284300 |
| 3309 | **blissful land** | 0.284551 |
| 3310 | **offer flesh** | 0.284917 |
| 3311 | **red syllable hrih** | 0.285262 |
| 3312 | **sacred wisdom** | 0.285307 |
| 3313 | **black mother** | 0.285523 |
| 3314 | **black mother use** | 0.285556 |
| 3315 | **ninefold black** | 0.285607 |
| 3316 | **negative imprint** | 0.285715 |
| 3317 | **naropa underwent** | 0.285752 |
| 3318 | **bodhicitta equally** | 0.285915 |
| 3319 | **humble place** | 0.286034 |
| 3320 | **paqqita naropa** | 0.286364 |
| 3321 | **captain compassionate heart** | 0.286849 |
| 3322 | **dark black** | 0.286862 |
| 3323 | **azure heaven** | 0.287000 |
| 3324 | **nagas** | 0.287085 |
| 3325 | **lightly small** | 0.287373 |
| 3326 | **perfectly dedicated merit** | 0.287608 |
| 3327 | **town scavenger offering** | 0.288047 |
| 3328 | **lack wealth** | 0.288143 |
| 3329 | **sincere bodhicitta** | 0.288515 |
| 3330 | **inconceivable power** | 0.289321 |
| 3331 | **opening** | 0.289482 |
| 3332 | **clear light spread** | 0.289546 |
| 3333 | **happiness today** | 0.289740 |
| 3334 | **perfection phase depend** | 0.290008 |
| 3335 | **wrong attitude** | 0.290989 |
| 3336 | **mother sixteen** | 0.291005 |
| 3337 | **practice take** | 0.291391 |
| 3338 | **constantly long** | 0.291680 |
| 3339 | **northern buddhafield** | 0.292585 |
| 3340 | **single night** | 0.292643 |
| 3341 | **simply free** | 0.292850 |
| 3342 | **state carefully** | 0.293341 |
| 3343 | **past perfectly dedicated** | 0.293462 |
| 3344 | **real determination** | 0.293558 |
| 3345 | **faith fully** | 0.293849 |
| 3346 | **jigme cbokyi** | 0.294274 |
| 3347 | **jigme gyalwai** | 0.294281 |
| 3348 | **feel happy** | 0.295129 |
| 3349 | **meditate single mindedly** | 0.295132 |
| 3350 | **heart centre** | 0.295151 |
| 3351 | **superior transference** | 0.295312 |
| 3352 | **profound essence** | 0.295352 |
| 3353 | **orgyen jigme cbokyi** | 0.295415 |
| 3354 | **day people** | 0.295670 |
| 3355 | **mantras perfunctorily** | 0.296256 |
| 3356 | **authentic view** | 0.296696 |
| 3357 | **dynasty** | 0.297052 |
| 3358 | **worldly point** | 0.297096 |
| 3359 | **belonging** | 0.297260 |
| 3360 | **practise virtue** | 0.297642 |
| 3361 | **refuge sincerely** | 0.297705 |
| 3362 | **tathagata ratnapada** | 0.297826 |
| 3363 | **tathagata siddhyaloka** | 0.297829 |
| 3364 | **guard** | 0.298007 |
| 3365 | **natural expression** | 0.298469 |
| 3366 | **hesitation** | 0.298586 |
| 3367 | **wound** | 0.298615 |
| 3368 | **thousand iron** | 0.298834 |
| 3369 | **wrist** | 0.298981 |
| 3370 | **indivisible yoga** | 0.299229 |
| 3371 | **principal sravakas** | 0.299401 |
| 3372 | **lita vimalamitra** | 0.299412 |
| 3373 | **prodigious negative** | 0.299641 |
| 3374 | **ludicrous negative** | 0.299648 |
| 3375 | **unmentionably negative** | 0.299807 |
| 3376 | **intense faith** | 0.299979 |

---
## Most Distinctive Words (highest TF-IDF, normalized)

Words that appear **frequently in this text** yet are **rare or absent in general English**. Lemmatized: plural/possessive variants (e.g. *buddhas* → *buddha*) are merged into one row; the `variants` shown lists the surface forms folded into each lemma.

**1. dharma** — count: 409, TF-IDF: 67,973, IDF: 9.59 🔴 extremely high — text-exclusive
**2. buddha** — count: 364, TF-IDF: 60,494, IDF: 9.59 🔴 extremely high — text-exclusive (variants: buddha, buddhas)
**3. teacher** — count: 373, TF-IDF: 57,530, IDF: 8.899988 🔴 extremely high — text-exclusive (variants: teacher, teachers)
**4. teaching** — count: 218, TF-IDF: 36,230, IDF: 9.59 🟠 very high — domain-specific (variants: teaching, teachings)
**5. like** — count: 397, TF-IDF: 35,724, IDF: 5.192532 🟠 very high — domain-specific (variants: like, likes)
**6. person** — count: 260, TF-IDF: 32,220, IDF: 7.150788 🟠 very high — domain-specific (variants: people, person, persons)
**7. mind** — count: 256, TF-IDF: 31,724, IDF: 7.150788 🟠 very high — domain-specific (variants: mind, minds)
**8. practice** — count: 236, TF-IDF: 27,769, IDF: 6.789775 🟠 very high — domain-specific (variants: practice, practices)
**9. action** — count: 340, TF-IDF: 26,092, IDF: 4.428349 🟠 very high — domain-specific (variants: action, actions)
**10. realm** — count: 149, TF-IDF: 24,763, IDF: 9.59 🟠 very high — domain-specific (variants: realm, realms)
**11. yourself** — count: 154, TF-IDF: 24,520, IDF: 9.18767 🟠 very high — domain-specific
**12. compassion** — count: 147, TF-IDF: 24,438, IDF: 9.593135 🟠 very high — domain-specific
**13. suffering** — count: 192, TF-IDF: 24,096, IDF: 7.24176 🟠 very high — domain-specific (variants: suffering, sufferings)
**14. life** — count: 240, TF-IDF: 22,905, IDF: 5.507159 🟠 very high — domain-specific
**15. time** — count: 329, TF-IDF: 21,906, IDF: 3.842151 🟠 very high — domain-specific (variants: time, times)
**16. without** — count: 266, TF-IDF: 21,766, IDF: 4.721762 🟠 very high — domain-specific
**17. bodhicitta** — count: 130, TF-IDF: 21,605, IDF: 9.59 🟠 very high — domain-specific
**18. never** — count: 197, TF-IDF: 21,563, IDF: 6.31599 🟠 very high — domain-specific
**19. jewel** — count: 128, TF-IDF: 21,273, IDF: 9.59 🟠 very high — domain-specific (variants: jewel, jewels)
**20. merit** — count: 142, TF-IDF: 20,524, IDF: 8.340372 🟠 very high — domain-specific (variants: merit, merits)
**21. practise** — count: 123, TF-IDF: 20,448, IDF: 9.593135 🟠 very high — domain-specific
**22. body** — count: 180, TF-IDF: 19,761, IDF: 6.335039 🟠 very high — domain-specific (variants: bodies, body)
**23. path** — count: 145, TF-IDF: 19,603, IDF: 7.801376 🟠 very high — domain-specific (variants: path, paths)
**24. refuge** — count: 129, TF-IDF: 18,990, IDF: 8.494523 🟠 very high — domain-specific (variants: refuge, refuges)
**25. being** — count: 258, TF-IDF: 18,491, IDF: 4.13568 🟠 very high — domain-specific
**26. death** — count: 129, TF-IDF: 18,347, IDF: 8.206841 🟠 very high — domain-specific (variants: death, deaths)
**27. king** — count: 144, TF-IDF: 17,956, IDF: 7.19524 🟠 very high — domain-specific (variants: king, kings)
**28. hell** — count: 114, TF-IDF: 17,583, IDF: 8.899988 🟠 very high — domain-specific (variants: hell, hells)
**29. word** — count: 128, TF-IDF: 16,963, IDF: 7.647225 🟠 very high — domain-specific (variants: word, words)
**30. negative** — count: 166, TF-IDF: 16,949, IDF: 5.891833 🟠 very high — domain-specific
**31. offering** — count: 180, TF-IDF: 16,499, IDF: 5.28907 🟠 very high — domain-specific (variants: offering, offerings)
**32. bodhisattva** — count: 99, TF-IDF: 16,453, IDF: 9.59 🟠 very high — domain-specific (variants: bodhisattva, bodhisattvas)
**33. whatever** — count: 132, TF-IDF: 16,260, IDF: 7.108229 🟠 very high — domain-specific
**34. wisdom** — count: 109, TF-IDF: 16,046, IDF: 8.494523 🟠 very high — domain-specific (variants: wisdom, wisdoms)
**35. hundred** — count: 124, TF-IDF: 16,016, IDF: 7.453069 🟠 very high — domain-specific (variants: hundred, hundreds)
**36. friend** — count: 96, TF-IDF: 15,960, IDF: 9.593135 🟠 very high — domain-specific (variants: friend, friends)
**37. god** — count: 96, TF-IDF: 15,960, IDF: 9.593135 🟠 very high — domain-specific (variants: god, gods)
**38. mother** — count: 96, TF-IDF: 15,955, IDF: 9.59 🟠 very high — domain-specific (variants: mother, mothers)
**39. thought** — count: 152, TF-IDF: 15,867, IDF: 6.023602 🟠 very high — domain-specific (variants: thought, thoughts)
**40. perfect** — count: 97, TF-IDF: 15,444, IDF: 9.18767 🟠 very high — domain-specific (variants: perfect, perfects)
**41. way** — count: 184, TF-IDF: 15,194, IDF: 4.764821 🟠 very high — domain-specific (variants: way, ways)
**42. come** — count: 178, TF-IDF: 15,121, IDF: 4.901787 🟠 very high — domain-specific (variants: come, comes)
**43. faith** — count: 108, TF-IDF: 14,942, IDF: 7.983697 🟠 very high — domain-specific
**44. make** — count: 211, TF-IDF: 14,759, IDF: 4.036307 🟠 very high — domain-specific (variants: make, makes)
**45. live** — count: 134, TF-IDF: 14,667, IDF: 6.31599 🟠 very high — domain-specific (variants: live, lives)
**46. disciple** — count: 86, TF-IDF: 14,293, IDF: 9.59 🟠 very high — domain-specific (variants: disciple, disciples)
**47. once** — count: 140, TF-IDF: 14,235, IDF: 5.867442 🟠 very high — domain-specific
**48. say** — count: 185, TF-IDF: 14,011, IDF: 4.37008 🟠 very high — domain-specific (variants: say, says)
**49. instruction** — count: 83, TF-IDF: 13,799, IDF: 9.593135 🟠 very high — domain-specific (variants: instruction, instructions)
**50. monk** — count: 82, TF-IDF: 13,628, IDF: 9.59 🟠 very high — domain-specific (variants: monk, monks)

---

## Least Distinctive Words (lowest TF-IDF, normalized)

Words that appear in this text but are also extremely common in general English.

**1. stock** — count: 1, TF-IDF: 52.87, IDF: 3.050663 🔵 low — common in general English
**2. agreement** — count: 1, TF-IDF: 58.50, IDF: 3.375532 🔵 low — common in general English
**3. exchange** — count: 1, TF-IDF: 58.64, IDF: 3.38354 🔵 low — common in general English
**4. expected** — count: 1, TF-IDF: 58.67, IDF: 3.385552 🔵 low — common in general English
**5. government** — count: 1, TF-IDF: 60.98, IDF: 3.518939 🔵 low — common in general English
**6. foreign** — count: 1, TF-IDF: 63.35, IDF: 3.655599 🔵 low — common in general English
**7. agreed** — count: 1, TF-IDF: 63.74, IDF: 3.678282 🔵 low — common in general English
**8. rose** — count: 1, TF-IDF: 63.77, IDF: 3.679632 🔵 low — common in general English
**9. tax** — count: 1, TF-IDF: 65.00, IDF: 3.751041 🔵 low — common in general English
**10. production** — count: 1, TF-IDF: 65.08, IDF: 3.755405 🔵 low — common in general English
**11. official** — count: 1, TF-IDF: 65.21, IDF: 3.76272 🔵 low — common in general English
**12. industry** — count: 1, TF-IDF: 67.84, IDF: 3.914671 🔵 low — common in general English
**13. statement** — count: 1, TF-IDF: 67.90, IDF: 3.918095 🔵 low — common in general English
**14. capital** — count: 1, TF-IDF: 69.49, IDF: 4.009639 🔵 low — common in general English
**15. trading** — count: 1, TF-IDF: 70.35, IDF: 4.059746 🔵 low — common in general English
**16. yesterday** — count: 1, TF-IDF: 70.42, IDF: 4.063706 🔵 low — common in general English
**17. outstanding** — count: 1, TF-IDF: 70.91, IDF: 4.091877 🔵 low — common in general English
**18. bought** — count: 1, TF-IDF: 74.65, IDF: 4.307397 🔵 low — common in general English
**19. public** — count: 1, TF-IDF: 76.25, IDF: 4.400178 🔵 low — common in general English
**20. loan** — count: 1, TF-IDF: 77.35, IDF: 4.463236 🔵 low — common in general English
**21. secretary** — count: 1, TF-IDF: 79.24, IDF: 4.57255 🔵 low — common in general English
**22. available** — count: 1, TF-IDF: 79.59, IDF: 4.59255 🔵 low — common in general English
**23. transaction** — count: 1, TF-IDF: 80.30, IDF: 4.633793 🔵 low — common in general English
**24. net** — count: 2, TF-IDF: 80.36, IDF: 2.318656 🔵 low — common in general English (variants: net, nets)
**25. despite** — count: 1, TF-IDF: 81.50, IDF: 4.702786 🔵 low — common in general English
**26. buying** — count: 1, TF-IDF: 82.50, IDF: 4.760829 🔵 low — common in general English
**27. selling** — count: 1, TF-IDF: 84.09, IDF: 4.85256 🔵 low — common in general English
**28. charge** — count: 1, TF-IDF: 85.35, IDF: 4.92499 🔵 low — common in general English
**29. probably** — count: 1, TF-IDF: 86.18, IDF: 4.973076 🔵 low — common in general English
**30. respectively** — count: 1, TF-IDF: 86.35, IDF: 4.982977 🔵 low — common in general English
**31. range** — count: 1, TF-IDF: 86.44, IDF: 4.987965 🔵 low — common in general English
**32. adding** — count: 1, TF-IDF: 87.06, IDF: 5.023592 🔵 low — common in general English
**33. gross** — count: 1, TF-IDF: 88.17, IDF: 5.087785 🔵 low — common in general English
**34. farm** — count: 1, TF-IDF: 88.85, IDF: 5.127227 🔵 low — common in general English
**35. initial** — count: 1, TF-IDF: 89.05, IDF: 5.138788 🔵 low — common in general English
**36. significant** — count: 1, TF-IDF: 89.26, IDF: 5.150484 🔵 low — common in general English
**37. regular** — count: 1, TF-IDF: 90.53, IDF: 5.223687 🔵 low — common in general English
**38. nearly** — count: 1, TF-IDF: 90.64, IDF: 5.230037 🔵 low — common in general English
**39. producing** — count: 1, TF-IDF: 90.97, IDF: 5.24933 🔵 low — common in general English
**40. required** — count: 1, TF-IDF: 91.20, IDF: 5.262402 🔵 low — common in general English
**41. information** — count: 1, TF-IDF: 91.66, IDF: 5.28907 🔵 low — common in general English
**42. rejected** — count: 1, TF-IDF: 92.01, IDF: 5.309549 🔵 low — common in general English
**43. closing** — count: 1, TF-IDF: 92.38, IDF: 5.330455 🔵 low — common in general English
**44. consumption** — count: 1, TF-IDF: 92.62, IDF: 5.34464 🔵 low — common in general English
**45. plus** — count: 1, TF-IDF: 92.87, IDF: 5.359029 🔵 low — common in general English
**46. performance** — count: 1, TF-IDF: 93.00, IDF: 5.366301 🔵 low — common in general English
**47. believed** — count: 1, TF-IDF: 95.29, IDF: 5.498791 🔵 low — common in general English
**48. assistance** — count: 1, TF-IDF: 95.44, IDF: 5.507159 🔵 low — common in general English
**49. raising** — count: 1, TF-IDF: 95.73, IDF: 5.524108 🔵 low — common in general English
**50. failed** — count: 1, TF-IDF: 95.73, IDF: 5.524108 🔵 low — common in general English

---

## Full Ranked Table (normalized)

All 7,632 lemmatized content terms, sorted by TF-IDF descending. Plural/possessive surface variants have been merged into a single lemma row (counts summed); the original un-lemmatized table (8,673 raw word-forms) has been superseded by this version.

| Rank | Word | Count | TF-IDF | IDF | Band | Variants merged |
|------|------|-------|--------|-----|------|----------------|
| 1 | **dharma** | 409 | 67,972.93 | 9.59 | 🔴 extremely high — text-exclusive | - |
| 2 | **buddha** | 364 | 60,494.25 | 9.59 | 🔴 extremely high — text-exclusive | buddha, buddhas |
| 3 | **teacher** | 373 | 57,529.73 | 8.899988 | 🔴 extremely high — text-exclusive | teacher, teachers |
| 4 | **teaching** | 218 | 36,230.07 | 9.59 | 🟠 very high — domain-specific | teaching, teachings |
| 5 | **like** | 397 | 35,724.30 | 5.192532 | 🟠 very high — domain-specific | like, likes |
| 6 | **person** | 260 | 32,219.69 | 7.150788 | 🟠 very high — domain-specific | people, person, persons |
| 7 | **mind** | 256 | 31,724.00 | 7.150788 | 🟠 very high — domain-specific | mind, minds |
| 8 | **practice** | 236 | 27,769.08 | 6.789775 | 🟠 very high — domain-specific | practice, practices |
| 9 | **action** | 340 | 26,092.45 | 4.428349 | 🟠 very high — domain-specific | action, actions |
| 10 | **realm** | 149 | 24,762.75 | 9.59 | 🟠 very high — domain-specific | realm, realms |
| 11 | **yourself** | 154 | 24,519.98 | 9.18767 | 🟠 very high — domain-specific | - |
| 12 | **compassion** | 147 | 24,438.36 | 9.593135 | 🟠 very high — domain-specific | - |
| 13 | **suffering** | 192 | 24,095.69 | 7.24176 | 🟠 very high — domain-specific | suffering, sufferings |
| 14 | **life** | 240 | 22,905.14 | 5.507159 | 🟠 very high — domain-specific | - |
| 15 | **time** | 329 | 21,906.07 | 3.842151 | 🟠 very high — domain-specific | time, times |
| 16 | **without** | 266 | 21,766.06 | 4.721762 | 🟠 very high — domain-specific | - |
| 17 | **bodhicitta** | 130 | 21,605.09 | 9.59 | 🟠 very high — domain-specific | - |
| 18 | **never** | 197 | 21,562.63 | 6.31599 | 🟠 very high — domain-specific | - |
| 19 | **jewel** | 128 | 21,272.70 | 9.59 | 🟠 very high — domain-specific | jewel, jewels |
| 20 | **merit** | 142 | 20,524.28 | 8.340372 | 🟠 very high — domain-specific | merit, merits |
| 21 | **practise** | 123 | 20,448.42 | 9.593135 | 🟠 very high — domain-specific | - |
| 22 | **body** | 180 | 19,761.32 | 6.335039 | 🟠 very high — domain-specific | bodies, body |
| 23 | **path** | 145 | 19,603.49 | 7.801376 | 🟠 very high — domain-specific | path, paths |
| 24 | **refuge** | 129 | 18,989.90 | 8.494523 | 🟠 very high — domain-specific | refuge, refuges |
| 25 | **being** | 258 | 18,491.01 | 4.13568 | 🟠 very high — domain-specific | - |
| 26 | **death** | 129 | 18,346.78 | 8.206841 | 🟠 very high — domain-specific | death, deaths |
| 27 | **king** | 144 | 17,955.68 | 7.19524 | 🟠 very high — domain-specific | king, kings |
| 28 | **hell** | 114 | 17,582.81 | 8.899988 | 🟠 very high — domain-specific | hell, hells |
| 29 | **word** | 128 | 16,963.21 | 7.647225 | 🟠 very high — domain-specific | word, words |
| 30 | **negative** | 166 | 16,949.33 | 5.891833 | 🟠 very high — domain-specific | - |
| 31 | **offering** | 180 | 16,498.55 | 5.28907 | 🟠 very high — domain-specific | offering, offerings |
| 32 | **bodhisattva** | 99 | 16,453.11 | 9.59 | 🟠 very high — domain-specific | bodhisattva, bodhisattvas |
| 33 | **whatever** | 132 | 16,260.33 | 7.108229 | 🟠 very high — domain-specific | - |
| 34 | **wisdom** | 109 | 16,045.73 | 8.494523 | 🟠 very high — domain-specific | wisdom, wisdoms |
| 35 | **hundred** | 124 | 16,015.88 | 7.453069 | 🟠 very high — domain-specific | hundred, hundreds |
| 36 | **friend** | 96 | 15,959.74 | 9.593135 | 🟠 very high — domain-specific | friend, friends |
| 37 | **god** | 96 | 15,959.74 | 9.593135 | 🟠 very high — domain-specific | god, gods |
| 38 | **mother** | 96 | 15,954.53 | 9.59 | 🟠 very high — domain-specific | mother, mothers |
| 39 | **thought** | 152 | 15,866.97 | 6.023602 | 🟠 very high — domain-specific | thought, thoughts |
| 40 | **perfect** | 97 | 15,444.41 | 9.18767 | 🟠 very high — domain-specific | perfect, perfects |
| 41 | **way** | 184 | 15,193.52 | 4.764821 | 🟠 very high — domain-specific | way, ways |
| 42 | **come** | 178 | 15,120.58 | 4.901787 | 🟠 very high — domain-specific | come, comes |
| 43 | **faith** | 108 | 14,942.45 | 7.983697 | 🟠 very high — domain-specific | - |
| 44 | **make** | 211 | 14,759.13 | 4.036307 | 🟠 very high — domain-specific | make, makes |
| 45 | **live** | 134 | 14,666.97 | 6.31599 | 🟠 very high — domain-specific | live, lives |
| 46 | **disciple** | 86 | 14,292.60 | 9.59 | 🟠 very high — domain-specific | disciple, disciples |
| 47 | **once** | 140 | 14,235.44 | 5.867442 | 🟠 very high — domain-specific | - |
| 48 | **say** | 185 | 14,010.55 | 4.37008 | 🟠 very high — domain-specific | say, says |
| 49 | **instruction** | 83 | 13,798.53 | 9.593135 | 🟠 very high — domain-specific | instruction, instructions |
| 50 | **monk** | 82 | 13,627.82 | 9.59 | 🟠 very high — domain-specific | monk, monks |
| 51 | **human** | 98 | 13,397.02 | 7.888387 | 🟠 very high — domain-specific | human, humans |
| 52 | **thing** | 113 | 13,180.98 | 6.730934 | 🟠 very high — domain-specific | thing, things |
| 53 | **samsara** | 79 | 13,129.25 | 9.59 | 🟠 very high — domain-specific | - |
| 54 | **happiness** | 77 | 12,796.86 | 9.59 | 🟠 very high — domain-specific | - |
| 55 | **reborn** | 75 | 12,464.47 | 9.59 | 🟠 very high — domain-specific | - |
| 56 | **evil** | 74 | 12,302.30 | 9.593135 | 🟠 very high — domain-specific | evil, evils |
| 57 | **day** | 164 | 12,234.83 | 4.304868 | 🟠 very high — domain-specific | day, days |
| 58 | **everything** | 96 | 12,214.35 | 7.341843 | 🟠 very high — domain-specific | - |
| 59 | **heart** | 99 | 11,993.17 | 6.990446 | 🟠 very high — domain-specific | heart, hearts |
| 60 | **themselve** | 72 | 11,965.89 | 9.59 | 🟠 very high — domain-specific | - |
| 61 | **thousand** | 96 | 11,896.50 | 7.150788 | 🟠 very high — domain-specific | thousand, thousands |
| 62 | **deity** | 71 | 11,799.70 | 9.59 | 🟠 very high — domain-specific | deities, deity |
| 63 | **many** | 146 | 11,654.17 | 4.60611 | 🟠 very high — domain-specific | - |
| 64 | **kalpa** | 70 | 11,633.51 | 9.59 | 🟠 very high — domain-specific | kalpa, kalpas |
| 65 | **wealth** | 76 | 11,427.98 | 8.676844 | 🟠 very high — domain-specific | - |
| 66 | **hand** | 103 | 11,413.93 | 6.394462 | 🟠 very high — domain-specific | hand, hands |
| 67 | **place** | 128 | 11,398.95 | 5.138788 | 🟠 very high — domain-specific | place, places |
| 68 | **meditate** | 68 | 11,301.12 | 9.59 | 🟠 very high — domain-specific | meditate, meditates |
| 69 | **meditation** | 68 | 11,301.12 | 9.59 | 🟠 very high — domain-specific | meditation, meditations |
| 70 | **take** | 166 | 11,261.53 | 3.914671 | 🟠 very high — domain-specific | take, takes |
| 71 | **prayer** | 67 | 11,138.57 | 9.593135 | 🟠 very high — domain-specific | prayer, prayers |
| 72 | **past** | 138 | 11,048.46 | 4.619856 | 🟠 very high — domain-specific | - |
| 73 | **lama** | 66 | 10,972.32 | 9.593135 | 🟠 very high — domain-specific | lama, lamas |
| 74 | **spiritual** | 66 | 10,968.74 | 9.59 | 🟠 very high — domain-specific | - |
| 75 | **vajra** | 66 | 10,968.74 | 9.59 | 🟠 very high — domain-specific | vajra, vajras |
| 76 | **master** | 77 | 10,653.42 | 7.983697 | 🟠 very high — domain-specific | master, masters |
| 77 | **mantra** | 63 | 10,470.16 | 9.59 | 🟠 very high — domain-specific | mantra, mantras |
| 78 | **vow** | 63 | 10,470.16 | 9.59 | 🟠 very high — domain-specific | vow, vows |
| 79 | **having** | 107 | 10,443.96 | 5.632322 | 🟠 very high — domain-specific | - |
| 80 | **effect** | 127 | 10,333.82 | 4.695295 | 🟠 very high — domain-specific | effect, effects |
| 81 | **die** | 67 | 10,333.76 | 8.899988 | 🟠 very high — domain-specific | - |
| 82 | **buddhahood** | 62 | 10,303.97 | 9.59 | 🟠 very high — domain-specific | - |
| 83 | **recite** | 62 | 10,303.97 | 9.59 | 🟠 very high — domain-specific | recite, recites |
| 84 | **again** | 116 | 10,183.83 | 5.065927 | 🟠 very high — domain-specific | - |
| 85 | **love** | 66 | 10,179.52 | 8.899988 | 🟠 very high — domain-specific | love, loves |
| 86 | **born** | 61 | 10,141.09 | 9.593135 | 🟠 very high — domain-specific | - |
| 87 | **perfection** | 61 | 10,137.77 | 9.59 | 🟠 very high — domain-specific | perfection, perfections |
| 88 | **demon** | 61 | 10,137.77 | 9.59 | 🟠 very high — domain-specific | demon, demons |
| 89 | **pure** | 72 | 10,093.10 | 8.089058 | 🟠 very high — domain-specific | - |
| 90 | **always** | 89 | 10,063.99 | 6.525082 | 🟠 very high — domain-specific | - |
| 91 | **mila** | 60 | 9,974.84 | 9.593135 | 🟡 high — specialist register | - |
| 92 | **man** | 77 | 9,945.35 | 7.453069 | 🟡 high — specialist register | man, men |
| 93 | **taking** | 111 | 9,862.79 | 5.127227 | 🟡 high — specialist register | - |
| 94 | **flesh** | 59 | 9,808.59 | 9.593135 | 🟡 high — specialist register | - |
| 95 | **other** | 178 | 9,798.28 | 3.176403 | 🟡 high — specialist register | - |
| 96 | **feel** | 90 | 9,793.18 | 6.278949 | 🟡 high — specialist register | feel, feels |
| 97 | **power** | 107 | 9,782.58 | 5.275647 | 🟡 high — specialist register | power, powers |
| 98 | **head** | 102 | 9,647.73 | 5.457969 | 🟡 high — specialist register | head, heads |
| 99 | **see** | 119 | 9,644.75 | 4.676811 | 🟡 high — specialist register | see, sees |
| 100 | **liberation** | 58 | 9,642.34 | 9.593135 | 🟡 high — specialist register | - |
| 101 | **animal** | 79 | 9,621.98 | 7.028186 | 🟡 high — specialist register | animal, animals |
| 102 | **get** | 111 | 9,604.54 | 4.992978 | 🟡 high — specialist register | get, gets |
| 103 | **called** | 116 | 9,507.43 | 4.729454 | 🟡 high — specialist register | - |
| 104 | **enemy** | 63 | 9,473.19 | 8.676844 | 🟡 high — specialist register | enemies, enemy |
| 105 | **kind** | 86 | 9,441.52 | 6.335039 | 🟡 high — specialist register | kind, kinds |
| 106 | **food** | 107 | 9,354.04 | 5.044535 | 🟡 high — specialist register | food, foods |
| 107 | **wrong** | 71 | 9,324.39 | 7.578232 | 🟡 high — specialist register | - |
| 108 | **too** | 109 | 9,303.06 | 4.92499 | 🟡 high — specialist register | - |
| 109 | **blessing** | 58 | 9,234.80 | 9.18767 | 🟡 high — specialist register | blessing, blessings |
| 110 | **visualize** | 55 | 9,143.60 | 9.593135 | 🟡 high — specialist register | - |
| 111 | **transference** | 55 | 9,140.61 | 9.59 | 🟡 high — specialist register | - |
| 112 | **realization** | 64 | 9,102.28 | 8.206841 | 🟡 high — specialist register | realization, realizations |
| 113 | **right** | 102 | 9,093.84 | 5.144619 | 🟡 high — specialist register | - |
| 114 | **positive** | 91 | 9,090.69 | 5.764494 | 🟡 high — specialist register | - |
| 115 | **moment** | 84 | 9,088.30 | 6.243231 | 🟡 high — specialist register | moment, moments |
| 116 | **himself** | 67 | 9,058.16 | 7.801376 | 🟡 high — specialist register | - |
| 117 | **water** | 87 | 9,019.36 | 5.982217 | 🟡 high — specialist register | water, waters |
| 118 | **nothing** | 86 | 8,956.52 | 6.009616 | 🟡 high — specialist register | - |
| 119 | **mean** | 88 | 8,929.73 | 5.855466 | 🟡 high — specialist register | mean, means |
| 120 | **tantra** | 53 | 8,808.23 | 9.59 | 🟡 high — specialist register | tantra, tantras |
| 121 | **obscuration** | 53 | 8,808.23 | 9.59 | 🟡 high — specialist register | - |
| 122 | **think** | 103 | 8,799.37 | 4.929696 | 🟡 high — specialist register | think, thinks |
| 123 | **single** | 84 | 8,748.23 | 6.009616 | 🟡 high — specialist register | - |
| 124 | **true** | 72 | 8,722.31 | 6.990446 | 🟡 high — specialist register | - |
| 125 | **harm** | 69 | 8,659.39 | 7.24176 | 🟡 high — specialist register | harm, harms |
| 126 | **quality** | 86 | 8,640.61 | 5.797646 | 🟡 high — specialist register | qualities, quality |
| 127 | **bring** | 93 | 8,568.41 | 5.316469 | 🟡 high — specialist register | bring, brings |
| 128 | **ordinary** | 84 | 8,558.91 | 5.879563 | 🟡 high — specialist register | - |
| 129 | **benefit** | 89 | 8,546.72 | 5.54135 | 🟡 high — specialist register | benefit, benefits |
| 130 | **every** | 84 | 8,439.66 | 5.797646 | 🟡 high — specialist register | - |
| 131 | **follow** | 80 | 8,390.65 | 6.052176 | 🟡 high — specialist register | follow, follows |
| 132 | **father** | 54 | 8,328.70 | 8.899988 | 🟡 high — specialist register | father, fathers |
| 133 | **essence** | 50 | 8,312.37 | 9.593135 | 🟡 high — specialist register | essence, essences |
| 134 | **sutra** | 50 | 8,309.65 | 9.59 | 🟡 high — specialist register | sutra, sutras |
| 135 | **jetsun** | 50 | 8,309.65 | 9.59 | 🟡 high — specialist register | - |
| 136 | **accomplishment** | 52 | 8,279.48 | 9.18767 | 🟡 high — specialist register | accomplishment, accomplishments |
| 137 | **state** | 110 | 8,154.06 | 4.277469 | 🟡 high — specialist register | state, states |
| 138 | **secret** | 61 | 8,011.09 | 7.578232 | 🟡 high — specialist register | secret, secrets |
| 139 | **down** | 121 | 8,007.22 | 3.818584 | 🟡 high — specialist register | down, downs |
| 140 | **cannot** | 84 | 8,004.62 | 5.498791 | 🟡 high — specialist register | - |
| 141 | **rebirth** | 48 | 7,977.26 | 9.59 | 🟡 high — specialist register | rebirth, rebirths |
| 142 | **samaya** | 48 | 7,977.26 | 9.59 | 🟡 high — specialist register | samaya, samayas |
| 143 | **preta** | 48 | 7,977.26 | 9.59 | 🟡 high — specialist register | preta, pretas |
| 144 | **profound** | 50 | 7,961.03 | 9.18767 | 🟡 high — specialist register | - |
| 145 | **know** | 78 | 7,898.99 | 5.843631 | 🟡 high — specialist register | know, knows |
| 146 | **harmful** | 57 | 7,886.29 | 7.983697 | 🟡 high — specialist register | - |
| 147 | **away** | 78 | 7,852.10 | 5.808946 | 🟡 high — specialist register | - |
| 148 | **lineage** | 47 | 7,811.07 | 9.59 | 🟡 high — specialist register | lineage, lineages |
| 149 | **whole** | 78 | 7,748.64 | 5.732405 | 🟡 high — specialist register | - |
| 150 | **become** | 89 | 7,700.94 | 4.992978 | 🟡 high — specialist register | become, becomes |
| 151 | **someone** | 60 | 7,690.19 | 7.395911 | 🟡 high — specialist register | - |
| 152 | **tibet** | 46 | 7,644.88 | 9.59 | 🟡 high — specialist register | - |
| 153 | **empowerment** | 46 | 7,644.88 | 9.59 | 🟡 high — specialist register | empowerment, empowerments |
| 154 | **protector** | 46 | 7,644.88 | 9.59 | 🟡 high — specialist register | protector, protectors |
| 155 | **mandala** | 46 | 7,644.88 | 9.59 | 🟡 high — specialist register | mandala, mandalas |
| 156 | **put** | 94 | 7,571.49 | 4.647928 | 🟡 high — specialist register | put, puts |
| 157 | **child** | 49 | 7,557.52 | 8.899988 | 🟡 high — specialist register | child, children |
| 158 | **root** | 55 | 7,518.74 | 7.888387 | 🟡 high — specialist register | root, roots |
| 159 | **therefore** | 69 | 7,444.59 | 6.225839 | 🟡 high — specialist register | - |
| 160 | **experience** | 63 | 7,412.93 | 6.789775 | 🟡 high — specialist register | experience, experiences |
| 161 | **taught** | 48 | 7,403.29 | 8.899988 | 🟡 high — specialist register | - |
| 162 | **act** | 80 | 7,390.07 | 5.330455 | 🟡 high — specialist register | act, acts |
| 163 | **doing** | 69 | 7,384.29 | 6.175409 | 🟡 high — specialist register | - |
| 164 | **give** | 91 | 7,313.10 | 4.637308 | 🟡 high — specialist register | give, gives |
| 165 | **devotion** | 44 | 7,312.49 | 9.59 | 🟡 high — specialist register | devotion, devotions |
| 166 | **ever** | 64 | 7,289.85 | 6.57271 | 🟡 high — specialist register | - |
| 167 | **off** | 96 | 7,270.34 | 4.37008 | 🟡 high — specialist register | - |
| 168 | **old** | 69 | 7,202.77 | 6.023602 | 🟡 high — specialist register | - |
| 169 | **nature** | 59 | 7,186.04 | 7.028186 | 🟡 high — specialist register | nature, natures |
| 170 | **blood** | 51 | 7,149.28 | 8.089058 | 🟡 high — specialist register | - |
| 171 | **practising** | 43 | 7,148.63 | 9.593135 | 🟡 high — specialist register | - |
| 172 | **teach** | 43 | 7,148.63 | 9.593135 | 🟡 high — specialist register | teach, teaches |
| 173 | **guru** | 43 | 7,146.30 | 9.59 | 🟡 high — specialist register | - |
| 174 | **precious** | 56 | 7,125.04 | 7.341843 | 🟡 high — specialist register | - |
| 175 | **eye** | 52 | 7,108.63 | 7.888387 | 🟡 high — specialist register | eye, eyes |
| 176 | **spirit** | 58 | 7,103.66 | 7.067407 | 🟡 high — specialist register | spirit, spirits |
| 177 | **son** | 46 | 7,094.82 | 8.899988 | 🟡 high — specialist register | son, sons |
| 178 | **find** | 75 | 7,083.56 | 5.45 | 🟡 high — specialist register | find, finds |
| 179 | **attain** | 51 | 7,056.16 | 7.983697 | 🟡 high — specialist register | - |
| 180 | **meaning** | 54 | 7,031.39 | 7.513694 | 🟡 high — specialist register | - |
| 181 | **transcendent** | 42 | 6,980.11 | 9.59 | 🟡 high — specialist register | - |
| 182 | **world** | 103 | 6,966.34 | 3.902776 | 🟡 high — specialist register | world, worlds |
| 183 | **until** | 92 | 6,941.83 | 4.354037 | 🟡 high — specialist register | - |
| 184 | **look** | 70 | 6,903.88 | 5.691163 | 🟡 high — specialist register | look, looks |
| 185 | **asked** | 90 | 6,897.94 | 4.422651 | 🟡 high — specialist register | - |
| 186 | **method** | 58 | 6,855.53 | 6.820546 | 🟡 high — specialist register | method, methods |
| 187 | **sky** | 41 | 6,816.14 | 9.593135 | 🟡 high — specialist register | skies, sky |
| 188 | **authentic** | 41 | 6,813.91 | 9.59 | 🟡 high — specialist register | - |
| 189 | **killing** | 44 | 6,786.35 | 8.899988 | 🟡 high — specialist register | - |
| 190 | **tree** | 48 | 6,728.73 | 8.089058 | 🟡 high — specialist register | tree, trees |
| 191 | **form** | 75 | 6,686.65 | 5.144619 | 🟡 high — specialist register | form, forms |
| 192 | **wish** | 54 | 6,651.95 | 7.108229 | 🟡 high — specialist register | wish, wishes |
| 193 | **wheel** | 40 | 6,649.89 | 9.593135 | 🟡 high — specialist register | wheel, wheels |
| 194 | **sublime** | 40 | 6,647.72 | 9.59 | 🟡 high — specialist register | - |
| 195 | **end** | 104 | 6,646.48 | 3.687773 | 🟡 high — specialist register | end, ends |
| 196 | **speech** | 64 | 6,634.93 | 5.982217 | 🟡 high — specialist register | - |
| 197 | **freedom** | 54 | 6,577.05 | 7.028186 | 🟡 high — specialist register | freedom, freedoms |
| 198 | **nectar** | 39 | 6,481.53 | 9.59 | 🟡 high — specialist register | - |
| 199 | **replied** | 56 | 6,452.36 | 6.648696 | 🟡 high — specialist register | - |
| 200 | **best** | 68 | 6,431.82 | 5.457969 | 🟡 high — specialist register | - |
| 201 | **anything** | 61 | 6,413.30 | 6.066775 | 🟡 high — specialist register | - |
| 202 | **point** | 78 | 6,398.16 | 4.733323 | 🟡 high — specialist register | point, points |
| 203 | **free** | 71 | 6,337.24 | 5.150484 | 🟡 high — specialist register | - |
| 204 | **eat** | 43 | 6,329.97 | 8.494523 | 🟡 high — specialist register | eat, eats |
| 205 | **myself** | 38 | 6,317.40 | 9.593135 | 🟡 high — specialist register | - |
| 206 | **joy** | 38 | 6,317.40 | 9.593135 | 🟡 high — specialist register | joy, joys |
| 207 | **emptiness** | 38 | 6,315.33 | 9.59 | 🟡 high — specialist register | - |
| 208 | **daughter** | 38 | 6,315.33 | 9.59 | 🟡 high — specialist register | daughter, daughters |
| 209 | **view** | 67 | 6,256.51 | 5.388443 | 🟡 high — specialist register | view, views |
| 210 | **fault** | 45 | 6,226.02 | 7.983697 | 🟡 high — specialist register | fault, faults |
| 211 | **while** | 98 | 6,199.45 | 3.650336 | 🟡 high — specialist register | - |
| 212 | **vehicle** | 49 | 6,190.85 | 7.29055 | 🟡 high — specialist register | vehicle, vehicles |
| 213 | **because** | 99 | 6,177.07 | 3.600421 | 🟡 high — specialist register | - |
| 214 | **lord** | 47 | 6,172.48 | 7.578232 | 🟡 high — specialist register | lord, lords |
| 215 | **possession** | 37 | 6,149.14 | 9.59 | 🟡 high — specialist register | possession, possessions |
| 216 | **killed** | 51 | 6,146.16 | 6.954078 | 🟡 high — specialist register | - |
| 217 | **want** | 69 | 6,103.74 | 5.104499 | 🟡 high — specialist register | want, wants |
| 218 | **left** | 64 | 6,080.42 | 5.482261 | 🟡 high — specialist register | - |
| 219 | **text** | 42 | 6,070.56 | 8.340372 | 🟡 high — specialist register | text, texts |
| 220 | **went** | 61 | 6,059.83 | 5.732405 | 🟡 high — specialist register | - |
| 221 | **pain** | 40 | 6,014.73 | 8.676844 | 🟡 high — specialist register | pain, pains |
| 222 | **suffer** | 50 | 5,995.24 | 6.918987 | 🟡 high — specialist register | suffer, suffers |
| 223 | **attachment** | 36 | 5,984.90 | 9.593135 | 🟡 high — specialist register | attachment, attachments |
| 224 | **together** | 61 | 5,984.68 | 5.66131 | 🟡 high — specialist register | - |
| 225 | **impermanence** | 36 | 5,982.95 | 9.59 | 🟡 high — specialist register | - |
| 226 | **oddiyana** | 36 | 5,982.95 | 9.59 | 🟡 high — specialist register | - |
| 227 | **innumerable** | 36 | 5,982.95 | 9.59 | 🟡 high — specialist register | - |
| 228 | **yoga** | 36 | 5,982.95 | 9.59 | 🟡 high — specialist register | yoga, yogas |
| 229 | **came** | 64 | 5,976.37 | 5.388443 | 🟡 high — specialist register | - |
| 230 | **much** | 80 | 5,964.71 | 4.302346 | 🟡 high — specialist register | - |
| 231 | **really** | 56 | 5,946.46 | 6.127399 | 🟡 high — specialist register | - |
| 232 | **noble** | 37 | 5,891.17 | 9.18767 | 🟡 high — specialist register | - |
| 233 | **anyone** | 44 | 5,831.10 | 7.647225 | 🟡 high — specialist register | - |
| 234 | **vajrasattva** | 35 | 5,816.75 | 9.59 | 🟡 high — specialist register | vajrasattva, vajrasattvas |
| 235 | **birth** | 35 | 5,816.75 | 9.59 | 🟡 high — specialist register | - |
| 236 | **naropa** | 35 | 5,816.75 | 9.59 | 🟡 high — specialist register | - |
| 237 | **present** | 69 | 5,802.49 | 4.85256 | 🟡 high — specialist register | - |
| 238 | **light** | 61 | 5,769.72 | 5.457969 | 🟡 high — specialist register | light, lights |
| 239 | **concentration** | 39 | 5,741.13 | 8.494523 | 🟡 high — specialist register | concentration, concentrations |
| 240 | **advantage** | 52 | 5,726.32 | 6.354457 | 🟡 high — specialist register | advantage, advantages |
| 241 | **supreme** | 46 | 5,700.41 | 7.150788 | 🟡 high — specialist register | - |
| 242 | **cause** | 60 | 5,700.40 | 5.482261 | 🟡 high — specialist register | - |
| 243 | **lower** | 84 | 5,688.69 | 3.907856 | 🟡 high — specialist register | - |
| 244 | **effort** | 59 | 5,674.74 | 5.550084 | 🟡 high — specialist register | effort, efforts |
| 245 | **prostration** | 34 | 5,650.56 | 9.59 | 🟡 high — specialist register | prostration, prostrations |
| 246 | **rinpoche** | 34 | 5,650.56 | 9.59 | 🟡 high — specialist register | - |
| 247 | **worldly** | 34 | 5,650.56 | 9.59 | 🟡 high — specialist register | - |
| 248 | **said** | 222 | 5,631.61 | 1.463813 | 🟡 high — specialist register | - |
| 249 | **living** | 49 | 5,623.76 | 6.622721 | 🟡 high — specialist register | - |
| 250 | **done** | 57 | 5,621.73 | 5.691163 | 🟡 high — specialist register | - |
| 251 | **thinking** | 43 | 5,599.07 | 7.513694 | 🟡 high — specialist register | - |
| 252 | **imagine** | 36 | 5,552.47 | 8.899988 | 🟡 high — specialist register | imagine, imagines |
| 253 | **giving** | 56 | 5,542.91 | 5.711571 | 🟡 high — specialist register | - |
| 254 | **rich** | 42 | 5,515.84 | 7.578232 | 🟡 high — specialist register | rich, riches |
| 255 | **doctrine** | 33 | 5,486.16 | 9.593135 | 🟡 high — specialist register | doctrine, doctrines |
| 256 | **emotion** | 33 | 5,484.37 | 9.59 | 🟡 high — specialist register | emotion, emotions |
| 257 | **moon** | 33 | 5,484.37 | 9.59 | 🟡 high — specialist register | - |
| 258 | **deed** | 33 | 5,484.37 | 9.59 | 🟡 high — specialist register | deed, deeds |
| 259 | **atisa** | 33 | 5,484.37 | 9.59 | 🟡 high — specialist register | - |
| 260 | **hatred** | 33 | 5,484.37 | 9.59 | 🟡 high — specialist register | - |
| 261 | **confess** | 33 | 5,484.37 | 9.59 | 🟡 high — specialist register | - |
| 262 | **going** | 61 | 5,463.50 | 5.168289 | 🟡 high — specialist register | - |
| 263 | **perfectly** | 38 | 5,404.48 | 8.206841 | 🟡 high — specialist register | - |
| 264 | **kill** | 38 | 5,404.48 | 8.206841 | 🟡 high — specialist register | kill, kills |
| 265 | **use** | 66 | 5,361.83 | 4.68786 | 🟡 high — specialist register | use, uses |
| 266 | **instead** | 55 | 5,341.54 | 5.604151 | 🟡 high — specialist register | - |
| 267 | **consciousness** | 32 | 5,319.91 | 9.593135 | 🟡 high — specialist register | consciousness, consciousnesses |
| 268 | **geshe** | 32 | 5,318.18 | 9.59 | 🟡 high — specialist register | - |
| 269 | **powerful** | 42 | 5,306.44 | 7.29055 | 🟡 high — specialist register | - |
| 270 | **vast** | 40 | 5,301.00 | 7.647225 | 🟡 high — specialist register | - |
| 271 | **important** | 56 | 5,296.80 | 5.457969 | 🟡 high — specialist register | - |
| 272 | **instant** | 33 | 5,254.28 | 9.18767 | 🟡 high — specialist register | instant, instants |
| 273 | **ten** | 49 | 5,230.11 | 6.159148 | 🟡 high — specialist register | ten, tens |
| 274 | **don** | 40 | 5,208.44 | 7.513694 | 🟡 high — specialist register | - |
| 275 | **accumulation** | 36 | 5,203.34 | 8.340372 | 🟡 high — specialist register | accumulation, accumulations |
| 276 | **dedicate** | 31 | 5,153.67 | 9.593135 | 🟡 high — specialist register | - |
| 277 | **conqueror** | 31 | 5,151.98 | 9.59 | 🟡 high — specialist register | conqueror, conquerors |
| 278 | **woman** | 31 | 5,151.98 | 9.59 | 🟡 high — specialist register | woman, women |
| 279 | **brahmin** | 31 | 5,151.98 | 9.59 | 🟡 high — specialist register | brahmin, brahmins |
| 280 | **whether** | 64 | 5,151.12 | 4.644375 | 🟡 high — specialist register | - |
| 281 | **perception** | 39 | 5,121.85 | 7.578232 | 🟡 high — specialist register | perception, perceptions |
| 282 | **listen** | 34 | 5,112.52 | 8.676844 | 🟡 high — specialist register | - |
| 283 | **activity** | 53 | 5,105.74 | 5.558895 | 🟡 high — specialist register | activities, activity |
| 284 | **infinite** | 32 | 5,095.06 | 9.18767 | 🟡 high — specialist register | - |
| 285 | **pile** | 33 | 5,089.76 | 8.899988 | 🟡 high — specialist register | pile, piles |
| 286 | **why** | 47 | 5,070.96 | 6.225839 | 🟡 high — specialist register | - |
| 287 | **sun** | 45 | 5,070.60 | 6.502093 | 🟡 high — specialist register | sun, suns |
| 288 | **need** | 62 | 5,065.09 | 4.714128 | 🟡 high — specialist register | need, needs |
| 289 | **different** | 50 | 5,043.30 | 5.820374 | 🟡 high — specialist register | - |
| 290 | **fire** | 45 | 5,035.94 | 6.457641 | 🟡 high — specialist register | fire, fires |
| 291 | **toward** | 49 | 5,035.16 | 5.929574 | 🟡 high — specialist register | toward, towards |
| 292 | **bad** | 47 | 5,029.88 | 6.175409 | 🟡 high — specialist register | - |
| 293 | **flower** | 30 | 4,987.42 | 9.593135 | 🟡 high — specialist register | flower, flowers |
| 294 | **tradition** | 30 | 4,987.42 | 9.593135 | 🟡 high — specialist register | tradition, traditions |
| 295 | **marpa** | 30 | 4,985.79 | 9.59 | 🟡 high — specialist register | - |
| 296 | **purify** | 30 | 4,985.79 | 9.59 | 🟡 high — specialist register | purifies, purify |
| 297 | **syllable** | 30 | 4,985.79 | 9.59 | 🟡 high — specialist register | syllable, syllables |
| 298 | **generation** | 35 | 4,977.81 | 8.206841 | 🟡 high — specialist register | generation, generations |
| 299 | **turn** | 47 | 4,965.71 | 6.096628 | 🟡 high — specialist register | turn, turns |
| 300 | **longer** | 53 | 4,962.99 | 5.40348 | 🟡 high — specialist register | - |
| 301 | **land** | 49 | 4,962.18 | 5.843631 | 🟡 high — specialist register | land, lands |
| 302 | **most** | 70 | 4,949.04 | 4.079706 | 🟡 high — specialist register | - |
| 303 | **arise** | 32 | 4,935.53 | 8.899988 | 🟡 high — specialist register | - |
| 304 | **appear** | 44 | 4,907.63 | 6.436135 | 🟡 high — specialist register | appear, appears |
| 305 | **outer** | 33 | 4,857.88 | 8.494523 | 🟡 high — specialist register | - |
| 306 | **simply** | 44 | 4,830.54 | 6.335039 | 🟡 high — specialist register | - |
| 307 | **desire** | 41 | 4,824.29 | 6.789775 | 🟡 high — specialist register | desire, desires |
| 308 | **sarhsara** | 29 | 4,819.60 | 9.59 | 🟡 high — specialist register | - |
| 309 | **caus** | 29 | 4,819.60 | 9.59 | 🟡 high — specialist register | - |
| 310 | **recitation** | 29 | 4,819.60 | 9.59 | 🟡 high — specialist register | recitation, recitations |
| 311 | **tilopa** | 29 | 4,819.60 | 9.59 | 🟡 high — specialist register | - |
| 312 | **intention** | 45 | 4,790.68 | 6.143148 | 🟡 high — specialist register | intention, intentions |
| 313 | **inner** | 30 | 4,776.62 | 9.18767 | 🟡 high — specialist register | - |
| 314 | **hear** | 34 | 4,766.19 | 8.089058 | 🟡 high — specialist register | hear, hears |
| 315 | **sure** | 43 | 4,720.76 | 6.335039 | 🟡 high — specialist register | - |
| 316 | **mountain** | 37 | 4,707.61 | 7.341843 | 🟡 high — specialist register | mountain, mountains |
| 317 | **foot** | 37 | 4,707.61 | 7.341843 | 🟡 high — specialist register | feet, foot |
| 318 | **else** | 39 | 4,676.29 | 6.918987 | 🟡 high — specialist register | - |
| 319 | **enlightenment** | 28 | 4,653.40 | 9.59 | 🟡 high — specialist register | - |
| 320 | **dissolve** | 28 | 4,653.40 | 9.59 | 🟡 high — specialist register | dissolve, dissolves |
| 321 | **attained** | 29 | 4,617.40 | 9.18767 | 🟡 high — specialist register | - |
| 322 | **circumstance** | 29 | 4,617.40 | 9.18767 | 🟡 high — specialist register | circumstance, circumstances |
| 323 | **companion** | 29 | 4,617.40 | 9.18767 | 🟡 high — specialist register | companion, companions |
| 324 | **whenever** | 34 | 4,596.68 | 7.801376 | 🟡 high — specialist register | - |
| 325 | **red** | 41 | 4,573.02 | 6.436135 | 🟡 high — specialist register | - |
| 326 | **example** | 42 | 4,570.15 | 6.278949 | 🟡 high — specialist register | example, examples |
| 327 | **completely** | 38 | 4,556.38 | 6.918987 | 🟡 high — specialist register | - |
| 328 | **leave** | 43 | 4,554.48 | 6.111895 | 🟡 high — specialist register | leave, leaves |
| 329 | **everyone** | 35 | 4,520.61 | 7.453069 | 🟡 high — specialist register | - |
| 330 | **during** | 65 | 4,512.38 | 4.005887 | 🟡 high — specialist register | - |
| 331 | **universe** | 27 | 4,488.68 | 9.593135 | 🟡 high — specialist register | - |
| 332 | **practised** | 27 | 4,488.68 | 9.593135 | 🟡 high — specialist register | - |
| 333 | **practitioner** | 27 | 4,487.21 | 9.59 | 🟡 high — specialist register | practitioner, practitioners |
| 334 | **phas** | 27 | 4,487.21 | 9.59 | 🟡 high — specialist register | - |
| 335 | **drink** | 31 | 4,480.65 | 8.340372 | 🟡 high — specialist register | drink, drinks |
| 336 | **story** | 34 | 4,465.20 | 7.578232 | 🟡 high — specialist register | stories, story |
| 337 | **patience** | 28 | 4,458.18 | 9.18767 | 🟡 high — specialist register | - |
| 338 | **understand** | 35 | 4,453.15 | 7.341843 | 🟡 high — specialist register | understand, understands |
| 339 | **something** | 40 | 4,432.60 | 6.394462 | 🟡 high — specialist register | - |
| 340 | **earth** | 30 | 4,416.26 | 8.494523 | 🟡 high — specialist register | - |
| 341 | **front** | 35 | 4,392.44 | 7.24176 | 🟡 high — specialist register | - |
| 342 | **finally** | 36 | 4,384.70 | 7.028186 | 🟡 high — specialist register | - |
| 343 | **tell** | 37 | 4,373.36 | 6.820546 | 🟡 high — specialist register | tell, tells |
| 344 | **ask** | 41 | 4,353.66 | 6.127399 | 🟡 high — specialist register | ask, asks |
| 345 | **ocean** | 35 | 4,337.27 | 7.150788 | 🟡 high — specialist register | ocean, oceans |
| 346 | **truth** | 26 | 4,322.43 | 9.593135 | 🟡 high — specialist register | truth, truths |
| 347 | **meditating** | 26 | 4,321.02 | 9.59 | 🟡 high — specialist register | - |
| 348 | **ritual** | 26 | 4,321.02 | 9.59 | 🟡 high — specialist register | ritual, rituals |
| 349 | **sheep** | 28 | 4,318.59 | 8.899988 | 🟡 high — specialist register | - |
| 350 | **ground** | 37 | 4,297.83 | 6.702763 | 🟡 high — specialist register | - |
| 351 | **element** | 33 | 4,296.96 | 7.513694 | 🟡 high — specialist register | element, elements |
| 352 | **died** | 31 | 4,289.04 | 7.983697 | 🟡 high — specialist register | - |
| 353 | **sign** | 41 | 4,269.97 | 6.009616 | 🟡 high — specialist register | sign, signs |
| 354 | **let** | 39 | 4,268.74 | 6.31599 | 🟡 high — specialist register | let, lets |
| 355 | **making** | 54 | 4,260.69 | 4.552941 | 🟡 high — specialist register | - |
| 356 | **made** | 68 | 4,242.84 | 3.600421 | 🟡 high — specialist register | - |
| 357 | **help** | 56 | 4,220.33 | 4.348746 | 🟡 high — specialist register | help, helps |
| 358 | **beginning** | 46 | 4,210.93 | 5.282336 | 🟡 high — specialist register | - |
| 359 | **parent** | 43 | 4,204.24 | 5.641891 | 🟡 high — specialist register | parent, parents |
| 360 | **alone** | 38 | 4,171.83 | 6.335039 | 🟡 high — specialist register | - |
| 361 | **arousing** | 25 | 4,156.18 | 9.593135 | 🟡 high — specialist register | - |
| 362 | **karmic** | 25 | 4,154.82 | 9.59 | 🟡 high — specialist register | - |
| 363 | **generosity** | 25 | 4,154.82 | 9.59 | 🟡 high — specialist register | - |
| 364 | **tirthika** | 25 | 4,154.82 | 9.59 | 🟡 high — specialist register | tirthika, tirthikas |
| 365 | **creature** | 25 | 4,154.82 | 9.59 | 🟡 high — specialist register | creature, creatures |
| 366 | **another** | 56 | 4,139.31 | 4.265259 | 🟡 high — specialist register | - |
| 367 | **able** | 45 | 4,124.64 | 5.28907 | 🟡 high — specialist register | - |
| 368 | **seeing** | 31 | 4,108.28 | 7.647225 | 🟡 high — specialist register | - |
| 369 | **family** | 39 | 4,080.72 | 6.037787 | 🟡 high — specialist register | families, family |
| 370 | **result** | 55 | 4,077.03 | 4.277469 | 🟡 high — specialist register | result, results |
| 371 | **depth** | 34 | 4,056.79 | 6.885085 | 🟡 high — specialist register | depth, depths |
| 372 | **realized** | 35 | 4,048.90 | 6.675364 | 🟡 high — specialist register | - |
| 373 | **start** | 48 | 4,018.55 | 4.830961 | 🟡 high — specialist register | start, starts |
| 374 | **peerless** | 26 | 4,010.12 | 8.899988 | 🟡 high — specialist register | - |
| 375 | **dead** | 31 | 4,003.97 | 7.453069 | 🟡 high — specialist register | - |
| 376 | **develop** | 38 | 3,995.17 | 6.066775 | 🟡 high — specialist register | develop, develops |
| 377 | **arouse** | 24 | 3,988.63 | 9.59 | 🟡 high — specialist register | - |
| 378 | **torment** | 24 | 3,988.63 | 9.59 | 🟡 high — specialist register | torment, torments |
| 379 | **beautiful** | 24 | 3,988.63 | 9.59 | 🟡 high — specialist register | - |
| 380 | **future** | 52 | 3,988.04 | 4.425496 | 🟡 high — specialist register | - |
| 381 | **immense** | 25 | 3,980.52 | 9.18767 | 🟡 high — specialist register | - |
| 382 | **work** | 48 | 3,980.33 | 4.785024 | 🟡 high — specialist register | work, works |
| 383 | **particular** | 38 | 3,976.08 | 6.037787 | 🟡 high — specialist register | - |
| 384 | **appeared** | 37 | 3,928.91 | 6.127399 | 🟡 high — specialist register | - |
| 385 | **keep** | 44 | 3,913.97 | 5.132991 | 🟡 high — specialist register | - |
| 386 | **complete** | 41 | 3,878.01 | 5.457969 | 🟡 high — specialist register | complete, completes |
| 387 | **attitude** | 32 | 3,876.58 | 6.990446 | 🟡 high — specialist register | attitude, attitudes |
| 388 | **essential** | 32 | 3,876.58 | 6.990446 | 🟡 high — specialist register | - |
| 389 | **stone** | 28 | 3,873.97 | 7.983697 | 🟡 high — specialist register | stone, stones |
| 390 | **feeling** | 30 | 3,845.09 | 7.395911 | 🟡 high — specialist register | feeling, feelings |
| 391 | **absolute** | 28 | 3,827.72 | 7.888387 | 🟡 high — specialist register | - |
| 392 | **pleasure** | 23 | 3,823.69 | 9.593135 | 🟡 high — specialist register | pleasure, pleasures |
| 393 | **sleep** | 23 | 3,823.69 | 9.593135 | 🟡 high — specialist register | - |
| 394 | **buddhafield** | 23 | 3,822.44 | 9.59 | 🟡 high — specialist register | buddhafield, buddhafields |
| 395 | **heaven** | 23 | 3,822.44 | 9.59 | 🟡 high — specialist register | heaven, heavens |
| 396 | **siddha** | 23 | 3,822.44 | 9.59 | 🟡 high — specialist register | siddha, siddhas |
| 397 | **dedication** | 23 | 3,822.44 | 9.59 | 🟡 high — specialist register | dedication, dedications |
| 398 | **confession** | 23 | 3,822.44 | 9.59 | 🟡 high — specialist register | - |
| 399 | **piece** | 24 | 3,821.30 | 9.18767 | 🟡 high — specialist register | piece, pieces |
| 400 | **fruit** | 30 | 3,816.98 | 7.341843 | 🟡 high — specialist register | fruit, fruits |
| 401 | **difficult** | 41 | 3,812.88 | 5.366301 | 🟡 high — specialist register | - |
| 402 | **space** | 31 | 3,796.78 | 7.067407 | 🟡 high — specialist register | - |
| 403 | **object** | 27 | 3,784.91 | 8.089058 | 🟡 high — specialist register | object, objects |
| 404 | **face** | 39 | 3,781.41 | 5.594934 | 🟡 high — specialist register | face, faces |
| 405 | **became** | 34 | 3,767.71 | 6.394462 | 🟡 high — specialist register | - |
| 406 | **palace** | 25 | 3,759.20 | 8.676844 | 🟡 high — specialist register | palace, palaces |
| 407 | **perform** | 26 | 3,757.97 | 8.340372 | 🟡 high — specialist register | - |
| 408 | **age** | 26 | 3,757.97 | 8.340372 | 🟡 high — specialist register | age, ages |
| 409 | **given** | 48 | 3,755.59 | 4.514841 | 🟡 high — specialist register | - |
| 410 | **known** | 37 | 3,754.54 | 5.855466 | 🟡 high — specialist register | - |
| 411 | **lead** | 44 | 3,748.24 | 4.915644 | 🟡 high — specialist register | lead, leads |
| 412 | **found** | 37 | 3,746.96 | 5.843631 | 🟡 high — specialist register | - |
| 413 | **sometime** | 29 | 3,745.65 | 7.453069 | 🟡 high — specialist register | sometime, sometimes |
| 414 | **sort** | 31 | 3,735.90 | 6.954078 | 🟡 high — specialist register | sort, sorts |
| 415 | **white** | 40 | 3,730.08 | 5.381008 | 🟡 high — specialist register | white, whites |
| 416 | **remember** | 24 | 3,701.64 | 8.899988 | 🟡 high — specialist register | - |
| 417 | **truly** | 24 | 3,701.64 | 8.899988 | 🟡 high — specialist register | - |
| 418 | **taken** | 44 | 3,696.81 | 4.848203 | 🟡 high — specialist register | - |
| 419 | **around** | 55 | 3,691.34 | 3.872823 | 🟡 high — specialist register | - |
| 420 | **clothing** | 28 | 3,677.22 | 7.578232 | 🟡 high — specialist register | - |
| 421 | **beyond** | 33 | 3,668.68 | 6.415081 | 🟡 high — specialist register | - |
| 422 | **inconceivable** | 23 | 3,662.08 | 9.18767 | 🟡 high — specialist register | - |
| 423 | **bird** | 23 | 3,662.08 | 9.18767 | 🟡 high — specialist register | bird, birds |
| 424 | **stay** | 34 | 3,658.28 | 6.208745 | 🟡 high — specialist register | stay, stays |
| 425 | **kindness** | 22 | 3,657.44 | 9.593135 | 🟡 high — specialist register | - |
| 426 | **skilful** | 22 | 3,656.25 | 9.59 | 🟡 high — specialist register | - |
| 427 | **faculty** | 22 | 3,656.25 | 9.59 | 🟡 high — specialist register | - |
| 428 | **sangha** | 22 | 3,656.25 | 9.59 | 🟡 high — specialist register | - |
| 429 | **slightest** | 22 | 3,656.25 | 9.59 | 🟡 high — specialist register | - |
| 430 | **karma** | 22 | 3,656.25 | 9.59 | 🟡 high — specialist register | - |
| 431 | **beggar** | 22 | 3,656.25 | 9.59 | 🟡 high — specialist register | beggar, beggars |
| 432 | **happy** | 30 | 3,653.92 | 7.028186 | 🟡 high — specialist register | - |
| 433 | **set** | 53 | 3,652.21 | 3.976364 | 🟡 high — specialist register | set, sets |
| 434 | **must** | 45 | 3,650.03 | 4.68048 | 🟡 high — specialist register | - |
| 435 | **numerous** | 26 | 3,644.73 | 8.089058 | 🟡 high — specialist register | - |
| 436 | **fact** | 36 | 3,624.05 | 5.808946 | 🟡 high — specialist register | - |
| 437 | **diligence** | 28 | 3,616.49 | 7.453069 | 🟡 high — specialist register | - |
| 438 | **source** | 37 | 3,599.37 | 5.613454 | 🟡 high — specialist register | source, sources |
| 439 | **took** | 38 | 3,578.64 | 5.434252 | 🟡 high — specialist register | - |
| 440 | **avoid** | 35 | 3,573.65 | 5.891833 | 🟡 high — specialist register | - |
| 441 | **happen** | 31 | 3,557.89 | 6.622721 | 🟡 high — specialist register | happen, happens |
| 442 | **guide** | 27 | 3,545.89 | 7.578232 | 🟡 high — specialist register | guide, guides |
| 443 | **hum** | 24 | 3,533.01 | 8.494523 | 🟡 high — specialist register | - |
| 444 | **obstacle** | 24 | 3,533.01 | 8.494523 | 🟡 high — specialist register | obstacle, obstacles |
| 445 | **direction** | 33 | 3,504.16 | 6.127399 | 🟡 high — specialist register | direction, directions |
| 446 | **forth** | 22 | 3,502.85 | 9.18767 | 🟡 high — specialist register | - |
| 447 | **dust** | 22 | 3,502.85 | 9.18767 | 🟡 high — specialist register | - |
| 448 | **india** | 33 | 3,495.30 | 6.111895 | 🟡 high — specialist register | - |
| 449 | **mental** | 21 | 3,491.19 | 9.593135 | 🟡 high — specialist register | - |
| 450 | **dharmakaya** | 21 | 3,490.05 | 9.59 | 🟡 high — specialist register | - |
| 451 | **visualization** | 21 | 3,490.05 | 9.59 | 🟡 high — specialist register | visualization, visualizations |
| 452 | **clothe** | 21 | 3,490.05 | 9.59 | 🟡 high — specialist register | clothe, clothes |
| 453 | **cho** | 21 | 3,490.05 | 9.59 | 🟡 high — specialist register | - |
| 454 | **along** | 36 | 3,479.19 | 5.576752 | 🟡 high — specialist register | - |
| 455 | **ultimate** | 26 | 3,479.04 | 7.721333 | 🟡 high — specialist register | - |
| 456 | **level** | 48 | 3,476.44 | 4.179259 | 🟡 high — specialist register | level, levels |
| 457 | **empty** | 24 | 3,468.89 | 8.340372 | 🟡 high — specialist register | - |
| 458 | **lifetime** | 24 | 3,468.89 | 8.340372 | 🟡 high — specialist register | lifetime, lifetimes |
| 459 | **bear** | 30 | 3,456.62 | 6.648696 | 🟡 high — specialist register | bear, bears |
| 460 | **existence** | 26 | 3,445.65 | 7.647225 | 🟡 high — specialist register | - |
| 461 | **lived** | 25 | 3,417.61 | 7.888387 | 🟡 high — specialist register | - |
| 462 | **training** | 26 | 3,414.56 | 7.578232 | 🟡 high — specialist register | - |
| 463 | **continent** | 24 | 3,413.35 | 8.206841 | 🟡 high — specialist register | continent, continents |
| 464 | **train** | 24 | 3,413.35 | 8.206841 | 🟡 high — specialist register | train, trains |
| 465 | **within** | 43 | 3,407.38 | 4.57255 | 🟡 high — specialist register | - |
| 466 | **black** | 30 | 3,404.59 | 6.548613 | 🟡 high — specialist register | - |
| 467 | **since** | 52 | 3,385.50 | 3.756864 | 🟡 high — specialist register | - |
| 468 | **learned** | 24 | 3,364.37 | 8.089058 | 🟡 high — specialist register | - |
| 469 | **throughout** | 32 | 3,356.26 | 6.052176 | 🟡 high — specialist register | - |
| 470 | **accumulate** | 21 | 3,343.63 | 9.18767 | 🟡 high — specialist register | accumulate, accumulates |
| 471 | **natural** | 38 | 3,339.65 | 5.071347 | 🟡 high — specialist register | - |
| 472 | **river** | 31 | 3,335.49 | 6.208745 | 🟡 high — specialist register | river, rivers |
| 473 | **saw** | 34 | 3,329.97 | 5.651553 | 🟡 high — specialist register | saw, saws |
| 474 | **dream** | 20 | 3,324.95 | 9.593135 | 🟡 high — specialist register | dream, dreams |
| 475 | **dog** | 20 | 3,324.95 | 9.593135 | 🟡 high — specialist register | dog, dogs |
| 476 | **servant** | 20 | 3,324.95 | 9.593135 | 🟡 high — specialist register | servant, servants |
| 477 | **mantrayana** | 20 | 3,323.86 | 9.59 | 🟡 high — specialist register | - |
| 478 | **reciting** | 20 | 3,323.86 | 9.59 | 🟡 high — specialist register | - |
| 479 | **goe** | 20 | 3,323.86 | 9.59 | 🟡 high — specialist register | - |
| 480 | **dying** | 20 | 3,323.86 | 9.59 | 🟡 high — specialist register | - |
| 481 | **emanation** | 20 | 3,323.86 | 9.59 | 🟡 high — specialist register | emanation, emanations |
| 482 | **impermanent** | 20 | 3,323.86 | 9.59 | 🟡 high — specialist register | - |
| 483 | **ourselve** | 20 | 3,323.86 | 9.59 | 🟡 high — specialist register | - |
| 484 | **sadaprarudita** | 20 | 3,323.86 | 9.59 | 🟡 high — specialist register | - |
| 485 | **above** | 42 | 3,295.27 | 4.527381 | 🟡 high — specialist register | - |
| 486 | **part** | 46 | 3,295.15 | 4.13355 | 🟡 high — specialist register | part, parts |
| 487 | **insect** | 23 | 3,271.13 | 8.206841 | 🟡 high — specialist register | insect, insects |
| 488 | **hard** | 34 | 3,270.19 | 5.550084 | 🟡 high — specialist register | - |
| 489 | **better** | 38 | 3,265.28 | 4.958406 | 🟡 high — specialist register | - |
| 490 | **channel** | 25 | 3,255.27 | 7.513694 | 🟡 high — specialist register | channel, channels |
| 491 | **matter** | 31 | 3,251.38 | 6.052176 | 🟡 high — specialist register | - |
| 492 | **cold** | 29 | 3,234.57 | 6.436135 | 🟡 high — specialist register | - |
| 493 | **although** | 40 | 3,204.85 | 4.623322 | 🟡 high — specialist register | - |
| 494 | **intermediate** | 30 | 3,202.11 | 6.159148 | 🟡 high — specialist register | - |
| 495 | **real** | 39 | 3,186.10 | 4.714128 | 🟡 high — specialist register | - |
| 496 | **small** | 37 | 3,185.60 | 4.968162 | 🟡 high — specialist register | - |
| 497 | **constantly** | 20 | 3,184.41 | 9.18767 | 🟡 high — specialist register | - |
| 498 | **concept** | 24 | 3,180.60 | 7.647225 | 🟡 high — specialist register | concept, concepts |
| 499 | **filled** | 22 | 3,179.82 | 8.340372 | 🟡 high — specialist register | - |
| 500 | **determination** | 27 | 3,176.97 | 6.789775 | 🟡 high — specialist register | - |
| 501 | **accumulated** | 26 | 3,166.73 | 7.028186 | 🟡 high — specialist register | - |
| 502 | **kaya** | 19 | 3,158.70 | 9.593135 | 🟡 high — specialist register | kaya, kayas |
| 503 | **pot** | 19 | 3,158.70 | 9.593135 | 🟡 high — specialist register | pot, pots |
| 504 | **received** | 39 | 3,158.41 | 4.673154 | 🟡 high — specialist register | - |
| 505 | **later** | 40 | 3,158.31 | 4.556183 | 🟡 high — specialist register | - |
| 506 | **dorje** | 19 | 3,157.67 | 9.59 | 🟡 high — specialist register | - |
| 507 | **jowo** | 19 | 3,157.67 | 9.59 | 🟡 high — specialist register | - |
| 508 | **bless** | 19 | 3,157.67 | 9.59 | 🟡 high — specialist register | - |
| 509 | **pray** | 19 | 3,157.67 | 9.59 | 🟡 high — specialist register | - |
| 510 | **purification** | 19 | 3,157.67 | 9.59 | 🟡 high — specialist register | purification, purifications |
| 511 | **ly** | 19 | 3,157.67 | 9.59 | 🟡 high — specialist register | - |
| 512 | **antidote** | 19 | 3,157.67 | 9.59 | 🟡 high — specialist register | antidote, antidotes |
| 513 | **dharmodgata** | 19 | 3,157.67 | 9.59 | 🟡 high — specialist register | - |
| 514 | **poison** | 24 | 3,151.91 | 7.578232 | 🟡 high — specialist register | poison, poisons |
| 515 | **suddenly** | 23 | 3,109.52 | 7.801376 | 🟡 high — specialist register | - |
| 516 | **using** | 31 | 3,108.63 | 5.786473 | 🟡 high — specialist register | - |
| 517 | **respect** | 27 | 3,098.81 | 6.622721 | 🟡 high — specialist register | respect, respects |
| 518 | **offer** | 48 | 3,098.78 | 3.725252 | 🟡 high — specialist register | - |
| 519 | **please** | 21 | 3,091.38 | 8.494523 | 🟡 high — specialist register | - |
| 520 | **behind** | 30 | 3,082.75 | 5.929574 | 🟡 high — specialist register | - |
| 521 | **night** | 31 | 3,079.59 | 5.732405 | 🟡 high — specialist register | night, nights |
| 522 | **rest** | 32 | 3,077.82 | 5.550084 | 🟡 high — specialist register | rest, rests |
| 523 | **realize** | 24 | 3,076.08 | 7.395911 | 🟡 high — specialist register | - |
| 524 | **care** | 28 | 3,073.98 | 6.335039 | 🟡 high — specialist register | care, cares |
| 525 | **year** | 82 | 3,066.19 | 2.157697 | 🟡 high — specialist register | year, years |
| 526 | **already** | 41 | 3,055.13 | 4.29983 | 🟡 high — specialist register | - |
| 527 | **lotus** | 19 | 3,025.19 | 9.18767 | 🟡 high — specialist register | - |
| 528 | **sick** | 19 | 3,025.19 | 9.18767 | 🟡 high — specialist register | - |
| 529 | **full** | 42 | 3,024.27 | 4.155056 | 🟡 high — specialist register | - |
| 530 | **told** | 54 | 3,008.36 | 3.214709 | 🟡 high — specialist register | - |
| 531 | **ray** | 22 | 3,007.50 | 7.888387 | 🟡 high — specialist register | ray, rays |
| 532 | **speak** | 20 | 3,007.36 | 8.676844 | 🟡 high — specialist register | speak, speaks |
| 533 | **middle** | 29 | 3,006.45 | 5.982217 | 🟡 high — specialist register | - |
| 534 | **lack** | 28 | 3,004.55 | 6.191938 | 🟡 high — specialist register | lack, lacks |
| 535 | **blind** | 18 | 2,992.45 | 9.593135 | 🟢 medium — moderately distinctive | - |
| 536 | **purified** | 18 | 2,992.45 | 9.593135 | 🟢 medium — moderately distinctive | - |
| 537 | **renounce** | 18 | 2,992.45 | 9.593135 | 🟢 medium — moderately distinctive | - |
| 538 | **hair** | 18 | 2,992.45 | 9.593135 | 🟢 medium — moderately distinctive | - |
| 539 | **lying** | 18 | 2,992.45 | 9.593135 | 🟢 medium — moderately distinctive | - |
| 540 | **nagarjuna** | 18 | 2,991.47 | 9.59 | 🟢 medium — moderately distinctive | - |
| 541 | **wherever** | 18 | 2,991.47 | 9.59 | 🟢 medium — moderately distinctive | - |
| 542 | **indra** | 18 | 2,991.47 | 9.59 | 🟢 medium — moderately distinctive | indra, indras |
| 543 | **sickness** | 18 | 2,991.47 | 9.59 | 🟢 medium — moderately distinctive | sickness, sicknesses |
| 544 | **pleasant** | 18 | 2,991.47 | 9.59 | 🟢 medium — moderately distinctive | - |
| 545 | **throne** | 18 | 2,991.47 | 9.59 | 🟢 medium — moderately distinctive | throne, thrones |
| 546 | **tonpa** | 18 | 2,991.47 | 9.59 | 🟢 medium — moderately distinctive | - |
| 547 | **unbearable** | 18 | 2,991.47 | 9.59 | 🟢 medium — moderately distinctive | - |
| 548 | **yogi** | 18 | 2,991.47 | 9.59 | 🟢 medium — moderately distinctive | yogi, yogis |
| 549 | **doubt** | 26 | 2,984.03 | 6.622721 | 🟢 medium — moderately distinctive | doubt, doubts |
| 550 | **soon** | 34 | 2,950.88 | 5.008168 | 🟢 medium — moderately distinctive | - |
| 551 | **fish** | 23 | 2,947.91 | 7.395911 | 🟢 medium — moderately distinctive | fish, fishes |
| 552 | **fly** | 21 | 2,943.82 | 8.089058 | 🟢 medium — moderately distinctive | flies, fly |
| 553 | **vision** | 21 | 2,943.82 | 8.089058 | 🟢 medium — moderately distinctive | vision, visions |
| 554 | **idea** | 26 | 2,929.68 | 6.502093 | 🟢 medium — moderately distinctive | idea, ideas |
| 555 | **explained** | 25 | 2,928.71 | 6.759922 | 🟢 medium — moderately distinctive | - |
| 556 | **consider** | 33 | 2,919.18 | 5.104499 | 🟢 medium — moderately distinctive | - |
| 557 | **young** | 22 | 2,915.55 | 7.647225 | 🟢 medium — moderately distinctive | - |
| 558 | **learn** | 21 | 2,905.48 | 7.983697 | 🟢 medium — moderately distinctive | learn, learns |
| 559 | **side** | 27 | 2,905.10 | 6.208745 | 🟢 medium — moderately distinctive | side, sides |
| 560 | **saying** | 35 | 2,887.65 | 4.760829 | 🟢 medium — moderately distinctive | saying, sayings |
| 561 | **try** | 30 | 2,885.46 | 5.550084 | 🟢 medium — moderately distinctive | - |
| 562 | **hold** | 34 | 2,877.49 | 4.883605 | 🟢 medium — moderately distinctive | hold, holds |
| 563 | **entire** | 28 | 2,877.24 | 5.929574 | 🟢 medium — moderately distinctive | - |
| 564 | **recognize** | 21 | 2,870.79 | 7.888387 | 🟢 medium — moderately distinctive | - |
| 565 | **seem** | 25 | 2,869.26 | 6.622721 | 🟢 medium — moderately distinctive | seem, seems |
| 566 | **clean** | 18 | 2,865.97 | 9.18767 | 🟢 medium — moderately distinctive | - |
| 567 | **no-one** | 19 | 2,856.99 | 8.676844 | 🟢 medium — moderately distinctive | - |
| 568 | **surrounded** | 19 | 2,856.99 | 8.676844 | 🟢 medium — moderately distinctive | - |
| 569 | **arrived** | 22 | 2,841.53 | 7.453069 | 🟢 medium — moderately distinctive | - |
| 570 | **cast** | 21 | 2,839.13 | 7.801376 | 🟢 medium — moderately distinctive | - |
| 571 | **reflection** | 21 | 2,839.13 | 7.801376 | 🟢 medium — moderately distinctive | reflection, reflections |
| 572 | **sit** | 21 | 2,839.13 | 7.801376 | 🟢 medium — moderately distinctive | sit, sits |
| 573 | **rain** | 25 | 2,826.96 | 6.525082 | 🟢 medium — moderately distinctive | rain, rains |
| 574 | **glorious** | 17 | 2,825.28 | 9.59 | 🟢 medium — moderately distinctive | - |
| 575 | **sangye** | 17 | 2,825.28 | 9.59 | 🟢 medium — moderately distinctive | - |
| 576 | **tear** | 17 | 2,825.28 | 9.59 | 🟢 medium — moderately distinctive | tear, tears |
| 577 | **tion** | 17 | 2,825.28 | 9.59 | 🟢 medium — moderately distinctive | tion, tions |
| 578 | **possess** | 17 | 2,825.28 | 9.59 | 🟢 medium — moderately distinctive | possess, possesses |
| 579 | **nanda** | 17 | 2,825.28 | 9.59 | 🟢 medium — moderately distinctive | - |
| 580 | **downfall** | 17 | 2,825.28 | 9.59 | 🟢 medium — moderately distinctive | downfall, downfalls |
| 581 | **mouth** | 21 | 2,810.00 | 7.721333 | 🟢 medium — moderately distinctive | mouth, mouths |
| 582 | **eating** | 19 | 2,796.96 | 8.494523 | 🟢 medium — moderately distinctive | - |
| 583 | **unless** | 30 | 2,774.95 | 5.337522 | 🟢 medium — moderately distinctive | - |
| 584 | **gave** | 32 | 2,771.67 | 4.998015 | 🟢 medium — moderately distinctive | - |
| 585 | **fear** | 25 | 2,770.37 | 6.394462 | 🟢 medium — moderately distinctive | fear, fears |
| 586 | **enjoy** | 19 | 2,746.21 | 8.340372 | 🟢 medium — moderately distinctive | enjoy, enjoys |
| 587 | **brought** | 28 | 2,742.33 | 5.651553 | 🟢 medium — moderately distinctive | - |
| 588 | **material** | 26 | 2,740.21 | 6.08159 | 🟢 medium — moderately distinctive | material, materials |
| 589 | **following** | 36 | 2,724.70 | 4.367389 | 🟢 medium — moderately distinctive | - |
| 590 | **actually** | 24 | 2,723.67 | 6.548613 | 🟢 medium — moderately distinctive | - |
| 591 | **next** | 40 | 2,712.44 | 3.912963 | 🟢 medium — moderately distinctive | - |
| 592 | **comfort** | 17 | 2,706.75 | 9.18767 | 🟢 medium — moderately distinctive | comfort, comforts |
| 593 | **bone** | 17 | 2,706.75 | 9.18767 | 🟢 medium — moderately distinctive | bone, bones |
| 594 | **iron** | 23 | 2,706.31 | 6.789775 | 🟢 medium — moderately distinctive | - |
| 595 | **straight** | 20 | 2,703.93 | 7.801376 | 🟢 medium — moderately distinctive | - |
| 596 | **ing** | 19 | 2,702.24 | 8.206841 | 🟢 medium — moderately distinctive | ing, ings |
| 597 | **clear** | 28 | 2,697.37 | 5.558895 | 🟢 medium — moderately distinctive | - |
| 598 | **experienced** | 21 | 2,691.57 | 7.395911 | 🟢 medium — moderately distinctive | - |
| 599 | **hardship** | 20 | 2,676.19 | 7.721333 | 🟢 medium — moderately distinctive | hardship, hardships |
| 600 | **intense** | 20 | 2,676.19 | 7.721333 | 🟢 medium — moderately distinctive | - |
| 601 | **reality** | 21 | 2,671.89 | 7.341843 | 🟢 medium — moderately distinctive | - |
| 602 | **brother** | 16 | 2,659.96 | 9.593135 | 🟢 medium — moderately distinctive | brother, brothers |
| 603 | **miraculous** | 16 | 2,659.96 | 9.593135 | 🟢 medium — moderately distinctive | - |
| 604 | **forever** | 16 | 2,659.96 | 9.593135 | 🟢 medium — moderately distinctive | - |
| 605 | **fortunate** | 16 | 2,659.09 | 9.59 | 🟢 medium — moderately distinctive | - |
| 606 | **omniscient** | 16 | 2,659.09 | 9.59 | 🟢 medium — moderately distinctive | - |
| 607 | **basi** | 16 | 2,659.09 | 9.59 | 🟢 medium — moderately distinctive | - |
| 608 | **padampa** | 16 | 2,659.09 | 9.59 | 🟢 medium — moderately distinctive | - |
| 609 | **thirst** | 16 | 2,659.09 | 9.59 | 🟢 medium — moderately distinctive | - |
| 610 | **sakyamuni** | 16 | 2,659.09 | 9.59 | 🟢 medium — moderately distinctive | - |
| 611 | **brahma** | 16 | 2,659.09 | 9.59 | 🟢 medium — moderately distinctive | - |
| 612 | **turtle** | 16 | 2,659.09 | 9.59 | 🟢 medium — moderately distinctive | turtle, turtles |
| 613 | **nowaday** | 16 | 2,659.09 | 9.59 | 🟢 medium — moderately distinctive | - |
| 614 | **seated** | 16 | 2,659.09 | 9.59 | 🟢 medium — moderately distinctive | - |
| 615 | **bliss** | 16 | 2,659.09 | 9.59 | 🟢 medium — moderately distinctive | - |
| 616 | **none** | 22 | 2,651.28 | 6.954078 | 🟢 medium — moderately distinctive | - |
| 617 | **perceive** | 18 | 2,649.75 | 8.494523 | 🟢 medium — moderately distinctive | perceive, perceives |
| 618 | **reason** | 28 | 2,644.53 | 5.45 | 🟢 medium — moderately distinctive | reason, reasons |
| 619 | **itself** | 27 | 2,639.87 | 5.641891 | 🟢 medium — moderately distinctive | - |
| 620 | **cut** | 38 | 2,634.32 | 4.000284 | 🟢 medium — moderately distinctive | cut, cuts |
| 621 | **fortune** | 19 | 2,628.76 | 7.983697 | 🟢 medium — moderately distinctive | fortune, fortunes |
| 622 | **far** | 33 | 2,624.48 | 4.589189 | 🟢 medium — moderately distinctive | - |
| 623 | **aspect** | 17 | 2,622.00 | 8.899988 | 🟢 medium — moderately distinctive | aspect, aspects |
| 624 | **hidden** | 17 | 2,622.00 | 8.899988 | 🟢 medium — moderately distinctive | - |
| 625 | **spend** | 23 | 2,619.79 | 6.57271 | 🟢 medium — moderately distinctive | - |
| 626 | **million** | 23 | 2,619.79 | 6.57271 | 🟢 medium — moderately distinctive | million, millions |
| 627 | **hot** | 20 | 2,604.22 | 7.513694 | 🟢 medium — moderately distinctive | - |
| 628 | **alive** | 18 | 2,601.67 | 8.340372 | 🟢 medium — moderately distinctive | - |
| 629 | **hunger** | 18 | 2,601.67 | 8.340372 | 🟢 medium — moderately distinctive | - |
| 630 | **seed** | 20 | 2,583.21 | 7.453069 | 🟢 medium — moderately distinctive | seed, seeds |
| 631 | **mount** | 19 | 2,568.73 | 7.801376 | 🟢 medium — moderately distinctive | - |
| 632 | **meat** | 23 | 2,565.35 | 6.436135 | 🟢 medium — moderately distinctive | meat, meats |
| 633 | **enter** | 24 | 2,561.69 | 6.159148 | 🟢 medium — moderately distinctive | enter, enters |
| 634 | **quite** | 23 | 2,556.96 | 6.415081 | 🟢 medium — moderately distinctive | - |
| 635 | **appearance** | 17 | 2,556.26 | 8.676844 | 🟢 medium — moderately distinctive | appearance, appearances |
| 636 | **main** | 31 | 2,555.50 | 4.756853 | 🟢 medium — moderately distinctive | - |
| 637 | **skin** | 16 | 2,547.53 | 9.18767 | 🟢 medium — moderately distinctive | skin, skins |
| 638 | **carefully** | 21 | 2,544.01 | 6.990446 | 🟢 medium — moderately distinctive | - |
| 639 | **properly** | 19 | 2,542.38 | 7.721333 | 🟢 medium — moderately distinctive | - |
| 640 | **similar** | 28 | 2,537.80 | 5.230037 | 🟢 medium — moderately distinctive | - |
| 641 | **rock** | 18 | 2,523.27 | 8.089058 | 🟢 medium — moderately distinctive | rock, rocks |
| 642 | **wind** | 19 | 2,495.26 | 7.578232 | 🟢 medium — moderately distinctive | wind, winds |
| 643 | **remembering** | 15 | 2,493.71 | 9.593135 | 🟢 medium — moderately distinctive | - |
| 644 | **pride** | 15 | 2,493.71 | 9.593135 | 🟢 medium — moderately distinctive | - |
| 645 | **cultivate** | 15 | 2,493.71 | 9.593135 | 🟢 medium — moderately distinctive | - |
| 646 | **utterly** | 15 | 2,493.71 | 9.593135 | 🟢 medium — moderately distinctive | - |
| 647 | **prostrate** | 15 | 2,492.89 | 9.59 | 🟢 medium — moderately distinctive | - |
| 648 | **amitabha** | 15 | 2,492.89 | 9.59 | 🟢 medium — moderately distinctive | - |
| 649 | **distraction** | 15 | 2,492.89 | 9.59 | 🟢 medium — moderately distinctive | distraction, distractions |
| 650 | **nirvana** | 15 | 2,492.89 | 9.59 | 🟢 medium — moderately distinctive | - |
| 651 | **countless** | 15 | 2,492.89 | 9.59 | 🟢 medium — moderately distinctive | - |
| 652 | **divine** | 15 | 2,492.89 | 9.59 | 🟢 medium — moderately distinctive | - |
| 653 | **liberate** | 15 | 2,492.89 | 9.59 | 🟢 medium — moderately distinctive | liberate, liberates |
| 654 | **milarepa** | 15 | 2,492.89 | 9.59 | 🟢 medium — moderately distinctive | - |
| 655 | **loved** | 15 | 2,492.89 | 9.59 | 🟢 medium — moderately distinctive | - |
| 656 | **frog** | 15 | 2,492.89 | 9.59 | 🟢 medium — moderately distinctive | frog, frogs |
| 657 | **goddess** | 15 | 2,492.89 | 9.59 | 🟢 medium — moderately distinctive | goddess, goddesses |
| 658 | **oneself** | 15 | 2,492.89 | 9.59 | 🟢 medium — moderately distinctive | - |
| 659 | **boundless** | 15 | 2,492.89 | 9.59 | 🟢 medium — moderately distinctive | - |
| 660 | **hunter** | 16 | 2,467.76 | 8.899988 | 🟢 medium — moderately distinctive | hunter, hunters |
| 661 | **leg** | 16 | 2,467.76 | 8.899988 | 🟢 medium — moderately distinctive | - |
| 662 | **self** | 16 | 2,467.76 | 8.899988 | 🟢 medium — moderately distinctive | - |
| 663 | **metal** | 24 | 2,466.20 | 5.929574 | 🟢 medium — moderately distinctive | metal, metals |
| 664 | **number** | 31 | 2,465.42 | 4.589189 | 🟢 medium — moderately distinctive | number, numbers |
| 665 | **bound** | 19 | 2,454.05 | 7.453069 | 🟢 medium — moderately distinctive | bound, bounds |
| 666 | **enough** | 27 | 2,453.16 | 5.242857 | 🟢 medium — moderately distinctive | - |
| 667 | **least** | 30 | 2,443.00 | 4.699034 | 🟢 medium — moderately distinctive | - |
| 668 | **hope** | 25 | 2,436.07 | 5.622843 | 🟢 medium — moderately distinctive | hope, hopes |
| 669 | **centre** | 20 | 2,435.94 | 7.028186 | 🟢 medium — moderately distinctive | - |
| 670 | **otherwise** | 21 | 2,429.34 | 6.675364 | 🟢 medium — moderately distinctive | - |
| 671 | **lake** | 21 | 2,419.64 | 6.648696 | 🟢 medium — moderately distinctive | lake, lakes |
| 672 | **twelve** | 17 | 2,417.79 | 8.206841 | 🟢 medium — moderately distinctive | - |
| 673 | **inside** | 19 | 2,417.42 | 7.341843 | 🟢 medium — moderately distinctive | - |
| 674 | **extremely** | 22 | 2,415.27 | 6.335039 | 🟢 medium — moderately distinctive | - |
| 675 | **reach** | 26 | 2,411.39 | 5.351808 | 🟢 medium — moderately distinctive | reach, reaches |
| 676 | **entirely** | 20 | 2,410.26 | 6.954078 | 🟢 medium — moderately distinctive | - |
| 677 | **undergo** | 16 | 2,405.89 | 8.676844 | 🟢 medium — moderately distinctive | - |
| 678 | **certain** | 30 | 2,403.64 | 4.623322 | 🟢 medium — moderately distinctive | - |
| 679 | **bed** | 15 | 2,388.31 | 9.18767 | 🟢 medium — moderately distinctive | bed, beds |
| 680 | **thirty-three** | 15 | 2,388.31 | 9.18767 | 🟢 medium — moderately distinctive | - |
| 681 | **subject** | 31 | 2,380.55 | 4.43121 | 🟢 medium — moderately distinctive | subject, subjects |
| 682 | **excellent** | 20 | 2,374.98 | 6.852295 | 🟢 medium — moderately distinctive | - |
| 683 | **top** | 25 | 2,368.12 | 5.466001 | 🟢 medium — moderately distinctive | top, tops |
| 684 | **belief** | 20 | 2,363.98 | 6.820546 | 🟢 medium — moderately distinctive | belief, beliefs |
| 685 | **opportunity** | 22 | 2,360.71 | 6.191938 | 🟢 medium — moderately distinctive | opportunities, opportunity |
| 686 | **accomplished** | 16 | 2,355.34 | 8.494523 | 🟢 medium — moderately distinctive | - |
| 687 | **heard** | 19 | 2,354.52 | 7.150788 | 🟢 medium — moderately distinctive | - |
| 688 | **preliminary** | 24 | 2,346.55 | 5.641891 | 🟢 medium — moderately distinctive | preliminaries, preliminary |
| 689 | **remain** | 29 | 2,341.28 | 4.658661 | 🟢 medium — moderately distinctive | remain, remains |
| 690 | **sixteen** | 14 | 2,327.46 | 9.593135 | 🟢 medium — moderately distinctive | - |
| 691 | **sexual** | 14 | 2,327.46 | 9.593135 | 🟢 medium — moderately distinctive | - |
| 692 | **crown** | 19 | 2,327.06 | 7.067407 | 🟢 medium — moderately distinctive | crown, crowns |
| 693 | **stop** | 24 | 2,327.02 | 5.594934 | 🟢 medium — moderately distinctive | stop, stops |
| 694 | **venerable** | 14 | 2,326.70 | 9.59 | 🟢 medium — moderately distinctive | venerable, venerables |
| 695 | **expanse** | 14 | 2,326.70 | 9.59 | 🟢 medium — moderately distinctive | - |
| 696 | **well-being** | 14 | 2,326.70 | 9.59 | 🟢 medium — moderately distinctive | - |
| 697 | **yak** | 14 | 2,326.70 | 9.59 | 🟢 medium — moderately distinctive | yak, yaks |
| 698 | **elephant** | 14 | 2,326.70 | 9.59 | 🟢 medium — moderately distinctive | elephant, elephants |
| 699 | **darkness** | 14 | 2,326.70 | 9.59 | 🟢 medium — moderately distinctive | - |
| 700 | **temple** | 14 | 2,326.70 | 9.59 | 🟢 medium — moderately distinctive | temple, temples |
| 701 | **vajrayana** | 14 | 2,326.70 | 9.59 | 🟢 medium — moderately distinctive | - |
| 702 | **pratyekabuddha** | 14 | 2,326.70 | 9.59 | 🟢 medium — moderately distinctive | pratyekabuddha, pratyekabuddhas |
| 703 | **mentally** | 14 | 2,326.70 | 9.59 | 🟢 medium — moderately distinctive | - |
| 704 | **liberated** | 14 | 2,326.70 | 9.59 | 🟢 medium — moderately distinctive | - |
| 705 | **treasure** | 14 | 2,326.70 | 9.59 | 🟢 medium — moderately distinctive | treasure, treasures |
| 706 | **sacred** | 14 | 2,326.70 | 9.59 | 🟢 medium — moderately distinctive | - |
| 707 | **wrathful** | 14 | 2,326.70 | 9.59 | 🟢 medium — moderately distinctive | - |
| 708 | **support** | 29 | 2,314.87 | 4.60611 | 🟢 medium — moderately distinctive | - |
| 709 | **relative** | 20 | 2,313.66 | 6.675364 | 🟢 medium — moderately distinctive | relative, relatives |
| 710 | **cloud** | 15 | 2,313.53 | 8.899988 | 🟢 medium — moderately distinctive | cloud, clouds |
| 711 | **honour** | 16 | 2,312.59 | 8.340372 | 🟢 medium — moderately distinctive | honour, honours |
| 712 | **fail** | 19 | 2,289.75 | 6.954078 | 🟢 medium — moderately distinctive | fail, fails |
| 713 | **claim** | 19 | 2,289.75 | 6.954078 | 🟢 medium — moderately distinctive | claim, claims |
| 714 | **discipline** | 17 | 2,274.76 | 7.721333 | 🟢 medium — moderately distinctive | - |
| 715 | **trying** | 23 | 2,268.42 | 5.691163 | 🟢 medium — moderately distinctive | - |
| 716 | **particularly** | 24 | 2,263.45 | 5.442095 | 🟢 medium — moderately distinctive | - |
| 717 | **protect** | 22 | 2,260.69 | 5.929574 | 🟢 medium — moderately distinctive | protect, protects |
| 718 | **arm** | 19 | 2,256.23 | 6.852295 | 🟢 medium — moderately distinctive | arm, arms |
| 719 | **listening** | 15 | 2,255.52 | 8.676844 | 🟢 medium — moderately distinctive | - |
| 720 | **horse** | 15 | 2,255.52 | 8.676844 | 🟢 medium — moderately distinctive | - |
| 721 | **name** | 28 | 2,250.18 | 4.637308 | 🟢 medium — moderately distinctive | name, names |
| 722 | **force** | 25 | 2,249.64 | 5.192532 | 🟢 medium — moderately distinctive | force, forces |
| 723 | **central** | 32 | 2,237.28 | 4.034378 | 🟢 medium — moderately distinctive | - |
| 724 | **fall** | 32 | 2,233.02 | 4.026701 | 🟢 medium — moderately distinctive | fall, falls |
| 725 | **arrow** | 14 | 2,229.09 | 9.18767 | 🟢 medium — moderately distinctive | arrow, arrows |
| 726 | **wild** | 14 | 2,229.09 | 9.18767 | 🟢 medium — moderately distinctive | - |
| 727 | **eighty** | 14 | 2,229.09 | 9.18767 | 🟢 medium — moderately distinctive | - |
| 728 | **hat** | 14 | 2,229.09 | 9.18767 | 🟢 medium — moderately distinctive | hat, hats |
| 729 | **slaughtered** | 14 | 2,229.09 | 9.18767 | 🟢 medium — moderately distinctive | - |
| 730 | **likewise** | 14 | 2,229.09 | 9.18767 | 🟢 medium — moderately distinctive | - |
| 731 | **worse** | 18 | 2,217.32 | 7.108229 | 🟢 medium — moderately distinctive | - |
| 732 | **easy** | 17 | 2,213.59 | 7.513694 | 🟢 medium — moderately distinctive | - |
| 733 | **stream** | 17 | 2,213.59 | 7.513694 | 🟢 medium — moderately distinctive | stream, streams |
| 734 | **open** | 28 | 2,199.91 | 4.53371 | 🟢 medium — moderately distinctive | open, opens |
| 735 | **turned** | 19 | 2,197.97 | 6.675364 | 🟢 medium — moderately distinctive | - |
| 736 | **transmission** | 17 | 2,195.73 | 7.453069 | 🟢 medium — moderately distinctive | transmission, transmissions |
| 737 | **clearly** | 20 | 2,189.10 | 6.31599 | 🟢 medium — moderately distinctive | - |
| 738 | **unable** | 20 | 2,189.10 | 6.31599 | 🟢 medium — moderately distinctive | - |
| 739 | **serve** | 19 | 2,180.64 | 6.622721 | 🟢 medium — moderately distinctive | serve, serves |
| 740 | **branch** | 19 | 2,172.30 | 6.597403 | 🟢 medium — moderately distinctive | branch, branches |
| 741 | **getting** | 20 | 2,170.02 | 6.260931 | 🟢 medium — moderately distinctive | - |
| 742 | **ill** | 18 | 2,169.23 | 6.954078 | 🟢 medium — moderately distinctive | ill, ills |
| 743 | **merchant** | 19 | 2,164.17 | 6.57271 | 🟢 medium — moderately distinctive | merchant, merchants |
| 744 | **accumulating** | 16 | 2,163.14 | 7.801376 | 🟢 medium — moderately distinctive | - |
| 745 | **anger** | 17 | 2,162.96 | 7.341843 | 🟢 medium — moderately distinctive | - |
| 746 | **bowl** | 13 | 2,161.22 | 9.593135 | 🟢 medium — moderately distinctive | bowl, bowls |
| 747 | **crowd** | 13 | 2,161.22 | 9.593135 | 🟢 medium — moderately distinctive | - |
| 748 | **endless** | 13 | 2,161.22 | 9.593135 | 🟢 medium — moderately distinctive | - |
| 749 | **wonderful** | 13 | 2,161.22 | 9.593135 | 🟢 medium — moderately distinctive | - |
| 750 | **selfish** | 13 | 2,161.22 | 9.593135 | 🟢 medium — moderately distinctive | - |
| 751 | **sambhogakaya** | 13 | 2,160.51 | 9.59 | 🟢 medium — moderately distinctive | - |
| 752 | **jigme** | 13 | 2,160.51 | 9.59 | 🟢 medium — moderately distinctive | - |
| 753 | **tormented** | 13 | 2,160.51 | 9.59 | 🟢 medium — moderately distinctive | - |
| 754 | **dagpo** | 13 | 2,160.51 | 9.59 | 🟢 medium — moderately distinctive | - |
| 755 | **sorrow** | 13 | 2,160.51 | 9.59 | 🟢 medium — moderately distinctive | sorrow, sorrows |
| 756 | **beast** | 13 | 2,160.51 | 9.59 | 🟢 medium — moderately distinctive | beast, beasts |
| 757 | **translator** | 13 | 2,160.51 | 9.59 | 🟢 medium — moderately distinctive | translator, translators |
| 758 | **statue** | 13 | 2,160.51 | 9.59 | 🟢 medium — moderately distinctive | statue, statues |
| 759 | **ephemeral** | 13 | 2,160.51 | 9.59 | 🟢 medium — moderately distinctive | - |
| 760 | **lamp** | 13 | 2,160.51 | 9.59 | 🟢 medium — moderately distinctive | lamp, lamps |
| 761 | **robe** | 13 | 2,160.51 | 9.59 | 🟢 medium — moderately distinctive | robe, robes |
| 762 | **yoke** | 13 | 2,160.51 | 9.59 | 🟢 medium — moderately distinctive | - |
| 763 | **tantric** | 13 | 2,160.51 | 9.59 | 🟢 medium — moderately distinctive | - |
| 764 | **follower** | 13 | 2,160.51 | 9.59 | 🟢 medium — moderately distinctive | follower, followers |
| 765 | **precept** | 13 | 2,160.51 | 9.59 | 🟢 medium — moderately distinctive | - |
| 766 | **tathagata** | 13 | 2,160.51 | 9.59 | 🟢 medium — moderately distinctive | tathagata, tathagatas |
| 767 | **skull** | 13 | 2,160.51 | 9.59 | 🟢 medium — moderately distinctive | skull, skulls |
| 768 | **primal** | 13 | 2,160.51 | 9.59 | 🟢 medium — moderately distinctive | - |
| 769 | **wife** | 14 | 2,159.29 | 8.899988 | 🟢 medium — moderately distinctive | - |
| 770 | **short** | 25 | 2,148.21 | 4.958406 | 🟢 medium — moderately distinctive | - |
| 771 | **regret** | 16 | 2,140.95 | 7.721333 | 🟢 medium — moderately distinctive | - |
| 772 | **looking** | 22 | 2,136.62 | 5.604151 | 🟢 medium — moderately distinctive | - |
| 773 | **used** | 27 | 2,136.44 | 4.565971 | 🟢 medium — moderately distinctive | - |
| 774 | **according** | 27 | 2,119.86 | 4.53054 | 🟢 medium — moderately distinctive | - |
| 775 | **create** | 20 | 2,113.07 | 6.096628 | 🟢 medium — moderately distinctive | create, creates |
| 776 | **grain** | 26 | 2,108.91 | 4.68048 | 🟢 medium — moderately distinctive | grain, grains |
| 777 | **dark** | 14 | 2,105.15 | 8.676844 | 🟢 medium — moderately distinctive | - |
| 778 | **exhausted** | 14 | 2,105.15 | 8.676844 | 🟢 medium — moderately distinctive | - |
| 779 | **substance** | 14 | 2,105.15 | 8.676844 | 🟢 medium — moderately distinctive | substance, substances |
| 780 | **ben** | 15 | 2,102.73 | 8.089058 | 🟢 medium — moderately distinctive | - |
| 781 | **high** | 29 | 2,101.47 | 4.181489 | 🟢 medium — moderately distinctive | - |
| 782 | **big** | 21 | 2,086.17 | 5.732405 | 🟢 medium — moderately distinctive | - |
| 783 | **one** | 43 | 2,082.10 | 2.794079 | 🟢 medium — moderately distinctive | - |
| 784 | **receive** | 24 | 2,080.86 | 5.003079 | 🟢 medium — moderately distinctive | receive, receives |
| 785 | **knowledge** | 15 | 2,075.34 | 7.983697 | 🟢 medium — moderately distinctive | - |
| 786 | **transform** | 13 | 2,069.87 | 9.18767 | 🟢 medium — moderately distinctive | transform, transforms |
| 787 | **heat** | 16 | 2,066.57 | 7.453069 | 🟢 medium — moderately distinctive | heat, heats |
| 788 | **case** | 22 | 2,065.93 | 5.418748 | 🟢 medium — moderately distinctive | - |
| 789 | **presence** | 18 | 2,065.87 | 6.622721 | 🟢 medium — moderately distinctive | - |
| 790 | **illness** | 14 | 2,060.92 | 8.494523 | 🟢 medium — moderately distinctive | illness, illnesses |
| 791 | **escape** | 14 | 2,060.92 | 8.494523 | 🟢 medium — moderately distinctive | escape, escapes |
| 792 | **sowing** | 14 | 2,060.92 | 8.494523 | 🟢 medium — moderately distinctive | - |
| 793 | **difficulty** | 17 | 2,059.43 | 6.990446 | 🟢 medium — moderately distinctive | difficulties, difficulty |
| 794 | **image** | 15 | 2,050.57 | 7.888387 | 🟢 medium — moderately distinctive | image, images |
| 795 | **kingdom** | 17 | 2,048.72 | 6.954078 | 🟢 medium — moderately distinctive | kingdom, kingdoms |
| 796 | **energy** | 26 | 2,041.35 | 4.53054 | 🟢 medium — moderately distinctive | energies, energy |
| 797 | **coming** | 21 | 2,026.26 | 5.567784 | 🟢 medium — moderately distinctive | - |
| 798 | **gather** | 14 | 2,023.52 | 8.340372 | 🟢 medium — moderately distinctive | gather, gathers |
| 799 | **chance** | 20 | 2,021.33 | 5.831935 | 🟢 medium — moderately distinctive | chance, chances |
| 800 | **reflect** | 23 | 2,019.21 | 5.065927 | 🟢 medium — moderately distinctive | - |
| 801 | **higher** | 30 | 2,018.60 | 3.882708 | 🟢 medium — moderately distinctive | - |
| 802 | **fully** | 21 | 2,007.27 | 5.515598 | 🟢 medium — moderately distinctive | - |
| 803 | **weapon** | 13 | 2,005.06 | 8.899988 | 🟢 medium — moderately distinctive | weapon, weapons |
| 804 | **awareness** | 13 | 2,005.06 | 8.899988 | 🟢 medium — moderately distinctive | - |
| 805 | **tooth** | 13 | 2,005.06 | 8.899988 | 🟢 medium — moderately distinctive | teeth, tooth |
| 806 | **blazing** | 12 | 1,994.97 | 9.593135 | 🟢 medium — moderately distinctive | - |
| 807 | **virtue** | 12 | 1,994.97 | 9.593135 | 🟢 medium — moderately distinctive | virtue, virtues |
| 808 | **meru** | 12 | 1,994.97 | 9.593135 | 🟢 medium — moderately distinctive | - |
| 809 | **devote** | 12 | 1,994.97 | 9.593135 | 🟢 medium — moderately distinctive | - |
| 810 | **sincere** | 12 | 1,994.97 | 9.593135 | 🟢 medium — moderately distinctive | - |
| 811 | **nirmanakaya** | 12 | 1,994.32 | 9.59 | 🟢 medium — moderately distinctive | - |
| 812 | **aspiration** | 12 | 1,994.32 | 9.59 | 🟢 medium — moderately distinctive | aspiration, aspirations |
| 813 | **compassionate** | 12 | 1,994.32 | 9.59 | 🟢 medium — moderately distinctive | - |
| 814 | **twenty-one** | 12 | 1,994.32 | 9.59 | 🟢 medium — moderately distinctive | - |
| 815 | **rejoice** | 12 | 1,994.32 | 9.59 | 🟢 medium — moderately distinctive | - |
| 816 | **useless** | 12 | 1,994.32 | 9.59 | 🟢 medium — moderately distinctive | - |
| 817 | **breath** | 12 | 1,994.32 | 9.59 | 🟢 medium — moderately distinctive | - |
| 818 | **sravaka** | 12 | 1,994.32 | 9.59 | 🟢 medium — moderately distinctive | sravaka, sravakas |
| 819 | **attendant** | 12 | 1,994.32 | 9.59 | 🟢 medium — moderately distinctive | attendant, attendants |
| 820 | **patron** | 12 | 1,994.32 | 9.59 | 🟢 medium — moderately distinctive | patron, patrons |
| 821 | **abbot** | 12 | 1,994.32 | 9.59 | 🟢 medium — moderately distinctive | - |
| 822 | **wish-granting** | 12 | 1,994.32 | 9.59 | 🟢 medium — moderately distinctive | - |
| 823 | **purifying** | 12 | 1,994.32 | 9.59 | 🟢 medium — moderately distinctive | - |
| 824 | **skilfully** | 12 | 1,994.32 | 9.59 | 🟢 medium — moderately distinctive | - |
| 825 | **apply** | 18 | 1,988.37 | 6.374259 | 🟢 medium — moderately distinctive | applies, apply |
| 826 | **home** | 22 | 1,972.73 | 5.174295 | 🟢 medium — moderately distinctive | home, homes |
| 827 | **lay** | 16 | 1,970.95 | 7.108229 | 🟢 medium — moderately distinctive | lay, lays |
| 828 | **immediately** | 22 | 1,963.65 | 5.150484 | 🟢 medium — moderately distinctive | - |
| 829 | **obtain** | 18 | 1,958.64 | 6.278949 | 🟢 medium — moderately distinctive | - |
| 830 | **destroy** | 13 | 1,954.79 | 8.676844 | 🟢 medium — moderately distinctive | destroy, destroys |
| 831 | **sake** | 13 | 1,954.79 | 8.676844 | 🟢 medium — moderately distinctive | - |
| 832 | **walk** | 13 | 1,954.79 | 8.676844 | 🟢 medium — moderately distinctive | walk, walks |
| 833 | **representation** | 15 | 1,953.16 | 7.513694 | 🟢 medium — moderately distinctive | representation, representations |
| 834 | **indeed** | 15 | 1,953.16 | 7.513694 | 🟢 medium — moderately distinctive | - |
| 835 | **approach** | 18 | 1,953.01 | 6.260931 | 🟢 medium — moderately distinctive | approach, approaches |
| 836 | **pass** | 16 | 1,948.76 | 7.028186 | 🟢 medium — moderately distinctive | pass, passes |
| 837 | **order** | 22 | 1,946.12 | 5.104499 | 🟢 medium — moderately distinctive | order, orders |
| 838 | **instance** | 14 | 1,936.98 | 7.983697 | 🟢 medium — moderately distinctive | instance, instances |
| 839 | **blue** | 14 | 1,936.98 | 7.983697 | 🟢 medium — moderately distinctive | - |
| 840 | **forest** | 15 | 1,922.55 | 7.395911 | 🟢 medium — moderately distinctive | forest, forests |
| 841 | **under** | 33 | 1,915.78 | 3.34994 | 🟢 medium — moderately distinctive | - |
| 842 | **offered** | 23 | 1,913.80 | 4.801485 | 🟢 medium — moderately distinctive | - |
| 843 | **beat** | 13 | 1,913.71 | 8.494523 | 🟢 medium — moderately distinctive | beat, beats |
| 844 | **harsh** | 13 | 1,913.71 | 8.494523 | 🟢 medium — moderately distinctive | - |
| 845 | **angry** | 13 | 1,913.71 | 8.494523 | 🟢 medium — moderately distinctive | - |
| 846 | **wear** | 13 | 1,913.71 | 8.494523 | 🟢 medium — moderately distinctive | wear, wears |
| 847 | **motivation** | 12 | 1,910.65 | 9.18767 | 🟢 medium — moderately distinctive | - |
| 848 | **tongue** | 12 | 1,910.65 | 9.18767 | 🟢 medium — moderately distinctive | tongue, tongues |
| 849 | **discord** | 12 | 1,910.65 | 9.18767 | 🟢 medium — moderately distinctive | - |
| 850 | **tea** | 16 | 1,909.08 | 6.885085 | 🟢 medium — moderately distinctive | - |
| 851 | **committed** | 18 | 1,897.07 | 6.08159 | 🟢 medium — moderately distinctive | - |
| 852 | **believe** | 21 | 1,896.46 | 5.211109 | 🟢 medium — moderately distinctive | - |
| 853 | **caught** | 14 | 1,892.75 | 7.801376 | 🟢 medium — moderately distinctive | - |
| 854 | **poor** | 18 | 1,892.45 | 6.066775 | 🟢 medium — moderately distinctive | - |
| 855 | **accomplish** | 13 | 1,878.98 | 8.340372 | 🟢 medium — moderately distinctive | accomplish, accomplishes |
| 856 | **knew** | 13 | 1,878.98 | 8.340372 | 🟢 medium — moderately distinctive | - |
| 857 | **met** | 20 | 1,878.12 | 5.418748 | 🟢 medium — moderately distinctive | - |
| 858 | **field** | 19 | 1,873.91 | 5.691163 | 🟢 medium — moderately distinctive | field, fields |
| 859 | **sole** | 14 | 1,873.33 | 7.721333 | 🟢 medium — moderately distinctive | sole, soles |
| 860 | **base** | 22 | 1,870.59 | 4.906385 | 🟢 medium — moderately distinctive | - |
| 861 | **extraordinary** | 23 | 1,862.65 | 4.673154 | 🟢 medium — moderately distinctive | - |
| 862 | **grow** | 19 | 1,860.87 | 5.651553 | 🟢 medium — moderately distinctive | grow, grows |
| 863 | **condition** | 18 | 1,857.75 | 5.955549 | 🟢 medium — moderately distinctive | condition, conditions |
| 864 | **include** | 25 | 1,855.33 | 4.282395 | 🟢 medium — moderately distinctive | include, includes |
| 865 | **leaving** | 17 | 1,855.23 | 6.297298 | 🟢 medium — moderately distinctive | - |
| 866 | **huge** | 18 | 1,853.68 | 5.942477 | 🟢 medium — moderately distinctive | - |
| 867 | **seen** | 23 | 1,852.60 | 4.647928 | 🟢 medium — moderately distinctive | - |
| 868 | **sense** | 16 | 1,850.93 | 6.675364 | 🟢 medium — moderately distinctive | - |
| 869 | **village** | 12 | 1,850.82 | 8.899988 | 🟢 medium — moderately distinctive | village, villages |
| 870 | **reign** | 12 | 1,850.82 | 8.899988 | 🟢 medium — moderately distinctive | - |
| 871 | **wishing** | 12 | 1,850.82 | 8.899988 | 🟢 medium — moderately distinctive | - |
| 872 | **detail** | 15 | 1,847.77 | 7.108229 | 🟢 medium — moderately distinctive | detail, details |
| 873 | **started** | 20 | 1,845.08 | 5.323438 | 🟢 medium — moderately distinctive | - |
| 874 | **conduct** | 15 | 1,837.15 | 7.067407 | 🟢 medium — moderately distinctive | - |
| 875 | **happened** | 15 | 1,837.15 | 7.067407 | 🟢 medium — moderately distinctive | - |
| 876 | **holding** | 22 | 1,835.37 | 4.814012 | 🟢 medium — moderately distinctive | - |
| 877 | **manifest** | 11 | 1,828.72 | 9.593135 | 🟢 medium — moderately distinctive | manifest, manifests |
| 878 | **terrible** | 11 | 1,828.72 | 9.593135 | 🟢 medium — moderately distinctive | - |
| 879 | **attaining** | 11 | 1,828.72 | 9.593135 | 🟢 medium — moderately distinctive | - |
| 880 | **shoulder** | 11 | 1,828.72 | 9.593135 | 🟢 medium — moderately distinctive | shoulder, shoulders |
| 881 | **misconduct** | 11 | 1,828.72 | 9.593135 | 🟢 medium — moderately distinctive | - |
| 882 | **finger** | 11 | 1,828.72 | 9.593135 | 🟢 medium — moderately distinctive | finger, fingers |
| 883 | **crest** | 11 | 1,828.72 | 9.593135 | 🟢 medium — moderately distinctive | - |
| 884 | **vidyadhara** | 11 | 1,828.12 | 9.59 | 🟢 medium — moderately distinctive | vidyadhara, vidyadharas |
| 885 | **rigdzin** | 11 | 1,828.12 | 9.59 | 🟢 medium — moderately distinctive | - |
| 886 | **lingpa** | 11 | 1,828.12 | 9.59 | 🟢 medium — moderately distinctive | - |
| 887 | **impure** | 11 | 1,828.12 | 9.59 | 🟢 medium — moderately distinctive | - |
| 888 | **samantabhadra** | 11 | 1,828.12 | 9.59 | 🟢 medium — moderately distinctive | samantabhadra, samantabhadras |
| 889 | **yidam** | 11 | 1,828.12 | 9.59 | 🟢 medium — moderately distinctive | yidam, yidams |
| 890 | **physically** | 11 | 1,828.12 | 9.59 | 🟢 medium — moderately distinctive | - |
| 891 | **tsa-tsa** | 11 | 1,828.12 | 9.59 | 🟢 medium — moderately distinctive | tsa-tsa, tsa-tsas |
| 892 | **pandita** | 11 | 1,828.12 | 9.59 | 🟢 medium — moderately distinctive | pandita, panditas |
| 893 | **spontaneously** | 11 | 1,828.12 | 9.59 | 🟢 medium — moderately distinctive | - |
| 894 | **limb** | 11 | 1,828.12 | 9.59 | 🟢 medium — moderately distinctive | limb, limbs |
| 895 | **misdeed** | 11 | 1,828.12 | 9.59 | 🟢 medium — moderately distinctive | misdeed, misdeeds |
| 896 | **torma** | 11 | 1,828.12 | 9.59 | 🟢 medium — moderately distinctive | torma, tormas |
| 897 | **knife** | 11 | 1,828.12 | 9.59 | 🟢 medium — moderately distinctive | - |
| 898 | **ignorance** | 11 | 1,828.12 | 9.59 | 🟢 medium — moderately distinctive | - |
| 899 | **chatter** | 11 | 1,828.12 | 9.59 | 🟢 medium — moderately distinctive | - |
| 900 | **obey** | 11 | 1,828.12 | 9.59 | 🟢 medium — moderately distinctive | obey, obeys |
| 901 | **mindfulness** | 11 | 1,828.12 | 9.59 | 🟢 medium — moderately distinctive | - |
| 902 | **manifestation** | 11 | 1,828.12 | 9.59 | 🟢 medium — moderately distinctive | manifestation, manifestations |
| 903 | **impartiality** | 11 | 1,828.12 | 9.59 | 🟢 medium — moderately distinctive | - |
| 904 | **lita** | 11 | 1,828.12 | 9.59 | 🟢 medium — moderately distinctive | lita, litas |
| 905 | **violation** | 14 | 1,822.95 | 7.513694 | 🟢 medium — moderately distinctive | violation, violations |
| 906 | **lose** | 16 | 1,815.78 | 6.548613 | 🟢 medium — moderately distinctive | - |
| 907 | **study** | 19 | 1,810.57 | 5.498791 | 🟢 medium — moderately distinctive | studies, study |
| 908 | **superior** | 14 | 1,808.24 | 7.453069 | 🟢 medium — moderately distinctive | superior, superiors |
| 909 | **importance** | 15 | 1,807.69 | 6.954078 | 🟢 medium — moderately distinctive | - |
| 910 | **physical** | 15 | 1,807.69 | 6.954078 | 🟢 medium — moderately distinctive | - |
| 911 | **female** | 12 | 1,804.42 | 8.676844 | 🟢 medium — moderately distinctive | female, females |
| 912 | **wonder** | 12 | 1,804.42 | 8.676844 | 🟢 medium — moderately distinctive | - |
| 913 | **ceremony** | 12 | 1,804.42 | 8.676844 | 🟢 medium — moderately distinctive | ceremonies, ceremony |
| 914 | **second** | 24 | 1,800.02 | 4.327858 | 🟢 medium — moderately distinctive | - |
| 915 | **mistake** | 13 | 1,798.63 | 7.983697 | 🟢 medium — moderately distinctive | mistake, mistakes |
| 916 | **consist** | 14 | 1,794.38 | 7.395911 | 🟢 medium — moderately distinctive | consist, consists |
| 917 | **putting** | 16 | 1,790.56 | 6.457641 | 🟢 medium — moderately distinctive | - |
| 918 | **equal** | 18 | 1,781.65 | 5.711571 | 🟢 medium — moderately distinctive | equal, equals |
| 919 | **symbol** | 13 | 1,777.16 | 7.888387 | 🟢 medium — moderately distinctive | symbol, symbols |
| 920 | **round** | 18 | 1,775.28 | 5.691163 | 🟢 medium — moderately distinctive | - |
| 921 | **road** | 14 | 1,768.82 | 7.29055 | 🟢 medium — moderately distinctive | road, roads |
| 922 | **smallest** | 12 | 1,766.50 | 8.494523 | 🟢 medium — moderately distinctive | - |
| 923 | **assembly** | 13 | 1,757.55 | 7.801376 | 🟢 medium — moderately distinctive | assemblies, assembly |
| 924 | **butter** | 13 | 1,757.55 | 7.801376 | 🟢 medium — moderately distinctive | - |
| 925 | **abandon** | 13 | 1,739.52 | 7.721333 | 🟢 medium — moderately distinctive | - |
| 926 | **false** | 13 | 1,739.52 | 7.721333 | 🟢 medium — moderately distinctive | - |
| 927 | **hearing** | 16 | 1,736.01 | 6.260931 | 🟢 medium — moderately distinctive | - |
| 928 | **league** | 12 | 1,734.45 | 8.340372 | 🟢 medium — moderately distinctive | league, leagues |
| 929 | **colour** | 12 | 1,734.45 | 8.340372 | 🟢 medium — moderately distinctive | colour, colours |
| 930 | **rely** | 13 | 1,722.83 | 7.647225 | 🟢 medium — moderately distinctive | relies, rely |
| 931 | **spread** | 15 | 1,714.98 | 6.597403 | 🟢 medium — moderately distinctive | spread, spreads |
| 932 | **warm** | 13 | 1,707.28 | 7.578232 | 🟢 medium — moderately distinctive | warm, warms |
| 933 | **confidence** | 16 | 1,703.35 | 6.143148 | 🟢 medium — moderately distinctive | - |
| 934 | **actual** | 16 | 1,698.99 | 6.127399 | 🟢 medium — moderately distinctive | - |
| 935 | **vigilance** | 11 | 1,696.59 | 8.899988 | 🟢 medium — moderately distinctive | - |
| 936 | **easily** | 14 | 1,696.00 | 6.990446 | 🟢 medium — moderately distinctive | - |
| 937 | **deep** | 14 | 1,696.00 | 6.990446 | 🟢 medium — moderately distinctive | - |
| 938 | **impossible** | 14 | 1,696.00 | 6.990446 | 🟢 medium — moderately distinctive | - |
| 939 | **across** | 15 | 1,690.20 | 6.502093 | 🟢 medium — moderately distinctive | - |
| 940 | **keeping** | 15 | 1,684.36 | 6.47962 | 🟢 medium — moderately distinctive | - |
| 941 | **gathered** | 12 | 1,682.18 | 8.089058 | 🟢 medium — moderately distinctive | - |
| 942 | **commit** | 12 | 1,682.18 | 8.089058 | 🟢 medium — moderately distinctive | - |
| 943 | **got** | 15 | 1,673.06 | 6.436135 | 🟢 medium — moderately distinctive | - |
| 944 | **spent** | 15 | 1,673.06 | 6.436135 | 🟢 medium — moderately distinctive | - |
| 945 | **protection** | 16 | 1,670.21 | 6.023602 | 🟢 medium — moderately distinctive | - |
| 946 | **explain** | 13 | 1,666.21 | 7.395911 | 🟢 medium — moderately distinctive | explain, explains |
| 947 | **chapter** | 14 | 1,662.49 | 6.852295 | 🟢 medium — moderately distinctive | - |
| 948 | **phase** | 14 | 1,662.49 | 6.852295 | 🟢 medium — moderately distinctive | - |
| 949 | **grass** | 10 | 1,662.47 | 9.593135 | 🟢 medium — moderately distinctive | - |
| 950 | **journey** | 10 | 1,662.47 | 9.593135 | 🟢 medium — moderately distinctive | journey, journeys |
| 951 | **pouring** | 10 | 1,662.47 | 9.593135 | 🟢 medium — moderately distinctive | - |
| 952 | **pith** | 10 | 1,661.93 | 9.59 | 🟢 medium — moderately distinctive | - |
| 953 | **dakini** | 10 | 1,661.93 | 9.59 | 🟢 medium — moderately distinctive | dakini, dakinis |
| 954 | **embodiment** | 10 | 1,661.93 | 9.59 | 🟢 medium — moderately distinctive | - |
| 955 | **jealousy** | 10 | 1,661.93 | 9.59 | 🟢 medium — moderately distinctive | - |
| 956 | **doctor** | 10 | 1,661.93 | 9.59 | 🟢 medium — moderately distinctive | doctor, doctors |
| 957 | **behave** | 10 | 1,661.93 | 9.59 | 🟢 medium — moderately distinctive | behave, behaves |
| 958 | **cave** | 10 | 1,661.93 | 9.59 | 🟢 medium — moderately distinctive | - |
| 959 | **princess** | 10 | 1,661.93 | 9.59 | 🟢 medium — moderately distinctive | princess, princesses |
| 960 | **monastic** | 10 | 1,661.93 | 9.59 | 🟢 medium — moderately distinctive | - |
| 961 | **lifespan** | 10 | 1,661.93 | 9.59 | 🟢 medium — moderately distinctive | - |
| 962 | **cried** | 10 | 1,661.93 | 9.59 | 🟢 medium — moderately distinctive | - |
| 963 | **traveller** | 10 | 1,661.93 | 9.59 | 🟢 medium — moderately distinctive | traveller, travellers |
| 964 | **condensed** | 10 | 1,661.93 | 9.59 | 🟢 medium — moderately distinctive | - |
| 965 | **burn** | 10 | 1,661.93 | 9.59 | 🟢 medium — moderately distinctive | burn, burns |
| 966 | **ornament** | 10 | 1,661.93 | 9.59 | 🟢 medium — moderately distinctive | ornament, ornaments |
| 967 | **clairvoyance** | 10 | 1,661.93 | 9.59 | 🟢 medium — moderately distinctive | - |
| 968 | **alm** | 10 | 1,661.93 | 9.59 | 🟢 medium — moderately distinctive | - |
| 969 | **humble** | 10 | 1,661.93 | 9.59 | 🟢 medium — moderately distinctive | - |
| 970 | **immeasurable** | 10 | 1,661.93 | 9.59 | 🟢 medium — moderately distinctive | - |
| 971 | **throat** | 10 | 1,661.93 | 9.59 | 🟢 medium — moderately distinctive | throat, throats |
| 972 | **hermitage** | 10 | 1,661.93 | 9.59 | 🟢 medium — moderately distinctive | hermitage, hermitages |
| 973 | **vase** | 10 | 1,661.93 | 9.59 | 🟢 medium — moderately distinctive | - |
| 974 | **ment** | 10 | 1,661.93 | 9.59 | 🟢 medium — moderately distinctive | ment, ments |
| 975 | **skull-cup** | 10 | 1,661.93 | 9.59 | 🟢 medium — moderately distinctive | - |
| 976 | **garab** | 10 | 1,661.93 | 9.59 | 🟢 medium — moderately distinctive | - |
| 977 | **call** | 18 | 1,658.40 | 5.316469 | 🟢 medium — moderately distinctive | call, calls |
| 978 | **understanding** | 14 | 1,654.78 | 6.820546 | 🟢 medium — moderately distinctive | - |
| 979 | **freed** | 11 | 1,654.05 | 8.676844 | 🟢 medium — moderately distinctive | - |
| 980 | **read** | 13 | 1,654.03 | 7.341843 | 🟢 medium — moderately distinctive | - |
| 981 | **followed** | 17 | 1,653.76 | 5.613454 | 🟢 medium — moderately distinctive | - |
| 982 | **strength** | 16 | 1,647.71 | 5.942477 | 🟢 medium — moderately distinctive | strength, strengths |
| 983 | **among** | 20 | 1,632.58 | 4.710333 | 🟢 medium — moderately distinctive | - |
| 984 | **examine** | 13 | 1,631.48 | 7.24176 | 🟢 medium — moderately distinctive | examine, examines |
| 985 | **section** | 14 | 1,626.21 | 6.702763 | 🟢 medium — moderately distinctive | section, sections |
| 986 | **run** | 16 | 1,623.59 | 5.855466 | 🟢 medium — moderately distinctive | run, runs |
| 987 | **tendency** | 12 | 1,622.36 | 7.801376 | 🟢 medium — moderately distinctive | tendencies, tendency |
| 988 | **rid** | 11 | 1,619.29 | 8.494523 | 🟢 medium — moderately distinctive | - |
| 989 | **baby** | 11 | 1,619.29 | 8.494523 | 🟢 medium — moderately distinctive | babies, baby |
| 990 | **shoot** | 11 | 1,619.29 | 8.494523 | 🟢 medium — moderately distinctive | shoot, shoots |
| 991 | **passed** | 15 | 1,618.39 | 6.225839 | 🟢 medium — moderately distinctive | - |
| 992 | **built** | 14 | 1,606.79 | 6.622721 | 🟢 medium — moderately distinctive | - |
| 993 | **foundation** | 13 | 1,601.40 | 7.108229 | 🟢 medium — moderately distinctive | foundation, foundations |
| 994 | **show** | 20 | 1,594.10 | 4.599307 | 🟢 medium — moderately distinctive | show, shows |
| 995 | **large** | 20 | 1,594.10 | 4.599307 | 🟢 medium — moderately distinctive | - |
| 996 | **indispensable** | 10 | 1,592.21 | 9.18767 | 🟢 medium — moderately distinctive | - |
| 997 | **eaten** | 10 | 1,592.21 | 9.18767 | 🟢 medium — moderately distinctive | - |
| 998 | **sincerely** | 10 | 1,592.21 | 9.18767 | 🟢 medium — moderately distinctive | - |
| 999 | **concern** | 18 | 1,590.53 | 5.098897 | 🟢 medium — moderately distinctive | concern, concerns |
| 1000 | **advice** | 12 | 1,590.30 | 7.647225 | 🟢 medium — moderately distinctive | - |
| 1001 | **moreover** | 12 | 1,590.30 | 7.647225 | 🟢 medium — moderately distinctive | - |
| 1002 | **examining** | 12 | 1,590.30 | 7.647225 | 🟢 medium — moderately distinctive | - |
| 1003 | **disappeared** | 11 | 1,589.91 | 8.340372 | 🟢 medium — moderately distinctive | - |
| 1004 | **knowing** | 11 | 1,589.91 | 8.340372 | 🟢 medium — moderately distinctive | - |
| 1005 | **shadow** | 11 | 1,589.91 | 8.340372 | 🟢 medium — moderately distinctive | shadow, shadows |
| 1006 | **purity** | 11 | 1,589.91 | 8.340372 | 🟢 medium — moderately distinctive | - |
| 1007 | **house** | 20 | 1,583.69 | 4.569255 | 🟢 medium — moderately distinctive | - |
| 1008 | **often** | 14 | 1,577.52 | 6.502093 | 🟢 medium — moderately distinctive | - |
| 1009 | **milk** | 12 | 1,575.95 | 7.578232 | 🟢 medium — moderately distinctive | - |
| 1010 | **individual** | 14 | 1,572.07 | 6.47962 | 🟢 medium — moderately distinctive | individual, individuals |
| 1011 | **few** | 18 | 1,570.29 | 5.034009 | 🟢 medium — moderately distinctive | - |
| 1012 | **disappear** | 11 | 1,564.45 | 8.206841 | 🟢 medium — moderately distinctive | disappear, disappears |
| 1013 | **burning** | 11 | 1,564.45 | 8.206841 | 🟢 medium — moderately distinctive | - |
| 1014 | **nevertheless** | 12 | 1,562.53 | 7.513694 | 🟢 medium — moderately distinctive | - |
| 1015 | **fill** | 12 | 1,562.53 | 7.513694 | 🟢 medium — moderately distinctive | fill, fills |
| 1016 | **prevent** | 16 | 1,559.09 | 5.622843 | 🟢 medium — moderately distinctive | prevent, prevents |
| 1017 | **depend** | 14 | 1,556.41 | 6.415081 | 🟢 medium — moderately distinctive | depend, depends |
| 1018 | **line** | 19 | 1,547.23 | 4.699034 | 🟢 medium — moderately distinctive | line, lines |
| 1019 | **invited** | 13 | 1,543.74 | 6.852295 | 🟢 medium — moderately distinctive | - |
| 1020 | **inward** | 10 | 1,542.35 | 8.899988 | 🟢 medium — moderately distinctive | inward, inwards |
| 1021 | **transformed** | 10 | 1,542.35 | 8.899988 | 🟢 medium — moderately distinctive | - |
| 1022 | **created** | 14 | 1,541.70 | 6.354457 | 🟢 medium — moderately distinctive | - |
| 1023 | **constant** | 12 | 1,538.04 | 7.395911 | 🟢 medium — moderately distinctive | - |
| 1024 | **fell** | 22 | 1,529.42 | 4.01152 | 🟢 medium — moderately distinctive | - |
| 1025 | **starting** | 15 | 1,512.99 | 5.820374 | 🟢 medium — moderately distinctive | - |
| 1026 | **involved** | 16 | 1,504.64 | 5.42647 | 🟢 medium — moderately distinctive | - |
| 1027 | **vital** | 13 | 1,503.88 | 6.675364 | 🟢 medium — moderately distinctive | - |
| 1028 | **bow** | 11 | 1,503.75 | 7.888387 | 🟢 medium — moderately distinctive | - |
| 1029 | **continually** | 10 | 1,503.68 | 8.676844 | 🟢 medium — moderately distinctive | - |
| 1030 | **treat** | 10 | 1,503.68 | 8.676844 | 🟢 medium — moderately distinctive | - |
| 1031 | **phenomena** | 9 | 1,496.23 | 9.593135 | 🟢 medium — moderately distinctive | - |
| 1032 | **wander** | 9 | 1,496.23 | 9.593135 | 🟢 medium — moderately distinctive | wander, wanders |
| 1033 | **deaf** | 9 | 1,496.23 | 9.593135 | 🟢 medium — moderately distinctive | - |
| 1034 | **skilled** | 9 | 1,496.23 | 9.593135 | 🟢 medium — moderately distinctive | - |
| 1035 | **caring** | 9 | 1,496.23 | 9.593135 | 🟢 medium — moderately distinctive | - |
| 1036 | **walking** | 9 | 1,496.23 | 9.593135 | 🟢 medium — moderately distinctive | - |
| 1037 | **victim** | 9 | 1,496.23 | 9.593135 | 🟢 medium — moderately distinctive | victim, victims |
| 1038 | **agony** | 9 | 1,496.23 | 9.593135 | 🟢 medium — moderately distinctive | agonies, agony |
| 1039 | **retribution** | 9 | 1,496.23 | 9.593135 | 🟢 medium — moderately distinctive | - |
| 1040 | **auspicious** | 9 | 1,496.23 | 9.593135 | 🟢 medium — moderately distinctive | - |
| 1041 | **loving** | 9 | 1,496.23 | 9.593135 | 🟢 medium — moderately distinctive | - |
| 1042 | **hate** | 9 | 1,496.23 | 9.593135 | 🟢 medium — moderately distinctive | - |
| 1043 | **attainment** | 9 | 1,496.23 | 9.593135 | 🟢 medium — moderately distinctive | attainment, attainments |
| 1044 | **distracted** | 9 | 1,495.74 | 9.59 | 🟢 medium — moderately distinctive | - |
| 1045 | **meritorious** | 9 | 1,495.74 | 9.59 | 🟢 medium — moderately distinctive | - |
| 1046 | **terrifying** | 9 | 1,495.74 | 9.59 | 🟢 medium — moderately distinctive | - |
| 1047 | **thirty-two** | 9 | 1,495.74 | 9.59 | 🟢 medium — moderately distinctive | - |
| 1048 | **jambudvipa** | 9 | 1,495.74 | 9.59 | 🟢 medium — moderately distinctive | - |
| 1049 | **detsen** | 9 | 1,495.74 | 9.59 | 🟢 medium — moderately distinctive | - |
| 1050 | **affliction** | 9 | 1,495.74 | 9.59 | 🟢 medium — moderately distinctive | affliction, afflictions |
| 1051 | **solitude** | 9 | 1,495.74 | 9.59 | 🟢 medium — moderately distinctive | solitude, solitudes |
| 1052 | **delusion** | 9 | 1,495.74 | 9.59 | 🟢 medium — moderately distinctive | delusion, delusions |
| 1053 | **doesn** | 9 | 1,495.74 | 9.59 | 🟢 medium — moderately distinctive | - |
| 1054 | **remorse** | 9 | 1,495.74 | 9.59 | 🟢 medium — moderately distinctive | - |
| 1055 | **aris** | 9 | 1,495.74 | 9.59 | 🟢 medium — moderately distinctive | - |
| 1056 | **holy** | 9 | 1,495.74 | 9.59 | 🟢 medium — moderately distinctive | - |
| 1057 | **celestial** | 9 | 1,495.74 | 9.59 | 🟢 medium — moderately distinctive | - |
| 1058 | **arhat** | 9 | 1,495.74 | 9.59 | 🟢 medium — moderately distinctive | arhat, arhats |
| 1059 | **lhasa** | 9 | 1,495.74 | 9.59 | 🟢 medium — moderately distinctive | - |
| 1060 | **corpse** | 9 | 1,495.74 | 9.59 | 🟢 medium — moderately distinctive | - |
| 1061 | **bitch** | 9 | 1,495.74 | 9.59 | 🟢 medium — moderately distinctive | - |
| 1062 | **thangpa** | 9 | 1,495.74 | 9.59 | 🟢 medium — moderately distinctive | - |
| 1063 | **thank** | 9 | 1,495.74 | 9.59 | 🟢 medium — moderately distinctive | thank, thanks |
| 1064 | **solitary** | 9 | 1,495.74 | 9.59 | 🟢 medium — moderately distinctive | - |
| 1065 | **sariputra** | 9 | 1,495.74 | 9.59 | 🟢 medium — moderately distinctive | - |
| 1066 | **virtuous** | 9 | 1,495.74 | 9.59 | 🟢 medium — moderately distinctive | - |
| 1067 | **hors** | 9 | 1,495.74 | 9.59 | 🟢 medium — moderately distinctive | - |
| 1068 | **nun** | 9 | 1,495.74 | 9.59 | 🟢 medium — moderately distinctive | nun, nuns |
| 1069 | **begging** | 9 | 1,495.74 | 9.59 | 🟢 medium — moderately distinctive | - |
| 1070 | **benefactor** | 9 | 1,495.74 | 9.59 | 🟢 medium — moderately distinctive | benefactor, benefactors |
| 1071 | **feast** | 9 | 1,495.74 | 9.59 | 🟢 medium — moderately distinctive | feast, feasts |
| 1072 | **dwell** | 9 | 1,495.74 | 9.59 | 🟢 medium — moderately distinctive | dwell, dwells |
| 1073 | **immaculate** | 9 | 1,495.74 | 9.59 | 🟢 medium — moderately distinctive | - |
| 1074 | **caste** | 9 | 1,495.74 | 9.59 | 🟢 medium — moderately distinctive | - |
| 1075 | **entrust** | 9 | 1,495.74 | 9.59 | 🟢 medium — moderately distinctive | - |
| 1076 | **visualized** | 9 | 1,495.74 | 9.59 | 🟢 medium — moderately distinctive | - |
| 1077 | **melt** | 9 | 1,495.74 | 9.59 | 🟢 medium — moderately distinctive | melt, melts |
| 1078 | **visualizing** | 9 | 1,495.74 | 9.59 | 🟢 medium — moderately distinctive | - |
| 1079 | **bhagavan** | 9 | 1,495.74 | 9.59 | 🟢 medium — moderately distinctive | - |
| 1080 | **immediate** | 15 | 1,492.87 | 5.742988 | 🟢 medium — moderately distinctive | - |
| 1081 | **army** | 11 | 1,487.16 | 7.801376 | 🟢 medium — moderately distinctive | armies, army |
| 1082 | **door** | 12 | 1,487.06 | 7.150788 | 🟢 medium — moderately distinctive | door, doors |
| 1083 | **carry** | 14 | 1,486.61 | 6.127399 | 🟢 medium — moderately distinctive | carries, carry |
| 1084 | **greater** | 16 | 1,485.94 | 5.359029 | 🟢 medium — moderately distinctive | - |
| 1085 | **necessary** | 16 | 1,483.93 | 5.351808 | 🟢 medium — moderately distinctive | - |
| 1086 | **representing** | 14 | 1,479.15 | 6.096628 | 🟢 medium — moderately distinctive | - |
| 1087 | **totally** | 12 | 1,478.21 | 7.108229 | 🟢 medium — moderately distinctive | - |
| 1088 | **error** | 10 | 1,472.09 | 8.494523 | 🟢 medium — moderately distinctive | error, errors |
| 1089 | **learning** | 10 | 1,472.09 | 8.494523 | 🟢 medium — moderately distinctive | - |
| 1090 | **green** | 12 | 1,469.72 | 7.067407 | 🟢 medium — moderately distinctive | - |
| 1091 | **satisfied** | 13 | 1,464.84 | 6.502093 | 🟢 medium — moderately distinctive | - |
| 1092 | **equally** | 12 | 1,461.57 | 7.028186 | 🟢 medium — moderately distinctive | - |
| 1093 | **golden** | 12 | 1,461.57 | 7.028186 | 🟢 medium — moderately distinctive | - |
| 1094 | **trust** | 17 | 1,460.78 | 4.958406 | 🟢 medium — moderately distinctive | - |
| 1095 | **possible** | 19 | 1,459.99 | 4.43408 | 🟢 medium — moderately distinctive | - |
| 1096 | **seat** | 11 | 1,457.78 | 7.647225 | 🟢 medium — moderately distinctive | - |
| 1097 | **length** | 11 | 1,457.78 | 7.647225 | 🟢 medium — moderately distinctive | - |
| 1098 | **disease** | 12 | 1,446.16 | 6.954078 | 🟢 medium — moderately distinctive | - |
| 1099 | **medicine** | 10 | 1,445.37 | 8.340372 | 🟢 medium — moderately distinctive | medicine, medicines |
| 1100 | **cushion** | 10 | 1,445.37 | 8.340372 | 🟢 medium — moderately distinctive | cushion, cushions |
| 1101 | **lie** | 10 | 1,445.37 | 8.340372 | 🟢 medium — moderately distinctive | - |
| 1102 | **beauty** | 10 | 1,445.37 | 8.340372 | 🟢 medium — moderately distinctive | - |
| 1103 | **crushed** | 10 | 1,445.37 | 8.340372 | 🟢 medium — moderately distinctive | - |
| 1104 | **region** | 14 | 1,444.92 | 5.955549 | 🟢 medium — moderately distinctive | region, regions |
| 1105 | **exactly** | 11 | 1,444.62 | 7.578232 | 🟢 medium — moderately distinctive | - |
| 1106 | **ago** | 19 | 1,437.15 | 4.364704 | 🟢 medium — moderately distinctive | - |
| 1107 | **poured** | 9 | 1,432.99 | 9.18767 | 🟢 medium — moderately distinctive | - |
| 1108 | **illusion** | 9 | 1,432.99 | 9.18767 | 🟢 medium — moderately distinctive | illusion, illusions |
| 1109 | **surface** | 11 | 1,432.32 | 7.513694 | 🟢 medium — moderately distinctive | surface, surfaces |
| 1110 | **drop** | 18 | 1,431.54 | 4.589189 | 🟢 medium — moderately distinctive | drop, drops |
| 1111 | **arisen** | 10 | 1,422.23 | 8.206841 | 🟢 medium — moderately distinctive | - |
| 1112 | **strive** | 10 | 1,422.23 | 8.206841 | 🟢 medium — moderately distinctive | - |
| 1113 | **position** | 17 | 1,410.91 | 4.789114 | 🟢 medium — moderately distinctive | position, positions |
| 1114 | **rule** | 13 | 1,410.51 | 6.260931 | 🟢 medium — moderately distinctive | rule, rules |
| 1115 | **arising** | 11 | 1,409.87 | 7.395911 | 🟢 medium — moderately distinctive | - |
| 1116 | **today** | 24 | 1,407.69 | 3.384545 | 🟢 medium — moderately distinctive | - |
| 1117 | **carried** | 13 | 1,402.60 | 6.225839 | 🟢 medium — moderately distinctive | - |
| 1118 | **repeat** | 10 | 1,401.82 | 8.089058 | 🟢 medium — moderately distinctive | repeat, repeats |
| 1119 | **sight** | 11 | 1,399.56 | 7.341843 | 🟢 medium — moderately distinctive | - |
| 1120 | **return** | 16 | 1,398.73 | 5.044535 | 🟢 medium — moderately distinctive | return, returns |
| 1121 | **established** | 13 | 1,394.97 | 6.191938 | 🟢 medium — moderately distinctive | - |
| 1122 | **especially** | 14 | 1,390.78 | 5.732405 | 🟢 medium — moderately distinctive | - |
| 1123 | **faithful** | 9 | 1,388.12 | 8.899988 | 🟢 medium — moderately distinctive | - |
| 1124 | **outward** | 9 | 1,388.12 | 8.899988 | 🟢 medium — moderately distinctive | outward, outwards |
| 1125 | **touching** | 9 | 1,388.12 | 8.899988 | 🟢 medium — moderately distinctive | - |
| 1126 | **peaceful** | 9 | 1,388.12 | 8.899988 | 🟢 medium — moderately distinctive | - |
| 1127 | **conviction** | 9 | 1,388.12 | 8.899988 | 🟢 medium — moderately distinctive | - |
| 1128 | **highest** | 13 | 1,383.98 | 6.143148 | 🟢 medium — moderately distinctive | - |
| 1129 | **driven** | 10 | 1,383.56 | 7.983697 | 🟢 medium — moderately distinctive | - |
| 1130 | **gesture** | 10 | 1,383.56 | 7.983697 | 🟢 medium — moderately distinctive | gesture, gestures |
| 1131 | **building** | 14 | 1,378.34 | 5.681112 | 🟢 medium — moderately distinctive | building, buildings |
| 1132 | **turning** | 12 | 1,377.25 | 6.622721 | 🟢 medium — moderately distinctive | turning, turnings |
| 1133 | **apart** | 11 | 1,371.61 | 7.19524 | 🟢 medium — moderately distinctive | - |
| 1134 | **comfortable** | 10 | 1,367.04 | 7.888387 | 🟢 medium — moderately distinctive | - |
| 1135 | **described** | 13 | 1,366.77 | 6.066775 | 🟢 medium — moderately distinctive | - |
| 1136 | **outside** | 14 | 1,355.21 | 5.585802 | 🟢 medium — moderately distinctive | - |
| 1137 | **accept** | 14 | 1,355.21 | 5.585802 | 🟢 medium — moderately distinctive | - |
| 1138 | **served** | 11 | 1,355.03 | 7.108229 | 🟢 medium — moderately distinctive | - |
| 1139 | **swept** | 9 | 1,353.31 | 8.676844 | 🟢 medium — moderately distinctive | - |
| 1140 | **appearing** | 9 | 1,353.31 | 8.676844 | 🟢 medium — moderately distinctive | - |
| 1141 | **sand** | 10 | 1,351.96 | 7.801376 | 🟢 medium — moderately distinctive | sand, sands |
| 1142 | **contain** | 11 | 1,347.25 | 7.067407 | 🟢 medium — moderately distinctive | contain, contains |
| 1143 | **sound** | 11 | 1,339.77 | 7.028186 | 🟢 medium — moderately distinctive | sound, sounds |
| 1144 | **involve** | 11 | 1,339.77 | 7.028186 | 🟢 medium — moderately distinctive | involve, involves |
| 1145 | **caused** | 15 | 1,338.85 | 5.150484 | 🟢 medium — moderately distinctive | - |
| 1146 | **yellow** | 10 | 1,338.09 | 7.721333 | 🟢 medium — moderately distinctive | - |
| 1147 | **union** | 17 | 1,333.80 | 4.527381 | 🟢 medium — moderately distinctive | union, unions |
| 1148 | **degenerate** | 8 | 1,329.98 | 9.593135 | 🟢 medium — moderately distinctive | - |
| 1149 | **criticize** | 8 | 1,329.98 | 9.593135 | 🟢 medium — moderately distinctive | - |
| 1150 | **sens** | 8 | 1,329.98 | 9.593135 | 🟢 medium — moderately distinctive | - |
| 1151 | **lip** | 8 | 1,329.98 | 9.593135 | 🟢 medium — moderately distinctive | lip, lips |
| 1152 | **burnt** | 8 | 1,329.98 | 9.593135 | 🟢 medium — moderately distinctive | - |
| 1153 | **ate** | 8 | 1,329.98 | 9.593135 | 🟢 medium — moderately distinctive | - |
| 1154 | **steal** | 8 | 1,329.98 | 9.593135 | 🟢 medium — moderately distinctive | steal, steals |
| 1155 | **worthless** | 8 | 1,329.98 | 9.593135 | 🟢 medium — moderately distinctive | - |
| 1156 | **beating** | 8 | 1,329.98 | 9.593135 | 🟢 medium — moderately distinctive | - |
| 1157 | **perhap** | 8 | 1,329.54 | 9.59 | 🟢 medium — moderately distinctive | - |
| 1158 | **believing** | 8 | 1,329.54 | 9.59 | 🟢 medium — moderately distinctive | - |
| 1159 | **beside** | 8 | 1,329.54 | 9.59 | 🟢 medium — moderately distinctive | beside, besides |
| 1160 | **endure** | 8 | 1,329.54 | 9.59 | 🟢 medium — moderately distinctive | endure, endures |
| 1161 | **henchmen** | 8 | 1,329.54 | 9.59 | 🟢 medium — moderately distinctive | - |
| 1162 | **trisong** | 8 | 1,329.54 | 9.59 | 🟢 medium — moderately distinctive | - |
| 1163 | **naga** | 8 | 1,329.54 | 9.59 | 🟢 medium — moderately distinctive | naga, nagas |
| 1164 | **ambrosia** | 8 | 1,329.54 | 9.59 | 🟢 medium — moderately distinctive | ambrosia, ambrosias |
| 1165 | **scripture** | 8 | 1,329.54 | 9.59 | 🟢 medium — moderately distinctive | - |
| 1166 | **eighteen** | 8 | 1,329.54 | 9.59 | 🟢 medium — moderately distinctive | - |
| 1167 | **endlessly** | 8 | 1,329.54 | 9.59 | 🟢 medium — moderately distinctive | - |
| 1168 | **cry** | 8 | 1,329.54 | 9.59 | 🟢 medium — moderately distinctive | cries, cry |
| 1169 | **sentient** | 8 | 1,329.54 | 9.59 | 🟢 medium — moderately distinctive | - |
| 1170 | **maitreya** | 8 | 1,329.54 | 9.59 | 🟢 medium — moderately distinctive | - |
| 1171 | **husband** | 8 | 1,329.54 | 9.59 | 🟢 medium — moderately distinctive | husband, husbands |
| 1172 | **monastery** | 8 | 1,329.54 | 9.59 | 🟢 medium — moderately distinctive | monasteries, monastery |
| 1173 | **hous** | 8 | 1,329.54 | 9.59 | 🟢 medium — moderately distinctive | - |
| 1174 | **lap** | 8 | 1,329.54 | 9.59 | 🟢 medium — moderately distinctive | lap, laps |
| 1175 | **blessed** | 8 | 1,329.54 | 9.59 | 🟢 medium — moderately distinctive | - |
| 1176 | **maudgalyayana** | 8 | 1,329.54 | 9.59 | 🟢 medium — moderately distinctive | - |
| 1177 | **samsaric** | 8 | 1,329.54 | 9.59 | 🟢 medium — moderately distinctive | - |
| 1178 | **ripened** | 8 | 1,329.54 | 9.59 | 🟢 medium — moderately distinctive | - |
| 1179 | **tiniest** | 8 | 1,329.54 | 9.59 | 🟢 medium — moderately distinctive | - |
| 1180 | **didn** | 8 | 1,329.54 | 9.59 | 🟢 medium — moderately distinctive | - |
| 1181 | **mouthful** | 8 | 1,329.54 | 9.59 | 🟢 medium — moderately distinctive | - |
| 1182 | **tsampa** | 8 | 1,329.54 | 9.59 | 🟢 medium — moderately distinctive | - |
| 1183 | **langri** | 8 | 1,329.54 | 9.59 | 🟢 medium — moderately distinctive | - |
| 1184 | **covetousness** | 8 | 1,329.54 | 9.59 | 🟢 medium — moderately distinctive | - |
| 1185 | **silken** | 8 | 1,329.54 | 9.59 | 🟢 medium — moderately distinctive | - |
| 1186 | **inseparable** | 8 | 1,329.54 | 9.59 | 🟢 medium — moderately distinctive | - |
| 1187 | **prajnaparamita** | 8 | 1,329.54 | 9.59 | 🟢 medium — moderately distinctive | - |
| 1188 | **padma** | 8 | 1,329.54 | 9.59 | 🟢 medium — moderately distinctive | - |
| 1189 | **chekawa** | 8 | 1,329.54 | 9.59 | 🟢 medium — moderately distinctive | - |
| 1190 | **manjusrimitra** | 8 | 1,329.54 | 9.59 | 🟢 medium — moderately distinctive | - |
| 1191 | **strong** | 17 | 1,328.27 | 4.50863 | 🟢 medium — moderately distinctive | - |
| 1192 | **posture** | 9 | 1,324.88 | 8.494523 | 🟢 medium — moderately distinctive | - |
| 1193 | **change** | 17 | 1,316.65 | 4.469171 | 🟢 medium — moderately distinctive | change, changes |
| 1194 | **goal** | 12 | 1,313.46 | 6.31599 | 🟢 medium — moderately distinctive | goal, goals |
| 1195 | **evening** | 10 | 1,313.29 | 7.578232 | 🟢 medium — moderately distinctive | - |
| 1196 | **danger** | 11 | 1,312.49 | 6.885085 | 🟢 medium — moderately distinctive | danger, dangers |
| 1197 | **break** | 12 | 1,309.57 | 6.297298 | 🟢 medium — moderately distinctive | break, breaks |
| 1198 | **standing** | 10 | 1,302.11 | 7.513694 | 🟢 medium — moderately distinctive | - |
| 1199 | **dry** | 12 | 1,302.01 | 6.260931 | 🟢 medium — moderately distinctive | - |
| 1200 | **male** | 9 | 1,300.83 | 8.340372 | 🟢 medium — moderately distinctive | male, males |
| 1201 | **lifestyle** | 9 | 1,300.83 | 8.340372 | 🟢 medium — moderately distinctive | lifestyle, lifestyles |
| 1202 | **lacking** | 9 | 1,300.83 | 8.340372 | 🟢 medium — moderately distinctive | - |
| 1203 | **destroyed** | 11 | 1,300.19 | 6.820546 | 🟢 medium — moderately distinctive | - |
| 1204 | **wood** | 11 | 1,294.32 | 6.789775 | 🟢 medium — moderately distinctive | wood, woods |
| 1205 | **named** | 13 | 1,293.82 | 5.742988 | 🟢 medium — moderately distinctive | - |
| 1206 | **exist** | 10 | 1,291.60 | 7.453069 | 🟢 medium — moderately distinctive | exist, exists |
| 1207 | **performed** | 10 | 1,291.60 | 7.453069 | 🟢 medium — moderately distinctive | - |
| 1208 | **stand** | 12 | 1,291.16 | 6.208745 | 🟢 medium — moderately distinctive | stand, stands |
| 1209 | **finding** | 11 | 1,283.10 | 6.730934 | 🟢 medium — moderately distinctive | - |
| 1210 | **bigger** | 10 | 1,281.70 | 7.395911 | 🟢 medium — moderately distinctive | - |
| 1211 | **harming** | 9 | 1,280.01 | 8.206841 | 🟢 medium — moderately distinctive | - |
| 1212 | **thrown** | 9 | 1,280.01 | 8.206841 | 🟢 medium — moderately distinctive | - |
| 1213 | **sitting** | 9 | 1,280.01 | 8.206841 | 🟢 medium — moderately distinctive | - |
| 1214 | **skill** | 8 | 1,273.77 | 9.18767 | 🟢 medium — moderately distinctive | - |
| 1215 | **taste** | 8 | 1,273.77 | 9.18767 | 🟢 medium — moderately distinctive | - |
| 1216 | **encounter** | 8 | 1,273.77 | 9.18767 | 🟢 medium — moderately distinctive | encounter, encounters |
| 1217 | **inspire** | 8 | 1,273.77 | 9.18767 | 🟢 medium — moderately distinctive | - |
| 1218 | **nowhere** | 8 | 1,273.77 | 9.18767 | 🟢 medium — moderately distinctive | - |
| 1219 | **butcher** | 8 | 1,273.77 | 9.18767 | 🟢 medium — moderately distinctive | - |
| 1220 | **tiny** | 8 | 1,273.77 | 9.18767 | 🟢 medium — moderately distinctive | - |
| 1221 | **unpleasant** | 8 | 1,273.77 | 9.18767 | 🟢 medium — moderately distinctive | - |
| 1222 | **term** | 15 | 1,271.83 | 4.892655 | 🟢 medium — moderately distinctive | term, terms |
| 1223 | **manner** | 10 | 1,263.44 | 7.29055 | 🟢 medium — moderately distinctive | - |
| 1224 | **process** | 13 | 1,260.47 | 5.594934 | 🟢 medium — moderately distinctive | process, processes |
| 1225 | **owner** | 11 | 1,257.65 | 6.597403 | 🟢 medium — moderately distinctive | owner, owners |
| 1226 | **stage** | 12 | 1,255.61 | 6.037787 | 🟢 medium — moderately distinctive | stage, stages |
| 1227 | **east** | 14 | 1,251.03 | 5.156384 | 🟢 medium — moderately distinctive | - |
| 1228 | **simple** | 9 | 1,245.20 | 7.983697 | 🟢 medium — moderately distinctive | - |
| 1229 | **slip** | 9 | 1,245.20 | 7.983697 | 🟢 medium — moderately distinctive | - |
| 1230 | **meet** | 15 | 1,244.92 | 4.789114 | 🟢 medium — moderately distinctive | - |
| 1231 | **kept** | 11 | 1,239.48 | 6.502093 | 🟢 medium — moderately distinctive | - |
| 1232 | **covered** | 11 | 1,239.48 | 6.502093 | 🟢 medium — moderately distinctive | - |
| 1233 | **separate** | 12 | 1,238.50 | 5.955549 | 🟢 medium — moderately distinctive | - |
| 1234 | **loose** | 8 | 1,233.88 | 8.899988 | 🟢 medium — moderately distinctive | - |
| 1235 | **whatsoever** | 8 | 1,233.88 | 8.899988 | 🟢 medium — moderately distinctive | - |
| 1236 | **twenty** | 8 | 1,233.88 | 8.899988 | 🟢 medium — moderately distinctive | - |
| 1237 | **crime** | 8 | 1,233.88 | 8.899988 | 🟢 medium — moderately distinctive | crime, crimes |
| 1238 | **committing** | 8 | 1,233.88 | 8.899988 | 🟢 medium — moderately distinctive | - |
| 1239 | **expression** | 8 | 1,233.88 | 8.899988 | 🟢 medium — moderately distinctive | expression, expressions |
| 1240 | **reflecting** | 12 | 1,233.10 | 5.929574 | 🟢 medium — moderately distinctive | - |
| 1241 | **ability** | 12 | 1,233.10 | 5.929574 | 🟢 medium — moderately distinctive | abilities, ability |
| 1242 | **close** | 16 | 1,231.87 | 4.442738 | 🟢 medium — moderately distinctive | - |
| 1243 | **trouble** | 10 | 1,231.84 | 7.108229 | 🟢 medium — moderately distinctive | trouble, troubles |
| 1244 | **sent** | 12 | 1,230.45 | 5.916835 | 🟢 medium — moderately distinctive | - |
| 1245 | **applying** | 9 | 1,230.34 | 7.888387 | 🟢 medium — moderately distinctive | - |
| 1246 | **breach** | 9 | 1,230.34 | 7.888387 | 🟢 medium — moderately distinctive | - |
| 1247 | **less** | 16 | 1,227.88 | 4.428349 | 🟢 medium — moderately distinctive | - |
| 1248 | **gone** | 10 | 1,217.97 | 7.028186 | 🟢 medium — moderately distinctive | - |
| 1249 | **establish** | 11 | 1,211.34 | 6.354457 | 🟢 medium — moderately distinctive | establish, establishes |
| 1250 | **felt** | 11 | 1,207.64 | 6.335039 | 🟢 medium — moderately distinctive | - |
| 1251 | **speaking** | 12 | 1,203.34 | 5.786473 | 🟢 medium — moderately distinctive | - |
| 1252 | **seal** | 8 | 1,202.95 | 8.676844 | 🟢 medium — moderately distinctive | - |
| 1253 | **behaviour** | 8 | 1,202.95 | 8.676844 | 🟢 medium — moderately distinctive | - |
| 1254 | **cosmo** | 8 | 1,202.95 | 8.676844 | 🟢 medium — moderately distinctive | - |
| 1255 | **attribute** | 8 | 1,202.95 | 8.676844 | 🟢 medium — moderately distinctive | - |
| 1256 | **peace** | 8 | 1,202.95 | 8.676844 | 🟢 medium — moderately distinctive | - |
| 1257 | **link** | 10 | 1,199.05 | 6.918987 | 🟢 medium — moderately distinctive | - |
| 1258 | **cross** | 10 | 1,193.17 | 6.885085 | 🟢 medium — moderately distinctive | cross, crosses |
| 1259 | **proper** | 9 | 1,192.73 | 7.647225 | 🟢 medium — moderately distinctive | - |
| 1260 | **nobody** | 9 | 1,192.73 | 7.647225 | 🟢 medium — moderately distinctive | - |
| 1261 | **cutting** | 12 | 1,192.10 | 5.732405 | 🟢 medium — moderately distinctive | - |
| 1262 | **containing** | 10 | 1,181.99 | 6.820546 | 🟢 medium — moderately distinctive | - |
| 1263 | **broken** | 10 | 1,181.99 | 6.820546 | 🟢 medium — moderately distinctive | - |
| 1264 | **explaining** | 9 | 1,181.96 | 7.578232 | 🟢 medium — moderately distinctive | - |
| 1265 | **pull** | 9 | 1,181.96 | 7.578232 | 🟢 medium — moderately distinctive | pull, pulls |
| 1266 | **trace** | 8 | 1,177.67 | 8.494523 | 🟢 medium — moderately distinctive | - |
| 1267 | **property** | 12 | 1,173.28 | 5.641891 | 🟢 medium — moderately distinctive | properties, property |
| 1268 | **serious** | 12 | 1,173.28 | 5.641891 | 🟢 medium — moderately distinctive | - |
| 1269 | **bringing** | 11 | 1,171.06 | 6.143148 | 🟢 medium — moderately distinctive | - |
| 1270 | **debt** | 16 | 1,169.52 | 4.217857 | 🟢 medium — moderately distinctive | debt, debts |
| 1271 | **flow** | 12 | 1,165.43 | 5.604151 | 🟢 medium — moderately distinctive | flow, flows |
| 1272 | **glad** | 7 | 1,163.73 | 9.593135 | 🟢 medium — moderately distinctive | - |
| 1273 | **technique** | 7 | 1,163.73 | 9.593135 | 🟢 medium — moderately distinctive | technique, techniques |
| 1274 | **sad** | 7 | 1,163.73 | 9.593135 | 🟢 medium — moderately distinctive | - |
| 1275 | **stupid** | 7 | 1,163.73 | 9.593135 | 🟢 medium — moderately distinctive | - |
| 1276 | **threw** | 7 | 1,163.73 | 9.593135 | 🟢 medium — moderately distinctive | - |
| 1277 | **poisonous** | 7 | 1,163.73 | 9.593135 | 🟢 medium — moderately distinctive | - |
| 1278 | **beg** | 7 | 1,163.73 | 9.593135 | 🟢 medium — moderately distinctive | - |
| 1279 | **sore** | 7 | 1,163.73 | 9.593135 | 🟢 medium — moderately distinctive | sore, sores |
| 1280 | **garland** | 7 | 1,163.73 | 9.593135 | 🟢 medium — moderately distinctive | garland, garlands |
| 1281 | **infinity** | 7 | 1,163.73 | 9.593135 | 🟢 medium — moderately distinctive | - |
| 1282 | **herself** | 7 | 1,163.73 | 9.593135 | 🟢 medium — moderately distinctive | - |
| 1283 | **multitude** | 7 | 1,163.73 | 9.593135 | 🟢 medium — moderately distinctive | multitude, multitudes |
| 1284 | **discover** | 7 | 1,163.73 | 9.593135 | 🟢 medium — moderately distinctive | - |
| 1285 | **avalokitesvara** | 7 | 1,163.35 | 9.59 | 🟢 medium — moderately distinctive | - |
| 1286 | **longchenpa** | 7 | 1,163.35 | 9.59 | 🟢 medium — moderately distinctive | - |
| 1287 | **habitual** | 7 | 1,163.35 | 9.59 | 🟢 medium — moderately distinctive | - |
| 1288 | **dedicating** | 7 | 1,163.35 | 9.59 | 🟢 medium — moderately distinctive | - |
| 1289 | **padmasambhava** | 7 | 1,163.35 | 9.59 | 🟢 medium — moderately distinctive | - |
| 1290 | **hungry** | 7 | 1,163.35 | 9.59 | 🟢 medium — moderately distinctive | - |
| 1291 | **forgetting** | 7 | 1,163.35 | 9.59 | 🟢 medium — moderately distinctive | - |
| 1292 | **smell** | 7 | 1,163.35 | 9.59 | 🟢 medium — moderately distinctive | smell, smells |
| 1293 | **deluded** | 7 | 1,163.35 | 9.59 | 🟢 medium — moderately distinctive | - |
| 1294 | **rope** | 7 | 1,163.35 | 9.59 | 🟢 medium — moderately distinctive | rope, ropes |
| 1295 | **layman** | 7 | 1,163.35 | 9.59 | 🟢 medium — moderately distinctive | - |
| 1296 | **mastered** | 7 | 1,163.35 | 9.59 | 🟢 medium — moderately distinctive | - |
| 1297 | **vinaya** | 7 | 1,163.35 | 9.59 | 🟢 medium — moderately distinctive | - |
| 1298 | **atra** | 7 | 1,163.35 | 9.59 | 🟢 medium — moderately distinctive | - |
| 1299 | **songtsen** | 7 | 1,163.35 | 9.59 | 🟢 medium — moderately distinctive | - |
| 1300 | **gampo** | 7 | 1,163.35 | 9.59 | 🟢 medium — moderately distinctive | - |
| 1301 | **tibetan** | 7 | 1,163.35 | 9.59 | 🟢 medium — moderately distinctive | tibetan, tibetans |
| 1302 | **begged** | 7 | 1,163.35 | 9.59 | 🟢 medium — moderately distinctive | - |
| 1303 | **everyday** | 7 | 1,163.35 | 9.59 | 🟢 medium — moderately distinctive | - |
| 1304 | **aroused** | 7 | 1,163.35 | 9.59 | 🟢 medium — moderately distinctive | - |
| 1305 | **ripen** | 7 | 1,163.35 | 9.59 | 🟢 medium — moderately distinctive | ripen, ripens |
| 1306 | **ancient** | 7 | 1,163.35 | 9.59 | 🟢 medium — moderately distinctive | - |
| 1307 | **magical** | 7 | 1,163.35 | 9.59 | 🟢 medium — moderately distinctive | - |
| 1308 | **needle** | 7 | 1,163.35 | 9.59 | 🟢 medium — moderately distinctive | needle, needles |
| 1309 | **kadampa** | 7 | 1,163.35 | 9.59 | 🟢 medium — moderately distinctive | kadampa, kadampas |
| 1310 | **katyayana** | 7 | 1,163.35 | 9.59 | 🟢 medium — moderately distinctive | - |
| 1311 | **dear** | 7 | 1,163.35 | 9.59 | 🟢 medium — moderately distinctive | - |
| 1312 | **clinging** | 7 | 1,163.35 | 9.59 | 🟢 medium — moderately distinctive | clinging, clingings |
| 1313 | **answered** | 7 | 1,163.35 | 9.59 | 🟢 medium — moderately distinctive | - |
| 1314 | **fool** | 7 | 1,163.35 | 9.59 | 🟢 medium — moderately distinctive | fool, fools |
| 1315 | **pus** | 7 | 1,163.35 | 9.59 | 🟢 medium — moderately distinctive | - |
| 1316 | **forehead** | 7 | 1,163.35 | 9.59 | 🟢 medium — moderately distinctive | forehead, foreheads |
| 1317 | **girl** | 7 | 1,163.35 | 9.59 | 🟢 medium — moderately distinctive | girl, girls |
| 1318 | **lala** | 7 | 1,163.35 | 9.59 | 🟢 medium — moderately distinctive | lala, lalas |
| 1319 | **medicinal** | 7 | 1,163.35 | 9.59 | 🟢 medium — moderately distinctive | - |
| 1320 | **praying** | 7 | 1,163.35 | 9.59 | 🟢 medium — moderately distinctive | - |
| 1321 | **marvellous** | 7 | 1,163.35 | 9.59 | 🟢 medium — moderately distinctive | - |
| 1322 | **lhodrak** | 7 | 1,163.35 | 9.59 | 🟢 medium — moderately distinctive | - |
| 1323 | **vimalamitra** | 7 | 1,163.35 | 9.59 | 🟢 medium — moderately distinctive | - |
| 1324 | **primordial** | 7 | 1,163.35 | 9.59 | 🟢 medium — moderately distinctive | - |
| 1325 | **symboliz** | 7 | 1,163.35 | 9.59 | 🟢 medium — moderately distinctive | - |
| 1326 | **stupa** | 7 | 1,163.35 | 9.59 | 🟢 medium — moderately distinctive | - |
| 1327 | **sharawa** | 7 | 1,163.35 | 9.59 | 🟢 medium — moderately distinctive | - |
| 1328 | **gift** | 7 | 1,163.35 | 9.59 | 🟢 medium — moderately distinctive | gift, gifts |
| 1329 | **atiyoga** | 7 | 1,163.35 | 9.59 | 🟢 medium — moderately distinctive | - |
| 1330 | **amount** | 15 | 1,163.30 | 4.475141 | 🟢 medium — moderately distinctive | amount, amounts |
| 1331 | **minor** | 9 | 1,162.44 | 7.453069 | 🟢 medium — moderately distinctive | - |
| 1332 | **language** | 9 | 1,162.44 | 7.453069 | 🟢 medium — moderately distinctive | language, languages |
| 1333 | **snow** | 9 | 1,162.44 | 7.453069 | 🟢 medium — moderately distinctive | snow, snows |
| 1334 | **naturally** | 8 | 1,156.30 | 8.340372 | 🟢 medium — moderately distinctive | - |
| 1335 | **refer** | 8 | 1,156.30 | 8.340372 | 🟢 medium — moderately distinctive | refer, refers |
| 1336 | **dedicated** | 8 | 1,156.30 | 8.340372 | 🟢 medium — moderately distinctive | - |
| 1337 | **bit** | 10 | 1,152.21 | 6.648696 | 🟢 medium — moderately distinctive | bit, bits |
| 1338 | **convinced** | 10 | 1,147.71 | 6.622721 | 🟢 medium — moderately distinctive | - |
| 1339 | **nine** | 19 | 1,139.53 | 3.460822 | 🟢 medium — moderately distinctive | - |
| 1340 | **period** | 17 | 1,139.52 | 3.867917 | 🟢 medium — moderately distinctive | period, periods |
| 1341 | **meal** | 10 | 1,139.04 | 6.57271 | 🟢 medium — moderately distinctive | meal, meals |
| 1342 | **plain** | 8 | 1,137.78 | 8.206841 | 🟢 medium — moderately distinctive | plain, plains |
| 1343 | **confusion** | 8 | 1,137.78 | 8.206841 | 🟢 medium — moderately distinctive | - |
| 1344 | **deeply** | 8 | 1,137.78 | 8.206841 | 🟢 medium — moderately distinctive | - |
| 1345 | **correspond** | 8 | 1,137.78 | 8.206841 | 🟢 medium — moderately distinctive | correspond, corresponds |
| 1346 | **rainbow** | 8 | 1,137.78 | 8.206841 | 🟢 medium — moderately distinctive | - |
| 1347 | **identical** | 8 | 1,137.78 | 8.206841 | 🟢 medium — moderately distinctive | - |
| 1348 | **check** | 9 | 1,137.10 | 7.29055 | 🟢 medium — moderately distinctive | - |
| 1349 | **seek** | 13 | 1,134.10 | 5.034009 | 🟢 medium — moderately distinctive | - |
| 1350 | **universal** | 9 | 1,129.49 | 7.24176 | 🟢 medium — moderately distinctive | - |
| 1351 | **summer** | 11 | 1,125.52 | 5.904256 | 🟢 medium — moderately distinctive | - |
| 1352 | **lost** | 12 | 1,125.28 | 5.411085 | 🟢 medium — moderately distinctive | - |
| 1353 | **trial** | 8 | 1,121.46 | 8.089058 | 🟢 medium — moderately distinctive | - |
| 1354 | **remedy** | 8 | 1,121.46 | 8.089058 | 🟢 medium — moderately distinctive | - |
| 1355 | **ride** | 8 | 1,121.46 | 8.089058 | 🟢 medium — moderately distinctive | ride, rides |
| 1356 | **occasion** | 8 | 1,121.46 | 8.089058 | 🟢 medium — moderately distinctive | occasion, occasions |
| 1357 | **disc** | 8 | 1,121.46 | 8.089058 | 🟢 medium — moderately distinctive | disc, discs |
| 1358 | **external** | 11 | 1,118.50 | 5.867442 | 🟢 medium — moderately distinctive | - |
| 1359 | **begin** | 12 | 1,117.49 | 5.373627 | 🟢 medium — moderately distinctive | begin, begins |
| 1360 | **represent** | 10 | 1,115.37 | 6.436135 | 🟢 medium — moderately distinctive | represent, represents |
| 1361 | **letting** | 7 | 1,114.54 | 9.18767 | 🟢 medium — moderately distinctive | - |
| 1362 | **onward** | 7 | 1,114.54 | 9.18767 | 🟢 medium — moderately distinctive | onward, onwards |
| 1363 | **ruin** | 7 | 1,114.54 | 9.18767 | 🟢 medium — moderately distinctive | - |
| 1364 | **quarrel** | 7 | 1,114.54 | 9.18767 | 🟢 medium — moderately distinctive | quarrel, quarrels |
| 1365 | **enjoying** | 7 | 1,114.54 | 9.18767 | 🟢 medium — moderately distinctive | - |
| 1366 | **afterward** | 7 | 1,114.54 | 9.18767 | 🟢 medium — moderately distinctive | - |
| 1367 | **cow** | 7 | 1,114.54 | 9.18767 | 🟢 medium — moderately distinctive | cow, cows |
| 1368 | **transmitted** | 7 | 1,114.54 | 9.18767 | 🟢 medium — moderately distinctive | - |
| 1369 | **step** | 11 | 1,113.96 | 5.843631 | 🟢 medium — moderately distinctive | step, steps |
| 1370 | **wall** | 11 | 1,111.73 | 5.831935 | 🟢 medium — moderately distinctive | wall, walls |
| 1371 | **principle** | 12 | 1,109.98 | 5.337522 | 🟢 medium — moderately distinctive | - |
| 1372 | **sister** | 8 | 1,106.85 | 7.983697 | 🟢 medium — moderately distinctive | - |
| 1373 | **pulled** | 8 | 1,106.85 | 7.983697 | 🟢 medium — moderately distinctive | - |
| 1374 | **request** | 11 | 1,105.19 | 5.797646 | 🟢 medium — moderately distinctive | request, requests |
| 1375 | **weak** | 11 | 1,103.06 | 5.786473 | 🟢 medium — moderately distinctive | - |
| 1376 | **fit** | 9 | 1,102.29 | 7.067407 | 🟢 medium — moderately distinctive | fit, fits |
| 1377 | **gold** | 13 | 1,096.19 | 4.865747 | 🟢 medium — moderately distinctive | - |
| 1378 | **aim** | 10 | 1,094.55 | 6.31599 | 🟢 medium — moderately distinctive | aim, aims |
| 1379 | **success** | 10 | 1,091.31 | 6.297298 | 🟢 medium — moderately distinctive | - |
| 1380 | **palm** | 10 | 1,088.13 | 6.278949 | 🟢 medium — moderately distinctive | palm, palms |
| 1381 | **rather** | 12 | 1,087.63 | 5.230037 | 🟢 medium — moderately distinctive | - |
| 1382 | **sea** | 11 | 1,082.98 | 5.681112 | 🟢 medium — moderately distinctive | sea, seas |
| 1383 | **absolutely** | 8 | 1,081.57 | 7.801376 | 🟢 medium — moderately distinctive | - |
| 1384 | **voice** | 8 | 1,081.57 | 7.801376 | 🟢 medium — moderately distinctive | voice, voices |
| 1385 | **touch** | 8 | 1,081.57 | 7.801376 | 🟢 medium — moderately distinctive | touch, touches |
| 1386 | **spark** | 8 | 1,081.57 | 7.801376 | 🟢 medium — moderately distinctive | - |
| 1387 | **travelling** | 7 | 1,079.65 | 8.899988 | 🟢 medium — moderately distinctive | - |
| 1388 | **opposite** | 7 | 1,079.65 | 8.899988 | 🟢 medium — moderately distinctive | - |
| 1389 | **hang** | 7 | 1,079.65 | 8.899988 | 🟢 medium — moderately distinctive | hang, hangs |
| 1390 | **poverty** | 7 | 1,079.65 | 8.899988 | 🟢 medium — moderately distinctive | - |
| 1391 | **prey** | 7 | 1,079.65 | 8.899988 | 🟢 medium — moderately distinctive | - |
| 1392 | **garment** | 7 | 1,079.65 | 8.899988 | 🟢 medium — moderately distinctive | garment, garments |
| 1393 | **calf** | 7 | 1,079.65 | 8.899988 | 🟢 medium — moderately distinctive | - |
| 1394 | **continue** | 15 | 1,076.17 | 4.139953 | 🟢 medium — moderately distinctive | continue, continues |
| 1395 | **difference** | 9 | 1,073.86 | 6.885085 | 🟢 medium — moderately distinctive | - |
| 1396 | **month** | 17 | 1,072.72 | 3.641191 | 🟢 medium — moderately distinctive | month, months |
| 1397 | **rise** | 17 | 1,070.81 | 3.634711 | 🟢 medium — moderately distinctive | - |
| 1398 | **combine** | 8 | 1,070.47 | 7.721333 | 🟢 medium — moderately distinctive | combine, combines |
| 1399 | **rival** | 9 | 1,068.74 | 6.852295 | 🟢 medium — moderately distinctive | rival, rivals |
| 1400 | **search** | 8 | 1,060.20 | 7.647225 | 🟢 medium — moderately distinctive | - |
| 1401 | **money** | 15 | 1,059.46 | 4.075682 | 🟢 medium — moderately distinctive | - |
| 1402 | **gradually** | 9 | 1,054.33 | 6.759922 | 🟢 medium — moderately distinctive | - |
| 1403 | **talking** | 10 | 1,053.93 | 6.08159 | 🟢 medium — moderately distinctive | - |
| 1404 | **destruction** | 7 | 1,052.58 | 8.676844 | 🟢 medium — moderately distinctive | destruction, destructions |
| 1405 | **oral** | 7 | 1,052.58 | 8.676844 | 🟢 medium — moderately distinctive | - |
| 1406 | **catch** | 7 | 1,052.58 | 8.676844 | 🟢 medium — moderately distinctive | catch, catches |
| 1407 | **till** | 7 | 1,052.58 | 8.676844 | 🟢 medium — moderately distinctive | - |
| 1408 | **gate** | 7 | 1,052.58 | 8.676844 | 🟢 medium — moderately distinctive | gate, gates |
| 1409 | **violent** | 7 | 1,052.58 | 8.676844 | 🟢 medium — moderately distinctive | - |
| 1410 | **considered** | 11 | 1,051.43 | 5.515598 | 🟢 medium — moderately distinctive | - |
| 1411 | **barley** | 10 | 1,048.83 | 6.052176 | 🟢 medium — moderately distinctive | - |
| 1412 | **country** | 13 | 1,046.32 | 4.644375 | 🟢 medium — moderately distinctive | countries, country |
| 1413 | **purpose** | 9 | 1,045.42 | 6.702763 | 🟢 medium — moderately distinctive | - |
| 1414 | **situation** | 12 | 1,044.70 | 5.023592 | 🟢 medium — moderately distinctive | situation, situations |
| 1415 | **task** | 8 | 1,041.69 | 7.513694 | 🟢 medium — moderately distinctive | task, tasks |
| 1416 | **usually** | 9 | 1,041.15 | 6.675364 | 🟢 medium — moderately distinctive | - |
| 1417 | **battle** | 9 | 1,041.15 | 6.675364 | 🟢 medium — moderately distinctive | battle, battles |
| 1418 | **prepared** | 11 | 1,032.97 | 5.418748 | 🟢 medium — moderately distinctive | - |
| 1419 | **receiving** | 9 | 1,032.94 | 6.622721 | 🟢 medium — moderately distinctive | - |
| 1420 | **gem** | 7 | 1,030.46 | 8.494523 | 🟢 medium — moderately distinctive | gem, gems |
| 1421 | **experiencing** | 7 | 1,030.46 | 8.494523 | 🟢 medium — moderately distinctive | - |
| 1422 | **previous** | 14 | 1,026.72 | 4.231843 | 🟢 medium — moderately distinctive | - |
| 1423 | **capable** | 8 | 1,017.86 | 7.341843 | 🟢 medium — moderately distinctive | - |
| 1424 | **occur** | 9 | 1,014.12 | 6.502093 | 🟢 medium — moderately distinctive | occur, occurs |
| 1425 | **pit** | 7 | 1,011.76 | 8.340372 | 🟢 medium — moderately distinctive | pit, pits |
| 1426 | **shore** | 7 | 1,011.76 | 8.340372 | 🟢 medium — moderately distinctive | shore, shores |
| 1427 | **display** | 7 | 1,011.76 | 8.340372 | 🟢 medium — moderately distinctive | display, displays |
| 1428 | **solid** | 8 | 1,010.75 | 7.29055 | 🟢 medium — moderately distinctive | - |
| 1429 | **favourable** | 9 | 1,010.62 | 6.47962 | 🟢 medium — moderately distinctive | - |
| 1430 | **greatest** | 8 | 1,003.99 | 7.24176 | 🟢 medium — moderately distinctive | - |
| 1431 | **travel** | 8 | 1,003.99 | 7.24176 | 🟢 medium — moderately distinctive | - |
| 1432 | **conclusion** | 8 | 997.54 | 7.19524 | 🟢 medium — moderately distinctive | - |
| 1433 | **permitted** | 8 | 997.54 | 7.19524 | 🟢 medium — moderately distinctive | - |
| 1434 | **whoever** | 6 | 997.48 | 9.593135 | 🟢 medium — moderately distinctive | - |
| 1435 | **famous** | 6 | 997.48 | 9.593135 | 🟢 medium — moderately distinctive | - |
| 1436 | **distinguish** | 6 | 997.48 | 9.593135 | 🟢 medium — moderately distinctive | - |
| 1437 | **pea** | 6 | 997.48 | 9.593135 | 🟢 medium — moderately distinctive | pea, peas |
| 1438 | **unpredictable** | 6 | 997.48 | 9.593135 | 🟢 medium — moderately distinctive | - |
| 1439 | **naked** | 6 | 997.48 | 9.593135 | 🟢 medium — moderately distinctive | - |
| 1440 | **whip** | 6 | 997.48 | 9.593135 | 🟢 medium — moderately distinctive | whip, whips |
| 1441 | **shame** | 6 | 997.48 | 9.593135 | 🟢 medium — moderately distinctive | - |
| 1442 | **worm** | 6 | 997.48 | 9.593135 | 🟢 medium — moderately distinctive | - |
| 1443 | **trunk** | 6 | 997.48 | 9.593135 | 🟢 medium — moderately distinctive | - |
| 1444 | **buddhist** | 6 | 997.48 | 9.593135 | 🟢 medium — moderately distinctive | buddhist, buddhists |
| 1445 | **heart-essence** | 6 | 997.16 | 9.59 | 🟢 medium — moderately distinctive | - |
| 1446 | **twenty-five** | 6 | 997.16 | 9.59 | 🟢 medium — moderately distinctive | - |
| 1447 | **vajradhara** | 6 | 997.16 | 9.59 | 🟢 medium — moderately distinctive | - |
| 1448 | **deer** | 6 | 997.16 | 9.59 | 🟢 medium — moderately distinctive | - |
| 1449 | **hallucination** | 6 | 997.16 | 9.59 | 🟢 medium — moderately distinctive | hallucination, hallucinations |
| 1450 | **metaphor** | 6 | 997.16 | 9.59 | 🟢 medium — moderately distinctive | - |
| 1451 | **gratitude** | 6 | 997.16 | 9.59 | 🟢 medium — moderately distinctive | - |
| 1452 | **millstone** | 6 | 997.16 | 9.59 | 🟢 medium — moderately distinctive | millstone, millstones |
| 1453 | **inhabitant** | 6 | 997.16 | 9.59 | 🟢 medium — moderately distinctive | - |
| 1454 | **sunak** | 6 | 997.16 | 9.59 | 🟢 medium — moderately distinctive | - |
| 1455 | **grasping** | 6 | 997.16 | 9.59 | 🟢 medium — moderately distinctive | - |
| 1456 | **bodh** | 6 | 997.16 | 9.59 | 🟢 medium — moderately distinctive | - |
| 1457 | **gaya** | 6 | 997.16 | 9.59 | 🟢 medium — moderately distinctive | - |
| 1458 | **wandering** | 6 | 997.16 | 9.59 | 🟢 medium — moderately distinctive | wandering, wanderings |
| 1459 | **shepherd** | 6 | 997.16 | 9.59 | 🟢 medium — moderately distinctive | shepherd, shepherds |
| 1460 | **inexhaustible** | 6 | 997.16 | 9.59 | 🟢 medium — moderately distinctive | - |
| 1461 | **omniscience** | 6 | 997.16 | 9.59 | 🟢 medium — moderately distinctive | - |
| 1462 | **hermit** | 6 | 997.16 | 9.59 | 🟢 medium — moderately distinctive | hermit, hermits |
| 1463 | **ris** | 6 | 997.16 | 9.59 | 🟢 medium — moderately distinctive | - |
| 1464 | **mighty** | 6 | 997.16 | 9.59 | 🟢 medium — moderately distinctive | - |
| 1465 | **santideva** | 6 | 997.16 | 9.59 | 🟢 medium — moderately distinctive | - |
| 1466 | **heavenly** | 6 | 997.16 | 9.59 | 🟢 medium — moderately distinctive | - |
| 1467 | **meditative** | 6 | 997.16 | 9.59 | 🟢 medium — moderately distinctive | - |
| 1468 | **ruler** | 6 | 997.16 | 9.59 | 🟢 medium — moderately distinctive | - |
| 1469 | **bristling** | 6 | 997.16 | 9.59 | 🟢 medium — moderately distinctive | - |
| 1470 | **possessed** | 6 | 997.16 | 9.59 | 🟢 medium — moderately distinctive | - |
| 1471 | **mastery** | 6 | 997.16 | 9.59 | 🟢 medium — moderately distinctive | - |
| 1472 | **prosperous** | 6 | 997.16 | 9.59 | 🟢 medium — moderately distinctive | - |
| 1473 | **ambition** | 6 | 997.16 | 9.59 | 🟢 medium — moderately distinctive | ambition, ambitions |
| 1474 | **weeping** | 6 | 997.16 | 9.59 | 🟢 medium — moderately distinctive | - |
| 1475 | **flock** | 6 | 997.16 | 9.59 | 🟢 medium — moderately distinctive | flock, flocks |
| 1476 | **meditated** | 6 | 997.16 | 9.59 | 🟢 medium — moderately distinctive | - |
| 1477 | **emulate** | 6 | 997.16 | 9.59 | 🟢 medium — moderately distinctive | emulate, emulates |
| 1478 | **terror** | 6 | 997.16 | 9.59 | 🟢 medium — moderately distinctive | - |
| 1479 | **delight** | 6 | 997.16 | 9.59 | 🟢 medium — moderately distinctive | delight, delights |
| 1480 | **particle** | 6 | 997.16 | 9.59 | 🟢 medium — moderately distinctive | - |
| 1481 | **ogress** | 6 | 997.16 | 9.59 | 🟢 medium — moderately distinctive | ogress, ogresses |
| 1482 | **guest** | 6 | 997.16 | 9.59 | 🟢 medium — moderately distinctive | guest, guests |
| 1483 | **tale** | 6 | 997.16 | 9.59 | 🟢 medium — moderately distinctive | tale, tales |
| 1484 | **bonpo** | 6 | 997.16 | 9.59 | 🟢 medium — moderately distinctive | bonpo, bonpos |
| 1485 | **pith-instruction** | 6 | 997.16 | 9.59 | 🟢 medium — moderately distinctive | - |
| 1486 | **boatman** | 6 | 997.16 | 9.59 | 🟢 medium — moderately distinctive | - |
| 1487 | **prostrated** | 6 | 997.16 | 9.59 | 🟢 medium — moderately distinctive | - |
| 1488 | **swan** | 6 | 997.16 | 9.59 | 🟢 medium — moderately distinctive | swan, swans |
| 1489 | **unsurpassable** | 6 | 997.16 | 9.59 | 🟢 medium — moderately distinctive | - |
| 1490 | **jealous** | 6 | 997.16 | 9.59 | 🟢 medium — moderately distinctive | - |
| 1491 | **prayed** | 6 | 997.16 | 9.59 | 🟢 medium — moderately distinctive | - |
| 1492 | **ngokpa** | 6 | 997.16 | 9.59 | 🟢 medium — moderately distinctive | - |
| 1493 | **incomparable** | 6 | 997.16 | 9.59 | 🟢 medium — moderately distinctive | - |
| 1494 | **vajrapani** | 6 | 997.16 | 9.59 | 🟢 medium — moderately distinctive | - |
| 1495 | **atriya** | 6 | 997.16 | 9.59 | 🟢 medium — moderately distinctive | - |
| 1496 | **dharmaraksita** | 6 | 997.16 | 9.59 | 🟢 medium — moderately distinctive | - |
| 1497 | **hard-to-endure** | 6 | 997.16 | 9.59 | 🟢 medium — moderately distinctive | - |
| 1498 | **zangpo** | 6 | 997.16 | 9.59 | 🟢 medium — moderately distinctive | - |
| 1499 | **rejoicing** | 6 | 997.16 | 9.59 | 🟢 medium — moderately distinctive | - |
| 1500 | **emanate** | 6 | 997.16 | 9.59 | 🟢 medium — moderately distinctive | emanate, emanates |
| 1501 | **wrist** | 6 | 997.16 | 9.59 | 🟢 medium — moderately distinctive | wrist, wrists |
| 1502 | **sever** | 6 | 997.16 | 9.59 | 🟢 medium — moderately distinctive | sever, severs |
| 1503 | **takaya** | 6 | 997.16 | 9.59 | 🟢 medium — moderately distinctive | - |
| 1504 | **hrih** | 6 | 997.16 | 9.59 | 🟢 medium — moderately distinctive | - |
| 1505 | **altogether** | 7 | 995.56 | 8.206841 | 🟢 medium — moderately distinctive | - |
| 1506 | **genuine** | 7 | 995.56 | 8.206841 | 🟢 medium — moderately distinctive | - |
| 1507 | **meant** | 9 | 994.18 | 6.374259 | 🟢 medium — moderately distinctive | - |
| 1508 | **move** | 13 | 988.82 | 4.389129 | 🟢 medium — moderately distinctive | move, moves |
| 1509 | **careful** | 8 | 985.47 | 7.108229 | 🟢 medium — moderately distinctive | - |
| 1510 | **mark** | 11 | 984.08 | 5.162318 | 🟢 medium — moderately distinctive | mark, marks |
| 1511 | **except** | 9 | 982.18 | 6.297298 | 🟢 medium — moderately distinctive | - |
| 1512 | **avoided** | 7 | 981.27 | 8.089058 | 🟢 medium — moderately distinctive | - |
| 1513 | **fat** | 7 | 981.27 | 8.089058 | 🟢 medium — moderately distinctive | - |
| 1514 | **health** | 10 | 979.40 | 5.651553 | 🟢 medium — moderately distinctive | - |
| 1515 | **heavy** | 11 | 977.39 | 5.127227 | 🟢 medium — moderately distinctive | - |
| 1516 | **highly** | 9 | 976.51 | 6.260931 | 🟢 medium — moderately distinctive | - |
| 1517 | **aside** | 8 | 969.15 | 6.990446 | 🟢 medium — moderately distinctive | - |
| 1518 | **concentrated** | 8 | 969.15 | 6.990446 | 🟢 medium — moderately distinctive | - |
| 1519 | **looked** | 8 | 969.15 | 6.990446 | 🟢 medium — moderately distinctive | - |
| 1520 | **based** | 13 | 968.70 | 4.29983 | 🟢 medium — moderately distinctive | - |
| 1521 | **bright** | 7 | 968.49 | 7.983697 | 🟢 medium — moderately distinctive | - |
| 1522 | **accepted** | 10 | 963.35 | 5.558895 | 🟢 medium — moderately distinctive | - |
| 1523 | **garden** | 7 | 956.93 | 7.888387 | 🟢 medium — moderately distinctive | garden, gardens |
| 1524 | **deepest** | 6 | 955.32 | 9.18767 | 🟢 medium — moderately distinctive | - |
| 1525 | **abuse** | 6 | 955.32 | 9.18767 | 🟢 medium — moderately distinctive | - |
| 1526 | **inferior** | 6 | 955.32 | 9.18767 | 🟢 medium — moderately distinctive | inferior, inferiors |
| 1527 | **nail** | 6 | 955.32 | 9.18767 | 🟢 medium — moderately distinctive | nail, nails |
| 1528 | **hesitation** | 6 | 955.32 | 9.18767 | 🟢 medium — moderately distinctive | hesitation, hesitations |
| 1529 | **suppose** | 6 | 955.32 | 9.18767 | 🟢 medium — moderately distinctive | - |
| 1530 | **wise** | 6 | 955.32 | 9.18767 | 🟢 medium — moderately distinctive | - |
| 1531 | **thorn** | 6 | 955.32 | 9.18767 | 🟢 medium — moderately distinctive | - |
| 1532 | **mouse** | 6 | 955.32 | 9.18767 | 🟢 medium — moderately distinctive | mice, mouse |
| 1533 | **clarity** | 6 | 955.32 | 9.18767 | 🟢 medium — moderately distinctive | - |
| 1534 | **cloth** | 6 | 955.32 | 9.18767 | 🟢 medium — moderately distinctive | - |
| 1535 | **dissolution** | 6 | 955.32 | 9.18767 | 🟢 medium — moderately distinctive | - |
| 1536 | **correct** | 8 | 954.54 | 6.885085 | 🟢 medium — moderately distinctive | - |
| 1537 | **hill** | 8 | 954.54 | 6.885085 | 🟢 medium — moderately distinctive | hill, hills |
| 1538 | **finished** | 8 | 954.54 | 6.885085 | 🟢 medium — moderately distinctive | - |
| 1539 | **bell** | 8 | 954.54 | 6.885085 | 🟢 medium — moderately distinctive | bell, bells |
| 1540 | **size** | 9 | 953.26 | 6.111895 | 🟢 medium — moderately distinctive | - |
| 1541 | **connection** | 9 | 953.26 | 6.111895 | 🟢 medium — moderately distinctive | connection, connections |
| 1542 | **obtained** | 8 | 949.99 | 6.852295 | 🟢 medium — moderately distinctive | - |
| 1543 | **blow** | 7 | 946.38 | 7.801376 | 🟢 medium — moderately distinctive | blow, blows |
| 1544 | **divided** | 8 | 945.59 | 6.820546 | 🟢 medium — moderately distinctive | - |
| 1545 | **beneficial** | 8 | 945.59 | 6.820546 | 🟢 medium — moderately distinctive | - |
| 1546 | **south** | 12 | 942.16 | 4.53054 | 🟢 medium — moderately distinctive | - |
| 1547 | **led** | 11 | 939.74 | 4.929696 | 🟢 medium — moderately distinctive | - |
| 1548 | **former** | 10 | 939.06 | 5.418748 | 🟢 medium — moderately distinctive | - |
| 1549 | **upward** | 9 | 937.31 | 6.009616 | 🟢 medium — moderately distinctive | upward, upwards |
| 1550 | **trapped** | 7 | 936.67 | 7.721333 | 🟢 medium — moderately distinctive | - |
| 1551 | **worst** | 8 | 929.26 | 6.702763 | 🟢 medium — moderately distinctive | - |
| 1552 | **weight** | 8 | 929.26 | 6.702763 | 🟢 medium — moderately distinctive | weight, weights |
| 1553 | **execution** | 7 | 927.68 | 7.647225 | 🟢 medium — moderately distinctive | - |
| 1554 | **bean** | 7 | 927.68 | 7.647225 | 🟢 medium — moderately distinctive | bean, beans |
| 1555 | **worth** | 11 | 926.71 | 4.861332 | 🟢 medium — moderately distinctive | - |
| 1556 | **tried** | 8 | 925.46 | 6.675364 | 🟢 medium — moderately distinctive | - |
| 1557 | **belong** | 6 | 925.41 | 8.899988 | 🟢 medium — moderately distinctive | belong, belongs |
| 1558 | **describe** | 6 | 925.41 | 8.899988 | 🟢 medium — moderately distinctive | describe, describes |
| 1559 | **distant** | 6 | 925.41 | 8.899988 | 🟢 medium — moderately distinctive | - |
| 1560 | **queen** | 6 | 925.41 | 8.899988 | 🟢 medium — moderately distinctive | queen, queens |
| 1561 | **quest** | 6 | 925.41 | 8.899988 | 🟢 medium — moderately distinctive | - |
| 1562 | **crossed** | 6 | 925.41 | 8.899988 | 🟢 medium — moderately distinctive | - |
| 1563 | **wool** | 6 | 925.41 | 8.899988 | 🟢 medium — moderately distinctive | - |
| 1564 | **disillusionment** | 6 | 925.41 | 8.899988 | 🟢 medium — moderately distinctive | - |
| 1565 | **wound** | 6 | 925.41 | 8.899988 | 🟢 medium — moderately distinctive | wound, wounds |
| 1566 | **distinction** | 6 | 925.41 | 8.899988 | 🟢 medium — moderately distinctive | - |
| 1567 | **soup** | 6 | 925.41 | 8.899988 | 🟢 medium — moderately distinctive | - |
| 1568 | **com** | 6 | 925.41 | 8.899988 | 🟢 medium — moderately distinctive | - |
| 1569 | **save** | 8 | 921.77 | 6.648696 | 🟢 medium — moderately distinctive | - |
| 1570 | **including** | 13 | 921.39 | 4.089838 | 🟢 medium — moderately distinctive | - |
| 1571 | **attached** | 7 | 919.31 | 7.578232 | 🟢 medium — moderately distinctive | - |
| 1572 | **arrive** | 7 | 919.31 | 7.578232 | 🟢 medium — moderately distinctive | - |
| 1573 | **special** | 11 | 915.30 | 4.801485 | 🟢 medium — moderately distinctive | - |
| 1574 | **summit** | 8 | 914.65 | 6.597403 | 🟢 medium — moderately distinctive | - |
| 1575 | **written** | 8 | 914.65 | 6.597403 | 🟢 medium — moderately distinctive | - |
| 1576 | **bearing** | 7 | 911.48 | 7.513694 | 🟢 medium — moderately distinctive | - |
| 1577 | **accepting** | 7 | 911.48 | 7.513694 | 🟢 medium — moderately distinctive | - |
| 1578 | **air** | 9 | 911.42 | 5.843631 | 🟢 medium — moderately distinctive | air, airs |
| 1579 | **influence** | 8 | 907.89 | 6.548613 | 🟢 medium — moderately distinctive | influence, influences |
| 1580 | **direct** | 9 | 902.51 | 5.786473 | 🟢 medium — moderately distinctive | - |
| 1581 | **tip** | 6 | 902.21 | 8.676844 | 🟢 medium — moderately distinctive | tip, tips |
| 1582 | **somewhere** | 6 | 902.21 | 8.676844 | 🟢 medium — moderately distinctive | - |
| 1583 | **cooked** | 6 | 902.21 | 8.676844 | 🟢 medium — moderately distinctive | - |
| 1584 | **mirror** | 6 | 902.21 | 8.676844 | 🟢 medium — moderately distinctive | - |
| 1585 | **exhaust** | 6 | 902.21 | 8.676844 | 🟢 medium — moderately distinctive | exhaust, exhausts |
| 1586 | **against** | 15 | 890.75 | 3.426667 | 🟢 medium — moderately distinctive | - |
| 1587 | **message** | 7 | 890.63 | 7.341843 | 🟢 medium — moderately distinctive | message, messages |
| 1588 | **returned** | 8 | 886.52 | 6.394462 | 🟢 medium — moderately distinctive | - |
| 1589 | **understood** | 7 | 884.41 | 7.29055 | 🟢 medium — moderately distinctive | - |
| 1590 | **slaughter** | 7 | 884.41 | 7.29055 | 🟢 medium — moderately distinctive | - |
| 1591 | **guided** | 6 | 883.25 | 8.494523 | 🟢 medium — moderately distinctive | - |
| 1592 | **forget** | 6 | 883.25 | 8.494523 | 🟢 medium — moderately distinctive | - |
| 1593 | **forgotten** | 6 | 883.25 | 8.494523 | 🟢 medium — moderately distinctive | - |
| 1594 | **spoken** | 6 | 883.25 | 8.494523 | 🟢 medium — moderately distinctive | - |
| 1595 | **book** | 8 | 880.97 | 6.354457 | 🟢 medium — moderately distinctive | - |
| 1596 | **morning** | 10 | 879.80 | 5.076796 | 🟢 medium — moderately distinctive | - |
| 1597 | **mentioned** | 7 | 878.49 | 7.24176 | 🟢 medium — moderately distinctive | - |
| 1598 | **various** | 9 | 876.99 | 5.622843 | 🟢 medium — moderately distinctive | - |
| 1599 | **decided** | 10 | 873.29 | 5.039258 | 🟢 medium — moderately distinctive | - |
| 1600 | **meanwhile** | 8 | 873.05 | 6.297298 | 🟢 medium — moderately distinctive | - |
| 1601 | **gathering** | 7 | 872.85 | 7.19524 | 🟢 medium — moderately distinctive | - |
| 1602 | **session** | 9 | 868.40 | 5.567784 | 🟢 medium — moderately distinctive | session, sessions |
| 1603 | **achieved** | 8 | 868.01 | 6.260931 | 🟢 medium — moderately distinctive | - |
| 1604 | **downward** | 8 | 868.01 | 6.260931 | 🟢 medium — moderately distinctive | downward, downwards |
| 1605 | **invite** | 6 | 867.22 | 8.340372 | 🟢 medium — moderately distinctive | - |
| 1606 | **cure** | 6 | 867.22 | 8.340372 | 🟢 medium — moderately distinctive | - |
| 1607 | **belonging** | 6 | 867.22 | 8.340372 | 🟢 medium — moderately distinctive | belonging, belongings |
| 1608 | **busy** | 6 | 867.22 | 8.340372 | 🟢 medium — moderately distinctive | - |
| 1609 | **leather** | 6 | 867.22 | 8.340372 | 🟢 medium — moderately distinctive | - |
| 1610 | **prince** | 6 | 867.22 | 8.340372 | 🟢 medium — moderately distinctive | - |
| 1611 | **everybody** | 6 | 867.22 | 8.340372 | 🟢 medium — moderately distinctive | - |
| 1612 | **consulted** | 6 | 867.22 | 8.340372 | 🟢 medium — moderately distinctive | - |
| 1613 | **entered** | 9 | 861.59 | 5.524108 | 🟢 medium — moderately distinctive | - |
| 1614 | **certainly** | 8 | 860.77 | 6.208745 | 🟢 medium — moderately distinctive | - |
| 1615 | **increase** | 14 | 857.70 | 3.535181 | 🟢 medium — moderately distinctive | - |
| 1616 | **refused** | 8 | 856.15 | 6.175409 | 🟢 medium — moderately distinctive | - |
| 1617 | **further** | 13 | 855.09 | 3.795559 | 🟢 medium — moderately distinctive | further, furthers |
| 1618 | **art** | 6 | 853.34 | 8.206841 | 🟢 medium — moderately distinctive | art, arts |
| 1619 | **spite** | 6 | 853.34 | 8.206841 | 🟢 medium — moderately distinctive | - |
| 1620 | **throw** | 6 | 853.34 | 8.206841 | 🟢 medium — moderately distinctive | throw, throws |
| 1621 | **swiftly** | 6 | 853.34 | 8.206841 | 🟢 medium — moderately distinctive | - |
| 1622 | **arranged** | 7 | 852.58 | 7.028186 | 🟢 medium — moderately distinctive | - |
| 1623 | **closer** | 7 | 852.58 | 7.028186 | 🟢 medium — moderately distinctive | - |
| 1624 | **giant** | 7 | 848.00 | 6.990446 | 🟢 medium — moderately distinctive | - |
| 1625 | **achieve** | 8 | 847.34 | 6.111895 | 🟢 medium — moderately distinctive | - |
| 1626 | **resolve** | 8 | 843.14 | 6.08159 | 🟢 medium — moderately distinctive | - |
| 1627 | **placed** | 8 | 843.14 | 6.08159 | 🟢 medium — moderately distinctive | - |
| 1628 | **several** | 11 | 841.46 | 4.414165 | 🟢 medium — moderately distinctive | - |
| 1629 | **command** | 6 | 841.09 | 8.089058 | 🟢 medium — moderately distinctive | command, commands |
| 1630 | **defeat** | 6 | 841.09 | 8.089058 | 🟢 medium — moderately distinctive | - |
| 1631 | **supposed** | 6 | 841.09 | 8.089058 | 🟢 medium — moderately distinctive | - |
| 1632 | **rejecting** | 6 | 841.09 | 8.089058 | 🟢 medium — moderately distinctive | - |
| 1633 | **transfer** | 8 | 841.09 | 6.066775 | 🟢 medium — moderately distinctive | - |
| 1634 | **type** | 7 | 839.33 | 6.918987 | 🟢 medium — moderately distinctive | type, types |
| 1635 | **commitment** | 8 | 837.07 | 6.037787 | 🟢 medium — moderately distinctive | commitment, commitments |
| 1636 | **content** | 7 | 835.22 | 6.885085 | 🟢 medium — moderately distinctive | content, contents |
| 1637 | **total** | 14 | 831.88 | 3.428768 | 🟢 medium — moderately distinctive | - |
| 1638 | **shearing** | 5 | 831.24 | 9.593135 | 🟢 medium — moderately distinctive | - |
| 1639 | **marriage** | 5 | 831.24 | 9.593135 | 🟢 medium — moderately distinctive | - |
| 1640 | **incapable** | 5 | 831.24 | 9.593135 | 🟢 medium — moderately distinctive | - |
| 1641 | **neck** | 5 | 831.24 | 9.593135 | 🟢 medium — moderately distinctive | neck, necks |
| 1642 | **permanence** | 5 | 831.24 | 9.593135 | 🟢 medium — moderately distinctive | - |
| 1643 | **entourage** | 5 | 831.24 | 9.593135 | 🟢 medium — moderately distinctive | - |
| 1644 | **piled** | 5 | 831.24 | 9.593135 | 🟢 medium — moderately distinctive | - |
| 1645 | **lit** | 5 | 831.24 | 9.593135 | 🟢 medium — moderately distinctive | - |
| 1646 | **friendship** | 5 | 831.24 | 9.593135 | 🟢 medium — moderately distinctive | - |
| 1647 | **silk** | 5 | 831.24 | 9.593135 | 🟢 medium — moderately distinctive | silk, silks |
| 1648 | **dispel** | 5 | 831.24 | 9.593135 | 🟢 medium — moderately distinctive | dispel, dispels |
| 1649 | **boil** | 5 | 831.24 | 9.593135 | 🟢 medium — moderately distinctive | boil, boils |
| 1650 | **distress** | 5 | 831.24 | 9.593135 | 🟢 medium — moderately distinctive | - |
| 1651 | **sensation** | 5 | 831.24 | 9.593135 | 🟢 medium — moderately distinctive | sensation, sensations |
| 1652 | **stomach** | 5 | 831.24 | 9.593135 | 🟢 medium — moderately distinctive | stomach, stomachs |
| 1653 | **courage** | 5 | 831.24 | 9.593135 | 🟢 medium — moderately distinctive | - |
| 1654 | **dirty** | 5 | 831.24 | 9.593135 | 🟢 medium — moderately distinctive | - |
| 1655 | **wasted** | 5 | 831.24 | 9.593135 | 🟢 medium — moderately distinctive | - |
| 1656 | **snake** | 5 | 831.24 | 9.593135 | 🟢 medium — moderately distinctive | snake, snakes |
| 1657 | **sleeping** | 5 | 831.24 | 9.593135 | 🟢 medium — moderately distinctive | - |
| 1658 | **insult** | 5 | 831.24 | 9.593135 | 🟢 medium — moderately distinctive | insult, insults |
| 1659 | **succession** | 5 | 831.24 | 9.593135 | 🟢 medium — moderately distinctive | - |
| 1660 | **courageous** | 5 | 831.24 | 9.593135 | 🟢 medium — moderately distinctive | - |
| 1661 | **infallible** | 5 | 831.24 | 9.593135 | 🟢 medium — moderately distinctive | - |
| 1662 | **shining** | 5 | 831.24 | 9.593135 | 🟢 medium — moderately distinctive | - |
| 1663 | **prisoner** | 5 | 831.24 | 9.593135 | 🟢 medium — moderately distinctive | prisoner, prisoners |
| 1664 | **enlightened** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive | - |
| 1665 | **twofold** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive | - |
| 1666 | **misery** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive | miseries, misery |
| 1667 | **fame** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive | - |
| 1668 | **stain** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive | stain, stains |
| 1669 | **dumb** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive | - |
| 1670 | **proverb** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive | - |
| 1671 | **dy** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive | - |
| 1672 | **sack** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive | - |
| 1673 | **ananda** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive | - |
| 1674 | **machik** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive | - |
| 1675 | **spoil** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive | spoil, spoils |
| 1676 | **persevere** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive | - |
| 1677 | **beginningless** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive | - |
| 1678 | **crying** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive | - |
| 1679 | **reigned** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive | - |
| 1680 | **unchanging** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive | - |
| 1681 | **vairotsana** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive | - |
| 1682 | **circum** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive | - |
| 1683 | **manjusri** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive | - |
| 1684 | **radiant** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive | - |
| 1685 | **drom** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive | - |
| 1686 | **meditator** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive | meditator, meditators |
| 1687 | **laziness** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive | - |
| 1688 | **ty** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive | - |
| 1689 | **decadent** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive | - |
| 1690 | **wearing** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive | - |
| 1691 | **scholar** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive | - |
| 1692 | **gonpo** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive | - |
| 1693 | **chengawa** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive | - |
| 1694 | **recited** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive | - |
| 1695 | **threefold** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive | - |
| 1696 | **flame** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive | flame, flames |
| 1697 | **precipice** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive | precipice, precipices |
| 1698 | **ghost** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive | ghost, ghosts |
| 1699 | **immortality** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive | - |
| 1700 | **hollow** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive | - |
| 1701 | **deserted** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive | - |
| 1702 | **womb** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive | - |
| 1703 | **asleep** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive | - |
| 1704 | **stronghold** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive | - |
| 1705 | **conduce** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive | - |
| 1706 | **molten** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive | - |
| 1707 | **red-hot** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive | - |
| 1708 | **unimaginable** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive | - |
| 1709 | **lover** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive | lover, lovers |
| 1710 | **repa** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive | - |
| 1711 | **turquoise** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive | - |
| 1712 | **swallow** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive | - |
| 1713 | **delicious** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive | - |
| 1714 | **rage** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive | - |
| 1715 | **novice** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive | novice, novices |
| 1716 | **mustard** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive | - |
| 1717 | **confessing** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive | - |
| 1718 | **protuberance** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive | protuberance, protuberances |
| 1719 | **evil-doer** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive | evil-doer, evil-doers |
| 1720 | **anguish** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive | - |
| 1721 | **boy** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive | boy, boys |
| 1722 | **song** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive | song, songs |
| 1723 | **displease** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive | - |
| 1724 | **cousin** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive | cousin, cousins |
| 1725 | **circumambulating** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive | - |
| 1726 | **resting** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive | - |
| 1727 | **smile** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive | smile, smiles |
| 1728 | **trickery** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive | - |
| 1729 | **householder** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive | householder, householders |
| 1730 | **defiled** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive | - |
| 1731 | **proliferating** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive | - |
| 1732 | **sakya** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive | sakya, sakyas |
| 1733 | **ashamed** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive | - |
| 1734 | **heartfelt** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive | - |
| 1735 | **sandal** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive | - |
| 1736 | **disrespect** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive | - |
| 1737 | **homage** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive | - |
| 1738 | **incense** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive | - |
| 1739 | **jewelled** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive | - |
| 1740 | **perseverance** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive | - |
| 1741 | **canopy** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive | canopies, canopy |
| 1742 | **lakini** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive | lakini, lakinis |
| 1743 | **consort** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive | consort, consorts |
| 1744 | **cup** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive | - |
| 1745 | **spontaneous** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive | - |
| 1746 | **obstacle-maker** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive | - |
| 1747 | **dwelling** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive | dwelling, dwellings |
| 1748 | **abhidharma** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive | - |
| 1749 | **asariga** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive | - |
| 1750 | **asanga** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive | - |
| 1751 | **rotten** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive | - |
| 1752 | **medi** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive | - |
| 1753 | **pacify** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive | - |
| 1754 | **non-dharma** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive | - |
| 1755 | **conceit** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive | - |
| 1756 | **tendzin** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive | - |
| 1757 | **maintain** | 9 | 830.29 | 5.323438 | 🟢 medium — moderately distinctive | - |
| 1758 | **hole** | 6 | 830.14 | 7.983697 | 🟢 medium — moderately distinctive | - |
| 1759 | **dried** | 6 | 830.14 | 7.983697 | 🟢 medium — moderately distinctive | - |
| 1760 | **plenty** | 6 | 830.14 | 7.983697 | 🟢 medium — moderately distinctive | - |
| 1761 | **perceived** | 6 | 830.14 | 7.983697 | 🟢 medium — moderately distinctive | - |
| 1762 | **boat** | 6 | 830.14 | 7.983697 | 🟢 medium — moderately distinctive | - |
| 1763 | **town** | 6 | 820.23 | 7.888387 | 🟢 medium — moderately distinctive | town, towns |
| 1764 | **nonetheless** | 6 | 820.23 | 7.888387 | 🟢 medium — moderately distinctive | - |
| 1765 | **enjoyed** | 6 | 820.23 | 7.888387 | 🟢 medium — moderately distinctive | - |
| 1766 | **cease** | 6 | 820.23 | 7.888387 | 🟢 medium — moderately distinctive | - |
| 1767 | **vessel** | 7 | 820.04 | 6.759922 | 🟢 medium — moderately distinctive | vessel, vessels |
| 1768 | **worked** | 7 | 820.04 | 6.759922 | 🟢 medium — moderately distinctive | - |
| 1769 | **course** | 8 | 818.56 | 5.904256 | 🟢 medium — moderately distinctive | - |
| 1770 | **visit** | 8 | 818.56 | 5.904256 | 🟢 medium — moderately distinctive | - |
| 1771 | **lot** | 8 | 815.13 | 5.879563 | 🟢 medium — moderately distinctive | lot, lots |
| 1772 | **indian** | 7 | 813.10 | 6.702763 | 🟢 medium — moderately distinctive | - |
| 1773 | **sweet** | 7 | 813.10 | 6.702763 | 🟢 medium — moderately distinctive | - |
| 1774 | **repay** | 7 | 813.10 | 6.702763 | 🟢 medium — moderately distinctive | - |
| 1775 | **mix** | 6 | 811.18 | 7.801376 | 🟢 medium — moderately distinctive | mix, mixes |
| 1776 | **rush** | 6 | 811.18 | 7.801376 | 🟢 medium — moderately distinctive | rush, rushes |
| 1777 | **seventh** | 6 | 811.18 | 7.801376 | 🟢 medium — moderately distinctive | - |
| 1778 | **guard** | 6 | 811.18 | 7.801376 | 🟢 medium — moderately distinctive | guard, guards |
| 1779 | **passing** | 6 | 811.18 | 7.801376 | 🟢 medium — moderately distinctive | - |
| 1780 | **working** | 9 | 807.97 | 5.180337 | 🟢 medium — moderately distinctive | - |
| 1781 | **ordered** | 7 | 806.54 | 6.648696 | 🟢 medium — moderately distinctive | - |
| 1782 | **causing** | 7 | 806.54 | 6.648696 | 🟢 medium — moderately distinctive | - |
| 1783 | **asking** | 7 | 803.39 | 6.622721 | 🟢 medium — moderately distinctive | - |
| 1784 | **circle** | 6 | 802.86 | 7.721333 | 🟢 medium — moderately distinctive | - |
| 1785 | **serving** | 6 | 802.86 | 7.721333 | 🟢 medium — moderately distinctive | - |
| 1786 | **ship** | 8 | 802.23 | 5.786473 | 🟢 medium — moderately distinctive | ship, ships |
| 1787 | **compared** | 12 | 800.33 | 3.848531 | 🟢 medium — moderately distinctive | - |
| 1788 | **carrying** | 7 | 800.32 | 6.597403 | 🟢 medium — moderately distinctive | - |
| 1789 | **waste** | 7 | 797.33 | 6.57271 | 🟢 medium — moderately distinctive | waste, wastes |
| 1790 | **control** | 10 | 796.47 | 4.595923 | 🟢 medium — moderately distinctive | - |
| 1791 | **horn** | 5 | 796.10 | 9.18767 | 🟢 medium — moderately distinctive | - |
| 1792 | **illusory** | 5 | 796.10 | 9.18767 | 🟢 medium — moderately distinctive | - |
| 1793 | **emperor** | 5 | 796.10 | 9.18767 | 🟢 medium — moderately distinctive | emperor, emperors |
| 1794 | **incalculable** | 5 | 796.10 | 9.18767 | 🟢 medium — moderately distinctive | - |
| 1795 | **wrapped** | 5 | 796.10 | 9.18767 | 🟢 medium — moderately distinctive | - |
| 1796 | **religious** | 5 | 796.10 | 9.18767 | 🟢 medium — moderately distinctive | - |
| 1797 | **corps** | 5 | 796.10 | 9.18767 | 🟢 medium — moderately distinctive | - |
| 1798 | **terribly** | 5 | 796.10 | 9.18767 | 🟢 medium — moderately distinctive | - |
| 1799 | **openly** | 5 | 796.10 | 9.18767 | 🟢 medium — moderately distinctive | - |
| 1800 | **odd** | 5 | 796.10 | 9.18767 | 🟢 medium — moderately distinctive | odd, odds |
| 1801 | **hail** | 5 | 796.10 | 9.18767 | 🟢 medium — moderately distinctive | - |
| 1802 | **captain** | 5 | 796.10 | 9.18767 | 🟢 medium — moderately distinctive | - |
| 1803 | **perfume** | 5 | 796.10 | 9.18767 | 🟢 medium — moderately distinctive | perfume, perfumes |
| 1804 | **faithfully** | 5 | 796.10 | 9.18767 | 🟢 medium — moderately distinctive | - |
| 1805 | **thirteen** | 5 | 796.10 | 9.18767 | 🟢 medium — moderately distinctive | - |
| 1806 | **emanating** | 5 | 796.10 | 9.18767 | 🟢 medium — moderately distinctive | - |
| 1807 | **studied** | 6 | 795.15 | 7.647225 | 🟢 medium — moderately distinctive | - |
| 1808 | **dangerous** | 6 | 795.15 | 7.647225 | 🟢 medium — moderately distinctive | - |
| 1809 | **generally** | 8 | 793.28 | 5.721934 | 🟢 medium — moderately distinctive | - |
| 1810 | **general** | 11 | 789.19 | 4.139953 | 🟢 medium — moderately distinctive | - |
| 1811 | **winter** | 8 | 789.01 | 5.691163 | 🟢 medium — moderately distinctive | - |
| 1812 | **constitute** | 6 | 787.98 | 7.578232 | 🟢 medium — moderately distinctive | constitute, constitutes |
| 1813 | **fighting** | 6 | 787.98 | 7.578232 | 🟢 medium — moderately distinctive | - |
| 1814 | **rank** | 6 | 787.98 | 7.578232 | 🟢 medium — moderately distinctive | rank, ranks |
| 1815 | **opening** | 8 | 786.24 | 5.671162 | 🟢 medium — moderately distinctive | opening, openings |
| 1816 | **calling** | 7 | 783.37 | 6.457641 | 🟢 medium — moderately distinctive | - |
| 1817 | **third** | 10 | 781.87 | 4.511731 | 🟢 medium — moderately distinctive | third, thirds |
| 1818 | **threatening** | 6 | 781.27 | 7.513694 | 🟢 medium — moderately distinctive | - |
| 1819 | **linked** | 7 | 778.21 | 6.415081 | 🟢 medium — moderately distinctive | - |
| 1820 | **concentrate** | 7 | 778.21 | 6.415081 | 🟢 medium — moderately distinctive | - |
| 1821 | **cattle** | 7 | 775.70 | 6.394462 | 🟢 medium — moderately distinctive | - |
| 1822 | **definitely** | 6 | 774.96 | 7.453069 | 🟢 medium — moderately distinctive | - |
| 1823 | **mine** | 8 | 771.91 | 5.567784 | 🟢 medium — moderately distinctive | - |
| 1824 | **everywhere** | 5 | 771.18 | 8.899988 | 🟢 medium — moderately distinctive | - |
| 1825 | **drag** | 5 | 771.18 | 8.899988 | 🟢 medium — moderately distinctive | drag, drags |
| 1826 | **missing** | 5 | 771.18 | 8.899988 | 🟢 medium — moderately distinctive | - |
| 1827 | **meaningless** | 5 | 771.18 | 8.899988 | 🟢 medium — moderately distinctive | - |
| 1828 | **foolish** | 5 | 771.18 | 8.899988 | 🟢 medium — moderately distinctive | - |
| 1829 | **certainty** | 5 | 771.18 | 8.899988 | 🟢 medium — moderately distinctive | - |
| 1830 | **pillar** | 5 | 771.18 | 8.899988 | 🟢 medium — moderately distinctive | pillar, pillars |
| 1831 | **beaten** | 5 | 771.18 | 8.899988 | 🟢 medium — moderately distinctive | - |
| 1832 | **lump** | 5 | 771.18 | 8.899988 | 🟢 medium — moderately distinctive | lump, lumps |
| 1833 | **painful** | 5 | 771.18 | 8.899988 | 🟢 medium — moderately distinctive | - |
| 1834 | **undergoing** | 5 | 771.18 | 8.899988 | 🟢 medium — moderately distinctive | - |
| 1835 | **boot** | 5 | 771.18 | 8.899988 | 🟢 medium — moderately distinctive | - |
| 1836 | **afraid** | 5 | 771.18 | 8.899988 | 🟢 medium — moderately distinctive | - |
| 1837 | **exceptional** | 6 | 769.02 | 7.395911 | 🟢 medium — moderately distinctive | - |
| 1838 | **included** | 9 | 765.96 | 4.911004 | 🟢 medium — moderately distinctive | - |
| 1839 | **choose** | 6 | 763.40 | 7.341843 | 🟢 medium — moderately distinctive | - |
| 1840 | **breaking** | 6 | 763.40 | 7.341843 | 🟢 medium — moderately distinctive | - |
| 1841 | **watch** | 6 | 763.40 | 7.341843 | 🟢 medium — moderately distinctive | - |
| 1842 | **creating** | 6 | 758.06 | 7.29055 | 🟢 medium — moderately distinctive | - |
| 1843 | **west** | 11 | 757.66 | 3.974548 | 🟢 medium — moderately distinctive | - |
| 1844 | **provide** | 9 | 756.85 | 4.85256 | 🟢 medium — moderately distinctive | provide, provides |
| 1845 | **focus** | 7 | 755.25 | 6.225839 | 🟢 medium — moderately distinctive | - |
| 1846 | **completed** | 10 | 753.63 | 4.348746 | 🟢 medium — moderately distinctive | - |
| 1847 | **wave** | 6 | 752.99 | 7.24176 | 🟢 medium — moderately distinctive | wave, waves |
| 1848 | **tied** | 6 | 752.99 | 7.24176 | 🟢 medium — moderately distinctive | - |
| 1849 | **city** | 8 | 752.32 | 5.42647 | 🟢 medium — moderately distinctive | cities, city |
| 1850 | **listened** | 5 | 751.84 | 8.676844 | 🟢 medium — moderately distinctive | - |
| 1851 | **consume** | 5 | 751.84 | 8.676844 | 🟢 medium — moderately distinctive | - |
| 1852 | **dragged** | 5 | 751.84 | 8.676844 | 🟢 medium — moderately distinctive | - |
| 1853 | **homeland** | 5 | 751.84 | 8.676844 | 🟢 medium — moderately distinctive | - |
| 1854 | **rocky** | 5 | 751.84 | 8.676844 | 🟢 medium — moderately distinctive | - |
| 1855 | **contaminated** | 5 | 751.84 | 8.676844 | 🟢 medium — moderately distinctive | - |
| 1856 | **sword** | 5 | 751.84 | 8.676844 | 🟢 medium — moderately distinctive | - |
| 1857 | **ala** | 5 | 751.84 | 8.676844 | 🟢 medium — moderately distinctive | ala, alas |
| 1858 | **devoted** | 5 | 751.84 | 8.676844 | 🟢 medium — moderately distinctive | - |
| 1859 | **generous** | 5 | 751.84 | 8.676844 | 🟢 medium — moderately distinctive | - |
| 1860 | **staying** | 5 | 751.84 | 8.676844 | 🟢 medium — moderately distinctive | - |
| 1861 | **application** | 7 | 749.13 | 6.175409 | 🟢 medium — moderately distinctive | - |
| 1862 | **setting** | 7 | 749.13 | 6.175409 | 🟢 medium — moderately distinctive | - |
| 1863 | **completing** | 6 | 748.15 | 7.19524 | 🟢 medium — moderately distinctive | - |
| 1864 | **fourth** | 9 | 744.41 | 4.772854 | 🟢 medium — moderately distinctive | - |
| 1865 | **visible** | 6 | 743.53 | 7.150788 | 🟢 medium — moderately distinctive | - |
| 1866 | **ready** | 7 | 739.57 | 6.096628 | 🟢 medium — moderately distinctive | - |
| 1867 | **firm** | 10 | 738.32 | 4.260416 | 🟢 medium — moderately distinctive | - |
| 1868 | **problem** | 8 | 738.03 | 5.323438 | 🟢 medium — moderately distinctive | problem, problems |
| 1869 | **confused** | 5 | 736.04 | 8.494523 | 🟢 medium — moderately distinctive | - |
| 1870 | **overcome** | 5 | 736.04 | 8.494523 | 🟢 medium — moderately distinctive | - |
| 1871 | **throwing** | 5 | 736.04 | 8.494523 | 🟢 medium — moderately distinctive | - |
| 1872 | **vicious** | 5 | 736.04 | 8.494523 | 🟢 medium — moderately distinctive | - |
| 1873 | **surpass** | 5 | 736.04 | 8.494523 | 🟢 medium — moderately distinctive | surpass, surpasses |
| 1874 | **wanting** | 5 | 736.04 | 8.494523 | 🟢 medium — moderately distinctive | - |
| 1875 | **grave** | 5 | 736.04 | 8.494523 | 🟢 medium — moderately distinctive | - |
| 1876 | **illustrated** | 5 | 736.04 | 8.494523 | 🟢 medium — moderately distinctive | - |
| 1877 | **surely** | 5 | 736.04 | 8.494523 | 🟢 medium — moderately distinctive | - |
| 1878 | **undesirable** | 5 | 736.04 | 8.494523 | 🟢 medium — moderately distinctive | - |
| 1879 | **temper** | 5 | 736.04 | 8.494523 | 🟢 medium — moderately distinctive | - |
| 1880 | **lowest** | 7 | 735.95 | 6.066775 | 🟢 medium — moderately distinctive | - |
| 1881 | **telling** | 6 | 734.86 | 7.067407 | 🟢 medium — moderately distinctive | - |
| 1882 | **emerge** | 6 | 734.86 | 7.067407 | 🟢 medium — moderately distinctive | emerge, emerges |
| 1883 | **stability** | 8 | 733.27 | 5.28907 | 🟢 medium — moderately distinctive | - |
| 1884 | **attacked** | 6 | 730.78 | 7.028186 | 🟢 medium — moderately distinctive | - |
| 1885 | **attack** | 7 | 729.02 | 6.009616 | 🟢 medium — moderately distinctive | attack, attacks |
| 1886 | **appropriate** | 7 | 729.02 | 6.009616 | 🟢 medium — moderately distinctive | - |
| 1887 | **helping** | 6 | 726.86 | 6.990446 | 🟢 medium — moderately distinctive | - |
| 1888 | **pressing** | 6 | 726.86 | 6.990446 | 🟢 medium — moderately distinctive | - |
| 1889 | **potential** | 8 | 725.08 | 5.230037 | 🟢 medium — moderately distinctive | - |
| 1890 | **abandoned** | 6 | 723.08 | 6.954078 | 🟢 medium — moderately distinctive | - |
| 1891 | **treasury** | 9 | 722.73 | 4.633793 | 🟢 medium — moderately distinctive | - |
| 1892 | **guidance** | 5 | 722.69 | 8.340372 | 🟢 medium — moderately distinctive | - |
| 1893 | **beneath** | 5 | 722.69 | 8.340372 | 🟢 medium — moderately distinctive | - |
| 1894 | **smoke** | 5 | 722.69 | 8.340372 | 🟢 medium — moderately distinctive | - |
| 1895 | **solely** | 5 | 722.69 | 8.340372 | 🟢 medium — moderately distinctive | - |
| 1896 | **logic** | 5 | 722.69 | 8.340372 | 🟢 medium — moderately distinctive | - |
| 1897 | **exchanging** | 5 | 722.69 | 8.340372 | 🟢 medium — moderately distinctive | - |
| 1898 | **maker** | 7 | 719.31 | 5.929574 | 🟢 medium — moderately distinctive | - |
| 1899 | **principal** | 7 | 717.76 | 5.916835 | 🟢 medium — moderately distinctive | - |
| 1900 | **forced** | 7 | 716.24 | 5.904256 | 🟢 medium — moderately distinctive | - |
| 1901 | **crucial** | 6 | 715.90 | 6.885085 | 🟢 medium — moderately distinctive | - |
| 1902 | **par** | 6 | 715.90 | 6.885085 | 🟢 medium — moderately distinctive | - |
| 1903 | **fight** | 6 | 712.49 | 6.852295 | 🟢 medium — moderately distinctive | fight, fights |
| 1904 | **succeed** | 6 | 712.49 | 6.852295 | 🟢 medium — moderately distinctive | succeed, succeeds |
| 1905 | **destroying** | 5 | 711.12 | 8.206841 | 🟢 medium — moderately distinctive | - |
| 1906 | **beer** | 5 | 711.12 | 8.206841 | 🟢 medium — moderately distinctive | - |
| 1907 | **rite** | 5 | 711.12 | 8.206841 | 🟢 medium — moderately distinctive | - |
| 1908 | **aggression** | 5 | 711.12 | 8.206841 | 🟢 medium — moderately distinctive | - |
| 1909 | **arose** | 5 | 711.12 | 8.206841 | 🟢 medium — moderately distinctive | - |
| 1910 | **common** | 11 | 710.95 | 3.729504 | 🟢 medium — moderately distinctive | - |
| 1911 | **low** | 9 | 708.61 | 4.543279 | 🟢 medium — moderately distinctive | - |
| 1912 | **hit** | 8 | 706.90 | 5.098897 | 🟢 medium — moderately distinctive | hit, hits |
| 1913 | **steady** | 7 | 704.68 | 5.808946 | 🟢 medium — moderately distinctive | - |
| 1914 | **answer** | 6 | 702.89 | 6.759922 | 🟢 medium — moderately distinctive | answer, answers |
| 1915 | **reading** | 5 | 700.91 | 8.089058 | 🟢 medium — moderately distinctive | - |
| 1916 | **touched** | 5 | 700.91 | 8.089058 | 🟢 medium — moderately distinctive | - |
| 1917 | **slightly** | 8 | 697.18 | 5.028787 | 🟢 medium — moderately distinctive | - |
| 1918 | **sovereign** | 5 | 691.78 | 7.983697 | 🟢 medium — moderately distinctive | - |
| 1919 | **sooner** | 5 | 691.78 | 7.983697 | 🟢 medium — moderately distinctive | - |
| 1920 | **accompanied** | 5 | 691.78 | 7.983697 | 🟢 medium — moderately distinctive | - |
| 1921 | **measure** | 7 | 689.17 | 5.681112 | 🟢 medium — moderately distinctive | measure, measures |
| 1922 | **plant** | 8 | 688.10 | 4.963272 | 🟢 medium — moderately distinctive | plant, plants |
| 1923 | **becoming** | 6 | 685.99 | 6.597403 | 🟢 medium — moderately distinctive | - |
| 1924 | **below** | 9 | 684.14 | 4.386385 | 🟢 medium — moderately distinctive | - |
| 1925 | **host** | 5 | 683.52 | 7.888387 | 🟢 medium — moderately distinctive | host, hosts |
| 1926 | **tremendous** | 5 | 683.52 | 7.888387 | 🟢 medium — moderately distinctive | - |
| 1927 | **expert** | 5 | 683.52 | 7.888387 | 🟢 medium — moderately distinctive | - |
| 1928 | **presented** | 6 | 676.08 | 6.502093 | 🟢 medium — moderately distinctive | - |
| 1929 | **accordingly** | 5 | 675.98 | 7.801376 | 🟢 medium — moderately distinctive | - |
| 1930 | **criticized** | 5 | 675.98 | 7.801376 | 🟢 medium — moderately distinctive | - |
| 1931 | **wait** | 6 | 671.46 | 6.457641 | 🟢 medium — moderately distinctive | - |
| 1932 | **hardly** | 5 | 669.05 | 7.721333 | 🟢 medium — moderately distinctive | - |
| 1933 | **question** | 7 | 668.07 | 5.507159 | 🟢 medium — moderately distinctive | question, questions |
| 1934 | **mar** | 6 | 667.03 | 6.415081 | 🟢 medium — moderately distinctive | - |
| 1935 | **business** | 10 | 666.94 | 3.848531 | 🟢 medium — moderately distinctive | - |
| 1936 | **discouragement** | 4 | 664.99 | 9.593135 | 🟢 medium — moderately distinctive | - |
| 1937 | **utter** | 4 | 664.99 | 9.593135 | 🟢 medium — moderately distinctive | - |
| 1938 | **nepal** | 4 | 664.99 | 9.593135 | 🟢 medium — moderately distinctive | - |
| 1939 | **youth** | 4 | 664.99 | 9.593135 | 🟢 medium — moderately distinctive | - |
| 1940 | **render** | 4 | 664.99 | 9.593135 | 🟢 medium — moderately distinctive | render, renders |
| 1941 | **breast** | 4 | 664.99 | 9.593135 | 🟢 medium — moderately distinctive | breast, breasts |
| 1942 | **dissolving** | 4 | 664.99 | 9.593135 | 🟢 medium — moderately distinctive | - |
| 1943 | **gently** | 4 | 664.99 | 9.593135 | 🟢 medium — moderately distinctive | - |
| 1944 | **intrinsic** | 4 | 664.99 | 9.593135 | 🟢 medium — moderately distinctive | - |
| 1945 | **famine** | 4 | 664.99 | 9.593135 | 🟢 medium — moderately distinctive | - |
| 1946 | **landscape** | 4 | 664.99 | 9.593135 | 🟢 medium — moderately distinctive | landscape, landscapes |
| 1947 | **cheat** | 4 | 664.99 | 9.593135 | 🟢 medium — moderately distinctive | cheat, cheats |
| 1948 | **suck** | 4 | 664.99 | 9.593135 | 🟢 medium — moderately distinctive | - |
| 1949 | **stricken** | 4 | 664.99 | 9.593135 | 🟢 medium — moderately distinctive | - |
| 1950 | **wrinkle** | 4 | 664.99 | 9.593135 | 🟢 medium — moderately distinctive | - |
| 1951 | **pinch** | 4 | 664.99 | 9.593135 | 🟢 medium — moderately distinctive | - |
| 1952 | **weary** | 4 | 664.99 | 9.593135 | 🟢 medium — moderately distinctive | - |
| 1953 | **multiply** | 4 | 664.99 | 9.593135 | 🟢 medium — moderately distinctive | multiplies, multiply |
| 1954 | **ati** | 4 | 664.99 | 9.593135 | 🟢 medium — moderately distinctive | - |
| 1955 | **spit** | 4 | 664.99 | 9.593135 | 🟢 medium — moderately distinctive | - |
| 1956 | **proud** | 4 | 664.99 | 9.593135 | 🟢 medium — moderately distinctive | - |
| 1957 | **praise** | 4 | 664.99 | 9.593135 | 🟢 medium — moderately distinctive | - |
| 1958 | **sandalwood** | 4 | 664.99 | 9.593135 | 🟢 medium — moderately distinctive | - |
| 1959 | **mentality** | 4 | 664.99 | 9.593135 | 🟢 medium — moderately distinctive | - |
| 1960 | **sweep** | 4 | 664.99 | 9.593135 | 🟢 medium — moderately distinctive | - |
| 1961 | **inherited** | 4 | 664.99 | 9.593135 | 🟢 medium — moderately distinctive | - |
| 1962 | **whack** | 4 | 664.99 | 9.593135 | 🟢 medium — moderately distinctive | whack, whacks |
| 1963 | **dawn** | 4 | 664.99 | 9.593135 | 🟢 medium — moderately distinctive | - |
| 1964 | **rubbing** | 4 | 664.99 | 9.593135 | 🟢 medium — moderately distinctive | - |
| 1965 | **wagon** | 4 | 664.99 | 9.593135 | 🟢 medium — moderately distinctive | wagon, wagons |
| 1966 | **ear** | 4 | 664.99 | 9.593135 | 🟢 medium — moderately distinctive | ear, ears |
| 1967 | **radial** | 4 | 664.99 | 9.593135 | 🟢 medium — moderately distinctive | - |
| 1968 | **pleasing** | 4 | 664.99 | 9.593135 | 🟢 medium — moderately distinctive | - |
| 1969 | **symbolize** | 4 | 664.99 | 9.593135 | 🟢 medium — moderately distinctive | - |
| 1970 | **hindu** | 4 | 664.99 | 9.593135 | 🟢 medium — moderately distinctive | - |
| 1971 | **defect** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | - |
| 1972 | **conceptualization** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | - |
| 1973 | **circumstantial** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | - |
| 1974 | **ence** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | ence, ences |
| 1975 | **embody** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | embodies, embody |
| 1976 | **assimilate** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | - |
| 1977 | **poisoned** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | - |
| 1978 | **blade** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | blade, blades |
| 1979 | **stag** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | stag, stags |
| 1980 | **bee** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | bee, bees |
| 1981 | **drown** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | - |
| 1982 | **pointless** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | - |
| 1983 | **srona** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | - |
| 1984 | **grasp** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | - |
| 1985 | **diligent** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | - |
| 1986 | **diseas** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | - |
| 1987 | **trap** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | trap, traps |
| 1988 | **parasol** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | parasol, parasols |
| 1989 | **entrusted** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | - |
| 1990 | **invocation** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | invocation, invocations |
| 1991 | **samye** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | - |
| 1992 | **prostitute** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | prostitute, prostitutes |
| 1993 | **con** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | - |
| 1994 | **joyous** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | - |
| 1995 | **exclaimed** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | - |
| 1996 | **sion** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | sion, sions |
| 1997 | **infatuation** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | - |
| 1998 | **procrastination** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | - |
| 1999 | **renounced** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | - |
| 2000 | **unshakeable** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | - |
| 2001 | **univers** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | - |
| 2002 | **inanimate** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | - |
| 2003 | **gyaltsen** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | - |
| 2004 | **fleeting** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | - |
| 2005 | **footstep** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | - |
| 2006 | **evaporate** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | evaporate, evaporates |
| 2007 | **footprint** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | footprint, footprints |
| 2008 | **gaze** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | - |
| 2009 | **isvara** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | - |
| 2010 | **thirty-seven** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | - |
| 2011 | **gange** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | - |
| 2012 | **miraculously** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | - |
| 2013 | **clenched** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | - |
| 2014 | **pillow** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | - |
| 2015 | **nest** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | nest, nests |
| 2016 | **asura** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | - |
| 2017 | **laugh** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | laugh, laughs |
| 2018 | **uncle** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | - |
| 2019 | **robber** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | - |
| 2020 | **sadness** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | - |
| 2021 | **earnestly** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | - |
| 2022 | **gesh** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | - |
| 2023 | **sang** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | - |
| 2024 | **potowa** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | - |
| 2025 | **armour** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | - |
| 2026 | **impervious** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | - |
| 2027 | **revered** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | - |
| 2028 | **bent** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | - |
| 2029 | **ember** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | - |
| 2030 | **joyful** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | - |
| 2031 | **grabbed** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | - |
| 2032 | **crawling** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | - |
| 2033 | **thicket** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | thicket, thickets |
| 2034 | **chastity** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | - |
| 2035 | **embrace** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | embrace, embraces |
| 2036 | **blister** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | blister, blisters |
| 2037 | **gyalpo** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | - |
| 2038 | **yeshe** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | - |
| 2039 | **tsogyal** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | - |
| 2040 | **selve** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | - |
| 2041 | **kasyapa** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | - |
| 2042 | **shang** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | - |
| 2043 | **chaff** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | - |
| 2044 | **heir** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | heir, heirs |
| 2045 | **shine** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | shine, shines |
| 2046 | **ignorant** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | - |
| 2047 | **tortured** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | - |
| 2048 | **enjoyment** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | - |
| 2049 | **terrified** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | - |
| 2050 | **limitless** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | - |
| 2051 | **adversary** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | - |
| 2052 | **wolve** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | - |
| 2053 | **knot** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | knot, knots |
| 2054 | **frustrating** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | - |
| 2055 | **grateful** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | - |
| 2056 | **smiling** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | - |
| 2057 | **transmigration** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | - |
| 2058 | **obeyed** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | - |
| 2059 | **wouldn** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | - |
| 2060 | **innocent** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | innocent, innocents |
| 2061 | **ogre** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | ogre, ogres |
| 2062 | **transgression** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | transgression, transgressions |
| 2063 | **amassed** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | - |
| 2064 | **spearman** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | - |
| 2065 | **purnakasyapa** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | - |
| 2066 | **ravati** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | - |
| 2067 | **curd** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | - |
| 2068 | **pebble** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | pebble, pebbles |
| 2069 | **unerringly** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | - |
| 2070 | **emulating** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | - |
| 2071 | **versed** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | - |
| 2072 | **characteristic** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | - |
| 2073 | **ingratitude** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | - |
| 2074 | **aversion** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | - |
| 2075 | **laughter** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | - |
| 2076 | **clay** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | - |
| 2077 | **adept** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | adept, adepts |
| 2078 | **hip** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | - |
| 2079 | **empow** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | - |
| 2080 | **adamantine** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | - |
| 2081 | **conferred** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | - |
| 2082 | **cleanse** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | - |
| 2083 | **eagerness** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | - |
| 2084 | **unfailing** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | - |
| 2085 | **dough** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | - |
| 2086 | **befall** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | - |
| 2087 | **adversity** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | - |
| 2088 | **diligently** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | - |
| 2089 | **perna** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | - |
| 2090 | **subjugate** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | - |
| 2091 | **nostril** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | - |
| 2092 | **fortress** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | - |
| 2093 | **supernatural** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | - |
| 2094 | **khampa** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | - |
| 2095 | **mafijusri** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | - |
| 2096 | **beginner** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | beginner, beginners |
| 2097 | **awaken** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | awaken, awakens |
| 2098 | **kar** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | - |
| 2099 | **maitriyogi** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | - |
| 2100 | **rohita** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | - |
| 2101 | **marici** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | - |
| 2102 | **passion** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | - |
| 2103 | **rinchen** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | - |
| 2104 | **ego-clinging** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | - |
| 2105 | **cleansed** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | - |
| 2106 | **imagining** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | - |
| 2107 | **conceptual** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | - |
| 2108 | **innate** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | - |
| 2109 | **lady** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | - |
| 2110 | **perceiving** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | - |
| 2111 | **worn** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | - |
| 2112 | **speck** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | speck, specks |
| 2113 | **damchen** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | - |
| 2114 | **curved** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | - |
| 2115 | **nirmar** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | - |
| 2116 | **emaho** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | - |
| 2117 | **effortless** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | - |
| 2118 | **pisaka** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | - |
| 2119 | **vajrapar** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | - |
| 2120 | **adhicitta** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | - |
| 2121 | **tulkus** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | - |
| 2122 | **dzogchen** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | - |
| 2123 | **dodrup** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | - |
| 2124 | **add** | 7 | 664.06 | 5.474098 | 🟢 medium — moderately distinctive | - |
| 2125 | **join** | 6 | 662.79 | 6.374259 | 🟢 medium — moderately distinctive | - |
| 2126 | **explanation** | 5 | 662.63 | 7.647225 | 🟢 medium — moderately distinctive | explanation, explanations |
| 2127 | **similarly** | 5 | 662.63 | 7.647225 | 🟢 medium — moderately distinctive | - |
| 2128 | **enormous** | 5 | 662.63 | 7.647225 | 🟢 medium — moderately distinctive | - |
| 2129 | **victory** | 5 | 662.63 | 7.647225 | 🟢 medium — moderately distinctive | - |
| 2130 | **won** | 6 | 658.71 | 6.335039 | 🟢 medium — moderately distinctive | - |
| 2131 | **floor** | 6 | 656.73 | 6.31599 | 🟢 medium — moderately distinctive | - |
| 2132 | **consisting** | 5 | 656.65 | 7.578232 | 🟢 medium — moderately distinctive | - |
| 2133 | **lasting** | 5 | 656.65 | 7.578232 | 🟢 medium — moderately distinctive | - |
| 2134 | **watching** | 5 | 656.65 | 7.578232 | 🟢 medium — moderately distinctive | - |
| 2135 | **directed** | 5 | 656.65 | 7.578232 | 🟢 medium — moderately distinctive | - |
| 2136 | **suitable** | 5 | 651.05 | 7.513694 | 🟢 medium — moderately distinctive | - |
| 2137 | **spoke** | 5 | 651.05 | 7.513694 | 🟢 medium — moderately distinctive | spoke, spokes |
| 2138 | **ensure** | 6 | 651.00 | 6.260931 | 🟢 medium — moderately distinctive | ensure, ensures |
| 2139 | **fresh** | 6 | 647.36 | 6.225839 | 🟢 medium — moderately distinctive | - |
| 2140 | **bar** | 5 | 645.80 | 7.453069 | 🟢 medium — moderately distinctive | bar, bars |
| 2141 | **reached** | 8 | 645.37 | 4.655071 | 🟢 medium — moderately distinctive | - |
| 2142 | **volume** | 7 | 644.93 | 5.316469 | 🟢 medium — moderately distinctive | volume, volumes |
| 2143 | **row** | 6 | 643.83 | 6.191938 | 🟢 medium — moderately distinctive | row, rows |
| 2144 | **context** | 5 | 640.85 | 7.395911 | 🟢 medium — moderately distinctive | context, contexts |
| 2145 | **related** | 7 | 640.79 | 5.282336 | 🟢 medium — moderately distinctive | - |
| 2146 | **almost** | 7 | 639.18 | 5.269003 | 🟢 medium — moderately distinctive | - |
| 2147 | **running** | 6 | 637.12 | 6.127399 | 🟢 medium — moderately distinctive | - |
| 2148 | **middling** | 4 | 636.88 | 9.18767 | 🟢 medium — moderately distinctive | - |
| 2149 | **swallowed** | 4 | 636.88 | 9.18767 | 🟢 medium — moderately distinctive | - |
| 2150 | **swamp** | 4 | 636.88 | 9.18767 | 🟢 medium — moderately distinctive | swamp, swamps |
| 2151 | **phrase** | 4 | 636.88 | 9.18767 | 🟢 medium — moderately distinctive | - |
| 2152 | **mistaken** | 4 | 636.88 | 9.18767 | 🟢 medium — moderately distinctive | - |
| 2153 | **deprived** | 4 | 636.88 | 9.18767 | 🟢 medium — moderately distinctive | - |
| 2154 | **mat** | 4 | 636.88 | 9.18767 | 🟢 medium — moderately distinctive | - |
| 2155 | **mould** | 4 | 636.88 | 9.18767 | 🟢 medium — moderately distinctive | - |
| 2156 | **array** | 4 | 636.88 | 9.18767 | 🟢 medium — moderately distinctive | - |
| 2157 | **irrelevant** | 4 | 636.88 | 9.18767 | 🟢 medium — moderately distinctive | - |
| 2158 | **deserve** | 4 | 636.88 | 9.18767 | 🟢 medium — moderately distinctive | deserve, deserves |
| 2159 | **spear** | 4 | 636.88 | 9.18767 | 🟢 medium — moderately distinctive | - |
| 2160 | **epidemic** | 4 | 636.88 | 9.18767 | 🟢 medium — moderately distinctive | epidemic, epidemics |
| 2161 | **separated** | 4 | 636.88 | 9.18767 | 🟢 medium — moderately distinctive | - |
| 2162 | **persistently** | 4 | 636.88 | 9.18767 | 🟢 medium — moderately distinctive | - |
| 2163 | **tsang** | 4 | 636.88 | 9.18767 | 🟢 medium — moderately distinctive | - |
| 2164 | **verbal** | 4 | 636.88 | 9.18767 | 🟢 medium — moderately distinctive | - |
| 2165 | **lightly** | 4 | 636.88 | 9.18767 | 🟢 medium — moderately distinctive | - |
| 2166 | **malaya** | 4 | 636.88 | 9.18767 | 🟢 medium — moderately distinctive | - |
| 2167 | **observe** | 4 | 636.88 | 9.18767 | 🟢 medium — moderately distinctive | - |
| 2168 | **interrupt** | 4 | 636.88 | 9.18767 | 🟢 medium — moderately distinctive | - |
| 2169 | **writing** | 5 | 636.16 | 7.341843 | 🟢 medium — moderately distinctive | writing, writings |
| 2170 | **protecting** | 5 | 636.16 | 7.341843 | 🟢 medium — moderately distinctive | - |
| 2171 | **heading** | 5 | 636.16 | 7.341843 | 🟢 medium — moderately distinctive | heading, headings |
| 2172 | **merely** | 5 | 636.16 | 7.341843 | 🟢 medium — moderately distinctive | - |
| 2173 | **scrap** | 5 | 636.16 | 7.341843 | 🟢 medium — moderately distinctive | - |
| 2174 | **stick** | 5 | 636.16 | 7.341843 | 🟢 medium — moderately distinctive | - |
| 2175 | **conclude** | 5 | 636.16 | 7.341843 | 🟢 medium — moderately distinctive | - |
| 2176 | **star** | 5 | 636.16 | 7.341843 | 🟢 medium — moderately distinctive | star, stars |
| 2177 | **major** | 10 | 634.89 | 3.663546 | 🟢 medium — moderately distinctive | - |
| 2178 | **soft** | 6 | 632.36 | 6.08159 | 🟢 medium — moderately distinctive | - |
| 2179 | **distance** | 5 | 631.72 | 7.29055 | 🟢 medium — moderately distinctive | - |
| 2180 | **pleased** | 5 | 631.72 | 7.29055 | 🟢 medium — moderately distinctive | - |
| 2181 | **developed** | 6 | 630.82 | 6.066775 | 🟢 medium — moderately distinctive | - |
| 2182 | **build** | 6 | 629.30 | 6.052176 | 🟢 medium — moderately distinctive | - |
| 2183 | **cost** | 8 | 628.99 | 4.536889 | 🟢 medium — moderately distinctive | cost, costs |
| 2184 | **satisfy** | 5 | 627.49 | 7.24176 | 🟢 medium — moderately distinctive | - |
| 2185 | **spring** | 6 | 624.87 | 6.009616 | 🟢 medium — moderately distinctive | spring, springs |
| 2186 | **continuous** | 5 | 623.46 | 7.19524 | 🟢 medium — moderately distinctive | - |
| 2187 | **resource** | 5 | 623.46 | 7.19524 | 🟢 medium — moderately distinctive | - |
| 2188 | **hoping** | 5 | 619.61 | 7.150788 | 🟢 medium — moderately distinctive | - |
| 2189 | **daily** | 7 | 617.19 | 5.087785 | 🟢 medium — moderately distinctive | - |
| 2190 | **sage** | 4 | 616.94 | 8.899988 | 🟢 medium — moderately distinctive | sage, sages |
| 2191 | **counting** | 4 | 616.94 | 8.899988 | 🟢 medium — moderately distinctive | - |
| 2192 | **fierce** | 4 | 616.94 | 8.899988 | 🟢 medium — moderately distinctive | - |
| 2193 | **penetrate** | 4 | 616.94 | 8.899988 | 🟢 medium — moderately distinctive | - |
| 2194 | **recipient** | 4 | 616.94 | 8.899988 | 🟢 medium — moderately distinctive | recipient, recipients |
| 2195 | **hook** | 4 | 616.94 | 8.899988 | 🟢 medium — moderately distinctive | hook, hooks |
| 2196 | **condemned** | 4 | 616.94 | 8.899988 | 🟢 medium — moderately distinctive | - |
| 2197 | **abundance** | 4 | 616.94 | 8.899988 | 🟢 medium — moderately distinctive | - |
| 2198 | **prosperity** | 4 | 616.94 | 8.899988 | 🟢 medium — moderately distinctive | - |
| 2199 | **sat** | 4 | 616.94 | 8.899988 | 🟢 medium — moderately distinctive | - |
| 2200 | **tower** | 4 | 616.94 | 8.899988 | 🟢 medium — moderately distinctive | tower, towers |
| 2201 | **eradicate** | 4 | 616.94 | 8.899988 | 🟢 medium — moderately distinctive | - |
| 2202 | **obtaining** | 5 | 615.92 | 7.108229 | 🟢 medium — moderately distinctive | - |
| 2203 | **determined** | 6 | 612.63 | 5.891833 | 🟢 medium — moderately distinctive | - |
| 2204 | **load** | 5 | 612.38 | 7.067407 | 🟢 medium — moderately distinctive | load, loads |
| 2205 | **degree** | 5 | 608.99 | 7.028186 | 🟢 medium — moderately distinctive | - |
| 2206 | **prepare** | 5 | 608.99 | 7.028186 | 🟢 medium — moderately distinctive | - |
| 2207 | **protected** | 5 | 608.99 | 7.028186 | 🟢 medium — moderately distinctive | - |
| 2208 | **eastern** | 6 | 608.85 | 5.855466 | 🟢 medium — moderately distinctive | - |
| 2209 | **pick** | 5 | 605.72 | 6.990446 | 🟢 medium — moderately distinctive | pick, picks |
| 2210 | **generate** | 5 | 605.72 | 6.990446 | 🟢 medium — moderately distinctive | - |
| 2211 | **factor** | 6 | 605.20 | 5.820374 | 🟢 medium — moderately distinctive | factor, factors |
| 2212 | **leading** | 7 | 605.08 | 4.987965 | 🟢 medium — moderately distinctive | - |
| 2213 | **corresponding** | 5 | 602.56 | 6.954078 | 🟢 medium — moderately distinctive | - |
| 2214 | **contact** | 5 | 602.56 | 6.954078 | 🟢 medium — moderately distinctive | - |
| 2215 | **motivated** | 4 | 601.47 | 8.676844 | 🟢 medium — moderately distinctive | - |
| 2216 | **notion** | 4 | 601.47 | 8.676844 | 🟢 medium — moderately distinctive | notion, notions |
| 2217 | **absent** | 4 | 601.47 | 8.676844 | 🟢 medium — moderately distinctive | - |
| 2218 | **arriving** | 4 | 601.47 | 8.676844 | 🟢 medium — moderately distinctive | - |
| 2219 | **remind** | 4 | 601.47 | 8.676844 | 🟢 medium — moderately distinctive | - |
| 2220 | **collection** | 4 | 601.47 | 8.676844 | 🟢 medium — moderately distinctive | - |
| 2221 | **breathing** | 4 | 601.47 | 8.676844 | 🟢 medium — moderately distinctive | - |
| 2222 | **casting** | 4 | 601.47 | 8.676844 | 🟢 medium — moderately distinctive | - |
| 2223 | **pearl** | 4 | 601.47 | 8.676844 | 🟢 medium — moderately distinctive | - |
| 2224 | **washed** | 4 | 601.47 | 8.676844 | 🟢 medium — moderately distinctive | - |
| 2225 | **interruption** | 4 | 601.47 | 8.676844 | 🟢 medium — moderately distinctive | - |
| 2226 | **chen** | 4 | 601.47 | 8.676844 | 🟢 medium — moderately distinctive | - |
| 2227 | **drawn** | 5 | 599.52 | 6.918987 | 🟢 medium — moderately distinctive | - |
| 2228 | **mixed** | 5 | 599.52 | 6.918987 | 🟢 medium — moderately distinctive | - |
| 2229 | **progress** | 6 | 599.39 | 5.764494 | 🟢 medium — moderately distinctive | - |
| 2230 | **spot** | 6 | 598.26 | 5.753683 | 🟢 medium — moderately distinctive | - |
| 2231 | **container** | 5 | 596.59 | 6.885085 | 🟢 medium — moderately distinctive | container, containers |
| 2232 | **grant** | 5 | 593.75 | 6.852295 | 🟢 medium — moderately distinctive | grant, grants |
| 2233 | **facing** | 5 | 593.75 | 6.852295 | 🟢 medium — moderately distinctive | - |
| 2234 | **held** | 8 | 591.67 | 4.267689 | 🟢 medium — moderately distinctive | - |
| 2235 | **conflict** | 5 | 590.99 | 6.820546 | 🟢 medium — moderately distinctive | conflict, conflicts |
| 2236 | **sour** | 5 | 590.99 | 6.820546 | 🟢 medium — moderately distinctive | - |
| 2237 | **basic** | 6 | 589.68 | 5.671162 | 🟢 medium — moderately distinctive | - |
| 2238 | **burst** | 4 | 588.83 | 8.494523 | 🟢 medium — moderately distinctive | - |
| 2239 | **castle** | 4 | 588.83 | 8.494523 | 🟢 medium — moderately distinctive | - |
| 2240 | **lamb** | 4 | 588.83 | 8.494523 | 🟢 medium — moderately distinctive | - |
| 2241 | **character** | 4 | 588.83 | 8.494523 | 🟢 medium — moderately distinctive | character, characters |
| 2242 | **delighted** | 4 | 588.83 | 8.494523 | 🟢 medium — moderately distinctive | - |
| 2243 | **filling** | 4 | 588.83 | 8.494523 | 🟢 medium — moderately distinctive | - |
| 2244 | **messenger** | 4 | 588.83 | 8.494523 | 🟢 medium — moderately distinctive | - |
| 2245 | **autumn** | 5 | 585.74 | 6.759922 | 🟢 medium — moderately distinctive | - |
| 2246 | **variety** | 5 | 583.23 | 6.730934 | 🟢 medium — moderately distinctive | varieties, variety |
| 2247 | **holder** | 5 | 583.23 | 6.730934 | 🟢 medium — moderately distinctive | - |
| 2248 | **adverse** | 5 | 580.79 | 6.702763 | 🟢 medium — moderately distinctive | - |
| 2249 | **easier** | 5 | 580.79 | 6.702763 | 🟢 medium — moderately distinctive | - |
| 2250 | **strike** | 6 | 579.86 | 5.576752 | 🟢 medium — moderately distinctive | - |
| 2251 | **notice** | 5 | 578.41 | 6.675364 | 🟢 medium — moderately distinctive | - |
| 2252 | **drawing** | 5 | 578.41 | 6.675364 | 🟢 medium — moderately distinctive | drawing, drawings |
| 2253 | **province** | 5 | 578.41 | 6.675364 | 🟢 medium — moderately distinctive | province, provinces |
| 2254 | **upper** | 5 | 578.41 | 6.675364 | 🟢 medium — moderately distinctive | - |
| 2255 | **consequence** | 4 | 578.15 | 8.340372 | 🟢 medium — moderately distinctive | - |
| 2256 | **upset** | 4 | 578.15 | 8.340372 | 🟢 medium — moderately distinctive | - |
| 2257 | **refuse** | 4 | 578.15 | 8.340372 | 🟢 medium — moderately distinctive | - |
| 2258 | **achievement** | 4 | 578.15 | 8.340372 | 🟢 medium — moderately distinctive | - |
| 2259 | **gateway** | 4 | 578.15 | 8.340372 | 🟢 medium — moderately distinctive | - |
| 2260 | **expressing** | 4 | 578.15 | 8.340372 | 🟢 medium — moderately distinctive | - |
| 2261 | **valley** | 5 | 576.10 | 6.648696 | 🟢 medium — moderately distinctive | valley, valleys |
| 2262 | **service** | 7 | 575.14 | 4.741105 | 🟢 medium — moderately distinctive | service, services |
| 2263 | **stance** | 5 | 573.85 | 6.622721 | 🟢 medium — moderately distinctive | stance, stances |
| 2264 | **final** | 7 | 571.87 | 4.714128 | 🟢 medium — moderately distinctive | - |
| 2265 | **war** | 6 | 570.04 | 5.482261 | 🟢 medium — moderately distinctive | war, wars |
| 2266 | **livestock** | 5 | 569.52 | 6.57271 | 🟢 medium — moderately distinctive | - |
| 2267 | **ignore** | 4 | 568.89 | 8.206841 | 🟢 medium — moderately distinctive | ignore, ignores |
| 2268 | **personally** | 4 | 568.89 | 8.206841 | 🟢 medium — moderately distinctive | - |
| 2269 | **ita** | 4 | 568.89 | 8.206841 | 🟢 medium — moderately distinctive | - |
| 2270 | **retreat** | 4 | 568.89 | 8.206841 | 🟢 medium — moderately distinctive | retreat, retreats |
| 2271 | **crystal** | 4 | 568.89 | 8.206841 | 🟢 medium — moderately distinctive | - |
| 2272 | **studying** | 5 | 565.39 | 6.525082 | 🟢 medium — moderately distinctive | - |
| 2273 | **good** | 7 | 563.83 | 4.647928 | 🟢 medium — moderately distinctive | - |
| 2274 | **identify** | 5 | 561.45 | 6.47962 | 🟢 medium — moderately distinctive | identifies, identify |
| 2275 | **stopped** | 5 | 561.45 | 6.47962 | 🟢 medium — moderately distinctive | - |
| 2276 | **discouraged** | 4 | 560.73 | 8.089058 | 🟢 medium — moderately distinctive | - |
| 2277 | **era** | 4 | 560.73 | 8.089058 | 🟢 medium — moderately distinctive | - |
| 2278 | **anywhere** | 4 | 560.73 | 8.089058 | 🟢 medium — moderately distinctive | - |
| 2279 | **hammer** | 4 | 560.73 | 8.089058 | 🟢 medium — moderately distinctive | - |
| 2280 | **destined** | 4 | 560.73 | 8.089058 | 🟢 medium — moderately distinctive | - |
| 2281 | **popularity** | 4 | 560.73 | 8.089058 | 🟢 medium — moderately distinctive | - |
| 2282 | **playing** | 4 | 560.73 | 8.089058 | 🟢 medium — moderately distinctive | - |
| 2283 | **performing** | 4 | 560.73 | 8.089058 | 🟢 medium — moderately distinctive | - |
| 2284 | **spreading** | 4 | 560.73 | 8.089058 | 🟢 medium — moderately distinctive | - |
| 2285 | **desirable** | 4 | 560.73 | 8.089058 | 🟢 medium — moderately distinctive | - |
| 2286 | **shown** | 5 | 559.55 | 6.457641 | 🟢 medium — moderately distinctive | - |
| 2287 | **pushed** | 5 | 559.55 | 6.457641 | 🟢 medium — moderately distinctive | - |
| 2288 | **interest** | 9 | 555.63 | 3.56245 | 🟢 medium — moderately distinctive | interest, interests |
| 2289 | **express** | 5 | 554.07 | 6.394462 | 🟢 medium — moderately distinctive | express, expresses |
| 2290 | **reveal** | 4 | 553.42 | 7.983697 | 🟢 medium — moderately distinctive | - |
| 2291 | **shot** | 4 | 553.42 | 7.983697 | 🟢 medium — moderately distinctive | - |
| 2292 | **crush** | 4 | 553.42 | 7.983697 | 🟢 medium — moderately distinctive | crush, crushes |
| 2293 | **behalf** | 5 | 552.32 | 6.374259 | 🟢 medium — moderately distinctive | - |
| 2294 | **decline** | 7 | 550.75 | 4.540079 | 🟢 medium — moderately distinctive | decline, declines |
| 2295 | **reduce** | 7 | 548.45 | 4.521091 | 🟢 medium — moderately distinctive | reduce, reduces |
| 2296 | **eventually** | 5 | 547.27 | 6.31599 | 🟢 medium — moderately distinctive | - |
| 2297 | **relying** | 4 | 546.82 | 7.888387 | 🟢 medium — moderately distinctive | - |
| 2298 | **simultaneously** | 4 | 546.82 | 7.888387 | 🟢 medium — moderately distinctive | - |
| 2299 | **undertaking** | 4 | 546.82 | 7.888387 | 🟢 medium — moderately distinctive | undertaking, undertakings |
| 2300 | **visiting** | 4 | 546.82 | 7.888387 | 🟢 medium — moderately distinctive | - |
| 2301 | **provoke** | 4 | 546.82 | 7.888387 | 🟢 medium — moderately distinctive | provoke, provokes |
| 2302 | **demanding** | 4 | 546.82 | 7.888387 | 🟢 medium — moderately distinctive | - |
| 2303 | **undertake** | 4 | 546.82 | 7.888387 | 🟢 medium — moderately distinctive | undertake, undertakes |
| 2304 | **saved** | 4 | 546.82 | 7.888387 | 🟢 medium — moderately distinctive | - |
| 2305 | **insisted** | 4 | 546.82 | 7.888387 | 🟢 medium — moderately distinctive | - |
| 2306 | **split** | 7 | 546.56 | 4.505539 | 🟢 medium — moderately distinctive | split, splits |
| 2307 | **produced** | 6 | 545.82 | 5.24933 | 🟢 medium — moderately distinctive | - |
| 2308 | **movement** | 5 | 542.50 | 6.260931 | 🟢 medium — moderately distinctive | movement, movements |
| 2309 | **conflicting** | 4 | 540.79 | 7.801376 | 🟢 medium — moderately distinctive | - |
| 2310 | **neighbouring** | 4 | 540.79 | 7.801376 | 🟢 medium — moderately distinctive | - |
| 2311 | **mature** | 4 | 540.79 | 7.801376 | 🟢 medium — moderately distinctive | - |
| 2312 | **lift** | 5 | 539.46 | 6.225839 | 🟢 medium — moderately distinctive | lift, lifts |
| 2313 | **swift** | 4 | 535.24 | 7.721333 | 🟢 medium — moderately distinctive | - |
| 2314 | **salt** | 4 | 535.24 | 7.721333 | 🟢 medium — moderately distinctive | - |
| 2315 | **fraud** | 4 | 535.24 | 7.721333 | 🟢 medium — moderately distinctive | fraud, frauds |
| 2316 | **silver** | 5 | 535.09 | 6.175409 | 🟢 medium — moderately distinctive | - |
| 2317 | **extreme** | 4 | 530.10 | 7.647225 | 🟢 medium — moderately distinctive | extreme, extremes |
| 2318 | **happening** | 4 | 530.10 | 7.647225 | 🟢 medium — moderately distinctive | happening, happenings |
| 2319 | **achieving** | 4 | 530.10 | 7.647225 | 🟢 medium — moderately distinctive | - |
| 2320 | **avoiding** | 4 | 530.10 | 7.647225 | 🟢 medium — moderately distinctive | - |
| 2321 | **eager** | 4 | 530.10 | 7.647225 | 🟢 medium — moderately distinctive | - |
| 2322 | **tomorrow** | 6 | 527.31 | 5.071347 | 🟢 medium — moderately distinctive | - |
| 2323 | **personal** | 5 | 526.96 | 6.08159 | 🟢 medium — moderately distinctive | - |
| 2324 | **member** | 6 | 526.75 | 5.065927 | 🟢 medium — moderately distinctive | member, members |
| 2325 | **useful** | 4 | 525.32 | 7.578232 | 🟢 medium — moderately distinctive | - |
| 2326 | **regardless** | 4 | 525.32 | 7.578232 | 🟢 medium — moderately distinctive | - |
| 2327 | **hurt** | 5 | 524.42 | 6.052176 | 🟢 medium — moderately distinctive | hurt, hurts |
| 2328 | **royal** | 5 | 524.42 | 6.052176 | 🟢 medium — moderately distinctive | - |
| 2329 | **sharp** | 6 | 522.35 | 5.023592 | 🟢 medium — moderately distinctive | - |
| 2330 | **decide** | 5 | 521.94 | 6.023602 | 🟢 medium — moderately distinctive | decide, decides |
| 2331 | **relation** | 4 | 520.84 | 7.513694 | 🟢 medium — moderately distinctive | relation, relations |
| 2332 | **connected** | 4 | 520.84 | 7.513694 | 🟢 medium — moderately distinctive | - |
| 2333 | **ought** | 4 | 520.84 | 7.513694 | 🟢 medium — moderately distinctive | - |
| 2334 | **belt** | 4 | 520.84 | 7.513694 | 🟢 medium — moderately distinctive | - |
| 2335 | **profit** | 9 | 519.33 | 3.329737 | 🟢 medium — moderately distinctive | profit, profits |
| 2336 | **confident** | 5 | 518.35 | 5.982217 | 🟢 medium — moderately distinctive | - |
| 2337 | **contrary** | 4 | 516.64 | 7.453069 | 🟢 medium — moderately distinctive | - |
| 2338 | **laid** | 4 | 516.64 | 7.453069 | 🟢 medium — moderately distinctive | - |
| 2339 | **accordance** | 4 | 516.64 | 7.453069 | 🟢 medium — moderately distinctive | - |
| 2340 | **promise** | 4 | 516.64 | 7.453069 | 🟢 medium — moderately distinctive | - |
| 2341 | **cotton** | 5 | 514.91 | 5.942477 | 🟢 medium — moderately distinctive | - |
| 2342 | **acquired** | 7 | 514.79 | 4.24365 | 🟢 medium — moderately distinctive | - |
| 2343 | **yes** | 4 | 512.68 | 7.395911 | 🟢 medium — moderately distinctive | - |
| 2344 | **regard** | 4 | 512.68 | 7.395911 | 🟢 medium — moderately distinctive | - |
| 2345 | **subsequently** | 4 | 512.68 | 7.395911 | 🟢 medium — moderately distinctive | - |
| 2346 | **shoe** | 4 | 512.68 | 7.395911 | 🟢 medium — moderately distinctive | - |
| 2347 | **repair** | 4 | 512.68 | 7.395911 | 🟢 medium — moderately distinctive | repair, repairs |
| 2348 | **associated** | 5 | 510.52 | 5.891833 | 🟢 medium — moderately distinctive | - |
| 2349 | **require** | 5 | 509.46 | 5.879563 | 🟢 medium — moderately distinctive | require, requires |
| 2350 | **wake** | 4 | 508.93 | 7.341843 | 🟢 medium — moderately distinctive | - |
| 2351 | **spell** | 4 | 508.93 | 7.341843 | 🟢 medium — moderately distinctive | - |
| 2352 | **plunged** | 4 | 505.38 | 7.29055 | 🟢 medium — moderately distinctive | - |
| 2353 | **site** | 4 | 505.38 | 7.29055 | 🟢 medium — moderately distinctive | - |
| 2354 | **unknown** | 4 | 501.99 | 7.24176 | 🟢 medium — moderately distinctive | - |
| 2355 | **couple** | 4 | 501.99 | 7.24176 | 🟢 medium — moderately distinctive | couple, couples |
| 2356 | **your** | 4 | 501.99 | 7.24176 | 🟢 medium — moderately distinctive | - |
| 2357 | **risk** | 5 | 500.44 | 5.775423 | 🟢 medium — moderately distinctive | - |
| 2358 | **pay** | 8 | 500.20 | 3.60794 | 🟢 medium — moderately distinctive | - |
| 2359 | **edge** | 4 | 498.77 | 7.19524 | 🔵 low — common in general English | - |
| 2360 | **irreversible** | 3 | 498.74 | 9.593135 | 🔵 low — common in general English | - |
| 2361 | **inclination** | 3 | 498.74 | 9.593135 | 🔵 low — common in general English | - |
| 2362 | **shelter** | 3 | 498.74 | 9.593135 | 🔵 low — common in general English | shelter, shelters |
| 2363 | **sixty** | 3 | 498.74 | 9.593135 | 🔵 low — common in general English | - |
| 2364 | **wooden** | 3 | 498.74 | 9.593135 | 🔵 low — common in general English | - |
| 2365 | **tossed** | 3 | 498.74 | 9.593135 | 🔵 low — common in general English | - |
| 2366 | **armoured** | 3 | 498.74 | 9.593135 | 🔵 low — common in general English | - |
| 2367 | **pierce** | 3 | 498.74 | 9.593135 | 🔵 low — common in general English | - |
| 2368 | **envy** | 3 | 498.74 | 9.593135 | 🔵 low — common in general English | - |
| 2369 | **folk** | 3 | 498.74 | 9.593135 | 🔵 low — common in general English | - |
| 2370 | **cas** | 3 | 498.74 | 9.593135 | 🔵 low — common in general English | - |
| 2371 | **uncomfortable** | 3 | 498.74 | 9.593135 | 🔵 low — common in general English | - |
| 2372 | **spoiled** | 3 | 498.74 | 9.593135 | 🔵 low — common in general English | - |
| 2373 | **talent** | 3 | 498.74 | 9.593135 | 🔵 low — common in general English | talent, talents |
| 2374 | **piling** | 3 | 498.74 | 9.593135 | 🔵 low — common in general English | - |
| 2375 | **glory** | 3 | 498.74 | 9.593135 | 🔵 low — common in general English | glories, glory |
| 2376 | **fearing** | 3 | 498.74 | 9.593135 | 🔵 low — common in general English | - |
| 2377 | **tiger** | 3 | 498.74 | 9.593135 | 🔵 low — common in general English | tiger, tigers |
| 2378 | **stir** | 3 | 498.74 | 9.593135 | 🔵 low — common in general English | - |
| 2379 | **organ** | 3 | 498.74 | 9.593135 | 🔵 low — common in general English | organ, organs |
| 2380 | **whipped** | 3 | 498.74 | 9.593135 | 🔵 low — common in general English | - |
| 2381 | **cultivated** | 3 | 498.74 | 9.593135 | 🔵 low — common in general English | - |
| 2382 | **drowned** | 3 | 498.74 | 9.593135 | 🔵 low — common in general English | - |
| 2383 | **correctly** | 3 | 498.74 | 9.593135 | 🔵 low — common in general English | - |
| 2384 | **monster** | 3 | 498.74 | 9.593135 | 🔵 low — common in general English | - |
| 2385 | **sur** | 3 | 498.74 | 9.593135 | 🔵 low — common in general English | - |
| 2386 | **healed** | 3 | 498.74 | 9.593135 | 🔵 low — common in general English | - |
| 2387 | **breathe** | 3 | 498.74 | 9.593135 | 🔵 low — common in general English | - |
| 2388 | **stealing** | 3 | 498.74 | 9.593135 | 🔵 low — common in general English | - |
| 2389 | **tail** | 3 | 498.74 | 9.593135 | 🔵 low — common in general English | tail, tails |
| 2390 | **mixing** | 3 | 498.74 | 9.593135 | 🔵 low — common in general English | - |
| 2391 | **pair** | 3 | 498.74 | 9.593135 | 🔵 low — common in general English | - |
| 2392 | **elder** | 3 | 498.74 | 9.593135 | 🔵 low — common in general English | - |
| 2393 | **handful** | 3 | 498.74 | 9.593135 | 🔵 low — common in general English | - |
| 2394 | **steadfast** | 3 | 498.74 | 9.593135 | 🔵 low — common in general English | - |
| 2395 | **tired** | 3 | 498.74 | 9.593135 | 🔵 low — common in general English | - |
| 2396 | **furious** | 3 | 498.74 | 9.593135 | 🔵 low — common in general English | - |
| 2397 | **meth** | 3 | 498.74 | 9.593135 | 🔵 low — common in general English | - |
| 2398 | **robbed** | 3 | 498.74 | 9.593135 | 🔵 low — common in general English | - |
| 2399 | **elaboration** | 3 | 498.74 | 9.593135 | 🔵 low — common in general English | elaboration, elaborations |
| 2400 | **chased** | 3 | 498.74 | 9.593135 | 🔵 low — common in general English | - |
| 2401 | **saddle** | 3 | 498.74 | 9.593135 | 🔵 low — common in general English | - |
| 2402 | **crippled** | 3 | 498.74 | 9.593135 | 🔵 low — common in general English | - |
| 2403 | **plausible** | 3 | 498.74 | 9.593135 | 🔵 low — common in general English | - |
| 2404 | **myriad** | 3 | 498.74 | 9.593135 | 🔵 low — common in general English | myriad, myriads |
| 2405 | **hero** | 3 | 498.74 | 9.593135 | 🔵 low — common in general English | - |
| 2406 | **misfortune** | 3 | 498.74 | 9.593135 | 🔵 low — common in general English | - |
| 2407 | **dispense** | 3 | 498.74 | 9.593135 | 🔵 low — common in general English | - |
| 2408 | **unaltered** | 3 | 498.74 | 9.593135 | 🔵 low — common in general English | - |
| 2409 | **petal** | 3 | 498.74 | 9.593135 | 🔵 low — common in general English | - |
| 2410 | **dancing** | 3 | 498.74 | 9.593135 | 🔵 low — common in general English | - |
| 2411 | **gracious** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - |
| 2412 | **quintessential** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - |
| 2413 | **copper-coloured** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - |
| 2414 | **hevajra** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - |
| 2415 | **pore** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | pore, pores |
| 2416 | **gossip** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - |
| 2417 | **prac** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - |
| 2418 | **contempt** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - |
| 2419 | **flaming** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - |
| 2420 | **inferno** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | inferno, infernos |
| 2421 | **engrossed** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - |
| 2422 | **gnawing** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - |
| 2423 | **labdron** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - |
| 2424 | **thirsty** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - |
| 2425 | **vowing** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - |
| 2426 | **elixir** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | elixir, elixirs |
| 2427 | **conquer** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | conquer, conquers |
| 2428 | **musk-deer** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - |
| 2429 | **musk** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - |
| 2430 | **brimming** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - |
| 2431 | **long-lived** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - |
| 2432 | **mute** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - |
| 2433 | **inheriting** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - |
| 2434 | **pernicious** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - |
| 2435 | **lha-thothori** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - |
| 2436 | **nyentsen** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - |
| 2437 | **alphabet** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - |
| 2438 | **avalokitdvara** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - |
| 2439 | **sery** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - |
| 2440 | **preceptor** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | preceptor, preceptors |
| 2441 | **unite** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | unite, unites |
| 2442 | **forty** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - |
| 2443 | **smrtijnana** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - |
| 2444 | **wept** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - |
| 2445 | **accom** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - |
| 2446 | **glimmer** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | glimmer, glimmers |
| 2447 | **servitude** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - |
| 2448 | **habit** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | habit, habits |
| 2449 | **tightly** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - |
| 2450 | **brew** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - |
| 2451 | **surabhibhadra** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - |
| 2452 | **upright** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - |
| 2453 | **promis** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - |
| 2454 | **slept** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - |
| 2455 | **spittle** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - |
| 2456 | **noose** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - |
| 2457 | **brilliance** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - |
| 2458 | **chest** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - |
| 2459 | **alight** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - |
| 2460 | **tsenpo** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - |
| 2461 | **tsen** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - |
| 2462 | **radiance** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - |
| 2463 | **wrong-doing** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - |
| 2464 | **shower** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | shower, showers |
| 2465 | **breez** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - |
| 2466 | **enmity** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - |
| 2467 | **brocade** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | brocade, brocades |
| 2468 | **cheek** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - |
| 2469 | **murdered** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - |
| 2470 | **starving** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - |
| 2471 | **affectionate** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - |
| 2472 | **tingri** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - |
| 2473 | **barren** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - |
| 2474 | **everlasting** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - |
| 2475 | **relish** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - |
| 2476 | **trivial** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - |
| 2477 | **murder** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - |
| 2478 | **daughter-in-law** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - |
| 2479 | **courageously** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - |
| 2480 | **thieve** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - |
| 2481 | **mortal** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - |
| 2482 | **single-mindedly** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - |
| 2483 | **experi** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - |
| 2484 | **amassing** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - |
| 2485 | **greasy** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - |
| 2486 | **arous** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - |
| 2487 | **assimilated** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - |
| 2488 | **yama** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - |
| 2489 | **chopped** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - |
| 2490 | **prong** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - |
| 2491 | **beak** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | beak, beaks |
| 2492 | **devour** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - |
| 2493 | **razor** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | razor, razors |
| 2494 | **biting** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - |
| 2495 | **brain** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | brain, brains |
| 2496 | **moun** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - |
| 2497 | **tain** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - |
| 2498 | **lamenting** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - |
| 2499 | **lingje** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - |
| 2500 | **lung** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | lung, lungs |
| 2501 | **uttered** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - |
| 2502 | **entrail** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - |
| 2503 | **derge** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - |
| 2504 | **intellectually** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - |
| 2505 | **karmapa** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | karmapa, karmapas |
| 2506 | **obsessed** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - |
| 2507 | **avarice** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - |
| 2508 | **dish** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | dish, dishes |
| 2509 | **nose** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - |
| 2510 | **ugliness** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - |
| 2511 | **snot** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - |
| 2512 | **mamo** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | mamo, mamos |
| 2513 | **happily** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - |
| 2514 | **bum** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | bum, bums |
| 2515 | **regretting** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - |
| 2516 | **accumu** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - |
| 2517 | **plunder** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | plunder, plunders |
| 2518 | **leprosy** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - |
| 2519 | **pregnancy** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - |
| 2520 | **creep** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | creep, creeps |
| 2521 | **granny** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - |
| 2522 | **frown** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | frown, frowns |
| 2523 | **ugly** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - |
| 2524 | **insipid** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - |
| 2525 | **lax** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - |
| 2526 | **left-over** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - |
| 2527 | **unclean** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - |
| 2528 | **apparition** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | apparition, apparitions |
| 2529 | **steeped** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - |
| 2530 | **married** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - |
| 2531 | **rosary** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - |
| 2532 | **kindly** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - |
| 2533 | **exhort** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | exhort, exhorts |
| 2534 | **disgust** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - |
| 2535 | **demigod** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - |
| 2536 | **wish-fulfilling** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - |
| 2537 | **waking** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - |
| 2538 | **imagination** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - |
| 2539 | **one-eyed** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - |
| 2540 | **affection** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - |
| 2541 | **mahayana** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - |
| 2542 | **slaughterer** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | slaughterer, slaughterers |
| 2543 | **streaming** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - |
| 2544 | **shortcoming** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | shortcoming, shortcomings |
| 2545 | **laypeople** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - |
| 2546 | **phoney** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - |
| 2547 | **deceive** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - |
| 2548 | **harshly** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - |
| 2549 | **robbery** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - |
| 2550 | **eternalism** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - |
| 2551 | **nihilism** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - |
| 2552 | **peacock** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | peacock, peacocks |
| 2553 | **multicoloured** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - |
| 2554 | **stole** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - |
| 2555 | **lied** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - |
| 2556 | **sin** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | sin, sins |
| 2557 | **futile** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - |
| 2558 | **virudhaka** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - |
| 2559 | **fishermen** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - |
| 2560 | **troop** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - |
| 2561 | **strayed** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - |
| 2562 | **elapatra** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - |
| 2563 | **miserly** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - |
| 2564 | **wholesome** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - |
| 2565 | **incarnation** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | incarnation, incarnations |
| 2566 | **unconscious** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - |
| 2567 | **ness** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - |
| 2568 | **cling** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | cling, clings |
| 2569 | **pathway** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | pathway, pathways |
| 2570 | **navigator** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - |
| 2571 | **pratimok** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - |
| 2572 | **brilliant** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - |
| 2573 | **bathe** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - |
| 2574 | **unfold** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | unfold, unfolds |
| 2575 | **dispelling** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - |
| 2576 | **tainted** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - |
| 2577 | **arrogance** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - |
| 2578 | **verbally** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - |
| 2579 | **slam** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | slam, slams |
| 2580 | **accomplishing** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - |
| 2581 | **impurity** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | impurities, impurity |
| 2582 | **imitate** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | imitate, imitates |
| 2583 | **prajflaparamita** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - |
| 2584 | **fatigue** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - |
| 2585 | **fragrant** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - |
| 2586 | **ods** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - |
| 2587 | **bestow** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - |
| 2588 | **retinue** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - |
| 2589 | **carriage** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | carriage, carriages |
| 2590 | **conquest** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - |
| 2591 | **sinner** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | sinner, sinners |
| 2592 | **inexpressible** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - |
| 2593 | **erment** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - |
| 2594 | **vers** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - |
| 2595 | **deceit** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - |
| 2596 | **kusali** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - |
| 2597 | **stroke** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - |
| 2598 | **devadatta** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - |
| 2599 | **imbued** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - |
| 2600 | **mafijusrimitra** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - |
| 2601 | **simha** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - |
| 2602 | **longchen** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - |
| 2603 | **lattice** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - |
| 2604 | **cruel** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - |
| 2605 | **unceasingly** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - |
| 2606 | **saucer** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - |
| 2607 | **transgress** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - |
| 2608 | **afar** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - |
| 2609 | **drip** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | drip, drips |
| 2610 | **malignant** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - |
| 2611 | **freshly** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - |
| 2612 | **hind** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - |
| 2613 | **faintest** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - |
| 2614 | **camel** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | camel, camels |
| 2615 | **verse** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - |
| 2616 | **quintessence** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - |
| 2617 | **panacea** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - |
| 2618 | **defilement** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - |
| 2619 | **louse** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - |
| 2620 | **vallabha** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - |
| 2621 | **leper** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - |
| 2622 | **dodepa** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - |
| 2623 | **cured** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - |
| 2624 | **risi** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - |
| 2625 | **omen** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - |
| 2626 | **transmitting** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - |
| 2627 | **warmth** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - |
| 2628 | **tame** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - |
| 2629 | **indivisible** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - |
| 2630 | **imprint** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | imprint, imprints |
| 2631 | **angulimala** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - |
| 2632 | **prostrating** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - |
| 2633 | **adorned** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - |
| 2634 | **tva** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - |
| 2635 | **sattva** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | sattva, sattvas |
| 2636 | **tsari** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - |
| 2637 | **perfumed** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - |
| 2638 | **explanatory** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - |
| 2639 | **mahakasyapa** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - |
| 2640 | **prasenajit** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - |
| 2641 | **aperture** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - |
| 2642 | **demoness** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - |
| 2643 | **duality** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - |
| 2644 | **mipham** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - |
| 2645 | **dissolved** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - |
| 2646 | **lotus-bud** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - |
| 2647 | **khatvanga** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - |
| 2648 | **rejoiced** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - |
| 2649 | **vaisali** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - |
| 2650 | **cubit** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - |
| 2651 | **kutra** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - |
| 2652 | **tingdzin** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - |
| 2653 | **santarak** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - |
| 2654 | **chopel** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - |
| 2655 | **hik** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - |
| 2656 | **ejection** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - |
| 2657 | **orgyen** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - |
| 2658 | **rising** | 6 | 498.39 | 4.793221 | 🔵 low — common in general English | - |
| 2659 | **royalty** | 4 | 495.69 | 7.150788 | 🔵 low — common in general English | - |
| 2660 | **comparison** | 4 | 492.74 | 7.108229 | 🔵 low — common in general English | comparison, comparisons |
| 2661 | **border** | 4 | 492.74 | 7.108229 | 🔵 low — common in general English | - |
| 2662 | **absence** | 4 | 492.74 | 7.108229 | 🔵 low — common in general English | - |
| 2663 | **slowly** | 4 | 492.74 | 7.108229 | 🔵 low — common in general English | - |
| 2664 | **sri** | 4 | 492.74 | 7.108229 | 🔵 low — common in general English | - |
| 2665 | **share** | 10 | 491.11 | 2.83388 | 🔵 low — common in general English | - |
| 2666 | **minister** | 7 | 491.05 | 4.047958 | 🔵 low — common in general English | minister, ministers |
| 2667 | **developing** | 5 | 490.55 | 5.66131 | 🔵 low — common in general English | - |
| 2668 | **intelligence** | 4 | 489.91 | 7.067407 | 🔵 low — common in general English | - |
| 2669 | **choice** | 4 | 487.19 | 7.028186 | 🔵 low — common in general English | - |
| 2670 | **hour** | 4 | 487.19 | 7.028186 | 🔵 low — common in general English | hour, hours |
| 2671 | **representative** | 5 | 486.40 | 5.613454 | 🔵 low — common in general English | representative, representatives |
| 2672 | **ultimately** | 4 | 484.57 | 6.990446 | 🔵 low — common in general English | - |
| 2673 | **sustained** | 4 | 484.57 | 6.990446 | 🔵 low — common in general English | - |
| 2674 | **temporarily** | 4 | 482.05 | 6.954078 | 🔵 low — common in general English | - |
| 2675 | **fine** | 4 | 479.62 | 6.918987 | 🔵 low — common in general English | - |
| 2676 | **shooting** | 3 | 477.66 | 9.18767 | 🔵 low — common in general English | - |
| 2677 | **visual** | 3 | 477.66 | 9.18767 | 🔵 low — common in general English | - |
| 2678 | **mud** | 3 | 477.66 | 9.18767 | 🔵 low — common in general English | - |
| 2679 | **attach** | 3 | 477.66 | 9.18767 | 🔵 low — common in general English | - |
| 2680 | **roof** | 3 | 477.66 | 9.18767 | 🔵 low — common in general English | - |
| 2681 | **plough** | 3 | 477.66 | 9.18767 | 🔵 low — common in general English | - |
| 2682 | **worthy** | 3 | 477.66 | 9.18767 | 🔵 low — common in general English | - |
| 2683 | **disciplined** | 3 | 477.66 | 9.18767 | 🔵 low — common in general English | - |
| 2684 | **stretched** | 3 | 477.66 | 9.18767 | 🔵 low — common in general English | - |
| 2685 | **magic** | 3 | 477.66 | 9.18767 | 🔵 low — common in general English | - |
| 2686 | **cardinal** | 3 | 477.66 | 9.18767 | 🔵 low — common in general English | - |
| 2687 | **sesame** | 3 | 477.66 | 9.18767 | 🔵 low — common in general English | - |
| 2688 | **belly** | 3 | 477.66 | 9.18767 | 🔵 low — common in general English | bellies, belly |
| 2689 | **isn** | 3 | 477.66 | 9.18767 | 🔵 low — common in general English | - |
| 2690 | **cheese** | 3 | 477.66 | 9.18767 | 🔵 low — common in general English | - |
| 2691 | **ragged** | 3 | 477.66 | 9.18767 | 🔵 low — common in general English | - |
| 2692 | **overcoming** | 3 | 477.66 | 9.18767 | 🔵 low — common in general English | - |
| 2693 | **theft** | 3 | 477.66 | 9.18767 | 🔵 low — common in general English | - |
| 2694 | **miracle** | 3 | 477.66 | 9.18767 | 🔵 low — common in general English | - |
| 2695 | **renouncing** | 3 | 477.66 | 9.18767 | 🔵 low — common in general English | - |
| 2696 | **severed** | 3 | 477.66 | 9.18767 | 🔵 low — common in general English | - |
| 2697 | **utmost** | 3 | 477.66 | 9.18767 | 🔵 low — common in general English | - |
| 2698 | **workable** | 3 | 477.66 | 9.18767 | 🔵 low — common in general English | - |
| 2699 | **resolute** | 3 | 477.66 | 9.18767 | 🔵 low — common in general English | - |
| 2700 | **wished** | 3 | 477.66 | 9.18767 | 🔵 low — common in general English | - |
| 2701 | **willingly** | 3 | 477.66 | 9.18767 | 🔵 low — common in general English | - |
| 2702 | **lunar** | 3 | 477.66 | 9.18767 | 🔵 low — common in general English | - |
| 2703 | **repetition** | 3 | 477.66 | 9.18767 | 🔵 low — common in general English | repetition, repetitions |
| 2704 | **shorten** | 3 | 477.66 | 9.18767 | 🔵 low — common in general English | - |
| 2705 | **repeating** | 3 | 477.66 | 9.18767 | 🔵 low — common in general English | - |
| 2706 | **event** | 4 | 477.27 | 6.885085 | 🔵 low — common in general English | event, events |
| 2707 | **losing** | 4 | 477.27 | 6.885085 | 🔵 low — common in general English | - |
| 2708 | **northern** | 5 | 475.03 | 5.482261 | 🔵 low — common in general English | - |
| 2709 | **bottom** | 4 | 472.80 | 6.820546 | 🔵 low — common in general English | - |
| 2710 | **elsewhere** | 4 | 472.80 | 6.820546 | 🔵 low — common in general English | - |
| 2711 | **criticism** | 4 | 472.80 | 6.820546 | 🔵 low — common in general English | - |
| 2712 | **law** | 5 | 471.55 | 5.442095 | 🔵 low — common in general English | law, laws |
| 2713 | **cover** | 5 | 470.87 | 5.434252 | 🔵 low — common in general English | cover, covers |
| 2714 | **chain** | 4 | 470.66 | 6.789775 | 🔵 low — common in general English | chain, chains |
| 2715 | **remained** | 5 | 469.53 | 5.418748 | 🔵 low — common in general English | - |
| 2716 | **jumped** | 4 | 468.59 | 6.759922 | 🔵 low — common in general English | - |
| 2717 | **ended** | 7 | 465.13 | 3.834233 | 🔵 low — common in general English | - |
| 2718 | **liquid** | 4 | 464.63 | 6.702763 | 🔵 low — common in general English | - |
| 2719 | **draw** | 4 | 464.63 | 6.702763 | 🔵 low — common in general English | draw, draws |
| 2720 | **discomfort** | 3 | 462.71 | 8.899988 | 🔵 low — common in general English | discomfort, discomforts |
| 2721 | **uphold** | 3 | 462.71 | 8.899988 | 🔵 low — common in general English | - |
| 2722 | **checking** | 3 | 462.71 | 8.899988 | 🔵 low — common in general English | - |
| 2723 | **descent** | 3 | 462.71 | 8.899988 | 🔵 low — common in general English | descent, descents |
| 2724 | **compounded** | 3 | 462.71 | 8.899988 | 🔵 low — common in general English | - |
| 2725 | **height** | 3 | 462.71 | 8.899988 | 🔵 low — common in general English | height, heights |
| 2726 | **thirty** | 3 | 462.71 | 8.899988 | 🔵 low — common in general English | - |
| 2727 | **mansion** | 3 | 462.71 | 8.899988 | 🔵 low — common in general English | mansion, mansions |
| 2728 | **amongst** | 3 | 462.71 | 8.899988 | 🔵 low — common in general English | - |
| 2729 | **powdered** | 3 | 462.71 | 8.899988 | 🔵 low — common in general English | - |
| 2730 | **bind** | 3 | 462.71 | 8.899988 | 🔵 low — common in general English | bind, binds |
| 2731 | **harmed** | 3 | 462.71 | 8.899988 | 🔵 low — common in general English | - |
| 2732 | **namely** | 3 | 462.71 | 8.899988 | 🔵 low — common in general English | - |
| 2733 | **drinking** | 3 | 462.71 | 8.899988 | 🔵 low — common in general English | - |
| 2734 | **shaken** | 3 | 462.71 | 8.899988 | 🔵 low — common in general English | - |
| 2735 | **pour** | 3 | 462.71 | 8.899988 | 🔵 low — common in general English | pour, pours |
| 2736 | **inspired** | 3 | 462.71 | 8.899988 | 🔵 low — common in general English | - |
| 2737 | **invoked** | 3 | 462.71 | 8.899988 | 🔵 low — common in general English | - |
| 2738 | **recognizing** | 3 | 462.71 | 8.899988 | 🔵 low — common in general English | - |
| 2739 | **pity** | 3 | 462.71 | 8.899988 | 🔵 low — common in general English | - |
| 2740 | **ring** | 3 | 462.71 | 8.899988 | 🔵 low — common in general English | ring, rings |
| 2741 | **assembled** | 3 | 462.71 | 8.899988 | 🔵 low — common in general English | - |
| 2742 | **origin** | 4 | 460.88 | 6.648696 | 🔵 low — common in general English | origin, origins |
| 2743 | **produce** | 5 | 459.47 | 5.302676 | 🔵 low — common in general English | produce, produces |
| 2744 | **maturity** | 4 | 459.08 | 6.622721 | 🔵 low — common in general English | - |
| 2745 | **wide** | 4 | 457.33 | 6.597403 | 🔵 low — common in general English | - |
| 2746 | **grown** | 4 | 457.33 | 6.597403 | 🔵 low — common in general English | - |
| 2747 | **provided** | 5 | 456.55 | 5.269003 | 🔵 low — common in general English | - |
| 2748 | **trade** | 8 | 455.18 | 3.283217 | 🔵 low — common in general English | - |
| 2749 | **gained** | 4 | 453.95 | 6.548613 | 🔵 low — common in general English | - |
| 2750 | **los** | 4 | 453.95 | 6.548613 | 🔵 low — common in general English | - |
| 2751 | **falling** | 5 | 453.18 | 5.230037 | 🔵 low — common in general English | - |
| 2752 | **fundamental** | 4 | 452.31 | 6.525082 | 🔵 low — common in general English | - |
| 2753 | **meeting** | 7 | 451.56 | 3.722427 | 🔵 low — common in general English | - |
| 2754 | **contemplate** | 3 | 451.10 | 8.676844 | 🔵 low — common in general English | - |
| 2755 | **imperative** | 3 | 451.10 | 8.676844 | 🔵 low — common in general English | - |
| 2756 | **chasing** | 3 | 451.10 | 8.676844 | 🔵 low — common in general English | - |
| 2757 | **intact** | 3 | 451.10 | 8.676844 | 🔵 low — common in general English | - |
| 2758 | **sink** | 3 | 451.10 | 8.676844 | 🔵 low — common in general English | - |
| 2759 | **progressively** | 3 | 451.10 | 8.676844 | 🔵 low — common in general English | - |
| 2760 | **guarded** | 3 | 451.10 | 8.676844 | 🔵 low — common in general English | - |
| 2761 | **compiled** | 3 | 451.10 | 8.676844 | 🔵 low — common in general English | - |
| 2762 | **welfare** | 3 | 451.10 | 8.676844 | 🔵 low — common in general English | - |
| 2763 | **profoundly** | 3 | 451.10 | 8.676844 | 🔵 low — common in general English | - |
| 2764 | **deeper** | 3 | 451.10 | 8.676844 | 🔵 low — common in general English | - |
| 2765 | **roasted** | 3 | 451.10 | 8.676844 | 🔵 low — common in general English | - |
| 2766 | **crack** | 3 | 451.10 | 8.676844 | 🔵 low — common in general English | - |
| 2767 | **thick** | 3 | 451.10 | 8.676844 | 🔵 low — common in general English | - |
| 2768 | **offensive** | 3 | 451.10 | 8.676844 | 🔵 low — common in general English | - |
| 2769 | **conditioning** | 3 | 451.10 | 8.676844 | 🔵 low — common in general English | - |
| 2770 | **splinter** | 3 | 451.10 | 8.676844 | 🔵 low — common in general English | - |
| 2771 | **weighed** | 3 | 451.10 | 8.676844 | 🔵 low — common in general English | - |
| 2772 | **heap** | 3 | 451.10 | 8.676844 | 🔵 low — common in general English | heap, heaps |
| 2773 | **capture** | 3 | 451.10 | 8.676844 | 🔵 low — common in general English | - |
| 2774 | **peak** | 4 | 449.16 | 6.47962 | 🔵 low — common in general English | - |
| 2775 | **pursue** | 4 | 447.64 | 6.457641 | 🔵 low — common in general English | - |
| 2776 | **store** | 4 | 446.15 | 6.436135 | 🔵 low — common in general English | - |
| 2777 | **defend** | 4 | 446.15 | 6.436135 | 🔵 low — common in general English | - |
| 2778 | **drive** | 4 | 446.15 | 6.436135 | 🔵 low — common in general English | drive, drives |
| 2779 | **billion** | 9 | 445.19 | 2.85439 | 🔵 low — common in general English | - |
| 2780 | **opinion** | 4 | 443.26 | 6.394462 | 🔵 low — common in general English | opinion, opinions |
| 2781 | **collapse** | 4 | 441.86 | 6.374259 | 🔵 low — common in general English | - |
| 2782 | **music** | 3 | 441.63 | 8.494523 | 🔵 low — common in general English | - |
| 2783 | **endeavour** | 3 | 441.63 | 8.494523 | 🔵 low — common in general English | - |
| 2784 | **wealthy** | 3 | 441.63 | 8.494523 | 🔵 low — common in general English | - |
| 2785 | **fur** | 3 | 441.63 | 8.494523 | 🔵 low — common in general English | fur, furs |
| 2786 | **nice** | 3 | 441.63 | 8.494523 | 🔵 low — common in general English | - |
| 2787 | **grove** | 3 | 441.63 | 8.494523 | 🔵 low — common in general English | grove, groves |
| 2788 | **introducing** | 3 | 441.63 | 8.494523 | 🔵 low — common in general English | - |
| 2789 | **sympathetic** | 3 | 441.63 | 8.494523 | 🔵 low — common in general English | - |
| 2790 | **unfortunate** | 3 | 441.63 | 8.494523 | 🔵 low — common in general English | - |
| 2791 | **closed** | 5 | 440.85 | 5.087785 | 🔵 low — common in general English | - |
| 2792 | **nearby** | 4 | 440.49 | 6.354457 | 🔵 low — common in general English | - |
| 2793 | **attention** | 4 | 440.49 | 6.354457 | 🔵 low — common in general English | - |
| 2794 | **growing** | 5 | 439.43 | 5.071347 | 🔵 low — common in general English | - |
| 2795 | **needed** | 5 | 436.65 | 5.039258 | 🔵 low — common in general English | - |
| 2796 | **covering** | 4 | 436.52 | 6.297298 | 🔵 low — common in general English | - |
| 2797 | **allow** | 5 | 433.95 | 5.008168 | 🔵 low — common in general English | allow, allows |
| 2798 | **drove** | 3 | 433.61 | 8.340372 | 🔵 low — common in general English | - |
| 2799 | **relaxed** | 3 | 433.61 | 8.340372 | 🔵 low — common in general English | - |
| 2800 | **frontier** | 3 | 433.61 | 8.340372 | 🔵 low — common in general English | frontier, frontiers |
| 2801 | **dig** | 3 | 433.61 | 8.340372 | 🔵 low — common in general English | dig, digs |
| 2802 | **disagreement** | 3 | 433.61 | 8.340372 | 🔵 low — common in general English | disagreement, disagreements |
| 2803 | **pig** | 3 | 433.61 | 8.340372 | 🔵 low — common in general English | - |
| 2804 | **declared** | 5 | 432.20 | 4.987965 | 🔵 low — common in general English | - |
| 2805 | **extent** | 4 | 431.57 | 6.225839 | 🔵 low — common in general English | - |
| 2806 | **providing** | 4 | 431.57 | 6.225839 | 🔵 low — common in general English | - |
| 2807 | **began** | 5 | 431.34 | 4.978015 | 🔵 low — common in general English | - |
| 2808 | **seeking** | 5 | 430.49 | 4.968162 | 🔵 low — common in general English | - |
| 2809 | **western** | 5 | 429.64 | 4.958406 | 🔵 low — common in general English | - |
| 2810 | **week** | 7 | 429.42 | 3.53987 | 🔵 low — common in general English | week, weeks |
| 2811 | **bank** | 8 | 428.96 | 3.0941 | 🔵 low — common in general English | bank, banks |
| 2812 | **near** | 5 | 428.80 | 4.948744 | 🔵 low — common in general English | - |
| 2813 | **moved** | 4 | 428.07 | 6.175409 | 🔵 low — common in general English | - |
| 2814 | **showed** | 5 | 426.75 | 4.92499 | 🔵 low — common in general English | - |
| 2815 | **function** | 3 | 426.67 | 8.206841 | 🔵 low — common in general English | function, functions |
| 2816 | **peripheral** | 3 | 426.67 | 8.206841 | 🔵 low — common in general English | - |
| 2817 | **affair** | 3 | 426.67 | 8.206841 | 🔵 low — common in general English | - |
| 2818 | **hawk** | 3 | 426.67 | 8.206841 | 🔵 low — common in general English | hawk, hawks |
| 2819 | **stepping** | 3 | 426.67 | 8.206841 | 🔵 low — common in general English | - |
| 2820 | **slope** | 3 | 426.67 | 8.206841 | 🔵 low — common in general English | slope, slopes |
| 2821 | **defeated** | 3 | 426.67 | 8.206841 | 🔵 low — common in general English | - |
| 2822 | **extend** | 4 | 425.84 | 6.143148 | 🔵 low — common in general English | - |
| 2823 | **talk** | 4 | 424.75 | 6.127399 | 🔵 low — common in general English | - |
| 2824 | **north** | 5 | 423.94 | 4.892655 | 🔵 low — common in general English | - |
| 2825 | **determine** | 4 | 423.67 | 6.111895 | 🔵 low — common in general English | determine, determines |
| 2826 | **enable** | 4 | 423.67 | 6.111895 | 🔵 low — common in general English | enable, enables |
| 2827 | **ending** | 5 | 423.55 | 4.88812 | 🔵 low — common in general English | - |
| 2828 | **rein** | 3 | 420.55 | 8.089058 | 🔵 low — common in general English | rein, reins |
| 2829 | **remote** | 3 | 420.55 | 8.089058 | 🔵 low — common in general English | - |
| 2830 | **earliest** | 3 | 420.55 | 8.089058 | 🔵 low — common in general English | - |
| 2831 | **smooth** | 3 | 420.55 | 8.089058 | 🔵 low — common in general English | - |
| 2832 | **distorted** | 3 | 420.55 | 8.089058 | 🔵 low — common in general English | - |
| 2833 | **vary** | 3 | 420.55 | 8.089058 | 🔵 low — common in general English | - |
| 2834 | **feeding** | 3 | 420.55 | 8.089058 | 🔵 low — common in general English | - |
| 2835 | **ceased** | 3 | 420.55 | 8.089058 | 🔵 low — common in general English | - |
| 2836 | **growth** | 6 | 418.10 | 4.020981 | 🔵 low — common in general English | - |
| 2837 | **sell** | 6 | 417.90 | 4.019082 | 🔵 low — common in general English | - |
| 2838 | **paying** | 4 | 417.55 | 6.023602 | 🔵 low — common in general English | - |
| 2839 | **harvest** | 4 | 416.58 | 6.009616 | 🔵 low — common in general English | harvest, harvests |
| 2840 | **successor** | 3 | 415.07 | 7.983697 | 🔵 low — common in general English | successor, successors |
| 2841 | **loaded** | 3 | 415.07 | 7.983697 | 🔵 low — common in general English | - |
| 2842 | **inherent** | 3 | 415.07 | 7.983697 | 🔵 low — common in general English | - |
| 2843 | **banner** | 3 | 415.07 | 7.983697 | 🔵 low — common in general English | banner, banners |
| 2844 | **inevitably** | 3 | 415.07 | 7.983697 | 🔵 low — common in general English | - |
| 2845 | **access** | 4 | 410.15 | 5.916835 | 🔵 low — common in general English | - |
| 2846 | **fulfil** | 3 | 410.11 | 7.888387 | 🔵 low — common in general English | - |
| 2847 | **upside** | 3 | 410.11 | 7.888387 | 🔵 low — common in general English | - |
| 2848 | **custom** | 3 | 410.11 | 7.888387 | 🔵 low — common in general English | - |
| 2849 | **translated** | 3 | 410.11 | 7.888387 | 🔵 low — common in general English | - |
| 2850 | **practical** | 3 | 410.11 | 7.888387 | 🔵 low — common in general English | - |
| 2851 | **scattered** | 3 | 410.11 | 7.888387 | 🔵 low — common in general English | - |
| 2852 | **unlimited** | 3 | 410.11 | 7.888387 | 🔵 low — common in general English | - |
| 2853 | **roll** | 3 | 410.11 | 7.888387 | 🔵 low — common in general English | roll, rolls |
| 2854 | **minute** | 3 | 410.11 | 7.888387 | 🔵 low — common in general English | - |
| 2855 | **ease** | 4 | 407.57 | 5.879563 | 🔵 low — common in general English | - |
| 2856 | **raise** | 5 | 407.17 | 4.699034 | 🔵 low — common in general English | - |
| 2857 | **count** | 3 | 405.59 | 7.801376 | 🔵 low — common in general English | - |
| 2858 | **bag** | 3 | 405.59 | 7.801376 | 🔵 low — common in general English | - |
| 2859 | **automatically** | 3 | 405.59 | 7.801376 | 🔵 low — common in general English | - |
| 2860 | **visited** | 3 | 405.59 | 7.801376 | 🔵 low — common in general English | - |
| 2861 | **fellow** | 3 | 405.59 | 7.801376 | 🔵 low — common in general English | - |
| 2862 | **moving** | 4 | 405.08 | 5.843631 | 🔵 low — common in general English | - |
| 2863 | **warned** | 4 | 405.08 | 5.843631 | 🔵 low — common in general English | - |
| 2864 | **deal** | 5 | 404.61 | 4.669511 | 🔵 low — common in general English | deal, deals |
| 2865 | **quickly** | 4 | 403.46 | 5.820374 | 🔵 low — common in general English | - |
| 2866 | **feed** | 4 | 402.67 | 5.808946 | 🔵 low — common in general English | - |
| 2867 | **resulting** | 4 | 401.89 | 5.797646 | 🔵 low — common in general English | - |
| 2868 | **merge** | 4 | 401.89 | 5.797646 | 🔵 low — common in general English | - |
| 2869 | **worker** | 3 | 401.43 | 7.721333 | 🔵 low — common in general English | - |
| 2870 | **farmer** | 3 | 401.43 | 7.721333 | 🔵 low — common in general English | - |
| 2871 | **cool** | 3 | 401.43 | 7.721333 | 🔵 low — common in general English | - |
| 2872 | **authority** | 4 | 399.59 | 5.764494 | 🔵 low — common in general English | - |
| 2873 | **possibility** | 4 | 398.84 | 5.753683 | 🔵 low — common in general English | possibilities, possibility |
| 2874 | **furthermore** | 3 | 397.58 | 7.647225 | 🔵 low — common in general English | - |
| 2875 | **memory** | 3 | 397.58 | 7.647225 | 🔵 low — common in general English | - |
| 2876 | **stayed** | 3 | 397.58 | 7.647225 | 🔵 low — common in general English | - |
| 2877 | **party** | 4 | 397.37 | 5.732405 | 🔵 low — common in general English | parties, party |
| 2878 | **mass** | 3 | 393.99 | 7.578232 | 🔵 low — common in general English | - |
| 2879 | **generating** | 3 | 393.99 | 7.578232 | 🔵 low — common in general English | - |
| 2880 | **armed** | 3 | 393.99 | 7.578232 | 🔵 low — common in general English | - |
| 2881 | **responsibility** | 3 | 393.99 | 7.578232 | 🔵 low — common in general English | responsibilities, responsibility |
| 2882 | **stood** | 4 | 393.81 | 5.681112 | 🔵 low — common in general English | - |
| 2883 | **wanted** | 4 | 393.12 | 5.671162 | 🔵 low — common in general English | - |
| 2884 | **class** | 4 | 392.44 | 5.66131 | 🔵 low — common in general English | - |
| 2885 | **firmly** | 3 | 390.63 | 7.513694 | 🔵 low — common in general English | - |
| 2886 | **conjunction** | 3 | 390.63 | 7.513694 | 🔵 low — common in general English | - |
| 2887 | **mention** | 3 | 390.63 | 7.513694 | 🔵 low — common in general English | - |
| 2888 | **flood** | 3 | 390.63 | 7.513694 | 🔵 low — common in general English | - |
| 2889 | **executed** | 3 | 390.63 | 7.513694 | 🔵 low — common in general English | - |
| 2890 | **affect** | 4 | 390.43 | 5.632322 | 🔵 low — common in general English | affect, affects |
| 2891 | **formed** | 4 | 387.84 | 5.594934 | 🔵 low — common in general English | - |
| 2892 | **absorb** | 3 | 387.48 | 7.453069 | 🔵 low — common in general English | absorb, absorbs |
| 2893 | **frost** | 3 | 387.48 | 7.453069 | 🔵 low — common in general English | frost, frosts |
| 2894 | **pledge** | 3 | 387.48 | 7.453069 | 🔵 low — common in general English | - |
| 2895 | **manage** | 3 | 387.48 | 7.453069 | 🔵 low — common in general English | - |
| 2896 | **specific** | 4 | 386.58 | 5.576752 | 🔵 low — common in general English | - |
| 2897 | **route** | 3 | 384.51 | 7.395911 | 🔵 low — common in general English | route, routes |
| 2898 | **surrounding** | 3 | 384.51 | 7.395911 | 🔵 low — common in general English | - |
| 2899 | **panic** | 3 | 384.51 | 7.395911 | 🔵 low — common in general English | - |
| 2900 | **ball** | 3 | 384.51 | 7.395911 | 🔵 low — common in general English | ball, balls |
| 2901 | **topped** | 3 | 384.51 | 7.395911 | 🔵 low — common in general English | - |
| 2902 | **our** | 5 | 383.71 | 4.428349 | 🔵 low — common in general English | - |
| 2903 | **predicted** | 4 | 382.34 | 5.515598 | 🔵 low — common in general English | - |
| 2904 | **placing** | 3 | 381.70 | 7.341843 | 🔵 low — common in general English | - |
| 2905 | **removed** | 3 | 381.70 | 7.341843 | 🔵 low — common in general English | - |
| 2906 | **successive** | 3 | 381.70 | 7.341843 | 🔵 low — common in general English | - |
| 2907 | **crushing** | 3 | 381.70 | 7.341843 | 🔵 low — common in general English | - |
| 2908 | **argument** | 3 | 381.70 | 7.341843 | 🔵 low — common in general English | argument, arguments |
| 2909 | **progressive** | 3 | 381.70 | 7.341843 | 🔵 low — common in general English | - |
| 2910 | **violated** | 3 | 381.70 | 7.341843 | 🔵 low — common in general English | - |
| 2911 | **temporary** | 4 | 381.17 | 5.498791 | 🔵 low — common in general English | - |
| 2912 | **counter** | 3 | 379.03 | 7.29055 | 🔵 low — common in general English | - |
| 2913 | **specifically** | 3 | 379.03 | 7.29055 | 🔵 low — common in general English | - |
| 2914 | **quantity** | 3 | 379.03 | 7.29055 | 🔵 low — common in general English | quantities, quantity |
| 2915 | **eliminated** | 3 | 379.03 | 7.29055 | 🔵 low — common in general English | - |
| 2916 | **preventing** | 3 | 376.50 | 7.24176 | 🔵 low — common in general English | - |
| 2917 | **write** | 3 | 376.50 | 7.24176 | 🔵 low — common in general English | - |
| 2918 | **season** | 4 | 376.16 | 5.42647 | 🔵 low — common in general English | season, seasons |
| 2919 | **half** | 5 | 374.11 | 4.317575 | 🔵 low — common in general English | - |
| 2920 | **category** | 3 | 374.08 | 7.19524 | 🔵 low — common in general English | categories, category |
| 2921 | **limit** | 4 | 373.52 | 5.388443 | 🔵 low — common in general English | limit, limits |
| 2922 | **entry** | 3 | 371.77 | 7.150788 | 🔵 low — common in general English | - |
| 2923 | **picture** | 3 | 371.77 | 7.150788 | 🔵 low — common in general English | picture, pictures |
| 2924 | **associate** | 3 | 371.77 | 7.150788 | 🔵 low — common in general English | associate, associates |
| 2925 | **introduce** | 3 | 371.77 | 7.150788 | 🔵 low — common in general English | - |
| 2926 | **argue** | 3 | 369.55 | 7.108229 | 🔵 low — common in general English | - |
| 2927 | **earned** | 4 | 368.53 | 5.316469 | 🔵 low — common in general English | - |
| 2928 | **history** | 3 | 367.43 | 7.067407 | 🔵 low — common in general English | - |
| 2929 | **assume** | 3 | 365.39 | 7.028186 | 🔵 low — common in general English | - |
| 2930 | **threaten** | 3 | 365.39 | 7.028186 | 🔵 low — common in general English | - |
| 2931 | **win** | 3 | 363.43 | 6.990446 | 🔵 low — common in general English | - |
| 2932 | **secure** | 3 | 363.43 | 6.990446 | 🔵 low — common in general English | secure, secures |
| 2933 | **china** | 4 | 362.10 | 5.223687 | 🔵 low — common in general English | - |
| 2934 | **midday** | 3 | 361.54 | 6.954078 | 🔵 low — common in general English | - |
| 2935 | **subsequent** | 3 | 361.54 | 6.954078 | 🔵 low — common in general English | - |
| 2936 | **severely** | 3 | 361.54 | 6.954078 | 🔵 low — common in general English | - |
| 2937 | **early** | 5 | 361.36 | 4.17039 | 🔵 low — common in general English | - |
| 2938 | **brief** | 3 | 359.71 | 6.918987 | 🔵 low — common in general English | - |
| 2939 | **ran** | 3 | 359.71 | 6.918987 | 🔵 low — common in general English | - |
| 2940 | **send** | 3 | 359.71 | 6.918987 | 🔵 low — common in general English | - |
| 2941 | **acquire** | 5 | 359.66 | 4.150717 | 🔵 low — common in general English | acquire, acquires |
| 2942 | **local** | 4 | 358.68 | 5.174295 | 🔵 low — common in general English | - |
| 2943 | **assuming** | 3 | 357.95 | 6.885085 | 🔵 low — common in general English | - |
| 2944 | **commerce** | 4 | 356.62 | 5.144619 | 🔵 low — common in general English | - |
| 2945 | **prove** | 3 | 356.25 | 6.852295 | 🔵 low — common in general English | prove, proves |
| 2946 | **increasing** | 4 | 355.42 | 5.127227 | 🔵 low — common in general English | - |
| 2947 | **warning** | 3 | 354.60 | 6.820546 | 🔵 low — common in general English | - |
| 2948 | **proportion** | 3 | 354.60 | 6.820546 | 🔵 low — common in general English | proportion, proportions |
| 2949 | **press** | 4 | 353.84 | 5.104499 | 🔵 low — common in general English | press, presses |
| 2950 | **urge** | 3 | 353.00 | 6.789775 | 🔵 low — common in general English | urge, urges |
| 2951 | **resolution** | 3 | 353.00 | 6.789775 | 🔵 low — common in general English | - |
| 2952 | **item** | 3 | 348.47 | 6.702763 | 🔵 low — common in general English | - |
| 2953 | **floating** | 3 | 348.47 | 6.702763 | 🔵 low — common in general English | - |
| 2954 | **environment** | 3 | 348.47 | 6.702763 | 🔵 low — common in general English | - |
| 2955 | **repayment** | 3 | 348.47 | 6.702763 | 🔵 low — common in general English | - |
| 2956 | **aggressive** | 3 | 348.47 | 6.702763 | 🔵 low — common in general English | - |
| 2957 | **acting** | 3 | 348.47 | 6.702763 | 🔵 low — common in general English | - |
| 2958 | **oil** | 6 | 348.32 | 3.34994 | 🔵 low — common in general English | - |
| 2959 | **figure** | 4 | 347.87 | 5.018424 | 🔵 low — common in general English | figure, figures |
| 2960 | **company** | 8 | 347.14 | 2.503892 | 🔵 low — common in general English | - |
| 2961 | **resist** | 3 | 347.05 | 6.675364 | 🔵 low — common in general English | resist, resists |
| 2962 | **managed** | 3 | 345.66 | 6.648696 | 🔵 low — common in general English | - |
| 2963 | **changing** | 3 | 345.66 | 6.648696 | 🔵 low — common in general English | - |
| 2964 | **aware** | 3 | 345.66 | 6.648696 | 🔵 low — common in general English | - |
| 2965 | **gain** | 5 | 343.61 | 3.965514 | 🔵 low — common in general English | - |
| 2966 | **arrange** | 3 | 341.71 | 6.57271 | 🔵 low — common in general English | - |
| 2967 | **shut** | 3 | 341.71 | 6.57271 | 🔵 low — common in general English | shut, shuts |
| 2968 | **slight** | 3 | 341.71 | 6.57271 | 🔵 low — common in general English | - |
| 2969 | **suffered** | 3 | 341.71 | 6.57271 | 🔵 low — common in general English | - |
| 2970 | **joined** | 3 | 340.46 | 6.548613 | 🔵 low — common in general English | - |
| 2971 | **joint** | 4 | 338.53 | 4.883605 | 🔵 low — common in general English | - |
| 2972 | **apparent** | 3 | 338.04 | 6.502093 | 🔵 low — common in general English | - |
| 2973 | **pointed** | 3 | 338.04 | 6.502093 | 🔵 low — common in general English | - |
| 2974 | **delivered** | 3 | 336.87 | 6.47962 | 🔵 low — common in general English | - |
| 2975 | **outcome** | 3 | 336.87 | 6.47962 | 🔵 low — common in general English | - |
| 2976 | **scale** | 3 | 335.73 | 6.457641 | 🔵 low — common in general English | - |
| 2977 | **attractive** | 3 | 335.73 | 6.457641 | 🔵 low — common in general English | - |
| 2978 | **permit** | 3 | 335.73 | 6.457641 | 🔵 low — common in general English | - |
| 2979 | **adequate** | 3 | 334.61 | 6.436135 | 🔵 low — common in general English | - |
| 2980 | **favour** | 3 | 334.61 | 6.436135 | 🔵 low — common in general English | - |
| 2981 | **repeated** | 3 | 334.61 | 6.436135 | 🔵 low — common in general English | - |
| 2982 | **requested** | 3 | 333.52 | 6.415081 | 🔵 low — common in general English | - |
| 2983 | **citadel** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English | - |
| 2984 | **bounty** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English | - |
| 2985 | **savage** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English | savage, savages |
| 2986 | **hindrance** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English | hindrance, hindrances |
| 2987 | **totality** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English | - |
| 2988 | **populated** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English | - |
| 2989 | **striving** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English | - |
| 2990 | **sway** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English | - |
| 2991 | **motive** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English | - |
| 2992 | **genuinely** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English | - |
| 2993 | **draught** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English | - |
| 2994 | **encompassing** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English | - |
| 2995 | **depart** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English | depart, departs |
| 2996 | **pale** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English | - |
| 2997 | **warrior** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English | - |
| 2998 | **prison** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English | - |
| 2999 | **miserable** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English | - |
| 3000 | **meagre** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English | - |
| 3001 | **momentary** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English | - |
| 3002 | **unrelenting** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English | - |
| 3003 | **axe** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English | - |
| 3004 | **pretend** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English | - |
| 3005 | **jar** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English | - |
| 3006 | **storey** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English | storey, storeys |
| 3007 | **reviving** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English | - |
| 3008 | **screaming** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English | - |
| 3009 | **sealed** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English | - |
| 3010 | **stabbed** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English | - |
| 3011 | **cracked** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English | - |
| 3012 | **boiling** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English | - |
| 3013 | **weep** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English | weep, weeps |
| 3014 | **deceased** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English | - |
| 3015 | **rib** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English | - |
| 3016 | **hauled** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English | - |
| 3017 | **arrogant** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English | - |
| 3018 | **stuff** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English | stuff, stuffs |
| 3019 | **ploughed** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English | - |
| 3020 | **halfway** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English | - |
| 3021 | **jaw** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English | - |
| 3022 | **chew** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English | - |
| 3023 | **clutch** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English | - |
| 3024 | **burglar** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English | burglar, burglars |
| 3025 | **haven** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English | - |
| 3026 | **confer** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English | - |
| 3027 | **irresistible** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English | - |
| 3028 | **abyss** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English | - |
| 3029 | **wit** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English | - |
| 3030 | **dress** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English | - |
| 3031 | **progression** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English | - |
| 3032 | **feeble** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English | - |
| 3033 | **secretly** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English | - |
| 3034 | **prowess** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English | - |
| 3035 | **renunciation** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English | - |
| 3036 | **exposing** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English | - |
| 3037 | **observation** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English | - |
| 3038 | **bother** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English | - |
| 3039 | **creator** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English | creator, creators |
| 3040 | **abstain** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English | - |
| 3041 | **pleasantly** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English | - |
| 3042 | **respectful** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English | - |
| 3043 | **headache** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English | - |
| 3044 | **saffron** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English | - |
| 3045 | **dense** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English | - |
| 3046 | **inherit** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English | - |
| 3047 | **maturation** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English | - |
| 3048 | **corrupted** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English | - |
| 3049 | **needing** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English | - |
| 3050 | **discrimination** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English | - |
| 3051 | **rebuke** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English | - |
| 3052 | **embarrassed** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English | - |
| 3053 | **irritated** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English | - |
| 3054 | **receptive** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English | - |
| 3055 | **externally** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English | - |
| 3056 | **requisite** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English | - |
| 3057 | **invoke** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English | - |
| 3058 | **underwent** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English | - |
| 3059 | **angrily** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English | - |
| 3060 | **remembered** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English | - |
| 3061 | **melted** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English | - |
| 3062 | **distinctly** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English | - |
| 3063 | **flash** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English | - |
| 3064 | **continuity** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English | - |
| 3065 | **self-centred** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English | - |
| 3066 | **indifferent** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English | - |
| 3067 | **perished** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English | - |
| 3068 | **nurtured** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English | - |
| 3069 | **kicked** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English | - |
| 3070 | **wrecked** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English | - |
| 3071 | **avail** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English | - |
| 3072 | **chariot** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English | - |
| 3073 | **oar** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English | - |
| 3074 | **twenty-three** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English | - |
| 3075 | **doha** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English | - |
| 3076 | **engender** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English | - |
| 3077 | **fore** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English | - |
| 3078 | **dirt** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English | - |
| 3079 | **aggressor** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English | - |
| 3080 | **observing** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English | - |
| 3081 | **emptied** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English | - |
| 3082 | **beam** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English | - |
| 3083 | **vibrant** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English | - |
| 3084 | **revitalize** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English | - |
| 3085 | **guarantee** | 3 | 332.44 | 6.394462 | 🔵 low — common in general English | - |
| 3086 | **exhaustion** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3087 | **unerring** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3088 | **greatness** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3089 | **permeate** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | permeate, permeates |
| 3090 | **semblance** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3091 | **daka** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3092 | **blissful** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3093 | **eternity** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3094 | **concealed** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3095 | **upside-down** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3096 | **nomad** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3097 | **savouring** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3098 | **vina** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3099 | **tingling** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3100 | **intently** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3101 | **razor-sharp** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3102 | **tising** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3103 | **ti-reciter** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3104 | **honest** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3105 | **i-reciter** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3106 | **fruition** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3107 | **sror** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3108 | **taut** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3109 | **inwardly** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3110 | **discour** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3111 | **mealtime** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | mealtime, mealtimes |
| 3112 | **undervalue** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3113 | **disobeying** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3114 | **treating** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3115 | **iala** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | iala, ialas |
| 3116 | **disrespectful** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3117 | **barbarian** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | barbarian, barbarians |
| 3118 | **slavery** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3119 | **blankness** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3120 | **inhabiting** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3121 | **eternalist** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | eternalist, eternalists |
| 3122 | **nihilist** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | nihilist, nihilists |
| 3123 | **tenma** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3124 | **flower-garden** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3125 | **expounding** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3126 | **description** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | description, descriptions |
| 3127 | **disability** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | disabilities, disability |
| 3128 | **possessing** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3129 | **immersed** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3130 | **variance** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3131 | **prophecy** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3132 | **thonmi** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3133 | **sambhota** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3134 | **owo** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3135 | **thadul** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3136 | **yangdul** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3137 | **buddhism** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3138 | **unequalled** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3139 | **sfitra** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3140 | **ordained** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3141 | **shone** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3142 | **kind-hearted** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3143 | **delightful** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3144 | **renown** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3145 | **manifesting** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3146 | **devoid** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3147 | **quench** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3148 | **excellence** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3149 | **khu** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3150 | **ngok** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3151 | **stupidity** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3152 | **ensnared** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3153 | **guise** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3154 | **blindly** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3155 | **tinder** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3156 | **oxen** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3157 | **hither** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3158 | **thither** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3159 | **intentionally** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3160 | **hurl** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3161 | **neglect** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3162 | **indulging** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3163 | **pond** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3164 | **blaz** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3165 | **infernal** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3166 | **disintegrate** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3167 | **legion** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3168 | **wondrous** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3169 | **livelihood** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3170 | **ferociously** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3171 | **soldier** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | soldier, soldiers |
| 3172 | **breadth** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3173 | **limp** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3174 | **hide** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3175 | **filthy** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3176 | **magnificent** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3177 | **five-fold** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3178 | **nyatri** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3179 | **dynasty** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3180 | **splendour** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | splendour, splendours |
| 3181 | **prize** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3182 | **tall** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3183 | **degenerated** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3184 | **plague** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3185 | **survivor** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3186 | **preach** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3187 | **glow** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3188 | **blossom** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | blossom, blossoms |
| 3189 | **wither** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3190 | **goat** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3191 | **thunderbolt** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3192 | **fearful** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3193 | **behold** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3194 | **nausea** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3195 | **beggary** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3196 | **market-day** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3197 | **bicker** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3198 | **consecrated** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3199 | **dwelt** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3200 | **cliff** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3201 | **mandhatri** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3202 | **dandle** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3203 | **buried** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3204 | **erudite** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3205 | **talented** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3206 | **beget** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3207 | **yearn** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3208 | **aryadeva** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3209 | **crave** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3210 | **phlegm** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3211 | **skeleton** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | skeleton, skeletons |
| 3212 | **tusk** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3213 | **forgetfulness** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3214 | **transient** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3215 | **lowly** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3216 | **deathless** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3217 | **imper** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3218 | **manence** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3219 | **nirvat** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3220 | **renunciate** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | renunciate, renunciates |
| 3221 | **permeated** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3222 | **ant** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3223 | **fiery** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3224 | **brandishing** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3225 | **phantom** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3226 | **slain** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3227 | **mortar** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3228 | **ofyama** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3229 | **hell-being** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3230 | **corre** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3231 | **spond** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3232 | **rounding-up** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3233 | **howling** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3234 | **bronze** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3235 | **sciousness** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3236 | **anus** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3237 | **glowing** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3238 | **subjected** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3239 | **salmali** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3240 | **mali** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3241 | **vulture** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | vulture, vultures |
| 3242 | **hideous** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3243 | **intolerable** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3244 | **groan** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3245 | **lotus-like** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3246 | **blistering** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3247 | **yamdrok** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3248 | **tangtong** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3249 | **glance** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3250 | **venerated** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3251 | **priest** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3252 | **quivering** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3253 | **knive** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3254 | **gleam** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3255 | **lovely** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3256 | **exemplary** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3257 | **shameful** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3258 | **withered** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3259 | **moonlight** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3260 | **srot** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3261 | **yelled** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3262 | **jetari** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3263 | **repulsive** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3264 | **wandered** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3265 | **afflict** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3266 | **stinginess** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3267 | **magician** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3268 | **imaginary** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3269 | **fragment** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | fragment, fragments |
| 3270 | **tum** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3271 | **garuc** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3272 | **gun** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | gun, guns |
| 3273 | **leopard** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3274 | **milked** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3275 | **sincerity** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3276 | **dread** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3277 | **adornment** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | adornment, adornments |
| 3278 | **mule** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3279 | **strand** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | strand, strands |
| 3280 | **disembowelled** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3281 | **suffocate** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | suffocate, suffocates |
| 3282 | **ewe** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3283 | **sip** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3284 | **calve** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3285 | **stolen** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3286 | **semen** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3287 | **fetus** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3288 | **banging** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3289 | **bony** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3290 | **rubbed** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3291 | **cradle** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3292 | **ripple** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3293 | **inconsequential** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3294 | **vigour** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3295 | **irritable** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3296 | **sing** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3297 | **stalking** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3298 | **protrude** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | protrude, protrudes |
| 3299 | **faded** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3300 | **scorn** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | scorn, scorns |
| 3301 | **terrify** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | terrifies, terrify |
| 3302 | **hallucinate** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3303 | **realiz** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | realiz, realizes |
| 3304 | **descend** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3305 | **unending** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3306 | **miserliness** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3307 | **charity** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3308 | **hostility** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3309 | **cours** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3310 | **tea-leave** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3311 | **dishonour** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3312 | **splendidly** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3313 | **nourishing** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3314 | **harness** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3315 | **despair** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | despair, despairs |
| 3316 | **red-faced** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3317 | **calamity** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | calamities, calamity |
| 3318 | **collaps** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3319 | **expedition** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3320 | **slave** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | slave, slaves |
| 3321 | **degeneration** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | degeneration, degenerations |
| 3322 | **distinguishing** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3323 | **resentment** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3324 | **grabbing** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3325 | **supremely** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3326 | **suffused** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3327 | **sweat** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3328 | **ceaseless** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3329 | **cesspit** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3330 | **recollection** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3331 | **overjoyed** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3332 | **crackling** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3333 | **hell-realm** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3334 | **transgressed** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3335 | **circumambulate** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3336 | **cherish** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3337 | **excrement** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3338 | **contaminate** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3339 | **tsik** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3340 | **astray** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3341 | **predilection** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3342 | **graze** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3343 | **dung** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3344 | **lice** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3345 | **bride** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3346 | **gobble** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | gobble, gobbles |
| 3347 | **smacking** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3348 | **muzzle** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3349 | **ceas** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3350 | **staring** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3351 | **skinned** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3352 | **all-pervading** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3353 | **stove** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3354 | **stealth** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3355 | **clos** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3356 | **obsession** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | obsession, obsessions |
| 3357 | **brooding** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3358 | **charlatan** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3359 | **behaving** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3360 | **flaw** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3361 | **offensively** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3362 | **singing** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3363 | **distracting** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3364 | **chanting** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3365 | **partake** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3366 | **sixty-two** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3367 | **downhill** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3368 | **sharpness** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3369 | **giver** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | giver, givers |
| 3370 | **nourishment** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3371 | **sustenance** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3372 | **defile** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3373 | **impulse** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3374 | **affinity** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3375 | **respite** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3376 | **disperse** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3377 | **impoverished** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3378 | **spouse** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3379 | **chore** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | chore, chores |
| 3380 | **reaping** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3381 | **insulted** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3382 | **denigrate** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | denigrate, denigrates |
| 3383 | **ravine** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3384 | **massacred** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3385 | **parivrajika** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3386 | **shrine** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3387 | **nirvar** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3388 | **kashmir** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3389 | **dyeing** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3390 | **sire** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3391 | **thief** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3392 | **kusa** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3393 | **disparage** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | disparage, disparages |
| 3394 | **ashota** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3395 | **scolded** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3396 | **serpent** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3397 | **rivalry** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3398 | **pratimo** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3399 | **stained** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3400 | **conversely** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3401 | **goodness** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3402 | **ofvajradhara** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3403 | **me-but** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3404 | **firstly** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3405 | **sastra** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | sastra, sastras |
| 3406 | **tripitaka** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3407 | **riddance** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3408 | **pitaka** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3409 | **ripening** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3410 | **tered** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3411 | **fief** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3412 | **puffed** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3413 | **bogus** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3414 | **unthinkingly** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3415 | **attuned** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3416 | **patiently** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3417 | **disci** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3418 | **radiate** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3419 | **simile** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3420 | **sparing** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3421 | **displeasing** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3422 | **anvil** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3423 | **sweeper** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3424 | **drank** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3425 | **mara** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3426 | **respectfully** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3427 | **paramount** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3428 | **indivisibly** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3429 | **obeying** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3430 | **profess** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3431 | **profundity** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | profundities, profundity |
| 3432 | **pretending** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3433 | **superfluous** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3434 | **rongton** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3435 | **lhaga** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3436 | **trowolung** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3437 | **imitation** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3438 | **engraved** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3439 | **wasteland** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3440 | **paramita** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3441 | **venerate** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3442 | **crossroad** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3443 | **thigh** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3444 | **preaching** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3445 | **filigree** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | filigree, filigrees |
| 3446 | **lapi** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3447 | **lazuli** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3448 | **maiden** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3449 | **proclaim** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | proclaim, proclaims |
| 3450 | **nine-storey** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3451 | **bamboo** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3452 | **toe** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3453 | **labourer** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3454 | **twenty-four** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3455 | **obscura** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3456 | **awakened** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3457 | **disobey** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3458 | **vikramasila** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3459 | **hailstorm** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | hailstorm, hailstorms |
| 3460 | **yungton** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3461 | **jug** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3462 | **sariwara** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3463 | **shepa** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3464 | **drowning** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3465 | **entrance-way** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3466 | **vivid** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3467 | **relic** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3468 | **kongpo** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3469 | **wick** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | wick, wicks |
| 3470 | **five-pronged** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3471 | **hooked** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3472 | **hadra** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3473 | **rabjampa** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3474 | **on-and** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3475 | **avalokitesvara-and** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3476 | **rear** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3477 | **encased** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3478 | **vowel** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | vowel, vowels |
| 3479 | **sugata** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3480 | **yearning** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3481 | **visnu** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3482 | **springing** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3483 | **glare** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3484 | **hid** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3485 | **manifested** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3486 | **fourfold** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3487 | **paqc** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3488 | **painting** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | painting, paintings |
| 3489 | **vairocana** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3490 | **beneficent** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3491 | **ajatasatru** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3492 | **fury** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3493 | **scoop** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3494 | **enlight** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3495 | **enment** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3496 | **lovingly** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3497 | **jarung** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3498 | **khashor** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3499 | **gentle** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3500 | **despised** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3501 | **summoning** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3502 | **dungeon** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3503 | **packhors** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3504 | **pain-you** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3505 | **panting** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3506 | **thrash** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3507 | **atsara** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3508 | **relishing** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3509 | **faint** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3510 | **marching** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3511 | **religion** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3512 | **paq** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3513 | **altruistic** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3514 | **lungpa** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3515 | **lhungpa** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3516 | **thenceforth** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3517 | **vasubandhu** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3518 | **departed** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3519 | **feather** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3520 | **unkind** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3521 | **pletely** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3522 | **tarlo** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3523 | **mistress** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3524 | **swim** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3525 | **shawopa** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3526 | **imponant** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3527 | **conceived** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3528 | **eighty-four** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3529 | **harnessed** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3530 | **belonged** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3531 | **jeweller** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3532 | **ancestor** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3533 | **hem** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3534 | **exquisite** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3535 | **fist** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | fist, fists |
| 3536 | **chakshingwa** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3537 | **shangshungpa** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3538 | **feverish** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3539 | **manicuda** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3540 | **dawned** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3541 | **bathed** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3542 | **brighu** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3543 | **sprang** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3544 | **duly** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3545 | **dharani** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | dharani, dharanis |
| 3546 | **tigress** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3547 | **laced** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3548 | **ego** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3549 | **craving** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | craving, cravings |
| 3550 | **yourselve** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3551 | **armour-like** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3552 | **preoccupation** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3553 | **diparhkara** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3554 | **childish** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3555 | **distrac** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3556 | **lonely** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3557 | **secluded** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3558 | **ascetic** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3559 | **discerning** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3560 | **concen** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3561 | **tration** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3562 | **athagata** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3563 | **equanimity** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3564 | **analysi** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3565 | **spoilt** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3566 | **transcend** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | transcend, transcends |
| 3567 | **self-liberation** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3568 | **saraha** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3569 | **kharak** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3570 | **gomchung** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3571 | **demonic** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3572 | **spiritually** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3573 | **nachung** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3574 | **non-buddhist** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3575 | **diminution** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3576 | **small-minded** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3577 | **cultivating** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3578 | **hiding** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3579 | **chagme** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3580 | **necklace** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | necklace, necklaces |
| 3581 | **perverse** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3582 | **venge** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3583 | **orna** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3584 | **appeased** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3585 | **navel** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3586 | **conch** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | conch, conches |
| 3587 | **light-ray** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3588 | **shapkyu** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3589 | **crescent** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3590 | **bindu** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3591 | **nada** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3592 | **ofvajrasattva** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3593 | **cymbal** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3594 | **prayer-book** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | prayer-book, prayer-books |
| 3595 | **transgressor** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3596 | **shingkyong** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3597 | **tation** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3598 | **sullied** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3599 | **snivaka** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3600 | **gifted** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3601 | **surround** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3602 | **rime** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | rime, rimes |
| 3603 | **underside** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | underside, undersides |
| 3604 | **clockwise** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3605 | **multiplying** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3606 | **multiplied** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3607 | **cleanly** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3608 | **churning** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3609 | **propitiating** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3610 | **ascending** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3611 | **eyebrow** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3612 | **brow** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | brow, brows |
| 3613 | **seventy-five** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3614 | **imbibe** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3615 | **iakini** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3616 | **tara** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3617 | **boast** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | boast, boasts |
| 3618 | **elemental** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3619 | **fearsome** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3620 | **annihilate** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3621 | **prophesied** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3622 | **goblin** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3623 | **dualistic** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3624 | **core-teaching** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3625 | **fervent** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3626 | **drikung** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3627 | **kyobpa** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3628 | **intellect** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | intellect, intellects |
| 3629 | **trekcho** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3630 | **gazing** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3631 | **longingly** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3632 | **skull-drum** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3633 | **charnel-ground** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3634 | **zahor** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3635 | **symbolizing** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3636 | **mudra** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3637 | **sambhoga** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3638 | **five-coloured** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3639 | **subjugated** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3640 | **luminous** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3641 | **sphere** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3642 | **knee** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3643 | **unfathomable** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3644 | **hypocrisy** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3645 | **intending** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3646 | **entreat** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3647 | **upayoga** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3648 | **mahayoga** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3649 | **anuyoga** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3650 | **ofg** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3651 | **reat** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3652 | **lotus-born** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3653 | **ruby** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | rubies, ruby |
| 3654 | **muni** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3655 | **twenty-eight** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3656 | **vajrapat** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3657 | **dhanakosa** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3658 | **sattvavajra** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3659 | **nine-pointed** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3660 | **expans** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3661 | **rajahasti** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3662 | **paqqita** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | paqqita, paqqitas |
| 3663 | **yamantaka** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3664 | **acarya** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3665 | **non-human** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | non-human, non-humans |
| 3666 | **genyen** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3667 | **treasure-discoverer** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | treasure-discoverer, treasure-discoverers |
| 3668 | **familiarity** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3669 | **mahamudra** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3670 | **ofvajra** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3671 | **yogini** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3672 | **enclosure** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3673 | **vibrating** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3674 | **mind-awareness** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3675 | **kyabje** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3676 | **kagyu** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3677 | **gampopa** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3678 | **instruc** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3679 | **phras** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3680 | **drunk** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3681 | **wangpo** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - |
| 3682 | **concerning** | 3 | 331.39 | 6.374259 | 🔵 low — common in general English | - |
| 3683 | **seriously** | 3 | 331.39 | 6.374259 | 🔵 low — common in general English | - |
| 3684 | **continued** | 4 | 329.74 | 4.756853 | 🔵 low — common in general English | - |
| 3685 | **band** | 3 | 329.36 | 6.335039 | 🔵 low — common in general English | - |
| 3686 | **directly** | 3 | 329.36 | 6.335039 | 🔵 low — common in general English | - |
| 3687 | **chinese** | 3 | 328.36 | 6.31599 | 🔵 low — common in general English | - |
| 3688 | **delay** | 3 | 327.39 | 6.297298 | 🔵 low — common in general English | - |
| 3689 | **detailed** | 3 | 327.39 | 6.297298 | 🔵 low — common in general English | - |
| 3690 | **island** | 3 | 326.44 | 6.278949 | 🔵 low — common in general English | - |
| 3691 | **account** | 4 | 325.99 | 4.702786 | 🔵 low — common in general English | account, accounts |
| 3692 | **broad** | 3 | 325.50 | 6.260931 | 🔵 low — common in general English | - |
| 3693 | **hostile** | 3 | 325.50 | 6.260931 | 🔵 low — common in general English | - |
| 3694 | **debate** | 3 | 325.50 | 6.260931 | 🔵 low — common in general English | - |
| 3695 | **status** | 3 | 324.58 | 6.243231 | 🔵 low — common in general English | - |
| 3696 | **closely** | 3 | 321.92 | 6.191938 | 🔵 low — common in general English | - |
| 3697 | **test** | 3 | 321.92 | 6.191938 | 🔵 low — common in general English | - |
| 3698 | **community** | 4 | 321.70 | 4.640835 | 🔵 low — common in general English | communities, community |
| 3699 | **adopted** | 3 | 319.38 | 6.143148 | 🔵 low — common in general English | - |
| 3700 | **sheet** | 3 | 319.38 | 6.143148 | 🔵 low — common in general English | - |
| 3701 | **trader** | 3 | 319.38 | 6.143148 | 🔵 low — common in general English | trader, traders |
| 3702 | **raised** | 4 | 318.59 | 4.595923 | 🔵 low — common in general English | - |
| 3703 | **prescription** | 2 | 318.44 | 9.18767 | 🔵 low — common in general English | - |
| 3704 | **excel** | 2 | 318.44 | 9.18767 | 🔵 low — common in general English | - |
| 3705 | **propensity** | 2 | 318.44 | 9.18767 | 🔵 low — common in general English | - |
| 3706 | **younger** | 2 | 318.44 | 9.18767 | 🔵 low — common in general English | - |
| 3707 | **monarch** | 2 | 318.44 | 9.18767 | 🔵 low — common in general English | monarch, monarchs |
| 3708 | **festival** | 2 | 318.44 | 9.18767 | 🔵 low — common in general English | - |
| 3709 | **embraced** | 2 | 318.44 | 9.18767 | 🔵 low — common in general English | - |
| 3710 | **inheritance** | 2 | 318.44 | 9.18767 | 🔵 low — common in general English | - |
| 3711 | **wounded** | 2 | 318.44 | 9.18767 | 🔵 low — common in general English | - |
| 3712 | **misguided** | 2 | 318.44 | 9.18767 | 🔵 low — common in general English | - |
| 3713 | **rotting** | 2 | 318.44 | 9.18767 | 🔵 low — common in general English | - |
| 3714 | **trickle** | 2 | 318.44 | 9.18767 | 🔵 low — common in general English | - |
| 3715 | **misuse** | 2 | 318.44 | 9.18767 | 🔵 low — common in general English | - |
| 3716 | **revealing** | 2 | 318.44 | 9.18767 | 🔵 low — common in general English | - |
| 3717 | **flew** | 2 | 318.44 | 9.18767 | 🔵 low — common in general English | - |
| 3718 | **bury** | 2 | 318.44 | 9.18767 | 🔵 low — common in general English | buries, bury |
| 3719 | **exploited** | 2 | 318.44 | 9.18767 | 🔵 low — common in general English | - |
| 3720 | **pulling** | 2 | 318.44 | 9.18767 | 🔵 low — common in general English | - |
| 3721 | **wasting** | 2 | 318.44 | 9.18767 | 🔵 low — common in general English | - |
| 3722 | **frightened** | 2 | 318.44 | 9.18767 | 🔵 low — common in general English | - |
| 3723 | **uproot** | 2 | 318.44 | 9.18767 | 🔵 low — common in general English | - |
| 3724 | **subside** | 2 | 318.44 | 9.18767 | 🔵 low — common in general English | subside, subsides |
| 3725 | **monkey** | 2 | 318.44 | 9.18767 | 🔵 low — common in general English | - |
| 3726 | **echo** | 2 | 318.44 | 9.18767 | 🔵 low — common in general English | - |
| 3727 | **empty-handed** | 2 | 318.44 | 9.18767 | 🔵 low — common in general English | - |
| 3728 | **prosper** | 2 | 318.44 | 9.18767 | 🔵 low — common in general English | - |
| 3729 | **painted** | 2 | 318.44 | 9.18767 | 🔵 low — common in general English | - |
| 3730 | **confessed** | 2 | 318.44 | 9.18767 | 🔵 low — common in general English | - |
| 3731 | **childhood** | 2 | 318.44 | 9.18767 | 🔵 low — common in general English | - |
| 3732 | **falcon** | 2 | 318.44 | 9.18767 | 🔵 low — common in general English | falcon, falcons |
| 3733 | **fade** | 2 | 318.44 | 9.18767 | 🔵 low — common in general English | - |
| 3734 | **needy** | 2 | 318.44 | 9.18767 | 🔵 low — common in general English | - |
| 3735 | **beset** | 2 | 318.44 | 9.18767 | 🔵 low — common in general English | - |
| 3736 | **pen** | 2 | 318.44 | 9.18767 | 🔵 low — common in general English | - |
| 3737 | **secondly** | 2 | 318.44 | 9.18767 | 🔵 low — common in general English | - |
| 3738 | **lifeline** | 2 | 318.44 | 9.18767 | 🔵 low — common in general English | - |
| 3739 | **embodied** | 2 | 318.44 | 9.18767 | 🔵 low — common in general English | - |
| 3740 | **disregard** | 2 | 318.44 | 9.18767 | 🔵 low — common in general English | - |
| 3741 | **dressed** | 2 | 318.44 | 9.18767 | 🔵 low — common in general English | - |
| 3742 | **richer** | 2 | 318.44 | 9.18767 | 🔵 low — common in general English | - |
| 3743 | **tamed** | 2 | 318.44 | 9.18767 | 🔵 low — common in general English | - |
| 3744 | **motivate** | 2 | 318.44 | 9.18767 | 🔵 low — common in general English | - |
| 3745 | **rounded** | 2 | 318.44 | 9.18767 | 🔵 low — common in general English | - |
| 3746 | **seventeen** | 2 | 318.44 | 9.18767 | 🔵 low — common in general English | - |
| 3747 | **incredible** | 2 | 318.44 | 9.18767 | 🔵 low — common in general English | - |
| 3748 | **subdue** | 2 | 318.44 | 9.18767 | 🔵 low — common in general English | subdue, subdues |
| 3749 | **wrongdoing** | 2 | 318.44 | 9.18767 | 🔵 low — common in general English | - |
| 3750 | **bite** | 2 | 318.44 | 9.18767 | 🔵 low — common in general English | - |
| 3751 | **sentence** | 2 | 318.44 | 9.18767 | 🔵 low — common in general English | - |
| 3752 | **occupation** | 2 | 318.44 | 9.18767 | 🔵 low — common in general English | occupation, occupations |
| 3753 | **liked** | 2 | 318.44 | 9.18767 | 🔵 low — common in general English | - |
| 3754 | **invalid** | 2 | 318.44 | 9.18767 | 🔵 low — common in general English | - |
| 3755 | **obscured** | 2 | 318.44 | 9.18767 | 🔵 low — common in general English | - |
| 3756 | **entirety** | 2 | 318.44 | 9.18767 | 🔵 low — common in general English | - |
| 3757 | **trained** | 2 | 318.44 | 9.18767 | 🔵 low — common in general English | - |
| 3758 | **flattened** | 2 | 318.44 | 9.18767 | 🔵 low — common in general English | - |
| 3759 | **owe** | 2 | 318.44 | 9.18767 | 🔵 low — common in general English | - |
| 3760 | **vengeance** | 2 | 318.44 | 9.18767 | 🔵 low — common in general English | - |
| 3761 | **spiralling** | 2 | 318.44 | 9.18767 | 🔵 low — common in general English | - |
| 3762 | **hence** | 2 | 318.44 | 9.18767 | 🔵 low — common in general English | - |
| 3763 | **narrow** | 3 | 316.96 | 6.096628 | 🔵 low — common in general English | - |
| 3764 | **wholly** | 3 | 313.16 | 6.023602 | 🔵 low — common in general English | - |
| 3765 | **acquiring** | 3 | 311.72 | 5.995823 | 🔵 low — common in general English | - |
| 3766 | **introduced** | 3 | 311.72 | 5.995823 | 🔵 low — common in general English | - |
| 3767 | **requirement** | 3 | 310.31 | 5.968794 | 🔵 low — common in general English | - |
| 3768 | **granted** | 3 | 310.31 | 5.968794 | 🔵 low — common in general English | - |
| 3769 | **earlier** | 5 | 310.05 | 3.578198 | 🔵 low — common in general English | - |
| 3770 | **encourage** | 3 | 309.63 | 5.955549 | 🔵 low — common in general English | - |
| 3771 | **intended** | 3 | 309.63 | 5.955549 | 🔵 low — common in general English | - |
| 3772 | **unaware** | 2 | 308.47 | 8.899988 | 🔵 low — common in general English | - |
| 3773 | **ignoring** | 2 | 308.47 | 8.899988 | 🔵 low — common in general English | - |
| 3774 | **tense** | 2 | 308.47 | 8.899988 | 🔵 low — common in general English | - |
| 3775 | **mode** | 2 | 308.47 | 8.899988 | 🔵 low — common in general English | mode, modes |
| 3776 | **geographically** | 2 | 308.47 | 8.899988 | 🔵 low — common in general English | - |
| 3777 | **rarely** | 2 | 308.47 | 8.899988 | 🔵 low — common in general English | - |
| 3778 | **strenuous** | 2 | 308.47 | 8.899988 | 🔵 low — common in general English | - |
| 3779 | **swimming** | 2 | 308.47 | 8.899988 | 🔵 low — common in general English | - |
| 3780 | **deliberate** | 2 | 308.47 | 8.899988 | 🔵 low — common in general English | - |
| 3781 | **pursuit** | 2 | 308.47 | 8.899988 | 🔵 low — common in general English | - |
| 3782 | **blizzard** | 2 | 308.47 | 8.899988 | 🔵 low — common in general English | blizzard, blizzards |
| 3783 | **derive** | 2 | 308.47 | 8.899988 | 🔵 low — common in general English | - |
| 3784 | **slice** | 2 | 308.47 | 8.899988 | 🔵 low — common in general English | - |
| 3785 | **grease** | 2 | 308.47 | 8.899988 | 🔵 low — common in general English | - |
| 3786 | **encountering** | 2 | 308.47 | 8.899988 | 🔵 low — common in general English | - |
| 3787 | **ploughing** | 2 | 308.47 | 8.899988 | 🔵 low — common in general English | - |
| 3788 | **digest** | 2 | 308.47 | 8.899988 | 🔵 low — common in general English | - |
| 3789 | **dim** | 2 | 308.47 | 8.899988 | 🔵 low — common in general English | dim, dims |
| 3790 | **appetite** | 2 | 308.47 | 8.899988 | 🔵 low — common in general English | - |
| 3791 | **carcass** | 2 | 308.47 | 8.899988 | 🔵 low — common in general English | - |
| 3792 | **forceful** | 2 | 308.47 | 8.899988 | 🔵 low — common in general English | - |
| 3793 | **eradicated** | 2 | 308.47 | 8.899988 | 🔵 low — common in general English | - |
| 3794 | **rift** | 2 | 308.47 | 8.899988 | 🔵 low — common in general English | - |
| 3795 | **donation** | 2 | 308.47 | 8.899988 | 🔵 low — common in general English | - |
| 3796 | **excuse** | 2 | 308.47 | 8.899988 | 🔵 low — common in general English | - |
| 3797 | **donor** | 2 | 308.47 | 8.899988 | 🔵 low — common in general English | - |
| 3798 | **muddy** | 2 | 308.47 | 8.899988 | 🔵 low — common in general English | - |
| 3799 | **diversity** | 2 | 308.47 | 8.899988 | 🔵 low — common in general English | - |
| 3800 | **handed** | 2 | 308.47 | 8.899988 | 🔵 low — common in general English | - |
| 3801 | **hay** | 2 | 308.47 | 8.899988 | 🔵 low — common in general English | - |
| 3802 | **permissible** | 2 | 308.47 | 8.899988 | 🔵 low — common in general English | - |
| 3803 | **impress** | 2 | 308.47 | 8.899988 | 🔵 low — common in general English | - |
| 3804 | **disturbed** | 2 | 308.47 | 8.899988 | 🔵 low — common in general English | - |
| 3805 | **checked** | 2 | 308.47 | 8.899988 | 🔵 low — common in general English | - |
| 3806 | **absorption** | 2 | 308.47 | 8.899988 | 🔵 low — common in general English | - |
| 3807 | **extraordinarily** | 2 | 308.47 | 8.899988 | 🔵 low — common in general English | - |
| 3808 | **constrained** | 2 | 308.47 | 8.899988 | 🔵 low — common in general English | - |
| 3809 | **uncovered** | 2 | 308.47 | 8.899988 | 🔵 low — common in general English | - |
| 3810 | **sausage** | 2 | 308.47 | 8.899988 | 🔵 low — common in general English | - |
| 3811 | **ingredient** | 2 | 308.47 | 8.899988 | 🔵 low — common in general English | ingredient, ingredients |
| 3812 | **witness** | 2 | 308.47 | 8.899988 | 🔵 low — common in general English | witness, witnesses |
| 3813 | **vain** | 2 | 308.47 | 8.899988 | 🔵 low — common in general English | - |
| 3814 | **contamination** | 2 | 308.47 | 8.899988 | 🔵 low — common in general English | - |
| 3815 | **sow** | 2 | 308.47 | 8.899988 | 🔵 low — common in general English | - |
| 3816 | **blend** | 2 | 308.47 | 8.899988 | 🔵 low — common in general English | - |
| 3817 | **unity** | 2 | 308.47 | 8.899988 | 🔵 low — common in general English | - |
| 3818 | **satisfying** | 2 | 308.47 | 8.899988 | 🔵 low — common in general English | - |
| 3819 | **bend** | 2 | 308.47 | 8.899988 | 🔵 low — common in general English | - |
| 3820 | **successful** | 3 | 307.61 | 5.916835 | 🔵 low — common in general English | - |
| 3821 | **consideration** | 3 | 306.31 | 5.891833 | 🔵 low — common in general English | consideration, considerations |
| 3822 | **effective** | 4 | 305.99 | 4.414165 | 🔵 low — common in general English | - |
| 3823 | **suspended** | 3 | 305.05 | 5.867442 | 🔵 low — common in general English | - |
| 3824 | **post** | 3 | 305.05 | 5.867442 | 🔵 low — common in general English | - |
| 3825 | **interested** | 3 | 304.42 | 5.855466 | 🔵 low — common in general English | - |
| 3826 | **controlled** | 3 | 303.20 | 5.831935 | 🔵 low — common in general English | - |
| 3827 | **identifying** | 2 | 300.74 | 8.676844 | 🔵 low — common in general English | - |
| 3828 | **hunting** | 2 | 300.74 | 8.676844 | 🔵 low — common in general English | - |
| 3829 | **reward** | 2 | 300.74 | 8.676844 | 🔵 low — common in general English | - |
| 3830 | **dissatisfaction** | 2 | 300.74 | 8.676844 | 🔵 low — common in general English | - |
| 3831 | **prestige** | 2 | 300.74 | 8.676844 | 🔵 low — common in general English | - |
| 3832 | **balancing** | 2 | 300.74 | 8.676844 | 🔵 low — common in general English | - |
| 3833 | **shrink** | 2 | 300.74 | 8.676844 | 🔵 low — common in general English | - |
| 3834 | **shorter** | 2 | 300.74 | 8.676844 | 🔵 low — common in general English | - |
| 3835 | **confronted** | 2 | 300.74 | 8.676844 | 🔵 low — common in general English | - |
| 3836 | **captured** | 2 | 300.74 | 8.676844 | 🔵 low — common in general English | - |
| 3837 | **relieved** | 2 | 300.74 | 8.676844 | 🔵 low — common in general English | - |
| 3838 | **corner** | 2 | 300.74 | 8.676844 | 🔵 low — common in general English | corner, corners |
| 3839 | **mere** | 2 | 300.74 | 8.676844 | 🔵 low — common in general English | - |
| 3840 | **somehow** | 2 | 300.74 | 8.676844 | 🔵 low — common in general English | - |
| 3841 | **anyway** | 2 | 300.74 | 8.676844 | 🔵 low — common in general English | - |
| 3842 | **freely** | 2 | 300.74 | 8.676844 | 🔵 low — common in general English | - |
| 3843 | **resemble** | 2 | 300.74 | 8.676844 | 🔵 low — common in general English | - |
| 3844 | **rushed** | 2 | 300.74 | 8.676844 | 🔵 low — common in general English | - |
| 3845 | **prediction** | 2 | 300.74 | 8.676844 | 🔵 low — common in general English | - |
| 3846 | **travelled** | 2 | 300.74 | 8.676844 | 🔵 low — common in general English | - |
| 3847 | **closest** | 2 | 300.74 | 8.676844 | 🔵 low — common in general English | - |
| 3848 | **unfavourable** | 2 | 300.74 | 8.676844 | 🔵 low — common in general English | - |
| 3849 | **overwhelming** | 2 | 300.74 | 8.676844 | 🔵 low — common in general English | - |
| 3850 | **voyage** | 2 | 300.74 | 8.676844 | 🔵 low — common in general English | voyage, voyages |
| 3851 | **alongside** | 2 | 300.74 | 8.676844 | 🔵 low — common in general English | - |
| 3852 | **stopping** | 2 | 300.74 | 8.676844 | 🔵 low — common in general English | - |
| 3853 | **sunbeam** | 2 | 300.74 | 8.676844 | 🔵 low — common in general English | sunbeam, sunbeams |
| 3854 | **guiding** | 2 | 300.74 | 8.676844 | 🔵 low — common in general English | - |
| 3855 | **failure** | 3 | 299.69 | 5.764494 | 🔵 low — common in general English | - |
| 3856 | **concerned** | 3 | 298.02 | 5.732405 | 🔵 low — common in general English | - |
| 3857 | **their** | 5 | 298.02 | 3.439339 | 🔵 low — common in general English | - |
| 3858 | **preceded** | 2 | 294.42 | 8.494523 | 🔵 low — common in general English | - |
| 3859 | **freeing** | 2 | 294.42 | 8.494523 | 🔵 low — common in general English | - |
| 3860 | **fragile** | 2 | 294.42 | 8.494523 | 🔵 low — common in general English | - |
| 3861 | **chose** | 2 | 294.42 | 8.494523 | 🔵 low — common in general English | - |
| 3862 | **paradise** | 2 | 294.42 | 8.494523 | 🔵 low — common in general English | - |
| 3863 | **separation** | 2 | 294.42 | 8.494523 | 🔵 low — common in general English | - |
| 3864 | **collect** | 2 | 294.42 | 8.494523 | 🔵 low — common in general English | - |
| 3865 | **leap** | 2 | 294.42 | 8.494523 | 🔵 low — common in general English | - |
| 3866 | **stranded** | 2 | 294.42 | 8.494523 | 🔵 low — common in general English | - |
| 3867 | **drift** | 2 | 294.42 | 8.494523 | 🔵 low — common in general English | - |
| 3868 | **pinpoint** | 2 | 294.42 | 8.494523 | 🔵 low — common in general English | - |
| 3869 | **addressed** | 2 | 294.42 | 8.494523 | 🔵 low — common in general English | - |
| 3870 | **reinforce** | 2 | 294.42 | 8.494523 | 🔵 low — common in general English | - |
| 3871 | **cell** | 2 | 294.42 | 8.494523 | 🔵 low — common in general English | - |
| 3872 | **dis** | 2 | 294.42 | 8.494523 | 🔵 low — common in general English | - |
| 3873 | **donated** | 2 | 294.42 | 8.494523 | 🔵 low — common in general English | - |
| 3874 | **liable** | 2 | 294.42 | 8.494523 | 🔵 low — common in general English | - |
| 3875 | **matured** | 2 | 294.42 | 8.494523 | 🔵 low — common in general English | - |
| 3876 | **sailing** | 2 | 294.42 | 8.494523 | 🔵 low — common in general English | - |
| 3877 | **fulfilling** | 2 | 294.42 | 8.494523 | 🔵 low — common in general English | - |
| 3878 | **mad** | 2 | 294.42 | 8.494523 | 🔵 low — common in general English | - |
| 3879 | **survival** | 2 | 294.42 | 8.494523 | 🔵 low — common in general English | - |
| 3880 | **forgiveness** | 2 | 294.42 | 8.494523 | 🔵 low — common in general English | - |
| 3881 | **vigorous** | 2 | 294.42 | 8.494523 | 🔵 low — common in general English | - |
| 3882 | **rough** | 2 | 294.42 | 8.494523 | 🔵 low — common in general English | - |
| 3883 | **benefiting** | 2 | 294.42 | 8.494523 | 🔵 low — common in general English | - |
| 3884 | **bud** | 2 | 294.42 | 8.494523 | 🔵 low — common in general English | - |
| 3885 | **whichever** | 2 | 294.42 | 8.494523 | 🔵 low — common in general English | - |
| 3886 | **sam** | 2 | 294.42 | 8.494523 | 🔵 low — common in general English | - |
| 3887 | **soften** | 2 | 294.42 | 8.494523 | 🔵 low — common in general English | - |
| 3888 | **foremost** | 2 | 294.42 | 8.494523 | 🔵 low — common in general English | - |
| 3889 | **agree** | 3 | 293.82 | 5.651553 | 🔵 low — common in general English | - |
| 3890 | **equivalent** | 3 | 292.82 | 5.632322 | 🔵 low — common in general English | - |
| 3891 | **normal** | 3 | 292.33 | 5.622843 | 🔵 low — common in general English | - |
| 3892 | **system** | 4 | 291.58 | 4.206349 | 🔵 low — common in general English | system, systems |
| 3893 | **completion** | 3 | 289.93 | 5.576752 | 🔵 low — common in general English | - |
| 3894 | **dispute** | 3 | 289.47 | 5.567784 | 🔵 low — common in general English | dispute, disputes |
| 3895 | **opened** | 3 | 289.47 | 5.567784 | 🔵 low — common in general English | - |
| 3896 | **sold** | 4 | 289.09 | 4.17039 | 🔵 low — common in general English | - |
| 3897 | **subdued** | 2 | 289.07 | 8.340372 | 🔵 low — common in general English | - |
| 3898 | **valuable** | 2 | 289.07 | 8.340372 | 🔵 low — common in general English | valuable, valuables |
| 3899 | **patch** | 2 | 289.07 | 8.340372 | 🔵 low — common in general English | patch, patches |
| 3900 | **seized** | 2 | 289.07 | 8.340372 | 🔵 low — common in general English | - |
| 3901 | **observed** | 2 | 289.07 | 8.340372 | 🔵 low — common in general English | - |
| 3902 | **patient** | 2 | 289.07 | 8.340372 | 🔵 low — common in general English | - |
| 3903 | **hired** | 2 | 289.07 | 8.340372 | 🔵 low — common in general English | - |
| 3904 | **anybody** | 2 | 289.07 | 8.340372 | 🔵 low — common in general English | - |
| 3905 | **tate** | 2 | 289.07 | 8.340372 | 🔵 low — common in general English | - |
| 3906 | **abundant** | 2 | 289.07 | 8.340372 | 🔵 low — common in general English | - |
| 3907 | **style** | 2 | 289.07 | 8.340372 | 🔵 low — common in general English | - |
| 3908 | **requesting** | 2 | 289.07 | 8.340372 | 🔵 low — common in general English | - |
| 3909 | **reflected** | 3 | 289.00 | 5.558895 | 🔵 low — common in general English | - |
| 3910 | **unconditional** | 2 | 284.45 | 8.206841 | 🔵 low — common in general English | - |
| 3911 | **consult** | 2 | 284.45 | 8.206841 | 🔵 low — common in general English | - |
| 3912 | **influenced** | 2 | 284.45 | 8.206841 | 🔵 low — common in general English | - |
| 3913 | **geography** | 2 | 284.45 | 8.206841 | 🔵 low — common in general English | - |
| 3914 | **existed** | 2 | 284.45 | 8.206841 | 🔵 low — common in general English | - |
| 3915 | **older** | 2 | 284.45 | 8.206841 | 🔵 low — common in general English | - |
| 3916 | **struggle** | 2 | 284.45 | 8.206841 | 🔵 low — common in general English | - |
| 3917 | **cheating** | 2 | 284.45 | 8.206841 | 🔵 low — common in general English | - |
| 3918 | **peg** | 2 | 284.45 | 8.206841 | 🔵 low — common in general English | - |
| 3919 | **lined** | 2 | 284.45 | 8.206841 | 🔵 low — common in general English | - |
| 3920 | **helpful** | 2 | 284.45 | 8.206841 | 🔵 low — common in general English | - |
| 3921 | **abandoning** | 2 | 284.45 | 8.206841 | 🔵 low — common in general English | - |
| 3922 | **relax** | 2 | 284.45 | 8.206841 | 🔵 low — common in general English | - |
| 3923 | **unique** | 2 | 284.45 | 8.206841 | 🔵 low — common in general English | - |
| 3924 | **tug** | 2 | 284.45 | 8.206841 | 🔵 low — common in general English | tug, tugs |
| 3925 | **undoubtedly** | 2 | 284.45 | 8.206841 | 🔵 low — common in general English | - |
| 3926 | **released** | 3 | 284.17 | 5.466001 | 🔵 low — common in general English | - |
| 3927 | **steel** | 3 | 282.12 | 5.42647 | 🔵 low — common in general English | - |
| 3928 | **entertain** | 2 | 280.36 | 8.089058 | 🔵 low — common in general English | - |
| 3929 | **burned** | 2 | 280.36 | 8.089058 | 🔵 low — common in general English | - |
| 3930 | **impressed** | 2 | 280.36 | 8.089058 | 🔵 low — common in general English | - |
| 3931 | **composed** | 2 | 280.36 | 8.089058 | 🔵 low — common in general English | - |
| 3932 | **fulfilled** | 2 | 280.36 | 8.089058 | 🔵 low — common in general English | - |
| 3933 | **stretch** | 2 | 280.36 | 8.089058 | 🔵 low — common in general English | - |
| 3934 | **insignificant** | 2 | 280.36 | 8.089058 | 🔵 low — common in general English | - |
| 3935 | **attracting** | 2 | 280.36 | 8.089058 | 🔵 low — common in general English | - |
| 3936 | **saving** | 2 | 280.36 | 8.089058 | 🔵 low — common in general English | - |
| 3937 | **comfortably** | 2 | 280.36 | 8.089058 | 🔵 low — common in general English | - |
| 3938 | **eliminating** | 2 | 280.36 | 8.089058 | 🔵 low — common in general English | - |
| 3939 | **repaired** | 2 | 280.36 | 8.089058 | 🔵 low — common in general English | - |
| 3940 | **attempt** | 3 | 280.14 | 5.388443 | 🔵 low — common in general English | attempt, attempts |
| 3941 | **improve** | 3 | 279.37 | 5.373627 | 🔵 low — common in general English | - |
| 3942 | **considering** | 3 | 278.99 | 5.366301 | 🔵 low — common in general English | - |
| 3943 | **steering** | 2 | 276.71 | 7.983697 | 🔵 low — common in general English | - |
| 3944 | **absorbed** | 2 | 276.71 | 7.983697 | 🔵 low — common in general English | - |
| 3945 | **eighth** | 2 | 276.71 | 7.983697 | 🔵 low — common in general English | - |
| 3946 | **diminish** | 2 | 276.71 | 7.983697 | 🔵 low — common in general English | - |
| 3947 | **impression** | 2 | 276.71 | 7.983697 | 🔵 low — common in general English | - |
| 3948 | **pool** | 2 | 276.71 | 7.983697 | 🔵 low — common in general English | pool, pools |
| 3949 | **rare** | 2 | 276.71 | 7.983697 | 🔵 low — common in general English | - |
| 3950 | **sinking** | 2 | 276.71 | 7.983697 | 🔵 low — common in general English | - |
| 3951 | **ice** | 2 | 276.71 | 7.983697 | 🔵 low — common in general English | - |
| 3952 | **cook** | 2 | 276.71 | 7.983697 | 🔵 low — common in general English | cook, cooks |
| 3953 | **lock** | 2 | 276.71 | 7.983697 | 🔵 low — common in general English | lock, locks |
| 3954 | **bitter** | 2 | 276.71 | 7.983697 | 🔵 low — common in general English | - |
| 3955 | **unhappy** | 2 | 276.71 | 7.983697 | 🔵 low — common in general English | - |
| 3956 | **consumed** | 2 | 276.71 | 7.983697 | 🔵 low — common in general English | - |
| 3957 | **examination** | 2 | 276.71 | 7.983697 | 🔵 low — common in general English | - |
| 3958 | **sank** | 2 | 276.71 | 7.983697 | 🔵 low — common in general English | - |
| 3959 | **school** | 2 | 276.71 | 7.983697 | 🔵 low — common in general English | - |
| 3960 | **positively** | 2 | 276.71 | 7.983697 | 🔵 low — common in general English | - |
| 3961 | **shape** | 2 | 276.71 | 7.983697 | 🔵 low — common in general English | shape, shapes |
| 3962 | **fixed** | 3 | 274.28 | 5.275647 | 🔵 low — common in general English | - |
| 3963 | **soar** | 2 | 273.41 | 7.888387 | 🔵 low — common in general English | soar, soars |
| 3964 | **safely** | 2 | 273.41 | 7.888387 | 🔵 low — common in general English | - |
| 3965 | **vowed** | 2 | 273.41 | 7.888387 | 🔵 low — common in general English | - |
| 3966 | **picked** | 2 | 273.41 | 7.888387 | 🔵 low — common in general English | - |
| 3967 | **survive** | 2 | 273.41 | 7.888387 | 🔵 low — common in general English | - |
| 3968 | **rolled** | 2 | 273.41 | 7.888387 | 🔵 low — common in general English | - |
| 3969 | **frequent** | 2 | 273.41 | 7.888387 | 🔵 low — common in general English | - |
| 3970 | **searching** | 2 | 273.41 | 7.888387 | 🔵 low — common in general English | - |
| 3971 | **sovereignty** | 2 | 273.41 | 7.888387 | 🔵 low — common in general English | - |
| 3972 | **bull** | 2 | 273.41 | 7.888387 | 🔵 low — common in general English | - |
| 3973 | **praised** | 2 | 273.41 | 7.888387 | 🔵 low — common in general English | - |
| 3974 | **exceptionally** | 2 | 273.41 | 7.888387 | 🔵 low — common in general English | - |
| 3975 | **changed** | 3 | 273.25 | 5.255844 | 🔵 low — common in general English | - |
| 3976 | **united** | 4 | 271.96 | 3.923254 | 🔵 low — common in general English | - |
| 3977 | **one-day** | 2 | 270.39 | 7.801376 | 🔵 low — common in general English | - |
| 3978 | **arguing** | 2 | 270.39 | 7.801376 | 🔵 low — common in general English | - |
| 3979 | **permanently** | 2 | 270.39 | 7.801376 | 🔵 low — common in general English | - |
| 3980 | **unnecessary** | 2 | 270.39 | 7.801376 | 🔵 low — common in general English | - |
| 3981 | **vein** | 2 | 270.39 | 7.801376 | 🔵 low — common in general English | vein, veins |
| 3982 | **stiff** | 2 | 270.39 | 7.801376 | 🔵 low — common in general English | - |
| 3983 | **capacity** | 3 | 269.96 | 5.192532 | 🔵 low — common in general English | capacities, capacity |
| 3984 | **provision** | 3 | 269.96 | 5.192532 | 🔵 low — common in general English | - |
| 3985 | **limited** | 3 | 267.77 | 5.150484 | 🔵 low — common in general English | - |
| 3986 | **worrying** | 2 | 267.62 | 7.721333 | 🔵 low — common in general English | - |
| 3987 | **collapsed** | 2 | 267.62 | 7.721333 | 🔵 low — common in general English | - |
| 3988 | **eagle** | 2 | 267.62 | 7.721333 | 🔵 low — common in general English | - |
| 3989 | **stepped** | 2 | 267.62 | 7.721333 | 🔵 low — common in general English | - |
| 3990 | **pill** | 2 | 267.62 | 7.721333 | 🔵 low — common in general English | - |
| 3991 | **flying** | 2 | 267.62 | 7.721333 | 🔵 low — common in general English | - |
| 3992 | **sticking** | 2 | 267.62 | 7.721333 | 🔵 low — common in general English | - |
| 3993 | **installed** | 2 | 267.62 | 7.721333 | 🔵 low — common in general English | - |
| 3994 | **steam** | 2 | 267.62 | 7.721333 | 🔵 low — common in general English | - |
| 3995 | **briefly** | 2 | 267.62 | 7.721333 | 🔵 low — common in general English | - |
| 3996 | **remaining** | 3 | 265.38 | 5.104499 | 🔵 low — common in general English | - |
| 3997 | **continuing** | 3 | 265.38 | 5.104499 | 🔵 low — common in general English | - |
| 3998 | **picking** | 2 | 265.05 | 7.647225 | 🔵 low — common in general English | - |
| 3999 | **pursuing** | 2 | 265.05 | 7.647225 | 🔵 low — common in general English | - |
| 4000 | **territory** | 2 | 265.05 | 7.647225 | 🔵 low — common in general English | - |
| 4001 | **strictly** | 2 | 265.05 | 7.647225 | 🔵 low — common in general English | - |
| 4002 | **approaching** | 2 | 265.05 | 7.647225 | 🔵 low — common in general English | - |
| 4003 | **postpone** | 2 | 265.05 | 7.647225 | 🔵 low — common in general English | - |
| 4004 | **dip** | 2 | 265.05 | 7.647225 | 🔵 low — common in general English | - |
| 4005 | **recognition** | 2 | 265.05 | 7.647225 | 🔵 low — common in general English | - |
| 4006 | **plunge** | 2 | 265.05 | 7.647225 | 🔵 low — common in general English | - |
| 4007 | **compare** | 2 | 265.05 | 7.647225 | 🔵 low — common in general English | - |
| 4008 | **wrote** | 2 | 265.05 | 7.647225 | 🔵 low — common in general English | - |
| 4009 | **cycle** | 2 | 262.66 | 7.578232 | 🔵 low — common in general English | cycle, cycles |
| 4010 | **sown** | 2 | 262.66 | 7.578232 | 🔵 low — common in general English | - |
| 4011 | **tend** | 2 | 262.66 | 7.578232 | 🔵 low — common in general English | - |
| 4012 | **pulp** | 2 | 262.66 | 7.578232 | 🔵 low — common in general English | - |
| 4013 | **treated** | 2 | 262.66 | 7.578232 | 🔵 low — common in general English | - |
| 4014 | **refrain** | 2 | 262.66 | 7.578232 | 🔵 low — common in general English | - |
| 4015 | **repaid** | 2 | 262.66 | 7.578232 | 🔵 low — common in general English | - |
| 4016 | **recognized** | 2 | 262.66 | 7.578232 | 🔵 low — common in general English | - |
| 4017 | **earning** | 2 | 260.42 | 7.513694 | 🔵 low — common in general English | - |
| 4018 | **engage** | 2 | 260.42 | 7.513694 | 🔵 low — common in general English | - |
| 4019 | **counsel** | 2 | 260.42 | 7.513694 | 🔵 low — common in general English | - |
| 4020 | **framework** | 2 | 260.42 | 7.513694 | 🔵 low — common in general English | - |
| 4021 | **science** | 2 | 260.42 | 7.513694 | 🔵 low — common in general English | - |
| 4022 | **fund** | 3 | 260.37 | 5.008168 | 🔵 low — common in general English | - |
| 4023 | **key** | 3 | 260.11 | 5.003079 | 🔵 low — common in general English | - |
| 4024 | **resort** | 2 | 258.32 | 7.453069 | 🔵 low — common in general English | - |
| 4025 | **passenger** | 2 | 258.32 | 7.453069 | 🔵 low — common in general English | - |
| 4026 | **latter** | 2 | 258.32 | 7.453069 | 🔵 low — common in general English | - |
| 4027 | **establishing** | 2 | 258.32 | 7.453069 | 🔵 low — common in general English | - |
| 4028 | **sudden** | 2 | 258.32 | 7.453069 | 🔵 low — common in general English | - |
| 4029 | **pat** | 2 | 258.32 | 7.453069 | 🔵 low — common in general English | - |
| 4030 | **payment** | 3 | 258.04 | 4.963272 | 🔵 low — common in general English | - |
| 4031 | **greatly** | 2 | 256.34 | 7.395911 | 🔵 low — common in general English | - |
| 4032 | **preparation** | 2 | 256.34 | 7.395911 | 🔵 low — common in general English | - |
| 4033 | **flowing** | 2 | 256.34 | 7.395911 | 🔵 low — common in general English | - |
| 4034 | **creditor** | 2 | 256.34 | 7.395911 | 🔵 low — common in general English | creditor, creditors |
| 4035 | **due** | 4 | 256.30 | 3.697356 | 🔵 low — common in general English | - |
| 4036 | **afford** | 2 | 254.47 | 7.341843 | 🔵 low — common in general English | - |
| 4037 | **pretty** | 2 | 254.47 | 7.341843 | 🔵 low — common in general English | - |
| 4038 | **climb** | 2 | 254.47 | 7.341843 | 🔵 low — common in general English | - |
| 4039 | **injured** | 2 | 254.47 | 7.341843 | 🔵 low — common in general English | - |
| 4040 | **population** | 2 | 252.69 | 7.29055 | 🔵 low — common in general English | - |
| 4041 | **shared** | 2 | 252.69 | 7.29055 | 🔵 low — common in general English | - |
| 4042 | **competitor** | 2 | 252.69 | 7.29055 | 🔵 low — common in general English | - |
| 4043 | **violating** | 2 | 252.69 | 7.29055 | 🔵 low — common in general English | - |
| 4044 | **bridge** | 2 | 252.69 | 7.29055 | 🔵 low — common in general English | - |
| 4045 | **referred** | 2 | 252.69 | 7.29055 | 🔵 low — common in general English | - |
| 4046 | **joining** | 2 | 252.69 | 7.29055 | 🔵 low — common in general English | - |
| 4047 | **renew** | 2 | 252.69 | 7.29055 | 🔵 low — common in general English | - |
| 4048 | **escort** | 2 | 251.00 | 7.24176 | 🔵 low — common in general English | - |
| 4049 | **restored** | 2 | 251.00 | 7.24176 | 🔵 low — common in general English | - |
| 4050 | **sustain** | 2 | 251.00 | 7.24176 | 🔵 low — common in general English | - |
| 4051 | **obviously** | 2 | 249.38 | 7.19524 | 🔵 low — common in general English | - |
| 4052 | **troubled** | 2 | 249.38 | 7.19524 | 🔵 low — common in general English | - |
| 4053 | **argued** | 2 | 249.38 | 7.19524 | 🔵 low — common in general English | - |
| 4054 | **attract** | 2 | 249.38 | 7.19524 | 🔵 low — common in general English | attract, attracts |
| 4055 | **exception** | 2 | 249.38 | 7.19524 | 🔵 low — common in general English | - |
| 4056 | **consulting** | 2 | 249.38 | 7.19524 | 🔵 low — common in general English | - |
| 4057 | **chief** | 3 | 247.93 | 4.768829 | 🔵 low — common in general English | chief, chiefs |
| 4058 | **blocked** | 2 | 247.84 | 7.150788 | 🔵 low — common in general English | - |
| 4059 | **maybe** | 2 | 247.84 | 7.150788 | 🔵 low — common in general English | - |
| 4060 | **quarter** | 4 | 247.53 | 3.570899 | 🔵 low — common in general English | quarter, quarters |
| 4061 | **wet** | 2 | 246.37 | 7.108229 | 🔵 low — common in general English | - |
| 4062 | **dependent** | 2 | 246.37 | 7.108229 | 🔵 low — common in general English | - |
| 4063 | **usual** | 2 | 244.95 | 7.067407 | 🔵 low — common in general English | - |
| 4064 | **jump** | 2 | 244.95 | 7.067407 | 🔵 low — common in general English | - |
| 4065 | **struck** | 2 | 244.95 | 7.067407 | 🔵 low — common in general English | - |
| 4066 | **transferred** | 2 | 244.95 | 7.067407 | 🔵 low — common in general English | - |
| 4067 | **stem** | 2 | 244.95 | 7.067407 | 🔵 low — common in general English | - |
| 4068 | **back** | 3 | 243.91 | 4.691571 | 🔵 low — common in general English | - |
| 4069 | **underground** | 2 | 243.59 | 7.028186 | 🔵 low — common in general English | - |
| 4070 | **paid** | 3 | 242.58 | 4.665882 | 🔵 low — common in general English | - |
| 4071 | **pattern** | 2 | 242.29 | 6.990446 | 🔵 low — common in general English | - |
| 4072 | **tension** | 2 | 242.29 | 6.990446 | 🔵 low — common in general English | - |
| 4073 | **attracted** | 2 | 242.29 | 6.990446 | 🔵 low — common in general English | - |
| 4074 | **fifth** | 2 | 242.29 | 6.990446 | 🔵 low — common in general English | - |
| 4075 | **club** | 2 | 242.29 | 6.990446 | 🔵 low — common in general English | - |
| 4076 | **react** | 2 | 242.29 | 6.990446 | 🔵 low — common in general English | - |
| 4077 | **neutral** | 2 | 242.29 | 6.990446 | 🔵 low — common in general English | - |
| 4078 | **steep** | 2 | 242.29 | 6.990446 | 🔵 low — common in general English | - |
| 4079 | **added** | 4 | 241.42 | 3.482777 | 🔵 low — common in general English | - |
| 4080 | **dropping** | 2 | 241.03 | 6.954078 | 🔵 low — common in general English | dropping, droppings |
| 4081 | **product** | 3 | 240.54 | 4.6268 | 🔵 low — common in general English | - |
| 4082 | **additional** | 3 | 240.00 | 4.616401 | 🔵 low — common in general English | - |
| 4083 | **badly** | 2 | 239.81 | 6.918987 | 🔵 low — common in general English | - |
| 4084 | **heating** | 2 | 239.81 | 6.918987 | 🔵 low — common in general English | - |
| 4085 | **calm** | 2 | 239.81 | 6.918987 | 🔵 low — common in general English | - |
| 4086 | **approached** | 2 | 239.81 | 6.918987 | 🔵 low — common in general English | - |
| 4087 | **safety** | 2 | 239.81 | 6.918987 | 🔵 low — common in general English | - |
| 4088 | **address** | 2 | 239.81 | 6.918987 | 🔵 low — common in general English | - |
| 4089 | **promised** | 2 | 239.81 | 6.918987 | 🔵 low — common in general English | - |
| 4090 | **late** | 3 | 238.76 | 4.59255 | 🔵 low — common in general English | - |
| 4091 | **tire** | 2 | 238.63 | 6.885085 | 🔵 low — common in general English | - |
| 4092 | **preparing** | 2 | 238.63 | 6.885085 | 🔵 low — common in general English | - |
| 4093 | **appointed** | 2 | 238.63 | 6.885085 | 🔵 low — common in general English | - |
| 4094 | **treatment** | 2 | 235.33 | 6.789775 | 🔵 low — common in general English | treatment, treatments |
| 4095 | **pushing** | 2 | 235.33 | 6.789775 | 🔵 low — common in general English | - |
| 4096 | **acceptable** | 2 | 235.33 | 6.789775 | 🔵 low — common in general English | - |
| 4097 | **maintaining** | 2 | 235.33 | 6.789775 | 🔵 low — common in general English | - |
| 4098 | **last** | 5 | 235.10 | 2.713265 | 🔵 low — common in general English | - |
| 4099 | **priority** | 2 | 234.30 | 6.759922 | 🔵 low — common in general English | - |
| 4100 | **encouraged** | 2 | 234.30 | 6.759922 | 🔵 low — common in general English | - |
| 4101 | **balanced** | 2 | 233.29 | 6.730934 | 🔵 low — common in general English | - |
| 4102 | **tonight** | 2 | 233.29 | 6.730934 | 🔵 low — common in general English | - |
| 4103 | **announcing** | 2 | 232.32 | 6.702763 | 🔵 low — common in general English | - |
| 4104 | **marked** | 2 | 232.32 | 6.702763 | 🔵 low — common in general English | - |
| 4105 | **failing** | 2 | 231.37 | 6.675364 | 🔵 low — common in general English | - |
| 4106 | **bidding** | 2 | 231.37 | 6.675364 | 🔵 low — common in general English | - |
| 4107 | **occurred** | 2 | 231.37 | 6.675364 | 🔵 low — common in general English | - |
| 4108 | **settle** | 2 | 231.37 | 6.675364 | 🔵 low — common in general English | - |
| 4109 | **seemed** | 2 | 231.37 | 6.675364 | 🔵 low — common in general English | - |
| 4110 | **complex** | 2 | 231.37 | 6.675364 | 🔵 low — common in general English | - |
| 4111 | **prospect** | 2 | 229.54 | 6.622721 | 🔵 low — common in general English | prospect, prospects |
| 4112 | **indication** | 2 | 229.54 | 6.622721 | 🔵 low — common in general English | - |
| 4113 | **broke** | 2 | 229.54 | 6.622721 | 🔵 low — common in general English | - |
| 4114 | **conditioned** | 2 | 229.54 | 6.622721 | 🔵 low — common in general English | - |
| 4115 | **twice** | 2 | 228.66 | 6.597403 | 🔵 low — common in general English | - |
| 4116 | **outright** | 2 | 228.66 | 6.597403 | 🔵 low — common in general English | - |
| 4117 | **recommend** | 2 | 228.66 | 6.597403 | 🔵 low — common in general English | - |
| 4118 | **sufficient** | 2 | 228.66 | 6.597403 | 🔵 low — common in general English | - |
| 4119 | **measured** | 2 | 227.81 | 6.57271 | 🔵 low — common in general English | - |
| 4120 | **core** | 2 | 226.97 | 6.548613 | 🔵 low — common in general English | - |
| 4121 | **welcomed** | 2 | 226.97 | 6.548613 | 🔵 low — common in general English | - |
| 4122 | **comprising** | 2 | 226.16 | 6.525082 | 🔵 low — common in general English | - |
| 4123 | **headed** | 2 | 225.36 | 6.502093 | 🔵 low — common in general English | - |
| 4124 | **lifted** | 2 | 225.36 | 6.502093 | 🔵 low — common in general English | - |
| 4125 | **comparable** | 2 | 225.36 | 6.502093 | 🔵 low — common in general English | - |
| 4126 | **frozen** | 2 | 224.58 | 6.47962 | 🔵 low — common in general English | - |
| 4127 | **involving** | 2 | 224.58 | 6.47962 | 🔵 low — common in general English | - |
| 4128 | **tight** | 2 | 223.82 | 6.457641 | 🔵 low — common in general English | - |
| 4129 | **supply** | 3 | 223.29 | 4.294818 | 🔵 low — common in general English | supplies, supply |
| 4130 | **contribute** | 2 | 223.07 | 6.436135 | 🔵 low — common in general English | - |
| 4131 | **room** | 2 | 223.07 | 6.436135 | 🔵 low — common in general English | - |
| 4132 | **faced** | 2 | 223.07 | 6.436135 | 🔵 low — common in general English | - |
| 4133 | **contained** | 2 | 223.07 | 6.436135 | 🔵 low — common in general English | - |
| 4134 | **flat** | 2 | 223.07 | 6.436135 | 🔵 low — common in general English | - |
| 4135 | **value** | 3 | 222.51 | 4.279929 | 🔵 low — common in general English | value, values |
| 4136 | **social** | 2 | 221.63 | 6.394462 | 🔵 low — common in general English | - |
| 4137 | **plan** | 3 | 221.37 | 4.258004 | 🔵 low — common in general English | - |
| 4138 | **depending** | 2 | 220.93 | 6.374259 | 🔵 low — common in general English | - |
| 4139 | **so-called** | 2 | 220.93 | 6.374259 | 🔵 low — common in general English | - |
| 4140 | **internal** | 2 | 220.24 | 6.354457 | 🔵 low — common in general English | - |
| 4141 | **rapid** | 2 | 220.24 | 6.354457 | 🔵 low — common in general English | - |
| 4142 | **proceed** | 2 | 220.24 | 6.354457 | 🔵 low — common in general English | - |
| 4143 | **likely** | 3 | 219.40 | 4.220174 | 🔵 low — common in general English | - |
| 4144 | **evidence** | 2 | 218.91 | 6.31599 | 🔵 low — common in general English | - |
| 4145 | **normally** | 2 | 217.63 | 6.278949 | 🔵 low — common in general English | - |
| 4146 | **competitiveness** | 2 | 217.00 | 6.260931 | 🔵 low — common in general English | - |
| 4147 | **decrease** | 2 | 217.00 | 6.260931 | 🔵 low — common in general English | - |
| 4148 | **structure** | 2 | 216.39 | 6.243231 | 🔵 low — common in general English | - |
| 4149 | **double** | 2 | 215.79 | 6.225839 | 🔵 low — common in general English | - |
| 4150 | **brown** | 2 | 215.79 | 6.225839 | 🔵 low — common in general English | - |
| 4151 | **retain** | 2 | 215.19 | 6.208745 | 🔵 low — common in general English | - |
| 4152 | **partner** | 2 | 214.61 | 6.191938 | 🔵 low — common in general English | - |
| 4153 | **fallen** | 2 | 214.04 | 6.175409 | 🔵 low — common in general English | - |
| 4154 | **participation** | 2 | 214.04 | 6.175409 | 🔵 low — common in general English | - |
| 4155 | **advanced** | 2 | 213.47 | 6.159148 | 🔵 low — common in general English | - |
| 4156 | **ruled** | 2 | 211.84 | 6.111895 | 🔵 low — common in general English | - |
| 4157 | **primarily** | 2 | 211.84 | 6.111895 | 🔵 low — common in general English | - |
| 4158 | **suit** | 2 | 211.84 | 6.111895 | 🔵 low — common in general English | - |
| 4159 | **loss** | 4 | 211.57 | 3.052105 | 🔵 low — common in general English | - |
| 4160 | **staff** | 2 | 210.79 | 6.08159 | 🔵 low — common in general English | staff, staffs |
| 4161 | **depressed** | 2 | 209.27 | 6.037787 | 🔵 low — common in general English | - |
| 4162 | **threatened** | 2 | 209.27 | 6.037787 | 🔵 low — common in general English | - |
| 4163 | **strongly** | 2 | 209.27 | 6.037787 | 🔵 low — common in general English | - |
| 4164 | **stake** | 3 | 209.25 | 4.024791 | 🔵 low — common in general English | - |
| 4165 | **push** | 2 | 207.81 | 5.995823 | 🔵 low — common in general English | - |
| 4166 | **discussed** | 2 | 207.34 | 5.982217 | 🔵 low — common in general English | - |
| 4167 | **pound** | 2 | 206.42 | 5.955549 | 🔵 low — common in general English | - |
| 4168 | **vegetable** | 2 | 206.42 | 5.955549 | 🔵 low — common in general English | vegetable, vegetables |
| 4169 | **larger** | 2 | 205.52 | 5.929574 | 🔵 low — common in general English | - |
| 4170 | **copper** | 2 | 205.52 | 5.929574 | 🔵 low — common in general English | - |
| 4171 | **smaller** | 2 | 205.08 | 5.916835 | 🔵 low — common in general English | - |
| 4172 | **asset** | 2 | 204.64 | 5.904256 | 🔵 low — common in general English | asset, assets |
| 4173 | **grew** | 2 | 204.21 | 5.891833 | 🔵 low — common in general English | - |
| 4174 | **release** | 2 | 202.13 | 5.831935 | 🔵 low — common in general English | - |
| 4175 | **forward** | 2 | 202.13 | 5.831935 | 🔵 low — common in general English | - |
| 4176 | **strategy** | 2 | 201.34 | 5.808946 | 🔵 low — common in general English | strategies, strategy |
| 4177 | **buy** | 3 | 195.62 | 3.76272 | 🔵 low — common in general English | - |
| 4178 | **helped** | 2 | 195.21 | 5.632322 | 🔵 low — common in general English | - |
| 4179 | **primary** | 2 | 193.60 | 5.585802 | 🔵 low — common in general English | - |
| 4180 | **majority** | 2 | 190.88 | 5.507159 | 🔵 low — common in general English | - |
| 4181 | **combined** | 2 | 190.01 | 5.482261 | 🔵 low — common in general English | - |
| 4182 | **paper** | 2 | 189.17 | 5.457969 | 🔵 low — common in general English | - |
| 4183 | **outlook** | 2 | 188.62 | 5.442095 | 🔵 low — common in general English | - |
| 4184 | **southern** | 2 | 187.81 | 5.418748 | 🔵 low — common in general English | - |
| 4185 | **existing** | 2 | 186.25 | 5.373627 | 🔵 low — common in general English | - |
| 4186 | **aimed** | 2 | 185.74 | 5.359029 | 🔵 low — common in general English | - |
| 4187 | **unlikely** | 2 | 185.49 | 5.351808 | 🔵 low — common in general English | - |
| 4188 | **affected** | 2 | 185.24 | 5.34464 | 🔵 low — common in general English | - |
| 4189 | **discuss** | 2 | 185.00 | 5.337522 | 🔵 low — common in general English | - |
| 4190 | **dropped** | 2 | 185.00 | 5.337522 | 🔵 low — common in general English | - |
| 4191 | **court** | 2 | 185.00 | 5.337522 | 🔵 low — common in general English | - |
| 4192 | **spending** | 2 | 183.55 | 5.29585 | 🔵 low — common in general English | - |
| 4193 | **ahead** | 2 | 183.08 | 5.282336 | 🔵 low — common in general English | - |
| 4194 | **current** | 3 | 179.81 | 3.458653 | 🔵 low — common in general English | - |
| 4195 | **mainly** | 2 | 179.13 | 5.168289 | 🔵 low — common in general English | - |
| 4196 | **quoted** | 2 | 177.51 | 5.121496 | 🔵 low — common in general English | - |
| 4197 | **price** | 3 | 175.34 | 3.372545 | 🔵 low — common in general English | price, prices |
| 4198 | **crop** | 2 | 171.69 | 4.953564 | 🔵 low — common in general English | crop, crops |
| 4199 | **letter** | 2 | 171.19 | 4.939175 | 🔵 low — common in general English | letter, letters |
| 4200 | **area** | 2 | 170.54 | 4.920306 | 🔵 low — common in general English | area, areas |
| 4201 | **addition** | 2 | 169.58 | 4.892655 | 🔵 low — common in general English | - |
| 4202 | **fed** | 2 | 169.42 | 4.88812 | 🔵 low — common in general English | - |
| 4203 | **planned** | 2 | 168.95 | 4.874636 | 🔵 low — common in general English | - |
| 4204 | **accord** | 2 | 168.34 | 4.856937 | 🔵 low — common in general English | - |
| 4205 | **expect** | 2 | 167.59 | 4.835244 | 🔵 low — common in general English | - |
| 4206 | **group** | 3 | 166.26 | 3.197874 | 🔵 low — common in general English | - |
| 4207 | **audi** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - |
| 4208 | **ale** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - |
| 4209 | **leak** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - |
| 4210 | **trusting** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - |
| 4211 | **flavour** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - |
| 4212 | **digging** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - |
| 4213 | **incorrectly** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - |
| 4214 | **expedient** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - |
| 4215 | **medication** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - |
| 4216 | **comprehend** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - |
| 4217 | **make-up** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - |
| 4218 | **ensue** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - |
| 4219 | **flagrant** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - |
| 4220 | **autonomy** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - |
| 4221 | **preoccupied** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - |
| 4222 | **entailed** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - |
| 4223 | **westward** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - |
| 4224 | **fruitful** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - |
| 4225 | **coincidence** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - |
| 4226 | **circular** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - |
| 4227 | **fuse** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - |
| 4228 | **flare** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - |
| 4229 | **torrential** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - |
| 4230 | **wielding** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - |
| 4231 | **good-looking** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - |
| 4232 | **horror** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - |
| 4233 | **cemetery** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - |
| 4234 | **unsatisfied** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - |
| 4235 | **reconciled** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - |
| 4236 | **authoritative** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - |
| 4237 | **aging** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - |
| 4238 | **disenchanted** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - |
| 4239 | **brave** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - |
| 4240 | **recklessly** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - |
| 4241 | **demise** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - |
| 4242 | **enduring** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - |
| 4243 | **suffice** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - |
| 4244 | **unsurpassed** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - |
| 4245 | **constellation** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - |
| 4246 | **trident** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - |
| 4247 | **toss** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - |
| 4248 | **trench** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - |
| 4249 | **chewing** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - |
| 4250 | **snowy** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - |
| 4251 | **lastly** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - |
| 4252 | **sacrificed** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - |
| 4253 | **commanding** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - |
| 4254 | **rang** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - |
| 4255 | **orchard** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - |
| 4256 | **fever** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - |
| 4257 | **gigantic** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - |
| 4258 | **horde** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - |
| 4259 | **offload** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - |
| 4260 | **comprehension** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - |
| 4261 | **fas** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - |
| 4262 | **snare** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - |
| 4263 | **otter** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - |
| 4264 | **musk-oxen** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - |
| 4265 | **irrigated** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - |
| 4266 | **rightful** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - |
| 4267 | **propped** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - |
| 4268 | **imbalanced** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - |
| 4269 | **bedding** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - |
| 4270 | **daytime** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - |
| 4271 | **overtake** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - |
| 4272 | **colder** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - |
| 4273 | **lure** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - |
| 4274 | **kin** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - |
| 4275 | **punished** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - |
| 4276 | **engulfed** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - |
| 4277 | **overwhelm** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - |
| 4278 | **oceanic** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - |
| 4279 | **transported** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - |
| 4280 | **inexorable** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - |
| 4281 | **mooring** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - |
| 4282 | **lymph** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - |
| 4283 | **prolific** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - |
| 4284 | **shocked** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - |
| 4285 | **disdain** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - |
| 4286 | **overpowering** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - |
| 4287 | **seizure** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - |
| 4288 | **knuckle** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - |
| 4289 | **shin** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - |
| 4290 | **indulge** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - |
| 4291 | **ethic** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - |
| 4292 | **daylight** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - |
| 4293 | **unsightly** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - |
| 4294 | **congregation** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - |
| 4295 | **summed** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - |
| 4296 | **commentator** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - |
| 4297 | **receiver** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - |
| 4298 | **differently** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - |
| 4299 | **destiny** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - |
| 4300 | **loot** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - |
| 4301 | **falsely** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - |
| 4302 | **accusation** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - |
| 4303 | **recalcitrant** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - |
| 4304 | **grim** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - |
| 4305 | **oblige** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - |
| 4306 | **seamless** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - |
| 4307 | **plucked** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - |
| 4308 | **squarely** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - |
| 4309 | **noticed** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - |
| 4310 | **finer** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - |
| 4311 | **ingenuity** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - |
| 4312 | **prohibition** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - |
| 4313 | **conformity** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - |
| 4314 | **purest** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - |
| 4315 | **blaze** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - |
| 4316 | **incomprehensible** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - |
| 4317 | **enquire** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - |
| 4318 | **conveyance** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - |
| 4319 | **tread** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - |
| 4320 | **sation** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - |
| 4321 | **smoothly** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - |
| 4322 | **respecting** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - |
| 4323 | **reproduce** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - |
| 4324 | **lethargy** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - |
| 4325 | **avenue** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - |
| 4326 | **makin** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - |
| 4327 | **harden** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - |
| 4328 | **debating** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - |
| 4329 | **appropriated** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - |
| 4330 | **demolished** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - |
| 4331 | **thrashing** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - |
| 4332 | **reprimanded** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - |
| 4333 | **calmed** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - |
| 4334 | **crowned** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - |
| 4335 | **commonplace** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - |
| 4336 | **distinct** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - |
| 4337 | **nightmare** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - |
| 4338 | **ransom** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - |
| 4339 | **cognizant** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - |
| 4340 | **unquestionably** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - |
| 4341 | **sym** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - |
| 4342 | **intensely** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - |
| 4343 | **straightforward** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - |
| 4344 | **watchdog** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - |
| 4345 | **imprisoned** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - |
| 4346 | **punishment** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - |
| 4347 | **invading** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - |
| 4348 | **inflict** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - |
| 4349 | **afflicted** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - |
| 4350 | **rider** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - |
| 4351 | **intimidation** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - |
| 4352 | **contravention** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - |
| 4353 | **predator** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - |
| 4354 | **outraged** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - |
| 4355 | **shedding** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - |
| 4356 | **tolerance** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - |
| 4357 | **tenderness** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - |
| 4358 | **flourish** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - |
| 4359 | **lasted** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - |
| 4360 | **dissuade** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - |
| 4361 | **jugular** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - |
| 4362 | **mini** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - |
| 4363 | **greed** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - |
| 4364 | **flee** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - |
| 4365 | **vicinity** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - |
| 4366 | **overwhelmed** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - |
| 4367 | **reappeared** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - |
| 4368 | **boasting** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - |
| 4369 | **sucked** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - |
| 4370 | **futility** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - |
| 4371 | **wealthier** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - |
| 4372 | **dwindle** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - |
| 4373 | **fare** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - |
| 4374 | **aberration** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - |
| 4375 | **mirage** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - |
| 4376 | **omitting** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - |
| 4377 | **summarized** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - |
| 4378 | **thirty-five** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - |
| 4379 | **instantly** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - |
| 4380 | **colossal** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - |
| 4381 | **transparent** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - |
| 4382 | **simplicity** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - |
| 4383 | **chatting** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - |
| 4384 | **smoking** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - |
| 4385 | **lowland** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - |
| 4386 | **abusing** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - |
| 4387 | **subtle** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - |
| 4388 | **occasional** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - |
| 4389 | **infested** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - |
| 4390 | **diseased** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - |
| 4391 | **smashing** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - |
| 4392 | **adult** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - |
| 4393 | **ration** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - |
| 4394 | **coral** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - |
| 4395 | **ordinarily** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - |
| 4396 | **ready-made** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - |
| 4397 | **subcontinent** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - |
| 4398 | **bountiful** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - |
| 4399 | **commentary** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - |
| 4400 | **impossibility** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - |
| 4401 | **amazed** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - |
| 4402 | **amazing** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - |
| 4403 | **resigning** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - |
| 4404 | **dispelled** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - |
| 4405 | **foodstuff** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - |
| 4406 | **rendered** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - |
| 4407 | **placated** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - |
| 4408 | **subduing** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - |
| 4409 | **scrape** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - |
| 4410 | **severity** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - |
| 4411 | **intel** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - |
| 4412 | **exile** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - |
| 4413 | **infinitesimal** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - |
| 4414 | **bloom** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - |
| 4415 | **supposedly** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - |
| 4416 | **knowingly** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - |
| 4417 | **demonstration** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - |
| 4418 | **cleansing** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - |
| 4419 | **spilt** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - |
| 4420 | **reassured** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - |
| 4421 | **predominate** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - |
| 4422 | **quelling** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - |
| 4423 | **misconception** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - |
| 4424 | **propagated** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - |
| 4425 | **bore** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - |
| 4426 | **negligence** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - |
| 4427 | **astonished** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - |
| 4428 | **proceeded** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - |
| 4429 | **vanished** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - |
| 4430 | **uncontrolled** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - |
| 4431 | **equality** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - |
| 4432 | **fabrication** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - |
| 4433 | **translating** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - |
| 4434 | **traced** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - |
| 4435 | **obstinate** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - |
| 4436 | **unfabricated** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - |
| 4437 | **accustomed** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - |
| 4438 | **impediment** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - |
| 4439 | **forcefully** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - |
| 4440 | **brush** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - |
| 4441 | **prematurely** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - |
| 4442 | **skylight** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - |
| 4443 | **inserting** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - |
| 4444 | **winnowed** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - |
| 4445 | **irrigate** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - |
| 4446 | **fertile** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - |
| 4447 | **invented** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - |
| 4448 | **vine** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - |
| 4449 | **azure** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - |
| 4450 | **beamed** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4451 | **elucidated** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4452 | **wonderfully** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4453 | **concerns-such** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4454 | **whatever-i** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4455 | **circumambulation** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4456 | **mantra-even** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4457 | **mani-it** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4458 | **torch** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4459 | **akani** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4460 | **tha** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4461 | **unexcelled** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4462 | **lotus-light** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4463 | **divinity** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4464 | **ever-revolving** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4465 | **buddha-nature** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4466 | **adventitious** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4467 | **entranced** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4468 | **tice** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4469 | **teaching-which** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4470 | **reasoning** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4471 | **proudly** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4472 | **minutely** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4473 | **leapt** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4474 | **moth** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4475 | **lamp-flame** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4476 | **carnivorous** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4477 | **seduced** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4478 | **bait** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4479 | **gyalse** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4480 | **mru** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4481 | **riverbed** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4482 | **indispensable-remembering** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4483 | **rat** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4484 | **dremo** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4485 | **marmot** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4486 | **sleepy** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4487 | **weren** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4488 | **string** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4489 | **loosely** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4490 | **elegant** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4491 | **meaning-you** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4492 | **debase** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4493 | **everything-the** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4494 | **teachings-properly** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4495 | **disheart** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4496 | **ened** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4497 | **elementary** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4498 | **prescribe** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4499 | **dharma-that** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4500 | **practice-i** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4501 | **death-bed** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4502 | **helplessly** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4503 | **perilous** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4504 | **libera** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4505 | **shallow-tongued** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4506 | **sneer** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4507 | **mal** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4508 | **joyfully** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4509 | **swathed** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4510 | **turban** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4511 | **ataka** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4512 | **dignified** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4513 | **oppor** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4514 | **tunity** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4515 | **khatha** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4516 | **outlying** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4517 | **attune** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4518 | **forefather** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4519 | **aspiring** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4520 | **liyana** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4521 | **atten** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4522 | **dant** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4523 | **oll** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4524 | **dysfunction** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4525 | **unheard** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4526 | **animal-even** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4527 | **prized** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4528 | **padme** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4529 | **heap-wherea** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4530 | **conceive** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4531 | **pratimoksa** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4532 | **dharma-the** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4533 | **buddha-exist** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4534 | **sparsely** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4535 | **whjch** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4536 | **script** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4537 | **intro** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4538 | **duced** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4539 | **mikyo** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4540 | **rasa** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4541 | **trulnang** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4542 | **estab** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4543 | **lished** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4544 | **kingtrisong** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4545 | **mantra-holder** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4546 | **sustra** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4547 | **dharma-for** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4548 | **queror** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4549 | **preached** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4550 | **extant** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4551 | **ahhough** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4552 | **destroyer-of-samsara** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4553 | **incalculably** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4554 | **infinite-aspiration** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4555 | **alternation** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4556 | **promulgated** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4557 | **once-come-king** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4558 | **trayana** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4559 | **uncompounded** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4560 | **interpreter** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4561 | **kham** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4562 | **degenerations-those** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4563 | **it-just** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4564 | **transmi** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4565 | **infiltrate** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4566 | **condense** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4567 | **important-the** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4568 | **canonical** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4569 | **commentar** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4570 | **ies** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4571 | **practice-even** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4572 | **triptaka** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4573 | **metaphysic** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4574 | **piety** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4575 | **illustrate** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4576 | **condi** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4577 | **endowed** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4578 | **enslavement** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4579 | **hypocritical** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4580 | **intrusive** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4581 | **depravity** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4582 | **heedlessness** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4583 | **poisons-that** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4584 | **dominat** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4585 | **plishing** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4586 | **perverted** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4587 | **lazy** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4588 | **indolence** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4589 | **life-that** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4590 | **impostor** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4591 | **pretence** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4592 | **humanity** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4593 | **depraved** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4594 | **suffedng** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4595 | **sarilsa** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4596 | **plishment** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4597 | **snuff** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4598 | **chieftain** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4599 | **worth-each** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4600 | **thirty-four** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4601 | **squander** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4602 | **mter** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4603 | **realiza** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4604 | **goal-the** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4605 | **dharma-i** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4606 | **junction** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4607 | **interconnected** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4608 | **elements-the** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4609 | **flint** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4610 | **rarer** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4611 | **advan** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4612 | **tage** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4613 | **perchance** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4614 | **adrift** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4615 | **shoreless** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4616 | **needle-which** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4617 | **saddened** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4618 | **fritter** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4619 | **jettison** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4620 | **trakpa** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4621 | **resourcefulness** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4622 | **raft** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4623 | **thing-the** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4624 | **preme** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4625 | **dharma-and** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4626 | **ineffectual** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4627 | **folly** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4628 | **betray** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4629 | **turning-point** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4630 | **bewildered** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4631 | **miyowa** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4632 | **fashioned** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4633 | **god-realm** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4634 | **fruit-bearing** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4635 | **manasarovar** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4636 | **sea-water** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4637 | **ear-shot** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4638 | **snow-covered** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4639 | **sub-continent** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4640 | **rim** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4641 | **engulf** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4642 | **conflagration** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4643 | **raincloud** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4644 | **devastation** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4645 | **sincerely-if** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4646 | **realm-even** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4647 | **gods-who** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4648 | **flicker** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4649 | **slumber** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4650 | **ever-present** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4651 | **status-until** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4652 | **gnashing** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4653 | **fang** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4654 | **charm** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4655 | **athlete** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4656 | **fleetness-none** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4657 | **impene** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4658 | **trable** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4659 | **concealment** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4660 | **glaze** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4661 | **willy-nilly** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4662 | **defender** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4663 | **you-can** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4664 | **dispensation** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4665 | **miracu** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4666 | **lous** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4667 | **ofyerpa** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4668 | **zur** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4669 | **nub** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4670 | **clan** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4671 | **plished** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4672 | **space-they** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4673 | **silence** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4674 | **nyeshangkatya** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4675 | **motionless** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4676 | **volley** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4677 | **cliff-but** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4678 | **firewood** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4679 | **contraption** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4680 | **depends-and** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4681 | **scarecrow** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4682 | **momerit** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4683 | **illustrious** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4684 | **stature** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4685 | **earshot** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4686 | **resplendence** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4687 | **outshine** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4688 | **mahdvara** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4689 | **evade** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4690 | **consolation** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4691 | **mahasammata** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4692 | **pala** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4693 | **candra** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4694 | **nivara** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4695 | **tavi** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4696 | **kambhin** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4697 | **earthly** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4698 | **lek** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4699 | **jambu** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4700 | **dvipa** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4701 | **ralpachen** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4702 | **gesar** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4703 | **tajikistan** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4704 | **ambassa** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4705 | **dor** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4706 | **beehive** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4707 | **race** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4708 | **abstinence** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4709 | **summertime** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4710 | **meadow** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4711 | **lush** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4712 | **bask** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4713 | **scarlet** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4714 | **grassland** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4715 | **hue** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4716 | **brittle** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4717 | **glacial** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4718 | **scour** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4719 | **helpless** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4720 | **grandparent** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4721 | **great-grandparent** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4722 | **eminent** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4723 | **year-or** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4724 | **animals-sheep** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4725 | **dogs-how** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4726 | **animate** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4727 | **mind-everything** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4728 | **exalted** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4729 | **rainbow-but** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4730 | **stiffly** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4731 | **armpit** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4732 | **cherished** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4733 | **thread** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4734 | **beloved** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4735 | **handsome** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4736 | **distinguished** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4737 | **horribly** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4738 | **livid** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4739 | **here-our** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4740 | **trussed** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4741 | **curtain** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4742 | **sheepskin** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4743 | **rug** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4744 | **tuft** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4745 | **bespattered** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4746 | **cremating** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4747 | **vagabond** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4748 | **enjoy-teacher** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4749 | **protege** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4750 | **comrade** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4751 | **wives-there** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4752 | **three-storeyed** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4753 | **emanated** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4754 | **rivalled** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4755 | **kagyupa** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4756 | **wield** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4757 | **governments-not** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4758 | **languishing** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4759 | **alms-round** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4760 | **sworn** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4761 | **intimately** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4762 | **paltry** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4763 | **insignifi** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4764 | **cant** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4765 | **deprivation** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4766 | **well-off** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4767 | **merry** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4768 | **nightfall** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4769 | **unparalleled** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4770 | **aparantaka** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4771 | **more-and** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4772 | **ever-changing** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4773 | **mediocrity** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4774 | **eloquent** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4775 | **despis** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4776 | **liar** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4777 | **common-sense** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4778 | **trusted** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4779 | **esteemed** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4780 | **busily** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4781 | **tricked** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4782 | **conscientious** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4783 | **stantly** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4784 | **poignant** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4785 | **transitoriness** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4786 | **feud** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4787 | **gelong** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4788 | **pigeon** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4789 | **exterminate** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4790 | **commander** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4791 | **superficial** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4792 | **beasts-all** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4793 | **lifesustaining** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4794 | **fatality** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4795 | **eating-the** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4796 | **oblivious** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4797 | **mear** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4798 | **unhealthy** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4799 | **tumour** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4800 | **disorder** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4801 | **dropsy** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4802 | **incite** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4803 | **decrepit** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4804 | **linger** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4805 | **glued** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4806 | **candle-flame** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4807 | **celebrity** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4808 | **sorrowful** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4809 | **escaping** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4810 | **bhik** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4811 | **ractice** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4812 | **sameness** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4813 | **insatiable** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4814 | **ha-ha** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4815 | **proudest** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4816 | **engross** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4817 | **revel** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4818 | **abhorrent** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4819 | **sealing** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4820 | **vaster** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4821 | **twinkling** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4822 | **headlong** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4823 | **scorching** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4824 | **perimeter** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4825 | **white-hot** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4826 | **smith-there** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4827 | **searingly** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4828 | **incandescent** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4829 | **snowflake** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4830 | **furiously** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4831 | **weapons-a** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4832 | **armoury** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4833 | **fifty** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4834 | **firebrand** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4835 | **cross-rule** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4836 | **on-which** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4837 | **hacked** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4838 | **whirling** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4839 | **ram** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4840 | **butt** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4841 | **horn-tip** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4842 | **spewing** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4843 | **scream** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4844 | **shove** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4845 | **howl** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4846 | **cauldron** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4847 | **impale** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4848 | **heel** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4849 | **edifice** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4850 | **bellow** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4851 | **leopard-skin** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4852 | **indi** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4853 | **tinguishable** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4854 | **razor-edged** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4855 | **directions-the** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4856 | **northeast-stand** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4857 | **purged** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4858 | **shady** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4859 | **putrescent** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4860 | **brazier** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4861 | **corpses-corps** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4862 | **dogs-all** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4863 | **decomposing** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4864 | **decompose** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4865 | **foulest** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4866 | **stench** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4867 | **mire** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4868 | **thrilled** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4869 | **slender** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4870 | **heal** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4871 | **it-only** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4872 | **excruciatingly** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4873 | **reconstitute** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4874 | **eagerly** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4875 | **stabbing** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4876 | **metallic** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4877 | **unshake** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4878 | **glacier** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4879 | **perpetually** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4880 | **enveloped** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4881 | **lamentation** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4882 | **ofutpala-like** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4883 | **petal-like** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4884 | **unbearably** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4885 | **broom** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4886 | **yutso** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4887 | **ngonmo** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4888 | **snpo** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4889 | **kangchen** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4890 | **zemaguru** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4891 | **exclaiming** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4892 | **misused** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4893 | **spanned** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4894 | **squirming** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4895 | **tsangla** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4896 | **tanakchen** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4897 | **angtong** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4898 | **exercis** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4899 | **gullet** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4900 | **kidney** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4901 | **shawl** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4902 | **munch** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4903 | **leisurely** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4904 | **steaming** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4905 | **whisker** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4906 | **reddish** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4907 | **tinge** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4908 | **palden** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4909 | **chokyong** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4910 | **ngor** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4911 | **ngulda** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4912 | **tree-trunk** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4913 | **aher** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4914 | **pogye** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4915 | **all-powerful** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4916 | **dignitary** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4917 | **srm** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4918 | **adulterer** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4919 | **infidelity** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4920 | **lunch-hour** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4921 | **obdurate** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4922 | **impulsively** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4923 | **exhausted-only** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4924 | **stony** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4925 | **torture** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4926 | **sroi** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4927 | **sombre** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4928 | **horse-hair** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4929 | **if-finally-enough** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4930 | **grass-like** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4931 | **devouring** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4932 | **exquisitely** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4933 | **bedecked** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4934 | **ravishing** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4935 | **srol** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4936 | **daughter-in** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4937 | **shaven-skulled** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4938 | **proposition** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4939 | **bald-head** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4940 | **ablution** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4941 | **squashed** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4942 | **jostling** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4943 | **thing-except** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4944 | **shindre** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4945 | **jungpo** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4946 | **theurang** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4947 | **relive** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4948 | **insanity** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4949 | **teem** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4950 | **reptile** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4951 | **shellfish** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4952 | **beer-barrel** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4953 | **burrow** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4954 | **torturing** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4955 | **devices-net** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4956 | **oyster** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4957 | **ass** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4958 | **domesticated** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4959 | **executioner** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4960 | **stare** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4961 | **pierced** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4962 | **yoked** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4963 | **continual** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4964 | **pelted** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4965 | **long-lasting** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4966 | **lated** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4967 | **scorning** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4968 | **old-age** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4969 | **hated** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4970 | **wracked** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4971 | **spasm** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4972 | **parasite** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4973 | **news-and** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4974 | **imme** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4975 | **diately** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4976 | **constancy** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4977 | **celebration** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4978 | **concoction** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4979 | **six-brick** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4980 | **dotok** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4981 | **dzo** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4982 | **perforated** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4983 | **chafed** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4984 | **lambskin** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4985 | **flea** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4986 | **tick** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4987 | **decapitated** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4988 | **die-they** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4989 | **incessantly** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4990 | **aquatic** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4991 | **threshing** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4992 | **untainted** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4993 | **suckle** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4994 | **tethered** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4995 | **paus** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4996 | **milk-their** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4997 | **drink-can** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4998 | **starved** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 4999 | **skeleton-like** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5000 | **stagger** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5001 | **constituting** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5002 | **happiness-food** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5003 | **of-are** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5004 | **interpose** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5005 | **embryonic** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5006 | **jelly** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5007 | **viscous** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5008 | **ellipse** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5009 | **oblong** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5010 | **oval** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5011 | **appendage** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5012 | **sense-organ** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5013 | **suffocating** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5014 | **uterus** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5015 | **buffeted** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5016 | **cervix** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5017 | **pelvi** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5018 | **draw-plate** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5019 | **wrenched** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5020 | **ever-unfinished** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5021 | **eyesight** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5022 | **articulate** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5023 | **unintelligible** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5024 | **mumble** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5025 | **impa** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5026 | **tient** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5027 | **scorned** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5028 | **shrunk** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5029 | **dazed** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5030 | **trampled** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5031 | **waist** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5032 | **gingerly** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5033 | **arthritic** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5034 | **cheek-bone** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5035 | **dull-witted** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5036 | **giddy** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5037 | **brightness** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5038 | **humour** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5039 | **illnesses-those** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5040 | **bile** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5041 | **on-arise** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5042 | **twinge** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5043 | **strike-however** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5044 | **radiantly** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5045 | **prime-we** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5046 | **crumple** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5047 | **bloodletting** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5048 | **cautery** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5049 | **morbid** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5050 | **epilepsy** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5051 | **short-tempered** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5052 | **foreboding** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5053 | **departure-you** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5054 | **menacing** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5055 | **hoarse** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5056 | **brigand** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5057 | **envied** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5058 | **devil** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5059 | **adage** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5060 | **compatriot** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5061 | **dangers-and** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5062 | **inescapably** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5063 | **through-but** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5064 | **wheedle** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5065 | **gods-a** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5066 | **malice** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5067 | **deign** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5068 | **swindler** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5069 | **tether** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5070 | **imperiously** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5071 | **monopolizing** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5072 | **sly** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5073 | **ravaging** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5074 | **incurable** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5075 | **lllead** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5076 | **dining** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5077 | **expend** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5078 | **enterpris** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5079 | **accomplished-and** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5080 | **dharmaless** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5081 | **whence** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5082 | **aren** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5083 | **nowa** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5084 | **decaying** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5085 | **everything-good** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5086 | **not-highly** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5087 | **appalled** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5088 | **pitiful** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5089 | **multiplicity** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5090 | **quarrelling** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5091 | **tree-whose** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5092 | **donning** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5093 | **weapons-vajra** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5094 | **taller** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5095 | **demi** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5096 | **dispatch** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5097 | **all-protector** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5098 | **crazed** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5099 | **fastened** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5100 | **exuberant** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5101 | **wore** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5102 | **perspired** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5103 | **sweetheart** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5104 | **powerlessness** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5105 | **birthplace** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5106 | **suffering-and** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5107 | **murderous** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5108 | **hell-fire** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5109 | **mindlessness** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5110 | **snow-mountain** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5111 | **she-monkey** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5112 | **pur** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5113 | **larika** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5114 | **pundarika** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5115 | **intimate** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5116 | **heartbroken** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5117 | **slighdy** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5118 | **extolled** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5119 | **sense-door** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5120 | **frighten** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5121 | **saligha** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5122 | **assembly-hall** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5123 | **balcony** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5124 | **overlooking** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5125 | **preoccupations-parent** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5126 | **possessions-like** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5127 | **mist** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5128 | **esteem** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5129 | **worm-fodder** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5130 | **watch-tower** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5131 | **gloomy-face** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5132 | **cheery** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5133 | **all-determining** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5134 | **consign** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5135 | **do-i** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5136 | **underfoot** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5137 | **gusto** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5138 | **wher** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5139 | **tea-party** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5140 | **hoove** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5141 | **swamped** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5142 | **fleece** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5143 | **lambing** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5144 | **dowry** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5145 | **in-law** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5146 | **pretentious** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5147 | **breast-meat** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5148 | **tripe** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5149 | **bloody** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5150 | **willow-wand** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5151 | **indeed-considering** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5152 | **mothers-we** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5153 | **thereupon** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5154 | **sundered** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5155 | **involved-a** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5156 | **seiz** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5157 | **lash** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5158 | **thong** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5159 | **bluish** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5160 | **not-or** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5161 | **subterfuge** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5162 | **deceiving** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5163 | **debilitate** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5164 | **poring** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5165 | **overpower** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5166 | **shoulder-blade** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5167 | **daybreak** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5168 | **wink** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5169 | **torrna-offering** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5170 | **carne** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5171 | **disdainfully** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5172 | **railed** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5173 | **dharma-practitioner** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5174 | **slander** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5175 | **ware** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5176 | **extort** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5177 | **haggling** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5178 | **covet** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5179 | **vaisravana** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5180 | **nefarious** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5181 | **corrupting** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5182 | **awl** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5183 | **laity** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5184 | **gravest** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5185 | **particu** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5186 | **lar** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5187 | **masturbation** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5188 | **bereavement** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5189 | **menstruation** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5190 | **recov** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5191 | **ery** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5192 | **child-birth** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5193 | **prepubescent** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5194 | **devastatingly** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5195 | **imposter** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5196 | **thanksgiving** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5197 | **chastised** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5198 | **concept-bound** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5199 | **second-and** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5200 | **rude** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5201 | **sweetly** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5202 | **not-such** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5203 | **aimlessly** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5204 | **libidinous** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5205 | **cussing** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5206 | **disturb** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5207 | **gossip-monger** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5208 | **rituals-just** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5209 | **perfunctorily** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5210 | **sorcerers-i** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5211 | **cast-iron** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5212 | **lethally** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5213 | **life-artery** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5214 | **desirous** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5215 | **acquisitive** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5216 | **contemplat** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5217 | **agreeable** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5218 | **invent** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5219 | **malicious** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5220 | **catego** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5221 | **ry** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5222 | **eternally** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5223 | **roundness** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5224 | **iridescent** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5225 | **sharpened** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5226 | **bad-all** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5227 | **spontane** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5228 | **ously** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5229 | **unvirtuous** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5230 | **mistakenly** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5231 | **meri** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5232 | **torious** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5233 | **resuscitate** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5234 | **negate** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5235 | **impulse-extremely** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5236 | **ignorance-motivating** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5237 | **instinct** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5238 | **newborn** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5239 | **adulthood** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5240 | **assaulted** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5241 | **pillage** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5242 | **bandit** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5243 | **raids-often** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5244 | **life-or** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5245 | **bereft** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5246 | **destitute** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5247 | **preta-like** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5248 | **indulged** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5249 | **hating** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5250 | **belittled** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5251 | **hurling** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5252 | **argumentative** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5253 | **defiantly** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5254 | **grudgingly** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5255 | **recon** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5256 | **ciling** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5257 | **insulting** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5258 | **or-worse** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5259 | **still-to** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5260 | **kapila** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5261 | **horse-head** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5262 | **ox-head** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5263 | **fish-like** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5264 | **extol** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5265 | **self-assurance** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5266 | **joyless** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5267 | **mortally** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5268 | **insecu** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5269 | **rity** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5270 | **inhabit** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5271 | **gorge** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5272 | **terrain** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5273 | **infertile** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5274 | **untimely** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5275 | **inhospitable** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5276 | **proliferate** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5277 | **example-or** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5278 | **animals-i** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5279 | **vaisakha** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5280 | **reconcile** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5281 | **uninterrupted** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5282 | **experiences-from** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5283 | **hell-arise** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5284 | **impel** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5285 | **identifiable** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5286 | **sravasti** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5287 | **pole** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5288 | **writhed** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5289 | **matropakara** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5290 | **tied-up** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5291 | **writhing** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5292 | **laughed** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5293 | **acacia** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5294 | **splinter-the** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5295 | **parivraji** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5296 | **kas** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5297 | **succumbed** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5298 | **jeta** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5299 | **suf** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5300 | **fering** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5301 | **clairvoyant** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5302 | **woodland** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5303 | **stoking** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5304 | **punish** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5305 | **debili** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5306 | **tated** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5307 | **nagar** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5308 | **juna** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5309 | **we-whose** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5310 | **innumerable-ever** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5311 | **underestimate** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5312 | **minutest** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5313 | **wedding** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5314 | **fistful** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5315 | **antisarar** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5316 | **devo** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5317 | **profuse** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5318 | **vajrap** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5319 | **pirate** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5320 | **non-returning** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5321 | **hopelessly** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5322 | **wrong-doer** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5323 | **impression-or** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5324 | **generator** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5325 | **moti** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5326 | **vation** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5327 | **neatly** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5328 | **kungyal** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5329 | **stumbled** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5330 | **penyulgyal** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5331 | **yoghurt-addict** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5332 | **self-centredness** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5333 | **expectant** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5334 | **ravi** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5335 | **cutter** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5336 | **tormented-in** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5337 | **tormented-by** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5338 | **prattling** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5339 | **materialism** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5340 | **ideology** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5341 | **tiness** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5342 | **authentically** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5343 | **heaping** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5344 | **ments-and** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5345 | **dhara** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5346 | **unreal** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5347 | **mingle** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5348 | **practices-the** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5349 | **formless** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5350 | **insight-should** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5351 | **take-while** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5352 | **impregnated** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5353 | **moist** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5354 | **whomever** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5355 | **vow-the** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5356 | **knowl** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5357 | **practices-out** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5358 | **wardly** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5359 | **actualized** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5360 | **observance** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5361 | **unbroken** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5362 | **preoc** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5363 | **cupation** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5364 | **seing** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5365 | **resolutely** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5366 | **nephew** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5367 | **descendant** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5368 | **mundane** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5369 | **reasons-like** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5370 | **priestly** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5371 | **suited** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5372 | **pedestal** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5373 | **visitor** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5374 | **fainted** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5375 | **ape** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5376 | **idiot** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5377 | **well-bound** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5378 | **leaping** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5379 | **venomous** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5380 | **coiled** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5381 | **beguiled** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5382 | **unmistaken** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5383 | **uniquely** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5384 | **ple** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5385 | **expediently** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5386 | **noblest** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5387 | **unfailingly** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5388 | **downpour** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5389 | **extinguish** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5390 | **agement** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5391 | **charting** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5392 | **quenching** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5393 | **showered** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5394 | **wayfarer** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5395 | **ferryman** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5396 | **stable-minded** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5397 | **all-such** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5398 | **sittra** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5399 | **anged** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5400 | **resentful** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5401 | **reprimand** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5402 | **resent** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5403 | **disregarding** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5404 | **incomprehensibly** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5405 | **ruined** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5406 | **tub** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5407 | **grilled** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5408 | **snapping** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5409 | **flawless** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5410 | **deceitful** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5411 | **glimpsed** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5412 | **outburst** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5413 | **treading** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5414 | **vanity** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5415 | **discontent** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5416 | **unconsidered** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5417 | **insincere** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5418 | **laughing** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5419 | **joking** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5420 | **chat** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5421 | **awe** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5422 | **casualness** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5423 | **solicitously** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5424 | **vainly** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5425 | **scowl** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5426 | **ill-considered** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5427 | **composure** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5428 | **conver** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5429 | **self-im** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5430 | **portance** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5431 | **untiringly** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5432 | **gliding** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5433 | **delighting** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5434 | **spoiling** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5435 | **bored** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5436 | **steadfastness** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5437 | **tasting** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5438 | **better-off** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5439 | **fellow-voyager** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5440 | **bean-tsampa** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5441 | **fruitful-thi** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5442 | **contemplation** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5443 | **portrait** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5444 | **epitomiz** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5445 | **assiduous** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5446 | **examina** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5447 | **abound** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5448 | **deception** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5449 | **voice-or** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5450 | **name-can** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5451 | **restless** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5452 | **transfixed** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5453 | **limb-just** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5454 | **ropa** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5455 | **bodily** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5456 | **prajna** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5457 | **go-and** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5458 | **abode** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5459 | **circumference** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5460 | **sixty-eight** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5461 | **blissfully** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5462 | **prais** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5463 | **sadapraru** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5464 | **dita** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5465 | **marrow** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5466 | **spurted** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5467 | **smash** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5468 | **inflicting** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5469 | **reassumed** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5470 | **domain** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5471 | **mersed** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5472 | **prajaa** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5473 | **deco** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5474 | **censer** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5475 | **wafted** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5476 | **aloe-wood** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5477 | **coffer** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5478 | **pranaparamita** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5479 | **sada** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5480 | **prarudita** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5481 | **sprinkle** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5482 | **sprinkled** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5483 | **lion-throne** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5484 | **expounded** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5485 | **buddhas-a** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5486 | **melodious** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5487 | **oiling** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5488 | **bearable** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5489 | **streamed** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5490 | **these-twenty-four** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5491 | **forbade** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5492 | **pandita-gatekeeper** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5493 | **magadha** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5494 | **insistently** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5495 | **compassion-why** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5496 | **gatekeeper** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5497 | **retorted** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5498 | **ngari** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5499 | **gungthang** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5500 | **sherab** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5501 | **thopa-ga** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5502 | **yungdrung** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5503 | **throgyal** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5504 | **lharje** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5505 | **nupchung** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5506 | **repenting** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5507 | **eminently** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5508 | **hail-if** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5509 | **night-and** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5510 | **suffuse** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5511 | **tingled** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5512 | **tarma** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5513 | **dode** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5514 | **continu** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5515 | **reckon** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5516 | **acquiesced** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5517 | **twelve-pillared** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5518 | **sanctuary** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5519 | **meton** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5520 | **tsonpo** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5521 | **tsangrong** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5522 | **sarilvara** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5523 | **tsurton** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5524 | **wange** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5525 | **dol** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5526 | **guhyasamaja** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5527 | **ngokton** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5528 | **chador** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5529 | **shung** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5530 | **khok** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5531 | **powerment** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5532 | **dispersed** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5533 | **mahasiddha** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5534 | **tacarya** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5535 | **floundering** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5536 | **byway** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5537 | **vajrasativa** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5538 | **life-story** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5539 | **sprout** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5540 | **bestowing** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5541 | **departed-i** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5542 | **simple-minded** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5543 | **caretaker** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5544 | **food-offering** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5545 | **butter-lamp** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5546 | **imagined** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5547 | **dunking** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5548 | **sputter** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5549 | **tthrow** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5550 | **though-so** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5551 | **jowo-act** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5552 | **wrong-the** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5553 | **leavingjetsun** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5554 | **unwavering** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5555 | **realms-the** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5556 | **realm-motivate** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5557 | **beings-our** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5558 | **beginnin** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5559 | **gless** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5560 | **time-are** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5561 | **dhar** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5562 | **makaya** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5563 | **indestructible** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5564 | **all-pervasive** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5565 | **mindstream** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5566 | **inseparability** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5567 | **irregulari** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5568 | **twig** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5569 | **entrancing** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5570 | **lion** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5571 | **multi-coloured** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5572 | **cloak** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5573 | **sleeved** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5574 | **tunic** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5575 | **samantab** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5576 | **jnanasiltra** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5577 | **consort-the** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5578 | **trisongdetsen** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5579 | **nirmanakya** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5580 | **garbed** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5581 | **hood-the** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5582 | **right-hand** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5583 | **families-mafijusri** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5584 | **left-hand** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5585 | **alms-bowl** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5586 | **topmost** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5587 | **resonate** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5588 | **melody** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5589 | **consonant** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5590 | **dharma-protector** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5591 | **leaking** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5592 | **detest** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5593 | **refuge-prayer** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5594 | **precedence** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5595 | **kinder** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5596 | **possessions-the** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5597 | **aunt** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5598 | **palmo** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5599 | **assailed** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5600 | **invade** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5601 | **fearlessness** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5602 | **impelled** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5603 | **slingstone** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5604 | **whirring** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5605 | **tirthika-who** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5606 | **criticiz** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5607 | **breeze** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5608 | **day-come** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5609 | **rend** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5610 | **doud** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5611 | **healing** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5612 | **life-comfort** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5613 | **whatever-spring** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5614 | **create-prostration** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5615 | **disciples-to** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5616 | **nicknamed** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5617 | **pawned** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5618 | **saliva** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5619 | **maxim** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5620 | **vajradhatvishvari** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5621 | **seed-syllable** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5622 | **disre** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5623 | **spect** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5624 | **seventy** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5625 | **stanza** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5626 | **reparation** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5627 | **tenuous** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5628 | **people-the** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5629 | **moulded** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5630 | **it-all** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5631 | **seductive** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5632 | **gullible** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5633 | **decadence** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5634 | **deceived** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5635 | **seduction** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5636 | **invaded** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5637 | **hesita** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5638 | **guis** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5639 | **oppos** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5640 | **disciples-none** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5641 | **goggle** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5642 | **effigy** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5643 | **goat-pen** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5644 | **legitimately** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5645 | **perni** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5646 | **cious** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5647 | **malevolent** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5648 | **confi** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5649 | **dence** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5650 | **pacified** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5651 | **harm-the** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5652 | **makers-will** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5653 | **quarter-pint** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5654 | **faint-hearted** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5655 | **pathetic** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5656 | **even-minded** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5657 | **on-while** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5658 | **low-caste** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5659 | **stung** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5660 | **brushing** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5661 | **accidentally** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5662 | **diffi** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5663 | **culty** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5664 | **all-those** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5665 | **you-train** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5666 | **beings-whether** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5667 | **between-a** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5668 | **mindless** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5669 | **distinc** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5670 | **devoting** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5671 | **cosy** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5672 | **glared** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5673 | **endeavouring** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5674 | **jeal** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5675 | **ousy** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5676 | **hypocrite** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5677 | **ity** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5678 | **despise** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5679 | **distressed** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5680 | **khotan** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5681 | **mafljusri** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5682 | **dismembered** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5683 | **vanquished** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5684 | **chick** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5685 | **torment-a** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5686 | **bursting** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5687 | **butchered** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5688 | **delay-thi** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5689 | **barbarity** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5690 | **twist** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5691 | **belly-hair** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5692 | **weal** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5693 | **grunting** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5694 | **backside** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5695 | **horseback** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5696 | **sidesaddle** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5697 | **stumble** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5698 | **sympathy** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5699 | **animal-a** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5700 | **example-that** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5701 | **paralyzing** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5702 | **blood-blister** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5703 | **gutted** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5704 | **bled** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5705 | **flesh-eating** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5706 | **resourceful** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5707 | **twine** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5708 | **ring-hole** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5709 | **gouged** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5710 | **hoisted** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5711 | **yak-hair** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5712 | **cord** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5713 | **aching** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5714 | **rasp** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5715 | **rump** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5716 | **bruised** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5717 | **stirrup** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5718 | **exhausting** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5719 | **help-impartial** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5720 | **ganging** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5721 | **mischievous** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5722 | **intoning** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5723 | **impartial** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5724 | **horrible** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5725 | **hurled** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5726 | **exorcising** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5727 | **intimidating** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5728 | **spanking** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5729 | **pandering** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5730 | **wrongdoer** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5731 | **hateful** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5732 | **enemies-protecting** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5733 | **hatred-were** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5734 | **expel** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5735 | **indeed-not** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5736 | **hate-a** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5737 | **chong** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5738 | **vinayaka** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5739 | **strode** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5740 | **recogniz** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5741 | **cleric** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5742 | **cle** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5743 | **bleeding** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5744 | **decorate** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5745 | **rites-they** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5746 | **shred** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5747 | **compa** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5748 | **boiled** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5749 | **protectors-we** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5750 | **bodhisat** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5751 | **tvas-then** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5752 | **gleefully** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5753 | **mantrayana-namely** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5754 | **succulent** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5755 | **heedlessly** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5756 | **slaugh** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5757 | **murdering** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5758 | **prowl** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5759 | **roam** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5760 | **gnaw** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5761 | **innard** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5762 | **lookout** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5763 | **killer** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5764 | **inflamed** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5765 | **shaking** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5766 | **intimacy** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5767 | **hell-unless** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5768 | **preying** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5769 | **bon** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5770 | **sublimity** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5771 | **conspicuous** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5772 | **encapsulate** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5773 | **dharmas** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5774 | **bared** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5775 | **abhid** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5776 | **harma** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5777 | **prakasasila** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5778 | **sarighab** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5779 | **kukku** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5780 | **apada** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5781 | **persistence** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5782 | **stroking** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5783 | **maggot** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5784 | **foreleg** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5785 | **halo** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5786 | **shoulder-all** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5787 | **ofmaitreya** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5788 | **feelings-like** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5789 | **contented** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5790 | **displeased** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5791 | **alarmingly** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5792 | **logician** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5793 | **tsakpuwa** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5794 | **deva** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5795 | **datta** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5796 | **prodigious** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5797 | **kunpang** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5798 | **rakgyal** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5799 | **darkened** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5800 | **negativity** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5801 | **vile** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5802 | **physique** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5803 | **correspondingly** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5804 | **summarize** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5805 | **ferryboat** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5806 | **jasako** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5807 | **materialized** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5808 | **beheaded** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5809 | **scabrous** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5810 | **shaven-headed** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5811 | **bigot** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5812 | **panicular** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5813 | **woke** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5814 | **benevolent** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5815 | **activities-prostration** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5816 | **circumam** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5817 | **bulation** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5818 | **hean** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5819 | **jackal** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5820 | **tative** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5821 | **discriminating** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5822 | **thusness** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5823 | **foundering** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5824 | **friendless** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5825 | **binh** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5826 | **suvarl** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5827 | **advipa** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5828 | **suvarnadvipa** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5829 | **swindle** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5830 | **either-try** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5831 | **pinprick** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5832 | **pain-we** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5833 | **thumbnail** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5834 | **enslaved** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5835 | **trungpa** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5836 | **sinachen** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5837 | **kamarupa** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5838 | **goaded** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5839 | **kamarapa** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5840 | **cart** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5841 | **sea-captain** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5842 | **mercha** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5843 | **plank** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5844 | **ashore** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5845 | **intoxication** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5846 | **ravishingly** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5847 | **couch** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5848 | **pulver** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5849 | **ized** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5850 | **smashed** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5851 | **ulti** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5852 | **mate** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5853 | **chak** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5854 | **shingwa** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5855 | **langthang** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5856 | **succe** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5857 | **sor** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5858 | **stfipa** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5859 | **selfishness** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5860 | **subjugating** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5861 | **vaibhasika** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5862 | **cine-the** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5863 | **dozed** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5864 | **spat** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5865 | **scar** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5866 | **treatis** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5867 | **ceaselessly** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5868 | **donned** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5869 | **fervently** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5870 | **nivritta** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5871 | **palace-one** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5872 | **cubits-and** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5873 | **alternately** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5874 | **ketaka** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5875 | **saketa** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5876 | **largesse** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5877 | **organize** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5878 | **yanta** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5879 | **hard-to** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5880 | **raksasa** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5881 | **oblation** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5882 | **smitten** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5883 | **grief** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5884 | **ter** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5885 | **veda** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5886 | **coveting** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5887 | **enchantment** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5888 | **it-for** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5889 | **queen-hi** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5890 | **wife-in** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5891 | **curse** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5892 | **unreliable** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5893 | **numer** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5894 | **ous** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5895 | **wasn** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5896 | **perfections-generosity** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5897 | **concentration-are** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5898 | **masterful** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5899 | **moan** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5900 | **starvation** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5901 | **preta-realm** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5902 | **daring** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5903 | **gladly** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5904 | **cunning** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5905 | **mandabhadri** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5906 | **brewed** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5907 | **emptying** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5908 | **expound** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5909 | **evil-doing** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5910 | **undertak** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5911 | **actions-even** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5912 | **amusing** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5913 | **wronged** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5914 | **slandered** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5915 | **shatter** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5916 | **zeal** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5917 | **accus** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5918 | **unjustly** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5919 | **effect-a** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5920 | **grudge-will** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5921 | **anger-so** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5922 | **puff** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5923 | **humiliated** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5924 | **touchiness** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5925 | **admiringly** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5926 | **marry** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5927 | **sew** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5928 | **double-pointed** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5929 | **nairaftjana** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5930 | **asceticism** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5931 | **nettle** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5932 | **greenish** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5933 | **tenaciously** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5934 | **hopeless** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5935 | **melong** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5936 | **practi** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5937 | **bark** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5938 | **lakhe** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5939 | **rabjam** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5940 | **snowed** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5941 | **well-be** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5942 | **mourn** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5943 | **gristle** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5944 | **vom** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5945 | **ited** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5946 | **recount** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5947 | **bod** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5948 | **hisattva** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5949 | **hardhip** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5950 | **druk** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5951 | **karpo** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5952 | **unhurriedly** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5953 | **beware** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5954 | **deathbed** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5955 | **immedi** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5956 | **ately** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5957 | **coward** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5958 | **dancing-girl** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5959 | **time-one** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5960 | **them-such** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5961 | **clump** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5962 | **idleness** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5963 | **tenacity** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5964 | **reputed** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5965 | **sporadically** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5966 | **excite** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5967 | **spous** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5968 | **relatives-even** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5969 | **birth-are** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5970 | **shiwa** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5971 | **heedless** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5972 | **trifling** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5973 | **forethought** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5974 | **roving** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5975 | **squandered** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5976 | **academia** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5977 | **path-disenchantment** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5978 | **absorption-arise** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5979 | **natu** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5980 | **tranquillity** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5981 | **bustling** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5982 | **dispensed** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5983 | **fascinated** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5984 | **concept-free** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5985 | **ofvairocana** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5986 | **concentra** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5987 | **confining** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5988 | **substantiality** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5989 | **gandharva** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5990 | **them-the** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5991 | **scendent** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5992 | **twenty-two** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5993 | **thirty-six** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5994 | **contami** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5995 | **nate** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5996 | **self-aggrandizement** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5997 | **pline** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5998 | **giving-offering** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 5999 | **tiring** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6000 | **subdivision** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6001 | **summing** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6002 | **guile** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6003 | **non-attachment** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6004 | **contentment** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6005 | **thinker** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6006 | **nutshell** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6007 | **nirvina** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6008 | **non-dwelling** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6009 | **grasped** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6010 | **conceptualize** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6011 | **bodhicitta-emptiness** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6012 | **nnhika** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6013 | **relegate** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6014 | **bodhi** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6015 | **citta** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6016 | **intensively** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6017 | **frescoe** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6018 | **plastered** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6019 | **sincerest** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6020 | **unimpeded** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6021 | **miracles-if** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6022 | **be-realization** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6023 | **on-you** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6024 | **askedjetsun** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6025 | **disso** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6026 | **ciating** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6027 | **nyethang** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6028 | **kyung** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6029 | **lhangtsang** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6030 | **discursive** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6031 | **dividing** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6032 | **chegom** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6033 | **indivi** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6034 | **ible** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6035 | **non-conceptualization** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6036 | **non-action** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6037 | **churn** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6038 | **purport** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6039 | **actions-except** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6040 | **actions-be** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6041 | **samayas-there** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6042 | **atapa** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6043 | **ninety-nine** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6044 | **carelessly** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6045 | **attentive** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6046 | **darsaka** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6047 | **sailkara** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6048 | **mouthing** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6049 | **anti** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6050 | **dote** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6051 | **buddhas-in** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6052 | **appli** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6053 | **cation** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6054 | **peril** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6055 | **dreadful** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6056 | **wickedness** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6057 | **concealing** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6058 | **trepidation** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6059 | **sukhavati** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6060 | **disillusioned** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6061 | **vajrasattva-purification** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6062 | **signify** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6063 | **fifteenth** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6064 | **reabsorb** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6065 | **sambhogakaya-the** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6066 | **headband** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6067 | **scarf** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6068 | **earring** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6069 | **armlet** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6070 | **bracelet** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6071 | **anklet** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6072 | **vajratopa** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6073 | **vividly** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6074 | **tangka** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6075 | **fresco** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6076 | **inert** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6077 | **pupil** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6078 | **atom** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6079 | **transgre** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6080 | **dishonourable** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6081 | **gooseflesh** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6082 | **glistening** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6083 | **dripping** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6084 | **flushed** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6085 | **expelled** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6086 | **spider** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6087 | **scorpion** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6088 | **toad** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6089 | **tadpole** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6090 | **vapour** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6091 | **orifice** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6092 | **personification** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6093 | **expectantly** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6094 | **earth-every** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6095 | **flesh-are** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6096 | **score** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6097 | **vertically** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6098 | **sixty-four** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6099 | **svabhavika** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6100 | **smilingly** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6101 | **behi** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6102 | **fringed** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6103 | **thousand-spoked** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6104 | **result-the** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6105 | **multi-col** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6106 | **oured** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6107 | **pronouncing** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6108 | **humming** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6109 | **rapakaya** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6110 | **spon** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6111 | **taneously** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6112 | **reabsorbing** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6113 | **vanishing** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6114 | **officiating** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6115 | **officiant** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6116 | **ornate** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6117 | **intonation** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6118 | **blaring** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6119 | **trumpet** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6120 | **drum** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6121 | **recited-at** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6122 | **goings-on** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6123 | **clattering** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6124 | **puspe** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6125 | **dhupe** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6126 | **travesty** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6127 | **swallowing** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6128 | **soul** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6129 | **grimy** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6130 | **scrupulous** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6131 | **tiresome** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6132 | **undistracted** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6133 | **laywoman** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6134 | **atiga** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6135 | **non-existent** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6136 | **valley-i** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6137 | **unfit** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6138 | **infecting** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6139 | **brightly** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6140 | **danced** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6141 | **samaya-and** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6142 | **delirious** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6143 | **urgyenpa** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6144 | **vanish** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6145 | **earthenware** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6146 | **denting** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6147 | **curing** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6148 | **unremittingly** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6149 | **joke** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6150 | **obscu** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6151 | **fooled** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6152 | **interdependently** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6153 | **virupa** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6154 | **replete** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6155 | **bell-metal** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6156 | **turquois** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6157 | **sapphire** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6158 | **arura** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6159 | **kyurura** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6160 | **puls** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6161 | **direction-meaning** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6162 | **dha** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6163 | **obhya** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6164 | **ratnasambhava** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6165 | **amoghasiddhi** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6166 | **stacked-up** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6167 | **altar** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6168 | **wiping** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6169 | **veil** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6170 | **woollen** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6171 | **chogyal** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6172 | **pakpa** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6173 | **nyingma** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6174 | **bhumi** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6175 | **sprinkling** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6176 | **ung** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6177 | **thumb** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6178 | **rekhe** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6179 | **purvavideha** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6180 | **deha** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6181 | **videha** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6182 | **inexhaustibly** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6183 | **victorious** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6184 | **unfilled** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6185 | **first-order** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6186 | **second-order** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6187 | **millionfold** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6188 | **third-order** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6189 | **buddha-sakyamuni** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6190 | **endurance** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6191 | **graced** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6192 | **infinitely** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6193 | **unborn** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6194 | **ache** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6195 | **seven-element** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6196 | **important-a** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6197 | **do-to** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6198 | **saturate** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6199 | **scented** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6200 | **generously** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6201 | **reasons-and** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6202 | **yourself-that** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6203 | **fooling** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6204 | **dirtily** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6205 | **mouldy** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6206 | **lamp-offering** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6207 | **rancid** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6208 | **shelze** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6209 | **consi** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6210 | **tency** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6211 | **torma-dough** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6212 | **distinctively** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6213 | **sublimely** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6214 | **scavenger** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6215 | **rice-gruel** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6216 | **maqc** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6217 | **fingernail** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6218 | **oily** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6219 | **rupakaya** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6220 | **converse** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6221 | **barbaric** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6222 | **exclaim** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6223 | **aiota** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6224 | **tree-or** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6225 | **world-even** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6226 | **rainbow-none** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6227 | **jaundice** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6228 | **cheerfully** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6229 | **dissipated** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6230 | **puri** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6231 | **fying** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6232 | **contradiction** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6233 | **tised** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6234 | **life-hermit** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6235 | **instance-use** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6236 | **clung** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6237 | **instantaneously** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6238 | **swaying** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6239 | **squealing** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6240 | **mother-the** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6241 | **consciousness-instantly** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6242 | **life-size** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6243 | **tripod** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6244 | **sizzle** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6245 | **foul** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6246 | **frothing** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6247 | **scum** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6248 | **exude** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6249 | **ridding** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6250 | **imperfection** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6251 | **billow** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6252 | **locality** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6253 | **teeming** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6254 | **deity-a** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6255 | **iaka** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6256 | **unfavour** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6257 | **swarm** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6258 | **activity-performing** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6259 | **appeasing** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6260 | **mother-use** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6261 | **scatter** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6262 | **victory-banner** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6263 | **overlord** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6264 | **underling** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6265 | **snatch** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6266 | **life-force** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6267 | **avenger** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6268 | **behind-the** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6269 | **suffering-the** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6270 | **life-restoring** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6271 | **offerer** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6272 | **vari** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6273 | **egated** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6274 | **variegated** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6275 | **grisly** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6276 | **slashing** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6277 | **bravado** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6278 | **hate-filled** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6279 | **clenching** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6280 | **lashing** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6281 | **whirl** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6282 | **inauspicious** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6283 | **compassion-but** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6284 | **ninefold** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6285 | **puny** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6286 | **retaliation-a** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6287 | **path-the** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6288 | **subjugation** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6289 | **instance-are** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6290 | **heaped** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6291 | **conceir** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6292 | **exultation** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6293 | **trampling** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6294 | **mischief** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6295 | **embar** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6296 | **rassed** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6297 | **mobilize** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6298 | **gyalgong** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6299 | **there-it** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6300 | **trance** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6301 | **insistent** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6302 | **predic** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6303 | **samaya-breaker** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6304 | **clergy** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6305 | **dream-like** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6306 | **momentarily** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6307 | **self-concern** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6308 | **maliciousness** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6309 | **others-and** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6310 | **fixation** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6311 | **qualifica** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6312 | **illustrative** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6313 | **untar** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6314 | **nished** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6315 | **alone-awaken** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6316 | **gotsangpa** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6317 | **rangrik** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6318 | **north-facing** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6319 | **devotional** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6320 | **uncontrived** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6321 | **vanquishing** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6322 | **nagabodhi** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6323 | **snatching** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6324 | **fervour** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6325 | **ligent** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6326 | **intellectualization** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6327 | **gyalmo** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6328 | **tsawarong** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6329 | **pang** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6330 | **meditation-band** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6331 | **hood** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6332 | **yana** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6333 | **enough-even** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6334 | **receptacle** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6335 | **vajrayogini** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6336 | **awakening** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6337 | **insubstantial** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6338 | **complexion** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6339 | **tinged** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6340 | **long-sleeved** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6341 | **gown** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6342 | **deerskin** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6343 | **adhara** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6344 | **unharmed** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6345 | **petalled** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6346 | **emblazoned** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6347 | **culmination** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6348 | **long-life** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6349 | **sprig** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6350 | **crook** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6351 | **mandarava** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6352 | **dried-up** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6353 | **looped** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6354 | **pennant** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6355 | **encircled** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6356 | **evenness** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6357 | **siddhi** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6358 | **pliramita** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6359 | **insurpassable** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6360 | **hrib** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6361 | **prelimi** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6362 | **nary** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6363 | **surrendering** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6364 | **passer-by** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6365 | **lurch** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6366 | **ordeal** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6367 | **reverence** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6368 | **bending** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6369 | **cupped** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6370 | **ful** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6371 | **hunchback** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6372 | **dwarf** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6373 | **them-so** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6374 | **deformed** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6375 | **impeccably** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6376 | **it-and** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6377 | **fruitless** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6378 | **proficient** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6379 | **head-dress** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6380 | **soaked** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6381 | **dye** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6382 | **dyed** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6383 | **successfully-but** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6384 | **violator** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6385 | **aya** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6386 | **evildoer** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6387 | **dharma-just** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6388 | **butter-bag** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6389 | **imprinted** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6390 | **clipping** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6391 | **usnisa** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6392 | **offering-that** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6393 | **ostentation** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6394 | **antabhadra** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6395 | **musical** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6396 | **ema** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6397 | **nated** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6398 | **multitudinous** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6399 | **mani** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6400 | **fested** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6401 | **cloudbank** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6402 | **perfecting** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6403 | **unmentionably** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6404 | **obstruction** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6405 | **doer** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6406 | **negative-not** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6407 | **ofi** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6408 | **nstruction** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6409 | **ostentatious** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6410 | **merus** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6411 | **ungrateful** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6412 | **subdivided** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6413 | **kriya** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6414 | **vedic** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6415 | **transmutation** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6416 | **cunda** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6417 | **non-conceptual** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6418 | **aigaramati** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6419 | **rub** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6420 | **wholeheartedly** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6421 | **dedica** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6422 | **ofvaisali** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6423 | **horrified** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6424 | **heruka** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6425 | **you-in** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6426 | **body-on** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6427 | **mala** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6428 | **orh** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6429 | **moon-crystal** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6430 | **actions-taking** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6431 | **misconduct-and** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6432 | **fro** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6433 | **nirm** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6434 | **actions-lying** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6435 | **chatter-and** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6436 | **views-and** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6437 | **streak** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6438 | **underly** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6439 | **svabhavikakaya** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6440 | **ardent** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6441 | **longing** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6442 | **you-up** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6443 | **vajrayogini-you** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6444 | **overexcited** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6445 | **lassitude** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6446 | **torpor** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6447 | **agitation** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6448 | **inseparably** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6449 | **naturalness** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6450 | **inconceivably** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6451 | **charac** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6452 | **teristic** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6453 | **listener** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6454 | **relate-neither** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6455 | **detail-the** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6456 | **translations-known** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6457 | **actualize** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6458 | **incon** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6459 | **ceivably** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6460 | **causal** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6461 | **mantrayana-kriya** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6462 | **bewilderment** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6463 | **doc** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6464 | **trine** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6465 | **acclaimed** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6466 | **kingja** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6467 | **nobility** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6468 | **lament** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6469 | **consented** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6470 | **kila** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6471 | **thotrengtsel** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6472 | **devabhadrapala** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6473 | **eldest** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6474 | **anandagarbha** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6475 | **devaputra** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6476 | **circling** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6477 | **pasupati** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6478 | **jewel-coloured** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6479 | **kausika** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6480 | **level-you** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6481 | **illuminate** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6482 | **symbolized** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6483 | **sponta** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6484 | **neously** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6485 | **primordially** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6486 | **vajraloka** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6487 | **vajraguhya** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6488 | **ratnaloka** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6489 | **ratnapada** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6490 | **padmakaya** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6491 | **padmaprabha** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6492 | **atha** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6493 | **gata** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6494 | **visuddhasiddha** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6495 | **siddhyaloka** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6496 | **viyoganta** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6497 | **irocana** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6498 | **all-victorious** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6499 | **vajrapal** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6500 | **dazzling** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6501 | **jewel-encrusted** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6502 | **ered** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6503 | **heart-son** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6504 | **uparaja** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6505 | **alokabhasvati** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6506 | **hap** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6507 | **pened** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6508 | **presage** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6509 | **gleaming** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6510 | **marvelling** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6511 | **vajrapaqi** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6512 | **twenty-thousand** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6513 | **empowered** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6514 | **sukhapala** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6515 | **kuhana** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6516 | **sarasiddhi** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6517 | **charnel** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6518 | **mahahe** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6519 | **compiler** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6520 | **nir** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6521 | **manakaya** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6522 | **dare** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6523 | **manife** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6524 | **uttering** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6525 | **polemic** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6526 | **compose** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6527 | **instantaneous** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6528 | **cessation** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6529 | **shosha** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6530 | **astrology** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6531 | **hastibhala** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6532 | **jnanasutra** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6533 | **pal** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6534 | **qita** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6535 | **tribe** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6536 | **descended** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6537 | **ape-an** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6538 | **crag-demoness** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6539 | **chao** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6540 | **satanika** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6541 | **webbed** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6542 | **eyelid** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6543 | **banished** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6544 | **ancient-nyatri** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6545 | **sarvanivaranaviskam** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6546 | **bhin** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6547 | **yumbu** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6548 | **lakhar** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6549 | **cintamani** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6550 | **kongjo-a** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6551 | **tara-and** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6552 | **nepalese** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6553 | **tritsun-a** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6554 | **bhrikuti** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6555 | **devavit** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6556 | **sirhha** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6557 | **ofj** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6558 | **ewel** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6559 | **akarmati** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6560 | **amradvipa** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6561 | **eleven-headed** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6562 | **ngam** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6563 | **lugong** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6564 | **lhazang** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6565 | **lupel** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6566 | **archive** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6567 | **discovering** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6568 | **forebear** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6569 | **gungtsen** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6570 | **nyang** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6571 | **resided** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6572 | **chimpu** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6573 | **insight** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6574 | **gomadeviya** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6575 | **aryapalo** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6576 | **tremble** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6577 | **subju** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6578 | **sariwari** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6579 | **horse-breeder** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6580 | **swineherd** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6581 | **poultryman** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6582 | **dog-breeder** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6583 | **trisher** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6584 | **dudjom** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6585 | **chim** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6586 | **sakyaprabha** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6587 | **shubu** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6588 | **palgyi** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6589 | **senge** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6590 | **protectress** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6591 | **oath** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6592 | **trakmar** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6593 | **three-storey** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6594 | **sub** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6595 | **enclosed** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6596 | **consecration** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6597 | **heart-disciples-the** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6598 | **nyangwen** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6599 | **antric** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6600 | **scroll** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6601 | **legacy** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6602 | **mindtt** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6603 | **together-the** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6604 | **lineage-from** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6605 | **recounting** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6606 | **already-with** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6607 | **dharma-companion** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6608 | **unmi** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6609 | **faultless** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6610 | **mind-consciousness** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6611 | **interme** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6612 | **diate** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6613 | **it-which** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6614 | **despicable** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6615 | **protruding** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6616 | **crimson** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6617 | **pilgrimage** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6618 | **incarnate** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6619 | **gyurme** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6620 | **thekchok** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6621 | **trime** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6622 | **golok** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6623 | **so-and-so** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6624 | **confe** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6625 | **enthroned** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6626 | **life-energy** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6627 | **pluck** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6628 | **auditory** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6629 | **blur** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6630 | **salivate** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6631 | **extremity** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6632 | **energies-the** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6633 | **life-supporting** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6634 | **life-channel** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6635 | **sigh** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6636 | **whiteness** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6637 | **cloudless** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6638 | **redness** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6639 | **lustful** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6640 | **blackness** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6641 | **swoon** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6642 | **vajra-posture** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6643 | **purpos** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6644 | **rattle** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6645 | **tent** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6646 | **axi** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6647 | **mind-con** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6648 | **visarga** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6649 | **flut** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6650 | **tering** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6651 | **three-layered** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6652 | **embodying** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6653 | **clad** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6654 | **attire** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6655 | **nirmat** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6656 | **ursina** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6657 | **bead** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6658 | **skyward** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6659 | **akanistha** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6660 | **repre** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6661 | **sentation** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6662 | **palate** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6663 | **grass-stalk** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6664 | **nyi** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6665 | **iyana** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6666 | **palyul** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6667 | **vajrapdt** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6668 | **one-pointed** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6669 | **beseech** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6670 | **gochen** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6671 | **contriving** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6672 | **amitayus** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6673 | **amarani** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6674 | **jivantiye** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6675 | **svaha** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6676 | **and-through** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6677 | **inter** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6678 | **dependence-dispel** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6679 | **ach** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6680 | **serum** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6681 | **dew** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6682 | **stalk** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6683 | **assiduously** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6684 | **shortcut** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6685 | **mutter** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6686 | **incoherently** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6687 | **interminable** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6688 | **goad** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6689 | **mination** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6690 | **meditation-all** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6691 | **creativity** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6692 | **aesthetic** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6693 | **literary** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6694 | **banish** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6695 | **fabricate** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6696 | **watershed** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6697 | **evil-even** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6698 | **indissolubly** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6699 | **clude** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6700 | **adulteration** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6701 | **well-cooked** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6702 | **fancy** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6703 | **seasoned** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6704 | **savoury** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6705 | **cooking-juice** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6706 | **ploughshare** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6707 | **unearthing** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6708 | **nanny** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6709 | **uprooting** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6710 | **elegance** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6711 | **poetry** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6712 | **copious** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6713 | **cramped** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6714 | **discours** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6715 | **philosophical** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6716 | **soak** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6717 | **gloom** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6718 | **imperturbable** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6719 | **instructor** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6720 | **impart** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6721 | **savant** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6722 | **verbose** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6723 | **discourse** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6724 | **confection** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6725 | **cleverly** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6726 | **fanciful** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6727 | **superficially** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6728 | **vajra-brother** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6729 | **compile** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6730 | **nourished** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6731 | **captivate** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6732 | **intoxicating** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6733 | **seclusion** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6734 | **dronma** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6735 | **tsering** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6736 | **kunzangthekchok** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6737 | **tulku** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6738 | **peated** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6739 | **times-even** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6740 | **kushab** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6741 | **shenpen** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6742 | **thaye** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6743 | **ozer** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6744 | **dharma-sovereign** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6745 | **tradition-in** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6746 | **changchub** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6747 | **cbokyi** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6748 | **embellishment** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6749 | **rough-mannered** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6750 | **rudam** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6751 | **samten** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6752 | **choling** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6753 | **palace-a** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6754 | **foliage** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6755 | **undergrowth** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6756 | **filtering** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6757 | **swasti** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6758 | **siddham** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6759 | **unfolded** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6760 | **renowned** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6761 | **gyalwai** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6762 | **nyugu** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6763 | **chokyi** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6764 | **lekdrup** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6765 | **temporally** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - |
| 6766 | **reduced** | 2 | 166.13 | 4.793221 | 🔵 low — common in general English | - |
| 6767 | **balance** | 2 | 161.72 | 4.665882 | 🔵 low — common in general English | - |
| 6768 | **own** | 2 | 160.97 | 4.644375 | 🔵 low — common in general English | - |
| 6769 | **decision** | 2 | 160.97 | 4.644375 | 🔵 low — common in general English | - |
| 6770 | **contradict** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - |
| 6771 | **lured** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - |
| 6772 | **snapped** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - |
| 6773 | **numerical** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - |
| 6774 | **orientation** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - |
| 6775 | **deprive** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - |
| 6776 | **reasoned** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - |
| 6777 | **disappearance** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - |
| 6778 | **inundated** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - |
| 6779 | **incompatible** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - |
| 6780 | **baring** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - |
| 6781 | **highway** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - |
| 6782 | **transformation** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - |
| 6783 | **pinnacle** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - |
| 6784 | **tri** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - |
| 6785 | **dependable** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - |
| 6786 | **escaped** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - |
| 6787 | **slab** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - |
| 6788 | **dearly** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - |
| 6789 | **transitory** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - |
| 6790 | **rigorous** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - |
| 6791 | **prolong** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - |
| 6792 | **toxic** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - |
| 6793 | **crawl** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - |
| 6794 | **formidable** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - |
| 6795 | **dangerously** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - |
| 6796 | **bribe** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - |
| 6797 | **immune** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - |
| 6798 | **amidst** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - |
| 6799 | **guideline** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - |
| 6800 | **marsh** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - |
| 6801 | **raven** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - |
| 6802 | **purse** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - |
| 6803 | **plying** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - |
| 6804 | **icy** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - |
| 6805 | **evaporated** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - |
| 6806 | **eyed** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - |
| 6807 | **castrated** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - |
| 6808 | **ridden** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - |
| 6809 | **entail** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - |
| 6810 | **bartering** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - |
| 6811 | **crow** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - |
| 6812 | **infant** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - |
| 6813 | **unnoticed** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - |
| 6814 | **integrity** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - |
| 6815 | **occupying** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - |
| 6816 | **charming** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - |
| 6817 | **strife** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - |
| 6818 | **haul** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - |
| 6819 | **outdoor** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - |
| 6820 | **guilty** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - |
| 6821 | **sharpest** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - |
| 6822 | **circulate** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - |
| 6823 | **transferring** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - |
| 6824 | **residue** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - |
| 6825 | **poorer** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - |
| 6826 | **unattractive** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - |
| 6827 | **unjust** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - |
| 6828 | **self-confidence** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - |
| 6829 | **fulfilment** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - |
| 6830 | **propel** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - |
| 6831 | **jam** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - |
| 6832 | **infuse** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - |
| 6833 | **absurd** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - |
| 6834 | **mindful** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - |
| 6835 | **vigilant** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - |
| 6836 | **incumbent** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - |
| 6837 | **decay** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - |
| 6838 | **immensely** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - |
| 6839 | **violently** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - |
| 6840 | **saint** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - |
| 6841 | **honoured** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - |
| 6842 | **piercing** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - |
| 6843 | **forbid** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - |
| 6844 | **wondering** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - |
| 6845 | **tending** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - |
| 6846 | **summoned** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - |
| 6847 | **compelling** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - |
| 6848 | **rosy** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - |
| 6849 | **one-sided** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - |
| 6850 | **sel** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - |
| 6851 | **opponent** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - |
| 6852 | **cheated** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - |
| 6853 | **banquet** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - |
| 6854 | **author** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - |
| 6855 | **stubborn** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - |
| 6856 | **sheltered** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - |
| 6857 | **void** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - |
| 6858 | **viewing** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - |
| 6859 | **slaughtering** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - |
| 6860 | **boarded** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - |
| 6861 | **ludicrous** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - |
| 6862 | **shade** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - |
| 6863 | **grinding** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - |
| 6864 | **invariably** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - |
| 6865 | **detrimental** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - |
| 6866 | **kicking** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - |
| 6867 | **welt** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - |
| 6868 | **charitable** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - |
| 6869 | **mediocre** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - |
| 6870 | **guarding** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - |
| 6871 | **tran** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - |
| 6872 | **counteract** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - |
| 6873 | **bounce** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - |
| 6874 | **print** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - |
| 6875 | **maya** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - |
| 6876 | **stan** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - |
| 6877 | **soaking** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - |
| 6878 | **thickness** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - |
| 6879 | **tumbling** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - |
| 6880 | **finest** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - |
| 6881 | **gratified** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - |
| 6882 | **expose** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - |
| 6883 | **fence** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - |
| 6884 | **straw** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - |
| 6885 | **deplete** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - |
| 6886 | **rushing** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - |
| 6887 | **confront** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - |
| 6888 | **vertical** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - |
| 6889 | **fifteen** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - |
| 6890 | **chopping** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - |
| 6891 | **deepen** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - |
| 6892 | **surrender** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - |
| 6893 | **south-west** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - |
| 6894 | **layer** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - |
| 6895 | **confidently** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - |
| 6896 | **respected** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - |
| 6897 | **midst** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - |
| 6898 | **concluding** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - |
| 6899 | **ame** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - |
| 6900 | **displayed** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - |
| 6901 | **hut** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - |
| 6902 | **berry** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - |
| 6903 | **opportune** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - |
| 6904 | **obscuring** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - |
| 6905 | **contradictory** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - |
| 6906 | **evacuation** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - |
| 6907 | **erect** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - |
| 6908 | **leaning** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - |
| 6909 | **regent** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - |
| 6910 | **henceforth** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - |
| 6911 | **market** | 3 | 156.83 | 3.016666 | 🔵 low — common in general English | - |
| 6912 | **wheat** | 2 | 155.84 | 4.496322 | 🔵 low — common in general English | - |
| 6913 | **owned** | 2 | 154.29 | 4.451472 | 🔵 low — common in general English | - |
| 6914 | **seize** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English | - |
| 6915 | **aged** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English | - |
| 6916 | **undue** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English | - |
| 6917 | **extracted** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English | - |
| 6918 | **thorough** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English | - |
| 6919 | **translation** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English | - |
| 6920 | **eastward** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English | - |
| 6921 | **erected** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English | - |
| 6922 | **wilderness** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English | - |
| 6923 | **contentious** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English | - |
| 6924 | **student** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English | - |
| 6925 | **wax** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English | - |
| 6926 | **diet** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English | - |
| 6927 | **als** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English | - |
| 6928 | **pause** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English | - |
| 6929 | **judging** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English | - |
| 6930 | **prelude** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English | - |
| 6931 | **ham** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English | - |
| 6932 | **exit** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English | - |
| 6933 | **ditch** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English | - |
| 6934 | **erupt** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English | - |
| 6935 | **fashion** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English | - |
| 6936 | **alike** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English | - |
| 6937 | **porter** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English | - |
| 6938 | **stall** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English | - |
| 6939 | **demonstrating** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English | - |
| 6940 | **neighbour** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English | - |
| 6941 | **tumble** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English | - |
| 6942 | **wolf** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English | - |
| 6943 | **overtly** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English | - |
| 6944 | **untrue** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English | - |
| 6945 | **diverse** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English | - |
| 6946 | **emotional** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English | - |
| 6947 | **choosing** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English | - |
| 6948 | **contravened** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English | - |
| 6949 | **disturbing** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English | - |
| 6950 | **mas** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English | - |
| 6951 | **fasting** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English | - |
| 6952 | **wondered** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English | - |
| 6953 | **crashed** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English | - |
| 6954 | **undergone** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English | - |
| 6955 | **suicide** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English | - |
| 6956 | **hardest** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English | - |
| 6957 | **desperately** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English | - |
| 6958 | **precipitous** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English | - |
| 6959 | **whereby** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English | - |
| 6960 | **progressed** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English | - |
| 6961 | **catching** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English | - |
| 6962 | **chronic** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English | - |
| 6963 | **bare** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English | - |
| 6964 | **hanging** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English | - |
| 6965 | **trailing** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English | - |
| 6966 | **materialize** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English | - |
| 6967 | **crossing** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English | - |
| 6968 | **dressing** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English | - |
| 6969 | **luck** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English | - |
| 6970 | **dashed** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English | - |
| 6971 | **fled** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English | - |
| 6972 | **analyzing** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English | - |
| 6973 | **dimmed** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English | - |
| 6974 | **favouring** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English | - |
| 6975 | **naive** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English | - |
| 6976 | **climbing** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English | - |
| 6977 | **affirmed** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English | - |
| 6978 | **pel** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English | - |
| 6979 | **frightening** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English | - |
| 6980 | **wipe** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English | - |
| 6981 | **cleaned** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English | - |
| 6982 | **thirdly** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English | - |
| 6983 | **extracting** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English | - |
| 6984 | **deadly** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English | - |
| 6985 | **violence** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English | - |
| 6986 | **cape** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English | - |
| 6987 | **chas** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English | - |
| 6988 | **discouraging** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English | - |
| 6989 | **realizing** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English | - |
| 6990 | **symbolic** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English | - |
| 6991 | **distilled** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English | - |
| 6992 | **misunderstanding** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English | - |
| 6993 | **ripe** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English | - |
| 6994 | **predominantly** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English | - |
| 6995 | **swelling** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English | - |
| 6996 | **intermediary** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English | - |
| 6997 | **evolution** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English | - |
| 6998 | **convey** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English | - |
| 6999 | **accrue** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English | - |
| 7000 | **new** | 3 | 151.18 | 2.907899 | 🔵 low — common in general English | - |
| 7001 | **focussing** | 1 | 150.37 | 8.676844 | 🔵 low — common in general English | - |
| 7002 | **impeded** | 1 | 150.37 | 8.676844 | 🔵 low — common in general English | - |
| 7003 | **silent** | 1 | 150.37 | 8.676844 | 🔵 low — common in general English | - |
| 7004 | **sheer** | 1 | 150.37 | 8.676844 | 🔵 low — common in general English | - |
| 7005 | **recede** | 1 | 150.37 | 8.676844 | 🔵 low — common in general English | - |
| 7006 | **blown** | 1 | 150.37 | 8.676844 | 🔵 low — common in general English | - |
| 7007 | **bubble** | 1 | 150.37 | 8.676844 | 🔵 low — common in general English | - |
| 7008 | **recourse** | 1 | 150.37 | 8.676844 | 🔵 low — common in general English | - |
| 7009 | **marking** | 1 | 150.37 | 8.676844 | 🔵 low — common in general English | - |
| 7010 | **cooler** | 1 | 150.37 | 8.676844 | 🔵 low — common in general English | - |
| 7011 | **constructed** | 1 | 150.37 | 8.676844 | 🔵 low — common in general English | - |
| 7012 | **wane** | 1 | 150.37 | 8.676844 | 🔵 low — common in general English | - |
| 7013 | **malt** | 1 | 150.37 | 8.676844 | 🔵 low — common in general English | - |
| 7014 | **freezing** | 1 | 150.37 | 8.676844 | 🔵 low — common in general English | - |
| 7015 | **mattress** | 1 | 150.37 | 8.676844 | 🔵 low — common in general English | - |
| 7016 | **await** | 1 | 150.37 | 8.676844 | 🔵 low — common in general English | - |
| 7017 | **rebel** | 1 | 150.37 | 8.676844 | 🔵 low — common in general English | - |
| 7018 | **hospitality** | 1 | 150.37 | 8.676844 | 🔵 low — common in general English | - |
| 7019 | **foreshadow** | 1 | 150.37 | 8.676844 | 🔵 low — common in general English | - |
| 7020 | **persuaded** | 1 | 150.37 | 8.676844 | 🔵 low — common in general English | - |
| 7021 | **yard** | 1 | 150.37 | 8.676844 | 🔵 low — common in general English | - |
| 7022 | **intermittent** | 1 | 150.37 | 8.676844 | 🔵 low — common in general English | - |
| 7023 | **emp** | 1 | 150.37 | 8.676844 | 🔵 low — common in general English | - |
| 7024 | **drifting** | 1 | 150.37 | 8.676844 | 🔵 low — common in general English | - |
| 7025 | **fragrance** | 1 | 150.37 | 8.676844 | 🔵 low — common in general English | - |
| 7026 | **ink** | 1 | 150.37 | 8.676844 | 🔵 low — common in general English | - |
| 7027 | **walked** | 1 | 150.37 | 8.676844 | 🔵 low — common in general English | - |
| 7028 | **pre** | 1 | 150.37 | 8.676844 | 🔵 low — common in general English | - |
| 7029 | **dole** | 1 | 150.37 | 8.676844 | 🔵 low — common in general English | - |
| 7030 | **hung** | 1 | 150.37 | 8.676844 | 🔵 low — common in general English | - |
| 7031 | **inviting** | 1 | 150.37 | 8.676844 | 🔵 low — common in general English | - |
| 7032 | **dragging** | 1 | 150.37 | 8.676844 | 🔵 low — common in general English | - |
| 7033 | **theme** | 1 | 150.37 | 8.676844 | 🔵 low — common in general English | - |
| 7034 | **reciprocal** | 1 | 150.37 | 8.676844 | 🔵 low — common in general English | - |
| 7035 | **individually** | 1 | 150.37 | 8.676844 | 🔵 low — common in general English | - |
| 7036 | **flank** | 1 | 150.37 | 8.676844 | 🔵 low — common in general English | - |
| 7037 | **fatty** | 1 | 150.37 | 8.676844 | 🔵 low — common in general English | - |
| 7038 | **ablaze** | 1 | 150.37 | 8.676844 | 🔵 low — common in general English | - |
| 7039 | **catapulted** | 1 | 150.37 | 8.676844 | 🔵 low — common in general English | - |
| 7040 | **dom** | 1 | 150.37 | 8.676844 | 🔵 low — common in general English | - |
| 7041 | **waited** | 1 | 150.37 | 8.676844 | 🔵 low — common in general English | - |
| 7042 | **prejudice** | 1 | 150.37 | 8.676844 | 🔵 low — common in general English | - |
| 7043 | **relaxing** | 1 | 150.37 | 8.676844 | 🔵 low — common in general English | - |
| 7044 | **annoyed** | 1 | 150.37 | 8.676844 | 🔵 low — common in general English | - |
| 7045 | **grazing** | 1 | 150.37 | 8.676844 | 🔵 low — common in general English | - |
| 7046 | **honesty** | 1 | 150.37 | 8.676844 | 🔵 low — common in general English | - |
| 7047 | **prudence** | 1 | 150.37 | 8.676844 | 🔵 low — common in general English | - |
| 7048 | **ted** | 1 | 150.37 | 8.676844 | 🔵 low — common in general English | - |
| 7049 | **sponsor** | 1 | 150.37 | 8.676844 | 🔵 low — common in general English | - |
| 7050 | **ideally** | 1 | 150.37 | 8.676844 | 🔵 low — common in general English | - |
| 7051 | **gravel** | 1 | 150.37 | 8.676844 | 🔵 low — common in general English | - |
| 7052 | **feasible** | 1 | 150.37 | 8.676844 | 🔵 low — common in general English | - |
| 7053 | **noticeable** | 1 | 150.37 | 8.676844 | 🔵 low — common in general English | - |
| 7054 | **tenth** | 1 | 150.37 | 8.676844 | 🔵 low — common in general English | - |
| 7055 | **sara** | 1 | 150.37 | 8.676844 | 🔵 low — common in general English | - |
| 7056 | **surpassing** | 1 | 150.37 | 8.676844 | 🔵 low — common in general English | - |
| 7057 | **unrealized** | 1 | 150.37 | 8.676844 | 🔵 low — common in general English | - |
| 7058 | **omitted** | 1 | 150.37 | 8.676844 | 🔵 low — common in general English | - |
| 7059 | **collected** | 1 | 150.37 | 8.676844 | 🔵 low — common in general English | - |
| 7060 | **demand** | 2 | 147.75 | 4.262835 | 🔵 low — common in general English | - |
| 7061 | **encountered** | 1 | 147.21 | 8.494523 | 🔵 low — common in general English | - |
| 7062 | **entrance** | 1 | 147.21 | 8.494523 | 🔵 low — common in general English | - |
| 7063 | **analyze** | 1 | 147.21 | 8.494523 | 🔵 low — common in general English | - |
| 7064 | **span** | 1 | 147.21 | 8.494523 | 🔵 low — common in general English | - |
| 7065 | **reassure** | 1 | 147.21 | 8.494523 | 🔵 low — common in general English | - |
| 7066 | **suspected** | 1 | 147.21 | 8.494523 | 🔵 low — common in general English | - |
| 7067 | **flurry** | 1 | 147.21 | 8.494523 | 🔵 low — common in general English | - |
| 7068 | **hal** | 1 | 147.21 | 8.494523 | 🔵 low — common in general English | - |
| 7069 | **herd** | 1 | 147.21 | 8.494523 | 🔵 low — common in general English | - |
| 7070 | **rescued** | 1 | 147.21 | 8.494523 | 🔵 low — common in general English | - |
| 7071 | **employing** | 1 | 147.21 | 8.494523 | 🔵 low — common in general English | - |
| 7072 | **intensity** | 1 | 147.21 | 8.494523 | 🔵 low — common in general English | - |
| 7073 | **fox** | 1 | 147.21 | 8.494523 | 🔵 low — common in general English | - |
| 7074 | **lapse** | 1 | 147.21 | 8.494523 | 🔵 low — common in general English | - |
| 7075 | **reception** | 1 | 147.21 | 8.494523 | 🔵 low — common in general English | - |
| 7076 | **practically** | 1 | 147.21 | 8.494523 | 🔵 low — common in general English | - |
| 7077 | **thoroughly** | 1 | 147.21 | 8.494523 | 🔵 low — common in general English | - |
| 7078 | **improper** | 1 | 147.21 | 8.494523 | 🔵 low — common in general English | - |
| 7079 | **landed** | 1 | 147.21 | 8.494523 | 🔵 low — common in general English | - |
| 7080 | **dormant** | 1 | 147.21 | 8.494523 | 🔵 low — common in general English | - |
| 7081 | **cooling** | 1 | 147.21 | 8.494523 | 🔵 low — common in general English | - |
| 7082 | **conform** | 1 | 147.21 | 8.494523 | 🔵 low — common in general English | - |
| 7083 | **complaining** | 1 | 147.21 | 8.494523 | 🔵 low — common in general English | - |
| 7084 | **enquiry** | 1 | 147.21 | 8.494523 | 🔵 low — common in general English | - |
| 7085 | **fetch** | 1 | 147.21 | 8.494523 | 🔵 low — common in general English | - |
| 7086 | **sail** | 1 | 147.21 | 8.494523 | 🔵 low — common in general English | - |
| 7087 | **caterpillar** | 1 | 147.21 | 8.494523 | 🔵 low — common in general English | - |
| 7088 | **occurrence** | 1 | 147.21 | 8.494523 | 🔵 low — common in general English | - |
| 7089 | **urgently** | 1 | 147.21 | 8.494523 | 🔵 low — common in general English | - |
| 7090 | **lean** | 1 | 147.21 | 8.494523 | 🔵 low — common in general English | - |
| 7091 | **brass** | 1 | 147.21 | 8.494523 | 🔵 low — common in general English | - |
| 7092 | **alternatively** | 1 | 147.21 | 8.494523 | 🔵 low — common in general English | - |
| 7093 | **absorbing** | 1 | 147.21 | 8.494523 | 🔵 low — common in general English | - |
| 7094 | **conversation** | 1 | 147.21 | 8.494523 | 🔵 low — common in general English | - |
| 7095 | **debated** | 1 | 147.21 | 8.494523 | 🔵 low — common in general English | - |
| 7096 | **vague** | 1 | 144.54 | 8.340372 | 🔵 low — common in general English | - |
| 7097 | **slipping** | 1 | 144.54 | 8.340372 | 🔵 low — common in general English | - |
| 7098 | **collectively** | 1 | 144.54 | 8.340372 | 🔵 low — common in general English | - |
| 7099 | **unwelcome** | 1 | 144.54 | 8.340372 | 🔵 low — common in general English | - |
| 7100 | **depression** | 1 | 144.54 | 8.340372 | 🔵 low — common in general English | - |
| 7101 | **liquor** | 1 | 144.54 | 8.340372 | 🔵 low — common in general English | - |
| 7102 | **counterpart** | 1 | 144.54 | 8.340372 | 🔵 low — common in general English | - |
| 7103 | **restriction** | 1 | 144.54 | 8.340372 | 🔵 low — common in general English | - |
| 7104 | **gravity** | 1 | 144.54 | 8.340372 | 🔵 low — common in general English | - |
| 7105 | **heaviest** | 1 | 144.54 | 8.340372 | 🔵 low — common in general English | - |
| 7106 | **outweighed** | 1 | 144.54 | 8.340372 | 🔵 low — common in general English | - |
| 7107 | **bleak** | 1 | 144.54 | 8.340372 | 🔵 low — common in general English | - |
| 7108 | **invisible** | 1 | 144.54 | 8.340372 | 🔵 low — common in general English | - |
| 7109 | **adopting** | 1 | 144.54 | 8.340372 | 🔵 low — common in general English | - |
| 7110 | **draining** | 1 | 144.54 | 8.340372 | 🔵 low — common in general English | - |
| 7111 | **negatively** | 1 | 144.54 | 8.340372 | 🔵 low — common in general English | - |
| 7112 | **upheld** | 1 | 144.54 | 8.340372 | 🔵 low — common in general English | - |
| 7113 | **lightning** | 1 | 144.54 | 8.340372 | 🔵 low — common in general English | - |
| 7114 | **penalty** | 1 | 144.54 | 8.340372 | 🔵 low — common in general English | - |
| 7115 | **wing** | 1 | 144.54 | 8.340372 | 🔵 low — common in general English | - |
| 7116 | **mixture** | 1 | 144.54 | 8.340372 | 🔵 low — common in general English | - |
| 7117 | **diminished** | 1 | 144.54 | 8.340372 | 🔵 low — common in general English | - |
| 7118 | **lent** | 1 | 144.54 | 8.340372 | 🔵 low — common in general English | - |
| 7119 | **spinning** | 1 | 144.54 | 8.340372 | 🔵 low — common in general English | - |
| 7120 | **transporting** | 1 | 144.54 | 8.340372 | 🔵 low — common in general English | - |
| 7121 | **rot** | 1 | 144.54 | 8.340372 | 🔵 low — common in general English | - |
| 7122 | **dram** | 1 | 144.54 | 8.340372 | 🔵 low — common in general English | - |
| 7123 | **occupied** | 1 | 144.54 | 8.340372 | 🔵 low — common in general English | - |
| 7124 | **admit** | 1 | 144.54 | 8.340372 | 🔵 low — common in general English | - |
| 7125 | **goldsmith** | 1 | 144.54 | 8.340372 | 🔵 low — common in general English | - |
| 7126 | **umbrella** | 1 | 144.54 | 8.340372 | 🔵 low — common in general English | - |
| 7127 | **tube** | 1 | 144.54 | 8.340372 | 🔵 low — common in general English | - |
| 7128 | **intangible** | 1 | 144.54 | 8.340372 | 🔵 low — common in general English | - |
| 7129 | **sunshine** | 1 | 144.54 | 8.340372 | 🔵 low — common in general English | - |
| 7130 | **north-west** | 1 | 144.54 | 8.340372 | 🔵 low — common in general English | - |
| 7131 | **ensuring** | 1 | 144.54 | 8.340372 | 🔵 low — common in general English | - |
| 7132 | **rod** | 1 | 144.54 | 8.340372 | 🔵 low — common in general English | - |
| 7133 | **chicken** | 1 | 144.54 | 8.340372 | 🔵 low — common in general English | - |
| 7134 | **unaffected** | 1 | 144.54 | 8.340372 | 🔵 low — common in general English | - |
| 7135 | **differ** | 1 | 144.54 | 8.340372 | 🔵 low — common in general English | - |
| 7136 | **duration** | 1 | 144.54 | 8.340372 | 🔵 low — common in general English | - |
| 7137 | **abu** | 1 | 144.54 | 8.340372 | 🔵 low — common in general English | - |
| 7138 | **increased** | 2 | 143.79 | 4.148555 | 🔵 low — common in general English | - |
| 7139 | **domestic** | 2 | 143.42 | 4.137814 | 🔵 low — common in general English | - |
| 7140 | **sounded** | 1 | 142.22 | 8.206841 | 🔵 low — common in general English | - |
| 7141 | **enthusiasm** | 1 | 142.22 | 8.206841 | 🔵 low — common in general English | - |
| 7142 | **reputation** | 1 | 142.22 | 8.206841 | 🔵 low — common in general English | - |
| 7143 | **demonstrate** | 1 | 142.22 | 8.206841 | 🔵 low — common in general English | - |
| 7144 | **reliable** | 1 | 142.22 | 8.206841 | 🔵 low — common in general English | - |
| 7145 | **pack** | 1 | 142.22 | 8.206841 | 🔵 low — common in general English | - |
| 7146 | **stuck** | 1 | 142.22 | 8.206841 | 🔵 low — common in general English | - |
| 7147 | **fate** | 1 | 142.22 | 8.206841 | 🔵 low — common in general English | - |
| 7148 | **endanger** | 1 | 142.22 | 8.206841 | 🔵 low — common in general English | - |
| 7149 | **diversion** | 1 | 142.22 | 8.206841 | 🔵 low — common in general English | - |
| 7150 | **pleas** | 1 | 142.22 | 8.206841 | 🔵 low — common in general English | - |
| 7151 | **softer** | 1 | 142.22 | 8.206841 | 🔵 low — common in general English | - |
| 7152 | **concentrating** | 1 | 142.22 | 8.206841 | 🔵 low — common in general English | - |
| 7153 | **shifted** | 1 | 142.22 | 8.206841 | 🔵 low — common in general English | - |
| 7154 | **hazardous** | 1 | 142.22 | 8.206841 | 🔵 low — common in general English | - |
| 7155 | **label** | 1 | 142.22 | 8.206841 | 🔵 low — common in general English | - |
| 7156 | **interference** | 1 | 142.22 | 8.206841 | 🔵 low — common in general English | - |
| 7157 | **directive** | 1 | 142.22 | 8.206841 | 🔵 low — common in general English | - |
| 7158 | **distributing** | 1 | 142.22 | 8.206841 | 🔵 low — common in general English | - |
| 7159 | **grip** | 1 | 142.22 | 8.206841 | 🔵 low — common in general English | - |
| 7160 | **mercury** | 1 | 142.22 | 8.206841 | 🔵 low — common in general English | - |
| 7161 | **finish** | 1 | 142.22 | 8.206841 | 🔵 low — common in general English | - |
| 7162 | **readily** | 1 | 142.22 | 8.206841 | 🔵 low — common in general English | - |
| 7163 | **lessening** | 1 | 142.22 | 8.206841 | 🔵 low — common in general English | - |
| 7164 | **desired** | 1 | 142.22 | 8.206841 | 🔵 low — common in general English | - |
| 7165 | **necessity** | 1 | 142.22 | 8.206841 | 🔵 low — common in general English | - |
| 7166 | **impatience** | 1 | 142.22 | 8.206841 | 🔵 low — common in general English | - |
| 7167 | **intelligent** | 1 | 142.22 | 8.206841 | 🔵 low — common in general English | - |
| 7168 | **pronounced** | 1 | 142.22 | 8.206841 | 🔵 low — common in general English | - |
| 7169 | **deter** | 1 | 142.22 | 8.206841 | 🔵 low — common in general English | - |
| 7170 | **agriculture** | 2 | 141.61 | 4.085773 | 🔵 low — common in general English | - |
| 7171 | **player** | 1 | 140.18 | 8.089058 | 🔵 low — common in general English | - |
| 7172 | **relaxation** | 1 | 140.18 | 8.089058 | 🔵 low — common in general English | - |
| 7173 | **dominate** | 1 | 140.18 | 8.089058 | 🔵 low — common in general English | - |
| 7174 | **proof** | 1 | 140.18 | 8.089058 | 🔵 low — common in general English | - |
| 7175 | **matching** | 1 | 140.18 | 8.089058 | 🔵 low — common in general English | - |
| 7176 | **unexpectedly** | 1 | 140.18 | 8.089058 | 🔵 low — common in general English | - |
| 7177 | **revived** | 1 | 140.18 | 8.089058 | 🔵 low — common in general English | - |
| 7178 | **supplementary** | 1 | 140.18 | 8.089058 | 🔵 low — common in general English | - |
| 7179 | **ridiculous** | 1 | 140.18 | 8.089058 | 🔵 low — common in general English | - |
| 7180 | **steer** | 1 | 140.18 | 8.089058 | 🔵 low — common in general English | - |
| 7181 | **chart** | 1 | 140.18 | 8.089058 | 🔵 low — common in general English | - |
| 7182 | **familiar** | 1 | 140.18 | 8.089058 | 🔵 low — common in general English | - |
| 7183 | **rigid** | 1 | 140.18 | 8.089058 | 🔵 low — common in general English | - |
| 7184 | **desperate** | 1 | 140.18 | 8.089058 | 🔵 low — common in general English | - |
| 7185 | **page** | 1 | 140.18 | 8.089058 | 🔵 low — common in general English | - |
| 7186 | **dealt** | 1 | 140.18 | 8.089058 | 🔵 low — common in general English | - |
| 7187 | **attacking** | 1 | 140.18 | 8.089058 | 🔵 low — common in general English | - |
| 7188 | **clouded** | 1 | 140.18 | 8.089058 | 🔵 low — common in general English | - |
| 7189 | **hitting** | 1 | 140.18 | 8.089058 | 🔵 low — common in general English | - |
| 7190 | **wiped** | 1 | 140.18 | 8.089058 | 🔵 low — common in general English | - |
| 7191 | **inclined** | 1 | 140.18 | 8.089058 | 🔵 low — common in general English | - |
| 7192 | **leaf** | 1 | 140.18 | 8.089058 | 🔵 low — common in general English | - |
| 7193 | **insist** | 1 | 140.18 | 8.089058 | 🔵 low — common in general English | - |
| 7194 | **grossly** | 1 | 140.18 | 8.089058 | 🔵 low — common in general English | - |
| 7195 | **spurred** | 1 | 140.18 | 8.089058 | 🔵 low — common in general English | - |
| 7196 | **clarify** | 1 | 140.18 | 8.089058 | 🔵 low — common in general English | - |
| 7197 | **intellectual** | 1 | 140.18 | 8.089058 | 🔵 low — common in general English | - |
| 7198 | **indebted** | 1 | 140.18 | 8.089058 | 🔵 low — common in general English | - |
| 7199 | **borrowed** | 1 | 140.18 | 8.089058 | 🔵 low — common in general English | - |
| 7200 | **lacked** | 1 | 140.18 | 8.089058 | 🔵 low — common in general English | - |
| 7201 | **stretching** | 1 | 140.18 | 8.089058 | 🔵 low — common in general English | - |
| 7202 | **funeral** | 1 | 140.18 | 8.089058 | 🔵 low — common in general English | - |
| 7203 | **solved** | 1 | 140.18 | 8.089058 | 🔵 low — common in general English | - |
| 7204 | **mutually** | 1 | 138.36 | 7.983697 | 🔵 low — common in general English | - |
| 7205 | **anchor** | 1 | 138.36 | 7.983697 | 🔵 low — common in general English | - |
| 7206 | **collective** | 1 | 138.36 | 7.983697 | 🔵 low — common in general English | - |
| 7207 | **shed** | 1 | 138.36 | 7.983697 | 🔵 low — common in general English | - |
| 7208 | **withdrawing** | 1 | 138.36 | 7.983697 | 🔵 low — common in general English | - |
| 7209 | **multiple** | 1 | 138.36 | 7.983697 | 🔵 low — common in general English | - |
| 7210 | **pan** | 1 | 138.36 | 7.983697 | 🔵 low — common in general English | - |
| 7211 | **varying** | 1 | 138.36 | 7.983697 | 🔵 low — common in general English | - |
| 7212 | **prominent** | 1 | 138.36 | 7.983697 | 🔵 low — common in general English | - |
| 7213 | **prop** | 1 | 138.36 | 7.983697 | 🔵 low — common in general English | - |
| 7214 | **pointing** | 1 | 138.36 | 7.983697 | 🔵 low — common in general English | - |
| 7215 | **thwart** | 1 | 138.36 | 7.983697 | 🔵 low — common in general English | - |
| 7216 | **evident** | 1 | 138.36 | 7.983697 | 🔵 low — common in general English | - |
| 7217 | **examined** | 1 | 138.36 | 7.983697 | 🔵 low — common in general English | - |
| 7218 | **nearing** | 1 | 138.36 | 7.983697 | 🔵 low — common in general English | - |
| 7219 | **obliged** | 1 | 138.36 | 7.983697 | 🔵 low — common in general English | - |
| 7220 | **extract** | 1 | 138.36 | 7.983697 | 🔵 low — common in general English | - |
| 7221 | **plate** | 1 | 138.36 | 7.983697 | 🔵 low — common in general English | - |
| 7222 | **persist** | 1 | 138.36 | 7.983697 | 🔵 low — common in general English | - |
| 7223 | **subscribe** | 1 | 138.36 | 7.983697 | 🔵 low — common in general English | - |
| 7224 | **unwanted** | 1 | 138.36 | 7.983697 | 🔵 low — common in general English | - |
| 7225 | **incorrect** | 1 | 138.36 | 7.983697 | 🔵 low — common in general English | - |
| 7226 | **turmoil** | 1 | 136.70 | 7.888387 | 🔵 low — common in general English | - |
| 7227 | **dominated** | 1 | 136.70 | 7.888387 | 🔵 low — common in general English | - |
| 7228 | **creek** | 1 | 136.70 | 7.888387 | 🔵 low — common in general English | - |
| 7229 | **fought** | 1 | 136.70 | 7.888387 | 🔵 low — common in general English | - |
| 7230 | **removing** | 1 | 136.70 | 7.888387 | 🔵 low — common in general English | - |
| 7231 | **preceding** | 1 | 136.70 | 7.888387 | 🔵 low — common in general English | - |
| 7232 | **calculation** | 1 | 136.70 | 7.888387 | 🔵 low — common in general English | - |
| 7233 | **disastrous** | 1 | 136.70 | 7.888387 | 🔵 low — common in general English | - |
| 7234 | **warranted** | 1 | 136.70 | 7.888387 | 🔵 low — common in general English | - |
| 7235 | **warn** | 1 | 136.70 | 7.888387 | 🔵 low — common in general English | - |
| 7236 | **austerity** | 1 | 136.70 | 7.888387 | 🔵 low — common in general English | - |
| 7237 | **modestly** | 1 | 136.70 | 7.888387 | 🔵 low — common in general English | - |
| 7238 | **limitation** | 1 | 136.70 | 7.888387 | 🔵 low — common in general English | - |
| 7239 | **worthwhile** | 1 | 136.70 | 7.888387 | 🔵 low — common in general English | - |
| 7240 | **halting** | 1 | 136.70 | 7.888387 | 🔵 low — common in general English | - |
| 7241 | **departure** | 1 | 136.70 | 7.888387 | 🔵 low — common in general English | - |
| 7242 | **persistent** | 1 | 136.70 | 7.888387 | 🔵 low — common in general English | - |
| 7243 | **revealed** | 1 | 135.20 | 7.801376 | 🔵 low — common in general English | - |
| 7244 | **topic** | 1 | 135.20 | 7.801376 | 🔵 low — common in general English | - |
| 7245 | **miss** | 1 | 135.20 | 7.801376 | 🔵 low — common in general English | - |
| 7246 | **dictate** | 1 | 135.20 | 7.801376 | 🔵 low — common in general English | - |
| 7247 | **prohibited** | 1 | 135.20 | 7.801376 | 🔵 low — common in general English | - |
| 7248 | **misleading** | 1 | 135.20 | 7.801376 | 🔵 low — common in general English | - |
| 7249 | **mood** | 1 | 135.20 | 7.801376 | 🔵 low — common in general English | - |
| 7250 | **purely** | 1 | 135.20 | 7.801376 | 🔵 low — common in general English | - |
| 7251 | **essentially** | 1 | 135.20 | 7.801376 | 🔵 low — common in general English | - |
| 7252 | **restrain** | 1 | 135.20 | 7.801376 | 🔵 low — common in general English | - |
| 7253 | **stemming** | 1 | 135.20 | 7.801376 | 🔵 low — common in general English | - |
| 7254 | **hall** | 1 | 135.20 | 7.801376 | 🔵 low — common in general English | - |
| 7255 | **tended** | 1 | 135.20 | 7.801376 | 🔵 low — common in general English | - |
| 7256 | **adapt** | 1 | 135.20 | 7.801376 | 🔵 low — common in general English | - |
| 7257 | **rolling** | 1 | 135.20 | 7.801376 | 🔵 low — common in general English | - |
| 7258 | **claiming** | 1 | 135.20 | 7.801376 | 🔵 low — common in general English | - |
| 7259 | **consequently** | 1 | 135.20 | 7.801376 | 🔵 low — common in general English | - |
| 7260 | **crew** | 1 | 135.20 | 7.801376 | 🔵 low — common in general English | - |
| 7261 | **soaring** | 1 | 135.20 | 7.801376 | 🔵 low — common in general English | - |
| 7262 | **classified** | 1 | 135.20 | 7.801376 | 🔵 low — common in general English | - |
| 7263 | **describing** | 1 | 135.20 | 7.801376 | 🔵 low — common in general English | - |
| 7264 | **wash** | 1 | 135.20 | 7.801376 | 🔵 low — common in general English | - |
| 7265 | **unstable** | 1 | 135.20 | 7.801376 | 🔵 low — common in general English | - |
| 7266 | **recording** | 1 | 135.20 | 7.801376 | 🔵 low — common in general English | - |
| 7267 | **forming** | 1 | 133.81 | 7.721333 | 🔵 low — common in general English | - |
| 7268 | **revive** | 1 | 133.81 | 7.721333 | 🔵 low — common in general English | - |
| 7269 | **location** | 1 | 133.81 | 7.721333 | 🔵 low — common in general English | - |
| 7270 | **sceptical** | 1 | 133.81 | 7.721333 | 🔵 low — common in general English | - |
| 7271 | **opposing** | 1 | 133.81 | 7.721333 | 🔵 low — common in general English | - |
| 7272 | **combining** | 1 | 133.81 | 7.721333 | 🔵 low — common in general English | - |
| 7273 | **composite** | 1 | 133.81 | 7.721333 | 🔵 low — common in general English | - |
| 7274 | **ideal** | 1 | 133.81 | 7.721333 | 🔵 low — common in general English | - |
| 7275 | **modify** | 1 | 133.81 | 7.721333 | 🔵 low — common in general English | - |
| 7276 | **repaying** | 1 | 133.81 | 7.721333 | 🔵 low — common in general English | - |
| 7277 | **cake** | 1 | 133.81 | 7.721333 | 🔵 low — common in general English | - |
| 7278 | **appreciate** | 1 | 133.81 | 7.721333 | 🔵 low — common in general English | - |
| 7279 | **goodwill** | 1 | 133.81 | 7.721333 | 🔵 low — common in general English | - |
| 7280 | **substitute** | 1 | 133.81 | 7.721333 | 🔵 low — common in general English | - |
| 7281 | **interesting** | 1 | 133.81 | 7.721333 | 🔵 low — common in general English | - |
| 7282 | **mission** | 1 | 133.81 | 7.721333 | 🔵 low — common in general English | - |
| 7283 | **thin** | 1 | 133.81 | 7.721333 | 🔵 low — common in general English | - |
| 7284 | **tangible** | 1 | 133.81 | 7.721333 | 🔵 low — common in general English | - |
| 7285 | **feature** | 1 | 133.81 | 7.721333 | 🔵 low — common in general English | - |
| 7286 | **destination** | 1 | 133.81 | 7.721333 | 🔵 low — common in general English | - |
| 7287 | **dot** | 1 | 133.81 | 7.721333 | 🔵 low — common in general English | - |
| 7288 | **played** | 1 | 132.53 | 7.647225 | 🔵 low — common in general English | - |
| 7289 | **thereby** | 1 | 132.53 | 7.647225 | 🔵 low — common in general English | - |
| 7290 | **weaken** | 1 | 132.53 | 7.647225 | 🔵 low — common in general English | - |
| 7291 | **remark** | 1 | 132.53 | 7.647225 | 🔵 low — common in general English | - |
| 7292 | **blame** | 1 | 132.53 | 7.647225 | 🔵 low — common in general English | - |
| 7293 | **accompanying** | 1 | 132.53 | 7.647225 | 🔵 low — common in general English | - |
| 7294 | **asa** | 1 | 132.53 | 7.647225 | 🔵 low — common in general English | - |
| 7295 | **dipped** | 1 | 132.53 | 7.647225 | 🔵 low — common in general English | - |
| 7296 | **professor** | 1 | 132.53 | 7.647225 | 🔵 low — common in general English | - |
| 7297 | **reacted** | 1 | 132.53 | 7.647225 | 🔵 low — common in general English | - |
| 7298 | **thereafter** | 1 | 132.53 | 7.647225 | 🔵 low — common in general English | - |
| 7299 | **game** | 1 | 132.53 | 7.647225 | 🔵 low — common in general English | - |
| 7300 | **exclusively** | 1 | 132.53 | 7.647225 | 🔵 low — common in general English | - |
| 7301 | **chosen** | 1 | 132.53 | 7.647225 | 🔵 low — common in general English | - |
| 7302 | **motion** | 1 | 132.53 | 7.647225 | 🔵 low — common in general English | - |
| 7303 | **testing** | 1 | 131.33 | 7.578232 | 🔵 low — common in general English | - |
| 7304 | **stored** | 1 | 131.33 | 7.578232 | 🔵 low — common in general English | - |
| 7305 | **mer** | 1 | 131.33 | 7.578232 | 🔵 low — common in general English | - |
| 7306 | **justified** | 1 | 131.33 | 7.578232 | 🔵 low — common in general English | - |
| 7307 | **rated** | 1 | 131.33 | 7.578232 | 🔵 low — common in general English | - |
| 7308 | **candidate** | 1 | 131.33 | 7.578232 | 🔵 low — common in general English | - |
| 7309 | **challenged** | 1 | 131.33 | 7.578232 | 🔵 low — common in general English | - |
| 7310 | **seller** | 1 | 131.33 | 7.578232 | 🔵 low — common in general English | - |
| 7311 | **revolving** | 1 | 131.33 | 7.578232 | 🔵 low — common in general English | - |
| 7312 | **interpreted** | 1 | 131.33 | 7.578232 | 🔵 low — common in general English | - |
| 7313 | **sending** | 1 | 131.33 | 7.578232 | 🔵 low — common in general English | - |
| 7314 | **declare** | 1 | 130.21 | 7.513694 | 🔵 low — common in general English | - |
| 7315 | **driving** | 1 | 130.21 | 7.513694 | 🔵 low — common in general English | - |
| 7316 | **comprise** | 1 | 130.21 | 7.513694 | 🔵 low — common in general English | - |
| 7317 | **inevitable** | 1 | 130.21 | 7.513694 | 🔵 low — common in general English | - |
| 7318 | **ferry** | 1 | 130.21 | 7.513694 | 🔵 low — common in general English | - |
| 7319 | **undertaken** | 1 | 130.21 | 7.513694 | 🔵 low — common in general English | - |
| 7320 | **coin** | 1 | 130.21 | 7.513694 | 🔵 low — common in general English | - |
| 7321 | **mild** | 1 | 130.21 | 7.513694 | 🔵 low — common in general English | - |
| 7322 | **wary** | 1 | 130.21 | 7.513694 | 🔵 low — common in general English | - |
| 7323 | **emerging** | 1 | 130.21 | 7.513694 | 🔵 low — common in general English | - |
| 7324 | **obligation** | 1 | 130.21 | 7.513694 | 🔵 low — common in general English | - |
| 7325 | **worry** | 1 | 130.21 | 7.513694 | 🔵 low — common in general English | - |
| 7326 | **unlike** | 1 | 130.21 | 7.513694 | 🔵 low — common in general English | - |
| 7327 | **soil** | 1 | 130.21 | 7.513694 | 🔵 low — common in general English | - |
| 7328 | **sale** | 2 | 129.81 | 3.745252 | 🔵 low — common in general English | - |
| 7329 | **decree** | 1 | 129.16 | 7.453069 | 🔵 low — common in general English | - |
| 7330 | **historical** | 1 | 129.16 | 7.453069 | 🔵 low — common in general English | - |
| 7331 | **calculating** | 1 | 129.16 | 7.453069 | 🔵 low — common in general English | - |
| 7332 | **sharing** | 1 | 129.16 | 7.453069 | 🔵 low — common in general English | - |
| 7333 | **assessment** | 1 | 129.16 | 7.453069 | 🔵 low — common in general English | - |
| 7334 | **regularly** | 1 | 129.16 | 7.453069 | 🔵 low — common in general English | - |
| 7335 | **reacting** | 1 | 129.16 | 7.453069 | 🔵 low — common in general English | - |
| 7336 | **farming** | 1 | 129.16 | 7.453069 | 🔵 low — common in general English | - |
| 7337 | **rejection** | 1 | 129.16 | 7.453069 | 🔵 low — common in general English | - |
| 7338 | **imposing** | 1 | 128.17 | 7.395911 | 🔵 low — common in general English | - |
| 7339 | **obvious** | 1 | 128.17 | 7.395911 | 🔵 low — common in general English | - |
| 7340 | **permission** | 1 | 128.17 | 7.395911 | 🔵 low — common in general English | - |
| 7341 | **fix** | 1 | 128.17 | 7.395911 | 🔵 low — common in general English | - |
| 7342 | **procedure** | 1 | 128.17 | 7.395911 | 🔵 low — common in general English | - |
| 7343 | **demanded** | 1 | 128.17 | 7.395911 | 🔵 low — common in general English | - |
| 7344 | **convince** | 1 | 128.17 | 7.395911 | 🔵 low — common in general English | - |
| 7345 | **secondary** | 1 | 128.17 | 7.395911 | 🔵 low — common in general English | - |
| 7346 | **apparel** | 1 | 128.17 | 7.395911 | 🔵 low — common in general English | - |
| 7347 | **society** | 1 | 128.17 | 7.395911 | 🔵 low — common in general English | - |
| 7348 | **lesser** | 1 | 128.17 | 7.395911 | 🔵 low — common in general English | - |
| 7349 | **ali** | 1 | 127.23 | 7.341843 | 🔵 low — common in general English | - |
| 7350 | **bob** | 1 | 127.23 | 7.341843 | 🔵 low — common in general English | - |
| 7351 | **milling** | 1 | 127.23 | 7.341843 | 🔵 low — common in general English | - |
| 7352 | **returning** | 1 | 127.23 | 7.341843 | 🔵 low — common in general English | - |
| 7353 | **handle** | 1 | 127.23 | 7.341843 | 🔵 low — common in general English | - |
| 7354 | **consent** | 1 | 127.23 | 7.341843 | 🔵 low — common in general English | - |
| 7355 | **evaluating** | 1 | 127.23 | 7.341843 | 🔵 low — common in general English | - |
| 7356 | **hurting** | 1 | 127.23 | 7.341843 | 🔵 low — common in general English | - |
| 7357 | **sensitive** | 1 | 127.23 | 7.341843 | 🔵 low — common in general English | - |
| 7358 | **judge** | 1 | 127.23 | 7.341843 | 🔵 low — common in general English | - |
| 7359 | **version** | 1 | 127.23 | 7.341843 | 🔵 low — common in general English | - |
| 7360 | **slack** | 1 | 126.34 | 7.29055 | 🔵 low — common in general English | - |
| 7361 | **favoured** | 1 | 126.34 | 7.29055 | 🔵 low — common in general English | - |
| 7362 | **quiet** | 1 | 126.34 | 7.29055 | 🔵 low — common in general English | - |
| 7363 | **mile** | 1 | 126.34 | 7.29055 | 🔵 low — common in general English | - |
| 7364 | **park** | 1 | 126.34 | 7.29055 | 🔵 low — common in general English | - |
| 7365 | **arranging** | 1 | 126.34 | 7.29055 | 🔵 low — common in general English | - |
| 7366 | **limiting** | 1 | 125.50 | 7.24176 | 🔵 low — common in general English | - |
| 7367 | **ward** | 1 | 125.50 | 7.24176 | 🔵 low — common in general English | - |
| 7368 | **reversal** | 1 | 125.50 | 7.24176 | 🔵 low — common in general English | - |
| 7369 | **accident** | 1 | 125.50 | 7.24176 | 🔵 low — common in general English | - |
| 7370 | **treasurer** | 1 | 125.50 | 7.24176 | 🔵 low — common in general English | - |
| 7371 | **concerted** | 1 | 125.50 | 7.24176 | 🔵 low — common in general English | - |
| 7372 | **pressed** | 1 | 125.50 | 7.24176 | 🔵 low — common in general English | - |
| 7373 | **prevented** | 1 | 125.50 | 7.24176 | 🔵 low — common in general English | - |
| 7374 | **alter** | 1 | 125.50 | 7.24176 | 🔵 low — common in general English | - |
| 7375 | **acted** | 1 | 125.50 | 7.24176 | 🔵 low — common in general English | - |
| 7376 | **evaluation** | 1 | 125.50 | 7.24176 | 🔵 low — common in general English | - |
| 7377 | **lanka** | 1 | 125.50 | 7.24176 | 🔵 low — common in general English | - |
| 7378 | **chamber** | 1 | 125.50 | 7.24176 | 🔵 low — common in general English | - |
| 7379 | **exercised** | 1 | 124.69 | 7.19524 | 🔵 low — common in general English | - |
| 7380 | **century** | 1 | 124.69 | 7.19524 | 🔵 low — common in general English | - |
| 7381 | **engine** | 1 | 124.69 | 7.19524 | 🔵 low — common in general English | - |
| 7382 | **accused** | 1 | 124.69 | 7.19524 | 🔵 low — common in general English | - |
| 7383 | **criteria** | 1 | 124.69 | 7.19524 | 🔵 low — common in general English | - |
| 7384 | **track** | 1 | 124.69 | 7.19524 | 🔵 low — common in general English | - |
| 7385 | **pro** | 1 | 124.69 | 7.19524 | 🔵 low — common in general English | - |
| 7386 | **distribute** | 1 | 124.69 | 7.19524 | 🔵 low — common in general English | - |
| 7387 | **challenge** | 1 | 124.69 | 7.19524 | 🔵 low — common in general English | - |
| 7388 | **instrument** | 1 | 124.69 | 7.19524 | 🔵 low — common in general English | - |
| 7389 | **cane** | 1 | 123.92 | 7.150788 | 🔵 low — common in general English | - |
| 7390 | **linking** | 1 | 123.92 | 7.150788 | 🔵 low — common in general English | - |
| 7391 | **disappointed** | 1 | 123.92 | 7.150788 | 🔵 low — common in general English | - |
| 7392 | **reject** | 1 | 123.92 | 7.150788 | 🔵 low — common in general English | - |
| 7393 | **defined** | 1 | 123.92 | 7.150788 | 🔵 low — common in general English | - |
| 7394 | **secured** | 1 | 123.92 | 7.150788 | 🔵 low — common in general English | - |
| 7395 | **dominion** | 1 | 123.92 | 7.150788 | 🔵 low — common in general English | - |
| 7396 | **considerably** | 1 | 123.18 | 7.108229 | 🔵 low — common in general English | - |
| 7397 | **basket** | 1 | 123.18 | 7.108229 | 🔵 low — common in general English | - |
| 7398 | **preserve** | 1 | 123.18 | 7.108229 | 🔵 low — common in general English | - |
| 7399 | **entering** | 1 | 122.48 | 7.067407 | 🔵 low — common in general English | - |
| 7400 | **freeze** | 1 | 122.48 | 7.067407 | 🔵 low — common in general English | - |
| 7401 | **accelerate** | 1 | 122.48 | 7.067407 | 🔵 low — common in general English | - |
| 7402 | **negotiation** | 1 | 122.48 | 7.067407 | 🔵 low — common in general English | - |
| 7403 | **awaiting** | 1 | 122.48 | 7.067407 | 🔵 low — common in general English | - |
| 7404 | **consuming** | 1 | 122.48 | 7.067407 | 🔵 low — common in general English | - |
| 7405 | **successfully** | 1 | 122.48 | 7.067407 | 🔵 low — common in general English | - |
| 7406 | **discovered** | 1 | 122.48 | 7.067407 | 🔵 low — common in general English | - |
| 7407 | **spur** | 1 | 122.48 | 7.067407 | 🔵 low — common in general English | - |
| 7408 | **contrast** | 1 | 121.80 | 7.028186 | 🔵 low — common in general English | - |
| 7409 | **valid** | 1 | 121.80 | 7.028186 | 🔵 low — common in general English | - |
| 7410 | **participating** | 1 | 121.80 | 7.028186 | 🔵 low — common in general English | - |
| 7411 | **forcing** | 1 | 121.80 | 7.028186 | 🔵 low — common in general English | - |
| 7412 | **questioned** | 1 | 121.80 | 7.028186 | 🔵 low — common in general English | - |
| 7413 | **sixth** | 1 | 121.80 | 7.028186 | 🔵 low — common in general English | - |
| 7414 | **printing** | 1 | 121.80 | 7.028186 | 🔵 low — common in general English | - |
| 7415 | **table** | 1 | 121.14 | 6.990446 | 🔵 low — common in general English | - |
| 7416 | **exact** | 1 | 121.14 | 6.990446 | 🔵 low — common in general English | - |
| 7417 | **convert** | 1 | 121.14 | 6.990446 | 🔵 low — common in general English | - |
| 7418 | **qualified** | 1 | 121.14 | 6.990446 | 🔵 low — common in general English | - |
| 7419 | **window** | 1 | 121.14 | 6.990446 | 🔵 low — common in general English | - |
| 7420 | **match** | 1 | 120.51 | 6.954078 | 🔵 low — common in general English | - |
| 7421 | **tighten** | 1 | 120.51 | 6.954078 | 🔵 low — common in general English | - |
| 7422 | **flour** | 1 | 120.51 | 6.954078 | 🔵 low — common in general English | - |
| 7423 | **reply** | 1 | 120.51 | 6.954078 | 🔵 low — common in general English | - |
| 7424 | **acceptance** | 1 | 120.51 | 6.954078 | 🔵 low — common in general English | - |
| 7425 | **scope** | 1 | 120.51 | 6.954078 | 🔵 low — common in general English | - |
| 7426 | **diamond** | 1 | 119.90 | 6.918987 | 🔵 low — common in general English | - |
| 7427 | **engaged** | 1 | 119.90 | 6.918987 | 🔵 low — common in general English | - |
| 7428 | **necessarily** | 1 | 119.90 | 6.918987 | 🔵 low — common in general English | - |
| 7429 | **soared** | 1 | 119.90 | 6.918987 | 🔵 low — common in general English | - |
| 7430 | **handling** | 1 | 119.90 | 6.918987 | 🔵 low — common in general English | - |
| 7431 | **tobacco** | 1 | 119.90 | 6.918987 | 🔵 low — common in general English | - |
| 7432 | **discussing** | 1 | 119.90 | 6.918987 | 🔵 low — common in general English | - |
| 7433 | **optimism** | 1 | 119.32 | 6.885085 | 🔵 low — common in general English | - |
| 7434 | **prevailing** | 1 | 119.32 | 6.885085 | 🔵 low — common in general English | - |
| 7435 | **expecting** | 1 | 119.32 | 6.885085 | 🔵 low — common in general English | - |
| 7436 | **critical** | 1 | 119.32 | 6.885085 | 🔵 low — common in general English | - |
| 7437 | **proceeding** | 1 | 119.32 | 6.885085 | 🔵 low — common in general English | - |
| 7438 | **conducted** | 1 | 119.32 | 6.885085 | 🔵 low — common in general English | - |
| 7439 | **respective** | 1 | 119.32 | 6.885085 | 🔵 low — common in general English | - |
| 7440 | **speed** | 1 | 119.32 | 6.885085 | 🔵 low — common in general English | - |
| 7441 | **friendly** | 1 | 119.32 | 6.885085 | 🔵 low — common in general English | - |
| 7442 | **adopt** | 1 | 119.32 | 6.885085 | 🔵 low — common in general English | - |
| 7443 | **explore** | 1 | 118.75 | 6.852295 | 🔵 low — common in general English | - |
| 7444 | **tool** | 1 | 118.75 | 6.852295 | 🔵 low — common in general English | - |
| 7445 | **quick** | 1 | 118.75 | 6.852295 | 🔵 low — common in general English | - |
| 7446 | **incurred** | 1 | 118.75 | 6.852295 | 🔵 low — common in general English | - |
| 7447 | **somewhat** | 1 | 118.75 | 6.852295 | 🔵 low — common in general English | - |
| 7448 | **eliminate** | 1 | 118.75 | 6.852295 | 🔵 low — common in general English | - |
| 7449 | **settled** | 1 | 118.75 | 6.852295 | 🔵 low — common in general English | - |
| 7450 | **responding** | 1 | 118.75 | 6.852295 | 🔵 low — common in general English | - |
| 7451 | **deterioration** | 1 | 118.20 | 6.820546 | 🔵 low — common in general English | - |
| 7452 | **formula** | 1 | 118.20 | 6.820546 | 🔵 low — common in general English | - |
| 7453 | **rally** | 1 | 118.20 | 6.820546 | 🔵 low — common in general English | - |
| 7454 | **steadily** | 1 | 118.20 | 6.820546 | 🔵 low — common in general English | - |
| 7455 | **flag** | 1 | 118.20 | 6.820546 | 🔵 low — common in general English | - |
| 7456 | **extensive** | 1 | 118.20 | 6.820546 | 🔵 low — common in general English | - |
| 7457 | **enhance** | 1 | 117.67 | 6.789775 | 🔵 low — common in general English | - |
| 7458 | **tightening** | 1 | 117.67 | 6.789775 | 🔵 low — common in general English | - |
| 7459 | **permanent** | 1 | 117.67 | 6.789775 | 🔵 low — common in general English | - |
| 7460 | **play** | 1 | 117.67 | 6.789775 | 🔵 low — common in general English | - |
| 7461 | **informed** | 1 | 117.67 | 6.789775 | 🔵 low — common in general English | - |
| 7462 | **prompted** | 1 | 117.67 | 6.789775 | 🔵 low — common in general English | - |
| 7463 | **incentive** | 1 | 117.67 | 6.789775 | 🔵 low — common in general English | - |
| 7464 | **indirect** | 1 | 117.15 | 6.759922 | 🔵 low — common in general English | - |
| 7465 | **healthy** | 1 | 117.15 | 6.759922 | 🔵 low — common in general English | - |
| 7466 | **missile** | 1 | 117.15 | 6.759922 | 🔵 low — common in general English | - |
| 7467 | **reaching** | 1 | 117.15 | 6.759922 | 🔵 low — common in general English | - |
| 7468 | **southeast** | 1 | 116.65 | 6.730934 | 🔵 low — common in general English | - |
| 7469 | **withdraw** | 1 | 116.65 | 6.730934 | 🔵 low — common in general English | - |
| 7470 | **burden** | 1 | 116.65 | 6.730934 | 🔵 low — common in general English | - |
| 7471 | **maturing** | 1 | 116.16 | 6.702763 | 🔵 low — common in general English | - |
| 7472 | **merchandise** | 1 | 116.16 | 6.702763 | 🔵 low — common in general English | - |
| 7473 | **flexible** | 1 | 116.16 | 6.702763 | 🔵 low — common in general English | - |
| 7474 | **chase** | 1 | 115.68 | 6.675364 | 🔵 low — common in general English | - |
| 7475 | **reviewing** | 1 | 115.68 | 6.675364 | 🔵 low — common in general English | - |
| 7476 | **uncertain** | 1 | 115.22 | 6.648696 | 🔵 low — common in general English | - |
| 7477 | **aggregate** | 1 | 115.22 | 6.648696 | 🔵 low — common in general English | - |
| 7478 | **southwest** | 1 | 114.77 | 6.622721 | 🔵 low — common in general English | - |
| 7479 | **northwest** | 1 | 114.77 | 6.622721 | 🔵 low — common in general English | - |
| 7480 | **referring** | 1 | 114.77 | 6.622721 | 🔵 low — common in general English | - |
| 7481 | **record** | 2 | 114.33 | 3.298792 | 🔵 low — common in general English | - |
| 7482 | **job** | 1 | 114.33 | 6.597403 | 🔵 low — common in general English | - |
| 7483 | **sum** | 1 | 114.33 | 6.597403 | 🔵 low — common in general English | - |
| 7484 | **scheme** | 1 | 114.33 | 6.597403 | 🔵 low — common in general English | - |
| 7485 | **fast** | 1 | 114.33 | 6.597403 | 🔵 low — common in general English | - |
| 7486 | **solution** | 1 | 113.90 | 6.57271 | 🔵 low — common in general English | - |
| 7487 | **investigation** | 1 | 113.90 | 6.57271 | 🔵 low — common in general English | - |
| 7488 | **promote** | 1 | 113.49 | 6.548613 | 🔵 low — common in general English | - |
| 7489 | **remove** | 1 | 113.49 | 6.548613 | 🔵 low — common in general English | - |
| 7490 | **regarding** | 1 | 113.08 | 6.525082 | 🔵 low — common in general English | - |
| 7491 | **dealing** | 1 | 113.08 | 6.525082 | 🔵 low — common in general English | - |
| 7492 | **arrangement** | 1 | 112.68 | 6.502093 | 🔵 low — common in general English | - |
| 7493 | **effectively** | 1 | 112.68 | 6.502093 | 🔵 low — common in general English | - |
| 7494 | **dumping** | 1 | 112.29 | 6.47962 | 🔵 low — common in general English | - |
| 7495 | **announce** | 1 | 112.29 | 6.47962 | 🔵 low — common in general English | - |
| 7496 | **maintained** | 1 | 111.91 | 6.457641 | 🔵 low — common in general English | - |
| 7497 | **respond** | 1 | 111.91 | 6.457641 | 🔵 low — common in general English | - |
| 7498 | **compete** | 1 | 111.91 | 6.457641 | 🔵 low — common in general English | - |
| 7499 | **widely** | 1 | 111.54 | 6.436135 | 🔵 low — common in general English | - |
| 7500 | **duty** | 1 | 111.54 | 6.436135 | 🔵 low — common in general English | - |
| 7501 | **calculated** | 1 | 111.54 | 6.436135 | 🔵 low — common in general English | - |
| 7502 | **planted** | 1 | 111.17 | 6.415081 | 🔵 low — common in general English | - |
| 7503 | **strengthen** | 1 | 111.17 | 6.415081 | 🔵 low — common in general English | - |
| 7504 | **consistent** | 1 | 111.17 | 6.415081 | 🔵 low — common in general English | - |
| 7505 | **charged** | 1 | 111.17 | 6.415081 | 🔵 low — common in general English | - |
| 7506 | **showing** | 1 | 110.81 | 6.394462 | 🔵 low — common in general English | - |
| 7507 | **list** | 1 | 110.46 | 6.374259 | 🔵 low — common in general English | - |
| 7508 | **increasingly** | 1 | 110.46 | 6.374259 | 🔵 low — common in general English | - |
| 7509 | **appreciation** | 1 | 110.46 | 6.374259 | 🔵 low — common in general English | - |
| 7510 | **broadly** | 1 | 110.46 | 6.374259 | 🔵 low — common in general English | - |
| 7511 | **apparently** | 1 | 110.12 | 6.354457 | 🔵 low — common in general English | - |
| 7512 | **contribution** | 1 | 110.12 | 6.354457 | 🔵 low — common in general English | - |
| 7513 | **concluded** | 1 | 110.12 | 6.354457 | 🔵 low — common in general English | - |
| 7514 | **shell** | 1 | 110.12 | 6.354457 | 🔵 low — common in general English | - |
| 7515 | **housing** | 1 | 109.79 | 6.335039 | 🔵 low — common in general English | - |
| 7516 | **stressed** | 1 | 109.79 | 6.335039 | 🔵 low — common in general English | - |
| 7517 | **represented** | 1 | 109.79 | 6.335039 | 🔵 low — common in general English | - |
| 7518 | **relief** | 1 | 109.45 | 6.31599 | 🔵 low — common in general English | - |
| 7519 | **smith** | 1 | 109.45 | 6.31599 | 🔵 low — common in general English | - |
| 7520 | **applied** | 1 | 109.45 | 6.31599 | 🔵 low — common in general English | - |
| 7521 | **moderate** | 1 | 109.45 | 6.31599 | 🔵 low — common in general English | - |
| 7522 | **expense** | 1 | 109.45 | 6.31599 | 🔵 low — common in general English | - |
| 7523 | **waiting** | 1 | 109.45 | 6.31599 | 🔵 low — common in general English | - |
| 7524 | **sentiment** | 1 | 109.13 | 6.297298 | 🔵 low — common in general English | - |
| 7525 | **affecting** | 1 | 108.81 | 6.278949 | 🔵 low — common in general English | - |
| 7526 | **indicate** | 1 | 108.81 | 6.278949 | 🔵 low — common in general English | - |
| 7527 | **uncertainty** | 1 | 108.50 | 6.260931 | 🔵 low — common in general English | - |
| 7528 | **mostly** | 1 | 108.50 | 6.260931 | 🔵 low — common in general English | - |
| 7529 | **resume** | 1 | 108.19 | 6.243231 | 🔵 low — common in general English | - |
| 7530 | **severe** | 1 | 108.19 | 6.243231 | 🔵 low — common in general English | - |
| 7531 | **portion** | 1 | 107.89 | 6.225839 | 🔵 low — common in general English | - |
| 7532 | **traditional** | 1 | 107.60 | 6.208745 | 🔵 low — common in general English | - |
| 7533 | **intervene** | 1 | 107.31 | 6.191938 | 🔵 low — common in general English | - |
| 7534 | **threat** | 1 | 107.02 | 6.175409 | 🔵 low — common in general English | - |
| 7535 | **gap** | 1 | 106.46 | 6.143148 | 🔵 low — common in general English | - |
| 7536 | **coal** | 1 | 106.19 | 6.127399 | 🔵 low — common in general English | - |
| 7537 | **medium** | 1 | 106.19 | 6.127399 | 🔵 low — common in general English | - |
| 7538 | **suggested** | 1 | 106.19 | 6.127399 | 🔵 low — common in general English | - |
| 7539 | **ups** | 1 | 105.92 | 6.111895 | 🔵 low — common in general English | - |
| 7540 | **subordinated** | 1 | 105.92 | 6.111895 | 🔵 low — common in general English | - |
| 7541 | **buyer** | 1 | 105.92 | 6.111895 | 🔵 low — common in general English | - |
| 7542 | **opposed** | 1 | 105.65 | 6.096628 | 🔵 low — common in general English | - |
| 7543 | **leader** | 1 | 105.65 | 6.096628 | 🔵 low — common in general English | - |
| 7544 | **stronger** | 1 | 105.14 | 6.066775 | 🔵 low — common in general English | - |
| 7545 | **fair** | 1 | 105.14 | 6.066775 | 🔵 low — common in general English | - |
| 7546 | **possibly** | 1 | 104.63 | 6.037787 | 🔵 low — common in general English | - |
| 7547 | **original** | 1 | 104.63 | 6.037787 | 🔵 low — common in general English | - |
| 7548 | **underlying** | 1 | 103.67 | 5.982217 | 🔵 low — common in general English | - |
| 7549 | **alternative** | 1 | 103.67 | 5.982217 | 🔵 low — common in general English | - |
| 7550 | **medical** | 1 | 103.44 | 5.968794 | 🔵 low — common in general English | - |
| 7551 | **raw** | 1 | 103.21 | 5.955549 | 🔵 low — common in general English | - |
| 7552 | **labour** | 1 | 103.21 | 5.955549 | 🔵 low — common in general English | - |
| 7553 | **active** | 1 | 103.21 | 5.955549 | 🔵 low — common in general English | - |
| 7554 | **profitable** | 1 | 102.76 | 5.929574 | 🔵 low — common in general English | - |
| 7555 | **rice** | 1 | 102.76 | 5.929574 | 🔵 low — common in general English | - |
| 7556 | **note** | 2 | 102.61 | 2.960475 | 🔵 low — common in general English | - |
| 7557 | **exceed** | 1 | 102.54 | 5.916835 | 🔵 low — common in general English | - |
| 7558 | **sought** | 1 | 102.54 | 5.916835 | 🔵 low — common in general English | - |
| 7559 | **governor** | 1 | 102.10 | 5.891833 | 🔵 low — common in general English | - |
| 7560 | **block** | 1 | 102.10 | 5.891833 | 🔵 low — common in general English | - |
| 7561 | **originally** | 1 | 101.07 | 5.831935 | 🔵 low — common in general English | - |
| 7562 | **afternoon** | 1 | 101.07 | 5.831935 | 🔵 low — common in general English | - |
| 7563 | **via** | 1 | 100.87 | 5.820374 | 🔵 low — common in general English | - |
| 7564 | **expressed** | 1 | 100.47 | 5.797646 | 🔵 low — common in general English | - |
| 7565 | **legal** | 1 | 100.28 | 5.786473 | 🔵 low — common in general English | - |
| 7566 | **yield** | 1 | 100.28 | 5.786473 | 🔵 low — common in general English | - |
| 7567 | **resulted** | 1 | 100.09 | 5.775423 | 🔵 low — common in general English | - |
| 7568 | **authorized** | 1 | 99.71 | 5.753683 | 🔵 low — common in general English | - |
| 7569 | **fuel** | 1 | 99.34 | 5.732405 | 🔵 low — common in general English | - |
| 7570 | **indicated** | 1 | 99.34 | 5.732405 | 🔵 low — common in general English | - |
| 7571 | **designed** | 1 | 99.34 | 5.732405 | 🔵 low — common in general English | - |
| 7572 | **projected** | 1 | 98.98 | 5.711571 | 🔵 low — common in general English | - |
| 7573 | **aid** | 1 | 97.77 | 5.641891 | 🔵 low — common in general English | - |
| 7574 | **recovery** | 1 | 97.61 | 5.632322 | 🔵 low — common in general English | - |
| 7575 | **planning** | 1 | 97.61 | 5.632322 | 🔵 low — common in general English | - |
| 7576 | **estate** | 1 | 97.28 | 5.613454 | 🔵 low — common in general English | - |
| 7577 | **bond** | 1 | 97.28 | 5.613454 | 🔵 low — common in general English | - |
| 7578 | **stable** | 1 | 97.12 | 5.604151 | 🔵 low — common in general English | - |
| 7579 | **project** | 1 | 96.96 | 5.594934 | 🔵 low — common in general English | - |
| 7580 | **minimum** | 1 | 96.18 | 5.550084 | 🔵 low — common in general English | - |
| 7581 | **construction** | 1 | 96.03 | 5.54135 | 🔵 low — common in general English | - |
| 7582 | **posted** | 1 | 95.88 | 5.532692 | 🔵 low — common in general English | - |
| 7583 | **failed** | 1 | 95.73 | 5.524108 | 🔵 low — common in general English | - |
| 7584 | **raising** | 1 | 95.73 | 5.524108 | 🔵 low — common in general English | - |
| 7585 | **assistance** | 1 | 95.44 | 5.507159 | 🔵 low — common in general English | - |
| 7586 | **believed** | 1 | 95.29 | 5.498791 | 🔵 low — common in general English | - |
| 7587 | **performance** | 1 | 93.00 | 5.366301 | 🔵 low — common in general English | - |
| 7588 | **plus** | 1 | 92.87 | 5.359029 | 🔵 low — common in general English | - |
| 7589 | **consumption** | 1 | 92.62 | 5.34464 | 🔵 low — common in general English | - |
| 7590 | **closing** | 1 | 92.38 | 5.330455 | 🔵 low — common in general English | - |
| 7591 | **rejected** | 1 | 92.01 | 5.309549 | 🔵 low — common in general English | - |
| 7592 | **information** | 1 | 91.66 | 5.28907 | 🔵 low — common in general English | - |
| 7593 | **required** | 1 | 91.20 | 5.262402 | 🔵 low — common in general English | - |
| 7594 | **producing** | 1 | 90.97 | 5.24933 | 🔵 low — common in general English | - |
| 7595 | **nearly** | 1 | 90.64 | 5.230037 | 🔵 low — common in general English | - |
| 7596 | **regular** | 1 | 90.53 | 5.223687 | 🔵 low — common in general English | - |
| 7597 | **significant** | 1 | 89.26 | 5.150484 | 🔵 low — common in general English | - |
| 7598 | **initial** | 1 | 89.05 | 5.138788 | 🔵 low — common in general English | - |
| 7599 | **farm** | 1 | 88.85 | 5.127227 | 🔵 low — common in general English | - |
| 7600 | **gross** | 1 | 88.17 | 5.087785 | 🔵 low — common in general English | - |
| 7601 | **adding** | 1 | 87.06 | 5.023592 | 🔵 low — common in general English | - |
| 7602 | **range** | 1 | 86.44 | 4.987965 | 🔵 low — common in general English | - |
| 7603 | **respectively** | 1 | 86.35 | 4.982977 | 🔵 low — common in general English | - |
| 7604 | **probably** | 1 | 86.18 | 4.973076 | 🔵 low — common in general English | - |
| 7605 | **charge** | 1 | 85.35 | 4.92499 | 🔵 low — common in general English | - |
| 7606 | **selling** | 1 | 84.09 | 4.85256 | 🔵 low — common in general English | - |
| 7607 | **buying** | 1 | 82.50 | 4.760829 | 🔵 low — common in general English | - |
| 7608 | **despite** | 1 | 81.50 | 4.702786 | 🔵 low — common in general English | - |
| 7609 | **net** | 2 | 80.36 | 2.318656 | 🔵 low — common in general English | net, nets |
| 7610 | **transaction** | 1 | 80.30 | 4.633793 | 🔵 low — common in general English | - |
| 7611 | **available** | 1 | 79.59 | 4.59255 | 🔵 low — common in general English | - |
| 7612 | **secretary** | 1 | 79.24 | 4.57255 | 🔵 low — common in general English | - |
| 7613 | **loan** | 1 | 77.35 | 4.463236 | 🔵 low — common in general English | - |
| 7614 | **public** | 1 | 76.25 | 4.400178 | 🔵 low — common in general English | - |
| 7615 | **bought** | 1 | 74.65 | 4.307397 | 🔵 low — common in general English | - |
| 7616 | **outstanding** | 1 | 70.91 | 4.091877 | 🔵 low — common in general English | - |
| 7617 | **yesterday** | 1 | 70.42 | 4.063706 | 🔵 low — common in general English | - |
| 7618 | **trading** | 1 | 70.35 | 4.059746 | 🔵 low — common in general English | - |
| 7619 | **capital** | 1 | 69.49 | 4.009639 | 🔵 low — common in general English | - |
| 7620 | **statement** | 1 | 67.90 | 3.918095 | 🔵 low — common in general English | - |
| 7621 | **industry** | 1 | 67.84 | 3.914671 | 🔵 low — common in general English | - |
| 7622 | **official** | 1 | 65.21 | 3.76272 | 🔵 low — common in general English | - |
| 7623 | **production** | 1 | 65.08 | 3.755405 | 🔵 low — common in general English | - |
| 7624 | **tax** | 1 | 65.00 | 3.751041 | 🔵 low — common in general English | - |
| 7625 | **rose** | 1 | 63.77 | 3.679632 | 🔵 low — common in general English | - |
| 7626 | **agreed** | 1 | 63.74 | 3.678282 | 🔵 low — common in general English | - |
| 7627 | **foreign** | 1 | 63.35 | 3.655599 | 🔵 low — common in general English | - |
| 7628 | **government** | 1 | 60.98 | 3.518939 | 🔵 low — common in general English | - |
| 7629 | **expected** | 1 | 58.67 | 3.385552 | 🔵 low — common in general English | - |
| 7630 | **exchange** | 1 | 58.64 | 3.38354 | 🔵 low — common in general English | - |
| 7631 | **agreement** | 1 | 58.50 | 3.375532 | 🔵 low — common in general English | - |
| 7632 | **stock** | 1 | 52.87 | 3.050663 | 🔵 low — common in general English | - |

---

*Corpus reference: Reuters-21578 (10,788 newswire documents) via NLTK · sklearn TfidfVectorizer(smooth\_idf=True, lowercase=True).*  
*Lemmatization: rule-based plural/possessive reduction (spaCy unavailable in this environment); irregular plurals (children, men, women, people, feet, teeth) handled via an explicit mapping.*  
*Regenerated 2026-08-04 — normalized pass added on top of the original `generate_termbase.py` output.*

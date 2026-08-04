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

## Most Distinctive Words (highest TF-IDF, normalized)

Words that appear **frequently in this text** yet are **rare or absent in general English**. Lemmatized: plural/possessive variants (e.g. *buddhas* → *buddha*) are merged into one row.

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
## Full Ranked Table (normalized + YAKE n-gram keywords combined)

Combines the two keyword passes into one table. The first 7,632 rows are the lemmatized TF-IDF word list (plural/possessive surface variants merged into one row per lemma; see **Variants merged**), ranked by TF-IDF descending. Where a word also scored as a standalone keyword in the separate YAKE pass, its **YAKE score** is shown alongside (lower = more important on YAKE's own scale — not comparable to the TF-IDF column). The remaining rows are the 1,558 multi-word YAKE phrases (bigrams/trigrams verified to occur literally in `en.md`) that have no single-word TF-IDF equivalent — these are appended after the word rows, ranked by YAKE score ascending.

| Rank | Term | Count | TF-IDF | IDF | Band | YAKE score | Variants merged | Glossary |
|------|------|-------|--------|-----|------|-----------|----------------|---------|
| 1 | **dharma** | 409 | 67,972.93 | 9.59 | 🔴 extremely high — text-exclusive | 0.000066 | - | ✓ ཆོས |
| 2 | **buddha** | 364 | 60,494.25 | 9.59 | 🔴 extremely high — text-exclusive | 0.000120 | buddha, buddhas | ✓ སངས་རྒྱས |
| 3 | **teacher** | 373 | 57,529.73 | 8.899988 | 🔴 extremely high — text-exclusive | 0.000327 | teacher, teachers | ~ |
| 4 | **teaching** | 218 | 36,230.07 | 9.59 | 🟠 very high — domain-specific | 0.001630 | teaching, teachings | ~ |
| 5 | **like** | 397 | 35,724.30 | 5.192532 | 🟠 very high — domain-specific | - | like, likes | — |
| 6 | **person** | 260 | 32,219.69 | 7.150788 | 🟠 very high — domain-specific | 0.004112 | people, person, persons | — |
| 7 | **mind** | 256 | 31,724.00 | 7.150788 | 🟠 very high — domain-specific | 0.000769 | mind, minds | ~ |
| 8 | **practice** | 236 | 27,769.08 | 6.789775 | 🟠 very high — domain-specific | 0.000961 | practice, practices | — |
| 9 | **action** | 340 | 26,092.45 | 4.428349 | 🟠 very high — domain-specific | 0.000450 | action, actions | ~ |
| 10 | **realm** | 149 | 24,762.75 | 9.59 | 🟠 very high — domain-specific | 0.002122 | realm, realms | ~ |
| 11 | **yourself** | 154 | 24,519.98 | 9.18767 | 🟠 very high — domain-specific | - | - | — |
| 12 | **compassion** | 147 | 24,438.36 | 9.593135 | 🟠 very high — domain-specific | 0.001779 | - | ~ |
| 13 | **suffering** | 192 | 24,095.69 | 7.24176 | 🟠 very high — domain-specific | 0.004281 | suffering, sufferings | ~ |
| 14 | **life** | 240 | 22,905.14 | 5.507159 | 🟠 very high — domain-specific | 0.000722 | - | — |
| 15 | **time** | 329 | 21,906.07 | 3.842151 | 🟠 very high — domain-specific | 0.000594 | time, times | — |
| 16 | **without** | 266 | 21,766.06 | 4.721762 | 🟠 very high — domain-specific | - | - | ~ |
| 17 | **bodhicitta** | 130 | 21,605.09 | 9.59 | 🟠 very high — domain-specific | 0.002119 | - | ✓ བྱང་ཆུབ་ཀྱི་སེམས |
| 18 | **never** | 197 | 21,562.63 | 6.31599 | 🟠 very high — domain-specific | - | - | — |
| 19 | **jewel** | 128 | 21,272.70 | 9.59 | 🟠 very high — domain-specific | 0.000988 | jewel, jewels | ~ |
| 20 | **merit** | 142 | 20,524.28 | 8.340372 | 🟠 very high — domain-specific | 0.001939 | merit, merits | ✓ བསོད་ནམས |
| 21 | **practise** | 123 | 20,448.42 | 9.593135 | 🟠 very high — domain-specific | 0.002308 | - | — |
| 22 | **body** | 180 | 19,761.32 | 6.335039 | 🟠 very high — domain-specific | 0.001752 | bodies, body | ~ |
| 23 | **path** | 145 | 19,603.49 | 7.801376 | 🟠 very high — domain-specific | 0.002170 | path, paths | ~ |
| 24 | **refuge** | 129 | 18,989.90 | 8.494523 | 🟠 very high — domain-specific | 0.002155 | refuge, refuges | — |
| 25 | **being** | 258 | 18,491.01 | 4.13568 | 🟠 very high — domain-specific | 0.059673 | - | ~ |
| 26 | **death** | 129 | 18,346.78 | 8.206841 | 🟠 very high — domain-specific | 0.001597 | death, deaths | ~ |
| 27 | **king** | 144 | 17,955.68 | 7.19524 | 🟠 very high — domain-specific | 0.001076 | king, kings | ~ |
| 28 | **hell** | 114 | 17,582.81 | 8.899988 | 🟠 very high — domain-specific | 0.002791 | hell, hells | ✓ དམྱལ་བ |
| 29 | **word** | 128 | 16,963.21 | 7.647225 | 🟠 very high — domain-specific | 0.002665 | word, words | ~ |
| 30 | **negative** | 166 | 16,949.33 | 5.891833 | 🟠 very high — domain-specific | 0.001416 | - | ~ |
| 31 | **offering** | 180 | 16,498.55 | 5.28907 | 🟠 very high — domain-specific | 0.002287 | offering, offerings | ~ |
| 32 | **bodhisattva** | 99 | 16,453.11 | 9.59 | 🟠 very high — domain-specific | 0.001569 | bodhisattva, bodhisattvas | ✓ བྱང་ཆུབ་སེམས་དཔའ |
| 33 | **whatever** | 132 | 16,260.33 | 7.108229 | 🟠 very high — domain-specific | - | - | — |
| 34 | **wisdom** | 109 | 16,045.73 | 8.494523 | 🟠 very high — domain-specific | 0.002631 | wisdom, wisdoms | ✓ ཤེས་རབ |
| 35 | **hundred** | 124 | 16,015.88 | 7.453069 | 🟠 very high — domain-specific | 0.015393 | hundred, hundreds | ~ |
| 36 | **friend** | 96 | 15,959.74 | 9.593135 | 🟠 very high — domain-specific | 0.005832 | friend, friends | ~ |
| 37 | **god** | 96 | 15,959.74 | 9.593135 | 🟠 very high — domain-specific | 0.004406 | god, gods | — |
| 38 | **mother** | 96 | 15,954.53 | 9.59 | 🟠 very high — domain-specific | 0.003439 | mother, mothers | ~ |
| 39 | **thought** | 152 | 15,866.97 | 6.023602 | 🟠 very high — domain-specific | 0.004203 | thought, thoughts | ✓ རྣམ་རྟོག |
| 40 | **perfect** | 97 | 15,444.41 | 9.18767 | 🟠 very high — domain-specific | 0.003425 | perfect, perfects | — |
| 41 | **way** | 184 | 15,193.52 | 4.764821 | 🟠 very high — domain-specific | - | way, ways | ~ |
| 42 | **come** | 178 | 15,120.58 | 4.901787 | 🟠 very high — domain-specific | - | come, comes | ~ |
| 43 | **faith** | 108 | 14,942.45 | 7.983697 | 🟠 very high — domain-specific | 0.002993 | - | — |
| 44 | **make** | 211 | 14,759.13 | 4.036307 | 🟠 very high — domain-specific | 0.004374 | make, makes | — |
| 45 | **live** | 134 | 14,666.97 | 6.31599 | 🟠 very high — domain-specific | 0.006374 | live, lives | — |
| 46 | **disciple** | 86 | 14,292.60 | 9.59 | 🟠 very high — domain-specific | 0.006740 | disciple, disciples | ~ |
| 47 | **once** | 140 | 14,235.44 | 5.867442 | 🟠 very high — domain-specific | - | - | ~ |
| 48 | **say** | 185 | 14,010.55 | 4.37008 | 🟠 very high — domain-specific | - | say, says | — |
| 49 | **instruction** | 83 | 13,798.53 | 9.593135 | 🟠 very high — domain-specific | 0.005127 | instruction, instructions | — |
| 50 | **monk** | 82 | 13,627.82 | 9.59 | 🟠 very high — domain-specific | - | monk, monks | — |
| 51 | **human** | 98 | 13,397.02 | 7.888387 | 🟠 very high — domain-specific | 0.003668 | human, humans | — |
| 52 | **thing** | 113 | 13,180.98 | 6.730934 | 🟠 very high — domain-specific | 0.003745 | thing, things | — |
| 53 | **samsara** | 79 | 13,129.25 | 9.59 | 🟠 very high — domain-specific | 0.004772 | - | ✓ འཁོར་བ |
| 54 | **happiness** | 77 | 12,796.86 | 9.59 | 🟠 very high — domain-specific | 0.005017 | - | — |
| 55 | **reborn** | 75 | 12,464.47 | 9.59 | 🟠 very high — domain-specific | 0.005302 | - | — |
| 56 | **evil** | 74 | 12,302.30 | 9.593135 | 🟠 very high — domain-specific | 0.006005 | evil, evils | — |
| 57 | **day** | 164 | 12,234.83 | 4.304868 | 🟠 very high — domain-specific | 0.002019 | day, days | — |
| 58 | **everything** | 96 | 12,214.35 | 7.341843 | 🟠 very high — domain-specific | - | - | — |
| 59 | **heart** | 99 | 11,993.17 | 6.990446 | 🟠 very high — domain-specific | 0.003583 | heart, hearts | — |
| 60 | **themselve** | 72 | 11,965.89 | 9.59 | 🟠 very high — domain-specific | - | - | — |
| 61 | **thousand** | 96 | 11,896.50 | 7.150788 | 🟠 very high — domain-specific | 0.004223 | thousand, thousands | ~ |
| 62 | **deity** | 71 | 11,799.70 | 9.59 | 🟠 very high — domain-specific | 0.008871 | deities, deity | ✓ ལྷ |
| 63 | **many** | 146 | 11,654.17 | 4.60611 | 🟠 very high — domain-specific | - | - | — |
| 64 | **kalpa** | 70 | 11,633.51 | 9.59 | 🟠 very high — domain-specific | 0.005390 | kalpa, kalpas | ✓ བསྐལ་པ |
| 65 | **wealth** | 76 | 11,427.98 | 8.676844 | 🟠 very high — domain-specific | 0.005259 | - | ~ |
| 66 | **hand** | 103 | 11,413.93 | 6.394462 | 🟠 very high — domain-specific | 0.005193 | hand, hands | — |
| 67 | **place** | 128 | 11,398.95 | 5.138788 | 🟠 very high — domain-specific | 0.002708 | place, places | — |
| 68 | **meditate** | 68 | 11,301.12 | 9.59 | 🟠 very high — domain-specific | 0.006176 | meditate, meditates | ~ |
| 69 | **meditation** | 68 | 11,301.12 | 9.59 | 🟠 very high — domain-specific | 0.006592 | meditation, meditations | ~ |
| 70 | **take** | 166 | 11,261.53 | 3.914671 | 🟠 very high — domain-specific | 0.002786 | take, takes | — |
| 71 | **prayer** | 67 | 11,138.57 | 9.593135 | 🟠 very high — domain-specific | 0.009960 | prayer, prayers | — |
| 72 | **past** | 138 | 11,048.46 | 4.619856 | 🟠 very high — domain-specific | 0.001969 | - | — |
| 73 | **lama** | 66 | 10,972.32 | 9.593135 | 🟠 very high — domain-specific | 0.007993 | lama, lamas | ✓ བླ་མ |
| 74 | **spiritual** | 66 | 10,968.74 | 9.59 | 🟠 very high — domain-specific | 0.006315 | - | ~ |
| 75 | **vajra** | 66 | 10,968.74 | 9.59 | 🟠 very high — domain-specific | 0.003303 | vajra, vajras | ✓ རྡོ་རྗེ |
| 76 | **master** | 77 | 10,653.42 | 7.983697 | 🟠 very high — domain-specific | 0.002529 | master, masters | ~ |
| 77 | **mantra** | 63 | 10,470.16 | 9.59 | 🟠 very high — domain-specific | 0.005553 | mantra, mantras | ✓ སྔགས |
| 78 | **vow** | 63 | 10,470.16 | 9.59 | 🟠 very high — domain-specific | 0.010677 | vow, vows | — |
| 79 | **having** | 107 | 10,443.96 | 5.632322 | 🟠 very high — domain-specific | - | - | — |
| 80 | **effect** | 127 | 10,333.82 | 4.695295 | 🟠 very high — domain-specific | 0.003358 | effect, effects | ~ |
| 81 | **die** | 67 | 10,333.76 | 8.899988 | 🟠 very high — domain-specific | 0.006037 | - | — |
| 82 | **buddhahood** | 62 | 10,303.97 | 9.59 | 🟠 very high — domain-specific | 0.002039 | - | — |
| 83 | **recite** | 62 | 10,303.97 | 9.59 | 🟠 very high — domain-specific | 0.007511 | recite, recites | — |
| 84 | **again** | 116 | 10,183.83 | 5.065927 | 🟠 very high — domain-specific | - | - | — |
| 85 | **love** | 66 | 10,179.52 | 8.899988 | 🟠 very high — domain-specific | 0.006964 | love, loves | — |
| 86 | **born** | 61 | 10,141.09 | 9.593135 | 🟠 very high — domain-specific | - | - | ~ |
| 87 | **perfection** | 61 | 10,137.77 | 9.59 | 🟠 very high — domain-specific | 0.006423 | perfection, perfections | ~ |
| 88 | **demon** | 61 | 10,137.77 | 9.59 | 🟠 very high — domain-specific | 0.011396 | demon, demons | ✓ བདུད |
| 89 | **pure** | 72 | 10,093.10 | 8.089058 | 🟠 very high — domain-specific | 0.005607 | - | ~ |
| 90 | **always** | 89 | 10,063.99 | 6.525082 | 🟠 very high — domain-specific | - | - | — |
| 91 | **mila** | 60 | 9,974.84 | 9.593135 | 🟡 high — specialist register | 0.002356 | - | ~ |
| 92 | **man** | 77 | 9,945.35 | 7.453069 | 🟡 high — specialist register | 0.009341 | man, men | — |
| 93 | **taking** | 111 | 9,862.79 | 5.127227 | 🟡 high — specialist register | - | - | — |
| 94 | **flesh** | 59 | 9,808.59 | 9.593135 | 🟡 high — specialist register | 0.007907 | - | — |
| 95 | **other** | 178 | 9,798.28 | 3.176403 | 🟡 high — specialist register | - | - | — |
| 96 | **feel** | 90 | 9,793.18 | 6.278949 | 🟡 high — specialist register | 0.004768 | feel, feels | — |
| 97 | **power** | 107 | 9,782.58 | 5.275647 | 🟡 high — specialist register | 0.003576 | power, powers | — |
| 98 | **head** | 102 | 9,647.73 | 5.457969 | 🟡 high — specialist register | 0.003943 | head, heads | — |
| 99 | **see** | 119 | 9,644.75 | 4.676811 | 🟡 high — specialist register | - | see, sees | — |
| 100 | **liberation** | 58 | 9,642.34 | 9.593135 | 🟡 high — specialist register | 0.007739 | - | ✓ ཐར་པ |
| 101 | **animal** | 79 | 9,621.98 | 7.028186 | 🟡 high — specialist register | 0.009116 | animal, animals | — |
| 102 | **get** | 111 | 9,604.54 | 4.992978 | 🟡 high — specialist register | - | get, gets | — |
| 103 | **called** | 116 | 9,507.43 | 4.729454 | 🟡 high — specialist register | - | - | — |
| 104 | **enemy** | 63 | 9,473.19 | 8.676844 | 🟡 high — specialist register | 0.009551 | enemies, enemy | — |
| 105 | **kind** | 86 | 9,441.52 | 6.335039 | 🟡 high — specialist register | 0.008009 | kind, kinds | — |
| 106 | **food** | 107 | 9,354.04 | 5.044535 | 🟡 high — specialist register | 0.003186 | food, foods | — |
| 107 | **wrong** | 71 | 9,324.39 | 7.578232 | 🟡 high — specialist register | 0.005832 | - | ~ |
| 108 | **too** | 109 | 9,303.06 | 4.92499 | 🟡 high — specialist register | - | - | — |
| 109 | **blessing** | 58 | 9,234.80 | 9.18767 | 🟡 high — specialist register | 0.009812 | blessing, blessings | — |
| 110 | **visualize** | 55 | 9,143.60 | 9.593135 | 🟡 high — specialist register | 0.008891 | - | — |
| 111 | **transference** | 55 | 9,140.61 | 9.59 | 🟡 high — specialist register | 0.008558 | - | ✓ འཕོ་བ |
| 112 | **realization** | 64 | 9,102.28 | 8.206841 | 🟡 high — specialist register | 0.006987 | realization, realizations | — |
| 113 | **right** | 102 | 9,093.84 | 5.144619 | 🟡 high — specialist register | - | - | — |
| 114 | **positive** | 91 | 9,090.69 | 5.764494 | 🟡 high — specialist register | 0.003805 | - | ~ |
| 115 | **moment** | 84 | 9,088.30 | 6.243231 | 🟡 high — specialist register | 0.004593 | moment, moments | ~ |
| 116 | **himself** | 67 | 9,058.16 | 7.801376 | 🟡 high — specialist register | - | - | — |
| 117 | **water** | 87 | 9,019.36 | 5.982217 | 🟡 high — specialist register | 0.004500 | water, waters | ~ |
| 118 | **nothing** | 86 | 8,956.52 | 6.009616 | 🟡 high — specialist register | - | - | — |
| 119 | **mean** | 88 | 8,929.73 | 5.855466 | 🟡 high — specialist register | 0.008328 | mean, means | — |
| 120 | **tantra** | 53 | 8,808.23 | 9.59 | 🟡 high — specialist register | 0.009426 | tantra, tantras | ✓ རྒྱུད |
| 121 | **obscuration** | 53 | 8,808.23 | 9.59 | 🟡 high — specialist register | - | - | — |
| 122 | **think** | 103 | 8,799.37 | 4.929696 | 🟡 high — specialist register | 0.002818 | think, thinks | — |
| 123 | **single** | 84 | 8,748.23 | 6.009616 | 🟡 high — specialist register | 0.004387 | - | — |
| 124 | **true** | 72 | 8,722.31 | 6.990446 | 🟡 high — specialist register | 0.005381 | - | ~ |
| 125 | **harm** | 69 | 8,659.39 | 7.24176 | 🟡 high — specialist register | 0.006225 | harm, harms | — |
| 126 | **quality** | 86 | 8,640.61 | 5.797646 | 🟡 high — specialist register | 0.003845 | qualities, quality | — |
| 127 | **bring** | 93 | 8,568.41 | 5.316469 | 🟡 high — specialist register | 0.005425 | bring, brings | — |
| 128 | **ordinary** | 84 | 8,558.91 | 5.879563 | 🟡 high — specialist register | 0.004252 | - | ~ |
| 129 | **benefit** | 89 | 8,546.72 | 5.54135 | 🟡 high — specialist register | 0.005053 | benefit, benefits | — |
| 130 | **every** | 84 | 8,439.66 | 5.797646 | 🟡 high — specialist register | - | - | — |
| 131 | **follow** | 80 | 8,390.65 | 6.052176 | 🟡 high — specialist register | 0.005941 | follow, follows | — |
| 132 | **father** | 54 | 8,328.70 | 8.899988 | 🟡 high — specialist register | 0.009656 | father, fathers | — |
| 133 | **essence** | 50 | 8,312.37 | 9.593135 | 🟡 high — specialist register | 0.009694 | essence, essences | ✓ ཐིག་ལེ |
| 134 | **sutra** | 50 | 8,309.65 | 9.59 | 🟡 high — specialist register | 0.006830 | sutra, sutras | ✓ མདོ |
| 135 | **jetsun** | 50 | 8,309.65 | 9.59 | 🟡 high — specialist register | 0.003646 | - | ~ |
| 136 | **accomplishment** | 52 | 8,279.48 | 9.18767 | 🟡 high — specialist register | 0.015271 | accomplishment, accomplishments | ✓ དངོས་གྲུབ |
| 137 | **state** | 110 | 8,154.06 | 4.277469 | 🟡 high — specialist register | 0.003281 | state, states | ~ |
| 138 | **secret** | 61 | 8,011.09 | 7.578232 | 🟡 high — specialist register | 0.002884 | secret, secrets | ~ |
| 139 | **down** | 121 | 8,007.22 | 3.818584 | 🟡 high — specialist register | - | down, downs | — |
| 140 | **cannot** | 84 | 8,004.62 | 5.498791 | 🟡 high — specialist register | - | - | — |
| 141 | **rebirth** | 48 | 7,977.26 | 9.59 | 🟡 high — specialist register | 0.014238 | rebirth, rebirths | — |
| 142 | **samaya** | 48 | 7,977.26 | 9.59 | 🟡 high — specialist register | 0.031117 | samaya, samayas | ✓ དམ་ཚིག |
| 143 | **preta** | 48 | 7,977.26 | 9.59 | 🟡 high — specialist register | 0.015646 | preta, pretas | ✓ ཡི་དྭགས |
| 144 | **profound** | 50 | 7,961.03 | 9.18767 | 🟡 high — specialist register | 0.010226 | - | ~ |
| 145 | **know** | 78 | 7,898.99 | 5.843631 | 🟡 high — specialist register | 0.061401 | know, knows | — |
| 146 | **harmful** | 57 | 7,886.29 | 7.983697 | 🟡 high — specialist register | 0.008334 | - | — |
| 147 | **away** | 78 | 7,852.10 | 5.808946 | 🟡 high — specialist register | - | - | — |
| 148 | **lineage** | 47 | 7,811.07 | 9.59 | 🟡 high — specialist register | 0.011716 | lineage, lineages | ~ |
| 149 | **whole** | 78 | 7,748.64 | 5.732405 | 🟡 high — specialist register | - | - | — |
| 150 | **become** | 89 | 7,700.94 | 4.992978 | 🟡 high — specialist register | - | become, becomes | — |
| 151 | **someone** | 60 | 7,690.19 | 7.395911 | 🟡 high — specialist register | - | - | — |
| 152 | **tibet** | 46 | 7,644.88 | 9.59 | 🟡 high — specialist register | 0.003430 | - | — |
| 153 | **empowerment** | 46 | 7,644.88 | 9.59 | 🟡 high — specialist register | 0.019056 | empowerment, empowerments | ✓ དབང་བསྐུར |
| 154 | **protector** | 46 | 7,644.88 | 9.59 | 🟡 high — specialist register | 0.017176 | protector, protectors | ~ |
| 155 | **mandala** | 46 | 7,644.88 | 9.59 | 🟡 high — specialist register | 0.011530 | mandala, mandalas | ✓ དཀྱིལ་འཁོར |
| 156 | **put** | 94 | 7,571.49 | 4.647928 | 🟡 high — specialist register | 0.047600 | put, puts | — |
| 157 | **child** | 49 | 7,557.52 | 8.899988 | 🟡 high — specialist register | 0.026889 | child, children | — |
| 158 | **root** | 55 | 7,518.74 | 7.888387 | 🟡 high — specialist register | 0.008647 | root, roots | ~ |
| 159 | **therefore** | 69 | 7,444.59 | 6.225839 | 🟡 high — specialist register | - | - | — |
| 160 | **experience** | 63 | 7,412.93 | 6.789775 | 🟡 high — specialist register | 0.008972 | experience, experiences | ~ |
| 161 | **taught** | 48 | 7,403.29 | 8.899988 | 🟡 high — specialist register | - | - | — |
| 162 | **act** | 80 | 7,390.07 | 5.330455 | 🟡 high — specialist register | 0.009438 | act, acts | — |
| 163 | **doing** | 69 | 7,384.29 | 6.175409 | 🟡 high — specialist register | - | - | — |
| 164 | **give** | 91 | 7,313.10 | 4.637308 | 🟡 high — specialist register | 0.008624 | give, gives | — |
| 165 | **devotion** | 44 | 7,312.49 | 9.59 | 🟡 high — specialist register | 0.012503 | devotion, devotions | — |
| 166 | **ever** | 64 | 7,289.85 | 6.57271 | 🟡 high — specialist register | - | - | — |
| 167 | **off** | 96 | 7,270.34 | 4.37008 | 🟡 high — specialist register | - | - | — |
| 168 | **old** | 69 | 7,202.77 | 6.023602 | 🟡 high — specialist register | - | - | — |
| 169 | **nature** | 59 | 7,186.04 | 7.028186 | 🟡 high — specialist register | 0.007632 | nature, natures | ~ |
| 170 | **blood** | 51 | 7,149.28 | 8.089058 | 🟡 high — specialist register | 0.009414 | - | — |
| 171 | **practising** | 43 | 7,148.63 | 9.593135 | 🟡 high — specialist register | - | - | — |
| 172 | **teach** | 43 | 7,148.63 | 9.593135 | 🟡 high — specialist register | 0.001889 | teach, teaches | — |
| 173 | **guru** | 43 | 7,146.30 | 9.59 | 🟡 high — specialist register | 0.004289 | - | ~ |
| 174 | **precious** | 56 | 7,125.04 | 7.341843 | 🟡 high — specialist register | 0.005355 | - | ~ |
| 175 | **eye** | 52 | 7,108.63 | 7.888387 | 🟡 high — specialist register | 0.011038 | eye, eyes | — |
| 176 | **spirit** | 58 | 7,103.66 | 7.067407 | 🟡 high — specialist register | 0.009555 | spirit, spirits | — |
| 177 | **son** | 46 | 7,094.82 | 8.899988 | 🟡 high — specialist register | 0.014079 | son, sons | — |
| 178 | **find** | 75 | 7,083.56 | 5.45 | 🟡 high — specialist register | 0.005444 | find, finds | — |
| 179 | **attain** | 51 | 7,056.16 | 7.983697 | 🟡 high — specialist register | 0.009875 | - | — |
| 180 | **meaning** | 54 | 7,031.39 | 7.513694 | 🟡 high — specialist register | - | - | ~ |
| 181 | **transcendent** | 42 | 6,980.11 | 9.59 | 🟡 high — specialist register | 0.009917 | - | ~ |
| 182 | **world** | 103 | 6,966.34 | 3.902776 | 🟡 high — specialist register | 0.005940 | world, worlds | ~ |
| 183 | **until** | 92 | 6,941.83 | 4.354037 | 🟡 high — specialist register | - | - | — |
| 184 | **look** | 70 | 6,903.88 | 5.691163 | 🟡 high — specialist register | 0.108107 | look, looks | — |
| 185 | **asked** | 90 | 6,897.94 | 4.422651 | 🟡 high — specialist register | - | - | — |
| 186 | **method** | 58 | 6,855.53 | 6.820546 | 🟡 high — specialist register | 0.009605 | method, methods | — |
| 187 | **sky** | 41 | 6,816.14 | 9.593135 | 🟡 high — specialist register | 0.013473 | skies, sky | — |
| 188 | **authentic** | 41 | 6,813.91 | 9.59 | 🟡 high — specialist register | 0.013536 | - | — |
| 189 | **killing** | 44 | 6,786.35 | 8.899988 | 🟡 high — specialist register | - | - | — |
| 190 | **tree** | 48 | 6,728.73 | 8.089058 | 🟡 high — specialist register | 0.012763 | tree, trees | ~ |
| 191 | **form** | 75 | 6,686.65 | 5.144619 | 🟡 high — specialist register | 0.007101 | form, forms | — |
| 192 | **wish** | 54 | 6,651.95 | 7.108229 | 🟡 high — specialist register | 0.055369 | wish, wishes | ~ |
| 193 | **wheel** | 40 | 6,649.89 | 9.593135 | 🟡 high — specialist register | 0.012437 | wheel, wheels | ✓ འཁོར་ལོ |
| 194 | **sublime** | 40 | 6,647.72 | 9.59 | 🟡 high — specialist register | 0.011347 | - | ~ |
| 195 | **end** | 104 | 6,646.48 | 3.687773 | 🟡 high — specialist register | 0.003186 | end, ends | — |
| 196 | **speech** | 64 | 6,634.93 | 5.982217 | 🟡 high — specialist register | 0.006963 | - | ~ |
| 197 | **freedom** | 54 | 6,577.05 | 7.028186 | 🟡 high — specialist register | 0.014596 | freedom, freedoms | — |
| 198 | **nectar** | 39 | 6,481.53 | 9.59 | 🟡 high — specialist register | 0.014724 | - | — |
| 199 | **replied** | 56 | 6,452.36 | 6.648696 | 🟡 high — specialist register | - | - | — |
| 200 | **best** | 68 | 6,431.82 | 5.457969 | 🟡 high — specialist register | - | - | — |
| 201 | **anything** | 61 | 6,413.30 | 6.066775 | 🟡 high — specialist register | - | - | — |
| 202 | **point** | 78 | 6,398.16 | 4.733323 | 🟡 high — specialist register | 0.007179 | point, points | ~ |
| 203 | **free** | 71 | 6,337.24 | 5.150484 | 🟡 high — specialist register | 0.005904 | - | ~ |
| 204 | **eat** | 43 | 6,329.97 | 8.494523 | 🟡 high — specialist register | 0.013319 | eat, eats | — |
| 205 | **myself** | 38 | 6,317.40 | 9.593135 | 🟡 high — specialist register | - | - | — |
| 206 | **joy** | 38 | 6,317.40 | 9.593135 | 🟡 high — specialist register | 0.012436 | joy, joys | ~ |
| 207 | **emptiness** | 38 | 6,315.33 | 9.59 | 🟡 high — specialist register | 0.014395 | - | ✓ སྟོང་པ་ཉིད |
| 208 | **daughter** | 38 | 6,315.33 | 9.59 | 🟡 high — specialist register | 0.010625 | daughter, daughters | — |
| 209 | **view** | 67 | 6,256.51 | 5.388443 | 🟡 high — specialist register | 0.012126 | view, views | ✓ ལྟ་བ |
| 210 | **fault** | 45 | 6,226.02 | 7.983697 | 🟡 high — specialist register | 0.021545 | fault, faults | — |
| 211 | **while** | 98 | 6,199.45 | 3.650336 | 🟡 high — specialist register | - | - | — |
| 212 | **vehicle** | 49 | 6,190.85 | 7.29055 | 🟡 high — specialist register | 0.007987 | vehicle, vehicles | ✓ ཐེག་པ |
| 213 | **because** | 99 | 6,177.07 | 3.600421 | 🟡 high — specialist register | - | - | — |
| 214 | **lord** | 47 | 6,172.48 | 7.578232 | 🟡 high — specialist register | 0.003741 | lord, lords | ~ |
| 215 | **possession** | 37 | 6,149.14 | 9.59 | 🟡 high — specialist register | 0.019133 | possession, possessions | — |
| 216 | **killed** | 51 | 6,146.16 | 6.954078 | 🟡 high — specialist register | - | - | — |
| 217 | **want** | 69 | 6,103.74 | 5.104499 | 🟡 high — specialist register | 0.182370 | want, wants | — |
| 218 | **left** | 64 | 6,080.42 | 5.482261 | 🟡 high — specialist register | - | - | — |
| 219 | **text** | 42 | 6,070.56 | 8.340372 | 🟡 high — specialist register | 0.025275 | text, texts | — |
| 220 | **went** | 61 | 6,059.83 | 5.732405 | 🟡 high — specialist register | - | - | — |
| 221 | **pain** | 40 | 6,014.73 | 8.676844 | 🟡 high — specialist register | 0.014714 | pain, pains | — |
| 222 | **suffer** | 50 | 5,995.24 | 6.918987 | 🟡 high — specialist register | 0.001467 | suffer, suffers | — |
| 223 | **attachment** | 36 | 5,984.90 | 9.593135 | 🟡 high — specialist register | 0.016816 | attachment, attachments | — |
| 224 | **together** | 61 | 5,984.68 | 5.66131 | 🟡 high — specialist register | - | - | — |
| 225 | **impermanence** | 36 | 5,982.95 | 9.59 | 🟡 high — specialist register | 0.014714 | - | — |
| 226 | **oddiyana** | 36 | 5,982.95 | 9.59 | 🟡 high — specialist register | 0.005205 | - | ✓ ཨོ་རྒྱན |
| 227 | **innumerable** | 36 | 5,982.95 | 9.59 | 🟡 high — specialist register | 0.016298 | - | — |
| 228 | **yoga** | 36 | 5,982.95 | 9.59 | 🟡 high — specialist register | 0.008115 | yoga, yogas | ~ |
| 229 | **came** | 64 | 5,976.37 | 5.388443 | 🟡 high — specialist register | - | - | — |
| 230 | **much** | 80 | 5,964.71 | 4.302346 | 🟡 high — specialist register | - | - | — |
| 231 | **really** | 56 | 5,946.46 | 6.127399 | 🟡 high — specialist register | - | - | — |
| 232 | **noble** | 37 | 5,891.17 | 9.18767 | 🟡 high — specialist register | 0.012060 | - | ~ |
| 233 | **anyone** | 44 | 5,831.10 | 7.647225 | 🟡 high — specialist register | - | - | — |
| 234 | **vajrasattva** | 35 | 5,816.75 | 9.59 | 🟡 high — specialist register | 0.005716 | vajrasattva, vajrasattvas | ✓ རྡོ་རྗེ་སེམས་དཔའ |
| 235 | **birth** | 35 | 5,816.75 | 9.59 | 🟡 high — specialist register | 0.016746 | - | — |
| 236 | **naropa** | 35 | 5,816.75 | 9.59 | 🟡 high — specialist register | 0.006602 | - | ✓ ནཱ་རོ་པ |
| 237 | **present** | 69 | 5,802.49 | 4.85256 | 🟡 high — specialist register | 0.006152 | - | — |
| 238 | **light** | 61 | 5,769.72 | 5.457969 | 🟡 high — specialist register | 0.006719 | light, lights | ~ |
| 239 | **concentration** | 39 | 5,741.13 | 8.494523 | 🟡 high — specialist register | 0.014655 | concentration, concentrations | ✓ བསམ་གཏན |
| 240 | **advantage** | 52 | 5,726.32 | 6.354457 | 🟡 high — specialist register | 0.011176 | advantage, advantages | — |
| 241 | **supreme** | 46 | 5,700.41 | 7.150788 | 🟡 high — specialist register | 0.010038 | - | ~ |
| 242 | **cause** | 60 | 5,700.40 | 5.482261 | 🟡 high — specialist register | 0.051129 | - | ~ |
| 243 | **lower** | 84 | 5,688.69 | 3.907856 | 🟡 high — specialist register | 0.004263 | - | ~ |
| 244 | **effort** | 59 | 5,674.74 | 5.550084 | 🟡 high — specialist register | 0.011153 | effort, efforts | — |
| 245 | **prostration** | 34 | 5,650.56 | 9.59 | 🟡 high — specialist register | 0.017677 | prostration, prostrations | ✓ ཕྱག་འཚལ་བ |
| 246 | **rinpoche** | 34 | 5,650.56 | 9.59 | 🟡 high — specialist register | 0.005697 | - | ~ |
| 247 | **worldly** | 34 | 5,650.56 | 9.59 | 🟡 high — specialist register | 0.016758 | - | ~ |
| 248 | **said** | 222 | 5,631.61 | 1.463813 | 🟡 high — specialist register | - | - | — |
| 249 | **living** | 49 | 5,623.76 | 6.622721 | 🟡 high — specialist register | - | - | — |
| 250 | **done** | 57 | 5,621.73 | 5.691163 | 🟡 high — specialist register | - | - | — |
| 251 | **thinking** | 43 | 5,599.07 | 7.513694 | 🟡 high — specialist register | - | - | — |
| 252 | **imagine** | 36 | 5,552.47 | 8.899988 | 🟡 high — specialist register | 0.016814 | imagine, imagines | — |
| 253 | **giving** | 56 | 5,542.91 | 5.711571 | 🟡 high — specialist register | - | - | — |
| 254 | **rich** | 42 | 5,515.84 | 7.578232 | 🟡 high — specialist register | 0.016753 | rich, riches | — |
| 255 | **doctrine** | 33 | 5,486.16 | 9.593135 | 🟡 high — specialist register | 0.020201 | doctrine, doctrines | — |
| 256 | **emotion** | 33 | 5,484.37 | 9.59 | 🟡 high — specialist register | 0.020815 | emotion, emotions | — |
| 257 | **moon** | 33 | 5,484.37 | 9.59 | 🟡 high — specialist register | 0.014089 | - | — |
| 258 | **deed** | 33 | 5,484.37 | 9.59 | 🟡 high — specialist register | 0.025390 | deed, deeds | — |
| 259 | **atisa** | 33 | 5,484.37 | 9.59 | 🟡 high — specialist register | 0.006960 | - | — |
| 260 | **hatred** | 33 | 5,484.37 | 9.59 | 🟡 high — specialist register | - | - | — |
| 261 | **confess** | 33 | 5,484.37 | 9.59 | 🟡 high — specialist register | 0.018582 | - | — |
| 262 | **going** | 61 | 5,463.50 | 5.168289 | 🟡 high — specialist register | - | - | — |
| 263 | **perfectly** | 38 | 5,404.48 | 8.206841 | 🟡 high — specialist register | 0.013666 | - | — |
| 264 | **kill** | 38 | 5,404.48 | 8.206841 | 🟡 high — specialist register | 0.009683 | kill, kills | — |
| 265 | **use** | 66 | 5,361.83 | 4.68786 | 🟡 high — specialist register | - | use, uses | — |
| 266 | **instead** | 55 | 5,341.54 | 5.604151 | 🟡 high — specialist register | - | - | — |
| 267 | **consciousness** | 32 | 5,319.91 | 9.593135 | 🟡 high — specialist register | 0.020347 | consciousness, consciousnesses | — |
| 268 | **geshe** | 32 | 5,318.18 | 9.59 | 🟡 high — specialist register | 0.007867 | - | ✓ དགེ་བཤེས |
| 269 | **powerful** | 42 | 5,306.44 | 7.29055 | 🟡 high — specialist register | 0.012428 | - | — |
| 270 | **vast** | 40 | 5,301.00 | 7.647225 | 🟡 high — specialist register | 0.010459 | - | — |
| 271 | **important** | 56 | 5,296.80 | 5.457969 | 🟡 high — specialist register | 0.008523 | - | — |
| 272 | **instant** | 33 | 5,254.28 | 9.18767 | 🟡 high — specialist register | 0.019112 | instant, instants | — |
| 273 | **ten** | 49 | 5,230.11 | 6.159148 | 🟡 high — specialist register | 0.253065 | ten, tens | ~ |
| 274 | **don** | 40 | 5,208.44 | 7.513694 | 🟡 high — specialist register | - | - | — |
| 275 | **accumulation** | 36 | 5,203.34 | 8.340372 | 🟡 high — specialist register | 0.031204 | accumulation, accumulations | — |
| 276 | **dedicate** | 31 | 5,153.67 | 9.593135 | 🟡 high — specialist register | 0.018971 | - | — |
| 277 | **conqueror** | 31 | 5,151.98 | 9.59 | 🟡 high — specialist register | 0.014091 | conqueror, conquerors | ✓ རྒྱལ་བ |
| 278 | **woman** | 31 | 5,151.98 | 9.59 | 🟡 high — specialist register | 0.031718 | woman, women | — |
| 279 | **brahmin** | 31 | 5,151.98 | 9.59 | 🟡 high — specialist register | 0.025005 | brahmin, brahmins | ✓ བྲམ་ཟེ |
| 280 | **whether** | 64 | 5,151.12 | 4.644375 | 🟡 high — specialist register | - | - | — |
| 281 | **perception** | 39 | 5,121.85 | 7.578232 | 🟡 high — specialist register | 0.025616 | perception, perceptions | ~ |
| 282 | **listen** | 34 | 5,112.52 | 8.676844 | 🟡 high — specialist register | 0.013656 | - | — |
| 283 | **activity** | 53 | 5,105.74 | 5.558895 | 🟡 high — specialist register | 0.016868 | activities, activity | ~ |
| 284 | **infinite** | 32 | 5,095.06 | 9.18767 | 🟡 high — specialist register | 0.018027 | - | ~ |
| 285 | **pile** | 33 | 5,089.76 | 8.899988 | 🟡 high — specialist register | 0.024563 | pile, piles | — |
| 286 | **why** | 47 | 5,070.96 | 6.225839 | 🟡 high — specialist register | - | - | — |
| 287 | **sun** | 45 | 5,070.60 | 6.502093 | 🟡 high — specialist register | 0.011250 | sun, suns | — |
| 288 | **need** | 62 | 5,065.09 | 4.714128 | 🟡 high — specialist register | 0.182428 | need, needs | — |
| 289 | **different** | 50 | 5,043.30 | 5.820374 | 🟡 high — specialist register | - | - | — |
| 290 | **fire** | 45 | 5,035.94 | 6.457641 | 🟡 high — specialist register | 0.013418 | fire, fires | — |
| 291 | **toward** | 49 | 5,035.16 | 5.929574 | 🟡 high — specialist register | - | toward, towards | — |
| 292 | **bad** | 47 | 5,029.88 | 6.175409 | 🟡 high — specialist register | 0.010992 | - | — |
| 293 | **flower** | 30 | 4,987.42 | 9.593135 | 🟡 high — specialist register | 0.023753 | flower, flowers | — |
| 294 | **tradition** | 30 | 4,987.42 | 9.593135 | 🟡 high — specialist register | 0.022832 | tradition, traditions | ~ |
| 295 | **marpa** | 30 | 4,985.79 | 9.59 | 🟡 high — specialist register | 0.007002 | - | ✓ ལྷོ་བྲག་མར་པ |
| 296 | **purify** | 30 | 4,985.79 | 9.59 | 🟡 high — specialist register | 0.024450 | purifies, purify | — |
| 297 | **syllable** | 30 | 4,985.79 | 9.59 | 🟡 high — specialist register | 0.022176 | syllable, syllables | — |
| 298 | **generation** | 35 | 4,977.81 | 8.206841 | 🟡 high — specialist register | 0.019343 | generation, generations | ~ |
| 299 | **turn** | 47 | 4,965.71 | 6.096628 | 🟡 high — specialist register | 0.012593 | turn, turns | — |
| 300 | **longer** | 53 | 4,962.99 | 5.40348 | 🟡 high — specialist register | - | - | — |
| 301 | **land** | 49 | 4,962.18 | 5.843631 | 🟡 high — specialist register | 0.009148 | land, lands | ~ |
| 302 | **most** | 70 | 4,949.04 | 4.079706 | 🟡 high — specialist register | - | - | — |
| 303 | **arise** | 32 | 4,935.53 | 8.899988 | 🟡 high — specialist register | 0.016540 | - | — |
| 304 | **appear** | 44 | 4,907.63 | 6.436135 | 🟡 high — specialist register | 0.015622 | appear, appears | — |
| 305 | **outer** | 33 | 4,857.88 | 8.494523 | 🟡 high — specialist register | 0.017520 | - | ~ |
| 306 | **simply** | 44 | 4,830.54 | 6.335039 | 🟡 high — specialist register | 0.012281 | - | — |
| 307 | **desire** | 41 | 4,824.29 | 6.789775 | 🟡 high — specialist register | 0.017616 | desire, desires | — |
| 308 | **sarhsara** | 29 | 4,819.60 | 9.59 | 🟡 high — specialist register | 0.021937 | - | — |
| 309 | **caus** | 29 | 4,819.60 | 9.59 | 🟡 high — specialist register | - | - | — |
| 310 | **recitation** | 29 | 4,819.60 | 9.59 | 🟡 high — specialist register | 0.026832 | recitation, recitations | ~ |
| 311 | **tilopa** | 29 | 4,819.60 | 9.59 | 🟡 high — specialist register | 0.008870 | - | ✓ ཏི་ལོ་པ |
| 312 | **intention** | 45 | 4,790.68 | 6.143148 | 🟡 high — specialist register | 0.014447 | intention, intentions | — |
| 313 | **inner** | 30 | 4,776.62 | 9.18767 | 🟡 high — specialist register | - | - | — |
| 314 | **hear** | 34 | 4,766.19 | 8.089058 | 🟡 high — specialist register | 0.017029 | hear, hears | — |
| 315 | **sure** | 43 | 4,720.76 | 6.335039 | 🟡 high — specialist register | - | - | — |
| 316 | **mountain** | 37 | 4,707.61 | 7.341843 | 🟡 high — specialist register | 0.016759 | mountain, mountains | ~ |
| 317 | **foot** | 37 | 4,707.61 | 7.341843 | 🟡 high — specialist register | 0.027007 | feet, foot | — |
| 318 | **else** | 39 | 4,676.29 | 6.918987 | 🟡 high — specialist register | - | - | — |
| 319 | **enlightenment** | 28 | 4,653.40 | 9.59 | 🟡 high — specialist register | 0.021734 | - | ✓ བྱང་ཆུབ |
| 320 | **dissolve** | 28 | 4,653.40 | 9.59 | 🟡 high — specialist register | 0.043423 | dissolve, dissolves | — |
| 321 | **attained** | 29 | 4,617.40 | 9.18767 | 🟡 high — specialist register | - | - | — |
| 322 | **circumstance** | 29 | 4,617.40 | 9.18767 | 🟡 high — specialist register | 0.023478 | circumstance, circumstances | — |
| 323 | **companion** | 29 | 4,617.40 | 9.18767 | 🟡 high — specialist register | 0.031766 | companion, companions | — |
| 324 | **whenever** | 34 | 4,596.68 | 7.801376 | 🟡 high — specialist register | - | - | — |
| 325 | **red** | 41 | 4,573.02 | 6.436135 | 🟡 high — specialist register | 0.011202 | - | — |
| 326 | **example** | 42 | 4,570.15 | 6.278949 | 🟡 high — specialist register | - | example, examples | — |
| 327 | **completely** | 38 | 4,556.38 | 6.918987 | 🟡 high — specialist register | 0.015133 | - | — |
| 328 | **leave** | 43 | 4,554.48 | 6.111895 | 🟡 high — specialist register | 0.007017 | leave, leaves | — |
| 329 | **everyone** | 35 | 4,520.61 | 7.453069 | 🟡 high — specialist register | - | - | — |
| 330 | **during** | 65 | 4,512.38 | 4.005887 | 🟡 high — specialist register | - | - | — |
| 331 | **universe** | 27 | 4,488.68 | 9.593135 | 🟡 high — specialist register | 0.021814 | - | ~ |
| 332 | **practised** | 27 | 4,488.68 | 9.593135 | 🟡 high — specialist register | - | - | — |
| 333 | **practitioner** | 27 | 4,487.21 | 9.59 | 🟡 high — specialist register | 0.035984 | practitioner, practitioners | ~ |
| 334 | **phas** | 27 | 4,487.21 | 9.59 | 🟡 high — specialist register | - | - | — |
| 335 | **drink** | 31 | 4,480.65 | 8.340372 | 🟡 high — specialist register | 0.019935 | drink, drinks | — |
| 336 | **story** | 34 | 4,465.20 | 7.578232 | 🟡 high — specialist register | 0.026800 | stories, story | — |
| 337 | **patience** | 28 | 4,458.18 | 9.18767 | 🟡 high — specialist register | 0.023240 | - | — |
| 338 | **understand** | 35 | 4,453.15 | 7.341843 | 🟡 high — specialist register | 0.016552 | understand, understands | — |
| 339 | **something** | 40 | 4,432.60 | 6.394462 | 🟡 high — specialist register | - | - | — |
| 340 | **earth** | 30 | 4,416.26 | 8.494523 | 🟡 high — specialist register | 0.020869 | - | — |
| 341 | **front** | 35 | 4,392.44 | 7.24176 | 🟡 high — specialist register | - | - | — |
| 342 | **finally** | 36 | 4,384.70 | 7.028186 | 🟡 high — specialist register | 0.015413 | - | — |
| 343 | **tell** | 37 | 4,373.36 | 6.820546 | 🟡 high — specialist register | 0.009061 | tell, tells | — |
| 344 | **ask** | 41 | 4,353.66 | 6.127399 | 🟡 high — specialist register | 0.004031 | ask, asks | — |
| 345 | **ocean** | 35 | 4,337.27 | 7.150788 | 🟡 high — specialist register | 0.020313 | ocean, oceans | — |
| 346 | **truth** | 26 | 4,322.43 | 9.593135 | 🟡 high — specialist register | 0.027735 | truth, truths | ~ |
| 347 | **meditating** | 26 | 4,321.02 | 9.59 | 🟡 high — specialist register | - | - | — |
| 348 | **ritual** | 26 | 4,321.02 | 9.59 | 🟡 high — specialist register | 0.047544 | ritual, rituals | — |
| 349 | **sheep** | 28 | 4,318.59 | 8.899988 | 🟡 high — specialist register | 0.022770 | - | — |
| 350 | **ground** | 37 | 4,297.83 | 6.702763 | 🟡 high — specialist register | 0.014770 | - | ~ |
| 351 | **element** | 33 | 4,296.96 | 7.513694 | 🟡 high — specialist register | 0.030317 | element, elements | — |
| 352 | **died** | 31 | 4,289.04 | 7.983697 | 🟡 high — specialist register | - | - | — |
| 353 | **sign** | 41 | 4,269.97 | 6.009616 | 🟡 high — specialist register | 0.026770 | sign, signs | ~ |
| 354 | **let** | 39 | 4,268.74 | 6.31599 | 🟡 high — specialist register | 0.125893 | let, lets | — |
| 355 | **making** | 54 | 4,260.69 | 4.552941 | 🟡 high — specialist register | - | - | — |
| 356 | **made** | 68 | 4,242.84 | 3.600421 | 🟡 high — specialist register | - | - | — |
| 357 | **help** | 56 | 4,220.33 | 4.348746 | 🟡 high — specialist register | 0.149113 | help, helps | — |
| 358 | **beginning** | 46 | 4,210.93 | 5.282336 | 🟡 high — specialist register | - | - | ✓ ཡེ |
| 359 | **parent** | 43 | 4,204.24 | 5.641891 | 🟡 high — specialist register | 0.014109 | parent, parents | — |
| 360 | **alone** | 38 | 4,171.83 | 6.335039 | 🟡 high — specialist register | - | - | — |
| 361 | **arousing** | 25 | 4,156.18 | 9.593135 | 🟡 high — specialist register | - | - | — |
| 362 | **karmic** | 25 | 4,154.82 | 9.59 | 🟡 high — specialist register | 0.026576 | - | ~ |
| 363 | **generosity** | 25 | 4,154.82 | 9.59 | 🟡 high — specialist register | 0.027012 | - | ✓ སྦྱིན་པ |
| 364 | **tirthika** | 25 | 4,154.82 | 9.59 | 🟡 high — specialist register | 0.133959 | tirthika, tirthikas | ✓ མུ་སྟེགས་པ |
| 365 | **creature** | 25 | 4,154.82 | 9.59 | 🟡 high — specialist register | 0.034890 | creature, creatures | — |
| 366 | **another** | 56 | 4,139.31 | 4.265259 | 🟡 high — specialist register | - | - | — |
| 367 | **able** | 45 | 4,124.64 | 5.28907 | 🟡 high — specialist register | - | - | — |
| 368 | **seeing** | 31 | 4,108.28 | 7.647225 | 🟡 high — specialist register | - | - | ~ |
| 369 | **family** | 39 | 4,080.72 | 6.037787 | 🟡 high — specialist register | 0.011289 | families, family | — |
| 370 | **result** | 55 | 4,077.03 | 4.277469 | 🟡 high — specialist register | 0.009732 | result, results | — |
| 371 | **depth** | 34 | 4,056.79 | 6.885085 | 🟡 high — specialist register | 0.028599 | depth, depths | — |
| 372 | **realized** | 35 | 4,048.90 | 6.675364 | 🟡 high — specialist register | - | - | — |
| 373 | **start** | 48 | 4,018.55 | 4.830961 | 🟡 high — specialist register | 0.012276 | start, starts | — |
| 374 | **peerless** | 26 | 4,010.12 | 8.899988 | 🟡 high — specialist register | 0.025641 | - | — |
| 375 | **dead** | 31 | 4,003.97 | 7.453069 | 🟡 high — specialist register | 0.020268 | - | — |
| 376 | **develop** | 38 | 3,995.17 | 6.066775 | 🟡 high — specialist register | 0.019079 | develop, develops | — |
| 377 | **arouse** | 24 | 3,988.63 | 9.59 | 🟡 high — specialist register | 0.025049 | - | — |
| 378 | **torment** | 24 | 3,988.63 | 9.59 | 🟡 high — specialist register | 0.035549 | torment, torments | — |
| 379 | **beautiful** | 24 | 3,988.63 | 9.59 | 🟡 high — specialist register | 0.028217 | - | — |
| 380 | **future** | 52 | 3,988.04 | 4.425496 | 🟡 high — specialist register | 0.009554 | - | — |
| 381 | **immense** | 25 | 3,980.52 | 9.18767 | 🟡 high — specialist register | 0.026834 | - | — |
| 382 | **work** | 48 | 3,980.33 | 4.785024 | 🟡 high — specialist register | 0.012414 | work, works | — |
| 383 | **particular** | 38 | 3,976.08 | 6.037787 | 🟡 high — specialist register | - | - | — |
| 384 | **appeared** | 37 | 3,928.91 | 6.127399 | 🟡 high — specialist register | - | - | — |
| 385 | **keep** | 44 | 3,913.97 | 5.132991 | 🟡 high — specialist register | 0.051802 | - | — |
| 386 | **complete** | 41 | 3,878.01 | 5.457969 | 🟡 high — specialist register | 0.012645 | complete, completes | — |
| 387 | **attitude** | 32 | 3,876.58 | 6.990446 | 🟡 high — specialist register | 0.024745 | attitude, attitudes | — |
| 388 | **essential** | 32 | 3,876.58 | 6.990446 | 🟡 high — specialist register | 0.018187 | - | ~ |
| 389 | **stone** | 28 | 3,873.97 | 7.983697 | 🟡 high — specialist register | 0.042975 | stone, stones | — |
| 390 | **feeling** | 30 | 3,845.09 | 7.395911 | 🟡 high — specialist register | 0.090158 | feeling, feelings | — |
| 391 | **absolute** | 28 | 3,827.72 | 7.888387 | 🟡 high — specialist register | 0.021793 | - | ~ |
| 392 | **pleasure** | 23 | 3,823.69 | 9.593135 | 🟡 high — specialist register | 0.048506 | pleasure, pleasures | — |
| 393 | **sleep** | 23 | 3,823.69 | 9.593135 | 🟡 high — specialist register | 0.029802 | - | — |
| 394 | **buddhafield** | 23 | 3,822.44 | 9.59 | 🟡 high — specialist register | 0.016543 | buddhafield, buddhafields | — |
| 395 | **heaven** | 23 | 3,822.44 | 9.59 | 🟡 high — specialist register | 0.022020 | heaven, heavens | ~ |
| 396 | **siddha** | 23 | 3,822.44 | 9.59 | 🟡 high — specialist register | 0.042659 | siddha, siddhas | ✓ གྲུབ་ཐོབ |
| 397 | **dedication** | 23 | 3,822.44 | 9.59 | 🟡 high — specialist register | 0.031656 | dedication, dedications | — |
| 398 | **confession** | 23 | 3,822.44 | 9.59 | 🟡 high — specialist register | 0.022968 | - | — |
| 399 | **piece** | 24 | 3,821.30 | 9.18767 | 🟡 high — specialist register | 0.052179 | piece, pieces | — |
| 400 | **fruit** | 30 | 3,816.98 | 7.341843 | 🟡 high — specialist register | 0.024469 | fruit, fruits | ~ |
| 401 | **difficult** | 41 | 3,812.88 | 5.366301 | 🟡 high — specialist register | 0.013406 | - | — |
| 402 | **space** | 31 | 3,796.78 | 7.067407 | 🟡 high — specialist register | 0.020275 | - | ~ |
| 403 | **object** | 27 | 3,784.91 | 8.089058 | 🟡 high — specialist register | 0.041215 | object, objects | ~ |
| 404 | **face** | 39 | 3,781.41 | 5.594934 | 🟡 high — specialist register | 0.016767 | face, faces | — |
| 405 | **became** | 34 | 3,767.71 | 6.394462 | 🟡 high — specialist register | - | - | — |
| 406 | **palace** | 25 | 3,759.20 | 8.676844 | 🟡 high — specialist register | 0.020211 | palace, palaces | ~ |
| 407 | **perform** | 26 | 3,757.97 | 8.340372 | 🟡 high — specialist register | 0.023935 | - | — |
| 408 | **age** | 26 | 3,757.97 | 8.340372 | 🟡 high — specialist register | 0.026551 | age, ages | ~ |
| 409 | **given** | 48 | 3,755.59 | 4.514841 | 🟡 high — specialist register | - | - | — |
| 410 | **known** | 37 | 3,754.54 | 5.855466 | 🟡 high — specialist register | - | - | — |
| 411 | **lead** | 44 | 3,748.24 | 4.915644 | 🟡 high — specialist register | 0.014612 | lead, leads | — |
| 412 | **found** | 37 | 3,746.96 | 5.843631 | 🟡 high — specialist register | - | - | — |
| 413 | **sometime** | 29 | 3,745.65 | 7.453069 | 🟡 high — specialist register | - | sometime, sometimes | — |
| 414 | **sort** | 31 | 3,735.90 | 6.954078 | 🟡 high — specialist register | 0.029553 | sort, sorts | — |
| 415 | **white** | 40 | 3,730.08 | 5.381008 | 🟡 high — specialist register | 0.014553 | white, whites | ~ |
| 416 | **remember** | 24 | 3,701.64 | 8.899988 | 🟡 high — specialist register | 0.028347 | - | — |
| 417 | **truly** | 24 | 3,701.64 | 8.899988 | 🟡 high — specialist register | - | - | — |
| 418 | **taken** | 44 | 3,696.81 | 4.848203 | 🟡 high — specialist register | - | - | — |
| 419 | **around** | 55 | 3,691.34 | 3.872823 | 🟡 high — specialist register | - | - | — |
| 420 | **clothing** | 28 | 3,677.22 | 7.578232 | 🟡 high — specialist register | 0.024323 | - | — |
| 421 | **beyond** | 33 | 3,668.68 | 6.415081 | 🟡 high — specialist register | - | - | — |
| 422 | **inconceivable** | 23 | 3,662.08 | 9.18767 | 🟡 high — specialist register | 0.029979 | - | — |
| 423 | **bird** | 23 | 3,662.08 | 9.18767 | 🟡 high — specialist register | 0.056882 | bird, birds | — |
| 424 | **stay** | 34 | 3,658.28 | 6.208745 | 🟡 high — specialist register | 0.019294 | stay, stays | — |
| 425 | **kindness** | 22 | 3,657.44 | 9.593135 | 🟡 high — specialist register | 0.031803 | - | — |
| 426 | **skilful** | 22 | 3,656.25 | 9.59 | 🟡 high — specialist register | 0.031629 | - | ~ |
| 427 | **faculty** | 22 | 3,656.25 | 9.59 | 🟡 high — specialist register | - | - | — |
| 428 | **sangha** | 22 | 3,656.25 | 9.59 | 🟡 high — specialist register | 0.012816 | - | ✓ དགེ་འདུན |
| 429 | **slightest** | 22 | 3,656.25 | 9.59 | 🟡 high — specialist register | - | - | — |
| 430 | **karma** | 22 | 3,656.25 | 9.59 | 🟡 high — specialist register | 0.029452 | - | ✓ ལས |
| 431 | **beggar** | 22 | 3,656.25 | 9.59 | 🟡 high — specialist register | 0.043268 | beggar, beggars | — |
| 432 | **happy** | 30 | 3,653.92 | 7.028186 | 🟡 high — specialist register | 0.020960 | - | — |
| 433 | **set** | 53 | 3,652.21 | 3.976364 | 🟡 high — specialist register | 0.009643 | set, sets | — |
| 434 | **must** | 45 | 3,650.03 | 4.68048 | 🟡 high — specialist register | - | - | — |
| 435 | **numerous** | 26 | 3,644.73 | 8.089058 | 🟡 high — specialist register | 0.025249 | - | — |
| 436 | **fact** | 36 | 3,624.05 | 5.808946 | 🟡 high — specialist register | 0.016068 | - | — |
| 437 | **diligence** | 28 | 3,616.49 | 7.453069 | 🟡 high — specialist register | 0.023244 | - | — |
| 438 | **source** | 37 | 3,599.37 | 5.613454 | 🟡 high — specialist register | 0.022493 | source, sources | ~ |
| 439 | **took** | 38 | 3,578.64 | 5.434252 | 🟡 high — specialist register | - | - | — |
| 440 | **avoid** | 35 | 3,573.65 | 5.891833 | 🟡 high — specialist register | 0.015771 | - | — |
| 441 | **happen** | 31 | 3,557.89 | 6.622721 | 🟡 high — specialist register | 0.036582 | happen, happens | — |
| 442 | **guide** | 27 | 3,545.89 | 7.578232 | 🟡 high — specialist register | 0.034420 | guide, guides | — |
| 443 | **hum** | 24 | 3,533.01 | 8.494523 | 🟡 high — specialist register | 0.016186 | - | — |
| 444 | **obstacle** | 24 | 3,533.01 | 8.494523 | 🟡 high — specialist register | 0.045656 | obstacle, obstacles | — |
| 445 | **direction** | 33 | 3,504.16 | 6.127399 | 🟡 high — specialist register | 0.032058 | direction, directions | — |
| 446 | **forth** | 22 | 3,502.85 | 9.18767 | 🟡 high — specialist register | - | - | — |
| 447 | **dust** | 22 | 3,502.85 | 9.18767 | 🟡 high — specialist register | 0.031956 | - | — |
| 448 | **india** | 33 | 3,495.30 | 6.111895 | 🟡 high — specialist register | 0.005850 | - | — |
| 449 | **mental** | 21 | 3,491.19 | 9.593135 | 🟡 high — specialist register | 0.033584 | - | — |
| 450 | **dharmakaya** | 21 | 3,490.05 | 9.59 | 🟡 high — specialist register | 0.033994 | - | ✓ ཆོས་སྐུ |
| 451 | **visualization** | 21 | 3,490.05 | 9.59 | 🟡 high — specialist register | 0.037560 | visualization, visualizations | — |
| 452 | **clothe** | 21 | 3,490.05 | 9.59 | 🟡 high — specialist register | 0.035428 | clothe, clothes | — |
| 453 | **cho** | 21 | 3,490.05 | 9.59 | 🟡 high — specialist register | 0.012481 | - | ✓ གཅོད |
| 454 | **along** | 36 | 3,479.19 | 5.576752 | 🟡 high — specialist register | - | - | — |
| 455 | **ultimate** | 26 | 3,479.04 | 7.721333 | 🟡 high — specialist register | 0.016805 | - | — |
| 456 | **level** | 48 | 3,476.44 | 4.179259 | 🟡 high — specialist register | 0.019930 | level, levels | ~ |
| 457 | **empty** | 24 | 3,468.89 | 8.340372 | 🟡 high — specialist register | - | - | — |
| 458 | **lifetime** | 24 | 3,468.89 | 8.340372 | 🟡 high — specialist register | 0.033975 | lifetime, lifetimes | — |
| 459 | **bear** | 30 | 3,456.62 | 6.648696 | 🟡 high — specialist register | 0.006929 | bear, bears | — |
| 460 | **existence** | 26 | 3,445.65 | 7.647225 | 🟡 high — specialist register | 0.025498 | - | ~ |
| 461 | **lived** | 25 | 3,417.61 | 7.888387 | 🟡 high — specialist register | - | - | — |
| 462 | **training** | 26 | 3,414.56 | 7.578232 | 🟡 high — specialist register | - | - | ~ |
| 463 | **continent** | 24 | 3,413.35 | 8.206841 | 🟡 high — specialist register | 0.033842 | continent, continents | — |
| 464 | **train** | 24 | 3,413.35 | 8.206841 | 🟡 high — specialist register | 0.023907 | train, trains | — |
| 465 | **within** | 43 | 3,407.38 | 4.57255 | 🟡 high — specialist register | - | - | — |
| 466 | **black** | 30 | 3,404.59 | 6.548613 | 🟡 high — specialist register | 0.011003 | - | ~ |
| 467 | **since** | 52 | 3,385.50 | 3.756864 | 🟡 high — specialist register | - | - | — |
| 468 | **learned** | 24 | 3,364.37 | 8.089058 | 🟡 high — specialist register | - | - | — |
| 469 | **throughout** | 32 | 3,356.26 | 6.052176 | 🟡 high — specialist register | - | - | — |
| 470 | **accumulate** | 21 | 3,343.63 | 9.18767 | 🟡 high — specialist register | 0.025488 | accumulate, accumulates | — |
| 471 | **natural** | 38 | 3,339.65 | 5.071347 | 🟡 high — specialist register | 0.014368 | - | ~ |
| 472 | **river** | 31 | 3,335.49 | 6.208745 | 🟡 high — specialist register | 0.019161 | river, rivers | — |
| 473 | **saw** | 34 | 3,329.97 | 5.651553 | 🟡 high — specialist register | - | saw, saws | — |
| 474 | **dream** | 20 | 3,324.95 | 9.593135 | 🟡 high — specialist register | 0.072226 | dream, dreams | — |
| 475 | **dog** | 20 | 3,324.95 | 9.593135 | 🟡 high — specialist register | 0.119583 | dog, dogs | — |
| 476 | **servant** | 20 | 3,324.95 | 9.593135 | 🟡 high — specialist register | 0.064933 | servant, servants | — |
| 477 | **mantrayana** | 20 | 3,323.86 | 9.59 | 🟡 high — specialist register | 0.013427 | - | ~ |
| 478 | **reciting** | 20 | 3,323.86 | 9.59 | 🟡 high — specialist register | - | - | — |
| 479 | **goe** | 20 | 3,323.86 | 9.59 | 🟡 high — specialist register | - | - | — |
| 480 | **dying** | 20 | 3,323.86 | 9.59 | 🟡 high — specialist register | - | - | — |
| 481 | **emanation** | 20 | 3,323.86 | 9.59 | 🟡 high — specialist register | 0.044304 | emanation, emanations | — |
| 482 | **impermanent** | 20 | 3,323.86 | 9.59 | 🟡 high — specialist register | 0.034895 | - | — |
| 483 | **ourselve** | 20 | 3,323.86 | 9.59 | 🟡 high — specialist register | - | - | — |
| 484 | **sadaprarudita** | 20 | 3,323.86 | 9.59 | 🟡 high — specialist register | 0.015007 | - | ✓ རྟག་ཏུ་ངུ |
| 485 | **above** | 42 | 3,295.27 | 4.527381 | 🟡 high — specialist register | - | - | — |
| 486 | **part** | 46 | 3,295.15 | 4.13355 | 🟡 high — specialist register | 0.040999 | part, parts | ~ |
| 487 | **insect** | 23 | 3,271.13 | 8.206841 | 🟡 high — specialist register | 0.041224 | insect, insects | — |
| 488 | **hard** | 34 | 3,270.19 | 5.550084 | 🟡 high — specialist register | 0.017718 | - | — |
| 489 | **better** | 38 | 3,265.28 | 4.958406 | 🟡 high — specialist register | - | - | — |
| 490 | **channel** | 25 | 3,255.27 | 7.513694 | 🟡 high — specialist register | 0.048293 | channel, channels | ✓ རྩ |
| 491 | **matter** | 31 | 3,251.38 | 6.052176 | 🟡 high — specialist register | 0.020052 | - | — |
| 492 | **cold** | 29 | 3,234.57 | 6.436135 | 🟡 high — specialist register | 0.021393 | - | — |
| 493 | **although** | 40 | 3,204.85 | 4.623322 | 🟡 high — specialist register | - | - | — |
| 494 | **intermediate** | 30 | 3,202.11 | 6.159148 | 🟡 high — specialist register | 0.021135 | - | ~ |
| 495 | **real** | 39 | 3,186.10 | 4.714128 | 🟡 high — specialist register | 0.014550 | - | ~ |
| 496 | **small** | 37 | 3,185.60 | 4.968162 | 🟡 high — specialist register | 0.015592 | - | ~ |
| 497 | **constantly** | 20 | 3,184.41 | 9.18767 | 🟡 high — specialist register | 0.035943 | - | — |
| 498 | **concept** | 24 | 3,180.60 | 7.647225 | 🟡 high — specialist register | 0.032692 | concept, concepts | ~ |
| 499 | **filled** | 22 | 3,179.82 | 8.340372 | 🟡 high — specialist register | - | - | — |
| 500 | **determination** | 27 | 3,176.97 | 6.789775 | 🟡 high — specialist register | 0.024144 | - | ~ |
| 501 | **accumulated** | 26 | 3,166.73 | 7.028186 | 🟡 high — specialist register | - | - | — |
| 502 | **kaya** | 19 | 3,158.70 | 9.593135 | 🟡 high — specialist register | 0.048989 | kaya, kayas | ✓ སྐུ |
| 503 | **pot** | 19 | 3,158.70 | 9.593135 | 🟡 high — specialist register | - | pot, pots | — |
| 504 | **received** | 39 | 3,158.41 | 4.673154 | 🟡 high — specialist register | - | - | — |
| 505 | **later** | 40 | 3,158.31 | 4.556183 | 🟡 high — specialist register | - | - | — |
| 506 | **dorje** | 19 | 3,157.67 | 9.59 | 🟡 high — specialist register | 0.014663 | - | ~ |
| 507 | **jowo** | 19 | 3,157.67 | 9.59 | 🟡 high — specialist register | 0.014742 | - | ✓ ཇོ་བོ |
| 508 | **bless** | 19 | 3,157.67 | 9.59 | 🟡 high — specialist register | 0.035531 | - | — |
| 509 | **pray** | 19 | 3,157.67 | 9.59 | 🟡 high — specialist register | 0.038407 | - | — |
| 510 | **purification** | 19 | 3,157.67 | 9.59 | 🟡 high — specialist register | 0.040723 | purification, purifications | — |
| 511 | **ly** | 19 | 3,157.67 | 9.59 | 🟡 high — specialist register | - | - | ~ |
| 512 | **antidote** | 19 | 3,157.67 | 9.59 | 🟡 high — specialist register | 0.052333 | antidote, antidotes | — |
| 513 | **dharmodgata** | 19 | 3,157.67 | 9.59 | 🟡 high — specialist register | 0.014680 | - | ✓ ཆོས་འཕགས |
| 514 | **poison** | 24 | 3,151.91 | 7.578232 | 🟡 high — specialist register | 0.057018 | poison, poisons | — |
| 515 | **suddenly** | 23 | 3,109.52 | 7.801376 | 🟡 high — specialist register | 0.029485 | - | — |
| 516 | **using** | 31 | 3,108.63 | 5.786473 | 🟡 high — specialist register | - | - | — |
| 517 | **respect** | 27 | 3,098.81 | 6.622721 | 🟡 high — specialist register | 0.028454 | respect, respects | — |
| 518 | **offer** | 48 | 3,098.78 | 3.725252 | 🟡 high — specialist register | 0.009902 | - | — |
| 519 | **please** | 21 | 3,091.38 | 8.494523 | 🟡 high — specialist register | 0.182384 | - | — |
| 520 | **behind** | 30 | 3,082.75 | 5.929574 | 🟡 high — specialist register | - | - | — |
| 521 | **night** | 31 | 3,079.59 | 5.732405 | 🟡 high — specialist register | 0.020479 | night, nights | — |
| 522 | **rest** | 32 | 3,077.82 | 5.550084 | 🟡 high — specialist register | 0.018300 | rest, rests | — |
| 523 | **realize** | 24 | 3,076.08 | 7.395911 | 🟡 high — specialist register | 0.016976 | - | — |
| 524 | **care** | 28 | 3,073.98 | 6.335039 | 🟡 high — specialist register | 0.023952 | care, cares | — |
| 525 | **year** | 82 | 3,066.19 | 2.157697 | 🟡 high — specialist register | 0.006052 | year, years | — |
| 526 | **already** | 41 | 3,055.13 | 4.29983 | 🟡 high — specialist register | - | - | — |
| 527 | **lotus** | 19 | 3,025.19 | 9.18767 | 🟡 high — specialist register | 0.024074 | - | ~ |
| 528 | **sick** | 19 | 3,025.19 | 9.18767 | 🟡 high — specialist register | 0.038534 | - | — |
| 529 | **full** | 42 | 3,024.27 | 4.155056 | 🟡 high — specialist register | - | - | ~ |
| 530 | **told** | 54 | 3,008.36 | 3.214709 | 🟡 high — specialist register | - | - | — |
| 531 | **ray** | 22 | 3,007.50 | 7.888387 | 🟡 high — specialist register | 0.037121 | ray, rays | — |
| 532 | **speak** | 20 | 3,007.36 | 8.676844 | 🟡 high — specialist register | 0.044614 | speak, speaks | — |
| 533 | **middle** | 29 | 3,006.45 | 5.982217 | 🟡 high — specialist register | 0.018845 | - | ~ |
| 534 | **lack** | 28 | 3,004.55 | 6.191938 | 🟡 high — specialist register | 0.024331 | lack, lacks | — |
| 535 | **blind** | 18 | 2,992.45 | 9.593135 | 🟢 medium — moderately distinctive | 0.040779 | - | — |
| 536 | **purified** | 18 | 2,992.45 | 9.593135 | 🟢 medium — moderately distinctive | - | - | — |
| 537 | **renounce** | 18 | 2,992.45 | 9.593135 | 🟢 medium — moderately distinctive | 0.040749 | - | — |
| 538 | **hair** | 18 | 2,992.45 | 9.593135 | 🟢 medium — moderately distinctive | 0.041123 | - | — |
| 539 | **lying** | 18 | 2,992.45 | 9.593135 | 🟢 medium — moderately distinctive | - | - | — |
| 540 | **nagarjuna** | 18 | 2,991.47 | 9.59 | 🟢 medium — moderately distinctive | 0.017060 | - | ✓ ཀླུ་སྒྲུབ |
| 541 | **wherever** | 18 | 2,991.47 | 9.59 | 🟢 medium — moderately distinctive | - | - | — |
| 542 | **indra** | 18 | 2,991.47 | 9.59 | 🟢 medium — moderately distinctive | 0.017403 | indra, indras | ✓ བརྒྱ་བྱིན |
| 543 | **sickness** | 18 | 2,991.47 | 9.59 | 🟢 medium — moderately distinctive | 0.044111 | sickness, sicknesses | — |
| 544 | **pleasant** | 18 | 2,991.47 | 9.59 | 🟢 medium — moderately distinctive | 0.040975 | - | — |
| 545 | **throne** | 18 | 2,991.47 | 9.59 | 🟢 medium — moderately distinctive | 0.039985 | throne, thrones | — |
| 546 | **tonpa** | 18 | 2,991.47 | 9.59 | 🟢 medium — moderately distinctive | 0.016266 | - | ~ |
| 547 | **unbearable** | 18 | 2,991.47 | 9.59 | 🟢 medium — moderately distinctive | 0.041133 | - | — |
| 548 | **yogi** | 18 | 2,991.47 | 9.59 | 🟢 medium — moderately distinctive | 0.048771 | yogi, yogis | — |
| 549 | **doubt** | 26 | 2,984.03 | 6.622721 | 🟢 medium — moderately distinctive | 0.035120 | doubt, doubts | — |
| 550 | **soon** | 34 | 2,950.88 | 5.008168 | 🟢 medium — moderately distinctive | 0.181215 | - | — |
| 551 | **fish** | 23 | 2,947.91 | 7.395911 | 🟢 medium — moderately distinctive | 0.031524 | fish, fishes | — |
| 552 | **fly** | 21 | 2,943.82 | 8.089058 | 🟢 medium — moderately distinctive | 0.067513 | flies, fly | — |
| 553 | **vision** | 21 | 2,943.82 | 8.089058 | 🟢 medium — moderately distinctive | 0.038720 | vision, visions | — |
| 554 | **idea** | 26 | 2,929.68 | 6.502093 | 🟢 medium — moderately distinctive | 0.029889 | idea, ideas | — |
| 555 | **explained** | 25 | 2,928.71 | 6.759922 | 🟢 medium — moderately distinctive | - | - | — |
| 556 | **consider** | 33 | 2,919.18 | 5.104499 | 🟢 medium — moderately distinctive | 0.074865 | - | — |
| 557 | **young** | 22 | 2,915.55 | 7.647225 | 🟢 medium — moderately distinctive | 0.031654 | - | — |
| 558 | **learn** | 21 | 2,905.48 | 7.983697 | 🟢 medium — moderately distinctive | 0.028215 | learn, learns | — |
| 559 | **side** | 27 | 2,905.10 | 6.208745 | 🟢 medium — moderately distinctive | 0.072818 | side, sides | — |
| 560 | **saying** | 35 | 2,887.65 | 4.760829 | 🟢 medium — moderately distinctive | - | saying, sayings | — |
| 561 | **try** | 30 | 2,885.46 | 5.550084 | 🟢 medium — moderately distinctive | - | - | — |
| 562 | **hold** | 34 | 2,877.49 | 4.883605 | 🟢 medium — moderately distinctive | 0.026270 | hold, holds | — |
| 563 | **entire** | 28 | 2,877.24 | 5.929574 | 🟢 medium — moderately distinctive | 0.023117 | - | — |
| 564 | **recognize** | 21 | 2,870.79 | 7.888387 | 🟢 medium — moderately distinctive | 0.033310 | - | — |
| 565 | **seem** | 25 | 2,869.26 | 6.622721 | 🟢 medium — moderately distinctive | - | seem, seems | — |
| 566 | **clean** | 18 | 2,865.97 | 9.18767 | 🟢 medium — moderately distinctive | 0.041351 | - | — |
| 567 | **no-one** | 19 | 2,856.99 | 8.676844 | 🟢 medium — moderately distinctive | - | - | — |
| 568 | **surrounded** | 19 | 2,856.99 | 8.676844 | 🟢 medium — moderately distinctive | - | - | — |
| 569 | **arrived** | 22 | 2,841.53 | 7.453069 | 🟢 medium — moderately distinctive | - | - | — |
| 570 | **cast** | 21 | 2,839.13 | 7.801376 | 🟢 medium — moderately distinctive | 0.033806 | - | — |
| 571 | **reflection** | 21 | 2,839.13 | 7.801376 | 🟢 medium — moderately distinctive | 0.041900 | reflection, reflections | — |
| 572 | **sit** | 21 | 2,839.13 | 7.801376 | 🟢 medium — moderately distinctive | 0.040825 | sit, sits | — |
| 573 | **rain** | 25 | 2,826.96 | 6.525082 | 🟢 medium — moderately distinctive | 0.030426 | rain, rains | — |
| 574 | **glorious** | 17 | 2,825.28 | 9.59 | 🟢 medium — moderately distinctive | 0.027039 | - | ~ |
| 575 | **sangye** | 17 | 2,825.28 | 9.59 | 🟢 medium — moderately distinctive | 0.016729 | - | ~ |
| 576 | **tear** | 17 | 2,825.28 | 9.59 | 🟢 medium — moderately distinctive | 0.053655 | tear, tears | — |
| 577 | **tion** | 17 | 2,825.28 | 9.59 | 🟢 medium — moderately distinctive | 0.096631 | tion, tions | — |
| 578 | **possess** | 17 | 2,825.28 | 9.59 | 🟢 medium — moderately distinctive | 0.149307 | possess, possesses | — |
| 579 | **nanda** | 17 | 2,825.28 | 9.59 | 🟢 medium — moderately distinctive | 0.021122 | - | ✓ དགའ་བོ |
| 580 | **downfall** | 17 | 2,825.28 | 9.59 | 🟢 medium — moderately distinctive | 0.039436 | downfall, downfalls | ✓ ལྟུང་བ |
| 581 | **mouth** | 21 | 2,810.00 | 7.721333 | 🟢 medium — moderately distinctive | 0.050093 | mouth, mouths | — |
| 582 | **eating** | 19 | 2,796.96 | 8.494523 | 🟢 medium — moderately distinctive | - | - | — |
| 583 | **unless** | 30 | 2,774.95 | 5.337522 | 🟢 medium — moderately distinctive | - | - | — |
| 584 | **gave** | 32 | 2,771.67 | 4.998015 | 🟢 medium — moderately distinctive | - | - | — |
| 585 | **fear** | 25 | 2,770.37 | 6.394462 | 🟢 medium — moderately distinctive | 0.030361 | fear, fears | — |
| 586 | **enjoy** | 19 | 2,746.21 | 8.340372 | 🟢 medium — moderately distinctive | 0.040140 | enjoy, enjoys | — |
| 587 | **brought** | 28 | 2,742.33 | 5.651553 | 🟢 medium — moderately distinctive | - | - | — |
| 588 | **material** | 26 | 2,740.21 | 6.08159 | 🟢 medium — moderately distinctive | 0.025889 | material, materials | — |
| 589 | **following** | 36 | 2,724.70 | 4.367389 | 🟢 medium — moderately distinctive | - | - | — |
| 590 | **actually** | 24 | 2,723.67 | 6.548613 | 🟢 medium — moderately distinctive | - | - | — |
| 591 | **next** | 40 | 2,712.44 | 3.912963 | 🟢 medium — moderately distinctive | - | - | — |
| 592 | **comfort** | 17 | 2,706.75 | 9.18767 | 🟢 medium — moderately distinctive | 0.046910 | comfort, comforts | — |
| 593 | **bone** | 17 | 2,706.75 | 9.18767 | 🟢 medium — moderately distinctive | 0.062540 | bone, bones | — |
| 594 | **iron** | 23 | 2,706.31 | 6.789775 | 🟢 medium — moderately distinctive | 0.029243 | - | — |
| 595 | **straight** | 20 | 2,703.93 | 7.801376 | 🟢 medium — moderately distinctive | 0.036158 | - | — |
| 596 | **ing** | 19 | 2,702.24 | 8.206841 | 🟢 medium — moderately distinctive | - | ing, ings | — |
| 597 | **clear** | 28 | 2,697.37 | 5.558895 | 🟢 medium — moderately distinctive | 0.016996 | - | ~ |
| 598 | **experienced** | 21 | 2,691.57 | 7.395911 | 🟢 medium — moderately distinctive | - | - | — |
| 599 | **hardship** | 20 | 2,676.19 | 7.721333 | 🟢 medium — moderately distinctive | 0.044841 | hardship, hardships | — |
| 600 | **intense** | 20 | 2,676.19 | 7.721333 | 🟢 medium — moderately distinctive | 0.035698 | - | — |
| 601 | **reality** | 21 | 2,671.89 | 7.341843 | 🟢 medium — moderately distinctive | 0.033936 | - | ~ |
| 602 | **brother** | 16 | 2,659.96 | 9.593135 | 🟢 medium — moderately distinctive | 0.039097 | brother, brothers | — |
| 603 | **miraculous** | 16 | 2,659.96 | 9.593135 | 🟢 medium — moderately distinctive | 0.047616 | - | — |
| 604 | **forever** | 16 | 2,659.96 | 9.593135 | 🟢 medium — moderately distinctive | 0.029084 | - | — |
| 605 | **fortunate** | 16 | 2,659.09 | 9.59 | 🟢 medium — moderately distinctive | 0.034132 | - | — |
| 606 | **omniscient** | 16 | 2,659.09 | 9.59 | 🟢 medium — moderately distinctive | 0.024140 | - | ~ |
| 607 | **basi** | 16 | 2,659.09 | 9.59 | 🟢 medium — moderately distinctive | - | - | — |
| 608 | **padampa** | 16 | 2,659.09 | 9.59 | 🟢 medium — moderately distinctive | 0.025096 | - | ~ |
| 609 | **thirst** | 16 | 2,659.09 | 9.59 | 🟢 medium — moderately distinctive | 0.046968 | - | — |
| 610 | **sakyamuni** | 16 | 2,659.09 | 9.59 | 🟢 medium — moderately distinctive | 0.018695 | - | — |
| 611 | **brahma** | 16 | 2,659.09 | 9.59 | 🟢 medium — moderately distinctive | 0.018823 | - | ✓ ཚངས་པ |
| 612 | **turtle** | 16 | 2,659.09 | 9.59 | 🟢 medium — moderately distinctive | 0.048949 | turtle, turtles | — |
| 613 | **nowaday** | 16 | 2,659.09 | 9.59 | 🟢 medium — moderately distinctive | - | - | — |
| 614 | **seated** | 16 | 2,659.09 | 9.59 | 🟢 medium — moderately distinctive | - | - | — |
| 615 | **bliss** | 16 | 2,659.09 | 9.59 | 🟢 medium — moderately distinctive | 0.040204 | - | ~ |
| 616 | **none** | 22 | 2,651.28 | 6.954078 | 🟢 medium — moderately distinctive | - | - | — |
| 617 | **perceive** | 18 | 2,649.75 | 8.494523 | 🟢 medium — moderately distinctive | 0.046368 | perceive, perceives | — |
| 618 | **reason** | 28 | 2,644.53 | 5.45 | 🟢 medium — moderately distinctive | 0.025140 | reason, reasons | — |
| 619 | **itself** | 27 | 2,639.87 | 5.641891 | 🟢 medium — moderately distinctive | - | - | — |
| 620 | **cut** | 38 | 2,634.32 | 4.000284 | 🟢 medium — moderately distinctive | 0.014595 | cut, cuts | — |
| 621 | **fortune** | 19 | 2,628.76 | 7.983697 | 🟢 medium — moderately distinctive | 0.042611 | fortune, fortunes | — |
| 622 | **far** | 33 | 2,624.48 | 4.589189 | 🟢 medium — moderately distinctive | - | - | — |
| 623 | **aspect** | 17 | 2,622.00 | 8.899988 | 🟢 medium — moderately distinctive | 0.057825 | aspect, aspects | — |
| 624 | **hidden** | 17 | 2,622.00 | 8.899988 | 🟢 medium — moderately distinctive | - | - | — |
| 625 | **spend** | 23 | 2,619.79 | 6.57271 | 🟢 medium — moderately distinctive | 0.029546 | - | — |
| 626 | **million** | 23 | 2,619.79 | 6.57271 | 🟢 medium — moderately distinctive | 0.036570 | million, millions | — |
| 627 | **hot** | 20 | 2,604.22 | 7.513694 | 🟢 medium — moderately distinctive | 0.035172 | - | — |
| 628 | **alive** | 18 | 2,601.67 | 8.340372 | 🟢 medium — moderately distinctive | 0.040574 | - | — |
| 629 | **hunger** | 18 | 2,601.67 | 8.340372 | 🟢 medium — moderately distinctive | 0.040507 | - | — |
| 630 | **seed** | 20 | 2,583.21 | 7.453069 | 🟢 medium — moderately distinctive | 0.047895 | seed, seeds | — |
| 631 | **mount** | 19 | 2,568.73 | 7.801376 | 🟢 medium — moderately distinctive | 0.016530 | - | ~ |
| 632 | **meat** | 23 | 2,565.35 | 6.436135 | 🟢 medium — moderately distinctive | 0.031376 | meat, meats | — |
| 633 | **enter** | 24 | 2,561.69 | 6.159148 | 🟢 medium — moderately distinctive | 0.032704 | enter, enters | — |
| 634 | **quite** | 23 | 2,556.96 | 6.415081 | 🟢 medium — moderately distinctive | - | - | — |
| 635 | **appearance** | 17 | 2,556.26 | 8.676844 | 🟢 medium — moderately distinctive | 0.068571 | appearance, appearances | — |
| 636 | **main** | 31 | 2,555.50 | 4.756853 | 🟢 medium — moderately distinctive | 0.020049 | - | ~ |
| 637 | **skin** | 16 | 2,547.53 | 9.18767 | 🟢 medium — moderately distinctive | 0.057760 | skin, skins | — |
| 638 | **carefully** | 21 | 2,544.01 | 6.990446 | 🟢 medium — moderately distinctive | 0.033591 | - | — |
| 639 | **properly** | 19 | 2,542.38 | 7.721333 | 🟢 medium — moderately distinctive | 0.038224 | - | — |
| 640 | **similar** | 28 | 2,537.80 | 5.230037 | 🟢 medium — moderately distinctive | 0.022808 | - | — |
| 641 | **rock** | 18 | 2,523.27 | 8.089058 | 🟢 medium — moderately distinctive | 0.041828 | rock, rocks | — |
| 642 | **wind** | 19 | 2,495.26 | 7.578232 | 🟢 medium — moderately distinctive | 0.051189 | wind, winds | ✓ རླུང |
| 643 | **remembering** | 15 | 2,493.71 | 9.593135 | 🟢 medium — moderately distinctive | - | - | — |
| 644 | **pride** | 15 | 2,493.71 | 9.593135 | 🟢 medium — moderately distinctive | 0.046590 | - | — |
| 645 | **cultivate** | 15 | 2,493.71 | 9.593135 | 🟢 medium — moderately distinctive | 0.051603 | - | — |
| 646 | **utterly** | 15 | 2,493.71 | 9.593135 | 🟢 medium — moderately distinctive | 0.047009 | - | — |
| 647 | **prostrate** | 15 | 2,492.89 | 9.59 | 🟢 medium — moderately distinctive | 0.051478 | - | — |
| 648 | **amitabha** | 15 | 2,492.89 | 9.59 | 🟢 medium — moderately distinctive | 0.022023 | - | ✓ འོད་དཔག་མེད |
| 649 | **distraction** | 15 | 2,492.89 | 9.59 | 🟢 medium — moderately distinctive | 0.077643 | distraction, distractions | — |
| 650 | **nirvana** | 15 | 2,492.89 | 9.59 | 🟢 medium — moderately distinctive | 0.046850 | - | ✓ མྱ་ངན་ལས་འདས་པ |
| 651 | **countless** | 15 | 2,492.89 | 9.59 | 🟢 medium — moderately distinctive | 0.051068 | - | — |
| 652 | **divine** | 15 | 2,492.89 | 9.59 | 🟢 medium — moderately distinctive | 0.050974 | - | — |
| 653 | **liberate** | 15 | 2,492.89 | 9.59 | 🟢 medium — moderately distinctive | 0.056217 | liberate, liberates | — |
| 654 | **milarepa** | 15 | 2,492.89 | 9.59 | 🟢 medium — moderately distinctive | 0.022093 | - | ~ |
| 655 | **loved** | 15 | 2,492.89 | 9.59 | 🟢 medium — moderately distinctive | - | - | — |
| 656 | **frog** | 15 | 2,492.89 | 9.59 | 🟢 medium — moderately distinctive | 0.064126 | frog, frogs | — |
| 657 | **goddess** | 15 | 2,492.89 | 9.59 | 🟢 medium — moderately distinctive | - | goddess, goddesses | — |
| 658 | **oneself** | 15 | 2,492.89 | 9.59 | 🟢 medium — moderately distinctive | 0.051671 | - | — |
| 659 | **boundless** | 15 | 2,492.89 | 9.59 | 🟢 medium — moderately distinctive | 0.051538 | - | ~ |
| 660 | **hunter** | 16 | 2,467.76 | 8.899988 | 🟢 medium — moderately distinctive | 0.094317 | hunter, hunters | — |
| 661 | **leg** | 16 | 2,467.76 | 8.899988 | 🟢 medium — moderately distinctive | - | - | — |
| 662 | **self** | 16 | 2,467.76 | 8.899988 | 🟢 medium — moderately distinctive | - | - | ~ |
| 663 | **metal** | 24 | 2,466.20 | 5.929574 | 🟢 medium — moderately distinctive | 0.028814 | metal, metals | — |
| 664 | **number** | 31 | 2,465.42 | 4.589189 | 🟢 medium — moderately distinctive | 0.021470 | number, numbers | — |
| 665 | **bound** | 19 | 2,454.05 | 7.453069 | 🟢 medium — moderately distinctive | 0.235801 | bound, bounds | — |
| 666 | **enough** | 27 | 2,453.16 | 5.242857 | 🟢 medium — moderately distinctive | - | - | — |
| 667 | **least** | 30 | 2,443.00 | 4.699034 | 🟢 medium — moderately distinctive | - | - | — |
| 668 | **hope** | 25 | 2,436.07 | 5.622843 | 🟢 medium — moderately distinctive | 0.051879 | hope, hopes | — |
| 669 | **centre** | 20 | 2,435.94 | 7.028186 | 🟢 medium — moderately distinctive | 0.036140 | - | — |
| 670 | **otherwise** | 21 | 2,429.34 | 6.675364 | 🟢 medium — moderately distinctive | - | - | — |
| 671 | **lake** | 21 | 2,419.64 | 6.648696 | 🟢 medium — moderately distinctive | 0.024613 | lake, lakes | — |
| 672 | **twelve** | 17 | 2,417.79 | 8.206841 | 🟢 medium — moderately distinctive | - | - | ~ |
| 673 | **inside** | 19 | 2,417.42 | 7.341843 | 🟢 medium — moderately distinctive | 0.037763 | - | — |
| 674 | **extremely** | 22 | 2,415.27 | 6.335039 | 🟢 medium — moderately distinctive | 0.029473 | - | — |
| 675 | **reach** | 26 | 2,411.39 | 5.351808 | 🟢 medium — moderately distinctive | 0.030614 | reach, reaches | — |
| 676 | **entirely** | 20 | 2,410.26 | 6.954078 | 🟢 medium — moderately distinctive | - | - | — |
| 677 | **undergo** | 16 | 2,405.89 | 8.676844 | 🟢 medium — moderately distinctive | 0.046959 | - | — |
| 678 | **certain** | 30 | 2,403.64 | 4.623322 | 🟢 medium — moderately distinctive | - | - | — |
| 679 | **bed** | 15 | 2,388.31 | 9.18767 | 🟢 medium — moderately distinctive | 0.054661 | bed, beds | — |
| 680 | **thirty-three** | 15 | 2,388.31 | 9.18767 | 🟢 medium — moderately distinctive | - | - | — |
| 681 | **subject** | 31 | 2,380.55 | 4.43121 | 🟢 medium — moderately distinctive | 0.030626 | subject, subjects | ~ |
| 682 | **excellent** | 20 | 2,374.98 | 6.852295 | 🟢 medium — moderately distinctive | 0.026887 | - | ~ |
| 683 | **top** | 25 | 2,368.12 | 5.466001 | 🟢 medium — moderately distinctive | - | top, tops | — |
| 684 | **belief** | 20 | 2,363.98 | 6.820546 | 🟢 medium — moderately distinctive | 0.044515 | belief, beliefs | — |
| 685 | **opportunity** | 22 | 2,360.71 | 6.191938 | 🟢 medium — moderately distinctive | 0.031613 | opportunities, opportunity | — |
| 686 | **accomplished** | 16 | 2,355.34 | 8.494523 | 🟢 medium — moderately distinctive | - | - | — |
| 687 | **heard** | 19 | 2,354.52 | 7.150788 | 🟢 medium — moderately distinctive | - | - | — |
| 688 | **preliminary** | 24 | 2,346.55 | 5.641891 | 🟢 medium — moderately distinctive | 0.043840 | preliminaries, preliminary | — |
| 689 | **remain** | 29 | 2,341.28 | 4.658661 | 🟢 medium — moderately distinctive | 0.033740 | remain, remains | — |
| 690 | **sixteen** | 14 | 2,327.46 | 9.593135 | 🟢 medium — moderately distinctive | 0.055082 | - | — |
| 691 | **sexual** | 14 | 2,327.46 | 9.593135 | 🟢 medium — moderately distinctive | 0.055649 | - | — |
| 692 | **crown** | 19 | 2,327.06 | 7.067407 | 🟢 medium — moderately distinctive | 0.040783 | crown, crowns | ~ |
| 693 | **stop** | 24 | 2,327.02 | 5.594934 | 🟢 medium — moderately distinctive | 0.032549 | stop, stops | — |
| 694 | **venerable** | 14 | 2,326.70 | 9.59 | 🟢 medium — moderately distinctive | 0.037616 | venerable, venerables | — |
| 695 | **expanse** | 14 | 2,326.70 | 9.59 | 🟢 medium — moderately distinctive | 0.033046 | - | — |
| 696 | **well-being** | 14 | 2,326.70 | 9.59 | 🟢 medium — moderately distinctive | - | - | — |
| 697 | **yak** | 14 | 2,326.70 | 9.59 | 🟢 medium — moderately distinctive | 0.079146 | yak, yaks | — |
| 698 | **elephant** | 14 | 2,326.70 | 9.59 | 🟢 medium — moderately distinctive | 0.071555 | elephant, elephants | — |
| 699 | **darkness** | 14 | 2,326.70 | 9.59 | 🟢 medium — moderately distinctive | 0.056032 | - | — |
| 700 | **temple** | 14 | 2,326.70 | 9.59 | 🟢 medium — moderately distinctive | 0.070976 | temple, temples | — |
| 701 | **vajrayana** | 14 | 2,326.70 | 9.59 | 🟢 medium — moderately distinctive | 0.023273 | - | ✓ རྡོ་རྗེ་ཐེག་པ |
| 702 | **pratyekabuddha** | 14 | 2,326.70 | 9.59 | 🟢 medium — moderately distinctive | 0.086164 | pratyekabuddha, pratyekabuddhas | ✓ རང་སངས་རྒྱས |
| 703 | **mentally** | 14 | 2,326.70 | 9.59 | 🟢 medium — moderately distinctive | 0.056042 | - | — |
| 704 | **liberated** | 14 | 2,326.70 | 9.59 | 🟢 medium — moderately distinctive | - | - | — |
| 705 | **treasure** | 14 | 2,326.70 | 9.59 | 🟢 medium — moderately distinctive | 0.072491 | treasure, treasures | ~ |
| 706 | **sacred** | 14 | 2,326.70 | 9.59 | 🟢 medium — moderately distinctive | 0.056327 | - | — |
| 707 | **wrathful** | 14 | 2,326.70 | 9.59 | 🟢 medium — moderately distinctive | 0.033007 | - | ~ |
| 708 | **support** | 29 | 2,314.87 | 4.60611 | 🟢 medium — moderately distinctive | 0.023100 | - | — |
| 709 | **relative** | 20 | 2,313.66 | 6.675364 | 🟢 medium — moderately distinctive | 0.071973 | relative, relatives | ~ |
| 710 | **cloud** | 15 | 2,313.53 | 8.899988 | 🟢 medium — moderately distinctive | 0.078582 | cloud, clouds | — |
| 711 | **honour** | 16 | 2,312.59 | 8.340372 | 🟢 medium — moderately distinctive | 0.058470 | honour, honours | — |
| 712 | **fail** | 19 | 2,289.75 | 6.954078 | 🟢 medium — moderately distinctive | 0.042523 | fail, fails | — |
| 713 | **claim** | 19 | 2,289.75 | 6.954078 | 🟢 medium — moderately distinctive | 0.042916 | claim, claims | — |
| 714 | **discipline** | 17 | 2,274.76 | 7.721333 | 🟢 medium — moderately distinctive | 0.044305 | - | — |
| 715 | **trying** | 23 | 2,268.42 | 5.691163 | 🟢 medium — moderately distinctive | - | - | — |
| 716 | **particularly** | 24 | 2,263.45 | 5.442095 | 🟢 medium — moderately distinctive | - | - | — |
| 717 | **protect** | 22 | 2,260.69 | 5.929574 | 🟢 medium — moderately distinctive | 0.032314 | protect, protects | — |
| 718 | **arm** | 19 | 2,256.23 | 6.852295 | 🟢 medium — moderately distinctive | 0.045838 | arm, arms | — |
| 719 | **listening** | 15 | 2,255.52 | 8.676844 | 🟢 medium — moderately distinctive | - | - | — |
| 720 | **horse** | 15 | 2,255.52 | 8.676844 | 🟢 medium — moderately distinctive | 0.042179 | - | — |
| 721 | **name** | 28 | 2,250.18 | 4.637308 | 🟢 medium — moderately distinctive | 0.061408 | name, names | — |
| 722 | **force** | 25 | 2,249.64 | 5.192532 | 🟢 medium — moderately distinctive | 0.044769 | force, forces | — |
| 723 | **central** | 32 | 2,237.28 | 4.034378 | 🟢 medium — moderately distinctive | 0.018204 | - | ~ |
| 724 | **fall** | 32 | 2,233.02 | 4.026701 | 🟢 medium — moderately distinctive | 0.022403 | fall, falls | — |
| 725 | **arrow** | 14 | 2,229.09 | 9.18767 | 🟢 medium — moderately distinctive | 0.097243 | arrow, arrows | — |
| 726 | **wild** | 14 | 2,229.09 | 9.18767 | 🟢 medium — moderately distinctive | 0.055560 | - | — |
| 727 | **eighty** | 14 | 2,229.09 | 9.18767 | 🟢 medium — moderately distinctive | 0.046015 | - | ~ |
| 728 | **hat** | 14 | 2,229.09 | 9.18767 | 🟢 medium — moderately distinctive | 0.046875 | hat, hats | — |
| 729 | **slaughtered** | 14 | 2,229.09 | 9.18767 | 🟢 medium — moderately distinctive | - | - | — |
| 730 | **likewise** | 14 | 2,229.09 | 9.18767 | 🟢 medium — moderately distinctive | 0.046579 | - | — |
| 731 | **worse** | 18 | 2,217.32 | 7.108229 | 🟢 medium — moderately distinctive | - | - | — |
| 732 | **easy** | 17 | 2,213.59 | 7.513694 | 🟢 medium — moderately distinctive | 0.044319 | - | — |
| 733 | **stream** | 17 | 2,213.59 | 7.513694 | 🟢 medium — moderately distinctive | 0.062499 | stream, streams | — |
| 734 | **open** | 28 | 2,199.91 | 4.53371 | 🟢 medium — moderately distinctive | 0.028304 | open, opens | — |
| 735 | **turned** | 19 | 2,197.97 | 6.675364 | 🟢 medium — moderately distinctive | - | - | — |
| 736 | **transmission** | 17 | 2,195.73 | 7.453069 | 🟢 medium — moderately distinctive | 0.068758 | transmission, transmissions | — |
| 737 | **clearly** | 20 | 2,189.10 | 6.31599 | 🟢 medium — moderately distinctive | - | - | — |
| 738 | **unable** | 20 | 2,189.10 | 6.31599 | 🟢 medium — moderately distinctive | 0.035634 | - | — |
| 739 | **serve** | 19 | 2,180.64 | 6.622721 | 🟢 medium — moderately distinctive | 0.038682 | serve, serves | — |
| 740 | **branch** | 19 | 2,172.30 | 6.597403 | 🟢 medium — moderately distinctive | 0.067202 | branch, branches | — |
| 741 | **getting** | 20 | 2,170.02 | 6.260931 | 🟢 medium — moderately distinctive | - | - | — |
| 742 | **ill** | 18 | 2,169.23 | 6.954078 | 🟢 medium — moderately distinctive | 0.061042 | ill, ills | — |
| 743 | **merchant** | 19 | 2,164.17 | 6.57271 | 🟢 medium — moderately distinctive | 0.060649 | merchant, merchants | — |
| 744 | **accumulating** | 16 | 2,163.14 | 7.801376 | 🟢 medium — moderately distinctive | - | - | ~ |
| 745 | **anger** | 17 | 2,162.96 | 7.341843 | 🟢 medium — moderately distinctive | 0.044261 | - | — |
| 746 | **bowl** | 13 | 2,161.22 | 9.593135 | 🟢 medium — moderately distinctive | 0.072659 | bowl, bowls | — |
| 747 | **crowd** | 13 | 2,161.22 | 9.593135 | 🟢 medium — moderately distinctive | 0.061197 | - | — |
| 748 | **endless** | 13 | 2,161.22 | 9.593135 | 🟢 medium — moderately distinctive | 0.061186 | - | — |
| 749 | **wonderful** | 13 | 2,161.22 | 9.593135 | 🟢 medium — moderately distinctive | 0.046532 | - | — |
| 750 | **selfish** | 13 | 2,161.22 | 9.593135 | 🟢 medium — moderately distinctive | 0.061503 | - | — |
| 751 | **sambhogakaya** | 13 | 2,160.51 | 9.59 | 🟢 medium — moderately distinctive | 0.061574 | - | ✓ ལོངས་སྤྱོད་རྫོགས་པའི་སྐུ |
| 752 | **jigme** | 13 | 2,160.51 | 9.59 | 🟢 medium — moderately distinctive | 0.025906 | - | ~ |
| 753 | **tormented** | 13 | 2,160.51 | 9.59 | 🟢 medium — moderately distinctive | - | - | — |
| 754 | **dagpo** | 13 | 2,160.51 | 9.59 | 🟢 medium — moderately distinctive | 0.025953 | - | ~ |
| 755 | **sorrow** | 13 | 2,160.51 | 9.59 | 🟢 medium — moderately distinctive | 0.098663 | sorrow, sorrows | — |
| 756 | **beast** | 13 | 2,160.51 | 9.59 | 🟢 medium — moderately distinctive | 0.087813 | beast, beasts | — |
| 757 | **translator** | 13 | 2,160.51 | 9.59 | 🟢 medium — moderately distinctive | 0.090008 | translator, translators | — |
| 758 | **statue** | 13 | 2,160.51 | 9.59 | 🟢 medium — moderately distinctive | 0.079674 | statue, statues | — |
| 759 | **ephemeral** | 13 | 2,160.51 | 9.59 | 🟢 medium — moderately distinctive | 0.060322 | - | — |
| 760 | **lamp** | 13 | 2,160.51 | 9.59 | 🟢 medium — moderately distinctive | 0.103287 | lamp, lamps | — |
| 761 | **robe** | 13 | 2,160.51 | 9.59 | 🟢 medium — moderately distinctive | 0.088063 | robe, robes | — |
| 762 | **yoke** | 13 | 2,160.51 | 9.59 | 🟢 medium — moderately distinctive | 0.059421 | - | — |
| 763 | **tantric** | 13 | 2,160.51 | 9.59 | 🟢 medium — moderately distinctive | 0.055672 | - | — |
| 764 | **follower** | 13 | 2,160.51 | 9.59 | 🟢 medium — moderately distinctive | 0.072524 | follower, followers | — |
| 765 | **precept** | 13 | 2,160.51 | 9.59 | 🟢 medium — moderately distinctive | - | - | — |
| 766 | **tathagata** | 13 | 2,160.51 | 9.59 | 🟢 medium — moderately distinctive | 0.042552 | tathagata, tathagatas | ✓ དེ་བཞིན་གཤེགས་པ |
| 767 | **skull** | 13 | 2,160.51 | 9.59 | 🟢 medium — moderately distinctive | 0.066785 | skull, skulls | ~ |
| 768 | **primal** | 13 | 2,160.51 | 9.59 | 🟢 medium — moderately distinctive | 0.061606 | - | ~ |
| 769 | **wife** | 14 | 2,159.29 | 8.899988 | 🟢 medium — moderately distinctive | 0.055951 | - | — |
| 770 | **short** | 25 | 2,148.21 | 4.958406 | 🟢 medium — moderately distinctive | 0.027056 | - | — |
| 771 | **regret** | 16 | 2,140.95 | 7.721333 | 🟢 medium — moderately distinctive | 0.047784 | - | — |
| 772 | **looking** | 22 | 2,136.62 | 5.604151 | 🟢 medium — moderately distinctive | - | - | — |
| 773 | **used** | 27 | 2,136.44 | 4.565971 | 🟢 medium — moderately distinctive | - | - | — |
| 774 | **according** | 27 | 2,119.86 | 4.53054 | 🟢 medium — moderately distinctive | - | - | — |
| 775 | **create** | 20 | 2,113.07 | 6.096628 | 🟢 medium — moderately distinctive | 0.039019 | create, creates | — |
| 776 | **grain** | 26 | 2,108.91 | 4.68048 | 🟢 medium — moderately distinctive | 0.041697 | grain, grains | — |
| 777 | **dark** | 14 | 2,105.15 | 8.676844 | 🟢 medium — moderately distinctive | 0.048236 | - | — |
| 778 | **exhausted** | 14 | 2,105.15 | 8.676844 | 🟢 medium — moderately distinctive | - | - | — |
| 779 | **substance** | 14 | 2,105.15 | 8.676844 | 🟢 medium — moderately distinctive | 0.087473 | substance, substances | ~ |
| 780 | **ben** | 15 | 2,102.73 | 8.089058 | 🟢 medium — moderately distinctive | 0.024482 | - | — |
| 781 | **high** | 29 | 2,101.47 | 4.181489 | 🟢 medium — moderately distinctive | 0.019297 | - | — |
| 782 | **big** | 21 | 2,086.17 | 5.732405 | 🟢 medium — moderately distinctive | 0.033108 | - | — |
| 783 | **one** | 43 | 2,082.10 | 2.794079 | 🟢 medium — moderately distinctive | - | - | ~ |
| 784 | **receive** | 24 | 2,080.86 | 5.003079 | 🟢 medium — moderately distinctive | 0.014649 | receive, receives | — |
| 785 | **knowledge** | 15 | 2,075.34 | 7.983697 | 🟢 medium — moderately distinctive | 0.046746 | - | — |
| 786 | **transform** | 13 | 2,069.87 | 9.18767 | 🟢 medium — moderately distinctive | 0.066518 | transform, transforms | — |
| 787 | **heat** | 16 | 2,066.57 | 7.453069 | 🟢 medium — moderately distinctive | 0.050572 | heat, heats | — |
| 788 | **case** | 22 | 2,065.93 | 5.418748 | 🟢 medium — moderately distinctive | 0.030757 | - | — |
| 789 | **presence** | 18 | 2,065.87 | 6.622721 | 🟢 medium — moderately distinctive | 0.041005 | - | — |
| 790 | **illness** | 14 | 2,060.92 | 8.494523 | 🟢 medium — moderately distinctive | 0.093633 | illness, illnesses | — |
| 791 | **escape** | 14 | 2,060.92 | 8.494523 | 🟢 medium — moderately distinctive | 0.059408 | escape, escapes | — |
| 792 | **sowing** | 14 | 2,060.92 | 8.494523 | 🟢 medium — moderately distinctive | - | - | — |
| 793 | **difficulty** | 17 | 2,059.43 | 6.990446 | 🟢 medium — moderately distinctive | 0.074646 | difficulties, difficulty | — |
| 794 | **image** | 15 | 2,050.57 | 7.888387 | 🟢 medium — moderately distinctive | 0.064384 | image, images | — |
| 795 | **kingdom** | 17 | 2,048.72 | 6.954078 | 🟢 medium — moderately distinctive | 0.053638 | kingdom, kingdoms | — |
| 796 | **energy** | 26 | 2,041.35 | 4.53054 | 🟢 medium — moderately distinctive | 0.047091 | energies, energy | ✓ རླུང |
| 797 | **coming** | 21 | 2,026.26 | 5.567784 | 🟢 medium — moderately distinctive | - | - | — |
| 798 | **gather** | 14 | 2,023.52 | 8.340372 | 🟢 medium — moderately distinctive | 0.065443 | gather, gathers | — |
| 799 | **chance** | 20 | 2,021.33 | 5.831935 | 🟢 medium — moderately distinctive | 0.036746 | chance, chances | — |
| 800 | **reflect** | 23 | 2,019.21 | 5.065927 | 🟢 medium — moderately distinctive | 0.029571 | - | — |
| 801 | **higher** | 30 | 2,018.60 | 3.882708 | 🟢 medium — moderately distinctive | 0.020978 | - | — |
| 802 | **fully** | 21 | 2,007.27 | 5.515598 | 🟢 medium — moderately distinctive | 0.033461 | - | — |
| 803 | **weapon** | 13 | 2,005.06 | 8.899988 | 🟢 medium — moderately distinctive | 0.065456 | weapon, weapons | — |
| 804 | **awareness** | 13 | 2,005.06 | 8.899988 | 🟢 medium — moderately distinctive | 0.061580 | - | ✓ རིག་པ |
| 805 | **tooth** | 13 | 2,005.06 | 8.899988 | 🟢 medium — moderately distinctive | 0.107960 | teeth, tooth | — |
| 806 | **blazing** | 12 | 1,994.97 | 9.593135 | 🟢 medium — moderately distinctive | - | - | — |
| 807 | **virtue** | 12 | 1,994.97 | 9.593135 | 🟢 medium — moderately distinctive | 0.101009 | virtue, virtues | — |
| 808 | **meru** | 12 | 1,994.97 | 9.593135 | 🟢 medium — moderately distinctive | 0.028081 | - | ~ |
| 809 | **devote** | 12 | 1,994.97 | 9.593135 | 🟢 medium — moderately distinctive | 0.067434 | - | — |
| 810 | **sincere** | 12 | 1,994.97 | 9.593135 | 🟢 medium — moderately distinctive | 0.067740 | - | — |
| 811 | **nirmanakaya** | 12 | 1,994.32 | 9.59 | 🟢 medium — moderately distinctive | 0.061129 | - | ✓ སྤྲུལ་སྐུ |
| 812 | **aspiration** | 12 | 1,994.32 | 9.59 | 🟢 medium — moderately distinctive | 0.081174 | aspiration, aspirations | ~ |
| 813 | **compassionate** | 12 | 1,994.32 | 9.59 | 🟢 medium — moderately distinctive | 0.043280 | - | ~ |
| 814 | **twenty-one** | 12 | 1,994.32 | 9.59 | 🟢 medium — moderately distinctive | - | - | — |
| 815 | **rejoice** | 12 | 1,994.32 | 9.59 | 🟢 medium — moderately distinctive | 0.061220 | - | — |
| 816 | **useless** | 12 | 1,994.32 | 9.59 | 🟢 medium — moderately distinctive | 0.067245 | - | — |
| 817 | **breath** | 12 | 1,994.32 | 9.59 | 🟢 medium — moderately distinctive | 0.067532 | - | — |
| 818 | **sravaka** | 12 | 1,994.32 | 9.59 | 🟢 medium — moderately distinctive | 0.096835 | sravaka, sravakas | — |
| 819 | **attendant** | 12 | 1,994.32 | 9.59 | 🟢 medium — moderately distinctive | 0.073427 | attendant, attendants | — |
| 820 | **patron** | 12 | 1,994.32 | 9.59 | 🟢 medium — moderately distinctive | 0.073269 | patron, patrons | — |
| 821 | **abbot** | 12 | 1,994.32 | 9.59 | 🟢 medium — moderately distinctive | 0.044039 | - | ✓ མཁན་པོ |
| 822 | **wish-granting** | 12 | 1,994.32 | 9.59 | 🟢 medium — moderately distinctive | - | - | — |
| 823 | **purifying** | 12 | 1,994.32 | 9.59 | 🟢 medium — moderately distinctive | - | - | — |
| 824 | **skilfully** | 12 | 1,994.32 | 9.59 | 🟢 medium — moderately distinctive | 0.067438 | - | — |
| 825 | **apply** | 18 | 1,988.37 | 6.374259 | 🟢 medium — moderately distinctive | 0.061410 | applies, apply | — |
| 826 | **home** | 22 | 1,972.73 | 5.174295 | 🟢 medium — moderately distinctive | 0.036743 | home, homes | — |
| 827 | **lay** | 16 | 1,970.95 | 7.108229 | 🟢 medium — moderately distinctive | 0.231227 | lay, lays | ~ |
| 828 | **immediately** | 22 | 1,963.65 | 5.150484 | 🟢 medium — moderately distinctive | 0.031588 | - | — |
| 829 | **obtain** | 18 | 1,958.64 | 6.278949 | 🟢 medium — moderately distinctive | 0.040960 | - | — |
| 830 | **destroy** | 13 | 1,954.79 | 8.676844 | 🟢 medium — moderately distinctive | 0.066418 | destroy, destroys | — |
| 831 | **sake** | 13 | 1,954.79 | 8.676844 | 🟢 medium — moderately distinctive | 0.061122 | - | — |
| 832 | **walk** | 13 | 1,954.79 | 8.676844 | 🟢 medium — moderately distinctive | 0.066301 | walk, walks | — |
| 833 | **representation** | 15 | 1,953.16 | 7.513694 | 🟢 medium — moderately distinctive | 0.085825 | representation, representations | — |
| 834 | **indeed** | 15 | 1,953.16 | 7.513694 | 🟢 medium — moderately distinctive | - | - | — |
| 835 | **approach** | 18 | 1,953.01 | 6.260931 | 🟢 medium — moderately distinctive | 0.046580 | approach, approaches | ~ |
| 836 | **pass** | 16 | 1,948.76 | 7.028186 | 🟢 medium — moderately distinctive | 0.051368 | pass, passes | — |
| 837 | **order** | 22 | 1,946.12 | 5.104499 | 🟢 medium — moderately distinctive | 0.034869 | order, orders | — |
| 838 | **instance** | 14 | 1,936.98 | 7.983697 | 🟢 medium — moderately distinctive | 0.059874 | instance, instances | — |
| 839 | **blue** | 14 | 1,936.98 | 7.983697 | 🟢 medium — moderately distinctive | 0.051151 | - | — |
| 840 | **forest** | 15 | 1,922.55 | 7.395911 | 🟢 medium — moderately distinctive | 0.069733 | forest, forests | — |
| 841 | **under** | 33 | 1,915.78 | 3.34994 | 🟢 medium — moderately distinctive | - | - | — |
| 842 | **offered** | 23 | 1,913.80 | 4.801485 | 🟢 medium — moderately distinctive | - | - | — |
| 843 | **beat** | 13 | 1,913.71 | 8.494523 | 🟢 medium — moderately distinctive | 0.064904 | beat, beats | — |
| 844 | **harsh** | 13 | 1,913.71 | 8.494523 | 🟢 medium — moderately distinctive | 0.060904 | - | — |
| 845 | **angry** | 13 | 1,913.71 | 8.494523 | 🟢 medium — moderately distinctive | 0.061251 | - | — |
| 846 | **wear** | 13 | 1,913.71 | 8.494523 | 🟢 medium — moderately distinctive | 0.072407 | wear, wears | — |
| 847 | **motivation** | 12 | 1,910.65 | 9.18767 | 🟢 medium — moderately distinctive | 0.067151 | - | — |
| 848 | **tongue** | 12 | 1,910.65 | 9.18767 | 🟢 medium — moderately distinctive | 0.101726 | tongue, tongues | — |
| 849 | **discord** | 12 | 1,910.65 | 9.18767 | 🟢 medium — moderately distinctive | 0.067037 | - | — |
| 850 | **tea** | 16 | 1,909.08 | 6.885085 | 🟢 medium — moderately distinctive | 0.173215 | - | — |
| 851 | **committed** | 18 | 1,897.07 | 6.08159 | 🟢 medium — moderately distinctive | - | - | — |
| 852 | **believe** | 21 | 1,896.46 | 5.211109 | 🟢 medium — moderately distinctive | 0.070206 | - | — |
| 853 | **caught** | 14 | 1,892.75 | 7.801376 | 🟢 medium — moderately distinctive | - | - | — |
| 854 | **poor** | 18 | 1,892.45 | 6.066775 | 🟢 medium — moderately distinctive | 0.037625 | - | — |
| 855 | **accomplish** | 13 | 1,878.98 | 8.340372 | 🟢 medium — moderately distinctive | 0.047770 | accomplish, accomplishes | — |
| 856 | **knew** | 13 | 1,878.98 | 8.340372 | 🟢 medium — moderately distinctive | - | - | — |
| 857 | **met** | 20 | 1,878.12 | 5.418748 | 🟢 medium — moderately distinctive | - | - | — |
| 858 | **field** | 19 | 1,873.91 | 5.691163 | 🟢 medium — moderately distinctive | 0.073309 | field, fields | ~ |
| 859 | **sole** | 14 | 1,873.33 | 7.721333 | 🟢 medium — moderately distinctive | 0.087170 | sole, soles | — |
| 860 | **base** | 22 | 1,870.59 | 4.906385 | 🟢 medium — moderately distinctive | 0.019476 | - | — |
| 861 | **extraordinary** | 23 | 1,862.65 | 4.673154 | 🟢 medium — moderately distinctive | 0.027741 | - | — |
| 862 | **grow** | 19 | 1,860.87 | 5.651553 | 🟢 medium — moderately distinctive | 0.055737 | grow, grows | — |
| 863 | **condition** | 18 | 1,857.75 | 5.955549 | 🟢 medium — moderately distinctive | 0.052513 | condition, conditions | — |
| 864 | **include** | 25 | 1,855.33 | 4.282395 | 🟢 medium — moderately distinctive | 0.036882 | include, includes | — |
| 865 | **leaving** | 17 | 1,855.23 | 6.297298 | 🟢 medium — moderately distinctive | - | - | — |
| 866 | **huge** | 18 | 1,853.68 | 5.942477 | 🟢 medium — moderately distinctive | 0.040754 | - | — |
| 867 | **seen** | 23 | 1,852.60 | 4.647928 | 🟢 medium — moderately distinctive | - | - | — |
| 868 | **sense** | 16 | 1,850.93 | 6.675364 | 🟢 medium — moderately distinctive | 0.042239 | - | — |
| 869 | **village** | 12 | 1,850.82 | 8.899988 | 🟢 medium — moderately distinctive | 0.080235 | village, villages | — |
| 870 | **reign** | 12 | 1,850.82 | 8.899988 | 🟢 medium — moderately distinctive | 0.067031 | - | — |
| 871 | **wishing** | 12 | 1,850.82 | 8.899988 | 🟢 medium — moderately distinctive | - | - | — |
| 872 | **detail** | 15 | 1,847.77 | 7.108229 | 🟢 medium — moderately distinctive | 0.086285 | detail, details | — |
| 873 | **started** | 20 | 1,845.08 | 5.323438 | 🟢 medium — moderately distinctive | - | - | — |
| 874 | **conduct** | 15 | 1,837.15 | 7.067407 | 🟢 medium — moderately distinctive | 0.051325 | - | — |
| 875 | **happened** | 15 | 1,837.15 | 7.067407 | 🟢 medium — moderately distinctive | - | - | — |
| 876 | **holding** | 22 | 1,835.37 | 4.814012 | 🟢 medium — moderately distinctive | - | - | — |
| 877 | **manifest** | 11 | 1,828.72 | 9.593135 | 🟢 medium — moderately distinctive | - | manifest, manifests | ~ |
| 878 | **terrible** | 11 | 1,828.72 | 9.593135 | 🟢 medium — moderately distinctive | 0.074420 | - | — |
| 879 | **attaining** | 11 | 1,828.72 | 9.593135 | 🟢 medium — moderately distinctive | - | - | — |
| 880 | **shoulder** | 11 | 1,828.72 | 9.593135 | 🟢 medium — moderately distinctive | 0.123066 | shoulder, shoulders | — |
| 881 | **misconduct** | 11 | 1,828.72 | 9.593135 | 🟢 medium — moderately distinctive | 0.074336 | - | — |
| 882 | **finger** | 11 | 1,828.72 | 9.593135 | 🟢 medium — moderately distinctive | 0.092690 | finger, fingers | — |
| 883 | **crest** | 11 | 1,828.72 | 9.593135 | 🟢 medium — moderately distinctive | 0.034927 | - | — |
| 884 | **vidyadhara** | 11 | 1,828.12 | 9.59 | 🟢 medium — moderately distinctive | 0.216530 | vidyadhara, vidyadharas | ✓ རིག་འཛིན |
| 885 | **rigdzin** | 11 | 1,828.12 | 9.59 | 🟢 medium — moderately distinctive | 0.044470 | - | — |
| 886 | **lingpa** | 11 | 1,828.12 | 9.59 | 🟢 medium — moderately distinctive | 0.033197 | - | ~ |
| 887 | **impure** | 11 | 1,828.12 | 9.59 | 🟢 medium — moderately distinctive | 0.074608 | - | — |
| 888 | **samantabhadra** | 11 | 1,828.12 | 9.59 | 🟢 medium — moderately distinctive | 0.038838 | samantabhadra, samantabhadras | ✓ ཀུན་ཏུ་བཟང་པོ |
| 889 | **yidam** | 11 | 1,828.12 | 9.59 | 🟢 medium — moderately distinctive | 0.102740 | yidam, yidams | ✓ ཡི་དམ |
| 890 | **physically** | 11 | 1,828.12 | 9.59 | 🟢 medium — moderately distinctive | 0.074608 | - | — |
| 891 | **tsa-tsa** | 11 | 1,828.12 | 9.59 | 🟢 medium — moderately distinctive | - | tsa-tsa, tsa-tsas | ✓ ཙ་ཙ |
| 892 | **pandita** | 11 | 1,828.12 | 9.59 | 🟢 medium — moderately distinctive | 0.137159 | pandita, panditas | ✓ |
| 893 | **spontaneously** | 11 | 1,828.12 | 9.59 | 🟢 medium — moderately distinctive | 0.067570 | - | — |
| 894 | **limb** | 11 | 1,828.12 | 9.59 | 🟢 medium — moderately distinctive | 0.081189 | limb, limbs | — |
| 895 | **misdeed** | 11 | 1,828.12 | 9.59 | 🟢 medium — moderately distinctive | 0.082485 | misdeed, misdeeds | — |
| 896 | **torma** | 11 | 1,828.12 | 9.59 | 🟢 medium — moderately distinctive | 0.193771 | torma, tormas | ✓ གཏོར་མ |
| 897 | **knife** | 11 | 1,828.12 | 9.59 | 🟢 medium — moderately distinctive | 0.074716 | - | — |
| 898 | **ignorance** | 11 | 1,828.12 | 9.59 | 🟢 medium — moderately distinctive | 0.074518 | - | — |
| 899 | **chatter** | 11 | 1,828.12 | 9.59 | 🟢 medium — moderately distinctive | 0.074360 | - | — |
| 900 | **obey** | 11 | 1,828.12 | 9.59 | 🟢 medium — moderately distinctive | 0.082087 | obey, obeys | — |
| 901 | **mindfulness** | 11 | 1,828.12 | 9.59 | 🟢 medium — moderately distinctive | 0.075027 | - | — |
| 902 | **manifestation** | 11 | 1,828.12 | 9.59 | 🟢 medium — moderately distinctive | 0.091940 | manifestation, manifestations | — |
| 903 | **impartiality** | 11 | 1,828.12 | 9.59 | 🟢 medium — moderately distinctive | 0.074795 | - | — |
| 904 | **lita** | 11 | 1,828.12 | 9.59 | 🟢 medium — moderately distinctive | 0.139439 | lita, litas | — |
| 905 | **violation** | 14 | 1,822.95 | 7.513694 | 🟢 medium — moderately distinctive | 0.071689 | violation, violations | — |
| 906 | **lose** | 16 | 1,815.78 | 6.548613 | 🟢 medium — moderately distinctive | 0.044764 | - | — |
| 907 | **study** | 19 | 1,810.57 | 5.498791 | 🟢 medium — moderately distinctive | 0.041174 | studies, study | ✓ ཐོས་པ |
| 908 | **superior** | 14 | 1,808.24 | 7.453069 | 🟢 medium — moderately distinctive | 0.060682 | superior, superiors | — |
| 909 | **importance** | 15 | 1,807.69 | 6.954078 | 🟢 medium — moderately distinctive | 0.051675 | - | — |
| 910 | **physical** | 15 | 1,807.69 | 6.954078 | 🟢 medium — moderately distinctive | 0.051112 | - | — |
| 911 | **female** | 12 | 1,804.42 | 8.676844 | 🟢 medium — moderately distinctive | 0.066672 | female, females | — |
| 912 | **wonder** | 12 | 1,804.42 | 8.676844 | 🟢 medium — moderately distinctive | - | - | — |
| 913 | **ceremony** | 12 | 1,804.42 | 8.676844 | 🟢 medium — moderately distinctive | 0.108364 | ceremonies, ceremony | — |
| 914 | **second** | 24 | 1,800.02 | 4.327858 | 🟢 medium — moderately distinctive | - | - | ~ |
| 915 | **mistake** | 13 | 1,798.63 | 7.983697 | 🟢 medium — moderately distinctive | 0.088559 | mistake, mistakes | — |
| 916 | **consist** | 14 | 1,794.38 | 7.395911 | 🟢 medium — moderately distinctive | 0.086916 | consist, consists | — |
| 917 | **putting** | 16 | 1,790.56 | 6.457641 | 🟢 medium — moderately distinctive | - | - | — |
| 918 | **equal** | 18 | 1,781.65 | 5.711571 | 🟢 medium — moderately distinctive | 0.043158 | equal, equals | — |
| 919 | **symbol** | 13 | 1,777.16 | 7.888387 | 🟢 medium — moderately distinctive | 0.100175 | symbol, symbols | ~ |
| 920 | **round** | 18 | 1,775.28 | 5.691163 | 🟢 medium — moderately distinctive | 0.041149 | - | — |
| 921 | **road** | 14 | 1,768.82 | 7.29055 | 🟢 medium — moderately distinctive | 0.060399 | road, roads | — |
| 922 | **smallest** | 12 | 1,766.50 | 8.494523 | 🟢 medium — moderately distinctive | - | - | — |
| 923 | **assembly** | 13 | 1,757.55 | 7.801376 | 🟢 medium — moderately distinctive | 0.067389 | assemblies, assembly | — |
| 924 | **butter** | 13 | 1,757.55 | 7.801376 | 🟢 medium — moderately distinctive | 0.067405 | - | — |
| 925 | **abandon** | 13 | 1,739.52 | 7.721333 | 🟢 medium — moderately distinctive | 0.055127 | - | — |
| 926 | **false** | 13 | 1,739.52 | 7.721333 | 🟢 medium — moderately distinctive | 0.061436 | - | — |
| 927 | **hearing** | 16 | 1,736.01 | 6.260931 | 🟢 medium — moderately distinctive | - | - | ~ |
| 928 | **league** | 12 | 1,734.45 | 8.340372 | 🟢 medium — moderately distinctive | 0.133526 | league, leagues | — |
| 929 | **colour** | 12 | 1,734.45 | 8.340372 | 🟢 medium — moderately distinctive | 0.090353 | colour, colours | — |
| 930 | **rely** | 13 | 1,722.83 | 7.647225 | 🟢 medium — moderately distinctive | 0.067782 | relies, rely | — |
| 931 | **spread** | 15 | 1,714.98 | 6.597403 | 🟢 medium — moderately distinctive | 0.050546 | spread, spreads | — |
| 932 | **warm** | 13 | 1,707.28 | 7.578232 | 🟢 medium — moderately distinctive | 0.066630 | warm, warms | — |
| 933 | **confidence** | 16 | 1,703.35 | 6.143148 | 🟢 medium — moderately distinctive | 0.047550 | - | — |
| 934 | **actual** | 16 | 1,698.99 | 6.127399 | 🟢 medium — moderately distinctive | 0.047605 | - | — |
| 935 | **vigilance** | 11 | 1,696.59 | 8.899988 | 🟢 medium — moderately distinctive | 0.074979 | - | — |
| 936 | **easily** | 14 | 1,696.00 | 6.990446 | 🟢 medium — moderately distinctive | 0.056063 | - | — |
| 937 | **deep** | 14 | 1,696.00 | 6.990446 | 🟢 medium — moderately distinctive | 0.050242 | - | — |
| 938 | **impossible** | 14 | 1,696.00 | 6.990446 | 🟢 medium — moderately distinctive | 0.055823 | - | — |
| 939 | **across** | 15 | 1,690.20 | 6.502093 | 🟢 medium — moderately distinctive | - | - | — |
| 940 | **keeping** | 15 | 1,684.36 | 6.47962 | 🟢 medium — moderately distinctive | - | - | — |
| 941 | **gathered** | 12 | 1,682.18 | 8.089058 | 🟢 medium — moderately distinctive | - | - | — |
| 942 | **commit** | 12 | 1,682.18 | 8.089058 | 🟢 medium — moderately distinctive | 0.041097 | - | — |
| 943 | **got** | 15 | 1,673.06 | 6.436135 | 🟢 medium — moderately distinctive | - | - | — |
| 944 | **spent** | 15 | 1,673.06 | 6.436135 | 🟢 medium — moderately distinctive | - | - | — |
| 945 | **protection** | 16 | 1,670.21 | 6.023602 | 🟢 medium — moderately distinctive | 0.047590 | - | — |
| 946 | **explain** | 13 | 1,666.21 | 7.395911 | 🟢 medium — moderately distinctive | 0.024967 | explain, explains | — |
| 947 | **chapter** | 14 | 1,662.49 | 6.852295 | 🟢 medium — moderately distinctive | 0.050763 | - | — |
| 948 | **phase** | 14 | 1,662.49 | 6.852295 | 🟢 medium — moderately distinctive | 0.020785 | - | ~ |
| 949 | **grass** | 10 | 1,662.47 | 9.593135 | 🟢 medium — moderately distinctive | 0.083143 | - | ~ |
| 950 | **journey** | 10 | 1,662.47 | 9.593135 | 🟢 medium — moderately distinctive | 0.092930 | journey, journeys | — |
| 951 | **pouring** | 10 | 1,662.47 | 9.593135 | 🟢 medium — moderately distinctive | - | - | — |
| 952 | **pith** | 10 | 1,661.93 | 9.59 | 🟢 medium — moderately distinctive | 0.083805 | - | ~ |
| 953 | **dakini** | 10 | 1,661.93 | 9.59 | 🟢 medium — moderately distinctive | 0.135195 | dakini, dakinis | ✓ མཁའ་འགྲོ་མ |
| 954 | **embodiment** | 10 | 1,661.93 | 9.59 | 🟢 medium — moderately distinctive | 0.083734 | - | — |
| 955 | **jealousy** | 10 | 1,661.93 | 9.59 | 🟢 medium — moderately distinctive | 0.083701 | - | — |
| 956 | **doctor** | 10 | 1,661.93 | 9.59 | 🟢 medium — moderately distinctive | 0.089046 | doctor, doctors | — |
| 957 | **behave** | 10 | 1,661.93 | 9.59 | 🟢 medium — moderately distinctive | 0.104226 | behave, behaves | — |
| 958 | **cave** | 10 | 1,661.93 | 9.59 | 🟢 medium — moderately distinctive | 0.074643 | - | — |
| 959 | **princess** | 10 | 1,661.93 | 9.59 | 🟢 medium — moderately distinctive | 0.075871 | princess, princesses | — |
| 960 | **monastic** | 10 | 1,661.93 | 9.59 | 🟢 medium — moderately distinctive | 0.082977 | - | — |
| 961 | **lifespan** | 10 | 1,661.93 | 9.59 | 🟢 medium — moderately distinctive | 0.082434 | - | — |
| 962 | **cried** | 10 | 1,661.93 | 9.59 | 🟢 medium — moderately distinctive | - | - | — |
| 963 | **traveller** | 10 | 1,661.93 | 9.59 | 🟢 medium — moderately distinctive | 0.092444 | traveller, travellers | — |
| 964 | **condensed** | 10 | 1,661.93 | 9.59 | 🟢 medium — moderately distinctive | - | - | — |
| 965 | **burn** | 10 | 1,661.93 | 9.59 | 🟢 medium — moderately distinctive | 0.074135 | burn, burns | — |
| 966 | **ornament** | 10 | 1,661.93 | 9.59 | 🟢 medium — moderately distinctive | 0.096875 | ornament, ornaments | — |
| 967 | **clairvoyance** | 10 | 1,661.93 | 9.59 | 🟢 medium — moderately distinctive | 0.083089 | - | — |
| 968 | **alm** | 10 | 1,661.93 | 9.59 | 🟢 medium — moderately distinctive | - | - | — |
| 969 | **humble** | 10 | 1,661.93 | 9.59 | 🟢 medium — moderately distinctive | 0.083819 | - | — |
| 970 | **immeasurable** | 10 | 1,661.93 | 9.59 | 🟢 medium — moderately distinctive | 0.083800 | - | — |
| 971 | **throat** | 10 | 1,661.93 | 9.59 | 🟢 medium — moderately distinctive | 0.093227 | throat, throats | — |
| 972 | **hermitage** | 10 | 1,661.93 | 9.59 | 🟢 medium — moderately distinctive | 0.104750 | hermitage, hermitages | — |
| 973 | **vase** | 10 | 1,661.93 | 9.59 | 🟢 medium — moderately distinctive | 0.074978 | - | ~ |
| 974 | **ment** | 10 | 1,661.93 | 9.59 | 🟢 medium — moderately distinctive | 0.139807 | ment, ments | — |
| 975 | **skull-cup** | 10 | 1,661.93 | 9.59 | 🟢 medium — moderately distinctive | - | - | — |
| 976 | **garab** | 10 | 1,661.93 | 9.59 | 🟢 medium — moderately distinctive | 0.038552 | - | ~ |
| 977 | **call** | 18 | 1,658.40 | 5.316469 | 🟢 medium — moderately distinctive | 0.002703 | call, calls | — |
| 978 | **understanding** | 14 | 1,654.78 | 6.820546 | 🟢 medium — moderately distinctive | - | - | — |
| 979 | **freed** | 11 | 1,654.05 | 8.676844 | 🟢 medium — moderately distinctive | - | - | — |
| 980 | **read** | 13 | 1,654.03 | 7.341843 | 🟢 medium — moderately distinctive | 0.061197 | - | — |
| 981 | **followed** | 17 | 1,653.76 | 5.613454 | 🟢 medium — moderately distinctive | - | - | — |
| 982 | **strength** | 16 | 1,647.71 | 5.942477 | 🟢 medium — moderately distinctive | 0.050849 | strength, strengths | — |
| 983 | **among** | 20 | 1,632.58 | 4.710333 | 🟢 medium — moderately distinctive | - | - | — |
| 984 | **examine** | 13 | 1,631.48 | 7.24176 | 🟢 medium — moderately distinctive | 0.066104 | examine, examines | — |
| 985 | **section** | 14 | 1,626.21 | 6.702763 | 🟢 medium — moderately distinctive | 0.060601 | section, sections | — |
| 986 | **run** | 16 | 1,623.59 | 5.855466 | 🟢 medium — moderately distinctive | 0.068970 | run, runs | — |
| 987 | **tendency** | 12 | 1,622.36 | 7.801376 | 🟢 medium — moderately distinctive | 0.074883 | tendencies, tendency | — |
| 988 | **rid** | 11 | 1,619.29 | 8.494523 | 🟢 medium — moderately distinctive | 0.074936 | - | — |
| 989 | **baby** | 11 | 1,619.29 | 8.494523 | 🟢 medium — moderately distinctive | 0.093562 | babies, baby | — |
| 990 | **shoot** | 11 | 1,619.29 | 8.494523 | 🟢 medium — moderately distinctive | 0.117995 | shoot, shoots | — |
| 991 | **passed** | 15 | 1,618.39 | 6.225839 | 🟢 medium — moderately distinctive | - | - | — |
| 992 | **built** | 14 | 1,606.79 | 6.622721 | 🟢 medium — moderately distinctive | - | - | — |
| 993 | **foundation** | 13 | 1,601.40 | 7.108229 | 🟢 medium — moderately distinctive | 0.059855 | foundation, foundations | — |
| 994 | **show** | 20 | 1,594.10 | 4.599307 | 🟢 medium — moderately distinctive | 0.182228 | show, shows | — |
| 995 | **large** | 20 | 1,594.10 | 4.599307 | 🟢 medium — moderately distinctive | 0.035892 | - | — |
| 996 | **indispensable** | 10 | 1,592.21 | 9.18767 | 🟢 medium — moderately distinctive | 0.083682 | - | — |
| 997 | **eaten** | 10 | 1,592.21 | 9.18767 | 🟢 medium — moderately distinctive | - | - | — |
| 998 | **sincerely** | 10 | 1,592.21 | 9.18767 | 🟢 medium — moderately distinctive | 0.083823 | - | — |
| 999 | **concern** | 18 | 1,590.53 | 5.098897 | 🟢 medium — moderately distinctive | 0.073707 | concern, concerns | — |
| 1000 | **advice** | 12 | 1,590.30 | 7.647225 | 🟢 medium — moderately distinctive | 0.060133 | - | — |
| 1001 | **moreover** | 12 | 1,590.30 | 7.647225 | 🟢 medium — moderately distinctive | - | - | — |
| 1002 | **examining** | 12 | 1,590.30 | 7.647225 | 🟢 medium — moderately distinctive | - | - | — |
| 1003 | **disappeared** | 11 | 1,589.91 | 8.340372 | 🟢 medium — moderately distinctive | - | - | — |
| 1004 | **knowing** | 11 | 1,589.91 | 8.340372 | 🟢 medium — moderately distinctive | - | - | — |
| 1005 | **shadow** | 11 | 1,589.91 | 8.340372 | 🟢 medium — moderately distinctive | 0.081984 | shadow, shadows | — |
| 1006 | **purity** | 11 | 1,589.91 | 8.340372 | 🟢 medium — moderately distinctive | 0.067411 | - | ~ |
| 1007 | **house** | 20 | 1,583.69 | 4.569255 | 🟢 medium — moderately distinctive | 0.031977 | - | — |
| 1008 | **often** | 14 | 1,577.52 | 6.502093 | 🟢 medium — moderately distinctive | - | - | — |
| 1009 | **milk** | 12 | 1,575.95 | 7.578232 | 🟢 medium — moderately distinctive | 0.061101 | - | — |
| 1010 | **individual** | 14 | 1,572.07 | 6.47962 | 🟢 medium — moderately distinctive | 0.065000 | individual, individuals | — |
| 1011 | **few** | 18 | 1,570.29 | 5.034009 | 🟢 medium — moderately distinctive | - | - | — |
| 1012 | **disappear** | 11 | 1,564.45 | 8.206841 | 🟢 medium — moderately distinctive | 0.074867 | disappear, disappears | — |
| 1013 | **burning** | 11 | 1,564.45 | 8.206841 | 🟢 medium — moderately distinctive | - | - | — |
| 1014 | **nevertheless** | 12 | 1,562.53 | 7.513694 | 🟢 medium — moderately distinctive | - | - | — |
| 1015 | **fill** | 12 | 1,562.53 | 7.513694 | 🟢 medium — moderately distinctive | 0.031997 | fill, fills | — |
| 1016 | **prevent** | 16 | 1,559.09 | 5.622843 | 🟢 medium — moderately distinctive | 0.050825 | prevent, prevents | — |
| 1017 | **depend** | 14 | 1,556.41 | 6.415081 | 🟢 medium — moderately distinctive | 0.087087 | depend, depends | — |
| 1018 | **line** | 19 | 1,547.23 | 4.699034 | 🟢 medium — moderately distinctive | 0.056530 | line, lines | — |
| 1019 | **invited** | 13 | 1,543.74 | 6.852295 | 🟢 medium — moderately distinctive | - | - | — |
| 1020 | **inward** | 10 | 1,542.35 | 8.899988 | 🟢 medium — moderately distinctive | - | inward, inwards | — |
| 1021 | **transformed** | 10 | 1,542.35 | 8.899988 | 🟢 medium — moderately distinctive | - | - | — |
| 1022 | **created** | 14 | 1,541.70 | 6.354457 | 🟢 medium — moderately distinctive | - | - | — |
| 1023 | **constant** | 12 | 1,538.04 | 7.395911 | 🟢 medium — moderately distinctive | 0.067073 | - | — |
| 1024 | **fell** | 22 | 1,529.42 | 4.01152 | 🟢 medium — moderately distinctive | - | - | — |
| 1025 | **starting** | 15 | 1,512.99 | 5.820374 | 🟢 medium — moderately distinctive | - | - | — |
| 1026 | **involved** | 16 | 1,504.64 | 5.42647 | 🟢 medium — moderately distinctive | - | - | — |
| 1027 | **vital** | 13 | 1,503.88 | 6.675364 | 🟢 medium — moderately distinctive | 0.061399 | - | — |
| 1028 | **bow** | 11 | 1,503.75 | 7.888387 | 🟢 medium — moderately distinctive | 0.074680 | - | — |
| 1029 | **continually** | 10 | 1,503.68 | 8.676844 | 🟢 medium — moderately distinctive | 0.082578 | - | — |
| 1030 | **treat** | 10 | 1,503.68 | 8.676844 | 🟢 medium — moderately distinctive | 0.073961 | - | — |
| 1031 | **phenomena** | 9 | 1,496.23 | 9.593135 | 🟢 medium — moderately distinctive | 0.093828 | - | ~ |
| 1032 | **wander** | 9 | 1,496.23 | 9.593135 | 🟢 medium — moderately distinctive | 0.106129 | wander, wanders | — |
| 1033 | **deaf** | 9 | 1,496.23 | 9.593135 | 🟢 medium — moderately distinctive | 0.093589 | - | — |
| 1034 | **skilled** | 9 | 1,496.23 | 9.593135 | 🟢 medium — moderately distinctive | 0.083368 | - | — |
| 1035 | **caring** | 9 | 1,496.23 | 9.593135 | 🟢 medium — moderately distinctive | - | - | — |
| 1036 | **walking** | 9 | 1,496.23 | 9.593135 | 🟢 medium — moderately distinctive | - | - | ~ |
| 1037 | **victim** | 9 | 1,496.23 | 9.593135 | 🟢 medium — moderately distinctive | 0.140929 | victim, victims | — |
| 1038 | **agony** | 9 | 1,496.23 | 9.593135 | 🟢 medium — moderately distinctive | 0.148567 | agonies, agony | — |
| 1039 | **retribution** | 9 | 1,496.23 | 9.593135 | 🟢 medium — moderately distinctive | 0.094738 | - | ~ |
| 1040 | **auspicious** | 9 | 1,496.23 | 9.593135 | 🟢 medium — moderately distinctive | 0.094813 | - | ~ |
| 1041 | **loving** | 9 | 1,496.23 | 9.593135 | 🟢 medium — moderately distinctive | - | - | — |
| 1042 | **hate** | 9 | 1,496.23 | 9.593135 | 🟢 medium — moderately distinctive | 0.094408 | - | — |
| 1043 | **attainment** | 9 | 1,496.23 | 9.593135 | 🟢 medium — moderately distinctive | 0.173552 | attainment, attainments | ~ |
| 1044 | **distracted** | 9 | 1,495.74 | 9.59 | 🟢 medium — moderately distinctive | - | - | — |
| 1045 | **meritorious** | 9 | 1,495.74 | 9.59 | 🟢 medium — moderately distinctive | 0.094567 | - | — |
| 1046 | **terrifying** | 9 | 1,495.74 | 9.59 | 🟢 medium — moderately distinctive | - | - | — |
| 1047 | **thirty-two** | 9 | 1,495.74 | 9.59 | 🟢 medium — moderately distinctive | - | - | — |
| 1048 | **jambudvipa** | 9 | 1,495.74 | 9.59 | 🟢 medium — moderately distinctive | 0.045437 | - | ✓ འཛམ་བུ་གླིང |
| 1049 | **detsen** | 9 | 1,495.74 | 9.59 | 🟢 medium — moderately distinctive | 0.044019 | - | ~ |
| 1050 | **affliction** | 9 | 1,495.74 | 9.59 | 🟢 medium — moderately distinctive | 0.169919 | affliction, afflictions | — |
| 1051 | **solitude** | 9 | 1,495.74 | 9.59 | 🟢 medium — moderately distinctive | 0.106517 | solitude, solitudes | — |
| 1052 | **delusion** | 9 | 1,495.74 | 9.59 | 🟢 medium — moderately distinctive | 0.140850 | delusion, delusions | — |
| 1053 | **doesn** | 9 | 1,495.74 | 9.59 | 🟢 medium — moderately distinctive | - | - | — |
| 1054 | **remorse** | 9 | 1,495.74 | 9.59 | 🟢 medium — moderately distinctive | 0.093866 | - | — |
| 1055 | **aris** | 9 | 1,495.74 | 9.59 | 🟢 medium — moderately distinctive | - | - | — |
| 1056 | **holy** | 9 | 1,495.74 | 9.59 | 🟢 medium — moderately distinctive | 0.093902 | - | — |
| 1057 | **celestial** | 9 | 1,495.74 | 9.59 | 🟢 medium — moderately distinctive | 0.094583 | - | — |
| 1058 | **arhat** | 9 | 1,495.74 | 9.59 | 🟢 medium — moderately distinctive | 0.056685 | arhat, arhats | ✓ དགྲ་བཅོམ་པ |
| 1059 | **lhasa** | 9 | 1,495.74 | 9.59 | 🟢 medium — moderately distinctive | 0.044230 | - | — |
| 1060 | **corpse** | 9 | 1,495.74 | 9.59 | 🟢 medium — moderately distinctive | 0.086287 | - | — |
| 1061 | **bitch** | 9 | 1,495.74 | 9.59 | 🟢 medium — moderately distinctive | 0.094532 | - | — |
| 1062 | **thangpa** | 9 | 1,495.74 | 9.59 | 🟢 medium — moderately distinctive | 0.044309 | - | ~ |
| 1063 | **thank** | 9 | 1,495.74 | 9.59 | 🟢 medium — moderately distinctive | - | thank, thanks | — |
| 1064 | **solitary** | 9 | 1,495.74 | 9.59 | 🟢 medium — moderately distinctive | 0.094631 | - | — |
| 1065 | **sariputra** | 9 | 1,495.74 | 9.59 | 🟢 medium — moderately distinctive | 0.049153 | - | — |
| 1066 | **virtuous** | 9 | 1,495.74 | 9.59 | 🟢 medium — moderately distinctive | 0.075500 | - | — |
| 1067 | **hors** | 9 | 1,495.74 | 9.59 | 🟢 medium — moderately distinctive | - | - | — |
| 1068 | **nun** | 9 | 1,495.74 | 9.59 | 🟢 medium — moderately distinctive | 0.141716 | nun, nuns | ~ |
| 1069 | **begging** | 9 | 1,495.74 | 9.59 | 🟢 medium — moderately distinctive | - | - | — |
| 1070 | **benefactor** | 9 | 1,495.74 | 9.59 | 🟢 medium — moderately distinctive | 0.172978 | benefactor, benefactors | — |
| 1071 | **feast** | 9 | 1,495.74 | 9.59 | 🟢 medium — moderately distinctive | 0.170151 | feast, feasts | ~ |
| 1072 | **dwell** | 9 | 1,495.74 | 9.59 | 🟢 medium — moderately distinctive | 0.170475 | dwell, dwells | — |
| 1073 | **immaculate** | 9 | 1,495.74 | 9.59 | 🟢 medium — moderately distinctive | 0.075919 | - | — |
| 1074 | **caste** | 9 | 1,495.74 | 9.59 | 🟢 medium — moderately distinctive | 0.094588 | - | — |
| 1075 | **entrust** | 9 | 1,495.74 | 9.59 | 🟢 medium — moderately distinctive | 0.083399 | - | — |
| 1076 | **visualized** | 9 | 1,495.74 | 9.59 | 🟢 medium — moderately distinctive | - | - | — |
| 1077 | **melt** | 9 | 1,495.74 | 9.59 | 🟢 medium — moderately distinctive | 0.142119 | melt, melts | — |
| 1078 | **visualizing** | 9 | 1,495.74 | 9.59 | 🟢 medium — moderately distinctive | - | - | — |
| 1079 | **bhagavan** | 9 | 1,495.74 | 9.59 | 🟢 medium — moderately distinctive | 0.047723 | - | ✓ བཅོམ་ལྡན་འདས |
| 1080 | **immediate** | 15 | 1,492.87 | 5.742988 | 🟢 medium — moderately distinctive | - | - | ~ |
| 1081 | **army** | 11 | 1,487.16 | 7.801376 | 🟢 medium — moderately distinctive | 0.107114 | armies, army | — |
| 1082 | **door** | 12 | 1,487.06 | 7.150788 | 🟢 medium — moderately distinctive | 0.134550 | door, doors | — |
| 1083 | **carry** | 14 | 1,486.61 | 6.127399 | 🟢 medium — moderately distinctive | 0.061427 | carries, carry | — |
| 1084 | **greater** | 16 | 1,485.94 | 5.359029 | 🟢 medium — moderately distinctive | - | - | — |
| 1085 | **necessary** | 16 | 1,483.93 | 5.351808 | 🟢 medium — moderately distinctive | - | - | — |
| 1086 | **representing** | 14 | 1,479.15 | 6.096628 | 🟢 medium — moderately distinctive | - | - | — |
| 1087 | **totally** | 12 | 1,478.21 | 7.108229 | 🟢 medium — moderately distinctive | 0.067717 | - | — |
| 1088 | **error** | 10 | 1,472.09 | 8.494523 | 🟢 medium — moderately distinctive | 0.139152 | error, errors | — |
| 1089 | **learning** | 10 | 1,472.09 | 8.494523 | 🟢 medium — moderately distinctive | - | - | — |
| 1090 | **green** | 12 | 1,469.72 | 7.067407 | 🟢 medium — moderately distinctive | 0.067429 | - | — |
| 1091 | **satisfied** | 13 | 1,464.84 | 6.502093 | 🟢 medium — moderately distinctive | - | - | — |
| 1092 | **equally** | 12 | 1,461.57 | 7.028186 | 🟢 medium — moderately distinctive | 0.067265 | - | — |
| 1093 | **golden** | 12 | 1,461.57 | 7.028186 | 🟢 medium — moderately distinctive | 0.055648 | - | — |
| 1094 | **trust** | 17 | 1,460.78 | 4.958406 | 🟢 medium — moderately distinctive | 0.044108 | - | — |
| 1095 | **possible** | 19 | 1,459.99 | 4.43408 | 🟢 medium — moderately distinctive | - | - | — |
| 1096 | **seat** | 11 | 1,457.78 | 7.647225 | 🟢 medium — moderately distinctive | 0.043340 | - | ~ |
| 1097 | **length** | 11 | 1,457.78 | 7.647225 | 🟢 medium — moderately distinctive | 0.074421 | - | — |
| 1098 | **disease** | 12 | 1,446.16 | 6.954078 | 🟢 medium — moderately distinctive | 0.062788 | - | — |
| 1099 | **medicine** | 10 | 1,445.37 | 8.340372 | 🟢 medium — moderately distinctive | 0.091405 | medicine, medicines | — |
| 1100 | **cushion** | 10 | 1,445.37 | 8.340372 | 🟢 medium — moderately distinctive | 0.139773 | cushion, cushions | — |
| 1101 | **lie** | 10 | 1,445.37 | 8.340372 | 🟢 medium — moderately distinctive | 0.033191 | - | — |
| 1102 | **beauty** | 10 | 1,445.37 | 8.340372 | 🟢 medium — moderately distinctive | 0.055430 | - | — |
| 1103 | **crushed** | 10 | 1,445.37 | 8.340372 | 🟢 medium — moderately distinctive | - | - | — |
| 1104 | **region** | 14 | 1,444.92 | 5.955549 | 🟢 medium — moderately distinctive | 0.068956 | region, regions | — |
| 1105 | **exactly** | 11 | 1,444.62 | 7.578232 | 🟢 medium — moderately distinctive | - | - | — |
| 1106 | **ago** | 19 | 1,437.15 | 4.364704 | 🟢 medium — moderately distinctive | 0.037959 | - | — |
| 1107 | **poured** | 9 | 1,432.99 | 9.18767 | 🟢 medium — moderately distinctive | - | - | — |
| 1108 | **illusion** | 9 | 1,432.99 | 9.18767 | 🟢 medium — moderately distinctive | 0.094707 | illusion, illusions | — |
| 1109 | **surface** | 11 | 1,432.32 | 7.513694 | 🟢 medium — moderately distinctive | 0.090363 | surface, surfaces | — |
| 1110 | **drop** | 18 | 1,431.54 | 4.589189 | 🟢 medium — moderately distinctive | 0.057167 | drop, drops | — |
| 1111 | **arisen** | 10 | 1,422.23 | 8.206841 | 🟢 medium — moderately distinctive | - | - | — |
| 1112 | **strive** | 10 | 1,422.23 | 8.206841 | 🟢 medium — moderately distinctive | 0.082330 | - | — |
| 1113 | **position** | 17 | 1,410.91 | 4.789114 | 🟢 medium — moderately distinctive | 0.050057 | position, positions | — |
| 1114 | **rule** | 13 | 1,410.51 | 6.260931 | 🟢 medium — moderately distinctive | 0.112965 | rule, rules | — |
| 1115 | **arising** | 11 | 1,409.87 | 7.395911 | 🟢 medium — moderately distinctive | - | - | — |
| 1116 | **today** | 24 | 1,407.69 | 3.384545 | 🟢 medium — moderately distinctive | 0.024230 | - | — |
| 1117 | **carried** | 13 | 1,402.60 | 6.225839 | 🟢 medium — moderately distinctive | - | - | — |
| 1118 | **repeat** | 10 | 1,401.82 | 8.089058 | 🟢 medium — moderately distinctive | 0.093251 | repeat, repeats | — |
| 1119 | **sight** | 11 | 1,399.56 | 7.341843 | 🟢 medium — moderately distinctive | 0.066914 | - | — |
| 1120 | **return** | 16 | 1,398.73 | 5.044535 | 🟢 medium — moderately distinctive | 0.050426 | return, returns | — |
| 1121 | **established** | 13 | 1,394.97 | 6.191938 | 🟢 medium — moderately distinctive | - | - | — |
| 1122 | **especially** | 14 | 1,390.78 | 5.732405 | 🟢 medium — moderately distinctive | - | - | — |
| 1123 | **faithful** | 9 | 1,388.12 | 8.899988 | 🟢 medium — moderately distinctive | 0.094756 | - | — |
| 1124 | **outward** | 9 | 1,388.12 | 8.899988 | 🟢 medium — moderately distinctive | 0.108435 | outward, outwards | — |
| 1125 | **touching** | 9 | 1,388.12 | 8.899988 | 🟢 medium — moderately distinctive | - | - | — |
| 1126 | **peaceful** | 9 | 1,388.12 | 8.899988 | 🟢 medium — moderately distinctive | 0.094181 | - | — |
| 1127 | **conviction** | 9 | 1,388.12 | 8.899988 | 🟢 medium — moderately distinctive | 0.093109 | - | — |
| 1128 | **highest** | 13 | 1,383.98 | 6.143148 | 🟢 medium — moderately distinctive | - | - | — |
| 1129 | **driven** | 10 | 1,383.56 | 7.983697 | 🟢 medium — moderately distinctive | - | - | — |
| 1130 | **gesture** | 10 | 1,383.56 | 7.983697 | 🟢 medium — moderately distinctive | 0.093323 | gesture, gestures | — |
| 1131 | **building** | 14 | 1,378.34 | 5.681112 | 🟢 medium — moderately distinctive | 0.261244 | building, buildings | — |
| 1132 | **turning** | 12 | 1,377.25 | 6.622721 | 🟢 medium — moderately distinctive | - | turning, turnings | — |
| 1133 | **apart** | 11 | 1,371.61 | 7.19524 | 🟢 medium — moderately distinctive | - | - | — |
| 1134 | **comfortable** | 10 | 1,367.04 | 7.888387 | 🟢 medium — moderately distinctive | 0.083399 | - | — |
| 1135 | **described** | 13 | 1,366.77 | 6.066775 | 🟢 medium — moderately distinctive | - | - | — |
| 1136 | **outside** | 14 | 1,355.21 | 5.585802 | 🟢 medium — moderately distinctive | - | - | — |
| 1137 | **accept** | 14 | 1,355.21 | 5.585802 | 🟢 medium — moderately distinctive | 0.055993 | - | — |
| 1138 | **served** | 11 | 1,355.03 | 7.108229 | 🟢 medium — moderately distinctive | - | - | — |
| 1139 | **swept** | 9 | 1,353.31 | 8.676844 | 🟢 medium — moderately distinctive | - | - | — |
| 1140 | **appearing** | 9 | 1,353.31 | 8.676844 | 🟢 medium — moderately distinctive | - | - | — |
| 1141 | **sand** | 10 | 1,351.96 | 7.801376 | 🟢 medium — moderately distinctive | 0.093792 | sand, sands | — |
| 1142 | **contain** | 11 | 1,347.25 | 7.067407 | 🟢 medium — moderately distinctive | - | contain, contains | — |
| 1143 | **sound** | 11 | 1,339.77 | 7.028186 | 🟢 medium — moderately distinctive | 0.102770 | sound, sounds | — |
| 1144 | **involve** | 11 | 1,339.77 | 7.028186 | 🟢 medium — moderately distinctive | 0.047152 | involve, involves | — |
| 1145 | **caused** | 15 | 1,338.85 | 5.150484 | 🟢 medium — moderately distinctive | - | - | — |
| 1146 | **yellow** | 10 | 1,338.09 | 7.721333 | 🟢 medium — moderately distinctive | 0.083591 | - | ~ |
| 1147 | **union** | 17 | 1,333.80 | 4.527381 | 🟢 medium — moderately distinctive | 0.045908 | union, unions | ~ |
| 1148 | **degenerate** | 8 | 1,329.98 | 9.593135 | 🟢 medium — moderately distinctive | 0.108300 | - | ~ |
| 1149 | **criticize** | 8 | 1,329.98 | 9.593135 | 🟢 medium — moderately distinctive | 0.105987 | - | — |
| 1150 | **sens** | 8 | 1,329.98 | 9.593135 | 🟢 medium — moderately distinctive | - | - | — |
| 1151 | **lip** | 8 | 1,329.98 | 9.593135 | 🟢 medium — moderately distinctive | 0.123628 | lip, lips | — |
| 1152 | **burnt** | 8 | 1,329.98 | 9.593135 | 🟢 medium — moderately distinctive | - | - | ~ |
| 1153 | **ate** | 8 | 1,329.98 | 9.593135 | 🟢 medium — moderately distinctive | - | - | — |
| 1154 | **steal** | 8 | 1,329.98 | 9.593135 | 🟢 medium — moderately distinctive | 0.123041 | steal, steals | — |
| 1155 | **worthless** | 8 | 1,329.98 | 9.593135 | 🟢 medium — moderately distinctive | 0.107567 | - | — |
| 1156 | **beating** | 8 | 1,329.98 | 9.593135 | 🟢 medium — moderately distinctive | 0.205096 | - | — |
| 1157 | **perhap** | 8 | 1,329.54 | 9.59 | 🟢 medium — moderately distinctive | - | - | — |
| 1158 | **believing** | 8 | 1,329.54 | 9.59 | 🟢 medium — moderately distinctive | - | - | — |
| 1159 | **beside** | 8 | 1,329.54 | 9.59 | 🟢 medium — moderately distinctive | - | beside, besides | — |
| 1160 | **endure** | 8 | 1,329.54 | 9.59 | 🟢 medium — moderately distinctive | 0.108036 | endure, endures | — |
| 1161 | **henchmen** | 8 | 1,329.54 | 9.59 | 🟢 medium — moderately distinctive | - | - | — |
| 1162 | **trisong** | 8 | 1,329.54 | 9.59 | 🟢 medium — moderately distinctive | 0.052034 | - | ~ |
| 1163 | **naga** | 8 | 1,329.54 | 9.59 | 🟢 medium — moderately distinctive | 0.172251 | naga, nagas | ✓ ཀླུ |
| 1164 | **ambrosia** | 8 | 1,329.54 | 9.59 | 🟢 medium — moderately distinctive | 0.123573 | ambrosia, ambrosias | ✓ བདུད་རྩི |
| 1165 | **scripture** | 8 | 1,329.54 | 9.59 | 🟢 medium — moderately distinctive | - | - | — |
| 1166 | **eighteen** | 8 | 1,329.54 | 9.59 | 🟢 medium — moderately distinctive | 0.106931 | - | — |
| 1167 | **endlessly** | 8 | 1,329.54 | 9.59 | 🟢 medium — moderately distinctive | 0.107555 | - | — |
| 1168 | **cry** | 8 | 1,329.54 | 9.59 | 🟢 medium — moderately distinctive | 0.083349 | cries, cry | — |
| 1169 | **sentient** | 8 | 1,329.54 | 9.59 | 🟢 medium — moderately distinctive | 0.108058 | - | — |
| 1170 | **maitreya** | 8 | 1,329.54 | 9.59 | 🟢 medium — moderately distinctive | 0.052242 | - | ✓ བྱམས་པ |
| 1171 | **husband** | 8 | 1,329.54 | 9.59 | 🟢 medium — moderately distinctive | 0.122278 | husband, husbands | — |
| 1172 | **monastery** | 8 | 1,329.54 | 9.59 | 🟢 medium — moderately distinctive | 0.114493 | monasteries, monastery | ~ |
| 1173 | **hous** | 8 | 1,329.54 | 9.59 | 🟢 medium — moderately distinctive | - | - | — |
| 1174 | **lap** | 8 | 1,329.54 | 9.59 | 🟢 medium — moderately distinctive | 0.123164 | lap, laps | — |
| 1175 | **blessed** | 8 | 1,329.54 | 9.59 | 🟢 medium — moderately distinctive | - | - | — |
| 1176 | **maudgalyayana** | 8 | 1,329.54 | 9.59 | 🟢 medium — moderately distinctive | 0.058914 | - | ✓ མོའུ་འགལ་གྱི་བུ |
| 1177 | **samsaric** | 8 | 1,329.54 | 9.59 | 🟢 medium — moderately distinctive | 0.107472 | - | — |
| 1178 | **ripened** | 8 | 1,329.54 | 9.59 | 🟢 medium — moderately distinctive | - | - | — |
| 1179 | **tiniest** | 8 | 1,329.54 | 9.59 | 🟢 medium — moderately distinctive | 0.108121 | - | — |
| 1180 | **didn** | 8 | 1,329.54 | 9.59 | 🟢 medium — moderately distinctive | - | - | — |
| 1181 | **mouthful** | 8 | 1,329.54 | 9.59 | 🟢 medium — moderately distinctive | 0.108008 | - | — |
| 1182 | **tsampa** | 8 | 1,329.54 | 9.59 | 🟢 medium — moderately distinctive | 0.107828 | - | ✓ རྩམ་པ |
| 1183 | **langri** | 8 | 1,329.54 | 9.59 | 🟢 medium — moderately distinctive | 0.052394 | - | ~ |
| 1184 | **covetousness** | 8 | 1,329.54 | 9.59 | 🟢 medium — moderately distinctive | 0.107598 | - | — |
| 1185 | **silken** | 8 | 1,329.54 | 9.59 | 🟢 medium — moderately distinctive | 0.108352 | - | — |
| 1186 | **inseparable** | 8 | 1,329.54 | 9.59 | 🟢 medium — moderately distinctive | 0.108342 | - | ~ |
| 1187 | **prajnaparamita** | 8 | 1,329.54 | 9.59 | 🟢 medium — moderately distinctive | 0.051658 | - | — |
| 1188 | **padma** | 8 | 1,329.54 | 9.59 | 🟢 medium — moderately distinctive | 0.052722 | - | ✓ པདྨ |
| 1189 | **chekawa** | 8 | 1,329.54 | 9.59 | 🟢 medium — moderately distinctive | 0.064999 | - | ~ |
| 1190 | **manjusrimitra** | 8 | 1,329.54 | 9.59 | 🟢 medium — moderately distinctive | 0.060847 | - | — |
| 1191 | **strong** | 17 | 1,328.27 | 4.50863 | 🟢 medium — moderately distinctive | 0.043822 | - | — |
| 1192 | **posture** | 9 | 1,324.88 | 8.494523 | 🟢 medium — moderately distinctive | 0.108410 | - | ~ |
| 1193 | **change** | 17 | 1,316.65 | 4.469171 | 🟢 medium — moderately distinctive | 0.049612 | change, changes | — |
| 1194 | **goal** | 12 | 1,313.46 | 6.31599 | 🟢 medium — moderately distinctive | 0.101532 | goal, goals | ~ |
| 1195 | **evening** | 10 | 1,313.29 | 7.578232 | 🟢 medium — moderately distinctive | 0.083448 | - | — |
| 1196 | **danger** | 11 | 1,312.49 | 6.885085 | 🟢 medium — moderately distinctive | 0.117540 | danger, dangers | — |
| 1197 | **break** | 12 | 1,309.57 | 6.297298 | 🟢 medium — moderately distinctive | 0.080544 | break, breaks | — |
| 1198 | **standing** | 10 | 1,302.11 | 7.513694 | 🟢 medium — moderately distinctive | - | - | — |
| 1199 | **dry** | 12 | 1,302.01 | 6.260931 | 🟢 medium — moderately distinctive | 0.067268 | - | — |
| 1200 | **male** | 9 | 1,300.83 | 8.340372 | 🟢 medium — moderately distinctive | 0.106580 | male, males | — |
| 1201 | **lifestyle** | 9 | 1,300.83 | 8.340372 | 🟢 medium — moderately distinctive | 0.137981 | lifestyle, lifestyles | — |
| 1202 | **lacking** | 9 | 1,300.83 | 8.340372 | 🟢 medium — moderately distinctive | - | - | — |
| 1203 | **destroyed** | 11 | 1,300.19 | 6.820546 | 🟢 medium — moderately distinctive | - | - | — |
| 1204 | **wood** | 11 | 1,294.32 | 6.789775 | 🟢 medium — moderately distinctive | 0.081963 | wood, woods | — |
| 1205 | **named** | 13 | 1,293.82 | 5.742988 | 🟢 medium — moderately distinctive | - | - | — |
| 1206 | **exist** | 10 | 1,291.60 | 7.453069 | 🟢 medium — moderately distinctive | 0.102658 | exist, exists | — |
| 1207 | **performed** | 10 | 1,291.60 | 7.453069 | 🟢 medium — moderately distinctive | - | - | — |
| 1208 | **stand** | 12 | 1,291.16 | 6.208745 | 🟢 medium — moderately distinctive | 0.083846 | stand, stands | — |
| 1209 | **finding** | 11 | 1,283.10 | 6.730934 | 🟢 medium — moderately distinctive | - | - | — |
| 1210 | **bigger** | 10 | 1,281.70 | 7.395911 | 🟢 medium — moderately distinctive | - | - | — |
| 1211 | **harming** | 9 | 1,280.01 | 8.206841 | 🟢 medium — moderately distinctive | - | - | — |
| 1212 | **thrown** | 9 | 1,280.01 | 8.206841 | 🟢 medium — moderately distinctive | - | - | — |
| 1213 | **sitting** | 9 | 1,280.01 | 8.206841 | 🟢 medium — moderately distinctive | - | - | — |
| 1214 | **skill** | 8 | 1,273.77 | 9.18767 | 🟢 medium — moderately distinctive | 0.095410 | - | — |
| 1215 | **taste** | 8 | 1,273.77 | 9.18767 | 🟢 medium — moderately distinctive | 0.107314 | - | — |
| 1216 | **encounter** | 8 | 1,273.77 | 9.18767 | 🟢 medium — moderately distinctive | 0.143809 | encounter, encounters | — |
| 1217 | **inspire** | 8 | 1,273.77 | 9.18767 | 🟢 medium — moderately distinctive | 0.107246 | - | — |
| 1218 | **nowhere** | 8 | 1,273.77 | 9.18767 | 🟢 medium — moderately distinctive | - | - | — |
| 1219 | **butcher** | 8 | 1,273.77 | 9.18767 | 🟢 medium — moderately distinctive | 0.107522 | - | — |
| 1220 | **tiny** | 8 | 1,273.77 | 9.18767 | 🟢 medium — moderately distinctive | 0.107853 | - | — |
| 1221 | **unpleasant** | 8 | 1,273.77 | 9.18767 | 🟢 medium — moderately distinctive | 0.107670 | - | — |
| 1222 | **term** | 15 | 1,271.83 | 4.892655 | 🟢 medium — moderately distinctive | 0.094965 | term, terms | — |
| 1223 | **manner** | 10 | 1,263.44 | 7.29055 | 🟢 medium — moderately distinctive | 0.083536 | - | — |
| 1224 | **process** | 13 | 1,260.47 | 5.594934 | 🟢 medium — moderately distinctive | 0.067733 | process, processes | ~ |
| 1225 | **owner** | 11 | 1,257.65 | 6.597403 | 🟢 medium — moderately distinctive | 0.138586 | owner, owners | ~ |
| 1226 | **stage** | 12 | 1,255.61 | 6.037787 | 🟢 medium — moderately distinctive | 0.101194 | stage, stages | — |
| 1227 | **east** | 14 | 1,251.03 | 5.156384 | 🟢 medium — moderately distinctive | 0.046253 | - | — |
| 1228 | **simple** | 9 | 1,245.20 | 7.983697 | 🟢 medium — moderately distinctive | 0.094256 | - | — |
| 1229 | **slip** | 9 | 1,245.20 | 7.983697 | 🟢 medium — moderately distinctive | 0.093631 | - | — |
| 1230 | **meet** | 15 | 1,244.92 | 4.789114 | 🟢 medium — moderately distinctive | 0.035821 | - | — |
| 1231 | **kept** | 11 | 1,239.48 | 6.502093 | 🟢 medium — moderately distinctive | - | - | — |
| 1232 | **covered** | 11 | 1,239.48 | 6.502093 | 🟢 medium — moderately distinctive | - | - | — |
| 1233 | **separate** | 12 | 1,238.50 | 5.955549 | 🟢 medium — moderately distinctive | 0.067561 | - | — |
| 1234 | **loose** | 8 | 1,233.88 | 8.899988 | 🟢 medium — moderately distinctive | 0.107100 | - | — |
| 1235 | **whatsoever** | 8 | 1,233.88 | 8.899988 | 🟢 medium — moderately distinctive | 0.108204 | - | — |
| 1236 | **twenty** | 8 | 1,233.88 | 8.899988 | 🟢 medium — moderately distinctive | - | - | ~ |
| 1237 | **crime** | 8 | 1,233.88 | 8.899988 | 🟢 medium — moderately distinctive | 0.123834 | crime, crimes | — |
| 1238 | **committing** | 8 | 1,233.88 | 8.899988 | 🟢 medium — moderately distinctive | - | - | — |
| 1239 | **expression** | 8 | 1,233.88 | 8.899988 | 🟢 medium — moderately distinctive | 0.123604 | expression, expressions | ~ |
| 1240 | **reflecting** | 12 | 1,233.10 | 5.929574 | 🟢 medium — moderately distinctive | - | - | — |
| 1241 | **ability** | 12 | 1,233.10 | 5.929574 | 🟢 medium — moderately distinctive | 0.074737 | abilities, ability | — |
| 1242 | **close** | 16 | 1,231.87 | 4.442738 | 🟢 medium — moderately distinctive | 0.039094 | - | ~ |
| 1243 | **trouble** | 10 | 1,231.84 | 7.108229 | 🟢 medium — moderately distinctive | 0.092090 | trouble, troubles | — |
| 1244 | **sent** | 12 | 1,230.45 | 5.916835 | 🟢 medium — moderately distinctive | - | - | — |
| 1245 | **applying** | 9 | 1,230.34 | 7.888387 | 🟢 medium — moderately distinctive | - | - | — |
| 1246 | **breach** | 9 | 1,230.34 | 7.888387 | 🟢 medium — moderately distinctive | - | - | — |
| 1247 | **less** | 16 | 1,227.88 | 4.428349 | 🟢 medium — moderately distinctive | - | - | — |
| 1248 | **gone** | 10 | 1,217.97 | 7.028186 | 🟢 medium — moderately distinctive | - | - | — |
| 1249 | **establish** | 11 | 1,211.34 | 6.354457 | 🟢 medium — moderately distinctive | 0.061699 | establish, establishes | — |
| 1250 | **felt** | 11 | 1,207.64 | 6.335039 | 🟢 medium — moderately distinctive | - | - | — |
| 1251 | **speaking** | 12 | 1,203.34 | 5.786473 | 🟢 medium — moderately distinctive | - | - | — |
| 1252 | **seal** | 8 | 1,202.95 | 8.676844 | 🟢 medium — moderately distinctive | 0.108488 | - | — |
| 1253 | **behaviour** | 8 | 1,202.95 | 8.676844 | 🟢 medium — moderately distinctive | 0.107761 | - | — |
| 1254 | **cosmo** | 8 | 1,202.95 | 8.676844 | 🟢 medium — moderately distinctive | - | - | — |
| 1255 | **attribute** | 8 | 1,202.95 | 8.676844 | 🟢 medium — moderately distinctive | - | - | — |
| 1256 | **peace** | 8 | 1,202.95 | 8.676844 | 🟢 medium — moderately distinctive | 0.108122 | - | — |
| 1257 | **link** | 10 | 1,199.05 | 6.918987 | 🟢 medium — moderately distinctive | 0.083842 | - | — |
| 1258 | **cross** | 10 | 1,193.17 | 6.885085 | 🟢 medium — moderately distinctive | 0.093988 | cross, crosses | — |
| 1259 | **proper** | 9 | 1,192.73 | 7.647225 | 🟢 medium — moderately distinctive | 0.094593 | - | — |
| 1260 | **nobody** | 9 | 1,192.73 | 7.647225 | 🟢 medium — moderately distinctive | - | - | — |
| 1261 | **cutting** | 12 | 1,192.10 | 5.732405 | 🟢 medium — moderately distinctive | - | - | — |
| 1262 | **containing** | 10 | 1,181.99 | 6.820546 | 🟢 medium — moderately distinctive | - | - | — |
| 1263 | **broken** | 10 | 1,181.99 | 6.820546 | 🟢 medium — moderately distinctive | - | - | — |
| 1264 | **explaining** | 9 | 1,181.96 | 7.578232 | 🟢 medium — moderately distinctive | - | - | — |
| 1265 | **pull** | 9 | 1,181.96 | 7.578232 | 🟢 medium — moderately distinctive | 0.106303 | pull, pulls | — |
| 1266 | **trace** | 8 | 1,177.67 | 8.494523 | 🟢 medium — moderately distinctive | 0.107658 | - | — |
| 1267 | **property** | 12 | 1,173.28 | 5.641891 | 🟢 medium — moderately distinctive | 0.074053 | properties, property | — |
| 1268 | **serious** | 12 | 1,173.28 | 5.641891 | 🟢 medium — moderately distinctive | - | - | — |
| 1269 | **bringing** | 11 | 1,171.06 | 6.143148 | 🟢 medium — moderately distinctive | - | - | — |
| 1270 | **debt** | 16 | 1,169.52 | 4.217857 | 🟢 medium — moderately distinctive | 0.054695 | debt, debts | — |
| 1271 | **flow** | 12 | 1,165.43 | 5.604151 | 🟢 medium — moderately distinctive | 0.101613 | flow, flows | — |
| 1272 | **glad** | 7 | 1,163.73 | 9.593135 | 🟢 medium — moderately distinctive | 0.125253 | - | — |
| 1273 | **technique** | 7 | 1,163.73 | 9.593135 | 🟢 medium — moderately distinctive | 0.176554 | technique, techniques | — |
| 1274 | **sad** | 7 | 1,163.73 | 9.593135 | 🟢 medium — moderately distinctive | 0.125498 | - | — |
| 1275 | **stupid** | 7 | 1,163.73 | 9.593135 | 🟢 medium — moderately distinctive | 0.124593 | - | — |
| 1276 | **threw** | 7 | 1,163.73 | 9.593135 | 🟢 medium — moderately distinctive | - | - | — |
| 1277 | **poisonous** | 7 | 1,163.73 | 9.593135 | 🟢 medium — moderately distinctive | 0.125227 | - | — |
| 1278 | **beg** | 7 | 1,163.73 | 9.593135 | 🟢 medium — moderately distinctive | 0.094506 | - | — |
| 1279 | **sore** | 7 | 1,163.73 | 9.593135 | 🟢 medium — moderately distinctive | 0.219609 | sore, sores | — |
| 1280 | **garland** | 7 | 1,163.73 | 9.593135 | 🟢 medium — moderately distinctive | 0.172031 | garland, garlands | — |
| 1281 | **infinity** | 7 | 1,163.73 | 9.593135 | 🟢 medium — moderately distinctive | 0.125545 | - | — |
| 1282 | **herself** | 7 | 1,163.73 | 9.593135 | 🟢 medium — moderately distinctive | - | - | — |
| 1283 | **multitude** | 7 | 1,163.73 | 9.593135 | 🟢 medium — moderately distinctive | 0.146440 | multitude, multitudes | — |
| 1284 | **discover** | 7 | 1,163.73 | 9.593135 | 🟢 medium — moderately distinctive | 0.125529 | - | — |
| 1285 | **avalokitesvara** | 7 | 1,163.35 | 9.59 | 🟢 medium — moderately distinctive | 0.063944 | - | — |
| 1286 | **longchenpa** | 7 | 1,163.35 | 9.59 | 🟢 medium — moderately distinctive | 0.068186 | - | ✓ ཀློང་ཆེན་རབ་འབྱམས་པ |
| 1287 | **habitual** | 7 | 1,163.35 | 9.59 | 🟢 medium — moderately distinctive | 0.110437 | - | ~ |
| 1288 | **dedicating** | 7 | 1,163.35 | 9.59 | 🟢 medium — moderately distinctive | - | - | — |
| 1289 | **padmasambhava** | 7 | 1,163.35 | 9.59 | 🟢 medium — moderately distinctive | 0.062531 | - | ~ |
| 1290 | **hungry** | 7 | 1,163.35 | 9.59 | 🟢 medium — moderately distinctive | 0.124765 | - | — |
| 1291 | **forgetting** | 7 | 1,163.35 | 9.59 | 🟢 medium — moderately distinctive | - | - | — |
| 1292 | **smell** | 7 | 1,163.35 | 9.59 | 🟢 medium — moderately distinctive | 0.146172 | smell, smells | — |
| 1293 | **deluded** | 7 | 1,163.35 | 9.59 | 🟢 medium — moderately distinctive | - | - | — |
| 1294 | **rope** | 7 | 1,163.35 | 9.59 | 🟢 medium — moderately distinctive | 0.145123 | rope, ropes | — |
| 1295 | **layman** | 7 | 1,163.35 | 9.59 | 🟢 medium — moderately distinctive | 0.125172 | - | — |
| 1296 | **mastered** | 7 | 1,163.35 | 9.59 | 🟢 medium — moderately distinctive | - | - | — |
| 1297 | **vinaya** | 7 | 1,163.35 | 9.59 | 🟢 medium — moderately distinctive | 0.062733 | - | ✓ འདུལ་བ |
| 1298 | **atra** | 7 | 1,163.35 | 9.59 | 🟢 medium — moderately distinctive | 0.125341 | - | — |
| 1299 | **songtsen** | 7 | 1,163.35 | 9.59 | 🟢 medium — moderately distinctive | 0.060538 | - | ~ |
| 1300 | **gampo** | 7 | 1,163.35 | 9.59 | 🟢 medium — moderately distinctive | 0.060557 | - | ~ |
| 1301 | **tibetan** | 7 | 1,163.35 | 9.59 | 🟢 medium — moderately distinctive | 0.090040 | tibetan, tibetans | — |
| 1302 | **begged** | 7 | 1,163.35 | 9.59 | 🟢 medium — moderately distinctive | - | - | — |
| 1303 | **everyday** | 7 | 1,163.35 | 9.59 | 🟢 medium — moderately distinctive | 0.125849 | - | — |
| 1304 | **aroused** | 7 | 1,163.35 | 9.59 | 🟢 medium — moderately distinctive | - | - | — |
| 1305 | **ripen** | 7 | 1,163.35 | 9.59 | 🟢 medium — moderately distinctive | 0.107624 | ripen, ripens | — |
| 1306 | **ancient** | 7 | 1,163.35 | 9.59 | 🟢 medium — moderately distinctive | 0.098045 | - | ~ |
| 1307 | **magical** | 7 | 1,163.35 | 9.59 | 🟢 medium — moderately distinctive | 0.125891 | - | — |
| 1308 | **needle** | 7 | 1,163.35 | 9.59 | 🟢 medium — moderately distinctive | 0.145864 | needle, needles | — |
| 1309 | **kadampa** | 7 | 1,163.35 | 9.59 | 🟢 medium — moderately distinctive | 0.221625 | kadampa, kadampas | ✓ བཀའ་གདམས་པ |
| 1310 | **katyayana** | 7 | 1,163.35 | 9.59 | 🟢 medium — moderately distinctive | 0.065110 | - | ✓ |
| 1311 | **dear** | 7 | 1,163.35 | 9.59 | 🟢 medium — moderately distinctive | 0.125878 | - | — |
| 1312 | **clinging** | 7 | 1,163.35 | 9.59 | 🟢 medium — moderately distinctive | - | clinging, clingings | ✓ འཛིན་པ |
| 1313 | **answered** | 7 | 1,163.35 | 9.59 | 🟢 medium — moderately distinctive | - | - | — |
| 1314 | **fool** | 7 | 1,163.35 | 9.59 | 🟢 medium — moderately distinctive | 0.175572 | fool, fools | — |
| 1315 | **pus** | 7 | 1,163.35 | 9.59 | 🟢 medium — moderately distinctive | 0.125436 | - | — |
| 1316 | **forehead** | 7 | 1,163.35 | 9.59 | 🟢 medium — moderately distinctive | 0.146358 | forehead, foreheads | — |
| 1317 | **girl** | 7 | 1,163.35 | 9.59 | 🟢 medium — moderately distinctive | 0.146325 | girl, girls | — |
| 1318 | **lala** | 7 | 1,163.35 | 9.59 | 🟢 medium — moderately distinctive | 0.178791 | lala, lalas | — |
| 1319 | **medicinal** | 7 | 1,163.35 | 9.59 | 🟢 medium — moderately distinctive | 0.125254 | - | — |
| 1320 | **praying** | 7 | 1,163.35 | 9.59 | 🟢 medium — moderately distinctive | - | - | — |
| 1321 | **marvellous** | 7 | 1,163.35 | 9.59 | 🟢 medium — moderately distinctive | 0.110709 | - | — |
| 1322 | **lhodrak** | 7 | 1,163.35 | 9.59 | 🟢 medium — moderately distinctive | 0.062478 | - | — |
| 1323 | **vimalamitra** | 7 | 1,163.35 | 9.59 | 🟢 medium — moderately distinctive | 0.063954 | - | ✓ དྲི་མེད་བཤེས་གཉེན |
| 1324 | **primordial** | 7 | 1,163.35 | 9.59 | 🟢 medium — moderately distinctive | 0.126075 | - | ~ |
| 1325 | **symboliz** | 7 | 1,163.35 | 9.59 | 🟢 medium — moderately distinctive | - | - | — |
| 1326 | **stupa** | 7 | 1,163.35 | 9.59 | 🟢 medium — moderately distinctive | 0.110471 | - | ✓ མཆོད་རྟེན |
| 1327 | **sharawa** | 7 | 1,163.35 | 9.59 | 🟢 medium — moderately distinctive | 0.068039 | - | ✓ ཤ་ར་བ |
| 1328 | **gift** | 7 | 1,163.35 | 9.59 | 🟢 medium — moderately distinctive | 0.176150 | gift, gifts | — |
| 1329 | **atiyoga** | 7 | 1,163.35 | 9.59 | 🟢 medium — moderately distinctive | 0.068765 | - | ✓ |
| 1330 | **amount** | 15 | 1,163.30 | 4.475141 | 🟢 medium — moderately distinctive | - | amount, amounts | — |
| 1331 | **minor** | 9 | 1,162.44 | 7.453069 | 🟢 medium — moderately distinctive | 0.094515 | - | ~ |
| 1332 | **language** | 9 | 1,162.44 | 7.453069 | 🟢 medium — moderately distinctive | 0.121017 | language, languages | — |
| 1333 | **snow** | 9 | 1,162.44 | 7.453069 | 🟢 medium — moderately distinctive | 0.099879 | snow, snows | — |
| 1334 | **naturally** | 8 | 1,156.30 | 8.340372 | 🟢 medium — moderately distinctive | 0.107449 | - | — |
| 1335 | **refer** | 8 | 1,156.30 | 8.340372 | 🟢 medium — moderately distinctive | 0.122194 | refer, refers | — |
| 1336 | **dedicated** | 8 | 1,156.30 | 8.340372 | 🟢 medium — moderately distinctive | - | - | — |
| 1337 | **bit** | 10 | 1,152.21 | 6.648696 | 🟢 medium — moderately distinctive | 0.103440 | bit, bits | — |
| 1338 | **convinced** | 10 | 1,147.71 | 6.622721 | 🟢 medium — moderately distinctive | - | - | — |
| 1339 | **nine** | 19 | 1,139.53 | 3.460822 | 🟢 medium — moderately distinctive | - | - | ~ |
| 1340 | **period** | 17 | 1,139.52 | 3.867917 | 🟢 medium — moderately distinctive | 0.061178 | period, periods | — |
| 1341 | **meal** | 10 | 1,139.04 | 6.57271 | 🟢 medium — moderately distinctive | 0.092095 | meal, meals | — |
| 1342 | **plain** | 8 | 1,137.78 | 8.206841 | 🟢 medium — moderately distinctive | 0.122724 | plain, plains | — |
| 1343 | **confusion** | 8 | 1,137.78 | 8.206841 | 🟢 medium — moderately distinctive | 0.108287 | - | — |
| 1344 | **deeply** | 8 | 1,137.78 | 8.206841 | 🟢 medium — moderately distinctive | 0.107003 | - | — |
| 1345 | **correspond** | 8 | 1,137.78 | 8.206841 | 🟢 medium — moderately distinctive | 0.172090 | correspond, corresponds | — |
| 1346 | **rainbow** | 8 | 1,137.78 | 8.206841 | 🟢 medium — moderately distinctive | 0.108367 | - | — |
| 1347 | **identical** | 8 | 1,137.78 | 8.206841 | 🟢 medium — moderately distinctive | 0.108367 | - | — |
| 1348 | **check** | 9 | 1,137.10 | 7.29055 | 🟢 medium — moderately distinctive | 0.094072 | - | — |
| 1349 | **seek** | 13 | 1,134.10 | 5.034009 | 🟢 medium — moderately distinctive | 0.055707 | - | — |
| 1350 | **universal** | 9 | 1,129.49 | 7.24176 | 🟢 medium — moderately distinctive | 0.083209 | - | ~ |
| 1351 | **summer** | 11 | 1,125.52 | 5.904256 | 🟢 medium — moderately distinctive | 0.073931 | - | — |
| 1352 | **lost** | 12 | 1,125.28 | 5.411085 | 🟢 medium — moderately distinctive | - | - | — |
| 1353 | **trial** | 8 | 1,121.46 | 8.089058 | 🟢 medium — moderately distinctive | - | - | — |
| 1354 | **remedy** | 8 | 1,121.46 | 8.089058 | 🟢 medium — moderately distinctive | 0.108324 | - | — |
| 1355 | **ride** | 8 | 1,121.46 | 8.089058 | 🟢 medium — moderately distinctive | 0.123545 | ride, rides | — |
| 1356 | **occasion** | 8 | 1,121.46 | 8.089058 | 🟢 medium — moderately distinctive | 0.173040 | occasion, occasions | — |
| 1357 | **disc** | 8 | 1,121.46 | 8.089058 | 🟢 medium — moderately distinctive | 0.123847 | disc, discs | — |
| 1358 | **external** | 11 | 1,118.50 | 5.867442 | 🟢 medium — moderately distinctive | 0.075072 | - | — |
| 1359 | **begin** | 12 | 1,117.49 | 5.373627 | 🟢 medium — moderately distinctive | 0.011577 | begin, begins | — |
| 1360 | **represent** | 10 | 1,115.37 | 6.436135 | 🟢 medium — moderately distinctive | 0.056419 | represent, represents | — |
| 1361 | **letting** | 7 | 1,114.54 | 9.18767 | 🟢 medium — moderately distinctive | - | - | — |
| 1362 | **onward** | 7 | 1,114.54 | 9.18767 | 🟢 medium — moderately distinctive | - | onward, onwards | — |
| 1363 | **ruin** | 7 | 1,114.54 | 9.18767 | 🟢 medium — moderately distinctive | 0.148767 | - | — |
| 1364 | **quarrel** | 7 | 1,114.54 | 9.18767 | 🟢 medium — moderately distinctive | 0.145701 | quarrel, quarrels | — |
| 1365 | **enjoying** | 7 | 1,114.54 | 9.18767 | 🟢 medium — moderately distinctive | - | - | ~ |
| 1366 | **afterward** | 7 | 1,114.54 | 9.18767 | 🟢 medium — moderately distinctive | - | - | — |
| 1367 | **cow** | 7 | 1,114.54 | 9.18767 | 🟢 medium — moderately distinctive | 0.127380 | cow, cows | — |
| 1368 | **transmitted** | 7 | 1,114.54 | 9.18767 | 🟢 medium — moderately distinctive | - | - | — |
| 1369 | **step** | 11 | 1,113.96 | 5.843631 | 🟢 medium — moderately distinctive | 0.137040 | step, steps | — |
| 1370 | **wall** | 11 | 1,111.73 | 5.831935 | 🟢 medium — moderately distinctive | 0.117169 | wall, walls | — |
| 1371 | **principle** | 12 | 1,109.98 | 5.337522 | 🟢 medium — moderately distinctive | 0.060295 | - | ~ |
| 1372 | **sister** | 8 | 1,106.85 | 7.983697 | 🟢 medium — moderately distinctive | - | - | — |
| 1373 | **pulled** | 8 | 1,106.85 | 7.983697 | 🟢 medium — moderately distinctive | - | - | — |
| 1374 | **request** | 11 | 1,105.19 | 5.797646 | 🟢 medium — moderately distinctive | 0.082714 | request, requests | — |
| 1375 | **weak** | 11 | 1,103.06 | 5.786473 | 🟢 medium — moderately distinctive | 0.074810 | - | — |
| 1376 | **fit** | 9 | 1,102.29 | 7.067407 | 🟢 medium — moderately distinctive | 0.121798 | fit, fits | — |
| 1377 | **gold** | 13 | 1,096.19 | 4.865747 | 🟢 medium — moderately distinctive | 0.055737 | - | — |
| 1378 | **aim** | 10 | 1,094.55 | 6.31599 | 🟢 medium — moderately distinctive | 0.138854 | aim, aims | — |
| 1379 | **success** | 10 | 1,091.31 | 6.297298 | 🟢 medium — moderately distinctive | 0.083705 | - | — |
| 1380 | **palm** | 10 | 1,088.13 | 6.278949 | 🟢 medium — moderately distinctive | 0.104993 | palm, palms | — |
| 1381 | **rather** | 12 | 1,087.63 | 5.230037 | 🟢 medium — moderately distinctive | - | - | — |
| 1382 | **sea** | 11 | 1,082.98 | 5.681112 | 🟢 medium — moderately distinctive | 0.091567 | sea, seas | — |
| 1383 | **absolutely** | 8 | 1,081.57 | 7.801376 | 🟢 medium — moderately distinctive | 0.108113 | - | — |
| 1384 | **voice** | 8 | 1,081.57 | 7.801376 | 🟢 medium — moderately distinctive | 0.126585 | voice, voices | ~ |
| 1385 | **touch** | 8 | 1,081.57 | 7.801376 | 🟢 medium — moderately distinctive | 0.094861 | touch, touches | — |
| 1386 | **spark** | 8 | 1,081.57 | 7.801376 | 🟢 medium — moderately distinctive | 0.108183 | - | — |
| 1387 | **travelling** | 7 | 1,079.65 | 8.899988 | 🟢 medium — moderately distinctive | - | - | — |
| 1388 | **opposite** | 7 | 1,079.65 | 8.899988 | 🟢 medium — moderately distinctive | 0.125124 | - | — |
| 1389 | **hang** | 7 | 1,079.65 | 8.899988 | 🟢 medium — moderately distinctive | 0.176413 | hang, hangs | — |
| 1390 | **poverty** | 7 | 1,079.65 | 8.899988 | 🟢 medium — moderately distinctive | 0.125851 | - | — |
| 1391 | **prey** | 7 | 1,079.65 | 8.899988 | 🟢 medium — moderately distinctive | 0.125689 | - | — |
| 1392 | **garment** | 7 | 1,079.65 | 8.899988 | 🟢 medium — moderately distinctive | 0.220395 | garment, garments | — |
| 1393 | **calf** | 7 | 1,079.65 | 8.899988 | 🟢 medium — moderately distinctive | 0.125182 | - | — |
| 1394 | **continue** | 15 | 1,076.17 | 4.139953 | 🟢 medium — moderately distinctive | 0.059725 | continue, continues | — |
| 1395 | **difference** | 9 | 1,073.86 | 6.885085 | 🟢 medium — moderately distinctive | 0.094566 | - | — |
| 1396 | **month** | 17 | 1,072.72 | 3.641191 | 🟢 medium — moderately distinctive | 0.068628 | month, months | — |
| 1397 | **rise** | 17 | 1,070.81 | 3.634711 | 🟢 medium — moderately distinctive | 0.040533 | - | — |
| 1398 | **combine** | 8 | 1,070.47 | 7.721333 | 🟢 medium — moderately distinctive | 0.123800 | combine, combines | — |
| 1399 | **rival** | 9 | 1,068.74 | 6.852295 | 🟢 medium — moderately distinctive | 0.141849 | rival, rivals | — |
| 1400 | **search** | 8 | 1,060.20 | 7.647225 | 🟢 medium — moderately distinctive | 0.085395 | - | — |
| 1401 | **money** | 15 | 1,059.46 | 4.075682 | 🟢 medium — moderately distinctive | 0.051416 | - | — |
| 1402 | **gradually** | 9 | 1,054.33 | 6.759922 | 🟢 medium — moderately distinctive | 0.094142 | - | — |
| 1403 | **talking** | 10 | 1,053.93 | 6.08159 | 🟢 medium — moderately distinctive | - | - | — |
| 1404 | **destruction** | 7 | 1,052.58 | 8.676844 | 🟢 medium — moderately distinctive | 0.144104 | destruction, destructions | — |
| 1405 | **oral** | 7 | 1,052.58 | 8.676844 | 🟢 medium — moderately distinctive | 0.126143 | - | — |
| 1406 | **catch** | 7 | 1,052.58 | 8.676844 | 🟢 medium — moderately distinctive | 0.055955 | catch, catches | — |
| 1407 | **till** | 7 | 1,052.58 | 8.676844 | 🟢 medium — moderately distinctive | 0.125423 | - | — |
| 1408 | **gate** | 7 | 1,052.58 | 8.676844 | 🟢 medium — moderately distinctive | 0.220532 | gate, gates | — |
| 1409 | **violent** | 7 | 1,052.58 | 8.676844 | 🟢 medium — moderately distinctive | 0.125682 | - | — |
| 1410 | **considered** | 11 | 1,051.43 | 5.515598 | 🟢 medium — moderately distinctive | - | - | — |
| 1411 | **barley** | 10 | 1,048.83 | 6.052176 | 🟢 medium — moderately distinctive | 0.083891 | - | — |
| 1412 | **country** | 13 | 1,046.32 | 4.644375 | 🟢 medium — moderately distinctive | 0.124497 | countries, country | ~ |
| 1413 | **purpose** | 9 | 1,045.42 | 6.702763 | 🟢 medium — moderately distinctive | 0.093260 | - | — |
| 1414 | **situation** | 12 | 1,044.70 | 5.023592 | 🟢 medium — moderately distinctive | 0.134961 | situation, situations | — |
| 1415 | **task** | 8 | 1,041.69 | 7.513694 | 🟢 medium — moderately distinctive | 0.171580 | task, tasks | — |
| 1416 | **usually** | 9 | 1,041.15 | 6.675364 | 🟢 medium — moderately distinctive | - | - | — |
| 1417 | **battle** | 9 | 1,041.15 | 6.675364 | 🟢 medium — moderately distinctive | 0.120540 | battle, battles | — |
| 1418 | **prepared** | 11 | 1,032.97 | 5.418748 | 🟢 medium — moderately distinctive | - | - | — |
| 1419 | **receiving** | 9 | 1,032.94 | 6.622721 | 🟢 medium — moderately distinctive | - | - | — |
| 1420 | **gem** | 7 | 1,030.46 | 8.494523 | 🟢 medium — moderately distinctive | 0.175592 | gem, gems | — |
| 1421 | **experiencing** | 7 | 1,030.46 | 8.494523 | 🟢 medium — moderately distinctive | - | - | — |
| 1422 | **previous** | 14 | 1,026.72 | 4.231843 | 🟢 medium — moderately distinctive | 0.056022 | - | — |
| 1423 | **capable** | 8 | 1,017.86 | 7.341843 | 🟢 medium — moderately distinctive | 0.107673 | - | — |
| 1424 | **occur** | 9 | 1,014.12 | 6.502093 | 🟢 medium — moderately distinctive | 0.120972 | occur, occurs | — |
| 1425 | **pit** | 7 | 1,011.76 | 8.340372 | 🟢 medium — moderately distinctive | 0.145425 | pit, pits | — |
| 1426 | **shore** | 7 | 1,011.76 | 8.340372 | 🟢 medium — moderately distinctive | 0.176023 | shore, shores | — |
| 1427 | **display** | 7 | 1,011.76 | 8.340372 | 🟢 medium — moderately distinctive | 0.147043 | display, displays | — |
| 1428 | **solid** | 8 | 1,010.75 | 7.29055 | 🟢 medium — moderately distinctive | 0.108092 | - | — |
| 1429 | **favourable** | 9 | 1,010.62 | 6.47962 | 🟢 medium — moderately distinctive | 0.094442 | - | — |
| 1430 | **greatest** | 8 | 1,003.99 | 7.24176 | 🟢 medium — moderately distinctive | - | - | — |
| 1431 | **travel** | 8 | 1,003.99 | 7.24176 | 🟢 medium — moderately distinctive | 0.108012 | - | — |
| 1432 | **conclusion** | 8 | 997.54 | 7.19524 | 🟢 medium — moderately distinctive | 0.107030 | - | ~ |
| 1433 | **permitted** | 8 | 997.54 | 7.19524 | 🟢 medium — moderately distinctive | - | - | — |
| 1434 | **whoever** | 6 | 997.48 | 9.593135 | 🟢 medium — moderately distinctive | - | - | — |
| 1435 | **famous** | 6 | 997.48 | 9.593135 | 🟢 medium — moderately distinctive | 0.109560 | - | — |
| 1436 | **distinguish** | 6 | 997.48 | 9.593135 | 🟢 medium — moderately distinctive | 0.148531 | - | — |
| 1437 | **pea** | 6 | 997.48 | 9.593135 | 🟢 medium — moderately distinctive | 0.222860 | pea, peas | — |
| 1438 | **unpredictable** | 6 | 997.48 | 9.593135 | 🟢 medium — moderately distinctive | 0.147529 | - | — |
| 1439 | **naked** | 6 | 997.48 | 9.593135 | 🟢 medium — moderately distinctive | 0.149556 | - | — |
| 1440 | **whip** | 6 | 997.48 | 9.593135 | 🟢 medium — moderately distinctive | 0.178244 | whip, whips | — |
| 1441 | **shame** | 6 | 997.48 | 9.593135 | 🟢 medium — moderately distinctive | 0.149437 | - | — |
| 1442 | **worm** | 6 | 997.48 | 9.593135 | 🟢 medium — moderately distinctive | 0.148067 | - | — |
| 1443 | **trunk** | 6 | 997.48 | 9.593135 | 🟢 medium — moderately distinctive | 0.148719 | - | — |
| 1444 | **buddhist** | 6 | 997.48 | 9.593135 | 🟢 medium — moderately distinctive | 0.093188 | buddhist, buddhists | — |
| 1445 | **heart-essence** | 6 | 997.16 | 9.59 | 🟢 medium — moderately distinctive | - | - | — |
| 1446 | **twenty-five** | 6 | 997.16 | 9.59 | 🟢 medium — moderately distinctive | - | - | — |
| 1447 | **vajradhara** | 6 | 997.16 | 9.59 | 🟢 medium — moderately distinctive | 0.078378 | - | ✓ རྡོ་རྗེ་འཆང |
| 1448 | **deer** | 6 | 997.16 | 9.59 | 🟢 medium — moderately distinctive | 0.147018 | - | — |
| 1449 | **hallucination** | 6 | 997.16 | 9.59 | 🟢 medium — moderately distinctive | 0.223669 | hallucination, hallucinations | — |
| 1450 | **metaphor** | 6 | 997.16 | 9.59 | 🟢 medium — moderately distinctive | - | - | — |
| 1451 | **gratitude** | 6 | 997.16 | 9.59 | 🟢 medium — moderately distinctive | 0.149070 | - | — |
| 1452 | **millstone** | 6 | 997.16 | 9.59 | 🟢 medium — moderately distinctive | 0.178376 | millstone, millstones | — |
| 1453 | **inhabitant** | 6 | 997.16 | 9.59 | 🟢 medium — moderately distinctive | - | - | — |
| 1454 | **sunak** | 6 | 997.16 | 9.59 | 🟢 medium — moderately distinctive | 0.063087 | - | — |
| 1455 | **grasping** | 6 | 997.16 | 9.59 | 🟢 medium — moderately distinctive | - | - | — |
| 1456 | **bodh** | 6 | 997.16 | 9.59 | 🟢 medium — moderately distinctive | 0.074742 | - | — |
| 1457 | **gaya** | 6 | 997.16 | 9.59 | 🟢 medium — moderately distinctive | 0.074741 | - | — |
| 1458 | **wandering** | 6 | 997.16 | 9.59 | 🟢 medium — moderately distinctive | - | wandering, wanderings | — |
| 1459 | **shepherd** | 6 | 997.16 | 9.59 | 🟢 medium — moderately distinctive | 0.223865 | shepherd, shepherds | — |
| 1460 | **inexhaustible** | 6 | 997.16 | 9.59 | 🟢 medium — moderately distinctive | 0.129001 | - | ~ |
| 1461 | **omniscience** | 6 | 997.16 | 9.59 | 🟢 medium — moderately distinctive | 0.148789 | - | — |
| 1462 | **hermit** | 6 | 997.16 | 9.59 | 🟢 medium — moderately distinctive | 0.179406 | hermit, hermits | — |
| 1463 | **ris** | 6 | 997.16 | 9.59 | 🟢 medium — moderately distinctive | - | - | — |
| 1464 | **mighty** | 6 | 997.16 | 9.59 | 🟢 medium — moderately distinctive | 0.127157 | - | — |
| 1465 | **santideva** | 6 | 997.16 | 9.59 | 🟢 medium — moderately distinctive | 0.077650 | - | — |
| 1466 | **heavenly** | 6 | 997.16 | 9.59 | 🟢 medium — moderately distinctive | 0.148967 | - | — |
| 1467 | **meditative** | 6 | 997.16 | 9.59 | 🟢 medium — moderately distinctive | 0.148483 | - | ~ |
| 1468 | **ruler** | 6 | 997.16 | 9.59 | 🟢 medium — moderately distinctive | 0.149143 | - | — |
| 1469 | **bristling** | 6 | 997.16 | 9.59 | 🟢 medium — moderately distinctive | - | - | — |
| 1470 | **possessed** | 6 | 997.16 | 9.59 | 🟢 medium — moderately distinctive | - | - | — |
| 1471 | **mastery** | 6 | 997.16 | 9.59 | 🟢 medium — moderately distinctive | 0.149355 | - | — |
| 1472 | **prosperous** | 6 | 997.16 | 9.59 | 🟢 medium — moderately distinctive | 0.147887 | - | — |
| 1473 | **ambition** | 6 | 997.16 | 9.59 | 🟢 medium — moderately distinctive | 0.223507 | ambition, ambitions | — |
| 1474 | **weeping** | 6 | 997.16 | 9.59 | 🟢 medium — moderately distinctive | 0.148916 | - | — |
| 1475 | **flock** | 6 | 997.16 | 9.59 | 🟢 medium — moderately distinctive | 0.223217 | flock, flocks | — |
| 1476 | **meditated** | 6 | 997.16 | 9.59 | 🟢 medium — moderately distinctive | - | - | — |
| 1477 | **emulate** | 6 | 997.16 | 9.59 | 🟢 medium — moderately distinctive | 0.168840 | emulate, emulates | — |
| 1478 | **terror** | 6 | 997.16 | 9.59 | 🟢 medium — moderately distinctive | 0.148018 | - | — |
| 1479 | **delight** | 6 | 997.16 | 9.59 | 🟢 medium — moderately distinctive | 0.179054 | delight, delights | — |
| 1480 | **particle** | 6 | 997.16 | 9.59 | 🟢 medium — moderately distinctive | - | - | — |
| 1481 | **ogress** | 6 | 997.16 | 9.59 | 🟢 medium — moderately distinctive | 0.109331 | ogress, ogresses | — |
| 1482 | **guest** | 6 | 997.16 | 9.59 | 🟢 medium — moderately distinctive | 0.179313 | guest, guests | — |
| 1483 | **tale** | 6 | 997.16 | 9.59 | 🟢 medium — moderately distinctive | 0.178740 | tale, tales | — |
| 1484 | **bonpo** | 6 | 997.16 | 9.59 | 🟢 medium — moderately distinctive | 0.273425 | bonpo, bonpos | ✓ བོན་པོ |
| 1485 | **pith-instruction** | 6 | 997.16 | 9.59 | 🟢 medium — moderately distinctive | - | - | — |
| 1486 | **boatman** | 6 | 997.16 | 9.59 | 🟢 medium — moderately distinctive | 0.149237 | - | — |
| 1487 | **prostrated** | 6 | 997.16 | 9.59 | 🟢 medium — moderately distinctive | - | - | — |
| 1488 | **swan** | 6 | 997.16 | 9.59 | 🟢 medium — moderately distinctive | 0.224425 | swan, swans | — |
| 1489 | **unsurpassable** | 6 | 997.16 | 9.59 | 🟢 medium — moderately distinctive | 0.149369 | - | — |
| 1490 | **jealous** | 6 | 997.16 | 9.59 | 🟢 medium — moderately distinctive | 0.149232 | - | — |
| 1491 | **prayed** | 6 | 997.16 | 9.59 | 🟢 medium — moderately distinctive | - | - | — |
| 1492 | **ngokpa** | 6 | 997.16 | 9.59 | 🟢 medium — moderately distinctive | 0.077251 | - | — |
| 1493 | **incomparable** | 6 | 997.16 | 9.59 | 🟢 medium — moderately distinctive | 0.149501 | - | — |
| 1494 | **vajrapani** | 6 | 997.16 | 9.59 | 🟢 medium — moderately distinctive | 0.093713 | - | ✓ ཕྱག་ན་རྡོ་རྗེ |
| 1495 | **atriya** | 6 | 997.16 | 9.59 | 🟢 medium — moderately distinctive | 0.149228 | - | — |
| 1496 | **dharmaraksita** | 6 | 997.16 | 9.59 | 🟢 medium — moderately distinctive | 0.084874 | - | — |
| 1497 | **hard-to-endure** | 6 | 997.16 | 9.59 | 🟢 medium — moderately distinctive | - | - | — |
| 1498 | **zangpo** | 6 | 997.16 | 9.59 | 🟢 medium — moderately distinctive | 0.078727 | - | ~ |
| 1499 | **rejoicing** | 6 | 997.16 | 9.59 | 🟢 medium — moderately distinctive | - | - | — |
| 1500 | **emanate** | 6 | 997.16 | 9.59 | 🟢 medium — moderately distinctive | - | emanate, emanates | — |
| 1501 | **wrist** | 6 | 997.16 | 9.59 | 🟢 medium — moderately distinctive | 0.298981 | wrist, wrists | — |
| 1502 | **sever** | 6 | 997.16 | 9.59 | 🟢 medium — moderately distinctive | 0.179429 | sever, severs | — |
| 1503 | **takaya** | 6 | 997.16 | 9.59 | 🟢 medium — moderately distinctive | 0.149598 | - | — |
| 1504 | **hrih** | 6 | 997.16 | 9.59 | 🟢 medium — moderately distinctive | 0.115355 | - | — |
| 1505 | **altogether** | 7 | 995.56 | 8.206841 | 🟢 medium — moderately distinctive | 0.125045 | - | — |
| 1506 | **genuine** | 7 | 995.56 | 8.206841 | 🟢 medium — moderately distinctive | 0.123861 | - | — |
| 1507 | **meant** | 9 | 994.18 | 6.374259 | 🟢 medium — moderately distinctive | - | - | — |
| 1508 | **move** | 13 | 988.82 | 4.389129 | 🟢 medium — moderately distinctive | 0.231353 | move, moves | — |
| 1509 | **careful** | 8 | 985.47 | 7.108229 | 🟢 medium — moderately distinctive | 0.107831 | - | — |
| 1510 | **mark** | 11 | 984.08 | 5.162318 | 🟢 medium — moderately distinctive | 0.103228 | mark, marks | — |
| 1511 | **except** | 9 | 982.18 | 6.297298 | 🟢 medium — moderately distinctive | - | - | — |
| 1512 | **avoided** | 7 | 981.27 | 8.089058 | 🟢 medium — moderately distinctive | - | - | — |
| 1513 | **fat** | 7 | 981.27 | 8.089058 | 🟢 medium — moderately distinctive | 0.125425 | - | — |
| 1514 | **health** | 10 | 979.40 | 5.651553 | 🟢 medium — moderately distinctive | 0.082917 | - | — |
| 1515 | **heavy** | 11 | 977.39 | 5.127227 | 🟢 medium — moderately distinctive | 0.074015 | - | — |
| 1516 | **highly** | 9 | 976.51 | 6.260931 | 🟢 medium — moderately distinctive | 0.094316 | - | — |
| 1517 | **aside** | 8 | 969.15 | 6.990446 | 🟢 medium — moderately distinctive | - | - | — |
| 1518 | **concentrated** | 8 | 969.15 | 6.990446 | 🟢 medium — moderately distinctive | - | - | — |
| 1519 | **looked** | 8 | 969.15 | 6.990446 | 🟢 medium — moderately distinctive | - | - | — |
| 1520 | **based** | 13 | 968.70 | 4.29983 | 🟢 medium — moderately distinctive | - | - | — |
| 1521 | **bright** | 7 | 968.49 | 7.983697 | 🟢 medium — moderately distinctive | 0.105317 | - | — |
| 1522 | **accepted** | 10 | 963.35 | 5.558895 | 🟢 medium — moderately distinctive | - | - | — |
| 1523 | **garden** | 7 | 956.93 | 7.888387 | 🟢 medium — moderately distinctive | - | garden, gardens | — |
| 1524 | **deepest** | 6 | 955.32 | 9.18767 | 🟢 medium — moderately distinctive | - | - | — |
| 1525 | **abuse** | 6 | 955.32 | 9.18767 | 🟢 medium — moderately distinctive | 0.149468 | - | — |
| 1526 | **inferior** | 6 | 955.32 | 9.18767 | 🟢 medium — moderately distinctive | 0.179261 | inferior, inferiors | — |
| 1527 | **nail** | 6 | 955.32 | 9.18767 | 🟢 medium — moderately distinctive | 0.223692 | nail, nails | — |
| 1528 | **hesitation** | 6 | 955.32 | 9.18767 | 🟢 medium — moderately distinctive | 0.298586 | hesitation, hesitations | — |
| 1529 | **suppose** | 6 | 955.32 | 9.18767 | 🟢 medium — moderately distinctive | 0.148971 | - | — |
| 1530 | **wise** | 6 | 955.32 | 9.18767 | 🟢 medium — moderately distinctive | 0.113293 | - | — |
| 1531 | **thorn** | 6 | 955.32 | 9.18767 | 🟢 medium — moderately distinctive | - | - | — |
| 1532 | **mouse** | 6 | 955.32 | 9.18767 | 🟢 medium — moderately distinctive | 0.181425 | mice, mouse | — |
| 1533 | **clarity** | 6 | 955.32 | 9.18767 | 🟢 medium — moderately distinctive | 0.149632 | - | ~ |
| 1534 | **cloth** | 6 | 955.32 | 9.18767 | 🟢 medium — moderately distinctive | 0.149401 | - | — |
| 1535 | **dissolution** | 6 | 955.32 | 9.18767 | 🟢 medium — moderately distinctive | 0.149662 | - | ~ |
| 1536 | **correct** | 8 | 954.54 | 6.885085 | 🟢 medium — moderately distinctive | 0.108413 | - | — |
| 1537 | **hill** | 8 | 954.54 | 6.885085 | 🟢 medium — moderately distinctive | 0.142410 | hill, hills | — |
| 1538 | **finished** | 8 | 954.54 | 6.885085 | 🟢 medium — moderately distinctive | - | - | — |
| 1539 | **bell** | 8 | 954.54 | 6.885085 | 🟢 medium — moderately distinctive | 0.123449 | bell, bells | ✓ དྲིལ་བུ |
| 1540 | **size** | 9 | 953.26 | 6.111895 | 🟢 medium — moderately distinctive | 0.094125 | - | — |
| 1541 | **connection** | 9 | 953.26 | 6.111895 | 🟢 medium — moderately distinctive | 0.141701 | connection, connections | — |
| 1542 | **obtained** | 8 | 949.99 | 6.852295 | 🟢 medium — moderately distinctive | - | - | — |
| 1543 | **blow** | 7 | 946.38 | 7.801376 | 🟢 medium — moderately distinctive | 0.219814 | blow, blows | — |
| 1544 | **divided** | 8 | 945.59 | 6.820546 | 🟢 medium — moderately distinctive | - | - | — |
| 1545 | **beneficial** | 8 | 945.59 | 6.820546 | 🟢 medium — moderately distinctive | 0.108327 | - | — |
| 1546 | **south** | 12 | 942.16 | 4.53054 | 🟢 medium — moderately distinctive | 0.055401 | - | — |
| 1547 | **led** | 11 | 939.74 | 4.929696 | 🟢 medium — moderately distinctive | - | - | — |
| 1548 | **former** | 10 | 939.06 | 5.418748 | 🟢 medium — moderately distinctive | - | - | — |
| 1549 | **upward** | 9 | 937.31 | 6.009616 | 🟢 medium — moderately distinctive | 0.284300 | upward, upwards | — |
| 1550 | **trapped** | 7 | 936.67 | 7.721333 | 🟢 medium — moderately distinctive | - | - | — |
| 1551 | **worst** | 8 | 929.26 | 6.702763 | 🟢 medium — moderately distinctive | 0.107502 | - | — |
| 1552 | **weight** | 8 | 929.26 | 6.702763 | 🟢 medium — moderately distinctive | 0.122957 | weight, weights | — |
| 1553 | **execution** | 7 | 927.68 | 7.647225 | 🟢 medium — moderately distinctive | 0.124980 | - | — |
| 1554 | **bean** | 7 | 927.68 | 7.647225 | 🟢 medium — moderately distinctive | 0.146072 | bean, beans | — |
| 1555 | **worth** | 11 | 926.71 | 4.861332 | 🟢 medium — moderately distinctive | 0.074152 | - | — |
| 1556 | **tried** | 8 | 925.46 | 6.675364 | 🟢 medium — moderately distinctive | - | - | — |
| 1557 | **belong** | 6 | 925.41 | 8.899988 | 🟢 medium — moderately distinctive | 0.179132 | belong, belongs | — |
| 1558 | **describe** | 6 | 925.41 | 8.899988 | 🟢 medium — moderately distinctive | 0.178542 | describe, describes | — |
| 1559 | **distant** | 6 | 925.41 | 8.899988 | 🟢 medium — moderately distinctive | 0.148301 | - | — |
| 1560 | **queen** | 6 | 925.41 | 8.899988 | 🟢 medium — moderately distinctive | 0.155583 | queen, queens | — |
| 1561 | **quest** | 6 | 925.41 | 8.899988 | 🟢 medium — moderately distinctive | 0.148891 | - | — |
| 1562 | **crossed** | 6 | 925.41 | 8.899988 | 🟢 medium — moderately distinctive | - | - | — |
| 1563 | **wool** | 6 | 925.41 | 8.899988 | 🟢 medium — moderately distinctive | 0.148105 | - | — |
| 1564 | **disillusionment** | 6 | 925.41 | 8.899988 | 🟢 medium — moderately distinctive | 0.148992 | - | — |
| 1565 | **wound** | 6 | 925.41 | 8.899988 | 🟢 medium — moderately distinctive | 0.298615 | wound, wounds | — |
| 1566 | **distinction** | 6 | 925.41 | 8.899988 | 🟢 medium — moderately distinctive | 0.149259 | - | — |
| 1567 | **soup** | 6 | 925.41 | 8.899988 | 🟢 medium — moderately distinctive | 0.149451 | - | — |
| 1568 | **com** | 6 | 925.41 | 8.899988 | 🟢 medium — moderately distinctive | - | - | — |
| 1569 | **save** | 8 | 921.77 | 6.648696 | 🟢 medium — moderately distinctive | 0.108201 | - | — |
| 1570 | **including** | 13 | 921.39 | 4.089838 | 🟢 medium — moderately distinctive | - | - | — |
| 1571 | **attached** | 7 | 919.31 | 7.578232 | 🟢 medium — moderately distinctive | - | - | — |
| 1572 | **arrive** | 7 | 919.31 | 7.578232 | 🟢 medium — moderately distinctive | 0.031723 | - | — |
| 1573 | **special** | 11 | 915.30 | 4.801485 | 🟢 medium — moderately distinctive | 0.074862 | - | — |
| 1574 | **summit** | 8 | 914.65 | 6.597403 | 🟢 medium — moderately distinctive | 0.108186 | - | — |
| 1575 | **written** | 8 | 914.65 | 6.597403 | 🟢 medium — moderately distinctive | - | - | — |
| 1576 | **bearing** | 7 | 911.48 | 7.513694 | 🟢 medium — moderately distinctive | - | - | — |
| 1577 | **accepting** | 7 | 911.48 | 7.513694 | 🟢 medium — moderately distinctive | - | - | — |
| 1578 | **air** | 9 | 911.42 | 5.843631 | 🟢 medium — moderately distinctive | 0.106655 | air, airs | — |
| 1579 | **influence** | 8 | 907.89 | 6.548613 | 🟢 medium — moderately distinctive | 0.214284 | influence, influences | — |
| 1580 | **direct** | 9 | 902.51 | 5.786473 | 🟢 medium — moderately distinctive | 0.094321 | - | — |
| 1581 | **tip** | 6 | 902.21 | 8.676844 | 🟢 medium — moderately distinctive | - | tip, tips | — |
| 1582 | **somewhere** | 6 | 902.21 | 8.676844 | 🟢 medium — moderately distinctive | - | - | — |
| 1583 | **cooked** | 6 | 902.21 | 8.676844 | 🟢 medium — moderately distinctive | - | - | — |
| 1584 | **mirror** | 6 | 902.21 | 8.676844 | 🟢 medium — moderately distinctive | 0.149438 | - | — |
| 1585 | **exhaust** | 6 | 902.21 | 8.676844 | 🟢 medium — moderately distinctive | 0.055829 | exhaust, exhausts | — |
| 1586 | **against** | 15 | 890.75 | 3.426667 | 🟢 medium — moderately distinctive | - | - | — |
| 1587 | **message** | 7 | 890.63 | 7.341843 | 🟢 medium — moderately distinctive | 0.219353 | message, messages | — |
| 1588 | **returned** | 8 | 886.52 | 6.394462 | 🟢 medium — moderately distinctive | - | - | — |
| 1589 | **understood** | 7 | 884.41 | 7.29055 | 🟢 medium — moderately distinctive | - | - | — |
| 1590 | **slaughter** | 7 | 884.41 | 7.29055 | 🟢 medium — moderately distinctive | 0.055612 | - | — |
| 1591 | **guided** | 6 | 883.25 | 8.494523 | 🟢 medium — moderately distinctive | - | - | — |
| 1592 | **forget** | 6 | 883.25 | 8.494523 | 🟢 medium — moderately distinctive | 0.124881 | - | — |
| 1593 | **forgotten** | 6 | 883.25 | 8.494523 | 🟢 medium — moderately distinctive | - | - | — |
| 1594 | **spoken** | 6 | 883.25 | 8.494523 | 🟢 medium — moderately distinctive | - | - | — |
| 1595 | **book** | 8 | 880.97 | 6.354457 | 🟢 medium — moderately distinctive | 0.108034 | - | — |
| 1596 | **morning** | 10 | 879.80 | 5.076796 | 🟢 medium — moderately distinctive | 0.083112 | - | — |
| 1597 | **mentioned** | 7 | 878.49 | 7.24176 | 🟢 medium — moderately distinctive | - | - | — |
| 1598 | **various** | 9 | 876.99 | 5.622843 | 🟢 medium — moderately distinctive | - | - | — |
| 1599 | **decided** | 10 | 873.29 | 5.039258 | 🟢 medium — moderately distinctive | - | - | — |
| 1600 | **meanwhile** | 8 | 873.05 | 6.297298 | 🟢 medium — moderately distinctive | - | - | — |
| 1601 | **gathering** | 7 | 872.85 | 7.19524 | 🟢 medium — moderately distinctive | - | - | — |
| 1602 | **session** | 9 | 868.40 | 5.567784 | 🟢 medium — moderately distinctive | 0.121594 | session, sessions | — |
| 1603 | **achieved** | 8 | 868.01 | 6.260931 | 🟢 medium — moderately distinctive | - | - | — |
| 1604 | **downward** | 8 | 868.01 | 6.260931 | 🟢 medium — moderately distinctive | - | downward, downwards | — |
| 1605 | **invite** | 6 | 867.22 | 8.340372 | 🟢 medium — moderately distinctive | 0.061459 | - | — |
| 1606 | **cure** | 6 | 867.22 | 8.340372 | 🟢 medium — moderately distinctive | 0.148960 | - | — |
| 1607 | **belonging** | 6 | 867.22 | 8.340372 | 🟢 medium — moderately distinctive | 0.297260 | belonging, belongings | — |
| 1608 | **busy** | 6 | 867.22 | 8.340372 | 🟢 medium — moderately distinctive | 0.149202 | - | — |
| 1609 | **leather** | 6 | 867.22 | 8.340372 | 🟢 medium — moderately distinctive | 0.149114 | - | — |
| 1610 | **prince** | 6 | 867.22 | 8.340372 | 🟢 medium — moderately distinctive | 0.129664 | - | — |
| 1611 | **everybody** | 6 | 867.22 | 8.340372 | 🟢 medium — moderately distinctive | - | - | — |
| 1612 | **consulted** | 6 | 867.22 | 8.340372 | 🟢 medium — moderately distinctive | - | - | — |
| 1613 | **entered** | 9 | 861.59 | 5.524108 | 🟢 medium — moderately distinctive | - | - | — |
| 1614 | **certainly** | 8 | 860.77 | 6.208745 | 🟢 medium — moderately distinctive | - | - | — |
| 1615 | **increase** | 14 | 857.70 | 3.535181 | 🟢 medium — moderately distinctive | 0.056027 | - | ~ |
| 1616 | **refused** | 8 | 856.15 | 6.175409 | 🟢 medium — moderately distinctive | - | - | — |
| 1617 | **further** | 13 | 855.09 | 3.795559 | 🟢 medium — moderately distinctive | - | further, furthers | — |
| 1618 | **art** | 6 | 853.34 | 8.206841 | 🟢 medium — moderately distinctive | 0.178857 | art, arts | — |
| 1619 | **spite** | 6 | 853.34 | 8.206841 | 🟢 medium — moderately distinctive | 0.148983 | - | — |
| 1620 | **throw** | 6 | 853.34 | 8.206841 | 🟢 medium — moderately distinctive | 0.093561 | throw, throws | — |
| 1621 | **swiftly** | 6 | 853.34 | 8.206841 | 🟢 medium — moderately distinctive | 0.149604 | - | — |
| 1622 | **arranged** | 7 | 852.58 | 7.028186 | 🟢 medium — moderately distinctive | - | - | — |
| 1623 | **closer** | 7 | 852.58 | 7.028186 | 🟢 medium — moderately distinctive | - | - | — |
| 1624 | **giant** | 7 | 848.00 | 6.990446 | 🟢 medium — moderately distinctive | 0.125791 | - | — |
| 1625 | **achieve** | 8 | 847.34 | 6.111895 | 🟢 medium — moderately distinctive | 0.107923 | - | — |
| 1626 | **resolve** | 8 | 843.14 | 6.08159 | 🟢 medium — moderately distinctive | 0.107927 | - | — |
| 1627 | **placed** | 8 | 843.14 | 6.08159 | 🟢 medium — moderately distinctive | - | - | — |
| 1628 | **several** | 11 | 841.46 | 4.414165 | 🟢 medium — moderately distinctive | - | - | — |
| 1629 | **command** | 6 | 841.09 | 8.089058 | 🟢 medium — moderately distinctive | 0.178589 | command, commands | — |
| 1630 | **defeat** | 6 | 841.09 | 8.089058 | 🟢 medium — moderately distinctive | 0.149289 | - | — |
| 1631 | **supposed** | 6 | 841.09 | 8.089058 | 🟢 medium — moderately distinctive | - | - | — |
| 1632 | **rejecting** | 6 | 841.09 | 8.089058 | 🟢 medium — moderately distinctive | - | - | — |
| 1633 | **transfer** | 8 | 841.09 | 6.066775 | 🟢 medium — moderately distinctive | 0.108528 | - | — |
| 1634 | **type** | 7 | 839.33 | 6.918987 | 🟢 medium — moderately distinctive | 0.175937 | type, types | — |
| 1635 | **commitment** | 8 | 837.07 | 6.037787 | 🟢 medium — moderately distinctive | 0.122383 | commitment, commitments | — |
| 1636 | **content** | 7 | 835.22 | 6.885085 | 🟢 medium — moderately distinctive | 0.175501 | content, contents | — |
| 1637 | **total** | 14 | 831.88 | 3.428768 | 🟢 medium — moderately distinctive | 0.056226 | - | ~ |
| 1638 | **shearing** | 5 | 831.24 | 9.593135 | 🟢 medium — moderately distinctive | - | - | — |
| 1639 | **marriage** | 5 | 831.24 | 9.593135 | 🟢 medium — moderately distinctive | 0.181456 | - | — |
| 1640 | **incapable** | 5 | 831.24 | 9.593135 | 🟢 medium — moderately distinctive | 0.181558 | - | — |
| 1641 | **neck** | 5 | 831.24 | 9.593135 | 🟢 medium — moderately distinctive | 0.226361 | neck, necks | — |
| 1642 | **permanence** | 5 | 831.24 | 9.593135 | 🟢 medium — moderately distinctive | 0.180369 | - | — |
| 1643 | **entourage** | 5 | 831.24 | 9.593135 | 🟢 medium — moderately distinctive | 0.181905 | - | — |
| 1644 | **piled** | 5 | 831.24 | 9.593135 | 🟢 medium — moderately distinctive | - | - | — |
| 1645 | **lit** | 5 | 831.24 | 9.593135 | 🟢 medium — moderately distinctive | - | - | — |
| 1646 | **friendship** | 5 | 831.24 | 9.593135 | 🟢 medium — moderately distinctive | 0.180327 | - | — |
| 1647 | **silk** | 5 | 831.24 | 9.593135 | 🟢 medium — moderately distinctive | 0.227529 | silk, silks | — |
| 1648 | **dispel** | 5 | 831.24 | 9.593135 | 🟢 medium — moderately distinctive | 0.194215 | dispel, dispels | — |
| 1649 | **boil** | 5 | 831.24 | 9.593135 | 🟢 medium — moderately distinctive | - | boil, boils | — |
| 1650 | **distress** | 5 | 831.24 | 9.593135 | 🟢 medium — moderately distinctive | 0.181515 | - | — |
| 1651 | **sensation** | 5 | 831.24 | 9.593135 | 🟢 medium — moderately distinctive | 0.226474 | sensation, sensations | — |
| 1652 | **stomach** | 5 | 831.24 | 9.593135 | 🟢 medium — moderately distinctive | 0.226323 | stomach, stomachs | — |
| 1653 | **courage** | 5 | 831.24 | 9.593135 | 🟢 medium — moderately distinctive | 0.155256 | - | — |
| 1654 | **dirty** | 5 | 831.24 | 9.593135 | 🟢 medium — moderately distinctive | 0.182532 | - | — |
| 1655 | **wasted** | 5 | 831.24 | 9.593135 | 🟢 medium — moderately distinctive | - | - | — |
| 1656 | **snake** | 5 | 831.24 | 9.593135 | 🟢 medium — moderately distinctive | - | snake, snakes | — |
| 1657 | **sleeping** | 5 | 831.24 | 9.593135 | 🟢 medium — moderately distinctive | - | - | — |
| 1658 | **insult** | 5 | 831.24 | 9.593135 | 🟢 medium — moderately distinctive | - | insult, insults | — |
| 1659 | **succession** | 5 | 831.24 | 9.593135 | 🟢 medium — moderately distinctive | 0.182311 | - | — |
| 1660 | **courageous** | 5 | 831.24 | 9.593135 | 🟢 medium — moderately distinctive | 0.182265 | - | — |
| 1661 | **infallible** | 5 | 831.24 | 9.593135 | 🟢 medium — moderately distinctive | 0.182460 | - | — |
| 1662 | **shining** | 5 | 831.24 | 9.593135 | 🟢 medium — moderately distinctive | - | - | — |
| 1663 | **prisoner** | 5 | 831.24 | 9.593135 | 🟢 medium — moderately distinctive | 0.227713 | prisoner, prisoners | — |
| 1664 | **enlightened** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive | - | - | — |
| 1665 | **twofold** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive | 0.182476 | - | ~ |
| 1666 | **misery** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive | - | miseries, misery | — |
| 1667 | **fame** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive | 0.181727 | - | — |
| 1668 | **stain** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive | - | stain, stains | — |
| 1669 | **dumb** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive | 0.182449 | - | — |
| 1670 | **proverb** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive | 0.181586 | - | — |
| 1671 | **dy** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive | - | - | ~ |
| 1672 | **sack** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive | 0.181133 | - | — |
| 1673 | **ananda** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive | 0.106884 | - | ✓ ཀུན་དགའ་བོ |
| 1674 | **machik** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive | 0.156950 | - | ~ |
| 1675 | **spoil** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive | 0.194355 | spoil, spoils | — |
| 1676 | **persevere** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive | 0.182233 | - | — |
| 1677 | **beginningless** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive | 0.181254 | - | — |
| 1678 | **crying** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive | - | - | — |
| 1679 | **reigned** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive | - | - | — |
| 1680 | **unchanging** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive | 0.181823 | - | — |
| 1681 | **vairotsana** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive | 0.100609 | - | ✓ བཻ་རོ་ཙ་ན |
| 1682 | **circum** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive | 0.180441 | - | — |
| 1683 | **manjusri** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive | 0.099665 | - | — |
| 1684 | **radiant** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive | 0.182197 | - | — |
| 1685 | **drom** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive | 0.122171 | - | ~ |
| 1686 | **meditator** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive | - | meditator, meditators | — |
| 1687 | **laziness** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive | 0.154540 | - | — |
| 1688 | **ty** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive | - | - | ~ |
| 1689 | **decadent** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive | 0.182357 | - | — |
| 1690 | **wearing** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive | - | - | — |
| 1691 | **scholar** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive | 0.182428 | - | — |
| 1692 | **gonpo** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive | 0.100607 | - | ~ |
| 1693 | **chengawa** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive | 0.109422 | - | ~ |
| 1694 | **recited** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive | - | - | — |
| 1695 | **threefold** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive | 0.182119 | - | ~ |
| 1696 | **flame** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive | - | flame, flames | — |
| 1697 | **precipice** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive | - | precipice, precipices | — |
| 1698 | **ghost** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive | 0.228207 | ghost, ghosts | ✓ འདྲེ |
| 1699 | **immortality** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive | 0.182578 | - | — |
| 1700 | **hollow** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive | 0.232242 | - | — |
| 1701 | **deserted** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive | - | - | — |
| 1702 | **womb** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive | 0.181176 | - | — |
| 1703 | **asleep** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive | 0.182086 | - | — |
| 1704 | **stronghold** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive | 0.182669 | - | — |
| 1705 | **conduce** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive | - | - | — |
| 1706 | **molten** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive | 0.180688 | - | — |
| 1707 | **red-hot** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive | - | - | — |
| 1708 | **unimaginable** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive | 0.182135 | - | — |
| 1709 | **lover** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive | 0.224264 | lover, lovers | ~ |
| 1710 | **repa** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive | 0.105295 | - | ~ |
| 1711 | **turquoise** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive | 0.153635 | - | — |
| 1712 | **swallow** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive | 0.181229 | - | — |
| 1713 | **delicious** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive | 0.181401 | - | — |
| 1714 | **rage** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive | 0.182284 | - | — |
| 1715 | **novice** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive | - | novice, novices | ✓ དགེ་ཚུལ |
| 1716 | **mustard** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive | 0.181677 | - | — |
| 1717 | **confessing** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive | - | - | — |
| 1718 | **protuberance** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive | 0.227915 | protuberance, protuberances | ~ |
| 1719 | **evil-doer** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive | - | evil-doer, evil-doers | — |
| 1720 | **anguish** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive | 0.181498 | - | — |
| 1721 | **boy** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive | - | boy, boys | — |
| 1722 | **song** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive | - | song, songs | ~ |
| 1723 | **displease** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive | 0.182073 | - | — |
| 1724 | **cousin** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive | 0.226706 | cousin, cousins | — |
| 1725 | **circumambulating** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive | - | - | — |
| 1726 | **resting** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive | - | - | — |
| 1727 | **smile** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive | 0.231764 | smile, smiles | — |
| 1728 | **trickery** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive | 0.181482 | - | — |
| 1729 | **householder** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive | 0.227659 | householder, householders | — |
| 1730 | **defiled** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive | - | - | — |
| 1731 | **proliferating** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive | - | - | — |
| 1732 | **sakya** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive | 0.244263 | sakya, sakyas | — |
| 1733 | **ashamed** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive | - | - | — |
| 1734 | **heartfelt** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive | 0.182294 | - | — |
| 1735 | **sandal** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive | 0.181775 | - | — |
| 1736 | **disrespect** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive | 0.182609 | - | — |
| 1737 | **homage** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive | 0.182086 | - | — |
| 1738 | **incense** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive | 0.182305 | - | — |
| 1739 | **jewelled** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive | - | - | — |
| 1740 | **perseverance** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive | 0.182389 | - | — |
| 1741 | **canopy** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive | - | canopies, canopy | ~ |
| 1742 | **lakini** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive | - | lakini, lakinis | — |
| 1743 | **consort** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive | 0.228064 | consort, consorts | ✓ ཡུམ / གསང་ཡུམ |
| 1744 | **cup** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive | 0.182542 | - | ~ |
| 1745 | **spontaneous** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive | 0.156990 | - | — |
| 1746 | **obstacle-maker** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive | - | - | — |
| 1747 | **dwelling** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive | 0.228019 | dwelling, dwellings | ~ |
| 1748 | **abhidharma** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive | 0.099487 | - | ✓ མངོན་པ |
| 1749 | **asariga** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive | 0.156255 | - | — |
| 1750 | **asanga** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive | 0.109476 | - | ✓ ཐོགས་མེད |
| 1751 | **rotten** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive | 0.156784 | - | — |
| 1752 | **medi** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive | 0.182312 | - | — |
| 1753 | **pacify** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive | 0.182564 | - | — |
| 1754 | **non-dharma** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive | - | - | — |
| 1755 | **conceit** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive | 0.182572 | - | — |
| 1756 | **tendzin** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive | 0.110807 | - | — |
| 1757 | **maintain** | 9 | 830.29 | 5.323438 | 🟢 medium — moderately distinctive | 0.094775 | - | — |
| 1758 | **hole** | 6 | 830.14 | 7.983697 | 🟢 medium — moderately distinctive | 0.147612 | - | — |
| 1759 | **dried** | 6 | 830.14 | 7.983697 | 🟢 medium — moderately distinctive | - | - | — |
| 1760 | **plenty** | 6 | 830.14 | 7.983697 | 🟢 medium — moderately distinctive | 0.149148 | - | — |
| 1761 | **perceived** | 6 | 830.14 | 7.983697 | 🟢 medium — moderately distinctive | - | - | — |
| 1762 | **boat** | 6 | 830.14 | 7.983697 | 🟢 medium — moderately distinctive | 0.149234 | - | — |
| 1763 | **town** | 6 | 820.23 | 7.888387 | 🟢 medium — moderately distinctive | 0.194358 | town, towns | — |
| 1764 | **nonetheless** | 6 | 820.23 | 7.888387 | 🟢 medium — moderately distinctive | 0.148830 | - | — |
| 1765 | **enjoyed** | 6 | 820.23 | 7.888387 | 🟢 medium — moderately distinctive | - | - | — |
| 1766 | **cease** | 6 | 820.23 | 7.888387 | 🟢 medium — moderately distinctive | 0.143959 | - | — |
| 1767 | **vessel** | 7 | 820.04 | 6.759922 | 🟢 medium — moderately distinctive | 0.176160 | vessel, vessels | — |
| 1768 | **worked** | 7 | 820.04 | 6.759922 | 🟢 medium — moderately distinctive | - | - | — |
| 1769 | **course** | 8 | 818.56 | 5.904256 | 🟢 medium — moderately distinctive | - | - | — |
| 1770 | **visit** | 8 | 818.56 | 5.904256 | 🟢 medium — moderately distinctive | 0.107839 | - | — |
| 1771 | **lot** | 8 | 815.13 | 5.879563 | 🟢 medium — moderately distinctive | 0.122978 | lot, lots | — |
| 1772 | **indian** | 7 | 813.10 | 6.702763 | 🟢 medium — moderately distinctive | 0.062503 | - | — |
| 1773 | **sweet** | 7 | 813.10 | 6.702763 | 🟢 medium — moderately distinctive | 0.125276 | - | ~ |
| 1774 | **repay** | 7 | 813.10 | 6.702763 | 🟢 medium — moderately distinctive | 0.125633 | - | — |
| 1775 | **mix** | 6 | 811.18 | 7.801376 | 🟢 medium — moderately distinctive | 0.182491 | mix, mixes | — |
| 1776 | **rush** | 6 | 811.18 | 7.801376 | 🟢 medium — moderately distinctive | 0.182268 | rush, rushes | — |
| 1777 | **seventh** | 6 | 811.18 | 7.801376 | 🟢 medium — moderately distinctive | 0.148308 | - | — |
| 1778 | **guard** | 6 | 811.18 | 7.801376 | 🟢 medium — moderately distinctive | 0.298007 | guard, guards | — |
| 1779 | **passing** | 6 | 811.18 | 7.801376 | 🟢 medium — moderately distinctive | - | - | — |
| 1780 | **working** | 9 | 807.97 | 5.180337 | 🟢 medium — moderately distinctive | - | - | — |
| 1781 | **ordered** | 7 | 806.54 | 6.648696 | 🟢 medium — moderately distinctive | - | - | — |
| 1782 | **causing** | 7 | 806.54 | 6.648696 | 🟢 medium — moderately distinctive | - | - | — |
| 1783 | **asking** | 7 | 803.39 | 6.622721 | 🟢 medium — moderately distinctive | - | - | — |
| 1784 | **circle** | 6 | 802.86 | 7.721333 | 🟢 medium — moderately distinctive | 0.149141 | - | — |
| 1785 | **serving** | 6 | 802.86 | 7.721333 | 🟢 medium — moderately distinctive | - | - | — |
| 1786 | **ship** | 8 | 802.23 | 5.786473 | 🟢 medium — moderately distinctive | 0.172654 | ship, ships | — |
| 1787 | **compared** | 12 | 800.33 | 3.848531 | 🟢 medium — moderately distinctive | - | - | — |
| 1788 | **carrying** | 7 | 800.32 | 6.597403 | 🟢 medium — moderately distinctive | - | - | — |
| 1789 | **waste** | 7 | 797.33 | 6.57271 | 🟢 medium — moderately distinctive | 0.145488 | waste, wastes | — |
| 1790 | **control** | 10 | 796.47 | 4.595923 | 🟢 medium — moderately distinctive | 0.082897 | - | — |
| 1791 | **horn** | 5 | 796.10 | 9.18767 | 🟢 medium — moderately distinctive | 0.181025 | - | — |
| 1792 | **illusory** | 5 | 796.10 | 9.18767 | 🟢 medium — moderately distinctive | 0.181305 | - | — |
| 1793 | **emperor** | 5 | 796.10 | 9.18767 | 🟢 medium — moderately distinctive | 0.258506 | emperor, emperors | — |
| 1794 | **incalculable** | 5 | 796.10 | 9.18767 | 🟢 medium — moderately distinctive | 0.180759 | - | — |
| 1795 | **wrapped** | 5 | 796.10 | 9.18767 | 🟢 medium — moderately distinctive | - | - | — |
| 1796 | **religious** | 5 | 796.10 | 9.18767 | 🟢 medium — moderately distinctive | 0.182569 | - | — |
| 1797 | **corps** | 5 | 796.10 | 9.18767 | 🟢 medium — moderately distinctive | - | - | — |
| 1798 | **terribly** | 5 | 796.10 | 9.18767 | 🟢 medium — moderately distinctive | 0.180987 | - | — |
| 1799 | **openly** | 5 | 796.10 | 9.18767 | 🟢 medium — moderately distinctive | 0.181529 | - | — |
| 1800 | **odd** | 5 | 796.10 | 9.18767 | 🟢 medium — moderately distinctive | 0.227341 | odd, odds | — |
| 1801 | **hail** | 5 | 796.10 | 9.18767 | 🟢 medium — moderately distinctive | 0.181968 | - | — |
| 1802 | **captain** | 5 | 796.10 | 9.18767 | 🟢 medium — moderately distinctive | 0.155150 | - | — |
| 1803 | **perfume** | 5 | 796.10 | 9.18767 | 🟢 medium — moderately distinctive | 0.227210 | perfume, perfumes | — |
| 1804 | **faithfully** | 5 | 796.10 | 9.18767 | 🟢 medium — moderately distinctive | 0.182711 | - | — |
| 1805 | **thirteen** | 5 | 796.10 | 9.18767 | 🟢 medium — moderately distinctive | 0.182648 | - | — |
| 1806 | **emanating** | 5 | 796.10 | 9.18767 | 🟢 medium — moderately distinctive | 0.182611 | - | — |
| 1807 | **studied** | 6 | 795.15 | 7.647225 | 🟢 medium — moderately distinctive | - | - | — |
| 1808 | **dangerous** | 6 | 795.15 | 7.647225 | 🟢 medium — moderately distinctive | 0.128285 | - | — |
| 1809 | **generally** | 8 | 793.28 | 5.721934 | 🟢 medium — moderately distinctive | 0.108258 | - | — |
| 1810 | **general** | 11 | 789.19 | 4.139953 | 🟢 medium — moderately distinctive | 0.074712 | - | — |
| 1811 | **winter** | 8 | 789.01 | 5.691163 | 🟢 medium — moderately distinctive | 0.106962 | - | — |
| 1812 | **constitute** | 6 | 787.98 | 7.578232 | 🟢 medium — moderately distinctive | 0.194533 | constitute, constitutes | — |
| 1813 | **fighting** | 6 | 787.98 | 7.578232 | 🟢 medium — moderately distinctive | - | - | ~ |
| 1814 | **rank** | 6 | 787.98 | 7.578232 | 🟢 medium — moderately distinctive | 0.178853 | rank, ranks | — |
| 1815 | **opening** | 8 | 786.24 | 5.671162 | 🟢 medium — moderately distinctive | 0.289482 | opening, openings | — |
| 1816 | **calling** | 7 | 783.37 | 6.457641 | 🟢 medium — moderately distinctive | - | - | ~ |
| 1817 | **third** | 10 | 781.87 | 4.511731 | 🟢 medium — moderately distinctive | - | third, thirds | — |
| 1818 | **threatening** | 6 | 781.27 | 7.513694 | 🟢 medium — moderately distinctive | - | - | ~ |
| 1819 | **linked** | 7 | 778.21 | 6.415081 | 🟢 medium — moderately distinctive | - | - | — |
| 1820 | **concentrate** | 7 | 778.21 | 6.415081 | 🟢 medium — moderately distinctive | 0.108208 | - | — |
| 1821 | **cattle** | 7 | 775.70 | 6.394462 | 🟢 medium — moderately distinctive | 0.124980 | - | — |
| 1822 | **definitely** | 6 | 774.96 | 7.453069 | 🟢 medium — moderately distinctive | - | - | — |
| 1823 | **mine** | 8 | 771.91 | 5.567784 | 🟢 medium — moderately distinctive | - | - | — |
| 1824 | **everywhere** | 5 | 771.18 | 8.899988 | 🟢 medium — moderately distinctive | - | - | — |
| 1825 | **drag** | 5 | 771.18 | 8.899988 | 🟢 medium — moderately distinctive | 0.181921 | drag, drags | — |
| 1826 | **missing** | 5 | 771.18 | 8.899988 | 🟢 medium — moderately distinctive | - | - | — |
| 1827 | **meaningless** | 5 | 771.18 | 8.899988 | 🟢 medium — moderately distinctive | 0.182596 | - | — |
| 1828 | **foolish** | 5 | 771.18 | 8.899988 | 🟢 medium — moderately distinctive | 0.135321 | - | — |
| 1829 | **certainty** | 5 | 771.18 | 8.899988 | 🟢 medium — moderately distinctive | 0.181352 | - | — |
| 1830 | **pillar** | 5 | 771.18 | 8.899988 | 🟢 medium — moderately distinctive | 0.227334 | pillar, pillars | — |
| 1831 | **beaten** | 5 | 771.18 | 8.899988 | 🟢 medium — moderately distinctive | - | - | — |
| 1832 | **lump** | 5 | 771.18 | 8.899988 | 🟢 medium — moderately distinctive | - | lump, lumps | — |
| 1833 | **painful** | 5 | 771.18 | 8.899988 | 🟢 medium — moderately distinctive | 0.181163 | - | — |
| 1834 | **undergoing** | 5 | 771.18 | 8.899988 | 🟢 medium — moderately distinctive | - | - | — |
| 1835 | **boot** | 5 | 771.18 | 8.899988 | 🟢 medium — moderately distinctive | - | - | — |
| 1836 | **afraid** | 5 | 771.18 | 8.899988 | 🟢 medium — moderately distinctive | 0.182496 | - | — |
| 1837 | **exceptional** | 6 | 769.02 | 7.395911 | 🟢 medium — moderately distinctive | 0.148972 | - | — |
| 1838 | **included** | 9 | 765.96 | 4.911004 | 🟢 medium — moderately distinctive | - | - | — |
| 1839 | **choose** | 6 | 763.40 | 7.341843 | 🟢 medium — moderately distinctive | 0.148531 | - | — |
| 1840 | **breaking** | 6 | 763.40 | 7.341843 | 🟢 medium — moderately distinctive | - | - | — |
| 1841 | **watch** | 6 | 763.40 | 7.341843 | 🟢 medium — moderately distinctive | 0.129108 | - | — |
| 1842 | **creating** | 6 | 758.06 | 7.29055 | 🟢 medium — moderately distinctive | - | - | — |
| 1843 | **west** | 11 | 757.66 | 3.974548 | 🟢 medium — moderately distinctive | 0.067431 | - | — |
| 1844 | **provide** | 9 | 756.85 | 4.85256 | 🟢 medium — moderately distinctive | 0.182455 | provide, provides | — |
| 1845 | **focus** | 7 | 755.25 | 6.225839 | 🟢 medium — moderately distinctive | 0.125723 | - | — |
| 1846 | **completed** | 10 | 753.63 | 4.348746 | 🟢 medium — moderately distinctive | - | - | — |
| 1847 | **wave** | 6 | 752.99 | 7.24176 | 🟢 medium — moderately distinctive | 0.178800 | wave, waves | — |
| 1848 | **tied** | 6 | 752.99 | 7.24176 | 🟢 medium — moderately distinctive | - | - | — |
| 1849 | **city** | 8 | 752.32 | 5.42647 | 🟢 medium — moderately distinctive | 0.097280 | cities, city | — |
| 1850 | **listened** | 5 | 751.84 | 8.676844 | 🟢 medium — moderately distinctive | - | - | — |
| 1851 | **consume** | 5 | 751.84 | 8.676844 | 🟢 medium — moderately distinctive | 0.154789 | - | — |
| 1852 | **dragged** | 5 | 751.84 | 8.676844 | 🟢 medium — moderately distinctive | - | - | — |
| 1853 | **homeland** | 5 | 751.84 | 8.676844 | 🟢 medium — moderately distinctive | 0.181297 | - | — |
| 1854 | **rocky** | 5 | 751.84 | 8.676844 | 🟢 medium — moderately distinctive | 0.181599 | - | — |
| 1855 | **contaminated** | 5 | 751.84 | 8.676844 | 🟢 medium — moderately distinctive | - | - | — |
| 1856 | **sword** | 5 | 751.84 | 8.676844 | 🟢 medium — moderately distinctive | - | - | — |
| 1857 | **ala** | 5 | 751.84 | 8.676844 | 🟢 medium — moderately distinctive | - | ala, alas | — |
| 1858 | **devoted** | 5 | 751.84 | 8.676844 | 🟢 medium — moderately distinctive | - | - | — |
| 1859 | **generous** | 5 | 751.84 | 8.676844 | 🟢 medium — moderately distinctive | 0.181831 | - | — |
| 1860 | **staying** | 5 | 751.84 | 8.676844 | 🟢 medium — moderately distinctive | - | - | — |
| 1861 | **application** | 7 | 749.13 | 6.175409 | 🟢 medium — moderately distinctive | 0.125733 | - | — |
| 1862 | **setting** | 7 | 749.13 | 6.175409 | 🟢 medium — moderately distinctive | - | - | — |
| 1863 | **completing** | 6 | 748.15 | 7.19524 | 🟢 medium — moderately distinctive | - | - | — |
| 1864 | **fourth** | 9 | 744.41 | 4.772854 | 🟢 medium — moderately distinctive | 0.074840 | - | ~ |
| 1865 | **visible** | 6 | 743.53 | 7.150788 | 🟢 medium — moderately distinctive | 0.149404 | - | — |
| 1866 | **ready** | 7 | 739.57 | 6.096628 | 🟢 medium — moderately distinctive | 0.125358 | - | — |
| 1867 | **firm** | 10 | 738.32 | 4.260416 | 🟢 medium — moderately distinctive | 0.083581 | - | — |
| 1868 | **problem** | 8 | 738.03 | 5.323438 | 🟢 medium — moderately distinctive | 0.216098 | problem, problems | — |
| 1869 | **confused** | 5 | 736.04 | 8.494523 | 🟢 medium — moderately distinctive | - | - | — |
| 1870 | **overcome** | 5 | 736.04 | 8.494523 | 🟢 medium — moderately distinctive | 0.182366 | - | — |
| 1871 | **throwing** | 5 | 736.04 | 8.494523 | 🟢 medium — moderately distinctive | - | - | — |
| 1872 | **vicious** | 5 | 736.04 | 8.494523 | 🟢 medium — moderately distinctive | 0.182211 | - | — |
| 1873 | **surpass** | 5 | 736.04 | 8.494523 | 🟢 medium — moderately distinctive | - | surpass, surpasses | — |
| 1874 | **wanting** | 5 | 736.04 | 8.494523 | 🟢 medium — moderately distinctive | - | - | — |
| 1875 | **grave** | 5 | 736.04 | 8.494523 | 🟢 medium — moderately distinctive | 0.182094 | - | ~ |
| 1876 | **illustrated** | 5 | 736.04 | 8.494523 | 🟢 medium — moderately distinctive | - | - | — |
| 1877 | **surely** | 5 | 736.04 | 8.494523 | 🟢 medium — moderately distinctive | 0.182201 | - | — |
| 1878 | **undesirable** | 5 | 736.04 | 8.494523 | 🟢 medium — moderately distinctive | 0.182141 | - | — |
| 1879 | **temper** | 5 | 736.04 | 8.494523 | 🟢 medium — moderately distinctive | 0.182379 | - | — |
| 1880 | **lowest** | 7 | 735.95 | 6.066775 | 🟢 medium — moderately distinctive | - | - | — |
| 1881 | **telling** | 6 | 734.86 | 7.067407 | 🟢 medium — moderately distinctive | - | - | — |
| 1882 | **emerge** | 6 | 734.86 | 7.067407 | 🟢 medium — moderately distinctive | 0.223495 | emerge, emerges | — |
| 1883 | **stability** | 8 | 733.27 | 5.28907 | 🟢 medium — moderately distinctive | 0.106842 | - | — |
| 1884 | **attacked** | 6 | 730.78 | 7.028186 | 🟢 medium — moderately distinctive | - | - | — |
| 1885 | **attack** | 7 | 729.02 | 6.009616 | 🟢 medium — moderately distinctive | 0.149302 | attack, attacks | — |
| 1886 | **appropriate** | 7 | 729.02 | 6.009616 | 🟢 medium — moderately distinctive | - | - | — |
| 1887 | **helping** | 6 | 726.86 | 6.990446 | 🟢 medium — moderately distinctive | - | - | — |
| 1888 | **pressing** | 6 | 726.86 | 6.990446 | 🟢 medium — moderately distinctive | - | - | — |
| 1889 | **potential** | 8 | 725.08 | 5.230037 | 🟢 medium — moderately distinctive | 0.108359 | - | — |
| 1890 | **abandoned** | 6 | 723.08 | 6.954078 | 🟢 medium — moderately distinctive | - | - | — |
| 1891 | **treasury** | 9 | 722.73 | 4.633793 | 🟢 medium — moderately distinctive | 0.049193 | - | — |
| 1892 | **guidance** | 5 | 722.69 | 8.340372 | 🟢 medium — moderately distinctive | 0.182328 | - | — |
| 1893 | **beneath** | 5 | 722.69 | 8.340372 | 🟢 medium — moderately distinctive | 0.182483 | - | — |
| 1894 | **smoke** | 5 | 722.69 | 8.340372 | 🟢 medium — moderately distinctive | 0.182478 | - | — |
| 1895 | **solely** | 5 | 722.69 | 8.340372 | 🟢 medium — moderately distinctive | 0.182433 | - | — |
| 1896 | **logic** | 5 | 722.69 | 8.340372 | 🟢 medium — moderately distinctive | 0.182448 | - | — |
| 1897 | **exchanging** | 5 | 722.69 | 8.340372 | 🟢 medium — moderately distinctive | - | - | — |
| 1898 | **maker** | 7 | 719.31 | 5.929574 | 🟢 medium — moderately distinctive | - | - | — |
| 1899 | **principal** | 7 | 717.76 | 5.916835 | 🟢 medium — moderately distinctive | 0.110506 | - | — |
| 1900 | **forced** | 7 | 716.24 | 5.904256 | 🟢 medium — moderately distinctive | - | - | — |
| 1901 | **crucial** | 6 | 715.90 | 6.885085 | 🟢 medium — moderately distinctive | 0.149191 | - | — |
| 1902 | **par** | 6 | 715.90 | 6.885085 | 🟢 medium — moderately distinctive | 0.148934 | - | — |
| 1903 | **fight** | 6 | 712.49 | 6.852295 | 🟢 medium — moderately distinctive | 0.127008 | fight, fights | — |
| 1904 | **succeed** | 6 | 712.49 | 6.852295 | 🟢 medium — moderately distinctive | 0.178963 | succeed, succeeds | — |
| 1905 | **destroying** | 5 | 711.12 | 8.206841 | 🟢 medium — moderately distinctive | - | - | — |
| 1906 | **beer** | 5 | 711.12 | 8.206841 | 🟢 medium — moderately distinctive | 0.181979 | - | — |
| 1907 | **rite** | 5 | 711.12 | 8.206841 | 🟢 medium — moderately distinctive | - | - | — |
| 1908 | **aggression** | 5 | 711.12 | 8.206841 | 🟢 medium — moderately distinctive | 0.182202 | - | — |
| 1909 | **arose** | 5 | 711.12 | 8.206841 | 🟢 medium — moderately distinctive | - | - | — |
| 1910 | **common** | 11 | 710.95 | 3.729504 | 🟢 medium — moderately distinctive | 0.075067 | - | ~ |
| 1911 | **low** | 9 | 708.61 | 4.543279 | 🟢 medium — moderately distinctive | 0.094379 | - | — |
| 1912 | **hit** | 8 | 706.90 | 5.098897 | 🟢 medium — moderately distinctive | 0.123401 | hit, hits | — |
| 1913 | **steady** | 7 | 704.68 | 5.808946 | 🟢 medium — moderately distinctive | 0.110343 | - | — |
| 1914 | **answer** | 6 | 702.89 | 6.759922 | 🟢 medium — moderately distinctive | 0.125433 | answer, answers | — |
| 1915 | **reading** | 5 | 700.91 | 8.089058 | 🟢 medium — moderately distinctive | - | - | — |
| 1916 | **touched** | 5 | 700.91 | 8.089058 | 🟢 medium — moderately distinctive | - | - | — |
| 1917 | **slightly** | 8 | 697.18 | 5.028787 | 🟢 medium — moderately distinctive | 0.108481 | - | — |
| 1918 | **sovereign** | 5 | 691.78 | 7.983697 | 🟢 medium — moderately distinctive | 0.136841 | - | — |
| 1919 | **sooner** | 5 | 691.78 | 7.983697 | 🟢 medium — moderately distinctive | - | - | — |
| 1920 | **accompanied** | 5 | 691.78 | 7.983697 | 🟢 medium — moderately distinctive | - | - | — |
| 1921 | **measure** | 7 | 689.17 | 5.681112 | 🟢 medium — moderately distinctive | 0.175002 | measure, measures | — |
| 1922 | **plant** | 8 | 688.10 | 4.963272 | 🟢 medium — moderately distinctive | 0.216066 | plant, plants | — |
| 1923 | **becoming** | 6 | 685.99 | 6.597403 | 🟢 medium — moderately distinctive | - | - | ✓ སྲིད་པ |
| 1924 | **below** | 9 | 684.14 | 4.386385 | 🟢 medium — moderately distinctive | - | - | — |
| 1925 | **host** | 5 | 683.52 | 7.888387 | 🟢 medium — moderately distinctive | - | host, hosts | — |
| 1926 | **tremendous** | 5 | 683.52 | 7.888387 | 🟢 medium — moderately distinctive | 0.181943 | - | — |
| 1927 | **expert** | 5 | 683.52 | 7.888387 | 🟢 medium — moderately distinctive | 0.182496 | - | — |
| 1928 | **presented** | 6 | 676.08 | 6.502093 | 🟢 medium — moderately distinctive | - | - | — |
| 1929 | **accordingly** | 5 | 675.98 | 7.801376 | 🟢 medium — moderately distinctive | - | - | — |
| 1930 | **criticized** | 5 | 675.98 | 7.801376 | 🟢 medium — moderately distinctive | - | - | — |
| 1931 | **wait** | 6 | 671.46 | 6.457641 | 🟢 medium — moderately distinctive | 0.149251 | - | — |
| 1932 | **hardly** | 5 | 669.05 | 7.721333 | 🟢 medium — moderately distinctive | - | - | — |
| 1933 | **question** | 7 | 668.07 | 5.507159 | 🟢 medium — moderately distinctive | 0.175558 | question, questions | — |
| 1934 | **mar** | 6 | 667.03 | 6.415081 | 🟢 medium — moderately distinctive | 0.149021 | - | — |
| 1935 | **business** | 10 | 666.94 | 3.848531 | 🟢 medium — moderately distinctive | 0.083096 | - | — |
| 1936 | **discouragement** | 4 | 664.99 | 9.593135 | 🟢 medium — moderately distinctive | 0.231470 | - | — |
| 1937 | **utter** | 4 | 664.99 | 9.593135 | 🟢 medium — moderately distinctive | 0.231641 | - | — |
| 1938 | **nepal** | 4 | 664.99 | 9.593135 | 🟢 medium — moderately distinctive | 0.125223 | - | — |
| 1939 | **youth** | 4 | 664.99 | 9.593135 | 🟢 medium — moderately distinctive | 0.230434 | - | — |
| 1940 | **render** | 4 | 664.99 | 9.593135 | 🟢 medium — moderately distinctive | - | render, renders | — |
| 1941 | **breast** | 4 | 664.99 | 9.593135 | 🟢 medium — moderately distinctive | - | breast, breasts | — |
| 1942 | **dissolving** | 4 | 664.99 | 9.593135 | 🟢 medium — moderately distinctive | - | - | — |
| 1943 | **gently** | 4 | 664.99 | 9.593135 | 🟢 medium — moderately distinctive | 0.231397 | - | — |
| 1944 | **intrinsic** | 4 | 664.99 | 9.593135 | 🟢 medium — moderately distinctive | 0.232059 | - | — |
| 1945 | **famine** | 4 | 664.99 | 9.593135 | 🟢 medium — moderately distinctive | 0.231721 | - | — |
| 1946 | **landscape** | 4 | 664.99 | 9.593135 | 🟢 medium — moderately distinctive | - | landscape, landscapes | — |
| 1947 | **cheat** | 4 | 664.99 | 9.593135 | 🟢 medium — moderately distinctive | - | cheat, cheats | — |
| 1948 | **suck** | 4 | 664.99 | 9.593135 | 🟢 medium — moderately distinctive | 0.230684 | - | — |
| 1949 | **stricken** | 4 | 664.99 | 9.593135 | 🟢 medium — moderately distinctive | 0.231427 | - | — |
| 1950 | **wrinkle** | 4 | 664.99 | 9.593135 | 🟢 medium — moderately distinctive | - | - | — |
| 1951 | **pinch** | 4 | 664.99 | 9.593135 | 🟢 medium — moderately distinctive | 0.232110 | - | — |
| 1952 | **weary** | 4 | 664.99 | 9.593135 | 🟢 medium — moderately distinctive | 0.231484 | - | — |
| 1953 | **multiply** | 4 | 664.99 | 9.593135 | 🟢 medium — moderately distinctive | - | multiplies, multiply | — |
| 1954 | **ati** | 4 | 664.99 | 9.593135 | 🟢 medium — moderately distinctive | 0.150427 | - | — |
| 1955 | **spit** | 4 | 664.99 | 9.593135 | 🟢 medium — moderately distinctive | 0.231950 | - | — |
| 1956 | **proud** | 4 | 664.99 | 9.593135 | 🟢 medium — moderately distinctive | 0.231914 | - | — |
| 1957 | **praise** | 4 | 664.99 | 9.593135 | 🟢 medium — moderately distinctive | 0.227397 | - | — |
| 1958 | **sandalwood** | 4 | 664.99 | 9.593135 | 🟢 medium — moderately distinctive | 0.231598 | - | — |
| 1959 | **mentality** | 4 | 664.99 | 9.593135 | 🟢 medium — moderately distinctive | 0.231722 | - | — |
| 1960 | **sweep** | 4 | 664.99 | 9.593135 | 🟢 medium — moderately distinctive | 0.094540 | - | — |
| 1961 | **inherited** | 4 | 664.99 | 9.593135 | 🟢 medium — moderately distinctive | - | - | — |
| 1962 | **whack** | 4 | 664.99 | 9.593135 | 🟢 medium — moderately distinctive | - | whack, whacks | — |
| 1963 | **dawn** | 4 | 664.99 | 9.593135 | 🟢 medium — moderately distinctive | 0.196697 | - | — |
| 1964 | **rubbing** | 4 | 664.99 | 9.593135 | 🟢 medium — moderately distinctive | - | - | — |
| 1965 | **wagon** | 4 | 664.99 | 9.593135 | 🟢 medium — moderately distinctive | - | wagon, wagons | — |
| 1966 | **ear** | 4 | 664.99 | 9.593135 | 🟢 medium — moderately distinctive | - | ear, ears | — |
| 1967 | **radial** | 4 | 664.99 | 9.593135 | 🟢 medium — moderately distinctive | 0.232154 | - | — |
| 1968 | **pleasing** | 4 | 664.99 | 9.593135 | 🟢 medium — moderately distinctive | - | - | — |
| 1969 | **symbolize** | 4 | 664.99 | 9.593135 | 🟢 medium — moderately distinctive | 0.118111 | - | — |
| 1970 | **hindu** | 4 | 664.99 | 9.593135 | 🟢 medium — moderately distinctive | 0.232369 | - | — |
| 1971 | **defect** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | - | - | — |
| 1972 | **conceptualization** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | 0.230841 | - | — |
| 1973 | **circumstantial** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | 0.228318 | - | — |
| 1974 | **ence** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | - | ence, ences | — |
| 1975 | **embody** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | - | embodies, embody | — |
| 1976 | **assimilate** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | 0.230884 | - | — |
| 1977 | **poisoned** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | - | - | — |
| 1978 | **blade** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | - | blade, blades | — |
| 1979 | **stag** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | - | stag, stags | — |
| 1980 | **bee** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | - | bee, bees | — |
| 1981 | **drown** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | 0.231352 | - | — |
| 1982 | **pointless** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | 0.231789 | - | — |
| 1983 | **srona** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | 0.141657 | - | — |
| 1984 | **grasp** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | 0.149407 | - | — |
| 1985 | **diligent** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | 0.232189 | - | — |
| 1986 | **diseas** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | - | - | — |
| 1987 | **trap** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | 0.124388 | trap, traps | — |
| 1988 | **parasol** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | - | parasol, parasols | — |
| 1989 | **entrusted** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | - | - | — |
| 1990 | **invocation** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | 0.108680 | invocation, invocations | — |
| 1991 | **samye** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | 0.132866 | - | ✓ བསམ་ཡས |
| 1992 | **prostitute** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | - | prostitute, prostitutes | — |
| 1993 | **con** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | 0.249804 | - | — |
| 1994 | **joyous** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | 0.131719 | - | ~ |
| 1995 | **exclaimed** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | - | - | — |
| 1996 | **sion** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | - | sion, sions | — |
| 1997 | **infatuation** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | 0.232039 | - | — |
| 1998 | **procrastination** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | 0.231493 | - | — |
| 1999 | **renounced** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | - | - | — |
| 2000 | **unshakeable** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | 0.231115 | - | — |
| 2001 | **univers** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | - | - | — |
| 2002 | **inanimate** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | 0.231600 | - | — |
| 2003 | **gyaltsen** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | 0.132238 | - | ~ |
| 2004 | **fleeting** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | 0.230761 | - | — |
| 2005 | **footstep** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | - | - | — |
| 2006 | **evaporate** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | - | evaporate, evaporates | — |
| 2007 | **footprint** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | - | footprint, footprints | — |
| 2008 | **gaze** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | 0.231897 | - | — |
| 2009 | **isvara** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | 0.231184 | - | — |
| 2010 | **thirty-seven** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | - | - | — |
| 2011 | **gange** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | - | - | — |
| 2012 | **miraculously** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | 0.230202 | - | — |
| 2013 | **clenched** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | - | - | — |
| 2014 | **pillow** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | 0.231878 | - | — |
| 2015 | **nest** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | - | nest, nests | — |
| 2016 | **asura** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | - | - | — |
| 2017 | **laugh** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | - | laugh, laughs | — |
| 2018 | **uncle** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | 0.231632 | - | — |
| 2019 | **robber** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | - | - | — |
| 2020 | **sadness** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | 0.231206 | - | — |
| 2021 | **earnestly** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | 0.232017 | - | — |
| 2022 | **gesh** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | - | - | — |
| 2023 | **sang** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | - | - | — |
| 2024 | **potowa** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | 0.147274 | - | ~ |
| 2025 | **armour** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | 0.230928 | - | — |
| 2026 | **impervious** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | 0.232284 | - | ~ |
| 2027 | **revered** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | - | - | — |
| 2028 | **bent** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | 0.230700 | - | — |
| 2029 | **ember** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | - | - | — |
| 2030 | **joyful** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | 0.196105 | - | ~ |
| 2031 | **grabbed** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | - | - | — |
| 2032 | **crawling** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | - | - | — |
| 2033 | **thicket** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | - | thicket, thickets | — |
| 2034 | **chastity** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | 0.231350 | - | — |
| 2035 | **embrace** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | - | embrace, embraces | — |
| 2036 | **blister** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | 0.219405 | blister, blisters | — |
| 2037 | **gyalpo** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | 0.144073 | - | ~ |
| 2038 | **yeshe** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | 0.132532 | - | ~ |
| 2039 | **tsogyal** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | 0.132549 | - | ~ |
| 2040 | **selve** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | - | - | — |
| 2041 | **kasyapa** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | 0.194143 | - | — |
| 2042 | **shang** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | 0.132308 | - | ~ |
| 2043 | **chaff** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | 0.231744 | - | — |
| 2044 | **heir** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | - | heir, heirs | — |
| 2045 | **shine** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | - | shine, shines | — |
| 2046 | **ignorant** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | 0.231186 | - | — |
| 2047 | **tortured** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | - | - | — |
| 2048 | **enjoyment** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | 0.232249 | - | — |
| 2049 | **terrified** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | - | - | — |
| 2050 | **limitless** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | 0.231500 | - | — |
| 2051 | **adversary** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | - | - | — |
| 2052 | **wolve** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | - | - | — |
| 2053 | **knot** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | - | knot, knots | — |
| 2054 | **frustrating** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | 0.230876 | - | — |
| 2055 | **grateful** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | 0.231074 | - | — |
| 2056 | **smiling** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | - | - | — |
| 2057 | **transmigration** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | 0.230976 | - | — |
| 2058 | **obeyed** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | - | - | — |
| 2059 | **wouldn** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | - | - | — |
| 2060 | **innocent** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | - | innocent, innocents | — |
| 2061 | **ogre** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | - | ogre, ogres | — |
| 2062 | **transgression** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | - | transgression, transgressions | — |
| 2063 | **amassed** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | - | - | — |
| 2064 | **spearman** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | 0.131225 | - | — |
| 2065 | **purnakasyapa** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | 0.131041 | - | — |
| 2066 | **ravati** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | 0.131104 | - | — |
| 2067 | **curd** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | 0.231390 | - | — |
| 2068 | **pebble** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | - | pebble, pebbles | — |
| 2069 | **unerringly** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | 0.231577 | - | — |
| 2070 | **emulating** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | - | - | — |
| 2071 | **versed** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | - | - | — |
| 2072 | **characteristic** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | - | - | — |
| 2073 | **ingratitude** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | 0.231656 | - | — |
| 2074 | **aversion** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | 0.231802 | - | — |
| 2075 | **laughter** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | 0.168434 | - | ~ |
| 2076 | **clay** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | 0.231776 | - | — |
| 2077 | **adept** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | - | adept, adepts | — |
| 2078 | **hip** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | 0.232214 | - | — |
| 2079 | **empow** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | - | - | — |
| 2080 | **adamantine** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | 0.169947 | - | ✓ |
| 2081 | **conferred** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | - | - | — |
| 2082 | **cleanse** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | 0.196303 | - | — |
| 2083 | **eagerness** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | 0.231704 | - | — |
| 2084 | **unfailing** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | 0.232046 | - | — |
| 2085 | **dough** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | 0.232027 | - | — |
| 2086 | **befall** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | 0.231867 | - | — |
| 2087 | **adversity** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | 0.231743 | - | — |
| 2088 | **diligently** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | 0.232209 | - | — |
| 2089 | **perna** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | 0.134442 | - | — |
| 2090 | **subjugate** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | 0.232086 | - | — |
| 2091 | **nostril** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | - | - | — |
| 2092 | **fortress** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | 0.195881 | - | — |
| 2093 | **supernatural** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | 0.232224 | - | — |
| 2094 | **khampa** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | 0.133200 | - | ~ |
| 2095 | **mafijusri** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | 0.134861 | - | — |
| 2096 | **beginner** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | - | beginner, beginners | — |
| 2097 | **awaken** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | - | awaken, awakens | — |
| 2098 | **kar** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | 0.231962 | - | — |
| 2099 | **maitriyogi** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | 0.133613 | - | ✓ བྱམས་པའི་རྣལ་འབྱོར་པ |
| 2100 | **rohita** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | 0.231991 | - | — |
| 2101 | **marici** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | 0.149537 | - | — |
| 2102 | **passion** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | 0.232306 | - | — |
| 2103 | **rinchen** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | 0.134083 | - | ~ |
| 2104 | **ego-clinging** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | - | - | — |
| 2105 | **cleansed** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | - | - | — |
| 2106 | **imagining** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | - | - | — |
| 2107 | **conceptual** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | 0.232166 | - | ~ |
| 2108 | **innate** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | 0.170316 | - | ✓ ལྷན་སྐྱེས |
| 2109 | **lady** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | 0.134336 | - | — |
| 2110 | **perceiving** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | - | - | — |
| 2111 | **worn** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | - | - | — |
| 2112 | **speck** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | - | speck, specks | — |
| 2113 | **damchen** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | 0.150270 | - | ✓ དམ་ཆེན་རྡོ་རྗེ་ལེགས་པ |
| 2114 | **curved** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | - | - | — |
| 2115 | **nirmar** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | 0.232317 | - | — |
| 2116 | **emaho** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | 0.134884 | - | — |
| 2117 | **effortless** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | 0.232326 | - | — |
| 2118 | **pisaka** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | 0.134799 | - | — |
| 2119 | **vajrapar** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | 0.134782 | - | — |
| 2120 | **adhicitta** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | 0.150657 | - | ✓ སེམས་ལྷག་ཅན |
| 2121 | **tulkus** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | 0.228340 | - | — |
| 2122 | **dzogchen** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | 0.134998 | - | — |
| 2123 | **dodrup** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive | 0.150831 | - | — |
| 2124 | **add** | 7 | 664.06 | 5.474098 | 🟢 medium — moderately distinctive | 0.125986 | - | — |
| 2125 | **join** | 6 | 662.79 | 6.374259 | 🟢 medium — moderately distinctive | 0.149194 | - | — |
| 2126 | **explanation** | 5 | 662.63 | 7.647225 | 🟢 medium — moderately distinctive | - | explanation, explanations | — |
| 2127 | **similarly** | 5 | 662.63 | 7.647225 | 🟢 medium — moderately distinctive | 0.156284 | - | — |
| 2128 | **enormous** | 5 | 662.63 | 7.647225 | 🟢 medium — moderately distinctive | 0.181955 | - | — |
| 2129 | **victory** | 5 | 662.63 | 7.647225 | 🟢 medium — moderately distinctive | 0.156416 | - | — |
| 2130 | **won** | 6 | 658.71 | 6.335039 | 🟢 medium — moderately distinctive | - | - | — |
| 2131 | **floor** | 6 | 656.73 | 6.31599 | 🟢 medium — moderately distinctive | 0.149095 | - | — |
| 2132 | **consisting** | 5 | 656.65 | 7.578232 | 🟢 medium — moderately distinctive | - | - | — |
| 2133 | **lasting** | 5 | 656.65 | 7.578232 | 🟢 medium — moderately distinctive | - | - | — |
| 2134 | **watching** | 5 | 656.65 | 7.578232 | 🟢 medium — moderately distinctive | - | - | — |
| 2135 | **directed** | 5 | 656.65 | 7.578232 | 🟢 medium — moderately distinctive | - | - | — |
| 2136 | **suitable** | 5 | 651.05 | 7.513694 | 🟢 medium — moderately distinctive | 0.181968 | - | — |
| 2137 | **spoke** | 5 | 651.05 | 7.513694 | 🟢 medium — moderately distinctive | - | spoke, spokes | — |
| 2138 | **ensure** | 6 | 651.00 | 6.260931 | 🟢 medium — moderately distinctive | 0.178989 | ensure, ensures | — |
| 2139 | **fresh** | 6 | 647.36 | 6.225839 | 🟢 medium — moderately distinctive | 0.149517 | - | — |
| 2140 | **bar** | 5 | 645.80 | 7.453069 | 🟢 medium — moderately distinctive | 0.227780 | bar, bars | — |
| 2141 | **reached** | 8 | 645.37 | 4.655071 | 🟢 medium — moderately distinctive | - | - | — |
| 2142 | **volume** | 7 | 644.93 | 5.316469 | 🟢 medium — moderately distinctive | 0.147096 | volume, volumes | — |
| 2143 | **row** | 6 | 643.83 | 6.191938 | 🟢 medium — moderately distinctive | 0.223477 | row, rows | — |
| 2144 | **context** | 5 | 640.85 | 7.395911 | 🟢 medium — moderately distinctive | 0.228065 | context, contexts | — |
| 2145 | **related** | 7 | 640.79 | 5.282336 | 🟢 medium — moderately distinctive | - | - | — |
| 2146 | **almost** | 7 | 639.18 | 5.269003 | 🟢 medium — moderately distinctive | - | - | ~ |
| 2147 | **running** | 6 | 637.12 | 6.127399 | 🟢 medium — moderately distinctive | - | - | — |
| 2148 | **middling** | 4 | 636.88 | 9.18767 | 🟢 medium — moderately distinctive | - | - | — |
| 2149 | **swallowed** | 4 | 636.88 | 9.18767 | 🟢 medium — moderately distinctive | - | - | — |
| 2150 | **swamp** | 4 | 636.88 | 9.18767 | 🟢 medium — moderately distinctive | - | swamp, swamps | — |
| 2151 | **phrase** | 4 | 636.88 | 9.18767 | 🟢 medium — moderately distinctive | 0.224327 | - | — |
| 2152 | **mistaken** | 4 | 636.88 | 9.18767 | 🟢 medium — moderately distinctive | 0.231356 | - | — |
| 2153 | **deprived** | 4 | 636.88 | 9.18767 | 🟢 medium — moderately distinctive | - | - | — |
| 2154 | **mat** | 4 | 636.88 | 9.18767 | 🟢 medium — moderately distinctive | 0.230932 | - | — |
| 2155 | **mould** | 4 | 636.88 | 9.18767 | 🟢 medium — moderately distinctive | 0.231564 | - | — |
| 2156 | **array** | 4 | 636.88 | 9.18767 | 🟢 medium — moderately distinctive | 0.132297 | - | — |
| 2157 | **irrelevant** | 4 | 636.88 | 9.18767 | 🟢 medium — moderately distinctive | 0.231365 | - | — |
| 2158 | **deserve** | 4 | 636.88 | 9.18767 | 🟢 medium — moderately distinctive | - | deserve, deserves | — |
| 2159 | **spear** | 4 | 636.88 | 9.18767 | 🟢 medium — moderately distinctive | - | - | — |
| 2160 | **epidemic** | 4 | 636.88 | 9.18767 | 🟢 medium — moderately distinctive | - | epidemic, epidemics | — |
| 2161 | **separated** | 4 | 636.88 | 9.18767 | 🟢 medium — moderately distinctive | - | - | — |
| 2162 | **persistently** | 4 | 636.88 | 9.18767 | 🟢 medium — moderately distinctive | 0.230107 | - | — |
| 2163 | **tsang** | 4 | 636.88 | 9.18767 | 🟢 medium — moderately distinctive | 0.130748 | - | — |
| 2164 | **verbal** | 4 | 636.88 | 9.18767 | 🟢 medium — moderately distinctive | 0.232134 | - | — |
| 2165 | **lightly** | 4 | 636.88 | 9.18767 | 🟢 medium — moderately distinctive | 0.231749 | - | — |
| 2166 | **malaya** | 4 | 636.88 | 9.18767 | 🟢 medium — moderately distinctive | 0.133577 | - | — |
| 2167 | **observe** | 4 | 636.88 | 9.18767 | 🟢 medium — moderately distinctive | 0.232076 | - | — |
| 2168 | **interrupt** | 4 | 636.88 | 9.18767 | 🟢 medium — moderately distinctive | 0.196345 | - | — |
| 2169 | **writing** | 5 | 636.16 | 7.341843 | 🟢 medium — moderately distinctive | - | writing, writings | — |
| 2170 | **protecting** | 5 | 636.16 | 7.341843 | 🟢 medium — moderately distinctive | - | - | — |
| 2171 | **heading** | 5 | 636.16 | 7.341843 | 🟢 medium — moderately distinctive | - | heading, headings | — |
| 2172 | **merely** | 5 | 636.16 | 7.341843 | 🟢 medium — moderately distinctive | - | - | — |
| 2173 | **scrap** | 5 | 636.16 | 7.341843 | 🟢 medium — moderately distinctive | 0.180917 | - | — |
| 2174 | **stick** | 5 | 636.16 | 7.341843 | 🟢 medium — moderately distinctive | 0.181149 | - | — |
| 2175 | **conclude** | 5 | 636.16 | 7.341843 | 🟢 medium — moderately distinctive | 0.182225 | - | — |
| 2176 | **star** | 5 | 636.16 | 7.341843 | 🟢 medium — moderately distinctive | 0.171685 | star, stars | — |
| 2177 | **major** | 10 | 634.89 | 3.663546 | 🟢 medium — moderately distinctive | 0.083497 | - | ~ |
| 2178 | **soft** | 6 | 632.36 | 6.08159 | 🟢 medium — moderately distinctive | 0.149201 | - | — |
| 2179 | **distance** | 5 | 631.72 | 7.29055 | 🟢 medium — moderately distinctive | 0.181323 | - | — |
| 2180 | **pleased** | 5 | 631.72 | 7.29055 | 🟢 medium — moderately distinctive | - | - | — |
| 2181 | **developed** | 6 | 630.82 | 6.066775 | 🟢 medium — moderately distinctive | - | - | — |
| 2182 | **build** | 6 | 629.30 | 6.052176 | 🟢 medium — moderately distinctive | 0.055945 | - | — |
| 2183 | **cost** | 8 | 628.99 | 4.536889 | 🟢 medium — moderately distinctive | 0.172671 | cost, costs | — |
| 2184 | **satisfy** | 5 | 627.49 | 7.24176 | 🟢 medium — moderately distinctive | 0.061514 | - | — |
| 2185 | **spring** | 6 | 624.87 | 6.009616 | 🟢 medium — moderately distinctive | 0.177493 | spring, springs | — |
| 2186 | **continuous** | 5 | 623.46 | 7.19524 | 🟢 medium — moderately distinctive | 0.181938 | - | — |
| 2187 | **resource** | 5 | 623.46 | 7.19524 | 🟢 medium — moderately distinctive | - | - | — |
| 2188 | **hoping** | 5 | 619.61 | 7.150788 | 🟢 medium — moderately distinctive | - | - | — |
| 2189 | **daily** | 7 | 617.19 | 5.087785 | 🟢 medium — moderately distinctive | 0.125952 | - | — |
| 2190 | **sage** | 4 | 616.94 | 8.899988 | 🟢 medium — moderately distinctive | 0.258182 | sage, sages | — |
| 2191 | **counting** | 4 | 616.94 | 8.899988 | 🟢 medium — moderately distinctive | - | - | — |
| 2192 | **fierce** | 4 | 616.94 | 8.899988 | 🟢 medium — moderately distinctive | 0.230755 | - | — |
| 2193 | **penetrate** | 4 | 616.94 | 8.899988 | 🟢 medium — moderately distinctive | 0.231807 | - | — |
| 2194 | **recipient** | 4 | 616.94 | 8.899988 | 🟢 medium — moderately distinctive | - | recipient, recipients | — |
| 2195 | **hook** | 4 | 616.94 | 8.899988 | 🟢 medium — moderately distinctive | - | hook, hooks | — |
| 2196 | **condemned** | 4 | 616.94 | 8.899988 | 🟢 medium — moderately distinctive | - | - | — |
| 2197 | **abundance** | 4 | 616.94 | 8.899988 | 🟢 medium — moderately distinctive | 0.230962 | - | — |
| 2198 | **prosperity** | 4 | 616.94 | 8.899988 | 🟢 medium — moderately distinctive | 0.231646 | - | — |
| 2199 | **sat** | 4 | 616.94 | 8.899988 | 🟢 medium — moderately distinctive | - | - | — |
| 2200 | **tower** | 4 | 616.94 | 8.899988 | 🟢 medium — moderately distinctive | - | tower, towers | — |
| 2201 | **eradicate** | 4 | 616.94 | 8.899988 | 🟢 medium — moderately distinctive | 0.232248 | - | — |
| 2202 | **obtaining** | 5 | 615.92 | 7.108229 | 🟢 medium — moderately distinctive | - | - | — |
| 2203 | **determined** | 6 | 612.63 | 5.891833 | 🟢 medium — moderately distinctive | - | - | — |
| 2204 | **load** | 5 | 612.38 | 7.067407 | 🟢 medium — moderately distinctive | 0.227735 | load, loads | — |
| 2205 | **degree** | 5 | 608.99 | 7.028186 | 🟢 medium — moderately distinctive | 0.181504 | - | — |
| 2206 | **prepare** | 5 | 608.99 | 7.028186 | 🟢 medium — moderately distinctive | 0.074937 | - | — |
| 2207 | **protected** | 5 | 608.99 | 7.028186 | 🟢 medium — moderately distinctive | - | - | — |
| 2208 | **eastern** | 6 | 608.85 | 5.855466 | 🟢 medium — moderately distinctive | 0.129479 | - | — |
| 2209 | **pick** | 5 | 605.72 | 6.990446 | 🟢 medium — moderately distinctive | - | pick, picks | — |
| 2210 | **generate** | 5 | 605.72 | 6.990446 | 🟢 medium — moderately distinctive | 0.182294 | - | — |
| 2211 | **factor** | 6 | 605.20 | 5.820374 | 🟢 medium — moderately distinctive | 0.177135 | factor, factors | — |
| 2212 | **leading** | 7 | 605.08 | 4.987965 | 🟢 medium — moderately distinctive | - | - | — |
| 2213 | **corresponding** | 5 | 602.56 | 6.954078 | 🟢 medium — moderately distinctive | - | - | — |
| 2214 | **contact** | 5 | 602.56 | 6.954078 | 🟢 medium — moderately distinctive | 0.182510 | - | — |
| 2215 | **motivated** | 4 | 601.47 | 8.676844 | 🟢 medium — moderately distinctive | - | - | — |
| 2216 | **notion** | 4 | 601.47 | 8.676844 | 🟢 medium — moderately distinctive | - | notion, notions | — |
| 2217 | **absent** | 4 | 601.47 | 8.676844 | 🟢 medium — moderately distinctive | 0.230581 | - | — |
| 2218 | **arriving** | 4 | 601.47 | 8.676844 | 🟢 medium — moderately distinctive | - | - | — |
| 2219 | **remind** | 4 | 601.47 | 8.676844 | 🟢 medium — moderately distinctive | 0.231012 | - | — |
| 2220 | **collection** | 4 | 601.47 | 8.676844 | 🟢 medium — moderately distinctive | 0.195879 | - | — |
| 2221 | **breathing** | 4 | 601.47 | 8.676844 | 🟢 medium — moderately distinctive | - | - | — |
| 2222 | **casting** | 4 | 601.47 | 8.676844 | 🟢 medium — moderately distinctive | - | - | — |
| 2223 | **pearl** | 4 | 601.47 | 8.676844 | 🟢 medium — moderately distinctive | - | - | — |
| 2224 | **washed** | 4 | 601.47 | 8.676844 | 🟢 medium — moderately distinctive | - | - | — |
| 2225 | **interruption** | 4 | 601.47 | 8.676844 | 🟢 medium — moderately distinctive | 0.232175 | - | — |
| 2226 | **chen** | 4 | 601.47 | 8.676844 | 🟢 medium — moderately distinctive | 0.135022 | - | — |
| 2227 | **drawn** | 5 | 599.52 | 6.918987 | 🟢 medium — moderately distinctive | - | - | — |
| 2228 | **mixed** | 5 | 599.52 | 6.918987 | 🟢 medium — moderately distinctive | 0.182436 | - | — |
| 2229 | **progress** | 6 | 599.39 | 5.764494 | 🟢 medium — moderately distinctive | 0.149456 | - | — |
| 2230 | **spot** | 6 | 598.26 | 5.753683 | 🟢 medium — moderately distinctive | 0.148922 | - | — |
| 2231 | **container** | 5 | 596.59 | 6.885085 | 🟢 medium — moderately distinctive | 0.227625 | container, containers | — |
| 2232 | **grant** | 5 | 593.75 | 6.852295 | 🟢 medium — moderately distinctive | 0.228181 | grant, grants | — |
| 2233 | **facing** | 5 | 593.75 | 6.852295 | 🟢 medium — moderately distinctive | - | - | — |
| 2234 | **held** | 8 | 591.67 | 4.267689 | 🟢 medium — moderately distinctive | - | - | — |
| 2235 | **conflict** | 5 | 590.99 | 6.820546 | 🟢 medium — moderately distinctive | 0.186818 | conflict, conflicts | — |
| 2236 | **sour** | 5 | 590.99 | 6.820546 | 🟢 medium — moderately distinctive | 0.182520 | - | — |
| 2237 | **basic** | 6 | 589.68 | 5.671162 | 🟢 medium — moderately distinctive | 0.112772 | - | — |
| 2238 | **burst** | 4 | 588.83 | 8.494523 | 🟢 medium — moderately distinctive | 0.192133 | - | — |
| 2239 | **castle** | 4 | 588.83 | 8.494523 | 🟢 medium — moderately distinctive | 0.168387 | - | — |
| 2240 | **lamb** | 4 | 588.83 | 8.494523 | 🟢 medium — moderately distinctive | - | - | — |
| 2241 | **character** | 4 | 588.83 | 8.494523 | 🟢 medium — moderately distinctive | - | character, characters | — |
| 2242 | **delighted** | 4 | 588.83 | 8.494523 | 🟢 medium — moderately distinctive | - | - | — |
| 2243 | **filling** | 4 | 588.83 | 8.494523 | 🟢 medium — moderately distinctive | - | - | — |
| 2244 | **messenger** | 4 | 588.83 | 8.494523 | 🟢 medium — moderately distinctive | 0.231926 | - | — |
| 2245 | **autumn** | 5 | 585.74 | 6.759922 | 🟢 medium — moderately distinctive | 0.180404 | - | — |
| 2246 | **variety** | 5 | 583.23 | 6.730934 | 🟢 medium — moderately distinctive | 0.231592 | varieties, variety | — |
| 2247 | **holder** | 5 | 583.23 | 6.730934 | 🟢 medium — moderately distinctive | 0.182301 | - | — |
| 2248 | **adverse** | 5 | 580.79 | 6.702763 | 🟢 medium — moderately distinctive | 0.154304 | - | — |
| 2249 | **easier** | 5 | 580.79 | 6.702763 | 🟢 medium — moderately distinctive | - | - | — |
| 2250 | **strike** | 6 | 579.86 | 5.576752 | 🟢 medium — moderately distinctive | 0.147519 | - | — |
| 2251 | **notice** | 5 | 578.41 | 6.675364 | 🟢 medium — moderately distinctive | 0.182216 | - | — |
| 2252 | **drawing** | 5 | 578.41 | 6.675364 | 🟢 medium — moderately distinctive | - | drawing, drawings | — |
| 2253 | **province** | 5 | 578.41 | 6.675364 | 🟢 medium — moderately distinctive | - | province, provinces | — |
| 2254 | **upper** | 5 | 578.41 | 6.675364 | 🟢 medium — moderately distinctive | 0.182668 | - | — |
| 2255 | **consequence** | 4 | 578.15 | 8.340372 | 🟢 medium — moderately distinctive | - | - | — |
| 2256 | **upset** | 4 | 578.15 | 8.340372 | 🟢 medium — moderately distinctive | 0.231779 | - | — |
| 2257 | **refuse** | 4 | 578.15 | 8.340372 | 🟢 medium — moderately distinctive | 0.108190 | - | — |
| 2258 | **achievement** | 4 | 578.15 | 8.340372 | 🟢 medium — moderately distinctive | - | - | — |
| 2259 | **gateway** | 4 | 578.15 | 8.340372 | 🟢 medium — moderately distinctive | 0.231712 | - | — |
| 2260 | **expressing** | 4 | 578.15 | 8.340372 | 🟢 medium — moderately distinctive | - | - | — |
| 2261 | **valley** | 5 | 576.10 | 6.648696 | 🟢 medium — moderately distinctive | - | valley, valleys | — |
| 2262 | **service** | 7 | 575.14 | 4.741105 | 🟢 medium — moderately distinctive | 0.219437 | service, services | — |
| 2263 | **stance** | 5 | 573.85 | 6.622721 | 🟢 medium — moderately distinctive | 0.225551 | stance, stances | — |
| 2264 | **final** | 7 | 571.87 | 4.714128 | 🟢 medium — moderately distinctive | 0.125397 | - | — |
| 2265 | **war** | 6 | 570.04 | 5.482261 | 🟢 medium — moderately distinctive | 0.178143 | war, wars | — |
| 2266 | **livestock** | 5 | 569.52 | 6.57271 | 🟢 medium — moderately distinctive | 0.181435 | - | — |
| 2267 | **ignore** | 4 | 568.89 | 8.206841 | 🟢 medium — moderately distinctive | - | ignore, ignores | — |
| 2268 | **personally** | 4 | 568.89 | 8.206841 | 🟢 medium — moderately distinctive | 0.231911 | - | — |
| 2269 | **ita** | 4 | 568.89 | 8.206841 | 🟢 medium — moderately distinctive | - | - | — |
| 2270 | **retreat** | 4 | 568.89 | 8.206841 | 🟢 medium — moderately distinctive | - | retreat, retreats | — |
| 2271 | **crystal** | 4 | 568.89 | 8.206841 | 🟢 medium — moderately distinctive | 0.232259 | - | — |
| 2272 | **studying** | 5 | 565.39 | 6.525082 | 🟢 medium — moderately distinctive | - | - | — |
| 2273 | **good** | 7 | 563.83 | 4.647928 | 🟢 medium — moderately distinctive | 0.000894 | - | ~ |
| 2274 | **identify** | 5 | 561.45 | 6.47962 | 🟢 medium — moderately distinctive | 0.231482 | identifies, identify | — |
| 2275 | **stopped** | 5 | 561.45 | 6.47962 | 🟢 medium — moderately distinctive | - | - | — |
| 2276 | **discouraged** | 4 | 560.73 | 8.089058 | 🟢 medium — moderately distinctive | - | - | — |
| 2277 | **era** | 4 | 560.73 | 8.089058 | 🟢 medium — moderately distinctive | 0.231632 | - | — |
| 2278 | **anywhere** | 4 | 560.73 | 8.089058 | 🟢 medium — moderately distinctive | - | - | — |
| 2279 | **hammer** | 4 | 560.73 | 8.089058 | 🟢 medium — moderately distinctive | - | - | — |
| 2280 | **destined** | 4 | 560.73 | 8.089058 | 🟢 medium — moderately distinctive | - | - | — |
| 2281 | **popularity** | 4 | 560.73 | 8.089058 | 🟢 medium — moderately distinctive | 0.231470 | - | — |
| 2282 | **playing** | 4 | 560.73 | 8.089058 | 🟢 medium — moderately distinctive | - | - | — |
| 2283 | **performing** | 4 | 560.73 | 8.089058 | 🟢 medium — moderately distinctive | - | - | — |
| 2284 | **spreading** | 4 | 560.73 | 8.089058 | 🟢 medium — moderately distinctive | - | - | — |
| 2285 | **desirable** | 4 | 560.73 | 8.089058 | 🟢 medium — moderately distinctive | 0.232020 | - | — |
| 2286 | **shown** | 5 | 559.55 | 6.457641 | 🟢 medium — moderately distinctive | - | - | — |
| 2287 | **pushed** | 5 | 559.55 | 6.457641 | 🟢 medium — moderately distinctive | - | - | — |
| 2288 | **interest** | 9 | 555.63 | 3.56245 | 🟢 medium — moderately distinctive | 0.106237 | interest, interests | — |
| 2289 | **express** | 5 | 554.07 | 6.394462 | 🟢 medium — moderately distinctive | 0.231724 | express, expresses | — |
| 2290 | **reveal** | 4 | 553.42 | 7.983697 | 🟢 medium — moderately distinctive | 0.232032 | - | — |
| 2291 | **shot** | 4 | 553.42 | 7.983697 | 🟢 medium — moderately distinctive | - | - | — |
| 2292 | **crush** | 4 | 553.42 | 7.983697 | 🟢 medium — moderately distinctive | 0.083042 | crush, crushes | — |
| 2293 | **behalf** | 5 | 552.32 | 6.374259 | 🟢 medium — moderately distinctive | 0.182596 | - | — |
| 2294 | **decline** | 7 | 550.75 | 4.540079 | 🟢 medium — moderately distinctive | 0.174566 | decline, declines | — |
| 2295 | **reduce** | 7 | 548.45 | 4.521091 | 🟢 medium — moderately distinctive | 0.146889 | reduce, reduces | — |
| 2296 | **eventually** | 5 | 547.27 | 6.31599 | 🟢 medium — moderately distinctive | 0.182032 | - | — |
| 2297 | **relying** | 4 | 546.82 | 7.888387 | 🟢 medium — moderately distinctive | - | - | — |
| 2298 | **simultaneously** | 4 | 546.82 | 7.888387 | 🟢 medium — moderately distinctive | 0.231870 | - | — |
| 2299 | **undertaking** | 4 | 546.82 | 7.888387 | 🟢 medium — moderately distinctive | - | undertaking, undertakings | — |
| 2300 | **visiting** | 4 | 546.82 | 7.888387 | 🟢 medium — moderately distinctive | - | - | — |
| 2301 | **provoke** | 4 | 546.82 | 7.888387 | 🟢 medium — moderately distinctive | - | provoke, provokes | — |
| 2302 | **demanding** | 4 | 546.82 | 7.888387 | 🟢 medium — moderately distinctive | - | - | — |
| 2303 | **undertake** | 4 | 546.82 | 7.888387 | 🟢 medium — moderately distinctive | - | undertake, undertakes | — |
| 2304 | **saved** | 4 | 546.82 | 7.888387 | 🟢 medium — moderately distinctive | - | - | — |
| 2305 | **insisted** | 4 | 546.82 | 7.888387 | 🟢 medium — moderately distinctive | - | - | — |
| 2306 | **split** | 7 | 546.56 | 4.505539 | 🟢 medium — moderately distinctive | 0.150993 | split, splits | — |
| 2307 | **produced** | 6 | 545.82 | 5.24933 | 🟢 medium — moderately distinctive | - | - | — |
| 2308 | **movement** | 5 | 542.50 | 6.260931 | 🟢 medium — moderately distinctive | - | movement, movements | ~ |
| 2309 | **conflicting** | 4 | 540.79 | 7.801376 | 🟢 medium — moderately distinctive | - | - | — |
| 2310 | **neighbouring** | 4 | 540.79 | 7.801376 | 🟢 medium — moderately distinctive | - | - | — |
| 2311 | **mature** | 4 | 540.79 | 7.801376 | 🟢 medium — moderately distinctive | 0.232231 | - | — |
| 2312 | **lift** | 5 | 539.46 | 6.225839 | 🟢 medium — moderately distinctive | 0.226780 | lift, lifts | — |
| 2313 | **swift** | 4 | 535.24 | 7.721333 | 🟢 medium — moderately distinctive | 0.230657 | - | — |
| 2314 | **salt** | 4 | 535.24 | 7.721333 | 🟢 medium — moderately distinctive | 0.231526 | - | — |
| 2315 | **fraud** | 4 | 535.24 | 7.721333 | 🟢 medium — moderately distinctive | - | fraud, frauds | — |
| 2316 | **silver** | 5 | 535.09 | 6.175409 | 🟢 medium — moderately distinctive | 0.182275 | - | — |
| 2317 | **extreme** | 4 | 530.10 | 7.647225 | 🟢 medium — moderately distinctive | - | extreme, extremes | — |
| 2318 | **happening** | 4 | 530.10 | 7.647225 | 🟢 medium — moderately distinctive | - | happening, happenings | — |
| 2319 | **achieving** | 4 | 530.10 | 7.647225 | 🟢 medium — moderately distinctive | - | - | — |
| 2320 | **avoiding** | 4 | 530.10 | 7.647225 | 🟢 medium — moderately distinctive | - | - | — |
| 2321 | **eager** | 4 | 530.10 | 7.647225 | 🟢 medium — moderately distinctive | 0.231784 | - | — |
| 2322 | **tomorrow** | 6 | 527.31 | 5.071347 | 🟢 medium — moderately distinctive | 0.148880 | - | — |
| 2323 | **personal** | 5 | 526.96 | 6.08159 | 🟢 medium — moderately distinctive | 0.181990 | - | — |
| 2324 | **member** | 6 | 526.75 | 5.065927 | 🟢 medium — moderately distinctive | 0.179077 | member, members | — |
| 2325 | **useful** | 4 | 525.32 | 7.578232 | 🟢 medium — moderately distinctive | - | - | — |
| 2326 | **regardless** | 4 | 525.32 | 7.578232 | 🟢 medium — moderately distinctive | - | - | — |
| 2327 | **hurt** | 5 | 524.42 | 6.052176 | 🟢 medium — moderately distinctive | 0.227733 | hurt, hurts | — |
| 2328 | **royal** | 5 | 524.42 | 6.052176 | 🟢 medium — moderately distinctive | 0.182342 | - | ~ |
| 2329 | **sharp** | 6 | 522.35 | 5.023592 | 🟢 medium — moderately distinctive | 0.148741 | - | — |
| 2330 | **decide** | 5 | 521.94 | 6.023602 | 🟢 medium — moderately distinctive | 0.083721 | decide, decides | — |
| 2331 | **relation** | 4 | 520.84 | 7.513694 | 🟢 medium — moderately distinctive | - | relation, relations | — |
| 2332 | **connected** | 4 | 520.84 | 7.513694 | 🟢 medium — moderately distinctive | - | - | — |
| 2333 | **ought** | 4 | 520.84 | 7.513694 | 🟢 medium — moderately distinctive | - | - | — |
| 2334 | **belt** | 4 | 520.84 | 7.513694 | 🟢 medium — moderately distinctive | 0.231712 | - | — |
| 2335 | **profit** | 9 | 519.33 | 3.329737 | 🟢 medium — moderately distinctive | 0.105943 | profit, profits | — |
| 2336 | **confident** | 5 | 518.35 | 5.982217 | 🟢 medium — moderately distinctive | 0.181992 | - | — |
| 2337 | **contrary** | 4 | 516.64 | 7.453069 | 🟢 medium — moderately distinctive | 0.228232 | - | — |
| 2338 | **laid** | 4 | 516.64 | 7.453069 | 🟢 medium — moderately distinctive | - | - | — |
| 2339 | **accordance** | 4 | 516.64 | 7.453069 | 🟢 medium — moderately distinctive | 0.231817 | - | — |
| 2340 | **promise** | 4 | 516.64 | 7.453069 | 🟢 medium — moderately distinctive | 0.190961 | - | — |
| 2341 | **cotton** | 5 | 514.91 | 5.942477 | 🟢 medium — moderately distinctive | 0.182370 | - | — |
| 2342 | **acquired** | 7 | 514.79 | 4.24365 | 🟢 medium — moderately distinctive | - | - | — |
| 2343 | **yes** | 4 | 512.68 | 7.395911 | 🟢 medium — moderately distinctive | - | - | — |
| 2344 | **regard** | 4 | 512.68 | 7.395911 | 🟢 medium — moderately distinctive | 0.231094 | - | — |
| 2345 | **subsequently** | 4 | 512.68 | 7.395911 | 🟢 medium — moderately distinctive | 0.232221 | - | — |
| 2346 | **shoe** | 4 | 512.68 | 7.395911 | 🟢 medium — moderately distinctive | 0.231776 | - | — |
| 2347 | **repair** | 4 | 512.68 | 7.395911 | 🟢 medium — moderately distinctive | - | repair, repairs | — |
| 2348 | **associated** | 5 | 510.52 | 5.891833 | 🟢 medium — moderately distinctive | - | - | — |
| 2349 | **require** | 5 | 509.46 | 5.879563 | 🟢 medium — moderately distinctive | - | require, requires | — |
| 2350 | **wake** | 4 | 508.93 | 7.341843 | 🟢 medium — moderately distinctive | 0.229924 | - | — |
| 2351 | **spell** | 4 | 508.93 | 7.341843 | 🟢 medium — moderately distinctive | - | - | — |
| 2352 | **plunged** | 4 | 505.38 | 7.29055 | 🟢 medium — moderately distinctive | - | - | — |
| 2353 | **site** | 4 | 505.38 | 7.29055 | 🟢 medium — moderately distinctive | 0.232341 | - | — |
| 2354 | **unknown** | 4 | 501.99 | 7.24176 | 🟢 medium — moderately distinctive | 0.231633 | - | — |
| 2355 | **couple** | 4 | 501.99 | 7.24176 | 🟢 medium — moderately distinctive | - | couple, couples | — |
| 2356 | **your** | 4 | 501.99 | 7.24176 | 🟢 medium — moderately distinctive | - | - | — |
| 2357 | **risk** | 5 | 500.44 | 5.775423 | 🟢 medium — moderately distinctive | 0.182394 | - | — |
| 2358 | **pay** | 8 | 500.20 | 3.60794 | 🟢 medium — moderately distinctive | 0.107870 | - | — |
| 2359 | **edge** | 4 | 498.77 | 7.19524 | 🔵 low — common in general English | 0.231759 | - | — |
| 2360 | **irreversible** | 3 | 498.74 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 2361 | **inclination** | 3 | 498.74 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 2362 | **shelter** | 3 | 498.74 | 9.593135 | 🔵 low — common in general English | - | shelter, shelters | — |
| 2363 | **sixty** | 3 | 498.74 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 2364 | **wooden** | 3 | 498.74 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 2365 | **tossed** | 3 | 498.74 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 2366 | **armoured** | 3 | 498.74 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 2367 | **pierce** | 3 | 498.74 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 2368 | **envy** | 3 | 498.74 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 2369 | **folk** | 3 | 498.74 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 2370 | **cas** | 3 | 498.74 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 2371 | **uncomfortable** | 3 | 498.74 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 2372 | **spoiled** | 3 | 498.74 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 2373 | **talent** | 3 | 498.74 | 9.593135 | 🔵 low — common in general English | - | talent, talents | — |
| 2374 | **piling** | 3 | 498.74 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 2375 | **glory** | 3 | 498.74 | 9.593135 | 🔵 low — common in general English | - | glories, glory | — |
| 2376 | **fearing** | 3 | 498.74 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 2377 | **tiger** | 3 | 498.74 | 9.593135 | 🔵 low — common in general English | - | tiger, tigers | — |
| 2378 | **stir** | 3 | 498.74 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 2379 | **organ** | 3 | 498.74 | 9.593135 | 🔵 low — common in general English | - | organ, organs | — |
| 2380 | **whipped** | 3 | 498.74 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 2381 | **cultivated** | 3 | 498.74 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 2382 | **drowned** | 3 | 498.74 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 2383 | **correctly** | 3 | 498.74 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 2384 | **monster** | 3 | 498.74 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 2385 | **sur** | 3 | 498.74 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 2386 | **healed** | 3 | 498.74 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 2387 | **breathe** | 3 | 498.74 | 9.593135 | 🔵 low — common in general English | 0.232160 | - | — |
| 2388 | **stealing** | 3 | 498.74 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 2389 | **tail** | 3 | 498.74 | 9.593135 | 🔵 low — common in general English | - | tail, tails | — |
| 2390 | **mixing** | 3 | 498.74 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 2391 | **pair** | 3 | 498.74 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 2392 | **elder** | 3 | 498.74 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 2393 | **handful** | 3 | 498.74 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 2394 | **steadfast** | 3 | 498.74 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 2395 | **tired** | 3 | 498.74 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 2396 | **furious** | 3 | 498.74 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 2397 | **meth** | 3 | 498.74 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 2398 | **robbed** | 3 | 498.74 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 2399 | **elaboration** | 3 | 498.74 | 9.593135 | 🔵 low — common in general English | - | elaboration, elaborations | — |
| 2400 | **chased** | 3 | 498.74 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 2401 | **saddle** | 3 | 498.74 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 2402 | **crippled** | 3 | 498.74 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 2403 | **plausible** | 3 | 498.74 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 2404 | **myriad** | 3 | 498.74 | 9.593135 | 🔵 low — common in general English | - | myriad, myriads | — |
| 2405 | **hero** | 3 | 498.74 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 2406 | **misfortune** | 3 | 498.74 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 2407 | **dispense** | 3 | 498.74 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 2408 | **unaltered** | 3 | 498.74 | 9.593135 | 🔵 low — common in general English | - | - | ✓ མ་བཅོས་པ |
| 2409 | **petal** | 3 | 498.74 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 2410 | **dancing** | 3 | 498.74 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 2411 | **gracious** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | 0.221874 | - | — |
| 2412 | **quintessential** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - | - | — |
| 2413 | **copper-coloured** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - | - | — |
| 2414 | **hevajra** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | 0.190399 | - | — |
| 2415 | **pore** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - | pore, pores | — |
| 2416 | **gossip** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - | - | — |
| 2417 | **prac** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - | - | — |
| 2418 | **contempt** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - | - | — |
| 2419 | **flaming** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - | - | — |
| 2420 | **inferno** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - | inferno, infernos | — |
| 2421 | **engrossed** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - | - | — |
| 2422 | **gnawing** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - | - | — |
| 2423 | **labdron** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | 0.193213 | - | ~ |
| 2424 | **thirsty** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - | - | — |
| 2425 | **vowing** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - | - | — |
| 2426 | **elixir** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - | elixir, elixirs | — |
| 2427 | **conquer** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - | conquer, conquers | — |
| 2428 | **musk-deer** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - | - | — |
| 2429 | **musk** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - | - | — |
| 2430 | **brimming** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - | - | — |
| 2431 | **long-lived** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - | - | — |
| 2432 | **mute** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - | - | — |
| 2433 | **inheriting** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - | - | — |
| 2434 | **pernicious** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - | - | — |
| 2435 | **lha-thothori** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - | - | — |
| 2436 | **nyentsen** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | 0.193784 | - | — |
| 2437 | **alphabet** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - | - | — |
| 2438 | **avalokitdvara** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | 0.191261 | - | — |
| 2439 | **sery** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - | - | — |
| 2440 | **preceptor** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - | preceptor, preceptors | — |
| 2441 | **unite** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | 0.232391 | unite, unites | — |
| 2442 | **forty** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - | - | — |
| 2443 | **smrtijnana** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | 0.177135 | - | — |
| 2444 | **wept** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - | - | — |
| 2445 | **accom** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - | - | — |
| 2446 | **glimmer** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - | glimmer, glimmers | — |
| 2447 | **servitude** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - | - | — |
| 2448 | **habit** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - | habit, habits | — |
| 2449 | **tightly** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - | - | — |
| 2450 | **brew** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - | - | — |
| 2451 | **surabhibhadra** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | 0.188818 | - | — |
| 2452 | **upright** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - | - | — |
| 2453 | **promis** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - | - | — |
| 2454 | **slept** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - | - | — |
| 2455 | **spittle** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - | - | — |
| 2456 | **noose** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - | - | — |
| 2457 | **brilliance** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - | - | — |
| 2458 | **chest** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | 0.254164 | - | — |
| 2459 | **alight** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - | - | — |
| 2460 | **tsenpo** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | 0.191054 | - | — |
| 2461 | **tsen** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | 0.214751 | - | — |
| 2462 | **radiance** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - | - | — |
| 2463 | **wrong-doing** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - | - | — |
| 2464 | **shower** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - | shower, showers | — |
| 2465 | **breez** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - | - | — |
| 2466 | **enmity** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - | - | — |
| 2467 | **brocade** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - | brocade, brocades | — |
| 2468 | **cheek** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - | - | — |
| 2469 | **murdered** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - | - | — |
| 2470 | **starving** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - | - | — |
| 2471 | **affectionate** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - | - | — |
| 2472 | **tingri** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | 0.188388 | - | — |
| 2473 | **barren** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - | - | — |
| 2474 | **everlasting** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - | - | — |
| 2475 | **relish** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - | - | — |
| 2476 | **trivial** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - | - | — |
| 2477 | **murder** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - | - | — |
| 2478 | **daughter-in-law** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - | - | — |
| 2479 | **courageously** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - | - | — |
| 2480 | **thieve** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - | - | — |
| 2481 | **mortal** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - | - | — |
| 2482 | **single-mindedly** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - | - | — |
| 2483 | **experi** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - | - | — |
| 2484 | **amassing** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - | - | — |
| 2485 | **greasy** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - | - | — |
| 2486 | **arous** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - | - | — |
| 2487 | **assimilated** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - | - | — |
| 2488 | **yama** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - | - | ✓ གཤིན་རྗེ |
| 2489 | **chopped** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - | - | — |
| 2490 | **prong** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - | - | — |
| 2491 | **beak** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - | beak, beaks | — |
| 2492 | **devour** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | 0.254280 | - | — |
| 2493 | **razor** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - | razor, razors | — |
| 2494 | **biting** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - | - | — |
| 2495 | **brain** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - | brain, brains | — |
| 2496 | **moun** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - | - | — |
| 2497 | **tain** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - | - | — |
| 2498 | **lamenting** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - | - | — |
| 2499 | **lingje** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | 0.214033 | - | ~ |
| 2500 | **lung** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - | lung, lungs | — |
| 2501 | **uttered** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - | - | — |
| 2502 | **entrail** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - | - | — |
| 2503 | **derge** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | 0.184928 | - | — |
| 2504 | **intellectually** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - | - | — |
| 2505 | **karmapa** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - | karmapa, karmapas | ✓ ཀར་མ་པ |
| 2506 | **obsessed** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - | - | — |
| 2507 | **avarice** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - | - | — |
| 2508 | **dish** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - | dish, dishes | — |
| 2509 | **nose** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - | - | — |
| 2510 | **ugliness** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - | - | — |
| 2511 | **snot** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - | - | — |
| 2512 | **mamo** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - | mamo, mamos | ✓ མ་མོ |
| 2513 | **happily** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - | - | — |
| 2514 | **bum** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - | bum, bums | — |
| 2515 | **regretting** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - | - | — |
| 2516 | **accumu** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - | - | — |
| 2517 | **plunder** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - | plunder, plunders | — |
| 2518 | **leprosy** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - | - | — |
| 2519 | **pregnancy** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - | - | — |
| 2520 | **creep** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - | creep, creeps | — |
| 2521 | **granny** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - | - | — |
| 2522 | **frown** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - | frown, frowns | — |
| 2523 | **ugly** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - | - | — |
| 2524 | **insipid** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - | - | — |
| 2525 | **lax** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | 0.257781 | - | — |
| 2526 | **left-over** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - | - | — |
| 2527 | **unclean** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - | - | — |
| 2528 | **apparition** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - | apparition, apparitions | — |
| 2529 | **steeped** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - | - | — |
| 2530 | **married** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - | - | — |
| 2531 | **rosary** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - | - | — |
| 2532 | **kindly** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - | - | — |
| 2533 | **exhort** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - | exhort, exhorts | — |
| 2534 | **disgust** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - | - | — |
| 2535 | **demigod** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - | - | ✓ ལྷ་མ་ཡིན |
| 2536 | **wish-fulfilling** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - | - | — |
| 2537 | **waking** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - | - | — |
| 2538 | **imagination** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - | - | — |
| 2539 | **one-eyed** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - | - | — |
| 2540 | **affection** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - | - | — |
| 2541 | **mahayana** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | 0.189334 | - | — |
| 2542 | **slaughterer** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - | slaughterer, slaughterers | — |
| 2543 | **streaming** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - | - | — |
| 2544 | **shortcoming** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - | shortcoming, shortcomings | — |
| 2545 | **laypeople** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - | - | — |
| 2546 | **phoney** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - | - | — |
| 2547 | **deceive** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - | - | — |
| 2548 | **harshly** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - | - | — |
| 2549 | **robbery** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - | - | — |
| 2550 | **eternalism** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - | - | ✓ རྟག་པར་ལྟ་བ |
| 2551 | **nihilism** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - | - | ✓ ཆད་པར་ལྟ་བ |
| 2552 | **peacock** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - | peacock, peacocks | — |
| 2553 | **multicoloured** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - | - | — |
| 2554 | **stole** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - | - | — |
| 2555 | **lied** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - | - | — |
| 2556 | **sin** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - | sin, sins | — |
| 2557 | **futile** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - | - | — |
| 2558 | **virudhaka** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | 0.188692 | - | — |
| 2559 | **fishermen** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - | - | — |
| 2560 | **troop** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - | - | — |
| 2561 | **strayed** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - | - | — |
| 2562 | **elapatra** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | 0.257398 | - | — |
| 2563 | **miserly** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - | - | — |
| 2564 | **wholesome** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - | - | — |
| 2565 | **incarnation** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - | incarnation, incarnations | — |
| 2566 | **unconscious** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - | - | — |
| 2567 | **ness** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - | - | — |
| 2568 | **cling** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | 0.127586 | cling, clings | — |
| 2569 | **pathway** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - | pathway, pathways | — |
| 2570 | **navigator** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - | - | — |
| 2571 | **pratimok** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | 0.219803 | - | — |
| 2572 | **brilliant** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - | - | — |
| 2573 | **bathe** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | 0.260790 | - | — |
| 2574 | **unfold** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - | unfold, unfolds | — |
| 2575 | **dispelling** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - | - | — |
| 2576 | **tainted** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - | - | ~ |
| 2577 | **arrogance** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - | - | — |
| 2578 | **verbally** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - | - | — |
| 2579 | **slam** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - | slam, slams | — |
| 2580 | **accomplishing** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - | - | — |
| 2581 | **impurity** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - | impurities, impurity | — |
| 2582 | **imitate** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - | imitate, imitates | — |
| 2583 | **prajflaparamita** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | 0.190023 | - | — |
| 2584 | **fatigue** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - | - | — |
| 2585 | **fragrant** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | 0.219006 | - | — |
| 2586 | **ods** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - | - | — |
| 2587 | **bestow** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | 0.260416 | - | — |
| 2588 | **retinue** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - | - | — |
| 2589 | **carriage** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - | carriage, carriages | — |
| 2590 | **conquest** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - | - | — |
| 2591 | **sinner** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - | sinner, sinners | — |
| 2592 | **inexpressible** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - | - | — |
| 2593 | **erment** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - | - | — |
| 2594 | **vers** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - | - | — |
| 2595 | **deceit** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - | - | — |
| 2596 | **kusali** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - | - | — |
| 2597 | **stroke** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | 0.259656 | - | — |
| 2598 | **devadatta** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | 0.191069 | - | ✓ ལྷས་བྱིན |
| 2599 | **imbued** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - | - | — |
| 2600 | **mafijusrimitra** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | 0.222327 | - | — |
| 2601 | **simha** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | 0.193739 | - | — |
| 2602 | **longchen** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | 0.221083 | - | — |
| 2603 | **lattice** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - | - | — |
| 2604 | **cruel** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - | - | — |
| 2605 | **unceasingly** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - | - | — |
| 2606 | **saucer** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - | - | — |
| 2607 | **transgress** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - | - | — |
| 2608 | **afar** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | 0.260609 | - | ~ |
| 2609 | **drip** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - | drip, drips | — |
| 2610 | **malignant** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - | - | — |
| 2611 | **freshly** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - | - | — |
| 2612 | **hind** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - | - | — |
| 2613 | **faintest** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - | - | — |
| 2614 | **camel** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - | camel, camels | — |
| 2615 | **verse** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | 0.205302 | - | — |
| 2616 | **quintessence** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - | - | — |
| 2617 | **panacea** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - | - | — |
| 2618 | **defilement** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - | - | — |
| 2619 | **louse** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - | - | — |
| 2620 | **vallabha** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | 0.220704 | - | — |
| 2621 | **leper** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - | - | — |
| 2622 | **dodepa** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | 0.192073 | - | — |
| 2623 | **cured** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - | - | — |
| 2624 | **risi** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - | - | — |
| 2625 | **omen** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - | - | — |
| 2626 | **transmitting** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - | - | — |
| 2627 | **warmth** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - | - | ~ |
| 2628 | **tame** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - | - | — |
| 2629 | **indivisible** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - | - | — |
| 2630 | **imprint** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - | imprint, imprints | — |
| 2631 | **angulimala** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | 0.221468 | - | ✓ སོར་མོ་ཕྲེང་བ |
| 2632 | **prostrating** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - | - | — |
| 2633 | **adorned** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - | - | — |
| 2634 | **tva** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - | - | — |
| 2635 | **sattva** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - | sattva, sattvas | — |
| 2636 | **tsari** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | 0.193859 | - | — |
| 2637 | **perfumed** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - | - | — |
| 2638 | **explanatory** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - | - | — |
| 2639 | **mahakasyapa** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | 0.221794 | - | — |
| 2640 | **prasenajit** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | 0.193542 | - | — |
| 2641 | **aperture** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - | - | ~ |
| 2642 | **demoness** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - | - | — |
| 2643 | **duality** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - | - | — |
| 2644 | **mipham** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | 0.222027 | - | — |
| 2645 | **dissolved** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - | - | — |
| 2646 | **lotus-bud** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - | - | — |
| 2647 | **khatvanga** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - | - | ✓ |
| 2648 | **rejoiced** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - | - | — |
| 2649 | **vaisali** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | 0.193584 | - | — |
| 2650 | **cubit** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - | - | — |
| 2651 | **kutra** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | 0.193708 | - | — |
| 2652 | **tingdzin** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | 0.193795 | - | ~ |
| 2653 | **santarak** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | 0.193796 | - | — |
| 2654 | **chopel** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | 0.222436 | - | — |
| 2655 | **hik** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | 0.193939 | - | — |
| 2656 | **ejection** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | - | - | — |
| 2657 | **orgyen** | 3 | 498.58 | 9.59 | 🔵 low — common in general English | 0.194107 | - | — |
| 2658 | **rising** | 6 | 498.39 | 4.793221 | 🔵 low — common in general English | - | - | — |
| 2659 | **royalty** | 4 | 495.69 | 7.150788 | 🔵 low — common in general English | 0.196475 | - | ~ |
| 2660 | **comparison** | 4 | 492.74 | 7.108229 | 🔵 low — common in general English | - | comparison, comparisons | — |
| 2661 | **border** | 4 | 492.74 | 7.108229 | 🔵 low — common in general English | 0.228120 | - | ~ |
| 2662 | **absence** | 4 | 492.74 | 7.108229 | 🔵 low — common in general English | 0.232022 | - | — |
| 2663 | **slowly** | 4 | 492.74 | 7.108229 | 🔵 low — common in general English | 0.231058 | - | — |
| 2664 | **sri** | 4 | 492.74 | 7.108229 | 🔵 low — common in general English | 0.134858 | - | — |
| 2665 | **share** | 10 | 491.11 | 2.83388 | 🔵 low — common in general English | 0.083269 | - | — |
| 2666 | **minister** | 7 | 491.05 | 4.047958 | 🔵 low — common in general English | 0.223920 | minister, ministers | — |
| 2667 | **developing** | 5 | 490.55 | 5.66131 | 🔵 low — common in general English | - | - | — |
| 2668 | **intelligence** | 4 | 489.91 | 7.067407 | 🔵 low — common in general English | 0.232004 | - | — |
| 2669 | **choice** | 4 | 487.19 | 7.028186 | 🔵 low — common in general English | 0.229797 | - | — |
| 2670 | **hour** | 4 | 487.19 | 7.028186 | 🔵 low — common in general English | - | hour, hours | — |
| 2671 | **representative** | 5 | 486.40 | 5.613454 | 🔵 low — common in general English | 0.228290 | representative, representatives | — |
| 2672 | **ultimately** | 4 | 484.57 | 6.990446 | 🔵 low — common in general English | 0.231971 | - | — |
| 2673 | **sustained** | 4 | 484.57 | 6.990446 | 🔵 low — common in general English | - | - | ~ |
| 2674 | **temporarily** | 4 | 482.05 | 6.954078 | 🔵 low — common in general English | 0.231384 | - | — |
| 2675 | **fine** | 4 | 479.62 | 6.918987 | 🔵 low — common in general English | 0.231988 | - | — |
| 2676 | **shooting** | 3 | 477.66 | 9.18767 | 🔵 low — common in general English | - | - | — |
| 2677 | **visual** | 3 | 477.66 | 9.18767 | 🔵 low — common in general English | - | - | — |
| 2678 | **mud** | 3 | 477.66 | 9.18767 | 🔵 low — common in general English | - | - | — |
| 2679 | **attach** | 3 | 477.66 | 9.18767 | 🔵 low — common in general English | 0.125608 | - | — |
| 2680 | **roof** | 3 | 477.66 | 9.18767 | 🔵 low — common in general English | - | - | — |
| 2681 | **plough** | 3 | 477.66 | 9.18767 | 🔵 low — common in general English | 0.255069 | - | — |
| 2682 | **worthy** | 3 | 477.66 | 9.18767 | 🔵 low — common in general English | - | - | — |
| 2683 | **disciplined** | 3 | 477.66 | 9.18767 | 🔵 low — common in general English | - | - | — |
| 2684 | **stretched** | 3 | 477.66 | 9.18767 | 🔵 low — common in general English | - | - | — |
| 2685 | **magic** | 3 | 477.66 | 9.18767 | 🔵 low — common in general English | 0.259973 | - | ~ |
| 2686 | **cardinal** | 3 | 477.66 | 9.18767 | 🔵 low — common in general English | - | - | — |
| 2687 | **sesame** | 3 | 477.66 | 9.18767 | 🔵 low — common in general English | - | - | — |
| 2688 | **belly** | 3 | 477.66 | 9.18767 | 🔵 low — common in general English | - | bellies, belly | — |
| 2689 | **isn** | 3 | 477.66 | 9.18767 | 🔵 low — common in general English | - | - | — |
| 2690 | **cheese** | 3 | 477.66 | 9.18767 | 🔵 low — common in general English | - | - | — |
| 2691 | **ragged** | 3 | 477.66 | 9.18767 | 🔵 low — common in general English | - | - | — |
| 2692 | **overcoming** | 3 | 477.66 | 9.18767 | 🔵 low — common in general English | - | - | — |
| 2693 | **theft** | 3 | 477.66 | 9.18767 | 🔵 low — common in general English | - | - | — |
| 2694 | **miracle** | 3 | 477.66 | 9.18767 | 🔵 low — common in general English | - | - | — |
| 2695 | **renouncing** | 3 | 477.66 | 9.18767 | 🔵 low — common in general English | - | - | — |
| 2696 | **severed** | 3 | 477.66 | 9.18767 | 🔵 low — common in general English | - | - | — |
| 2697 | **utmost** | 3 | 477.66 | 9.18767 | 🔵 low — common in general English | - | - | — |
| 2698 | **workable** | 3 | 477.66 | 9.18767 | 🔵 low — common in general English | - | - | — |
| 2699 | **resolute** | 3 | 477.66 | 9.18767 | 🔵 low — common in general English | - | - | — |
| 2700 | **wished** | 3 | 477.66 | 9.18767 | 🔵 low — common in general English | - | - | — |
| 2701 | **willingly** | 3 | 477.66 | 9.18767 | 🔵 low — common in general English | - | - | — |
| 2702 | **lunar** | 3 | 477.66 | 9.18767 | 🔵 low — common in general English | - | - | — |
| 2703 | **repetition** | 3 | 477.66 | 9.18767 | 🔵 low — common in general English | - | repetition, repetitions | — |
| 2704 | **shorten** | 3 | 477.66 | 9.18767 | 🔵 low — common in general English | - | - | — |
| 2705 | **repeating** | 3 | 477.66 | 9.18767 | 🔵 low — common in general English | - | - | — |
| 2706 | **event** | 4 | 477.27 | 6.885085 | 🔵 low — common in general English | - | event, events | — |
| 2707 | **losing** | 4 | 477.27 | 6.885085 | 🔵 low — common in general English | - | - | — |
| 2708 | **northern** | 5 | 475.03 | 5.482261 | 🔵 low — common in general English | 0.182444 | - | — |
| 2709 | **bottom** | 4 | 472.80 | 6.820546 | 🔵 low — common in general English | - | - | — |
| 2710 | **elsewhere** | 4 | 472.80 | 6.820546 | 🔵 low — common in general English | - | - | — |
| 2711 | **criticism** | 4 | 472.80 | 6.820546 | 🔵 low — common in general English | 0.231870 | - | — |
| 2712 | **law** | 5 | 471.55 | 5.442095 | 🔵 low — common in general English | - | law, laws | — |
| 2713 | **cover** | 5 | 470.87 | 5.434252 | 🔵 low — common in general English | 0.074620 | cover, covers | — |
| 2714 | **chain** | 4 | 470.66 | 6.789775 | 🔵 low — common in general English | - | chain, chains | — |
| 2715 | **remained** | 5 | 469.53 | 5.418748 | 🔵 low — common in general English | - | - | — |
| 2716 | **jumped** | 4 | 468.59 | 6.759922 | 🔵 low — common in general English | - | - | — |
| 2717 | **ended** | 7 | 465.13 | 3.834233 | 🔵 low — common in general English | - | - | — |
| 2718 | **liquid** | 4 | 464.63 | 6.702763 | 🔵 low — common in general English | 0.230940 | - | — |
| 2719 | **draw** | 4 | 464.63 | 6.702763 | 🔵 low — common in general English | 0.181389 | draw, draws | — |
| 2720 | **discomfort** | 3 | 462.71 | 8.899988 | 🔵 low — common in general English | - | discomfort, discomforts | — |
| 2721 | **uphold** | 3 | 462.71 | 8.899988 | 🔵 low — common in general English | - | - | — |
| 2722 | **checking** | 3 | 462.71 | 8.899988 | 🔵 low — common in general English | - | - | — |
| 2723 | **descent** | 3 | 462.71 | 8.899988 | 🔵 low — common in general English | - | descent, descents | — |
| 2724 | **compounded** | 3 | 462.71 | 8.899988 | 🔵 low — common in general English | - | - | — |
| 2725 | **height** | 3 | 462.71 | 8.899988 | 🔵 low — common in general English | - | height, heights | — |
| 2726 | **thirty** | 3 | 462.71 | 8.899988 | 🔵 low — common in general English | 0.024295 | - | ~ |
| 2727 | **mansion** | 3 | 462.71 | 8.899988 | 🔵 low — common in general English | - | mansion, mansions | — |
| 2728 | **amongst** | 3 | 462.71 | 8.899988 | 🔵 low — common in general English | - | - | — |
| 2729 | **powdered** | 3 | 462.71 | 8.899988 | 🔵 low — common in general English | - | - | — |
| 2730 | **bind** | 3 | 462.71 | 8.899988 | 🔵 low — common in general English | 0.044213 | bind, binds | — |
| 2731 | **harmed** | 3 | 462.71 | 8.899988 | 🔵 low — common in general English | - | - | — |
| 2732 | **namely** | 3 | 462.71 | 8.899988 | 🔵 low — common in general English | - | - | — |
| 2733 | **drinking** | 3 | 462.71 | 8.899988 | 🔵 low — common in general English | - | - | — |
| 2734 | **shaken** | 3 | 462.71 | 8.899988 | 🔵 low — common in general English | - | - | — |
| 2735 | **pour** | 3 | 462.71 | 8.899988 | 🔵 low — common in general English | 0.083975 | pour, pours | — |
| 2736 | **inspired** | 3 | 462.71 | 8.899988 | 🔵 low — common in general English | - | - | — |
| 2737 | **invoked** | 3 | 462.71 | 8.899988 | 🔵 low — common in general English | - | - | — |
| 2738 | **recognizing** | 3 | 462.71 | 8.899988 | 🔵 low — common in general English | - | - | — |
| 2739 | **pity** | 3 | 462.71 | 8.899988 | 🔵 low — common in general English | - | - | — |
| 2740 | **ring** | 3 | 462.71 | 8.899988 | 🔵 low — common in general English | - | ring, rings | — |
| 2741 | **assembled** | 3 | 462.71 | 8.899988 | 🔵 low — common in general English | - | - | — |
| 2742 | **origin** | 4 | 460.88 | 6.648696 | 🔵 low — common in general English | - | origin, origins | — |
| 2743 | **produce** | 5 | 459.47 | 5.302676 | 🔵 low — common in general English | 0.148306 | produce, produces | — |
| 2744 | **maturity** | 4 | 459.08 | 6.622721 | 🔵 low — common in general English | 0.231784 | - | — |
| 2745 | **wide** | 4 | 457.33 | 6.597403 | 🔵 low — common in general English | 0.231448 | - | — |
| 2746 | **grown** | 4 | 457.33 | 6.597403 | 🔵 low — common in general English | - | - | — |
| 2747 | **provided** | 5 | 456.55 | 5.269003 | 🔵 low — common in general English | - | - | — |
| 2748 | **trade** | 8 | 455.18 | 3.283217 | 🔵 low — common in general English | 0.108214 | - | — |
| 2749 | **gained** | 4 | 453.95 | 6.548613 | 🔵 low — common in general English | - | - | — |
| 2750 | **los** | 4 | 453.95 | 6.548613 | 🔵 low — common in general English | - | - | — |
| 2751 | **falling** | 5 | 453.18 | 5.230037 | 🔵 low — common in general English | - | - | — |
| 2752 | **fundamental** | 4 | 452.31 | 6.525082 | 🔵 low — common in general English | 0.231986 | - | — |
| 2753 | **meeting** | 7 | 451.56 | 3.722427 | 🔵 low — common in general English | 0.125390 | - | — |
| 2754 | **contemplate** | 3 | 451.10 | 8.676844 | 🔵 low — common in general English | 0.215583 | - | — |
| 2755 | **imperative** | 3 | 451.10 | 8.676844 | 🔵 low — common in general English | - | - | — |
| 2756 | **chasing** | 3 | 451.10 | 8.676844 | 🔵 low — common in general English | - | - | — |
| 2757 | **intact** | 3 | 451.10 | 8.676844 | 🔵 low — common in general English | - | - | — |
| 2758 | **sink** | 3 | 451.10 | 8.676844 | 🔵 low — common in general English | 0.254061 | - | — |
| 2759 | **progressively** | 3 | 451.10 | 8.676844 | 🔵 low — common in general English | - | - | — |
| 2760 | **guarded** | 3 | 451.10 | 8.676844 | 🔵 low — common in general English | - | - | — |
| 2761 | **compiled** | 3 | 451.10 | 8.676844 | 🔵 low — common in general English | - | - | — |
| 2762 | **welfare** | 3 | 451.10 | 8.676844 | 🔵 low — common in general English | - | - | — |
| 2763 | **profoundly** | 3 | 451.10 | 8.676844 | 🔵 low — common in general English | - | - | — |
| 2764 | **deeper** | 3 | 451.10 | 8.676844 | 🔵 low — common in general English | - | - | — |
| 2765 | **roasted** | 3 | 451.10 | 8.676844 | 🔵 low — common in general English | - | - | — |
| 2766 | **crack** | 3 | 451.10 | 8.676844 | 🔵 low — common in general English | - | - | — |
| 2767 | **thick** | 3 | 451.10 | 8.676844 | 🔵 low — common in general English | - | - | — |
| 2768 | **offensive** | 3 | 451.10 | 8.676844 | 🔵 low — common in general English | - | - | — |
| 2769 | **conditioning** | 3 | 451.10 | 8.676844 | 🔵 low — common in general English | - | - | ~ |
| 2770 | **splinter** | 3 | 451.10 | 8.676844 | 🔵 low — common in general English | - | - | — |
| 2771 | **weighed** | 3 | 451.10 | 8.676844 | 🔵 low — common in general English | - | - | — |
| 2772 | **heap** | 3 | 451.10 | 8.676844 | 🔵 low — common in general English | - | heap, heaps | — |
| 2773 | **capture** | 3 | 451.10 | 8.676844 | 🔵 low — common in general English | - | - | — |
| 2774 | **peak** | 4 | 449.16 | 6.47962 | 🔵 low — common in general English | 0.232291 | - | — |
| 2775 | **pursue** | 4 | 447.64 | 6.457641 | 🔵 low — common in general English | 0.231065 | - | — |
| 2776 | **store** | 4 | 446.15 | 6.436135 | 🔵 low — common in general English | 0.232101 | - | — |
| 2777 | **defend** | 4 | 446.15 | 6.436135 | 🔵 low — common in general English | 0.231668 | - | — |
| 2778 | **drive** | 4 | 446.15 | 6.436135 | 🔵 low — common in general English | 0.083444 | drive, drives | — |
| 2779 | **billion** | 9 | 445.19 | 2.85439 | 🔵 low — common in general English | 0.094762 | - | ~ |
| 2780 | **opinion** | 4 | 443.26 | 6.394462 | 🔵 low — common in general English | - | opinion, opinions | — |
| 2781 | **collapse** | 4 | 441.86 | 6.374259 | 🔵 low — common in general English | 0.222362 | - | — |
| 2782 | **music** | 3 | 441.63 | 8.494523 | 🔵 low — common in general English | - | - | — |
| 2783 | **endeavour** | 3 | 441.63 | 8.494523 | 🔵 low — common in general English | - | - | — |
| 2784 | **wealthy** | 3 | 441.63 | 8.494523 | 🔵 low — common in general English | - | - | — |
| 2785 | **fur** | 3 | 441.63 | 8.494523 | 🔵 low — common in general English | - | fur, furs | — |
| 2786 | **nice** | 3 | 441.63 | 8.494523 | 🔵 low — common in general English | - | - | — |
| 2787 | **grove** | 3 | 441.63 | 8.494523 | 🔵 low — common in general English | - | grove, groves | — |
| 2788 | **introducing** | 3 | 441.63 | 8.494523 | 🔵 low — common in general English | - | - | — |
| 2789 | **sympathetic** | 3 | 441.63 | 8.494523 | 🔵 low — common in general English | - | - | — |
| 2790 | **unfortunate** | 3 | 441.63 | 8.494523 | 🔵 low — common in general English | - | - | — |
| 2791 | **closed** | 5 | 440.85 | 5.087785 | 🔵 low — common in general English | - | - | — |
| 2792 | **nearby** | 4 | 440.49 | 6.354457 | 🔵 low — common in general English | 0.231739 | - | — |
| 2793 | **attention** | 4 | 440.49 | 6.354457 | 🔵 low — common in general English | 0.231950 | - | — |
| 2794 | **growing** | 5 | 439.43 | 5.071347 | 🔵 low — common in general English | - | - | — |
| 2795 | **needed** | 5 | 436.65 | 5.039258 | 🔵 low — common in general English | - | - | — |
| 2796 | **covering** | 4 | 436.52 | 6.297298 | 🔵 low — common in general English | - | - | — |
| 2797 | **allow** | 5 | 433.95 | 5.008168 | 🔵 low — common in general English | - | allow, allows | — |
| 2798 | **drove** | 3 | 433.61 | 8.340372 | 🔵 low — common in general English | - | - | — |
| 2799 | **relaxed** | 3 | 433.61 | 8.340372 | 🔵 low — common in general English | - | - | — |
| 2800 | **frontier** | 3 | 433.61 | 8.340372 | 🔵 low — common in general English | - | frontier, frontiers | — |
| 2801 | **dig** | 3 | 433.61 | 8.340372 | 🔵 low — common in general English | - | dig, digs | — |
| 2802 | **disagreement** | 3 | 433.61 | 8.340372 | 🔵 low — common in general English | - | disagreement, disagreements | — |
| 2803 | **pig** | 3 | 433.61 | 8.340372 | 🔵 low — common in general English | - | - | — |
| 2804 | **declared** | 5 | 432.20 | 4.987965 | 🔵 low — common in general English | - | - | — |
| 2805 | **extent** | 4 | 431.57 | 6.225839 | 🔵 low — common in general English | 0.231142 | - | — |
| 2806 | **providing** | 4 | 431.57 | 6.225839 | 🔵 low — common in general English | - | - | — |
| 2807 | **began** | 5 | 431.34 | 4.978015 | 🔵 low — common in general English | - | - | — |
| 2808 | **seeking** | 5 | 430.49 | 4.968162 | 🔵 low — common in general English | - | - | — |
| 2809 | **western** | 5 | 429.64 | 4.958406 | 🔵 low — common in general English | 0.137829 | - | — |
| 2810 | **week** | 7 | 429.42 | 3.53987 | 🔵 low — common in general English | 0.175504 | week, weeks | — |
| 2811 | **bank** | 8 | 428.96 | 3.0941 | 🔵 low — common in general English | 0.216397 | bank, banks | — |
| 2812 | **near** | 5 | 428.80 | 4.948744 | 🔵 low — common in general English | - | - | — |
| 2813 | **moved** | 4 | 428.07 | 6.175409 | 🔵 low — common in general English | - | - | — |
| 2814 | **showed** | 5 | 426.75 | 4.92499 | 🔵 low — common in general English | - | - | — |
| 2815 | **function** | 3 | 426.67 | 8.206841 | 🔵 low — common in general English | - | function, functions | — |
| 2816 | **peripheral** | 3 | 426.67 | 8.206841 | 🔵 low — common in general English | - | - | — |
| 2817 | **affair** | 3 | 426.67 | 8.206841 | 🔵 low — common in general English | - | - | — |
| 2818 | **hawk** | 3 | 426.67 | 8.206841 | 🔵 low — common in general English | - | hawk, hawks | — |
| 2819 | **stepping** | 3 | 426.67 | 8.206841 | 🔵 low — common in general English | - | - | — |
| 2820 | **slope** | 3 | 426.67 | 8.206841 | 🔵 low — common in general English | - | slope, slopes | — |
| 2821 | **defeated** | 3 | 426.67 | 8.206841 | 🔵 low — common in general English | - | - | — |
| 2822 | **extend** | 4 | 425.84 | 6.143148 | 🔵 low — common in general English | 0.232029 | - | — |
| 2823 | **talk** | 4 | 424.75 | 6.127399 | 🔵 low — common in general English | 0.083287 | - | — |
| 2824 | **north** | 5 | 423.94 | 4.892655 | 🔵 low — common in general English | 0.182510 | - | — |
| 2825 | **determine** | 4 | 423.67 | 6.111895 | 🔵 low — common in general English | 0.129065 | determine, determines | — |
| 2826 | **enable** | 4 | 423.67 | 6.111895 | 🔵 low — common in general English | - | enable, enables | — |
| 2827 | **ending** | 5 | 423.55 | 4.88812 | 🔵 low — common in general English | - | - | — |
| 2828 | **rein** | 3 | 420.55 | 8.089058 | 🔵 low — common in general English | - | rein, reins | — |
| 2829 | **remote** | 3 | 420.55 | 8.089058 | 🔵 low — common in general English | - | - | — |
| 2830 | **earliest** | 3 | 420.55 | 8.089058 | 🔵 low — common in general English | - | - | — |
| 2831 | **smooth** | 3 | 420.55 | 8.089058 | 🔵 low — common in general English | - | - | — |
| 2832 | **distorted** | 3 | 420.55 | 8.089058 | 🔵 low — common in general English | - | - | — |
| 2833 | **vary** | 3 | 420.55 | 8.089058 | 🔵 low — common in general English | - | - | — |
| 2834 | **feeding** | 3 | 420.55 | 8.089058 | 🔵 low — common in general English | - | - | — |
| 2835 | **ceased** | 3 | 420.55 | 8.089058 | 🔵 low — common in general English | - | - | — |
| 2836 | **growth** | 6 | 418.10 | 4.020981 | 🔵 low — common in general English | 0.148398 | - | — |
| 2837 | **sell** | 6 | 417.90 | 4.019082 | 🔵 low — common in general English | 0.148906 | - | — |
| 2838 | **paying** | 4 | 417.55 | 6.023602 | 🔵 low — common in general English | - | - | — |
| 2839 | **harvest** | 4 | 416.58 | 6.009616 | 🔵 low — common in general English | 0.260769 | harvest, harvests | — |
| 2840 | **successor** | 3 | 415.07 | 7.983697 | 🔵 low — common in general English | - | successor, successors | — |
| 2841 | **loaded** | 3 | 415.07 | 7.983697 | 🔵 low — common in general English | - | - | — |
| 2842 | **inherent** | 3 | 415.07 | 7.983697 | 🔵 low — common in general English | - | - | — |
| 2843 | **banner** | 3 | 415.07 | 7.983697 | 🔵 low — common in general English | - | banner, banners | ~ |
| 2844 | **inevitably** | 3 | 415.07 | 7.983697 | 🔵 low — common in general English | - | - | — |
| 2845 | **access** | 4 | 410.15 | 5.916835 | 🔵 low — common in general English | 0.232275 | - | — |
| 2846 | **fulfil** | 3 | 410.11 | 7.888387 | 🔵 low — common in general English | - | - | — |
| 2847 | **upside** | 3 | 410.11 | 7.888387 | 🔵 low — common in general English | - | - | — |
| 2848 | **custom** | 3 | 410.11 | 7.888387 | 🔵 low — common in general English | - | - | — |
| 2849 | **translated** | 3 | 410.11 | 7.888387 | 🔵 low — common in general English | - | - | — |
| 2850 | **practical** | 3 | 410.11 | 7.888387 | 🔵 low — common in general English | - | - | — |
| 2851 | **scattered** | 3 | 410.11 | 7.888387 | 🔵 low — common in general English | - | - | — |
| 2852 | **unlimited** | 3 | 410.11 | 7.888387 | 🔵 low — common in general English | - | - | — |
| 2853 | **roll** | 3 | 410.11 | 7.888387 | 🔵 low — common in general English | - | roll, rolls | — |
| 2854 | **minute** | 3 | 410.11 | 7.888387 | 🔵 low — common in general English | - | - | — |
| 2855 | **ease** | 4 | 407.57 | 5.879563 | 🔵 low — common in general English | 0.231697 | - | — |
| 2856 | **raise** | 5 | 407.17 | 4.699034 | 🔵 low — common in general English | 0.182083 | - | — |
| 2857 | **count** | 3 | 405.59 | 7.801376 | 🔵 low — common in general English | 0.231779 | - | — |
| 2858 | **bag** | 3 | 405.59 | 7.801376 | 🔵 low — common in general English | - | - | — |
| 2859 | **automatically** | 3 | 405.59 | 7.801376 | 🔵 low — common in general English | - | - | — |
| 2860 | **visited** | 3 | 405.59 | 7.801376 | 🔵 low — common in general English | - | - | — |
| 2861 | **fellow** | 3 | 405.59 | 7.801376 | 🔵 low — common in general English | - | - | — |
| 2862 | **moving** | 4 | 405.08 | 5.843631 | 🔵 low — common in general English | - | - | — |
| 2863 | **warned** | 4 | 405.08 | 5.843631 | 🔵 low — common in general English | - | - | — |
| 2864 | **deal** | 5 | 404.61 | 4.669511 | 🔵 low — common in general English | - | deal, deals | — |
| 2865 | **quickly** | 4 | 403.46 | 5.820374 | 🔵 low — common in general English | 0.231105 | - | — |
| 2866 | **feed** | 4 | 402.67 | 5.808946 | 🔵 low — common in general English | 0.231291 | - | — |
| 2867 | **resulting** | 4 | 401.89 | 5.797646 | 🔵 low — common in general English | - | - | — |
| 2868 | **merge** | 4 | 401.89 | 5.797646 | 🔵 low — common in general English | 0.232289 | - | — |
| 2869 | **worker** | 3 | 401.43 | 7.721333 | 🔵 low — common in general English | - | - | — |
| 2870 | **farmer** | 3 | 401.43 | 7.721333 | 🔵 low — common in general English | - | - | — |
| 2871 | **cool** | 3 | 401.43 | 7.721333 | 🔵 low — common in general English | - | - | — |
| 2872 | **authority** | 4 | 399.59 | 5.764494 | 🔵 low — common in general English | 0.230720 | - | — |
| 2873 | **possibility** | 4 | 398.84 | 5.753683 | 🔵 low — common in general English | - | possibilities, possibility | — |
| 2874 | **furthermore** | 3 | 397.58 | 7.647225 | 🔵 low — common in general English | - | - | — |
| 2875 | **memory** | 3 | 397.58 | 7.647225 | 🔵 low — common in general English | - | - | — |
| 2876 | **stayed** | 3 | 397.58 | 7.647225 | 🔵 low — common in general English | - | - | — |
| 2877 | **party** | 4 | 397.37 | 5.732405 | 🔵 low — common in general English | - | parties, party | — |
| 2878 | **mass** | 3 | 393.99 | 7.578232 | 🔵 low — common in general English | - | - | — |
| 2879 | **generating** | 3 | 393.99 | 7.578232 | 🔵 low — common in general English | - | - | — |
| 2880 | **armed** | 3 | 393.99 | 7.578232 | 🔵 low — common in general English | - | - | — |
| 2881 | **responsibility** | 3 | 393.99 | 7.578232 | 🔵 low — common in general English | - | responsibilities, responsibility | — |
| 2882 | **stood** | 4 | 393.81 | 5.681112 | 🔵 low — common in general English | - | - | — |
| 2883 | **wanted** | 4 | 393.12 | 5.671162 | 🔵 low — common in general English | - | - | — |
| 2884 | **class** | 4 | 392.44 | 5.66131 | 🔵 low — common in general English | - | - | — |
| 2885 | **firmly** | 3 | 390.63 | 7.513694 | 🔵 low — common in general English | - | - | — |
| 2886 | **conjunction** | 3 | 390.63 | 7.513694 | 🔵 low — common in general English | - | - | — |
| 2887 | **mention** | 3 | 390.63 | 7.513694 | 🔵 low — common in general English | 0.125851 | - | — |
| 2888 | **flood** | 3 | 390.63 | 7.513694 | 🔵 low — common in general English | - | - | — |
| 2889 | **executed** | 3 | 390.63 | 7.513694 | 🔵 low — common in general English | - | - | — |
| 2890 | **affect** | 4 | 390.43 | 5.632322 | 🔵 low — common in general English | - | affect, affects | — |
| 2891 | **formed** | 4 | 387.84 | 5.594934 | 🔵 low — common in general English | - | - | — |
| 2892 | **absorb** | 3 | 387.48 | 7.453069 | 🔵 low — common in general English | - | absorb, absorbs | — |
| 2893 | **frost** | 3 | 387.48 | 7.453069 | 🔵 low — common in general English | - | frost, frosts | — |
| 2894 | **pledge** | 3 | 387.48 | 7.453069 | 🔵 low — common in general English | - | - | — |
| 2895 | **manage** | 3 | 387.48 | 7.453069 | 🔵 low — common in general English | - | - | — |
| 2896 | **specific** | 4 | 386.58 | 5.576752 | 🔵 low — common in general English | 0.231774 | - | — |
| 2897 | **route** | 3 | 384.51 | 7.395911 | 🔵 low — common in general English | - | route, routes | — |
| 2898 | **surrounding** | 3 | 384.51 | 7.395911 | 🔵 low — common in general English | - | - | — |
| 2899 | **panic** | 3 | 384.51 | 7.395911 | 🔵 low — common in general English | - | - | — |
| 2900 | **ball** | 3 | 384.51 | 7.395911 | 🔵 low — common in general English | - | ball, balls | — |
| 2901 | **topped** | 3 | 384.51 | 7.395911 | 🔵 low — common in general English | - | - | — |
| 2902 | **our** | 5 | 383.71 | 4.428349 | 🔵 low — common in general English | - | - | — |
| 2903 | **predicted** | 4 | 382.34 | 5.515598 | 🔵 low — common in general English | - | - | — |
| 2904 | **placing** | 3 | 381.70 | 7.341843 | 🔵 low — common in general English | - | - | — |
| 2905 | **removed** | 3 | 381.70 | 7.341843 | 🔵 low — common in general English | - | - | — |
| 2906 | **successive** | 3 | 381.70 | 7.341843 | 🔵 low — common in general English | - | - | — |
| 2907 | **crushing** | 3 | 381.70 | 7.341843 | 🔵 low — common in general English | - | - | — |
| 2908 | **argument** | 3 | 381.70 | 7.341843 | 🔵 low — common in general English | - | argument, arguments | — |
| 2909 | **progressive** | 3 | 381.70 | 7.341843 | 🔵 low — common in general English | - | - | — |
| 2910 | **violated** | 3 | 381.70 | 7.341843 | 🔵 low — common in general English | - | - | — |
| 2911 | **temporary** | 4 | 381.17 | 5.498791 | 🔵 low — common in general English | 0.232158 | - | — |
| 2912 | **counter** | 3 | 379.03 | 7.29055 | 🔵 low — common in general English | - | - | — |
| 2913 | **specifically** | 3 | 379.03 | 7.29055 | 🔵 low — common in general English | - | - | — |
| 2914 | **quantity** | 3 | 379.03 | 7.29055 | 🔵 low — common in general English | - | quantities, quantity | — |
| 2915 | **eliminated** | 3 | 379.03 | 7.29055 | 🔵 low — common in general English | - | - | — |
| 2916 | **preventing** | 3 | 376.50 | 7.24176 | 🔵 low — common in general English | - | - | — |
| 2917 | **write** | 3 | 376.50 | 7.24176 | 🔵 low — common in general English | 0.096051 | - | — |
| 2918 | **season** | 4 | 376.16 | 5.42647 | 🔵 low — common in general English | - | season, seasons | — |
| 2919 | **half** | 5 | 374.11 | 4.317575 | 🔵 low — common in general English | 0.181396 | - | — |
| 2920 | **category** | 3 | 374.08 | 7.19524 | 🔵 low — common in general English | - | categories, category | — |
| 2921 | **limit** | 4 | 373.52 | 5.388443 | 🔵 low — common in general English | - | limit, limits | — |
| 2922 | **entry** | 3 | 371.77 | 7.150788 | 🔵 low — common in general English | - | - | — |
| 2923 | **picture** | 3 | 371.77 | 7.150788 | 🔵 low — common in general English | - | picture, pictures | — |
| 2924 | **associate** | 3 | 371.77 | 7.150788 | 🔵 low — common in general English | - | associate, associates | — |
| 2925 | **introduce** | 3 | 371.77 | 7.150788 | 🔵 low — common in general English | - | - | — |
| 2926 | **argue** | 3 | 369.55 | 7.108229 | 🔵 low — common in general English | - | - | — |
| 2927 | **earned** | 4 | 368.53 | 5.316469 | 🔵 low — common in general English | - | - | — |
| 2928 | **history** | 3 | 367.43 | 7.067407 | 🔵 low — common in general English | - | - | — |
| 2929 | **assume** | 3 | 365.39 | 7.028186 | 🔵 low — common in general English | - | - | — |
| 2930 | **threaten** | 3 | 365.39 | 7.028186 | 🔵 low — common in general English | 0.149107 | - | — |
| 2931 | **win** | 3 | 363.43 | 6.990446 | 🔵 low — common in general English | - | - | — |
| 2932 | **secure** | 3 | 363.43 | 6.990446 | 🔵 low — common in general English | - | secure, secures | — |
| 2933 | **china** | 4 | 362.10 | 5.223687 | 🔵 low — common in general English | 0.127503 | - | — |
| 2934 | **midday** | 3 | 361.54 | 6.954078 | 🔵 low — common in general English | - | - | — |
| 2935 | **subsequent** | 3 | 361.54 | 6.954078 | 🔵 low — common in general English | - | - | — |
| 2936 | **severely** | 3 | 361.54 | 6.954078 | 🔵 low — common in general English | - | - | — |
| 2937 | **early** | 5 | 361.36 | 4.17039 | 🔵 low — common in general English | 0.181574 | - | — |
| 2938 | **brief** | 3 | 359.71 | 6.918987 | 🔵 low — common in general English | - | - | — |
| 2939 | **ran** | 3 | 359.71 | 6.918987 | 🔵 low — common in general English | - | - | — |
| 2940 | **send** | 3 | 359.71 | 6.918987 | 🔵 low — common in general English | - | - | — |
| 2941 | **acquire** | 5 | 359.66 | 4.150717 | 🔵 low — common in general English | 0.125898 | acquire, acquires | — |
| 2942 | **local** | 4 | 358.68 | 5.174295 | 🔵 low — common in general English | 0.231682 | - | — |
| 2943 | **assuming** | 3 | 357.95 | 6.885085 | 🔵 low — common in general English | - | - | — |
| 2944 | **commerce** | 4 | 356.62 | 5.144619 | 🔵 low — common in general English | 0.231747 | - | — |
| 2945 | **prove** | 3 | 356.25 | 6.852295 | 🔵 low — common in general English | - | prove, proves | — |
| 2946 | **increasing** | 4 | 355.42 | 5.127227 | 🔵 low — common in general English | - | - | — |
| 2947 | **warning** | 3 | 354.60 | 6.820546 | 🔵 low — common in general English | - | - | — |
| 2948 | **proportion** | 3 | 354.60 | 6.820546 | 🔵 low — common in general English | - | proportion, proportions | — |
| 2949 | **press** | 4 | 353.84 | 5.104499 | 🔵 low — common in general English | 0.149501 | press, presses | — |
| 2950 | **urge** | 3 | 353.00 | 6.789775 | 🔵 low — common in general English | - | urge, urges | — |
| 2951 | **resolution** | 3 | 353.00 | 6.789775 | 🔵 low — common in general English | - | - | — |
| 2952 | **item** | 3 | 348.47 | 6.702763 | 🔵 low — common in general English | 0.253195 | - | — |
| 2953 | **floating** | 3 | 348.47 | 6.702763 | 🔵 low — common in general English | - | - | — |
| 2954 | **environment** | 3 | 348.47 | 6.702763 | 🔵 low — common in general English | - | - | — |
| 2955 | **repayment** | 3 | 348.47 | 6.702763 | 🔵 low — common in general English | - | - | — |
| 2956 | **aggressive** | 3 | 348.47 | 6.702763 | 🔵 low — common in general English | - | - | — |
| 2957 | **acting** | 3 | 348.47 | 6.702763 | 🔵 low — common in general English | - | - | — |
| 2958 | **oil** | 6 | 348.32 | 3.34994 | 🔵 low — common in general English | 0.149503 | - | — |
| 2959 | **figure** | 4 | 347.87 | 5.018424 | 🔵 low — common in general English | - | figure, figures | — |
| 2960 | **company** | 8 | 347.14 | 2.503892 | 🔵 low — common in general English | 0.107879 | - | — |
| 2961 | **resist** | 3 | 347.05 | 6.675364 | 🔵 low — common in general English | - | resist, resists | — |
| 2962 | **managed** | 3 | 345.66 | 6.648696 | 🔵 low — common in general English | - | - | — |
| 2963 | **changing** | 3 | 345.66 | 6.648696 | 🔵 low — common in general English | - | - | — |
| 2964 | **aware** | 3 | 345.66 | 6.648696 | 🔵 low — common in general English | - | - | — |
| 2965 | **gain** | 5 | 343.61 | 3.965514 | 🔵 low — common in general English | 0.182415 | - | — |
| 2966 | **arrange** | 3 | 341.71 | 6.57271 | 🔵 low — common in general English | 0.098349 | - | — |
| 2967 | **shut** | 3 | 341.71 | 6.57271 | 🔵 low — common in general English | - | shut, shuts | — |
| 2968 | **slight** | 3 | 341.71 | 6.57271 | 🔵 low — common in general English | 0.031764 | - | — |
| 2969 | **suffered** | 3 | 341.71 | 6.57271 | 🔵 low — common in general English | - | - | — |
| 2970 | **joined** | 3 | 340.46 | 6.548613 | 🔵 low — common in general English | - | - | — |
| 2971 | **joint** | 4 | 338.53 | 4.883605 | 🔵 low — common in general English | - | - | — |
| 2972 | **apparent** | 3 | 338.04 | 6.502093 | 🔵 low — common in general English | - | - | — |
| 2973 | **pointed** | 3 | 338.04 | 6.502093 | 🔵 low — common in general English | - | - | — |
| 2974 | **delivered** | 3 | 336.87 | 6.47962 | 🔵 low — common in general English | - | - | — |
| 2975 | **outcome** | 3 | 336.87 | 6.47962 | 🔵 low — common in general English | - | - | — |
| 2976 | **scale** | 3 | 335.73 | 6.457641 | 🔵 low — common in general English | - | - | — |
| 2977 | **attractive** | 3 | 335.73 | 6.457641 | 🔵 low — common in general English | - | - | — |
| 2978 | **permit** | 3 | 335.73 | 6.457641 | 🔵 low — common in general English | 0.107674 | - | — |
| 2979 | **adequate** | 3 | 334.61 | 6.436135 | 🔵 low — common in general English | - | - | — |
| 2980 | **favour** | 3 | 334.61 | 6.436135 | 🔵 low — common in general English | - | - | — |
| 2981 | **repeated** | 3 | 334.61 | 6.436135 | 🔵 low — common in general English | - | - | — |
| 2982 | **requested** | 3 | 333.52 | 6.415081 | 🔵 low — common in general English | - | - | — |
| 2983 | **citadel** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 2984 | **bounty** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 2985 | **savage** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English | - | savage, savages | — |
| 2986 | **hindrance** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English | - | hindrance, hindrances | — |
| 2987 | **totality** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 2988 | **populated** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 2989 | **striving** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 2990 | **sway** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 2991 | **motive** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 2992 | **genuinely** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 2993 | **draught** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 2994 | **encompassing** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 2995 | **depart** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English | - | depart, departs | — |
| 2996 | **pale** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 2997 | **warrior** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 2998 | **prison** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 2999 | **miserable** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 3000 | **meagre** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 3001 | **momentary** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 3002 | **unrelenting** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 3003 | **axe** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 3004 | **pretend** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 3005 | **jar** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 3006 | **storey** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English | - | storey, storeys | — |
| 3007 | **reviving** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 3008 | **screaming** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 3009 | **sealed** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 3010 | **stabbed** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 3011 | **cracked** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 3012 | **boiling** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 3013 | **weep** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English | - | weep, weeps | — |
| 3014 | **deceased** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 3015 | **rib** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 3016 | **hauled** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 3017 | **arrogant** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 3018 | **stuff** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English | - | stuff, stuffs | — |
| 3019 | **ploughed** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 3020 | **halfway** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 3021 | **jaw** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 3022 | **chew** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 3023 | **clutch** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 3024 | **burglar** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English | - | burglar, burglars | — |
| 3025 | **haven** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 3026 | **confer** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 3027 | **irresistible** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 3028 | **abyss** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 3029 | **wit** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 3030 | **dress** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 3031 | **progression** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 3032 | **feeble** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 3033 | **secretly** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 3034 | **prowess** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 3035 | **renunciation** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 3036 | **exposing** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 3037 | **observation** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 3038 | **bother** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 3039 | **creator** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English | - | creator, creators | — |
| 3040 | **abstain** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 3041 | **pleasantly** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 3042 | **respectful** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 3043 | **headache** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 3044 | **saffron** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 3045 | **dense** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 3046 | **inherit** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English | 0.232058 | - | — |
| 3047 | **maturation** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 3048 | **corrupted** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 3049 | **needing** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 3050 | **discrimination** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 3051 | **rebuke** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 3052 | **embarrassed** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 3053 | **irritated** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 3054 | **receptive** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 3055 | **externally** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 3056 | **requisite** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 3057 | **invoke** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 3058 | **underwent** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 3059 | **angrily** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 3060 | **remembered** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 3061 | **melted** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 3062 | **distinctly** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 3063 | **flash** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 3064 | **continuity** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 3065 | **self-centred** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 3066 | **indifferent** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 3067 | **perished** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 3068 | **nurtured** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 3069 | **kicked** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 3070 | **wrecked** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 3071 | **avail** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 3072 | **chariot** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 3073 | **oar** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 3074 | **twenty-three** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 3075 | **doha** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English | - | - | ✓ |
| 3076 | **engender** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 3077 | **fore** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 3078 | **dirt** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 3079 | **aggressor** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 3080 | **observing** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 3081 | **emptied** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 3082 | **beam** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 3083 | **vibrant** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 3084 | **revitalize** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 3085 | **guarantee** | 3 | 332.44 | 6.394462 | 🔵 low — common in general English | - | - | — |
| 3086 | **exhaustion** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | ~ |
| 3087 | **unerring** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3088 | **greatness** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3089 | **permeate** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | permeate, permeates | — |
| 3090 | **semblance** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3091 | **daka** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | ✓ དཔའ་བོ |
| 3092 | **blissful** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | ~ |
| 3093 | **eternity** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3094 | **concealed** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3095 | **upside-down** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3096 | **nomad** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3097 | **savouring** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3098 | **vina** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | ✓ |
| 3099 | **tingling** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3100 | **intently** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3101 | **razor-sharp** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3102 | **tising** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3103 | **ti-reciter** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3104 | **honest** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3105 | **i-reciter** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3106 | **fruition** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3107 | **sror** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3108 | **taut** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3109 | **inwardly** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3110 | **discour** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3111 | **mealtime** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | mealtime, mealtimes | — |
| 3112 | **undervalue** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3113 | **disobeying** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3114 | **treating** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3115 | **iala** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | iala, ialas | — |
| 3116 | **disrespectful** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3117 | **barbarian** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | barbarian, barbarians | — |
| 3118 | **slavery** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3119 | **blankness** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3120 | **inhabiting** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3121 | **eternalist** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | eternalist, eternalists | — |
| 3122 | **nihilist** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | nihilist, nihilists | — |
| 3123 | **tenma** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | ✓ རྟེན་མ་བཅུ་གཉིས |
| 3124 | **flower-garden** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3125 | **expounding** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3126 | **description** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | description, descriptions | — |
| 3127 | **disability** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | disabilities, disability | — |
| 3128 | **possessing** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3129 | **immersed** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3130 | **variance** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3131 | **prophecy** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3132 | **thonmi** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3133 | **sambhota** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3134 | **owo** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3135 | **thadul** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3136 | **yangdul** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3137 | **buddhism** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3138 | **unequalled** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3139 | **sfitra** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3140 | **ordained** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3141 | **shone** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3142 | **kind-hearted** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3143 | **delightful** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3144 | **renown** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3145 | **manifesting** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3146 | **devoid** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3147 | **quench** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3148 | **excellence** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3149 | **khu** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | ~ |
| 3150 | **ngok** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | ~ |
| 3151 | **stupidity** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3152 | **ensnared** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3153 | **guise** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3154 | **blindly** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3155 | **tinder** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3156 | **oxen** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3157 | **hither** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3158 | **thither** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3159 | **intentionally** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3160 | **hurl** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3161 | **neglect** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3162 | **indulging** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3163 | **pond** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3164 | **blaz** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3165 | **infernal** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3166 | **disintegrate** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3167 | **legion** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3168 | **wondrous** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3169 | **livelihood** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3170 | **ferociously** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3171 | **soldier** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | soldier, soldiers | — |
| 3172 | **breadth** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3173 | **limp** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3174 | **hide** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | 0.044473 | - | — |
| 3175 | **filthy** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3176 | **magnificent** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3177 | **five-fold** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3178 | **nyatri** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3179 | **dynasty** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | 0.297052 | - | — |
| 3180 | **splendour** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | splendour, splendours | — |
| 3181 | **prize** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3182 | **tall** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3183 | **degenerated** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3184 | **plague** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3185 | **survivor** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3186 | **preach** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3187 | **glow** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3188 | **blossom** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | blossom, blossoms | — |
| 3189 | **wither** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3190 | **goat** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3191 | **thunderbolt** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3192 | **fearful** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3193 | **behold** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3194 | **nausea** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3195 | **beggary** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3196 | **market-day** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3197 | **bicker** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3198 | **consecrated** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3199 | **dwelt** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3200 | **cliff** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3201 | **mandhatri** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | ✓ ང་ལས་ནུ |
| 3202 | **dandle** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3203 | **buried** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3204 | **erudite** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3205 | **talented** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3206 | **beget** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3207 | **yearn** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3208 | **aryadeva** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | ✓ འཕགས་པ་ལྷ |
| 3209 | **crave** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3210 | **phlegm** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | ✓ བད་ཀན |
| 3211 | **skeleton** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | skeleton, skeletons | — |
| 3212 | **tusk** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3213 | **forgetfulness** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3214 | **transient** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3215 | **lowly** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3216 | **deathless** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3217 | **imper** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3218 | **manence** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3219 | **nirvat** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3220 | **renunciate** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | renunciate, renunciates | — |
| 3221 | **permeated** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3222 | **ant** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3223 | **fiery** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3224 | **brandishing** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3225 | **phantom** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3226 | **slain** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3227 | **mortar** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3228 | **ofyama** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3229 | **hell-being** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3230 | **corre** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3231 | **spond** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3232 | **rounding-up** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3233 | **howling** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3234 | **bronze** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3235 | **sciousness** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3236 | **anus** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3237 | **glowing** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3238 | **subjected** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3239 | **salmali** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3240 | **mali** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3241 | **vulture** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | vulture, vultures | — |
| 3242 | **hideous** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3243 | **intolerable** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3244 | **groan** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3245 | **lotus-like** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3246 | **blistering** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3247 | **yamdrok** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3248 | **tangtong** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | ~ |
| 3249 | **glance** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3250 | **venerated** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3251 | **priest** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3252 | **quivering** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3253 | **knive** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3254 | **gleam** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3255 | **lovely** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3256 | **exemplary** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3257 | **shameful** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3258 | **withered** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3259 | **moonlight** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3260 | **srot** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3261 | **yelled** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3262 | **jetari** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3263 | **repulsive** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3264 | **wandered** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3265 | **afflict** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3266 | **stinginess** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3267 | **magician** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3268 | **imaginary** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3269 | **fragment** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | fragment, fragments | — |
| 3270 | **tum** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3271 | **garuc** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3272 | **gun** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | gun, guns | — |
| 3273 | **leopard** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3274 | **milked** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3275 | **sincerity** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3276 | **dread** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3277 | **adornment** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | adornment, adornments | — |
| 3278 | **mule** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3279 | **strand** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | strand, strands | — |
| 3280 | **disembowelled** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3281 | **suffocate** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | suffocate, suffocates | — |
| 3282 | **ewe** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3283 | **sip** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3284 | **calve** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3285 | **stolen** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3286 | **semen** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3287 | **fetus** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3288 | **banging** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3289 | **bony** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3290 | **rubbed** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3291 | **cradle** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3292 | **ripple** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3293 | **inconsequential** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3294 | **vigour** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3295 | **irritable** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3296 | **sing** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3297 | **stalking** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3298 | **protrude** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | protrude, protrudes | — |
| 3299 | **faded** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3300 | **scorn** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | scorn, scorns | — |
| 3301 | **terrify** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | 0.082265 | terrifies, terrify | — |
| 3302 | **hallucinate** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3303 | **realiz** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | realiz, realizes | — |
| 3304 | **descend** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3305 | **unending** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3306 | **miserliness** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3307 | **charity** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3308 | **hostility** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3309 | **cours** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3310 | **tea-leave** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3311 | **dishonour** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3312 | **splendidly** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3313 | **nourishing** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3314 | **harness** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3315 | **despair** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | despair, despairs | — |
| 3316 | **red-faced** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3317 | **calamity** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | calamities, calamity | — |
| 3318 | **collaps** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3319 | **expedition** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3320 | **slave** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | slave, slaves | — |
| 3321 | **degeneration** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | degeneration, degenerations | — |
| 3322 | **distinguishing** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | ~ |
| 3323 | **resentment** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3324 | **grabbing** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3325 | **supremely** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3326 | **suffused** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3327 | **sweat** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3328 | **ceaseless** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3329 | **cesspit** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3330 | **recollection** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3331 | **overjoyed** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3332 | **crackling** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3333 | **hell-realm** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3334 | **transgressed** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3335 | **circumambulate** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | 0.182316 | - | — |
| 3336 | **cherish** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3337 | **excrement** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3338 | **contaminate** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | 0.182500 | - | — |
| 3339 | **tsik** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3340 | **astray** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3341 | **predilection** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3342 | **graze** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3343 | **dung** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3344 | **lice** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3345 | **bride** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3346 | **gobble** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | gobble, gobbles | — |
| 3347 | **smacking** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3348 | **muzzle** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3349 | **ceas** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3350 | **staring** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3351 | **skinned** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3352 | **all-pervading** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3353 | **stove** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3354 | **stealth** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3355 | **clos** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3356 | **obsession** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | obsession, obsessions | — |
| 3357 | **brooding** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3358 | **charlatan** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3359 | **behaving** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3360 | **flaw** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3361 | **offensively** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3362 | **singing** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3363 | **distracting** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3364 | **chanting** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3365 | **partake** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3366 | **sixty-two** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3367 | **downhill** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3368 | **sharpness** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3369 | **giver** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | giver, givers | — |
| 3370 | **nourishment** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3371 | **sustenance** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3372 | **defile** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | 0.182436 | - | — |
| 3373 | **impulse** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3374 | **affinity** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3375 | **respite** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3376 | **disperse** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3377 | **impoverished** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3378 | **spouse** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3379 | **chore** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | chore, chores | — |
| 3380 | **reaping** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3381 | **insulted** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3382 | **denigrate** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | denigrate, denigrates | — |
| 3383 | **ravine** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3384 | **massacred** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3385 | **parivrajika** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3386 | **shrine** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3387 | **nirvar** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3388 | **kashmir** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3389 | **dyeing** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3390 | **sire** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3391 | **thief** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3392 | **kusa** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3393 | **disparage** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | disparage, disparages | — |
| 3394 | **ashota** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3395 | **scolded** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3396 | **serpent** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3397 | **rivalry** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3398 | **pratimo** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3399 | **stained** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3400 | **conversely** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3401 | **goodness** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3402 | **ofvajradhara** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3403 | **me-but** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3404 | **firstly** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3405 | **sastra** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | sastra, sastras | — |
| 3406 | **tripitaka** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | ✓ སྡེ་སྣོད་གསུམ |
| 3407 | **riddance** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3408 | **pitaka** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | ~ |
| 3409 | **ripening** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3410 | **tered** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3411 | **fief** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3412 | **puffed** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3413 | **bogus** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3414 | **unthinkingly** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3415 | **attuned** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3416 | **patiently** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3417 | **disci** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3418 | **radiate** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3419 | **simile** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3420 | **sparing** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3421 | **displeasing** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3422 | **anvil** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3423 | **sweeper** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3424 | **drank** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3425 | **mara** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | ✓ བདུད |
| 3426 | **respectfully** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3427 | **paramount** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3428 | **indivisibly** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3429 | **obeying** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3430 | **profess** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3431 | **profundity** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | profundities, profundity | — |
| 3432 | **pretending** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3433 | **superfluous** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3434 | **rongton** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3435 | **lhaga** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3436 | **trowolung** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3437 | **imitation** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3438 | **engraved** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3439 | **wasteland** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3440 | **paramita** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3441 | **venerate** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3442 | **crossroad** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3443 | **thigh** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3444 | **preaching** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3445 | **filigree** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | filigree, filigrees | — |
| 3446 | **lapi** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3447 | **lazuli** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3448 | **maiden** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3449 | **proclaim** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | proclaim, proclaims | — |
| 3450 | **nine-storey** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3451 | **bamboo** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3452 | **toe** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3453 | **labourer** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3454 | **twenty-four** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3455 | **obscura** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3456 | **awakened** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3457 | **disobey** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3458 | **vikramasila** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3459 | **hailstorm** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | hailstorm, hailstorms | — |
| 3460 | **yungton** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3461 | **jug** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3462 | **sariwara** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3463 | **shepa** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3464 | **drowning** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3465 | **entrance-way** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3466 | **vivid** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3467 | **relic** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3468 | **kongpo** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3469 | **wick** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | wick, wicks | — |
| 3470 | **five-pronged** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3471 | **hooked** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3472 | **hadra** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3473 | **rabjampa** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3474 | **on-and** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3475 | **avalokitesvara-and** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3476 | **rear** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3477 | **encased** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3478 | **vowel** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | vowel, vowels | — |
| 3479 | **sugata** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | ✓ བདེ་བར་གཤེགས་པ |
| 3480 | **yearning** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3481 | **visnu** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3482 | **springing** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3483 | **glare** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3484 | **hid** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3485 | **manifested** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3486 | **fourfold** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3487 | **paqc** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3488 | **painting** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | painting, paintings | — |
| 3489 | **vairocana** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | ✓ རྣམ་པར་སྣང་མཛད |
| 3490 | **beneficent** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3491 | **ajatasatru** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3492 | **fury** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3493 | **scoop** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3494 | **enlight** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3495 | **enment** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3496 | **lovingly** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3497 | **jarung** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3498 | **khashor** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3499 | **gentle** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3500 | **despised** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3501 | **summoning** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3502 | **dungeon** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3503 | **packhors** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3504 | **pain-you** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3505 | **panting** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3506 | **thrash** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3507 | **atsara** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3508 | **relishing** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | ~ |
| 3509 | **faint** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3510 | **marching** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3511 | **religion** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3512 | **paq** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3513 | **altruistic** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3514 | **lungpa** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | ~ |
| 3515 | **lhungpa** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3516 | **thenceforth** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3517 | **vasubandhu** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3518 | **departed** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3519 | **feather** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3520 | **unkind** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3521 | **pletely** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3522 | **tarlo** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3523 | **mistress** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3524 | **swim** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3525 | **shawopa** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3526 | **imponant** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3527 | **conceived** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3528 | **eighty-four** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3529 | **harnessed** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3530 | **belonged** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3531 | **jeweller** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3532 | **ancestor** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3533 | **hem** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3534 | **exquisite** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3535 | **fist** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | fist, fists | — |
| 3536 | **chakshingwa** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | ~ |
| 3537 | **shangshungpa** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3538 | **feverish** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3539 | **manicuda** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3540 | **dawned** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3541 | **bathed** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3542 | **brighu** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3543 | **sprang** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3544 | **duly** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3545 | **dharani** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | dharani, dharanis | ✓ གཟུངས |
| 3546 | **tigress** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3547 | **laced** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3548 | **ego** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3549 | **craving** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | craving, cravings | — |
| 3550 | **yourselve** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3551 | **armour-like** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3552 | **preoccupation** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3553 | **diparhkara** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3554 | **childish** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3555 | **distrac** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3556 | **lonely** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3557 | **secluded** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3558 | **ascetic** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3559 | **discerning** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3560 | **concen** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3561 | **tration** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3562 | **athagata** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3563 | **equanimity** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3564 | **analysi** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3565 | **spoilt** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3566 | **transcend** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | transcend, transcends | — |
| 3567 | **self-liberation** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3568 | **saraha** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | ✓ ས་ར་ཧ |
| 3569 | **kharak** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | ~ |
| 3570 | **gomchung** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | ~ |
| 3571 | **demonic** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3572 | **spiritually** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3573 | **nachung** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3574 | **non-buddhist** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3575 | **diminution** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3576 | **small-minded** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3577 | **cultivating** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3578 | **hiding** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3579 | **chagme** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | ~ |
| 3580 | **necklace** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | necklace, necklaces | — |
| 3581 | **perverse** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | ~ |
| 3582 | **venge** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3583 | **orna** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3584 | **appeased** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3585 | **navel** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3586 | **conch** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | conch, conches | — |
| 3587 | **light-ray** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3588 | **shapkyu** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | ✓ ཞབས་ཀྱུ |
| 3589 | **crescent** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3590 | **bindu** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | ✓ ཐིག་ལེ |
| 3591 | **nada** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | ✓ |
| 3592 | **ofvajrasattva** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3593 | **cymbal** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3594 | **prayer-book** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | prayer-book, prayer-books | — |
| 3595 | **transgressor** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3596 | **shingkyong** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3597 | **tation** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3598 | **sullied** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3599 | **snivaka** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3600 | **gifted** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3601 | **surround** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | 0.038386 | - | — |
| 3602 | **rime** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | rime, rimes | — |
| 3603 | **underside** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | underside, undersides | — |
| 3604 | **clockwise** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3605 | **multiplying** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3606 | **multiplied** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3607 | **cleanly** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3608 | **churning** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3609 | **propitiating** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3610 | **ascending** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3611 | **eyebrow** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3612 | **brow** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | brow, brows | — |
| 3613 | **seventy-five** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3614 | **imbibe** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3615 | **iakini** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3616 | **tara** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | ✓ སྒྲོལ་མ |
| 3617 | **boast** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | boast, boasts | — |
| 3618 | **elemental** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3619 | **fearsome** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3620 | **annihilate** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3621 | **prophesied** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3622 | **goblin** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3623 | **dualistic** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | ✓ གཉིས་འཛིན |
| 3624 | **core-teaching** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3625 | **fervent** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3626 | **drikung** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | ~ |
| 3627 | **kyobpa** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | ~ |
| 3628 | **intellect** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | intellect, intellects | — |
| 3629 | **trekcho** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3630 | **gazing** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3631 | **longingly** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3632 | **skull-drum** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3633 | **charnel-ground** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3634 | **zahor** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3635 | **symbolizing** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3636 | **mudra** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | ~ |
| 3637 | **sambhoga** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3638 | **five-coloured** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3639 | **subjugated** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3640 | **luminous** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3641 | **sphere** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3642 | **knee** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3643 | **unfathomable** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3644 | **hypocrisy** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3645 | **intending** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3646 | **entreat** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3647 | **upayoga** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3648 | **mahayoga** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3649 | **anuyoga** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | ✓ |
| 3650 | **ofg** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3651 | **reat** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3652 | **lotus-born** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3653 | **ruby** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | rubies, ruby | — |
| 3654 | **muni** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | ✓ ཐུབ་པ |
| 3655 | **twenty-eight** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3656 | **vajrapat** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3657 | **dhanakosa** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3658 | **sattvavajra** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | ✓ སེམས་དཔའ་རྡོ་རྗེ |
| 3659 | **nine-pointed** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3660 | **expans** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3661 | **rajahasti** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3662 | **paqqita** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | paqqita, paqqitas | — |
| 3663 | **yamantaka** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | ✓ གཤིན་རྗེ་གཤེད |
| 3664 | **acarya** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | ✓ སློབ་དཔོན |
| 3665 | **non-human** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | non-human, non-humans | — |
| 3666 | **genyen** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | ~ |
| 3667 | **treasure-discoverer** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | treasure-discoverer, treasure-discoverers | — |
| 3668 | **familiarity** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3669 | **mahamudra** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | ✓ ཕྱག་རྒྱ་ཆེན་པོ |
| 3670 | **ofvajra** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3671 | **yogini** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | ~ |
| 3672 | **enclosure** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3673 | **vibrating** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3674 | **mind-awareness** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3675 | **kyabje** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3676 | **kagyu** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3677 | **gampopa** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | ~ |
| 3678 | **instruc** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3679 | **phras** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3680 | **drunk** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3681 | **wangpo** | 2 | 332.39 | 9.59 | 🔵 low — common in general English | - | - | — |
| 3682 | **concerning** | 3 | 331.39 | 6.374259 | 🔵 low — common in general English | - | - | — |
| 3683 | **seriously** | 3 | 331.39 | 6.374259 | 🔵 low — common in general English | - | - | — |
| 3684 | **continued** | 4 | 329.74 | 4.756853 | 🔵 low — common in general English | - | - | — |
| 3685 | **band** | 3 | 329.36 | 6.335039 | 🔵 low — common in general English | - | - | — |
| 3686 | **directly** | 3 | 329.36 | 6.335039 | 🔵 low — common in general English | - | - | — |
| 3687 | **chinese** | 3 | 328.36 | 6.31599 | 🔵 low — common in general English | 0.186719 | - | — |
| 3688 | **delay** | 3 | 327.39 | 6.297298 | 🔵 low — common in general English | - | - | — |
| 3689 | **detailed** | 3 | 327.39 | 6.297298 | 🔵 low — common in general English | - | - | — |
| 3690 | **island** | 3 | 326.44 | 6.278949 | 🔵 low — common in general English | - | - | — |
| 3691 | **account** | 4 | 325.99 | 4.702786 | 🔵 low — common in general English | - | account, accounts | — |
| 3692 | **broad** | 3 | 325.50 | 6.260931 | 🔵 low — common in general English | - | - | — |
| 3693 | **hostile** | 3 | 325.50 | 6.260931 | 🔵 low — common in general English | - | - | — |
| 3694 | **debate** | 3 | 325.50 | 6.260931 | 🔵 low — common in general English | - | - | — |
| 3695 | **status** | 3 | 324.58 | 6.243231 | 🔵 low — common in general English | - | - | — |
| 3696 | **closely** | 3 | 321.92 | 6.191938 | 🔵 low — common in general English | - | - | — |
| 3697 | **test** | 3 | 321.92 | 6.191938 | 🔵 low — common in general English | - | - | — |
| 3698 | **community** | 4 | 321.70 | 4.640835 | 🔵 low — common in general English | - | communities, community | — |
| 3699 | **adopted** | 3 | 319.38 | 6.143148 | 🔵 low — common in general English | - | - | — |
| 3700 | **sheet** | 3 | 319.38 | 6.143148 | 🔵 low — common in general English | - | - | — |
| 3701 | **trader** | 3 | 319.38 | 6.143148 | 🔵 low — common in general English | - | trader, traders | — |
| 3702 | **raised** | 4 | 318.59 | 4.595923 | 🔵 low — common in general English | - | - | — |
| 3703 | **prescription** | 2 | 318.44 | 9.18767 | 🔵 low — common in general English | - | - | — |
| 3704 | **excel** | 2 | 318.44 | 9.18767 | 🔵 low — common in general English | - | - | — |
| 3705 | **propensity** | 2 | 318.44 | 9.18767 | 🔵 low — common in general English | - | - | — |
| 3706 | **younger** | 2 | 318.44 | 9.18767 | 🔵 low — common in general English | - | - | — |
| 3707 | **monarch** | 2 | 318.44 | 9.18767 | 🔵 low — common in general English | - | monarch, monarchs | ~ |
| 3708 | **festival** | 2 | 318.44 | 9.18767 | 🔵 low — common in general English | - | - | — |
| 3709 | **embraced** | 2 | 318.44 | 9.18767 | 🔵 low — common in general English | - | - | — |
| 3710 | **inheritance** | 2 | 318.44 | 9.18767 | 🔵 low — common in general English | - | - | — |
| 3711 | **wounded** | 2 | 318.44 | 9.18767 | 🔵 low — common in general English | - | - | — |
| 3712 | **misguided** | 2 | 318.44 | 9.18767 | 🔵 low — common in general English | - | - | — |
| 3713 | **rotting** | 2 | 318.44 | 9.18767 | 🔵 low — common in general English | - | - | — |
| 3714 | **trickle** | 2 | 318.44 | 9.18767 | 🔵 low — common in general English | - | - | — |
| 3715 | **misuse** | 2 | 318.44 | 9.18767 | 🔵 low — common in general English | - | - | — |
| 3716 | **revealing** | 2 | 318.44 | 9.18767 | 🔵 low — common in general English | - | - | — |
| 3717 | **flew** | 2 | 318.44 | 9.18767 | 🔵 low — common in general English | - | - | — |
| 3718 | **bury** | 2 | 318.44 | 9.18767 | 🔵 low — common in general English | - | buries, bury | — |
| 3719 | **exploited** | 2 | 318.44 | 9.18767 | 🔵 low — common in general English | - | - | — |
| 3720 | **pulling** | 2 | 318.44 | 9.18767 | 🔵 low — common in general English | - | - | — |
| 3721 | **wasting** | 2 | 318.44 | 9.18767 | 🔵 low — common in general English | - | - | — |
| 3722 | **frightened** | 2 | 318.44 | 9.18767 | 🔵 low — common in general English | - | - | — |
| 3723 | **uproot** | 2 | 318.44 | 9.18767 | 🔵 low — common in general English | - | - | — |
| 3724 | **subside** | 2 | 318.44 | 9.18767 | 🔵 low — common in general English | - | subside, subsides | — |
| 3725 | **monkey** | 2 | 318.44 | 9.18767 | 🔵 low — common in general English | - | - | — |
| 3726 | **echo** | 2 | 318.44 | 9.18767 | 🔵 low — common in general English | - | - | — |
| 3727 | **empty-handed** | 2 | 318.44 | 9.18767 | 🔵 low — common in general English | - | - | — |
| 3728 | **prosper** | 2 | 318.44 | 9.18767 | 🔵 low — common in general English | - | - | — |
| 3729 | **painted** | 2 | 318.44 | 9.18767 | 🔵 low — common in general English | - | - | — |
| 3730 | **confessed** | 2 | 318.44 | 9.18767 | 🔵 low — common in general English | - | - | — |
| 3731 | **childhood** | 2 | 318.44 | 9.18767 | 🔵 low — common in general English | - | - | — |
| 3732 | **falcon** | 2 | 318.44 | 9.18767 | 🔵 low — common in general English | - | falcon, falcons | — |
| 3733 | **fade** | 2 | 318.44 | 9.18767 | 🔵 low — common in general English | - | - | — |
| 3734 | **needy** | 2 | 318.44 | 9.18767 | 🔵 low — common in general English | - | - | — |
| 3735 | **beset** | 2 | 318.44 | 9.18767 | 🔵 low — common in general English | - | - | — |
| 3736 | **pen** | 2 | 318.44 | 9.18767 | 🔵 low — common in general English | - | - | — |
| 3737 | **secondly** | 2 | 318.44 | 9.18767 | 🔵 low — common in general English | - | - | — |
| 3738 | **lifeline** | 2 | 318.44 | 9.18767 | 🔵 low — common in general English | - | - | — |
| 3739 | **embodied** | 2 | 318.44 | 9.18767 | 🔵 low — common in general English | - | - | — |
| 3740 | **disregard** | 2 | 318.44 | 9.18767 | 🔵 low — common in general English | - | - | — |
| 3741 | **dressed** | 2 | 318.44 | 9.18767 | 🔵 low — common in general English | - | - | — |
| 3742 | **richer** | 2 | 318.44 | 9.18767 | 🔵 low — common in general English | - | - | — |
| 3743 | **tamed** | 2 | 318.44 | 9.18767 | 🔵 low — common in general English | - | - | — |
| 3744 | **motivate** | 2 | 318.44 | 9.18767 | 🔵 low — common in general English | - | - | — |
| 3745 | **rounded** | 2 | 318.44 | 9.18767 | 🔵 low — common in general English | - | - | — |
| 3746 | **seventeen** | 2 | 318.44 | 9.18767 | 🔵 low — common in general English | - | - | — |
| 3747 | **incredible** | 2 | 318.44 | 9.18767 | 🔵 low — common in general English | - | - | — |
| 3748 | **subdue** | 2 | 318.44 | 9.18767 | 🔵 low — common in general English | - | subdue, subdues | — |
| 3749 | **wrongdoing** | 2 | 318.44 | 9.18767 | 🔵 low — common in general English | - | - | — |
| 3750 | **bite** | 2 | 318.44 | 9.18767 | 🔵 low — common in general English | - | - | — |
| 3751 | **sentence** | 2 | 318.44 | 9.18767 | 🔵 low — common in general English | - | - | — |
| 3752 | **occupation** | 2 | 318.44 | 9.18767 | 🔵 low — common in general English | - | occupation, occupations | — |
| 3753 | **liked** | 2 | 318.44 | 9.18767 | 🔵 low — common in general English | - | - | — |
| 3754 | **invalid** | 2 | 318.44 | 9.18767 | 🔵 low — common in general English | - | - | — |
| 3755 | **obscured** | 2 | 318.44 | 9.18767 | 🔵 low — common in general English | - | - | — |
| 3756 | **entirety** | 2 | 318.44 | 9.18767 | 🔵 low — common in general English | - | - | — |
| 3757 | **trained** | 2 | 318.44 | 9.18767 | 🔵 low — common in general English | - | - | — |
| 3758 | **flattened** | 2 | 318.44 | 9.18767 | 🔵 low — common in general English | - | - | — |
| 3759 | **owe** | 2 | 318.44 | 9.18767 | 🔵 low — common in general English | - | - | — |
| 3760 | **vengeance** | 2 | 318.44 | 9.18767 | 🔵 low — common in general English | - | - | — |
| 3761 | **spiralling** | 2 | 318.44 | 9.18767 | 🔵 low — common in general English | - | - | — |
| 3762 | **hence** | 2 | 318.44 | 9.18767 | 🔵 low — common in general English | - | - | — |
| 3763 | **narrow** | 3 | 316.96 | 6.096628 | 🔵 low — common in general English | - | - | — |
| 3764 | **wholly** | 3 | 313.16 | 6.023602 | 🔵 low — common in general English | - | - | — |
| 3765 | **acquiring** | 3 | 311.72 | 5.995823 | 🔵 low — common in general English | - | - | — |
| 3766 | **introduced** | 3 | 311.72 | 5.995823 | 🔵 low — common in general English | - | - | — |
| 3767 | **requirement** | 3 | 310.31 | 5.968794 | 🔵 low — common in general English | - | - | — |
| 3768 | **granted** | 3 | 310.31 | 5.968794 | 🔵 low — common in general English | - | - | — |
| 3769 | **earlier** | 5 | 310.05 | 3.578198 | 🔵 low — common in general English | - | - | — |
| 3770 | **encourage** | 3 | 309.63 | 5.955549 | 🔵 low — common in general English | - | - | — |
| 3771 | **intended** | 3 | 309.63 | 5.955549 | 🔵 low — common in general English | - | - | — |
| 3772 | **unaware** | 2 | 308.47 | 8.899988 | 🔵 low — common in general English | - | - | — |
| 3773 | **ignoring** | 2 | 308.47 | 8.899988 | 🔵 low — common in general English | - | - | — |
| 3774 | **tense** | 2 | 308.47 | 8.899988 | 🔵 low — common in general English | - | - | — |
| 3775 | **mode** | 2 | 308.47 | 8.899988 | 🔵 low — common in general English | - | mode, modes | — |
| 3776 | **geographically** | 2 | 308.47 | 8.899988 | 🔵 low — common in general English | - | - | — |
| 3777 | **rarely** | 2 | 308.47 | 8.899988 | 🔵 low — common in general English | - | - | — |
| 3778 | **strenuous** | 2 | 308.47 | 8.899988 | 🔵 low — common in general English | - | - | — |
| 3779 | **swimming** | 2 | 308.47 | 8.899988 | 🔵 low — common in general English | - | - | — |
| 3780 | **deliberate** | 2 | 308.47 | 8.899988 | 🔵 low — common in general English | - | - | — |
| 3781 | **pursuit** | 2 | 308.47 | 8.899988 | 🔵 low — common in general English | - | - | — |
| 3782 | **blizzard** | 2 | 308.47 | 8.899988 | 🔵 low — common in general English | - | blizzard, blizzards | — |
| 3783 | **derive** | 2 | 308.47 | 8.899988 | 🔵 low — common in general English | - | - | — |
| 3784 | **slice** | 2 | 308.47 | 8.899988 | 🔵 low — common in general English | - | - | — |
| 3785 | **grease** | 2 | 308.47 | 8.899988 | 🔵 low — common in general English | - | - | — |
| 3786 | **encountering** | 2 | 308.47 | 8.899988 | 🔵 low — common in general English | - | - | — |
| 3787 | **ploughing** | 2 | 308.47 | 8.899988 | 🔵 low — common in general English | - | - | — |
| 3788 | **digest** | 2 | 308.47 | 8.899988 | 🔵 low — common in general English | - | - | — |
| 3789 | **dim** | 2 | 308.47 | 8.899988 | 🔵 low — common in general English | - | dim, dims | — |
| 3790 | **appetite** | 2 | 308.47 | 8.899988 | 🔵 low — common in general English | - | - | — |
| 3791 | **carcass** | 2 | 308.47 | 8.899988 | 🔵 low — common in general English | - | - | — |
| 3792 | **forceful** | 2 | 308.47 | 8.899988 | 🔵 low — common in general English | - | - | — |
| 3793 | **eradicated** | 2 | 308.47 | 8.899988 | 🔵 low — common in general English | - | - | — |
| 3794 | **rift** | 2 | 308.47 | 8.899988 | 🔵 low — common in general English | - | - | — |
| 3795 | **donation** | 2 | 308.47 | 8.899988 | 🔵 low — common in general English | - | - | — |
| 3796 | **excuse** | 2 | 308.47 | 8.899988 | 🔵 low — common in general English | - | - | — |
| 3797 | **donor** | 2 | 308.47 | 8.899988 | 🔵 low — common in general English | - | - | — |
| 3798 | **muddy** | 2 | 308.47 | 8.899988 | 🔵 low — common in general English | - | - | — |
| 3799 | **diversity** | 2 | 308.47 | 8.899988 | 🔵 low — common in general English | - | - | — |
| 3800 | **handed** | 2 | 308.47 | 8.899988 | 🔵 low — common in general English | - | - | — |
| 3801 | **hay** | 2 | 308.47 | 8.899988 | 🔵 low — common in general English | - | - | — |
| 3802 | **permissible** | 2 | 308.47 | 8.899988 | 🔵 low — common in general English | - | - | — |
| 3803 | **impress** | 2 | 308.47 | 8.899988 | 🔵 low — common in general English | - | - | — |
| 3804 | **disturbed** | 2 | 308.47 | 8.899988 | 🔵 low — common in general English | - | - | — |
| 3805 | **checked** | 2 | 308.47 | 8.899988 | 🔵 low — common in general English | - | - | — |
| 3806 | **absorption** | 2 | 308.47 | 8.899988 | 🔵 low — common in general English | - | - | — |
| 3807 | **extraordinarily** | 2 | 308.47 | 8.899988 | 🔵 low — common in general English | - | - | — |
| 3808 | **constrained** | 2 | 308.47 | 8.899988 | 🔵 low — common in general English | - | - | — |
| 3809 | **uncovered** | 2 | 308.47 | 8.899988 | 🔵 low — common in general English | - | - | — |
| 3810 | **sausage** | 2 | 308.47 | 8.899988 | 🔵 low — common in general English | - | - | — |
| 3811 | **ingredient** | 2 | 308.47 | 8.899988 | 🔵 low — common in general English | - | ingredient, ingredients | — |
| 3812 | **witness** | 2 | 308.47 | 8.899988 | 🔵 low — common in general English | - | witness, witnesses | — |
| 3813 | **vain** | 2 | 308.47 | 8.899988 | 🔵 low — common in general English | - | - | — |
| 3814 | **contamination** | 2 | 308.47 | 8.899988 | 🔵 low — common in general English | - | - | — |
| 3815 | **sow** | 2 | 308.47 | 8.899988 | 🔵 low — common in general English | 0.055646 | - | — |
| 3816 | **blend** | 2 | 308.47 | 8.899988 | 🔵 low — common in general English | - | - | — |
| 3817 | **unity** | 2 | 308.47 | 8.899988 | 🔵 low — common in general English | - | - | — |
| 3818 | **satisfying** | 2 | 308.47 | 8.899988 | 🔵 low — common in general English | - | - | — |
| 3819 | **bend** | 2 | 308.47 | 8.899988 | 🔵 low — common in general English | - | - | — |
| 3820 | **successful** | 3 | 307.61 | 5.916835 | 🔵 low — common in general English | - | - | — |
| 3821 | **consideration** | 3 | 306.31 | 5.891833 | 🔵 low — common in general English | - | consideration, considerations | — |
| 3822 | **effective** | 4 | 305.99 | 4.414165 | 🔵 low — common in general English | 0.231962 | - | — |
| 3823 | **suspended** | 3 | 305.05 | 5.867442 | 🔵 low — common in general English | - | - | — |
| 3824 | **post** | 3 | 305.05 | 5.867442 | 🔵 low — common in general English | - | - | — |
| 3825 | **interested** | 3 | 304.42 | 5.855466 | 🔵 low — common in general English | - | - | — |
| 3826 | **controlled** | 3 | 303.20 | 5.831935 | 🔵 low — common in general English | - | - | — |
| 3827 | **identifying** | 2 | 300.74 | 8.676844 | 🔵 low — common in general English | - | - | — |
| 3828 | **hunting** | 2 | 300.74 | 8.676844 | 🔵 low — common in general English | - | - | — |
| 3829 | **reward** | 2 | 300.74 | 8.676844 | 🔵 low — common in general English | - | - | — |
| 3830 | **dissatisfaction** | 2 | 300.74 | 8.676844 | 🔵 low — common in general English | - | - | — |
| 3831 | **prestige** | 2 | 300.74 | 8.676844 | 🔵 low — common in general English | - | - | — |
| 3832 | **balancing** | 2 | 300.74 | 8.676844 | 🔵 low — common in general English | - | - | — |
| 3833 | **shrink** | 2 | 300.74 | 8.676844 | 🔵 low — common in general English | - | - | — |
| 3834 | **shorter** | 2 | 300.74 | 8.676844 | 🔵 low — common in general English | - | - | — |
| 3835 | **confronted** | 2 | 300.74 | 8.676844 | 🔵 low — common in general English | - | - | — |
| 3836 | **captured** | 2 | 300.74 | 8.676844 | 🔵 low — common in general English | - | - | — |
| 3837 | **relieved** | 2 | 300.74 | 8.676844 | 🔵 low — common in general English | - | - | — |
| 3838 | **corner** | 2 | 300.74 | 8.676844 | 🔵 low — common in general English | - | corner, corners | — |
| 3839 | **mere** | 2 | 300.74 | 8.676844 | 🔵 low — common in general English | - | - | — |
| 3840 | **somehow** | 2 | 300.74 | 8.676844 | 🔵 low — common in general English | - | - | — |
| 3841 | **anyway** | 2 | 300.74 | 8.676844 | 🔵 low — common in general English | - | - | — |
| 3842 | **freely** | 2 | 300.74 | 8.676844 | 🔵 low — common in general English | - | - | — |
| 3843 | **resemble** | 2 | 300.74 | 8.676844 | 🔵 low — common in general English | - | - | — |
| 3844 | **rushed** | 2 | 300.74 | 8.676844 | 🔵 low — common in general English | - | - | — |
| 3845 | **prediction** | 2 | 300.74 | 8.676844 | 🔵 low — common in general English | - | - | — |
| 3846 | **travelled** | 2 | 300.74 | 8.676844 | 🔵 low — common in general English | - | - | — |
| 3847 | **closest** | 2 | 300.74 | 8.676844 | 🔵 low — common in general English | - | - | — |
| 3848 | **unfavourable** | 2 | 300.74 | 8.676844 | 🔵 low — common in general English | - | - | — |
| 3849 | **overwhelming** | 2 | 300.74 | 8.676844 | 🔵 low — common in general English | - | - | — |
| 3850 | **voyage** | 2 | 300.74 | 8.676844 | 🔵 low — common in general English | - | voyage, voyages | — |
| 3851 | **alongside** | 2 | 300.74 | 8.676844 | 🔵 low — common in general English | - | - | — |
| 3852 | **stopping** | 2 | 300.74 | 8.676844 | 🔵 low — common in general English | - | - | — |
| 3853 | **sunbeam** | 2 | 300.74 | 8.676844 | 🔵 low — common in general English | - | sunbeam, sunbeams | — |
| 3854 | **guiding** | 2 | 300.74 | 8.676844 | 🔵 low — common in general English | - | - | — |
| 3855 | **failure** | 3 | 299.69 | 5.764494 | 🔵 low — common in general English | - | - | — |
| 3856 | **concerned** | 3 | 298.02 | 5.732405 | 🔵 low — common in general English | - | - | — |
| 3857 | **their** | 5 | 298.02 | 3.439339 | 🔵 low — common in general English | - | - | — |
| 3858 | **preceded** | 2 | 294.42 | 8.494523 | 🔵 low — common in general English | - | - | — |
| 3859 | **freeing** | 2 | 294.42 | 8.494523 | 🔵 low — common in general English | - | - | — |
| 3860 | **fragile** | 2 | 294.42 | 8.494523 | 🔵 low — common in general English | - | - | — |
| 3861 | **chose** | 2 | 294.42 | 8.494523 | 🔵 low — common in general English | - | - | — |
| 3862 | **paradise** | 2 | 294.42 | 8.494523 | 🔵 low — common in general English | - | - | — |
| 3863 | **separation** | 2 | 294.42 | 8.494523 | 🔵 low — common in general English | - | - | — |
| 3864 | **collect** | 2 | 294.42 | 8.494523 | 🔵 low — common in general English | - | - | — |
| 3865 | **leap** | 2 | 294.42 | 8.494523 | 🔵 low — common in general English | - | - | — |
| 3866 | **stranded** | 2 | 294.42 | 8.494523 | 🔵 low — common in general English | - | - | — |
| 3867 | **drift** | 2 | 294.42 | 8.494523 | 🔵 low — common in general English | - | - | — |
| 3868 | **pinpoint** | 2 | 294.42 | 8.494523 | 🔵 low — common in general English | - | - | — |
| 3869 | **addressed** | 2 | 294.42 | 8.494523 | 🔵 low — common in general English | - | - | — |
| 3870 | **reinforce** | 2 | 294.42 | 8.494523 | 🔵 low — common in general English | - | - | — |
| 3871 | **cell** | 2 | 294.42 | 8.494523 | 🔵 low — common in general English | - | - | — |
| 3872 | **dis** | 2 | 294.42 | 8.494523 | 🔵 low — common in general English | - | - | — |
| 3873 | **donated** | 2 | 294.42 | 8.494523 | 🔵 low — common in general English | - | - | — |
| 3874 | **liable** | 2 | 294.42 | 8.494523 | 🔵 low — common in general English | - | - | — |
| 3875 | **matured** | 2 | 294.42 | 8.494523 | 🔵 low — common in general English | - | - | — |
| 3876 | **sailing** | 2 | 294.42 | 8.494523 | 🔵 low — common in general English | - | - | — |
| 3877 | **fulfilling** | 2 | 294.42 | 8.494523 | 🔵 low — common in general English | - | - | ~ |
| 3878 | **mad** | 2 | 294.42 | 8.494523 | 🔵 low — common in general English | - | - | — |
| 3879 | **survival** | 2 | 294.42 | 8.494523 | 🔵 low — common in general English | - | - | — |
| 3880 | **forgiveness** | 2 | 294.42 | 8.494523 | 🔵 low — common in general English | - | - | — |
| 3881 | **vigorous** | 2 | 294.42 | 8.494523 | 🔵 low — common in general English | 0.233824 | - | — |
| 3882 | **rough** | 2 | 294.42 | 8.494523 | 🔵 low — common in general English | - | - | — |
| 3883 | **benefiting** | 2 | 294.42 | 8.494523 | 🔵 low — common in general English | - | - | — |
| 3884 | **bud** | 2 | 294.42 | 8.494523 | 🔵 low — common in general English | - | - | — |
| 3885 | **whichever** | 2 | 294.42 | 8.494523 | 🔵 low — common in general English | - | - | — |
| 3886 | **sam** | 2 | 294.42 | 8.494523 | 🔵 low — common in general English | - | - | — |
| 3887 | **soften** | 2 | 294.42 | 8.494523 | 🔵 low — common in general English | - | - | — |
| 3888 | **foremost** | 2 | 294.42 | 8.494523 | 🔵 low — common in general English | - | - | — |
| 3889 | **agree** | 3 | 293.82 | 5.651553 | 🔵 low — common in general English | - | - | — |
| 3890 | **equivalent** | 3 | 292.82 | 5.632322 | 🔵 low — common in general English | - | - | — |
| 3891 | **normal** | 3 | 292.33 | 5.622843 | 🔵 low — common in general English | - | - | — |
| 3892 | **system** | 4 | 291.58 | 4.206349 | 🔵 low — common in general English | - | system, systems | — |
| 3893 | **completion** | 3 | 289.93 | 5.576752 | 🔵 low — common in general English | - | - | — |
| 3894 | **dispute** | 3 | 289.47 | 5.567784 | 🔵 low — common in general English | - | dispute, disputes | — |
| 3895 | **opened** | 3 | 289.47 | 5.567784 | 🔵 low — common in general English | - | - | — |
| 3896 | **sold** | 4 | 289.09 | 4.17039 | 🔵 low — common in general English | - | - | — |
| 3897 | **subdued** | 2 | 289.07 | 8.340372 | 🔵 low — common in general English | - | - | — |
| 3898 | **valuable** | 2 | 289.07 | 8.340372 | 🔵 low — common in general English | - | valuable, valuables | — |
| 3899 | **patch** | 2 | 289.07 | 8.340372 | 🔵 low — common in general English | - | patch, patches | — |
| 3900 | **seized** | 2 | 289.07 | 8.340372 | 🔵 low — common in general English | - | - | — |
| 3901 | **observed** | 2 | 289.07 | 8.340372 | 🔵 low — common in general English | - | - | — |
| 3902 | **patient** | 2 | 289.07 | 8.340372 | 🔵 low — common in general English | - | - | — |
| 3903 | **hired** | 2 | 289.07 | 8.340372 | 🔵 low — common in general English | - | - | — |
| 3904 | **anybody** | 2 | 289.07 | 8.340372 | 🔵 low — common in general English | - | - | — |
| 3905 | **tate** | 2 | 289.07 | 8.340372 | 🔵 low — common in general English | - | - | — |
| 3906 | **abundant** | 2 | 289.07 | 8.340372 | 🔵 low — common in general English | - | - | — |
| 3907 | **style** | 2 | 289.07 | 8.340372 | 🔵 low — common in general English | - | - | — |
| 3908 | **requesting** | 2 | 289.07 | 8.340372 | 🔵 low — common in general English | - | - | — |
| 3909 | **reflected** | 3 | 289.00 | 5.558895 | 🔵 low — common in general English | - | - | — |
| 3910 | **unconditional** | 2 | 284.45 | 8.206841 | 🔵 low — common in general English | - | - | — |
| 3911 | **consult** | 2 | 284.45 | 8.206841 | 🔵 low — common in general English | 0.149592 | - | — |
| 3912 | **influenced** | 2 | 284.45 | 8.206841 | 🔵 low — common in general English | - | - | — |
| 3913 | **geography** | 2 | 284.45 | 8.206841 | 🔵 low — common in general English | - | - | — |
| 3914 | **existed** | 2 | 284.45 | 8.206841 | 🔵 low — common in general English | - | - | — |
| 3915 | **older** | 2 | 284.45 | 8.206841 | 🔵 low — common in general English | - | - | — |
| 3916 | **struggle** | 2 | 284.45 | 8.206841 | 🔵 low — common in general English | - | - | — |
| 3917 | **cheating** | 2 | 284.45 | 8.206841 | 🔵 low — common in general English | - | - | — |
| 3918 | **peg** | 2 | 284.45 | 8.206841 | 🔵 low — common in general English | - | - | — |
| 3919 | **lined** | 2 | 284.45 | 8.206841 | 🔵 low — common in general English | - | - | — |
| 3920 | **helpful** | 2 | 284.45 | 8.206841 | 🔵 low — common in general English | - | - | — |
| 3921 | **abandoning** | 2 | 284.45 | 8.206841 | 🔵 low — common in general English | - | - | — |
| 3922 | **relax** | 2 | 284.45 | 8.206841 | 🔵 low — common in general English | - | - | — |
| 3923 | **unique** | 2 | 284.45 | 8.206841 | 🔵 low — common in general English | - | - | — |
| 3924 | **tug** | 2 | 284.45 | 8.206841 | 🔵 low — common in general English | - | tug, tugs | — |
| 3925 | **undoubtedly** | 2 | 284.45 | 8.206841 | 🔵 low — common in general English | - | - | — |
| 3926 | **released** | 3 | 284.17 | 5.466001 | 🔵 low — common in general English | - | - | — |
| 3927 | **steel** | 3 | 282.12 | 5.42647 | 🔵 low — common in general English | - | - | — |
| 3928 | **entertain** | 2 | 280.36 | 8.089058 | 🔵 low — common in general English | - | - | — |
| 3929 | **burned** | 2 | 280.36 | 8.089058 | 🔵 low — common in general English | - | - | — |
| 3930 | **impressed** | 2 | 280.36 | 8.089058 | 🔵 low — common in general English | - | - | — |
| 3931 | **composed** | 2 | 280.36 | 8.089058 | 🔵 low — common in general English | - | - | — |
| 3932 | **fulfilled** | 2 | 280.36 | 8.089058 | 🔵 low — common in general English | - | - | — |
| 3933 | **stretch** | 2 | 280.36 | 8.089058 | 🔵 low — common in general English | - | - | — |
| 3934 | **insignificant** | 2 | 280.36 | 8.089058 | 🔵 low — common in general English | - | - | — |
| 3935 | **attracting** | 2 | 280.36 | 8.089058 | 🔵 low — common in general English | - | - | ~ |
| 3936 | **saving** | 2 | 280.36 | 8.089058 | 🔵 low — common in general English | - | - | — |
| 3937 | **comfortably** | 2 | 280.36 | 8.089058 | 🔵 low — common in general English | - | - | — |
| 3938 | **eliminating** | 2 | 280.36 | 8.089058 | 🔵 low — common in general English | - | - | — |
| 3939 | **repaired** | 2 | 280.36 | 8.089058 | 🔵 low — common in general English | - | - | — |
| 3940 | **attempt** | 3 | 280.14 | 5.388443 | 🔵 low — common in general English | - | attempt, attempts | — |
| 3941 | **improve** | 3 | 279.37 | 5.373627 | 🔵 low — common in general English | - | - | — |
| 3942 | **considering** | 3 | 278.99 | 5.366301 | 🔵 low — common in general English | - | - | — |
| 3943 | **steering** | 2 | 276.71 | 7.983697 | 🔵 low — common in general English | - | - | — |
| 3944 | **absorbed** | 2 | 276.71 | 7.983697 | 🔵 low — common in general English | - | - | — |
| 3945 | **eighth** | 2 | 276.71 | 7.983697 | 🔵 low — common in general English | - | - | — |
| 3946 | **diminish** | 2 | 276.71 | 7.983697 | 🔵 low — common in general English | - | - | — |
| 3947 | **impression** | 2 | 276.71 | 7.983697 | 🔵 low — common in general English | - | - | — |
| 3948 | **pool** | 2 | 276.71 | 7.983697 | 🔵 low — common in general English | - | pool, pools | — |
| 3949 | **rare** | 2 | 276.71 | 7.983697 | 🔵 low — common in general English | - | - | — |
| 3950 | **sinking** | 2 | 276.71 | 7.983697 | 🔵 low — common in general English | - | - | — |
| 3951 | **ice** | 2 | 276.71 | 7.983697 | 🔵 low — common in general English | - | - | — |
| 3952 | **cook** | 2 | 276.71 | 7.983697 | 🔵 low — common in general English | 0.148465 | cook, cooks | — |
| 3953 | **lock** | 2 | 276.71 | 7.983697 | 🔵 low — common in general English | - | lock, locks | — |
| 3954 | **bitter** | 2 | 276.71 | 7.983697 | 🔵 low — common in general English | - | - | — |
| 3955 | **unhappy** | 2 | 276.71 | 7.983697 | 🔵 low — common in general English | - | - | — |
| 3956 | **consumed** | 2 | 276.71 | 7.983697 | 🔵 low — common in general English | - | - | — |
| 3957 | **examination** | 2 | 276.71 | 7.983697 | 🔵 low — common in general English | - | - | — |
| 3958 | **sank** | 2 | 276.71 | 7.983697 | 🔵 low — common in general English | - | - | — |
| 3959 | **school** | 2 | 276.71 | 7.983697 | 🔵 low — common in general English | - | - | — |
| 3960 | **positively** | 2 | 276.71 | 7.983697 | 🔵 low — common in general English | - | - | — |
| 3961 | **shape** | 2 | 276.71 | 7.983697 | 🔵 low — common in general English | - | shape, shapes | — |
| 3962 | **fixed** | 3 | 274.28 | 5.275647 | 🔵 low — common in general English | - | - | — |
| 3963 | **soar** | 2 | 273.41 | 7.888387 | 🔵 low — common in general English | - | soar, soars | — |
| 3964 | **safely** | 2 | 273.41 | 7.888387 | 🔵 low — common in general English | - | - | — |
| 3965 | **vowed** | 2 | 273.41 | 7.888387 | 🔵 low — common in general English | - | - | — |
| 3966 | **picked** | 2 | 273.41 | 7.888387 | 🔵 low — common in general English | - | - | — |
| 3967 | **survive** | 2 | 273.41 | 7.888387 | 🔵 low — common in general English | - | - | — |
| 3968 | **rolled** | 2 | 273.41 | 7.888387 | 🔵 low — common in general English | - | - | — |
| 3969 | **frequent** | 2 | 273.41 | 7.888387 | 🔵 low — common in general English | - | - | — |
| 3970 | **searching** | 2 | 273.41 | 7.888387 | 🔵 low — common in general English | - | - | — |
| 3971 | **sovereignty** | 2 | 273.41 | 7.888387 | 🔵 low — common in general English | - | - | — |
| 3972 | **bull** | 2 | 273.41 | 7.888387 | 🔵 low — common in general English | - | - | — |
| 3973 | **praised** | 2 | 273.41 | 7.888387 | 🔵 low — common in general English | - | - | — |
| 3974 | **exceptionally** | 2 | 273.41 | 7.888387 | 🔵 low — common in general English | - | - | — |
| 3975 | **changed** | 3 | 273.25 | 5.255844 | 🔵 low — common in general English | - | - | — |
| 3976 | **united** | 4 | 271.96 | 3.923254 | 🔵 low — common in general English | - | - | — |
| 3977 | **one-day** | 2 | 270.39 | 7.801376 | 🔵 low — common in general English | - | - | — |
| 3978 | **arguing** | 2 | 270.39 | 7.801376 | 🔵 low — common in general English | - | - | — |
| 3979 | **permanently** | 2 | 270.39 | 7.801376 | 🔵 low — common in general English | - | - | — |
| 3980 | **unnecessary** | 2 | 270.39 | 7.801376 | 🔵 low — common in general English | - | - | — |
| 3981 | **vein** | 2 | 270.39 | 7.801376 | 🔵 low — common in general English | - | vein, veins | — |
| 3982 | **stiff** | 2 | 270.39 | 7.801376 | 🔵 low — common in general English | - | - | — |
| 3983 | **capacity** | 3 | 269.96 | 5.192532 | 🔵 low — common in general English | - | capacities, capacity | — |
| 3984 | **provision** | 3 | 269.96 | 5.192532 | 🔵 low — common in general English | - | - | — |
| 3985 | **limited** | 3 | 267.77 | 5.150484 | 🔵 low — common in general English | - | - | — |
| 3986 | **worrying** | 2 | 267.62 | 7.721333 | 🔵 low — common in general English | - | - | — |
| 3987 | **collapsed** | 2 | 267.62 | 7.721333 | 🔵 low — common in general English | - | - | — |
| 3988 | **eagle** | 2 | 267.62 | 7.721333 | 🔵 low — common in general English | - | - | — |
| 3989 | **stepped** | 2 | 267.62 | 7.721333 | 🔵 low — common in general English | - | - | — |
| 3990 | **pill** | 2 | 267.62 | 7.721333 | 🔵 low — common in general English | - | - | — |
| 3991 | **flying** | 2 | 267.62 | 7.721333 | 🔵 low — common in general English | - | - | — |
| 3992 | **sticking** | 2 | 267.62 | 7.721333 | 🔵 low — common in general English | - | - | — |
| 3993 | **installed** | 2 | 267.62 | 7.721333 | 🔵 low — common in general English | - | - | — |
| 3994 | **steam** | 2 | 267.62 | 7.721333 | 🔵 low — common in general English | - | - | — |
| 3995 | **briefly** | 2 | 267.62 | 7.721333 | 🔵 low — common in general English | - | - | — |
| 3996 | **remaining** | 3 | 265.38 | 5.104499 | 🔵 low — common in general English | - | - | — |
| 3997 | **continuing** | 3 | 265.38 | 5.104499 | 🔵 low — common in general English | - | - | — |
| 3998 | **picking** | 2 | 265.05 | 7.647225 | 🔵 low — common in general English | - | - | — |
| 3999 | **pursuing** | 2 | 265.05 | 7.647225 | 🔵 low — common in general English | - | - | — |
| 4000 | **territory** | 2 | 265.05 | 7.647225 | 🔵 low — common in general English | - | - | — |
| 4001 | **strictly** | 2 | 265.05 | 7.647225 | 🔵 low — common in general English | - | - | — |
| 4002 | **approaching** | 2 | 265.05 | 7.647225 | 🔵 low — common in general English | - | - | — |
| 4003 | **postpone** | 2 | 265.05 | 7.647225 | 🔵 low — common in general English | - | - | — |
| 4004 | **dip** | 2 | 265.05 | 7.647225 | 🔵 low — common in general English | - | - | — |
| 4005 | **recognition** | 2 | 265.05 | 7.647225 | 🔵 low — common in general English | - | - | — |
| 4006 | **plunge** | 2 | 265.05 | 7.647225 | 🔵 low — common in general English | 0.231326 | - | — |
| 4007 | **compare** | 2 | 265.05 | 7.647225 | 🔵 low — common in general English | 0.065552 | - | — |
| 4008 | **wrote** | 2 | 265.05 | 7.647225 | 🔵 low — common in general English | - | - | — |
| 4009 | **cycle** | 2 | 262.66 | 7.578232 | 🔵 low — common in general English | - | cycle, cycles | — |
| 4010 | **sown** | 2 | 262.66 | 7.578232 | 🔵 low — common in general English | - | - | — |
| 4011 | **tend** | 2 | 262.66 | 7.578232 | 🔵 low — common in general English | - | - | — |
| 4012 | **pulp** | 2 | 262.66 | 7.578232 | 🔵 low — common in general English | - | - | — |
| 4013 | **treated** | 2 | 262.66 | 7.578232 | 🔵 low — common in general English | - | - | — |
| 4014 | **refrain** | 2 | 262.66 | 7.578232 | 🔵 low — common in general English | - | - | — |
| 4015 | **repaid** | 2 | 262.66 | 7.578232 | 🔵 low — common in general English | - | - | — |
| 4016 | **recognized** | 2 | 262.66 | 7.578232 | 🔵 low — common in general English | - | - | — |
| 4017 | **earning** | 2 | 260.42 | 7.513694 | 🔵 low — common in general English | - | - | — |
| 4018 | **engage** | 2 | 260.42 | 7.513694 | 🔵 low — common in general English | - | - | — |
| 4019 | **counsel** | 2 | 260.42 | 7.513694 | 🔵 low — common in general English | - | - | — |
| 4020 | **framework** | 2 | 260.42 | 7.513694 | 🔵 low — common in general English | - | - | — |
| 4021 | **science** | 2 | 260.42 | 7.513694 | 🔵 low — common in general English | - | - | — |
| 4022 | **fund** | 3 | 260.37 | 5.008168 | 🔵 low — common in general English | - | - | — |
| 4023 | **key** | 3 | 260.11 | 5.003079 | 🔵 low — common in general English | - | - | — |
| 4024 | **resort** | 2 | 258.32 | 7.453069 | 🔵 low — common in general English | - | - | — |
| 4025 | **passenger** | 2 | 258.32 | 7.453069 | 🔵 low — common in general English | - | - | — |
| 4026 | **latter** | 2 | 258.32 | 7.453069 | 🔵 low — common in general English | - | - | — |
| 4027 | **establishing** | 2 | 258.32 | 7.453069 | 🔵 low — common in general English | - | - | — |
| 4028 | **sudden** | 2 | 258.32 | 7.453069 | 🔵 low — common in general English | - | - | — |
| 4029 | **pat** | 2 | 258.32 | 7.453069 | 🔵 low — common in general English | - | - | — |
| 4030 | **payment** | 3 | 258.04 | 4.963272 | 🔵 low — common in general English | - | - | — |
| 4031 | **greatly** | 2 | 256.34 | 7.395911 | 🔵 low — common in general English | - | - | — |
| 4032 | **preparation** | 2 | 256.34 | 7.395911 | 🔵 low — common in general English | - | - | ~ |
| 4033 | **flowing** | 2 | 256.34 | 7.395911 | 🔵 low — common in general English | - | - | — |
| 4034 | **creditor** | 2 | 256.34 | 7.395911 | 🔵 low — common in general English | - | creditor, creditors | — |
| 4035 | **due** | 4 | 256.30 | 3.697356 | 🔵 low — common in general English | - | - | — |
| 4036 | **afford** | 2 | 254.47 | 7.341843 | 🔵 low — common in general English | - | - | — |
| 4037 | **pretty** | 2 | 254.47 | 7.341843 | 🔵 low — common in general English | - | - | — |
| 4038 | **climb** | 2 | 254.47 | 7.341843 | 🔵 low — common in general English | - | - | — |
| 4039 | **injured** | 2 | 254.47 | 7.341843 | 🔵 low — common in general English | - | - | — |
| 4040 | **population** | 2 | 252.69 | 7.29055 | 🔵 low — common in general English | - | - | — |
| 4041 | **shared** | 2 | 252.69 | 7.29055 | 🔵 low — common in general English | - | - | — |
| 4042 | **competitor** | 2 | 252.69 | 7.29055 | 🔵 low — common in general English | - | - | — |
| 4043 | **violating** | 2 | 252.69 | 7.29055 | 🔵 low — common in general English | - | - | — |
| 4044 | **bridge** | 2 | 252.69 | 7.29055 | 🔵 low — common in general English | - | - | — |
| 4045 | **referred** | 2 | 252.69 | 7.29055 | 🔵 low — common in general English | - | - | — |
| 4046 | **joining** | 2 | 252.69 | 7.29055 | 🔵 low — common in general English | - | - | ~ |
| 4047 | **renew** | 2 | 252.69 | 7.29055 | 🔵 low — common in general English | - | - | — |
| 4048 | **escort** | 2 | 251.00 | 7.24176 | 🔵 low — common in general English | - | - | — |
| 4049 | **restored** | 2 | 251.00 | 7.24176 | 🔵 low — common in general English | - | - | — |
| 4050 | **sustain** | 2 | 251.00 | 7.24176 | 🔵 low — common in general English | 0.231673 | - | — |
| 4051 | **obviously** | 2 | 249.38 | 7.19524 | 🔵 low — common in general English | - | - | — |
| 4052 | **troubled** | 2 | 249.38 | 7.19524 | 🔵 low — common in general English | - | - | — |
| 4053 | **argued** | 2 | 249.38 | 7.19524 | 🔵 low — common in general English | - | - | — |
| 4054 | **attract** | 2 | 249.38 | 7.19524 | 🔵 low — common in general English | - | attract, attracts | — |
| 4055 | **exception** | 2 | 249.38 | 7.19524 | 🔵 low — common in general English | - | - | — |
| 4056 | **consulting** | 2 | 249.38 | 7.19524 | 🔵 low — common in general English | - | - | — |
| 4057 | **chief** | 3 | 247.93 | 4.768829 | 🔵 low — common in general English | - | chief, chiefs | — |
| 4058 | **blocked** | 2 | 247.84 | 7.150788 | 🔵 low — common in general English | - | - | — |
| 4059 | **maybe** | 2 | 247.84 | 7.150788 | 🔵 low — common in general English | - | - | — |
| 4060 | **quarter** | 4 | 247.53 | 3.570899 | 🔵 low — common in general English | - | quarter, quarters | — |
| 4061 | **wet** | 2 | 246.37 | 7.108229 | 🔵 low — common in general English | - | - | — |
| 4062 | **dependent** | 2 | 246.37 | 7.108229 | 🔵 low — common in general English | - | - | — |
| 4063 | **usual** | 2 | 244.95 | 7.067407 | 🔵 low — common in general English | - | - | — |
| 4064 | **jump** | 2 | 244.95 | 7.067407 | 🔵 low — common in general English | 0.231663 | - | — |
| 4065 | **struck** | 2 | 244.95 | 7.067407 | 🔵 low — common in general English | - | - | — |
| 4066 | **transferred** | 2 | 244.95 | 7.067407 | 🔵 low — common in general English | - | - | — |
| 4067 | **stem** | 2 | 244.95 | 7.067407 | 🔵 low — common in general English | - | - | — |
| 4068 | **back** | 3 | 243.91 | 4.691571 | 🔵 low — common in general English | 0.136707 | - | — |
| 4069 | **underground** | 2 | 243.59 | 7.028186 | 🔵 low — common in general English | - | - | — |
| 4070 | **paid** | 3 | 242.58 | 4.665882 | 🔵 low — common in general English | - | - | — |
| 4071 | **pattern** | 2 | 242.29 | 6.990446 | 🔵 low — common in general English | - | - | — |
| 4072 | **tension** | 2 | 242.29 | 6.990446 | 🔵 low — common in general English | - | - | — |
| 4073 | **attracted** | 2 | 242.29 | 6.990446 | 🔵 low — common in general English | - | - | — |
| 4074 | **fifth** | 2 | 242.29 | 6.990446 | 🔵 low — common in general English | - | - | — |
| 4075 | **club** | 2 | 242.29 | 6.990446 | 🔵 low — common in general English | - | - | — |
| 4076 | **react** | 2 | 242.29 | 6.990446 | 🔵 low — common in general English | - | - | — |
| 4077 | **neutral** | 2 | 242.29 | 6.990446 | 🔵 low — common in general English | - | - | — |
| 4078 | **steep** | 2 | 242.29 | 6.990446 | 🔵 low — common in general English | - | - | — |
| 4079 | **added** | 4 | 241.42 | 3.482777 | 🔵 low — common in general English | - | - | — |
| 4080 | **dropping** | 2 | 241.03 | 6.954078 | 🔵 low — common in general English | - | dropping, droppings | — |
| 4081 | **product** | 3 | 240.54 | 4.6268 | 🔵 low — common in general English | - | - | — |
| 4082 | **additional** | 3 | 240.00 | 4.616401 | 🔵 low — common in general English | - | - | — |
| 4083 | **badly** | 2 | 239.81 | 6.918987 | 🔵 low — common in general English | - | - | — |
| 4084 | **heating** | 2 | 239.81 | 6.918987 | 🔵 low — common in general English | - | - | — |
| 4085 | **calm** | 2 | 239.81 | 6.918987 | 🔵 low — common in general English | - | - | ~ |
| 4086 | **approached** | 2 | 239.81 | 6.918987 | 🔵 low — common in general English | - | - | — |
| 4087 | **safety** | 2 | 239.81 | 6.918987 | 🔵 low — common in general English | - | - | — |
| 4088 | **address** | 2 | 239.81 | 6.918987 | 🔵 low — common in general English | - | - | — |
| 4089 | **promised** | 2 | 239.81 | 6.918987 | 🔵 low — common in general English | - | - | — |
| 4090 | **late** | 3 | 238.76 | 4.59255 | 🔵 low — common in general English | - | - | — |
| 4091 | **tire** | 2 | 238.63 | 6.885085 | 🔵 low — common in general English | - | - | — |
| 4092 | **preparing** | 2 | 238.63 | 6.885085 | 🔵 low — common in general English | - | - | — |
| 4093 | **appointed** | 2 | 238.63 | 6.885085 | 🔵 low — common in general English | - | - | — |
| 4094 | **treatment** | 2 | 235.33 | 6.789775 | 🔵 low — common in general English | - | treatment, treatments | — |
| 4095 | **pushing** | 2 | 235.33 | 6.789775 | 🔵 low — common in general English | - | - | — |
| 4096 | **acceptable** | 2 | 235.33 | 6.789775 | 🔵 low — common in general English | - | - | — |
| 4097 | **maintaining** | 2 | 235.33 | 6.789775 | 🔵 low — common in general English | - | - | — |
| 4098 | **last** | 5 | 235.10 | 2.713265 | 🔵 low — common in general English | 0.181530 | - | — |
| 4099 | **priority** | 2 | 234.30 | 6.759922 | 🔵 low — common in general English | - | - | — |
| 4100 | **encouraged** | 2 | 234.30 | 6.759922 | 🔵 low — common in general English | - | - | — |
| 4101 | **balanced** | 2 | 233.29 | 6.730934 | 🔵 low — common in general English | - | - | — |
| 4102 | **tonight** | 2 | 233.29 | 6.730934 | 🔵 low — common in general English | - | - | — |
| 4103 | **announcing** | 2 | 232.32 | 6.702763 | 🔵 low — common in general English | - | - | — |
| 4104 | **marked** | 2 | 232.32 | 6.702763 | 🔵 low — common in general English | - | - | — |
| 4105 | **failing** | 2 | 231.37 | 6.675364 | 🔵 low — common in general English | - | - | — |
| 4106 | **bidding** | 2 | 231.37 | 6.675364 | 🔵 low — common in general English | - | - | — |
| 4107 | **occurred** | 2 | 231.37 | 6.675364 | 🔵 low — common in general English | - | - | — |
| 4108 | **settle** | 2 | 231.37 | 6.675364 | 🔵 low — common in general English | - | - | — |
| 4109 | **seemed** | 2 | 231.37 | 6.675364 | 🔵 low — common in general English | - | - | — |
| 4110 | **complex** | 2 | 231.37 | 6.675364 | 🔵 low — common in general English | - | - | — |
| 4111 | **prospect** | 2 | 229.54 | 6.622721 | 🔵 low — common in general English | - | prospect, prospects | — |
| 4112 | **indication** | 2 | 229.54 | 6.622721 | 🔵 low — common in general English | - | - | — |
| 4113 | **broke** | 2 | 229.54 | 6.622721 | 🔵 low — common in general English | - | - | — |
| 4114 | **conditioned** | 2 | 229.54 | 6.622721 | 🔵 low — common in general English | - | - | ✓ འདུས་བྱས |
| 4115 | **twice** | 2 | 228.66 | 6.597403 | 🔵 low — common in general English | - | - | — |
| 4116 | **outright** | 2 | 228.66 | 6.597403 | 🔵 low — common in general English | - | - | — |
| 4117 | **recommend** | 2 | 228.66 | 6.597403 | 🔵 low — common in general English | - | - | — |
| 4118 | **sufficient** | 2 | 228.66 | 6.597403 | 🔵 low — common in general English | - | - | — |
| 4119 | **measured** | 2 | 227.81 | 6.57271 | 🔵 low — common in general English | - | - | — |
| 4120 | **core** | 2 | 226.97 | 6.548613 | 🔵 low — common in general English | - | - | — |
| 4121 | **welcomed** | 2 | 226.97 | 6.548613 | 🔵 low — common in general English | - | - | — |
| 4122 | **comprising** | 2 | 226.16 | 6.525082 | 🔵 low — common in general English | - | - | — |
| 4123 | **headed** | 2 | 225.36 | 6.502093 | 🔵 low — common in general English | - | - | — |
| 4124 | **lifted** | 2 | 225.36 | 6.502093 | 🔵 low — common in general English | - | - | — |
| 4125 | **comparable** | 2 | 225.36 | 6.502093 | 🔵 low — common in general English | - | - | — |
| 4126 | **frozen** | 2 | 224.58 | 6.47962 | 🔵 low — common in general English | - | - | — |
| 4127 | **involving** | 2 | 224.58 | 6.47962 | 🔵 low — common in general English | - | - | — |
| 4128 | **tight** | 2 | 223.82 | 6.457641 | 🔵 low — common in general English | - | - | — |
| 4129 | **supply** | 3 | 223.29 | 4.294818 | 🔵 low — common in general English | - | supplies, supply | — |
| 4130 | **contribute** | 2 | 223.07 | 6.436135 | 🔵 low — common in general English | - | - | — |
| 4131 | **room** | 2 | 223.07 | 6.436135 | 🔵 low — common in general English | - | - | — |
| 4132 | **faced** | 2 | 223.07 | 6.436135 | 🔵 low — common in general English | - | - | — |
| 4133 | **contained** | 2 | 223.07 | 6.436135 | 🔵 low — common in general English | - | - | — |
| 4134 | **flat** | 2 | 223.07 | 6.436135 | 🔵 low — common in general English | - | - | — |
| 4135 | **value** | 3 | 222.51 | 4.279929 | 🔵 low — common in general English | - | value, values | — |
| 4136 | **social** | 2 | 221.63 | 6.394462 | 🔵 low — common in general English | - | - | — |
| 4137 | **plan** | 3 | 221.37 | 4.258004 | 🔵 low — common in general English | - | - | — |
| 4138 | **depending** | 2 | 220.93 | 6.374259 | 🔵 low — common in general English | - | - | — |
| 4139 | **so-called** | 2 | 220.93 | 6.374259 | 🔵 low — common in general English | - | - | — |
| 4140 | **internal** | 2 | 220.24 | 6.354457 | 🔵 low — common in general English | - | - | — |
| 4141 | **rapid** | 2 | 220.24 | 6.354457 | 🔵 low — common in general English | - | - | — |
| 4142 | **proceed** | 2 | 220.24 | 6.354457 | 🔵 low — common in general English | - | - | — |
| 4143 | **likely** | 3 | 219.40 | 4.220174 | 🔵 low — common in general English | - | - | — |
| 4144 | **evidence** | 2 | 218.91 | 6.31599 | 🔵 low — common in general English | - | - | — |
| 4145 | **normally** | 2 | 217.63 | 6.278949 | 🔵 low — common in general English | - | - | — |
| 4146 | **competitiveness** | 2 | 217.00 | 6.260931 | 🔵 low — common in general English | - | - | — |
| 4147 | **decrease** | 2 | 217.00 | 6.260931 | 🔵 low — common in general English | - | - | — |
| 4148 | **structure** | 2 | 216.39 | 6.243231 | 🔵 low — common in general English | - | - | — |
| 4149 | **double** | 2 | 215.79 | 6.225839 | 🔵 low — common in general English | - | - | — |
| 4150 | **brown** | 2 | 215.79 | 6.225839 | 🔵 low — common in general English | - | - | — |
| 4151 | **retain** | 2 | 215.19 | 6.208745 | 🔵 low — common in general English | - | - | — |
| 4152 | **partner** | 2 | 214.61 | 6.191938 | 🔵 low — common in general English | - | - | — |
| 4153 | **fallen** | 2 | 214.04 | 6.175409 | 🔵 low — common in general English | - | - | — |
| 4154 | **participation** | 2 | 214.04 | 6.175409 | 🔵 low — common in general English | - | - | — |
| 4155 | **advanced** | 2 | 213.47 | 6.159148 | 🔵 low — common in general English | - | - | — |
| 4156 | **ruled** | 2 | 211.84 | 6.111895 | 🔵 low — common in general English | - | - | — |
| 4157 | **primarily** | 2 | 211.84 | 6.111895 | 🔵 low — common in general English | - | - | — |
| 4158 | **suit** | 2 | 211.84 | 6.111895 | 🔵 low — common in general English | - | - | — |
| 4159 | **loss** | 4 | 211.57 | 3.052105 | 🔵 low — common in general English | 0.231648 | - | — |
| 4160 | **staff** | 2 | 210.79 | 6.08159 | 🔵 low — common in general English | - | staff, staffs | — |
| 4161 | **depressed** | 2 | 209.27 | 6.037787 | 🔵 low — common in general English | - | - | — |
| 4162 | **threatened** | 2 | 209.27 | 6.037787 | 🔵 low — common in general English | - | - | — |
| 4163 | **strongly** | 2 | 209.27 | 6.037787 | 🔵 low — common in general English | - | - | — |
| 4164 | **stake** | 3 | 209.25 | 4.024791 | 🔵 low — common in general English | - | - | — |
| 4165 | **push** | 2 | 207.81 | 5.995823 | 🔵 low — common in general English | 0.181948 | - | — |
| 4166 | **discussed** | 2 | 207.34 | 5.982217 | 🔵 low — common in general English | - | - | — |
| 4167 | **pound** | 2 | 206.42 | 5.955549 | 🔵 low — common in general English | - | - | — |
| 4168 | **vegetable** | 2 | 206.42 | 5.955549 | 🔵 low — common in general English | - | vegetable, vegetables | — |
| 4169 | **larger** | 2 | 205.52 | 5.929574 | 🔵 low — common in general English | - | - | — |
| 4170 | **copper** | 2 | 205.52 | 5.929574 | 🔵 low — common in general English | - | - | ~ |
| 4171 | **smaller** | 2 | 205.08 | 5.916835 | 🔵 low — common in general English | - | - | — |
| 4172 | **asset** | 2 | 204.64 | 5.904256 | 🔵 low — common in general English | - | asset, assets | — |
| 4173 | **grew** | 2 | 204.21 | 5.891833 | 🔵 low — common in general English | - | - | — |
| 4174 | **release** | 2 | 202.13 | 5.831935 | 🔵 low — common in general English | - | - | — |
| 4175 | **forward** | 2 | 202.13 | 5.831935 | 🔵 low — common in general English | - | - | — |
| 4176 | **strategy** | 2 | 201.34 | 5.808946 | 🔵 low — common in general English | - | strategies, strategy | — |
| 4177 | **buy** | 3 | 195.62 | 3.76272 | 🔵 low — common in general English | - | - | — |
| 4178 | **helped** | 2 | 195.21 | 5.632322 | 🔵 low — common in general English | - | - | — |
| 4179 | **primary** | 2 | 193.60 | 5.585802 | 🔵 low — common in general English | - | - | — |
| 4180 | **majority** | 2 | 190.88 | 5.507159 | 🔵 low — common in general English | - | - | — |
| 4181 | **combined** | 2 | 190.01 | 5.482261 | 🔵 low — common in general English | - | - | — |
| 4182 | **paper** | 2 | 189.17 | 5.457969 | 🔵 low — common in general English | - | - | — |
| 4183 | **outlook** | 2 | 188.62 | 5.442095 | 🔵 low — common in general English | - | - | — |
| 4184 | **southern** | 2 | 187.81 | 5.418748 | 🔵 low — common in general English | - | - | — |
| 4185 | **existing** | 2 | 186.25 | 5.373627 | 🔵 low — common in general English | - | - | — |
| 4186 | **aimed** | 2 | 185.74 | 5.359029 | 🔵 low — common in general English | - | - | — |
| 4187 | **unlikely** | 2 | 185.49 | 5.351808 | 🔵 low — common in general English | - | - | — |
| 4188 | **affected** | 2 | 185.24 | 5.34464 | 🔵 low — common in general English | - | - | — |
| 4189 | **discuss** | 2 | 185.00 | 5.337522 | 🔵 low — common in general English | - | - | — |
| 4190 | **dropped** | 2 | 185.00 | 5.337522 | 🔵 low — common in general English | - | - | — |
| 4191 | **court** | 2 | 185.00 | 5.337522 | 🔵 low — common in general English | - | - | — |
| 4192 | **spending** | 2 | 183.55 | 5.29585 | 🔵 low — common in general English | - | - | — |
| 4193 | **ahead** | 2 | 183.08 | 5.282336 | 🔵 low — common in general English | - | - | — |
| 4194 | **current** | 3 | 179.81 | 3.458653 | 🔵 low — common in general English | - | - | — |
| 4195 | **mainly** | 2 | 179.13 | 5.168289 | 🔵 low — common in general English | - | - | — |
| 4196 | **quoted** | 2 | 177.51 | 5.121496 | 🔵 low — common in general English | - | - | — |
| 4197 | **price** | 3 | 175.34 | 3.372545 | 🔵 low — common in general English | - | price, prices | — |
| 4198 | **crop** | 2 | 171.69 | 4.953564 | 🔵 low — common in general English | - | crop, crops | — |
| 4199 | **letter** | 2 | 171.19 | 4.939175 | 🔵 low — common in general English | - | letter, letters | — |
| 4200 | **area** | 2 | 170.54 | 4.920306 | 🔵 low — common in general English | - | area, areas | — |
| 4201 | **addition** | 2 | 169.58 | 4.892655 | 🔵 low — common in general English | - | - | — |
| 4202 | **fed** | 2 | 169.42 | 4.88812 | 🔵 low — common in general English | - | - | — |
| 4203 | **planned** | 2 | 168.95 | 4.874636 | 🔵 low — common in general English | - | - | — |
| 4204 | **accord** | 2 | 168.34 | 4.856937 | 🔵 low — common in general English | - | - | — |
| 4205 | **expect** | 2 | 167.59 | 4.835244 | 🔵 low — common in general English | - | - | — |
| 4206 | **group** | 3 | 166.26 | 3.197874 | 🔵 low — common in general English | - | - | — |
| 4207 | **audi** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 4208 | **ale** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 4209 | **leak** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 4210 | **trusting** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 4211 | **flavour** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 4212 | **digging** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 4213 | **incorrectly** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 4214 | **expedient** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - | - | ~ |
| 4215 | **medication** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 4216 | **comprehend** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 4217 | **make-up** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 4218 | **ensue** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 4219 | **flagrant** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 4220 | **autonomy** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 4221 | **preoccupied** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 4222 | **entailed** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 4223 | **westward** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 4224 | **fruitful** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 4225 | **coincidence** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 4226 | **circular** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 4227 | **fuse** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 4228 | **flare** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 4229 | **torrential** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 4230 | **wielding** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 4231 | **good-looking** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 4232 | **horror** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 4233 | **cemetery** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 4234 | **unsatisfied** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 4235 | **reconciled** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 4236 | **authoritative** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 4237 | **aging** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 4238 | **disenchanted** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 4239 | **brave** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 4240 | **recklessly** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 4241 | **demise** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 4242 | **enduring** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 4243 | **suffice** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 4244 | **unsurpassed** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 4245 | **constellation** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 4246 | **trident** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 4247 | **toss** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 4248 | **trench** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 4249 | **chewing** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 4250 | **snowy** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 4251 | **lastly** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 4252 | **sacrificed** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 4253 | **commanding** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 4254 | **rang** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 4255 | **orchard** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 4256 | **fever** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 4257 | **gigantic** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 4258 | **horde** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 4259 | **offload** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 4260 | **comprehension** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 4261 | **fas** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 4262 | **snare** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 4263 | **otter** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 4264 | **musk-oxen** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 4265 | **irrigated** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 4266 | **rightful** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 4267 | **propped** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 4268 | **imbalanced** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 4269 | **bedding** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 4270 | **daytime** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 4271 | **overtake** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 4272 | **colder** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 4273 | **lure** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 4274 | **kin** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 4275 | **punished** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 4276 | **engulfed** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 4277 | **overwhelm** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 4278 | **oceanic** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 4279 | **transported** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 4280 | **inexorable** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 4281 | **mooring** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 4282 | **lymph** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 4283 | **prolific** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 4284 | **shocked** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 4285 | **disdain** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 4286 | **overpowering** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 4287 | **seizure** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 4288 | **knuckle** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 4289 | **shin** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 4290 | **indulge** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 4291 | **ethic** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 4292 | **daylight** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 4293 | **unsightly** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 4294 | **congregation** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 4295 | **summed** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 4296 | **commentator** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 4297 | **receiver** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 4298 | **differently** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 4299 | **destiny** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 4300 | **loot** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 4301 | **falsely** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 4302 | **accusation** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 4303 | **recalcitrant** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 4304 | **grim** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 4305 | **oblige** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 4306 | **seamless** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 4307 | **plucked** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 4308 | **squarely** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 4309 | **noticed** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 4310 | **finer** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 4311 | **ingenuity** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 4312 | **prohibition** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 4313 | **conformity** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 4314 | **purest** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 4315 | **blaze** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | 0.066366 | - | — |
| 4316 | **incomprehensible** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 4317 | **enquire** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 4318 | **conveyance** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 4319 | **tread** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 4320 | **sation** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 4321 | **smoothly** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 4322 | **respecting** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 4323 | **reproduce** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 4324 | **lethargy** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 4325 | **avenue** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 4326 | **makin** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 4327 | **harden** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 4328 | **debating** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 4329 | **appropriated** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 4330 | **demolished** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 4331 | **thrashing** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 4332 | **reprimanded** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 4333 | **calmed** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 4334 | **crowned** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 4335 | **commonplace** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 4336 | **distinct** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 4337 | **nightmare** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 4338 | **ransom** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 4339 | **cognizant** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 4340 | **unquestionably** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 4341 | **sym** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 4342 | **intensely** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 4343 | **straightforward** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 4344 | **watchdog** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 4345 | **imprisoned** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 4346 | **punishment** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 4347 | **invading** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 4348 | **inflict** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 4349 | **afflicted** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 4350 | **rider** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 4351 | **intimidation** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 4352 | **contravention** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 4353 | **predator** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 4354 | **outraged** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 4355 | **shedding** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 4356 | **tolerance** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 4357 | **tenderness** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 4358 | **flourish** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 4359 | **lasted** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 4360 | **dissuade** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 4361 | **jugular** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 4362 | **mini** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 4363 | **greed** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 4364 | **flee** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 4365 | **vicinity** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 4366 | **overwhelmed** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 4367 | **reappeared** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 4368 | **boasting** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 4369 | **sucked** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 4370 | **futility** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 4371 | **wealthier** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 4372 | **dwindle** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 4373 | **fare** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 4374 | **aberration** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 4375 | **mirage** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 4376 | **omitting** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 4377 | **summarized** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 4378 | **thirty-five** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 4379 | **instantly** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 4380 | **colossal** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 4381 | **transparent** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 4382 | **simplicity** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 4383 | **chatting** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 4384 | **smoking** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 4385 | **lowland** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 4386 | **abusing** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 4387 | **subtle** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 4388 | **occasional** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 4389 | **infested** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 4390 | **diseased** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 4391 | **smashing** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 4392 | **adult** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 4393 | **ration** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 4394 | **coral** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 4395 | **ordinarily** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 4396 | **ready-made** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 4397 | **subcontinent** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 4398 | **bountiful** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 4399 | **commentary** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 4400 | **impossibility** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 4401 | **amazed** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 4402 | **amazing** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 4403 | **resigning** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 4404 | **dispelled** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 4405 | **foodstuff** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 4406 | **rendered** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 4407 | **placated** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 4408 | **subduing** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 4409 | **scrape** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 4410 | **severity** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 4411 | **intel** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 4412 | **exile** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 4413 | **infinitesimal** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 4414 | **bloom** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 4415 | **supposedly** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 4416 | **knowingly** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 4417 | **demonstration** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 4418 | **cleansing** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 4419 | **spilt** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 4420 | **reassured** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 4421 | **predominate** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 4422 | **quelling** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 4423 | **misconception** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 4424 | **propagated** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 4425 | **bore** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 4426 | **negligence** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 4427 | **astonished** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 4428 | **proceeded** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 4429 | **vanished** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 4430 | **uncontrolled** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 4431 | **equality** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - | - | ✓ མཉམ་པ་ཉིད |
| 4432 | **fabrication** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 4433 | **translating** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 4434 | **traced** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 4435 | **obstinate** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 4436 | **unfabricated** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 4437 | **accustomed** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 4438 | **impediment** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 4439 | **forcefully** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 4440 | **brush** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 4441 | **prematurely** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 4442 | **skylight** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 4443 | **inserting** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 4444 | **winnowed** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 4445 | **irrigate** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 4446 | **fertile** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 4447 | **invented** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 4448 | **vine** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 4449 | **azure** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English | - | - | — |
| 4450 | **beamed** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4451 | **elucidated** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4452 | **wonderfully** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4453 | **concerns-such** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4454 | **whatever-i** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4455 | **circumambulation** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | ✓ སྐོར་བ |
| 4456 | **mantra-even** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4457 | **mani-it** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4458 | **torch** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4459 | **akani** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4460 | **tha** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4461 | **unexcelled** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4462 | **lotus-light** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4463 | **divinity** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4464 | **ever-revolving** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4465 | **buddha-nature** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4466 | **adventitious** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4467 | **entranced** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4468 | **tice** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4469 | **teaching-which** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4470 | **reasoning** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4471 | **proudly** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4472 | **minutely** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4473 | **leapt** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4474 | **moth** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4475 | **lamp-flame** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4476 | **carnivorous** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4477 | **seduced** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4478 | **bait** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4479 | **gyalse** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | ~ |
| 4480 | **mru** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4481 | **riverbed** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4482 | **indispensable-remembering** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4483 | **rat** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4484 | **dremo** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4485 | **marmot** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4486 | **sleepy** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4487 | **weren** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4488 | **string** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4489 | **loosely** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4490 | **elegant** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4491 | **meaning-you** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4492 | **debase** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4493 | **everything-the** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4494 | **teachings-properly** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4495 | **disheart** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4496 | **ened** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4497 | **elementary** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4498 | **prescribe** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4499 | **dharma-that** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4500 | **practice-i** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4501 | **death-bed** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4502 | **helplessly** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4503 | **perilous** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4504 | **libera** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4505 | **shallow-tongued** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4506 | **sneer** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4507 | **mal** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4508 | **joyfully** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4509 | **swathed** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4510 | **turban** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4511 | **ataka** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4512 | **dignified** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4513 | **oppor** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4514 | **tunity** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4515 | **khatha** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4516 | **outlying** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4517 | **attune** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4518 | **forefather** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4519 | **aspiring** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4520 | **liyana** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4521 | **atten** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4522 | **dant** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4523 | **oll** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4524 | **dysfunction** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4525 | **unheard** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4526 | **animal-even** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4527 | **prized** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4528 | **padme** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4529 | **heap-wherea** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4530 | **conceive** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4531 | **pratimoksa** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4532 | **dharma-the** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4533 | **buddha-exist** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4534 | **sparsely** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4535 | **whjch** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4536 | **script** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4537 | **intro** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4538 | **duced** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4539 | **mikyo** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4540 | **rasa** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4541 | **trulnang** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4542 | **estab** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4543 | **lished** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4544 | **kingtrisong** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4545 | **mantra-holder** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4546 | **sustra** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4547 | **dharma-for** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4548 | **queror** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4549 | **preached** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4550 | **extant** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4551 | **ahhough** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4552 | **destroyer-of-samsara** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | ✓ འཁོར་བ་འཇིག |
| 4553 | **incalculably** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4554 | **infinite-aspiration** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4555 | **alternation** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4556 | **promulgated** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4557 | **once-come-king** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | ✓ སྔོན་བྱུང་གི་རྒྱལ་པོ |
| 4558 | **trayana** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4559 | **uncompounded** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4560 | **interpreter** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4561 | **kham** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4562 | **degenerations-those** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4563 | **it-just** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4564 | **transmi** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4565 | **infiltrate** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4566 | **condense** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | 0.049148 | - | — |
| 4567 | **important-the** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4568 | **canonical** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4569 | **commentar** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4570 | **ies** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4571 | **practice-even** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4572 | **triptaka** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4573 | **metaphysic** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4574 | **piety** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4575 | **illustrate** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4576 | **condi** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4577 | **endowed** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4578 | **enslavement** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4579 | **hypocritical** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4580 | **intrusive** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4581 | **depravity** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4582 | **heedlessness** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4583 | **poisons-that** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4584 | **dominat** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4585 | **plishing** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4586 | **perverted** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4587 | **lazy** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4588 | **indolence** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4589 | **life-that** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4590 | **impostor** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4591 | **pretence** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4592 | **humanity** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4593 | **depraved** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4594 | **suffedng** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4595 | **sarilsa** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4596 | **plishment** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4597 | **snuff** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4598 | **chieftain** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4599 | **worth-each** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4600 | **thirty-four** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4601 | **squander** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4602 | **mter** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4603 | **realiza** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4604 | **goal-the** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4605 | **dharma-i** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4606 | **junction** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4607 | **interconnected** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4608 | **elements-the** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4609 | **flint** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4610 | **rarer** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4611 | **advan** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4612 | **tage** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4613 | **perchance** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4614 | **adrift** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4615 | **shoreless** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4616 | **needle-which** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4617 | **saddened** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4618 | **fritter** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4619 | **jettison** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4620 | **trakpa** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | ~ |
| 4621 | **resourcefulness** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4622 | **raft** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4623 | **thing-the** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4624 | **preme** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4625 | **dharma-and** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4626 | **ineffectual** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4627 | **folly** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4628 | **betray** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4629 | **turning-point** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4630 | **bewildered** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4631 | **miyowa** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4632 | **fashioned** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4633 | **god-realm** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4634 | **fruit-bearing** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4635 | **manasarovar** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4636 | **sea-water** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4637 | **ear-shot** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4638 | **snow-covered** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4639 | **sub-continent** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4640 | **rim** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4641 | **engulf** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4642 | **conflagration** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4643 | **raincloud** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4644 | **devastation** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4645 | **sincerely-if** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4646 | **realm-even** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4647 | **gods-who** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4648 | **flicker** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4649 | **slumber** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4650 | **ever-present** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4651 | **status-until** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4652 | **gnashing** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4653 | **fang** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4654 | **charm** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4655 | **athlete** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4656 | **fleetness-none** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4657 | **impene** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4658 | **trable** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4659 | **concealment** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4660 | **glaze** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4661 | **willy-nilly** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4662 | **defender** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4663 | **you-can** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4664 | **dispensation** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4665 | **miracu** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4666 | **lous** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4667 | **ofyerpa** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4668 | **zur** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | ~ |
| 4669 | **nub** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | ~ |
| 4670 | **clan** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4671 | **plished** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4672 | **space-they** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4673 | **silence** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4674 | **nyeshangkatya** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4675 | **motionless** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4676 | **volley** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4677 | **cliff-but** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4678 | **firewood** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4679 | **contraption** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4680 | **depends-and** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4681 | **scarecrow** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4682 | **momerit** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4683 | **illustrious** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4684 | **stature** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4685 | **earshot** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4686 | **resplendence** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4687 | **outshine** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4688 | **mahdvara** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4689 | **evade** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4690 | **consolation** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4691 | **mahasammata** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4692 | **pala** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4693 | **candra** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4694 | **nivara** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4695 | **tavi** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4696 | **kambhin** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4697 | **earthly** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4698 | **lek** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4699 | **jambu** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4700 | **dvipa** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4701 | **ralpachen** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4702 | **gesar** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4703 | **tajikistan** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4704 | **ambassa** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4705 | **dor** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4706 | **beehive** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4707 | **race** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4708 | **abstinence** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4709 | **summertime** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4710 | **meadow** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4711 | **lush** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4712 | **bask** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4713 | **scarlet** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4714 | **grassland** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4715 | **hue** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4716 | **brittle** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4717 | **glacial** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4718 | **scour** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4719 | **helpless** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4720 | **grandparent** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4721 | **great-grandparent** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4722 | **eminent** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4723 | **year-or** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4724 | **animals-sheep** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4725 | **dogs-how** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4726 | **animate** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4727 | **mind-everything** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4728 | **exalted** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4729 | **rainbow-but** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4730 | **stiffly** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4731 | **armpit** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4732 | **cherished** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4733 | **thread** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4734 | **beloved** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4735 | **handsome** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4736 | **distinguished** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4737 | **horribly** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4738 | **livid** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4739 | **here-our** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4740 | **trussed** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4741 | **curtain** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4742 | **sheepskin** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4743 | **rug** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4744 | **tuft** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4745 | **bespattered** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4746 | **cremating** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4747 | **vagabond** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4748 | **enjoy-teacher** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4749 | **protege** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4750 | **comrade** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4751 | **wives-there** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4752 | **three-storeyed** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4753 | **emanated** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4754 | **rivalled** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4755 | **kagyupa** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | ✓ བཀའ་བརྒྱུད་པ |
| 4756 | **wield** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4757 | **governments-not** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4758 | **languishing** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4759 | **alms-round** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4760 | **sworn** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4761 | **intimately** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4762 | **paltry** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4763 | **insignifi** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4764 | **cant** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4765 | **deprivation** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4766 | **well-off** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4767 | **merry** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4768 | **nightfall** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4769 | **unparalleled** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4770 | **aparantaka** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4771 | **more-and** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4772 | **ever-changing** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4773 | **mediocrity** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4774 | **eloquent** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4775 | **despis** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4776 | **liar** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4777 | **common-sense** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4778 | **trusted** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4779 | **esteemed** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4780 | **busily** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4781 | **tricked** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4782 | **conscientious** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4783 | **stantly** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4784 | **poignant** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4785 | **transitoriness** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4786 | **feud** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4787 | **gelong** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4788 | **pigeon** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4789 | **exterminate** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4790 | **commander** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4791 | **superficial** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4792 | **beasts-all** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4793 | **lifesustaining** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4794 | **fatality** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4795 | **eating-the** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4796 | **oblivious** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4797 | **mear** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4798 | **unhealthy** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4799 | **tumour** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4800 | **disorder** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4801 | **dropsy** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4802 | **incite** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4803 | **decrepit** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4804 | **linger** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4805 | **glued** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4806 | **candle-flame** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4807 | **celebrity** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4808 | **sorrowful** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4809 | **escaping** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4810 | **bhik** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4811 | **ractice** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4812 | **sameness** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4813 | **insatiable** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4814 | **ha-ha** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4815 | **proudest** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4816 | **engross** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4817 | **revel** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4818 | **abhorrent** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4819 | **sealing** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4820 | **vaster** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4821 | **twinkling** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4822 | **headlong** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4823 | **scorching** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4824 | **perimeter** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4825 | **white-hot** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4826 | **smith-there** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4827 | **searingly** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4828 | **incandescent** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4829 | **snowflake** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4830 | **furiously** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4831 | **weapons-a** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4832 | **armoury** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4833 | **fifty** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4834 | **firebrand** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4835 | **cross-rule** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4836 | **on-which** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4837 | **hacked** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4838 | **whirling** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4839 | **ram** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4840 | **butt** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4841 | **horn-tip** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4842 | **spewing** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4843 | **scream** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4844 | **shove** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4845 | **howl** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4846 | **cauldron** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4847 | **impale** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4848 | **heel** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4849 | **edifice** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4850 | **bellow** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4851 | **leopard-skin** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4852 | **indi** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4853 | **tinguishable** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4854 | **razor-edged** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4855 | **directions-the** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4856 | **northeast-stand** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4857 | **purged** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4858 | **shady** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4859 | **putrescent** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4860 | **brazier** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4861 | **corpses-corps** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4862 | **dogs-all** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4863 | **decomposing** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4864 | **decompose** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4865 | **foulest** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4866 | **stench** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4867 | **mire** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4868 | **thrilled** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4869 | **slender** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4870 | **heal** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4871 | **it-only** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4872 | **excruciatingly** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4873 | **reconstitute** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4874 | **eagerly** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4875 | **stabbing** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4876 | **metallic** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4877 | **unshake** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4878 | **glacier** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4879 | **perpetually** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4880 | **enveloped** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4881 | **lamentation** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4882 | **ofutpala-like** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4883 | **petal-like** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4884 | **unbearably** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4885 | **broom** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4886 | **yutso** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4887 | **ngonmo** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4888 | **snpo** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4889 | **kangchen** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4890 | **zemaguru** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4891 | **exclaiming** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4892 | **misused** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4893 | **spanned** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4894 | **squirming** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4895 | **tsangla** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4896 | **tanakchen** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4897 | **angtong** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4898 | **exercis** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4899 | **gullet** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4900 | **kidney** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4901 | **shawl** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4902 | **munch** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4903 | **leisurely** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4904 | **steaming** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4905 | **whisker** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4906 | **reddish** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4907 | **tinge** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4908 | **palden** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4909 | **chokyong** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4910 | **ngor** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4911 | **ngulda** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4912 | **tree-trunk** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4913 | **aher** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4914 | **pogye** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4915 | **all-powerful** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4916 | **dignitary** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4917 | **srm** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4918 | **adulterer** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4919 | **infidelity** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4920 | **lunch-hour** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4921 | **obdurate** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4922 | **impulsively** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4923 | **exhausted-only** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4924 | **stony** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4925 | **torture** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | 0.231483 | - | — |
| 4926 | **sroi** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4927 | **sombre** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4928 | **horse-hair** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4929 | **if-finally-enough** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4930 | **grass-like** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4931 | **devouring** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4932 | **exquisitely** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4933 | **bedecked** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4934 | **ravishing** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4935 | **srol** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4936 | **daughter-in** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4937 | **shaven-skulled** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4938 | **proposition** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4939 | **bald-head** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4940 | **ablution** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4941 | **squashed** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4942 | **jostling** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4943 | **thing-except** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4944 | **shindre** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4945 | **jungpo** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | ✓ འབྱུང་པོ |
| 4946 | **theurang** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | ✓ ཐེའུ་རང |
| 4947 | **relive** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4948 | **insanity** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4949 | **teem** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4950 | **reptile** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4951 | **shellfish** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4952 | **beer-barrel** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4953 | **burrow** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4954 | **torturing** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4955 | **devices-net** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4956 | **oyster** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4957 | **ass** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4958 | **domesticated** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4959 | **executioner** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4960 | **stare** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4961 | **pierced** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4962 | **yoked** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4963 | **continual** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4964 | **pelted** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4965 | **long-lasting** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4966 | **lated** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4967 | **scorning** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4968 | **old-age** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4969 | **hated** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4970 | **wracked** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4971 | **spasm** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4972 | **parasite** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4973 | **news-and** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4974 | **imme** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4975 | **diately** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4976 | **constancy** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4977 | **celebration** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4978 | **concoction** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4979 | **six-brick** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4980 | **dotok** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4981 | **dzo** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4982 | **perforated** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4983 | **chafed** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4984 | **lambskin** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4985 | **flea** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4986 | **tick** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4987 | **decapitated** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4988 | **die-they** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4989 | **incessantly** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4990 | **aquatic** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4991 | **threshing** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4992 | **untainted** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | ~ |
| 4993 | **suckle** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4994 | **tethered** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4995 | **paus** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4996 | **milk-their** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4997 | **drink-can** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4998 | **starved** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 4999 | **skeleton-like** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5000 | **stagger** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5001 | **constituting** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5002 | **happiness-food** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5003 | **of-are** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5004 | **interpose** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5005 | **embryonic** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5006 | **jelly** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5007 | **viscous** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5008 | **ellipse** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5009 | **oblong** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5010 | **oval** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5011 | **appendage** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5012 | **sense-organ** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5013 | **suffocating** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5014 | **uterus** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5015 | **buffeted** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5016 | **cervix** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5017 | **pelvi** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5018 | **draw-plate** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5019 | **wrenched** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5020 | **ever-unfinished** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5021 | **eyesight** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5022 | **articulate** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5023 | **unintelligible** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5024 | **mumble** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5025 | **impa** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5026 | **tient** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5027 | **scorned** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5028 | **shrunk** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5029 | **dazed** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5030 | **trampled** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5031 | **waist** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5032 | **gingerly** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5033 | **arthritic** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5034 | **cheek-bone** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5035 | **dull-witted** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5036 | **giddy** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5037 | **brightness** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5038 | **humour** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5039 | **illnesses-those** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5040 | **bile** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | ✓ མཁྲིས་པ |
| 5041 | **on-arise** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5042 | **twinge** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5043 | **strike-however** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5044 | **radiantly** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5045 | **prime-we** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5046 | **crumple** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5047 | **bloodletting** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5048 | **cautery** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5049 | **morbid** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5050 | **epilepsy** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5051 | **short-tempered** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5052 | **foreboding** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5053 | **departure-you** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5054 | **menacing** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5055 | **hoarse** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5056 | **brigand** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5057 | **envied** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5058 | **devil** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5059 | **adage** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5060 | **compatriot** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5061 | **dangers-and** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5062 | **inescapably** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5063 | **through-but** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5064 | **wheedle** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5065 | **gods-a** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5066 | **malice** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5067 | **deign** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5068 | **swindler** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5069 | **tether** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5070 | **imperiously** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5071 | **monopolizing** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5072 | **sly** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5073 | **ravaging** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5074 | **incurable** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5075 | **lllead** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5076 | **dining** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5077 | **expend** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5078 | **enterpris** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5079 | **accomplished-and** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5080 | **dharmaless** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5081 | **whence** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5082 | **aren** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5083 | **nowa** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5084 | **decaying** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5085 | **everything-good** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5086 | **not-highly** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5087 | **appalled** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5088 | **pitiful** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5089 | **multiplicity** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5090 | **quarrelling** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5091 | **tree-whose** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5092 | **donning** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5093 | **weapons-vajra** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5094 | **taller** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5095 | **demi** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5096 | **dispatch** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5097 | **all-protector** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5098 | **crazed** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5099 | **fastened** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5100 | **exuberant** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | ~ |
| 5101 | **wore** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5102 | **perspired** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5103 | **sweetheart** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5104 | **powerlessness** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5105 | **birthplace** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5106 | **suffering-and** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5107 | **murderous** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5108 | **hell-fire** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5109 | **mindlessness** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5110 | **snow-mountain** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5111 | **she-monkey** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5112 | **pur** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5113 | **larika** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5114 | **pundarika** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5115 | **intimate** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5116 | **heartbroken** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5117 | **slighdy** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5118 | **extolled** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5119 | **sense-door** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5120 | **frighten** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5121 | **saligha** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5122 | **assembly-hall** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5123 | **balcony** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5124 | **overlooking** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5125 | **preoccupations-parent** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5126 | **possessions-like** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5127 | **mist** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5128 | **esteem** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5129 | **worm-fodder** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5130 | **watch-tower** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5131 | **gloomy-face** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5132 | **cheery** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5133 | **all-determining** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5134 | **consign** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5135 | **do-i** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5136 | **underfoot** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5137 | **gusto** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5138 | **wher** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5139 | **tea-party** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5140 | **hoove** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5141 | **swamped** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5142 | **fleece** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5143 | **lambing** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5144 | **dowry** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5145 | **in-law** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5146 | **pretentious** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5147 | **breast-meat** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5148 | **tripe** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5149 | **bloody** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5150 | **willow-wand** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5151 | **indeed-considering** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5152 | **mothers-we** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5153 | **thereupon** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5154 | **sundered** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5155 | **involved-a** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5156 | **seiz** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5157 | **lash** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5158 | **thong** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5159 | **bluish** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5160 | **not-or** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5161 | **subterfuge** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5162 | **deceiving** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5163 | **debilitate** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5164 | **poring** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5165 | **overpower** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5166 | **shoulder-blade** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5167 | **daybreak** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5168 | **wink** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5169 | **torrna-offering** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5170 | **carne** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5171 | **disdainfully** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5172 | **railed** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5173 | **dharma-practitioner** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5174 | **slander** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5175 | **ware** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5176 | **extort** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5177 | **haggling** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5178 | **covet** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5179 | **vaisravana** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5180 | **nefarious** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5181 | **corrupting** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5182 | **awl** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5183 | **laity** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5184 | **gravest** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5185 | **particu** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5186 | **lar** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5187 | **masturbation** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5188 | **bereavement** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5189 | **menstruation** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5190 | **recov** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5191 | **ery** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5192 | **child-birth** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5193 | **prepubescent** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5194 | **devastatingly** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5195 | **imposter** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5196 | **thanksgiving** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5197 | **chastised** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5198 | **concept-bound** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5199 | **second-and** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5200 | **rude** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | 0.238979 | - | — |
| 5201 | **sweetly** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5202 | **not-such** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5203 | **aimlessly** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5204 | **libidinous** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5205 | **cussing** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5206 | **disturb** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5207 | **gossip-monger** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5208 | **rituals-just** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5209 | **perfunctorily** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5210 | **sorcerers-i** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5211 | **cast-iron** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5212 | **lethally** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5213 | **life-artery** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5214 | **desirous** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5215 | **acquisitive** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5216 | **contemplat** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5217 | **agreeable** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5218 | **invent** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5219 | **malicious** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5220 | **catego** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5221 | **ry** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | ~ |
| 5222 | **eternally** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5223 | **roundness** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5224 | **iridescent** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5225 | **sharpened** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5226 | **bad-all** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5227 | **spontane** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5228 | **ously** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5229 | **unvirtuous** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5230 | **mistakenly** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5231 | **meri** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5232 | **torious** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5233 | **resuscitate** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5234 | **negate** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5235 | **impulse-extremely** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5236 | **ignorance-motivating** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5237 | **instinct** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5238 | **newborn** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5239 | **adulthood** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5240 | **assaulted** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5241 | **pillage** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5242 | **bandit** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5243 | **raids-often** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5244 | **life-or** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5245 | **bereft** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5246 | **destitute** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5247 | **preta-like** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5248 | **indulged** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5249 | **hating** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5250 | **belittled** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5251 | **hurling** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5252 | **argumentative** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5253 | **defiantly** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5254 | **grudgingly** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5255 | **recon** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5256 | **ciling** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5257 | **insulting** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5258 | **or-worse** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5259 | **still-to** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5260 | **kapila** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5261 | **horse-head** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5262 | **ox-head** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5263 | **fish-like** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5264 | **extol** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5265 | **self-assurance** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5266 | **joyless** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5267 | **mortally** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5268 | **insecu** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5269 | **rity** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5270 | **inhabit** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5271 | **gorge** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5272 | **terrain** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5273 | **infertile** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5274 | **untimely** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5275 | **inhospitable** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5276 | **proliferate** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | 0.181607 | - | — |
| 5277 | **example-or** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5278 | **animals-i** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5279 | **vaisakha** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5280 | **reconcile** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5281 | **uninterrupted** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5282 | **experiences-from** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5283 | **hell-arise** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5284 | **impel** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5285 | **identifiable** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5286 | **sravasti** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5287 | **pole** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5288 | **writhed** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5289 | **matropakara** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5290 | **tied-up** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5291 | **writhing** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5292 | **laughed** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5293 | **acacia** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5294 | **splinter-the** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5295 | **parivraji** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5296 | **kas** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5297 | **succumbed** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5298 | **jeta** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5299 | **suf** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5300 | **fering** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5301 | **clairvoyant** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5302 | **woodland** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5303 | **stoking** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5304 | **punish** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5305 | **debili** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5306 | **tated** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5307 | **nagar** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5308 | **juna** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5309 | **we-whose** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5310 | **innumerable-ever** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5311 | **underestimate** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5312 | **minutest** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5313 | **wedding** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5314 | **fistful** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5315 | **antisarar** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5316 | **devo** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5317 | **profuse** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5318 | **vajrap** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5319 | **pirate** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5320 | **non-returning** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5321 | **hopelessly** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5322 | **wrong-doer** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5323 | **impression-or** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5324 | **generator** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5325 | **moti** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5326 | **vation** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5327 | **neatly** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5328 | **kungyal** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5329 | **stumbled** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5330 | **penyulgyal** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5331 | **yoghurt-addict** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5332 | **self-centredness** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5333 | **expectant** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5334 | **ravi** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5335 | **cutter** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5336 | **tormented-in** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5337 | **tormented-by** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5338 | **prattling** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5339 | **materialism** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5340 | **ideology** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5341 | **tiness** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5342 | **authentically** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5343 | **heaping** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5344 | **ments-and** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5345 | **dhara** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5346 | **unreal** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5347 | **mingle** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5348 | **practices-the** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5349 | **formless** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | ~ |
| 5350 | **insight-should** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5351 | **take-while** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5352 | **impregnated** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5353 | **moist** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5354 | **whomever** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5355 | **vow-the** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5356 | **knowl** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5357 | **practices-out** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5358 | **wardly** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5359 | **actualized** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5360 | **observance** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5361 | **unbroken** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5362 | **preoc** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5363 | **cupation** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5364 | **seing** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5365 | **resolutely** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5366 | **nephew** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5367 | **descendant** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5368 | **mundane** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5369 | **reasons-like** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5370 | **priestly** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5371 | **suited** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5372 | **pedestal** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5373 | **visitor** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5374 | **fainted** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5375 | **ape** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5376 | **idiot** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5377 | **well-bound** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5378 | **leaping** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5379 | **venomous** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5380 | **coiled** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5381 | **beguiled** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5382 | **unmistaken** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5383 | **uniquely** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5384 | **ple** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5385 | **expediently** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5386 | **noblest** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5387 | **unfailingly** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5388 | **downpour** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5389 | **extinguish** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5390 | **agement** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5391 | **charting** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5392 | **quenching** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5393 | **showered** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5394 | **wayfarer** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5395 | **ferryman** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5396 | **stable-minded** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5397 | **all-such** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5398 | **sittra** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5399 | **anged** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5400 | **resentful** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5401 | **reprimand** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5402 | **resent** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5403 | **disregarding** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5404 | **incomprehensibly** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5405 | **ruined** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5406 | **tub** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5407 | **grilled** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5408 | **snapping** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5409 | **flawless** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5410 | **deceitful** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5411 | **glimpsed** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5412 | **outburst** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5413 | **treading** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5414 | **vanity** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5415 | **discontent** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5416 | **unconsidered** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5417 | **insincere** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5418 | **laughing** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5419 | **joking** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5420 | **chat** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5421 | **awe** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5422 | **casualness** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5423 | **solicitously** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5424 | **vainly** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5425 | **scowl** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5426 | **ill-considered** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5427 | **composure** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5428 | **conver** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5429 | **self-im** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5430 | **portance** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5431 | **untiringly** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5432 | **gliding** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5433 | **delighting** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5434 | **spoiling** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5435 | **bored** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5436 | **steadfastness** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | 0.239102 | - | — |
| 5437 | **tasting** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5438 | **better-off** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5439 | **fellow-voyager** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5440 | **bean-tsampa** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5441 | **fruitful-thi** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5442 | **contemplation** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5443 | **portrait** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5444 | **epitomiz** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5445 | **assiduous** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5446 | **examina** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5447 | **abound** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5448 | **deception** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5449 | **voice-or** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5450 | **name-can** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5451 | **restless** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5452 | **transfixed** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5453 | **limb-just** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5454 | **ropa** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5455 | **bodily** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5456 | **prajna** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5457 | **go-and** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5458 | **abode** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5459 | **circumference** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5460 | **sixty-eight** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5461 | **blissfully** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5462 | **prais** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5463 | **sadapraru** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5464 | **dita** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5465 | **marrow** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5466 | **spurted** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5467 | **smash** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5468 | **inflicting** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5469 | **reassumed** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5470 | **domain** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5471 | **mersed** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5472 | **prajaa** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5473 | **deco** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5474 | **censer** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5475 | **wafted** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5476 | **aloe-wood** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5477 | **coffer** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5478 | **pranaparamita** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5479 | **sada** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5480 | **prarudita** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5481 | **sprinkle** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5482 | **sprinkled** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5483 | **lion-throne** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5484 | **expounded** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5485 | **buddhas-a** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5486 | **melodious** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | ~ |
| 5487 | **oiling** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5488 | **bearable** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5489 | **streamed** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5490 | **these-twenty-four** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5491 | **forbade** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5492 | **pandita-gatekeeper** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5493 | **magadha** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5494 | **insistently** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5495 | **compassion-why** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5496 | **gatekeeper** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5497 | **retorted** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5498 | **ngari** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5499 | **gungthang** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5500 | **sherab** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5501 | **thopa-ga** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5502 | **yungdrung** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5503 | **throgyal** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5504 | **lharje** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5505 | **nupchung** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5506 | **repenting** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5507 | **eminently** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5508 | **hail-if** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5509 | **night-and** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5510 | **suffuse** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5511 | **tingled** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5512 | **tarma** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5513 | **dode** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5514 | **continu** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5515 | **reckon** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5516 | **acquiesced** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5517 | **twelve-pillared** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5518 | **sanctuary** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5519 | **meton** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5520 | **tsonpo** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5521 | **tsangrong** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5522 | **sarilvara** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5523 | **tsurton** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5524 | **wange** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5525 | **dol** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5526 | **guhyasamaja** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5527 | **ngokton** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5528 | **chador** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5529 | **shung** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5530 | **khok** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5531 | **powerment** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5532 | **dispersed** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5533 | **mahasiddha** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | ✓ གྲུབ་ཆེན |
| 5534 | **tacarya** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5535 | **floundering** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5536 | **byway** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5537 | **vajrasativa** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5538 | **life-story** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5539 | **sprout** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5540 | **bestowing** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5541 | **departed-i** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5542 | **simple-minded** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5543 | **caretaker** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5544 | **food-offering** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5545 | **butter-lamp** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5546 | **imagined** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5547 | **dunking** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5548 | **sputter** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5549 | **tthrow** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5550 | **though-so** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5551 | **jowo-act** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5552 | **wrong-the** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5553 | **leavingjetsun** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5554 | **unwavering** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5555 | **realms-the** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5556 | **realm-motivate** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5557 | **beings-our** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5558 | **beginnin** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5559 | **gless** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5560 | **time-are** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5561 | **dhar** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5562 | **makaya** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5563 | **indestructible** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5564 | **all-pervasive** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5565 | **mindstream** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5566 | **inseparability** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5567 | **irregulari** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5568 | **twig** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5569 | **entrancing** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5570 | **lion** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5571 | **multi-coloured** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5572 | **cloak** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5573 | **sleeved** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5574 | **tunic** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5575 | **samantab** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5576 | **jnanasiltra** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5577 | **consort-the** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5578 | **trisongdetsen** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5579 | **nirmanakya** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5580 | **garbed** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5581 | **hood-the** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5582 | **right-hand** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5583 | **families-mafijusri** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5584 | **left-hand** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5585 | **alms-bowl** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5586 | **topmost** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5587 | **resonate** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5588 | **melody** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5589 | **consonant** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5590 | **dharma-protector** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5591 | **leaking** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5592 | **detest** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5593 | **refuge-prayer** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5594 | **precedence** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5595 | **kinder** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5596 | **possessions-the** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5597 | **aunt** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5598 | **palmo** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | ~ |
| 5599 | **assailed** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5600 | **invade** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5601 | **fearlessness** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5602 | **impelled** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5603 | **slingstone** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5604 | **whirring** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5605 | **tirthika-who** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5606 | **criticiz** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5607 | **breeze** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | 0.224277 | - | — |
| 5608 | **day-come** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5609 | **rend** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5610 | **doud** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5611 | **healing** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5612 | **life-comfort** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5613 | **whatever-spring** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5614 | **create-prostration** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5615 | **disciples-to** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5616 | **nicknamed** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5617 | **pawned** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5618 | **saliva** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5619 | **maxim** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5620 | **vajradhatvishvari** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | ✓ རྡོ་རྗེ་དབྱིངས་ཕྱུག་མ |
| 5621 | **seed-syllable** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5622 | **disre** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5623 | **spect** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5624 | **seventy** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5625 | **stanza** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5626 | **reparation** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5627 | **tenuous** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5628 | **people-the** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5629 | **moulded** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5630 | **it-all** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5631 | **seductive** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5632 | **gullible** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5633 | **decadence** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5634 | **deceived** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5635 | **seduction** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5636 | **invaded** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5637 | **hesita** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5638 | **guis** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5639 | **oppos** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5640 | **disciples-none** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5641 | **goggle** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5642 | **effigy** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5643 | **goat-pen** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5644 | **legitimately** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5645 | **perni** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5646 | **cious** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5647 | **malevolent** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5648 | **confi** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5649 | **dence** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5650 | **pacified** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5651 | **harm-the** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5652 | **makers-will** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5653 | **quarter-pint** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5654 | **faint-hearted** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5655 | **pathetic** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5656 | **even-minded** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5657 | **on-while** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5658 | **low-caste** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5659 | **stung** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5660 | **brushing** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5661 | **accidentally** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5662 | **diffi** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5663 | **culty** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5664 | **all-those** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5665 | **you-train** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5666 | **beings-whether** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5667 | **between-a** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5668 | **mindless** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5669 | **distinc** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5670 | **devoting** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5671 | **cosy** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5672 | **glared** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5673 | **endeavouring** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5674 | **jeal** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5675 | **ousy** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5676 | **hypocrite** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5677 | **ity** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5678 | **despise** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5679 | **distressed** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5680 | **khotan** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5681 | **mafljusri** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5682 | **dismembered** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5683 | **vanquished** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5684 | **chick** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5685 | **torment-a** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5686 | **bursting** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5687 | **butchered** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5688 | **delay-thi** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5689 | **barbarity** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5690 | **twist** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5691 | **belly-hair** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5692 | **weal** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5693 | **grunting** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5694 | **backside** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5695 | **horseback** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5696 | **sidesaddle** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5697 | **stumble** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5698 | **sympathy** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5699 | **animal-a** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5700 | **example-that** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5701 | **paralyzing** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5702 | **blood-blister** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5703 | **gutted** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5704 | **bled** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5705 | **flesh-eating** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5706 | **resourceful** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5707 | **twine** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5708 | **ring-hole** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5709 | **gouged** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5710 | **hoisted** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5711 | **yak-hair** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5712 | **cord** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5713 | **aching** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5714 | **rasp** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5715 | **rump** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5716 | **bruised** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5717 | **stirrup** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5718 | **exhausting** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5719 | **help-impartial** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5720 | **ganging** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5721 | **mischievous** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5722 | **intoning** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5723 | **impartial** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5724 | **horrible** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5725 | **hurled** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5726 | **exorcising** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5727 | **intimidating** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5728 | **spanking** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5729 | **pandering** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5730 | **wrongdoer** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5731 | **hateful** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5732 | **enemies-protecting** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5733 | **hatred-were** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5734 | **expel** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5735 | **indeed-not** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5736 | **hate-a** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5737 | **chong** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5738 | **vinayaka** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5739 | **strode** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5740 | **recogniz** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5741 | **cleric** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5742 | **cle** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5743 | **bleeding** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5744 | **decorate** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5745 | **rites-they** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5746 | **shred** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5747 | **compa** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5748 | **boiled** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5749 | **protectors-we** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5750 | **bodhisat** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5751 | **tvas-then** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5752 | **gleefully** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5753 | **mantrayana-namely** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5754 | **succulent** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5755 | **heedlessly** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5756 | **slaugh** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5757 | **murdering** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5758 | **prowl** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5759 | **roam** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5760 | **gnaw** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5761 | **innard** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5762 | **lookout** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5763 | **killer** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5764 | **inflamed** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5765 | **shaking** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5766 | **intimacy** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5767 | **hell-unless** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5768 | **preying** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5769 | **bon** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5770 | **sublimity** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5771 | **conspicuous** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5772 | **encapsulate** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5773 | **dharmas** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5774 | **bared** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5775 | **abhid** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5776 | **harma** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5777 | **prakasasila** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5778 | **sarighab** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5779 | **kukku** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5780 | **apada** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5781 | **persistence** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5782 | **stroking** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5783 | **maggot** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5784 | **foreleg** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5785 | **halo** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5786 | **shoulder-all** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5787 | **ofmaitreya** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5788 | **feelings-like** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5789 | **contented** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5790 | **displeased** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5791 | **alarmingly** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5792 | **logician** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5793 | **tsakpuwa** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5794 | **deva** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5795 | **datta** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5796 | **prodigious** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5797 | **kunpang** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5798 | **rakgyal** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5799 | **darkened** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5800 | **negativity** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5801 | **vile** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5802 | **physique** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5803 | **correspondingly** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5804 | **summarize** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5805 | **ferryboat** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5806 | **jasako** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5807 | **materialized** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5808 | **beheaded** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5809 | **scabrous** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5810 | **shaven-headed** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5811 | **bigot** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5812 | **panicular** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5813 | **woke** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5814 | **benevolent** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5815 | **activities-prostration** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5816 | **circumam** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5817 | **bulation** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5818 | **hean** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5819 | **jackal** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5820 | **tative** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5821 | **discriminating** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5822 | **thusness** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | ✓ དེ་བཞིན་ཉིད |
| 5823 | **foundering** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5824 | **friendless** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5825 | **binh** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5826 | **suvarl** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5827 | **advipa** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5828 | **suvarnadvipa** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | ~ |
| 5829 | **swindle** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5830 | **either-try** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5831 | **pinprick** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5832 | **pain-we** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5833 | **thumbnail** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5834 | **enslaved** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5835 | **trungpa** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5836 | **sinachen** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5837 | **kamarupa** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5838 | **goaded** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5839 | **kamarapa** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5840 | **cart** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5841 | **sea-captain** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5842 | **mercha** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5843 | **plank** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5844 | **ashore** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5845 | **intoxication** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5846 | **ravishingly** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5847 | **couch** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5848 | **pulver** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5849 | **ized** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5850 | **smashed** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5851 | **ulti** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5852 | **mate** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5853 | **chak** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5854 | **shingwa** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5855 | **langthang** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5856 | **succe** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5857 | **sor** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5858 | **stfipa** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5859 | **selfishness** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5860 | **subjugating** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5861 | **vaibhasika** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5862 | **cine-the** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5863 | **dozed** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5864 | **spat** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5865 | **scar** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5866 | **treatis** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5867 | **ceaselessly** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5868 | **donned** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5869 | **fervently** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5870 | **nivritta** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5871 | **palace-one** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5872 | **cubits-and** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5873 | **alternately** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5874 | **ketaka** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5875 | **saketa** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5876 | **largesse** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5877 | **organize** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5878 | **yanta** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5879 | **hard-to** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5880 | **raksasa** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5881 | **oblation** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5882 | **smitten** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5883 | **grief** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5884 | **ter** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5885 | **veda** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5886 | **coveting** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5887 | **enchantment** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5888 | **it-for** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5889 | **queen-hi** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5890 | **wife-in** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5891 | **curse** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5892 | **unreliable** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5893 | **numer** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5894 | **ous** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5895 | **wasn** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5896 | **perfections-generosity** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5897 | **concentration-are** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5898 | **masterful** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5899 | **moan** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5900 | **starvation** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5901 | **preta-realm** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5902 | **daring** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5903 | **gladly** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5904 | **cunning** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5905 | **mandabhadri** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5906 | **brewed** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5907 | **emptying** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5908 | **expound** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5909 | **evil-doing** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5910 | **undertak** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5911 | **actions-even** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5912 | **amusing** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5913 | **wronged** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5914 | **slandered** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5915 | **shatter** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5916 | **zeal** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5917 | **accus** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5918 | **unjustly** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5919 | **effect-a** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5920 | **grudge-will** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5921 | **anger-so** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5922 | **puff** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5923 | **humiliated** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5924 | **touchiness** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5925 | **admiringly** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5926 | **marry** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5927 | **sew** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5928 | **double-pointed** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5929 | **nairaftjana** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5930 | **asceticism** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5931 | **nettle** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5932 | **greenish** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5933 | **tenaciously** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5934 | **hopeless** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5935 | **melong** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | ~ |
| 5936 | **practi** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5937 | **bark** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5938 | **lakhe** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | ✓ གླ་ཁེ |
| 5939 | **rabjam** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5940 | **snowed** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5941 | **well-be** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5942 | **mourn** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5943 | **gristle** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5944 | **vom** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5945 | **ited** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5946 | **recount** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5947 | **bod** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5948 | **hisattva** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5949 | **hardhip** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5950 | **druk** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | ~ |
| 5951 | **karpo** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | ~ |
| 5952 | **unhurriedly** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5953 | **beware** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5954 | **deathbed** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5955 | **immedi** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5956 | **ately** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5957 | **coward** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5958 | **dancing-girl** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5959 | **time-one** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5960 | **them-such** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5961 | **clump** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5962 | **idleness** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5963 | **tenacity** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5964 | **reputed** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5965 | **sporadically** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5966 | **excite** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5967 | **spous** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5968 | **relatives-even** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5969 | **birth-are** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5970 | **shiwa** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | ~ |
| 5971 | **heedless** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5972 | **trifling** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5973 | **forethought** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5974 | **roving** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5975 | **squandered** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5976 | **academia** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5977 | **path-disenchantment** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5978 | **absorption-arise** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5979 | **natu** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5980 | **tranquillity** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5981 | **bustling** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5982 | **dispensed** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5983 | **fascinated** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5984 | **concept-free** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5985 | **ofvairocana** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5986 | **concentra** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5987 | **confining** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5988 | **substantiality** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5989 | **gandharva** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | ✓ དྲི་ཟ |
| 5990 | **them-the** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5991 | **scendent** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5992 | **twenty-two** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5993 | **thirty-six** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5994 | **contami** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5995 | **nate** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5996 | **self-aggrandizement** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5997 | **pline** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5998 | **giving-offering** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 5999 | **tiring** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6000 | **subdivision** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6001 | **summing** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6002 | **guile** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6003 | **non-attachment** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6004 | **contentment** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6005 | **thinker** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6006 | **nutshell** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6007 | **nirvina** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6008 | **non-dwelling** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6009 | **grasped** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6010 | **conceptualize** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6011 | **bodhicitta-emptiness** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6012 | **nnhika** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6013 | **relegate** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6014 | **bodhi** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6015 | **citta** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6016 | **intensively** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6017 | **frescoe** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6018 | **plastered** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6019 | **sincerest** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6020 | **unimpeded** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6021 | **miracles-if** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6022 | **be-realization** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6023 | **on-you** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6024 | **askedjetsun** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6025 | **disso** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6026 | **ciating** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6027 | **nyethang** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6028 | **kyung** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6029 | **lhangtsang** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6030 | **discursive** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6031 | **dividing** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6032 | **chegom** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6033 | **indivi** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6034 | **ible** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6035 | **non-conceptualization** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6036 | **non-action** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | ✓ |
| 6037 | **churn** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6038 | **purport** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6039 | **actions-except** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6040 | **actions-be** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6041 | **samayas-there** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6042 | **atapa** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6043 | **ninety-nine** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6044 | **carelessly** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6045 | **attentive** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6046 | **darsaka** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6047 | **sailkara** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6048 | **mouthing** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6049 | **anti** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6050 | **dote** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6051 | **buddhas-in** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6052 | **appli** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6053 | **cation** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6054 | **peril** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6055 | **dreadful** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6056 | **wickedness** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6057 | **concealing** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6058 | **trepidation** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6059 | **sukhavati** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6060 | **disillusioned** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6061 | **vajrasattva-purification** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6062 | **signify** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6063 | **fifteenth** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6064 | **reabsorb** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6065 | **sambhogakaya-the** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6066 | **headband** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6067 | **scarf** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6068 | **earring** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6069 | **armlet** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6070 | **bracelet** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6071 | **anklet** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6072 | **vajratopa** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6073 | **vividly** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6074 | **tangka** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | ✓ ཐང་ཀ |
| 6075 | **fresco** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6076 | **inert** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6077 | **pupil** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6078 | **atom** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6079 | **transgre** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6080 | **dishonourable** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6081 | **gooseflesh** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6082 | **glistening** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6083 | **dripping** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6084 | **flushed** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6085 | **expelled** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6086 | **spider** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6087 | **scorpion** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6088 | **toad** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6089 | **tadpole** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6090 | **vapour** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6091 | **orifice** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6092 | **personification** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6093 | **expectantly** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6094 | **earth-every** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6095 | **flesh-are** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6096 | **score** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6097 | **vertically** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6098 | **sixty-four** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6099 | **svabhavika** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6100 | **smilingly** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6101 | **behi** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6102 | **fringed** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6103 | **thousand-spoked** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6104 | **result-the** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6105 | **multi-col** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6106 | **oured** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6107 | **pronouncing** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6108 | **humming** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6109 | **rapakaya** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6110 | **spon** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6111 | **taneously** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6112 | **reabsorbing** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6113 | **vanishing** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6114 | **officiating** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6115 | **officiant** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6116 | **ornate** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6117 | **intonation** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6118 | **blaring** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6119 | **trumpet** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6120 | **drum** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | ~ |
| 6121 | **recited-at** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6122 | **goings-on** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6123 | **clattering** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6124 | **puspe** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6125 | **dhupe** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6126 | **travesty** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6127 | **swallowing** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6128 | **soul** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6129 | **grimy** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6130 | **scrupulous** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6131 | **tiresome** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6132 | **undistracted** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6133 | **laywoman** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6134 | **atiga** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6135 | **non-existent** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6136 | **valley-i** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6137 | **unfit** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6138 | **infecting** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6139 | **brightly** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6140 | **danced** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6141 | **samaya-and** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6142 | **delirious** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6143 | **urgyenpa** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6144 | **vanish** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6145 | **earthenware** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6146 | **denting** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6147 | **curing** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6148 | **unremittingly** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6149 | **joke** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6150 | **obscu** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6151 | **fooled** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6152 | **interdependently** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6153 | **virupa** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | ✓ |
| 6154 | **replete** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6155 | **bell-metal** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6156 | **turquois** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6157 | **sapphire** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6158 | **arura** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | ~ |
| 6159 | **kyurura** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | ~ |
| 6160 | **puls** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6161 | **direction-meaning** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6162 | **dha** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6163 | **obhya** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6164 | **ratnasambhava** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | ✓ རིན་ཆེན་འབྱུང་གནས |
| 6165 | **amoghasiddhi** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | ✓ དོན་ཡོད་གྲུབ་པ |
| 6166 | **stacked-up** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6167 | **altar** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6168 | **wiping** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6169 | **veil** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6170 | **woollen** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6171 | **chogyal** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | ~ |
| 6172 | **pakpa** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | ~ |
| 6173 | **nyingma** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6174 | **bhumi** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6175 | **sprinkling** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6176 | **ung** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6177 | **thumb** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6178 | **rekhe** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6179 | **purvavideha** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6180 | **deha** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6181 | **videha** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6182 | **inexhaustibly** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6183 | **victorious** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | ~ |
| 6184 | **unfilled** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6185 | **first-order** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6186 | **second-order** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6187 | **millionfold** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6188 | **third-order** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6189 | **buddha-sakyamuni** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6190 | **endurance** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6191 | **graced** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6192 | **infinitely** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6193 | **unborn** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6194 | **ache** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6195 | **seven-element** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6196 | **important-a** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6197 | **do-to** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6198 | **saturate** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6199 | **scented** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6200 | **generously** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6201 | **reasons-and** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6202 | **yourself-that** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6203 | **fooling** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6204 | **dirtily** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6205 | **mouldy** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6206 | **lamp-offering** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6207 | **rancid** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6208 | **shelze** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6209 | **consi** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6210 | **tency** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6211 | **torma-dough** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6212 | **distinctively** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6213 | **sublimely** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6214 | **scavenger** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6215 | **rice-gruel** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6216 | **maqc** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6217 | **fingernail** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6218 | **oily** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6219 | **rupakaya** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | ✓ གཟུགས་སྐུ |
| 6220 | **converse** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6221 | **barbaric** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6222 | **exclaim** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | 0.231249 | - | — |
| 6223 | **aiota** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6224 | **tree-or** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6225 | **world-even** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6226 | **rainbow-none** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6227 | **jaundice** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6228 | **cheerfully** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6229 | **dissipated** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6230 | **puri** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6231 | **fying** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6232 | **contradiction** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6233 | **tised** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6234 | **life-hermit** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6235 | **instance-use** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6236 | **clung** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6237 | **instantaneously** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6238 | **swaying** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6239 | **squealing** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6240 | **mother-the** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6241 | **consciousness-instantly** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6242 | **life-size** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6243 | **tripod** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6244 | **sizzle** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6245 | **foul** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6246 | **frothing** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6247 | **scum** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6248 | **exude** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6249 | **ridding** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6250 | **imperfection** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6251 | **billow** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6252 | **locality** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6253 | **teeming** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6254 | **deity-a** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6255 | **iaka** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6256 | **unfavour** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6257 | **swarm** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6258 | **activity-performing** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6259 | **appeasing** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6260 | **mother-use** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6261 | **scatter** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6262 | **victory-banner** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6263 | **overlord** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6264 | **underling** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6265 | **snatch** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6266 | **life-force** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6267 | **avenger** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6268 | **behind-the** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6269 | **suffering-the** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6270 | **life-restoring** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6271 | **offerer** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6272 | **vari** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6273 | **egated** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6274 | **variegated** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6275 | **grisly** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6276 | **slashing** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6277 | **bravado** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6278 | **hate-filled** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6279 | **clenching** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6280 | **lashing** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6281 | **whirl** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6282 | **inauspicious** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6283 | **compassion-but** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6284 | **ninefold** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6285 | **puny** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6286 | **retaliation-a** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6287 | **path-the** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6288 | **subjugation** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6289 | **instance-are** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6290 | **heaped** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6291 | **conceir** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6292 | **exultation** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6293 | **trampling** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6294 | **mischief** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6295 | **embar** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6296 | **rassed** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6297 | **mobilize** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6298 | **gyalgong** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6299 | **there-it** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6300 | **trance** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6301 | **insistent** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6302 | **predic** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6303 | **samaya-breaker** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6304 | **clergy** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6305 | **dream-like** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6306 | **momentarily** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6307 | **self-concern** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6308 | **maliciousness** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6309 | **others-and** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6310 | **fixation** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6311 | **qualifica** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6312 | **illustrative** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | ~ |
| 6313 | **untar** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6314 | **nished** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6315 | **alone-awaken** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6316 | **gotsangpa** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | ~ |
| 6317 | **rangrik** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6318 | **north-facing** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6319 | **devotional** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6320 | **uncontrived** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6321 | **vanquishing** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6322 | **nagabodhi** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6323 | **snatching** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6324 | **fervour** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6325 | **ligent** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6326 | **intellectualization** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6327 | **gyalmo** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6328 | **tsawarong** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6329 | **pang** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6330 | **meditation-band** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6331 | **hood** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6332 | **yana** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6333 | **enough-even** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6334 | **receptacle** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6335 | **vajrayogini** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6336 | **awakening** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6337 | **insubstantial** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6338 | **complexion** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6339 | **tinged** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6340 | **long-sleeved** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6341 | **gown** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6342 | **deerskin** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6343 | **adhara** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6344 | **unharmed** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6345 | **petalled** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6346 | **emblazoned** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6347 | **culmination** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6348 | **long-life** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6349 | **sprig** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6350 | **crook** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6351 | **mandarava** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | ✓ |
| 6352 | **dried-up** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6353 | **looped** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6354 | **pennant** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6355 | **encircled** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6356 | **evenness** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6357 | **siddhi** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | ✓ དངོས་གྲུབ |
| 6358 | **pliramita** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6359 | **insurpassable** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6360 | **hrib** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6361 | **prelimi** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6362 | **nary** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6363 | **surrendering** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6364 | **passer-by** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6365 | **lurch** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6366 | **ordeal** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6367 | **reverence** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6368 | **bending** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6369 | **cupped** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6370 | **ful** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6371 | **hunchback** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6372 | **dwarf** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6373 | **them-so** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6374 | **deformed** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6375 | **impeccably** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6376 | **it-and** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6377 | **fruitless** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6378 | **proficient** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6379 | **head-dress** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6380 | **soaked** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6381 | **dye** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6382 | **dyed** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6383 | **successfully-but** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6384 | **violator** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6385 | **aya** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6386 | **evildoer** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6387 | **dharma-just** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6388 | **butter-bag** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6389 | **imprinted** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6390 | **clipping** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6391 | **usnisa** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6392 | **offering-that** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6393 | **ostentation** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6394 | **antabhadra** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6395 | **musical** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6396 | **ema** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6397 | **nated** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6398 | **multitudinous** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6399 | **mani** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | ✓ |
| 6400 | **fested** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6401 | **cloudbank** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6402 | **perfecting** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6403 | **unmentionably** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6404 | **obstruction** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6405 | **doer** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6406 | **negative-not** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6407 | **ofi** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6408 | **nstruction** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6409 | **ostentatious** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6410 | **merus** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6411 | **ungrateful** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6412 | **subdivided** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6413 | **kriya** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | ~ |
| 6414 | **vedic** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6415 | **transmutation** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6416 | **cunda** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6417 | **non-conceptual** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6418 | **aigaramati** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6419 | **rub** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | 0.231898 | - | — |
| 6420 | **wholeheartedly** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6421 | **dedica** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6422 | **ofvaisali** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6423 | **horrified** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6424 | **heruka** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6425 | **you-in** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6426 | **body-on** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6427 | **mala** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6428 | **orh** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6429 | **moon-crystal** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6430 | **actions-taking** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6431 | **misconduct-and** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6432 | **fro** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6433 | **nirm** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6434 | **actions-lying** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6435 | **chatter-and** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6436 | **views-and** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6437 | **streak** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6438 | **underly** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6439 | **svabhavikakaya** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | ✓ ངོ་བོ་ཉིད་ཀྱི་སྐུ |
| 6440 | **ardent** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6441 | **longing** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6442 | **you-up** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6443 | **vajrayogini-you** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6444 | **overexcited** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6445 | **lassitude** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6446 | **torpor** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6447 | **agitation** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6448 | **inseparably** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6449 | **naturalness** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6450 | **inconceivably** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6451 | **charac** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6452 | **teristic** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6453 | **listener** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6454 | **relate-neither** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6455 | **detail-the** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6456 | **translations-known** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6457 | **actualize** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6458 | **incon** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6459 | **ceivably** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6460 | **causal** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6461 | **mantrayana-kriya** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6462 | **bewilderment** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6463 | **doc** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6464 | **trine** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6465 | **acclaimed** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6466 | **kingja** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6467 | **nobility** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6468 | **lament** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6469 | **consented** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6470 | **kila** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | ✓ ཕུར་བ |
| 6471 | **thotrengtsel** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6472 | **devabhadrapala** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6473 | **eldest** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6474 | **anandagarbha** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | ✓ བདེ་མཆོག་སྙིང་པོ |
| 6475 | **devaputra** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6476 | **circling** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6477 | **pasupati** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6478 | **jewel-coloured** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6479 | **kausika** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6480 | **level-you** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6481 | **illuminate** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6482 | **symbolized** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6483 | **sponta** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6484 | **neously** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6485 | **primordially** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6486 | **vajraloka** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6487 | **vajraguhya** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6488 | **ratnaloka** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6489 | **ratnapada** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6490 | **padmakaya** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6491 | **padmaprabha** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6492 | **atha** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6493 | **gata** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6494 | **visuddhasiddha** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6495 | **siddhyaloka** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6496 | **viyoganta** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6497 | **irocana** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6498 | **all-victorious** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6499 | **vajrapal** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6500 | **dazzling** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6501 | **jewel-encrusted** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6502 | **ered** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6503 | **heart-son** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6504 | **uparaja** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6505 | **alokabhasvati** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6506 | **hap** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6507 | **pened** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6508 | **presage** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6509 | **gleaming** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6510 | **marvelling** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6511 | **vajrapaqi** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6512 | **twenty-thousand** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6513 | **empowered** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6514 | **sukhapala** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6515 | **kuhana** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6516 | **sarasiddhi** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6517 | **charnel** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | ~ |
| 6518 | **mahahe** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6519 | **compiler** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6520 | **nir** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6521 | **manakaya** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6522 | **dare** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6523 | **manife** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6524 | **uttering** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6525 | **polemic** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6526 | **compose** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6527 | **instantaneous** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6528 | **cessation** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6529 | **shosha** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6530 | **astrology** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6531 | **hastibhala** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6532 | **jnanasutra** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6533 | **pal** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | ~ |
| 6534 | **qita** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6535 | **tribe** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6536 | **descended** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6537 | **ape-an** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6538 | **crag-demoness** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6539 | **chao** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6540 | **satanika** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6541 | **webbed** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6542 | **eyelid** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6543 | **banished** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6544 | **ancient-nyatri** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6545 | **sarvanivaranaviskam** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6546 | **bhin** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6547 | **yumbu** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6548 | **lakhar** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6549 | **cintamani** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6550 | **kongjo-a** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6551 | **tara-and** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6552 | **nepalese** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6553 | **tritsun-a** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6554 | **bhrikuti** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | ✓ ཇོ་མོ་ཁྲོ་གཉེར་ཅན |
| 6555 | **devavit** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6556 | **sirhha** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6557 | **ofj** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6558 | **ewel** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6559 | **akarmati** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6560 | **amradvipa** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6561 | **eleven-headed** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6562 | **ngam** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6563 | **lugong** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6564 | **lhazang** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6565 | **lupel** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6566 | **archive** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6567 | **discovering** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6568 | **forebear** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6569 | **gungtsen** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6570 | **nyang** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | ~ |
| 6571 | **resided** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6572 | **chimpu** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | ~ |
| 6573 | **insight** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | ~ |
| 6574 | **gomadeviya** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6575 | **aryapalo** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6576 | **tremble** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6577 | **subju** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6578 | **sariwari** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6579 | **horse-breeder** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6580 | **swineherd** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6581 | **poultryman** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6582 | **dog-breeder** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6583 | **trisher** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6584 | **dudjom** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6585 | **chim** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6586 | **sakyaprabha** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6587 | **shubu** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | ~ |
| 6588 | **palgyi** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | ~ |
| 6589 | **senge** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | ~ |
| 6590 | **protectress** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6591 | **oath** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6592 | **trakmar** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6593 | **three-storey** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6594 | **sub** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6595 | **enclosed** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6596 | **consecration** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6597 | **heart-disciples-the** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6598 | **nyangwen** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6599 | **antric** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6600 | **scroll** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | ~ |
| 6601 | **legacy** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6602 | **mindtt** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6603 | **together-the** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6604 | **lineage-from** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6605 | **recounting** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6606 | **already-with** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6607 | **dharma-companion** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6608 | **unmi** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6609 | **faultless** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6610 | **mind-consciousness** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6611 | **interme** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6612 | **diate** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6613 | **it-which** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6614 | **despicable** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6615 | **protruding** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6616 | **crimson** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6617 | **pilgrimage** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6618 | **incarnate** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6619 | **gyurme** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6620 | **thekchok** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6621 | **trime** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6622 | **golok** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6623 | **so-and-so** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6624 | **confe** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6625 | **enthroned** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6626 | **life-energy** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6627 | **pluck** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6628 | **auditory** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6629 | **blur** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6630 | **salivate** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6631 | **extremity** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6632 | **energies-the** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6633 | **life-supporting** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6634 | **life-channel** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6635 | **sigh** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6636 | **whiteness** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6637 | **cloudless** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6638 | **redness** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6639 | **lustful** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6640 | **blackness** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6641 | **swoon** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6642 | **vajra-posture** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6643 | **purpos** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6644 | **rattle** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6645 | **tent** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6646 | **axi** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6647 | **mind-con** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6648 | **visarga** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6649 | **flut** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6650 | **tering** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6651 | **three-layered** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6652 | **embodying** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6653 | **clad** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6654 | **attire** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6655 | **nirmat** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6656 | **ursina** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6657 | **bead** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6658 | **skyward** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6659 | **akanistha** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6660 | **repre** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6661 | **sentation** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6662 | **palate** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6663 | **grass-stalk** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6664 | **nyi** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6665 | **iyana** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6666 | **palyul** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | ~ |
| 6667 | **vajrapdt** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6668 | **one-pointed** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6669 | **beseech** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6670 | **gochen** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6671 | **contriving** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6672 | **amitayus** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | ✓ ཚེ་དཔག་མེད |
| 6673 | **amarani** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6674 | **jivantiye** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6675 | **svaha** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6676 | **and-through** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6677 | **inter** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6678 | **dependence-dispel** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6679 | **ach** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6680 | **serum** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6681 | **dew** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6682 | **stalk** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6683 | **assiduously** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6684 | **shortcut** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6685 | **mutter** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6686 | **incoherently** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6687 | **interminable** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6688 | **goad** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6689 | **mination** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6690 | **meditation-all** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6691 | **creativity** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | ~ |
| 6692 | **aesthetic** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6693 | **literary** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6694 | **banish** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6695 | **fabricate** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6696 | **watershed** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6697 | **evil-even** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6698 | **indissolubly** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6699 | **clude** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6700 | **adulteration** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6701 | **well-cooked** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6702 | **fancy** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6703 | **seasoned** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6704 | **savoury** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6705 | **cooking-juice** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6706 | **ploughshare** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6707 | **unearthing** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6708 | **nanny** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6709 | **uprooting** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6710 | **elegance** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6711 | **poetry** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6712 | **copious** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6713 | **cramped** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6714 | **discours** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6715 | **philosophical** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6716 | **soak** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6717 | **gloom** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6718 | **imperturbable** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6719 | **instructor** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6720 | **impart** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6721 | **savant** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6722 | **verbose** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6723 | **discourse** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6724 | **confection** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6725 | **cleverly** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6726 | **fanciful** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6727 | **superficially** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6728 | **vajra-brother** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6729 | **compile** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6730 | **nourished** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6731 | **captivate** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6732 | **intoxicating** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6733 | **seclusion** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6734 | **dronma** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6735 | **tsering** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6736 | **kunzangthekchok** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6737 | **tulku** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | ✓ སྤྲུལ་སྐུ |
| 6738 | **peated** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6739 | **times-even** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6740 | **kushab** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6741 | **shenpen** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6742 | **thaye** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | ~ |
| 6743 | **ozer** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6744 | **dharma-sovereign** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6745 | **tradition-in** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6746 | **changchub** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6747 | **cbokyi** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6748 | **embellishment** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6749 | **rough-mannered** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6750 | **rudam** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6751 | **samten** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6752 | **choling** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6753 | **palace-a** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6754 | **foliage** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6755 | **undergrowth** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6756 | **filtering** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6757 | **swasti** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6758 | **siddham** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6759 | **unfolded** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6760 | **renowned** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6761 | **gyalwai** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6762 | **nyugu** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6763 | **chokyi** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6764 | **lekdrup** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6765 | **temporally** | 1 | 166.19 | 9.59 | 🔵 low — common in general English | - | - | — |
| 6766 | **reduced** | 2 | 166.13 | 4.793221 | 🔵 low — common in general English | - | - | — |
| 6767 | **balance** | 2 | 161.72 | 4.665882 | 🔵 low — common in general English | - | - | — |
| 6768 | **own** | 2 | 160.97 | 4.644375 | 🔵 low — common in general English | - | - | — |
| 6769 | **decision** | 2 | 160.97 | 4.644375 | 🔵 low — common in general English | - | - | ~ |
| 6770 | **contradict** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - | - | — |
| 6771 | **lured** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - | - | — |
| 6772 | **snapped** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - | - | — |
| 6773 | **numerical** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - | - | — |
| 6774 | **orientation** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - | - | — |
| 6775 | **deprive** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - | - | — |
| 6776 | **reasoned** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - | - | — |
| 6777 | **disappearance** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - | - | — |
| 6778 | **inundated** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - | - | — |
| 6779 | **incompatible** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - | - | — |
| 6780 | **baring** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - | - | — |
| 6781 | **highway** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - | - | — |
| 6782 | **transformation** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - | - | — |
| 6783 | **pinnacle** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - | - | — |
| 6784 | **tri** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - | - | — |
| 6785 | **dependable** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - | - | — |
| 6786 | **escaped** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - | - | — |
| 6787 | **slab** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - | - | — |
| 6788 | **dearly** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - | - | — |
| 6789 | **transitory** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - | - | — |
| 6790 | **rigorous** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - | - | — |
| 6791 | **prolong** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - | - | — |
| 6792 | **toxic** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - | - | — |
| 6793 | **crawl** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | 0.231070 | - | — |
| 6794 | **formidable** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - | - | — |
| 6795 | **dangerously** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - | - | — |
| 6796 | **bribe** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - | - | — |
| 6797 | **immune** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - | - | — |
| 6798 | **amidst** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - | - | — |
| 6799 | **guideline** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - | - | — |
| 6800 | **marsh** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - | - | — |
| 6801 | **raven** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - | - | — |
| 6802 | **purse** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - | - | — |
| 6803 | **plying** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - | - | — |
| 6804 | **icy** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - | - | — |
| 6805 | **evaporated** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - | - | — |
| 6806 | **eyed** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - | - | — |
| 6807 | **castrated** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - | - | — |
| 6808 | **ridden** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - | - | — |
| 6809 | **entail** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - | - | — |
| 6810 | **bartering** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - | - | — |
| 6811 | **crow** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - | - | — |
| 6812 | **infant** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - | - | — |
| 6813 | **unnoticed** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - | - | — |
| 6814 | **integrity** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - | - | — |
| 6815 | **occupying** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - | - | — |
| 6816 | **charming** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - | - | — |
| 6817 | **strife** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - | - | — |
| 6818 | **haul** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - | - | — |
| 6819 | **outdoor** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - | - | — |
| 6820 | **guilty** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - | - | — |
| 6821 | **sharpest** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - | - | — |
| 6822 | **circulate** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - | - | — |
| 6823 | **transferring** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - | - | — |
| 6824 | **residue** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - | - | — |
| 6825 | **poorer** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - | - | — |
| 6826 | **unattractive** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - | - | — |
| 6827 | **unjust** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - | - | — |
| 6828 | **self-confidence** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - | - | — |
| 6829 | **fulfilment** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - | - | — |
| 6830 | **propel** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - | - | — |
| 6831 | **jam** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - | - | — |
| 6832 | **infuse** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - | - | — |
| 6833 | **absurd** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - | - | — |
| 6834 | **mindful** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - | - | — |
| 6835 | **vigilant** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - | - | — |
| 6836 | **incumbent** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - | - | — |
| 6837 | **decay** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - | - | — |
| 6838 | **immensely** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - | - | — |
| 6839 | **violently** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - | - | — |
| 6840 | **saint** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - | - | — |
| 6841 | **honoured** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - | - | — |
| 6842 | **piercing** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - | - | — |
| 6843 | **forbid** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - | - | — |
| 6844 | **wondering** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - | - | — |
| 6845 | **tending** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - | - | — |
| 6846 | **summoned** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - | - | — |
| 6847 | **compelling** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - | - | — |
| 6848 | **rosy** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - | - | — |
| 6849 | **one-sided** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - | - | — |
| 6850 | **sel** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - | - | — |
| 6851 | **opponent** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - | - | — |
| 6852 | **cheated** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - | - | — |
| 6853 | **banquet** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - | - | — |
| 6854 | **author** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - | - | — |
| 6855 | **stubborn** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - | - | — |
| 6856 | **sheltered** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - | - | — |
| 6857 | **void** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - | - | — |
| 6858 | **viewing** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - | - | — |
| 6859 | **slaughtering** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - | - | — |
| 6860 | **boarded** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - | - | — |
| 6861 | **ludicrous** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - | - | — |
| 6862 | **shade** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - | - | — |
| 6863 | **grinding** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - | - | — |
| 6864 | **invariably** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - | - | — |
| 6865 | **detrimental** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - | - | — |
| 6866 | **kicking** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - | - | — |
| 6867 | **welt** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - | - | — |
| 6868 | **charitable** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - | - | — |
| 6869 | **mediocre** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - | - | — |
| 6870 | **guarding** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - | - | — |
| 6871 | **tran** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - | - | — |
| 6872 | **counteract** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - | - | — |
| 6873 | **bounce** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - | - | — |
| 6874 | **print** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - | - | — |
| 6875 | **maya** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - | - | — |
| 6876 | **stan** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - | - | — |
| 6877 | **soaking** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - | - | — |
| 6878 | **thickness** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - | - | — |
| 6879 | **tumbling** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - | - | — |
| 6880 | **finest** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - | - | — |
| 6881 | **gratified** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - | - | — |
| 6882 | **expose** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - | - | — |
| 6883 | **fence** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - | - | — |
| 6884 | **straw** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - | - | — |
| 6885 | **deplete** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - | - | — |
| 6886 | **rushing** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - | - | — |
| 6887 | **confront** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - | - | — |
| 6888 | **vertical** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - | - | — |
| 6889 | **fifteen** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - | - | — |
| 6890 | **chopping** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - | - | — |
| 6891 | **deepen** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - | - | — |
| 6892 | **surrender** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - | - | — |
| 6893 | **south-west** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - | - | — |
| 6894 | **layer** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - | - | — |
| 6895 | **confidently** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - | - | — |
| 6896 | **respected** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - | - | — |
| 6897 | **midst** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - | - | — |
| 6898 | **concluding** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - | - | — |
| 6899 | **ame** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - | - | — |
| 6900 | **displayed** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - | - | — |
| 6901 | **hut** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - | - | — |
| 6902 | **berry** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - | - | — |
| 6903 | **opportune** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - | - | — |
| 6904 | **obscuring** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - | - | — |
| 6905 | **contradictory** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - | - | — |
| 6906 | **evacuation** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - | - | — |
| 6907 | **erect** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - | - | — |
| 6908 | **leaning** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - | - | — |
| 6909 | **regent** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - | - | — |
| 6910 | **henceforth** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English | - | - | — |
| 6911 | **market** | 3 | 156.83 | 3.016666 | 🔵 low — common in general English | - | - | — |
| 6912 | **wheat** | 2 | 155.84 | 4.496322 | 🔵 low — common in general English | - | - | — |
| 6913 | **owned** | 2 | 154.29 | 4.451472 | 🔵 low — common in general English | - | - | — |
| 6914 | **seize** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English | - | - | — |
| 6915 | **aged** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English | - | - | — |
| 6916 | **undue** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English | - | - | — |
| 6917 | **extracted** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English | - | - | — |
| 6918 | **thorough** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English | - | - | — |
| 6919 | **translation** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English | - | - | — |
| 6920 | **eastward** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English | - | - | — |
| 6921 | **erected** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English | - | - | — |
| 6922 | **wilderness** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English | - | - | — |
| 6923 | **contentious** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English | - | - | — |
| 6924 | **student** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English | - | - | — |
| 6925 | **wax** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English | - | - | — |
| 6926 | **diet** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English | - | - | — |
| 6927 | **als** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English | - | - | — |
| 6928 | **pause** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English | - | - | — |
| 6929 | **judging** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English | - | - | — |
| 6930 | **prelude** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English | - | - | — |
| 6931 | **ham** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English | - | - | — |
| 6932 | **exit** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English | - | - | — |
| 6933 | **ditch** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English | - | - | — |
| 6934 | **erupt** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English | - | - | — |
| 6935 | **fashion** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English | - | - | — |
| 6936 | **alike** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English | - | - | — |
| 6937 | **porter** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English | - | - | — |
| 6938 | **stall** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English | - | - | — |
| 6939 | **demonstrating** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English | - | - | — |
| 6940 | **neighbour** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English | 0.192017 | - | — |
| 6941 | **tumble** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English | - | - | — |
| 6942 | **wolf** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English | 0.231618 | - | — |
| 6943 | **overtly** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English | - | - | — |
| 6944 | **untrue** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English | - | - | — |
| 6945 | **diverse** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English | - | - | — |
| 6946 | **emotional** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English | - | - | — |
| 6947 | **choosing** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English | - | - | — |
| 6948 | **contravened** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English | - | - | — |
| 6949 | **disturbing** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English | - | - | — |
| 6950 | **mas** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English | - | - | — |
| 6951 | **fasting** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English | - | - | — |
| 6952 | **wondered** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English | - | - | — |
| 6953 | **crashed** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English | - | - | — |
| 6954 | **undergone** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English | - | - | — |
| 6955 | **suicide** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English | - | - | — |
| 6956 | **hardest** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English | - | - | — |
| 6957 | **desperately** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English | - | - | — |
| 6958 | **precipitous** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English | - | - | — |
| 6959 | **whereby** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English | - | - | — |
| 6960 | **progressed** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English | - | - | — |
| 6961 | **catching** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English | - | - | — |
| 6962 | **chronic** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English | - | - | — |
| 6963 | **bare** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English | - | - | — |
| 6964 | **hanging** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English | - | - | — |
| 6965 | **trailing** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English | - | - | — |
| 6966 | **materialize** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English | - | - | — |
| 6967 | **crossing** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English | - | - | — |
| 6968 | **dressing** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English | - | - | — |
| 6969 | **luck** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English | - | - | — |
| 6970 | **dashed** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English | - | - | — |
| 6971 | **fled** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English | - | - | — |
| 6972 | **analyzing** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English | - | - | — |
| 6973 | **dimmed** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English | - | - | — |
| 6974 | **favouring** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English | - | - | — |
| 6975 | **naive** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English | - | - | — |
| 6976 | **climbing** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English | - | - | — |
| 6977 | **affirmed** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English | - | - | — |
| 6978 | **pel** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English | - | - | — |
| 6979 | **frightening** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English | - | - | — |
| 6980 | **wipe** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English | - | - | — |
| 6981 | **cleaned** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English | - | - | — |
| 6982 | **thirdly** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English | - | - | — |
| 6983 | **extracting** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English | - | - | ~ |
| 6984 | **deadly** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English | - | - | — |
| 6985 | **violence** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English | - | - | — |
| 6986 | **cape** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English | - | - | — |
| 6987 | **chas** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English | - | - | — |
| 6988 | **discouraging** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English | - | - | — |
| 6989 | **realizing** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English | - | - | — |
| 6990 | **symbolic** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English | - | - | — |
| 6991 | **distilled** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English | - | - | — |
| 6992 | **misunderstanding** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English | - | - | — |
| 6993 | **ripe** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English | - | - | — |
| 6994 | **predominantly** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English | - | - | — |
| 6995 | **swelling** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English | - | - | — |
| 6996 | **intermediary** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English | - | - | — |
| 6997 | **evolution** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English | - | - | — |
| 6998 | **convey** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English | - | - | — |
| 6999 | **accrue** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English | - | - | — |
| 7000 | **new** | 3 | 151.18 | 2.907899 | 🔵 low — common in general English | - | - | ~ |
| 7001 | **focussing** | 1 | 150.37 | 8.676844 | 🔵 low — common in general English | - | - | — |
| 7002 | **impeded** | 1 | 150.37 | 8.676844 | 🔵 low — common in general English | - | - | — |
| 7003 | **silent** | 1 | 150.37 | 8.676844 | 🔵 low — common in general English | - | - | — |
| 7004 | **sheer** | 1 | 150.37 | 8.676844 | 🔵 low — common in general English | - | - | — |
| 7005 | **recede** | 1 | 150.37 | 8.676844 | 🔵 low — common in general English | - | - | — |
| 7006 | **blown** | 1 | 150.37 | 8.676844 | 🔵 low — common in general English | - | - | — |
| 7007 | **bubble** | 1 | 150.37 | 8.676844 | 🔵 low — common in general English | - | - | — |
| 7008 | **recourse** | 1 | 150.37 | 8.676844 | 🔵 low — common in general English | - | - | — |
| 7009 | **marking** | 1 | 150.37 | 8.676844 | 🔵 low — common in general English | - | - | — |
| 7010 | **cooler** | 1 | 150.37 | 8.676844 | 🔵 low — common in general English | - | - | — |
| 7011 | **constructed** | 1 | 150.37 | 8.676844 | 🔵 low — common in general English | - | - | — |
| 7012 | **wane** | 1 | 150.37 | 8.676844 | 🔵 low — common in general English | - | - | — |
| 7013 | **malt** | 1 | 150.37 | 8.676844 | 🔵 low — common in general English | - | - | — |
| 7014 | **freezing** | 1 | 150.37 | 8.676844 | 🔵 low — common in general English | - | - | — |
| 7015 | **mattress** | 1 | 150.37 | 8.676844 | 🔵 low — common in general English | - | - | — |
| 7016 | **await** | 1 | 150.37 | 8.676844 | 🔵 low — common in general English | - | - | — |
| 7017 | **rebel** | 1 | 150.37 | 8.676844 | 🔵 low — common in general English | - | - | — |
| 7018 | **hospitality** | 1 | 150.37 | 8.676844 | 🔵 low — common in general English | - | - | — |
| 7019 | **foreshadow** | 1 | 150.37 | 8.676844 | 🔵 low — common in general English | - | - | — |
| 7020 | **persuaded** | 1 | 150.37 | 8.676844 | 🔵 low — common in general English | - | - | — |
| 7021 | **yard** | 1 | 150.37 | 8.676844 | 🔵 low — common in general English | - | - | — |
| 7022 | **intermittent** | 1 | 150.37 | 8.676844 | 🔵 low — common in general English | - | - | — |
| 7023 | **emp** | 1 | 150.37 | 8.676844 | 🔵 low — common in general English | - | - | — |
| 7024 | **drifting** | 1 | 150.37 | 8.676844 | 🔵 low — common in general English | - | - | — |
| 7025 | **fragrance** | 1 | 150.37 | 8.676844 | 🔵 low — common in general English | - | - | — |
| 7026 | **ink** | 1 | 150.37 | 8.676844 | 🔵 low — common in general English | - | - | — |
| 7027 | **walked** | 1 | 150.37 | 8.676844 | 🔵 low — common in general English | - | - | — |
| 7028 | **pre** | 1 | 150.37 | 8.676844 | 🔵 low — common in general English | - | - | — |
| 7029 | **dole** | 1 | 150.37 | 8.676844 | 🔵 low — common in general English | - | - | — |
| 7030 | **hung** | 1 | 150.37 | 8.676844 | 🔵 low — common in general English | - | - | — |
| 7031 | **inviting** | 1 | 150.37 | 8.676844 | 🔵 low — common in general English | - | - | — |
| 7032 | **dragging** | 1 | 150.37 | 8.676844 | 🔵 low — common in general English | - | - | — |
| 7033 | **theme** | 1 | 150.37 | 8.676844 | 🔵 low — common in general English | - | - | — |
| 7034 | **reciprocal** | 1 | 150.37 | 8.676844 | 🔵 low — common in general English | - | - | — |
| 7035 | **individually** | 1 | 150.37 | 8.676844 | 🔵 low — common in general English | - | - | — |
| 7036 | **flank** | 1 | 150.37 | 8.676844 | 🔵 low — common in general English | - | - | — |
| 7037 | **fatty** | 1 | 150.37 | 8.676844 | 🔵 low — common in general English | - | - | — |
| 7038 | **ablaze** | 1 | 150.37 | 8.676844 | 🔵 low — common in general English | - | - | — |
| 7039 | **catapulted** | 1 | 150.37 | 8.676844 | 🔵 low — common in general English | - | - | — |
| 7040 | **dom** | 1 | 150.37 | 8.676844 | 🔵 low — common in general English | - | - | — |
| 7041 | **waited** | 1 | 150.37 | 8.676844 | 🔵 low — common in general English | - | - | — |
| 7042 | **prejudice** | 1 | 150.37 | 8.676844 | 🔵 low — common in general English | - | - | — |
| 7043 | **relaxing** | 1 | 150.37 | 8.676844 | 🔵 low — common in general English | - | - | — |
| 7044 | **annoyed** | 1 | 150.37 | 8.676844 | 🔵 low — common in general English | - | - | — |
| 7045 | **grazing** | 1 | 150.37 | 8.676844 | 🔵 low — common in general English | - | - | — |
| 7046 | **honesty** | 1 | 150.37 | 8.676844 | 🔵 low — common in general English | - | - | — |
| 7047 | **prudence** | 1 | 150.37 | 8.676844 | 🔵 low — common in general English | - | - | — |
| 7048 | **ted** | 1 | 150.37 | 8.676844 | 🔵 low — common in general English | - | - | — |
| 7049 | **sponsor** | 1 | 150.37 | 8.676844 | 🔵 low — common in general English | - | - | — |
| 7050 | **ideally** | 1 | 150.37 | 8.676844 | 🔵 low — common in general English | - | - | — |
| 7051 | **gravel** | 1 | 150.37 | 8.676844 | 🔵 low — common in general English | - | - | — |
| 7052 | **feasible** | 1 | 150.37 | 8.676844 | 🔵 low — common in general English | - | - | — |
| 7053 | **noticeable** | 1 | 150.37 | 8.676844 | 🔵 low — common in general English | - | - | — |
| 7054 | **tenth** | 1 | 150.37 | 8.676844 | 🔵 low — common in general English | - | - | — |
| 7055 | **sara** | 1 | 150.37 | 8.676844 | 🔵 low — common in general English | - | - | — |
| 7056 | **surpassing** | 1 | 150.37 | 8.676844 | 🔵 low — common in general English | - | - | — |
| 7057 | **unrealized** | 1 | 150.37 | 8.676844 | 🔵 low — common in general English | - | - | — |
| 7058 | **omitted** | 1 | 150.37 | 8.676844 | 🔵 low — common in general English | - | - | — |
| 7059 | **collected** | 1 | 150.37 | 8.676844 | 🔵 low — common in general English | - | - | — |
| 7060 | **demand** | 2 | 147.75 | 4.262835 | 🔵 low — common in general English | - | - | — |
| 7061 | **encountered** | 1 | 147.21 | 8.494523 | 🔵 low — common in general English | - | - | — |
| 7062 | **entrance** | 1 | 147.21 | 8.494523 | 🔵 low — common in general English | - | - | — |
| 7063 | **analyze** | 1 | 147.21 | 8.494523 | 🔵 low — common in general English | - | - | — |
| 7064 | **span** | 1 | 147.21 | 8.494523 | 🔵 low — common in general English | - | - | — |
| 7065 | **reassure** | 1 | 147.21 | 8.494523 | 🔵 low — common in general English | - | - | — |
| 7066 | **suspected** | 1 | 147.21 | 8.494523 | 🔵 low — common in general English | - | - | — |
| 7067 | **flurry** | 1 | 147.21 | 8.494523 | 🔵 low — common in general English | - | - | — |
| 7068 | **hal** | 1 | 147.21 | 8.494523 | 🔵 low — common in general English | - | - | — |
| 7069 | **herd** | 1 | 147.21 | 8.494523 | 🔵 low — common in general English | - | - | — |
| 7070 | **rescued** | 1 | 147.21 | 8.494523 | 🔵 low — common in general English | - | - | — |
| 7071 | **employing** | 1 | 147.21 | 8.494523 | 🔵 low — common in general English | - | - | — |
| 7072 | **intensity** | 1 | 147.21 | 8.494523 | 🔵 low — common in general English | - | - | — |
| 7073 | **fox** | 1 | 147.21 | 8.494523 | 🔵 low — common in general English | - | - | — |
| 7074 | **lapse** | 1 | 147.21 | 8.494523 | 🔵 low — common in general English | - | - | — |
| 7075 | **reception** | 1 | 147.21 | 8.494523 | 🔵 low — common in general English | - | - | — |
| 7076 | **practically** | 1 | 147.21 | 8.494523 | 🔵 low — common in general English | - | - | — |
| 7077 | **thoroughly** | 1 | 147.21 | 8.494523 | 🔵 low — common in general English | - | - | — |
| 7078 | **improper** | 1 | 147.21 | 8.494523 | 🔵 low — common in general English | - | - | — |
| 7079 | **landed** | 1 | 147.21 | 8.494523 | 🔵 low — common in general English | - | - | — |
| 7080 | **dormant** | 1 | 147.21 | 8.494523 | 🔵 low — common in general English | - | - | — |
| 7081 | **cooling** | 1 | 147.21 | 8.494523 | 🔵 low — common in general English | - | - | — |
| 7082 | **conform** | 1 | 147.21 | 8.494523 | 🔵 low — common in general English | - | - | — |
| 7083 | **complaining** | 1 | 147.21 | 8.494523 | 🔵 low — common in general English | - | - | — |
| 7084 | **enquiry** | 1 | 147.21 | 8.494523 | 🔵 low — common in general English | - | - | — |
| 7085 | **fetch** | 1 | 147.21 | 8.494523 | 🔵 low — common in general English | - | - | — |
| 7086 | **sail** | 1 | 147.21 | 8.494523 | 🔵 low — common in general English | - | - | — |
| 7087 | **caterpillar** | 1 | 147.21 | 8.494523 | 🔵 low — common in general English | - | - | — |
| 7088 | **occurrence** | 1 | 147.21 | 8.494523 | 🔵 low — common in general English | - | - | — |
| 7089 | **urgently** | 1 | 147.21 | 8.494523 | 🔵 low — common in general English | - | - | — |
| 7090 | **lean** | 1 | 147.21 | 8.494523 | 🔵 low — common in general English | - | - | — |
| 7091 | **brass** | 1 | 147.21 | 8.494523 | 🔵 low — common in general English | - | - | — |
| 7092 | **alternatively** | 1 | 147.21 | 8.494523 | 🔵 low — common in general English | - | - | — |
| 7093 | **absorbing** | 1 | 147.21 | 8.494523 | 🔵 low — common in general English | - | - | — |
| 7094 | **conversation** | 1 | 147.21 | 8.494523 | 🔵 low — common in general English | - | - | — |
| 7095 | **debated** | 1 | 147.21 | 8.494523 | 🔵 low — common in general English | - | - | — |
| 7096 | **vague** | 1 | 144.54 | 8.340372 | 🔵 low — common in general English | - | - | — |
| 7097 | **slipping** | 1 | 144.54 | 8.340372 | 🔵 low — common in general English | - | - | — |
| 7098 | **collectively** | 1 | 144.54 | 8.340372 | 🔵 low — common in general English | - | - | — |
| 7099 | **unwelcome** | 1 | 144.54 | 8.340372 | 🔵 low — common in general English | - | - | — |
| 7100 | **depression** | 1 | 144.54 | 8.340372 | 🔵 low — common in general English | - | - | — |
| 7101 | **liquor** | 1 | 144.54 | 8.340372 | 🔵 low — common in general English | - | - | — |
| 7102 | **counterpart** | 1 | 144.54 | 8.340372 | 🔵 low — common in general English | - | - | — |
| 7103 | **restriction** | 1 | 144.54 | 8.340372 | 🔵 low — common in general English | - | - | — |
| 7104 | **gravity** | 1 | 144.54 | 8.340372 | 🔵 low — common in general English | - | - | — |
| 7105 | **heaviest** | 1 | 144.54 | 8.340372 | 🔵 low — common in general English | - | - | — |
| 7106 | **outweighed** | 1 | 144.54 | 8.340372 | 🔵 low — common in general English | - | - | — |
| 7107 | **bleak** | 1 | 144.54 | 8.340372 | 🔵 low — common in general English | - | - | — |
| 7108 | **invisible** | 1 | 144.54 | 8.340372 | 🔵 low — common in general English | - | - | — |
| 7109 | **adopting** | 1 | 144.54 | 8.340372 | 🔵 low — common in general English | - | - | — |
| 7110 | **draining** | 1 | 144.54 | 8.340372 | 🔵 low — common in general English | - | - | — |
| 7111 | **negatively** | 1 | 144.54 | 8.340372 | 🔵 low — common in general English | - | - | — |
| 7112 | **upheld** | 1 | 144.54 | 8.340372 | 🔵 low — common in general English | - | - | — |
| 7113 | **lightning** | 1 | 144.54 | 8.340372 | 🔵 low — common in general English | - | - | — |
| 7114 | **penalty** | 1 | 144.54 | 8.340372 | 🔵 low — common in general English | - | - | — |
| 7115 | **wing** | 1 | 144.54 | 8.340372 | 🔵 low — common in general English | - | - | — |
| 7116 | **mixture** | 1 | 144.54 | 8.340372 | 🔵 low — common in general English | - | - | — |
| 7117 | **diminished** | 1 | 144.54 | 8.340372 | 🔵 low — common in general English | - | - | — |
| 7118 | **lent** | 1 | 144.54 | 8.340372 | 🔵 low — common in general English | - | - | — |
| 7119 | **spinning** | 1 | 144.54 | 8.340372 | 🔵 low — common in general English | - | - | — |
| 7120 | **transporting** | 1 | 144.54 | 8.340372 | 🔵 low — common in general English | - | - | — |
| 7121 | **rot** | 1 | 144.54 | 8.340372 | 🔵 low — common in general English | - | - | — |
| 7122 | **dram** | 1 | 144.54 | 8.340372 | 🔵 low — common in general English | - | - | — |
| 7123 | **occupied** | 1 | 144.54 | 8.340372 | 🔵 low — common in general English | - | - | — |
| 7124 | **admit** | 1 | 144.54 | 8.340372 | 🔵 low — common in general English | - | - | — |
| 7125 | **goldsmith** | 1 | 144.54 | 8.340372 | 🔵 low — common in general English | - | - | — |
| 7126 | **umbrella** | 1 | 144.54 | 8.340372 | 🔵 low — common in general English | - | - | — |
| 7127 | **tube** | 1 | 144.54 | 8.340372 | 🔵 low — common in general English | - | - | — |
| 7128 | **intangible** | 1 | 144.54 | 8.340372 | 🔵 low — common in general English | - | - | — |
| 7129 | **sunshine** | 1 | 144.54 | 8.340372 | 🔵 low — common in general English | - | - | — |
| 7130 | **north-west** | 1 | 144.54 | 8.340372 | 🔵 low — common in general English | - | - | — |
| 7131 | **ensuring** | 1 | 144.54 | 8.340372 | 🔵 low — common in general English | - | - | — |
| 7132 | **rod** | 1 | 144.54 | 8.340372 | 🔵 low — common in general English | - | - | — |
| 7133 | **chicken** | 1 | 144.54 | 8.340372 | 🔵 low — common in general English | - | - | — |
| 7134 | **unaffected** | 1 | 144.54 | 8.340372 | 🔵 low — common in general English | - | - | — |
| 7135 | **differ** | 1 | 144.54 | 8.340372 | 🔵 low — common in general English | - | - | — |
| 7136 | **duration** | 1 | 144.54 | 8.340372 | 🔵 low — common in general English | - | - | — |
| 7137 | **abu** | 1 | 144.54 | 8.340372 | 🔵 low — common in general English | - | - | — |
| 7138 | **increased** | 2 | 143.79 | 4.148555 | 🔵 low — common in general English | - | - | — |
| 7139 | **domestic** | 2 | 143.42 | 4.137814 | 🔵 low — common in general English | - | - | — |
| 7140 | **sounded** | 1 | 142.22 | 8.206841 | 🔵 low — common in general English | - | - | — |
| 7141 | **enthusiasm** | 1 | 142.22 | 8.206841 | 🔵 low — common in general English | - | - | — |
| 7142 | **reputation** | 1 | 142.22 | 8.206841 | 🔵 low — common in general English | - | - | — |
| 7143 | **demonstrate** | 1 | 142.22 | 8.206841 | 🔵 low — common in general English | - | - | — |
| 7144 | **reliable** | 1 | 142.22 | 8.206841 | 🔵 low — common in general English | - | - | — |
| 7145 | **pack** | 1 | 142.22 | 8.206841 | 🔵 low — common in general English | - | - | — |
| 7146 | **stuck** | 1 | 142.22 | 8.206841 | 🔵 low — common in general English | - | - | — |
| 7147 | **fate** | 1 | 142.22 | 8.206841 | 🔵 low — common in general English | - | - | — |
| 7148 | **endanger** | 1 | 142.22 | 8.206841 | 🔵 low — common in general English | - | - | — |
| 7149 | **diversion** | 1 | 142.22 | 8.206841 | 🔵 low — common in general English | - | - | — |
| 7150 | **pleas** | 1 | 142.22 | 8.206841 | 🔵 low — common in general English | - | - | — |
| 7151 | **softer** | 1 | 142.22 | 8.206841 | 🔵 low — common in general English | - | - | — |
| 7152 | **concentrating** | 1 | 142.22 | 8.206841 | 🔵 low — common in general English | - | - | — |
| 7153 | **shifted** | 1 | 142.22 | 8.206841 | 🔵 low — common in general English | - | - | — |
| 7154 | **hazardous** | 1 | 142.22 | 8.206841 | 🔵 low — common in general English | - | - | — |
| 7155 | **label** | 1 | 142.22 | 8.206841 | 🔵 low — common in general English | - | - | — |
| 7156 | **interference** | 1 | 142.22 | 8.206841 | 🔵 low — common in general English | - | - | — |
| 7157 | **directive** | 1 | 142.22 | 8.206841 | 🔵 low — common in general English | - | - | — |
| 7158 | **distributing** | 1 | 142.22 | 8.206841 | 🔵 low — common in general English | - | - | — |
| 7159 | **grip** | 1 | 142.22 | 8.206841 | 🔵 low — common in general English | - | - | — |
| 7160 | **mercury** | 1 | 142.22 | 8.206841 | 🔵 low — common in general English | - | - | — |
| 7161 | **finish** | 1 | 142.22 | 8.206841 | 🔵 low — common in general English | 0.107895 | - | — |
| 7162 | **readily** | 1 | 142.22 | 8.206841 | 🔵 low — common in general English | - | - | — |
| 7163 | **lessening** | 1 | 142.22 | 8.206841 | 🔵 low — common in general English | - | - | — |
| 7164 | **desired** | 1 | 142.22 | 8.206841 | 🔵 low — common in general English | - | - | — |
| 7165 | **necessity** | 1 | 142.22 | 8.206841 | 🔵 low — common in general English | - | - | — |
| 7166 | **impatience** | 1 | 142.22 | 8.206841 | 🔵 low — common in general English | - | - | — |
| 7167 | **intelligent** | 1 | 142.22 | 8.206841 | 🔵 low — common in general English | - | - | — |
| 7168 | **pronounced** | 1 | 142.22 | 8.206841 | 🔵 low — common in general English | - | - | — |
| 7169 | **deter** | 1 | 142.22 | 8.206841 | 🔵 low — common in general English | - | - | — |
| 7170 | **agriculture** | 2 | 141.61 | 4.085773 | 🔵 low — common in general English | - | - | — |
| 7171 | **player** | 1 | 140.18 | 8.089058 | 🔵 low — common in general English | - | - | — |
| 7172 | **relaxation** | 1 | 140.18 | 8.089058 | 🔵 low — common in general English | - | - | — |
| 7173 | **dominate** | 1 | 140.18 | 8.089058 | 🔵 low — common in general English | - | - | — |
| 7174 | **proof** | 1 | 140.18 | 8.089058 | 🔵 low — common in general English | - | - | — |
| 7175 | **matching** | 1 | 140.18 | 8.089058 | 🔵 low — common in general English | - | - | — |
| 7176 | **unexpectedly** | 1 | 140.18 | 8.089058 | 🔵 low — common in general English | - | - | — |
| 7177 | **revived** | 1 | 140.18 | 8.089058 | 🔵 low — common in general English | - | - | — |
| 7178 | **supplementary** | 1 | 140.18 | 8.089058 | 🔵 low — common in general English | - | - | — |
| 7179 | **ridiculous** | 1 | 140.18 | 8.089058 | 🔵 low — common in general English | - | - | — |
| 7180 | **steer** | 1 | 140.18 | 8.089058 | 🔵 low — common in general English | - | - | — |
| 7181 | **chart** | 1 | 140.18 | 8.089058 | 🔵 low — common in general English | - | - | — |
| 7182 | **familiar** | 1 | 140.18 | 8.089058 | 🔵 low — common in general English | - | - | — |
| 7183 | **rigid** | 1 | 140.18 | 8.089058 | 🔵 low — common in general English | - | - | — |
| 7184 | **desperate** | 1 | 140.18 | 8.089058 | 🔵 low — common in general English | - | - | — |
| 7185 | **page** | 1 | 140.18 | 8.089058 | 🔵 low — common in general English | - | - | — |
| 7186 | **dealt** | 1 | 140.18 | 8.089058 | 🔵 low — common in general English | - | - | — |
| 7187 | **attacking** | 1 | 140.18 | 8.089058 | 🔵 low — common in general English | - | - | — |
| 7188 | **clouded** | 1 | 140.18 | 8.089058 | 🔵 low — common in general English | - | - | — |
| 7189 | **hitting** | 1 | 140.18 | 8.089058 | 🔵 low — common in general English | - | - | — |
| 7190 | **wiped** | 1 | 140.18 | 8.089058 | 🔵 low — common in general English | - | - | — |
| 7191 | **inclined** | 1 | 140.18 | 8.089058 | 🔵 low — common in general English | - | - | — |
| 7192 | **leaf** | 1 | 140.18 | 8.089058 | 🔵 low — common in general English | - | - | — |
| 7193 | **insist** | 1 | 140.18 | 8.089058 | 🔵 low — common in general English | 0.231806 | - | — |
| 7194 | **grossly** | 1 | 140.18 | 8.089058 | 🔵 low — common in general English | - | - | — |
| 7195 | **spurred** | 1 | 140.18 | 8.089058 | 🔵 low — common in general English | - | - | — |
| 7196 | **clarify** | 1 | 140.18 | 8.089058 | 🔵 low — common in general English | - | - | — |
| 7197 | **intellectual** | 1 | 140.18 | 8.089058 | 🔵 low — common in general English | - | - | — |
| 7198 | **indebted** | 1 | 140.18 | 8.089058 | 🔵 low — common in general English | - | - | — |
| 7199 | **borrowed** | 1 | 140.18 | 8.089058 | 🔵 low — common in general English | - | - | — |
| 7200 | **lacked** | 1 | 140.18 | 8.089058 | 🔵 low — common in general English | - | - | — |
| 7201 | **stretching** | 1 | 140.18 | 8.089058 | 🔵 low — common in general English | - | - | — |
| 7202 | **funeral** | 1 | 140.18 | 8.089058 | 🔵 low — common in general English | - | - | — |
| 7203 | **solved** | 1 | 140.18 | 8.089058 | 🔵 low — common in general English | - | - | — |
| 7204 | **mutually** | 1 | 138.36 | 7.983697 | 🔵 low — common in general English | - | - | — |
| 7205 | **anchor** | 1 | 138.36 | 7.983697 | 🔵 low — common in general English | - | - | — |
| 7206 | **collective** | 1 | 138.36 | 7.983697 | 🔵 low — common in general English | - | - | — |
| 7207 | **shed** | 1 | 138.36 | 7.983697 | 🔵 low — common in general English | - | - | — |
| 7208 | **withdrawing** | 1 | 138.36 | 7.983697 | 🔵 low — common in general English | - | - | — |
| 7209 | **multiple** | 1 | 138.36 | 7.983697 | 🔵 low — common in general English | - | - | — |
| 7210 | **pan** | 1 | 138.36 | 7.983697 | 🔵 low — common in general English | - | - | — |
| 7211 | **varying** | 1 | 138.36 | 7.983697 | 🔵 low — common in general English | - | - | — |
| 7212 | **prominent** | 1 | 138.36 | 7.983697 | 🔵 low — common in general English | - | - | — |
| 7213 | **prop** | 1 | 138.36 | 7.983697 | 🔵 low — common in general English | - | - | — |
| 7214 | **pointing** | 1 | 138.36 | 7.983697 | 🔵 low — common in general English | - | - | — |
| 7215 | **thwart** | 1 | 138.36 | 7.983697 | 🔵 low — common in general English | - | - | — |
| 7216 | **evident** | 1 | 138.36 | 7.983697 | 🔵 low — common in general English | - | - | — |
| 7217 | **examined** | 1 | 138.36 | 7.983697 | 🔵 low — common in general English | - | - | — |
| 7218 | **nearing** | 1 | 138.36 | 7.983697 | 🔵 low — common in general English | - | - | — |
| 7219 | **obliged** | 1 | 138.36 | 7.983697 | 🔵 low — common in general English | - | - | — |
| 7220 | **extract** | 1 | 138.36 | 7.983697 | 🔵 low — common in general English | - | - | — |
| 7221 | **plate** | 1 | 138.36 | 7.983697 | 🔵 low — common in general English | - | - | — |
| 7222 | **persist** | 1 | 138.36 | 7.983697 | 🔵 low — common in general English | - | - | — |
| 7223 | **subscribe** | 1 | 138.36 | 7.983697 | 🔵 low — common in general English | - | - | — |
| 7224 | **unwanted** | 1 | 138.36 | 7.983697 | 🔵 low — common in general English | - | - | — |
| 7225 | **incorrect** | 1 | 138.36 | 7.983697 | 🔵 low — common in general English | - | - | — |
| 7226 | **turmoil** | 1 | 136.70 | 7.888387 | 🔵 low — common in general English | - | - | — |
| 7227 | **dominated** | 1 | 136.70 | 7.888387 | 🔵 low — common in general English | - | - | — |
| 7228 | **creek** | 1 | 136.70 | 7.888387 | 🔵 low — common in general English | - | - | — |
| 7229 | **fought** | 1 | 136.70 | 7.888387 | 🔵 low — common in general English | - | - | — |
| 7230 | **removing** | 1 | 136.70 | 7.888387 | 🔵 low — common in general English | - | - | — |
| 7231 | **preceding** | 1 | 136.70 | 7.888387 | 🔵 low — common in general English | - | - | — |
| 7232 | **calculation** | 1 | 136.70 | 7.888387 | 🔵 low — common in general English | - | - | — |
| 7233 | **disastrous** | 1 | 136.70 | 7.888387 | 🔵 low — common in general English | - | - | — |
| 7234 | **warranted** | 1 | 136.70 | 7.888387 | 🔵 low — common in general English | - | - | — |
| 7235 | **warn** | 1 | 136.70 | 7.888387 | 🔵 low — common in general English | - | - | — |
| 7236 | **austerity** | 1 | 136.70 | 7.888387 | 🔵 low — common in general English | - | - | — |
| 7237 | **modestly** | 1 | 136.70 | 7.888387 | 🔵 low — common in general English | - | - | — |
| 7238 | **limitation** | 1 | 136.70 | 7.888387 | 🔵 low — common in general English | - | - | — |
| 7239 | **worthwhile** | 1 | 136.70 | 7.888387 | 🔵 low — common in general English | - | - | — |
| 7240 | **halting** | 1 | 136.70 | 7.888387 | 🔵 low — common in general English | - | - | — |
| 7241 | **departure** | 1 | 136.70 | 7.888387 | 🔵 low — common in general English | - | - | — |
| 7242 | **persistent** | 1 | 136.70 | 7.888387 | 🔵 low — common in general English | - | - | — |
| 7243 | **revealed** | 1 | 135.20 | 7.801376 | 🔵 low — common in general English | - | - | — |
| 7244 | **topic** | 1 | 135.20 | 7.801376 | 🔵 low — common in general English | - | - | — |
| 7245 | **miss** | 1 | 135.20 | 7.801376 | 🔵 low — common in general English | 0.179528 | - | — |
| 7246 | **dictate** | 1 | 135.20 | 7.801376 | 🔵 low — common in general English | - | - | — |
| 7247 | **prohibited** | 1 | 135.20 | 7.801376 | 🔵 low — common in general English | - | - | — |
| 7248 | **misleading** | 1 | 135.20 | 7.801376 | 🔵 low — common in general English | - | - | — |
| 7249 | **mood** | 1 | 135.20 | 7.801376 | 🔵 low — common in general English | - | - | — |
| 7250 | **purely** | 1 | 135.20 | 7.801376 | 🔵 low — common in general English | - | - | — |
| 7251 | **essentially** | 1 | 135.20 | 7.801376 | 🔵 low — common in general English | - | - | — |
| 7252 | **restrain** | 1 | 135.20 | 7.801376 | 🔵 low — common in general English | - | - | — |
| 7253 | **stemming** | 1 | 135.20 | 7.801376 | 🔵 low — common in general English | - | - | — |
| 7254 | **hall** | 1 | 135.20 | 7.801376 | 🔵 low — common in general English | - | - | — |
| 7255 | **tended** | 1 | 135.20 | 7.801376 | 🔵 low — common in general English | - | - | — |
| 7256 | **adapt** | 1 | 135.20 | 7.801376 | 🔵 low — common in general English | - | - | — |
| 7257 | **rolling** | 1 | 135.20 | 7.801376 | 🔵 low — common in general English | - | - | — |
| 7258 | **claiming** | 1 | 135.20 | 7.801376 | 🔵 low — common in general English | - | - | — |
| 7259 | **consequently** | 1 | 135.20 | 7.801376 | 🔵 low — common in general English | - | - | — |
| 7260 | **crew** | 1 | 135.20 | 7.801376 | 🔵 low — common in general English | - | - | — |
| 7261 | **soaring** | 1 | 135.20 | 7.801376 | 🔵 low — common in general English | - | - | — |
| 7262 | **classified** | 1 | 135.20 | 7.801376 | 🔵 low — common in general English | - | - | — |
| 7263 | **describing** | 1 | 135.20 | 7.801376 | 🔵 low — common in general English | - | - | — |
| 7264 | **wash** | 1 | 135.20 | 7.801376 | 🔵 low — common in general English | 0.232066 | - | — |
| 7265 | **unstable** | 1 | 135.20 | 7.801376 | 🔵 low — common in general English | - | - | — |
| 7266 | **recording** | 1 | 135.20 | 7.801376 | 🔵 low — common in general English | - | - | — |
| 7267 | **forming** | 1 | 133.81 | 7.721333 | 🔵 low — common in general English | - | - | — |
| 7268 | **revive** | 1 | 133.81 | 7.721333 | 🔵 low — common in general English | - | - | — |
| 7269 | **location** | 1 | 133.81 | 7.721333 | 🔵 low — common in general English | - | - | — |
| 7270 | **sceptical** | 1 | 133.81 | 7.721333 | 🔵 low — common in general English | - | - | — |
| 7271 | **opposing** | 1 | 133.81 | 7.721333 | 🔵 low — common in general English | - | - | — |
| 7272 | **combining** | 1 | 133.81 | 7.721333 | 🔵 low — common in general English | - | - | — |
| 7273 | **composite** | 1 | 133.81 | 7.721333 | 🔵 low — common in general English | - | - | — |
| 7274 | **ideal** | 1 | 133.81 | 7.721333 | 🔵 low — common in general English | - | - | — |
| 7275 | **modify** | 1 | 133.81 | 7.721333 | 🔵 low — common in general English | - | - | — |
| 7276 | **repaying** | 1 | 133.81 | 7.721333 | 🔵 low — common in general English | - | - | — |
| 7277 | **cake** | 1 | 133.81 | 7.721333 | 🔵 low — common in general English | - | - | — |
| 7278 | **appreciate** | 1 | 133.81 | 7.721333 | 🔵 low — common in general English | - | - | — |
| 7279 | **goodwill** | 1 | 133.81 | 7.721333 | 🔵 low — common in general English | - | - | — |
| 7280 | **substitute** | 1 | 133.81 | 7.721333 | 🔵 low — common in general English | - | - | — |
| 7281 | **interesting** | 1 | 133.81 | 7.721333 | 🔵 low — common in general English | - | - | — |
| 7282 | **mission** | 1 | 133.81 | 7.721333 | 🔵 low — common in general English | - | - | — |
| 7283 | **thin** | 1 | 133.81 | 7.721333 | 🔵 low — common in general English | - | - | — |
| 7284 | **tangible** | 1 | 133.81 | 7.721333 | 🔵 low — common in general English | - | - | — |
| 7285 | **feature** | 1 | 133.81 | 7.721333 | 🔵 low — common in general English | - | - | — |
| 7286 | **destination** | 1 | 133.81 | 7.721333 | 🔵 low — common in general English | - | - | — |
| 7287 | **dot** | 1 | 133.81 | 7.721333 | 🔵 low — common in general English | - | - | — |
| 7288 | **played** | 1 | 132.53 | 7.647225 | 🔵 low — common in general English | - | - | — |
| 7289 | **thereby** | 1 | 132.53 | 7.647225 | 🔵 low — common in general English | - | - | — |
| 7290 | **weaken** | 1 | 132.53 | 7.647225 | 🔵 low — common in general English | - | - | — |
| 7291 | **remark** | 1 | 132.53 | 7.647225 | 🔵 low — common in general English | - | - | — |
| 7292 | **blame** | 1 | 132.53 | 7.647225 | 🔵 low — common in general English | - | - | — |
| 7293 | **accompanying** | 1 | 132.53 | 7.647225 | 🔵 low — common in general English | - | - | — |
| 7294 | **asa** | 1 | 132.53 | 7.647225 | 🔵 low — common in general English | - | - | — |
| 7295 | **dipped** | 1 | 132.53 | 7.647225 | 🔵 low — common in general English | - | - | — |
| 7296 | **professor** | 1 | 132.53 | 7.647225 | 🔵 low — common in general English | - | - | — |
| 7297 | **reacted** | 1 | 132.53 | 7.647225 | 🔵 low — common in general English | - | - | — |
| 7298 | **thereafter** | 1 | 132.53 | 7.647225 | 🔵 low — common in general English | - | - | — |
| 7299 | **game** | 1 | 132.53 | 7.647225 | 🔵 low — common in general English | - | - | — |
| 7300 | **exclusively** | 1 | 132.53 | 7.647225 | 🔵 low — common in general English | - | - | — |
| 7301 | **chosen** | 1 | 132.53 | 7.647225 | 🔵 low — common in general English | - | - | — |
| 7302 | **motion** | 1 | 132.53 | 7.647225 | 🔵 low — common in general English | - | - | — |
| 7303 | **testing** | 1 | 131.33 | 7.578232 | 🔵 low — common in general English | - | - | — |
| 7304 | **stored** | 1 | 131.33 | 7.578232 | 🔵 low — common in general English | - | - | — |
| 7305 | **mer** | 1 | 131.33 | 7.578232 | 🔵 low — common in general English | - | - | — |
| 7306 | **justified** | 1 | 131.33 | 7.578232 | 🔵 low — common in general English | - | - | — |
| 7307 | **rated** | 1 | 131.33 | 7.578232 | 🔵 low — common in general English | - | - | — |
| 7308 | **candidate** | 1 | 131.33 | 7.578232 | 🔵 low — common in general English | - | - | — |
| 7309 | **challenged** | 1 | 131.33 | 7.578232 | 🔵 low — common in general English | - | - | — |
| 7310 | **seller** | 1 | 131.33 | 7.578232 | 🔵 low — common in general English | - | - | — |
| 7311 | **revolving** | 1 | 131.33 | 7.578232 | 🔵 low — common in general English | - | - | — |
| 7312 | **interpreted** | 1 | 131.33 | 7.578232 | 🔵 low — common in general English | - | - | — |
| 7313 | **sending** | 1 | 131.33 | 7.578232 | 🔵 low — common in general English | - | - | — |
| 7314 | **declare** | 1 | 130.21 | 7.513694 | 🔵 low — common in general English | 0.182648 | - | — |
| 7315 | **driving** | 1 | 130.21 | 7.513694 | 🔵 low — common in general English | - | - | — |
| 7316 | **comprise** | 1 | 130.21 | 7.513694 | 🔵 low — common in general English | - | - | — |
| 7317 | **inevitable** | 1 | 130.21 | 7.513694 | 🔵 low — common in general English | - | - | — |
| 7318 | **ferry** | 1 | 130.21 | 7.513694 | 🔵 low — common in general English | - | - | — |
| 7319 | **undertaken** | 1 | 130.21 | 7.513694 | 🔵 low — common in general English | - | - | — |
| 7320 | **coin** | 1 | 130.21 | 7.513694 | 🔵 low — common in general English | - | - | — |
| 7321 | **mild** | 1 | 130.21 | 7.513694 | 🔵 low — common in general English | - | - | — |
| 7322 | **wary** | 1 | 130.21 | 7.513694 | 🔵 low — common in general English | - | - | — |
| 7323 | **emerging** | 1 | 130.21 | 7.513694 | 🔵 low — common in general English | - | - | — |
| 7324 | **obligation** | 1 | 130.21 | 7.513694 | 🔵 low — common in general English | - | - | — |
| 7325 | **worry** | 1 | 130.21 | 7.513694 | 🔵 low — common in general English | - | - | — |
| 7326 | **unlike** | 1 | 130.21 | 7.513694 | 🔵 low — common in general English | - | - | — |
| 7327 | **soil** | 1 | 130.21 | 7.513694 | 🔵 low — common in general English | - | - | — |
| 7328 | **sale** | 2 | 129.81 | 3.745252 | 🔵 low — common in general English | - | - | — |
| 7329 | **decree** | 1 | 129.16 | 7.453069 | 🔵 low — common in general English | - | - | — |
| 7330 | **historical** | 1 | 129.16 | 7.453069 | 🔵 low — common in general English | - | - | — |
| 7331 | **calculating** | 1 | 129.16 | 7.453069 | 🔵 low — common in general English | - | - | — |
| 7332 | **sharing** | 1 | 129.16 | 7.453069 | 🔵 low — common in general English | - | - | — |
| 7333 | **assessment** | 1 | 129.16 | 7.453069 | 🔵 low — common in general English | - | - | — |
| 7334 | **regularly** | 1 | 129.16 | 7.453069 | 🔵 low — common in general English | - | - | — |
| 7335 | **reacting** | 1 | 129.16 | 7.453069 | 🔵 low — common in general English | - | - | — |
| 7336 | **farming** | 1 | 129.16 | 7.453069 | 🔵 low — common in general English | - | - | — |
| 7337 | **rejection** | 1 | 129.16 | 7.453069 | 🔵 low — common in general English | - | - | — |
| 7338 | **imposing** | 1 | 128.17 | 7.395911 | 🔵 low — common in general English | - | - | — |
| 7339 | **obvious** | 1 | 128.17 | 7.395911 | 🔵 low — common in general English | - | - | — |
| 7340 | **permission** | 1 | 128.17 | 7.395911 | 🔵 low — common in general English | - | - | — |
| 7341 | **fix** | 1 | 128.17 | 7.395911 | 🔵 low — common in general English | - | - | — |
| 7342 | **procedure** | 1 | 128.17 | 7.395911 | 🔵 low — common in general English | - | - | — |
| 7343 | **demanded** | 1 | 128.17 | 7.395911 | 🔵 low — common in general English | - | - | — |
| 7344 | **convince** | 1 | 128.17 | 7.395911 | 🔵 low — common in general English | 0.082998 | - | — |
| 7345 | **secondary** | 1 | 128.17 | 7.395911 | 🔵 low — common in general English | - | - | — |
| 7346 | **apparel** | 1 | 128.17 | 7.395911 | 🔵 low — common in general English | - | - | — |
| 7347 | **society** | 1 | 128.17 | 7.395911 | 🔵 low — common in general English | - | - | — |
| 7348 | **lesser** | 1 | 128.17 | 7.395911 | 🔵 low — common in general English | - | - | — |
| 7349 | **ali** | 1 | 127.23 | 7.341843 | 🔵 low — common in general English | - | - | — |
| 7350 | **bob** | 1 | 127.23 | 7.341843 | 🔵 low — common in general English | - | - | — |
| 7351 | **milling** | 1 | 127.23 | 7.341843 | 🔵 low — common in general English | - | - | — |
| 7352 | **returning** | 1 | 127.23 | 7.341843 | 🔵 low — common in general English | - | - | — |
| 7353 | **handle** | 1 | 127.23 | 7.341843 | 🔵 low — common in general English | - | - | — |
| 7354 | **consent** | 1 | 127.23 | 7.341843 | 🔵 low — common in general English | - | - | — |
| 7355 | **evaluating** | 1 | 127.23 | 7.341843 | 🔵 low — common in general English | - | - | — |
| 7356 | **hurting** | 1 | 127.23 | 7.341843 | 🔵 low — common in general English | - | - | — |
| 7357 | **sensitive** | 1 | 127.23 | 7.341843 | 🔵 low — common in general English | - | - | — |
| 7358 | **judge** | 1 | 127.23 | 7.341843 | 🔵 low — common in general English | - | - | — |
| 7359 | **version** | 1 | 127.23 | 7.341843 | 🔵 low — common in general English | - | - | — |
| 7360 | **slack** | 1 | 126.34 | 7.29055 | 🔵 low — common in general English | - | - | — |
| 7361 | **favoured** | 1 | 126.34 | 7.29055 | 🔵 low — common in general English | - | - | — |
| 7362 | **quiet** | 1 | 126.34 | 7.29055 | 🔵 low — common in general English | - | - | — |
| 7363 | **mile** | 1 | 126.34 | 7.29055 | 🔵 low — common in general English | - | - | — |
| 7364 | **park** | 1 | 126.34 | 7.29055 | 🔵 low — common in general English | - | - | — |
| 7365 | **arranging** | 1 | 126.34 | 7.29055 | 🔵 low — common in general English | - | - | — |
| 7366 | **limiting** | 1 | 125.50 | 7.24176 | 🔵 low — common in general English | - | - | — |
| 7367 | **ward** | 1 | 125.50 | 7.24176 | 🔵 low — common in general English | - | - | — |
| 7368 | **reversal** | 1 | 125.50 | 7.24176 | 🔵 low — common in general English | - | - | — |
| 7369 | **accident** | 1 | 125.50 | 7.24176 | 🔵 low — common in general English | - | - | — |
| 7370 | **treasurer** | 1 | 125.50 | 7.24176 | 🔵 low — common in general English | - | - | — |
| 7371 | **concerted** | 1 | 125.50 | 7.24176 | 🔵 low — common in general English | - | - | — |
| 7372 | **pressed** | 1 | 125.50 | 7.24176 | 🔵 low — common in general English | - | - | — |
| 7373 | **prevented** | 1 | 125.50 | 7.24176 | 🔵 low — common in general English | - | - | — |
| 7374 | **alter** | 1 | 125.50 | 7.24176 | 🔵 low — common in general English | - | - | — |
| 7375 | **acted** | 1 | 125.50 | 7.24176 | 🔵 low — common in general English | - | - | — |
| 7376 | **evaluation** | 1 | 125.50 | 7.24176 | 🔵 low — common in general English | - | - | — |
| 7377 | **lanka** | 1 | 125.50 | 7.24176 | 🔵 low — common in general English | - | - | — |
| 7378 | **chamber** | 1 | 125.50 | 7.24176 | 🔵 low — common in general English | - | - | — |
| 7379 | **exercised** | 1 | 124.69 | 7.19524 | 🔵 low — common in general English | - | - | — |
| 7380 | **century** | 1 | 124.69 | 7.19524 | 🔵 low — common in general English | - | - | — |
| 7381 | **engine** | 1 | 124.69 | 7.19524 | 🔵 low — common in general English | - | - | — |
| 7382 | **accused** | 1 | 124.69 | 7.19524 | 🔵 low — common in general English | - | - | — |
| 7383 | **criteria** | 1 | 124.69 | 7.19524 | 🔵 low — common in general English | - | - | — |
| 7384 | **track** | 1 | 124.69 | 7.19524 | 🔵 low — common in general English | - | - | — |
| 7385 | **pro** | 1 | 124.69 | 7.19524 | 🔵 low — common in general English | - | - | — |
| 7386 | **distribute** | 1 | 124.69 | 7.19524 | 🔵 low — common in general English | - | - | — |
| 7387 | **challenge** | 1 | 124.69 | 7.19524 | 🔵 low — common in general English | - | - | — |
| 7388 | **instrument** | 1 | 124.69 | 7.19524 | 🔵 low — common in general English | - | - | — |
| 7389 | **cane** | 1 | 123.92 | 7.150788 | 🔵 low — common in general English | - | - | — |
| 7390 | **linking** | 1 | 123.92 | 7.150788 | 🔵 low — common in general English | - | - | — |
| 7391 | **disappointed** | 1 | 123.92 | 7.150788 | 🔵 low — common in general English | - | - | — |
| 7392 | **reject** | 1 | 123.92 | 7.150788 | 🔵 low — common in general English | 0.149318 | - | — |
| 7393 | **defined** | 1 | 123.92 | 7.150788 | 🔵 low — common in general English | - | - | — |
| 7394 | **secured** | 1 | 123.92 | 7.150788 | 🔵 low — common in general English | - | - | — |
| 7395 | **dominion** | 1 | 123.92 | 7.150788 | 🔵 low — common in general English | - | - | — |
| 7396 | **considerably** | 1 | 123.18 | 7.108229 | 🔵 low — common in general English | - | - | — |
| 7397 | **basket** | 1 | 123.18 | 7.108229 | 🔵 low — common in general English | - | - | — |
| 7398 | **preserve** | 1 | 123.18 | 7.108229 | 🔵 low — common in general English | - | - | — |
| 7399 | **entering** | 1 | 122.48 | 7.067407 | 🔵 low — common in general English | - | - | — |
| 7400 | **freeze** | 1 | 122.48 | 7.067407 | 🔵 low — common in general English | - | - | — |
| 7401 | **accelerate** | 1 | 122.48 | 7.067407 | 🔵 low — common in general English | - | - | — |
| 7402 | **negotiation** | 1 | 122.48 | 7.067407 | 🔵 low — common in general English | - | - | — |
| 7403 | **awaiting** | 1 | 122.48 | 7.067407 | 🔵 low — common in general English | - | - | — |
| 7404 | **consuming** | 1 | 122.48 | 7.067407 | 🔵 low — common in general English | - | - | — |
| 7405 | **successfully** | 1 | 122.48 | 7.067407 | 🔵 low — common in general English | - | - | — |
| 7406 | **discovered** | 1 | 122.48 | 7.067407 | 🔵 low — common in general English | - | - | — |
| 7407 | **spur** | 1 | 122.48 | 7.067407 | 🔵 low — common in general English | - | - | — |
| 7408 | **contrast** | 1 | 121.80 | 7.028186 | 🔵 low — common in general English | - | - | — |
| 7409 | **valid** | 1 | 121.80 | 7.028186 | 🔵 low — common in general English | - | - | — |
| 7410 | **participating** | 1 | 121.80 | 7.028186 | 🔵 low — common in general English | - | - | — |
| 7411 | **forcing** | 1 | 121.80 | 7.028186 | 🔵 low — common in general English | - | - | — |
| 7412 | **questioned** | 1 | 121.80 | 7.028186 | 🔵 low — common in general English | - | - | — |
| 7413 | **sixth** | 1 | 121.80 | 7.028186 | 🔵 low — common in general English | - | - | — |
| 7414 | **printing** | 1 | 121.80 | 7.028186 | 🔵 low — common in general English | - | - | — |
| 7415 | **table** | 1 | 121.14 | 6.990446 | 🔵 low — common in general English | - | - | — |
| 7416 | **exact** | 1 | 121.14 | 6.990446 | 🔵 low — common in general English | - | - | — |
| 7417 | **convert** | 1 | 121.14 | 6.990446 | 🔵 low — common in general English | - | - | — |
| 7418 | **qualified** | 1 | 121.14 | 6.990446 | 🔵 low — common in general English | - | - | — |
| 7419 | **window** | 1 | 121.14 | 6.990446 | 🔵 low — common in general English | - | - | — |
| 7420 | **match** | 1 | 120.51 | 6.954078 | 🔵 low — common in general English | - | - | — |
| 7421 | **tighten** | 1 | 120.51 | 6.954078 | 🔵 low — common in general English | - | - | — |
| 7422 | **flour** | 1 | 120.51 | 6.954078 | 🔵 low — common in general English | - | - | — |
| 7423 | **reply** | 1 | 120.51 | 6.954078 | 🔵 low — common in general English | 0.008506 | - | — |
| 7424 | **acceptance** | 1 | 120.51 | 6.954078 | 🔵 low — common in general English | - | - | — |
| 7425 | **scope** | 1 | 120.51 | 6.954078 | 🔵 low — common in general English | - | - | — |
| 7426 | **diamond** | 1 | 119.90 | 6.918987 | 🔵 low — common in general English | - | - | — |
| 7427 | **engaged** | 1 | 119.90 | 6.918987 | 🔵 low — common in general English | - | - | — |
| 7428 | **necessarily** | 1 | 119.90 | 6.918987 | 🔵 low — common in general English | - | - | — |
| 7429 | **soared** | 1 | 119.90 | 6.918987 | 🔵 low — common in general English | - | - | — |
| 7430 | **handling** | 1 | 119.90 | 6.918987 | 🔵 low — common in general English | - | - | — |
| 7431 | **tobacco** | 1 | 119.90 | 6.918987 | 🔵 low — common in general English | - | - | — |
| 7432 | **discussing** | 1 | 119.90 | 6.918987 | 🔵 low — common in general English | - | - | — |
| 7433 | **optimism** | 1 | 119.32 | 6.885085 | 🔵 low — common in general English | - | - | — |
| 7434 | **prevailing** | 1 | 119.32 | 6.885085 | 🔵 low — common in general English | - | - | — |
| 7435 | **expecting** | 1 | 119.32 | 6.885085 | 🔵 low — common in general English | - | - | — |
| 7436 | **critical** | 1 | 119.32 | 6.885085 | 🔵 low — common in general English | - | - | — |
| 7437 | **proceeding** | 1 | 119.32 | 6.885085 | 🔵 low — common in general English | - | - | — |
| 7438 | **conducted** | 1 | 119.32 | 6.885085 | 🔵 low — common in general English | - | - | — |
| 7439 | **respective** | 1 | 119.32 | 6.885085 | 🔵 low — common in general English | - | - | — |
| 7440 | **speed** | 1 | 119.32 | 6.885085 | 🔵 low — common in general English | - | - | — |
| 7441 | **friendly** | 1 | 119.32 | 6.885085 | 🔵 low — common in general English | - | - | — |
| 7442 | **adopt** | 1 | 119.32 | 6.885085 | 🔵 low — common in general English | - | - | — |
| 7443 | **explore** | 1 | 118.75 | 6.852295 | 🔵 low — common in general English | - | - | — |
| 7444 | **tool** | 1 | 118.75 | 6.852295 | 🔵 low — common in general English | - | - | — |
| 7445 | **quick** | 1 | 118.75 | 6.852295 | 🔵 low — common in general English | - | - | — |
| 7446 | **incurred** | 1 | 118.75 | 6.852295 | 🔵 low — common in general English | - | - | — |
| 7447 | **somewhat** | 1 | 118.75 | 6.852295 | 🔵 low — common in general English | - | - | — |
| 7448 | **eliminate** | 1 | 118.75 | 6.852295 | 🔵 low — common in general English | - | - | — |
| 7449 | **settled** | 1 | 118.75 | 6.852295 | 🔵 low — common in general English | - | - | — |
| 7450 | **responding** | 1 | 118.75 | 6.852295 | 🔵 low — common in general English | - | - | — |
| 7451 | **deterioration** | 1 | 118.20 | 6.820546 | 🔵 low — common in general English | - | - | — |
| 7452 | **formula** | 1 | 118.20 | 6.820546 | 🔵 low — common in general English | - | - | — |
| 7453 | **rally** | 1 | 118.20 | 6.820546 | 🔵 low — common in general English | - | - | — |
| 7454 | **steadily** | 1 | 118.20 | 6.820546 | 🔵 low — common in general English | - | - | — |
| 7455 | **flag** | 1 | 118.20 | 6.820546 | 🔵 low — common in general English | - | - | — |
| 7456 | **extensive** | 1 | 118.20 | 6.820546 | 🔵 low — common in general English | - | - | — |
| 7457 | **enhance** | 1 | 117.67 | 6.789775 | 🔵 low — common in general English | - | - | — |
| 7458 | **tightening** | 1 | 117.67 | 6.789775 | 🔵 low — common in general English | - | - | — |
| 7459 | **permanent** | 1 | 117.67 | 6.789775 | 🔵 low — common in general English | - | - | — |
| 7460 | **play** | 1 | 117.67 | 6.789775 | 🔵 low — common in general English | 0.231986 | - | — |
| 7461 | **informed** | 1 | 117.67 | 6.789775 | 🔵 low — common in general English | - | - | — |
| 7462 | **prompted** | 1 | 117.67 | 6.789775 | 🔵 low — common in general English | - | - | — |
| 7463 | **incentive** | 1 | 117.67 | 6.789775 | 🔵 low — common in general English | - | - | — |
| 7464 | **indirect** | 1 | 117.15 | 6.759922 | 🔵 low — common in general English | - | - | — |
| 7465 | **healthy** | 1 | 117.15 | 6.759922 | 🔵 low — common in general English | - | - | — |
| 7466 | **missile** | 1 | 117.15 | 6.759922 | 🔵 low — common in general English | - | - | — |
| 7467 | **reaching** | 1 | 117.15 | 6.759922 | 🔵 low — common in general English | - | - | — |
| 7468 | **southeast** | 1 | 116.65 | 6.730934 | 🔵 low — common in general English | - | - | — |
| 7469 | **withdraw** | 1 | 116.65 | 6.730934 | 🔵 low — common in general English | - | - | — |
| 7470 | **burden** | 1 | 116.65 | 6.730934 | 🔵 low — common in general English | - | - | — |
| 7471 | **maturing** | 1 | 116.16 | 6.702763 | 🔵 low — common in general English | - | - | — |
| 7472 | **merchandise** | 1 | 116.16 | 6.702763 | 🔵 low — common in general English | - | - | — |
| 7473 | **flexible** | 1 | 116.16 | 6.702763 | 🔵 low — common in general English | - | - | — |
| 7474 | **chase** | 1 | 115.68 | 6.675364 | 🔵 low — common in general English | - | - | — |
| 7475 | **reviewing** | 1 | 115.68 | 6.675364 | 🔵 low — common in general English | - | - | — |
| 7476 | **uncertain** | 1 | 115.22 | 6.648696 | 🔵 low — common in general English | - | - | — |
| 7477 | **aggregate** | 1 | 115.22 | 6.648696 | 🔵 low — common in general English | - | - | — |
| 7478 | **southwest** | 1 | 114.77 | 6.622721 | 🔵 low — common in general English | - | - | — |
| 7479 | **northwest** | 1 | 114.77 | 6.622721 | 🔵 low — common in general English | - | - | — |
| 7480 | **referring** | 1 | 114.77 | 6.622721 | 🔵 low — common in general English | - | - | — |
| 7481 | **record** | 2 | 114.33 | 3.298792 | 🔵 low — common in general English | - | - | — |
| 7482 | **job** | 1 | 114.33 | 6.597403 | 🔵 low — common in general English | - | - | — |
| 7483 | **sum** | 1 | 114.33 | 6.597403 | 🔵 low — common in general English | - | - | — |
| 7484 | **scheme** | 1 | 114.33 | 6.597403 | 🔵 low — common in general English | - | - | — |
| 7485 | **fast** | 1 | 114.33 | 6.597403 | 🔵 low — common in general English | - | - | — |
| 7486 | **solution** | 1 | 113.90 | 6.57271 | 🔵 low — common in general English | - | - | — |
| 7487 | **investigation** | 1 | 113.90 | 6.57271 | 🔵 low — common in general English | - | - | — |
| 7488 | **promote** | 1 | 113.49 | 6.548613 | 🔵 low — common in general English | - | - | — |
| 7489 | **remove** | 1 | 113.49 | 6.548613 | 🔵 low — common in general English | - | - | — |
| 7490 | **regarding** | 1 | 113.08 | 6.525082 | 🔵 low — common in general English | - | - | — |
| 7491 | **dealing** | 1 | 113.08 | 6.525082 | 🔵 low — common in general English | - | - | — |
| 7492 | **arrangement** | 1 | 112.68 | 6.502093 | 🔵 low — common in general English | - | - | — |
| 7493 | **effectively** | 1 | 112.68 | 6.502093 | 🔵 low — common in general English | - | - | — |
| 7494 | **dumping** | 1 | 112.29 | 6.47962 | 🔵 low — common in general English | - | - | — |
| 7495 | **announce** | 1 | 112.29 | 6.47962 | 🔵 low — common in general English | - | - | — |
| 7496 | **maintained** | 1 | 111.91 | 6.457641 | 🔵 low — common in general English | - | - | — |
| 7497 | **respond** | 1 | 111.91 | 6.457641 | 🔵 low — common in general English | - | - | — |
| 7498 | **compete** | 1 | 111.91 | 6.457641 | 🔵 low — common in general English | - | - | — |
| 7499 | **widely** | 1 | 111.54 | 6.436135 | 🔵 low — common in general English | - | - | — |
| 7500 | **duty** | 1 | 111.54 | 6.436135 | 🔵 low — common in general English | - | - | — |
| 7501 | **calculated** | 1 | 111.54 | 6.436135 | 🔵 low — common in general English | - | - | — |
| 7502 | **planted** | 1 | 111.17 | 6.415081 | 🔵 low — common in general English | - | - | — |
| 7503 | **strengthen** | 1 | 111.17 | 6.415081 | 🔵 low — common in general English | - | - | — |
| 7504 | **consistent** | 1 | 111.17 | 6.415081 | 🔵 low — common in general English | - | - | — |
| 7505 | **charged** | 1 | 111.17 | 6.415081 | 🔵 low — common in general English | - | - | — |
| 7506 | **showing** | 1 | 110.81 | 6.394462 | 🔵 low — common in general English | - | - | — |
| 7507 | **list** | 1 | 110.46 | 6.374259 | 🔵 low — common in general English | - | - | — |
| 7508 | **increasingly** | 1 | 110.46 | 6.374259 | 🔵 low — common in general English | - | - | — |
| 7509 | **appreciation** | 1 | 110.46 | 6.374259 | 🔵 low — common in general English | - | - | — |
| 7510 | **broadly** | 1 | 110.46 | 6.374259 | 🔵 low — common in general English | - | - | — |
| 7511 | **apparently** | 1 | 110.12 | 6.354457 | 🔵 low — common in general English | - | - | — |
| 7512 | **contribution** | 1 | 110.12 | 6.354457 | 🔵 low — common in general English | - | - | — |
| 7513 | **concluded** | 1 | 110.12 | 6.354457 | 🔵 low — common in general English | - | - | — |
| 7514 | **shell** | 1 | 110.12 | 6.354457 | 🔵 low — common in general English | - | - | — |
| 7515 | **housing** | 1 | 109.79 | 6.335039 | 🔵 low — common in general English | - | - | — |
| 7516 | **stressed** | 1 | 109.79 | 6.335039 | 🔵 low — common in general English | - | - | — |
| 7517 | **represented** | 1 | 109.79 | 6.335039 | 🔵 low — common in general English | - | - | — |
| 7518 | **relief** | 1 | 109.45 | 6.31599 | 🔵 low — common in general English | - | - | — |
| 7519 | **smith** | 1 | 109.45 | 6.31599 | 🔵 low — common in general English | - | - | — |
| 7520 | **applied** | 1 | 109.45 | 6.31599 | 🔵 low — common in general English | - | - | — |
| 7521 | **moderate** | 1 | 109.45 | 6.31599 | 🔵 low — common in general English | - | - | — |
| 7522 | **expense** | 1 | 109.45 | 6.31599 | 🔵 low — common in general English | - | - | — |
| 7523 | **waiting** | 1 | 109.45 | 6.31599 | 🔵 low — common in general English | - | - | — |
| 7524 | **sentiment** | 1 | 109.13 | 6.297298 | 🔵 low — common in general English | - | - | — |
| 7525 | **affecting** | 1 | 108.81 | 6.278949 | 🔵 low — common in general English | - | - | — |
| 7526 | **indicate** | 1 | 108.81 | 6.278949 | 🔵 low — common in general English | - | - | — |
| 7527 | **uncertainty** | 1 | 108.50 | 6.260931 | 🔵 low — common in general English | - | - | — |
| 7528 | **mostly** | 1 | 108.50 | 6.260931 | 🔵 low — common in general English | - | - | — |
| 7529 | **resume** | 1 | 108.19 | 6.243231 | 🔵 low — common in general English | - | - | — |
| 7530 | **severe** | 1 | 108.19 | 6.243231 | 🔵 low — common in general English | - | - | — |
| 7531 | **portion** | 1 | 107.89 | 6.225839 | 🔵 low — common in general English | - | - | — |
| 7532 | **traditional** | 1 | 107.60 | 6.208745 | 🔵 low — common in general English | - | - | — |
| 7533 | **intervene** | 1 | 107.31 | 6.191938 | 🔵 low — common in general English | - | - | — |
| 7534 | **threat** | 1 | 107.02 | 6.175409 | 🔵 low — common in general English | - | - | — |
| 7535 | **gap** | 1 | 106.46 | 6.143148 | 🔵 low — common in general English | - | - | — |
| 7536 | **coal** | 1 | 106.19 | 6.127399 | 🔵 low — common in general English | - | - | — |
| 7537 | **medium** | 1 | 106.19 | 6.127399 | 🔵 low — common in general English | - | - | — |
| 7538 | **suggested** | 1 | 106.19 | 6.127399 | 🔵 low — common in general English | - | - | — |
| 7539 | **ups** | 1 | 105.92 | 6.111895 | 🔵 low — common in general English | - | - | — |
| 7540 | **subordinated** | 1 | 105.92 | 6.111895 | 🔵 low — common in general English | - | - | — |
| 7541 | **buyer** | 1 | 105.92 | 6.111895 | 🔵 low — common in general English | - | - | — |
| 7542 | **opposed** | 1 | 105.65 | 6.096628 | 🔵 low — common in general English | - | - | — |
| 7543 | **leader** | 1 | 105.65 | 6.096628 | 🔵 low — common in general English | - | - | — |
| 7544 | **stronger** | 1 | 105.14 | 6.066775 | 🔵 low — common in general English | - | - | — |
| 7545 | **fair** | 1 | 105.14 | 6.066775 | 🔵 low — common in general English | - | - | — |
| 7546 | **possibly** | 1 | 104.63 | 6.037787 | 🔵 low — common in general English | - | - | — |
| 7547 | **original** | 1 | 104.63 | 6.037787 | 🔵 low — common in general English | - | - | — |
| 7548 | **underlying** | 1 | 103.67 | 5.982217 | 🔵 low — common in general English | - | - | — |
| 7549 | **alternative** | 1 | 103.67 | 5.982217 | 🔵 low — common in general English | - | - | — |
| 7550 | **medical** | 1 | 103.44 | 5.968794 | 🔵 low — common in general English | - | - | — |
| 7551 | **raw** | 1 | 103.21 | 5.955549 | 🔵 low — common in general English | - | - | — |
| 7552 | **labour** | 1 | 103.21 | 5.955549 | 🔵 low — common in general English | - | - | — |
| 7553 | **active** | 1 | 103.21 | 5.955549 | 🔵 low — common in general English | - | - | — |
| 7554 | **profitable** | 1 | 102.76 | 5.929574 | 🔵 low — common in general English | - | - | — |
| 7555 | **rice** | 1 | 102.76 | 5.929574 | 🔵 low — common in general English | - | - | — |
| 7556 | **note** | 2 | 102.61 | 2.960475 | 🔵 low — common in general English | - | - | — |
| 7557 | **exceed** | 1 | 102.54 | 5.916835 | 🔵 low — common in general English | - | - | — |
| 7558 | **sought** | 1 | 102.54 | 5.916835 | 🔵 low — common in general English | - | - | — |
| 7559 | **governor** | 1 | 102.10 | 5.891833 | 🔵 low — common in general English | - | - | — |
| 7560 | **block** | 1 | 102.10 | 5.891833 | 🔵 low — common in general English | - | - | — |
| 7561 | **originally** | 1 | 101.07 | 5.831935 | 🔵 low — common in general English | - | - | — |
| 7562 | **afternoon** | 1 | 101.07 | 5.831935 | 🔵 low — common in general English | - | - | — |
| 7563 | **via** | 1 | 100.87 | 5.820374 | 🔵 low — common in general English | - | - | — |
| 7564 | **expressed** | 1 | 100.47 | 5.797646 | 🔵 low — common in general English | - | - | — |
| 7565 | **legal** | 1 | 100.28 | 5.786473 | 🔵 low — common in general English | - | - | — |
| 7566 | **yield** | 1 | 100.28 | 5.786473 | 🔵 low — common in general English | - | - | — |
| 7567 | **resulted** | 1 | 100.09 | 5.775423 | 🔵 low — common in general English | - | - | — |
| 7568 | **authorized** | 1 | 99.71 | 5.753683 | 🔵 low — common in general English | - | - | — |
| 7569 | **fuel** | 1 | 99.34 | 5.732405 | 🔵 low — common in general English | - | - | — |
| 7570 | **indicated** | 1 | 99.34 | 5.732405 | 🔵 low — common in general English | - | - | — |
| 7571 | **designed** | 1 | 99.34 | 5.732405 | 🔵 low — common in general English | - | - | — |
| 7572 | **projected** | 1 | 98.98 | 5.711571 | 🔵 low — common in general English | - | - | — |
| 7573 | **aid** | 1 | 97.77 | 5.641891 | 🔵 low — common in general English | - | - | — |
| 7574 | **recovery** | 1 | 97.61 | 5.632322 | 🔵 low — common in general English | - | - | — |
| 7575 | **planning** | 1 | 97.61 | 5.632322 | 🔵 low — common in general English | - | - | — |
| 7576 | **estate** | 1 | 97.28 | 5.613454 | 🔵 low — common in general English | - | - | — |
| 7577 | **bond** | 1 | 97.28 | 5.613454 | 🔵 low — common in general English | - | - | — |
| 7578 | **stable** | 1 | 97.12 | 5.604151 | 🔵 low — common in general English | - | - | — |
| 7579 | **project** | 1 | 96.96 | 5.594934 | 🔵 low — common in general English | - | - | — |
| 7580 | **minimum** | 1 | 96.18 | 5.550084 | 🔵 low — common in general English | - | - | — |
| 7581 | **construction** | 1 | 96.03 | 5.54135 | 🔵 low — common in general English | - | - | — |
| 7582 | **posted** | 1 | 95.88 | 5.532692 | 🔵 low — common in general English | - | - | — |
| 7583 | **failed** | 1 | 95.73 | 5.524108 | 🔵 low — common in general English | - | - | — |
| 7584 | **raising** | 1 | 95.73 | 5.524108 | 🔵 low — common in general English | - | - | — |
| 7585 | **assistance** | 1 | 95.44 | 5.507159 | 🔵 low — common in general English | - | - | — |
| 7586 | **believed** | 1 | 95.29 | 5.498791 | 🔵 low — common in general English | - | - | — |
| 7587 | **performance** | 1 | 93.00 | 5.366301 | 🔵 low — common in general English | - | - | — |
| 7588 | **plus** | 1 | 92.87 | 5.359029 | 🔵 low — common in general English | - | - | — |
| 7589 | **consumption** | 1 | 92.62 | 5.34464 | 🔵 low — common in general English | - | - | — |
| 7590 | **closing** | 1 | 92.38 | 5.330455 | 🔵 low — common in general English | - | - | — |
| 7591 | **rejected** | 1 | 92.01 | 5.309549 | 🔵 low — common in general English | - | - | — |
| 7592 | **information** | 1 | 91.66 | 5.28907 | 🔵 low — common in general English | - | - | — |
| 7593 | **required** | 1 | 91.20 | 5.262402 | 🔵 low — common in general English | - | - | — |
| 7594 | **producing** | 1 | 90.97 | 5.24933 | 🔵 low — common in general English | - | - | — |
| 7595 | **nearly** | 1 | 90.64 | 5.230037 | 🔵 low — common in general English | - | - | — |
| 7596 | **regular** | 1 | 90.53 | 5.223687 | 🔵 low — common in general English | - | - | — |
| 7597 | **significant** | 1 | 89.26 | 5.150484 | 🔵 low — common in general English | - | - | — |
| 7598 | **initial** | 1 | 89.05 | 5.138788 | 🔵 low — common in general English | - | - | — |
| 7599 | **farm** | 1 | 88.85 | 5.127227 | 🔵 low — common in general English | - | - | — |
| 7600 | **gross** | 1 | 88.17 | 5.087785 | 🔵 low — common in general English | - | - | — |
| 7601 | **adding** | 1 | 87.06 | 5.023592 | 🔵 low — common in general English | - | - | — |
| 7602 | **range** | 1 | 86.44 | 4.987965 | 🔵 low — common in general English | - | - | — |
| 7603 | **respectively** | 1 | 86.35 | 4.982977 | 🔵 low — common in general English | - | - | — |
| 7604 | **probably** | 1 | 86.18 | 4.973076 | 🔵 low — common in general English | - | - | — |
| 7605 | **charge** | 1 | 85.35 | 4.92499 | 🔵 low — common in general English | - | - | — |
| 7606 | **selling** | 1 | 84.09 | 4.85256 | 🔵 low — common in general English | - | - | — |
| 7607 | **buying** | 1 | 82.50 | 4.760829 | 🔵 low — common in general English | - | - | — |
| 7608 | **despite** | 1 | 81.50 | 4.702786 | 🔵 low — common in general English | - | - | — |
| 7609 | **net** | 2 | 80.36 | 2.318656 | 🔵 low — common in general English | - | net, nets | — |
| 7610 | **transaction** | 1 | 80.30 | 4.633793 | 🔵 low — common in general English | - | - | — |
| 7611 | **available** | 1 | 79.59 | 4.59255 | 🔵 low — common in general English | - | - | — |
| 7612 | **secretary** | 1 | 79.24 | 4.57255 | 🔵 low — common in general English | - | - | — |
| 7613 | **loan** | 1 | 77.35 | 4.463236 | 🔵 low — common in general English | - | - | — |
| 7614 | **public** | 1 | 76.25 | 4.400178 | 🔵 low — common in general English | - | - | — |
| 7615 | **bought** | 1 | 74.65 | 4.307397 | 🔵 low — common in general English | - | - | — |
| 7616 | **outstanding** | 1 | 70.91 | 4.091877 | 🔵 low — common in general English | - | - | — |
| 7617 | **yesterday** | 1 | 70.42 | 4.063706 | 🔵 low — common in general English | - | - | — |
| 7618 | **trading** | 1 | 70.35 | 4.059746 | 🔵 low — common in general English | - | - | — |
| 7619 | **capital** | 1 | 69.49 | 4.009639 | 🔵 low — common in general English | - | - | — |
| 7620 | **statement** | 1 | 67.90 | 3.918095 | 🔵 low — common in general English | - | - | — |
| 7621 | **industry** | 1 | 67.84 | 3.914671 | 🔵 low — common in general English | - | - | — |
| 7622 | **official** | 1 | 65.21 | 3.76272 | 🔵 low — common in general English | - | - | — |
| 7623 | **production** | 1 | 65.08 | 3.755405 | 🔵 low — common in general English | - | - | — |
| 7624 | **tax** | 1 | 65.00 | 3.751041 | 🔵 low — common in general English | - | - | — |
| 7625 | **rose** | 1 | 63.77 | 3.679632 | 🔵 low — common in general English | - | - | — |
| 7626 | **agreed** | 1 | 63.74 | 3.678282 | 🔵 low — common in general English | - | - | — |
| 7627 | **foreign** | 1 | 63.35 | 3.655599 | 🔵 low — common in general English | - | - | — |
| 7628 | **government** | 1 | 60.98 | 3.518939 | 🔵 low — common in general English | - | - | — |
| 7629 | **expected** | 1 | 58.67 | 3.385552 | 🔵 low — common in general English | - | - | — |
| 7630 | **exchange** | 1 | 58.64 | 3.38354 | 🔵 low — common in general English | 0.182281 | - | — |
| 7631 | **agreement** | 1 | 58.50 | 3.375532 | 🔵 low — common in general English | - | - | — |
| 7632 | **stock** | 1 | 52.87 | 3.050663 | 🔵 low — common in general English | - | - | — |
| 7633 | **great dharma king** | - | - | - | - | 0.000345 | - | ~ |
| 7634 | **negative action** | - | - | - | - | 0.000408 | - | ✓ སྡིག་པ / མི་དགེ་བ |
| 7635 | **dharma king** | - | - | - | - | 0.000417 | - | ~ |
| 7636 | **dharma practice** | - | - | - | - | 0.000553 | - | — |
| 7637 | **dharma king trisong** | - | - | - | - | 0.000557 | - | ~ |
| 7638 | **dharma king songtsen** | - | - | - | - | 0.000568 | - | ~ |
| 7639 | **true dharma** | - | - | - | - | 0.000664 | - | ~ |
| 7640 | **practise dharma** | - | - | - | - | 0.000705 | - | — |
| 7641 | **time lord buddha** | - | - | - | - | 0.000773 | - | — |
| 7642 | **buddha dharma** | - | - | - | - | 0.000845 | - | ~ |
| 7643 | **jetsun mila** | - | - | - | - | 0.000853 | - | ~ |
| 7644 | **buddha sakyamuni** | - | - | - | - | 0.001044 | - | — |
| 7645 | **lord buddha** | - | - | - | - | 0.001077 | - | ~ |
| 7646 | **perfect buddha** | - | - | - | - | 0.001148 | - | — |
| 7647 | **great master** | - | - | - | - | 0.001219 | - | ~ |
| 7648 | **king jewel crest** | - | - | - | - | 0.001307 | - | — |
| 7649 | **positive action** | - | - | - | - | 0.001327 | - | ✓ དགེ་བ |
| 7650 | **authentic dharma** | - | - | - | - | 0.001389 | - | — |
| 7651 | **great teacher** | - | - | - | - | 0.001423 | - | ~ |
| 7652 | **secret mantra vajrayana** | - | - | - | - | 0.001430 | - | ~ |
| 7653 | **omniscient dharma king** | - | - | - | - | 0.001542 | - | ~ |
| 7654 | **great vehicle** | - | - | - | - | 0.001587 | - | ✓ ཐེག་པ་ཆེན་པོ |
| 7655 | **great perfection** | - | - | - | - | 0.001754 | - | ✓ རྫོགས་པ་ཆེན་པོ |
| 7656 | **perfect buddhahood** | - | - | - | - | 0.001807 | - | — |
| 7657 | **great compassion** | - | - | - | - | 0.001869 | - | ~ |
| 7658 | **single dharma practice** | - | - | - | - | 0.001979 | - | — |
| 7659 | **real buddha** | - | - | - | - | 0.001997 | - | ~ |
| 7660 | **secret mantra vehicle** | - | - | - | - | 0.002038 | - | ~ |
| 7661 | **guru yoga** | - | - | - | - | 0.002044 | - | ✓ བླ་མའི་རྣལ་འབྱོར |
| 7662 | **dharma protector** | - | - | - | - | 0.002166 | - | ✓ ཆོས་སྐྱོང |
| 7663 | **secret mantra** | - | - | - | - | 0.002174 | - | ~ |
| 7664 | **great bodhisattva abbot** | - | - | - | - | 0.002367 | - | ~ |
| 7665 | **great dharma** | - | - | - | - | 0.002466 | - | ~ |
| 7666 | **secret mantrayana** | - | - | - | - | 0.002519 | - | ✓ གསང་སྔགས་ཀྱི་ཐེག་པ |
| 7667 | **bodhisattva dharmodgata** | - | - | - | - | 0.002558 | - | ~ |
| 7668 | **buddha amitabha** | - | - | - | - | 0.002597 | - | ~ |
| 7669 | **dharma teaching** | - | - | - | - | 0.002600 | - | ~ |
| 7670 | **practise real dharma** | - | - | - | - | 0.002649 | - | — |
| 7671 | **dharma king trisongdetsen** | - | - | - | - | 0.002791 | - | — |
| 7672 | **take refuge** | - | - | - | - | 0.002983 | - | — |
| 7673 | **human life** | - | - | - | - | 0.003045 | - | — |
| 7674 | **king jewel** | - | - | - | - | 0.003134 | - | ~ |
| 7675 | **practise true dharma** | - | - | - | - | 0.003397 | - | — |
| 7676 | **perfect buddha sakyamuni** | - | - | - | - | 0.003445 | - | — |
| 7677 | **pure dharma** | - | - | - | - | 0.003690 | - | ~ |
| 7678 | **time bodhisattva dharmodgata** | - | - | - | - | 0.003742 | - | — |
| 7679 | **root teacher** | - | - | - | - | 0.003766 | - | ✓ རྩ་བའི་བླ་མ |
| 7680 | **real dharma** | - | - | - | - | 0.003907 | - | ~ |
| 7681 | **discover dharma** | - | - | - | - | 0.004069 | - | — |
| 7682 | **great bodhisattva** | - | - | - | - | 0.004088 | - | ~ |
| 7683 | **great king** | - | - | - | - | 0.004218 | - | ~ |
| 7684 | **king trisong detsen** | - | - | - | - | 0.004222 | - | ~ |
| 7685 | **jewel crest** | - | - | - | - | 0.004470 | - | — |
| 7686 | **bhagavan buddha** | - | - | - | - | 0.004516 | - | ~ |
| 7687 | **attain perfect buddhahood** | - | - | - | - | 0.004525 | - | — |
| 7688 | **present buddha sakyamuni** | - | - | - | - | 0.004603 | - | — |
| 7689 | **perfect teacher** | - | - | - | - | 0.004633 | - | — |
| 7690 | **spiritual teacher** | - | - | - | - | 0.004746 | - | ~ |
| 7691 | **perfectly practise dharma** | - | - | - | - | 0.004766 | - | — |
| 7692 | **peerless teacher** | - | - | - | - | 0.004883 | - | — |
| 7693 | **practise guru yoga** | - | - | - | - | 0.004946 | - | — |
| 7694 | **past life** | - | - | - | - | 0.005028 | - | — |
| 7695 | **bodhisattva dharmodgata teaching** | - | - | - | - | 0.005203 | - | ~ |
| 7696 | **vajra guru mantra** | - | - | - | - | 0.005212 | - | ~ |
| 7697 | **omniscient dharma** | - | - | - | - | 0.005293 | - | ~ |
| 7698 | **spiritual friend** | - | - | - | - | 0.005295 | - | ✓ དགེ་བའི་བཤེས་གཉེན |
| 7699 | **great perfection lineage** | - | - | - | - | 0.005301 | - | ~ |
| 7700 | **teacher vajrasattva** | - | - | - | - | 0.005395 | - | ~ |
| 7701 | **precious lord guru** | - | - | - | - | 0.005405 | - | ~ |
| 7702 | **long time** | - | - | - | - | 0.005735 | - | — |
| 7703 | **evil action** | - | - | - | - | 0.006054 | - | — |
| 7704 | **syllable mantra** | - | - | - | - | 0.006142 | - | — |
| 7705 | **buddha kasyapa** | - | - | - | - | 0.006191 | - | — |
| 7706 | **sublime dharma** | - | - | - | - | 0.006231 | - | ~ |
| 7707 | **jetsun milarepa** | - | - | - | - | 0.006429 | - | ~ |
| 7708 | **glorious root teacher** | - | - | - | - | 0.006506 | - | ~ |
| 7709 | **good kalpa** | - | - | - | - | 0.006532 | - | ✓ བསྐལ་པ་བཟང་པོ |
| 7710 | **king songtsen gampo** | - | - | - | - | 0.006571 | - | ~ |
| 7711 | **buddha maitreya** | - | - | - | - | 0.006589 | - | ~ |
| 7712 | **dharma properly** | - | - | - | - | 0.006697 | - | — |
| 7713 | **precious jewel** | - | - | - | - | 0.006924 | - | ~ |
| 7714 | **dagpo rinpoche** | - | - | - | - | 0.006992 | - | ~ |
| 7715 | **bring great benefit** | - | - | - | - | 0.007020 | - | — |
| 7716 | **profound dharma** | - | - | - | - | 0.007031 | - | ~ |
| 7717 | **negative emotion** | - | - | - | - | 0.007189 | - | — |
| 7718 | **completely perfect buddha** | - | - | - | - | 0.007404 | - | — |
| 7719 | **sublime teacher** | - | - | - | - | 0.007414 | - | ~ |
| 7720 | **mantra vajrayana** | - | - | - | - | 0.007475 | - | ~ |
| 7721 | **attain buddhahood** | - | - | - | - | 0.007556 | - | — |
| 7722 | **ordinary people** | - | - | - | - | 0.007655 | - | — |
| 7723 | **great indian master** | - | - | - | - | 0.007730 | - | — |
| 7724 | **perfect teacher vajrasattva** | - | - | - | - | 0.007775 | - | — |
| 7725 | **great kalpa** | - | - | - | - | 0.007840 | - | ~ |
| 7726 | **present life** | - | - | - | - | 0.007945 | - | — |
| 7727 | **padampa sangye** | - | - | - | - | 0.008057 | - | ✓ ཕ་དམ་པ་སངས་རྒྱས |
| 7728 | **perfection phase** | - | - | - | - | 0.008196 | - | ✓ རྫོགས་རིམ |
| 7729 | **precious dharma** | - | - | - | - | 0.008199 | - | ~ |
| 7730 | **dharma practitioner** | - | - | - | - | 0.008435 | - | ~ |
| 7731 | **great guru** | - | - | - | - | 0.008508 | - | ~ |
| 7732 | **natural state** | - | - | - | - | 0.008517 | - | ✓ གནས་ལུགས |
| 7733 | **past negative** | - | - | - | - | 0.008528 | - | — |
| 7734 | **main practice** | - | - | - | - | 0.008529 | - | — |
| 7735 | **kind teacher** | - | - | - | - | 0.008532 | - | — |
| 7736 | **king trisong** | - | - | - | - | 0.008689 | - | ~ |
| 7737 | **natural great perfection** | - | - | - | - | 0.008765 | - | ~ |
| 7738 | **great bliss** | - | - | - | - | 0.008853 | - | ~ |
| 7739 | **perfect dharma** | - | - | - | - | 0.008996 | - | — |
| 7740 | **true jewel** | - | - | - | - | 0.009018 | - | ~ |
| 7741 | **rigdzin jigme lingpa** | - | - | - | - | 0.009199 | - | — |
| 7742 | **guru rinpoche** | - | - | - | - | 0.009262 | - | ✓ གུ་རུ་རིན་པོ་ཆེ |
| 7743 | **peerless dagpo rinpoche** | - | - | - | - | 0.009321 | - | — |
| 7744 | **great ocean** | - | - | - | - | 0.009409 | - | — |
| 7745 | **supreme authentic dharma** | - | - | - | - | 0.009519 | - | — |
| 7746 | **jowo rinpoche** | - | - | - | - | 0.009561 | - | ✓ ཇོ་བོ་རིན་པོ་ཆེ |
| 7747 | **vajra master** | - | - | - | - | 0.009585 | - | ✓ རྡོ་རྗེ་སློབ་དཔོན |
| 7748 | **utterly perfect buddha** | - | - | - | - | 0.009613 | - | — |
| 7749 | **great river** | - | - | - | - | 0.009848 | - | — |
| 7750 | **future life** | - | - | - | - | 0.009851 | - | — |
| 7751 | **wisdom mind** | - | - | - | - | 0.009857 | - | ~ |
| 7752 | **precious human life** | - | - | - | - | 0.009863 | - | — |
| 7753 | **mount meru** | - | - | - | - | 0.009863 | - | ~ |
| 7754 | **mantra vehicle** | - | - | - | - | 0.009864 | - | ~ |
| 7755 | **single dharma** | - | - | - | - | 0.010094 | - | — |
| 7756 | **great master tendzin** | - | - | - | - | 0.010097 | - | — |
| 7757 | **jewel family** | - | - | - | - | 0.010464 | - | — |
| 7758 | **practise dharma alongside** | - | - | - | - | 0.010472 | - | — |
| 7759 | **refuge practice** | - | - | - | - | 0.010514 | - | — |
| 7760 | **buddha family** | - | - | - | - | 0.010651 | - | — |
| 7761 | **authentic teacher** | - | - | - | - | 0.010700 | - | — |
| 7762 | **practise dharma authentically** | - | - | - | - | 0.010741 | - | — |
| 7763 | **wrong view** | - | - | - | - | 0.010834 | - | ✓ ལོག་ལྟ |
| 7764 | **true dharma properly** | - | - | - | - | 0.010843 | - | — |
| 7765 | **intermediate state** | - | - | - | - | 0.011133 | - | ✓ བར་དོ |
| 7766 | **great benefit** | - | - | - | - | 0.011212 | - | — |
| 7767 | **geshe tonpa** | - | - | - | - | 0.011368 | - | ~ |
| 7768 | **great giving** | - | - | - | - | 0.011454 | - | — |
| 7769 | **present great kalpa** | - | - | - | - | 0.011470 | - | — |
| 7770 | **long life** | - | - | - | - | 0.011520 | - | — |
| 7771 | **buddha protector amitayus** | - | - | - | - | 0.011577 | - | ~ |
| 7772 | **arouse bodhicitta** | - | - | - | - | 0.011581 | - | — |
| 7773 | **authentic spiritual teacher** | - | - | - | - | 0.011750 | - | — |
| 7774 | **good fortune** | - | - | - | - | 0.011909 | - | — |
| 7775 | **garab dorje** | - | - | - | - | 0.012033 | - | ✓ དགའ་རབ་རྡོ་རྗེ |
| 7776 | **genuine dharma** | - | - | - | - | 0.012040 | - | — |
| 7777 | **transcendent wisdom** | - | - | - | - | 0.012075 | - | ~ |
| 7778 | **true buddha** | - | - | - | - | 0.012203 | - | ~ |
| 7779 | **buddha samantabhadra** | - | - | - | - | 0.012234 | - | ~ |
| 7780 | **king songtsen** | - | - | - | - | 0.012398 | - | ~ |
| 7781 | **buddha protector** | - | - | - | - | 0.012447 | - | ~ |
| 7782 | **time bodhisattva** | - | - | - | - | 0.012644 | - | — |
| 7783 | **master jowo atisa** | - | - | - | - | 0.012716 | - | — |
| 7784 | **pure buddha** | - | - | - | - | 0.012723 | - | ~ |
| 7785 | **jigme lingpa** | - | - | - | - | 0.012748 | - | ✓ འཇིགས་མེད་གླིང་པ |
| 7786 | **time great** | - | - | - | - | 0.012830 | - | — |
| 7787 | **great vehicle tradition** | - | - | - | - | 0.013087 | - | ~ |
| 7788 | **surpass buddha sakyamuni** | - | - | - | - | 0.013331 | - | — |
| 7789 | **present buddha** | - | - | - | - | 0.013387 | - | — |
| 7790 | **wrong action** | - | - | - | - | 0.013612 | - | ~ |
| 7791 | **love compassion** | - | - | - | - | 0.013699 | - | — |
| 7792 | **worldly life** | - | - | - | - | 0.013702 | - | — |
| 7793 | **jowo atisa** | - | - | - | - | 0.013750 | - | — |
| 7794 | **bodhisattva sadaprarudita** | - | - | - | - | 0.013787 | - | ~ |
| 7795 | **great love** | - | - | - | - | 0.013816 | - | — |
| 7796 | **day geshe ben** | - | - | - | - | 0.013825 | - | — |
| 7797 | **secret true teaching** | - | - | - | - | 0.013934 | - | ~ |
| 7798 | **lord nagarjuna** | - | - | - | - | 0.013947 | - | ~ |
| 7799 | **venerable teacher** | - | - | - | - | 0.014035 | - | — |
| 7800 | **gracious root teacher** | - | - | - | - | 0.014167 | - | — |
| 7801 | **good thing** | - | - | - | - | 0.014174 | - | — |
| 7802 | **secret path** | - | - | - | - | 0.014381 | - | ~ |
| 7803 | **buddha vajradhara** | - | - | - | - | 0.014852 | - | ~ |
| 7804 | **great secret** | - | - | - | - | 0.014869 | - | ~ |
| 7805 | **profound path** | - | - | - | - | 0.015066 | - | ~ |
| 7806 | **great faith** | - | - | - | - | 0.015102 | - | — |
| 7807 | **great perfect** | - | - | - | - | 0.015369 | - | — |
| 7808 | **good thought** | - | - | - | - | 0.015436 | - | ~ |
| 7809 | **sakya buddha** | - | - | - | - | 0.015437 | - | — |
| 7810 | **lord maitreya** | - | - | - | - | 0.015497 | - | ~ |
| 7811 | **future buddha** | - | - | - | - | 0.015703 | - | — |
| 7812 | **buddha manjusri** | - | - | - | - | 0.015752 | - | — |
| 7813 | **speech mind** | - | - | - | - | 0.016056 | - | ~ |
| 7814 | **bodhisattva level** | - | - | - | - | 0.016194 | - | ~ |
| 7815 | **lord guru** | - | - | - | - | 0.016389 | - | ~ |
| 7816 | **great compassionate** | - | - | - | - | 0.016480 | - | ~ |
| 7817 | **bring great** | - | - | - | - | 0.016784 | - | — |
| 7818 | **feel great** | - | - | - | - | 0.016996 | - | — |
| 7819 | **teacher nagarjuna** | - | - | - | - | 0.017267 | - | ~ |
| 7820 | **good lama** | - | - | - | - | 0.017422 | - | ~ |
| 7821 | **great translator** | - | - | - | - | 0.017471 | - | — |
| 7822 | **great perfect vajradhara** | - | - | - | - | 0.017509 | - | — |
| 7823 | **great siddha** | - | - | - | - | 0.017657 | - | ~ |
| 7824 | **effect similar** | - | - | - | - | 0.017783 | - | — |
| 7825 | **entire dharma** | - | - | - | - | 0.017868 | - | — |
| 7826 | **bodhisattva samantabhadra** | - | - | - | - | 0.017987 | - | ~ |
| 7827 | **precious lord** | - | - | - | - | 0.018135 | - | ~ |
| 7828 | **buddha infinite** | - | - | - | - | 0.018279 | - | ~ |
| 7829 | **human life complete** | - | - | - | - | 0.018362 | - | — |
| 7830 | **practise guru** | - | - | - | - | 0.018416 | - | — |
| 7831 | **great translator vairotsana** | - | - | - | - | 0.018484 | - | — |
| 7832 | **human form** | - | - | - | - | 0.018667 | - | — |
| 7833 | **accumulate merit** | - | - | - | - | 0.019462 | - | — |
| 7834 | **single good thought** | - | - | - | - | 0.019643 | - | — |
| 7835 | **rigdzin jigme** | - | - | - | - | 0.019723 | - | — |
| 7836 | **buddha vairocana** | - | - | - | - | 0.019863 | - | ~ |
| 7837 | **study dharma** | - | - | - | - | 0.020511 | - | ~ |
| 7838 | **vajra guru** | - | - | - | - | 0.020613 | - | ~ |
| 7839 | **naropa thought** | - | - | - | - | 0.020993 | - | ~ |
| 7840 | **negative karmic effect** | - | - | - | - | 0.021015 | - | ~ |
| 7841 | **good worldly life** | - | - | - | - | 0.021128 | - | — |
| 7842 | **buddha ratnasambhava** | - | - | - | - | 0.021370 | - | ~ |
| 7843 | **buddha amoghasiddhi** | - | - | - | - | 0.021370 | - | ~ |
| 7844 | **primordially buddha** | - | - | - | - | 0.021426 | - | — |
| 7845 | **buddha vajraguhya** | - | - | - | - | 0.021427 | - | — |
| 7846 | **inexhaustible dharma** | - | - | - | - | 0.021440 | - | ~ |
| 7847 | **dharma understanding** | - | - | - | - | 0.021587 | - | — |
| 7848 | **bodhisattva santideva** | - | - | - | - | 0.021733 | - | — |
| 7849 | **sacred dharma** | - | - | - | - | 0.021853 | - | — |
| 7850 | **action good** | - | - | - | - | 0.022000 | - | ~ |
| 7851 | **ordinary life** | - | - | - | - | 0.022004 | - | — |
| 7852 | **action family** | - | - | - | - | 0.022048 | - | — |
| 7853 | **great par** | - | - | - | - | 0.022053 | - | — |
| 7854 | **buddha immediately** | - | - | - | - | 0.022103 | - | — |
| 7855 | **perfect teacher venerable** | - | - | - | - | 0.022253 | - | — |
| 7856 | **poison jetsun mila** | - | - | - | - | 0.022368 | - | — |
| 7857 | **primal wisdom** | - | - | - | - | 0.022389 | - | ✓ ཡེ་ཤེས |
| 7858 | **generation perfection** | - | - | - | - | 0.022451 | - | ~ |
| 7859 | **guru mantra** | - | - | - | - | 0.022474 | - | ~ |
| 7860 | **long ago** | - | - | - | - | 0.022532 | - | — |
| 7861 | **mind lineage** | - | - | - | - | 0.022945 | - | ~ |
| 7862 | **hell realm** | - | - | - | - | 0.022999 | - | ~ |
| 7863 | **great pandita naropa** | - | - | - | - | 0.023039 | - | ~ |
| 7864 | **negative effect** | - | - | - | - | 0.023070 | - | ~ |
| 7865 | **buddha infinite aspiration** | - | - | - | - | 0.023248 | - | ~ |
| 7866 | **ephemeral hell** | - | - | - | - | 0.023269 | - | — |
| 7867 | **medicine buddha** | - | - | - | - | 0.023285 | - | — |
| 7868 | **holy dharma** | - | - | - | - | 0.023456 | - | — |
| 7869 | **dharma language** | - | - | - | - | 0.023513 | - | — |
| 7870 | **great kalpas** | - | - | - | - | 0.023520 | - | — |
| 7871 | **bring buddhahood** | - | - | - | - | 0.023706 | - | — |
| 7872 | **secret mantra mandala** | - | - | - | - | 0.023876 | - | ~ |
| 7873 | **great tilopa** | - | - | - | - | 0.023891 | - | ~ |
| 7874 | **combine dharma** | - | - | - | - | 0.024067 | - | — |
| 7875 | **good bad** | - | - | - | - | 0.024096 | - | — |
| 7876 | **lord padampa sangye** | - | - | - | - | 0.024346 | - | ~ |
| 7877 | **mandala offering** | - | - | - | - | 0.024477 | - | ~ |
| 7878 | **time lord** | - | - | - | - | 0.024621 | - | — |
| 7879 | **trisong detsen** | - | - | - | - | 0.024685 | - | ✓ ཁྲི་སྲོང་སྡེའུ་བཙན |
| 7880 | **bodhisattva abbot** | - | - | - | - | 0.024797 | - | ✓ |
| 7881 | **merit great** | - | - | - | - | 0.024874 | - | ~ |
| 7882 | **negative act** | - | - | - | - | 0.025015 | - | — |
| 7883 | **langri thangpa** | - | - | - | - | 0.025087 | - | ~ |
| 7884 | **great compassion possess** | - | - | - | - | 0.025116 | - | — |
| 7885 | **cho practice** | - | - | - | - | 0.025117 | - | — |
| 7886 | **black true mother** | - | - | - | - | 0.025355 | - | ~ |
| 7887 | **geshe ben** | - | - | - | - | 0.025468 | - | — |
| 7888 | **sambhogakaya buddha** | - | - | - | - | 0.025546 | - | ~ |
| 7889 | **lama ngokpa** | - | - | - | - | 0.025651 | - | — |
| 7890 | **authentic vajra master** | - | - | - | - | 0.025955 | - | — |
| 7891 | **natural great** | - | - | - | - | 0.026054 | - | ~ |
| 7892 | **vajra family** | - | - | - | - | 0.026132 | - | — |
| 7893 | **great wisdom** | - | - | - | - | 0.026204 | - | ~ |
| 7894 | **bodhicitta practice** | - | - | - | - | 0.026465 | - | — |
| 7895 | **mila dorje gyaltsen** | - | - | - | - | 0.026697 | - | ~ |
| 7896 | **great pain** | - | - | - | - | 0.026716 | - | — |
| 7897 | **dharma drift** | - | - | - | - | 0.026742 | - | — |
| 7898 | **great lama** | - | - | - | - | 0.026803 | - | ~ |
| 7899 | **dharma alongside** | - | - | - | - | 0.026809 | - | — |
| 7900 | **dodrup chen rinpoche** | - | - | - | - | 0.027255 | - | — |
| 7901 | **dharma authentically** | - | - | - | - | 0.027310 | - | — |
| 7902 | **purest dharma** | - | - | - | - | 0.027312 | - | — |
| 7903 | **marry dharma** | - | - | - | - | 0.027332 | - | — |
| 7904 | **single negative thought** | - | - | - | - | 0.027656 | - | — |
| 7905 | **mandala base** | - | - | - | - | 0.027775 | - | — |
| 7906 | **karmic effect** | - | - | - | - | 0.027992 | - | ~ |
| 7907 | **primordial buddha** | - | - | - | - | 0.028239 | - | ~ |
| 7908 | **great paqqita naropa** | - | - | - | - | 0.028465 | - | — |
| 7909 | **noble sangha** | - | - | - | - | 0.028784 | - | ~ |
| 7910 | **king prasenajit** | - | - | - | - | 0.028976 | - | — |
| 7911 | **chen rinpoche** | - | - | - | - | 0.029208 | - | — |
| 7912 | **buddha miraculously** | - | - | - | - | 0.029500 | - | — |
| 7913 | **vajra body** | - | - | - | - | 0.029676 | - | ~ |
| 7914 | **good food** | - | - | - | - | 0.029715 | - | — |
| 7915 | **great close** | - | - | - | - | 0.030077 | - | ~ |
| 7916 | **noble master nagarjuna** | - | - | - | - | 0.030195 | - | ~ |
| 7917 | **compassionate root teacher** | - | - | - | - | 0.030403 | - | ~ |
| 7918 | **great power** | - | - | - | - | 0.030420 | - | — |
| 7919 | **great vehicle widely** | - | - | - | - | 0.030590 | - | — |
| 7920 | **great care** | - | - | - | - | 0.031160 | - | — |
| 7921 | **merit great rejoicing** | - | - | - | - | 0.031215 | - | — |
| 7922 | **songtsen gampo** | - | - | - | - | 0.031281 | - | ✓ སྲོང་བཙན་སྒམ་པོ |
| 7923 | **preliminary practice** | - | - | - | - | 0.031378 | - | — |
| 7924 | **eighty thousand** | - | - | - | - | 0.031406 | - | ~ |
| 7925 | **surpass buddha** | - | - | - | - | 0.031489 | - | — |
| 7926 | **extraordinary secret mantra** | - | - | - | - | 0.031680 | - | — |
| 7927 | **perfect place** | - | - | - | - | 0.031858 | - | — |
| 7928 | **negative thought** | - | - | - | - | 0.032067 | - | ~ |
| 7929 | **day geshe** | - | - | - | - | 0.032187 | - | — |
| 7930 | **fourth jewel** | - | - | - | - | 0.032217 | - | ~ |
| 7931 | **peerless dagpo** | - | - | - | - | 0.032245 | - | — |
| 7932 | **ordinary worldly people** | - | - | - | - | 0.032371 | - | — |
| 7933 | **ultimate torment** | - | - | - | - | 0.032727 | - | — |
| 7934 | **sublime path** | - | - | - | - | 0.032878 | - | ~ |
| 7935 | **ordinary human form** | - | - | - | - | 0.033002 | - | — |
| 7936 | **attain perfect** | - | - | - | - | 0.033069 | - | — |
| 7937 | **authentic path** | - | - | - | - | 0.033131 | - | — |
| 7938 | **dark kalpa** | - | - | - | - | 0.033138 | - | — |
| 7939 | **clear light** | - | - | - | - | 0.033217 | - | ✓ འོད་གསལ |
| 7940 | **feel good** | - | - | - | - | 0.033363 | - | — |
| 7941 | **teacher sakyamuni** | - | - | - | - | 0.033607 | - | — |
| 7942 | **great kindness** | - | - | - | - | 0.033884 | - | — |
| 7943 | **master teaching** | - | - | - | - | 0.033925 | - | ~ |
| 7944 | **essential point** | - | - | - | - | 0.033934 | - | ~ |
| 7945 | **single good** | - | - | - | - | 0.033963 | - | — |
| 7946 | **complete buddhahood** | - | - | - | - | 0.034160 | - | — |
| 7947 | **lord vajrasattva** | - | - | - | - | 0.034594 | - | ~ |
| 7948 | **pure perception** | - | - | - | - | 0.034677 | - | ✓ དག་སྣང |
| 7949 | **great wheel** | - | - | - | - | 0.035031 | - | ~ |
| 7950 | **evil spirit** | - | - | - | - | 0.035258 | - | — |
| 7951 | **great perfection subsequently** | - | - | - | - | 0.035269 | - | — |
| 7952 | **sublime bodhicitta** | - | - | - | - | 0.035722 | - | ~ |
| 7953 | **reason guru yoga** | - | - | - | - | 0.036073 | - | — |
| 7954 | **great omniscient** | - | - | - | - | 0.036308 | - | ~ |
| 7955 | **life death** | - | - | - | - | 0.036755 | - | — |
| 7956 | **vajrasattva practice** | - | - | - | - | 0.036768 | - | — |
| 7957 | **total buddhahood** | - | - | - | - | 0.036841 | - | — |
| 7958 | **protector amitabha** | - | - | - | - | 0.037524 | - | ~ |
| 7959 | **great wealth** | - | - | - | - | 0.037623 | - | ~ |
| 7960 | **great sage** | - | - | - | - | 0.037785 | - | — |
| 7961 | **great importance** | - | - | - | - | 0.037816 | - | — |
| 7962 | **perfectly pure** | - | - | - | - | 0.037897 | - | — |
| 7963 | **great tree** | - | - | - | - | 0.038472 | - | ~ |
| 7964 | **point lord maitreya** | - | - | - | - | 0.038611 | - | ~ |
| 7965 | **great demon** | - | - | - | - | 0.038654 | - | ~ |
| 7966 | **positive act** | - | - | - | - | 0.038682 | - | — |
| 7967 | **single word** | - | - | - | - | 0.038729 | - | — |
| 7968 | **great evil** | - | - | - | - | 0.039051 | - | — |
| 7969 | **jewel free** | - | - | - | - | 0.039146 | - | ~ |
| 7970 | **previous life** | - | - | - | - | 0.039346 | - | — |
| 7971 | **wrong path** | - | - | - | - | 0.039533 | - | ~ |
| 7972 | **excellent human life** | - | - | - | - | 0.039679 | - | — |
| 7973 | **present great** | - | - | - | - | 0.040051 | - | — |
| 7974 | **thousand people** | - | - | - | - | 0.040179 | - | — |
| 7975 | **great pandita** | - | - | - | - | 0.040337 | - | ~ |
| 7976 | **mila dorje** | - | - | - | - | 0.040990 | - | ~ |
| 7977 | **spiritual practice** | - | - | - | - | 0.041164 | - | — |
| 7978 | **great indian** | - | - | - | - | 0.041329 | - | — |
| 7979 | **great remorse** | - | - | - | - | 0.041497 | - | — |
| 7980 | **lord avalokitesvara** | - | - | - | - | 0.041722 | - | — |
| 7981 | **single teacher** | - | - | - | - | 0.041728 | - | — |
| 7982 | **good health** | - | - | - | - | 0.041757 | - | — |
| 7983 | **great lake** | - | - | - | - | 0.041871 | - | — |
| 7984 | **bodh gaya** | - | - | - | - | 0.041955 | - | — |
| 7985 | **human realm** | - | - | - | - | 0.042105 | - | — |
| 7986 | **king surabhibhadra** | - | - | - | - | 0.042313 | - | — |
| 7987 | **ordinary human** | - | - | - | - | 0.042327 | - | — |
| 7988 | **great liberation** | - | - | - | - | 0.042443 | - | ~ |
| 7989 | **great ship** | - | - | - | - | 0.042481 | - | — |
| 7990 | **humble life** | - | - | - | - | 0.042509 | - | — |
| 7991 | **exceptionally great giving** | - | - | - | - | 0.043184 | - | — |
| 7992 | **pure land** | - | - | - | - | 0.043334 | - | ✓ དག་པའི་ཞིང |
| 7993 | **time sakyamuni** | - | - | - | - | 0.043592 | - | — |
| 7994 | **authentic spiritual friend** | - | - | - | - | 0.043731 | - | — |
| 7995 | **true teacher** | - | - | - | - | 0.043964 | - | ~ |
| 7996 | **jetsun shepa dorje** | - | - | - | - | 0.043979 | - | — |
| 7997 | **human existence** | - | - | - | - | 0.044075 | - | — |
| 7998 | **vajra sattva hum** | - | - | - | - | 0.044224 | - | — |
| 7999 | **great effort** | - | - | - | - | 0.044377 | - | — |
| 8000 | **thousand water** | - | - | - | - | 0.044464 | - | ~ |
| 8001 | **great vajradhara** | - | - | - | - | 0.044560 | - | ~ |
| 8002 | **great maudgalyayana** | - | - | - | - | 0.044663 | - | ~ |
| 8003 | **wrathful black true** | - | - | - | - | 0.044853 | - | ~ |
| 8004 | **kind heart** | - | - | - | - | 0.044885 | - | — |
| 8005 | **wrathful black** | - | - | - | - | 0.044998 | - | ~ |
| 8006 | **great elapatra tree** | - | - | - | - | 0.045068 | - | — |
| 8007 | **great scholar** | - | - | - | - | 0.045103 | - | — |
| 8008 | **action positive** | - | - | - | - | 0.045133 | - | ~ |
| 8009 | **great longchenpa** | - | - | - | - | 0.045256 | - | ~ |
| 8010 | **numerous great sravakas** | - | - | - | - | 0.045308 | - | — |
| 8011 | **great sravakas** | - | - | - | - | 0.045938 | - | — |
| 8012 | **wonderful teacher forever** | - | - | - | - | 0.046127 | - | — |
| 8013 | **negative karmic** | - | - | - | - | 0.046268 | - | ~ |
| 8014 | **great sinner** | - | - | - | - | 0.046818 | - | — |
| 8015 | **great desire** | - | - | - | - | 0.046838 | - | — |
| 8016 | **great misfortune** | - | - | - | - | 0.046876 | - | — |
| 8017 | **future good** | - | - | - | - | 0.046898 | - | — |
| 8018 | **bodhisattva tradition** | - | - | - | - | 0.047022 | - | ~ |
| 8019 | **prajnaparamita teacher** | - | - | - | - | 0.047035 | - | — |
| 8020 | **king ajatasatru** | - | - | - | - | 0.047128 | - | — |
| 8021 | **great vairotsana** | - | - | - | - | 0.047814 | - | ~ |
| 8022 | **exceptionally great** | - | - | - | - | 0.047842 | - | — |
| 8023 | **daily practice** | - | - | - | - | 0.047939 | - | — |
| 8024 | **vast expanse** | - | - | - | - | 0.048003 | - | — |
| 8025 | **noble lord avalokitesvara** | - | - | - | - | 0.048050 | - | — |
| 8026 | **life complete** | - | - | - | - | 0.048064 | - | — |
| 8027 | **precious supreme path** | - | - | - | - | 0.048083 | - | ~ |
| 8028 | **beginningless time** | - | - | - | - | 0.048300 | - | — |
| 8029 | **single instant** | - | - | - | - | 0.048487 | - | — |
| 8030 | **harmful spirit** | - | - | - | - | 0.048933 | - | — |
| 8031 | **past good** | - | - | - | - | 0.049205 | - | — |
| 8032 | **vajra seat** | - | - | - | - | 0.049233 | - | ✓ རྡོ་རྗེ་གདན |
| 8033 | **entire time** | - | - | - | - | 0.049688 | - | — |
| 8034 | **unsurpassable secret mantra** | - | - | - | - | 0.049927 | - | — |
| 8035 | **feel great sadness** | - | - | - | - | 0.049931 | - | — |
| 8036 | **take care** | - | - | - | - | 0.050005 | - | — |
| 8037 | **perfect enlightenment** | - | - | - | - | 0.050020 | - | — |
| 8038 | **authentic spiritual** | - | - | - | - | 0.050154 | - | — |
| 8039 | **teacher buddha** | - | - | - | - | 0.050223 | - | ~ |
| 8040 | **great abbot** | - | - | - | - | 0.050352 | - | ~ |
| 8041 | **entire human life** | - | - | - | - | 0.050601 | - | — |
| 8042 | **central tibet** | - | - | - | - | 0.050615 | - | — |
| 8043 | **master jowo** | - | - | - | - | 0.050616 | - | ~ |
| 8044 | **dharma people** | - | - | - | - | 0.050623 | - | — |
| 8045 | **great smrtijnana** | - | - | - | - | 0.050646 | - | — |
| 8046 | **true nature** | - | - | - | - | 0.050671 | - | ~ |
| 8047 | **good intention** | - | - | - | - | 0.050821 | - | — |
| 8048 | **bad thought** | - | - | - | - | 0.050898 | - | — |
| 8049 | **noble teacher** | - | - | - | - | 0.050977 | - | ~ |
| 8050 | **omniscient buddhahood** | - | - | - | - | 0.051339 | - | — |
| 8051 | **great fault** | - | - | - | - | 0.051370 | - | — |
| 8052 | **ordinary body** | - | - | - | - | 0.051402 | - | ~ |
| 8053 | **hell live** | - | - | - | - | 0.051473 | - | — |
| 8054 | **practise good** | - | - | - | - | 0.051520 | - | — |
| 8055 | **feel great affection** | - | - | - | - | 0.051629 | - | — |
| 8056 | **wrathful mother** | - | - | - | - | 0.052055 | - | ~ |
| 8057 | **great middle** | - | - | - | - | 0.052161 | - | ~ |
| 8058 | **derive great benefit** | - | - | - | - | 0.052231 | - | — |
| 8059 | **precious human** | - | - | - | - | 0.052242 | - | — |
| 8060 | **black spearman** | - | - | - | - | 0.052396 | - | — |
| 8061 | **positive effect** | - | - | - | - | 0.052706 | - | ~ |
| 8062 | **king golden crest** | - | - | - | - | 0.052806 | - | — |
| 8063 | **supreme teachers** | - | - | - | - | 0.052846 | - | — |
| 8064 | **dedicate merit** | - | - | - | - | 0.053150 | - | — |
| 8065 | **teacher forever** | - | - | - | - | 0.053279 | - | — |
| 8066 | **dharma free** | - | - | - | - | 0.053461 | - | ~ |
| 8067 | **dharma give** | - | - | - | - | 0.053673 | - | — |
| 8068 | **actual practice** | - | - | - | - | 0.053815 | - | — |
| 8069 | **great siddha lingje** | - | - | - | - | 0.053839 | - | ~ |
| 8070 | **giving dharma** | - | - | - | - | 0.053867 | - | — |
| 8071 | **profound teaching** | - | - | - | - | 0.054041 | - | ~ |
| 8072 | **drom tonpa** | - | - | - | - | 0.054452 | - | ✓ འབྲོམ་སྟོན་པ |
| 8073 | **great avalokitdvara** | - | - | - | - | 0.054907 | - | — |
| 8074 | **true path** | - | - | - | - | 0.055065 | - | ~ |
| 8075 | **small good** | - | - | - | - | 0.055294 | - | ~ |
| 8076 | **perfection lineage** | - | - | - | - | 0.055340 | - | ~ |
| 8077 | **great outer** | - | - | - | - | 0.055350 | - | ~ |
| 8078 | **vajra body enter** | - | - | - | - | 0.055424 | - | — |
| 8079 | **dharma like ambrosia** | - | - | - | - | 0.055487 | - | — |
| 8080 | **pure buddhafield** | - | - | - | - | 0.055665 | - | — |
| 8081 | **master nagarjuna** | - | - | - | - | 0.055766 | - | ~ |
| 8082 | **glorious root** | - | - | - | - | 0.055939 | - | ~ |
| 8083 | **refuge prayer** | - | - | - | - | 0.056083 | - | — |
| 8084 | **teacher venerable** | - | - | - | - | 0.056140 | - | — |
| 8085 | **past generosity** | - | - | - | - | 0.056176 | - | — |
| 8086 | **dharmodgata teaching** | - | - | - | - | 0.056198 | - | ~ |
| 8087 | **harmful act** | - | - | - | - | 0.056306 | - | — |
| 8088 | **omniscient longchenpa** | - | - | - | - | 0.056504 | - | ~ |
| 8089 | **human birth** | - | - | - | - | 0.056713 | - | — |
| 8090 | **great accumulation** | - | - | - | - | 0.056838 | - | — |
| 8091 | **moment mila** | - | - | - | - | 0.056949 | - | ~ |
| 8092 | **shang rinpoche** | - | - | - | - | 0.057107 | - | ✓ བླ་མ་ཞང་རིན་པོ་ཆེ |
| 8093 | **vajra posture** | - | - | - | - | 0.057190 | - | ✓ རྡོ་རྗེ་དཀྱིལ་ཀྲུང |
| 8094 | **human world** | - | - | - | - | 0.057459 | - | — |
| 8095 | **great siddha melong** | - | - | - | - | 0.057715 | - | ~ |
| 8096 | **great hard** | - | - | - | - | 0.057804 | - | — |
| 8097 | **great howling** | - | - | - | - | 0.057817 | - | — |
| 8098 | **precious jetsun** | - | - | - | - | 0.057822 | - | ~ |
| 8099 | **important people** | - | - | - | - | 0.057900 | - | — |
| 8100 | **great lotus like** | - | - | - | - | 0.057972 | - | — |
| 8101 | **perfect mind** | - | - | - | - | 0.058041 | - | — |
| 8102 | **dzogchen rinpoche** | - | - | - | - | 0.058404 | - | — |
| 8103 | **great courage giving** | - | - | - | - | 0.058744 | - | — |
| 8104 | **geshe langri thangpa** | - | - | - | - | 0.059179 | - | ~ |
| 8105 | **wrong thought** | - | - | - | - | 0.059386 | - | ~ |
| 8106 | **master aryadeva** | - | - | - | - | 0.059664 | - | ~ |
| 8107 | **bodhisattva samantabhadra ema** | - | - | - | - | 0.060355 | - | — |
| 8108 | **bodhisattva nivara** | - | - | - | - | 0.060662 | - | — |
| 8109 | **prayer beginning** | - | - | - | - | 0.061038 | - | — |
| 8110 | **lotus family** | - | - | - | - | 0.061098 | - | — |
| 8111 | **present human world** | - | - | - | - | 0.061471 | - | — |
| 8112 | **great translator rinchen** | - | - | - | - | 0.061472 | - | — |
| 8113 | **pure past** | - | - | - | - | 0.061601 | - | — |
| 8114 | **king padma** | - | - | - | - | 0.061679 | - | ~ |
| 8115 | **relative bodhicitta** | - | - | - | - | 0.061820 | - | ~ |
| 8116 | **bodhisattvas dissolve** | - | - | - | - | 0.061838 | - | — |
| 8117 | **excellent teacher** | - | - | - | - | 0.062082 | - | ~ |
| 8118 | **escape death** | - | - | - | - | 0.062510 | - | — |
| 8119 | **natural death** | - | - | - | - | 0.062836 | - | ~ |
| 8120 | **present time** | - | - | - | - | 0.063020 | - | — |
| 8121 | **great guide** | - | - | - | - | 0.063066 | - | — |
| 8122 | **ordinary speech** | - | - | - | - | 0.063100 | - | ~ |
| 8123 | **sick people** | - | - | - | - | 0.063113 | - | — |
| 8124 | **great exuberant** | - | - | - | - | 0.063287 | - | ~ |
| 8125 | **numerous great** | - | - | - | - | 0.063319 | - | — |
| 8126 | **mila joy** | - | - | - | - | 0.063560 | - | ~ |
| 8127 | **thousand samayas** | - | - | - | - | 0.063758 | - | ~ |
| 8128 | **intermediate kalpa** | - | - | - | - | 0.063786 | - | ~ |
| 8129 | **true mother** | - | - | - | - | 0.063851 | - | ~ |
| 8130 | **indian king** | - | - | - | - | 0.064130 | - | — |
| 8131 | **wisdom nectar** | - | - | - | - | 0.064269 | - | — |
| 8132 | **word vajra** | - | - | - | - | 0.064552 | - | ~ |
| 8133 | **jewels bless** | - | - | - | - | 0.064589 | - | — |
| 8134 | **master mafijusrimitra** | - | - | - | - | 0.064795 | - | — |
| 8135 | **central channel** | - | - | - | - | 0.064975 | - | ✓ རྩ་དབུ་མ |
| 8136 | **precious word empowerment** | - | - | - | - | 0.065036 | - | ✓ ཚིག་དབང་རིན་པོ་ཆེ |
| 8137 | **noble land** | - | - | - | - | 0.065046 | - | ~ |
| 8138 | **sublime katyayana** | - | - | - | - | 0.065205 | - | ~ |
| 8139 | **thousand mandala** | - | - | - | - | 0.065342 | - | ~ |
| 8140 | **people practise** | - | - | - | - | 0.065780 | - | — |
| 8141 | **day tilopa** | - | - | - | - | 0.065866 | - | — |
| 8142 | **life force** | - | - | - | - | 0.065887 | - | — |
| 8143 | **perfect spiritual friend** | - | - | - | - | 0.065893 | - | — |
| 8144 | **jewel garland** | - | - | - | - | 0.065919 | - | — |
| 8145 | **great yogi** | - | - | - | - | 0.066027 | - | — |
| 8146 | **teacher face** | - | - | - | - | 0.066064 | - | — |
| 8147 | **celestial realm** | - | - | - | - | 0.066287 | - | — |
| 8148 | **desire buddhahood** | - | - | - | - | 0.066509 | - | — |
| 8149 | **mind carefully** | - | - | - | - | 0.066705 | - | — |
| 8150 | **secret true** | - | - | - | - | 0.066746 | - | ~ |
| 8151 | **supreme path** | - | - | - | - | 0.067048 | - | ~ |
| 8152 | **samsara fall** | - | - | - | - | 0.067140 | - | — |
| 8153 | **true realization** | - | - | - | - | 0.067227 | - | — |
| 8154 | **sutra tantra** | - | - | - | - | 0.067338 | - | ~ |
| 8155 | **absolute bodhicitta** | - | - | - | - | 0.067349 | - | ~ |
| 8156 | **wish granting** | - | - | - | - | 0.067448 | - | — |
| 8157 | **omniscient jigme lingpa** | - | - | - | - | 0.067767 | - | ~ |
| 8158 | **preta realm** | - | - | - | - | 0.067806 | - | ~ |
| 8159 | **jewels spread** | - | - | - | - | 0.067916 | - | — |
| 8160 | **genuine spiritual teacher** | - | - | - | - | 0.068008 | - | — |
| 8161 | **great scholar vimalamitra** | - | - | - | - | 0.068293 | - | — |
| 8162 | **slight positive action** | - | - | - | - | 0.068336 | - | — |
| 8163 | **great ray** | - | - | - | - | 0.068352 | - | — |
| 8164 | **dark kalpas** | - | - | - | - | 0.068792 | - | — |
| 8165 | **pure intention** | - | - | - | - | 0.068796 | - | — |
| 8166 | **hundred thousand** | - | - | - | - | 0.068952 | - | ~ |
| 8167 | **compassionate action** | - | - | - | - | 0.069254 | - | ~ |
| 8168 | **kyobpa rinpoche** | - | - | - | - | 0.069445 | - | ~ |
| 8169 | **negative thought run** | - | - | - | - | 0.069455 | - | — |
| 8170 | **true meaning** | - | - | - | - | 0.070326 | - | ~ |
| 8171 | **wonderful teacher** | - | - | - | - | 0.070384 | - | — |
| 8172 | **great treasure** | - | - | - | - | 0.070386 | - | ~ |
| 8173 | **practise meditation** | - | - | - | - | 0.070445 | - | — |
| 8174 | **worldly people** | - | - | - | - | 0.070703 | - | — |
| 8175 | **virtuous practice** | - | - | - | - | 0.070781 | - | — |
| 8176 | **profound atiyoga teaching** | - | - | - | - | 0.071309 | - | ~ |
| 8177 | **real thing** | - | - | - | - | 0.071393 | - | — |
| 8178 | **ing negative effect** | - | - | - | - | 0.071482 | - | — |
| 8179 | **heart sutra** | - | - | - | - | 0.071525 | - | — |
| 8180 | **spiritual companion** | - | - | - | - | 0.072038 | - | — |
| 8181 | **single good dream** | - | - | - | - | 0.072068 | - | — |
| 8182 | **pure mind** | - | - | - | - | 0.072232 | - | ~ |
| 8183 | **conqueror sakyamuni** | - | - | - | - | 0.072313 | - | — |
| 8184 | **eighty thousand people** | - | - | - | - | 0.072490 | - | — |
| 8185 | **food drink** | - | - | - | - | 0.072525 | - | — |
| 8186 | **perfectly dedicate merit** | - | - | - | - | 0.072738 | - | — |
| 8187 | **great universal** | - | - | - | - | 0.072883 | - | ~ |
| 8188 | **solitary place** | - | - | - | - | 0.072995 | - | — |
| 8189 | **bodhisattva sam** | - | - | - | - | 0.073065 | - | — |
| 8190 | **live forever** | - | - | - | - | 0.073091 | - | — |
| 8191 | **undergo great** | - | - | - | - | 0.073140 | - | — |
| 8192 | **black true** | - | - | - | - | 0.073318 | - | ~ |
| 8193 | **great energy** | - | - | - | - | 0.073362 | - | ~ |
| 8194 | **jewel chest** | - | - | - | - | 0.073568 | - | — |
| 8195 | **bring benefit** | - | - | - | - | 0.073684 | - | — |
| 8196 | **indian master diparhkara** | - | - | - | - | 0.074028 | - | — |
| 8197 | **great confidence** | - | - | - | - | 0.074129 | - | — |
| 8198 | **lord padampa** | - | - | - | - | 0.074217 | - | ~ |
| 8199 | **evil mind** | - | - | - | - | 0.074270 | - | — |
| 8200 | **point lord** | - | - | - | - | 0.074311 | - | ~ |
| 8201 | **extraordinary teacher** | - | - | - | - | 0.074524 | - | — |
| 8202 | **great difficulty** | - | - | - | - | 0.074633 | - | — |
| 8203 | **vast mind** | - | - | - | - | 0.075050 | - | — |
| 8204 | **food offering** | - | - | - | - | 0.075100 | - | — |
| 8205 | **ordinary person** | - | - | - | - | 0.075182 | - | — |
| 8206 | **mind free** | - | - | - | - | 0.075205 | - | ~ |
| 8207 | **great elapatra** | - | - | - | - | 0.075323 | - | — |
| 8208 | **great stupa** | - | - | - | - | 0.075439 | - | ~ |
| 8209 | **single teaching** | - | - | - | - | 0.075609 | - | — |
| 8210 | **great marvellous** | - | - | - | - | 0.075614 | - | — |
| 8211 | **great courage** | - | - | - | - | 0.075752 | - | — |
| 8212 | **supreme accomplishment** | - | - | - | - | 0.075815 | - | ✓ མཆོག་གི་དངོས་གྲུབ |
| 8213 | **prince great** | - | - | - | - | 0.075931 | - | — |
| 8214 | **bright kalpa** | - | - | - | - | 0.076548 | - | — |
| 8215 | **powerful king** | - | - | - | - | 0.077466 | - | — |
| 8216 | **good spiritual** | - | - | - | - | 0.077522 | - | ~ |
| 8217 | **secret essence** | - | - | - | - | 0.077611 | - | ~ |
| 8218 | **great mistake** | - | - | - | - | 0.077934 | - | — |
| 8219 | **practise true** | - | - | - | - | 0.077972 | - | — |
| 8220 | **master padma** | - | - | - | - | 0.078221 | - | ~ |
| 8221 | **wish harm** | - | - | - | - | 0.078265 | - | — |
| 8222 | **great skull** | - | - | - | - | 0.078398 | - | ~ |
| 8223 | **tirthika teacher** | - | - | - | - | 0.078525 | - | ~ |
| 8224 | **garab dorje set** | - | - | - | - | 0.078643 | - | — |
| 8225 | **ordinary death** | - | - | - | - | 0.078784 | - | ~ |
| 8226 | **large number** | - | - | - | - | 0.079187 | - | — |
| 8227 | **true teaching** | - | - | - | - | 0.079800 | - | ~ |
| 8228 | **geshe chengawa** | - | - | - | - | 0.079871 | - | ~ |
| 8229 | **unbearable compassion** | - | - | - | - | 0.080023 | - | — |
| 8230 | **practise cho** | - | - | - | - | 0.080376 | - | — |
| 8231 | **lower left hand** | - | - | - | - | 0.080392 | - | — |
| 8232 | **great mindfulness** | - | - | - | - | 0.080922 | - | — |
| 8233 | **good nature** | - | - | - | - | 0.081182 | - | ~ |
| 8234 | **bring suffering** | - | - | - | - | 0.081208 | - | — |
| 8235 | **indian master** | - | - | - | - | 0.081380 | - | — |
| 8236 | **oddiyana points** | - | - | - | - | 0.081467 | - | — |
| 8237 | **day long** | - | - | - | - | 0.081623 | - | — |
| 8238 | **human speech** | - | - | - | - | 0.081794 | - | — |
| 8239 | **immense suffering** | - | - | - | - | 0.081891 | - | — |
| 8240 | **tsa tsa** | - | - | - | - | 0.082258 | - | ~ |
| 8241 | **love life** | - | - | - | - | 0.082334 | - | — |
| 8242 | **kadampa masters** | - | - | - | - | 0.082533 | - | — |
| 8243 | **great yogi virupa** | - | - | - | - | 0.083068 | - | — |
| 8244 | **noble master** | - | - | - | - | 0.083129 | - | ~ |
| 8245 | **time difficult** | - | - | - | - | 0.083142 | - | — |
| 8246 | **noble lord** | - | - | - | - | 0.083162 | - | ~ |
| 8247 | **vajra sattva** | - | - | - | - | 0.083209 | - | — |
| 8248 | **seventh bodhisattva level** | - | - | - | - | 0.083209 | - | — |
| 8249 | **confident faith** | - | - | - | - | 0.083330 | - | — |
| 8250 | **single lifetime** | - | - | - | - | 0.083509 | - | — |
| 8251 | **skull cup** | - | - | - | - | 0.083962 | - | ✓ ཐོད་ཕོར |
| 8252 | **present practice** | - | - | - | - | 0.083979 | - | — |
| 8253 | **guru padma** | - | - | - | - | 0.084357 | - | ~ |
| 8254 | **generation phase** | - | - | - | - | 0.084528 | - | ✓ བསྐྱེད་རིམ |
| 8255 | **king virudhaka** | - | - | - | - | 0.084566 | - | — |
| 8256 | **guru padma siddhi** | - | - | - | - | 0.084673 | - | ~ |
| 8257 | **sublime lord** | - | - | - | - | 0.084713 | - | ~ |
| 8258 | **essential nature** | - | - | - | - | 0.084746 | - | ~ |
| 8259 | **heart essence** | - | - | - | - | 0.085173 | - | — |
| 8260 | **ordinary tree** | - | - | - | - | 0.085388 | - | ~ |
| 8261 | **people follow** | - | - | - | - | 0.085534 | - | — |
| 8262 | **mila sherab gyaltsen** | - | - | - | - | 0.085834 | - | — |
| 8263 | **accomplishment mandala** | - | - | - | - | 0.085867 | - | ~ |
| 8264 | **ordinary form** | - | - | - | - | 0.086240 | - | — |
| 8265 | **supreme master** | - | - | - | - | 0.086275 | - | ~ |
| 8266 | **human flesh** | - | - | - | - | 0.086284 | - | — |
| 8267 | **true existence** | - | - | - | - | 0.086398 | - | ~ |
| 8268 | **seventh bodhisattva** | - | - | - | - | 0.086439 | - | — |
| 8269 | **extraordinary faith** | - | - | - | - | 0.086598 | - | — |
| 8270 | **great primordial** | - | - | - | - | 0.087022 | - | ~ |
| 8271 | **geshe potowa** | - | - | - | - | 0.087068 | - | ~ |
| 8272 | **important thing** | - | - | - | - | 0.087108 | - | — |
| 8273 | **food clothing** | - | - | - | - | 0.087159 | - | — |
| 8274 | **god realm** | - | - | - | - | 0.087288 | - | — |
| 8275 | **innumerable kalpas** | - | - | - | - | 0.087293 | - | — |
| 8276 | **indian siddha naropa** | - | - | - | - | 0.087571 | - | — |
| 8277 | **present teaching** | - | - | - | - | 0.088118 | - | — |
| 8278 | **eastern india** | - | - | - | - | 0.088218 | - | — |
| 8279 | **great rejoicing** | - | - | - | - | 0.088622 | - | — |
| 8280 | **great deal** | - | - | - | - | 0.089707 | - | — |
| 8281 | **human body** | - | - | - | - | 0.089727 | - | — |
| 8282 | **extremely negative** | - | - | - | - | 0.089908 | - | — |
| 8283 | **yoga tantra** | - | - | - | - | 0.090055 | - | ~ |
| 8284 | **great evil doer** | - | - | - | - | 0.090336 | - | — |
| 8285 | **bodhisattvas undertake** | - | - | - | - | 0.090596 | - | — |
| 8286 | **jewels render** | - | - | - | - | 0.090801 | - | — |
| 8287 | **perfect kalpa** | - | - | - | - | 0.090848 | - | — |
| 8288 | **vajrayana path** | - | - | - | - | 0.091027 | - | ~ |
| 8289 | **central place** | - | - | - | - | 0.091419 | - | — |
| 8290 | **jowo sakyamuni** | - | - | - | - | 0.091442 | - | — |
| 8291 | **great sadness** | - | - | - | - | 0.091575 | - | — |
| 8292 | **evil karma** | - | - | - | - | 0.091744 | - | — |
| 8293 | **venerable master** | - | - | - | - | 0.091835 | - | — |
| 8294 | **embrace great** | - | - | - | - | 0.091918 | - | — |
| 8295 | **powerful secret** | - | - | - | - | 0.092064 | - | — |
| 8296 | **great moving** | - | - | - | - | 0.092064 | - | — |
| 8297 | **find happiness** | - | - | - | - | 0.092157 | - | — |
| 8298 | **ninefold black cho** | - | - | - | - | 0.092220 | - | — |
| 8299 | **precious word** | - | - | - | - | 0.092546 | - | ~ |
| 8300 | **virtuous action** | - | - | - | - | 0.092587 | - | — |
| 8301 | **avoid negative** | - | - | - | - | 0.092900 | - | — |
| 8302 | **good suffer** | - | - | - | - | 0.093062 | - | — |
| 8303 | **great relish** | - | - | - | - | 0.093137 | - | — |
| 8304 | **mind workable** | - | - | - | - | 0.093388 | - | — |
| 8305 | **geshe shawopa** | - | - | - | - | 0.093478 | - | — |
| 8306 | **great arrogance** | - | - | - | - | 0.093590 | - | — |
| 8307 | **great affection** | - | - | - | - | 0.093693 | - | — |
| 8308 | **single hair** | - | - | - | - | 0.093768 | - | — |
| 8309 | **perfect body** | - | - | - | - | 0.093859 | - | — |
| 8310 | **body perfect** | - | - | - | - | 0.093859 | - | — |
| 8311 | **tantric samayas** | - | - | - | - | 0.093883 | - | — |
| 8312 | **geshe kharak** | - | - | - | - | 0.093960 | - | ~ |
| 8313 | **practice transference** | - | - | - | - | 0.093972 | - | — |
| 8314 | **transference practice** | - | - | - | - | 0.093972 | - | — |
| 8315 | **secret empowerment** | - | - | - | - | 0.094305 | - | ✓ གསང་དབང |
| 8316 | **ordinary human simply** | - | - | - | - | 0.094309 | - | — |
| 8317 | **king manicuda** | - | - | - | - | 0.094313 | - | — |
| 8318 | **vital point** | - | - | - | - | 0.094496 | - | — |
| 8319 | **feel love** | - | - | - | - | 0.094531 | - | — |
| 8320 | **extremely negative act** | - | - | - | - | 0.094563 | - | — |
| 8321 | **live human** | - | - | - | - | 0.094645 | - | — |
| 8322 | **black cho** | - | - | - | - | 0.094712 | - | ~ |
| 8323 | **black horse lama** | - | - | - | - | 0.094746 | - | — |
| 8324 | **single negative** | - | - | - | - | 0.094831 | - | — |
| 8325 | **time training** | - | - | - | - | 0.095055 | - | — |
| 8326 | **great renown** | - | - | - | - | 0.095063 | - | — |
| 8327 | **absolute cho** | - | - | - | - | 0.095191 | - | ~ |
| 8328 | **teacher explain** | - | - | - | - | 0.095250 | - | — |
| 8329 | **important practice** | - | - | - | - | 0.095416 | - | — |
| 8330 | **derive great** | - | - | - | - | 0.095426 | - | — |
| 8331 | **great sincerity** | - | - | - | - | 0.095588 | - | — |
| 8332 | **great paqc** | - | - | - | - | 0.095701 | - | — |
| 8333 | **great paqqita** | - | - | - | - | 0.095759 | - | — |
| 8334 | **master dharmaraksita** | - | - | - | - | 0.096001 | - | — |
| 8335 | **practise real** | - | - | - | - | 0.096002 | - | — |
| 8336 | **practise taking** | - | - | - | - | 0.096240 | - | — |
| 8337 | **teacher stand** | - | - | - | - | 0.096422 | - | — |
| 8338 | **people die** | - | - | - | - | 0.096428 | - | — |
| 8339 | **teacher skilfully** | - | - | - | - | 0.096452 | - | — |
| 8340 | **hell suffer** | - | - | - | - | 0.096612 | - | — |
| 8341 | **basic vehicle** | - | - | - | - | 0.096747 | - | — |
| 8342 | **noble spiritual friend** | - | - | - | - | 0.097105 | - | ~ |
| 8343 | **guru sri simha** | - | - | - | - | 0.097121 | - | — |
| 8344 | **single day** | - | - | - | - | 0.097123 | - | — |
| 8345 | **positive thought** | - | - | - | - | 0.097438 | - | ~ |
| 8346 | **buddhist teaching** | - | - | - | - | 0.097554 | - | — |
| 8347 | **great gusto** | - | - | - | - | 0.097563 | - | — |
| 8348 | **great inseparability** | - | - | - | - | 0.097640 | - | — |
| 8349 | **order great** | - | - | - | - | 0.097701 | - | — |
| 8350 | **great fervour** | - | - | - | - | 0.097707 | - | — |
| 8351 | **great evenness** | - | - | - | - | 0.097709 | - | — |
| 8352 | **great pal** | - | - | - | - | 0.097717 | - | ~ |
| 8353 | **great equality** | - | - | - | - | 0.097717 | - | ~ |
| 8354 | **yeshe tsogyal** | - | - | - | - | 0.097740 | - | ✓ ཡེ་ཤེས་མཚོ་རྒྱལ |
| 8355 | **renounce taking** | - | - | - | - | 0.097805 | - | — |
| 8356 | **people die suddenly** | - | - | - | - | 0.097838 | - | — |
| 8357 | **transcendent generosity** | - | - | - | - | 0.097840 | - | ~ |
| 8358 | **compassionate heart** | - | - | - | - | 0.097905 | - | — |
| 8359 | **glorious vajrasattva** | - | - | - | - | 0.098087 | - | ~ |
| 8360 | **mother bird taking** | - | - | - | - | 0.099149 | - | — |
| 8361 | **single tibetan** | - | - | - | - | 0.099445 | - | — |
| 8362 | **profound meaning** | - | - | - | - | 0.099535 | - | ~ |
| 8363 | **dead person** | - | - | - | - | 0.099537 | - | — |
| 8364 | **action properly** | - | - | - | - | 0.099590 | - | — |
| 8365 | **relative buddhahood** | - | - | - | - | 0.100107 | - | — |
| 8366 | **endless suffering** | - | - | - | - | 0.100144 | - | — |
| 8367 | **mantrayana tantras** | - | - | - | - | 0.100258 | - | — |
| 8368 | **mount malaya** | - | - | - | - | 0.100824 | - | — |
| 8369 | **king trisongdetsen** | - | - | - | - | 0.101001 | - | — |
| 8370 | **ordinary transference** | - | - | - | - | 0.101044 | - | ~ |
| 8371 | **atiyoga teaching** | - | - | - | - | 0.101108 | - | ~ |
| 8372 | **holy teacher** | - | - | - | - | 0.101159 | - | — |
| 8373 | **king golden** | - | - | - | - | 0.101299 | - | — |
| 8374 | **animal realm** | - | - | - | - | 0.101344 | - | — |
| 8375 | **supreme spiritual friend** | - | - | - | - | 0.101641 | - | ~ |
| 8376 | **people present** | - | - | - | - | 0.101693 | - | — |
| 8377 | **incomparable dagpo rinpoche** | - | - | - | - | 0.101856 | - | — |
| 8378 | **geshe kharak gomchung** | - | - | - | - | 0.101939 | - | ~ |
| 8379 | **lord mafijusri** | - | - | - | - | 0.102317 | - | — |
| 8380 | **king uparaja** | - | - | - | - | 0.102363 | - | — |
| 8381 | **king gomadeviya** | - | - | - | - | 0.102392 | - | — |
| 8382 | **profound practice** | - | - | - | - | 0.102917 | - | — |
| 8383 | **western buddhafield** | - | - | - | - | 0.103138 | - | — |
| 8384 | **teacher spiritual** | - | - | - | - | 0.103580 | - | ~ |
| 8385 | **clear sky** | - | - | - | - | 0.103667 | - | — |
| 8386 | **absolute wisdom** | - | - | - | - | 0.103695 | - | ~ |
| 8387 | **mila thopa** | - | - | - | - | 0.103700 | - | — |
| 8388 | **mila sherab** | - | - | - | - | 0.103704 | - | — |
| 8389 | **past positive** | - | - | - | - | 0.103852 | - | — |
| 8390 | **experience suffering** | - | - | - | - | 0.103889 | - | ~ |
| 8391 | **thousand million** | - | - | - | - | 0.103933 | - | — |
| 8392 | **authentic refuge vow** | - | - | - | - | 0.103957 | - | — |
| 8393 | **secret tantric samayas** | - | - | - | - | 0.104151 | - | — |
| 8394 | **ordinary giving** | - | - | - | - | 0.104218 | - | — |
| 8395 | **short time** | - | - | - | - | 0.104311 | - | — |
| 8396 | **open mind** | - | - | - | - | 0.104312 | - | — |
| 8397 | **practice perfectly** | - | - | - | - | 0.104697 | - | — |
| 8398 | **head cut** | - | - | - | - | 0.104760 | - | — |
| 8399 | **transference prayer** | - | - | - | - | 0.104928 | - | — |
| 8400 | **true absolute bodhicitta** | - | - | - | - | 0.105193 | - | ~ |
| 8401 | **master tendzin** | - | - | - | - | 0.105333 | - | — |
| 8402 | **noble mafijusri** | - | - | - | - | 0.105670 | - | — |
| 8403 | **physical action** | - | - | - | - | 0.105722 | - | — |
| 8404 | **vajra speech** | - | - | - | - | 0.105784 | - | ~ |
| 8405 | **shepa dorje** | - | - | - | - | 0.105814 | - | — |
| 8406 | **vajra essence** | - | - | - | - | 0.105857 | - | ~ |
| 8407 | **mind completely** | - | - | - | - | 0.106141 | - | — |
| 8408 | **mila adamantine** | - | - | - | - | 0.106288 | - | ~ |
| 8409 | **immense compassion** | - | - | - | - | 0.106360 | - | — |
| 8410 | **experience immense suffering** | - | - | - | - | 0.106921 | - | — |
| 8411 | **perfectly pure intention** | - | - | - | - | 0.107534 | - | — |
| 8412 | **head lama** | - | - | - | - | 0.108132 | - | — |
| 8413 | **good worldly** | - | - | - | - | 0.109074 | - | ~ |
| 8414 | **syllable hum** | - | - | - | - | 0.109327 | - | — |
| 8415 | **miraculous power** | - | - | - | - | 0.109895 | - | — |
| 8416 | **profoundly secret true** | - | - | - | - | 0.110304 | - | — |
| 8417 | **pure realm** | - | - | - | - | 0.110366 | - | ~ |
| 8418 | **brahma heavens** | - | - | - | - | 0.110468 | - | — |
| 8419 | **attain enlightenment** | - | - | - | - | 0.110476 | - | — |
| 8420 | **guru sri** | - | - | - | - | 0.110490 | - | — |
| 8421 | **lotus light** | - | - | - | - | 0.110740 | - | ~ |
| 8422 | **pure meaning** | - | - | - | - | 0.110915 | - | ~ |
| 8423 | **glorious protector** | - | - | - | - | 0.110944 | - | ~ |
| 8424 | **lack food** | - | - | - | - | 0.111150 | - | — |
| 8425 | **red light** | - | - | - | - | 0.111302 | - | — |
| 8426 | **powerful positive act** | - | - | - | - | 0.112237 | - | — |
| 8427 | **vajra speech enter** | - | - | - | - | 0.112838 | - | — |
| 8428 | **rinchen zangpo** | - | - | - | - | 0.113100 | - | ✓ རིན་ཆེན་བཟང་པོ |
| 8429 | **present day** | - | - | - | - | 0.113566 | - | — |
| 8430 | **real meaning** | - | - | - | - | 0.114211 | - | ✓ ངེས་དོན |
| 8431 | **king mandhatri** | - | - | - | - | 0.114522 | - | ~ |
| 8432 | **jowo ben** | - | - | - | - | 0.114651 | - | — |
| 8433 | **extraordinary secret** | - | - | - | - | 0.114887 | - | — |
| 8434 | **universal king** | - | - | - | - | 0.115016 | - | ~ |
| 8435 | **pure path** | - | - | - | - | 0.115301 | - | ~ |
| 8436 | **find tilopa** | - | - | - | - | 0.115606 | - | — |
| 8437 | **mind training** | - | - | - | - | 0.115722 | - | ~ |
| 8438 | **master tendzin chopel** | - | - | - | - | 0.116170 | - | — |
| 8439 | **jetsun rangrik repa** | - | - | - | - | 0.116193 | - | — |
| 8440 | **single prostration** | - | - | - | - | 0.116446 | - | — |
| 8441 | **master jetari** | - | - | - | - | 0.116468 | - | — |
| 8442 | **excellent mountain** | - | - | - | - | 0.116712 | - | ~ |
| 8443 | **conditioning effect** | - | - | - | - | 0.116865 | - | ✓ དབང་གི་འབྲས་བུ |
| 8444 | **white lotus** | - | - | - | - | 0.116873 | - | ~ |
| 8445 | **buddhas body** | - | - | - | - | 0.116993 | - | ~ |
| 8446 | **false spiritual friend** | - | - | - | - | 0.117021 | - | — |
| 8447 | **innumerable hell** | - | - | - | - | 0.117068 | - | — |
| 8448 | **action slip** | - | - | - | - | 0.117431 | - | — |
| 8449 | **geshe langri** | - | - | - | - | 0.117975 | - | ~ |
| 8450 | **precious mountain** | - | - | - | - | 0.117988 | - | ~ |
| 8451 | **lightly small good** | - | - | - | - | 0.118265 | - | — |
| 8452 | **mount merus** | - | - | - | - | 0.118358 | - | — |
| 8453 | **authentic teaching** | - | - | - | - | 0.118401 | - | — |
| 8454 | **practise generosity** | - | - | - | - | 0.118571 | - | — |
| 8455 | **single lama** | - | - | - | - | 0.118615 | - | — |
| 8456 | **perfect faith** | - | - | - | - | 0.118889 | - | — |
| 8457 | **head call** | - | - | - | - | 0.118985 | - | — |
| 8458 | **absolute bodhicitta present** | - | - | - | - | 0.119196 | - | — |
| 8459 | **eastern buddhafield** | - | - | - | - | 0.119404 | - | — |
| 8460 | **qualified teacher** | - | - | - | - | 0.119415 | - | — |
| 8461 | **true bodhicitta** | - | - | - | - | 0.119463 | - | ~ |
| 8462 | **lita naropa** | - | - | - | - | 0.119828 | - | — |
| 8463 | **vast path** | - | - | - | - | 0.119987 | - | — |
| 8464 | **gracious root** | - | - | - | - | 0.120037 | - | — |
| 8465 | **hevajra tantra** | - | - | - | - | 0.120214 | - | — |
| 8466 | **realize emptiness** | - | - | - | - | 0.120375 | - | — |
| 8467 | **master diparhkara** | - | - | - | - | 0.120816 | - | — |
| 8468 | **dodrup chen** | - | - | - | - | 0.120836 | - | — |
| 8469 | **follow sakyamuni** | - | - | - | - | 0.121570 | - | — |
| 8470 | **achieve buddhahood** | - | - | - | - | 0.122630 | - | — |
| 8471 | **red mountain palace** | - | - | - | - | 0.122869 | - | — |
| 8472 | **fritter life** | - | - | - | - | 0.123644 | - | — |
| 8473 | **precious metal** | - | - | - | - | 0.124011 | - | — |
| 8474 | **phoney lama** | - | - | - | - | 0.124021 | - | — |
| 8475 | **mother bird** | - | - | - | - | 0.124625 | - | — |
| 8476 | **give rise** | - | - | - | - | 0.124683 | - | — |
| 8477 | **reason guru** | - | - | - | - | 0.125223 | - | — |
| 8478 | **evil rebirth** | - | - | - | - | 0.125445 | - | — |
| 8479 | **harmful negative** | - | - | - | - | 0.125698 | - | — |
| 8480 | **single drop** | - | - | - | - | 0.125710 | - | — |
| 8481 | **good karma** | - | - | - | - | 0.125926 | - | ~ |
| 8482 | **precious wheel** | - | - | - | - | 0.125978 | - | ~ |
| 8483 | **local people** | - | - | - | - | 0.126178 | - | — |
| 8484 | **tingdzin zangpo** | - | - | - | - | 0.126198 | - | ~ |
| 8485 | **entire life** | - | - | - | - | 0.126415 | - | — |
| 8486 | **worldly activity** | - | - | - | - | 0.126721 | - | ~ |
| 8487 | **ordinary worldly** | - | - | - | - | 0.127745 | - | ~ |
| 8488 | **death finally** | - | - | - | - | 0.127977 | - | — |
| 8489 | **powerful people** | - | - | - | - | 0.128025 | - | — |
| 8490 | **naropa set** | - | - | - | - | 0.128204 | - | — |
| 8491 | **moon lamp sutra** | - | - | - | - | 0.128304 | - | — |
| 8492 | **young brahmin** | - | - | - | - | 0.128490 | - | — |
| 8493 | **innate absolute wisdom** | - | - | - | - | 0.128653 | - | ~ |
| 8494 | **sutra pisaka** | - | - | - | - | 0.128867 | - | — |
| 8495 | **auspicious day** | - | - | - | - | 0.128927 | - | — |
| 8496 | **noble path** | - | - | - | - | 0.129001 | - | ~ |
| 8497 | **jetsun shepa** | - | - | - | - | 0.129023 | - | — |
| 8498 | **ultimate cho** | - | - | - | - | 0.129331 | - | — |
| 8499 | **good age** | - | - | - | - | 0.129400 | - | ~ |
| 8500 | **mind enter** | - | - | - | - | 0.129431 | - | — |
| 8501 | **lord suvarl** | - | - | - | - | 0.130111 | - | — |
| 8502 | **lord suvarnadvipa** | - | - | - | - | 0.130115 | - | ~ |
| 8503 | **pronged vajra** | - | - | - | - | 0.130217 | - | — |
| 8504 | **tathagata family** | - | - | - | - | 0.130307 | - | — |
| 8505 | **vajra core teaching** | - | - | - | - | 0.130352 | - | — |
| 8506 | **wonderful teaching** | - | - | - | - | 0.130447 | - | — |
| 8507 | **bodhicitta free** | - | - | - | - | 0.130537 | - | ~ |
| 8508 | **master chegom** | - | - | - | - | 0.130586 | - | — |
| 8509 | **period tibet** | - | - | - | - | 0.131028 | - | — |
| 8510 | **master hastibhala** | - | - | - | - | 0.131188 | - | — |
| 8511 | **perfect horse** | - | - | - | - | 0.131310 | - | — |
| 8512 | **gyalse rinpoche** | - | - | - | - | 0.131479 | - | ✓ རྒྱལ་སྲས་རིན་པོ་ཆེ |
| 8513 | **absolute teaching** | - | - | - | - | 0.131739 | - | ~ |
| 8514 | **ordinary god** | - | - | - | - | 0.131814 | - | — |
| 8515 | **black horse** | - | - | - | - | 0.131989 | - | — |
| 8516 | **refuge vow** | - | - | - | - | 0.132348 | - | — |
| 8517 | **secret tantric** | - | - | - | - | 0.132361 | - | — |
| 8518 | **excellent people** | - | - | - | - | 0.132404 | - | — |
| 8519 | **bodhicitta present** | - | - | - | - | 0.132422 | - | — |
| 8520 | **time immeasurable** | - | - | - | - | 0.132537 | - | — |
| 8521 | **mantra tradition** | - | - | - | - | 0.132680 | - | ~ |
| 8522 | **short life** | - | - | - | - | 0.132854 | - | — |
| 8523 | **bodhicitta vow** | - | - | - | - | 0.133321 | - | — |
| 8524 | **wisdom free** | - | - | - | - | 0.133778 | - | ~ |
| 8525 | **mantra mandala** | - | - | - | - | 0.134184 | - | ~ |
| 8526 | **blind man** | - | - | - | - | 0.134436 | - | — |
| 8527 | **practice patience** | - | - | - | - | 0.134756 | - | — |
| 8528 | **mind turn** | - | - | - | - | 0.134760 | - | — |
| 8529 | **supreme tilopa** | - | - | - | - | 0.134786 | - | ~ |
| 8530 | **authentic vajra** | - | - | - | - | 0.135243 | - | — |
| 8531 | **symbol lineage** | - | - | - | - | 0.135421 | - | ~ |
| 8532 | **sarhsara fritter life** | - | - | - | - | 0.135684 | - | — |
| 8533 | **ultimate refuge** | - | - | - | - | 0.135824 | - | — |
| 8534 | **bodhicitta meditation** | - | - | - | - | 0.136156 | - | ~ |
| 8535 | **negative karmic result** | - | - | - | - | 0.136162 | - | — |
| 8536 | **great scholar trakpa** | - | - | - | - | 0.136372 | - | — |
| 8537 | **mahayana sutras** | - | - | - | - | 0.136693 | - | — |
| 8538 | **absolute truth** | - | - | - | - | 0.136803 | - | ✓ དོན་དམ་བདེན་པ |
| 8539 | **vehicle tradition** | - | - | - | - | 0.136818 | - | ~ |
| 8540 | **ignorant people follow** | - | - | - | - | 0.137286 | - | — |
| 8541 | **degenerate time** | - | - | - | - | 0.137647 | - | — |
| 8542 | **protector nagarjuna** | - | - | - | - | 0.138068 | - | ~ |
| 8543 | **perform transference** | - | - | - | - | 0.138087 | - | — |
| 8544 | **sky yoga** | - | - | - | - | 0.138126 | - | — |
| 8545 | **people lack** | - | - | - | - | 0.138538 | - | — |
| 8546 | **find fault** | - | - | - | - | 0.138560 | - | — |
| 8547 | **time onwards** | - | - | - | - | 0.138740 | - | — |
| 8548 | **waste time** | - | - | - | - | 0.138828 | - | — |
| 8549 | **action consistent** | - | - | - | - | 0.139301 | - | — |
| 8550 | **dry land** | - | - | - | - | 0.139732 | - | — |
| 8551 | **jetsun rangrik** | - | - | - | - | 0.139894 | - | — |
| 8552 | **venerable geshe** | - | - | - | - | 0.140395 | - | — |
| 8553 | **good listening** | - | - | - | - | 0.141400 | - | — |
| 8554 | **omniscient state** | - | - | - | - | 0.141793 | - | ~ |
| 8555 | **relative good** | - | - | - | - | 0.141855 | - | ~ |
| 8556 | **strong mind** | - | - | - | - | 0.141955 | - | — |
| 8557 | **root text** | - | - | - | - | 0.141998 | - | — |
| 8558 | **practice train** | - | - | - | - | 0.142057 | - | — |
| 8559 | **present work** | - | - | - | - | 0.142132 | - | — |
| 8560 | **thought cease** | - | - | - | - | 0.142236 | - | — |
| 8561 | **good advice** | - | - | - | - | 0.142274 | - | — |
| 8562 | **good dream** | - | - | - | - | 0.142425 | - | — |
| 8563 | **poison jetsun** | - | - | - | - | 0.142493 | - | — |
| 8564 | **material giving** | - | - | - | - | 0.142902 | - | — |
| 8565 | **meditate persistently** | - | - | - | - | 0.142949 | - | — |
| 8566 | **nachung tonpa** | - | - | - | - | 0.143041 | - | — |
| 8567 | **father mother** | - | - | - | - | 0.143178 | - | — |
| 8568 | **ordinary people pretend** | - | - | - | - | 0.143462 | - | — |
| 8569 | **master alive** | - | - | - | - | 0.143665 | - | — |
| 8570 | **religious king** | - | - | - | - | 0.143820 | - | — |
| 8571 | **ordinary people partake** | - | - | - | - | 0.143852 | - | — |
| 8572 | **shearing time** | - | - | - | - | 0.144730 | - | — |
| 8573 | **people today** | - | - | - | - | 0.144745 | - | — |
| 8574 | **time lift** | - | - | - | - | 0.145055 | - | — |
| 8575 | **perfect happiness** | - | - | - | - | 0.145480 | - | — |
| 8576 | **transcendent concentration** | - | - | - | - | 0.145871 | - | ~ |
| 8577 | **approach practice** | - | - | - | - | 0.146146 | - | — |
| 8578 | **perfectly dedicate** | - | - | - | - | 0.146571 | - | — |
| 8579 | **people imagine** | - | - | - | - | 0.146739 | - | — |
| 8580 | **siddha naropa** | - | - | - | - | 0.146982 | - | ~ |
| 8581 | **vast attitude** | - | - | - | - | 0.147463 | - | — |
| 8582 | **bear death** | - | - | - | - | 0.148091 | - | — |
| 8583 | **hot food** | - | - | - | - | 0.148185 | - | — |
| 8584 | **harmful past** | - | - | - | - | 0.148194 | - | — |
| 8585 | **water tormas** | - | - | - | - | 0.148361 | - | — |
| 8586 | **perfect dedication** | - | - | - | - | 0.148472 | - | — |
| 8587 | **warm flesh** | - | - | - | - | 0.148728 | - | — |
| 8588 | **good tea** | - | - | - | - | 0.148742 | - | — |
| 8589 | **joyous realm** | - | - | - | - | 0.149053 | - | ✓ དགའ་ལྡན |
| 8590 | **padampa sangye heard** | - | - | - | - | 0.149169 | - | — |
| 8591 | **dear body** | - | - | - | - | 0.149336 | - | — |
| 8592 | **supreme wisdom** | - | - | - | - | 0.149396 | - | ~ |
| 8593 | **omniscient jigme** | - | - | - | - | 0.149522 | - | ~ |
| 8594 | **intense practice** | - | - | - | - | 0.149813 | - | — |
| 8595 | **prince great courage** | - | - | - | - | 0.150240 | - | — |
| 8596 | **feel natural love** | - | - | - | - | 0.150404 | - | — |
| 8597 | **kushab rinpoche** | - | - | - | - | 0.150435 | - | — |
| 8598 | **rinpoche shenpen** | - | - | - | - | 0.150435 | - | — |
| 8599 | **geshe chekawa** | - | - | - | - | 0.150630 | - | ~ |
| 8600 | **find food** | - | - | - | - | 0.150648 | - | — |
| 8601 | **completely pure** | - | - | - | - | 0.151177 | - | — |
| 8602 | **day chengawa** | - | - | - | - | 0.151324 | - | — |
| 8603 | **single year** | - | - | - | - | 0.151512 | - | — |
| 8604 | **superior mind** | - | - | - | - | 0.151587 | - | — |
| 8605 | **sri simha** | - | - | - | - | 0.152241 | - | — |
| 8606 | **western india** | - | - | - | - | 0.153455 | - | — |
| 8607 | **joyous kalpa** | - | - | - | - | 0.154030 | - | ~ |
| 8608 | **material offering** | - | - | - | - | 0.154136 | - | — |
| 8609 | **mind awareness** | - | - | - | - | 0.154175 | - | ~ |
| 8610 | **present human** | - | - | - | - | 0.154632 | - | — |
| 8611 | **sadaprarudita cut open** | - | - | - | - | 0.154654 | - | — |
| 8612 | **swift path** | - | - | - | - | 0.154672 | - | — |
| 8613 | **act positive** | - | - | - | - | 0.154729 | - | — |
| 8614 | **time swimming** | - | - | - | - | 0.154879 | - | — |
| 8615 | **geshe khampa** | - | - | - | - | 0.154917 | - | ~ |
| 8616 | **illusory body** | - | - | - | - | 0.154969 | - | — |
| 8617 | **teaching sror** | - | - | - | - | 0.155099 | - | — |
| 8618 | **geshe khampa lungpa** | - | - | - | - | 0.155285 | - | ~ |
| 8619 | **wrong food** | - | - | - | - | 0.155483 | - | — |
| 8620 | **state free** | - | - | - | - | 0.155770 | - | ~ |
| 8621 | **single person** | - | - | - | - | 0.155878 | - | — |
| 8622 | **heating hell** | - | - | - | - | 0.155978 | - | — |
| 8623 | **long run** | - | - | - | - | 0.156440 | - | — |
| 8624 | **long term** | - | - | - | - | 0.156726 | - | — |
| 8625 | **main practice train** | - | - | - | - | 0.156751 | - | — |
| 8626 | **perfect view** | - | - | - | - | 0.156794 | - | — |
| 8627 | **mind totally** | - | - | - | - | 0.156864 | - | — |
| 8628 | **sincere mind** | - | - | - | - | 0.156925 | - | — |
| 8629 | **wrong direction** | - | - | - | - | 0.156960 | - | — |
| 8630 | **single prayer** | - | - | - | - | 0.157130 | - | — |
| 8631 | **thousand bad** | - | - | - | - | 0.157608 | - | — |
| 8632 | **excellent kalpa** | - | - | - | - | 0.157704 | - | ~ |
| 8633 | **day day** | - | - | - | - | 0.157974 | - | — |
| 8634 | **kalpas time** | - | - | - | - | 0.158025 | - | — |
| 8635 | **moment bring** | - | - | - | - | 0.158068 | - | — |
| 8636 | **present state** | - | - | - | - | 0.158071 | - | — |
| 8637 | **path empowerment** | - | - | - | - | 0.158258 | - | ~ |
| 8638 | **authentic realization** | - | - | - | - | 0.158261 | - | — |
| 8639 | **central region** | - | - | - | - | 0.158331 | - | — |
| 8640 | **dorje set** | - | - | - | - | 0.158759 | - | — |
| 8641 | **perfect spiritual** | - | - | - | - | 0.158785 | - | — |
| 8642 | **distant past** | - | - | - | - | 0.159418 | - | — |
| 8643 | **sexual misconduct** | - | - | - | - | 0.159565 | - | — |
| 8644 | **vajra recitation** | - | - | - | - | 0.160408 | - | ✓ རྡོ་རྗེ་བཟླས་པ |
| 8645 | **bring happiness** | - | - | - | - | 0.160514 | - | — |
| 8646 | **good doctor** | - | - | - | - | 0.160539 | - | — |
| 8647 | **case death** | - | - | - | - | 0.160573 | - | — |
| 8648 | **precious supreme** | - | - | - | - | 0.160719 | - | ~ |
| 8649 | **leavingjetsun mila** | - | - | - | - | 0.160892 | - | — |
| 8650 | **askedjetsun mila** | - | - | - | - | 0.160982 | - | — |
| 8651 | **death suddenly** | - | - | - | - | 0.160986 | - | — |
| 8652 | **true benefit** | - | - | - | - | 0.161415 | - | — |
| 8653 | **sublime nagarjuna** | - | - | - | - | 0.161955 | - | ~ |
| 8654 | **body speech** | - | - | - | - | 0.162562 | - | ~ |
| 8655 | **cutter sutra** | - | - | - | - | 0.162932 | - | — |
| 8656 | **gonpo dorje** | - | - | - | - | 0.162988 | - | ~ |
| 8657 | **single grain** | - | - | - | - | 0.162991 | - | — |
| 8658 | **vast ocean** | - | - | - | - | 0.163522 | - | — |
| 8659 | **perfect vase** | - | - | - | - | 0.163565 | - | — |
| 8660 | **mind slip** | - | - | - | - | 0.163620 | - | — |
| 8661 | **omniscient primal wisdom** | - | - | - | - | 0.164082 | - | ~ |
| 8662 | **past perfectly** | - | - | - | - | 0.164276 | - | — |
| 8663 | **true primal wisdom** | - | - | - | - | 0.164813 | - | ~ |
| 8664 | **perfect secluded place** | - | - | - | - | 0.165102 | - | — |
| 8665 | **dakini yeshe tsogyal** | - | - | - | - | 0.165718 | - | ~ |
| 8666 | **live incalculably long** | - | - | - | - | 0.165787 | - | — |
| 8667 | **golden wheel** | - | - | - | - | 0.165914 | - | — |
| 8668 | **good meal** | - | - | - | - | 0.166955 | - | — |
| 8669 | **infinite buddhafield** | - | - | - | - | 0.167053 | - | — |
| 8670 | **golden vajra** | - | - | - | - | 0.167334 | - | — |
| 8671 | **mipham gonpo** | - | - | - | - | 0.167965 | - | — |
| 8672 | **ordinary folk** | - | - | - | - | 0.168118 | - | — |
| 8673 | **attachment hatred** | - | - | - | - | 0.168269 | - | — |
| 8674 | **ati vehicle** | - | - | - | - | 0.168458 | - | — |
| 8675 | **vajra bhumi** | - | - | - | - | 0.168694 | - | — |
| 8676 | **vajra rekhe** | - | - | - | - | 0.168695 | - | — |
| 8677 | **central buddhafield** | - | - | - | - | 0.168972 | - | — |
| 8678 | **scavenger offering** | - | - | - | - | 0.169007 | - | — |
| 8679 | **unsurpassable secret** | - | - | - | - | 0.169244 | - | — |
| 8680 | **jowo river** | - | - | - | - | 0.169468 | - | — |
| 8681 | **lingje repa** | - | - | - | - | 0.170227 | - | ✓ གླིང་རྗེ་རས་པ |
| 8682 | **perfect lake** | - | - | - | - | 0.170480 | - | — |
| 8683 | **manifestation garab dorje** | - | - | - | - | 0.170648 | - | — |
| 8684 | **bodhicitta arise** | - | - | - | - | 0.170677 | - | — |
| 8685 | **completely sincere mind** | - | - | - | - | 0.170695 | - | — |
| 8686 | **vajra throne** | - | - | - | - | 0.170843 | - | — |
| 8687 | **life slip** | - | - | - | - | 0.171104 | - | — |
| 8688 | **compassionate wisdom** | - | - | - | - | 0.171226 | - | ~ |
| 8689 | **find freedom** | - | - | - | - | 0.171594 | - | — |
| 8690 | **recognize suffering** | - | - | - | - | 0.171987 | - | — |
| 8691 | **omniscient longchen** | - | - | - | - | 0.172195 | - | — |
| 8692 | **dorje gyaltsen** | - | - | - | - | 0.172837 | - | ~ |
| 8693 | **chagme rinpoche** | - | - | - | - | 0.172853 | - | ~ |
| 8694 | **perfectly practise** | - | - | - | - | 0.172898 | - | — |
| 8695 | **sadaprarudita set** | - | - | - | - | 0.173152 | - | — |
| 8696 | **lotus hat** | - | - | - | - | 0.173207 | - | — |
| 8697 | **lake kutra** | - | - | - | - | 0.173363 | - | — |
| 8698 | **people spend** | - | - | - | - | 0.173383 | - | — |
| 8699 | **refuge simply** | - | - | - | - | 0.173563 | - | — |
| 8700 | **mental suffering** | - | - | - | - | 0.173645 | - | — |
| 8701 | **rigdzin changchub dorje** | - | - | - | - | 0.173799 | - | — |
| 8702 | **single point** | - | - | - | - | 0.173896 | - | — |
| 8703 | **sattva hum** | - | - | - | - | 0.174020 | - | — |
| 8704 | **sincere practice** | - | - | - | - | 0.174187 | - | — |
| 8705 | **hot metal** | - | - | - | - | 0.174667 | - | — |
| 8706 | **nirvana sutra** | - | - | - | - | 0.174790 | - | ~ |
| 8707 | **red blood lake** | - | - | - | - | 0.174867 | - | — |
| 8708 | **develop compassion** | - | - | - | - | 0.175997 | - | — |
| 8709 | **true happiness** | - | - | - | - | 0.176005 | - | — |
| 8710 | **mantra recitation** | - | - | - | - | 0.176714 | - | ~ |
| 8711 | **wisdom empowerment** | - | - | - | - | 0.176743 | - | ✓ ཤེས་རབ་ཀྱི་དབང |
| 8712 | **fortunate son** | - | - | - | - | 0.176977 | - | — |
| 8713 | **meet marpa** | - | - | - | - | 0.177166 | - | — |
| 8714 | **word empowerment** | - | - | - | - | 0.177474 | - | ~ |
| 8715 | **pure water** | - | - | - | - | 0.177540 | - | ~ |
| 8716 | **thousand prelimi** | - | - | - | - | 0.177916 | - | — |
| 8717 | **precious lineage** | - | - | - | - | 0.177954 | - | ~ |
| 8718 | **sutras speak** | - | - | - | - | 0.178033 | - | — |
| 8719 | **perfectly complete** | - | - | - | - | 0.178131 | - | — |
| 8720 | **sincere faith** | - | - | - | - | 0.178178 | - | — |
| 8721 | **heart blood** | - | - | - | - | 0.178375 | - | — |
| 8722 | **outer cho** | - | - | - | - | 0.178601 | - | ~ |
| 8723 | **bring harm** | - | - | - | - | 0.178631 | - | — |
| 8724 | **mental offering** | - | - | - | - | 0.178673 | - | — |
| 8725 | **body physically present** | - | - | - | - | 0.178837 | - | — |
| 8726 | **spiritual instruction** | - | - | - | - | 0.178881 | - | — |
| 8727 | **single form** | - | - | - | - | 0.178931 | - | — |
| 8728 | **authentic refuge** | - | - | - | - | 0.179086 | - | — |
| 8729 | **sixteen thousand** | - | - | - | - | 0.179160 | - | — |
| 8730 | **omniscient sovereign** | - | - | - | - | 0.179589 | - | — |
| 8731 | **human rebirth** | - | - | - | - | 0.180242 | - | — |
| 8732 | **everyday life** | - | - | - | - | 0.180273 | - | — |
| 8733 | **profoundly secret** | - | - | - | - | 0.180322 | - | — |
| 8734 | **dear life** | - | - | - | - | 0.180323 | - | — |
| 8735 | **eighteen hell** | - | - | - | - | 0.180350 | - | — |
| 8736 | **heart doctrine** | - | - | - | - | 0.180439 | - | — |
| 8737 | **red hot** | - | - | - | - | 0.180694 | - | — |
| 8738 | **lamp sutra** | - | - | - | - | 0.180738 | - | — |
| 8739 | **pure vision** | - | - | - | - | 0.180961 | - | — |
| 8740 | **sadaprarudita cut** | - | - | - | - | 0.181079 | - | — |
| 8741 | **blue vajra** | - | - | - | - | 0.181646 | - | — |
| 8742 | **distinguish good** | - | - | - | - | 0.181791 | - | — |
| 8743 | **practise concentration** | - | - | - | - | 0.181911 | - | — |
| 8744 | **people learn** | - | - | - | - | 0.181975 | - | — |
| 8745 | **mila adamantine victory** | - | - | - | - | 0.182370 | - | — |
| 8746 | **non dharma** | - | - | - | - | 0.182428 | - | ~ |
| 8747 | **infinite merit** | - | - | - | - | 0.182512 | - | ~ |
| 8748 | **perfect vajradhara** | - | - | - | - | 0.182876 | - | — |
| 8749 | **sick person** | - | - | - | - | 0.183007 | - | — |
| 8750 | **accumulate negative** | - | - | - | - | 0.183311 | - | — |
| 8751 | **transcendent primal wisdom** | - | - | - | - | 0.183568 | - | ~ |
| 8752 | **drikung kyobpa rinpoche** | - | - | - | - | 0.183570 | - | ~ |
| 8753 | **people speak** | - | - | - | - | 0.183729 | - | — |
| 8754 | **people lose** | - | - | - | - | 0.184462 | - | — |
| 8755 | **firm faith** | - | - | - | - | 0.185066 | - | — |
| 8756 | **god demon** | - | - | - | - | 0.185706 | - | — |
| 8757 | **transcendent patience** | - | - | - | - | 0.185907 | - | — |
| 8758 | **transcendent diligence** | - | - | - | - | 0.185954 | - | — |
| 8759 | **dakini yeshe** | - | - | - | - | 0.186165 | - | ~ |
| 8760 | **people enjoy** | - | - | - | - | 0.186387 | - | — |
| 8761 | **people fail** | - | - | - | - | 0.186496 | - | — |
| 8762 | **black man** | - | - | - | - | 0.186610 | - | — |
| 8763 | **disciple left** | - | - | - | - | 0.186790 | - | — |
| 8764 | **geshe chakshingwa** | - | - | - | - | 0.186896 | - | ~ |
| 8765 | **obtain human** | - | - | - | - | 0.186991 | - | — |
| 8766 | **huge offering** | - | - | - | - | 0.187187 | - | — |
| 8767 | **perfect health** | - | - | - | - | 0.187372 | - | — |
| 8768 | **risk life** | - | - | - | - | 0.187815 | - | — |
| 8769 | **end result** | - | - | - | - | 0.187828 | - | — |
| 8770 | **suddenly find** | - | - | - | - | 0.187941 | - | — |
| 8771 | **outer refuge** | - | - | - | - | 0.187980 | - | — |
| 8772 | **white syllable** | - | - | - | - | 0.188195 | - | — |
| 8773 | **people claim** | - | - | - | - | 0.188548 | - | — |
| 8774 | **single tibetan practitioner** | - | - | - | - | 0.189241 | - | — |
| 8775 | **main path** | - | - | - | - | 0.189276 | - | ~ |
| 8776 | **translator vairotsana** | - | - | - | - | 0.189318 | - | — |
| 8777 | **invoke glorious vajrasattva** | - | - | - | - | 0.189815 | - | — |
| 8778 | **karmapa lamas** | - | - | - | - | 0.190134 | - | — |
| 8779 | **foundation stone** | - | - | - | - | 0.190253 | - | — |
| 8780 | **mother camel** | - | - | - | - | 0.190750 | - | — |
| 8781 | **life renounce** | - | - | - | - | 0.190863 | - | — |
| 8782 | **human lifetime forever** | - | - | - | - | 0.191047 | - | — |
| 8783 | **lower left** | - | - | - | - | 0.191658 | - | — |
| 8784 | **kushab rinpoche shenpen** | - | - | - | - | 0.192233 | - | — |
| 8785 | **rinpoche shenpen thaye** | - | - | - | - | 0.192233 | - | — |
| 8786 | **ultimate fruit** | - | - | - | - | 0.192495 | - | — |
| 8787 | **red mountain** | - | - | - | - | 0.192810 | - | — |
| 8788 | **glorious mountain** | - | - | - | - | 0.192996 | - | ~ |
| 8789 | **happiness free** | - | - | - | - | 0.193224 | - | — |
| 8790 | **material body** | - | - | - | - | 0.193564 | - | — |
| 8791 | **rich man** | - | - | - | - | 0.193809 | - | — |
| 8792 | **place arouse** | - | - | - | - | 0.194010 | - | — |
| 8793 | **mind minutely** | - | - | - | - | 0.194032 | - | — |
| 8794 | **profound emptiness** | - | - | - | - | 0.194142 | - | ~ |
| 8795 | **great primordial kingdom** | - | - | - | - | 0.194338 | - | — |
| 8796 | **spend day** | - | - | - | - | 0.195107 | - | — |
| 8797 | **complete faith** | - | - | - | - | 0.195434 | - | — |
| 8798 | **tendzin chopel** | - | - | - | - | 0.195524 | - | — |
| 8799 | **mountain palace** | - | - | - | - | 0.195595 | - | ~ |
| 8800 | **thirty seven** | - | - | - | - | 0.195611 | - | ~ |
| 8801 | **pointed mind** | - | - | - | - | 0.195825 | - | — |
| 8802 | **mind indissolubly** | - | - | - | - | 0.195828 | - | — |
| 8803 | **favour life** | - | - | - | - | 0.195845 | - | — |
| 8804 | **entire kalpa** | - | - | - | - | 0.196136 | - | — |
| 8805 | **visit shang rinpoche** | - | - | - | - | 0.196220 | - | — |
| 8806 | **black hat karmapas** | - | - | - | - | 0.196380 | - | — |
| 8807 | **omniscient longchen rabjampa** | - | - | - | - | 0.197291 | - | — |
| 8808 | **wrathful black mother** | - | - | - | - | 0.197485 | - | ~ |
| 8809 | **wrathful black mother use** | - | - | - | - | 0.197514 | - | — |
| 8810 | **summit teaching** | - | - | - | - | 0.197750 | - | — |
| 8811 | **sixteen vajra** | - | - | - | - | 0.198377 | - | — |
| 8812 | **diamond cutter sutra** | - | - | - | - | 0.198410 | - | — |
| 8813 | **nowadays people** | - | - | - | - | 0.198413 | - | — |
| 8814 | **people nowadays** | - | - | - | - | 0.198413 | - | — |
| 8815 | **marvellous protector amitabha** | - | - | - | - | 0.198463 | - | — |
| 8816 | **negative mental** | - | - | - | - | 0.198719 | - | — |
| 8817 | **head visualize** | - | - | - | - | 0.198799 | - | — |
| 8818 | **personal practice** | - | - | - | - | 0.199130 | - | — |
| 8819 | **requisite good** | - | - | - | - | 0.199296 | - | — |
| 8820 | **good ascetic** | - | - | - | - | 0.199377 | - | — |
| 8821 | **extraordinary compassion** | - | - | - | - | 0.200233 | - | — |
| 8822 | **sleep yoga** | - | - | - | - | 0.200307 | - | — |
| 8823 | **vast wealth** | - | - | - | - | 0.200812 | - | — |
| 8824 | **vajra ogre** | - | - | - | - | 0.200890 | - | — |
| 8825 | **geshe tsakpuwa** | - | - | - | - | 0.202394 | - | — |
| 8826 | **respected master** | - | - | - | - | 0.203053 | - | — |
| 8827 | **collective good** | - | - | - | - | 0.203101 | - | — |
| 8828 | **entire body** | - | - | - | - | 0.203289 | - | — |
| 8829 | **uninterrupted good** | - | - | - | - | 0.203631 | - | — |
| 8830 | **ostentatious good** | - | - | - | - | 0.203918 | - | — |
| 8831 | **adopt good** | - | - | - | - | 0.203945 | - | — |
| 8832 | **diligent practice** | - | - | - | - | 0.204086 | - | — |
| 8833 | **excellent human** | - | - | - | - | 0.204295 | - | — |
| 8834 | **present wealth** | - | - | - | - | 0.204368 | - | — |
| 8835 | **prolong life** | - | - | - | - | 0.204374 | - | — |
| 8836 | **body dissolve** | - | - | - | - | 0.204822 | - | — |
| 8837 | **wild animal** | - | - | - | - | 0.204942 | - | — |
| 8838 | **main refuge** | - | - | - | - | 0.204961 | - | — |
| 8839 | **ordinary man** | - | - | - | - | 0.205048 | - | — |
| 8840 | **single offensive word** | - | - | - | - | 0.205055 | - | — |
| 8841 | **state arise** | - | - | - | - | 0.205078 | - | — |
| 8842 | **human simply** | - | - | - | - | 0.205510 | - | — |
| 8843 | **clear recollection** | - | - | - | - | 0.205986 | - | — |
| 8844 | **red syllable** | - | - | - | - | 0.206235 | - | — |
| 8845 | **element mandala** | - | - | - | - | 0.206440 | - | — |
| 8846 | **bodhicitta training** | - | - | - | - | 0.206592 | - | ~ |
| 8847 | **hells derive** | - | - | - | - | 0.207039 | - | — |
| 8848 | **terrible suffering** | - | - | - | - | 0.207343 | - | — |
| 8849 | **arouse absolute bodhicitta** | - | - | - | - | 0.207750 | - | — |
| 8850 | **fortunate human** | - | - | - | - | 0.208145 | - | — |
| 8851 | **delicious food** | - | - | - | - | 0.208989 | - | — |
| 8852 | **life good** | - | - | - | - | 0.209081 | - | — |
| 8853 | **short path** | - | - | - | - | 0.209489 | - | — |
| 8854 | **siddha melong dorje** | - | - | - | - | 0.209713 | - | ~ |
| 8855 | **extraordinary main path** | - | - | - | - | 0.209798 | - | — |
| 8856 | **commit negative** | - | - | - | - | 0.210478 | - | — |
| 8857 | **mikyo dorje** | - | - | - | - | 0.210493 | - | — |
| 8858 | **achieve liberation** | - | - | - | - | 0.211136 | - | — |
| 8859 | **goddesses offering** | - | - | - | - | 0.211292 | - | ~ |
| 8860 | **present form** | - | - | - | - | 0.211900 | - | — |
| 8861 | **hell ofutpala like** | - | - | - | - | 0.211962 | - | — |
| 8862 | **strong negative** | - | - | - | - | 0.212283 | - | — |
| 8863 | **frightening hell** | - | - | - | - | 0.212485 | - | — |
| 8864 | **day practice** | - | - | - | - | 0.212836 | - | — |
| 8865 | **intermediate state arise** | - | - | - | - | 0.213172 | - | — |
| 8866 | **lotus crest** | - | - | - | - | 0.213196 | - | — |
| 8867 | **extraordinary bodhicitta** | - | - | - | - | 0.213225 | - | — |
| 8868 | **langri thangpa gloomy face** | - | - | - | - | 0.213438 | - | — |
| 8869 | **past karma** | - | - | - | - | 0.213657 | - | — |
| 8870 | **eager faith** | - | - | - | - | 0.213939 | - | — |
| 8871 | **impure offering** | - | - | - | - | 0.214179 | - | — |
| 8872 | **nanda set** | - | - | - | - | 0.214455 | - | — |
| 8873 | **entire refuge** | - | - | - | - | 0.215291 | - | — |
| 8874 | **golden place** | - | - | - | - | 0.215358 | - | — |
| 8875 | **arhat katyayana** | - | - | - | - | 0.215582 | - | ~ |
| 8876 | **action take** | - | - | - | - | 0.215644 | - | — |
| 8877 | **offer water** | - | - | - | - | 0.215821 | - | — |
| 8878 | **padma siddhi hum** | - | - | - | - | 0.215839 | - | — |
| 8879 | **clear water** | - | - | - | - | 0.216139 | - | ~ |
| 8880 | **birth death** | - | - | - | - | 0.217018 | - | — |
| 8881 | **selfish desire** | - | - | - | - | 0.217051 | - | — |
| 8882 | **supreme happiness** | - | - | - | - | 0.217112 | - | — |
| 8883 | **hypocritical practice** | - | - | - | - | 0.217113 | - | — |
| 8884 | **lama yungton** | - | - | - | - | 0.217372 | - | — |
| 8885 | **vast scale** | - | - | - | - | 0.217700 | - | — |
| 8886 | **assiduous practice** | - | - | - | - | 0.217920 | - | — |
| 8887 | **devotional practice** | - | - | - | - | 0.218136 | - | — |
| 8888 | **practice predominate** | - | - | - | - | 0.218150 | - | — |
| 8889 | **renounce evil** | - | - | - | - | 0.218282 | - | — |
| 8890 | **body enter** | - | - | - | - | 0.218399 | - | — |
| 8891 | **immense merit** | - | - | - | - | 0.218752 | - | — |
| 8892 | **hunter gonpo dorje** | - | - | - | - | 0.219582 | - | — |
| 8893 | **past existence** | - | - | - | - | 0.219691 | - | — |
| 8894 | **perfectly pure motivation** | - | - | - | - | 0.219735 | - | — |
| 8895 | **evil nature** | - | - | - | - | 0.219859 | - | — |
| 8896 | **doctrines transference tradition** | - | - | - | - | 0.219969 | - | — |
| 8897 | **samsaric suffering** | - | - | - | - | 0.220060 | - | — |
| 8898 | **famous moon** | - | - | - | - | 0.220073 | - | — |
| 8899 | **sublime root** | - | - | - | - | 0.220318 | - | ~ |
| 8900 | **powerful positive** | - | - | - | - | 0.220623 | - | — |
| 8901 | **lack faith** | - | - | - | - | 0.220812 | - | — |
| 8902 | **people behave** | - | - | - | - | 0.221451 | - | — |
| 8903 | **sympathetic joy** | - | - | - | - | 0.221733 | - | — |
| 8904 | **abbot santarak** | - | - | - | - | 0.221756 | - | — |
| 8905 | **realization free** | - | - | - | - | 0.221886 | - | — |
| 8906 | **complete enlightenment** | - | - | - | - | 0.222347 | - | — |
| 8907 | **horse lama** | - | - | - | - | 0.222582 | - | — |
| 8908 | **feast offering** | - | - | - | - | 0.223781 | - | ✓ ཚོགས་ཀྱི་འཁོར་ལོ |
| 8909 | **black noose** | - | - | - | - | 0.224014 | - | — |
| 8910 | **dark red** | - | - | - | - | 0.224809 | - | — |
| 8911 | **tathagata sri** | - | - | - | - | 0.224937 | - | — |
| 8912 | **pure conduct** | - | - | - | - | 0.225493 | - | — |
| 8913 | **vivid faith** | - | - | - | - | 0.225579 | - | — |
| 8914 | **complete instruction** | - | - | - | - | 0.225699 | - | — |
| 8915 | **great universal system** | - | - | - | - | 0.226492 | - | — |
| 8916 | **immense bodhicitta** | - | - | - | - | 0.226675 | - | — |
| 8917 | **starting point** | - | - | - | - | 0.226954 | - | — |
| 8918 | **develop faith** | - | - | - | - | 0.226984 | - | — |
| 8919 | **day elapatra** | - | - | - | - | 0.227758 | - | — |
| 8920 | **precious medicinal tree** | - | - | - | - | 0.227835 | - | — |
| 8921 | **black hat** | - | - | - | - | 0.228020 | - | — |
| 8922 | **clear vision** | - | - | - | - | 0.228068 | - | — |
| 8923 | **noble spiritual** | - | - | - | - | 0.228477 | - | ~ |
| 8924 | **transcendent discipline** | - | - | - | - | 0.228563 | - | — |
| 8925 | **single instant lead** | - | - | - | - | 0.228715 | - | — |
| 8926 | **work hard** | - | - | - | - | 0.228964 | - | — |
| 8927 | **precious material** | - | - | - | - | 0.228989 | - | — |
| 8928 | **kalpa delightful** | - | - | - | - | 0.229062 | - | — |
| 8929 | **jowo dole** | - | - | - | - | 0.229221 | - | — |
| 8930 | **intense compassion** | - | - | - | - | 0.229528 | - | — |
| 8931 | **melong dorje** | - | - | - | - | 0.229734 | - | ✓ མེ་ལོང་རྡོ་རྗེ |
| 8932 | **teaching yard** | - | - | - | - | 0.229890 | - | — |
| 8933 | **outdoor teaching** | - | - | - | - | 0.229891 | - | — |
| 8934 | **harma teaching** | - | - | - | - | 0.230169 | - | — |
| 8935 | **teachings ofmaitreya** | - | - | - | - | 0.230175 | - | — |
| 8936 | **elapatra tree** | - | - | - | - | 0.230316 | - | — |
| 8937 | **southern buddhafield** | - | - | - | - | 0.230631 | - | — |
| 8938 | **people pay** | - | - | - | - | 0.230980 | - | — |
| 8939 | **dorje dudjom** | - | - | - | - | 0.231342 | - | — |
| 8940 | **natural state support** | - | - | - | - | 0.231526 | - | — |
| 8941 | **changchub dorje** | - | - | - | - | 0.231666 | - | — |
| 8942 | **ego clinging** | - | - | - | - | 0.232131 | - | — |
| 8943 | **gathering offering** | - | - | - | - | 0.232208 | - | — |
| 8944 | **hand high** | - | - | - | - | 0.232871 | - | — |
| 8945 | **completely perfect** | - | - | - | - | 0.233124 | - | — |
| 8946 | **mountain vajrapar** | - | - | - | - | 0.234171 | - | — |
| 8947 | **suffer terribly** | - | - | - | - | 0.234328 | - | — |
| 8948 | **equal nature** | - | - | - | - | 0.234388 | - | — |
| 8949 | **vast skill** | - | - | - | - | 0.234572 | - | — |
| 8950 | **pandita naropa** | - | - | - | - | 0.234817 | - | ~ |
| 8951 | **wisdom dakini** | - | - | - | - | 0.234995 | - | ~ |
| 8952 | **unbearable pain** | - | - | - | - | 0.235483 | - | — |
| 8953 | **powerful person** | - | - | - | - | 0.236129 | - | — |
| 8954 | **branch visualize** | - | - | - | - | 0.236882 | - | — |
| 8955 | **complete root downfall** | - | - | - | - | 0.236927 | - | — |
| 8956 | **people add** | - | - | - | - | 0.237253 | - | — |
| 8957 | **important point** | - | - | - | - | 0.237432 | - | — |
| 8958 | **immaculate wisdom** | - | - | - | - | 0.238134 | - | — |
| 8959 | **supreme spiritual** | - | - | - | - | 0.238331 | - | ~ |
| 8960 | **karmic result** | - | - | - | - | 0.238891 | - | — |
| 8961 | **prosperous people** | - | - | - | - | 0.239060 | - | — |
| 8962 | **main subject** | - | - | - | - | 0.239194 | - | ~ |
| 8963 | **attain accomplishment** | - | - | - | - | 0.239367 | - | — |
| 8964 | **wisdom enter** | - | - | - | - | 0.239650 | - | — |
| 8965 | **fortunate dynasty** | - | - | - | - | 0.240140 | - | — |
| 8966 | **compassion hurl** | - | - | - | - | 0.240397 | - | — |
| 8967 | **union wisdom** | - | - | - | - | 0.240449 | - | ~ |
| 8968 | **effect utterly** | - | - | - | - | 0.240977 | - | — |
| 8969 | **pure motivation** | - | - | - | - | 0.241094 | - | — |
| 8970 | **suffering befall** | - | - | - | - | 0.241572 | - | — |
| 8971 | **true tradition** | - | - | - | - | 0.241609 | - | ~ |
| 8972 | **white nectar** | - | - | - | - | 0.241743 | - | — |
| 8973 | **supreme joy** | - | - | - | - | 0.242617 | - | ~ |
| 8974 | **long training** | - | - | - | - | 0.242629 | - | — |
| 8975 | **happiness comfort** | - | - | - | - | 0.243439 | - | — |
| 8976 | **offering practice** | - | - | - | - | 0.243516 | - | — |
| 8977 | **vajra song** | - | - | - | - | 0.243588 | - | ✓ རྡོ་རྗེ་མགུར |
| 8978 | **sublime path unerringly** | - | - | - | - | 0.243875 | - | — |
| 8979 | **orgyen jigme** | - | - | - | - | 0.243952 | - | — |
| 8980 | **ultimate liberation** | - | - | - | - | 0.243956 | - | — |
| 8981 | **postpone death** | - | - | - | - | 0.244359 | - | — |
| 8982 | **kyung tonpa** | - | - | - | - | 0.244671 | - | — |
| 8983 | **lhangtsang tonpa** | - | - | - | - | 0.244684 | - | — |
| 8984 | **refuge constantly** | - | - | - | - | 0.244930 | - | — |
| 8985 | **meritorious act** | - | - | - | - | 0.245536 | - | — |
| 8986 | **evil man** | - | - | - | - | 0.245932 | - | — |
| 8987 | **central head** | - | - | - | - | 0.246165 | - | — |
| 8988 | **strive day** | - | - | - | - | 0.246546 | - | — |
| 8989 | **feel natural** | - | - | - | - | 0.246675 | - | — |
| 8990 | **unaltered natural state** | - | - | - | - | 0.246835 | - | ~ |
| 8991 | **root samayas** | - | - | - | - | 0.246946 | - | ~ |
| 8992 | **cruel suffering** | - | - | - | - | 0.247102 | - | — |
| 8993 | **develop positive** | - | - | - | - | 0.247188 | - | — |
| 8994 | **seek refuge** | - | - | - | - | 0.247194 | - | — |
| 8995 | **marpa severely** | - | - | - | - | 0.247339 | - | — |
| 8996 | **actual meditation** | - | - | - | - | 0.247799 | - | — |
| 8997 | **outward sign** | - | - | - | - | 0.248102 | - | — |
| 8998 | **hollow vajra** | - | - | - | - | 0.249086 | - | — |
| 8999 | **khampa lhungpa** | - | - | - | - | 0.249121 | - | — |
| 9000 | **moment onwards** | - | - | - | - | 0.249182 | - | — |
| 9001 | **false spiritual** | - | - | - | - | 0.249504 | - | — |
| 9002 | **negative connection** | - | - | - | - | 0.249758 | - | — |
| 9003 | **precious golden** | - | - | - | - | 0.250387 | - | — |
| 9004 | **dumb person** | - | - | - | - | 0.250584 | - | — |
| 9005 | **khampa lungpa** | - | - | - | - | 0.251062 | - | ✓ ཁམས་པ་ལུང་པ |
| 9006 | **infinite number** | - | - | - | - | 0.251201 | - | — |
| 9007 | **sublime sariputra** | - | - | - | - | 0.251230 | - | — |
| 9008 | **cheat people** | - | - | - | - | 0.251639 | - | — |
| 9009 | **ignorant people** | - | - | - | - | 0.251680 | - | — |
| 9010 | **complete root** | - | - | - | - | 0.251875 | - | — |
| 9011 | **double suffering** | - | - | - | - | 0.252119 | - | — |
| 9012 | **precious umbrella** | - | - | - | - | 0.252581 | - | — |
| 9013 | **religious king gomadeviya** | - | - | - | - | 0.252787 | - | — |
| 9014 | **ceaseless suffering** | - | - | - | - | 0.252930 | - | — |
| 9015 | **incredible suffering** | - | - | - | - | 0.252971 | - | — |
| 9016 | **boundless compassion** | - | - | - | - | 0.253347 | - | ~ |
| 9017 | **sublime essence** | - | - | - | - | 0.253757 | - | ~ |
| 9018 | **feel pain** | - | - | - | - | 0.254127 | - | — |
| 9019 | **negative behaviour** | - | - | - | - | 0.254136 | - | — |
| 9020 | **fully ripen** | - | - | - | - | 0.255275 | - | — |
| 9021 | **noble katyayana** | - | - | - | - | 0.255287 | - | ~ |
| 9022 | **real benefit** | - | - | - | - | 0.255613 | - | — |
| 9023 | **sangha fail** | - | - | - | - | 0.256006 | - | — |
| 9024 | **finally eighty thousand** | - | - | - | - | 0.256388 | - | — |
| 9025 | **entire human** | - | - | - | - | 0.256598 | - | — |
| 9026 | **outer water element** | - | - | - | - | 0.256622 | - | — |
| 9027 | **boundless love** | - | - | - | - | 0.256638 | - | — |
| 9028 | **compassion possess** | - | - | - | - | 0.256849 | - | — |
| 9029 | **false path** | - | - | - | - | 0.257097 | - | — |
| 9030 | **perfection subsequently** | - | - | - | - | 0.257432 | - | — |
| 9031 | **sublime method** | - | - | - | - | 0.257704 | - | — |
| 9032 | **profound truth** | - | - | - | - | 0.257981 | - | ~ |
| 9033 | **totally free** | - | - | - | - | 0.258290 | - | — |
| 9034 | **people manage** | - | - | - | - | 0.258720 | - | — |
| 9035 | **karmic effect similar** | - | - | - | - | 0.259337 | - | — |
| 9036 | **sangye heard** | - | - | - | - | 0.259402 | - | — |
| 9037 | **ordinary outer** | - | - | - | - | 0.260241 | - | ~ |
| 9038 | **compassionate root** | - | - | - | - | 0.260377 | - | ~ |
| 9039 | **old people** | - | - | - | - | 0.260402 | - | — |
| 9040 | **vajra sprang** | - | - | - | - | 0.260603 | - | — |
| 9041 | **lotus bud** | - | - | - | - | 0.260613 | - | — |
| 9042 | **boundless merit** | - | - | - | - | 0.260777 | - | ~ |
| 9043 | **wisdom kaya** | - | - | - | - | 0.260794 | - | ~ |
| 9044 | **precious lineage dawn** | - | - | - | - | 0.261610 | - | — |
| 9045 | **syllable hrih** | - | - | - | - | 0.261964 | - | — |
| 9046 | **sutra ofi** | - | - | - | - | 0.262232 | - | — |
| 9047 | **state support** | - | - | - | - | 0.262569 | - | — |
| 9048 | **bring unending** | - | - | - | - | 0.262646 | - | — |
| 9049 | **body life** | - | - | - | - | 0.263008 | - | — |
| 9050 | **people crave** | - | - | - | - | 0.263730 | - | — |
| 9051 | **people pretend** | - | - | - | - | 0.263862 | - | — |
| 9052 | **marvellous essence** | - | - | - | - | 0.264030 | - | — |
| 9053 | **impress people** | - | - | - | - | 0.264249 | - | — |
| 9054 | **people partake** | - | - | - | - | 0.264372 | - | — |
| 9055 | **people unhappy** | - | - | - | - | 0.264384 | - | — |
| 9056 | **sacred place** | - | - | - | - | 0.264623 | - | — |
| 9057 | **primordial state free** | - | - | - | - | 0.264659 | - | ~ |
| 9058 | **false cho** | - | - | - | - | 0.264748 | - | — |
| 9059 | **gifted people** | - | - | - | - | 0.264916 | - | — |
| 9060 | **entire time swimming** | - | - | - | - | 0.265051 | - | — |
| 9061 | **take pleasure** | - | - | - | - | 0.265872 | - | — |
| 9062 | **poor thing** | - | - | - | - | 0.266663 | - | — |
| 9063 | **vajra puspe** | - | - | - | - | 0.266809 | - | — |
| 9064 | **dha vajra** | - | - | - | - | 0.266817 | - | — |
| 9065 | **kind lack** | - | - | - | - | 0.266852 | - | — |
| 9066 | **tangtong gyalpo** | - | - | - | - | 0.267318 | - | ✓ ཐང་སྟོང་རྒྱལ་པོ |
| 9067 | **physically present** | - | - | - | - | 0.267338 | - | — |
| 9068 | **bird taking** | - | - | - | - | 0.267607 | - | — |
| 9069 | **virtuous thing** | - | - | - | - | 0.267787 | - | — |
| 9070 | **long iron** | - | - | - | - | 0.267871 | - | — |
| 9071 | **present perfectly dedicate** | - | - | - | - | 0.268011 | - | — |
| 9072 | **entire world** | - | - | - | - | 0.268208 | - | — |
| 9073 | **light empowerment** | - | - | - | - | 0.268264 | - | ~ |
| 9074 | **close friend** | - | - | - | - | 0.268385 | - | ~ |
| 9075 | **past sexual** | - | - | - | - | 0.268509 | - | — |
| 9076 | **adamantine clear light** | - | - | - | - | 0.270074 | - | ~ |
| 9077 | **blood lake** | - | - | - | - | 0.270176 | - | — |
| 9078 | **people intimately** | - | - | - | - | 0.270304 | - | — |
| 9079 | **reliable people** | - | - | - | - | 0.270322 | - | — |
| 9080 | **people declare** | - | - | - | - | 0.270794 | - | — |
| 9081 | **cultivate bodhicitta** | - | - | - | - | 0.270999 | - | — |
| 9082 | **feel attachment** | - | - | - | - | 0.271123 | - | — |
| 9083 | **seventh day** | - | - | - | - | 0.271895 | - | — |
| 9084 | **upayoga tantra** | - | - | - | - | 0.271909 | - | — |
| 9085 | **steel wheel** | - | - | - | - | 0.272270 | - | — |
| 9086 | **powerful demon** | - | - | - | - | 0.272499 | - | — |
| 9087 | **body physically** | - | - | - | - | 0.272590 | - | — |
| 9088 | **harsh speech** | - | - | - | - | 0.272611 | - | — |
| 9089 | **human lifetime** | - | - | - | - | 0.272854 | - | — |
| 9090 | **mix negative** | - | - | - | - | 0.273038 | - | — |
| 9091 | **demon tsang** | - | - | - | - | 0.273180 | - | — |
| 9092 | **rich person** | - | - | - | - | 0.273206 | - | — |
| 9093 | **meet dharmodgata** | - | - | - | - | 0.273718 | - | — |
| 9094 | **yoga technique** | - | - | - | - | 0.273758 | - | — |
| 9095 | **practice like compassion** | - | - | - | - | 0.273786 | - | — |
| 9096 | **water element** | - | - | - | - | 0.274082 | - | — |
| 9097 | **small pile** | - | - | - | - | 0.274297 | - | — |
| 9098 | **perform positive** | - | - | - | - | 0.274683 | - | — |
| 9099 | **ultimate goal** | - | - | - | - | 0.275078 | - | — |
| 9100 | **outer water** | - | - | - | - | 0.275384 | - | ~ |
| 9101 | **glorious vajradhara** | - | - | - | - | 0.275783 | - | ~ |
| 9102 | **order great universal** | - | - | - | - | 0.275906 | - | — |
| 9103 | **beggar woman** | - | - | - | - | 0.275925 | - | — |
| 9104 | **powerful evil** | - | - | - | - | 0.275937 | - | — |
| 9105 | **direct empowerment** | - | - | - | - | 0.275993 | - | — |
| 9106 | **control body** | - | - | - | - | 0.276101 | - | — |
| 9107 | **immense faith** | - | - | - | - | 0.276851 | - | — |
| 9108 | **nyatri tsenpo** | - | - | - | - | 0.277423 | - | — |
| 9109 | **sublime son** | - | - | - | - | 0.277577 | - | — |
| 9110 | **animal today** | - | - | - | - | 0.277699 | - | — |
| 9111 | **action avoid** | - | - | - | - | 0.277733 | - | — |
| 9112 | **king ravati** | - | - | - | - | 0.277805 | - | — |
| 9113 | **merit totally** | - | - | - | - | 0.277821 | - | — |
| 9114 | **machik labdron** | - | - | - | - | 0.278144 | - | ✓ མ་ཅིག་ལབ་སྒྲོན |
| 9115 | **king subject** | - | - | - | - | 0.278362 | - | ~ |
| 9116 | **negative mentality** | - | - | - | - | 0.278561 | - | — |
| 9117 | **animal birth** | - | - | - | - | 0.280518 | - | — |
| 9118 | **immeasurable compassion** | - | - | - | - | 0.280598 | - | — |
| 9119 | **suffering negative** | - | - | - | - | 0.280983 | - | ~ |
| 9120 | **apply bodhicitta** | - | - | - | - | 0.281897 | - | — |
| 9121 | **consume flesh** | - | - | - | - | 0.282540 | - | — |
| 9122 | **kyabje dodrup chen** | - | - | - | - | 0.282625 | - | — |
| 9123 | **suddenly end** | - | - | - | - | 0.282646 | - | — |
| 9124 | **present perfectly** | - | - | - | - | 0.282812 | - | — |
| 9125 | **white hum** | - | - | - | - | 0.282824 | - | — |
| 9126 | **red blood** | - | - | - | - | 0.282897 | - | — |
| 9127 | **feel hatred** | - | - | - | - | 0.282959 | - | — |
| 9128 | **head dissolve** | - | - | - | - | 0.283487 | - | — |
| 9129 | **metal ground** | - | - | - | - | 0.283910 | - | — |
| 9130 | **comfortable place** | - | - | - | - | 0.284192 | - | — |
| 9131 | **blissful land** | - | - | - | - | 0.284551 | - | ~ |
| 9132 | **offer flesh** | - | - | - | - | 0.284917 | - | — |
| 9133 | **red syllable hrih** | - | - | - | - | 0.285262 | - | — |
| 9134 | **sacred wisdom** | - | - | - | - | 0.285307 | - | — |
| 9135 | **black mother** | - | - | - | - | 0.285523 | - | ~ |
| 9136 | **black mother use** | - | - | - | - | 0.285556 | - | — |
| 9137 | **ninefold black** | - | - | - | - | 0.285607 | - | — |
| 9138 | **negative imprint** | - | - | - | - | 0.285715 | - | — |
| 9139 | **naropa underwent** | - | - | - | - | 0.285752 | - | — |
| 9140 | **bodhicitta equally** | - | - | - | - | 0.285915 | - | — |
| 9141 | **humble place** | - | - | - | - | 0.286034 | - | — |
| 9142 | **paqqita naropa** | - | - | - | - | 0.286364 | - | — |
| 9143 | **captain compassionate heart** | - | - | - | - | 0.286849 | - | — |
| 9144 | **dark black** | - | - | - | - | 0.286862 | - | — |
| 9145 | **azure heaven** | - | - | - | - | 0.287000 | - | — |
| 9146 | **lightly small** | - | - | - | - | 0.287373 | - | — |
| 9147 | **perfectly dedicated merit** | - | - | - | - | 0.287608 | - | — |
| 9148 | **town scavenger offering** | - | - | - | - | 0.288047 | - | — |
| 9149 | **lack wealth** | - | - | - | - | 0.288143 | - | — |
| 9150 | **sincere bodhicitta** | - | - | - | - | 0.288515 | - | — |
| 9151 | **inconceivable power** | - | - | - | - | 0.289321 | - | — |
| 9152 | **clear light spread** | - | - | - | - | 0.289546 | - | — |
| 9153 | **happiness today** | - | - | - | - | 0.289740 | - | — |
| 9154 | **perfection phase depend** | - | - | - | - | 0.290008 | - | — |
| 9155 | **wrong attitude** | - | - | - | - | 0.290989 | - | — |
| 9156 | **mother sixteen** | - | - | - | - | 0.291005 | - | — |
| 9157 | **practice take** | - | - | - | - | 0.291391 | - | — |
| 9158 | **constantly long** | - | - | - | - | 0.291680 | - | — |
| 9159 | **northern buddhafield** | - | - | - | - | 0.292585 | - | — |
| 9160 | **single night** | - | - | - | - | 0.292643 | - | — |
| 9161 | **simply free** | - | - | - | - | 0.292850 | - | — |
| 9162 | **state carefully** | - | - | - | - | 0.293341 | - | — |
| 9163 | **past perfectly dedicated** | - | - | - | - | 0.293462 | - | — |
| 9164 | **real determination** | - | - | - | - | 0.293558 | - | ~ |
| 9165 | **faith fully** | - | - | - | - | 0.293849 | - | — |
| 9166 | **jigme cbokyi** | - | - | - | - | 0.294274 | - | — |
| 9167 | **jigme gyalwai** | - | - | - | - | 0.294281 | - | — |
| 9168 | **feel happy** | - | - | - | - | 0.295129 | - | — |
| 9169 | **meditate single mindedly** | - | - | - | - | 0.295132 | - | — |
| 9170 | **heart centre** | - | - | - | - | 0.295151 | - | — |
| 9171 | **superior transference** | - | - | - | - | 0.295312 | - | — |
| 9172 | **profound essence** | - | - | - | - | 0.295352 | - | ~ |
| 9173 | **orgyen jigme cbokyi** | - | - | - | - | 0.295415 | - | — |
| 9174 | **day people** | - | - | - | - | 0.295670 | - | — |
| 9175 | **mantras perfunctorily** | - | - | - | - | 0.296256 | - | — |
| 9176 | **authentic view** | - | - | - | - | 0.296696 | - | — |
| 9177 | **worldly point** | - | - | - | - | 0.297096 | - | ~ |
| 9178 | **practise virtue** | - | - | - | - | 0.297642 | - | — |
| 9179 | **refuge sincerely** | - | - | - | - | 0.297705 | - | — |
| 9180 | **tathagata ratnapada** | - | - | - | - | 0.297826 | - | — |
| 9181 | **tathagata siddhyaloka** | - | - | - | - | 0.297829 | - | — |
| 9182 | **natural expression** | - | - | - | - | 0.298469 | - | ~ |
| 9183 | **thousand iron** | - | - | - | - | 0.298834 | - | — |
| 9184 | **indivisible yoga** | - | - | - | - | 0.299229 | - | — |
| 9185 | **principal sravakas** | - | - | - | - | 0.299401 | - | — |
| 9186 | **lita vimalamitra** | - | - | - | - | 0.299412 | - | — |
| 9187 | **prodigious negative** | - | - | - | - | 0.299641 | - | — |
| 9188 | **ludicrous negative** | - | - | - | - | 0.299648 | - | — |
| 9189 | **unmentionably negative** | - | - | - | - | 0.299807 | - | — |
| 9190 | **intense faith** | - | - | - | - | 0.299979 | - | — |

---

*Corpus reference: Reuters-21578 (10,788 newswire documents) via NLTK · sklearn TfidfVectorizer(smooth\_idf=True, lowercase=True). YAKE (unigram–trigram, spaCy-lemmatized, dedupLim=0.9) via `4-SYSTEM/scripts/english_keyword/keywords.py`.*  
*Lemmatization for the TF-IDF word list: rule-based plural/possessive reduction (spaCy unavailable in this environment); irregular plurals (children, men, women, people, feet, teeth) handled via an explicit mapping.*  
*Regenerated 2026-08-04 — N-gram Keywords and Full Ranked Table sections merged into one combined table.*

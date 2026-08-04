---
title: TF-IDF Vocabulary Analysis — en
source: C:\Users\geshe lobzang tseten\repos\bodhisattvacharyavatara-rails\0-INBOX\ཀུན་བཟང་བླ་མའི་ཞལ་ལུང\en.md
corpus: Reuters-21578 (10,788 newswire documents) via NLTK · sklearn TfidfVectorizer(smooth_idf=True)
method: TF × IDF — term frequency in translation vs. inverse document frequency in Reuters corpus
generated: 2026-08-03
unique_terms: 8673
total_content_tokens: 57,704
status: draft
---

# TF-IDF Vocabulary Analysis — en

Generated **2026-08-03** · source: `en.md` · **8,673 unique content terms** ranked.

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
| 🔴 extremely high — text-exclusive | 2 | 0.0% |
| 🟠 very high — domain-specific | 71 | 0.8% |
| 🟡 high — specialist register | 453 | 5.2% |
| 🟢 medium — moderately distinctive | 2,021 | 23.3% |
| 🔵 low — common in general English | 6,125 | 70.6% |
| ⚪ very low — function / universal word | 1 | 0.0% |

---

## Most Distinctive Words (highest TF-IDF)

Words that appear **frequently in this text** yet are **rare or absent in general English**.

**1. dharma** — count: 409, TF-IDF: 67,973, IDF: 9.59 🔴 extremely high — text-exclusive
**2. teacher** — count: 333, TF-IDF: 51,360, IDF: 8.899988 🔴 extremely high — text-exclusive
**3. buddha** — count: 260, TF-IDF: 43,210, IDF: 9.59 🟠 very high — domain-specific
**4. beings** — count: 258, TF-IDF: 42,878, IDF: 9.59 🟠 very high — domain-specific
**5. like** — count: 396, TF-IDF: 35,634, IDF: 5.192532 🟠 very high — domain-specific
**6. actions** — count: 278, TF-IDF: 27,986, IDF: 5.808946 🟠 very high — domain-specific
**7. mind** — count: 217, TF-IDF: 26,891, IDF: 7.150788 🟠 very high — domain-specific
**8. yourself** — count: 154, TF-IDF: 24,520, IDF: 9.18767 🟠 very high — domain-specific
**9. compassion** — count: 147, TF-IDF: 24,438, IDF: 9.593135 🟠 very high — domain-specific
**10. life** — count: 240, TF-IDF: 22,905, IDF: 5.507159 🟠 very high — domain-specific
**11. practice** — count: 190, TF-IDF: 22,356, IDF: 6.789775 🟠 very high — domain-specific
**12. without** — count: 266, TF-IDF: 21,766, IDF: 4.721762 🟠 very high — domain-specific
**13. bodhicitta** — count: 130, TF-IDF: 21,605, IDF: 9.59 🟠 very high — domain-specific
**14. never** — count: 197, TF-IDF: 21,563, IDF: 6.31599 🟠 very high — domain-specific
**15. practise** — count: 123, TF-IDF: 20,448, IDF: 9.593135 🟠 very high — domain-specific
**16. merit** — count: 139, TF-IDF: 20,091, IDF: 8.340372 🟠 very high — domain-specific
**17. teachings** — count: 117, TF-IDF: 19,445, IDF: 9.59 🟠 very high — domain-specific
**18. realms** — count: 116, TF-IDF: 19,278, IDF: 9.59 🟠 very high — domain-specific
**19. refuge** — count: 127, TF-IDF: 18,695, IDF: 8.494523 🟠 very high — domain-specific
**20. death** — count: 128, TF-IDF: 18,205, IDF: 8.206841 🟠 very high — domain-specific
**21. suffering** — count: 143, TF-IDF: 17,946, IDF: 7.24176 🟠 very high — domain-specific
**22. others** — count: 178, TF-IDF: 17,433, IDF: 5.651553 🟠 very high — domain-specific
**23. buddhas** — count: 104, TF-IDF: 17,284, IDF: 9.59 🟠 very high — domain-specific
**24. negative** — count: 166, TF-IDF: 16,949, IDF: 5.891833 🟠 very high — domain-specific
**25. teaching** — count: 101, TF-IDF: 16,785, IDF: 9.59 🟠 very high — domain-specific
**26. body** — count: 149, TF-IDF: 16,358, IDF: 6.335039 🟠 very high — domain-specific
**27. whatever** — count: 132, TF-IDF: 16,260, IDF: 7.108229 🟠 very high — domain-specific
**28. king** — count: 129, TF-IDF: 16,085, IDF: 7.19524 🟠 very high — domain-specific
**29. path** — count: 118, TF-IDF: 15,953, IDF: 7.801376 🟠 very high — domain-specific
**30. wisdom** — count: 107, TF-IDF: 15,751, IDF: 8.494523 🟠 very high — domain-specific
**31. time** — count: 235, TF-IDF: 15,647, IDF: 3.842151 🟠 very high — domain-specific
**32. people** — count: 170, TF-IDF: 15,352, IDF: 5.211109 🟠 very high — domain-specific
**33. perfect** — count: 96, TF-IDF: 15,285, IDF: 9.18767 🟠 very high — domain-specific
**34. jewels** — count: 91, TF-IDF: 15,124, IDF: 9.59 🟠 very high — domain-specific
**35. faith** — count: 108, TF-IDF: 14,942, IDF: 7.983697 🟠 very high — domain-specific
**36. once** — count: 140, TF-IDF: 14,235, IDF: 5.867442 🟠 very high — domain-specific
**37. mother** — count: 85, TF-IDF: 14,126, IDF: 9.59 🟠 very high — domain-specific
**38. words** — count: 106, TF-IDF: 14,048, IDF: 7.647225 🟠 very high — domain-specific
**39. hundred** — count: 107, TF-IDF: 13,820, IDF: 7.453069 🟠 very high — domain-specific
**40. way** — count: 164, TF-IDF: 13,542, IDF: 4.764821 🟠 very high — domain-specific
**41. lives** — count: 91, TF-IDF: 13,396, IDF: 8.494523 🟠 very high — domain-specific
**42. samsara** — count: 79, TF-IDF: 13,129, IDF: 9.59 🟠 very high — domain-specific
**43. happiness** — count: 77, TF-IDF: 12,797, IDF: 9.59 🟠 very high — domain-specific
**44. gods** — count: 77, TF-IDF: 12,797, IDF: 9.59 🟠 very high — domain-specific
**45. reborn** — count: 75, TF-IDF: 12,464, IDF: 9.59 🟠 very high — domain-specific
**46. offerings** — count: 94, TF-IDF: 12,457, IDF: 7.647225 🟠 very high — domain-specific
**47. everything** — count: 96, TF-IDF: 12,214, IDF: 7.341843 🟠 very high — domain-specific
**48. human** — count: 86, TF-IDF: 11,757, IDF: 7.888387 🟠 very high — domain-specific
**49. many** — count: 146, TF-IDF: 11,654, IDF: 4.60611 🟠 very high — domain-specific
**50. evil** — count: 70, TF-IDF: 11,637, IDF: 9.593135 🟠 very high — domain-specific

---

## Least Distinctive Words (lowest TF-IDF)

Words that appear in this text but are also extremely common in general English.

**1. net** — count: 1, TF-IDF: 40.18, IDF: 2.318656 ⚪ very low — function / universal word
**2. stock** — count: 1, TF-IDF: 52.87, IDF: 3.050663 🔵 low — common in general English
**3. prices** — count: 1, TF-IDF: 58.41, IDF: 3.370559 🔵 low — common in general English
**4. agreement** — count: 1, TF-IDF: 58.50, IDF: 3.375532 🔵 low — common in general English
**5. exchange** — count: 1, TF-IDF: 58.64, IDF: 3.38354 🔵 low — common in general English
**6. expected** — count: 1, TF-IDF: 58.67, IDF: 3.385552 🔵 low — common in general English
**7. government** — count: 1, TF-IDF: 60.98, IDF: 3.518939 🔵 low — common in general English
**8. quarter** — count: 1, TF-IDF: 61.88, IDF: 3.570899 🔵 low — common in general English
**9. foreign** — count: 1, TF-IDF: 63.35, IDF: 3.655599 🔵 low — common in general English
**10. agreed** — count: 1, TF-IDF: 63.74, IDF: 3.678282 🔵 low — common in general English
**11. rose** — count: 1, TF-IDF: 63.77, IDF: 3.679632 🔵 low — common in general English
**12. tax** — count: 1, TF-IDF: 65.00, IDF: 3.751041 🔵 low — common in general English
**13. production** — count: 1, TF-IDF: 65.08, IDF: 3.755405 🔵 low — common in general English
**14. industry** — count: 1, TF-IDF: 67.84, IDF: 3.914671 🔵 low — common in general English
**15. officials** — count: 1, TF-IDF: 68.63, IDF: 3.960133 🔵 low — common in general English
**16. assets** — count: 1, TF-IDF: 68.88, IDF: 3.974548 🔵 low — common in general English
**17. capital** — count: 1, TF-IDF: 69.49, IDF: 4.009639 🔵 low — common in general English
**18. trading** — count: 1, TF-IDF: 70.35, IDF: 4.059746 🔵 low — common in general English
**19. yesterday** — count: 1, TF-IDF: 70.42, IDF: 4.063706 🔵 low — common in general English
**20. outstanding** — count: 1, TF-IDF: 70.91, IDF: 4.091877 🔵 low — common in general English
**21. sees** — count: 1, TF-IDF: 73.42, IDF: 4.236549 🔵 low — common in general English
**22. supply** — count: 1, TF-IDF: 74.43, IDF: 4.294818 🔵 low — common in general English
**23. bought** — count: 1, TF-IDF: 74.65, IDF: 4.307397 🔵 low — common in general English
**24. public** — count: 1, TF-IDF: 76.25, IDF: 4.400178 🔵 low — common in general English
**25. loan** — count: 1, TF-IDF: 77.35, IDF: 4.463236 🔵 low — common in general English
**26. secretary** — count: 1, TF-IDF: 79.24, IDF: 4.57255 🔵 low — common in general English
**27. available** — count: 1, TF-IDF: 79.59, IDF: 4.59255 🔵 low — common in general English
**28. profits** — count: 1, TF-IDF: 80.24, IDF: 4.630291 🔵 low — common in general English
**29. account** — count: 1, TF-IDF: 81.50, IDF: 4.702786 🔵 low — common in general English
**30. despite** — count: 1, TF-IDF: 81.50, IDF: 4.702786 🔵 low — common in general English
**31. buying** — count: 1, TF-IDF: 82.50, IDF: 4.760829 🔵 low — common in general English
**32. chief** — count: 1, TF-IDF: 82.64, IDF: 4.768829 🔵 low — common in general English
**33. selling** — count: 1, TF-IDF: 84.09, IDF: 4.85256 🔵 low — common in general English
**34. area** — count: 1, TF-IDF: 85.27, IDF: 4.920306 🔵 low — common in general English
**35. letter** — count: 1, TF-IDF: 85.59, IDF: 4.939175 🔵 low — common in general English
**36. negotiations** — count: 1, TF-IDF: 85.68, IDF: 4.943948 🔵 low — common in general English
**37. crop** — count: 1, TF-IDF: 85.84, IDF: 4.953564 🔵 low — common in general English
**38. areas** — count: 1, TF-IDF: 86.01, IDF: 4.963272 🔵 low — common in general English
**39. probably** — count: 1, TF-IDF: 86.18, IDF: 4.973076 🔵 low — common in general English
**40. respectively** — count: 1, TF-IDF: 86.35, IDF: 4.982977 🔵 low — common in general English
**41. range** — count: 1, TF-IDF: 86.44, IDF: 4.987965 🔵 low — common in general English
**42. figure** — count: 1, TF-IDF: 86.97, IDF: 5.018424 🔵 low — common in general English
**43. adding** — count: 1, TF-IDF: 87.06, IDF: 5.023592 🔵 low — common in general English
**44. member** — count: 1, TF-IDF: 87.79, IDF: 5.065927 🔵 low — common in general English
**45. gross** — count: 1, TF-IDF: 88.17, IDF: 5.087785 🔵 low — common in general English
**46. farm** — count: 1, TF-IDF: 88.85, IDF: 5.127227 🔵 low — common in general English
**47. interests** — count: 1, TF-IDF: 89.05, IDF: 5.138788 🔵 low — common in general English
**48. initial** — count: 1, TF-IDF: 89.05, IDF: 5.138788 🔵 low — common in general English
**49. significant** — count: 1, TF-IDF: 89.26, IDF: 5.150484 🔵 low — common in general English
**50. regular** — count: 1, TF-IDF: 90.53, IDF: 5.223687 🔵 low — common in general English

---

## Full Ranked Table

All 8,673 content terms, sorted by TF-IDF descending.

| Rank | Word | Count | TF-IDF | IDF | Band |
|------|------|-------|--------|-----|------|
| 1 | **dharma** | 409 | 67,972.93 | 9.59 | 🔴 extremely high — text-exclusive |
| 2 | **teacher** | 333 | 51,360.32 | 8.899988 | 🔴 extremely high — text-exclusive |
| 3 | **buddha** | 260 | 43,210.18 | 9.59 | 🟠 very high — domain-specific |
| 4 | **beings** | 258 | 42,877.79 | 9.59 | 🟠 very high — domain-specific |
| 5 | **like** | 396 | 35,634.32 | 5.192532 | 🟠 very high — domain-specific |
| 6 | **actions** | 278 | 27,985.70 | 5.808946 | 🟠 very high — domain-specific |
| 7 | **mind** | 217 | 26,891.05 | 7.150788 | 🟠 very high — domain-specific |
| 8 | **yourself** | 154 | 24,519.98 | 9.18767 | 🟠 very high — domain-specific |
| 9 | **compassion** | 147 | 24,438.36 | 9.593135 | 🟠 very high — domain-specific |
| 10 | **life** | 240 | 22,905.14 | 5.507159 | 🟠 very high — domain-specific |
| 11 | **practice** | 190 | 22,356.46 | 6.789775 | 🟠 very high — domain-specific |
| 12 | **without** | 266 | 21,766.06 | 4.721762 | 🟠 very high — domain-specific |
| 13 | **bodhicitta** | 130 | 21,605.09 | 9.59 | 🟠 very high — domain-specific |
| 14 | **never** | 197 | 21,562.63 | 6.31599 | 🟠 very high — domain-specific |
| 15 | **practise** | 123 | 20,448.42 | 9.593135 | 🟠 very high — domain-specific |
| 16 | **merit** | 139 | 20,090.66 | 8.340372 | 🟠 very high — domain-specific |
| 17 | **teachings** | 117 | 19,444.58 | 9.59 | 🟠 very high — domain-specific |
| 18 | **realms** | 116 | 19,278.39 | 9.59 | 🟠 very high — domain-specific |
| 19 | **refuge** | 127 | 18,695.49 | 8.494523 | 🟠 very high — domain-specific |
| 20 | **death** | 128 | 18,204.56 | 8.206841 | 🟠 very high — domain-specific |
| 21 | **suffering** | 143 | 17,946.27 | 7.24176 | 🟠 very high — domain-specific |
| 22 | **others** | 178 | 17,433.39 | 5.651553 | 🟠 very high — domain-specific |
| 23 | **buddhas** | 104 | 17,284.07 | 9.59 | 🟠 very high — domain-specific |
| 24 | **negative** | 166 | 16,949.33 | 5.891833 | 🟠 very high — domain-specific |
| 25 | **teaching** | 101 | 16,785.49 | 9.59 | 🟠 very high — domain-specific |
| 26 | **body** | 149 | 16,357.98 | 6.335039 | 🟠 very high — domain-specific |
| 27 | **whatever** | 132 | 16,260.33 | 7.108229 | 🟠 very high — domain-specific |
| 28 | **king** | 129 | 16,085.30 | 7.19524 | 🟠 very high — domain-specific |
| 29 | **path** | 118 | 15,953.18 | 7.801376 | 🟠 very high — domain-specific |
| 30 | **wisdom** | 107 | 15,751.32 | 8.494523 | 🟠 very high — domain-specific |
| 31 | **time** | 235 | 15,647.19 | 3.842151 | 🟠 very high — domain-specific |
| 32 | **people** | 170 | 15,352.29 | 5.211109 | 🟠 very high — domain-specific |
| 33 | **perfect** | 96 | 15,285.19 | 9.18767 | 🟠 very high — domain-specific |
| 34 | **jewels** | 91 | 15,123.56 | 9.59 | 🟠 very high — domain-specific |
| 35 | **faith** | 108 | 14,942.45 | 7.983697 | 🟠 very high — domain-specific |
| 36 | **once** | 140 | 14,235.44 | 5.867442 | 🟠 very high — domain-specific |
| 37 | **mother** | 85 | 14,126.40 | 9.59 | 🟠 very high — domain-specific |
| 38 | **words** | 106 | 14,047.65 | 7.647225 | 🟠 very high — domain-specific |
| 39 | **hundred** | 107 | 13,820.16 | 7.453069 | 🟠 very high — domain-specific |
| 40 | **way** | 164 | 13,542.05 | 4.764821 | 🟠 very high — domain-specific |
| 41 | **lives** | 91 | 13,395.98 | 8.494523 | 🟠 very high — domain-specific |
| 42 | **samsara** | 79 | 13,129.25 | 9.59 | 🟠 very high — domain-specific |
| 43 | **happiness** | 77 | 12,796.86 | 9.59 | 🟠 very high — domain-specific |
| 44 | **gods** | 77 | 12,796.86 | 9.59 | 🟠 very high — domain-specific |
| 45 | **reborn** | 75 | 12,464.47 | 9.59 | 🟠 very high — domain-specific |
| 46 | **offerings** | 94 | 12,457.35 | 7.647225 | 🟠 very high — domain-specific |
| 47 | **everything** | 96 | 12,214.35 | 7.341843 | 🟠 very high — domain-specific |
| 48 | **human** | 86 | 11,756.57 | 7.888387 | 🟠 very high — domain-specific |
| 49 | **many** | 146 | 11,654.17 | 4.60611 | 🟠 very high — domain-specific |
| 50 | **evil** | 70 | 11,637.31 | 9.593135 | 🟠 very high — domain-specific |
| 51 | **make** | 166 | 11,611.45 | 4.036307 | 🟠 very high — domain-specific |
| 52 | **wealth** | 76 | 11,427.98 | 8.676844 | 🟠 very high — domain-specific |
| 53 | **qualities** | 81 | 11,206.84 | 7.983697 | 🟠 very high — domain-specific |
| 54 | **past** | 138 | 11,048.46 | 4.619856 | 🟠 very high — domain-specific |
| 55 | **person** | 89 | 11,029.05 | 7.150788 | 🟠 very high — domain-specific |
| 56 | **spiritual** | 66 | 10,968.74 | 9.59 | 🟠 very high — domain-specific |
| 57 | **meditation** | 66 | 10,968.74 | 9.59 | 🟠 very high — domain-specific |
| 58 | **vajra** | 65 | 10,802.54 | 9.59 | 🟠 very high — domain-specific |
| 59 | **heart** | 89 | 10,781.74 | 6.990446 | 🟠 very high — domain-specific |
| 60 | **instructions** | 71 | 10,676.14 | 8.676844 | 🟠 very high — domain-specific |
| 61 | **meditate** | 64 | 10,636.35 | 9.59 | 🟠 very high — domain-specific |
| 62 | **come** | 123 | 10,448.49 | 4.901787 | 🟠 very high — domain-specific |
| 63 | **having** | 107 | 10,443.96 | 5.632322 | 🟠 very high — domain-specific |
| 64 | **die** | 67 | 10,333.76 | 8.899988 | 🟠 very high — domain-specific |
| 65 | **buddhahood** | 62 | 10,303.97 | 9.59 | 🟠 very high — domain-specific |
| 66 | **take** | 151 | 10,243.92 | 3.914671 | 🟠 very high — domain-specific |
| 67 | **again** | 116 | 10,183.83 | 5.065927 | 🟠 very high — domain-specific |
| 68 | **thoughts** | 61 | 10,141.09 | 9.593135 | 🟠 very high — domain-specific |
| 69 | **born** | 61 | 10,141.09 | 9.593135 | 🟠 very high — domain-specific |
| 70 | **recite** | 61 | 10,137.77 | 9.59 | 🟠 very high — domain-specific |
| 71 | **pure** | 72 | 10,093.10 | 8.089058 | 🟠 very high — domain-specific |
| 72 | **always** | 89 | 10,063.99 | 6.525082 | 🟠 very high — domain-specific |
| 73 | **thousand** | 81 | 10,037.67 | 7.150788 | 🟠 very high — domain-specific |
| 74 | **mila** | 60 | 9,974.84 | 9.593135 | 🟡 high — specialist register |
| 75 | **hell** | 64 | 9,871.05 | 8.899988 | 🟡 high — specialist register |
| 76 | **taking** | 111 | 9,862.79 | 5.127227 | 🟡 high — specialist register |
| 77 | **flesh** | 59 | 9,808.59 | 9.593135 | 🟡 high — specialist register |
| 78 | **love** | 63 | 9,716.82 | 8.899988 | 🟡 high — specialist register |
| 79 | **liberation** | 58 | 9,642.34 | 9.593135 | 🟡 high — specialist register |
| 80 | **see** | 118 | 9,563.70 | 4.676811 | 🟡 high — specialist register |
| 81 | **called** | 116 | 9,507.43 | 4.729454 | 🟡 high — specialist register |
| 82 | **thought** | 91 | 9,499.30 | 6.023602 | 🟡 high — specialist register |
| 83 | **bodhisattva** | 57 | 9,473.00 | 9.59 | 🟡 high — specialist register |
| 84 | **master** | 68 | 9,408.21 | 7.983697 | 🟡 high — specialist register |
| 85 | **wrong** | 71 | 9,324.39 | 7.578232 | 🟡 high — specialist register |
| 86 | **too** | 109 | 9,303.06 | 4.92499 | 🟡 high — specialist register |
| 87 | **visualize** | 55 | 9,143.60 | 9.593135 | 🟡 high — specialist register |
| 88 | **transference** | 55 | 9,140.61 | 9.59 | 🟡 high — specialist register |
| 89 | **deities** | 55 | 9,140.61 | 9.59 | 🟡 high — specialist register |
| 90 | **times** | 94 | 9,129.18 | 5.604151 | 🟡 high — specialist register |
| 91 | **right** | 102 | 9,093.84 | 5.144619 | 🟡 high — specialist register |
| 92 | **positive** | 91 | 9,090.69 | 5.764494 | 🟡 high — specialist register |
| 93 | **himself** | 67 | 9,058.16 | 7.801376 | 🟡 high — specialist register |
| 94 | **get** | 104 | 8,998.85 | 4.992978 | 🟡 high — specialist register |
| 95 | **moment** | 83 | 8,980.11 | 6.243231 | 🟡 high — specialist register |
| 96 | **nothing** | 86 | 8,956.52 | 6.009616 | 🟡 high — specialist register |
| 97 | **food** | 102 | 8,916.93 | 5.044535 | 🟡 high — specialist register |
| 98 | **things** | 83 | 8,882.55 | 6.175409 | 🟡 high — specialist register |
| 99 | **day** | 119 | 8,877.71 | 4.304868 | 🟡 high — specialist register |
| 100 | **realization** | 62 | 8,817.83 | 8.206841 | 🟡 high — specialist register |
| 101 | **obscurations** | 53 | 8,808.23 | 9.59 | 🟡 high — specialist register |
| 102 | **single** | 84 | 8,748.23 | 6.009616 | 🟡 high — specialist register |
| 103 | **place** | 98 | 8,727.32 | 5.138788 | 🟡 high — specialist register |
| 104 | **true** | 72 | 8,722.31 | 6.990446 | 🟡 high — specialist register |
| 105 | **disciples** | 52 | 8,642.04 | 9.59 | 🟡 high — specialist register |
| 106 | **enemies** | 52 | 8,642.04 | 9.59 | 🟡 high — specialist register |
| 107 | **think** | 101 | 8,628.51 | 4.929696 | 🟡 high — specialist register |
| 108 | **water** | 83 | 8,604.67 | 5.982217 | 🟡 high — specialist register |
| 109 | **ordinary** | 84 | 8,558.91 | 5.879563 | 🟡 high — specialist register |
| 110 | **harm** | 68 | 8,533.89 | 7.24176 | 🟡 high — specialist register |
| 111 | **every** | 84 | 8,439.66 | 5.797646 | 🟡 high — specialist register |
| 112 | **power** | 91 | 8,319.77 | 5.275647 | 🟡 high — specialist register |
| 113 | **hells** | 50 | 8,309.65 | 9.59 | 🟡 high — specialist register |
| 114 | **jetsun** | 50 | 8,309.65 | 9.59 | 🟡 high — specialist register |
| 115 | **feel** | 76 | 8,269.79 | 6.278949 | 🟡 high — specialist register |
| 116 | **friends** | 58 | 8,248.94 | 8.206841 | 🟡 high — specialist register |
| 117 | **themselves** | 72 | 8,171.01 | 6.548613 | 🟡 high — specialist register |
| 118 | **sufferings** | 49 | 8,143.46 | 9.59 | 🟡 high — specialist register |
| 119 | **head** | 86 | 8,134.36 | 5.457969 | 🟡 high — specialist register |
| 120 | **says** | 120 | 8,016.67 | 3.854951 | 🟡 high — specialist register |
| 121 | **cannot** | 84 | 8,004.62 | 5.498791 | 🟡 high — specialist register |
| 122 | **profound** | 50 | 7,961.03 | 9.18767 | 🟡 high — specialist register |
| 123 | **down** | 120 | 7,941.05 | 3.818584 | 🟡 high — specialist register |
| 124 | **harmful** | 57 | 7,886.29 | 7.983697 | 🟡 high — specialist register |
| 125 | **offering** | 86 | 7,882.64 | 5.28907 | 🟡 high — specialist register |
| 126 | **father** | 51 | 7,866.00 | 8.899988 | 🟡 high — specialist register |
| 127 | **away** | 78 | 7,852.10 | 5.808946 | 🟡 high — specialist register |
| 128 | **kalpa** | 47 | 7,811.07 | 9.59 | 🟡 high — specialist register |
| 129 | **whole** | 78 | 7,748.64 | 5.732405 | 🟡 high — specialist register |
| 130 | **someone** | 60 | 7,690.19 | 7.395911 | 🟡 high — specialist register |
| 131 | **essence** | 46 | 7,647.38 | 9.593135 | 🟡 high — specialist register |
| 132 | **tibet** | 46 | 7,644.88 | 9.59 | 🟡 high — specialist register |
| 133 | **blessings** | 46 | 7,644.88 | 9.59 | 🟡 high — specialist register |
| 134 | **worlds** | 47 | 7,483.37 | 9.18767 | 🟡 high — specialist register |
| 135 | **monk** | 45 | 7,478.68 | 9.59 | 🟡 high — specialist register |
| 136 | **therefore** | 69 | 7,444.59 | 6.225839 | 🟡 high — specialist register |
| 137 | **taught** | 48 | 7,403.29 | 8.899988 | 🟡 high — specialist register |
| 138 | **doing** | 69 | 7,384.29 | 6.175409 | 🟡 high — specialist register |
| 139 | **secret** | 56 | 7,354.45 | 7.578232 | 🟡 high — specialist register |
| 140 | **perfection** | 44 | 7,312.49 | 9.59 | 🟡 high — specialist register |
| 141 | **mandala** | 44 | 7,312.49 | 9.59 | 🟡 high — specialist register |
| 142 | **ever** | 64 | 7,289.85 | 6.57271 | 🟡 high — specialist register |
| 143 | **off** | 96 | 7,270.34 | 4.37008 | 🟡 high — specialist register |
| 144 | **state** | 98 | 7,264.52 | 4.277469 | 🟡 high — specialist register |
| 145 | **hand** | 65 | 7,202.97 | 6.394462 | 🟡 high — specialist register |
| 146 | **old** | 69 | 7,202.77 | 6.023602 | 🟡 high — specialist register |
| 147 | **means** | 77 | 7,190.32 | 5.388443 | 🟡 high — specialist register |
| 148 | **put** | 89 | 7,168.75 | 4.647928 | 🟡 high — specialist register |
| 149 | **eyes** | 45 | 7,164.93 | 9.18767 | 🟡 high — specialist register |
| 150 | **blood** | 51 | 7,149.28 | 8.089058 | 🟡 high — specialist register |
| 151 | **practising** | 43 | 7,148.63 | 9.593135 | 🟡 high — specialist register |
| 152 | **lineage** | 43 | 7,146.30 | 9.59 | 🟡 high — specialist register |
| 153 | **devotion** | 43 | 7,146.30 | 9.59 | 🟡 high — specialist register |
| 154 | **guru** | 43 | 7,146.30 | 9.59 | 🟡 high — specialist register |
| 155 | **precious** | 56 | 7,125.04 | 7.341843 | 🟡 high — specialist register |
| 156 | **nature** | 58 | 7,064.24 | 7.028186 | 🟡 high — specialist register |
| 157 | **attain** | 51 | 7,056.16 | 7.983697 | 🟡 high — specialist register |
| 158 | **meaning** | 54 | 7,031.39 | 7.513694 | 🟡 high — specialist register |
| 159 | **find** | 74 | 6,989.12 | 5.45 | 🟡 high — specialist register |
| 160 | **mantra** | 42 | 6,980.11 | 9.59 | 🟡 high — specialist register |
| 161 | **bodhisattvas** | 42 | 6,980.11 | 9.59 | 🟡 high — specialist register |
| 162 | **transcendent** | 42 | 6,980.11 | 9.59 | 🟡 high — specialist register |
| 163 | **until** | 92 | 6,941.83 | 4.354037 | 🟡 high — specialist register |
| 164 | **asked** | 90 | 6,897.94 | 4.422651 | 🟡 high — specialist register |
| 165 | **know** | 68 | 6,886.30 | 5.843631 | 🟡 high — specialist register |
| 166 | **benefit** | 71 | 6,818.17 | 5.54135 | 🟡 high — specialist register |
| 167 | **authentic** | 41 | 6,813.91 | 9.59 | 🟡 high — specialist register |
| 168 | **killing** | 44 | 6,786.35 | 8.899988 | 🟡 high — specialist register |
| 169 | **effect** | 82 | 6,672.23 | 4.695295 | 🟡 high — specialist register |
| 170 | **teachers** | 40 | 6,649.89 | 9.593135 | 🟡 high — specialist register |
| 171 | **parents** | 40 | 6,647.72 | 9.59 | 🟡 high — specialist register |
| 172 | **sublime** | 40 | 6,647.72 | 9.59 | 🟡 high — specialist register |
| 173 | **speech** | 64 | 6,634.93 | 5.982217 | 🟡 high — specialist register |
| 174 | **spirits** | 50 | 6,626.25 | 7.647225 | 🟡 high — specialist register |
| 175 | **man** | 51 | 6,587.18 | 7.453069 | 🟡 high — specialist register |
| 176 | **end** | 102 | 6,518.66 | 3.687773 | 🟡 high — specialist register |
| 177 | **nectar** | 39 | 6,481.53 | 9.59 | 🟡 high — specialist register |
| 178 | **replied** | 56 | 6,452.36 | 6.648696 | 🟡 high — specialist register |
| 179 | **best** | 68 | 6,431.82 | 5.457969 | 🟡 high — specialist register |
| 180 | **anything** | 61 | 6,413.30 | 6.066775 | 🟡 high — specialist register |
| 181 | **follow** | 61 | 6,397.87 | 6.052176 | 🟡 high — specialist register |
| 182 | **free** | 71 | 6,337.24 | 5.150484 | 🟡 high — specialist register |
| 183 | **myself** | 38 | 6,317.40 | 9.593135 | 🟡 high — specialist register |
| 184 | **friend** | 38 | 6,317.40 | 9.593135 | 🟡 high — specialist register |
| 185 | **emptiness** | 38 | 6,315.33 | 9.59 | 🟡 high — specialist register |
| 186 | **root** | 46 | 6,288.40 | 7.888387 | 🟡 high — specialist register |
| 187 | **give** | 78 | 6,268.37 | 4.637308 | 🟡 high — specialist register |
| 188 | **while** | 98 | 6,199.45 | 3.650336 | 🟡 high — specialist register |
| 189 | **because** | 99 | 6,177.07 | 3.600421 | 🟡 high — specialist register |
| 190 | **sky** | 37 | 6,151.15 | 9.593135 | 🟡 high — specialist register |
| 191 | **prayers** | 37 | 6,149.14 | 9.59 | 🟡 high — specialist register |
| 192 | **monks** | 37 | 6,149.14 | 9.59 | 🟡 high — specialist register |
| 193 | **jewel** | 37 | 6,149.14 | 9.59 | 🟡 high — specialist register |
| 194 | **killed** | 51 | 6,146.16 | 6.954078 | 🟡 high — specialist register |
| 195 | **bring** | 66 | 6,080.81 | 5.316469 | 🟡 high — specialist register |
| 196 | **left** | 64 | 6,080.42 | 5.482261 | 🟡 high — specialist register |
| 197 | **went** | 61 | 6,059.83 | 5.732405 | 🟡 high — specialist register |
| 198 | **lord** | 46 | 6,041.15 | 7.578232 | 🟡 high — specialist register |
| 199 | **comes** | 55 | 6,002.21 | 6.297298 | 🟡 high — specialist register |
| 200 | **lama** | 36 | 5,984.90 | 9.593135 | 🟡 high — specialist register |
| 201 | **together** | 61 | 5,984.68 | 5.66131 | 🟡 high — specialist register |
| 202 | **impermanence** | 36 | 5,982.95 | 9.59 | 🟡 high — specialist register |
| 203 | **oddiyana** | 36 | 5,982.95 | 9.59 | 🟡 high — specialist register |
| 204 | **innumerable** | 36 | 5,982.95 | 9.59 | 🟡 high — specialist register |
| 205 | **tantras** | 36 | 5,982.95 | 9.59 | 🟡 high — specialist register |
| 206 | **demons** | 36 | 5,982.95 | 9.59 | 🟡 high — specialist register |
| 207 | **came** | 64 | 5,976.37 | 5.388443 | 🟡 high — specialist register |
| 208 | **much** | 80 | 5,964.71 | 4.302346 | 🟡 high — specialist register |
| 209 | **really** | 56 | 5,946.46 | 6.127399 | 🟡 high — specialist register |
| 210 | **look** | 60 | 5,917.61 | 5.691163 | 🟡 high — specialist register |
| 211 | **noble** | 37 | 5,891.17 | 9.18767 | 🟡 high — specialist register |
| 212 | **vows** | 40 | 5,888.34 | 8.494523 | 🟡 high — specialist register |
| 213 | **experience** | 50 | 5,883.28 | 6.789775 | 🟡 high — specialist register |
| 214 | **anyone** | 44 | 5,831.10 | 7.647225 | 🟡 high — specialist register |
| 215 | **attachment** | 35 | 5,818.66 | 9.593135 | 🟡 high — specialist register |
| 216 | **birth** | 35 | 5,816.75 | 9.59 | 🟡 high — specialist register |
| 217 | **naropa** | 35 | 5,816.75 | 9.59 | 🟡 high — specialist register |
| 218 | **present** | 69 | 5,802.49 | 4.85256 | 🟡 high — specialist register |
| 219 | **minds** | 39 | 5,741.13 | 8.494523 | 🟡 high — specialist register |
| 220 | **pain** | 38 | 5,713.99 | 8.676844 | 🟡 high — specialist register |
| 221 | **supreme** | 46 | 5,700.41 | 7.150788 | 🟡 high — specialist register |
| 222 | **cause** | 60 | 5,700.40 | 5.482261 | 🟡 high — specialist register |
| 223 | **lower** | 84 | 5,688.69 | 3.907856 | 🟡 high — specialist register |
| 224 | **animals** | 41 | 5,672.60 | 7.983697 | 🟡 high — specialist register |
| 225 | **joy** | 34 | 5,652.41 | 9.593135 | 🟡 high — specialist register |
| 226 | **vajrasattva** | 34 | 5,650.56 | 9.59 | 🟡 high — specialist register |
| 227 | **disciple** | 34 | 5,650.56 | 9.59 | 🟡 high — specialist register |
| 228 | **rinpoche** | 34 | 5,650.56 | 9.59 | 🟡 high — specialist register |
| 229 | **worldly** | 34 | 5,650.56 | 9.59 | 🟡 high — specialist register |
| 230 | **rebirth** | 34 | 5,650.56 | 9.59 | 🟡 high — specialist register |
| 231 | **daughter** | 34 | 5,650.56 | 9.59 | 🟡 high — specialist register |
| 232 | **ones** | 43 | 5,647.16 | 7.578232 | 🟡 high — specialist register |
| 233 | **said** | 222 | 5,631.61 | 1.463813 | 🟡 high — specialist register |
| 234 | **become** | 65 | 5,624.28 | 4.992978 | 🟡 high — specialist register |
| 235 | **living** | 49 | 5,623.76 | 6.622721 | 🟡 high — specialist register |
| 236 | **done** | 57 | 5,621.73 | 5.691163 | 🟡 high — specialist register |
| 237 | **thinking** | 43 | 5,599.07 | 7.513694 | 🟡 high — specialist register |
| 238 | **eat** | 38 | 5,593.93 | 8.494523 | 🟡 high — specialist register |
| 239 | **light** | 59 | 5,580.55 | 5.457969 | 🟡 high — specialist register |
| 240 | **acts** | 39 | 5,546.70 | 8.206841 | 🟡 high — specialist register |
| 241 | **giving** | 56 | 5,542.91 | 5.711571 | 🟡 high — specialist register |
| 242 | **moon** | 33 | 5,484.37 | 9.59 | 🟡 high — specialist register |
| 243 | **realm** | 33 | 5,484.37 | 9.59 | 🟡 high — specialist register |
| 244 | **atisa** | 33 | 5,484.37 | 9.59 | 🟡 high — specialist register |
| 245 | **hatred** | 33 | 5,484.37 | 9.59 | 🟡 high — specialist register |
| 246 | **confess** | 33 | 5,484.37 | 9.59 | 🟡 high — specialist register |
| 247 | **methods** | 47 | 5,482.36 | 6.730934 | 🟡 high — specialist register |
| 248 | **going** | 61 | 5,463.50 | 5.168289 | 🟡 high — specialist register |
| 249 | **concentration** | 37 | 5,446.72 | 8.494523 | 🟡 high — specialist register |
| 250 | **perfectly** | 38 | 5,404.48 | 8.206841 | 🟡 high — specialist register |
| 251 | **imagine** | 35 | 5,398.23 | 8.899988 | 🟡 high — specialist register |
| 252 | **want** | 61 | 5,396.06 | 5.104499 | 🟡 high — specialist register |
| 253 | **suffer** | 45 | 5,395.72 | 6.918987 | 🟡 high — specialist register |
| 254 | **instead** | 55 | 5,341.54 | 5.604151 | 🟡 high — specialist register |
| 255 | **pretas** | 32 | 5,318.18 | 9.59 | 🟡 high — specialist register |
| 256 | **samayas** | 32 | 5,318.18 | 9.59 | 🟡 high — specialist register |
| 257 | **geshe** | 32 | 5,318.18 | 9.59 | 🟡 high — specialist register |
| 258 | **powerful** | 42 | 5,306.44 | 7.29055 | 🟡 high — specialist register |
| 259 | **vast** | 40 | 5,301.00 | 7.647225 | 🟡 high — specialist register |
| 260 | **important** | 56 | 5,296.80 | 5.457969 | 🟡 high — specialist register |
| 261 | **advantages** | 39 | 5,272.66 | 7.801376 | 🟡 high — specialist register |
| 262 | **accomplishment** | 33 | 5,254.28 | 9.18767 | 🟡 high — specialist register |
| 263 | **son** | 34 | 5,244.00 | 8.899988 | 🟡 high — specialist register |
| 264 | **kinds** | 39 | 5,218.56 | 7.721333 | 🟡 high — specialist register |
| 265 | **don** | 40 | 5,208.44 | 7.513694 | 🟡 high — specialist register |
| 266 | **use** | 64 | 5,199.35 | 4.68786 | 🟡 high — specialist register |
| 267 | **form** | 58 | 5,171.01 | 5.144619 | 🟡 high — specialist register |
| 268 | **kind** | 47 | 5,159.90 | 6.335039 | 🟡 high — specialist register |
| 269 | **consciousness** | 31 | 5,153.67 | 9.593135 | 🟡 high — specialist register |
| 270 | **dedicate** | 31 | 5,153.67 | 9.593135 | 🟡 high — specialist register |
| 271 | **freedoms** | 31 | 5,151.98 | 9.59 | 🟡 high — specialist register |
| 272 | **sutra** | 31 | 5,151.98 | 9.59 | 🟡 high — specialist register |
| 273 | **whether** | 64 | 5,151.12 | 4.644375 | 🟡 high — specialist register |
| 274 | **listen** | 34 | 5,112.52 | 8.676844 | 🟡 high — specialist register |
| 275 | **infinite** | 32 | 5,095.06 | 9.18767 | 🟡 high — specialist register |
| 276 | **instant** | 32 | 5,095.06 | 9.18767 | 🟡 high — specialist register |
| 277 | **why** | 47 | 5,070.96 | 6.225839 | 🟡 high — specialist register |
| 278 | **wish** | 41 | 5,050.56 | 7.108229 | 🟡 high — specialist register |
| 279 | **different** | 50 | 5,043.30 | 5.820374 | 🟡 high — specialist register |
| 280 | **bad** | 47 | 5,029.88 | 6.175409 | 🟡 high — specialist register |
| 281 | **ten** | 47 | 5,016.64 | 6.159148 | 🟡 high — specialist register |
| 282 | **practices** | 46 | 4,991.04 | 6.260931 | 🟡 high — specialist register |
| 283 | **wheel** | 30 | 4,987.42 | 9.593135 | 🟡 high — specialist register |
| 284 | **prayer** | 30 | 4,987.42 | 9.593135 | 🟡 high — specialist register |
| 285 | **possessions** | 30 | 4,985.79 | 9.59 | 🟡 high — specialist register |
| 286 | **marpa** | 30 | 4,985.79 | 9.59 | 🟡 high — specialist register |
| 287 | **lamas** | 30 | 4,985.79 | 9.59 | 🟡 high — specialist register |
| 288 | **yoga** | 30 | 4,985.79 | 9.59 | 🟡 high — specialist register |
| 289 | **kill** | 35 | 4,977.81 | 8.206841 | 🟡 high — specialist register |
| 290 | **longer** | 53 | 4,962.99 | 5.40348 | 🟡 high — specialist register |
| 291 | **most** | 70 | 4,949.04 | 4.079706 | 🟡 high — specialist register |
| 292 | **arise** | 32 | 4,935.53 | 8.899988 | 🟡 high — specialist register |
| 293 | **say** | 65 | 4,922.63 | 4.37008 | 🟡 high — specialist register |
| 294 | **outer** | 33 | 4,857.88 | 8.494523 | 🟡 high — specialist register |
| 295 | **simply** | 44 | 4,830.54 | 6.335039 | 🟡 high — specialist register |
| 296 | **prostrations** | 29 | 4,819.60 | 9.59 | 🟡 high — specialist register |
| 297 | **emotions** | 29 | 4,819.60 | 9.59 | 🟡 high — specialist register |
| 298 | **sarhsara** | 29 | 4,819.60 | 9.59 | 🟡 high — specialist register |
| 299 | **tilopa** | 29 | 4,819.60 | 9.59 | 🟡 high — specialist register |
| 300 | **inner** | 30 | 4,776.62 | 9.18767 | 🟡 high — specialist register |
| 301 | **action** | 62 | 4,758.03 | 4.428349 | 🟡 high — specialist register |
| 302 | **sure** | 43 | 4,720.76 | 6.335039 | 🟡 high — specialist register |
| 303 | **live** | 43 | 4,706.56 | 6.31599 | 🟡 high — specialist register |
| 304 | **effects** | 45 | 4,697.46 | 6.023602 | 🟡 high — specialist register |
| 305 | **else** | 39 | 4,676.29 | 6.918987 | 🟡 high — specialist register |
| 306 | **teach** | 28 | 4,654.92 | 9.593135 | 🟡 high — specialist register |
| 307 | **enlightenment** | 28 | 4,653.40 | 9.59 | 🟡 high — specialist register |
| 308 | **empowerment** | 28 | 4,653.40 | 9.59 | 🟡 high — specialist register |
| 309 | **animal** | 38 | 4,628.29 | 7.028186 | 🟡 high — specialist register |
| 310 | **hear** | 33 | 4,626.00 | 8.089058 | 🟡 high — specialist register |
| 311 | **sun** | 41 | 4,619.88 | 6.502093 | 🟡 high — specialist register |
| 312 | **attained** | 29 | 4,617.40 | 9.18767 | 🟡 high — specialist register |
| 313 | **whenever** | 34 | 4,596.68 | 7.801376 | 🟡 high — specialist register |
| 314 | **rich** | 35 | 4,596.53 | 7.578232 | 🟡 high — specialist register |
| 315 | **point** | 56 | 4,593.55 | 4.733323 | 🟡 high — specialist register |
| 316 | **red** | 41 | 4,573.02 | 6.436135 | 🟡 high — specialist register |
| 317 | **completely** | 38 | 4,556.38 | 6.918987 | 🟡 high — specialist register |
| 318 | **everyone** | 35 | 4,520.61 | 7.453069 | 🟡 high — specialist register |
| 319 | **during** | 65 | 4,512.38 | 4.005887 | 🟡 high — specialist register |
| 320 | **universe** | 27 | 4,488.68 | 9.593135 | 🟡 high — specialist register |
| 321 | **practised** | 27 | 4,488.68 | 9.593135 | 🟡 high — specialist register |
| 322 | **phases** | 27 | 4,488.68 | 9.593135 | 🟡 high — specialist register |
| 323 | **purify** | 27 | 4,487.21 | 9.59 | 🟡 high — specialist register |
| 324 | **tree** | 32 | 4,485.82 | 8.089058 | 🟡 high — specialist register |
| 325 | **patience** | 28 | 4,458.18 | 9.18767 | 🟡 high — specialist register |
| 326 | **something** | 40 | 4,432.60 | 6.394462 | 🟡 high — specialist register |
| 327 | **earth** | 30 | 4,416.26 | 8.494523 | 🟡 high — specialist register |
| 328 | **generation** | 31 | 4,408.92 | 8.206841 | 🟡 high — specialist register |
| 329 | **front** | 35 | 4,392.44 | 7.24176 | 🟡 high — specialist register |
| 330 | **finally** | 36 | 4,384.70 | 7.028186 | 🟡 high — specialist register |
| 331 | **fire** | 39 | 4,364.48 | 6.457641 | 🟡 high — specialist register |
| 332 | **understand** | 34 | 4,325.92 | 7.341843 | 🟡 high — specialist register |
| 333 | **meditating** | 26 | 4,321.02 | 9.59 | 🟡 high — specialist register |
| 334 | **sheep** | 28 | 4,318.59 | 8.899988 | 🟡 high — specialist register |
| 335 | **paths** | 27 | 4,298.96 | 9.18767 | 🟡 high — specialist register |
| 336 | **ground** | 37 | 4,297.83 | 6.702763 | 🟡 high — specialist register |
| 337 | **died** | 31 | 4,289.04 | 7.983697 | 🟡 high — specialist register |
| 338 | **making** | 54 | 4,260.69 | 4.552941 | 🟡 high — specialist register |
| 339 | **made** | 68 | 4,242.84 | 3.600421 | 🟡 high — specialist register |
| 340 | **beginning** | 46 | 4,210.93 | 5.282336 | 🟡 high — specialist register |
| 341 | **drink** | 29 | 4,191.58 | 8.340372 | 🟡 high — specialist register |
| 342 | **alone** | 38 | 4,171.83 | 6.335039 | 🟡 high — specialist register |
| 343 | **let** | 38 | 4,159.29 | 6.31599 | 🟡 high — specialist register |
| 344 | **children** | 25 | 4,156.18 | 9.593135 | 🟡 high — specialist register |
| 345 | **arousing** | 25 | 4,156.18 | 9.593135 | 🟡 high — specialist register |
| 346 | **karmic** | 25 | 4,154.82 | 9.59 | 🟡 high — specialist register |
| 347 | **generosity** | 25 | 4,154.82 | 9.59 | 🟡 high — specialist register |
| 348 | **demon** | 25 | 4,154.82 | 9.59 | 🟡 high — specialist register |
| 349 | **brahmin** | 25 | 4,154.82 | 9.59 | 🟡 high — specialist register |
| 350 | **another** | 56 | 4,139.31 | 4.265259 | 🟡 high — specialist register |
| 351 | **able** | 45 | 4,124.64 | 5.28907 | 🟡 high — specialist register |
| 352 | **turn** | 39 | 4,120.49 | 6.096628 | 🟡 high — specialist register |
| 353 | **seeing** | 31 | 4,108.28 | 7.647225 | 🟡 high — specialist register |
| 354 | **bodies** | 31 | 4,071.21 | 7.578232 | 🟡 high — specialist register |
| 355 | **makes** | 45 | 4,063.84 | 5.211109 | 🟡 high — specialist register |
| 356 | **land** | 40 | 4,050.76 | 5.843631 | 🟡 high — specialist register |
| 357 | **realized** | 35 | 4,048.90 | 6.675364 | 🟡 high — specialist register |
| 358 | **effort** | 42 | 4,039.64 | 5.550084 | 🟡 high — specialist register |
| 359 | **hands** | 38 | 4,024.89 | 6.111895 | 🟡 high — specialist register |
| 360 | **peerless** | 26 | 4,010.12 | 8.899988 | 🟡 high — specialist register |
| 361 | **dead** | 31 | 4,003.97 | 7.453069 | 🟡 high — specialist register |
| 362 | **doctrine** | 24 | 3,989.94 | 9.593135 | 🟡 high — specialist register |
| 363 | **truth** | 24 | 3,989.94 | 9.593135 | 🟡 high — specialist register |
| 364 | **arouse** | 24 | 3,988.63 | 9.59 | 🟡 high — specialist register |
| 365 | **beautiful** | 24 | 3,988.63 | 9.59 | 🟡 high — specialist register |
| 366 | **deeds** | 24 | 3,988.63 | 9.59 | 🟡 high — specialist register |
| 367 | **recitation** | 24 | 3,988.63 | 9.59 | 🟡 high — specialist register |
| 368 | **future** | 52 | 3,988.04 | 4.425496 | 🟡 high — specialist register |
| 369 | **immense** | 25 | 3,980.52 | 9.18767 | 🟡 high — specialist register |
| 370 | **faults** | 25 | 3,980.52 | 9.18767 | 🟡 high — specialist register |
| 371 | **particular** | 38 | 3,976.08 | 6.037787 | 🟡 high — specialist register |
| 372 | **places** | 30 | 3,975.75 | 7.647225 | 🟡 high — specialist register |
| 373 | **causes** | 29 | 3,964.43 | 7.888387 | 🟡 high — specialist register |
| 374 | **intention** | 37 | 3,939.01 | 6.143148 | 🟡 high — specialist register |
| 375 | **appeared** | 37 | 3,928.91 | 6.127399 | 🟡 high — specialist register |
| 376 | **years** | 59 | 3,926.82 | 3.840563 | 🟡 high — specialist register |
| 377 | **need** | 48 | 3,921.36 | 4.714128 | 🟡 high — specialist register |
| 378 | **keep** | 44 | 3,913.97 | 5.132991 | 🟡 high — specialist register |
| 379 | **tell** | 33 | 3,900.56 | 6.820546 | 🟡 high — specialist register |
| 380 | **essential** | 32 | 3,876.58 | 6.990446 | 🟡 high — specialist register |
| 381 | **pile** | 25 | 3,855.88 | 8.899988 | 🟡 high — specialist register |
| 382 | **absolute** | 28 | 3,827.72 | 7.888387 | 🟡 high — specialist register |
| 383 | **sleep** | 23 | 3,823.69 | 9.593135 | 🟡 high — specialist register |
| 384 | **ask** | 36 | 3,822.72 | 6.127399 | 🟡 high — specialist register |
| 385 | **kalpas** | 23 | 3,822.44 | 9.59 | 🟡 high — specialist register |
| 386 | **vow** | 23 | 3,822.44 | 9.59 | 🟡 high — specialist register |
| 387 | **protector** | 23 | 3,822.44 | 9.59 | 🟡 high — specialist register |
| 388 | **protectors** | 23 | 3,822.44 | 9.59 | 🟡 high — specialist register |
| 389 | **confession** | 23 | 3,822.44 | 9.59 | 🟡 high — specialist register |
| 390 | **views** | 33 | 3,817.53 | 6.675364 | 🟡 high — specialist register |
| 391 | **difficult** | 41 | 3,812.88 | 5.366301 | 🟡 high — specialist register |
| 392 | **space** | 31 | 3,796.78 | 7.067407 | 🟡 high — specialist register |
| 393 | **vehicle** | 30 | 3,790.32 | 7.29055 | 🟡 high — specialist register |
| 394 | **world** | 56 | 3,787.53 | 3.902776 | 🟡 high — specialist register |
| 395 | **act** | 41 | 3,787.41 | 5.330455 | 🟡 high — specialist register |
| 396 | **complete** | 40 | 3,783.43 | 5.457969 | 🟡 high — specialist register |
| 397 | **result** | 51 | 3,780.52 | 4.277469 | 🟡 high — specialist register |
| 398 | **became** | 34 | 3,767.71 | 6.394462 | 🟡 high — specialist register |
| 399 | **perform** | 26 | 3,757.97 | 8.340372 | 🟡 high — specialist register |
| 400 | **given** | 48 | 3,755.59 | 4.514841 | 🟡 high — specialist register |
| 401 | **known** | 37 | 3,754.54 | 5.855466 | 🟡 high — specialist register |
| 402 | **found** | 37 | 3,746.96 | 5.843631 | 🟡 high — specialist register |
| 403 | **remember** | 24 | 3,701.64 | 8.899988 | 🟡 high — specialist register |
| 404 | **child** | 24 | 3,701.64 | 8.899988 | 🟡 high — specialist register |
| 405 | **truly** | 24 | 3,701.64 | 8.899988 | 🟡 high — specialist register |
| 406 | **taken** | 44 | 3,696.81 | 4.848203 | 🟡 high — specialist register |
| 407 | **around** | 55 | 3,691.34 | 3.872823 | 🟡 high — specialist register |
| 408 | **appear** | 33 | 3,680.72 | 6.436135 | 🟡 high — specialist register |
| 409 | **clothing** | 28 | 3,677.22 | 7.578232 | 🟡 high — specialist register |
| 410 | **beyond** | 33 | 3,668.68 | 6.415081 | 🟡 high — specialist register |
| 411 | **inconceivable** | 23 | 3,662.08 | 9.18767 | 🟡 high — specialist register |
| 412 | **kindness** | 22 | 3,657.44 | 9.593135 | 🟡 high — specialist register |
| 413 | **texts** | 22 | 3,657.44 | 9.593135 | 🟡 high — specialist register |
| 414 | **tradition** | 22 | 3,657.44 | 9.593135 | 🟡 high — specialist register |
| 415 | **skilful** | 22 | 3,656.25 | 9.59 | 🟡 high — specialist register |
| 416 | **faculties** | 22 | 3,656.25 | 9.59 | 🟡 high — specialist register |
| 417 | **sangha** | 22 | 3,656.25 | 9.59 | 🟡 high — specialist register |
| 418 | **slightest** | 22 | 3,656.25 | 9.59 | 🟡 high — specialist register |
| 419 | **karma** | 22 | 3,656.25 | 9.59 | 🟡 high — specialist register |
| 420 | **dedication** | 22 | 3,656.25 | 9.59 | 🟡 high — specialist register |
| 421 | **woman** | 22 | 3,656.25 | 9.59 | 🟡 high — specialist register |
| 422 | **syllable** | 22 | 3,656.25 | 9.59 | 🟡 high — specialist register |
| 423 | **happy** | 30 | 3,653.92 | 7.028186 | 🟡 high — specialist register |
| 424 | **must** | 45 | 3,650.03 | 4.68048 | 🟡 high — specialist register |
| 425 | **numerous** | 26 | 3,644.73 | 8.089058 | 🟡 high — specialist register |
| 426 | **white** | 39 | 3,636.82 | 5.381008 | 🟡 high — specialist register |
| 427 | **fact** | 36 | 3,624.05 | 5.808946 | 🟡 high — specialist register |
| 428 | **help** | 48 | 3,617.42 | 4.348746 | 🟡 high — specialist register |
| 429 | **diligence** | 28 | 3,616.49 | 7.453069 | 🟡 high — specialist register |
| 430 | **age** | 25 | 3,613.43 | 8.340372 | 🟡 high — specialist register |
| 431 | **sometimes** | 27 | 3,612.85 | 7.721333 | 🟡 high — specialist register |
| 432 | **ocean** | 29 | 3,593.73 | 7.150788 | 🟡 high — specialist register |
| 433 | **took** | 38 | 3,578.64 | 5.434252 | 🟡 high — specialist register |
| 434 | **avoid** | 35 | 3,573.65 | 5.891833 | 🟡 high — specialist register |
| 435 | **hum** | 24 | 3,533.01 | 8.494523 | 🟡 high — specialist register |
| 436 | **start** | 42 | 3,516.23 | 4.830961 | 🟡 high — specialist register |
| 437 | **set** | 51 | 3,514.39 | 3.976364 | 🟡 high — specialist register |
| 438 | **forth** | 22 | 3,502.85 | 9.18767 | 🟡 high — specialist register |
| 439 | **dust** | 22 | 3,502.85 | 9.18767 | 🟡 high — specialist register |
| 440 | **thing** | 30 | 3,499.38 | 6.730934 | 🟡 high — specialist register |
| 441 | **india** | 33 | 3,495.30 | 6.111895 | 🟡 high — specialist register |
| 442 | **mental** | 21 | 3,491.19 | 9.593135 | 🟡 high — specialist register |
| 443 | **dharmakaya** | 21 | 3,490.05 | 9.59 | 🟡 high — specialist register |
| 444 | **mantras** | 21 | 3,490.05 | 9.59 | 🟡 high — specialist register |
| 445 | **cho** | 21 | 3,490.05 | 9.59 | 🟡 high — specialist register |
| 446 | **work** | 42 | 3,482.79 | 4.785024 | 🟡 high — specialist register |
| 447 | **example** | 32 | 3,482.02 | 6.278949 | 🟡 high — specialist register |
| 448 | **along** | 36 | 3,479.19 | 5.576752 | 🟡 high — specialist register |
| 449 | **ultimate** | 26 | 3,479.04 | 7.721333 | 🟡 high — specialist register |
| 450 | **days** | 45 | 3,478.32 | 4.460282 | 🟡 high — specialist register |
| 451 | **empty** | 24 | 3,468.89 | 8.340372 | 🟡 high — specialist register |
| 452 | **palace** | 23 | 3,458.47 | 8.676844 | 🟡 high — specialist register |
| 453 | **existence** | 26 | 3,445.65 | 7.647225 | 🟡 high — specialist register |
| 454 | **men** | 26 | 3,445.65 | 7.647225 | 🟡 high — specialist register |
| 455 | **activities** | 35 | 3,439.81 | 5.671162 | 🟡 high — specialist register |
| 456 | **lived** | 25 | 3,417.61 | 7.888387 | 🟡 high — specialist register |
| 457 | **training** | 26 | 3,414.56 | 7.578232 | 🟡 high — specialist register |
| 458 | **within** | 43 | 3,407.38 | 4.57255 | 🟡 high — specialist register |
| 459 | **black** | 30 | 3,404.59 | 6.548613 | 🟡 high — specialist register |
| 460 | **since** | 52 | 3,385.50 | 3.756864 | 🟡 high — specialist register |
| 461 | **learned** | 24 | 3,364.37 | 8.089058 | 🟡 high — specialist register |
| 462 | **throughout** | 32 | 3,356.26 | 6.052176 | 🟡 high — specialist register |
| 463 | **natural** | 38 | 3,339.65 | 5.071347 | 🟡 high — specialist register |
| 464 | **mantrayana** | 20 | 3,323.86 | 9.59 | 🟡 high — specialist register |
| 465 | **reciting** | 20 | 3,323.86 | 9.59 | 🟡 high — specialist register |
| 466 | **companions** | 20 | 3,323.86 | 9.59 | 🟡 high — specialist register |
| 467 | **tirthikas** | 20 | 3,323.86 | 9.59 | 🟡 high — specialist register |
| 468 | **dying** | 20 | 3,323.86 | 9.59 | 🟡 high — specialist register |
| 469 | **impermanent** | 20 | 3,323.86 | 9.59 | 🟡 high — specialist register |
| 470 | **sadaprarudita** | 20 | 3,323.86 | 9.59 | 🟡 high — specialist register |
| 471 | **flowers** | 22 | 3,308.10 | 8.676844 | 🟡 high — specialist register |
| 472 | **fruit** | 26 | 3,308.05 | 7.341843 | 🟡 high — specialist register |
| 473 | **face** | 34 | 3,296.61 | 5.594934 | 🟡 high — specialist register |
| 474 | **above** | 42 | 3,295.27 | 4.527381 | 🟡 high — specialist register |
| 475 | **desire** | 28 | 3,294.64 | 6.789775 | 🟡 high — specialist register |
| 476 | **story** | 25 | 3,283.24 | 7.578232 | 🟡 high — specialist register |
| 477 | **towards** | 33 | 3,272.28 | 5.721934 | 🟡 high — specialist register |
| 478 | **hard** | 34 | 3,270.19 | 5.550084 | 🟡 high — specialist register |
| 479 | **better** | 38 | 3,265.28 | 4.958406 | 🟡 high — specialist register |
| 480 | **matter** | 31 | 3,251.38 | 6.052176 | 🟡 high — specialist register |
| 481 | **sorts** | 21 | 3,238.94 | 8.899988 | 🟡 high — specialist register |
| 482 | **cold** | 29 | 3,234.57 | 6.436135 | 🟡 high — specialist register |
| 483 | **saw** | 33 | 3,232.03 | 5.651553 | 🟡 high — specialist register |
| 484 | **although** | 40 | 3,204.85 | 4.623322 | 🟡 high — specialist register |
| 485 | **intermediate** | 30 | 3,202.11 | 6.159148 | 🟡 high — specialist register |
| 486 | **real** | 39 | 3,186.10 | 4.714128 | 🟡 high — specialist register |
| 487 | **small** | 37 | 3,185.60 | 4.968162 | 🟡 high — specialist register |
| 488 | **accumulate** | 20 | 3,184.41 | 9.18767 | 🟡 high — specialist register |
| 489 | **constantly** | 20 | 3,184.41 | 9.18767 | 🟡 high — specialist register |
| 490 | **clothes** | 20 | 3,184.41 | 9.18767 | 🟡 high — specialist register |
| 491 | **filled** | 22 | 3,179.82 | 8.340372 | 🟡 high — specialist register |
| 492 | **determination** | 27 | 3,176.97 | 6.789775 | 🟡 high — specialist register |
| 493 | **view** | 34 | 3,174.95 | 5.388443 | 🟡 high — specialist register |
| 494 | **accumulated** | 26 | 3,166.73 | 7.028186 | 🟡 high — specialist register |
| 495 | **insects** | 19 | 3,158.70 | 9.593135 | 🟡 high — specialist register |
| 496 | **god** | 19 | 3,158.70 | 9.593135 | 🟡 high — specialist register |
| 497 | **received** | 39 | 3,158.41 | 4.673154 | 🟡 high — specialist register |
| 498 | **later** | 40 | 3,158.31 | 4.556183 | 🟡 high — specialist register |
| 499 | **concepts** | 21 | 3,157.73 | 8.676844 | 🟡 high — specialist register |
| 500 | **sutras** | 19 | 3,157.67 | 9.59 | 🟡 high — specialist register |
| 501 | **dorje** | 19 | 3,157.67 | 9.59 | 🟡 high — specialist register |
| 502 | **jowo** | 19 | 3,157.67 | 9.59 | 🟡 high — specialist register |
| 503 | **bless** | 19 | 3,157.67 | 9.59 | 🟡 high — specialist register |
| 504 | **pray** | 19 | 3,157.67 | 9.59 | 🟡 high — specialist register |
| 505 | **creatures** | 19 | 3,157.67 | 9.59 | 🟡 high — specialist register |
| 506 | **dharmodgata** | 19 | 3,157.67 | 9.59 | 🟡 high — specialist register |
| 507 | **visualization** | 19 | 3,157.67 | 9.59 | 🟡 high — specialist register |
| 508 | **develop** | 30 | 3,154.08 | 6.066775 | 🟡 high — specialist register |
| 509 | **family** | 30 | 3,139.01 | 6.037787 | 🟡 high — specialist register |
| 510 | **train** | 22 | 3,128.91 | 8.206841 | 🟡 high — specialist register |
| 511 | **stay** | 29 | 3,120.30 | 6.208745 | 🟡 high — specialist register |
| 512 | **suddenly** | 23 | 3,109.52 | 7.801376 | 🟡 high — specialist register |
| 513 | **using** | 31 | 3,108.63 | 5.786473 | 🟡 high — specialist register |
| 514 | **offer** | 48 | 3,098.78 | 3.725252 | 🟡 high — specialist register |
| 515 | **depths** | 21 | 3,091.38 | 8.494523 | 🟡 high — specialist register |
| 516 | **please** | 21 | 3,091.38 | 8.494523 | 🟡 high — specialist register |
| 517 | **behind** | 30 | 3,082.75 | 5.929574 | 🟡 high — specialist register |
| 518 | **realize** | 24 | 3,076.08 | 7.395911 | 🟡 high — specialist register |
| 519 | **already** | 41 | 3,055.13 | 4.29983 | 🟡 high — specialist register |
| 520 | **lotus** | 19 | 3,025.19 | 9.18767 | 🟡 high — specialist register |
| 521 | **sick** | 19 | 3,025.19 | 9.18767 | 🟡 high — specialist register |
| 522 | **accomplishments** | 19 | 3,025.19 | 9.18767 | 🟡 high — specialist register |
| 523 | **rays** | 19 | 3,025.19 | 9.18767 | 🟡 high — specialist register |
| 524 | **full** | 42 | 3,024.27 | 4.155056 | 🟡 high — specialist register |
| 525 | **told** | 54 | 3,008.36 | 3.214709 | 🟡 high — specialist register |
| 526 | **middle** | 29 | 3,006.45 | 5.982217 | 🟡 high — specialist register |
| 527 | **blind** | 18 | 2,992.45 | 9.593135 | 🟢 medium — moderately distinctive |
| 528 | **purified** | 18 | 2,992.45 | 9.593135 | 🟢 medium — moderately distinctive |
| 529 | **pot** | 18 | 2,992.45 | 9.593135 | 🟢 medium — moderately distinctive |
| 530 | **renounce** | 18 | 2,992.45 | 9.593135 | 🟢 medium — moderately distinctive |
| 531 | **hair** | 18 | 2,992.45 | 9.593135 | 🟢 medium — moderately distinctive |
| 532 | **lying** | 18 | 2,992.45 | 9.593135 | 🟢 medium — moderately distinctive |
| 533 | **nagarjuna** | 18 | 2,991.47 | 9.59 | 🟢 medium — moderately distinctive |
| 534 | **wherever** | 18 | 2,991.47 | 9.59 | 🟢 medium — moderately distinctive |
| 535 | **pleasant** | 18 | 2,991.47 | 9.59 | 🟢 medium — moderately distinctive |
| 536 | **tonpa** | 18 | 2,991.47 | 9.59 | 🟢 medium — moderately distinctive |
| 537 | **unbearable** | 18 | 2,991.47 | 9.59 | 🟢 medium — moderately distinctive |
| 538 | **purification** | 18 | 2,991.47 | 9.59 | 🟢 medium — moderately distinctive |
| 539 | **empowerments** | 18 | 2,991.47 | 9.59 | 🟢 medium — moderately distinctive |
| 540 | **lead** | 35 | 2,981.55 | 4.915644 | 🟢 medium — moderately distinctive |
| 541 | **night** | 30 | 2,980.25 | 5.732405 | 🟢 medium — moderately distinctive |
| 542 | **care** | 27 | 2,964.20 | 6.335039 | 🟢 medium — moderately distinctive |
| 543 | **soon** | 34 | 2,950.88 | 5.008168 | 🟢 medium — moderately distinctive |
| 544 | **feeling** | 23 | 2,947.91 | 7.395911 | 🟢 medium — moderately distinctive |
| 545 | **becomes** | 24 | 2,939.45 | 7.067407 | 🟢 medium — moderately distinctive |
| 546 | **explained** | 25 | 2,928.71 | 6.759922 | 🟢 medium — moderately distinctive |
| 547 | **consider** | 33 | 2,919.18 | 5.104499 | 🟢 medium — moderately distinctive |
| 548 | **word** | 22 | 2,915.55 | 7.647225 | 🟢 medium — moderately distinctive |
| 549 | **young** | 22 | 2,915.55 | 7.647225 | 🟢 medium — moderately distinctive |
| 550 | **circumstances** | 27 | 2,913.10 | 6.225839 | 🟢 medium — moderately distinctive |
| 551 | **river** | 27 | 2,905.10 | 6.208745 | 🟢 medium — moderately distinctive |
| 552 | **lifetime** | 20 | 2,890.74 | 8.340372 | 🟢 medium — moderately distinctive |
| 553 | **text** | 20 | 2,890.74 | 8.340372 | 🟢 medium — moderately distinctive |
| 554 | **try** | 30 | 2,885.46 | 5.550084 | 🟢 medium — moderately distinctive |
| 555 | **rest** | 30 | 2,885.46 | 5.550084 | 🟢 medium — moderately distinctive |
| 556 | **entire** | 28 | 2,877.24 | 5.929574 | 🟢 medium — moderately distinctive |
| 557 | **recognize** | 21 | 2,870.79 | 7.888387 | 🟢 medium — moderately distinctive |
| 558 | **clean** | 18 | 2,865.97 | 9.18767 | 🟢 medium — moderately distinctive |
| 559 | **leave** | 27 | 2,859.79 | 6.111895 | 🟢 medium — moderately distinctive |
| 560 | **no-one** | 19 | 2,856.99 | 8.676844 | 🟢 medium — moderately distinctive |
| 561 | **surrounded** | 19 | 2,856.99 | 8.676844 | 🟢 medium — moderately distinctive |
| 562 | **arrived** | 22 | 2,841.53 | 7.453069 | 🟢 medium — moderately distinctive |
| 563 | **cast** | 21 | 2,839.13 | 7.801376 | 🟢 medium — moderately distinctive |
| 564 | **brings** | 27 | 2,831.84 | 6.052176 | 🟢 medium — moderately distinctive |
| 565 | **perfections** | 17 | 2,825.28 | 9.59 | 🟢 medium — moderately distinctive |
| 566 | **glorious** | 17 | 2,825.28 | 9.59 | 🟢 medium — moderately distinctive |
| 567 | **tantra** | 17 | 2,825.28 | 9.59 | 🟢 medium — moderately distinctive |
| 568 | **sangye** | 17 | 2,825.28 | 9.59 | 🟢 medium — moderately distinctive |
| 569 | **indra** | 17 | 2,825.28 | 9.59 | 🟢 medium — moderately distinctive |
| 570 | **sickness** | 17 | 2,825.28 | 9.59 | 🟢 medium — moderately distinctive |
| 571 | **practitioners** | 17 | 2,825.28 | 9.59 | 🟢 medium — moderately distinctive |
| 572 | **throne** | 17 | 2,825.28 | 9.59 | 🟢 medium — moderately distinctive |
| 573 | **nanda** | 17 | 2,825.28 | 9.59 | 🟢 medium — moderately distinctive |
| 574 | **fish** | 22 | 2,819.74 | 7.395911 | 🟢 medium — moderately distinctive |
| 575 | **saying** | 34 | 2,805.15 | 4.760829 | 🟢 medium — moderately distinctive |
| 576 | **freedom** | 23 | 2,801.34 | 7.028186 | 🟢 medium — moderately distinctive |
| 577 | **eating** | 19 | 2,796.96 | 8.494523 | 🟢 medium — moderately distinctive |
| 578 | **perceptions** | 18 | 2,776.23 | 8.899988 | 🟢 medium — moderately distinctive |
| 579 | **directions** | 18 | 2,776.23 | 8.899988 | 🟢 medium — moderately distinctive |
| 580 | **unless** | 30 | 2,774.95 | 5.337522 | 🟢 medium — moderately distinctive |
| 581 | **gave** | 32 | 2,771.67 | 4.998015 | 🟢 medium — moderately distinctive |
| 582 | **learn** | 20 | 2,767.12 | 7.983697 | 🟢 medium — moderately distinctive |
| 583 | **fault** | 20 | 2,767.12 | 7.983697 | 🟢 medium — moderately distinctive |
| 584 | **perception** | 21 | 2,757.92 | 7.578232 | 🟢 medium — moderately distinctive |
| 585 | **accumulation** | 19 | 2,746.21 | 8.340372 | 🟢 medium — moderately distinctive |
| 586 | **brought** | 28 | 2,742.33 | 5.651553 | 🟢 medium — moderately distinctive |
| 587 | **following** | 36 | 2,724.70 | 4.367389 | 🟢 medium — moderately distinctive |
| 588 | **actually** | 24 | 2,723.67 | 6.548613 | 🟢 medium — moderately distinctive |
| 589 | **next** | 40 | 2,712.44 | 3.912963 | 🟢 medium — moderately distinctive |
| 590 | **iron** | 23 | 2,706.31 | 6.789775 | 🟢 medium — moderately distinctive |
| 591 | **straight** | 20 | 2,703.93 | 7.801376 | 🟢 medium — moderately distinctive |
| 592 | **clear** | 28 | 2,697.37 | 5.558895 | 🟢 medium — moderately distinctive |
| 593 | **experienced** | 21 | 2,691.57 | 7.395911 | 🟢 medium — moderately distinctive |
| 594 | **intense** | 20 | 2,676.19 | 7.721333 | 🟢 medium — moderately distinctive |
| 595 | **mountain** | 21 | 2,671.89 | 7.341843 | 🟢 medium — moderately distinctive |
| 596 | **reality** | 21 | 2,671.89 | 7.341843 | 🟢 medium — moderately distinctive |
| 597 | **attitude** | 22 | 2,665.15 | 6.990446 | 🟢 medium — moderately distinctive |
| 598 | **continents** | 16 | 2,659.96 | 9.593135 | 🟢 medium — moderately distinctive |
| 599 | **miraculous** | 16 | 2,659.96 | 9.593135 | 🟢 medium — moderately distinctive |
| 600 | **forever** | 16 | 2,659.96 | 9.593135 | 🟢 medium — moderately distinctive |
| 601 | **legs** | 16 | 2,659.96 | 9.593135 | 🟢 medium — moderately distinctive |
| 602 | **fortunate** | 16 | 2,659.09 | 9.59 | 🟢 medium — moderately distinctive |
| 603 | **omniscient** | 16 | 2,659.09 | 9.59 | 🟢 medium — moderately distinctive |
| 604 | **preliminaries** | 16 | 2,659.09 | 9.59 | 🟢 medium — moderately distinctive |
| 605 | **deity** | 16 | 2,659.09 | 9.59 | 🟢 medium — moderately distinctive |
| 606 | **hardships** | 16 | 2,659.09 | 9.59 | 🟢 medium — moderately distinctive |
| 607 | **padampa** | 16 | 2,659.09 | 9.59 | 🟢 medium — moderately distinctive |
| 608 | **samaya** | 16 | 2,659.09 | 9.59 | 🟢 medium — moderately distinctive |
| 609 | **preta** | 16 | 2,659.09 | 9.59 | 🟢 medium — moderately distinctive |
| 610 | **thirst** | 16 | 2,659.09 | 9.59 | 🟢 medium — moderately distinctive |
| 611 | **conqueror** | 16 | 2,659.09 | 9.59 | 🟢 medium — moderately distinctive |
| 612 | **sakyamuni** | 16 | 2,659.09 | 9.59 | 🟢 medium — moderately distinctive |
| 613 | **brahma** | 16 | 2,659.09 | 9.59 | 🟢 medium — moderately distinctive |
| 614 | **nowadays** | 16 | 2,659.09 | 9.59 | 🟢 medium — moderately distinctive |
| 615 | **seated** | 16 | 2,659.09 | 9.59 | 🟢 medium — moderately distinctive |
| 616 | **bliss** | 16 | 2,659.09 | 9.59 | 🟢 medium — moderately distinctive |
| 617 | **none** | 22 | 2,651.28 | 6.954078 | 🟢 medium — moderately distinctive |
| 618 | **bear** | 23 | 2,650.08 | 6.648696 | 🟢 medium — moderately distinctive |
| 619 | **itself** | 27 | 2,639.87 | 5.641891 | 🟢 medium — moderately distinctive |
| 620 | **respect** | 23 | 2,639.72 | 6.622721 | 🟢 medium — moderately distinctive |
| 621 | **far** | 33 | 2,624.48 | 4.589189 | 🟢 medium — moderately distinctive |
| 622 | **hidden** | 17 | 2,622.00 | 8.899988 | 🟢 medium — moderately distinctive |
| 623 | **accumulations** | 17 | 2,622.00 | 8.899988 | 🟢 medium — moderately distinctive |
| 624 | **spend** | 23 | 2,619.79 | 6.57271 | 🟢 medium — moderately distinctive |
| 625 | **hot** | 20 | 2,604.22 | 7.513694 | 🟢 medium — moderately distinctive |
| 626 | **alive** | 18 | 2,601.67 | 8.340372 | 🟢 medium — moderately distinctive |
| 627 | **hunger** | 18 | 2,601.67 | 8.340372 | 🟢 medium — moderately distinctive |
| 628 | **enjoy** | 18 | 2,601.67 | 8.340372 | 🟢 medium — moderately distinctive |
| 629 | **mount** | 19 | 2,568.73 | 7.801376 | 🟢 medium — moderately distinctive |
| 630 | **ourselves** | 20 | 2,563.40 | 7.395911 | 🟢 medium — moderately distinctive |
| 631 | **quite** | 23 | 2,556.96 | 6.415081 | 🟢 medium — moderately distinctive |
| 632 | **main** | 31 | 2,555.50 | 4.756853 | 🟢 medium — moderately distinctive |
| 633 | **comfort** | 16 | 2,547.53 | 9.18767 | 🟢 medium — moderately distinctive |
| 634 | **carefully** | 21 | 2,544.01 | 6.990446 | 🟢 medium — moderately distinctive |
| 635 | **properly** | 19 | 2,542.38 | 7.721333 | 🟢 medium — moderately distinctive |
| 636 | **lies** | 19 | 2,542.38 | 7.721333 | 🟢 medium — moderately distinctive |
| 637 | **similar** | 28 | 2,537.80 | 5.230037 | 🟢 medium — moderately distinctive |
| 638 | **material** | 24 | 2,529.43 | 6.08159 | 🟢 medium — moderately distinctive |
| 639 | **source** | 26 | 2,529.28 | 5.613454 | 🟢 medium — moderately distinctive |
| 640 | **part** | 35 | 2,507.18 | 4.13355 | 🟢 medium — moderately distinctive |
| 641 | **feet** | 25 | 2,502.18 | 5.775423 | 🟢 medium — moderately distinctive |
| 642 | **guide** | 19 | 2,495.26 | 7.578232 | 🟢 medium — moderately distinctive |
| 643 | **teaches** | 15 | 2,493.71 | 9.593135 | 🟢 medium — moderately distinctive |
| 644 | **remembering** | 15 | 2,493.71 | 9.593135 | 🟢 medium — moderately distinctive |
| 645 | **pride** | 15 | 2,493.71 | 9.593135 | 🟢 medium — moderately distinctive |
| 646 | **cultivate** | 15 | 2,493.71 | 9.593135 | 🟢 medium — moderately distinctive |
| 647 | **utterly** | 15 | 2,493.71 | 9.593135 | 🟢 medium — moderately distinctive |
| 648 | **prostrate** | 15 | 2,492.89 | 9.59 | 🟢 medium — moderately distinctive |
| 649 | **conquerors** | 15 | 2,492.89 | 9.59 | 🟢 medium — moderately distinctive |
| 650 | **buddhafield** | 15 | 2,492.89 | 9.59 | 🟢 medium — moderately distinctive |
| 651 | **amitabha** | 15 | 2,492.89 | 9.59 | 🟢 medium — moderately distinctive |
| 652 | **kayas** | 15 | 2,492.89 | 9.59 | 🟢 medium — moderately distinctive |
| 653 | **nirvana** | 15 | 2,492.89 | 9.59 | 🟢 medium — moderately distinctive |
| 654 | **countless** | 15 | 2,492.89 | 9.59 | 🟢 medium — moderately distinctive |
| 655 | **divine** | 15 | 2,492.89 | 9.59 | 🟢 medium — moderately distinctive |
| 656 | **turtle** | 15 | 2,492.89 | 9.59 | 🟢 medium — moderately distinctive |
| 657 | **milarepa** | 15 | 2,492.89 | 9.59 | 🟢 medium — moderately distinctive |
| 658 | **loved** | 15 | 2,492.89 | 9.59 | 🟢 medium — moderately distinctive |
| 659 | **dissolves** | 15 | 2,492.89 | 9.59 | 🟢 medium — moderately distinctive |
| 660 | **heaven** | 15 | 2,492.89 | 9.59 | 🟢 medium — moderately distinctive |
| 661 | **beggar** | 15 | 2,492.89 | 9.59 | 🟢 medium — moderately distinctive |
| 662 | **oneself** | 15 | 2,492.89 | 9.59 | 🟢 medium — moderately distinctive |
| 663 | **downfalls** | 15 | 2,492.89 | 9.59 | 🟢 medium — moderately distinctive |
| 664 | **boundless** | 15 | 2,492.89 | 9.59 | 🟢 medium — moderately distinctive |
| 665 | **rain** | 22 | 2,487.73 | 6.525082 | 🟢 medium — moderately distinctive |
| 666 | **idea** | 22 | 2,478.96 | 6.502093 | 🟢 medium — moderately distinctive |
| 667 | **lack** | 23 | 2,468.02 | 6.191938 | 🟢 medium — moderately distinctive |
| 668 | **objects** | 16 | 2,467.76 | 8.899988 | 🟢 medium — moderately distinctive |
| 669 | **self** | 16 | 2,467.76 | 8.899988 | 🟢 medium — moderately distinctive |
| 670 | **meat** | 22 | 2,453.82 | 6.436135 | 🟢 medium — moderately distinctive |
| 671 | **enough** | 27 | 2,453.16 | 5.242857 | 🟢 medium — moderately distinctive |
| 672 | **least** | 30 | 2,443.00 | 4.699034 | 🟢 medium — moderately distinctive |
| 673 | **fear** | 22 | 2,437.93 | 6.394462 | 🟢 medium — moderately distinctive |
| 674 | **centre** | 20 | 2,435.94 | 7.028186 | 🟢 medium — moderately distinctive |
| 675 | **otherwise** | 21 | 2,429.34 | 6.675364 | 🟢 medium — moderately distinctive |
| 676 | **cut** | 35 | 2,426.35 | 4.000284 | 🟢 medium — moderately distinctive |
| 677 | **twelve** | 17 | 2,417.79 | 8.206841 | 🟢 medium — moderately distinctive |
| 678 | **ing** | 17 | 2,417.79 | 8.206841 | 🟢 medium — moderately distinctive |
| 679 | **elements** | 19 | 2,417.42 | 7.341843 | 🟢 medium — moderately distinctive |
| 680 | **inside** | 19 | 2,417.42 | 7.341843 | 🟢 medium — moderately distinctive |
| 681 | **extremely** | 22 | 2,415.27 | 6.335039 | 🟢 medium — moderately distinctive |
| 682 | **entirely** | 20 | 2,410.26 | 6.954078 | 🟢 medium — moderately distinctive |
| 683 | **speak** | 16 | 2,405.89 | 8.676844 | 🟢 medium — moderately distinctive |
| 684 | **undergo** | 16 | 2,405.89 | 8.676844 | 🟢 medium — moderately distinctive |
| 685 | **certain** | 30 | 2,403.64 | 4.623322 | 🟢 medium — moderately distinctive |
| 686 | **kings** | 15 | 2,388.31 | 9.18767 | 🟢 medium — moderately distinctive |
| 687 | **thirty-three** | 15 | 2,388.31 | 9.18767 | 🟢 medium — moderately distinctive |
| 688 | **vision** | 17 | 2,383.09 | 8.089058 | 🟢 medium — moderately distinctive |
| 689 | **excellent** | 20 | 2,374.98 | 6.852295 | 🟢 medium — moderately distinctive |
| 690 | **metal** | 23 | 2,363.44 | 5.929574 | 🟢 medium — moderately distinctive |
| 691 | **mountains** | 16 | 2,355.34 | 8.494523 | 🟢 medium — moderately distinctive |
| 692 | **accomplished** | 16 | 2,355.34 | 8.494523 | 🟢 medium — moderately distinctive |
| 693 | **perceive** | 16 | 2,355.34 | 8.494523 | 🟢 medium — moderately distinctive |
| 694 | **vehicles** | 19 | 2,354.52 | 7.150788 | 🟢 medium — moderately distinctive |
| 695 | **heard** | 19 | 2,354.52 | 7.150788 | 🟢 medium — moderately distinctive |
| 696 | **fortune** | 17 | 2,352.05 | 7.983697 | 🟢 medium — moderately distinctive |
| 697 | **pleasure** | 14 | 2,327.46 | 9.593135 | 🟢 medium — moderately distinctive |
| 698 | **dog** | 14 | 2,327.46 | 9.593135 | 🟢 medium — moderately distinctive |
| 699 | **sixteen** | 14 | 2,327.46 | 9.593135 | 🟢 medium — moderately distinctive |
| 700 | **stones** | 14 | 2,327.46 | 9.593135 | 🟢 medium — moderately distinctive |
| 701 | **sexual** | 14 | 2,327.46 | 9.593135 | 🟢 medium — moderately distinctive |
| 702 | **expanse** | 14 | 2,326.70 | 9.59 | 🟢 medium — moderately distinctive |
| 703 | **well-being** | 14 | 2,326.70 | 9.59 | 🟢 medium — moderately distinctive |
| 704 | **tears** | 14 | 2,326.70 | 9.59 | 🟢 medium — moderately distinctive |
| 705 | **rebirths** | 14 | 2,326.70 | 9.59 | 🟢 medium — moderately distinctive |
| 706 | **darkness** | 14 | 2,326.70 | 9.59 | 🟢 medium — moderately distinctive |
| 707 | **emanation** | 14 | 2,326.70 | 9.59 | 🟢 medium — moderately distinctive |
| 708 | **possess** | 14 | 2,326.70 | 9.59 | 🟢 medium — moderately distinctive |
| 709 | **vajrayana** | 14 | 2,326.70 | 9.59 | 🟢 medium — moderately distinctive |
| 710 | **mentally** | 14 | 2,326.70 | 9.59 | 🟢 medium — moderately distinctive |
| 711 | **rituals** | 14 | 2,326.70 | 9.59 | 🟢 medium — moderately distinctive |
| 712 | **liberated** | 14 | 2,326.70 | 9.59 | 🟢 medium — moderately distinctive |
| 713 | **yogi** | 14 | 2,326.70 | 9.59 | 🟢 medium — moderately distinctive |
| 714 | **antidote** | 14 | 2,326.70 | 9.59 | 🟢 medium — moderately distinctive |
| 715 | **sacred** | 14 | 2,326.70 | 9.59 | 🟢 medium — moderately distinctive |
| 716 | **wrathful** | 14 | 2,326.70 | 9.59 | 🟢 medium — moderately distinctive |
| 717 | **support** | 29 | 2,314.87 | 4.60611 | 🟢 medium — moderately distinctive |
| 718 | **reflection** | 17 | 2,298.34 | 7.801376 | 🟢 medium — moderately distinctive |
| 719 | **discipline** | 17 | 2,274.76 | 7.721333 | 🟢 medium — moderately distinctive |
| 720 | **happens** | 17 | 2,274.76 | 7.721333 | 🟢 medium — moderately distinctive |
| 721 | **top** | 24 | 2,273.40 | 5.466001 | 🟢 medium — moderately distinctive |
| 722 | **trying** | 23 | 2,268.42 | 5.691163 | 🟢 medium — moderately distinctive |
| 723 | **reason** | 24 | 2,266.74 | 5.45 | 🟢 medium — moderately distinctive |
| 724 | **particularly** | 24 | 2,263.45 | 5.442095 | 🟢 medium — moderately distinctive |
| 725 | **listening** | 15 | 2,255.52 | 8.676844 | 🟢 medium — moderately distinctive |
| 726 | **horse** | 15 | 2,255.52 | 8.676844 | 🟢 medium — moderately distinctive |
| 727 | **opportunity** | 21 | 2,253.41 | 6.191938 | 🟢 medium — moderately distinctive |
| 728 | **enter** | 21 | 2,241.48 | 6.159148 | 🟢 medium — moderately distinctive |
| 729 | **central** | 32 | 2,237.28 | 4.034378 | 🟢 medium — moderately distinctive |
| 730 | **goes** | 20 | 2,230.74 | 6.436135 | 🟢 medium — moderately distinctive |
| 731 | **bed** | 14 | 2,229.09 | 9.18767 | 🟢 medium — moderately distinctive |
| 732 | **wild** | 14 | 2,229.09 | 9.18767 | 🟢 medium — moderately distinctive |
| 733 | **eighty** | 14 | 2,229.09 | 9.18767 | 🟢 medium — moderately distinctive |
| 734 | **subjects** | 14 | 2,229.09 | 9.18767 | 🟢 medium — moderately distinctive |
| 735 | **slaughtered** | 14 | 2,229.09 | 9.18767 | 🟢 medium — moderately distinctive |
| 736 | **likewise** | 14 | 2,229.09 | 9.18767 | 🟢 medium — moderately distinctive |
| 737 | **worse** | 18 | 2,217.32 | 7.108229 | 🟢 medium — moderately distinctive |
| 738 | **easy** | 17 | 2,213.59 | 7.513694 | 🟢 medium — moderately distinctive |
| 739 | **crown** | 18 | 2,204.58 | 7.067407 | 🟢 medium — moderately distinctive |
| 740 | **turned** | 19 | 2,197.97 | 6.675364 | 🟢 medium — moderately distinctive |
| 741 | **clearly** | 20 | 2,189.10 | 6.31599 | 🟢 medium — moderately distinctive |
| 742 | **unable** | 20 | 2,189.10 | 6.31599 | 🟢 medium — moderately distinctive |
| 743 | **sign** | 21 | 2,187.06 | 6.009616 | 🟢 medium — moderately distinctive |
| 744 | **doubt** | 19 | 2,180.64 | 6.622721 | 🟢 medium — moderately distinctive |
| 745 | **getting** | 20 | 2,170.02 | 6.260931 | 🟢 medium — moderately distinctive |
| 746 | **million** | 19 | 2,164.17 | 6.57271 | 🟢 medium — moderately distinctive |
| 747 | **accumulating** | 16 | 2,163.14 | 7.801376 | 🟢 medium — moderately distinctive |
| 748 | **sit** | 16 | 2,163.14 | 7.801376 | 🟢 medium — moderately distinctive |
| 749 | **anger** | 17 | 2,162.96 | 7.341843 | 🟢 medium — moderately distinctive |
| 750 | **crowd** | 13 | 2,161.22 | 9.593135 | 🟢 medium — moderately distinctive |
| 751 | **endless** | 13 | 2,161.22 | 9.593135 | 🟢 medium — moderately distinctive |
| 752 | **experiences** | 13 | 2,161.22 | 9.593135 | 🟢 medium — moderately distinctive |
| 753 | **wonderful** | 13 | 2,161.22 | 9.593135 | 🟢 medium — moderately distinctive |
| 754 | **selfish** | 13 | 2,161.22 | 9.593135 | 🟢 medium — moderately distinctive |
| 755 | **venerable** | 13 | 2,160.51 | 9.59 | 🟢 medium — moderately distinctive |
| 756 | **sambhogakaya** | 13 | 2,160.51 | 9.59 | 🟢 medium — moderately distinctive |
| 757 | **jigme** | 13 | 2,160.51 | 9.59 | 🟢 medium — moderately distinctive |
| 758 | **tormented** | 13 | 2,160.51 | 9.59 | 🟢 medium — moderately distinctive |
| 759 | **dagpo** | 13 | 2,160.51 | 9.59 | 🟢 medium — moderately distinctive |
| 760 | **ephemeral** | 13 | 2,160.51 | 9.59 | 🟢 medium — moderately distinctive |
| 761 | **yoke** | 13 | 2,160.51 | 9.59 | 🟢 medium — moderately distinctive |
| 762 | **tantric** | 13 | 2,160.51 | 9.59 | 🟢 medium — moderately distinctive |
| 763 | **siddha** | 13 | 2,160.51 | 9.59 | 🟢 medium — moderately distinctive |
| 764 | **dissolve** | 13 | 2,160.51 | 9.59 | 🟢 medium — moderately distinctive |
| 765 | **precepts** | 13 | 2,160.51 | 9.59 | 🟢 medium — moderately distinctive |
| 766 | **primal** | 13 | 2,160.51 | 9.59 | 🟢 medium — moderately distinctive |
| 767 | **wife** | 14 | 2,159.29 | 8.899988 | 🟢 medium — moderately distinctive |
| 768 | **short** | 25 | 2,148.21 | 4.958406 | 🟢 medium — moderately distinctive |
| 769 | **number** | 27 | 2,147.31 | 4.589189 | 🟢 medium — moderately distinctive |
| 770 | **regret** | 16 | 2,140.95 | 7.721333 | 🟢 medium — moderately distinctive |
| 771 | **looking** | 22 | 2,136.62 | 5.604151 | 🟢 medium — moderately distinctive |
| 772 | **used** | 27 | 2,136.44 | 4.565971 | 🟢 medium — moderately distinctive |
| 773 | **according** | 27 | 2,119.86 | 4.53054 | 🟢 medium — moderately distinctive |
| 774 | **forms** | 17 | 2,119.77 | 7.19524 | 🟢 medium — moderately distinctive |
| 775 | **points** | 22 | 2,112.67 | 5.54135 | 🟢 medium — moderately distinctive |
| 776 | **dark** | 14 | 2,105.15 | 8.676844 | 🟢 medium — moderately distinctive |
| 777 | **exhausted** | 14 | 2,105.15 | 8.676844 | 🟢 medium — moderately distinctive |
| 778 | **ben** | 15 | 2,102.73 | 8.089058 | 🟢 medium — moderately distinctive |
| 779 | **high** | 29 | 2,101.47 | 4.181489 | 🟢 medium — moderately distinctive |
| 780 | **big** | 21 | 2,086.17 | 5.732405 | 🟢 medium — moderately distinctive |
| 781 | **trees** | 16 | 2,083.38 | 7.513694 | 🟢 medium — moderately distinctive |
| 782 | **knowledge** | 15 | 2,075.34 | 7.983697 | 🟢 medium — moderately distinctive |
| 783 | **lake** | 18 | 2,073.97 | 6.648696 | 🟢 medium — moderately distinctive |
| 784 | **skin** | 13 | 2,069.87 | 9.18767 | 🟢 medium — moderately distinctive |
| 785 | **bound** | 16 | 2,066.57 | 7.453069 | 🟢 medium — moderately distinctive |
| 786 | **case** | 22 | 2,065.93 | 5.418748 | 🟢 medium — moderately distinctive |
| 787 | **presence** | 18 | 2,065.87 | 6.622721 | 🟢 medium — moderately distinctive |
| 788 | **seem** | 18 | 2,065.87 | 6.622721 | 🟢 medium — moderately distinctive |
| 789 | **sowing** | 14 | 2,060.92 | 8.494523 | 🟢 medium — moderately distinctive |
| 790 | **protect** | 20 | 2,055.17 | 5.929574 | 🟢 medium — moderately distinctive |
| 791 | **fail** | 17 | 2,048.72 | 6.954078 | 🟢 medium — moderately distinctive |
| 792 | **claim** | 17 | 2,048.72 | 6.954078 | 🟢 medium — moderately distinctive |
| 793 | **hundreds** | 17 | 2,038.38 | 6.918987 | 🟢 medium — moderately distinctive |
| 794 | **stop** | 21 | 2,036.14 | 5.594934 | 🟢 medium — moderately distinctive |
| 795 | **coming** | 21 | 2,026.26 | 5.567784 | 🟢 medium — moderately distinctive |
| 796 | **reflect** | 23 | 2,019.21 | 5.065927 | 🟢 medium — moderately distinctive |
| 797 | **higher** | 30 | 2,018.60 | 3.882708 | 🟢 medium — moderately distinctive |
| 798 | **ways** | 20 | 2,009.44 | 5.797646 | 🟢 medium — moderately distinctive |
| 799 | **arms** | 16 | 2,007.97 | 7.24176 | 🟢 medium — moderately distinctive |
| 800 | **fully** | 21 | 2,007.27 | 5.515598 | 🟢 medium — moderately distinctive |
| 801 | **desires** | 13 | 2,005.06 | 8.899988 | 🟢 medium — moderately distinctive |
| 802 | **awareness** | 13 | 2,005.06 | 8.899988 | 🟢 medium — moderately distinctive |
| 803 | **instruction** | 12 | 1,994.97 | 9.593135 | 🟢 medium — moderately distinctive |
| 804 | **blazing** | 12 | 1,994.97 | 9.593135 | 🟢 medium — moderately distinctive |
| 805 | **meru** | 12 | 1,994.97 | 9.593135 | 🟢 medium — moderately distinctive |
| 806 | **devote** | 12 | 1,994.97 | 9.593135 | 🟢 medium — moderately distinctive |
| 807 | **sincere** | 12 | 1,994.97 | 9.593135 | 🟢 medium — moderately distinctive |
| 808 | **nirmanakaya** | 12 | 1,994.32 | 9.59 | 🟢 medium — moderately distinctive |
| 809 | **poisons** | 12 | 1,994.32 | 9.59 | 🟢 medium — moderately distinctive |
| 810 | **torments** | 12 | 1,994.32 | 9.59 | 🟢 medium — moderately distinctive |
| 811 | **compassionate** | 12 | 1,994.32 | 9.59 | 🟢 medium — moderately distinctive |
| 812 | **twenty-one** | 12 | 1,994.32 | 9.59 | 🟢 medium — moderately distinctive |
| 813 | **rejoice** | 12 | 1,994.32 | 9.59 | 🟢 medium — moderately distinctive |
| 814 | **useless** | 12 | 1,994.32 | 9.59 | 🟢 medium — moderately distinctive |
| 815 | **breath** | 12 | 1,994.32 | 9.59 | 🟢 medium — moderately distinctive |
| 816 | **bones** | 12 | 1,994.32 | 9.59 | 🟢 medium — moderately distinctive |
| 817 | **torment** | 12 | 1,994.32 | 9.59 | 🟢 medium — moderately distinctive |
| 818 | **frog** | 12 | 1,994.32 | 9.59 | 🟢 medium — moderately distinctive |
| 819 | **abbot** | 12 | 1,994.32 | 9.59 | 🟢 medium — moderately distinctive |
| 820 | **ritual** | 12 | 1,994.32 | 9.59 | 🟢 medium — moderately distinctive |
| 821 | **goddesses** | 12 | 1,994.32 | 9.59 | 🟢 medium — moderately distinctive |
| 822 | **wish-granting** | 12 | 1,994.32 | 9.59 | 🟢 medium — moderately distinctive |
| 823 | **purifying** | 12 | 1,994.32 | 9.59 | 🟢 medium — moderately distinctive |
| 824 | **skilfully** | 12 | 1,994.32 | 9.59 | 🟢 medium — moderately distinctive |
| 825 | **skull** | 12 | 1,994.32 | 9.59 | 🟢 medium — moderately distinctive |
| 826 | **receive** | 23 | 1,994.16 | 5.003079 | 🟢 medium — moderately distinctive |
| 827 | **signs** | 20 | 1,990.50 | 5.742988 | 🟢 medium — moderately distinctive |
| 828 | **obstacles** | 15 | 1,987.88 | 7.647225 | 🟢 medium — moderately distinctive |
| 829 | **immediately** | 22 | 1,963.65 | 5.150484 | 🟢 medium — moderately distinctive |
| 830 | **obtain** | 18 | 1,958.64 | 6.278949 | 🟢 medium — moderately distinctive |
| 831 | **sake** | 13 | 1,954.79 | 8.676844 | 🟢 medium — moderately distinctive |
| 832 | **indeed** | 15 | 1,953.16 | 7.513694 | 🟢 medium — moderately distinctive |
| 833 | **hold** | 23 | 1,946.54 | 4.883605 | 🟢 medium — moderately distinctive |
| 834 | **heat** | 15 | 1,937.41 | 7.453069 | 🟢 medium — moderately distinctive |
| 835 | **seed** | 15 | 1,937.41 | 7.453069 | 🟢 medium — moderately distinctive |
| 836 | **blue** | 14 | 1,936.98 | 7.983697 | 🟢 medium — moderately distinctive |
| 837 | **stone** | 14 | 1,936.98 | 7.983697 | 🟢 medium — moderately distinctive |
| 838 | **channels** | 14 | 1,936.98 | 7.983697 | 🟢 medium — moderately distinctive |
| 839 | **side** | 18 | 1,936.74 | 6.208745 | 🟢 medium — moderately distinctive |
| 840 | **chance** | 19 | 1,920.26 | 5.831935 | 🟢 medium — moderately distinctive |
| 841 | **heads** | 16 | 1,918.48 | 6.918987 | 🟢 medium — moderately distinctive |
| 842 | **under** | 33 | 1,915.78 | 3.34994 | 🟢 medium — moderately distinctive |
| 843 | **offered** | 23 | 1,913.80 | 4.801485 | 🟢 medium — moderately distinctive |
| 844 | **escape** | 13 | 1,913.71 | 8.494523 | 🟢 medium — moderately distinctive |
| 845 | **harsh** | 13 | 1,913.71 | 8.494523 | 🟢 medium — moderately distinctive |
| 846 | **pieces** | 13 | 1,913.71 | 8.494523 | 🟢 medium — moderately distinctive |
| 847 | **angry** | 13 | 1,913.71 | 8.494523 | 🟢 medium — moderately distinctive |
| 848 | **motivation** | 12 | 1,910.65 | 9.18767 | 🟢 medium — moderately distinctive |
| 849 | **blessing** | 12 | 1,910.65 | 9.18767 | 🟢 medium — moderately distinctive |
| 850 | **transform** | 12 | 1,910.65 | 9.18767 | 🟢 medium — moderately distinctive |
| 851 | **hat** | 12 | 1,910.65 | 9.18767 | 🟢 medium — moderately distinctive |
| 852 | **discord** | 12 | 1,910.65 | 9.18767 | 🟢 medium — moderately distinctive |
| 853 | **tea** | 16 | 1,909.08 | 6.885085 | 🟢 medium — moderately distinctive |
| 854 | **committed** | 18 | 1,897.07 | 6.08159 | 🟢 medium — moderately distinctive |
| 855 | **believe** | 21 | 1,896.46 | 5.211109 | 🟢 medium — moderately distinctive |
| 856 | **caught** | 14 | 1,892.75 | 7.801376 | 🟢 medium — moderately distinctive |
| 857 | **poor** | 18 | 1,892.45 | 6.066775 | 🟢 medium — moderately distinctive |
| 858 | **fall** | 27 | 1,884.11 | 4.026701 | 🟢 medium — moderately distinctive |
| 859 | **level** | 26 | 1,883.07 | 4.179259 | 🟢 medium — moderately distinctive |
| 860 | **wishes** | 13 | 1,878.98 | 8.340372 | 🟢 medium — moderately distinctive |
| 861 | **knew** | 13 | 1,878.98 | 8.340372 | 🟢 medium — moderately distinctive |
| 862 | **honour** | 13 | 1,878.98 | 8.340372 | 🟢 medium — moderately distinctive |
| 863 | **met** | 20 | 1,878.12 | 5.418748 | 🟢 medium — moderately distinctive |
| 864 | **powers** | 16 | 1,874.37 | 6.759922 | 🟢 medium — moderately distinctive |
| 865 | **mouth** | 14 | 1,873.33 | 7.721333 | 🟢 medium — moderately distinctive |
| 866 | **base** | 22 | 1,870.59 | 4.906385 | 🟢 medium — moderately distinctive |
| 867 | **extraordinary** | 23 | 1,862.65 | 4.673154 | 🟢 medium — moderately distinctive |
| 868 | **leaving** | 17 | 1,855.23 | 6.297298 | 🟢 medium — moderately distinctive |
| 869 | **reach** | 20 | 1,854.92 | 5.351808 | 🟢 medium — moderately distinctive |
| 870 | **huge** | 18 | 1,853.68 | 5.942477 | 🟢 medium — moderately distinctive |
| 871 | **seen** | 23 | 1,852.60 | 4.647928 | 🟢 medium — moderately distinctive |
| 872 | **sense** | 16 | 1,850.93 | 6.675364 | 🟢 medium — moderately distinctive |
| 873 | **leaves** | 16 | 1,850.93 | 6.675364 | 🟢 medium — moderately distinctive |
| 874 | **reign** | 12 | 1,850.82 | 8.899988 | 🟢 medium — moderately distinctive |
| 875 | **humans** | 12 | 1,850.82 | 8.899988 | 🟢 medium — moderately distinctive |
| 876 | **birds** | 12 | 1,850.82 | 8.899988 | 🟢 medium — moderately distinctive |
| 877 | **wishing** | 12 | 1,850.82 | 8.899988 | 🟢 medium — moderately distinctive |
| 878 | **lay** | 15 | 1,847.77 | 7.108229 | 🟢 medium — moderately distinctive |
| 879 | **started** | 20 | 1,845.08 | 5.323438 | 🟢 medium — moderately distinctive |
| 880 | **wind** | 14 | 1,838.61 | 7.578232 | 🟢 medium — moderately distinctive |
| 881 | **conduct** | 15 | 1,837.15 | 7.067407 | 🟢 medium — moderately distinctive |
| 882 | **happened** | 15 | 1,837.15 | 7.067407 | 🟢 medium — moderately distinctive |
| 883 | **serve** | 16 | 1,836.33 | 6.622721 | 🟢 medium — moderately distinctive |
| 884 | **holding** | 22 | 1,835.37 | 4.814012 | 🟢 medium — moderately distinctive |
| 885 | **terrible** | 11 | 1,828.72 | 9.593135 | 🟢 medium — moderately distinctive |
| 886 | **attaining** | 11 | 1,828.72 | 9.593135 | 🟢 medium — moderately distinctive |
| 887 | **attendants** | 11 | 1,828.72 | 9.593135 | 🟢 medium — moderately distinctive |
| 888 | **servant** | 11 | 1,828.72 | 9.593135 | 🟢 medium — moderately distinctive |
| 889 | **bowl** | 11 | 1,828.72 | 9.593135 | 🟢 medium — moderately distinctive |
| 890 | **misconduct** | 11 | 1,828.72 | 9.593135 | 🟢 medium — moderately distinctive |
| 891 | **crest** | 11 | 1,828.72 | 9.593135 | 🟢 medium — moderately distinctive |
| 892 | **rigdzin** | 11 | 1,828.12 | 9.59 | 🟢 medium — moderately distinctive |
| 893 | **lingpa** | 11 | 1,828.12 | 9.59 | 🟢 medium — moderately distinctive |
| 894 | **impure** | 11 | 1,828.12 | 9.59 | 🟢 medium — moderately distinctive |
| 895 | **physically** | 11 | 1,828.12 | 9.59 | 🟢 medium — moderately distinctive |
| 896 | **mothers** | 11 | 1,828.12 | 9.59 | 🟢 medium — moderately distinctive |
| 897 | **spontaneously** | 11 | 1,828.12 | 9.59 | 🟢 medium — moderately distinctive |
| 898 | **followers** | 11 | 1,828.12 | 9.59 | 🟢 medium — moderately distinctive |
| 899 | **patrons** | 11 | 1,828.12 | 9.59 | 🟢 medium — moderately distinctive |
| 900 | **elephant** | 11 | 1,828.12 | 9.59 | 🟢 medium — moderately distinctive |
| 901 | **knife** | 11 | 1,828.12 | 9.59 | 🟢 medium — moderately distinctive |
| 902 | **ignorance** | 11 | 1,828.12 | 9.59 | 🟢 medium — moderately distinctive |
| 903 | **appearances** | 11 | 1,828.12 | 9.59 | 🟢 medium — moderately distinctive |
| 904 | **chatter** | 11 | 1,828.12 | 9.59 | 🟢 medium — moderately distinctive |
| 905 | **mindfulness** | 11 | 1,828.12 | 9.59 | 🟢 medium — moderately distinctive |
| 906 | **impartiality** | 11 | 1,828.12 | 9.59 | 🟢 medium — moderately distinctive |
| 907 | **element** | 14 | 1,822.95 | 7.513694 | 🟢 medium — moderately distinctive |
| 908 | **rock** | 13 | 1,822.37 | 8.089058 | 🟢 medium — moderately distinctive |
| 909 | **follows** | 19 | 1,818.90 | 5.524108 | 🟢 medium — moderately distinctive |
| 910 | **lose** | 16 | 1,815.78 | 6.548613 | 🟢 medium — moderately distinctive |
| 911 | **importance** | 15 | 1,807.69 | 6.954078 | 🟢 medium — moderately distinctive |
| 912 | **physical** | 15 | 1,807.69 | 6.954078 | 🟢 medium — moderately distinctive |
| 913 | **thousands** | 15 | 1,807.69 | 6.954078 | 🟢 medium — moderately distinctive |
| 914 | **wonder** | 12 | 1,804.42 | 8.676844 | 🟢 medium — moderately distinctive |
| 915 | **destroy** | 12 | 1,804.42 | 8.676844 | 🟢 medium — moderately distinctive |
| 916 | **walk** | 12 | 1,804.42 | 8.676844 | 🟢 medium — moderately distinctive |
| 917 | **second** | 24 | 1,800.02 | 4.327858 | 🟢 medium — moderately distinctive |
| 918 | **instance** | 13 | 1,798.63 | 7.983697 | 🟢 medium — moderately distinctive |
| 919 | **create** | 17 | 1,796.11 | 6.096628 | 🟢 medium — moderately distinctive |
| 920 | **putting** | 16 | 1,790.56 | 6.457641 | 🟢 medium — moderately distinctive |
| 921 | **benefits** | 18 | 1,788.15 | 5.732405 | 🟢 medium — moderately distinctive |
| 922 | **sections** | 13 | 1,777.16 | 7.888387 | 🟢 medium — moderately distinctive |
| 923 | **round** | 18 | 1,775.28 | 5.691163 | 🟢 medium — moderately distinctive |
| 924 | **belief** | 15 | 1,772.98 | 6.820546 | 🟢 medium — moderately distinctive |
| 925 | **order** | 20 | 1,769.20 | 5.104499 | 🟢 medium — moderately distinctive |
| 926 | **smallest** | 12 | 1,766.50 | 8.494523 | 🟢 medium — moderately distinctive |
| 927 | **butter** | 13 | 1,757.55 | 7.801376 | 🟢 medium — moderately distinctive |
| 928 | **tendencies** | 11 | 1,751.43 | 9.18767 | 🟢 medium — moderately distinctive |
| 929 | **piece** | 11 | 1,751.43 | 9.18767 | 🟢 medium — moderately distinctive |
| 930 | **bird** | 11 | 1,751.43 | 9.18767 | 🟢 medium — moderately distinctive |
| 931 | **abandon** | 13 | 1,739.52 | 7.721333 | 🟢 medium — moderately distinctive |
| 932 | **false** | 13 | 1,739.52 | 7.721333 | 🟢 medium — moderately distinctive |
| 933 | **hearing** | 16 | 1,736.01 | 6.260931 | 🟢 medium — moderately distinctive |
| 934 | **feels** | 14 | 1,734.91 | 7.150788 | 🟢 medium — moderately distinctive |
| 935 | **gather** | 12 | 1,734.45 | 8.340372 | 🟢 medium — moderately distinctive |
| 936 | **accomplish** | 12 | 1,734.45 | 8.340372 | 🟢 medium — moderately distinctive |
| 937 | **activity** | 18 | 1,734.02 | 5.558895 | 🟢 medium — moderately distinctive |
| 938 | **study** | 18 | 1,715.28 | 5.498791 | 🟢 medium — moderately distinctive |
| 939 | **weapons** | 12 | 1,706.68 | 8.206841 | 🟢 medium — moderately distinctive |
| 940 | **home** | 19 | 1,703.72 | 5.174295 | 🟢 medium — moderately distinctive |
| 941 | **confidence** | 16 | 1,703.35 | 6.143148 | 🟢 medium — moderately distinctive |
| 942 | **actual** | 16 | 1,698.99 | 6.127399 | 🟢 medium — moderately distinctive |
| 943 | **vigilance** | 11 | 1,696.59 | 8.899988 | 🟢 medium — moderately distinctive |
| 944 | **easily** | 14 | 1,696.00 | 6.990446 | 🟢 medium — moderately distinctive |
| 945 | **deep** | 14 | 1,696.00 | 6.990446 | 🟢 medium — moderately distinctive |
| 946 | **impossible** | 14 | 1,696.00 | 6.990446 | 🟢 medium — moderately distinctive |
| 947 | **across** | 15 | 1,690.20 | 6.502093 | 🟢 medium — moderately distinctive |
| 948 | **name** | 21 | 1,687.64 | 4.637308 | 🟢 medium — moderately distinctive |
| 949 | **kingdom** | 14 | 1,687.18 | 6.954078 | 🟢 medium — moderately distinctive |
| 950 | **keeping** | 15 | 1,684.36 | 6.47962 | 🟢 medium — moderately distinctive |
| 951 | **equal** | 17 | 1,682.67 | 5.711571 | 🟢 medium — moderately distinctive |
| 952 | **gathered** | 12 | 1,682.18 | 8.089058 | 🟢 medium — moderately distinctive |
| 953 | **fly** | 12 | 1,682.18 | 8.089058 | 🟢 medium — moderately distinctive |
| 954 | **commit** | 12 | 1,682.18 | 8.089058 | 🟢 medium — moderately distinctive |
| 955 | **levels** | 22 | 1,679.72 | 4.405749 | 🟢 medium — moderately distinctive |
| 956 | **superior** | 13 | 1,679.08 | 7.453069 | 🟢 medium — moderately distinctive |
| 957 | **got** | 15 | 1,673.06 | 6.436135 | 🟢 medium — moderately distinctive |
| 958 | **spent** | 15 | 1,673.06 | 6.436135 | 🟢 medium — moderately distinctive |
| 959 | **protection** | 16 | 1,670.21 | 6.023602 | 🟢 medium — moderately distinctive |
| 960 | **chapter** | 14 | 1,662.49 | 6.852295 | 🟢 medium — moderately distinctive |
| 961 | **phase** | 14 | 1,662.49 | 6.852295 | 🟢 medium — moderately distinctive |
| 962 | **manifest** | 10 | 1,662.47 | 9.593135 | 🟢 medium — moderately distinctive |
| 963 | **grass** | 10 | 1,662.47 | 9.593135 | 🟢 medium — moderately distinctive |
| 964 | **dream** | 10 | 1,662.47 | 9.593135 | 🟢 medium — moderately distinctive |
| 965 | **relatives** | 10 | 1,662.47 | 9.593135 | 🟢 medium — moderately distinctive |
| 966 | **energies** | 10 | 1,662.47 | 9.593135 | 🟢 medium — moderately distinctive |
| 967 | **pouring** | 10 | 1,662.47 | 9.593135 | 🟢 medium — moderately distinctive |
| 968 | **pith** | 10 | 1,661.93 | 9.59 | 🟢 medium — moderately distinctive |
| 969 | **samantabhadra** | 10 | 1,661.93 | 9.59 | 🟢 medium — moderately distinctive |
| 970 | **embodiment** | 10 | 1,661.93 | 9.59 | 🟢 medium — moderately distinctive |
| 971 | **distraction** | 10 | 1,661.93 | 9.59 | 🟢 medium — moderately distinctive |
| 972 | **jealousy** | 10 | 1,661.93 | 9.59 | 🟢 medium — moderately distinctive |
| 973 | **practitioner** | 10 | 1,661.93 | 9.59 | 🟢 medium — moderately distinctive |
| 974 | **dreams** | 10 | 1,661.93 | 9.59 | 🟢 medium — moderately distinctive |
| 975 | **cave** | 10 | 1,661.93 | 9.59 | 🟢 medium — moderately distinctive |
| 976 | **tsa-tsa** | 10 | 1,661.93 | 9.59 | 🟢 medium — moderately distinctive |
| 977 | **monastic** | 10 | 1,661.93 | 9.59 | 🟢 medium — moderately distinctive |
| 978 | **lifespan** | 10 | 1,661.93 | 9.59 | 🟢 medium — moderately distinctive |
| 979 | **cried** | 10 | 1,661.93 | 9.59 | 🟢 medium — moderately distinctive |
| 980 | **condensed** | 10 | 1,661.93 | 9.59 | 🟢 medium — moderately distinctive |
| 981 | **liberate** | 10 | 1,661.93 | 9.59 | 🟢 medium — moderately distinctive |
| 982 | **limbs** | 10 | 1,661.93 | 9.59 | 🟢 medium — moderately distinctive |
| 983 | **siddhas** | 10 | 1,661.93 | 9.59 | 🟢 medium — moderately distinctive |
| 984 | **clairvoyance** | 10 | 1,661.93 | 9.59 | 🟢 medium — moderately distinctive |
| 985 | **alms** | 10 | 1,661.93 | 9.59 | 🟢 medium — moderately distinctive |
| 986 | **temple** | 10 | 1,661.93 | 9.59 | 🟢 medium — moderately distinctive |
| 987 | **humble** | 10 | 1,661.93 | 9.59 | 🟢 medium — moderately distinctive |
| 988 | **immeasurable** | 10 | 1,661.93 | 9.59 | 🟢 medium — moderately distinctive |
| 989 | **misdeeds** | 10 | 1,661.93 | 9.59 | 🟢 medium — moderately distinctive |
| 990 | **obey** | 10 | 1,661.93 | 9.59 | 🟢 medium — moderately distinctive |
| 991 | **treasure** | 10 | 1,661.93 | 9.59 | 🟢 medium — moderately distinctive |
| 992 | **vase** | 10 | 1,661.93 | 9.59 | 🟢 medium — moderately distinctive |
| 993 | **skull-cup** | 10 | 1,661.93 | 9.59 | 🟢 medium — moderately distinctive |
| 994 | **statue** | 10 | 1,661.93 | 9.59 | 🟢 medium — moderately distinctive |
| 995 | **tormas** | 10 | 1,661.93 | 9.59 | 🟢 medium — moderately distinctive |
| 996 | **garab** | 10 | 1,661.93 | 9.59 | 🟢 medium — moderately distinctive |
| 997 | **understanding** | 14 | 1,654.78 | 6.820546 | 🟢 medium — moderately distinctive |
| 998 | **female** | 11 | 1,654.05 | 8.676844 | 🟢 medium — moderately distinctive |
| 999 | **enemy** | 11 | 1,654.05 | 8.676844 | 🟢 medium — moderately distinctive |
| 1000 | **freed** | 11 | 1,654.05 | 8.676844 | 🟢 medium — moderately distinctive |
| 1001 | **aspects** | 13 | 1,654.03 | 7.341843 | 🟢 medium — moderately distinctive |
| 1002 | **read** | 13 | 1,654.03 | 7.341843 | 🟢 medium — moderately distinctive |
| 1003 | **followed** | 17 | 1,653.76 | 5.613454 | 🟢 medium — moderately distinctive |
| 1004 | **toward** | 16 | 1,644.14 | 5.929574 | 🟢 medium — moderately distinctive |
| 1005 | **road** | 13 | 1,642.47 | 7.29055 | 🟢 medium — moderately distinctive |
| 1006 | **image** | 12 | 1,640.45 | 7.888387 | 🟢 medium — moderately distinctive |
| 1007 | **among** | 20 | 1,632.58 | 4.710333 | 🟢 medium — moderately distinctive |
| 1008 | **approach** | 15 | 1,627.51 | 6.260931 | 🟢 medium — moderately distinctive |
| 1009 | **assembly** | 12 | 1,622.36 | 7.801376 | 🟢 medium — moderately distinctive |
| 1010 | **rid** | 11 | 1,619.29 | 8.494523 | 🟢 medium — moderately distinctive |
| 1011 | **beat** | 11 | 1,619.29 | 8.494523 | 🟢 medium — moderately distinctive |
| 1012 | **wear** | 11 | 1,619.29 | 8.494523 | 🟢 medium — moderately distinctive |
| 1013 | **passed** | 15 | 1,618.39 | 6.225839 | 🟢 medium — moderately distinctive |
| 1014 | **built** | 14 | 1,606.79 | 6.622721 | 🟢 medium — moderately distinctive |
| 1015 | **happen** | 14 | 1,606.79 | 6.622721 | 🟢 medium — moderately distinctive |
| 1016 | **sons** | 12 | 1,605.71 | 7.721333 | 🟢 medium — moderately distinctive |
| 1017 | **spread** | 14 | 1,600.65 | 6.597403 | 🟢 medium — moderately distinctive |
| 1018 | **large** | 20 | 1,594.10 | 4.599307 | 🟢 medium — moderately distinctive |
| 1019 | **direction** | 15 | 1,592.80 | 6.127399 | 🟢 medium — moderately distinctive |
| 1020 | **indispensable** | 10 | 1,592.21 | 9.18767 | 🟢 medium — moderately distinctive |
| 1021 | **eaten** | 10 | 1,592.21 | 9.18767 | 🟢 medium — moderately distinctive |
| 1022 | **sincerely** | 10 | 1,592.21 | 9.18767 | 🟢 medium — moderately distinctive |
| 1023 | **hearts** | 10 | 1,592.21 | 9.18767 | 🟢 medium — moderately distinctive |
| 1024 | **wheels** | 10 | 1,592.21 | 9.18767 | 🟢 medium — moderately distinctive |
| 1025 | **advice** | 12 | 1,590.30 | 7.647225 | 🟢 medium — moderately distinctive |
| 1026 | **moreover** | 12 | 1,590.30 | 7.647225 | 🟢 medium — moderately distinctive |
| 1027 | **rely** | 12 | 1,590.30 | 7.647225 | 🟢 medium — moderately distinctive |
| 1028 | **examining** | 12 | 1,590.30 | 7.647225 | 🟢 medium — moderately distinctive |
| 1029 | **disappeared** | 11 | 1,589.91 | 8.340372 | 🟢 medium — moderately distinctive |
| 1030 | **knowing** | 11 | 1,589.91 | 8.340372 | 🟢 medium — moderately distinctive |
| 1031 | **purity** | 11 | 1,589.91 | 8.340372 | 🟢 medium — moderately distinctive |
| 1032 | **forces** | 15 | 1,588.77 | 6.111895 | 🟢 medium — moderately distinctive |
| 1033 | **house** | 20 | 1,583.69 | 4.569255 | 🟢 medium — moderately distinctive |
| 1034 | **often** | 14 | 1,577.52 | 6.502093 | 🟢 medium — moderately distinctive |
| 1035 | **poison** | 12 | 1,575.95 | 7.578232 | 🟢 medium — moderately distinctive |
| 1036 | **warm** | 12 | 1,575.95 | 7.578232 | 🟢 medium — moderately distinctive |
| 1037 | **milk** | 12 | 1,575.95 | 7.578232 | 🟢 medium — moderately distinctive |
| 1038 | **open** | 20 | 1,571.37 | 4.53371 | 🟢 medium — moderately distinctive |
| 1039 | **few** | 18 | 1,570.29 | 5.034009 | 🟢 medium — moderately distinctive |
| 1040 | **burning** | 11 | 1,564.45 | 8.206841 | 🟢 medium — moderately distinctive |
| 1041 | **nevertheless** | 12 | 1,562.53 | 7.513694 | 🟢 medium — moderately distinctive |
| 1042 | **stream** | 12 | 1,562.53 | 7.513694 | 🟢 medium — moderately distinctive |
| 1043 | **efforts** | 17 | 1,560.19 | 5.29585 | 🟢 medium — moderately distinctive |
| 1044 | **debts** | 14 | 1,556.41 | 6.415081 | 🟢 medium — moderately distinctive |
| 1045 | **depth** | 13 | 1,551.12 | 6.885085 | 🟢 medium — moderately distinctive |
| 1046 | **strength** | 15 | 1,544.73 | 5.942477 | 🟢 medium — moderately distinctive |
| 1047 | **invited** | 13 | 1,543.74 | 6.852295 | 🟢 medium — moderately distinctive |
| 1048 | **village** | 10 | 1,542.35 | 8.899988 | 🟢 medium — moderately distinctive |
| 1049 | **examples** | 10 | 1,542.35 | 8.899988 | 🟢 medium — moderately distinctive |
| 1050 | **transformed** | 10 | 1,542.35 | 8.899988 | 🟢 medium — moderately distinctive |
| 1051 | **object** | 11 | 1,542.00 | 8.089058 | 🟢 medium — moderately distinctive |
| 1052 | **created** | 14 | 1,541.70 | 6.354457 | 🟢 medium — moderately distinctive |
| 1053 | **constant** | 12 | 1,538.04 | 7.395911 | 🟢 medium — moderately distinctive |
| 1054 | **remain** | 19 | 1,533.94 | 4.658661 | 🟢 medium — moderately distinctive |
| 1055 | **fell** | 22 | 1,529.42 | 4.01152 | 🟢 medium — moderately distinctive |
| 1056 | **foot** | 12 | 1,526.79 | 7.341843 | 🟢 medium — moderately distinctive |
| 1057 | **starting** | 15 | 1,512.99 | 5.820374 | 🟢 medium — moderately distinctive |
| 1058 | **takes** | 15 | 1,510.02 | 5.808946 | 🟢 medium — moderately distinctive |
| 1059 | **examine** | 12 | 1,505.98 | 7.24176 | 🟢 medium — moderately distinctive |
| 1060 | **involved** | 16 | 1,504.64 | 5.42647 | 🟢 medium — moderately distinctive |
| 1061 | **vital** | 13 | 1,503.88 | 6.675364 | 🟢 medium — moderately distinctive |
| 1062 | **bow** | 11 | 1,503.75 | 7.888387 | 🟢 medium — moderately distinctive |
| 1063 | **continually** | 10 | 1,503.68 | 8.676844 | 🟢 medium — moderately distinctive |
| 1064 | **treat** | 10 | 1,503.68 | 8.676844 | 🟢 medium — moderately distinctive |
| 1065 | **attitudes** | 10 | 1,503.68 | 8.676844 | 🟢 medium — moderately distinctive |
| 1066 | **phenomena** | 9 | 1,496.23 | 9.593135 | 🟢 medium — moderately distinctive |
| 1067 | **roots** | 9 | 1,496.23 | 9.593135 | 🟢 medium — moderately distinctive |
| 1068 | **deaf** | 9 | 1,496.23 | 9.593135 | 🟢 medium — moderately distinctive |
| 1069 | **beasts** | 9 | 1,496.23 | 9.593135 | 🟢 medium — moderately distinctive |
| 1070 | **journey** | 9 | 1,496.23 | 9.593135 | 🟢 medium — moderately distinctive |
| 1071 | **skilled** | 9 | 1,496.23 | 9.593135 | 🟢 medium — moderately distinctive |
| 1072 | **servants** | 9 | 1,496.23 | 9.593135 | 🟢 medium — moderately distinctive |
| 1073 | **caring** | 9 | 1,496.23 | 9.593135 | 🟢 medium — moderately distinctive |
| 1074 | **walking** | 9 | 1,496.23 | 9.593135 | 🟢 medium — moderately distinctive |
| 1075 | **retribution** | 9 | 1,496.23 | 9.593135 | 🟢 medium — moderately distinctive |
| 1076 | **auspicious** | 9 | 1,496.23 | 9.593135 | 🟢 medium — moderately distinctive |
| 1077 | **loving** | 9 | 1,496.23 | 9.593135 | 🟢 medium — moderately distinctive |
| 1078 | **hate** | 9 | 1,496.23 | 9.593135 | 🟢 medium — moderately distinctive |
| 1079 | **vidyadharas** | 9 | 1,495.74 | 9.59 | 🟢 medium — moderately distinctive |
| 1080 | **aspiration** | 9 | 1,495.74 | 9.59 | 🟢 medium — moderately distinctive |
| 1081 | **distracted** | 9 | 1,495.74 | 9.59 | 🟢 medium — moderately distinctive |
| 1082 | **yak** | 9 | 1,495.74 | 9.59 | 🟢 medium — moderately distinctive |
| 1083 | **meritorious** | 9 | 1,495.74 | 9.59 | 🟢 medium — moderately distinctive |
| 1084 | **doctor** | 9 | 1,495.74 | 9.59 | 🟢 medium — moderately distinctive |
| 1085 | **terrifying** | 9 | 1,495.74 | 9.59 | 🟢 medium — moderately distinctive |
| 1086 | **hunters** | 9 | 1,495.74 | 9.59 | 🟢 medium — moderately distinctive |
| 1087 | **thirty-two** | 9 | 1,495.74 | 9.59 | 🟢 medium — moderately distinctive |
| 1088 | **masters** | 9 | 1,495.74 | 9.59 | 🟢 medium — moderately distinctive |
| 1089 | **jambudvipa** | 9 | 1,495.74 | 9.59 | 🟢 medium — moderately distinctive |
| 1090 | **detsen** | 9 | 1,495.74 | 9.59 | 🟢 medium — moderately distinctive |
| 1091 | **deed** | 9 | 1,495.74 | 9.59 | 🟢 medium — moderately distinctive |
| 1092 | **doctrines** | 9 | 1,495.74 | 9.59 | 🟢 medium — moderately distinctive |
| 1093 | **traveller** | 9 | 1,495.74 | 9.59 | 🟢 medium — moderately distinctive |
| 1094 | **tions** | 9 | 1,495.74 | 9.59 | 🟢 medium — moderately distinctive |
| 1095 | **pleasures** | 9 | 1,495.74 | 9.59 | 🟢 medium — moderately distinctive |
| 1096 | **robes** | 9 | 1,495.74 | 9.59 | 🟢 medium — moderately distinctive |
| 1097 | **doesn** | 9 | 1,495.74 | 9.59 | 🟢 medium — moderately distinctive |
| 1098 | **remorse** | 9 | 1,495.74 | 9.59 | 🟢 medium — moderately distinctive |
| 1099 | **holy** | 9 | 1,495.74 | 9.59 | 🟢 medium — moderately distinctive |
| 1100 | **celestial** | 9 | 1,495.74 | 9.59 | 🟢 medium — moderately distinctive |
| 1101 | **lhasa** | 9 | 1,495.74 | 9.59 | 🟢 medium — moderately distinctive |
| 1102 | **corpse** | 9 | 1,495.74 | 9.59 | 🟢 medium — moderately distinctive |
| 1103 | **bitch** | 9 | 1,495.74 | 9.59 | 🟢 medium — moderately distinctive |
| 1104 | **thangpa** | 9 | 1,495.74 | 9.59 | 🟢 medium — moderately distinctive |
| 1105 | **solitary** | 9 | 1,495.74 | 9.59 | 🟢 medium — moderately distinctive |
| 1106 | **sariputra** | 9 | 1,495.74 | 9.59 | 🟢 medium — moderately distinctive |
| 1107 | **virtuous** | 9 | 1,495.74 | 9.59 | 🟢 medium — moderately distinctive |
| 1108 | **horses** | 9 | 1,495.74 | 9.59 | 🟢 medium — moderately distinctive |
| 1109 | **begging** | 9 | 1,495.74 | 9.59 | 🟢 medium — moderately distinctive |
| 1110 | **immaculate** | 9 | 1,495.74 | 9.59 | 🟢 medium — moderately distinctive |
| 1111 | **caste** | 9 | 1,495.74 | 9.59 | 🟢 medium — moderately distinctive |
| 1112 | **entrust** | 9 | 1,495.74 | 9.59 | 🟢 medium — moderately distinctive |
| 1113 | **throat** | 9 | 1,495.74 | 9.59 | 🟢 medium — moderately distinctive |
| 1114 | **visualized** | 9 | 1,495.74 | 9.59 | 🟢 medium — moderately distinctive |
| 1115 | **princess** | 9 | 1,495.74 | 9.59 | 🟢 medium — moderately distinctive |
| 1116 | **breaches** | 9 | 1,495.74 | 9.59 | 🟢 medium — moderately distinctive |
| 1117 | **manifestation** | 9 | 1,495.74 | 9.59 | 🟢 medium — moderately distinctive |
| 1118 | **visualizing** | 9 | 1,495.74 | 9.59 | 🟢 medium — moderately distinctive |
| 1119 | **bhagavan** | 9 | 1,495.74 | 9.59 | 🟢 medium — moderately distinctive |
| 1120 | **immediate** | 15 | 1,492.87 | 5.742988 | 🟢 medium — moderately distinctive |
| 1121 | **greater** | 16 | 1,485.94 | 5.359029 | 🟢 medium — moderately distinctive |
| 1122 | **brothers** | 15 | 1,484.71 | 5.711571 | 🟢 medium — moderately distinctive |
| 1123 | **necessary** | 16 | 1,483.93 | 5.351808 | 🟢 medium — moderately distinctive |
| 1124 | **representing** | 14 | 1,479.15 | 6.096628 | 🟢 medium — moderately distinctive |
| 1125 | **foundation** | 12 | 1,478.21 | 7.108229 | 🟢 medium — moderately distinctive |
| 1126 | **totally** | 12 | 1,478.21 | 7.108229 | 🟢 medium — moderately distinctive |
| 1127 | **learning** | 10 | 1,472.09 | 8.494523 | 🟢 medium — moderately distinctive |
| 1128 | **green** | 12 | 1,469.72 | 7.067407 | 🟢 medium — moderately distinctive |
| 1129 | **satisfied** | 13 | 1,464.84 | 6.502093 | 🟢 medium — moderately distinctive |
| 1130 | **prevent** | 15 | 1,461.64 | 5.622843 | 🟢 medium — moderately distinctive |
| 1131 | **equally** | 12 | 1,461.57 | 7.028186 | 🟢 medium — moderately distinctive |
| 1132 | **golden** | 12 | 1,461.57 | 7.028186 | 🟢 medium — moderately distinctive |
| 1133 | **pass** | 12 | 1,461.57 | 7.028186 | 🟢 medium — moderately distinctive |
| 1134 | **trust** | 17 | 1,460.78 | 4.958406 | 🟢 medium — moderately distinctive |
| 1135 | **possible** | 19 | 1,459.99 | 4.43408 | 🟢 medium — moderately distinctive |
| 1136 | **seat** | 11 | 1,457.78 | 7.647225 | 🟢 medium — moderately distinctive |
| 1137 | **length** | 11 | 1,457.78 | 7.647225 | 🟢 medium — moderately distinctive |
| 1138 | **gives** | 13 | 1,454.83 | 6.457641 | 🟢 medium — moderately distinctive |
| 1139 | **ill** | 12 | 1,446.16 | 6.954078 | 🟢 medium — moderately distinctive |
| 1140 | **disease** | 12 | 1,446.16 | 6.954078 | 🟢 medium — moderately distinctive |
| 1141 | **lie** | 10 | 1,445.37 | 8.340372 | 🟢 medium — moderately distinctive |
| 1142 | **beauty** | 10 | 1,445.37 | 8.340372 | 🟢 medium — moderately distinctive |
| 1143 | **crushed** | 10 | 1,445.37 | 8.340372 | 🟢 medium — moderately distinctive |
| 1144 | **shadow** | 10 | 1,445.37 | 8.340372 | 🟢 medium — moderately distinctive |
| 1145 | **exactly** | 11 | 1,444.62 | 7.578232 | 🟢 medium — moderately distinctive |
| 1146 | **ago** | 19 | 1,437.15 | 4.364704 | 🟢 medium — moderately distinctive |
| 1147 | **apply** | 13 | 1,436.04 | 6.374259 | 🟢 medium — moderately distinctive |
| 1148 | **poured** | 9 | 1,432.99 | 9.18767 | 🟢 medium — moderately distinctive |
| 1149 | **flies** | 9 | 1,432.99 | 9.18767 | 🟢 medium — moderately distinctive |
| 1150 | **stories** | 9 | 1,432.99 | 9.18767 | 🟢 medium — moderately distinctive |
| 1151 | **companion** | 9 | 1,432.99 | 9.18767 | 🟢 medium — moderately distinctive |
| 1152 | **substances** | 9 | 1,432.99 | 9.18767 | 🟢 medium — moderately distinctive |
| 1153 | **channel** | 11 | 1,432.32 | 7.513694 | 🟢 medium — moderately distinctive |
| 1154 | **advantage** | 13 | 1,431.58 | 6.354457 | 🟢 medium — moderately distinctive |
| 1155 | **arisen** | 10 | 1,422.23 | 8.206841 | 🟢 medium — moderately distinctive |
| 1156 | **strive** | 10 | 1,422.23 | 8.206841 | 🟢 medium — moderately distinctive |
| 1157 | **transmission** | 11 | 1,420.76 | 7.453069 | 🟢 medium — moderately distinctive |
| 1158 | **arising** | 11 | 1,409.87 | 7.395911 | 🟢 medium — moderately distinctive |
| 1159 | **today** | 24 | 1,407.69 | 3.384545 | 🟢 medium — moderately distinctive |
| 1160 | **carried** | 13 | 1,402.60 | 6.225839 | 🟢 medium — moderately distinctive |
| 1161 | **sight** | 11 | 1,399.56 | 7.341843 | 🟢 medium — moderately distinctive |
| 1162 | **established** | 13 | 1,394.97 | 6.191938 | 🟢 medium — moderately distinctive |
| 1163 | **especially** | 14 | 1,390.78 | 5.732405 | 🟢 medium — moderately distinctive |
| 1164 | **faithful** | 9 | 1,388.12 | 8.899988 | 🟢 medium — moderately distinctive |
| 1165 | **clouds** | 9 | 1,388.12 | 8.899988 | 🟢 medium — moderately distinctive |
| 1166 | **touching** | 9 | 1,388.12 | 8.899988 | 🟢 medium — moderately distinctive |
| 1167 | **representations** | 9 | 1,388.12 | 8.899988 | 🟢 medium — moderately distinctive |
| 1168 | **peaceful** | 9 | 1,388.12 | 8.899988 | 🟢 medium — moderately distinctive |
| 1169 | **conviction** | 9 | 1,388.12 | 8.899988 | 🟢 medium — moderately distinctive |
| 1170 | **arises** | 9 | 1,388.12 | 8.899988 | 🟢 medium — moderately distinctive |
| 1171 | **highest** | 13 | 1,383.98 | 6.143148 | 🟢 medium — moderately distinctive |
| 1172 | **driven** | 10 | 1,383.56 | 7.983697 | 🟢 medium — moderately distinctive |
| 1173 | **call** | 15 | 1,382.00 | 5.316469 | 🟢 medium — moderately distinctive |
| 1174 | **apart** | 11 | 1,371.61 | 7.19524 | 🟢 medium — moderately distinctive |
| 1175 | **comfortable** | 10 | 1,367.04 | 7.888387 | 🟢 medium — moderately distinctive |
| 1176 | **described** | 13 | 1,366.77 | 6.066775 | 🟢 medium — moderately distinctive |
| 1177 | **outside** | 14 | 1,355.21 | 5.585802 | 🟢 medium — moderately distinctive |
| 1178 | **accept** | 14 | 1,355.21 | 5.585802 | 🟢 medium — moderately distinctive |
| 1179 | **served** | 11 | 1,355.03 | 7.108229 | 🟢 medium — moderately distinctive |
| 1180 | **show** | 17 | 1,354.99 | 4.599307 | 🟢 medium — moderately distinctive |
| 1181 | **swept** | 9 | 1,353.31 | 8.676844 | 🟢 medium — moderately distinctive |
| 1182 | **women** | 9 | 1,353.31 | 8.676844 | 🟢 medium — moderately distinctive |
| 1183 | **appearing** | 9 | 1,353.31 | 8.676844 | 🟢 medium — moderately distinctive |
| 1184 | **individual** | 12 | 1,347.49 | 6.47962 | 🟢 medium — moderately distinctive |
| 1185 | **merchants** | 11 | 1,347.25 | 7.067407 | 🟢 medium — moderately distinctive |
| 1186 | **needs** | 14 | 1,344.43 | 5.54135 | 🟢 medium — moderately distinctive |
| 1187 | **violations** | 11 | 1,339.77 | 7.028186 | 🟢 medium — moderately distinctive |
| 1188 | **caused** | 15 | 1,338.85 | 5.150484 | 🟢 medium — moderately distinctive |
| 1189 | **yellow** | 10 | 1,338.09 | 7.721333 | 🟢 medium — moderately distinctive |
| 1190 | **degenerate** | 8 | 1,329.98 | 9.593135 | 🟢 medium — moderately distinctive |
| 1191 | **criticize** | 8 | 1,329.98 | 9.593135 | 🟢 medium — moderately distinctive |
| 1192 | **sisters** | 8 | 1,329.98 | 9.593135 | 🟢 medium — moderately distinctive |
| 1193 | **virtue** | 8 | 1,329.98 | 9.593135 | 🟢 medium — moderately distinctive |
| 1194 | **wander** | 8 | 1,329.98 | 9.593135 | 🟢 medium — moderately distinctive |
| 1195 | **burnt** | 8 | 1,329.98 | 9.593135 | 🟢 medium — moderately distinctive |
| 1196 | **ate** | 8 | 1,329.98 | 9.593135 | 🟢 medium — moderately distinctive |
| 1197 | **flower** | 8 | 1,329.98 | 9.593135 | 🟢 medium — moderately distinctive |
| 1198 | **worthless** | 8 | 1,329.98 | 9.593135 | 🟢 medium — moderately distinctive |
| 1199 | **beating** | 8 | 1,329.98 | 9.593135 | 🟢 medium — moderately distinctive |
| 1200 | **buddhafields** | 8 | 1,329.54 | 9.59 | 🟢 medium — moderately distinctive |
| 1201 | **yidam** | 8 | 1,329.54 | 9.59 | 🟢 medium — moderately distinctive |
| 1202 | **believing** | 8 | 1,329.54 | 9.59 | 🟢 medium — moderately distinctive |
| 1203 | **senses** | 8 | 1,329.54 | 9.59 | 🟢 medium — moderately distinctive |
| 1204 | **turns** | 8 | 1,329.54 | 9.59 | 🟢 medium — moderately distinctive |
| 1205 | **henchmen** | 8 | 1,329.54 | 9.59 | 🟢 medium — moderately distinctive |
| 1206 | **tion** | 8 | 1,329.54 | 9.59 | 🟢 medium — moderately distinctive |
| 1207 | **behave** | 8 | 1,329.54 | 9.59 | 🟢 medium — moderately distinctive |
| 1208 | **translator** | 8 | 1,329.54 | 9.59 | 🟢 medium — moderately distinctive |
| 1209 | **trisong** | 8 | 1,329.54 | 9.59 | 🟢 medium — moderately distinctive |
| 1210 | **pratyekabuddhas** | 8 | 1,329.54 | 9.59 | 🟢 medium — moderately distinctive |
| 1211 | **scriptures** | 8 | 1,329.54 | 9.59 | 🟢 medium — moderately distinctive |
| 1212 | **eighteen** | 8 | 1,329.54 | 9.59 | 🟢 medium — moderately distinctive |
| 1213 | **solitude** | 8 | 1,329.54 | 9.59 | 🟢 medium — moderately distinctive |
| 1214 | **cosmos** | 8 | 1,329.54 | 9.59 | 🟢 medium — moderately distinctive |
| 1215 | **endlessly** | 8 | 1,329.54 | 9.59 | 🟢 medium — moderately distinctive |
| 1216 | **burn** | 8 | 1,329.54 | 9.59 | 🟢 medium — moderately distinctive |
| 1217 | **heavens** | 8 | 1,329.54 | 9.59 | 🟢 medium — moderately distinctive |
| 1218 | **sentient** | 8 | 1,329.54 | 9.59 | 🟢 medium — moderately distinctive |
| 1219 | **maitreya** | 8 | 1,329.54 | 9.59 | 🟢 medium — moderately distinctive |
| 1220 | **sorrow** | 8 | 1,329.54 | 9.59 | 🟢 medium — moderately distinctive |
| 1221 | **piles** | 8 | 1,329.54 | 9.59 | 🟢 medium — moderately distinctive |
| 1222 | **blessed** | 8 | 1,329.54 | 9.59 | 🟢 medium — moderately distinctive |
| 1223 | **maudgalyayana** | 8 | 1,329.54 | 9.59 | 🟢 medium — moderately distinctive |
| 1224 | **samsaric** | 8 | 1,329.54 | 9.59 | 🟢 medium — moderately distinctive |
| 1225 | **ripened** | 8 | 1,329.54 | 9.59 | 🟢 medium — moderately distinctive |
| 1226 | **tiniest** | 8 | 1,329.54 | 9.59 | 🟢 medium — moderately distinctive |
| 1227 | **didn** | 8 | 1,329.54 | 9.59 | 🟢 medium — moderately distinctive |
| 1228 | **mouthful** | 8 | 1,329.54 | 9.59 | 🟢 medium — moderately distinctive |
| 1229 | **tsampa** | 8 | 1,329.54 | 9.59 | 🟢 medium — moderately distinctive |
| 1230 | **langri** | 8 | 1,329.54 | 9.59 | 🟢 medium — moderately distinctive |
| 1231 | **covetousness** | 8 | 1,329.54 | 9.59 | 🟢 medium — moderately distinctive |
| 1232 | **silken** | 8 | 1,329.54 | 9.59 | 🟢 medium — moderately distinctive |
| 1233 | **hermitage** | 8 | 1,329.54 | 9.59 | 🟢 medium — moderately distinctive |
| 1234 | **guides** | 8 | 1,329.54 | 9.59 | 🟢 medium — moderately distinctive |
| 1235 | **inseparable** | 8 | 1,329.54 | 9.59 | 🟢 medium — moderately distinctive |
| 1236 | **prajnaparamita** | 8 | 1,329.54 | 9.59 | 🟢 medium — moderately distinctive |
| 1237 | **tathagata** | 8 | 1,329.54 | 9.59 | 🟢 medium — moderately distinctive |
| 1238 | **padma** | 8 | 1,329.54 | 9.59 | 🟢 medium — moderately distinctive |
| 1239 | **chekawa** | 8 | 1,329.54 | 9.59 | 🟢 medium — moderately distinctive |
| 1240 | **traditions** | 8 | 1,329.54 | 9.59 | 🟢 medium — moderately distinctive |
| 1241 | **syllables** | 8 | 1,329.54 | 9.59 | 🟢 medium — moderately distinctive |
| 1242 | **manjusrimitra** | 8 | 1,329.54 | 9.59 | 🟢 medium — moderately distinctive |
| 1243 | **strong** | 17 | 1,328.27 | 4.50863 | 🟢 medium — moderately distinctive |
| 1244 | **knows** | 10 | 1,325.25 | 7.647225 | 🟢 medium — moderately distinctive |
| 1245 | **illness** | 9 | 1,324.88 | 8.494523 | 🟢 medium — moderately distinctive |
| 1246 | **lands** | 9 | 1,324.88 | 8.494523 | 🟢 medium — moderately distinctive |
| 1247 | **baby** | 9 | 1,324.88 | 8.494523 | 🟢 medium — moderately distinctive |
| 1248 | **posture** | 9 | 1,324.88 | 8.494523 | 🟢 medium — moderately distinctive |
| 1249 | **obstacle** | 9 | 1,324.88 | 8.494523 | 🟢 medium — moderately distinctive |
| 1250 | **evening** | 10 | 1,313.29 | 7.578232 | 🟢 medium — moderately distinctive |
| 1251 | **return** | 15 | 1,311.31 | 5.044535 | 🟢 medium — moderately distinctive |
| 1252 | **lines** | 13 | 1,306.14 | 5.797646 | 🟢 medium — moderately distinctive |
| 1253 | **subject** | 17 | 1,305.47 | 4.43121 | 🟢 medium — moderately distinctive |
| 1254 | **standing** | 10 | 1,302.11 | 7.513694 | 🟢 medium — moderately distinctive |
| 1255 | **dry** | 12 | 1,302.01 | 6.260931 | 🟢 medium — moderately distinctive |
| 1256 | **lacking** | 9 | 1,300.83 | 8.340372 | 🟢 medium — moderately distinctive |
| 1257 | **colour** | 9 | 1,300.83 | 8.340372 | 🟢 medium — moderately distinctive |
| 1258 | **destroyed** | 11 | 1,300.19 | 6.820546 | 🟢 medium — moderately distinctive |
| 1259 | **method** | 11 | 1,300.19 | 6.820546 | 🟢 medium — moderately distinctive |
| 1260 | **grain** | 16 | 1,297.79 | 4.68048 | 🟢 medium — moderately distinctive |
| 1261 | **named** | 13 | 1,293.82 | 5.742988 | 🟢 medium — moderately distinctive |
| 1262 | **performed** | 10 | 1,291.60 | 7.453069 | 🟢 medium — moderately distinctive |
| 1263 | **finding** | 11 | 1,283.10 | 6.730934 | 🟢 medium — moderately distinctive |
| 1264 | **explain** | 10 | 1,281.70 | 7.395911 | 🟢 medium — moderately distinctive |
| 1265 | **forest** | 10 | 1,281.70 | 7.395911 | 🟢 medium — moderately distinctive |
| 1266 | **bigger** | 10 | 1,281.70 | 7.395911 | 🟢 medium — moderately distinctive |
| 1267 | **harming** | 9 | 1,280.01 | 8.206841 | 🟢 medium — moderately distinctive |
| 1268 | **thrown** | 9 | 1,280.01 | 8.206841 | 🟢 medium — moderately distinctive |
| 1269 | **disappear** | 9 | 1,280.01 | 8.206841 | 🟢 medium — moderately distinctive |
| 1270 | **sitting** | 9 | 1,280.01 | 8.206841 | 🟢 medium — moderately distinctive |
| 1271 | **skill** | 8 | 1,273.77 | 9.18767 | 🟢 medium — moderately distinctive |
| 1272 | **arrow** | 8 | 1,273.77 | 9.18767 | 🟢 medium — moderately distinctive |
| 1273 | **trials** | 8 | 1,273.77 | 9.18767 | 🟢 medium — moderately distinctive |
| 1274 | **taste** | 8 | 1,273.77 | 9.18767 | 🟢 medium — moderately distinctive |
| 1275 | **inspire** | 8 | 1,273.77 | 9.18767 | 🟢 medium — moderately distinctive |
| 1276 | **nowhere** | 8 | 1,273.77 | 9.18767 | 🟢 medium — moderately distinctive |
| 1277 | **illusion** | 8 | 1,273.77 | 9.18767 | 🟢 medium — moderately distinctive |
| 1278 | **butcher** | 8 | 1,273.77 | 9.18767 | 🟢 medium — moderately distinctive |
| 1279 | **tiny** | 8 | 1,273.77 | 9.18767 | 🟢 medium — moderately distinctive |
| 1280 | **tongue** | 8 | 1,273.77 | 9.18767 | 🟢 medium — moderately distinctive |
| 1281 | **unpleasant** | 8 | 1,273.77 | 9.18767 | 🟢 medium — moderately distinctive |
| 1282 | **fingers** | 8 | 1,273.77 | 9.18767 | 🟢 medium — moderately distinctive |
| 1283 | **basis** | 16 | 1,270.62 | 4.5825 | 🟢 medium — moderately distinctive |
| 1284 | **hope** | 13 | 1,266.76 | 5.622843 | 🟢 medium — moderately distinctive |
| 1285 | **manner** | 10 | 1,263.44 | 7.29055 | 🟢 medium — moderately distinctive |
| 1286 | **turning** | 11 | 1,262.48 | 6.622721 | 🟢 medium — moderately distinctive |
| 1287 | **repeat** | 9 | 1,261.64 | 8.089058 | 🟢 medium — moderately distinctive |
| 1288 | **energy** | 16 | 1,256.22 | 4.53054 | 🟢 medium — moderately distinctive |
| 1289 | **east** | 14 | 1,251.03 | 5.156384 | 🟢 medium — moderately distinctive |
| 1290 | **mistake** | 9 | 1,245.20 | 7.983697 | 🟢 medium — moderately distinctive |
| 1291 | **simple** | 9 | 1,245.20 | 7.983697 | 🟢 medium — moderately distinctive |
| 1292 | **slip** | 9 | 1,245.20 | 7.983697 | 🟢 medium — moderately distinctive |
| 1293 | **gesture** | 9 | 1,245.20 | 7.983697 | 🟢 medium — moderately distinctive |
| 1294 | **position** | 15 | 1,244.92 | 4.789114 | 🟢 medium — moderately distinctive |
| 1295 | **meet** | 15 | 1,244.92 | 4.789114 | 🟢 medium — moderately distinctive |
| 1296 | **kept** | 11 | 1,239.48 | 6.502093 | 🟢 medium — moderately distinctive |
| 1297 | **covered** | 11 | 1,239.48 | 6.502093 | 🟢 medium — moderately distinctive |
| 1298 | **separate** | 12 | 1,238.50 | 5.955549 | 🟢 medium — moderately distinctive |
| 1299 | **loose** | 8 | 1,233.88 | 8.899988 | 🟢 medium — moderately distinctive |
| 1300 | **ceremonies** | 8 | 1,233.88 | 8.899988 | 🟢 medium — moderately distinctive |
| 1301 | **whatsoever** | 8 | 1,233.88 | 8.899988 | 🟢 medium — moderately distinctive |
| 1302 | **attributes** | 8 | 1,233.88 | 8.899988 | 🟢 medium — moderately distinctive |
| 1303 | **twenty** | 8 | 1,233.88 | 8.899988 | 🟢 medium — moderately distinctive |
| 1304 | **committing** | 8 | 1,233.88 | 8.899988 | 🟢 medium — moderately distinctive |
| 1305 | **tooth** | 8 | 1,233.88 | 8.899988 | 🟢 medium — moderately distinctive |
| 1306 | **reflecting** | 12 | 1,233.10 | 5.929574 | 🟢 medium — moderately distinctive |
| 1307 | **close** | 16 | 1,231.87 | 4.442738 | 🟢 medium — moderately distinctive |
| 1308 | **sent** | 12 | 1,230.45 | 5.916835 | 🟢 medium — moderately distinctive |
| 1309 | **applying** | 9 | 1,230.34 | 7.888387 | 🟢 medium — moderately distinctive |
| 1310 | **families** | 9 | 1,230.34 | 7.888387 | 🟢 medium — moderately distinctive |
| 1311 | **less** | 16 | 1,227.88 | 4.428349 | 🟢 medium — moderately distinctive |
| 1312 | **hopes** | 12 | 1,222.70 | 5.879563 | 🟢 medium — moderately distinctive |
| 1313 | **gone** | 10 | 1,217.97 | 7.028186 | 🟢 medium — moderately distinctive |
| 1314 | **felt** | 11 | 1,207.64 | 6.335039 | 🟢 medium — moderately distinctive |
| 1315 | **sort** | 10 | 1,205.13 | 6.954078 | 🟢 medium — moderately distinctive |
| 1316 | **sole** | 9 | 1,204.28 | 7.721333 | 🟢 medium — moderately distinctive |
| 1317 | **speaking** | 12 | 1,203.34 | 5.786473 | 🟢 medium — moderately distinctive |
| 1318 | **seal** | 8 | 1,202.95 | 8.676844 | 🟢 medium — moderately distinctive |
| 1319 | **behaviour** | 8 | 1,202.95 | 8.676844 | 🟢 medium — moderately distinctive |
| 1320 | **peace** | 8 | 1,202.95 | 8.676844 | 🟢 medium — moderately distinctive |
| 1321 | **link** | 10 | 1,199.05 | 6.918987 | 🟢 medium — moderately distinctive |
| 1322 | **includes** | 18 | 1,193.10 | 3.824814 | 🟢 medium — moderately distinctive |
| 1323 | **proper** | 9 | 1,192.73 | 7.647225 | 🟢 medium — moderately distinctive |
| 1324 | **nobody** | 9 | 1,192.73 | 7.647225 | 🟢 medium — moderately distinctive |
| 1325 | **cutting** | 12 | 1,192.10 | 5.732405 | 🟢 medium — moderately distinctive |
| 1326 | **branches** | 10 | 1,187.49 | 6.852295 | 🟢 medium — moderately distinctive |
| 1327 | **containing** | 10 | 1,181.99 | 6.820546 | 🟢 medium — moderately distinctive |
| 1328 | **broken** | 10 | 1,181.99 | 6.820546 | 🟢 medium — moderately distinctive |
| 1329 | **explaining** | 9 | 1,181.96 | 7.578232 | 🟢 medium — moderately distinctive |
| 1330 | **difficulties** | 11 | 1,180.36 | 6.191938 | 🟢 medium — moderately distinctive |
| 1331 | **trace** | 8 | 1,177.67 | 8.494523 | 🟢 medium — moderately distinctive |
| 1332 | **helps** | 8 | 1,177.67 | 8.494523 | 🟢 medium — moderately distinctive |
| 1333 | **union** | 15 | 1,176.88 | 4.527381 | 🟢 medium — moderately distinctive |
| 1334 | **wood** | 10 | 1,176.66 | 6.789775 | 🟢 medium — moderately distinctive |
| 1335 | **grow** | 12 | 1,175.28 | 5.651553 | 🟢 medium — moderately distinctive |
| 1336 | **serious** | 12 | 1,173.28 | 5.641891 | 🟢 medium — moderately distinctive |
| 1337 | **surface** | 9 | 1,171.90 | 7.513694 | 🟢 medium — moderately distinctive |
| 1338 | **bringing** | 11 | 1,171.06 | 6.143148 | 🟢 medium — moderately distinctive |
| 1339 | **carry** | 11 | 1,168.05 | 6.127399 | 🟢 medium — moderately distinctive |
| 1340 | **glad** | 7 | 1,163.73 | 9.593135 | 🟢 medium — moderately distinctive |
| 1341 | **sad** | 7 | 1,163.73 | 9.593135 | 🟢 medium — moderately distinctive |
| 1342 | **stupid** | 7 | 1,163.73 | 9.593135 | 🟢 medium — moderately distinctive |
| 1343 | **threw** | 7 | 1,163.73 | 9.593135 | 🟢 medium — moderately distinctive |
| 1344 | **riches** | 7 | 1,163.73 | 9.593135 | 🟢 medium — moderately distinctive |
| 1345 | **mouths** | 7 | 1,163.73 | 9.593135 | 🟢 medium — moderately distinctive |
| 1346 | **poisonous** | 7 | 1,163.73 | 9.593135 | 🟢 medium — moderately distinctive |
| 1347 | **beg** | 7 | 1,163.73 | 9.593135 | 🟢 medium — moderately distinctive |
| 1348 | **steal** | 7 | 1,163.73 | 9.593135 | 🟢 medium — moderately distinctive |
| 1349 | **shoots** | 7 | 1,163.73 | 9.593135 | 🟢 medium — moderately distinctive |
| 1350 | **infinity** | 7 | 1,163.73 | 9.593135 | 🟢 medium — moderately distinctive |
| 1351 | **herself** | 7 | 1,163.73 | 9.593135 | 🟢 medium — moderately distinctive |
| 1352 | **discover** | 7 | 1,163.73 | 9.593135 | 🟢 medium — moderately distinctive |
| 1353 | **process** | 12 | 1,163.51 | 5.594934 | 🟢 medium — moderately distinctive |
| 1354 | **avalokitesvara** | 7 | 1,163.35 | 9.59 | 🟢 medium — moderately distinctive |
| 1355 | **longchenpa** | 7 | 1,163.35 | 9.59 | 🟢 medium — moderately distinctive |
| 1356 | **habitual** | 7 | 1,163.35 | 9.59 | 🟢 medium — moderately distinctive |
| 1357 | **dedicating** | 7 | 1,163.35 | 9.59 | 🟢 medium — moderately distinctive |
| 1358 | **padmasambhava** | 7 | 1,163.35 | 9.59 | 🟢 medium — moderately distinctive |
| 1359 | **hungry** | 7 | 1,163.35 | 9.59 | 🟢 medium — moderately distinctive |
| 1360 | **forgetting** | 7 | 1,163.35 | 9.59 | 🟢 medium — moderately distinctive |
| 1361 | **deluded** | 7 | 1,163.35 | 9.59 | 🟢 medium — moderately distinctive |
| 1362 | **layman** | 7 | 1,163.35 | 9.59 | 🟢 medium — moderately distinctive |
| 1363 | **endure** | 7 | 1,163.35 | 9.59 | 🟢 medium — moderately distinctive |
| 1364 | **mastered** | 7 | 1,163.35 | 9.59 | 🟢 medium — moderately distinctive |
| 1365 | **vinaya** | 7 | 1,163.35 | 9.59 | 🟢 medium — moderately distinctive |
| 1366 | **atra** | 7 | 1,163.35 | 9.59 | 🟢 medium — moderately distinctive |
| 1367 | **songtsen** | 7 | 1,163.35 | 9.59 | 🟢 medium — moderately distinctive |
| 1368 | **gampo** | 7 | 1,163.35 | 9.59 | 🟢 medium — moderately distinctive |
| 1369 | **ambrosia** | 7 | 1,163.35 | 9.59 | 🟢 medium — moderately distinctive |
| 1370 | **begged** | 7 | 1,163.35 | 9.59 | 🟢 medium — moderately distinctive |
| 1371 | **everyday** | 7 | 1,163.35 | 9.59 | 🟢 medium — moderately distinctive |
| 1372 | **aroused** | 7 | 1,163.35 | 9.59 | 🟢 medium — moderately distinctive |
| 1373 | **cry** | 7 | 1,163.35 | 9.59 | 🟢 medium — moderately distinctive |
| 1374 | **sravakas** | 7 | 1,163.35 | 9.59 | 🟢 medium — moderately distinctive |
| 1375 | **ornaments** | 7 | 1,163.35 | 9.59 | 🟢 medium — moderately distinctive |
| 1376 | **ancient** | 7 | 1,163.35 | 9.59 | 🟢 medium — moderately distinctive |
| 1377 | **magical** | 7 | 1,163.35 | 9.59 | 🟢 medium — moderately distinctive |
| 1378 | **katyayana** | 7 | 1,163.35 | 9.59 | 🟢 medium — moderately distinctive |
| 1379 | **lap** | 7 | 1,163.35 | 9.59 | 🟢 medium — moderately distinctive |
| 1380 | **husband** | 7 | 1,163.35 | 9.59 | 🟢 medium — moderately distinctive |
| 1381 | **possession** | 7 | 1,163.35 | 9.59 | 🟢 medium — moderately distinctive |
| 1382 | **dear** | 7 | 1,163.35 | 9.59 | 🟢 medium — moderately distinctive |
| 1383 | **beggars** | 7 | 1,163.35 | 9.59 | 🟢 medium — moderately distinctive |
| 1384 | **answered** | 7 | 1,163.35 | 9.59 | 🟢 medium — moderately distinctive |
| 1385 | **crimes** | 7 | 1,163.35 | 9.59 | 🟢 medium — moderately distinctive |
| 1386 | **lips** | 7 | 1,163.35 | 9.59 | 🟢 medium — moderately distinctive |
| 1387 | **pus** | 7 | 1,163.35 | 9.59 | 🟢 medium — moderately distinctive |
| 1388 | **medicinal** | 7 | 1,163.35 | 9.59 | 🟢 medium — moderately distinctive |
| 1389 | **praying** | 7 | 1,163.35 | 9.59 | 🟢 medium — moderately distinctive |
| 1390 | **marvellous** | 7 | 1,163.35 | 9.59 | 🟢 medium — moderately distinctive |
| 1391 | **lhodrak** | 7 | 1,163.35 | 9.59 | 🟢 medium — moderately distinctive |
| 1392 | **lamps** | 7 | 1,163.35 | 9.59 | 🟢 medium — moderately distinctive |
| 1393 | **lita** | 7 | 1,163.35 | 9.59 | 🟢 medium — moderately distinctive |
| 1394 | **vimalamitra** | 7 | 1,163.35 | 9.59 | 🟢 medium — moderately distinctive |
| 1395 | **primordial** | 7 | 1,163.35 | 9.59 | 🟢 medium — moderately distinctive |
| 1396 | **symbolizes** | 7 | 1,163.35 | 9.59 | 🟢 medium — moderately distinctive |
| 1397 | **stupa** | 7 | 1,163.35 | 9.59 | 🟢 medium — moderately distinctive |
| 1398 | **sharawa** | 7 | 1,163.35 | 9.59 | 🟢 medium — moderately distinctive |
| 1399 | **atiyoga** | 7 | 1,163.35 | 9.59 | 🟢 medium — moderately distinctive |
| 1400 | **minor** | 9 | 1,162.44 | 7.453069 | 🟢 medium — moderately distinctive |
| 1401 | **leads** | 9 | 1,162.44 | 7.453069 | 🟢 medium — moderately distinctive |
| 1402 | **change** | 15 | 1,161.75 | 4.469171 | 🟢 medium — moderately distinctive |
| 1403 | **relative** | 10 | 1,156.83 | 6.675364 | 🟢 medium — moderately distinctive |
| 1404 | **male** | 8 | 1,156.30 | 8.340372 | 🟢 medium — moderately distinctive |
| 1405 | **naturally** | 8 | 1,156.30 | 8.340372 | 🟢 medium — moderately distinctive |
| 1406 | **medicine** | 8 | 1,156.30 | 8.340372 | 🟢 medium — moderately distinctive |
| 1407 | **dedicated** | 8 | 1,156.30 | 8.340372 | 🟢 medium — moderately distinctive |
| 1408 | **consists** | 9 | 1,153.53 | 7.395911 | 🟢 medium — moderately distinctive |
| 1409 | **appears** | 11 | 1,150.97 | 6.037787 | 🟢 medium — moderately distinctive |
| 1410 | **conditions** | 14 | 1,148.39 | 4.733323 | 🟢 medium — moderately distinctive |
| 1411 | **convinced** | 10 | 1,147.71 | 6.622721 | 🟢 medium — moderately distinctive |
| 1412 | **nine** | 19 | 1,139.53 | 3.460822 | 🟢 medium — moderately distinctive |
| 1413 | **confusion** | 8 | 1,137.78 | 8.206841 | 🟢 medium — moderately distinctive |
| 1414 | **continent** | 8 | 1,137.78 | 8.206841 | 🟢 medium — moderately distinctive |
| 1415 | **deeply** | 8 | 1,137.78 | 8.206841 | 🟢 medium — moderately distinctive |
| 1416 | **rainbow** | 8 | 1,137.78 | 8.206841 | 🟢 medium — moderately distinctive |
| 1417 | **identical** | 8 | 1,137.78 | 8.206841 | 🟢 medium — moderately distinctive |
| 1418 | **check** | 9 | 1,137.10 | 7.29055 | 🟢 medium — moderately distinctive |
| 1419 | **region** | 11 | 1,135.29 | 5.955549 | 🟢 medium — moderately distinctive |
| 1420 | **seek** | 13 | 1,134.10 | 5.034009 | 🟢 medium — moderately distinctive |
| 1421 | **ability** | 11 | 1,130.34 | 5.929574 | 🟢 medium — moderately distinctive |
| 1422 | **universal** | 9 | 1,129.49 | 7.24176 | 🟢 medium — moderately distinctive |
| 1423 | **summer** | 11 | 1,125.52 | 5.904256 | 🟢 medium — moderately distinctive |
| 1424 | **lost** | 12 | 1,125.28 | 5.411085 | 🟢 medium — moderately distinctive |
| 1425 | **remedy** | 8 | 1,121.46 | 8.089058 | 🟢 medium — moderately distinctive |
| 1426 | **external** | 11 | 1,118.50 | 5.867442 | 🟢 medium — moderately distinctive |
| 1427 | **run** | 11 | 1,116.22 | 5.855466 | 🟢 medium — moderately distinctive |
| 1428 | **mean** | 11 | 1,116.22 | 5.855466 | 🟢 medium — moderately distinctive |
| 1429 | **letting** | 7 | 1,114.54 | 9.18767 | 🟢 medium — moderately distinctive |
| 1430 | **ruin** | 7 | 1,114.54 | 9.18767 | 🟢 medium — moderately distinctive |
| 1431 | **enjoying** | 7 | 1,114.54 | 9.18767 | 🟢 medium — moderately distinctive |
| 1432 | **bears** | 7 | 1,114.54 | 9.18767 | 🟢 medium — moderately distinctive |
| 1433 | **transmitted** | 7 | 1,114.54 | 9.18767 | 🟢 medium — moderately distinctive |
| 1434 | **looks** | 10 | 1,111.72 | 6.415081 | 🟢 medium — moderately distinctive |
| 1435 | **principle** | 12 | 1,109.98 | 5.337522 | 🟢 medium — moderately distinctive |
| 1436 | **trouble** | 9 | 1,108.66 | 7.108229 | 🟢 medium — moderately distinctive |
| 1437 | **detail** | 9 | 1,108.66 | 7.108229 | 🟢 medium — moderately distinctive |
| 1438 | **pulled** | 8 | 1,106.85 | 7.983697 | 🟢 medium — moderately distinctive |
| 1439 | **weak** | 11 | 1,103.06 | 5.786473 | 🟢 medium — moderately distinctive |
| 1440 | **gold** | 13 | 1,096.19 | 4.865747 | 🟢 medium — moderately distinctive |
| 1441 | **symbol** | 8 | 1,093.63 | 7.888387 | 🟢 medium — moderately distinctive |
| 1442 | **success** | 10 | 1,091.31 | 6.297298 | 🟢 medium — moderately distinctive |
| 1443 | **concerns** | 10 | 1,091.31 | 6.297298 | 🟢 medium — moderately distinctive |
| 1444 | **break** | 10 | 1,091.31 | 6.297298 | 🟢 medium — moderately distinctive |
| 1445 | **parts** | 11 | 1,088.79 | 5.711571 | 🟢 medium — moderately distinctive |
| 1446 | **rather** | 12 | 1,087.63 | 5.230037 | 🟢 medium — moderately distinctive |
| 1447 | **building** | 11 | 1,082.98 | 5.681112 | 🟢 medium — moderately distinctive |
| 1448 | **absolutely** | 8 | 1,081.57 | 7.801376 | 🟢 medium — moderately distinctive |
| 1449 | **army** | 8 | 1,081.57 | 7.801376 | 🟢 medium — moderately distinctive |
| 1450 | **sand** | 8 | 1,081.57 | 7.801376 | 🟢 medium — moderately distinctive |
| 1451 | **spark** | 8 | 1,081.57 | 7.801376 | 🟢 medium — moderately distinctive |
| 1452 | **hunter** | 7 | 1,079.65 | 8.899988 | 🟢 medium — moderately distinctive |
| 1453 | **outward** | 7 | 1,079.65 | 8.899988 | 🟢 medium — moderately distinctive |
| 1454 | **travelling** | 7 | 1,079.65 | 8.899988 | 🟢 medium — moderately distinctive |
| 1455 | **opposite** | 7 | 1,079.65 | 8.899988 | 🟢 medium — moderately distinctive |
| 1456 | **refers** | 7 | 1,079.65 | 8.899988 | 🟢 medium — moderately distinctive |
| 1457 | **poverty** | 7 | 1,079.65 | 8.899988 | 🟢 medium — moderately distinctive |
| 1458 | **prey** | 7 | 1,079.65 | 8.899988 | 🟢 medium — moderately distinctive |
| 1459 | **feelings** | 7 | 1,079.65 | 8.899988 | 🟢 medium — moderately distinctive |
| 1460 | **calf** | 7 | 1,079.65 | 8.899988 | 🟢 medium — moderately distinctive |
| 1461 | **expression** | 7 | 1,079.65 | 8.899988 | 🟢 medium — moderately distinctive |
| 1462 | **property** | 11 | 1,075.50 | 5.641891 | 🟢 medium — moderately distinctive |
| 1463 | **difference** | 9 | 1,073.86 | 6.885085 | 🟢 medium — moderately distinctive |
| 1464 | **cross** | 9 | 1,073.86 | 6.885085 | 🟢 medium — moderately distinctive |
| 1465 | **rise** | 17 | 1,070.81 | 3.634711 | 🟢 medium — moderately distinctive |
| 1466 | **develops** | 8 | 1,070.47 | 7.721333 | 🟢 medium — moderately distinctive |
| 1467 | **search** | 8 | 1,060.20 | 7.647225 | 🟢 medium — moderately distinctive |
| 1468 | **money** | 15 | 1,059.46 | 4.075682 | 🟢 medium — moderately distinctive |
| 1469 | **depends** | 9 | 1,058.99 | 6.789775 | 🟢 medium — moderately distinctive |
| 1470 | **gradually** | 9 | 1,054.33 | 6.759922 | 🟢 medium — moderately distinctive |
| 1471 | **talking** | 10 | 1,053.93 | 6.08159 | 🟢 medium — moderately distinctive |
| 1472 | **oral** | 7 | 1,052.58 | 8.676844 | 🟢 medium — moderately distinctive |
| 1473 | **till** | 7 | 1,052.58 | 8.676844 | 🟢 medium — moderately distinctive |
| 1474 | **violent** | 7 | 1,052.58 | 8.676844 | 🟢 medium — moderately distinctive |
| 1475 | **considered** | 11 | 1,051.43 | 5.515598 | 🟢 medium — moderately distinctive |
| 1476 | **pull** | 8 | 1,050.64 | 7.578232 | 🟢 medium — moderately distinctive |
| 1477 | **grains** | 10 | 1,048.83 | 6.052176 | 🟢 medium — moderately distinctive |
| 1478 | **barley** | 10 | 1,048.83 | 6.052176 | 🟢 medium — moderately distinctive |
| 1479 | **purpose** | 9 | 1,045.42 | 6.702763 | 🟢 medium — moderately distinctive |
| 1480 | **fill** | 8 | 1,041.69 | 7.513694 | 🟢 medium — moderately distinctive |
| 1481 | **fields** | 10 | 1,041.46 | 6.009616 | 🟢 medium — moderately distinctive |
| 1482 | **usually** | 9 | 1,041.15 | 6.675364 | 🟢 medium — moderately distinctive |
| 1483 | **drop** | 13 | 1,033.89 | 4.589189 | 🟢 medium — moderately distinctive |
| 1484 | **exist** | 8 | 1,033.28 | 7.453069 | 🟢 medium — moderately distinctive |
| 1485 | **stages** | 8 | 1,033.28 | 7.453069 | 🟢 medium — moderately distinctive |
| 1486 | **prepared** | 11 | 1,032.97 | 5.418748 | 🟢 medium — moderately distinctive |
| 1487 | **receiving** | 9 | 1,032.94 | 6.622721 | 🟢 medium — moderately distinctive |
| 1488 | **experiencing** | 7 | 1,030.46 | 8.494523 | 🟢 medium — moderately distinctive |
| 1489 | **branch** | 9 | 1,028.99 | 6.597403 | 🟢 medium — moderately distinctive |
| 1490 | **previous** | 14 | 1,026.72 | 4.231843 | 🟢 medium — moderately distinctive |
| 1491 | **meal** | 9 | 1,025.13 | 6.57271 | 🟢 medium — moderately distinctive |
| 1492 | **capable** | 8 | 1,017.86 | 7.341843 | 🟢 medium — moderately distinctive |
| 1493 | **solid** | 8 | 1,010.75 | 7.29055 | 🟢 medium — moderately distinctive |
| 1494 | **favourable** | 9 | 1,010.62 | 6.47962 | 🟢 medium — moderately distinctive |
| 1495 | **holds** | 11 | 1,008.25 | 5.28907 | 🟢 medium — moderately distinctive |
| 1496 | **amount** | 13 | 1,008.19 | 4.475141 | 🟢 medium — moderately distinctive |
| 1497 | **request** | 10 | 1,004.72 | 5.797646 | 🟢 medium — moderately distinctive |
| 1498 | **greatest** | 8 | 1,003.99 | 7.24176 | 🟢 medium — moderately distinctive |
| 1499 | **travel** | 8 | 1,003.99 | 7.24176 | 🟢 medium — moderately distinctive |
| 1500 | **represent** | 9 | 1,003.83 | 6.436135 | 🟢 medium — moderately distinctive |
| 1501 | **conclusion** | 8 | 997.54 | 7.19524 | 🟢 medium — moderately distinctive |
| 1502 | **permitted** | 8 | 997.54 | 7.19524 | 🟢 medium — moderately distinctive |
| 1503 | **whoever** | 6 | 997.48 | 9.593135 | 🟢 medium — moderately distinctive |
| 1504 | **famous** | 6 | 997.48 | 9.593135 | 🟢 medium — moderately distinctive |
| 1505 | **distinguish** | 6 | 997.48 | 9.593135 | 🟢 medium — moderately distinctive |
| 1506 | **leagues** | 6 | 997.48 | 9.593135 | 🟢 medium — moderately distinctive |
| 1507 | **unpredictable** | 6 | 997.48 | 9.593135 | 🟢 medium — moderately distinctive |
| 1508 | **naked** | 6 | 997.48 | 9.593135 | 🟢 medium — moderately distinctive |
| 1509 | **shame** | 6 | 997.48 | 9.593135 | 🟢 medium — moderately distinctive |
| 1510 | **agony** | 6 | 997.48 | 9.593135 | 🟢 medium — moderately distinctive |
| 1511 | **trunk** | 6 | 997.48 | 9.593135 | 🟢 medium — moderately distinctive |
| 1512 | **shoulder** | 6 | 997.48 | 9.593135 | 🟢 medium — moderately distinctive |
| 1513 | **multitude** | 6 | 997.48 | 9.593135 | 🟢 medium — moderately distinctive |
| 1514 | **heart-essence** | 6 | 997.16 | 9.59 | 🟢 medium — moderately distinctive |
| 1515 | **inwards** | 6 | 997.16 | 9.59 | 🟢 medium — moderately distinctive |
| 1516 | **twenty-five** | 6 | 997.16 | 9.59 | 🟢 medium — moderately distinctive |
| 1517 | **vajradhara** | 6 | 997.16 | 9.59 | 🟢 medium — moderately distinctive |
| 1518 | **deer** | 6 | 997.16 | 9.59 | 🟢 medium — moderately distinctive |
| 1519 | **smell** | 6 | 997.16 | 9.59 | 🟢 medium — moderately distinctive |
| 1520 | **rope** | 6 | 997.16 | 9.59 | 🟢 medium — moderately distinctive |
| 1521 | **metaphors** | 6 | 997.16 | 9.59 | 🟢 medium — moderately distinctive |
| 1522 | **gratitude** | 6 | 997.16 | 9.59 | 🟢 medium — moderately distinctive |
| 1523 | **inhabitants** | 6 | 997.16 | 9.59 | 🟢 medium — moderately distinctive |
| 1524 | **sunak** | 6 | 997.16 | 9.59 | 🟢 medium — moderately distinctive |
| 1525 | **grasping** | 6 | 997.16 | 9.59 | 🟢 medium — moderately distinctive |
| 1526 | **bodh** | 6 | 997.16 | 9.59 | 🟢 medium — moderately distinctive |
| 1527 | **gaya** | 6 | 997.16 | 9.59 | 🟢 medium — moderately distinctive |
| 1528 | **emanations** | 6 | 997.16 | 9.59 | 🟢 medium — moderately distinctive |
| 1529 | **panditas** | 6 | 997.16 | 9.59 | 🟢 medium — moderately distinctive |
| 1530 | **inexhaustible** | 6 | 997.16 | 9.59 | 🟢 medium — moderately distinctive |
| 1531 | **omniscience** | 6 | 997.16 | 9.59 | 🟢 medium — moderately distinctive |
| 1532 | **ills** | 6 | 997.16 | 9.59 | 🟢 medium — moderately distinctive |
| 1533 | **lamp** | 6 | 997.16 | 9.59 | 🟢 medium — moderately distinctive |
| 1534 | **mighty** | 6 | 997.16 | 9.59 | 🟢 medium — moderately distinctive |
| 1535 | **santideva** | 6 | 997.16 | 9.59 | 🟢 medium — moderately distinctive |
| 1536 | **delusion** | 6 | 997.16 | 9.59 | 🟢 medium — moderately distinctive |
| 1537 | **heavenly** | 6 | 997.16 | 9.59 | 🟢 medium — moderately distinctive |
| 1538 | **meditative** | 6 | 997.16 | 9.59 | 🟢 medium — moderately distinctive |
| 1539 | **oceans** | 6 | 997.16 | 9.59 | 🟢 medium — moderately distinctive |
| 1540 | **ruler** | 6 | 997.16 | 9.59 | 🟢 medium — moderately distinctive |
| 1541 | **bristling** | 6 | 997.16 | 9.59 | 🟢 medium — moderately distinctive |
| 1542 | **arrows** | 6 | 997.16 | 9.59 | 🟢 medium — moderately distinctive |
| 1543 | **possessed** | 6 | 997.16 | 9.59 | 🟢 medium — moderately distinctive |
| 1544 | **mastery** | 6 | 997.16 | 9.59 | 🟢 medium — moderately distinctive |
| 1545 | **prosperous** | 6 | 997.16 | 9.59 | 🟢 medium — moderately distinctive |
| 1546 | **needle** | 6 | 997.16 | 9.59 | 🟢 medium — moderately distinctive |
| 1547 | **quarrels** | 6 | 997.16 | 9.59 | 🟢 medium — moderately distinctive |
| 1548 | **weeping** | 6 | 997.16 | 9.59 | 🟢 medium — moderately distinctive |
| 1549 | **meditated** | 6 | 997.16 | 9.59 | 🟢 medium — moderately distinctive |
| 1550 | **clinging** | 6 | 997.16 | 9.59 | 🟢 medium — moderately distinctive |
| 1551 | **terror** | 6 | 997.16 | 9.59 | 🟢 medium — moderately distinctive |
| 1552 | **worms** | 6 | 997.16 | 9.59 | 🟢 medium — moderately distinctive |
| 1553 | **dogs** | 6 | 997.16 | 9.59 | 🟢 medium — moderately distinctive |
| 1554 | **monastery** | 6 | 997.16 | 9.59 | 🟢 medium — moderately distinctive |
| 1555 | **brahmins** | 6 | 997.16 | 9.59 | 🟢 medium — moderately distinctive |
| 1556 | **particles** | 6 | 997.16 | 9.59 | 🟢 medium — moderately distinctive |
| 1557 | **forehead** | 6 | 997.16 | 9.59 | 🟢 medium — moderately distinctive |
| 1558 | **thorns** | 6 | 997.16 | 9.59 | 🟢 medium — moderately distinctive |
| 1559 | **lala** | 6 | 997.16 | 9.59 | 🟢 medium — moderately distinctive |
| 1560 | **creature** | 6 | 997.16 | 9.59 | 🟢 medium — moderately distinctive |
| 1561 | **benefactors** | 6 | 997.16 | 9.59 | 🟢 medium — moderately distinctive |
| 1562 | **nun** | 6 | 997.16 | 9.59 | 🟢 medium — moderately distinctive |
| 1563 | **pratyekabuddha** | 6 | 997.16 | 9.59 | 🟢 medium — moderately distinctive |
| 1564 | **girl** | 6 | 997.16 | 9.59 | 🟢 medium — moderately distinctive |
| 1565 | **pith-instructions** | 6 | 997.16 | 9.59 | 🟢 medium — moderately distinctive |
| 1566 | **boatman** | 6 | 997.16 | 9.59 | 🟢 medium — moderately distinctive |
| 1567 | **prostrated** | 6 | 997.16 | 9.59 | 🟢 medium — moderately distinctive |
| 1568 | **unsurpassable** | 6 | 997.16 | 9.59 | 🟢 medium — moderately distinctive |
| 1569 | **yogas** | 6 | 997.16 | 9.59 | 🟢 medium — moderately distinctive |
| 1570 | **jealous** | 6 | 997.16 | 9.59 | 🟢 medium — moderately distinctive |
| 1571 | **prayed** | 6 | 997.16 | 9.59 | 🟢 medium — moderately distinctive |
| 1572 | **ngokpa** | 6 | 997.16 | 9.59 | 🟢 medium — moderately distinctive |
| 1573 | **incomparable** | 6 | 997.16 | 9.59 | 🟢 medium — moderately distinctive |
| 1574 | **vajrapani** | 6 | 997.16 | 9.59 | 🟢 medium — moderately distinctive |
| 1575 | **thank** | 6 | 997.16 | 9.59 | 🟢 medium — moderately distinctive |
| 1576 | **ments** | 6 | 997.16 | 9.59 | 🟢 medium — moderately distinctive |
| 1577 | **atriya** | 6 | 997.16 | 9.59 | 🟢 medium — moderately distinctive |
| 1578 | **melts** | 6 | 997.16 | 9.59 | 🟢 medium — moderately distinctive |
| 1579 | **dharmaraksita** | 6 | 997.16 | 9.59 | 🟢 medium — moderately distinctive |
| 1580 | **hard-to-endure** | 6 | 997.16 | 9.59 | 🟢 medium — moderately distinctive |
| 1581 | **zangpo** | 6 | 997.16 | 9.59 | 🟢 medium — moderately distinctive |
| 1582 | **rejoicing** | 6 | 997.16 | 9.59 | 🟢 medium — moderately distinctive |
| 1583 | **takaya** | 6 | 997.16 | 9.59 | 🟢 medium — moderately distinctive |
| 1584 | **hrih** | 6 | 997.16 | 9.59 | 🟢 medium — moderately distinctive |
| 1585 | **plain** | 7 | 995.56 | 8.206841 | 🟢 medium — moderately distinctive |
| 1586 | **altogether** | 7 | 995.56 | 8.206841 | 🟢 medium — moderately distinctive |
| 1587 | **genuine** | 7 | 995.56 | 8.206841 | 🟢 medium — moderately distinctive |
| 1588 | **afterwards** | 7 | 995.56 | 8.206841 | 🟢 medium — moderately distinctive |
| 1589 | **meant** | 9 | 994.18 | 6.374259 | 🟢 medium — moderately distinctive |
| 1590 | **careful** | 8 | 985.47 | 7.108229 | 🟢 medium — moderately distinctive |
| 1591 | **except** | 9 | 982.18 | 6.297298 | 🟢 medium — moderately distinctive |
| 1592 | **avoided** | 7 | 981.27 | 8.089058 | 🟢 medium — moderately distinctive |
| 1593 | **ride** | 7 | 981.27 | 8.089058 | 🟢 medium — moderately distinctive |
| 1594 | **fat** | 7 | 981.27 | 8.089058 | 🟢 medium — moderately distinctive |
| 1595 | **disc** | 7 | 981.27 | 8.089058 | 🟢 medium — moderately distinctive |
| 1596 | **contain** | 8 | 979.82 | 7.067407 | 🟢 medium — moderately distinctive |
| 1597 | **spirit** | 8 | 979.82 | 7.067407 | 🟢 medium — moderately distinctive |
| 1598 | **health** | 10 | 979.40 | 5.651553 | 🟢 medium — moderately distinctive |
| 1599 | **heavy** | 11 | 977.39 | 5.127227 | 🟢 medium — moderately distinctive |
| 1600 | **highly** | 9 | 976.51 | 6.260931 | 🟢 medium — moderately distinctive |
| 1601 | **sound** | 8 | 974.38 | 7.028186 | 🟢 medium — moderately distinctive |
| 1602 | **aside** | 8 | 969.15 | 6.990446 | 🟢 medium — moderately distinctive |
| 1603 | **concentrated** | 8 | 969.15 | 6.990446 | 🟢 medium — moderately distinctive |
| 1604 | **involves** | 8 | 969.15 | 6.990446 | 🟢 medium — moderately distinctive |
| 1605 | **looked** | 8 | 969.15 | 6.990446 | 🟢 medium — moderately distinctive |
| 1606 | **based** | 13 | 968.70 | 4.29983 | 🟢 medium — moderately distinctive |
| 1607 | **grows** | 7 | 968.49 | 7.983697 | 🟢 medium — moderately distinctive |
| 1608 | **bright** | 7 | 968.49 | 7.983697 | 🟢 medium — moderately distinctive |
| 1609 | **sides** | 9 | 965.75 | 6.191938 | 🟢 medium — moderately distinctive |
| 1610 | **accepted** | 10 | 963.35 | 5.558895 | 🟢 medium — moderately distinctive |
| 1611 | **intentions** | 8 | 959.24 | 6.918987 | 🟢 medium — moderately distinctive |
| 1612 | **eye** | 7 | 956.93 | 7.888387 | 🟢 medium — moderately distinctive |
| 1613 | **deepest** | 6 | 955.32 | 9.18767 | 🟢 medium — moderately distinctive |
| 1614 | **abuse** | 6 | 955.32 | 9.18767 | 🟢 medium — moderately distinctive |
| 1615 | **encounter** | 6 | 955.32 | 9.18767 | 🟢 medium — moderately distinctive |
| 1616 | **suppose** | 6 | 955.32 | 9.18767 | 🟢 medium — moderately distinctive |
| 1617 | **transmissions** | 6 | 955.32 | 9.18767 | 🟢 medium — moderately distinctive |
| 1618 | **wise** | 6 | 955.32 | 9.18767 | 🟢 medium — moderately distinctive |
| 1619 | **cow** | 6 | 955.32 | 9.18767 | 🟢 medium — moderately distinctive |
| 1620 | **clarity** | 6 | 955.32 | 9.18767 | 🟢 medium — moderately distinctive |
| 1621 | **cloth** | 6 | 955.32 | 9.18767 | 🟢 medium — moderately distinctive |
| 1622 | **dissolution** | 6 | 955.32 | 9.18767 | 🟢 medium — moderately distinctive |
| 1623 | **correct** | 8 | 954.54 | 6.885085 | 🟢 medium — moderately distinctive |
| 1624 | **finished** | 8 | 954.54 | 6.885085 | 🟢 medium — moderately distinctive |
| 1625 | **size** | 9 | 953.26 | 6.111895 | 🟢 medium — moderately distinctive |
| 1626 | **obtained** | 8 | 949.99 | 6.852295 | 🟢 medium — moderately distinctive |
| 1627 | **opens** | 8 | 949.99 | 6.852295 | 🟢 medium — moderately distinctive |
| 1628 | **divided** | 8 | 945.59 | 6.820546 | 🟢 medium — moderately distinctive |
| 1629 | **beneficial** | 8 | 945.59 | 6.820546 | 🟢 medium — moderately distinctive |
| 1630 | **south** | 12 | 942.16 | 4.53054 | 🟢 medium — moderately distinctive |
| 1631 | **led** | 11 | 939.74 | 4.929696 | 🟢 medium — moderately distinctive |
| 1632 | **former** | 10 | 939.06 | 5.418748 | 🟢 medium — moderately distinctive |
| 1633 | **trapped** | 7 | 936.67 | 7.721333 | 🟢 medium — moderately distinctive |
| 1634 | **combine** | 7 | 936.67 | 7.721333 | 🟢 medium — moderately distinctive |
| 1635 | **continue** | 13 | 932.68 | 4.139953 | 🟢 medium — moderately distinctive |
| 1636 | **perhaps** | 8 | 929.26 | 6.702763 | 🟢 medium — moderately distinctive |
| 1637 | **worst** | 8 | 929.26 | 6.702763 | 🟢 medium — moderately distinctive |
| 1638 | **execution** | 7 | 927.68 | 7.647225 | 🟢 medium — moderately distinctive |
| 1639 | **worth** | 11 | 926.71 | 4.861332 | 🟢 medium — moderately distinctive |
| 1640 | **tried** | 8 | 925.46 | 6.675364 | 🟢 medium — moderately distinctive |
| 1641 | **distant** | 6 | 925.41 | 8.899988 | 🟢 medium — moderately distinctive |
| 1642 | **quest** | 6 | 925.41 | 8.899988 | 🟢 medium — moderately distinctive |
| 1643 | **crossed** | 6 | 925.41 | 8.899988 | 🟢 medium — moderately distinctive |
| 1644 | **situations** | 6 | 925.41 | 8.899988 | 🟢 medium — moderately distinctive |
| 1645 | **wool** | 6 | 925.41 | 8.899988 | 🟢 medium — moderately distinctive |
| 1646 | **disillusionment** | 6 | 925.41 | 8.899988 | 🟢 medium — moderately distinctive |
| 1647 | **distinction** | 6 | 925.41 | 8.899988 | 🟢 medium — moderately distinctive |
| 1648 | **cloud** | 6 | 925.41 | 8.899988 | 🟢 medium — moderately distinctive |
| 1649 | **soup** | 6 | 925.41 | 8.899988 | 🟢 medium — moderately distinctive |
| 1650 | **com** | 6 | 925.41 | 8.899988 | 🟢 medium — moderately distinctive |
| 1651 | **remains** | 10 | 922.54 | 5.323438 | 🟢 medium — moderately distinctive |
| 1652 | **bit** | 8 | 921.77 | 6.648696 | 🟢 medium — moderately distinctive |
| 1653 | **save** | 8 | 921.77 | 6.648696 | 🟢 medium — moderately distinctive |
| 1654 | **including** | 13 | 921.39 | 4.089838 | 🟢 medium — moderately distinctive |
| 1655 | **attached** | 7 | 919.31 | 7.578232 | 🟢 medium — moderately distinctive |
| 1656 | **arrive** | 7 | 919.31 | 7.578232 | 🟢 medium — moderately distinctive |
| 1657 | **special** | 11 | 915.30 | 4.801485 | 🟢 medium — moderately distinctive |
| 1658 | **summit** | 8 | 914.65 | 6.597403 | 🟢 medium — moderately distinctive |
| 1659 | **written** | 8 | 914.65 | 6.597403 | 🟢 medium — moderately distinctive |
| 1660 | **bearing** | 7 | 911.48 | 7.513694 | 🟢 medium — moderately distinctive |
| 1661 | **accepting** | 7 | 911.48 | 7.513694 | 🟢 medium — moderately distinctive |
| 1662 | **names** | 7 | 911.48 | 7.513694 | 🟢 medium — moderately distinctive |
| 1663 | **merchant** | 8 | 911.23 | 6.57271 | 🟢 medium — moderately distinctive |
| 1664 | **books** | 8 | 907.89 | 6.548613 | 🟢 medium — moderately distinctive |
| 1665 | **language** | 7 | 904.12 | 7.453069 | 🟢 medium — moderately distinctive |
| 1666 | **direct** | 9 | 902.51 | 5.786473 | 🟢 medium — moderately distinctive |
| 1667 | **destruction** | 6 | 902.21 | 8.676844 | 🟢 medium — moderately distinctive |
| 1668 | **catch** | 6 | 902.21 | 8.676844 | 🟢 medium — moderately distinctive |
| 1669 | **somewhere** | 6 | 902.21 | 8.676844 | 🟢 medium — moderately distinctive |
| 1670 | **victims** | 6 | 902.21 | 8.676844 | 🟢 medium — moderately distinctive |
| 1671 | **cooked** | 6 | 902.21 | 8.676844 | 🟢 medium — moderately distinctive |
| 1672 | **fires** | 6 | 902.21 | 8.676844 | 🟢 medium — moderately distinctive |
| 1673 | **mirror** | 6 | 902.21 | 8.676844 | 🟢 medium — moderately distinctive |
| 1674 | **appearance** | 6 | 902.21 | 8.676844 | 🟢 medium — moderately distinctive |
| 1675 | **force** | 10 | 899.86 | 5.192532 | 🟢 medium — moderately distinctive |
| 1676 | **downwards** | 7 | 897.19 | 7.395911 | 🟢 medium — moderately distinctive |
| 1677 | **against** | 15 | 890.75 | 3.426667 | 🟢 medium — moderately distinctive |
| 1678 | **field** | 9 | 887.64 | 5.691163 | 🟢 medium — moderately distinctive |
| 1679 | **returned** | 8 | 886.52 | 6.394462 | 🟢 medium — moderately distinctive |
| 1680 | **sea** | 9 | 886.07 | 5.681112 | 🟢 medium — moderately distinctive |
| 1681 | **doubts** | 7 | 884.41 | 7.29055 | 🟢 medium — moderately distinctive |
| 1682 | **understood** | 7 | 884.41 | 7.29055 | 🟢 medium — moderately distinctive |
| 1683 | **slaughter** | 7 | 884.41 | 7.29055 | 🟢 medium — moderately distinctive |
| 1684 | **guided** | 6 | 883.25 | 8.494523 | 🟢 medium — moderately distinctive |
| 1685 | **forget** | 6 | 883.25 | 8.494523 | 🟢 medium — moderately distinctive |
| 1686 | **forgotten** | 6 | 883.25 | 8.494523 | 🟢 medium — moderately distinctive |
| 1687 | **spoken** | 6 | 883.25 | 8.494523 | 🟢 medium — moderately distinctive |
| 1688 | **error** | 6 | 883.25 | 8.494523 | 🟢 medium — moderately distinctive |
| 1689 | **rivals** | 6 | 883.25 | 8.494523 | 🟢 medium — moderately distinctive |
| 1690 | **establish** | 8 | 880.97 | 6.354457 | 🟢 medium — moderately distinctive |
| 1691 | **morning** | 10 | 879.80 | 5.076796 | 🟢 medium — moderately distinctive |
| 1692 | **mentioned** | 7 | 878.49 | 7.24176 | 🟢 medium — moderately distinctive |
| 1693 | **various** | 9 | 876.99 | 5.622843 | 🟢 medium — moderately distinctive |
| 1694 | **goal** | 8 | 875.64 | 6.31599 | 🟢 medium — moderately distinctive |
| 1695 | **decided** | 10 | 873.29 | 5.039258 | 🟢 medium — moderately distinctive |
| 1696 | **meanwhile** | 8 | 873.05 | 6.297298 | 🟢 medium — moderately distinctive |
| 1697 | **gathering** | 7 | 872.85 | 7.19524 | 🟢 medium — moderately distinctive |
| 1698 | **palm** | 8 | 870.50 | 6.278949 | 🟢 medium — moderately distinctive |
| 1699 | **achieved** | 8 | 868.01 | 6.260931 | 🟢 medium — moderately distinctive |
| 1700 | **invite** | 6 | 867.22 | 8.340372 | 🟢 medium — moderately distinctive |
| 1701 | **cure** | 6 | 867.22 | 8.340372 | 🟢 medium — moderately distinctive |
| 1702 | **lifestyle** | 6 | 867.22 | 8.340372 | 🟢 medium — moderately distinctive |
| 1703 | **league** | 6 | 867.22 | 8.340372 | 🟢 medium — moderately distinctive |
| 1704 | **pit** | 6 | 867.22 | 8.340372 | 🟢 medium — moderately distinctive |
| 1705 | **busy** | 6 | 867.22 | 8.340372 | 🟢 medium — moderately distinctive |
| 1706 | **display** | 6 | 867.22 | 8.340372 | 🟢 medium — moderately distinctive |
| 1707 | **leather** | 6 | 867.22 | 8.340372 | 🟢 medium — moderately distinctive |
| 1708 | **prince** | 6 | 867.22 | 8.340372 | 🟢 medium — moderately distinctive |
| 1709 | **cushion** | 6 | 867.22 | 8.340372 | 🟢 medium — moderately distinctive |
| 1710 | **everybody** | 6 | 867.22 | 8.340372 | 🟢 medium — moderately distinctive |
| 1711 | **consulted** | 6 | 867.22 | 8.340372 | 🟢 medium — moderately distinctive |
| 1712 | **entered** | 9 | 861.59 | 5.524108 | 🟢 medium — moderately distinctive |
| 1713 | **stand** | 8 | 860.77 | 6.208745 | 🟢 medium — moderately distinctive |
| 1714 | **certainly** | 8 | 860.77 | 6.208745 | 🟢 medium — moderately distinctive |
| 1715 | **year** | 23 | 860.03 | 2.157697 | 🟢 medium — moderately distinctive |
| 1716 | **increase** | 14 | 857.70 | 3.535181 | 🟢 medium — moderately distinctive |
| 1717 | **fit** | 7 | 857.34 | 7.067407 | 🟢 medium — moderately distinctive |
| 1718 | **refused** | 8 | 856.15 | 6.175409 | 🟢 medium — moderately distinctive |
| 1719 | **onwards** | 6 | 853.34 | 8.206841 | 🟢 medium — moderately distinctive |
| 1720 | **spite** | 6 | 853.34 | 8.206841 | 🟢 medium — moderately distinctive |
| 1721 | **swiftly** | 6 | 853.34 | 8.206841 | 🟢 medium — moderately distinctive |
| 1722 | **arranged** | 7 | 852.58 | 7.028186 | 🟢 medium — moderately distinctive |
| 1723 | **closer** | 7 | 852.58 | 7.028186 | 🟢 medium — moderately distinctive |
| 1724 | **giant** | 7 | 848.00 | 6.990446 | 🟢 medium — moderately distinctive |
| 1725 | **achieve** | 8 | 847.34 | 6.111895 | 🟢 medium — moderately distinctive |
| 1726 | **resolve** | 8 | 843.14 | 6.08159 | 🟢 medium — moderately distinctive |
| 1727 | **placed** | 8 | 843.14 | 6.08159 | 🟢 medium — moderately distinctive |
| 1728 | **several** | 11 | 841.46 | 4.414165 | 🟢 medium — moderately distinctive |
| 1729 | **defeat** | 6 | 841.09 | 8.089058 | 🟢 medium — moderately distinctive |
| 1730 | **supposed** | 6 | 841.09 | 8.089058 | 🟢 medium — moderately distinctive |
| 1731 | **rejecting** | 6 | 841.09 | 8.089058 | 🟢 medium — moderately distinctive |
| 1732 | **transfer** | 8 | 841.09 | 6.066775 | 🟢 medium — moderately distinctive |
| 1733 | **move** | 11 | 836.69 | 4.389129 | 🟢 medium — moderately distinctive |
| 1734 | **bell** | 7 | 835.22 | 6.885085 | 🟢 medium — moderately distinctive |
| 1735 | **danger** | 7 | 835.22 | 6.885085 | 🟢 medium — moderately distinctive |
| 1736 | **total** | 14 | 831.88 | 3.428768 | 🟢 medium — moderately distinctive |
| 1737 | **shearing** | 5 | 831.24 | 9.593135 | 🟢 medium — moderately distinctive |
| 1738 | **marriage** | 5 | 831.24 | 9.593135 | 🟢 medium — moderately distinctive |
| 1739 | **incapable** | 5 | 831.24 | 9.593135 | 🟢 medium — moderately distinctive |
| 1740 | **permanence** | 5 | 831.24 | 9.593135 | 🟢 medium — moderately distinctive |
| 1741 | **entourage** | 5 | 831.24 | 9.593135 | 🟢 medium — moderately distinctive |
| 1742 | **piled** | 5 | 831.24 | 9.593135 | 🟢 medium — moderately distinctive |
| 1743 | **lit** | 5 | 831.24 | 9.593135 | 🟢 medium — moderately distinctive |
| 1744 | **friendship** | 5 | 831.24 | 9.593135 | 🟢 medium — moderately distinctive |
| 1745 | **eats** | 5 | 831.24 | 9.593135 | 🟢 medium — moderately distinctive |
| 1746 | **whip** | 5 | 831.24 | 9.593135 | 🟢 medium — moderately distinctive |
| 1747 | **distress** | 5 | 831.24 | 9.593135 | 🟢 medium — moderately distinctive |
| 1748 | **corpses** | 5 | 831.24 | 9.593135 | 🟢 medium — moderately distinctive |
| 1749 | **courage** | 5 | 831.24 | 9.593135 | 🟢 medium — moderately distinctive |
| 1750 | **dirty** | 5 | 831.24 | 9.593135 | 🟢 medium — moderately distinctive |
| 1751 | **wasted** | 5 | 831.24 | 9.593135 | 🟢 medium — moderately distinctive |
| 1752 | **sleeping** | 5 | 831.24 | 9.593135 | 🟢 medium — moderately distinctive |
| 1753 | **buddhist** | 5 | 831.24 | 9.593135 | 🟢 medium — moderately distinctive |
| 1754 | **succession** | 5 | 831.24 | 9.593135 | 🟢 medium — moderately distinctive |
| 1755 | **attainment** | 5 | 831.24 | 9.593135 | 🟢 medium — moderately distinctive |
| 1756 | **courageous** | 5 | 831.24 | 9.593135 | 🟢 medium — moderately distinctive |
| 1757 | **infallible** | 5 | 831.24 | 9.593135 | 🟢 medium — moderately distinctive |
| 1758 | **shining** | 5 | 831.24 | 9.593135 | 🟢 medium — moderately distinctive |
| 1759 | **technique** | 5 | 831.24 | 9.593135 | 🟢 medium — moderately distinctive |
| 1760 | **secrets** | 5 | 831.24 | 9.593135 | 🟢 medium — moderately distinctive |
| 1761 | **enlightened** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive |
| 1762 | **twofold** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive |
| 1763 | **fame** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive |
| 1764 | **dakinis** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive |
| 1765 | **dakini** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive |
| 1766 | **dumb** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive |
| 1767 | **proverb** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive |
| 1768 | **sorrows** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive |
| 1769 | **sack** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive |
| 1770 | **ananda** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive |
| 1771 | **machik** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive |
| 1772 | **persevere** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive |
| 1773 | **beginningless** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive |
| 1774 | **crying** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive |
| 1775 | **millstone** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive |
| 1776 | **beliefs** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive |
| 1777 | **reigned** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive |
| 1778 | **tibetan** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive |
| 1779 | **unchanging** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive |
| 1780 | **translators** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive |
| 1781 | **vairotsana** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive |
| 1782 | **circum** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive |
| 1783 | **manjusri** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive |
| 1784 | **radiant** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive |
| 1785 | **pandita** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive |
| 1786 | **drom** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive |
| 1787 | **laziness** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive |
| 1788 | **afflictions** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive |
| 1789 | **decadent** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive |
| 1790 | **hermit** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive |
| 1791 | **wearing** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive |
| 1792 | **horns** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive |
| 1793 | **scholar** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive |
| 1794 | **gonpo** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive |
| 1795 | **chengawa** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive |
| 1796 | **recited** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive |
| 1797 | **threefold** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive |
| 1798 | **streams** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive |
| 1799 | **ripen** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive |
| 1800 | **immortality** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive |
| 1801 | **naga** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive |
| 1802 | **kadampas** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive |
| 1803 | **hollow** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive |
| 1804 | **arhat** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive |
| 1805 | **deserted** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive |
| 1806 | **womb** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive |
| 1807 | **asleep** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive |
| 1808 | **stronghold** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive |
| 1809 | **conduces** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive |
| 1810 | **emulate** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive |
| 1811 | **molten** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive |
| 1812 | **fool** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive |
| 1813 | **red-hot** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive |
| 1814 | **unimaginable** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive |
| 1815 | **shoulders** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive |
| 1816 | **delight** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive |
| 1817 | **swords** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive |
| 1818 | **repa** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive |
| 1819 | **turquoise** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive |
| 1820 | **swallow** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive |
| 1821 | **delicious** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive |
| 1822 | **rage** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive |
| 1823 | **mustard** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive |
| 1824 | **yaks** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive |
| 1825 | **confessing** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive |
| 1826 | **illnesses** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive |
| 1827 | **anguish** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive |
| 1828 | **ogress** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive |
| 1829 | **displease** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive |
| 1830 | **circumambulating** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive |
| 1831 | **resting** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive |
| 1832 | **trickery** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive |
| 1833 | **rites** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive |
| 1834 | **defiled** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive |
| 1835 | **proliferating** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive |
| 1836 | **antidotes** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive |
| 1837 | **sravaka** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive |
| 1838 | **tirthika** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive |
| 1839 | **ashamed** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive |
| 1840 | **guests** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive |
| 1841 | **feast** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive |
| 1842 | **heartfelt** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive |
| 1843 | **tale** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive |
| 1844 | **sandal** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive |
| 1845 | **disrespect** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive |
| 1846 | **dwell** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive |
| 1847 | **homage** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive |
| 1848 | **incense** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive |
| 1849 | **jewelled** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive |
| 1850 | **prostration** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive |
| 1851 | **soles** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive |
| 1852 | **perseverance** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive |
| 1853 | **boots** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive |
| 1854 | **cup** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive |
| 1855 | **spontaneous** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive |
| 1856 | **obstacle-makers** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive |
| 1857 | **abhidharma** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive |
| 1858 | **asariga** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive |
| 1859 | **asanga** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive |
| 1860 | **rotten** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive |
| 1861 | **medi** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive |
| 1862 | **gift** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive |
| 1863 | **distractions** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive |
| 1864 | **tathagatas** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive |
| 1865 | **pacify** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive |
| 1866 | **non-dharma** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive |
| 1867 | **symbols** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive |
| 1868 | **liberates** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive |
| 1869 | **recitations** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive |
| 1870 | **sever** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive |
| 1871 | **conceit** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive |
| 1872 | **tendzin** | 5 | 830.96 | 9.59 | 🟢 medium — moderately distinctive |
| 1873 | **maintain** | 9 | 830.29 | 5.323438 | 🟢 medium — moderately distinctive |
| 1874 | **hole** | 6 | 830.14 | 7.983697 | 🟢 medium — moderately distinctive |
| 1875 | **dried** | 6 | 830.14 | 7.983697 | 🟢 medium — moderately distinctive |
| 1876 | **plenty** | 6 | 830.14 | 7.983697 | 🟢 medium — moderately distinctive |
| 1877 | **perceived** | 6 | 830.14 | 7.983697 | 🟢 medium — moderately distinctive |
| 1878 | **boat** | 6 | 830.14 | 7.983697 | 🟢 medium — moderately distinctive |
| 1879 | **states** | 12 | 829.58 | 3.989173 | 🟢 medium — moderately distinctive |
| 1880 | **houses** | 8 | 825.67 | 5.955549 | 🟢 medium — moderately distinctive |
| 1881 | **nonetheless** | 6 | 820.23 | 7.888387 | 🟢 medium — moderately distinctive |
| 1882 | **enjoyed** | 6 | 820.23 | 7.888387 | 🟢 medium — moderately distinctive |
| 1883 | **cease** | 6 | 820.23 | 7.888387 | 🟢 medium — moderately distinctive |
| 1884 | **worked** | 7 | 820.04 | 6.759922 | 🟢 medium — moderately distinctive |
| 1885 | **course** | 8 | 818.56 | 5.904256 | 🟢 medium — moderately distinctive |
| 1886 | **visit** | 8 | 818.56 | 5.904256 | 🟢 medium — moderately distinctive |
| 1887 | **indian** | 7 | 813.10 | 6.702763 | 🟢 medium — moderately distinctive |
| 1888 | **weight** | 7 | 813.10 | 6.702763 | 🟢 medium — moderately distinctive |
| 1889 | **sweet** | 7 | 813.10 | 6.702763 | 🟢 medium — moderately distinctive |
| 1890 | **repay** | 7 | 813.10 | 6.702763 | 🟢 medium — moderately distinctive |
| 1891 | **seventh** | 6 | 811.18 | 7.801376 | 🟢 medium — moderately distinctive |
| 1892 | **voice** | 6 | 811.18 | 7.801376 | 🟢 medium — moderately distinctive |
| 1893 | **touch** | 6 | 811.18 | 7.801376 | 🟢 medium — moderately distinctive |
| 1894 | **passing** | 6 | 811.18 | 7.801376 | 🟢 medium — moderately distinctive |
| 1895 | **air** | 8 | 810.15 | 5.843631 | 🟢 medium — moderately distinctive |
| 1896 | **battle** | 7 | 809.78 | 6.675364 | 🟢 medium — moderately distinctive |
| 1897 | **working** | 9 | 807.97 | 5.180337 | 🟢 medium — moderately distinctive |
| 1898 | **ordered** | 7 | 806.54 | 6.648696 | 🟢 medium — moderately distinctive |
| 1899 | **causing** | 7 | 806.54 | 6.648696 | 🟢 medium — moderately distinctive |
| 1900 | **period** | 12 | 804.36 | 3.867917 | 🟢 medium — moderately distinctive |
| 1901 | **asking** | 7 | 803.39 | 6.622721 | 🟢 medium — moderately distinctive |
| 1902 | **reaches** | 6 | 802.86 | 7.721333 | 🟢 medium — moderately distinctive |
| 1903 | **circle** | 6 | 802.86 | 7.721333 | 🟢 medium — moderately distinctive |
| 1904 | **doors** | 6 | 802.86 | 7.721333 | 🟢 medium — moderately distinctive |
| 1905 | **serving** | 6 | 802.86 | 7.721333 | 🟢 medium — moderately distinctive |
| 1906 | **compared** | 12 | 800.33 | 3.848531 | 🟢 medium — moderately distinctive |
| 1907 | **carrying** | 7 | 800.32 | 6.597403 | 🟢 medium — moderately distinctive |
| 1908 | **control** | 10 | 796.47 | 4.595923 | 🟢 medium — moderately distinctive |
| 1909 | **inferior** | 5 | 796.10 | 9.18767 | 🟢 medium — moderately distinctive |
| 1910 | **dies** | 5 | 796.10 | 9.18767 | 🟢 medium — moderately distinctive |
| 1911 | **illusory** | 5 | 796.10 | 9.18767 | 🟢 medium — moderately distinctive |
| 1912 | **incalculable** | 5 | 796.10 | 9.18767 | 🟢 medium — moderately distinctive |
| 1913 | **wrapped** | 5 | 796.10 | 9.18767 | 🟢 medium — moderately distinctive |
| 1914 | **religious** | 5 | 796.10 | 9.18767 | 🟢 medium — moderately distinctive |
| 1915 | **terribly** | 5 | 796.10 | 9.18767 | 🟢 medium — moderately distinctive |
| 1916 | **sits** | 5 | 796.10 | 9.18767 | 🟢 medium — moderately distinctive |
| 1917 | **tasks** | 5 | 796.10 | 9.18767 | 🟢 medium — moderately distinctive |
| 1918 | **openly** | 5 | 796.10 | 9.18767 | 🟢 medium — moderately distinctive |
| 1919 | **mouse** | 5 | 796.10 | 9.18767 | 🟢 medium — moderately distinctive |
| 1920 | **hail** | 5 | 796.10 | 9.18767 | 🟢 medium — moderately distinctive |
| 1921 | **captain** | 5 | 796.10 | 9.18767 | 🟢 medium — moderately distinctive |
| 1922 | **faithfully** | 5 | 796.10 | 9.18767 | 🟢 medium — moderately distinctive |
| 1923 | **bone** | 5 | 796.10 | 9.18767 | 🟢 medium — moderately distinctive |
| 1924 | **thirteen** | 5 | 796.10 | 9.18767 | 🟢 medium — moderately distinctive |
| 1925 | **emanating** | 5 | 796.10 | 9.18767 | 🟢 medium — moderately distinctive |
| 1926 | **studied** | 6 | 795.15 | 7.647225 | 🟢 medium — moderately distinctive |
| 1927 | **dangerous** | 6 | 795.15 | 7.647225 | 🟢 medium — moderately distinctive |
| 1928 | **makers** | 7 | 794.40 | 6.548613 | 🟢 medium — moderately distinctive |
| 1929 | **generally** | 8 | 793.28 | 5.721934 | 🟢 medium — moderately distinctive |
| 1930 | **further** | 12 | 789.32 | 3.795559 | 🟢 medium — moderately distinctive |
| 1931 | **general** | 11 | 789.19 | 4.139953 | 🟢 medium — moderately distinctive |
| 1932 | **winter** | 8 | 789.01 | 5.691163 | 🟢 medium — moderately distinctive |
| 1933 | **occur** | 7 | 788.76 | 6.502093 | 🟢 medium — moderately distinctive |
| 1934 | **fighting** | 6 | 787.98 | 7.578232 | 🟢 medium — moderately distinctive |
| 1935 | **calling** | 7 | 783.37 | 6.457641 | 🟢 medium — moderately distinctive |
| 1936 | **preliminary** | 8 | 782.18 | 5.641891 | 🟢 medium — moderately distinctive |
| 1937 | **representation** | 6 | 781.27 | 7.513694 | 🟢 medium — moderately distinctive |
| 1938 | **threatening** | 6 | 781.27 | 7.513694 | 🟢 medium — moderately distinctive |
| 1939 | **sources** | 11 | 779.64 | 4.089838 | 🟢 medium — moderately distinctive |
| 1940 | **linked** | 7 | 778.21 | 6.415081 | 🟢 medium — moderately distinctive |
| 1941 | **concentrate** | 7 | 778.21 | 6.415081 | 🟢 medium — moderately distinctive |
| 1942 | **flow** | 8 | 776.95 | 5.604151 | 🟢 medium — moderately distinctive |
| 1943 | **cattle** | 7 | 775.70 | 6.394462 | 🟢 medium — moderately distinctive |
| 1944 | **definitely** | 6 | 774.96 | 7.453069 | 🟢 medium — moderately distinctive |
| 1945 | **mine** | 8 | 771.91 | 5.567784 | 🟢 medium — moderately distinctive |
| 1946 | **everywhere** | 5 | 771.18 | 8.899988 | 🟢 medium — moderately distinctive |
| 1947 | **snows** | 5 | 771.18 | 8.899988 | 🟢 medium — moderately distinctive |
| 1948 | **missing** | 5 | 771.18 | 8.899988 | 🟢 medium — moderately distinctive |
| 1949 | **meaningless** | 5 | 771.18 | 8.899988 | 🟢 medium — moderately distinctive |
| 1950 | **waves** | 5 | 771.18 | 8.899988 | 🟢 medium — moderately distinctive |
| 1951 | **foolish** | 5 | 771.18 | 8.899988 | 🟢 medium — moderately distinctive |
| 1952 | **lasts** | 5 | 771.18 | 8.899988 | 🟢 medium — moderately distinctive |
| 1953 | **forests** | 5 | 771.18 | 8.899988 | 🟢 medium — moderately distinctive |
| 1954 | **certainty** | 5 | 771.18 | 8.899988 | 🟢 medium — moderately distinctive |
| 1955 | **hang** | 5 | 771.18 | 8.899988 | 🟢 medium — moderately distinctive |
| 1956 | **beaten** | 5 | 771.18 | 8.899988 | 🟢 medium — moderately distinctive |
| 1957 | **lacks** | 5 | 771.18 | 8.899988 | 🟢 medium — moderately distinctive |
| 1958 | **painful** | 5 | 771.18 | 8.899988 | 🟢 medium — moderately distinctive |
| 1959 | **describe** | 5 | 771.18 | 8.899988 | 🟢 medium — moderately distinctive |
| 1960 | **undergoing** | 5 | 771.18 | 8.899988 | 🟢 medium — moderately distinctive |
| 1961 | **gardens** | 5 | 771.18 | 8.899988 | 🟢 medium — moderately distinctive |
| 1962 | **afraid** | 5 | 771.18 | 8.899988 | 🟢 medium — moderately distinctive |
| 1963 | **queen** | 5 | 771.18 | 8.899988 | 🟢 medium — moderately distinctive |
| 1964 | **exceptional** | 6 | 769.02 | 7.395911 | 🟢 medium — moderately distinctive |
| 1965 | **seems** | 7 | 768.50 | 6.335039 | 🟢 medium — moderately distinctive |
| 1966 | **included** | 9 | 765.96 | 4.911004 | 🟢 medium — moderately distinctive |
| 1967 | **choose** | 6 | 763.40 | 7.341843 | 🟢 medium — moderately distinctive |
| 1968 | **breaking** | 6 | 763.40 | 7.341843 | 🟢 medium — moderately distinctive |
| 1969 | **watch** | 6 | 763.40 | 7.341843 | 🟢 medium — moderately distinctive |
| 1970 | **creating** | 6 | 758.06 | 7.29055 | 🟢 medium — moderately distinctive |
| 1971 | **west** | 11 | 757.66 | 3.974548 | 🟢 medium — moderately distinctive |
| 1972 | **wants** | 8 | 755.58 | 5.45 | 🟢 medium — moderately distinctive |
| 1973 | **focus** | 7 | 755.25 | 6.225839 | 🟢 medium — moderately distinctive |
| 1974 | **completed** | 10 | 753.63 | 4.348746 | 🟢 medium — moderately distinctive |
| 1975 | **tied** | 6 | 752.99 | 7.24176 | 🟢 medium — moderately distinctive |
| 1976 | **listened** | 5 | 751.84 | 8.676844 | 🟢 medium — moderately distinctive |
| 1977 | **theirs** | 5 | 751.84 | 8.676844 | 🟢 medium — moderately distinctive |
| 1978 | **consume** | 5 | 751.84 | 8.676844 | 🟢 medium — moderately distinctive |
| 1979 | **dragged** | 5 | 751.84 | 8.676844 | 🟢 medium — moderately distinctive |
| 1980 | **homeland** | 5 | 751.84 | 8.676844 | 🟢 medium — moderately distinctive |
| 1981 | **rocky** | 5 | 751.84 | 8.676844 | 🟢 medium — moderately distinctive |
| 1982 | **contaminated** | 5 | 751.84 | 8.676844 | 🟢 medium — moderately distinctive |
| 1983 | **rocks** | 5 | 751.84 | 8.676844 | 🟢 medium — moderately distinctive |
| 1984 | **devoted** | 5 | 751.84 | 8.676844 | 🟢 medium — moderately distinctive |
| 1985 | **generous** | 5 | 751.84 | 8.676844 | 🟢 medium — moderately distinctive |
| 1986 | **staying** | 5 | 751.84 | 8.676844 | 🟢 medium — moderately distinctive |
| 1987 | **substance** | 5 | 751.84 | 8.676844 | 🟢 medium — moderately distinctive |
| 1988 | **application** | 7 | 749.13 | 6.175409 | 🟢 medium — moderately distinctive |
| 1989 | **setting** | 7 | 749.13 | 6.175409 | 🟢 medium — moderately distinctive |
| 1990 | **completing** | 6 | 748.15 | 7.19524 | 🟢 medium — moderately distinctive |
| 1991 | **begin** | 8 | 744.99 | 5.373627 | 🟢 medium — moderately distinctive |
| 1992 | **fourth** | 9 | 744.41 | 4.772854 | 🟢 medium — moderately distinctive |
| 1993 | **door** | 6 | 743.53 | 7.150788 | 🟢 medium — moderately distinctive |
| 1994 | **visible** | 6 | 743.53 | 7.150788 | 🟢 medium — moderately distinctive |
| 1995 | **ready** | 7 | 739.57 | 6.096628 | 🟢 medium — moderately distinctive |
| 1996 | **upwards** | 6 | 739.11 | 7.108229 | 🟢 medium — moderately distinctive |
| 1997 | **firm** | 10 | 738.32 | 4.260416 | 🟢 medium — moderately distinctive |
| 1998 | **commitments** | 7 | 737.75 | 6.08159 | 🟢 medium — moderately distinctive |
| 1999 | **confused** | 5 | 736.04 | 8.494523 | 🟢 medium — moderately distinctive |
| 2000 | **overcome** | 5 | 736.04 | 8.494523 | 🟢 medium — moderately distinctive |
| 2001 | **stays** | 5 | 736.04 | 8.494523 | 🟢 medium — moderately distinctive |
| 2002 | **ours** | 5 | 736.04 | 8.494523 | 🟢 medium — moderately distinctive |
| 2003 | **throwing** | 5 | 736.04 | 8.494523 | 🟢 medium — moderately distinctive |
| 2004 | **teeth** | 5 | 736.04 | 8.494523 | 🟢 medium — moderately distinctive |
| 2005 | **vicious** | 5 | 736.04 | 8.494523 | 🟢 medium — moderately distinctive |
| 2006 | **gem** | 5 | 736.04 | 8.494523 | 🟢 medium — moderately distinctive |
| 2007 | **wanting** | 5 | 736.04 | 8.494523 | 🟢 medium — moderately distinctive |
| 2008 | **grave** | 5 | 736.04 | 8.494523 | 🟢 medium — moderately distinctive |
| 2009 | **illustrated** | 5 | 736.04 | 8.494523 | 🟢 medium — moderately distinctive |
| 2010 | **occasions** | 5 | 736.04 | 8.494523 | 🟢 medium — moderately distinctive |
| 2011 | **surely** | 5 | 736.04 | 8.494523 | 🟢 medium — moderately distinctive |
| 2012 | **undesirable** | 5 | 736.04 | 8.494523 | 🟢 medium — moderately distinctive |
| 2013 | **temper** | 5 | 736.04 | 8.494523 | 🟢 medium — moderately distinctive |
| 2014 | **lowest** | 7 | 735.95 | 6.066775 | 🟢 medium — moderately distinctive |
| 2015 | **telling** | 6 | 734.86 | 7.067407 | 🟢 medium — moderately distinctive |
| 2016 | **stability** | 8 | 733.27 | 5.28907 | 🟢 medium — moderately distinctive |
| 2017 | **attacked** | 6 | 730.78 | 7.028186 | 🟢 medium — moderately distinctive |
| 2018 | **appropriate** | 7 | 729.02 | 6.009616 | 🟢 medium — moderately distinctive |
| 2019 | **difficulty** | 6 | 726.86 | 6.990446 | 🟢 medium — moderately distinctive |
| 2020 | **helping** | 6 | 726.86 | 6.990446 | 🟢 medium — moderately distinctive |
| 2021 | **beans** | 6 | 726.86 | 6.990446 | 🟢 medium — moderately distinctive |
| 2022 | **pressing** | 6 | 726.86 | 6.990446 | 🟢 medium — moderately distinctive |
| 2023 | **gets** | 7 | 725.70 | 5.982217 | 🟢 medium — moderately distinctive |
| 2024 | **potential** | 8 | 725.08 | 5.230037 | 🟢 medium — moderately distinctive |
| 2025 | **abandoned** | 6 | 723.08 | 6.954078 | 🟢 medium — moderately distinctive |
| 2026 | **treasury** | 9 | 722.73 | 4.633793 | 🟢 medium — moderately distinctive |
| 2027 | **shore** | 5 | 722.69 | 8.340372 | 🟢 medium — moderately distinctive |
| 2028 | **guidance** | 5 | 722.69 | 8.340372 | 🟢 medium — moderately distinctive |
| 2029 | **beneath** | 5 | 722.69 | 8.340372 | 🟢 medium — moderately distinctive |
| 2030 | **suffers** | 5 | 722.69 | 8.340372 | 🟢 medium — moderately distinctive |
| 2031 | **smoke** | 5 | 722.69 | 8.340372 | 🟢 medium — moderately distinctive |
| 2032 | **solely** | 5 | 722.69 | 8.340372 | 🟢 medium — moderately distinctive |
| 2033 | **logic** | 5 | 722.69 | 8.340372 | 🟢 medium — moderately distinctive |
| 2034 | **exchanging** | 5 | 722.69 | 8.340372 | 🟢 medium — moderately distinctive |
| 2035 | **principal** | 7 | 717.76 | 5.916835 | 🟢 medium — moderately distinctive |
| 2036 | **forced** | 7 | 716.24 | 5.904256 | 🟢 medium — moderately distinctive |
| 2037 | **crucial** | 6 | 715.90 | 6.885085 | 🟢 medium — moderately distinctive |
| 2038 | **hill** | 6 | 715.90 | 6.885085 | 🟢 medium — moderately distinctive |
| 2039 | **par** | 6 | 715.90 | 6.885085 | 🟢 medium — moderately distinctive |
| 2040 | **marks** | 8 | 714.06 | 5.150484 | 🟢 medium — moderately distinctive |
| 2041 | **lot** | 7 | 713.24 | 5.879563 | 🟢 medium — moderately distinctive |
| 2042 | **belongs** | 5 | 711.12 | 8.206841 | 🟢 medium — moderately distinctive |
| 2043 | **art** | 5 | 711.12 | 8.206841 | 🟢 medium — moderately distinctive |
| 2044 | **destroying** | 5 | 711.12 | 8.206841 | 🟢 medium — moderately distinctive |
| 2045 | **beer** | 5 | 711.12 | 8.206841 | 🟢 medium — moderately distinctive |
| 2046 | **correspond** | 5 | 711.12 | 8.206841 | 🟢 medium — moderately distinctive |
| 2047 | **throw** | 5 | 711.12 | 8.206841 | 🟢 medium — moderately distinctive |
| 2048 | **aggression** | 5 | 711.12 | 8.206841 | 🟢 medium — moderately distinctive |
| 2049 | **arose** | 5 | 711.12 | 8.206841 | 🟢 medium — moderately distinctive |
| 2050 | **common** | 11 | 710.95 | 3.729504 | 🟢 medium — moderately distinctive |
| 2051 | **volumes** | 6 | 709.19 | 6.820546 | 🟢 medium — moderately distinctive |
| 2052 | **low** | 9 | 708.61 | 4.543279 | 🟢 medium — moderately distinctive |
| 2053 | **wall** | 7 | 707.46 | 5.831935 | 🟢 medium — moderately distinctive |
| 2054 | **concern** | 8 | 706.90 | 5.098897 | 🟢 medium — moderately distinctive |
| 2055 | **steady** | 7 | 704.68 | 5.808946 | 🟢 medium — moderately distinctive |
| 2056 | **third** | 9 | 703.69 | 4.511731 | 🟢 medium — moderately distinctive |
| 2057 | **command** | 5 | 700.91 | 8.089058 | 🟢 medium — moderately distinctive |
| 2058 | **reading** | 5 | 700.91 | 8.089058 | 🟢 medium — moderately distinctive |
| 2059 | **touched** | 5 | 700.91 | 8.089058 | 🟢 medium — moderately distinctive |
| 2060 | **works** | 6 | 699.88 | 6.730934 | 🟢 medium — moderately distinctive |
| 2061 | **slightly** | 8 | 697.18 | 5.028787 | 🟢 medium — moderately distinctive |
| 2062 | **sovereign** | 5 | 691.78 | 7.983697 | 🟢 medium — moderately distinctive |
| 2063 | **sooner** | 5 | 691.78 | 7.983697 | 🟢 medium — moderately distinctive |
| 2064 | **accompanied** | 5 | 691.78 | 7.983697 | 🟢 medium — moderately distinctive |
| 2065 | **becoming** | 6 | 685.99 | 6.597403 | 🟢 medium — moderately distinctive |
| 2066 | **owner** | 6 | 685.99 | 6.597403 | 🟢 medium — moderately distinctive |
| 2067 | **below** | 9 | 684.14 | 4.386385 | 🟢 medium — moderately distinctive |
| 2068 | **tremendous** | 5 | 683.52 | 7.888387 | 🟢 medium — moderately distinctive |
| 2069 | **expert** | 5 | 683.52 | 7.888387 | 🟢 medium — moderately distinctive |
| 2070 | **waste** | 6 | 683.42 | 6.57271 | 🟢 medium — moderately distinctive |
| 2071 | **presented** | 6 | 676.08 | 6.502093 | 🟢 medium — moderately distinctive |
| 2072 | **mix** | 5 | 675.98 | 7.801376 | 🟢 medium — moderately distinctive |
| 2073 | **accordingly** | 5 | 675.98 | 7.801376 | 🟢 medium — moderately distinctive |
| 2074 | **criticized** | 5 | 675.98 | 7.801376 | 🟢 medium — moderately distinctive |
| 2075 | **rush** | 5 | 675.98 | 7.801376 | 🟢 medium — moderately distinctive |
| 2076 | **seeds** | 5 | 675.98 | 7.801376 | 🟢 medium — moderately distinctive |
| 2077 | **session** | 7 | 675.42 | 5.567784 | 🟢 medium — moderately distinctive |
| 2078 | **wait** | 6 | 671.46 | 6.457641 | 🟢 medium — moderately distinctive |
| 2079 | **hardly** | 5 | 669.05 | 7.721333 | 🟢 medium — moderately distinctive |
| 2080 | **mar** | 6 | 667.03 | 6.415081 | 🟢 medium — moderately distinctive |
| 2081 | **business** | 10 | 666.94 | 3.848531 | 🟢 medium — moderately distinctive |
| 2082 | **discouragement** | 4 | 664.99 | 9.593135 | 🟢 medium — moderately distinctive |
| 2083 | **constitutes** | 4 | 664.99 | 9.593135 | 🟢 medium — moderately distinctive |
| 2084 | **utter** | 4 | 664.99 | 9.593135 | 🟢 medium — moderately distinctive |
| 2085 | **nepal** | 4 | 664.99 | 9.593135 | 🟢 medium — moderately distinctive |
| 2086 | **youth** | 4 | 664.99 | 9.593135 | 🟢 medium — moderately distinctive |
| 2087 | **neck** | 4 | 664.99 | 9.593135 | 🟢 medium — moderately distinctive |
| 2088 | **peas** | 4 | 664.99 | 9.593135 | 🟢 medium — moderately distinctive |
| 2089 | **dissolving** | 4 | 664.99 | 9.593135 | 🟢 medium — moderately distinctive |
| 2090 | **gently** | 4 | 664.99 | 9.593135 | 🟢 medium — moderately distinctive |
| 2091 | **intrinsic** | 4 | 664.99 | 9.593135 | 🟢 medium — moderately distinctive |
| 2092 | **famine** | 4 | 664.99 | 9.593135 | 🟢 medium — moderately distinctive |
| 2093 | **silk** | 4 | 664.99 | 9.593135 | 🟢 medium — moderately distinctive |
| 2094 | **ambitions** | 4 | 664.99 | 9.593135 | 🟢 medium — moderately distinctive |
| 2095 | **dispel** | 4 | 664.99 | 9.593135 | 🟢 medium — moderately distinctive |
| 2096 | **suck** | 4 | 664.99 | 9.593135 | 🟢 medium — moderately distinctive |
| 2097 | **stomach** | 4 | 664.99 | 9.593135 | 🟢 medium — moderately distinctive |
| 2098 | **sore** | 4 | 664.99 | 9.593135 | 🟢 medium — moderately distinctive |
| 2099 | **stricken** | 4 | 664.99 | 9.593135 | 🟢 medium — moderately distinctive |
| 2100 | **pinch** | 4 | 664.99 | 9.593135 | 🟢 medium — moderately distinctive |
| 2101 | **weary** | 4 | 664.99 | 9.593135 | 🟢 medium — moderately distinctive |
| 2102 | **ati** | 4 | 664.99 | 9.593135 | 🟢 medium — moderately distinctive |
| 2103 | **spit** | 4 | 664.99 | 9.593135 | 🟢 medium — moderately distinctive |
| 2104 | **proud** | 4 | 664.99 | 9.593135 | 🟢 medium — moderately distinctive |
| 2105 | **speaks** | 4 | 664.99 | 9.593135 | 🟢 medium — moderately distinctive |
| 2106 | **praise** | 4 | 664.99 | 9.593135 | 🟢 medium — moderately distinctive |
| 2107 | **stars** | 4 | 664.99 | 9.593135 | 🟢 medium — moderately distinctive |
| 2108 | **spells** | 4 | 664.99 | 9.593135 | 🟢 medium — moderately distinctive |
| 2109 | **sandalwood** | 4 | 664.99 | 9.593135 | 🟢 medium — moderately distinctive |
| 2110 | **mentality** | 4 | 664.99 | 9.593135 | 🟢 medium — moderately distinctive |
| 2111 | **sweep** | 4 | 664.99 | 9.593135 | 🟢 medium — moderately distinctive |
| 2112 | **prisoner** | 4 | 664.99 | 9.593135 | 🟢 medium — moderately distinctive |
| 2113 | **inherited** | 4 | 664.99 | 9.593135 | 🟢 medium — moderately distinctive |
| 2114 | **dawn** | 4 | 664.99 | 9.593135 | 🟢 medium — moderately distinctive |
| 2115 | **rubbing** | 4 | 664.99 | 9.593135 | 🟢 medium — moderately distinctive |
| 2116 | **radial** | 4 | 664.99 | 9.593135 | 🟢 medium — moderately distinctive |
| 2117 | **kaya** | 4 | 664.99 | 9.593135 | 🟢 medium — moderately distinctive |
| 2118 | **pleasing** | 4 | 664.99 | 9.593135 | 🟢 medium — moderately distinctive |
| 2119 | **symbolize** | 4 | 664.99 | 9.593135 | 🟢 medium — moderately distinctive |
| 2120 | **hindu** | 4 | 664.99 | 9.593135 | 🟢 medium — moderately distinctive |
| 2121 | **lineages** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive |
| 2122 | **defects** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive |
| 2123 | **conceptualization** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive |
| 2124 | **circumstantial** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive |
| 2125 | **stains** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive |
| 2126 | **assimilate** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive |
| 2127 | **poisoned** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive |
| 2128 | **nails** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive |
| 2129 | **hallucinations** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive |
| 2130 | **drown** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive |
| 2131 | **joys** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive |
| 2132 | **pointless** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive |
| 2133 | **srona** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive |
| 2134 | **grasp** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive |
| 2135 | **spoil** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive |
| 2136 | **diligent** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive |
| 2137 | **beside** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive |
| 2138 | **cushions** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive |
| 2139 | **entrusted** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive |
| 2140 | **generations** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive |
| 2141 | **samye** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive |
| 2142 | **con** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive |
| 2143 | **stances** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive |
| 2144 | **joyous** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive |
| 2145 | **exclaimed** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive |
| 2146 | **wandering** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive |
| 2147 | **shepherd** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive |
| 2148 | **infatuation** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive |
| 2149 | **procrastination** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive |
| 2150 | **renounced** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive |
| 2151 | **unshakeable** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive |
| 2152 | **universes** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive |
| 2153 | **inanimate** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive |
| 2154 | **gyaltsen** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive |
| 2155 | **fleeting** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive |
| 2156 | **footsteps** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive |
| 2157 | **suns** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive |
| 2158 | **spears** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive |
| 2159 | **arhats** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive |
| 2160 | **ghost** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive |
| 2161 | **gaze** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive |
| 2162 | **isvara** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive |
| 2163 | **thirty-seven** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive |
| 2164 | **ganges** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive |
| 2165 | **miraculously** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive |
| 2166 | **clenched** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive |
| 2167 | **pillow** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive |
| 2168 | **asuras** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive |
| 2169 | **uncle** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive |
| 2170 | **robbers** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive |
| 2171 | **sadness** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive |
| 2172 | **flock** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive |
| 2173 | **earnestly** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive |
| 2174 | **geshes** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive |
| 2175 | **sang** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive |
| 2176 | **potowa** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive |
| 2177 | **armour** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive |
| 2178 | **impervious** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive |
| 2179 | **robe** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive |
| 2180 | **fills** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive |
| 2181 | **revered** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive |
| 2182 | **bent** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive |
| 2183 | **embers** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive |
| 2184 | **hammers** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive |
| 2185 | **joyful** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive |
| 2186 | **grabbed** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive |
| 2187 | **crawling** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive |
| 2188 | **chastity** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive |
| 2189 | **gyalpo** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive |
| 2190 | **yeshe** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive |
| 2191 | **tsogyal** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive |
| 2192 | **selves** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive |
| 2193 | **kasyapa** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive |
| 2194 | **shang** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive |
| 2195 | **sensations** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive |
| 2196 | **chaff** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive |
| 2197 | **ignorant** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive |
| 2198 | **pearls** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive |
| 2199 | **affliction** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive |
| 2200 | **tortured** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive |
| 2201 | **lambs** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive |
| 2202 | **joints** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive |
| 2203 | **enjoyment** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive |
| 2204 | **wrinkles** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive |
| 2205 | **yogis** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive |
| 2206 | **terrified** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive |
| 2207 | **limitless** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive |
| 2208 | **adversaries** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive |
| 2209 | **wolves** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive |
| 2210 | **frustrating** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive |
| 2211 | **grateful** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive |
| 2212 | **daughters** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive |
| 2213 | **smiling** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive |
| 2214 | **transmigration** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive |
| 2215 | **garlands** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive |
| 2216 | **cousin** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive |
| 2217 | **surpasses** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive |
| 2218 | **obeyed** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive |
| 2219 | **wouldn** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive |
| 2220 | **evils** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive |
| 2221 | **beast** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive |
| 2222 | **householders** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive |
| 2223 | **attainments** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive |
| 2224 | **lifetimes** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive |
| 2225 | **treasures** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive |
| 2226 | **amassed** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive |
| 2227 | **spearman** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive |
| 2228 | **purnakasyapa** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive |
| 2229 | **ravati** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive |
| 2230 | **curd** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive |
| 2231 | **dwells** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive |
| 2232 | **unerringly** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive |
| 2233 | **reflections** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive |
| 2234 | **emulating** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive |
| 2235 | **versed** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive |
| 2236 | **visions** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive |
| 2237 | **yours** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive |
| 2238 | **ingratitude** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive |
| 2239 | **ment** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive |
| 2240 | **aversion** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive |
| 2241 | **laughter** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive |
| 2242 | **swan** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive |
| 2243 | **virtues** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive |
| 2244 | **clay** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive |
| 2245 | **meditates** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive |
| 2246 | **hip** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive |
| 2247 | **empow** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive |
| 2248 | **adamantine** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive |
| 2249 | **conferred** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive |
| 2250 | **litas** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive |
| 2251 | **cleanse** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive |
| 2252 | **eagerness** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive |
| 2253 | **unfailing** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive |
| 2254 | **dough** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive |
| 2255 | **essences** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive |
| 2256 | **consort** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive |
| 2257 | **protuberance** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive |
| 2258 | **befall** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive |
| 2259 | **adversity** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive |
| 2260 | **diligently** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive |
| 2261 | **bonpos** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive |
| 2262 | **perna** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive |
| 2263 | **feasts** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive |
| 2264 | **subjugate** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive |
| 2265 | **alas** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive |
| 2266 | **nostrils** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive |
| 2267 | **fortress** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive |
| 2268 | **supernatural** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive |
| 2269 | **khampa** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive |
| 2270 | **dwelling** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive |
| 2271 | **mafijusri** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive |
| 2272 | **kar** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive |
| 2273 | **maitriyogi** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive |
| 2274 | **rohita** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive |
| 2275 | **marici** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive |
| 2276 | **emotion** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive |
| 2277 | **passion** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive |
| 2278 | **rinchen** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive |
| 2279 | **ego-clinging** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive |
| 2280 | **cleansed** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive |
| 2281 | **emanates** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive |
| 2282 | **imagining** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive |
| 2283 | **conceptual** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive |
| 2284 | **innate** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive |
| 2285 | **lady** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive |
| 2286 | **perceiving** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive |
| 2287 | **worn** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive |
| 2288 | **damchen** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive |
| 2289 | **curved** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive |
| 2290 | **tongues** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive |
| 2291 | **nirmar** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive |
| 2292 | **emaho** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive |
| 2293 | **effortless** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive |
| 2294 | **pisaka** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive |
| 2295 | **vajrapar** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive |
| 2296 | **adhicitta** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive |
| 2297 | **tulkus** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive |
| 2298 | **dzogchen** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive |
| 2299 | **dodrup** | 4 | 664.77 | 9.59 | 🟢 medium — moderately distinctive |
| 2300 | **add** | 7 | 664.06 | 5.474098 | 🟢 medium — moderately distinctive |
| 2301 | **join** | 6 | 662.79 | 6.374259 | 🟢 medium — moderately distinctive |
| 2302 | **similarly** | 5 | 662.63 | 7.647225 | 🟢 medium — moderately distinctive |
| 2303 | **enormous** | 5 | 662.63 | 7.647225 | 🟢 medium — moderately distinctive |
| 2304 | **victory** | 5 | 662.63 | 7.647225 | 🟢 medium — moderately distinctive |
| 2305 | **rules** | 7 | 660.17 | 5.442095 | 🟢 medium — moderately distinctive |
| 2306 | **won** | 6 | 658.71 | 6.335039 | 🟢 medium — moderately distinctive |
| 2307 | **city** | 7 | 658.28 | 5.42647 | 🟢 medium — moderately distinctive |
| 2308 | **aim** | 6 | 656.73 | 6.31599 | 🟢 medium — moderately distinctive |
| 2309 | **floor** | 6 | 656.73 | 6.31599 | 🟢 medium — moderately distinctive |
| 2310 | **consisting** | 5 | 656.65 | 7.578232 | 🟢 medium — moderately distinctive |
| 2311 | **lasting** | 5 | 656.65 | 7.578232 | 🟢 medium — moderately distinctive |
| 2312 | **watching** | 5 | 656.65 | 7.578232 | 🟢 medium — moderately distinctive |
| 2313 | **rank** | 5 | 656.65 | 7.578232 | 🟢 medium — moderately distinctive |
| 2314 | **directed** | 5 | 656.65 | 7.578232 | 🟢 medium — moderately distinctive |
| 2315 | **suitable** | 5 | 651.05 | 7.513694 | 🟢 medium — moderately distinctive |
| 2316 | **rule** | 6 | 651.00 | 6.260931 | 🟢 medium — moderately distinctive |
| 2317 | **starts** | 6 | 649.16 | 6.243231 | 🟢 medium — moderately distinctive |
| 2318 | **fresh** | 6 | 647.36 | 6.225839 | 🟢 medium — moderately distinctive |
| 2319 | **reached** | 8 | 645.37 | 4.655071 | 🟢 medium — moderately distinctive |
| 2320 | **types** | 5 | 640.85 | 7.395911 | 🟢 medium — moderately distinctive |
| 2321 | **applies** | 5 | 640.85 | 7.395911 | 🟢 medium — moderately distinctive |
| 2322 | **winds** | 5 | 640.85 | 7.395911 | 🟢 medium — moderately distinctive |
| 2323 | **consist** | 5 | 640.85 | 7.395911 | 🟢 medium — moderately distinctive |
| 2324 | **related** | 7 | 640.79 | 5.282336 | 🟢 medium — moderately distinctive |
| 2325 | **almost** | 7 | 639.18 | 5.269003 | 🟢 medium — moderately distinctive |
| 2326 | **running** | 6 | 637.12 | 6.127399 | 🟢 medium — moderately distinctive |
| 2327 | **middling** | 4 | 636.88 | 9.18767 | 🟢 medium — moderately distinctive |
| 2328 | **swallowed** | 4 | 636.88 | 9.18767 | 🟢 medium — moderately distinctive |
| 2329 | **phrase** | 4 | 636.88 | 9.18767 | 🟢 medium — moderately distinctive |
| 2330 | **mistaken** | 4 | 636.88 | 9.18767 | 🟢 medium — moderately distinctive |
| 2331 | **deprived** | 4 | 636.88 | 9.18767 | 🟢 medium — moderately distinctive |
| 2332 | **mat** | 4 | 636.88 | 9.18767 | 🟢 medium — moderately distinctive |
| 2333 | **mould** | 4 | 636.88 | 9.18767 | 🟢 medium — moderately distinctive |
| 2334 | **array** | 4 | 636.88 | 9.18767 | 🟢 medium — moderately distinctive |
| 2335 | **irrelevant** | 4 | 636.88 | 9.18767 | 🟢 medium — moderately distinctive |
| 2336 | **skies** | 4 | 636.88 | 9.18767 | 🟢 medium — moderately distinctive |
| 2337 | **separated** | 4 | 636.88 | 9.18767 | 🟢 medium — moderately distinctive |
| 2338 | **persistently** | 4 | 636.88 | 9.18767 | 🟢 medium — moderately distinctive |
| 2339 | **tsang** | 4 | 636.88 | 9.18767 | 🟢 medium — moderately distinctive |
| 2340 | **loses** | 4 | 636.88 | 9.18767 | 🟢 medium — moderately distinctive |
| 2341 | **mistakes** | 4 | 636.88 | 9.18767 | 🟢 medium — moderately distinctive |
| 2342 | **verbal** | 4 | 636.88 | 9.18767 | 🟢 medium — moderately distinctive |
| 2343 | **blows** | 4 | 636.88 | 9.18767 | 🟢 medium — moderately distinctive |
| 2344 | **lightly** | 4 | 636.88 | 9.18767 | 🟢 medium — moderately distinctive |
| 2345 | **malaya** | 4 | 636.88 | 9.18767 | 🟢 medium — moderately distinctive |
| 2346 | **perfume** | 4 | 636.88 | 9.18767 | 🟢 medium — moderately distinctive |
| 2347 | **characteristics** | 4 | 636.88 | 9.18767 | 🟢 medium — moderately distinctive |
| 2348 | **observe** | 4 | 636.88 | 9.18767 | 🟢 medium — moderately distinctive |
| 2349 | **interrupt** | 4 | 636.88 | 9.18767 | 🟢 medium — moderately distinctive |
| 2350 | **protecting** | 5 | 636.16 | 7.341843 | 🟢 medium — moderately distinctive |
| 2351 | **merely** | 5 | 636.16 | 7.341843 | 🟢 medium — moderately distinctive |
| 2352 | **scrap** | 5 | 636.16 | 7.341843 | 🟢 medium — moderately distinctive |
| 2353 | **stick** | 5 | 636.16 | 7.341843 | 🟢 medium — moderately distinctive |
| 2354 | **conclude** | 5 | 636.16 | 7.341843 | 🟢 medium — moderately distinctive |
| 2355 | **connection** | 6 | 635.51 | 6.111895 | 🟢 medium — moderately distinctive |
| 2356 | **major** | 10 | 634.89 | 3.663546 | 🟢 medium — moderately distinctive |
| 2357 | **soft** | 6 | 632.36 | 6.08159 | 🟢 medium — moderately distinctive |
| 2358 | **distance** | 5 | 631.72 | 7.29055 | 🟢 medium — moderately distinctive |
| 2359 | **asks** | 5 | 631.72 | 7.29055 | 🟢 medium — moderately distinctive |
| 2360 | **pleased** | 5 | 631.72 | 7.29055 | 🟢 medium — moderately distinctive |
| 2361 | **month** | 10 | 631.01 | 3.641191 | 🟢 medium — moderately distinctive |
| 2362 | **developed** | 6 | 630.82 | 6.066775 | 🟢 medium — moderately distinctive |
| 2363 | **build** | 6 | 629.30 | 6.052176 | 🟢 medium — moderately distinctive |
| 2364 | **satisfy** | 5 | 627.49 | 7.24176 | 🟢 medium — moderately distinctive |
| 2365 | **puts** | 5 | 623.46 | 7.19524 | 🟢 medium — moderately distinctive |
| 2366 | **continuous** | 5 | 623.46 | 7.19524 | 🟢 medium — moderately distinctive |
| 2367 | **drops** | 5 | 623.46 | 7.19524 | 🟢 medium — moderately distinctive |
| 2368 | **ties** | 5 | 619.61 | 7.150788 | 🟢 medium — moderately distinctive |
| 2369 | **hoping** | 5 | 619.61 | 7.150788 | 🟢 medium — moderately distinctive |
| 2370 | **hit** | 7 | 618.54 | 5.098897 | 🟢 medium — moderately distinctive |
| 2371 | **daily** | 7 | 617.19 | 5.087785 | 🟢 medium — moderately distinctive |
| 2372 | **counting** | 4 | 616.94 | 8.899988 | 🟢 medium — moderately distinctive |
| 2373 | **inward** | 4 | 616.94 | 8.899988 | 🟢 medium — moderately distinctive |
| 2374 | **fierce** | 4 | 616.94 | 8.899988 | 🟢 medium — moderately distinctive |
| 2375 | **drag** | 4 | 616.94 | 8.899988 | 🟢 medium — moderately distinctive |
| 2376 | **penetrate** | 4 | 616.94 | 8.899988 | 🟢 medium — moderately distinctive |
| 2377 | **temples** | 4 | 616.94 | 8.899988 | 🟢 medium — moderately distinctive |
| 2378 | **pillar** | 4 | 616.94 | 8.899988 | 🟢 medium — moderately distinctive |
| 2379 | **condemned** | 4 | 616.94 | 8.899988 | 🟢 medium — moderately distinctive |
| 2380 | **abundance** | 4 | 616.94 | 8.899988 | 🟢 medium — moderately distinctive |
| 2381 | **prosperity** | 4 | 616.94 | 8.899988 | 🟢 medium — moderately distinctive |
| 2382 | **sat** | 4 | 616.94 | 8.899988 | 🟢 medium — moderately distinctive |
| 2383 | **achievements** | 4 | 616.94 | 8.899988 | 🟢 medium — moderately distinctive |
| 2384 | **aspect** | 4 | 616.94 | 8.899988 | 🟢 medium — moderately distinctive |
| 2385 | **eradicate** | 4 | 616.94 | 8.899988 | 🟢 medium — moderately distinctive |
| 2386 | **obtaining** | 5 | 615.92 | 7.108229 | 🟢 medium — moderately distinctive |
| 2387 | **determined** | 6 | 612.63 | 5.891833 | 🟢 medium — moderately distinctive |
| 2388 | **degree** | 5 | 608.99 | 7.028186 | 🟢 medium — moderately distinctive |
| 2389 | **prepare** | 5 | 608.99 | 7.028186 | 🟢 medium — moderately distinctive |
| 2390 | **protected** | 5 | 608.99 | 7.028186 | 🟢 medium — moderately distinctive |
| 2391 | **eastern** | 6 | 608.85 | 5.855466 | 🟢 medium — moderately distinctive |
| 2392 | **step** | 6 | 607.61 | 5.843631 | 🟢 medium — moderately distinctive |
| 2393 | **generate** | 5 | 605.72 | 6.990446 | 🟢 medium — moderately distinctive |
| 2394 | **leading** | 7 | 605.08 | 4.987965 | 🟢 medium — moderately distinctive |
| 2395 | **corresponding** | 5 | 602.56 | 6.954078 | 🟢 medium — moderately distinctive |
| 2396 | **contact** | 5 | 602.56 | 6.954078 | 🟢 medium — moderately distinctive |
| 2397 | **motivated** | 4 | 601.47 | 8.676844 | 🟢 medium — moderately distinctive |
| 2398 | **absent** | 4 | 601.47 | 8.676844 | 🟢 medium — moderately distinctive |
| 2399 | **arriving** | 4 | 601.47 | 8.676844 | 🟢 medium — moderately distinctive |
| 2400 | **remind** | 4 | 601.47 | 8.676844 | 🟢 medium — moderately distinctive |
| 2401 | **tip** | 4 | 601.47 | 8.676844 | 🟢 medium — moderately distinctive |
| 2402 | **collection** | 4 | 601.47 | 8.676844 | 🟢 medium — moderately distinctive |
| 2403 | **breathing** | 4 | 601.47 | 8.676844 | 🟢 medium — moderately distinctive |
| 2404 | **casting** | 4 | 601.47 | 8.676844 | 🟢 medium — moderately distinctive |
| 2405 | **walls** | 4 | 601.47 | 8.676844 | 🟢 medium — moderately distinctive |
| 2406 | **washed** | 4 | 601.47 | 8.676844 | 🟢 medium — moderately distinctive |
| 2407 | **garments** | 4 | 601.47 | 8.676844 | 🟢 medium — moderately distinctive |
| 2408 | **exhaust** | 4 | 601.47 | 8.676844 | 🟢 medium — moderately distinctive |
| 2409 | **gate** | 4 | 601.47 | 8.676844 | 🟢 medium — moderately distinctive |
| 2410 | **ceremony** | 4 | 601.47 | 8.676844 | 🟢 medium — moderately distinctive |
| 2411 | **interruption** | 4 | 601.47 | 8.676844 | 🟢 medium — moderately distinctive |
| 2412 | **chen** | 4 | 601.47 | 8.676844 | 🟢 medium — moderately distinctive |
| 2413 | **drawn** | 5 | 599.52 | 6.918987 | 🟢 medium — moderately distinctive |
| 2414 | **mixed** | 5 | 599.52 | 6.918987 | 🟢 medium — moderately distinctive |
| 2415 | **progress** | 6 | 599.39 | 5.764494 | 🟢 medium — moderately distinctive |
| 2416 | **spot** | 6 | 598.26 | 5.753683 | 🟢 medium — moderately distinctive |
| 2417 | **runs** | 5 | 596.59 | 6.885085 | 🟢 medium — moderately distinctive |
| 2418 | **content** | 5 | 596.59 | 6.885085 | 🟢 medium — moderately distinctive |
| 2419 | **fight** | 5 | 593.75 | 6.852295 | 🟢 medium — moderately distinctive |
| 2420 | **succeed** | 5 | 593.75 | 6.852295 | 🟢 medium — moderately distinctive |
| 2421 | **facing** | 5 | 593.75 | 6.852295 | 🟢 medium — moderately distinctive |
| 2422 | **term** | 7 | 593.52 | 4.892655 | 🟢 medium — moderately distinctive |
| 2423 | **held** | 8 | 591.67 | 4.267689 | 🟢 medium — moderately distinctive |
| 2424 | **sour** | 5 | 590.99 | 6.820546 | 🟢 medium — moderately distinctive |
| 2425 | **basic** | 6 | 589.68 | 5.671162 | 🟢 medium — moderately distinctive |
| 2426 | **burst** | 4 | 588.83 | 8.494523 | 🟢 medium — moderately distinctive |
| 2427 | **castle** | 4 | 588.83 | 8.494523 | 🟢 medium — moderately distinctive |
| 2428 | **respects** | 4 | 588.83 | 8.494523 | 🟢 medium — moderately distinctive |
| 2429 | **odds** | 4 | 588.83 | 8.494523 | 🟢 medium — moderately distinctive |
| 2430 | **delighted** | 4 | 588.83 | 8.494523 | 🟢 medium — moderately distinctive |
| 2431 | **filling** | 4 | 588.83 | 8.494523 | 🟢 medium — moderately distinctive |
| 2432 | **shoot** | 4 | 588.83 | 8.494523 | 🟢 medium — moderately distinctive |
| 2433 | **messenger** | 4 | 588.83 | 8.494523 | 🟢 medium — moderately distinctive |
| 2434 | **vessel** | 5 | 585.74 | 6.759922 | 🟢 medium — moderately distinctive |
| 2435 | **answer** | 5 | 585.74 | 6.759922 | 🟢 medium — moderately distinctive |
| 2436 | **autumn** | 5 | 585.74 | 6.759922 | 🟢 medium — moderately distinctive |
| 2437 | **holder** | 5 | 583.23 | 6.730934 | 🟢 medium — moderately distinctive |
| 2438 | **adverse** | 5 | 580.79 | 6.702763 | 🟢 medium — moderately distinctive |
| 2439 | **easier** | 5 | 580.79 | 6.702763 | 🟢 medium — moderately distinctive |
| 2440 | **strike** | 6 | 579.86 | 5.576752 | 🟢 medium — moderately distinctive |
| 2441 | **notice** | 5 | 578.41 | 6.675364 | 🟢 medium — moderately distinctive |
| 2442 | **upper** | 5 | 578.41 | 6.675364 | 🟢 medium — moderately distinctive |
| 2443 | **errors** | 4 | 578.15 | 8.340372 | 🟢 medium — moderately distinctive |
| 2444 | **diseases** | 4 | 578.15 | 8.340372 | 🟢 medium — moderately distinctive |
| 2445 | **upset** | 4 | 578.15 | 8.340372 | 🟢 medium — moderately distinctive |
| 2446 | **refuse** | 4 | 578.15 | 8.340372 | 🟢 medium — moderately distinctive |
| 2447 | **gateway** | 4 | 578.15 | 8.340372 | 🟢 medium — moderately distinctive |
| 2448 | **expressing** | 4 | 578.15 | 8.340372 | 🟢 medium — moderately distinctive |
| 2449 | **goods** | 7 | 574.19 | 4.733323 | 🟢 medium — moderately distinctive |
| 2450 | **final** | 7 | 571.87 | 4.714128 | 🟢 medium — moderately distinctive |
| 2451 | **owners** | 5 | 569.52 | 6.57271 | 🟢 medium — moderately distinctive |
| 2452 | **livestock** | 5 | 569.52 | 6.57271 | 🟢 medium — moderately distinctive |
| 2453 | **insect** | 4 | 568.89 | 8.206841 | 🟢 medium — moderately distinctive |
| 2454 | **fruits** | 4 | 568.89 | 8.206841 | 🟢 medium — moderately distinctive |
| 2455 | **personally** | 4 | 568.89 | 8.206841 | 🟢 medium — moderately distinctive |
| 2456 | **ita** | 4 | 568.89 | 8.206841 | 🟢 medium — moderately distinctive |
| 2457 | **crystal** | 4 | 568.89 | 8.206841 | 🟢 medium — moderately distinctive |
| 2458 | **studying** | 5 | 565.39 | 6.525082 | 🟢 medium — moderately distinctive |
| 2459 | **country** | 7 | 563.40 | 4.644375 | 🟢 medium — moderately distinctive |
| 2460 | **faces** | 5 | 561.45 | 6.47962 | 🟢 medium — moderately distinctive |
| 2461 | **stopped** | 5 | 561.45 | 6.47962 | 🟢 medium — moderately distinctive |
| 2462 | **discouraged** | 4 | 560.73 | 8.089058 | 🟢 medium — moderately distinctive |
| 2463 | **era** | 4 | 560.73 | 8.089058 | 🟢 medium — moderately distinctive |
| 2464 | **anywhere** | 4 | 560.73 | 8.089058 | 🟢 medium — moderately distinctive |
| 2465 | **destined** | 4 | 560.73 | 8.089058 | 🟢 medium — moderately distinctive |
| 2466 | **popularity** | 4 | 560.73 | 8.089058 | 🟢 medium — moderately distinctive |
| 2467 | **playing** | 4 | 560.73 | 8.089058 | 🟢 medium — moderately distinctive |
| 2468 | **performing** | 4 | 560.73 | 8.089058 | 🟢 medium — moderately distinctive |
| 2469 | **spreading** | 4 | 560.73 | 8.089058 | 🟢 medium — moderately distinctive |
| 2470 | **desirable** | 4 | 560.73 | 8.089058 | 🟢 medium — moderately distinctive |
| 2471 | **shown** | 5 | 559.55 | 6.457641 | 🟢 medium — moderately distinctive |
| 2472 | **pushed** | 5 | 559.55 | 6.457641 | 🟢 medium — moderately distinctive |
| 2473 | **depend** | 5 | 555.86 | 6.415081 | 🟢 medium — moderately distinctive |
| 2474 | **reveal** | 4 | 553.42 | 7.983697 | 🟢 medium — moderately distinctive |
| 2475 | **shot** | 4 | 553.42 | 7.983697 | 🟢 medium — moderately distinctive |
| 2476 | **passes** | 4 | 553.42 | 7.983697 | 🟢 medium — moderately distinctive |
| 2477 | **behalf** | 5 | 552.32 | 6.374259 | 🟢 medium — moderately distinctive |
| 2478 | **eventually** | 5 | 547.27 | 6.31599 | 🟢 medium — moderately distinctive |
| 2479 | **relying** | 4 | 546.82 | 7.888387 | 🟢 medium — moderately distinctive |
| 2480 | **simultaneously** | 4 | 546.82 | 7.888387 | 🟢 medium — moderately distinctive |
| 2481 | **visiting** | 4 | 546.82 | 7.888387 | 🟢 medium — moderately distinctive |
| 2482 | **demanding** | 4 | 546.82 | 7.888387 | 🟢 medium — moderately distinctive |
| 2483 | **saved** | 4 | 546.82 | 7.888387 | 🟢 medium — moderately distinctive |
| 2484 | **insisted** | 4 | 546.82 | 7.888387 | 🟢 medium — moderately distinctive |
| 2485 | **town** | 4 | 546.82 | 7.888387 | 🟢 medium — moderately distinctive |
| 2486 | **terms** | 8 | 546.33 | 3.940646 | 🟢 medium — moderately distinctive |
| 2487 | **produced** | 6 | 545.82 | 5.24933 | 🟢 medium — moderately distinctive |
| 2488 | **ensure** | 5 | 542.50 | 6.260931 | 🟢 medium — moderately distinctive |
| 2489 | **conflicting** | 4 | 540.79 | 7.801376 | 🟢 medium — moderately distinctive |
| 2490 | **dangers** | 4 | 540.79 | 7.801376 | 🟢 medium — moderately distinctive |
| 2491 | **neighbouring** | 4 | 540.79 | 7.801376 | 🟢 medium — moderately distinctive |
| 2492 | **mature** | 4 | 540.79 | 7.801376 | 🟢 medium — moderately distinctive |
| 2493 | **tells** | 4 | 540.79 | 7.801376 | 🟢 medium — moderately distinctive |
| 2494 | **foods** | 5 | 537.98 | 6.208745 | 🟢 medium — moderately distinctive |
| 2495 | **swift** | 4 | 535.24 | 7.721333 | 🟢 medium — moderately distinctive |
| 2496 | **rivers** | 4 | 535.24 | 7.721333 | 🟢 medium — moderately distinctive |
| 2497 | **salt** | 4 | 535.24 | 7.721333 | 🟢 medium — moderately distinctive |
| 2498 | **classes** | 4 | 535.24 | 7.721333 | 🟢 medium — moderately distinctive |
| 2499 | **hardship** | 4 | 535.24 | 7.721333 | 🟢 medium — moderately distinctive |
| 2500 | **silver** | 5 | 535.09 | 6.175409 | 🟢 medium — moderately distinctive |
| 2501 | **achieving** | 4 | 530.10 | 7.647225 | 🟢 medium — moderately distinctive |
| 2502 | **avoiding** | 4 | 530.10 | 7.647225 | 🟢 medium — moderately distinctive |
| 2503 | **eager** | 4 | 530.10 | 7.647225 | 🟢 medium — moderately distinctive |
| 2504 | **tomorrow** | 6 | 527.31 | 5.071347 | 🟢 medium — moderately distinctive |
| 2505 | **personal** | 5 | 526.96 | 6.08159 | 🟢 medium — moderately distinctive |
| 2506 | **useful** | 4 | 525.32 | 7.578232 | 🟢 medium — moderately distinctive |
| 2507 | **regardless** | 4 | 525.32 | 7.578232 | 🟢 medium — moderately distinctive |
| 2508 | **rises** | 6 | 524.53 | 5.044535 | 🟢 medium — moderately distinctive |
| 2509 | **royal** | 5 | 524.42 | 6.052176 | 🟢 medium — moderately distinctive |
| 2510 | **sharp** | 6 | 522.35 | 5.023592 | 🟢 medium — moderately distinctive |
| 2511 | **situation** | 6 | 522.35 | 5.023592 | 🟢 medium — moderately distinctive |
| 2512 | **besides** | 4 | 520.84 | 7.513694 | 🟢 medium — moderately distinctive |
| 2513 | **connected** | 4 | 520.84 | 7.513694 | 🟢 medium — moderately distinctive |
| 2514 | **ought** | 4 | 520.84 | 7.513694 | 🟢 medium — moderately distinctive |
| 2515 | **belt** | 4 | 520.84 | 7.513694 | 🟢 medium — moderately distinctive |
| 2516 | **spoke** | 4 | 520.84 | 7.513694 | 🟢 medium — moderately distinctive |
| 2517 | **spring** | 5 | 520.73 | 6.009616 | 🟢 medium — moderately distinctive |
| 2518 | **include** | 7 | 519.49 | 4.282395 | 🟢 medium — moderately distinctive |
| 2519 | **confident** | 5 | 518.35 | 5.982217 | 🟢 medium — moderately distinctive |
| 2520 | **contrary** | 4 | 516.64 | 7.453069 | 🟢 medium — moderately distinctive |
| 2521 | **laid** | 4 | 516.64 | 7.453069 | 🟢 medium — moderately distinctive |
| 2522 | **accordance** | 4 | 516.64 | 7.453069 | 🟢 medium — moderately distinctive |
| 2523 | **snow** | 4 | 516.64 | 7.453069 | 🟢 medium — moderately distinctive |
| 2524 | **promise** | 4 | 516.64 | 7.453069 | 🟢 medium — moderately distinctive |
| 2525 | **bar** | 4 | 516.64 | 7.453069 | 🟢 medium — moderately distinctive |
| 2526 | **cotton** | 5 | 514.91 | 5.942477 | 🟢 medium — moderately distinctive |
| 2527 | **acquired** | 7 | 514.79 | 4.24365 | 🟢 medium — moderately distinctive |
| 2528 | **yes** | 4 | 512.68 | 7.395911 | 🟢 medium — moderately distinctive |
| 2529 | **regard** | 4 | 512.68 | 7.395911 | 🟢 medium — moderately distinctive |
| 2530 | **subsequently** | 4 | 512.68 | 7.395911 | 🟢 medium — moderately distinctive |
| 2531 | **shoe** | 4 | 512.68 | 7.395911 | 🟢 medium — moderately distinctive |
| 2532 | **context** | 4 | 512.68 | 7.395911 | 🟢 medium — moderately distinctive |
| 2533 | **associated** | 5 | 510.52 | 5.891833 | 🟢 medium — moderately distinctive |
| 2534 | **influences** | 4 | 508.93 | 7.341843 | 🟢 medium — moderately distinctive |
| 2535 | **wake** | 4 | 508.93 | 7.341843 | 🟢 medium — moderately distinctive |
| 2536 | **message** | 4 | 508.93 | 7.341843 | 🟢 medium — moderately distinctive |
| 2537 | **millions** | 4 | 508.93 | 7.341843 | 🟢 medium — moderately distinctive |
| 2538 | **steps** | 5 | 507.37 | 5.855466 | 🟢 medium — moderately distinctive |
| 2539 | **plunged** | 4 | 505.38 | 7.29055 | 🟢 medium — moderately distinctive |
| 2540 | **site** | 4 | 505.38 | 7.29055 | 🟢 medium — moderately distinctive |
| 2541 | **quality** | 5 | 502.36 | 5.797646 | 🟢 medium — moderately distinctive |
| 2542 | **unknown** | 4 | 501.99 | 7.24176 | 🟢 medium — moderately distinctive |
| 2543 | **ideas** | 4 | 501.99 | 7.24176 | 🟢 medium — moderately distinctive |
| 2544 | **goals** | 4 | 501.99 | 7.24176 | 🟢 medium — moderately distinctive |
| 2545 | **ship** | 5 | 501.39 | 5.786473 | 🟢 medium — moderately distinctive |
| 2546 | **risk** | 5 | 500.44 | 5.775423 | 🟢 medium — moderately distinctive |
| 2547 | **pay** | 8 | 500.20 | 3.60794 | 🟢 medium — moderately distinctive |
| 2548 | **edge** | 4 | 498.77 | 7.19524 | 🔵 low — common in general English |
| 2549 | **irreversible** | 3 | 498.74 | 9.593135 | 🔵 low — common in general English |
| 2550 | **inclination** | 3 | 498.74 | 9.593135 | 🔵 low — common in general English |
| 2551 | **lifestyles** | 3 | 498.74 | 9.593135 | 🔵 low — common in general English |
| 2552 | **sixty** | 3 | 498.74 | 9.593135 | 🔵 low — common in general English |
| 2553 | **wooden** | 3 | 498.74 | 9.593135 | 🔵 low — common in general English |
| 2554 | **tossed** | 3 | 498.74 | 9.593135 | 🔵 low — common in general English |
| 2555 | **breast** | 3 | 498.74 | 9.593135 | 🔵 low — common in general English |
| 2556 | **flames** | 3 | 498.74 | 9.593135 | 🔵 low — common in general English |
| 2557 | **armoured** | 3 | 498.74 | 9.593135 | 🔵 low — common in general English |
| 2558 | **pierce** | 3 | 498.74 | 9.593135 | 🔵 low — common in general English |
| 2559 | **envy** | 3 | 498.74 | 9.593135 | 🔵 low — common in general English |
| 2560 | **folk** | 3 | 498.74 | 9.593135 | 🔵 low — common in general English |
| 2561 | **uncomfortable** | 3 | 498.74 | 9.593135 | 🔵 low — common in general English |
| 2562 | **spoiled** | 3 | 498.74 | 9.593135 | 🔵 low — common in general English |
| 2563 | **piling** | 3 | 498.74 | 9.593135 | 🔵 low — common in general English |
| 2564 | **fearing** | 3 | 498.74 | 9.593135 | 🔵 low — common in general English |
| 2565 | **stir** | 3 | 498.74 | 9.593135 | 🔵 low — common in general English |
| 2566 | **cracks** | 3 | 498.74 | 9.593135 | 🔵 low — common in general English |
| 2567 | **kills** | 3 | 498.74 | 9.593135 | 🔵 low — common in general English |
| 2568 | **whipped** | 3 | 498.74 | 9.593135 | 🔵 low — common in general English |
| 2569 | **cultivated** | 3 | 498.74 | 9.593135 | 🔵 low — common in general English |
| 2570 | **drowned** | 3 | 498.74 | 9.593135 | 🔵 low — common in general English |
| 2571 | **correctly** | 3 | 498.74 | 9.593135 | 🔵 low — common in general English |
| 2572 | **finger** | 3 | 498.74 | 9.593135 | 🔵 low — common in general English |
| 2573 | **monster** | 3 | 498.74 | 9.593135 | 🔵 low — common in general English |
| 2574 | **sur** | 3 | 498.74 | 9.593135 | 🔵 low — common in general English |
| 2575 | **wounds** | 3 | 498.74 | 9.593135 | 🔵 low — common in general English |
| 2576 | **healed** | 3 | 498.74 | 9.593135 | 🔵 low — common in general English |
| 2577 | **breathe** | 3 | 498.74 | 9.593135 | 🔵 low — common in general English |
| 2578 | **stealing** | 3 | 498.74 | 9.593135 | 🔵 low — common in general English |
| 2579 | **multiply** | 3 | 498.74 | 9.593135 | 🔵 low — common in general English |
| 2580 | **mixing** | 3 | 498.74 | 9.593135 | 🔵 low — common in general English |
| 2581 | **pair** | 3 | 498.74 | 9.593135 | 🔵 low — common in general English |
| 2582 | **elder** | 3 | 498.74 | 9.593135 | 🔵 low — common in general English |
| 2583 | **handful** | 3 | 498.74 | 9.593135 | 🔵 low — common in general English |
| 2584 | **snake** | 3 | 498.74 | 9.593135 | 🔵 low — common in general English |
| 2585 | **steadfast** | 3 | 498.74 | 9.593135 | 🔵 low — common in general English |
| 2586 | **messages** | 3 | 498.74 | 9.593135 | 🔵 low — common in general English |
| 2587 | **tired** | 3 | 498.74 | 9.593135 | 🔵 low — common in general English |
| 2588 | **furious** | 3 | 498.74 | 9.593135 | 🔵 low — common in general English |
| 2589 | **meth** | 3 | 498.74 | 9.593135 | 🔵 low — common in general English |
| 2590 | **garland** | 3 | 498.74 | 9.593135 | 🔵 low — common in general English |
| 2591 | **robbed** | 3 | 498.74 | 9.593135 | 🔵 low — common in general English |
| 2592 | **chased** | 3 | 498.74 | 9.593135 | 🔵 low — common in general English |
| 2593 | **whack** | 3 | 498.74 | 9.593135 | 🔵 low — common in general English |
| 2594 | **saddle** | 3 | 498.74 | 9.593135 | 🔵 low — common in general English |
| 2595 | **victim** | 3 | 498.74 | 9.593135 | 🔵 low — common in general English |
| 2596 | **crippled** | 3 | 498.74 | 9.593135 | 🔵 low — common in general English |
| 2597 | **plausible** | 3 | 498.74 | 9.593135 | 🔵 low — common in general English |
| 2598 | **wagon** | 3 | 498.74 | 9.593135 | 🔵 low — common in general English |
| 2599 | **hero** | 3 | 498.74 | 9.593135 | 🔵 low — common in general English |
| 2600 | **misfortune** | 3 | 498.74 | 9.593135 | 🔵 low — common in general English |
| 2601 | **dispense** | 3 | 498.74 | 9.593135 | 🔵 low — common in general English |
| 2602 | **unaltered** | 3 | 498.74 | 9.593135 | 🔵 low — common in general English |
| 2603 | **dancing** | 3 | 498.74 | 9.593135 | 🔵 low — common in general English |
| 2604 | **gracious** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2605 | **quintessential** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2606 | **aspirations** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2607 | **copper-coloured** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2608 | **ence** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2609 | **embodies** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2610 | **hevajra** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2611 | **gossip** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2612 | **prac** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2613 | **contempt** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2614 | **flaming** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2615 | **blades** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2616 | **engrossed** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2617 | **stag** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2618 | **elephants** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2619 | **gnawing** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2620 | **labdron** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2621 | **thirsty** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2622 | **vowing** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2623 | **notions** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2624 | **musk-deer** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2625 | **musk** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2626 | **trap** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2627 | **hesitations** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2628 | **parasols** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2629 | **brimming** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2630 | **long-lived** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2631 | **mute** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2632 | **inheriting** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2633 | **pernicious** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2634 | **lha-thothori** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2635 | **nyentsen** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2636 | **alphabet** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2637 | **avalokitdvara** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2638 | **statues** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2639 | **prostitutes** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2640 | **nagas** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2641 | **forty** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2642 | **smrtijnana** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2643 | **wept** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2644 | **sion** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2645 | **meditators** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2646 | **accom** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2647 | **servitude** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2648 | **tightly** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2649 | **brew** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2650 | **surabhibhadra** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2651 | **upright** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2652 | **slept** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2653 | **spittle** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2654 | **evaporate** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2655 | **noose** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2656 | **brilliance** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2657 | **chest** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2658 | **precipices** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2659 | **alight** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2660 | **tsenpo** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2661 | **tsen** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2662 | **belongings** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2663 | **radiance** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2664 | **wrong-doing** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2665 | **breezes** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2666 | **enmity** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2667 | **cheek** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2668 | **murdered** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2669 | **starving** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2670 | **affectionate** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2671 | **couples** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2672 | **tingri** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2673 | **nests** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2674 | **barren** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2675 | **armies** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2676 | **everlasting** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2677 | **relish** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2678 | **laugh** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2679 | **trivial** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2680 | **murder** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2681 | **misery** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2682 | **daughter-in-law** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2683 | **courageously** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2684 | **frauds** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2685 | **thieves** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2686 | **mortal** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2687 | **single-mindedly** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2688 | **delusions** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2689 | **experi** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2690 | **footprints** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2691 | **amassing** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2692 | **greasy** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2693 | **arouses** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2694 | **assimilated** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2695 | **yama** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2696 | **chopped** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2697 | **prongs** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2698 | **agonies** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2699 | **devour** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2700 | **thicket** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2701 | **nuns** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2702 | **lovers** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2703 | **embrace** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2704 | **biting** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2705 | **moun** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2706 | **tains** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2707 | **blisters** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2708 | **lamenting** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2709 | **lingje** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2710 | **uttered** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2711 | **entrails** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2712 | **derge** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2713 | **bounds** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2714 | **intellectually** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2715 | **obsessed** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2716 | **avarice** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2717 | **nose** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2718 | **ugliness** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2719 | **novice** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2720 | **snot** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2721 | **happily** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2722 | **shine** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2723 | **skins** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2724 | **regretting** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2725 | **accumu** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2726 | **leprosy** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2727 | **boils** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2728 | **pregnancy** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2729 | **granny** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2730 | **ugly** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2731 | **insipid** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2732 | **lax** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2733 | **left-overs** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2734 | **unclean** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2735 | **evil-doer** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2736 | **steeped** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2737 | **married** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2738 | **rosary** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2739 | **song** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2740 | **kindly** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2741 | **goddess** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2742 | **disgust** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2743 | **demigods** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2744 | **wish-fulfilling** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2745 | **waking** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2746 | **imagination** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2747 | **one-eyed** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2748 | **affection** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2749 | **mahayana** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2750 | **colours** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2751 | **tear** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2752 | **smile** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2753 | **innocent** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2754 | **benefactor** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2755 | **frogs** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2756 | **streaming** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2757 | **laypeople** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2758 | **phoney** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2759 | **deceive** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2760 | **harshly** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2761 | **robbery** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2762 | **eternalism** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2763 | **nihilism** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2764 | **multicoloured** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2765 | **stole** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2766 | **corresponds** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2767 | **lied** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2768 | **insults** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2769 | **futile** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2770 | **miracles** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2771 | **virudhaka** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2772 | **sakyas** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2773 | **fishermen** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2774 | **strayed** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2775 | **boy** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2776 | **elapatra** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2777 | **miserly** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2778 | **hosts** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2779 | **wholesome** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2780 | **unconscious** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2781 | **ness** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2782 | **navigator** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2783 | **pratimok** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2784 | **brilliant** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2785 | **honours** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2786 | **bathe** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2787 | **dispelling** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2788 | **tainted** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2789 | **arrogance** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2790 | **verbally** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2791 | **accomplishing** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2792 | **prajflaparamita** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2793 | **fatigue** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2794 | **fragrant** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2795 | **possesses** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2796 | **ods** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2797 | **bestow** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2798 | **retinue** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2799 | **splinters** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2800 | **adept** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2801 | **conquest** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2802 | **inexpressible** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2803 | **erment** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2804 | **verses** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2805 | **deceit** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2806 | **kusali** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2807 | **stroke** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2808 | **devadatta** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2809 | **canopy** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2810 | **imbued** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2811 | **yidams** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2812 | **lakinis** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2813 | **purifies** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2814 | **mafijusrimitra** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2815 | **simha** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2816 | **longchen** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2817 | **lattice** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2818 | **cruel** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2819 | **melt** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2820 | **kingdoms** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2821 | **unceasingly** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2822 | **saucers** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2823 | **transgress** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2824 | **afar** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2825 | **malignant** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2826 | **freshly** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2827 | **hind** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2828 | **faintest** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2829 | **awaken** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2830 | **verse** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2831 | **quintessence** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2832 | **panacea** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2833 | **defilements** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2834 | **louse** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2835 | **vallabha** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2836 | **leper** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2837 | **dodepa** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2838 | **cured** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2839 | **risi** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2840 | **omens** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2841 | **transmitting** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2842 | **warmth** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2843 | **tame** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2844 | **indivisible** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2845 | **angulimala** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2846 | **prostrating** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2847 | **petals** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2848 | **adorned** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2849 | **wrist** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2850 | **tva** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2851 | **ornament** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2852 | **sores** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2853 | **tsari** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2854 | **wrists** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2855 | **perfumed** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2856 | **explanatory** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2857 | **mahakasyapa** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2858 | **prasenajit** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2859 | **aperture** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2860 | **demoness** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2861 | **duality** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2862 | **mipham** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2863 | **dissolved** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2864 | **lotus-bud** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2865 | **khatvanga** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2866 | **rejoiced** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2867 | **vaisali** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2868 | **cubit** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2869 | **kutra** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2870 | **tingdzin** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2871 | **santarak** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2872 | **knot** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2873 | **chopel** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2874 | **hik** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2875 | **ejection** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2876 | **orgyen** | 3 | 498.58 | 9.59 | 🔵 low — common in general English |
| 2877 | **rising** | 6 | 498.39 | 4.793221 | 🔵 low — common in general English |
| 2878 | **consequences** | 4 | 495.69 | 7.150788 | 🔵 low — common in general English |
| 2879 | **royalty** | 4 | 495.69 | 7.150788 | 🔵 low — common in general English |
| 2880 | **interest** | 8 | 493.89 | 3.56245 | 🔵 low — common in general English |
| 2881 | **details** | 6 | 493.38 | 4.745019 | 🔵 low — common in general English |
| 2882 | **border** | 4 | 492.74 | 7.108229 | 🔵 low — common in general English |
| 2883 | **absence** | 4 | 492.74 | 7.108229 | 🔵 low — common in general English |
| 2884 | **slowly** | 4 | 492.74 | 7.108229 | 🔵 low — common in general English |
| 2885 | **sri** | 4 | 492.74 | 7.108229 | 🔵 low — common in general English |
| 2886 | **measure** | 5 | 492.26 | 5.681112 | 🔵 low — common in general English |
| 2887 | **opening** | 5 | 491.40 | 5.671162 | 🔵 low — common in general English |
| 2888 | **share** | 10 | 491.11 | 2.83388 | 🔵 low — common in general English |
| 2889 | **developing** | 5 | 490.55 | 5.66131 | 🔵 low — common in general English |
| 2890 | **numbers** | 4 | 489.91 | 7.067407 | 🔵 low — common in general English |
| 2891 | **intelligence** | 4 | 489.91 | 7.067407 | 🔵 low — common in general English |
| 2892 | **emerge** | 4 | 489.91 | 7.067407 | 🔵 low — common in general English |
| 2893 | **load** | 4 | 489.91 | 7.067407 | 🔵 low — common in general English |
| 2894 | **line** | 6 | 488.60 | 4.699034 | 🔵 low — common in general English |
| 2895 | **choice** | 4 | 487.19 | 7.028186 | 🔵 low — common in general English |
| 2896 | **ultimately** | 4 | 484.57 | 6.990446 | 🔵 low — common in general English |
| 2897 | **sustained** | 4 | 484.57 | 6.990446 | 🔵 low — common in general English |
| 2898 | **temporarily** | 4 | 482.05 | 6.954078 | 🔵 low — common in general English |
| 2899 | **fine** | 4 | 479.62 | 6.918987 | 🔵 low — common in general English |
| 2900 | **shooting** | 3 | 477.66 | 9.18767 | 🔵 low — common in general English |
| 2901 | **visual** | 3 | 477.66 | 9.18767 | 🔵 low — common in general English |
| 2902 | **swamp** | 3 | 477.66 | 9.18767 | 🔵 low — common in general English |
| 2903 | **mud** | 3 | 477.66 | 9.18767 | 🔵 low — common in general English |
| 2904 | **attach** | 3 | 477.66 | 9.18767 | 🔵 low — common in general English |
| 2905 | **roof** | 3 | 477.66 | 9.18767 | 🔵 low — common in general English |
| 2906 | **plough** | 3 | 477.66 | 9.18767 | 🔵 low — common in general English |
| 2907 | **worthy** | 3 | 477.66 | 9.18767 | 🔵 low — common in general English |
| 2908 | **disciplined** | 3 | 477.66 | 9.18767 | 🔵 low — common in general English |
| 2909 | **stops** | 3 | 477.66 | 9.18767 | 🔵 low — common in general English |
| 2910 | **stretched** | 3 | 477.66 | 9.18767 | 🔵 low — common in general English |
| 2911 | **magic** | 3 | 477.66 | 9.18767 | 🔵 low — common in general English |
| 2912 | **cardinal** | 3 | 477.66 | 9.18767 | 🔵 low — common in general English |
| 2913 | **sesame** | 3 | 477.66 | 9.18767 | 🔵 low — common in general English |
| 2914 | **isn** | 3 | 477.66 | 9.18767 | 🔵 low — common in general English |
| 2915 | **cheese** | 3 | 477.66 | 9.18767 | 🔵 low — common in general English |
| 2916 | **ragged** | 3 | 477.66 | 9.18767 | 🔵 low — common in general English |
| 2917 | **overcoming** | 3 | 477.66 | 9.18767 | 🔵 low — common in general English |
| 2918 | **theft** | 3 | 477.66 | 9.18767 | 🔵 low — common in general English |
| 2919 | **renouncing** | 3 | 477.66 | 9.18767 | 🔵 low — common in general English |
| 2920 | **severed** | 3 | 477.66 | 9.18767 | 🔵 low — common in general English |
| 2921 | **emperor** | 3 | 477.66 | 9.18767 | 🔵 low — common in general English |
| 2922 | **utmost** | 3 | 477.66 | 9.18767 | 🔵 low — common in general English |
| 2923 | **workable** | 3 | 477.66 | 9.18767 | 🔵 low — common in general English |
| 2924 | **loves** | 3 | 477.66 | 9.18767 | 🔵 low — common in general English |
| 2925 | **resolute** | 3 | 477.66 | 9.18767 | 🔵 low — common in general English |
| 2926 | **hesitation** | 3 | 477.66 | 9.18767 | 🔵 low — common in general English |
| 2927 | **wished** | 3 | 477.66 | 9.18767 | 🔵 low — common in general English |
| 2928 | **willingly** | 3 | 477.66 | 9.18767 | 🔵 low — common in general English |
| 2929 | **lunar** | 3 | 477.66 | 9.18767 | 🔵 low — common in general English |
| 2930 | **shorten** | 3 | 477.66 | 9.18767 | 🔵 low — common in general English |
| 2931 | **repeating** | 3 | 477.66 | 9.18767 | 🔵 low — common in general English |
| 2932 | **openings** | 3 | 477.66 | 9.18767 | 🔵 low — common in general English |
| 2933 | **losing** | 4 | 477.27 | 6.885085 | 🔵 low — common in general English |
| 2934 | **container** | 4 | 477.27 | 6.885085 | 🔵 low — common in general English |
| 2935 | **falls** | 5 | 477.19 | 5.507159 | 🔵 low — common in general English |
| 2936 | **question** | 5 | 477.19 | 5.507159 | 🔵 low — common in general English |
| 2937 | **northern** | 5 | 475.03 | 5.482261 | 🔵 low — common in general English |
| 2938 | **war** | 5 | 475.03 | 5.482261 | 🔵 low — common in general English |
| 2939 | **grant** | 4 | 475.00 | 6.852295 | 🔵 low — common in general English |
| 2940 | **bottom** | 4 | 472.80 | 6.820546 | 🔵 low — common in general English |
| 2941 | **elsewhere** | 4 | 472.80 | 6.820546 | 🔵 low — common in general English |
| 2942 | **criticism** | 4 | 472.80 | 6.820546 | 🔵 low — common in general English |
| 2943 | **reduce** | 6 | 470.10 | 4.521091 | 🔵 low — common in general English |
| 2944 | **remained** | 5 | 469.53 | 5.418748 | 🔵 low — common in general English |
| 2945 | **jumped** | 4 | 468.59 | 6.759922 | 🔵 low — common in general English |
| 2946 | **aims** | 4 | 466.58 | 6.730934 | 🔵 low — common in general English |
| 2947 | **variety** | 4 | 466.58 | 6.730934 | 🔵 low — common in general English |
| 2948 | **ended** | 7 | 465.13 | 3.834233 | 🔵 low — common in general English |
| 2949 | **liquid** | 4 | 464.63 | 6.702763 | 🔵 low — common in general English |
| 2950 | **stands** | 4 | 462.73 | 6.675364 | 🔵 low — common in general English |
| 2951 | **drawing** | 4 | 462.73 | 6.675364 | 🔵 low — common in general English |
| 2952 | **sage** | 3 | 462.71 | 8.899988 | 🔵 low — common in general English |
| 2953 | **images** | 3 | 462.71 | 8.899988 | 🔵 low — common in general English |
| 2954 | **uphold** | 3 | 462.71 | 8.899988 | 🔵 low — common in general English |
| 2955 | **checking** | 3 | 462.71 | 8.899988 | 🔵 low — common in general English |
| 2956 | **compounded** | 3 | 462.71 | 8.899988 | 🔵 low — common in general English |
| 2957 | **thirty** | 3 | 462.71 | 8.899988 | 🔵 low — common in general English |
| 2958 | **lump** | 3 | 462.71 | 8.899988 | 🔵 low — common in general English |
| 2959 | **amongst** | 3 | 462.71 | 8.899988 | 🔵 low — common in general English |
| 2960 | **powdered** | 3 | 462.71 | 8.899988 | 🔵 low — common in general English |
| 2961 | **fathers** | 3 | 462.71 | 8.899988 | 🔵 low — common in general English |
| 2962 | **harmed** | 3 | 462.71 | 8.899988 | 🔵 low — common in general English |
| 2963 | **determines** | 3 | 462.71 | 8.899988 | 🔵 low — common in general English |
| 2964 | **namely** | 3 | 462.71 | 8.899988 | 🔵 low — common in general English |
| 2965 | **drinking** | 3 | 462.71 | 8.899988 | 🔵 low — common in general English |
| 2966 | **shaken** | 3 | 462.71 | 8.899988 | 🔵 low — common in general English |
| 2967 | **tower** | 3 | 462.71 | 8.899988 | 🔵 low — common in general English |
| 2968 | **inspired** | 3 | 462.71 | 8.899988 | 🔵 low — common in general English |
| 2969 | **invoked** | 3 | 462.71 | 8.899988 | 🔵 low — common in general English |
| 2970 | **recognizing** | 3 | 462.71 | 8.899988 | 🔵 low — common in general English |
| 2971 | **pity** | 3 | 462.71 | 8.899988 | 🔵 low — common in general English |
| 2972 | **garment** | 3 | 462.71 | 8.899988 | 🔵 low — common in general English |
| 2973 | **wound** | 3 | 462.71 | 8.899988 | 🔵 low — common in general English |
| 2974 | **connections** | 3 | 462.71 | 8.899988 | 🔵 low — common in general English |
| 2975 | **establishes** | 3 | 462.71 | 8.899988 | 🔵 low — common in general English |
| 2976 | **assembled** | 3 | 462.71 | 8.899988 | 🔵 low — common in general English |
| 2977 | **hook** | 3 | 462.71 | 8.899988 | 🔵 low — common in general English |
| 2978 | **enters** | 3 | 462.71 | 8.899988 | 🔵 low — common in general English |
| 2979 | **profit** | 8 | 461.63 | 3.329737 | 🔵 low — common in general English |
| 2980 | **waters** | 4 | 460.88 | 6.648696 | 🔵 low — common in general English |
| 2981 | **maturity** | 4 | 459.08 | 6.622721 | 🔵 low — common in general English |
| 2982 | **flows** | 4 | 459.08 | 6.622721 | 🔵 low — common in general English |
| 2983 | **wide** | 4 | 457.33 | 6.597403 | 🔵 low — common in general English |
| 2984 | **grown** | 4 | 457.33 | 6.597403 | 🔵 low — common in general English |
| 2985 | **factors** | 5 | 457.13 | 5.275647 | 🔵 low — common in general English |
| 2986 | **provided** | 5 | 456.55 | 5.269003 | 🔵 low — common in general English |
| 2987 | **ministers** | 5 | 455.98 | 5.262402 | 🔵 low — common in general English |
| 2988 | **begins** | 4 | 455.62 | 6.57271 | 🔵 low — common in general English |
| 2989 | **trade** | 8 | 455.18 | 3.283217 | 🔵 low — common in general English |
| 2990 | **gained** | 4 | 453.95 | 6.548613 | 🔵 low — common in general English |
| 2991 | **influence** | 4 | 453.95 | 6.548613 | 🔵 low — common in general English |
| 2992 | **periods** | 5 | 453.73 | 5.236426 | 🔵 low — common in general English |
| 2993 | **falling** | 5 | 453.18 | 5.230037 | 🔵 low — common in general English |
| 2994 | **fundamental** | 4 | 452.31 | 6.525082 | 🔵 low — common in general English |
| 2995 | **meeting** | 7 | 451.56 | 3.722427 | 🔵 low — common in general English |
| 2996 | **contemplate** | 3 | 451.10 | 8.676844 | 🔵 low — common in general English |
| 2997 | **imperative** | 3 | 451.10 | 8.676844 | 🔵 low — common in general English |
| 2998 | **chasing** | 3 | 451.10 | 8.676844 | 🔵 low — common in general English |
| 2999 | **intact** | 3 | 451.10 | 8.676844 | 🔵 low — common in general English |
| 3000 | **sink** | 3 | 451.10 | 8.676844 | 🔵 low — common in general English |
| 3001 | **progressively** | 3 | 451.10 | 8.676844 | 🔵 low — common in general English |
| 3002 | **guarded** | 3 | 451.10 | 8.676844 | 🔵 low — common in general English |
| 3003 | **compiled** | 3 | 451.10 | 8.676844 | 🔵 low — common in general English |
| 3004 | **welfare** | 3 | 451.10 | 8.676844 | 🔵 low — common in general English |
| 3005 | **profoundly** | 3 | 451.10 | 8.676844 | 🔵 low — common in general English |
| 3006 | **deeper** | 3 | 451.10 | 8.676844 | 🔵 low — common in general English |
| 3007 | **roasted** | 3 | 451.10 | 8.676844 | 🔵 low — common in general English |
| 3008 | **sheets** | 3 | 451.10 | 8.676844 | 🔵 low — common in general English |
| 3009 | **thick** | 3 | 451.10 | 8.676844 | 🔵 low — common in general English |
| 3010 | **offensive** | 3 | 451.10 | 8.676844 | 🔵 low — common in general English |
| 3011 | **conditioning** | 3 | 451.10 | 8.676844 | 🔵 low — common in general English |
| 3012 | **explains** | 3 | 451.10 | 8.676844 | 🔵 low — common in general English |
| 3013 | **weighed** | 3 | 451.10 | 8.676844 | 🔵 low — common in general English |
| 3014 | **capture** | 3 | 451.10 | 8.676844 | 🔵 low — common in general English |
| 3015 | **identify** | 4 | 449.16 | 6.47962 | 🔵 low — common in general English |
| 3016 | **peak** | 4 | 449.16 | 6.47962 | 🔵 low — common in general English |
| 3017 | **pursue** | 4 | 447.64 | 6.457641 | 🔵 low — common in general English |
| 3018 | **store** | 4 | 446.15 | 6.436135 | 🔵 low — common in general English |
| 3019 | **defend** | 4 | 446.15 | 6.436135 | 🔵 low — common in general English |
| 3020 | **billion** | 9 | 445.19 | 2.85439 | 🔵 low — common in general English |
| 3021 | **express** | 4 | 443.26 | 6.394462 | 🔵 low — common in general English |
| 3022 | **reasons** | 4 | 443.26 | 6.394462 | 🔵 low — common in general English |
| 3023 | **months** | 7 | 442.82 | 3.650336 | 🔵 low — common in general English |
| 3024 | **collapse** | 4 | 441.86 | 6.374259 | 🔵 low — common in general English |
| 3025 | **music** | 3 | 441.63 | 8.494523 | 🔵 low — common in general English |
| 3026 | **endeavour** | 3 | 441.63 | 8.494523 | 🔵 low — common in general English |
| 3027 | **promises** | 3 | 441.63 | 8.494523 | 🔵 low — common in general English |
| 3028 | **wealthy** | 3 | 441.63 | 8.494523 | 🔵 low — common in general English |
| 3029 | **gates** | 3 | 441.63 | 8.494523 | 🔵 low — common in general English |
| 3030 | **nice** | 3 | 441.63 | 8.494523 | 🔵 low — common in general English |
| 3031 | **character** | 3 | 441.63 | 8.494523 | 🔵 low — common in general English |
| 3032 | **introducing** | 3 | 441.63 | 8.494523 | 🔵 low — common in general English |
| 3033 | **sympathetic** | 3 | 441.63 | 8.494523 | 🔵 low — common in general English |
| 3034 | **unfortunate** | 3 | 441.63 | 8.494523 | 🔵 low — common in general English |
| 3035 | **guards** | 3 | 441.63 | 8.494523 | 🔵 low — common in general English |
| 3036 | **closed** | 5 | 440.85 | 5.087785 | 🔵 low — common in general English |
| 3037 | **nearby** | 4 | 440.49 | 6.354457 | 🔵 low — common in general English |
| 3038 | **attention** | 4 | 440.49 | 6.354457 | 🔵 low — common in general English |
| 3039 | **growing** | 5 | 439.43 | 5.071347 | 🔵 low — common in general English |
| 3040 | **needed** | 5 | 436.65 | 5.039258 | 🔵 low — common in general English |
| 3041 | **covering** | 4 | 436.52 | 6.297298 | 🔵 low — common in general English |
| 3042 | **drove** | 3 | 433.61 | 8.340372 | 🔵 low — common in general English |
| 3043 | **sounds** | 3 | 433.61 | 8.340372 | 🔵 low — common in general English |
| 3044 | **relaxed** | 3 | 433.61 | 8.340372 | 🔵 low — common in general English |
| 3045 | **thanks** | 3 | 433.61 | 8.340372 | 🔵 low — common in general English |
| 3046 | **belonging** | 3 | 433.61 | 8.340372 | 🔵 low — common in general English |
| 3047 | **pig** | 3 | 433.61 | 8.340372 | 🔵 low — common in general English |
| 3048 | **declared** | 5 | 432.20 | 4.987965 | 🔵 low — common in general English |
| 3049 | **extent** | 4 | 431.57 | 6.225839 | 🔵 low — common in general English |
| 3050 | **lift** | 4 | 431.57 | 6.225839 | 🔵 low — common in general English |
| 3051 | **providing** | 4 | 431.57 | 6.225839 | 🔵 low — common in general English |
| 3052 | **began** | 5 | 431.34 | 4.978015 | 🔵 low — common in general English |
| 3053 | **seeking** | 5 | 430.49 | 4.968162 | 🔵 low — common in general English |
| 3054 | **western** | 5 | 429.64 | 4.958406 | 🔵 low — common in general English |
| 3055 | **row** | 4 | 429.22 | 6.191938 | 🔵 low — common in general English |
| 3056 | **near** | 5 | 428.80 | 4.948744 | 🔵 low — common in general English |
| 3057 | **moved** | 4 | 428.07 | 6.175409 | 🔵 low — common in general English |
| 3058 | **showed** | 5 | 426.75 | 4.92499 | 🔵 low — common in general English |
| 3059 | **merits** | 3 | 426.67 | 8.206841 | 🔵 low — common in general English |
| 3060 | **peripheral** | 3 | 426.67 | 8.206841 | 🔵 low — common in general English |
| 3061 | **creates** | 3 | 426.67 | 8.206841 | 🔵 low — common in general English |
| 3062 | **stepping** | 3 | 426.67 | 8.206841 | 🔵 low — common in general English |
| 3063 | **ignore** | 3 | 426.67 | 8.206841 | 🔵 low — common in general English |
| 3064 | **defeated** | 3 | 426.67 | 8.206841 | 🔵 low — common in general English |
| 3065 | **retreat** | 3 | 426.67 | 8.206841 | 🔵 low — common in general English |
| 3066 | **plants** | 4 | 425.84 | 6.143148 | 🔵 low — common in general English |
| 3067 | **extend** | 4 | 425.84 | 6.143148 | 🔵 low — common in general English |
| 3068 | **talk** | 4 | 424.75 | 6.127399 | 🔵 low — common in general English |
| 3069 | **north** | 5 | 423.94 | 4.892655 | 🔵 low — common in general English |
| 3070 | **provides** | 4 | 423.67 | 6.111895 | 🔵 low — common in general English |
| 3071 | **ending** | 5 | 423.55 | 4.88812 | 🔵 low — common in general English |
| 3072 | **remote** | 3 | 420.55 | 8.089058 | 🔵 low — common in general English |
| 3073 | **earliest** | 3 | 420.55 | 8.089058 | 🔵 low — common in general English |
| 3074 | **smooth** | 3 | 420.55 | 8.089058 | 🔵 low — common in general English |
| 3075 | **distorted** | 3 | 420.55 | 8.089058 | 🔵 low — common in general English |
| 3076 | **vary** | 3 | 420.55 | 8.089058 | 🔵 low — common in general English |
| 3077 | **feeding** | 3 | 420.55 | 8.089058 | 🔵 low — common in general English |
| 3078 | **occasion** | 3 | 420.55 | 8.089058 | 🔵 low — common in general English |
| 3079 | **ceased** | 3 | 420.55 | 8.089058 | 🔵 low — common in general English |
| 3080 | **provide** | 5 | 420.47 | 4.85256 | 🔵 low — common in general English |
| 3081 | **hurt** | 4 | 419.53 | 6.052176 | 🔵 low — common in general English |
| 3082 | **stage** | 4 | 418.54 | 6.037787 | 🔵 low — common in general English |
| 3083 | **growth** | 6 | 418.10 | 4.020981 | 🔵 low — common in general English |
| 3084 | **sell** | 6 | 417.90 | 4.019082 | 🔵 low — common in general English |
| 3085 | **decide** | 4 | 417.55 | 6.023602 | 🔵 low — common in general English |
| 3086 | **paying** | 4 | 417.55 | 6.023602 | 🔵 low — common in general English |
| 3087 | **attack** | 4 | 416.58 | 6.009616 | 🔵 low — common in general English |
| 3088 | **buildings** | 3 | 415.07 | 7.983697 | 🔵 low — common in general English |
| 3089 | **loaded** | 3 | 415.07 | 7.983697 | 🔵 low — common in general English |
| 3090 | **inherent** | 3 | 415.07 | 7.983697 | 🔵 low — common in general English |
| 3091 | **troops** | 3 | 415.07 | 7.983697 | 🔵 low — common in general English |
| 3092 | **inevitably** | 3 | 415.07 | 7.983697 | 🔵 low — common in general English |
| 3093 | **crush** | 3 | 415.07 | 7.983697 | 🔵 low — common in general English |
| 3094 | **members** | 5 | 414.27 | 4.780951 | 🔵 low — common in general English |
| 3095 | **condition** | 4 | 412.83 | 5.955549 | 🔵 low — common in general English |
| 3096 | **countries** | 6 | 411.96 | 3.961923 | 🔵 low — common in general English |
| 3097 | **resources** | 5 | 410.81 | 4.741105 | 🔵 low — common in general English |
| 3098 | **access** | 4 | 410.15 | 5.916835 | 🔵 low — common in general English |
| 3099 | **fulfil** | 3 | 410.11 | 7.888387 | 🔵 low — common in general English |
| 3100 | **upside** | 3 | 410.11 | 7.888387 | 🔵 low — common in general English |
| 3101 | **translated** | 3 | 410.11 | 7.888387 | 🔵 low — common in general English |
| 3102 | **practical** | 3 | 410.11 | 7.888387 | 🔵 low — common in general English |
| 3103 | **scattered** | 3 | 410.11 | 7.888387 | 🔵 low — common in general English |
| 3104 | **unlimited** | 3 | 410.11 | 7.888387 | 🔵 low — common in general English |
| 3105 | **approaches** | 3 | 410.11 | 7.888387 | 🔵 low — common in general English |
| 3106 | **provoke** | 3 | 410.11 | 7.888387 | 🔵 low — common in general English |
| 3107 | **undertake** | 3 | 410.11 | 7.888387 | 🔵 low — common in general English |
| 3108 | **minute** | 3 | 410.11 | 7.888387 | 🔵 low — common in general English |
| 3109 | **undertaking** | 3 | 410.11 | 7.888387 | 🔵 low — common in general English |
| 3110 | **ray** | 3 | 410.11 | 7.888387 | 🔵 low — common in general English |
| 3111 | **ease** | 4 | 407.57 | 5.879563 | 🔵 low — common in general English |
| 3112 | **raise** | 5 | 407.17 | 4.699034 | 🔵 low — common in general English |
| 3113 | **count** | 3 | 405.59 | 7.801376 | 🔵 low — common in general English |
| 3114 | **guard** | 3 | 405.59 | 7.801376 | 🔵 low — common in general English |
| 3115 | **bag** | 3 | 405.59 | 7.801376 | 🔵 low — common in general English |
| 3116 | **automatically** | 3 | 405.59 | 7.801376 | 🔵 low — common in general English |
| 3117 | **visited** | 3 | 405.59 | 7.801376 | 🔵 low — common in general English |
| 3118 | **fellow** | 3 | 405.59 | 7.801376 | 🔵 low — common in general English |
| 3119 | **blow** | 3 | 405.59 | 7.801376 | 🔵 low — common in general English |
| 3120 | **moving** | 4 | 405.08 | 5.843631 | 🔵 low — common in general English |
| 3121 | **warned** | 4 | 405.08 | 5.843631 | 🔵 low — common in general English |
| 3122 | **quickly** | 4 | 403.46 | 5.820374 | 🔵 low — common in general English |
| 3123 | **feed** | 4 | 402.67 | 5.808946 | 🔵 low — common in general English |
| 3124 | **resulting** | 4 | 401.89 | 5.797646 | 🔵 low — common in general English |
| 3125 | **merge** | 4 | 401.89 | 5.797646 | 🔵 low — common in general English |
| 3126 | **lakes** | 3 | 401.43 | 7.721333 | 🔵 low — common in general English |
| 3127 | **farmer** | 3 | 401.43 | 7.721333 | 🔵 low — common in general English |
| 3128 | **cool** | 3 | 401.43 | 7.721333 | 🔵 low — common in general English |
| 3129 | **authority** | 4 | 399.59 | 5.764494 | 🔵 low — common in general English |
| 3130 | **explanation** | 3 | 397.58 | 7.647225 | 🔵 low — common in general English |
| 3131 | **furthermore** | 3 | 397.58 | 7.647225 | 🔵 low — common in general English |
| 3132 | **memory** | 3 | 397.58 | 7.647225 | 🔵 low — common in general English |
| 3133 | **happening** | 3 | 397.58 | 7.647225 | 🔵 low — common in general English |
| 3134 | **stayed** | 3 | 397.58 | 7.647225 | 🔵 low — common in general English |
| 3135 | **concept** | 3 | 397.58 | 7.647225 | 🔵 low — common in general English |
| 3136 | **mass** | 3 | 393.99 | 7.578232 | 🔵 low — common in general English |
| 3137 | **generating** | 3 | 393.99 | 7.578232 | 🔵 low — common in general English |
| 3138 | **armed** | 3 | 393.99 | 7.578232 | 🔵 low — common in general English |
| 3139 | **stood** | 4 | 393.81 | 5.681112 | 🔵 low — common in general English |
| 3140 | **decline** | 5 | 393.39 | 4.540079 | 🔵 low — common in general English |
| 3141 | **wanted** | 4 | 393.12 | 5.671162 | 🔵 low — common in general English |
| 3142 | **cost** | 5 | 393.12 | 4.536889 | 🔵 low — common in general English |
| 3143 | **firmly** | 3 | 390.63 | 7.513694 | 🔵 low — common in general English |
| 3144 | **task** | 3 | 390.63 | 7.513694 | 🔵 low — common in general English |
| 3145 | **conjunction** | 3 | 390.63 | 7.513694 | 🔵 low — common in general English |
| 3146 | **mention** | 3 | 390.63 | 7.513694 | 🔵 low — common in general English |
| 3147 | **flood** | 3 | 390.63 | 7.513694 | 🔵 low — common in general English |
| 3148 | **executed** | 3 | 390.63 | 7.513694 | 🔵 low — common in general English |
| 3149 | **violation** | 3 | 390.63 | 7.513694 | 🔵 low — common in general English |
| 3150 | **split** | 5 | 390.40 | 4.505539 | 🔵 low — common in general English |
| 3151 | **representative** | 4 | 389.12 | 5.613454 | 🔵 low — common in general English |
| 3152 | **formed** | 4 | 387.84 | 5.594934 | 🔵 low — common in general English |
| 3153 | **carries** | 3 | 387.48 | 7.453069 | 🔵 low — common in general English |
| 3154 | **pledge** | 3 | 387.48 | 7.453069 | 🔵 low — common in general English |
| 3155 | **manage** | 3 | 387.48 | 7.453069 | 🔵 low — common in general English |
| 3156 | **specific** | 4 | 386.58 | 5.576752 | 🔵 low — common in general English |
| 3157 | **surrounding** | 3 | 384.51 | 7.395911 | 🔵 low — common in general English |
| 3158 | **backs** | 3 | 384.51 | 7.395911 | 🔵 low — common in general English |
| 3159 | **panic** | 3 | 384.51 | 7.395911 | 🔵 low — common in general English |
| 3160 | **repair** | 3 | 384.51 | 7.395911 | 🔵 low — common in general English |
| 3161 | **topped** | 3 | 384.51 | 7.395911 | 🔵 low — common in general English |
| 3162 | **predicted** | 4 | 382.34 | 5.515598 | 🔵 low — common in general English |
| 3163 | **heading** | 3 | 381.70 | 7.341843 | 🔵 low — common in general English |
| 3164 | **placing** | 3 | 381.70 | 7.341843 | 🔵 low — common in general English |
| 3165 | **removed** | 3 | 381.70 | 7.341843 | 🔵 low — common in general English |
| 3166 | **successive** | 3 | 381.70 | 7.341843 | 🔵 low — common in general English |
| 3167 | **crushing** | 3 | 381.70 | 7.341843 | 🔵 low — common in general English |
| 3168 | **progressive** | 3 | 381.70 | 7.341843 | 🔵 low — common in general English |
| 3169 | **violated** | 3 | 381.70 | 7.341843 | 🔵 low — common in general English |
| 3170 | **writing** | 3 | 381.70 | 7.341843 | 🔵 low — common in general English |
| 3171 | **temporary** | 4 | 381.17 | 5.498791 | 🔵 low — common in general English |
| 3172 | **contains** | 3 | 379.03 | 7.29055 | 🔵 low — common in general English |
| 3173 | **counter** | 3 | 379.03 | 7.29055 | 🔵 low — common in general English |
| 3174 | **specifically** | 3 | 379.03 | 7.29055 | 🔵 low — common in general English |
| 3175 | **eliminated** | 3 | 379.03 | 7.29055 | 🔵 low — common in general English |
| 3176 | **cover** | 4 | 376.70 | 5.434252 | 🔵 low — common in general English |
| 3177 | **preventing** | 3 | 376.50 | 7.24176 | 🔵 low — common in general English |
| 3178 | **write** | 3 | 376.50 | 7.24176 | 🔵 low — common in general English |
| 3179 | **half** | 5 | 374.11 | 4.317575 | 🔵 low — common in general English |
| 3180 | **entry** | 3 | 371.77 | 7.150788 | 🔵 low — common in general English |
| 3181 | **introduce** | 3 | 371.77 | 7.150788 | 🔵 low — common in general English |
| 3182 | **argue** | 3 | 369.55 | 7.108229 | 🔵 low — common in general English |
| 3183 | **problem** | 4 | 369.02 | 5.323438 | 🔵 low — common in general English |
| 3184 | **earned** | 4 | 368.53 | 5.316469 | 🔵 low — common in general English |
| 3185 | **serves** | 3 | 367.43 | 7.067407 | 🔵 low — common in general English |
| 3186 | **history** | 3 | 367.43 | 7.067407 | 🔵 low — common in general English |
| 3187 | **assume** | 3 | 365.39 | 7.028186 | 🔵 low — common in general English |
| 3188 | **threaten** | 3 | 365.39 | 7.028186 | 🔵 low — common in general English |
| 3189 | **involve** | 3 | 365.39 | 7.028186 | 🔵 low — common in general English |
| 3190 | **win** | 3 | 363.43 | 6.990446 | 🔵 low — common in general English |
| 3191 | **pick** | 3 | 363.43 | 6.990446 | 🔵 low — common in general English |
| 3192 | **china** | 4 | 362.10 | 5.223687 | 🔵 low — common in general English |
| 3193 | **midday** | 3 | 361.54 | 6.954078 | 🔵 low — common in general English |
| 3194 | **subsequent** | 3 | 361.54 | 6.954078 | 🔵 low — common in general English |
| 3195 | **severely** | 3 | 361.54 | 6.954078 | 🔵 low — common in general English |
| 3196 | **early** | 5 | 361.36 | 4.17039 | 🔵 low — common in general English |
| 3197 | **regions** | 3 | 359.71 | 6.918987 | 🔵 low — common in general English |
| 3198 | **brief** | 3 | 359.71 | 6.918987 | 🔵 low — common in general English |
| 3199 | **ran** | 3 | 359.71 | 6.918987 | 🔵 low — common in general English |
| 3200 | **send** | 3 | 359.71 | 6.918987 | 🔵 low — common in general English |
| 3201 | **local** | 4 | 358.68 | 5.174295 | 🔵 low — common in general English |
| 3202 | **assuming** | 3 | 357.95 | 6.885085 | 🔵 low — common in general English |
| 3203 | **commerce** | 4 | 356.62 | 5.144619 | 🔵 low — common in general English |
| 3204 | **rival** | 3 | 356.25 | 6.852295 | 🔵 low — common in general English |
| 3205 | **arm** | 3 | 356.25 | 6.852295 | 🔵 low — common in general English |
| 3206 | **increasing** | 4 | 355.42 | 5.127227 | 🔵 low — common in general English |
| 3207 | **conflict** | 3 | 354.60 | 6.820546 | 🔵 low — common in general English |
| 3208 | **homes** | 3 | 354.60 | 6.820546 | 🔵 low — common in general English |
| 3209 | **warning** | 3 | 354.60 | 6.820546 | 🔵 low — common in general English |
| 3210 | **resolution** | 3 | 353.00 | 6.789775 | 🔵 low — common in general English |
| 3211 | **item** | 3 | 348.47 | 6.702763 | 🔵 low — common in general English |
| 3212 | **floating** | 3 | 348.47 | 6.702763 | 🔵 low — common in general English |
| 3213 | **environment** | 3 | 348.47 | 6.702763 | 🔵 low — common in general English |
| 3214 | **repayment** | 3 | 348.47 | 6.702763 | 🔵 low — common in general English |
| 3215 | **rains** | 3 | 348.47 | 6.702763 | 🔵 low — common in general English |
| 3216 | **aggressive** | 3 | 348.47 | 6.702763 | 🔵 low — common in general English |
| 3217 | **acting** | 3 | 348.47 | 6.702763 | 🔵 low — common in general English |
| 3218 | **oil** | 6 | 348.32 | 3.34994 | 🔵 low — common in general English |
| 3219 | **allow** | 4 | 347.16 | 5.008168 | 🔵 low — common in general English |
| 3220 | **company** | 8 | 347.14 | 2.503892 | 🔵 low — common in general English |
| 3221 | **province** | 3 | 347.05 | 6.675364 | 🔵 low — common in general English |
| 3222 | **managed** | 3 | 345.66 | 6.648696 | 🔵 low — common in general English |
| 3223 | **changing** | 3 | 345.66 | 6.648696 | 🔵 low — common in general English |
| 3224 | **valley** | 3 | 345.66 | 6.648696 | 🔵 low — common in general English |
| 3225 | **aware** | 3 | 345.66 | 6.648696 | 🔵 low — common in general English |
| 3226 | **plant** | 4 | 344.05 | 4.963272 | 🔵 low — common in general English |
| 3227 | **gain** | 5 | 343.61 | 3.965514 | 🔵 low — common in general English |
| 3228 | **problems** | 4 | 342.38 | 4.939175 | 🔵 low — common in general English |
| 3229 | **arrange** | 3 | 341.71 | 6.57271 | 🔵 low — common in general English |
| 3230 | **slight** | 3 | 341.71 | 6.57271 | 🔵 low — common in general English |
| 3231 | **suffered** | 3 | 341.71 | 6.57271 | 🔵 low — common in general English |
| 3232 | **joined** | 3 | 340.46 | 6.548613 | 🔵 low — common in general English |
| 3233 | **cases** | 3 | 338.04 | 6.502093 | 🔵 low — common in general English |
| 3234 | **apparent** | 3 | 338.04 | 6.502093 | 🔵 low — common in general English |
| 3235 | **pointed** | 3 | 338.04 | 6.502093 | 🔵 low — common in general English |
| 3236 | **customs** | 3 | 336.87 | 6.47962 | 🔵 low — common in general English |
| 3237 | **delivered** | 3 | 336.87 | 6.47962 | 🔵 low — common in general English |
| 3238 | **outcome** | 3 | 336.87 | 6.47962 | 🔵 low — common in general English |
| 3239 | **attacks** | 3 | 335.73 | 6.457641 | 🔵 low — common in general English |
| 3240 | **scale** | 3 | 335.73 | 6.457641 | 🔵 low — common in general English |
| 3241 | **attractive** | 3 | 335.73 | 6.457641 | 🔵 low — common in general English |
| 3242 | **permit** | 3 | 335.73 | 6.457641 | 🔵 low — common in general English |
| 3243 | **adequate** | 3 | 334.61 | 6.436135 | 🔵 low — common in general English |
| 3244 | **favour** | 3 | 334.61 | 6.436135 | 🔵 low — common in general English |
| 3245 | **repeated** | 3 | 334.61 | 6.436135 | 🔵 low — common in general English |
| 3246 | **drive** | 3 | 334.61 | 6.436135 | 🔵 low — common in general English |
| 3247 | **requested** | 3 | 333.52 | 6.415081 | 🔵 low — common in general English |
| 3248 | **citadel** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English |
| 3249 | **bounty** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English |
| 3250 | **prescriptions** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English |
| 3251 | **shelter** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English |
| 3252 | **totality** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English |
| 3253 | **populated** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English |
| 3254 | **languages** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English |
| 3255 | **lights** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English |
| 3256 | **striving** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English |
| 3257 | **render** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English |
| 3258 | **sway** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English |
| 3259 | **pains** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English |
| 3260 | **motives** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English |
| 3261 | **genuinely** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English |
| 3262 | **draught** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English |
| 3263 | **pea** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English |
| 3264 | **encompassing** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English |
| 3265 | **deserves** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English |
| 3266 | **pale** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English |
| 3267 | **warrior** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English |
| 3268 | **landscape** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English |
| 3269 | **prison** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English |
| 3270 | **miserable** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English |
| 3271 | **meagre** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English |
| 3272 | **talent** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English |
| 3273 | **momentary** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English |
| 3274 | **unrelenting** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English |
| 3275 | **axe** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English |
| 3276 | **pretend** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English |
| 3277 | **jar** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English |
| 3278 | **glory** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English |
| 3279 | **reviving** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English |
| 3280 | **screaming** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English |
| 3281 | **sealed** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English |
| 3282 | **boil** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English |
| 3283 | **stabbed** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English |
| 3284 | **cracked** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English |
| 3285 | **boiling** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English |
| 3286 | **deceased** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English |
| 3287 | **organs** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English |
| 3288 | **knives** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English |
| 3289 | **hauled** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English |
| 3290 | **arrogant** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English |
| 3291 | **bits** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English |
| 3292 | **hawks** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English |
| 3293 | **ploughed** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English |
| 3294 | **calves** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English |
| 3295 | **halfway** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English |
| 3296 | **chew** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English |
| 3297 | **clutches** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English |
| 3298 | **collapses** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English |
| 3299 | **haven** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English |
| 3300 | **confers** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English |
| 3301 | **irresistible** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English |
| 3302 | **abyss** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English |
| 3303 | **dress** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English |
| 3304 | **progression** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English |
| 3305 | **feeble** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English |
| 3306 | **secretly** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English |
| 3307 | **prowess** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English |
| 3308 | **renunciation** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English |
| 3309 | **tail** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English |
| 3310 | **exposing** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English |
| 3311 | **insult** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English |
| 3312 | **cheat** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English |
| 3313 | **observation** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English |
| 3314 | **donations** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English |
| 3315 | **bother** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English |
| 3316 | **abstain** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English |
| 3317 | **pleasantly** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English |
| 3318 | **respectful** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English |
| 3319 | **headache** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English |
| 3320 | **saffron** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English |
| 3321 | **dense** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English |
| 3322 | **inherit** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English |
| 3323 | **maturation** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English |
| 3324 | **corrupted** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English |
| 3325 | **needing** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English |
| 3326 | **discrimination** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English |
| 3327 | **embarrassed** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English |
| 3328 | **irritated** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English |
| 3329 | **receptive** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English |
| 3330 | **externally** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English |
| 3331 | **requisite** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English |
| 3332 | **crossroads** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English |
| 3333 | **invoke** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English |
| 3334 | **gems** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English |
| 3335 | **underwent** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English |
| 3336 | **toes** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English |
| 3337 | **angrily** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English |
| 3338 | **remembered** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English |
| 3339 | **melted** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English |
| 3340 | **trains** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English |
| 3341 | **distinctly** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English |
| 3342 | **elaboration** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English |
| 3343 | **flash** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English |
| 3344 | **continuity** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English |
| 3345 | **self-centred** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English |
| 3346 | **indifferent** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English |
| 3347 | **perished** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English |
| 3348 | **beginners** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English |
| 3349 | **nurtured** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English |
| 3350 | **myriad** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English |
| 3351 | **ancestors** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English |
| 3352 | **kicked** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English |
| 3353 | **wrecked** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English |
| 3354 | **avail** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English |
| 3355 | **chariot** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English |
| 3356 | **gifts** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English |
| 3357 | **twenty-three** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English |
| 3358 | **engender** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English |
| 3359 | **tips** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English |
| 3360 | **fore** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English |
| 3361 | **dirt** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English |
| 3362 | **ear** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English |
| 3363 | **aggressor** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English |
| 3364 | **palms** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English |
| 3365 | **observing** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English |
| 3366 | **emptied** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English |
| 3367 | **explanations** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English |
| 3368 | **vibrant** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English |
| 3369 | **phrases** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English |
| 3370 | **revitalize** | 2 | 332.49 | 9.593135 | 🔵 low — common in general English |
| 3371 | **opinion** | 3 | 332.44 | 6.394462 | 🔵 low — common in general English |
| 3372 | **guarantee** | 3 | 332.44 | 6.394462 | 🔵 low — common in general English |
| 3373 | **exhaustion** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3374 | **writings** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3375 | **unerring** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3376 | **miseries** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3377 | **greatness** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3378 | **semblance** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3379 | **dakas** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3380 | **blissful** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3381 | **eternity** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3382 | **visualizations** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3383 | **concealed** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3384 | **upside-down** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3385 | **nomad** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3386 | **savouring** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3387 | **vina** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3388 | **pore** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3389 | **tingling** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3390 | **intently** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3391 | **infernos** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3392 | **razor-sharp** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3393 | **bees** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3394 | **tising** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3395 | **ti-reciters** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3396 | **honest** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3397 | **i-reciters** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3398 | **fruition** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3399 | **sror** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3400 | **taut** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3401 | **inwardly** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3402 | **discour** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3403 | **undervalue** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3404 | **disobeying** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3405 | **treating** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3406 | **elixir** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3407 | **disrespectful** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3408 | **slavery** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3409 | **blankness** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3410 | **inhabiting** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3411 | **tenma** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3412 | **flower-garden** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3413 | **expounding** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3414 | **possessing** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3415 | **immersed** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3416 | **variance** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3417 | **invocations** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3418 | **prophecies** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3419 | **thonmi** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3420 | **sambhota** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3421 | **owo** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3422 | **thadul** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3423 | **yangdul** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3424 | **buddhism** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3425 | **preceptor** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3426 | **unequalled** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3427 | **sfitras** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3428 | **ordained** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3429 | **shone** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3430 | **kind-hearted** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3431 | **delightful** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3432 | **renown** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3433 | **tibetans** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3434 | **manifesting** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3435 | **disappears** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3436 | **devoid** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3437 | **quench** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3438 | **excellence** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3439 | **khu** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3440 | **ngok** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3441 | **stupidity** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3442 | **propensities** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3443 | **glimmer** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3444 | **ensnared** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3445 | **guise** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3446 | **blindly** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3447 | **tinder** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3448 | **oxen** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3449 | **hither** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3450 | **thither** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3451 | **intentionally** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3452 | **surfaces** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3453 | **hurl** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3454 | **neglect** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3455 | **indulging** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3456 | **meditations** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3457 | **ponds** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3458 | **blazes** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3459 | **infernal** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3460 | **disintegrate** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3461 | **legions** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3462 | **wondrous** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3463 | **livelihood** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3464 | **ferociously** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3465 | **breadth** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3466 | **limp** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3467 | **hide** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3468 | **filthy** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3469 | **magnificent** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3470 | **five-fold** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3471 | **emperors** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3472 | **nyatri** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3473 | **dynasty** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3474 | **prize** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3475 | **tall** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3476 | **degenerated** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3477 | **plague** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3478 | **preach** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3479 | **glow** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3480 | **wither** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3481 | **goats** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3482 | **thunderbolt** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3483 | **fearful** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3484 | **behold** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3485 | **nausea** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3486 | **beggary** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3487 | **epidemics** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3488 | **market-day** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3489 | **bicker** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3490 | **monasteries** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3491 | **consecrated** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3492 | **dwelt** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3493 | **cliffs** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3494 | **mandhatri** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3495 | **beats** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3496 | **dandles** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3497 | **buried** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3498 | **erudite** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3499 | **talented** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3500 | **cheats** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3501 | **beget** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3502 | **yearn** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3503 | **aryadeva** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3504 | **crave** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3505 | **phlegm** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3506 | **tusks** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3507 | **kadampa** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3508 | **forgetfulness** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3509 | **transient** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3510 | **lowly** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3511 | **realizations** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3512 | **deathless** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3513 | **flocks** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3514 | **follower** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3515 | **imper** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3516 | **manence** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3517 | **nirvat** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3518 | **pursuits** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3519 | **permeated** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3520 | **ants** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3521 | **fiery** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3522 | **flame** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3523 | **brandishing** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3524 | **phantom** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3525 | **slain** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3526 | **mortars** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3527 | **valleys** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3528 | **ofyama** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3529 | **hell-beings** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3530 | **corre** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3531 | **spond** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3532 | **rounding-up** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3533 | **howling** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3534 | **bronze** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3535 | **sciousness** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3536 | **anus** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3537 | **glowing** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3538 | **subjected** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3539 | **salmali** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3540 | **beaks** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3541 | **razors** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3542 | **mali** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3543 | **hideous** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3544 | **brains** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3545 | **intolerable** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3546 | **groans** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3547 | **voices** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3548 | **lotus-like** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3549 | **blistering** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3550 | **yamdrok** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3551 | **tangtong** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3552 | **glance** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3553 | **venerated** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3554 | **priest** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3555 | **quivering** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3556 | **ribs** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3557 | **babies** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3558 | **slices** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3559 | **gleam** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3560 | **lovely** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3561 | **exemplary** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3562 | **karmapas** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3563 | **shameful** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3564 | **withered** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3565 | **moonlight** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3566 | **lumps** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3567 | **lungs** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3568 | **srot** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3569 | **heir** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3570 | **yelled** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3571 | **dish** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3572 | **jetari** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3573 | **repulsive** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3574 | **wandered** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3575 | **afflict** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3576 | **stinginess** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3577 | **mamo** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3578 | **hallucination** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3579 | **magicians** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3580 | **bum** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3581 | **imaginary** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3582 | **tum** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3583 | **garuc** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3584 | **tigers** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3585 | **leopards** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3586 | **milked** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3587 | **sincerity** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3588 | **dread** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3589 | **wears** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3590 | **mules** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3591 | **disembowelled** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3592 | **ewes** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3593 | **sip** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3594 | **stolen** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3595 | **semen** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3596 | **fetus** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3597 | **precipice** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3598 | **banging** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3599 | **bony** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3600 | **jaws** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3601 | **rubbed** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3602 | **cradle** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3603 | **ripples** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3604 | **inconsequential** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3605 | **vigour** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3606 | **irritable** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3607 | **sings** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3608 | **creep** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3609 | **stalking** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3610 | **hangs** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3611 | **frowns** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3612 | **faded** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3613 | **hallucinate** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3614 | **discomforts** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3615 | **perceives** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3616 | **apparitions** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3617 | **descend** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3618 | **unending** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3619 | **miserliness** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3620 | **charity** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3621 | **hostility** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3622 | **tea-leaves** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3623 | **dishonour** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3624 | **splendidly** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3625 | **nourishing** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3626 | **harness** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3627 | **red-faced** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3628 | **expedition** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3629 | **exhort** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3630 | **distinguishing** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3631 | **ambition** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3632 | **resentment** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3633 | **grabbing** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3634 | **supremely** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3635 | **slopes** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3636 | **suffused** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3637 | **sweat** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3638 | **ceaseless** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3639 | **cesspit** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3640 | **recollection** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3641 | **overjoyed** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3642 | **crackling** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3643 | **hell-realms** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3644 | **transgressed** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3645 | **circumambulate** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3646 | **wits** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3647 | **cherish** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3648 | **excrement** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3649 | **hermitages** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3650 | **contaminate** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3651 | **tsik** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3652 | **astray** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3653 | **headings** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3654 | **predilection** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3655 | **graze** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3656 | **dung** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3657 | **snakes** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3658 | **lice** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3659 | **bride** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3660 | **smacking** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3661 | **ogres** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3662 | **ogre** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3663 | **slaughterer** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3664 | **binds** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3665 | **muzzle** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3666 | **staring** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3667 | **skinned** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3668 | **all-pervading** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3669 | **stove** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3670 | **stealth** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3671 | **plunder** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3672 | **shortcomings** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3673 | **brooding** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3674 | **charlatans** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3675 | **behaving** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3676 | **offensively** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3677 | **singing** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3678 | **songs** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3679 | **distracting** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3680 | **chanting** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3681 | **bonpo** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3682 | **transgression** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3683 | **partake** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3684 | **sixty-two** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3685 | **downhill** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3686 | **sharpness** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3687 | **peacocks** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3688 | **nourishment** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3689 | **sustenance** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3690 | **defile** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3691 | **impulse** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3692 | **affinity** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3693 | **respite** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3694 | **disperse** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3695 | **impoverished** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3696 | **spouse** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3697 | **behaves** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3698 | **reaping** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3699 | **insulted** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3700 | **sin** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3701 | **landscapes** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3702 | **ravines** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3703 | **encounters** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3704 | **wanderings** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3705 | **massacred** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3706 | **parivrajikas** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3707 | **sakya** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3708 | **shrine** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3709 | **shower** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3710 | **nirvar** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3711 | **kashmir** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3712 | **dyeing** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3713 | **sire** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3714 | **thief** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3715 | **kusa** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3716 | **ashota** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3717 | **scolded** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3718 | **serpent** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3719 | **lover** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3720 | **rivalry** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3721 | **pratimo** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3722 | **stained** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3723 | **pebble** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3724 | **pebbles** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3725 | **ripens** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3726 | **conversely** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3727 | **goodness** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3728 | **incarnation** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3729 | **ofvajradhara** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3730 | **me-but** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3731 | **manifestations** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3732 | **cling** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3733 | **evil-doers** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3734 | **firstly** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3735 | **concentrations** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3736 | **tripitaka** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3737 | **riddance** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3738 | **pitakas** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3739 | **ripening** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3740 | **tered** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3741 | **fiefs** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3742 | **puffed** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3743 | **bogus** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3744 | **unthinkingly** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3745 | **attuned** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3746 | **patiently** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3747 | **disci** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3748 | **radiates** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3749 | **similes** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3750 | **sparing** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3751 | **displeasing** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3752 | **anvil** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3753 | **sweeper** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3754 | **rebukes** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3755 | **drank** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3756 | **mara** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3757 | **respectfully** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3758 | **slam** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3759 | **bee** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3760 | **paramount** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3761 | **indivisibly** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3762 | **unite** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3763 | **obeying** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3764 | **profess** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3765 | **fools** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3766 | **pretending** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3767 | **superfluous** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3768 | **rongton** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3769 | **lhaga** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3770 | **trowolung** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3771 | **impurity** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3772 | **imitation** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3773 | **imitate** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3774 | **engraved** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3775 | **wasteland** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3776 | **paramita** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3777 | **venerate** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3778 | **thigh** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3779 | **carriages** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3780 | **preaching** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3781 | **lapis** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3782 | **lazuli** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3783 | **maidens** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3784 | **nine-storey** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3785 | **bamboo** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3786 | **labourers** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3787 | **twenty-four** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3788 | **obscura** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3789 | **awakened** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3790 | **disobey** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3791 | **vikramasila** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3792 | **yungton** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3793 | **sinner** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3794 | **jug** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3795 | **sariwara** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3796 | **shepa** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3797 | **drowning** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3798 | **entrance-way** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3799 | **vivid** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3800 | **relic** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3801 | **kongpo** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3802 | **motivates** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3803 | **five-pronged** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3804 | **brocade** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3805 | **lakini** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3806 | **hooked** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3807 | **hadra** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3808 | **rabjampa** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3809 | **on-and** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3810 | **avalokitesvara-and** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3811 | **rear** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3812 | **encased** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3813 | **outwards** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3814 | **sugatas** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3815 | **yearning** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3816 | **refuges** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3817 | **visnu** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3818 | **springing** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3819 | **glare** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3820 | **hid** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3821 | **manifested** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3822 | **fourfold** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3823 | **paqc** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3824 | **wisdoms** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3825 | **vairocana** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3826 | **beneficent** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3827 | **exhausts** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3828 | **ajatasatru** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3829 | **fury** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3830 | **scoop** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3831 | **enlight** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3832 | **enment** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3833 | **lovingly** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3834 | **jarung** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3835 | **khashor** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3836 | **gentle** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3837 | **despised** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3838 | **novices** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3839 | **summoning** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3840 | **conquer** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3841 | **dungeon** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3842 | **packhorses** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3843 | **pain-you** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3844 | **panting** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3845 | **thrash** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3846 | **sausages** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3847 | **drips** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3848 | **atsaras** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3849 | **relishing** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3850 | **faint** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3851 | **marching** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3852 | **religion** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3853 | **paq** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3854 | **altruistic** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3855 | **lungpa** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3856 | **lhungpa** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3857 | **ings** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3858 | **thenceforth** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3859 | **vasubandhu** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3860 | **departed** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3861 | **feather** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3862 | **unkind** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3863 | **pletely** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3864 | **tarlo** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3865 | **mistress** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3866 | **camel** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3867 | **swim** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3868 | **shawopa** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3869 | **bowls** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3870 | **imponant** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3871 | **shepherds** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3872 | **conceived** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3873 | **eighty-four** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3874 | **harnessed** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3875 | **belonged** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3876 | **jewellers** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3877 | **hem** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3878 | **exquisite** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3879 | **chakshingwa** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3880 | **shangshungpa** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3881 | **feverish** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3882 | **manicuda** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3883 | **dawned** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3884 | **bathed** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3885 | **brighu** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3886 | **sprang** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3887 | **smiles** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3888 | **duly** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3889 | **tigress** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3890 | **beginner** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3891 | **laced** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3892 | **ego** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3893 | **ears** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3894 | **yourselves** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3895 | **armour-like** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3896 | **preoccupations** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3897 | **diparhkara** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3898 | **oars** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3899 | **childish** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3900 | **distrac** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3901 | **lonely** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3902 | **secluded** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3903 | **ascetic** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3904 | **discerning** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3905 | **concen** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3906 | **tration** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3907 | **athagatas** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3908 | **equanimity** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3909 | **spoilt** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3910 | **self-liberation** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3911 | **saraha** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3912 | **dohas** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3913 | **kharak** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3914 | **gomchung** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3915 | **demonic** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3916 | **spiritually** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3917 | **nachung** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3918 | **non-buddhist** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3919 | **imprint** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3920 | **meditator** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3921 | **diminution** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3922 | **small-minded** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3923 | **transgressions** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3924 | **cultivating** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3925 | **hiding** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3926 | **chagme** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3927 | **perverse** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3928 | **pours** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3929 | **venge** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3930 | **orna** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3931 | **appeased** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3932 | **navel** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3933 | **sattva** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3934 | **emanate** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3935 | **canopies** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3936 | **light-rays** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3937 | **vidyadhara** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3938 | **shapkyu** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3939 | **crescent** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3940 | **bindu** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3941 | **nada** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3942 | **ofvajrasattva** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3943 | **cymbals** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3944 | **transgressors** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3945 | **shingkyong** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3946 | **mandalas** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3947 | **tation** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3948 | **sullied** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3949 | **snivakas** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3950 | **downfall** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3951 | **gifted** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3952 | **repetitions** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3953 | **surround** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3954 | **clockwise** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3955 | **multiplying** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3956 | **palaces** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3957 | **multiplied** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3958 | **speck** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3959 | **cleanly** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3960 | **churning** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3961 | **propitiating** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3962 | **ascending** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3963 | **seventy-five** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3964 | **specks** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3965 | **imbibe** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3966 | **iakinis** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3967 | **tara** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3968 | **elemental** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3969 | **fearsome** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3970 | **annihilate** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3971 | **prophesied** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3972 | **goblins** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3973 | **dualistic** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3974 | **core-teaching** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3975 | **fervent** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3976 | **drikung** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3977 | **kyobpa** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3978 | **trekcho** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3979 | **gazing** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3980 | **longingly** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3981 | **skull-drum** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3982 | **hats** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3983 | **charnel-grounds** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3984 | **zahor** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3985 | **symbolizing** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3986 | **mudra** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3987 | **sambhoga** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3988 | **five-coloured** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3989 | **subjugated** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3990 | **luminous** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3991 | **sphere** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3992 | **knees** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3993 | **unfathomable** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3994 | **hypocrisy** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3995 | **truths** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3996 | **intending** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3997 | **entreat** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3998 | **upayoga** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 3999 | **mahayoga** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 4000 | **anuyoga** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 4001 | **ofg** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 4002 | **reat** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 4003 | **lotus-born** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 4004 | **invocation** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 4005 | **beams** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 4006 | **munis** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 4007 | **twenty-eight** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 4008 | **vajrapat** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 4009 | **unfold** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 4010 | **dhanakosa** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 4011 | **sattvavajra** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 4012 | **nine-pointed** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 4013 | **swans** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 4014 | **expanses** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 4015 | **rajahasti** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 4016 | **yamantaka** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 4017 | **acarya** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 4018 | **genyen** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 4019 | **familiarity** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 4020 | **pathway** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 4021 | **mahamudra** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 4022 | **ofvajra** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 4023 | **yogini** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 4024 | **enclosure** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 4025 | **vibrating** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 4026 | **mind-awareness** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 4027 | **kyabje** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 4028 | **kagyu** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 4029 | **gampopa** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 4030 | **instruc** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 4031 | **drunk** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 4032 | **wangpo** | 2 | 332.39 | 9.59 | 🔵 low — common in general English |
| 4033 | **concerning** | 3 | 331.39 | 6.374259 | 🔵 low — common in general English |
| 4034 | **seriously** | 3 | 331.39 | 6.374259 | 🔵 low — common in general English |
| 4035 | **continued** | 4 | 329.74 | 4.756853 | 🔵 low — common in general English |
| 4036 | **requires** | 3 | 329.36 | 6.335039 | 🔵 low — common in general English |
| 4037 | **band** | 3 | 329.36 | 6.335039 | 🔵 low — common in general English |
| 4038 | **directly** | 3 | 329.36 | 6.335039 | 🔵 low — common in general English |
| 4039 | **chinese** | 3 | 328.36 | 6.31599 | 🔵 low — common in general English |
| 4040 | **delay** | 3 | 327.39 | 6.297298 | 🔵 low — common in general English |
| 4041 | **detailed** | 3 | 327.39 | 6.297298 | 🔵 low — common in general English |
| 4042 | **island** | 3 | 326.44 | 6.278949 | 🔵 low — common in general English |
| 4043 | **movement** | 3 | 325.50 | 6.260931 | 🔵 low — common in general English |
| 4044 | **broad** | 3 | 325.50 | 6.260931 | 🔵 low — common in general English |
| 4045 | **hostile** | 3 | 325.50 | 6.260931 | 🔵 low — common in general English |
| 4046 | **debate** | 3 | 325.50 | 6.260931 | 🔵 low — common in general English |
| 4047 | **status** | 3 | 324.58 | 6.243231 | 🔵 low — common in general English |
| 4048 | **shows** | 3 | 323.68 | 6.225839 | 🔵 low — common in general English |
| 4049 | **quarters** | 3 | 322.79 | 6.208745 | 🔵 low — common in general English |
| 4050 | **closely** | 3 | 321.92 | 6.191938 | 🔵 low — common in general English |
| 4051 | **test** | 3 | 321.92 | 6.191938 | 🔵 low — common in general English |
| 4052 | **adopted** | 3 | 319.38 | 6.143148 | 🔵 low — common in general English |
| 4053 | **raised** | 4 | 318.59 | 4.595923 | 🔵 low — common in general English |
| 4054 | **circumstance** | 2 | 318.44 | 9.18767 | 🔵 low — common in general English |
| 4055 | **excel** | 2 | 318.44 | 9.18767 | 🔵 low — common in general English |
| 4056 | **younger** | 2 | 318.44 | 9.18767 | 🔵 low — common in general English |
| 4057 | **festival** | 2 | 318.44 | 9.18767 | 🔵 low — common in general English |
| 4058 | **survivors** | 2 | 318.44 | 9.18767 | 🔵 low — common in general English |
| 4059 | **embraced** | 2 | 318.44 | 9.18767 | 🔵 low — common in general English |
| 4060 | **inheritance** | 2 | 318.44 | 9.18767 | 🔵 low — common in general English |
| 4061 | **heights** | 2 | 318.44 | 9.18767 | 🔵 low — common in general English |
| 4062 | **wounded** | 2 | 318.44 | 9.18767 | 🔵 low — common in general English |
| 4063 | **misguided** | 2 | 318.44 | 9.18767 | 🔵 low — common in general English |
| 4064 | **rotting** | 2 | 318.44 | 9.18767 | 🔵 low — common in general English |
| 4065 | **trickle** | 2 | 318.44 | 9.18767 | 🔵 low — common in general English |
| 4066 | **misuse** | 2 | 318.44 | 9.18767 | 🔵 low — common in general English |
| 4067 | **revealing** | 2 | 318.44 | 9.18767 | 🔵 low — common in general English |
| 4068 | **flew** | 2 | 318.44 | 9.18767 | 🔵 low — common in general English |
| 4069 | **exploited** | 2 | 318.44 | 9.18767 | 🔵 low — common in general English |
| 4070 | **pulling** | 2 | 318.44 | 9.18767 | 🔵 low — common in general English |
| 4071 | **wasting** | 2 | 318.44 | 9.18767 | 🔵 low — common in general English |
| 4072 | **medicines** | 2 | 318.44 | 9.18767 | 🔵 low — common in general English |
| 4073 | **frightened** | 2 | 318.44 | 9.18767 | 🔵 low — common in general English |
| 4074 | **uproot** | 2 | 318.44 | 9.18767 | 🔵 low — common in general English |
| 4075 | **disagreements** | 2 | 318.44 | 9.18767 | 🔵 low — common in general English |
| 4076 | **monkey** | 2 | 318.44 | 9.18767 | 🔵 low — common in general English |
| 4077 | **echo** | 2 | 318.44 | 9.18767 | 🔵 low — common in general English |
| 4078 | **empty-handed** | 2 | 318.44 | 9.18767 | 🔵 low — common in general English |
| 4079 | **ceases** | 2 | 318.44 | 9.18767 | 🔵 low — common in general English |
| 4080 | **rows** | 2 | 318.44 | 9.18767 | 🔵 low — common in general English |
| 4081 | **prosper** | 2 | 318.44 | 9.18767 | 🔵 low — common in general English |
| 4082 | **painted** | 2 | 318.44 | 9.18767 | 🔵 low — common in general English |
| 4083 | **confessed** | 2 | 318.44 | 9.18767 | 🔵 low — common in general English |
| 4084 | **childhood** | 2 | 318.44 | 9.18767 | 🔵 low — common in general English |
| 4085 | **renders** | 2 | 318.44 | 9.18767 | 🔵 low — common in general English |
| 4086 | **fade** | 2 | 318.44 | 9.18767 | 🔵 low — common in general English |
| 4087 | **needy** | 2 | 318.44 | 9.18767 | 🔵 low — common in general English |
| 4088 | **beset** | 2 | 318.44 | 9.18767 | 🔵 low — common in general English |
| 4089 | **pen** | 2 | 318.44 | 9.18767 | 🔵 low — common in general English |
| 4090 | **secondly** | 2 | 318.44 | 9.18767 | 🔵 low — common in general English |
| 4091 | **shores** | 2 | 318.44 | 9.18767 | 🔵 low — common in general English |
| 4092 | **lifeline** | 2 | 318.44 | 9.18767 | 🔵 low — common in general English |
| 4093 | **embodied** | 2 | 318.44 | 9.18767 | 🔵 low — common in general English |
| 4094 | **disregard** | 2 | 318.44 | 9.18767 | 🔵 low — common in general English |
| 4095 | **dressed** | 2 | 318.44 | 9.18767 | 🔵 low — common in general English |
| 4096 | **richer** | 2 | 318.44 | 9.18767 | 🔵 low — common in general English |
| 4097 | **tamed** | 2 | 318.44 | 9.18767 | 🔵 low — common in general English |
| 4098 | **gathers** | 2 | 318.44 | 9.18767 | 🔵 low — common in general English |
| 4099 | **rounded** | 2 | 318.44 | 9.18767 | 🔵 low — common in general English |
| 4100 | **seventeen** | 2 | 318.44 | 9.18767 | 🔵 low — common in general English |
| 4101 | **incredible** | 2 | 318.44 | 9.18767 | 🔵 low — common in general English |
| 4102 | **deserve** | 2 | 318.44 | 9.18767 | 🔵 low — common in general English |
| 4103 | **wrongdoing** | 2 | 318.44 | 9.18767 | 🔵 low — common in general English |
| 4104 | **bite** | 2 | 318.44 | 9.18767 | 🔵 low — common in general English |
| 4105 | **sentence** | 2 | 318.44 | 9.18767 | 🔵 low — common in general English |
| 4106 | **liked** | 2 | 318.44 | 9.18767 | 🔵 low — common in general English |
| 4107 | **invalid** | 2 | 318.44 | 9.18767 | 🔵 low — common in general English |
| 4108 | **epidemic** | 2 | 318.44 | 9.18767 | 🔵 low — common in general English |
| 4109 | **obscured** | 2 | 318.44 | 9.18767 | 🔵 low — common in general English |
| 4110 | **proves** | 2 | 318.44 | 9.18767 | 🔵 low — common in general English |
| 4111 | **entirety** | 2 | 318.44 | 9.18767 | 🔵 low — common in general English |
| 4112 | **trained** | 2 | 318.44 | 9.18767 | 🔵 low — common in general English |
| 4113 | **extremes** | 2 | 318.44 | 9.18767 | 🔵 low — common in general English |
| 4114 | **flattened** | 2 | 318.44 | 9.18767 | 🔵 low — common in general English |
| 4115 | **owe** | 2 | 318.44 | 9.18767 | 🔵 low — common in general English |
| 4116 | **vengeance** | 2 | 318.44 | 9.18767 | 🔵 low — common in general English |
| 4117 | **spiralling** | 2 | 318.44 | 9.18767 | 🔵 low — common in general English |
| 4118 | **hence** | 2 | 318.44 | 9.18767 | 🔵 low — common in general English |
| 4119 | **nail** | 2 | 318.44 | 9.18767 | 🔵 low — common in general English |
| 4120 | **eyebrows** | 2 | 318.44 | 9.18767 | 🔵 low — common in general English |
| 4121 | **touches** | 2 | 318.44 | 9.18767 | 🔵 low — common in general English |
| 4122 | **enable** | 3 | 317.75 | 6.111895 | 🔵 low — common in general English |
| 4123 | **narrow** | 3 | 316.96 | 6.096628 | 🔵 low — common in general English |
| 4124 | **fears** | 3 | 314.65 | 6.052176 | 🔵 low — common in general English |
| 4125 | **wholly** | 3 | 313.16 | 6.023602 | 🔵 low — common in general English |
| 4126 | **upward** | 3 | 312.44 | 6.009616 | 🔵 low — common in general English |
| 4127 | **harvest** | 3 | 312.44 | 6.009616 | 🔵 low — common in general English |
| 4128 | **services** | 4 | 312.32 | 4.505539 | 🔵 low — common in general English |
| 4129 | **acquiring** | 3 | 311.72 | 5.995823 | 🔵 low — common in general English |
| 4130 | **relations** | 3 | 311.72 | 5.995823 | 🔵 low — common in general English |
| 4131 | **introduced** | 3 | 311.72 | 5.995823 | 🔵 low — common in general English |
| 4132 | **affairs** | 3 | 311.01 | 5.982217 | 🔵 low — common in general English |
| 4133 | **granted** | 3 | 310.31 | 5.968794 | 🔵 low — common in general English |
| 4134 | **earlier** | 5 | 310.05 | 3.578198 | 🔵 low — common in general English |
| 4135 | **encourage** | 3 | 309.63 | 5.955549 | 🔵 low — common in general English |
| 4136 | **intended** | 3 | 309.63 | 5.955549 | 🔵 low — common in general English |
| 4137 | **unaware** | 2 | 308.47 | 8.899988 | 🔵 low — common in general English |
| 4138 | **ignoring** | 2 | 308.47 | 8.899988 | 🔵 low — common in general English |
| 4139 | **draws** | 2 | 308.47 | 8.899988 | 🔵 low — common in general English |
| 4140 | **tense** | 2 | 308.47 | 8.899988 | 🔵 low — common in general English |
| 4141 | **territories** | 2 | 308.47 | 8.899988 | 🔵 low — common in general English |
| 4142 | **geographically** | 2 | 308.47 | 8.899988 | 🔵 low — common in general English |
| 4143 | **rarely** | 2 | 308.47 | 8.899988 | 🔵 low — common in general English |
| 4144 | **strenuous** | 2 | 308.47 | 8.899988 | 🔵 low — common in general English |
| 4145 | **swimming** | 2 | 308.47 | 8.899988 | 🔵 low — common in general English |
| 4146 | **deliberate** | 2 | 308.47 | 8.899988 | 🔵 low — common in general English |
| 4147 | **descent** | 2 | 308.47 | 8.899988 | 🔵 low — common in general English |
| 4148 | **tens** | 2 | 308.47 | 8.899988 | 🔵 low — common in general English |
| 4149 | **villages** | 2 | 308.47 | 8.899988 | 🔵 low — common in general English |
| 4150 | **protects** | 2 | 308.47 | 8.899988 | 🔵 low — common in general English |
| 4151 | **derive** | 2 | 308.47 | 8.899988 | 🔵 low — common in general English |
| 4152 | **grease** | 2 | 308.47 | 8.899988 | 🔵 low — common in general English |
| 4153 | **mansion** | 2 | 308.47 | 8.899988 | 🔵 low — common in general English |
| 4154 | **encountering** | 2 | 308.47 | 8.899988 | 🔵 low — common in general English |
| 4155 | **ploughing** | 2 | 308.47 | 8.899988 | 🔵 low — common in general English |
| 4156 | **digest** | 2 | 308.47 | 8.899988 | 🔵 low — common in general English |
| 4157 | **appetite** | 2 | 308.47 | 8.899988 | 🔵 low — common in general English |
| 4158 | **boys** | 2 | 308.47 | 8.899988 | 🔵 low — common in general English |
| 4159 | **carcass** | 2 | 308.47 | 8.899988 | 🔵 low — common in general English |
| 4160 | **forceful** | 2 | 308.47 | 8.899988 | 🔵 low — common in general English |
| 4161 | **eradicated** | 2 | 308.47 | 8.899988 | 🔵 low — common in general English |
| 4162 | **rift** | 2 | 308.47 | 8.899988 | 🔵 low — common in general English |
| 4163 | **flaws** | 2 | 308.47 | 8.899988 | 🔵 low — common in general English |
| 4164 | **pills** | 2 | 308.47 | 8.899988 | 🔵 low — common in general English |
| 4165 | **excuse** | 2 | 308.47 | 8.899988 | 🔵 low — common in general English |
| 4166 | **donor** | 2 | 308.47 | 8.899988 | 🔵 low — common in general English |
| 4167 | **muddy** | 2 | 308.47 | 8.899988 | 🔵 low — common in general English |
| 4168 | **diversity** | 2 | 308.47 | 8.899988 | 🔵 low — common in general English |
| 4169 | **handed** | 2 | 308.47 | 8.899988 | 🔵 low — common in general English |
| 4170 | **hay** | 2 | 308.47 | 8.899988 | 🔵 low — common in general English |
| 4171 | **heirs** | 2 | 308.47 | 8.899988 | 🔵 low — common in general English |
| 4172 | **permissible** | 2 | 308.47 | 8.899988 | 🔵 low — common in general English |
| 4173 | **impress** | 2 | 308.47 | 8.899988 | 🔵 low — common in general English |
| 4174 | **disturbed** | 2 | 308.47 | 8.899988 | 🔵 low — common in general English |
| 4175 | **checked** | 2 | 308.47 | 8.899988 | 🔵 low — common in general English |
| 4176 | **absorption** | 2 | 308.47 | 8.899988 | 🔵 low — common in general English |
| 4177 | **extraordinarily** | 2 | 308.47 | 8.899988 | 🔵 low — common in general English |
| 4178 | **constrained** | 2 | 308.47 | 8.899988 | 🔵 low — common in general English |
| 4179 | **uncovered** | 2 | 308.47 | 8.899988 | 🔵 low — common in general English |
| 4180 | **chains** | 2 | 308.47 | 8.899988 | 🔵 low — common in general English |
| 4181 | **vain** | 2 | 308.47 | 8.899988 | 🔵 low — common in general English |
| 4182 | **recipient** | 2 | 308.47 | 8.899988 | 🔵 low — common in general English |
| 4183 | **ring** | 2 | 308.47 | 8.899988 | 🔵 low — common in general English |
| 4184 | **contamination** | 2 | 308.47 | 8.899988 | 🔵 low — common in general English |
| 4185 | **sow** | 2 | 308.47 | 8.899988 | 🔵 low — common in general English |
| 4186 | **blend** | 2 | 308.47 | 8.899988 | 🔵 low — common in general English |
| 4187 | **unity** | 2 | 308.47 | 8.899988 | 🔵 low — common in general English |
| 4188 | **satisfying** | 2 | 308.47 | 8.899988 | 🔵 low — common in general English |
| 4189 | **bend** | 2 | 308.47 | 8.899988 | 🔵 low — common in general English |
| 4190 | **successful** | 3 | 307.61 | 5.916835 | 🔵 low — common in general English |
| 4191 | **week** | 5 | 306.73 | 3.53987 | 🔵 low — common in general English |
| 4192 | **effective** | 4 | 305.99 | 4.414165 | 🔵 low — common in general English |
| 4193 | **suspended** | 3 | 305.05 | 5.867442 | 🔵 low — common in general English |
| 4194 | **post** | 3 | 305.05 | 5.867442 | 🔵 low — common in general English |
| 4195 | **interested** | 3 | 304.42 | 5.855466 | 🔵 low — common in general English |
| 4196 | **controlled** | 3 | 303.20 | 5.831935 | 🔵 low — common in general English |
| 4197 | **identifying** | 2 | 300.74 | 8.676844 | 🔵 low — common in general English |
| 4198 | **reins** | 2 | 300.74 | 8.676844 | 🔵 low — common in general English |
| 4199 | **hunting** | 2 | 300.74 | 8.676844 | 🔵 low — common in general English |
| 4200 | **recipients** | 2 | 300.74 | 8.676844 | 🔵 low — common in general English |
| 4201 | **reward** | 2 | 300.74 | 8.676844 | 🔵 low — common in general English |
| 4202 | **dissatisfaction** | 2 | 300.74 | 8.676844 | 🔵 low — common in general English |
| 4203 | **habits** | 2 | 300.74 | 8.676844 | 🔵 low — common in general English |
| 4204 | **prestige** | 2 | 300.74 | 8.676844 | 🔵 low — common in general English |
| 4205 | **balancing** | 2 | 300.74 | 8.676844 | 🔵 low — common in general English |
| 4206 | **shrink** | 2 | 300.74 | 8.676844 | 🔵 low — common in general English |
| 4207 | **shorter** | 2 | 300.74 | 8.676844 | 🔵 low — common in general English |
| 4208 | **confronted** | 2 | 300.74 | 8.676844 | 🔵 low — common in general English |
| 4209 | **battles** | 2 | 300.74 | 8.676844 | 🔵 low — common in general English |
| 4210 | **captured** | 2 | 300.74 | 8.676844 | 🔵 low — common in general English |
| 4211 | **relieved** | 2 | 300.74 | 8.676844 | 🔵 low — common in general English |
| 4212 | **mere** | 2 | 300.74 | 8.676844 | 🔵 low — common in general English |
| 4213 | **somehow** | 2 | 300.74 | 8.676844 | 🔵 low — common in general English |
| 4214 | **courses** | 2 | 300.74 | 8.676844 | 🔵 low — common in general English |
| 4215 | **anyway** | 2 | 300.74 | 8.676844 | 🔵 low — common in general English |
| 4216 | **freely** | 2 | 300.74 | 8.676844 | 🔵 low — common in general English |
| 4217 | **resemble** | 2 | 300.74 | 8.676844 | 🔵 low — common in general English |
| 4218 | **rushed** | 2 | 300.74 | 8.676844 | 🔵 low — common in general English |
| 4219 | **prediction** | 2 | 300.74 | 8.676844 | 🔵 low — common in general English |
| 4220 | **travelled** | 2 | 300.74 | 8.676844 | 🔵 low — common in general English |
| 4221 | **closest** | 2 | 300.74 | 8.676844 | 🔵 low — common in general English |
| 4222 | **unfavourable** | 2 | 300.74 | 8.676844 | 🔵 low — common in general English |
| 4223 | **overwhelming** | 2 | 300.74 | 8.676844 | 🔵 low — common in general English |
| 4224 | **picks** | 2 | 300.74 | 8.676844 | 🔵 low — common in general English |
| 4225 | **alongside** | 2 | 300.74 | 8.676844 | 🔵 low — common in general English |
| 4226 | **stopping** | 2 | 300.74 | 8.676844 | 🔵 low — common in general English |
| 4227 | **heap** | 2 | 300.74 | 8.676844 | 🔵 low — common in general English |
| 4228 | **guiding** | 2 | 300.74 | 8.676844 | 🔵 low — common in general English |
| 4229 | **failure** | 3 | 299.69 | 5.764494 | 🔵 low — common in general English |
| 4230 | **possibility** | 3 | 299.13 | 5.753683 | 🔵 low — common in general English |
| 4231 | **concerned** | 3 | 298.02 | 5.732405 | 🔵 low — common in general English |
| 4232 | **party** | 3 | 298.02 | 5.732405 | 🔵 low — common in general English |
| 4233 | **preceded** | 2 | 294.42 | 8.494523 | 🔵 low — common in general English |
| 4234 | **freeing** | 2 | 294.42 | 8.494523 | 🔵 low — common in general English |
| 4235 | **towns** | 2 | 294.42 | 8.494523 | 🔵 low — common in general English |
| 4236 | **fragile** | 2 | 294.42 | 8.494523 | 🔵 low — common in general English |
| 4237 | **chose** | 2 | 294.42 | 8.494523 | 🔵 low — common in general English |
| 4238 | **paradise** | 2 | 294.42 | 8.494523 | 🔵 low — common in general English |
| 4239 | **separation** | 2 | 294.42 | 8.494523 | 🔵 low — common in general English |
| 4240 | **collect** | 2 | 294.42 | 8.494523 | 🔵 low — common in general English |
| 4241 | **clubs** | 2 | 294.42 | 8.494523 | 🔵 low — common in general English |
| 4242 | **leap** | 2 | 294.42 | 8.494523 | 🔵 low — common in general English |
| 4243 | **fur** | 2 | 294.42 | 8.494523 | 🔵 low — common in general English |
| 4244 | **stranded** | 2 | 294.42 | 8.494523 | 🔵 low — common in general English |
| 4245 | **drift** | 2 | 294.42 | 8.494523 | 🔵 low — common in general English |
| 4246 | **pinpoint** | 2 | 294.42 | 8.494523 | 🔵 low — common in general English |
| 4247 | **addressed** | 2 | 294.42 | 8.494523 | 🔵 low — common in general English |
| 4248 | **reinforce** | 2 | 294.42 | 8.494523 | 🔵 low — common in general English |
| 4249 | **cell** | 2 | 294.42 | 8.494523 | 🔵 low — common in general English |
| 4250 | **dis** | 2 | 294.42 | 8.494523 | 🔵 low — common in general English |
| 4251 | **donated** | 2 | 294.42 | 8.494523 | 🔵 low — common in general English |
| 4252 | **liable** | 2 | 294.42 | 8.494523 | 🔵 low — common in general English |
| 4253 | **grove** | 2 | 294.42 | 8.494523 | 🔵 low — common in general English |
| 4254 | **matured** | 2 | 294.42 | 8.494523 | 🔵 low — common in general English |
| 4255 | **sailing** | 2 | 294.42 | 8.494523 | 🔵 low — common in general English |
| 4256 | **fulfilling** | 2 | 294.42 | 8.494523 | 🔵 low — common in general English |
| 4257 | **mad** | 2 | 294.42 | 8.494523 | 🔵 low — common in general English |
| 4258 | **survival** | 2 | 294.42 | 8.494523 | 🔵 low — common in general English |
| 4259 | **forgiveness** | 2 | 294.42 | 8.494523 | 🔵 low — common in general English |
| 4260 | **rests** | 2 | 294.42 | 8.494523 | 🔵 low — common in general English |
| 4261 | **vigorous** | 2 | 294.42 | 8.494523 | 🔵 low — common in general English |
| 4262 | **rough** | 2 | 294.42 | 8.494523 | 🔵 low — common in general English |
| 4263 | **benefiting** | 2 | 294.42 | 8.494523 | 🔵 low — common in general English |
| 4264 | **bud** | 2 | 294.42 | 8.494523 | 🔵 low — common in general English |
| 4265 | **whichever** | 2 | 294.42 | 8.494523 | 🔵 low — common in general English |
| 4266 | **sam** | 2 | 294.42 | 8.494523 | 🔵 low — common in general English |
| 4267 | **soften** | 2 | 294.42 | 8.494523 | 🔵 low — common in general English |
| 4268 | **foremost** | 2 | 294.42 | 8.494523 | 🔵 low — common in general English |
| 4269 | **ships** | 3 | 294.33 | 5.66131 | 🔵 low — common in general English |
| 4270 | **agree** | 3 | 293.82 | 5.651553 | 🔵 low — common in general English |
| 4271 | **requirements** | 3 | 293.32 | 5.641891 | 🔵 low — common in general English |
| 4272 | **parent** | 3 | 293.32 | 5.641891 | 🔵 low — common in general English |
| 4273 | **equivalent** | 3 | 292.82 | 5.632322 | 🔵 low — common in general English |
| 4274 | **normal** | 3 | 292.33 | 5.622843 | 🔵 low — common in general English |
| 4275 | **completion** | 3 | 289.93 | 5.576752 | 🔵 low — common in general English |
| 4276 | **opened** | 3 | 289.47 | 5.567784 | 🔵 low — common in general English |
| 4277 | **sold** | 4 | 289.09 | 4.17039 | 🔵 low — common in general English |
| 4278 | **patterns** | 2 | 289.07 | 8.340372 | 🔵 low — common in general English |
| 4279 | **drinks** | 2 | 289.07 | 8.340372 | 🔵 low — common in general English |
| 4280 | **subdued** | 2 | 289.07 | 8.340372 | 🔵 low — common in general English |
| 4281 | **frontier** | 2 | 289.07 | 8.340372 | 🔵 low — common in general English |
| 4282 | **dig** | 2 | 289.07 | 8.340372 | 🔵 low — common in general English |
| 4283 | **seized** | 2 | 289.07 | 8.340372 | 🔵 low — common in general English |
| 4284 | **observed** | 2 | 289.07 | 8.340372 | 🔵 low — common in general English |
| 4285 | **patient** | 2 | 289.07 | 8.340372 | 🔵 low — common in general English |
| 4286 | **hired** | 2 | 289.07 | 8.340372 | 🔵 low — common in general English |
| 4287 | **seas** | 2 | 289.07 | 8.340372 | 🔵 low — common in general English |
| 4288 | **anybody** | 2 | 289.07 | 8.340372 | 🔵 low — common in general English |
| 4289 | **tate** | 2 | 289.07 | 8.340372 | 🔵 low — common in general English |
| 4290 | **abundant** | 2 | 289.07 | 8.340372 | 🔵 low — common in general English |
| 4291 | **style** | 2 | 289.07 | 8.340372 | 🔵 low — common in general English |
| 4292 | **requesting** | 2 | 289.07 | 8.340372 | 🔵 low — common in general English |
| 4293 | **reflected** | 3 | 289.00 | 5.558895 | 🔵 low — common in general English |
| 4294 | **series** | 3 | 288.55 | 5.550084 | 🔵 low — common in general English |
| 4295 | **provisions** | 3 | 288.55 | 5.550084 | 🔵 low — common in general English |
| 4296 | **banks** | 4 | 288.48 | 4.161599 | 🔵 low — common in general English |
| 4297 | **acquire** | 4 | 287.72 | 4.150717 | 🔵 low — common in general English |
| 4298 | **accounts** | 3 | 287.64 | 5.532692 | 🔵 low — common in general English |
| 4299 | **results** | 4 | 286.24 | 4.129303 | 🔵 low — common in general English |
| 4300 | **unconditional** | 2 | 284.45 | 8.206841 | 🔵 low — common in general English |
| 4301 | **consult** | 2 | 284.45 | 8.206841 | 🔵 low — common in general English |
| 4302 | **influenced** | 2 | 284.45 | 8.206841 | 🔵 low — common in general English |
| 4303 | **function** | 2 | 284.45 | 8.206841 | 🔵 low — common in general English |
| 4304 | **geography** | 2 | 284.45 | 8.206841 | 🔵 low — common in general English |
| 4305 | **existed** | 2 | 284.45 | 8.206841 | 🔵 low — common in general English |
| 4306 | **conflicts** | 2 | 284.45 | 8.206841 | 🔵 low — common in general English |
| 4307 | **older** | 2 | 284.45 | 8.206841 | 🔵 low — common in general English |
| 4308 | **struggle** | 2 | 284.45 | 8.206841 | 🔵 low — common in general English |
| 4309 | **burns** | 2 | 284.45 | 8.206841 | 🔵 low — common in general English |
| 4310 | **bellies** | 2 | 284.45 | 8.206841 | 🔵 low — common in general English |
| 4311 | **cheating** | 2 | 284.45 | 8.206841 | 🔵 low — common in general English |
| 4312 | **peg** | 2 | 284.45 | 8.206841 | 🔵 low — common in general English |
| 4313 | **lined** | 2 | 284.45 | 8.206841 | 🔵 low — common in general English |
| 4314 | **helpful** | 2 | 284.45 | 8.206841 | 🔵 low — common in general English |
| 4315 | **abandoning** | 2 | 284.45 | 8.206841 | 🔵 low — common in general English |
| 4316 | **relax** | 2 | 284.45 | 8.206841 | 🔵 low — common in general English |
| 4317 | **unique** | 2 | 284.45 | 8.206841 | 🔵 low — common in general English |
| 4318 | **contents** | 2 | 284.45 | 8.206841 | 🔵 low — common in general English |
| 4319 | **emerges** | 2 | 284.45 | 8.206841 | 🔵 low — common in general English |
| 4320 | **undoubtedly** | 2 | 284.45 | 8.206841 | 🔵 low — common in general English |
| 4321 | **released** | 3 | 284.17 | 5.466001 | 🔵 low — common in general English |
| 4322 | **calls** | 3 | 283.76 | 5.457969 | 🔵 low — common in general English |
| 4323 | **law** | 3 | 282.93 | 5.442095 | 🔵 low — common in general English |
| 4324 | **steel** | 3 | 282.12 | 5.42647 | 🔵 low — common in general English |
| 4325 | **entertain** | 2 | 280.36 | 8.089058 | 🔵 low — common in general English |
| 4326 | **fortunes** | 2 | 280.36 | 8.089058 | 🔵 low — common in general English |
| 4327 | **burned** | 2 | 280.36 | 8.089058 | 🔵 low — common in general English |
| 4328 | **impressed** | 2 | 280.36 | 8.089058 | 🔵 low — common in general English |
| 4329 | **composed** | 2 | 280.36 | 8.089058 | 🔵 low — common in general English |
| 4330 | **chiefs** | 2 | 280.36 | 8.089058 | 🔵 low — common in general English |
| 4331 | **fulfilled** | 2 | 280.36 | 8.089058 | 🔵 low — common in general English |
| 4332 | **stretch** | 2 | 280.36 | 8.089058 | 🔵 low — common in general English |
| 4333 | **insignificant** | 2 | 280.36 | 8.089058 | 🔵 low — common in general English |
| 4334 | **attracting** | 2 | 280.36 | 8.089058 | 🔵 low — common in general English |
| 4335 | **saving** | 2 | 280.36 | 8.089058 | 🔵 low — common in general English |
| 4336 | **comfortably** | 2 | 280.36 | 8.089058 | 🔵 low — common in general English |
| 4337 | **sands** | 2 | 280.36 | 8.089058 | 🔵 low — common in general English |
| 4338 | **eliminating** | 2 | 280.36 | 8.089058 | 🔵 low — common in general English |
| 4339 | **fits** | 2 | 280.36 | 8.089058 | 🔵 low — common in general English |
| 4340 | **repaired** | 2 | 280.36 | 8.089058 | 🔵 low — common in general English |
| 4341 | **improve** | 3 | 279.37 | 5.373627 | 🔵 low — common in general English |
| 4342 | **considering** | 3 | 278.99 | 5.366301 | 🔵 low — common in general English |
| 4343 | **workers** | 3 | 277.87 | 5.34464 | 🔵 low — common in general English |
| 4344 | **steering** | 2 | 276.71 | 7.983697 | 🔵 low — common in general English |
| 4345 | **absorbed** | 2 | 276.71 | 7.983697 | 🔵 low — common in general English |
| 4346 | **successor** | 2 | 276.71 | 7.983697 | 🔵 low — common in general English |
| 4347 | **eighth** | 2 | 276.71 | 7.983697 | 🔵 low — common in general English |
| 4348 | **diminish** | 2 | 276.71 | 7.983697 | 🔵 low — common in general English |
| 4349 | **impression** | 2 | 276.71 | 7.983697 | 🔵 low — common in general English |
| 4350 | **rare** | 2 | 276.71 | 7.983697 | 🔵 low — common in general English |
| 4351 | **sinking** | 2 | 276.71 | 7.983697 | 🔵 low — common in general English |
| 4352 | **ice** | 2 | 276.71 | 7.983697 | 🔵 low — common in general English |
| 4353 | **bitter** | 2 | 276.71 | 7.983697 | 🔵 low — common in general English |
| 4354 | **unhappy** | 2 | 276.71 | 7.983697 | 🔵 low — common in general English |
| 4355 | **passengers** | 2 | 276.71 | 7.983697 | 🔵 low — common in general English |
| 4356 | **consumed** | 2 | 276.71 | 7.983697 | 🔵 low — common in general English |
| 4357 | **examination** | 2 | 276.71 | 7.983697 | 🔵 low — common in general English |
| 4358 | **banner** | 2 | 276.71 | 7.983697 | 🔵 low — common in general English |
| 4359 | **sank** | 2 | 276.71 | 7.983697 | 🔵 low — common in general English |
| 4360 | **school** | 2 | 276.71 | 7.983697 | 🔵 low — common in general English |
| 4361 | **positively** | 2 | 276.71 | 7.983697 | 🔵 low — common in general English |
| 4362 | **produce** | 3 | 275.68 | 5.302676 | 🔵 low — common in general English |
| 4363 | **fixed** | 3 | 274.28 | 5.275647 | 🔵 low — common in general English |
| 4364 | **safely** | 2 | 273.41 | 7.888387 | 🔵 low — common in general English |
| 4365 | **host** | 2 | 273.41 | 7.888387 | 🔵 low — common in general English |
| 4366 | **vowed** | 2 | 273.41 | 7.888387 | 🔵 low — common in general English |
| 4367 | **picked** | 2 | 273.41 | 7.888387 | 🔵 low — common in general English |
| 4368 | **survive** | 2 | 273.41 | 7.888387 | 🔵 low — common in general English |
| 4369 | **roll** | 2 | 273.41 | 7.888387 | 🔵 low — common in general English |
| 4370 | **rolled** | 2 | 273.41 | 7.888387 | 🔵 low — common in general English |
| 4371 | **frequent** | 2 | 273.41 | 7.888387 | 🔵 low — common in general English |
| 4372 | **searching** | 2 | 273.41 | 7.888387 | 🔵 low — common in general English |
| 4373 | **sovereignty** | 2 | 273.41 | 7.888387 | 🔵 low — common in general English |
| 4374 | **bull** | 2 | 273.41 | 7.888387 | 🔵 low — common in general English |
| 4375 | **garden** | 2 | 273.41 | 7.888387 | 🔵 low — common in general English |
| 4376 | **praised** | 2 | 273.41 | 7.888387 | 🔵 low — common in general English |
| 4377 | **exceptionally** | 2 | 273.41 | 7.888387 | 🔵 low — common in general English |
| 4378 | **changed** | 3 | 273.25 | 5.255844 | 🔵 low — common in general English |
| 4379 | **united** | 4 | 271.96 | 3.923254 | 🔵 low — common in general English |
| 4380 | **techniques** | 2 | 270.39 | 7.801376 | 🔵 low — common in general English |
| 4381 | **seasons** | 2 | 270.39 | 7.801376 | 🔵 low — common in general English |
| 4382 | **affects** | 2 | 270.39 | 7.801376 | 🔵 low — common in general English |
| 4383 | **occurs** | 2 | 270.39 | 7.801376 | 🔵 low — common in general English |
| 4384 | **one-day** | 2 | 270.39 | 7.801376 | 🔵 low — common in general English |
| 4385 | **arguing** | 2 | 270.39 | 7.801376 | 🔵 low — common in general English |
| 4386 | **permanently** | 2 | 270.39 | 7.801376 | 🔵 low — common in general English |
| 4387 | **unnecessary** | 2 | 270.39 | 7.801376 | 🔵 low — common in general English |
| 4388 | **stiff** | 2 | 270.39 | 7.801376 | 🔵 low — common in general English |
| 4389 | **suits** | 2 | 270.39 | 7.801376 | 🔵 low — common in general English |
| 4390 | **mark** | 3 | 268.39 | 5.162318 | 🔵 low — common in general English |
| 4391 | **limited** | 3 | 267.77 | 5.150484 | 🔵 low — common in general English |
| 4392 | **worrying** | 2 | 267.62 | 7.721333 | 🔵 low — common in general English |
| 4393 | **collapsed** | 2 | 267.62 | 7.721333 | 🔵 low — common in general English |
| 4394 | **eagle** | 2 | 267.62 | 7.721333 | 🔵 low — common in general English |
| 4395 | **stepped** | 2 | 267.62 | 7.721333 | 🔵 low — common in general English |
| 4396 | **flying** | 2 | 267.62 | 7.721333 | 🔵 low — common in general English |
| 4397 | **sticking** | 2 | 267.62 | 7.721333 | 🔵 low — common in general English |
| 4398 | **installed** | 2 | 267.62 | 7.721333 | 🔵 low — common in general English |
| 4399 | **steam** | 2 | 267.62 | 7.721333 | 🔵 low — common in general English |
| 4400 | **briefly** | 2 | 267.62 | 7.721333 | 🔵 low — common in general English |
| 4401 | **remaining** | 3 | 265.38 | 5.104499 | 🔵 low — common in general English |
| 4402 | **continuing** | 3 | 265.38 | 5.104499 | 🔵 low — common in general English |
| 4403 | **press** | 3 | 265.38 | 5.104499 | 🔵 low — common in general English |
| 4404 | **picking** | 2 | 265.05 | 7.647225 | 🔵 low — common in general English |
| 4405 | **pursuing** | 2 | 265.05 | 7.647225 | 🔵 low — common in general English |
| 4406 | **strictly** | 2 | 265.05 | 7.647225 | 🔵 low — common in general English |
| 4407 | **approaching** | 2 | 265.05 | 7.647225 | 🔵 low — common in general English |
| 4408 | **postpone** | 2 | 265.05 | 7.647225 | 🔵 low — common in general English |
| 4409 | **dip** | 2 | 265.05 | 7.647225 | 🔵 low — common in general English |
| 4410 | **extreme** | 2 | 265.05 | 7.647225 | 🔵 low — common in general English |
| 4411 | **arguments** | 2 | 265.05 | 7.647225 | 🔵 low — common in general English |
| 4412 | **recognition** | 2 | 265.05 | 7.647225 | 🔵 low — common in general English |
| 4413 | **plunge** | 2 | 265.05 | 7.647225 | 🔵 low — common in general English |
| 4414 | **compare** | 2 | 265.05 | 7.647225 | 🔵 low — common in general English |
| 4415 | **wrote** | 2 | 265.05 | 7.647225 | 🔵 low — common in general English |
| 4416 | **origins** | 2 | 265.05 | 7.647225 | 🔵 low — common in general English |
| 4417 | **breaks** | 2 | 262.66 | 7.578232 | 🔵 low — common in general English |
| 4418 | **constitute** | 2 | 262.66 | 7.578232 | 🔵 low — common in general English |
| 4419 | **thinks** | 2 | 262.66 | 7.578232 | 🔵 low — common in general English |
| 4420 | **sown** | 2 | 262.66 | 7.578232 | 🔵 low — common in general English |
| 4421 | **tend** | 2 | 262.66 | 7.578232 | 🔵 low — common in general English |
| 4422 | **exists** | 2 | 262.66 | 7.578232 | 🔵 low — common in general English |
| 4423 | **pulp** | 2 | 262.66 | 7.578232 | 🔵 low — common in general English |
| 4424 | **treated** | 2 | 262.66 | 7.578232 | 🔵 low — common in general English |
| 4425 | **refrain** | 2 | 262.66 | 7.578232 | 🔵 low — common in general English |
| 4426 | **repaid** | 2 | 262.66 | 7.578232 | 🔵 low — common in general English |
| 4427 | **recognized** | 2 | 262.66 | 7.578232 | 🔵 low — common in general English |
| 4428 | **responsibility** | 2 | 262.66 | 7.578232 | 🔵 low — common in general English |
| 4429 | **engage** | 2 | 260.42 | 7.513694 | 🔵 low — common in general English |
| 4430 | **fails** | 2 | 260.42 | 7.513694 | 🔵 low — common in general English |
| 4431 | **counsel** | 2 | 260.42 | 7.513694 | 🔵 low — common in general English |
| 4432 | **framework** | 2 | 260.42 | 7.513694 | 🔵 low — common in general English |
| 4433 | **key** | 3 | 260.11 | 5.003079 | 🔵 low — common in general English |
| 4434 | **sometime** | 2 | 258.32 | 7.453069 | 🔵 low — common in general English |
| 4435 | **absorb** | 2 | 258.32 | 7.453069 | 🔵 low — common in general English |
| 4436 | **hills** | 2 | 258.32 | 7.453069 | 🔵 low — common in general English |
| 4437 | **resort** | 2 | 258.32 | 7.453069 | 🔵 low — common in general English |
| 4438 | **frost** | 2 | 258.32 | 7.453069 | 🔵 low — common in general English |
| 4439 | **latter** | 2 | 258.32 | 7.453069 | 🔵 low — common in general English |
| 4440 | **establishing** | 2 | 258.32 | 7.453069 | 🔵 low — common in general English |
| 4441 | **sudden** | 2 | 258.32 | 7.453069 | 🔵 low — common in general English |
| 4442 | **pat** | 2 | 258.32 | 7.453069 | 🔵 low — common in general English |
| 4443 | **considerations** | 2 | 258.32 | 7.453069 | 🔵 low — common in general English |
| 4444 | **payment** | 3 | 258.04 | 4.963272 | 🔵 low — common in general English |
| 4445 | **splits** | 2 | 256.34 | 7.395911 | 🔵 low — common in general English |
| 4446 | **greatly** | 2 | 256.34 | 7.395911 | 🔵 low — common in general English |
| 4447 | **preparation** | 2 | 256.34 | 7.395911 | 🔵 low — common in general English |
| 4448 | **flowing** | 2 | 256.34 | 7.395911 | 🔵 low — common in general English |
| 4449 | **route** | 2 | 256.34 | 7.395911 | 🔵 low — common in general English |
| 4450 | **ball** | 2 | 256.34 | 7.395911 | 🔵 low — common in general English |
| 4451 | **due** | 4 | 256.30 | 3.697356 | 🔵 low — common in general English |
| 4452 | **sessions** | 2 | 254.47 | 7.341843 | 🔵 low — common in general English |
| 4453 | **afford** | 2 | 254.47 | 7.341843 | 🔵 low — common in general English |
| 4454 | **pretty** | 2 | 254.47 | 7.341843 | 🔵 low — common in general English |
| 4455 | **climb** | 2 | 254.47 | 7.341843 | 🔵 low — common in general English |
| 4456 | **injured** | 2 | 254.47 | 7.341843 | 🔵 low — common in general English |
| 4457 | **sciences** | 2 | 254.47 | 7.341843 | 🔵 low — common in general English |
| 4458 | **population** | 2 | 252.69 | 7.29055 | 🔵 low — common in general English |
| 4459 | **shared** | 2 | 252.69 | 7.29055 | 🔵 low — common in general English |
| 4460 | **provinces** | 2 | 252.69 | 7.29055 | 🔵 low — common in general English |
| 4461 | **violating** | 2 | 252.69 | 7.29055 | 🔵 low — common in general English |
| 4462 | **bridge** | 2 | 252.69 | 7.29055 | 🔵 low — common in general English |
| 4463 | **uses** | 2 | 252.69 | 7.29055 | 🔵 low — common in general English |
| 4464 | **referred** | 2 | 252.69 | 7.29055 | 🔵 low — common in general English |
| 4465 | **joining** | 2 | 252.69 | 7.29055 | 🔵 low — common in general English |
| 4466 | **renew** | 2 | 252.69 | 7.29055 | 🔵 low — common in general English |
| 4467 | **analysis** | 2 | 252.69 | 7.29055 | 🔵 low — common in general English |
| 4468 | **cuts** | 3 | 252.51 | 4.856937 | 🔵 low — common in general English |
| 4469 | **events** | 2 | 251.00 | 7.24176 | 🔵 low — common in general English |
| 4470 | **escort** | 2 | 251.00 | 7.24176 | 🔵 low — common in general English |
| 4471 | **quantities** | 2 | 251.00 | 7.24176 | 🔵 low — common in general English |
| 4472 | **restored** | 2 | 251.00 | 7.24176 | 🔵 low — common in general English |
| 4473 | **sustain** | 2 | 251.00 | 7.24176 | 🔵 low — common in general English |
| 4474 | **category** | 2 | 249.38 | 7.19524 | 🔵 low — common in general English |
| 4475 | **obviously** | 2 | 249.38 | 7.19524 | 🔵 low — common in general English |
| 4476 | **troubled** | 2 | 249.38 | 7.19524 | 🔵 low — common in general English |
| 4477 | **argued** | 2 | 249.38 | 7.19524 | 🔵 low — common in general English |
| 4478 | **competitors** | 2 | 249.38 | 7.19524 | 🔵 low — common in general English |
| 4479 | **exception** | 2 | 249.38 | 7.19524 | 🔵 low — common in general English |
| 4480 | **consulting** | 2 | 249.38 | 7.19524 | 🔵 low — common in general English |
| 4481 | **blocked** | 2 | 247.84 | 7.150788 | 🔵 low — common in general English |
| 4482 | **maybe** | 2 | 247.84 | 7.150788 | 🔵 low — common in general English |
| 4483 | **picture** | 2 | 247.84 | 7.150788 | 🔵 low — common in general English |
| 4484 | **associate** | 2 | 247.84 | 7.150788 | 🔵 low — common in general English |
| 4485 | **service** | 3 | 246.49 | 4.741105 | 🔵 low — common in general English |
| 4486 | **wet** | 2 | 246.37 | 7.108229 | 🔵 low — common in general English |
| 4487 | **dependent** | 2 | 246.37 | 7.108229 | 🔵 low — common in general English |
| 4488 | **comparison** | 2 | 246.37 | 7.108229 | 🔵 low — common in general English |
| 4489 | **usual** | 2 | 244.95 | 7.067407 | 🔵 low — common in general English |
| 4490 | **individuals** | 2 | 244.95 | 7.067407 | 🔵 low — common in general English |
| 4491 | **jump** | 2 | 244.95 | 7.067407 | 🔵 low — common in general English |
| 4492 | **struck** | 2 | 244.95 | 7.067407 | 🔵 low — common in general English |
| 4493 | **transferred** | 2 | 244.95 | 7.067407 | 🔵 low — common in general English |
| 4494 | **stem** | 2 | 244.95 | 7.067407 | 🔵 low — common in general English |
| 4495 | **comparisons** | 2 | 243.59 | 7.028186 | 🔵 low — common in general English |
| 4496 | **underground** | 2 | 243.59 | 7.028186 | 🔵 low — common in general English |
| 4497 | **hour** | 2 | 243.59 | 7.028186 | 🔵 low — common in general English |
| 4498 | **funds** | 3 | 243.53 | 4.684164 | 🔵 low — common in general English |
| 4499 | **deal** | 3 | 242.77 | 4.669511 | 🔵 low — common in general English |
| 4500 | **paid** | 3 | 242.58 | 4.665882 | 🔵 low — common in general English |
| 4501 | **tension** | 2 | 242.29 | 6.990446 | 🔵 low — common in general English |
| 4502 | **attracted** | 2 | 242.29 | 6.990446 | 🔵 low — common in general English |
| 4503 | **fifth** | 2 | 242.29 | 6.990446 | 🔵 low — common in general English |
| 4504 | **secure** | 2 | 242.29 | 6.990446 | 🔵 low — common in general English |
| 4505 | **react** | 2 | 242.29 | 6.990446 | 🔵 low — common in general English |
| 4506 | **neutral** | 2 | 242.29 | 6.990446 | 🔵 low — common in general English |
| 4507 | **steep** | 2 | 242.29 | 6.990446 | 🔵 low — common in general English |
| 4508 | **added** | 4 | 241.42 | 3.482777 | 🔵 low — common in general English |
| 4509 | **community** | 3 | 241.27 | 4.640835 | 🔵 low — common in general English |
| 4510 | **additional** | 3 | 240.00 | 4.616401 | 🔵 low — common in general English |
| 4511 | **badly** | 2 | 239.81 | 6.918987 | 🔵 low — common in general English |
| 4512 | **heating** | 2 | 239.81 | 6.918987 | 🔵 low — common in general English |
| 4513 | **calm** | 2 | 239.81 | 6.918987 | 🔵 low — common in general English |
| 4514 | **approached** | 2 | 239.81 | 6.918987 | 🔵 low — common in general English |
| 4515 | **safety** | 2 | 239.81 | 6.918987 | 🔵 low — common in general English |
| 4516 | **type** | 2 | 239.81 | 6.918987 | 🔵 low — common in general English |
| 4517 | **address** | 2 | 239.81 | 6.918987 | 🔵 low — common in general English |
| 4518 | **promised** | 2 | 239.81 | 6.918987 | 🔵 low — common in general English |
| 4519 | **late** | 3 | 238.76 | 4.59255 | 🔵 low — common in general English |
| 4520 | **event** | 2 | 238.63 | 6.885085 | 🔵 low — common in general English |
| 4521 | **closes** | 2 | 238.63 | 6.885085 | 🔵 low — common in general English |
| 4522 | **tire** | 2 | 238.63 | 6.885085 | 🔵 low — common in general English |
| 4523 | **preparing** | 2 | 238.63 | 6.885085 | 🔵 low — common in general English |
| 4524 | **appointed** | 2 | 238.63 | 6.885085 | 🔵 low — common in general English |
| 4525 | **proportion** | 2 | 236.40 | 6.820546 | 🔵 low — common in general English |
| 4526 | **pushing** | 2 | 235.33 | 6.789775 | 🔵 low — common in general English |
| 4527 | **disputes** | 2 | 235.33 | 6.789775 | 🔵 low — common in general English |
| 4528 | **acceptable** | 2 | 235.33 | 6.789775 | 🔵 low — common in general English |
| 4529 | **urge** | 2 | 235.33 | 6.789775 | 🔵 low — common in general English |
| 4530 | **chain** | 2 | 235.33 | 6.789775 | 🔵 low — common in general English |
| 4531 | **maintaining** | 2 | 235.33 | 6.789775 | 🔵 low — common in general English |
| 4532 | **news** | 3 | 234.89 | 4.517961 | 🔵 low — common in general English |
| 4533 | **priority** | 2 | 234.30 | 6.759922 | 🔵 low — common in general English |
| 4534 | **encouraged** | 2 | 234.30 | 6.759922 | 🔵 low — common in general English |
| 4535 | **balanced** | 2 | 233.29 | 6.730934 | 🔵 low — common in general English |
| 4536 | **tonight** | 2 | 233.29 | 6.730934 | 🔵 low — common in general English |
| 4537 | **announcing** | 2 | 232.32 | 6.702763 | 🔵 low — common in general English |
| 4538 | **marked** | 2 | 232.32 | 6.702763 | 🔵 low — common in general English |
| 4539 | **draw** | 2 | 232.32 | 6.702763 | 🔵 low — common in general English |
| 4540 | **failing** | 2 | 231.37 | 6.675364 | 🔵 low — common in general English |
| 4541 | **questions** | 2 | 231.37 | 6.675364 | 🔵 low — common in general English |
| 4542 | **bidding** | 2 | 231.37 | 6.675364 | 🔵 low — common in general English |
| 4543 | **occurred** | 2 | 231.37 | 6.675364 | 🔵 low — common in general English |
| 4544 | **resist** | 2 | 231.37 | 6.675364 | 🔵 low — common in general English |
| 4545 | **settle** | 2 | 231.37 | 6.675364 | 🔵 low — common in general English |
| 4546 | **seemed** | 2 | 231.37 | 6.675364 | 🔵 low — common in general English |
| 4547 | **attempts** | 2 | 231.37 | 6.675364 | 🔵 low — common in general English |
| 4548 | **complex** | 2 | 231.37 | 6.675364 | 🔵 low — common in general English |
| 4549 | **origin** | 2 | 230.44 | 6.648696 | 🔵 low — common in general English |
| 4550 | **indication** | 2 | 229.54 | 6.622721 | 🔵 low — common in general English |
| 4551 | **deals** | 2 | 229.54 | 6.622721 | 🔵 low — common in general English |
| 4552 | **broke** | 2 | 229.54 | 6.622721 | 🔵 low — common in general English |
| 4553 | **conditioned** | 2 | 229.54 | 6.622721 | 🔵 low — common in general English |
| 4554 | **twice** | 2 | 228.66 | 6.597403 | 🔵 low — common in general English |
| 4555 | **outright** | 2 | 228.66 | 6.597403 | 🔵 low — common in general English |
| 4556 | **recommend** | 2 | 228.66 | 6.597403 | 🔵 low — common in general English |
| 4557 | **sufficient** | 2 | 228.66 | 6.597403 | 🔵 low — common in general English |
| 4558 | **measured** | 2 | 227.81 | 6.57271 | 🔵 low — common in general English |
| 4559 | **shut** | 2 | 227.81 | 6.57271 | 🔵 low — common in general English |
| 4560 | **unions** | 2 | 227.81 | 6.57271 | 🔵 low — common in general English |
| 4561 | **costs** | 3 | 227.48 | 4.375486 | 🔵 low — common in general English |
| 4562 | **core** | 2 | 226.97 | 6.548613 | 🔵 low — common in general English |
| 4563 | **welcomed** | 2 | 226.97 | 6.548613 | 🔵 low — common in general English |
| 4564 | **comprising** | 2 | 226.16 | 6.525082 | 🔵 low — common in general English |
| 4565 | **headed** | 2 | 225.36 | 6.502093 | 🔵 low — common in general English |
| 4566 | **lifted** | 2 | 225.36 | 6.502093 | 🔵 low — common in general English |
| 4567 | **comparable** | 2 | 225.36 | 6.502093 | 🔵 low — common in general English |
| 4568 | **frozen** | 2 | 224.58 | 6.47962 | 🔵 low — common in general English |
| 4569 | **involving** | 2 | 224.58 | 6.47962 | 🔵 low — common in general English |
| 4570 | **tight** | 2 | 223.82 | 6.457641 | 🔵 low — common in general English |
| 4571 | **produces** | 2 | 223.82 | 6.457641 | 🔵 low — common in general English |
| 4572 | **contribute** | 2 | 223.07 | 6.436135 | 🔵 low — common in general English |
| 4573 | **room** | 2 | 223.07 | 6.436135 | 🔵 low — common in general English |
| 4574 | **faced** | 2 | 223.07 | 6.436135 | 🔵 low — common in general English |
| 4575 | **contained** | 2 | 223.07 | 6.436135 | 🔵 low — common in general English |
| 4576 | **flat** | 2 | 223.07 | 6.436135 | 🔵 low — common in general English |
| 4577 | **social** | 2 | 221.63 | 6.394462 | 🔵 low — common in general English |
| 4578 | **depending** | 2 | 220.93 | 6.374259 | 🔵 low — common in general English |
| 4579 | **so-called** | 2 | 220.93 | 6.374259 | 🔵 low — common in general English |
| 4580 | **internal** | 2 | 220.24 | 6.354457 | 🔵 low — common in general English |
| 4581 | **rapid** | 2 | 220.24 | 6.354457 | 🔵 low — common in general English |
| 4582 | **proceed** | 2 | 220.24 | 6.354457 | 🔵 low — common in general English |
| 4583 | **likely** | 3 | 219.40 | 4.220174 | 🔵 low — common in general English |
| 4584 | **movements** | 2 | 218.91 | 6.31599 | 🔵 low — common in general English |
| 4585 | **demands** | 2 | 218.91 | 6.31599 | 🔵 low — common in general English |
| 4586 | **evidence** | 2 | 218.91 | 6.31599 | 🔵 low — common in general English |
| 4587 | **normally** | 2 | 217.63 | 6.278949 | 🔵 low — common in general English |
| 4588 | **competitiveness** | 2 | 217.00 | 6.260931 | 🔵 low — common in general English |
| 4589 | **decrease** | 2 | 217.00 | 6.260931 | 🔵 low — common in general English |
| 4590 | **structure** | 2 | 216.39 | 6.243231 | 🔵 low — common in general English |
| 4591 | **double** | 2 | 215.79 | 6.225839 | 🔵 low — common in general English |
| 4592 | **brown** | 2 | 215.79 | 6.225839 | 🔵 low — common in general English |
| 4593 | **retain** | 2 | 215.19 | 6.208745 | 🔵 low — common in general English |
| 4594 | **limits** | 2 | 215.19 | 6.208745 | 🔵 low — common in general English |
| 4595 | **partner** | 2 | 214.61 | 6.191938 | 🔵 low — common in general English |
| 4596 | **bank** | 4 | 214.48 | 3.0941 | 🔵 low — common in general English |
| 4597 | **fallen** | 2 | 214.04 | 6.175409 | 🔵 low — common in general English |
| 4598 | **vessels** | 2 | 214.04 | 6.175409 | 🔵 low — common in general English |
| 4599 | **participation** | 2 | 214.04 | 6.175409 | 🔵 low — common in general English |
| 4600 | **advanced** | 2 | 213.47 | 6.159148 | 🔵 low — common in general English |
| 4601 | **figures** | 3 | 212.21 | 4.081725 | 🔵 low — common in general English |
| 4602 | **ruled** | 2 | 211.84 | 6.111895 | 🔵 low — common in general English |
| 4603 | **primarily** | 2 | 211.84 | 6.111895 | 🔵 low — common in general English |
| 4604 | **loss** | 4 | 211.57 | 3.052105 | 🔵 low — common in general English |
| 4605 | **plans** | 3 | 209.95 | 4.03824 | 🔵 low — common in general English |
| 4606 | **depressed** | 2 | 209.27 | 6.037787 | 🔵 low — common in general English |
| 4607 | **threatened** | 2 | 209.27 | 6.037787 | 🔵 low — common in general English |
| 4608 | **strongly** | 2 | 209.27 | 6.037787 | 🔵 low — common in general English |
| 4609 | **stake** | 3 | 209.25 | 4.024791 | 🔵 low — common in general English |
| 4610 | **declines** | 2 | 208.29 | 6.009616 | 🔵 low — common in general English |
| 4611 | **push** | 2 | 207.81 | 5.995823 | 🔵 low — common in general English |
| 4612 | **discussed** | 2 | 207.34 | 5.982217 | 🔵 low — common in general English |
| 4613 | **claims** | 2 | 206.88 | 5.968794 | 🔵 low — common in general English |
| 4614 | **pound** | 2 | 206.42 | 5.955549 | 🔵 low — common in general English |
| 4615 | **larger** | 2 | 205.52 | 5.929574 | 🔵 low — common in general English |
| 4616 | **copper** | 2 | 205.52 | 5.929574 | 🔵 low — common in general English |
| 4617 | **laws** | 2 | 205.52 | 5.929574 | 🔵 low — common in general English |
| 4618 | **smaller** | 2 | 205.08 | 5.916835 | 🔵 low — common in general English |
| 4619 | **positions** | 2 | 204.64 | 5.904256 | 🔵 low — common in general English |
| 4620 | **grew** | 2 | 204.21 | 5.891833 | 🔵 low — common in general English |
| 4621 | **require** | 2 | 203.78 | 5.879563 | 🔵 low — common in general English |
| 4622 | **products** | 3 | 203.26 | 3.909555 | 🔵 low — common in general English |
| 4623 | **orders** | 2 | 202.13 | 5.831935 | 🔵 low — common in general English |
| 4624 | **release** | 2 | 202.13 | 5.831935 | 🔵 low — common in general English |
| 4625 | **forward** | 2 | 202.13 | 5.831935 | 🔵 low — common in general English |
| 4626 | **hours** | 2 | 201.73 | 5.820374 | 🔵 low — common in general English |
| 4627 | **materials** | 2 | 201.34 | 5.808946 | 🔵 low — common in general English |
| 4628 | **continues** | 2 | 197.25 | 5.691163 | 🔵 low — common in general English |
| 4629 | **buy** | 3 | 195.62 | 3.76272 | 🔵 low — common in general English |
| 4630 | **helped** | 2 | 195.21 | 5.632322 | 🔵 low — common in general English |
| 4631 | **affect** | 2 | 195.21 | 5.632322 | 🔵 low — common in general English |
| 4632 | **amounts** | 2 | 194.89 | 5.622843 | 🔵 low — common in general English |
| 4633 | **primary** | 2 | 193.60 | 5.585802 | 🔵 low — common in general English |
| 4634 | **ends** | 2 | 191.76 | 5.532692 | 🔵 low — common in general English |
| 4635 | **majority** | 2 | 190.88 | 5.507159 | 🔵 low — common in general English |
| 4636 | **combined** | 2 | 190.01 | 5.482261 | 🔵 low — common in general English |
| 4637 | **notes** | 2 | 190.01 | 5.482261 | 🔵 low — common in general English |
| 4638 | **paper** | 2 | 189.17 | 5.457969 | 🔵 low — common in general English |
| 4639 | **supplies** | 2 | 188.90 | 5.45 | 🔵 low — common in general English |
| 4640 | **outlook** | 2 | 188.62 | 5.442095 | 🔵 low — common in general English |
| 4641 | **moves** | 2 | 188.62 | 5.442095 | 🔵 low — common in general English |
| 4642 | **season** | 2 | 188.08 | 5.42647 | 🔵 low — common in general English |
| 4643 | **southern** | 2 | 187.81 | 5.418748 | 🔵 low — common in general English |
| 4644 | **limit** | 2 | 186.76 | 5.388443 | 🔵 low — common in general English |
| 4645 | **existing** | 2 | 186.25 | 5.373627 | 🔵 low — common in general English |
| 4646 | **aimed** | 2 | 185.74 | 5.359029 | 🔵 low — common in general English |
| 4647 | **unlikely** | 2 | 185.49 | 5.351808 | 🔵 low — common in general English |
| 4648 | **affected** | 2 | 185.24 | 5.34464 | 🔵 low — common in general English |
| 4649 | **discuss** | 2 | 185.00 | 5.337522 | 🔵 low — common in general English |
| 4650 | **dropped** | 2 | 185.00 | 5.337522 | 🔵 low — common in general English |
| 4651 | **court** | 2 | 185.00 | 5.337522 | 🔵 low — common in general English |
| 4652 | **spending** | 2 | 183.55 | 5.29585 | 🔵 low — common in general English |
| 4653 | **ahead** | 2 | 183.08 | 5.282336 | 🔵 low — common in general English |
| 4654 | **capacity** | 2 | 179.97 | 5.192532 | 🔵 low — common in general English |
| 4655 | **current** | 3 | 179.81 | 3.458653 | 🔵 low — common in general English |
| 4656 | **owns** | 2 | 179.76 | 5.186416 | 🔵 low — common in general English |
| 4657 | **mainly** | 2 | 179.13 | 5.168289 | 🔵 low — common in general English |
| 4658 | **quoted** | 2 | 177.51 | 5.121496 | 🔵 low — common in general English |
| 4659 | **changes** | 2 | 171.19 | 4.939175 | 🔵 low — common in general English |
| 4660 | **measures** | 2 | 170.86 | 4.929696 | 🔵 low — common in general English |
| 4661 | **addition** | 2 | 169.58 | 4.892655 | 🔵 low — common in general English |
| 4662 | **fed** | 2 | 169.42 | 4.88812 | 🔵 low — common in general English |
| 4663 | **planned** | 2 | 168.95 | 4.874636 | 🔵 low — common in general English |
| 4664 | **accord** | 2 | 168.34 | 4.856937 | 🔵 low — common in general English |
| 4665 | **expect** | 2 | 167.59 | 4.835244 | 🔵 low — common in general English |
| 4666 | **group** | 3 | 166.26 | 3.197874 | 🔵 low — common in general English |
| 4667 | **combines** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4668 | **audi** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4669 | **ale** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4670 | **leak** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4671 | **trusting** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4672 | **flavour** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4673 | **digging** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4674 | **strings** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4675 | **incorrectly** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4676 | **expedient** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4677 | **modes** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4678 | **savage** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4679 | **comprehend** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4680 | **hindrance** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4681 | **make-up** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4682 | **queens** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4683 | **unites** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4684 | **ensue** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4685 | **flagrant** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4686 | **autonomy** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4687 | **dominates** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4688 | **preoccupied** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4689 | **entailed** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4690 | **shuts** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4691 | **westward** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4692 | **presses** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4693 | **fruitful** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4694 | **coincidence** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4695 | **anchors** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4696 | **circular** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4697 | **fuse** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4698 | **torrential** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4699 | **flurries** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4700 | **wielding** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4701 | **lip** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4702 | **resists** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4703 | **cycles** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4704 | **good-looking** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4705 | **horror** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4706 | **cemetery** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4707 | **unsatisfied** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4708 | **reconciled** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4709 | **reversals** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4710 | **authoritative** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4711 | **aging** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4712 | **disenchanted** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4713 | **wanes** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4714 | **brave** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4715 | **recklessly** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4716 | **demise** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4717 | **enduring** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4718 | **suffice** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4719 | **unsurpassed** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4720 | **constellation** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4721 | **sheds** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4722 | **toss** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4723 | **tiger** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4724 | **trench** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4725 | **chewing** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4726 | **corners** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4727 | **snowy** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4728 | **lastly** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4729 | **brooms** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4730 | **weep** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4731 | **sacrificed** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4732 | **commanding** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4733 | **rang** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4734 | **orchard** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4735 | **fever** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4736 | **gigantic** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4737 | **stuff** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4738 | **horde** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4739 | **offload** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4740 | **comprehension** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4741 | **fas** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4742 | **musk-oxen** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4743 | **irrigated** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4744 | **rightful** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4745 | **propped** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4746 | **wastes** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4747 | **imbalanced** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4748 | **bedding** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4749 | **daytime** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4750 | **nights** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4751 | **treatments** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4752 | **colder** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4753 | **realizes** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4754 | **lure** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4755 | **kin** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4756 | **expresses** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4757 | **endangers** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4758 | **punished** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4759 | **organ** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4760 | **fights** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4761 | **engulfed** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4762 | **overwhelm** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4763 | **oceanic** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4764 | **transported** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4765 | **brother** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4766 | **inexorable** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4767 | **lymph** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4768 | **dictates** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4769 | **prolific** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4770 | **shocked** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4771 | **disdain** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4772 | **pulls** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4773 | **identifies** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4774 | **seizes** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4775 | **catches** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4776 | **throws** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4777 | **overpowering** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4778 | **seizure** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4779 | **burglar** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4780 | **indulge** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4781 | **needles** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4782 | **ethic** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4783 | **daylight** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4784 | **abilities** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4785 | **unsightly** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4786 | **congregation** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4787 | **summed** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4788 | **creator** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4789 | **receivers** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4790 | **negates** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4791 | **differently** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4792 | **destiny** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4793 | **loot** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4794 | **lays** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4795 | **falsely** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4796 | **recalcitrant** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4797 | **grim** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4798 | **obliges** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4799 | **seamless** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4800 | **plucked** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4801 | **squarely** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4802 | **airs** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4803 | **noticed** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4804 | **finer** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4805 | **ingenuity** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4806 | **absorbs** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4807 | **conformity** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4808 | **purest** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4809 | **blaze** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4810 | **incomprehensible** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4811 | **enquire** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4812 | **conveyance** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4813 | **tread** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4814 | **smoothly** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4815 | **respecting** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4816 | **examines** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4817 | **lethargy** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4818 | **praises** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4819 | **perfumes** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4820 | **makin** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4821 | **veins** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4822 | **harden** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4823 | **debating** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4824 | **appropriated** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4825 | **arts** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4826 | **demolished** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4827 | **storey** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4828 | **baskets** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4829 | **thrashing** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4830 | **reprimanded** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4831 | **calmed** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4832 | **crowned** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4833 | **wicks** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4834 | **commonplace** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4835 | **staffs** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4836 | **distinct** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4837 | **nightmare** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4838 | **ransom** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4839 | **cognizant** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4840 | **unquestionably** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4841 | **sym** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4842 | **intensely** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4843 | **straightforward** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4844 | **watchdog** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4845 | **imprisoned** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4846 | **invading** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4847 | **shelters** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4848 | **wings** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4849 | **inflict** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4850 | **crosses** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4851 | **afflicted** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4852 | **rider** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4853 | **stuffs** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4854 | **recognizes** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4855 | **intimidation** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4856 | **contravention** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4857 | **directives** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4858 | **cows** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4859 | **outraged** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4860 | **shedding** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4861 | **depart** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4862 | **tolerance** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4863 | **tenderness** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4864 | **flourish** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4865 | **towers** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4866 | **successors** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4867 | **lasted** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4868 | **doctors** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4869 | **dissuade** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4870 | **jugular** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4871 | **greed** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4872 | **flee** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4873 | **vicinity** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4874 | **overwhelmed** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4875 | **reappeared** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4876 | **boasting** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4877 | **sucked** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4878 | **games** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4879 | **futility** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4880 | **wealthier** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4881 | **dwindle** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4882 | **fare** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4883 | **aberration** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4884 | **mirage** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4885 | **ignores** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4886 | **omitting** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4887 | **subdivisions** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4888 | **summarized** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4889 | **imprints** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4890 | **slaughterers** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4891 | **thirty-five** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4892 | **instantly** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4893 | **colossal** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4894 | **transparent** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4895 | **banners** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4896 | **simplicity** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4897 | **chatting** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4898 | **smoking** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4899 | **abusing** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4900 | **subtle** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4901 | **occasional** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4902 | **infested** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4903 | **spoils** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4904 | **diseased** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4905 | **smashing** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4906 | **coral** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4907 | **ordinarily** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4908 | **ready-made** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4909 | **bountiful** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4910 | **commentary** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4911 | **impossibility** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4912 | **amazed** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4913 | **amazing** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4914 | **resigning** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4915 | **heats** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4916 | **imperfections** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4917 | **dispelled** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4918 | **rendered** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4919 | **loads** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4920 | **placated** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4921 | **females** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4922 | **subduing** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4923 | **scrape** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4924 | **severity** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4925 | **deepens** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4926 | **intel** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4927 | **exile** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4928 | **infinitesimal** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4929 | **bloom** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4930 | **layers** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4931 | **displays** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4932 | **rings** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4933 | **supposedly** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4934 | **violators** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4935 | **knowingly** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4936 | **demonstration** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4937 | **cleansing** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4938 | **spilt** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4939 | **reassured** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4940 | **mixes** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4941 | **predominate** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4942 | **quelling** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4943 | **propagated** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4944 | **bore** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4945 | **negligence** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4946 | **astonished** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4947 | **proceeded** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4948 | **vanished** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4949 | **uncontrolled** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4950 | **equality** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4951 | **translating** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4952 | **archives** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4953 | **traced** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4954 | **obstinate** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4955 | **unfabricated** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4956 | **accustomed** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4957 | **forcefully** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4958 | **brush** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4959 | **prematurely** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4960 | **sensation** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4961 | **skylight** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4962 | **inserting** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4963 | **winnowed** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4964 | **fertile** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4965 | **invented** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4966 | **azure** | 1 | 166.25 | 9.593135 | 🔵 low — common in general English |
| 4967 | **beamed** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 4968 | **elucidated** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 4969 | **wonderfully** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 4970 | **concerns-such** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 4971 | **whatever-is** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 4972 | **permeate** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 4973 | **circumambulations** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 4974 | **mantra-even** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 4975 | **mani-it** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 4976 | **torch** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 4977 | **akani** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 4978 | **tha** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 4979 | **unexcelled** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 4980 | **lotus-light** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 4981 | **divinities** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 4982 | **ever-revolving** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 4983 | **accomplishes** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 4984 | **buddha-nature** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 4985 | **adventitious** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 4986 | **entranced** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 4987 | **wanders** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 4988 | **tice** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 4989 | **teaching-which** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 4990 | **reasoning** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 4991 | **proudly** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 4992 | **minutely** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 4993 | **leapt** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 4994 | **moth** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 4995 | **lamp-flame** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 4996 | **carnivorous** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 4997 | **seduced** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 4998 | **bait** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 4999 | **gyalse** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5000 | **mru** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5001 | **nets** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5002 | **riverbed** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5003 | **indispensable-remembering** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5004 | **rat** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5005 | **dremo** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5006 | **marmots** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5007 | **sleepy** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5008 | **weren** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5009 | **loosely** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5010 | **mealtimes** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5011 | **elegant** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5012 | **meaning-you** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5013 | **debase** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5014 | **everything-the** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5015 | **teachings-properly** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5016 | **disheart** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5017 | **ened** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5018 | **elementary** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5019 | **prescribes** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5020 | **dharma-that** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5021 | **practice-is** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5022 | **medications** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5023 | **death-bed** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5024 | **rushes** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5025 | **helplessly** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5026 | **perilous** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5027 | **conquers** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5028 | **libera** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5029 | **shallow-tongued** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5030 | **natures** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5031 | **sneer** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5032 | **mal** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5033 | **iala** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5034 | **joyfully** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5035 | **canes** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5036 | **swathed** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5037 | **turbans** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5038 | **atakas** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5039 | **dignified** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5040 | **barbarian** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5041 | **oppor** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5042 | **tunity** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5043 | **barbarians** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5044 | **khatha** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5045 | **outlying** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5046 | **attune** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5047 | **forefathers** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5048 | **eternalist** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5049 | **nihilist** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5050 | **aspiring** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5051 | **liyana** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5052 | **atten** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5053 | **dant** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5054 | **oll** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5055 | **description** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5056 | **dysfunction** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5057 | **disability** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5058 | **deprives** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5059 | **unheard** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5060 | **disabilities** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5061 | **animal-even** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5062 | **prized** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5063 | **padme** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5064 | **heap-whereas** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5065 | **conceive** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5066 | **pratimoksa** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5067 | **dharma-the** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5068 | **buddha-exists** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5069 | **sparsely** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5070 | **whjch** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5071 | **scripts** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5072 | **intro** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5073 | **duced** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5074 | **princesses** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5075 | **mikyo** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5076 | **rasa** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5077 | **trulnang** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5078 | **estab** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5079 | **lished** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5080 | **kingtrisong** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5081 | **mantra-holders** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5082 | **sustras** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5083 | **dharma-for** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5084 | **queror** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5085 | **preached** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5086 | **extant** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5087 | **ahhough** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5088 | **destroyer-of-samsara** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5089 | **incalculably** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5090 | **infinite-aspiration** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5091 | **alternation** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5092 | **promulgated** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5093 | **once-come-king** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5094 | **trayana** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5095 | **uncompounded** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5096 | **interpreter** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5097 | **kham** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5098 | **degenerations-those** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5099 | **it-just** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5100 | **transmis** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5101 | **infiltrate** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5102 | **condense** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5103 | **important-the** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5104 | **canonical** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5105 | **commentar** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5106 | **ies** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5107 | **practice-even** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5108 | **triptaka** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5109 | **metaphysics** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5110 | **piety** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5111 | **illustrates** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5112 | **condi** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5113 | **endowed** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5114 | **enslavement** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5115 | **hypocritical** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5116 | **intrusive** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5117 | **depravity** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5118 | **heedlessness** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5119 | **poisons-that** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5120 | **dominat** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5121 | **plishing** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5122 | **perverted** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5123 | **lazy** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5124 | **indolence** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5125 | **life-that** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5126 | **impostors** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5127 | **pretence** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5128 | **humanity** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5129 | **depraved** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5130 | **suffedngs** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5131 | **sarilsa** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5132 | **plishments** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5133 | **snuff** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5134 | **chieftain** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5135 | **parasol** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5136 | **worth-each** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5137 | **thirty-four** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5138 | **squander** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5139 | **mter** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5140 | **realiza** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5141 | **goal-the** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5142 | **dharma-is** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5143 | **junction** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5144 | **interconnected** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5145 | **elements-the** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5146 | **flint** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5147 | **rarer** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5148 | **advan** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5149 | **tages** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5150 | **perchance** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5151 | **adrift** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5152 | **shoreless** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5153 | **needle-which** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5154 | **saddened** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5155 | **fritter** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5156 | **jettison** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5157 | **trakpa** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5158 | **resourcefulness** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5159 | **raft** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5160 | **thing-the** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5161 | **preme** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5162 | **dharma-and** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5163 | **ineffectual** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5164 | **folly** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5165 | **betray** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5166 | **turning-point** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5167 | **bewildered** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5168 | **miyowa** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5169 | **fashioned** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5170 | **god-realm** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5171 | **fruit-bearing** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5172 | **creeks** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5173 | **manasarovar** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5174 | **sea-water** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5175 | **ear-shot** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5176 | **footprint** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5177 | **snow-covered** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5178 | **sub-continents** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5179 | **rim** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5180 | **wards** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5181 | **flares** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5182 | **engulf** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5183 | **conflagration** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5184 | **destructions** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5185 | **rainclouds** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5186 | **devastation** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5187 | **sincerely-if** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5188 | **realm-even** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5189 | **gods-who** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5190 | **sayings** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5191 | **flickers** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5192 | **departs** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5193 | **slumber** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5194 | **ever-present** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5195 | **status-until** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5196 | **gnashing** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5197 | **fangs** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5198 | **soldier** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5199 | **decrees** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5200 | **charms** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5201 | **athlete** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5202 | **fleetness-none** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5203 | **impene** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5204 | **trable** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5205 | **concealment** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5206 | **secures** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5207 | **glaze** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5208 | **willy-nilly** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5209 | **defender** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5210 | **you-can** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5211 | **dispensation** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5212 | **miracu** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5213 | **lous** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5214 | **ofyerpa** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5215 | **zur** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5216 | **nub** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5217 | **clans** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5218 | **plished** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5219 | **transformations** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5220 | **space-they** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5221 | **silence** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5222 | **nyeshangkatya** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5223 | **motionless** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5224 | **volley** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5225 | **cliff-but** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5226 | **firewood** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5227 | **contraption** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5228 | **depends-and** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5229 | **scarecrow** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5230 | **momerit** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5231 | **illustrious** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5232 | **statures** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5233 | **earshots** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5234 | **resplendence** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5235 | **outshine** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5236 | **mahdvara** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5237 | **monarchs** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5238 | **evade** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5239 | **consolation** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5240 | **mahasammata** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5241 | **palas** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5242 | **candras** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5243 | **nivara** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5244 | **tavi** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5245 | **kambhin** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5246 | **earthly** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5247 | **lek** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5248 | **jambu** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5249 | **dvipa** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5250 | **ralpachen** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5251 | **gesar** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5252 | **tajikistan** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5253 | **ambassa** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5254 | **dors** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5255 | **splendours** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5256 | **beehive** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5257 | **race** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5258 | **abstinence** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5259 | **summertime** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5260 | **lush** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5261 | **bask** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5262 | **blossoms** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5263 | **scarlet** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5264 | **grasslands** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5265 | **hue** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5266 | **brittle** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5267 | **glacial** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5268 | **scour** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5269 | **helpless** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5270 | **grandparents** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5271 | **great-grandparents** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5272 | **eminent** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5273 | **year-or** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5274 | **animals-sheep** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5275 | **dogs-how** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5276 | **animate** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5277 | **mind-everything** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5278 | **exalted** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5279 | **rainbow-but** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5280 | **stiffly** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5281 | **armpits** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5282 | **cherished** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5283 | **thread** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5284 | **beloved** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5285 | **brocades** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5286 | **handsome** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5287 | **distinguished** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5288 | **horribly** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5289 | **livid** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5290 | **here-our** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5291 | **trussed** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5292 | **curtain** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5293 | **furs** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5294 | **sheepskin** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5295 | **rugs** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5296 | **tuft** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5297 | **bespattered** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5298 | **cremating** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5299 | **vagabond** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5300 | **enjoy-teachers** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5301 | **proteges** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5302 | **comrades** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5303 | **husbands** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5304 | **wives-there** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5305 | **three-storeyed** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5306 | **emanated** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5307 | **rivalled** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5308 | **kagyupas** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5309 | **wield** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5310 | **governments-not** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5311 | **languishing** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5312 | **alms-round** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5313 | **sworn** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5314 | **intimately** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5315 | **paltry** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5316 | **insignifi** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5317 | **cant** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5318 | **deprivation** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5319 | **well-off** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5320 | **merry** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5321 | **nightfall** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5322 | **unparalleled** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5323 | **aparantaka** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5324 | **more-and** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5325 | **ever-changing** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5326 | **comforts** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5327 | **mediocrity** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5328 | **eloquent** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5329 | **despises** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5330 | **liars** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5331 | **common-sense** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5332 | **trusted** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5333 | **esteemed** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5334 | **busily** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5335 | **preceptors** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5336 | **tricked** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5337 | **conscientious** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5338 | **stantly** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5339 | **poignant** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5340 | **transitoriness** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5341 | **feud** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5342 | **gelong** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5343 | **pigeons** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5344 | **exterminate** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5345 | **commander** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5346 | **superficial** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5347 | **waxes** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5348 | **savages** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5349 | **beasts-all** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5350 | **lifesustaining** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5351 | **fatalities** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5352 | **eating-the** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5353 | **oblivious** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5354 | **mear** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5355 | **unhealthy** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5356 | **diets** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5357 | **tumours** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5358 | **dropsy** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5359 | **glories** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5360 | **incites** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5361 | **decrepit** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5362 | **linger** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5363 | **glued** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5364 | **skeletons** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5365 | **candle-flame** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5366 | **celebrity** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5367 | **ences** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5368 | **sorrowful** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5369 | **escaping** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5370 | **bhik** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5371 | **ractice** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5372 | **sameness** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5373 | **insatiable** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5374 | **whips** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5375 | **valuables** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5376 | **bribes** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5377 | **ha-ha** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5378 | **proudest** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5379 | **hermits** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5380 | **engross** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5381 | **renunciates** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5382 | **revel** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5383 | **abhorrent** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5384 | **permeates** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5385 | **sealing** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5386 | **vaster** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5387 | **attachments** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5388 | **thrones** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5389 | **silks** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5390 | **twinkling** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5391 | **headlong** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5392 | **scorching** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5393 | **storeys** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5394 | **perimeter** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5395 | **white-hot** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5396 | **smith-there** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5397 | **searingly** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5398 | **incandescent** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5399 | **snowflakes** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5400 | **furiously** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5401 | **weapons-a** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5402 | **armoury** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5403 | **fifty** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5404 | **firebrands** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5405 | **cross-rule** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5406 | **on-which** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5407 | **saws** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5408 | **hacked** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5409 | **whirling** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5410 | **mers** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5411 | **stags** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5412 | **rams** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5413 | **butt** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5414 | **horn-tips** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5415 | **spewing** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5416 | **scream** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5417 | **shove** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5418 | **howl** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5419 | **cauldrons** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5420 | **hooks** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5421 | **moments** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5422 | **impale** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5423 | **tridents** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5424 | **edifice** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5425 | **coals** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5426 | **bellows** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5427 | **leopard-skin** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5428 | **indis** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5429 | **tinguishable** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5430 | **cries** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5431 | **razor-edged** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5432 | **directions-the** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5433 | **northeast-stands** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5434 | **purged** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5435 | **shady** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5436 | **putrescent** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5437 | **brazier** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5438 | **corpses-corpses** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5439 | **dogs-all** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5440 | **decomposing** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5441 | **decompose** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5442 | **foulest** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5443 | **stenches** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5444 | **mire** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5445 | **thrilled** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5446 | **slender** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5447 | **heals** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5448 | **it-only** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5449 | **excruciatingly** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5450 | **reconstitute** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5451 | **eagerly** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5452 | **ravens** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5453 | **vultures** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5454 | **stabbing** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5455 | **metallic** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5456 | **unshake** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5457 | **glaciers** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5458 | **perpetually** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5459 | **enveloped** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5460 | **blizzards** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5461 | **lamentations** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5462 | **ofutpala-like** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5463 | **petal-like** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5464 | **unbearably** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5465 | **pans** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5466 | **pillars** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5467 | **bobs** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5468 | **ropes** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5469 | **yutso** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5470 | **ngonmo** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5471 | **snpo** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5472 | **lung** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5473 | **kangchen** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5474 | **zemaguru** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5475 | **exclaiming** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5476 | **misused** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5477 | **spanned** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5478 | **squirming** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5479 | **tsangla** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5480 | **tanakchen** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5481 | **angtong** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5482 | **exercises** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5483 | **patron** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5484 | **cooks** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5485 | **gullet** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5486 | **kidneys** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5487 | **shawl** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5488 | **munch** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5489 | **leisurely** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5490 | **steaming** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5491 | **whiskers** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5492 | **reddish** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5493 | **tinge** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5494 | **palden** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5495 | **chokyong** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5496 | **ngor** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5497 | **ngulda** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5498 | **tree-trunk** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5499 | **aher** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5500 | **pogye** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5501 | **all-powerful** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5502 | **dignitaries** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5503 | **srm** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5504 | **adulterer** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5505 | **infidelity** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5506 | **lunch-hour** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5507 | **obdurate** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5508 | **karmapa** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5509 | **impulsively** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5510 | **exhausted-only** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5511 | **stony** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5512 | **torture** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5513 | **sroi** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5514 | **sombre** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5515 | **throats** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5516 | **horse-hair** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5517 | **stomachs** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5518 | **if-finally-enough** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5519 | **grass-like** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5520 | **devouring** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5521 | **exquisitely** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5522 | **bedecked** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5523 | **ravishing** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5524 | **srol** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5525 | **daughter-in** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5526 | **shaven-skulled** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5527 | **proposition** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5528 | **bald-head** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5529 | **prostitute** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5530 | **pots** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5531 | **ablution** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5532 | **squashed** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5533 | **torma** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5534 | **jostling** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5535 | **thing-except** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5536 | **shindre** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5537 | **jungpo** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5538 | **theurang** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5539 | **relive** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5540 | **insanity** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5541 | **fragments** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5542 | **bums** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5543 | **teem** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5544 | **reptiles** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5545 | **turtles** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5546 | **shellfish** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5547 | **beer-barrel** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5548 | **burrow** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5549 | **torturing** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5550 | **devices-nets** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5551 | **snares** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5552 | **traps** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5553 | **guns** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5554 | **oysters** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5555 | **otters** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5556 | **foxes** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5557 | **asses** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5558 | **domesticated** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5559 | **executioner** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5560 | **stare** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5561 | **pierced** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5562 | **yoked** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5563 | **escapes** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5564 | **continual** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5565 | **pelted** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5566 | **long-lasting** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5567 | **lated** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5568 | **scorning** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5569 | **old-age** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5570 | **hated** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5571 | **wracked** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5572 | **spasms** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5573 | **parasites** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5574 | **plunders** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5575 | **news-and** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5576 | **imme** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5577 | **diately** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5578 | **constancy** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5579 | **adornments** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5580 | **concoction** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5581 | **six-brick** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5582 | **packs** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5583 | **dotok** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5584 | **dzo** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5585 | **perforated** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5586 | **patches** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5587 | **chafed** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5588 | **lambskins** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5589 | **fleas** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5590 | **ticks** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5591 | **strands** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5592 | **decapitated** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5593 | **suffocate** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5594 | **instants** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5595 | **die-they** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5596 | **buries** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5597 | **crows** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5598 | **incessantly** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5599 | **aquatic** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5600 | **threshing** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5601 | **untainted** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5602 | **suckle** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5603 | **necks** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5604 | **tethered** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5605 | **pauses** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5606 | **journeys** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5607 | **milk-their** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5608 | **drink-can** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5609 | **stalls** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5610 | **starved** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5611 | **skeleton-like** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5612 | **stagger** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5613 | **constituting** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5614 | **happiness-food** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5615 | **of-are** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5616 | **interpose** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5617 | **embryonic** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5618 | **jelly** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5619 | **viscous** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5620 | **ellipse** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5621 | **oblong** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5622 | **oval** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5623 | **appendages** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5624 | **sense-organs** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5625 | **suffocating** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5626 | **uterus** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5627 | **walks** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5628 | **buffeted** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5629 | **cervix** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5630 | **pelvis** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5631 | **draw-plate** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5632 | **wrenched** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5633 | **ever-unfinished** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5634 | **creeps** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5635 | **eyesight** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5636 | **dims** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5637 | **articulate** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5638 | **unintelligible** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5639 | **mumble** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5640 | **impa** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5641 | **tient** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5642 | **scorned** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5643 | **protrude** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5644 | **shrunk** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5645 | **dazed** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5646 | **trampled** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5647 | **waist** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5648 | **gingerly** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5649 | **arthritic** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5650 | **cheek-bones** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5651 | **protuberances** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5652 | **dull-witted** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5653 | **giddy** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5654 | **brightness** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5655 | **foreheads** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5656 | **humour** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5657 | **scorns** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5658 | **illnesses-those** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5659 | **bile** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5660 | **on-arise** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5661 | **twinges** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5662 | **strike-however** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5663 | **radiantly** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5664 | **prime-we** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5665 | **crumple** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5666 | **evaporates** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5667 | **bloodletting** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5668 | **cautery** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5669 | **terrifies** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5670 | **morbid** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5671 | **epilepsy** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5672 | **short-tempered** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5673 | **forebodings** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5674 | **departure-you** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5675 | **overtakes** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5676 | **menacing** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5677 | **hoarse** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5678 | **brigands** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5679 | **burglars** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5680 | **envied** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5681 | **knots** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5682 | **attracts** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5683 | **drags** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5684 | **devils** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5685 | **adage** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5686 | **compatriots** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5687 | **dangers-and** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5688 | **inescapably** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5689 | **girls** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5690 | **through-but** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5691 | **wheedle** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5692 | **gods-as** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5693 | **malice** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5694 | **deign** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5695 | **swindler** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5696 | **tethers** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5697 | **imperiously** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5698 | **monopolizing** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5699 | **steals** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5700 | **sly** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5701 | **despair** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5702 | **calamity** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5703 | **ravaging** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5704 | **incurable** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5705 | **lllead** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5706 | **dining** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5707 | **expend** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5708 | **accomplished-and** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5709 | **slaves** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5710 | **dharmaless** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5711 | **whence** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5712 | **aren** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5713 | **nowa** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5714 | **degeneration** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5715 | **accelerates** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5716 | **mealtime** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5717 | **decaying** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5718 | **everything-good** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5719 | **not-highly** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5720 | **appalled** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5721 | **subsides** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5722 | **pitiful** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5723 | **multiplicity** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5724 | **quarrelling** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5725 | **tree-whose** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5726 | **donning** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5727 | **rides** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5728 | **splendour** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5729 | **weapons-vajras** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5730 | **laps** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5731 | **taller** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5732 | **demi** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5733 | **dispatch** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5734 | **all-protector** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5735 | **crazed** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5736 | **fastened** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5737 | **exuberant** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5738 | **diversions** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5739 | **pleases** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5740 | **wore** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5741 | **perspired** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5742 | **sweethearts** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5743 | **despairs** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5744 | **realiz** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5745 | **powerlessness** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5746 | **birthplace** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5747 | **multiplies** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5748 | **suffering-and** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5749 | **murderous** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5750 | **ogresses** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5751 | **hell-fire** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5752 | **mindlessness** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5753 | **smells** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5754 | **snow-mountain** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5755 | **she-monkey** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5756 | **pur** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5757 | **larika** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5758 | **pundarika** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5759 | **intimate** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5760 | **heartbroken** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5761 | **slighdy** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5762 | **extolled** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5763 | **sense-doors** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5764 | **frighten** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5765 | **saligha** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5766 | **assembly-halls** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5767 | **descriptions** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5768 | **balcony** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5769 | **overlooking** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5770 | **moorings** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5771 | **preoccupations-parents** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5772 | **possessions-like** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5773 | **mist** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5774 | **esteem** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5775 | **worm-fodder** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5776 | **watch-tower** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5777 | **gloomy-face** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5778 | **cheery** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5779 | **turnings** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5780 | **all-determining** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5781 | **consigns** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5782 | **do-is** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5783 | **underfoot** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5784 | **gusto** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5785 | **guest** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5786 | **wher** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5787 | **tea-parties** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5788 | **receptions** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5789 | **hooves** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5790 | **swamped** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5791 | **fleece** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5792 | **lambing** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5793 | **dowry** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5794 | **in-laws** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5795 | **pretentious** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5796 | **breast-meat** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5797 | **tripe** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5798 | **gobbles** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5799 | **bloody** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5800 | **willow-wand** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5801 | **indeed-considering** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5802 | **mothers-we** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5803 | **gun** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5804 | **thereupon** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5805 | **sundered** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5806 | **involved-a** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5807 | **lashes** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5808 | **thongs** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5809 | **suffocates** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5810 | **bluish** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5811 | **stain** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5812 | **not-or** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5813 | **subterfuges** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5814 | **contexts** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5815 | **deceiving** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5816 | **debilitates** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5817 | **poring** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5818 | **overpowers** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5819 | **shoulder-blade** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5820 | **knuckles** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5821 | **shins** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5822 | **daybreak** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5823 | **wink** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5824 | **devotions** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5825 | **torrna-offerings** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5826 | **carne** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5827 | **disdainfully** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5828 | **railed** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5829 | **dharma-practitioner** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5830 | **slander** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5831 | **wares** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5832 | **extort** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5833 | **haggling** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5834 | **covet** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5835 | **vaisravana** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5836 | **nefarious** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5837 | **breasts** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5838 | **obsessions** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5839 | **millstones** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5840 | **corrupting** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5841 | **awls** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5842 | **laity** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5843 | **gravest** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5844 | **particu** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5845 | **lar** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5846 | **masturbation** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5847 | **bereavement** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5848 | **menstruation** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5849 | **recov** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5850 | **ery** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5851 | **child-birth** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5852 | **prepubescent** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5853 | **devastatingly** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5854 | **imposters** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5855 | **thanksgiving** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5856 | **chastised** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5857 | **concept-bound** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5858 | **second-and** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5859 | **rude** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5860 | **sweetly** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5861 | **imagines** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5862 | **not-such** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5863 | **aimlessly** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5864 | **libidinous** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5865 | **cussing** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5866 | **disturb** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5867 | **gossip-monger** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5868 | **rituals-just** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5869 | **perfunctorily** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5870 | **sorcerers-is** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5871 | **cast-iron** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5872 | **lethally** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5873 | **life-artery** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5874 | **desirous** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5875 | **acquisitive** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5876 | **contemplat** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5877 | **agreeable** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5878 | **invent** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5879 | **malicious** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5880 | **catego** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5881 | **ries** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5882 | **eternalists** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5883 | **eternally** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5884 | **nihilists** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5885 | **roundness** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5886 | **iridescent** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5887 | **sharpened** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5888 | **peacock** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5889 | **bad-all** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5890 | **spontane** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5891 | **ously** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5892 | **commentators** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5893 | **unvirtuous** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5894 | **mistakenly** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5895 | **meri** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5896 | **torious** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5897 | **givers** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5898 | **resuscitate** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5899 | **impulse-extremely** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5900 | **ignorance-motivating** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5901 | **instinct** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5902 | **falcons** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5903 | **mice** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5904 | **newborn** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5905 | **adulthood** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5906 | **assaulted** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5907 | **pillage** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5908 | **calamities** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5909 | **bandits** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5910 | **raids-often** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5911 | **life-or** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5912 | **bereft** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5913 | **destitute** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5914 | **preta-like** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5915 | **indulged** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5916 | **hating** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5917 | **belittled** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5918 | **hurling** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5919 | **destroys** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5920 | **argumentative** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5921 | **defiantly** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5922 | **chores** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5923 | **grudgingly** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5924 | **recon** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5925 | **ciling** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5926 | **insulting** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5927 | **provokes** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5928 | **or-worse** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5929 | **still-to** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5930 | **kapila** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5931 | **horse-head** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5932 | **ox-head** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5933 | **fish-like** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5934 | **extol** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5935 | **denigrate** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5936 | **self-assurance** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5937 | **joyless** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5938 | **mortally** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5939 | **swamps** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5940 | **insecu** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5941 | **rity** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5942 | **inhabit** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5943 | **gorges** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5944 | **terrain** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5945 | **infertile** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5946 | **untimely** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5947 | **inhospitable** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5948 | **proliferate** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5949 | **example-or** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5950 | **animals-is** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5951 | **vaisakha** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5952 | **reconcile** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5953 | **uninterrupted** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5954 | **experiences-from** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5955 | **hell-arise** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5956 | **impels** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5957 | **identifiable** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5958 | **sravasti** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5959 | **pole** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5960 | **writhed** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5961 | **fishes** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5962 | **matropakara** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5963 | **tied-up** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5964 | **writhing** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5965 | **laughed** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5966 | **acacia** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5967 | **splinter-the** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5968 | **parivraji** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5969 | **kas** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5970 | **succumbed** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5971 | **jeta** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5972 | **suf** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5973 | **fering** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5974 | **clairvoyant** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5975 | **woodland** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5976 | **stoking** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5977 | **punish** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5978 | **debili** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5979 | **tated** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5980 | **blade** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5981 | **nagar** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5982 | **juna** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5983 | **we-whose** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5984 | **innumerable-ever** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5985 | **misdeed** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5986 | **underestimate** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5987 | **minutest** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5988 | **disparage** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5989 | **wedding** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5990 | **fistful** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5991 | **antisarar** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5992 | **devo** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5993 | **indras** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5994 | **profuse** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5995 | **vajrap** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5996 | **pirate** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5997 | **non-returning** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5998 | **hopelessly** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 5999 | **wrong-doer** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6000 | **impression-or** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6001 | **generator** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6002 | **moti** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6003 | **vation** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6004 | **neatly** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6005 | **kungyal** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6006 | **stumbled** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6007 | **penyulgyal** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6008 | **yoghurt-addict** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6009 | **self-centredness** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6010 | **expectant** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6011 | **ravi** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6012 | **cutter** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6013 | **tormented-in** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6014 | **tormented-by** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6015 | **scorn** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6016 | **prattling** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6017 | **materialism** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6018 | **ideology** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6019 | **tiness** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6020 | **authentically** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6021 | **heaping** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6022 | **ments-and** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6023 | **dhara** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6024 | **unreal** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6025 | **mingle** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6026 | **pathways** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6027 | **practices-the** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6028 | **formless** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6029 | **insight-should** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6030 | **sastra** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6031 | **take-while** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6032 | **impregnated** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6033 | **moist** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6034 | **whomever** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6035 | **prohibitions** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6036 | **vow-the** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6037 | **knowl** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6038 | **sastras** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6039 | **practices-out** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6040 | **wardly** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6041 | **actualized** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6042 | **observance** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6043 | **unbroken** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6044 | **preoc** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6045 | **cupations** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6046 | **seing** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6047 | **commands** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6048 | **resolutely** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6049 | **nephew** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6050 | **descendants** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6051 | **mundane** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6052 | **reasons-like** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6053 | **priestly** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6054 | **incumbents** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6055 | **suited** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6056 | **pedestal** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6057 | **visitor** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6058 | **fainted** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6059 | **ape** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6060 | **idiot** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6061 | **well-bound** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6062 | **leaping** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6063 | **venomous** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6064 | **coiled** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6065 | **beguiled** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6066 | **unmistaken** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6067 | **uniquely** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6068 | **endures** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6069 | **ples** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6070 | **expediently** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6071 | **noblest** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6072 | **unfailingly** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6073 | **downpour** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6074 | **extinguishes** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6075 | **dispels** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6076 | **agement** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6077 | **unfolds** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6078 | **charting** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6079 | **quenching** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6080 | **inferno** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6081 | **showered** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6082 | **wayfarers** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6083 | **ferryman** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6084 | **stable-minded** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6085 | **obeys** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6086 | **all-such** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6087 | **sittra** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6088 | **anged** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6089 | **resentful** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6090 | **reprimands** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6091 | **resent** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6092 | **disregarding** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6093 | **incomprehensibly** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6094 | **ruined** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6095 | **tub** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6096 | **grilled** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6097 | **snapping** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6098 | **flawless** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6099 | **deceitful** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6100 | **glimpsed** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6101 | **outburst** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6102 | **attendant** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6103 | **treading** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6104 | **vanity** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6105 | **discontent** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6106 | **unconsidered** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6107 | **insincere** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6108 | **laughing** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6109 | **joking** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6110 | **chat** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6111 | **awe** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6112 | **casualness** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6113 | **solicitously** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6114 | **vainly** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6115 | **scowl** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6116 | **ill-considered** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6117 | **composure** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6118 | **disparages** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6119 | **conver** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6120 | **sations** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6121 | **self-im** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6122 | **portance** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6123 | **untiringly** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6124 | **gliding** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6125 | **delighting** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6126 | **spoiling** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6127 | **bored** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6128 | **steadfastness** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6129 | **tasting** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6130 | **accumulates** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6131 | **better-off** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6132 | **fellow-voyager** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6133 | **bean-tsampa** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6134 | **fruitful-this** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6135 | **contemplation** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6136 | **profundities** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6137 | **portrait** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6138 | **epitomizes** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6139 | **assiduous** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6140 | **examina** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6141 | **saints** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6142 | **abound** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6143 | **deception** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6144 | **voice-or** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6145 | **name-can** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6146 | **restless** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6147 | **transfixed** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6148 | **imitates** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6149 | **reproduces** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6150 | **emulates** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6151 | **limb-just** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6152 | **ropa** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6153 | **bodily** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6154 | **prajna** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6155 | **go-and** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6156 | **abode** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6157 | **circumference** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6158 | **sixty-eight** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6159 | **blissfully** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6160 | **sadapraru** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6161 | **dita** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6162 | **marrow** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6163 | **spurted** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6164 | **smash** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6165 | **inflicting** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6166 | **reassumed** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6167 | **domain** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6168 | **mersed** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6169 | **prajaa** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6170 | **deco** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6171 | **filigree** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6172 | **censers** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6173 | **wafted** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6174 | **aloe-wood** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6175 | **pranaparamita** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6176 | **sada** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6177 | **prarudita** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6178 | **sprinkle** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6179 | **sprinkled** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6180 | **lion-throne** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6181 | **expounded** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6182 | **buddhas-a** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6183 | **proclaims** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6184 | **melodious** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6185 | **oiling** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6186 | **bearable** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6187 | **streamed** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6188 | **these-twenty-four** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6189 | **forbade** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6190 | **pandita-gatekeeper** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6191 | **magadha** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6192 | **insistently** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6193 | **compassion-why** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6194 | **gatekeeper** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6195 | **retorted** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6196 | **ngari** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6197 | **gungthang** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6198 | **sherab** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6199 | **thopa-ga** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6200 | **yungdrung** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6201 | **throgyal** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6202 | **lharje** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6203 | **nupchung** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6204 | **hailstorm** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6205 | **repenting** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6206 | **eminently** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6207 | **hail-if** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6208 | **night-and** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6209 | **suffuse** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6210 | **tingled** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6211 | **tarma** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6212 | **dode** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6213 | **continu** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6214 | **clothe** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6215 | **reckon** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6216 | **acquiesced** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6217 | **twelve-pillared** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6218 | **sanctuary** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6219 | **meton** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6220 | **tsonpo** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6221 | **tsangrong** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6222 | **sarilvara** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6223 | **tsurton** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6224 | **wange** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6225 | **dol** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6226 | **guhyasamaja** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6227 | **ngokton** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6228 | **chador** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6229 | **shung** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6230 | **khok** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6231 | **powerment** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6232 | **dispersed** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6233 | **mahasiddha** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6234 | **tacarya** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6235 | **floundering** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6236 | **multitudes** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6237 | **degenerations** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6238 | **byways** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6239 | **vajrasativa** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6240 | **life-story** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6241 | **sprout** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6242 | **bestowing** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6243 | **departed-i** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6244 | **simple-minded** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6245 | **caretaker** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6246 | **food-offerings** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6247 | **butter-lamps** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6248 | **imagined** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6249 | **dunking** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6250 | **sputter** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6251 | **tthrow** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6252 | **though-so** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6253 | **jowo-acts** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6254 | **wrong-the** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6255 | **leavingjetsun** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6256 | **unwavering** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6257 | **realms-the** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6258 | **realm-motivates** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6259 | **beings-our** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6260 | **beginnin** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6261 | **gless** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6262 | **time-are** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6263 | **dhar** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6264 | **makaya** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6265 | **indestructible** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6266 | **all-pervasive** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6267 | **mindstream** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6268 | **inseparability** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6269 | **irregulari** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6270 | **twig** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6271 | **entrancing** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6272 | **bells** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6273 | **lions** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6274 | **multi-coloured** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6275 | **cloak** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6276 | **sleeved** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6277 | **tunic** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6278 | **samantab** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6279 | **jnanasiltra** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6280 | **consort-the** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6281 | **trisongdetsen** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6282 | **nirmanakya** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6283 | **garbed** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6284 | **hood-the** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6285 | **right-hand** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6286 | **families-mafijusri** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6287 | **left-hand** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6288 | **alms-bowls** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6289 | **topmost** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6290 | **resonate** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6291 | **melody** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6292 | **vowels** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6293 | **consonants** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6294 | **dharma-protectors** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6295 | **hindrances** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6296 | **leaking** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6297 | **detest** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6298 | **refuge-prayer** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6299 | **precedence** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6300 | **kinder** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6301 | **possessions-the** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6302 | **aunt** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6303 | **palmo** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6304 | **assailed** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6305 | **invade** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6306 | **fearlessness** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6307 | **ghosts** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6308 | **impelled** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6309 | **slingstone** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6310 | **whirring** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6311 | **tirthika-who** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6312 | **denigrates** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6313 | **fragment** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6314 | **breeze** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6315 | **day-comes** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6316 | **rends** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6317 | **douds** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6318 | **healing** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6319 | **life-comfort** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6320 | **whatever-spring** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6321 | **create-prostrations** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6322 | **disciples-to** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6323 | **nicknamed** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6324 | **paintings** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6325 | **pawned** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6326 | **saliva** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6327 | **maxim** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6328 | **ensures** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6329 | **vajradhatvishvari** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6330 | **seed-syllables** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6331 | **consorts** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6332 | **ialas** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6333 | **disre** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6334 | **spect** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6335 | **seventy** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6336 | **stanzas** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6337 | **reparation** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6338 | **tenuous** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6339 | **people-the** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6340 | **moulded** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6341 | **it-all** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6342 | **seductive** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6343 | **gullible** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6344 | **decadence** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6345 | **deceived** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6346 | **seductions** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6347 | **invaded** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6348 | **hesita** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6349 | **guises** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6350 | **disciples-none** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6351 | **goggle** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6352 | **effigy** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6353 | **goat-pen** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6354 | **legitimately** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6355 | **perni** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6356 | **cious** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6357 | **malevolent** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6358 | **confi** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6359 | **dence** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6360 | **pacified** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6361 | **harm-the** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6362 | **makers-will** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6363 | **quarter-pint** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6364 | **faint-hearted** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6365 | **pathetic** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6366 | **even-minded** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6367 | **on-while** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6368 | **low-caste** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6369 | **stung** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6370 | **brushing** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6371 | **accidentally** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6372 | **characters** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6373 | **diffi** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6374 | **culties** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6375 | **obsession** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6376 | **all-those** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6377 | **you-train** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6378 | **beings-whether** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6379 | **between-as** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6380 | **mindless** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6381 | **sages** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6382 | **distinc** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6383 | **devoting** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6384 | **cosy** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6385 | **glared** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6386 | **endeavouring** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6387 | **jeal** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6388 | **ousy** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6389 | **hypocrite** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6390 | **ity** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6391 | **despise** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6392 | **distressed** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6393 | **khotan** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6394 | **mafljusri** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6395 | **punishments** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6396 | **prisoners** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6397 | **dismembered** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6398 | **vanquished** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6399 | **frontiers** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6400 | **dwellings** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6401 | **chicks** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6402 | **nest** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6403 | **torment-a** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6404 | **bursting** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6405 | **butchered** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6406 | **delay-this** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6407 | **barbarity** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6408 | **strand** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6409 | **twist** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6410 | **belly-hairs** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6411 | **weal** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6412 | **grunting** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6413 | **blister** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6414 | **backsides** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6415 | **horseback** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6416 | **sidesaddle** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6417 | **stumbles** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6418 | **sympathy** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6419 | **animal-a** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6420 | **example-that** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6421 | **paralyzing** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6422 | **blood-blister** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6423 | **gutted** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6424 | **bled** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6425 | **flesh-eating** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6426 | **renunciate** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6427 | **resourceful** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6428 | **venerables** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6429 | **twine** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6430 | **ring-hole** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6431 | **gouged** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6432 | **hoisted** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6433 | **yak-hair** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6434 | **cord** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6435 | **digs** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6436 | **whacks** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6437 | **aching** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6438 | **rasps** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6439 | **slams** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6440 | **rump** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6441 | **flanks** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6442 | **bruised** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6443 | **stirrups** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6444 | **descents** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6445 | **glimmers** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6446 | **exhausting** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6447 | **help-impartial** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6448 | **ganging** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6449 | **mischievous** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6450 | **intoning** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6451 | **impartial** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6452 | **horrible** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6453 | **hurled** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6454 | **exorcising** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6455 | **intimidating** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6456 | **spanking** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6457 | **pandering** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6458 | **wrongdoers** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6459 | **hateful** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6460 | **enemies-protecting** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6461 | **hatred-were** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6462 | **expel** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6463 | **indeed-not** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6464 | **hate-as** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6465 | **chong** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6466 | **vinayaka** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6467 | **strode** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6468 | **clerics** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6469 | **cle** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6470 | **bleeding** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6471 | **decorate** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6472 | **rites-they** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6473 | **shred** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6474 | **compas** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6475 | **boiled** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6476 | **protectors-we** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6477 | **bodhisat** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6478 | **tvas-then** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6479 | **gleefully** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6480 | **gobble** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6481 | **ambrosias** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6482 | **mantrayana-namely** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6483 | **succulent** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6484 | **heedlessly** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6485 | **slaugh** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6486 | **murdering** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6487 | **sicknesses** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6488 | **prowl** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6489 | **roam** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6490 | **gnaw** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6491 | **innards** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6492 | **lookout** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6493 | **killer** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6494 | **asas** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6495 | **inflamed** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6496 | **shaking** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6497 | **intimacy** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6498 | **hell-unless** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6499 | **preying** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6500 | **bon** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6501 | **sublimity** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6502 | **conspicuous** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6503 | **encapsulates** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6504 | **dharmas** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6505 | **bared** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6506 | **abhid** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6507 | **harma** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6508 | **prakasasila** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6509 | **sarighab** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6510 | **kukku** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6511 | **apada** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6512 | **persistence** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6513 | **stroking** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6514 | **maggots** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6515 | **forelegs** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6516 | **halo** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6517 | **shoulder-all** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6518 | **ofmaitreya** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6519 | **talents** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6520 | **feelings-like** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6521 | **contented** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6522 | **displeased** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6523 | **alarmingly** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6524 | **logician** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6525 | **tsakpuwa** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6526 | **deva** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6527 | **datta** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6528 | **cousins** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6529 | **prodigious** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6530 | **kunpang** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6531 | **rakgyal** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6532 | **darkened** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6533 | **furthers** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6534 | **negativity** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6535 | **vile** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6536 | **physique** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6537 | **camels** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6538 | **correspondingly** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6539 | **summarize** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6540 | **ferryboat** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6541 | **jasako** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6542 | **carriage** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6543 | **materialized** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6544 | **beheaded** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6545 | **scabrous** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6546 | **shaven-headed** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6547 | **bigot** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6548 | **shadows** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6549 | **panicular** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6550 | **woke** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6551 | **benevolent** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6552 | **activities-prostrations** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6553 | **circumam** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6554 | **bulations** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6555 | **hean** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6556 | **proclaim** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6557 | **jackals** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6558 | **tative** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6559 | **discriminating** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6560 | **thusness** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6561 | **witnesses** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6562 | **foundering** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6563 | **friendless** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6564 | **binh** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6565 | **suvarl** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6566 | **advipa** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6567 | **suvarnadvipa** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6568 | **swindle** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6569 | **either-try** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6570 | **pinprick** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6571 | **pain-we** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6572 | **thumbnails** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6573 | **enslaved** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6574 | **prejudices** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6575 | **trungpa** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6576 | **sinachen** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6577 | **kamarupa** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6578 | **goaded** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6579 | **kamarapa** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6580 | **cart** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6581 | **sea-captain** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6582 | **householder** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6583 | **mercha** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6584 | **plank** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6585 | **ashore** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6586 | **intoxication** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6587 | **ravishingly** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6588 | **couch** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6589 | **fist** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6590 | **pulver** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6591 | **ized** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6592 | **brain** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6593 | **smashed** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6594 | **ulti** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6595 | **mate** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6596 | **chak** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6597 | **shingwa** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6598 | **langthang** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6599 | **succes** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6600 | **sor** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6601 | **shortcoming** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6602 | **stfipa** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6603 | **selfishness** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6604 | **subjugating** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6605 | **vaibhasika** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6606 | **cine-the** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6607 | **dozed** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6608 | **spat** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6609 | **scar** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6610 | **treatises** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6611 | **ceaselessly** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6612 | **donned** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6613 | **fervently** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6614 | **nivritta** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6615 | **palace-one** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6616 | **cubits-and** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6617 | **alternately** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6618 | **ketaka** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6619 | **saketa** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6620 | **largesse** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6621 | **organize** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6622 | **yanta** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6623 | **hard-to** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6624 | **raksasa** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6625 | **oblation** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6626 | **dishes** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6627 | **smitten** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6628 | **grief** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6629 | **minis** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6630 | **ter** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6631 | **vedas** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6632 | **coveting** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6633 | **enchantment** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6634 | **it-for** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6635 | **queen-his** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6636 | **wife-in** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6637 | **curse** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6638 | **unreliable** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6639 | **numer** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6640 | **ous** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6641 | **wasn** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6642 | **perfections-generosity** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6643 | **concentration-are** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6644 | **masterful** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6645 | **dharanis** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6646 | **moan** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6647 | **starvation** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6648 | **preta-realm** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6649 | **slave** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6650 | **daring** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6651 | **gladly** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6652 | **cunning** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6653 | **mandabhadri** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6654 | **brewed** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6655 | **emptying** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6656 | **expound** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6657 | **evil-doing** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6658 | **undertak** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6659 | **actions-even** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6660 | **amusing** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6661 | **caterpillars** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6662 | **occurrences** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6663 | **wronged** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6664 | **slandered** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6665 | **ages** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6666 | **shatters** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6667 | **zeal** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6668 | **accuses** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6669 | **unjustly** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6670 | **effect-as** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6671 | **grudge-will** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6672 | **anger-so** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6673 | **puffs** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6674 | **humiliated** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6675 | **touchiness** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6676 | **admiringly** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6677 | **marry** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6678 | **sew** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6679 | **double-pointed** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6680 | **nairaftjana** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6681 | **asceticism** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6682 | **nettles** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6683 | **skeleton** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6684 | **greenish** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6685 | **tenaciously** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6686 | **hopeless** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6687 | **melong** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6688 | **practis** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6689 | **bark** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6690 | **lakhe** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6691 | **rabjam** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6692 | **snowed** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6693 | **well-be** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6694 | **mourn** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6695 | **gristle** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6696 | **cravings** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6697 | **laughs** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6698 | **vom** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6699 | **ited** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6700 | **recount** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6701 | **happenings** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6702 | **bod** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6703 | **hisattvas** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6704 | **hardhips** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6705 | **limb** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6706 | **druk** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6707 | **karpo** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6708 | **unhurriedly** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6709 | **beware** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6710 | **deathbed** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6711 | **immedi** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6712 | **ately** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6713 | **coward** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6714 | **dancing-girl** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6715 | **time-one** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6716 | **them-such** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6717 | **clump** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6718 | **idleness** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6719 | **tenacity** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6720 | **reputed** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6721 | **tsa-tsas** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6722 | **sporadically** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6723 | **excite** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6724 | **spouses** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6725 | **relatives-even** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6726 | **birth-are** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6727 | **shiwa** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6728 | **heedless** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6729 | **trifling** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6730 | **forethought** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6731 | **roving** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6732 | **squandered** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6733 | **occupations** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6734 | **academia** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6735 | **path-disenchantment** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6736 | **absorption-arise** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6737 | **natu** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6738 | **tranquillity** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6739 | **bustling** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6740 | **dispensed** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6741 | **fascinated** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6742 | **concept-free** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6743 | **ofvairocana** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6744 | **concentra** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6745 | **confining** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6746 | **substantiality** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6747 | **gandharvas** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6748 | **them-the** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6749 | **scendent** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6750 | **twenty-two** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6751 | **thirty-six** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6752 | **contami** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6753 | **nate** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6754 | **self-aggrandizement** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6755 | **pline** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6756 | **giving-offering** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6757 | **giver** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6758 | **tiring** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6759 | **summing** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6760 | **guile** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6761 | **transcend** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6762 | **non-attachment** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6763 | **contentment** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6764 | **clings** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6765 | **thinker** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6766 | **nutshell** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6767 | **nirvina** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6768 | **non-dwelling** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6769 | **grasped** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6770 | **craving** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6771 | **conceptualize** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6772 | **bodhicitta-emptiness** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6773 | **nnhikas** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6774 | **relegate** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6775 | **bodhi** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6776 | **citta** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6777 | **intensively** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6778 | **painting** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6779 | **frescoes** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6780 | **plastered** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6781 | **sincerest** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6782 | **purifications** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6783 | **unimpeded** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6784 | **miracles-if** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6785 | **innocents** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6786 | **be-realization** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6787 | **on-you** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6788 | **askedjetsun** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6789 | **disso** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6790 | **ciating** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6791 | **nyethang** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6792 | **kyung** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6793 | **lhangtsang** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6794 | **buddhists** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6795 | **discursive** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6796 | **illusions** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6797 | **dividing** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6798 | **counteracts** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6799 | **chegom** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6800 | **indivis** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6801 | **ible** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6802 | **non-conceptualization** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6803 | **non-action** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6804 | **churn** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6805 | **purport** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6806 | **actions-except** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6807 | **actions-be** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6808 | **samayas-there** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6809 | **atapa** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6810 | **ninety-nine** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6811 | **carelessly** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6812 | **attentive** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6813 | **darsaka** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6814 | **sailkara** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6815 | **mouthing** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6816 | **anti** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6817 | **dotes** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6818 | **buddhas-in** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6819 | **appli** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6820 | **cation** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6821 | **perils** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6822 | **dreadful** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6823 | **wickedness** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6824 | **sins** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6825 | **concealing** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6826 | **trepidation** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6827 | **sukhavati** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6828 | **disillusioned** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6829 | **vajrasattva-purification** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6830 | **signify** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6831 | **fifteenth** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6832 | **reabsorbs** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6833 | **sambhogakaya-the** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6834 | **headband** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6835 | **scarf** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6836 | **earrings** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6837 | **necklace** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6838 | **armlets** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6839 | **necklaces** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6840 | **bracelet** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6841 | **anklet** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6842 | **embraces** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6843 | **vajratopa** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6844 | **vividly** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6845 | **tangka** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6846 | **fresco** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6847 | **inert** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6848 | **pupils** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6849 | **atom** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6850 | **transgres** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6851 | **sions** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6852 | **dishonourable** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6853 | **gooseflesh** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6854 | **glistening** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6855 | **dripping** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6856 | **flushed** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6857 | **expelled** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6858 | **spiders** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6859 | **scorpions** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6860 | **toads** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6861 | **tadpoles** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6862 | **vapours** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6863 | **orifices** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6864 | **pores** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6865 | **personification** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6866 | **impurities** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6867 | **expectantly** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6868 | **earth-every** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6869 | **flesh-are** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6870 | **scores** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6871 | **vertically** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6872 | **sixty-four** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6873 | **svabhavika** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6874 | **smilingly** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6875 | **behi** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6876 | **fringed** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6877 | **thousand-spoked** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6878 | **conch** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6879 | **result-the** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6880 | **multi-col** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6881 | **oured** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6882 | **sattvas** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6883 | **pronouncing** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6884 | **humming** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6885 | **rapakaya** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6886 | **spon** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6887 | **taneously** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6888 | **clingings** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6889 | **reabsorbing** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6890 | **vajrasattvas** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6891 | **vanishing** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6892 | **elaborations** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6893 | **officiating** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6894 | **officiants** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6895 | **ornate** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6896 | **intonations** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6897 | **blaring** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6898 | **trumpets** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6899 | **recited-at** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6900 | **goings-on** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6901 | **lowlands** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6902 | **clattering** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6903 | **puspe** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6904 | **dhupe** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6905 | **travesties** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6906 | **swallowing** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6907 | **balls** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6908 | **soul** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6909 | **prayer-books** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6910 | **grimy** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6911 | **scrupulous** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6912 | **tiresome** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6913 | **chore** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6914 | **undistracted** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6915 | **recites** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6916 | **laywoman** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6917 | **atiga** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6918 | **non-existent** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6919 | **valley-is** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6920 | **unfit** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6921 | **infecting** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6922 | **brightly** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6923 | **danced** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6924 | **samaya-and** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6925 | **delirious** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6926 | **urgyenpa** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6927 | **vanish** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6928 | **terrify** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6929 | **earthenware** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6930 | **denting** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6931 | **curing** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6932 | **adults** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6933 | **unremittingly** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6934 | **joke** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6935 | **obscu** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6936 | **rations** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6937 | **embody** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6938 | **fooled** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6939 | **interdependently** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6940 | **virupa** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6941 | **transcends** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6942 | **replete** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6943 | **lalas** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6944 | **bell-metal** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6945 | **turquoises** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6946 | **sapphires** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6947 | **arura** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6948 | **kyurura** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6949 | **direction-meaning** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6950 | **dha** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6951 | **obhya** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6952 | **ratnasambhava** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6953 | **amoghasiddhi** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6954 | **stacked-up** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6955 | **altar** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6956 | **rime** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6957 | **underside** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6958 | **wiping** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6959 | **veil** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6960 | **undersides** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6961 | **woollen** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6962 | **chogyal** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6963 | **pakpa** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6964 | **nyingma** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6965 | **bhumi** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6966 | **sprinkling** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6967 | **ung** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6968 | **thumb** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6969 | **rekhe** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6970 | **purvavideha** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6971 | **subcontinents** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6972 | **deha** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6973 | **videha** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6974 | **inexhaustibly** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6975 | **victorious** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6976 | **unfilled** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6977 | **first-order** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6978 | **second-order** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6979 | **millionfold** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6980 | **third-order** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6981 | **buddha-sakyamuni** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6982 | **endurance** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6983 | **graced** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6984 | **delights** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6985 | **infinitely** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6986 | **unborn** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6987 | **ache** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6988 | **heaps** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6989 | **seven-element** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6990 | **important-as** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6991 | **do-to** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6992 | **droppings** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6993 | **saturate** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6994 | **scented** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6995 | **generously** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6996 | **reasons-and** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6997 | **yourself-that** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6998 | **fooling** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 6999 | **dirtily** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7000 | **mouldy** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7001 | **lamp-offerings** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7002 | **rancid** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7003 | **shelze** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7004 | **consis** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7005 | **tency** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7006 | **torma-dough** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7007 | **distinctively** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7008 | **sublimely** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7009 | **scavenger** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7010 | **rice-gruel** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7011 | **maqc** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7012 | **fingernail** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7013 | **oily** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7014 | **rupakaya** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7015 | **converse** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7016 | **barbaric** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7017 | **exclaim** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7018 | **aiota** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7019 | **tree-or** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7020 | **world-even** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7021 | **rainbow-none** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7022 | **jaundice** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7023 | **cheerfully** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7024 | **necessities** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7025 | **dissipated** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7026 | **puri** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7027 | **fying** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7028 | **contradiction** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7029 | **tised** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7030 | **life-hermits** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7031 | **instance-use** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7032 | **clung** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7033 | **instantaneously** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7034 | **swaying** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7035 | **squealing** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7036 | **protrudes** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7037 | **mother-the** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7038 | **consciousness-instantly** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7039 | **life-size** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7040 | **brow** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7041 | **tripod** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7042 | **skulls** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7043 | **sizzles** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7044 | **foul** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7045 | **frothing** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7046 | **scum** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7047 | **exudes** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7048 | **drip** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7049 | **ridding** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7050 | **transforms** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7051 | **manifests** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7052 | **billow** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7053 | **locality** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7054 | **teeming** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7055 | **deity-a** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7056 | **iakas** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7057 | **sunbeams** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7058 | **unfavour** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7059 | **swarms** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7060 | **activity-performing** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7061 | **myriads** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7062 | **appeasing** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7063 | **mother-use** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7064 | **scatter** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7065 | **victory-banners** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7066 | **spokes** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7067 | **conches** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7068 | **superiors** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7069 | **inferiors** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7070 | **overlords** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7071 | **underlings** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7072 | **snatch** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7073 | **life-force** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7074 | **avengers** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7075 | **behind-the** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7076 | **suffering-the** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7077 | **life-restoring** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7078 | **elixirs** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7079 | **males** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7080 | **offerer** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7081 | **vari** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7082 | **egated** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7083 | **variegated** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7084 | **grisly** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7085 | **slashing** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7086 | **bravado** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7087 | **hate-filled** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7088 | **clenching** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7089 | **fists** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7090 | **lashing** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7091 | **whirl** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7092 | **inauspicious** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7093 | **compassion-but** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7094 | **adepts** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7095 | **boast** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7096 | **ninefold** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7097 | **puny** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7098 | **retaliation-as** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7099 | **path-the** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7100 | **subjugation** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7101 | **instance-are** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7102 | **heaped** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7103 | **conceir** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7104 | **exultation** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7105 | **solitudes** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7106 | **trampling** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7107 | **mischief** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7108 | **creators** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7109 | **embar** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7110 | **rassed** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7111 | **mobilize** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7112 | **gyalgong** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7113 | **there-it** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7114 | **trances** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7115 | **insistent** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7116 | **predic** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7117 | **samaya-breakers** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7118 | **clergy** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7119 | **dream-like** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7120 | **momentarily** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7121 | **self-concern** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7122 | **maliciousness** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7123 | **others-and** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7124 | **fixation** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7125 | **qualifica** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7126 | **illustrative** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7127 | **untar** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7128 | **nished** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7129 | **alone-awakens** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7130 | **gotsangpa** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7131 | **perfects** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7132 | **rangrik** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7133 | **intellect** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7134 | **north-facing** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7135 | **devotional** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7136 | **uncontrived** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7137 | **vanquishing** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7138 | **nagabodhi** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7139 | **snatching** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7140 | **fervour** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7141 | **ligent** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7142 | **intellectualization** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7143 | **gyalmo** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7144 | **tsawarong** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7145 | **pang** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7146 | **meditation-band** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7147 | **hood** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7148 | **yanas** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7149 | **enough-even** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7150 | **receptacle** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7151 | **vajrayogini** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7152 | **awakening** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7153 | **insubstantial** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7154 | **complexion** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7155 | **tinged** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7156 | **long-sleeved** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7157 | **gown** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7158 | **deerskin** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7159 | **adhara** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7160 | **unharmed** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7161 | **petalled** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7162 | **emblazoned** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7163 | **vulture** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7164 | **culmination** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7165 | **long-life** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7166 | **sprig** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7167 | **crook** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7168 | **mandarava** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7169 | **dried-up** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7170 | **looped** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7171 | **pennants** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7172 | **mamos** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7173 | **encircled** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7174 | **evenness** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7175 | **siddhi** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7176 | **pliramitas** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7177 | **insurpassable** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7178 | **hrib** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7179 | **prelimi** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7180 | **naries** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7181 | **surrendering** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7182 | **chases** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7183 | **passer-by** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7184 | **lurches** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7185 | **ordeal** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7186 | **blossom** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7187 | **reverence** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7188 | **bending** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7189 | **cupped** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7190 | **ful** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7191 | **hunchback** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7192 | **dwarf** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7193 | **them-so** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7194 | **deformed** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7195 | **impeccably** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7196 | **it-and** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7197 | **fruitless** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7198 | **proficient** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7199 | **head-dress** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7200 | **soaked** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7201 | **dye** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7202 | **learns** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7203 | **dyed** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7204 | **successfully-but** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7205 | **aya** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7206 | **evildoers** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7207 | **dharma-just** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7208 | **butter-bag** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7209 | **imprinted** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7210 | **clippings** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7211 | **usnisa** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7212 | **offering-that** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7213 | **ostentation** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7214 | **antabhadra** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7215 | **mansions** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7216 | **musical** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7217 | **ema** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7218 | **nated** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7219 | **multitudinous** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7220 | **samantabhadras** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7221 | **mani** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7222 | **fested** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7223 | **cloudbanks** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7224 | **perfecting** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7225 | **unmentionably** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7226 | **obstructions** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7227 | **doer** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7228 | **negative-not** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7229 | **ofi** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7230 | **nstructions** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7231 | **ostentatious** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7232 | **merus** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7233 | **ungrateful** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7234 | **subdivided** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7235 | **kriya** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7236 | **vedic** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7237 | **transmutation** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7238 | **cunda** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7239 | **non-conceptual** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7240 | **aigaramati** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7241 | **rub** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7242 | **wholeheartedly** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7243 | **dedica** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7244 | **ofvaisali** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7245 | **horrified** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7246 | **vajras** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7247 | **heruka** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7248 | **you-in** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7249 | **body-on** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7250 | **mala** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7251 | **orh** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7252 | **moon-crystal** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7253 | **actions-taking** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7254 | **misconduct-and** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7255 | **fro** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7256 | **nirm** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7257 | **ruby** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7258 | **actions-lying** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7259 | **chatter-and** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7260 | **views-and** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7261 | **streaks** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7262 | **underlies** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7263 | **svabhavikakaya** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7264 | **ardent** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7265 | **longing** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7266 | **you-up** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7267 | **vajrayogini-you** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7268 | **overexcited** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7269 | **lassitude** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7270 | **torpor** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7271 | **agitation** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7272 | **inseparably** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7273 | **consciousnesses** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7274 | **naturalness** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7275 | **profundity** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7276 | **inconceivably** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7277 | **charac** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7278 | **teristics** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7279 | **listeners** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7280 | **relate-neither** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7281 | **detail-the** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7282 | **translations-known** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7283 | **actualize** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7284 | **incon** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7285 | **ceivably** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7286 | **causal** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7287 | **mantrayana-kriya** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7288 | **bewilderment** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7289 | **subdues** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7290 | **doc** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7291 | **trine** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7292 | **acclaimed** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7293 | **kingja** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7294 | **nobility** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7295 | **lament** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7296 | **consented** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7297 | **kila** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7298 | **thotrengtsel** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7299 | **devabhadrapala** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7300 | **eldest** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7301 | **anandagarbha** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7302 | **devaputra** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7303 | **circling** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7304 | **pasupati** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7305 | **jewel-coloured** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7306 | **berries** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7307 | **kausika** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7308 | **level-you** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7309 | **adornment** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7310 | **illuminate** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7311 | **symbolized** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7312 | **sponta** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7313 | **neously** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7314 | **primordially** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7315 | **vajraloka** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7316 | **vajraguhya** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7317 | **ratnaloka** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7318 | **ratnapada** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7319 | **padmakaya** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7320 | **padmaprabha** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7321 | **atha** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7322 | **gatas** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7323 | **visuddhasiddha** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7324 | **siddhyaloka** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7325 | **viyoganta** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7326 | **irocana** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7327 | **misconceptions** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7328 | **all-victorious** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7329 | **vajrapal** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7330 | **dazzling** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7331 | **jewel-encrusted** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7332 | **ered** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7333 | **heart-son** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7334 | **uparaja** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7335 | **alokabhasvati** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7336 | **beak** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7337 | **hap** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7338 | **pened** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7339 | **presage** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7340 | **gleaming** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7341 | **marvelling** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7342 | **vajrapaqi** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7343 | **twenty-thousand** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7344 | **empowered** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7345 | **sukhapala** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7346 | **kuhana** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7347 | **sarasiddhi** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7348 | **charnel** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7349 | **mahahe** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7350 | **compiler** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7351 | **nir** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7352 | **manakaya** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7353 | **dare** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7354 | **weeps** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7355 | **manifes** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7356 | **uttering** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7357 | **polemic** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7358 | **razor** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7359 | **compose** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7360 | **paqqitas** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7361 | **instantaneous** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7362 | **cessation** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7363 | **shosha** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7364 | **astrology** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7365 | **hastibhala** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7366 | **fabrications** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7367 | **jnanasutra** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7368 | **pal** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7369 | **qita** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7370 | **tribe** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7371 | **descended** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7372 | **ape-an** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7373 | **crag-demoness** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7374 | **chaos** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7375 | **satanika** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7376 | **webbed** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7377 | **eyelids** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7378 | **non-human** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7379 | **banished** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7380 | **ancient-nyatri** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7381 | **sarvanivaranaviskam** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7382 | **bhin** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7383 | **yumbu** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7384 | **lakhar** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7385 | **cintamani** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7386 | **kongjo-a** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7387 | **tara-and** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7388 | **nepalese** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7389 | **tritsun-a** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7390 | **bhrikuti** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7391 | **devavit** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7392 | **sirhha** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7393 | **ofj** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7394 | **ewels** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7395 | **akarmati** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7396 | **brows** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7397 | **amradvipa** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7398 | **eleven-headed** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7399 | **ngam** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7400 | **lugong** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7401 | **lhazang** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7402 | **lupel** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7403 | **discovering** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7404 | **forebears** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7405 | **gungtsen** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7406 | **nyang** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7407 | **resided** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7408 | **chimpu** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7409 | **insight** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7410 | **gomadeviya** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7411 | **aryapalo** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7412 | **non-humans** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7413 | **crushes** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7414 | **tremble** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7415 | **subju** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7416 | **sariwari** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7417 | **horse-breeder** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7418 | **swineherd** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7419 | **poultryman** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7420 | **dog-breeder** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7421 | **trisher** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7422 | **dudjom** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7423 | **chim** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7424 | **sakyaprabha** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7425 | **shubu** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7426 | **palgyi** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7427 | **senge** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7428 | **protectresses** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7429 | **oaths** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7430 | **trakmar** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7431 | **three-storey** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7432 | **sub** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7433 | **enclosed** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7434 | **consecration** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7435 | **heart-disciples-the** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7436 | **nyangwen** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7437 | **antric** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7438 | **scrolls** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7439 | **legacy** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7440 | **treasure-discoverers** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7441 | **mindtt** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7442 | **together-the** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7443 | **lineage-from** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7444 | **frown** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7445 | **recounting** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7446 | **warms** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7447 | **already-with** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7448 | **dharma-companions** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7449 | **unmis** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7450 | **faultless** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7451 | **mind-consciousness** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7452 | **interme** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7453 | **diate** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7454 | **it-which** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7455 | **despicable** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7456 | **protruding** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7457 | **crimson** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7458 | **apparition** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7459 | **pilgrimage** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7460 | **incarnate** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7461 | **gyurme** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7462 | **thekchok** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7463 | **trime** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7464 | **golok** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7465 | **so-and-so** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7466 | **dedications** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7467 | **incarnations** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7468 | **retreats** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7469 | **confes** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7470 | **enthroned** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7471 | **sinners** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7472 | **paqqita** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7473 | **life-energy** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7474 | **pluck** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7475 | **auditory** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7476 | **blur** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7477 | **salivate** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7478 | **extremities** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7479 | **energies-the** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7480 | **life-supporting** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7481 | **life-channel** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7482 | **sighs** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7483 | **whiteness** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7484 | **cloudless** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7485 | **redness** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7486 | **lustful** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7487 | **blackness** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7488 | **swoon** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7489 | **vajra-posture** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7490 | **rattles** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7491 | **awakens** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7492 | **severs** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7493 | **tent** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7494 | **mind-con** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7495 | **vowel** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7496 | **dots** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7497 | **visarga** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7498 | **flut** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7499 | **tering** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7500 | **three-layered** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7501 | **embodying** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7502 | **rubies** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7503 | **clad** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7504 | **attire** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7505 | **nirmat** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7506 | **ursina** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7507 | **beads** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7508 | **skyward** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7509 | **akanistha** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7510 | **repre** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7511 | **sentation** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7512 | **palate** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7513 | **rimes** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7514 | **grass-stalk** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7515 | **treasure-discoverer** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7516 | **nyi** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7517 | **iyana** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7518 | **palyul** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7519 | **vajrapdt** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7520 | **one-pointed** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7521 | **beseech** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7522 | **gochen** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7523 | **prayer-book** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7524 | **habit** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7525 | **versions** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7526 | **contriving** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7527 | **amitayus** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7528 | **amarani** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7529 | **jivantiye** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7530 | **svaha** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7531 | **dharani** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7532 | **and-through** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7533 | **inter** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7534 | **dependence-dispels** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7535 | **aches** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7536 | **serum** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7537 | **dew** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7538 | **stalk** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7539 | **assiduously** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7540 | **shortcut** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7541 | **mutter** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7542 | **incoherently** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7543 | **interminable** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7544 | **goad** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7545 | **mination** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7546 | **meditation-all** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7547 | **creativity** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7548 | **aesthetic** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7549 | **literary** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7550 | **banish** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7551 | **fabricate** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7552 | **watershed** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7553 | **evil-even** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7554 | **indissolubly** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7555 | **cludes** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7556 | **adulteration** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7557 | **well-cooked** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7558 | **fancy** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7559 | **seasoned** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7560 | **savoury** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7561 | **cooking-juice** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7562 | **ploughshare** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7563 | **unearthing** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7564 | **irrigates** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7565 | **nanny** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7566 | **uprooting** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7567 | **exhorts** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7568 | **elegance** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7569 | **poetry** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7570 | **copious** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7571 | **cramped** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7572 | **discourses** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7573 | **philosophical** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7574 | **intellects** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7575 | **soak** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7576 | **gloom** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7577 | **imperturbable** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7578 | **instructor** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7579 | **imparts** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7580 | **savant** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7581 | **verbose** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7582 | **discourse** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7583 | **boasts** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7584 | **confection** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7585 | **cleverly** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7586 | **fanciful** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7587 | **superficially** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7588 | **vajra-brothers** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7589 | **compile** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7590 | **conveys** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7591 | **nourished** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7592 | **regents** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7593 | **captivate** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7594 | **intoxicating** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7595 | **seclusion** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7596 | **dronma** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7597 | **tsering** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7598 | **kunzangthekchok** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7599 | **tulku** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7600 | **peated** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7601 | **times-even** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7602 | **kushab** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7603 | **shenpen** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7604 | **thaye** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7605 | **ozer** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7606 | **dharma-sovereign** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7607 | **tradition-in** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7608 | **wick** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7609 | **changchub** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7610 | **cbokyi** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7611 | **embellishment** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7612 | **rough-mannered** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7613 | **rudam** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7614 | **samten** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7615 | **choling** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7616 | **palace-a** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7617 | **foliage** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7618 | **vines** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7619 | **thickets** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7620 | **undergrowth** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7621 | **filigrees** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7622 | **filtering** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7623 | **swasti** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7624 | **siddham** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7625 | **unfolded** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7626 | **renowned** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7627 | **gyalwai** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7628 | **nyugu** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7629 | **chokyi** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7630 | **lekdrup** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7631 | **temporally** | 1 | 166.19 | 9.59 | 🔵 low — common in general English |
| 7632 | **reduced** | 2 | 166.13 | 4.793221 | 🔵 low — common in general English |
| 7633 | **weeks** | 2 | 162.48 | 4.68786 | 🔵 low — common in general English |
| 7634 | **balance** | 2 | 161.72 | 4.665882 | 🔵 low — common in general English |
| 7635 | **decision** | 2 | 160.97 | 4.644375 | 🔵 low — common in general English |
| 7636 | **systems** | 2 | 160.85 | 4.640835 | 🔵 low — common in general English |
| 7637 | **contradict** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English |
| 7638 | **pits** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English |
| 7639 | **lured** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English |
| 7640 | **snapped** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English |
| 7641 | **numerical** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English |
| 7642 | **orientation** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English |
| 7643 | **reasoned** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English |
| 7644 | **capacities** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English |
| 7645 | **disappearance** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English |
| 7646 | **inundated** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English |
| 7647 | **incompatible** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English |
| 7648 | **baring** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English |
| 7649 | **highway** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English |
| 7650 | **pinnacle** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English |
| 7651 | **tri** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English |
| 7652 | **dependable** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English |
| 7653 | **escaped** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English |
| 7654 | **slab** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English |
| 7655 | **dearly** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English |
| 7656 | **lords** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English |
| 7657 | **transitory** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English |
| 7658 | **rigorous** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English |
| 7659 | **sentiments** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English |
| 7660 | **prolong** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English |
| 7661 | **toxic** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English |
| 7662 | **disorders** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English |
| 7663 | **crawl** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English |
| 7664 | **formidable** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English |
| 7665 | **dangerously** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English |
| 7666 | **immune** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English |
| 7667 | **amidst** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English |
| 7668 | **marsh** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English |
| 7669 | **multiples** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English |
| 7670 | **purse** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English |
| 7671 | **plying** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English |
| 7672 | **centuries** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English |
| 7673 | **icy** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English |
| 7674 | **evaporated** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English |
| 7675 | **bury** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English |
| 7676 | **eyed** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English |
| 7677 | **castrated** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English |
| 7678 | **ridden** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English |
| 7679 | **celebrations** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English |
| 7680 | **bartering** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English |
| 7681 | **infant** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English |
| 7682 | **unnoticed** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English |
| 7683 | **belly** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English |
| 7684 | **integrity** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English |
| 7685 | **occupying** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English |
| 7686 | **tightens** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English |
| 7687 | **charming** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English |
| 7688 | **strife** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English |
| 7689 | **soldiers** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English |
| 7690 | **haul** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English |
| 7691 | **outdoor** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English |
| 7692 | **instances** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English |
| 7693 | **guilty** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English |
| 7694 | **odd** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English |
| 7695 | **sharpest** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English |
| 7696 | **tales** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English |
| 7697 | **circulate** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English |
| 7698 | **tails** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English |
| 7699 | **transferring** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English |
| 7700 | **residue** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English |
| 7701 | **poorer** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English |
| 7702 | **unattractive** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English |
| 7703 | **unjust** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English |
| 7704 | **accusations** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English |
| 7705 | **self-confidence** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English |
| 7706 | **fulfilment** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English |
| 7707 | **propel** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English |
| 7708 | **onward** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English |
| 7709 | **jam** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English |
| 7710 | **infuse** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English |
| 7711 | **absurd** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English |
| 7712 | **mindful** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English |
| 7713 | **vigilant** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English |
| 7714 | **cares** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English |
| 7715 | **decay** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English |
| 7716 | **immensely** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English |
| 7717 | **travellers** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English |
| 7718 | **relies** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English |
| 7719 | **violently** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English |
| 7720 | **parks** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English |
| 7721 | **avenues** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English |
| 7722 | **honoured** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English |
| 7723 | **piercing** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English |
| 7724 | **forbid** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English |
| 7725 | **hailstorms** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English |
| 7726 | **wondering** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English |
| 7727 | **tending** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English |
| 7728 | **summoned** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English |
| 7729 | **compelling** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English |
| 7730 | **rosy** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English |
| 7731 | **criticizes** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English |
| 7732 | **groves** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English |
| 7733 | **pages** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English |
| 7734 | **hears** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English |
| 7735 | **one-sided** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English |
| 7736 | **sel** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English |
| 7737 | **opponents** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English |
| 7738 | **cheated** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English |
| 7739 | **quarrel** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English |
| 7740 | **banquet** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English |
| 7741 | **author** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English |
| 7742 | **stubborn** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English |
| 7743 | **monarch** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English |
| 7744 | **sheltered** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English |
| 7745 | **subdue** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English |
| 7746 | **void** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English |
| 7747 | **viewing** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English |
| 7748 | **slaughtering** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English |
| 7749 | **harms** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English |
| 7750 | **boarded** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English |
| 7751 | **ludicrous** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English |
| 7752 | **shade** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English |
| 7753 | **grinding** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English |
| 7754 | **invariably** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English |
| 7755 | **detrimental** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English |
| 7756 | **occupation** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English |
| 7757 | **voyages** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English |
| 7758 | **kicking** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English |
| 7759 | **welt** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English |
| 7760 | **charitable** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English |
| 7761 | **mediocre** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English |
| 7762 | **guarding** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English |
| 7763 | **subside** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English |
| 7764 | **tran** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English |
| 7765 | **falcon** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English |
| 7766 | **bounce** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English |
| 7767 | **print** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English |
| 7768 | **maya** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English |
| 7769 | **stan** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English |
| 7770 | **soaking** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English |
| 7771 | **thickness** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English |
| 7772 | **tumbling** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English |
| 7773 | **finest** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English |
| 7774 | **repetition** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English |
| 7775 | **gratified** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English |
| 7776 | **expose** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English |
| 7777 | **fence** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English |
| 7778 | **straw** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English |
| 7779 | **deplete** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English |
| 7780 | **rushing** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English |
| 7781 | **confront** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English |
| 7782 | **vertical** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English |
| 7783 | **fifteen** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English |
| 7784 | **shapes** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English |
| 7785 | **chopping** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English |
| 7786 | **surrender** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English |
| 7787 | **shines** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English |
| 7788 | **south-west** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English |
| 7789 | **confidently** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English |
| 7790 | **respected** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English |
| 7791 | **midst** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English |
| 7792 | **concluding** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English |
| 7793 | **undertakes** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English |
| 7794 | **ame** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English |
| 7795 | **displayed** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English |
| 7796 | **hut** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English |
| 7797 | **opportune** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English |
| 7798 | **foundations** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English |
| 7799 | **obscuring** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English |
| 7800 | **contradictory** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English |
| 7801 | **impediments** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English |
| 7802 | **evacuation** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English |
| 7803 | **erect** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English |
| 7804 | **axis** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English |
| 7805 | **leaning** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English |
| 7806 | **intermediaries** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English |
| 7807 | **strengths** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English |
| 7808 | **henceforth** | 1 | 159.22 | 9.18767 | 🔵 low — common in general English |
| 7809 | **traders** | 2 | 158.48 | 4.57255 | 🔵 low — common in general English |
| 7810 | **market** | 3 | 156.83 | 3.016666 | 🔵 low — common in general English |
| 7811 | **wheat** | 2 | 155.84 | 4.496322 | 🔵 low — common in general English |
| 7812 | **owned** | 2 | 154.29 | 4.451472 | 🔵 low — common in general English |
| 7813 | **lets** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English |
| 7814 | **seize** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English |
| 7815 | **aged** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English |
| 7816 | **discomfort** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English |
| 7817 | **undue** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English |
| 7818 | **extracted** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English |
| 7819 | **thorough** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English |
| 7820 | **translation** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English |
| 7821 | **eastward** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English |
| 7822 | **erected** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English |
| 7823 | **wilderness** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English |
| 7824 | **contentious** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English |
| 7825 | **student** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English |
| 7826 | **als** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English |
| 7827 | **pause** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English |
| 7828 | **judging** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English |
| 7829 | **prelude** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English |
| 7830 | **blizzard** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English |
| 7831 | **ham** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English |
| 7832 | **exit** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English |
| 7833 | **heels** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English |
| 7834 | **ditch** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English |
| 7835 | **erupt** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English |
| 7836 | **fashion** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English |
| 7837 | **alike** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English |
| 7838 | **entails** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English |
| 7839 | **porter** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English |
| 7840 | **demonstrating** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English |
| 7841 | **neighbour** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English |
| 7842 | **tumble** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English |
| 7843 | **dim** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English |
| 7844 | **wars** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English |
| 7845 | **wolf** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English |
| 7846 | **weapon** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English |
| 7847 | **overtly** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English |
| 7848 | **untrue** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English |
| 7849 | **diverse** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English |
| 7850 | **emotional** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English |
| 7851 | **choosing** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English |
| 7852 | **contravened** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English |
| 7853 | **disturbing** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English |
| 7854 | **mas** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English |
| 7855 | **pools** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English |
| 7856 | **fasting** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English |
| 7857 | **pour** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English |
| 7858 | **wondered** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English |
| 7859 | **coffers** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English |
| 7860 | **crashed** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English |
| 7861 | **undergone** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English |
| 7862 | **suicide** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English |
| 7863 | **hardest** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English |
| 7864 | **desperately** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English |
| 7865 | **precipitous** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English |
| 7866 | **whereby** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English |
| 7867 | **proportions** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English |
| 7868 | **progressed** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English |
| 7869 | **catching** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English |
| 7870 | **chronic** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English |
| 7871 | **bare** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English |
| 7872 | **gestures** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English |
| 7873 | **ingredient** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English |
| 7874 | **meats** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English |
| 7875 | **hanging** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English |
| 7876 | **predators** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English |
| 7877 | **trailing** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English |
| 7878 | **materialize** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English |
| 7879 | **crossing** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English |
| 7880 | **dressing** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English |
| 7881 | **belong** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English |
| 7882 | **luck** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English |
| 7883 | **height** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English |
| 7884 | **answers** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English |
| 7885 | **dashed** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English |
| 7886 | **fled** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English |
| 7887 | **analyzing** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English |
| 7888 | **dimmed** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English |
| 7889 | **limitations** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English |
| 7890 | **tugs** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English |
| 7891 | **favouring** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English |
| 7892 | **naive** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English |
| 7893 | **climbing** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English |
| 7894 | **affirmed** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English |
| 7895 | **crime** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English |
| 7896 | **pel** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English |
| 7897 | **frightening** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English |
| 7898 | **frosts** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English |
| 7899 | **pulses** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English |
| 7900 | **wipe** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English |
| 7901 | **cleaned** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English |
| 7902 | **thirdly** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English |
| 7903 | **extracting** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English |
| 7904 | **tubes** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English |
| 7905 | **foodstuffs** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English |
| 7906 | **deadly** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English |
| 7907 | **violence** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English |
| 7908 | **cape** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English |
| 7909 | **locks** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English |
| 7910 | **discouraging** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English |
| 7911 | **realizing** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English |
| 7912 | **symbolic** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English |
| 7913 | **distilled** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English |
| 7914 | **bind** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English |
| 7915 | **misunderstanding** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English |
| 7916 | **mode** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English |
| 7917 | **ripe** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English |
| 7918 | **predominantly** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English |
| 7919 | **swelling** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English |
| 7920 | **evolution** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English |
| 7921 | **witness** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English |
| 7922 | **accrue** | 1 | 154.24 | 8.899988 | 🔵 low — common in general English |
| 7923 | **focussing** | 1 | 150.37 | 8.676844 | 🔵 low — common in general English |
| 7924 | **describes** | 1 | 150.37 | 8.676844 | 🔵 low — common in general English |
| 7925 | **impeded** | 1 | 150.37 | 8.676844 | 🔵 low — common in general English |
| 7926 | **downs** | 1 | 150.37 | 8.676844 | 🔵 low — common in general English |
| 7927 | **silent** | 1 | 150.37 | 8.676844 | 🔵 low — common in general English |
| 7928 | **sheer** | 1 | 150.37 | 8.676844 | 🔵 low — common in general English |
| 7929 | **notion** | 1 | 150.37 | 8.676844 | 🔵 low — common in general English |
| 7930 | **recede** | 1 | 150.37 | 8.676844 | 🔵 low — common in general English |
| 7931 | **blown** | 1 | 150.37 | 8.676844 | 🔵 low — common in general English |
| 7932 | **bubble** | 1 | 150.37 | 8.676844 | 🔵 low — common in general English |
| 7933 | **recourse** | 1 | 150.37 | 8.676844 | 🔵 low — common in general English |
| 7934 | **marking** | 1 | 150.37 | 8.676844 | 🔵 low — common in general English |
| 7935 | **meadows** | 1 | 150.37 | 8.676844 | 🔵 low — common in general English |
| 7936 | **cooler** | 1 | 150.37 | 8.676844 | 🔵 low — common in general English |
| 7937 | **herds** | 1 | 150.37 | 8.676844 | 🔵 low — common in general English |
| 7938 | **constructed** | 1 | 150.37 | 8.676844 | 🔵 low — common in general English |
| 7939 | **deaths** | 1 | 150.37 | 8.676844 | 🔵 low — common in general English |
| 7940 | **beds** | 1 | 150.37 | 8.676844 | 🔵 low — common in general English |
| 7941 | **ala** | 1 | 150.37 | 8.676844 | 🔵 low — common in general English |
| 7942 | **malt** | 1 | 150.37 | 8.676844 | 🔵 low — common in general English |
| 7943 | **freezing** | 1 | 150.37 | 8.676844 | 🔵 low — common in general English |
| 7944 | **mattress** | 1 | 150.37 | 8.676844 | 🔵 low — common in general English |
| 7945 | **rebel** | 1 | 150.37 | 8.676844 | 🔵 low — common in general English |
| 7946 | **hospitality** | 1 | 150.37 | 8.676844 | 🔵 low — common in general English |
| 7947 | **foreshadow** | 1 | 150.37 | 8.676844 | 🔵 low — common in general English |
| 7948 | **persuaded** | 1 | 150.37 | 8.676844 | 🔵 low — common in general English |
| 7949 | **yard** | 1 | 150.37 | 8.676844 | 🔵 low — common in general English |
| 7950 | **functions** | 1 | 150.37 | 8.676844 | 🔵 low — common in general English |
| 7951 | **intermittent** | 1 | 150.37 | 8.676844 | 🔵 low — common in general English |
| 7952 | **soars** | 1 | 150.37 | 8.676844 | 🔵 low — common in general English |
| 7953 | **emp** | 1 | 150.37 | 8.676844 | 🔵 low — common in general English |
| 7954 | **drifting** | 1 | 150.37 | 8.676844 | 🔵 low — common in general English |
| 7955 | **responsibilities** | 1 | 150.37 | 8.676844 | 🔵 low — common in general English |
| 7956 | **fragrance** | 1 | 150.37 | 8.676844 | 🔵 low — common in general English |
| 7957 | **springs** | 1 | 150.37 | 8.676844 | 🔵 low — common in general English |
| 7958 | **enjoys** | 1 | 150.37 | 8.676844 | 🔵 low — common in general English |
| 7959 | **likes** | 1 | 150.37 | 8.676844 | 🔵 low — common in general English |
| 7960 | **corner** | 1 | 150.37 | 8.676844 | 🔵 low — common in general English |
| 7961 | **ink** | 1 | 150.37 | 8.676844 | 🔵 low — common in general English |
| 7962 | **walked** | 1 | 150.37 | 8.676844 | 🔵 low — common in general English |
| 7963 | **pre** | 1 | 150.37 | 8.676844 | 🔵 low — common in general English |
| 7964 | **cakes** | 1 | 150.37 | 8.676844 | 🔵 low — common in general English |
| 7965 | **dole** | 1 | 150.37 | 8.676844 | 🔵 low — common in general English |
| 7966 | **hung** | 1 | 150.37 | 8.676844 | 🔵 low — common in general English |
| 7967 | **inviting** | 1 | 150.37 | 8.676844 | 🔵 low — common in general English |
| 7968 | **dragging** | 1 | 150.37 | 8.676844 | 🔵 low — common in general English |
| 7969 | **theme** | 1 | 150.37 | 8.676844 | 🔵 low — common in general English |
| 7970 | **reciprocal** | 1 | 150.37 | 8.676844 | 🔵 low — common in general English |
| 7971 | **individually** | 1 | 150.37 | 8.676844 | 🔵 low — common in general English |
| 7972 | **fatty** | 1 | 150.37 | 8.676844 | 🔵 low — common in general English |
| 7973 | **ablaze** | 1 | 150.37 | 8.676844 | 🔵 low — common in general English |
| 7974 | **catapulted** | 1 | 150.37 | 8.676844 | 🔵 low — common in general English |
| 7975 | **dom** | 1 | 150.37 | 8.676844 | 🔵 low — common in general English |
| 7976 | **waited** | 1 | 150.37 | 8.676844 | 🔵 low — common in general English |
| 7977 | **voyage** | 1 | 150.37 | 8.676844 | 🔵 low — common in general English |
| 7978 | **woods** | 1 | 150.37 | 8.676844 | 🔵 low — common in general English |
| 7979 | **relaxing** | 1 | 150.37 | 8.676844 | 🔵 low — common in general English |
| 7980 | **annoyed** | 1 | 150.37 | 8.676844 | 🔵 low — common in general English |
| 7981 | **grazing** | 1 | 150.37 | 8.676844 | 🔵 low — common in general English |
| 7982 | **honesty** | 1 | 150.37 | 8.676844 | 🔵 low — common in general English |
| 7983 | **prudence** | 1 | 150.37 | 8.676844 | 🔵 low — common in general English |
| 7984 | **ted** | 1 | 150.37 | 8.676844 | 🔵 low — common in general English |
| 7985 | **sponsor** | 1 | 150.37 | 8.676844 | 🔵 low — common in general English |
| 7986 | **drums** | 1 | 150.37 | 8.676844 | 🔵 low — common in general English |
| 7987 | **assemblies** | 1 | 150.37 | 8.676844 | 🔵 low — common in general English |
| 7988 | **ideally** | 1 | 150.37 | 8.676844 | 🔵 low — common in general English |
| 7989 | **gravel** | 1 | 150.37 | 8.676844 | 🔵 low — common in general English |
| 7990 | **feasible** | 1 | 150.37 | 8.676844 | 🔵 low — common in general English |
| 7991 | **ingredients** | 1 | 150.37 | 8.676844 | 🔵 low — common in general English |
| 7992 | **sunbeam** | 1 | 150.37 | 8.676844 | 🔵 low — common in general English |
| 7993 | **understands** | 1 | 150.37 | 8.676844 | 🔵 low — common in general English |
| 7994 | **noticeable** | 1 | 150.37 | 8.676844 | 🔵 low — common in general English |
| 7995 | **tenth** | 1 | 150.37 | 8.676844 | 🔵 low — common in general English |
| 7996 | **sara** | 1 | 150.37 | 8.676844 | 🔵 low — common in general English |
| 7997 | **surpassing** | 1 | 150.37 | 8.676844 | 🔵 low — common in general English |
| 7998 | **unrealized** | 1 | 150.37 | 8.676844 | 🔵 low — common in general English |
| 7999 | **omitted** | 1 | 150.37 | 8.676844 | 🔵 low — common in general English |
| 8000 | **discs** | 1 | 150.37 | 8.676844 | 🔵 low — common in general English |
| 8001 | **collected** | 1 | 150.37 | 8.676844 | 🔵 low — common in general English |
| 8002 | **value** | 2 | 148.34 | 4.279929 | 🔵 low — common in general English |
| 8003 | **encountered** | 1 | 147.21 | 8.494523 | 🔵 low — common in general English |
| 8004 | **entrance** | 1 | 147.21 | 8.494523 | 🔵 low — common in general English |
| 8005 | **drawings** | 1 | 147.21 | 8.494523 | 🔵 low — common in general English |
| 8006 | **analyze** | 1 | 147.21 | 8.494523 | 🔵 low — common in general English |
| 8007 | **span** | 1 | 147.21 | 8.494523 | 🔵 low — common in general English |
| 8008 | **topics** | 1 | 147.21 | 8.494523 | 🔵 low — common in general English |
| 8009 | **reassure** | 1 | 147.21 | 8.494523 | 🔵 low — common in general English |
| 8010 | **suspected** | 1 | 147.21 | 8.494523 | 🔵 low — common in general English |
| 8011 | **hal** | 1 | 147.21 | 8.494523 | 🔵 low — common in general English |
| 8012 | **rescued** | 1 | 147.21 | 8.494523 | 🔵 low — common in general English |
| 8013 | **employing** | 1 | 147.21 | 8.494523 | 🔵 low — common in general English |
| 8014 | **intensity** | 1 | 147.21 | 8.494523 | 🔵 low — common in general English |
| 8015 | **lapse** | 1 | 147.21 | 8.494523 | 🔵 low — common in general English |
| 8016 | **practically** | 1 | 147.21 | 8.494523 | 🔵 low — common in general English |
| 8017 | **weights** | 1 | 147.21 | 8.494523 | 🔵 low — common in general English |
| 8018 | **thoroughly** | 1 | 147.21 | 8.494523 | 🔵 low — common in general English |
| 8019 | **prevents** | 1 | 147.21 | 8.494523 | 🔵 low — common in general English |
| 8020 | **improper** | 1 | 147.21 | 8.494523 | 🔵 low — common in general English |
| 8021 | **landed** | 1 | 147.21 | 8.494523 | 🔵 low — common in general English |
| 8022 | **portions** | 1 | 147.21 | 8.494523 | 🔵 low — common in general English |
| 8023 | **dormant** | 1 | 147.21 | 8.494523 | 🔵 low — common in general English |
| 8024 | **cooling** | 1 | 147.21 | 8.494523 | 🔵 low — common in general English |
| 8025 | **conform** | 1 | 147.21 | 8.494523 | 🔵 low — common in general English |
| 8026 | **charts** | 1 | 147.21 | 8.494523 | 🔵 low — common in general English |
| 8027 | **complaining** | 1 | 147.21 | 8.494523 | 🔵 low — common in general English |
| 8028 | **fetch** | 1 | 147.21 | 8.494523 | 🔵 low — common in general English |
| 8029 | **rolls** | 1 | 147.21 | 8.494523 | 🔵 low — common in general English |
| 8030 | **tracks** | 1 | 147.21 | 8.494523 | 🔵 low — common in general English |
| 8031 | **wagons** | 1 | 147.21 | 8.494523 | 🔵 low — common in general English |
| 8032 | **sail** | 1 | 147.21 | 8.494523 | 🔵 low — common in general English |
| 8033 | **urgently** | 1 | 147.21 | 8.494523 | 🔵 low — common in general English |
| 8034 | **surpass** | 1 | 147.21 | 8.494523 | 🔵 low — common in general English |
| 8035 | **troubles** | 1 | 147.21 | 8.494523 | 🔵 low — common in general English |
| 8036 | **lean** | 1 | 147.21 | 8.494523 | 🔵 low — common in general English |
| 8037 | **shells** | 1 | 147.21 | 8.494523 | 🔵 low — common in general English |
| 8038 | **enables** | 1 | 147.21 | 8.494523 | 🔵 low — common in general English |
| 8039 | **brass** | 1 | 147.21 | 8.494523 | 🔵 low — common in general English |
| 8040 | **alternatively** | 1 | 147.21 | 8.494523 | 🔵 low — common in general English |
| 8041 | **absorbing** | 1 | 147.21 | 8.494523 | 🔵 low — common in general English |
| 8042 | **conversation** | 1 | 147.21 | 8.494523 | 🔵 low — common in general English |
| 8043 | **debated** | 1 | 147.21 | 8.494523 | 🔵 low — common in general English |
| 8044 | **debt** | 2 | 146.19 | 4.217857 | 🔵 low — common in general English |
| 8045 | **system** | 2 | 145.79 | 4.206349 | 🔵 low — common in general English |
| 8046 | **refer** | 1 | 144.54 | 8.340372 | 🔵 low — common in general English |
| 8047 | **bars** | 1 | 144.54 | 8.340372 | 🔵 low — common in general English |
| 8048 | **vague** | 1 | 144.54 | 8.340372 | 🔵 low — common in general English |
| 8049 | **slipping** | 1 | 144.54 | 8.340372 | 🔵 low — common in general English |
| 8050 | **collectively** | 1 | 144.54 | 8.340372 | 🔵 low — common in general English |
| 8051 | **unwelcome** | 1 | 144.54 | 8.340372 | 🔵 low — common in general English |
| 8052 | **depression** | 1 | 144.54 | 8.340372 | 🔵 low — common in general English |
| 8053 | **awaits** | 1 | 144.54 | 8.340372 | 🔵 low — common in general English |
| 8054 | **liquor** | 1 | 144.54 | 8.340372 | 🔵 low — common in general English |
| 8055 | **disagreement** | 1 | 144.54 | 8.340372 | 🔵 low — common in general English |
| 8056 | **counterparts** | 1 | 144.54 | 8.340372 | 🔵 low — common in general English |
| 8057 | **gravity** | 1 | 144.54 | 8.340372 | 🔵 low — common in general English |
| 8058 | **heaviest** | 1 | 144.54 | 8.340372 | 🔵 low — common in general English |
| 8059 | **outweighed** | 1 | 144.54 | 8.340372 | 🔵 low — common in general English |
| 8060 | **steers** | 1 | 144.54 | 8.340372 | 🔵 low — common in general English |
| 8061 | **bleak** | 1 | 144.54 | 8.340372 | 🔵 low — common in general English |
| 8062 | **invisible** | 1 | 144.54 | 8.340372 | 🔵 low — common in general English |
| 8063 | **adopting** | 1 | 144.54 | 8.340372 | 🔵 low — common in general English |
| 8064 | **expressions** | 1 | 144.54 | 8.340372 | 🔵 low — common in general English |
| 8065 | **draining** | 1 | 144.54 | 8.340372 | 🔵 low — common in general English |
| 8066 | **negatively** | 1 | 144.54 | 8.340372 | 🔵 low — common in general English |
| 8067 | **upheld** | 1 | 144.54 | 8.340372 | 🔵 low — common in general English |
| 8068 | **patch** | 1 | 144.54 | 8.340372 | 🔵 low — common in general English |
| 8069 | **lightning** | 1 | 144.54 | 8.340372 | 🔵 low — common in general English |
| 8070 | **penalty** | 1 | 144.54 | 8.340372 | 🔵 low — common in general English |
| 8071 | **mixture** | 1 | 144.54 | 8.340372 | 🔵 low — common in general English |
| 8072 | **diminished** | 1 | 144.54 | 8.340372 | 🔵 low — common in general English |
| 8073 | **lent** | 1 | 144.54 | 8.340372 | 🔵 low — common in general English |
| 8074 | **spinning** | 1 | 144.54 | 8.340372 | 🔵 low — common in general English |
| 8075 | **transporting** | 1 | 144.54 | 8.340372 | 🔵 low — common in general English |
| 8076 | **hurts** | 1 | 144.54 | 8.340372 | 🔵 low — common in general English |
| 8077 | **rot** | 1 | 144.54 | 8.340372 | 🔵 low — common in general English |
| 8078 | **repeats** | 1 | 144.54 | 8.340372 | 🔵 low — common in general English |
| 8079 | **dram** | 1 | 144.54 | 8.340372 | 🔵 low — common in general English |
| 8080 | **occupied** | 1 | 144.54 | 8.340372 | 🔵 low — common in general English |
| 8081 | **admit** | 1 | 144.54 | 8.340372 | 🔵 low — common in general English |
| 8082 | **tops** | 1 | 144.54 | 8.340372 | 🔵 low — common in general English |
| 8083 | **goldsmith** | 1 | 144.54 | 8.340372 | 🔵 low — common in general English |
| 8084 | **umbrella** | 1 | 144.54 | 8.340372 | 🔵 low — common in general English |
| 8085 | **intangible** | 1 | 144.54 | 8.340372 | 🔵 low — common in general English |
| 8086 | **sunshine** | 1 | 144.54 | 8.340372 | 🔵 low — common in general English |
| 8087 | **north-west** | 1 | 144.54 | 8.340372 | 🔵 low — common in general English |
| 8088 | **ensuring** | 1 | 144.54 | 8.340372 | 🔵 low — common in general English |
| 8089 | **rod** | 1 | 144.54 | 8.340372 | 🔵 low — common in general English |
| 8090 | **opinions** | 1 | 144.54 | 8.340372 | 🔵 low — common in general English |
| 8091 | **chicken** | 1 | 144.54 | 8.340372 | 🔵 low — common in general English |
| 8092 | **valuable** | 1 | 144.54 | 8.340372 | 🔵 low — common in general English |
| 8093 | **unaffected** | 1 | 144.54 | 8.340372 | 🔵 low — common in general English |
| 8094 | **differ** | 1 | 144.54 | 8.340372 | 🔵 low — common in general English |
| 8095 | **duration** | 1 | 144.54 | 8.340372 | 🔵 low — common in general English |
| 8096 | **abu** | 1 | 144.54 | 8.340372 | 🔵 low — common in general English |
| 8097 | **increased** | 2 | 143.79 | 4.148555 | 🔵 low — common in general English |
| 8098 | **domestic** | 2 | 143.42 | 4.137814 | 🔵 low — common in general English |
| 8099 | **sets** | 2 | 143.27 | 4.13355 | 🔵 low — common in general English |
| 8100 | **sounded** | 1 | 142.22 | 8.206841 | 🔵 low — common in general English |
| 8101 | **enthusiasm** | 1 | 142.22 | 8.206841 | 🔵 low — common in general English |
| 8102 | **reputation** | 1 | 142.22 | 8.206841 | 🔵 low — common in general English |
| 8103 | **demonstrate** | 1 | 142.22 | 8.206841 | 🔵 low — common in general English |
| 8104 | **reliable** | 1 | 142.22 | 8.206841 | 🔵 low — common in general English |
| 8105 | **stuck** | 1 | 142.22 | 8.206841 | 🔵 low — common in general English |
| 8106 | **hawk** | 1 | 142.22 | 8.206841 | 🔵 low — common in general English |
| 8107 | **undertakings** | 1 | 142.22 | 8.206841 | 🔵 low — common in general English |
| 8108 | **fate** | 1 | 142.22 | 8.206841 | 🔵 low — common in general English |
| 8109 | **softer** | 1 | 142.22 | 8.206841 | 🔵 low — common in general English |
| 8110 | **concentrating** | 1 | 142.22 | 8.206841 | 🔵 low — common in general English |
| 8111 | **shifted** | 1 | 142.22 | 8.206841 | 🔵 low — common in general English |
| 8112 | **hazardous** | 1 | 142.22 | 8.206841 | 🔵 low — common in general English |
| 8113 | **label** | 1 | 142.22 | 8.206841 | 🔵 low — common in general English |
| 8114 | **interference** | 1 | 142.22 | 8.206841 | 🔵 low — common in general English |
| 8115 | **tug** | 1 | 142.22 | 8.206841 | 🔵 low — common in general English |
| 8116 | **distributing** | 1 | 142.22 | 8.206841 | 🔵 low — common in general English |
| 8117 | **grip** | 1 | 142.22 | 8.206841 | 🔵 low — common in general English |
| 8118 | **mercury** | 1 | 142.22 | 8.206841 | 🔵 low — common in general English |
| 8119 | **burdens** | 1 | 142.22 | 8.206841 | 🔵 low — common in general English |
| 8120 | **finish** | 1 | 142.22 | 8.206841 | 🔵 low — common in general English |
| 8121 | **readily** | 1 | 142.22 | 8.206841 | 🔵 low — common in general English |
| 8122 | **lessening** | 1 | 142.22 | 8.206841 | 🔵 low — common in general English |
| 8123 | **ranks** | 1 | 142.22 | 8.206841 | 🔵 low — common in general English |
| 8124 | **desired** | 1 | 142.22 | 8.206841 | 🔵 low — common in general English |
| 8125 | **impatience** | 1 | 142.22 | 8.206841 | 🔵 low — common in general English |
| 8126 | **slope** | 1 | 142.22 | 8.206841 | 🔵 low — common in general English |
| 8127 | **intelligent** | 1 | 142.22 | 8.206841 | 🔵 low — common in general English |
| 8128 | **pronounced** | 1 | 142.22 | 8.206841 | 🔵 low — common in general English |
| 8129 | **deter** | 1 | 142.22 | 8.206841 | 🔵 low — common in general English |
| 8130 | **drives** | 1 | 142.22 | 8.206841 | 🔵 low — common in general English |
| 8131 | **agriculture** | 2 | 141.61 | 4.085773 | 🔵 low — common in general English |
| 8132 | **minister** | 2 | 140.30 | 4.047958 | 🔵 low — common in general English |
| 8133 | **rein** | 1 | 140.18 | 8.089058 | 🔵 low — common in general English |
| 8134 | **player** | 1 | 140.18 | 8.089058 | 🔵 low — common in general English |
| 8135 | **relaxation** | 1 | 140.18 | 8.089058 | 🔵 low — common in general English |
| 8136 | **lists** | 1 | 140.18 | 8.089058 | 🔵 low — common in general English |
| 8137 | **proof** | 1 | 140.18 | 8.089058 | 🔵 low — common in general English |
| 8138 | **matching** | 1 | 140.18 | 8.089058 | 🔵 low — common in general English |
| 8139 | **unexpectedly** | 1 | 140.18 | 8.089058 | 🔵 low — common in general English |
| 8140 | **roads** | 1 | 140.18 | 8.089058 | 🔵 low — common in general English |
| 8141 | **revived** | 1 | 140.18 | 8.089058 | 🔵 low — common in general English |
| 8142 | **supplementary** | 1 | 140.18 | 8.089058 | 🔵 low — common in general English |
| 8143 | **ridiculous** | 1 | 140.18 | 8.089058 | 🔵 low — common in general English |
| 8144 | **schemes** | 1 | 140.18 | 8.089058 | 🔵 low — common in general English |
| 8145 | **familiar** | 1 | 140.18 | 8.089058 | 🔵 low — common in general English |
| 8146 | **rigid** | 1 | 140.18 | 8.089058 | 🔵 low — common in general English |
| 8147 | **desperate** | 1 | 140.18 | 8.089058 | 🔵 low — common in general English |
| 8148 | **dealt** | 1 | 140.18 | 8.089058 | 🔵 low — common in general English |
| 8149 | **attacking** | 1 | 140.18 | 8.089058 | 🔵 low — common in general English |
| 8150 | **clouded** | 1 | 140.18 | 8.089058 | 🔵 low — common in general English |
| 8151 | **hitting** | 1 | 140.18 | 8.089058 | 🔵 low — common in general English |
| 8152 | **wiped** | 1 | 140.18 | 8.089058 | 🔵 low — common in general English |
| 8153 | **inclined** | 1 | 140.18 | 8.089058 | 🔵 low — common in general English |
| 8154 | **leaf** | 1 | 140.18 | 8.089058 | 🔵 low — common in general English |
| 8155 | **insist** | 1 | 140.18 | 8.089058 | 🔵 low — common in general English |
| 8156 | **grossly** | 1 | 140.18 | 8.089058 | 🔵 low — common in general English |
| 8157 | **spurred** | 1 | 140.18 | 8.089058 | 🔵 low — common in general English |
| 8158 | **clarify** | 1 | 140.18 | 8.089058 | 🔵 low — common in general English |
| 8159 | **intellectual** | 1 | 140.18 | 8.089058 | 🔵 low — common in general English |
| 8160 | **spreads** | 1 | 140.18 | 8.089058 | 🔵 low — common in general English |
| 8161 | **indebted** | 1 | 140.18 | 8.089058 | 🔵 low — common in general English |
| 8162 | **borrowed** | 1 | 140.18 | 8.089058 | 🔵 low — common in general English |
| 8163 | **lacked** | 1 | 140.18 | 8.089058 | 🔵 low — common in general English |
| 8164 | **stretching** | 1 | 140.18 | 8.089058 | 🔵 low — common in general English |
| 8165 | **funeral** | 1 | 140.18 | 8.089058 | 🔵 low — common in general English |
| 8166 | **solved** | 1 | 140.18 | 8.089058 | 🔵 low — common in general English |
| 8167 | **mutually** | 1 | 138.36 | 7.983697 | 🔵 low — common in general English |
| 8168 | **collective** | 1 | 138.36 | 7.983697 | 🔵 low — common in general English |
| 8169 | **showers** | 1 | 138.36 | 7.983697 | 🔵 low — common in general English |
| 8170 | **succeeds** | 1 | 138.36 | 7.983697 | 🔵 low — common in general English |
| 8171 | **pool** | 1 | 138.36 | 7.983697 | 🔵 low — common in general English |
| 8172 | **withdrawing** | 1 | 138.36 | 7.983697 | 🔵 low — common in general English |
| 8173 | **varying** | 1 | 138.36 | 7.983697 | 🔵 low — common in general English |
| 8174 | **lock** | 1 | 138.36 | 7.983697 | 🔵 low — common in general English |
| 8175 | **prominent** | 1 | 138.36 | 7.983697 | 🔵 low — common in general English |
| 8176 | **prop** | 1 | 138.36 | 7.983697 | 🔵 low — common in general English |
| 8177 | **pointing** | 1 | 138.36 | 7.983697 | 🔵 low — common in general English |
| 8178 | **thwart** | 1 | 138.36 | 7.983697 | 🔵 low — common in general English |
| 8179 | **evident** | 1 | 138.36 | 7.983697 | 🔵 low — common in general English |
| 8180 | **examined** | 1 | 138.36 | 7.983697 | 🔵 low — common in general English |
| 8181 | **nearing** | 1 | 138.36 | 7.983697 | 🔵 low — common in general English |
| 8182 | **cook** | 1 | 138.36 | 7.983697 | 🔵 low — common in general English |
| 8183 | **obliged** | 1 | 138.36 | 7.983697 | 🔵 low — common in general English |
| 8184 | **extract** | 1 | 138.36 | 7.983697 | 🔵 low — common in general English |
| 8185 | **plate** | 1 | 138.36 | 7.983697 | 🔵 low — common in general English |
| 8186 | **equals** | 1 | 138.36 | 7.983697 | 🔵 low — common in general English |
| 8187 | **persist** | 1 | 138.36 | 7.983697 | 🔵 low — common in general English |
| 8188 | **features** | 1 | 138.36 | 7.983697 | 🔵 low — common in general English |
| 8189 | **shape** | 1 | 138.36 | 7.983697 | 🔵 low — common in general English |
| 8190 | **subscribe** | 1 | 138.36 | 7.983697 | 🔵 low — common in general English |
| 8191 | **unwanted** | 1 | 138.36 | 7.983697 | 🔵 low — common in general English |
| 8192 | **incorrect** | 1 | 138.36 | 7.983697 | 🔵 low — common in general English |
| 8193 | **turmoil** | 1 | 136.70 | 7.888387 | 🔵 low — common in general English |
| 8194 | **dominated** | 1 | 136.70 | 7.888387 | 🔵 low — common in general English |
| 8195 | **fought** | 1 | 136.70 | 7.888387 | 🔵 low — common in general English |
| 8196 | **soar** | 1 | 136.70 | 7.888387 | 🔵 low — common in general English |
| 8197 | **removing** | 1 | 136.70 | 7.888387 | 🔵 low — common in general English |
| 8198 | **preceding** | 1 | 136.70 | 7.888387 | 🔵 low — common in general English |
| 8199 | **strategies** | 1 | 136.70 | 7.888387 | 🔵 low — common in general English |
| 8200 | **meals** | 1 | 136.70 | 7.888387 | 🔵 low — common in general English |
| 8201 | **persons** | 1 | 136.70 | 7.888387 | 🔵 low — common in general English |
| 8202 | **disastrous** | 1 | 136.70 | 7.888387 | 🔵 low — common in general English |
| 8203 | **warranted** | 1 | 136.70 | 7.888387 | 🔵 low — common in general English |
| 8204 | **plains** | 1 | 136.70 | 7.888387 | 🔵 low — common in general English |
| 8205 | **austerity** | 1 | 136.70 | 7.888387 | 🔵 low — common in general English |
| 8206 | **modestly** | 1 | 136.70 | 7.888387 | 🔵 low — common in general English |
| 8207 | **worthwhile** | 1 | 136.70 | 7.888387 | 🔵 low — common in general English |
| 8208 | **halting** | 1 | 136.70 | 7.888387 | 🔵 low — common in general English |
| 8209 | **departure** | 1 | 136.70 | 7.888387 | 🔵 low — common in general English |
| 8210 | **persistent** | 1 | 136.70 | 7.888387 | 🔵 low — common in general English |
| 8211 | **revealed** | 1 | 135.20 | 7.801376 | 🔵 low — common in general English |
| 8212 | **tendency** | 1 | 135.20 | 7.801376 | 🔵 low — common in general English |
| 8213 | **thirds** | 1 | 135.20 | 7.801376 | 🔵 low — common in general English |
| 8214 | **miss** | 1 | 135.20 | 7.801376 | 🔵 low — common in general English |
| 8215 | **prohibited** | 1 | 135.20 | 7.801376 | 🔵 low — common in general English |
| 8216 | **misleading** | 1 | 135.20 | 7.801376 | 🔵 low — common in general English |
| 8217 | **mood** | 1 | 135.20 | 7.801376 | 🔵 low — common in general English |
| 8218 | **purely** | 1 | 135.20 | 7.801376 | 🔵 low — common in general English |
| 8219 | **essentially** | 1 | 135.20 | 7.801376 | 🔵 low — common in general English |
| 8220 | **restrain** | 1 | 135.20 | 7.801376 | 🔵 low — common in general English |
| 8221 | **stemming** | 1 | 135.20 | 7.801376 | 🔵 low — common in general English |
| 8222 | **hall** | 1 | 135.20 | 7.801376 | 🔵 low — common in general English |
| 8223 | **candidates** | 1 | 135.20 | 7.801376 | 🔵 low — common in general English |
| 8224 | **tended** | 1 | 135.20 | 7.801376 | 🔵 low — common in general English |
| 8225 | **adapt** | 1 | 135.20 | 7.801376 | 🔵 low — common in general English |
| 8226 | **rolling** | 1 | 135.20 | 7.801376 | 🔵 low — common in general English |
| 8227 | **claiming** | 1 | 135.20 | 7.801376 | 🔵 low — common in general English |
| 8228 | **finds** | 1 | 135.20 | 7.801376 | 🔵 low — common in general English |
| 8229 | **consequently** | 1 | 135.20 | 7.801376 | 🔵 low — common in general English |
| 8230 | **crew** | 1 | 135.20 | 7.801376 | 🔵 low — common in general English |
| 8231 | **soaring** | 1 | 135.20 | 7.801376 | 🔵 low — common in general English |
| 8232 | **vein** | 1 | 135.20 | 7.801376 | 🔵 low — common in general English |
| 8233 | **repairs** | 1 | 135.20 | 7.801376 | 🔵 low — common in general English |
| 8234 | **containers** | 1 | 135.20 | 7.801376 | 🔵 low — common in general English |
| 8235 | **classified** | 1 | 135.20 | 7.801376 | 🔵 low — common in general English |
| 8236 | **describing** | 1 | 135.20 | 7.801376 | 🔵 low — common in general English |
| 8237 | **processes** | 1 | 135.20 | 7.801376 | 🔵 low — common in general English |
| 8238 | **wash** | 1 | 135.20 | 7.801376 | 🔵 low — common in general English |
| 8239 | **unstable** | 1 | 135.20 | 7.801376 | 🔵 low — common in general English |
| 8240 | **recording** | 1 | 135.20 | 7.801376 | 🔵 low — common in general English |
| 8241 | **earnings** | 2 | 134.69 | 3.886025 | 🔵 low — common in general English |
| 8242 | **forming** | 1 | 133.81 | 7.721333 | 🔵 low — common in general English |
| 8243 | **varieties** | 1 | 133.81 | 7.721333 | 🔵 low — common in general English |
| 8244 | **revive** | 1 | 133.81 | 7.721333 | 🔵 low — common in general English |
| 8245 | **sceptical** | 1 | 133.81 | 7.721333 | 🔵 low — common in general English |
| 8246 | **opposing** | 1 | 133.81 | 7.721333 | 🔵 low — common in general English |
| 8247 | **combining** | 1 | 133.81 | 7.721333 | 🔵 low — common in general English |
| 8248 | **composite** | 1 | 133.81 | 7.721333 | 🔵 low — common in general English |
| 8249 | **calculations** | 1 | 133.81 | 7.721333 | 🔵 low — common in general English |
| 8250 | **ideal** | 1 | 133.81 | 7.721333 | 🔵 low — common in general English |
| 8251 | **modify** | 1 | 133.81 | 7.721333 | 🔵 low — common in general English |
| 8252 | **fraud** | 1 | 133.81 | 7.721333 | 🔵 low — common in general English |
| 8253 | **repaying** | 1 | 133.81 | 7.721333 | 🔵 low — common in general English |
| 8254 | **appreciate** | 1 | 133.81 | 7.721333 | 🔵 low — common in general English |
| 8255 | **goodwill** | 1 | 133.81 | 7.721333 | 🔵 low — common in general English |
| 8256 | **substitute** | 1 | 133.81 | 7.721333 | 🔵 low — common in general English |
| 8257 | **interesting** | 1 | 133.81 | 7.721333 | 🔵 low — common in general English |
| 8258 | **mission** | 1 | 133.81 | 7.721333 | 🔵 low — common in general English |
| 8259 | **thin** | 1 | 133.81 | 7.721333 | 🔵 low — common in general English |
| 8260 | **tangible** | 1 | 133.81 | 7.721333 | 🔵 low — common in general English |
| 8261 | **destination** | 1 | 133.81 | 7.721333 | 🔵 low — common in general English |
| 8262 | **played** | 1 | 132.53 | 7.647225 | 🔵 low — common in general English |
| 8263 | **thereby** | 1 | 132.53 | 7.647225 | 🔵 low — common in general English |
| 8264 | **categories** | 1 | 132.53 | 7.647225 | 🔵 low — common in general English |
| 8265 | **weaken** | 1 | 132.53 | 7.647225 | 🔵 low — common in general English |
| 8266 | **blame** | 1 | 132.53 | 7.647225 | 🔵 low — common in general English |
| 8267 | **letters** | 1 | 132.53 | 7.647225 | 🔵 low — common in general English |
| 8268 | **accompanying** | 1 | 132.53 | 7.647225 | 🔵 low — common in general English |
| 8269 | **dipped** | 1 | 132.53 | 7.647225 | 🔵 low — common in general English |
| 8270 | **professor** | 1 | 132.53 | 7.647225 | 🔵 low — common in general English |
| 8271 | **reacted** | 1 | 132.53 | 7.647225 | 🔵 low — common in general English |
| 8272 | **thereafter** | 1 | 132.53 | 7.647225 | 🔵 low — common in general English |
| 8273 | **bean** | 1 | 132.53 | 7.647225 | 🔵 low — common in general English |
| 8274 | **exclusively** | 1 | 132.53 | 7.647225 | 🔵 low — common in general English |
| 8275 | **chosen** | 1 | 132.53 | 7.647225 | 🔵 low — common in general English |
| 8276 | **vegetables** | 1 | 132.53 | 7.647225 | 🔵 low — common in general English |
| 8277 | **challenges** | 1 | 132.53 | 7.647225 | 🔵 low — common in general English |
| 8278 | **motion** | 1 | 132.53 | 7.647225 | 🔵 low — common in general English |
| 8279 | **testing** | 1 | 131.33 | 7.578232 | 🔵 low — common in general English |
| 8280 | **aggregates** | 1 | 131.33 | 7.578232 | 🔵 low — common in general English |
| 8281 | **cycle** | 1 | 131.33 | 7.578232 | 🔵 low — common in general English |
| 8282 | **stored** | 1 | 131.33 | 7.578232 | 🔵 low — common in general English |
| 8283 | **harvests** | 1 | 131.33 | 7.578232 | 🔵 low — common in general English |
| 8284 | **justified** | 1 | 131.33 | 7.578232 | 🔵 low — common in general English |
| 8285 | **rated** | 1 | 131.33 | 7.578232 | 🔵 low — common in general English |
| 8286 | **hits** | 1 | 131.33 | 7.578232 | 🔵 low — common in general English |
| 8287 | **challenged** | 1 | 131.33 | 7.578232 | 🔵 low — common in general English |
| 8288 | **seller** | 1 | 131.33 | 7.578232 | 🔵 low — common in general English |
| 8289 | **revolving** | 1 | 131.33 | 7.578232 | 🔵 low — common in general English |
| 8290 | **interpreted** | 1 | 131.33 | 7.578232 | 🔵 low — common in general English |
| 8291 | **sending** | 1 | 131.33 | 7.578232 | 🔵 low — common in general English |
| 8292 | **routes** | 1 | 130.21 | 7.513694 | 🔵 low — common in general English |
| 8293 | **relation** | 1 | 130.21 | 7.513694 | 🔵 low — common in general English |
| 8294 | **pictures** | 1 | 130.21 | 7.513694 | 🔵 low — common in general English |
| 8295 | **declare** | 1 | 130.21 | 7.513694 | 🔵 low — common in general English |
| 8296 | **driving** | 1 | 130.21 | 7.513694 | 🔵 low — common in general English |
| 8297 | **comprise** | 1 | 130.21 | 7.513694 | 🔵 low — common in general English |
| 8298 | **inevitable** | 1 | 130.21 | 7.513694 | 🔵 low — common in general English |
| 8299 | **ferry** | 1 | 130.21 | 7.513694 | 🔵 low — common in general English |
| 8300 | **undertaken** | 1 | 130.21 | 7.513694 | 🔵 low — common in general English |
| 8301 | **mild** | 1 | 130.21 | 7.513694 | 🔵 low — common in general English |
| 8302 | **wary** | 1 | 130.21 | 7.513694 | 🔵 low — common in general English |
| 8303 | **emerging** | 1 | 130.21 | 7.513694 | 🔵 low — common in general English |
| 8304 | **whites** | 1 | 130.21 | 7.513694 | 🔵 low — common in general English |
| 8305 | **worry** | 1 | 130.21 | 7.513694 | 🔵 low — common in general English |
| 8306 | **unlike** | 1 | 130.21 | 7.513694 | 🔵 low — common in general English |
| 8307 | **soil** | 1 | 130.21 | 7.513694 | 🔵 low — common in general English |
| 8308 | **sale** | 2 | 129.81 | 3.745252 | 🔵 low — common in general English |
| 8309 | **communities** | 1 | 129.16 | 7.453069 | 🔵 low — common in general English |
| 8310 | **historical** | 1 | 129.16 | 7.453069 | 🔵 low — common in general English |
| 8311 | **calculating** | 1 | 129.16 | 7.453069 | 🔵 low — common in general English |
| 8312 | **sharing** | 1 | 129.16 | 7.453069 | 🔵 low — common in general English |
| 8313 | **assessment** | 1 | 129.16 | 7.453069 | 🔵 low — common in general English |
| 8314 | **regularly** | 1 | 129.16 | 7.453069 | 🔵 low — common in general English |
| 8315 | **reacting** | 1 | 129.16 | 7.453069 | 🔵 low — common in general English |
| 8316 | **farming** | 1 | 129.16 | 7.453069 | 🔵 low — common in general English |
| 8317 | **cities** | 1 | 129.16 | 7.453069 | 🔵 low — common in general English |
| 8318 | **rejection** | 1 | 129.16 | 7.453069 | 🔵 low — common in general English |
| 8319 | **imposing** | 1 | 128.17 | 7.395911 | 🔵 low — common in general English |
| 8320 | **lots** | 1 | 128.17 | 7.395911 | 🔵 low — common in general English |
| 8321 | **threats** | 1 | 128.17 | 7.395911 | 🔵 low — common in general English |
| 8322 | **obvious** | 1 | 128.17 | 7.395911 | 🔵 low — common in general English |
| 8323 | **permission** | 1 | 128.17 | 7.395911 | 🔵 low — common in general English |
| 8324 | **enquiries** | 1 | 128.17 | 7.395911 | 🔵 low — common in general English |
| 8325 | **fix** | 1 | 128.17 | 7.395911 | 🔵 low — common in general English |
| 8326 | **possibilities** | 1 | 128.17 | 7.395911 | 🔵 low — common in general English |
| 8327 | **procedure** | 1 | 128.17 | 7.395911 | 🔵 low — common in general English |
| 8328 | **demanded** | 1 | 128.17 | 7.395911 | 🔵 low — common in general English |
| 8329 | **creditor** | 1 | 128.17 | 7.395911 | 🔵 low — common in general English |
| 8330 | **convince** | 1 | 128.17 | 7.395911 | 🔵 low — common in general English |
| 8331 | **secondary** | 1 | 128.17 | 7.395911 | 🔵 low — common in general English |
| 8332 | **apparel** | 1 | 128.17 | 7.395911 | 🔵 low — common in general English |
| 8333 | **society** | 1 | 128.17 | 7.395911 | 🔵 low — common in general English |
| 8334 | **lesser** | 1 | 128.17 | 7.395911 | 🔵 low — common in general English |
| 8335 | **requests** | 1 | 128.17 | 7.395911 | 🔵 low — common in general English |
| 8336 | **ali** | 1 | 127.23 | 7.341843 | 🔵 low — common in general English |
| 8337 | **milling** | 1 | 127.23 | 7.341843 | 🔵 low — common in general English |
| 8338 | **argument** | 1 | 127.23 | 7.341843 | 🔵 low — common in general English |
| 8339 | **returning** | 1 | 127.23 | 7.341843 | 🔵 low — common in general English |
| 8340 | **handle** | 1 | 127.23 | 7.341843 | 🔵 low — common in general English |
| 8341 | **consent** | 1 | 127.23 | 7.341843 | 🔵 low — common in general English |
| 8342 | **evaluating** | 1 | 127.23 | 7.341843 | 🔵 low — common in general English |
| 8343 | **hurting** | 1 | 127.23 | 7.341843 | 🔵 low — common in general English |
| 8344 | **sensitive** | 1 | 127.23 | 7.341843 | 🔵 low — common in general English |
| 8345 | **judge** | 1 | 127.23 | 7.341843 | 🔵 low — common in general English |
| 8346 | **grants** | 1 | 127.23 | 7.341843 | 🔵 low — common in general English |
| 8347 | **star** | 1 | 127.23 | 7.341843 | 🔵 low — common in general English |
| 8348 | **slack** | 1 | 126.34 | 7.29055 | 🔵 low — common in general English |
| 8349 | **favoured** | 1 | 126.34 | 7.29055 | 🔵 low — common in general English |
| 8350 | **quiet** | 1 | 126.34 | 7.29055 | 🔵 low — common in general English |
| 8351 | **quantity** | 1 | 126.34 | 7.29055 | 🔵 low — common in general English |
| 8352 | **arranging** | 1 | 126.34 | 7.29055 | 🔵 low — common in general English |
| 8353 | **limiting** | 1 | 125.50 | 7.24176 | 🔵 low — common in general English |
| 8354 | **accident** | 1 | 125.50 | 7.24176 | 🔵 low — common in general English |
| 8355 | **treasurer** | 1 | 125.50 | 7.24176 | 🔵 low — common in general English |
| 8356 | **concerted** | 1 | 125.50 | 7.24176 | 🔵 low — common in general English |
| 8357 | **pressed** | 1 | 125.50 | 7.24176 | 🔵 low — common in general English |
| 8358 | **opposes** | 1 | 125.50 | 7.24176 | 🔵 low — common in general English |
| 8359 | **couple** | 1 | 125.50 | 7.24176 | 🔵 low — common in general English |
| 8360 | **prevented** | 1 | 125.50 | 7.24176 | 🔵 low — common in general English |
| 8361 | **alter** | 1 | 125.50 | 7.24176 | 🔵 low — common in general English |
| 8362 | **acted** | 1 | 125.50 | 7.24176 | 🔵 low — common in general English |
| 8363 | **evaluation** | 1 | 125.50 | 7.24176 | 🔵 low — common in general English |
| 8364 | **wave** | 1 | 125.50 | 7.24176 | 🔵 low — common in general English |
| 8365 | **lanka** | 1 | 125.50 | 7.24176 | 🔵 low — common in general English |
| 8366 | **chamber** | 1 | 125.50 | 7.24176 | 🔵 low — common in general English |
| 8367 | **covers** | 1 | 124.69 | 7.19524 | 🔵 low — common in general English |
| 8368 | **exercised** | 1 | 124.69 | 7.19524 | 🔵 low — common in general English |
| 8369 | **engine** | 1 | 124.69 | 7.19524 | 🔵 low — common in general English |
| 8370 | **accused** | 1 | 124.69 | 7.19524 | 🔵 low — common in general English |
| 8371 | **criteria** | 1 | 124.69 | 7.19524 | 🔵 low — common in general English |
| 8372 | **pro** | 1 | 124.69 | 7.19524 | 🔵 low — common in general English |
| 8373 | **attract** | 1 | 124.69 | 7.19524 | 🔵 low — common in general English |
| 8374 | **distribute** | 1 | 124.69 | 7.19524 | 🔵 low — common in general English |
| 8375 | **instrument** | 1 | 124.69 | 7.19524 | 🔵 low — common in general English |
| 8376 | **linking** | 1 | 123.92 | 7.150788 | 🔵 low — common in general English |
| 8377 | **locations** | 1 | 123.92 | 7.150788 | 🔵 low — common in general English |
| 8378 | **disappointed** | 1 | 123.92 | 7.150788 | 🔵 low — common in general English |
| 8379 | **reject** | 1 | 123.92 | 7.150788 | 🔵 low — common in general English |
| 8380 | **coins** | 1 | 123.92 | 7.150788 | 🔵 low — common in general English |
| 8381 | **defined** | 1 | 123.92 | 7.150788 | 🔵 low — common in general English |
| 8382 | **secured** | 1 | 123.92 | 7.150788 | 🔵 low — common in general English |
| 8383 | **dominion** | 1 | 123.92 | 7.150788 | 🔵 low — common in general English |
| 8384 | **considerably** | 1 | 123.18 | 7.108229 | 🔵 low — common in general English |
| 8385 | **preserve** | 1 | 123.18 | 7.108229 | 🔵 low — common in general English |
| 8386 | **entering** | 1 | 122.48 | 7.067407 | 🔵 low — common in general English |
| 8387 | **freeze** | 1 | 122.48 | 7.067407 | 🔵 low — common in general English |
| 8388 | **awaiting** | 1 | 122.48 | 7.067407 | 🔵 low — common in general English |
| 8389 | **consuming** | 1 | 122.48 | 7.067407 | 🔵 low — common in general English |
| 8390 | **successfully** | 1 | 122.48 | 7.067407 | 🔵 low — common in general English |
| 8391 | **discovered** | 1 | 122.48 | 7.067407 | 🔵 low — common in general English |
| 8392 | **receives** | 1 | 122.48 | 7.067407 | 🔵 low — common in general English |
| 8393 | **spur** | 1 | 122.48 | 7.067407 | 🔵 low — common in general English |
| 8394 | **guidelines** | 1 | 121.80 | 7.028186 | 🔵 low — common in general English |
| 8395 | **contrast** | 1 | 121.80 | 7.028186 | 🔵 low — common in general English |
| 8396 | **decides** | 1 | 121.80 | 7.028186 | 🔵 low — common in general English |
| 8397 | **valid** | 1 | 121.80 | 7.028186 | 🔵 low — common in general English |
| 8398 | **participating** | 1 | 121.80 | 7.028186 | 🔵 low — common in general English |
| 8399 | **forcing** | 1 | 121.80 | 7.028186 | 🔵 low — common in general English |
| 8400 | **questioned** | 1 | 121.80 | 7.028186 | 🔵 low — common in general English |
| 8401 | **sixth** | 1 | 121.80 | 7.028186 | 🔵 low — common in general English |
| 8402 | **printing** | 1 | 121.80 | 7.028186 | 🔵 low — common in general English |
| 8403 | **warns** | 1 | 121.14 | 6.990446 | 🔵 low — common in general English |
| 8404 | **table** | 1 | 121.14 | 6.990446 | 🔵 low — common in general English |
| 8405 | **exact** | 1 | 121.14 | 6.990446 | 🔵 low — common in general English |
| 8406 | **lifts** | 1 | 121.14 | 6.990446 | 🔵 low — common in general English |
| 8407 | **convert** | 1 | 121.14 | 6.990446 | 🔵 low — common in general English |
| 8408 | **qualified** | 1 | 121.14 | 6.990446 | 🔵 low — common in general English |
| 8409 | **window** | 1 | 121.14 | 6.990446 | 🔵 low — common in general English |
| 8410 | **match** | 1 | 120.51 | 6.954078 | 🔵 low — common in general English |
| 8411 | **returns** | 1 | 120.51 | 6.954078 | 🔵 low — common in general English |
| 8412 | **dropping** | 1 | 120.51 | 6.954078 | 🔵 low — common in general English |
| 8413 | **missiles** | 1 | 120.51 | 6.954078 | 🔵 low — common in general English |
| 8414 | **flour** | 1 | 120.51 | 6.954078 | 🔵 low — common in general English |
| 8415 | **reply** | 1 | 120.51 | 6.954078 | 🔵 low — common in general English |
| 8416 | **acceptance** | 1 | 120.51 | 6.954078 | 🔵 low — common in general English |
| 8417 | **scope** | 1 | 120.51 | 6.954078 | 🔵 low — common in general English |
| 8418 | **diamond** | 1 | 119.90 | 6.918987 | 🔵 low — common in general English |
| 8419 | **engaged** | 1 | 119.90 | 6.918987 | 🔵 low — common in general English |
| 8420 | **necessarily** | 1 | 119.90 | 6.918987 | 🔵 low — common in general English |
| 8421 | **soared** | 1 | 119.90 | 6.918987 | 🔵 low — common in general English |
| 8422 | **handling** | 1 | 119.90 | 6.918987 | 🔵 low — common in general English |
| 8423 | **tobacco** | 1 | 119.90 | 6.918987 | 🔵 low — common in general English |
| 8424 | **discussing** | 1 | 119.90 | 6.918987 | 🔵 low — common in general English |
| 8425 | **optimism** | 1 | 119.32 | 6.885085 | 🔵 low — common in general English |
| 8426 | **prevailing** | 1 | 119.32 | 6.885085 | 🔵 low — common in general English |
| 8427 | **studies** | 1 | 119.32 | 6.885085 | 🔵 low — common in general English |
| 8428 | **expecting** | 1 | 119.32 | 6.885085 | 🔵 low — common in general English |
| 8429 | **critical** | 1 | 119.32 | 6.885085 | 🔵 low — common in general English |
| 8430 | **proceeding** | 1 | 119.32 | 6.885085 | 🔵 low — common in general English |
| 8431 | **conducted** | 1 | 119.32 | 6.885085 | 🔵 low — common in general English |
| 8432 | **respective** | 1 | 119.32 | 6.885085 | 🔵 low — common in general English |
| 8433 | **speed** | 1 | 119.32 | 6.885085 | 🔵 low — common in general English |
| 8434 | **friendly** | 1 | 119.32 | 6.885085 | 🔵 low — common in general English |
| 8435 | **adopt** | 1 | 119.32 | 6.885085 | 🔵 low — common in general English |
| 8436 | **explore** | 1 | 118.75 | 6.852295 | 🔵 low — common in general English |
| 8437 | **tool** | 1 | 118.75 | 6.852295 | 🔵 low — common in general English |
| 8438 | **quick** | 1 | 118.75 | 6.852295 | 🔵 low — common in general English |
| 8439 | **incurred** | 1 | 118.75 | 6.852295 | 🔵 low — common in general English |
| 8440 | **somewhat** | 1 | 118.75 | 6.852295 | 🔵 low — common in general English |
| 8441 | **eliminate** | 1 | 118.75 | 6.852295 | 🔵 low — common in general English |
| 8442 | **settled** | 1 | 118.75 | 6.852295 | 🔵 low — common in general English |
| 8443 | **prove** | 1 | 118.75 | 6.852295 | 🔵 low — common in general English |
| 8444 | **responding** | 1 | 118.75 | 6.852295 | 🔵 low — common in general English |
| 8445 | **deterioration** | 1 | 118.20 | 6.820546 | 🔵 low — common in general English |
| 8446 | **reduces** | 1 | 118.20 | 6.820546 | 🔵 low — common in general English |
| 8447 | **formula** | 1 | 118.20 | 6.820546 | 🔵 low — common in general English |
| 8448 | **rally** | 1 | 118.20 | 6.820546 | 🔵 low — common in general English |
| 8449 | **steadily** | 1 | 118.20 | 6.820546 | 🔵 low — common in general English |
| 8450 | **flag** | 1 | 118.20 | 6.820546 | 🔵 low — common in general English |
| 8451 | **extensive** | 1 | 118.20 | 6.820546 | 🔵 low — common in general English |
| 8452 | **enhance** | 1 | 117.67 | 6.789775 | 🔵 low — common in general English |
| 8453 | **tightening** | 1 | 117.67 | 6.789775 | 🔵 low — common in general English |
| 8454 | **permanent** | 1 | 117.67 | 6.789775 | 🔵 low — common in general English |
| 8455 | **play** | 1 | 117.67 | 6.789775 | 🔵 low — common in general English |
| 8456 | **allows** | 1 | 117.67 | 6.789775 | 🔵 low — common in general English |
| 8457 | **treatment** | 1 | 117.67 | 6.789775 | 🔵 low — common in general English |
| 8458 | **informed** | 1 | 117.67 | 6.789775 | 🔵 low — common in general English |
| 8459 | **prompted** | 1 | 117.67 | 6.789775 | 🔵 low — common in general English |
| 8460 | **indirect** | 1 | 117.15 | 6.759922 | 🔵 low — common in general English |
| 8461 | **healthy** | 1 | 117.15 | 6.759922 | 🔵 low — common in general English |
| 8462 | **reaching** | 1 | 117.15 | 6.759922 | 🔵 low — common in general English |
| 8463 | **price** | 2 | 116.89 | 3.372545 | 🔵 low — common in general English |
| 8464 | **southeast** | 1 | 116.65 | 6.730934 | 🔵 low — common in general English |
| 8465 | **withdraw** | 1 | 116.65 | 6.730934 | 🔵 low — common in general English |
| 8466 | **maturing** | 1 | 116.16 | 6.702763 | 🔵 low — common in general English |
| 8467 | **merchandise** | 1 | 116.16 | 6.702763 | 🔵 low — common in general English |
| 8468 | **section** | 1 | 116.16 | 6.702763 | 🔵 low — common in general English |
| 8469 | **flexible** | 1 | 116.16 | 6.702763 | 🔵 low — common in general English |
| 8470 | **chances** | 1 | 115.68 | 6.675364 | 🔵 low — common in general English |
| 8471 | **chase** | 1 | 115.68 | 6.675364 | 🔵 low — common in general English |
| 8472 | **reviewing** | 1 | 115.68 | 6.675364 | 🔵 low — common in general English |
| 8473 | **uncertain** | 1 | 115.22 | 6.648696 | 🔵 low — common in general English |
| 8474 | **prospect** | 1 | 114.77 | 6.622721 | 🔵 low — common in general English |
| 8475 | **stance** | 1 | 114.77 | 6.622721 | 🔵 low — common in general English |
| 8476 | **southwest** | 1 | 114.77 | 6.622721 | 🔵 low — common in general English |
| 8477 | **northwest** | 1 | 114.77 | 6.622721 | 🔵 low — common in general English |
| 8478 | **referring** | 1 | 114.77 | 6.622721 | 🔵 low — common in general English |
| 8479 | **record** | 2 | 114.33 | 3.298792 | 🔵 low — common in general English |
| 8480 | **job** | 1 | 114.33 | 6.597403 | 🔵 low — common in general English |
| 8481 | **sum** | 1 | 114.33 | 6.597403 | 🔵 low — common in general English |
| 8482 | **fast** | 1 | 114.33 | 6.597403 | 🔵 low — common in general English |
| 8483 | **solution** | 1 | 113.90 | 6.57271 | 🔵 low — common in general English |
| 8484 | **investigation** | 1 | 113.90 | 6.57271 | 🔵 low — common in general English |
| 8485 | **promote** | 1 | 113.49 | 6.548613 | 🔵 low — common in general English |
| 8486 | **remove** | 1 | 113.49 | 6.548613 | 🔵 low — common in general English |
| 8487 | **regarding** | 1 | 113.08 | 6.525082 | 🔵 low — common in general English |
| 8488 | **dealing** | 1 | 113.08 | 6.525082 | 🔵 low — common in general English |
| 8489 | **arrangement** | 1 | 112.68 | 6.502093 | 🔵 low — common in general English |
| 8490 | **creditors** | 1 | 112.68 | 6.502093 | 🔵 low — common in general English |
| 8491 | **effectively** | 1 | 112.68 | 6.502093 | 🔵 low — common in general English |
| 8492 | **dumping** | 1 | 112.29 | 6.47962 | 🔵 low — common in general English |
| 8493 | **announce** | 1 | 112.29 | 6.47962 | 🔵 low — common in general English |
| 8494 | **maintained** | 1 | 111.91 | 6.457641 | 🔵 low — common in general English |
| 8495 | **respond** | 1 | 111.91 | 6.457641 | 🔵 low — common in general English |
| 8496 | **compete** | 1 | 111.91 | 6.457641 | 🔵 low — common in general English |
| 8497 | **urges** | 1 | 111.54 | 6.436135 | 🔵 low — common in general English |
| 8498 | **widely** | 1 | 111.54 | 6.436135 | 🔵 low — common in general English |
| 8499 | **calculated** | 1 | 111.54 | 6.436135 | 🔵 low — common in general English |
| 8500 | **planted** | 1 | 111.17 | 6.415081 | 🔵 low — common in general English |
| 8501 | **strengthen** | 1 | 111.17 | 6.415081 | 🔵 low — common in general English |
| 8502 | **consistent** | 1 | 111.17 | 6.415081 | 🔵 low — common in general English |
| 8503 | **charged** | 1 | 111.17 | 6.415081 | 🔵 low — common in general English |
| 8504 | **obligations** | 1 | 111.17 | 6.415081 | 🔵 low — common in general English |
| 8505 | **incentives** | 1 | 111.17 | 6.415081 | 🔵 low — common in general English |
| 8506 | **showing** | 1 | 110.81 | 6.394462 | 🔵 low — common in general English |
| 8507 | **duties** | 1 | 110.81 | 6.394462 | 🔵 low — common in general English |
| 8508 | **increasingly** | 1 | 110.46 | 6.374259 | 🔵 low — common in general English |
| 8509 | **appreciation** | 1 | 110.46 | 6.374259 | 🔵 low — common in general English |
| 8510 | **broadly** | 1 | 110.46 | 6.374259 | 🔵 low — common in general English |
| 8511 | **apparently** | 1 | 110.12 | 6.354457 | 🔵 low — common in general English |
| 8512 | **contribution** | 1 | 110.12 | 6.354457 | 🔵 low — common in general English |
| 8513 | **concluded** | 1 | 110.12 | 6.354457 | 🔵 low — common in general English |
| 8514 | **crowns** | 1 | 110.12 | 6.354457 | 🔵 low — common in general English |
| 8515 | **housing** | 1 | 109.79 | 6.335039 | 🔵 low — common in general English |
| 8516 | **stressed** | 1 | 109.79 | 6.335039 | 🔵 low — common in general English |
| 8517 | **represented** | 1 | 109.79 | 6.335039 | 🔵 low — common in general English |
| 8518 | **relief** | 1 | 109.45 | 6.31599 | 🔵 low — common in general English |
| 8519 | **smith** | 1 | 109.45 | 6.31599 | 🔵 low — common in general English |
| 8520 | **applied** | 1 | 109.45 | 6.31599 | 🔵 low — common in general English |
| 8521 | **moderate** | 1 | 109.45 | 6.31599 | 🔵 low — common in general English |
| 8522 | **expense** | 1 | 109.45 | 6.31599 | 🔵 low — common in general English |
| 8523 | **waiting** | 1 | 109.45 | 6.31599 | 🔵 low — common in general English |
| 8524 | **affecting** | 1 | 108.81 | 6.278949 | 🔵 low — common in general English |
| 8525 | **indicate** | 1 | 108.81 | 6.278949 | 🔵 low — common in general English |
| 8526 | **uncertainty** | 1 | 108.50 | 6.260931 | 🔵 low — common in general English |
| 8527 | **mostly** | 1 | 108.50 | 6.260931 | 🔵 low — common in general English |
| 8528 | **opportunities** | 1 | 108.50 | 6.260931 | 🔵 low — common in general English |
| 8529 | **downward** | 1 | 108.50 | 6.260931 | 🔵 low — common in general English |
| 8530 | **resume** | 1 | 108.19 | 6.243231 | 🔵 low — common in general English |
| 8531 | **severe** | 1 | 108.19 | 6.243231 | 🔵 low — common in general English |
| 8532 | **traditional** | 1 | 107.60 | 6.208745 | 🔵 low — common in general English |
| 8533 | **intervene** | 1 | 107.31 | 6.191938 | 🔵 low — common in general English |
| 8534 | **gap** | 1 | 106.46 | 6.143148 | 🔵 low — common in general English |
| 8535 | **trader** | 1 | 106.46 | 6.143148 | 🔵 low — common in general English |
| 8536 | **medium** | 1 | 106.19 | 6.127399 | 🔵 low — common in general English |
| 8537 | **suggested** | 1 | 106.19 | 6.127399 | 🔵 low — common in general English |
| 8538 | **ups** | 1 | 105.92 | 6.111895 | 🔵 low — common in general English |
| 8539 | **subordinated** | 1 | 105.92 | 6.111895 | 🔵 low — common in general English |
| 8540 | **miles** | 1 | 105.92 | 6.111895 | 🔵 low — common in general English |
| 8541 | **buyer** | 1 | 105.92 | 6.111895 | 🔵 low — common in general English |
| 8542 | **determine** | 1 | 105.92 | 6.111895 | 🔵 low — common in general English |
| 8543 | **opposed** | 1 | 105.65 | 6.096628 | 🔵 low — common in general English |
| 8544 | **leader** | 1 | 105.65 | 6.096628 | 🔵 low — common in general English |
| 8545 | **metals** | 1 | 105.65 | 6.096628 | 🔵 low — common in general English |
| 8546 | **staff** | 1 | 105.39 | 6.08159 | 🔵 low — common in general English |
| 8547 | **stronger** | 1 | 105.14 | 6.066775 | 🔵 low — common in general English |
| 8548 | **fair** | 1 | 105.14 | 6.066775 | 🔵 low — common in general English |
| 8549 | **projects** | 1 | 104.88 | 6.052176 | 🔵 low — common in general English |
| 8550 | **commitment** | 1 | 104.63 | 6.037787 | 🔵 low — common in general English |
| 8551 | **possibly** | 1 | 104.63 | 6.037787 | 🔵 low — common in general English |
| 8552 | **original** | 1 | 104.63 | 6.037787 | 🔵 low — common in general English |
| 8553 | **statements** | 1 | 104.39 | 6.023602 | 🔵 low — common in general English |
| 8554 | **underlying** | 1 | 103.67 | 5.982217 | 🔵 low — common in general English |
| 8555 | **alternative** | 1 | 103.67 | 5.982217 | 🔵 low — common in general English |
| 8556 | **represents** | 1 | 103.67 | 5.982217 | 🔵 low — common in general English |
| 8557 | **restrictions** | 1 | 103.44 | 5.968794 | 🔵 low — common in general English |
| 8558 | **medical** | 1 | 103.44 | 5.968794 | 🔵 low — common in general English |
| 8559 | **raw** | 1 | 103.21 | 5.955549 | 🔵 low — common in general English |
| 8560 | **labour** | 1 | 103.21 | 5.955549 | 🔵 low — common in general English |
| 8561 | **vegetable** | 1 | 103.21 | 5.955549 | 🔵 low — common in general English |
| 8562 | **active** | 1 | 103.21 | 5.955549 | 🔵 low — common in general English |
| 8563 | **parties** | 1 | 102.98 | 5.942477 | 🔵 low — common in general English |
| 8564 | **profitable** | 1 | 102.76 | 5.929574 | 🔵 low — common in general English |
| 8565 | **rice** | 1 | 102.76 | 5.929574 | 🔵 low — common in general English |
| 8566 | **exceed** | 1 | 102.54 | 5.916835 | 🔵 low — common in general English |
| 8567 | **sought** | 1 | 102.54 | 5.916835 | 🔵 low — common in general English |
| 8568 | **asset** | 1 | 102.32 | 5.904256 | 🔵 low — common in general English |
| 8569 | **values** | 1 | 102.10 | 5.891833 | 🔵 low — common in general English |
| 8570 | **governor** | 1 | 102.10 | 5.891833 | 🔵 low — common in general English |
| 8571 | **acquires** | 1 | 102.10 | 5.891833 | 🔵 low — common in general English |
| 8572 | **consideration** | 1 | 102.10 | 5.891833 | 🔵 low — common in general English |
| 8573 | **block** | 1 | 102.10 | 5.891833 | 🔵 low — common in general English |
| 8574 | **bonds** | 1 | 101.68 | 5.867442 | 🔵 low — common in general English |
| 8575 | **purposes** | 1 | 101.68 | 5.867442 | 🔵 low — common in general English |
| 8576 | **originally** | 1 | 101.07 | 5.831935 | 🔵 low — common in general English |
| 8577 | **afternoon** | 1 | 101.07 | 5.831935 | 🔵 low — common in general English |
| 8578 | **factor** | 1 | 100.87 | 5.820374 | 🔵 low — common in general English |
| 8579 | **via** | 1 | 100.87 | 5.820374 | 🔵 low — common in general English |
| 8580 | **strategy** | 1 | 100.67 | 5.808946 | 🔵 low — common in general English |
| 8581 | **expressed** | 1 | 100.47 | 5.797646 | 🔵 low — common in general English |
| 8582 | **legal** | 1 | 100.28 | 5.786473 | 🔵 low — common in general English |
| 8583 | **remarks** | 1 | 100.28 | 5.786473 | 🔵 low — common in general English |
| 8584 | **yield** | 1 | 100.28 | 5.786473 | 🔵 low — common in general English |
| 8585 | **enterprises** | 1 | 100.09 | 5.775423 | 🔵 low — common in general English |
| 8586 | **resulted** | 1 | 100.09 | 5.775423 | 🔵 low — common in general English |
| 8587 | **associates** | 1 | 99.71 | 5.753683 | 🔵 low — common in general English |
| 8588 | **authorized** | 1 | 99.71 | 5.753683 | 🔵 low — common in general English |
| 8589 | **fuel** | 1 | 99.34 | 5.732405 | 🔵 low — common in general English |
| 8590 | **indicated** | 1 | 99.34 | 5.732405 | 🔵 low — common in general English |
| 8591 | **designed** | 1 | 99.34 | 5.732405 | 🔵 low — common in general English |
| 8592 | **projected** | 1 | 98.98 | 5.711571 | 🔵 low — common in general English |
| 8593 | **aid** | 1 | 97.77 | 5.641891 | 🔵 low — common in general English |
| 8594 | **recovery** | 1 | 97.61 | 5.632322 | 🔵 low — common in general English |
| 8595 | **representatives** | 1 | 97.61 | 5.632322 | 🔵 low — common in general English |
| 8596 | **planning** | 1 | 97.61 | 5.632322 | 🔵 low — common in general English |
| 8597 | **estate** | 1 | 97.28 | 5.613454 | 🔵 low — common in general English |
| 8598 | **crops** | 1 | 97.28 | 5.613454 | 🔵 low — common in general English |
| 8599 | **stable** | 1 | 97.12 | 5.604151 | 🔵 low — common in general English |
| 8600 | **dispute** | 1 | 96.49 | 5.567784 | 🔵 low — common in general English |
| 8601 | **minimum** | 1 | 96.18 | 5.550084 | 🔵 low — common in general English |
| 8602 | **construction** | 1 | 96.03 | 5.54135 | 🔵 low — common in general English |
| 8603 | **posted** | 1 | 95.88 | 5.532692 | 🔵 low — common in general English |
| 8604 | **failed** | 1 | 95.73 | 5.524108 | 🔵 low — common in general English |
| 8605 | **raising** | 1 | 95.73 | 5.524108 | 🔵 low — common in general English |
| 8606 | **assistance** | 1 | 95.44 | 5.507159 | 🔵 low — common in general English |
| 8607 | **believed** | 1 | 95.29 | 5.498791 | 🔵 low — common in general English |
| 8608 | **charges** | 1 | 94.17 | 5.434252 | 🔵 low — common in general English |
| 8609 | **transactions** | 1 | 93.77 | 5.411085 | 🔵 low — common in general English |
| 8610 | **properties** | 1 | 93.64 | 5.40348 | 🔵 low — common in general English |
| 8611 | **attempt** | 1 | 93.38 | 5.388443 | 🔵 low — common in general English |
| 8612 | **performance** | 1 | 93.00 | 5.366301 | 🔵 low — common in general English |
| 8613 | **plus** | 1 | 92.87 | 5.359029 | 🔵 low — common in general English |
| 8614 | **prospects** | 1 | 92.62 | 5.34464 | 🔵 low — common in general English |
| 8615 | **consumption** | 1 | 92.62 | 5.34464 | 🔵 low — common in general English |
| 8616 | **closing** | 1 | 92.38 | 5.330455 | 🔵 low — common in general English |
| 8617 | **volume** | 1 | 92.13 | 5.316469 | 🔵 low — common in general English |
| 8618 | **rejected** | 1 | 92.01 | 5.309549 | 🔵 low — common in general English |
| 8619 | **information** | 1 | 91.66 | 5.28907 | 🔵 low — common in general English |
| 8620 | **completes** | 1 | 91.43 | 5.275647 | 🔵 low — common in general English |
| 8621 | **required** | 1 | 91.20 | 5.262402 | 🔵 low — common in general English |
| 8622 | **producing** | 1 | 90.97 | 5.24933 | 🔵 low — common in general English |
| 8623 | **nearly** | 1 | 90.64 | 5.230037 | 🔵 low — common in general English |
| 8624 | **regular** | 1 | 90.53 | 5.223687 | 🔵 low — common in general English |
| 8625 | **significant** | 1 | 89.26 | 5.150484 | 🔵 low — common in general English |
| 8626 | **initial** | 1 | 89.05 | 5.138788 | 🔵 low — common in general English |
| 8627 | **interests** | 1 | 89.05 | 5.138788 | 🔵 low — common in general English |
| 8628 | **farm** | 1 | 88.85 | 5.127227 | 🔵 low — common in general English |
| 8629 | **gross** | 1 | 88.17 | 5.087785 | 🔵 low — common in general English |
| 8630 | **member** | 1 | 87.79 | 5.065927 | 🔵 low — common in general English |
| 8631 | **adding** | 1 | 87.06 | 5.023592 | 🔵 low — common in general English |
| 8632 | **figure** | 1 | 86.97 | 5.018424 | 🔵 low — common in general English |
| 8633 | **range** | 1 | 86.44 | 4.987965 | 🔵 low — common in general English |
| 8634 | **respectively** | 1 | 86.35 | 4.982977 | 🔵 low — common in general English |
| 8635 | **probably** | 1 | 86.18 | 4.973076 | 🔵 low — common in general English |
| 8636 | **areas** | 1 | 86.01 | 4.963272 | 🔵 low — common in general English |
| 8637 | **crop** | 1 | 85.84 | 4.953564 | 🔵 low — common in general English |
| 8638 | **negotiations** | 1 | 85.68 | 4.943948 | 🔵 low — common in general English |
| 8639 | **letter** | 1 | 85.59 | 4.939175 | 🔵 low — common in general English |
| 8640 | **area** | 1 | 85.27 | 4.920306 | 🔵 low — common in general English |
| 8641 | **selling** | 1 | 84.09 | 4.85256 | 🔵 low — common in general English |
| 8642 | **chief** | 1 | 82.64 | 4.768829 | 🔵 low — common in general English |
| 8643 | **buying** | 1 | 82.50 | 4.760829 | 🔵 low — common in general English |
| 8644 | **despite** | 1 | 81.50 | 4.702786 | 🔵 low — common in general English |
| 8645 | **account** | 1 | 81.50 | 4.702786 | 🔵 low — common in general English |
| 8646 | **profits** | 1 | 80.24 | 4.630291 | 🔵 low — common in general English |
| 8647 | **available** | 1 | 79.59 | 4.59255 | 🔵 low — common in general English |
| 8648 | **secretary** | 1 | 79.24 | 4.57255 | 🔵 low — common in general English |
| 8649 | **loan** | 1 | 77.35 | 4.463236 | 🔵 low — common in general English |
| 8650 | **public** | 1 | 76.25 | 4.400178 | 🔵 low — common in general English |
| 8651 | **bought** | 1 | 74.65 | 4.307397 | 🔵 low — common in general English |
| 8652 | **supply** | 1 | 74.43 | 4.294818 | 🔵 low — common in general English |
| 8653 | **sees** | 1 | 73.42 | 4.236549 | 🔵 low — common in general English |
| 8654 | **outstanding** | 1 | 70.91 | 4.091877 | 🔵 low — common in general English |
| 8655 | **yesterday** | 1 | 70.42 | 4.063706 | 🔵 low — common in general English |
| 8656 | **trading** | 1 | 70.35 | 4.059746 | 🔵 low — common in general English |
| 8657 | **capital** | 1 | 69.49 | 4.009639 | 🔵 low — common in general English |
| 8658 | **assets** | 1 | 68.88 | 3.974548 | 🔵 low — common in general English |
| 8659 | **officials** | 1 | 68.63 | 3.960133 | 🔵 low — common in general English |
| 8660 | **industry** | 1 | 67.84 | 3.914671 | 🔵 low — common in general English |
| 8661 | **production** | 1 | 65.08 | 3.755405 | 🔵 low — common in general English |
| 8662 | **tax** | 1 | 65.00 | 3.751041 | 🔵 low — common in general English |
| 8663 | **rose** | 1 | 63.77 | 3.679632 | 🔵 low — common in general English |
| 8664 | **agreed** | 1 | 63.74 | 3.678282 | 🔵 low — common in general English |
| 8665 | **foreign** | 1 | 63.35 | 3.655599 | 🔵 low — common in general English |
| 8666 | **quarter** | 1 | 61.88 | 3.570899 | 🔵 low — common in general English |
| 8667 | **government** | 1 | 60.98 | 3.518939 | 🔵 low — common in general English |
| 8668 | **expected** | 1 | 58.67 | 3.385552 | 🔵 low — common in general English |
| 8669 | **exchange** | 1 | 58.64 | 3.38354 | 🔵 low — common in general English |
| 8670 | **agreement** | 1 | 58.50 | 3.375532 | 🔵 low — common in general English |
| 8671 | **prices** | 1 | 58.41 | 3.370559 | 🔵 low — common in general English |
| 8672 | **stock** | 1 | 52.87 | 3.050663 | 🔵 low — common in general English |
| 8673 | **net** | 1 | 40.18 | 2.318656 | ⚪ very low — function / universal word |

---

*Corpus reference: Reuters-21578 (10,788 newswire documents) via NLTK · sklearn TfidfVectorizer(smooth\_idf=True, lowercase=True).*  
*Generated 2026-08-03 by `generate_termbase.py`.*
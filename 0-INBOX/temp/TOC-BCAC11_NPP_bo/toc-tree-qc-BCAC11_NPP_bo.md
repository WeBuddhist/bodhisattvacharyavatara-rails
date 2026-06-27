---
source: BCAC11_NPP_bo
skill: toc-candidate-extraction
stage: toc-tree-qc
date: 2026-06-27
model: gemini-flash-latest
repaired: true
issues_before: 7
issues_after: 7
---

# TOC tree QC report

## Issues found (before repair)

- L41: Tibetan ordinal = 1 but decimal last segment = 13  ->  13 དང་པོ་སྦྱིན་པའི་ཕ་རོལ་ཏུ་ཕྱིན་པའི་དབང་དུ
- L46: Tibetan ordinal = 1 but decimal last segment = 4  ->  14.4 དང་པོ་ཤེས་བཞིན་མ་ཡིན་པའི་ཉེ་བའི་ཉོན་མོངས
- L63: Tibetan ordinal = 3 but decimal last segment = 1  ->  23.1.1 གསུམ་པས་ནི་ངོ་བོ་ཉིད་
- L64: Tibetan ordinal = 4 but decimal last segment = 2  ->  23.1.2 བཞི་པས་ནི་བྱེད་པ་
- L99: Tibetan ordinal = 1 but decimal last segment = 31  ->  31 དང་པོ་
- L102: Tibetan ordinal = 2 but decimal last segment = 32  ->  32 གཉིས་པ་འཇིག་རྟེན་པའི་ཆོས་བརྒྱད་ལ་ཆགས་པ་ས
- L103: Tibetan ordinal = 2 but decimal last segment = 1  ->  32.1 གཉིས་པས་ནི་ཤི་ནས་ཞག་བདུན་ལོན་པའི་དབང་དུ་

## Issues remaining after repair

- L41: Tibetan ordinal = 1 but decimal last segment = 13  ->  13 དང་པོ་སྦྱིན་པའི་ཕ་རོལ་ཏུ་ཕྱིན་པའི་དབང་དུ
- L46: Tibetan ordinal = 1 but decimal last segment = 4  ->  14.4 དང་པོ་ཤེས་བཞིན་མ་ཡིན་པའི་ཉེ་བའི་ཉོན་མོངས
- L63: Tibetan ordinal = 3 but decimal last segment = 1  ->  23.1.1 གསུམ་པས་ནི་ངོ་བོ་ཉིད་
- L64: Tibetan ordinal = 4 but decimal last segment = 2  ->  23.1.2 བཞི་པས་ནི་བྱེད་པ་
- L99: Tibetan ordinal = 1 but decimal last segment = 31  ->  31 དང་པོ་
- L102: Tibetan ordinal = 2 but decimal last segment = 32  ->  32 གཉིས་པ་འཇིག་རྟེན་པའི་ཆོས་བརྒྱད་ལ་ཆགས་པ་ས
- L103: Tibetan ordinal = 2 but decimal last segment = 1  ->  32.1 གཉིས་པས་ནི་ཤི་ནས་ཞག་བདུན་ལོན་པའི་དབང་དུ་

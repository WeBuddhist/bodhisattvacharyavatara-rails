---
source: BCAC14_GDR_bo
skill: toc-candidate-extraction
stage: toc-tree-qc
date: 2026-06-26
model: gemini-flash-latest
repaired: true
issues_before: 17
issues_after: 55
---

# TOC tree QC report

## Issues found (before repair)

- L272: indent 39 spaces != expected 36 for depth 13 (1.3.2.2.2.2.1.1.1.4.2.3.3)
- L429: ordinal 2 (གཉིས་པ) not attested for this title in candidates/enumerations (source attaches: 4)  ->  1.3.2.2.2.2.2.2.2.1.1.4.2 གཉིས་པ་མཇུག་བསྡུ་བ་
- L443: duplicate decimal 1.3.2.2.2.2.1.1.1.4.2.1.1.1 (also at L113)
- L445: indent 42 spaces != expected 39 for depth 14 (1.3.2.2.2.2.1.1.1.4.2.1.1.2)
- L445: duplicate decimal 1.3.2.2.2.2.1.1.1.4.2.1.1.2 (also at L114)
- L463: duplicate decimal 1.3.2.2.2.2.1.1.1.4.2.1.1.2 (also at L114)
- L464: duplicate decimal 1.3.2.2.2.2.1.1.1.4.2.1.1.3 (also at L115)
- L589: ordinal 2 (གཉིས་པ) not attested for this title in candidates/enumerations (source attaches: 4)  ->  1.3.2.2.2.2.2.3.3.1.2.1.2.4.5.2 གཉིས་པ་དབེན་པ་བསྟེན་པའི་ཕན་ཡོན་
- L673: ordinal 1 (དང་པོ) not attested for this title in candidates/enumerations (source attaches: 2)  ->  1.3.2.2.2.2.2.3.3.1.3.2.1.1 དང་པོ་བདག་གཞན་བརྗེ་བའི་ཚུལ་
- L702: ordinal 1 (དང་པོ) not attested for this title in candidates/enumerations (source attaches: 2)  ->  1.3.2.2.2.2.2.3.3.1.3.2.2.1.2.1 དང་པོ་བདག་གཞན་བརྗེ་བའི་ཚུལ་
- L949: indent 45 spaces != expected 39 for depth 14 (1.3.2.2.2.2.2.3.4.1.2.2.2.1)
- L950: indent 45 spaces != expected 39 for depth 14 (1.3.2.2.2.2.2.3.4.1.2.2.2.2)
- L951: indent 45 spaces != expected 39 for depth 14 (1.3.2.2.2.2.2.3.4.1.2.2.2.3)
- L952: indent 45 spaces != expected 39 for depth 14 (1.3.2.2.2.2.2.3.4.1.2.2.2.4)
- L953: indent 45 spaces != expected 39 for depth 14 (1.3.2.2.2.2.2.3.4.1.2.2.2.5)
- L967: Tibetan ordinal = 4 but decimal last segment = 2  ->  2 བཞི་པ་མཇུག་གི་དོན་
- children of 1.3.2.2.2.2.1.1.1.4.2.1.1: numbered [1, 1, 2, 2, 2, 3, 3, 4], expected [1, 2, 3, 4, 5, 6, 7, 8]

## Issues remaining after repair

- L34: indent 30 spaces != expected 39 for depth 14 (1.3.2.2.2.2.1.1.1.4.2.1.1.3)
- L54: indent 33 spaces != expected 39 for depth 14 (1.3.2.2.2.2.1.1.1.4.2.1.1.2)
- L55: indent 33 spaces != expected 39 for depth 14 (1.3.2.2.2.2.1.1.1.4.2.1.1.3)
- L55: duplicate decimal 1.3.2.2.2.2.1.1.1.4.2.1.1.3 (also at L34)
- L114: duplicate decimal 1.3.2.2.2.2.1.1.1.4.2.1.1.2 (also at L54)
- L115: duplicate decimal 1.3.2.2.2.2.1.1.1.4.2.1.1.3 (also at L34)
- L150: indent 39 spaces != expected 36 for depth 13 (1.3.2.2.2.2.2.1.1.2.4.1.2)
- L175: indent 39 spaces != expected 42 for depth 15 (1.3.2.2.2.2.2.1.2.1.1.5.1.2.2)
- L272: indent 39 spaces != expected 36 for depth 13 (1.3.2.2.2.2.1.1.1.4.2.3.3)
- L429: ordinal 2 (གཉིས་པ) not attested for this title in candidates/enumerations (source attaches: 4)  ->  1.3.2.2.2.2.2.2.2.1.1.4.2 གཉིས་པ་མཇུག་བསྡུ་བ་
- L491: ordinal 2 (གཉིས་པ) not attested for this title in candidates/enumerations (source attaches: 3)  ->  1.3.2.2.2.2.2.3.1.1.2.1.4.2.1.1.3.3.2 གཉིས་པ་རྩོད་པ་སྤང་བ་
- L607: indent 30 spaces != expected 33 for depth 12 (1.3.2.2.2.2.2.3.1.1.2.2)
- L608: indent 33 spaces != expected 36 for depth 13 (1.3.2.2.2.2.2.3.1.1.2.2.1)
- L609: indent 33 spaces != expected 36 for depth 13 (1.3.2.2.2.2.2.3.1.1.2.2.2)
- L610: indent 36 spaces != expected 39 for depth 14 (1.3.2.2.2.2.2.3.1.1.2.2.2.1)
- L611: indent 39 spaces != expected 42 for depth 15 (1.3.2.2.2.2.2.3.1.1.2.2.2.1.1)
- L612: indent 39 spaces != expected 42 for depth 15 (1.3.2.2.2.2.2.3.1.1.2.2.2.1.2)
- L613: indent 36 spaces != expected 39 for depth 14 (1.3.2.2.2.2.2.3.1.1.2.2.2.2)
- L614: indent 33 spaces != expected 36 for depth 13 (1.3.2.2.2.2.2.3.1.1.2.2.3)
- L615: indent 36 spaces != expected 39 for depth 14 (1.3.2.2.2.2.2.3.1.1.2.2.3.1)
- L616: indent 36 spaces != expected 39 for depth 14 (1.3.2.2.2.2.2.3.1.1.2.2.3.2)
- L617: indent 36 spaces != expected 39 for depth 14 (1.3.2.2.2.2.2.3.1.1.2.2.3.3)
- L707: indent 45 spaces != expected 39 for depth 14 (1.3.2.2.2.2.2.3.2.1.2.2.2.2)
- L708: indent 48 spaces != expected 42 for depth 15 (1.3.2.2.2.2.2.3.2.1.2.2.2.2.1)
- L709: indent 48 spaces != expected 42 for depth 15 (1.3.2.2.2.2.2.3.2.1.2.2.2.2.2)
- L710: indent 48 spaces != expected 42 for depth 15 (1.3.2.2.2.2.2.3.2.1.2.2.2.2.3)
- L711: indent 42 spaces != expected 39 for depth 14 (1.3.2.2.2.2.2.3.2.1.2.2.1.3)
- L712: indent 45 spaces != expected 42 for depth 15 (1.3.2.2.2.2.2.3.2.1.2.2.1.3.1)
- L713: indent 45 spaces != expected 42 for depth 15 (1.3.2.2.2.2.2.3.2.1.2.2.1.3.2)
- L714: indent 45 spaces != expected 42 for depth 15 (1.3.2.2.2.2.2.3.2.1.2.2.1.3.3)
- L715: indent 42 spaces != expected 39 for depth 14 (1.3.2.2.2.2.2.3.2.1.2.2.1.4)
- L716: indent 45 spaces != expected 42 for depth 15 (1.3.2.2.2.2.2.3.2.1.2.2.1.4.1)
- L717: indent 45 spaces != expected 42 for depth 15 (1.3.2.2.2.2.2.3.2.1.2.2.1.4.2)
- L718: duplicate decimal 1.3.2.2.2.2.2.3.2.1.2.2 (also at L667)
- L719: indent 36 spaces != expected 39 for depth 14 (1.3.2.2.2.2.2.3.2.1.2.2.2.1)
- L720: indent 36 spaces != expected 39 for depth 14 (1.3.2.2.2.2.2.3.2.1.2.2.2.2)
- L720: duplicate decimal 1.3.2.2.2.2.2.3.2.1.2.2.2.2 (also at L707)
- L721: indent 36 spaces != expected 39 for depth 14 (1.3.2.2.2.2.2.3.2.1.2.2.2.3)
- L722: indent 36 spaces != expected 39 for depth 14 (1.3.2.2.2.2.2.3.2.1.2.2.2.4)
- L723: indent 36 spaces != expected 39 for depth 14 (1.3.2.2.2.2.2.3.2.1.2.2.2.5)
- L724: indent 33 spaces != expected 36 for depth 13 (1.3.2.2.2.2.2.3.2.1.2.2.3)
- L725: indent 36 spaces != expected 39 for depth 14 (1.3.2.2.2.2.2.3.2.1.2.2.3.1)
- L726: indent 39 spaces != expected 42 for depth 15 (1.3.2.2.2.2.2.3.2.1.2.2.3.1.1)
- L727: indent 39 spaces != expected 42 for depth 15 (1.3.2.2.2.2.2.3.2.1.2.2.3.1.2)
- L728: indent 36 spaces != expected 39 for depth 14 (1.3.2.2.2.2.2.3.2.1.2.2.3.2)
- L780: ordinal 2 (གཉིས་པ) not attested for this title in candidates/enumerations (source attaches: 4)  ->  1.3.2.2.2.2.2.3.3.1.2.1.2.4.5.2 གཉིས་པ་དབེན་པ་བསྟེན་པའི་ཕན་ཡོན་
- L866: ordinal 1 (དང་པོ) not attested for this title in candidates/enumerations (source attaches: 2)  ->  1.3.2.2.2.2.2.3.3.1.3.2.1.1 དང་པོ་བདག་གཞན་བརྗེ་བའི་ཚུལ་
- L895: ordinal 1 (དང་པོ) not attested for this title in candidates/enumerations (source attaches: 2)  ->  1.3.2.2.2.2.2.3.3.1.3.2.2.1.2.1 དང་པོ་བདག་གཞན་བརྗེ་བའི་ཚུལ་
- children of 1.3.2.2.2.2.1.1.1.4.2.1.1: numbered [1, 2, 2, 3, 3, 3, 4], expected [1, 2, 3, 4, 5, 6, 7]
- children of 1.3.2.2.2.1.1.2.3.2.1: numbered [1, 4], expected [1, 2]
- children of 1.3.2.2.2.2.2.1.1.2.4.1: numbered [2], expected [1]
- children of 1.3.2.2.2.2.2.1.2.1.1.5.1.2: numbered [2], expected [1]
- children of 1.3.2.2.2.2.2.3.2.1.2: numbered [1, 2, 2], expected [1, 2, 3]
- children of 1.3.2.2.2.2.2.3.2.1.2.2: numbered [1, 3], expected [1, 2]
- children of 1.3.2.2.2.2.2.3.2.1.2.2.2: numbered [1, 2, 2, 3, 4, 5], expected [1, 2, 3, 4, 5, 6]

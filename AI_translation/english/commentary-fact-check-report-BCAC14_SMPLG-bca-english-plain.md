# BCA Translation — Commentary Fact-Check

- **Commentary (ground truth):** `1-SOURCES/commentaries/Transcluded/BCAC14_SMPLG_bo_segmented.md`
- **Translation audited:** `AI_translation/english/bca-english-plain.md`

Method: strict term-by-term alignment against the commentary's own glosses
(kāya/entity/number/simile/agent/order sensitive), not a gist check. Preliminary
self-check, not a scholarly sign-off — a domain specialist reviews before this is
treated as final (an LLM never marks its own output complete).

## Progress

| Scope checked |
|---|
| Chapter 1 (verses 1–36) |
| Chapter 2 (verses 1–65) |
| Chapter 3 (verses 1–33) |
| Chapter 4 (verses 1–48) |
| Chapter 5 (verses 1–109) |
| Chapter 6 (verses 1–134) |
| Chapter 7 (verses 1–75) |
| Chapter 8 (verses 1–185) |
| Chapter 9 (verses 1–167) |
| Chapter 10 (verses 1–58) |

## Notes on extraction

Same quatrain-per-block re-extraction as the NTS pass (see the companion
report `commentary-fact-check-report-BCAC14_NTS-bca-english-plain.md` for
detail). SMPLG's transclusion markers align 1:1 with the translation's
verse numbering; unlike NTS, none of chapter 1's 36 buckets were empty, so
no forward-merging was needed. SMPLG is considerably more verbose than
NTS — several buckets (notably verse 5, ~12,000 characters) carry long
scholastic digressions on bodhicitta typology that aren't tied to specific
words in that verse; these were treated as elaboration per the skill's
guidance and not scanned word-for-word against the translation.

### Chapter 1 — verses 1–36

| Verse | Verdict | Tibetan (Wylie) | Commentary gloss | English | Fix |
|---|---|---|---|---|---|
| 1-5 | ⚠ ERROR | གློ་བུར་དུ་གློག་འགྱུ་བའི་འོད་ཀྱིས་...རབ་ཏུ་སྣང་བའི་དངོས་པོ་ཅུང་ཟད་སྟོན་པ (the lightning's light momentarily reveals a small amount of **objects/things**, dngos po) | lightning reveals **objects**, not the night itself | "a flash of lightning briefly illuminates a dark, cloudy night" | wrong simile tenor — same finding as the NTS pass, independently confirmed: SMPLG glosses the revealed object as *dngos po* (things/objects), not the night/sky. Restore "reveals objects/forms" |
| 1-14 | ⚠ ERROR | བྱམས་མགོན་...ཚོང་དཔོན་གྱི་བུ་གཞོན་ནུ་ནོར་བཟང་...བཤད་དེ (Maitreya taught **Sudhana**, the young merchant's son, by name) | Maitreya taught the Dharma **to Sudhana** (a named bodhisattva in the Gaṇḍavyūha) | "explained by Maitreya, the wise and excellent one" | dropped named entity — same finding as NTS, independently confirmed: SMPLG names Sudhana explicitly as the addressee. Translation drops him and misapplies "excellent" (bzang) as an epithet of Maitreya instead |
| 1-20 | ⚠ ERROR | ཐེག་པ་དམན་པ་ལ་མོས་པའི་སེམས་ཅན་རྣམས་ཐེག་ཆེན་ལ་སྤྲོ་བ་བསྐྱེད་པའི་དོན་གྱིར (for the sake of inspiring beings **inclined toward the Lesser Vehicle** toward the Great Vehicle) | beings inclined to Hīnayāna (doctrinal capacity classification) | "for the benefit of humble beings" | precise term → wrong referent — same finding as NTS, independently confirmed |

**Result: 33/36 clean, 3 errors (all independently confirmed by both commentaries), 0 new findings unique to SMPLG.**

Second pass (kāya/dharma/mind swaps, wrong named entity, wrong number/scope)
did not surface additional errors in chapter 1 beyond the three above.
Kāya terms (v.10 rgyal ba'i sku → "buddha's body"; v.36 sku → "body"),
similes (v.12 chu shing → "plantain"; v.13 dpa' bo → "hero"), numbers
(v.8/33 brgya phrag → "hundreds"; v.32 nyin phyed → "half a day"), and
other named entities (Bhadrapāla v.20, Brahmā v.23) are all rendered
correctly and consistently between the two commentaries.

### Chapter 2 — verses 1–65

No errors found. SMPLG independently confirms the same named-entity set as
NTS for the offering (v.13) and refuge (v.22, v.49–52) passages —
Samantabhadra, Mañjuśrī, Avalokiteśvara, Ākāśagarbha, Kṣitigarbha,
Vajrapāṇi — all correctly named, right order. No kāya/dharma/mind swaps,
number mismatches, or simile-tenor errors found.

**Result: 65/65 clean, 0 errors.**

### Chapter 3 — verses 1–33

No errors found. SMPLG independently confirms the NTS pass — rejoicing,
request, dedication, self-gift-giving, and wish-list similes all check
cleanly. No kāya/dharma/mind swaps, number mismatches, wrong entities, or
simile-tenor errors found.

**Result: 33/33 clean, 0 errors.**

### Chapter 4 — verses 1–48

No errors found. SMPLG independently confirms the NTS pass throughout the
perseverance, cost-of-abandoning-bodhicitta, rarity, and kleśa-as-enemy
sections. No kāya/dharma/mind swaps, number mismatches, wrong entities, or
simile-tenor errors found.

**Result: 48/48 clean, 0 errors.**

### Chapter 5 — verses 1–109

No errors found. SMPLG independently confirms the NTS pass throughout the
guarding-the-mind teachings, deportment rules, and closing recommended-texts
list. The three-way almsgiving distribution at v.85 (those who have fallen /
the helpless / discipline-observers) is correctly and fully rendered in the
raw translation file. No kāya/dharma/mind swaps, number mismatches, wrong
entities, or simile-tenor errors found.

**Result: 109/109 clean, 0 errors.**

### Chapter 6 — verses 1–134

No errors found. SMPLG independently confirms the NTS pass on the patience
chapter's core arguments — the anti-anger opening, the dependent-origination
refutation of an independent agent, the weapon/body suffering-cause analysis,
the enemies-as-bodhisattva-companions and sentient-beings-equal-to-buddhas
arguments, and the closing dedication. No kāya/dharma/mind swaps, number
mismatches, wrong entities, or simile-tenor errors found.

**Result: 134/134 clean, 0 errors.**

### Chapter 7 — verses 1–75

No errors found. SMPLG independently confirms the NTS pass on the diligence
chapter — indolence taxonomy, death-imminence exhortations, the four powers,
the confidence threefold, the arrogance-vs-confidence distinction, and the
closing mastery similes. No kāya/dharma/mind swaps, number mismatches, wrong
entities, or simile-tenor errors found.

**Result: 75/75 clean, 0 errors.**

### Chapter 8 — verses 1–185

No errors found. SMPLG independently confirms the NTS pass on the
meditation chapter throughout: the solitude/mental-quiescence opening,
the foolish-people taxonomy, the forest-solitude praise and charnel-ground
imagery, the extensive impure-body meditation (flesh-mud, sandalwood/
vulture-food, saliva/excrement, insentient-flesh arguments), the
danger-of-desire section (merchant/messenger narrative, weapon/poison/
fire/precipice/enemy comparison), the self/other equality proof (hand-and-
body-part analogy, shared-desire-for-happiness logic), and the extended
self/other exchange section (Avalokiteśvara's name-recitation story,
old-self/new-self contemplative technique, envy/rivalry/pride turned
against self-cherishing, body-as-tool conclusion, closing exhortation to
meditative absorption). SMPLG's verbose scholastic digressions (e.g. the
"four carriers" and "old self" passages) were treated as elaboration per
the skill's guidance and not scanned word-for-word. No kāya/dharma/mind
swaps, number mismatches, wrong entities, or simile-tenor errors found.

**Result: 185/185 clean, 0 errors.**

### Chapter 9 — verses 1–167

No errors found. SMPLG independently confirms the NTS pass on the wisdom
chapter throughout: the two-truths framework, the Cittamātra debate, the
Śrāvaka objections on illusion-like beings and karma, the Mahāyāna
scriptural-authority debate, the meaning and fruit of emptiness, the
extended selflessness-of-persons analysis (body dissection, aggregates),
the refutation of Īśvara/puruṣa/pradhāna/paramāṇu, and the closing
compassion/saṃsāra-fault/dedication passage. SMPLG is markedly more
verbose than NTS in this chapter (several buckets carry extensive
scholastic digressions, one verse-9-77 bucket alone over 6,700 characters,
and the final verse's commentary over 11,000) — these were treated as
elaboration per the skill's guidance and not scanned word-for-word beyond
confirming no named entity, number, kāya-term, or simile-tenor mismatch
against the root verse. No kāya/dharma/mind swaps, number mismatches,
wrong entities, or simile-tenor errors found.

**Result: 167/167 clean, 0 errors.**

### Chapter 10 — verses 1–58

No errors found. SMPLG independently confirms the NTS pass on the closing
dedication chapter: the hell-realm aspirations, the animal/hungry-ghost
dedications, the human dedications (including "just like Māyādevī" at
v.19, which SMPLG's commentary glosses explicitly as "mother, the great
goddess Māyā, who gave birth to the youthful son Siddhārtha" —
independently confirming the named-entity identification), the common
dedications, the saṅgha/teachings dedication, and the author's closing
personal dedication and homage to Mañjuśrī and the kalyāṇamitra. All named
entities (Vajrapāṇi, Avalokiteśvara, Mañjuśrī, Samantabhadra, Māyādevī)
correctly identified. No kāya/dharma/mind swaps, number mismatches, wrong
entities, or simile-tenor errors found.

**Result: 58/58 clean, 0 errors.**

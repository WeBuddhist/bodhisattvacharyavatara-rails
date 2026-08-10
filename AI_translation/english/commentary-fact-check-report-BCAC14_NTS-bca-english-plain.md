# BCA Translation — Commentary Fact-Check

- **Commentary (ground truth):** `1-SOURCES/commentaries/Transcluded/BCAC14_NTS_bo_segmented.md` (Ngulchu Thokme, *Ocean of Good Explanations*)
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

The translation file (`bca-english-plain.md`) is quatrain-per-block, not
line-per-block, so `extract_translation.py` (built for one-line-per-verse
"graded" files) only captured each verse's last line. Full quatrains were
re-extracted directly from the raw file for this audit. The NTS commentary's
own internal paragraph numbers (the `^1-N` trailing every block inside the
file) are **not** verse IDs — they're the commentary's sequential paragraph
count. The true root-verse alignment comes from the `![[bo-...#^1-N]]`
transclusion markers, which do match the translation's verse numbering
1–36. Ten of thirty-six transclusion markers in chapter 1 had no prose
directly after them (content absorbed into the next marker, e.g. verse 2
folds into the commentary block anchored at marker 3); these were merged
forward per the skill's standard handling and are not translation defects.

### Chapter 1 — verses 1–36

| Verse | Verdict | Tibetan (Wylie) | Commentary gloss | English | Fix |
|---|---|---|---|---|---|
| 1-5 | ⚠ ERROR | གཟུགས་རབ་ཏུ་སྣང་བ་སྟོན་པ (gzugs rab tu snang ba ston pa) | lightning momentarily reveals **forms** (gzugs) in the dark | "a flash of lightning briefly illuminates a dark, cloudy night" | wrong simile tenor: the lightning reveals *forms/objects*, not "the night" itself — restore "forms" as the object revealed |
| 1-14 | ⚠ ERROR | བྱམས་མགོན་བློ་དང་ལྡན་པས་ནོར་བཟང་བཤད (byams mgon blo dang ldan pas nor bzang bshad) | Maitreya (byams mgon) **taught Sudhana** (nor bzang, a named bodhisattva, per commentary's Gaṇḍavyūha citation) | "explained by Maitreya, the wise and excellent one" | dropped named entity: Sudhana (the recipient) is deleted, and part of his name ("bzang" = excellent) is misapplied as an epithet of Maitreya instead — should read "...explained to Sudhana" |
| 1-20 | ⚠ ERROR | ཐེག་དམན་ལ་མོས་པའི་སེམས་ཅན་ (theg dman la mos pa'i sems can) | beings **inclined toward the Lesser Vehicle** (a doctrinal capacity classification), so the Tathāgata could lead them to the Great Vehicle | "for the benefit of humble beings" | precise term → wrong referent: "humble" (a personality trait) replaces "inclined to the Hīnayāna" (a specific class of practitioner) — the group named is not the group meant |
| 1-20 | note | དེ་བཞིན་གཤེགས་པ་ཉིད (de bzhin gshegs pa nyid) — singular, "the Tathāgata himself," the speaker in the cited sūtra | one specific Buddha | "taught by the buddhas themselves" | minor number mismatch (singular → plural); flagged alongside the entity error above, not independently severe |
| 1-1 | style note | ཆོས་ཀྱི་སྐུ (chos kyi sku) glossed at length as *dharmakāya*, a buddha-body (citing the Uttaratantra's two kāyas) | dharmakāya / truth-body | "who embody the truth" | not a hard error — "embody" retains the bodily sense even though "kāya" isn't spelled out — but flagging since kāya-terms are the highest-risk class |
| 1-4 | style note | དལ་འབ�ྱོར (dal 'byor), glossed via the classical 8 unfree states + 10 endowments (18 qualities enumerated) | "leisure and endowment" (technical term for a fully qualified human rebirth) | "this opportunity" | acceptable simplification for a plain-audience translation; the doctrinal term is compressed to its gist, not misnamed |

**Result: 33/36 clean, 3 errors, 2 softening notes.**

Second pass (kāya/dharma/mind swaps, wrong named entity, wrong number/scope)
did not surface additional errors beyond the above in chapter 1. Kāya terms
elsewhere (v.10 rgyal ba'i sku → "buddha's body"; v.36 sku → "body") are
rendered correctly. Other named entities (Bhadrapāla v.20, Brahmā v.23) are
correctly identified.

### Chapter 2 — verses 1–65

No errors found. Term-by-term pass (offering list, refuge formula, confession
section) checked cleanly against NTS, including named entities — v.13
Samantabhadra/Mañjuśrī/Avalokiteśvara (kun tu bzang po / 'jam dbyangs /
'jig rten dbang phyug); v.22 Mañjuśrī ('jam dbyangs); v.49–52 Samantabhadra,
Mañjuśrī, Avalokiteśvara, Ākāśagarbha, Kṣitigarbha, Vajrapāṇi (kun tu bzang
po / 'jam pa'i dbyangs / spyan ras gzigs / nam mkha'i snying po / sa yi
snying po / rdo rje can) — all correctly named and in the commentary's
order. No kāya/dharma/mind swaps, number mismatches, or simile-tenor
errors found.

**Result: 65/65 clean, 0 errors.**

### Chapter 3 — verses 1–33

No errors found. Rejoicing, request, dedication, and self-gift-giving
(v.12–21) sections checked cleanly. Wish-list similes (island, lamp,
bridge, wish-fulfilling jewel, medicine, wish-granting tree/cow, earth
elements, etc., v.17–20) all correctly matched. No kāya/dharma/mind swaps,
number mismatches, wrong entities, or simile-tenor errors found.

**Result: 33/33 clean, 0 errors.**

### Chapter 4 — verses 1–48

No errors found. Checked the exhortation-to-persevere, cost-of-abandoning-
bodhicitta, rarity-of-freedom-and-endowment (turtle-and-yoke simile), and
kleśa-as-enemy sections. Commentary's illustrative narratives (Śāriputra's
prior bodhicitta, Suvarṇavarṇa) are elaboration not carried by the root
verse and correctly not forced into the translation. No kāya/dharma/mind
swaps, number mismatches, wrong entities, or simile-tenor errors found.

**Result: 48/48 clean, 0 errors.**

### Chapter 5 — verses 1–109

No errors found. Checked the guarding-the-mind teachings throughout: mind-elephant
similes, wild-animal/thief lists, fire-arises-from-mind and Brahmā-realm
citations, leaky-pot and thief similes, the "remain like wood" conditions list,
Mount Meru and impure-aggregates dissection meditation, deportment rules
(gaze, eating, sitting, sleeping-like-the-Protector-in-nirvana), rejoicing/
praise sequence, guru-reliance (Sudhana's biography cited), and the closing
recommended-texts list (Ākāśagarbha-sūtra, Śikṣāsamuccaya, Sūtrasamuccaya,
Nāgārjuna's two texts). The three-way almsgiving distribution at v.85
(those who have fallen / the helpless / discipline-observers, matching NTS's
log par ltung / mgon med / brtul zhugs gnas) is correctly rendered in full —
initially flagged as a possible dropped category during this audit, but the
raw translation file confirms "those who have fallen" is present as the
opening line of the quatrain (a condensed-excerpt artifact, not a translation
defect). No kāya/dharma/mind swaps, number mismatches, wrong entities, or
simile-tenor errors found.

**Result: 109/109 clean, 0 errors.**

### Chapter 6 — verses 1–134

No errors found. This is the patience chapter's core doctrinal argument —
checked closely given the density of technical points: the "hatred destroys
merit" opening, the dependent-origination refutation of an independent agent
(Sāṃkhya's *pradhāna*/*puruṣa*, v.27–33), the "weapon and body both causes of
suffering" analysis, the sword-leaf-forest/hell-guardian similes, the
rejoicing-in-enemies-as-bodhisattva-companions argument, the sentient-beings-
equal-to-buddhas-as-fields-of-merit argument, and the closing "world's servant"
dedication. No kāya/dharma/mind swaps, number mismatches, wrong entities, or
simile-tenor errors found.

**Result: 134/134 clean, 0 errors.**

### Chapter 7 — verses 1–75

No errors found. Checked the diligence chapter's key passages: the
indolence-taxonomy opening, death-imminence exhortations, the insect-attains-
awakening-through-diligence citation, the four powers (aspiration, steadfastness,
joy, relinquishment), the confidence-in-action/kleśa/capacity threefold, the
arrogance-vs-confidence distinction (spang bya'i nga rgyal vs gnyen po'i nga
rgyal), and closing mind/body mastery similes (wind and cotton, elephant and
lake). No kāya/dharma/mind swaps, number mismatches, wrong entities, or
simile-tenor errors found.

**Result: 75/75 clean, 0 errors.**

### Chapter 8 — verses 1–185

No errors found. This is the meditation (dhyāna) chapter and the largest in
the text (185 verses) — checked closely given its doctrinal density: the
solitude-and-mental-quiescence opening, the taxonomy of foolish/childish
people to avoid, the bee-gathering-nectar simile for taking only the
essential teaching, the dangers of gain/respect/fame, forest-solitude
praise (animal and tree similes, the "four carriers" verse, corpse-viewing
at charnel grounds, undisturbed recollection of the Three Jewels), the
extended meditation on the body's impurity (hair/nails/teeth, the flesh-mud
simile, the charnel-ground bone imagery, the sandalwood/vulture-food
argument, the saliva/excrement-from-one-food argument, the insentient-flesh
argument), the danger-of-desire section (the merchant/messenger narrative,
the weapon/poison/fire/precipice/enemy comparison exceeded by hell), the
transition into self/other equality (bdag gzhan mnyam pa — the
hand-and-body-part analogy, the logical proof from shared desire for
happiness and aversion to suffering, the answers to the "suffering isn't
mine to remove" objections), and the extended self/other exchange (bdag
gzhan brje ba — Avalokiteśvara's name-recitation story, the "old self" vs
"new self" contemplative technique, envy/rivalry/pride meditations turned
against self-cherishing, the body-as-tool-for-others conclusion, and the
closing exhortation to calm abiding and mind training). No kāya/dharma/mind
swaps, number mismatches, wrong named entities, or simile-tenor errors
found.

**Result: 185/185 clean, 0 errors.**

### Chapter 9 — verses 1–167

No errors found. This is the wisdom (prajñā) chapter — dense Madhyamaka
argumentation with comparatively few of the skill's highest-risk features
(named entities, numbered lists, similes with a concrete tenor) but checked
closely for kāya/dharma/mind swaps and dropped or altered technical terms
given the philosophical density. Covered: the two-truths framework and the
yogin/ordinary-person dispute, the Cittamātra debate (mind-only refutation
of external objects, the lamp/self-illumination argument, the sword-cannot-
cut-itself simile), the Śrāvaka objections and Madhyamaka replies on
illusion-like beings and karma, the scriptural-authority debate over the
Mahāyāna canon (citing Kāśyapa, the four āgamas), the meaning and fruit of
emptiness, the extended selflessness-of-persons analysis (the body
dissected part by part, the aggregates), the refutation of Īśvara/puruṣa/
pradhāna/paramāṇu as causes (the Sāṃkhya three-guṇa argument), the
tathāgatagarbha-adjacent "nature is luminosity/nirvāṇa" passage, and the
closing exhortation on compassion, saṃsāra's faults, and dedicating merit
via emptiness. Named entities present (Kāśyapa, Sāṃkhya's guṇa terms,
Īśvara) are all correctly rendered. No kāya/dharma/mind swaps, number
mismatches, wrong entities, or simile-tenor errors found.

**Result: 167/167 clean, 0 errors.**

### Chapter 10 — verses 1–58

No errors found. This is the closing dedication chapter, rich in named
entities and vivid similes — checked closely for named-entity accuracy and
simile-tenor fidelity. Covered: the general dedication, the hell-realm
aspirations (cold and hot hells becoming cool/warm, weapons becoming
flowers, the sword-leaf forest becoming sandalwood, hell-beings seeing
Vajrapāṇi, Avalokiteśvara, and Mañjuśrī and being freed), the dedication
for animals and hungry ghosts (fed by the stream of milk from
Avalokiteśvara's hand), the dedication for humans (the blind seeing, the
deaf hearing, pregnant women giving birth safely "like Māyādevī" —
correctly named as the Buddha's mother), the common dedications (long
life, fertile earth like lapis lazuli, the Dharma heard from birds and
light), the dedication for the saṅgha and the teachings, and the author's
personal dedication to Mañjuśrī (attaining the ground of Great Joy,
meeting Mañjuśrī without obstruction) closing with the homage to Mañjuśrī
and one's kalyāṇamitra. All named entities (Vajrapāṇi, Avalokiteśvara,
Mañjuśrī, Samantabhadra, Māyādevī) are correctly identified and in the
commentary's own order. No kāya/dharma/mind swaps, number mismatches,
wrong entities, or simile-tenor errors found.

**Result: 58/58 clean, 0 errors.**

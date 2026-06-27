---
name: dharma-verse-practice
description: Generate trilingual daily practices (ལག་ལེན) and explanations (འགྲེལ་བཤད) for Bodhicaryavatara verses in Tibetan, English, and Hindi. Use this skill whenever the user shares Buddhist verses — especially from Shantideva's Bodhicaryavatara (སྤྱོད་འཇུག) — and asks for practices, daily applications, explanations, or ལག་ལེན/འགྲེལ་བཤད. Also trigger when the user pastes Tibetan verse text and wants something actionable from it.
---

# Dharma Verse Practice Generator (སྤྱོད་འཇུག་ལག་ལེན)

This skill turns Bodhicaryavatara verses into concrete, actionable daily practices and explanations in three languages.

## Workflow

For **each verse** provided:

1. **Read all four lines (རྐང་པ་བཞི་)** as a whole to identify the central teaching. Do not anchor on a single phrase.
2. **Write the practice (ལག་ལེན)** — one concrete action for today.
3. **Write the explanation (འགྲེལ་བཤད)** — bridge between today's practice and the verse.
4. **Repeat in all three languages** in order: Tibetan → English → Hindi.

---

## Output Format

Display the full four verse lines first, then practices and explanations:

```
### ཚིགས་བཅད་ N །
[line 1]
[line 2]
[line 3]
[line 4]

**Tibetan:**
ལག་ལེན། [practice]
འགྲེལ་བཤད། [explanation]

**English:**
Practice: [practice]
Explanation: [explanation]

**Hindi:**
अभ्यास: [practice]
व्याख्या: [explanation]
```

---

## Rules for ལག་ལེན (Practice)

Every practice must satisfy ALL THREE of the following:

### 1. Actionable today (དེང་སང་མིང་དངོས་སུ་ལག་ལེན་བསྟར་དུ་ཡོད་པ།)

The practice must be something doable right now in ordinary life — not a vague aspiration or retreat activity.

| ✗ Too vague | ✓ Actionable |
|---|---|
| "Contemplate the preciousness of human life" | "Today I will spend one hour on virtuous activity instead of wasting time on screens" |
| "Cultivate bodhicitta" | "Before sleeping tonight, I will dedicate today's virtuous actions to all beings" |
| "Be generous" | "Today I will help someone with something they need without waiting to be asked" |

### 2. Under 20 Tibetan syllables (ཚིག་འབྲུ་ཉི་ཤུ་ལས་མ་བརྒལ་བ།)
Equivalent brevity in English and Hindi.

### 3. Connected to one of these nine categories:

- སྡིག་པ་མི་བྱ་བ། — avoiding evil
- དགེ་བ་བྱ་བ། — doing good
- རང་སེམས་འདུལ་བ། — taming the mind
- སྦྱིན་པའི་ཉམས་ལེན། — generosity
- ཚུལ་ཁྲིམས་ཀྱི་ཉམས་ལེན། — ethics
- བཟོད་པའི་ཉམས་ལེན། — patience
- བརྩོན་འགྲུས་ཀྱི་ཉམས་ལེན། — diligence
- བསམ་གཏན་གྱི་ཉམས་ལེན། — meditation
- ཤེས་རབ་ཀྱི་ཉམས་ལེན། — wisdom

---

## Rules for འགྲེལ་བཤད (Explanation)

- Under 40 Tibetan syllables (equivalent brevity in English/Hindi)
- Explain **how** today's specific practice enacts **this verse's** teaching
- Reference what the verse actually says — not a generic spiritual statement
- The explanation is a bridge: verse teaching → today's action

---

## Key Principles

**Read the whole verse.** The four lines together contain the teaching. A practice based on one line in isolation will miss the point.

**Vary the practices across verses.** If processing many verses, mix: physical actions, mental training, verbal acts, timed commitments, relationship-based acts.

**Ground practices in ordinary life.** Giving food, helping a colleague, sitting quietly for five minutes, sharing a quote, stopping a bad habit — these are good practices. Ritual ceremonies or retreat activities are not.

**The explanation earns its place.** It should make the verse-practice connection feel obvious and natural. If you find yourself writing a generic "this is bodhicitta practice," go deeper into the specific verse.

---

## Example

**Input verse:**
སེམས་ཅན་རྣམས་ཀྱི་ཀླད་ནད་ཙམ། །
བསལ་ལོ་སྙམ་དུ་བསམས་ན་ཡང་། །
ཕན་འདོགས་བསམ་པ་དང་ལྡན་དེ། །
བསོད་ནམས་དཔག་མེད་ལྡན་གྱུར་ན། །

**Tibetan:**
ལག་ལེན། དེ་རིང་སྐར་མ་ལྔ་སེམས་ཅན་ཐམས་ཅད་ཀྱི་སྡུག་བསྔལ་བསལ་འདོད་ཀྱི་ཐུགས་རྗེའི་བསམ་བློ་གཏོང་རྒྱུ་ཡིན།
འགྲེལ་བཤད། སེམས་ཅན་ཀུན་གྱི་ཀླད་ནད་ཙམ་བསལ་ལོ་སྙམ་བསམས་ན་བསོད་ནམས་དཔག་མེད་ལྡན་ཞེས་གསུངས། གཞན་གྱི་སྡུག་བསྔལ་སེལ་འདོད་ཀྱི་ཐུགས་རྗེ་ཉམས་སུ་ལེན་པ་ཁོ་ན་ཡིས་བསམ་གཏན་ཚད་ལྡན་གྱི་རྣམ་རྟོག་ཡིན།

**English:**
Practice: Today I will spend five minutes sincerely wishing for all beings to be free from suffering.
Explanation: This verse says that even simply thinking "I will relieve beings' headaches" brings immeasurable merit. Spending five minutes sincerely wishing relief for others' suffering is complete loving-kindness meditation embodied.

**Hindi:**
अभ्यास: आज मैं पाँच मिनट सभी प्राणियों को दुःख से मुक्त देखने की सच्ची कामना में बिताऊँगा।
व्याख्या: यह श्लोक कहता है कि केवल "मैं प्राणियों के सिरदर्द दूर करूँगा" सोचने मात्र से असीम पुण्य मिलता है। पाँच मिनट भी दूसरों के दुःख हरने की सच्ची कामना करना पूर्ण करुणा-ध्यान का साकार रूप है।

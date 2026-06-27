---
name: daily-challenge-creator
description: Generate one trilingual daily practice (ལག་ལེན) and explanation (འགྲེལ་བཤད) per Bodhicaryavatara verse in Tibetan, English, and Hindi. Use when the user shares one or more སྤྱོད་འཇུག verses and asks for a daily challenge, action, practice, or ལག་ལེན/འགྲེལ་བཤད.
---

# Daily Challenge Creator (ལག་ལེན་དང་འགྲེལ་བཤད།)

This skill generates one concrete daily practice and its explanation for each Bodhicaryavatara verse — in Tibetan, English, and Hindi.

---

## Workflow

For **each verse** provided:

1. **Read all four lines (རྐང་པ་བཞི་) as a whole.** Identify the central teaching of the entire verse — not just a single phrase.
2. **Write the practice (ལག་ལེན)** — one concrete action for today, grounded in ordinary life.
3. **Write the explanation (འགྲེལ་བཤད)** — bridging today's practice to this verse's teaching.
4. **Output in all three languages** in order: Tibetan → English → Hindi.

---

## Output Format

Place the verse lines first, then practices and explanations grouped as shown:

```
**ལག་ལེན།**
**Tibetan:** [practice]
**English:** [practice]
**Hindi:** [practice]

**འགྲེལ་བཤད།**
**Tibetan:** (category) [explanation]
**English:** (category) [explanation]
**Hindi:** (category) [explanation]
```

Practices and explanations for each verse appear together directly beneath that verse.

---

## Rules for ལག་ལེན (Practice)

Every practice must satisfy ALL THREE:

### 1. Actionable today (དེང་སང་མིང་དངོས་སུ་ལག་ལེན་བསྟར་དུ་ཡོད་པ།)

Must be doable in ordinary daily life right now — not a vague aspiration or retreat activity.

| ✗ Not actionable | ✓ Actionable |
|---|---|
| "དེ་རིང་མི་ལུས་རིན་ཆེན་ཐོབ་པར་དགའ་བ་སྒོམ་ཞིང་དུས་ཚོད་ཆུད་ཟོས་སུ་མི་གཏོང་རྒྱུ་ཡིན།" | "དེ་རིང་ངས་མི་དབུལ་པོ་ཞིག་ལ་ཉིན་གུང་ཁ་ལག་ཅིག་སྤྲད་རྒྱུ་ཡིན།" |
| General aspiration or reflection only | A specific, named act you can complete today |

### 2. Under 20 Tibetan syllables (ཚིག་འབྲུ་ཉི་ཤུ་ལས་མ་བརྒལ་བ།)

Equivalent brevity in English (≤ 20 words) and Hindi (≤ 20 words).

### 3. Connected to one of nine categories

Label the explanation (not the practice) with the matching category in parentheses:

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

- Under 40 Tibetan syllables (equivalent brevity in English and Hindi)
- Explain **how** today's specific practice enacts **this verse's** teaching
- Reference what the verse actually says — not a generic spiritual statement
- Open the explanation with the relevant category in parentheses (see nine categories above)
- The explanation is a bridge: verse teaching → today's action

---

## Key Principles

**Read the whole verse.** Anchor on the meaning of all four lines together, not on isolated phrases.

**Ground practices in ordinary life.** Giving food, helping someone, sitting quietly for five minutes, sharing a quote, refraining from a harmful habit — these are good practices. Ritual ceremonies or retreat activities are not.

**Vary across verses.** When processing multiple verses, mix categories: physical acts, mental training, verbal acts, timed commitments, relationship-based acts.

**The explanation earns its place.** It should make the verse–practice connection feel obvious. Avoid generic "this is bodhicitta practice" — go into the specific verse.

---

## Example

**Input verse:**
བདེ་གཤེགས་ཆོས་ཀྱི་སྐུ་མངའ་སྲས་བཅས་དང་། །
ཕྱག་འོས་ཀུན་ལའང་གུས་པར་ཕྱག་འཚལ་ཏེ། །
བདེ་གཤེགས་སྲས་ཀྱི་སྡོམ་ལ་འཇུག་པ་ནི། །
ལུང་བཞིན་མདོར་བསྡུས་ནས་ནི་བརྗོད་པར་བྱ། །

**ལག་ལེན།**
**Tibetan:** དེ་རིང་ངས་དྲ་ལམ་དུ་ནང་ཆོས་ཀྱི་ལུང་ཐུང་ངུ་ཞིག་མཉམ་སྤྱོད་བྱ་རྒྱུ་ཡིན།
**English:** I will share a short Buddhist quote on my social media today.
**Hindi:** आज मैं सोशल मीडिया पर एक संक्षिप्त बौद्ध उद्धरण साझा करूंगा।

**འགྲེལ་བཤད།**
**Tibetan:** (དགེ་བ་བྱ་བ།) ཆོས་ཀྱི་ཚིག་སྤེལ་བ་ནི་བསྟན་བཅོས་འདི་མཐོང་མཁན་གཞན་ལ་ཕན་པར་འགྱུར་བའི་སྨོན་ལམ་དང་མཐུན་པའི་དགེ་བའི་ལག་ལེན་ཡིན།
**English:** (Practicing virtue) Sharing dharma text connects others to virtue, fulfilling the author's wish that spreading these words benefits like-minded people.
**Hindi:** (पुण्य कर्म) धर्म का पाठ साझा करना दूसरों को पुण्य से जोड़ता है, जो लेखक की इच्छा को पूरा करता है।

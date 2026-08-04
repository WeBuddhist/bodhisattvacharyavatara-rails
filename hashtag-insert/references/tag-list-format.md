# Hashtag list format (real example)

Source pattern seen in this project's vault, e.g. a note named `མཚན་རྟགས། Tags.md`.

The file opens with a short intro paragraph explaining the tags are grouped into categories to make it easy to find a verse for a specific kind of difficulty. Then each category looks like this:

```markdown
### ༡. མི་དང་སྤྱི་ཚོགས་ལས་བྱུང་བའི་དཀའ་ངལ་གདོང་ལེན། (Interpersonal & Social Challenges)

གཞན་གྱིས་སྨད་ར་གཏོང་བ། རྒྱབ་བཤད་རྒྱག་པ། མགོ་སྐོར་བཏང་བ་སོགས་མི་འབྲེལ་གྱི་དཀའ་ངལ་ལ་གདོང་ལེན་བྱེད་པའི་མཚན་རྟགས།

| མཚན་རྟགས། (Tags) | གང་ལ་སྦྱར་བའི་གནས་སྐབས། (Application) |

| --- | --- |

| `#ཚིག་ངན་བཟོད་པ།` | གཞན་གྱིས་ཚིག་རྩུབ་དང་སྨད་ར་བཏང་བའི་སྐབས་སུ་བཟོད་སྲན་བྱེད་པ། |

| `#སྙན་གྲགས་ཤོར་བ་དང་ལེན།` | རང་གི་མིང་ཆད་དང་སྙན་གྲགས་ཉམས་པའི་སྐབས་སུ་སེམས་མི་འཁྲུག་པ། |
```

Notes:

- The `###` heading names the category in Tibetan with an English gloss in parentheses. `extract_tags.py` captures the whole heading text (including the gloss) as `category`.
- Immediately after the heading is a one- or two-sentence description of what kind of hardship the category covers. This isn't parsed structurally, but it's useful context to read before matching verses in that category — it tells you the intended scope.
- The table has a header row, a `--- | ---` separator row, then one row per tag. **Rows are sometimes separated by blank lines** (an artifact of how the note was authored/exported) — the parser tolerates this by matching each `| ... | ... |` row independently rather than requiring a contiguous block.
- Tags are backtick-quoted and start with `#`. The application column is the actual matching signal — read it closely; two tags in the same broad category (e.g. "enduring harsh words" vs. "not retaliating against harm") can require quite different verses even though both are nominally about patience.
- A real vault had 4 categories and ~23 tags total, covering: interpersonal/social harm, material/financial loss, physical harm & environmental hardship, and psychological/emotional struggle. The list is user-provided and may differ each time — don't assume these exact categories or counts; always re-parse the file given for the current task.

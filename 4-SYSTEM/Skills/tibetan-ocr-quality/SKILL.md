---
name: tibetan-ocr-quality
description: Calculate perplexity of a Tibetan OCR output file using KenLM and Botok normalization to assess OCR quality.
---

# tibetan-ocr-quality

Assesses the quality of a Tibetan OCR output by calculating its perplexity against a pre-trained KenLM syllable-level language model (`BoKenlm-syl-v0.4.arpa`). Lower perplexity indicates text that better matches expected Tibetan language patterns — i.e. cleaner OCR. High perplexity signals garbled or mis-recognized text. The text is normalized using Botok's `normalize_for_perplexity()` pipeline before scoring, which handles tsheg normalization, case-affix splitting, Sanskrit folding, and punctuation standardization.

---

## Inputs

| Input | Description | Path / Format |
|---|---|---|
| `input-file` | A `.txt` file containing raw Tibetan OCR output to evaluate | Any path; typically `0-INBOX/` or `1-SOURCES/` |
| `model-file` | The KenLM ARPA model file | Must be downloaded once from [HuggingFace: openpecha/BoKenlm-syl-v0.4](https://huggingface.co/openpecha/BoKenlm-syl-v0.4). Default expected location: `4-SYSTEM/models/BoKenlm-syl-v0.4.arpa` |

## Output

Results are printed to the console. No output file is written by default.

The output includes: total number of sentences, total tokens, log-probability sum, and **perplexity** (the primary quality metric).

---

## Output file format

Console output only:

```
=== Tibetan OCR Quality Report ===
File:       <input-file>
Model:      <model-file>
Sentences:  <N>
Tokens:     <N>
Log-prob:   <float>
Perplexity: <float>
================================
```

Interpretation:
- **Lower perplexity = better OCR quality.** Well-recognized Tibetan text typically scores in a predictable range for the given model.
- Extremely high perplexity (orders of magnitude above normal) signals severe OCR errors, wrong script, or corrupted text.

---

## Rules

1. **Dependencies must be installed before running.** The script requires only the `kenlm` Python package. Install with: `pip install kenlm --break-system-packages`. The Botok normalization logic is inlined in the script — no `botok` dependency needed.
2. **The ARPA model must be present on disk.** If the model file is not found at the expected path, the skill stops and tells the user to download it from `https://huggingface.co/openpecha/BoKenlm-syl-v0.4`.
3. **Normalization uses the inlined `normalize_for_perplexity()`.** The function is ported from Botok's `corpus_normalization.py` (Apache-2.0) to ensure consistency with the model's training tokenization, without requiring botok as a runtime dependency.
4. **Do not modify the input file.** This is a read-only quality check.
5. **Empty files or files with no Tibetan content must be reported, not scored.** If normalization produces zero tokens, report an error rather than dividing by zero.

---

## Procedure

1. **Check dependencies.** Verify `kenlm` is importable. If not, install it:
   ```
   pip install kenlm --break-system-packages
   ```

2. **Locate the model file.** Check the path provided by the user, or the default `4-SYSTEM/models/BoKenlm-syl-v0.4.arpa`. If not found, stop and instruct the user to download it:
   ```
   # From https://huggingface.co/openpecha/BoKenlm-syl-v0.4
   # Download BoKenlm-syl-v0.4.arpa and place in 4-SYSTEM/models/
   ```

3. **Run the scoring script.** Execute `4-SYSTEM/Skills/tibetan-ocr-quality/scripts/score_ocr.py`:
   ```
   python 4-SYSTEM/Skills/tibetan-ocr-quality/scripts/score_ocr.py <input-file> [--model <model-path>]
   ```

4. **Report the result.** Present the perplexity score and a brief interpretation to the user.

---

## Completion check

- [ ] `kenlm` is installed and importable
- [ ] Model file exists at the specified path
- [ ] Script ran without errors on the input file
- [ ] Perplexity score was reported to the user

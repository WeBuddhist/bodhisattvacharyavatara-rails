#!/usr/bin/env python3
"""System-level chrF of the English versions against the human English translations.

  python3 reports/chrf_systems.py      (from kf-pilot)  -> reports/chrf-systems-bodhicaryavatara.json

Segments: those of the first English academic fact-check (factcheck/academic-a1). References: Padmakara, Wallace,
Choephel, aligned to the Tibetan verse ids by factcheck/improvement.py (aligned_reference). chrF as in
improvement.py (character 6-grams, beta 2, corpus level), over the segments that both system and reference have.
"""
import json
import pathlib
import sys

KF = pathlib.Path(__file__).resolve().parents[1]
sys.argv = sys.argv[:1]
sys.path.insert(0, str(KF / "factcheck"))
import improvement as im  # noqa: E402
from segment_context import blocks  # noqa: E402

SYSTEMS = [("DharmaMitra zero-shot", "3-TRANSFORMATIONS/Translations/Dharmamitra/en/bo-བློ་ལྡན་ཤེས་རབ།-en.md"),
           ("Gemini zero-shot", "3-TRANSFORMATIONS/Translations/Gemini/en/bo-བློ་ལྡན་ཤེས་རབ།-en.md"),
           ("Old Rails scholar", "3-TRANSFORMATIONS/Translations/en-translate/BCA-Full-Scholar-English.md"),
           ("Academic final", "3-TRANSFORMATIONS/Translations/en-academic/bo-བློ་ལྡན་ཤེས་རབ།-en.md")]


def main():
    refs = im.references("en-academic")
    ids = [s["id"] for s in json.loads((KF / "factcheck/academic-a1/verdicts.json").read_text(encoding="utf-8"))]
    out = {}
    for name, path in SYSTEMS:
        h = blocks(path)
        row = {}
        for rn, r in refs:
            common = [i for i in ids if h.get(i) and r.get(i)]
            row[rn] = im.chrf([h[i] for i in common], [r[i] for i in common])
        out[name] = row
        print(name, row, "mean", round(sum(row.values()) / len(row), 2))
    (KF / "reports/chrf-systems-bodhicaryavatara.json").write_text(json.dumps(out, indent=1, ensure_ascii=False),
                                                                    encoding="utf-8")


if __name__ == "__main__":
    main()

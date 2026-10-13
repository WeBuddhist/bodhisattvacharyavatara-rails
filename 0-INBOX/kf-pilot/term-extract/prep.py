#!/usr/bin/env python3
"""Build the per-segment input for term extraction and split it into agent batches.

  python3 prep.py --root 1-SOURCES/Translations/bo-བློ་ལྡན་ཤེས་རབ།.md \
      --baseline dm=3-TRANSFORMATIONS/Translations/Dharmamitra/en/bo-བློ་ལྡན་ཤེས་རབ།-en.md \
      --baseline gm=3-TRANSFORMATIONS/Translations/Gemini/en/bo-བློ་ལྡན་ཤེས་རབ།-en.md \
      --out 0-INBOX/kf-pilot/term-extract/bodhicaryavatara-en

Paths are relative to the vault root. Writes <out>/segments.json
([{id, heading, bo, <label>: text, ...}]) and <out>/batches/batch-NN.json.
Batches never exceed --max-batch segments and break at section boundaries
where they can (a section larger than the cap is split evenly).
"""
import argparse
import json
import math
import pathlib
import re

VAULT = pathlib.Path(__file__).resolve().parents[3]
MARK = re.compile(r"\s*\^([0-9A-Za-z]+(?:-[0-9A-Za-z]+)*)\s*$")  # BCA has I-1, 1-a, a-1, b-1
PLACEHOLDER = "*[not yet translated]*"  # partial render of a machine-translate ledger


def body(text):
    if text.startswith("---"):
        end = text.find("\n---", 3)
        return text[end + 4:] if end != -1 else text
    return text


def blocks(path):
    """{id: (text, is_heading)} in file order; multi-line blocks joined with spaces."""
    out, pending = {}, []
    for line in body(path.read_text(encoding="utf-8")).splitlines():
        line = line.strip().replace("​", "")
        if not line or line.startswith("![["):
            continue
        heading = line.startswith("#")
        line = re.sub(r"^#+\s*", "", line)
        m = MARK.search(line)
        if m:
            pending.append(line[: m.start()].strip())
            text = " ".join(p for p in pending if p)
            out[m.group(1)] = ("" if text == PLACEHOLDER else text, heading)
            pending = []
        else:
            pending.append(line)
    return out


def make_batches(segs, cap):
    sections = {}
    for s in segs:
        sections.setdefault(s["id"].split("-")[0], []).append(s)
    chunks = []
    for group in sections.values():
        k = math.ceil(len(group) / cap)
        size = math.ceil(len(group) / k)
        chunks += [group[i:i + size] for i in range(0, len(group), size)]
    batches, cur = [], []
    for c in chunks:
        if cur and len(cur) + len(c) > cap:
            batches.append(cur)
            cur = []
        cur += c
    if cur:
        batches.append(cur)
    return batches


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--root", required=True)
    p.add_argument("--baseline", action="append", required=True, help="label=path")
    p.add_argument("--out", required=True)
    p.add_argument("--max-batch", type=int, default=45)
    a = p.parse_args()

    root = blocks(VAULT / a.root)
    bases = {}
    for spec in a.baseline:
        label, path = spec.split("=", 1)
        bases[label] = blocks(VAULT / path)
    segs = []
    for sid, (bo, heading) in root.items():
        seg = {"id": sid, "heading": heading, "bo": bo}
        for label, b in bases.items():
            text = b.get(sid, ("", False))[0]
            seg[label] = "" if text.replace(" ", "") == bo.replace(" ", "") else text  # untranslated heading copy
        segs.append(seg)

    out = VAULT / a.out
    (out / "batches").mkdir(parents=True, exist_ok=True)
    (out / "segments.json").write_text(json.dumps(segs, ensure_ascii=False, indent=1), encoding="utf-8")
    batches = make_batches(segs, a.max_batch)
    for i, b in enumerate(batches, 1):
        (out / "batches" / f"batch-{i:02d}.json").write_text(json.dumps(b, ensure_ascii=False, indent=1), encoding="utf-8")
    missing = {label: [s["id"] for s in segs if not s[label]] for label in bases}
    print(f"segments={len(segs)} headings={sum(s['heading'] for s in segs)} batches={len(batches)} "
          f"sizes={[len(b) for b in batches]} missing={ {k: v for k, v in missing.items() if v} }")


if __name__ == "__main__":
    main()

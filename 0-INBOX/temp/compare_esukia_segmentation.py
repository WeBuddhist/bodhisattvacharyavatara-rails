import re
import sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(r"c:\Users\geshe lobzang tseten\repos\bodhisattvacharyavatara-rails")
OUT = ROOT / "0-INBOX" / "temp" / "compare_esukia_segmentation_results.txt"
ESUKIA = ROOT / "0-INBOX" / "esukia_align"
SEG = ROOT / "0-INBOX" / "segmentation"


def find_commentary_file(folder: Path):
    for name in ["Commentary.txt", "commentary", "Commentary", "Commentary (1).txt"]:
        p = folder / name
        if p.exists():
            return p
    return None


def normalize(text: str) -> str:
    if text.startswith("---"):
        parts = text.split("---", 2)
        if len(parts) >= 3:
            text = parts[2]
    text = re.sub(r"\{D\d+[a-z]?\}", "", text)
    text = re.sub(r"\^[\d\-]+", "", text)
    text = re.sub(r"[#*_`\[\]|]", "", text)
    text = re.sub(r"\s+", "", text)
    return text


def sample_chunks(norm: str, n: int = 8, size: int = 500):
    if len(norm) < size:
        return [norm] if norm else []
    if n == 1:
        return [norm[:size]]
    step = max(1, (len(norm) - size) // (n - 1))
    chunks = []
    for i in range(n):
        start = min(i * step, len(norm) - size)
        chunks.append(norm[start : start + size])
    return chunks


def overlap_ratio(a: str, b: str, n: int = 12, size: int = 500) -> float:
    if not a or not b:
        return 0.0
    chunks = sample_chunks(a, n=n, size=size)
    if not chunks:
        return 0.0
    return sum(1 for c in chunks if c in b) / len(chunks)


esukia = {}
for d in sorted(ESUKIA.iterdir()):
    if not d.is_dir():
        continue
    cf = find_commentary_file(d)
    if not cf:
        continue
    raw = cf.read_text(encoding="utf-8", errors="replace")
    esukia[d.name] = {"file": cf, "raw": raw, "norm": normalize(raw)}

seg_files = {}
for p in sorted(SEG.glob("*.md")):
    raw = p.read_text(encoding="utf-8", errors="replace")
    seg_files[p.name] = {"raw": raw, "norm": normalize(raw)}

lines = []
lines.append("ESUKIA -> SEGMENTATION MATCHES")
lines.append("=" * 90)
for ename, ed in esukia.items():
    lines.append(f"\n{ename} ({ed['file'].name}, {len(ed['norm'])} chars)")
    preview = ed["raw"][:100].replace("\n", " ")
    lines.append(f"  preview: {preview}")
    if len(ed["norm"]) < 200:
        lines.append("  STATUS: empty or too small")
        continue
    scored = []
    for sname, sd in seg_files.items():
        ratio = overlap_ratio(ed["norm"], sd["norm"])
        if ratio > 0:
            scored.append((ratio, sname, len(sd["norm"])))
    scored.sort(reverse=True)
    if not scored:
        lines.append("  BEST: no match in segmentation")
    else:
        for ratio, sname, slen in scored[:5]:
            flag = "LIKELY MATCH" if ratio >= 0.75 else "partial"
            lines.append(f"  {ratio:5.0%}  {sname} ({slen} chars) [{flag}]")

lines.append("\n\nSEGMENTATION INTERNAL DUPLICATES (>=75% sample overlap)")
lines.append("=" * 90)
names = list(seg_files.keys())
for i in range(len(names)):
    for j in range(i + 1, len(names)):
        a, b = names[i], names[j]
        na, nb = seg_files[a]["norm"], seg_files[b]["norm"]
        if len(na) < 2000 or len(nb) < 2000:
            continue
        r_ab = overlap_ratio(na, nb)
        r_ba = overlap_ratio(nb, na)
        r = max(r_ab, r_ba)
        if r >= 0.75:
            shorter, longer = (a, b) if len(na) <= len(nb) else (b, a)
            lines.append(f"  {r:5.0%}  {shorter}")
            lines.append(f"         <-> {longer}")

lines.append("\n\nESUKIA INTERNAL DUPLICATES")
lines.append("=" * 90)
enames = list(esukia.keys())
for i in range(len(enames)):
    for j in range(i + 1, len(enames)):
        a, b = enames[i], enames[j]
        na, nb = esukia[a]["norm"], esukia[b]["norm"]
        if len(na) < 2000 or len(nb) < 2000:
            continue
        r = max(overlap_ratio(na, nb), overlap_ratio(nb, na))
        if r >= 0.75:
            lines.append(f"  {r:5.0%}  {a} <-> {b}")

OUT.write_text("\n".join(lines), encoding="utf-8")
print(f"Wrote {OUT}")

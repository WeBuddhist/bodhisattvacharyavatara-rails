import json
import re
from pathlib import Path

PART_DIR = Path("/tmp/vi_partials")
OUT_DIR = Path("/tmp/vi_final")
OUT_DIR.mkdir(exist_ok=True)
STEM = "vi-BCA-Full-Beginner"

partials = sorted(PART_DIR.glob("partial_ch*.json"))

# 1. Merge keyword scores globally: keep min (best) score per normalized key
global_scores = {}   # normalized -> {"raw":..., "score":...}
all_verses = {}       # verse_id -> {"text":..., "chapter":...}
chapter_verse_keywords = {}  # verse_id -> list of {"key","score","raw"}

for p in partials:
    data = json.loads(p.read_text(encoding="utf-8"))
    chapter = data["chapter"]
    for kw in data["keywords"]:
        norm = kw["normalized"]
        if norm not in global_scores or kw["score"] < global_scores[norm]["score"]:
            global_scores[norm] = {"raw": kw["raw"], "score": kw["score"]}
    for v in data["verses"]:
        vid = v["verse_id"]
        all_verses[vid] = {"text": v["text"], "chapter": chapter}

# 2. Global rank = sort all unique normalized keywords by best score
sorted_keys = sorted(global_scores.items(), key=lambda kv: kv[1]["score"])
rank_of = {norm: i + 1 for i, (norm, _) in enumerate(sorted_keys)}

# 3. raw.json / normalized.json  (key -> score, sorted by score)
def write_score_json(data: dict, path: Path):
    items = list(data.items())
    lines = ["{"]
    for i, (key, score) in enumerate(items):
        suffix = "," if i < len(items) - 1 else ""
        lines.append(f'  {json.dumps(key, ensure_ascii=False)}: {round(score, 6):.6f}{suffix}')
    lines.append("}")
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")

raw_data = {v["raw"]: v["score"] for _, v in sorted_keys}
norm_data = {k: v["score"] for k, v in sorted_keys}
write_score_json(raw_data, OUT_DIR / f"{STEM}-raw.json")
write_score_json(norm_data, OUT_DIR / f"{STEM}-normalized.json")
print(f"Global unique keywords: {len(sorted_keys)}")

# 4. keywords.md
lines = ["# Keywords\n", "| Score | Keyword |", "|-------|---------|"]
for k, v in sorted_keys:
    lines.append(f"| {round(v['score'], 6):.6f} | {k} |")
(OUT_DIR / f"{STEM}-keywords.md").write_text("\n".join(lines), encoding="utf-8")

# 5. verse-centric keyword_verses_yake.json
#    re-derive per-verse keyword hits via substring match against each
#    verse's own text (case-insensitive), using the GLOBAL rank/score.
result = {}
for vid, vinfo in all_verses.items():
    text_lower = vinfo["text"].lower()
    hits = []
    for norm, info in global_scores.items():
        raw_lower = info["raw"].lower()
        if raw_lower in text_lower:
            count = text_lower.count(raw_lower)
            hits.append({
                "key": norm,
                "rank": rank_of[norm],
                "score": info["score"],
                "count": count,
            })
    hits.sort(key=lambda h: h["score"])
    result[vid] = {"text": vinfo["text"], "keywords": hits}

def _verse_key(vid):
    parts = re.split(r"[-]", vid)
    try:
        return [int(p) for p in parts]
    except ValueError:
        return [0]

ordered = dict(sorted(result.items(), key=lambda kv: _verse_key(kv[0])))
(OUT_DIR / f"{STEM}-keyword_verses_yake.json").write_text(
    json.dumps(ordered, ensure_ascii=False, indent=2), encoding="utf-8"
)
total_hits = sum(len(v["keywords"]) for v in ordered.values())
print(f"Verse file: {len(ordered)} verses, {total_hits} keyword hits")

#!/usr/bin/env python3
"""
json_inspector.py — profile a JSON file holding a classical text and report
its structure so a converter can be built.

Usage:
    python json_inspector.py path/to/source.json
    python json_inspector.py path/to/source.json --out profile.json

Outputs (stdout by default, JSON):

  {
    "file":               { "path", "size_bytes" },
    "top_level":          { "type", "keys" or "length" },
    "metadata_candidates": { ... top-level string/int fields ... },
    "content_array":      { "name", "length", "item_keys" } | null,
    "category_fields":    { "<key>": { "distribution": {...}, "samples": {...} } },
    "chapter_field":      { "name", "distribution" } | null,
    "samples":            [...],
    "source_slug":        "tipitaka_org_book"
  }
"""

from __future__ import annotations
import argparse
import json
import re
import sys
from collections import Counter
from pathlib import Path


# Field names that commonly identify a segment's role/type
CATEGORY_FIELD_HINTS = {"type", "kind", "class", "css_class", "style", "role", "level", "tag"}
# Field names that commonly identify a chapter/section number
CHAPTER_FIELD_HINTS = {"chapter", "section", "book", "part", "ch", "div"}
# Field names that commonly hold metadata strings
METADATA_FIELD_HINTS = {
    "id", "title", "title_pali", "title_sanskrit", "title_tibetan", "title_en",
    "author", "translator", "publisher", "language", "lang", "script",
    "date", "year", "source", "source_filename", "source_url",
    "pitaka", "collection", "layer", "layer_type",
    "total_segments", "total_characters",
}
# Field names that commonly hold the actual text content
CONTENT_FIELD_HINTS = {"content", "text", "body", "value", "string"}


def file_info(path: Path) -> dict:
    return {"path": str(path), "size_bytes": path.stat().st_size}


def top_level(data) -> dict:
    if isinstance(data, dict):
        return {"type": "object", "keys": list(data.keys())}
    if isinstance(data, list):
        return {"type": "array", "length": len(data)}
    return {"type": type(data).__name__}


def metadata_candidates(data: dict) -> dict:
    """Top-level fields that look like metadata: short strings, numbers, or simple lists."""
    out = {}
    for k, v in data.items():
        if k.lower() in METADATA_FIELD_HINTS:
            out[k] = v
            continue
        if isinstance(v, str) and len(v) <= 200:
            out[k] = v
        elif isinstance(v, (int, float, bool)):
            out[k] = v
        elif isinstance(v, list) and v and all(isinstance(x, str) for x in v) and len(v) <= 20:
            out[k] = v
    return out


def find_content_array(data: dict) -> tuple[str, list] | tuple[None, None]:
    """Find the largest array-of-dicts in the top level — likely the content stream."""
    best_name, best_arr = None, None
    for k, v in data.items():
        if isinstance(v, list) and v and isinstance(v[0], dict):
            if best_arr is None or len(v) > len(best_arr):
                best_name, best_arr = k, v
    return best_name, best_arr


def union_keys(items: list[dict], cap: int = 500) -> list[str]:
    seen = set()
    for it in items[:cap]:
        if isinstance(it, dict):
            seen.update(it.keys())
    return sorted(seen)


def detect_category_fields(items: list[dict], max_categories: int = 20) -> dict:
    """For each candidate category-like key, build a distribution + sample content per value."""
    if not items:
        return {}
    keys = union_keys(items)
    out = {}
    for k in keys:
        # candidate if name hints OR values are a small enumerated set
        values = [it.get(k) for it in items if isinstance(it, dict) and it.get(k) is not None]
        if not values:
            continue
        # only care about scalar values (str / int)
        if not all(isinstance(v, (str, int, float, bool)) for v in values):
            continue
        distinct = set(values)
        is_hint = k.lower() in CATEGORY_FIELD_HINTS
        is_enum = 1 < len(distinct) <= max_categories and len(distinct) < len(values) / 5
        if not (is_hint or is_enum):
            continue
        dist = Counter(values)
        # samples: first content-bearing item for each distinct value
        samples = {}
        for it in items:
            if not isinstance(it, dict):
                continue
            v = it.get(k)
            if v is None or v in samples:
                continue
            text = _extract_content(it)
            samples[v] = text[:160] if text else None
            if len(samples) == len(dist):
                break
        out[k] = {
            "distribution": dict(dist.most_common()),
            "samples": {str(kk): vv for kk, vv in samples.items()},
        }
    return out


def detect_chapter_field(items: list[dict]) -> dict | None:
    """Best guess at the chapter-numbering field."""
    if not items:
        return None
    keys = union_keys(items)
    candidates = []
    for k in keys:
        if k.lower() not in CHAPTER_FIELD_HINTS:
            continue
        values = [it.get(k) for it in items if isinstance(it, dict) and it.get(k) is not None]
        if not values or not all(isinstance(v, (int, str)) for v in values):
            continue
        dist = Counter(values)
        # plausible chapter field: small number of distinct values, integer-like
        if 1 < len(dist) <= 200:
            candidates.append((k, dist))
    if not candidates:
        return None
    # prefer integer-valued fields with smallest cardinality (i.e. real chapters not paragraph IDs)
    candidates.sort(key=lambda c: (
        not all(isinstance(v, int) for v in c[1]),
        len(c[1]),
    ))
    name, dist = candidates[0]
    return {"name": name, "distribution": dict(sorted(dist.items(), key=lambda x: (str(type(x[0])), x[0])))}


def _extract_content(item: dict) -> str | None:
    """Pull out the textual content of a segment-like object."""
    for k in ("content", "text", "body", "value", "string", "pali", "sanskrit", "tibetan"):
        v = item.get(k)
        if isinstance(v, str) and v.strip():
            return v
    return None


def collect_samples(items: list[dict], k: int = 7) -> list[dict]:
    """First k-2, middle 1, last 2 of the segments — full objects."""
    if not items:
        return []
    n = len(items)
    if n <= k:
        return items
    out = items[: max(1, k - 3)]
    out.append(items[n // 2])
    out.extend(items[-2:])
    return out


def suggest_source_slug(data: dict, path: Path) -> str:
    """Derive a slug for naming the converter."""
    # Highest priority: explicit source identification fields
    for key in ("source", "publisher", "source_filename"):
        v = data.get(key) if isinstance(data, dict) else None
        if isinstance(v, str) and v.strip():
            return _slugify(v)
    # tipitaka.org pattern: id like 'abh01m', source_filename like 'book/abh01m.mul.html'
    if isinstance(data, dict):
        sfn = data.get("source_filename", "")
        if isinstance(sfn, str) and ".mul.html" in sfn:
            return "tipitaka_org_book"
        layer = data.get("layer_type")
        pitaka = data.get("pitaka")
        if layer == "mul" and pitaka in {"abhidhamma", "sutta", "vinaya"}:
            return "tipitaka_org_book"
    # Filename fallback
    stem = path.stem
    return _slugify(stem)


_slug_re = re.compile(r"[^a-z0-9]+")

def _slugify(s: str) -> str:
    s = s.lower()
    s = _slug_re.sub("_", s).strip("_")
    return s or "unknown"


def inspect(path: Path) -> dict:
    with path.open(encoding="utf-8") as f:
        data = json.load(f)
    profile: dict = {
        "file": file_info(path),
        "top_level": top_level(data),
    }
    if isinstance(data, dict):
        profile["metadata_candidates"] = metadata_candidates(data)
        arr_name, arr = find_content_array(data)
        if arr is not None:
            profile["content_array"] = {
                "name": arr_name,
                "length": len(arr),
                "item_keys": union_keys(arr),
            }
            profile["category_fields"] = detect_category_fields(arr)
            profile["chapter_field"] = detect_chapter_field(arr)
            profile["samples"] = collect_samples(arr)
        else:
            profile["content_array"] = None
            profile["category_fields"] = {}
            profile["chapter_field"] = None
            profile["samples"] = []
    elif isinstance(data, list):
        profile["metadata_candidates"] = {}
        profile["content_array"] = {
            "name": "(root)",
            "length": len(data),
            "item_keys": union_keys(data),
        }
        profile["category_fields"] = detect_category_fields(data)
        profile["chapter_field"] = detect_chapter_field(data)
        profile["samples"] = collect_samples(data)
    else:
        profile["metadata_candidates"] = {}
        profile["content_array"] = None
        profile["category_fields"] = {}
        profile["chapter_field"] = None
        profile["samples"] = []
    profile["source_slug"] = suggest_source_slug(data if isinstance(data, dict) else {}, path)
    return profile


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("json_path", type=Path)
    ap.add_argument("--out", type=Path, default=None, help="write profile to this file (default: stdout)")
    args = ap.parse_args()
    profile = inspect(args.json_path)
    text = json.dumps(profile, ensure_ascii=False, indent=2, default=str)
    if args.out:
        args.out.write_text(text, encoding="utf-8")
        print(f"Wrote profile to {args.out}", file=sys.stderr)
    else:
        print(text)


if __name__ == "__main__":
    main()

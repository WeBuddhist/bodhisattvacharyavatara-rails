#!/usr/bin/env python3
"""Audit track termbases vs bo-en.md and promote missing entries."""
from __future__ import annotations

import json
import re
from collections import defaultdict
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
BO_EN = ROOT / "2-RAILS/Bilingual-Glossaries/bo-en.md"
KEYWORD_JSON = ROOT / (
    "4-SYSTEM/scripts/english_keyword/output/"
    "en-David_Karma_Choephel_en_bo_keyword_meaning_enriched.json"
)
TRACKS = {
    "en-beginner-audience": ROOT / "3-TRANSFORMATIONS/Translations/en-beginner-audience/termbase.md",
    "en-general-audience": ROOT / "3-TRANSFORMATIONS/Translations/en-general-audience/termbase.md",
    "en-scholarly-audience": ROOT / "3-TRANSFORMATIONS/Translations/en-scholarly-audience/termbase.md",
}
AUDIT_OUT = ROOT / "0-INBOX/glossary-audit.md"

TABLE_ROW = re.compile(r"^\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|\s*([^|]*)\s*\|\s*$")
HEADING = re.compile(r"^##\s+(.+?)\s*$")


def normalize_bo(key: str) -> str:
    return re.sub(r"\s+", " ", key.strip())


def parse_termbase(path: Path) -> dict[str, str]:
    rows = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        m = TABLE_ROW.match(line)
        if not m or m.group(1).strip() in ("Source Lemma (bo)", ":---"):
            continue
        bo = normalize_bo(m.group(1))
        en = m.group(2).strip()
        rows[bo] = en
    return rows


def parse_bo_en(path: Path) -> set[str]:
    keys = set()
    for line in path.read_text(encoding="utf-8").splitlines():
        m = HEADING.match(line)
        if m:
            keys.add(normalize_bo(m.group(1)))
    return keys


def parse_keyword_json(path: Path, rank_cutoff: int = 500) -> dict[str, set[str]]:
    data = json.loads(path.read_text(encoding="utf-8"))
    mapping: dict[str, set[str]] = defaultdict(set)
    for block in data.values():
        for kw in block.get("keywords", []):
            if kw.get("rank", 9999) > rank_cutoff:
                continue
            bo = normalize_bo(kw.get("bo", ""))
            if bo:
                mapping[bo].add(kw.get("key", ""))
    return mapping


def first_rendering(en: str) -> str:
    """Take primary rendering from a termbase cell (may list alternates)."""
    text = en.strip().strip("*")
    if " / " in text:
        return text.split(" / ")[0].strip()
    if " → " in text:
        return text.split(" → ")[0].strip()
    paren = text.find(" (")
    if paren > 0 and text[paren:].startswith(" ("):
        return text[:paren].strip()
    return text


def promote_to_bo_en(
    bo_en_path: Path,
    track_data: dict[str, dict[str, str]],
    missing: list[str],
    existing_count: int,
) -> int:
    """Append termbase attestations to bo-en.md; return count added."""
    by_bo: dict[str, dict[str, str]] = defaultdict(dict)
    for track, rows in track_data.items():
        for bo, en in rows.items():
            by_bo[bo][track] = en

    blocks = []
    for bo in missing:
        tracks = by_bo.get(bo, {})
        renderings: dict[str, list[str]] = defaultdict(list)
        for track, en in tracks.items():
            primary = first_rendering(en)
            renderings[primary].append(track)
        rows_out = []
        for rendering, sources in sorted(renderings.items(), key=lambda x: -len(x[1])):
            src = ", ".join(f"{s} (0)" for s in sorted(sources))
            rows_out.append(
                f"| {rendering} | {src} | 0 | — |"
            )
        block = f"## {bo}\n\n| Rendering | Sources | Total frequency | Local-Wiki |\n"
        block += "|-----------|---------|-----------------|------------|\n"
        block += "\n".join(rows_out)
        block += "\n\n---\n"
        blocks.append(block)

    text = bo_en_path.read_text(encoding="utf-8")
    if not text.endswith("\n"):
        text += "\n"
    text += "\n# Zero-shot track attestations (promoted from termbases)\n\n"
    text += "".join(blocks)

    # Update frontmatter counts
    new_total = existing_count + len(missing)
    text = re.sub(
        r"^total_keywords:\s*\d+\s*$",
        f"total_keywords: {new_total}",
        text,
        count=1,
        flags=re.MULTILINE,
    )
    raw_sources = [
        "2-RAILS/Bilingual-Glossaries/Raw/bo-en-ai.md",
        "2-RAILS/Bilingual-Glossaries/Raw/bo-en-choephel.md",
        "2-RAILS/Bilingual-Glossaries/Raw/bo-en-padmakara.md",
        "2-RAILS/Bilingual-Glossaries/Raw/bo-en-wallace.md",
        "3-TRANSFORMATIONS/Translations/en-beginner-audience/termbase.md",
        "3-TRANSFORMATIONS/Translations/en-general-audience/termbase.md",
        "3-TRANSFORMATIONS/Translations/en-scholarly-audience/termbase.md",
    ]
    if "en-beginner-audience/termbase.md" not in text:
        text = re.sub(
            r"(raw_sources:\n(?:  - .+\n)+)",
            "raw_sources:\n" + "".join(f"  - {s}\n" for s in raw_sources),
            text,
            count=1,
        )
    text = re.sub(
        r"^generated:\s*.+$",
        f"generated: {date.today().isoformat()}",
        text,
        count=1,
        flags=re.MULTILINE,
    )
    bo_en_path.write_text(text, encoding="utf-8")
    return len(missing)


def main() -> None:
    import argparse

    ap = argparse.ArgumentParser()
    ap.add_argument("--promote", action="store_true", help="Append missing terms to bo-en.md")
    args = ap.parse_args()

    bo_en_keys = parse_bo_en(BO_EN)
    track_data = {name: parse_termbase(p) for name, p in TRACKS.items()}
    json_keys = parse_keyword_json(KEYWORD_JSON)

    all_termbase_keys = set()
    for rows in track_data.values():
        all_termbase_keys.update(rows.keys())

    missing_from_bo_en = sorted(all_termbase_keys - bo_en_keys)
    json_only = sorted(set(json_keys.keys()) - bo_en_keys - all_termbase_keys)

    conflicts = []
    by_bo: dict[str, dict[str, str]] = defaultdict(dict)
    for track, rows in track_data.items():
        for bo, en in rows.items():
            by_bo[bo][track] = en
    for bo, tracks in sorted(by_bo.items()):
        renderings = set(tracks.values())
        if len(renderings) > 1:
            conflicts.append((bo, tracks))

    lines = [
        "# Glossary audit — bo → en",
        "",
        f"**Date:** {date.today().isoformat()}",
        "",
        "## Summary",
        "",
        f"- Keywords in `bo-en.md`: **{len(bo_en_keys)}**",
        f"- Keywords in track termbases (union): **{len(all_termbase_keys)}**",
        f"- Keywords in keyword JSON (rank ≤ 500): **{len(json_keys)}**",
        f"- Termbase keywords missing from `bo-en.md`: **{len(missing_from_bo_en)}**",
        f"- Cross-track rendering conflicts: **{len(conflicts)}**",
        "",
        "## Missing from bo-en.md (present in at least one track termbase)",
        "",
    ]
    for bo in missing_from_bo_en[:200]:
        sources = [t for t, rows in track_data.items() if bo in rows]
        en = track_data[sources[0]][bo]
        lines.append(f"- `{bo}` → {en} ({', '.join(sources)})")
    if len(missing_from_bo_en) > 200:
        lines.append(f"- … and {len(missing_from_bo_en) - 200} more")

    lines.extend(["", "## Cross-track conflicts (intentional register divergences flagged)", ""])
    for bo, tracks in conflicts[:80]:
        parts = [f"**{t}:** {r}" for t, r in tracks.items()]
        lines.append(f"- `{bo}` — " + " | ".join(parts))
    if len(conflicts) > 80:
        lines.append(f"- … and {len(conflicts) - 80} more")

    lines.extend(["", "## Keyword JSON lemmas not yet in bo-en or termbases (sample)", ""])
    for bo in json_only[:50]:
        lines.append(f"- `{bo}`")
    if len(json_only) > 50:
        lines.append(f"- … and {len(json_only) - 50} more")

    AUDIT_OUT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Wrote {AUDIT_OUT}")
    print(f"missing_from_bo_en={len(missing_from_bo_en)} conflicts={len(conflicts)}")

    if args.promote and missing_from_bo_en:
        added = promote_to_bo_en(BO_EN, track_data, missing_from_bo_en, len(bo_en_keys))
        print(f"Promoted {added} keywords into {BO_EN}")


if __name__ == "__main__":
    main()

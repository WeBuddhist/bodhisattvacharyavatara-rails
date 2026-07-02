#!/usr/bin/env python3
"""Formalize per-track termbase.md via glossary-select rules."""
from __future__ import annotations

import re
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
BO_EN = ROOT / "2-RAILS/Bilingual-Glossaries/bo-en.md"

TRACKS = {
    "en-general-audience": {
        "termbase": ROOT / "3-TRANSFORMATIONS/Translations/en-general-audience/termbase.md",
        "requirements": ROOT / "3-TRANSFORMATIONS/Translations/en-general-audience/requirements.md",
        "rank_cutoff": 500,
        "title": "General Audience Translation (en-general-audience)",
        "register_note": (
            "Naturalized loanwords (bodhichitta, samsara, dharma, karma, nirvana, "
            "buddha, bodhisattva) bare; rarer Sanskrit rendered in plain English."
        ),
    },
    "en-beginner-audience": {
        "termbase": ROOT / "3-TRANSFORMATIONS/Translations/en-beginner-audience/termbase.md",
        "requirements": ROOT / "3-TRANSFORMATIONS/Translations/en-beginner-audience/requirements.md",
        "rank_cutoff": 200,
        "title": "Beginner Register (en-beginner-audience)",
        "register_note": "Plain English; loanwords glossed once per chapter; avoid scholastic terms.",
    },
    "en-scholarly-audience": {
        "termbase": ROOT / "3-TRANSFORMATIONS/Translations/en-scholarly-audience/termbase.md",
        "requirements": ROOT / "3-TRANSFORMATIONS/Translations/en-scholarly-audience/requirements.md",
        "rank_cutoff": None,
        "title": "Scholarly Register (en-scholarly-audience)",
        "register_note": "Technical Buddhist English; Sanskrit terms retained where standard.",
    },
}

TABLE_ROW = re.compile(r"^\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|\s*([^|]*)\s*\|\s*$")
HEADING = re.compile(r"^##\s+(.+?)\s*$")
RENDER_ROW = re.compile(r"^\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|\s*(\d+)\s*\|\s*([^|]*)\s*\|\s*$")


def parse_termbase(path: Path) -> list[tuple[str, str, str]]:
    rows = []
    for line in path.read_text(encoding="utf-8").splitlines():
        m = TABLE_ROW.match(line)
        if not m or m.group(1).strip() in ("Source Lemma (bo)", ":---"):
            continue
        rows.append((m.group(1).strip(), m.group(2).strip(), m.group(3).strip()))
    return rows


def parse_bo_en_renderings(path: Path) -> dict[str, list[tuple[str, int, str]]]:
    text = path.read_text(encoding="utf-8")
    out: dict[str, list[tuple[str, int, str]]] = {}
    parts = re.split(r"^##\s+(?!#)(.+?)\s*$", text, flags=re.MULTILINE)
    for i in range(1, len(parts), 2):
        key = parts[i].strip()
        section = parts[i + 1]
        renderings = []
        for line in section.splitlines():
            m = RENDER_ROW.match(line)
            if not m:
                continue
            try:
                freq = int(m.group(3).strip())
            except ValueError:
                freq = 0
            renderings.append((m.group(1).strip(), freq, m.group(2).strip()))
        renderings.sort(key=lambda x: -x[1])
        out[key] = renderings
    return out


def pick_rendering(
    track: str,
    bo: str,
    current: str,
    bo_en: dict[str, list[tuple[str, int, str]]],
) -> tuple[str, str, str]:
    """Return (rendering, origin, rationale)."""
    candidates = bo_en.get(bo, [])
    if current:
        return (
            current,
            "attested",
            f"Locked zero-shot rendering retained; aligned with `{track}` requirements.md.",
        )
    if candidates:
        rendering, freq, sources = candidates[0]
        return (
            rendering,
            "attested",
            f"Selected from bo-en.md ({sources}, freq {freq}).",
        )
    return ("", "derived", "No attested rendering; requires Local-Wiki derivation.")


def write_termbase(
    track: str,
    cfg: dict,
    rows: list[tuple[str, str, str, str, str]],
    derivations: list[tuple[str, str]],
) -> None:
    path = cfg["termbase"]
    body = [
        "---",
        f"track: {track}",
        "language_pair: bo-en",
        f"requirements: 3-TRANSFORMATIONS/Translations/{track}/requirements.md",
        "consolidated_glossary: 2-RAILS/Bilingual-Glossaries/bo-en.md",
        f"total_keywords: {len(rows)}",
        f"last_updated: {date.today().isoformat()}",
        "status: draft",
        "---",
        "",
        f"# Termbase — {cfg['title']}",
        "",
        f"Formalized by `glossary-select` on {date.today().isoformat()}. "
        f"{cfg['register_note']}",
        "",
        "Selection rubric: [`requirements.md`](requirements.md) · attestation menu: "
        "[`2-RAILS/Bilingual-Glossaries/bo-en.md`](../../2-RAILS/Bilingual-Glossaries/bo-en.md).",
        "",
        "| Source Lemma (bo) | Chosen Rendering (en) | Origin | Rationale |",
        "| :--- | :--- | :--- | :--- |",
    ]
    for bo, en, origin, rationale, _ in rows:
        body.append(f"| {bo} | {en} | {origin} | {rationale} |")

    if derivations:
        body.extend(["", "## Notes on derivations", ""])
        for bo, note in derivations:
            body.extend([f"### {bo}", "", note, ""])

    path.write_text("\n".join(body) + "\n", encoding="utf-8")
    print(f"Wrote {path} ({len(rows)} keywords)")


def run_track(track: str, cfg: dict, bo_en: dict[str, list[tuple[str, int, str]]]) -> None:
    existing = parse_termbase(cfg["termbase"])
    rows_out = []
    derivations = []
    for bo, current, old_rationale in existing:
        en, origin, rationale = pick_rendering(track, bo, current, bo_en)
        if origin == "derived":
            derivations.append(
                (
                    bo,
                    f"No satisfactory attested rendering in bo-en.md; derive from Local-Wiki before translation QA.",
                )
            )
        elif old_rationale and old_rationale != rationale:
            rationale = old_rationale
        rows_out.append((bo, en, origin, rationale, old_rationale))

    write_termbase(track, cfg, rows_out, derivations)


def main() -> None:
    bo_en = parse_bo_en_renderings(BO_EN)
    for track, cfg in TRACKS.items():
        run_track(track, cfg, bo_en)


if __name__ == "__main__":
    main()

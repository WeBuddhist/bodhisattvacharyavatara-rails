#!/usr/bin/env python3
"""Write qa-report.md for a translation track from Stage 0 JSON + Stage 1 annotations."""
from __future__ import annotations

import json
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def load_stage0(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def write_report(
    track_dir: Path,
    label: str,
    stage0_path: Path,
    stage1: list[dict],
    rails_basis: str,
) -> None:
    s0 = load_stage0(stage0_path)
    counts = s0["counts"]
    crit = counts["critical"]
    maj = counts["major"]
    gate = "FAIL" if crit or maj else "PASS"
    score = max(0.0, 100.0 - (crit * 10 + maj * 5) * 0.1)

    profile: dict[str, int] = {}
    for f in s0.get("findings", []):
        dim = f["dimension"]
        profile[dim] = profile.get(dim, 0) + 1
    for f in stage1:
        dim = f["dimension"]
        profile[dim] = profile.get(dim, 0) + 1

    profile_line = " · ".join(f"{k} {v}" for k, v in sorted(profile.items()))

    lines = [
        f"## QA run — {label} — {date.today().isoformat()}",
        "",
        f"**Score:** {score:.1f} / 100   **Gate:** {gate} "
        f"({crit} critical, {maj} major present in Stage 0+1)",
        f"**Profile:** {profile_line or 'none'}",
        f"**Rails basis:** {rails_basis}",
        "",
        "### Stage 0 — mechanical (full merged text)",
        "",
        f"- File: `{s0['file']}`",
        f"- Verse IDs in translation: {s0['verse_count']}",
        f"- Critical: {crit} · Major: {maj} · Minor: {counts['minor']}",
        "",
    ]

    crit_major = [f for f in s0.get("findings", []) if f["severity"] in ("critical", "major")]
    if crit_major:
        lines.extend(["| Verse | Dimension | Severity | Note |", "|---|---|---|---|"])
        for f in crit_major[:30]:
            lines.append(
                f"| {f['verse']} | {f['dimension']} | {f['severity'].upper()} | {f['detail']} |"
            )
        lines.append("")

    if stage1:
        lines.extend(
            [
                "### Stage 1 — semantic (pilot scope)",
                "",
                "| Verse | Dimension | Severity | Note | Suggested fix | Cite |",
                "|---|---|---|---|---|---|",
            ]
        )
        for f in stage1:
            lines.append(
                f"| {f['verse']} | {f['dimension']} | {f['severity'].upper()} | "
                f"{f['note']} | {f.get('suggested_fix', '—')} | {f.get('cite', '—')} |"
            )
        lines.append("")

    if stage1:
        lines.extend(["### Top fixes", ""])
        for i, f in enumerate(
            [x for x in stage1 if x["severity"] in ("critical", "major")][:5], 1
        ):
            lines.append(f"{i}. {f.get('suggested_fix', f['note'])}")
        if not any(x["severity"] in ("critical", "major") for x in stage1):
            lines.append("1. No Critical/Major semantic issues in pilot scope.")
        lines.append("")

    out = track_dir / "qa-report.md"
    existing = out.read_text(encoding="utf-8") if out.exists() else ""
    out.write_text(existing + "\n".join(lines) + "\n", encoding="utf-8")
    print(f"Appended qa-report to {out}")


STAGE1_GENERAL_CH12 = [
    {
        "verse": "1-1",
        "dimension": "Terminology",
        "severity": "minor",
        "note": "Uses \"dharma they embody\" for ཆོས་ཀྱི་སྐུ་མངའ་; acceptable general-register paraphrase of dharmakāya possession.",
        "suggested_fix": "Optional: \"the teaching they embody\" if emphasizing Dharma Jewel over realization body.",
        "cite": "1-SOURCES/Translations/bo-བློ་ལྡན་ཤེས་རབ།.md#^1-1",
    },
    {
        "verse": "1-9",
        "dimension": "Terminology",
        "severity": "minor",
        "note": "\"child of the buddhas\" for བདེ་གཤེགས་རྣམས་ཀྱི་སྲས་; consistent with heir imagery though termbase prefers \"bodhisattva(s)\".",
        "suggested_fix": "Consider \"heir of the buddhas\" for closer alignment with termbase.",
        "cite": "1-SOURCES/Translations/bo-བློ་ལྡན་ཤེས་རབ།.md#^1-9",
    },
    {
        "verse": "2-13",
        "dimension": "LocaleConvention",
        "severity": "minor",
        "note": "Proper names Samantabhadra, Manjushri, Avalokiteshvara without diacritics; acceptable for general register.",
        "suggested_fix": "—",
        "cite": "1-SOURCES/Translations/bo-བློ་ལྡན་ཤེས་རབ།.md#^2-13",
    },
    {
        "verse": "2-41",
        "dimension": "Terminology",
        "severity": "minor",
        "note": "\"Yama's messengers\" for གཤིན་རྗེའི་ཕོ་ཉ་; plain English per requirements.",
        "suggested_fix": "—",
        "cite": "1-SOURCES/Translations/bo-བློ་ལྡན་ཤེས་རབ།.md#^2-41",
    },
]

STAGE1_BEGINNER_CH12 = [
    {
        "verse": "1-1",
        "dimension": "Audience",
        "severity": "minor",
        "note": "Opening bowing verse reads clearly at beginner register; bodhichitta gloss policy deferred to per-chapter first use.",
        "suggested_fix": "—",
        "cite": "1-SOURCES/Translations/bo-བློ་ལྡན་ཤེས་རབ།.md#^1-1",
    },
]

STAGE1_SCHOLARLY_CH12 = [
    {
        "verse": "1-1",
        "dimension": "Style/Register",
        "severity": "minor",
        "note": "Uses \"Bodhicitta\" spelling in chapter title vs \"bodhichitta\" in termbase; internal consistency check recommended.",
        "suggested_fix": "Pick one spelling (termbase: bodhicitta) across title and body.",
        "cite": "3-TRANSFORMATIONS/Translations/en-scholarly-audience/requirements.md",
    },
]


def main() -> None:
    reports = [
        (
            ROOT / "3-TRANSFORMATIONS/Translations/en-general-audience",
            "BCA-Full-General-English.md + Chapter-01/02 pilot",
            ROOT / "0-INBOX/qa-stage0-en-general-v2.json",
            STAGE1_GENERAL_CH12,
            "2-RAILS/Verses draft for ch.1 (1-1–1-15); ch.1–2 scored against Tibetan/Sanskrit source.",
        ),
        (
            ROOT / "3-TRANSFORMATIONS/Translations/en-beginner-audience",
            "BCA-Full-Beginner-English.md + Chapter-01/02 pilot",
            ROOT / "0-INBOX/qa-stage0-en-beginner-v2.json",
            STAGE1_BEGINNER_CH12,
            "Source-only for ch.1–2; verse rails not complete.",
        ),
        (
            ROOT / "3-TRANSFORMATIONS/Translations/en-scholarly-audience",
            "BCA-Full-Scholarly-English.md + Chapter-01/02 pilot",
            ROOT / "0-INBOX/qa-stage0-en-scholarly-v2.json",
            STAGE1_SCHOLARLY_CH12,
            "Source-only for ch.1–2; verse rails not complete.",
        ),
    ]
    for track_dir, label, s0, s1, basis in reports:
        if not s0.exists():
            print(f"Skip {label}: missing {s0}", file=sys.stderr)
            continue
        write_report(track_dir, label, s0, s1, basis)


if __name__ == "__main__":
    main()

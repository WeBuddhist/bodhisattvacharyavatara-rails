#!/usr/bin/env python3
"""Build a Chinese track's requirements.md from its bilingual prompt draft.

  python3 assemble.py <draft.md> <track-dir> [--title "# 翻譯要求 —— <經名>，中文<版本>"]

The draft holds sections 一…五. Each section is the Chinese text Gemini receives, followed by
"### English mirror" and "### Design notes", which are never sent. Sections are separated by a line
"---" and start with "## 一、", "## 二、" … This script puts the sections in order (and rewrites the draft
in that order), takes only the Chinese part of each, and writes it into <track-dir>/requirements.md
below that file's own frontmatter and title line, which are kept. The whole of requirements.md minus its
frontmatter is the system instruction (translation runner option --system).

Edit the draft, never requirements.md directly; then run this script. Archive the previous
requirements.md before the first build (see SKILL.md, step 6).
"""
import argparse
import pathlib
import re

ORDER = "一二三四五"

p = argparse.ArgumentParser()
p.add_argument("draft")
p.add_argument("track_dir")
p.add_argument("--title", help="H1 line to use when requirements.md has none")
a = p.parse_args()

draft = pathlib.Path(a.draft)
req = pathlib.Path(a.track_dir) / "requirements.md"
text = draft.read_text(encoding="utf-8")
head, *parts = re.split(r"\n---\n\n(?=## )", text)
parts.sort(key=lambda s: ORDER.index(s[3]) if s[3] in ORDER else 99)
if [s[3] for s in parts] != list(ORDER):
    raise SystemExit(f"draft must contain exactly the sections 一…五, found: {[s.split(chr(10))[0] for s in parts]}")
draft.write_text("\n---\n\n".join([head] + [s.rstrip("\n") for s in parts]) + "\n", encoding="utf-8")

zh = "\n\n".join(s.split("\n### English mirror")[0].rstrip() for s in parts)
if "English mirror" in zh or "Design notes" in zh:
    raise SystemExit("an English mirror or design note would leak into the prompt")

old = req.read_text(encoding="utf-8") if req.exists() else ""
fm = re.match(r"\A---\n.*?\n---\n", old, flags=re.S)
if not fm:
    raise SystemExit(f"{req} needs YAML frontmatter (track, target_language, register, termbase …) before the first build")
title = re.search(r"^# .+$", old[fm.end():], flags=re.M)
title = title.group(0) if title else a.title
if not title:
    raise SystemExit("requirements.md has no '# ' title line: pass --title")
req.write_text(f"{fm.group(0)}\n{title}\n\n{zh}\n", encoding="utf-8")
print(f"wrote {req}: {len(zh)} chars, sections {[s.split(chr(10))[0] for s in parts]}")

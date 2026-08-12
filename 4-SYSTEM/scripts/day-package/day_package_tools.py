#!/usr/bin/env python3
"""
day_package_tools.py — lock + enforce the Day-Package (English) format.

Two subcommands:

  validate <file.md> [...]   Check a day-package file against the locked
                             contract. Exits non-zero and prints every
                             violation ("fail loud"). Structural problems are
                             ERRORS; softer issues are WARNINGS.

  conform  <file.md> [...]   Rewrite a day-package file in place to match the
                             contract: insert machine anchors before every
                             recognized heading, and consolidate inline
                             citation links into a single `Sources:` line per
                             leaf section. Never rewords prose. Tables are left
                             untouched (their Source column is legitimate
                             structured provenance).

  guard record               Record sha256 of every protected file (listed in
                             `guard.paths`) into `guard.lock`. Run this after an
                             APPROVED change so the baseline stays current.
  guard check                Re-hash the protected files and report any that
                             changed / went missing since the last `record`.
                             Exits non-zero on any drift ("fail loud"). This is
                             advisory drift-detection, not enforcement.

PROTECTED SOURCE-OF-TRUTH TOOL — do not edit, move, or delete this script
without explicit human confirmation (see 4-SYSTEM/CLAUDE.md -> "Protected files").

The canonical spec lives in:
  3-TRANSFORMATIONS/Day-Packages/bo/_TEMPLATE.md
This script and that document must agree.
"""
import hashlib
import os
import re
import sys

# ---- locked section vocabulary -------------------------------------------

# Top-level (H2) sections, in required order. key -> (exact heading text w/o "N. ", anchor)
TOP_SECTIONS = [
    ("challenge", "Today's Challenge", "sec:challenge"),
    ("verses",    "Today's Verses",    "sec:verses"),
    ("rails",     "Verse Rails",       "sec:rails"),
]

# H3 subsections inside "Today's Challenge" (exact text -> anchor slug)
CHALLENGE_SUBS = {
    "Notification":       "challenge:notification",
    "Opening":            "challenge:opening",
    "From the Tradition": "challenge:tradition",
    "Today's Practice":   "challenge:practice",
}

# H4 subsections inside each verse. exact heading text -> (anchor slug, required?)
VERSE_SUBS = [
    ("Root Verse",                                              "sub:root-verse",      True),
    ("Interlinear Gloss",                                       "sub:interlinear",     True),   # prefix match
    ("Commentary Explanations",                                 "sub:commentary",      True),
    ("Stories and Illustrations",                               "sub:stories",         False),
    ("Metaphors and Examples",                                  "sub:metaphors",       False),
    ("Scriptural Quotations",                                   "sub:quotations",      False),
    ("Main Teaching Points",                                    "sub:teaching-points", True),
    ("Key Terms",                                               "sub:key-terms",       True),
    ("Verse Synthesis (overview)",                              "sub:synthesis",       True),
]

# sentinel: this heading's machine id lives in its <!-- cm:/story: --> anchor,
# not in the visible heading text (which is display-only: name + work).
PRESERVE = "\x00PRESERVE"

CITATION = re.compile(r"\[\[[^\]]*\]\]")
# an inline citation "wrapper": optional arrow, then (link link ...) containing only links
CIT_WRAPPER = re.compile(r"\s*(?:→\s*)?\(\s*(?:\[\[[^\]]*\]\]\s*)+\)")
ANCHOR = re.compile(r"^<!--\s*([a-z]+:[A-Za-z0-9._:-]+)\s*-->\s*$")
HEADING = re.compile(r"^(#{2,5})\s+(.*?)\s*$")


def split_frontmatter(text):
    m = re.match(r"^(---\n.*?\n---\n)(.*)$", text, re.DOTALL)
    if m:
        return m.group(1), m.group(2)
    return "", text


def heading_anchor(level, text):
    """Return the anchor slug a heading should carry, or None if not tracked."""
    if level == 2:
        m = re.match(r"^\d+\.\s+(.*)$", text)
        core = m.group(1) if m else text
        for _key, htext, slug in TOP_SECTIONS:
            if core.startswith(htext):
                return slug
        return None
    if level == 3:
        if text.startswith("Verse "):
            vid = text[len("Verse "):].strip()
            return f"verse:{vid}"
        for htext, slug in CHALLENGE_SUBS.items():
            if text == htext:
                return slug
        return None
    if level == 4:
        core4 = text.lstrip("⚑ ").strip()
        if core4.startswith("Divergences"):
            return "sub:divergences"
        for htext, slug, _req in VERSE_SUBS:
            if text.startswith(htext):
                return slug
        return None
    if level == 5:
        # a "Divergences" block (records where commentators disagree)
        core5 = text.lstrip("⚑ ").strip()
        if core5.startswith("Divergences"):
            return "div:divergences"
        # commentator / story block. The visible heading is display-only
        # (Name + Work, or story Title); the machine id lives in the
        # `<!-- cm:.. -->` / `<!-- story:.. -->` anchor above. Preserve it.
        return PRESERVE
    return None


# ---------------------------------------------------------------- validate --

def validate(path):
    errors, warnings = [], []
    raw = open(path, encoding="utf-8").read()
    fm, body = split_frontmatter(raw)

    # frontmatter required keys
    if not fm:
        errors.append("missing YAML frontmatter")
    else:
        for key in ("day:", "chapter:", "verses:", "status:", "language:", "document_type:"):
            if not re.search(r"(?m)^" + re.escape(key), fm):
                errors.append(f"frontmatter missing `{key}`")

    lines = body.split("\n")

    # no unresolved Obsidian transclusions
    for i, ln in enumerate(lines, 1):
        if "![[" in ln:
            errors.append(f"line {i}: unresolved transclusion `![[...]]` (inline the text instead)")

    # every tracked heading must be immediately preceded by its correct anchor
    top_seen = []
    verse_ids = []
    for i, ln in enumerate(lines):
        m = HEADING.match(ln)
        if not m:
            continue
        level = len(m.group(1))
        text = m.group(2)
        want = heading_anchor(level, text)
        if want is None:
            if level in (2, 4):
                warnings.append(f'heading not in locked vocabulary: "{ln.strip()}"')
            continue
        prev = lines[i - 1].strip() if i > 0 else ""
        am = ANCHOR.match(prev)
        if want is PRESERVE:
            # commentator/story H5: id lives in the anchor, heading is display-only.
            if not am:
                errors.append(f'line {i+1}: H5 heading "{text}" missing its `<!-- cm:… -->` / `<!-- story:… -->` anchor on preceding line')
            elif not re.match(r"^(cm|story):[A-Za-z0-9._:-]+$", am.group(1)):
                errors.append(f'line {i+1}: H5 heading "{text}" has anchor `{am.group(1)}`, expected a `cm:…` / `story:…` id')
            continue
        if not am:
            errors.append(f'line {i+1}: heading "{text}" missing anchor `<!-- {want} -->` on preceding line')
        elif am.group(1) != want:
            errors.append(f'line {i+1}: heading "{text}" has anchor `{am.group(1)}`, expected `{want}`')
        if want.startswith("sec:"):
            top_seen.append(want)
        if want.startswith("verse:"):
            verse_ids.append(want.split(":", 1)[1])

    # top-level sections present and in order
    want_order = [slug for _k, _t, slug in TOP_SECTIONS]
    if top_seen != want_order:
        errors.append(f"top-level sections {top_seen} != required {want_order}")

    # verse ids match frontmatter `verses:`
    vm = re.search(r'(?m)^verses:\s*"?([0-9]+)-([0-9]+)\s+to\s+([0-9]+)-([0-9]+)"?', fm)
    if not vm:
        vm2 = re.search(r'(?m)^verses:\s*"?([0-9]+)-([0-9]+)"?', fm)
        expect = [f"{vm2.group(1)}-{vm2.group(2)}"] if vm2 else []
    else:
        ch = vm.group(1)
        expect = [f"{ch}-{n}" for n in range(int(vm.group(2)), int(vm.group(4)) + 1)]
    if expect and verse_ids != expect:
        errors.append(f"verse blocks {verse_ids} != frontmatter range {expect}")

    # required per-verse subsections present
    blocks = re.split(r"(?m)^<!-- verse:", body)
    for blk in blocks[1:]:
        vid = blk.split(" ", 1)[0].split("-->", 1)[0].strip()
        for htext, _slug, req in VERSE_SUBS:
            if req and (("#### " + htext) not in blk):
                errors.append(f"verse {vid}: missing required subsection `{htext}`")

    # stray inline citations outside a Sources: line or a table row
    for i, ln in enumerate(lines, 1):
        if ln.lstrip().startswith("|"):
            continue                      # table cell provenance is allowed
        if ln.strip().startswith("Sources:"):
            continue
        if CITATION.search(ln):
            errors.append(f"line {i}: inline citation link outside a `Sources:` line: {ln.strip()[:70]}")

    ok = not errors
    tag = "PASS" if ok else "FAIL"
    print(f"[{tag}] {path}")
    for e in errors:
        print(f"  ERROR:   {e}")
    for w in warnings:
        print(f"  warning: {w}")
    return ok


# ----------------------------------------------------------------- conform --

def conform(path):
    raw = open(path, encoding="utf-8").read()
    fm, body = split_frontmatter(raw)

    orig_lines = body.split("\n")
    # capture, in document order, the anchor immediately preceding each heading.
    # Commentator/story H5 ids are not derivable from the (display-only) heading,
    # so their anchor must be preserved rather than regenerated.
    orig_anchor_by_heading = []
    for i, ln in enumerate(orig_lines):
        if HEADING.match(ln):
            prev = orig_lines[i - 1].strip() if i > 0 else ""
            am = ANCHOR.match(prev)
            orig_anchor_by_heading.append(am.group(1) if am else None)

    # strip ALL existing anchors first; they are regenerated deterministically
    lines = [ln for ln in orig_lines if not ANCHOR.match(ln.strip())]

    # segment the body by headings; segment 0 is the preamble (before 1st heading)
    head_idxs = [i for i, ln in enumerate(lines) if HEADING.match(ln)]
    segments = []
    if not head_idxs:
        segments.append((None, lines))
    else:
        if head_idxs[0] > 0:
            segments.append((None, lines[:head_idxs[0]]))
        for k, hi in enumerate(head_idxs):
            end = head_idxs[k + 1] if k + 1 < len(head_idxs) else len(lines)
            segments.append((hi, lines[hi:end]))

    out = []
    heading_i = -1
    for head_pos, seg in segments:
        if head_pos is None:
            out.extend(seg)                       # preamble, verbatim
            continue

        heading_i += 1
        head_line = seg[0]
        m = HEADING.match(head_line)
        want = heading_anchor(len(m.group(1)), m.group(2))
        if want is PRESERVE:
            # reuse the id from the anchor that was already there (display-only heading)
            want = orig_anchor_by_heading[heading_i]
        content = list(seg[1:])

        # peel trailing blanks and a trailing "---" rule (remembered, re-added last)
        trailing_sep = False
        while content and content[-1].strip() == "":
            content.pop()
        if content and content[-1].strip() == "---":
            trailing_sep = True
            content.pop()
            while content and content[-1].strip() == "":
                content.pop()

        has_table = any(l.lstrip().startswith("|") for l in content)
        toks = []
        if not has_table:
            rebuilt = []
            for l in content:
                if not CITATION.search(l):
                    rebuilt.append(l)             # no citation -> leave verbatim (keeps hard breaks)
                    continue
                for t in CITATION.findall(l):
                    if t not in toks:
                        toks.append(t)
                if l.lstrip().startswith("Sources:"):
                    continue                      # drop old Sources line (rebuilt below)
                s = CIT_WRAPPER.sub("", l).rstrip()
                if s.strip() == "" and l.strip() != "":
                    continue                      # drop citation-only line
                rebuilt.append(s)
            content = rebuilt
            while content and content[-1].strip() == "":
                content.pop()

        if want:
            out.append(f"<!-- {want} -->")
        out.append(head_line)
        out.extend(content)
        if toks and not has_table:
            out.append("")
            out.append("Sources: " + " ".join(toks))
        if trailing_sep:
            out.append("")
            out.append("---")
        out.append("")

    new_body = "\n".join(out)
    new_body = re.sub(r"\n{3,}", "\n\n", new_body).rstrip() + "\n"
    open(path, "w", encoding="utf-8").write(fm + new_body)
    print(f"conformed: {path}")


# ------------------------------------------------------------------- guard --
# Advisory drift-detection for the protected source-of-truth files. Not
# enforcement: it cannot stop an edit, only make an unauthorized one loud.

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
# vault root = 4-SYSTEM/scripts/day-package/ -> up three levels
VAULT_ROOT = os.path.abspath(os.path.join(SCRIPT_DIR, "..", "..", ".."))
GUARD_PATHS = os.path.join(SCRIPT_DIR, "guard.paths")
GUARD_LOCK = os.path.join(SCRIPT_DIR, "guard.lock")


def _protected_files():
    """Expand guard.paths (globs, relative to vault root) into concrete files."""
    import glob
    files = []
    if not os.path.exists(GUARD_PATHS):
        return files
    for line in open(GUARD_PATHS, encoding="utf-8"):
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        for p in sorted(glob.glob(os.path.join(VAULT_ROOT, line))):
            if os.path.isfile(p):
                files.append(os.path.relpath(p, VAULT_ROOT))
    return sorted(set(files))


def _sha256(rel):
    with open(os.path.join(VAULT_ROOT, rel), "rb") as fh:
        return hashlib.sha256(fh.read()).hexdigest()


def _load_lock():
    lock = {}
    if os.path.exists(GUARD_LOCK):
        for line in open(GUARD_LOCK, encoding="utf-8"):
            line = line.rstrip("\n")
            if not line or line.startswith("#"):
                continue
            h, _, rel = line.partition("  ")
            lock[rel] = h
    return lock


def guard_record():
    files = _protected_files()
    with open(GUARD_LOCK, "w", encoding="utf-8") as fh:
        fh.write("# guard.lock — sha256 baseline of protected source-of-truth files.\n")
        fh.write("# Regenerate ONLY after an approved change: `guard record`.\n")
        for rel in files:
            fh.write(f"{_sha256(rel)}  {rel}\n")
    print(f"recorded {len(files)} protected files -> {os.path.relpath(GUARD_LOCK, VAULT_ROOT)}")
    return 0


def guard_check():
    lock = _load_lock()
    current = {rel: _sha256(rel) for rel in _protected_files()}
    changed = [r for r in current if r in lock and current[r] != lock[r]]
    missing = [r for r in lock if r not in current]        # moved/deleted/renamed
    added = [r for r in current if r not in lock]          # new protected file, not yet baselined
    for r in changed:
        print(f"  CHANGED: {r}")
    for r in missing:
        print(f"  MISSING (moved/deleted?): {r}")
    for r in added:
        print(f"  warning: untracked protected file (run `guard record`): {r}")
    if not lock:
        print("[guard] no baseline yet — run `guard record` first.")
        return 1
    if changed or missing:
        print(f"[guard] DRIFT DETECTED — {len(changed)} changed, {len(missing)} missing. "
              f"If unauthorized, restore from version control; if approved, re-run `guard record`.")
        return 1
    print(f"[guard] OK — {len(current)} protected files match the baseline.")
    return 0


# --------------------------------------------------------------------- main --

def main(argv):
    if len(argv) >= 2 and argv[1] == "guard":
        mode = argv[2] if len(argv) >= 3 else ""
        if mode == "record":
            return guard_record()
        if mode == "check":
            return guard_check()
        print("usage: day_package_tools.py guard [record|check]")
        return 2
    if len(argv) < 3 or argv[1] not in ("validate", "conform"):
        print(__doc__)
        return 2
    cmd, files = argv[1], argv[2:]
    ok = True
    for f in files:
        if cmd == "validate":
            ok = validate(f) and ok
        else:
            conform(f)
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))

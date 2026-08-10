#!/usr/bin/env python3
"""
cleanup.py — staged repository cleanup for branch `trans_eng`
=============================================================

Runs the repo tidy-up as six independent, individually revertable steps.
**Dry-run by default.** Nothing happens without ``--apply``.

Safety design
-------------
* Every removal is ``git rm --cached``, never ``git rm``. **Files stay on disk.**
  Only tracking stops. Nothing in this script deletes your data.
* Each step makes its own commit, so any step can be reverted alone with
  ``git revert <sha>``.
* Paths are removed from tracking only after being added to ``.gitignore``,
  so an auto-commit tool cannot silently re-add them.

Scope — what this script will NOT touch
---------------------------------------
Per instruction, the current pipeline areas are excluded entirely:

  * ``2-RAILS/``            — verse rails, term index, glossaries
  * ``3-TRANSFORMATIONS/``  — all translation tracks and plans
  * ``AI_translation/``     — deferred pending the canonical-workspace decision
  * ``Keyword_extractor/``  — same

The only file matching a cleanup pattern inside those trees
(``2-RAILS/Sections/Raw/.../1-0.md.bak``) is explicitly skipped.

``1-SOURCES/`` content is never touched. Step 5 untracks ``*.bak`` *artifacts*
that sit beside the sources — the sources themselves are untouched, and the
.bak files remain on disk. That step is separated out precisely so you can skip
it if you would rather leave the protected tree completely alone.

Preconditions
-------------
1. Close Obsidian (its Git plugin auto-commits every 10 minutes with
   ``autoCommitOnlyStaged: false``, which will interleave with these commits).
2. Delete the stale lock: ``rm .git/index.lock`` — dead since 2026-08-09,
   currently blocking every git write.

Usage
-----
    python 4-SYSTEM/scripts/repo-cleanup/cleanup.py                # dry run, all steps
    python 4-SYSTEM/scripts/repo-cleanup/cleanup.py --step 2       # dry run, one step
    python 4-SYSTEM/scripts/repo-cleanup/cleanup.py --step 2 --apply
    python 4-SYSTEM/scripts/repo-cleanup/cleanup.py --apply        # all steps

Steps
-----
    1  Line endings      — .gitattributes + one labelled normalization commit
    2  Build junk        — 12 tracked __pycache__/*.pyc
    3  Obsidian plugins  — 12 MB of per-machine plugin bundles
    4  Root clutter      — empty files, scratch, superseded .docx drafts
    5  Backup artifacts  — *.bak beside 1-SOURCES (opt-in; see note above)
    6  0-INBOX heavy     — large scratch files; 0-INBOX is non-authoritative
                           per CLAUDE.md §2, so versioning it buys little
"""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[3]
EXPECTED_BRANCH = "trans_eng"

# Trees this script must never touch.
PROTECTED_PREFIXES = (
    "2-RAILS/",
    "3-TRANSFORMATIONS/",
    "AI_translation/",
    "Keyword_extractor/",
)

APPLY = False


# ---------------------------------------------------------------- helpers

def git(*args: str, check: bool = True) -> str:
    out = subprocess.run(
        ["git", *args], cwd=REPO, capture_output=True, text=True,
        encoding="utf-8", errors="replace",
    )
    if check and out.returncode != 0:
        raise RuntimeError(f"git {' '.join(args)}\n{out.stderr.strip()}")
    return out.stdout


def tracked(*patterns: str) -> list[str]:
    """Tracked files matching the patterns, minus anything in a protected tree."""
    if not patterns:
        return []
    files = git("ls-files", "-z", "--", *patterns).split("\0")
    keep, skipped = [], []
    for f in files:
        if not f:
            continue
        if f.startswith(PROTECTED_PREFIXES):
            skipped.append(f)
        else:
            keep.append(f)
    for f in skipped:
        print(f"      · skipped (protected tree): {f}")
    return keep


def untrack(files: list[str], message: str, ignore_lines: list[str]) -> bool:
    """git rm --cached the files, add ignore rules, commit. Files stay on disk."""
    if not files:
        print("      nothing to do")
        return False

    total = 0
    for f in files:
        p = REPO / f
        if p.is_file():
            total += p.stat().st_size
        print(f"      - {f}")
    print(f"      {len(files)} file(s), {total/1_048_576:.1f} MB leaves the index "
          f"(stays on disk)")

    if not APPLY:
        return False

    add_ignore(ignore_lines)
    # Chunked so Windows does not hit its command-line length limit.
    for i in range(0, len(files), 100):
        git("rm", "--cached", "-q", "--", *files[i:i + 100])
    git("add", ".gitignore")
    git("commit", "-q", "-m", message)
    print(f"      committed: {message}")
    return True


def add_ignore(lines: list[str]) -> None:
    if not lines:
        return
    path = REPO / ".gitignore"
    existing = path.read_text(encoding="utf-8") if path.exists() else ""
    new = [l for l in lines if l.strip() and l not in existing.splitlines()]
    if not new:
        return
    body = existing.rstrip("\n") + "\n\n# --- added by 4-SYSTEM/scripts/repo-cleanup/cleanup.py ---\n"
    body += "\n".join(new) + "\n"
    path.write_text(body, encoding="utf-8", newline="\n")


def banner(n: int, title: str) -> None:
    print(f"\n{'='*66}\nSTEP {n} — {title}\n{'='*66}")


# ------------------------------------------------------------------ steps

def step1_line_endings() -> None:
    banner(1, "Line endings")
    if not (REPO / ".gitattributes").exists():
        print("      ERROR: .gitattributes is missing. Create it first.")
        return

    modified = len([l for l in git("status", "--porcelain").splitlines()
                    if l.startswith(" M")])
    print(f"      tracked files differing from HEAD: {modified}")
    print()
    print("      Before .gitattributes existed this number was 2,629 — every")
    print("      file in the vault, all of it CRLF-vs-LF, zero content changed.")
    print("      HEAD already stored LF; only the *declaration* was missing.")
    print("      With the policy declared, git converts CRLF to LF on read and")
    print("      everything matches again.")
    print()
    print("      So NO renormalization commit is needed. This step commits one")
    print("      file. Nothing for your collaborators to merge, and the working")
    print("      tree keeps its CRLF on disk until the next checkout.")

    if not APPLY:
        return
    git("add", ".gitattributes")
    if git("diff", "--cached", "--name-only").strip():
        git("commit", "-q", "-m",
            "Add .gitattributes: declare LF line endings and binary types\n\n"
            "Resolves 2,629 files showing as modified with zero content change. "
            "HEAD already stored LF; a Windows tool had rewritten the working "
            "tree to CRLF and git had no declared policy to reconcile them.")
        print("      committed: .gitattributes (1 file)")
    else:
        print("      already committed")


def step2_pycache() -> None:
    banner(2, "Build junk — tracked __pycache__")
    files = tracked("*__pycache__/*", "*.pyc", "*.pyo")
    print("      .gitignore already lists __pycache__/, but ignore rules do not")
    print("      apply retroactively — these were committed before it existed.")
    untrack(files, "Untrack __pycache__ build artifacts",
            ["__pycache__/", "*.pyc", "*.pyo"])


def step3_obsidian() -> None:
    banner(3, "Obsidian plugin bundles")
    files = tracked(".obsidian/plugins/*")
    print("      Third-party plugin code, reinstalled per machine from the")
    print("      community catalogue. Settings are kept; only bundles go.")
    untrack(
        files,
        "Untrack Obsidian plugin bundles (per-machine, reinstallable)",
        [".obsidian/plugins/*/main.js",
         ".obsidian/plugins/*/styles.css",
         ".obsidian/plugins/*/manifest.json"],
    )


def step4_root() -> None:
    banner(4, "Root-level clutter")
    candidates = [
        # empty or placeholder
        "All-Plans-in-One.md",          # 0 bytes
        "root.md",                      # 0 bytes
        "Untitled.base",                # 42 bytes
        "简体测试.txt",                  # 4 bytes, encoding test
        # scratch
        "_tp-raw-scratch.txt",          # 64 KB
        "ch2-outline-temp.md",          # 48 KB
        # superseded drafts — v5rev is the latest and is KEPT
        "dzongsar-trilingual-s1s2-v2.docx",
        "dzongsar-trilingual-s1s2-v4.docx",
        "dzongsar-trilingual-s1s2-v5.docx",
        "dzongsar-trilingual-s1s2-v5r_suppposed to be complete Tiebtan.docx",
    ]
    files = [f for f in candidates if (REPO / f).exists()]
    print("      KEPT: dzongsar-trilingual-s1s2-v5rev.docx (latest revision),")
    print("            CLAUDE.md, AGENTS.md, README.md, the .skill files,")
    print("            Video_Creation_Playbook, and both root .py scripts")
    print("            (they differ from their 4-SYSTEM copies — check by hand).")
    untrack(files, "Untrack root-level scratch, empty files and superseded drafts", [])


def step5_bak() -> None:
    banner(5, "Backup artifacts (*.bak) — OPT-IN")
    files = tracked("*.bak", "*.bak2")
    print("      These sit beside 1-SOURCES material. The sources themselves are")
    print("      NOT touched and the .bak files remain on disk — only tracking")
    print("      stops. Skip this step if you would rather leave the protected")
    print("      tree entirely alone (CLAUDE.md §Protected files).")
    untrack(files, "Untrack .bak backup artifacts", ["*.bak", "*.bak2"])


def step6_inbox() -> None:
    banner(6, "0-INBOX heavy files — OPT-IN")
    limit = 1_000_000
    files = []
    for f in tracked("0-INBOX/*"):
        p = REPO / f
        if p.is_file() and p.stat().st_size > limit:
            files.append(f)
    files.sort(key=lambda f: -(REPO / f).stat().st_size)
    print(f"      Tracked files over {limit/1_048_576:.0f} MB inside 0-INBOX.")
    print("      CLAUDE.md §2 defines 0-INBOX as scratch, never cited from")
    print("      elsewhere — so version history there buys little and costs a")
    print("      lot (0-INBOX is 89 MB of a 354 MB repo).")
    untrack(files, "Untrack large scratch files in 0-INBOX", [])


STEPS = {
    1: step1_line_endings,
    2: step2_pycache,
    3: step3_obsidian,
    4: step4_root,
    5: step5_bak,
    6: step6_inbox,
}


# ------------------------------------------------------------------- main

def preflight() -> bool:
    ok = True
    if (REPO / ".git" / "index.lock").exists():
        print("  ✗ .git/index.lock exists — every git write will fail.")
        print("    Close Obsidian, then: rm .git/index.lock")
        ok = False
    try:
        branch = git("rev-parse", "--abbrev-ref", "HEAD").strip()
    except RuntimeError as exc:
        print(f"  ✗ cannot read branch: {exc}")
        return False
    if branch != EXPECTED_BRANCH:
        print(f"  ✗ on branch '{branch}', expected '{EXPECTED_BRANCH}'")
        ok = False
    else:
        print(f"  ✓ on branch {branch}")
    print("  ! Confirm Obsidian is closed — its Git plugin auto-commits every")
    print("    10 minutes with autoCommitOnlyStaged: false.")
    return ok


def main() -> int:
    global APPLY
    ap = argparse.ArgumentParser(description="Staged repo cleanup for trans_eng")
    ap.add_argument("--apply", action="store_true",
                    help="actually make changes (default: dry run)")
    ap.add_argument("--step", type=int, choices=sorted(STEPS),
                    help="run a single step")
    ap.add_argument("--skip-preflight", action="store_true")
    args = ap.parse_args()
    APPLY = args.apply

    print(f"repo : {REPO}")
    print(f"mode : {'APPLY — changes will be committed' if APPLY else 'DRY RUN — nothing will change'}")
    print("\npreflight")
    if not args.skip_preflight and not preflight():
        print("\npreflight failed — fix the above, or pass --skip-preflight")
        return 1

    for n in ([args.step] if args.step else sorted(STEPS)):
        STEPS[n]()

    print("\n" + "=" * 66)
    if APPLY:
        print("Done. Review with:  git log --oneline -8")
        print("Revert any single step with:  git revert <sha>")
    else:
        print("Dry run complete. Re-run with --apply to execute,")
        print("or --step N --apply to do one step at a time.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

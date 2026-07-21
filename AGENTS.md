# AGENTS.md — instructions for AI agents in this repository

1. **Read `4-SYSTEM/CLAUDE.md` in full before doing anything.** It holds the operational rules, folder write-permissions, and the skill-lookup step for this vault.

2. 🔒 **Protected files — confirm before touching.** Several practice-plan *day-package* files are source-of-truth: downstream tools pull plan content directly from them. Do **not** edit, move, rename, or delete any file that is marked `PROTECTED — SOURCE OF TRUTH` (a banner at the top of the file, and `protected: true` in its frontmatter) **without explicit human confirmation**. State the file and the exact change, and wait for approval first.

   The full policy and the protected-file list live in `4-SYSTEM/CLAUDE.md` → "Protected files", and the machine-readable globs are in `4-SYSTEM/scripts/day-package/guard.paths`. To check whether any protected file has been changed without approval:

   ```
   python3 4-SYSTEM/scripts/day-package/day_package_tools.py guard check
   ```

This file exists because some AI tools read `AGENTS.md` rather than `CLAUDE.md`. Both point to the same rules.

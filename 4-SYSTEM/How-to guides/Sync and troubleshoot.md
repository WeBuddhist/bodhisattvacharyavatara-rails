# Sync and troubleshoot

How the vault keeps everyone's edits in sync, how to save on demand, and what to do when something goes wrong.

## How sync works

Every 10 minutes, the Obsidian Git plugin does two things:

- **Pulls** — downloads any changes your teammates have made.
- **Saves and uploads** — records your changes (called a *commit*) and sends them up to GitHub (called a *push*).

It also pulls when you first open Obsidian, so you start with the latest copy of the vault.

If two people edit the same line of the same note at the same time, Git won't know which version to keep. This is called a **merge conflict**. Obsidian Git will mark the conflicting lines in the file with special symbols. You can pick the version you want, delete the rest, and save the file.

## Saving on demand

If you don't want to wait 10 minutes (for example, you just finished a big edit and want your teammates to see it now), you can save manually.

- Click the **Source Control View** icon in the left ribbon to open the Git panel on the right side of Obsidian. From there, you can pick which files to save, type a short message about the change, and click to save and upload.
- Or, open Obsidian's command palette by pressing `Cmd + P` (Mac) or `Ctrl + P` (Windows). Type "create backup" and choose **Obsidian Git: Create backup**. This saves and uploads everything in one step.

## Troubleshooting

- **Obsidian Git isn't enabled** — go to **Settings → Community plugins** and check that **Obsidian Git** is turned on. If you don't see it in the list, click **Browse** and install it.
- **Nothing is syncing** — open the command palette (`Cmd + P` on Mac, `Ctrl + P` on Windows) and run **Obsidian Git: Check repository status**. The bar at the bottom of Obsidian also shows the current branch and sync status.
- **You see an authentication error when saving** — run `gh auth login` again to reconnect your GitHub account. If that doesn't work, you can [set up an SSH key](https://docs.github.com/en/authentication/connecting-to-github-with-ssh) instead.

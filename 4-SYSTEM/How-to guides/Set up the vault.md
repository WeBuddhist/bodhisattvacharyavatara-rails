# Set up the vault

This guide walks you through getting the vault running on your own computer. You only need to do this once. After setup, Obsidian will sync everyone's changes automatically every 10 minutes.

---

## 1. Install Obsidian

Download Obsidian from [obsidian.md](https://obsidian.md) and install it. It's free and works on Mac, Windows, and Linux.

---

## 2. Get access to the GitHub repo

Ask the vault administrator to add you to the GitHub repository for this vault. You'll need a [GitHub account](https://github.com/join) if you don't have one.

---

## 3. Install Git and connect your GitHub account

You only do this once per computer. Git is the tool Obsidian uses to sync the vault.

### Mac

1. Open Terminal. (Press `Cmd + Space`, type "Terminal", and press Return.)
2. Type `git --version` and press Return. If Git isn't installed, your Mac will ask if you want to install the Xcode Command Line Tools — click **Install** and wait for it to finish.
3. Tell Git who you are (this name and email will appear next to every change you save):
   ```
   git config --global user.name "Your Name"
   git config --global user.email "you@example.com"
   ```
4. Connect your GitHub account. Install [GitHub CLI](https://cli.github.com/) by running:
   ```
   brew install gh
   ```
   If Terminal says `command not found: brew`, install Homebrew first:
   ```
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   ```
   Follow the "Next steps" it shows you at the end. Then run `brew install gh` again.

   Once GitHub CLI is installed, run:
   ```
   gh auth login
   ```
   Choose **GitHub.com → HTTPS → Login with a web browser** and follow the steps. After this, GitHub won't ask for your password again.

### Windows

1. Install [Git for Windows](https://git-scm.com/download/win). Keep the default settings during installation.
2. Open Git Bash (or PowerShell) and tell Git who you are:
   ```
   git config --global user.name "Your Name"
   git config --global user.email "you@example.com"
   ```
3. Install [GitHub CLI](https://cli.github.com/), then run:
   ```
   gh auth login
   ```
   Choose **GitHub.com → HTTPS → Login with a web browser** and follow the steps.

---

## 4. Clone the repo onto your computer

This downloads a copy of the vault from GitHub to your computer. The technical word for this is *cloning*.

**First, decide where the vault should live.** Create a folder for it — for example, a folder named after the project inside your Documents folder.

**Navigate there in the Terminal:**

*Mac* — Type `cd ` (c-d followed by one space), then **drag the folder from Finder onto the Terminal window**. Terminal will paste the path for you. Press Return.

*Windows* — In PowerShell or Git Bash, type `cd ` and paste the path to the folder.

**Copy the repo's link from GitHub.** On the repo's GitHub page, click the green **Code** button and copy the HTTPS link.

**Clone the repo:**
```
git clone https://github.com/<org>/<repo-name>.git
```

This creates a new subfolder inside the folder you chose, with the vault's contents inside.

---

## 5. Open the vault in Obsidian

1. Open Obsidian.
2. In the menu, choose **File → Open Vault**.
3. Click **Open** next to **Open folder as vault**.
4. Choose the folder that was just created by `git clone`.

Or if you already have another vault open:

1. Click the vault name in the bottom-left corner of the Obsidian window.
2. Choose **Manage Vaults**.
3. Click **Open** next to **Open folder as vault** and choose the cloned folder.

---

## 6. Trust the author and close the plugin window

The first time you open the vault, Obsidian will warn you about community plugins. This is because the Obsidian Git plugin comes pre-installed.

1. Click **Trust author & enable plugins**.
2. Obsidian will open the Community plugins window. The Git plugin is already installed and on — just **close the window** to see your vault.

That's it. The vault will now sync your changes and pull your teammates' changes automatically every 10 minutes.

---

## Troubleshooting

- **Obsidian Git isn't enabled** — go to **Settings → Community plugins** and check that **Obsidian Git** is turned on. If it's not in the list, click **Browse** and install it.
- **Nothing is syncing** — open the command palette (`Cmd + P` on Mac, `Ctrl + P` on Windows) and run **Obsidian Git: Check repository status**.
- **Authentication error** — run `gh auth login` again to reconnect your GitHub account.

See also:
- [Sync and troubleshoot](Sync%20and%20troubleshoot.md)
- [How to Fix Git Merge Conflicts in Obsidian](How%20to%20Fix%20Git%20Merge%20Conflicts%20in%20Obsidian.md)
- [Solving the Obsidian Git workspace.json Tracking Issue](Solving%20the%20Obsidian%20Git%20workspace.json%20Tracking%20Issue.md)

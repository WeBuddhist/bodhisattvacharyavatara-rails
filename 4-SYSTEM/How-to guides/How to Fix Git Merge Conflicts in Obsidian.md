
This guide explains how to resolve the `unresolved conflict`error when syncing your Obsidian vault with Git.

---

Why this happens

`data.json`

---

Method 1: Using the Terminal (Recommended)

Open your terminal or command prompt in your vault's root folder and choose **one** of the options below.

Option A: Keep your current local settings

Run these commands to overwrite the incoming changes with your current plugin settings:

bash

```
git checkout --ours .obsidian/plugins/gemini-scribe/data.json
git add .obsidian/plugins/gemini-scribe/data.json
git commit -m "Fix conflict using local settings"
```

Please use code with caution.

Option B: Accept the incoming settings

Run these commands to overwrite your local settings with the incoming changes from the remote repository:

bash

```
git checkout --theirs .obsidian/plugins/gemini-scribe/data.json
git add .obsidian/plugins/gemini-scribe/data.json
git commit -m "Fix conflict using remote settings"
```

Please use code with caution.

Option C: Reset and start over

bash

```
git merge --abort
```

Please use code with caution.

---

Method 2: Using the Obsidian Git Plugin UI

If you use the **Obsidian Git** community plugin inside Obsidian, follow these steps:

1. Open the **Command Palette** (`Ctrl + P` on Windows/Linux, `Cmd + P` on Mac).
2. Type `Obsidian Git: Open source control view` and press enter.
3. Look for the `data.json` file under the **Conflicts** section.
4. Right-click (or click the icon next to) the file.
5. Select **Change version to local (ours)** or **Change version to remote (theirs)**.
6. Commit and push your changes using the source control sidebar.

---

Method 3: Prevent future conflicts

Plugin settings change constantly and do not need to be tracked. Prevent this error from happening again by adding them to your ignore list.

1. Open the `.gitignore`file in your main vault folder.
2. Add this line to the bottom of the file:
    
    text
    
    ```
    .obsidian/plugins/*/data.json
    ```
    
    Please use code with caution.
    
3. Save the file.

---

Obsidian updates `workspace.json` every time you open notes or change layouts. If you added this file to `.gitignore` but it still appears in your Git changes, Git is already tracking it. A `.gitignore` file cannot ignore files that are already part of your repository history.

## Follow this guide to stop tracking the file without losing your local layout settings.

---

#### Step 1: Open Your Terminal

1. Open your terminal or command prompt.
2. Navigate to your Obsidian vault root directory.
    
    bash
    
    ```
    cd /path/to/your/obsidian/vault
    ```
    
    Use code with caution.
    

#### Step 2: Remove the File From Git Index

Run the following command to tell Git to stop tracking the file. This deletes the file from Git's memory but **keeps the file safe on your computer**.

- **For Desktop:**
    
    bash
    
    ```
    git rm --cached .obsidian/workspace.json
    ```
    
    Use code with caution.
    
- **For Mobile (Optional):**
    
    bash
    
    ```
    git rm --cached .obsidian/workspace-mobile.json
    ```
    
    Use code with caution.
    

#### Step 3: Update Your `.gitignore`

Ensure your `.gitignore` file explicitly lists these paths. Open your `.gitignore` file in a text editor and add the following lines:

text

```
.obsidian/workspace.json
.obsidian/workspace-mobile.json
```

Use code with caution.

#### Step 4: Commit and Push the Changes

Commit the tracking removal and push the update to your remote repository (e.g., GitHub).

bash

```
git add .gitignore
git commit -m "chore: stop tracking obsidian workspace settings"
git push
```

Use code with caution.

---

Result

- **Remote Repository:** The `workspace.json` file will disappear from your remote GitHub/GitLab repository.
- **Local Vault:** The file stays on your computer. Your open tabs and sidebar layouts remain intact.
- **Future Commits:** Git will completely ignore all future changes to your workspace layout.
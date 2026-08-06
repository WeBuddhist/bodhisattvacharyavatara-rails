# Setup script — create the board with the gh CLI

Run once the drafts are approved. Requires `gh` authenticated with `project` scope:
`gh auth refresh -s project,repo`

Set these first:

```bash
OWNER="<your-github-user-or-org>"     # e.g. OpenPecha
REPO="$OWNER/<repo-name>"             # repo where issues live
TITLE="Text Processing Pipeline"
```

## 1 · Create the project + status columns

```bash
gh project create --owner "$OWNER" --title "$TITLE"
PROJECT=$(gh project list --owner "$OWNER" --format json \
  | jq -r ".projects[] | select(.title==\"$TITLE\") | .number")

# The default Status field ships with Todo/In Progress/Done.
# Edit its options in the UI (Project → Settings → Status) to:
#   Backlog | 1 · Sources: Root Text | 1 · Sources: Translations & Commentaries |
#   2 · Rails: Sections & Verses | 2 · Rails: Claims & Wiki | 3 · Transformations | Done
# (Single-select option editing is UI-only; the CLI can't rename Status options.)

# Extra fields:
gh project field-create $PROJECT --owner "$OWNER" --name "Priority" \
  --data-type SINGLE_SELECT --single-select-options "P0,P1,P2"
gh project field-create $PROJECT --owner "$OWNER" --name "Target" --data-type DATE
gh project field-create $PROJECT --owner "$OWNER" --name "Languages" --data-type TEXT
```

## 2 · Create labels

```bash
while IFS='|' read -r name color desc; do
  gh label create "$name" --repo "$REPO" --color "$color" --description "$desc" --force
done <<'EOF'
text|1D76DB|Parent card: one text moving across the board
artifact|BFDADC|Sub-issue: one pipeline artifact
stage:sources|0E8A16|Stage 1 - Sources
stage:rails|FBCA04|Stage 2 - Rails
stage:transformations|D93F0B|Stage 3 - Transformations
root-text|C2E0C6|Root text (Sanskrit/Tibetan editions)
translations|C2E0C6|Existing human translations
commentaries|C2E0C6|Commentaries
sections|FEF2C0|Sections / TOC / summaries
verses|FEF2C0|Per-verse compilations
claims|FEF2C0|Claims extraction & consolidation
local-wiki|FEF2C0|Keyword lists & wiki articles
plans|F9D0C4|Transformation: plans
translation-out|F9D0C4|Transformation: translations
video|F9D0C4|Transformation: short videos
elearning|F9D0C4|Transformation: e-learning
blocked|B60205|Blocked
needs-review|5319E7|Needs human review
tooling|EDEDED|Pipeline/script work not tied to one text
EOF
```

## 3 · Create issues for a text

For each text, create the parent, then the 15 sub-issues, then attach them.
(Bodies: paste from `01-issues-bodhicharyavatara.md` / `02-new-text-template.md`, or keep them in a `drafts/` folder as files and pass `--body-file`.)

```bash
TEXT="Bodhicharyavatara"

PARENT_URL=$(gh issue create --repo "$REPO" --label text \
  --title "[TEXT] $TEXT" --body-file "drafts/$TEXT/parent.md")
PARENT_NUM=${PARENT_URL##*/}
gh project item-add $PROJECT --owner "$OWNER" --url "$PARENT_URL"

# Sub-issues (repeat per S1..T4; labels per the template table):
SUB_URL=$(gh issue create --repo "$REPO" \
  --label artifact --label "stage:sources" --label "root-text" \
  --title "S1 [$TEXT] Sanskrit root text: source high-quality edition + assign IDs" \
  --body-file "drafts/$TEXT/S1.md")
SUB_NUM=${SUB_URL##*/}

# Link as a native sub-issue (GraphQL; no CLI subcommand yet):
PARENT_ID=$(gh api repos/$REPO/issues/$PARENT_NUM --jq .node_id)
SUB_ID=$(gh api repos/$REPO/issues/$SUB_NUM --jq .node_id)
gh api graphql -f query='
  mutation($parent: ID!, $child: ID!) {
    addSubIssue(input: {issueId: $parent, subIssueId: $child}) {
      issue { number }
    }
  }' -f parent="$PARENT_ID" -f child="$SUB_ID"
```

> When we run this for real, I'll generate a full non-interactive script that loops over all 15 sub-issues per text with their exact titles, labels, and body files — the above shows the mechanism.

## 4 · Board views

Views are UI-only:
1. **Pipeline** — Board layout, group by Status, filter `label:text`
2. **Work detail** — Table layout, all issues, group by Parent issue
3. Enable workflows: *Item added → Backlog*, *Item closed → Done*

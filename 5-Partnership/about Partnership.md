# 🌐 Managing Partnerships in Obsidian

This document serves as the central guide and playbook for how our organization approaches, tracks, and nurtures partnerships. Use this guide to understand our partnership lifecycle, relationship ownership responsibilities, and how to leverage Obsidian to keep our collaborative efforts organized.

## 🧭 The Core Philosophy of Our Partnerships

A successful partnership is built on transparency, clear alignment of mutual value, and rigorous follow-through. We track partnerships in Obsidian to ensure that:

1. **No commitment is forgotten:** We hold ourselves and our partners accountable to what was promised.
2. **Context is preserved:** Anyone in the organization can open a partner's markdown file and instantly understand the relationship history, current lead, and next steps.
3. **Smooth transitions:** If a relationship lead changes, the new owner can seamlessly step in without losing critical background context.

## 🚦 Partnership Lifecycle Stages

We categorize our partnerships into four key statuses. These align with the `status` field in your `partnership_template.md` frontmatter:

### 💡 1. Potential (`#status/potential`)

- **Definition:** An organization we have recently initiated contact with, or who has reached out to us, where mutual interest is being explored.
- **Goal:** Determine alignment, establish key contacts, and define what a mutual collaboration could look like.
- **Exit Criteria:** Moves to _Active_ once formal agreements/commitments are made, or _Inactive_ if there is no immediate fit.
    

### 🚀 2. Active (`#status/active`)

- **Definition:** A live partnership with active projects, shared workflows, or reciprocal commitments currently underway.
- **Goal:** Execute on promises, maintain regular communication, and maximize the mutual value of the relationship.
- **Review Cycle:** Active partners should be reviewed or contacted at least once every 30 to 45 days.
    

### ⏸️ 3. Paused (`#status/paused`)

- **Definition:** An established partner where collaboration is temporarily on hold due to bandwidth, changing priorities, or project-specific timelines.
- **Goal:** Keep the relationship warm without active overhead, ready to reactivate when conditions allow.

### 🛑 4. Inactive (`#status/inactive`)

- **Definition:** A relationship that did not materialize, has reached its natural conclusion, or was mutually ended.
- **Goal:** Keep the file as historical archive. Do not delete, as the historical context of "why it didn't work" or "who we talked to" remains highly valuable.

## 👤 Key Roles & Responsibilities

Every partnership file must have two roles clearly assigned:

### 1. Relationship Owner (Internal Lead)

- **Who they are:** The single point of contact on our side responsible for maintaining the health of the relationship.
- **Responsibilities:**
    - Keeping the partner's `.md` file updated in Obsidian.
    - Ensuring next steps are executed on time.
    - Driving internal teams to deliver on **"What Was Promised From Our Side"**.
    - Monitoring and politely holding the partner accountable for **"What Was Promised From Their Side"**.

### 2. First Contacted By

- **Who they are:** The person who initially opened the door (either outbound outreach or handling an inbound inquiry).
- **Why it matters:** Even if they aren't the current owner, they hold the initial rapport and historical context of how the connection was established, which can be useful to re-leverage in the future.
    

## 🛠️ Supercharging Obsidian (Dataview Queries)

If you install the **Dataview** community plugin in Obsidian, you can paste the following code blocks into a central dashboard note (e.g., `Partnership Dashboard.md`) to automatically aggregate and display your partner data.

### 🔍 View All Active Partnerships

```
TABLE relationship_lead AS "Owner", last_contacted AS "Last Contact"
FROM #partner-tracking
WHERE status = "active"
SORT last_contacted DESC
```

### 💡 View Potential Partnerships & Leads

```
TABLE relationship_lead AS "Owner", initial_contact_by AS "First Contact"
FROM #partner-tracking
WHERE status = "potential"
```

### ⚠️ Missing Relationship Leads (Cleanup Query)

Use this query to find any partner file that doesn't have an owner assigned:

```
TABLE status
FROM #partner-tracking
WHERE !relationship_lead or relationship_lead = ""
```

## 📝 Best Practices for Updating Files

- **Update after every call:** Spend 3 minutes immediately following a partner call to append a bullet point to the `Discussions & History` section and update the `last_contacted` frontmatter date.
    
- **Use Checklist Items (`[ ]`):** Use standard markdown checklists for promises. This allows you to check them off as completed, giving an instant visual status of outstanding commitments.
    
- **Link liberally:** Use internal Obsidian links `[[Like This]]` to link partner files to relevant internal projects, meeting notes, or task lists.
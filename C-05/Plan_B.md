# C5-3 Step 3 — Plan B Ready

## Late Work Management System

---

# 1. Design Risks and Contingencies

## Risk 1 — Overly Complex Status Update System

### Risk

The one-click status system (Missing → Late → Submitted) may become too complex to implement reliably, especially if multiple updates happen simultaneously or if data conflicts occur.

### Contingency Plan

* Replace real-time multi-button updates with a **single dropdown selector**
* Add a **“Save Changes” confirmation button** to reduce accidental overwrites
* Store updates in a simple local state first before syncing to database

### Backup Design

If the button-based system fails:

* Use a **table-based edit system** where each row has a status dropdown
* Remove animations or live updates to reduce system load

---

## Risk 2 — Search Function Performance Issues

### Risk

Real-time search filtering may become slow or laggy if the dataset grows large (e.g. many students or assignments).

### Contingency Plan

* Switch from “live filtering on every keystroke” to a **submit-based search (press Enter)**
* Limit search scope to **student names only (not full assignment metadata)**
* Implement basic caching of filtered results

### Backup Design

* Replace dynamic search with:

  * A **dropdown student selector**
  * Or a **paginated student list (A–F, G–L, etc.)**

---

## Risk 3 — Notification System Not Supported in Final Tech Stack

### Risk

Automatic reminder notifications for overdue “Missing” work may not be supported depending on the final implementation environment (e.g. Python GUI limitations or no background scheduler).

### Contingency Plan

* Replace automatic alerts with a **manual “Check Overdue Work” button**
* Generate a **daily summary report panel instead of push notifications**
* Use timestamp comparison only when dashboard is opened

### Backup Design

* Add a **visual warning badge system instead of pop-ups**

  * Example: red dot next to overdue students
* Keep all alerts **passive (on-screen only)** instead of automated

---

## Risk 4 — UI Too Dense for Teachers During Marking

### Risk

Teachers may find the dashboard overwhelming if too many statuses, colours, and actions are displayed at once.

### Contingency Plan

* Introduce a **“Simple View / Advanced View toggle”**
* Simple View shows only:

  * Student name
  * Status
  * One action button
* Advanced View shows full metadata and history

### Backup Design

* If toggle system is too complex:

  * Default to **minimalist dashboard only**
  * Move detailed history into a separate “Student Profile” page

---

## Risk 5 — Data Inconsistency Between Status Updates

### Risk

Teachers might update status incorrectly (e.g. marking “Submitted” when it should be “Late”), leading to inaccurate records.

### Contingency Plan

* Enforce **dropdown-only input (no free text)**
* Add a **confirmation prompt before saving status changes**
* Log every change with timestamp and previous value

### Backup Design

* If logging system becomes too complex:

  * Store only **current status (no history tracking)**
  * Prioritise simplicity over full audit trail

---

# 2. Summary of Contingency Strategy

Across all risks, the fallback philosophy is:

* **Simplify interaction before removing features**
* Replace automation with **manual but reliable alternatives**
* Prioritise **teacher usability over technical complexity**
* Always maintain at least a **basic working version of every feature**

---

# Key Design Insight

This system is designed so that:

* If advanced features fail → a **simpler but functional version still works**
* No feature is “single-point-of-failure”
* Every complex idea has a **low-tech fallback equivalent**

---

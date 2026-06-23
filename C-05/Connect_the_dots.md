# Connect the Dots

## Late Work Management System

---

# 1. Design Annotations (What appears on your mockups)

These are notes you would place directly on your UI sketches or wireframes.

### Dashboard / Home Screen

* “Search bar at top → allows fast filtering of students by name (reduces time spent scrolling)”
* “Status cards (Missing / Late / Submitted) → visually separates workload into clear categories”
* “Colour coding (red = missing, orange = late, green = submitted) → quick visual scanning for teachers”
* “One-click status button → reduces Canvas multi-step workflow to a single action”
* “Student list sorted by urgency → ensures missing work appears first”

---

### Student Detail View

* “Assignment timeline → shows progression from Missing → Late → Submitted”
* “Edit status dropdown instead of free text → prevents inconsistent data entry”
* “Timestamp display → helps track when work was updated (supports accountability)”

---

### Notification Panel

* “Auto-alert banner → reminds teacher when work is still marked ‘Missing’ after submission”
* “Daily summary → reduces cognitive load by grouping updates instead of constant alerts”

---

# 2. Links to SRS Requirements

(You can adjust FR/NFR numbers to match your document — these are aligned to your system description)

| Design Element                        | Requirement (SRS ref)                           | Justification                                |
| ------------------------------------- | ----------------------------------------------- | -------------------------------------------- |
| Search bar on dashboard               | FR-1: Teachers can locate students quickly      | Reduces time to find student records         |
| Status cards (Missing/Late/Submitted) | FR-2: System must track assignment status       | Makes workflow states visible and structured |
| Colour-coded statuses                 | NFR-3: Usability (quick interpretation of data) | Supports rapid scanning without reading text |
| One-click status update button        | FR-3: Teachers can update submission status     | Fixes Canvas issue of multi-step updates     |
| Student timeline view                 | FR-4: System records submission history         | Ensures tracking of changes over time        |
| Auto reminder notifications           | NFR-2: Reliability (reduce missed updates)      | Prevents forgotten status changes            |
| Dropdown status selector              | NFR-3: Usability + data consistency             | Prevents incorrect manual input              |

---

# 3. Traceability Path (Idea → Design → Implementation)

This shows how your ideas evolve into your final system.

---

## Example 1 — Status Management System

**Idea (from Step 1 research):**
Canvas is powerful but requires too many steps to update submission status.

⬇

**Mockup Design:**
One-click status buttons (Missing / Late / Submitted)

⬇

**Data Dictionary Entry:**

* Field: `submission_status`
* Type: Enum
* Values: Missing, Late, Submitted

⬇

**IPO Chart:**

* Input: Teacher selects student + status
* Process: Update record in system
* Output: Updated dashboard view

⬇

**Pseudocode:**

```plaintext
IF buttonClicked = "Late"
    THEN update student.status = "Late"
    SAVE changes
    refresh dashboard
```

---

## Example 2 — Search Function

**Idea:**
Google Classroom shows that simple search improves navigation speed.

⬇

**Mockup Design:**
Top-of-page search bar filtering student list in real time

⬇

**Data Dictionary Entry:**

* Field: `student_name_search`
* Type: String input filter

⬇

**IPO Chart:**

* Input: Text entered by teacher
* Process: Filter dataset by matching names
* Output: Updated filtered list

⬇

**Pseudocode:**

```plaintext
FOR each student in list
    IF student.name contains searchText
        DISPLAY student
    ELSE hide student
```

---

## Example 3 — Reminder System

**Idea:**
Microsoft Teams uses notifications to prevent missed tasks.

⬇

**Mockup Design:**
Notification panel showing overdue “Missing” assignments

⬇

**Data Dictionary Entry:**

* Field: `reminder_flag`
* Type: Boolean
* Trigger: status = Missing for > X days

⬇

**IPO Chart:**

* Input: Time + status data
* Process: Check overdue conditions
* Output: Alert notification

⬇

**Pseudocode:**

```plaintext
IF status = "Missing" AND daysSinceDue > 2
    THEN trigger reminder
```

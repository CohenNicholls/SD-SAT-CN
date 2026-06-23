# C5-3 Step 1 — Shoulders of Giants

## 1. Google Classroom

### What it does well

Google Classroom makes assignment tracking simple by using a clear stream of posts and a dedicated “Classwork” tab. Students can quickly see what is due, what is missing, and submit work directly. Teachers can return feedback and update grades in one place.

### What it does poorly

* Limited automation for “late vs missing” status tracking
* Teachers often still manually check and correct submission states
* Weak support for detailed workflow tracking (e.g. missing → late → submitted transitions are not always explicit)

### How it relates to your problem

This directly relates to Mr Marshall’s issue: Canvas currently requires manual updating of submission status, which is easy to forget. Google Classroom shows that simplicity improves student engagement, but also shows the downside of **limited workflow control for teachers**.

### Design influence

Because Google Classroom prioritises simplicity over deep status tracking, your system should:

* Keep a simple interface (like Classroom)
* BUT include **explicit status states (Missing → Late → Submitted)** to avoid confusion

---

## 2. Microsoft Teams (Assignments feature)

### What it does well

Microsoft Teams integrates assignments with a calendar-style due date system. Teachers can assign work, set deadlines, and track submissions in a structured dashboard. Notifications also help reduce forgotten updates.

### What it does poorly

* Interface can feel cluttered with multiple tabs and features
* Status updates are sometimes buried in menus
* Not optimised specifically for “late work correction workflows”

### How it relates to your problem

Teams reduces forgetting through notifications, but it still doesn’t solve the core issue your system targets: **teachers forgetting to manually update status after late submission**.

### Design influence

Because Teams uses reminders effectively, your system should:

* Include **automatic reminders for unmarked late work**
* But avoid clutter by keeping everything in one focused dashboard

---

## 3. Canvas LMS

### What it does well

Canvas provides a powerful LMS with detailed grading, assignment tracking, and status indicators like “Missing,” “Submitted,” and “Late.” It integrates deeply with marking workflows and supports large class management.

### What it does poorly

* Status updates often require multiple clicks and manual adjustment
* Teachers can overlook updating statuses when marking in bulk
* Interface is feature-heavy and not optimised for quick corrections

### How it relates to your problem

This is the **most directly related system**, since your design brief is based on Canvas. It confirms the exact issue: teachers struggle to maintain accurate submission status during marking workflows.

### Design influence

Because Canvas is powerful but slow for status correction, your system should:

* Extract only the **late/missing management feature**
* Make status updates **one-click or automatic**
* Reduce multi-step workflows into a single action

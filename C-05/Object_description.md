# Object Descriptions – Late Work Management System

---

## 1. Assignment Object

### Purpose

Stores information about a student's assignment and submission status.

### Attributes

| Attribute      | Data Type | Description                      |
| -------------- | --------- | -------------------------------- |
| assignmentID   | Integer   | Unique identifier for assignment |
| assignmentName | String    | Name of assignment               |
| dueDate        | Date      | Assignment due date              |
| submissionDate | Date      | Date assignment was submitted    |
| status         | String    | Missing, Late, or Submitted      |
| studentID      | Integer   | Associated student ID            |

### Methods

| Method          | Purpose                   |
| --------------- | ------------------------- |
| updateStatus()  | Changes assignment status |
| markLate()      | Sets status to Late       |
| markSubmitted() | Sets status to Submitted  |
| getStatus()     | Returns current status    |

---

## 2. Student Object

### Purpose

Stores student information and links students to assignments.

### Attributes

| Attribute   | Data Type | Description               |
| ----------- | --------- | ------------------------- |
| studentID   | Integer   | Unique student identifier |
| studentName | String    | Student's full name       |
| className   | String    | Student's class           |

### Methods

| Method            | Purpose                        |
| ----------------- | ------------------------------ |
| viewAssignments() | Displays student's assignments |
| getDetails()      | Returns student information    |

---

## 3. Teacher Object

### Purpose

Represents the teacher using the system.

### Attributes

| Attribute   | Data Type | Description               |
| ----------- | --------- | ------------------------- |
| teacherID   | Integer   | Unique teacher identifier |
| teacherName | String    | Teacher's name            |

### Methods

| Method                   | Purpose                    |
| ------------------------ | -------------------------- |
| updateAssignmentStatus() | Changes assignment status  |
| filterAssignments()      | Filters assignment records |
| searchAssignments()      | Searches for assignments   |
| viewReminders()          | Displays notifications     |

---

## 4. Reminder Object

### Purpose

Manages notifications for unresolved assignments.

### Attributes

| Attribute       | Data Type | Description                      |
| --------------- | --------- | -------------------------------- |
| reminderID      | Integer   | Unique reminder identifier       |
| reminderMessage | String    | Reminder text                    |
| reminderDate    | Date      | Date generated                   |
| viewed          | Boolean   | Whether reminder has been viewed |

### Methods

| Method             | Purpose                   |
| ------------------ | ------------------------- |
| generateReminder() | Creates a new reminder    |
| markViewed()       | Marks reminder as viewed  |
| displayReminder()  | Shows reminder to teacher |

---

## 5. AssignmentManager Object

### Purpose

Handles assignment management operations.

### Attributes

| Attribute      | Data Type | Description               |
| -------------- | --------- | ------------------------- |
| assignmentList | List      | Collection of assignments |

### Methods

| Method             | Purpose                        |
| ------------------ | ------------------------------ |
| addAssignment()    | Adds assignment record         |
| removeAssignment() | Deletes assignment             |
| findAssignment()   | Searches for assignment        |
| updateAssignment() | Updates assignment information |

---

## 6. FilterManager Object

### Purpose

Provides filtering and searching functionality.

### Attributes

| Attribute     | Data Type | Description         |
| ------------- | --------- | ------------------- |
| currentFilter | String    | Active filter type  |
| searchTerm    | String    | Current search text |

### Methods

| Method            | Purpose                      |
| ----------------- | ---------------------------- |
| filterByClass()   | Filters by class             |
| filterByStudent() | Filters by student           |
| filterByStatus()  | Filters by submission status |
| searchRecords()   | Searches assignment records  |

---

## 7. DataManager Object

### Purpose

Handles storage and retrieval of system data.

### Attributes

| Attribute         | Data Type | Description           |
| ----------------- | --------- | --------------------- |
| assignmentRecords | List      | Stored assignments    |
| historyRecords    | List      | Status change history |
| canvasData        | List      | Imported Canvas data  |

### Methods

| Method             | Purpose                |
| ------------------ | ---------------------- |
| saveData()         | Saves records          |
| loadData()         | Loads records          |
| importCanvasData() | Imports Canvas data    |
| storeHistory()     | Records status changes |

---

## 8. Dashboard Object

### Purpose

Displays a summary view for teachers.

### Attributes

| Attribute        | Data Type | Description                 |
| ---------------- | --------- | --------------------------- |
| totalAssignments | Integer   | Number of assignments       |
| missingCount     | Integer   | Missing assignments count   |
| lateCount        | Integer   | Late assignments count      |
| submittedCount   | Integer   | Submitted assignments count |

### Methods

| Method             | Purpose                       |
| ------------------ | ----------------------------- |
| displayDashboard() | Shows dashboard               |
| refreshDashboard() | Updates displayed information |
| generateSummary()  | Creates assignment summary    |

---

### Object Relationships

```text
Teacher
   │
   ├── manages ──► AssignmentManager
   │                    │
   │                    ├── Assignment
   │                    └── Student
   │
   ├── uses ──► FilterManager
   │
   ├── receives ──► Reminder
   │
   └── views ──► Dashboard

DataManager
   │
   ├── stores Assignment records
   ├── stores Reminder records
   └── stores History records
```

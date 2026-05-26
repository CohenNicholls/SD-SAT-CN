# Part 1: SRS Documentation

# Mr Marshall’s Late Work Management System

## User Story Template

| No  | Long User Story                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| --- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| US1 | As a teacher, I want to quickly update student submission statuses so that I can keep records accurate and reduce confusion during marking.<br><br>**Acceptance Criteria:**<br><br>- Given a student’s work is marked as missing, when the teacher updates the submission, then the status changes to “Late” or “Submitted”.<br>- Given the teacher is viewing student submissions, when they select a student, then the updated status is saved and displayed immediately.<br><br>**Priority:** Must Have |
| US2 | As a teacher, I want to filter classes and students so that I can find missing or late work more efficiently.<br><br>**Acceptance Criteria:**<br><br>- Given multiple classes are stored in the system, when the teacher selects a class filter, then only students from that class are displayed.<br>- Given a list of student submissions, when the teacher filters by missing work, then only students with missing submissions are shown.<br><br>**Priority:** Should Have                             |
| US3 | As a teacher, I want reminder notifications for outstanding submission updates so that I do not forget to follow up on late or missing work.<br><br>**Acceptance Criteria:**<br><br>- Given there are outstanding missing submissions, when the teacher opens the application, then reminders are displayed.<br>- Given a submission has not been updated, when the reminder system runs, then the teacher receives a notification to review it.<br><br>**Priority:** Could Have                           |

---

## Functional Requirements Template

| No  | User Story                                                                                                                                   | Functional Requirements                                                                                                                                                                                                                          |
| --- | -------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| US1 | As a teacher, I want to quickly update student submission statuses so that I can keep records accurate and reduce confusion during marking.  | The system must allow teachers to change submission statuses from “Missing” to “Late” or “Submitted”. The system must save status changes automatically. The system must display updated submission statuses immediately after changes are made. |
| US2 | As a teacher, I want to filter classes and students so that I can find missing or late work more efficiently.                                | The system must provide class filtering options. The system must allow teachers to filter student submissions by status, such as missing, late, or submitted. The system must display filtered student lists clearly.                            |
| US3 | As a teacher, I want reminder notifications for outstanding submission updates so that I do not forget to follow up on late or missing work. | The system must generate reminders for outstanding missing work. The system must display notifications when unresolved submissions require attention. The system must track unresolved updates until they are addressed.                         |

---

## Non-functional Requirements Template

| No  | User Story                                                                                                                                   | Non-functional Requirements                                                                                                                                                      |
| --- | -------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| US1 | As a teacher, I want to quickly update student submission statuses so that I can keep records accurate and reduce confusion during marking.  | The interface must be simple and intuitive. Status updates must occur within 2 seconds. The system must run on existing school computers.                                        |
| US2 | As a teacher, I want to filter classes and students so that I can find missing or late work more efficiently.                                | Filtering results must load quickly. The filtered view must remain clear and uncluttered. The interface must make it easy for teachers to identify the correct class or student. |
| US3 | As a teacher, I want reminder notifications for outstanding submission updates so that I do not forget to follow up on late or missing work. | Notifications must be clear, reliable, and non-intrusive. Reminders must not interfere with normal marking or record management tasks.                                           |

---

## Scope Template

| No  | User Story                                                                                                                                               | MoSCoW      |
| --- | -------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| US1 | As a teacher, I want to view and manage a checklist of missing or late student submissions so that I can quickly track outstanding work after due dates. | Must Have   |
| US2 | As a student, I want to see clearly marked missing or late submissions so that I can stay aware of what work I still need to complete.                   | Should Have |
| US3 | As a teacher, I want the submission status to update automatically after the due date so that I do not have to manually check and change each entry.     | Could Have  |

---

## Scope Statement

The scope of this project includes a late work management system that helps teachers track, update, and manage student submission statuses. The system is designed to support classroom marking and follow-up processes by making missing, late, and submitted work easier to identify and manage.

### 1. Must Have Features

* Student submission status updates
* Missing, late, and submitted work tracking
* Data saving functionality
* A checklist or table showing student submission records
* Teacher access to update student work statuses

### 2. Should Have Features

* Class filtering tools
* Student filtering options
* Simplified interface navigation
* Clear visual display of missing or late submissions
* Student-facing clarity around outstanding work, where appropriate

### 3. Could Have Features

* Reminder notifications
* Automated prompts for outstanding work
* Automatic status updates after due dates
* Additional teacher customisation options

### The following is explicitly out of scope for this version:

* Direct integration with Canvas
* Mobile app support
* Cloud-based syncing
* Student login accounts

---

## Constraint Template

| Constraint | Description                                                                                   |
| ---------- | --------------------------------------------------------------------------------------------- |
| Economic   | The project must remain cost free by using open-source software and existing school hardware. |
| Legal      | Student data must be handled responsibly and comply with school privacy expectations.         |
| Social     | The system must be simple for teachers to adopt with minimal training required.               |
| Technical  | The software must be developed in Python and run on standard school computers.                |
| Usability  | The interface must be teacher friendly, clean, and efficient to use during marking sessions.  |

---

## User Characteristics Template

| User Type       | Who They Are                                                                                       | Tech Skills                                                                       | Domain Knowledge                                                                     | Usage Patterns                                                                  | Special Needs                                                                              |
| --------------- | -------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------ |
| Developer       | The person building and maintaining the system, such as a software developer or student developer. | High — understands programming, databases, and user interface design.             | High — understands system requirements and the Canvas or school submission workflow. | Works during development cycles, testing, debugging, and maintenance phases.    | Needs clear requirements, consistent data structures, and access to testing examples.      |
| Primary Users   | Teachers who manage student submissions and track missing or late work.                            | Moderate — comfortable with basic LMS tools such as Canvas and digital documents. | High — understand submission deadlines, marking, and student progress.               | Regularly check and update missing or late work lists, usually daily or weekly. | Need a simple, fast, and uncluttered interface that works efficiently during marking.      |
| Secondary Users | Students who view or receive information about their submission status and missing work.           | Low to moderate — basic use of Canvas and online learning tools.                  | Moderate — understand their own assignments and deadlines.                           | Intermittent use, mainly when checking tasks, reminders, or teacher feedback.   | Need clear wording and easily understandable labels for missing, late, and submitted work. |

---

## Technical Environment Template

| Category              | Description                                                                   |
| --------------------- | ----------------------------------------------------------------------------- |
| Hardware Requirements | Existing school desktop or laptop computers.                                  |
| Software Requirements | Python and Python libraries for GUI development and data handling.            |
| Network Requirements  | Minimal internet connection required unless syncing features are added later. |
| Data Storage          | Local file storage for submission records and reminder data.                  |
| Security Requirements | Restricted access to teacher data and secure handling of student information. |

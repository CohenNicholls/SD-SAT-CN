# Data Dictionary

| Data Item          | Description                                    | Data Type     | Example                      | Validation Rules                       |
| ------------------ | ---------------------------------------------- | ------------- | ---------------------------- | -------------------------------------- |
| AssignmentID       | Unique identifier for each assignment          | Integer       | 1001                         | Must be unique and greater than 0      |
| AssignmentName     | Name of the assignment                         | String        | "Math Investigation"         | Cannot be blank                        |
| StudentID          | Unique identifier for each student             | Integer       | 20543                        | Must be unique and greater than 0      |
| StudentName        | Full name of student                           | String        | "John Smith"                 | Cannot be blank                        |
| ClassName          | Name of the class                              | String        | "Year 10 Mathematics"        | Cannot be blank                        |
| SubmissionStatus   | Current status of assignment submission        | Enum/String   | Missing, Late, Submitted     | Must be one of the predefined statuses |
| DueDate            | Assignment due date                            | Date          | 15/08/2026                   | Must be a valid date                   |
| SubmissionDate     | Date work was submitted                        | Date          | 17/08/2026                   | Must be a valid date or null           |
| ReminderID         | Unique identifier for reminder notification    | Integer       | 5001                         | Must be unique                         |
| ReminderMessage    | Reminder text displayed to teacher             | String        | "Review missing submissions" | Cannot be blank                        |
| ReminderDate       | Date reminder is generated                     | Date          | 18/08/2026                   | Must be a valid date                   |
| NotificationStatus | Indicates whether reminder has been viewed     | Boolean       | True                         | Must be True or False                  |
| TeacherID          | Unique identifier for teacher                  | Integer       | 101                          | Must be unique                         |
| TeacherName        | Name of teacher using the system               | String        | "Mr Marshall"                | Cannot be blank                        |
| SearchTerm         | Text entered into search bar                   | String        | "Smith"                      | Can contain letters and numbers        |
| FilterType         | Type of filter currently applied               | Enum/String   | Class, Status, Student       | Must match available filter options    |
| StatusChangeDate   | Date a submission status was updated           | Date          | 18/08/2026                   | Must be a valid date                   |
| HistoryRecord      | Log of status changes made by teacher          | String        | "Missing → Submitted"        | Automatically generated                |
| CanvasImportData   | Imported assignment and submission information | Record/Object | Assignment dataset           | Must match import format               |
| AssignmentRecord   | Stored record containing assignment details    | Record/Object | Complete assignment entry    | Must contain required fields           |
| DashboardView      | Current dashboard screen data                  | Record/Object | Assignment summary           | Generated from stored records          |

---

## Data Structures

### Assignment Record

| Field            | Data Type |
| ---------------- | --------- |
| AssignmentID     | Integer   |
| AssignmentName   | String    |
| StudentID        | Integer   |
| StudentName      | String    |
| ClassName        | String    |
| DueDate          | Date      |
| SubmissionStatus | Enum      |
| SubmissionDate   | Date      |

### Reminder Record

| Field              | Data Type |
| ------------------ | --------- |
| ReminderID         | Integer   |
| ReminderMessage    | String    |
| ReminderDate       | Date      |
| NotificationStatus | Boolean   |

### Status History Record

| Field            | Data Type |
| ---------------- | --------- |
| StudentID        | Integer   |
| AssignmentID     | Integer   |
| OldStatus        | Enum      |
| NewStatus        | Enum      |
| StatusChangeDate | Date      |

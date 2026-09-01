# Pseudocode – Mr Marshall's Late Work Management System

## Main Program

```text
BEGIN PROGRAM

LOAD assignment records
LOAD status history

DISPLAY main menu

WHILE application is running

    DISPLAY dashboard

    GET user choice

    IF choice = "View Assignments" THEN
        DISPLAY all assignments

    ELSE IF choice = "Update Status" THEN
        CALL UpdateStatus()

    ELSE IF choice = "Filter Assignments" THEN
        CALL FilterAssignments()

    ELSE IF choice = "Search Assignments" THEN
        CALL SearchAssignments()

    ELSE IF choice = "View Reminders" THEN
        CALL GenerateReminders()

    ELSE IF choice = "Exit" THEN
        SAVE all records
        CLOSE application

    END IF

END WHILE

END PROGRAM
```

---

## Update Submission Status

```text
PROCEDURE UpdateStatus()

    DISPLAY assignment list

    INPUT AssignmentID

    FIND matching assignment

    DISPLAY current status

    INPUT new status

    IF new status = "Missing"
       OR new status = "Late"
       OR new status = "Submitted" THEN

        UPDATE assignment status

        RECORD status change in history

        SAVE changes

        DISPLAY "Status updated successfully"

    ELSE

        DISPLAY "Invalid status"

    END IF

END PROCEDURE
```

---

## Filter Assignments

```text
PROCEDURE FilterAssignments()

    DISPLAY filter options
        1. Class
        2. Student
        3. Status

    INPUT filter choice

    IF filter choice = Class THEN

        INPUT class name

        DISPLAY assignments matching class

    ELSE IF filter choice = Student THEN

        INPUT student name

        DISPLAY assignments matching student

    ELSE IF filter choice = Status THEN

        INPUT status

        DISPLAY assignments matching status

    END IF

END PROCEDURE
```

---

## Search Assignments

```text
PROCEDURE SearchAssignments()

    INPUT search term

    FOR each assignment record

        IF student name contains search term
           OR assignment name contains search term THEN

            DISPLAY matching record

        END IF

    NEXT assignment

END PROCEDURE
```

---

## Generate Reminders

```text
PROCEDURE GenerateReminders()

    FOR each assignment

        IF status = "Missing" THEN

            CREATE reminder

            DISPLAY notification

        END IF

    NEXT assignment

END PROCEDURE
```

---

## Import Canvas Data

```text
PROCEDURE ImportCanvasData()

    SELECT Canvas export file

    READ file

    FOR each record in file

        STORE assignment information

    NEXT record

    DISPLAY "Import Complete"

END PROCEDURE
```

---

## Save Records

```text
PROCEDURE SaveRecords()

    SAVE assignment records

    SAVE status history

    SAVE reminder data

END PROCEDURE
```

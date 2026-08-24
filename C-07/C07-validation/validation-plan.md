# C07 Validation Plan

**Student name:** Cohen Nicholls

**Project name:** EduTrack

**Date committed:** 24/08/26

## Purpose

This file helps me prepare for the C7-3 validation task.

During Part B of the Live Coding Validation, I will add validation checks to real inputs in my teacher-picked feature.

I may need to add:

* # C723 existence checks
* # C724 type checks
* # C725 range checks

---

## Feature 1 validation planning

**Feature name:** Add Student
**Linked C06 feature file:** c06-validation/feature-1.md

| Input that needs validation | Where it appears in the code          | Existence check needed? | Type check needed? | Range check needed? | What bad input could test it?                               |
| --------------------------- | ------------------------------------- | ----------------------- | ------------------ | ------------------- | ----------------------------------------------------------- |
| Student ID                  | add_student_window() → student_id | Yes                     | Yes                | Yes                 | Enter letters, fewer than 10 digits, or more than 10 digits |
| Class                       | add_student_window() → class_box  | Yes                     | No                 | No                  | Leave the class unselected                                  |
| Status                      | add_student_window() → status_box | Yes                     | No                 | No                  | Leave the status unselected                                 |

### Notes for Feature 1

**What could go wrong if this input is not validated?**

Invalid or incomplete student records could be added to the system. This could make the student records inaccurate and affect other features such as filtering, reminders and reports.

**What should happen when invalid input is entered?**

The program should display a warning explaining the problem and prevent the student record from being saved until valid information is entered.

---

## Feature 2 validation planning

**Feature name:** Filter Students - Class Filter
**Linked C06 feature file:** c06-validation/feature-2.md

| Input that needs validation | Where it appears in the code      | Existence check needed? | Type check needed? | Range check needed? | What bad input could test it?                              |
| --------------------------- | --------------------------------- | ----------------------- | ------------------ | ------------------- | ---------------------------------------------------------- |
| Class filter                | filter_students() → class_box | Yes                     | No                 | No                  | No class is selected or an invalid class value is supplied |

### Notes for Feature 2

**What could go wrong if this input is not validated?**

An invalid class value could cause the filter to produce incorrect results or fail to match the available student records correctly.

**What should happen when invalid input is entered?**

The program should only allow a class from the available CLASSES list to be selected. If no class is selected, the program can treat the value as "All Classes" and show all classes.

The existing code uses:

values=["All Classes"] + CLASSES

and:

state="readonly"

This limits the user to the available options instead of allowing arbitrary text to be entered.

---

## Feature 3 validation planning

**Feature name:** Reminder Page
**Linked C06 feature file:** c06-validation/feature-3.md

| Input that needs validation | Where it appears in the code             | Existence check needed? | Type check needed? | Range check needed? | What bad input could test it?                                         |
| --------------------------- | ---------------------------------------- | ----------------------- | ------------------ | ------------------- | --------------------------------------------------------------------- |
| Student status data         | show_reminders() → student["Status"] | Yes                     | Yes                | No                  | A student record has no Status value or has an invalid status value |

### Notes for Feature 3

**What could go wrong if this input is not validated?**

If a student record does not contain a valid Status value, the Reminder Page may fail when trying to access student["Status"], or it may incorrectly identify students who need reminders.

**What should happen when invalid input is detected?**

The program should handle the invalid student record without crashing. The status should be checked against the valid STATUSES values before it is used by the Reminder Page.

The Reminder Page currently checks:

student["Status"] == "Missing"

so only students marked as "Missing" are displayed as requiring attention.

---

## Quick reference

| Skill code | Meaning                           |
| ---------- | --------------------------------- |
| C723       | Existence check                   |
| C724       | Type check                        |
| C725       | Range check                       |
| C735       | Two validation check types        |
| C745       | All three validation check types  |
| C753       | All relevant input data validated |

---

## Final check

* [x] I identified real inputs from my actual project.
* [x] I planned checks that match my actual features.
* [x] I did not invent fake inputs just for the assessment.
* [x] I know how to test at least one bad input.
* [ ] I committed this file before the validation.

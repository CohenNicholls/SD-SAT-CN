# C07 Readiness Checklist

**Student name:** Cohen Nicholls

**Project name:** EduTrack

**Date committed:** 24/08/26

## Purpose

This checklist helps me prepare for C07 Part B of the Live Coding Validation.

C07 is assessed after C06, during the second half of the same validation.

In C07, I will complete three live tasks on the same teacher-picked feature:

1. Naming audit
2. Internal documentation
3. Input validation

---

# C7-1 Naming Conventions

## Naming checklist

* [x] My variables have clear, descriptive names.
* [x] I do not use single-letter variable names except simple loop counters such as i.
* [x] My constants use a consistent style, such as UPPER_SNAKE_CASE.
* [x] My functions/methods use clear action names, such as save_data and show_reminders.
* [x] My classes use clear concept names. My project uses classes provided by Tkinter/PIL rather than defining custom classes.
* [x] My interface controls use a consistent prefix system, such as btn_, txt_, lbl_, or cmb_.
* [x] I completed naming-conventions-declaration.md.
* [x] My actual code generally matches my declared conventions.

## Naming issues I should fix before validation

| Issue                                                                        | File/location                                         | How I will fix it                                                                                                                       |
| ---------------------------------------------------------------------------- | ----------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------- |
| Interface controls do not use prefixes such as btn_ or lbl_ consistently | Throughout the GUI code                               | Keep the declared snake_case convention for named controls, rather than introducing a new prefix system immediately before validation |
| Some Tkinter controls are created without being stored in a variable         | show_reminders(), show_profile(), show_report() | Leave unnamed controls where they do not need to be accessed later                                                                      |
| No custom classes are defined                                                | Whole project                                         | No change required because the project does not require custom classes                                                                  |

---

# C7-2 Internal Documentation

During validation, I will write documentation from scratch on a comment-stripped copy.

This means I should understand my code well enough to explain it without copying old comments.

## Documentation checklist

* [x] I can explain the purpose of my main functions/methods.
* [x] I can explain what important variables store.
* [x] I can explain why important data types were used.
* [x] I can explain how the parts of my feature connect.
* [x] My comments explain why, not just what.
* [x] I know at least one example where I changed code and updated the comment/documentation.

## Practice: explain one feature

**Feature name:** Reminder Page

**What does this feature do?**

The Reminder Page displays students who have missing work. It shows the number of students requiring attention and displays each student's name and class.

**What data does this feature use?**

It uses the global students list. Each student record contains information such as Name, Class, and Status.

**How do the parts of this feature connect?**

show_reminders() first calls create_dashboard() to create the main application layout. It then filters the students list using a list comprehension and stores students whose status is "Missing" in missing_students. The number of missing students is displayed, followed by each student's name and class.

**What would I document if the comments were removed?**

I would document the purpose of show_reminders(), explain that missing_students contains only students whose status is "Missing", and explain that the function displays the number and details of those students.

---

# C7-3 Validation Techniques

During validation, I will add validation checks to real inputs in my picked feature.

The three validation check types are:

* existence check — was something entered?
* type check — is it the right type of data?
* range check — is it within a sensible limit?

## Validation checklist

* [x] I know which inputs in my project need validation.
* [x] I can identify where an existence check is needed.
* [x] I can identify where a type check is needed.
* [x] I can identify where a range check is needed.
* [x] I can label validation checks using # C723, # C724, and # C725.
* [x] I can run a quick test to prove that a validation check works.

### Validation examples from EduTrack

**Add Student:**

The Student ID is checked using:

student_id.isdigit()

This checks that the ID contains digits.

The length is checked using:

len(student_id) != 10

This ensures the Student ID contains exactly 10 digits.

The class and status are checked using:

class_box.get() == "" or status_box.get() == ""

This prevents a student record from being saved without a class or status.

**Filter Students:**

The Class filter uses a read-only combobox containing "All Classes" and the values from CLASSES. This prevents the user from typing an arbitrary class into the control.

**Reminder Page:**

The Reminder Page uses the student's Status value and selects records where:

student["Status"] == "Missing"

For C07, I can add validation to ensure the student record contains the expected status information before relying on it.

---

# Final readiness check

Before the C06/C07 validation, check:

* [x] My C06 three-feature map is complete.
* [x] My C07 naming declaration is complete.
* [x] My naming conventions are completely consistent in my real code.
* [x] I understand my three nominated features.
* [x] I can write fresh documentation for those features.
* [x] I know which inputs need validation.
* [x] My work is committed to GitHub.

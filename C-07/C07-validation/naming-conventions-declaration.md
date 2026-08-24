# C07 Naming Conventions Declaration

**Student name:**Cohen Nicholls

**Project name:** EduTrack

**Date committed:** 24 August 2026

## Purpose

This file declares the naming conventions I use in my SAT project.

During the C07 Part B validation, I will audit my teacher-picked feature against these conventions and fix any non-compliant names live.

---

## My naming conventions

| Element             | My convention                                                               | Example from my project | Code location                     |
| ------------------- | --------------------------------------------------------------------------- | ----------------------- | --------------------------------- |
| Variables           | Use lowercase snake_case names that clearly describe the data they store. | current_user          | Global Variables                  |
| Constants           | Use uppercase SNAKE_CASE names for values that remain unchanged.          | FONT_TITLE            | Fonts                             |
| Functions / methods | Use lowercase snake_case names that describe the action performed.        | save_data()           | Save Data                         |
| Classes             | Use PascalCase, with each word beginning with a capital letter.             | ImageTk, Toplevel   | Logo Loading / Add Student Window |
| Interface controls  | Use lowercase snake_case names that describe the purpose of the control.  | search_entry          | Student Management Page           |

---

## Naming convention examples

### Variables

My variables use **lowercase snake_case**, with words separated by underscores. Names should describe what the variable stores or represents.

Example from my project:

current_user

Why this is a good name:

current_user clearly describes that the variable stores the username of the teacher who is currently logged in. It follows the lowercase snake_case convention.

---

### Constants

My constants use **uppercase snake_case**, with words separated by underscores.

Example from my project:

FONT_TITLE

Why this is a good name:

FONT_TITLE is a constant because it stores a font setting that is reused by the interface. The uppercase name makes it clear that it is intended to remain unchanged.

Other examples include COLORS, FONT_HEADER, FONT_NORMAL, CLASSES, and STATUSES.

---

### Functions / methods

My functions and methods use **lowercase snake_case** and describe the action or purpose of the function.

Example from my project:

create_account()

Why this is a good name:

create_account() clearly describes what the function does. It uses lowercase letters with an underscore separating the two words, following the snake_case convention.

Other examples include save_data(), load_account(), login_user(), show_student_list(), filter_students(), and remove_student().

---

### Classes

My classes use **PascalCase**, where each word starts with a capital letter and there are no underscores.

Example from my project:

Toplevel

Why this is a good name:

Toplevel follows the PascalCase convention used for class names. It is also a class provided by Tkinter and is used in my project to create popup windows.

Other classes used in my project include Image, ImageTk, Tk, Frame, Label, Button, Entry, and Combobox.

---

### Interface controls

My interface controls use **lowercase snake_case** when they are stored in variables. The name should describe the purpose of the control.

Example from my project:

search_entry

Why this is a good name:

search_entry clearly identifies the control as an entry field used for searching student records. It uses lowercase snake_case, making the purpose of the control easy to understand.

Other examples include username_entry, password_entry, class_box, status_box, id_entry, button_frame, and report_box.

---

## Self-check

Before committing, check:

* [x] I have declared a convention for variables.
* [x] I have declared a convention for constants.
* [x] I have declared a convention for functions/methods.
* [x] I have declared a convention for classes, as my project uses classes.
* [x] I have declared a convention for interface controls, as my project uses a GUI.
* [x] I included real examples from my project.
* [x] My examples actually follow the conventions I declared.
* [x] This file is committed before the C06/C07 Live Coding Validation.

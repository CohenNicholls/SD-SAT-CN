# C06 Validation Setup Instructions

## Purpose

For C06, you need to nominate your **three most significant features** from your SAT project.

Your teacher may choose **one** of these features for the **Prove It’s Yours** task during the Live Coding Validation. You will not know which feature will be chosen in advance.

During the validation, you will work from a **comment-stripped copy** of your project and re-label the chosen feature using the correct `# C6XX` skill codes.

This task helps prove that:

- the feature is genuinely part of your project
- the feature links to your SRS requirements
- you understand the code you wrote
- you can explain and re-label the code without relying on comments

---

## Files you need to complete

In your GitHub repository, you should have this folder:

```text
c06-validation/
````

Inside that folder, you should have these files:

```text
three-feature-map.md
feature-a.md
feature-b.md
feature-c.md
```

You need to complete all four files.

---

# Step-by-step instructions

## Step 1: Choose your three most significant features

Choose three important features from your SAT project.

A feature should be something meaningful your program does, not just one line of code.

Good examples:

* adding a new habit/task/record
* saving user data to a file
* loading saved data
* calculating a result or recommendation
* displaying filtered results
* validating user input
* updating a dashboard or GUI display
* using a class/object to manage part of the system

Weak examples:

* “I used a variable”
* “I made a button”
* “I wrote an if statement”
* “I imported tkinter”
* “I changed the colour”

A strong feature usually includes several smaller programming skills working together.

---

## Step 2: Check that each feature links to your SRS

For each feature, find the matching requirement/s from your SRS.

Each feature should link to at least one:

* Functional Requirement, such as `FR-01`, `FR-02`, `FR-03`
* Non-Functional Requirement, such as `NFR-01`, `NFR-02`

Example:

```text
Feature: Add a new habit
Linked requirements:
- FR-01: The user can create a new habit.
- NFR-02: The solution should be easy for a first-time user to understand.
```

If you cannot link the feature to your SRS, it may not be one of your most significant features.

---

## Step 3: Complete `three-feature-map.md`

Open:

```text
c06-validation/three-feature-map.md
```

For each feature, write:

* the feature name
* what it does
* the linked FR/NFR codes
* where it appears in your code
* the matching feature evidence file

Example:

```text
## Feature a

**Feature name:**  
Add new habit

**Short description:**  
Allows the user to enter and save a new habit.

**Linked SRS requirements:**
FR-01, NFR-02 

**Code location:** 
main.py, class Habit, add_habit(), Line 67
```

---

## Step 4: Complete `feature-a.md`

Open:

```text
c06-validation/feature-a.md
```

Paste your commented code relevant to the nominated feature.

---

## Step 5: Complete `feature-b.md` and `feature-c.md`

Repeat the same process for:

```text
c06-validation/feature-b.md
c06-validation/feature-c.md
```

Each file should describe a different feature.

Do not copy the same explanation three times.

Each feature should have its own:

* purpose
* SRS link
* code location
* C6 skill evidence
* data evidence
* re-labelling notes

---

## Step 6: Add C6 skill-code labels to your real code

Your real project code needs `# C6XX` skill-code labels.

These labels go in your actual code files, not just in the feature evidence files.

Example:

```python
# C621: local variable stores the user's entered habit name
habit_name = self.habit_input.get()

# C624: conditional operator checks whether the user entered a blank habit
if habit_name == "":
    self.error_label.config(text="Please enter a habit name")
```

Use the C6 skill codes from your tick sheet.

Common C6-1 programming language skill codes include:

```text
C611 instructions
C612 arithmetic operators
C621 local variables
C622 constants
C623 logical operators
C624 conditional operators
C625 sequence
C626 selection
C627 GUI
C631 global variables
C632 iteration/repetition
C633 GUI controls
C641 functions
C642 methods
C643 access modifiers
C651 classes
C652 objects
C653 abstraction
C654 encapsulation
C655 generalisation
C656 inheritance
```

Common C6-2 data skill codes include:

```text
C613 text data
C614 numeric data
C615 Boolean data
C628 local variable data types
C629 why selected data types were used
C634 global variable data types
C635 arrays
C636 records
C637 data structures
C638 why data types/data structures were used
C644 data sources
C645 why data sources were used
C657 range of data types, structures and sources
C658 complete reasoning for data choices
```

Only label things that are actually present in your code.

Do not add fake or unnecessary features just to tick boxes.

---

## Step 7: Check that your labels and feature files match

Before committing, check that:

* each feature file points to real code
* the real code contains matching `# C6XX` labels
* the SRS requirements listed in the feature files actually exist in your SRS
* your explanations match what your code actually does

If your feature file says the feature uses a class, but your code does not use a class, fix the feature file.

If your code has a useful skill label but your feature file does not mention it, update the feature file.

---

## Step 8: Commit your work to GitHub

Commit your completed C06 validation files and your labelled code.

Suggested commit message:

```text
Complete C06 three feature map and skill-code labels
```

Make sure the following are committed:

```text
c06-validation/three-feature-map.md
c06-validation/feature-a.md
c06-validation/feature-b.md
c06-validation/feature-c.md
your real labelled project code
your updated SRS, if needed
```

---

# What to practise before the validation

For each of your three features, practise explaining:

1. What does this feature do?
2. Which FR/NFR does it link to?
3. Where is it in your code?
4. What C6 programming language features does it show?
5. What data types does it use?
6. What data structures does it use?
7. Does it use a data source, such as user input or a file?
8. Why did you choose those data types, structures or sources?
9. How would you re-label this feature if all comments were removed?
10. What small change could you make to this feature live?

---

# Important reminder

Your teacher may choose any one of your three nominated features for the Prove It’s Yours task.

You will need to re-label the chosen feature live, on a comment-stripped copy of your project.

The goal is not to memorise comments.

The goal is to understand your own code well enough that you can re-create the labels and reasoning during the validation.

# C07 Validation Preparation Instructions

## Purpose

C07 is assessed in **Part B** of the same Live Coding Validation as C06.

- **C06** happens in Part A.
- **C07** happens in Part B.
- You use the same comment-stripped copy of your project.
- You work on the same teacher-picked feature from your C06 three-feature map.

For C07, you will complete three live tasks:

1. **Naming audit**
2. **Internal documentation**
3. **Input validation**

Your goal is to show that you understand your own code and can improve it under validation conditions.

---

## Files to complete

In your GitHub repository, create this folder:

```text
c07-validation/
```

Inside it, complete these files:

```text
c07-validation/
  instructions.md
  naming-conventions-declaration.md
  c07-readiness-checklist.md
  validation-plan.md
```

---

# Step 1: Complete your naming conventions declaration

Open:

```text
c07-validation/naming-conventions-declaration.md
```

Complete the table for:

- variables
- constants
- functions / methods
- classes
- interface controls

Use real examples from your project.

Your teacher will use this declaration during the C7-1 naming audit.

---

# Step 2: Check your actual code names

Look through your project code.

Check that your names match the conventions you declared.

Fix names that are unclear, inconsistent, or too vague.

## Weak examples

```python
x = input()
data = []
button1 = Button()
def process():
```

## Stronger examples

```python
student_name = input()
assessment_scores = []
btn_submit_habit = Button()
def calculate_weekly_total():
```

Commit any naming improvements.

Suggested commit message:

```text
Improve naming conventions for C07 validation
```

---

# Step 3: Prepare for the naming audit

During C07 Part B, you will audit the teacher-picked feature.

You will need to:

1. compare the picked feature against your naming declaration
2. fix any names that do not follow your declared convention
3. add one short written self-check line

Use this sentence starter:

```text
One name I would reconsider is __________ because __________.
```

Finding an inconsistency is not automatically bad. It can show that you understand your own naming standard.

---

# Step 4: Prepare for internal documentation

During validation, you will work on a comment-stripped copy of your project.

That means your original comments and docstrings will be removed.

You will need to write fresh documentation for the picked feature.

Your documentation should explain:

- what the feature does
- what important data is used
- why that data is needed
- how functions, methods, classes, or GUI parts connect
- any change you made during the C06 Part A mini-challenges

Good documentation explains **why**, not just **what**.

## Weak comment

```python
# adds 1 to count
count += 1
```

## Stronger comment

```python
# Tracks one more completed habit so the weekly progress total stays accurate.
count += 1
```

Do not try to memorise comments. Understand your code well enough to write useful documentation again.

---

# Step 5: Complete the C07 readiness checklist

Open:

```text
c07-validation/c07-readiness-checklist.md
```

Work through each section:

- C7-1 Naming Conventions
- C7-2 Internal Documentation
- C7-3 Validation Techniques

Use the checklist to find what you still need to fix or practise.

---

# Step 6: Complete the validation plan

Open:

```text
c07-validation/validation-plan.md
```

For each of your three nominated C06 features, identify real inputs that may need validation.

For each input, decide whether it needs:

- **existence checking** — was something entered?
- **type checking** — is it the right kind of data?
- **range checking** — is it within sensible limits?

## Example

| Input | Where it appears | Existence check | Type check | Range check | Bad input to test |
|---|---|---|---|---|---|
| age | user profile form | Yes | Yes, integer | Yes, 0–120 | `abc`, `-5`, blank |
| habit name | add habit form | Yes | No | No | blank |
| weekly goal | goal setting form | Yes | Yes, integer | Yes, 1–7 | `ten`, `0`, `9` |

---

# Step 7: Practise validation skill codes

During C07 Part B, label validation checks as you write them.

Use these skill codes:

```python
# C723 existence check
# C724 type check
# C725 range check
```

Before finishing, run a quick test to prove at least one check catches bad input.

For example:

- try an empty value
- try text where a number is expected
- try a number outside the allowed range

A validation check only counts strongly if it actually works when tested.

---

# Step 8: Commit your C07 preparation files

Commit your completed C07 files to GitHub.

Suggested commit message:

```text
Complete C07 validation preparation
```

Make sure these files are committed:

```text
c07-validation/instructions.md
c07-validation/naming-conventions-declaration.md
c07-validation/c07-readiness-checklist.md
c07-validation/validation-plan.md
```

---

# What will happen during C07 Part B

C07 happens after C06 Part A.

You will continue using the same stripped project copy and the same teacher-picked feature.

## Task 1: Naming audit

You will:

- use your naming declaration
- check the picked feature
- fix non-compliant names
- write one self-check line about a name you would reconsider

## Task 2: Internal documentation

You will write fresh documentation for the picked feature.

Your documentation should cover:

- functionality
- data usage
- code structure
- any C06 Part A mini-challenge change

## Task 3: Input validation

You will add validation checks to real inputs in the picked feature.

You should aim to include:

- existence checks
- type checks
- range checks
- skill-code labels
- a quick test run

---

# Final checklist

Before the C06/C07 Live Coding Validation, check:

- [ ] My C06 three-feature map is complete.
- [ ] My C06 feature evidence files are complete.
- [ ] My C07 naming declaration is complete.
- [ ] My actual code follows my naming declaration.
- [ ] My C07 readiness checklist is complete.
- [ ] My validation plan identifies real inputs from my three features.
- [ ] I know the difference between existence, type, and range checks.
- [ ] I can write fresh documentation without copying old comments.
- [ ] I can explain how my picked feature works.
- [ ] I have committed all C07 preparation files to GitHub.
- [ ] I am ready to work without internet, AI, phone, or second device.

---

# Reminder

C07 is not about pretending your code is perfect.

It is about showing that you can:

- apply naming conventions deliberately
- explain your own code clearly
- add useful validation to real inputs
- test that your validation works
- make improvements under validation conditions

# C08-1 — Alpha Testing Plan
## Testing & Debugging

Use this document to plan, perform and document alpha testing on your **real SAT project**.

Your goal is not to prove that your program never fails. Good testing deliberately tries inputs that might reveal problems, then documents what you did when a problem was found.

---

# 1. Testing Table

Add as many rows as needed. Your table should contain a **range** of test cases.

| Test # | Feature / Module | Test Data / Input | Type of Test | Expected Result | Actual Result | Pass / Fail | Debugging Used | Corrective Action |
|---|---|---|---|---|---|---|---|---|
| 1 |  |  | Valid / Invalid / Boundary / Validation / Other |  |  |  |  |  |
| 2 |  |  |  |  |  |  |  |  |
| 3 |  |  |  |  |  |  |  |  |
| 4 |  |  |  |  |  |  |  |  |
| 5 |  |  |  |  |  |  |  |  |
| 6 |  |  |  |  |  |  |  |  |

## Your table should include

- [ ] valid/normal test data
- [ ] invalid test data
- [ ] at least one boundary or edge case
- [ ] at least one test that triggers a validation rule
- [ ] specific expected results
- [ ] specific actual results
- [ ] corrective actions for failed tests

Where relevant, validation tests could include:

- empty input
- wrong type
- out-of-range value

Do not write only **“works”**, **“doesn't work”**, **“pass”** or **“fail”** in the result columns. State what actually happened.

---

# 2. Debugging Evidence

While completing the testing table, genuinely use debugging techniques.

## Debugging statements

Example evidence could include temporary `print()` statements or logging that help you inspect values or trace program flow.

**Where did you use a debugging statement?**

Feature/module:

Debugging statement used:

What were you trying to find out?

What did it tell you?

---

## Breakpoint

Use your IDE's breakpoint/debugging tools during testing.

**Where did you use a breakpoint?**

Feature/module:

Where was the breakpoint placed?

What value or program behaviour were you inspecting?

What did the breakpoint help you discover?

---

# 3. Failed-Test Investigation

Choose a genuine failed test from your table that you understand well.

This is a strong candidate for your C08-1 screen recording.

**Test number:**

**Feature/module:**

**Input/test data:**

**Expected result:**

**Actual result:**

## Diagnose

What did the failure suggest might be wrong?

What breakpoint and/or debugging statement did you use?

What did the debugging evidence show?

What was the actual cause of the problem?

## Fix

What code did you change?

Why should this change fix the problem?

## Re-test

What happened when you ran the same test again?

Did the test now produce the expected result?

- [ ] Yes
- [ ] No — further debugging was required

If further debugging was required, briefly explain what happened next:

---

# 4. Recording Test

Choose the failed test you will be ready to demonstrate in your recording.

> **FAIL → DEBUG → FIX → PASS**

**My recording test is Test #:**

Before recording:

- [ ] I can find this row in my testing table quickly.
- [ ] I can reproduce the failing result.
- [ ] I know how to investigate it using a breakpoint and/or debugging statements.
- [ ] I understand the cause of the problem.
- [ ] I understand the fix.
- [ ] I can re-run the test to demonstrate the corrected result.

If a previously documented problem does not reproduce exactly during your recording, do **not** fake it. Explain what is happening and reason through it genuinely.

---

# 5. Commit Check

Before recording:

- [ ] My testing plan is complete enough to show a range of testing.
- [ ] Expected and actual results are documented.
- [ ] Failed tests include corrective actions.
- [ ] My C08-1 evidence uses the required `# C8-1-X` labels.
- [ ] My work is committed to GitHub.
- [ ] My AI disclosure log is up to date.

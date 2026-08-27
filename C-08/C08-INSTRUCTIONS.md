# C08 — Student Instructions
## Testing, Debugging, Design Modifications & Contingencies

C08 has **two parts**. For our class, they will be completed **back-to-back**.

- **C08-1 — Testing & Debugging:** alpha testing plan + screen recording
- **C08-2 — Design Modifications & Contingencies:** annotated design modification + 8-minute viva

The easiest way to prepare is to treat them as **one connected process**:

> **TEST → DEBUG → MODIFY → PREPARE → RECORD → VIVA**

Your testing should help generate the evidence you use for your design modification.

---

# Step 1 — Build Your Alpha Testing Plan

Use `C08-1-ALPHA-TESTING.md` to plan and record your testing.

Your testing should include a **range of test data**, not just normal inputs. Include tests such as:

- valid/normal input
- invalid input
- empty input where relevant
- wrong data type where relevant
- boundary or edge cases
- out-of-range input where relevant
- tests that deliberately trigger your validation rules

For every test, record:

1. the feature being tested
2. the test data/input
3. the expected result
4. the actual result
5. whether it passed or failed
6. any debugging used
7. any corrective action taken

You must genuinely use **debugging statements and/or breakpoints** while testing. Strong evidence should include use of a breakpoint.

Label your C08-1 evidence using the required `# C8-1-X` labels in your project/documentation.

---

# Step 2 — Find and Fix Real Problems

A failed test is useful evidence.

When a test fails:

1. reproduce the problem
2. use a breakpoint and/or debugging statements to investigate it
3. identify what is causing the problem
4. change the code
5. run the test again
6. record the corrective action and new result in your testing table

Choose **one failed test that you understand well**. This will become your main C08-1 recording example.

You should be able to demonstrate:

> **FAIL → DEBUG → FIX → PASS**

Do not deliberately create a fake bug just for the assessment. Use genuine testing and debugging from your SAT project.

---

# Step 3 — Identify a Design Modification

While testing, look for a result or piece of feedback that tells you something about your **design** should change.

The design could be something such as:

- a mock-up
- data dictionary
- IPO chart
- pseudocode
- object description

Use `C08-2-DESIGN-MODIFICATION.md` to document the change.

You need to show:

1. **the original design**
2. **the modified design**
3. **what changed**
4. **the specific test result or feedback that caused the change**
5. **why the modified design is better**

Your explanation should follow this chain:

> **TEST RESULT → DESIGN PROBLEM → MODIFICATION → IMPROVEMENT**

Do not just write, “I changed the layout because it was better.” Your reason must be connected to real evidence from your project.

---

# Step 4 — Check Your Evaluation Criteria and Contingency

## Evaluation criteria

Ask yourself:

> Did this design modification change how I would judge whether my solution is successful?

If **yes**, update the relevant evaluation criterion from your C4 evaluation matrix and explain why it changed.

If **no**, be ready to explain why no change was needed.

## Contingency

Identify at least one **specific problem that could still occur during development** and what you would do about it.

A weak contingency:

> The program might not work.

A stronger contingency:

> The imported file may be missing a required column. I would check the headings before processing the file and display an error message if a required column is missing.

Your contingency needs both:

- a **specific risk**
- a **specific mitigation** or backup plan

---

# Step 5 — Commit Your Evidence

Before assessment, make sure your work is committed to GitHub.

You should have committed:

- your alpha testing plan
- expected and actual test results
- debugging/corrective-action evidence
- your annotated design modification
- updated evaluation criteria, if relevant
- your contingency plan

Also make sure your **AI disclosure log is up to date**.

Your Git history is part of the authenticity evidence, so your commits and dates need to make sense alongside the work you show.

---

# Step 6 — Complete C08-1: Screen Recording

Your C08-1 recording must be **3–15 minutes** and use your **real SAT project**.

The easiest structure to remember is:

> **SHOW → FAIL → DEBUG → FIX → PASS**

## SHOW

At the start, make sure the recording shows:

- your real SAT codebase
- your testing table open beside your IDE
- your Git log with your own dated commits/messages
- the testing-table row you are about to demonstrate

## FAIL

Run a test from your testing table that fails.

Explain aloud:

- which test you are running
- the input
- what you expected
- what actually happened

## DEBUG

Use a breakpoint and/or debugging statements to investigate.

**Narrate continuously.** Explain what you are checking, what the evidence tells you, and what you think the problem is.

## FIX

Make the correction in your real project.

Explain what you changed and why.

## PASS

Run the same test again and show the corrected result.

Your recording must include **at least one unbroken fix cycle**:

> failing test → breakpoint/debugging → fix → re-run to pass

There must be **no cuts inside this cycle**.

### Important recording rules

- Narrate continuously.
- Do not use a silent screen capture.
- Do not dub narration over the recording afterwards.
- Do not use a demo or scratch project.
- Keep your testing table visible/available so the demonstrated test can be matched to the recorded row.
- Make sure the Git log shown is consistent with your actual repository.

---

# Step 7 — Complete C08-2: 8-Minute Viva

After C08-1, you will complete a one-on-one **8-minute viva** with your teacher.

You may use your own prepared design-modification documents. This is **not a memory test**.

Conditions:

- no internet
- no AI
- no phone
- your own documents only

Be ready to explain:

1. **Which design did you modify?**
2. **What was the design like before?**
3. **What changed?**
4. **What specific test result or feedback caused the change?**
5. **Why is the modified design better?**
6. **Did your evaluation criteria change? Why/why not?**
7. **What contingency have you planned?**
8. **What is your mitigation if that problem occurs?**

The most important explanation is:

> **“I found ___ during testing. This showed ___. Therefore I changed ___ to ___. This improves the solution because ___.”**

For higher-level evidence, your explanation must be tied to a **real test result or feedback** that is consistent with your testing evidence, Git history and development timeline.

---

# Final Check

Before you begin the assessments, complete `C08-READINESS-CHECKLIST.md`.

If every section is ready, you should have everything needed for both C08-1 and C08-2.

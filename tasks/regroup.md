# AI Agent Plan for Function Consolidation

**Goal:** Automatically refactor the project by moving single-function modules into the files that use them, while ignoring certain directories and specific files.

---

## 1. Scope and Objectives

The AI agent is responsible for restructuring the project by reducing unnecessary file fragmentation.
It should identify modules that contain only one function and are used by only one other file.
Those functions will be moved directly into the file that consumes them.

**The agent must ignore the following:**

- Any file located under directories containing:

  - `helps/`
  - `utils/`

---

## 2. Project Scanning Phase

### Tasks

1. Recursively scan the project source directory (e.g., `ArWikiCats/`).

2. Collect all `.py` files except:

   - Files inside paths containing `helps/`
   - Files inside paths containing `utils/`

3. For each remaining file:

   - Parse the file using AST.
   - Count the number of function definitions.
   - Exclude files containing classes or multiple functions.

### Output

A list of candidate files, each containing exactly one top-level function.

---

## 3. Function Usage Analysis

For every candidate file:

1. Extract the function name.
2. Search the entire project for usages of that function (simple static analysis + regex + AST checks).
3. Determine all files where the function is imported or called.

### Rules

- If the function is used by **more than one** file → skip.
- If the function is used by **zero files** → optional: log as unused.
- If the function is used by **exactly one** file → mark as safe to move.

### Output Table Example

| Function | Defined in_str       | Used By                 | Status  |
| -------- | -------------------- | ----------------------- | ------- |
| slugify  | ArWikiCats/tools/slugify.py | ArWikiCats/processors/title.py | movable |

---

## 4. Destination File Selection

For each movable function:

1. Identify the target file (the only file that imports/uses it).

2. Choose insertion location:

   - After imports
   - Before other function definitions
   - Maintain logical ordering

3. Ensure no name conflicts occur in the destination file.

---

## 5. Move Operation (Refactor Step)

For each approved function:

1. Copy the full function definition into the destination file.

2. Remove the import statement related to that function.

3. Remove the original source file if it contains no other code.

4. Apply formatting tools:

   - `isort`
   - `black`
   - `ruff --fix`

5. Rebuild imports if necessary.

---

## 6. Post-Refactor Validation

### Tasks

1. Run the full test suite:

   ```
   pytest -q
   ```

2. Run static analysis:

   ```
   mypy .
   ruff .
   ```

3. If any errors arise:

   - Roll back the last move.
   - Log the issue for manual review.

---

## 7. Reporting

After restructuring, the agent generates a Markdown report containing:

### 7.1 Summary

- Number of files scanned
- Number of candidates found
- Number of functions moved
- Number of functions skipped
- Confirmation of ignored paths:

  - `helps/`
  - `utils/`

### 7.2 Detailed Log Example

```
Moved function: normalize_text
From: ArWikiCats/cleaners/normalize.py
To:   ArWikiCats/parsers/title_parser.py
Reason: Function used in only one file
Status: SUCCESS
```

### 7.3 Skipped Examples

```
Skipped function: fix_spaces
Reason: File located inside "utils/" → excluded by policy.
```

---

## 8. Hard Constraints

The AI agent must enforce:

1. Never move functions from:

   - `helps/*`
   - `utils/*`

2. Never modify files containing classes or multiple functions.
3. Only move functions with exactly one consumer.
4. Always run test and static validation after each move.
5. Stop and rollback if any change introduces errors.

---

## 9. Optional Enhancements

- Automatic Git commits before and after each refactor step.
- Ability to run in “dry mode” for preview.
- Integration with CI pipelines.
- Generate dependency graphs before and after refactoring.

# AI Agent Prompt: Full Regex Optimization Across Entire Project

Use this prompt to refactor the entire Python project by replacing all inline regex
patterns with precompiled constants. This ensures significant performance gains,
eliminating millions of repeated `re.compile()` calls detected in profiling.

---

## Instructions for the AI Agent

### 1. Scan All Project Files
Process every `.py` file recursively.

Identify all usages of:
- `re.match(...)`
- `re.search(...)`
- `re.sub(...)`
- `re.findall(...)`
- `re.finditer(...)`
- `re.fullmatch(...)`
- inline `re.compile(...).X()`

Only convert when the pattern is:
- literal string
- not dynamically generated
- not already compiled

---

### 2. Extract Unique Patterns
For each pattern:
- Keep it exactly as written.
- Extract flags (if present).
- Assign a unique, meaningful name such as:
  - `REGEX_YEAR_RANGE`
  - `REGEX_SUFFIX_FOOTBALLERS`
  - `REGEX_CATEGORY_CLEANUP`
- If unclear: use `REGEX_001`, `REGEX_002`, etc.

---

### 3. Insert Precompiled Patterns at Top of File
Each file gets a block:

```python
import re

# Precompiled Regex Patterns
REGEX_XXX = re.compile(PATTERN, FLAGS)
```

Example:

```python
# Matches century expressions like “10th century BC”
REGEX_CENTURY = re.compile(r"\b\d+(st|nd|rd|th) century( BC| BCE)?\b", re.I)
```

---

### 4. Replace Runtime Calls with Precompiled Ones

### Before:
```python
re.search(r"\d{4}", text)
```

### After:
```python
REGEX_4DIGITS.search(text)
```

---

### 5. Remove inline re.compile calls
Replace:

```python
re.compile("xyz").search(...)
```

With:

```python
REGEX_XYZ.search(...)
```

---

### 6. Preserve Behavior
- identical flags
- identical grouping
- identical replacement logic
- no functional changes

---

### 7. Multi-File Architecture
If multiple files share the same regex patterns:

1. Create a file:
   `regex_constants.py`

2. Move shared constants into it.

3. Replace imports:

```python
from regex_constants import REGEX_EXAMPLE
```

---

### 8. Output Format
For each input file:
- Return updated code only (no explanations).
- All regex constants must be grouped at the top.
- Files without regex should be returned unchanged.

---

### 9. Priority Targets Based on Profiling
Optimize regex in:
- `event_lab_bot.py`
- `format_bots/*`
- `date_bots/*`
- `reg_result.py`
- `mv_years.py`
- all normalization functions
- category and label resolvers

These account for >80% of CPU time in profiling.

---

### End
Run this transformation on the entire codebase.

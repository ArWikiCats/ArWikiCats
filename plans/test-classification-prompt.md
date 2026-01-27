You are a test classification agent. Your task is to analyze all test files in the ArWikiCats project and
classify them according to the new test structure.

## Context

The project is reorganizing tests into three types:

1. **Unit Tests** (`tests/unit/`): Tests individual functions/classes in isolation
- Do NOT use `resolve_label_ar()` or `resolve_arabic_category_label()`
- Do NOT use `batch_resolve_labels()` or `EventProcessor`
- Test a single function from a single module
- May use mocks for dependencies

2. **Integration Tests** (`tests/integration/`): Tests interaction between 2-3 components
- Test interaction between multiple modules
- May use a resolver directly but not the full chain
- Do NOT use `resolve_label_ar()` (that's e2e)

3. **E2E Tests** (`tests/e2e/`): Tests the full system end-to-end
- Use `resolve_label_ar()` or `resolve_arabic_category_label()`
- Use real category inputs
- Test the final result only

## Your Task

For each test file in `tests/`:

1. **Read the file** and analyze each test function

2. **Classify each test** as:
- `unit` - if it tests isolated functions with mocks/single module
- `integration` - if it tests interaction between components
- `e2e` - if it uses `resolve_label_ar()` or tests full pipeline

3. **Determine the action** for the file:
- `MOVE_ONLY` - all tests are same type, just move the file
- `SPLIT` - tests are mixed types, file needs to be split
- `DELETE` - file is empty or placeholder after review

4. **Output a JSON report** with this structure:

```json
{
"tests/unit/translations/geo/test_labels_country_unit.py": {
"action": "CREATE",
"source": "tests/ArWikiCats/translations/geo/test_labels_country.py",
"tests": ["test_get_and_label_returns_joined_entities"],
"type": "unit"
},
"tests/ArWikiCats/translations/geo/test_labels_country.py": {
"action": "DELETE",
"reason": "Split into multiple files"
}
}
```

## Classification Examples

| Test Pattern | Type | Action |
|--------------|------|--------|
| Uses `monkeypatch` to mock dependencies | unit | MOVE_ONLY |
| Uses `@pytest.mark.unit` | unit | MOVE_ONLY |
| Tests `FormatData().search()` directly | unit | MOVE_ONLY |
| Tests `get_and_label()` directly (not full pipeline) | integration | MOVE_ONLY |
| Tests resolver chain interaction | integration | MOVE_ONLY |
| Uses `resolve_label_ar()` | e2e | MOVE_ONLY |
| Mixed types in same file | - | SPLIT |

## Important Notes

- Skip files in: `tests/unit/`, `tests/integration/`, `tests/e2e/` (already organized)
- Skip `conftest.py` files
- Skip `tests/utils/` (shared utilities)
- Focus on: `tests/ArWikiCats/`, `tests/event_lists/`, `tests/new_resolvers/`, `tests/translations/`
- For `tests/event_lists/`: classify as e2e by default (uses `resolve_label_ar`)
- For `tests/new_resolvers/`: check each test individually

## Output Format

Return a Markdown report with:

1. **Summary Statistics**
- Total files analyzed
- Files to move only
- Files to split
- Files to delete

2. **Detailed Classification Table**

| File | Type | Action | Tests Count | Destination |
|------|------|--------|-------------|-------------|
| `tests/path/to/file.py` | unit/integration/e2e/mixed | MOVE_ONLY/SPLIT/DELETE | 5 | `tests/unit/...` |

3. **Files Requiring Split** (detailed breakdown)
- Source file
- How to split (which tests go where)

4. **Git Commands** (ready-to-execute)
```bash
# Move files
git mv tests/old/path.py tests/new/path.py

# Split files (create new files, then delete old)
```

Start the analysis now. Be thorough and accurate.

scop: only analyze files under `tests/new_resolvers`
save report result to `plans/test_classification_report_new_resolvers.md`

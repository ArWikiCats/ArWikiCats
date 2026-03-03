# Agent Instructions for ArWikiCats

AI agent guide for the ArWikiCats Arabic Wikipedia Categories Translation Engine repository.

## Build, Lint & Test Commands

### Running Tests

```bash
# Run all default tests (excludes e2e, big, skip2, dump)
pytest

# Run a single test file
pytest tests/unit/test_example.py

# Run a specific test
pytest tests/unit/test_example.py::test_function_name

# Run tests by marker
pytest -m unit          # Unit tests only
pytest -m integration   # Integration tests
pytest -m e2e           # End-to-end tests
pytest -m big           # Big dataset tests

# Run all tests including slow ones
pytest --rune2e -m "not skip2" -n 16
```

### Code Quality

```bash
# Format code
black ArWikiCats/

# Sort imports
isort ArWikiCats/

# Lint code
ruff check ArWikiCats/

# Fix auto-fixable issues
ruff check --fix ArWikiCats/

# Run all quality checks
black ArWikiCats/ && isort ArWikiCats/ && ruff check ArWikiCats/
```

## Code Style Guidelines

### Python Standards

- **Python version**: 3.10+ (target 3.13 for linting)
- **Line length**: 120 characters
- **Use type hints** where appropriate
- **Docstrings**: Use double quotes, document public APIs

### Imports

```python
# Standard library imports first
import os
import sys
from pathlib import Path

# Third-party imports second
import pytest

# Local imports last
from ArWikiCats import resolve_label_ar
```

**Rules:**
- Sort with isort (black profile)
- Use multi-line imports with parentheses
- Include trailing commas
- Group: stdlib → third-party → local

### Naming Conventions

- **Functions**: `snake_case` (e.g., `resolve_label_ar`)
- **Classes**: `PascalCase` (e.g., `EventProcessor`)
- **Constants**: `UPPER_CASE` (e.g., `MAX_BATCH_SIZE`)
- **Private**: `_leading_underscore` for internal use
- **Modules**: `snake_case.py`

### Formatting

- Use Black for formatting
- Use double quotes for strings
- 4 spaces indentation
- Keep trailing commas in multi-line structures
- Use f-strings for string formatting

### Logging

**Always use f-strings for logging:**

```python
# ✅ Correct
logger.debug(f"Processing category: {category_name}")

# ❌ Incorrect
logger.debug("Processing category: %s", category_name)
```

### Error Handling

```python
# Prefer specific exceptions
try:
    result = process_data(data)
except ValueError as e:
    logger.error(f"Invalid data format: {e}")
    raise
except Exception as e:
    logger.exception(f"Unexpected error: {e}")
    raise
```

### Arabic Text Handling

- Preserve UTF-8 encoding for Arabic characters
- Maintain RTL text directionality in outputs
- Follow Arabic Wikipedia naming conventions
- Test with actual Arabic text, not just ASCII

## Project Structure

```
ArWikiCats/          # Main package
├── __init__.py      # Public API exports
├── config.py        # Configuration
├── event_processing.py
├── logging_config.py
└── main_processers/

tests/
├── unit/            # Fast unit tests (< 0.1s)
├── integration/     # Component tests (< 1s)
├── e2e/             # End-to-end tests (15,000+ cases)
├── big/             # Large dataset tests (26,000+ cases)
└── conftest.py      # Test configuration

pyproject.toml       # Project config, tool settings
pytest.ini           # Test configuration
```

## Key Dependencies

- `psutil` - System monitoring
- `humanize` - Human-readable formats
- `jsonlines` - JSON Lines support
- `pytest` - Testing framework
- `black`, `isort`, `ruff` - Code quality

## Performance Considerations

- Use caching for repeated translations
- Avoid computations in tight loops
- Batch processing is preferred
- Profile changes affecting core translation logic

## Development Workflow

1. Write tests for new functionality
2. Ensure all tests pass: `pytest`
3. Format code: `black && isort`
4. Lint: `ruff check`
5. Update `changelog.md` with changes

## Ignored Ruff Rules

E501, UP035, UP006, N806, N999, UP015, I001, N802, UP007, UP045

---

For complete guidelines, see `.github/copilot-instructions.md`

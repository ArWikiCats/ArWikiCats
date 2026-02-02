# Copilot Instructions for ArWikiCats

This document provides guidance for GitHub Copilot when working with the ArWikiCats repository, an Arabic Wikipedia Categories Translation Engine.

## Repository Overview

ArWikiCats is a Python library designed to automatically translate and standardize Arabic Wikipedia categories. The system handles complex patterns including temporal, geographical, functional, and mathematical categories.

## Testing Instructions

After completing any modifications in this repository, run the test suite to verify stability.

**Steps:**
1. Execute the following command: `pytest`
2. Ensure that all tests pass and no failures are introduced by the new changes.
3. If any issues are detected, attempt to fix them up to two times.
4. If the errors persist after two attempts, stop debugging and suggest a separate task proposing a clear plan or solution to resolve the remaining issues.

**Purpose:**
1. To maintain code reliability and ensure that recent edits do not break existing functionality.
2. To prevent excessive debugging in a single session and promote organized, trackable fixes.

## Code Formatting and Linting

This project uses multiple tools to maintain code quality:

### Black
- **Line length**: 120 characters
- **Target version**: Python 3.10+
- Run with: `black ArWikiCats/`

### isort
- **Profile**: black
- **Line length**: 120 characters
- **Import style**: Multi-line with parentheses
- Run with: `isort ArWikiCats/`

### Ruff
- **Line length**: 120 characters
- **Target version**: Python 3.13 (linter target, project requires 3.10+)
- **Ignored rules**: E402, E225, E226, E227, E228, E252, E501, F841, E224, E203, F401
- Run with: `ruff check ArWikiCats/`

## Logging Conventions

**Use f-strings for logging:**

✅ Correct: `logger.debug(f"part1={a} part2={b}")`

❌ Incorrect: `logger.debug("part1=%s part2=%s", a, b)`

## Changelog Updates

Generate an updated changelog section for `changelog.md` based on the modifications in this pull request.

**Include:**
- **Added:** new features
- **Changed:** refactors or improvements
- **Fixed:** bug fixes
- **Removed:** deprecated or deleted parts

**Format:**
Start the section with a header in the following form: `[<PR title>] - <date>`

**Note:**
Do **not** duplicate existing entries.

## Project Structure

- `ArWikiCats/` - Main package directory
- `tests/` - Test suite with 30,000+ tests organized in 3 categories:
  - `tests/unit/` - Unit tests (fast, isolated function/class tests)
  - `tests/integration/` - Integration tests (component interaction tests)
  - `tests/e2e/` - End-to-end tests (full system tests)
- `examples/` - Usage examples
- `help_scripts/` - Helper scripts
- `tasks/` - Task definitions
- `queries/` - Query-related code
- `pyproject.toml` - Project configuration and tool settings

## Development Requirements

- **Python**: 3.10 or higher
- **Core dependencies**: psutil, humanize, jsonlines
- **Build system**: hatchling

## Key Features to Preserve

When making changes, ensure these core features remain functional:
- High-speed category translation
- Extensive translation rules covering thousands of patterns
- Internal caching system
- Modular bot system architecture
- Batch processing capabilities
- Accurate and standardized results compatible with Arabic Wikipedia style

## Arabic Language Support

This project works extensively with Arabic text. When handling strings:
- Preserve Arabic character encoding (UTF-8)
- Maintain RTL (right-to-left) text directionality requirements
- Keep Arabic category naming conventions intact
- Follow Arabic Wikipedia standards for category translations

## Performance Considerations

The system is optimized for high-speed processing:
- Use caching where appropriate
- Avoid unnecessary computations in translation loops
- Maintain efficient batch processing capabilities
- Profile changes that affect core translation logic

## Contributing Guidelines

When adding new features or fixing bugs:
1. Write clear, descriptive commit messages
2. Add tests for new functionality
3. Update documentation for API changes
4. Follow existing code patterns and conventions
5. Ensure all tests pass before submitting changes
6. Update the changelog with your modifications

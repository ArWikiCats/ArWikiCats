# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

**ArWikiCats** is an Arabic Wikipedia Categories Translation Engine - a Python library that automatically translates English Wikipedia category names into standardized Arabic category names. It's designed for bot operations, mass translation, and automated editing tasks.

- **Status**: Beta
- **Tests**: 60,000+ tests (all four types)
- **Python**: 3.10+

## Common Commands

### Testing

Tests are organized into four categories:

| Category | Directory | Description |
|----------|-----------|-------------|
| **Unit** | `tests/unit/` | Fast tests for individual functions/classes in isolation (< 0.1s) |
| **Integration** | `tests/integration/` | Tests for interaction between components (< 1s) |
| **E2E** | `tests/e2e/` | Full system tests with real inputs (may be slow) |
| **BIG** | `tests/big/` | large dataset tests (slow) |

```bash
# Run all tests (60,000+ tests across all types)
pytest --rune2e -m "not skip2" -n 16

# Run by test category
pytest tests/unit/           # Unit tests only
pytest tests/integration/    # Integration tests only
pytest tests/e2e/            # End-to-end tests only (15,000+ categories)
pytest tests/big/ -m big     # large dataset tests (26,000+ categories)

# Run by marker
pytest -m unit               # Unit tests only
pytest -m integration        # Integration tests only
pytest --rune2e              # End-to-end tests only
pytest -m big                # large dataset tests

# Run specific test category
pytest -k "jobs"
pytest tests/test_languages/

# Run slow tests
pytest -m slow

# Verbose with short traceback
pytest -v --tb=short
```

### Code Quality
```bash
# Format code (line length: 120)
black ArWikiCats/

# Sort imports (black profile, line length: 120)
isort ArWikiCats/

# Lint (line length: 120, Python 3.13 target)
ruff check ArWikiCats/
```

### Installation
```bash
pip install ArWikiCats --pre
# or
pip install -r requirements.in
```

## High-Level Architecture

The translation pipeline processes category labels through multiple specialized resolvers:

```
Input Category → Normalization → Pattern Detection → Specialized Resolvers
    → Pattern-Based Resolvers → Time Format Resolver → Legacy Resolvers
    → Formatting → Output "تصنيف:..."
```

### Resolution Chain Order (from `ArWikiCats/new_resolvers/__init__.py`)

1. **Time to Arabic** (years, centuries, millennia, BC)
2. **Pattern-based resolvers**
3. **Jobs resolvers** (highest priority for job titles)
4. **Time + Jobs resolvers**
5. **Sports resolvers** (before nationalities to avoid conflicts)
6. **Nationalities resolvers**
7. **Countries names resolvers**
8. **Films resolvers**
9. **Relations resolvers**
10. **Countries with sports resolvers**
11. **Languages resolvers**
12. **Other resolvers** (catch-all)

### Key Components

- **`main_processers/main_resolve.py`** - Main resolution coordinator that orchestrates all resolvers
- **`new_resolvers/`** - Specialized resolver modules (jobs, sports, nationalities, countries, films, etc.)
- **`patterns_resolvers/`** - Pattern-based resolvers for complex patterns
- **`legacy_bots/`** - Legacy resolver pipeline (still used for some patterns)
- **`time_formats/`** - Time pattern handling (years, decades, centuries, BC)
- **`translations/`** - Translation dictionaries (jobs, sports, geo, nats, tv, medical, politics)
- **`fix/`** - Normalization and Arabic text cleaning
- **`event_processing.py`** - Batch processing engine

### Data Flow

1. **Input**: Category string (e.g., "Category:British footballers")
2. **Normalization**: Remove prefix, clean spaces/underscores (`fix/fixtitle.py`)
3. **Time Detection**: Extract years, decades, centuries (`time_formats/time_to_arabic.py`)
4. **Resolver Chain**: Try specialized resolvers in priority order (`new_resolvers/__init__.py`)
5. **Legacy Fallback**: If no match, try legacy bots (`legacy_bots/common_resolver_chain.py`)
6. **Formatting**: Apply Arabic formatting rules (`format_bots/`)
7. **Output**: Arabic label with "تصنيف:" prefix

## Core API

```python
from ArWikiCats import (
    resolve_arabic_category_label,  # Translate single category with prefix
    resolve_label_ar,               # Translate single category without prefix
    batch_resolve_labels,           # Batch translation
    EventProcessor,                 # Detailed processing class
)

# Single category
label = resolve_arabic_category_label("Category:2015 in Yemen")
# Output: "تصنيف:2015 في اليمن"

# Batch processing
result = batch_resolve_labels(["Category:British footballers", ...])
# result.labels: dict of translations
# result.no_labels: list of unmatched
```

## Key Design Patterns

1. **Resolver Chain Pattern**: Priority-based resolution through multiple specialized resolvers
2. **Caching**: `@functools.lru_cache` on all resolver functions for performance
3. **Pipeline Pattern**: Legacy resolvers organized into ordered pipeline
4. **Data Formatting Pattern**: `FormatData` and `MultiDataFormatter` classes for template-based translations

## Adding New Features

### Adding Translations
Edit modules in `ArWikiCats/translations/[category]/` - add to dictionaries with plural/singular forms

### Adding Resolvers
1. Create resolver in `ArWikiCats/new_resolvers/`
2. Import and register in `new_resolvers/__init__.py`
3. Add tests in `tests/new_resolvers/`

### Translation Data Format
```python
# Simple format
FormatData(
    formatted_data={"{sport} players": "لاعبو {sport_ar}"},
    data_list={"football": "كرة القدم"},
    key_placeholder="{sport}",
    value_placeholder="{sport_ar}",
)

# Dual-element format
format_multi_data(
    formatted_data={"{nat} {sport} players": "لاعبو {sport_ar} {nat_ar}"},
    data_list={"british": "بريطانيون"},
    data_list2={"football": "كرة القدم"},
)
```

## Important Conventions

### Logging
**Use f-strings for logging** (from `.github/copilot-instructions.md`):
- Correct: `logger.debug(f"part1={a} part2={b}")`
- Incorrect: `logger.debug("part1=%s part2=%s", a, b)`

### Testing Protocol
After any changes:
1. Run `pytest`
2. Fix any failures up to 2 times
3. If errors persist after 2 attempts, stop and propose a separate fix plan

### Arabic Text Handling
- Preserve UTF-8 encoding
- Maintain RTL (right-to-left) text directionality
- Follow Arabic Wikipedia naming conventions
- All resolver outputs should be Arabic text (except debug paths)

### Working with Large Files (API Context Limits)
**Model context limit**: ~200k tokens (~256k input tokens max)

When working with large files that may exceed the model's context:
- **Read files in chunks** using `Read` tool with `offset` and `limit` parameters
- **Use `Grep` for targeted searches** instead of reading entire files
- **Use `Task` with `Explore` agent** for open-ended codebase exploration

## Directory Structure

```
ArWikiCats/
├── __init__.py              # Public API exports
├── config.py                # Environment/CLI config
├── event_processing.py      # Batch processing engine
├── fix/                     # Normalization & text cleaning
├── main_processers/         # Core resolution logic
├── new_resolvers/           # Specialized resolver modules
├── patterns_resolvers/      # Pattern-based resolvers
├── legacy_bots/             # Legacy resolver pipeline
├── time_formats/            # Time pattern handling
├── format_bots/             # Category formatting
├── translations/            # Translation dictionaries
├── translations_formats/    # Data model formatters
├── jsons/                   # JSON data files
└── utils/                   # Shared utilities

tests/
├── unit/                    # Unit tests (fast, isolated)
├── integration/             # Integration tests (component interaction)
├── e2e/                     # End-to-end tests (15,000+ categories)
└── big/                     # Large dataset tests (26,000+ categories)
```

## Performance Characteristics

- Memory: <100MB (optimized from 2GB)
- Test suite: ~23 seconds
- Batch processing: >5,000 categories in seconds

# ArWikiCats - Arabic Wikipedia Categories Translation Engine

[![License](https://img.shields.io/badge/license-MIT-green)]()
[![Python](https://img.shields.io/badge/Python-3.10+-blue)]()
[![Status](https://img.shields.io/badge/status-Beta-orange)]()
[![Tests](https://img.shields.io/badge/tests-30000+-success)]()
[![Version](https://img.shields.io/badge/version-0.1.0b6-blue)]()

---

**ArWikiCats** is a Python library that automatically translates English Wikipedia category names into standardized Arabic category names. It is designed for bot operations, mass translation, and automated editing tasks on Arabic Wikipedia.

---

## Table of Contents

- [Why ArWikiCats](#why-arwikicats)
- [Key Features](#key-features)
- [Installation](#installation)
- [Quick Start](#quick-start)
- [How It Works](#how-it-works)
- [Configuration](#configuration)
- [Extending the System](#extending-the-system)
- [Project Structure](#project-structure)
- [Testing](#testing)
- [Performance](#performance)
- [Contributing](#contributing)
- [API Reference](#api-reference)

---

## Why ArWikiCats

Translating Wikipedia categories to Arabic presents unique challenges due to:

- The enormous volume of English categories
- Overlapping and complex patterns
- Need for consistent translation standards
- Complex temporal, geographical, occupational, and sports patterns
- Support for bot operations and automated editing

ArWikiCats addresses these challenges with a specialized translation engine that provides:

- **Unified translation style** following Arabic Wikipedia conventions
- **High accuracy** with specialized resolvers for different category types
- **Batch processing** support for thousands of categories
- **Extensible architecture** for adding new translation patterns

---

## Key Features

- **High Performance** - Process 5,000+ categories in seconds
- **Comprehensive Coverage** - 30,000+ tests covering thousands of patterns
- **Specialized Resolvers** - Separate modules for jobs, sports, nationalities, countries, films, etc.
- **Smart Caching** - `functools.lru_cache` for optimal performance
- **Modular Bots System** - Easy to extend with new translation rules
- **Complex Pattern Support** - Handles temporal, geographical, occupational, and sports patterns
- **Batch Processing** - Built-in support for processing large datasets
- **Detailed Results** - Optional detailed processing information with `EventProcessor`

---

## Installation

### Requirements

- Python 3.10 or later

### Install via pip

```bash
pip install ArWikiCats --pre
```

### Install from source

```bash
git clone https://github.com/MrIbrahem/ArWikiCats.git
cd ArWikiCats
pip install -r requirements.in
```

---

## Quick Start

### Single Category Translation

```python
from ArWikiCats import resolve_arabic_category_label

label = resolve_arabic_category_label("Category:2015 in Yemen")
print(label)
# Output: تصنيف:2015 في اليمن
```

### Batch Processing

```python
from ArWikiCats import batch_resolve_labels

categories = [
    "Category:2015 American television",
    "Category:1999 establishments in Europe",
    "Category:Belgian cyclists",
    "Category:American basketball coaches",
]

result = batch_resolve_labels(categories)

print(f"Translated: {len(result.labels)} categories")
print(f"Unmatched: {len(result.no_labels)} categories")

# Display results
for en, ar in result.labels.items():
    print(f"  {en} → {ar}")
```

### Direct Label Translation (without prefix)

```python
from ArWikiCats import resolve_label_ar

label = resolve_label_ar("American basketball players")
print(label)
# Output: لاعبو كرة سلة أمريكيون
```

### Detailed Processing

```python
from ArWikiCats import EventProcessor

processor = EventProcessor()
result = processor.process_single("Category:British footballers")

print(f"Original: {result.original}")
print(f"Normalized: {result.normalized}")
print(f"Raw Label: {result.raw_label}")
print(f"Final Label: {result.final_label}")
print(f"Has Label: {result.has_label}")
```

---

## How It Works

The translation pipeline processes category labels through multiple specialized resolvers:

```
Input Category → Normalization → Pattern Detection → Specialized Resolvers
    → Pattern-Based Resolvers → Time Format Resolver → Legacy Resolvers
    → Formatting → Output "تصنيف:..."
```

### Resolution Chain Order

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

### Data Flow

1. **Input**: Category string (e.g., "Category:British footballers")
2. **Normalization**: Remove prefix, clean spaces/underscores
3. **Time Detection**: Extract years, decades, centuries
4. **Resolver Chain**: Try specialized resolvers in priority order
5. **Legacy Fallback**: If no match, try legacy bots
6. **Formatting**: Apply Arabic formatting rules
7. **Output**: Arabic label with "تصنيف:" prefix

---

## Configuration

Customize system behavior using environment variables or CLI arguments:

| Setting | Description |
|---------|-------------|
| `TGC_RESOLVER_FIRST` | Enable general resolver first |
| `-STUBS` | Search for stub categories |
| `MAKEERR` | Enable error tracking mode |
| `NOPRINT` | Disable message printing |
| `SAVE_DATA_PATH` | Path for saving temporary data |

### Example Usage

```bash
# Via environment variables
NOPRINT=true python examples/run.py

# Via command line
python examples/run.py -stubs
```

---

## Extending the System

### Adding New Translations

Add dictionaries in `ArWikiCats/translations/`:

```python
# In ArWikiCats/translations/jobs/Jobs.py
jobs_mens_data = {
    "footballers": "لاعبو كرة قدم",
    "painters": "رسامون",
}

jobs_womens_data = {
    "footballers": "لاعبات كرة قدم",
    "painters": "رسامات",
}
```

### Adding a New Resolver

Create resolver in `ArWikiCats/new_resolvers/` and register in `reslove_all.py`:

```python
# In ArWikiCats/new_resolvers/reslove_all.py
from .your_resolver import resolve_your_category

def new_resolvers_all(category: str) -> str:
    category_lab = (
        resolve_jobs_main(category) or
        resolve_your_category(category) or  # Your new resolver
        resolve_sports_main(category) or
        ""
    )
    return category_lab
```

### Using Data Formats

```python
from ArWikiCats.translations_formats import FormatData, format_multi_data

# Simple single-element format
formatter = FormatData(
    formatted_data={"{sport} players": "لاعبو {sport_ar}"},
    data_list={"football": "كرة القدم"},
    key_placeholder="{sport}",
    value_placeholder="{sport_ar}",
)
result = formatter.search("football players")

# Dual-element format
multi_formatter = format_multi_data(
    formatted_data={"{nat} {sport} players": "لاعبو {sport_ar} {nat_ar}"},
    data_list={"british": "بريطانيون"},
    data_list2={"football": "كرة القدم"},
)
```

---

## Project Structure

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
├── time_resolvers/          # Time pattern handling
├── format_bots/             # Category formatting
├── translations/            # Translation dictionaries
├── translations_formats/    # Data model formatters
├── jsons/                   # JSON data files
└── utils/                   # Shared utilities

tests/
├── unit/                    # Unit tests (fast, isolated)
├── integration/             # Integration tests (component interaction)
└── e2e/                     # End-to-end tests (full system)
└── big/                     # large dataset tests (full system)

examples/                    # Usage examples
```

---

## Testing

After any changes, run tests:

```bash
# Run all tests
pytest

# Run by category
pytest tests/unit/           # Unit tests only
pytest tests/integration/    # Integration tests only
pytest tests/e2e/            # End-to-end tests only
pytest tests/big/            # large dataset tests

# Run by marker
pytest -m unit               # Unit tests only
pytest -m integration        # Integration tests only
pytest --rune2e              # End-to-end tests only

# Run specific test category
pytest -k "jobs"
pytest tests/test_languages/

# Run slow tests
pytest -m slow
```

### Test Coverage

The project has **30,000+ tests** covering:
- Core functionality
- Temporal patterns (years, decades, centuries, millennia, BC)
- Countries, nationalities, and various category cases
- Complex patterns (nationality + sport + job)
- Edge cases
- System performance
- Dictionary matching
- Sports teams and competitions
- Films and television
- Advanced job resolvers

---

## Performance

| Metric | Value |
|--------|-------|
| Memory Usage | <100MB (optimized from 2GB) |
| Test Suite Runtime | ~23 seconds |
| Batch Processing | >5,000 categories in seconds |

---

## Contributing

### Guidelines

- Any addition must include a rule + dictionary + test
- Follow Black (line length: 120), Isort (black profile), and Ruff for linting
- No rules without tests
- Use f-strings for logging: `logger.debug(f"part1={a} part2={b}")`
- Maintain UTF-8 encoding for Arabic text

### Code Quality Tools

```bash
# Format code (line length: 120)
black ArWikiCats/

# Sort imports (black profile, line length: 120)
isort ArWikiCats/

# Lint (line length: 120, Python 3.13 target)
ruff check ArWikiCats/
```

---

## API Reference

### Main Functions

```python
from ArWikiCats import (
    resolve_arabic_category_label,  # Translate single category with prefix
    resolve_label_ar,               # Translate single category without prefix
    batch_resolve_labels,           # Batch translation
    EventProcessor,                 # Detailed processing class
    logger,                         # Logging system
    print_memory,                   # Print memory usage
    dump_all_len,                   # Print data lengths
    config_all_params,              # List available parameters
)
```

### Single Category Translation

```python
label = resolve_arabic_category_label("Category:2015 in Yemen")
# Output: "تصنيف:2015 في اليمن"
```

### Batch Processing

```python
result = batch_resolve_labels(["Category:British footballers", ...])
# result.labels: dict of translations
# result.no_labels: list of unmatched
```

### EventProcessor

```python
processor = EventProcessor()
result = processor.process_single("Category:British footballers")
# Returns detailed processing information
```

---

## Links

- **GitHub**: https://github.com/MrIbrahem/ArWikiCats
- **Issues**: https://github.com/MrIbrahem/ArWikiCats/issues
- **PyPI**: `pip install ArWikiCats --pre`

---

## License

MIT License - see LICENSE file for details

---

**Author**: Ibrahim Qasim

**Version**: 0.1.0b6 (Beta)

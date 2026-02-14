# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

ArWikiCats is a Python library for automatically translating English Wikipedia category names to Arabic. It handles complex patterns including temporal (years, centuries), geographical (countries, cities), occupational, and sports-related categories.

## Development Commands

### Testing

```bash
# Run default tests (unit + integration, excludes slow tests)
pytest

# Run specific test categories
pytest tests/unit/           # Unit tests only
pytest tests/integration/    # Integration tests only
pytest tests/e2e/ --rune2e   # End-to-end tests (15,000+ categories)
pytest tests/big/ -m big     # Big dataset tests (26,000+ categories)

# Run all 60,000+ tests with parallel execution
pytest --rune2e -m "not skip2" -n 16

# Run tests matching a pattern
pytest -k "jobs"
pytest -m slow
```

### Code Formatting and Linting

```bash
black ArWikiCats/    # Format code (line length: 120)
isort ArWikiCats/    # Sort imports (profile: black)
ruff check ArWikiCats/  # Lint code
```

### After Making Changes

Always run `pytest` to verify no regressions. If tests fail after two fix attempts, stop and propose a plan rather than continuing to debug.

## Architecture

### Resolution Pipeline

Category translation flows through a priority-based resolver chain in `main_processers/main_resolve.py:resolve_label()`:

1. **Filter**: Categories may be filtered out by `filter_en.is_category_allowed()`
2. **Pattern resolvers** (`patterns_resolvers/`): Regex-based matching for complex structures (country+time, nationality patterns)
3. **New resolvers** (`new_resolvers/`): Specialized resolvers tried in priority order:
   - Time patterns (years, centuries, millennia)
   - Jobs/occupations
   - Time + Jobs combinations
   - Sports
   - Nationalities
   - Country names
   - Films/TV
   - Relations
   - Languages
4. **Legacy resolvers** (`legacy_bots/`): Fallback resolver chain for backward compatibility
5. **Post-processing**: `fixlabel()` applies Arabic text corrections, then `cleanse_category_label()` finalizes

The first resolver to return a non-empty result wins. Resolver order is critical for correctness.

### Key Modules

- `ArWikiCats/__init__.py`: Public API exports (`resolve_label_ar`, `batch_resolve_labels`, `EventProcessor`)
- `ArWikiCats/main_processers/main_resolve.py`: Core resolution logic with LRU caching
- `ArWikiCats/event_processing.py`: Batch processing and `EventProcessor` class
- `ArWikiCats/new_resolvers/__init__.py`: Orchestrates the new resolver chain (`_RESOLVER_CHAIN`)
- `ArWikiCats/patterns_resolvers/`: Pattern-based resolvers for structured categories
- `ArWikiCats/legacy_bots/`: Legacy resolver pipeline for backward compatibility
- `ArWikiCats/translations/`: Translation dictionaries (geo, sports, jobs, nats, etc.)
- `ArWikiCats/translations_formats/`: Template-based formatting classes (FormatData, MultiDataFormatterBase, etc.)
- `ArWikiCats/fix/`: Arabic text normalization and correction utilities

### Adding a New Resolver

1. Create resolver in `ArWikiCats/new_resolvers/your_resolver.py`
2. Import and add to `_RESOLVER_CHAIN` in `new_resolvers/__init__.py` at the appropriate priority position
3. Add tests in `tests/`

### Translation Data Format

The `translations_formats` module provides template-based translation:

```python
from ArWikiCats.translations_formats import format_multi_data

bot = format_multi_data(
    formatted_data={"{nat} players": "لاعبو {nat_ar}"},
    data_list={"british": "بريطانيون"},
    key_placeholder="{nat}",
    value_placeholder="{nat_ar}",
)
result = bot.search("british players")  # -> "لاعبو بريطانيون"
```

## Code Style

- Line length: 120 characters
- Use f-strings for logging: `logger.debug(f"part1={a} part2={b}")`
- Python 3.10+ required
- Maintain UTF-8 encoding for Arabic text

## Test Markers

Tests are organized with pytest markers:
- `@pytest.mark.unit`: Fast isolated tests
- `@pytest.mark.integration`: Component interaction tests
- `@pytest.mark.e2e`: Full system tests (requires `--rune2e`)
- `@pytest.mark.big`: Large dataset tests
- `@pytest.mark.slow`: Slow tests (excluded by default)
- `@pytest.mark.skip2`: Skip by default, run with `-m skip2`

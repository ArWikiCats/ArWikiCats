# 🏗️ ArWikiCats Refactoring Plan

This document outlines the technical architecture, execution flow, and refactoring recommendations for the ArWikiCats Arabic Wikipedia Categories Translation Engine.

---

## Table of Contents

1. [Complete Execution Flow Documentation](#1-complete-execution-flow-documentation)
2. [Main Entry Point](#2-main-entry-point)
3. [Detailed Execution Sequence Diagram](#3-detailed-execution-sequence-diagram)
4. [Architecture Layers](#4-architecture-layers)
5. [Data Flow Diagrams](#5-data-flow-diagrams)
6. [Required Refactoring](#6-required-refactoring)
7. [Performance Optimizations](#7-performance-optimizations)
8. [Code Quality Improvements](#8-code-quality-improvements)

---

## 1. Complete Execution Flow Documentation

### 1.1 High-Level Translation Pipeline

The ArWikiCats system processes categories through a multi-stage pipeline:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                          CATEGORY TRANSLATION PIPELINE                       │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  Raw Category → Normalization → Pattern Detection → Translation → Formatting│
│                                                                              │
│  "Category:2015 in Yemen" → "2015 in Yemen" → [Year+Country] → "2015 في اليمن" → "تصنيف:2015 في اليمن"│
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 1.2 Processing Stages

| Stage | Module | Function | Description |
|-------|--------|----------|-------------|
| 1. Input | `event_processing.py` | `EventProcessor.process()` | Receives categories |
| 2. Normalization | `event_processing.py` | `_normalize_category()` | Cleans input |
| 3. Format | `make_bots/format_bots` | `change_cat()` | Initial transformation |
| 4. Filter | `make_bots/filter_en` | `is_category_allowed()` | Validates category |
| 6. Pattern Resolution | Multiple resolvers | Various | Matches patterns |
| 7. Translation | `main_processers/main_resolve.py` | `resolve_label()` | Core translation |
| 8. Fix Label | `fix/` | `fixlabel()` | Post-processing |
| 9. Prefix | `event_processing.py` | `_prefix_label()` | Adds "تصنيف:" |

### 1.3 Resolver Priority Chain

The system attempts resolvers in a specific order, stopping at the first successful match:

```
1. labs_years_bot.lab_from_year()           # Year/decade/century patterns
        ↓ (if no match)
2. all_new_resolvers()                       # New resolver chain
        ↓ (if no match)
3. resolve_country_time_pattern()            # Country + time patterns
        ↓ (if no match)
4. resolve_nat_males_pattern()             # Nationality + gender patterns
        ↓ (if no match)
6. event2_new2()                              # Event2 bot
        ↓ (if no match)
7. event_lab()                               # Event Lab bot
        ↓ (if no match)
8. translate_general_category()              # General translation
```

---

## 2. Main Entry Point

### 2.1 Public API Entry Points

```python
# ArWikiCats/__init__.py - Public Interface

# Single category translation
resolve_arabic_category_label(category: str) -> str
    └── Returns: "تصنيف:translated_label"

# Batch processing
batch_resolve_labels(categories: List[str]) -> EventProcessingResult
    └── Returns: EventProcessingResult(processed, labels, no_labels, category_patterns)

# Low-level access
resolve_label_ar(category: str, fix_label: bool = True) -> str
    └── Returns: "translated_label" (without prefix)

# Processor class
EventProcessor()
    ├── .process(categories: Iterable[str]) -> EventProcessingResult
    └── .process_single(category: str) -> ProcessedCategory
```

### 2.2 Entry Point Code Flow

```python
# 1. User calls public API
from ArWikiCats import resolve_arabic_category_label

result = resolve_arabic_category_label("Category:2015 in Yemen")


# 2. Internal flow
def resolve_arabic_category_label(category_r: str) -> str:
    return _get_processed_category(category_r).final_label


def _get_processed_category(category_r: str) -> ProcessedCategory:
    processor = EventProcessor()
    return processor.process_single(category_r)


# 3. EventProcessor.process_single()
def process_single(self, category: str) -> ProcessedCategory:
    processed = self.process([category]).processed
    return processed[0] if processed else ProcessedCategory(...)


# 4. EventProcessor.process() - Main processing loop
def process(self, categories: Iterable[str]) -> EventProcessingResult:
    for original in categories:
        normalized = self._normalize_category(original)
        raw_label: CategoryResult = resolve_label(normalized)  # Core resolver
        final_label = self._prefix_label(raw_label.ar)
        # ... build result
```

### 2.3 Configuration Entry Points

```python
# ArWikiCats/config.py

settings = Config(
    app=AppConfig(
        save_data_path=os.getenv("SAVE_DATA_PATH", ""),
    ),
)

# Accessed as:
from ArWikiCats.config import app_settings
```

---

## 3. Detailed Execution Sequence Diagram

### 3.1 Single Category Translation Sequence

```
┌──────────┐     ┌─────────────────┐     ┌──────────────┐     ┌─────────────┐
│  Client  │     │ EventProcessor  │     │ main_resolve │     │  Resolvers  │
└────┬─────┘     └───────┬─────────┘     └──────┬───────┘     └──────┬──────┘
     │                   │                      │                    │
     │ resolve_arabic_category_label("Cat:2015 in Yemen")            │
     │──────────────────>│                      │                    │
     │                   │                      │                    │
     │                   │ _normalize_category()│                    │
     │                   │──────────────────────│                    │
     │                   │<─────────────────────│                    │
     │                   │ "2015 in Yemen"      │                    │
     │                   │                      │                    │
     │                   │ resolve_label("2015 in Yemen")            │
     │                   │─────────────────────>│                    │
     │                   │                      │                    │
     │                   │                      │ change_cat()       │
     │                   │                      │───────────────────>│
     │                   │                      │<──────────────────-│
     │                   │                      │                    │
     │                   │                      │ is_category_allowed()       │
     │                   │                      │───────────────────>│
     │                   │                      │<──────────────────-│
     │                   │                      │                    │
     │                   │                      │ lab_from_year()    │
     │                   │                      │───────────────────>│
     │                   │                      │<──────────────────-│
     │                   │                      │ (year: 2015)       │
     │                   │                      │                    │
     │                   │                      │ [Pattern Matching] │
     │                   │                      │───────────────────>│
     │                   │                      │<──────────────────-│
     │                   │                      │ "2015 في اليمن"    │
     │                   │                      │                    │
     │                   │                      │ fixlabel()         │
     │                   │                      │───────────────────>│
     │                   │                      │<──────────────────-│
     │                   │                      │                    │
     │                   │ CategoryResult       │                    │
     │                   │<─────────────────────│                    │
     │                   │                      │                    │
     │                   │ _prefix_label()      │                    │
     │                   │─────────────────────>│                    │
     │                   │<─────────────────────│                    │
     │                   │ "تصنيف:2015 في اليمن"│                    │
     │                   │                      │                    │
     │ "تصنيف:2015 في اليمن"                    │                    │
     │<──────────────────│                      │                    │
     │                   │                      │                    │
```

### 3.2 Resolver Chain Sequence

```
┌──────────────┐     ┌──────────────┐     ┌──────────────────┐     ┌────────────┐
│ main_resolve │     │ timeresolvers│     │ pattern_resolvers│     │ make_bots  │
└──────┬───────┘     └──────┬───────┘     └────────┬─────────┘     └────┬───────┘
       │                    │                     │                     │
       │ lab_from_year()    │                     │                     │
       │───────────────────>│                     │                     │
       │                    │ parse year/decade   │                     │
       │<───────────────────│                     │                     │
       │ (year data or "")  │                     │                     │
       │                    │                     │                     │
       │ [If no year match] │                     │                     │
       │                    │                     │                     │
       │ all_new_resolvers()│                     │                     │
       │──────────────────────────────────────────────────────────────>│
       │<─────────────────────────────────────────────────────────────-│
       │ (translation or "")│                     │                     │
       │                    │                     │                     │
       │ [If still no match]│                     │                     │
       │                    │                     │                     │
       │ resolve_country_time_pattern()           │                     │
       │─────────────────────────────────────────>│                     │
       │<────────────────────────────────────────-│                     │
       │                    │                     │                     │
       │ resolve_nat_males_pattern()            │                     │
       │─────────────────────────────────────────>│                     │
       │<────────────────────────────────────────-│                     │
       │                    │                     │                     │
       │ [Continue chain...]│                     │                     │
```

---

## 4. Architecture Layers

### 4.1 Current Architecture Overview

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                              PRESENTATION LAYER                              │
├─────────────────────────────────────────────────────────────────────────────┤
│  __init__.py                                                                 │
│  ├── resolve_arabic_category_label()  - Single category API                 │
│  ├── batch_resolve_labels()           - Batch processing API                │
│  ├── EventProcessor                   - Processing class                    │
└─────────────────────────────────────────────────────────────────────────────┘
                                      │
                                      ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                              PROCESSING LAYER                                │
├─────────────────────────────────────────────────────────────────────────────┤
│  event_processing.py                                                         │
│  ├── EventProcessor.process()         - Batch iteration                     │
│  ├── EventProcessor.process_single()  - Single processing                   │
│  ├── _normalize_category()            - Input cleaning                      │
│  └── _prefix_label()                  - Output formatting                   │
└─────────────────────────────────────────────────────────────────────────────┘
                                      │
                                      ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                              RESOLUTION LAYER                                │
├─────────────────────────────────────────────────────────────────────────────┤
│  main_processers/                                                            │
│  ├── main_resolve.py                  - Core resolver orchestration         │
│  ├── event2bot.py                     - Event type 2 processing             │
│  └── event_lab_bot.py                 - Event Lab processing                │
└─────────────────────────────────────────────────────────────────────────────┘
                                      │
                                      ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                              PATTERN LAYER                                   │
├─────────────────────────────────────────────────────────────────────────────┤
│  patterns_resolvers/                   │  time_formats/                    │
│  ├── country_time_pattern.py          │  ├──     *.py                        │
│  └── nat_males_pattern.py               │  ├── time_to_arabic.py              │
│                                        │  └── utils_time.py                  │
│  new_resolvers/                        │                                     │
│  ├── reslove_all.py                   │  genders_resolvers/                  │
│  ├── nationalities_resolvers/          │  └── jobs_and_genders_resolver.py  │
│  ├── jobs_resolvers/                   │                                     │
│  └── sports_resolvers/                │                                      │
└─────────────────────────────────────────────────────────────────────────────┘
                                      │
                                      ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                              BOT LAYER                                       │
├─────────────────────────────────────────────────────────────────────────────┤
│  make_bots/                            │  ma_bots/                           │
│  ├── format_bots/                      │  ├── country_bot.py                │
│  ├── date_bots/                        │  ├──                               │
│  ├── jobs_bots/                        │  └── general_resolver.py                  │
│  ├── sports_bots/                      │  ma_bots/                          │
│  └── matables_bots/                    │  └── ...                            │
└─────────────────────────────────────────────────────────────────────────────┘
                                      │
                                      ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                              DATA LAYER                                      │
├─────────────────────────────────────────────────────────────────────────────┤
│  translations/                         │  jsons/                             │
│  ├── geo/                              │  ├── nationalities/                 │
│  ├── sports/                           │  ├── geography/                     │
│  ├── jobs/                             │  ├── cities/                        │
│  ├── medical/                          │  ├── jobs/                          │
│  └── ...                               │  └── sports/                        │
│                                        │                                     │
│  translations_formats/                 │  fix/                               │
│  └── ...                               │  ├── fixlabel()                     │
│                                        │  └── specific_normalizations.py    │
└─────────────────────────────────────────────────────────────────────────────┘
                                      │
                                      ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                              UTILITIES LAYER                                 │
├─────────────────────────────────────────────────────────────────────────────┤
│  utils/                                │  helps/                             │
│  ├── match_relation_word.py            │  ├── log.py                        │
│  ├── fixing.py                         │  ├── memory.py                     │
│  └── check_it.py                       │  └── len_print.py                  │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 4.2 Module Dependency Graph

```
                          ┌──────────────────┐
                          │   __init__.py    │
                          └────────┬─────────┘
                                   │
                    ┌──────────────┼──────────────┐
                    ▼              ▼              ▼
            ┌───────────┐  ┌──────────────┐  ┌────────┐
            │  config   │  │event_process │  │ helps  │
            └───────────┘  └──────┬───────┘  └────────┘
                                  │
                                  ▼
                          ┌──────────────────┐
                          │  main_resolve    │
                          └────────┬─────────┘
                                   │
         ┌──────────────────┬──────┴───────┬──────────────────┐
         ▼                  ▼              ▼                  ▼
  ┌─────────────┐   ┌─────────────┐  ┌──────────┐    ┌──────────────┐
  │patterns_res │   │time_resolv  │  │new_resolv│    │  make_bots   │
  └─────────────┘   └─────────────┘  └──────────┘    └──────────────┘
         │                  │              │                  │
         └──────────────────┴──────────────┴──────────────────┘
                                   │
                                   ▼
                          ┌──────────────────┐
                          │  translations    │
                          │     (data)       │
                          └──────────────────┘
```

---

## 5. Data Flow Diagrams

### 5.1 Single Category Data Flow

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                         SINGLE CATEGORY DATA FLOW                            │
└─────────────────────────────────────────────────────────────────────────────┘

Input: "Category:2015 in Yemen"
                │
                ▼
┌───────────────────────────────────────┐
│          NORMALIZATION                 │
│  • Remove BOM (\ufeff)                 │
│  • Replace underscores with spaces     │
│  • Strip whitespace                    │
└───────────────────────────────────────┘
                │
        "2015 in Yemen"
                │
                ▼
┌───────────────────────────────────────┐
│          FORMAT TRANSFORM              │
│  • change_cat() processing             │
│  • Case normalization                  │
│  • Special character handling          │
└───────────────────────────────────────┘
                │
        "2015 in yemen" (normalized)
                │
                ▼
┌───────────────────────────────────────┐
│          FILTER CHECK                  │
│  • is_category_allowed() validation             │
│  • Check if category is translatable   │
│  • Early exit for invalid patterns     │
└───────────────────────────────────────┘
                │
        is_cat_okay: True/False
                │
                ▼
┌───────────────────────────────────────┐
│          YEAR EXTRACTION               │
│  • LabsYearsFormat.lab_from_year()     │
│  • Extract: year, decade, century      │
│  • Return: (cat_year, from_year)       │
└───────────────────────────────────────┘
                │
        cat_year: "2015", from_year: "2015 في اليمن"
                │
                ▼
┌───────────────────────────────────────┐
│          RESOLVER CHAIN                │
│  • all_new_resolvers()                 │
│  • resolve_country_time_pattern()      │
│  • resolve_nat_males_pattern()       │
│  • Dictionary lookups                  │
│  • Bot translations                    │
└───────────────────────────────────────┘
                │
        category_lab: "2015 في اليمن"
                │
                ▼
┌───────────────────────────────────────┐
│          POST-PROCESSING               │
│  • fixlabel() corrections              │
│  • Arabic text normalization           │
│  • Specific replacements               │
└───────────────────────────────────────┘
                │
        category_lab: "2015 في اليمن" (fixed)
                │
                ▼
┌───────────────────────────────────────┐
│          PREFIX ADDITION               │
│  • Add "تصنيف:" prefix                 │
│  • Skip if already present             │
│  • Handle empty labels                 │
└───────────────────────────────────────┘
                │
                ▼

Output: "تصنيف:2015 في اليمن"
```

### 5.2 Batch Processing Data Flow

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                          BATCH PROCESSING DATA FLOW                          │
└─────────────────────────────────────────────────────────────────────────────┘

Input: List[str] categories
        │
        ▼
┌───────────────────────────────────────┐
│      EventProcessingResult Init        │
│  processed: []                         │
│  labels: {}                            │
│  no_labels: []                         │
│  category_patterns: 0                  │
└───────────────────────────────────────┘
        │
        ▼
┌───────────────────────────────────────┐
│         ITERATION LOOP                 │
│  for original in categories:           │
│    if not original: continue           │
└───────────────────────────────────────┘
        │
        ├─────────────────────────────────────────────────────┐
        ▼                                                      │
┌───────────────────────────────────────┐                     │
│      Process Each Category             │                     │
│  normalized = _normalize_category()    │                     │
│  raw_label = resolve_label()           │  ◄─────────────────┘
│  final_label = _prefix_label()         │     (loop)
└───────────────────────────────────────┘
        │
        ▼
┌───────────────────────────────────────┐
│         RESULT CLASSIFICATION          │
│  if has_label:                         │
│    result.labels[normalized] = final   │
│    if from_match: patterns += 1        │
│  else:                                 │
│    result.no_labels.append(normalized) │
└───────────────────────────────────────┘
        │
        ▼
┌───────────────────────────────────────┐
│         BUILD ProcessedCategory        │
│  ProcessedCategory(                    │
│    original,                           │
│    normalized,                         │
│    raw_label.ar,                       │
│    final_label,                        │
│    has_label                           │
│  )                                     │
└───────────────────────────────────────┘
        │
        ▼

Output: EventProcessingResult
        ├── processed: List[ProcessedCategory]
        ├── labels: Dict[str, str]  {normalized: final_label}
        ├── no_labels: List[str]
        └── category_patterns: int
```

### 5.3 Cache Data Flow

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                            CACHE DATA FLOW                                   │
└─────────────────────────────────────────────────────────────────────────────┘

                    resolve_label(category, fix_label=True)
                                    │
                                    ▼
                    ┌───────────────────────────────┐
                    │     LRU CACHE CHECK           │
                    │  @functools.lru_cache(None)   │
                    └───────────────────────────────┘
                                    │
                    ┌───────────────┴───────────────┐
                    │                               │
                    ▼                               ▼
            ┌───────────────┐               ┌───────────────┐
            │  CACHE HIT    │               │  CACHE MISS   │
            │  Return cached │               │  Execute full │
            │  CategoryResult│               │  resolution   │
            └───────────────┘               └───────────────┘
                    │                               │
                    │                               ▼
                    │               ┌───────────────────────────┐
                    │               │  Full Resolution Chain    │
                    │               │  • Pattern matching       │
                    │               │  • Dictionary lookups     │
                    │               │  • Bot translations       │
                    │               │  • Post-processing        │
                    │               └───────────────────────────┘
                    │                               │
                    │                               ▼
                    │               ┌───────────────────────────┐
                    │               │  CACHE STORE              │
                    │               │  Store result for key     │
                    │               │  (category, fix_label)    │
                    │               └───────────────────────────┘
                    │                               │
                    └───────────────┬───────────────┘
                                    │
                                    ▼
                            CategoryResult(en, ar, from_match)
```

---

## 6. Required Refactoring

### 6.1 Separation of Concerns

#### 6.1.1 Repository Pattern

**Current State**: Data access is scattered across multiple modules with direct dictionary access.

**Proposed Refactoring**:

```python
# ArWikiCats/repositories/__init__.py

from abc import ABC, abstractmethod
from typing import Dict, Optional, List


class TranslationRepository(ABC):
    """Abstract base class for translation data access."""

    @abstractmethod
    def get_translation(self, key: str) -> Optional[str]:
        """Get translation for a given key."""
        pass

    @abstractmethod
    def has_translation(self, key: str) -> bool:
        """Check if translation exists."""
        pass


class DictionaryTranslationRepository(TranslationRepository):
    """Dictionary-based translation repository."""

    def __init__(self, data: Dict[str, str]):
        self._data = data

    def get_translation(self, key: str) -> Optional[str]:
        return self._data.get(key)

    def has_translation(self, key: str) -> bool:
        return key in self._data


class NationalityRepository(TranslationRepository):
    """Repository for nationality translations."""

    def __init__(self):
        self._load_data()

    def _load_data(self):
        # Load from ArWikiCats/jsons/nationalities/
        pass

    def get_nationality(self, english: str) -> Optional[dict]:
        """Get full nationality data including masculine, feminine, plural."""
        pass


class GeographyRepository(TranslationRepository):
    """Repository for geography translations."""

    def __init__(self):
        self._load_data()

    def _load_data(self):
        # Load from ArWikiCats/jsons/geography/
        pass

    def get_country_label(self, english: str) -> Optional[str]:
        pass

    def get_city(self, english: str) -> Optional[str]:
        pass
```

#### 6.1.2 Dependency Injection

**Current State**: Dependencies are imported directly, making testing difficult.

**Proposed Refactoring**:

```python
# ArWikiCats/container.py

from dataclasses import dataclass
from typing import Protocol


class ResolverProtocol(Protocol):
    """Protocol for category resolvers."""

    def resolve(self, category: str) -> str:
        """Resolve a category to Arabic translation."""
        ...


class CacheProtocol(Protocol):
    """Protocol for caching implementations."""

    def get(self, key: str) -> Optional[str]: ...

    def set(self, key: str, value: str) -> None: ...

    def clear(self) -> None: ...


@dataclass
class Container:
    """Dependency injection container."""

    # Repositories
    nationality_repo: NationalityRepository
    geography_repo: GeographyRepository
    jobs_repo: JobsRepository

    # Resolvers
    time_resolver: TimeResolver
    pattern_resolver: PatternResolver

    # Cache
    cache: CacheProtocol

    # Configuration
    config: Config

    @classmethod
    def create_default(cls) -> "Container":
        """Create container with default implementations."""
        return cls(
            nationality_repo=NationalityRepository(),
            geography_repo=GeographyRepository(),
            jobs_repo=JobsRepository(),
            time_resolver=TimeResolver(),
            pattern_resolver=PatternResolver(),
            cache=LRUCache(),
            config=settings,
        )

    @classmethod
    def create_for_testing(cls, **overrides) -> "Container":
        """Create container with test implementations."""
        defaults = {
            "nationality_repo": MockNationalityRepository(),
            "geography_repo": MockGeographyRepository(),
            # ...
        }
        defaults.update(overrides)
        return cls(**defaults)


# Usage in main_resolve.py
class CategoryResolver:
    def __init__(self, container: Container = None):
        self.container = container or Container.create_default()

    def resolve(self, category: str) -> CategoryResult:
        # Use self.container.nationality_repo instead of direct imports
        pass
```

### 6.2 Error Handling

#### 6.2.1 Custom Exceptions

```python
# ArWikiCats/exceptions.py


class ArWikiCatsError(Exception):
    """Base exception for ArWikiCats errors."""

    pass


class TranslationError(ArWikiCatsError):
    """Error during translation process."""

    def __init__(self, category: str, message: str, cause: Exception = None):
        self.category = category
        self.cause = cause
        super().__init__(f"Translation error for '{category}': {message}")


class PatternMatchError(ArWikiCatsError):
    """Error during pattern matching."""

    def __init__(self, pattern: str, input_text: str, message: str):
        self.pattern = pattern
        self.input_text = input_text
        super().__init__(f"Pattern '{pattern}' failed on '{input_text}': {message}")


class DataLoadError(ArWikiCatsError):
    """Error loading translation data."""

    def __init__(self, data_source: str, message: str):
        self.data_source = data_source
        super().__init__(f"Failed to load data from '{data_source}': {message}")


class ConfigurationError(ArWikiCatsError):
    """Error in configuration."""

    def __init__(self, config_key: str, message: str):
        self.config_key = config_key
        super().__init__(f"Configuration error for '{config_key}': {message}")


class CacheError(ArWikiCatsError):
    """Error in caching operations."""

    pass
```

#### 6.2.2 Unified Error Handler

```python
# ArWikiCats/error_handler.py

import functools
import logging
from typing import TypeVar, Callable, Any

from .exceptions import ArWikiCatsError, TranslationError
import logging

logger = logging.getLogger(__name__)

T = TypeVar("T")


class ErrorHandler:
    """Centralized error handling for ArWikiCats."""

    def __init__(self, logger_instance=None):
        self.logger = logger_instance or logger

    def handle_translation_error(self, error: Exception, category: str, default: str = "") -> str:
        """Handle translation errors with logging and fallback."""
        if isinstance(error, TranslationError):
            self.logger.warning(f"Translation failed for '{category}': {error}")
        else:
            self.logger.error(f"Unexpected error translating '{category}': {error}")
        return default

    def safe_resolve(self, func: Callable[..., T], *args, default: T = None, **kwargs) -> T:
        """Safely execute a resolver function with error handling."""
        try:
            return func(*args, **kwargs)
        except ArWikiCatsError as e:
            self.logger.warning(f"Resolver error: {e}")
            return default
        except Exception as e:
            self.logger.error(f"Unexpected resolver error: {e}")
            return default


def handle_errors(default_return=None, log_level=logging.WARNING):
    """Decorator for error handling."""

    def decorator(func: Callable[..., T]) -> Callable[..., T]:
        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> T:
            try:
                return func(*args, **kwargs)
            except ArWikiCatsError as e:
                logger.log(log_level, f"Error in {func.__name__}: {e}")
                return default_return
            except Exception as e:
                logger.error(f"Unexpected error in {func.__name__}: {e}")
                return default_return

        return wrapper

    return decorator


# Usage example:
@handle_errors(default_return="")
def resolve_country_time_pattern(category: str) -> str:
    # Implementation
    pass
```

### 6.3 Caching Strategy

#### 6.3.1 Current Implementation Issues

```python
# Current: @functools.lru_cache(maxsize=None)
# Problems:
# - Unbounded cache can cause memory issues
# - No cache statistics/monitoring
# - No cache invalidation strategy
# - Hard to test with caching
```

#### 6.3.2 Improved Caching Implementation

```python
# ArWikiCats/cache.py

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Optional, Dict, Any, TypeVar, Generic
import functools
import threading
import time

T = TypeVar("T")


@dataclass
class CacheStats:
    """Cache statistics."""

    hits: int = 0
    misses: int = 0
    size: int = 0

    @property
    def hit_rate(self) -> float:
        total = self.hits + self.misses
        return self.hits / total if total > 0 else 0.0


class CacheBackend(ABC, Generic[T]):
    """Abstract cache backend."""

    @abstractmethod
    def get(self, key: str) -> Optional[T]:
        pass

    @abstractmethod
    def set(self, key: str, value: T) -> None:
        pass

    @abstractmethod
    def clear(self) -> None:
        pass

    @abstractmethod
    def stats(self) -> CacheStats:
        pass


class LRUCacheBackend(CacheBackend[T]):
    """Thread-safe LRU cache with statistics."""

    def __init__(self, maxsize: int = 10000):
        self.maxsize = maxsize
        self._cache: Dict[str, T] = {}
        self._stats = CacheStats()
        self._lock = threading.RLock()

    def get(self, key: str) -> Optional[T]:
        with self._lock:
            if key in self._cache:
                self._stats.hits += 1
                return self._cache[key]
            self._stats.misses += 1
            return None

    def set(self, key: str, value: T) -> None:
        with self._lock:
            if len(self._cache) >= self.maxsize:
                # Remove oldest entry (simple LRU approximation)
                oldest_key = next(iter(self._cache))
                del self._cache[oldest_key]
            self._cache[key] = value
            self._stats.size = len(self._cache)

    def clear(self) -> None:
        with self._lock:
            self._cache.clear()
            self._stats = CacheStats()

    def stats(self) -> CacheStats:
        with self._lock:
            return CacheStats(hits=self._stats.hits, misses=self._stats.misses, size=len(self._cache))


class NoOpCacheBackend(CacheBackend[T]):
    """No-operation cache for testing."""

    def get(self, key: str) -> Optional[T]:
        return None

    def set(self, key: str, value: T) -> None:
        pass

    def clear(self) -> None:
        pass

    def stats(self) -> CacheStats:
        return CacheStats()


# Global cache instance
_translation_cache: CacheBackend = LRUCacheBackend(maxsize=50000)


def cached_translation(func):
    """Decorator for caching translation results."""

    @functools.wraps(func)
    def wrapper(category: str, *args, **kwargs):
        cache_key = f"{category}:{args}:{kwargs}"

        # Try cache first
        cached = _translation_cache.get(cache_key)
        if cached is not None:
            return cached

        # Execute function
        result = func(category, *args, **kwargs)

        # Store in cache
        _translation_cache.set(cache_key, result)
        return result

    return wrapper


def get_cache_stats() -> CacheStats:
    """Get current cache statistics."""
    return _translation_cache.stats()


def clear_cache() -> None:
    """Clear the translation cache."""
    _translation_cache.clear()
```

### 6.4 Centralized Configuration

```python
# ArWikiCats/config.py (Enhanced)

import os
from dataclasses import dataclass, field
from typing import Optional, List
from pathlib import Path


@dataclass(frozen=True)
class CacheConfig:
    """Configuration for caching."""

    enabled: bool = True
    max_size: int = 50000
    ttl_seconds: Optional[int] = None  # None = no expiry


@dataclass(frozen=True)
class ResolverConfig:
    """Configuration for resolvers."""

    enable_pattern_matching: bool = True
    enable_dictionary_lookup: bool = True
    enable_bot_resolution: bool = True


@dataclass(frozen=True)
class AppConfig:
    """Application configuration."""

    save_data_path: str = ""
    data_directory: Path = field(default_factory=lambda: Path(__file__).parent / "jsons")


@dataclass(frozen=True)
class Config:
    """Main configuration container."""

    cache: CacheConfig = field(default_factory=CacheConfig)
    resolver: ResolverConfig = field(default_factory=ResolverConfig)
    app: AppConfig = field(default_factory=AppConfig)

    @classmethod
    def from_environment(cls) -> "Config":
        """Create configuration from environment variables."""
        return cls(
            cache=CacheConfig(
                enabled=_env_bool("ARWIKICATS_CACHE_ENABLED", True),
                max_size=int(os.getenv("ARWIKICATS_CACHE_MAX_SIZE", "50000")),
            ),
            app=AppConfig(
                save_data_path=os.getenv("SAVE_DATA_PATH", ""),
            ),
        )

    @classmethod
    def for_testing(cls) -> "Config":
        """Create configuration for testing."""
        return cls(
            cache=CacheConfig(enabled=False),
        )


def _env_bool(name: str, default: bool) -> bool:
    """Parse boolean from environment variable."""
    value = os.getenv(name, str(default)).lower()
    return value in ("1", "true", "yes", "on")


# Global settings instance
settings = Config.from_environment()


# Convenience accessors (backward compatible)
app_settings = settings.app
cache_settings = settings.cache
resolver_settings = settings.resolver
```

### 6.5 Documentation Standards

#### 6.5.1 Module Documentation Template

```python
"""
Module: ArWikiCats.patterns_resolvers.country_time_pattern

Purpose:
    Resolves category patterns containing country and time components.
    Example: "2015 in Yemen" → "2015 في اليمن"

Dependencies:
    - ArWikiCats.translations.geo (country translations)
    - ArWikiCats.time_formats (time conversion)

Public Functions:
    - resolve_country_time_pattern(category: str) -> str

Usage:
    >>> from ArWikiCats.patterns_resolvers.country_time_pattern import resolve_country_time_pattern
    >>> result = resolve_country_time_pattern("2015 in Yemen")
    >>> print(result)  # "2015 في اليمن"

Notes:
    - Supports years, decades, centuries, and millennia
    - Handles BC/BCE date formats
    - Returns empty string if pattern doesn't match
"""
```

#### 6.5.2 Function Documentation Template

```python
def resolve_label(category: str, fix_label: bool = True) -> CategoryResult:
    """
    Resolve an English category name to its Arabic translation.

    This is the core resolution function that orchestrates multiple resolvers
    to find the appropriate Arabic translation for a given category.

    Args:
        category: The English category name (without "Category:" prefix).
                  Example: "2015 in Yemen"
        fix_label: Whether to apply post-processing fixes to the label.
                   Default is True.

    Returns:
        CategoryResult: A dataclass containing:
            - en: Original English category
            - ar: Arabic translation (empty string if not found)
            - from_match: Boolean indicating if resolved via pattern matching

    Raises:
        None: This function doesn't raise exceptions; failures return
              CategoryResult with empty ar field.

    Examples:
        >>> result = resolve_label("2015 in Yemen")
        >>> print(result.ar)
        '2015 في اليمن'

        >>> result = resolve_label("Belgian cyclists")
        >>> print(result.from_match)
        True

    Notes:
        - Results are cached using LRU cache
        - Resolution follows a priority chain (see resolver documentation)
        - Invalid categories return empty translations

    See Also:
        - resolve_label_ar: Convenience function returning only Arabic string
        - resolve_arabic_category_label: Full resolution with prefix
    """
    pass
```

---

## 7. Performance Optimizations

### 7.1 Batch Processing Optimization

```python
# ArWikiCats/batch_processor.py

from concurrent.futures import ThreadPoolExecutor, as_completed
from typing import List, Iterator, Tuple
import itertools


class BatchProcessor:
    """Optimized batch processing for categories."""

    def __init__(self, chunk_size: int = 1000, max_workers: int = 4):
        self.chunk_size = chunk_size
        self.max_workers = max_workers

    def process_batch(self, categories: List[str], processor_func) -> Iterator[Tuple[str, str]]:
        """
        Process categories in optimized batches.

        Args:
            categories: List of category strings
            processor_func: Function to process each category

        Yields:
            Tuples of (original_category, translated_label)
        """
        # Split into chunks for parallel processing
        chunks = list(self._chunk_list(categories, self.chunk_size))

        with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            futures = {executor.submit(self._process_chunk, chunk, processor_func): i for i, chunk in enumerate(chunks)}

            for future in as_completed(futures):
                chunk_results = future.result()
                yield from chunk_results

    def _process_chunk(self, chunk: List[str], processor_func) -> List[Tuple[str, str]]:
        """Process a single chunk of categories."""
        results = []
        for category in chunk:
            try:
                result = processor_func(category)
                results.append((category, result))
            except Exception as e:
                results.append((category, ""))
        return results

    @staticmethod
    def _chunk_list(lst: List, chunk_size: int) -> Iterator[List]:
        """Split list into chunks."""
        for i in range(0, len(lst), chunk_size):
            yield lst[i : i + chunk_size]
```

### 7.2 Async/Await Support

```python
# ArWikiCats/async_processor.py

import asyncio
from typing import List, Dict
from concurrent.futures import ProcessPoolExecutor


class AsyncCategoryProcessor:
    """Async category processing for high-throughput scenarios."""

    def __init__(self, max_concurrent: int = 100):
        self.semaphore = asyncio.Semaphore(max_concurrent)

    async def process_category(self, category: str) -> str:
        """Process a single category asynchronously."""
        async with self.semaphore:
            # Run CPU-bound translation in thread pool
            loop = asyncio.get_event_loop()
            result = await loop.run_in_executor(None, resolve_label, category)
            return result.ar

    async def process_batch(self, categories: List[str]) -> Dict[str, str]:
        """Process multiple categories concurrently."""
        tasks = [self.process_category(cat) for cat in categories]
        results = await asyncio.gather(*tasks, return_exceptions=True)

        return {cat: (res if isinstance(res, str) else "") for cat, res in zip(categories, results)}


# Usage example:
async def translate_categories_async(categories: List[str]) -> Dict[str, str]:
    """Translate categories using async processing."""
    processor = AsyncCategoryProcessor()
    return await processor.process_batch(categories)


# Synchronous wrapper
def translate_categories_concurrent(categories: List[str]) -> Dict[str, str]:
    """Synchronous wrapper for async translation."""
    return asyncio.run(translate_categories_async(categories))
```

### 7.3 Memory Optimization

```python
# ArWikiCats/memory_optimization.py

import sys
from typing import Dict, Any
import gc


class LazyLoader:
    """Lazy loading for translation dictionaries."""

    def __init__(self, load_func):
        self._load_func = load_func
        self._data = None

    @property
    def data(self):
        if self._data is None:
            self._data = self._load_func()
        return self._data

    def unload(self):
        """Unload data to free memory."""
        self._data = None
        gc.collect()


class MemoryManager:
    """Memory management utilities."""

    @staticmethod
    def get_object_size(obj: Any) -> int:
        """Get approximate memory size of an object."""
        size = sys.getsizeof(obj)
        if isinstance(obj, dict):
            size += sum(sys.getsizeof(k) + sys.getsizeof(v) for k, v in obj.items())
        elif isinstance(obj, (list, tuple)):
            size += sum(sys.getsizeof(item) for item in obj)
        return size

    @staticmethod
    def optimize_dict(d: Dict[str, str]) -> Dict[str, str]:
        """Optimize dictionary memory usage using string interning."""
        return {sys.intern(k): sys.intern(v) for k, v in d.items()}
```

---

## 8. Code Quality Improvements

### 8.1 Type Hints Enhancement

```python
# ArWikiCats/types.py

from typing import TypedDict, Optional, List, Dict, Union, Protocol, TypeVar
from dataclasses import dataclass


# Type aliases
CategoryName = str
ArabicLabel = str
TranslationDict = Dict[str, str]


class NationalityData(TypedDict):
    """Type definition for nationality data."""

    masculine_singular: str
    masculine_plural: str
    feminine_singular: str
    feminine_plural: str
    country_name: str


class CategoryResultDict(TypedDict):
    """Type definition for category result."""

    en: str
    ar: str
    from_match: bool


# Protocols for dependency injection
class ResolverProtocol(Protocol):
    """Protocol for resolver implementations."""

    def resolve(self, category: CategoryName) -> ArabicLabel:
        """Resolve category to Arabic label."""
        ...


class CacheProtocol(Protocol):
    """Protocol for cache implementations."""

    def get(self, key: str) -> Optional[str]: ...

    def set(self, key: str, value: str) -> None: ...


# Generic type variable for processors
T = TypeVar("T")
ResultT = TypeVar("ResultT", bound="CategoryResult")
```

### 8.2 Linting Configuration

```toml
# pyproject.toml additions for enhanced linting

[tool.mypy]
python_version = "3.10"
warn_return_any = true
warn_unused_configs = true
disallow_untyped_defs = true
disallow_incomplete_defs = true
check_untyped_defs = true
strict_optional = true
warn_redundant_casts = true
warn_unused_ignores = true
show_error_codes = true
exclude = [
    "tests/",
    "examples/",
    "_work_files/",
]

[[tool.mypy.overrides]]
module = "ArWikiCats.translations.*"
disallow_untyped_defs = false

[tool.ruff.lint]
select = [
    "E",      # pycodestyle errors
    "W",      # pycodestyle warnings
    "F",      # Pyflakes
    "I",      # isort
    "N",      # pep8-naming
    "D",      # pydocstring
    "UP",     # pyupgrade
    "B",      # flake8-bugbear
    "C4",     # flake8-comprehensions
    "S",      # flake8-bandit
    "T20",    # flake8-print
    "SIM",    # flake8-simplify
    "ARG",    # flake8-unused-arguments
    "PTH",    # flake8-use-pathlib
    "RUF",    # Ruff-specific rules
]
ignore = [
    "E402",   # Module level import not at top
    "E501",   # Line too long
    "D100",   # Missing docstring in public module
    "D104",   # Missing docstring in public package
]

[tool.ruff.lint.pydocstring]
convention = "google"

[tool.ruff.lint.per-file-ignores]
"tests/**/*.py" = ["S101", "D"]  # Allow assert and missing docstrings in tests
```

### 8.3 Code Style Guidelines

```python
# ArWikiCats/style_guide.py
"""
ArWikiCats Code Style Guide

1. NAMING CONVENTIONS
   - Classes: PascalCase (EventProcessor, CategoryResult)
   - Functions/methods: snake_case (resolve_label, get_translation)
   - Constants: UPPER_SNAKE_CASE (LABEL_PREFIX, MAX_CACHE_SIZE)
   - Private members: _leading_underscore (_data, _cache)
   - Module names: lowercase (event_processing.py, main_resolve.py)

2. TYPE HINTS
   - All public functions must have type hints
   - Use typing module for complex types
   - Example:
     def resolve_label(category: str, fix_label: bool = True) -> CategoryResult:

3. DOCSTRINGS
   - Use Google-style docstrings
   - Include Args, Returns, Raises, Examples sections
   - Example:
     def function(arg: str) -> str:
         '''Brief description.

         Args:
             arg: Description of argument.

         Returns:
             Description of return value.
         '''

4. IMPORTS
   - Group: standard library, third-party, local
   - Sort alphabetically within groups
   - Use absolute imports from ArWikiCats
   - Example:
     from __future__ import annotations

     import os
     import sys
     from typing import Dict, List

     import pytest

     from ArWikiCats.config import settings
     from ArWikiCats.main_processers import main_resolve

5. F-STRINGS FOR LOGGING
   - Use f-strings for all logging
   - ✅ logger.debug(f"Processing {category}")
   - ❌ logger.debug("Processing %s", category)

6. ERROR HANDLING
   - Use custom exceptions from ArWikiCats.exceptions
   - Always log errors before re-raising
   - Provide meaningful error messages

7. ARABIC TEXT
   - Always use UTF-8 encoding
   - Test with actual Arabic characters
   - Preserve RTL text handling
"""
```

---

## Summary

This refactoring plan provides a roadmap for improving the ArWikiCats codebase through:

1. **Separation of Concerns**: Repository pattern and dependency injection
2. **Error Handling**: Custom exceptions and unified error handler
3. **Caching**: Improved caching strategy with statistics and configurability
4. **Configuration**: Centralized, typed configuration management
5. **Documentation**: Clear standards for modules and functions
6. **Performance**: Batch processing, async support, and memory optimization
7. **Code Quality**: Enhanced type hints, linting, and style guidelines

Implementation should be done incrementally, starting with the most impactful changes (error handling, configuration) and gradually adopting patterns like dependency injection as the codebase evolves.

---

*Document Version: 1.0*
*Last Updated: 2024*
*Author: ArWikiCats Team*

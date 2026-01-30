# Legacy Bots Static Analysis & Refactoring Roadmap

**Scope**: `ArWikiCats/legacy_bots/` only
**Analysis Date**: 2026-01-26
**Total Files Analyzed**: 32 Python modules

---

## 1. System Overview

### 1.1 Current Architecture

The `legacy_bots` package implements a **chain-of-responsibility pattern** for translating English Wikipedia category names to Arabic. It serves as a fallback system when the newer resolver chain fails.

```
┌─────────────────────────────────────────────────────────────────┐
│                    ENTRY POINT                                  │
│  __init__.py: legacy_resolvers() with RESOLVER_PIPELINE         │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│              RESOLVER PIPELINE (Priority Order)                 │
│  1. country_bot.event2_d2         [circular_dependency/]       │
│  2. with_years_bot.wrap_try_with_years  [legacy_resolvers_bots/]│
│  3. year_or_typeo.label_for_startwith_year_or_typeo            │
│  4. event_lab_bot.event_lab                                     │
│  5. translate_general_category_wrap (sub + general)             │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                    SUPPORTING LAYERS                             │
│  ┌──────────────────┐  ┌──────────────────┐  ┌─────────────┐  │
│  │ Data Mappings    │  │ Utility Classes  │  │ Regex Hub   │  │
│  │ (data/mappings.py)│  │ (legacy_utils/)  │  │ (utils/)    │  │
│  └──────────────────┘  └──────────────────┘  └─────────────┘  │
│  ┌──────────────────┐  ┌──────────────────┐                   │
│  │ Make Bots        │  │ End/Start Bots   │                   │
│  │ (make_bots/)     │  │ (end_start_bots/)│                   │
│  └──────────────────┘  └──────────────────┘                   │
└─────────────────────────────────────────────────────────────────┘
```

### 1.2 Module Organization

| Directory | Purpose | Files |
|-----------|---------|-------|
| `circular_dependency/` | Contains circular imports between modules | 3 files |
| `legacy_resolvers_bots/` | Core resolver implementations | 5 files |
| `make_bots/` | Table lookups and data access | 4 files |
| `legacy_utils/` | Shared utility functions | 4 files |
| `end_start_bots/` | Suffix/prefix pattern matching | 5 files |
| `data/` | Centralized data mappings | 2 files |
| `utils/` | Regex patterns | 2 files |

---

## 2. Code Smells & Anti-Patterns

### 2.1 Circular Dependencies (Critical)

**Location**: [circular_dependency/__init__.py](../ArWikiCats/legacy_bots/circular_dependency/__init__.py:14-14)

```python
# Documented circular import chain:
country_bot.py imports:
    from . import general_resolver

general_resolver.py imports:
    from .ar_lab_bot import find_ar_label

ar_lab_bot.py imports:
    from . import country_bot

# Cycle: country_bot -> general_resolver -> ar_lab_bot -> country_bot
```

**Impact**: Runtime module loading issues, testing difficulties, potential for incomplete initialization.

---

### 2.2 God Object Anti-Pattern

**File**: [circular_dependency/country_bot.py](../ArWikiCats/legacy_bots/circular_dependency/country_bot.py:147-203)

**Issue**: `CountryLabelRetriever` class has excessive responsibilities:
- Country label resolution
- Prefix checking
- Regex year matching
- Member suffix handling
- Historical prefix resolution

**Evidence**:
```python
class CountryLabelRetriever(CountryLabelAndTermParent):
    def get_country_label(self, country: str, ...):  # 67 lines
    def _check_basic_lookups(self, country: str):    # 23 lines
    def fetch_country_term_label(...):                         # 82 lines
    def _handle_type_lab_logic(self, ...):           # 52 lines
```

**Suggested Approach**: Split into:
- `CountryLookup` (basic lookups)
- `PrefixHandler` (prefix matching)
- `YearPatternHandler` (regex year logic)

---

### 2.3 Long Method Anti-Pattern

**File**: [circular_dependency/ar_lab_bot.py](../ArWikiCats/legacy_bots/circular_dependency/ar_lab_bot.py:391-558)

**Method**: `LabelPipeline.build()` - 20 lines of complex logic

**File**: [circular_dependency/ar_lab_bot.py](../ArWikiCats/legacy_bots/circular_dependency/ar_lab_bot.py:314-388)

**Method**: `Fixing.determine_separator()` - 75 lines with nested conditionals

**Evidence**:
```python
def determine_separator(self) -> str:
    ar_separator = " "
    if self.separator_stripped == "in":
        ar_separator = " في "
    if (self.separator_stripped == "in" or self.separator_stripped == "at") and (" في" not in self.type_label):
        self.type_label = self.type_label + " في"
    # ... 60+ more lines of nested conditions
```

**Impact**: Difficult to test, understand, and modify.

---

### 2.4 Magic Strings & Numbers

**File**: [legacy_resolvers_bots/event_lab_bot.py](../ArWikiCats/legacy_bots/legacy_resolvers_bots/event_lab_bot.py:26-34)

```python
SUFFIX_EPISODES: Literal[" episodes"] = " episodes"
SUFFIX_TEMPLATES: Literal[" templates"] = " templates"
CATEGORY_PEOPLE: Literal["people"] = "people"
# ... 30+ more literal string constants
```

**Issue**: String literals scattered throughout code create maintenance burden.

**Recommendation**: Consolidate into a dedicated `constants.py` module.

---

### 2.5 Duplicate Code

**Pattern 1**: Resolver chain repetition in multiple files

**Locations**:
- [common_resolver_chain.py:119-128](../ArWikiCats/legacy_bots/common_resolver_chain.py:119-128)
- [legacy_resolvers_bots/country2_label_bot.py:72-81](../ArWikiCats/legacy_bots/legacy_resolvers_bots/country2_label_bot.py:72-81)

**Evidence**:
```python
# Repeated in 5+ files
resolved_label = (
    ""
    or all_new_resolvers(country2)
    or get_from_pf_keys2(country2)
    or parties_resolver.get_parties_lab(country2)
    or team_work.resolve_clubs_teams_leagues(country2)
    or university_resolver.resolve_university_category(country2)
    or work_peoples(country2)
    or ""
)
```

**Pattern 2**: "في" (in) preposition logic duplicated

**Locations**:
- [circular_dependency/ar_lab_bot.py:71-155](../ArWikiCats/legacy_bots/circular_dependency/ar_lab_bot.py:71-155)
- [legacy_resolvers_bots/country2_label_bot.py:283-290](../ArWikiCats/legacy_bots/legacy_resolvers_bots/country2_label_bot.py:283-290)
- [legacy_resolvers_bots/mk3.py:110-140](../ArWikiCats/legacy_bots/legacy_resolvers_bots/mk3.py:110-140)

---

### 2.6 Feature Envy

**File**: [circular_dependency/country_bot.py](../ArWikiCats/legacy_bots/circular_dependency/country_bot.py:204-227)

**Issue**: Methods heavily depend on external functions:
```python
def _check_basic_lookups(self, country: str) -> str:
    label = (
        New_female_keys.get(country, "")         # External
        or religious_entries.get(country, "")    # External
        or People_key.get(country)               # External
        or all_new_resolvers(country)            # External
        or team_work.resolve_clubs_teams_leagues(country)  # External
    )
```

**Impact**: High coupling, difficult to unit test in isolation.

---

### 2.7 Inappropriate Intimacy

**File**: [legacy_resolvers_bots/bot_2018.py](../ArWikiCats/legacy_bots/legacy_resolvers_bots/bot_2018.py:14-15)

```python
from ...translations.funcs import _get_from_alias, open_json_file
pop_All_2018 = open_json_file("population/pop_All_2018.json")  # 524266 entries
```

**Issue**: Direct access to private function `_get_from_alias` (leading underscore indicates private API).

---

### 2.8 Shotgun Surgery (Data Scattering)

**Problem**: Related data is scattered across multiple files.

**Example**: Number translations
- Originally in `legacy_utils/numbers1.py`
- Now duplicated in [data/mappings.py:16-146](../ArWikiCats/legacy_bots/data/mappings.py:16-146)

**Example**: Suffix mappings
- [data/mappings.py:153-274](../ArWikiCats/legacy_bots/data/mappings.py:153-274) defines `pp_ends_with_pase`, `pp_ends_with`
- [end_start_bots/end_start_match.py:3-88](../ArWikiCats/legacy_bots/end_start_bots/end_start_match.py:3-88) defines similar structures

---

### 2.9 Primitive Obsession

**File**: [make_bots/reg_result.py:38-45](../ArWikiCats/legacy_bots/make_bots/reg_result.py:38-45)

```python
@dataclass
class TypiesResult:
    year_at_first: str
    year_at_first_strip: str
    In: str
    country: str
    cat_test: str
```

**Issue**: All fields are primitive strings; no domain-specific types or validation.

**Example Usage**:
```python
# Caller must remember to call .strip() and .lower()
result = get_reg_result(category_r)
country = result.country.lower().strip()
```

---

### 2.10 Cache Invalidation Issues

**Pattern**: Inconsistent `@lru_cache` usage

**Examples**:
- [__init__.py:61](../ArWikiCats/legacy_bots/__init__.py:61): `maxsize=50000`
- [circular_dependency/country_bot.py:49](../ArWikiCats/legacy_bots/circular_dependency/country_bot.py:49): `maxsize=10000`
- [circular_dependency/country_bot.py:163](../ArWikiCats/legacy_bots/circular_dependency/country_bot.py:163): `maxsize=1024`

**Issue**: No cache invalidation strategy; mutable dictionaries like `Films_O_TT` are cached but can be modified at runtime.

**File**: [make_bots/bot.py:47-55](../ArWikiCats/legacy_bots/make_bots/bot.py:47-55)
```python
Films_O_TT = {}  # Mutable dict

@functools.lru_cache(maxsize=10000)
def get_KAKO(text: str) -> str:
    _, label = _get_KAKO(text)  # Caches access to Films_O_TT
    return label

def add_to_Films_O_TT(en: str, ar: str) -> None:
    Films_O_TT[en] = ar  # Invalidates cache assumptions!
```

---

## 3. Dependency Issues & Coupling Map

### 3.1 External Dependencies (Outside legacy_bots)

| Module | Dependencies | Coupling Level |
|--------|-------------|----------------|
| `common_resolver_chain.py` | `new_resolvers`, `sub_new_resolvers`, `translations`, `legacy_resolvers_bots`, `make_bots` | **High** |
| `circular_dependency/country_bot.py` | `new_resolvers`, `sub_new_resolvers`, `time_formats`, `translations`, `format_bots`, `fix`, `config` | **Very High** |
| `circular_dependency/ar_lab_bot.py` | `patterns_resolvers`, `sub_new_resolvers`, `translations`, `common_resolver_chain`, `legacy_resolvers_bots`, `make_bots`, `circular_dependency` | **Very High** |
| `legacy_resolvers_bots/event_lab_bot.py` | `config`, `fix`, `format_bots`, `main_processers`, `translations`, `sub_new_resolvers`, `circular_dependency`, `common_resolver_chain`, `make_bots` | **Very High** |

### 3.2 Internal Dependency Graph

```
┌─────────────────────────────────────────────────────────────────────┐
│                        ENTRY POINTS                                 │
│  __init__.py ─────────────────────────────────────────────────────┐  │
│                                                │                   │  │
│  tmp_bot.py ──────────────────────────────────┼───────────────────┤  │
│                                                │                   │  │
└────────────────────────────────────────────────┼───────────────────┘  │
                                                 │                      │
┌────────────────────────────────────────────────┼───────────────────┐  │
│              CIRCULAR DEPENDENCY MODULE         │                   │  │
│  ┌─────────────────────────────────────────────┼──────────────────┤  │
│  │ country_bot.py ◄────────────────────────────┼──────────────────┤  │
│  │        │                                    │                  │  │
│  │        ├──imports──► general_resolver.py ◄──┼──────────────────┤  │
│  │        │                                    │                  │  │
│  │        └──imports──► ar_lab_bot.py ────────┼──────┐           │  │
│  │                       │                      │      │           │  │
│  │                       └──imports──► country_bot.py│           │  │
│  └─────────────────────────────────────────────┼──────────────────┘  │
└────────────────────────────────────────────────┼─────────────────────┘
                                                 │
┌────────────────────────────────────────────────┼─────────────────────┐
│           LEGACY RESOLVERS BOTS                │                     │
│  ┌─────────────────────────────────────────────┼──────────────────┐  │
│  │ event_lab_bot.py ───────────────────────────┼─────────────────┤  │
│  │        │                                    │                 │  │
│  │ with_years_bot.py ◄─────────────────────────┼─────────────────┤  │
│  │        │                                    │                 │  │
│  │ year_or_typeo.py ◄──────────────────────────┼─────────────────┤  │
│  │        │                                    │                 │  │
│  │ bys.py ◄────────────────────────────────────┼─────────────────┤  │
│  │        │                                    │                 │  │
│  │ mk3.py ◄────────────────────────────────────┼─────────────────┤  │
│  │        │                                    │                 │  │
│  │ bot_2018.py ◄───────────────────────────────┼─────────────────┤  │
│  │        │                                    │                 │  │
│  │ country2_label_bot.py ──────────────────────┼─────────────────┤  │
│  └─────────────────────────────────────────────┼─────────────────┘  │
└────────────────────────────────────────────────┼─────────────────────┘
                                                 │
┌────────────────────────────────────────────────┼─────────────────────┐
│              SUPPORTING MODULES                │                     │
│  ┌─────────────────┐  ┌──────────────────────┼──────────────────┐  │
│  │  make_bots/     │  │  legacy_utils/       │                  │  │
│  │  ├── bot.py     │  │  ├── data.py         │                  │  │
│  │  ├── table1_bot │  │  ├── fixing.py       │                  │  │
│  │  ├── check_bot  │  │  ├── joint_class.py  │                  │  │
│  │  └── reg_result │  │  └── utils.py        │                  │  │
│  └─────────────────┘  └──────────────────────┼──────────────────┘  │
│                                                 │                    │
│  ┌─────────────────┐  ┌──────────────────────┼──────────────────┐  │
│  │ end_start_bots/ │  │  data/               │                  │  │
│  │ ├── fax2.py     │  │  └── mappings.py     │                  │  │
│  │ ├── fax2_*      │  │                      │                  │  │
│  │ └── utils.py    │  │  utils/              │                  │  │
│  └─────────────────┘  │  └── regex_hub.py    │                  │  │
│                       └──────────────────────┼──────────────────┘  │
└────────────────────────────────────────────────┼─────────────────────┘
```

### 3.3 Key Coupling Issues

1. **Bidirectional coupling between `circular_dependency/` modules**
2. **`common_resolver_chain.py` couples to 6+ external modules**
3. **`event_lab_bot.py` imports from 8 different modules**
4. **Mutable global state** (`Films_O_TT`, `players_new_keys`) shared across modules

---

## 4. Refactoring Roadmap

### Phase 1: Break Circular Dependencies (Priority: Critical)

**Target**: `circular_dependency/` directory

**Steps**:
1. Extract shared interface from `CountryLabelAndTermParent` into new `interfaces.py`
2. Create dependency injection container for resolver functions
3. Move `find_ar_label()` to separate module to break the cycle
4. Rename directory to `resolvers/` (no longer circular)

**Files Affected**:
- [circular_dependency/__init__.py](../ArWikiCats/legacy_bots/circular_dependency/__init__.py:1-17)
- [circular_dependency/country_bot.py](../ArWikiCats/legacy_bots/circular_dependency/country_bot.py:1-403)
- [circular_dependency/general_resolver.py](../ArWikiCats/legacy_bots/circular_dependency/general_resolver.py:1-54)
- [circular_dependency/sub_general_resolver.py](../ArWikiCats/legacy_bots/circular_dependency/sub_general_resolver.py:1-50)
- [circular_dependency/ar_lab_bot.py](../ArWikiCats/legacy_bots/circular_dependency/ar_lab_bot.py:1-586)

**Deliverables**:
- `resolvers/interface.py` - Abstract base classes
- `resolvers/country_resolver.py` - Refactored country_bot
- `resolvers/general_resolver.py` - Refactored general_resolver
- `resolvers/arabic_label_builder.py` - Extracted from ar_lab_bot
- `resolvers/__init__.py` - Clean imports

---

### Phase 2: Extract Value Objects & Constants (Priority: High)

**Target**: Magic strings, primitive data structures

**Steps**:
1. Create `constants/` package
2. Extract all literal strings to named constants
3. Create value objects for `Category`, `Separator`, `ArabicLabel`

**Files to Create**:
```
constants/
├── __init__.py
├── suffixes.py      # From data/mappings.py
├── prefixes.py      # From data/mappings.py
├── separators.py    # Separator mappings
└── patterns.py      # Regex pattern constants
```

**Example**:
```python
# constants/separators.py
class Separator(str):
    """Type-safe separator representation."""
    def __new__(cls, value: str):
        if value not in VALID_SEPARATORS:
            raise ValueError(f"Invalid separator: {value}")
        return str.__new__(cls, value)

    @property
    def arabic(self) -> str:
        return SEPARATOR_ARABIC_MAP[self]

VALID_SEPARATORS = {"in", "of", "from", "by", "at", "to", "on", "about"}
SEPARATOR_ARABIC_MAP = {
    "in": "في",
    "of": "من",
    "from": "من",
    # ...
}
```

---

### Phase 3: Implement Composition Over Inheritance (Priority: High)

**Target**: `CountryLabelRetriever` and `LabelPipeline`

**Current Issue**: Deep inheritance hierarchy with mixed concerns

**Refactored Structure**:
```python
# New architecture using composition
class CountryResolver:
    def __init__(self, lookup_chain: list[Callable]):
        self._lookup_chain = lookup_chain

    def resolve(self, country: str) -> str:
        for lookup in self._lookup_chain:
            if result := lookup(country):
                return result
        return ""

class ArabicLabelBuilder:
    def __init__(
        self,
        country_resolver: CountryResolver,
        type_resolver: TypeResolver,
        preposition_handler: PrepositionHandler,
    ):
        self._country = country_resolver
        self._type = type_resolver
        self._preposition = preposition_handler

    def build(self, category: str, separator: str) -> str:
        # Orchestrate composition
        ...
```

**Files Affected**:
- [circular_dependency/country_bot.py:147-203](../ArWikiCats/legacy_bots/circular_dependency/country_bot.py:147-203)
- [circular_dependency/ar_lab_bot.py:314-558](../ArWikiCats/legacy_bots/circular_dependency/ar_lab_bot.py:314-558)

---

### Phase 4: Centralize Data Access (Priority: Medium)

**Target**: Scattered lookup tables

**Steps**:
1. Create `data_access/` package
2. Implement repository pattern for all lookups
3. Add caching layer with proper invalidation

**Structure**:
```
data_access/
├── __init__.py
├── repositories.py
├── cache.py
└── loaders.py
```

**Example**:
```python
# data_access/repositories.py
class LabelRepository:
    def __init__(self, cache: Cache):
        self._cache = cache
        self._sources = [
            Population2018Source(),
            PlayersKeysSource(),
            JobsDataSource(),
            NewResolversSource(),
        ]

    def get(self, key: str) -> str | None:
        if cached := self._cache.get(key):
            return cached

        for source in self._sources:
            if value := source.get(key):
                self._cache.set(key, value)
                return value
        return None
```

**Files Affected**:
- [make_bots/bot.py](../ArWikiCats/legacy_bots/make_bots/bot.py:1-64)
- [legacy_resolvers_bots/bot_2018.py](../ArWikiCats/legacy_bots/legacy_resolvers_bots/bot_2018.py:1-113)
- [make_bots/table1_bot.py](../ArWikiCats/legacy_bots/make_bots/table1_bot.py:1-81)

---

### Phase 5: Reduce Method Complexity (Priority: Medium)

**Target**: Methods > 20 lines

**Files**:
1. [circular_dependency/ar_lab_bot.py:318-388](../ArWikiCats/legacy_bots/circular_dependency/ar_lab_bot.py:318-388) - `determine_separator()`
2. [circular_dependency/country_bot.py:284-335](../ArWikiCats/legacy_bots/circular_dependency/country_bot.py:284-335) - `_handle_type_lab_logic()`
3. [legacy_resolvers_bots/country2_label_bot.py:145-221](../ArWikiCats/legacy_bots/legacy_resolvers_bots/country2_label_bot.py:145-221) - `make_cnt_lab()`

**Refactoring Pattern**: Extract Method / Replace Conditional with Polymorphism

**Example**:
```python
# Before (75 lines, deep nesting)
def determine_separator(self) -> str:
    if self.separator_stripped == "in":
        ar_separator = " في "
    if (self.separator_stripped == "in" or ...) and (" في" not in self.type_label):
        self.type_label = self.type_label + " في"
    # ... 60 more lines

# After
def determine_separator(self) -> str:
    return self._separator_strategy.get_arabic(
        self.separator_stripped,
        self.type_label,
        self.country_lower,
    )

class SeparatorStrategy:
    def get_arabic(self, sep: str, type_label: str, country: str) -> str:
        handler = self._handlers.get(sep, self._default_handler)
        return handler(type_label, country)
```

---

### Phase 6: Standardize Error Handling (Priority: Low)

**Current State**: No explicit error handling; functions return empty strings on failure

**Recommendation**:
1. Define domain exceptions
2. Return `Result` objects instead of empty strings
3. Add proper logging at boundaries

**Structure**:
```python
# core/types.py
@dataclass
class ResolutionResult:
    label: str | None
    resolver_used: str
    fallback_tried: bool

    @property
    def success(self) -> bool:
        return self.label is not None

# core/exceptions.py
class ResolutionError(Exception):
    """Base exception for resolution failures."""

class CountryNotFoundError(ResolutionError):
    """Country could not be resolved."""
```

---

### Phase 7: Improve Testability (Priority: Medium)

**Target**: All modules

**Actions**:
1. Remove global state
2. Inject dependencies via constructors
3. Create test fixtures for external dependencies

**Example Refactoring**:
```python
# Before - hard to test
def get_KAKO(text: str) -> str:
    _, label = _get_KAKO(text)  # Accesses global Films_O_TT
    return label

# After - testable
class LabelLookup:
    def __init__(self, sources: dict[str, Callable[[str], str]]):
        self._sources = sources

    def get(self, text: str) -> str:
        for source_name, source_func in self._sources.items():
            if result := source_func(text):
                return result
        return ""
```

---

## 5. Concrete Changes Per File/Module

### 5.1 Entry Point

**File**: [`__init__.py`](../ArWikiCats/legacy_bots/__init__.py:1-88)

**Current Issues**:
- Lines 40-49: `translate_general_category_wrap()` duplicates logic from circular_dependency
- Line 62: Cache size 50000 may be excessive
- Missing type hints on callable signatures

**Recommended Changes**:
```python
# Add proper type hints
from typing import Protocol

class Resolver(Protocol):
    def __call__(self, category: str) -> str: ...

RESOLVER_PIPELINE: list[Resolver] = [
    country_bot.event2_d2,
    with_years_bot.wrap_try_with_years,
    year_or_typeo.label_for_startwith_year_or_typeo,
    event_lab_bot.event_lab,
    translate_general_category_wrap,
]

# Reduce cache size, add explicit cache key
@functools.lru_cache(maxsize=10000)
def legacy_resolvers(changed_cat: str) -> str:
    # Normalize input before caching
    changed_cat = changed_cat.strip().lower()
    # ... rest of implementation
```

---

### 5.2 Circular Dependency Modules

#### File: [`circular_dependency/__init__.py`](../ArWikiCats/legacy_bots/circular_dependency/__init__.py:1-17)

**Current**: Empty file with only circular dependency documentation

**Change**: Delete after refactoring; replace with proper `resolvers/__init__.py`

---

#### File: [`circular_dependency/country_bot.py`](../ArWikiCats/legacy_bots/circular_dependency/country_bot.py:1-403)

**Issues**:
- Line 27: Imports from same package creating circular dependency
- Lines 30-46: `translate_general_category_wrap()` duplicates code from __init__.py
- Lines 147-335: `CountryLabelRetriever` is a god object
- Lines 342-365: `event2_d2()` has unclear name and responsibility

**Refactoring**:
```python
# New structure: resolvers/country_resolver.py

class CountryResolver:
    """Resolves country labels using composition."""

    def __init__(
        self,
        basic_lookup: BasicLookupService,
        prefix_handler: PrefixHandler,
        year_handler: YearPatternHandler,
        member_handler: MemberSuffixHandler,
    ):
        self._basic = basic_lookup
        self._prefix = prefix_handler
        self._year = year_handler
        self._member = member_handler

    def resolve(self, country: str, use_fallback: bool = True) -> str:
        """Resolve country label using layered strategy."""
        if result := self._basic.lookup(country):
            return result

        if use_fallback:
            return (
                self._prefix.handle(country)
                or self._year.handle(country)
                or self._member.handle(country)
            )
        return ""

# Move event2_d2 to separate file
# resolvers/event_based_resolver.py
def event_based_resolver(category: str) -> str:
    """Handles event-based category patterns."""
    # Extract logic from lines 342-365
```

---

#### File: [`circular_dependency/ar_lab_bot.py`](../ArWikiCats/legacy_bots/circular_dependency/ar_lab_bot.py:1-586)

**Issues**:
- Lines 25-31: Global mutable list `separators_lists_raw`
- Lines 45-68: `CountryResolver` class shadows the one from country_bot.py
- Lines 71-155: Helper functions should be methods
- Lines 273-309: `TypeResolver.resolve()` has complex logic
- Lines 314-388: `Fixing.determine_separator()` is too long
- Lines 391-558: `LabelPipeline` mixes orchestration with business logic

**Refactoring**:
```python
# New structure: resolvers/arabic_label_builder.py

class ArabicLabelBuilder:
    """Builds Arabic labels from category components."""

    def __init__(
        self,
        type_resolver: TypeResolver,
        country_resolver: CountryResolver,
        preposition_handler: PrepositionHandler,
        formatter: LabelFormatter,
    ):
        self._type = type_resolver
        self._country = country_resolver
        self._preposition = preposition_handler
        self._formatter = formatter

    def build(
        self,
        category: str,
        separator: Separator,
        context: BuildContext,
    ) -> BuildResult:
        """Build an Arabic label from components."""
        components = self._extract_components(category, separator)

        type_result = self._type.resolve(
            components.type_value,
            separator,
            context,
        )
        country_result = self._country.resolve(
            components.country,
            separator,
            context,
        )

        if not (type_result and country_result):
            return BuildResult.failure()

        preposition = self._preposition.determine(
            separator,
            type_result.label,
            country_result.label,
        )

        label = self._formatter.join(
            type_result.label,
            preposition,
            country_result.label,
        )

        return BuildResult.success(label)

# Extract separator handling
# resolvers/preposition_handler.py
class PrepositionHandler:
    """Handles Arabic preposition insertion logic."""

    def determine(
        self,
        separator: Separator,
        type_label: str,
        country_label: str,
    ) -> str:
        """Determine appropriate Arabic preposition."""
        if separator.requires_preposition(type_label):
            return separator.to_arabic()
        return " "
```

---

#### File: [`circular_dependency/general_resolver.py`](../ArWikiCats/legacy_bots/circular_dependency/general_resolver.py:1-54)

**Issues**:
- Line 15: Imports from ar_lab_bot (circular)
- Line 17: Constant `en_literes` poorly named
- Lines 20-54: Function mixes multiple concerns

**Refactoring**:
```python
# New structure: resolvers/separator_based_resolver.py

class SeparatorBasedResolver:
    """Resolves categories containing relational separators."""

    def __init__(
        self,
        separator_finder: SeparatorFinder,
        arabic_builder: ArabicLabelBuilder,
    ):
        self._find_separator = separator_finder
        self._build_arabic = arabic_builder

    def resolve(self, category: str) -> str:
        """Resolve category with separator pattern."""
        separator = self._find_separator.find(category)
        if not separator:
            return ""

        result = self._build_arabic.find_label(
            category,
            separator,
            category,
        )

        if not self._contains_arabic(result):
            return ""

        return result

    @staticmethod
    def _contains_arabic(text: str) -> bool:
        """Check if text contains Arabic characters."""
        ENGLISH_PATTERN = r"[a-z]"
        return re.sub(ENGLISH_PATTERN, "", text, flags=re.IGNORECASE) != text
```

---

### 5.3 Legacy Resolvers Bots

#### File: [`legacy_resolvers_bots/event_lab_bot.py`](../ArWikiCats/legacy_bots/legacy_resolvers_bots/event_lab_bot.py:1-392)

**Issues**:
- Lines 26-34: Constants should be in constants module
- Lines 40-55: `_resolve_via_chain()` duplicates common pattern
- Lines 58-74: `translate_general_category_wrap()` is duplicate
- Lines 115-317: `EventLabResolver` class is complex (203 lines)
- Lines 320-329: `_load_resolver()` unnecessary singleton pattern

**Refactoring**:
```python
# New structure: resolvers/event_resolver.py

class EventResolver:
    """Handles event-based category resolution."""

    def __init__(
        self,
        chain_resolver: ChainResolver,
        suffix_handler: SuffixHandler,
        list_formatter: ListFormatter,
    ):
        self._chain = chain_resolver
        self._suffix = suffix_handler
        self._list_format = list_formatter

    def resolve(self, category: str) -> str:
        """Resolve event-based category."""
        suffix_result = self._suffix.handle(category)

        if suffix_result.has_list_template():
            country_result = self._chain.resolve_for_country(
                suffix_result.remainder,
            )
            if country_result:
                return self._list_format.format(
                    country_result,
                    suffix_result.template,
                )

        return self._chain.resolve_general(suffix_result.remainder)

# Extract constants
# constants/event_constants.py
class EventSuffix(Literal):
    EPISODES = " episodes"
    TEMPLATES = " templates"

class EventLabel(str):
    PEOPLE = "أشخاص"
    SPORTS_EVENTS = "أحداث رياضية"
```

---

#### File: [`legacy_resolvers_bots/with_years_bot.py`](../ArWikiCats/legacy_bots/legacy_resolvers_bots/with_years_bot.py:1-257)

**Issues**:
- Lines 25-30: List `arabic_labels_preceding_year` should be constant
- Lines 33-37: Dict `known_bodies` should be in data module
- Lines 44-50: `translate_general_category_wrap()` duplicate
- Lines 74-132: `_handle_year_at_start()` is complex
- Lines 135-187: `_handle_year_at_end()` has duplicated logic

**Refactoring**:
```python
# New structure: resolvers/year_based_resolver.py

class YearBasedResolver:
    """Resolves categories containing year patterns."""

    def __init__(
        self,
        year_extractor: YearExtractor,
        remainder_resolver: RemainderResolver,
        label_formatter: YearLabelFormatter,
    ):
        self._extract = year_extractor
        self._resolve_remainder = remainder_resolver
        self._format = label_formatter

    def resolve(self, category: str) -> str:
        """Resolve year-based category."""
        year_position = self._extract.detect_position(category)

        if year_position == Position.START:
            return self._resolve_year_at_start(category)
        elif year_position == Position.END:
            return self._resolve_year_at_end(category)

        return ""

    def _resolve_year_at_start(self, category: str) -> str:
        """Handle year at beginning of category."""
        year, remainder = self._extract.split_at_start(category)

        remainder_label = self._resolve_remainder.resolve(remainder)
        if not remainder_label:
            return ""

        return self._format.year_first(remainder_label, year)

# Extract data
# data/year_data.py
ARABIC_LABELS_PRECEDING_YEAR = frozenset([
    "كتاب بأسماء مستعارة",
    "بطولات اتحاد رجبي للمنتخبات الوطنية",
])

KNOWN_POLITICAL_BODIES = {
    "iranian majlis": "المجلس الإيراني",
    "united states congress": "الكونغرس الأمريكي",
}
```

---

#### File: [`legacy_resolvers_bots/year_or_typeo.py`](../ArWikiCats/legacy_bots/legacy_resolvers_bots/year_or_typeo.py:1-309)

**Issues**:
- Lines 37-287: `LabelForStartWithYearOrTypeo` class is complex
- Multiple instance variables create high state complexity
- Lines 213-292: `new_func_mk2()` is complex and poorly named

**Refactoring**:
```python
# New structure: resolvers/year_prefix_resolver.py

class YearPrefixResolver:
    """Resolves categories starting with year patterns."""

    def __init__(
        self,
        parser: CategoryParser,
        country_lookup: CountryLookup,
        year_formatter: YearFormatter,
        rule_engine: LabelRuleEngine,
    ):
        self._parse = parser
        self._lookup_country = country_lookup
        self._format_year = year_formatter
        self._apply_rules = rule_engine

    def resolve(self, category: str) -> str:
        """Resolve category starting with year."""
        parsed = self._parse.parse(category)

        if not parsed.has_year():
            return ""

        country_label = self._lookup_country.lookup(parsed.country)
        year_label = self._format_year.format(parsed.year)

        return self._apply_rules.apply(
            parsed=parsed,
            country_label=country_label,
            year_label=year_label,
        )

# Simplify state management
@dataclass(frozen=True)
class ParsedCategory:
    """Immutable parsed category representation."""
    original: str
    year: str
    country: str
    separator: str
```

---

#### File: [`legacy_resolvers_bots/bys.py`](../ArWikiCats/legacy_bots/legacy_resolvers_bots/bys.py:1-140)

**Issues**:
- Line 4: TODO comment says "need refactoring"
- Lines 42-58: `by_people_bot()` logic unclear
- Lines 62-88: `make_new_by_label()` complex
- Lines 97-133: `get_by_label()` has multiple responsibilities

**Refactoring**:
```python
# New structure: resolvers/by_pattern_resolver.py

class ByPatternResolver:
    """Handles 'by X' category patterns."""

    def __init__(
        self,
        people_lookup: PeopleLookup,
        dual_by_handler: DualByHandler,
        label_formatter: ByLabelFormatter,
    ):
        self._lookup_people = people_lookup
        self._handle_dual = dual_by_handler
        self._format = label_formatter

    def resolve(self, category: str) -> str:
        """Resolve 'by' pattern category."""
        if self._is_dual_by(category):
            return self._handle_dual.resolve(category)

        if category.startswith("by "):
            return self._resolve_simple_by(category)

        if " by " in category:
            return self._resolve_contained_by(category)

        return ""

    def _resolve_simple_by(self, category: str) -> str:
        """Handle categories starting with 'by '."""
        term = category[3:].strip()

        if label := self._lookup_people.lookup(term):
            return self._format.people(label)

        if label := self._lookup_general(term):
            return self._format.general(label)

        return ""
```

---

#### File: [`legacy_resolvers_bots/mk3.py`](../ArWikiCats/legacy_bots/legacy_resolvers_bots/mk3.py:1-293)

**Issues**:
- Line 3: Module docstring is just "Usage:"
- Lines 58-74: `check_country_in_tables()` is pure lookup
- Lines 77-139: `add_the_in()` has 9 parameters
- Lines 213-292: `new_func_mk2()` has 12 parameters

**Refactoring**:
```python
# New structure: resolvers/preposition_builder.py

@dataclass
class PrepositionContext:
    """Context for preposition insertion."""
    country: str
    in_table: bool
    type_value: str
    separator: str
    year_label: str
    country_label: str

class PrepositionBuilder:
    """Builds labels with appropriate prepositions."""

    def __init__(
        self,
        table_checker: TableChecker,
        preposition_rules: list[PrepositionRule],
    ):
        self._check_table = table_checker
        self._rules = preposition_rules

    def build(
        self,
        ar_label: str,
        context: PrepositionContext,
    ) -> str:
        """Build label with prepositions."""
        in_table = self._check_table.check(context.country)

        for rule in self._rules:
            if rule.matches(context, in_table):
                return rule.apply(ar_label, context)

        return ar_label

# Use dataclass to reduce parameters
@dataclass
class NewFuncContext:
    """Context for new_func_mk2 logic."""
    category: str
    cat_test: str
    year: str
    typeo: str
    in_sep: str
    country: str
    arlabel: str
    year_labe: str
    suf: str
    add_in: bool
    country_label: str
    add_in_done: bool
```

---

#### File: [`legacy_resolvers_bots/bot_2018.py`](../ArWikiCats/legacy_bots/legacy_resolvers_bots/bot_2018.py:1-113)

**Issues**:
- Line 15: Loads 524,266 entries at module import time
- Lines 24-38: Dictionary `first_data` should be in data module
- Lines 57-90: Resolver chain in `get_pop_all_18_wrap()` should use common pattern

**Refactoring**:
```python
# New structure: data_access/population_loader.py

class PopulationDataLoader:
    """Loads population data with lazy initialization."""

    def __init__(self, path: str):
        self._path = path
        self._data: dict[str, str] | None = None

    @property
    def data(self) -> dict[str, str]:
        """Lazy load population data."""
        if self._data is None:
            self._data = self._load()
            self._data.update(self._get_overrides())
        return self._data

    def _load(self) -> dict[str, str]:
        """Load from JSON file."""
        from ...translations.funcs import open_json_file
        return open_json_file(self._path)

    def _get_overrides(self) -> dict[str, str]:
        """Get hardcoded overrides."""
        return {
            "establishments": "تأسيسات",
            "disestablishments": "انحلالات",
        }

# Use common resolver pattern
# resolvers/population_resolver.py
class PopulationResolver:
    def __init__(self, sources: list[Callable[[str], str]]):
        self._sources = sources

    def resolve(self, key: str, default: str = "") -> str:
        """Resolve using chain of responsibility."""
        key = self._normalize(key)

        for source in self._sources:
            if result := source(key):
                return result

        if "-" in key:
            return self.resolve(key.replace("-", " "), default)

        return default

    @staticmethod
    def _normalize(key: str) -> str:
        """Normalize lookup key."""
        if key.startswith("the "):
            return key[len("the "):]
        return key.lower()
```

---

#### File: [`legacy_resolvers_bots/country2_label_bot.py`](../ArWikiCats/legacy_bots/legacy_resolvers_bots/country2_label_bot.py:1-400)

**Issues**:
- Lines 35-42: `get_table_with_in()` creates inline dict
- Lines 145-221: `make_cnt_lab()` is 77 lines with complex logic
- Lines 251-291: `make_parts_labels()` mixes concerns

**Refactoring**:
```python
# New structure: resolvers/two_part_resolver.py

class TwoPartResolver:
    """Resolves categories with two parts separated by a delimiter."""

    def __init__(
        self,
        part1_resolver: PartResolver,
        part2_resolver: PartResolver,
        label_combiner: LabelCombiner,
    ):
        self._resolve_part1 = part1_resolver
        self._resolve_part2 = part2_resolver
        self._combine = label_combiner

    def resolve(
        self,
        category: str,
        separator: Separator,
        with_years: bool = True,
    ) -> str:
        """Resolve two-part category."""
        if separator not in category:
            return ""

        part1, part2 = split_parts(category, separator)

        label1 = self._resolve_part1.resolve(part1, separator)
        label2 = self._resolve_part2.resolve(part2, with_years)

        if not (label1 and label2):
            return ""

        return self._combine.combine(
            label1,
            label2,
            separator,
            part1,
            part2,
        )

# Simplify make_cnt_lab
class LabelCombiner:
    """Combines two labels with appropriate separator."""

    def combine(
        self,
        label1: str,
        label2: str,
        separator: Separator,
        part1_normalized: str,
        part2_normalized: str,
    ) -> str:
        """Combine labels with separator."""
        ar_separator = separator.to_arabic()

        combined = f"{label1}{ar_separator}{label2}"

        # Apply special rules
        combined = self._apply_player_rules(combined, part1_normalized, part2_normalized)
        combined = self._apply_format_rules(combined, part1_normalized, label2)
        combined = self._normalize(combined)

        return combined
```

---

### 5.4 Make Bots

#### File: [`make_bots/bot.py`](../ArWikiCats/legacy_bots/make_bots/bot.py:1-64)

**Issues**:
- Lines 11-28: `_make_players_keys()` creates mutable global dict
- Lines 31-33: Global `Films_O_TT` dict
- Lines 36-44: `add_to_new_players()` modifies global state
- Lines 47-55: `add_to_Films_O_TT()` modifies global state

**Refactoring**:
```python
# New structure: data_access/label_registry.py

class LabelRegistry:
    """Thread-safe registry for dynamic label mappings."""

    def __init__(self, initial_data: dict[str, str] | None = None):
        self._data = dict(initial_data or {})
        self._lock = threading.RLock()

    def get(self, key: str) -> str | None:
        """Get label by key."""
        with self._lock:
            return self._data.get(key)

    def add(self, key: str, value: str) -> None:
        """Add or update a label mapping."""
        if not key or not value:
            return
        if not isinstance(key, str) or not isinstance(value, str):
            raise TypeError("Key and value must be strings")

        with self._lock:
            self._data[key] = value

    def add_batch(self, mappings: dict[str, str]) -> None:
        """Add multiple mappings at once."""
        with self._lock:
            self._data.update(mappings)

# Create singleton instances
players_registry = LabelRegistry(_build_initial_players_keys())
films_registry = LabelRegistry()
```

---

#### File: [`make_bots/check_bot.py`](../ArWikiCats/legacy_bots/make_bots/check_bot.py:1-67)

**Issues**:
- Line 17: Global list `set_tables`
- Lines 20-26: `check_key_in_tables()` is generic utility
- Lines 40-53: Inconsistent caching in `check_key_new_players()`

**Refactoring**:
```python
# New structure: data_access/table_checker.py

class TableChecker:
    """Checks for key existence across multiple tables."""

    def __init__(self, tables: list[Mapping[str, Any]]):
        self._tables = list(tables)

    def check(self, key: str) -> bool:
        """Check if key exists in any table."""
        key_lower = key.lower()
        return any(
            key in table or key_lower in table
            for table in self._tables
        )

    def check_with_callback(
        self,
        key: str,
        callback: Callable[[str, str], None],
    ) -> bool:
        """Check and call callback with table name on match."""
        key_lower = key.lower()

        for table in self._tables:
            if key in table:
                callback(key, table.__class__.__name__)
                return True
            if key_lower in table:
                callback(key_lower, table.__class__.__name__)
                return True

        return False

# Remove caching at this level
# Let callers handle caching strategy
```

---

#### File: [`make_bots/reg_result.py`](../ArWikiCats/legacy_bots/make_bots/reg_result.py:1-91)

**Issues**:
- Lines 38-45: `TypiesResult` dataclass has primitive fields
- Lines 47-51: `get_cats()` function name unclear
- Lines 54-90: `get_reg_result()` is complex

**Refactoring**:
```python
# New structure: core/category_parser.py

@dataclass(frozen=True)
class ParsedCategory:
    """Immutable result of parsing a category string."""

    original: str
    normalized: str
    year_prefix: str | None
    separator: Separator | None
    country: str | None
    remainder: str

    @classmethod
    def parse(cls, category: str) -> "ParsedCategory":
        """Parse a category string into components."""
        normalized = _normalize(category)

        match = _CATEGORY_PATTERN.match(normalized)
        if not match:
            return cls(category, normalized, None, None, None, normalized)

        return cls(
            original=category,
            normalized=normalized,
            year_prefix=match.group("year"),
            separator=Separator.from_string(match.group("separator")) if match.group("separator") else None,
            country=match.group("country"),
            remainder=_extract_remainder(normalized, match),
        )
```

---

#### File: [`make_bots/table1_bot.py`](../ArWikiCats/legacy_bots/make_bots/table1_bot.py:1-81)

**Issues**:
- Lines 18-24: `KAKO` dict structure nested
- Lines 28-60: `_get_KAKO()` has mixed responsibilities
- Lines 64-75: `get_KAKO()` is just a wrapper

**Refactoring**:
```python
# New structure: data_access/composite_resolver.py

class CompositeResolver:
    """Resolves labels from multiple sources."""

    def __init__(self, sources: dict[str, Callable[[str], str]]):
        self._sources = sources

    def resolve(self, text: str) -> tuple[str, str]:
        """
        Resolve label from first matching source.

        Returns:
            (source_name, label) tuple
        """
        for source_name, source_func in self._sources.items():
            if result := source_func(text):
                if not isinstance(result, str):
                    raise TypeError(
                        f"Source '{source_name}' returned "
                        f"non-string type {type(result)}"
                    )
                return source_name, result

        return "", ""

    def resolve_label_only(self, text: str) -> str:
        """Resolve and return only the label."""
        _, label = self.resolve(text)
        return label

# Build sources from dependencies
def build_composite_resolver(
    by_resolver: ByResolver,
    films_table: dict[str, str],
    players_table: dict[str, str],
    jobs_data: dict[str, str],
    jobs_new: dict[str, str],
) -> CompositeResolver:
    """Build a composite resolver from dependencies."""
    sources = {
        "resolve_by_labels": by_resolver.resolve,
        "Films_key_man": lambda k: films_table.get(k, ""),
        "players_new_keys": lambda k: players_table.get(k, ""),
        "jobs_mens_data": lambda k: jobs_data.get(k, ""),
        "Jobs_new": lambda k: jobs_new.get(k, ""),
    }
    return CompositeResolver(sources)
```

---

### 5.5 Legacy Utils

#### File: [`legacy_utils/data.py`](../ArWikiCats/legacy_bots/legacy_utils/data.py:1-47)

**Issues**:
- Lines 4-6: Hardcoded lists
- Lines 28-38: `Add_in_table` list unclear purpose

**Refactoring**:
```python
# Move to constants/label_rules.py
@dataclass(frozen=True)
class LabelRule:
    """Rule for label formatting."""
    name: str
    values: frozenset[str]

class PredefinedSets:
    """Predefined sets for label rules."""

    KEEP_IT_LAST = frozenset([
        "remakes of",
    ])

    KEEP_IT_FIRST = frozenset([
        "spaceflight",
        "lists of",
        "actors in",
        # ...
    ])

    ADD_IN_TABLE = frozenset([
        "historical documents",
        "road incidents",
        # ...
    ])
```

---

#### File: [`legacy_utils/fixing.py`](../ArWikiCats/legacy_bots/legacy_utils/fixing.py:1-38)

**Issues**:
- Lines 17-22: Hardcoded list `sps_list`
- Line 28: Replaces in loop inefficiently

**Refactoring**:
```python
# New structure: core/label_formatter.py

class LabelCleaner:
    """Cleans and normalizes Arabic labels."""

    DEFAULT_PREPOSITIONS = frozenset(["من", "في", "و"])

    def __init__(
        self,
        prepositions: frozenset[str] = DEFAULT_PREPOSITIONS,
    ):
        self._prepositions = prepositions

    def clean(
        self,
        label: str,
        separator: str = "",
    ) -> str:
        """Clean duplicate spaces and repeated prepositions."""
        label = " ".join(label.strip().split())

        prepositions_to_check = self._prepositions | {separator.strip()}

        for prep in prepositions_to_check:
            label = self._remove_duplicates(prep, label)

        return " ".join(label.strip().split())

    def _remove_duplicates(self, preposition: str, label: str) -> str:
        """Remove duplicate prepositions."""
        pattern = rf" {preposition}\s+{preposition} "
        replacement = f" {preposition} "

        label = re.sub(pattern, replacement, label)

        if preposition == "و":
            label = re.sub(rf" {preposition} ", f" {preposition}", label)

        return label
```

---

#### File: [`legacy_utils/joint_class.py`](../ArWikiCats/legacy_bots/legacy_utils/joint_class.py:1-93)

**Issues**:
- Lines 14-24: Class has only one method with dependencies
- Lines 25-54: `_check_prefixes()` mixes concerns
- Lines 56-69: `_check_regex_years()` creates regex patterns

**Refactoring**:
```python
# New structure: resolvers/prefix_handlers.py

class GenderPrefixHandler:
    """Handles gender-based prefixes (men's/women's)."""

    PREFIX_LABELS = {
        "women's ": "نسائية",
        "men's ": "رجالية",
    }

    def handle(
        self,
        text: str,
        resolver: Callable[[str], str],
    ) -> str:
        """Handle gender prefixes."""
        for prefix, label in self.PREFIX_LABELS.items():
            if text.startswith(prefix):
                remainder = text[len(prefix):]
                remainder_label = resolver(remainder)

                if remainder_label:
                    return f"{remainder_label} {label}"

        return ""

class MemberSuffixHandler:
    """Handles 'members of' suffix patterns."""

    PATTERN = re.compile(r" members of$")

    def handle(
        self,
        text: str,
        nationalities: dict[str, str],
    ) -> str:
        """Handle member suffix patterns."""
        match = self.PATTERN.search(text)
        if not match:
            return ""

        base = text[: match.start()].strip()
        label = nationalities.get(base)

        if label:
            return f"{label} أعضاء في  "

        return ""
```

---

#### File: [`legacy_utils/utils.py`](../ArWikiCats/legacy_bots/legacy_utils/utils.py:1-236)

**Issues**:
- Lines 13-93: `split_text_by_separator()` is complex (81 lines)
- Lines 96-115: `_split_category_by_separator()` duplicates logic
- Lines 117-146: `_adjust_separator_position()` has nested logic
- Lines 148-184: `_apply_regex_extraction()` complex

**Refactoring**:
```python
# New structure: core/separator_parser.py

class SeparatorParser:
    """Parses category strings using separators."""

    def __init__(
        self,
        normalizer: TextNormalizer,
        regex_extractor: RegexExtractor,
    ):
        self._normalize = normalizer
        self._extract = regex_extractor

    def parse(
        self,
        category: str,
        separator: Separator,
    ) -> ParsedParts:
        """Parse category into parts using separator."""
        category = self._normalize.normalize(category)

        if separator not in category:
            return ParsedParts.empty()

        parts = self._split_once(category, separator)

        if self._has_multiple_separators(category, separator):
            return self._parse_multiple(category, separator, parts)

        return self._parse_single(category, separator, parts)

    def _split_once(
        self,
        category: str,
        separator: Separator,
    ) -> tuple[str, str]:
        """Split on first occurrence."""
        idx = category.lower().find(separator.lower())
        return category[:idx], category[idx + len(separator):]
```

---

### 5.6 End Start Bots

#### File: [`end_start_bots/fax2.py`](../ArWikiCats/legacy_bots/end_start_bots/fax2.py:1-65)

**Issues**:
- Lines 16-64: `get_list_of_and_cat3()` has complex conditional logic
- Multiple hardcoded patterns

**Refactoring**:
```python
# New structure: matchers/pattern_matcher.py

class SuffixMatcher:
    """Matches category suffixes and extracts templates."""

    def __init__(self, patterns: dict[str, SuffixPattern]):
        self._patterns = self._sort_patterns(patterns)

    def match(
        self,
        category: str,
    ) -> MatchResult:
        """Match category against suffix patterns."""
        # Try prefixes first
        for pattern in self._prefix_patterns:
            if category.startswith(pattern.key):
                return self._apply_prefix(category, pattern)

        # Try suffixes
        for pattern in self._suffix_patterns:
            if category.endswith(pattern.key):
                return self._apply_suffix(category, pattern)

        # Special patterns
        if self._is_footballers(category):
            return self._handle_footballers(category)

        return MatchResult.none()

    def _sort_patterns(
        self,
        patterns: dict[str, SuffixPattern],
    ) -> list[SuffixPattern]:
        """Sort patterns by specificity (spaces, then length)."""
        return sorted(
            patterns.values(),
            key=lambda p: (-p.key.count(" "), -len(p.key)),
        )
```

---

#### File: [`end_start_bots/utils.py`](../ArWikiCats/legacy_bots/end_start_bots/utils.py:1-126)

**Issues**:
- Lines 6-45: `_get_from_dict()` is complex generic function
- Lines 48-87: `get_from_starts_dict()` wraps generic
- Lines 90-125: `get_from_endswith_dict()` wraps generic

**Refactoring**:
```python
# New structure: matchers/dictionary_matcher.py

class DictionaryMatcher:
    """Matches categories against dictionary patterns."""

    def __init__(self, patterns: dict[str, PatternEntry]):
        self._patterns = self._prepare_patterns(patterns)

    def match_startswith(
        self,
        category: str,
    ) -> MatchResult:
        """Match category against startswith patterns."""
        category_original = category

        for pattern in self._patterns:
            if category_original.startswith(pattern.remove_key):
                remainder = category_original[len(pattern.remove_key):]
                return MatchResult(
                    template=pattern.template,
                    remainder=remainder,
                    matched_key=pattern.key,
                )

        return MatchResult.none()

    def match_endswith(
        self,
        category: str,
    ) -> MatchResult:
        """Match category against endswith patterns."""
        category_original = category

        for pattern in self._patterns:
            if category_original.endswith(pattern.remove_key):
                remainder = category_original[: -len(pattern.remove_key)]
                return MatchResult(
                    template=pattern.template,
                    remainder=remainder,
                    matched_key=pattern.key,
                )

        return MatchResult.none()

@dataclass(frozen=True)
class PatternEntry:
    """Single pattern entry."""
    key: str
    template: str
    remove_key: str
    example: str = ""
```

---

### 5.7 Data Module

#### File: [`data/mappings.py`](../ArWikiCats/legacy_bots/data/mappings.py:1-329)

**Issues**:
- Lines 16-146: Programmatic generation of number mappings
- Lines 153-274: Two large dictionaries merged
- Lines 281-287: Prefix mappings
- Lines 294-317: Type table

**Current State**: Already partially refactored (good consolidation)

**Recommended Changes**:
1. Split into separate modules by domain
2. Add documentation for mappings
3. Consider using YAML/JSON for static data

```python
# Proposed structure
data/
├── __init__.py
├── number_mappings.py    # Lines 16-146
├── suffix_mappings.py    # Lines 153-274
├── prefix_mappings.py    # Lines 281-287
└── type_mappings.py      # Lines 294-317
```

---

### 5.8 Utils

#### File: [`utils/regex_hub.py`](../ArWikiCats/legacy_bots/utils/regex_hub.py:1-84)

**Current State**: Well-organized centralization of regex patterns

**Recommended Changes**:
1. Add docstrings explaining each pattern's purpose
2. Use `enum` for pattern types
3. Add compilation validation

```python
# Enhanced version
from enum import Enum

class RegexPattern(Enum):
    """Pre-compiled regex patterns for category matching."""

    YEAR_AT_START = re.compile(r"^(\d+\-\d+|\d+\–\d+|\d+\−\d+|\d\d\d\d).*", re.I)
    YEAR_AT_END = re.compile(r"^.*?\s*(\d+\-\d+|\d+\–\d+|\d+\−\d+|\d\d\d\d)$", re.I)
    # ... etc

    @property
    def pattern(self) -> re.Pattern:
        """Get the compiled regex pattern."""
        return self.value

    def match(self, text: str) -> re.Match | None:
        """Match the pattern against text."""
        return self.pattern.match(text)
```

---

## 6. Technical Debt Risks

### 6.1 High Risk Items

| Risk | Impact | Files Affected | Mitigation |
|------|--------|----------------|------------|
| Circular imports | Runtime failures, untestable code | `circular_dependency/` (all) | Phase 1 refactoring |
| Mutable global state | Race conditions, cache invalidation | `make_bots/bot.py`, `bot_2018.py` | Phase 4 refactoring |
| No dependency injection | Tight coupling, hard to test | All modules | Phase 3 refactoring |
| Excessive cache sizes | Memory pressure | `__init__.py`, `country_bot.py` | Review and reduce |

### 6.2 Medium Risk Items

| Risk | Impact | Files Affected | Mitigation |
|------|--------|----------------|------------|
| Duplicate resolver chains | Maintenance burden | 8+ files | Create common base class |
| Magic strings | Typos, poor maintainability | All files | Phase 2 refactoring |
| Long methods | Bug-prone, hard to test | `ar_lab_bot.py`, `country2_label_bot.py` | Phase 5 refactoring |

### 6.3 Low Risk Items

| Risk | Impact | Files Affected | Mitigation |
|------|--------|----------------|------------|
| TODO comments | Technical debt indicators | `bys.py`, `with_years_bot.py` | Address or remove |
| Inconsistent naming | Confusion | Various | Standardize conventions |

---

## 7. Success Criteria

Refactoring should achieve:

1. **Zero circular dependencies** - All imports must form a DAG
2. **Testability** - 80%+ unit test coverage possible without mocking internals
3. **Composability** - Resolvers can be combined/reordered without code changes
4. **Type safety** - Full type hints coverage, mypy strict mode passing
5. **Performance** - No regression in resolution speed (benchmark before/after)
6. **Documentation** - Every public API has clear docstring with examples

---

## 8. Summary Statistics

| Metric | Current | Target |
|--------|---------|--------|
| Circular import cycles | 1 documented | 0 |
| Files with >300 lines | 4 | 0 |
| Methods with >50 lines | 8 | 0 |
| Global mutable dicts | 3 | 0 |
| Modules with >5 external dependencies | 5 | 0 |
| Test coverage | Unknown | >80% |

---

## 9. Refactoring Checklist

### Phase 1: Break Circular Dependencies

- [ ] **Infrastructure Setup**
  - [ ] Create `resolvers/` directory to replace `circular_dependency/`
  - [ ] Create `resolvers/interface.py` for abstract base classes
  - [ ] Create `resolvers/__init__.py` for clean imports

- [ ] **Data Extraction**
  - [ ] Extract `ar_lab_bot.find_ar_label()` to a separate module
  - [ ] Extract `event2_d2` logic from `country_bot.py` to `resolvers/event_based_resolver.py`

- [ ] **Module Refactoring**
  - [ ] Refactor `country_bot.py` -> `resolvers/country_resolver.py` using composition
  - [ ] Refactor `ar_lab_bot.py` -> `resolvers/arabic_label_builder.py` and `resolvers/preposition_handler.py`
  - [ ] Refactor `general_resolver.py` -> `resolvers/separator_based_resolver.py`
  - [ ] Refactor `sub_general_resolver.py` (if applicable) or merge logic
  - [ ] Delete `circular_dependency/` directory once empty

### Phase 2: Extract Value Objects & Constants

- [ ] **Constants Package**
  - [ ] Create `constants/` directory and `__init__.py`
  - [ ] Create `constants/suffixes.py` (from `data/mappings.py`)
  - [ ] Create `constants/prefixes.py` (from `data/mappings.py`)
  - [ ] Create `constants/separators.py` with `Separator` class and `VALID_SEPARATORS`
  - [ ] Create `constants/patterns.py` for regex constants
  - [ ] Create `constants/event_constants.py` (from `legacy_resolvers_bots/event_lab_bot.py`)
  - [ ] Create `constants/label_rules.py` (from `legacy_utils/data.py` - `Add_in_table`, etc.)

- [ ] **Type Definitions**
  - [ ] Define `Category`, `ArabicLabel` value objects

### Phase 3: Implement Composition Over Inheritance

- [ ] **CountryResolver Redesign**
  - [ ] Implement `CountryResolver` with `_lookup_chain` (composition)
  - [ ] Replace `CountryLabelRetriever` inheritance hierarchy

- [ ] **ArabicLabelBuilder Redesign**
  - [ ] Implement `ArabicLabelBuilder` taking `CountryResolver`, `TypeResolver`, `PrepositionHandler`
  - [ ] Update `LabelPipeline.build()` to use composition

### Phase 4: Centralize Data Access

- [ ] **Data Access Layer**
  - [ ] Create `data_access/` directory and `__init__.py`
  - [ ] Create `data_access/label_registry.py` (Thread-safe registry for `players_new_keys`, `Films_O_TT`)
  - [ ] Create `data_access/table_checker.py` (Refactor `make_bots/check_bot.py`)
  - [ ] Create `data_access/composite_resolver.py` (Refactor `make_bots/table1_bot.py`)
  - [ ] Create `data_access/population_loader.py` (Refactor `legacy_resolvers_bots/bot_2018.py`)
  - [ ] Create `data_access/repositories.py`

- [ ] **Data Files**
  - [ ] Extract `known_political_bodies` from `legacy_resolvers_bots/with_years_bot.py` to `data/year_data.py`
  - [ ] Extract `arabic_labels_preceding_year` from `legacy_resolvers_bots/with_years_bot.py` to `data/year_data.py`
  - [ ] Refactor `data/mappings.py` into `data/number_mappings.py`, `data/suffix_mappings.py`, `data/prefix_mappings.py`, `data/type_mappings.py`

### Phase 5: Reduce Method Complexity

- [ ] **Specific Method Refactoring**
  - [ ] `ar_lab_bot.py`: Refactor `determine_separator()` -> `SeparatorStrategy`
  - [ ] `country_bot.py`: Refactor `_handle_type_lab_logic()`
  - [ ] `country2_label_bot.py`: Refactor `make_cnt_lab()` -> `LabelCombiner.combine()`

### Phase 6: Standardize Error Handling

- [ ] **Core Types**
  - [ ] Create `core/types.py` with `ResolutionResult` dataclass
  - [ ] Create `core/exceptions.py` with `ResolutionError` and subclasses
  - [ ] Update resolvers to return `Result` objects or handle exceptions properly (optional, vs empty strings)

### Phase 7: Improve Testability

- [ ] **Dependency Injection**
  - [ ] Update all resolver constructors to accept dependencies
  - [ ] Remove global state usage (`Films_O_TT`, etc.) in functions
  - [ ] Create `core/category_parser.py` with `ParsedCategory` (Refactor `make_bots/reg_result.py`)
  - [ ] Create `core/label_formatter.py` (Refactor `legacy_utils/fixing.py`)
  - [ ] Create `core/separator_parser.py` (Refactor `legacy_utils/utils.py`)
  - [ ] Refactor `legacy_utils/joint_class.py` -> `resolvers/prefix_handlers.py`

### Concrete File Refactoring Steps

#### entry point (`__init__.py`)
- [ ] Add `Resolver` Protocol type hint
- [ ] Define `RESOLVER_PIPELINE` list
- [ ] Reduce cache size on `legacy_resolvers` and normalize input key

#### `legacy_resolvers_bots/event_lab_bot.py`
- [ ] Refactor into `resolvers/event_resolver.py`
- [ ] Implement `EventResolver` class
- [ ] Extract constants to `constants/event_constants.py`
- [ ] Remove duplicate `translate_general_category_wrap`

#### `legacy_resolvers_bots/with_years_bot.py`
- [ ] Refactor into `resolvers/year_based_resolver.py`
- [ ] Implement `YearBasedResolver` class
- [ ] Extract data to `data/year_data.py`

#### `legacy_resolvers_bots/year_or_typeo.py`
- [ ] Refactor into `resolvers/year_prefix_resolver.py`
- [ ] Implement `YearPrefixResolver` class
- [ ] Simplify `new_func_mk2` logic

#### `legacy_resolvers_bots/bys.py`
- [ ] Refactor into `resolvers/by_pattern_resolver.py`
- [ ] Implement `ByPatternResolver` class

#### `legacy_resolvers_bots/mk3.py`
- [ ] Refactor into `resolvers/preposition_builder.py`
- [ ] Implement `PrepositionBuilder` and `PrepositionContext`

#### `legacy_resolvers_bots/country2_label_bot.py`
- [ ] Refactor into `resolvers/two_part_resolver.py`
- [ ] Implement `TwoPartResolver` class with `LabelCombiner`

#### `end_start_bots/fax2.py`
- [ ] Refactor into `matchers/pattern_matcher.py`
- [ ] Implement `SuffixMatcher` class

#### `end_start_bots/utils.py`
- [ ] Refactor into `matchers/dictionary_matcher.py`
- [ ] Implement `DictionaryMatcher` and `PatternEntry`

#### `utils/regex_hub.py`
- [ ] Enhance with `RegexPattern` Enum
- [ ] Add docstrings to patterns

**Analysis Complete**

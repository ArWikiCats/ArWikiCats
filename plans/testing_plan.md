# 📋 ArWikiCats Testing Plan

This document outlines a comprehensive testing strategy for the ArWikiCats Arabic Wikipedia Categories Translation Engine.

---

## Table of Contents

1. [Testing Strategy](#1-testing-strategy)
2. [Testing Tools and Mocking Strategy](#2-testing-tools-and-mocking-strategy)
3. [Test File Structure](#3-test-file-structure)
4. [Module-by-Module Testing Plans](#4-module-by-module-testing-plans)
5. [Test Quality Standards](#5-test-quality-standards)
6. [Practical Test Examples](#6-practical-test-examples)
7. [Configuration](#7-configuration)
8. [Implementation Plan](#8-implementation-plan)
9. [Success Metrics and CI/CD Integration](#9-success-metrics-and-cicd-integration)

---

## 1. Testing Strategy

### 1.1 Unit Testing

**Goal**: Test individual functions and classes in isolation.

**Scope**:
- Translation functions (e.g., `resolve_label`, `resolve_label_ar`)
- Pattern matching functions (country, time, nationality patterns)
- Utility functions (normalization, string manipulation)
- Configuration loading and validation
- Data structure operations (CategoryResult, ProcessedCategory)

**Characteristics**:
- Fast execution (< 1 second per test)
- No external dependencies
- Pure function testing
- Edge case coverage

### 1.2 Integration Testing

**Goal**: Test interactions between multiple modules.

**Scope**:
- End-to-end category translation workflows
- Resolver chain integration (main_resolve.py coordination)
- Bot integration (event2bot, event_lab_bot)
- Cache behavior across module boundaries
- Configuration propagation

**Characteristics**:
- Tests multiple modules together
- Validates data flow between components
- Tests resolver priority and fallback behavior
- May use fixtures for test data

### 1.3 Fixtures Strategy

**Goal**: Provide consistent, reusable test data.

**Types of Fixtures**:

```python
# 1. Category fixtures - Input test categories
@pytest.fixture
def simple_category():
    return "Category:2015 in Yemen"

@pytest.fixture
def complex_category():
    return "Category:1550s establishments in Namibia"

@pytest.fixture
def category_batch():
    return [
        "Category:2015 American television",
        "Category:1999 establishments in Europe",
        "Category:Belgian cyclists",
    ]

# 2. Expected result fixtures
@pytest.fixture
def expected_yemen_label():
    return "تصنيف:2015 في اليمن"

# 3. Translation data fixtures
@pytest.fixture
def nationality_translations():
    return {
        "Belgian": "بلجيكي",
        "American": "أمريكي",
    }

# 4. Configuration fixtures
@pytest.fixture
def test_config():
    return Config(
        print=PrintConfig(noprint=True),
        app=AppConfig(
            save_data_path="",
        ),
    )
```

**Fixture Organization**:
- `tests/conftest.py` - Global fixtures
- `tests/{module}/conftest.py` - Module-specific fixtures
- `tests/fixtures/` - JSON/data file fixtures

---

## 2. Testing Tools and Mocking Strategy

### 2.1 Testing Framework Stack

| Tool | Purpose | Version |
|------|---------|---------|
| pytest | Test framework | >=7.0 |
| pytest-cov | Coverage reporting | >=4.0 |
| pytest-mock | Mocking utilities | >=3.0 |
| pytest-xdist | Parallel execution | >=3.0 |
| pytest-timeout | Test timeouts | >=2.0 |

### 2.2 Mocking Strategy

**When to Mock**:
- External dependencies (file I/O, caching)
- Slow operations during unit tests
- Non-deterministic behavior
- Configuration settings

**What NOT to Mock**:
- Core translation logic
- Pattern matching algorithms
- Dictionary lookups (use fixtures instead)

**Mocking Patterns**:

```python
# 1. Mock caching for isolated tests
@pytest.fixture
def no_cache(mocker):
    mocker.patch.object(resolve_label, 'cache_clear')
    mocker.patch.object(resolve_label, 'cache_info', return_value=None)

# 3. Mock resolver chain for unit tests
@pytest.fixture
def mock_resolver_chain(mocker):
    mocker.patch('ArWikiCats.main_processers.event_lab_bot.event_Lab', return_value="")
```

### 2.3 Test Isolation

```python
# Clear LRU cache between tests when needed
@pytest.fixture(autouse=True)
def clear_caches():
    resolve_label.cache_clear()
    yield
    resolve_label.cache_clear()
```

---

## 3. Test File Structure

### 3.1 Complete Test Directory Structure

```
tests/
├── conftest.py                    # Global fixtures and configuration
├── fixtures/
│   ├── categories.json            # Category test data
│   ├── expected_results.json      # Expected translation results
│   └── edge_cases.json            # Edge case test data
│
├── unit/
│   ├── test_event_processing.py   # EventProcessor unit tests
│   ├── test_config.py             # Configuration tests
│   ├── test_category_result.py    # Data structure tests
│   │
│   ├── main_processers/
│   │   ├── test_main_resolve.py   # Core resolver tests
│   │   ├── test_event2bot.py      # Event2 bot tests
│   │   └── test_event_lab_bot.py  # Event Lab bot tests
│   │
│   ├── patterns_resolvers/
│   │   ├── test_country_time_pattern.py
│   │   └── test_nat_males_pattern.py
│   │
│   ├── time_formats/
│   │   ├── test_labs_years.py
│   │   ├── test_time_to_arabic.py
│   │   └── test_utils_time.py
│   │
│   ├── new_resolvers/
│   │   ├── test_resolve_all.py
│   │   ├── test_nationalities_resolvers.py
│   │   ├── test_jobs_resolvers.py
│   │   └── test_sports_resolvers.py
│   │
│   ├── utils/
│   │   ├── test_match_relation_word.py
│   │   ├── test_fixing.py
│   │   └── test_check_it.py
│   │
│   ├── translations/
│   │   ├── test_geo_translations.py
│   │   ├── test_sports_translations.py
│   │   ├── test_jobs_translations.py
│   │   └── test_medical_translations.py
│   │
│   └── fix/
│       ├── test_fixlabel.py
│       ├── test_fixtitle.py
│       └── test_specific_normalizations.py
│
├── integration/
│   ├── test_end_to_end.py         # Full workflow tests
│   ├── test_batch_processing.py   # Batch category tests
│   ├── test_resolver_chain.py     # Resolver integration
│   └── test_cache_integration.py  # Caching behavior
│
├── regression/
│   ├── test_known_categories.py   # Known working categories
│   ├── test_bug_fixes.py          # Previously fixed bugs
│   └── test_edge_cases.py         # Edge case regressions
│
└── performance/
    ├── test_speed.py              # Performance benchmarks
    └── test_memory.py             # Memory usage tests
```

### 3.2 Test File Naming Conventions

| Pattern | Purpose |
|---------|---------|
| `test_*.py` | Test files |
| `*Test.py` | Alternative test files |
| `conftest.py` | Fixture files |
| `test_*_unit.py` | Unit test files |
| `test_*_integration.py` | Integration test files |

---

## 4. Module-by-Module Testing Plans

### Priority Levels

| Priority | Meaning |
|----------|---------|
| P0 | Critical - Must have tests |
| P1 | High - Should have tests |
| P2 | Medium - Nice to have tests |
| P3 | Low - Optional tests |

### 4.1 Core Modules (P0 - Critical)

#### `main_processers/main_resolve.py`

| Component | Test Focus | Priority |
|-----------|-----------|----------|
| `resolve_label()` | All input types, caching, fallback | P0 |
| `resolve_label_ar()` | Arabic output format | P0 |
| `CategoryResult` | Data structure integrity | P0 |
| `build_labs_years_object()` | Singleton behavior | P1 |

**Test Cases**:
- Simple category resolution
- Complex pattern matching
- Fallback chain behavior
- Cache hit/miss scenarios
- Invalid input handling
- Arabic text encoding

#### `event_processing.py`

| Component | Test Focus | Priority |
|-----------|-----------|----------|
| `EventProcessor.process()` | Batch processing | P0 |
| `EventProcessor.process_single()` | Single category | P0 |
| `_normalize_category()` | Normalization rules | P0 |
| `_prefix_label()` | Prefix handling | P0 |
| `batch_resolve_labels()` | Batch interface | P0 |

### 4.2 Pattern Resolvers (P0-P1)

#### `patterns_resolvers/country_time_pattern.py`

| Test Case | Example | Priority |
|-----------|---------|----------|
| Country + Year | "2015 in Yemen" | P0 |
| Country + Decade | "1990s in France" | P0 |
| Country + Century | "19th century in Egypt" | P1 |
| Invalid patterns | "in invalid" | P0 |

#### `patterns_resolvers/nat_males_pattern.py`

| Test Case | Example | Priority |
|-----------|---------|----------|
| Nationality + Job | "Belgian cyclists" | P0 |
| Nationality + Gender | "French women" | P0 |
| Complex patterns | "American male actors" | P1 |

### 4.3 Time Resolvers (P0-P1)

#### `time_formats/*.py`

| Test Case | Priority |
|-----------|----------|
| Year extraction | P0 |
| Decade handling | P0 |
| Century conversion | P1 |
| BC/BCE years | P1 |
| Invalid years | P0 |

### 4.4 New Resolvers (P1)

#### `new_resolvers/reslove_all.py`

| Test Case | Priority |
|-----------|----------|
| Nationality resolution | P1 |
| Job resolution | P1 |
| Sports resolution | P1 |
| Fallback behavior | P1 |

### 4.5 Translation Data (P1-P2)

| Module | Test Focus | Priority |
|--------|-----------|----------|
| `translations/geo/` | Geography translations | P1 |
| `translations/sports/` | Sports translations | P1 |
| `translations/jobs/` | Job translations | P1 |
| `translations/medical/` | Medical translations | P2 |

### 4.6 Utilities (P1-P2)

| Module | Test Focus | Priority |
|--------|-----------|----------|
| `utils/match_relation_word.py` | Pattern matching | P1 |
| `utils/fixing.py` | String fixes | P1 |
| `helps/log.py` | Logging | P2 |
| `helps/memory.py` | Memory utils | P2 |

### 4.7 Fix Module (P1)

| Component | Test Focus | Priority |
|-----------|-----------|----------|
| `fixlabel()` | Label correction | P1 |
| `fixtitle.py` | Title fixes | P1 |
| `specific_normalizations.py` | Special cases | P1 |

---

## 5. Test Quality Standards

### 5.1 Coverage Target

**Overall Goal**: 80%+ code coverage

| Module Type | Target Coverage |
|-------------|-----------------|
| Core modules | 90%+ |
| Pattern resolvers | 85%+ |
| Time resolvers | 85%+ |
| Utilities | 75%+ |
| Translations | 70%+ |

### 5.2 Test Quality Criteria

**Each test must**:
- Have a clear, descriptive name
- Test one specific behavior
- Include assertion messages
- Handle edge cases
- Be independent and isolated
- Execute in < 1 second (unit) or < 10 seconds (integration)

### 5.3 Test Documentation

```python
def test_resolve_label_with_year_and_country():
    """
    Test that resolve_label correctly translates a category
    with both year and country components.

    Input: "2015 in Yemen"
    Expected: "2015 في اليمن"
    """
    result = resolve_label("2015 in Yemen")
    assert result.ar == "2015 في اليمن", f"Expected Arabic translation, got {result.ar}"
```

### 5.4 Test Markers

```python
@pytest.mark.unit
@pytest.mark.fast
def test_fast_unit_test():
    pass

@pytest.mark.integration
@pytest.mark.slow
def test_slow_integration_test():
    pass

@pytest.mark.dict
def test_dictionary_lookup():
    pass
```

---

## 6. Practical Test Examples

### 6.1 Example 1: Unit Test for EventProcessor

```python
# tests/unit/test_event_processing.py

import pytest
from ArWikiCats.event_processing import (
    EventProcessor,
    ProcessedCategory,
    EventProcessingResult,
)


class TestEventProcessor:
    """Test suite for EventProcessor class."""

    @pytest.fixture
    def processor(self):
        """Create a fresh EventProcessor instance."""
        return EventProcessor()

    @pytest.mark.unit
    def test_normalize_category_removes_bom(self, processor):
        """Test that BOM character is removed from category."""
        category = "\ufeffTest Category"
        result = processor._normalize_category(category)
        assert result == "Test Category"

    @pytest.mark.unit
    def test_normalize_category_replaces_underscores(self, processor):
        """Test that underscores are replaced with spaces."""
        category = "Test_Category_Name"
        result = processor._normalize_category(category)
        assert result == "Test Category Name"

    @pytest.mark.unit
    def test_prefix_label_adds_prefix(self, processor):
        """Test that Arabic prefix is added correctly."""
        raw_label = "2015 في اليمن"
        result = processor._prefix_label(raw_label)
        assert result == "تصنيف:2015 في اليمن"

    @pytest.mark.unit
    def test_prefix_label_skips_empty(self, processor):
        """Test that empty labels return empty string."""
        assert processor._prefix_label("") == ""
        assert processor._prefix_label("   ") == ""

    @pytest.mark.unit
    def test_prefix_label_skips_existing_prefix(self, processor):
        """Test that existing prefix is not duplicated."""
        labeled = "تصنيف:Already Prefixed"
        result = processor._prefix_label(labeled)
        assert result == "تصنيف:Already Prefixed"

    @pytest.mark.unit
    def test_process_single_valid_category(self, processor):
        """Test processing a single valid category."""
        result = processor.process_single("2015 in Yemen")

        assert isinstance(result, ProcessedCategory)
        assert result.original == "2015 in Yemen"
        assert result.normalized == "2015 in Yemen"
        # Note: actual translation depends on resolver

    @pytest.mark.unit
    def test_process_batch_returns_result_object(self, processor):
        """Test that batch processing returns EventProcessingResult."""
        categories = ["Category:Test1", "Category:Test2"]
        result = processor.process(categories)

        assert isinstance(result, EventProcessingResult)
        assert isinstance(result.processed, list)
        assert isinstance(result.labels, dict)
        assert isinstance(result.no_labels, list)

    @pytest.mark.unit
    def test_process_skips_empty_categories(self, processor):
        """Test that empty categories are skipped."""
        categories = ["Valid Category", "", "Another Valid"]
        result = processor.process(categories)

        assert len(result.processed) == 2
```

### 6.2 Example 2: Integration Test for Resolver Chain

```python
# tests/integration/test_resolver_chain.py

import pytest
from ArWikiCats import (
    resolve_arabic_category_label,
    batch_resolve_labels,
)


class TestResolverChainIntegration:
    """Integration tests for the complete resolver chain."""

    @pytest.mark.integration
    def test_year_country_pattern_resolution(self):
        """
        Test end-to-end resolution of year + country pattern.

        This tests the integration of:
        - EventProcessor
        - main_resolve
        - country_time_pattern resolver
        - fixlabel
        """
        result = resolve_arabic_category_label("2015 in Yemen")
        assert result == "تصنيف:2015 في اليمن"

    @pytest.mark.integration
    def test_decade_country_pattern_resolution(self):
        """
        Test resolution of decade + country establishment pattern.

        Expected flow:
        1. EventProcessor normalizes input
        2. LabsYearsFormat extracts decade (1550s)
        3. Pattern matcher identifies establishment pattern
        4. Translation generates Arabic output
        """
        result = resolve_arabic_category_label("1550s establishments in Namibia")
        assert "1550" in result
        assert "ناميبيا" in result

    @pytest.mark.integration
    def test_nationality_job_pattern_resolution(self):
        """Test resolution of nationality + job pattern."""
        result = resolve_arabic_category_label("Belgian cyclists")
        assert "بلجيك" in result or "دراج" in result

    @pytest.mark.integration
    def test_batch_processing_integration(self):
        """
        Test batch processing with multiple pattern types.

        Validates:
        - Multiple categories processed together
        - Different resolver paths work in same batch
        - Results properly categorized (labels vs no_labels)
        """
        categories = [
            "2015 American television",
            "1999 establishments in Europe",
            "Belgian cyclists",
        ]

        result = batch_resolve_labels(categories)

        # Verify structure
        assert len(result.processed) == 3

        # Verify at least some translations succeeded
        assert len(result.labels) > 0 or len(result.no_labels) > 0

    @pytest.mark.integration
    def test_resolver_fallback_behavior(self):
        """
        Test that resolvers fall back correctly when patterns don't match.

        The resolver chain should:
        1. Try time resolvers
        2. Try all_new_resolvers
        3. Try country_time_pattern
        4. Try nat_males_pattern
        5. Try event2bot
        6. Try event_lab_bot
        7. Try general_resolver
        """
        # A category that should trigger fallback
        result = resolve_arabic_category_label("Unknown Category Type")

        # Even unknown categories should return a ProcessedCategory
        # (may be empty translation)
        assert isinstance(result, str)
```

### 6.3 Example 3: Fixture-Based Pattern Testing

```python
# tests/unit/patterns_resolvers/test_country_time_pattern.py

import pytest
from ArWikiCats.patterns_resolvers.country_time_pattern import (
    resolve_country_time_pattern,
)


class TestCountryTimePattern:
    """Test suite for country + time pattern resolution."""

    @pytest.fixture
    def year_patterns(self):
        """Fixture providing year-based test cases."""
        return [
            ("2015 in Yemen", "2015 في اليمن"),
            ("1999 in France", "1999 في فرنسا"),
            ("2020 in Egypt", "2020 في مصر"),
        ]

    @pytest.fixture
    def decade_patterns(self):
        """Fixture providing decade-based test cases."""
        return [
            ("1990s in Germany", "عقد 1990 في ألمانيا"),
            ("2000s in Japan", "عقد 2000 في اليابان"),
        ]

    @pytest.fixture
    def edge_cases(self):
        """Fixture providing edge cases."""
        return [
            ("in invalid", ""),  # No year
            ("2015", ""),  # No country
            ("2015 in", ""),  # Incomplete
            ("", ""),  # Empty
        ]

    @pytest.mark.unit
    @pytest.mark.parametrize("input_cat,expected", [
        ("2015 in Yemen", True),
        ("1999 in France", True),
        ("invalid pattern", False),
    ])
    def test_pattern_detection(self, input_cat, expected):
        """Test that country+time patterns are correctly detected."""
        result = resolve_country_time_pattern(input_cat)
        has_result = bool(result)
        assert has_result == expected

    @pytest.mark.unit
    def test_year_patterns(self, year_patterns):
        """Test year + country pattern translations."""
        for input_cat, expected_part in year_patterns:
            result = resolve_country_time_pattern(input_cat)
            # Check that key parts are present
            if expected_part:
                assert result, f"Expected translation for {input_cat}"

    @pytest.mark.unit
    def test_edge_cases(self, edge_cases):
        """Test edge cases return empty strings."""
        for input_cat, expected in edge_cases:
            result = resolve_country_time_pattern(input_cat)
            assert result == expected, f"Edge case failed: {input_cat}"

    @pytest.mark.unit
    def test_arabic_output_encoding(self):
        """Test that output is properly encoded Arabic text."""
        result = resolve_country_time_pattern("2015 in Yemen")
        if result:
            # Verify Arabic characters present
            assert any('\u0600' <= c <= '\u06FF' for c in result)
```

---

## 7. Configuration

### 7.1 pytest.ini (Enhanced)

```ini
[pytest]
testpaths = tests
python_files = test*.py *Test.py
python_classes = Test*
python_functions = test*

# Enhanced options
addopts =
    -v
    --tb=short
    --strict-markers
    -m "not skip2 and not dump and not dumpbig and not examples"
    --durations=10
    --maxfail=25
    --cov=ArWikiCats
    --cov-report=term-missing
    --cov-report=html:coverage_report
    --cov-fail-under=80

markers =
    all: runs all tests including slow ones
    slow: marks tests as slow (deselect with '-m "not slow"')
    fast: marks tests as fast (deselect with '-m "not fast"')
    unit: marks tests as unit tests
    integration: marks tests as integration tests
    regression: marks tests as regression tests
    dict: marks tests that work on translations dicts
    skip2: skip them default, but can be run with '-m skip2'
    dump: skip them default, but can be run with '-m dump'
    dumpbig: skip them default, but can be run with '-m dumpbig'
    examples: skip them default, but can be run with '-m examples'
    performance: marks performance/benchmark tests

filterwarnings =
    ignore::DeprecationWarning
    ignore::PendingDeprecationWarning

# Timeout settings
timeout = 300
timeout_method = thread
```

### 7.2 requirements-test.txt

```
# Testing framework
pytest>=7.0.0
pytest-cov>=4.0.0
pytest-mock>=3.10.0
pytest-xdist>=3.0.0
pytest-timeout>=2.1.0
pytest-randomly>=3.12.0

# Coverage
coverage>=7.0.0

# Code quality (optional but recommended)
black>=23.0.0
isort>=5.12.0
ruff>=0.1.0
mypy>=1.0.0

# Performance testing
pytest-benchmark>=4.0.0
```

### 7.3 Coverage Configuration (.coveragerc)

```ini
[run]
source = ArWikiCats
omit =
    */tests/*
    */__pycache__/*
    */site-packages/*
    ArWikiCats/helps/log.py

[report]
exclude_lines =
    pragma: no cover
    def __repr__
    raise AssertionError
    raise NotImplementedError
    if __name__ == .__main__.:

show_missing = True
precision = 2

[html]
directory = coverage_report
```

---

## 8. Implementation Plan

### Phase 1: Foundation (Days 1-2)

**Goals**:
- Set up testing infrastructure
- Configure pytest and coverage
- Create fixture framework

**Tasks**:
- [ ] Update pytest.ini with enhanced configuration
- [ ] Create requirements-test.txt
- [ ] Set up .coveragerc
- [ ] Create tests/fixtures/ directory
- [ ] Implement global conftest.py with common fixtures
- [ ] Create initial fixture data files (categories.json)

**Deliverables**:
- Working test infrastructure
- Fixture framework
- Base test configuration

### Phase 2: Core Module Tests (Days 3-5)

**Goals**:
- Achieve 90%+ coverage on core modules
- Test critical path functionality

**Tasks**:
- [ ] Test EventProcessor (event_processing.py)
- [ ] Test main_resolve.py (resolve_label, resolve_label_ar)
- [ ] Test CategoryResult and ProcessedCategory data classes
- [ ] Test event2bot.py
- [ ] Test event_lab_bot.py
- [ ] Test config.py

**Deliverables**:
- tests/unit/test_event_processing.py
- tests/unit/main_processers/test_main_resolve.py
- tests/unit/test_config.py
- 90%+ coverage on core modules

### Phase 3: Pattern Resolver Tests (Days 6-8)

**Goals**:
- Test all pattern matching functionality
- Cover edge cases for patterns

**Tasks**:
- [ ] Test country_time_pattern.py
- [ ] Test nat_males_pattern.py
- [ ] Test time resolvers
- [ ] Test new_resolvers/reslove_all.py
- [ ] Test nationalities, jobs, sports resolvers

**Deliverables**:
- tests/unit/patterns_resolvers/
- tests/unit/time_formats/
- tests/unit/new_resolvers/
- 85%+ coverage on pattern modules

### Phase 4: Integration Tests (Days 9-11)

**Goals**:
- Test end-to-end workflows
- Validate resolver chain integration

**Tasks**:
- [ ] Create integration test suite
- [ ] Test batch processing
- [ ] Test resolver chain fallback
- [ ] Test cache integration
- [ ] Test configuration propagation

**Deliverables**:
- tests/integration/test_end_to_end.py
- tests/integration/test_batch_processing.py
- tests/integration/test_resolver_chain.py
- Full workflow coverage

### Phase 5: Regression and Polish (Days 12-14)

**Goals**:
- Add regression tests
- Achieve coverage targets
- CI/CD integration

**Tasks**:
- [ ] Create regression test suite from known categories
- [ ] Add performance benchmarks
- [ ] Set up CI/CD pipeline
- [ ] Generate coverage report
- [ ] Document testing procedures
- [ ] Final coverage gap analysis

**Deliverables**:
- tests/regression/
- tests/performance/
- CI/CD workflow file
- Final documentation
- 80%+ overall coverage

---

## 9. Success Metrics and CI/CD Integration

### 9.1 Success Metrics

| Metric | Target | Measurement |
|--------|--------|-------------|
| Overall Coverage | 80%+ | pytest-cov |
| Core Module Coverage | 90%+ | pytest-cov |
| Test Count | 15,000+ | pytest |
| Test Speed | < 30s (unit) | pytest --durations |
| CI Pass Rate | 100% | GitHub Actions |
| Flaky Test Rate | < 1% | pytest-randomly |

### 9.2 CI/CD Integration

**GitHub Actions Workflow** (`.github/workflows/test.yml`):

```yaml
name: Tests

on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main]

jobs:
  test:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        python-version: ['3.10', '3.11', '3.12']

    steps:
      - uses: actions/checkout@v6

      - name: Set up Python ${{ matrix.python-version }}
        uses: actions/setup-python@v6
        with:
          python-version: ${{ matrix.python-version }}

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.in
          pip install pytest pytest-cov pytest-xdist

      - name: Run tests
        run: |
          pytest --cov=ArWikiCats --cov-report=xml --cov-fail-under=80

      - name: Upload coverage to Codecov
        uses: codecov/codecov-action@v3
        with:
          file: ./coverage.xml
          fail_ci_if_error: true

  lint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v6

      - name: Set up Python
        uses: actions/setup-python@v6
        with:
          python-version: '3.11'

      - name: Install linters
        run: |
          pip install black isort ruff

      - name: Run Black
        run: black --check ArWikiCats/

      - name: Run isort
        run: isort --check-only ArWikiCats/

      - name: Run Ruff
        run: ruff check ArWikiCats/
```

### 9.3 Test Execution Commands

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=ArWikiCats --cov-report=html

# Run only unit tests
pytest -m unit

# Run only integration tests
pytest -m integration

# Run tests in parallel
pytest -n auto

# Run specific test file
pytest tests/unit/test_event_processing.py

# Run with verbose output
pytest -v --tb=long

# Run excluding slow tests
pytest -m "not slow"

# Run only fast tests
pytest -m fast

# Generate coverage report
pytest --cov=ArWikiCats --cov-report=term-missing --cov-report=html

# Profile slow tests
python -m cProfile -o profile_slow.prof -m pytest -m slow
snakeviz profile_slow.prof
```

---

## Appendix: Test Data Management

### Category Test Data Format (fixtures/categories.json)

```json
{
  "year_country": [
    {
      "input": "2015 in Yemen",
      "expected": "تصنيف:2015 في اليمن",
      "pattern_type": "year_country"
    }
  ],
  "decade_country": [
    {
      "input": "1550s establishments in Namibia",
      "expected_contains": ["1550", "ناميبيا"],
      "pattern_type": "decade_establishment"
    }
  ],
  "nationality_job": [
    {
      "input": "Belgian cyclists",
      "expected_contains": ["بلجيك"],
      "pattern_type": "nationality_job"
    }
  ],
  "edge_cases": [
    {
      "input": "",
      "expected": "",
      "description": "Empty input"
    },
    {
      "input": "Invalid Pattern Here",
      "expected": "",
      "description": "No matching pattern"
    }
  ]
}
```

---

*Document Version: 1.0*
*Last Updated: 2024*
*Author: ArWikiCats Team*

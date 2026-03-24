---
name: base-worker-migration
description: Migrate resolver code to use BaseResolversWorker pattern. Use when refactoring resolvers in new_resolvers/, creating new resolvers, or converting function-based resolvers to class-based workers with load_bot/before_run/process/after_run lifecycle.
---

# BaseResolversWorker Migration Guide

This skill helps you refactor existing resolver code to use the `BaseResolversWorker` base class for standardized lifecycle management in the ArWikiCats project.

## When to use this pattern

Use `BaseResolversWorker` when:

-   Creating a new resolver in `ArWikiCats/new_resolvers/`
-   Refactoring existing function-based resolvers to class-based pattern
-   Need consistent lifecycle (load/process/cleanup) across resolvers
-   Want automatic logging and singleton instance management

## Quick Example

### Before (Old Pattern)

```python
@functools.lru_cache(maxsize=10000)
def resolve_us_states(category: str) -> str:
    result = us_bot.search(category)
    return normalize_state(result)
```

### After (New Pattern)

```python
class UsStates(BaseResolversWorker):
    def process(self, category: str) -> str:
        return self.bot.search(category)

    def after_run(self) -> None:
        self.result = normalize_state(self.result)

@functools.lru_cache(maxsize=10000)
def resolve_us_states(category: str) -> str:
    return load_class().run(category)
```

## Migration Steps

### Step 1: Create the Worker Class

```python
from ..base_worker import BaseResolversWorker

class YourResolver(BaseResolversWorker):
    """Resolver for your specific category type."""
    pass
```

### Step 2: Implement `load_bot()`

Move bot/tool initialization from module-level into `load_bot()`:

```python
def load_bot(self) -> None:
    data = load_your_data()
    self.bot: FormatData = FormatData(
        data,
        YOUR_TRANSLATIONS,
        key_placeholder="{en}",
        value_placeholder="{ar}",
    )
```

**Key points:**

-   Use `self.bot` (or `self.something`) to store the initialized tool
-   Don't return anything - just set instance attributes
-   This is called once in `__init__`

### Step 2.5: Implement `before_run()` (Optional)

Override `before_run()` if you need custom pre-processing (default lowercases the category):

```python
def before_run(self, category: str) -> str:
    category = super().before_run(category)  # lowercases
    # Add custom pre-processing if needed
    return category
```

**Key points:**

-   Called before `process()`
-   Default implementation lowercases the category
-   Override only if you need additional pre-processing

### Step 3: Implement `process()`

Extract the core logic into `process()`:

```python
def process(self, category: str) -> str:
    return self.bot.search(category)
```

**Key points:**

-   Takes `category` as parameter (after `before_run()` processing)
-   Returns the raw result (string)
-   Don't do post-processing here - use `after_run()` for that

### Step 4: Implement `after_run()` (if needed)

Move any post-processing/cleanup logic here:

```python
def after_run(self) -> None:
    self.result = normalize_state(self.result)
```

**Key points:**

-   No return value - modify `self.result` in place
-   Called after `process()` completes
-   Use for text normalization, fixing edge cases, etc.

### Step 5: Create Singleton Loader

```python
@functools.lru_cache(maxsize=1)
def load_class() -> YourResolver:
    return YourResolver('your_resolver_name')
```

### Step 6: Update Public Function

```python
@functools.lru_cache(maxsize=10000)
def resolve_your_category(category: str) -> str:
    return load_class().run(category)
```

## Complete Template

```python
"""Description of your resolver."""

from __future__ import annotations

import functools
import logging

from ...translations import YOUR_TRANSLATIONS
from ...translations_formats import FormatData
from ..base_worker import BaseResolversWorker

logger = logging.getLogger(__name__)


def load_your_data() -> dict[str, str]:
    """Load or generate your translation patterns."""
    return {...}


def normalize_your_result(ar_name: str) -> str:
    """Optional: Post-process the Arabic result."""
    return ar_name


class YourResolver(BaseResolversWorker):
    """Resolver for your specific category type."""

    def load_bot(self) -> None:
        """Initialize the translation bot."""
        data = load_your_data()
        self.bot: FormatData = FormatData(
            data,
            YOUR_TRANSLATIONS,
            key_placeholder="{en}",
            value_placeholder="{ar}",
        )

    def before_run(self, category: str) -> str:
        """Optional: Custom pre-processing before main logic."""
        category = super().before_run(category)  # lowercases
        # Add custom pre-processing if needed
        return category

    def process(self, category: str) -> str:
        """Process the category and return raw translation."""
        return self.bot.search(category)

    def after_run(self) -> None:
        """Post-process the result if needed."""
        self.result = normalize_your_result(self.result)


@functools.lru_cache(maxsize=1)
def load_class() -> YourResolver:
    """Get singleton instance of the resolver."""
    return YourResolver('your_resolver_name')


@functools.lru_cache(maxsize=10000)
def resolve_your_category(category: str) -> str:
    """Public API for resolving your categories."""
    return load_class().run(category)


__all__ = [
    "resolve_your_category",
]
```

## Lifecycle Flow

```
resolve_your_category("some category")
    → load_class() → YourResolver('your_resolver_name')
        → __init__() → load_bot()
    → .run("some category")
        → before_run("some category") → "some category" (lowercased)
        → process("some category") → raw_result
        → after_run() → modifies self.result
        → return self.result
```

## Reference: example_before.py Example

See `example_before.py` for a complete working example.

Key features:

-   `_STATE_SUFFIX_TEMPLATES_BASE` defined at module level
-   `load_us_states_new_keys()` builds dynamic patterns
-   `UsStates` class implements all lifecycle methods
-   `before_run()` lowercases categories (default behavior)
-   `normalize_state()` applied in `after_run()`
-   Double caching: singleton instance + result cache

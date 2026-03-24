# Migrating Resolvers to BaseResolversWorker

This skill explains how to refactor existing resolver code to use the `BaseResolversWorker` base class for standardized lifecycle management.

## Overview

The `BaseResolversWorker` abstract class provides a unified pattern for all resolvers in `ArWikiCats/new_resolvers/`. It standardizes the lifecycle into three phases:

1. **`load_bot()`** - Initialize translation/formatting tools
2. **`process(category)`** - Execute main logic and return result
3. **`after_run()`** - Post-process/clean up the result

## Before and After Comparison

### Before (Old Pattern - `us_states.py`)

```python
@functools.lru_cache(maxsize=10000)
def resolve_us_states(category: str) -> str:
    logger.debug(f"<<yellow>> start {category=}")

    result = us_bot.search(category)
    result = normalize_state(result)

    logger.log(20 if result else 10, f"<<yellow>> end {category=}, {result=}")
    return result
```

### After (New Pattern - `us_states_base.py`)

```python
class UsStates(BaseResolversWorker):

    def load_bot(self) -> None:
        us_states_new_keys = load_us_states_new_keys()
        self.bot = FormatData(
            us_states_new_keys,
            US_STATES,
            key_placeholder="{en}",
            value_placeholder="{ar}",
        )

    def process(self, category: str) -> str:
        return self.bot.search(category)

    def after_run(self) -> None:
        self.result = normalize_state(self.result)


@functools.lru_cache(maxsize=1)
def load_class() -> UsStates:
    return UsStates('resolve_us_states')


@functools.lru_cache(maxsize=10000)
def resolve_us_states(category: str) -> str:
    return load_class().run(category)
```

## Migration Steps

### Step 1: Create the Worker Class

Create a class that inherits from `BaseResolversWorker`:

```python
from ..base_worker import BaseResolversWorker

class YourResolver(BaseResolversWorker):
    pass
```

### Step 2: Implement `load_bot()`

Move bot/tool initialization from module-level into `load_bot()`:

```python
def load_bot(self) -> None:
    # Load your translation data
    data = load_your_data()

    # Initialize your bot/formatter
    self.bot = FormatData(
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

### Step 3: Implement `process()`

Extract the core logic into `process()`:

```python
def process(self, category: str) -> str:
    return self.bot.search(category)
```

**Key points:**

-   Takes `category` as parameter
-   Returns the raw result (string)
-   Don't do post-processing here - use `after_run()` for that

### Step 4: Implement `after_run()` (if needed)

Move any post-processing/cleanup logic here:

```python
def after_run(self) -> None:
    # self.result contains the output from process()
    self.result = normalize_your_result(self.result)
```

**Key points:**

-   No return value - modify `self.result` in place
-   Called after `process()` completes
-   Use for text normalization, fixing edge cases, etc.

### Step 5: Create Singleton Loader

Add a cached function to create a single instance:

```python
@functools.lru_cache(maxsize=1)
def load_class() -> YourResolver:
    return YourResolver('your_resolver_name')
```

**Key points:**

-   `maxsize=1` ensures only one instance exists
-   Pass a descriptive name for logging purposes

### Step 6: Update Public Function

Modify the public resolver function to use the class:

```python
@functools.lru_cache(maxsize=10000)
def resolve_your_category(category: str) -> str:
    return load_class().run(category)
```

**Key points:**

-   Keep the `@lru_cache` on the public function for result caching
-   Call `.run(category)` - this is provided by `BaseResolversWorker`

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
    # Your normalization logic
    return ar_name


class YourResolver(BaseResolversWorker):
    """Resolver for your specific category type."""

    def load_bot(self) -> None:
        """Initialize the translation bot."""
        data = load_your_data()
        self.bot = FormatData(
            data,
            YOUR_TRANSLATIONS,
            key_placeholder="{en}",
            value_placeholder="{ar}",
        )

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
    └── load_class() → YourResolver('your_resolver_name')
        └── __init__() → load_bot()
    └── .run("some category")
        ├── before_run("some category") → "some category" (lowercased)
        ├── process("some category") → raw_result
        ├── after_run() → modifies self.result
        └── return self.result
```

## Benefits

1. **Consistent structure** across all resolvers
2. **Automatic logging** - handled by base class
3. **Clear separation** of concerns (load/process/cleanup)
4. **Easier testing** - each phase is isolated
5. **Singleton pattern** - bot is initialized once per resolver type

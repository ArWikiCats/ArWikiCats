---
name: base-worker-migration
description: Migrate resolver code to use BaseResolversWorker pattern. Use when refactoring resolvers in new_resolvers/, creating new resolvers, or converting function-based resolvers to class-based workers with load_bot/before_run/process/after_run lifecycle.
---

# BaseResolversWorker Migration Guide

Refactor existing resolver code to use the `BaseResolversWorker` base class for standardized lifecycle management in the ArWikiCats project.

## When to use this pattern

-   Creating a new resolver in `ArWikiCats/new_resolvers/`
-   Refactoring existing function-based resolvers to class-based pattern
-   Need consistent lifecycle (load/process/cleanup) across resolvers
-   Want automatic logging and singleton instance management

---

## Quick Before/After

**Before (old pattern)** — module-level state, inline logic, no separation:

```python
us_bot = FormatData(us_states_new_keys, US_STATES, ...)  # module-level init

@functools.lru_cache(maxsize=10000)
def resolve_us_states(category: str) -> str:
    result = us_bot.search(category)
    return normalize_state(result)
```

**After (new pattern)** — encapsulated in class, lifecycle methods, double caching:

```python
class UsStates(BaseResolversWorker):
    def load_bot(self) -> None:
        self.bot = FormatData(load_us_states_new_keys(), US_STATES, ...)

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

---

## Lifecycle Flow

```
resolve_us_states("Texas democrats")
    → load_class()                          # returns cached UsStates singleton
        → UsStates('resolve_us_states')
            → __init__() → load_bot()       # runs ONCE at first call
    → .run("Texas democrats")
        → before_run(category)              # lowercases → "texas democrats"
        → process("texas democrats")        # → raw Arabic string
        → after_run()                       # modifies self.result in place
        → return self.result
```

Two caches work together:

-   `load_class()` (`maxsize=1`) — the class instance is created **once**, so `load_bot()` runs only once
-   `resolve_us_states()` (`maxsize=10000`) — individual results are cached per category string

---

## Migration Steps

### Step 1: Move module-level data to a top-level function

If your old code had dictionaries or bot initialization at module level, extract them into a standalone function. This keeps module import fast and makes the data testable in isolation.

```python
# OLD — runs at import time, hard to test
_TEMPLATES = { ... }
us_bot = FormatData(_TEMPLATES, US_STATES, ...)

# NEW — lazy, testable
_TEMPLATES = { ... }   # constants stay at module level

def load_your_data() -> dict[str, str]:
    """Build and return translation pattern dict."""
    keys = dict(_TEMPLATES)
    # any dynamic additions ...
    return keys
```

> **Key point:** Pure constants (like `_STATE_SUFFIX_TEMPLATES_BASE`) stay at module level. Only _initialization logic_ (building derived dicts, constructing `FormatData`) moves into `load_bot()`.

---

### Step 2: Create the Worker Class

```python
from ..base_worker import BaseResolversWorker

class YourResolver(BaseResolversWorker):
    """Resolver for your specific category type."""
    pass
```

---

### Step 3: Implement `load_bot()`

Move bot construction from module level into `load_bot()`. This is called **once** inside `__init__`.

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

-   Store result on `self` (e.g. `self.bot`)
-   No return value
-   Do **not** call this yourself — the base class calls it in `__init__`

---

### Step 4: Implement `process()`

The core lookup logic. Receives the already-preprocessed category string.

```python
def process(self, category: str) -> str:
    return self.bot.search(category)
```

-   Input is the output of `before_run()` (lowercased by default)
-   Return the raw result string
-   Do **not** post-process here — that belongs in `after_run()`

---

### Step 5: Implement `after_run()` (if needed)

Post-process `self.result` in place. Called automatically after `process()`.

```python
def after_run(self) -> None:
    self.result = normalize_state(self.result)
```

-   Modify `self.result` directly — no return value
-   Use for string normalization, deduplication, edge-case fixes
-   Skip this method entirely if no post-processing is needed

---

### Step 6: Override `before_run()` (only if needed)

The default lowercases the category. Override only when you need additional preprocessing.

```python
def before_run(self, category: str) -> str:
    category = super().before_run(category)  # always call super() first
    category = category.strip()              # example: add stripping
    return category
```

> ⚠️ Always call `super().before_run(category)` first, or you lose the default lowercasing.

---

### Step 7: Add singleton loader + public function

```python
@functools.lru_cache(maxsize=1)
def load_class() -> YourResolver:
    return YourResolver('your_resolver_name')   # name used in log messages


@functools.lru_cache(maxsize=10000)
def resolve_your_category(category: str) -> str:
    return load_class().run(category)
```

The string passed to `YourResolver(...)` is used in log output to identify which resolver is running. Use the same name as the public function (e.g. `'resolve_us_states'`).

---

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


# Module-level constants only — no initialization logic here
_TEMPLATES_BASE: dict[str, str] = {
    "{en} some pattern": "arabic {ar}",
    # ...
}


def load_your_data() -> dict[str, str]:
    """Build and return the full translation pattern dict."""
    keys = dict(_TEMPLATES_BASE)
    # add any dynamically generated entries
    return keys


def normalize_your_result(ar_name: str) -> str:
    """Post-process the Arabic result string."""
    # fix double-prefix bugs, replace known bad strings, etc.
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

    # Override before_run() only if you need preprocessing beyond lowercasing
    # def before_run(self, category: str) -> str:
    #     category = super().before_run(category)
        # Add custom pre-processing if needed
    #     return category

    def process(self, category: str) -> str:
        """Process the category and return raw translation."""
        return self.bot.search(category)

    def after_run(self) -> None:
        """Post-process the result if needed."""
        self.result = normalize_your_result(self.result)


@functools.lru_cache(maxsize=1)
def load_class() -> YourResolver:
    """Get singleton instance of the resolver."""
    return YourResolver('resolve_your_category')


@functools.lru_cache(maxsize=10000)
def resolve_your_category(category: str) -> str:
    return load_class().run(category)


__all__ = [
    "resolve_your_category",
]
```

---

## Lifecycle (what happens when `resolve_your_category("some input")` is called)

```
resolve_your_category("Texas Democrats")
  → load_class()                     # returns cached YourResolver singleton
      first call only:
        YourResolver('resolve_your_category')
          → __init__() → load_bot()  # FormatData built here, stored as self.bot
  → .run("Texas Democrats")
      → before_run("Texas Democrats")   → "texas democrats"   (lowercased)
      → process("texas democrats")      → raw Arabic string
      → after_run()                     → self.result modified in place
      → return self.result
```

---

## Rules — follow these exactly

**load_bot()**

-   Move all `FormatData(...)` construction here — never at module level
-   Set `self.bot` (or another `self.*` attribute); do not return anything
-   Do not call `load_bot()` yourself — the base `__init__` calls it once

**process()**

-   Return the result of `self.bot.search(category)`
-   Do not normalize or post-process — that belongs in `after_run()`

**after_run()**

-   Assign to `self.result` in place; return nothing
-   Omit entirely if there is no post-processing

**before_run()**

-   Omit entirely unless you need preprocessing beyond lowercasing
-   If overriding: `category = super().before_run(category)` must be the first line

**load_class()**

-   Always `maxsize=1` — only one instance is ever needed
-   The name string passed to the constructor must match the public function name

**Module level**

-   Only plain dicts and `.update()` calls that reference those dicts
-   No `FormatData(...)`, no function calls that do real work

---

## What changes when migrating from the old pattern

| Old code location                                     | New location                                                                                                   |
| ----------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `us_bot = FormatData(...)` at module level            | Inside `load_bot()` as `self.bot = FormatData(...)`                                                            |
| `result = us_bot.search(category)` in public function | Inside `process()` as `return self.bot.search(category)`                                                       |
| `result = normalize_state(result)` in public function | Inside `after_run()` as `self.result = normalize_state(self.result)`                                           |
| `@functools.lru_cache` on public function only        | `@functools.lru_cache(maxsize=1)` on `load_class()` + `@functools.lru_cache(maxsize=10000)` on public function |

---

## Common Mistakes

| Mistake                                       | Fix                                                  |
| --------------------------------------------- | ---------------------------------------------------- |
| Calling `load_bot()` manually                 | Don't — the base `__init__` calls it automatically   |
| Returning a value from `after_run()`          | Modify `self.result` in place; return nothing        |
| Forgetting `super().before_run()` in override | Always call `super()` first to preserve lowercasing  |
| Putting `FormatData(...)` at module level     | Move it into `load_bot()` so it runs lazily          |
| Using `maxsize=None` on `load_class()`        | Use `maxsize=1` — only one instance is ever needed   |
| Post-processing inside `process()`            | Move any fixup to `after_run()` for clean separation |

---

## Reference Files

See `example_before.py` and `example_after.py` for the complete `UsStates` migration.

Notable patterns in that example:

-   `_STATE_SUFFIX_TEMPLATES_BASE` stays at module level (pure constant dict)
-   `_STATE_SUFFIX_TEMPLATES_BASE.update(...)` also stays at module level (still just building a constant)
-   `load_us_states_new_keys()` adds the dynamic party-name entries and is called from `load_bot()`
-   `normalize_state()` fixes double-prefix bugs (`ولاية ولاية`) in `after_run()`

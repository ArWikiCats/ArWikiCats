"""
Legacy Resolvers - Circular Dependency Module

=== Historical Import Chain Analysis ===

This module was originally named 'circular_dependency' due to a circular import issue:

country_bot.py imports:
    from . import general_resolver

general_resolver.py imports:
    from .ar_lab_bot import find_ar_label

ar_lab_bot.py imports:
    from . import country_bot  # ← THIS WAS THE CIRCULAR IMPORT

=== Circular Dependency Resolution ===

**Status**: ✓ RESOLVED (2026-01-26)

The circular dependency has been broken using lazy imports in ar_lab_bot.py:
- Removed module-level: `from . import country_bot`
- Added function-level imports in:
  1. CountryResolver.resolve_labels() method
  2. wrap_event2() function

This allows modules to be imported in any order without circular dependency errors.

**Future Work** (see ArWikiCats/legacy_bots/refactor.md for details):
- Consider renaming this directory from 'circular_dependency' to 'resolvers'
- Extract shared interfaces (abstract base classes for resolvers)
- Implement dependency injection patterns for better testability
- Move find_ar_label() to a separate module for cleaner separation

These enhancements are described in detail in refactor.md Phase 1, which also
outlines 6 additional refactoring phases for the legacy_bots module.

"""

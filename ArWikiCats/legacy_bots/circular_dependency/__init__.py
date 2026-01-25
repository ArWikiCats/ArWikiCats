"""
Circular Dependency Resolution Module

=== Original Import Chain (Now Resolved) ===

country_bot.py imports:
    from . import general_resolver

general_resolver.py imports:
    from .ar_lab_bot import find_ar_label

ar_lab_bot.py imports:
    from . import country_bot  # CIRCULAR!

=== Original Circular Dependency ===
country_bot -> general_resolver -> ar_lab_bot -> country_bot

=== Resolution Strategy (Implemented) ===

The circular dependency has been broken using lazy imports via the
`interfaces.py` module. Instead of importing `country_bot` directly
at module load time, `ar_lab_bot.py` now uses:

1. `get_country_term_label_resolver()` - Returns the `fetch_country_term_label`
   function via lazy import when first called.

2. `get_event2_d2_resolver()` - Returns the `event2_d2` function via
   lazy import when first called.

This approach:
- Breaks the import cycle at module load time
- Preserves all existing functionality
- Is thread-safe (Python handles global assignment atomically)
- Maintains LRU caching on the original functions

=== Module Structure ===

- interfaces.py: Protocol classes and lazy resolver accessors
- country_bot.py: Country label resolution and event handling
- general_resolver.py: Separator-based category resolution
- ar_lab_bot.py: Arabic label building pipeline
- sub_general_resolver.py: Sub-category resolution
"""

"""Arabic label normalization and fixing pipeline.

This module provides the post-processing pipeline that cleans and normalizes
Arabic category labels after they are resolved. The pipeline includes:

- fixlabel: Main entry point that applies all normalization rules
- cleanse_category_label: Final cleansing step for formatting issues
- add_fee: Ensures proper preposition usage with year references
- move_years: Reorders year references in labels

The fix pipeline is applied after resolution to ensure labels are grammatically
correct and follow Arabic Wikipedia naming conventions.
"""

from __future__ import annotations

from .fixtitle import add_fee, cleanse_category_label, fix_it, fixlabel
from .mv_years import move_by_in, move_years, move_years_first

__all__ = [
    "cleanse_category_label",
    "add_fee",
    "fix_it",
    "fixlabel",
    "move_by_in",
    "move_years",
    "move_years_first",
]

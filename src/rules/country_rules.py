from __future__ import annotations

import re
from typing import Optional

from .engine import Rule
from src.make2_bots.ma_bots.country_bot import get_country


class CountryRule(Rule):
    """A rule that handles country categories."""

    def apply(self, category: str) -> Optional[str]:
        """
        Apply the rule to the category.

        Args:
            category: The category to process.

        Returns:
            The transformed label, or None if the rule doesn't match.
        """
        cat_lower = category.lower()
        if re.sub(r"^\d", "", cat_lower) == cat_lower:
            label = get_country(cat_lower)
            return label if label else None
        return None

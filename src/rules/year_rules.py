from __future__ import annotations

from typing import Optional

from .engine import Rule
from src.make2_bots.date_bots import with_years_bot
from src.make2_bots.ma_bots.year_or_typeo.bot_lab import (
    label_for_startwith_year_or_typeo,
)


class YearsRule(Rule):
    """A rule that handles categories starting with years."""

    def apply(self, category: str) -> Optional[str]:
        """
        Apply the rule to the category.

        Args:
            category: The category to process.

        Returns:
            The transformed label, or None if the rule doesn't match.
        """
        cat_lower = category.lower()
        if cat_lower.isdigit():
            return with_years_bot.Try_With_Years(cat_lower)
        return None


class StartWithYearOrTypoRule(Rule):
    """A rule that handles categories starting with a year or typo."""

    def apply(self, category: str) -> Optional[str]:
        """
        Apply the rule to the category.

        Args:
            category: The category to process.

        Returns:
            The transformed label, or None if the rule doesn't match.
        """
        return label_for_startwith_year_or_typeo(category) or None

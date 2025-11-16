from __future__ import annotations

from typing import Optional

from .engine import Rule
from src.make2_bots.o_bots import univer


class UniversityRule(Rule):
    """A rule that handles university categories."""

    def apply(self, category: str) -> Optional[str]:
        """
        Apply the rule to the category.

        Args:
            category: The category to process.

        Returns:
            The transformed label, or None if the rule doesn't match.
        """
        return univer.te_universities(category) or None

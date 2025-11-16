from __future__ import annotations

from typing import Optional

from .engine import Rule
from src.make2_bots.ma_bots.lab_seoo_bot import event_Lab_seoo
from src.make2_bots.bots import tmp_bot
from src import app_settings


class BlockedWordsRule(Rule):
    """A rule that blocks categories containing common English prepositions."""

    BLOCKED_WORDS = {"in", "of", "from", "by", "at"}

    def apply(self, category: str) -> Optional[str]:
        """
        Apply the rule to the category.

        Args:
            category: The category to process.

        Returns:
            An empty string if a blocked word is found, otherwise None.
        """
        category_lower = category.lower()
        if any(f" {word} " in category_lower.split(" ") for word in self.BLOCKED_WORDS):
            return ""
        return None


class StubsRule(Rule):
    """A rule that handles "stubs" categories."""

    def apply(self, category: str) -> Optional[str]:
        """
        Apply the rule to the category.

        Args:
            category: The category to process.

        Returns:
            The transformed label, or None if the rule doesn't match.
        """
        category_lower = category.lower()

        if category_lower.endswith(" stubs") and app_settings.find_stubs:
            list_of_cat = "بذرة {}"
            category = category_lower.replace(" stubs", "", 1)

            sub_ar_label = event_Lab_seoo("", category)

            if not sub_ar_label:
                sub_ar_label = tmp_bot.Work_Templates(category)

            if sub_ar_label:
                return list_of_cat.format(sub_ar_label)
            else:
                return "بذرة"
        return None

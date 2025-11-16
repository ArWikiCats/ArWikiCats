from __future__ import annotations

import re
from typing import Callable, Optional

from .engine import Rule


class RegexRule(Rule):
    """A rule that applies a regex and a transformation function."""

    def __init__(
        self,
        pattern: str,
        transform: Callable[[re.Match], str],
        flags: int = 0,
    ):
        self.regex = re.compile(pattern, flags)
        self.transform = transform

    def apply(self, category: str) -> Optional[str]:
        """
        Apply the rule to the category.

        Args:
            category: The category to process.

        Returns:
            The transformed label, or None if the rule doesn't match.
        """
        if match := self.regex.search(category):
            return self.transform(match)
        return None

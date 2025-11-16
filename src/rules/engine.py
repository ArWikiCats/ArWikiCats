from __future__ import annotations

from typing import Callable, List, Optional, Protocol

class Rule(Protocol):
    """A rule that can be applied to a category string."""

    def apply(self, category: str) -> Optional[str]:
        """
        Apply the rule to the category.

        Args:
            category: The category to process.

        Returns:
            The transformed label, or None if the rule doesn't match.
        """
        ...

class RuleEngine:
    """A simple rule engine that applies a list of rules to a category."""

    def __init__(self, rules: Optional[List[Rule]] = None):
        self.rules = rules or []

    def add_rule(self, rule: Rule) -> None:
        """Add a rule to the engine."""
        self.rules.append(rule)

    def apply(self, category: str) -> Optional[str]:
        """
        Apply the rules to the category and return the first matching label.

        Args:
            category: The category to process.

        Returns:
            The transformed label, or None if no rules match.
        """
        for rule in self.rules:
            if label := rule.apply(category):
                return label
        return None

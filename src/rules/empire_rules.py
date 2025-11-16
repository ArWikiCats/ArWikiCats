from __future__ import annotations

from .base_rules import RegexRule


class CenturyDutchEmpireRule(RegexRule):
    """A rule that handles "Dutch Empire" categories that start with a century."""

    def __init__(self):
        super().__init__(
            r"^(\d+..)-century people of the Dutch Empire",
            lambda m: f"أشخاص من الإمبراطورية الهولندية القرن {m.group(1)}",
        )

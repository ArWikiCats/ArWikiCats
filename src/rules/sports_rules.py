from __future__ import annotations

from .base_rules import RegexRule


class YearSportsEventsRule(RegexRule):
    """A rule that handles "sports events" categories that start with a year."""

    def __init__(self):
        super().__init__(
            r"^(\d{4})\s+sports\s+events\s+in\s+(.*)",
            lambda m: f"أحداث {m.group(1)} الرياضية في {m.group(2)}",
        )


class MultiSportEventsRule(RegexRule):
    """A rule that handles "multi-sport events" categories."""

    def __init__(self):
        super().__init__(
            r"^(.*) at multi-sport events$",
            lambda m: f"أحداث {m.group(1)} في رياضية متعددة",
        )

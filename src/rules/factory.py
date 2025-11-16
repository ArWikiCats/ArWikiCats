from __future__ import annotations

from .engine import RuleEngine
from .university_rules import UniversityRule
from .general_rules import BlockedWordsRule, StubsRule
from .country_rules import CountryRule
from .year_rules import YearsRule, StartWithYearOrTypoRule


def create_event2_rule_engine() -> RuleEngine:
    """Create a rule engine with the rules from event2bot."""
    rules = [
        UniversityRule(),
        BlockedWordsRule(),
        CountryRule(),
        YearsRule(),
        StartWithYearOrTypoRule(),
        StubsRule(),
    ]
    return RuleEngine(rules)

from __future__ import annotations

from .engine import RuleEngine
from .university_rules import UniversityRule
from .general_rules import BlockedWordsRule, StubsRule
from .country_rules import CountryRule
from .year_rules import YearsRule, StartWithYearOrTypoRule
from .sports_rules import YearSportsEventsRule, MultiSportEventsRule
from .empire_rules import CenturyDutchEmpireRule


def create_event2_rule_engine() -> RuleEngine:
    """Create a rule engine with the rules from event2bot."""
    rules = [
        UniversityRule(),
        BlockedWordsRule(),
        CountryRule(),
        YearsRule(),
        StartWithYearOrTypoRule(),
        StubsRule(),
        YearSportsEventsRule(),
        MultiSportEventsRule(),
        CenturyDutchEmpireRule(),
    ]
    return RuleEngine(rules)

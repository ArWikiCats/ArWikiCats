import pytest
from src.rules import RuleEngine
from src.rules.base_rules import RegexRule

from src.rules.general_rules import BlockedWordsRule, StubsRule


def test_rule_engine():
    """Test that the rule engine applies the first matching rule."""
    rules = [
        RegexRule(r"foo", lambda m: "bar"),
        RegexRule(r"baz", lambda m: "qux"),
    ]
    engine = RuleEngine(rules)

    assert engine.apply("foo") == "bar"
    assert engine.apply("baz") == "qux"
    assert engine.apply("spam") is None


def test_blocked_words_rule():
    """Test that the blocked words rule blocks categories with certain words."""
    rule = BlockedWordsRule()
    assert rule.apply("foo in bar") == ""
    assert rule.apply("foo of bar") == ""
    assert rule.apply("foo from bar") == ""
    assert rule.apply("foo by bar") == ""
    assert rule.apply("foo at bar") == ""
    assert rule.apply("foo bar") is None


from src.rules.country_rules import CountryRule
from src.rules.year_rules import YearsRule, StartWithYearOrTypoRule
from src.rules.university_rules import UniversityRule




def test_country_rule():
    """Test that the country rule correctly identifies and transforms country names."""
    rule = CountryRule()
    assert rule.apply("Egypt") is not None
    assert rule.apply("foo") is None


def test_years_rule():
    """Test that the years rule correctly identifies and transforms years."""
    rule = YearsRule()
    assert rule.apply("2022") is not None
    assert rule.apply("foo") is None

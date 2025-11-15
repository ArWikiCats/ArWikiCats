
from __future__ import annotations

import pytest

# Adjust this import to your real module path
import src.make2_bots.o_bots.ethnic_bot as ethnic_mod  # e.g. src.ethnic or src.fix.ethnic_helpers

ethnic = ethnic_mod.ethnic
ethnic_culture = ethnic_mod.ethnic_culture

# ---------- Structural tests for data dictionaries ----------


@pytest.fixture(autouse=True)
def clear_lru_caches():
    """Clear caches before each test."""
    ethnic_mod.ethnic.cache_clear()
    ethnic_mod.ethnic_culture.cache_clear()


@pytest.mark.fast
def test_en_is_nat_ar_is_women_templates_have_single_placeholder():
    """Each female-topic template must contain exactly one {} placeholder."""
    for template in ethnic_mod.en_is_nat_ar_is_women_2.values():
        assert "{}" in template
        assert template.count("{}") == 1


@pytest.mark.fast
def test_male_topic_table_templates_have_single_placeholder():
    """Each male-topic template must contain exactly one {} placeholder."""
    for template in ethnic_mod.MALE_TOPIC_TABLE.values():
        assert "{}" in template
        assert template.count("{}") == 1


# ---------- Tests for ethnic_culture() female-path using all topics ----------


@pytest.mark.fast
def test_ethnic_culture_female_topics_cover_all_entries():
    """
    For every female-topic mapping, ethnic_culture should build a formatted label
    when given a known female nationality.
    """
    for topic, template in ethnic_mod.en_is_nat_ar_is_women_2.items():
        start = "zanzibari-american"
        base_label = ethnic_mod.Nat_women[start]
        suffix = f"{start} {topic}"

        result = ethnic_culture("Category:Test", start, suffix)

        expected_inner = f"{base_label} {base_label}"
        expected = template.format(expected_inner)

        assert result == expected


# ---------- Tests for ethnic_culture() male-path using all topics ----------


@pytest.mark.fast
def test_ethnic_culture_male_topics_cover_all_entries():
    """
    For every male-topic mapping, ethnic_culture should build a formatted label
    when given a known male nationality.
    """
    for topic, template in ethnic_mod.MALE_TOPIC_TABLE.items():
        start = "afghan"
        base_label = ethnic_mod.Nat_men[start]
        suffix = f"{start} {topic}"

        result = ethnic_culture("Category:Test", start, suffix)

        expected_inner = f"{base_label} {base_label}"
        expected = template.format(expected_inner)

        assert result == expected


# ---------- Edge cases for ethnic_culture() ----------


def test_ethnic_culture_unknown_nationality_returns_empty():
    """When nationality is not found in Nat_men or Nat_women, result must be empty."""
    result = ethnic_culture("Category:Unknown", "unknown-nat", "unknown-nat history")
    assert result == ""


# ---------- Core tests for ethnic() direct -mens composition path ----------


def test_ethnic_direct_mens_composition_basic():
    """
    When suffix matches `<nat> people` and both start and suffix exist in Nat_mens,
    ethnic() should combine plural nationalities.
    """
    category = "Category:People"
    start = "yemeni"
    suffix = "zanzibari people"

    result = ethnic(category, start, suffix)

    expected = f"{ethnic_mod.Nat_mens['zanzibari']} {ethnic_mod.Nat_mens['yemeni']}"
    assert result == expected


def test_ethnic_direct_mens_composition_trims_people_suffix():
    """Suffix should be trimmed from ' people' before lookup in Nat_mens."""
    category = "Category:PeopleTrim"
    start = "afghan"
    suffix = "afghan people"

    result = ethnic(category, start, suffix)

    expected = f"{ethnic_mod.Nat_mens['afghan']} {ethnic_mod.Nat_mens['afghan']}"
    assert result == expected


def test_ethnic_direct_mens_composition_requires_both_nationalities():
    """
    If suffix nationality exists in Nat_mens but start nationality does not,
    the direct composition path should not fire and result should fall back.
    """
    category = "Category:PeopleMissing"
    start = "unknown-yemeni"
    suffix = "yemeni people"

    result = ethnic(category, start, suffix)

    assert result == ""


# ---------- Tests for ethnic() fallback to ethnic_culture() ----------

def test_ethnic_falls_back_to_ethnic_culture():
    """
    When direct mens-composition path does not produce a label, ethnic()
    must call ethnic_culture() and return its result.
    """
    category = "Category:History"
    start = "afghan"
    suffix = "afghan history"

    direct = ethnic(category, start, suffix)
    fallback = ethnic_culture(category, start, suffix)

    assert direct == fallback
    assert direct != ""


def test_ethnic_unknown_everything_returns_empty():
    """If neither mens-composition nor ethnic_culture can resolve, result must be empty."""
    category = "Category:Unknown"
    start = "unknown-nat"
    suffix = "unknown-nat people"

    result = ethnic(category, start, suffix)

    assert result == ""


# ---------- Integration-style sanity checks ----------


def test_ethnic_culture_female_example_music():
    """Concrete female example using zanzibari-american music."""
    start = "zanzibari-american"
    suffix = "zanzibari-american music"
    result = ethnic_culture("Category:Music", start, suffix)

    base = ethnic_mod.Nat_women[start]
    expected_inner = f"{base} {base}"
    expected = ethnic_mod.en_is_nat_ar_is_women_2["music"].format(expected_inner)

    assert result == expected


def test_ethnic_culture_male_example_history():
    """Concrete male example using afghan history."""
    start = "afghan"
    suffix = "afghan history"
    result = ethnic_culture("Category:History", start, suffix)

    base = ethnic_mod.Nat_men[start]
    expected_inner = f"{base} {base}"
    expected = ethnic_mod.MALE_TOPIC_TABLE["history"].format(expected_inner)

    assert result == expected


def test_ethnic_prefers_direct_mens_over_culture_when_possible():
    """
    If both direct mens-composition and culture mapping are theoretically possible,
    ethnic() should use the direct mens-composition path.
    """
    category = "Category:People"
    start = "yemeni"
    suffix = "zanzibari people"

    result = ethnic(category, start, suffix)

    expected_direct = f"{ethnic_mod.Nat_mens['zanzibari']} {ethnic_mod.Nat_mens['yemeni']}"
    assert result == expected_direct

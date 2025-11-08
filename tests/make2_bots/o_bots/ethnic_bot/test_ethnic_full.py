
from __future__ import annotations

import pytest

# Adjust this import to your real module path
import src.make2_bots.o_bots.ethnic_bot as ethnic_mod  # e.g. src.ethnic or src.fix.ethnic_helpers

ethnic = ethnic_mod.ethnic
ethnic_culture = ethnic_mod.ethnic_culture


@pytest.fixture(autouse=True)
def clear_caches():
    """Ensure caches are clean before and after each test."""
    ethnic_mod.ETHNIC_CACHE.clear()
    ethnic_mod.ETHNIC_CULTURE_CACHE.clear()
    yield
    ethnic_mod.ETHNIC_CACHE.clear()
    ethnic_mod.ETHNIC_CULTURE_CACHE.clear()


# ---------- Structural tests for data dictionaries ----------


@pytest.mark.slow
@pytest.mark.parametrize("topic,template", ethnic_mod.en_is_nat_ar_is_women_2.items())
def test_en_is_nat_ar_is_women_templates_have_single_placeholder(topic, template):
    """Each female-topic template must contain exactly one {} placeholder."""
    assert "{}" in template
    assert template.count("{}") == 1


@pytest.mark.slow
@pytest.mark.parametrize("topic,template", ethnic_mod.MALE_TOPIC_TABLE.items())
def test_male_topic_table_templates_have_single_placeholder(topic, template):
    """Each male-topic template must contain exactly one {} placeholder."""
    assert "{}" in template
    assert template.count("{}") == 1


# ---------- Tests for ethnic_culture() female-path using all topics ----------


@pytest.mark.slow
@pytest.mark.parametrize(
    "topic,template", sorted(ethnic_mod.en_is_nat_ar_is_women_2.items())
)
def test_ethnic_culture_female_topics_cover_all_entries(topic, template):
    """
    For every female-topic mapping, ethnic_culture should build a formatted label
    when given a known female nationality.
    """
    start = "zanzibari-american"
    base_label = ethnic_mod.Nat_women[start]
    suffix = f"{start} {topic}"

    result = ethnic_culture("Category:Test", start, suffix)

    expected_inner = f"{base_label} {base_label}"
    expected = template.format(expected_inner)

    assert result == expected


# ---------- Tests for ethnic_culture() male-path using all topics ----------


@pytest.mark.slow
@pytest.mark.parametrize(
    "topic,template", sorted(ethnic_mod.MALE_TOPIC_TABLE.items())
)
def test_ethnic_culture_male_topics_cover_all_entries(topic, template):
    """
    For every male-topic mapping, ethnic_culture should build a formatted label
    when given a known male nationality.
    """
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


def test_ethnic_culture_uses_cache():
    """ethnic_culture must reuse cached result for identical inputs."""
    category = "Category:CacheTest"
    start = "afghan"
    suffix = "afghan history"

    first = ethnic_culture(category, start, suffix)
    assert first != ""

    cache_size_before = len(ethnic_mod.ETHNIC_CULTURE_CACHE)

    # Mutate underlying data to detect correct cache usage
    original = ethnic_mod.Nat_men["afghan"]
    ethnic_mod.Nat_men["afghan"] = "MODIFIED"
    try:
        second = ethnic_culture(category, start, suffix)
        assert second == first
        assert len(ethnic_mod.ETHNIC_CULTURE_CACHE) == cache_size_before
    finally:
        ethnic_mod.Nat_men["afghan"] = original


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


# ---------- Cache behavior for ethnic() ----------


def test_ethnic_cache_is_used_for_repeated_calls():
    """ethnic() must reuse cached result when called with same parameters."""
    category = "Category:CacheTestEthnic"
    start = "yemeni"
    suffix = "zanzibari people"

    first = ethnic(category, start, suffix)
    assert first != ""

    cache_size_before = len(ethnic_mod.ETHNIC_CACHE)

    original = ethnic_mod.Nat_mens["zanzibari"]
    ethnic_mod.Nat_mens["zanzibari"] = "MODIFIED"
    try:
        second = ethnic(category, start, suffix)
        assert second == first
        assert len(ethnic_mod.ETHNIC_CACHE) == cache_size_before
    finally:
        ethnic_mod.Nat_mens["zanzibari"] = original


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

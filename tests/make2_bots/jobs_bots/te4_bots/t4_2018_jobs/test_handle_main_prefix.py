"""
Tests
"""

import pytest

from src.make2_bots.jobs_bots.te4_bots.t4_2018_jobs import _handle_main_prefix

# Dummy maps for testing (customized for test isolation)
Main_priffix = {
    "cultural depictions of": "تصوير ثقافي عن {}",
    "fictional depictions of": "تصوير خيالي عن {}",
    "depictions of": "تصوير عن {}",
    "non": "{} غير",
    "fictional": "{} خياليون",
    "native": "{} أصليون",
}

# Sorted as the real code does
Main_priffix = dict(
    sorted(Main_priffix.items(), key=lambda x: x[0].count(" "), reverse=True)
)

change_male_to_female = {
    "{} خياليون": "{} خياليات",
    "{} أصليون": "{} أصليات",
}


@pytest.mark.parametrize("category, expected_key", data.items(), ids=list(data.keys()))
@pytest.mark.slow
def test_te4_2018_Jobs_data(category, expected_key) -> None:
    label = _handle_main_prefix(category)
    assert label.strip() == expected_key


def test_simple_prefix_match():
    """Prefix should be detected and removed correctly."""
    category = "fictional cats"
    category_original = category

    new_cat, prefix, label = _handle_main_prefix(category, category_original)

    assert prefix == "fictional"
    assert new_cat == "cats"
    assert label == "{} خياليون"


def test_no_prefix_match():
    """Should return unchanged category if no prefix matches."""
    category = "random category"
    category_original = category

    new_cat, prefix, label = _handle_main_prefix(category, category_original)

    assert new_cat == category
    assert prefix == ""
    assert label == ""


def test_multi_word_prefix_priority():
    """
    Ensure the function respects the sorting order.
    'fictional depictions of' must match BEFORE 'fictional'.
    """
    category = "fictional depictions of birds"
    category_original = category

    new_cat, prefix, label = _handle_main_prefix(category, category_original)

    assert prefix == "fictional depictions of"
    assert new_cat == "birds"
    assert label == "تصوير خيالي عن {}"


def test_prefix_with_women_singular():
    """If suffix ends with 'women', use female version if available."""
    category = "fictional women"
    category_original = category

    new_cat, prefix, label = _handle_main_prefix(category, category_original)

    assert prefix == "fictional"
    assert new_cat == "women"
    assert label == "{} خياليات"  # female version


def test_prefix_with_women_apostrophe_s():
    """If suffix ends with women's, use female version."""
    category = "native women's"
    category_original = category

    new_cat, prefix, label = _handle_main_prefix(category, category_original)

    assert prefix == "native"
    assert new_cat == "women's"
    assert label == "{} أصليات"


def test_case_insensitive_prefix():
    """Prefix match must be case-insensitive."""
    category = "FiCtIoNaL cats"
    category_original = category

    new_cat, prefix, label = _handle_main_prefix(category, category_original)

    assert prefix.lower() == "fictional"
    assert new_cat == "cats"


def test_break_after_first_match():
    """If two prefixes could match the original string, only first (sorted) should apply."""
    category = "fictional depictions of cats"
    category_original = category

    new_cat, prefix, label = _handle_main_prefix(category, category_original)

    assert prefix == "fictional depictions of"  # not "fictional"
    assert new_cat == "cats"


def test_non_prefix():
    """Test key 'non' mapping."""
    category = "non mammals"
    category_original = category

    new_cat, prefix, label = _handle_main_prefix(category, category_original)

    assert prefix == "non"
    assert new_cat == "mammals"
    assert label == "{} غير"

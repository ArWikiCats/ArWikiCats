"""
Tests
"""

import pytest

from ArWikiCats.make_bots.countries_formats.t4_2018_jobs import handle_main_prefix

data = {
    "fictional basic": {
        "category_original": "fictional cats",
        "expected_category": "cats",
        "expected_main_ss": "fictional",
        "expected_main_lab": "{} خياليون",
    },
    "native women": {
        "category_original": "native women",
        "expected_category": "women",
        "expected_main_ss": "native",
        "expected_main_lab": "{} أصليات",  # بعد التحويل للمؤنث
    },
    "no prefix": {
        "category_original": "random text",
        "expected_category": "random text",
        "expected_main_ss": "",
        "expected_main_lab": "",
    },
    "depictions prefix": {
        "category_original": "depictions of lions",
        "expected_category": "lions",
        "expected_main_ss": "depictions of",
        "expected_main_lab": "تصوير عن {}",
    },
    "multiword prefix": {
        "category_original": "cultural depictions of lions",
        "expected_category": "lions",
        "expected_main_ss": "cultural depictions of",
        "expected_main_lab": "تصوير ثقافي عن {}",
    },
}


@pytest.mark.parametrize(
    "case_key, case_data",
    data.items(),
    ids=list(data.keys()),
)
@pytest.mark.fast
def testhandle_main_prefix(case_key, case_data):
    category_original = case_data["category_original"]

    result_category, main_ss, main_lab = handle_main_prefix(
        category_original,
        category_original,
    )

    assert result_category == case_data["expected_category"], f"Category mismatch in case: {case_key}"

    assert main_ss == case_data["expected_main_ss"], f"main_ss mismatch in case: {case_key}"

    assert main_lab == case_data["expected_main_lab"], f"main_lab mismatch in case: {case_key}"


def test_simple_prefix_match():
    """Prefix should be detected and removed correctly."""
    category = "fictional cats"
    category_original = category

    new_cat, prefix, label = handle_main_prefix(category, category_original)

    assert prefix == "fictional"
    assert new_cat == "cats"
    assert label == "{} خياليون"


def test_no_prefix_match():
    """Should return unchanged category if no prefix matches."""
    category = "random category"
    category_original = category

    new_cat, prefix, label = handle_main_prefix(category, category_original)

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

    new_cat, prefix, label = handle_main_prefix(category, category_original)

    assert prefix == "fictional depictions of"
    assert new_cat == "birds"
    assert label == "تصوير خيالي عن {}"


def test_prefix_with_women_singular():
    """If suffix ends with 'women', use female version if available."""
    category = "fictional women"
    category_original = category

    new_cat, prefix, label = handle_main_prefix(category, category_original)

    assert prefix == "fictional"
    assert new_cat == "women"
    assert label == "{} خياليات"  # female version


def test_prefix_with_women_apostrophe_s():
    """If suffix ends with women's, use female version."""
    category = "native women's"
    category_original = category

    new_cat, prefix, label = handle_main_prefix(category, category_original)

    assert prefix == "native"
    assert new_cat == "women's"
    assert label == "{} أصليات"


def test_case_insensitive_prefix():
    """Prefix match must be case-insensitive."""
    category = "FiCtIoNaL cats"
    category_original = category

    new_cat, prefix, label = handle_main_prefix(category, category_original)

    assert prefix.lower() == "fictional"
    assert new_cat == "cats"


def test_break_after_first_match():
    """If two prefixes could match the original string, only first (sorted) should apply."""
    category = "fictional depictions of cats"
    category_original = category

    new_cat, prefix, label = handle_main_prefix(category, category_original)

    assert prefix == "fictional depictions of"  # not "fictional"
    assert new_cat == "cats"


def test_non_prefix():
    """Test key 'non' mapping."""
    category = "non mammals"
    category_original = category

    new_cat, prefix, label = handle_main_prefix(category, category_original)

    assert prefix == "non"
    assert new_cat == "mammals"
    assert label == "{} غير"

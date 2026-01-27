#!/usr/bin/python3
"""Integration tests for FormatDataV2 with nationality placeholders."""

import pytest

from ArWikiCats.translations_formats import FormatDataV2


@pytest.fixture
def bot() -> FormatDataV2:
    """FormatDataV2 instance configured for nationality-based categories."""
    nationality_data = {
        "egyptian": {
            "male": "مصري",
            "female": "مصرية",
            "males": "مصريون",
            "females": "مصريات",
        },
        "algerian": {
            "male": "جزائري",
            "female": "جزائرية",
            "males": "جزائريون",
            "females": "جزائريات",
        },
        "moroccan": {
            "male": "مغربي",
            "female": "مغربية",
            "males": "مغاربة",
            "females": "مغربيات",
        },
        "yemeni": {
            "male": "يمني",
            "female": "يمنية",
            "males": "يمنيون",
            "females": "يمنيات",
        },
    }

    formatted_data = {
        # Uses {males}
        "{nat_en} writers": "كتاب {males}",
        "{nat_en} poets": "شعراء {males}",
        "{nat_en} people": "أعلام {males}",
        "{nat_en} heroes": "أبطال {males}",
        # Uses {male}
        "{nat_en} descent": "أصل {male}",
        # Uses {females}
        "{nat_en} women activists": "ناشطات {females}",
        "{nat_en} women politicians": "سياسيات {females}",
        "{nat_en} female singers": "مغنيات {females}",
        # Uses {female}
        "{nat_en} gods": "آلهة {female}",
        # Mixed placeholders in the same template
        "{nat_en} males and women": "رجال {males} ونساء {females}",
        # For get_template_ar tests (with/without Category: prefix)
        "{nat_en} philosophers": "فلاسفة {males}",
    }

    return FormatDataV2(
        formatted_data=formatted_data,
        data_list=nationality_data,
        key_placeholder="{nat_en}",
        text_before="the ",
    )


# -----------------------------
# Happy-path tests (all forms)
# -----------------------------

basic_cases = {
    # {males}
    "Algerian writers": "كتاب جزائريون",
    "Yemeni writers": "كتاب يمنيون",
    "Yemeni poets": "شعراء يمنيون",
    # {male}
    "Moroccan descent": "أصل مغربي",
    # {females}
    "Algerian women activists": "ناشطات جزائريات",
    "yemeni women politicians": "سياسيات يمنيات",
    "egyptian female singers": "مغنيات مصريات",
    # {female}
    "egyptian gods": "آلهة مصرية",
    # Extra spaces and mixed case
    "  Moroccan   writers  ": "كتاب مغاربة",
}


@pytest.mark.parametrize("category, expected", basic_cases.items(), ids=basic_cases.keys())
@pytest.mark.fast
def test_search_nationality_basic(bot: FormatDataV2, category: str, expected: str) -> None:
    """Ensure all basic nationality cases resolve correctly."""
    result = bot.search(category)
    assert result == expected


# -----------------------------
# Mixed placeholders
# -----------------------------


@pytest.mark.fast
def test_search_nationality_mixed_placeholders(bot: FormatDataV2) -> None:
    """Template that uses both {males} and {females} in the same label."""
    category = "Yemeni males and women"
    expected = "رجال يمنيون ونساء يمنيات"
    assert bot.search(category) == expected


# -----------------------------
# Negative / edge cases
# -----------------------------


@pytest.mark.fast
def test_search_unknown_nationality_returns_empty(bot: FormatDataV2) -> None:
    """If nationality is not in data_list, search should return an empty string."""
    assert bot.search("Spanish writers") == ""


@pytest.mark.fast
def test_search_missing_template_returns_empty(bot: FormatDataV2) -> None:
    """If template does not exist for a known nationality, search should return empty."""
    # 'Yemeni dancers' has no matching '{nat_en} dancers' template
    assert bot.search("Yemeni dancers") == ""


@pytest.mark.fast
def test_match_key_normalizes_whitespace_and_case(bot: FormatDataV2) -> None:
    """match_key should ignore extra spaces and be case-insensitive."""
    category = "   yemeni   WRITERS  "
    key = bot.match_key(category)
    assert key == "yemeni"


@pytest.mark.fast
def test_match_key_does_not_match_inside_longer_words(bot: FormatDataV2) -> None:
    """
    Ensure regex does not match nationality keys inside larger words.

    'egyptian' should not match inside 'preEgyptian'.
    """
    category = "preEgyptian writers"
    key = bot.match_key(category)
    assert key == ""


# -----------------------------
# Direct tests for helpers
# -----------------------------


@pytest.mark.fast
def test_normalize_category_with_key(bot: FormatDataV2) -> None:
    """normalize_category_with_key should return the key and placeholder-normalized category."""
    category = "Yemeni writers"
    key, normalized = bot.normalize_category_with_key(category)
    assert key == "yemeni"
    assert normalized == "{nat_en} writers"


@pytest.mark.fast
def test_get_template_ar_supports_category_prefix(bot: FormatDataV2) -> None:
    """
    get_template_ar should resolve the same template with or without 'Category:' prefix.
    """
    # Without prefix
    base_template = bot.get_template_ar("{nat_en} philosophers")
    # With 'Category:' prefix; get_template_ar should normalize
    prefixed_template = bot.get_template_ar("Category:{nat_en} philosophers")

    assert base_template == "فلاسفة {males}"
    assert prefixed_template == "فلاسفة {males}"


@pytest.mark.fast
def test_match_key_descent(bot: FormatDataV2) -> None:
    """
    "people of Moroccan-Jewish descent": "أعلام من أصل يهودي مغربي",
    Ensure regex does not match nationality keys inside larger words.

    'egyptian' should not match inside 'preEgyptian'.
    """
    category = "people of Moroccan-Jewish descent"

    key1 = bot.match_key(category)
    key2, normalized = bot.normalize_category_with_key(category)

    assert key2 == key1 == "moroccan", f"Expected 'moroccan', got {key1} and {key2}"


@pytest.mark.fast
def test_normalize_category_descent(bot: FormatDataV2) -> None:
    """
    "people of Moroccan-Jewish descent": "أعلام من أصل يهودي مغربي",
    Ensure regex does not match nationality keys inside larger words.

    'egyptian' should not match inside 'preEgyptian'.
    """
    category = "people of the Moroccan-Jewish descent"

    normalized = bot.normalize_category(category, "moroccan")

    assert normalized == "people of {nat_en}-Jewish descent"

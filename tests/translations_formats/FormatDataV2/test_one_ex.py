#!/usr/bin/python3
"""Integration tests for FormatDataV2 with nationality placeholders."""

import pytest

from ArWikiCats.translations_formats import FormatDataV2


@pytest.fixture
def bot() -> FormatDataV2:
    """FormatDataV2 instance configured for nationality-based categories."""
    nationality_data = {
        "egyptian": {
            "man": "مصري",
            "women": "مصرية",
            "men": "مصريون",
            "womens": "مصريات",
        },
        "algerian": {
            "man": "جزائري",
            "women": "جزائرية",
            "men": "جزائريون",
            "womens": "جزائريات",
        },
        "moroccan": {
            "man": "مغربي",
            "women": "مغربية",
            "men": "مغاربة",
            "womens": "مغربيات",
        },
        "yemeni": {
            "man": "يمني",
            "women": "يمنية",
            "men": "يمنيون",
            "womens": "يمنيات",
        },
    }

    formatted_data = {
        # Uses {men}
        "{nat_en} writers": "كتاب {men}",
        "{nat_en} poets": "شعراء {men}",
        "{nat_en} people": "أشخاص {men}",
        "{nat_en} heroes": "أبطال {men}",

        # Uses {man}
        "{nat_en} descent": "أصل {man}",

        # Uses {womens}
        "{nat_en} women activists": "ناشطات {womens}",
        "{nat_en} women politicians": "سياسيات {womens}",
        "{nat_en} female singers": "مغنيات {womens}",

        # Uses {women}
        "{nat_en} gods": "آلهة {women}",

        # Mixed placeholders in the same template
        "{nat_en} men and women": "رجال {men} ونساء {womens}",

        # For get_template_ar tests (with/without Category: prefix)
        "{nat_en} philosophers": "فلاسفة {men}",
    }

    return FormatDataV2(
        formatted_data=formatted_data,
        data_list=nationality_data,
        key_placeholder="{nat_en}",
        value_placeholder="{men}",  # still used for legacy string cases
    )


# -----------------------------
# Happy-path tests (all forms)
# -----------------------------

basic_cases = {
    # {men}
    "Algerian writers": "كتاب جزائريون",
    "Yemeni writers": "كتاب يمنيون",
    "Yemeni poets": "شعراء يمنيون",

    # {man}
    "Moroccan descent": "أصل مغربي",

    # {womens}
    "Algerian women activists": "ناشطات جزائريات",
    "yemeni women politicians": "سياسيات يمنيات",
    "egyptian female singers": "مغنيات مصريات",

    # {women}
    "egyptian gods": "آلهة مصرية",

    # Extra spaces and mixed case
    "  Moroccan   writers  ": "كتاب مغاربة",
}


@pytest.mark.parametrize("category, expected", basic_cases.items(), ids=list(basic_cases.keys()))
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
    """Template that uses both {men} and {womens} in the same label."""
    category = "Yemeni men and women"
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

    assert base_template == "فلاسفة {men}"
    assert prefixed_template == "فلاسفة {men}"


# -----------------------------
# Legacy behavior: string labels
# -----------------------------

@pytest.fixture
def simple_bot() -> "FormatDataV2":
    """
    FormatDataV2 instance that uses string values instead of dict values.

    This verifies that the legacy code path with `value_placeholder`
    still works correctly.
    """
    formatted_data = {
        "xoxo players": "لاعبو xoxo",
    }
    data_list = {
        "football": "كرة القدم",
    }

    return FormatDataV2(
        formatted_data=formatted_data,
        data_list=data_list,
        key_placeholder="xoxo",
        value_placeholder="xoxo",
    )


@pytest.mark.fast
def test_legacy_string_label_success(simple_bot: "FormatDataV2") -> None:
    """Ensure the legacy path (string label + single placeholder) works."""
    result = simple_bot.search("Football players")
    assert result == "لاعبو كرة القدم"


@pytest.mark.fast
def test_legacy_string_label_no_match(simple_bot: "FormatDataV2") -> None:
    """Unknown key or missing template should still return an empty string."""
    result = simple_bot.search("Basketball players")
    assert result == ""

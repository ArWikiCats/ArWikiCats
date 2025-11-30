"""
Tests
"""

import pytest

from ArWikiCats.new.end_start_bots.fax2_temp import get_templates_fo


@pytest.mark.fast
def test_get_templates_fo() -> None:
    # Test with a templates category
    list_of_cat, category3 = get_templates_fo("test templates")
    assert isinstance(list_of_cat, str)
    assert isinstance(category3, str)

    # Test with a specific template type
    list_of_cat2, category3_2 = get_templates_fo("test sidebar templates")
    assert isinstance(list_of_cat2, str)
    assert isinstance(category3_2, str)

    # Test with empty string
    list_of_cat_empty, category3_empty = get_templates_fo("")
    assert isinstance(list_of_cat_empty, str)
    assert isinstance(category3_empty, str)


@pytest.mark.fast
def test_specific_keys_in_dict_temps() -> None:
    # Test each specific known key branch
    cases = {
        "sidebar templates": "قوالب اشرطة جانبية {}",
        "politics and government templates": "قوالب سياسة وحكومة {}",
        "infobox templates": "قوالب معلومات {}",
        "squad templates": "قوالب تشكيلات {}",
    }

    for key, expected_lab in cases.items():
        inp = f"MyCategory {key}"
        list_of_cat, category3 = get_templates_fo(inp)

        assert list_of_cat == expected_lab
        assert category3 == "MyCategory"  # key removed
        assert not category3.endswith("templates")


@pytest.mark.fast
def test_generic_templates_fallback() -> None:
    # Should use: list_of_cat = "قوالب {}"
    list_of_cat, category3 = get_templates_fo("ExampleCategory templates")

    assert list_of_cat == "قوالب {}"
    assert category3 == "ExampleCategory"


@pytest.mark.fast
def test_no_templates_anywhere_returns_original() -> None:
    # If no match and doesn't end with "templates", category remains as-is
    list_of_cat, category3 = get_templates_fo("RandomCategory")

    assert list_of_cat == "قوالب {}"
    assert category3 == "RandomCategory"


@pytest.mark.fast
def test_empty_string() -> None:
    list_of_cat, category3 = get_templates_fo("")

    assert list_of_cat == "قوالب {}"
    assert category3 == ""


@pytest.mark.fast
def test_spaces_are_stripped_correctly() -> None:
    list_of_cat, category3 = get_templates_fo("  myname   templates   ")

    assert list_of_cat == "قوالب {}"
    assert category3 == "myname"


@pytest.mark.fast
def test_specific_key_with_extra_spaces() -> None:
    list_of_cat, category3 = get_templates_fo(" title   sidebar templates")

    assert list_of_cat == "قوالب اشرطة جانبية {}"
    assert category3 == "title"


@pytest.mark.fast
def test_no_key_but_word_templates_inside_not_at_end() -> None:
    # Should NOT remove "templates" in the middle
    # لأنه لا ينتهي بـ " templates"
    list_of_cat, category3 = get_templates_fo("my templates category")

    # default fallback will fire because it does NOT end with " templates"
    assert list_of_cat == "قوالب {}"
    assert category3 == "my templates category"

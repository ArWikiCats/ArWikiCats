"""
Tests
"""
import pytest

from src.make2_bots.ma_bots.end_start_bots.fax2 import get_from_starts_dict, get_from_endswith_dict, get_templates_fo, get_list_of_and_cat3, to_get_endswith, to_get_startswith


@pytest.mark.fast
def test_get_from_starts_dict():
    # Test with a basic input that starts with a known key
    category3, list_of_cat, Find_wd = get_from_starts_dict("21st century members of test", to_get_startswith)
    assert isinstance(category3, str)
    assert isinstance(list_of_cat, str)
    assert isinstance(Find_wd, bool)

    # Test with empty string
    category3_empty, list_of_cat_empty, Find_wd_empty = get_from_starts_dict("", to_get_startswith)
    assert isinstance(category3_empty, str)
    assert isinstance(list_of_cat_empty, str)
    assert isinstance(Find_wd_empty, bool)


@pytest.mark.fast
def test_get_from_endswith_dict():
    # Test with a basic input that ends with a known key
    category3, list_of_cat, Find_wd, _ = get_from_endswith_dict("test squad navigational boxes", to_get_endswith)
    assert isinstance(category3, str)
    assert isinstance(list_of_cat, str)
    assert isinstance(Find_wd, bool)

    # Test with empty string
    category3_empty, list_of_cat_empty, Find_wd_empty, _ = get_from_endswith_dict("", to_get_endswith)
    assert isinstance(category3_empty, str)
    assert isinstance(list_of_cat_empty, str)
    assert isinstance(Find_wd_empty, bool)


@pytest.mark.fast
def test_get_templates_fo():
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
def test_get_list_of_and_cat3():
    # Test with a basic input
    list_of_cat, Find_wd, Find_ko, foot_ballers, category3 = get_list_of_and_cat3("test category", "Test Category")
    assert isinstance(list_of_cat, str)
    assert isinstance(Find_wd, bool)
    assert isinstance(Find_ko, bool)
    assert isinstance(foot_ballers, bool)
    assert isinstance(category3, str)

    # Test with episodes
    list_of_cat2, Find_wd2, Find_ko2, foot_ballers2, category3_2 = get_list_of_and_cat3("test episodes", "Test Episodes")
    assert isinstance(list_of_cat2, str)
    assert isinstance(Find_wd2, bool)
    assert isinstance(Find_ko2, bool)
    assert isinstance(foot_ballers2, bool)
    assert isinstance(category3_2, str)

    # Test with empty strings
    list_of_cat_empty, Find_wd_empty, Find_ko_empty, foot_ballers_empty, category3_empty = get_list_of_and_cat3("", "")
    assert isinstance(list_of_cat_empty, str)
    assert isinstance(Find_wd_empty, bool)
    assert isinstance(Find_ko_empty, bool)
    assert isinstance(foot_ballers_empty, bool)
    assert isinstance(category3_empty, str)

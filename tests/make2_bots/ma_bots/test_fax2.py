"""
Tests
"""
import pytest

from src.make2_bots.ma_bots.fax2 import get_episodes, get_from_starts_dict, get_from_endswith_dict, get_templates_fo, get_list_of_and_cat3_with_lab2, get_list_of_and_cat3

def test_get_episodes():
    # Test with a basic episode category
    list_of_cat, category3 = get_episodes("2016 american television episodes", "2016 American television episodes")
    assert isinstance(list_of_cat, str)
    assert isinstance(category3, str)

    # Test with season episodes
    list_of_cat2, category3_2 = get_episodes("game of thrones (season 1) episodes", "Game of Thrones (season 1) episodes")
    assert isinstance(list_of_cat2, str)
    assert isinstance(category3_2, str)

    # Test with empty string
    list_of_cat_empty, category3_empty = get_episodes("", "")
    assert isinstance(list_of_cat_empty, str)
    assert isinstance(category3_empty, str)

def test_get_from_starts_dict():
    # Test with a basic input that starts with a known key
    category3, list_of_cat, Find_wd = get_from_starts_dict("21st century members of test")
    assert isinstance(category3, str)
    assert isinstance(list_of_cat, str)
    assert isinstance(Find_wd, bool)

    # Test with empty string
    category3_empty, list_of_cat_empty, Find_wd_empty = get_from_starts_dict("")
    assert isinstance(category3_empty, str)
    assert isinstance(list_of_cat_empty, str)
    assert isinstance(Find_wd_empty, bool)

def test_get_from_endswith_dict():
    # Test with a basic input that ends with a known key
    category3, list_of_cat, Find_wd = get_from_endswith_dict("test squad navigational boxes")
    assert isinstance(category3, str)
    assert isinstance(list_of_cat, str)
    assert isinstance(Find_wd, bool)

    # Test with empty string
    category3_empty, list_of_cat_empty, Find_wd_empty = get_from_endswith_dict("")
    assert isinstance(category3_empty, str)
    assert isinstance(list_of_cat_empty, str)
    assert isinstance(Find_wd_empty, bool)

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

def test_get_list_of_and_cat3_with_lab2():
    # Test with a basic input
    result = get_list_of_and_cat3_with_lab2("test category", "Test Category")
    assert isinstance(result, str)

    # Test with squad templates
    result_squad = get_list_of_and_cat3_with_lab2("test squad templates", "Test Squad Templates")
    assert isinstance(result_squad, str)

    # Test with empty strings
    result_empty = get_list_of_and_cat3_with_lab2("", "")
    assert isinstance(result_empty, str)

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
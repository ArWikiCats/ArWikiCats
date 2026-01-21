"""
Tests
"""

import pytest

from ArWikiCats.legacy_bots.end_start_bots.fax2 import (
    get_from_endswith_dict,
    get_from_starts_dict,
    get_list_of_and_cat3,
    to_get_endswith,
    to_get_startswith,
)


@pytest.mark.fast
def test_get_from_starts_dict() -> None:
    # Test with a basic input that starts with a known key
    category3, list_of_cat = get_from_starts_dict("21st century members of test", to_get_startswith)
    assert isinstance(category3, str)
    assert isinstance(list_of_cat, str)

    # Test with empty string
    category3_empty, list_of_cat_empty = get_from_starts_dict("", to_get_startswith)
    assert isinstance(category3_empty, str)
    assert isinstance(list_of_cat_empty, str)


@pytest.mark.fast
def test_get_from_endswith_dict() -> None:
    # Test with a basic input that ends with a known key
    category3, list_of_cat = get_from_endswith_dict("test squad navigational boxes", to_get_endswith)
    assert isinstance(category3, str)
    assert isinstance(list_of_cat, str)

    # Test with empty string
    category3_empty, list_of_cat_empty = get_from_endswith_dict("", to_get_endswith)
    assert isinstance(category3_empty, str)
    assert isinstance(list_of_cat_empty, str)


@pytest.mark.fast
def test_get_list_of_and_cat3() -> None:
    # Test with a basic input
    list_of_cat, foot_ballers, category3 = get_list_of_and_cat3("test category", "Test Category")
    assert isinstance(list_of_cat, str)
    assert isinstance(foot_ballers, bool)
    assert isinstance(category3, str)

    # Test with episodes
    list_of_cat22, foot_ballers2, category3_2 = get_list_of_and_cat3("test episodes", "Test Episodes")
    assert isinstance(foot_ballers2, bool)
    assert isinstance(category3_2, str)

    # Test with empty strings
    list_of_cat_empty, foot_ballers_empty, category3_empty = get_list_of_and_cat3("", "")
    assert isinstance(list_of_cat_empty, str)
    assert isinstance(foot_ballers_empty, bool)
    assert isinstance(category3_empty, str)

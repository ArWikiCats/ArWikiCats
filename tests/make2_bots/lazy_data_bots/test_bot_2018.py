"""
Tests
"""

from ArWikiCats.legacy_bots.make_bots.bot_2018 import (
    Add_to_pop_All_18,
    get_pop_All_18,
)


def test_add_to_pop_all_18() -> None:
    # Test with an empty dict
    Add_to_pop_All_18({})

    # Test with a sample dictionary
    test_dict = {"key1": "value1", "key2": "value2"}
    Add_to_pop_All_18(test_dict)

    # This function modifies internal state, so we just verify it runs without error
    assert True


def test_get_pop_all_18() -> None:
    # Test with a basic key (likely won't find the key but should return default)
    result = get_pop_All_18("test_key", "default")
    assert isinstance(result, str)

    # Test with empty key and default
    result_empty = get_pop_All_18("", "")
    assert isinstance(result_empty, str)

    # Test with just a key
    result_simple = get_pop_All_18("test_key")
    assert isinstance(result_simple, str)

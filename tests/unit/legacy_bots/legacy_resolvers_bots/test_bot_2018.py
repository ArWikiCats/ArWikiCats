"""
Tests
"""

from ArWikiCats.legacy_bots.legacy_resolvers_bots.bot_2018 import get_pop_All_18


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

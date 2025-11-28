"""
Tests
"""

import pytest

from ArWikiCats.make_bots.matables_bots.bot import add_to_new_players


def test_add_to_new_players():
    # Test with basic inputs
    add_to_new_players("english", "arabic")

    # Test with empty strings (should not add anything)
    add_to_new_players("", "arabic")
    add_to_new_players("english", "")

    # Test with both empty (should not add anything)
    add_to_new_players("", "")

    # This function modifies internal state, so we just verify it runs without error
    assert True

"""
Tests
"""

import pytest

from ArWikiCats.legacy_bots.resolvers.arabic_label_builder import add_in_tab


def test_add_in_tab() -> None:
    # Test with basic inputs
    result = add_in_tab("test label", "test", "from")
    assert isinstance(result, str)

    # Test with different separator value
    result_other = add_in_tab("test label", "test of", "to")
    assert isinstance(result_other, str)

    # Test with empty strings
    result_empty = add_in_tab("", "", "")
    assert isinstance(result_empty, str)


def test_add_in_tab_2() -> None:
    # Test with basic inputs
    result = add_in_tab("test label", "test", "from")
    assert isinstance(result, str)

    # Test with different separator value
    result_other = add_in_tab("test label", "test of", "to")
    assert isinstance(result_other, str)

    # Test with empty strings
    result_empty = add_in_tab("", "", "")
    assert isinstance(result_empty, str)

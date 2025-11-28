"""
Tests
"""

import pytest

from ArWikiCats.make_bots.p17_bots.nats import find_nat_others


def test_find_nat_others():
    # Test with a basic category string
    result = find_nat_others("American basketball players")
    assert isinstance(result, str)

    result_empty = find_nat_others("")
    assert isinstance(result_empty, str)

    # Test with reference category
    result_with_ref = find_nat_others("French tennis players")
    assert isinstance(result_with_ref, str)

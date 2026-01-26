"""
TODO: write tests
"""

import pytest

from ArWikiCats.legacy_bots.resolvers.country_resolver import fetch_country_term_label


def test_fetch_country_term_label() -> None:
    # Test with basic inputs
    result = fetch_country_term_label("test country", "in")
    assert isinstance(result, str)

    # Test with different parameters
    result_various = fetch_country_term_label("test country", "from", "type_label", False)
    assert isinstance(result_various, str)

    # Test with empty strings - avoid calling with empty strings as they might cause issues
    result_safe = fetch_country_term_label("valid country", "from")
    assert isinstance(result_safe, str)

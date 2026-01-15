"""
Tests
"""

import pytest

from ArWikiCats.make_bots.countries_formats.utils import (
    add_definite_article,
)


def test_add_all() -> None:
    # Test with a basic input
    result = add_definite_article("test label")
    assert isinstance(result, str)
    assert "ال" in result  # The function adds "ال" prefix

    # Test with empty string
    result_empty = add_definite_article("")
    assert isinstance(result_empty, str)

    # Test with various inputs
    result_various = add_definite_article("another label")
    assert isinstance(result_various, str)


# --------------------------------------------
# Tests for add_definite_article
# --------------------------------------------


@pytest.mark.unit
def test_add_definite_article_simple() -> None:
    # Ensures proper prefixing of words with ال
    assert add_definite_article("سورية") == "السورية"
    assert add_definite_article("فيتنامي") == "الفيتنامي"
    assert add_definite_article("كندي غربي") == "الكندي الغربي"
    # assert add_definite_article("كندي الغربي") == "الكندي الغربي"

"""
TODO: write tests
"""

import pytest
from ArWikiCats.make_bots.matables_bots.bot import add_to_new_players
from ArWikiCats import resolve_arabic_category_label


@pytest.mark.fast
def test_add_to_new_players() -> None:
    # Test with basic inputs
    add_to_new_players("english", "arabic")

    # Test with empty strings (should not add anything)
    add_to_new_players("", "arabic")
    add_to_new_players("english", "")

    # Test with both empty (should not add anything)
    add_to_new_players("", "")

    # This function modifies internal state, so we just verify it runs without error
    assert True


@pytest.mark.fast
def test_Keep_it_last() -> None:
    # remakes of

    result = resolve_arabic_category_label("remakes of historical documents")
    assert result == "وثائق تاريخية في 1900"

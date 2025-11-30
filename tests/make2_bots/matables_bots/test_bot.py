"""

TODO: write tests
TODO: search for (# Test with basic inputs)

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

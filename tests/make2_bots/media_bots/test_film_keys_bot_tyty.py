"""
Tests
"""

import pytest

from ArWikiCats.make_bots.media_bots.film_keys_bot_tyty import get_films_key_tyty

fast_data2 = {
}


@pytest.mark.parametrize("category, expected", fast_data2.items(), ids=list(fast_data2.keys()))
@pytest.mark.fast
def test_get_films_key_tyty(category: str, expected: str) -> None:
    label = get_films_key_tyty(category)
    assert label == expected

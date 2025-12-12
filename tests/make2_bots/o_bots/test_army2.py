"""
Tests
"""

import pytest

from ArWikiCats.translations_resolvers_v2.army2 import resolve_secretaries_labels

fast_data = {
    "United States secretaries-of war": "وزراء حرب أمريكيون",
    "secretaries-of war of yemen": "وزراء حرب يمنيون",
}


@pytest.mark.parametrize("category, expected", fast_data.items(), ids=list(fast_data.keys()))
@pytest.mark.fast
def test_fast_data(category: str, expected: str) -> None:
    label = resolve_secretaries_labels(category)
    assert label == expected

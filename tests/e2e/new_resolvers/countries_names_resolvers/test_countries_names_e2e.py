"""
E2E tests for countries names resolvers
"""

import pytest

from ArWikiCats import resolve_label_ar

data_main = {
    "Spies for Federal Republic of Germany": "جواسيس لصالح جمهورية ألمانيا الاتحادية",
    "Spies for Soviet Union by nationality": "جواسيس لصالح الاتحاد السوفيتي حسب الجنسية",
    "World War I spies for Russian Empire": "جواسيس الحرب العالمية الأولى لصالح الإمبراطورية الروسية",
}


@pytest.mark.parametrize("category, expected", data_main.items(), ids=data_main.keys())
@pytest.mark.fast
def test_resolve_main(category: str, expected: str) -> None:
    label = resolve_label_ar(category)
    assert label == expected

"""
tests
"""

import pytest
from ArWikiCats.translations_resolvers.nats_women import nats_women_label
from ArWikiCats import resolve_arabic_category_label

all_test_data = {
    "non-american television series": "مسلسلات تلفزيونية غير أمريكية",
    "non american television series": "مسلسلات تلفزيونية غير أمريكية",
    "non yemeni television series": "مسلسلات تلفزيونية غير يمنية",
    "non-yemeni television series": "مسلسلات تلفزيونية غير يمنية",
}


@pytest.mark.parametrize("category, expected_key", all_test_data.items(), ids=list(all_test_data.keys()))
@pytest.mark.slow
def test_nats_women_label(category: str, expected_key: str) -> None:
    label2 = nats_women_label(category)
    assert label2 == expected_key


all_test_data = {
    "Category:Non-American television series based on American television series": "تصنيف:مسلسلات تلفزيونية غير أمريكية مبنية على مسلسلات تلفزيونية أمريكية",
}


@pytest.mark.parametrize("category, expected_key", all_test_data.items(), ids=list(all_test_data.keys()))
@pytest.mark.slow
def test_with_resolve_arabic_category_label(category: str, expected_key: str) -> None:
    label2 = resolve_arabic_category_label(category)
    assert label2 == expected_key

"""
Tests
"""

import pytest

from ArWikiCats.new_resolvers.languages_resolves import resolve_languages_labels_with_time

test_data_0 = {}

test_data = {
    "Cantonese-language singers": "مغنون باللغة الكانتونية",
    "urdu-language non-fiction writers": "كتاب غير روائيين باللغة الأردية",
    "arabic-language writers": "كتاب باللغة العربية",
    "arabic language writers": "كتاب باللغة العربية",
    "abkhazian-language writers": "كتاب باللغة الأبخازية",
    "2010 Tamil-language television seasons": "مواسم تلفزيونية باللغة التاميلية في 2010",
}


@pytest.mark.parametrize("input_category, expected_output", test_data.items(), ids=test_data.keys())
@pytest.mark.fast
def test_resolve_languages_labels(input_category: str, expected_output: str) -> None:
    result = resolve_languages_labels_with_time(input_category)
    assert result == expected_output

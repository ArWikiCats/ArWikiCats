"""
Tests
"""

import pytest

from ArWikiCats.new_resolvers.languages_resolves import resolve_languages_labels_with_time

test_data_0 = {
    "Persian-language singers of Tajikistan": "مغنون باللغة الفارسية في طاجيكستان",
    "Yiddish-language singers of Austria": "مغنون باللغة اليديشية في النمسا",
    "Yiddish-language singers of Russia": "مغنون باللغة اليديشية في روسيا",
    "Tajik-language singers of Russia": "مغنون باللغة الطاجيكية في روسيا",
    "Persian-language singers of Russia": "مغنون باللغة الفارسية في روسيا",
    "Hebrew-language singers of Russia": "مغنون باللغة العبرية في روسيا",
    "German-language singers of Russia": "مغنون باللغة الألمانية في روسيا",
    "Azerbaijani-language singers of Russia": "مغنون باللغة الأذربيجانية في روسيا",
}

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

"""
Tests
"""

import pytest

from ArWikiCats.new_resolvers.resolve_languages import resolve_languages_labels

test_data = {
    "Category:Persian-language singers of Tajikistan": "تصنيف:مغنون باللغة الفارسية في طاجيكستان",
    "Category:2010 Tamil-language television seasons": "تصنيف:مواسم تلفزيونية باللغة التاميلية 2010",
    "Category:Urdu-language fiction": "تصنيف:خيالية باللغة الأردية",
    "Category:Cantonese-language singers": "تصنيف:مغنون باللغة الكانتونية",
    "Category:Yiddish-language singers of Austria": "تصنيف:مغنون باللغة اليديشية في النمسا",
    "Category:Yiddish-language singers of Russia": "تصنيف:مغنون باللغة اليديشية في روسيا",
    "Category:Tajik-language singers of Russia": "تصنيف:مغنون باللغة الطاجيكية في روسيا",
    "Category:Persian-language singers of Russia": "تصنيف:مغنون باللغة الفارسية في روسيا",
    "Category:Hebrew-language singers of Russia": "تصنيف:مغنون باللغة العبرية في روسيا",
    "Category:German-language singers of Russia": "تصنيف:مغنون باللغة الألمانية في روسيا",
    "Category:Azerbaijani-language singers of Russia": "تصنيف:مغنون باللغة الأذربيجانية في روسيا",
    "category:urdu-language non-fiction writers": "تصنيف:كتاب غير روائيين باللغة الأردية",
    "bengali-language romantic comedy films": "أفلام كوميدية رومانسية باللغة البنغالية",
    "cantonese-language speculative fiction films": "أفلام خيالية تأملية باللغة الكانتونية",
    "abkhazian-language writers": "كتاب باللغة الأبخازية",
}


@pytest.mark.parametrize("input_category, expected_output", test_data.items())
@pytest.mark.skip2
def test_resolve_languages_labels(input_category: str, expected_output: str) -> None:
    result = resolve_languages_labels(input_category)
    assert result == expected_output

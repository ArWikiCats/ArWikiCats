"""
Tests
"""

import pytest

from ArWikiCats.legacy_bots.o_bots.parties_resolver import get_parties_lab

fast_data = {
    # Basic party lookups (if applicable via FormatData or fallback)
    # Note: currently get_parties_lab only uses .search() which matches patterns.
    # If the pattern is just {party_key}, it might match.
    # Let's check if there is a pattern for just the party name.

    # Based on formatted_data in parties_resolver.py:
    "libertarian party of canada candidates": "مرشحو الحزب التحرري الكندي",
    "libertarian party-of-canada candidates": "مرشحو الحزب التحرري الكندي",
    "new labour leaders": "قادة حزب العمال الجديد",
    "pakistan peoples party politicians": "سياسيو حزب الشعب الباكستاني",
    "party for freedom members": "أعضاء حزب من أجل الحرية",
    "green party of the united states state governors": "حكام ولايات من حزب الخضر الأمريكي",
    "republican party of armenia candidates for member of parliament": "مرشحو حزب أرمينيا الجمهوري لعضوية البرلمان",

    # More variations
    "workers' party of korea members": "أعضاء حزب العمال الكوري",
    "scottish national party leaders": "قادة الحزب القومي الإسكتلندي",
    "serbian radical party politicians": "سياسيو الحزب الراديكالي الصربي",
}


@pytest.mark.parametrize("category, expected", fast_data.items(), ids=fast_data.keys())
@pytest.mark.fast
def test_fast_data(category: str, expected: str) -> None:
    label = get_parties_lab(category)
    assert label == expected


def test_get_parties_lab() -> None:
    # Test with a basic input
    result = get_parties_lab("republican party")
    assert isinstance(result, str)

    result_empty = get_parties_lab("")
    assert isinstance(result_empty, str)

    # Test with various inputs
    result_various = get_parties_lab("some party")
    assert isinstance(result_various, str)

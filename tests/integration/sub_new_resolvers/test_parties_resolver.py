"""
Tests
"""

import pytest

from ArWikiCats.sub_new_resolvers.parties_resolver import get_parties_lab

fast_data = {
    # {party_key} candidates for member of parliament
    "republican party of armenia candidates for member of parliament": "مرشحو حزب أرمينيا الجمهوري لعضوية البرلمان",
    # {party_key} candidates for member-of-parliament
    "republican party of armenia candidates for member-of-parliament": "مرشحو حزب أرمينيا الجمهوري لعضوية البرلمان",
    # {party_key} candidates
    "libertarian party of canada candidates": "مرشحو الحزب التحرري الكندي",
    # {party_key} leaders
    "new labour leaders": "قادة حزب العمال الجديد",
    # {party_key} politicians
    "pakistan peoples party politicians": "سياسيو حزب الشعب الباكستاني",
    # {party_key} members
    "party for freedom members": "أعضاء حزب من أجل الحرية",
    # {party_key} state governors
    "green party of the united states state governors": "حكام ولايات من حزب الخضر الأمريكي",
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

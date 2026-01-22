"""
TODO: write tests
"""

import pytest
from utils.dump_runner import make_dump_test_name_data

from ArWikiCats import resolve_label_ar

data_1 = {
    "Category:July 2010 crimes": "تصنيف:جرائم يوليو 2010",
    "Category:June 2010 crimes": "تصنيف:جرائم يونيو 2010",
    "Category:March 2010 crimes": "تصنيف:جرائم مارس 2010",
    "Category:February 2010 crimes": "تصنيف:جرائم فبراير 2010",
    "Category:February 2010 events by country": "تصنيف:أحداث فبراير 2010 حسب البلد",
    "Category:August 2010 crimes": "تصنيف:جرائم أغسطس 2010",
    "Category:Businesspeople in aviation by nationality": "تصنيف:شخصيات أعمال في الطيران حسب الجنسية",
    "2010 in motorsport by country": "رياضة المحركات في 2010 حسب البلد",
    "2010s in international relations": "علاقات دولية في عقد 2010",
    "2010s in law": "القانون في عقد 2010",
    "2010s introductions": "استحداثات عقد 2010",
    "2010s meteorology": "الأرصاد الجوية في عقد 2010",
    "2010s murders": "جرائم قتل في عقد 2010",
    "2010s natural disasters": "كوارث طبيعية في عقد 2010",
    "2010s non-fiction books": "كتب غير خيالية عقد 2010",
    "2010s paintings": "لوحات عقد 2010",
    "2010s plays": "مسرحيات عقد 2010",
    "2010s poems": "قصائد عقد 2010",
    "2010s sculptures": "منحوتات عقد 2010",
    "2010s ships": "سفن عقد 2010",
    "2010s short stories": "قصص قصيرة عقد 2010",
    "2010s songs": "أغاني عقد 2010",
    "2010s treaties": "معاهدات في عقد 2010",
    "2010s works": "أعمال عقد 2010",
    "21st-century BC births": "مواليد القرن 21 ق م",
    "220 BC births": "مواليد 220 ق م",
    "260 births": "مواليد 260",
    "276 births": "مواليد 276",
    "278 deaths": "وفيات 278",
    "298 deaths": "وفيات 298",
    "365 BC deaths": "وفيات 365 ق م",
    "448 births": "مواليد 448",
    "498 births": "مواليد 498",
    "501 deaths": "وفيات 501",
    "540s births": "مواليد عقد 540",
    "647 births": "مواليد 647",
    "672 deaths": "وفيات 672",
    "721 births": "مواليد 721",
    "730s births": "مواليد عقد 730",
    "808 births": "مواليد 808",
    "921 births": "مواليد 921",
    "969 births": "مواليد 969"
}


TEMPORAL_CASES = [
    ("test_resolve_label_ar_1", data_1),
]


@pytest.mark.parametrize("category, expected", data_1.items(), ids=data_1.keys())
@pytest.mark.fast
def test_resolve_label_ar_1(category: str, expected: str) -> None:
    label = resolve_label_ar(category)
    assert label == expected


test_dump_all = make_dump_test_name_data(TEMPORAL_CASES, resolve_label_ar, run_same=False)

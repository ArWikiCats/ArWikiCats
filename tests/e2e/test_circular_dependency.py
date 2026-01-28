""" """

import pytest

from ArWikiCats import resolve_label_ar
from utils.dump_runner import make_dump_test_name_data

data_0 = {
    "Suicides by Jews during Holocaust": "منتحرون بواسطة يهود خلال هولوكوست",
    "Persecution of Christians by Hindus": "اضطهاد مسيحيون بواسطة هندوس",
    "Persecution of Christians by Jews": "اضطهاد مسيحيون بواسطة يهود",
    "Persecution of Christians by Muslims": "اضطهاد مسيحيون بواسطة مسلمون",
    "Persecution of Hindus by Muslims": "اضطهاد هندوس بواسطة مسلمون",
    "Persecution of Muslims by Christians": "اضطهاد مسلمون بواسطة مسيحيون",
    "Persecution of Muslims by Jews": "اضطهاد مسلمون بواسطة يهود",
    "Persecution of Yazidis by Muslims": "اضطهاد يزيديون بواسطة مسلمون",
}

data_1 = {
    "Water resource management in Netherlands": "إدارة الموارد المائية في هولندا",
    "Sports ministers of Comoros": "وزراء رياضة جزر القمر",
    "Sports ministers of Nauru": "وزراء رياضة ناورو",
    "Sports ministers of Sri Lanka": "وزراء رياضة سريلانكا",
    "National sports teams of Saint Helena": "منتخبات رياضية وطنية في سانت هيلانة",
    "November 2010 crimes": "جرائم نوفمبر 2010",
    "October 2010 crimes": "جرائم أكتوبر 2010",
    "July 2010 crimes": "جرائم يوليو 2010",
    "June 2010 crimes": "جرائم يونيو 2010",
    "March 2010 crimes": "جرائم مارس 2010",
    "February 2010 crimes": "جرائم فبراير 2010",
    "February 2010 events by country": "أحداث فبراير 2010 حسب البلد",
    "August 2010 crimes": "جرائم أغسطس 2010",
    "Businesspeople in aviation by nationality": "شخصيات أعمال في طيران حسب الجنسية",
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
    "969 births": "مواليد 969",
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

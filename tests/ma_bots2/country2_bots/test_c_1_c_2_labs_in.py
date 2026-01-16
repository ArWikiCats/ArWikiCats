"""
Tests
"""

import pytest
from load_one_data import dump_diff, one_dump_test

from ArWikiCats.legacy_bots.ma_bots2.country2_label_bot import c_1_1_lab

test_data = {
    "american football teams": "فرق كرة قدم أمريكية",
    "art museums and galleries": "متاحف فنية ومعارض",
    "asian games medalists": "فائزون بميداليات الألعاب الآسيوية",
    "bosnia and herzegovina": "البوسنة والهرسك",
    "buildings and structures": "مبان ومنشآت",
    "by high school": "حسب المدرسة الثانوية",
    "by populated place and occupation": "حسب المكان المأهول والمهنة",
    "canadian chief executives": "رؤساء تنفيذيون كنديون",
    "cities and towns": "مدن وبلدات",
    "clubs and societies": "أندية وجمعيات",
    "covid-19 pandemic": "جائحة فيروس كورونا",
    "deaths due to animal attacks": "وفيات ناجمة عن هجمات الحيوانات",
    "deaths from cancer": "وفيات السرطان",
    "disused railway stations": "محطات سكك حديدية مهجورة",
    "dutch chief executives": "رؤساء تنفيذيون هولنديون",
    "electric power infrastructure": "بنية تحتية للقدرة الكهربائية",
    "field hockey clubs": "أندية هوكي ميدان",
    "field hockey playerss": "لاعبو هوكي ميدان",
    "finnish military personnel": "أفراد عسكريون فنلنديون",
    "food and drink": "أطعمة ومشروبات",
    "former buildings and structures": "مبان ومنشآت سابقة",
    "former populated places": "أماكن كانت مأهولة",
    "french-language radio stations": "محطات إذاعية باللغة الفرنسية",
    "gaelic football clubs": "أندية كرة قدم غالية",
    "german prisoners of war": "أسرى ألمان",
    "historic american buildings survey": "مسح المبان التاريخية الأمريكية",
    "hong kong businesspeople": "شخصيات أعمال هونغ كونغية",
    "ice hockey playerss": "لاعبو هوكي جليد",
    "indonesian expatriate sports-people": "رياضيون إندونيسيون مغتربون",
    "jews and judaism": "اليهود واليهودية",
    "libertarian party-of-canada candidates": "مرشحو الحزب التحرري الكندي",
    "mayors of places": "رؤساء بلديات",
    "media and communications": "الإعلام والاتصالات",
    "medical research institutes": "معاهد أبحاث طبية",
    "military units and formations": "وحدات وتشكيلات عسكرية",
    "monuments and memorials": "معالم أثرية ونصب تذكارية",
    "new democratic party candidates": "مرشحو الحزب الديمقراطي الجديد",
    "north american competitors": "منافسون أمريكيون شماليون",
    "pan american games silver medalists": "فائزون بميداليات فضية في دورة الألعاب الأمريكية",
    "papua new guinea": "بابوا غينيا الجديدة",
    "parks and open spaces": "متنزهات ومساحات مفتوحة",
    "places of worship": "أماكن عبادة",
    "polish air force": "القوات الجوية البولندية",
    "populated coastal places": "أماكن ساحلية مأهولة",
    "road incident deaths": "وفيات حوادث الطرق",
    "roman catholic archbishops": "رؤساء أساقفة رومان كاثوليك",
    "roman catholic bishops": "أساقفة كاثوليك رومان",
    "roman catholic churches": "كنائس رومانية كاثوليكية",
    "rugby league playerss": "لاعبو دوري رجبي",
    "rugby union leagues": "اتحاد دوري الرجبي",
    "rugby union teams": "فرق اتحاد رجبي",
    "science and technology": "العلوم والتقانة",
    "sierra leonean expatriates": "سيراليونيون مغتربون",
    "south african businesspeople": "شخصيات أعمال جنوب إفريقية",
    "south american competitors": "منافسون أمريكيون جنوبيون",
    "television series produced": "مسلسلات تلفزيونية أنتجت",
    "television series set": "مسلسلات تلفزيونية تقع أحداثها",
    "television shows filmed": "عروض تلفزيونية صورت",
    "television shows set": "عروض تلفزيونية تقع أحداثها",
    "television shows shot": "عروض تلفزيونية مصورة",
    "towns and villages": "بلدات وقرى",
    "track and field athletes": "رياضيو المسار والميدان",
    "transport buildings and structures": "مبان ومنشآت نقل",
    "united states house-of-representatives elections": "انتخابات مجلس النواب الأمريكي",
}


@pytest.mark.parametrize("category, expected", test_data.items(), ids=test_data.keys())
@pytest.mark.fast
def test_c_1_1_lab_3(category: str, expected: str) -> None:
    label = c_1_1_lab(" in ", category, with_years=False)
    assert label == expected

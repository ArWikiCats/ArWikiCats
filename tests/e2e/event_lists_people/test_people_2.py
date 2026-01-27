#
import pytest

from ArWikiCats import resolve_label_ar
from utils.dump_runner import make_dump_test_name_data

data1 = {
    "Afghan emigrants": "أفغان مهاجرون",
    "Afghan expatriates": "أفغان مغتربون",
    "Ambassadors of Afghanistan to Argentina": "سفراء أفغانستان لدى الأرجنتين",
    "Ambassadors of Afghanistan to Australia": "سفراء أفغانستان لدى أستراليا",
    "American people by status": "أمريكيون حسب الحالة",
    "American people of the Iraq War": "أمريكيون في حرب العراق",
    "European women in business": "أوروبيات في الأعمال",
    "Ivorian emigrants": "إيفواريون مهاجرون",
    "Ivorian expatriates": "إيفواريون مغتربون",
    "Polish businesspeople": "شخصيات أعمال بولندية",
    "Polish women in business": "بولنديات في الأعمال",
}

data2 = {
    # "sports-people from Westchester County, New York": "رياضيون من مقاطعة ويستتشستر (نيويورك)",
    "Mixed martial artists from Massachusetts": "مقاتلو فنون قتالية مختلطة من ماساتشوستس",
    "People from Buenos Aires": "أشخاص من بوينس آيرس",
    "Players of American football from Massachusetts": "لاعبو كرة قدم أمريكية من ماساتشوستس",
    "Professional wrestlers from Massachusetts": "مصارعون محترفون من ماساتشوستس",
    "Racing drivers from Massachusetts": "سائقو سيارات سباق من ماساتشوستس",
    "Singers from Buenos Aires": "مغنون من بوينس آيرس",
    "Soccer players from Massachusetts": "لاعبو كرة قدم من ماساتشوستس",
    "Sports coaches from Massachusetts": "مدربو رياضة من ماساتشوستس",
    "Sportswriters from Massachusetts": "كتاب رياضيون من ماساتشوستس",
}
data3 = {
    "Baseball players from Massachusetts": "لاعبو كرة قاعدة من ماساتشوستس",
    "Basketball coaches from Indiana": "مدربو كرة سلة من إنديانا",
    "Basketball people from Indiana": "أعلام كرة سلة من إنديانا",
    "Basketball players from Indiana": "لاعبو كرة سلة من إنديانا",
    "Basketball players from Massachusetts": "لاعبو كرة سلة من ماساتشوستس",
    "Boxers from Massachusetts": "ملاكمون من ماساتشوستس",
    "Female single skaters from Georgia (country)": "متزلجات فرديات من جورجيا",
    "Golfers from Massachusetts": "لاعبو غولف من ماساتشوستس",
    "Ice hockey people from Massachusetts": "أعلام هوكي جليد من ماساتشوستس",
    "Immigrants to the United Kingdom from Aden": "مهاجرون إلى المملكة المتحدة من عدن",
    "Kickboxers from Massachusetts": "مقاتلو كيك بوكسنغ من ماساتشوستس",
    "Lacrosse players from Massachusetts": "لاعبو لاكروس من ماساتشوستس",
    "Swimmers from Massachusetts": "سباحون من ماساتشوستس",
    "Tennis people from Massachusetts": "أعلام كرة مضرب من ماساتشوستس",
    "Track and field athletes from Massachusetts": "رياضيو المسار والميدان من ماساتشوستس",
}

to_test = [
    ("test_people_labels_1", data1),
    ("test_people_labels_2", data2),
    ("test_people_labels_3", data3),
]


@pytest.mark.parametrize("category, expected", data1.items(), ids=data1.keys())
@pytest.mark.fast
def test_people_labels_1(category: str, expected: str) -> None:
    label = resolve_label_ar(category)
    assert label == expected


@pytest.mark.parametrize("category, expected", data2.items(), ids=data2.keys())
@pytest.mark.fast
def test_people_labels_2(category: str, expected: str) -> None:
    label = resolve_label_ar(category)
    assert label == expected


@pytest.mark.parametrize("category, expected", data3.items(), ids=data3.keys())
@pytest.mark.fast
def test_people_labels_3(category: str, expected: str) -> None:
    label = resolve_label_ar(category)
    assert label == expected


test_dump_all = make_dump_test_name_data(to_test, resolve_label_ar, run_same=True)

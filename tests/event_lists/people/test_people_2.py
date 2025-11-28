#
import pytest
from load_one_data import dump_diff, one_dump_test

from src import resolve_arabic_category_label

data1 = {
    "Category:Afghan emigrants": "تصنيف:أفغان مهاجرون",
    "Category:Afghan expatriates": "تصنيف:أفغان مغتربون",
    "Category:Ambassadors of Afghanistan to Argentina": "تصنيف:سفراء أفغانستان لدى الأرجنتين",
    "Category:Ambassadors of Afghanistan to Australia": "تصنيف:سفراء أفغانستان لدى أستراليا",
    "Category:American people by status": "تصنيف:أعلام أمريكيون حسب الحالة",
    "Category:American people of the Iraq War": "تصنيف:أمريكيون في حرب العراق",
    "Category:European women in business": "تصنيف:أوروبيات في الأعمال",
    "Category:Ivorian emigrants": "تصنيف:إيفواريون مهاجرون",
    "Category:Ivorian expatriates": "تصنيف:إيفواريون مغتربون",
    "Category:Polish businesspeople": "تصنيف:شخصيات أعمال بولندية",
    "Category:Polish women in business": "تصنيف:بولنديات في الأعمال",
}

data2 = {
    "Category:Mixed martial artists from Massachusetts": "تصنيف:مقاتلو فنون قتالية مختلطة من ماساتشوستس",
    "Category:People from Buenos Aires": "تصنيف:أشخاص من بوينس آيرس",
    "Category:People from Westchester County, New York by city": "تصنيف:أشخاص من مقاطعة ويستتشستر (نيويورك) حسب المدينة",
    "Category:People from Westchester County, New York by hamlet": "تصنيف:أشخاص من مقاطعة ويستتشستر (نيويورك) حسب القرية",
    "Category:People from Westchester County, New York by town": "تصنيف:أشخاص من مقاطعة ويستتشستر (نيويورك) حسب البلدة",
    "Category:People from Westchester County, New York by village": "تصنيف:أشخاص من مقاطعة ويستتشستر (نيويورك) حسب القرية",
    "Category:People from Westchester County, New York": "تصنيف:أشخاص من مقاطعة ويستتشستر (نيويورك)",
    "Category:Players of American football from Massachusetts": "تصنيف:لاعبو كرة قدم أمريكية من ماساتشوستس",
    "Category:Professional wrestlers from Massachusetts": "تصنيف:مصارعون محترفون من ماساتشوستس",
    "Category:Racing drivers from Massachusetts": "تصنيف:سائقو سيارات سباق من ماساتشوستس",
    "Category:Singers from Buenos Aires": "تصنيف:مغنون من بوينس آيرس",
    "Category:Soccer players from Massachusetts": "تصنيف:لاعبو كرة قدم من ماساتشوستس",
    "Category:Sports coaches from Massachusetts": "تصنيف:مدربو رياضة من ماساتشوستس",
    "Category:Sportspeople from Westchester County, New York": "تصنيف:رياضيون من مقاطعة ويستتشستر (نيويورك)",
    "Category:Sportswriters from Massachusetts": "تصنيف:كتاب رياضيون من ماساتشوستس",
}
data3 = {
    "Category:Baseball players from Massachusetts": "تصنيف:لاعبو كرة قاعدة من ماساتشوستس",
    "Category:Basketball coaches from Indiana": "تصنيف:مدربو كرة سلة من إنديانا",
    "Category:Basketball people from Indiana": "تصنيف:أعلام كرة سلة من إنديانا",
    "Category:Basketball players from Indiana": "تصنيف:لاعبو كرة سلة من إنديانا",
    "Category:Basketball players from Massachusetts": "تصنيف:لاعبو كرة سلة من ماساتشوستس",
    "Category:Boxers from Massachusetts": "تصنيف:ملاكمون من ماساتشوستس",
    "Category:Female single skaters from Georgia (country)": "تصنيف:متزلجات فرديات من جورجيا",
    "Category:Golfers from Massachusetts": "تصنيف:لاعبو غولف من ماساتشوستس",
    "Category:Ice hockey people from Massachusetts": "تصنيف:أعلام هوكي جليد من ماساتشوستس",
    "Category:Immigrants to the United Kingdom from Aden": "تصنيف:مهاجرون إلى المملكة المتحدة من عدن",
    "Category:Kickboxers from Massachusetts": "تصنيف:مقاتلو كيك بوكسنغ من ماساتشوستس",
    "Category:Lacrosse players from Massachusetts": "تصنيف:لاعبو لاكروس من ماساتشوستس",
    "Category:Swimmers from Massachusetts": "تصنيف:سباحون من ماساتشوستس",
    "Category:Tennis people from Massachusetts": "تصنيف:أعلام كرة مضرب من ماساتشوستس",
    "Category:Track and field athletes from Massachusetts": "تصنيف:رياضيو المسار والميدان من ماساتشوستس",
}

to_test = [
    ("test_people_labels_1", data1),
    ("test_people_labels_2", data2),
    ("test_people_labels_3", data3),
]


@pytest.mark.parametrize("category, expected", data1.items(), ids=list(data1.keys()))
@pytest.mark.fast
def test_people_labels_1(category, expected) -> None:
    label = resolve_arabic_category_label(category)
    assert label.strip() == expected


@pytest.mark.parametrize("category, expected", data2.items(), ids=list(data2.keys()))
@pytest.mark.fast
def test_people_labels_2(category, expected) -> None:
    label = resolve_arabic_category_label(category)
    assert label.strip() == expected


@pytest.mark.parametrize("category, expected", data3.items(), ids=list(data3.keys()))
@pytest.mark.fast
def test_people_labels_3(category, expected) -> None:
    label = resolve_arabic_category_label(category)
    assert label.strip() == expected


@pytest.mark.parametrize("name,data", to_test)
@pytest.mark.slow
def test_peoples_2(name, data):

    expected, diff_result = one_dump_test(data, resolve_arabic_category_label)

    dump_diff(diff_result, name)
    assert diff_result == expected, f"Differences found: {len(diff_result)}"

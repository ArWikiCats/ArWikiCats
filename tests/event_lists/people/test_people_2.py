#
import pytest
from load_one_data import ye_test_one_dataset_new, dump_diff


def test_people_labels_2():
    data = {
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
    print(f"len of data: {len(data)}")
    expected, diff_result = ye_test_one_dataset_new(data)

    dump_diff(diff_result, "test_people_labels_2")
    assert diff_result == expected, f"Differences found: {len(diff_result)}"


def test_people_labels_from():
    data = {
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
    print(f"len of data: {len(data)}")
    expected, diff_result = ye_test_one_dataset_new(data)

    dump_diff(diff_result, "test_people_labels_from")
    assert diff_result == expected, f"Differences found: {len(diff_result)}"


@pytest.mark.slow
def test_people_labels_from_2():
    data = {
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
    print(f"len of data: {len(data)}")
    expected, diff_result = ye_test_one_dataset_new(data)

    dump_diff(diff_result, "test_people_labels_from_2")
    assert diff_result == expected, f"Differences found: {len(diff_result)}"

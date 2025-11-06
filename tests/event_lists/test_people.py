#
from src import new_func_lab_final_label
from load_one_data import ye_test_one_dataset, dump_diff

data = {
    "Category:Afghan diplomats": "تصنيف:دبلوماسيون أفغان",
    "Category:Ambassadors of Afghanistan": "تصنيف:سفراء أفغانستان",
    "Category:Ambassadors of the Ottoman Empire": "تصنيف:سفراء الدولة العثمانية",
    "Category:Ambassadors to the Ottoman Empire": "تصنيف:سفراء لدى الدولة العثمانية",
    "Category:American nuclear medicine physicians": "تصنيف:أطباء طب نووي أمريكيون",
    "Category:Argentine multi-instrumentalists": "تصنيف:عازفون على عدة آلات أرجنتينيون",
    "Category:Attacks on diplomatic missions": "تصنيف:هجمات على بعثات دبلوماسية",
    "Category:Australian Internet celebrities": "تصنيف:مشاهير إنترنت أستراليون",
    "Category:Canadian nuclear medicine physicians": "تصنيف:أطباء طب نووي كنديون",
    "Category:Croatian nuclear medicine physicians": "تصنيف:أطباء طب نووي كروات",
    "Category:Expatriate male actors in New Zealand": "تصنيف:ممثلون ذكور مغتربون في نيوزيلندا",
    "Category:Expatriate male actors": "تصنيف:ممثلون ذكور مغتربون",
    "Category:German nuclear medicine physicians": "تصنيف:أطباء طب نووي ألمان",
    "Category:Immigrants to New Zealand": "تصنيف:مهاجرون إلى نيوزيلندا",
    "Category:Immigration to New Zealand": "تصنيف:الهجرة إلى نيوزيلندا",
    "Category:Internees at the Sheberghan Prison": "تصنيف:معتقلين في سجن شيبرغان",
    "Category:Iranian nuclear medicine physicians": "تصنيف:أطباء طب نووي إيرانيون",
    "Category:Israeli people of Northern Ireland descent": "تصنيف:إسرائيليون من أصل أيرلندي شمالي",
    "Category:Italian defectors to the Soviet Union": "تصنيف:إيطاليون منشقون إلى الاتحاد السوفيتي",
    "Category:Ivorian American": "تصنيف:أمريكيون إيفواريون",
    "Category:Ivorian diaspora in Asia": "تصنيف:شتات إيفواري في آسيا",
    "Category:Medical doctors by specialty and nationality": "تصنيف:أطباء حسب التخصص والجنسية",
    "Category:Multi-instrumentalists": "تصنيف:عازفون على عدة آلات",
    "Category:People by nationality and status": "تصنيف:أشخاص حسب الجنسية والحالة",
    "Category:People executed by Afghanistan": "تصنيف:أشخاص أعدموا من قبل أفغانستان",
    "Category:People in arts occupations by nationality": "تصنيف:مهن أشخاص في الفنون حسب الجنسية",
    "Category:People of Ivorian descent": "تصنيف:أشخاص من أصل إيفواري",
    "Category:Polish women by occupation": "تصنيف:بولنديات حسب المهنة",
    "Category:Portuguese healthcare managers": "تصنيف:مدراء رعاية صحية برتغاليون",
    "Category:Prisoners and detainees of Afghanistan": "تصنيف:سجناء ومعتقلون في أفغانستان",
    "Category:Prisons in Afghanistan": "تصنيف:سجون في أفغانستان",
    "Category:Scholars by subfield": "تصنيف:دارسون حسب الحقل الفرعي",
    "Category:Women in business by nationality": "تصنيف:سيدات أعمال حسب الجنسية",
    "Category:women in business": "تصنيف:سيدات أعمال"
}


def test_people():
    print(f"len of data: {len(data)}")
    org, diff = ye_test_one_dataset(data, new_func_lab_final_label)

    dump_diff(diff, "test_people")
    assert diff == org, f"Differences found: {len(diff)}"


def test_people_2():
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
    org, diff = ye_test_one_dataset(data, new_func_lab_final_label)

    dump_diff(diff, "test_people")
    assert diff == org, f"Differences found: {len(diff)}"


def test_people_from():
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
        "Category:Swimmers from Massachusetts": "تصنيف:سباحون من ماساتشوستس",
        "Category:Tennis people from Massachusetts": "تصنيف:أعلام كرة مضرب من ماساتشوستس",
        "Category:Track and field athletes from Massachusetts": "تصنيف:رياضيو المسار والميدان من ماساتشوستس",
    }
    print(f"len of data: {len(data)}")
    org, diff = ye_test_one_dataset(data, new_func_lab_final_label)

    dump_diff(diff, "test_people")
    assert diff == org, f"Differences found: {len(diff)}"

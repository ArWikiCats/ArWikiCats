
import pytest
from load_one_data import dump_diff, dump_same_and_not_same, one_dump_test
from ArWikiCats import resolve_label_ar

test_data_0 = {
}

test_data_1 = {
    "12th-century Indian books": "كتب هندية القرن 12",
    "13th-century Roman Catholic archbishops in Ireland": "رؤساء أساقفة رومان كاثوليك في أيرلندا القرن 13",
    "14th-century lords of Monaco": "لوردات موناكو القرن 14",
    "1520s censuses": "تعداد السكان في عقد 1520",
    "15th-century executions": "إعدامات في القرن 15",
    "15th-century lords of Monaco": "لوردات موناكو القرن 15",
    "1630s science fiction works": "أعمال خيال علمي عقد 1630",
    "1650s controversies": "خلافات عقد 1650",
    "1650s floods": "فيضانات عقد 1650",
    "1650s mass shootings": "إطلاق نار عشوائي عقد 1650",
    "1650s murders": "جرائم قتل عقد 1650",
    "1650s science fiction works": "أعمال خيال علمي عقد 1650",
    "16th century music": "الموسيقى في القرن 16",
    "16th century theatre": "المسرح في القرن 16",
    "16th-century lords of Monaco": "لوردات موناكو القرن 16",
    "17th century music": "الموسيقى في القرن 17",
    "17th century theatre": "المسرح في القرن 17",
    "17th-century cookbooks": "كتب طبخ القرن 17",
    "17th-century lords of Monaco": "لوردات موناكو القرن 17",
    "1830s alabama": "ألاباما عقد 1830",
    "1830s arkansas": "أركنساس عقد 1830",
    "1830s connecticut": "كونيتيكت عقد 1830",
    "1830s delaware": "ديلاوير عقد 1830",
    "1830s georgia (u.s. state)": "ولاية جورجيا عقد 1830",
    "1830s indiana": "إنديانا عقد 1830",
    "1830s iowa territory": "إقليم آيوا عقد 1830",
    "1830s iowa": "آيوا عقد 1830",
    "1830s kentucky": "كنتاكي عقد 1830",
    "1830s louisiana": "لويزيانا عقد 1830",
    "1830s maine": "مين عقد 1830",
    "1830s maryland": "ماريلند عقد 1830",
    "1830s massachusetts": "ماساتشوستس عقد 1830",
    "1830s michigan": "ميشيغان عقد 1830",
    "1830s minnesota territory": "إقليم منيسوتا عقد 1830",
    "1830s mississippi territory": "إقليم مسيسيبي عقد 1830",
    "1830s mississippi": "مسيسيبي عقد 1830",
    "1830s missouri": "ميزوري عقد 1830",
    "1830s new hampshire": "نيوهامشير عقد 1830",
    "1830s new jersey": "نيوجيرسي عقد 1830",
    "1830s new york (state)": "ولاية نيويورك عقد 1830",
    "1830s north carolina": "كارولاينا الشمالية عقد 1830",
    "1830s ohio": "أوهايو عقد 1830",
    "1830s pennsylvania": "بنسلفانيا عقد 1830",
    "1830s rhode island": "رود آيلاند عقد 1830",
    "1830s south carolina": "كارولاينا الجنوبية عقد 1830",
    "1830s tennessee": "تينيسي عقد 1830",
    "1830s vermont": "فيرمونت عقد 1830",
    "1830s virginia": "فرجينيا عقد 1830",
    "1830s wisconsin territory": "إقليم ويسكونسن عقد 1830",
    "1830s wisconsin": "ويسكونسن عقد 1830",
    "1910s musicals": "مسرحيات غنائية عقد 1910",
    "1910s racehorse deaths": "خيول سباق نفقت في عقد 1910",
    "1914 mining disasters": "كوارث التعدين 1914",
    "1950s Scottish television series debuts": "مسلسلات تلفزيونية إسكتلندية بدأ عرضها في عقد 1950",
    "1970s albums": "ألبومات عقد 1970",
    "1980s Christmas albums": "ألبومات عيد الميلاد عقد 1980",
    "1990s landslides": "انهيارات أرضية عقد 1990",
    "19th-century executions by Spain": "إعدامات في إسبانيا في القرن 19",
    "19th-century publications": "منشورات القرن 19",
    "1st-century BC Kings of Bithynia": "ملوك بيثينيا القرن 1 ق م",
    "1st-millennium literature": "أدب الألفية 1",
    "2000s Singaporean television series debuts": "مسلسلات تلفزيونية سنغافورية بدأ عرضها في عقد 2000",
    "2020s revolutions": "ثورات عقد 2020",
    "2020s Taiwanese television series debuts": "مسلسلات تلفزيونية تايوانية بدأ عرضها في عقد 2020",
    "2020s transport disasters": "كوارث نقل في عقد 2020",
    "20th century bc kings of": "ملوك القرن 20 ق م",
    "20th century bce kings of": "ملوك القرن 20 ق م",
    "20th century heads of": "قادة القرن 20",
    "20th century kings of": "ملوك القرن 20",
    "20th century mayors of": "عمدات القرن 20",
    "20th century members of": "أعضاء القرن 20",
    "20th century military history of": "التاريخ العسكري في القرن 20",
    "20th century presidents of": "رؤساء القرن 20",
    "20th century prime ministers of": "رؤساء وزراء القرن 20",
    "20th century princesses of": "أميرات القرن 20",
    "20th century religious buildings": "مبان دينية القرن 20",
    "20th century roman catholic church buildings": "مبان كنائس رومانية كاثوليكية القرن 20",
    "20th century sultans of": "سلاطين القرن 20",
    "20th-century executions by Gambia": "إعدامات في غامبيا في القرن 20",
    "20th-century Ghanaian literature": "أدب غاني القرن 20",
    "20th-century House of Habsburg": "آل هابسبورغ القرن 20",
    "20th-century Islamic terrorist incidents": "حوادث إرهابية منسوبة للمسلمين القرن 20",
    "20th-century men from Northern Ireland": "رجال من أيرلندا الشمالية في القرن 20",
    "20th-century Mexican literature": "أدب مكسيكي القرن 20",
    "20th-century railway accidents": "حوادث سكك حديد في القرن 20",
    "20th-century Taiwanese literature": "أدب تايواني القرن 20",
    "20th-century Ukrainian literature": "أدب أوكراني القرن 20",
    "20th-century Zimbabwean literature": "أدب زيمبابوي القرن 20",
    "21st-century executions by Alabama": "إعدامات في ألاباما في القرن 21",
    "21st-century executions by Somalia": "إعدامات في الصومال في القرن 21",
    "21st-century Ghanaian literature": "أدب غاني القرن 21",
    "21st-century Islamic terrorist incidents": "حوادث إرهابية منسوبة للمسلمين القرن 21",
    "21st-century men from Northern Ireland": "رجال من أيرلندا الشمالية في القرن 21",
    "21st-century military alliances": "تحالفات عسكرية في القرن 21",
    "21st-century Moroccan literature": "أدب مغربي القرن 21",
    "21st-century mosques": "مساجد القرن 21",
    "21st-century Taiwanese literature": "أدب تايواني القرن 21",
    "21st-century terrorist incidents in Denmark": "حوادث إرهابية في الدنمارك القرن 21",
    "21st-century Ukrainian literature": "أدب أوكراني القرن 21",
    "21st-century Zimbabwean literature": "أدب زيمبابوي القرن 21",
    "2nd-millennium texts": "نصوص الألفية 2",
    "5th-century BC kings of Tyre": "ملوك صور القرن 5 ق م",
    "8th-century executions by Umayyad Caliphate": "إعدامات في الدولة الأموية في القرن 8",
    "Deaths by drone strikes": "وفيات بواسطة هجمات الطائرات بدون طيار",
    "Qualification for 1968 Summer Olympics": "تصفيات مؤهلة إلى الألعاب الأولمبية الصيفية 1968",
    "Qualification for the 2026 Winter Olympics": "تصفيات مؤهلة إلى الألعاب الأولمبية الشتوية 2026",
    "Works by musicians from Northern Ireland": "أعمال موسيقيون من أيرلندا الشمالية",
}


@pytest.mark.parametrize("category, expected", test_data_0.items(), ids=test_data_0.keys())
@pytest.mark.fast
def test_mk3_skips_test_data_0(category: str, expected: str) -> None:
    label = resolve_label_ar(category)
    assert label == expected


@pytest.mark.parametrize("category, expected", test_data_1.items(), ids=test_data_1.keys())
@pytest.mark.fast
def test_mk3_skips_test_data_1(category: str, expected: str) -> None:
    label = resolve_label_ar(category)
    assert label == expected


to_test = [
    ("test_mk3_skips_test_data_1", test_data_1),
]


@pytest.mark.parametrize("name,data", to_test)
@pytest.mark.dump
def test_peoples(name: str, data: dict[str, str]) -> None:
    expected, diff_result = one_dump_test(data, resolve_label_ar)

    dump_diff(diff_result, name)
    # dump_same_and_not_same(data, expected, name)
    assert diff_result == expected, f"Differences found: {len(diff_result):,}, len all :{len(data):,}"

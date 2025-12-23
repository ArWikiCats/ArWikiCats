#
import pytest
from load_one_data import dump_diff, one_dump_test, dump_diff_text

from ArWikiCats import resolve_arabic_category_label

data_empty = {
    "Category:Academic staff of Incheon National University": "تصنيف:أعضاء هيئة تدريس جامعة إنتشون الوطنية",
    "Category:Lists of 1900s films": "تصنيف:قوائم أفلام إنتاج عقد 1900",
    "Category:Academic staff of University of Galați": "تصنيف:أعضاء هيئة تدريس جامعة غالاتس",
    "Category:Women members of Senate of Spain": "تصنيف:عضوات مجلس شيوخ إسبانيا",
    "Category:Defunct shopping malls in Malaysia": "تصنيف:مراكز تسوق سابقة في ماليزيا",
    "Category:Defunct communist parties in Nepal": "تصنيف:أحزاب شيوعية سابقة في نيبال",
    "Category:Defunct European restaurants in London": "تصنيف:مطاعم أوروبية سابقة في لندن",
    "Category:Burial sites of Aragonese royal houses": "",
    "Category:Burial sites of Castilian royal houses": "",
    "Category:Burial sites of Frankish noble families": "",
    "Category:Burial sites of Georgian royal dynasties": "",
    "Category:Burial sites of Hawaiian royal houses": "",
    "Category:Burial sites of Hessian noble families": "",
    "Category:Burial sites of Kotromanić dynasty": "",
    "Category:Burial sites of Leonese royal houses": "",
    "Category:Burial sites of Lorraine noble families": "",
    "Category:Burial sites of Lower Saxon noble families": "",
    "Category:Burial sites of Muslim dynasties": "",
    "Category:Burial sites of Navarrese royal houses": "",
    "Category:Burial sites of Neapolitan royal houses": "",
    "Category:Burial sites of noble families": "",
    "Category:Burial sites of Norman families": ""
}

data0 = {
    "Category:Lists of American reality television series episodes": "تصنيف:قوائم حلقات مسلسلات تلفزيونية واقعية أمريكية",
    "Category:Academic staff of University of Nigeria": "تصنيف:أعضاء هيئة تدريس جامعة نيجيريا",
    "Category:Early modern history of Portugal": "تصنيف:تاريخ البرتغال الحديث المبكر",
}

data1 = {
    "south american second tier football leagues": "تصنيف:دوريات كرة قدم أمريكية جنوبية من الدرجة الثانية",
    "european second tier basketball leagues": "تصنيف:دوريات كرة سلة أوروبية من الدرجة الثانية",
    "european second tier ice hockey leagues": "تصنيف:دوريات هوكي جليد أوروبية من الدرجة الثانية",
    "israeli basketball premier league": "تصنيف:الدوري الإسرائيلي الممتاز لكرة السلة",

    "Category:Burial sites of ancient Irish dynasties": "تصنيف:مواقع دفن أسر أيرلندية قديمة",
    "Category:Burial sites of Arab dynasties": "تصنيف:مواقع دفن أسر عربية",
    "Category:Burial sites of Asian royal families": "تصنيف:مواقع دفن عائلات ملكية آسيوية",
    "Category:Burial sites of Austrian noble families": "تصنيف:مواقع دفن عائلات نبيلة نمساوية",
    "Category:Burial sites of Belgian noble families": "تصنيف:مواقع دفن عائلات نبيلة بلجيكية",
    "Category:Burial sites of Bohemian royal houses": "تصنيف:مواقع دفن بيوت ملكية بوهيمية",
    "Category:Burial sites of Bosnian noble families": "تصنيف:مواقع دفن عائلات نبيلة بوسنية",
    "Category:Burial sites of British royal houses": "تصنيف:مواقع دفن بيوت ملكية بريطانية",
    "Category:Burial sites of Bulgarian royal houses": "تصنيف:مواقع دفن بيوت ملكية بلغارية",
    "Category:Burial sites of Byzantine imperial dynasties": "تصنيف:مواقع دفن أسر إمبراطورية بيزنطية",
    "Category:Burial sites of Cornish families": "تصنيف:مواقع دفن عائلات كورنية",
    "Category:Burial sites of Danish noble families": "تصنيف:مواقع دفن عائلات نبيلة دنماركية",
    "Category:Burial sites of Dutch noble families": "تصنيف:مواقع دفن عائلات نبيلة هولندية",
    "Category:Burial sites of English families": "تصنيف:مواقع دفن عائلات إنجليزية",
    "Category:Burial sites of English royal houses": "تصنيف:مواقع دفن بيوت ملكية إنجليزية",
    "Category:Burial sites of European noble families": "تصنيف:مواقع دفن عائلات نبيلة أوروبية",
    "Category:Burial sites of European royal families": "تصنيف:مواقع دفن عائلات ملكية أوروبية",
    "Category:Burial sites of French noble families": "تصنيف:مواقع دفن عائلات نبيلة فرنسية",
    "Category:Burial sites of French royal families": "تصنيف:مواقع دفن عائلات ملكية فرنسية",
    "Category:Burial sites of German noble families": "تصنيف:مواقع دفن عائلات نبيلة ألمانية",
    "Category:Burial sites of German royal houses": "تصنيف:مواقع دفن بيوت ملكية ألمانية",
    "Category:Burial sites of Hungarian noble families": "تصنيف:مواقع دفن عائلات نبيلة مجرية",
    "Category:Burial sites of Hungarian royal houses": "تصنيف:مواقع دفن بيوت ملكية مجرية",
    "Category:Burial sites of Iranian dynasties": "تصنيف:مواقع دفن أسر إيرانية",
    "Category:Burial sites of Irish noble families": "تصنيف:مواقع دفن عائلات نبيلة أيرلندية",
    "Category:Burial sites of Irish royal families": "تصنيف:مواقع دفن عائلات ملكية أيرلندية",
    "Category:Burial sites of Italian noble families": "تصنيف:مواقع دفن عائلات نبيلة إيطالية",
    "Category:Burial sites of Italian royal houses": "تصنيف:مواقع دفن بيوت ملكية إيطالية",
    "Category:Burial sites of Lithuanian noble families": "تصنيف:مواقع دفن عائلات نبيلة ليتوانية",
    "Category:Burial sites of Luxembourgian noble families": "تصنيف:مواقع دفن عائلات نبيلة لوكسمبورغية",
    "Category:Burial sites of Mexican noble families": "تصنيف:مواقع دفن عائلات نبيلة مكسيكية",
    "Category:Burial sites of Middle Eastern royal families": "تصنيف:مواقع دفن عائلات ملكية شرقية أوسطية",
    "Category:Burial sites of Polish noble families": "تصنيف:مواقع دفن عائلات نبيلة بولندية",
    "Category:Burial sites of Polish royal houses": "تصنيف:مواقع دفن بيوت ملكية بولندية",
    "Category:Burial sites of Romanian noble families": "تصنيف:مواقع دفن عائلات نبيلة رومانية",
    "Category:Burial sites of Romanian royal houses": "تصنيف:مواقع دفن بيوت ملكية رومانية",
    "Category:Burial sites of imperial Chinese families": "تصنيف:مواقع دفن أسر إمبراطورية صينية",
}
data_2 = {
}

data_3 = {
}

to_test = [
    ("test_5_data_0", data0),
    ("test_5_data_1", data1),
    ("test_5_data_3", data_3),
]


@pytest.mark.parametrize("category, expected", data0.items(), ids=data0.keys())
def test_5_data_0(category: str, expected: str) -> None:
    assert resolve_arabic_category_label(category) == expected


@pytest.mark.parametrize("category, expected", data1.items(), ids=data1.keys())
def test_5_data_1(category: str, expected: str) -> None:
    assert resolve_arabic_category_label(category) == expected


@pytest.mark.parametrize("category, expected", data_3.items(), ids=data_3.keys())
def test_5_data_3(category: str, expected: str) -> None:
    assert resolve_arabic_category_label(category) == expected


@pytest.mark.parametrize("name,data", to_test)
@pytest.mark.dump
def test_dump_it(name: str, data: dict[str, str]) -> None:
    expected, diff_result = one_dump_test(data, resolve_arabic_category_label)
    dump_diff(diff_result, name)

    # dump_diff_text(expected, diff_result, name)
    assert diff_result == expected, f"Differences found: {len(diff_result):,}, len all :{len(data):,}"

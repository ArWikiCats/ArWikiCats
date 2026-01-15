#
import pytest
from load_one_data import dump_diff, dump_diff_text, one_dump_test

from ArWikiCats import resolve_arabic_category_label

data_empty = {
    "lists of 20th millennium women's olympic table tennis players films by city": "قوائم أفلام لاعبات كرة طاولة أولمبيات الألفية 20 حسب المدينة",
    "category:2020 women's wheelchair tennis players by city": "تصنيف:لاعبات كرة مضرب على كراسي متحركة نسائية في 2020 حسب المدينة",
    "Category:2020 wheelchair tennis by city": "تصنيف:كرة المضرب على الكراسي المتحركة في 2020 حسب المدينة",
    "Category:Political positions of the 2000 United States presidential candidates": "تصنيف:مواقف سياسية لمرشحي الرئاسة الأمريكية 2000",
    "Category:Political positions of the 2008 United States presidential candidates": "تصنيف:مواقف سياسية لمرشحي الرئاسة الأمريكية 2008",
    "Category:Political positions of the 2016 United States presidential candidates": "تصنيف:مواقف سياسية لمرشحي الرئاسة الأمريكية 2016",
    "Category:Political positions of the 2020 United States presidential candidates": "تصنيف:مواقف سياسية لمرشحي الرئاسة الأمريكية 2020",
    "Category:Political positions of the 2024 United States presidential candidates": "تصنيف:مواقف سياسية لمرشحي الرئاسة الأمريكية 2024",
    "Category:17th-century dukes of Limburg": "تصنيف:دوقات ليمبورغ في القرن 17",
    "Category:Politics and technology": "تصنيف:السياسة والتقانة",
    "Category:National association football second-tier league champions": "x",
    "Category:Association football third-tier league seasons": "x",
    "Category:Association football second-tier league seasons": "x",
    "Category:Association football fourth-tier league seasons": "x",
    "Category:National association football third-tier leagues": "x",
    "Category:National association football fifth-tier leagues": "x",
    "Category:National association football fourth-tier leagues": "x",
    "Category:National association football second-tier leagues": "x",
    "Category:National association football seventh-tier leagues": "x",
    "Category:National association football sixth-tier leagues": "x",
    "Category:Seasons in European third-tier association football leagues": "x",
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
    "Category:Burial sites of Norman families": "",
}

data0 = {
    "Category:chess composers": "تصنيف:مؤلفو مسائل شطرنج",
    "Category:cultural depictions of Canadian activists": "تصنيف:تصوير ثقافي عن ناشطون كنديون",
    "Category:Assassinated Canadian activists": "تصنيف:ناشطون كنديون مغتالون",
    "Category:Assassinated Guatemalan diplomats": "تصنيف:دبلوماسيون غواتيماليون مغتالون",
    "Category:Assassinated Swedish diplomats": "تصنيف:دبلوماسيون سويديون مغتالون",
    "Category:Ancient Indian people by occupation": "تصنيف:هنود قدماء حسب المهنة",
    "Category:Fictional Australian criminals": "تصنيف:مجرمون أستراليون خياليون",
    "Category:Assassinated Peruvian politicians": "تصنيف:سياسيون بيرويون مغتالون",
    # "Category:Native American women leaders": "تصنيف:قائدات أمريكيات أصليون",
    "yemeni national junior women's under-16 football teams players": "تصنيف:لاعبات منتخبات كرة قدم وطنية يمنية تحت 16 سنة للناشئات",
    "yemeni national junior women's football teams players": "تصنيف:لاعبات منتخبات كرة قدم وطنية يمنية للناشئات",
    "yemeni national women's under-16 football teams players": "تصنيف:لاعبات منتخبات كرة قدم وطنية يمنية تحت 16 سنة للسيدات",
    "yemeni national youth women's under-16 football teams players": "تصنيف:لاعبات منتخبات كرة قدم وطنية يمنية تحت 16 سنة للشابات",
    "yemeni national youth women's football teams players": "تصنيف:لاعبات منتخبات كرة قدم وطنية يمنية للشابات",
    "Category:zaïrean wheelchair sports federation": "تصنيف:الاتحاد الزائيري للرياضة على الكراسي المتحركة",
    "Category:surinamese sports federation": "تصنيف:الاتحاد السورينامي للرياضة",
    "Category:Romania football manager history navigational boxes": "تصنيف:صناديق تصفح تاريخ مدربو كرة قدم رومانيا",
    "Category:Jewish football clubs": "تصنيف:أندية كرة القدم اليهودية",
    "Category:Jewish sports": "تصنيف:ألعاب رياضية يهودية",
    "Category:European League of Football coaches": "تصنيف:مدربو الدوري الأوروبي لكرة القدم",
    "Category:Australian soccer by year": "تصنيف:كرة القدم الأسترالية حسب السنة",
    "Category:Political positions of United States presidential candidates": "تصنيف:مواقف سياسية لمرشحي الرئاسة الأمريكية",
}

data1 = {
    "Category:Lists of American reality television series episodes": "تصنيف:قوائم حلقات مسلسلات تلفزيونية واقعية أمريكية",
    "Category:Academic staff of University of Nigeria": "تصنيف:أعضاء هيئة تدريس جامعة نيجيريا",
    "Category:Early modern history of Portugal": "تصنيف:تاريخ البرتغال الحديث المبكر",
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

data_2 = {}

data_3 = {
    "1550 in asian women's football": "تصنيف:كرة قدم آسيوية للسيدات في 1550",
    "1520 in south american women's football": "تصنيف:كرة قدم أمريكية جنوبية للسيدات في 1520",
    "canadian women's ice hockey by league": "تصنيف:هوكي جليد كندية للسيدات حسب الدوري",
    "european women's football by country": "تصنيف:كرة قدم أوروبية للسيدات حسب البلد",
    "south american women's football": "تصنيف:كرة قدم أمريكية جنوبية للسيدات",
    "1789 in south american women's football": "تصنيف:كرة قدم أمريكية جنوبية للسيدات في 1789",
    "european national men's field hockey teams": "تصنيف:منتخبات هوكي ميدان وطنية أوروبية للرجال",
    "northern ireland national men's football teams": "تصنيف:منتخبات كرة قدم وطنية أيرلندية شمالية للرجال",
}

to_test = [
    ("test_5_data_0", data0),
    # ("test_5_data_1", data1),
    # ("test_5_data_3", data_3),
]


@pytest.mark.parametrize("category, expected", data0.items(), ids=data0.keys())
def test_5_data_0(category: str, expected: str) -> None:
    """
    pytest tests/event_lists/importants/test_5_important.py::test_5_data_0
    """
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

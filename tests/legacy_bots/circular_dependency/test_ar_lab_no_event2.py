"""
Tests
"""

import pytest
from load_one_data import dump_diff

from ArWikiCats import resolve_label_ar
from ArWikiCats.fix import fixtitle
from ArWikiCats.legacy_bots.resolvers.arabic_label_builder import find_ar_label
from ArWikiCats.legacy_bots.resolvers.separator_based_resolver import work_separator_names
from ArWikiCats.legacy_bots.resolvers.sub_resolver import sub_translate_general_category


def translate_general_category_wrap(category: str) -> str:
    arlabel = "" or sub_translate_general_category(category) or work_separator_names(category)
    if arlabel:
        arlabel = fixtitle.fixlabel(arlabel, en=category)

    return arlabel


fast_data_list = [
    {
        "separator": " in ",
        "category": "1450s disestablishments in arizona territory",
        "output": "انحلالات عقد 1450 في إقليم أريزونا",
    },
    {
        "separator": " in ",
        "category": "1450s disestablishments in the papal states",
        "output": "انحلالات عقد 1450 في الدولة البابوية",
    },
    {"separator": " in ", "category": "1450s crimes in california", "output": "جرائم عقد 1450 في كاليفورنيا"},
    {"separator": " in ", "category": "1450s crimes in asia", "output": "جرائم عقد 1450 في آسيا"},
    {"separator": " in ", "category": "1450s establishments in england", "output": "تأسيسات عقد 1450 في إنجلترا"},
    {"separator": " in ", "category": "may 1450 crimes in asia", "output": "جرائم مايو 1450 في آسيا"},
]

data_list_1 = {
    "13th century philosophers by nationality": "فلاسفة في القرن 13 حسب الجنسية",
    "1450s architecture in the united states": "عمارة عقد 1450 في الولايات المتحدة",
    "1450s crimes in asia": "جرائم عقد 1450 في آسيا",
    "1450s crimes in california": "جرائم عقد 1450 في كاليفورنيا",
    "1450s crimes in germany": "جرائم عقد 1450 في ألمانيا",
    "1450s crimes in hong kong": "جرائم عقد 1450 في هونغ كونغ",
    "1450s crimes in peshawar": "جرائم عقد 1450 في بيشاور",
    "1450s disasters in ireland": "كوارث عقد 1450 في أيرلندا",
    "1450s disestablishments by continent": "انحلالات عقد 1450 حسب القارة",
    "1450s disestablishments in africa": "انحلالات عقد 1450 في إفريقيا",
    "1450s disestablishments in arizona territory": "انحلالات عقد 1450 في إقليم أريزونا",
    "1450s disestablishments in british columbia": "انحلالات عقد 1450 في كولومبيا البريطانية",
    "1450s disestablishments in canada": "انحلالات عقد 1450 في كندا",
    "1450s disestablishments in cape verde": "انحلالات عقد 1450 في الرأس الأخضر",
    "1450s disestablishments in france": "انحلالات عقد 1450 في فرنسا",
    "1450s disestablishments in georgia (country)": "انحلالات عقد 1450 في جورجيا",
    "1450s disestablishments in hawaii": "انحلالات عقد 1450 في هاواي",
    "1450s disestablishments in idaho": "انحلالات عقد 1450 في أيداهو",
    "1450s disestablishments in minnesota": "انحلالات عقد 1450 في منيسوتا",
    "1450s disestablishments in nauru": "انحلالات عقد 1450 في ناورو",
    "1450s disestablishments in nebraska": "انحلالات عقد 1450 في نبراسكا",
    "1450s disestablishments in oceania": "انحلالات عقد 1450 في أوقيانوسيا",
    "1450s disestablishments in oklahoma": "انحلالات عقد 1450 في أوكلاهوما",
    "1450s disestablishments in rhode island": "انحلالات عقد 1450 في رود آيلاند",
    "1450s disestablishments in south america": "انحلالات عقد 1450 في أمريكا الجنوبية",
    "1450s disestablishments in taiwan": "انحلالات عقد 1450 في تايوان",
    "1450s disestablishments in the british empire": "انحلالات عقد 1450 في الإمبراطورية البريطانية",
    "1450s disestablishments in the netherlands": "انحلالات عقد 1450 في هولندا",
    "1450s disestablishments in the papal states": "انحلالات عقد 1450 في الدولة البابوية",
    "1450s disestablishments in tunisia": "انحلالات عقد 1450 في تونس",
    "1450s disestablishments in vermont": "انحلالات عقد 1450 في فيرمونت",
    "1450s disestablishments in west virginia": "انحلالات عقد 1450 في فرجينيا الغربية",
    "1450s establishments by country": "تأسيسات عقد 1450 حسب البلد",
    "1450s establishments in armenia": "تأسيسات عقد 1450 في أرمينيا",
    "1450s establishments in asia": "تأسيسات عقد 1450 في آسيا",
    "1450s establishments in bavaria": "تأسيسات عقد 1450 في بافاريا",
    "1450s establishments in burkina faso": "تأسيسات عقد 1450 في بوركينا فاسو",
    "1450s establishments in burma": "تأسيسات عقد 1450 في بورما",
    "1450s establishments in colorado": "تأسيسات عقد 1450 في كولورادو",
    "1450s establishments in england": "تأسيسات عقد 1450 في إنجلترا",
    "1450s establishments in france": "تأسيسات عقد 1450 في فرنسا",
    "1450s establishments in georgia (u.s. state)": "تأسيسات عقد 1450 في ولاية جورجيا",
    "1450s establishments in germany": "تأسيسات عقد 1450 في ألمانيا",
    "1450s establishments in greenland": "تأسيسات عقد 1450 في جرينلاند",
    "1450s establishments in grenada": "تأسيسات عقد 1450 في غرينادا",
    "1450s establishments in indonesia": "تأسيسات عقد 1450 في إندونيسيا",
    "1450s establishments in italy": "تأسيسات عقد 1450 في إيطاليا",
    "1450s establishments in kentucky": "تأسيسات عقد 1450 في كنتاكي",
    "1450s establishments in kiribati": "تأسيسات عقد 1450 في كيريباتي",
    "1450s establishments in malaysia": "تأسيسات عقد 1450 في ماليزيا",
    "1450s establishments in mali": "تأسيسات عقد 1450 في مالي",
    "1450s establishments in malta": "تأسيسات عقد 1450 في مالطا",
    "1450s establishments in meghalaya": "تأسيسات عقد 1450 في ميغالايا",
    "1450s establishments in montenegro": "تأسيسات عقد 1450 في الجبل الأسود",
    "1450s establishments in saint vincent and grenadines": "تأسيسات عقد 1450 في سانت فنسنت وجزر غرينادين",
    "1450s establishments in saskatchewan": "تأسيسات عقد 1450 في ساسكاتشوان",
    "1450s establishments in shanghai": "تأسيسات عقد 1450 في شانغهاي",
    "1450s establishments in sikkim": "تأسيسات عقد 1450 في سيكيم",
    "1450s establishments in slovenia": "تأسيسات عقد 1450 في سلوفينيا",
    "1450s establishments in south africa": "تأسيسات عقد 1450 في جنوب إفريقيا",
    "1450s establishments in south america": "تأسيسات عقد 1450 في أمريكا الجنوبية",
    "1450s establishments in taiwan": "تأسيسات عقد 1450 في تايوان",
    "1450s establishments in the community of madrid": "تأسيسات عقد 1450 في منطقة مدريد",
    "1450s establishments in the french colonial empire": "تأسيسات عقد 1450 في الإمبراطورية الاستعمارية الفرنسية",
    "1450s establishments in the holy roman empire": "تأسيسات عقد 1450 في الإمبراطورية الرومانية المقدسة",
    "1450s establishments in the united kingdom": "تأسيسات عقد 1450 في المملكة المتحدة",
    "1450s establishments in uttar pradesh": "تأسيسات عقد 1450 في أتر برديش",
    "1450s establishments in west virginia": "تأسيسات عقد 1450 في فرجينيا الغربية",
    "14th century establishments in bohemia": "تأسيسات القرن 14 في بوهيميا",
    "15th century establishments in poland": "تأسيسات القرن 15 في بولندا",
    "16th century architecture in romania": "عمارة القرن 16 في رومانيا",
    "17th century disestablishments in ireland": "انحلالات القرن 17 في أيرلندا",
    "17th century disestablishments in sri lanka": "انحلالات القرن 17 في سريلانكا",
    "17th century disestablishments in the dutch empire": "انحلالات القرن 17 في الإمبراطورية الهولندية",
    "19th century establishments in kingdom-of hanover": "تأسيسات القرن 19 في مملكة هانوفر",
    "19th century establishments in kingdom-of sicily": "تأسيسات القرن 19 في مملكة صقلية",
    "19th century establishments in nepal": "تأسيسات القرن 19 في نيبال",
    "19th century establishments in yukon": "تأسيسات القرن 19 في يوكون",
    "19th century male composers by nationality": "ملحنون ذكور في القرن 19 حسب الجنسية",
    "1st millennium bc establishments in the roman empire": "تأسيسات الألفية 1 ق م في الإمبراطورية الرومانية",
    "1st millennium establishments in morocco": "تأسيسات الألفية 1 في المغرب",
    "20th century chemists by nationality": "كيميائيون في القرن 20 حسب الجنسية",
    "20th century crimes in slovenia": "جرائم القرن 20 في سلوفينيا",
    "20th century disestablishments in alberta": "انحلالات القرن 20 في ألبرتا",
    "20th century governors of ottoman empire": "حكام في القرن 20 في الدولة العثمانية",
    "21st century crimes in croatia": "جرائم القرن 21 في كرواتيا",
    "21st century disestablishments in korea": "انحلالات القرن 21 في كوريا",
    "21st century disestablishments in south dakota": "انحلالات القرن 21 في داكوتا الجنوبية",
    "21st century disestablishments in wales": "انحلالات القرن 21 في ويلز",
    "21st century establishments in kosovo": "تأسيسات القرن 21 في كوسوفو",
    "2nd millennium disestablishments in hawaii": "انحلالات الألفية 2 في هاواي",
    "2nd millennium disestablishments in india": "انحلالات الألفية 2 في الهند",
    "2nd millennium disestablishments in prince edward island": "انحلالات الألفية 2 في جزيرة الأمير إدوارد",
    "2nd millennium establishments in arkansas": "تأسيسات الألفية 2 في أركنساس",
    "2nd millennium establishments in el salvador": "تأسيسات الألفية 2 في السلفادور",
    "2nd millennium establishments in lebanon": "تأسيسات الألفية 2 في لبنان",
    "2nd millennium establishments in massachusetts": "تأسيسات الألفية 2 في ماساتشوستس",
    "2nd millennium establishments in morocco": "تأسيسات الألفية 2 في المغرب",
    "2nd millennium establishments in thailand": "تأسيسات الألفية 2 في تايلاند",
    "3rd century bishops in germania": "أساقفة في القرن 3 في جرمانية",
    "3rd millennium establishments in british overseas territories": "تأسيسات الألفية 3 في أقاليم ما وراء البحار البريطانية",
    "3rd millennium establishments in south korea": "تأسيسات الألفية 3 في كوريا الجنوبية",
    "450s disestablishments in the roman empire": "انحلالات عقد 450 في الإمبراطورية الرومانية",
    "5th century bc establishments by country": "تأسيسات القرن 5 ق م حسب البلد",
    "5th century disestablishments in the byzantine empire": "انحلالات القرن 5 في الإمبراطورية البيزنطية",
    "60s establishments in the roman empire": "تأسيسات عقد 60 في الإمبراطورية الرومانية",
    "6th century disestablishments in the byzantine empire": "انحلالات القرن 6 في الإمبراطورية البيزنطية",
    "april 1450 crimes in asia": "جرائم أبريل 1450 في آسيا",
    "august 1450 crimes in asia": "جرائم أغسطس 1450 في آسيا",
    "april 1450 crimes in south america": "جرائم أبريل 1450 في أمريكا الجنوبية",
    "february 1450 crimes in asia": "جرائم فبراير 1450 في آسيا",
    "february 1450 crimes in europe": "جرائم فبراير 1450 في أوروبا",
    "december 1450 crimes in europe": "جرائم ديسمبر 1450 في أوروبا",
    "february 1450 crimes in south america": "جرائم فبراير 1450 في أمريكا الجنوبية",
    "september 1450 crimes in africa": "جرائم سبتمبر 1450 في إفريقيا",
    "september 1450 crimes in asia": "جرائم سبتمبر 1450 في آسيا",
    "september 1450 crimes in europe": "جرائم سبتمبر 1450 في أوروبا",
    "october 1450 crimes in north america": "جرائم أكتوبر 1450 في أمريكا الشمالية",
    "may 1450 crimes in asia": "جرائم مايو 1450 في آسيا",
    "may 1450 crimes in europe": "جرائم مايو 1450 في أوروبا",
    "june 1450 crimes in the united states": "جرائم يونيو 1450 في الولايات المتحدة",
    "july 1450 crimes in north america": "جرائم يوليو 1450 في أمريكا الشمالية",
    "january 1450 crimes in north america": "جرائم يناير 1450 في أمريكا الشمالية",
}


@pytest.mark.parametrize("category, expected", data_list_1.items(), ids=data_list_1.keys())
@pytest.mark.fast
def test_1(category: str, expected: str) -> None:
    label = resolve_label_ar(category)
    assert label == expected


@pytest.mark.parametrize("tab", fast_data_list, ids=lambda x: x["category"])
@pytest.mark.fast
def test_translate_general_category_event2_fast(tab) -> None:
    label = translate_general_category_wrap(tab["category"])
    # ---
    assert label == tab["output"]


data_list_bad = [
    ("1550s disestablishments in yugoslavia", " in ", "انحلالات عقد 1550 في يوغسلافيا"),
    ("20th century disestablishments in the united kingdom", " in ", "انحلالات القرن 20 في المملكة المتحدة"),
    ("1550s establishments in wisconsin", " in ", "تأسيسات عقد 1550 في ويسكونسن"),
    ("20th century disestablishments in sri lanka", " in ", "انحلالات القرن 20 في سريلانكا"),
    ("3rd millennium disestablishments in england", " in ", "انحلالات الألفية 3 في إنجلترا"),
    ("1550s crimes in pakistan", " in ", "جرائم عقد 1550 في باكستان"),
    ("2nd millennium establishments in rhode island", " in ", "تأسيسات الألفية 2 في رود آيلاند"),
    ("1550s establishments in chile", " in ", "تأسيسات عقد 1550 في تشيلي"),
    ("1550s disestablishments in southeast asia", " in ", "انحلالات عقد 1550 في جنوب شرق آسيا"),
    ("1550s establishments in jamaica", " in ", "تأسيسات عقد 1550 في جامايكا"),
    ("20th century disasters in afghanistan", " in ", "كوارث القرن 20 في أفغانستان"),
    ("1550s disestablishments in mississippi", " in ", "انحلالات عقد 1550 في مسيسيبي"),
    ("1550s establishments in maine", " in ", "تأسيسات عقد 1550 في مين"),
    ("1550s establishments in sweden", " in ", "تأسيسات عقد 1550 في السويد"),
    (
        "20th century disestablishments in newfoundland and labrador",
        " in ",
        "انحلالات القرن 20 في نيوفاوندلاند واللابرادور",
    ),
    (
        "20th century disestablishments in the danish colonial empire",
        " in ",
        "انحلالات القرن 20 في الإمبراطورية الاستعمارية الدنماركية",
    ),
    ("20th century establishments in french guiana", " in ", "تأسيسات القرن 20 في غويانا الفرنسية"),
    ("20th century establishments in ireland", " in ", "تأسيسات القرن 20 في أيرلندا"),
    ("20th century monarchs by country", " by ", "ملكيون في القرن 20 حسب البلد"),
    ("july 1550 crimes by continent", " by ", "جرائم يوليو 1550 حسب القارة"),
]


def test_result_only_with_event2() -> None:
    expected_result = {}
    diff_result = {}
    for tab in data_list_bad:
        category, separator, expected = tab
        result = find_ar_label(category, separator, use_event2=True)
        result2 = find_ar_label(category, separator, use_event2=False)
        if result != expected and result2 != expected:
            expected_result[category] = expected
            diff_result[category] = result

    dump_diff(diff_result, "test_result_only_with_event2")
    assert diff_result == expected_result, f"Differences found: {len(diff_result)}"

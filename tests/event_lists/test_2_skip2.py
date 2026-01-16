#
import pytest
from load_one_data import dump_diff, dump_same_and_not_same, one_dump_test

from ArWikiCats import resolve_label_ar

data0_no_label = {
    "Category:1st-millennium architecture": "تصنيف:عمارة الألفية 1",
    "Category:10th-century BC architecture": "تصنيف:عمارة القرن 10 ق م",
    "Category:1st-century architecture": "تصنيف:عمارة القرن 1",
    "Category:1370s conflicts": "تصنيف:نزاعات في عقد 1370",
    "Attacks on Jewish institutions by century": "تصنيف:هجمات على مؤسسات يهودية حسب القرن",
    "Attacks on Jewish institutions in Poland": "تصنيف:هجمات على مؤسسات يهودية في بولندا",
    "Attacks on Jewish institutions in United States": "تصنيف:هجمات على مؤسسات يهودية في الولايات المتحدة",
    "Attacks on Jewish institutions": "تصنيف:هجمات على مؤسسات يهودية",
    "18th-century attacks on Jewish institutions": "تصنيف:هجمات القرن 18 في مؤسسات يهودية",
    "20th-century attacks on Jewish institutions in United States": "تصنيف:هجمات القرن 20 في مؤسسات يهودية في الولايات المتحدة",
    "20th-century attacks on Jewish institutions": "تصنيف:هجمات القرن 20 في مؤسسات يهودية",
    "21st-century attacks on Jewish institutions in United States": "تصنيف:هجمات القرن 21 في مؤسسات يهودية في الولايات المتحدة",
    "21st-century attacks on Jewish institutions": "تصنيف:هجمات القرن 21 في مؤسسات يهودية",
    "Lists of people executed in the United States by year": "قوائم أشخاص أعدموا في الولايات المتحدة حسب السنة",
    "Lists of people executed in United States by year": "قوائم أشخاص أعدموا في الولايات المتحدة حسب السنة",
    "Healthcare by city of the United States": "الرعاية الصحية بواسطة مدينة الولايات المتحدة",
    "north american television awards": "جوائز التلفزة الأمريكية الشمالية",
    "mexican revolution films": "أفلام الثورة المكسيكية",
    "northern-ireland football cups": "كؤوس كرة القدم الأيرلندية الشمالية",
    "chinese professional baseball league awards": "جوائز دوري كرة القاعدة الصيني للمحترفين",
    "paralympics people": "أشخاص في الألعاب البارالمبية",
    "Fictional people executed for murder": "أشخاص خياليون أعدموا بتهمة قتل",
    "Fictional people executed for treason": "أشخاص خياليون أعدموا بتهمة خيانة",
    "Buddhist comics": "قصص مصورة بوذيون",
    "Buddhist media in Taiwan": "إعلام بوذيون في تايوان",
    "Buddhist media": "إعلام بوذيون",
    "Buddhist music": "موسيقى بوذيون",
    "Mexican television awards": "جوائز التلفزة المكسيكية",
    "2025–26 in Northern Ireland association football": "كرة القدم الأيرلندية الشمالية في 2025–26",
    "1971–72 in Northern Ireland association football": "كرة القدم الأيرلندية الشمالية في 1971–72",
    "Buddhist video games": "ألعاب فيديو بوذيون",
    "Hindu music": "موسيقى هندوس",
    "Islamic media in India": "إعلام إسلاميون في الهند",
    "Islamic media": "إعلام إسلاميون",
    "Islamic music": "موسيقى إسلاميون",
    "Nazi culture": "ثقافة نازيون",
    "Nazi songs": "أغاني نازيون",
    "Saints and Soldiers films": "قديسون وأفلام مجندون",
    "muslim people templates": "قوالب أعلام مسلمون",
    "deaf culture": "ثقافة صم",
    "singaporean blind people": "أعلام سنغافوريون مكفوفون",
    "ukrainian deaf people": "أعلام أوكرانيون صم",
    "slovenian deaf people": "أعلام سلوفينيون صم",
    "russian blind people": "أعلام روس مكفوفون",
    "czech deaf people": "أعلام تشيكيون صم",
    "by benjamin britten": "بواسطة بنجامين بريتن",
    "by james cameron": "بواسطة جيمس كاميرون",
    "by raphael": "بواسطة رافاييل",
    "by vaikom muhammad basheer": "بواسطة محمد بشير",
    "expatriate men's footballers": "لاعبو كرة قدم مغتربون",
    "expatriate men's soccer players": "لاعبو كرة قدم مغتربون",
    "Icelandic deaf people": "أعلام آيسلنديون صم",
    "Romantic composers": "ملحنون رومانسيون",
    "Expatriate men's footballers in Papua New Guinea": "لاعبو كرة قدم مغتربون في بابوا غينيا الجديدة",
    "American expatriate men's soccer players": "لاعبو كرة قدم أمريكيون مغتربون",
    "Byzantine female saints": "قديسات بيزنطيات",
    "Ancient Christians": "مسيحيون قدماء",
    "Ancient Christian female saints": "قديسات مسيحيات قدماء",
    "Ancient Jewish physicians": "أطباء يهود قدماء",
    "Ancient Jewish scholars": "دارسون يهود قدماء",
    "Ancient Jewish women": "يهوديات قدماء",
    "Ancient Jewish writers": "كتاب يهود قدماء",
    "Murdered American Jews": "أمريكيون يهود قتلوا",
}

data0 = {
    "Category:1630s natural disasters": "",
    "Category:17th-century plays": "",
    "Category:1830s documents": "",
    "Category:1990s television series debuts": "",
    "Category:19th-century books": "",
    "Category:3rd-century paintings": "",
    "Category:3rd-millennium works": "",
    "Category:2026 television series debuts": "",
    "Category:13th-century plays": "",
    "Category:1009 works": "تصنيف:أعمال 1009",
    "Category:1239 works": "تصنيف:أعمال 1239",
    "Category:1261 works": "تصنيف:أعمال 1261",
    "Category:1429 in law": "تصنيف:قانون في 1429",
    "Category:1483 works": "تصنيف:أعمال 1483",
    "Category:1562 works": "تصنيف:أعمال 1562",
    "Category:1701 in international relations": "تصنيف:العلاقات الدولية في 1701",
    "Category:1727 in law": "تصنيف:قانون في 1727",
    "Category:1737 in music": "تصنيف:الموسيقى في 1737",
    "Category:1752 works": "تصنيف:أعمال 1752",
    "Category:1793 elections": "تصنيف:انتخابات 1793",
    "Category:1795 in mass media": "تصنيف:وسائل إعلام في 1795",
    "Category:1826 murders by continent": "تصنيف:جرائم قتل في 1826 حسب القارة",
    "Category:1832 works": "تصنيف:أعمال 1832",
    "Category:1833 in mass media": "تصنيف:وسائل إعلام في 1833",
    "Category:1835 meteorology": "تصنيف:الأرصاد الجوية 1835",
    "Category:1842 in mass media": "تصنيف:وسائل إعلام في 1842",
    "Category:1854 in law": "تصنيف:قانون في 1854",
    "Category:1855 disasters by country": "تصنيف:كوارث 1855 حسب البلد",
    "Category:1867 in mass media": "تصنيف:وسائل إعلام في 1867",
    "Category:1902 in music by country": "تصنيف:موسيقى في 1902 حسب البلد",
    "Category:1904 murders by country": "تصنيف:جرائم قتل في 1904 حسب البلد",
    "Category:1910 in international relations": "تصنيف:العلاقات الدولية في 1910",
    "Category:1917 in music": "تصنيف:الموسيقى في 1917",
    "Category:1934 murders": "تصنيف:جرائم قتل في 1934",
    "Category:1948 in law": "تصنيف:قانون في 1948",
    "Category:1948 treaties": "تصنيف:اتفاقيات 1948",
    "Category:1965 in music by country": "تصنيف:موسيقى في 1965 حسب البلد",
    "Category:1970s elections": "تصنيف:انتخابات عقد 1970",
    "Category:1972 murders": "تصنيف:جرائم قتل في 1972",
    "Category:1990 in international relations": "تصنيف:العلاقات الدولية في 1990",
    "Category:2021 meteorology": "تصنيف:الأرصاد الجوية 2021",
    "Category:2024 disasters by country": "تصنيف:كوارث 2024 حسب البلد",
    "Category:60s conflicts": "تصنيف:نزاعات عقد 60",
    "Category:April 1959 in sports": "تصنيف:أبريل 1959 في ألعاب رياضية",
    "Category:December 2007 in sports": "تصنيف:ديسمبر 2007 في ألعاب رياضية",
    "Category:Fiction set in 1716": "تصنيف:الخيال تقع أحداثها في 1716",
    "Category:Fiction set in 1790s": "تصنيف:الخيال تقع أحداثها في عقد 1790",
    "Category:Fiction set in 1819": "تصنيف:الخيال تقع أحداثها في 1819",
    "Category:Fiction set in 27th century": "تصنيف:الخيال تقع أحداثها في القرن 27",
    "Category:January 1901 in sports": "تصنيف:يناير 1901 في ألعاب رياضية",
    "Category:January 1952 in sports": "تصنيف:يناير 1952 في ألعاب رياضية",
    "Category:May 1946 in sports": "تصنيف:مايو 1946 في ألعاب رياضية",
    "Category:May 1993 in sports": "تصنيف:مايو 1993 في ألعاب رياضية",
    "Category:September 2024 in sports": "تصنيف:سبتمبر 2024 في ألعاب رياضية",
    "Category:Transport companies established in 1946": "تصنيف:شركات النقل أسست في 1946",
    "Category:Transport infrastructure completed in 1916": "تصنيف:البنية التحتية للنقل اكتملت في 1916",
    "Category:Transport infrastructure completed in 1972": "تصنيف:البنية التحتية للنقل اكتملت في 1972",
    "Category:Transport infrastructure completed in 21st century": "تصنيف:البنية التحتية للنقل اكتملت في القرن 21",
    "Category:Articles containing potentially dated statements from February 2024": "",
    "Category:Articles lacking reliable references from February 2013": "",
    "Category:Articles with dead external links from June 2017": "",
    "Category:Educational institutions established in 2009": "",
    "Category:1013 works": "تصنيف:أعمال 1013",
    "Category:1817 treaties": "تصنيف:اتفاقيات 1817",
    "Category:1999 disasters by country": "تصنيف:كوارث 1999 حسب البلد",
    "Category:1909 murders by country": "تصنيف:جرائم قتل في 1909 حسب البلد",
    "Category:1265 works": "تصنيف:أعمال 1265",
    "Category:October 1922 in sports": "تصنيف:أكتوبر 1922 في ألعاب رياضية",
    "Category:1708 in law": "تصنيف:قانون في 1708",
    "Category:June 1956 in sports": "تصنيف:يونيو 1956 في ألعاب رياضية",
    "Category:Articles containing potentially dated statements from April 2014": "",
    "Category:January 2026 in sports": "تصنيف:يناير 2026 في ألعاب رياضية",
    "Category:July 2026 in sports": "تصنيف:يوليو 2026 في ألعاب رياضية",
    "Category:2026 elections by country": "تصنيف:انتخابات 2026 حسب البلد",
    "Category:2026 in music by country": "تصنيف:موسيقى في 2026 حسب البلد",
    "Category:April 2026 in sports": "تصنيف:أبريل 2026 في ألعاب رياضية",
    "Category:August 2026 in sports": "تصنيف:أغسطس 2026 في ألعاب رياضية",
    "Category:February 2026 in sports": "تصنيف:فبراير 2026 في ألعاب رياضية",
    "Category:June 2026 in sports": "تصنيف:يونيو 2026 في ألعاب رياضية",
    "Category:March 2026 in sports": "تصنيف:مارس 2026 في ألعاب رياضية",
    "Category:May 2026 in sports": "تصنيف:مايو 2026 في ألعاب رياضية",
    "Category:November 2026 in sports": "تصنيف:نوفمبر 2026 في ألعاب رياضية",
    "Category:September 2026 in sports": "تصنيف:سبتمبر 2026 في ألعاب رياضية",
    "20th-century Anglican archbishops in Ireland": "رؤساء أساقفة أنجليكيون في أيرلندا في القرن 20",
    "20th-century Anglican archbishops in New Zealand": "رؤساء أساقفة أنجليكيون في نيوزيلندا في القرن 20",
    "21st-century Anglican archbishops in New Zealand": "رؤساء أساقفة أنجليكيون في نيوزيلندا في القرن 21",
    "17th-century Dutch books": "كتب هولندية في القرن 17",
}

data1 = {}

to_test = [
    # ("test_2_skip2_0", data0),
    ("test_2_skip2_2", data1),
]


@pytest.mark.parametrize("category, expected", data0.items(), ids=data0.keys())
@pytest.mark.skip2
def test_2_skip2_0(category: str, expected: str) -> None:
    label = resolve_label_ar(category)
    assert label == expected


@pytest.mark.parametrize("category, expected", data0_no_label.items(), ids=data0_no_label.keys())
@pytest.mark.skip2
def test_2_skip2_2(category: str, expected: str) -> None:
    label = resolve_label_ar(category)
    assert label == expected


@pytest.mark.parametrize("name,data", to_test)
@pytest.mark.dump
def test_peoples(name: str, data: dict[str, str]) -> None:
    expected, diff_result = one_dump_test(data, resolve_label_ar)

    dump_diff(diff_result, name)
    dump_same_and_not_same(data, expected, name)
    assert diff_result == expected, f"Differences found: {len(diff_result):,}, len all :{len(data):,}"

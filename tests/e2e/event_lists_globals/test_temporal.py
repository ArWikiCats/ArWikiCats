#
import pytest
from load_one_data import dump_diff, one_dump_test

from ArWikiCats import resolve_label_ar

temporal_1 = {
    "1950s criminal comedy films": "أفلام كوميديا الجريمة في عقد 1950",
    "1960s black comedy films": "أفلام كوميدية سوداء في عقد 1960",
    "1960s criminal comedy films": "أفلام كوميديا الجريمة في عقد 1960",
    "1970s black comedy films": "أفلام كوميدية سوداء في عقد 1970",
    "1970s criminal comedy films": "أفلام كوميديا الجريمة في عقد 1970",
    "1980s black comedy films": "أفلام كوميدية سوداء في عقد 1980",
    "1980s criminal comedy films": "أفلام كوميديا الجريمة في عقد 1980",
    "00s establishments in the Roman Empire": "تأسيسات عقد 00 في الإمبراطورية الرومانية",
    "1000 disestablishments by country": "انحلالات سنة 1000 حسب البلد",
    "1000 disestablishments in Europe": "انحلالات سنة 1000 في أوروبا",
    "1000s disestablishments in Asia": "انحلالات عقد 1000 في آسيا",
    "13th century establishments in the Roman Empire": "تأسيسات القرن 13 في الإمبراطورية الرومانية",
    "14th-century establishments in India": "تأسيسات القرن 14 في الهند",
    "1902 films": "أفلام إنتاج 1902",
    "1990s BC disestablishments in Asia": "انحلالات عقد 1990 ق م في آسيا",
    "1990s disestablishments in Europe": "انحلالات عقد 1990 في أوروبا",
    "1994–95 in European rugby union by country": "اتحاد الرجبي الأوروبي في 1994–95 حسب البلد",
    "1st century BC": "القرن 1 ق م",
}

temporal_2 = {
    "2000s films": "أفلام إنتاج عقد 2000",
    "2000s in American cinema": "السينما الأمريكية في عقد 2000",
    "2000s in film": "عقد 2000 في الأفلام",
    "2006 Winter Paralympics events": "أحداث الألعاب البارالمبية الشتوية 2006",
    "2006 establishments by country": "تأسيسات سنة 2006 حسب البلد",
    "2006 in north korean sport": "رياضة كورية شمالية في 2006",
    "2017 American television series debuts": "مسلسلات تلفزيونية أمريكية بدأ عرضها في 2017",
    "2017 American television series endings": "مسلسلات تلفزيونية أمريكية انتهت في 2017",
    "2017 events by country": "أحداث 2017 حسب البلد",
    "2017 events": "أحداث 2017",
    "2017 in Emirati football": "كرة القدم الإماراتية في 2017",
    "2017–18 in Emirati football": "كرة القدم الإماراتية في 2017–18",
    "2018 Summer Youth Olympics events": "أحداث الألعاب الأولمبية الشبابية الصيفية 2018",
    "20th-century disestablishments in India": "انحلالات القرن 20 في الهند",
    "21st century in film": "القرن 21 في الأفلام",
    "21st-century films": "أفلام إنتاج القرن 21",
    "440s bc": "عقد 440 ق م",
    "440s": "عقد 440",
    "977 by country": "977 حسب البلد",
    "Airlines by year of establishment": "شركات طيران حسب سنة التأسيس",
    "American cinema by decade": "السينما الأمريكية حسب العقد",
}

temporal_3 = {
    "10th millennium in fiction": "الخيال في الألفية 10",
    "1270s in the Holy Roman Empire": "الإمبراطورية الرومانية المقدسة في عقد 1270",
    "19th-century actors by religion": "ممثلون في القرن 19 حسب الدين",
    "19th-century people by religion": "أشخاص في القرن 19 حسب الدين",
    "2000s in the United States by state": "الولايات المتحدة في عقد 2000 حسب الولاية",
    "21st century in the Czech Republic": "التشيك في القرن 21",
    "21st-century in Qatar": "قطر في القرن 21",
    "Manufacturing companies established in the 2nd millennium": "شركات تصنيع أسست في الألفية 2",
}
temporal_4 = {
    "Animals by year of formal description": "حيوانات حسب سنة الوصف",
    "April 1983 events in Europe": "أحداث أبريل 1983 في أوروبا",
    "Comics set in the 1st century BC": "قصص مصورة تقع أحداثها في القرن 1 ق م",
    "Decades by country": "عقود حسب البلد",
    "Decades in Oklahoma": "عقود في أوكلاهوما",
    "Decades in the United States by state": "عقود في الولايات المتحدة حسب الولاية",
    "Films set in the 21st century": "أفلام تقع أحداثها في القرن 21",
    "Historical webcomics": "ويب كومكس تاريخية",
    "July 2018 events by continent": "أحداث يوليو 2018 حسب القارة",
    "Mammals by century of formal description": "ثدييات حسب قرن الوصف",
    "Multi-sport events in the Soviet Union": "أحداث رياضية متعددة في الاتحاد السوفيتي",
    # "November 2006 in Yemen": "نوفمبر 2006 في اليمن",
    "Olympic figure skaters by year": "متزلجون فنيون أولمبيون حسب السنة",
    "Publications by year of disestablishment": "منشورات حسب سنة الانحلال",
    "Publications by year of establishment": "منشورات حسب سنة التأسيس",
    "Sports organisations by decade of establishment": "منظمات رياضية حسب عقد التأسيس",
    "Television series endings by year": "مسلسلات تلفزيونية حسب سنة انتهاء العرض",
    "Tetrapods by century of formal description": "رباعيات الأطراف حسب قرن الوصف",
    "Vertebrates described in the 20th century": "فقاريات وصفت في القرن 20",
    "Years in north korean television": "سنوات في التلفزة الكورية الشمالية",
    "Years in the United States by state": "سنوات في الولايات المتحدة حسب الولاية",
    "multi-sport events at Yemen": "أحداث رياضية متعددة في اليمن",
}
TEMPORAL_CASES = [
    ("temporal_1", temporal_1),
    ("temporal_2", temporal_2),
    ("temporal_3", temporal_3),
    ("temporal_4", temporal_4),
]


@pytest.mark.parametrize("name,data", TEMPORAL_CASES)
@pytest.mark.dump
def test_temporal(name: str, data: dict[str, str]) -> None:
    expected, diff_result = one_dump_test(data, resolve_label_ar)
    dump_diff(diff_result, name)
    assert diff_result == expected, f"Differences found: {len(diff_result):,}, len all :{len(data):,}"


@pytest.mark.parametrize("category, expected", temporal_1.items(), ids=temporal_1.keys())
@pytest.mark.fast
def test_temporal_1(category: str, expected: str) -> None:
    label = resolve_label_ar(category)
    assert label == expected


@pytest.mark.parametrize("category, expected", temporal_2.items(), ids=temporal_2.keys())
@pytest.mark.fast
def test_temporal_2(category: str, expected: str) -> None:
    label = resolve_label_ar(category)
    assert label == expected


@pytest.mark.parametrize("category, expected", temporal_3.items(), ids=temporal_3.keys())
@pytest.mark.fast
def test_temporal_3(category: str, expected: str) -> None:
    label = resolve_label_ar(category)
    assert label == expected


@pytest.mark.parametrize("category, expected", temporal_4.items(), ids=temporal_4.keys())
@pytest.mark.fast
def test_temporal_4(category: str, expected: str) -> None:
    label = resolve_label_ar(category)
    assert label == expected

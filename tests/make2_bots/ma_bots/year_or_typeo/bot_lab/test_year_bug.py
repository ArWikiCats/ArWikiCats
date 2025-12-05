import pytest
from load_one_data import dump_diff, one_dump_test

from ArWikiCats.make_bots.ma_bots.year_or_typeo.bot_lab import (
    label_for_startwith_year_or_typeo,
)

examples = {
    "2017 American television series debuts": "مسلسلات تلفزيونية أمريكية بدأ عرضها في 2017",
    "2017 American television series endings": "مسلسلات تلفزيونية أمريكية انتهت في 2017",
    "Paralympic competitors for Cape Verde": "منافسون في الألعاب البارالمبية من الرأس الأخضر",
    "1980 sports events in Europe": "أحداث 1980 الرياضية في أوروبا",
    "April 1983 sports events": "أحداث أبريل 1983 الرياضية",
    "April 1983 events in Europe": "أحداث أبريل 1983 في أوروبا",
    "July 2018 events by continent": "أحداث يوليو 2018 حسب القارة",
    "2000s films": "أفلام إنتاج عقد 2000",
    "00s establishments in the Roman Empire": "تأسيسات عقد 00 في الإمبراطورية الرومانية",
    "1000s disestablishments in Asia": "انحلالات عقد 1000 في آسيا",
    "1370s conflicts": "نزاعات عقد 1370",
    "1950s criminal comedy films": "أفلام كوميديا الجريمة عقد 1950",
    "1960s black comedy films": "أفلام كوميدية سوداء عقد 1960",
    "1960s criminal comedy films": "أفلام كوميديا الجريمة عقد 1960",
    "1970s black comedy films": "أفلام كوميدية سوداء عقد 1970",
    "1970s criminal comedy films": "أفلام كوميديا الجريمة عقد 1970",
    "1980s black comedy films": "أفلام كوميدية سوداء عقد 1980",
    "1980s criminal comedy films": "أفلام كوميديا الجريمة عقد 1980",
    "1990s BC disestablishments in Asia": "انحلالات عقد 1990 ق م في آسيا",
    "1990s disestablishments in Europe": "انحلالات عقد 1990 في أوروبا",
    # "8th parliament of la rioja": "برلمان منطقة لا ريوخا الثامن",
}

examples_century = {
    "1st-millennium architecture": "عمارة الألفية 1",
    "1st-millennium literature": "أدب الألفية 1",
    "18th-century Dutch explorers": "مستكشفون هولنديون في القرن 18",
    "20th-century Albanian sports coaches": "مدربو رياضة ألبان في القرن 20",
    "19th-century actors": "ممثلون في القرن 19",
    "19th-century actors by religion": "ممثلون في القرن 19 حسب الدين",
    "19th-century people by religion": "أشخاص في القرن 19 حسب الدين",
    "20th-century railway accidents": "حوادث سكك حديد في القرن 20",
    "18th-century people of the Dutch Empire": "أشخاص من الإمبراطورية الهولندية القرن 18",
    "20th-century disestablishments in India": "انحلالات القرن 20 في الهند",
    "21st-century films": "أفلام القرن 21",
    "10th-century BC architecture": "عمارة القرن 10 ق م",
    "13th century establishments in the Roman Empire": "تأسيسات القرن 13 في الإمبراطورية الرومانية",
    "14th-century establishments in India": "تأسيسات القرن 14 في الهند",
    "19th-century publications": "منشورات القرن 19",
    "1st-century architecture": "عمارة القرن 1",
}


TEMPORAL_CASES = [
    ("test_label_for_startwith_year_or_typeo", examples),
    ("test_label_for_startwith_year_or_typeo_centuries", examples_century),
]


@pytest.mark.parametrize("name,data", TEMPORAL_CASES)
@pytest.mark.dump
def test_all(name: str, data: dict[str, str]) -> None:
    expected, diff_result = one_dump_test(data, label_for_startwith_year_or_typeo)

    dump_diff(diff_result, name)
    assert diff_result == expected, f"Differences found: {len(diff_result)}"


@pytest.mark.parametrize("category, expected", examples.items(), ids=list(examples.keys()))
@pytest.mark.fast
def test_label_for_startwith_year_or_typeo(category: str, expected: str) -> None:
    label = label_for_startwith_year_or_typeo(category)
    assert label == expected


@pytest.mark.parametrize("category, expected", examples_century.items(), ids=list(examples_century.keys()))
@pytest.mark.fast
def test_label_for_startwith_year_or_typeo_centuries(category: str, expected: str) -> None:
    label = label_for_startwith_year_or_typeo(category)
    assert label == expected

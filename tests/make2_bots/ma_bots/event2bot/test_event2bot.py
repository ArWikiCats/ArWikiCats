
import pytest
from src.make2_bots.ma_bots.event2bot import make_lab_dodo
from load_one_data import ye_test_one_dataset, dump_diff

examples = {
    '18th-century Dutch explorers': 'مستكشفون هولنديون في القرن 18',
    "20th-century Albanian sports coaches": "مدربو رياضة ألبان في القرن 20",
    '19th-century actors': 'ممثلون في القرن 19',
    '2000s American films': 'أفلام أمريكية في عقد 2000',
    '2017 American television series debuts': 'مسلسلات تلفزيونية أمريكية بدأ عرضها في 2017',
    '2017 American television series endings': 'مسلسلات تلفزيونية أمريكية انتهت في 2017',
    "Paralympic competitors for Cape Verde": "منافسون في الألعاب البارالمبية من الرأس الأخضر",
    "19th-century actors by religion": "ممثلون في القرن 19 حسب الدين",
    "19th-century people by religion": "أشخاص في القرن 19 حسب الدين",
    "20th-century railway accidents": "حوادث سكك حديد في القرن 20",
    "18th-century people of the Dutch Empire": "",
    "19th-century actors by religion": "",
    "19th-century people by religion": "",
    "20th-century railway accidents": "",
    "April 1983 sports events": "",
    "April 1983 events in Europe": "",
    "July 2018 events by continent": "",
    "1st-millennium architecture": "",
    "1st-millennium literature": "",
    "2000s films": "",
    "20th-century disestablishments in India": "",
    "21st-century films": "",
    "00s establishments in the Roman Empire": "",
    "1000s disestablishments in Asia": "",
    "10th-century BC architecture": "",
    "1370s conflicts": "",
    "13th century establishments in the Roman Empire": "",
    "14th-century establishments in India": "",
    "1950s criminal comedy films": "",
    "1960s black comedy films": "",
    "1960s criminal comedy films": "",
    "1970s black comedy films": "",
    "1970s criminal comedy films": "",
    '1980 sports events in Europe': 'أحداث 1980 الرياضية في أوروبا',
    "1980s black comedy films": "",
    "1980s criminal comedy films": "",
    "1990s BC disestablishments in Asia": "",
    "1990s disestablishments in Europe": "",
    "19th-century publications": "",
    "1st-century architecture": "",
}


@pytest.mark.parametrize(
    "category, expected",
    examples.items(),
    ids=[k for k in examples],
)
def _test_make_lab_dodo(category: str, expected: str) -> None:
    assert make_lab_dodo(category) == expected


def test_make_lab_dodo():
    expected, diff_result = ye_test_one_dataset(examples, make_lab_dodo)

    dump_diff(diff_result, "test_make_lab_dodo")
    assert diff_result == expected, f"Differences found: {len(diff_result)}"

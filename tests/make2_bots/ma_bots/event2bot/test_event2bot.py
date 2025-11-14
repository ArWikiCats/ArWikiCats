
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
    "Category:18th-century people of the Dutch Empire": "",
    "Category:19th-century actors by religion": "",
    "Category:19th-century people by religion": "",
    "Category:20th-century railway accidents": "",
    "Category:April 1983 sports events": "",
    "Category:April 1983 events in Europe": "",
    "Category:July 2018 events by continent": "",
    "Category:1st-millennium architecture": "",
    "Category:1st-millennium literature": "",
    "Category:2000s films": "",
    "Category:20th-century disestablishments in India": "",
    "Category:21st-century films": "",
    "Category:00s establishments in the Roman Empire": "",
    "Category:1000s disestablishments in Asia": "",
    "Category:10th-century BC architecture": "",
    "Category:1370s conflicts": "",
    "Category:13th century establishments in the Roman Empire": "",
    "Category:14th-century establishments in India": "",
    "Category:1950s criminal comedy films": "",
    "Category:1960s black comedy films": "",
    "Category:1960s criminal comedy films": "",
    "Category:1970s black comedy films": "",
    "Category:1970s criminal comedy films": "",
    'Category:1980 sports events in Europe': 'تصنيف:أحداث 1980 الرياضية في أوروبا',
    "Category:1980s black comedy films": "",
    "Category:1980s criminal comedy films": "",
    "Category:1990s BC disestablishments in Asia": "",
    "Category:1990s disestablishments in Europe": "",
    "Category:19th-century publications": "",
    "Category:1st-century architecture": "",
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

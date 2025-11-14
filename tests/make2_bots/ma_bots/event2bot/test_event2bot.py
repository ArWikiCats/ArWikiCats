
import pytest
from src.make2_bots.ma_bots.event2bot import make_lab_dodo

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
}


@pytest.mark.parametrize(
    "category, expected",
    examples.items(),
    ids=[k for k in examples],
)
def test_make_lab_dodo(category: str, expected: str) -> None:

    assert make_lab_dodo(category) == expected

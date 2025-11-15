
import pytest
from src.make2_bots.ma_bots.dodo_bots.dodo_2019 import work_2019_wrap

examples = {
    '18th-century Dutch explorers': 'مستكشفون هولنديون في القرن 18',
    '19th-century actors': 'ممثلون في القرن 19',
    '2017 American television series debuts': 'مسلسلات تلفزيونية أمريكية بدأ عرضها في 2017',
    '2017 American television series endings': 'مسلسلات تلفزيونية أمريكية انتهت في 2017',
    "20th-century railway accidents": "حوادث سكك حديد في القرن 20",
    "Paralympic competitors for Cape Verde": "",
}


@pytest.mark.parametrize(
    "category, expected",
    examples.items(),
    ids=[k for k in examples],
)
def test_work_2019(category: str, expected: str) -> None:
    assert work_2019_wrap(category) == expected

#
import pytest

from ArWikiCats import resolve_label_ar
from utils.dump_runner import make_dump_test_name_data

data_1 = {
    "Women's universities and colleges in India": "جامعات وكليات نسائية في الهند",
    "women's universities and colleges": "جامعات وكليات نسائية",
    "Christian universities and colleges templates": "قوالب جامعات وكليات مسيحية",
    "Hindu philosophers and theologians": "فلاسفة ولاهوتيون هندوس",
    "17th-century_establishments_in_Närke_and_Värmland_County": "تأسيسات القرن 17 في مقاطعة ناركه وفارملاند",
    "17th_century_in_Närke_and_Värmland_County": "مقاطعة ناركه وفارملاند في القرن 17",
    "Centuries_in_Närke_and_Värmland_County": "قرون في مقاطعة ناركه وفارملاند",
    "Establishments_in_Närke_and_Värmland_County_by_century": "تأسيسات في مقاطعة ناركه وفارملاند حسب القرن",
    "Närke_and_Värmland_County": "مقاطعة ناركه وفارملاند",
}


@pytest.mark.parametrize("category, expected", data_1.items(), ids=data_1.keys())
@pytest.mark.fast
def test_2(category: str, expected: str) -> None:
    label = resolve_label_ar(category)
    assert label == expected


to_test = [
    ("test_1", data_1),
]


test_dump_all = make_dump_test_name_data(to_test, resolve_label_ar, run_same=False)

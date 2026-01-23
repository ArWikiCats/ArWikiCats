#
import pytest

from ArWikiCats import resolve_label_ar
from utils.dump_runner import make_dump_test_name_data

data_1 = {
    "Defunct national sports teams by country": "منتخبات رياضية وطنية سابقة حسب البلد",
    "defunct rugby union stadiums": "استادات اتحاد رجبي سابقة",
    "defunct american football venues": "ملاعب كرة قدم أمريكية سابقة",
    "defunct athletics venues": "ملاعب ألعاب قوى سابقة",
    "defunct baseball venues": "ملاعب كرة قاعدة سابقة",
    "defunct basketball venues": "ملاعب كرة سلة سابقة",
    "defunct football clubs": "أندية كرة قدم سابقة",
    "defunct football venues": "ملاعب كرة قدم سابقة",
    "defunct golf tournaments": "بطولات غولف سابقة",
    "defunct ice hockey venues": "ملاعب هوكي جليد سابقة",
    "defunct motorsport venues": "ملاعب رياضة محركات سابقة",
    "defunct private universities and colleges": "جامعات وكليات خاصة سابقة",
    "defunct rugby league venues": "ملاعب دوري رجبي سابقة",
    "defunct soccer clubs": "أندية كرة قدم سابقة",
    "defunct soccer venues": "ملاعب كرة قدم سابقة",
    "defunct softball venues": "ملاعب كرة لينة سابقة",
    "defunct tennis tournaments": "بطولات كرة مضرب سابقة",
}


@pytest.mark.parametrize("category, expected", data_1.items(), ids=data_1.keys())
@pytest.mark.fast
def test_2_fast_2(category: str, expected: str) -> None:
    label = resolve_label_ar(category)
    assert label == expected


test_dump_all = make_dump_test_name_data([("data_1", data_1)], resolve_label_ar, run_same=True)

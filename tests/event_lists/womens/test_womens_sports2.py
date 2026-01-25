#
import pytest
from load_one_data import dump_diff, dump_diff_text, dump_same_and_not_same, one_dump_test

from ArWikiCats import resolve_label_ar
from utils.dump_runner import make_dump_test_name_data

data0 = {
    "Women's sports clubs and teams in Afghanistan": "أندية وفرق رياضية نسائية في أفغانستان",
    # "Women's sports seasons": "مواسم رياضات نسائية",
}

data1 = {
    "American women's sports": "رياضات نسائية أمريكية",
    "Women's sports by dependent territory": "رياضات نسائية حسب الأقاليم التابعة",
    "women's sports clubs": "أندية رياضية نسائية",
    "women's sports competitions": "منافسات رياضية نسائية",
    "women's sports leagues": "دوريات رياضية نسائية",
    "women's sports organizations": "منظمات رياضية نسائية",
    "women's sports teams": "فرق رياضية نسائية",
    "national women's sports teams": "منتخبات رياضية وطنية نسائية",
    "college women's sports teams in united states": "فرق رياضات الكليات للسيدات في الولايات المتحدة",
    "mexican women's sports": "رياضات نسائية مكسيكية",
    "canadian women's sports": "رياضات نسائية كندية",
    "american women's sports": "رياضات نسائية أمريكية",
    "2026 in American women's sports": "رياضات نسائية أمريكية في 2026",
    "1964 in American women's sports": "رياضات نسائية أمريكية في 1964",
    "1972 in American women's sports": "رياضات نسائية أمريكية في 1972",
    "2003 in Canadian women's sports": "رياضات نسائية كندية في 2003",
    "Defunct women's sports clubs and teams": "",
    "Women's sport by continent and period": "رياضة نسائية حسب القارة والحقبة",
    "Women's sport by period": "رياضة نسائية حسب الحقبة",
    "Women's sport in Mexico City": "رياضة نسائية في مدينة مكسيكو",
    "Women's sport in Oceania by period": "رياضة نسائية في أوقيانوسيا حسب الحقبة",
}

data2 = {
    "Summer Olympics sports navigational boxes": "صناديق تصفح رياضات الألعاب الأولمبية الصيفية",
    "Winter Olympics sports navigational boxes": "صناديق تصفح رياضات الألعاب الأولمبية الشتوية",
    "Former Olympic sports": "رياضات أولمبية سابقة",
    "Ancient Olympic sports": "رياضات أولمبية قديمة",
    "Summer Olympic sports": "رياضات الألعاب الأولمبية الصيفية",
    "Winter Olympics sports templates": "قوالب رياضات الألعاب الأولمبية الشتوية",
    "Summer Olympics sports templates": "قوالب رياضات الألعاب الأولمبية الصيفية",
    "Winter Olympics sports": "رياضات الألعاب الأولمبية الشتوية",
    "Summer Olympics sports": "رياضات الألعاب الأولمبية الصيفية",
    "Azerbaijan sports navigational boxes": "صناديق تصفح الرياضة في أذربيجان",
    "Austria sports navigational boxes": "صناديق تصفح الرياضة في النمسا",
    "wheelchair sports": "ألعاب رياضية على الكراسي المتحركة",
}

to_test = [
    ("test_sports2_data_0", data0),
    ("test_sports2_data_1", data1),
    ("test_sports2_data_2", data2),
]


@pytest.mark.parametrize("category, expected", data0.items(), ids=data0.keys())
@pytest.mark.fast
def test_sports2_data_0(category: str, expected: str) -> None:
    """
    pytest tests/event_lists/womens/test_womens_sports2.py::test_sports2_data_0
    """
    assert resolve_label_ar(category) == expected


@pytest.mark.parametrize("category, expected", data1.items(), ids=data1.keys())
@pytest.mark.fast
def test_sports2_data_1(category: str, expected: str) -> None:
    assert resolve_label_ar(category) == expected


@pytest.mark.parametrize("category, expected", data2.items(), ids=data2.keys())
@pytest.mark.fast
def test_sports2_data_2(category: str, expected: str) -> None:
    assert resolve_label_ar(category) == expected


test_dump_all = make_dump_test_name_data(to_test, resolve_label_ar, run_same=False)

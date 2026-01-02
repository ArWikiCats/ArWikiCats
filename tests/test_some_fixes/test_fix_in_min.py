#
import pytest
from load_one_data import dump_diff, dump_diff_text, one_dump_test

from ArWikiCats import resolve_arabic_category_label, resolve_label_ar

data0 = {}

data_1 = {
    # FINE
    "14th-century writers from Yemen": "كتاب من اليمن في القرن 14",
    "14th-century football players from Yemen": "لاعبو كرة قدم من اليمن في القرن 14",
    "wheelchair basketball players from Yemen": "لاعبو كرة سلة على كراسي متحركة من اليمن",
    "1400s BC wheelchair basketball players from Yemen": "لاعبو كرة سلة على كراسي متحركة من اليمن في عقد 1400 ق م",
}

data_2 = {
    # NEED FIXING
    "2020 international footballers from Yemen": "لاعبو كرة قدم دوليون من اليمن في 2020",
    "14th-century writers from the democratic republic of the Congo": "كتاب من جمهورية الكونغو الديمقراطية في القرن 14",
    "14th-century writers from Crown of Aragon": "كتاب من تاج أرغون في القرن 14",
    "14th-century writers from the Crown of Aragon": "كتاب من تاج أرغون في القرن 14",
}

to_test = [
    ("test_fix_in_min_0", data0),
    ("test_fix_in_min_1", data_1),
    ("test_fix_in_min_2", data_2),
]


@pytest.mark.parametrize("category, expected", data_1.items(), ids=data_1.keys())
@pytest.mark.fast
def test_fix_in_min_1(category: str, expected: str) -> None:
    label = resolve_label_ar(category)
    assert label == expected


@pytest.mark.parametrize("category, expected", data_2.items(), ids=data_2.keys())
@pytest.mark.skip2
def test_fix_in_min_2(category: str, expected: str) -> None:
    label = resolve_label_ar(category)
    assert label == expected


@pytest.mark.parametrize("name,data", to_test)
@pytest.mark.dump
def test_dump_all(name: str, data: dict[str, str]) -> None:
    expected, diff_result = one_dump_test(data, resolve_label_ar)
    dump_diff(diff_result, name)
    # dump_diff_text(expected, diff_result, name)
    assert diff_result == expected, f"Differences found: {len(diff_result):,}, len all :{len(data):,}"

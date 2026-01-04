#
import pytest
from load_one_data import dump_diff, one_dump_test, dump_same_and_not_same

from ArWikiCats import resolve_label_ar

test_classical_musicians_1 = {
    "Filipino classical musicians": "موسيقيون كلاسيكيون فلبينيون",
    "20th-century British classical musicians": "موسيقيون كلاسيكيون بريطانيون في القرن 20",
    "Welsh classical musicians": "موسيقيون كلاسيكيون ويلزيون",
    "Classical musicians from West Virginia": "موسيقيون كلاسيكيون من فرجينيا الغربية",
    "paraguayan classical musicians": "موسيقيون كلاسيكيون بارغوايانيون",
    "Jewish classical musicians": "موسيقيون كلاسيكيون يهود",
    "20th-century classical musicians from Northern Ireland": "موسيقيون كلاسيكيون من أيرلندا الشمالية في القرن 20",
    "21st-century classical musicians from Northern Ireland": "موسيقيون كلاسيكيون من أيرلندا الشمالية في القرن 21",
}

test_classical_musicians_3 = {
}

test_classical_musicians_4 = {
}

to_test = [
    ("test_classical_musicians_1", test_classical_musicians_1),
    ("test_classical_musicians_3", test_classical_musicians_3),
    ("test_classical_musicians_4", test_classical_musicians_4),
]


@pytest.mark.parametrize("category, expected", test_classical_musicians_1.items(), ids=test_classical_musicians_1.keys())
@pytest.mark.fast
def test_classical_musicians_1(category: str, expected: str) -> None:
    label = resolve_label_ar(category)
    assert label == expected


@pytest.mark.parametrize("name,data", to_test)
@pytest.mark.dump
def test_dump_all(name: str, data: dict[str, str]) -> None:
    expected, diff_result = one_dump_test(data, resolve_label_ar)

    dump_diff(diff_result, name)
    # dump_same_and_not_same(data, diff_result, name, True)
    assert diff_result == expected, f"Differences found: {len(diff_result):,}, len all :{len(data):,}"

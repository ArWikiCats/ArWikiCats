import pytest
from load_one_data import dump_diff, dump_same_and_not_same, one_dump_test

from ArWikiCats import resolve_label_ar
from utils.dump_runner import make_dump_test_name_data

fast_data = {
    "1650s crimes": "جرائم عقد 1650",
    "1650s disasters": "كوارث عقد 1650",
    "1650s disestablishments": "انحلالات عقد 1650",
    "1650s establishments": "تأسيسات عقد 1650",
    "1st millennium bc establishments": "تأسيسات الألفية 1 ق م",
    "1st millennium disestablishments": "انحلالات الألفية 1",
    "20th century attacks": "هجمات القرن 20",
    "20th century clergy": "رجال دين في القرن 20",
    "20th century lawyers": "محامون في القرن 20",
    "20th century mathematicians": "رياضياتيون في القرن 20",
    "20th century north american people": "أمريكيون شماليون في القرن 20",
    "20th century norwegian people": "نرويجيون في القرن 20",
    "20th century people": "أشخاص في القرن 20",
    "20th century philosophers": "فلاسفة في القرن 20",
    "20th century photographers": "مصورون في القرن 20",
    "20th century roman catholic bishops": "أساقفة كاثوليك رومان في القرن 20",
    "20th century romanian people": "رومان في القرن 20",
    "march 1650 crimes": "جرائم مارس 1650",
    "september 1650 crimes": "جرائم سبتمبر 1650",
}


@pytest.mark.parametrize("category, expected", fast_data.items(), ids=fast_data.keys())
@pytest.mark.fast
def test_event2_fast(category: str, expected: str) -> None:
    label = resolve_label_ar(category)
    assert label == expected


to_test = [
    ("fast_data", fast_data),
]

test_dump_all = make_dump_test_name_data(to_test, resolve_label_ar, run_same=True)

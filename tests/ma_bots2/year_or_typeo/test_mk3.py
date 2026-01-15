
import pytest
from load_one_data import dump_diff, dump_same_and_not_same, one_dump_test
from ArWikiCats import resolve_label_ar

data1 = {
    "1000 disestablishments by country": "انحلالات سنة 1000 حسب البلد",
    "1000 disestablishments in europe": "انحلالات سنة 1000 في أوروبا",
    "2000s films": "أفلام في عقد 2000",
    "awards by country": "جوائز حسب البلد",
    "politics of united states by state": "سياسة الولايات المتحدة حسب الولاية",
    "television series by city of location": "مسلسلات تلفزيونية حسب مدينة الموقع",
    "19th century people": "أشخاص في القرن 19",
    "lists of football players by national team": "قوائم لاعبو كرة قدم حسب المنتخب الوطني"
}


@pytest.mark.parametrize("category, expected", data1.items(), ids=data1.keys())
@pytest.mark.fast
def test_mk3_0(category: str, expected: str) -> None:
    label = resolve_label_ar(category)
    assert label == expected


to_test = [
    ("test_2_skip2_2", data1),
]


@pytest.mark.parametrize("name,data", to_test)
@pytest.mark.dump
def test_peoples(name: str, data: dict[str, str]) -> None:
    expected, diff_result = one_dump_test(data, resolve_label_ar)

    dump_diff(diff_result, name)
    dump_same_and_not_same(data, expected, name)
    assert diff_result == expected, f"Differences found: {len(diff_result):,}, len all :{len(data):,}"


import pytest
from load_one_data import dump_diff, dump_same_and_not_same, one_dump_test
from ArWikiCats.ma_bots2.year_or_typeo.mk3 import new_func_mk2
from ArWikiCats import resolve_label_ar


EXAMPLES = [
    {
        "category": "awards by country",
        "year": "",
        "typeo": "awards",
        "In": "by ",
        "country": "by country",
        "arlabel": "جوائز",
        "year_labe": "",
        "suf": "",
        "Add_In": True,
        "country_label": "حسب البلد",
        "Add_In_Done": False,
        "output": "جوائز حسب البلد",
    },
    {
        "category": "politics of united states by state",
        "year": "",
        "typeo": "politics",
        "In": "of ",
        "country": "united states by state",
        "arlabel": "سياسة",
        "year_labe": "",
        "suf": "",
        "Add_In": True,
        "country_label": "الولايات المتحدة حسب الولاية",
        "Add_In_Done": False,
        "output": "سياسة الولايات المتحدة حسب الولاية",
    },
    {
        "category": "television series by city of location",
        "year": "",
        "typeo": "television series",
        "In": "by ",
        "country": "by city of location",
        "arlabel": "مسلسلات تلفزيونية",
        "year_labe": "",
        "suf": "",
        "Add_In": True,
        "country_label": "حسب مدينة الموقع",
        "Add_In_Done": False,
        "output": "مسلسلات تلفزيونية حسب مدينة الموقع",
    },
    {
        "category": "19th century people",
        "year": "19th century ",
        "typeo": "",
        "In": "",
        "country": "people",
        "arlabel": " القرن 19",
        "year_labe": "القرن 19",
        "suf": "",
        "Add_In": True,
        "country_label": "أشخاص",
        "Add_In_Done": False,
        "output": "أشخاص في القرن 19",
    },
    {
        "category": "lists of football players by national team",
        "year": "",
        "typeo": "lists of",
        "In": "",
        "country": "football players by national team",
        "arlabel": "قوائم",
        "year_labe": "",
        "suf": "",
        "Add_In": True,
        "country_label": "لاعبو كرة قدم حسب المنتخب الوطني",
        "Add_In_Done": False,
        "output": "قوائم لاعبو كرة قدم حسب المنتخب الوطني",
    },
    {
        "category": "1000 disestablishments by country",
        "year": "1000 ",
        "typeo": "disestablishments",
        "In": "by ",
        "country": "by country",
        "arlabel": "انحلالات 1000",
        "year_labe": "1000",
        "suf": "",
        "Add_In": True,
        "country_label": "حسب البلد",
        "Add_In_Done": False,
        "output": "انحلالات 1000 حسب البلد",
    },
    {
        "category": "1000 disestablishments in europe",
        "year": "1000 ",
        "typeo": "disestablishments",
        "In": "in ",
        "country": "europe",
        "arlabel": "انحلالات 1000 في ",
        "year_labe": "1000",
        "suf": "",
        "Add_In": False,
        "country_label": "أوروبا",
        "Add_In_Done": True,
        "output": "انحلالات 1000 في أوروبا",
    },
    {
        "category": "2000s films",
        "year": "2000s ",
        "typeo": "",
        "In": "",
        "country": "films",
        "arlabel": " عقد 2000",
        "year_labe": "عقد 2000",
        "suf": "",
        "Add_In": True,
        "country_label": "أفلام",
        "Add_In_Done": False,
        "output": "أفلام عقد 2000",
    },
]


@pytest.mark.parametrize("example", EXAMPLES, ids=lambda e: e["category"])
@pytest.mark.skip2
def test_new_func_mk2_subset(example) -> None:
    _, result = new_func_mk2(
        example["category"],
        "",
        example["year"],
        example["typeo"],
        example["In"],
        example["country"],
        example["arlabel"],
        example["year_labe"],
        example["suf"],
        example["Add_In"],
        example["country_label"],
        example["Add_In_Done"],
    )

    expected = example["output"]
    assert result == expected


data1 = {x["category"]: x["output"] for x in EXAMPLES}

to_test = [
    # ("test_2_skip2_0", data0),
    ("test_2_skip2_2", data1),
]


@pytest.mark.parametrize("name,data", to_test)
@pytest.mark.dump
def test_peoples(name: str, data: dict[str, str]) -> None:
    expected, diff_result = one_dump_test(data, resolve_label_ar)

    dump_diff(diff_result, name)
    dump_same_and_not_same(data, expected, name)
    assert diff_result == expected, f"Differences found: {len(diff_result):,}, len all :{len(data):,}"

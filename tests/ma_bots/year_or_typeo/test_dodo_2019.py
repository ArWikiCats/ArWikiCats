import pytest

from ArWikiCats.make_bots.ma_bots.year_or_typeo.dodo_2019 import work_2019, work_2019_wrap

examples = {
    "18th-century Dutch explorers": "مستكشفون هولنديون في القرن 18",
    "19th-century actors": "ممثلون في القرن 19",
    "2017 American television series debuts": "مسلسلات تلفزيونية أمريكية بدأ عرضها في 2017",
    "2017 American television series endings": "مسلسلات تلفزيونية أمريكية انتهت في 2017",
    "20th-century railway accidents": "حوادث سكك حديد في القرن 20",
}


@pytest.mark.parametrize(
    "category, expected",
    examples.items(),
    ids=[k for k in examples],
)
def test_work_2019(category: str, expected: str) -> None:
    assert work_2019_wrap(category) == expected


examples2 = [
    {
        "category3": "18th-century Dutch explorers",
        "year": "18th-century",
        "year_labe": "القرن 18",
        "output": "مستكشفون هولنديون في القرن 18",
    },
    {
        "category3": "19th-century actors",
        "year": "19th-century",
        "year_labe": "القرن 19",
        "output": "ممثلون في القرن 19",
    },
    {
        "category3": "2017 American television series debuts",
        "year": "2017",
        "year_labe": "2017",
        "output": "مسلسلات تلفزيونية أمريكية بدأ عرضها في 2017",
    },
    {
        "category3": "2017 American television series endings",
        "year": "2017",
        "year_labe": "2017",
        "output": "مسلسلات تلفزيونية أمريكية انتهت في 2017",
    },
    {
        "category3": "20th-century railway accidents",
        "year": "20th-century",
        "year_labe": "القرن 20",
        "output": "حوادث سكك حديد في القرن 20",
    },
]


@pytest.mark.parametrize(
    "data",
    examples2,
    ids=[k["category3"] for k in examples2],
)
def test_work_2019_new(data: dict) -> None:
    result = work_2019(data["category3"], data["year"], data["year_labe"])
    assert result == data["output"]

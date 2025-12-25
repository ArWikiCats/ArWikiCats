import pytest
from load_one_data import dump_diff, one_dump_test

from ArWikiCats.new_resolvers.sports_formats_national.sport_lab_nat import sport_lab_nat_load_new

data_1 = {
    "yemeni national football teams fifth tier": "منتخبات كرة قدم وطنية يمنية من الدرجة الخامسة",
    "yemeni national football teams first tier": "منتخبات كرة قدم وطنية يمنية من الدرجة الأولى",
    "yemeni national football teams fourth tier": "منتخبات كرة قدم وطنية يمنية من الدرجة الرابعة",
    "yemeni national football teams premier": "منتخبات كرة قدم وطنية يمنية من الدرجة الممتازة",
    "yemeni national football teams second tier": "منتخبات كرة قدم وطنية يمنية من الدرجة الثانية",
    "yemeni national football teams seventh tier": "منتخبات كرة قدم وطنية يمنية من الدرجة السابعة",
    "yemeni national football teams sixth tier": "منتخبات كرة قدم وطنية يمنية من الدرجة السادسة",
    "yemeni national football teams third tier": "منتخبات كرة قدم وطنية يمنية من الدرجة الثالثة",
    "yemeni national football teams top tier": "منتخبات كرة قدم وطنية يمنية من الدرجة الأولى",
    "yemeni football teams fifth tier": "فرق كرة قدم يمنية من الدرجة الخامسة",
    "yemeni football teams first tier": "فرق كرة قدم يمنية من الدرجة الأولى",
    "yemeni football teams fourth tier": "فرق كرة قدم يمنية من الدرجة الرابعة",
    "yemeni football teams premier": "فرق كرة قدم يمنية من الدرجة الممتازة",
    "yemeni football teams second tier": "فرق كرة قدم يمنية من الدرجة الثانية",
    "yemeni football teams seventh tier": "فرق كرة قدم يمنية من الدرجة السابعة",
    "yemeni football teams sixth tier": "فرق كرة قدم يمنية من الدرجة السادسة",
    "yemeni football teams third tier": "فرق كرة قدم يمنية من الدرجة الثالثة",
    "yemeni football teams top tier": "فرق كرة قدم يمنية من الدرجة الأولى"
}

data_2 = {

}


@pytest.mark.parametrize("key,expected", data_1.items(), ids=data_1.keys())
@pytest.mark.fast
def test_sport_lab_with_nuder_1(key: str, expected: str) -> None:
    result2 = sport_lab_nat_load_new(key)
    assert result2 == expected


@pytest.mark.parametrize("key,expected", data_2.items(), ids=data_2.keys())
@pytest.mark.fast
def test_sport_lab_with_nuder_2(key: str, expected: str) -> None:
    result2 = sport_lab_nat_load_new(key)
    assert result2 == expected


to_test = [
    ("test_sport_lab_with_nuder_1", data_1),
    ("test_sport_lab_with_nuder_2", data_2),
]


@pytest.mark.parametrize("name,data", to_test)
@pytest.mark.dump
def test_dump_all(name: str, data: dict[str, str]) -> None:
    expected, diff_result = one_dump_test(data, sport_lab_nat_load_new)
    dump_diff(diff_result, name)

    # add_result = {x: v for x, v in data.items() if x in diff_result and "" == diff_result.get(x)}
    # dump_diff(add_result, f"{name}_empty")

    # add_result2 = {x: v for x, v in data.items() if x not in add_result}
    # dump_diff(add_result2, f"{name}_not_empty")

    assert diff_result == expected, f"Differences found: {len(diff_result):,}, len all :{len(data):,}"

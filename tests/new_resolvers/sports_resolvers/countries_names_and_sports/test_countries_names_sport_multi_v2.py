#
import pytest
from load_one_data import dump_diff, one_dump_test

from ArWikiCats.new_resolvers.sports_resolvers.countries_names_and_sports import (
    resolve_countries_names_sport,
)

test_data_1 = {
    "olympic gold medalists for the united states": "فائزون بميداليات ذهبية أولمبية من الولايات المتحدة",
    "olympic gold medalists for finland": "فائزون بميداليات ذهبية أولمبية من فنلندا",
    "olympic gold medalists for the united states in baseball": "فائزون بميداليات ذهبية أولمبية من الولايات المتحدة في كرة القاعدة",
    "olympic gold medalists for finland in baseball": "فائزون بميداليات ذهبية أولمبية من فنلندا في كرة القاعدة",
    "Category:Afghanistan Football Federation": "الاتحاد الأفغاني لكرة القدم",
    "Category:Aruba Football Federation": "الاتحاد الأروبي لكرة القدم",
    "Category:Bhutan Football Federation": "الاتحاد البوتاني لكرة القدم",
    "Olympic gold medalists for United States": "فائزون بميداليات ذهبية أولمبية من الولايات المتحدة",
    "Olympic gold medalists for United States in alpine skiing": "فائزون بميداليات ذهبية أولمبية من الولايات المتحدة في التزلج على المنحدرات الثلجية",
    "Category:Olympic gold medalists for United States in alpine skiing": "فائزون بميداليات ذهبية أولمبية من الولايات المتحدة في التزلج على المنحدرات الثلجية",
    "Category:Olympic gold medalists for the United States in football": "فائزون بميداليات ذهبية أولمبية من الولايات المتحدة في كرة القدم",
    # "yemen international soccer players": "لاعبو كرة قدم دوليون من اليمن",
    "yemen international soccer players": "لاعبو منتخب اليمن لكرة القدم",
    "fiji women's international rugby union players": "لاعبات اتحاد رجبي دوليات من فيجي",
    "france international women's rugby sevens players": "لاعبات سباعيات رجبي دوليات من فرنسا",
    "mali summer olympics football": "كرة قدم مالي في الألعاب الأولمبية الصيفية",
    "moldova football manager history": "تاريخ مدربو كرة قدم مولدوفا",
    "poland summer olympics football": "كرة قدم بولندا في الألعاب الأولمبية الصيفية",
    "yemen under-17 international basketball managers": "مدربو كرة سلة تحت 17 سنة دوليون من اليمن",
}


@pytest.mark.parametrize("category, expected", test_data_1.items(), ids=test_data_1.keys())
@pytest.mark.fast
def test_resolve_countries_names_sport(category: str, expected: str) -> None:
    label = resolve_countries_names_sport(category)
    assert label == expected


test_data_dump = [
    # ("test_resolve_countries_names_sport", test_data_1),
]


@pytest.mark.dump
@pytest.mark.parametrize("name,data", test_data_dump)
def test_dump_all(name: str, data: dict[str, str]) -> None:
    expected, diff_result = one_dump_test(data, resolve_countries_names_sport)

    dump_diff(diff_result, name)
    assert diff_result == expected, f"Differences found: {len(diff_result):,}, len all :{len(data):,}"

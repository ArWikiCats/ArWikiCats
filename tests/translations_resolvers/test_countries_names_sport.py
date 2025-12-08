#
import pytest
from load_one_data import dump_diff, one_dump_test
from ArWikiCats.translations_formats import FormatDataV2, MultiDataFormatterBaseV2
from ArWikiCats.translations_resolvers.countries_names_sport import resolve_countries_names_sport

test_data_1 = {
    "United States": "الولايات المتحدة",
    "Olympic gold medalists for United States": "فائزون بميداليات ذهبية أولمبية من الولايات المتحدة",
    "Olympic gold medalists for United States in alpine skiing":
        "فائزون بميداليات ذهبية أولمبية من الولايات المتحدة في التزلج على المنحدرات الثلجية",
    "Category:Olympic gold medalists for United States in alpine skiing":
        "تصنيف:فائزون بميداليات ذهبية أولمبية من الولايات المتحدة في التزلج على المنحدرات الثلجية",
    "Category:Olympic gold medalists for the United States in football":
        "تصنيف:فائزون بميداليات ذهبية أولمبية من الولايات المتحدة في كرة القدم",
}


@pytest.mark.parametrize("category, expected", test_data_1.items(), ids=list(test_data_1.keys()))
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

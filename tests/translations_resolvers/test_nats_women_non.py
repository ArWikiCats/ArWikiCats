"""
tests
"""

import pytest
from load_one_data import dump_diff, one_dump_test

from ArWikiCats.translations_resolvers.nats_women_non import nats_women_label
from ArWikiCats import resolve_arabic_category_label

all_test_data = {
    "non-american television series": "مسلسلات تلفزيونية غير أمريكية",
    "non american television series": "مسلسلات تلفزيونية غير أمريكية",
    "non yemeni television series": "مسلسلات تلفزيونية غير يمنية",
    "non-yemeni television series": "مسلسلات تلفزيونية غير يمنية",
}


@pytest.mark.parametrize("category, expected_key", all_test_data.items(), ids=list(all_test_data.keys()))
@pytest.mark.slow
def test_nats_women_label(category: str, expected_key: str) -> None:
    label2 = nats_women_label(category)
    assert label2 == expected_key


all_test_data = {
    "Category:Non-American television series based on American television series": "تصنيف:مسلسلات تلفزيونية غير أمريكية مبنية على مسلسلات تلفزيونية أمريكية",
    "Category:American television series based on non-American television series": "تصنيف:مسلسلات تلفزيونية أمريكية مبنية على مسلسلات تلفزيونية غير أمريكية",
    "Category:Australian television series based on non-Australian television series": "تصنيف:مسلسلات تلفزيونية أسترالية مبنية على مسلسلات تلفزيونية غير أسترالية",
    "Category:Austrian television series based on non-Austrian television series": "تصنيف:مسلسلات تلفزيونية نمساوية مبنية على مسلسلات تلفزيونية غير نمساوية",
    "Category:Belgian television series based on non-Belgian television series": "تصنيف:مسلسلات تلفزيونية بلجيكية مبنية على مسلسلات تلفزيونية غير بلجيكية",
    "Category:Brazilian television series based on non-Brazilian television series": "تصنيف:مسلسلات تلفزيونية برازيلية مبنية على مسلسلات تلفزيونية غير برازيلية",
    "Category:British television series based on non-British television series": "تصنيف:مسلسلات تلفزيونية بريطانية مبنية على مسلسلات تلفزيونية غير بريطانية",
    "Category:Bulgarian television series based on non-Bulgarian television series": "تصنيف:مسلسلات تلفزيونية بلغارية مبنية على مسلسلات تلفزيونية غير بلغارية",
    "Category:Canadian television series based on non-Canadian television series": "تصنيف:مسلسلات تلفزيونية كندية مبنية على مسلسلات تلفزيونية غير كندية",
    "Category:Chinese television series based on non-Chinese television series": "تصنيف:مسلسلات تلفزيونية صينية مبنية على مسلسلات تلفزيونية غير صينية",
    "Category:Croatian television series based on non-Croatian television series": "تصنيف:مسلسلات تلفزيونية كرواتية مبنية على مسلسلات تلفزيونية غير كرواتية",
    "Category:Czech television series based on non-Czech television series": "تصنيف:مسلسلات تلفزيونية تشيكية مبنية على مسلسلات تلفزيونية غير تشيكية",
    "Category:Dutch television series based on non-Dutch television series": "تصنيف:مسلسلات تلفزيونية هولندية مبنية على مسلسلات تلفزيونية غير هولندية",
    "Category:Estonian television series based on non-Estonian television series": "تصنيف:مسلسلات تلفزيونية إستونية مبنية على مسلسلات تلفزيونية غير إستونية",
    "Category:Finnish television series based on non-Finnish television series": "تصنيف:مسلسلات تلفزيونية فنلندية مبنية على مسلسلات تلفزيونية غير فنلندية",
    "Category:French television series based on non-French television series": "تصنيف:مسلسلات تلفزيونية فرنسية مبنية على مسلسلات تلفزيونية غير فرنسية",
    "Category:Georgia (country) television series based on non-Georgia (country) television series": "تصنيف:مسلسلات تلفزيونية جورجية مبنية على مسلسلات تلفزيونية غير جورجية",
    "Category:German television series based on non-German television series": "تصنيف:مسلسلات تلفزيونية ألمانية مبنية على مسلسلات تلفزيونية غير ألمانية",
    "Category:Hungarian television series based on non-Hungarian television series": "تصنيف:مسلسلات تلفزيونية مجرية مبنية على مسلسلات تلفزيونية غير مجرية",
    "Category:Indian television series based on non-Indian television series": "تصنيف:مسلسلات تلفزيونية هندية مبنية على مسلسلات تلفزيونية غير هندية",
    "Category:Indonesian television series based on non-Indonesian television series": "تصنيف:مسلسلات تلفزيونية إندونيسية مبنية على مسلسلات تلفزيونية غير إندونيسية",
    "Category:Irish television series based on non-Irish television series": "تصنيف:مسلسلات تلفزيونية أيرلندية مبنية على مسلسلات تلفزيونية غير أيرلندية",
    "Category:Israeli television series based on non-Israeli television series": "تصنيف:مسلسلات تلفزيونية إسرائيلية مبنية على مسلسلات تلفزيونية غير إسرائيلية",
    "Category:Italian television series based on non-Italian television series": "تصنيف:مسلسلات تلفزيونية إيطالية مبنية على مسلسلات تلفزيونية غير إيطالية",
    "Category:Japanese television series based on non-Japanese television series": "تصنيف:مسلسلات تلفزيونية يابانية مبنية على مسلسلات تلفزيونية غير يابانية",
    "Category:Lithuanian television series based on non-Lithuanian television series": "تصنيف:مسلسلات تلفزيونية ليتوانية مبنية على مسلسلات تلفزيونية غير ليتوانية",
    "Category:Malaysian television series based on non-Malaysian television series": "تصنيف:مسلسلات تلفزيونية ماليزية مبنية على مسلسلات تلفزيونية غير ماليزية",
    "Category:Mexican television series based on non-Mexican television series": "تصنيف:مسلسلات تلفزيونية مكسيكية مبنية على مسلسلات تلفزيونية غير مكسيكية",
    "Category:Non-Argentine television series based on Argentine television series": "تصنيف:مسلسلات تلفزيونية غير أرجنتينية مبنية على مسلسلات تلفزيونية أرجنتينية",
    "Category:Non-Australian television series based on Australian television series": "تصنيف:مسلسلات تلفزيونية غير أسترالية مبنية على مسلسلات تلفزيونية أسترالية",
    "Category:Non-British television series based on British television series": "تصنيف:مسلسلات تلفزيونية غير بريطانية مبنية على مسلسلات تلفزيونية بريطانية",
    "Category:Non-Canadian television series based on Canadian television series": "تصنيف:مسلسلات تلفزيونية غير كندية مبنية على مسلسلات تلفزيونية كندية",
    "Category:Non-Colombian television series based on Colombian television series": "تصنيف:مسلسلات تلفزيونية غير كولومبية مبنية على مسلسلات تلفزيونية كولومبية",
    "Category:Non-French television series based on French television series": "تصنيف:مسلسلات تلفزيونية غير فرنسية مبنية على مسلسلات تلفزيونية فرنسية",
    "Category:Non-Japanese television series based on Japanese television series": "تصنيف:مسلسلات تلفزيونية غير يابانية مبنية على مسلسلات تلفزيونية يابانية",
    "Category:Non-Pakistani television series based on Pakistani television series": "تصنيف:مسلسلات تلفزيونية غير باكستانية مبنية على مسلسلات تلفزيونية باكستانية",
    "Category:Non-South Korean television series based on South Korean television series": "تصنيف:مسلسلات تلفزيونية غير كورية جنوبية مبنية على مسلسلات تلفزيونية كورية جنوبية",
    "Category:Non-Spanish television series based on Spanish television series": "تصنيف:مسلسلات تلفزيونية غير إسبانية مبنية على مسلسلات تلفزيونية إسبانية",
    "Category:Non-Taiwanese television series based on Taiwanese television series": "تصنيف:مسلسلات تلفزيونية غير تايوانية مبنية على مسلسلات تلفزيونية تايوانية",
    "Category:Non-Turkish television series based on Turkish television series": "تصنيف:مسلسلات تلفزيونية غير تركية مبنية على مسلسلات تلفزيونية تركية",
    "Category:Pakistani television series based on non-Pakistani television series": "تصنيف:مسلسلات تلفزيونية باكستانية مبنية على مسلسلات تلفزيونية غير باكستانية",
    "Category:Philippine television series based on non-Philippine television series": "تصنيف:مسلسلات تلفزيونية فلبينية مبنية على مسلسلات تلفزيونية غير فلبينية",
    "Category:Portuguese television series based on non-Portuguese television series": "تصنيف:مسلسلات تلفزيونية برتغالية مبنية على مسلسلات تلفزيونية غير برتغالية",
    "Category:Romanian television series based on non-Romanian television series": "تصنيف:مسلسلات تلفزيونية رومانية مبنية على مسلسلات تلفزيونية غير رومانية",
    "Category:Russian television series based on non-Russian television series": "تصنيف:مسلسلات تلفزيونية روسية مبنية على مسلسلات تلفزيونية غير روسية",
    "Category:Singaporean television series based on non-Singaporean television series": "تصنيف:مسلسلات تلفزيونية سنغافورية مبنية على مسلسلات تلفزيونية غير سنغافورية",
    "Category:South Korean television series based on non-South Korean television series": "تصنيف:مسلسلات تلفزيونية كورية جنوبية مبنية على مسلسلات تلفزيونية غير كورية جنوبية",
    "Category:Spanish television series based on non-Spanish television series": "تصنيف:مسلسلات تلفزيونية إسبانية مبنية على مسلسلات تلفزيونية غير إسبانية",
    "Category:Taiwanese television series based on non-Taiwanese television series": "تصنيف:مسلسلات تلفزيونية تايوانية مبنية على مسلسلات تلفزيونية غير تايوانية",
    "Category:Turkish television series based on non-Turkish television series": "تصنيف:مسلسلات تلفزيونية تركية مبنية على مسلسلات تلفزيونية غير تركية",
    "Category:Uruguayan television series based on non-Uruguayan television series": "تصنيف:مسلسلات تلفزيونية أوروغويانية مبنية على مسلسلات تلفزيونية غير أوروغويانية",
    "Category:Vietnamese television series based on non-Vietnamese television series": "تصنيف:مسلسلات تلفزيونية فيتنامية مبنية على مسلسلات تلفزيونية غير فيتنامية",
}


data_series_empty = {
    "Category:New Zealand television series based on non-New Zealand television series": "x",
    "Category:Non-New Zealand television series based on New Zealand television series": "x",
    "Category:Non-Tamil-language television series based on Tamil-language television series": "x",
    "Category:Tamil-language television series based on non-Tamil-language television series": "x"
}


@pytest.mark.parametrize("category, expected_key", all_test_data.items(), ids=list(all_test_data.keys()))
@pytest.mark.slow
def test_with_resolve_arabic_category_label(category: str, expected_key: str) -> None:
    label2 = resolve_arabic_category_label(category)
    assert label2 == expected_key


to_test = [
    ("test_with_resolve_arabic_category_label", all_test_data),
]


@pytest.mark.parametrize("name,data", to_test)
@pytest.mark.dump
def test_non_dump(name: str, data: dict[str, str]) -> None:

    expected, diff_result = one_dump_test(data, resolve_arabic_category_label)

    dump_diff(diff_result, name)
    assert diff_result == expected, f"Differences found: {len(diff_result)}"

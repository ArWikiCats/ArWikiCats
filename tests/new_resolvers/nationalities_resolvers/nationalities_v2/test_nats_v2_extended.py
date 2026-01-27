"""
tests
"""

import pytest

from ArWikiCats import resolve_label_ar
from ArWikiCats.new_resolvers.nationalities_resolvers.nationalities_v2 import resolve_by_nats
from utils.dump_runner import make_dump_test_name_data_callback

all_test_data_integrated = {
    "Non-American television series based on American television series": "مسلسلات تلفزيونية غير أمريكية مبنية على مسلسلات تلفزيونية أمريكية",
    "American television series based on non-American television series": "مسلسلات تلفزيونية أمريكية مبنية على مسلسلات تلفزيونية غير أمريكية",
    "Australian television series based on non-Australian television series": "مسلسلات تلفزيونية أسترالية مبنية على مسلسلات تلفزيونية غير أسترالية",
    "Austrian television series based on non-Austrian television series": "مسلسلات تلفزيونية نمساوية مبنية على مسلسلات تلفزيونية غير نمساوية",
    "Belgian television series based on non-Belgian television series": "مسلسلات تلفزيونية بلجيكية مبنية على مسلسلات تلفزيونية غير بلجيكية",
    "Brazilian television series based on non-Brazilian television series": "مسلسلات تلفزيونية برازيلية مبنية على مسلسلات تلفزيونية غير برازيلية",
    "British television series based on non-British television series": "مسلسلات تلفزيونية بريطانية مبنية على مسلسلات تلفزيونية غير بريطانية",
    "Bulgarian television series based on non-Bulgarian television series": "مسلسلات تلفزيونية بلغارية مبنية على مسلسلات تلفزيونية غير بلغارية",
    "Canadian television series based on non-Canadian television series": "مسلسلات تلفزيونية كندية مبنية على مسلسلات تلفزيونية غير كندية",
    "Chinese television series based on non-Chinese television series": "مسلسلات تلفزيونية صينية مبنية على مسلسلات تلفزيونية غير صينية",
    "Croatian television series based on non-Croatian television series": "مسلسلات تلفزيونية كرواتية مبنية على مسلسلات تلفزيونية غير كرواتية",
    "Czech television series based on non-Czech television series": "مسلسلات تلفزيونية تشيكية مبنية على مسلسلات تلفزيونية غير تشيكية",
    "Dutch television series based on non-Dutch television series": "مسلسلات تلفزيونية هولندية مبنية على مسلسلات تلفزيونية غير هولندية",
    "Estonian television series based on non-Estonian television series": "مسلسلات تلفزيونية إستونية مبنية على مسلسلات تلفزيونية غير إستونية",
    "Finnish television series based on non-Finnish television series": "مسلسلات تلفزيونية فنلندية مبنية على مسلسلات تلفزيونية غير فنلندية",
    "French television series based on non-French television series": "مسلسلات تلفزيونية فرنسية مبنية على مسلسلات تلفزيونية غير فرنسية",
    "Georgia (country) television series based on non-Georgia (country) television series": "مسلسلات تلفزيونية جورجية مبنية على مسلسلات تلفزيونية غير جورجية",
    "German television series based on non-German television series": "مسلسلات تلفزيونية ألمانية مبنية على مسلسلات تلفزيونية غير ألمانية",
    "Hungarian television series based on non-Hungarian television series": "مسلسلات تلفزيونية مجرية مبنية على مسلسلات تلفزيونية غير مجرية",
    "Indian television series based on non-Indian television series": "مسلسلات تلفزيونية هندية مبنية على مسلسلات تلفزيونية غير هندية",
    "Indonesian television series based on non-Indonesian television series": "مسلسلات تلفزيونية إندونيسية مبنية على مسلسلات تلفزيونية غير إندونيسية",
    "Irish television series based on non-Irish television series": "مسلسلات تلفزيونية أيرلندية مبنية على مسلسلات تلفزيونية غير أيرلندية",
    "Israeli television series based on non-Israeli television series": "مسلسلات تلفزيونية إسرائيلية مبنية على مسلسلات تلفزيونية غير إسرائيلية",
    "Italian television series based on non-Italian television series": "مسلسلات تلفزيونية إيطالية مبنية على مسلسلات تلفزيونية غير إيطالية",
    "Japanese television series based on non-Japanese television series": "مسلسلات تلفزيونية يابانية مبنية على مسلسلات تلفزيونية غير يابانية",
    "Lithuanian television series based on non-Lithuanian television series": "مسلسلات تلفزيونية ليتوانية مبنية على مسلسلات تلفزيونية غير ليتوانية",
    "Malaysian television series based on non-Malaysian television series": "مسلسلات تلفزيونية ماليزية مبنية على مسلسلات تلفزيونية غير ماليزية",
    "Mexican television series based on non-Mexican television series": "مسلسلات تلفزيونية مكسيكية مبنية على مسلسلات تلفزيونية غير مكسيكية",
    "Non-Argentine television series based on Argentine television series": "مسلسلات تلفزيونية غير أرجنتينية مبنية على مسلسلات تلفزيونية أرجنتينية",
    "Non-Australian television series based on Australian television series": "مسلسلات تلفزيونية غير أسترالية مبنية على مسلسلات تلفزيونية أسترالية",
    "Non-British television series based on British television series": "مسلسلات تلفزيونية غير بريطانية مبنية على مسلسلات تلفزيونية بريطانية",
    "Non-Canadian television series based on Canadian television series": "مسلسلات تلفزيونية غير كندية مبنية على مسلسلات تلفزيونية كندية",
    "Non-Colombian television series based on Colombian television series": "مسلسلات تلفزيونية غير كولومبية مبنية على مسلسلات تلفزيونية كولومبية",
    "Non-French television series based on French television series": "مسلسلات تلفزيونية غير فرنسية مبنية على مسلسلات تلفزيونية فرنسية",
    "Non-Japanese television series based on Japanese television series": "مسلسلات تلفزيونية غير يابانية مبنية على مسلسلات تلفزيونية يابانية",
    "Non-Pakistani television series based on Pakistani television series": "مسلسلات تلفزيونية غير باكستانية مبنية على مسلسلات تلفزيونية باكستانية",
    "Non-South Korean television series based on South Korean television series": "مسلسلات تلفزيونية غير كورية جنوبية مبنية على مسلسلات تلفزيونية كورية جنوبية",
    "Non-Spanish television series based on Spanish television series": "مسلسلات تلفزيونية غير إسبانية مبنية على مسلسلات تلفزيونية إسبانية",
    "Non-Taiwanese television series based on Taiwanese television series": "مسلسلات تلفزيونية غير تايوانية مبنية على مسلسلات تلفزيونية تايوانية",
    "Non-Turkish television series based on Turkish television series": "مسلسلات تلفزيونية غير تركية مبنية على مسلسلات تلفزيونية تركية",
    "Pakistani television series based on non-Pakistani television series": "مسلسلات تلفزيونية باكستانية مبنية على مسلسلات تلفزيونية غير باكستانية",
    "Philippine television series based on non-Philippine television series": "مسلسلات تلفزيونية فلبينية مبنية على مسلسلات تلفزيونية غير فلبينية",
    "Portuguese television series based on non-Portuguese television series": "مسلسلات تلفزيونية برتغالية مبنية على مسلسلات تلفزيونية غير برتغالية",
    "Romanian television series based on non-Romanian television series": "مسلسلات تلفزيونية رومانية مبنية على مسلسلات تلفزيونية غير رومانية",
    "Russian television series based on non-Russian television series": "مسلسلات تلفزيونية روسية مبنية على مسلسلات تلفزيونية غير روسية",
    "Singaporean television series based on non-Singaporean television series": "مسلسلات تلفزيونية سنغافورية مبنية على مسلسلات تلفزيونية غير سنغافورية",
    "South Korean television series based on non-South Korean television series": "مسلسلات تلفزيونية كورية جنوبية مبنية على مسلسلات تلفزيونية غير كورية جنوبية",
    "Spanish television series based on non-Spanish television series": "مسلسلات تلفزيونية إسبانية مبنية على مسلسلات تلفزيونية غير إسبانية",
    "Taiwanese television series based on non-Taiwanese television series": "مسلسلات تلفزيونية تايوانية مبنية على مسلسلات تلفزيونية غير تايوانية",
    "Turkish television series based on non-Turkish television series": "مسلسلات تلفزيونية تركية مبنية على مسلسلات تلفزيونية غير تركية",
    "Uruguayan television series based on non-Uruguayan television series": "مسلسلات تلفزيونية أوروغويانية مبنية على مسلسلات تلفزيونية غير أوروغويانية",
    "Vietnamese television series based on non-Vietnamese television series": "مسلسلات تلفزيونية فيتنامية مبنية على مسلسلات تلفزيونية غير فيتنامية",
}


data_series_empty = {
    "New Zealand television series based on non-New Zealand television series": "x",
    "Non-New Zealand television series based on New Zealand television series": "x",
    "Non-Tamil-language television series based on Tamil-language television series": "x",
    "Tamil-language television series based on non-Tamil-language television series": "x",
}


@pytest.mark.parametrize(
    "category, expected_key", all_test_data_integrated.items(), ids=all_test_data_integrated.keys()
)
@pytest.mark.slow
def test_with_resolve_label_ar(category: str, expected_key: str) -> None:
    label2 = resolve_label_ar(category)
    assert label2 == expected_key


to_test = [
    ("test_with_resolve_label_ar", all_test_data_integrated, resolve_label_ar),
]

test_dump_all = make_dump_test_name_data_callback(to_test, run_same=True)

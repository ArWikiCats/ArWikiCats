"""
Tests for bys_new bot
"""

from __future__ import annotations

import pytest
from load_one_data import dump_diff, one_dump_test
from ArWikiCats.make_bots.o_bots.bys_new import resolve_by_labels

from ArWikiCats.translations.by_type import (
    by_of_fields,
    by_table_year,
    by_and_fields,
    by_or_fields,
    by_by_fields,
    by_musics,
    Music_By_table,
)

data1 = {
    "by country and country": "حسب البلد والبلد",
    "by country and city of setting": "حسب البلد ومدينة الأحداث",
    "by country and city of developer": "حسب البلد ومدينة التطوير",
    "by city": "حسب المدينة",
    "by country": "حسب البلد",
    "by year": "حسب السنة",
    "by city of developer": "حسب مدينة التطوير",
    "by organization": "حسب المنظمة",
    "by nonprofit organization": "حسب المؤسسات غير الربحية",
    "by organization or nonprofit organization": "حسب المنظمة أو المؤسسات غير الربحية",
}

by_table_all = {
    "by country and country subdivision": "حسب البلد وتقسيم البلد",
    "by country and country subdivisions": "حسب البلد وتقسيمات البلد",
    "by country and country-of-residence": "حسب البلد وبلد الإقامة",
    "by company and shipbuilding company": "حسب الشركة وشركة بناء السفن",
    "by organization and nonprofit organization": "حسب المنظمة والمؤسسات غير الربحية",
    "by organization and research organization": "حسب المنظمة ومنظمة البحوث",
    "by orientation and political orientation": "حسب التوجه والتوجه السياسي",
    "by religion and former religion": "حسب الدين والدين السابق",
    "by subdivision and country subdivision": "حسب التقسيم وتقسيم البلد",
    "by country or country subdivision": "حسب البلد أو تقسيم البلد",
    "by country or country subdivisions": "حسب البلد أو تقسيمات البلد",
    "by country or country-of-residence": "حسب البلد أو بلد الإقامة",
    "by company or shipbuilding company": "حسب الشركة أو شركة بناء السفن",
    "by organization or nonprofit organization": "حسب المنظمة أو المؤسسات غير الربحية",
    "by organization or research organization": "حسب المنظمة أو منظمة البحوث",
    "by orientation or political orientation": "حسب التوجه أو التوجه السياسي",
    "by religion or former religion": "حسب الدين أو الدين السابق",
    "by subdivision or country subdivision": "حسب التقسيم أو تقسيم البلد",
    "by country by country subdivision": "حسب البلد حسب تقسيم البلد",
    "by country by country subdivisions": "حسب البلد حسب تقسيمات البلد",
    "by country by country-of-residence": "حسب البلد حسب بلد الإقامة",
    "by company by shipbuilding company": "حسب الشركة حسب شركة بناء السفن",
    "by organization by nonprofit organization": "حسب المنظمة حسب المؤسسات غير الربحية",
    "by organization by research organization": "حسب المنظمة حسب منظمة البحوث",
    "by orientation by political orientation": "حسب التوجه حسب التوجه السياسي",
    "by religion by former religion": "حسب الدين حسب الدين السابق",
    "by subdivision by country subdivision": "حسب التقسيم حسب تقسيم البلد",
    "by city of shooting location": "x",
    "by continent of shooting location": "x",
    "by country of shooting location": "x",
    "by city of developer": "x",
    "by city of disestablishment": "x",
    "by city of reestablishment": "x",
    "by city of establishment": "x",
    "by city of setting location": "x",
    "by city of invention": "x",
    "by city of introduction": "x",
    "by city of formal description": "x",
    "by city of photographing": "x",
    "by city of completion": "x",
    "by date of shooting location": "x",
    "by date of developer": "x",
    "by date of location": "x",
    "by date of setting": "x",
    "by date of disestablishment": "x",
    "by date of reestablishment": "x",
    "by date of establishment": "x",
    "by date of setting location": "x",
    "by date of invention": "x",
    "by date of introduction": "x",
    "by date of formal description": "x",
    "by date of photographing": "x",
    "by date of completion": "x",
    "by country of developer": "x",
    "by country of disestablishment": "x",
    "by country of reestablishment": "x",
    "by country of establishment": "x",
    "by country of invention": "x",
    "by country of introduction": "x",
    "by country of formal description": "x",
    "by country of photographing": "x",
    "by country of completion": "x",
    "by continent of developer": "x",
    "by continent of location": "x",
    "by continent of disestablishment": "x",
    "by continent of reestablishment": "x",
    "by continent of establishment": "x",
    "by continent of setting location": "x",
    "by continent of invention": "x",
    "by continent of introduction": "x",
    "by continent of formal description": "x",
    "by continent of photographing": "x",
    "by continent of completion": "x",
    "by location of shooting location": "x",
    "by location of developer": "x",
    "by location of location": "x",
    "by location of setting": "x",
    "by location of disestablishment": "x",
    "by location of reestablishment": "x",
    "by location of establishment": "x",
    "by location of setting location": "x",
    "by location of invention": "x",
    "by location of introduction": "x",
    "by location of formal description": "x",
    "by location of photographing": "x",
    "by location of completion": "x",
    "by period of shooting location": "x",
    "by period of developer": "x",
    "by period of location": "x",
    "by period of disestablishment": "x",
    "by period of reestablishment": "x",
    "by period of establishment": "x",
    "by period of invention": "x",
    "by period of introduction": "x",
    "by period of formal description": "x",
    "by period of photographing": "x",
    "by period of completion": "x",
    "by time of shooting location": "x",
    "by time of developer": "x",
    "by time of location": "x",
    "by time of setting": "x",
    "by time of disestablishment": "x",
    "by time of reestablishment": "x",
    "by time of establishment": "x",
    "by time of setting location": "x",
    "by time of invention": "x",
    "by time of introduction": "x",
    "by time of formal description": "x",
    "by time of photographing": "x",
    "by time of completion": "x",
    "by year of shooting location": "x",
    "by year of developer": "x",
    "by year of location": "x",
    "by year of setting": "x",
    "by year of disestablishment": "x",
    "by year of reestablishment": "x",
    "by year of establishment": "x",
    "by year of setting location": "x",
    "by year of invention": "x",
    "by year of formal description": "x",
    "by decade of shooting location": "x",
    "by decade of developer": "x",
    "by decade of location": "x",
    "by decade of setting": "x",
    "by decade of disestablishment": "x",
    "by decade of reestablishment": "x",
    "by decade of establishment": "x",
    "by decade of setting location": "x",
    "by decade of invention": "x",
    "by decade of formal description": "x",
    "by decade of photographing": "x",
    "by decade of completion": "x",
    "by era of shooting location": "x",
    "by era of developer": "x",
    "by era of location": "x",
    "by era of setting": "x",
    "by era of disestablishment": "x",
    "by era of reestablishment": "x",
    "by era of establishment": "x",
    "by era of setting location": "x",
    "by era of invention": "x",
    "by era of introduction": "x",
    "by era of formal description": "x",
    "by era of photographing": "x",
    "by era of completion": "x",
    "by millennium of shooting location": "x",
    "by millennium of developer": "x",
    "by millennium of location": "x",
    "by millennium of setting": "x",
    "by millennium of disestablishment": "x",
    "by millennium of reestablishment": "x",
    "by millennium of establishment": "x",
    "by millennium of setting location": "x",
    "by millennium of invention": "x",
    "by millennium of introduction": "x",
    "by millennium of formal description": "x",
    "by millennium of photographing": "x",
    "by millennium of completion": "x",
    "by century of shooting location": "x",
    "by century of developer": "x",
    "by century of location": "x",
    "by century of setting": "x",
    "by century of disestablishment": "x",
    "by century of reestablishment": "x",
    "by century of establishment": "x",
    "by century of setting location": "x",
    "by century of invention": "x",
    "by century of introduction": "x",
    "by century of formal description": "x",
    "by century of photographing": "x",
    "by century of completion": "x",
    "by country and country of residence": "x",
    "by country or country of residence": "x",
    "by country by country of residence": ""
}

to_test = [
    ("test_bys_all", by_table_all),
    ("test_bys_new_1", data1),
    # ("test_by_table_year", by_table_year),
    # ("test_by_of_fields", by_of_fields),
    # ("test_by_and_fields", by_and_fields),
    # ("test_by_or_fields", by_or_fields),
    # ("test_by_by_fields", by_by_fields),
    # ("test_by_musics", by_musics),
    # ("test_music_by_table", Music_By_table),
]


@pytest.mark.parametrize("category, expected", by_table_all.items(), ids=by_table_all.keys())
@pytest.mark.skip2
def test_bys_all(category: str, expected: str) -> None:
    label = resolve_by_labels(category)
    assert label == expected, f"Failed for category: {category}"


@pytest.mark.parametrize("category, expected", data1.items(), ids=data1.keys())
@pytest.mark.skip2
def test_bys_new_1(category: str, expected: str) -> None:
    label = resolve_by_labels(category)
    assert label == expected, f"Failed for category: {category}"


@pytest.mark.parametrize("category, expected", by_table_year.items(), ids=by_table_year.keys())
@pytest.mark.skip2
def test_by_table_year(category: str, expected: str) -> None:
    label = resolve_by_labels(category)
    assert label == expected, f"Failed for category: {category}"


@pytest.mark.parametrize("category, expected", by_of_fields.items(), ids=by_of_fields.keys())
@pytest.mark.skip2
def test_by_of_fields(category: str, expected: str) -> None:
    label = resolve_by_labels(category)
    assert label == expected, f"Failed for category: {category}"


@pytest.mark.parametrize("name,data", to_test)
@pytest.mark.dump
def test_dump_all(name: str, data: dict[str, str]) -> None:
    expected, diff_result = one_dump_test(data, resolve_by_labels)
    dump_diff(diff_result, name)
    assert diff_result == expected, f"Differences found: {len(diff_result):,}, len all :{len(data):,}"

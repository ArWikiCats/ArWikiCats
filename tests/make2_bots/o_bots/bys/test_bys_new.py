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
    "by city of shooting location": "",
    "by continent of shooting location": "",
    "by country of shooting location": "",
    "by city of developer": "",
    "by city of disestablishment": "",
    "by city of reestablishment": "",
    "by city of establishment": "",
    "by city of setting location": "",
    "by city of invention": "",
    "by city of introduction": "",
    "by city of formal description": "",
    "by city of photographing": "",
    "by city of completion": "",
    "by date of shooting location": "",
    "by date of developer": "",
    "by date of location": "",
    "by date of setting": "",
    "by date of disestablishment": "",
    "by date of reestablishment": "",
    "by date of establishment": "",
    "by date of setting location": "",
    "by date of invention": "",
    "by date of introduction": "",
    "by date of formal description": "",
    "by date of photographing": "",
    "by date of completion": "",
    "by country of developer": "",
    "by country of disestablishment": "",
    "by country of reestablishment": "",
    "by country of establishment": "",
    "by country of invention": "",
    "by country of introduction": "",
    "by country of formal description": "",
    "by country of photographing": "",
    "by country of completion": "",
    "by continent of developer": "",
    "by continent of location": "",
    "by continent of disestablishment": "",
    "by continent of reestablishment": "",
    "by continent of establishment": "",
    "by continent of setting location": "",
    "by continent of invention": "",
    "by continent of introduction": "",
    "by continent of formal description": "",
    "by continent of photographing": "",
    "by continent of completion": "",
    "by location of shooting location": "",
    "by location of developer": "",
    "by location of location": "",
    "by location of setting": "",
    "by location of disestablishment": "",
    "by location of reestablishment": "",
    "by location of establishment": "",
    "by location of setting location": "",
    "by location of invention": "",
    "by location of introduction": "",
    "by location of formal description": "",
    "by location of photographing": "",
    "by location of completion": "",
    "by period of shooting location": "",
    "by period of developer": "",
    "by period of location": "",
    "by period of disestablishment": "",
    "by period of reestablishment": "",
    "by period of establishment": "",
    "by period of invention": "",
    "by period of introduction": "",
    "by period of formal description": "",
    "by period of photographing": "",
    "by period of completion": "",
    "by time of shooting location": "",
    "by time of developer": "",
    "by time of location": "",
    "by time of setting": "",
    "by time of disestablishment": "",
    "by time of reestablishment": "",
    "by time of establishment": "",
    "by time of setting location": "",
    "by time of invention": "",
    "by time of introduction": "",
    "by time of formal description": "",
    "by time of photographing": "",
    "by time of completion": "",
    "by year of shooting location": "",
    "by year of developer": "",
    "by year of location": "",
    "by year of setting": "",
    "by year of disestablishment": "",
    "by year of reestablishment": "",
    "by year of establishment": "",
    "by year of setting location": "",
    "by year of invention": "",
    "by year of formal description": "",
    "by decade of shooting location": "",
    "by decade of developer": "",
    "by decade of location": "",
    "by decade of setting": "",
    "by decade of disestablishment": "",
    "by decade of reestablishment": "",
    "by decade of establishment": "",
    "by decade of setting location": "",
    "by decade of invention": "",
    "by decade of formal description": "",
    "by decade of photographing": "",
    "by decade of completion": "",
    "by era of shooting location": "",
    "by era of developer": "",
    "by era of location": "",
    "by era of setting": "",
    "by era of disestablishment": "",
    "by era of reestablishment": "",
    "by era of establishment": "",
    "by era of setting location": "",
    "by era of invention": "",
    "by era of introduction": "",
    "by era of formal description": "",
    "by era of photographing": "",
    "by era of completion": "",
    "by millennium of shooting location": "",
    "by millennium of developer": "",
    "by millennium of location": "",
    "by millennium of setting": "",
    "by millennium of disestablishment": "",
    "by millennium of reestablishment": "",
    "by millennium of establishment": "",
    "by millennium of setting location": "",
    "by millennium of invention": "",
    "by millennium of introduction": "",
    "by millennium of formal description": "",
    "by millennium of photographing": "",
    "by millennium of completion": "",
    "by century of shooting location": "",
    "by century of developer": "",
    "by century of location": "",
    "by century of setting": "",
    "by century of disestablishment": "",
    "by century of reestablishment": "",
    "by century of establishment": "",
    "by century of setting location": "",
    "by century of invention": "",
    "by century of introduction": "",
    "by century of formal description": "",
    "by century of photographing": "",
    "by century of completion": "",
    "by country and country of residence": "",
    "by country or country of residence": "",
    "by country by country of residence": ""
}

to_test = [
    ("test_bys_all", by_table_all),
    ("test_bys_new_1", data1),
    ("test_by_table_year", by_table_year),
    ("test_by_of_fields", by_of_fields),
    ("test_by_and_fields", by_and_fields),
    ("test_by_or_fields", by_or_fields),
    ("test_by_by_fields", by_by_fields),
    ("test_by_musics", by_musics),
    ("test_music_by_table", Music_By_table),
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

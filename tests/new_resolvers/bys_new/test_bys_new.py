"""
Tests for bys_new bot
"""

from __future__ import annotations

import pytest
from load_one_data import dump_diff, one_dump_test
from ArWikiCats.new_resolvers.bys_new import resolve_by_labels

from ArWikiCats.translations.by_type import (
    _by_of_fields,
    _by_table_year,
)

data1 = {
    "by populated place and decade": "حسب المكان المأهول والعقد",
    "by populated place and year": "حسب المكان المأهول والسنة",
    "by city or city of sport": "حسب المدينة أو مدينة الرياضة",
    "by city by city of sport": "حسب المدينة حسب مدينة الرياضة",
    "by city and city of sport": "حسب المدينة ومدينة الرياضة",
    "by country and country": "حسب البلد والبلد",
    "by country and city of setting": "حسب البلد ومدينة الأحداث",
    "by country and city of developer": "حسب البلد ومدينة التطوير",
    "by city": "حسب المدينة",
    "by country": "حسب البلد",
    "by year": "حسب السنة",
    "by city of developer": "حسب مدينة التطوير",
    "by organization": "حسب المنظمة",
    "by nonprofit organization": "حسب المنظمات غير الربحية",
    "by organization or nonprofit organization": "حسب المنظمة أو المنظمات غير الربحية",
    "by organization by nonprofit organization": "حسب المنظمة حسب المنظمات غير الربحية",
    "by organization and nonprofit organization": "حسب المنظمة والمنظمات غير الربحية",
}

by_table_all = {
    "by country and country subdivision": "حسب البلد وتقسيم البلد",
    "by country and country subdivisions": "حسب البلد وتقسيمات البلد",
    "by country and country-of-residence": "حسب البلد وبلد الإقامة",
    "by company and shipbuilding company": "حسب الشركة وشركة بناء السفن",
    "by organization and research organization": "حسب المنظمة ومنظمة البحوث",
    "by orientation and political orientation": "حسب التوجه والتوجه السياسي",
    "by religion and former religion": "حسب الدين والدين السابق",
    "by subdivision and country subdivision": "حسب التقسيم وتقسيم البلد",
    "by country or country subdivision": "حسب البلد أو تقسيم البلد",
    "by country or country subdivisions": "حسب البلد أو تقسيمات البلد",
    "by country or country-of-residence": "حسب البلد أو بلد الإقامة",
    "by company or shipbuilding company": "حسب الشركة أو شركة بناء السفن",
    "by organization or research organization": "حسب المنظمة أو منظمة البحوث",
    "by orientation or political orientation": "حسب التوجه أو التوجه السياسي",
    "by religion or former religion": "حسب الدين أو الدين السابق",
    "by subdivision or country subdivision": "حسب التقسيم أو تقسيم البلد",
    "by country by country subdivision": "حسب البلد حسب تقسيم البلد",
    "by country by country subdivisions": "حسب البلد حسب تقسيمات البلد",
    "by country by country-of-residence": "حسب البلد حسب بلد الإقامة",
    "by company by shipbuilding company": "حسب الشركة حسب شركة بناء السفن",
    "by organization by research organization": "حسب المنظمة حسب منظمة البحوث",
    "by orientation by political orientation": "حسب التوجه حسب التوجه السياسي",
    "by religion by former religion": "حسب الدين حسب الدين السابق",
    "by subdivision by country subdivision": "حسب التقسيم حسب تقسيم البلد",

    "by city of shooting location": "حسب مدينة موقع التصوير",
    "by continent of shooting location": "حسب قارة موقع التصوير",
    "by country of shooting location": "حسب بلد موقع التصوير",
    "by city of developer": "حسب مدينة التطوير",
    "by city of disestablishment": "حسب مدينة الانحلال",
    "by city of reestablishment": "حسب مدينة إعادة التأسيس",
    "by city of establishment": "حسب مدينة التأسيس",
    "by city of setting location": "حسب مدينة موقع الأحداث",
    "by city of invention": "حسب مدينة الاختراع",
    "by city of introduction": "حسب مدينة الاستحداث",
    "by city of formal description": "حسب مدينة الوصف",
    "by city of photographing": "حسب مدينة التصوير",
    "by city of completion": "حسب مدينة الانتهاء",
    "by date of shooting location": "حسب تاريخ موقع التصوير",
    "by date of developer": "حسب تاريخ التطوير",
    "by date of location": "حسب تاريخ الموقع",
    "by date of setting": "حسب تاريخ الأحداث",
    "by date of disestablishment": "حسب تاريخ الانحلال",
    "by date of reestablishment": "حسب تاريخ إعادة التأسيس",
    "by date of establishment": "حسب تاريخ التأسيس",
    "by date of setting location": "حسب تاريخ موقع الأحداث",
    "by date of invention": "حسب تاريخ الاختراع",
    "by date of introduction": "حسب تاريخ الاستحداث",
    "by date of formal description": "حسب تاريخ الوصف",
    "by date of photographing": "حسب تاريخ التصوير",
    "by date of completion": "حسب تاريخ الانتهاء",
    "by country of developer": "حسب بلد التطوير",
    "by country of disestablishment": "حسب بلد الانحلال",
    "by country of reestablishment": "حسب بلد إعادة التأسيس",
    "by country of establishment": "حسب بلد التأسيس",
    "by country of invention": "حسب بلد الاختراع",
    "by country of introduction": "حسب بلد الاستحداث",
    "by country of formal description": "حسب بلد الوصف",
    "by country of photographing": "حسب بلد التصوير",
    "by country of completion": "حسب بلد الانتهاء",
    "by continent of developer": "حسب قارة التطوير",
    "by continent of location": "حسب قارة الموقع",
    "by continent of disestablishment": "حسب قارة الانحلال",
    "by continent of reestablishment": "حسب قارة إعادة التأسيس",
    "by continent of establishment": "حسب قارة التأسيس",
    "by continent of setting location": "حسب قارة موقع الأحداث",
    "by continent of invention": "حسب قارة الاختراع",
    "by continent of introduction": "حسب قارة الاستحداث",
    "by continent of formal description": "حسب قارة الوصف",
    "by continent of photographing": "حسب قارة التصوير",
    "by continent of completion": "حسب قارة الانتهاء",
    "by location of shooting location": "حسب موقع موقع التصوير",
    "by location of developer": "حسب موقع التطوير",
    "by location of location": "حسب موقع الموقع",
    "by location of setting": "حسب موقع الأحداث",
    "by location of disestablishment": "حسب موقع الانحلال",
    "by location of reestablishment": "حسب موقع إعادة التأسيس",
    "by location of establishment": "حسب موقع التأسيس",
    "by location of setting location": "حسب موقع موقع الأحداث",
    "by location of invention": "حسب موقع الاختراع",
    "by location of introduction": "حسب موقع الاستحداث",
    "by location of formal description": "حسب موقع الوصف",
    "by location of photographing": "حسب موقع التصوير",
    "by location of completion": "حسب موقع الانتهاء",
    "by period of shooting location": "حسب حقبة موقع التصوير",
    "by period of developer": "حسب حقبة التطوير",
    "by period of location": "حسب حقبة الموقع",
    "by period of disestablishment": "حسب حقبة الانحلال",
    "by period of reestablishment": "حسب حقبة إعادة التأسيس",
    "by period of establishment": "حسب حقبة التأسيس",
    "by period of invention": "حسب حقبة الاختراع",
    "by period of introduction": "حسب حقبة الاستحداث",
    "by period of formal description": "حسب حقبة الوصف",
    "by period of photographing": "حسب حقبة التصوير",
    "by period of completion": "حسب حقبة الانتهاء",
    "by time of shooting location": "حسب وقت موقع التصوير",
    "by time of developer": "حسب وقت التطوير",
    "by time of location": "حسب وقت الموقع",
    "by time of setting": "حسب وقت الأحداث",
    "by time of disestablishment": "حسب وقت الانحلال",
    "by time of reestablishment": "حسب وقت إعادة التأسيس",
    "by time of establishment": "حسب وقت التأسيس",
    "by time of setting location": "حسب وقت موقع الأحداث",
    "by time of invention": "حسب وقت الاختراع",
    "by time of introduction": "حسب وقت الاستحداث",
    "by time of formal description": "حسب وقت الوصف",
    "by time of photographing": "حسب وقت التصوير",
    "by time of completion": "حسب وقت الانتهاء",
    "by year of shooting location": "حسب سنة موقع التصوير",
    "by year of developer": "حسب سنة التطوير",
    "by year of location": "حسب سنة الموقع",
    "by year of setting": "حسب سنة الأحداث",
    "by year of disestablishment": "حسب سنة الانحلال",
    "by year of reestablishment": "حسب سنة إعادة التأسيس",
    "by year of establishment": "حسب سنة التأسيس",
    "by year of setting location": "حسب سنة موقع الأحداث",
    "by year of invention": "حسب سنة الاختراع",
    "by year of formal description": "حسب سنة الوصف",
    "by decade of shooting location": "حسب عقد موقع التصوير",
    "by decade of developer": "حسب عقد التطوير",
    "by decade of location": "حسب عقد الموقع",
    "by decade of setting": "حسب عقد الأحداث",
    "by decade of disestablishment": "حسب عقد الانحلال",
    "by decade of reestablishment": "حسب عقد إعادة التأسيس",
    "by decade of establishment": "حسب عقد التأسيس",
    "by decade of setting location": "حسب عقد موقع الأحداث",
    "by decade of invention": "حسب عقد الاختراع",
    "by decade of formal description": "حسب عقد الوصف",
    "by decade of photographing": "حسب عقد التصوير",
    "by decade of completion": "حسب عقد الانتهاء",
    "by era of shooting location": "حسب عصر موقع التصوير",
    "by era of developer": "حسب عصر التطوير",
    "by era of location": "حسب عصر الموقع",
    "by era of setting": "حسب عصر الأحداث",
    "by era of disestablishment": "حسب عصر الانحلال",
    "by era of reestablishment": "حسب عصر إعادة التأسيس",
    "by era of establishment": "حسب عصر التأسيس",
    "by era of setting location": "حسب عصر موقع الأحداث",
    "by era of invention": "حسب عصر الاختراع",
    "by era of introduction": "حسب عصر الاستحداث",
    "by era of formal description": "حسب عصر الوصف",
    "by era of photographing": "حسب عصر التصوير",
    "by era of completion": "حسب عصر الانتهاء",
    "by millennium of shooting location": "حسب ألفية موقع التصوير",
    "by millennium of developer": "حسب ألفية التطوير",
    "by millennium of location": "حسب ألفية الموقع",
    "by millennium of setting": "حسب ألفية الأحداث",
    "by millennium of disestablishment": "حسب ألفية الانحلال",
    "by millennium of reestablishment": "حسب ألفية إعادة التأسيس",
    "by millennium of establishment": "حسب ألفية التأسيس",
    "by millennium of setting location": "حسب ألفية موقع الأحداث",
    "by millennium of invention": "حسب ألفية الاختراع",
    "by millennium of introduction": "حسب ألفية الاستحداث",
    "by millennium of formal description": "حسب ألفية الوصف",
    "by millennium of photographing": "حسب ألفية التصوير",
    "by millennium of completion": "حسب ألفية الانتهاء",
    "by century of shooting location": "حسب قرن موقع التصوير",
    "by century of developer": "حسب قرن التطوير",
    "by century of location": "حسب قرن الموقع",
    "by century of setting": "حسب قرن الأحداث",
    "by century of disestablishment": "حسب قرن الانحلال",
    "by century of reestablishment": "حسب قرن إعادة التأسيس",
    "by century of establishment": "حسب قرن التأسيس",
    "by century of setting location": "حسب قرن موقع الأحداث",
    "by century of invention": "حسب قرن الاختراع",
    "by century of introduction": "حسب قرن الاستحداث",
    "by century of formal description": "حسب قرن الوصف",
    "by century of photographing": "حسب قرن التصوير",
    "by century of completion": "حسب قرن الانتهاء",
}

to_test = [
    ("test_bys_all", by_table_all),
    ("test_bys_new_1", data1),
]


@pytest.mark.parametrize("category, expected", by_table_all.items(), ids=by_table_all.keys())
@pytest.mark.fast
def test_bys_all(category: str, expected: str) -> None:
    label = resolve_by_labels(category)
    assert label == expected, f"Failed for category: {category}"


@pytest.mark.parametrize("category, expected", data1.items(), ids=data1.keys())
@pytest.mark.fast
def test_bys_new_1(category: str, expected: str) -> None:
    label = resolve_by_labels(category)
    assert label == expected, f"Failed for category: {category}"


@pytest.mark.parametrize("category, expected", _by_table_year.items(), ids=_by_table_year.keys())
@pytest.mark.slow
def test_by_table_year(category: str, expected: str) -> None:
    label = resolve_by_labels(category)
    assert label == expected, f"Failed for category: {category}"


@pytest.mark.parametrize("category, expected", _by_of_fields.items(), ids=_by_of_fields.keys())
@pytest.mark.slow
def test__by_of_fields(category: str, expected: str) -> None:
    label = resolve_by_labels(category)
    assert label == expected, f"Failed for category: {category}"


@pytest.mark.parametrize("name,data", to_test)
@pytest.mark.dump
def test_dump_all(name: str, data: dict[str, str]) -> None:
    expected, diff_result = one_dump_test(data, resolve_by_labels)
    dump_diff(diff_result, name)
    assert diff_result == expected, f"Differences found: {len(diff_result):,}, len all :{len(data):,}"

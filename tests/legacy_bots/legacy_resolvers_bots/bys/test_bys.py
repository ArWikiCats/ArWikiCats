"""Tests for :mod:`make_bots.bys`."""

from __future__ import annotations

import pytest

from ArWikiCats.legacy_bots.legacy_resolvers_bots.bys import get_by_label
from utils.dump_runner import make_dump_test_name_data_callback

by_label_data = {
    "africa by country": "إفريقيا حسب البلد",
    "alaska by populated place": "ألاسكا حسب المكان المأهول",
    "alberta by city": "ألبرتا حسب المدينة",
    "antarctica by country": "القارة القطبية الجنوبية حسب البلد",
    "asia by country": "آسيا حسب البلد",
    "asia by region": "آسيا حسب المنطقة",
    "australia by city": "أستراليا حسب المدينة",
    "australia by populated place": "أستراليا حسب المكان المأهول",
    "australia by state or territory": "أستراليا حسب الولاية أو الإقليم",
    "austria by city": "النمسا حسب المدينة",
    "belgium by region": "بلجيكا حسب المنطقة",
    "brazil by state": "البرازيل حسب الولاية",
    "budapest by line": "بودابست حسب الخط",
    "canada by province or territory": "كندا حسب المقاطعة أو الإقليم",
    "caribbean by country": "الكاريبي حسب البلد",
    "caribbean by dependent territory": "الكاريبي حسب الأقاليم التابعة",
    "china by city": "الصين حسب المدينة",
    "costa rica by firing squad": "كوستاريكا رميا بالرصاص",
    "czech republic by city": "التشيك حسب المدينة",
    "drug offenses by nationality": "جرائم المخدرات حسب الجنسية",
    "europe by country": "أوروبا حسب البلد",
    "illinois by populated place": "إلينوي حسب المكان المأهول",
    "india by state or union territory": "الهند حسب الولاية أو الإقليم الاتحادي",
    "ivory coast by subject": "ساحل العاج حسب الموضوع",
    "netherlands by city": "هولندا حسب المدينة",
    "netherlands by province": "هولندا حسب المقاطعة",
    "non-profit organizations by country": "منظمات غير ربحية حسب البلد",
    "north america by country": "أمريكا الشمالية حسب البلد",
    "oceania by country": "أوقيانوسيا حسب البلد",
    "peru by province": "بيرو حسب المقاطعة",
    "philippines by architectural style": "الفلبين حسب الطراز المعماري",
    "philippines by region": "الفلبين حسب المنطقة",
    "philippines by type": "الفلبين حسب الفئة",
    "politics by state": "سياسة حسب الولاية",
    "republic-of ireland by year": "جمهورية أيرلندا حسب السنة",
    "russia by city": "روسيا حسب المدينة",
    "slovenia by populated place": "سلوفينيا حسب المكان المأهول",
    "south africa by city": "جنوب إفريقيا حسب المدينة",
    "south america by country": "أمريكا الجنوبية حسب البلد",
    "soviet union by war": "الاتحاد السوفيتي حسب الحرب",
    "spain by autonomous community": "إسبانيا حسب الحكم الذاتي",
    "spain by populated place": "إسبانيا حسب المكان المأهول",
    "spain by year": "إسبانيا حسب السنة",
    "sri lanka by city": "سريلانكا حسب المدينة",
    "summer olympics by year": "الألعاب الأولمبية الصيفية حسب السنة",
    "sweden by diocese": "السويد حسب الأبرشية",
    "sweden by populated place": "السويد حسب المكان المأهول",
    "turkey by province": "تركيا حسب المقاطعة",
    "ukraine by firing squad": "أوكرانيا رميا بالرصاص",
    "ukraine by region": "أوكرانيا حسب المنطقة",
    "united kingdom by city": "المملكة المتحدة حسب المدينة",
    "united states by architectural style": "الولايات المتحدة حسب الطراز المعماري",
    "united states by century": "الولايات المتحدة حسب القرن",
    "united states by city": "الولايات المتحدة حسب المدينة",
    "united states by county": "الولايات المتحدة حسب المقاطعة",
    "united states by decade": "الولايات المتحدة حسب العقد",
    "united states by industry": "الولايات المتحدة حسب الصناعة",
    "united states by issue": "الولايات المتحدة حسب القضية",
    "united states by populated place": "الولايات المتحدة حسب المكان المأهول",
    "united states by school": "الولايات المتحدة حسب المدرسة",
    "united states by state or region": "الولايات المتحدة حسب الولاية أو المنطقة",
    "united states by state or territory": "الولايات المتحدة حسب الولاية أو الإقليم",
    "united states by state": "الولايات المتحدة حسب الولاية",
    "united states by team": "الولايات المتحدة حسب الفريق",
    "united states by time": "الولايات المتحدة حسب الوقت",
    "united states by year": "الولايات المتحدة حسب السنة",
    "utah by firing squad": "يوتا رميا بالرصاص",
    "western sahara by subject": "الصحراء الغربية حسب الموضوع",
    "winter olympics by year": "الألعاب الأولمبية الشتوية حسب السنة",
    "world-war-ii by nationality": "الحرب العالمية الثانية حسب الجنسية",
}

to_test = [
    ("test_get_by_label", by_label_data, get_by_label),
]


@pytest.mark.parametrize("category, expected", by_label_data.items(), ids=by_label_data.keys())
@pytest.mark.fast
def test_get_by_label(category: str, expected: str) -> None:
    label = get_by_label(category)
    assert label == expected, f"Failed for category: {category}"


test_dump_all = make_dump_test_name_data_callback(to_test, run_same=True)

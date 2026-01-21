""" """

from __future__ import annotations

import pytest

from ArWikiCats.new_resolvers.countries_names_resolvers.countries_names_v2 import resolve_by_countries_names_v2

test_army_data_1 = {
    "Unmanned military aircraft of Belgium": "طائرات عسكرية بدون طيار بلجيكية",
    "Unmanned military aircraft of Canada": "طائرات عسكرية بدون طيار كندية",
    "Unmanned military aircraft of Egypt": "طائرات عسكرية بدون طيار مصرية",
    "Unmanned military aircraft of Japan": "طائرات عسكرية بدون طيار يابانية",
    "Unmanned military aircraft of Pakistan": "طائرات عسكرية بدون طيار باكستانية",
    "Unmanned military aircraft of Spain": "طائرات عسكرية بدون طيار إسبانية",
    "Unmanned military aircraft of Sweden": "طائرات عسكرية بدون طيار سويدية",
    "Unmanned aerial vehicles of Brazil": "طائرات بدون طيار برازيلية",
    "Unmanned aerial vehicles of Egypt": "طائرات بدون طيار مصرية",
    "Unmanned aerial vehicles of Iraq": "طائرات بدون طيار عراقية",
    "Unmanned aerial vehicles of Mexico": "طائرات بدون طيار مكسيكية",
    "Unmanned aerial vehicles of Morocco": "طائرات بدون طيار مغربية",
    "Unmanned aerial vehicles of Norway": "طائرات بدون طيار نرويجية",
    "Unmanned aerial vehicles of Pakistan": "طائرات بدون طيار باكستانية",
    "Unmanned aerial vehicles of Spain": "طائرات بدون طيار إسبانية",
    "Unmanned aerial vehicles of Switzerland": "طائرات بدون طيار سويسرية",
    "Unmanned aerial vehicles of Thailand": "طائرات بدون طيار تايلندية",
    "Unmanned aerial vehicles of Yemen": "طائرات بدون طيار يمنية",
}

test_army_data_2 = {
    "Unmanned military aircraft of Austria": "طائرات عسكرية بدون طيار نمساوية",
    "Unmanned military aircraft of China": "طائرات عسكرية بدون طيار صينية",
    "Unmanned military aircraft of France": "طائرات عسكرية بدون طيار فرنسية",
    "Unmanned military aircraft of Germany": "طائرات عسكرية بدون طيار ألمانية",
    "Unmanned military aircraft of Greece": "طائرات عسكرية بدون طيار يونانية",
    "Unmanned military aircraft of India": "طائرات عسكرية بدون طيار هندية",
    "Unmanned military aircraft of Iran": "طائرات عسكرية بدون طيار إيرانية",
    "Unmanned military aircraft of Israel": "طائرات عسكرية بدون طيار إسرائيلية",
    "Unmanned military aircraft of Italy": "طائرات عسكرية بدون طيار إيطالية",
    "Unmanned military aircraft of Russia": "طائرات عسكرية بدون طيار روسية",
    "Unmanned military aircraft of Turkey": "طائرات عسكرية بدون طيار تركية",
    "Unmanned military aircraft of Ukraine": "طائرات عسكرية بدون طيار أوكرانية",
    "Unmanned aerial vehicles of Algeria": "طائرات بدون طيار جزائرية",
    "Unmanned aerial vehicles of Australia": "طائرات بدون طيار أسترالية",
    "Unmanned aerial vehicles of Austria": "طائرات بدون طيار نمساوية",
    "Unmanned aerial vehicles of Belarus": "طائرات بدون طيار بيلاروسية",
    "Unmanned aerial vehicles of Canada": "طائرات بدون طيار كندية",
    "Unmanned aerial vehicles of China": "طائرات بدون طيار صينية",
    "Unmanned aerial vehicles of France": "طائرات بدون طيار فرنسية",
    "Unmanned aerial vehicles of Germany": "طائرات بدون طيار ألمانية",
    "Unmanned aerial vehicles of Greece": "طائرات بدون طيار يونانية",
    "Unmanned aerial vehicles of India": "طائرات بدون طيار هندية",
    "Unmanned aerial vehicles of Indonesia": "طائرات بدون طيار إندونيسية",
    "Unmanned aerial vehicles of Iran": "طائرات بدون طيار إيرانية",
    "Unmanned aerial vehicles of Israel": "طائرات بدون طيار إسرائيلية",
    "Unmanned aerial vehicles of Italy": "طائرات بدون طيار إيطالية",
    "Unmanned aerial vehicles of Japan": "طائرات بدون طيار يابانية",
    "Unmanned aerial vehicles of Jordan": "طائرات بدون طيار أردنية",
    "Unmanned aerial vehicles of Poland": "طائرات بدون طيار بولندية",
    "Unmanned aerial vehicles of Russia": "طائرات بدون طيار روسية",
    "Unmanned aerial vehicles of Saudi Arabia": "طائرات بدون طيار سعودية",
    "Unmanned aerial vehicles of Tunisia": "طائرات بدون طيار تونسية",
    "Unmanned aerial vehicles of Turkey": "طائرات بدون طيار تركية",
    "Unmanned aerial vehicles of Ukraine": "طائرات بدون طيار أوكرانية",
    "Unmanned aerial vehicles of the Soviet Union": "طائرات بدون طيار سوفيتية",
    "Unmanned aerial vehicles of the United Arab Emirates": "طائرات بدون طيار إماراتية",
    "Unmanned aerial vehicles of the United Kingdom": "طائرات بدون طيار بريطانية",
    "Unmanned aerial vehicles of the United States": "طائرات بدون طيار أمريكية",
}


@pytest.mark.fast
@pytest.mark.parametrize("category,expected", test_army_data_1.items(), ids=test_army_data_1.keys())
def test_army_1(category: str, expected: str) -> None:
    result = resolve_by_countries_names_v2(category)
    assert result == expected


@pytest.mark.fast
@pytest.mark.parametrize("category,expected", test_army_data_2.items(), ids=test_army_data_2.keys())
def test_army_2(category: str, expected: str) -> None:
    result = resolve_by_countries_names_v2(category)
    assert result == expected

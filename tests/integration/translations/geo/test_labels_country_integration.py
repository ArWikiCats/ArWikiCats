"""
Integration tests for the get_and_label function in labels_country module.
Tests the function directly with real data (without the full resolve pipeline).
"""

from __future__ import annotations

import pytest

from ArWikiCats.translations.funcs import get_and_label

integration_data = {
    "Hong Kong and Macao": "هونغ كونغ وماكاو",
    "Labuan and Sarawak": "لابوان وساراواك",
    "Nova Scotia and Prince Edward Island": "نوفا سكوشا وجزيرة الأمير إدوارد",
    "Rwanda and Burundi": "رواندا وبوروندي",
    "Roman Republic and Roman Empire": "الجمهورية الرومانية والإمبراطورية الرومانية",
    "qatar and yemen": "قطر واليمن",
}


@pytest.mark.integration
@pytest.mark.parametrize("category,expected", integration_data.items(), ids=integration_data.keys())
def test_get_and_label_integration(category: str, expected: str) -> None:
    """Test get_and_label with real data for joined country/region names."""
    label = get_and_label(category)
    assert label == expected

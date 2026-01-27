"""
End-to-end tests for labels with joined country/region names.
Tests the full resolve pipeline with real category inputs.
"""

from __future__ import annotations

import pytest

from ArWikiCats import resolve_label_ar
from utils.dump_runner import make_dump_test_name_data_callback

e2e_data = {
    "Anglican bishops of Hong Kong and Macao": "أساقفة أنجليكيون من هونغ كونغ وماكاو",
    "Anglican bishops of Labuan and Sarawak": "أساقفة أنجليكيون من لابوان وساراواك",
    "Anglican bishops of Nova Scotia and Prince Edward Island": "أساقفة أنجليكيون من نوفا سكوشا وجزيرة الأمير إدوارد",
    "Anglican bishops of Rwanda and Burundi": "أساقفة أنجليكيون من رواندا وبوروندي",
    "Jews and Judaism in Roman Republic and Roman Empire": "اليهود واليهودية في الجمهورية الرومانية والإمبراطورية الرومانية",
}


@pytest.mark.e2e
@pytest.mark.parametrize("category,expected", e2e_data.items(), ids=e2e_data.keys())
def test_resolve_joined_entities_labels(category: str, expected: str) -> None:
    """Test full resolve pipeline for categories with joined country/region names."""
    label = resolve_label_ar(category)
    assert label == expected


# Dump test for data comparison
test_dump_joined_entities = make_dump_test_name_data_callback(
    [("e2e_data", e2e_data, resolve_label_ar)], run_same=True, just_dump=True
)

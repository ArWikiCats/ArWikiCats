"""
Unit tests for the get_and_label function in labels_country module.
"""

from __future__ import annotations

import pytest

from ArWikiCats import resolve_label_ar
from ArWikiCats.translations.funcs import get_and_label
from utils.dump_runner import make_dump_test_name_data_callback

integration_data = {
    "Hong Kong and Macao": "هونغ كونغ وماكاو",
    "Labuan and Sarawak": "لابوان وساراواك",
    "Nova Scotia and Prince Edward Island": "نوفا سكوشا وجزيرة الأمير إدوارد",
    "Rwanda and Burundi": "رواندا وبوروندي",
    "Roman Republic and Roman Empire": "الجمهورية الرومانية والإمبراطورية الرومانية",
}


@pytest.mark.parametrize("category,expected", integration_data.items(), ids=integration_data.keys())
def test_integration_data(category: str, expected: str) -> None:
    label = get_and_label(category)
    assert label == expected


e2e_data = {
    "Anglican bishops of Hong Kong and Macao": "أساقفة أنجليكيون من هونغ كونغ وماكاو",
    "Anglican bishops of Labuan and Sarawak": "أساقفة أنجليكيون من لابوان وساراواك",
    "Anglican bishops of Nova Scotia and Prince Edward Island": "أساقفة أنجليكيون من نوفا سكوشا وجزيرة الأمير إدوارد",
    "Anglican bishops of Rwanda and Burundi": "أساقفة أنجليكيون من رواندا وبوروندي",
    "Jews and Judaism in Roman Republic and Roman Empire": "اليهود واليهودية في الجمهورية الرومانية والإمبراطورية الرومانية",
}


@pytest.mark.parametrize("category,expected", e2e_data.items(), ids=e2e_data.keys())
@pytest.mark.fast
def test_get_and_label(category: str, expected: str) -> None:
    label = resolve_label_ar(category)
    assert label == expected


test_dump_all = make_dump_test_name_data_callback(
    [("e2e_data", e2e_data, resolve_label_ar)], run_same=True, just_dump=True
)


@pytest.mark.unit
def test_get_and_label_returns_joined_entities(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(
        "ArWikiCats.translations.funcs.get_from_new_p17_final",
        lambda name, _: {"artist": "فنان", "painter": "رسام"}.get(name, ""),
    )

    result = get_and_label("Artist and Painter")
    assert result == "فنان ورسام"

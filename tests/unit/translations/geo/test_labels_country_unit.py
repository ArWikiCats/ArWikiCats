"""
Unit tests for the get_and_label function in labels_country module.
"""

from __future__ import annotations

import pytest

from ArWikiCats.translations.funcs import get_and_label


@pytest.mark.unit
def test_get_and_label_returns_joined_entities(monkeypatch: pytest.MonkeyPatch) -> None:
    """Test that get_and_label joins two entities with 'and' correctly."""
    monkeypatch.setattr(
        "ArWikiCats.translations.funcs.get_from_new_p17_final",
        lambda name, _: {"artist": "فنان", "painter": "رسام"}.get(name, ""),
    )

    result = get_and_label("Artist and Painter")
    assert result == "فنان ورسام"

#
import pytest

from ArWikiCats.translations.geo.us_counties import (
    USA_PARTY_LABELS,
    _build_party_derived_keys,
)


@pytest.mark.unit
class TestUSCountiesHelpers:
    def test_build_party_derived_keys_skips_blank_labels(self) -> None:
        derived = _build_party_derived_keys({"Democratic Party": "الحزب الديمقراطي", "Blank Party": " "})

        assert "democratic party" in derived
        assert derived["democratic party members"] == "أعضاء الحزب الديمقراطي"
        assert "blank party" not in derived

    def test_get_party_labels_returns_copy(self) -> None:
        assert USA_PARTY_LABELS["democratic party"] == "الحزب الديمقراطي"

from __future__ import annotations

import pytest

from ArWikiCats.translations.geo import (
    Cities,
    labels_country,
    labels_country2,
)


@pytest.mark.unit
class TestCountryLabels:
    def test_country_label_index_contains_overrides(self) -> None:
        labels = labels_country.New_P17_Finall

        assert labels["indycar"] == "أندي كار"

    def test_country_admin_labels_include_suffix_variants(self) -> None:
        admin_labels = labels_country2.COUNTRY_ADMIN_LABELS

        assert admin_labels["luanda"] == "لواندا"
        assert admin_labels["luanda province"] == "مقاطعة لواندا"

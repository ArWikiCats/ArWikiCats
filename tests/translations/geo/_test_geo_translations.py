from __future__ import annotations

import pytest

from ArWikiCats.translations.geo import (
    Cities,
    labels_country,
    labels_country2,
)


@pytest.mark.unit
class TestCitiesModule:
    def test_get_city_translations_returns_copy(self) -> None:

        assert Cities.CITY_TRANSLATIONS_LOWER["jerusalem"] == "القدس"

    def test_city_label_patches_returns_copy(self) -> None:
        patches = Cities.get_city_label_patches()

        assert patches is not Cities.CITY_LABEL_PATCHES
        assert patches == Cities.CITY_LABEL_PATCHES


@pytest.mark.unit
class TestCountryLabels:
    def test_country_label_index_contains_overrides(self) -> None:
        labels = labels_country.COUNTRY_LABEL_INDEX_LOWER

        assert labels["indycar"] == "أندي كار"

    def test_country_label_index_lower_is_lowercase(self) -> None:
        lower_labels = labels_country.COUNTRY_LABEL_INDEX_LOWER

        assert all(key == key.lower() for key in lower_labels)

    def test_country_admin_labels_include_suffix_variants(self) -> None:
        admin_labels = labels_country2.COUNTRY_ADMIN_LABELS

        assert admin_labels["luanda"] == "لواندا"
        assert admin_labels["luanda province"] == "مقاطعة لواندا"

"""Tests for build_labels_country.py country label aggregation utilities."""

from collections.abc import MutableMapping

from ArWikiCats.translations.data_builders.build_labels_country import (
    _build_country_label_index,
    _handle_the_prefix,
    _make_japan_labels,
    _make_turkey_labels,
    setdefault_with_lowercased,
    update_with_lowercased,
)


class TestUpdateWithLowercased:
    """Tests for update_with_lowercased function."""

    def test_update_lowercases_keys(self) -> None:
        target: MutableMapping[str, str] = {}
        mapping = {"Cairo": "القاهرة", "London": "لندن"}

        update_with_lowercased(target, mapping)

        assert target["cairo"] == "القاهرة"
        assert target["london"] == "لندن"

    def test_update_skips_empty_values(self) -> None:
        target: MutableMapping[str, str] = {"existing": "موجود"}
        mapping = {"New": "", "Value": "قيمة"}

        update_with_lowercased(target, mapping)

        assert "new" not in target
        assert target["value"] == "قيمة"

    def test_update_overwrites_existing(self) -> None:
        target: MutableMapping[str, str] = {"key": "قديم"}
        mapping = {"Key": "جديد"}

        update_with_lowercased(target, mapping)

        assert target["key"] == "جديد"


class TestSetdefaultWithLowercased:
    """Tests for setdefault_with_lowercased function."""

    def test_setdefault_adds_missing_keys(self) -> None:
        target: MutableMapping[str, str] = {}
        mapping = {"Key": "قيمة"}

        setdefault_with_lowercased(target, mapping)

        assert target["key"] == "قيمة"

    def test_setdefault_skips_existing_keys(self) -> None:
        target: MutableMapping[str, str] = {"key": "_original"}
        mapping = {"Key": "جديد"}

        setdefault_with_lowercased(target, mapping)

        assert target["key"] == "_original"

    def test_setdefault_skips_empty_values(self) -> None:
        target: MutableMapping[str, str] = {}
        mapping = {"Empty": "", "Value": "قيمة"}

        setdefault_with_lowercased(target, mapping)

        assert "empty" not in target
        assert target["value"] == "قيمة"


class TestMakeJapanLabels:
    """Tests for _make_japan_labels function."""

    def test_creates_base_labels(self) -> None:
        data = {"Tokyo": "طوكيو", "Osaka": "أوساكا"}
        result = _make_japan_labels(data)

        assert result["tokyo"] == "طوكيو"
        assert result["osaka"] == "أوساكا"

    def test_creates_prefecture_variants(self) -> None:
        data = {"Hokkaido": "هوكايدو"}
        result = _make_japan_labels(data)

        assert result["hokkaido prefecture"] == "محافظة هوكايدو"

    def test_creates_region_variants(self) -> None:
        data = {"Kyoto": "كيوتو"}
        result = _make_japan_labels(data)

        assert result["kyoto region"] == "منطقة كيوتو"

    def test_skips_empty_labels(self) -> None:
        data = {"Valid": "صحيح", "Empty": ""}
        result = _make_japan_labels(data)

        assert "valid" in result
        assert "valid prefecture" in result
        assert "empty" not in result


class TestMakeTurkeyLabels:
    """Tests for _make_turkey_labels function."""

    def test_creates_base_labels(self) -> None:
        data = {"Istanbul": "إسطنبول", "Ankara": "أنقرة"}
        result = _make_turkey_labels(data)

        assert result["istanbul"] == "إسطنبول"
        assert result["ankara"] == "أنقرة"

    def test_creates_province_variants(self) -> None:
        data = {"Izmir": "إزمير"}
        result = _make_turkey_labels(data)

        assert result["izmir province"] == "محافظة إزمير"

    def test_creates_districts_variants(self) -> None:
        data = {"Bursa": "بورصة"}
        result = _make_turkey_labels(data)

        assert result["districts of bursa province"] == "أقضية محافظة بورصة"

    def test_skips_empty_labels(self) -> None:
        data = {"Valid": "صحيح", "Empty": ""}
        result = _make_turkey_labels(data)

        assert "valid" in result
        assert "valid province" in result
        assert "empty" not in result


class TestHandleThePrefix:
    """Tests for _handle_the_prefix function."""

    def test_creates_entries_without_the(self) -> None:
        label_index = {"the gambia": "غامبيا", "egypt": "مصر"}
        result = _handle_the_prefix(label_index)

        assert "gambia" in result
        assert result["gambia"] == "غامبيا"

    def test_skips_if_trimmed_key_exists(self) -> None:
        label_index = {"the netherlands": "هولندا", "netherlands": "هولندا"}
        result = _handle_the_prefix(label_index)

        assert "netherlands" not in result  # already exists

    def test_case_insensitive_matching(self) -> None:
        label_index = {"The Gambia": "غامبيا"}
        result = _handle_the_prefix(label_index)

        # The function preserves the original case after removing "the "
        assert "Gambia" in result

    def test_skips_empty_values(self) -> None:
        label_index = {"the empty": "", "valid": "صحيح"}
        result = _handle_the_prefix(label_index)

        assert "empty" not in result


class TestBuildCountryLabelIndex:
    """Tests for _build_country_label_index function."""

    def test_merges_all_sources(self) -> None:
        CITY_TRANSLATIONS_LOWER = {"cairo": "القاهرة"}
        all_country_ar = {"egypt": "مصر"}
        US_STATES = {}
        COUNTRY_LABEL_OVERRIDES = {}
        COUNTRY_ADMIN_LABELS = {}
        MAIN_REGION_TRANSLATIONS = {}
        raw_region_overrides = {}
        SECONDARY_REGION_TRANSLATIONS = {}
        INDIA_REGION_TRANSLATIONS = {}
        TAXON_TABLE = {}
        BASE_POP_FINAL_5 = {}

        result = _build_country_label_index(
            CITY_TRANSLATIONS_LOWER,
            all_country_ar,
            US_STATES,
            COUNTRY_LABEL_OVERRIDES,
            COUNTRY_ADMIN_LABELS,
            MAIN_REGION_TRANSLATIONS,
            raw_region_overrides,
            SECONDARY_REGION_TRANSLATIONS,
            INDIA_REGION_TRANSLATIONS,
            TAXON_TABLE,
            BASE_POP_FINAL_5,
        )

        assert "cairo" in result
        assert result["cairo"] == "القاهرة"

    def test_adds_specific_overrides(self) -> None:
        # Minimal setup for testing specific overrides
        result = _build_country_label_index(
            CITY_TRANSLATIONS_LOWER={},
            all_country_ar={},
            US_STATES={},
            COUNTRY_LABEL_OVERRIDES={},
            COUNTRY_ADMIN_LABELS={},
            MAIN_REGION_TRANSLATIONS={},
            raw_region_overrides={},
            SECONDARY_REGION_TRANSLATIONS={},
            INDIA_REGION_TRANSLATIONS={},
            TAXON_TABLE={},
            BASE_POP_FINAL_5={},
        )

        assert "indycar" in result
        assert result["indycar"] == "أندي كار"
        assert "motorsport" in result

    def test_adds_setdefault_entries(self) -> None:
        # Test that setdefault_with_lowercased is called for fallback tables
        CITY_TRANSLATIONS_LOWER = {}
        all_country_ar = {}
        US_STATES = {}
        COUNTRY_LABEL_OVERRIDES = {}
        COUNTRY_ADMIN_LABELS = {}
        MAIN_REGION_TRANSLATIONS = {}
        raw_region_overrides = {}
        SECONDARY_REGION_TRANSLATIONS = {}
        INDIA_REGION_TRANSLATIONS = {}
        TAXON_TABLE = {"taxon_key": "قيمة"}
        BASE_POP_FINAL_5 = {"pop_key": "سكان"}

        result = _build_country_label_index(
            CITY_TRANSLATIONS_LOWER,
            all_country_ar,
            US_STATES,
            COUNTRY_LABEL_OVERRIDES,
            COUNTRY_ADMIN_LABELS,
            MAIN_REGION_TRANSLATIONS,
            raw_region_overrides,
            SECONDARY_REGION_TRANSLATIONS,
            INDIA_REGION_TRANSLATIONS,
            TAXON_TABLE,
            BASE_POP_FINAL_5,
        )

        # These should be added via setdefault (not overwriting existing)
        assert result["taxon_key"] == "قيمة"
        assert result["pop_key"] == "سكان"

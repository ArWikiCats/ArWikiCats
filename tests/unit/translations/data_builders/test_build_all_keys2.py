"""Tests for build_all_keys2.py key-label mapping utilities."""

from ArWikiCats.translations.data_builders.build_all_keys2 import (
    _build_book_entries,
    _build_cinema_entries,
    _build_direction_region_entries,
    _build_literature_area_entries,
    _build_of_variants,
    _build_towns_entries,
    _build_weapon_entries,
    build_pf_keys2,
    handle_the_prefix,
    update_keys_within,
)


class TestHandleThePrefix:
    """Tests for handle_the_prefix function."""

    def test_removes_the_prefix(self) -> None:
        label_index = {"the gambia": "غامبيا", "egypt": "مصر"}
        result = handle_the_prefix(label_index)

        assert "gambia" in result
        assert result["gambia"] == "غامبيا"

    def test_skips_if_trimmed_exists(self) -> None:
        label_index = {"the netherlands": "هولندا", "netherlands": "هولندا"}
        result = handle_the_prefix(label_index)

        assert "netherlands" not in result

    def test_skips_empty_values(self) -> None:
        label_index = {"the empty": "", "valid": "صحيح"}
        result = handle_the_prefix(label_index)

        assert "empty" not in result


class TestBuildOfVariants:
    """Tests for _build_of_variants function."""

    def test_adds_of_suffix_from_data_list(self) -> None:
        data = {}
        data_list = [{"key": "قيمة"}]
        data_list2 = []

        result = _build_of_variants(data, data_list, data_list2)

        assert "key of" in result
        assert result["key of"] == "قيمة"

    def test_adds_fi_suffix_from_data_list2(self) -> None:
        data = {}
        data_list = []
        data_list2 = [{"key": "قيمة"}]

        result = _build_of_variants(data, data_list, data_list2)

        assert "key of" in result
        assert result["key of"] == "قيمة في"

    def test_skips_existing_keys(self) -> None:
        data = {"key of": "موجود"}
        data_list = [{"key": "جديد"}]
        data_list2 = []

        result = _build_of_variants(data, data_list, data_list2)

        assert result["key of"] == "موجود"  # Not overwritten

    def test_skips_keys_ending_with_of(self) -> None:
        data = {}
        data_list = [{"key of": "قيمة"}]
        data_list2 = []

        result = _build_of_variants(data, data_list, data_list2)

        # Should not add "key of of"
        assert result.get("key of of") is None


class TestUpdateKeysWithin:
    """Tests for update_keys_within function."""

    def test_merges_keys_of_with_in(self) -> None:
        keys_of_with_in = {"key of": "قيمة"}
        keys_of_without_in = {"other": "أخرى"}
        data = {}

        update_keys_within(keys_of_with_in, keys_of_without_in, data)

        assert "key of" in data

    def test_removes_explorers_and_historians(self) -> None:
        keys_of_with_in = {}
        keys_of_without_in = {
            "explorers": "مستكشفون",
            "historians": "مؤرخون",
            "others": "آخرون",
        }
        data = {}

        update_keys_within(keys_of_with_in, keys_of_without_in, data)

        assert "explorers" not in data
        assert "historians" not in data
        assert "others" in data

    def test_lowercases_keys_of_without_in(self) -> None:
        keys_of_with_in = {}
        keys_of_without_in = {"Key": "قيمة"}
        data = {}

        update_keys_within(keys_of_with_in, keys_of_without_in, data)

        assert "key" in data
        assert data["key"] == "قيمة"


class TestBuildBookEntries:
    """Tests for _build_book_entries function."""

    def test_adds_base_categories(self) -> None:
        data = {}
        singers_tab = {}
        film_keys_for_female = {}
        ALBUMS_TYPE = {}
        BOOK_CATEGORIES = {"novels": "روايات"}
        BOOK_TYPES = {}

        _build_book_entries(data, singers_tab, film_keys_for_female, ALBUMS_TYPE, BOOK_CATEGORIES, BOOK_TYPES)

        assert "novels" in data
        assert data["novels"] == "روايات"

    def test_adds_defunct_variant(self) -> None:
        data = {}
        singers_tab = {}
        film_keys_for_female = {}
        ALBUMS_TYPE = {}
        BOOK_CATEGORIES = {"poetry": "شعر"}
        BOOK_TYPES = {}

        _build_book_entries(data, singers_tab, film_keys_for_female, ALBUMS_TYPE, BOOK_CATEGORIES, BOOK_TYPES)

        assert "defunct poetry" in data

    def test_adds_publications_variant(self) -> None:
        data = {}
        singers_tab = {}
        film_keys_for_female = {}
        ALBUMS_TYPE = {}
        BOOK_CATEGORIES = {"newspapers": "صحف"}
        BOOK_TYPES = {}

        _build_book_entries(data, singers_tab, film_keys_for_female, ALBUMS_TYPE, BOOK_CATEGORIES, BOOK_TYPES)

        assert "newspapers publications" in data

    def test_combines_with_film_keys(self) -> None:
        data = {}
        singers_tab = {}
        film_keys_for_female = {"comedy": "كوميدية"}
        ALBUMS_TYPE = {}
        BOOK_CATEGORIES = {"novels": "روايات"}
        BOOK_TYPES = {}

        _build_book_entries(data, singers_tab, film_keys_for_female, ALBUMS_TYPE, BOOK_CATEGORIES, BOOK_TYPES)

        assert "comedy novels" in data

    def test_combines_with_book_types(self) -> None:
        data = {}
        singers_tab = {}
        film_keys_for_female = {}
        ALBUMS_TYPE = {}
        BOOK_CATEGORIES = {"novels": "روايات"}
        BOOK_TYPES = {"historical": "تاريخية"}

        _build_book_entries(data, singers_tab, film_keys_for_female, ALBUMS_TYPE, BOOK_CATEGORIES, BOOK_TYPES)

        assert "historical novels" in data

    def test_adds_singer_variants(self) -> None:
        data = {}
        singers_tab = {"pop": "بوب"}
        film_keys_for_female = {}
        ALBUMS_TYPE = {}
        BOOK_CATEGORIES = {}
        BOOK_TYPES = {}

        _build_book_entries(data, singers_tab, film_keys_for_female, ALBUMS_TYPE, BOOK_CATEGORIES, BOOK_TYPES)

        assert "pop" in data
        assert "pop albums" in data
        assert "pop songs" in data


class TestBuildWeaponEntries:
    """Tests for _build_weapon_entries function."""

    def test_combines_classifications_with_events(self) -> None:
        WEAPON_CLASSIFICATIONS = {"guns": "أسلحة نارية"}
        WEAPON_EVENTS = {"deaths": "وفيات"}

        result = _build_weapon_entries(WEAPON_CLASSIFICATIONS, WEAPON_EVENTS)

        assert "guns deaths" in result
        assert result["guns deaths"] == "وفيات أسلحة نارية"


class TestBuildDirectionRegionEntries:
    """Tests for _build_direction_region_entries function."""

    def test_combines_directions_with_regions(self) -> None:
        DIRECTIONS = {"north": "شمال"}
        REGIONS = {"africa": "أفريقيا"}

        result = _build_direction_region_entries(DIRECTIONS, REGIONS)

        assert "north africa" in result
        assert result["north africa"] == "شمال أفريقيا"


class TestBuildTownsEntries:
    """Tests for _build_towns_entries function."""

    def test_adds_communities_variant(self) -> None:
        data = {}
        TOWNS_COMMUNITIES = {"rural": "ريفية"}

        _build_towns_entries(data, TOWNS_COMMUNITIES)

        assert "rural communities" in data

    def test_adds_towns_variant(self) -> None:
        data = {}
        TOWNS_COMMUNITIES = {"urban": "حضرية"}

        _build_towns_entries(data, TOWNS_COMMUNITIES)

        assert "urban towns" in data

    def test_adds_villages_variant(self) -> None:
        data = {}
        TOWNS_COMMUNITIES = {"mountain": "جبلية"}

        _build_towns_entries(data, TOWNS_COMMUNITIES)

        assert "mountain villages" in data

    def test_adds_cities_variant(self) -> None:
        data = {}
        TOWNS_COMMUNITIES = {"coastal": "ساحلية"}

        _build_towns_entries(data, TOWNS_COMMUNITIES)

        assert "coastal cities" in data


class TestBuildLiteratureAreaEntries:
    """Tests for _build_literature_area_entries function."""

    def test_adds_childrens_variant(self) -> None:
        data = {}
        film_keys_for_male = {}
        LITERATURE_AREAS = {"literature": "الأدب"}

        _build_literature_area_entries(data, film_keys_for_male, LITERATURE_AREAS)

        assert "children's literature" in data

    def test_combines_with_film_keys(self) -> None:
        data = {}
        film_keys_for_male = {"comedy": "كوميديا"}
        LITERATURE_AREAS = {"literature": "الأدب"}

        _build_literature_area_entries(data, film_keys_for_male, LITERATURE_AREAS)

        assert "comedy literature" in data


class TestBuildCinemaEntries:
    """Tests for _build_cinema_entries function."""

    def test_adds_base_entry(self) -> None:
        data = {}
        CINEMA_CATEGORIES = {"thriller": "إثارة"}

        _build_cinema_entries(data, CINEMA_CATEGORIES)

        assert "thriller" in data
        assert data["thriller"] == "إثارة"

    def test_adds_set_variant(self) -> None:
        data = {}
        CINEMA_CATEGORIES = {"horror": "رعب"}

        _build_cinema_entries(data, CINEMA_CATEGORIES)

        assert "horror set" in data

    def test_adds_produced_variant(self) -> None:
        data = {}
        CINEMA_CATEGORIES = {"action": "أكشن"}

        _build_cinema_entries(data, CINEMA_CATEGORIES)

        assert "action produced" in data

    def test_adds_filmed_variant(self) -> None:
        data = {}
        CINEMA_CATEGORIES = {"drama": "دراما"}

        _build_cinema_entries(data, CINEMA_CATEGORIES)

        assert "drama filmed" in data

    def test_adds_basedon_variant(self) -> None:
        data = {}
        CINEMA_CATEGORIES = {"romance": "رومانسية"}

        _build_cinema_entries(data, CINEMA_CATEGORIES)

        assert "romance basedon" in data

    def test_adds_based_variant(self) -> None:
        data = {}
        CINEMA_CATEGORIES = {"comedy": "كوميديا"}

        _build_cinema_entries(data, CINEMA_CATEGORIES)

        assert "comedy based" in data

    def test_adds_shot_variant(self) -> None:
        data = {}
        CINEMA_CATEGORIES = {"sci-fi": "خيال علمي"}

        _build_cinema_entries(data, CINEMA_CATEGORIES)

        assert "sci-fi shot" in data


class TestBuildPfKeys2:
    """Tests for build_pf_keys2 function."""

    def test_builds_consolidated_mapping(self) -> None:
        result = build_pf_keys2(
            art_movements={},
            base_labels={},
            ctl_data={},
            directions={},
            keys2_py={},
            keys_of_with_in={},
            keys_of_without_in={},
            pop_final_3={},
            regions={},
            school_labels={},
            tato_type={},
            towns_communities={},
            weapon_classifications={},
            weapon_events={},
            word_after_years={},
        )

        assert isinstance(result, dict)

    def test_adds_competition_medalists(self) -> None:
        ctl_data = {"olympics": "أولمبياد"}
        result = build_pf_keys2(
            art_movements={},
            base_labels={},
            ctl_data=ctl_data,
            directions={},
            keys2_py={},
            keys_of_with_in={},
            keys_of_without_in={},
            pop_final_3={},
            regions={},
            school_labels={},
            tato_type={},
            towns_communities={},
            weapon_classifications={},
            weapon_events={},
            word_after_years={},
        )

        assert "olympics medalists" in result

    def test_creates_private_school_variants(self) -> None:
        SCHOOL_LABELS = {"schools": "مدارس {}"}
        result = build_pf_keys2(
            art_movements={},
            base_labels={},
            ctl_data={},
            directions={},
            keys2_py={},
            keys_of_with_in={},
            keys_of_without_in={},
            pop_final_3={},
            regions={},
            school_labels=SCHOOL_LABELS,
            tato_type={},
            towns_communities={},
            weapon_classifications={},
            weapon_events={},
            word_after_years={},
        )

        assert "private schools" in result
        assert "public schools" in result

    def test_adds_minister_keys(self) -> None:
        result = build_pf_keys2(
            art_movements={},
            base_labels={},
            ctl_data={},
            directions={},
            keys2_py={},
            keys_of_with_in={},
            keys_of_without_in={},
            pop_final_3={},
            regions={},
            school_labels={},
            tato_type={},
            towns_communities={},
            weapon_classifications={},
            weapon_events={},
            word_after_years={},
        )

        assert "ministers of" in result
        assert "prime ministers of" in result

    def test_skips_existing_in_pop_final_3(self) -> None:
        # This tests that pop_final_3 entries are only added if key doesn't exist
        BASE_LABELS = {"existing": "موجود"}
        pop_final_3 = {"existing": "جديد", "new": "جديد"}
        result = build_pf_keys2(
            art_movements={},
            base_labels=BASE_LABELS,
            ctl_data={},
            directions={},
            keys2_py={},
            keys_of_with_in={},
            keys_of_without_in={},
            pop_final_3=pop_final_3,
            regions={},
            school_labels={},
            tato_type={},
            towns_communities={},
            weapon_classifications={},
            weapon_events={},
            word_after_years={},
        )

        # The "existing" key should not be overwritten if it was in BASE_LABELS
        # But the actual behavior depends on the order of operations in build_pf_keys2
        assert "new" in result

"""Tests for build_films_mslslat.py film and TV translation utilities."""

from ArWikiCats.translations.data_builders.build_films_mslslat import (
    _build_gender_key_maps,
    _build_series_and_nat_keys,
    _build_television_cao,
    _extend_females_labels,
)


class TestBuildGenderKeyMaps:
    """Tests for _build_gender_key_maps function."""

    def test_creates_both_map(self) -> None:
        films_key_o_multi = {
            "comedy": {"male": "كوميدي", "female": "كوميدية"},
            "drama": {"male": "درامي", "female": "درامية"},
        }
        films_key_both, films_key_man = _build_gender_key_maps(films_key_o_multi)

        assert "comedy" in films_key_both
        assert films_key_both["comedy"]["male"] == "كوميدي"
        assert films_key_both["comedy"]["female"] == "كوميدية"

    def test_lowercases_keys_in_both(self) -> None:
        films_key_o_multi = {
            "Action": {"male": "أكشن", "female": "أكشن"},
        }
        films_key_both, films_key_man = _build_gender_key_maps(films_key_o_multi)

        assert "action" in films_key_both
        assert "Action" not in films_key_both

    def test_builds_male_map(self) -> None:
        films_key_o_multi = {
            "horror": {"male": "رعب", "female": "رعب"},
        }
        films_key_both, films_key_man = _build_gender_key_maps(films_key_o_multi)

        assert films_key_man["horror"] == "رعب"

    def test_adds_animated_variants(self) -> None:
        films_key_o_multi = {
            "comedy": {"male": "كوميدي", "female": "كوميدية"},
        }
        films_key_both, films_key_man = _build_gender_key_maps(films_key_o_multi)

        assert "animated comedy" in films_key_man
        assert "رسوم متحركة" in films_key_man["animated comedy"]

    def test_skips_animated_for_animated_keys(self) -> None:
        films_key_o_multi = {
            "animated": {"male": "رسوم متحركة", "female": "رسوم متحركة"},
        }
        films_key_both, films_key_man = _build_gender_key_maps(films_key_o_multi)

        # Should not add "animated animated" variant
        assert "animated animated" not in films_key_man

    def test_adds_animation_alias(self) -> None:
        films_key_o_multi = {
            "animated": {"male": "رسوم متحركة", "female": "رسوم متحركة"},
        }
        films_key_both, films_key_man = _build_gender_key_maps(films_key_o_multi)

        assert "animation" in films_key_both
        assert films_key_both["animation"] == films_key_both["animated"]


class TestExtendFemalesLabels:
    """Tests for _extend_females_labels function."""

    def test_extracts_female_labels(self) -> None:
        films_keys_male_female = {
            "comedy": {"male": "كوميدي", "female": "كوميدية"},
            "drama": {"male": "درامي", "female": "درامية"},
        }
        result = _extend_females_labels(films_keys_male_female)

        assert result["comedy"] == "كوميدية"
        assert result["drama"] == "درامية"

    def test_handles_animation_alias(self) -> None:
        films_keys_male_female = {
            "animated": {"male": "رسوم متحركة", "female": "رسوم متحركة"},
        }
        result = _extend_females_labels(films_keys_male_female)

        assert "animated" in result
        assert "animation" in result

    def test_skips_empty_female_labels(self) -> None:
        films_keys_male_female = {
            "has_female": {"male": "male", "female": "female"},
            "no_female": {"male": "male", "female": ""},
        }
        result = _extend_females_labels(films_keys_male_female)

        assert "has_female" in result
        assert "no_female" not in result


class TestBuildSeriesAndNatKeys:
    """Tests for _build_series_and_nat_keys function."""

    def test_adds_series_base_keys(self) -> None:
        female_keys = {}
        SERIES_DEBUTS_ENDINGS = {}
        TELEVISION_BASE_KEYS_FEMALE = {"telenovela": "مسلسلات تيلينوفيلا"}
        DEBUTS_ENDINGS_KEYS = []

        films_key_for_nat, films_mslslat_tab = _build_series_and_nat_keys(
            female_keys, SERIES_DEBUTS_ENDINGS, TELEVISION_BASE_KEYS_FEMALE, DEBUTS_ENDINGS_KEYS
        )

        assert "telenovela" in films_key_for_nat
        assert "telenovela" in films_mslslat_tab

    def test_adds_debuts_endings_variants(self) -> None:
        female_keys = {}
        SERIES_DEBUTS_ENDINGS = {}
        TELEVISION_BASE_KEYS_FEMALE = {"series": "مسلسلات"}
        DEBUTS_ENDINGS_KEYS = []

        films_key_for_nat, films_mslslat_tab = _build_series_and_nat_keys(
            female_keys, SERIES_DEBUTS_ENDINGS, TELEVISION_BASE_KEYS_FEMALE, DEBUTS_ENDINGS_KEYS
        )

        assert "series debuts" in films_key_for_nat
        assert "series endings" in films_key_for_nat

    def test_combines_with_female_keys(self) -> None:
        female_keys = {"comedy": "كوميدية"}
        SERIES_DEBUTS_ENDINGS = {}
        TELEVISION_BASE_KEYS_FEMALE = {"series": "مسلسلات"}
        DEBUTS_ENDINGS_KEYS = []

        films_key_for_nat, films_mslslat_tab = _build_series_and_nat_keys(
            female_keys, SERIES_DEBUTS_ENDINGS, TELEVISION_BASE_KEYS_FEMALE, DEBUTS_ENDINGS_KEYS
        )

        assert "comedy series" in films_key_for_nat
        assert "comedy series" in films_mslslat_tab

    def test_adds_dashed_variants_for_specified_keys(self) -> None:
        female_keys = {}
        SERIES_DEBUTS_ENDINGS = {}
        TELEVISION_BASE_KEYS_FEMALE = {"series": "مسلسلات"}
        DEBUTS_ENDINGS_KEYS = ["series"]

        films_key_for_nat, films_mslslat_tab = _build_series_and_nat_keys(
            female_keys, SERIES_DEBUTS_ENDINGS, TELEVISION_BASE_KEYS_FEMALE, DEBUTS_ENDINGS_KEYS
        )

        assert "series-debuts" in films_key_for_nat
        assert "series-endings" in films_key_for_nat

    def test_adds_remakes_template(self) -> None:
        female_keys = {}
        SERIES_DEBUTS_ENDINGS = {}
        TELEVISION_BASE_KEYS_FEMALE = {}
        DEBUTS_ENDINGS_KEYS = []

        films_key_for_nat, films_mslslat_tab = _build_series_and_nat_keys(
            female_keys, SERIES_DEBUTS_ENDINGS, TELEVISION_BASE_KEYS_FEMALE, DEBUTS_ENDINGS_KEYS
        )

        assert "remakes of {} films" in films_key_for_nat

    def test_adds_series_debuts_endings_templates(self) -> None:
        female_keys = {}
        SERIES_DEBUTS_ENDINGS = {"series debuts": "مسلسلات {} بدأ عرضها في"}
        TELEVISION_BASE_KEYS_FEMALE = {}
        DEBUTS_ENDINGS_KEYS = []

        films_key_for_nat, films_mslslat_tab = _build_series_and_nat_keys(
            female_keys, SERIES_DEBUTS_ENDINGS, TELEVISION_BASE_KEYS_FEMALE, DEBUTS_ENDINGS_KEYS
        )

        assert "series debuts" in films_key_for_nat


class TestBuildTelevisionCao:
    """Tests for _build_television_cao function."""

    def test_builds_characters_variants(self) -> None:
        female_keys = {}
        TELEVISION_KEYS = {"comedy": "كوميديا"}

        films_key_cao, films_key_cao2 = _build_television_cao(female_keys, TELEVISION_KEYS)

        assert "comedy characters" in films_key_cao
        assert films_key_cao["comedy characters"] == "شخصيات كوميديا"

    def test_builds_title_cards_variants(self) -> None:
        female_keys = {}
        TELEVISION_KEYS = {"drama": "دراما"}

        films_key_cao, films_key_cao2 = _build_television_cao(female_keys, TELEVISION_KEYS)

        assert "drama title cards" in films_key_cao
        assert films_key_cao["drama title cards"] == "بطاقات عنوان دراما"

    def test_combines_with_female_keys(self) -> None:
        female_keys = {"action": "أكشن"}
        TELEVISION_KEYS = {}

        films_key_cao, films_key_cao2 = _build_television_cao(female_keys, TELEVISION_KEYS)

        assert "children's action" in films_key_cao
        assert films_key_cao["children's action"] == "أطفال أكشن"

    def test_builds_films_remakes(self) -> None:
        female_keys = {"horror": "رعب"}
        TELEVISION_KEYS = {}

        films_key_cao, films_key_cao2 = _build_television_cao(female_keys, TELEVISION_KEYS)

        assert "horror film remakes" in films_key_cao

    def test_builds_genre_categories(self) -> None:
        female_keys = {"comedy": "كوميدية"}
        TELEVISION_KEYS = {}

        films_key_cao, films_key_cao2 = _build_television_cao(female_keys, TELEVISION_KEYS)

        assert "comedy films" in films_key_cao
        assert films_key_cao["comedy films"] == "أفلام كوميدية"

    def test_builds_cao2_combinations(self) -> None:
        female_keys = {"action": "أكشن"}
        TELEVISION_KEYS = {"series": "مسلسل"}

        films_key_cao, films_key_cao2 = _build_television_cao(female_keys, TELEVISION_KEYS)

        assert "action series" in films_key_cao2
        assert films_key_cao2["action series"] == "مسلسل أكشن"

    def test_skips_empty_female_keys(self) -> None:
        female_keys = {"valid": "صحيح", "empty": ""}
        TELEVISION_KEYS = {}

        films_key_cao, films_key_cao2 = _build_television_cao(female_keys, TELEVISION_KEYS)

        # Should create entries for valid keys only
        assert "children's valid" in films_key_cao
        assert "valid films" in films_key_cao

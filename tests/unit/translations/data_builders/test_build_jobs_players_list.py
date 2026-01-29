"""Tests for build_jobs_players_list.py gendered player label utilities."""

from ArWikiCats.translations.data_builders.build_jobs_players_list import (
    GenderedLabel,
    GenderedLabelMap,
    _build_boxing_labels,
    _build_champion_labels,
    _build_general_scope_labels,
    _build_jobs_player_variants,
    _build_skating_labels,
    _build_sports_job_variants,
    _build_team_sport_labels,
    _build_world_champion_labels,
    _merge_maps,
)
from ArWikiCats.translations.data_builders.jobs_defs import combine_gender_labels


class TestBuildBoxingLabels:
    """Tests for _build_boxing_labels function."""

    def test_builds_boxer_labels(self) -> None:
        weights = {"heavyweight": "الوزن الثقيل", "flyweight": "الوزن الذبابي"}
        result = _build_boxing_labels(weights)

        assert "heavyweight boxers" in result
        assert result["heavyweight boxers"]["males"] == "ملاكمو الوزن الثقيل"
        assert result["heavyweight boxers"]["females"] == "ملاكمات الوزن الثقيل"

    def test_builds_world_champions(self) -> None:
        weights = {"welterweight": "الوزن الويلتر"}
        result = _build_boxing_labels(weights)

        assert "world welterweight boxing champions" in result
        assert result["world welterweight boxing champions"]["males"] == "أبطال العالم للملاكمة فئة الوزن الويلتر"

    def test_skips_empty_weights(self) -> None:
        weights = {"valid": "صحيح", "empty": ""}
        result = _build_boxing_labels(weights)

        assert "valid boxers" in result
        assert "empty boxers" not in result


class TestBuildSkatingLabels:
    """Tests for _build_skating_labels function."""

    def test_builds_skater_variants(self) -> None:
        labels = {
            "figure": {"males": "فني التزلج", "females": "فنية التزلج"},
            "speed": {"males": "سرعة التزلج", "females": "سرعة التزلج"},
        }
        result = _build_skating_labels(labels)

        assert "figure skaters" in result
        assert result["figure skaters"]["males"] == "متزلجو فني التزلج"
        assert result["figure skaters"]["females"] == "متزلجات فنية التزلج"

    def test_builds_skier_variants(self) -> None:
        labels = {
            "alpine": {"males": "تزلج جبالي", "females": "تزلج جبالي"},
        }
        result = _build_skating_labels(labels)

        assert "alpine skiers" in result
        assert result["alpine skiers"]["males"] == "متزحلقو تزلج جبالي"
        assert result["alpine skiers"]["females"] == "متزحلقات تزلج جبالي"


class TestBuildTeamSportLabels:
    """Tests for _build_team_sport_labels function."""

    def test_builds_team_labels(self) -> None:
        translations = {
            "football": "كرة القدم",
            "basketball": "كرة السلة",
        }
        result = _build_team_sport_labels(translations)

        assert result["football"]["males"] == "لاعبو كرة القدم"
        assert result["football"]["females"] == "لاعبات كرة القدم"

    def test_skips_empty_translations(self) -> None:
        translations = {"valid": "صحيح", "empty": ""}
        result = _build_team_sport_labels(translations)

        assert "valid" in result
        assert "empty" not in result


class TestBuildJobsPlayerVariants:
    """Tests for _build_jobs_player_variants function."""

    def test_adds_lowercase_key(self) -> None:
        players = {"Players": {"males": "لاعبو", "females": "لاعبات"}}
        result = _build_jobs_player_variants(players)

        assert "players" in result
        assert result["players"]["males"] == "لاعبو"

    def test_adds_olympic_variants(self) -> None:
        players = {"players": {"males": "لاعبو", "females": "لاعبات"}}
        result = _build_jobs_player_variants(players)

        assert "olympic players" in result
        assert result["olympic players"]["males"] == "لاعبو أولمبيون"
        assert result["olympic players"]["females"] == "لاعبات أولمبيات"

    def test_adds_international_variants(self) -> None:
        players = {"players": {"males": "لاعبو", "females": "لاعبات"}}
        result = _build_jobs_player_variants(players)

        assert "international players" in result
        assert result["international players"]["males"] == "لاعبو دوليون"
        assert result["international players"]["females"] == "لاعبات دوليات"

    def test_skips_empty_labels(self) -> None:
        players = {"empty": {"males": "", "females": ""}}
        result = _build_jobs_player_variants(players)

        assert "empty" not in result
        assert "olympic empty" not in result


class TestBuildGeneralScopeLabels:
    """Tests for _build_general_scope_labels function."""

    def test_combines_roles_and_scopes(self) -> None:
        roles = {"coach": {"males": "مدربو", "females": "مدربات"}}
        scopes = {"olympic": {"males": "أولمبيون", "females": "أولمبيات"}}
        result = _build_general_scope_labels(roles, scopes)

        assert "olympic coach" in result
        # Result should have combined labels
        assert result["olympic coach"]["males"] == combine_gender_labels("مدربو", "أولمبيون")

    def test_handles_empty_labels(self) -> None:
        roles = {"coach": {"males": "مدربو", "females": ""}}
        scopes = {"olympic": {"males": "", "females": "أولمبيات"}}
        result = _build_general_scope_labels(roles, scopes)

        assert "olympic coach" in result


class TestBuildChampionLabels:
    """Tests for _build_champion_labels function."""

    def test_builds_champions(self) -> None:
        labels = {"football": "كرة القدم", "basketball": "كرة السلة"}
        result = _build_champion_labels(labels)

        assert "football champions" in result
        assert result["football champions"]["males"] == "أبطال كرة القدم"
        assert result["football champions"]["females"] == ""

    def test_skips_empty_labels(self) -> None:
        labels = {"valid": "صحيح", "empty": ""}
        result = _build_champion_labels(labels)

        assert "valid champions" in result
        assert "empty champions" not in result


class TestBuildWorldChampionLabels:
    """Tests for _build_world_champion_labels function."""

    def test_builds_world_champions(self) -> None:
        labels = {"boxing": "الملاكمة", "wrestling": "المصارعة"}
        result = _build_world_champion_labels(labels)

        assert "world boxing champions" in result
        assert result["world boxing champions"]["males"] == "أبطال العالم الملاكمة "
        assert result["world boxing champions"]["females"] == ""

    def test_skips_empty_labels(self) -> None:
        labels = {"valid": "صحيح", "empty": ""}
        result = _build_world_champion_labels(labels)

        assert "world valid champions" in result
        assert "world empty champions" not in result


class TestBuildSportsJobVariants:
    """Tests for _build_sports_job_variants function."""

    def test_builds_biography_variants(self) -> None:
        sport_jobs = {"football": "كرة القدم"}
        football_roles = {}
        result = _build_sports_job_variants(sport_jobs, football_roles)

        assert "football biography" in result
        assert result["football biography"]["males"] == "أعلام كرة القدم"

    def test_builds_coaches_variants(self) -> None:
        sport_jobs = {"basketball": "كرة السلة"}
        football_roles = {}
        result = _build_sports_job_variants(sport_jobs, football_roles)

        assert "basketball coaches" in result
        assert result["basketball coaches"]["males"] == "مدربو كرة السلة"

    def test_combines_with_football_roles(self) -> None:
        sport_jobs = {"football": "كرة القدم"}
        football_roles = {"goalkeeper": {"males": "حراس مرمى", "females": "حارسات مرمى"}}
        result = _build_sports_job_variants(sport_jobs, football_roles)

        # Should create composite entries
        assert "football goalkeeper" in result
        # Check that it combines labels properly
        assert (
            "goalkeeper" in result["football goalkeeper"]["males"]
            or "كرة القدم" in result["football goalkeeper"]["males"]
        )

    def test_skips_empty_jobs(self) -> None:
        sport_jobs = {"valid": "صحيح", "empty": ""}
        football_roles = {}
        result = _build_sports_job_variants(sport_jobs, football_roles)

        assert "valid biography" in result
        assert "empty biography" not in result


class TestMergeMaps:
    """Tests for _merge_maps function."""

    def test_merges_multiple_maps(self) -> None:
        map1: GenderedLabelMap = {"key1": {"males": "1", "females": "1f"}}
        map2: GenderedLabelMap = {"key2": {"males": "2", "females": "2f"}}
        map3: GenderedLabelMap = {"key3": {"males": "3", "females": "3f"}}

        result = _merge_maps(map1, map2, map3)

        assert "key1" in result
        assert "key2" in result
        assert "key3" in result

    def test_later_maps_override(self) -> None:
        map1: GenderedLabelMap = {"key": {"males": "first", "females": "first_f"}}
        map2: GenderedLabelMap = {"key": {"males": "second", "females": "second_f"}}

        result = _merge_maps(map1, map2)

        assert result["key"]["males"] == "second"

    def test_empty_maps(self) -> None:
        result = _merge_maps()
        assert result == {}

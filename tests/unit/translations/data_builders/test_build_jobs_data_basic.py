"""Tests for build_jobs_data_basic.py specialized job label builders."""

from collections.abc import Iterable

from ArWikiCats.translations.data_builders.build_jobs_data_basic import (
    _build_military_job_labels,
    _build_painter_job_labels,
    _build_religious_job_labels,
)
from ArWikiCats.translations.data_builders.jobs_defs import GenderedLabelMap


class TestBuildReligiousJobLabels:
    """Tests for _build_religious_job_labels function."""

    def test_combines_religions_and_roles(self) -> None:
        religions: GenderedLabelMap = {
            "christian": {"males": "مسيحي", "females": "مسيحية"},
        }
        roles: GenderedLabelMap = {
            "saints": {"males": "قديسون", "females": "قديسات"},
        }
        result = _build_religious_job_labels(religions, roles)

        assert "christian saints" in result
        assert "قديسون" in result["christian saints"]["males"]
        assert "مسيحية" in result["christian saints"]["females"]

    def test_combines_multiple_pairs(self) -> None:
        religions: GenderedLabelMap = {
            "christian": {"males": "مسيحي", "females": "مسيحية"},
            "islamic": {"males": "إسلامي", "females": "إسلامية"},
        }
        roles: GenderedLabelMap = {
            "saints": {"males": "قديسون", "females": "قديسات"},
            "scholars": {"males": "علماء", "females": "عالمات"},
        }
        result = _build_religious_job_labels(religions, roles)

        assert "christian saints" in result
        assert "christian scholars" in result
        assert "islamic saints" in result
        assert "islamic scholars" in result

    def test_skips_empty_religions(self) -> None:
        religions: GenderedLabelMap = {}
        roles: GenderedLabelMap = {
            "saints": {"males": "قديسون", "females": "قديسات"},
        }
        result = _build_religious_job_labels(religions, roles)

        assert result == {}

    def test_skips_empty_roles(self) -> None:
        religions: GenderedLabelMap = {
            "christian": {"males": "مسيحي", "females": "مسيحية"},
        }
        roles: GenderedLabelMap = {}
        result = _build_religious_job_labels(religions, roles)

        assert result == {}

    def test_skips_empty_gendered_labels(self) -> None:
        religions: GenderedLabelMap = {
            "valid": {"males": "صحيح", "females": "صحيحة"},
            "empty": {"males": "", "females": ""},
        }
        roles: GenderedLabelMap = {
            "saints": {"males": "قديسون", "females": "قديسات"},
        }
        result = _build_religious_job_labels(religions, roles)

        assert "valid saints" in result
        assert "empty saints" not in result


class TestBuildPainterJobLabels:
    """Tests for _build_painter_job_labels function."""

    def test_includes_base_roles(self) -> None:
        painter_styles: GenderedLabelMap = {}
        painter_roles: GenderedLabelMap = {
            "painters": {"males": "رسامون", "females": "رسامات"},
        }
        painter_categories = {}

        result = _build_painter_job_labels(painter_styles, painter_roles, painter_categories)

        assert "painters" in result
        assert result["painters"]["males"] == "رسامون"

    def test_includes_styles_except_history(self) -> None:
        painter_styles: GenderedLabelMap = {
            "impressionist": {"males": "انطباعي", "females": "انطباعية"},
            "history": {"males": "تاريخي", "females": "تاريخية"},
        }
        painter_roles: GenderedLabelMap = {}
        painter_categories = {}

        result = _build_painter_job_labels(painter_styles, painter_roles, painter_categories)

        assert "impressionist" in result
        assert "history" not in result

    def test_creates_style_role_combinations(self) -> None:
        painter_styles: GenderedLabelMap = {
            "symbolist": {"males": "رمزي", "females": "رمزية"},
        }
        painter_roles: GenderedLabelMap = {
            "painters": {"males": "رسامون", "females": "رسامات"},
        }
        painter_categories = {}

        result = _build_painter_job_labels(painter_styles, painter_roles, painter_categories)

        assert "symbolist painters" in result
        assert "رسامون" in result["symbolist painters"]["males"]
        assert "رمزي" in result["symbolist painters"]["males"]

    def test_creates_category_painters_variants(self) -> None:
        painter_styles: GenderedLabelMap = {}
        painter_roles: GenderedLabelMap = {}
        painter_categories = {"french": "فرنسية"}

        result = _build_painter_job_labels(painter_styles, painter_roles, painter_categories)

        assert "french painters" in result
        assert result["french painters"]["males"] == "رسامو فرنسية"

    def test_creates_category_artists_variants(self) -> None:
        painter_styles: GenderedLabelMap = {}
        painter_roles: GenderedLabelMap = {}
        painter_categories = {"modern": "حديثة"}

        result = _build_painter_job_labels(painter_styles, painter_roles, painter_categories)

        assert "modern artists" in result
        assert result["modern artists"]["males"] == "فنانو حديثة"

    def test_skips_empty_categories(self) -> None:
        painter_styles: GenderedLabelMap = {}
        painter_roles: GenderedLabelMap = {}
        painter_categories = {"valid": "صحيح", "empty": ""}

        result = _build_painter_job_labels(painter_styles, painter_roles, painter_categories)

        assert "valid painters" in result
        assert "valid artists" in result
        assert "empty painters" not in result
        assert "empty artists" not in result


class TestBuildMilitaryJobLabels:
    """Tests for _build_military_job_labels function."""

    def test_includes_base_roles(self) -> None:
        military_prefixes: GenderedLabelMap = {}
        military_roles: GenderedLabelMap = {
            "soldiers": {"males": "جنود", "females": "جنوديات"},
        }
        excluded_prefixes: Iterable[str] = []

        result = _build_military_job_labels(military_prefixes, military_roles, excluded_prefixes)

        assert "soldiers" in result
        assert result["soldiers"]["males"] == "جنود"

    def test_includes_allowed_prefixes(self) -> None:
        military_prefixes: GenderedLabelMap = {
            "army": {"males": "جيش", "females": "جيش"},
        }
        military_roles: GenderedLabelMap = {}
        excluded_prefixes: Iterable[str] = []

        result = _build_military_job_labels(military_prefixes, military_roles, excluded_prefixes)

        assert "army" in result

    def test_excludes_specified_prefixes(self) -> None:
        military_prefixes: GenderedLabelMap = {
            "special": {"males": "خاص", "females": "خاصة"},
        }
        military_roles: GenderedLabelMap = {}
        excluded_prefixes = ["special"]

        result = _build_military_job_labels(military_prefixes, military_roles, excluded_prefixes)

        assert "special" not in result

    def test_creates_prefix_role_combinations(self) -> None:
        military_prefixes: GenderedLabelMap = {
            "army": {"males": "جيش", "females": "جيش"},
        }
        military_roles: GenderedLabelMap = {
            "soldiers": {"males": "جنود", "females": "جنوديات"},
        }
        excluded_prefixes: Iterable[str] = []

        result = _build_military_job_labels(military_prefixes, military_roles, excluded_prefixes)

        assert "army soldiers" in result
        assert "جنود" in result["army soldiers"]["males"]
        assert "جيش" in result["army soldiers"]["males"]

    def test_excluded_prefixes_still_used_in_combinations(self) -> None:
        military_prefixes: GenderedLabelMap = {
            "navy": {"males": "بحري", "females": "بحرية"},
        }
        military_roles: GenderedLabelMap = {
            "soldiers": {"males": "جنود", "females": "جنوديات"},
        }
        excluded_prefixes = ["navy"]

        result = _build_military_job_labels(military_prefixes, military_roles, excluded_prefixes)

        # Navy should be excluded as standalone but used in combinations
        assert "navy" not in result
        assert "navy soldiers" in result

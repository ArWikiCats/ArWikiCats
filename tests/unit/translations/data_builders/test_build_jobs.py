"""Tests for build_jobs.py comprehensive job label building utilities."""

from collections.abc import Mapping

from ArWikiCats.translations.data_builders.build_jobs import (
    JobsDataset,
    _add_cycling_variants,
    _add_film_variants,
    _add_jobs_from_jobs2,
    _add_jobs_people_variants,
    _add_singer_variants,
    _add_sport_variants,
    _build_jobs_2020,
    _build_jobs_new,
    _extend_with_disability_jobs,
    _extend_with_religious_jobs,
    _finalise_jobs_dataset,
    _load_activist_jobs,
    _merge_jobs_sources,
)
from ArWikiCats.translations.data_builders.jobs_defs import GenderedLabel, GenderedLabelMap


class TestBuildJobs2020:
    """Tests for _build_jobs_2020 function."""

    def test_returns_copy(self) -> None:
        JOBS_2020_BASE: GenderedLabelMap = {"architects": {"males": "مهندسون", "females": "مهندسات"}}
        result = _build_jobs_2020(JOBS_2020_BASE)

        assert result == JOBS_2020_BASE
        assert result is not JOBS_2020_BASE  # Should be a copy


class TestExtendWithReligiousJobs:
    """Tests for _extend_with_religious_jobs function."""

    def test_adds_religious_roles(self) -> None:
        base_jobs: GenderedLabelMap = {}
        RELIGIOUS_KEYS_PP = {
            "priests": {"males": "قساوسة", "females": "قساوسة"},
        }
        result = _extend_with_religious_jobs(base_jobs, RELIGIOUS_KEYS_PP)

        assert "priests" in result
        assert result["priests"]["males"] == "قساوسة"

    def test_adds_activist_variants(self) -> None:
        base_jobs: GenderedLabelMap = {}
        RELIGIOUS_KEYS_PP = {
            "monks": {"males": "رهبان", "females": "راهبات"},
        }
        result = _extend_with_religious_jobs(base_jobs, RELIGIOUS_KEYS_PP)

        assert "monks activists" in result
        assert result["monks activists"]["males"] == "ناشطون رهبان"


class TestExtendWithDisabilityJobs:
    """Tests for _extend_with_disability_jobs function."""

    def test_adds_disability_labels(self) -> None:
        base_jobs: GenderedLabelMap = {}
        DISABILITY_LABELS: GenderedLabelMap = {
            "deaf": {"males": "صم", "females": "صم"},
        }
        EXECUTIVE_DOMAINS: Mapping[str, str] = {}

        result = _extend_with_disability_jobs(base_jobs, DISABILITY_LABELS, EXECUTIVE_DOMAINS)

        assert "deaf" in result
        assert result["deaf"]["males"] == "صم"

    def test_adds_executive_variants(self) -> None:
        base_jobs: GenderedLabelMap = {}
        DISABILITY_LABELS: GenderedLabelMap = {}
        EXECUTIVE_DOMAINS = {"banking": "البنوك"}

        result = _extend_with_disability_jobs(base_jobs, DISABILITY_LABELS, EXECUTIVE_DOMAINS)

        assert "banking executives" in result
        assert result["banking executives"]["males"] == "مدراء البنوك"

    def test_skips_empty_executive_domains(self) -> None:
        base_jobs: GenderedLabelMap = {}
        DISABILITY_LABELS: GenderedLabelMap = {}
        EXECUTIVE_DOMAINS = {"empty": ""}

        result = _extend_with_disability_jobs(base_jobs, DISABILITY_LABELS, EXECUTIVE_DOMAINS)

        assert "empty executives" not in result


class TestMergeJobsSources:
    """Tests for _merge_jobs_sources function."""

    def test_adds_static_entries(self) -> None:
        jobs_pp: GenderedLabelMap = {}
        result = _merge_jobs_sources(
            jobs_pp=jobs_pp,
            EXECUTIVE_DOMAINS={},
            DISABILITY_LABELS={},
            RELIGIOUS_KEYS_PP={},
            FOOTBALL_KEYS_PLAYERS={},
            JOBS_2020_BASE={},
            companies_to_jobs={},
            RELIGIOUS_FEMALE_KEYS={},
        )

        assert "candidates" in result
        assert result["candidates"]["males"] == "مرشحون"

    def test_adds_coaches_entry(self) -> None:
        jobs_pp: GenderedLabelMap = {}
        result = _merge_jobs_sources(
            jobs_pp=jobs_pp,
            EXECUTIVE_DOMAINS={},
            DISABILITY_LABELS={},
            RELIGIOUS_KEYS_PP={},
            FOOTBALL_KEYS_PLAYERS={},
            JOBS_2020_BASE={},
            companies_to_jobs={},
            RELIGIOUS_FEMALE_KEYS={},
        )

        assert "coaches" in result
        assert result["coaches"]["males"] == "مدربون"


class TestAddJobsFromJobs2:
    """Tests for _add_jobs_from_jobs2 function."""

    def test_adds_missing_jobs_from_jobs2(self) -> None:
        jobs_pp: GenderedLabelMap = {}
        JOBS_2 = {"new_job": {"males": "وظيفة جديدة", "females": ""}}
        JOBS_3333 = {}

        result = _add_jobs_from_jobs2(jobs_pp, JOBS_2, JOBS_3333)

        assert "new_job" in result
        assert result["new_job"]["males"] == "وظيفة جديدة"

    def test_skips_existing_keys(self) -> None:
        jobs_pp: GenderedLabelMap = {"existing": {"males": "موجود", "females": ""}}
        JOBS_2 = {"existing": {"males": "جديد", "females": ""}}
        JOBS_3333 = {}

        result = _add_jobs_from_jobs2(jobs_pp, JOBS_2, JOBS_3333)

        assert result["existing"]["males"] == "موجود"  # Not overwritten

    def test_skips_empty_labels(self) -> None:
        jobs_pp: GenderedLabelMap = {}
        JOBS_2 = {"empty": {"males": "", "females": ""}}
        JOBS_3333 = {}

        result = _add_jobs_from_jobs2(jobs_pp, JOBS_2, JOBS_3333)

        assert "empty" not in result


class TestLoadActivistJobs:
    """Tests for _load_activist_jobs function."""

    def test_loads_activists(self) -> None:
        m_w_jobs: GenderedLabelMap = {}
        nat_before_occ: list[str] = []
        activists = {"activists": {"males": "ناشطون", "females": "ناشطات"}}

        _load_activist_jobs(m_w_jobs, nat_before_occ, activists)

        assert "activists" in m_w_jobs
        assert m_w_jobs["activists"]["males"] == "ناشطون"
        assert "activists" in nat_before_occ

    def test_appends_unique_keys(self) -> None:
        m_w_jobs: GenderedLabelMap = {}
        nat_before_occ = ["existing"]
        activists = {"activists": {"males": "ناشطون", "females": "ناشطات"}}

        _load_activist_jobs(m_w_jobs, nat_before_occ, activists)

        assert "activists" in nat_before_occ
        assert nat_before_occ.count("activists") == 1


class TestAddSportVariants:
    """Tests for _add_sport_variants function."""

    def test_adds_sports_variants(self) -> None:
        base_jobs: Mapping[str, GenderedLabel] = {"players": {"males": "لاعبو", "females": "لاعبات"}}
        result = _add_sport_variants(base_jobs)

        assert "sports players" in result
        assert "لاعبو" in result["sports players"]["males"]
        assert "رياضيون" in result["sports players"]["males"]

    def test_adds_professional_variants(self) -> None:
        base_jobs: Mapping[str, GenderedLabel] = {"players": {"males": "لاعبو", "females": "لاعبات"}}
        result = _add_sport_variants(base_jobs)

        assert "professional players" in result
        assert "لاعبو" in result["professional players"]["males"]
        assert "محترفون" in result["professional players"]["males"]

    def test_adds_wheelchair_variants(self) -> None:
        base_jobs: Mapping[str, GenderedLabel] = {"players": {"males": "لاعبو", "females": "لاعبات"}}
        result = _add_sport_variants(base_jobs)

        assert "wheelchair players" in result
        assert "الكراسي المتحركة" in result["wheelchair players"]["males"]


class TestAddCyclingVariants:
    """Tests for _add_cycling_variants function."""

    def test_adds_cyclist_variants(self) -> None:
        BASE_CYCLING_EVENTS = {"tour de france": " Tour de France "}
        nat_before_occ: list[str] = []
        result = _add_cycling_variants(nat_before_occ, BASE_CYCLING_EVENTS)

        assert "tour de france cyclists" in result
        # Note: double space due to how join_terms works with trailing space in input
        assert result["tour de france cyclists"]["males"] == "دراجو  Tour de France "

    def test_adds_winners_variants(self) -> None:
        BASE_CYCLING_EVENTS = {"giro d'italia": " Giro d'Italia "}
        nat_before_occ: list[str] = []
        result = _add_cycling_variants(nat_before_occ, BASE_CYCLING_EVENTS)

        assert "giro d'italia winners" in result
        # Note: double space due to how join_terms works with trailing space in input
        assert result["giro d'italia winners"]["males"] == "فائزون في  Giro d'Italia "

    def test_appends_to_nat_before_occ(self) -> None:
        BASE_CYCLING_EVENTS = {"vuelta a espana": " Vuelta a España "}
        nat_before_occ: list[str] = []
        result = _add_cycling_variants(nat_before_occ, BASE_CYCLING_EVENTS)

        assert "vuelta a espana winners" in nat_before_occ
        assert "vuelta a espana stage winners" in nat_before_occ


class TestAddJobsPeopleVariants:
    """Tests for _add_jobs_people_variants function."""

    def test_combines_with_book_categories(self) -> None:
        JOBS_PEOPLE_ROLES: GenderedLabelMap = {"writers": {"males": "كتاب", "females": "كاتبات"}}
        BOOK_CATEGORIES = {"children's": "الأطفال"}
        JOBS_TYPE_TRANSLATIONS = {}

        result = _add_jobs_people_variants(JOBS_PEOPLE_ROLES, BOOK_CATEGORIES, JOBS_TYPE_TRANSLATIONS)

        assert "children's writers" in result
        assert result["children's writers"]["males"] == "كتاب الأطفال"

    def test_combines_with_job_types(self) -> None:
        JOBS_PEOPLE_ROLES: GenderedLabelMap = {"writers": {"males": "كتاب", "females": "كاتبات"}}
        BOOK_CATEGORIES = {}
        JOBS_TYPE_TRANSLATIONS = {"science fiction": "خيال علمي"}

        result = _add_jobs_people_variants(JOBS_PEOPLE_ROLES, BOOK_CATEGORIES, JOBS_TYPE_TRANSLATIONS)

        assert "science fiction writers" in result
        assert result["science fiction writers"]["males"] == "كتاب خيال علمي"

    def test_skips_roles_without_both_genders(self) -> None:
        JOBS_PEOPLE_ROLES: GenderedLabelMap = {
            "complete": {"males": "كامل", "females": "كاملة"},
            "incomplete": {"males": "غير كامل", "females": ""},
        }
        BOOK_CATEGORIES = {"test": "اختبار"}
        JOBS_TYPE_TRANSLATIONS = {}

        result = _add_jobs_people_variants(JOBS_PEOPLE_ROLES, BOOK_CATEGORIES, JOBS_TYPE_TRANSLATIONS)

        assert "test complete" in result
        assert "test incomplete" not in result


class TestAddFilmVariants:
    """Tests for _add_film_variants function."""

    def test_adds_film_job_variants(self) -> None:
        result = _add_film_variants()

        assert "film directors" in result
        assert result["film directors"]["males"] == "مخرجو أفلام"

    def test_includes_documentary_variants(self) -> None:
        result = _add_film_variants()

        assert "documentary filmmakers" in result
        assert result["documentary filmmakers"]["males"] == "صانعو أفلام وثائقية"


class TestAddSingerVariants:
    """Tests for _add_singer_variants function."""

    def test_adds_classical_variants(self) -> None:
        result = _add_singer_variants()

        assert "classical composers" in result
        assert result["classical composers"]["males"] == "ملحنون كلاسيكيون"

    def test_adds_singers(self) -> None:
        result = _add_singer_variants()

        assert "classical singers" in result
        assert result["classical singers"]["females"] == "مغنيات كلاسيكيات"


class TestFinaliseJobsDataset:
    """Tests for _finalise_jobs_dataset function."""

    def test_returns_jobs_dataset(self) -> None:
        # Minimal setup for testing
        result = _finalise_jobs_dataset(
            jobs_pp={},
            sport_variants={},
            people_variants={},
            MEN_WOMENS_JOBS_2={},
            NAT_BEFORE_OCC=[],
            MEN_WOMENS_SINGERS_BASED={},
            MEN_WOMENS_SINGERS={},
            PLAYERS_TO_MEN_WOMENS_JOBS={},
            SPORT_JOB_VARIANTS={},
            RELIGIOUS_FEMALE_KEYS={},
            BASE_CYCLING_EVENTS={},
            JOBS_2={},
            JOBS_3333={},
            RELIGIOUS_KEYS_PP={},
            FOOTBALL_KEYS_PLAYERS={},
            EXECUTIVE_DOMAINS={},
            DISABILITY_LABELS={},
            JOBS_2020_BASE={},
            companies_to_jobs={},
            activists={},
        )

        assert isinstance(result, JobsDataset)
        assert hasattr(result, "males_jobs")
        assert hasattr(result, "females_jobs")

    def test_adds_men_s_footballers(self) -> None:
        # Setup with at least one job to trigger the special entry
        result = _finalise_jobs_dataset(
            jobs_pp={"test": {"males": "اختبار", "females": ""}},
            sport_variants={},
            people_variants={},
            MEN_WOMENS_JOBS_2={},
            NAT_BEFORE_OCC=[],
            MEN_WOMENS_SINGERS_BASED={},
            MEN_WOMENS_SINGERS={},
            PLAYERS_TO_MEN_WOMENS_JOBS={},
            SPORT_JOB_VARIANTS={},
            RELIGIOUS_FEMALE_KEYS={},
            BASE_CYCLING_EVENTS={},
            JOBS_2={},
            JOBS_3333={},
            RELIGIOUS_KEYS_PP={},
            FOOTBALL_KEYS_PLAYERS={},
            EXECUTIVE_DOMAINS={},
            DISABILITY_LABELS={},
            JOBS_2020_BASE={},
            companies_to_jobs={},
            activists={},
        )

        assert result.males_jobs["men's footballers"] == "لاعبو كرة قدم رجالية"


class TestBuildJobsNew:
    """Tests for _build_jobs_new function."""

    def test_lowercases_female_job_keys(self) -> None:
        female_jobs = {"Writers": "كاتبات"}
        Nat_mens = {}

        result = _build_jobs_new(female_jobs, Nat_mens)

        assert "writers" in result
        assert result["writers"] == "كاتبات"

    def test_adds_nationality_people_variants(self) -> None:
        female_jobs = {}
        Nat_mens = {"egyptian": "مصريون"}

        result = _build_jobs_new(female_jobs, Nat_mens)

        assert "egyptian people" in result
        assert result["egyptian people"] == "مصريون"

    def test_adds_ottoman_empire_entry(self) -> None:
        female_jobs = {}
        Nat_mens = {}

        result = _build_jobs_new(female_jobs, Nat_mens)

        assert "people of the ottoman empire" in result
        assert result["people of the ottoman empire"] == "عثمانيون"

    def test_skips_empty_jobs(self) -> None:
        female_jobs = {"valid": "صحيح", "empty": ""}
        Nat_mens = {}

        result = _build_jobs_new(female_jobs, Nat_mens)

        assert "valid" in result
        assert "empty" not in result

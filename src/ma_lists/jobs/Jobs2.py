"""Assemble gendered Arabic labels for general job categories.

This module historically populated two large dictionaries: ``Jobs_2`` and
``Jobs_3333``.  The original implementation performed a series of untyped
mutations, loaded JSON documents directly into globals, and printed diagnostic
information on import.  The refactor recreates the same data while providing
type hints, reusable helpers, structured logging, and inline documentation that
explains the intent of each transformation.
"""

from __future__ import annotations

import logging
from typing import Iterable, Mapping, Tuple

from .jobs_defs import GenderedLabel, GenderedLabelMap, gendered_label, load_gendered_label_map

LOGGER = logging.getLogger(__name__)


# ---------------------------------------------------------------------------
# JSON configuration


JSON_JOBS_ADDITIONAL_FILE = "jobs_3"
"""Filename containing supplemental job labels keyed by category."""

JSON_JOBS_PRIMARY_FILE = "Jobs_22"
"""Filename storing the primary set of job labels used across modules."""


# ---------------------------------------------------------------------------
# Static configuration


SCIENTIST_DISCIPLINES: Mapping[str, str] = {
    "anatomists": "تشريح",
    "anthropologists": "أنثروبولوجيا",
    "arachnologists": "عنكبوتيات",
    "archaeologists": "آثار",
    "assyriologists": "آشوريات",
    "atmospheric scientists": "غلاف جوي",
    "biblical scholars": "الكتاب المقدس",
    "biologists": "أحياء",
    "biotechnologists": "تكنولوجيا حيوية",
    "botanists": "نباتات",
    "cartographers": "رسم خرائط",
    "cell biologists": "أحياء خلوية",
    "computer scientists": "حاسوب",
    "cosmologists": "كون",
    "criminologists": "جريمة",
    "cryptographers": "تعمية",
    "crystallographers": "بلورات",
    "demographers": "سكان",
    "dialectologists": "لهجات",
    "earth scientists": "الأرض",
    "ecologists": "بيئة",
    "egyptologists": "مصريات",
    "entomologists": "حشرات",
    "epidemiologists": "وبائيات",
    "epigraphers": "نقائش",
    "evolutionary biologists": "أحياء تطورية",
    "experimental physicists": "فيزياء تجريبية",
    "forensic scientists": "أدلة جنائية",
    "geneticists": "وراثة",
    "herpetologists": "زواحف وبرمائيات",
    "hydrographers": "وصف المياه",
    "hygienists": "صحة",
    "ichthyologists": "أسماك",
    "immunologists": "مناعة",
    "iranologists": "إيرانيات",
    "malariologists": "ملاريا",
    "mammalogists": "ثدييات",
    "marine biologists": "أحياء بحرية",
    "mineralogists": "معادن",
    "molecular biologists": "أحياء جزيئية",
    "mongolists": "منغوليات",
    "musicologists": "موسيقى",
    "naturalists": "طبيعة",
    "neuroscientists": "أعصاب",
    "nuclear physicists": "ذرة",
    "oceanographers": "محيطات",
    "ornithologists": "طيور",
    "paleontologists": "حفريات",
    "parasitologists": "طفيليات",
    "philologists": "لغة",
    "phycologists": "طحالب",
    "physical chemists": "كيمياء فيزيائية",
    "planetary scientists": "كواكب",
    "prehistorians": "عصر ما قبل التاريخ",
    "primatologists": "رئيسيات",
    "pteridologists": "سرخسيات",
    "quantum physicists": "فيزياء الكم",
    "seismologists": "زلازل",
    "sexologists": "جنس",
    "sinologists": "صينيات",
    "sociologists": "اجتماع",
    "taxonomists": "تصنيف",
    "toxicologists": "سموم",
    "turkologists": "تركيات",
    "virologists": "فيروسات",
    "zoologists": "حيوانات",
}

SCHOLAR_DISCIPLINES: Mapping[str, str] = {
    "islamic studies": "دراسات إسلامية",
    "native american studies": "دراسات الأمريكيين الأصليين",
    "strategic studies": "دراسات إستراتيجية",
    "romance studies": "دراسات رومانسية",
    "black studies": "دراسات إفريقية",
    "literary studies": "دراسات أدبية",
}

LEGACY_EXPECTED_MENS_LABELS: Mapping[str, str] = {
    "air force generals": "جنرالات القوات الجوية",
    "air force officers": "ضباط القوات الجوية",
    "architecture critics": "نقاد عمارة",
    "businesspeople in advertising": "رجال وسيدات أعمال إعلانيون",
    "businesspeople in shipping": "شخصيات أعمال في نقل بحري",
    "child actors": "ممثلون أطفال",
    "child psychiatrists": "أخصائيو طب نفس الأطفال",
    "child singers": "مغنون أطفال",
    "christian clergy": "رجال دين مسيحيون",
    "competitors in athletics": "لاعبو قوى",
    "computer occupations": "مهن الحاسوب",
    "contributors to the encyclopédie": "مشاركون في وضع موسوعة الإنسيكلوبيدي",
    "critics of religions": "نقاد الأديان",
    "daimyo": "دايميو",
    "eugenicists": "علماء متخصصون في تحسين النسل",
    "founders of religions": "مؤسسو أديان",
    "french navy officers": "ضباط بحرية فرنسيون",
    "geisha": "غايشا",
    "hacking (computer security)": "اختراق (حماية الحاسوب)",
    "health occupations": "مهن صحية",
    "historians of christianity": "مؤرخو مسيحية",
    "historians of mathematics": "مؤرخو رياضيات",
    "historians of philosophy": "مؤرخو فلسفة",
    "historians of religion": "مؤرخو دين",
    "historians of science": "مؤرخو علم",
    "historians of technology": "مؤرخو تقنية",
    "human computers": "أجهزة حواسيب بشرية",
    "japanese voice actors": "ممثلو أداء صوتي يابانيون",
    "literary editors": "محرر أدبي",
    "midwives": "قابلات",
    "military doctors": "أطباء عسكريون",
    "muslim scholars of islam": "مسلمون باحثون عن الإسلام",
    "ninja": "نينجا",
    "nuns": "راهبات",
    "physiologists": "علماء وظائف الأعضاء",
    "political commentators": "نقاد سياسيون",
    "political consultants": "استشاريون سياسيون",
    "political scientists": "علماء سياسة",
    "political theorists": "منظرون سياسيون",
    "prophets": "أنبياء ورسل",
    "prostitutes": "داعرات",
    "religious writers": "كتاب دينيون",
    "service occupations": "مهن خدمية",
    "sports scientists": "علماء رياضيون",
    "women writers": "كاتبات",
}


# ---------------------------------------------------------------------------
# Helper functions


def _lowercase_keys(jobs: Mapping[str, GenderedLabel]) -> GenderedLabelMap:
    """Return a new mapping that lowercases every key.

    Args:
        jobs: The mapping whose keys should be normalised.

    Returns:
        A dictionary keyed by lowercase category names.  The original values are
        reused because :class:`GenderedLabel` objects are immutable mappings.
    """

    return {key.lower(): value for key, value in jobs.items()}


def _build_scientist_roles(disciplines: Mapping[str, str]) -> GenderedLabelMap:
    """Create gendered labels for scientist categories.

    Args:
        disciplines: Mapping of role names to the Arabic specialisation.

    Returns:
        A dictionary containing entries such as ``"anatomists"`` whose values
        include the masculine and feminine Arabic forms.
    """

    scientist_roles: GenderedLabelMap = {}
    for role_key, subject in disciplines.items():
        scientist_roles[role_key.lower()] = gendered_label(
            f"علماء {subject}",
            f"عالمات {subject}",
        )
    return scientist_roles


def _build_scholar_roles(disciplines: Mapping[str, str]) -> GenderedLabelMap:
    """Create gendered labels for scholar categories."""

    scholar_roles: GenderedLabelMap = {}
    for discipline, subject in disciplines.items():
        scholar_roles[f"{discipline.lower()} scholars"] = gendered_label(
            f"علماء {subject}",
            f"عالمات {subject}",
        )
    return scholar_roles


def _merge_job_sources(
    base_jobs: GenderedLabelMap,
    supplemental_sources: Iterable[Mapping[str, GenderedLabel]],
) -> GenderedLabelMap:
    """Merge multiple job dictionaries while preserving existing entries.

    Args:
        base_jobs: Initial mapping that will be updated in-place.
        supplemental_sources: Additional mappings layered on top of ``base_jobs``.

    Returns:
        The ``base_jobs`` dictionary after merging all supplemental sources.
        Empty labels are skipped to mimic the behaviour of the legacy script.
    """

    for source in supplemental_sources:
        for job_key, labels in source.items():
            if job_key in base_jobs:
                continue
            if labels["mens"] or labels["womens"]:
                base_jobs[job_key] = labels
    return base_jobs


def _log_expected_label_consistency(jobs: Mapping[str, GenderedLabel]) -> None:
    """Emit debug information comparing legacy expectations to new data."""

    matching = 0
    mismatched = 0
    missing = 0

    for expected_key, expected_mens_label in LEGACY_EXPECTED_MENS_LABELS.items():
        normalised_key = expected_key.lower()
        gendered_label = jobs.get(normalised_key)
        if gendered_label is None:
            missing += 1
            continue
        if gendered_label["mens"] == expected_mens_label:
            matching += 1
        else:
            mismatched += 1

    LOGGER.debug(
        "legacy job labels compared (matching=%d, mismatched=%d, missing=%d)",
        matching,
        mismatched,
        missing,
    )


def _build_jobs_datasets() -> Tuple[GenderedLabelMap, GenderedLabelMap]:
    """Construct the ``Jobs_2`` and ``Jobs_3333`` datasets.

    Returns:
        A tuple where the first item represents ``Jobs_2`` and the second item
        represents ``Jobs_3333`` from the legacy implementation.
    """

    scientist_jobs = _build_scientist_roles(SCIENTIST_DISCIPLINES)
    scholar_jobs = _build_scholar_roles(SCHOLAR_DISCIPLINES)

    jobs_additional = load_gendered_label_map(JSON_JOBS_ADDITIONAL_FILE)
    jobs_primary = load_gendered_label_map(JSON_JOBS_PRIMARY_FILE)

    lowercase_additional = _lowercase_keys(jobs_additional)
    lowercase_primary = _lowercase_keys(jobs_primary)

    combined_jobs = {**scientist_jobs, **scholar_jobs}
    _merge_job_sources(combined_jobs, (lowercase_additional, lowercase_primary))
    _log_expected_label_consistency(combined_jobs)

    return combined_jobs, lowercase_additional


# ---------------------------------------------------------------------------
# Public API


JOBS_2, JOBS_3333 = _build_jobs_datasets()

# Backwards compatible exports -------------------------------------------------
Jobs_2: GenderedLabelMap = JOBS_2
Jobs_3333: GenderedLabelMap = JOBS_3333

__all__ = ["JOBS_2", "JOBS_3333", "Jobs_2", "Jobs_3333", "GenderedLabel", "GenderedLabelMap"]


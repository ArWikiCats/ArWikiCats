"""
Assemble gendered Arabic labels for general job categories.
"""

from __future__ import annotations

from typing import Mapping, Tuple

from ..data_builders.jobs_defs import GenderedLabelMap
from ..helps import len_print, logger
from ..utils import open_json_file

jobs_primary = open_json_file("jobs/Jobs_22.json")
jobs_additional = open_json_file("jobs/jobs_3.json")
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
    "biotechnologists": "تقانة حيوية",
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
    "historians of technology": "مؤرخو تقانة",
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
        scientist_roles[role_key.lower()] = {
            "males": f"علماء {subject}",
            "females": f"عالمات {subject}",
        }
    return scientist_roles


def _build_scholar_roles(disciplines: Mapping[str, str]) -> GenderedLabelMap:
    """Create gendered labels for scholar categories."""

    scholar_roles: GenderedLabelMap = {}
    for discipline, subject in disciplines.items():
        scholar_roles[f"{discipline.lower()} scholars"] = {
            "males": f"علماء {subject}",
            "females": f"عالمات {subject}",
        }
    return scholar_roles


def _build_jobs_datasets() -> Tuple[GenderedLabelMap, GenderedLabelMap]:
    """Construct the ``JOBS_2`` and ``JOBS_3333`` datasets.

    Returns:
        A tuple where the first item represents ``JOBS_2`` and the second item
        represents ``JOBS_3333`` from the legacy implementation.
    """

    scientist_jobs = _build_scientist_roles(SCIENTIST_DISCIPLINES)
    scholar_jobs = _build_scholar_roles(SCHOLAR_DISCIPLINES)

    lowercase_additional = {key.lower(): value for key, value in jobs_additional.items()}
    lowercase_primary = {key.lower(): value for key, value in jobs_primary.items()}

    combined_jobs = {**scientist_jobs, **scholar_jobs}

    for source in (lowercase_additional, lowercase_primary):
        for job_key, labels in source.items():
            if job_key in combined_jobs:
                continue
            if labels["males"] or labels["females"]:
                combined_jobs[job_key] = labels

    logger.debug(f"Built JOBS_2 with {len(combined_jobs)} entries")
    return combined_jobs, lowercase_additional


JOBS_2, JOBS_3333 = _build_jobs_datasets()

__all__ = [
    "JOBS_2",
    "JOBS_3333",
]

len_print.data_len(
    "Jobs2.py",
    {
        "JOBS_2": JOBS_2,
        "JOBS_3333": JOBS_3333,
    },
)

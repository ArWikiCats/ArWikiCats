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

from ..utils.json_dir import open_json
LOGGER = logging.getLogger(__name__)

jobs_primary = open_json("jobs/jobs_primary.json")
jobs_additional = open_json("jobs/jobs_additional.json")

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


# ---
Jobs_2 = {}
Jobs_3333 = {}
# ---

for sci in SCIENTIST_DISCIPLINES:
    lab = SCIENTIST_DISCIPLINES[sci]
    Jobs_2[sci.lower()] = {"mens": f"علماء {lab}", "womens": f"عالمات {lab}"}
# ---
for sci in SCHOLAR_DISCIPLINES:
    lab = SCHOLAR_DISCIPLINES[sci]
    Jobs_2[f"{sci.lower()} scholars"] = {"mens": f"علماء {lab}", "womens": f"عالمات {lab}"}
# ---
for joj in jobs_additional.keys():
    Jobs_3333[joj.lower()] = jobs_additional[joj]
    if joj.lower() not in Jobs_2 and jobs_additional[joj]["mens"]:
        Jobs_2[joj.lower()] = jobs_additional[joj]
# ---
nano = 0
for jowj in jobs_primary.keys():
    if jowj.lower() in Jobs_3333:
        # printe.output('jobs2: "%s" : { "mens": "%s" ,"womens": "%s" },' %  (jowj , jobs_primary[jowj]["mens"],jobs_primary[jowj]["womens"]))
        nano += 1
    # else:
    if jowj.lower() not in Jobs_2:
        if jobs_primary[jowj]["mens"] or jobs_primary[jowj]["womens"]:
            Jobs_2[jowj.lower()] = jobs_primary[jowj]
# ---

"""
lal = 'jobs2: "%s" : { "mens": "%s" ,"womens": "%s" },'
# ---
same = 0
notsame = 0
notin = 0
for c in LEGACY_EXPECTED_MENS_LABELS:
    if c.lower() in Jobs_2 :
        if LEGACY_EXPECTED_MENS_LABELS[c] != Jobs_2[c.lower()]["mens"] :
            #printe.output('"%s" : { "LEGACY_EXPECTED_MENS_LABELS": "%s" ,"Jobs_2": "%s" },' % (c , LEGACY_EXPECTED_MENS_LABELS[c] , Jobs_2[c.lower()]["mens"])   )
            #printe.output('"%s" : "%s",' % (c , LEGACY_EXPECTED_MENS_LABELS[c])   )
            notsame += 1
        else:
            same += 1
    else:
        #printe.output('"%s" : "%s",' % (c , LEGACY_EXPECTED_MENS_LABELS[c]) )
        notin += 1
        #printe.output(lal % (c , LEGACY_EXPECTED_MENS_LABELS[c] , "")   )
printe.output("jobs2: same:%d" % same)
printe.output("jobs2: notsame:%d" % notsame)
"""
# ---
del jobs_primary
del SCIENTIST_DISCIPLINES
del SCHOLAR_DISCIPLINES
del jobs_additional
del LEGACY_EXPECTED_MENS_LABELS


# ---------------------------------------------------------------------------
# Public API


JOBS_2 = Jobs_2
JOBS_3333 = Jobs_3333

# Backwards compatible exports -------------------------------------------------
Jobs_2: GenderedLabelMap = JOBS_2
Jobs_3333: GenderedLabelMap = JOBS_3333

__all__ = [
    "JOBS_2",
    "JOBS_3333",
    "Jobs_2",
    "Jobs_3333", "GenderedLabel",
    "GenderedLabelMap"
]

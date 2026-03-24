"""
jobs data
"""

from __future__ import annotations

from typing import Dict, List

from ..data_builders.build_jobs_data_basic import (
    _build_military_job_labels,
    _build_painter_job_labels,
    _build_religious_job_labels,
)
from ..data_builders.jobs_defs import GenderedLabelMap
from ..helps import len_print

# --- Religious role definitions -------------------------------------------------
# (?<!\w)(shi'a\ muslims|sunni\ muslims|shia\ muslims|shi'a\ muslim|sunni\ muslim|shia\ muslim|episcopalians|evangelical|christians|protestant|anglicans|christian|methodist|religious|venerated|anglican|buddhist|bahá'ís|yazidis|islamic|muslims|muslim|coptic|hindus|jewish|zaydis|saints|hindu|zaydi|sufis|nazi|jews)(?!\w)

RELIGIOUS_KEYS_PP: GenderedLabelMap = {
    "bahá'ís": {"males": "بهائيون", "females": "بهائيات"},
    "baháís": {"males": "بهائيون", "females": "بهائيات"},
    "yazidis": {"males": "يزيديون", "females": "يزيديات"},
    "christians": {"males": "مسيحيون", "females": "مسيحيات"},
    "anglican": {"males": "أنجليكيون", "females": "أنجليكيات"},
    "anglicans": {"males": "أنجليكيون", "females": "أنجليكيات"},
    "episcopalians": {"males": "أسقفيون", "females": "أسقفيات"},
    "christian": {"males": "مسيحيون", "females": "مسيحيات"},
    "buddhist": {"males": "بوذيون", "females": "بوذيات"},
    "nazi": {"males": "نازيون", "females": "نازيات"},
    "muslim": {"males": "مسلمون", "females": "مسلمات"},
    "coptic": {"males": "أقباط", "females": "قبطيات"},
    "islamic": {"males": "إسلاميون", "females": "إسلاميات"},
    "hindus": {"males": "هندوس", "females": "هندوسيات"},
    "hindu": {"males": "هندوس", "females": "هندوسيات"},
    "protestant": {"males": "بروتستانتيون", "females": "بروتستانتيات"},
    "methodist": {"males": "ميثوديون لاهوتيون", "females": "ميثوديات لاهوتيات"},
    "jewish": {"males": "يهود", "females": "يهوديات"},
    "jews": {"males": "يهود", "females": "يهوديات"},
    "zaydis": {"males": "زيود", "females": "زيديات"},
    "zaydi": {"males": "زيود", "females": "زيديات"},
    "sufis": {"males": "صوفيون", "females": "صوفيات"},
    "religious": {"males": "دينيون", "females": "دينيات"},
    "muslims": {"males": "مسلمون", "females": "مسلمات"},
    "shia muslims": {"males": "مسلمون شيعة", "females": "مسلمات شيعيات"},
    "shi'a muslims": {"males": "مسلمون شيعة", "females": "مسلمات شيعيات"},
    "sunni muslims": {"males": "مسلمون سنة", "females": "مسلمات سنيات"},
    "shia muslim": {"males": "مسلمون شيعة", "females": "مسلمات شيعيات"},
    "shi'a muslim": {"males": "مسلمون شيعة", "females": "مسلمات شيعيات"},
    "sunni muslim": {"males": "مسلمون سنة", "females": "مسلمات سنيات"},
    "evangelical": {"males": "إنجيليون", "females": "إنجيليات"},
    "venerated": {"males": "مبجلون", "females": "مبجلات"},
    "saints": {"males": "قديسون", "females": "قديسات"},
}

NAT_BEFORE_OCC_BASE: List[str] = [
    "murdered abroad",
    "contemporary",
    "tour de france stage winners",
    "deafblind",
    "deaf",
    "blind",
    "jews",
    "women's rights activists",
    "female rights activists",
    "human rights activists",
    "imprisoned",
    "imprisoned abroad",
    "conservationists",
    "expatriate",
    "defectors",
    "scholars of islam",
    "scholars-of-islam",
    "amputees",
    "expatriates",
    "executed abroad",
    "emigrants",
]

NAT_BEFORE_OCC = list(NAT_BEFORE_OCC_BASE)
NAT_BEFORE_OCC.extend(key for key in RELIGIOUS_KEYS_PP.keys())

RELIGIOUS_ROLE_LABELS: GenderedLabelMap = {
    "christians": {"males": "مسيحيون", "females": "مسيحيات"},
    "venerated": {"males": "مبجلون", "females": "مبجلات"},
    "missionaries": {"males": "مبشرون", "females": "مبشرات"},
    "evangelical": {"males": "إنجيليون", "females": "إنجيليات"},
    "monks": {"males": "رهبان", "females": "راهبات"},
    "nuns": {"males": "", "females": "راهبات"},
    "saints": {"males": "قديسون", "females": "قديسات"},
    "astrologers": {"males": "منجمون", "females": "منجمات"},
    "leaders": {"males": "قادة", "females": "قائدات"},
    "bishops": {"males": "أساقفة", "females": ""},
    "actors": {"males": "ممثلون", "females": "ممثلات"},
    "theologians": {"males": "لاهوتيون", "females": "لاهوتيات"},
    "clergy": {"males": "رجال دين", "females": "سيدات دين"},
    "religious leaders": {"males": "قادة دينيون", "females": "قائدات دينيات"},
}


# --- Painter role definitions ---------------------------------------------------
PAINTER_STYLES: GenderedLabelMap = {
    "symbolist": {"males": "رمزيون", "females": "رمزيات"},
    "history": {"males": "تاريخيون", "females": "تاريخيات"},
    "romantic": {"males": "رومانسيون", "females": "رومانسيات"},
    "neoclassical": {"males": "كلاسيكيون حديثون", "females": "كلاسيكيات حديثات"},
    "religious": {"males": "دينيون", "females": "دينيات"},
}

PAINTER_ROLE_LABELS: GenderedLabelMap = {
    "painters": {"males": "رسامون", "females": "رسامات"},
    "artists": {"males": "فنانون", "females": "فنانات"},
}

PAINTER_CATEGORY_LABELS: Dict[str, str] = {
    "make-up": "مكياج",
    "comics": "قصص مصورة",
    "marvel comics": "مارفال كومكس",
    "manga": "مانغا",
    "landscape": "مناظر طبيعية",
    "wildlife": "حياة برية",
    "portrait": "بورتريه",
    "animal": "حيوانات",
    "genre": "نوع",
    "still life": "طبيعة صامتة",
}

# --- Military role definitions --------------------------------------------------
MILITARY_PREFIXES: GenderedLabelMap = {
    "military": {"males": "عسكريون", "females": "عسكريات"},
    "politicians": {"males": "سياسيون", "females": "سياسيات"},
    "nazi": {"males": "نازيون", "females": "نازيات"},
    "literary": {"males": "أدبيون", "females": "أدبيات"},
    "organizational": {"males": "تنظيميون", "females": "تنظيميات"},
}

MILITARY_ROLE_LABELS: GenderedLabelMap = {
    "theorists": {"males": "منظرون", "females": "منظرات"},
    "musicians": {"males": "موسيقيون", "females": "موسيقيات"},
    "engineers": {"males": "مهندسون", "females": "مهندسات"},
    "leaders": {"males": "قادة", "females": "قائدات"},
    "officers": {"males": "ضباط", "females": "ضابطات"},
    "historians": {"males": "مؤرخون", "females": "مؤرخات"},
    "strategists": {"males": "استراتيجيون", "females": "استراتيجيات"},
    "nurses": {"males": "ممرضون", "females": "ممرضات"},
}

EXCLUDED_MILITARY_PREFIXES = ("military", "literary")


# --- Aggregate outputs ----------------------------------------------------------
MEN_WOMENS_JOBS_2: GenderedLabelMap = {}
MEN_WOMENS_JOBS_2.update(_build_religious_job_labels(RELIGIOUS_KEYS_PP, RELIGIOUS_ROLE_LABELS))

MEN_WOMENS_JOBS_2.update(_build_painter_job_labels(PAINTER_STYLES, PAINTER_ROLE_LABELS, PAINTER_CATEGORY_LABELS))

MEN_WOMENS_JOBS_2.update(
    _build_military_job_labels(
        MILITARY_PREFIXES,
        MILITARY_ROLE_LABELS,
        EXCLUDED_MILITARY_PREFIXES,
    )
)

__all__ = [
    "MEN_WOMENS_JOBS_2",
    "MILITARY_PREFIXES",
    "MILITARY_ROLE_LABELS",
    "PAINTER_CATEGORY_LABELS",
    "PAINTER_ROLE_LABELS",
    "PAINTER_STYLES",
    "RELIGIOUS_KEYS_PP",
    "NAT_BEFORE_OCC",
]

len_print.data_len(
    "jobs_data_basic.py",
    {
        "MEN_WOMENS_JOBS_2": MEN_WOMENS_JOBS_2,
        "MILITARY_PREFIXES": MILITARY_PREFIXES,
        "MILITARY_ROLE_LABELS": MILITARY_ROLE_LABELS,
        "PAINTER_CATEGORY_LABELS": PAINTER_CATEGORY_LABELS,
        "PAINTER_ROLE_LABELS": PAINTER_ROLE_LABELS,
        "PAINTER_STYLES": PAINTER_STYLES,
        "RELIGIOUS_KEYS_PP": RELIGIOUS_KEYS_PP,
        "NAT_BEFORE_OCC": NAT_BEFORE_OCC,
    },
)

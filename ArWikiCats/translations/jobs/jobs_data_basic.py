"""
jobs data
"""

from __future__ import annotations

from typing import Dict, Iterable, List, Mapping

from ...helps import len_print
from .jobs_defs import GenderedLabel, GenderedLabelMap


def _build_religious_job_labels(
    religions: Mapping[str, GenderedLabel],
    roles: Mapping[str, GenderedLabel],
) -> GenderedLabelMap:
    """Generate gendered labels for religious roles.

    Args:
        religions: Mapping of religion identifiers to their gendered labels.
        roles: Mapping of religious roles to gendered labels.

    Returns:
        A dictionary keyed by string templates representing the combination of
        religion and role, matching the original dataset used by downstream
        modules.
    """

    combined_roles: GenderedLabelMap = {}
    for religion_key, religion_labels in religions.items():
        for role_key, role_labels in roles.items():
            womens_label = f"{role_labels['womens']} {religion_labels['womens']}" if role_labels["females"] else ""
            combined_roles[f"{religion_key} {role_key}"] = {
                "mens": f"{role_labels['mens']} {religion_labels['mens']}",
                "females": womens_label,
            }

    return combined_roles


def _build_painter_job_labels(
    painter_styles: Mapping[str, GenderedLabel],
    painter_roles: Mapping[str, GenderedLabel],
    painter_categories: Mapping[str, str],
) -> GenderedLabelMap:
    """Construct gendered labels for painting and artistic roles.

    Args:
        painter_styles: Mapping of painter descriptors (e.g. ``symbolist``) to
            their gendered Arabic forms.
        painter_roles: Mapping of artistic roles associated with painting.
        painter_categories: Additional label categories that are appended as
            human-readable Arabic strings.

    Returns:
        A dictionary containing both base roles and combined painter role
        variants.
    """
    # _build_painter_job_labels(PAINTER_STYLES, PAINTER_ROLE_LABELS, PAINTER_CATEGORY_LABELS)
    combined_data: GenderedLabelMap = {role_key: role_labels for role_key, role_labels in painter_roles.items()}

    combined_data.update({_style: _labels for _style, _labels in painter_styles.items() if _style != "history"})
    for style_key, style_labels in painter_styles.items():
        for role_key, role_labels in painter_roles.items():
            composite_key = f"{style_key} {role_key}"
            combined_data[composite_key] = {
                "mens": f"{role_labels['mens']} {style_labels['mens']}",
                "females": f"{role_labels['womens']} {style_labels['womens']}",
            }
    for painter_category, category_label in painter_categories.items():
        combined_data[f"{painter_category} painters"] = {
            "mens": f"رسامو {category_label}",
            "females": f"رسامات {category_label}",
        }
        combined_data[f"{painter_category} artists"] = {
            "mens": f"فنانو {category_label}",
            "females": f"فنانات {category_label}",
        }

    return combined_data


def _build_military_job_labels(
    military_prefixes: Mapping[str, GenderedLabel],
    military_roles: Mapping[str, GenderedLabel],
    excluded_prefixes: Iterable[str],
) -> GenderedLabelMap:
    """Construct gendered labels for military related jobs.

    Args:
        military_prefixes: Base labels that modify the general military roles.
        military_roles: Roles that can be combined with each prefix.
        excluded_prefixes: Prefix keys that should not be added directly to the
            result set but are still used for composite roles.

    Returns:
        A dictionary of gendered labels covering both base roles and composite
        role names.
    """
    excluded = set(excluded_prefixes)

    combined_roles: GenderedLabelMap = {role_key: role_labels for role_key, role_labels in military_roles.items()}

    combined_roles.update(
        {
            prefix_key: prefix_labels
            for prefix_key, prefix_labels in military_prefixes.items()
            if prefix_key not in excluded
        }
    )

    for military_key, prefix_labels in military_prefixes.items():
        for role_key, role_labels in military_roles.items():
            composite_key = f"{military_key} {role_key}"
            combined_roles[composite_key] = {
                "mens": f"{role_labels['mens']} {prefix_labels['mens']}",
                "females": f"{role_labels['womens']} {prefix_labels['womens']}",
            }

    return combined_roles


# --- Religious role definitions -------------------------------------------------
# (?<!\w)(shi'a\ muslims|sunni\ muslims|shia\ muslims|shi'a\ muslim|sunni\ muslim|shia\ muslim|episcopalians|evangelical|christians|protestant|anglicans|christian|methodist|religious|venerated|anglican|buddhist|bahá'ís|yazidis|islamic|muslims|muslim|coptic|hindus|jewish|zaydis|saints|hindu|zaydi|sufis|nazi|jews)(?!\w)
RELIGIOUS_KEYS_PP: GenderedLabelMap = {
    "bahá'ís": {"mens": "بهائيون", "females": "بهائيات"},
    "yazidis": {"mens": "يزيديون", "females": "يزيديات"},
    "christians": {"mens": "مسيحيون", "females": "مسيحيات"},
    "anglican": {"mens": "أنجليكيون", "females": "أنجليكيات"},
    "anglicans": {"mens": "أنجليكيون", "females": "أنجليكيات"},
    "episcopalians": {"mens": "أسقفيون", "females": "أسقفيات"},
    "christian": {"mens": "مسيحيون", "females": "مسيحيات"},
    "buddhist": {"mens": "بوذيون", "females": "بوذيات"},
    "nazi": {"mens": "نازيون", "females": "نازيات"},
    "muslim": {"mens": "مسلمون", "females": "مسلمات"},
    "coptic": {"mens": "أقباط", "females": "قبطيات"},
    "islamic": {"mens": "إسلاميون", "females": "إسلاميات"},
    "hindus": {"mens": "هندوس", "females": "هندوسيات"},
    "hindu": {"mens": "هندوس", "females": "هندوسيات"},
    "protestant": {"mens": "بروتستانتيون", "females": "بروتستانتيات"},
    "methodist": {"mens": "ميثوديون لاهوتيون", "females": "ميثوديات لاهوتيات"},
    "jewish": {"mens": "يهود", "females": "يهوديات"},
    "jews": {"mens": "يهود", "females": "يهوديات"},
    "zaydis": {"mens": "زيود", "females": "زيديات"},
    "zaydi": {"mens": "زيود", "females": "زيديات"},
    "sufis": {"mens": "صوفيون", "females": "صوفيات"},
    "religious": {"mens": "دينيون", "females": "دينيات"},
    "muslims": {"mens": "مسلمون", "females": "مسلمات"},
    "shia muslims": {"mens": "مسلمون شيعة", "females": "مسلمات شيعيات"},
    "shi'a muslims": {"mens": "مسلمون شيعة", "females": "مسلمات شيعيات"},
    "sunni muslims": {"mens": "مسلمون سنة", "females": "مسلمات سنيات"},
    "shia muslim": {"mens": "مسلمون شيعة", "females": "مسلمات شيعيات"},
    "shi'a muslim": {"mens": "مسلمون شيعة", "females": "مسلمات شيعيات"},
    "sunni muslim": {"mens": "مسلمون سنة", "females": "مسلمات سنيات"},
    "evangelical": {"mens": "إنجيليون", "females": "إنجيليات"},
    "venerated": {"mens": "مبجلون", "females": "مبجلات"},
    "saints": {"mens": "قديسون", "females": "قديسات"},
}

NAT_BEFORE_OCC_BASE: List[str] = [
    "convicted-of-murder",
    "murdered abroad",
    "contemporary",
    "tour de france stage winners",
    "deafblind",
    "deaf",
    "blind",
    "jews",
    "women's rights activists",
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
    "christians": {"mens": "مسيحيون", "females": "مسيحيات"},
    "venerated": {"mens": "مبجلون", "females": "مبجلات"},
    "missionaries": {"mens": "مبشرون", "females": "مبشرات"},
    "evangelical": {"mens": "إنجيليون", "females": "إنجيليات"},
    "monks": {"mens": "رهبان", "females": "راهبات"},
    "nuns": {"mens": "", "females": "راهبات"},
    "saints": {"mens": "قديسون", "females": "قديسات"},
    "astrologers": {"mens": "منجمون", "females": "منجمات"},
    "leaders": {"mens": "قادة", "females": "قائدات"},
    "bishops": {"mens": "أساقفة", "females": ""},
    "actors": {"mens": "ممثلون", "females": "ممثلات"},
    "theologians": {"mens": "لاهوتيون", "females": "لاهوتيات"},
    "clergy": {"mens": "رجال دين", "females": "سيدات دين"},
    "religious leaders": {"mens": "قادة دينيون", "females": "قائدات دينيات"},
}


# --- Painter role definitions ---------------------------------------------------
PAINTER_STYLES: GenderedLabelMap = {
    "symbolist": {"mens": "رمزيون", "females": "رمزيات"},
    "history": {"mens": "تاريخيون", "females": "تاريخيات"},
    "romantic": {"mens": "رومانسيون", "females": "رومانسيات"},
    "neoclassical": {"mens": "كلاسيكيون حديثون", "females": "كلاسيكيات حديثات"},
    "religious": {"mens": "دينيون", "females": "دينيات"},
}

PAINTER_ROLE_LABELS: GenderedLabelMap = {
    "painters": {"mens": "رسامون", "females": "رسامات"},
    "artists": {"mens": "فنانون", "females": "فنانات"},
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
    "military": {"mens": "عسكريون", "females": "عسكريات"},
    "politicians": {"mens": "سياسيون", "females": "سياسيات"},
    "nazi": {"mens": "نازيون", "females": "نازيات"},
    "literary": {"mens": "أدبيون", "females": "أدبيات"},
    "organizational": {"mens": "تنظيميون", "females": "تنظيميات"},
}

MILITARY_ROLE_LABELS: GenderedLabelMap = {
    "theorists": {"mens": "منظرون", "females": "منظرات"},
    "musicians": {"mens": "موسيقيون", "females": "موسيقيات"},
    "engineers": {"mens": "مهندسون", "females": "مهندسات"},
    "leaders": {"mens": "قادة", "females": "قائدات"},
    "officers": {"mens": "ضباط", "females": "ضابطات"},
    "historians": {"mens": "مؤرخون", "females": "مؤرخات"},
    "strategists": {"mens": "استراتيجيون", "females": "استراتيجيات"},
    "nurses": {"mens": "ممرضون", "females": "ممرضات"},
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
    "RELIGIOUS_ROLE_LABELS",
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
        "RELIGIOUS_ROLE_LABELS": RELIGIOUS_ROLE_LABELS,
        "NAT_BEFORE_OCC": NAT_BEFORE_OCC,
    },
)

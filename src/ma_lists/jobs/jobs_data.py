"""
jobs data
"""

from __future__ import annotations

from typing import Dict, Mapping, Iterable, List

from .jobs_defs import (
    GenderedLabel,
    GenderedLabelMap,
)


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
            womens_label = (
                f'{role_labels["womens"]} {religion_labels["womens"]}'
                if role_labels["womens"]
                else ""
            )
            combined_roles[f"{religion_key} {role_key}"] = {
                "mens": f'{role_labels["mens"]} {religion_labels["mens"]}',
                "womens": womens_label,
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
    # ---
    combined_data: GenderedLabelMap = {role_key: role_labels for role_key, role_labels in painter_roles.items()}

    combined_data.update({_style: _labels for _style, _labels in painter_styles.items() if _style != "history"})
    # ---
    for style_key, style_labels in painter_styles.items():
        for role_key, role_labels in painter_roles.items():
            composite_key = f"{style_key} {role_key}"
            # ---
            combined_data[composite_key] = {
                "mens": f"{role_labels['mens']} {style_labels['mens']}",
                "womens": f"{role_labels['womens']} {style_labels['womens']}"
            }

    # ---
    for painter_category, category_label in painter_categories.items():
        combined_data[f"{painter_category} painters"] = {
            "mens": f"رسامو {category_label}",
            "womens": f"رسامات {category_label}",
        }
        combined_data[f"{painter_category} artists"] = {
            "mens": f"فنانو {category_label}",
            "womens": f"فنانات {category_label}",
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

    combined_roles.update({
        prefix_key: prefix_labels
        for prefix_key, prefix_labels
        in military_prefixes.items()
        if prefix_key not in excluded
    })

    for military_key, prefix_labels in military_prefixes.items():
        for role_key, role_labels in military_roles.items():
            # ---
            composite_key = f"{military_key} {role_key}"
            # ---
            combined_roles[composite_key] = {
                "mens": f"{role_labels['mens']} {prefix_labels['mens']}",
                "womens": f"{role_labels['womens']} {prefix_labels['womens']}"
            }

    return combined_roles


# --- Religious role definitions -------------------------------------------------
RELIGIOUS_KEYS_PP: GenderedLabelMap = {
    "bahá'ís": {"mens": "بهائيون", "womens": "بهائيات"},
    "yazidis": {"mens": "يزيديون", "womens": "يزيديات"},
    "christians": {"mens": "مسيحيون", "womens": "مسيحيات"},
    "anglican": {"mens": "أنجليكيون", "womens": "أنجليكيات"},
    "anglicans": {"mens": "أنجليكيون", "womens": "أنجليكيات"},
    "episcopalians": {"mens": "أسقفيون", "womens": "أسقفيات"},
    "christian": {"mens": "مسيحيون", "womens": "مسيحيات"},
    "buddhist": {"mens": "بوذيون", "womens": "بوذيات"},
    "nazi": {"mens": "نازيون", "womens": "نازيات"},
    "muslim": {"mens": "مسلمون", "womens": "مسلمات"},
    "coptic": {"mens": "أقباط", "womens": "قبطيات"},
    "islamic": {"mens": "إسلاميون", "womens": "إسلاميات"},
    "hindus": {"mens": "هندوس", "womens": "هندوسيات"},
    "hindu": {"mens": "هندوس", "womens": "هندوسيات"},
    "protestant": {"mens": "بروتستانتيون", "womens": "بروتستانتيات"},
    "methodist": {"mens": "ميثوديون لاهوتيون", "womens": "ميثوديات لاهوتيات"},
    "jewish": {"mens": "يهود", "womens": "يهوديات"},
    "jews": {"mens": "يهود", "womens": "يهوديات"},
    "zaydis": {"mens": "زيود", "womens": "زيديات"},
    "zaydi": {"mens": "زيود", "womens": "زيديات"},
    "sufis": {"mens": "صوفيون", "womens": "صوفيات"},
    "religious": {"mens": "دينيون", "womens": "دينيات"},
    "muslims": {"mens": "مسلمون", "womens": "مسلمات"},
    "shia muslims": {"mens": "مسلمون شيعة", "womens": "مسلمات شيعيات"},
    "shi'a muslims": {"mens": "مسلمون شيعة", "womens": "مسلمات شيعيات"},
    "sunni muslims": {"mens": "مسلمون سنة", "womens": "مسلمات سنيات"},
    "shia muslim": {"mens": "مسلمون شيعة", "womens": "مسلمات شيعيات"},
    "shi'a muslim": {"mens": "مسلمون شيعة", "womens": "مسلمات شيعيات"},
    "sunni muslim": {"mens": "مسلمون سنة", "womens": "مسلمات سنيات"},
    "evangelical": {"mens": "إنجيليون", "womens": "إنجيليات"},
    "venerated": {"mens": "مبجلون", "womens": "مبجلات"},
    "saints": {"mens": "قديسون", "womens": "قديسات"},
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
    "scholars of",
    "executed abroad",
    "emigrants",
]

NAT_BEFORE_OCC = list(NAT_BEFORE_OCC_BASE)
NAT_BEFORE_OCC.extend(key for key in RELIGIOUS_KEYS_PP.keys())

RELIGIOUS_ROLE_LABELS: GenderedLabelMap = {
    "christians": {"mens": "مسيحيون", "womens": "مسيحيات"},
    "venerated": {"mens": "مبجلون", "womens": "مبجلات"},
    "missionaries": {"mens": "مبشرون", "womens": "مبشرات"},
    "evangelical": {"mens": "إنجيليون", "womens": "إنجيليات"},
    "monks": {"mens": "رهبان", "womens": "راهبات"},
    "nuns": {"mens": "", "womens": "راهبات"},
    "saints": {"mens": "قديسون", "womens": "قديسات"},
    "astrologers": {"mens": "منجمون", "womens": "منجمات"},
    "leaders": {"mens": "قادة", "womens": "قائدات"},
    "bishops": {"mens": "أساقفة", "womens": ""},
    "actors": {"mens": "ممثلون", "womens": "ممثلات"},
    "theologians": {"mens": "لاهوتيون", "womens": "لاهوتيات"},
    "clergy": {"mens": "رجال دين", "womens": "سيدات دين"},
    "religious leaders": {"mens": "قادة دينيون", "womens": "قائدات دينيات"},
}


# --- Painter role definitions ---------------------------------------------------
PAINTER_STYLES: GenderedLabelMap = {
    "symbolist": {"mens": "رمزيون", "womens": "رمزيات"},
    "history": {"mens": "تاريخيون", "womens": "تاريخيات"},
    "romantic": {"mens": "رومانسيون", "womens": "رومانسيات"},
    "neoclassical": {"mens": "كلاسيكيون حديثون", "womens": "كلاسيكيات حديثات"},
    "religious": {"mens": "دينيون", "womens": "دينيات"},
}

PAINTER_ROLE_LABELS: GenderedLabelMap = {
    "painters": {"mens": "رسامون", "womens": "رسامات"},
    "artists": {"mens": "فنانون", "womens": "فنانات"},
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
    "military": {"mens": "عسكريون", "womens": "عسكريات"},
    "politicians": {"mens": "سياسيون", "womens": "سياسيات"},
    "nazi": {"mens": "نازيون", "womens": "نازيات"},
    "literary": {"mens": "أدبيون", "womens": "أدبيات"},
    "organizational": {"mens": "تنظيميون", "womens": "تنظيميات"},
}

MILITARY_ROLE_LABELS: GenderedLabelMap = {
    "theorists": {"mens": "منظرون", "womens": "منظرات"},
    "musicians": {"mens": "موسيقيون", "womens": "موسيقيات"},
    "engineers": {"mens": "مهندسون", "womens": "مهندسات"},
    "leaders": {"mens": "قادة", "womens": "قائدات"},
    "officers": {"mens": "ضباط", "womens": "ضابطات"},
    "historians": {"mens": "مؤرخون", "womens": "مؤرخات"},
    "strategists": {"mens": "استراتيجيون", "womens": "استراتيجيات"},
    "nurses": {"mens": "ممرضون", "womens": "ممرضات"},
}

EXCLUDED_MILITARY_PREFIXES = ("military", "literary")


# --- Aggregate outputs ----------------------------------------------------------
MEN_WOMENS_JOBS_2: GenderedLabelMap = {}
MEN_WOMENS_JOBS_2.update(_build_religious_job_labels(RELIGIOUS_KEYS_PP, RELIGIOUS_ROLE_LABELS))

MEN_WOMENS_JOBS_2.update(
    _build_painter_job_labels(PAINTER_STYLES, PAINTER_ROLE_LABELS, PAINTER_CATEGORY_LABELS)
)

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

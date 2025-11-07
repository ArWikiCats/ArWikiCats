"""Utilities for managing gendered Arabic labels used across job modules.

This module replaces hand-written dictionary concatenation with typed helper
functions.  Each helper keeps the original Arabic content intact while
documenting the logic used to combine masculine and feminine labels.
"""

from __future__ import annotations

from typing import Dict, Iterable, Mapping, TypedDict


class GenderedLabel(TypedDict):
    """Represent an Arabic label split into masculine and feminine forms."""

    mens: str
    womens: str


GenderedLabelMap = Dict[str, GenderedLabel]


def _join_terms(*terms: str) -> str:
    """Join non-empty terms with a single space.

    Args:
        *terms: Terms that should be concatenated.

    Returns:
        A single string that concatenates the provided terms while skipping
        empty values.  The function is intentionally small because it is used
        repeatedly when combining base labels with modifiers.
    """

    filtered_terms = [term for term in terms if term]
    return " ".join(filtered_terms)


def _combine_gendered_labels(
    base_labels: GenderedLabel,
    suffix_labels: GenderedLabel,
    *,
    require_base_womens: bool = False,
) -> GenderedLabel:
    """Merge two :class:`GenderedLabel` mappings.

    Args:
        base_labels: The primary role labels.
        suffix_labels: The modifiers appended to the base labels.
        require_base_womens: When ``True`` the feminine label is emitted only if
            the base feminine label is available.  This mirrors the legacy
            behaviour used for some religious titles where the feminine form
            should remain empty unless explicitly defined for the base role.

    Returns:
        A new mapping containing concatenated masculine and feminine labels.
    """

    mens_label = _join_terms(base_labels["mens"], suffix_labels["mens"])
    womens_label = ""
    if not require_base_womens or base_labels["womens"]:
        womens_label = _join_terms(base_labels["womens"], suffix_labels["womens"])
    return {"mens": mens_label, "womens": womens_label}


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
        label_template = f"{religion_key} %s"
        for role_key, role_labels in roles.items():
            combined_roles[label_template % role_key] = _combine_gendered_labels(role_labels, religion_labels, require_base_womens=True)
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

    combined_roles: GenderedLabelMap = {role_key: role_labels for role_key, role_labels in painter_roles.items()}

    for style_key, style_labels in painter_styles.items():
        if style_key != "history":
            combined_roles[style_key] = style_labels

        for role_key, role_labels in painter_roles.items():
            composite_key = f"{style_key} {role_key}"
            combined_roles[composite_key] = _combine_gendered_labels(role_labels, style_labels)

    for category_key, category_label in painter_categories.items():
        combined_roles[f"{category_key} painters"] = {
            "mens": f"رسامو {category_label}",
            "womens": f"رسامات {category_label}",
        }
        combined_roles[f"{category_key} artists"] = {
            "mens": f"فنانو {category_label}",
            "womens": f"فنانات {category_label}",
        }

    return combined_roles


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

    combined_roles: GenderedLabelMap = {role_key: role_labels for role_key, role_labels in military_roles.items()}

    excluded = set(excluded_prefixes)
    for prefix_key, prefix_labels in military_prefixes.items():
        if prefix_key not in excluded:
            combined_roles[prefix_key] = prefix_labels

        for role_key, role_labels in military_roles.items():
            composite_key = f"{prefix_key} {role_key}"
            combined_roles[composite_key] = _combine_gendered_labels(role_labels, prefix_labels)

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
    _build_painter_job_labels(
        PAINTER_STYLES,
        PAINTER_ROLE_LABELS,
        PAINTER_CATEGORY_LABELS,
    )
)
MEN_WOMENS_JOBS_2.update(
    _build_military_job_labels(
        MILITARY_PREFIXES,
        MILITARY_ROLE_LABELS,
        EXCLUDED_MILITARY_PREFIXES,
    )
)


# --- Backwards compatibility exports -------------------------------------------
# The original module exposed ``religious_keys_PP`` and ``Men_Womens_Jobs_2``
# using mixed-case identifiers.  Retain those names for callers that have not
# yet migrated to the uppercase constants.
religious_keys_PP: GenderedLabelMap = RELIGIOUS_KEYS_PP
Men_Womens_Jobs_2: GenderedLabelMap = MEN_WOMENS_JOBS_2


__all__ = [
    "GenderedLabel",
    "GenderedLabelMap",
    "MEN_WOMENS_JOBS_2",
    "MILITARY_PREFIXES",
    "MILITARY_ROLE_LABELS",
    "PAINTER_CATEGORY_LABELS",
    "PAINTER_ROLE_LABELS",
    "PAINTER_STYLES",
    "RELIGIOUS_KEYS_PP",
    "RELIGIOUS_ROLE_LABELS",
    "Men_Womens_Jobs_2",
    "religious_keys_PP",
]

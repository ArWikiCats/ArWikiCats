"""Static lookup tables used by multiple sports modules.

The module mostly contains translation dictionaries that are reused across
different sports builders.  The dictionaries keep placeholder tokens such as
``{nat}`` which are later formatted by the calling code.
"""

from __future__ import annotations

from collections.abc import Mapping
from typing import Final

from ._helpers import YEARS, extend_with_templates, extend_with_year_templates

# Mapping of prefixes (menstt333) used when generating nationality based
# templates.  The strings keep ``{}`` placeholders which are filled either at
# dictionary creation time or by consumers when the final value is required.
MENSTT333: Final[dict[str, str]] = {
    "": "{}",
    "national": "{}",
    "national youth": "{} للشباب",
    "national amateur": "{} للهواة",
    "national junior men's": "{} للناشئين",
    "national junior women's": "{} للناشئات",
    "national men's": "{} للرجال",
    "national women's": "{} للسيدات",
    "multi-national women's": "{} متعددة الجنسيات للسيدات",
    "national youth women's": "{} للشابات",
}

# The MENSTT333 values are re-used with ``{nat}`` placeholders in some
# contexts, therefore we prepare a second mapping that already incorporates
# the placeholder in its value.
NAT_MENSTT33: Final[dict[str, str]] = {key: value.replace("{}", "{nat}") for key, value in MENSTT333.items()}


def _build_new_tato_nat() -> dict[str, str]:
    """Construct the ``New_Tato_nat`` dictionary.

    The data expands ``NAT_MENSTT33`` by adding templates for different age
    categories.  ``{nat}`` remains a placeholder in the resulting strings.
    """

    result: dict[str, str] = {}
    for template_key, template_label in NAT_MENSTT33.items():
        extend_with_templates(result, {template_key: template_label}, nat="{nat}")

        year_templates: Mapping[str, str] = {f"{template_key} under-{{year}}": template_label.replace("{nat}", "{nat} تحت {year} سنة")}
        extend_with_year_templates(result, year_templates, nat="{nat}")
    return result


NEW_TATO_NAT: Final[dict[str, str]] = _build_new_tato_nat()

# Gender/age qualifiers applied to job and team dictionaries when generating
# composite keys.
PPP_KEYS: Final[dict[str, str]] = {
    "men's": "رجالية",
    "women's": "نسائية",
    "youth": "شبابية",
    "men's youth": "للشباب",
    "women's youth": "للشابات",
    "amateur": "للهواة",
}

# League levels used when describing national competitions.  Consumers provide
# the base label (``{lab}``) for the translation.
LEVELS: Final[dict[str, str]] = {
    "premier": "الدرجة الممتازة",
    "top level": "الدرجة الأولى",
    "first level": "الدرجة الأولى",
    "first tier": "الدرجة الأولى",
    "second level": "الدرجة الثانية",
    "second tier": "الدرجة الثانية",
    "third level": "الدرجة الثالثة",
    "third tier": "الدرجة الثالثة",
    "fourth level": "الدرجة الرابعة",
    "fourth tier": "الدرجة الرابعة",
    "fifth level": "الدرجة الخامسة",
    "fifth tier": "الدرجة الخامسة",
    "sixth level": "الدرجة السادسة",
    "sixth tier": "الدرجة السادسة",
    "seventh level": "الدرجة السابعة",
    "seventh tier": "الدرجة السابعة",
}

# Keys appended after a base sport name when generating extended templates.
AFTER_KEYS: Final[dict[str, str]] = {
    "squads": "تشكيلات",
    "finals": "نهائيات",
    "positions": "مراكز",
    "tournaments": "بطولات",
    "films": "أفلام",
    "teams": "فرق",
    "venues": "ملاعب",
    "clubs": "أندية",
    "organizations": "منظمات",
    "non-profit organizations": "منظمات غير ربحية",
    "non-profit publishers": "ناشرون غير ربحيون",
    "organisations": "منظمات",
    "events": "أحداث",
    "umpires": "حكام",
    "trainers": "مدربو",
    "scouts": "كشافة",
    "coaches": "مدربو",
    "leagues": "دوريات",
    "managers": "مدربو",
    "playerss": "لاعبو",
    "players": "لاعبو",
    "results": "نتائج",
    "matches": "مباريات",
    "navigational boxes": "صناديق تصفح",
    "lists": "قوائم",
    "home stadiums": "ملاعب",
    "templates": "قوالب",
    "rivalries": "دربيات",
    "champions": "أبطال",
    "competitions": "منافسات",
    "statistics": "إحصائيات",
    "records": "سجلات",
    "records and statistics": "سجلات وإحصائيات",
    "manager history": "تاريخ مدربو",
}

# Templates used when building team specific suffixes.
AFTER_KEYS_TEAM: Final[dict[str, str]] = {
    "team": "{}",
    "team umpires": "حكام {}",
    "team trainers": "مدربو {}",
    "team scouts": "كشافة {}",
}

# Templates applied to national teams.  ``{lab}`` is supplied by the caller
# and usually corresponds to a translated sport label.
AFTER_KEYS_NAT: Final[dict[str, str]] = {
    "": "{lab}",
    "second level leagues": "دوريات {lab} من الدرجة الثانية",
    "second tier leagues": "دوريات {lab} من الدرجة الثانية",
}


def _extend_suffix_mappings() -> None:
    """Populate ``AFTER_KEYS_TEAM`` and ``AFTER_KEYS_NAT`` with variants."""

    for suffix_key, suffix_label in AFTER_KEYS.items():
        AFTER_KEYS_TEAM[f"team {suffix_key}"] = f"{suffix_label} {{}}"
        AFTER_KEYS_NAT[suffix_key] = f"{suffix_label} {{lab}}"

    for level_key, level_label in LEVELS.items():
        AFTER_KEYS_NAT[f"{level_key} league"] = f"دوريات {{lab}} من {level_label}"
        AFTER_KEYS_NAT[f"{level_key} leagues"] = f"دوريات {{lab}} من {level_label}"


_extend_suffix_mappings()

# Backwards compatibility aliases -------------------------------------------------
#
# Historical consumers import the lowercase/TitleCase names.  Provide aliases so
# that the refactor that introduced uppercase constants remains source
# compatible.
levels: Final[dict[str, str]] = LEVELS
New_Tato_nat: Final[dict[str, str]] = NEW_TATO_NAT
menstt333: Final[dict[str, str]] = MENSTT333

__all__ = [
    "AFTER_KEYS",
    "AFTER_KEYS_NAT",
    "AFTER_KEYS_TEAM",
    "LEVELS",
    "MENSTT333",
    "NAT_MENSTT33",
    "NEW_TATO_NAT",
    "PPP_KEYS",
    "YEARS",
    "levels",
    "New_Tato_nat",
    "menstt333",
]

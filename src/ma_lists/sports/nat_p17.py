"""Nationality aware sport templates used by p17 infoboxes."""

from __future__ import annotations

import logging
from collections.abc import Mapping
from typing import Final

from .Sport_key import SPORTS_KEYS_FOR_TEAM
from ._helpers import extend_with_templates, extend_with_year_templates, log_length_stats

LOGGER = logging.getLogger(__name__)

NAT_PLACEHOLDER: Final[str] = "{nat}"
CHAMPIONSHIP_SUFFIXES: Final[tuple[str, str]] = ("championships", "championship")

TYPE_LABELS: Final[dict[str, str]] = {
    "cups": "كؤوس",
    "clubs": "أندية",
    "competitions": "منافسات",
    "leagues": "دوريات",
    "coaches": "مدربو",
}


def _build_championship_templates(team: str, label: str) -> dict[str, str]:
    """Generate templates covering championship terminology for ``team``."""

    templates: dict[str, str] = {}

    for suffix in CHAMPIONSHIP_SUFFIXES:
        extend_with_templates(
            templates,
            {
                "{team} {suffix}": "بطولة {nat} {label}",
                "youth {team} {suffix}": "بطولة {nat} {label} للشباب",
                "men's {team} {suffix}": "بطولة {nat} {label} للرجال",
                "women's {team} {suffix}": "بطولة {nat} {label} للسيدات",
                "amateur {team} {suffix}": "بطولة {nat} {label} للهواة",
                "outdoor {team} {suffix}": "بطولة {nat} {label} في الهواء الطلق",
                "{team} indoor {suffix}": "بطولة {nat} {label} داخل الصالات",
            },
            team=team,
            label=label,
            suffix=suffix,
            nat=NAT_PLACEHOLDER,
        )

    extend_with_year_templates(
        templates,
        {
            "{team} u{year} championships": "بطولة {nat} {label} تحت {year} سنة",
            "{team} u-{year} championships": "بطولة {nat} {label} تحت {year} سنة",
        },
        team=team,
        label=label,
        nat=NAT_PLACEHOLDER,
    )

    extend_with_templates(
        templates,
        {
            "{team} junior championships": "بطولة {nat} {label} للناشئين",
            "championships ({team})": "بطولة {nat} {label}",
            "championships {team}": "بطولة {nat} {label}",
            "open ({team})": "{nat} المفتوحة {label}",
            "open {team}": "{nat} المفتوحة {label}",
        },
        team=team,
        label=label,
        nat=NAT_PLACEHOLDER,
    )

    extend_with_templates(
        templates,
        {
            "{team} national team": "منتخب {nat} {label}",
            "men's {team} national team": "منتخب {nat} {label} للرجال",
            "men's u23 national {team} team": "منتخب {nat} {label} تحت 23 سنة للرجال",
        },
        team=team,
        label=label,
        nat=NAT_PLACEHOLDER,
    )

    extend_with_templates(
        templates,
        {
            "women's {team}": "{label} {nat} نسائية",
            "{team} chairmen and investors": "رؤساء ومسيرو {label} {nat}",
            "defunct {team} cup competitions": "منافسات كؤوس {label} {nat} سابقة",
            "{team} cup competitions": "منافسات كؤوس {label} {nat}",
            "domestic {team} cup": "كؤوس {label} {nat} محلية",
            "current {team} seasons": "مواسم {label} {nat} حالية",
            "domestic {team}": "{label} {nat} محلية",
            "indoor {team}": "{label} {nat} داخل الصالات",
            "outdoor {team}": "{label} {nat} في الهواء الطلق",
        },
        team=team,
        label=label,
        nat=NAT_PLACEHOLDER,
    )

    for key, translation in TYPE_LABELS.items():
        extend_with_templates(
            templates,
            {
                f"{{team}} {key}": f"{translation} {{label}} {{nat}}",
                f"professional {{team}} {key}": f"{translation} {{label}} {{nat}} للمحترفين",
                f"defunct {{team}} {key}": f"{translation} {{label}} {{nat}} سابقة",
                f"domestic {{team}} {key}": f"{translation} {{label}} {{nat}} محلية",
                f"domestic women's {{team}} {key}": f"{translation} {{label}} {{nat}} محلية للسيدات",
                f"indoor {{team}} {key}": f"{translation} {{label}} {{nat}} داخل الصالات",
                f"outdoor {{team}} {key}": f"{translation} {{label}} {{nat}} في الهواء الطلق",
                f"defunct indoor {{team}} {key}": f"{translation} {{label}} {{nat}} داخل الصالات سابقة",
                f"defunct outdoor {{team}} {key}": f"{translation} {{label}} {{nat}} في الهواء الطلق سابقة",
            },
            team=team,
            label=label,
            nat=NAT_PLACEHOLDER,
        )

    return templates


def _build_templates_for_all_teams(teams: Mapping[str, str]) -> dict[str, str]:
    """Construct the complete mapping for all national teams."""

    result: dict[str, str] = {}
    for team, label in teams.items():
        result.update(_build_championship_templates(team, label))
    return result


def _build_placeholder_templates() -> dict[str, str]:
    """Create placeholder templates used for pattern matching and testing."""

    # "oioioi" mirrors the placeholder used by the legacy script.  Keeping the
    # same token ensures that downstream consumers continue to behave
    # correctly.
    placeholder_templates = _build_championship_templates("oioioi", "oioioi")
    return placeholder_templates


def _initialise_templates() -> tuple[dict[str, str], dict[str, str]]:
    """Generate both concrete and placeholder mappings."""

    sport_formats = _build_templates_for_all_teams(SPORTS_KEYS_FOR_TEAM)
    sport_formats["sports templates"] = "قوالب رياضة {nat}"

    placeholder = _build_placeholder_templates()

    log_length_stats(
        "sports/nat_p17.py",
        {
            "sport_formts_for_p17": len(sport_formats),
            "nat_p17_oioi": len(placeholder),
        },
        max_entries=1,
    )

    return sport_formats, placeholder


SPORT_FORMATS_FOR_P17, NAT_P17_OIOI = _initialise_templates()

# Backwards compatibility aliases for legacy imports.
sport_formts_for_p17 = SPORT_FORMATS_FOR_P17
nat_p17_oioi = NAT_P17_OIOI

__all__ = [
    "NAT_P17_OIOI",
    "SPORT_FORMATS_FOR_P17",
    "sport_formts_for_p17",
    "nat_p17_oioi",
]

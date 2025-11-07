"""Comprehensive sport template dictionaries used throughout the project."""

from __future__ import annotations

from collections.abc import Mapping
from typing import Final

from ..jobs.jobs_players_list import Football_Keys_players
from ..sports_formats_teams.team_job import sf_en_ar_is_p17
from .Sport_key import (
    SPORTS_KEYS_FOR_JOBS,
    SPORTS_KEYS_FOR_LABEL,
    SPORTS_KEYS_FOR_OLYMPIC,
    SPORTS_KEYS_FOR_TEAM,
)
from ._helpers import YEARS, extend_with_year_templates, log_length_stats
from .sports_lists import AFTER_KEYS, NEW_TATO_NAT, PPP_KEYS

COUNTRY_PLACEHOLDER: Final[str] = "{}"
NAT_PLACEHOLDER: Final[str] = "{nat}"


def _build_gender_variations(base: Mapping[str, str]) -> dict[str, str]:
    """Expand ``base`` with gender and age qualifiers defined in ``PPP_KEYS``."""

    variations = {key: value for key, value in base.items()}
    for sport, label in base.items():
        for qualifier, qualifier_label in PPP_KEYS.items():
            variations[f"{qualifier} {sport}"] = f"{label} {qualifier_label}"
    return variations


def _build_sport_formts_en_ar_is_p17() -> dict[str, str]:
    """Construct mappings where the English key holds the country name."""

    templates = {**sf_en_ar_is_p17}

    # Generic under-age templates.
    extend_with_year_templates(
        templates,
        {
            "under-{year} international managers": "مدربو تحت {year} سنة دوليون من {}",
            "under-{year} international players": "لاعبو تحت {year} سنة دوليون من {}",
            "under-{year} international playerss": "لاعبو تحت {year} سنة دوليون من {}",
        },
    )

    men_variations: dict[str, str] = {
        "": "",
        "men's a' ": " للرجال للمحليين",
        "men's b ": " الرديف للرجال",
        "men's ": " للرجال",
        "women's ": " للسيدات",
        "men's youth ": " للشباب",
        "women's youth ": " للشابات",
        "amateur ": " للهواة",
        "youth ": " للشباب",
    }

    for prefix, suffix in men_variations.items():
        start = "لاعبو منتخب"
        if "women's" in prefix:
            start = "لاعبات منتخب"
        base_label = f"{start} {{}} لكرة القدم {suffix}".strip()
        templates[f"{prefix}international footballers"] = base_label
        templates[f"{prefix}international soccer players"] = base_label
        templates[f"{prefix}international soccer playerss"] = base_label

        year_label = f"{start} {{}} تحت {{year}} سنة لكرة القدم {suffix}".strip()
        extend_with_year_templates(
            templates,
            {
                f"{prefix}under-{{year}} international footballers": year_label,
                f"{prefix}under-{{year}} international soccer players": year_label,
                f"{prefix}under-{{year}} international soccer playerss": year_label,
            },
        )

    templates["international rules football team"] = "منتخب {} لكرة القدم الدولية"
    templates["cup"] = "كأس {}"
    templates["presidents"] = "رؤساء {}"
    templates["territorial officials"] = "مسؤولو أقاليم {}"
    templates["territorial judges"] = "قضاة أقاليم {}"
    templates["war"] = "حرب {}"
    templates["rally championship"] = "بطولة {nat} للراليات"
    templates["war and conflict"] = "حروب ونزاعات {nat}"
    templates["governorate"] = "حكومة {nat}"
    templates["sports templates"] = "قوالب {} الرياضية"
    templates["national team"] = "منتخبات {} الوطنية"
    templates["national teams"] = "منتخبات {} الوطنية"
    templates["national football team managers"] = "مدربو منتخب {} لكرة القدم"
    templates["international rally"] = "رالي {} الدولي"

    return templates


def _build_sport_formts_en_p17_ar_nat() -> dict[str, str]:
    """Build mappings where the English key and Arabic label mix nationality."""

    result: dict[str, str] = {}
    for team, label in SPORTS_KEYS_FOR_TEAM.items():
        result[f"{team} federation"] = f"الاتحاد {NAT_PLACEHOLDER} {label}"
    return result


def _build_sport_formts_male_female_nat() -> tuple[dict[str, str], dict[str, str]]:
    """Generate dictionaries used for gender specific national competitions."""

    male: dict[str, str] = {}
    female: dict[str, str] = {}

    for label_key, label in SPORTS_KEYS_FOR_LABEL.items():
        lower_key = label_key.lower()
        male[f"{lower_key} super league"] = f"دوري السوبر {label} {COUNTRY_PLACEHOLDER}"
        male[f"professional {lower_key} league"] = f"دوري {label} {COUNTRY_PLACEHOLDER} للمحترفين"
        female[f"outdoor {lower_key}"] = f"{label} {COUNTRY_PLACEHOLDER} في الهواء الطلق"
        female[f"indoor {lower_key}"] = f"{label} {COUNTRY_PLACEHOLDER} داخل الصالات"

    for team, label in SPORTS_KEYS_FOR_TEAM.items():
        lower_team = team.lower()
        male[f"{lower_team} federation"] = f"الاتحاد {COUNTRY_PLACEHOLDER} {label}"
        male[f"{lower_team} league"] = f"الدوري {COUNTRY_PLACEHOLDER} {label}"
        male[f"women's {lower_team} league"] = f"الدوري {COUNTRY_PLACEHOLDER} {label} للسيدات"
        male[f"{lower_team} league administrators"] = f"مدراء الدوري {COUNTRY_PLACEHOLDER} {label}"
        male[f"{lower_team} league players"] = f"لاعبو الدوري {COUNTRY_PLACEHOLDER} {label}"
        male[f"{lower_team} league playerss"] = f"لاعبو الدوري {COUNTRY_PLACEHOLDER} {label}"
        male[f"indoor {lower_team} league"] = f"الدوري {COUNTRY_PLACEHOLDER} {label} داخل الصالات"
        male[f"outdoor {lower_team} league"] = f"الدوري {COUNTRY_PLACEHOLDER} {label} في الهواء الطلق"
        male[f"major indoor {lower_team} league"] = f"الدوري الرئيسي {COUNTRY_PLACEHOLDER} {label} داخل الصالات"

    return male, female


def _build_sport_formts_new_kkk() -> dict[str, str]:
    """Build templates mixing nationality placeholders with explicit teams."""

    result: dict[str, str] = {}
    for team, label in SPORTS_KEYS_FOR_TEAM.items():
        result[f"men's {team} cup"] = f"كأس {{}} {label} للرجال"
        result[f"women's {team} cup"] = f"كأس {{}} {label} للسيدات"
        result[f"{team} cup"] = f"كأس {{}} {label}"
        result[f"national junior men's {team} team"] = f"منتخب {{}} {label} للناشئين"
        result[f"national junior {team} team"] = f"منتخب {{}} {label} للناشئين"
        result[f"national {team} team"] = f"منتخب {{}} {label}"
        result[f"national women's {team} team"] = f"منتخب {{}} {label} للسيدات"
        result[f"national men's {team} team"] = f"منتخب {{}} {label} للرجال"
    return result


def _build_teams_new(new_with_women: Mapping[str, str]) -> dict[str, str]:
    """Create the large ``Teams_new`` dictionary used across bots."""

    teams: dict[str, str] = {
        "current seasons": "مواسم حالية",
        "international races": "سباقات دولية",
        "national championships": "بطولات وطنية",
        "national champions": "أبطال بطولات وطنية",
        "world competitions": "منافسات عالمية",
        "military competitions": "منافسات عسكرية",
        "men's teams": "فرق رجالية",
        "world championships competitors": "منافسون في بطولات العالم",
        "world championships medalists": "فائزون بميداليات بطولات العالم",
        "women's teams": "فرق نسائية",
        "world championships": "بطولة العالم",
        "international women's competitions": "منافسات نسائية دولية",
        "international men's competitions": "منافسات رجالية دولية",
        "international competitions": "منافسات دولية",
        "national team results": "نتائج منتخبات وطنية",
        "national teams": "منتخبات وطنية",
        "national youth teams": "منتخبات وطنية شبابية",
        "national men's teams": "منتخبات وطنية رجالية",
        "national women's teams": "منتخبات وطنية نسائية",
        "national youth sports teams of": "منتخبات رياضية وطنية شبابية في",
        "national sports teams of": "منتخبات رياضية وطنية في",
        "national sports teams": "منتخبات رياضية وطنية",
        "national men's sports teams": "منتخبات رياضية وطنية رجالية",
        "national men's sports teams of": "منتخبات رياضية وطنية رجالية في",
        "national women's sports teams": "منتخبات رياضية وطنية نسائية",
        "national women's sports teams of": "منتخبات رياضية وطنية نسائية في",
        "men's footballers": "لاعبو كرة قدم رجالية",
        "teams": "فرق",
        "sports teams": "فرق رياضية",
        "football clubs": "أندية كرة قدم",
        "clubs": "أندية",
    }

    jobs_with_additional = dict(SPORTS_KEYS_FOR_JOBS)
    jobs_with_additional["sports"] = "رياضية"

    for sport, label in jobs_with_additional.items():
        teams[f"{sport} managers"] = f"مدربو {label}"
        teams[f"{sport} coaches"] = f"مدربو {label}"
        teams[f"{sport} people"] = f"أعلام {label}"
        teams[f"{sport} playerss"] = f"لاعبو {label}"
        teams[f"{sport} players"] = f"لاعبو {label}"
        teams[f"{sport} referees"] = f"حكام {label}"

    extend_with_year_templates(
        teams,
        {"under-{year} sport": "رياضة تحت {year} سنة"},
        years=YEARS,
    )

    men_variations = {
        "": "",
        "men's a' ": " للرجال للمحليين",
        "men's b ": " الرديف للرجال",
        "men's ": " للرجال",
        "women's ": " للسيدات",
        "men's youth ": " للشباب",
        "women's youth ": " للشابات",
        "amateur ": " للهواة",
        "youth ": " للشباب",
    }

    for sport, label in SPORTS_KEYS_FOR_LABEL.items():
        teams[f"youth {sport}"] = f"{label} للشباب"
        teams[f"{sport} mass media"] = f"إعلام {label}"
        teams[f"{sport} non-playing staff"] = f"طاقم {label} غير اللاعبين"
        for prefix, suffix in men_variations.items():
            key = f"{prefix.strip()} {sport}".strip()
            teams[key] = f"{label}{suffix}".strip()

        olympic_label = f"{label} أولمبية"
        if sport in SPORTS_KEYS_FOR_OLYMPIC:
            olympic_label = SPORTS_KEYS_FOR_OLYMPIC[sport]

        teams[f"{sport} olympic champions"] = f"أبطال {olympic_label}"
        teams[f"{sport} olympics"] = olympic_label
        teams[f"{sport} olympic"] = olympic_label
        teams[f"olympic {sport}"] = olympic_label
        teams[f"olympics mens {sport}"] = olympic_label
        teams[f"international {sport}"] = olympic_label.replace("أولمبي", "دولي")
        teams[f"olympics men's {sport}"] = f"{olympic_label} للرجال"
        teams[f"olympics women's {sport}"] = f"{olympic_label} للسيدات"

    for sport, base_label in new_with_women.items():
        for suffix, suffix_label in AFTER_KEYS.items():
            teams[f"{sport} {suffix}"] = f"{suffix_label} {base_label}"

        for suffix, translations in Football_Keys_players.items():
            key = f"{sport} {suffix}"
            label = translations.get("mens", "")
            if "women's" in sport:
                label = translations.get("womens", label)
            teams[key] = f"{label} {base_label}".strip()

    return teams


def _initialise_templates() -> tuple[
    dict[str, str],
    dict[str, str],
    dict[str, str],
    dict[str, str],
    dict[str, str],
    dict[str, str],
    dict[str, str],
]:
    """Build every dictionary exported by this module."""

    new_with_women = _build_gender_variations(SPORTS_KEYS_FOR_JOBS)

    sport_formts_en_ar_is_p17 = _build_sport_formts_en_ar_is_p17()
    sport_formts_en_p17_ar_nat = _build_sport_formts_en_p17_ar_nat()
    sport_formts_male_nat, sport_formts_female_nat = _build_sport_formts_male_female_nat()
    sport_formts_new_kkk = _build_sport_formts_new_kkk()
    sport_formts_enar_p17_team = dict(NEW_TATO_NAT)

    teams_new = _build_teams_new(new_with_women)

    log_length_stats(
        "sports/skeys.py",
        {
            "sport_formts_en_ar_is_p17": len(sport_formts_en_ar_is_p17),
            "sport_formts_enar_p17_team": len(sport_formts_enar_p17_team),
            "teams_new": len(teams_new),
            "sport_formts_female_nat": len(sport_formts_female_nat),
            "sport_formts_male_nat": len(sport_formts_male_nat),
            "sport_formts_new_kkk": len(sport_formts_new_kkk),
            "sport_formts_en_p17_ar_nat": len(sport_formts_en_p17_ar_nat),
            "new_with_women": len(new_with_women),
        },
    )

    return (
        teams_new,
        sport_formts_en_ar_is_p17,
        sport_formts_en_p17_ar_nat,
        sport_formts_enar_p17_team,
        sport_formts_new_kkk,
        sport_formts_male_nat,
        sport_formts_female_nat,
    )


(
    TEAMS_NEW,
    SPORT_FORMTS_EN_AR_IS_P17,
    SPORT_FORMTS_EN_P17_AR_NAT,
    SPORT_FORMTS_ENAR_P17_TEAM,
    SPORT_FORMTS_NEW_KKK,
    SPORT_FORMTS_MALE_NAT,
    SPORT_FORMTS_FEMALE_NAT,
) = _initialise_templates()

# Backwards compatibility aliases for existing imports throughout the codebase.
Teams_new = TEAMS_NEW
sport_formts_en_ar_is_p17 = SPORT_FORMTS_EN_AR_IS_P17
sport_formts_en_p17_ar_nat = SPORT_FORMTS_EN_P17_AR_NAT
sport_formts_enar_p17_team = SPORT_FORMTS_ENAR_P17_TEAM
sport_formts_new_kkk = SPORT_FORMTS_NEW_KKK
sport_formts_male_nat = SPORT_FORMTS_MALE_NAT
sport_formts_female_nat = SPORT_FORMTS_FEMALE_NAT

__all__ = [
    "SPORT_FORMTS_EN_AR_IS_P17",
    "SPORT_FORMTS_EN_P17_AR_NAT",
    "SPORT_FORMTS_ENAR_P17_TEAM",
    "SPORT_FORMTS_FEMALE_NAT",
    "SPORT_FORMTS_MALE_NAT",
    "SPORT_FORMTS_NEW_KKK",
    "TEAMS_NEW",
    "sport_formts_en_ar_is_p17",
    "sport_formts_en_p17_ar_nat",
    "sport_formts_enar_p17_team",
    "sport_formts_female_nat",
    "sport_formts_male_nat",
    "sport_formts_new_kkk",
    "Teams_new",
]

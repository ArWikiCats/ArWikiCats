"""Utility tables for translating multi-season sporting competitions."""

from __future__ import annotations

import logging
from collections.abc import Mapping

from ._shared import log_mapping_stats

LOGGER = logging.getLogger(__name__)


def _build_base_games() -> dict[str, str]:
    """Return base competition labels keyed by their English names."""

    return {
        "african games": "الألعاب الإفريقية",
        "all-africa games": "ألعاب عموم إفريقيا",
        "asian games": "الألعاب الآسيية",
        "central american games": "ألعاب أمريكا الوسطى",
        "commonwealth games": "دورة ألعاب الكومنولث",
        "deaflympic games": "ألعاب ديفلمبياد",
        "european youth olympic winter": "الألعاب الأولمبية الشبابية الأوروبية الشتوية",
        "european youth olympic": "الألعاب الأولمبية الشبابية الأوروبية",
        "jeux de la francophonie": "الألعاب الفرانكوفونية",
        "olympic games": "الألعاب الأولمبية",
        "olympics": "الألعاب الأولمبية",
        "paralympics games": "الألعاب البارالمبية",
        "south american games": "ألعاب أمريكا الجنوبية",
        "universiade": "الألعاب الجامعية",
        "world games": "دورة الألعاب العالمية",
        "youth olympic games": "الألعاب الأولمبية الشبابية",
        "youth olympics": "الألعاب الأولمبية الشبابية",
    }


def _build_multi_season_games() -> dict[str, str]:
    """Return the manual overrides for summer and winter competitions."""

    return {
        "african games": "الألعاب الإفريقية",
        "asian beach games": "دورة الألعاب الآسيوية الشاطئية",
        "asian games": "الألعاب الآسيوية",
        "asian para games": "دورة الألعاب الآسيوية البارالمبية",
        "asian summer games": "الألعاب الآسيوية الصيفية",
        "asian winter games": "الألعاب الآسيوية الشتوية",
        "bolivarian games": "الألعاب البوليفارية",
        "central american and caribbean games": "ألعاب أمريكا الوسطى والكاريبي",
        "central american games": "ألعاب أمريكا الوسطى",
        "commonwealth games": "ألعاب الكومنولث",
        "commonwealth youth games": "ألعاب الكومنولث الشبابية",
        "european games": "الألعاب الأوروبية",
        "european youth olympic winter": "الألعاب الأولمبية الشبابية الأوروبية الشتوية",
        "european youth olympic": "الألعاب الأولمبية الشبابية الأوروبية",
        "fis nordic world ski championships": "بطولة العالم للتزلج النوردي على الثلج",
        "friendship games": "ألعاب الصداقة",
        "goodwill games": "ألعاب النوايا الحسنة",
        "islamic solidarity games": "ألعاب التضامن الإسلامي",
        "maccabiah games": "الألعاب المكابيه",
        "mediterranean games": "الألعاب المتوسطية",
        "micronesian games": "الألعاب الميكرونيزية",
        "military world games": "دورة الألعاب العسكرية",
        "asian indoor games": "دورة الألعاب الآسيوية داخل الصالات",
        "pan american games": "دورة الألعاب الأمريكية",
        "pan arab games": "دورة الألعاب العربية",
        "pan asian games": "دورة الألعاب الآسيوية",
        "paralympic": "الألعاب البارالمبية",
        "paralympics": "الألعاب البارالمبية",
        "parapan american games": "ألعاب بارابان الأمريكية",
        "sea games": "ألعاب البحر",
        "south american games": "ألعاب أمريكا الجنوبية",
        "south asian beach games": "دورة ألعاب جنوب أسيا الشاطئية",
        "south asian games": "ألعاب جنوب أسيا",
        "south asian winter games": "ألعاب جنوب آسيا الشتوية",
        "southeast asian games": "ألعاب جنوب شرق آسيا",
        "summer olympics": "الألعاب الأولمبية الصيفية",
        "summer universiade": "الألعاب الجامعية الصيفية",
        "summer world university games": "ألعاب الجامعات العالمية الصيفية",
        "the universiade": "الألعاب الجامعية",
        "universiade": "الألعاب الجامعية",
        "winter olympics": "الألعاب الأولمبية الشتوية",
        "winter universiade": "الألعاب الجامعية الشتوية",
        "winter world university games": "ألعاب الجامعات العالمية الشتوية",
        "world championships": "بطولات العالم",
        "youth olympic": "الألعاب الأولمبية الشبابية",
        "youth olympics games": "الألعاب الأولمبية الشبابية",
        "youth olympics": "الألعاب الأولمبية الشبابية",
        "deaflympic games": "ألعاب ديفلمبياد",
    }


def _build_game_categories() -> dict[str, str]:
    """Return mappings for the auxiliary competition categories."""

    return {
        "competitions": "منافسات",
        "events": "أحداث",
        "festival": "مهرجانات",
        "bids": "عروض",
        "templates": "قوالب",
    }


BASE_GAME_LABELS = _build_base_games()
SUMMER_WINTER_GAMES = _build_multi_season_games()
GAME_CATEGORY_LABELS = _build_game_categories()


def _build_seasonal_labels() -> dict[str, str]:
    """Return the label table that includes seasonal variants."""

    seasonal_labels = dict(SUMMER_WINTER_GAMES)

    for base_key, base_label in BASE_GAME_LABELS.items():
        seasonal_labels[base_key] = base_label
        seasonal_labels[f"winter {base_key}"] = f"{base_label} الشتوية"
        seasonal_labels[f"summer {base_key}"] = f"{base_label} الصيفية"
        seasonal_labels[f"west {base_key}"] = f"{base_label} الغربية"

    return seasonal_labels


SEASONAL_GAME_LABELS = _build_seasonal_labels()


def _build_tab_labels() -> dict[str, str]:
    """Return tabs that combine games with category labels."""

    tab_labels: dict[str, str] = {}

    for game_key, game_label in SEASONAL_GAME_LABELS.items():
        tab_labels[game_key] = game_label

        # Categories are appended to each game label so that consumers do not
        # need to duplicate formatting logic.
        for category_key, category_label in GAME_CATEGORY_LABELS.items():
            category_entry_key = f"{game_key} {category_key}"
            tab_labels[category_entry_key] = f"{category_label} {game_label}"

    return tab_labels


SUMMER_WINTER_TABS = _build_tab_labels()

log_mapping_stats(
    "games_labs",
    seasonal_game_labels=SEASONAL_GAME_LABELS,
    tab_labels=SUMMER_WINTER_TABS,
)


def get_seasonal_game_labels() -> dict[str, str]:
    """Return a copy of the seasonal game labels mapping."""

    return dict(SEASONAL_GAME_LABELS)


def get_game_category_tabs() -> dict[str, str]:
    """Return a copy of the tab labels mapping."""

    return dict(SUMMER_WINTER_TABS)


# --- backwards compatibility -------------------------------------------------
summer_winter_games = SUMMER_WINTER_GAMES
summer_winter_tabs = SUMMER_WINTER_TABS
pop_Summer = SEASONAL_GAME_LABELS
Params = BASE_GAME_LABELS
Game_s = GAME_CATEGORY_LABELS

__all__ = [
    "BASE_GAME_LABELS",
    "GAME_CATEGORY_LABELS",
    "SUMMER_WINTER_GAMES",
    "SUMMER_WINTER_TABS",
    "SEASONAL_GAME_LABELS",
    "get_game_category_tabs",
    "get_seasonal_game_labels",
    # Backwards-compatible exports
    "summer_winter_games",
    "summer_winter_tabs",
    "pop_Summer",
    "Params",
    "Game_s",
]

#!/usr/bin/python3
"""
Film and TV Series Translation Mappings.

Builds translation mappings for film and television categories from English to Arabic,
handling gender-specific translations and nationality-based categories.
"""

from typing import Dict, Tuple
from ...helps import len_print
from ..utils.json_dir import open_json_file


# =============================================================================
# Constants
# =============================================================================

NAT_PLACEHOLDER = "{}"

# Keys that support debuts/endings variants
DEBUTS_ENDINGS_KEYS = ["television series", "television miniseries", "television films"]

# Fixed television/web series templates
SERIES_DEBUTS_ENDINGS = {
    "television-series debuts": "مسلسلات تلفزيونية {} بدأ عرضها في",
    "television-series endings": "مسلسلات تلفزيونية {} انتهت في",
    "web series-debuts": "مسلسلات ويب {} بدأ عرضها في",
    "web series debuts": "مسلسلات ويب {} بدأ عرضها في",
    "television series-debuts": "مسلسلات تلفزيونية {} بدأ عرضها في",
    "television series debuts": "مسلسلات تلفزيونية {} بدأ عرضها في",
    "television series endings": "مسلسلات تلفزيونية {} انتهت في",
}

# General television/media category base translations
TELEVISION_BASE_KEYS = {
    "video games": "ألعاب فيديو",
    "soap opera": "مسلسلات طويلة",
    "television characters": "شخصيات تلفزيونية",
    "television programs": "برامج تلفزيونية",
    "television programmes": "برامج تلفزيونية",
    "web series": "مسلسلات ويب",
    "television series": "مسلسلات تلفزيونية",
    "film series": "سلاسل أفلام",
    "television episodes": "حلقات تلفزيونية",
    "television news": "أخبار تلفزيونية",
    "comics": "قصص مصورة",
    "television films": "أفلام تلفزيونية",
    "television miniseries": "مسلسلات قصيرة",
}

# Extended television keys dictionary
TELEVISION_KEYS = {
    "albums": "ألبومات",
    "animation": "رسوم متحركة",
    "anime and manga": "أنمي ومانغا",
    "bodies": "هيئات",
    "championships": "بطولات",
    "clubs": "أندية",
    "comic strips": "شرائط مصورة",
    "comics": "قصص مصورة",
    "competition": "منافسات",
    "competitions": "منافسات",
    "culture": "ثقافة",
    "equipment": "معدات",
    "executives": "مدراء",
    "films": "أفلام",
    "games": "ألعاب",
    "governing bodies": "هيئات تنظيم",
    "graphic novels": "روايات مصورة",
    "logos": "شعارات",
    "magazines": "مجلات",
    "manga": "مانغا",
    "media": "إعلام",
    "music": "موسيقى",
    "non-profit organizations": "منظمات غير ربحية",
    "non-profit publishers": "ناشرون غير ربحيون",
    "novellas": "روايات قصيرة",
    "novels": "روايات",
    "occupations": "مهن",
    "organizations": "منظمات",
    "people": "أعلام",
    "short stories": "قصص قصيرة",
    "soap opera": "مسلسلات طويلة",
    "soundtracks": "موسيقى تصويرية",
    "tactics and skills": "مهارات",
    "teams": "فرق",
    "television commercials": "إعلانات تجارية تلفزيونية",
    "television episodes": "حلقات تلفزيونية",
    "television films": "أفلام تلفزيونية",
    "television miniseries": "مسلسلات قصيرة",
    "television news": "أخبار تلفزيونية",
    "television programmes": "برامج تلفزيونية",
    "television programming": "برمجة تلفزيونية",
    "television programs": "برامج تلفزيونية",
    "television schedules": "جداول تلفزيونية",
    "television series": "مسلسلات تلفزيونية",
    "film series": "سلاسل أفلام",
    "television shows": "عروض تلفزيونية",
    "terminology": "مصطلحات",
    "variants": "أشكال",
    "video games": "ألعاب فيديو",
    "web series": "مسلسلات ويب",
    "webcomic": "ويب كومكس",
    "webcomics": "ويب كومكس",
    "works": "أعمال"
}

# LGBTQ-related films format
Films_key_CAO_new_format = {
    "lgbtq-related films": "أفلام {} متعلقة بإل جي بي تي كيو",
}


# =============================================================================
# Helper Functions
# =============================================================================

def _build_gender_key_maps(
    films_keys_male_female: Dict[str, Dict[str, str]],
    films_key_o_multi: Dict[str, Dict[str, str]],
) -> Tuple[
    Dict[str, Dict[str, str]],  # films_key_both
    Dict[str, str],              # films_key_333
    Dict[str, str],              # films_key_man
    Dict[str, str],              # film_keys_for_male
    Dict[str, str],              # film_keys_for_female
]:
    """
    Build gender-aware film key mappings from JSON sources.

    Returns:
        - films_key_both: Lowercase key → {male, female}
        - films_key_333: Original key → female label
        - films_key_man: Key → male label (with animated variants)
        - film_keys_for_male: Key → male label
        - film_keys_for_female: Key → female label
    """
    films_key_both = {}
    films_key_333 = {}
    films_key_man = {}
    film_keys_for_male = {}
    film_keys_for_female = {}

    # Process films_key_o_multi
    for en_key, labels in films_key_o_multi.items():
        key_lower = en_key.lower()
        films_key_both[key_lower] = labels
        female_label = labels.get("female", "").strip()
        if female_label:
            films_key_333[en_key] = female_label

    # Handle "animated" → "animation" aliasing
    if "animated" in films_key_both:
        films_key_both["animation"] = films_key_both["animated"]

    # Build gender-specific maps
    for en_key, labels in films_key_both.items():
        male_label = labels.get("male", "").strip()
        female_label = labels.get("female", "").strip()

        if male_label:
            films_key_man[en_key] = male_label
            # Add animated variant for male
            if "animated" not in en_key:
                films_key_man[f"animated {en_key}"] = f"{male_label} رسوم متحركة"
            film_keys_for_male[en_key] = male_label

        if female_label:
            film_keys_for_female[en_key] = female_label

    # Process films_keys_male_female (with animation aliasing)
    male_female_copy = dict(films_keys_male_female)
    if "animated" in male_female_copy:
        male_female_copy["animation"] = male_female_copy["animated"]

    for en_key, labels in male_female_copy.items():
        female_label = labels.get("female", "").strip()
        if female_label:
            films_key_333[en_key] = female_label
            film_keys_for_female[en_key] = female_label

    return (
        films_key_both,
        films_key_333,
        films_key_man,
        film_keys_for_male,
        film_keys_for_female,
    )


def _build_series_and_nat_keys(
    films_key_for_nat: Dict[str, str],
    female_keys: Dict[str, str],
) -> Tuple[Dict[str, str], Dict[str, str]]:
    """
    Build nationality-aware and series-based translation mappings.

    Returns:
        - films_key_for_nat: With nationality placeholder {}
        - films_mslslat_tab: Without nationality placeholder
    """
    films_mslslat_tab = {}

    # Add fixed templates
    films_key_for_nat.update(SERIES_DEBUTS_ENDINGS)

    # Add remakes mapping
    films_key_for_nat["remakes of {} films"] = f"أفلام {NAT_PLACEHOLDER} معاد إنتاجها"

    # Build base series keys
    for tt, tt_lab in TELEVISION_BASE_KEYS.items():
        films_key_for_nat[tt] = f"{tt_lab} {NAT_PLACEHOLDER}"
        films_mslslat_tab[tt] = tt_lab

        # Debuts, endings, revived variants
        for suffix, arabic_suffix in [
            ("debuts", "بدأ عرضها في"),
            ("endings", "انتهت في"),
            ("revived after cancellation", "أعيدت بعد إلغائها"),
        ]:
            key_with_suffix = f"{tt} {suffix}"
            films_key_for_nat[key_with_suffix] = f"{tt_lab} {NAT_PLACEHOLDER} {arabic_suffix}"
            films_mslslat_tab[key_with_suffix] = f"{tt_lab} {arabic_suffix}"

        # Dashed variants for specific keys
        if tt.lower() in DEBUTS_ENDINGS_KEYS:
            for suffix, arabic_suffix in [("debuts", "بدأ عرضها في"), ("endings", "انتهت في")]:
                dashed_key = f"{tt}-{suffix}"
                films_key_for_nat[dashed_key] = f"{tt_lab} {NAT_PLACEHOLDER} {arabic_suffix}"
                films_mslslat_tab[dashed_key] = f"{tt_lab} {arabic_suffix}"

    # Build combinations of female film keys with series keys
    for ke, ke_lab in female_keys.items():
        for tt, tt_lab in TELEVISION_BASE_KEYS.items():
            key_base = f"{ke} {tt}"

            # Base combination
            films_key_for_nat[key_base] = f"{tt_lab} {ke_lab} {NAT_PLACEHOLDER}"
            films_mslslat_tab[key_base] = f"{tt_lab} {ke_lab}"

            # Debuts, endings, revived variants
            for suffix, arabic_suffix in [
                ("debuts", "بدأ عرضها في"),
                ("endings", "انتهت في"),
                ("revived after cancellation", "أعيدت بعد إلغائها"),
            ]:
                combo_key = f"{key_base} {suffix}"

                if suffix == "revived after cancellation":
                    films_key_for_nat[combo_key] = f"{tt_lab} {ke_lab} {NAT_PLACEHOLDER} {arabic_suffix}"
                    films_mslslat_tab[combo_key] = f"{tt_lab} {ke_lab} {arabic_suffix}"
                else:
                    films_key_for_nat[combo_key] = f"{tt_lab} {ke_lab} {NAT_PLACEHOLDER} {arabic_suffix}"
                    films_mslslat_tab[combo_key] = f"{tt_lab} {ke_lab} {arabic_suffix}"

            # Dashed variants
            if tt.lower() in DEBUTS_ENDINGS_KEYS:
                for suffix, arabic_suffix in [("debuts", "بدأ عرضها في"), ("endings", "انتهت في")]:
                    dashed_key = f"{key_base}-{suffix}"
                    films_key_for_nat[dashed_key] = f"{tt_lab} {ke_lab} {NAT_PLACEHOLDER} {arabic_suffix}"
                    films_mslslat_tab[dashed_key] = f"{tt_lab} {ke_lab} {arabic_suffix}"

    return films_key_for_nat, films_mslslat_tab


def _build_television_cao(
    female_keys: Dict[str, str],
) -> Tuple[Dict[str, str], int]:
    """
    Build CAO (Characters, Albums, Organizations, etc.) mappings.

    Returns:
        - films_key_cao: CAO translation mapping
        - count: Number of genre-TV combinations created
    """
    films_key_cao = {}
    count = 0

    # Base TV keys with common suffixes
    for ff, label in TELEVISION_KEYS.items():
        films_key_cao[ff] = label
        for suffix, arabic_suffix in [
            ("characters", "شخصيات"),
            ("title cards", "بطاقات عنوان"),
            ("video covers", "أغلفة فيديو"),
            ("posters", "ملصقات"),
            ("images", "صور"),
        ]:
            films_key_cao[f"{ff} {suffix}"] = f"{arabic_suffix} {label}"

    # Genre-based categories
    genre_categories = [
        ("anime and manga", "أنمي ومانغا"),
        ("compilation albums", "ألبومات تجميعية"),
        ("folk albums", "ألبومات فلكلورية"),
        ("classical albums", "ألبومات كلاسيكية"),
        ("comedy albums", "ألبومات كوميدية"),
        ("mixtape albums", "ألبومات ميكستايب"),
        ("soundtracks", "موسيقى تصويرية"),
        ("terminology", "مصطلحات"),
        ("television series", "مسلسلات تلفزيونية"),
        ("television episodes", "حلقات تلفزيونية"),
        ("television programs", "برامج تلفزيونية"),
        ("television programmes", "برامج تلفزيونية"),
        ("groups", "مجموعات"),
        ("novellas", "روايات قصيرة"),
        ("novels", "روايات"),
        ("films", "أفلام"),
    ]

    for ke, ke_lab in female_keys.items():
        # Special cases
        films_key_cao[f"children's {ke}"] = f"أطفال {ke_lab}"
        films_key_cao[f"{ke} film remakes"] = f"أفلام {ke_lab} معاد إنتاجها"

        # Standard categories
        for suffix, arabic_base in genre_categories:
            films_key_cao[f"{ke} {suffix}"] = f"{arabic_base} {ke_lab}"

        # Combinations with all TV keys
        for fao, base_label in TELEVISION_KEYS.items():
            count += 1
            films_key_cao[f"{ke} {fao}"] = f"{base_label} {ke_lab}"

    return films_key_cao, count


def _build_female_combo_keys(
    films_keys_male_female: Dict[str, Dict[str, str]],
) -> Dict[str, str]:
    """Build all pairwise combinations of female genre labels."""
    result = {}

    # Extract female labels
    base_female = {
        x: v["female"]
        for x, v in films_keys_male_female.items()
        if v.get("female", "").strip()
    }

    # Generate combinations
    for en, tab in films_keys_male_female.items():
        tab_female = tab.get("female", "").strip()
        if not tab_female:
            continue

        for en2, tab2_female in base_female.items():
            if en == en2:
                continue
            new_key = f"{en} {en2}".lower()
            if tab2_female:
                result[new_key] = f"{tab_female} {tab2_female}"

    return result


# =============================================================================
# Module Initialization
# =============================================================================

# Load JSON resources
Films_keys_male_female = open_json_file("media/Films_keys_male_female.json") or {}
Films_key_For_nat = open_json_file("media/Films_key_For_nat.json") or {}
_Films_key_O_multi = open_json_file("media/Films_key_O_multi.json") or {}

# Filter to only entries with both male and female
Films_key_O_multi = {
    x: v
    for x, v in _Films_key_O_multi.items()
    if v.get("male", "").strip() and v.get("female", "").strip()
}

# Build gender-aware mappings
(
    Films_key_both,
    Films_key_333,
    Films_key_man,
    film_keys_for_male,
    film_keys_for_female,
) = _build_gender_key_maps(Films_keys_male_female, Films_key_O_multi)

# Legacy alias
Films_key2 = film_keys_for_female

# Build series and nationality keys
Films_key_For_nat, films_mslslat_tab = _build_series_and_nat_keys(
    Films_key_For_nat,
    film_keys_for_female,
)

# Extend Films_key_333 with female labels from Films_key_O_multi
for cd, ff in Films_key_O_multi.items():
    female_label = ff.get("female", "").strip()
    if female_label:
        Films_key_333[cd] = female_label

# Build television CAO mappings
Films_key_CAO, ss_Films_key_CAO = _build_television_cao(film_keys_for_female)

# Build female combination keys
Films_keys_both_new_female = _build_female_combo_keys(Films_keys_male_female)

# Legacy aliases
film_key_women_2 = TELEVISION_BASE_KEYS
television_keys = TELEVISION_KEYS

# Summary output
len_print.data_len(
    "films_mslslat.py",
    {
        "television_keys": television_keys,
        "Films_key_For_nat": Films_key_For_nat,
        "films_mslslat_tab": films_mslslat_tab,
        "ss_Films_key_CAO": ss_Films_key_CAO,
        "Films_key_333": Films_key_333,
        "Films_key_CAO": Films_key_CAO,
        "Films_keys_both_new_female": Films_keys_both_new_female,
        "film_keys_for_female": film_keys_for_female,
        "film_keys_for_male": film_keys_for_male,
        "Films_key_man": Films_key_man,
        "film_key_women_2": film_key_women_2,
    },
)


# =============================================================================
# Public API
# =============================================================================

__all__ = [
    "television_keys",
    "films_mslslat_tab",
    "film_keys_for_female",
    "film_keys_for_male",
    "Films_key_333",
    "Films_key_CAO",
    "Films_key_CAO_new_format",
    "Films_key_For_nat",
    "Films_key_man",
    "Films_keys_both_new_female",
    "film_key_women_2",
]

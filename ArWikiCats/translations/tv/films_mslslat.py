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
    "miniseries": "مسلسلات قصيرة",
    "television miniseries": "مسلسلات قصيرة تلفزيونية",
}

# Extended television keys dictionary
TELEVISION_KEYS = {
    # "people": "أعلام",
    "albums": "ألبومات",
    "animation": "رسوم متحركة",
    "anime and manga": "أنمي ومانغا",
    "bodies": "هيئات",
    "championships": "بطولات",
    "clubs": "أندية",
    "clubs and teams": "أندية وفرق",
    "comic strips": "شرائط كومكس",
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
    "short stories": "قصص قصيرة",
    "soap opera": "مسلسلات طويلة",
    "soundtracks": "موسيقى تصويرية",
    "tactics and skills": "مهارات",
    "teams": "فرق",
    "television commercials": "إعلانات تجارية تلفزيونية",
    "television episodes": "حلقات تلفزيونية",
    "television films": "أفلام تلفزيونية",
    "miniseries": "مسلسلات قصيرة",
    "television miniseries": "مسلسلات قصيرة تلفزيونية",
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
    "works": "أعمال",
}

# =============================================================================
# Helper Functions
# =============================================================================


def _build_gender_key_maps(
    films_key_o_multi: Dict[str, Dict[str, str]]
) -> Tuple[Dict[str, Dict[str, str]], Dict[str, str],]:  # films_key_both  # films_key_man
    """
    Build gender-aware film key mappings from JSON sources.

    Returns:
        - films_key_both: Lowercase key → {male, female}
        - films_key_man: Key → male label (with animated variants)
    """
    films_key_both = {}
    films_key_man = {}

    # Process films_key_o_multi
    for en_key, labels in films_key_o_multi.items():
        key_lower = en_key.lower()
        films_key_both[key_lower] = labels

    # Handle "animated" → "animation" aliasing
    if "animated" in films_key_both:
        films_key_both["animation"] = films_key_both["animated"]

    # Build gender-specific maps
    for en_key, labels in films_key_both.items():
        male_label = labels.get("male", "").strip()

        if male_label:
            films_key_man[en_key] = male_label
            # Add animated variant for male
            if "animated" not in en_key:
                films_key_man[f"animated {en_key}"] = f"{male_label} رسوم متحركة"

    return (
        films_key_both,
        films_key_man,
    )


def _extend_females_labels(
    films_keys_male_female: Dict[str, Dict[str, str]],
) -> Dict[str, str]:
    """
    Extract female labels from the male/female dictionary with animation aliasing.

    Processes the input dictionary and returns a mapping of original keys to their
    female labels. Includes special handling to alias "animated" to "animation".

    Args:
        films_keys_male_female: Dictionary mapping English keys to gender label pairs

     Returns:
        Dictionary mapping original keys to female labels
    """
    data = {}

    # Process films_keys_male_female (with animation aliasing)
    male_female_copy = dict(films_keys_male_female)
    if "animated" in male_female_copy:
        male_female_copy["animation"] = male_female_copy["animated"]

    for en_key, labels in male_female_copy.items():
        female_label = labels.get("female", "").strip()
        if female_label:
            data[en_key] = female_label

    return data


def _build_series_and_nat_keys(
    female_keys: Dict[str, str],
) -> Tuple[Dict[str, str], Dict[str, str]]:
    """
    Build nationality-aware and series-based translation mappings.

    Returns:
        - films_key_for_nat: With nationality placeholder {}
        - films_mslslat_tab: Without nationality placeholder
    """
    _mslslat_tab = {}
    _key_for_nat = {}

    # Add fixed templates
    _key_for_nat.update(SERIES_DEBUTS_ENDINGS)

    # Add remakes mapping
    _key_for_nat["remakes of {} films"] = f"أفلام {NAT_PLACEHOLDER} معاد إنتاجها"

    # Build base series keys
    for tt, tt_lab in TELEVISION_BASE_KEYS.items():
        _key_for_nat[tt] = f"{tt_lab} {NAT_PLACEHOLDER}"
        _mslslat_tab[tt] = tt_lab

        # Debuts, endings, revived variants
        for suffix, arabic_suffix in [
            ("debuts", "بدأ عرضها في"),
            ("endings", "انتهت في"),
            ("revived after cancellation", "أعيدت بعد إلغائها"),
        ]:
            key_with_suffix = f"{tt} {suffix}"
            _key_for_nat[key_with_suffix] = f"{tt_lab} {NAT_PLACEHOLDER} {arabic_suffix}"
            _mslslat_tab[key_with_suffix] = f"{tt_lab} {arabic_suffix}"

        # Dashed variants for specific keys
        if tt.lower() in DEBUTS_ENDINGS_KEYS:
            for suffix, arabic_suffix in [("debuts", "بدأ عرضها في"), ("endings", "انتهت في")]:
                dashed_key = f"{tt}-{suffix}"
                _key_for_nat[dashed_key] = f"{tt_lab} {NAT_PLACEHOLDER} {arabic_suffix}"
                _mslslat_tab[dashed_key] = f"{tt_lab} {arabic_suffix}"

    # Build combinations of female film keys with series keys
    for ke, ke_lab in female_keys.items():
        for tt, tt_lab in TELEVISION_BASE_KEYS.items():
            key_base = f"{ke} {tt}"

            # Base combination
            _key_for_nat[key_base] = f"{tt_lab} {ke_lab} {NAT_PLACEHOLDER}"
            _mslslat_tab[key_base] = f"{tt_lab} {ke_lab}"

            # Debuts, endings, revived variants
            for suffix, arabic_suffix in [
                ("debuts", "بدأ عرضها في"),
                ("endings", "انتهت في"),
                ("revived after cancellation", "أعيدت بعد إلغائها"),
            ]:
                combo_key = f"{key_base} {suffix}"

                if suffix == "revived after cancellation":
                    _key_for_nat[combo_key] = f"{tt_lab} {ke_lab} {NAT_PLACEHOLDER} {arabic_suffix}"
                    _mslslat_tab[combo_key] = f"{tt_lab} {ke_lab} {arabic_suffix}"
                else:
                    _key_for_nat[combo_key] = f"{tt_lab} {ke_lab} {NAT_PLACEHOLDER} {arabic_suffix}"
                    _mslslat_tab[combo_key] = f"{tt_lab} {ke_lab} {arabic_suffix}"

            # Dashed variants
            if tt.lower() in DEBUTS_ENDINGS_KEYS:
                for suffix, arabic_suffix in [("debuts", "بدأ عرضها في"), ("endings", "انتهت في")]:
                    dashed_key = f"{key_base}-{suffix}"
                    _key_for_nat[dashed_key] = f"{tt_lab} {ke_lab} {NAT_PLACEHOLDER} {arabic_suffix}"
                    _mslslat_tab[dashed_key] = f"{tt_lab} {ke_lab} {arabic_suffix}"

    return _key_for_nat, _mslslat_tab


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
    filmskeys_male_female: Dict[str, Dict[str, str]],
) -> Dict[str, str]:
    """Build all pairwise combinations of female genre labels."""
    result = {}

    # Extract female labels
    base_female = {x: v["female"] for x, v in filmskeys_male_female.items() if v.get("female", "").strip()}

    # Generate combinations
    for en, tab in filmskeys_male_female.items():
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


def build_gender_specific_film_maps(
    Films_keys_male_female: Dict[str, Dict[str, str]],
    Films_key_O_multi: Dict[str, Dict[str, str]],
    films_key_both: Dict[str, Dict[str, str]],
) -> tuple[dict, dict]:
    """
    Build gender-aware film key mappings.

    Returns:
        - Films_key_333: key → {male, female}
        - film_keys_for_female: Key → female label
    """
    Films_key_333: Dict[str, str] = {}
    # Build gender-specific maps

    film_keys_for_female: Dict[str, str] = {
        x: v.get("female", "").strip() for x, v in films_key_both.items() if v.get("female", "").strip()
    }

    female_extended_labels = _extend_females_labels(Films_keys_male_female)
    Films_key_333.update(female_extended_labels)
    film_keys_for_female.update(female_extended_labels)

    # Extend Films_key_333 with female labels from Films_key_O_multi
    for cd, ff in Films_key_O_multi.items():
        female_label = ff.get("female", "").strip()
        if female_label:  # and cd not in Films_key_333:
            Films_key_333[cd] = female_label

    return Films_key_333, film_keys_for_female


# =============================================================================
# Module Initialization
# =============================================================================

# Load JSON resources
Films_key_For_nat = open_json_file("media/Films_key_For_nat.json") or {}
_Films_key_O_multi = open_json_file("media/Films_key_O_multi.json") or {}

Films_keys_male_female = open_json_file("media/Films_keys_male_female.json") or {}
Films_keys_male_female["sports"] = {"male": "رياضي", "female": "رياضية"}
# Films_keys_male_female["superhero"] = {"male": "خارق", "female": "أبطال خارقين"}

# Filter to only entries with both male and female
Films_key_O_multi = {
    x: v for x, v in _Films_key_O_multi.items() if v.get("male", "").strip() and v.get("female", "").strip()
}

# Build gender-aware mappings
(
    Films_key_both,
    Films_key_man,
) = _build_gender_key_maps(Films_key_O_multi)

film_keys_for_male: Dict[str, str] = {
    x: v.get("male", "").strip() for x, v in Films_key_both.items() if v.get("male", "").strip()
}

Films_key_333, film_keys_for_female = build_gender_specific_film_maps(
    Films_keys_male_female, Films_key_O_multi, Films_key_both
)


# Build series and nationality keys
# films_key_for_nat_extended_org, films_mslslat_tab_base_org = _build_series_and_nat_keys(film_keys_for_female)

films_mslslat_tab_base = open_json_file("films_mslslat_tab_found.json")

# Films_key_For_nat_extended = open_json_file("Films_key_For_nat_extended_found.json")
# NOTE: "Films_key_For_nat_extended_found.json" and "films_mslslat_tab_found.json" looks the same exept Films_key_For_nat_extended_found has placeholder {} in values

Films_key_For_nat_extended = {x: f"{v} {{}}" for x, v in films_mslslat_tab_base.items()}

films_mslslat_tab = dict(films_mslslat_tab_base)

films_mslslat_tab.update(
    {
        "science fiction film series-endings": "سلاسل أفلام خيال علمي انتهت في",
        "science fiction film series debuts": "سلاسل أفلام خيال علمي بدأ عرضها في",
        "television series revived after cancellation": "مسلسلات تلفزيونية أعيدت بعد إلغائها",
        "comics endings": "قصص مصورة انتهت في",
        "television series endings": "مسلسلات تلفزيونية انتهت في",
        "animated television series endings": "مسلسلات تلفزيونية رسوم متحركة انتهت في",
        "web series endings": "مسلسلات ويب انتهت في",
        "web series debuts": "مسلسلات ويب بدأ عرضها في",
        "anime television series debuts": "مسلسلات تلفزيونية أنمي بدأ عرضها في",
        "comics debuts": "قصص مصورة بدأ عرضها في",
        "animated television series debuts": "مسلسلات تلفزيونية رسوم متحركة بدأ عرضها في",
        "television series debuts": "مسلسلات تلفزيونية بدأ عرضها في",
        "supernatural television series": "مسلسلات تلفزيونية خارقة للطبيعة",
        "supernatural comics": "قصص مصورة خارقة للطبيعة",
        "adult animated supernatural television series": "مسلسلات تلفزيونية رسوم متحركة خارقة للطبيعة للكبار",
        "superhero television characters": "شخصيات تلفزيونية أبطال خارقين",
        "superhero television series": "مسلسلات تلفزيونية أبطال خارقين",
        "superhero film series": "سلاسل أفلام أبطال خارقين",
        "superhero television episodes": "حلقات تلفزيونية أبطال خارقين",
        "superhero video games": "ألعاب فيديو أبطال خارقين",
        "superhero web series": "مسلسلات ويب أبطال خارقين",
        "superhero comics": "قصص مصورة أبطال خارقين",
        "superhero television films": "أفلام تلفزيونية أبطال خارقين",
    }
)

films_mslslat_tab.update(
    {x.replace(" endings", "-endings"): y for x, y in films_mslslat_tab.items() if " endings" in x}
)

Films_key_For_nat.update(
    {
        "drama films": "أفلام درامية {}",
        "legal drama films": "أفلام قانونية درامية {}",
        # "yemeni musical drama films" : "تصنيف:أفلام موسيقية درامية يمنية",
        "musical drama films": "أفلام موسيقية درامية {}",
        "political drama films": "أفلام سياسية درامية {}",
        "romantic drama films": "أفلام رومانسية درامية {}",
        "sports drama films": "أفلام رياضية درامية {}",
        "comedy drama films": "أفلام كوميدية درامية {}",
        "war drama films": "أفلام حربية درامية {}",
        "action drama films": "أفلام حركة درامية {}",
        "adventure drama films": "أفلام مغامرات درامية {}",
        "animated drama films": "أفلام رسوم متحركة درامية {}",
        "children's drama films": "أفلام أطفال درامية {}",
        "crime drama films": "أفلام جريمة درامية {}",
        "erotic drama films": "أفلام إغرائية درامية {}",
        "fantasy drama films": "أفلام فانتازيا درامية {}",
        "horror drama films": "أفلام رعب درامية {}",
    }
)
Films_key_For_nat.update(Films_key_For_nat_extended)

Films_key_For_nat.update(
    {
        "science fiction film series endings": "سلاسل أفلام خيال علمي {} انتهت في",
        "science fiction film series debuts": "سلاسل أفلام خيال علمي {} بدأ عرضها في",
        "television series revived after cancellation": "مسلسلات تلفزيونية {} أعيدت بعد إلغائها",
        "web series endings": "مسلسلات ويب {} انتهت في",
        "animated television series endings": "مسلسلات تلفزيونية رسوم متحركة {} انتهت في",
        "comics endings": "قصص مصورة {} انتهت في",
        "television series endings": "مسلسلات تلفزيونية {} انتهت في",
        "television series debuts": "مسلسلات تلفزيونية {} بدأ عرضها في",
        "comics debuts": "قصص مصورة {} بدأ عرضها في",
        "animated television series debuts": "مسلسلات تلفزيونية رسوم متحركة {} بدأ عرضها في",
        "web series debuts": "مسلسلات ويب {} بدأ عرضها في",
        "anime television series debuts": "مسلسلات تلفزيونية أنمي {} بدأ عرضها في",
        "supernatural television series": "مسلسلات تلفزيونية خارقة للطبيعة {}",
        "supernatural comics": "قصص مصورة خارقة للطبيعة {}",
        "adult animated supernatural television series": "مسلسلات تلفزيونية رسوم متحركة خارقة للطبيعة للكبار {}",
        "superhero film series": "سلاسل أفلام أبطال خارقين {}",
        "superhero television episodes": "حلقات تلفزيونية أبطال خارقين {}",
        "superhero video games": "ألعاب فيديو أبطال خارقين {}",
        "superhero web series": "مسلسلات ويب أبطال خارقين {}",
        "superhero television films": "أفلام تلفزيونية أبطال خارقين {}",
        "superhero comics": "قصص مصورة أبطال خارقين {}",
        "superhero television characters": "شخصيات تلفزيونية أبطال خارقين {}",
        "superhero television series": "مسلسلات تلفزيونية أبطال خارقين {}",
    }
)

# Build television CAO mappings
Films_key_CAO, ss_Films_key_CAO = _build_television_cao(film_keys_for_female)

# Build female combination keys
# Films_keys_both_new_female = _build_female_combo_keys(Films_keys_male_female)
Films_keys_both_new_female = open_json_file("Films_keys_both_new_female_found.json")

# Legacy aliases
film_key_women_2 = TELEVISION_BASE_KEYS
television_keys = TELEVISION_KEYS

# Summary output
len_print.data_len(
    "films_mslslat.py",
    {
        "Films_key_For_nat_extended": Films_key_For_nat_extended,
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
        # "films_key_for_nat_extended_org": films_key_for_nat_extended_org,
        # "films_mslslat_tab_base_org": films_mslslat_tab_base_org,
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
    "Films_key_For_nat",
    "Films_key_man",
    "Films_keys_both_new_female",
    "film_key_women_2",
]

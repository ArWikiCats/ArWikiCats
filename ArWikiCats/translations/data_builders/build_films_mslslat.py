#!/usr/bin/python3
"""
Film and TV Series Translation Mappings.

Builds translation mappings for film and television categories from English to Arabic,
handling gender-specific translations and nationality-based categories.
"""

from typing import Dict, List, Tuple

# =============================================================================
# Helper Functions
# =============================================================================


def _build_gender_key_maps(
    films_key_o_multi: Dict[str, Dict[str, str]],
) -> Tuple[
    Dict[str, Dict[str, str]],
    Dict[str, str],
]:  # films_key_both  # films_key_man
    """
    Build gender-aware film key mappings from a source mapping of keys to gendered labels.

    Parameters:
        films_key_o_multi (Dict[str, Dict[str, str]]): Mapping from English keys to dictionaries containing at least 'male' and/or 'female' labels.

    Returns:
        Tuple[Dict[str, Dict[str, str]], Dict[str, str]]:
            films_key_both: Mapping of lowercase English keys to the original label dictionaries (contains 'male' and/or 'female' entries).
            films_key_man: Mapping of English keys to the male Arabic label; also includes animated variants (keys prefixed with "animated ") whose value appends the Arabic "رسوم متحركة" phrase to the male label.
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
    Build a mapping from English keys to their female Arabic labels, treating "animated" as an alias for "animation".
    
    Parameters:
        films_keys_male_female (Dict[str, Dict[str, str]]): Mapping from English keys to label dictionaries containing at least 'male' and/or 'female' entries.
    
    Returns:
        Dict[str, str]: Mapping of English keys to their female Arabic labels (only keys with a non-empty female label are included).
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
    SERIES_DEBUTS_ENDINGS: Dict[str, str],
    TELEVISION_BASE_KEYS_FEMALE: Dict[str, str],
    DEBUTS_ENDINGS_KEYS: List[str],
) -> Tuple[Dict[str, str], Dict[str, str]]:
    """
    Construct nationality-aware and series-based Arabic translation mappings for film and television keys.
    
    Parameters:
        female_keys (Dict[str, str]): Mapping of English film/series keys to their Arabic female labels.
        SERIES_DEBUTS_ENDINGS (Dict[str, str]): Predefined templates that include a `{}` placeholder for nationality-aware phrases.
        TELEVISION_BASE_KEYS_FEMALE (Dict[str, str]): Base television-related keys mapped to their Arabic female labels.
        DEBUTS_ENDINGS_KEYS (List[str]): List of television base keys (lowercased) that should also have dashed `-debuts`/`-endings` variants.
    
    Returns:
        Tuple[Dict[str, str], Dict[str, str]]: 
            - films_key_for_nat: Mapping of English keys (some containing `{}`) to Arabic templates that include a `{}` placeholder for nationality insertion.
            - films_mslslat_tab: Mapping of the same English keys to Arabic phrases without the nationality placeholder.
    """
    _mslslat_tab = {}
    _key_for_nat = {}

    # Add fixed templates
    _key_for_nat.update(SERIES_DEBUTS_ENDINGS)

    # Add remakes mapping
    _key_for_nat["remakes of {} films"] = "أفلام {{}} معاد إنتاجها"

    # Build base series keys
    for tt, tt_lab in TELEVISION_BASE_KEYS_FEMALE.items():
        _key_for_nat[tt] = f"{tt_lab} {{}}"
        _mslslat_tab[tt] = tt_lab

        # Debuts, endings, revived variants
        for suffix, arabic_suffix in [
            ("debuts", "بدأ عرضها في"),
            ("endings", "انتهت في"),
            ("revived after cancellation", "أعيدت بعد إلغائها"),
        ]:
            key_with_suffix = f"{tt} {suffix}"
            _key_for_nat[key_with_suffix] = f"{tt_lab} {{}} {arabic_suffix}"
            _mslslat_tab[key_with_suffix] = f"{tt_lab} {arabic_suffix}"

        # Dashed variants for specific keys
        if tt.lower() in DEBUTS_ENDINGS_KEYS:
            for suffix, arabic_suffix in [("debuts", "بدأ عرضها في"), ("endings", "انتهت في")]:
                dashed_key = f"{tt}-{suffix}"
                _key_for_nat[dashed_key] = f"{tt_lab} {{}} {arabic_suffix}"
                _mslslat_tab[dashed_key] = f"{tt_lab} {arabic_suffix}"

    # Build combinations of female film keys with series keys
    for ke, ke_lab in female_keys.items():
        for tt, tt_lab in TELEVISION_BASE_KEYS_FEMALE.items():
            key_base = f"{ke} {tt}"

            # Base combination
            _key_for_nat[key_base] = f"{tt_lab} {ke_lab} {{}}"
            _mslslat_tab[key_base] = f"{tt_lab} {ke_lab}"

            # Debuts, endings, revived variants
            for suffix, arabic_suffix in [
                ("debuts", "بدأ عرضها في"),
                ("endings", "انتهت في"),
                ("revived after cancellation", "أعيدت بعد إلغائها"),
            ]:
                combo_key = f"{key_base} {suffix}"

                if suffix == "revived after cancellation":
                    _key_for_nat[combo_key] = f"{tt_lab} {ke_lab} {{}} {arabic_suffix}"
                    _mslslat_tab[combo_key] = f"{tt_lab} {ke_lab} {arabic_suffix}"
                else:
                    _key_for_nat[combo_key] = f"{tt_lab} {ke_lab} {{}} {arabic_suffix}"
                    _mslslat_tab[combo_key] = f"{tt_lab} {ke_lab} {arabic_suffix}"

            # Dashed variants
            if tt.lower() in DEBUTS_ENDINGS_KEYS:
                for suffix, arabic_suffix in [("debuts", "بدأ عرضها في"), ("endings", "انتهت في")]:
                    dashed_key = f"{key_base}-{suffix}"
                    _key_for_nat[dashed_key] = f"{tt_lab} {ke_lab} {{}} {arabic_suffix}"
                    _mslslat_tab[dashed_key] = f"{tt_lab} {ke_lab} {arabic_suffix}"

    return _key_for_nat, _mslslat_tab


def _build_television_cao(
    female_keys: Dict[str, str],
    TELEVISION_KEYS: Dict[str, str],
) -> Tuple[Dict[str, str], Dict[str, str]]:
    """
    Build CAO (characters, albums, organizations, etc.) translation mappings by combining female-key labels with television and genre categories.
    
    Parameters:
        female_keys (Dict[str, str]): Mapping from English keys to their Arabic female labels (e.g., "comedy" -> "كوميدية").
        TELEVISION_KEYS (Dict[str, str]): Mapping of base television-related English keys to Arabic labels (e.g., "title" -> "عنوان").
    
    Returns:
        Tuple[Dict[str, str], Dict[str, str]]: 
            - films_key_cao: Mapping of combined keys to Arabic CAO phrases (e.g., "comedy characters" -> "شخصيات كوميدية").
            - films_key_cao2: Extended mappings combining female keys with TELEVISION_KEYS (e.g., "comedy title" -> "عنوان كوميدية").
    """
    films_key_cao2 = {}
    films_key_cao = {}

    # Base TV keys with common suffixes
    for ff, label in TELEVISION_KEYS.items():
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
        if not ke or not ke_lab:
            continue
        # Special cases
        films_key_cao[f"children's {ke}"] = f"أطفال {ke_lab}"
        films_key_cao[f"{ke} film remakes"] = f"أفلام {ke_lab} معاد إنتاجها"

        # Standard categories
        for suffix, arabic_base in genre_categories:
            if not suffix or not arabic_base:
                continue
            films_key_cao[f"{ke} {suffix}"] = f"{arabic_base} {ke_lab}"

        # Combinations with all TV keys
        for fao, base_label in TELEVISION_KEYS.items():
            if not fao or not base_label:
                continue
            films_key_cao2[f"{ke} {fao}"] = f"{base_label} {ke_lab}"

    return films_key_cao, films_key_cao2


# =============================================================================
# Module Initialization
# =============================================================================


__all__ = [
    "_build_gender_key_maps",
    "_extend_females_labels",
    "_build_series_and_nat_keys",
    "_build_television_cao",
]
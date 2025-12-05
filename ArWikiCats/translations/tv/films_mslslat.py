#!/usr/bin/python3
"""
new pages from file

python3 core8/pwb.py update/update

TODO: need refactoring
"""

from ...helps import len_print

from typing import Dict, Tuple

from ..utils.json_dir import open_json_file


# --- base templates / helpers -------------------------------------------------

Films_Key_for_mat2 = {
    "television-series debuts": "مسلسلات تلفزيونية {} بدأ عرضها في",
    "television-series endings": "مسلسلات تلفزيونية {} انتهت في",
    "web series-debuts": "مسلسلات ويب {} بدأ عرضها في",
    "web series debuts": "مسلسلات ويب {} بدأ عرضها في",
    "television series-debuts": "مسلسلات تلفزيونية {} بدأ عرضها في",
    "television series debuts": "مسلسلات تلفزيونية {} بدأ عرضها في",
    "television series endings": "مسلسلات تلفزيونية {} انتهت في",
}

film_key_women_2 = {
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

debuts_endings_key = ["television series", "television miniseries", "television films"]

nat_key_f = "{}"

Films_key_CAO_new_format = {
    "lgbtq-related films": "أفلام {} متعلقة بإل جي بي تي كيو",
}


# --- pure builder helpers -----------------------------------------------------


def _build_gender_key_maps(
    films_keys_male_female: Dict[str, Dict[str, str]],
    films_key_o_multi: Dict[str, Dict[str, str]],
) -> Tuple[
    Dict[str, Dict[str, str]],
    Dict[str, str],
    Dict[str, str],
    Dict[str, str],
    Dict[str, str],
]:
    """Build gender-aware film key mappings from the JSON sources.

    Returns:
        films_key_both: english key (lower) -> {"male": ..., "female": ...}
        films_key_333: english key (original) -> female label
        films_key_man: english key -> male label (with animated variants)
        film_keys_for_male: english key -> male label
        film_keys_for_female: english key -> female label
    """
    films_key_both: Dict[str, Dict[str, str]] = {}
    films_key_333: Dict[str, str] = {}
    films_key_man: Dict[str, str] = {}
    film_keys_for_male: Dict[str, str] = {}
    film_keys_for_female: Dict[str, str] = {}

    def _consume_source(source: Dict[str, Dict[str, str]]) -> None:
        """Merge a male/female mapping source into the combined structures."""
        for en_key, labels in source.items():
            key_lower = en_key.lower()
            films_key_both[key_lower] = labels
            female_label = labels.get("female", "").strip()
            if female_label:
                films_key_333[en_key] = female_label

    _consume_source(films_key_o_multi)

    # Alias "animated" to "animation" if present
    if "animated" in films_key_both:
        films_key_both["animation"] = films_key_both["animated"]

    # Build gender-specific maps
    for en_key, labels in films_key_both.items():
        male_label = labels.get("male", "").strip()
        female_label = labels.get("female", "").strip()

        if male_label:
            films_key_man[en_key] = male_label
            # Add explicit animated variant for male only
            if "animated" not in en_key:
                films_key_man[f"animated {en_key}"] = f"{male_label} رسوم متحركة"
            film_keys_for_male[en_key] = male_label

        if female_label:
            film_keys_for_female[en_key] = female_label

    films_keys_male_female = dict(films_keys_male_female)
    # Alias "animated" to "animation" if present
    if "animated" in films_keys_male_female:
        films_keys_male_female["animation"] = films_keys_male_female["animated"]

    for en_key, labels in films_keys_male_female.items():
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


def _extend_films_key_for_nat_with_mat2(
    films_key_for_nat: Dict[str, str],
) -> Dict[str, str]:
    """Extend Films_key_For_nat with additional fixed television/web templates."""
    for key, label in Films_Key_for_mat2.items():
        films_key_for_nat[key] = label
    return films_key_for_nat


def _build_series_and_nat_keys(
    films_key_for_nat: Dict[str, str],
    female_keys: Dict[str, str],
) -> Tuple[Dict[str, str], Dict[str, str]]:
    """Build Films_key_For_nat and films_mslslat_tab for series and combinations."""
    films_mslslat_tab: Dict[str, str] = {}

    # Base series keys (television, web, comics, etc.)
    for tt, tt_lab in film_key_women_2.items():
        films_key_for_nat[tt] = f"{tt_lab} {nat_key_f}"
        films_key_for_nat[f"{tt} debuts"] = f"{tt_lab} {nat_key_f} بدأ عرضها في"
        films_key_for_nat[f"{tt} endings"] = f"{tt_lab} {nat_key_f} انتهت في"
        films_key_for_nat[f"{tt} revived after cancellation"] = (
            f"{tt_lab} {nat_key_f} أعيدت بعد إلغائها"
        )

        films_mslslat_tab[tt] = tt_lab
        films_mslslat_tab[f"{tt} revived after cancellation"] = (
            f"{tt_lab} أعيدت بعد إلغائها"
        )
        films_mslslat_tab[f"{tt} debuts"] = f"{tt_lab} بدأ عرضها في"
        films_mslslat_tab[f"{tt} endings"] = f"{tt_lab} انتهت في"

        # Handle dashed variants for specific television keys
        if tt.lower() in debuts_endings_key:
            films_mslslat_tab[f"{tt}-debuts"] = f"{tt_lab} بدأ عرضها في"
            films_mslslat_tab[f"{tt}-endings"] = f"{tt_lab} انتهت في"
            films_key_for_nat[f"{tt}-debuts"] = (
                f"{tt_lab} {nat_key_f} بدأ عرضها في"
            )
            films_key_for_nat[f"{tt}-endings"] = (
                f"{tt_lab} {nat_key_f} انتهت في"
            )

    # Remakes mapping
    films_key_for_nat["remakes of {} films"] = f"أفلام {nat_key_f} معاد إنتاجها"

    # Combinations of female film keys with series keys
    for ke, ke_lab in female_keys.items():
        for tt, tt_lab in film_key_women_2.items():
            key_base = f"{ke} {tt}"

            films_key_for_nat[key_base] = f"{tt_lab} {ke_lab} {nat_key_f}"
            films_key_for_nat[f"{key_base} revived after cancellation"] = (
                f"{tt_lab} {ke_lab} {nat_key_f} أعيدت بعد إلغائها"
            )
            films_key_for_nat[f"{key_base} debuts"] = (
                f"{tt_lab} {ke_lab} {nat_key_f} بدأ عرضها في"
            )
            films_key_for_nat[f"{key_base} endings"] = (
                f"{tt_lab} {ke_lab} {nat_key_f} انتهت في"
            )

            films_mslslat_tab[key_base] = f"{tt_lab} {ke_lab}"
            films_mslslat_tab[f"{key_base} revived after cancellation"] = (
                f"{tt_lab} {ke_lab} {nat_key_f} أعيدت بعد إلغائها"
            )
            films_mslslat_tab[f"{key_base} debuts"] = (
                f"{tt_lab} {ke_lab} بدأ عرضها في"
            )
            films_mslslat_tab[f"{key_base} endings"] = (
                f"{tt_lab} {ke_lab} انتهت في"
            )

            if tt.lower() in debuts_endings_key:
                films_mslslat_tab[f"{key_base}-debuts"] = (
                    f"{tt_lab} {ke_lab} بدأ عرضها في"
                )
                films_mslslat_tab[f"{key_base}-endings"] = (
                    f"{tt_lab} {ke_lab} انتهت في"
                )
                films_key_for_nat[f"{key_base}-debuts"] = (
                    f"{tt_lab} {ke_lab} {nat_key_f} بدأ عرضها في"
                )
                films_key_for_nat[f"{key_base}-endings"] = (
                    f"{tt_lab} {ke_lab} {nat_key_f} انتهت في"
                )

    return films_key_for_nat, films_mslslat_tab


def _build_television_cao(
    tv_keys: Dict[str, str],
    female_keys: Dict[str, str],
) -> Tuple[Dict[str, str], int]:
    """Build Films_key_CAO mappings for TV/media-related categories."""
    films_key_cao: Dict[str, str] = {}
    count = 0

    # Base TV keys (per language-independent tv_keys)
    for ff, label in tv_keys.items():
        films_key_cao[ff] = label
        films_key_cao[f"{ff} characters"] = f"شخصيات {label}"
        films_key_cao[f"{ff} title cards"] = f"بطاقات عنوان {label}"
        films_key_cao[f"{ff} video covers"] = f"أغلفة فيديو {label}"
        films_key_cao[f"{ff} posters"] = f"ملصقات {label}"
        films_key_cao[f"{ff} images"] = f"صور {label}"

    # Combinations with film genres (female_keys)
    for ke, ke_lab in female_keys.items():
        films_key_cao[f"{ke} anime and manga"] = f"أنمي ومانغا {ke_lab}"
        films_key_cao[f"{ke} compilation albums"] = f"ألبومات تجميعية {ke_lab}"
        films_key_cao[f"{ke} folk albums"] = f"ألبومات فلكلورية {ke_lab}"
        films_key_cao[f"{ke} classical albums"] = f"ألبومات كلاسيكية {ke_lab}"
        films_key_cao[f"{ke} comedy albums"] = f"ألبومات كوميدية {ke_lab}"
        films_key_cao[f"{ke} mixtape albums"] = f"ألبومات ميكستايب {ke_lab}"
        films_key_cao[f"{ke} soundtracks"] = f"موسيقى تصويرية {ke_lab}"
        films_key_cao[f"{ke} terminology"] = f"مصطلحات {ke_lab}"
        films_key_cao[f"children's {ke}"] = f"أطفال {ke_lab}"
        films_key_cao[f"{ke} television series"] = f"مسلسلات تلفزيونية {ke_lab}"
        films_key_cao[f"{ke} television episodes"] = f"حلقات تلفزيونية {ke_lab}"
        films_key_cao[f"{ke} television programs"] = f"برامج تلفزيونية {ke_lab}"
        films_key_cao[f"{ke} television programmes"] = f"برامج تلفزيونية {ke_lab}"
        films_key_cao[f"{ke} groups"] = f"مجموعات {ke_lab}"
        films_key_cao[f"{ke} novellas"] = f"روايات قصيرة {ke_lab}"
        films_key_cao[f"{ke} novels"] = f"روايات {ke_lab}"
        films_key_cao[f"{ke} film remakes"] = f"أفلام {ke_lab} معاد إنتاجها"
        films_key_cao[f"{ke} films"] = f"أفلام {ke_lab}"

        for fao, base_label in tv_keys.items():
            count += 1
            films_key_cao[f"{ke} {fao}"] = f"{base_label} {ke_lab}"

    return films_key_cao, count


def _build_female_combo_keys(
    films_keys_male_female: Dict[str, Dict[str, str]],
) -> Dict[str, str]:
    """Build all pairwise combinations of female labels (new key -> combined label)."""
    result: Dict[str, str] = {}

    base_female = {
        x: v["female"]
        for x, v in films_keys_male_female.items()
        if v.get("female", "").strip()
    }

    for en, tab in films_keys_male_female.items():
        tab_female = tab.get("female", "").strip()
        if not tab_female:
            continue

        for en2, tab2_female in base_female.items():
            if en == en2:
                continue
            new_key = f"{en} {en2}".lower()
            if tab2_female:
                new_lab_female = f"{tab_female} {tab2_female}"
                result[new_key] = new_lab_female

    return result


# --- module-level build pipeline ---------------------------------------------

television_keys = {
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


# Load JSON resources
Films_keys_male_female = open_json_file("media/Films_keys_male_female.json") or {}
Films_key_For_nat = open_json_file("media/Films_key_For_nat.json") or {}
_Films_key_O_multi = open_json_file("media/Films_key_O_multi.json") or {}
Films_key_O_multi = {x: v for x, v in _Films_key_O_multi.items() if v.get("male", "").strip() and v.get("female", "").strip()}

# Gender-aware film mappings
(
    Films_key_both,
    Films_key_333,
    Films_key_man,
    film_keys_for_male,
    film_keys_for_female,
) = _build_gender_key_maps(Films_keys_male_female, Films_key_O_multi)

# Convenient alias (kept for compatibility if used elsewhere)
Films_key2 = film_keys_for_female

# Nat/series keys (Films_key_For_nat + films_mslslat_tab)
Films_key_For_nat = _extend_films_key_for_nat_with_mat2(Films_key_For_nat)
Films_key_For_nat, films_mslslat_tab = _build_series_and_nat_keys(
    Films_key_For_nat,
    film_keys_for_female,
)

# Female values from Films_key_O_multi also contribute to Films_key_333
for cd, ff in Films_key_O_multi.items():
    female_label = ff.get("female", "").strip()
    if female_label:
        Films_key_333[cd] = female_label

# Television CAO mappings
Films_key_CAO, ss_Films_key_CAO = _build_television_cao(
    television_keys,
    film_keys_for_female,
)

# Extended female-only combinations (both keys)
Films_keys_both_new_female = _build_female_combo_keys(Films_keys_male_female)

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

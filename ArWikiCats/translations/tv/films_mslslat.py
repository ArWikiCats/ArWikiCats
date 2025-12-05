#!/usr/bin/python3
"""
Film and TV Series Translation Mappings Module.

This module builds and provides translation mappings for film and television
categories from English to Arabic, handling gender-specific translations,
nationality-based categories, and various media types.

The module loads JSON configuration files and generates multiple mapping
dictionaries used for category translation across the ArWikiCats system.
"""

from typing import Dict, Final, TypeAlias
from dataclasses import dataclass, field

from ...helps import len_print
from ..utils.json_dir import open_json_file


# Type Aliases for better readability
TranslationMap: TypeAlias = Dict[str, str]
GenderMapping: TypeAlias = Dict[str, Dict[str, str]]


@dataclass(frozen=True)
class Constants:
    """Immutable constants used throughout the translation process."""

    # Nationality placeholder for dynamic substitution
    NAT_PLACEHOLDER: str = "{}"

    # Keys that support debuts/endings variants
    DEBUTS_ENDINGS_KEYS: tuple[str, ...] = (
        "television series",
        "television miniseries",
        "television films"
    )

    # Fixed television/web series templates
    SERIES_DEBUTS_ENDINGS: TranslationMap = field(default_factory=lambda: {
        "television-series debuts": "مسلسلات تلفزيونية {} بدأ عرضها في",
        "television-series endings": "مسلسلات تلفزيونية {} انتهت في",
        "web series-debuts": "مسلسلات ويب {} بدأ عرضها في",
        "web series debuts": "مسلسلات ويب {} بدأ عرضها في",
        "television series-debuts": "مسلسلات تلفزيونية {} بدأ عرضها في",
        "television series debuts": "مسلسلات تلفزيونية {} بدأ عرضها في",
        "television series endings": "مسلسلات تلفزيونية {} انتهت في",
    })

    # General television/media category base translations
    TELEVISION_BASE_KEYS: TranslationMap = field(default_factory=lambda: {
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
    })

    # Legacy CAO format for LGBTQ-related films
    LGBTQ_RELATED_FILMS: TranslationMap = field(default_factory=lambda: {
        "lgbtq-related films": "أفلام {} متعلقة بإل جي بي تي كيو",
    })


# Module-level constants instance
CONST: Final = Constants()


class TranslationBuilder:
    """
    Builder class for constructing film and television translation mappings.

    This class encapsulates the logic for building various translation
    dictionaries from JSON sources and static templates.
    """

    def __init__(
        self,
        films_keys_male_female: GenderMapping,
        films_key_o_multi: GenderMapping,
        films_key_for_nat_base: TranslationMap,
        television_keys: TranslationMap,
    ):
        """
        Initialize the translation builder.

        Args:
            films_keys_male_female: Gender-specific film category mappings
            films_key_o_multi: Additional gender mappings from O_multi source
            films_key_for_nat_base: Base nationality-aware translations
            television_keys: Base television category translations
        """
        self.films_keys_male_female = films_keys_male_female
        self.films_key_o_multi = films_key_o_multi
        self.films_key_for_nat_base = films_key_for_nat_base
        self.television_keys = television_keys

    def build_gender_key_maps(
        self,
    ) -> tuple[
        GenderMapping,  # films_key_both
        TranslationMap,  # films_key_333
        TranslationMap,  # films_key_man
        TranslationMap,  # film_keys_for_male
        TranslationMap,  # film_keys_for_female
    ]:
        """
        Build gender-aware film key mappings from JSON sources.

        This method consolidates male and female translations from multiple
        sources into unified mappings.

        Returns:
            A tuple containing:
            - films_key_both: Lowercase English key → {male, female} labels
            - films_key_333: Original English key → female label
            - films_key_man: English key → male label (with animated variants)
            - film_keys_for_male: English key → male label
            - film_keys_for_female: English key → female label
        """
        films_key_both: GenderMapping = {}
        films_key_333: TranslationMap = {}
        films_key_man: TranslationMap = {}
        film_keys_for_male: TranslationMap = {}
        film_keys_for_female: TranslationMap = {}

        # Merge films_key_o_multi into the combined structure
        self._consume_gender_source(
            self.films_key_o_multi,
            films_key_both,
            films_key_333,
        )

        # Handle "animated" → "animation" aliasing
        self._add_animation_alias(films_key_both)

        # Build gender-specific maps
        self._populate_gender_specific_maps(
            films_key_both,
            films_key_man,
            film_keys_for_male,
            film_keys_for_female,
        )

        # Process films_keys_male_female (with animation aliasing)
        male_female_copy = dict(self.films_keys_male_female)
        self._add_animation_alias(male_female_copy)

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

    @staticmethod
    def _consume_gender_source(
        source: GenderMapping,
        films_key_both: GenderMapping,
        films_key_333: TranslationMap,
    ) -> None:
        """
        Merge a gender mapping source into the combined structures.

        Args:
            source: Source mapping with male/female labels
            films_key_both: Target mapping for both genders
            films_key_333: Target mapping for female labels
        """
        for en_key, labels in source.items():
            key_lower = en_key.lower()
            films_key_both[key_lower] = labels
            female_label = labels.get("female", "").strip()
            if female_label:
                films_key_333[en_key] = female_label

    @staticmethod
    def _add_animation_alias(mapping: GenderMapping) -> None:
        """
        Add "animation" as an alias to "animated" if present.

        Args:
            mapping: Mapping to update in-place
        """
        if "animated" in mapping:
            mapping["animation"] = mapping["animated"]

    @staticmethod
    def _populate_gender_specific_maps(
        films_key_both: GenderMapping,
        films_key_man: TranslationMap,
        film_keys_for_male: TranslationMap,
        film_keys_for_female: TranslationMap,
    ) -> None:
        """
        Populate male and female specific translation maps.

        Args:
            films_key_both: Source with both genders
            films_key_man: Target for male translations (with animated variants)
            film_keys_for_male: Target for male translations
            film_keys_for_female: Target for female translations
        """
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

    def build_series_and_nat_keys(
        self,
        female_keys: TranslationMap,
    ) -> tuple[TranslationMap, TranslationMap]:
        """
        Build nationality-aware and series-based translation mappings.

        This method generates comprehensive mappings for TV series, including
        debuts, endings, revivals, and combinations with film genres.

        Args:
            female_keys: Female-gendered film category labels

        Returns:
            A tuple containing:
            - films_key_for_nat: Nationality-aware translations
            - films_mslslat_tab: Series translations without nationality
        """
        films_key_for_nat = dict(self.films_key_for_nat_base)
        films_mslslat_tab: TranslationMap = {}

        # Extend with fixed templates
        films_key_for_nat.update(CONST.SERIES_DEBUTS_ENDINGS)

        # Build base series keys
        self._build_base_series_keys(films_key_for_nat, films_mslslat_tab)

        # Add remakes mapping
        films_key_for_nat["remakes of {} films"] = f"أفلام {CONST.NAT_PLACEHOLDER} معاد إنتاجها"

        # Build combinations of female film keys with series keys
        self._build_genre_series_combinations(
            films_key_for_nat,
            films_mslslat_tab,
            female_keys,
        )

        return films_key_for_nat, films_mslslat_tab

    def _build_base_series_keys(
        self,
        films_key_for_nat: TranslationMap,
        films_mslslat_tab: TranslationMap,
    ) -> None:
        """
        Build base series keys for television/web/comics categories.

        Args:
            films_key_for_nat: Target nationality-aware mapping
            films_mslslat_tab: Target series mapping without nationality
        """
        for tt, tt_lab in CONST.TELEVISION_BASE_KEYS.items():
            # Base key with nationality
            films_key_for_nat[tt] = f"{tt_lab} {CONST.NAT_PLACEHOLDER}"
            films_mslslat_tab[tt] = tt_lab

            # Debuts, endings, and revived variants
            for suffix, arabic_suffix in [
                ("debuts", "بدأ عرضها في"),
                ("endings", "انتهت في"),
                ("revived after cancellation", "أعيدت بعد إلغائها"),
            ]:
                key_with_suffix = f"{tt} {suffix}"
                films_key_for_nat[key_with_suffix] = (
                    f"{tt_lab} {CONST.NAT_PLACEHOLDER} {arabic_suffix}"
                )
                films_mslslat_tab[key_with_suffix] = f"{tt_lab} {arabic_suffix}"

            # Handle dashed variants for specific keys
            if tt.lower() in CONST.DEBUTS_ENDINGS_KEYS:
                for suffix, arabic_suffix in [("debuts", "بدأ عرضها في"), ("endings", "انتهت في")]:
                    dashed_key = f"{tt}-{suffix}"
                    films_key_for_nat[dashed_key] = (
                        f"{tt_lab} {CONST.NAT_PLACEHOLDER} {arabic_suffix}"
                    )
                    films_mslslat_tab[dashed_key] = f"{tt_lab} {arabic_suffix}"

    def _build_genre_series_combinations(
        self,
        films_key_for_nat: TranslationMap,
        films_mslslat_tab: TranslationMap,
        female_keys: TranslationMap,
    ) -> None:
        """
        Build combinations of film genres with TV series categories.

        Args:
            films_key_for_nat: Target nationality-aware mapping
            films_mslslat_tab: Target series mapping
            female_keys: Female-gendered film category labels
        """
        for ke, ke_lab in female_keys.items():
            for tt, tt_lab in CONST.TELEVISION_BASE_KEYS.items():
                key_base = f"{ke} {tt}"

                # Base combination
                films_key_for_nat[key_base] = (
                    f"{tt_lab} {ke_lab} {CONST.NAT_PLACEHOLDER}"
                )
                films_mslslat_tab[key_base] = f"{tt_lab} {ke_lab}"

                # Debuts, endings, and revived variants
                for suffix, arabic_suffix in [
                    ("debuts", "بدأ عرضها في"),
                    ("endings", "انتهت في"),
                    ("revived after cancellation", "أعيدت بعد إلغائها"),
                ]:
                    combo_key = f"{key_base} {suffix}"

                    if suffix == "revived after cancellation":
                        # Special format for revived
                        films_key_for_nat[combo_key] = (
                            f"{tt_lab} {ke_lab} {CONST.NAT_PLACEHOLDER} {arabic_suffix}"
                        )
                        films_mslslat_tab[combo_key] = (
                            f"{tt_lab} {ke_lab} {CONST.NAT_PLACEHOLDER} {arabic_suffix}"
                        )
                    else:
                        films_key_for_nat[combo_key] = (
                            f"{tt_lab} {ke_lab} {CONST.NAT_PLACEHOLDER} {arabic_suffix}"
                        )
                        films_mslslat_tab[combo_key] = f"{tt_lab} {ke_lab} {arabic_suffix}"

                # Dashed variants for specific keys
                if tt.lower() in CONST.DEBUTS_ENDINGS_KEYS:
                    for suffix, arabic_suffix in [("debuts", "بدأ عرضها في"), ("endings", "انتهت في")]:
                        dashed_key = f"{key_base}-{suffix}"
                        films_key_for_nat[dashed_key] = (
                            f"{tt_lab} {ke_lab} {CONST.NAT_PLACEHOLDER} {arabic_suffix}"
                        )
                        films_mslslat_tab[dashed_key] = f"{tt_lab} {ke_lab} {arabic_suffix}"

    def build_television_cao(
        self,
        female_keys: TranslationMap,
    ) -> tuple[TranslationMap, int]:
        """
        Build CAO (Characters, Albums, Organizations, etc.) mappings.

        This method creates mappings for various media-related categories
        like characters, posters, soundtracks, etc.

        Args:
            female_keys: Female-gendered film category labels

        Returns:
            A tuple containing:
            - films_key_cao: CAO translation mapping
            - count: Number of genre-TV combinations created
        """
        films_key_cao: TranslationMap = {}
        count = 0

        # Base TV keys with common suffixes
        self._build_base_cao_keys(films_key_cao)

        # Combinations with film genres
        count = self._build_genre_cao_combinations(films_key_cao, female_keys)

        return films_key_cao, count

    def _build_base_cao_keys(self, films_key_cao: TranslationMap) -> None:
        """
        Build base CAO keys for television categories.

        Args:
            films_key_cao: Target CAO mapping
        """
        for ff, label in self.television_keys.items():
            films_key_cao[ff] = label

            # Add common media-related suffixes
            for suffix, arabic_suffix in [
                ("characters", "شخصيات"),
                ("title cards", "بطاقات عنوان"),
                ("video covers", "أغلفة فيديو"),
                ("posters", "ملصقات"),
                ("images", "صور"),
            ]:
                films_key_cao[f"{ff} {suffix}"] = f"{arabic_suffix} {label}"

    def _build_genre_cao_combinations(
        self,
        films_key_cao: TranslationMap,
        female_keys: TranslationMap,
    ) -> int:
        """
        Build genre-specific CAO combinations.

        Args:
            films_key_cao: Target CAO mapping
            female_keys: Female-gendered film category labels

        Returns:
            Count of genre-TV combinations created
        """
        count = 0

        # Predefined genre-based categories
        GENRE_CATEGORIES = [
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
            ("film remakes", "أفلام {} معاد إنتاجها"),
            ("films", "أفلام"),
        ]

        for ke, ke_lab in female_keys.items():
            # Special case for children's
            films_key_cao[f"children's {ke}"] = f"أطفال {ke_lab}"

            # Add predefined categories
            for suffix, arabic_template in GENRE_CATEGORIES:
                films_key_cao[f"{ke} {suffix}"] = arabic_template.replace("{}", ke_lab)

            # Add combinations with all TV keys
            for fao, base_label in self.television_keys.items():
                count += 1
                films_key_cao[f"{ke} {fao}"] = f"{base_label} {ke_lab}"

        return count

    @staticmethod
    def build_female_combo_keys(
        films_keys_male_female: GenderMapping,
    ) -> TranslationMap:
        """
        Build all pairwise combinations of female genre labels.

        This creates compound categories like "action comedy" from individual
        genre labels.

        Args:
            films_keys_male_female: Source gender mappings

        Returns:
            Mapping of combined English keys → combined Arabic labels
        """
        result: TranslationMap = {}

        # Extract base female labels
        base_female = {
            x: v["female"]
            for x, v in films_keys_male_female.items()
            if v.get("female", "").strip()
        }

        # Generate pairwise combinations
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


# --- Extended Television Keys Dictionary -----------------------------------

TELEVISION_KEYS: Final[TranslationMap] = {
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


# --- Module Initialization and Data Loading ----------------------------------

def _load_and_build_translations() -> tuple[
    TranslationMap,  # films_mslslat_tab
    TranslationMap,  # film_keys_for_female
    TranslationMap,  # film_keys_for_male
    TranslationMap,  # Films_key_333
    TranslationMap,  # Films_key_CAO
    TranslationMap,  # Films_key_For_nat
    TranslationMap,  # Films_key_man
    TranslationMap,  # Films_keys_both_new_female
]:
    """
    Load JSON resources and build all translation mappings.

    This is the main initialization function that orchestrates loading
    source data and building all translation dictionaries.

    Returns:
        A tuple of all generated translation mappings
    """
    # Load JSON resources
    films_keys_male_female_raw = open_json_file("media/Films_keys_male_female.json") or {}
    films_key_for_nat_raw = open_json_file("media/Films_key_For_nat.json") or {}
    films_key_o_multi_raw = open_json_file("media/Films_key_O_multi.json") or {}

    # Filter Films_key_O_multi to only include entries with both male and female
    films_key_o_multi_filtered = {
        x: v
        for x, v in films_key_o_multi_raw.items()
        if v.get("male", "").strip() and v.get("female", "").strip()
    }

    # Initialize builder
    builder = TranslationBuilder(
        films_keys_male_female=films_keys_male_female_raw,
        films_key_o_multi=films_key_o_multi_filtered,
        films_key_for_nat_base=films_key_for_nat_raw,
        television_keys=TELEVISION_KEYS,
    )

    # Build gender-aware mappings
    (
        _,  # films_key_both (not exported)
        films_key_333,
        films_key_man,
        film_keys_for_male,
        film_keys_for_female,
    ) = builder.build_gender_key_maps()

    # Build series and nationality keys
    films_key_for_nat, films_mslslat_tab = builder.build_series_and_nat_keys(
        film_keys_for_female
    )

    # Extend Films_key_333 with female labels from Films_key_O_multi
    for cd, ff in films_key_o_multi_filtered.items():
        female_label = ff.get("female", "").strip()
        if female_label:
            films_key_333[cd] = female_label

    # Build television CAO mappings
    films_key_cao, ss_films_key_cao = builder.build_television_cao(
        film_keys_for_female
    )

    # Build female combination keys
    films_keys_both_new_female = builder.build_female_combo_keys(
        films_keys_male_female_raw
    )

    # Log summary statistics
    len_print.data_len(
        "films_mslslat.py",
        {
            "television_keys": TELEVISION_KEYS,
            "Films_key_For_nat": films_key_for_nat,
            "films_mslslat_tab": films_mslslat_tab,
            "ss_Films_key_CAO": ss_films_key_cao,
            "Films_key_333": films_key_333,
            "Films_key_CAO": films_key_cao,
            "Films_keys_both_new_female": films_keys_both_new_female,
            "film_keys_for_female": film_keys_for_female,
            "film_keys_for_male": film_keys_for_male,
            "Films_key_man": films_key_man,
            "film_key_women_2": CONST.TELEVISION_BASE_KEYS,
        },
    )

    return (
        films_mslslat_tab,
        film_keys_for_female,
        film_keys_for_male,
        films_key_333,
        films_key_cao,
        films_key_for_nat,
        films_key_man,
        films_keys_both_new_female,
    )


# Execute initialization and export results
(
    films_mslslat_tab,
    film_keys_for_female,
    film_keys_for_male,
    Films_key_333,
    Films_key_CAO,
    Films_key_For_nat,
    Films_key_man,
    Films_keys_both_new_female,
) = _load_and_build_translations()

# Legacy alias (kept for backward compatibility)
film_key_women_2: Final[TranslationMap] = CONST.TELEVISION_BASE_KEYS
Films_key_CAO_new_format: Final[TranslationMap] = CONST.LGBTQ_RELATED_FILMS
television_keys: Final[TranslationMap] = TELEVISION_KEYS


# --- Public API Exports -------------------------------------------------------

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

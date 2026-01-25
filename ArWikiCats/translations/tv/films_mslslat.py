#!/usr/bin/python3
"""
Film and TV Series Translation Mappings.

Builds translation mappings for film and television categories from English to Arabic,
handling gender-specific translations and nationality-based categories.
"""

from typing import Dict, Tuple

from ..data_builders.build_films_mslslat import (
    _build_gender_key_maps,
    _build_television_cao,
)
from ..helps import len_print
from ..utils import open_json_file

# =============================================================================
# Constants
# =============================================================================

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
TELEVISION_BASE_KEYS_FEMALE = {
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
Films_key_both, Films_key_man = _build_gender_key_maps(Films_key_O_multi)

film_keys_for_male: Dict[str, str] = {
    x: v.get("male", "").strip() for x, v in Films_key_both.items() if v.get("male", "").strip()
}

film_keys_for_female = open_json_file("media/film_keys_for_female.json")
films_mslslat_tab_base = open_json_file("media/films_mslslat_tab_found.json")

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
Films_key_CAO, films_key_cao2 = _build_television_cao(film_keys_for_female, TELEVISION_KEYS)
Films_key_CAO.update(TELEVISION_KEYS)
Films_key_CAO.update(films_key_cao2)

# Build female combination keys
Films_keys_both_new_female = open_json_file("media/Films_keys_both_new_female_found.json")

# Summary output
len_print.data_len(
    "films_mslslat.py",
    {
        "Films_key_For_nat_extended": Films_key_For_nat_extended,
        "TELEVISION_KEYS": TELEVISION_KEYS,
        "Films_key_For_nat": Films_key_For_nat,
        "films_mslslat_tab": films_mslslat_tab,
        "films_key_cao2": films_key_cao2,
        "Films_key_CAO": Films_key_CAO,
        "Films_keys_both_new_female": Films_keys_both_new_female,
        "film_keys_for_female": film_keys_for_female,
        "film_keys_for_male": film_keys_for_male,
        "Films_key_man": Films_key_man,
        # "films_key_for_nat_extended_org": films_key_for_nat_extended_org,
        # "films_mslslat_tab_base_org": films_mslslat_tab_base_org,
    },
)


# =============================================================================
# Public API
# =============================================================================

__all__ = [
    "films_mslslat_tab",
    "film_keys_for_female",
    "film_keys_for_male",
    "Films_key_CAO",
    "Films_key_For_nat",
    "Films_key_man",
    "Films_keys_both_new_female",
]

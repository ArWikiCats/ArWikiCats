#!/usr/bin/python3
"""

TODO:
    - use this file instead of film_keys_bot.py
    - add formated_data from ArWikiCats/translations/tv/films_mslslat.py

"""

import functools
from typing import Dict

from ...helps import logger
from ...translations import (  # film_keys_for_female,
    Nat_women,
)
from ...translations_formats import MultiDataFormatterBase, format_films_country_data, format_multi_data

film_keys_for_female = {
    "3d": "ثلاثية الأبعاد",
    "4d": "رباعية الأبعاد",
    "action": "حركة",
    "action comedy": "حركة كوميدية",
    "action thriller": "إثارة حركة",
    "adaptation": "مقتبسة",
    "adult animated": "رسوم متحركة للكبار",
    "adult animated drama": "رسوم متحركة دراما للكبار",
    "adult animated supernatural": "رسوم متحركة خارقة للطبيعة للكبار",
    "adventure": "مغامرات",
    "animated": "رسوم متحركة",
    "animated science": "علمية رسوم متحركة",
    "animated short film": "رسوم متحركة قصيرة",
    "animated short": "رسوم متحركة قصيرة",
    "animation": "رسوم متحركة",
    "anime": "أنمي",
    "anthology": "أنثولوجيا",
    "apocalyptic": "نهاية العالم",
    "astronomical": "فلكية",
    "aviation": "طيران",
    "b movie": "درجة ثانية",
    "biographical": "سير ذاتية",
    "black": "سوداء",
    "black and white": "أبيض وأسود",
    "black comedy": "كوميدية سوداء",
    "black-and-white": "أبيض وأسود",
    "bollywood": "بوليوود",
    "buddy": "رفقاء",
    "cancelled": "ملغية",
    "cannibal": "آكلو لحم البشر",
    "chase": "مطاردة",
    "children's": "أطفال",
    "children's animated": "رسوم متحركة أطفال",
    "children's comedy": "أطفال كوميدية",
    "christmas": "عيد الميلاد",
    "colonial cinema": "استعمار",
    "comedy": "كوميدية",
    "comedy drama": "كوميدية درامية",
    "comedy fiction": "كوميدية خيالية",
    "comedy horror": "كوميدية رعب",
    "comedy thriller": "كوميدية إثارة",
    "comedy-drama": "كوميدية درامية",
    "comic science fiction": "خيالية علمية كوميدية",
    "coming-of-age": "تقدم في العمر",
    "coming-of-age story": "قصة تقدم في العمر",
    "computer animated": "حركة حاسوبية",
    "computer-animated": "حركة حاسوبية",
    "crime": "جريمة",
    "crime comedy": "جنائية كوميدية",
    "crime thriller": "إثارة وجريمة",
    "crime-comedy": "جنائية كوميدية",
    "criminal": "جنائية",
    "criminal comedy": "كوميديا الجريمة",
    "cyberpunk": "سايبربانك",
    "dance": "رقص",
    "dark fantasy": "فانتازيا مظلمة",
    "detective": "مباحث",
    "detective fiction": "خيالية بوليسية",
    "disaster": "كوارثية",
    "disney animated": "رسوم متحركة ديزني",
    "docudrama": "درامية وثائقية",
    "documentary": "وثائقية",
    "drama": "درامية",
    "educational": "تعليمية",
    "environment": "بيئية",
    "epic": "ملحمية",
    "erotic": "إغرائية",
    "erotic thriller": "إثارة جنسية",
    "european art cinema": "السينما الفنية الأوروبية",
    "experimental": "تجريبية",
    "exploitation": "استغلالية",
    "family": "عائلية",
    "fan": "معجبين",
    "fantasy": "فانتازيا",
    "feature": "طويلة",
    "female buddy": "رفيقات",
    "feminist": "نسوية",
    "fiction": "خيالية",
    "final fantasy": "فاينل فانتازي",
    "flashback": "استرجاع",
    "found footage": "تسجيلات مكتشفة",
    "free cinema": "سينما حرة",
    "gangster": "عصابات",
    "girls with guns": "فتيات مع أسلحة",
    "hacking": "إختراق",
    "heist": "سرقة",
    "historical": "تاريخية",
    "holocaust": "هولوكوستية",
    "hood": "هود",
    "horror": "رعب",
    "independent": "مستقلة",
    "interactive": "تفاعلية",
    "internet": "إنترنت",
    "japanese horror": "رعب يابانية",
    "joker": "جوكر",
    "kaiju": "كايجو",
    "kung fu": "كونغ فو",
    "latin": "لاتينية",
    "legal": "قانونية",
    "legal drama": "دراما قانونية",
    "legal thriller": "إثارة قانونية",
    "lgbt": "إل جي بي تي",
    "lgbtq": "إل جي بي تي كيو",
    "lgbtq-related": "متعلقة بإل جي بي تي كيو",
    "live": "مباشرة",
    "live-action": "حركة مباشرة",
    "lost": "مفقودة",
    "low-budget": "منخفضة التكلفة",
    "mafia": "مافيا",
    "magic realism": "واقعية سحرية",
    "magical girl": "فتاة ساحرة",
    "maritime": "بحرية",
    "martial arts": "فنون قتال",
    "melodrama": "ميلودراما",
    "metafictional": "ما وراء القص",
    "military": "عسكرية",
    "mixtape": "ميكستايب",
    "mockumentary": "وثائقية كاذبة",
    "monster": "وحوش",
    "music": "موسيقية",
    "musical": "موسيقية",
    "musical comedy": "كوميدية موسيقية",
    "mystery": "غموض",
    "nature documentary": "وثائقية برية",
    "nautical": "بحرية",
    "naval": "بحرية عسكرية",
    "neo-noir": "نيو-نوار",
    "noir": "نوار",
    "non fiction": "غير خيالية",
    "non narrative": "غير سردية",
    "non-fiction": "غير خيالية",
    "non-narrative": "غير سردية",
    "one man": "رجل واحد",
    "one-man": "رجل واحد",
    "parody": "ساخرة",
    "period": "حقبية",
    "pirate": "قراصنة",
    "police procedural": "إجراءات الشرطة",
    "political": "سياسية",
    "political cinema": "سينما سياسية",
    "political fiction": "خيالية سياسية",
    "political thriller": "إثارة سياسية",
    "porno": "إباحية",
    "pornographic": "إباحية",
    "post-apocalyptic": "ما بعد الكارثة",
    "prequel": "بادئة",
    "propaganda": "دعائية",
    "psychological": "نفسية",
    "psychological horror": "رعب نفسي",
    "psychological thriller": "إثارة نفسية",
    "reality": "واقعية",
    "reboot": "ريبوت",
    "rediscovered": "اكتشاف",
    "religious": "دينية",
    "remix": "ريمكس",
    "reportage": "تقرير",
    "robot": "آلية",
    "rockumentary": "وثائقي الروك",
    "romance": "رومانسية",
    "romantic": "رومانسية",
    "romantic comedy": "كوميدية رومانسية",
    "sailing": "إبحار",
    "samurai cinema": "ساموراي",
    "satire": "هجائية",
    "school": "مدرسية",
    "science": "علمية",
    "science fantasy": "فنتازيا علمية",
    "science fiction": "خيال علمي",
    "science fiction action": "خيال علمي وحركة",
    "science fiction thriller": "إثارة خيال علمي",
    "sequel": "متممة",
    "sex": "جنسية",
    "short": "قصيرة",
    "siddy": "أصدقاء",
    "silent": "صامتة",
    "silent short": "قصيرة صامته",
    "sisiness": "أعمال",
    "slapstick": "كوميدية تهريجية",
    "slasher": "تقطيع",
    "sound": "ناطقة",
    "spaghetti western": "سباغيتي وسترن",
    "speculative": "تأملية",
    "speculative fiction": "خيالية تأملية",
    "sports": "رياضية",
    "spy": "تجسسية",
    "street fighter": "قتال شوارع",
    "student": "طلاب",
    "submarines": "غواصات",
    "super robot": "آلية خارقة",
    "supernatural": "خارقة للطبيعة",
    "supernatural drama": "دراما خارقة للطبيعة",
    "survival": "البقاء على قيد الحياة",
    "teen": "مراهقة",
    "television": "تلفزيونية",
    "thriller": "إثارة",
    "tragicomedy": "تراجيدية كوميدية",
    "travel documentary": "وثائقي سفر",
    "treasure hunt": "صيد كنوز",
    "unfinished": "ناقصة",
    "upcoming": "قادمة",
    "vampire": "مصاصي دماء",
    "war": "حربية",
    "werewolve": "مستذئب",
    "western": "غرب أمريكية",
    "woman's": "نسائية",
    "zombie": "زومبي",
    "zombie comedy": "كوميدية الزومبي",
}


def _build_television_cao() -> tuple[Dict[str, str], Dict[str, str]]:
    """
    Build translation mappings for CAO-related film and television keys.

    Creates two dictionaries: one containing patterns that include nationality placeholders and film-key placeholders for generating localized Arabic labels, and another containing equivalent mappings that omit nationality placeholders.

    Returns:
        films_key_cao (dict): Mapping of English pattern keys (may include `{nat_en}` and `{film_key}`) to Arabic translation templates (may include `{nat_ar}` and `{film_ar}`).
        data_no_nats (dict): Mapping of English pattern keys (without nationality placeholders) to Arabic translation templates (may include `{film_ar}`).
    """
    data = {}
    data_no_nats = {}

    # Base TV keys with common suffixes
    for suffix, arabic_suffix in [
        ("characters", "شخصيات"),
        ("title cards", "بطاقات عنوان"),
        ("video covers", "أغلفة فيديو"),
        ("posters", "ملصقات"),
        ("images", "صور"),
    ]:
        data_no_nats.update(
            {
                f"{{film_key}} {suffix}": f"{arabic_suffix} {{film_ar}}",
            }
        )
        data.update(
            {
                f"{{nat_en}} {suffix}": f"{arabic_suffix} {{nat_ar}}",
                f"{{nat_en}} {{film_key}} {suffix}": f"{arabic_suffix} {{film_ar}} {{nat_ar}}",
            }
        )

    # Genre-based categories
    # ArWikiCats/jsons/media/Films_key_For_nat.json
    genre_categories = {
        # "fiction": "خيال",
        "film series": "سلاسل أفلام",
        "webcomics": "ويب كومكس",
        "anime and manga": "أنمي ومانغا",
        "compilation albums": "ألبومات تجميعية",
        "folk albums": "ألبومات فلكلورية",
        "classical albums": "ألبومات كلاسيكية",
        "comedy albums": "ألبومات كوميدية",
        "mixtape albums": "ألبومات ميكستايب",
        "soundtracks": "موسيقى تصويرية",
        "terminology": "مصطلحات",
        "series": "مسلسلات",
        "television series": "مسلسلات تلفزيونية",
        "television episodes": "حلقات تلفزيونية",
        "television programs": "برامج تلفزيونية",
        "television programmes": "برامج تلفزيونية",
        "groups": "مجموعات",
        "novellas": "روايات قصيرة",
        "novels": "روايات",
        "films": "أفلام",
        "comic strips": "شرائط كومكس",
        "comics": "قصص مصورة",
        "television shows": "عروض تلفزيونية",
        "television films": "أفلام تلفزيونية",
        "teams": "فرق",
        "television characters": "شخصيات تلفزيونية",
        "video games": "ألعاب فيديو",
        "web series": "مسلسلات ويب",
        "film characters": "شخصيات أفلام",
        "games": "ألعاب",
        "soap opera": "مسلسلات طويلة",
        "television news": "أخبار تلفزيونية",
        "miniseries": "مسلسلات قصيرة",
        "television miniseries": "مسلسلات قصيرة تلفزيونية",
    }

    genre_categories_skip_it = {
        "film characters",
        "series",
        "games",
    }

    # Standard categories
    for suffix, arabic_base in genre_categories.items():
        # Base TV keys with common suffixes
        for sub_suffix, arabic_sub_suffix in [
            ("characters", "شخصيات"),
            ("title cards", "بطاقات عنوان"),
            ("video covers", "أغلفة فيديو"),
            ("posters", "ملصقات"),
            ("images", "صور"),
        ]:
            data_no_nats.update(
                {
                    f"{suffix} {sub_suffix}": f"{arabic_sub_suffix} {arabic_base}",
                    f"{{film_key}} {suffix} {sub_suffix}": f"{arabic_sub_suffix} {arabic_base} {{film_ar}}",
                }
            )
            data.update(
                {
                    f"{{nat_en}} {suffix} {sub_suffix}": f"{arabic_sub_suffix} {arabic_base} {{nat_ar}}",
                    f"{{nat_en}} {{film_key}} {suffix} {sub_suffix}": f"{arabic_sub_suffix} {arabic_base} {{film_ar}} {{nat_ar}}",
                }
            )

        data_no_nats.update(
            {
                f"{suffix}": f"{arabic_base}",
                f"television {suffix}": f"{arabic_base} تلفزيونية",
                f"{{film_key}} {suffix}": f"{arabic_base} {{film_ar}}",
                f"children's-animated-superhero {suffix}": f"{arabic_base} رسوم متحركة أبطال خارقين للأطفال",
                f"children's-animated-adventure-television {suffix}": f"{arabic_base} مغامرات رسوم متحركة تلفزيونية للأطفال",
            }
        )

        # NOTE: we use genre_categories_skip_it because next line makes errors like:
        # "Category:Golf at 2022 Asian Games": "تصنيف:الغولف في ألعاب آسيوية في 2022",
        if suffix not in genre_categories_skip_it:
            data[f"{{nat_en}} {suffix}"] = f"{arabic_base} {{nat_ar}}"

        data.update(
            {
                f"{{nat_en}} {{film_key}} {suffix}": f"{arabic_base} {{film_ar}} {{nat_ar}}",
                f"{{nat_en}} children's-animated-superhero {suffix}": f"{arabic_base} رسوم متحركة أبطال خارقين {{nat_ar}} للأطفال",
                f"{{nat_en}} children's-animated-adventure-television {suffix}": f"{arabic_base} مغامرات رسوم متحركة تلفزيونية {{nat_ar}} للأطفال",
            }
        )

    return data, data_no_nats


@functools.lru_cache(maxsize=1)
def _make_bot() -> MultiDataFormatterBase:
    # NOTE: keys with non-patterns should be added to populate_film_patterns()
    # Template data with both nationality and sport placeholders
    """
    Create and configure formatter bots for film and television category translations.

    Builds and merges formatted pattern data (including television CAO entries and film-key mappings),
    prepares nationality and film-key lookup lists, and generates two formatter instances:
    - `double_bot`: a combined formatter populated with country+film patterns and additional adjustments.
    - `bot`: a multi-data formatter built from the same inputs.

    This function also updates `double_bot.other_bot` to set the `put_label_last` label ordering.

    Returns:
        tuple: `(double_bot, bot)` where `double_bot` is the combined MultiDataFormatterBase with populated film-country patterns and `bot` is an additional MultiDataFormatterBase built from the same formatted data.
    """
    formatted_data = {
        # "{nat_en} films": "أفلام {nat_ar}", #  [2000s American films] : "تصنيف:أفلام أمريكية في عقد 2000",
        "{nat_en} films": "أفلام {nat_ar}",
        # "Category:yemeni action Teen superhero films" : "تصنيف:أفلام حركة مراهقة يمنية أبطال خارقين",
        "{nat_en} television episodes": "حلقات تلفزيونية {nat_ar}",
        "{nat_en} television series": "مسلسلات تلفزيونية {nat_ar}",
        "{nat_en} television-seasons": "مواسم تلفزيونية {nat_ar}",
        "{nat_en} television seasons": "مواسم تلفزيونية {nat_ar}",
        "{nat_en} {film_key} television-seasons": "مواسم تلفزيونية {film_ar} {nat_ar}",
        "{nat_en} {film_key} television seasons": "مواسم تلفزيونية {film_ar} {nat_ar}",
        "{nat_en} {film_key} television series": "مسلسلات تلفزيونية {film_ar} {nat_ar}",
        "{nat_en} {film_key} filmszz": "أفلام {film_ar} {nat_ar}",
        "{nat_en} {film_key} films": "أفلام {film_ar} {nat_ar}",
        "{nat_en} {film_key} television commercials": "إعلانات تجارية تلفزيونية {film_ar} {nat_ar}",
        # TODO: move this to jobs bot?
        # "{nat_en} sports coaches": "مدربو رياضة {nat_ar}",
        "{nat_en} animated television films": "أفلام رسوم متحركة تلفزيونية {nat_ar}",
        "{nat_en} animated television series": "مسلسلات رسوم متحركة تلفزيونية {nat_ar}",
    }

    _data, data_no_nats = _build_television_cao()

    formatted_data.update(_data)

    other_formatted_data = {
        "{film_key} films": "أفلام {film_ar}",
        # "Category:action Teen superhero films" : "تصنيف:أفلام حركة مراهقة أبطال خارقين",
        "{film_key} television commercials": "إعلانات تجارية تلفزيونية {film_ar}",
        "animated television films": "أفلام رسوم متحركة تلفزيونية",
        "animated television series": "مسلسلات رسوم متحركة تلفزيونية",
    }
    other_formatted_data.update(data_no_nats)

    # film_keys_for_female
    data_list2 = {
        "action comedy": "حركة كوميدية",
        "action thriller": "إثارة حركة",
        "action": "حركة",
        "drama": "درامية",
        "upcoming": "قادمة",
        "horror": "رعب",
        "black-and-white": "أبيض وأسود",
        "psychological horror": "رعب نفسي",
    }

    put_label_last = {
        "low-budget",
        "supernatural",
        "christmas",
        "lgbtq-related",
        "upcoming",
    }

    data_list2 = dict(film_keys_for_female)
    data_list2.pop("television", None)

    # data_list2.pop("superhero", None)
    data_list2["superhero"] = "أبطال خارقين"

    double_bot = format_films_country_data(
        formatted_data=formatted_data,
        data_list=Nat_women,
        key_placeholder="{nat_en}",
        value_placeholder="{nat_ar}",
        data_list2=data_list2,
        key2_placeholder="{film_key}",
        value2_placeholder="{film_ar}",
        text_after="",
        text_before="",
        other_formatted_data=other_formatted_data,
    )

    double_bot.other_bot.update_put_label_last(put_label_last)
    bot = format_multi_data(
        formatted_data=formatted_data,
        data_list=Nat_women,
        key_placeholder="{nat_en}",
        value_placeholder="{nat_ar}",
        data_list2=data_list2,
        key2_placeholder="{film_key}",
        value2_placeholder="{film_ar}",
        text_after="",
        text_before="",
        other_formatted_data=other_formatted_data,
    )
    return double_bot, bot


def fix_keys(category: str) -> str:
    """Fix known issues in category keys."""
    normalized_text = category.lower().replace("category:", " ").strip()
    fixes = {
        "saudi arabian": "saudiarabian",
        # "animated television": "animated-television",
        "children's animated adventure television": "children's-animated-adventure-television",
        "children's animated superhero": "children's-animated-superhero",
    }
    category = category.lower().strip()

    for old, new in fixes.items():
        category = category.replace(old, new)

    return category


@functools.lru_cache(maxsize=None)
def _get_films_key_tyty_new(text: str) -> str:
    """
    Function to generate a films key based on the country identifier.
    Args:
        text (str): The country identifier string to process.
    Returns:
        str: The resolved label string, or empty string if no match is found.
    """
    normalized_text = fix_keys(text)
    logger.debug(f"<<yellow>> start get_films_key_tyty_new: {normalized_text=}")
    double_bot, bot = _make_bot()

    result = bot.search_all(normalized_text) or double_bot.search_all(normalized_text)
    logger.info_if_or_debug(f"<<yellow>> end get_films_key_tyty_new: {normalized_text=}, {result=}", result)
    return result


@functools.lru_cache(maxsize=None)
def get_films_key_tyty_new(text: str) -> str:
    """
    Function to generate a films key based on the country identifier.
    Args:
        text (str): The country identifier string to process.
    Returns:
        str: The resolved label string, or empty string if no match is found.
    """
    # return ""
    return _get_films_key_tyty_new(text)

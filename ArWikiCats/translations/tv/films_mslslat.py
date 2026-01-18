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
    for tt, tt_lab in TELEVISION_BASE_KEYS_FEMALE.items():
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
        for tt, tt_lab in TELEVISION_BASE_KEYS_FEMALE.items():
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
) -> Tuple[Dict[str, str], Dict[str, str]]:
    """
    Build CAO (Characters, Albums, Organizations, etc.) mappings.

    Returns:
        - films_key_cao: CAO translation mapping
        - films_key_cao2: Extended CAO mapping
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
Films_key_CAO, films_key_cao2 = _build_television_cao(film_keys_for_female)
Films_key_CAO.update(TELEVISION_KEYS)
Films_key_CAO.update(films_key_cao2)

# Build female combination keys
Films_keys_both_new_female = open_json_file("Films_keys_both_new_female_found.json")

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

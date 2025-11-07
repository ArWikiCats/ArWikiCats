"""Additional mixed keys introduced in 2023."""

from __future__ import annotations

from typing import Final

from .key_registry import KeyRegistry

__all__ = ["AFC_KEYS", "afc_keys", "build_new_2023", "new_2023"]


BASE_NEW_2023: Final[dict[str, str]] = {
    "continental indoor soccer league": "الدوري القاري لكرة القدم داخل الصالات",
    "western indoor soccer league": "الدوري الغربي لكرة القدم داخل الصالات",
    "world indoor soccer league": "الدوري العالمي لكرة القدم داخل الصالات",
    "major indoor soccer league": "الدوري الرئيسي لكرة القدم داخل الصالات",
    "eastern indoor soccer league": "الدوري الشرقي لكرة القدم داخل الصالات",
    "game-of-thrones": "صراع العروش",
    "game of thrones": "صراع العروش",
    "statistics": "إحصائيات",
    "records": "سجلات",
    "records and statistics": "سجلات وإحصائيات",
    "literary characters": "شخصيات أدبية",
    "audiovisual introductions": "استحداثات سمعية بصرية",
    "amusement rides": "ألعاب ملاهي",
    "amusement ride introductions": "استحداثات ألعاب ملاهي",
    "amusement rides introductions": "استحداثات ألعاب ملاهي",
    "amusement parks": "متنزهات ملاهي",
    "amusement park": "متنزهات ملاهي",
    "amusement park introductions": "استحداثات متنزهات ملاهي",
    "amusement parks introductions": "استحداثات متنزهات ملاهي",
    "amusement ride attractions": "ألعاب ملاهي جاذبة",
    "amusement rides attractions": "ألعاب ملاهي جاذبة",
    "amusement park attraction introductions": "استحداثات متنزهات ملاهي جاذبة",
    "amusement park attractions": "متنزهات ملاهي جاذبة",
    "amusement attractions": "ملاهي جاذبة",
    "visitor attractions": "معالم سياحية",
    "tourist attractions": "مواقع جذب سياحي",
    "roadside attractions": "مناطق جذب على جانب الطريق",
    "dubailand": "دبي لاند",
    "freethought": "فكر حر",
    "changyi": "تشانجي",
    "cattle": "الماشية",
    "lgbt rights": "حقوق المثليين",
    "capes": "رؤوس",
    "stalls": "الانهيار",
    "privately held companies": "شركات خاصة",
    "charter-airlines": "طيران عارض",
    "charter airlines": "طيران عارض",
    "defunct charter-airlines": "طيران عارض سابق",
    "psychotherapy": "علاج نفسي",
    "healthcare reform": "إصلاح الرعاية الصحية",
    "pseudonymous writers": "كتاب بأسماء مستعارة",
    "1st millennium": "الألفية الأولى",
    "2nd millennium": "الألفية الثانية",
    "3rd millennium": "الألفية الثالثة",
    "4th millennium": "الألفية الرابعة",
    "5th millennium": "الألفية الخامسة",
    "6th millennium": "الألفية السادسة",
    "7th millennium": "الألفية السابعة",
    "8th millennium": "الألفية الثامنة",
    "9th millennium": "الألفية الرابعة",
    "10th millennium": "الألفية الخامسة",
    "1st millennium bc": "الألفية الأولى ق م",
    "2nd millennium bc": "الألفية الثانية ق م",
    "3rd millennium bc": "الألفية الثالثة ق م",
    "4th millennium bc": "الألفية الرابعة ق م",
    "5th millennium bc": "الألفية الخامسة ق م",
    "6th millennium bc": "الألفية السادسة ق م",
    "7th millennium bc": "الألفية السابعة ق م",
    "8th millennium bc": "الألفية الثامنة ق م",
    "9th millennium bc": "الألفية التاسعة ق م",
    "10th millennium bc": "الألفية العاشرة ق م",
    "11th millennium bc": "الألفية 11 ق م",
}


ANTI_KEYS: Final[dict[str, str]] = {
    "anti-war": "مناهضة للحرب",
    "anti-revisionist": "مناهضة للتحريفية",
    "anti-communism": "مناهضة للشيوعية",
    "anti-capitalist": "مناهضة للرأسمالية",
    "anti-islam": "مناهضة للإسلام",
    "anti-zionist": "مناهضة للصهيونية",
    "anti-jewish": "مناهضة لليهودية",
    "anti-monopoly": "مناهضة للإحتكار",
    "anti-masonic": "مناهضة للماسونية",
    "anti-smoking": "مناهضة للتدخين",
    "anti-obesity": "مناهضة للسمنة",
    "anti-vaccination": "مناهضة للتطعيم",
    "anti-poverty": "مناهضة للفقر",
    "anti-communists": "مناهضة للشيوعية",
    "anti-racism": "مناهضة للعنصرية",
    "anti-liquor": "مناهضة للخمور",
    "anti-abortion": "مناهضة للإجهاض",
}


ANTI_SUFFIXES: Final[dict[str, str]] = {
    "company": "شركات",
    "protests": "احتجاجات",
    "organizations": "منظمات",
    "organization": "منظمات",
    "works": "أعمال",
    "movement": "حركات",
    "albums": "ألبومات",
    "books": "كتب",
    "comic book": "كتب قصص مصورة",
    "comic strips": "شرائط مصورة",
    "comic": "قصص مصورة",
    "comics": "قصص مصورة",
    "marvel comics": "مارفال كومكس",
    "dictionaries": "قواميس",
    "encyclopedias": "موسوعات",
    "films": "أفلام",
    "given names": "أسماء شخصية",
    "graphic novels": "روايات مصورة",
    "inscriptionss": "نقوش وكتابات",
    "literary awards": "جوائز أدبية",
    "magazines": "مجلات",
    "manga": "مانغا",
    "mmagazines": "مجلات",
    "music": "موسيقى",
    "names": "أسماء",
    "newspapers": "صحف",
    "novels": "روايات",
    "novellas": "روايات قصيرة",
    "operas": "أوبيرات",
    "plays": "مسرحيات",
    "poems": "قصائد",
    "publications": "منشورات",
    "radio stations": "محطات إذاعية",
    "short stories": "قصص قصيرة",
    "songs": "أغان",
    "surnames": "ألقاب",
    "video games": "ألعاب فيديو",
    "webcomic": "ويب كومكس",
    "webcomics": "ويب كومكس",
    "websites": "مواقع ويب",
}


AFC_KEYS: Final[dict[str, str]] = {
    "afc asian cup qualification": "تصفيات كأس آسيا",
    "fifa world cup qualification (caf)": "تصفيات كأس العالم لكرة القدم (إفريقيا)",
    "fifa world cup qualification (afc)": "تصفيات كأس العالم لكرة القدم (آسيا)",
    "fifa futsal world cup qualification": "تصفيات كأس العالم لكرة الصالات",
    "fifa futsal world cup qualification (afc)": "تصفيات كأس العالم لكرة الصالات (آسيا)",
    "fifa futsal world cup qualification (caf)": "تصفيات كأس العالم لكرة الصالات (إفريقيا)",
    "afc challenge league": "دوري التحدي الآسيوي",
    "association football afc": "كرة القدم في الاتحاد الآسيوي لكرة القدم",
    "association-football afc": "كرة القدم في الاتحاد الآسيوي لكرة القدم",
    "afc elite league": "دوري نخبة ابطال آسيا",
    "afc champions league elite": "دوري نخبة ابطال آسيا",
    "afc champions league two": "دوري أبطال آسيا الثاني",
    "afc cup participants": "مشاركون في كأس الاتحاد الآسيوي لكرة القدم",
    "asian football confederation": "الاتحاد الآسيوي لكرة القدم",
    "afc football": "كرة قدم الاتحاد الآسيوي لكرة القدم",
    "afc cup": "كأس الاتحاد الآسيوي",
    "afc asian cup": "كأس آسيا",
    "afc champions league": "دوري أبطال آسيا",
    "afc asian cup finals": "نهائيات كأس آسيا",
    "afc president's cup": "كأس رئيس الاتحاد الآسيوي",
    "afc solidarity cup": "كأس التضامن الآسيوي",
    "afc women's asian cup": "كأس الأمم الآسيوية لكرة القدم للسيدات",
    "afc u-23 women's asian cup": "كأس آسيا للسيدات تحت 23 سنة",
    "afc u-22 women's asian cup": "كأس آسيا للسيدات تحت 22 سنة",
    "afc u-20 women's asian cup": "كأس آسيا للسيدات تحت 20 سنة",
    "afc u-19 women's asian cup": "كأس آسيا للسيدات تحت 19 سنة",
    "afc u-17 women's asian cup": "كأس آسيا للسيدات تحت 17 سنة",
    "afc u-16 women's asian cup": "كأس آسيا للسيدات تحت 16 سنة",
    "afc women's championship": "بطولة آسيا للسيدات",
    "afc u-22 women's championship": "بطولة آسيا للسيدات تحت 22 سنة",
    "afc u-23 women's championship": "بطولة آسيا للسيدات تحت 23 سنة",
    "afc u-20 women's championship": "بطولة آسيا للسيدات تحت 20 سنة",
    "afc u-19 women's championship": "بطولة آسيا للسيدات تحت 19 سنة",
    "afc u-17 women's championship": "بطولة آسيا للسيدات تحت 17 سنة",
    "afc u-16 women's championship": "بطولة آسيا للسيدات تحت 16 سنة",
    "afc youth championship": "بطولة آسيا للشباب",
    "afc u-23 championship": "بطولة آسيا تحت 23 سنة",
    "afc u-22 championship": "بطولة آسيا للناشئين تحت 22 سنة",
    "afc u-20 championship": "بطولة آسيا للناشئين تحت 20 سنة",
    "afc u-19 championship": "بطولة آسيا للناشئين تحت 19 سنة",
    "afc u-17 championship": "بطولة آسيا للناشئين تحت 17 سنة",
    "afc u-16 championship": "بطولة آسيا للناشئين تحت 16 سنة",
    "afc u-23 asian cup": "كأس آسيا تحت 23 سنة",
    "afc u-22 asian cup": "كأس آسيا للناشئين تحت 22 سنة",
    "afc u-20 asian cup": "كأس آسيا للناشئين تحت 20 سنة",
    "afc u-19 asian cup": "كأس آسيا للناشئين تحت 19 سنة",
    "afc u-17 asian cup": "كأس آسيا للناشئين تحت 17 سنة",
    "afc u-16 asian cup": "كأس آسيا للناشئين تحت 16 سنة",
    "afc futsal championship": "بطولة آسيا لكرة الصالات",
    "afc women's futsal championship": "بطولة آسيا لكرة الصالات للسيدات",
    "afc futsal asian cup": "كأس آسيا لكرة الصالات",
    "afc futsal club championship": "بطولة آسيا لكرة الصالات للأندية",
}

# Provide lowercase alias for legacy imports expecting ``afc_keys``.
afc_keys = AFC_KEYS


def _add_anti_suffixes(registry: KeyRegistry) -> None:
    """Expand ``ANTI_KEYS`` with a rich set of suffix categories."""

    for prefix, prefix_label in ANTI_KEYS.items():
        lowered = prefix.lower()
        for suffix, suffix_label in ANTI_SUFFIXES.items():
            registry.data[f"{lowered} {suffix}"] = f"{suffix_label} {prefix_label}"


def build_new_2023() -> dict[str, str]:
    """Return the mapping that augments the historical ``new_2023`` dictionary."""

    registry = KeyRegistry(dict(BASE_NEW_2023))
    _add_anti_suffixes(registry)
    registry.update_lowercase(AFC_KEYS)
    return registry.data


new_2023: dict[str, str] = build_new_2023()

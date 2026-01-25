"""
Helper utilities and datasets for the mixed key collections.
"""

from ..helps import len_print
from ..others import medical_keys
from ..utils import open_json_file

PARTIES: dict[str, str] = {
    "libertarian party of canada": "الحزب التحرري الكندي",
    "libertarian party-of-canada": "الحزب التحرري الكندي",
    "green party-of-quebec": "حزب الخضر في كيبك",
    "balochistan national party (awami)": "حزب بلوشستان الوطني (عوامي)",
    "republican party-of armenia": "حزب أرمينيا الجمهوري",
    "republican party of armenia": "حزب أرمينيا الجمهوري",
    "green party of the united states": "حزب الخضر الأمريكي",
    "green party-of the united states": "حزب الخضر الأمريكي",
    "armenian revolutionary federation": "حزب الطاشناق",
    "telugu desam party": "حزب تيلوغو ديسام",
    "tunisian pirate party": "حزب القراصنة التونسي",
    "uk independence party": "حزب استقلال المملكة المتحدة",
    "motherland party (turkey)": "حزب الوطن الأم",
    "national action party (mexico)": "حزب الفعل الوطني (المكسيك)",
    "nationalist movement party": "حزب الحركة القومية",
    "new labour": "حزب العمال الجديد",
    "pakistan peoples party": "حزب الشعب الباكستاني",
    "party for freedom": "حزب من أجل الحرية",
    "party for the animals": "حزب من أجل الحيوانات",
    "party of democratic action": "حزب العمل الديمقراطي (البوسنة)",
    "party of european socialists": "حزب الاشتراكيين الأوروبيين",
    "party of labour of albania": "حزب العمل الألباني",
    "party of regions": "حزب الأقاليم",
    "party-of democratic action": "حزب العمل الديمقراطي (البوسنة)",
    "party-of european socialists": "حزب الاشتراكيين الأوروبيين",
    "party-of labour of albania": "حزب العمل الألباني",
    "party-of regions": "حزب الأقاليم",
    "people's democratic party (nigeria)": "حزب الشعب الديمقراطي (نيجيريا)",
    "people's party (spain)": "حزب الشعب (إسبانيا)",
    "people's party for freedom and democracy": "حزب الشعب من أجل الحرية والديمقراطية",
    "peoples' democratic party (turkey)": "حزب الشعوب الديمقراطي",
    "polish united workers' party": "حزب العمال البولندي الموحد",
    "progress party (norway)": "حزب التقدم (النرويج)",
    "red party (norway)": "حزب الحمر (النرويج)",
    "ruling party": "حزب حاكم",
    "spanish socialist workers' party": "حزب العمال الاشتراكي الإسباني",
    "swedish social democratic party": "حزب العمال الديمقراطي الاشتراكي السويدي",
    "swiss people's party": "حزب الشعب السويسري",
    "ulster unionist party": "حزب ألستر الوحدوي",
    "united development party": "حزب الاتحاد والتنمية",
    "welfare party": "حزب الرفاه",
    "whig party (united states)": "حزب اليمين (الولايات المتحدة)",
    "workers' party of korea": "حزب العمال الكوري",
    "workers' party-of korea": "حزب العمال الكوري",
    "national party of australia": "الحزب الوطني الأسترالي",
    "people's democratic party of afghanistan": "الحزب الديمقراطي الشعبي الأفغاني",
    "social democratic party of switzerland": "الحزب الاشتراكي الديمقراطي السويسري",
    "national party-of australia": "الحزب الوطني الأسترالي",
    "people's democratic party-of afghanistan": "الحزب الديمقراطي الشعبي الأفغاني",
    "social democratic party-of switzerland": "الحزب الاشتراكي الديمقراطي السويسري",
    "national party (south africa)": "الحزب الوطني (جنوب إفريقيا)",
    "national woman's party": "الحزب الوطني للمرأة",
    "new democratic party": "الحزب الديمقراطي الجديد",
    "parti québécois": "الحزب الكيبكي",
    "republican party (united states)": "الحزب الجمهوري (الولايات المتحدة)",
    "revolutionary socialist party (india)": "الحزب الاشتراكي الثوري",
    "scottish national party": "الحزب القومي الإسكتلندي",
    "scottish socialist party": "الحزب الاشتراكي الإسكتلندي",
    "serbian radical party": "الحزب الراديكالي الصربي",
    "shining path": "الحزب الشيوعي في بيرو (الدرب المضيء)",
    "social democratic and labour party": "الحزب الاشتراكي العمالي",
    "socialist left party (norway)": "الحزب الاشتراكي اليساري (النرويج)",
    "the left (germany)": "الحزب اليساري الألماني",
    "united national party": "الحزب الوطني المتحد",
    "federalist party": "الحزب الفيدرالي الأمريكي",
    "socialist party of albania": "الحزب الإشتراكي (ألبانيا)",
    "socialist party-of albania": "الحزب الإشتراكي (ألبانيا)",
    "anti-islam political parties": "أحزاب سياسية معادية للإسلام",
    "anti-zionist political parties": "أحزاب سياسية معادية للصهيونية",
    "youth wings of political parties": "أجنحة شبابية لأحزاب سياسية",
    "far-right political parties": "أحزاب اليمين المتطرف",
    "defunct political parties": "أحزاب سياسية سابقة",
    "pan-africanist political parties": "أحزاب سياسية وحدوية إفريقية",
    "pan africanist political parties": "أحزاب سياسية وحدوية إفريقية",
    "banned political parties": "أحزاب سياسية محظورة",
    "pan-african democratic party": "الحزب الديمقراطي الوحدوي الإفريقي",
}


def build_keys2_mapping() -> dict[str, str]:
    """
    Builds a mapping of English keys to Arabic labels by loading "keys/keys2.json" and merging the module's PARTIES translations.
    
    Returns:
        dict[str, str]: Mapping where keys are English identifiers and values are Arabic labels. Entries from PARTIES override or add to any loaded entries.
    """

    data = open_json_file("keys/keys2.json") or {}
    data.update(PARTIES)

    # for xg, xg_lab in USA_PARTY_DERIVED_KEYS.items(): data[xg.lower()] = xg_lab

    return data


def build_keys2_py_mapping() -> dict[str, str]:
    """Return the mapping previously stored in ``keys2_py``."""

    data = open_json_file("keys/keys2_py.json") or {}
    # data["men"] = "رجال"
    # https://quarry.wmcloud.org/query/100263#
    # (مرشحو|مدربو|صحفيو|مستكشفو|سياسيو|لاعبو|مدربو|مؤرخو|مؤسسو|موظفو|مدربو|مسيرو|خريجو|معلقو|مفوضو|مذيعو|موسيقيو|مغنو|معلمو|طبالو|مدونو|ملحنو|مؤلفو|منتجو|محررو|فنانو|مخرجو|ناشرو|مبتكرو) (في|من)
    others = {
        "producers": "منتجو",
        "editors": "محررو",
        "artists": "فنانو",
        "directors": "مخرجو",
        "publisherspeople": "ناشرو",
        "presenters": "مذيعو",
        "creators": "مبتكرو",
        "musicians": "موسيقيو",
        "singers": "مغنو",
        "educators": "معلمو",
        "bloggers": "مدونو",
        "drummers": "طبالو",
        "authors": "مؤلفو",
        "composers": "ملحنو",
        "broadcasters": "مذيعو",
        "commentators": "معلقو",
        "commissioners": "مفوضو",
    }
    data.update(
        {
            "candidates for": "مرشحو",
            "trainers of": "مدربو",
            "journalists of": "صحفيو",
            "explorers of": "مستكشفو",
            "political people of": "سياسيو",
            "players of": "لاعبو",
            "managers of": "مدربو",
            "historians of": "مؤرخو",
            "founders of": "مؤسسو",
            "employees of": "موظفو",
            "coaches of": "مدربو",
            "investors of": "مسيرو",
            "alumni of": "خريجو",
            "chairmen and investors of": "رؤساء ومسيرو",
        }
    )
    data.update(medical_keys)

    return data


new_2019: dict[str, str] = build_keys2_mapping()
keys2_py: dict[str, str] = build_keys2_py_mapping()

__all__ = [
    "PARTIES",
    "keys2_py",
    "new_2019",
]

len_print.data_len(
    "keys2.py",
    {
        "PARTIES": PARTIES,
        "keys2_py": keys2_py,
        "new_2019": new_2019,
    },
)
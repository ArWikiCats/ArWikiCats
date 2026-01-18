"""Party label helpers."""

from __future__ import annotations

from ...helps import logger
from ...translations_formats import FormatData

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

formatted_data = {
    "{party_key} candidates for member of parliament": "مرشحو {party_label} لعضوية البرلمان",
    "{party_key} candidates for member-of-parliament": "مرشحو {party_label} لعضوية البرلمان",
    "{party_key} candidates": "مرشحو {party_label}",
    "{party_key} leaders": "قادة {party_label}",
    "{party_key} politicians": "سياسيو {party_label}",
    "{party_key} members": "أعضاء {party_label}",
    "{party_key} state governors": "حكام ولايات من {party_label}",
}

_parties_bot = FormatData(
    formatted_data=formatted_data,
    data_list=PARTIES,
    key_placeholder="{party_key}",
    value_placeholder="{party_label}",
)


def get_parties_lab(party: str) -> str:
    """Return the Arabic label for ``party`` using known suffixes.

    Args:
        party: The party name to resolve.

    Returns:
        The resolved Arabic label or an empty string if the suffix is unknown.
    """

    normalized_party = party.strip()
    logger.debug(f"get_parties_lab {party=}")

    # Try FormatData first
    label = _parties_bot.search(normalized_party)
    logger.info(f"get_parties_lab {party=}, {label=}")

    return label


__all__ = ["get_parties_lab"]

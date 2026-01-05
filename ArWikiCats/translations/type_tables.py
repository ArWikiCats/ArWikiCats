from ..helps import len_print
from .sports.olympics_data import olympic_event_translations
from .tv.films_mslslat import television_keys

basedtypeTable = {
    "sports events": "أحداث رياضية",
    "sports-events": "أحداث رياضية",
    "video games": "ألعاب فيديو",
    "politics": "سياسة",
    "installations": "منشآت",
    "fortifications": "تحصينات",
    "finales": "نهايات",
    "festivals": "مهرجانات",
    "establishments": "تأسيسات",
    "elections": "انتخابات",
    "disestablishments": "انحلالات",
    "counties": "مقاطعات",
    "awards": "جوائز",
    "youth sport": "رياضة شبابية",
    "works by": "أعمال بواسطة",
    "warm springs of": "ينابيع دائفة في",
    "uci road world cup": "كأس العالم لسباق الدراجات على الطريق",
    "television series": "مسلسلات تلفزيونية",
    "television seasons": "مواسم تلفزيونية",
    "television news": "أخبار تلفزيونية",
    "miniseries": "مسلسلات قصيرة",
    "television miniseries": "مسلسلات قصيرة تلفزيونية",
    "television films": "أفلام تلفزيونية",
    "television commercials": "إعلانات تجارية تلفزيونية",
    "road cycling": "سباق الدراجات على الطريق",
    "qualification for": "تصفيات مؤهلة إلى",
    "produced": "أنتجت",
    "paralympic competitors for": "منافسون بارالمبيون من",
    "olympic medalists for": "فائزون بميداليات أولمبية من",
    "olympic competitors for": "منافسون أولمبيون من",
    "members of parliament for": "أعضاء البرلمان عن",
    "lists of": "قوائم",
    "interactive fiction": "الخيال التفاعلي",
    "fish described": "أسماك وصفت",
    "events": "أحداث",
    "endings": "نهايات",
    "disasters": "كوارث",
    "deaths by": "وفيات بواسطة",
    "deaths": "وفيات",
    "crimes": "جرائم",
    "conflicts": "نزاعات",
    "characters": "شخصيات",
    "births": "مواليد",
    "beginnings": "بدايات",
    "attacks": "هجمات",
    "architecture": "عمارة",
    "UCI Oceania Tour": "طواف أوقيانوسيا للدراجات",
    "UCI Europe Tour": "طواف أوروبا للدراجات",
    "UCI Asia Tour": "طواف آسيا للدراجات",
    "UCI America Tour": "طواف أمريكا للدراجات",
    "UCI Africa Tour": "طواف إفريقيا للدراجات",
    "Hot springs of": "ينابيع حارة في",
    "FIFA World Cup players": "لاعبو كأس العالم لكرة القدم",
    "FIFA futsal World Cup players": "لاعبو كأس العالم لكرة الصالات",
    "-related timelines": "جداول زمنية متعلقة",
    "-related professional associations": "جمعيات تخصصية متعلقة",
    "-related lists": "قوائم متعلقة",
    "commonwealth games competitors for": "منافسون في ألعاب الكومنولث من",
    "winter olympics competitors for": "منافسون أولمبيون شتويون من",
    "uci women's road world cup": "كأس العالم لسباق الدراجات على الطريق للنساء",
}

debuts_endings_key = [
    "television series",
    "television miniseries",
    "television films",
]

type_Table_no = {
    "cycling race winners": "فائزون في سباق الدراجات",
    "films": "أفلام",
    "short films": "أفلام قصيرة",
    "interactive fiction": "الخيال التفاعلي",
    "american comedy television series": "مسلسلات تلفزيونية أمريكية",
    "american television series": "مسلسلات تلفزيونية أمريكية كوميدية",
    "comedy television series": "مسلسلات تلفزيونية كوميدية",
}

for ff, la_b in television_keys.items():
    type_Table_no[f"{ff} debuts"] = f"{la_b} بدأ عرضها في"
    type_Table_no[f"{ff} revived after cancellation"] = f"{la_b} أعيدت بعد إلغائها"
    type_Table_no[f"{ff} endings"] = f"{la_b} انتهت في"

    if ff.lower() in debuts_endings_key:
        type_Table_no[f"{ff}-debuts"] = f"{la_b} بدأ عرضها في"
        type_Table_no[f"{ff}-endings"] = f"{la_b} انتهت في"

type_table_labels = dict(type_Table_no) | dict(basedtypeTable)

for olmp, olmp_lab in olympic_event_translations.items():
    type_table_labels[f"{olmp} for"] = f"{olmp_lab} من"

type_Table_oo = {
    "prisoners sentenced to life imprisonment by": "سجناء حكم عليهم بالحبس المؤبد من قبل",
    "categories by province of": "تصنيفات حسب المقاطعة في",
    "invasions of": "غزو",
    "invasions by": "غزوات",
    "casualties": "خسائر",
    "prisoners of war held by": "أسرى أعتقلوا من قبل",
    "amnesty international prisoners-of-conscience held by": "سجناء حرية التعبير في",
}

type_table_labels.update(type_Table_oo)

typeTable = {x: {"ar": v} for x, v in type_table_labels.items()}

typeTable.update(
    {
        "sports events": {"ar": "أحداث", "s": "الرياضية"},
        "sports-events": {"ar": "أحداث", "s": "الرياضية"},
    }
)

__all__ = [
    "typeTable",
    "basedtypeTable",
]

len_print.data_len(
    "type_tables.py",
    {
        "typeTable": typeTable,
    },
)

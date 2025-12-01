from ..helps import len_print
from .sports.olympics_data import olympics
from .tv.films_mslslat import television_keys

basedtypeTable = {
    "sports events": {"ar": "أحداث", "s": "الرياضية"},
    "sorts-events": {"ar": "أحداث", "s": "الرياضية"},

    "video games": {"ar": "ألعاب فيديو"},
    "politics": {"ar": "سياسة"},
    "installations": {"ar": "منشآت"},
    "fortifications": {"ar": "تحصينات"},
    "finales": {"ar": "نهايات"},
    "festivals": {"ar": "مهرجانات"},
    "establishments": {"ar": "تأسيسات"},
    "elections": {"ar": "انتخابات"},
    "disestablishments": {"ar": "انحلالات"},
    "counties": {"ar": "مقاطعات"},
    "awards": {"ar": "جوائز"},

    "youth sport": {"ar": "رياضة شبابية"},
    "works by": {"ar": "أعمال بواسطة"},
    "warm springs of": {"ar": "ينابيع دائفة في"},
    "uci road world cup": {"ar": "كأس العالم لسباق الدراجات على الطريق"},
    "television series": {"ar": "مسلسلات تلفزيونية"},
    "television seasons": {"ar": "مواسم تلفزيونية"},
    "television news": {"ar": "أخبار تلفزيونية"},
    "television miniseries": {"ar": "مسلسلات قصيرة"},
    "television films": {"ar": "أفلام تلفزيونية"},
    "television commercials": {"ar": "إعلانات تجارية تلفزيونية"},
    "road cycling": {"ar": "سباق الدراجات على الطريق"},
    "qualification for": {"ar": "تصفيات مؤهلة إلى"},
    "produced": {"ar": "أنتجت"},
    "paralympic competitors for": {"ar": "منافسون بارالمبيون من"},
    "olympic medalists for": {"ar": "فائزون بميداليات أولمبية من"},
    "olympic competitors for": {"ar": "منافسون أولمبيون من"},
    "members of parliament for": {"ar": "أعضاء البرلمان عن"},
    "lists of": {"ar": "قوائم"},
    "interactive fiction": {"ar": "الخيال التفاعلي"},
    "fish described": {"ar": "أسماك وصفت"},
    "events": {"ar": "أحداث"},
    "endings": {"ar": "نهايات"},
    "disasters": {"ar": "كوارث"},
    "deaths by": {"ar": "وفيات بواسطة"},
    "deaths": {"ar": "وفيات"},
    "crimes": {"ar": "جرائم"},
    "conflicts": {"ar": "نزاعات"},
    "characters": {"ar": "شخصيات"},
    "births": {"ar": "مواليد"},
    "beginnings": {"ar": "بدايات"},
    "attacks": {"ar": "هجمات"},
    "architecture": {"ar": "عمارة"},
    "UCI Oceania Tour": {"ar": "طواف أوقيانوسيا للدراجات"},
    "UCI Europe Tour": {"ar": "طواف أوروبا للدراجات"},
    "UCI Asia Tour": {"ar": "طواف آسيا للدراجات"},
    "UCI America Tour": {"ar": "طواف أمريكا للدراجات"},
    "UCI Africa Tour": {"ar": "طواف إفريقيا للدراجات"},
    "Hot springs of": {"ar": "ينابيع حارة في"},
    "FIFA World Cup players": {"ar": "لاعبو كأس العالم لكرة القدم"},
    "FIFA futsal World Cup players": {"ar": "لاعبو كأس العالم لكرة الصالات"},
    "-related timelines": {"ar": "جداول زمنية متعلقة"},
    "-related professional associations": {"ar": "جمعيات تخصصية متعلقة"},
    "-related lists": {"ar": "قوائم متعلقة"},
    "commonwealth games competitors for": {
        "ar": "منافسون في ألعاب الكومنولث من",
    },
    "winter olympics competitors for": {
        "ar": "منافسون في الألعاب الأولمبية الشتوية من",
    },
    "uci women's road world cup": {
        "ar": "كأس العالم لسباق الدراجات على الطريق للنساء",
    },
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

type_table_labels = dict(type_Table_no)

for olmp, olmp_lab in olympics.items():
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
for tt_ype in list(type_Table_oo):
    type_table_labels[tt_ype.lower()] = type_Table_oo[tt_ype]

typeTable = dict(basedtypeTable) | {x: {"ar": v} for x, v in type_table_labels.items()}

__all__ = [
    "typeTable",
]

len_print.data_len(
    "type_tables.py",
    {
        "typeTable": typeTable,
    },
)

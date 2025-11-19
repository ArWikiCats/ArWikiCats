from .tv.films_mslslat import television_keys
from .sports.olympics_data import olympics

basedtypeTable = {
    "youth sport": {"ar": "رياضة شبابية"},
    "works by": {"ar": "أعمال بواسطة"},
    "warm springs of": {"ar": "ينابيع دائفة في"},
    "video games": {"ar": "ألعاب فيديو", "priff": "ألعاب فيديو"},
    "uci road world cup": {"ar": "كأس العالم لسباق الدراجات على الطريق"},
    "television series": {"ar": "مسلسلات تلفزيونية"},
    "television seasons": {"ar": "مواسم تلفزيونية"},
    "television news": {"ar": "أخبار تلفزيونية"},
    "television miniseries": {"ar": "مسلسلات قصيرة"},
    "television films": {"ar": "أفلام تلفزيونية"},
    "television commercials": {"ar": "إعلانات تجارية تلفزيونية"},
    "sports events": {"ar": "أحداث", "s": "الرياضية"},
    "sorts-events": {"ar": "أحداث", "s": "الرياضية"},
    "road cycling": {"ar": "سباق الدراجات على الطريق"},
    "qualification for": {"ar": "تصفيات مؤهلة إلى"},
    "produced": {"ar": "أنتجت"},
    "politics": {"ar": "سياسة", "priff": "سياسة"},
    "paralympic competitors for": {"ar": "منافسون بارالمبيون من"},
    "olympic medalists for": {"ar": "فائزون بميداليات أولمبية من"},
    "olympic competitors for": {"ar": "منافسون أولمبيون من"},
    "members of parliament for": {"ar": "أعضاء البرلمان عن"},
    "lists of": {"ar": "قوائم"},
    "interactive fiction": {"ar": "الخيال التفاعلي"},
    "installations": {"ar": "منشآت", "priff": "منشآت"},
    "fortifications": {"ar": "تحصينات", "priff": "تحصينات"},
    "fish described": {"ar": "أسماك وصفت"},
    "finales": {"ar": "نهايات", "priff": "نهايات"},
    "festivals": {"ar": "مهرجانات", "priff": "مهرجانات"},
    "events": {"ar": "أحداث"},
    "establishments": {"ar": "تأسيسات", "priff": "تأسيسات"},
    "endings": {"ar": "نهايات"},
    "elections": {"ar": "انتخابات", "priff": "انتخابات"},
    "disestablishments": {"ar": "انحلالات", "priff": "انحلالات"},
    "disasters": {"ar": "كوارث"},
    "deaths by": {"ar": "وفيات بواسطة"},
    "deaths": {"ar": "وفيات"},
    "crimes": {"ar": "جرائم"},
    "counties": {"ar": "مقاطعات", "priff": "مقاطعات"},
    "conflicts": {"ar": "نزاعات"},
    "characters": {"ar": "شخصيات"},
    "births": {"ar": "مواليد"},
    "beginnings": {"ar": "بدايات"},
    "awards": {"ar": "جوائز", "priff": "جوائز"},
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
    "civil aviation in": {
        "ar": "الطيران المدني في",
        "priff": "الطيران المدني في",
    },
    "national football team managers": {
        "priff": "مدربو منتخب",
        "s": "الوطني لكرة القدم",
        "ar": "",
    },
    "uci women's road world cup": {
        "ar": "كأس العالم لسباق الدراجات على الطريق للنساء",
    },
    # 'olympic gold medalists for' : {"ar":"حائزون على ميداليات ذهبية أولمبية من"},
    # 'sports ' : {"ar":"ألعاب رياضية", "s":""},
}

typeTable_4 = {
    "interactive fiction": {"ar": "الخيال التفاعلي"},
    "american comedy television series": {"ar": "مسلسلات تلفزيونية أمريكية"},
    "american television series": {"ar": "مسلسلات تلفزيونية أمريكية كوميدية"},
    "comedy television series": {"ar": "مسلسلات تلفزيونية كوميدية"},
}

type_Table_no = {}
type_Table_no["cycling race winners"] = "فائزون في سباق الدراجات"
type_Table_no["films"] = "أفلام"
type_Table_no["short films"] = "أفلام قصيرة"

debuts_endings_key = ["television series", "television miniseries", "television films"]

for ff, la_b in television_keys.items():
    type_Table_no[f"{ff} debuts"] = f"{la_b} بدأ عرضها في"
    type_Table_no[f"{ff} revived after cancellation"] = f"{la_b} أعيدت بعد إلغائها"
    type_Table_no[f"{ff} endings"] = f"{la_b} انتهت في"
    if ff.lower() in debuts_endings_key:
        type_Table_no[f"{ff}-debuts"] = f"{la_b} بدأ عرضها في"
        type_Table_no[f"{ff}-endings"] = f"{la_b} انتهت في"
# ---
for uu, uu_tab in type_Table_no.items():
    if uu_tab:
        typeTable_4[uu] = {"ar": uu_tab}
# ---
typeTable = dict(basedtypeTable)

typeTable.update({x.lower(): v for x, v in typeTable_4.items() if v})

for olmp, olmp_lab in olympics.items():
    typeTable[f"{olmp} for"] = {"ar": f"{olmp_lab} من"}

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
    typeTable[tt_ype.lower()] = {"ar": type_Table_oo[tt_ype]}


__all__ = [
    "typeTable",
]

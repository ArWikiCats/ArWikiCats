#!/usr/bin/python3
"""

"""


import sys

from .json_dir import open_json_file

# ---
# from .by_table import By_table
# ---
# "by painter":"",
# "by order":"",
# "by function":"",
# "by district":"",
# "by province":"حسب المقاطعة",
# "by firing squad":"رمياً بالرصاص",
# "by stabbing":"طعناً",
# "by hanging":"شنقاً",
# "by continent":"حسب القارة",
# "by men's junior or schools national team" : "حسب ",
# "by men's wartime national team" : "",
# "by women's national team":"حسب المنتخب الوطني للنساء",
# "by men's national team":"حسب المنتخب الوطني للرجال",
# "by common content":"",
# "by continent":"حسب القارة",
# "by filmation":"حسب الفيلمية",
# "by order of fresnel lens":"",
# "by period":"حسب العصر",
# "by style":"",
# "by subnational entity":"",
# "by type and year of completion":"حسب الفئة وسنة الانتهاء", #a  الاكتمال
# "by type":"حسب النوع",
# "by wikipedia article importance":"",
# "by wikipedia article quality":"حسب جودة مقالة ويكيبيديا",
# "female rower":"",
# "male rower":"",
# ---
By_table = {}
# ---
By_table = open_json_file("By_table") or {}
# ---
Music_By_table = {
    "by city": "حسب المدينة",
    "by seniority": "حسب الأقدمية",
    "by producer": "حسب المنتج",
    "by software": "حسب البرمجيات",
    "by band": "حسب الفرقة",
    "by medium by nationality": "حسب الوسط حسب الجنسية",
    "by instrument": "حسب الآلة",
    "by instrument, genre and nationality": "حسب الآلة والنوع والجنسية",
    "by genre, nationality and instrument": "حسب النوع والجنسية والآلة",
    "by nationality, genre and instrument": "حسب الجنسية والنوع والآلة",
    "by instrument and nationality": "حسب الآلة والجنسية",
    "by instrument and genre": "حسب الآلة والنوع",
    "by genre and instrument": "حسب النوع والآلة",
    "by nationality and instrument ": "حسب الجنسية والآلة الموسيقية",
    "by century and instrument": "حسب القرن والآلة",
    "by medium": "حسب الوسط",
    "by name": "حسب الإسم",
    "by voice type": "حسب نوع الصوت",
    "by language": "حسب اللغة",
    "by nationality": "حسب الجنسية",
}
# ---
By_table_Q = {  # \u200e #by decade
    "by city": "Q18683478",  # حسب المدينة
    "by country": "Q19360703",  # حسب البلد
    "by continent": "Q19360700",  # حسب القارة
    "by century": "Q24571878",  # حسب القرن
    "by name": "Q24571879",  # حسب الإسم
    "by sea": "Q24571876",  # حسب البحر
    "by shape": "Q24572115",  # حسب الشكل
    "by wikipedia article quality": "Q24575823",  # حسب جودة مقالة ويكيبيديا
    "by year": "Q29053180",  # حسب السنة
    "by language": "Q30432875",  # حسب اللغة
    "by nationality": "Q30905655",  # حسب الجنسية
    "by genre": "Q42903116",  # حسب النوع الفني
    "by subnational entity": "Q19588365",
    "by year of completion": "Q24571882",
    "by heritage register": "Q24571881",
    "by body of water": "Q24571884",
    "by height": "Q24571891",
    "by range": "Q24571895",
    "by order of fresnel lens": "Q24571898",
    "by builder": "Q24571904",
    "by condition": "Q24571908",
    "by material": "Q24572019",
    "by style": "Q24572752",
    "by lake": "Q24572867",
    "by period of time": "Q24572874",
    "by wikipedia article importance": "Q24575841",
    "by topic": "Q37765851",
    "by month": "Q38515061",
}

# ---
# "by men's under-20 national team" : "حسب ",
# "by men's under-21 national team" : "حسب ",
# "by men's under-23 national team" : "حسب ",
# by women's under-17 national team
# "by under-20 national team":"حسب المنتخب الوطني",
for year in [16, 17, 18, 19, 20, 21, 23]:
    # By_table["by under-%d national team" % year] = "المنتخب الوطني تحت %d سنة"  % year
    By_table[f"by under-{year} national team"] = f"حسب المنتخب الوطني تحت {year} سنة"
    By_table[f"by men's under-{year} national team"] = f"حسب المنتخب الوطني للرجال تحت {year} سنة"
    By_table[f"by women's under-{year} national team"] = f"حسب المنتخب الوطني للسيدات تحت {year} سنة"
# ---
by_Only = {by1: By_table[by1] for by1 in By_table}
# ---
key_5_suff1 = {
    "tournament": "مسابقة",
    "singles": "فردي",
    "qualification": "تصفيات",
    "team": "فريق",
    "doubles": "زوجي",
}
# ---
key_2_311 = {
    "girls": "فتيات",
    "mixed": "مختلط",
    "boys": "فتيان",
    "singles": "فردي",
    "womens": "سيدات",
    "ladies": "سيدات",
    "mens": "رجال",
    "men's": "رجال",
    # ---
}
# ---
for start in key_2_311:  # –
    for suff in key_5_suff1:  # –
        ke = f"by year - {start} {suff}"
        lab_ke = f"حسب السنة - {key_5_suff1[suff]} {key_2_311[start]}"
        By_table[ke] = lab_ke
        # By_table[ "by year – %s %s" % (start , suff ) ] = "حسب السنة – %s %s" % (key_5_suff1[suff] , key_2_311[start])
        # printe.output('%s=[%s]' % (ke , lab_ke) )
# ---
Contry_cite_el = {
    "city": "مدينة",
    "date": "تاريخ",
    "country": "بلد",
    "continent": "قارة",
    "location": "موقع",
    "period": "حقبة",
    "time": "وقت",
    "year": "سنة",
    "decade": "عقد",
    "era": "عصر",
    "millennium": "ألفية",
    "century": "قرن",
}
for cc in Contry_cite_el:
    # ---
    By_table[f"by {cc} of shooting location"] = f"حسب {Contry_cite_el[cc]} التصوير"
    By_table[f"by {cc} of developer"] = f"حسب {Contry_cite_el[cc]} التطوير"
    By_table[f"by {cc} of location"] = f"حسب {Contry_cite_el[cc]} الموقع"
    By_table[f"by {cc} of setting"] = f"حسب {Contry_cite_el[cc]} الأحداث"
    By_table[f"by {cc} of disestablishment"] = f"حسب {Contry_cite_el[cc]} الانحلال"
    By_table[f"by {cc} of reestablishment"] = f"حسب {Contry_cite_el[cc]} إعادة التأسيس"
    By_table[f"by {cc} of establishment"] = f"حسب {Contry_cite_el[cc]} التأسيس"
    By_table[f"by {cc} of setting location"] = f"حسب {Contry_cite_el[cc]} موقع الأحداث"
    By_table[f"by {cc} of invention"] = f"حسب {Contry_cite_el[cc]} الاختراع"
    By_table[f"by {cc} of introduction"] = f"حسب {Contry_cite_el[cc]} الاستحداث"
    By_table[f"by {cc} of formal description"] = f"حسب {Contry_cite_el[cc]} الوصف"

    By_table[f"by {cc} of photographing"] = f"حسب {Contry_cite_el[cc]} التصوير"
    By_table[f"by photographing {cc} "] = f"حسب {Contry_cite_el[cc]} التصوير"

    By_table[f"by {cc} of completion"] = f"حسب {Contry_cite_el[cc]} الانتهاء"
    # By_table["by {} of completion".format(cc) ] = "حسب {} الاكتمال".format(Contry_cite_el[cc])

    By_table[f"by {cc} of opening"] = f"حسب {Contry_cite_el[cc]} الافتتاح"
    By_table[f"by opening {cc} "] = f"حسب {Contry_cite_el[cc]} الافتتاح"

# ---
by_and_by = {
    "city": "المدينة",
    "rank": "الرتبة",
    "non-profit organizations": "المؤسسات غير الربحية",
    "non-profit publishers": "ناشرون غير ربحيون",
    "nonprofit organization": "المؤسسات غير الربحية",
    "series": "السلسلة",
    "sport": "الرياضة",
    "importance": "الأهمية",
    "league": "الدوري",
    "quality": "الجودة",
    "industry": "الصناعة",
    "sector": "القطاع",
    "conflict": "النزاع",
    "role": "الدور",
    "issue": "القضية",
    "organizer": "المنظم",
    "history of colleges and universities": "تاريخ الكليات والجامعات",
    "subdivision": "التقسيم",
    "country subdivision": "تقسيم البلد",
    "country subdivisions": "تقسيمات البلد",
    "county": "المقاطعة",
    "region": "المنطقة",
    "territory": "الإقليم",
    "behavior": "السلوك",
    "event": "الحدث",
    "competition": "المنافسة",
    "political orientation": "التوجه السياسي",
    "orientation": "التوجه",
    "branch": "الطائفة",
    "class": "الصنف",
    "prison": "السجن",
    "former religion": "الدين السابق",
    "religion": "الدين",
    "ethnicity": "المجموعة العرقية",
    "country": "البلد",
    "writer": "الكاتب",
    "record label": "شركة التسجيلات",
    "publication": "المؤسسة",
    "team": "الفريق",
    "club": "النادي",
    "government agency": "الوكالة الحكومية",
    "status": "الحالة",
    "condition": "الحالة",
    "bank": "البنك",
    "occupation": "المهنة",
    "magazine": "المجلة",
    "newspaper": "الصحيفة",
    "station": "المحطة",
    "shipbuilding company": "شركة بناء السفن",
    "company": "الشركة",
    "organization": "المنظمة",
    "continent": "القارة",
    "specialty": "التخصص",
    "medium": "الوسط",
    "educational institution": "الهيئة التعليمية",
    "educational establishment": "المؤسسات التعليمية",
    "research organization": "منظمة البحوث",
    "trade union": "النقابات العمالية",
    "professional association": "الجمعيات المهنية",
    "instrument": "الآلة",
    "type": "الفئة",
    "genre": "النوع الفني",
    "nationality": "الجنسية",
    "country-of-residence": "بلد الإقامة",
    "country of residence": "بلد الإقامة",
    "nation": "الموطن",
    "century": "القرن",
    "decade": "العقد",
    "year": "السنة",
    "millennium": "الألفية",
    "state": "الولاية",
    "party": "الحزب",
}
# ---
by_and_by2 = by_and_by
for by in by_and_by:
    by_Only[f"by {by}"] = f"حسب {by_and_by[by]}"
    By_table[f"by {by}"] = f"حسب {by_and_by[by]}"
    # print("{} : {}".format("by {}".format( by) , "حسب {}".format(by_and_by[by]) ))
    for by2 in by_and_by2:
        if by != by2:
            by_by = f"by {by} and {by2}"
            ar_ar = f"حسب {by_and_by[by]} و{by_and_by[by2]}"
            By_table[by_by] = ar_ar
            # print("{} : {}".format(by_by , ar_ar))
            # ---
            by_or = f"by {by} or {by2}"
            ar_or = f"حسب {by_and_by[by]} أو {by_and_by[by2]}"
            By_table[by_or] = ar_or
            # print("{} : {}".format(by_by , ar_ar))
            # ---
            by_by2 = f"by {by} by {by2}"
            ar_ar2 = f"حسب {by_and_by[by]} حسب {by_and_by[by2]}"
            By_table[by_by2] = ar_ar2
# ---
by_and_by_new = {
    "composer": "الملحن",
    "composer nationality": "جنسية الملحن",
    "artist": "الفنان",
    "artist nationality": "جنسية الفنان",
    "manufacturer": "الصانع",
    "manufacturer nationality": "جنسية الصانع",
}
# ---
for by in by_and_by_new:
    By_table[f"by {by}"] = f"حسب {by_and_by_new[by]}"
    By_table[f"by genre and {by}"] = f"حسب النوع الفني و{by_and_by_new[by]}"
# ---
for by, value in Music_By_table.items():  #
    if value:  # and not by.lower() in By_table :
        By_table[by.lower()] = value
# ---
By_table_orginal = By_table
By_orginal2 = {x.replace("by ", "", 1).lower(): By_table_orginal[x].replace("حسب ", "", 1) for x in By_table_orginal}
# ---
"""
from .Sport_key import Sports_Keys_For_Label
for ss in Sports_Keys_For_Label:#
    cd = "by %s team" % ss.lower()
    By_table[cd] = f"حسب فريق {Sports_Keys_For_Label[ss]}"
# ---
from .peoples import People_key
for uh in People_key:#
    By_table[f"by {uh.lower()}"] = f"بواسطة {People_key[uh]}"


def main():
    for k in poo:
        if k not in By_table:
            printe.output('   ,"%s":"%s"' %   (k , ""))
"""
# ---
Lenth1 = {"by_table": sys.getsizeof(By_table)}
# ---
from .helps import len_print

len_print.lenth_pri("by_table.py", Lenth1)
# ---
# if __name__ == "__main__":
# main()
# ---

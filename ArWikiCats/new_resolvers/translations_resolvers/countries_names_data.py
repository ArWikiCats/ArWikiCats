#!/usr/bin/python3
"""

"""
from typing import Dict

# NOTE: formatted_data_en_ar_only used in other resolver
formatted_data_en_ar_only: Dict[str, str] = {
    "early modern history of {en}": "تاريخ {ar} الحديث المبكر",
    "early-modern history of {en}": "تاريخ {ar} الحديث المبكر",
    "modern history of {en}": "تاريخ {ar} الحديث",
    "history of {en}": "تاريخ {ar}",
    "academic staff of university of {en}": "أعضاء هيئة تدريس جامعة {ar}",

    "ministries of the government of {en}": "وزارات حكومة {ar}",
    "government ministers of {en}": "وزراء {ar}",
    "secretaries of {en}": "وزراء {ar}",
    "united states secretaries of state": "وزراء خارجية أمريكيون",
    "state cabinet secretaries of {en}": "أعضاء مجلس وزراء {ar}",

    "{en}": "{ar}",
    "{en} women's international footballers": "لاعبات منتخب {ar} لكرة القدم للسيدات",
    "{en} women's youth international footballers": "لاعبات منتخب {ar} لكرة القدم للشابات",
    "{en} international footballers": "لاعبو منتخب {ar} لكرة القدم",

    "police of {en}": "شرطة {ar}",
    "army of {en}": "جيش {ar}",
    "national congress ({en})": "المؤتمر الوطني ({ar})",
    "national council ({en})": "المجلس الوطني ({ar})",
    "national assembly ({en})": "الجمعية الوطنية ({ar})",

    "senate ({en})": "مجلس الشيوخ ({ar})",
    "{en} general assembly": "جمعية {ar} العامة",
    "parliament of {en}": "برلمان {ar}",
    "accidental deaths from falls in {en}": "وفيات عرضية نتيجة السقوط في {ar}",
    "bodies of water of {en}": "مسطحات مائية في {ar}",
    "national university of {en}": "جامعة {ar} الوطنية",
    "national library of {en}": "مكتبة {ar} الوطنية",
    "{en} afc asian cup squad": "تشكيلات {ar} في كأس آسيا",
    "{en} afc women's asian cup squad": "تشكيلات {ar} في كأس آسيا للسيدات",
    "{en} board members": "أعضاء مجلس {ar}",
    "{en} conflict": "نزاع {ar}",
    "{en} cup": "كأس {ar}",
    "{en} elections": "انتخابات {ar}",
    "{en} executive cabinet": "مجلس وزراء {ar} التنفيذي",
    "{en} fifa futsal world cup squad": "تشكيلات {ar} في كأس العالم لكرة الصالات",
    "{en} fifa world cup squad": "تشكيلات {ar} في كأس العالم",
    "{en} government personnel": "موظفي حكومة {ar}",
    "{en} government": "حكومة {ar}",
    "{en} governorate": "محافظة {ar}",
    "{en} olympics squad": "تشكيلات {ar} في الألعاب الأولمبية",
    "{en} presidents": "رؤساء {ar}",
    "{en} responses": "استجابات {ar}",
    "{en} summer olympics squad": "تشكيلات {ar} في الألعاب الأولمبية الصيفية",
    "{en} summer olympics": " {ar} في الألعاب الأولمبية الصيفية",
    "{en} territorial judges": "قضاة أقاليم {ar}",
    "{en} territorial officials": "مسؤولو أقاليم {ar}",
    "{en} war and conflict": "حروب ونزاعات {ar}",
    "{en} war": "حرب {ar}",
    "{en} winter olympics squad": "تشكيلات {ar} في الألعاب الأولمبية الشتوية",
    "{en} winter olympics": " {ar} في الألعاب الأولمبية الشتوية",
}


# TODO: add data from pop_of_without_in.json
pop_of_without_in_data = {
    "university of {en}": "جامعة {ar}",
    "presidents of {en}": "رؤساء {ar}",
}
formatted_data_en_ar_only.update(pop_of_without_in_data)

main_data = {
    "{en} amateur international footballers": "لاعبو منتخب {ar} لكرة القدم للهواة",
    "{en} amateur international soccer players": "لاعبو منتخب {ar} لكرة القدم للهواة",
    "{en} amateur international soccer playerss": "لاعبو منتخب {ar} لكرة القدم للهواة",
    "{en} international footballers": "لاعبو منتخب {ar} لكرة القدم",
    "{en} international rally": "رالي {ar} الدولي",
    "{en} international rules football team": "منتخب {ar} لكرة القدم الدولية",
    "{en} international soccer players": "لاعبو منتخب {ar} لكرة القدم",
    "{en} international soccer playerss": "لاعبو منتخب {ar} لكرة القدم",
    "{en} men's a' international footballers": "لاعبو منتخب {ar} لكرة القدم للرجال للمحليين",
    "{en} men's a' international soccer players": "لاعبو منتخب {ar} لكرة القدم للرجال للمحليين",
    "{en} men's a' international soccer playerss": "لاعبو منتخب {ar} لكرة القدم للرجال للمحليين",
    "{en} men's b international footballers": "لاعبو منتخب {ar} لكرة القدم الرديف للرجال",
    "{en} men's b international soccer players": "لاعبو منتخب {ar} لكرة القدم الرديف للرجال",
    "{en} men's b international soccer playerss": "لاعبو منتخب {ar} لكرة القدم الرديف للرجال",
    "{en} men's international footballers": "لاعبو منتخب {ar} لكرة القدم للرجال",
    "{en} men's international soccer players": "لاعبو منتخب {ar} لكرة القدم للرجال",
    "{en} men's international soccer playerss": "لاعبو منتخب {ar} لكرة القدم للرجال",
    "{en} men's youth international footballers": "لاعبو منتخب {ar} لكرة القدم للشباب",
    "{en} men's youth international soccer players": "لاعبو منتخب {ar} لكرة القدم للشباب",
    "{en} men's youth international soccer playerss": "لاعبو منتخب {ar} لكرة القدم للشباب",
    "{en} national football team managers": "مدربو منتخب {ar} لكرة القدم",
    "{en} national team": "منتخبات {ar} الوطنية",
    "{en} national teams": "منتخبات {ar} الوطنية",
    "{en} rally championship": "بطولة {ar} للراليات",
    "{en} sports templates": "قوالب {ar} الرياضية",
    "{en} women's international footballers": "لاعبات منتخب {ar} لكرة القدم للسيدات",
    "{en} women's international soccer players": "لاعبات منتخب {ar} لكرة القدم للسيدات",
    "{en} women's international soccer playerss": "لاعبات منتخب {ar} لكرة القدم للسيدات",
    "{en} women's youth international footballers": "لاعبات منتخب {ar} لكرة القدم للشابات",
    "{en} women's youth international soccer players": "لاعبات منتخب {ar} لكرة القدم للشابات",
    "{en} women's youth international soccer playerss": "لاعبات منتخب {ar} لكرة القدم للشابات",
    "{en} youth international footballers": "لاعبو منتخب {ar} لكرة القدم للشباب",
    "{en} youth international soccer players": "لاعبو منتخب {ar} لكرة القدم للشباب",
    "{en} youth international soccer playerss": "لاعبو منتخب {ar} لكرة القدم للشباب",
}

formatted_data_en_ar_only.update(main_data)

formatted_data_en_ar_only.update({
    x.replace("secretaries of", "secretaries-of"): y
    for x, y in formatted_data_en_ar_only.items()
    if "secretaries of" in x
})

__all__ = [
    "formatted_data_en_ar_only",
]

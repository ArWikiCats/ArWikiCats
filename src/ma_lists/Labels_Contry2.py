#!/usr/bin/python3
"""

python3 core8/pwb.py make/lists/Labels_Contry2

"""

import sys
from pathlib import Path
import json

# ---
Dir2 = Path(__file__).parent
# ---
P17_PP = {}
with open(f"{Dir2}/jsons/P17_PP.json", "r", encoding="utf-8") as f:
    P17_PP = json.load(f)
# ---
New_Keys = {}
with open(f"{Dir2}/jsons/New_Keys.json", "r", encoding="utf-8") as f:
    New_Keys = json.load(f)
# ---
Cantons = {
    "aarga": "أرجاو",
    "aargau": "أرجاو",
    "appenzell ausserrhoden": "أبينزيل أوسيرهودن",
    "appenzell innerrhoden": "أبينزيل إينرهودن",
    "basel-landschaft": "ريف بازل",
    "basel-land": "ريف بازل",
    "basel-stadt": "مدينة بازل",
    "bern": "برن",
    "fribourg": "فريبورغ",
    "geneva": "جنيف",
    "glarus": "غلاروس",
    "graubünden": "غراوبوندن",
    "grisons": "غراوبوندن",
    "jura": "جورا",
    "lucerne": "لوسيرن",
    "neuchâtel": "نيوشاتل",
    "nidwalden": "نيدفالدن",
    "obwalden": "أوبفالدن",
    "schaffhausen": "شافهوزن",
    "schwyz": "شفيتس",
    "solothurn": "سولوتورن",
    "st. gallen": "سانت غالن",
    "thurga": "تورغاو",
    "thurgau": "تورغاو",
    "ticino": "تيسينو",
    "uri": "أوري",
    "valais": "فاليز",
    "vaud": "فود",
    "zug": "تسوغ",
    "zürich": "زيورخ",
}
# ---
P17_PP.update({k.lower(): v for k, v in Cantons.items()})
# ---
for canton, value in Cantons.items():
    P17_PP[f"canton-of {canton.lower()}"] = f"كانتون {value}"
# ---
P17_PP.update({k.lower(): v for k, v in New_Keys.items()})
# ---
OIO_KK = {
    # ---
    "quintana roo": "ولاية كينتانا رو",
    "tamaulipas": "ولاية تاماوليباس",
    "campeche": "ولاية كامبيتشي",
    "helmand": "ولاية هلمند",
    "nuristan": "ولاية نورستان",
    "badghis": "ولاية بادغيس",
    "badakhshan": "ولاية بدخشان",
    "kapisa": "ولاية كابيسا",
    "baghlan": "ولاية بغلان",
    "daykundi": "ولاية دايكندي",
    "kandahar": "ولاية قندهار",
    "bamyan": "ولاية باميان",
    "nangarhar": "ولاية ننكرهار",
    "aklan": "ولاية أكلان",
    "zacatecas": "ولاية زاكاتيكاس",
    "zabul": "ولاية زابل",
    "balkh": "ولاية بلخ",
    "tlaxcala": "ولاية تلاكسكالا",
    "sinaloa": "ولاية سينالوا",
    # ---
    "nam định": "محافظة نام دنه",
    "malampa": "محافظة مالامبا",
    "đắk lắk": "محافظة داك لاك",
    "lâm đồng": "محافظة لام دونغ",
    "điện biên": "محافظة دين بين",
    # ---
    "northern province": "المحافظة الشمالية (زامبيا)",
    "central java province": "جاوة الوسطى",
    "south hwanghae province": "جنوب مقاطعة هوانغاي",
    "north sumatra province": "سومطرة الشمالية",
    "sancti spíritus province": "سانكتي سبيريتوس",
    "formosa province": "فورموسا",
    "orientale province": "أوريونتال",
    "western province": "المحافظة الغربية (زامبيا)",
    "papua province": "بابوا",
    "jambi province": "جمبي",
    "east nusa tenggara province": "نوسا تنقارا الشرقية",
    "southeast sulawesi province": "سولاوسي الجنوبية الشرقية",
    "chagang province": "تشاغانغ",
    "gorontalo province": "غورونتالو",
    "riau province": "رياو",
    "chaco province": "شاكو",
    "jujuy province": "خوخوي",
    "holguín province": "هولغوين",
    "north maluku province": "مالوكو الشمالية",
    "central province": "المحافظة الوسطى (زامبيا)",
    "central sulawesi province": "سولاوسي الوسطى",
    "southern province": "المحافظة الجنوبية (زامبيا)",
    "west papua province": "بابوا الغربية",
    "copperbelt province": "كوبربيلت",
    "granma province": "غرانما",
    "cienfuegos province": "سينفويغوس",
    "santiago de cuba province": "سانتياغو دي كوبا",
    "salavan province": "سالافان",
    "équateur province": "إكواتور",
    "entre ríos province": "إنتري ريوس",
    "north pyongan province": "بيونغان الشمالية",
    "west java province": "جاوة الغربية",
    "eastern province": "المحافظة الشرقية (زامبيا)",
    "north hwanghae province": "هوانغهاي الشمالية",
    "northwestern province": "المحافظة الشمالية الغربية (زامبيا)",
    "córdoba province": "كوردوبا",
    "matanzas": "ماتنزاس",
    "matanzas province": "مقاطعة ماتنزاس",
    "north sulawesi province": "سولاوسي الشمالية",
    # ---
    "osh region": "أوش أوبلاستي",
    "puno region": "بونو",
    "flemish region": "الإقليم الفلامندي",
    "zanzibar urban/west region": "زنجبار الحضرية / المقاطعة الغربية",
    "talas region": "طلاس أوبلاستي",
    "tansift region": "جهة تانسيفت",
    "central region": "الجهة الوسطى",
    "northwestern region": "الجهة الشمالية الغربية",
    "cajamarca region": "كاخاماركا",
    # ---
    "sacatepéquez department": "ساكاتيبيكيز",
    "escuintla department": "إسكوينتلا",
    # ---
    "prevalje municipality": "بريفالجه",
    "moravče municipality": "مورافسكه (مورافسكه)",
    "vraneštica municipality": "فرانيستيكا (كيسيفو)",
    "vasilevo municipality": "فاسيليفو",
    "šentjernej municipality": "شينتيرني",
    # ---
}
# ---
P17_PP.update({k.lower(): v for k, v in OIO_KK.items()})
# ---
Kos_en = [
    " province",
    " district",
    " state",
    " region",
    " division",
    " county",
    " department",
    " municipality",
    " governorate",
    " voivodeship",
]
Kos_ar = [
    "ولاية ",
    "الشعبة ",
    "شعبة ",
    "القسم ",
    "قسم ",
    "منطقة ",
    "محافظة ",
    "مقاطعة ",
    "إدارة ",
    "بلدية ",
    "إقليم ",
    "اقليم ",
]
# ---
New_Way_adding_Citeis = 0
# ---
for cc, lab in New_Keys.items():
    TOI = True
    cc2 = cc.lower()
    for en_k in Kos_en:
        for ar_k in Kos_ar:
            if TOI and cc2.endswith(en_k) and lab.startswith(ar_k):
                TOI = False
                # ---
                cc3 = cc2[: -len(en_k)]
                lab_2 = lab[len(ar_k) :]
                # ---
                P17_PP[cc3] = lab_2
                New_Way_adding_Citeis += 1

# ---
# ,"mountain" : "ماونتين"
Provincess = {
    "antananarivo": "فيانارانتسوا",
    "antsiranana": "أنتسيرانانا",
    "artemisa": "أرتيميسا",
    "bandundu": "بانداندو",
    "banten": "بنتن",
    "bas-congo": "الكونغو الوسطى",
    "bengkulu": "بنغكولو",
    "bengo": "بنغو",
    "benguela": "بنغيلا",
    "bié": "بيي",
    "buenos aires": "بوينس آيرس",
    "cabinda": "كابيندا",
    "camagüey": "كاماغوي",
    "cuando cubango": "كواندو كوبانغو",
    "cuanza norte": "كوانزا نورت",
    "cunene": "كونيني",
    "fianarantsoa": "فيانارانتسوا",
    "guantánamo": "غوانتانامو",
    "huambo": "هوامبو",
    "kangwon": "كانغوون",
    "katanga": "كاتانغا",
    "lampung": "لامبونغ",
    "las tunas": "لاس توناس",
    "luanda": "لواندا",
    "lunda norte": "لوندا نورتي",
    "lunda sul": "لوندا سول",
    "lusaka": "لوساكا",
    "mahajanga": "ماهاجانجا",
    "malanje": "مالانجي",
    "maluku": "مالوكو",
    "moxico": "موكسيكو",
    "namibe": "ناميبي",
    "ogooué-lolo": "أوغووي-لولو",
    "ogooué-maritime": "أوغووي - البحرية",
    "ryanggang": "ريانغانغ",
    "south pyongan": "بيونغان الجنوبية",
    "toamasina": "تواماسينا",
    "toliara": "توليارا",
    "uíge": "أوجي",
    "woleu-ntem": "وليو-نتم",
    "zaire": "زائير",
}
# ---
for city, city_lab in Provincess.items():
    city2 = city.lower()
    if city_lab:
        P17_PP[city2] = city_lab
        P17_PP[f"{city2} province"] = f"مقاطعة {city_lab}"
        P17_PP[f"{city2} (province)"] = f"مقاطعة {city_lab}"
# ---
Lenth1 = {
    "New_Keys": sys.getsizeof(New_Keys),
    "P17_PP": sys.getsizeof(P17_PP),
    "New_Way_adding_Citeis": New_Way_adding_Citeis,
}
# ---
from .helps import len_print

len_print.lenth_pri("Labels_Contry2.py", Lenth1, Max=21)
# ---
# del New_Keys

"""


"""

import sys
import copy

from ..utils.json_dir import open_json_file

from .us_counties import Counties
from ..others.tax_table import Taxons_table
from ...helps import len_print
from ..companies import New_Company
from ..mixed.all_keys5 import pop_final_5
from ..mixed.all_keys2 import pf_keys2
from .india import Main_Table
from .india_2 import India_Main_Table, Main_Table_2
from .Cities import N_cit_ies_s, tabe_lab_yy2
from .Labels_Contry2 import P17_PP


P17_2_final_ll = {}
# ---
P17_2_final_ll = open_json_file("P17_2_final_ll") or {}
# ---
opop = {}
# ---
opop = open_json_file("opop") or {}
# ---
Jaban_cities = {
    "gokishichidō": "",
    "saitama": "سايتاما",
    "tohoku": "توهوكو",
    "shikoku": "شيكوكو",
    "kyushu": "كيوشو",
    "kantō": "كانتو",
    "kansai": "كانساي",
    "hokkaido": "هوكايدو",
    "hokuriku": "هوكوريكو",
    "chūgoku": "تشوغوكو",
    "toyama": "توياما",
    "tokushima": "توكوشيما",
    "chiba": "تشيبا",
    "tottori": "توتوري",
    "tochigi": "توتشيغي",
    "iwate": "إيواته",
    "ibaraki": "إيباراكي",
    "ishikawa": "إيشيكاوا",
    "ōsaka": "أوساكا",
    "okayama": "أوكاياما",
    "ehime": "إهيمه",
    "akita": "أكيتا",
    "aomori": "آوموري",
    "aichi": "آيتشي",
    "ōita": "أويتا",
    "okinawa": "أوكيناوا",
    "saga": "ساغا",
    "shimane": "شيمانه",
    "shiga": "شيغا",
    "shizuoka": "شيزوكا",
    "kanagawa": "كاناغاوا",
    "kagoshima": "كاغوشيما",
    "kagawa": "كاغاوا",
    "fukui": "فوكوي",
    "fukuoka": "فوكوكا",
    "fukushima": "فوكوشيما",
    "gifu": "غيفو",
    "gunma": "غونما",
    "kōchi": "كوتشي",
    "kumamoto": "كوماموتو",
    "kyōto": "كيوتو",
    "nagano": "ناغانو",
    "nagasaki": "ناغاساكي",
    "nara": "نارا",
    "mie": "ميه",
    "miyagi": "مياغي",
    "miyazaki": "ميازاكي",
    "yamanashi": "ياماناشي",
    "yamaguchi": "ياماغوتشي",
    "yamagata": "ياماغاتا",
    "wakayama": "واكاياما",
    "hyōgo": "هيوغو",
    "hiroshima prefecture": "عمالة هيروشيما",
    "niigata": "نييغاتا",
    "hokkaidō": "هوكايدو",
}

Turky = {
    "adana": "أضنة",
    "adıyaman": "أديامان",
    "afyonkarahisar": "أفيون قره حصار",
    "ağrı": "أغري",
    "aksaray": "آق سراي",
    "amasya": "أماصيا",
    "ankara": "أنقرة",
    "antalya": "أنطاليا",
    "ardahan": "أردهان",
    "artvin": "أرتوين",
    "aydın": "أيدين",
    "balıkesir": "بالق أسير",
    "bartın": "بارتين",
    "batman": "بطمان",
    "bayburt": "بايبورت",
    "bilecik": "بيله جك",
    "bingöl": "بينكل",
    "bitlis": "بتليس",
    "bolu": "بولو",
    "burdur": "بوردور",
    "bursa": "بورصة",
    "çanakkale": "جاناكالي",
    "çankırı": "جانقري",
    "çorum": "جوروم",
    "denizli": "دنيزلي",
    "diyarbakır": "دياربكر",
    "düzce": "دوزجه",
    "edirne": "أدرنة",
    "elazığ": "إلازيغ",
    "erzincan": "أرزينجان",
    "erzurum": "أرضروم",
    "eskişehir": "إسكيشهر",
    "gaziantep": "عنتاب",
    "giresun": "غيرسون",
    "gümüşhane": "كوموش خانة",
    "hakkâri": "حكاري",
    "hatay": "هاتاي",
    "iğdır": "اغدير",
    "isparta": "إسبرطة",
    "istanbul": "إسطنبول",
    "izmir": "إزمير",
    "kahramanmaraş": "قهرمان مرعش",
    "karabük": "كارابوك",
    "karaman": "كارامان",
    "kars": "كارس",
    "kastamonu": "قسطموني",
    "kayseri": "قيصري",
    "kilis": "كلس",
    "kırıkkale": "قيريقكالي",
    "kırklareli": "قرقلر ايلي",
    "kırşehir": "قرشهر",
    "kocaeli": "قوجه ايلي",
    "konya": "قونية",
    "kütahya": "كوتاهية",
    "malatya": "ملطية",
    "manisa": "مانيسا",
    "mardin": "ماردين",
    "mersin": "مرسين",
    "muğla": "موغلا",
    "muş": "موش",
    "nevşehir": "نوشهر",
    "niğde": "نيدا",
    "ordu": "أردو",
    "osmaniye": "عثمانية",
    "rize": "ريزه",
    "sakarya": "صقاريا",
    "samsun": "سامسون",
    "şanlıurfa": "شانلي أورفة",
    "siirt": "سعرد",
    "sinop": "سينوب",
    "sivas": "سيواس",
    "şırnak": "شرناق",
    "tekirdağ": "تكيرداغ",
    "tokat": "توقات",
    "trabzon": "طرابزون",
    "tunceli": "تونجلي",
    "uşak": "أوشاك",
    "van": "وان",
    "yalova": "يالوفا",
    "yozgat": "يوزغات",
    "zonguldak": "زانغولداك",
}

pop_final_Without_Years = {}
P17_final_ll = {}
New_P17_Finall = {city1.lower(): N_cit_ies_s[city1] for city1 in N_cit_ies_s if N_cit_ies_s[city1] != ""}
# ---
# ---
# 402.55859375 before del
# 402.42578125 after del
# ---
for city, lal in Jaban_cities.items():
    city2 = city.lower()
    if lal:
        New_P17_Finall[city2] = lal
        New_P17_Finall[f"{city2} Prefecture"] = f"محافظة {lal}"
        New_P17_Finall[f"{city2} region"] = f"منطقة {lal}"

frf = []
for xa in P17_2_final_ll:
    if P17_2_final_ll[xa]:
        New_P17_Finall[xa.lower()] = P17_2_final_ll[xa]

for xa in opop:
    if opop[xa]:
        New_P17_Finall[xa.lower()] = opop[xa]

for xa in P17_PP:
    if P17_PP[xa]:
        New_P17_Finall[xa.lower()] = P17_PP[xa]

for ccc, ccc_lab in Main_Table.items():
    New_P17_Finall[ccc.lower()] = ccc_lab

for ccc, ccc_lab in Main_Table_2.items():
    New_P17_Finall[ccc.lower()] = ccc_lab

Main_Table_tr = {}
Turky_Province = {}

for dyd in Turky:
    New_P17_Finall[dyd.lower()] = Turky[dyd]
    New_P17_Finall[f"{dyd.lower()} Province"] = f"محافظة {Turky[dyd]}"
    Turky_Province[f"{dyd.lower()} Province"] = f"محافظة {Turky[dyd]}"
    New_P17_Finall[f"districts of {dyd.lower()} Province"] = f"أقضية محافظة {Turky[dyd]}"

for indi in India_Main_Table:
    New_P17_Finall[indi.lower()] = India_Main_Table[indi]

for vvvv in tabe_lab_yy2:
    New_P17_Finall[vvvv.lower()] = tabe_lab_yy2[vvvv]

for contry in pf_keys2:
    if pf_keys2[contry]:
        New_P17_Finall[contry.lower()] = pf_keys2[contry]

for p_o_5 in New_Company:
    if p_o_5.lower() not in pf_keys2 and New_Company[p_o_5]:
        New_P17_Finall[p_o_5.lower()] = New_Company[p_o_5]

New_P17_Finall["indycar"] = "أندي كار"
New_P17_Finall["indiana"] = "إنديانا"
New_P17_Finall["motorsport"] = "رياضة محركات"
New_P17_Finall["indianapolis"] = "إنديانابوليس"
New_P17_Finall["sports in indiana"] = "الرياضة في إنديانا"
New_P17_Finall["igbo"] = "إغبو"

for vg in Counties:
    if Counties[vg]:
        New_P17_Finall[vg.lower()] = Counties[vg]

the_keys = 0

for ase, z in copy.deepcopy(New_P17_Finall).items():
    if z:
        ase3 = ase.lower()

        if ase.startswith("the "):
            the_keys += 1
            ase33 = ase3[len("the ") :].strip()
            New_P17_Finall[ase33] = z

for ta2 in Taxons_table:
    if ta2.lower() not in New_P17_Finall and Taxons_table[ta2]:
        New_P17_Finall[ta2.lower()] = Taxons_table[ta2]

for po_5, poll in pop_final_5.items():
    if poll:
        if po_5.lower() not in New_P17_Finall:
            New_P17_Finall[po_5.lower()] = poll

P17_fdd = {}

Lentha = {
    "New_P17_Finall": sys.getsizeof(New_P17_Finall),
    "opop": sys.getsizeof(opop),
    "the_keys": the_keys,
}

len_print.lenth_pri("Labels_Contry.py", Lentha)

del Counties
del tabe_lab_yy2
del P17_2_final_ll
del N_cit_ies_s
del opop
del Main_Table
del P17_PP

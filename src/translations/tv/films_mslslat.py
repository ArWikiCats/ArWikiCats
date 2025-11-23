#!/usr/bin/python3
"""
new pages from file

python3 core8/pwb.py update/update

SELECT DISTINCT (CONCAT("\"", ?en, "\"") AS ?ss) (CONCAT(":") AS ?ss2) (CONCAT("  \"", ?ar, "\",") AS ?ss3) WHERE {
  ?item (wdt:P31/(wdt:P279*)) wd:Q201658;
    wdt:P910 ?cat.
  ?cat rdfs:label ?en.
  FILTER((LANG(?en)) = "en")
  ?cat rdfs:label ?ar.
  FILTER((LANG(?ar)) = "ar")
  OPTIONAL {
    ?item rdfs:label ?itemaa.
    FILTER((LANG(?itemaa)) = "ar")
  }
  OPTIONAL {
    ?cat rdfs:label ?catar.
    FILTER((LANG(?catar)) = "ar")
  }
}
"""

from ...helps import len_print
from ..utils.json_dir import open_json_file

Films_keys_both_new = {}
# ---
Films_keys_male_female = open_json_file("media/Films_keys_male_female.json") or {}
# ---
television_keys = open_json_file("media/television_keys.json") or {}
Films_key_O_multi = open_json_file("media/Films_key_O_multi.json") or {}
Films_key_For_nat = open_json_file("media/Films_key_For_nat.json") or {}
# ---
films_mslslat_tab = {}
Films_key_For_Jobs = {}
# ---
Films_key_333 = {}
# ---
Films_key_CAO = {}
Films_key_man = {}
# ---
Films_TT = {}
# ---
Films_key_multi = {}
Films_key_both = {}
# ---
Films_Key_for_mat2 = {
    "television-series debuts": "مسلسلات تلفزيونية {} بدأ عرضها في",
    "television-series endings": "مسلسلات تلفزيونية {} انتهت في",
    "web series-debuts": "مسلسلات ويب {} بدأ عرضها في",
    "web series debuts": "مسلسلات ويب {} بدأ عرضها في",
    "television series-debuts": "مسلسلات تلفزيونية {} بدأ عرضها في",
    "television series debuts": "مسلسلات تلفزيونية {} بدأ عرضها في",
    "television series endings": "مسلسلات تلفزيونية {} انتهت في",
}
# ---
film_key_women_2 = {
    "video games": "ألعاب فيديو",
    "soap opera": "مسلسلات طويلة",
    "television characters": "شخصيات تلفزيونية",
    "television programs": "برامج تلفزيونية",
    "television programmes": "برامج تلفزيونية",
    "television programme": "برامج تلفزيونية",
    "web series": "مسلسلات ويب",
    "television series": "مسلسلات تلفزيونية",
    "film series": "سلاسل أفلام",
    "television episodes": "حلقات تلفزيونية",
    "television news": "أخبار تلفزيونية",
    "comics": "قصص مصورة",
    "television films": "أفلام تلفزيونية",
    "television miniseries": "مسلسلات قصيرة",
}
# ---
television_keys_female = dict(television_keys)
# ---
for na4, na4_lab in Films_Key_for_mat2.items():
    Films_key_For_nat[na4] = na4_lab
# ---
for xxx, xxx_lab in Films_key_O_multi.items():
    ka2 = xxx.lower()
    Films_key_multi[ka2] = xxx_lab
    Films_key_both[ka2] = xxx_lab
# ---
for xo, ttt in Films_keys_male_female.items():
    Films_key_both[ka2] = ttt
    if ttt["female"]:
        Films_key_333[xo] = ttt["female"]
# ---
if Films_key_both.get("animated"):
    Films_key_both["animation"] = Films_key_both["animated"]
# ---
film_Keys_For_male = {}
film_Keys_For_female = {}
# ---
for x, da in Films_key_both.items():
    if da["male"]:
        Films_key_man[x] = da["male"]
        if "animated" not in x:
            Films_key_man[f"animated {x}"] = f"{da['male']} رسوم متحركة"
        # Films_key_For_Jobs[x] = da["male"]
    if da["male"]:
        film_Keys_For_male[x] = da["male"]
    if da["female"]:
        film_Keys_For_female[x] = da["female"]
# ---
debuts_endings_key = ["television series", "television miniseries", "television films"]
# ---
Films_key2 = film_Keys_For_female
# ---Category:Anime_and_manga_by_genre
Films_Frist = ["low-budget", "christmas", "lgbtq-related", "lgbt-related", "lgbtqrelated", "lgbtrelated", "upcoming"]
# ---
nat_key_f = "{}"
# ---
# إضافة المسلسلات
for tt, tt_lab in film_key_women_2.items():
    # "television-series debuts" : "مسلسلات تلفزيونية {} بدأ عرضها في",
    Films_key_For_nat[tt] = f"%s {nat_key_f}" % tt_lab
    Films_key_For_nat[f"{tt} debuts"] = f"%s {nat_key_f} بدأ عرضها في" % tt_lab
    Films_key_For_nat[f"{tt} endings"] = f"%s {nat_key_f} انتهت في" % tt_lab
    Films_key_For_nat[f"{tt} revived after cancellation"] = f"%s {nat_key_f} أعيدت بعد إلغائها" % tt_lab
    films_mslslat_tab[tt] = tt_lab
    films_mslslat_tab[f"{tt} revived after cancellation"] = f"{tt_lab} أعيدت بعد إلغائها"
    films_mslslat_tab[f"{tt} debuts"] = f"{tt_lab} بدأ عرضها في"
    films_mslslat_tab[f"{tt} endings"] = f"{tt_lab} انتهت في"
    if tt.lower() in debuts_endings_key:
        films_mslslat_tab[f"{tt}-debuts"] = f"{tt_lab} بدأ عرضها في"
        films_mslslat_tab[f"{tt}-endings"] = f"{tt_lab} انتهت في"
        Films_key_For_nat[f"{tt}-debuts"] = f"%s {nat_key_f} بدأ عرضها في" % tt_lab
        Films_key_For_nat[f"{tt}-endings"] = f"%s {nat_key_f} انتهت في" % tt_lab
# ---
Films_key_For_nat["remakes of {} films"] = f"أفلام {nat_key_f} معاد إنتاجها"
# ---
for ff in television_keys:
    la_b = television_keys[ff]
    Films_key_CAO[ff] = la_b
    Films_key_CAO[f"{ff} characters"] = f"شخصيات {la_b}"

    Films_key_CAO[f"{ff} title cards"] = f"بطاقات عنوان {la_b}"
    Films_key_CAO[f"{ff} video covers"] = f"أغلفة فيديو {la_b}"
    Films_key_CAO[f"{ff} posters"] = f"ملصقات {la_b}"
    Films_key_CAO[f"{ff} images"] = f"صور {la_b}"
# ---
for ke, ke_lab in film_Keys_For_female.items():
    for tt, tt_lab in film_key_women_2.items():
        Films_key_For_nat[f"{ke} {tt}"] = f"{tt_lab} {ke_lab} {nat_key_f}"
        Films_key_For_nat[f"{ke} {tt} revived after cancellation"] = f"{tt_lab} {ke_lab} {nat_key_f} أعيدت بعد إلغائها"
        Films_key_For_nat[f"{ke} {tt} debuts"] = f"{tt_lab} {ke_lab} {nat_key_f} بدأ عرضها في"
        Films_key_For_nat[f"{ke} {tt} endings"] = f"{tt_lab} {ke_lab} {nat_key_f} انتهت في"
        films_mslslat_tab[f"{ke} {tt}"] = f"{tt_lab} {ke_lab}"
        films_mslslat_tab[f"{ke} {tt} revived after cancellation"] = f"{tt_lab} {ke_lab} {nat_key_f} أعيدت بعد إلغائها"
        films_mslslat_tab[f"{ke} {tt} debuts"] = f"{tt_lab} {ke_lab} بدأ عرضها في"
        films_mslslat_tab[f"{ke} {tt} endings"] = f"{tt_lab} {ke_lab} انتهت في"
        if tt.lower() in debuts_endings_key:
            films_mslslat_tab[f"{ke} {tt}-debuts"] = f"{tt_lab} {ke_lab} بدأ عرضها في"
            films_mslslat_tab[f"{ke} {tt}-endings"] = f"{tt_lab} {ke_lab} انتهت في"
            Films_key_For_nat[f"{ke} {tt}-debuts"] = f"{tt_lab} {ke_lab} {nat_key_f} بدأ عرضها في"
            Films_key_For_nat[f"{ke} {tt}-endings"] = f"{tt_lab} {ke_lab} {nat_key_f} انتهت في"
        # "television-series endings" : "مسلسلات تلفزيونية {} انتهت في",
# ---
for cd, ff in Films_key_O_multi.items():
    if ff["female"]:
        Films_key_333[cd] = ff["female"]
# ---
ss_Films_key_CAO = 0
third_Films_key_CAO = 0
vfvfv = 0
# ---
for ke, ke_lab in film_Keys_For_female.items():
    Films_key_CAO[f"{ke} anime and manga"] = f"أنمي ومانغا {ke_lab}"
    Films_key_CAO[f"{ke} compilation albums"] = f"ألبومات تجميعية {ke_lab}"
    Films_key_CAO[f"{ke} folk albums"] = f"ألبومات فلكلورية {ke_lab}"
    Films_key_CAO[f"{ke} classical albums"] = f"ألبومات كلاسيكية {ke_lab}"
    Films_key_CAO[f"{ke} comedy albums"] = f"ألبومات كوميدية {ke_lab}"
    Films_key_CAO[f"{ke} mixtape albums"] = f"ألبومات ميكستايب {ke_lab}"
    Films_key_CAO[f"{ke} soundtracks"] = f"موسيقى تصويرية {ke_lab}"
    Films_key_CAO[f"{ke} terminology"] = f"مصطلحات {ke_lab}"
    Films_key_CAO[f"children's {ke}"] = f"أطفال {ke_lab}"
    Films_key_CAO[f"{ke} television series"] = f"مسلسلات تلفزيونية {ke_lab}"
    Films_key_CAO[f"{ke} television episodes"] = f"حلقات تلفزيونية {ke_lab}"
    Films_key_CAO[f"{ke} television programs"] = f"برامج تلفزيونية {ke_lab}"
    Films_key_CAO[f"{ke} television programmes"] = f"برامج تلفزيونية {ke_lab}"
    Films_key_CAO[f"{ke} television programme"] = f"برامج تلفزيونية {ke_lab}"
    Films_key_CAO[f"{ke} web programme"] = f"مسلسلات ويب {ke_lab}"
    Films_key_CAO[f"{ke} groups"] = f"مجموعات {ke_lab}"
    Films_key_CAO[f"{ke} novellas"] = f"روايات قصيرة {ke_lab}"
    Films_key_CAO[f"{ke} novels"] = f"روايات {ke_lab}"
    Films_key_CAO[f"{ke} film remakes"] = f"أفلام {ke_lab} معاد إنتاجها"
    Films_key_For_Jobs[ke] = ke_lab

    F_k = f"{ke} films"
    Films_key_CAO[F_k] = f"أفلام {ke_lab}"
    for fao in television_keys:
        ss_Films_key_CAO += 1
        rr = f"{ke} {fao}"
        Films_key_CAO[rr] = f"{television_keys[fao]} {ke_lab}"
        # printe.output("vv : %s:%s " % (rr , "%s %s" % (television_keys[fao] , ke_lab)) )
    ke_lower = ke.lower()
    tyty = "{tyty}"
    for ke2, ke2_lab in Films_key2.items():
        vfvfv += 1
        ke22 = ke2.lower()
        if ke22 != ke_lower:
            Paop_1 = f"{tyty} %s %s" % (ke_lab, ke2_lab)
            Paop_2 = f"{tyty} %s %s" % (ke2_lab, ke_lab)
            if ke_lower in Films_Frist:
                Paop_1 = f"{tyty} %s %s" % (ke2_lab, ke_lab)
                Paop_2 = Paop_1
                # print(Paop_1)
            elif ke22 in Films_Frist:
                Paop_1 = f"{tyty} %s %s" % (ke_lab, ke2_lab)
                Paop_2 = Paop_1
                # print(Paop_1)
            k1 = f"{ke} {ke2}"
            if k1 not in Films_key_333:
                Films_key_333[k1] = Paop_1
                # print(f"{k1} : {Paop_1}")
            k2 = f"{ke2} {ke}"
            if k2 not in Films_key_333:
                Films_key_333[k2] = Paop_2
                # print(f"{k2} : {Paop_2}")
Films_key_CAO["lgbt-related films"] = "أفلام {} متعلقة بإل جي بي تي"
Films_key_CAO["lgbtrelated films"] = "أفلام {} متعلقة بإل جي بي تي"
Films_key_CAO["lgbtq-related films"] = "أفلام {} متعلقة بإل جي بي تي كيو"
Films_key_CAO["lgbtqrelated films"] = "أفلام {} متعلقة بإل جي بي تي كيو"
# ---
Films_key_CAO_new_format = {}
Films_key_CAO_new_format["lgbtrelated films"] = "أفلام {} متعلقة بإل جي بي تي"
Films_key_CAO_new_format["lgbtqrelated films"] = "أفلام {} متعلقة بإل جي بي تي كيو"
# ---
tabe_2 = dict(Films_keys_male_female)
# ---
for en, tab in Films_keys_male_female.items():
    for en2, tab2 in tabe_2.items():
        if en == en2:
            continue
        new_lab_male = ""
        new_lab_female = ""
        if tab["female"] and tab2["female"]:
            new_lab_female = f"{tab['female']} {tab2['female']}"
        if tab["male"] and tab2["male"]:
            new_lab_male = f"{tab['male']} {tab2['male']}"
        new_key = f"{en} {en2}".lower()
        Films_keys_both_new[new_key] = {"male": new_lab_male, "female": new_lab_female}


len_print.data_len(
    "films_mslslat.py",
    {
        "Films_key_For_nat": Films_key_For_nat,
        "films_mslslat_tab": films_mslslat_tab,
        "third_Films_key_CAO": third_Films_key_CAO,
        "ss_Films_key_CAO": ss_Films_key_CAO,
        "vfvfv": vfvfv,
        "Films_key_333": Films_key_333,
        "Films_TT": Films_TT,
        "Films_key_CAO": Films_key_CAO,
        "Films_keys_both_new": Films_keys_both_new,
    },
)

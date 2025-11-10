#!/usr/bin/python3
"""
new pages from file

python3 core8/pwb.py update/update

SELECT DISTINCT
(concat('  ,"', ?itemen , '"')  as ?ss)
(concat(':')  as ?ss2)
(concat('  "', ?itemaa , '"')  as ?ss3)
WHERE {
  ?item wdt:P31/wdt:P279* wd:Q7275.
  ?item rdfs:label ?itemen filter (lang(?itemen) = "en")
OPTIONAL {?item rdfs:label ?itemaa filter (lang(?itemaa) = "ar")   }
    }
#LIMIT 100
"""
#
import copy
import sys

from ..utils.json_dir import open_json_file

from ...helps import len_print

# ---
Films_keys_both_new = {}
Films_keys_male_female = {}
television_keys = {}
Films_key_O_multi = {}
# ---
# ,"anime":{"male":"أنيمي", "female":"أنيمي", "Q":"Q20650540"}
# ,"slapstick":{"male":"كوميديا تهريجية", "female":"كوميديا تهريجية", "Q":"Q624771"}
# ,"silent":{"male":"صامت", "female":"صامت", "Q":""}
#
# # ,"propaganda":{"male":"بروباغندا", "female":"بروباغندا", "Q":"Q1935609"}
# ,"world cinema":{"male":"سينما عالمية", "female":"سينما عالمية", "Q":"Q1150666"}
# ,"historical":{"male":"تاريخي", "female":"تاريخية", "Q":"Q17013749"}
# ,"independent":{"male":"مستقل", "female":"مستقل", "Q":"Q459290"}
# ,"musical":{"male":"موسيقي", "female":"موسيقي", "Q":"Q842256"}
# ,"narrative":{"male":"سردي", "female":"سردية", "Q":"Q12912091"}
# ,"neo-noir":{"male":"نوار-جديد", "female":"نوار-جديد", "Q":"Q2421031"}
# ,"docudrama":{"male":"دراما وثائقية", "female":"دراما وثائقية", "Q":"Q622370"}
# ,"documentary":{"male":"وثائقي", "female":"وثائقي", "Q":"Q93204"}
# ,"drama":{"male":"دراما", "female":"دراما", "Q":"Q130232"}
# ,"epic":{"male":"ملحمي", "female":"ملحمي", "Q":"Q652256"}
# ,"exploitation":{"male":"سينما الاستغلال", "female":"سينما الاستغلال", "Q":"Q1067324"}
# ,"fantasy":{"male":"فنتازيا", "female":"فنتازيا", "Q":"Q157394"}
# ,"children's":{"male":"عائلي", "female":"عائلي", "Q":"Q2143665"}
# ,"cinéma vérité":{"male":"سينما فيريتيه", "female":"سينما فيريتيه", "Q":"Q1092621"},
# ,"comedy":{"male":"كوميديا", "female":"كوميديا", "Q":"Q157443"}
# ,"cinema novo":{"male":"سينما نوفو", "female":"سينما نوفو", "Q":"Q1092442"}
# ,"prussian":{"male":"بروسي", "female":"بروسي", "Q":"Q1456178"}
# ,"black comedy":{"male":"كوميديا سوداء", "female":"كوميديا سوداء", "Q":"Q5778924"}
# ---
Films_keys_male_female = open_json_file("Films_keys_male_female") or {}
# ---
# "drafts" : " {}",
# "executives" : " {}",
# "fan clubs" : " {}",
# "organizations":"منظمات",
television_keys = open_json_file("television_keys") or {}
# ---
# ,"science fantasy": {"male":"خيال فانتازي", "female":"خيالية فانتازيا", "Q":""}
# ,"comedy-drama": {"male":"كوميديا درامية", "female":"كوميديا درامية", "Q":"Q859369"}
# ---
Films_key_O_multi = open_json_file("Films_key_O_multi") or {}
# ---
Films_key_For_nat = {}
Films_key_For_nat = open_json_file("Films_key_For_nat") or {}
# ---
films_mslslat_tab = {}
Films_key_For_Jobs = {}
# Films_key_For_Jobs_both= {}
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
"""
    SELECT DISTINCT
    (concat('  ,"', ?en , '"')  as ?ss)
    (concat(':')  as ?ss2)
    (concat('  "', ?ar , '"')  as ?ss3)
    WHERE {
    ?item wdt:P31/wdt:P279* wd:Q201658.
    ?item wdt:P910 ?cat.
    ?cat rdfs:label ?en filter (lang(?en) = "en")
    ?cat rdfs:label ?ar filter (lang(?ar) = "ar")
    OPTIONAL {?item rdfs:label ?itemaa filter (lang(?itemaa) = "ar")   }
    OPTIONAL {?cat rdfs:label ?catar filter (lang(?catar) = "ar")   }
        }
    #LIMIT 100

    "gay male pornography" : "إباحية مثلية",
    "erotic thriller" : "إثارة جنسية",
    "crime thriller" : "إثارة وجريمة",
    "police procedurals" : "إجراءات الشرطة",
    "police procedural" : "إجراءات الشرطة",
    "french comedy" : "كوميدية فرنسية",
    "bollywood" : "بوليوود",
    "found footage" : "تسجيلات مكتشفة",
    "stop-motion animated" : "الرسوم المتحركة بتقنية إيقاف الحركة",
    "alternate history" : "تاريخ بديل",
    "courtroom" : "تدور أحداثها في قاعة محكمة",
    "erotic" : "جنسية",
    "about religion" : "دينية",
    "clay animation" : "رسوم متحركة طينية",
    "gothic horror" : "رعب قوطية",
    "surfing" : "ركمجة",
    "vigilante" : "حراسة",
    "prison" : "سجون",
    "mafia comedy" : "مافيا كوميدية",
    "parody" : "محاكاة ساخرة",
    "epic" : "ملحمية",
    "anti-war" : "مناهضة للحرب",
    "yakuza" : "ياكوزا",
    "rape and revenge" : "إغتصاب وإنتقام",
    "crossover fiction" : "خيال متقاطع",
    "weird west" : "غرب أمريكي غريب",
    "mysticism" : "غموضية",
    "tokusatsu" : "توكوساتسو",
    "political fiction" : "خيال سياسي",
    "docudramas" : "دراما وثائقية",
    "drama" : "دراما",
    "psychological horror" : "رعب نفسي",
    "japanese horror" : "رعب ياباني",
    "cyberpunk" : "سايبربانك",
    "cyberpunk" : "سايبربانك",
    "spaghetti western" : "سباغيتي وسترن",
    "silent" : "سينما صامتة",
    "girls with guns" : "فتيات مع أسلحة",
    "educational" : "فلم تعليمي",
    "horror" : "فلم رعب",
    "musical" : "فلم موسيقي",
    "cannibal" : "آكلو لحم البشر",
    "pornographic" : "إباحي",
    "thriller" : "إثارة",
    "exploitation" : "الاستغلال",
    "survival" : "البقاء على قيد الحياة",
    "anthology" : "أنثولوجيا",
    "propaganda" : "بروباغندا",
    "prussian" : "بروسي",
    "superhero" : "بطل خارق",
    "historical" : "تاريخي",
    "experimental  :   "تجريبي",
    "spy" : "تجسس",
    "slasher" : "تقطيع",
    "3d" : "ثلاثي الأبعاد",
    "crime" : "جريمة",
    "criminal comedy" : "جنائي كوميدي",
    "war" : "حربي",
    "action comedy" : "حركة كوميدي",
    "action" : "حركة",
    "speculative fiction" : "خيال تأملي",
    "science fiction action" : "خيال علمي وحركة",
    "science fiction" : "خيال علمي",
    "drama" : "دراما",
    "b-movies" : "درجة ثانية",
    "dystopian" : "ديستوبيا",
    "animated" : "رسوم متحركة",
    "buddy" : "رفقاء",
    "dance" : "رقص",
    "romance" : "رومانسي",
    "sports" : "رياضة",
    "zombie" : "زومبي",
    "samurai" : "ساموراي",
    "heist" : "سرقة",
    "political" : "سياسي",
    "biographical" : "سيرة ذاتية",
    "treasure hunt" : "صيد كنوز",
    "road movies" : "طريق",
    "family movies" : "عائلي",
    "children's" : "عائلي",
    "gangster" : "عصابات",
    "christmas" : "عيد الميلاد",
    "western (genre)" : "غرب أمريكي",
    "mystery" : "غموض",
    "submarine" : "غواصات",
    "fantasy" : "فنتازيا",
    "martial arts" : "فنون قتالية",
    "pirate" : "قراصنة",
    "disaster" : "كوارث",
    "black comedy" : "كوميديا سوداء",
    "comedy" : "كوميديا",
    "kung fu" : "كونغ فو",
    "apocalyptic" : "ما بعد الكارثة",
    "post-apocalyptic" : "ما بعد الكارثة",
    "mafia" : "مافيا",
    "lgbt-related  :   "متعلّق بالمثليين",
    "teen" : "مراهقة",
    "independent" : "مستقل",
    "vampires in   :   "مصاصي دماء",
    "adventure" : "مغامرة",
    "based on works" : "مقتبس",
    "epic" : "ملحمي",
    , noir" : "نوار"
    "hood" : "هود",
    "about animals" : "وثائقي بري",
    "documentary" : "وثائقي",
    "documentary   :   "وثائقي",
    "monster movies" : "وحوش",
    "coming-of-age fiction" : "قصة تقدم في العمر",
    "kaiju" : "كايجو",
    "kaiju" : "كايجو",
    "horror comedy" : "كوميدي رعب",
    "comedy thriller" : "كوميديا إثارة",
    "slapstick" : "كوميديا تهريجية",
    "comedy-drama" : "كوميديا درامية",
    "romantic comedy" : "كوميديا رومانسية",
    "romantic comedy" : "كوميديا رومانسية",
    "melodramas" : "ميلودراما",
    "neo-noir" : "نوار-جديد",
    "satire" : "هجاء",
    "hentai" : "هنتاي",
    "magic realism" : "واقعية سحرية",
    "mockumentary" : "وثائقي كاذب",
"""
# ---
type_Table_no = {}
type_Table_no["cycling race winners"] = "فائزون في سباق الدراجات"
type_Table_no["films"] = "أفلام"
type_Table_no["short films"] = "أفلام قصيرة"
# ---
typeTable_4 = {
    "interactive fiction": {"ar": "الخيال التفاعلي", "Q": ""},
    "american comedy television series": {"ar": "مسلسلات تلفزيونية أمريكية", "Q": ""},
    "american television series": {"ar": "مسلسلات تلفزيونية أمريكية كوميدية", "Q": ""},
    "comedy television series": {"ar": "مسلسلات تلفزيونية كوميدية", "Q": ""},
}
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
# for x2a in typeTable_4:
# Films_TT[x2a] =typeTable_4[x2a]["ar"]
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
television_keys_female = television_keys
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
    # ---
    if da["male"]:
        Films_key_man[x] = da["male"]
        if not x.find("animated"):
            Films_key_man[f"animated {x}"] = f"{da['male']} رسوم متحركة"
        # Films_key_For_Jobs[x] = da["male"]
    # ---
    if da["male"]:
        film_Keys_For_male[x] = da["male"]
    # ---
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
    # ---
    films_mslslat_tab[tt] = tt_lab
    films_mslslat_tab[f"{tt} revived after cancellation"] = f"{tt_lab} أعيدت بعد إلغائها"
    films_mslslat_tab[f"{tt} debuts"] = f"{tt_lab} بدأ عرضها في"
    films_mslslat_tab[f"{tt} endings"] = f"{tt_lab} انتهت في"
    # ---
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
    type_Table_no[f"{ff} debuts"] = f"{la_b} بدأ عرضها في"
    type_Table_no[f"{ff} revived after cancellation"] = f"{la_b} أعيدت بعد إلغائها"
    type_Table_no[f"{ff} endings"] = f"{la_b} انتهت في"
    Films_key_CAO[f"{ff} characters"] = f"شخصيات {la_b}"

    Films_key_CAO[f"{ff} title cards"] = f"بطاقات عنوان {la_b}"
    Films_key_CAO[f"{ff} video covers"] = f"أغلفة فيديو {la_b}"
    Films_key_CAO[f"{ff} posters"] = f"ملصقات {la_b}"
    Films_key_CAO[f"{ff} images"] = f"صور {la_b}"
    # ---
    if ff.lower() in debuts_endings_key:
        type_Table_no[f"{ff}-debuts"] = f"{la_b} بدأ عرضها في"
        type_Table_no[f"{ff}-endings"] = f"{la_b} انتهت في"
# ---
for ke, ke_lab in film_Keys_For_female.items():
    # ---
    for tt, tt_lab in film_key_women_2.items():
        Films_key_For_nat[f"{ke} {tt}"] = f"{tt_lab} {ke_lab} {nat_key_f}"
        Films_key_For_nat[f"{ke} {tt} revived after cancellation"] = f"{tt_lab} {ke_lab} {nat_key_f} أعيدت بعد إلغائها"
        Films_key_For_nat[f"{ke} {tt} debuts"] = f"{tt_lab} {ke_lab} {nat_key_f} بدأ عرضها في"
        Films_key_For_nat[f"{ke} {tt} endings"] = f"{tt_lab} {ke_lab} {nat_key_f} انتهت في"
        # ---
        films_mslslat_tab[f"{ke} {tt}"] = f"{tt_lab} {ke_lab}"
        films_mslslat_tab[f"{ke} {tt} revived after cancellation"] = f"{tt_lab} {ke_lab} {nat_key_f} أعيدت بعد إلغائها"
        films_mslslat_tab[f"{ke} {tt} debuts"] = f"{tt_lab} {ke_lab} بدأ عرضها في"
        films_mslslat_tab[f"{ke} {tt} endings"] = f"{tt_lab} {ke_lab} انتهت في"
        # ---
        if tt.lower() in debuts_endings_key:
            films_mslslat_tab[f"{ke} {tt}-debuts"] = f"{tt_lab} {ke_lab} بدأ عرضها في"
            films_mslslat_tab[f"{ke} {tt}-endings"] = f"{tt_lab} {ke_lab} انتهت في"
            Films_key_For_nat[f"{ke} {tt}-debuts"] = f"{tt_lab} {ke_lab} {nat_key_f} بدأ عرضها في"
            Films_key_For_nat[f"{ke} {tt}-endings"] = f"{tt_lab} {ke_lab} {nat_key_f} انتهت في"
        # ---
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
    # ---
    Films_key_For_Jobs[ke] = ke_lab
    # Films_key_For_Jobs_both[ke] = ke_lab
    F_k = f"{ke} films"
    Films_key_CAO[F_k] = f"أفلام {ke_lab}"
    # ---
    for fao in television_keys:
        ss_Films_key_CAO += 1
        rr = f"{ke} {fao}"
        Films_key_CAO[rr] = f"{television_keys[fao]} {ke_lab}"
        # printe.output("vv : %s:%s " % (rr , "%s %s" % (television_keys[fao] , ke_lab)) )
    # ---
    ke_lower = ke.lower()
    # ---
    tyty = "{tyty}"
    # ---
    for ke2, ke2_lab in Films_key2.items():
        vfvfv += 1
        ke22 = ke2.lower()
        if ke22 != ke_lower:
            # ---
            Paop_1 = f"{tyty} %s %s" % (ke_lab, ke2_lab)
            Paop_2 = f"{tyty} %s %s" % (ke2_lab, ke_lab)
            # ---
            if ke_lower in Films_Frist:
                Paop_1 = f"{tyty} %s %s" % (ke2_lab, ke_lab)
                Paop_2 = Paop_1
                # print(Paop_1)
            # ---
            elif ke22 in Films_Frist:
                Paop_1 = f"{tyty} %s %s" % (ke_lab, ke2_lab)
                Paop_2 = Paop_1
                # print(Paop_1)
            # ---
            k1 = f"{ke} {ke2}"
            if k1 not in Films_key_333:
                Films_key_333[k1] = Paop_1
                # print(f"{k1} : {Paop_1}")
            k2 = f"{ke2} {ke}"
            if k2 not in Films_key_333:
                Films_key_333[k2] = Paop_2
                # print(f"{k2} : {Paop_2}")

# ---
# إضافة Q
Films_key_Q = {}
# ---
"""
Films_key_both_oihn =  Films_key_both
# ---
for ke in Films_key_both:
    ke1_Q = Films_key_both[ke].get("Q" , "")
    # ---
    if ke1_Q :
        Films_key_Q[F_k] = [ke1_Q]
    # ---
    ke2 = ke.lower()
    # ---
    for kak in Films_key_both_oihn:
        kak2 = kak.lower()
        if kak != ke:
            Paop = "{} %s %s" % (Films_key_both[ke] , Films_key_both[kak] )
            ke2_Q = Films_key_both[kak].get("Q" , "")
            # ---
            Q_List = []
            if ke1_Q :     Q_List.append(ke1_Q)
            if ke2_Q :    Q_List.append(ke2_Q)
            # ---
            # ---
            fa1 = "%s %s" % (ke2, kak2 )
            fa2 = "%s %s" % (kak2, ke2 )
            # ---
            if Q_List != []:
                Films_key_Q[fa1] = Q_List
                Films_key_Q[fa2] = Q_List
            # ---
"""
# for CO in Films_key_CAO:
# type_Table_no[CO] =Films_key_CAO[CO]
# ---
# from .all_keys2 import Books_table
# ---
# Films_key_CAO["films"] = "أفلام"
# Films_key_CAO["video games"] = "ألعاب فيديو"
# Films_key_CAO["television series characters"] = "شخصيات مسلسلات تلفزيونية"
# Films_key_CAO["television episodes"] = "حلقات تلفزيونية"
# Films_key_CAO["television shows"] = "عروض تلفزيونية"
# Films_key_CAO["television series"] = "مسلسلات تلفزيونية"
# Films_key_CAO["television programming"] = "برمجة تلفزيونية"
# Films_key_CAO["television programs"] = "برامج تلفزيونية"
# Films_key_CAO["television schedules"] = "جداول تلفزيونية"
# ---
Films_key_CAO["lgbt-related films"] = "أفلام {} متعلقة بإل جي بي تي"
Films_key_CAO["lgbtrelated films"] = "أفلام {} متعلقة بإل جي بي تي"
Films_key_CAO["lgbtq-related films"] = "أفلام {} متعلقة بإل جي بي تي كيو"
Films_key_CAO["lgbtqrelated films"] = "أفلام {} متعلقة بإل جي بي تي كيو"
# ---
Films_key_CAO_new_format = {}
Films_key_CAO_new_format["lgbtrelated films"] = "أفلام {} متعلقة بإل جي بي تي"
Films_key_CAO_new_format["lgbtqrelated films"] = "أفلام {} متعلقة بإل جي بي تي كيو"
# ---
for uu, uu_tab in type_Table_no.items():
    if uu_tab:
        typeTable_4[uu] = {"ar": uu_tab, "Q": ""}
# ---
# for le in Lenth:
# printe.output('<<lightblue>> films_mslslat len "<<lightpurple>>%s"<<default>>:\t%d. '% (le , len(Lenth[le].keys())))
# ---
boh = 0
# --- films_mslslat.py: len Nat_women:267, Films_key_man:131 boh : 69954
# films_mslslat len "Films_TT":  5073.
# films_mslslat len "Films_key_CAO":     51628.
# ---
# printe.output("third_Films_key_CAO == %d " % third_Films_key_CAO)
# printe.output("ss_Films_key_CAO == %d " % ss_Films_key_CAO)
# printe.output("vfvfv == %d " % vfvfv)
# printe.output("len(Films_key_333) == %d " % len(Films_key_333))
# ---
tabe_2 = copy.deepcopy(Films_keys_male_female)
# ---
for en, tab in Films_keys_male_female.items():
    for en2, tab2 in tabe_2.items():
        if en == en2:
            continue
        # ---
        new_lab_male = ""
        new_lab_female = ""
        # ---
        if tab["female"] and tab2["female"]:
            new_lab_female = f"{tab['female']} {tab2['female']}"
        # ---
        if tab["male"] and tab2["male"]:
            new_lab_male = f"{tab['male']} {tab2['male']}"
        # ---
        new_key = f"{en} {en2}".lower()
        # ---
        # if new_key == "historical romance": print("(historical romance)\n" * 10)
        # ---
        Films_keys_both_new[new_key] = {"male": new_lab_male, "female": new_lab_female}


len_print.data_len("films_mslslat.py", {
    "Films_key_For_nat": Films_key_For_nat,
    "films_mslslat_tab": films_mslslat_tab,
    "third_Films_key_CAO": third_Films_key_CAO,
    "ss_Films_key_CAO": ss_Films_key_CAO,
    "vfvfv": vfvfv,
    "Films_key_333": Films_key_333,
    "Films_TT": Films_TT,
    "Films_key_CAO": Films_key_CAO,
    "Films_keys_both_new": Films_keys_both_new,
})

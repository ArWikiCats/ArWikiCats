#!/usr/bin/python3
"""

الأسطر المخفية تبدأ بـ
#o

SELECT DISTINCT #?item ?humanLabel
#?ar
#?page_en ?page_ar
(concat('   "' , ?page_en , '":"' , ?page_ar  , '",')  as ?itemscds)
WHERE {
 # ?human wdt:P31 ?cc.
  #?cc wdt:P31 wd:Q31629.
  #?cc wdt:P31 wd:Q151885.
 { ?human wdt:P31 wd:Q28640. } UNION { ?human wdt:P31 wd:Q12737077.}#مهنة
  FILTER NOT EXISTS {?human wdt:P31 wd:Q31629. }
  FILTER NOT EXISTS {?human wdt:P31 wd:Q188451. }
  FILTER NOT EXISTS {?human wdt:P31 wd:Q1968435. }
  ?human wdt:P910 ?item .
  ?item wdt:P301 ?human.
  ?article schema:about ?item ; schema:isPartOf <https://en.wikipedia.org/> ; schema:name ?page_en .
  ?article2 schema:about ?item ; schema:isPartOf <https://ar.wikipedia.org/> ; schema:name ?page_ar .
  #FILTER NOT EXISTS {?article schema:about ?item ; schema:isPartOf <https://ar.wikipedia.org/> . }.
  SERVICE wikibase:label {
    bd:serviceParam wikibase:language "ar,en" .
  }
  ?item rdfs:label ?ar .  FILTER((LANG(?ar)) = "ar")

    }
#LIMIT 100

"""

import sys
from ...helps import len_print
from ..utils.json_dir import open_json_file

# ---
from ..nats.Nationality import Nat_mens
from ..sports.cycling import new2019_cycling
from ..mixed.all_keys2 import Books_table
from ..politics.ministers import ministrs_tab_for_Jobs_2020
from ..by_type import Music_By_table
from ..tv.films_mslslat import Films_key_For_Jobs
from .Jobs2 import Jobs_2
from ..mixed.male_keys import religious_female_keys
from ..companies import companies_to_jobs
from .jobs_singers import Men_Womens_Singers, films_type
from .jobs_players_list import Football_Keys_players, players_to_Men_Womens_Jobs, Female_Jobs_to
from .jobs_defs import religious_keys_PP, Men_Womens_Jobs_2


Jobs_new = {}
# Jobs_new["fifa world cup players"] = "لاعبو كأس العالم لكرة القدم"
# ---
Jobs_2020 = {
    # "bridge players" : {"mens":"", "womens":""},
    # "soft tennis players" : {"mens":"", "womens":""},
    # "xiangqi players" : {"mens":"", "womens":""},
    "lawn bowls players": {"mens": "", "womens": ""},
    # "dartchers" : {"mens":"", "womens":""},
    # "jet skiers" : {"mens":"", "womens":""},
    # "freestyle skiers" : {"mens":"", "womens":""},
    # "alpine skiers" : {"mens":"", "womens":""}
    # "modern pentathletes" : {"mens":"", "womens":""},
    "community activists": {"mens": "ناشطو مجتمع", "womens": "ناشطات مجتمع"},
    "ecosocialists": {"mens": "إيكولوجيون", "womens": "إيكولوجيات"},
    "ecosocialistes": {"mens": "إيكولوجيون", "womens": "إيكولوجيات"},
    "horse trainers": {"mens": "مدربو خيول", "womens": "مدربات خيول"},
    "bullfighters": {"mens": "مصارعو ثيران", "womens": "مصارعات ثيران"},
    "supremacists": {"mens": "عنصريون", "womens": "عنصريات"},
    "white supremacists": {"mens": "عنصريون بيض", "womens": "عنصريات بيضوات"},
    "ceramists": {"mens": "خزفيون", "womens": "خزفيات"},
    "bodybuilders": {"mens": "لاعبو كمال أجسام", "womens": "لاعبات كمال أجسام"},
    "bowlers": {"mens": "لاعبو بولينج", "womens": "لاعبات بولينج"},
    "dragon boat racers": {
        "mens": "متسابقو قوارب التنين",
        "womens": "متسابقات قوارب التنين",
    },
    # "ice sledge speed racers" : {"mens":"متسابقو ", "womens":"متسابقات "},
    "ju-jitsu practitioners": {"mens": "ممارسو جوجوتسو", "womens": "ممارسات جوجوتسو"},
    "kurash practitioners": {"mens": "ممارسو كوراش", "womens": "ممارسات كوراش"},
    "silat practitioners": {"mens": "ممارسو سيلات", "womens": "ممارسات سيلات"},
    "pencak silat practitioners": {
        "mens": "ممارسو بنكات سيلات",
        "womens": "ممارسات بنكات سيلات",
    },
    "sambo practitioners": {"mens": "ممارسو سامبو", "womens": "ممارسات سامبو"},
    "ski orienteers": {"mens": "متسابقو تزلج موجه", "womens": "متسابقات تزلج موجه"},
    "ski-orienteers": {"mens": "متسابقو تزلج موجه", "womens": "متسابقات تزلج موجه"},
    "artistic swimmers": {"mens": "سباحون فنيون", "womens": "سباحات فنيات"},
    "synchronised swimmers": {"mens": "سباحون متزامنون", "womens": "سباحات متزامنات"},
    "powerlifters": {"mens": "ممارسو رياضة القوة", "womens": "ممارسات رياضة القوة"},
    "rifle shooters": {"mens": "رماة بندقية", "womens": "راميات بندقية"},
    "wheelchair curlers": {
        "mens": "لاعبو كيرلنغ على الكراسي المتحركة",
        "womens": "لاعبات كيرلنغ على الكراسي المتحركة",
    },
    "wheelchair fencers": {
        "mens": "مبارزون على الكراسي المتحركة",
        "womens": "مبارزات على الكراسي المتحركة",
    },
    "sepak takraw players": {
        "mens": "لاعبو سيباك تاكرو",
        "womens": "لاعبات سيباك تاكرو",
    },
    "boccia players": {"mens": "لاعبو بوتشيا", "womens": "لاعبات بوتشيا"},
    "wheelchair rugby players": {
        "mens": "لاعبو رغبي على الكراسي المتحركة",
        "womens": "لاعبات رغبي على الكراسي المتحركة",
    },
    "wheelchair tennis players": {
        "mens": "لاعبو كرة مضرب على الكراسي المتحركة",
        "womens": "لاعبات كرة مضرب على الكراسي المتحركة",
    },
}
# ---
for a, aa in ministrs_tab_for_Jobs_2020.items():
    Jobs_2020[a] = aa
# ---
Jobs_key_mens = {}
# Jobs_key_womens#Jobs_key_mens
Jobs_key_womens = {}
womens_Jobs_2017 = {}
# ,"male actors":"ممثلون ذكور"
# ,"film people":"مهن سينمائية"
# ,"country singers":"مغنو "
# ,"child singers":"مغنو "
# ,"crooners":""
# ,"musical theatre actors":"مغنو "

# ---
Men_Womens_Jobs = {}
# ---
Men_Womens_Jobs.update(Men_Womens_Jobs_2)
# ---
Jobs_key_Format = {
    # "politicians who committed suicide" : {"mens":"سياسيون أقدموا على الانتحار", "womens":"سياسيات أقدمن على الانتحار"},
    "{} people in health professions": "عاملون {} بمهن صحية",
    # "{} people in health occupations":"عاملون {} بمهن صحية",
    "{} eugenicists": "علماء {nato} متخصصون في تحسين النسل",
}
Men_Womens_with_nato = {
    "eugenicists": {
        "mens": "علماء {nato} متخصصون في تحسين النسل",
        "womens": "عالمات {nato} متخصصات في تحسين النسل",
    },
    "politicians who committed suicide": {
        "mens": "سياسيون {nato} أقدموا على الانتحار",
        "womens": "سياسيات {nato} أقدمن على الانتحار",
    },
    "contemporary artists": {
        "mens": "فنانون {nato} معاصرون",
        "womens": "فنانات {nato} معاصرات",
    },
}
# ---
# ,"marine painters":  {"mens":"رسامو ", "womens":"رسامات "}
# "propagandists" : {"mens":"مدربو", "womens":"مدربات"},
# "mnemonists":  {"mens":"", "womens":""}
# "art curators" : {"mens":"", "womens":""},
# "erotic artists" : {"mens":"", "womens":""},
# "general practitioners":  {"mens":"", "womens":""},
# "otolaryngologists":  {"mens":"", "womens":""},
# "comic book creators":  {"mens":"", "womens":""},
# "inkers":  {"mens":"", "womens":""},
# "pencillers":  {"mens":"", "womens":""},
# "letterers":  {"mens":"", "womens":""},
# "video game businesspeople":  { "mens": "شخصيات أعمال {nato} في ألعاب الفيديو"   ,"womens": "سيدات أعمال {nato} في ألعاب الفيديو"},

# ,"people":  {"mens":"أشخاص", "womens":"نساء"}

# ,"ssssss": {"mens":"لاعبو", "womens":""}
# ,"emigrants": {"mens":"نازحون", "womens":"نازحات"}#emigration
# ,"football players":  {"mens":"لاعبو كرة قدم", "womens":"لاعبات كرة قدم"}
# ,"chess players":  {"mens":"لاعبو شطرنج", "womens":"لاعبات شطرنج"}
# ,"businesswomen":  {"mens":"شخصيات أعمال", "womens":"سيدات أعمال"}
# ,"collaborators":  {"mens":"متعاونون", "womens":"متعاونات"}  # ,"people":  {"mens":"أشخاص", "womens":""}  # ,"justices":  {"mens":"قضاة", "womens":"قاضيات"}  # ,"notaries" : {"mens":"كتاب عدل", "womens":"كاتبات عدل"}  # ,"dramatists and playwrights":  {"mens":"دراميون وكتاب مسرحيون", "womens":"دراميات وكاتبات مسرحيات"} # ,"fictional":  {"mens":"خياليون", "womens":"خياليات"} # ,"educators":  {"mens":"مربون", "womens":"مربيات"} # ,"sculptures":  {"mens":"مخرجون", "womens":"مخرجات"}

# ,"paleontologists":  {"mens":"إحاثيون", "womens":"إحاثيات"}
# ,"secretaries":  {"mens":"أمناء", "womens":"أمينات"}
# ,"cartoonists":  {"mens":"كاريكاتوريون", "womens":"كاريكاتوريات"}
# ,"cartoonists":  {"mens":"كارتونيون", "womens":"كارتونيات"}
# ,"creators":  {"mens":"صانعون", "womens":"صانعات"}
# ,"webcomic creators":  {"mens":"صانعو ويب كومكس", "womens":"صانعات ويب كومكس"}
# ,"comics people":  {"mens":"كتاب قصص مصورة", "womens":"كاتبات قصص مصورة"}
# ,"military":  {"mens":"عسكريون", "womens":"عسكريات"}
# ,"commodores": {"mens":"ضباط بحرية", "womens":"ضابطات بحرية"}
# ---
MenWomensJobsPP = open_json_file("jobs_Men_Womens_PP")
# ---
for k, tab in religious_keys_PP.items():
    MenWomensJobsPP[k] = tab
    # ---
    # "religious activists" = {"mens":"ناشطون دينيون", "womens":"ناشطات دينيات"}
    # ---
    MenWomensJobsPP[f"{k} activists"] = {
        "mens": f"ناشطون {tab['mens']}",
        "womens": f"ناشطات {tab['womens']}",
    }
    # ---
    # print(f"{k} activists")
    # print(MenWomensJobsPP[f"{k} activists"])


# ---
jobs_table_3 = {
    "deaf": {"mens": "صم", "womens": "صم"},
    "blind": {"mens": "مكفوفون", "womens": "مكفوفات"},
    "deafblind": {"mens": "صم ومكفوفون", "womens": "صم ومكفوفات"},
}
# ---
executives = {
    # "chief":  "" ,
    "railroad": "سكك حديدية",
    "media": "وسائل إعلام",
    "public transportation": "نقل عام",
    "film studio": "استوديوهات أفلام",
    "advertising": "إعلانات",
    "music industry": "صناعة الموسيقى",
    "newspaper": "جرائد",
    "radio": "مذياع",
    "television": "تلفاز",
    "media5": "",
}
# ---
for dcf, ll in executives.items():
    jobs_table_3[f"{dcf} executives"] = {
        "mens": f"مدراء {ll}",
        "womens": f"مديرات {ll}",
    }
# ---
for dgh in jobs_table_3.keys():
    MenWomensJobsPP[dgh] = jobs_table_3[dgh]
# ---
for va, b in Jobs_2020.items():
    # printe.output("python3 core8/pwb.py asa/like addpro -ns:14 -project:أعلام -like:%s -like:%s" % (b["mens"].replace(" ","_"),b["womens"].replace(" ","_") ) )
    if b["mens"] and b["womens"]:
        if va.lower() not in MenWomensJobsPP:
            MenWomensJobsPP[va.lower()] = b
# ---
for gf, gftab in Football_Keys_players.items():
    if gf.lower() not in MenWomensJobsPP:
        MenWomensJobsPP[gf.lower()] = gftab
# ---
# ---
# "non-fiction writers":  {"mens":"كتاب غير روائيون", "womens":"كاتبات غير روائيات"}
# ---
Nat_Before_Occ = [
    "convicted-of-murder",
    "murdered abroad",
    "contemporary",
    # "university and college presidents",
    "tour de france stage winners",
    "deafblind",
    "deaf",
    "blind",
    "jews",
    "women's rights activists",
    "human rights activists",
    "imprisoned",
    "imprisoned abroad",
    "conservationists",
    "expatriate",
    "defectors",
    "scholars of islam",
    "scholars-of-islam",
    "amputees",
    "expatriates",
    "scholars of",
    "executed abroad",
    "emigrants",
]
# ---
activists_keys = open_json_file("activists_keys")
# ---
for activ in activists_keys.keys():
    activ2 = activ.lower()
    Nat_Before_Occ.append(activ2)
    Men_Womens_Jobs[activ2] = activists_keys[activ]
# ---
MenWomensJobsPP["fashion journalists"] = {
    "mens": "صحفيو موضة",
    "womens": "صحفيات موضة",
}
MenWomensJobsPP["zionists"] = {"mens": "صهاينة", "womens": "صهيونيات"}
MenWomensJobsPP.update(companies_to_jobs)
# ---
for ggg in religious_female_keys.keys():
    MenWomensJobsPP[f"{ggg} founders"] = {
        "mens": f"مؤسسو {religious_female_keys[ggg]}",
        "womens": f"مؤسسات {religious_female_keys[ggg]}",
    }

# ---
MenWomensJobsPP["imprisoned abroad"] = {
    "mens": "مسجونون في الخارج",
    "womens": "مسجونات في الخارج",
}
MenWomensJobsPP["imprisoned"] = {"mens": "مسجونون", "womens": "مسجونات"}
# ---
MenWomensJobsPP["escapees"] = {"mens": "هاربون", "womens": "هاربات"}
MenWomensJobsPP["prison escapees"] = {
    "mens": "هاربون من السجن",
    "womens": "هاربات من السجن",
}
MenWomensJobsPP["missionaries"] = {"mens": "مبشرون", "womens": "مبشرات"}
MenWomensJobsPP["venerated"] = {"mens": "مبجلون", "womens": "مبجلات"}
# MenWomensJobsPP[ "jews" ] = {"mens":"يهود", "womens":"يهوديات"}
# MenWomensJobsPP[ "christians"] = {"mens":"مسيحيون", "womens":"مسيحيات"}
# MenWomensJobsPP[ "muslims"] = {"mens":"مسلمون", "womens":"مسلمات"}
# MenWomensJobsPP[ "zaydis"] = {"mens":"زيود", "womens":"زيديات"}
# ---
"""
booook = {}
for tg in jobs_type.keys():
    booook[ tg.lower() ] = jobs_type[ tg ]

for fff in Books_table.keys():
    if fff.lower() in booook.keys():
        printe.output("fff:%s in jobs_type and in Books_table."  % fff)
printe.output("for fff in jobs_type.keys(): ")
"""
# ---
# printe.output('jobs in Jobs_2: ')
for ioi in Jobs_2:
    ioi2 = ioi.lower()
    if ioi not in MenWomensJobsPP and ioi2 not in MenWomensJobsPP:
        if Jobs_2[ioi]["mens"] or Jobs_2[ioi]["womens"]:
            MenWomensJobsPP[ioi2] = Jobs_2[ioi]
    # else:
    # printe.output('jobs: "%s" : { "mens": "%s" ,"womens":  "%s" },' %  (ioi , Jobs_2[ioi]["mens"],Jobs_2[ioi]["womens"]) )
# ---
for ioiz, b in MenWomensJobsPP.items():
    Men_Womens_Jobs[ioiz.lower()] = b
# ---
# إضافة وضائف مثل مذيعون رياضيون
sports_len = 0
for M_W in MenWomensJobsPP.keys():
    sports_len += 1
    M_W2 = M_W.lower()
    # ---
    Men_Womens_Jobs[f"sports {M_W2}"] = {}
    Men_Womens_Jobs[f"sports {M_W2}"]["mens"] = f"{MenWomensJobsPP[M_W]['mens']} رياضيون"
    Men_Womens_Jobs[f"sports {M_W2}"]["womens"] = f"{MenWomensJobsPP[M_W]['womens']} رياضيات"
    # ---
    Men_Womens_Jobs[f"professional {M_W2}"] = {}
    Men_Womens_Jobs[f"professional {M_W2}"]["mens"] = f"{MenWomensJobsPP[M_W]['mens']} محترفون"
    Men_Womens_Jobs[f"professional {M_W2}"]["womens"] = f"{MenWomensJobsPP[M_W]['womens']} محترفات"
    # ---
    Men_Womens_Jobs[f"wheelchair {M_W2}"] = {}
    Men_Womens_Jobs[f"wheelchair {M_W2}"]["mens"] = f"{MenWomensJobsPP[M_W]['mens']} على الكراسي المتحركة"
    Men_Womens_Jobs[f"wheelchair {M_W2}"]["womens"] = f"{MenWomensJobsPP[M_W]['womens']} على الكراسي المتحركة"
# ---
# "skaters": {"mens":"متزلجون على اللوح", "womens":"متزلجات على اللوح"},#تزلج على اللوح
# "skiers":  {"mens":"متزلجون على الثلج", "womens":"متزلجات على الثلج"},#تزحلق على الثلج
# ---
for cyc, cyc_la in new2019_cycling.items():
    cy2 = cyc.lower()
    Men_Womens_Jobs[f"{cy2} cyclists"] = {"mens": f"دراجو {cyc_la}", "womens": f"دراجات {cyc_la}"}
    Men_Womens_Jobs[f"{cy2} winners"] = {"mens": f"فائزون في {cyc_la}", "womens": f"فائزات في {cyc_la}"}
    Men_Womens_Jobs[f"{cy2} stage winners"] = {"mens": f"فائزون في مراحل {cyc_la}", "womens": f"فائزات في مراحل {cyc_la}"}
    Nat_Before_Occ.append(f"{cy2} winners")
    Nat_Before_Occ.append(f"{cy2} stage winners")
# ---
Female_Jobs2 = {}
# ---
for fop in films_type:
    Female_Jobs2[f"{fop} actresses"] = f"ممثلات {films_type[fop]['womens']}"
Female_Jobs2["sportswomen"] = "رياضيات"
# ---
# immigration    الهجرة
# migrations    الهجرة
# emigration  النزوح
# ---
for hh, hh_lab in players_to_Men_Womens_Jobs.items():
    Men_Womens_Jobs[hh] = hh_lab
for gr, gr_lab in Female_Jobs_to.items():
    Female_Jobs2[gr] = gr_lab
# ---
typi = {
    "classical": {"mens": "كلاسيكيون", "womens": "كلاسيكيات"},
    "historical": {"mens": "تاريخيون", "womens": "تاريخيات"},
}
# ---
fffff = []
# ---
"""
gogo = [ x for x in Men_Womens_Jobs]
gogo.sort()
for papa in gogo:
    kaka = '\t,"%s":  {\n\t\t"mens": "%s"\t,"womens": "%s"}'% (papa.lower() , Men_Womens_Jobs[papa]["mens"] , Men_Womens_Jobs[papa]["womens"])
    printe.output(kaka)
"""
# ---
# Nat_Womens = {"estonian":"إستونيات"}
Female_Jobs = {
    "nuns": "راهبات",
    "deafblind actresses": "ممثلات صم ومكفوفات",
    "deaf actresses": "ممثلات صم",
    # "blind" : "ممثلات مكفوفات",
    # "deafblind" : "صم ومكفوفات",
    "actresses": "ممثلات",
    "princesses": "أميرات",
    # ,"female models":"عارضات أزياء",
    "video game actresses": "ممثلات ألعاب فيديو",
    "musical theatre actresses": "ممثلات مسرحيات موسيقية",
    "television actresses": "ممثلات تلفزيون",
    "stage actresses": "ممثلات مسرح",
    "voice actresses": "ممثلات أداء صوتي",
}
# ---
Female_Jobs["women in business"] = "سيدات أعمال"
Female_Jobs["women in politics"] = "سياسيات"
Female_Jobs["lesbians"] = "سحاقيات"
Female_Jobs["businesswomen"] = "سيدات أعمال"
Jobs_key = {}
# ---
NNN_Keys_Films = {
    "filmmakers": {"mens": "صانعو أفلام", "womens": "صانعات أفلام"},
    "film editors": {"mens": "محررو أفلام", "womens": "محررات أفلام"},
    "film directors": {"mens": "مخرجو أفلام", "womens": "مخرجات أفلام"},
    "film producers": {"mens": "منتجو أفلام", "womens": "منتجات أفلام"},
    # "film choreographers" : {"mens":"", "womens":""},
    "film critics": {"mens": "نقاد أفلام", "womens": "ناقدات أفلام"},
    "film historians": {"mens": "مؤرخو أفلام", "womens": "مؤرخات أفلام"},
    # "film people" : {"mens":"", "womens":""},
    # "film score composers" : {"mens":"", "womens":""},
    "cinema editors": {"mens": "محررون سينمائون", "womens": "محررات سينمائيات"},
    "cinema directors": {"mens": "مخرجون سينمائون", "womens": "مخرجات سينمائيات"},
    "cinema producers": {"mens": "منتجون سينمائون", "womens": "منتجات سينمائيات"},
}
# ---
Len_of_Films_Jobs = 0
Len_of_Films_Jobs_bo = 0
for film, film_lab in Films_key_For_Jobs.items():
    # ---
    film2 = film.lower()
    # ---
    for key_o, key_lab in NNN_Keys_Films.items():
        Len_of_Films_Jobs += 1
        Men_Womens_Jobs[key_o] = key_lab
        Len_of_Films_Jobs_bo += 1
        # ---
        key_o2 = key_o.lower()
        oiuio = f"{film2} {key_o2}"
        Men_Womens_Jobs[oiuio] = {}
        # ---
        Men_Womens_Jobs[oiuio]["mens"] = f"{key_lab['mens']} {film_lab}"
        # ---
        Men_Womens_Jobs[oiuio]["womens"] = f"{key_lab['womens']} {film_lab}"
# ---
jobs_type = {
    # ,"film":"أفلام"    ,"action":"حركة"
    "adventure": "مغامرة",
    "alternate history": "تاريخ بديل",
    "animated": "رسوم متحركة",
    "anthology": "أنثولوجيا",
    "biographical": "سيرة ذاتية",
    "black comedy": "كوميديا سوداء",
    "bollywood": "بوليوود",
    "buddy": "رفقاء",
    "business and financial": "أعمال ومالية",
    "financial": "مالية",
    "business": "أعمال",
    "clay animation": "رسوم متحركة طينية",
    "comedy fiction": "خيال كوميدي",
    "comedy thriller": "كوميديا إثارة",
    "comedy": "كوميديا",
    "comedy drama": "كوميديا درامية",  # ,"comedy-drama":"كوميديا درامية"
    "comics": "قصص مصورة",
    "crime thriller": "إثارة وجريمة",
    "crime": "جريمة",
    "crossover fiction": "خيال متقاطع",
    "cyberpunk": "سايبربانك",
    "dance": "رقص",
    "disaster": "كوارث",
    "docudramas": "دراما وثائقية",
    "drama": "دراما",
    "dystopian": "ديستوبيا",
    "environmental fiction": "خيال بيئي",
    "environmental": "بيئة",
    "erotic thriller": "إثارة جنسية",
    "erotica": "أدب جنسي",
    "fantasy": "فنتازيا",
    "finance and investment": "تمويل واستثمار",
    "finance": "تمويل",
    "french comedy": "كوميديا فرنسية",
    "gay male pornography": "إباحية مثلية",
    "gothic horror": "رعب قوطي",
    "historical": "تاريخ",
    "horror": "رعب",
    "investment": "استثمار",
    "japanese horror": "رعب ياباني",
    "kung fu": "كونغ فو",
    "mafia comedy": "مافيا كوميدية",
    "mafia": "مافيا",
    "magazine": "مجلات",
    "magic realism": "واقعية سحرية",
    "martial arts": "فنون قتالية",
    "mystery": "غموض",
    "mysticism": "غموض",
    "newspaper": "صحف",
    "parody": "محاكاة ساخرة",
    "pirate": "قراصنة",
    "police procedural": "إجراءات الشرطة",
    "police procedurals": "إجراءات الشرطة",
    "political fiction": "خيال سياسي",
    "propaganda": "بروباغندا",
    "prussian": "بروسي",
    "psychological horror": "رعب نفسي",
    "radio": "راديو",
    "rape and revenge": "إغتصاب وإنتقام",
    "romantic comedy": "كوميديا رومانسية",
    "samurai": "ساموراي",
    "satire": "هجاء",
    "science fiction action": "خيال علمي وحركة",
    "science fiction": "خيال علمي",
    "silent": "سينما صامتة",
    "slapstick": "كوميديا تهريجية",
    "socialist realism": "واقعية اشتراكية",
    "speculative fiction": "خيال تأملي",
    "sports": "رياضة",
    "spy": "تجسس",
    "surfing": "ركمجة",
    "teen": "مراهقة",
    "television": "تلفزيون",
    "thriller": "إثارة",
    "war": "حرب",
    "yakuza": "ياكوزا",
    "zombie": "زومبي",
}
# ---
jobs_people = {
    "bloggers": {"mens": "مدونو", "womens": "مدونات"},
    "writers": {"mens": "كتاب", "womens": "كاتبات"},
    "critics": {"mens": "نقاد", "womens": "ناقدات"},
    "journalists": {"mens": "صحفيو", "womens": "صحفيات"},
    "producers": {"mens": "منتجو", "womens": "منتجات"},
    "authors": {"mens": "مؤلفو", "womens": "مؤلفات"},
    "editors": {"mens": "محررو", "womens": "محررات"},
    "artists": {"mens": "فنانو", "womens": "فنانات"},
    "directors": {"mens": "مخرجو", "womens": "مخرجات"},
    "publisherspeople": {"mens": "ناشرو", "womens": "ناشرات"},
    "publishers (people)": {"mens": "ناشرو", "womens": "ناشرات"},
    # "evangelists" : {"mens":"", "womens":""},
    # "news anchors" : {"mens":"", "womens":""},
    # "people" : {"mens":"", "womens":""},
    "personalities": {"mens": "شخصيات", "womens": "شخصيات"},
    "presenters": {"mens": "مذيعو", "womens": "مذيعات"},
    "creators": {"mens": "مبتكرو", "womens": "مبتكرات"},
    # "creators":  {"mens":"صانعو", "womens":"صانعات"},
}


# def Add_Jobs():
# ---
for men, men_tab in jobs_people.items():
    if men_tab["mens"] and men_tab["womens"]:
        # ---
        # Books_table
        for book, book_la in Books_table.items():
            Men_Womens_Jobs[f"{book} {men}"] = {
                "mens": f"{men_tab['mens']} {book_la}",
                "womens": f"{men_tab['womens']} {book_la}",
            }
        # ---
        # jobs_type
        for vg, vg_lab in jobs_type.items():
            Men_Womens_Jobs[f"{vg} {men}"] = {
                "mens": f"{men_tab['mens']} {vg_lab}",
                "womens": f"{men_tab['womens']} {vg_lab}",
            }
        # ---
# ---
for put in Men_Womens_Singers.keys():
    Men_Womens_Jobs[put] = Men_Womens_Singers[put]
    # Men_Womens_Jobs["classical {}".format(put)] = {
    # "mens": "{} كلاسيكيون".format(Men_Womens_Singers[put]["mens"])
    # ,"womens": "{} كلاسيكيات".format(Men_Womens_Singers[put]["womens"])
    # }
    # ---
    for nasd, nasd_la in typi.items():
        Men_Womens_Jobs[f"{nasd} {put}"] = {
            "mens": f"{Men_Womens_Singers[put]['mens']} {nasd_la['mens']}",
            "womens": f"{Men_Womens_Singers[put]['womens']} {nasd_la['womens']}",
        }
    # printe.output(put2o)
    # printe.output({"mens": put_m ,"womens": put_f }    )
# ---
for papa, papa_ka in Men_Womens_Jobs.items():
    # if papa not in fffff: fffff.append(papa)
    # Jobs_key_mens[f"male {papa}" ] = "%s ذكور" % papa_ka["mens"]
    # o Jobs_new[f"male {papa}" ] = "%s ذكور" % papa_ka["mens"]
    # ---
    Jobs_key_mens[papa] = papa_ka["mens"]
    # ---
    if papa_ka["womens"]:
        womens_Jobs_2017[papa] = papa_ka["womens"]
        # o Jobs_key_womens["women's " + papa] =  papa_ka["womens"]
        # o Jobs_key_womens["women " + papa] =  papa_ka["womens"]
        # o Jobs_key_womens["female " + papa] =  papa_ka["womens"]
# ---
for bbb3 in Female_Jobs2:
    Female_Jobs[bbb3] = Female_Jobs2[bbb3]
# ---
# ll = 0
for PP, pkk in Jobs_key_mens.items():  #
    if pkk:
        Jobs_key[PP] = pkk
        # print(pkk)
        # if PP.startswith("male"):
        # ll += 1
        # if ll < 5:
        # print("%s: %s" % (PP , pkk) )
        # o else:
        # o Jobs_new[ f"male {PP}" ] = f"{pkk} ذكور"
        # Jobs_new[ f"expatriate {PP}" ] =f"{pkk} مغتربون"
# print ("FF Jobs.py: startswith make :  %d" % ll)
# ---
for yuy in Female_Jobs:
    yuy2 = yuy.lower()
    if Female_Jobs[yuy]:
        Jobs_new[yuy2] = Female_Jobs[yuy]
        Jobs_key_womens[yuy2] = Female_Jobs[yuy]
# ---
# for women in Jobs_key_womens:#
# if Jobs_key_womens[women]:
# Jobs_new[women] = Jobs_key_womens[women]
# ---

# Add_Jobs()

Jobs_key_mens["men's footballers"] = "لاعبو كرة قدم رجالية"

for xi in religious_keys_PP:
    Nat_Before_Occ.append(xi)
# ---
"""for cory in Nat_mens:
    cony2 = cory.lower()
    if Nat_mens[cory] :
        Jobs_new[f"{cony2} people" ] = "%s" % Nat_mens[cory]
        for io in Jobs_key:
            io2 = io.lower()"""
# ---
# ---
for cory in Nat_mens:
    cony2 = cory.lower()
    if Nat_mens[cory]:
        Jobs_new[f"{cony2} people"] = f"{Nat_mens[cory]}"
        # printe.output("%s %s" % (f"{cony2} people", Nat_mens[cory]))
# ---
# ---
Jobs_new["people of the ottoman empire"] = "عثمانيون"
# oppp = {}
# ---
dfg = 0
for x in Jobs_key.keys():
    # oppp[x.lower()] =  Jobs_key[x]
    Jobs_new[x.lower()] = Jobs_key[x]
    if sys.argv and "2080io" in sys.argv:
        for key in Music_By_table:
            if (Jobs_key[x] != "") and (Music_By_table[key] != ""):
                ip_1 = f"{x} {key}"
                ip_2 = f"{Jobs_key[x]} {Music_By_table[key]}"
                dfg += 1
                Jobs_new[ip_1] = ip_2
                # printe.output(',"%s":"%s"' %   (ip_1 , ip_2))
# ---
Lenth = {
    "Len_of_Films_Jobs": Len_of_Films_Jobs,
    "Jobs_key": sys.getsizeof(Jobs_key),
    "Jobs_new": sys.getsizeof(Jobs_new),
    "Jobs_key_mens": sys.getsizeof(Jobs_key_mens),
    "Jobs_key_womens": sys.getsizeof(Jobs_key_womens),
    "Men_Womens_Jobs": sys.getsizeof(Men_Womens_Jobs),
}
# ---

len_print.lenth_pri("jobs.py", Lenth)

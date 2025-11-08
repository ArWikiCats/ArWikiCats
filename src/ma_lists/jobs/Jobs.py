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
from ..utils.json_dir import open_json

# ---
from ..nats.Nationality import Nat_mens
from ..sports.cycling import new2019_cycling
from ..mixed.all_keys2 import Books_table
from ..politics.ministers import ministrs_tab_for_Jobs_2020
# from ..by_type import Music_By_table
from ..tv.films_mslslat import Films_key_For_Jobs
from .Jobs2 import Jobs_2
from ..mixed.male_keys import religious_female_keys
from ..companies import companies_to_jobs
from .jobs_singers import Men_Womens_Singers, films_type
from .jobs_players_list import Football_Keys_players, players_to_Men_Womens_Jobs, Female_Jobs_to
from .jobs_defs import RELIGIOUS_KEYS_PP, MEN_WOMENS_JOBS_2

Jobs_new = {}
# ---
Jobs_2020 = {
    "ecosocialists": {"mens": "إيكولوجيون", "womens": "إيكولوجيات"},
    "wheelchair tennis players": {
        "mens": "لاعبو كرة مضرب على الكراسي المتحركة",
        "womens": "لاعبات كرة مضرب على الكراسي المتحركة",
    },
}
# ---
jobs_people = {
    "bloggers": {"mens": "مدونو", "womens": "مدونات"},
    "writers": {"mens": "كتاب", "womens": "كاتبات"},
}
# ---
jobs_type = {
    "adventure": "مغامرة",
    "alternate history": "تاريخ بديل",
    "animated": "رسوم متحركة",
    "science fiction action": "خيال علمي وحركة",
}
# ---
jobs_data = open_json("jobs/jobs.json")
# ---
Jobs_2020.update({x: v for x, v in jobs_data["Jobs_2020"].items() if v.get("mens") and v.get("womens")})
jobs_people.update({x: v for x, v in jobs_data["jobs_people"].items() if v.get("mens") and v.get("womens")})
jobs_type.update({x: v for x, v in jobs_data["jobs_type"].items() if v})  # v is string
# ---
for minister_category, minister_labels in ministrs_tab_for_Jobs_2020.items():
    Jobs_2020[minister_category] = minister_labels
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
Men_Womens_Jobs.update(MEN_WOMENS_JOBS_2)
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
MenWomensJobsPP = open_json("jobs/jobs_Men_Womens_PP.json")
# ---
for religious_key, gendered_titles in RELIGIOUS_KEYS_PP.items():
    MenWomensJobsPP[religious_key] = gendered_titles
    # ---
    # "religious activists" = {"mens":"ناشطون دينيون", "womens":"ناشطات دينيات"}
    # ---
    MenWomensJobsPP[f"{religious_key} activists"] = {
        "mens": f"ناشطون {gendered_titles['mens']}",
        "womens": f"ناشطات {gendered_titles['womens']}",
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
for industry_key, industry_label in executives.items():
    jobs_table_3[f"{industry_key} executives"] = {
        "mens": f"مدراء {industry_label}",
        "womens": f"مديرات {industry_label}",
    }
# ---
for disability_key, disability_labels in jobs_table_3.items():
    MenWomensJobsPP[disability_key] = disability_labels
# ---
for job_name, gender_labels in Jobs_2020.items():
    # printe.output("python3 core8/pwb.py asa/like addpro -ns:14 -project:أعلام -like:%s -like:%s" % (b["mens"].replace(" ","_"),b["womens"].replace(" ","_") ) )
    if gender_labels["mens"] and gender_labels["womens"]:
        if job_name.lower() not in MenWomensJobsPP:
            MenWomensJobsPP[job_name.lower()] = gender_labels
# ---
for player_category, player_labels in Football_Keys_players.items():
    if player_category.lower() not in MenWomensJobsPP:
        MenWomensJobsPP[player_category.lower()] = player_labels
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
activists_keys = open_json("jobs/activists_keys.json")
# ---
for activist_category, activist_labels in activists_keys.items():
    normalized_key = activist_category.lower()
    Nat_Before_Occ.append(normalized_key)
    Men_Womens_Jobs[normalized_key] = activist_labels
# ---
MenWomensJobsPP["fashion journalists"] = {
    "mens": "صحفيو موضة",
    "womens": "صحفيات موضة",
}
MenWomensJobsPP["zionists"] = {"mens": "صهاينة", "womens": "صهيونيات"}
MenWomensJobsPP.update(companies_to_jobs)
# ---
for religious_key, female_label in religious_female_keys.items():
    MenWomensJobsPP[f"{religious_key} founders"] = {
        "mens": f"مؤسسو {female_label}",
        "womens": f"مؤسسات {female_label}",
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
for job_key in Jobs_2:
    lowered_job_key = job_key.lower()
    if job_key not in MenWomensJobsPP and lowered_job_key not in MenWomensJobsPP:
        if Jobs_2[job_key]["mens"] or Jobs_2[job_key]["womens"]:
            MenWomensJobsPP[lowered_job_key] = Jobs_2[job_key]
    # else:
    # printe.output('jobs: "%s" : { "mens": "%s" ,"womens":  "%s" },' %  (ioi , Jobs_2[ioi]["mens"],Jobs_2[ioi]["womens"]) )
# ---
for job_key, gender_labels in MenWomensJobsPP.items():
    Men_Womens_Jobs[job_key.lower()] = gender_labels
# ---
# إضافة وضائف مثل مذيعون رياضيون
sports_len = 0
for base_job_key, base_job_labels in MenWomensJobsPP.items():
    sports_len += 1
    lowered_job_key = base_job_key.lower()
    # ---
    Men_Womens_Jobs[f"sports {lowered_job_key}"] = {}
    Men_Womens_Jobs[f"sports {lowered_job_key}"]["mens"] = f"{base_job_labels['mens']} رياضيون"
    Men_Womens_Jobs[f"sports {lowered_job_key}"]["womens"] = f"{base_job_labels['womens']} رياضيات"
    # ---
    Men_Womens_Jobs[f"professional {lowered_job_key}"] = {}
    Men_Womens_Jobs[f"professional {lowered_job_key}"]["mens"] = f"{base_job_labels['mens']} محترفون"
    Men_Womens_Jobs[f"professional {lowered_job_key}"]["womens"] = f"{base_job_labels['womens']} محترفات"
    # ---
    Men_Womens_Jobs[f"wheelchair {lowered_job_key}"] = {}
    Men_Womens_Jobs[f"wheelchair {lowered_job_key}"]["mens"] = f"{base_job_labels['mens']} على الكراسي المتحركة"
    Men_Womens_Jobs[f"wheelchair {lowered_job_key}"]["womens"] = f"{base_job_labels['womens']} على الكراسي المتحركة"
# ---
# "skaters": {"mens":"متزلجون على اللوح", "womens":"متزلجات على اللوح"},#تزلج على اللوح
# "skiers":  {"mens":"متزلجون على الثلج", "womens":"متزلجات على الثلج"},#تزحلق على الثلج
# ---
for cycling_event_key, cycling_event_label in new2019_cycling.items():
    lowered_event_key = cycling_event_key.lower()
    Men_Womens_Jobs[f"{lowered_event_key} cyclists"] = {
        "mens": f"دراجو {cycling_event_label}",
        "womens": f"دراجات {cycling_event_label}",
    }
    Men_Womens_Jobs[f"{lowered_event_key} winners"] = {
        "mens": f"فائزون في {cycling_event_label}",
        "womens": f"فائزات في {cycling_event_label}",
    }
    Men_Womens_Jobs[f"{lowered_event_key} stage winners"] = {
        "mens": f"فائزون في مراحل {cycling_event_label}",
        "womens": f"فائزات في مراحل {cycling_event_label}",
    }
    Nat_Before_Occ.append(f"{lowered_event_key} winners")
    Nat_Before_Occ.append(f"{lowered_event_key} stage winners")
# ---
Female_Jobs2 = {}
# ---
for film_category, film_gender_labels in films_type.items():
    Female_Jobs2[f"{film_category} actresses"] = f"ممثلات {film_gender_labels['womens']}"
Female_Jobs2["sportswomen"] = "رياضيات"
# ---
# immigration    الهجرة
# migrations    الهجرة
# emigration  النزوح
# ---
for sports_category, sports_labels in players_to_Men_Womens_Jobs.items():
    Men_Womens_Jobs[sports_category] = sports_labels
for female_job_key, female_job_label in Female_Jobs_to.items():
    Female_Jobs2[female_job_key] = female_job_label
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

# def Add_Jobs():
# ---
for job_category, job_titles in jobs_people.items():
    if job_titles["mens"] and job_titles["womens"]:
        # ---
        # Books_table
        for book_key, book_label in Books_table.items():
            Men_Womens_Jobs[f"{book_key} {job_category}"] = {
                "mens": f"{job_titles['mens']} {book_label}",
                "womens": f"{job_titles['womens']} {book_label}",
            }
        # ---
        # jobs_type
        for genre_key, genre_label in jobs_type.items():
            Men_Womens_Jobs[f"{genre_key} {job_category}"] = {
                "mens": f"{job_titles['mens']} {genre_label}",
                "womens": f"{job_titles['womens']} {genre_label}",
            }
        # ---
# ---
for singer_category, singer_labels in Men_Womens_Singers.items():
    Men_Womens_Jobs[singer_category] = singer_labels
    # Men_Womens_Jobs["classical {}".format(put)] = {
    # "mens": "{} كلاسيكيون".format(Men_Womens_Singers[put]["mens"])
    # ,"womens": "{} كلاسيكيات".format(Men_Womens_Singers[put]["womens"])
    # }
    # ---
    for style_key, style_labels in typi.items():
        Men_Womens_Jobs[f"{style_key} {singer_category}"] = {
            "mens": f"{Men_Womens_Singers[singer_category]['mens']} {style_labels['mens']}",
            "womens": f"{Men_Womens_Singers[singer_category]['womens']} {style_labels['womens']}",
        }
    # printe.output(put2o)
    # printe.output({"mens": put_m ,"womens": put_f }    )
# ---
for job_key, gender_labels in Men_Womens_Jobs.items():
    # if papa not in fffff: fffff.append(papa)
    # Jobs_key_mens[f"male {papa}" ] = "%s ذكور" % papa_ka["mens"]
    # o Jobs_new[f"male {papa}" ] = "%s ذكور" % papa_ka["mens"]
    # ---
    Jobs_key_mens[job_key] = gender_labels["mens"]
    # ---
    if gender_labels["womens"]:
        womens_Jobs_2017[job_key] = gender_labels["womens"]
        # o Jobs_key_womens["women's " + papa] =  papa_ka["womens"]
        # o Jobs_key_womens["women " + papa] =  papa_ka["womens"]
        # o Jobs_key_womens["female " + papa] =  papa_ka["womens"]
# ---
for female_job_key, female_job_label in Female_Jobs2.items():
    Female_Jobs[female_job_key] = female_job_label
# ---
# ll = 0
for job_key, job_label in Jobs_key_mens.items():  #
    if job_label:
        Jobs_key[job_key] = job_label
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
for female_job_key, female_job_label in Female_Jobs.items():
    lowered_female_job_key = female_job_key.lower()
    if female_job_label:
        Jobs_new[lowered_female_job_key] = female_job_label
        Jobs_key_womens[lowered_female_job_key] = female_job_label
# ---
# for women in Jobs_key_womens:#
# if Jobs_key_womens[women]:
# Jobs_new[women] = Jobs_key_womens[women]
# ---

# Add_Jobs()

Jobs_key_mens["men's footballers"] = "لاعبو كرة قدم رجالية"

for religious_key in RELIGIOUS_KEYS_PP:
    Nat_Before_Occ.append(religious_key)
# ---
"""for cory in Nat_mens:
    cony2 = cory.lower()
    if Nat_mens[cory] :
        Jobs_new[f"{cony2} people" ] = "%s" % Nat_mens[cory]
        for io in Jobs_key:
            io2 = io.lower()"""
# ---
# ---
for nationality_key, nationality_label in Nat_mens.items():
    lowered_nationality = nationality_key.lower()
    if nationality_label:
        Jobs_new[f"{lowered_nationality} people"] = f"{nationality_label}"
        # printe.output("%s %s" % (f"{lowered_nationality} people", nationality_label))
# ---
# ---
Jobs_new["people of the ottoman empire"] = "عثمانيون"
# oppp = {}
# ---
dfg = 0
for job_key in Jobs_key.keys():
    # oppp[x.lower()] =  Jobs_key[x]
    Jobs_new[job_key.lower()] = Jobs_key[job_key]
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

#!/usr/bin/python3
"""

from .jobs_players_list import Jobs_players, Football_Keys_players, players_to_Men_Womens_Jobs, Female_Jobs_to

"""
from ..utils.json_dir import open_json

# ---
from ..sports.Sport_key import (
    Sports_Keys_For_Team,
    Sports_Keys_For_Jobs,
    Sports_Keys_For_Label,
)

# ---
Female_Jobs_to = {}
players_to_Men_Womens_Jobs = {}
# ---
Football_Keys_players = open_json("jobs/jobs_Football_Keys_players.json") or {}
# ---
Football_Keys_players_x = {}
# "punters": {"mens":"", "womens":""},
# "return specialists": {"mens":"", "womens":""},
# "long snappers": {"mens":"", "womens":""},
# "ends": {"mens":"", "womens":""},
# "tight ends": {"mens":"", "womens":""},
# "five-eighths": {"mens":"", "womens":""},
# "hookers": {"mens":"", "womens":""},
# "locks": {"mens":"", "womens":""},
# "props": {"mens":"", "womens":""},
# "second-rows": {"mens":"", "womens":""},
# "managers" : {"mens":"مدربو", "womens":"مدربات"},
# "slotbacks": {"mens":"", "womens":""},
# "defensive backs" : {"mens":"ظهور دفاع", "womens":"ظهيرات دفاع"},
# "sweepers" : {"mens":"أجنحة", "womens":"جناحات"},

# ---

"""
"beach volleyball players":""#"لاعبو ss",
"racquets players":""#"لاعبو ss",
"real tennis players":""#"لاعبو ss",
"roque players":""#"لاعبو ss",
"glider pilots":""#"لاعبو ss",
"javelin throwers":""#"لاعبو ss",
"modern pentathletes":""#"لاعبو ss",
"motorboat racers":""#"لاعبو ss",
"pelotaris":""#"لاعبو ss",
"synchronized swimmers":""#"لاعبو ss",
"tug of war competitors":""#"لاعبو ss",
"wheelchair racers":""#"لاعبو ss",
#"strength athletes":"",
#"cue sports players":"",
#"esports players":"",
"""
# ---
# Jobs_players = {
# ,"divers":  {"mens":"غطاسون", "womens":"غطاسات"}
# ,"triathletes":  {"mens":"رياضيون", "womens":"رياضيات"}
# "speed skaters": {"mens":"", "womens":""},
# "skaters": {"mens":"متزلجون", "womens":"متزلجات"},
# ---
# "freestyle swimmers" : {"mens":"سباحو التزلج الحر", "womens":"سباحات التزلج الحر"},
# "fencers" : {"mens":"مبارزو سيف الشيش", "womens":"مبارزات سيف الشيش"},
# ,"women's footballers":  {"mens":"", "womens":"لاعبات كرة قدم"}
# نقلت من jobs2.py

# ---
Jobs_players = open_json("jobs/Jobs_players.json") or {}
# ---
Jobs_players["freestyle swimmers"] = {"mens": "سباحو تزلج حر", "womens": "سباحات تزلج حر"}
# ---
boxerss = {
    "bantamweight": "وزن بانتام",
    "featherweight": "وزن الريشة",
    "lightweight": "وزن خفيف",
    "light heavyweight": "وزن ثقيل خفيف",
    "light-heavyweight": "وزن ثقيل خفيف",
    "light middleweight": "وزن خفيف متوسط",
    "middleweight": "وزن متوسط",
    "super heavyweight": "وزن ثقيل سوبر",
    # ---
    "heavyweight": "وزن ثقيل",
    "welterweight": "وزن الويلتر",
    "flyweight": "وزن الذبابة",
    "super middleweight": "وزن متوسط سوبر",
    "pinweight": "وزن الذرة",
    "super flyweight": "وزن الذبابة سوبر",
    "super featherweight": "وزن الريشة سوبر",
    "super bantamweight": "وزن البانتام سوبر",
    "light flyweight": "وزن ذبابة خفيف",
    "light welterweight": "وزن والتر خفيف",
    "cruiserweight": "وزن الطراد",
    "minimumwe": "",
    "inimumweight": "",
    "atomweight": "وزن الذرة",
    "super cruiserweight": "وزن الطراد سوبر",
    # ---
}
for bo, bo_lab in boxerss.items():
    Jobs_players[f"{bo} boxers"] = {"mens": f"ملاكمو {bo_lab}", "womens": f"ملاكمات {bo_lab}"}
    Jobs_players[f"world {bo} boxing champions"] = {"mens": f"أبطال العالم للملاكمة فئة {bo_lab}", "womens": ""}
# ---
skaterss = {
    "nordic combined": {"mens": "تزلج نوردي مزدوج", "womens": "تزلج نوردي مزدوج"},
    "speed": {"mens": "سرعة", "womens": "سرعة"},
    "roller": {"mens": "بالعجلات", "womens": "بالعجلات"},
    "alpine": {"mens": "منحدرات ثلجية", "womens": "منحدرات ثلجية"},
    "short track speed": {"mens": "مسار قصير", "womens": "مسار قصير"},
}
# ---
for cc, cc_lab in skaterss.items():
    mens = cc_lab["mens"]
    womens = cc_lab["womens"]
    players_to_Men_Womens_Jobs[f"{cc} skaters"] = {
        "mens": f"متزلجو {mens}",
        "womens": f"متزلجات {womens}",
    }
    players_to_Men_Womens_Jobs[f"{cc} skiers"] = {
        "mens": f"متزحلقو {mens}",
        "womens": f"متزحلقات {womens}",
    }
# ---
players_kt = {
    # "ice hockey players":"هوكي جليد",
    # "ice hockey playerss":"هوكي جليد",
    # "floorball players":"هوكي العشب",
    # "tennis players":"تنس",
    "croquet players": "",  # "كروكيت"
    "badminton players": "تنس الريشة",
    "chess players": "شطرنج",
    "basketball players": "كرة السلة",
    "beach volleyball players": "",
    "fifa world cup players": "كأس العالم لكرة القدم",
    "fifa futsal world cup players": "كأس العالم لكرة الصالات",
    "polo players": "بولو",
    "racquets players": "",
    "real tennis players": "",
    "roque players": "",
    "rugby players": "الرجبي",
    "softball players": "سوفتبول",
    "floorball players": "كرة الأرض",
    "table tennis players": "كرة الطاولة",
    "volleyball players": "كرة الطائرة",
    "water polo players": "كرة الماء",
    "field hockey players": "هوكي الميدان",
    "handball players": "كرة يد",
    "tennis players": "كرة مضرب",
    "football referees": "حكام كرة قدم",
    "racing drivers": "سائقو سيارات سباق",
    "snooker players": "سنوكر",
    "baseball players": "كرة القاعدة",
    "players of american football": "كرة قدم أمريكية",
    "players of canadian football": "كرة قدم كندية",
    "association football players": "كرة قدم",
    "gaelic footballers": "كرة قدم غيلية",
    "australian rules footballers": "كرة قدم أسترالية",
    "rules footballers": "كرة قدم",
    "players of australian rules football": "كرة القدم الأسترالية",
    "kabaddi players": "كابادي",
    "poker players": "بوكر",
    "rugby league players": "دوري الرغبي",
    "rugby union players": "اتحاد الرغبي",
    "lacrosse players": "لاكروس",
}
for cc, cva in players_kt.items():
    if cva:
        players_to_Men_Womens_Jobs[cc] = {}
        players_to_Men_Womens_Jobs[cc]["mens"] = f"لاعبو {cva}"
        players_to_Men_Womens_Jobs[cc]["womens"] = f"لاعبات {cva}"
# ---
for pla, pla_la in Jobs_players.items():
    pla2 = pla.lower()
    if pla_la:
        mens = pla_la["mens"]
        womens = pla_la["womens"]
        players_to_Men_Womens_Jobs[pla2] = pla_la
        # --- International
        players_to_Men_Womens_Jobs[f"olympic {pla2}"] = {}
        players_to_Men_Womens_Jobs[f"olympic {pla2}"]["mens"] = f"{mens} أولمبيون"
        players_to_Men_Womens_Jobs[f"olympic {pla2}"]["womens"] = f"{womens} أولمبيات"
        # ---
        players_to_Men_Womens_Jobs[f"international {pla2}"] = {}
        players_to_Men_Womens_Jobs[f"international {pla2}"]["mens"] = f"{mens} دوليون"
        players_to_Men_Womens_Jobs[f"international {pla2}"]["womens"] = f"{womens} دوليات"
# ---
Sport_men = {
    "managers": {"mens": "مدربون", "womens": "مدربات"},
    "competitors": {"mens": "منافسون", "womens": "منافسات"},
    "coaches": {"mens": "مدربون", "womens": "مدربات"},
}
# ---
Sportui = {
    "paralympic": {"mens": "بارالمبيون", "womens": "بارالمبيات"},
    "olympics": {"mens": "أولمبيون", "womens": "أولمبيات"},
    "sports": {"mens": "رياضيون", "womens": "رياضيات"},
}
# ---
players_to_Men_Womens_Jobs["national team coaches"] = {
    "mens": "مدربو فرق وطنية",
    "womens": "مدربات فرق وطنية",
}
players_to_Men_Womens_Jobs["national team managers"] = {
    "mens": "مدربو فرق وطنية",
    "womens": "مدربات فرق وطنية",
}
# players_to_Men_Womens_Jobs["sports agents"] = {"mens":"وكلاء لاعبون", "womens":"وكيلات لاعبون"}
players_to_Men_Womens_Jobs["sports agents"] = {"mens": "وكلاء رياضات", "womens": "وكيلات رياضات"}
players_to_Men_Womens_Jobs["expatriate sprtspeople"] = {
    "mens": "رياضيون مغتربون",
    "womens": "رياضيات مغتربات",
}
players_to_Men_Womens_Jobs["expatriate sportspeople"] = {
    "mens": "رياضيون مغتربون",
    "womens": "رياضيات مغتربات",
}
# ---
for ghj, ghj_tab in Sport_men.items():
    for men, men_tab in Sportui.items():
        kk = f"{men} {ghj}".lower()
        players_to_Men_Womens_Jobs[kk] = {}
        players_to_Men_Womens_Jobs[kk]["mens"] = f"{ghj_tab['mens']} {men_tab['mens']}"
        players_to_Men_Womens_Jobs[kk]["womens"] = f"{ghj_tab['womens']} {men_tab['womens']}"
# ---
for rvf, sport_cla4b in Sports_Keys_For_Label.items():
    players_to_Men_Womens_Jobs["%s champions" % rvf.lower()] = {
        "mens": "أبطال %s " % sport_cla4b,
        "womens": "",
    }
    # players_to_Men_Womens_Jobs[ f"{rvf} coaches"  ] = { "mens":"مدربو %s " % sport_cla4b ,"womens":"مدربات %s " % sport_cla4b }
    # players_to_Men_Womens_Jobs[ f"{rvf} chairmen and investors"  ] = { "mens":"رؤساء ومسيرو %s " % sport_cla4b ,"womens":"رئيسات ومسيرات %s " % sport_cla4b }
# ---
for vvv, sport_clab in Sports_Keys_For_Team.items():
    players_to_Men_Womens_Jobs["world %s champions" % vvv.lower()] = {
        "mens": "أبطال العالم %s " % sport_clab,
        "womens": "",
    }
# ---
for sop, spor_lab in Sports_Keys_For_Jobs.items():
    # ---
    sop2 = sop.lower()
    # ---
    players_to_Men_Womens_Jobs[f"{sop2} biography"] = {
        "mens": "أعلام %s " % spor_lab,
        "womens": "",
    }
    players_to_Men_Womens_Jobs[f"{sop2} commentators"] = {
        "mens": "معلقو %s " % spor_lab,
        "womens": f"معلقات {spor_lab}",
    }
    players_to_Men_Womens_Jobs[f"{sop2} announcers"] = {
        "mens": "مذيعو %s " % spor_lab,
        "womens": f"مذيعات {spor_lab}",
    }
    # players_to_Men_Womens_Jobs[ "%s women's biography" % sop2  ] = { "mens":"" ,"womens":"أعلام %s " % spor_lab}
    # ---
    # players_to_Men_Womens_Jobs[ f"{sop2} champions"  ] = { "mens":"أبطال %s " % spor_lab ,"womens":""}
    # ---
    for ty, ty_la in Football_Keys_players.items():
        y_mens = ty_la["mens"]
        y_womens = ty_la["womens"]
        # ---
        players_to_Men_Womens_Jobs[f"olympic {sop2} {ty.lower()}"] = {
            "mens": f"{y_mens} {spor_lab} أولمبيون",
            "womens": f"{y_womens} {spor_lab} أولمبيات",
        }
        # ---
        ww = f"men's {sop2} {ty.lower()}"
        players_to_Men_Womens_Jobs[ww] = {
            "mens": f"{y_mens} {spor_lab} رجالية",
            "womens": f"{y_mens} {spor_lab} رجالية",
        }
        # ---
        # players_to_Men_Womens_Jobs["women's {} players".format(sop2)] = {"mens":"" ,"womens":"لاعبات {} نسائية".format(spor_lab)}
        Female_Jobs_to[f"women's {sop2} players"] = f"لاعبات {spor_lab} نسائية"
    # ---
    # players_to_Men_Womens_Jobs[ f"{rvf} coaches"  ] = { "mens":"مدربو %s " % sport_cla4b ,"womens":"مدربات %s " % sport_cla4b }
    players_to_Men_Womens_Jobs[f"{sop2} stage winners"] = {
        "mens": f"فائزون في مراحل {spor_lab}",
        "womens": f"فائزات في مراحل {spor_lab}",
    }
    players_to_Men_Womens_Jobs[f"{sop2} coaches"] = {
        "mens": f"مدربو {spor_lab}",
        "womens": f"مدربات {spor_lab}",
    }
    players_to_Men_Womens_Jobs[f"{sop2} executives"] = {
        "mens": f"مسيرو {spor_lab}",
        "womens": f"مسيرات {spor_lab}",
    }
    players_to_Men_Womens_Jobs[f"{sop2} sprtspeople"] = {
        "mens": f"رياضيو {spor_lab}",
        "womens": f"رياضيات {spor_lab}",
    }
    players_to_Men_Womens_Jobs[f"{sop2} sportspeople"] = {
        "mens": f"رياضيو {spor_lab}",
        "womens": f"رياضيات {spor_lab}",
    }
    # players_to_Men_Womens_Jobs["olympic {} players".format(sop2)] = {"mens":"لاعبو {} أولمبيون".format(spor_lab) ,"womens":"لاعبات {} أولمبيات".format(spor_lab)}
    # players_to_Men_Womens_Jobs["men's {} players".format(sop2)] = {"mens":"لاعبو {} رجالية".format(spor_lab) ,"womens":"لاعبات {} رجالية".format(spor_lab)}
    # Female_Jobs2["women's {} players".format(sop2)] = "لاعبات {} نسائية".format(spor_lab)
    # ---
    for ko, ko_tab in Football_Keys_players.items():
        mens = ko_tab["mens"]
        womens = ko_tab["womens"]
        ko2 = ko.lower()
        hghg = f"{sop2} {ko2}"
        # ---
        players_to_Men_Womens_Jobs[hghg] = {}
        players_to_Men_Womens_Jobs[hghg]["mens"] = f"{mens} {spor_lab}"
        players_to_Men_Womens_Jobs[hghg]["womens"] = f"{womens} {spor_lab}"

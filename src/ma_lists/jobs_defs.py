"""

from .jobs_defs import religious_keys_PP, Men_Womens_Jobs_2

"""

religious_keys_PP = {
    "bahá'ís": {"mens": "بهائيون", "womens": "بهائيات"},
    "yazidis": {"mens": "يزيديون", "womens": "يزيديات"},
    "christians": {"mens": "مسيحيون", "womens": "مسيحيات"},
    "anglican": {"mens": "أنجليكيون", "womens": "أنجليكيات"},
    "anglicans": {"mens": "أنجليكيون", "womens": "أنجليكيات"},
    "episcopalians": {"mens": "أسقفيون", "womens": "أسقفيات"},
    "christian": {"mens": "مسيحيون", "womens": "مسيحيات"},
    "buddhist": {"mens": "بوذيون", "womens": "بوذيات"},
    "nazi": {"mens": "نازيون", "womens": "نازيات"},
    "muslim": {"mens": "مسلمون", "womens": "مسلمات"},
    "coptic": {"mens": "أقباط", "womens": "قبطيات"},
    "islamic": {"mens": "إسلاميون", "womens": "إسلاميات"},
    "hindus": {"mens": "هندوس", "womens": "هندوسيات"},
    "hindu": {"mens": "هندوس", "womens": "هندوسيات"},
    "protestant": {"mens": "بروتستانتيون", "womens": "بروتستانتيات"},
    "methodist": {"mens": "ميثوديون لاهوتيون", "womens": "ميثوديات لاهوتيات"},
    # ---
    "jewish": {"mens": "يهود", "womens": "يهوديات"},
    "jews": {"mens": "يهود", "womens": "يهوديات"},
    "zaydis": {"mens": "زيود", "womens": "زيديات"},
    "zaydi": {"mens": "زيود", "womens": "زيديات"},
    "sufis": {"mens": "صوفيون", "womens": "صوفيات"},
    "religious": {"mens": "دينيون", "womens": "دينيات"},
    "muslims": {"mens": "مسلمون", "womens": "مسلمات"},
    "shia muslims": {"mens": "مسلمون شيعة", "womens": "مسلمات شيعيات"},
    "shi'a muslims": {"mens": "مسلمون شيعة", "womens": "مسلمات شيعيات"},
    "sunni muslims": {"mens": "مسلمون سنة", "womens": "مسلمات سنيات"},
    "shia muslim": {"mens": "مسلمون شيعة", "womens": "مسلمات شيعيات"},
    "shi'a muslim": {"mens": "مسلمون شيعة", "womens": "مسلمات شيعيات"},
    "sunni muslim": {"mens": "مسلمون سنة", "womens": "مسلمات سنيات"},
    "evangelical": {"mens": "إنجيليون", "womens": "إنجيليات"},
    "venerated": {"mens": "مبجلون", "womens": "مبجلات"},
    "saints": {"mens": "قديسون", "womens": "قديسات"},
}
# ---
Men_Womens_Jobs_2 = {}
# ---
rel_jOBS = {
    "christians": {"mens": "مسيحيون", "womens": "مسيحيات"},
    "venerated": {"mens": "مبجلون", "womens": "مبجلات"},
    "missionaries": {"mens": "مبشرون", "womens": "مبشرات"},
    "evangelical": {"mens": "إنجيليون", "womens": "إنجيليات"},
    "monks": {"mens": "رهبان", "womens": "راهبات"},
    "nuns": {"mens": "", "womens": "راهبات"},
    "saints": {"mens": "قديسون", "womens": "قديسات"},
    # "hindu":  {"mens":"هندوس", "womens":"هندوسيات"},
    "astrologers": {"mens": "منجمون", "womens": "منجمات"},
    "leaders": {"mens": "قادة", "womens": "قائدات"},
    "bishops": {"mens": "أساقفة", "womens": ""},
    "actors": {"mens": "ممثلون", "womens": "ممثلات"},
    "theologians": {"mens": "لاهوتيون", "womens": "لاهوتيات"},
    "clergy": {"mens": "رجال دين", "womens": "سيدات دين"},
    "religious leaders": {"mens": "قادة دينيون", "womens": "قائدات دينيات"},
}
# ---
for oiuio, oiuio_lab in religious_keys_PP.items():
    kj = f"{oiuio} %s"
    for jobe, jobe_lab in rel_jOBS.items():
        womens = f'{jobe_lab["womens"]} {oiuio_lab["womens"]}' if jobe_lab["womens"] else ""
        Men_Womens_Jobs_2[kj % jobe] = {"mens": f'{jobe_lab["mens"]} {oiuio_lab["mens"]}', "womens": womens}
# ---
painters_PP = {
    "symbolist": {"mens": "رمزيون", "womens": "رمزيات"},
    "history": {"mens": "تاريخيون", "womens": "تاريخيات"},
    "romantic": {"mens": "رومانسيون", "womens": "رومانسيات"},
    "neoclassical": {"mens": "كلاسيكيون حديثون", "womens": "كلاسيكيات حديثات"},
    "religious": {"mens": "دينيون", "womens": "دينيات"},
}
# ---
painters_jOBS = {
    "painters": {"mens": "رسامون", "womens": "رسامات"},
    "artists": {"mens": "فنانون", "womens": "فنانات"},
}
# ---
for fgrrh, fgrrh_lab in painters_PP.items():
    if fgrrh != "history":
        Men_Womens_Jobs_2[fgrrh] = fgrrh_lab

    for jcccobe, jcccobe_lab in painters_jOBS.items():
        Men_Womens_Jobs_2[jcccobe] = jcccobe_lab
        ky = f"{fgrrh} {jcccobe}"
        Men_Womens_Jobs_2[ky] = {}
        Men_Womens_Jobs_2[ky]["mens"] = f"{jcccobe_lab['mens']} {fgrrh_lab['mens']}"
        Men_Womens_Jobs_2[ky]["womens"] = f"{jcccobe_lab['womens']} {fgrrh_lab['womens']}"
# ---
painters_TT = {
    "make-up": "مكياج",
    "comics": "قصص مصورة",
    "marvel comics": "مارفال كومكس",
    "manga": "مانغا",
    "landscape": "مناظر طبيعية",
    "wildlife": "حياة برية",
    "portrait": "بورتريه",
    "animal": "حيوانات",
    "genre": "نوع",
    # "marine": "",
    "still life": "طبيعة صامتة",
}
# ---
for hhh, LLab in painters_TT.items():
    # ---
    Men_Womens_Jobs_2[f"{hhh} painters"] = {
        "mens": f"رسامو {LLab}",
        "womens": f"رسامات {LLab}",
    }
    # ---
    Men_Womens_Jobs_2[f"{hhh} artists"] = {
        "mens": f"فنانو {LLab}",
        "womens": f"فنانات {LLab}",
    }
# ---
military_PP = {
    "military": {"mens": "عسكريون", "womens": "عسكريات"},
    "politicians": {"mens": "سياسيون", "womens": "سياسيات"},
    "nazi": {"mens": "نازيون", "womens": "نازيات"},
    "literary": {"mens": "أدبيون", "womens": "أدبيات"},
    "organizational": {"mens": "تنظيميون", "womens": "تنظيميات"},
}
# ---
military_jOBS = {
    "theorists": {"mens": "منظرون", "womens": "منظرات"},
    "musicians": {"mens": "موسيقيون", "womens": "موسيقيات"},
    "engineers": {"mens": "مهندسون", "womens": "مهندسات"},
    "leaders": {"mens": "قادة", "womens": "قائدات"},
    "officers": {"mens": "ضباط", "womens": "ضابطات"},
    "historians": {"mens": "مؤرخون", "womens": "مؤرخات"},
    "strategists": {"mens": "استراتيجيون", "womens": "استراتيجيات"},
    "nurses": {"mens": "ممرضون", "womens": "ممرضات"},
}
# ---
pppp = ["military", "literary"]
# ---
for fgh, fgh_tab in military_PP.items():
    if fgh not in pppp:
        Men_Womens_Jobs_2[fgh] = fgh_tab
    # ---
    for jccobe, jccobe_tab in military_jOBS.items():
        ky = f"{fgh} {jccobe}"
        Men_Womens_Jobs_2[jccobe] = jccobe_tab
        Men_Womens_Jobs_2[ky] = {}
        Men_Womens_Jobs_2[ky]["mens"] = f"{jccobe_tab['mens']} {fgh_tab['mens']}"
        Men_Womens_Jobs_2[ky]["womens"] = f"{jccobe_tab['womens']} {fgh_tab['womens']}"
# ---
"""
# ---
for cory in Nat_Womens:
    cony2 = cory.lower()
    if Nat_Womens[cory] :
        #Jobs_new[f"{cony2} women in business" ] = "سيدات أعمال %s" % Nat_Womens[cory]
        #o Jobs_new[f"{cony2} women" ] = "%s" % Nat_Womens[cory]
        #o Jobs_new[f"{cony2} female" ] = "%s" % Nat_Womens[cory]
        for io in Female_Jobs:
            io2 = io.lower()
            if Female_Jobs[io] :
                Jobs_new["%s %s" % (cony2 , io2) ] = "%s %s" % (Female_Jobs[io], Nat_Womens[cory])
                #o Jobs_new["%s female %s" % (cony2 , io2) ] = "%s %s" % (Female_Jobs[io], Nat_Womens[cory])
                #printe.output("-----%s female %s" % (cony2 , io2))
                #printe.output("%s %s" % (Female_Jobs[io], Nat_Womens[cory]))
        # ---
        for w_jo in Jobs_key_womens:
            w_jo2 = w_jo.lower()
            if Jobs_key_womens[w_jo] :
                catn  = "%s %s" % (Jobs_key_womens[w_jo], Nat_Womens[cory])
                Jobs_new["%s %s" % (cony2 , w_jo2) ] = catn

"""
# ---

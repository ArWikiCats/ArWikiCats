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
RELIGIOUS_ROLE_LABELS = {
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
for religion_key, religion_labels in religious_keys_PP.items():
    label_template = f"{religion_key} %s"
    for job_key, job_labels in RELIGIOUS_ROLE_LABELS.items():
        womens_label = (
            f'{job_labels["womens"]} {religion_labels["womens"]}'
            if job_labels["womens"]
            else ""
        )
        Men_Womens_Jobs_2[label_template % job_key] = {
            "mens": f'{job_labels["mens"]} {religion_labels["mens"]}',
            "womens": womens_label,
        }
# ---
painters_PP = {
    "symbolist": {"mens": "رمزيون", "womens": "رمزيات"},
    "history": {"mens": "تاريخيون", "womens": "تاريخيات"},
    "romantic": {"mens": "رومانسيون", "womens": "رومانسيات"},
    "neoclassical": {"mens": "كلاسيكيون حديثون", "womens": "كلاسيكيات حديثات"},
    "religious": {"mens": "دينيون", "womens": "دينيات"},
}
# ---
PAINTER_ROLE_LABELS = {
    "painters": {"mens": "رسامون", "womens": "رسامات"},
    "artists": {"mens": "فنانون", "womens": "فنانات"},
}
# ---
for painter_style, painter_style_labels in painters_PP.items():
    if painter_style != "history":
        Men_Womens_Jobs_2[painter_style] = painter_style_labels

    for artist_role, artist_role_labels in PAINTER_ROLE_LABELS.items():
        Men_Womens_Jobs_2[artist_role] = artist_role_labels
        composite_key = f"{painter_style} {artist_role}"
        Men_Womens_Jobs_2[composite_key] = {}
        Men_Womens_Jobs_2[composite_key]["mens"] = (
            f"{artist_role_labels['mens']} {painter_style_labels['mens']}"
        )
        Men_Womens_Jobs_2[composite_key]["womens"] = (
            f"{artist_role_labels['womens']} {painter_style_labels['womens']}"
        )
# ---
PAINTER_CATEGORY_LABELS = {
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
for painter_category, category_label in PAINTER_CATEGORY_LABELS.items():
    Men_Womens_Jobs_2[f"{painter_category} painters"] = {
        "mens": f"رسامو {category_label}",
        "womens": f"رسامات {category_label}",
    }
    Men_Womens_Jobs_2[f"{painter_category} artists"] = {
        "mens": f"فنانو {category_label}",
        "womens": f"فنانات {category_label}",
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
MILITARY_ROLE_LABELS = {
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
for military_key, military_labels in military_PP.items():
    if military_key not in pppp:
        Men_Womens_Jobs_2[military_key] = military_labels
    # ---
    for role_key, role_labels in MILITARY_ROLE_LABELS.items():
        composite_key = f"{military_key} {role_key}"
        Men_Womens_Jobs_2[role_key] = role_labels
        Men_Womens_Jobs_2[composite_key] = {}
        Men_Womens_Jobs_2[composite_key]["mens"] = (
            f"{role_labels['mens']} {military_labels['mens']}"
        )
        Men_Womens_Jobs_2[composite_key]["womens"] = (
            f"{role_labels['womens']} {military_labels['womens']}"
        )
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


MEN_WOMENS_JOBS_2 = Men_Womens_Jobs_2


# --- Tour de
pp_start_with = {
    "wikipedia categories named after": "تصنيفات سميت بأسماء {}",
    "candidates for president of": "مرشحو رئاسة {}",
    # "candidates in president of" : "مرشحو رئاسة {}",
    "candidates-for": "مرشحو {}",
    # "candidates for" : "مرشحو {}",
    "categories named afters": "تصنيفات سميت بأسماء {}",
    "scheduled": "{} مقررة",
    # "defunct" : "{} سابقة",
}
# ---
pp_ends_with = {}
pp_ends_with_pase = {
    "-related professional associations": "جمعيات تخصصية متعلقة ب{}",
    "-related media": "إعلام متعلق ب{}",
    "-related lists": "قوائم متعلقة ب{}",
    "with disabilities": "{} بإعاقات",
    " mens tournament": "{} - مسابقة الرجال",
    " - telugu": "{} - تيلوغوي",
    "first division": "{} الدرجة الأولى",
    "second division": "{} الدرجة الثانية",
    "third division": "{} الدرجة الثالثة",
    "forth division": "{} الدرجة الرابعة",
    "candidates": "مرشحو {}",
    # "candidates for": "مرشحو {} في",
    "squad": "تشكيلة {}",
    "squads": "تشكيلات {}",
    "final tournaments": "نهائيات مسابقات {}",
    "finals": "نهائيات {}",
    " - kannada": "{} - كنادي",
    " - tamil": "{} - تاميلي",
    " - qualifying": "{} - التصفيات",  # – Mixed Doubles
    " - mixed doubles": "{} - زوجي مختلط",  # – Mixed Doubles
    " - men's tournament": "{} - مسابقة الرجال",
    " - women's tournament": "{} - مسابقة السيدات",
    " - men's qualification": "{} - تصفيات الرجال",
    " - women's qualification": "{} - تصفيات السيدات",
    " – kannada": "{} – كنادي",
    " – tamil": "{} – تاميلي",
    " – qualifying": "{} – التصفيات",  # – Mixed Doubles
    " – mixed doubles": "{} – زوجي مختلط",  # – Mixed Doubles
    " – men's tournament": "{} – مسابقة الرجال",
    " – women's tournament": "{} – مسابقة السيدات",
    " womens tournament": "{} – مسابقة السيدات",
    " – men's qualification": "{} – تصفيات الرجال",
    " – women's qualification": "{} – تصفيات السيدات",
}
# ---
# "mixed doubles" : " زوجي مختلط",
# "mixed team" : " فريق مختلط",
#  "womens team" : " فريق سيدات",
#  "mens team" : " فريق رجال",
#   "womens tournament" : " منافسة السيدات",
#   "mens tournament" : " منافسة الرجال",
# ---

fix_o = {
    # "squad navigational boxes": "صناديق تصفح تشكيلات",
    "squads navigational boxes": "صناديق تصفح تشكيلات",
    "navigational boxes": "صناديق تصفح",
    "bids": "ترشيحات",
    "episodes": "حلقات",
    "treaties": "معاهدات",
    "leagues seasons": "مواسم دوريات",
    "leagues": "دوريات",
    "seasons": "مواسم",
    "local elections": "انتخابات محلية",
    "presidential elections": "انتخابات رئاسية",
    "presidential primaries": "انتخابات رئاسية تمهيدية",
    "elections": "انتخابات",
    "champions": "أبطال",
    "organizations": "منظمات",
    "nonprofits": "منظمات غير ربحية",
    "non-profit organizations": "منظمات غير ربحية",
    "non-profit publishers": "ناشرون غير ربحيون",
    "applications": "تطبيقات",
    "employees": "موظفو",
    "resolutions": "قرارات",
    # "ministries" : "وزارات",
    "campaigns": "حملات",
    "referees": "حكام",
    # "films" : "أفلام",
    "squad templates": "قوالب تشكيلات",
    "templates": "قوالب",
    "venues": "ملاعب",
    "stadiums": "استادات",
    "managers": "مدربو",
    "trainers": "مدربو",
    "scouts": "كشافة",
    "coaches": "مدربو",
    "teams": "فرق",
    "owners": "ملاك",
    "owners and executives": "رؤساء تنفيذيون وملاك {}",
    "uniforms": "بدلات",
    "announcers": "مذيعو",
    "playoffs": "تصفيات",
    "genres": "أنواع",
    "leaks": "تسريبات",
    "categories": "تصانيف",
    "qualification": "تصفيات",
    "counties": "مقاطعات",
    # "religious occupations": "مهن دينية",
    # "occupations": "مهن",
    "equipment": "معدات",
    "trophies and awards": "جوائز وإنجازات",
    "logos": "شعارات",
    "tactics and skills": "مهارات",
    "terminology": "مصطلحات",
    "variants": "أشكال",
}

key_5_suff = {
    "tournament": "مسابقة",
    "singles": "فردي",
    "qualification": "تصفيات",
    "team": "فريق",
    "doubles": "زوجي",
}

# ---
key_2_3 = {
    "girls": "فتيات",
    "mixed": "مختلط",
    "boys": "فتيان",
    "singles": "فردي",
    "womens": "سيدات",
    "ladies": "سيدات",
    "males": "رجال",
    "men's": "رجال",
}

for start, start_lab in key_2_3.items():
    for suff, suff_lab in key_5_suff.items():
        ke = f" - {start} {suff}"
        lab_ke = f"{{}} - {suff_lab} {start_lab}"
        pp_ends_with[ke] = lab_ke
# ---
for i, i_lab in fix_o.items():
    pp_ends_with[f" {i}"] = i_lab + " {}"


__all__ = [
    "pp_start_with",
    "pp_ends_with",
    "pp_ends_with_pase",
]

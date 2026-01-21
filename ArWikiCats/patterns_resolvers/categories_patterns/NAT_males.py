"""
# TODO: ADD SOME DATA FROM D:/categories_bot/langlinks/z2_data/NAT.json"""

NAT_PARAMS = ["{males}"]

NAT_DATA_to_check = {
    "{en_nat} martial artists": "ممارسو وممارسات فنون قتالية {males}",  # 120
    "{en_nat} singers": "مغنون ومغنيات {males}",  # 84
    "{en_nat} actors": "ممثلون وممثلات {males}",  # 90
    "{en_nat} boxers": "ملاكمون وملاكمات {males}",  # 136
    "{en_nat} cyclists": "دراجون ودراجات {males}",  # 68
    "{en_nat} film actors": "ممثلو وممثلات أفلام {males}",  # 74
    "{en_nat} television actors": "ممثلو وممثلات تلفاز {males}",  # 60
    "{en_nat} actors by medium": "ممثلون وممثلات {males} حسب الوسط",  # 65
    "{en_nat} footballers": "لاعبو ولاعبات كرة قدم {males}",  # 171
    "{en_nat} tennis players": "لاعبو ولاعبات كرة مضرب {males}",  # 87
    "{en_nat} basketball players": "لاعبو ولاعبات كرة سلة {males}",  # 65
    "{en_nat} expatriate footballers": "لاعبو ولاعبات كرة قدم {males} مغتربون",  # 162
    "{en_nat} businesspeople": "أصحاب أعمال {males}",  # 110
    "{en_nat} non-fiction writers": "كتاب غير روائيين {males}",  # 118
    "{en_nat} christians": "مسيحيون {males}",  # 134
    "{en_nat} muslims": "مسلمون {males}",  # 132
    "{en_nat} sports coaches": "مدربون رياضيون {males}",  # 110
    # "{en_nat} diaspora in united states": "أمريكيون {males}",  # 126
    "{en_nat} diaspora in united states": "شتات {males} في الولايات المتحدة",  # 126
}

NAT_DATA_MALES = {
    # Afghan officials of the United Nations
    "{en_nat} officials of the United Nations": "مسؤولون {males} في الأمم المتحدة",
    # 17th-century Hindu philosophers and theologians
    "{en_nat} philosophers and theologians": "فلاسفة ولاهوتيون {males}",
    "{en_nat} men's basketball players": "لاعبو كرة سلة {males}",  # 64
    "{en_nat} men's footballers": "لاعبو كرة قدم {males}",  # 167
    "{en_nat} expatriate men's footballers": "لاعبو كرة قدم {males} مغتربون",  # 163
    # "{en_nat} general election": "الانتخابات التشريعية {males}",
    # "{en_nat} presidential election": "الانتخابات الرئاسية {males}",
    # "{en_nat} sports coaches": "مدربو رياضة {males}",  # 110
    "{en_nat}": "{males}",  # 187
    # "{en_nat} people": "أعلام {males}",  # 187
    "{en_nat} lgbtq people": "أعلام إل جي بي تي كيو {males}",  # 187
    "{en_nat} people by occupation": "{males} حسب المهنة",  # 182
    "{en_nat} sports-people": "رياضيون {males}",  # 174
    "{en_nat} men": "رجال {males}",  # 183
    "{en_nat} sportsmen": "رياضيون رجال {males}",  # 182
    "{en_nat} people in sports": "{males} في ألعاب رياضية",  # 177
    "{en_nat} people by ethnic or national origin": "{males} حسب الأصل العرقي أو الوطني",  # 178
    "{en_nat} expatriates": "{males} مغتربون",  # 116
    "{en_nat} expatriate": "{males} مغتربون",  # 116
    "{en_nat} men by occupation": "رجال {males} حسب المهنة",  # 174
    "{en_nat} people by descent": "{males} حسب الأصل العرقي أو الوطني",  # 175
    "{en_nat} writers": "كتاب {males}",  # 95
    "{en_nat} politicians": "سياسيون {males}",  # 179
    "{en_nat} sports-people by sport": "رياضيون {males} حسب الرياضة",  # 178
    "{en_nat} expatriate sports-people": "رياضيون {males} مغتربون",  # 171
    "{en_nat} musicians": "موسيقيون {males}",  # 157
    "{en_nat} people by religion": "{males} حسب الدين",  # 164
    "{en_nat} expatriate sports-people by country of residence": "رياضيون {males} مغتربون حسب بلد الإقامة",  # 168
    "{en_nat} diplomats": "دبلوماسيون {males}",  # 172
    "{en_nat} emigrants": "{males} مهاجرون",  # 135
    "{en_nat} people by century": "{males} حسب القرن",  # 121
    "{en_nat} people by political orientation": "{males} حسب التوجه السياسي",  # 156
    "{en_nat} political people": "ساسة {males}",  # 160
    "{en_nat} military personnel": "أفراد عسكريون {males}",  # 106
    "{en_nat} activists": "ناشطون {males}",  # 159
    "{en_nat} lawyers": "محامون {males}",  # 158
    "{en_nat} athletes": "لاعبو قوى {males}",  # 79
    "{en_nat} football managers": "مدربو كرة قدم {males}",  # 154
    "{en_nat} prisoners and detainees": "سجناء ومعتقلون {males}",  # 153
    "{en_nat} scientists": "علماء {males}",  # 151
    "{en_nat} artists": "فنانون {males}",  # 129
    "{en_nat} swimmers": "سباحون {males}",  # 112
    "{en_nat} journalists": "صحفيون {males}",  # 138
    "{en_nat} runners": "عداؤون {males}",  # 142
    "{en_nat} poets": "شعراء {males}",  # 86
    "{en_nat} people by occupation and century": "{males} حسب المهنة والقرن",  # 130
    "{en_nat} film directors": "مخرجو أفلام {males}",  # 134
    "{en_nat} educators": "معلمون {males}",  # 80
    "{en_nat} competitors by sports event": "منافسون {males} حسب الحدث الرياضي",  # 136
    "{en_nat} academics": "أكاديميون {males}",  # 136
    "{en_nat} novelists": "روائيون {males}",  # 101
    "{en_nat} sprinters": "عداؤون سريعون {males}",  # 85
    "{en_nat} criminals": "مجرمون {males}",  # 124
    "{en_nat} murder victims": "ضحايا قتل {males}",  # 128
    "{en_nat} roman catholics": "رومان كاثوليك {males}",  # 127
    "{en_nat} religious leaders": "قادة دينيون {males}",  # 110
    "{en_nat} socialists": "اشتراكيون {males}",  # 127
    "{en_nat} judges": "قضاة {males}",  # 125
    "{en_nat} victims of crime": "ضحايا جرائم {males}",  # 123
    "{en_nat} economists": "اقتصاديون {males}",  # 124
    "{en_nat} mass media people": "إعلاميون {males}",  # 122
    "{en_nat} people by century and occupation": "{males} حسب القرن والمهنة",  # 105
    "{en_nat} writers by century": "كتاب {males} حسب القرن",  # 122
    "{en_nat} freestyle swimmers": "سباحو تزلج حر {males}",  # 122
    "{en_nat} politicians by century": "سياسيون {males} حسب القرن",  # 121
    "{en_nat} human rights activists": "{males} ناشطون في حقوق الإنسان",  # 108
    "{en_nat} composers": "ملحنون {males}",  # 102
    "{en_nat} physicians": "أطباء {males}",  # 117
    "{en_nat} feminists": "نسويون {males}",  # 115
    "{en_nat} historians": "مؤرخون {males}",  # 114
    "{en_nat} communists": "شيوعيون {males}",  # 113
    "{en_nat} people of german descent": "{males} من أصل ألماني",  # 109
    "executed {en_nat} people": "{males} أعدموا",  # 67
    "{en_nat} models": "عارضو أزياء {males}",  # 70
    "{en_nat} painters": "رسامون {males}",  # 94
    "{en_nat} bankers": "مصرفيون {males}",  # 109
    "{en_nat} people with disabilities": "{males} بإعاقات",  # 71
    "assassinated {en_nat} people": "{males} مغتالون",  # 109
    "{en_nat} jews": "يهود {males}",  # 103
    "{en_nat} theatre people": "مسرحيون {males}",  # 102
    "{en_nat} anti-communists": "{males} مناهضون للشيوعية",  # 87
    "{en_nat} prisoners sentenced to death": "مسجونون {males} حكم عليهم بالإعدام",  # 99
    "{en_nat} designers": "مصممون {males}",  # 106
    "{en_nat} engineers": "مهندسون {males}",  # 106
    "{en_nat} short story writers": "كتاب قصة قصيرة {males}",  # 71
    "{en_nat} actors by century": "ممثلون {males} حسب القرن",  # 69
    "{en_nat} murderers": "قتلة {males}",  # 103
    "{en_nat} producers": "منتجون {males}",  # 103
    "{en_nat} musicians by instrument": "موسيقيون {males} حسب الآلة",  # 97
    "{en_nat} architects": "معماريون {males}",  # 102
    "{en_nat} generals": "جنرالات {males}",  # 99
    "{en_nat} long-distance runners": "عداؤو مسافات طويلة {males}",  # 64
    "{en_nat} middle-distance runners": "عداؤو مسافات متوسطة {males}",  # 65
    "{en_nat} civil servants": "موظفو خدمة مدنية {males}",  # 100
    "{en_nat} nationalists": "قوميون {males}",  # 99
    # males with ذكور
    "{en_nat} male swimmers": "سباحون ذكور {males}",  # 101
    "{en_nat} male freestyle swimmers": "سباحو تزلج حر ذكور {males}",  # 121
    "{en_nat} male sprinters": "عداؤون سريعون ذكور {males}",  # 71
    # males without ذكور
    "{en_nat} male martial artists": "ممارسو فنون قتالية ذكور {males}",  # 137
    "{en_nat} male boxers": "ملاكمون ذكور {males}",  # 136
    "{en_nat} male athletes": "لاعبو قوى ذكور {males}",  # 81
    "{en_nat} male actors": "ممثلون ذكور {males}",  # 91
    "{en_nat} male singers": "مغنون ذكور {males}",  # 85
    "{en_nat} male writers": "كتاب ذكور {males}",  # 86
    "{en_nat} male film actors": "ممثلو أفلام ذكور {males}",  # 80
    "{en_nat} martial artists": "ممارسو فنون قتالية {males}",  # 120
}

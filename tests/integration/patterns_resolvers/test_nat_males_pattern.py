"""
Tests
"""

import pytest

from ArWikiCats.patterns_resolvers.nat_males_pattern import resolve_nat_males_pattern
from utils.dump_runner import make_dump_test_name_data_callback

_mens_data_old = {
    # {en_nat} christians
    "bissau-guinean christians": "مسيحيون غينيون بيساويون",
    "anglo-irish christians": "مسيحيون أنجلو إيرلنديون",
    # {en_nat} muslims
    "czechoslovak muslims": "مسلمون تشيكوسلوفاكيون",
    "east german muslims": "مسلمون ألمانيون شرقيون",
}

test_data_males = {
    # standard - {en_nat} people
    "welsh people": "ويلزيون",
    "yemeni people": "يمنيون",
    "africanamerican people": "أمريكيون أفارقة",
    "american people": "أمريكيون",
    "argentine people": "أرجنتينيون",
    "australian people": "أستراليون",
    "austrian people": "نمساويون",
    "barbadian people": "بربادوسيون",
    "bhutanese people": "بوتانيون",
    "bolivian people": "بوليفيون",
    "botswana people": "بوتسوانيون",
    "cameroonian people": "كاميرونيون",
    "cape verdean people": "أخضريون",
    "central american people": "أمريكيون أوسطيون",
    "dutch people": "هولنديون",
    "english people": "إنجليز",
    "gambian people": "غامبيون",
    "german people": "ألمان",
    "indian people": "هنود",
    "iraqi people": "عراقيون",
    "italian people": "إيطاليون",
    "latvian people": "لاتفيون",
    "malagasy people": "مدغشقريون",
    "malaysian people": "ماليزيون",
    "mexican people": "مكسيكيون",
    "moldovan people": "مولدوفيون",
    "mongolian people": "منغوليون",
    "polish people": "بولنديون",
    "rhodesian people": "رودوسيون",
    "romanian people": "رومان",
    "salvadoran people": "سلفادوريون",
    "scottish people": "إسكتلنديون",
    "serbian people": "صرب",
    "somalian people": "صوماليون",
    "sri lankan people": "سريلانكيون",
    "sudanese people": "سودانيون",
    "swedish people": "سويديون",
    "tajikistani people": "طاجيك",
    "togolese people": "توغويون",
    "turkish cypriot people": "قبرصيون شماليون",
    "turkish people": "أتراك",
    "ukrainian people": "أوكرانيون",
    "native american people": "أمريكيون أصليون",
    # {en_nat} lgbtq people
    "albanian lgbtq people": "أعلام إل جي بي تي كيو ألبان",
    "bangladeshi lgbtq people": "أعلام إل جي بي تي كيو بنغلاديشيون",
    "east german lgbtq people": "أعلام إل جي بي تي كيو ألمانيون شرقيون",
    "jamaican lgbtq people": "أعلام إل جي بي تي كيو جامايكيون",
    "norwegian lgbtq people": "أعلام إل جي بي تي كيو نرويجيون",
    "sierra leonean lgbtq people": "أعلام إل جي بي تي كيو سيراليونيون",
    "thai lgbtq people": "أعلام إل جي بي تي كيو تايلنديون",
    "tunisian lgbtq people": "أعلام إل جي بي تي كيو تونسيون",
    # {en_nat} political people
    "libyan political people": "ساسة ليبيون",
    "south african political people": "ساسة جنوب إفريقيون",
    "south african lgbtq people": "أعلام إل جي بي تي كيو جنوب إفريقيون",
    "south african people": "جنوب إفريقيون",
    "central african republic political people": "ساسة أفارقة أوسطيون",
    # {en_nat} people by occupation
    "bissau-guinean people by occupation": "غينيون بيساويون حسب المهنة",
    "equatoguinean people by occupation": "غينيون استوائيون حسب المهنة",
    # {en_nat} sports-people
    "east timorese sports-people": "رياضيون تيموريون شرقيون",
    "dominican republic sports-people": "رياضيون دومينيكانيون",
    "brazilian sports-people": "رياضيون برازيليون",
    # {en_nat} men
    "czechoslovak men": "رجال تشيكوسلوفاكيون",
    "bosnia and herzegovina men": "رجال بوسنيون",
    # {en_nat} sportsmen
    "anglo-irish sportsmen": "رياضيون رجال أنجلو إيرلنديون",
    "ancient-romans sportsmen": "رياضيون رجال رومان قدماء",
    # {en_nat} people in sports
    "chinese taipei people in sports": "تايبيون صينيون في ألعاب رياضية",
    "democratic-republic-of-congo people in sports": "كونغويون ديمقراطيون في ألعاب رياضية",
    # {en_nat} people by ethnic or national origin
    "central american people by ethnic or national origin": "أمريكيون أوسطيون حسب الأصل العرقي أو الوطني",
    "eastern asian people by ethnic or national origin": "آسيويون شرقيون حسب الأصل العرقي أو الوطني",
    # {en_nat} expatriates
    "eastern european expatriates": "أوروبيون شرقيون مغتربون",
    "central asian expatriates": "آسيويون أوسطيون مغتربون",
    # {en_nat} men by occupation
    "federated states-of micronesia men by occupation": "رجال ميكرونيزيون حسب المهنة",
    "equatorial guinean men by occupation": "رجال غينيون استوائيون حسب المهنة",
    # {en_nat} people by descent
    "bissau-guinean people by descent": "غينيون بيساويون حسب الأصل العرقي أو الوطني",
    "east german people by descent": "ألمانيون شرقيون حسب الأصل العرقي أو الوطني",
    # {en_nat} writers
    "ancient-romans writers": "كتاب رومان قدماء",
    "anglo-irish writers": "كتاب أنجلو إيرلنديون",
    # {en_nat} politicians
    "czechoslovak politicians": "سياسيون تشيكوسلوفاكيون",
    "bosnia and herzegovina politicians": "سياسيون بوسنيون",
    # {en_nat} sports-people by sport
    "chinese taipei sports-people by sport": "رياضيون تايبيون صينيون حسب الرياضة",
    "democratic-republic-of-congo sports-people by sport": "رياضيون كونغويون ديمقراطيون حسب الرياضة",
    # {en_nat} expatriate sports-people
    "dominican republic expatriate sports-people": "رياضيون دومينيكانيون مغتربون",
    "east timorese expatriate sports-people": "رياضيون تيموريون شرقيون مغتربون",
    # {en_nat} musicians
    "central african republic musicians": "موسيقيون أفارقة أوسطيون",
    "equatoguinean musicians": "موسيقيون غينيون استوائيون",
    # {en_nat} people by religion
    "eastern asian people by religion": "آسيويون شرقيون حسب الدين",
    "central asian people by religion": "آسيويون أوسطيون حسب الدين",
    # {en_nat} expatriate sports-people by country of residence
    "bissau-guinean expatriate sports-people by country of residence": "رياضيون غينيون بيساويون مغتربون حسب بلد الإقامة",
    "anglo-irish expatriate sports-people by country of residence": "رياضيون أنجلو إيرلنديون مغتربون حسب بلد الإقامة",
    # {en_nat} men's footballers
    "east german men's footballers": "لاعبو كرة قدم ألمانيون شرقيون",
    "czechoslovak men's footballers": "لاعبو كرة قدم تشيكوسلوفاكيون",
    # {en_nat} diplomats
    "ancient-romans diplomats": "دبلوماسيون رومان قدماء",
    "bosnia and herzegovina diplomats": "دبلوماسيون بوسنيون",
    # {en_nat} emigrants
    "chinese taipei emigrants": "تايبيون صينيون مهاجرون",
    "democratic-republic-of-congo emigrants": "كونغويون ديمقراطيون مهاجرون",
    # {en_nat} expatriate men's footballers
    "dominican republic expatriate men's footballers": "لاعبو كرة قدم دومينيكانيون مغتربون",
    "equatorial guinean expatriate men's footballers": "لاعبو كرة قدم غينيون استوائيون مغتربون",
    # {en_nat} people by century
    "ancient-romans people by century": "رومان قدماء حسب القرن",
    "eastern european people by century": "أوروبيون شرقيون حسب القرن",
    # {en_nat} people by political orientation
    "central american people by political orientation": "أمريكيون أوسطيون حسب التوجه السياسي",
    "central asian people by political orientation": "آسيويون أوسطيون حسب التوجه السياسي",
    # {en_nat} military personnel
    "east timorese military personnel": "أفراد عسكريون تيموريون شرقيون",
    "federated states-of micronesia military personnel": "أفراد عسكريون ميكرونيزيون",
    # {en_nat} activists
    "bissau-guinean activists": "ناشطون غينيون بيساويون",
    "anglo-irish activists": "ناشطون أنجلو إيرلنديون",
    # {en_nat} lawyers
    "czechoslovak lawyers": "محامون تشيكوسلوفاكيون",
    "east german lawyers": "محامون ألمانيون شرقيون",
    # {en_nat} athletes
    "bosnia and herzegovina athletes": "لاعبو قوى بوسنيون",
    "chinese taipei athletes": "لاعبو قوى تايبيون صينيون",
    # {en_nat} football managers
    "democratic-republic-of-congo football managers": "مدربو كرة قدم كونغويون ديمقراطيون",
    "dominican republic football managers": "مدربو كرة قدم دومينيكانيون",
    # {en_nat} martial artists
    "eastern asian martial artists": "ممارسو فنون قتالية آسيويون شرقيون",
    "equatoguinean martial artists": "ممارسو فنون قتالية غينيون استوائيون",
    # {en_nat} prisoners and detainees
    "central african republic prisoners and detainees": "سجناء ومعتقلون أفارقة أوسطيون",
    "equatorial guinean prisoners and detainees": "سجناء ومعتقلون غينيون استوائيون",
    # {en_nat} scientists
    "ancient-romans scientists": "علماء رومان قدماء",
    "eastern european scientists": "علماء أوروبيون شرقيون",
    # {en_nat} artists
    "central american artists": "فنانون أمريكيون أوسطيون",
    "central asian artists": "فنانون آسيويون أوسطيون",
    # {en_nat} swimmers
    "east timorese swimmers": "سباحون تيموريون شرقيون",
    "federated states-of micronesia swimmers": "سباحون ميكرونيزيون",
    # {en_nat} journalists
    "bissau-guinean journalists": "صحفيون غينيون بيساويون",
    "anglo-irish journalists": "صحفيون أنجلو إيرلنديون",
    # {en_nat} runners
    "czechoslovak runners": "عداؤون تشيكوسلوفاكيون",
    "east german runners": "عداؤون ألمانيون شرقيون",
    # {en_nat} poets
    "bosnia and herzegovina poets": "شعراء بوسنيون",
    "chinese taipei poets": "شعراء تايبيون صينيون",
    # {en_nat} people by occupation and century
    "democratic-republic-of-congo people by occupation and century": "كونغويون ديمقراطيون حسب المهنة والقرن",
    "dominican republic people by occupation and century": "دومينيكانيون حسب المهنة والقرن",
    # {en_nat} film directors
    "eastern asian film directors": "مخرجو أفلام آسيويون شرقيون",
    "equatoguinean film directors": "مخرجو أفلام غينيون استوائيون",
    # {en_nat} educators
    "central african republic educators": "معلمون أفارقة أوسطيون",
    "equatorial guinean educators": "معلمون غينيون استوائيون",
    # {en_nat} competitors by sports event
    "ancient-romans competitors by sports event": "منافسون رومان قدماء حسب الحدث الرياضي",
    "eastern european competitors by sports event": "منافسون أوروبيون شرقيون حسب الحدث الرياضي",
    # {en_nat} academics
    "central american academics": "أكاديميون أمريكيون أوسطيون",
    "central asian academics": "أكاديميون آسيويون أوسطيون",
    # {en_nat} novelists
    "east timorese novelists": "روائيون تيموريون شرقيون",
    "federated states-of micronesia novelists": "روائيون ميكرونيزيون",
    # {en_nat} sprinters
    "bissau-guinean sprinters": "عداؤون سريعون غينيون بيساويون",
    "anglo-irish sprinters": "عداؤون سريعون أنجلو إيرلنديون",
    # {en_nat} criminals
    "czechoslovak criminals": "مجرمون تشيكوسلوفاكيون",
    "east german criminals": "مجرمون ألمانيون شرقيون",
    # {en_nat} murder victims
    "bosnia and herzegovina murder victims": "ضحايا قتل بوسنيون",
    "chinese taipei murder victims": "ضحايا قتل تايبيون صينيون",
    # {en_nat} roman catholics
    "democratic-republic-of-congo roman catholics": "رومان كاثوليك كونغويون ديمقراطيون",
    "dominican republic roman catholics": "رومان كاثوليك دومينيكانيون",
    # {en_nat} religious leaders
    "eastern asian religious leaders": "قادة دينيون آسيويون شرقيون",
    "equatoguinean religious leaders": "قادة دينيون غينيون استوائيون",
    # {en_nat} socialists
    "central african republic socialists": "اشتراكيون أفارقة أوسطيون",
    "equatorial guinean socialists": "اشتراكيون غينيون استوائيون",
    # {en_nat} judges
    "ancient-romans judges": "قضاة رومان قدماء",
    "eastern european judges": "قضاة أوروبيون شرقيون",
    # {en_nat} victims of crime
    "central american victims of crime": "ضحايا جرائم أمريكيون أوسطيون",
    "central asian victims of crime": "ضحايا جرائم آسيويون أوسطيون",
    # {en_nat} economists
    "east timorese economists": "اقتصاديون تيموريون شرقيون",
    "federated states-of micronesia economists": "اقتصاديون ميكرونيزيون",
    # {en_nat} mass media people
    "bissau-guinean mass media people": "إعلاميون غينيون بيساويون",
    "anglo-irish mass media people": "إعلاميون أنجلو إيرلنديون",
    # {en_nat} people by century and occupation
    "czechoslovak people by century and occupation": "تشيكوسلوفاكيون حسب القرن والمهنة",
    "east german people by century and occupation": "ألمانيون شرقيون حسب القرن والمهنة",
    # {en_nat} writers by century
    "bosnia and herzegovina writers by century": "كتاب بوسنيون حسب القرن",
    "chinese taipei writers by century": "كتاب تايبيون صينيون حسب القرن",
    # {en_nat} freestyle swimmers
    "democratic-republic-of-congo freestyle swimmers": "سباحو تزلج حر كونغويون ديمقراطيون",
    "dominican republic freestyle swimmers": "سباحو تزلج حر دومينيكانيون",
    # {en_nat} politicians by century
    "eastern asian politicians by century": "سياسيون آسيويون شرقيون حسب القرن",
    "equatoguinean politicians by century": "سياسيون غينيون استوائيون حسب القرن",
    # {en_nat} men's basketball players
    "central african republic men's basketball players": "لاعبو كرة سلة أفارقة أوسطيون",
    "equatorial guinean men's basketball players": "لاعبو كرة سلة غينيون استوائيون",
    # {en_nat} human rights activists
    "ancient-romans human rights activists": "رومان قدماء ناشطون في حقوق الإنسان",
    "eastern european human rights activists": "أوروبيون شرقيون ناشطون في حقوق الإنسان",
    # {en_nat} composers
    "central american composers": "ملحنون أمريكيون أوسطيون",
    "central asian composers": "ملحنون آسيويون أوسطيون",
    # {en_nat} physicians
    "east timorese physicians": "أطباء تيموريون شرقيون",
    "federated states-of micronesia physicians": "أطباء ميكرونيزيون",
    # {en_nat} feminists
    "bissau-guinean feminists": "نسويون غينيون بيساويون",
    "anglo-irish feminists": "نسويون أنجلو إيرلنديون",
    # {en_nat} historians
    "czechoslovak historians": "مؤرخون تشيكوسلوفاكيون",
    "east german historians": "مؤرخون ألمانيون شرقيون",
    # {en_nat} communists
    "bosnia and herzegovina communists": "شيوعيون بوسنيون",
    "chinese taipei communists": "شيوعيون تايبيون صينيون",
    # {en_nat} people of german descent
    "american people of german descent": "أمريكيون من أصل ألماني",
    "brazilian people of german descent": "برازيليون من أصل ألماني",
    # executed {en_nat} people
    "executed democratic-republic-of-congo people": "كونغويون ديمقراطيون أعدموا",
    "executed dominican republic people": "دومينيكانيون أعدموا",
    # {en_nat} models
    "eastern asian models": "عارضو أزياء آسيويون شرقيون",
    "equatoguinean models": "عارضو أزياء غينيون استوائيون",
    # {en_nat} painters
    "central african republic painters": "رسامون أفارقة أوسطيون",
    "equatorial guinean painters": "رسامون غينيون استوائيون",
    # {en_nat} bankers
    "ancient-romans bankers": "مصرفيون رومان قدماء",
    "eastern european bankers": "مصرفيون أوروبيون شرقيون",
    # {en_nat} people with disabilities
    "central american people with disabilities": "أمريكيون أوسطيون بإعاقات",
    "central asian people with disabilities": "آسيويون أوسطيون بإعاقات",
    # assassinated {en_nat} people
    "assassinated east timorese people": "تيموريون شرقيون مغتالون",
    "assassinated federated states-of micronesia people": "ميكرونيزيون مغتالون",
    # {en_nat} jews
    "bissau-guinean jews": "يهود غينيون بيساويون",
    "anglo-irish jews": "يهود أنجلو إيرلنديون",
    # {en_nat} theatre people
    "czechoslovak theatre people": "مسرحيون تشيكوسلوفاكيون",
    "east german theatre people": "مسرحيون ألمانيون شرقيون",
    # {en_nat} anti-communists
    "bosnia and herzegovina anti-communists": "بوسنيون مناهضون للشيوعية",
    "chinese taipei anti-communists": "تايبيون صينيون مناهضون للشيوعية",
    # {en_nat} prisoners sentenced to death
    "democratic-republic-of-congo prisoners sentenced to death": "مسجونون كونغويون ديمقراطيون حكم عليهم بالإعدام",
    "dominican republic prisoners sentenced to death": "مسجونون دومينيكانيون حكم عليهم بالإعدام",
    # {en_nat} designers
    "eastern asian designers": "مصممون آسيويون شرقيون",
    "equatoguinean designers": "مصممون غينيون استوائيون",
    # {en_nat} engineers
    "central african republic engineers": "مهندسون أفارقة أوسطيون",
    "equatorial guinean engineers": "مهندسون غينيون استوائيون",
    # {en_nat} short story writers
    "ancient-romans short story writers": "كتاب قصة قصيرة رومان قدماء",
    "eastern european short story writers": "كتاب قصة قصيرة أوروبيون شرقيون",
    # {en_nat} actors by century
    "central american actors by century": "ممثلون أمريكيون أوسطيون حسب القرن",
    "central asian actors by century": "ممثلون آسيويون أوسطيون حسب القرن",
    # {en_nat} murderers
    "east timorese murderers": "قتلة تيموريون شرقيون",
    "federated states-of micronesia murderers": "قتلة ميكرونيزيون",
    # {en_nat} producers
    "bissau-guinean producers": "منتجون غينيون بيساويون",
    "anglo-irish producers": "منتجون أنجلو إيرلنديون",
    # {en_nat} musicians by instrument
    "czechoslovak musicians by instrument": "موسيقيون تشيكوسلوفاكيون حسب الآلة",
    "east german musicians by instrument": "موسيقيون ألمانيون شرقيون حسب الآلة",
    # {en_nat} architects
    "bosnia and herzegovina architects": "معماريون بوسنيون",
    "chinese taipei architects": "معماريون تايبيون صينيون",
    # {en_nat} generals
    "democratic-republic-of-congo generals": "جنرالات كونغويون ديمقراطيون",
    "dominican republic generals": "جنرالات دومينيكانيون",
    # {en_nat} long-distance runners
    "eastern asian long-distance runners": "عداؤو مسافات طويلة آسيويون شرقيون",
    "equatoguinean long-distance runners": "عداؤو مسافات طويلة غينيون استوائيون",
    # {en_nat} middle-distance runners
    "central african republic middle-distance runners": "عداؤو مسافات متوسطة أفارقة أوسطيون",
    "equatorial guinean middle-distance runners": "عداؤو مسافات متوسطة غينيون استوائيون",
    # {en_nat} civil servants
    "ancient-romans civil servants": "موظفو خدمة مدنية رومان قدماء",
    "eastern european civil servants": "موظفو خدمة مدنية أوروبيون شرقيون",
    # {en_nat} nationalists
    "central american nationalists": "قوميون أمريكيون أوسطيون",
    "central asian nationalists": "قوميون آسيويون أوسطيون",
    # males with ذكور - {en_nat} male swimmers
    "east timorese male swimmers": "سباحون ذكور تيموريون شرقيون",
    "federated states-of micronesia male swimmers": "سباحون ذكور ميكرونيزيون",
    # {en_nat} male freestyle swimmers
    "bissau-guinean male freestyle swimmers": "سباحو تزلج حر ذكور غينيون بيساويون",
    "anglo-irish male freestyle swimmers": "سباحو تزلج حر ذكور أنجلو إيرلنديون",
    # {en_nat} male sprinters
    "czechoslovak male sprinters": "عداؤون سريعون ذكور تشيكوسلوفاكيون",
    "east german male sprinters": "عداؤون سريعون ذكور ألمانيون شرقيون",
    # males without ذكور - {en_nat} male martial artists
    "bosnia and herzegovina male martial artists": "ممارسو فنون قتالية ذكور بوسنيون",
    "chinese taipei male martial artists": "ممارسو فنون قتالية ذكور تايبيون صينيون",
    # {en_nat} male boxers
    "democratic-republic-of-congo male boxers": "ملاكمون ذكور كونغويون ديمقراطيون",
    "dominican republic male boxers": "ملاكمون ذكور دومينيكانيون",
    # {en_nat} male athletes
    "eastern asian male athletes": "لاعبو قوى ذكور آسيويون شرقيون",
    "equatoguinean male athletes": "لاعبو قوى ذكور غينيون استوائيون",
    # {en_nat} male actors
    "central african republic male actors": "ممثلون ذكور أفارقة أوسطيون",
    "equatorial guinean male actors": "ممثلون ذكور غينيون استوائيون",
    # {en_nat} male singers
    "ancient-romans male singers": "مغنون ذكور رومان قدماء",
    "eastern european male singers": "مغنون ذكور أوروبيون شرقيون",
    # {en_nat} male writers
    "central american male writers": "كتاب ذكور أمريكيون أوسطيون",
    "central asian male writers": "كتاب ذكور آسيويون أوسطيون",
    # {en_nat} male film actors
    "east timorese male film actors": "ممثلو أفلام ذكور تيموريون شرقيون",
    "federated states-of micronesia male film actors": "ممثلو أفلام ذكور ميكرونيزيون",
}

test_data_ar = {}

test_data_the_male = {}

test_data_male = {
    # {en_nat} diaspora
    "bosnia and herzegovina diaspora": "شتات بوسني",
    "chinese taipei diaspora": "شتات تايبي صيني",
}

test_data_female = {}

test_data_the_female = {}


@pytest.mark.parametrize("category, expected", test_data_males.items(), ids=test_data_males.keys())
@pytest.mark.fast
def test_p_resolve_males(category: str, expected: str) -> None:
    label = resolve_nat_males_pattern(category)
    assert label == expected


@pytest.mark.parametrize("category, expected", test_data_ar.items(), ids=test_data_ar.keys())
@pytest.mark.fast
def test_p_resolve_ar(category: str, expected: str) -> None:
    label = resolve_nat_males_pattern(category)
    assert label == expected


@pytest.mark.parametrize("category, expected", test_data_the_male.items(), ids=test_data_the_male.keys())
@pytest.mark.fast
def test_p_resolve_the_male(category: str, expected: str) -> None:
    label = resolve_nat_males_pattern(category)
    assert label == expected


@pytest.mark.parametrize("category, expected", test_data_male.items(), ids=test_data_male.keys())
@pytest.mark.fast
def test_p_resolve_male(category: str, expected: str) -> None:
    label = resolve_nat_males_pattern(category)
    assert label == expected


@pytest.mark.parametrize("category, expected", test_data_female.items(), ids=test_data_female.keys())
@pytest.mark.fast
def test_p_resolve_female(category: str, expected: str) -> None:
    label = resolve_nat_males_pattern(category)
    assert label == expected


@pytest.mark.parametrize("category, expected", test_data_the_female.items(), ids=test_data_the_female.keys())
@pytest.mark.fast
def test_p_resolve_the_female(category: str, expected: str) -> None:
    label = resolve_nat_males_pattern(category)
    assert label == expected


to_test = [
    ("test_p_resolve_males", test_data_males, resolve_nat_males_pattern),
    ("test_p_resolve_ar", test_data_ar, resolve_nat_males_pattern),
    ("test_p_resolve_the_male", test_data_the_male, resolve_nat_males_pattern),
    ("test_p_resolve_male", test_data_male, resolve_nat_males_pattern),
    ("test_p_resolve_female", test_data_female, resolve_nat_males_pattern),
    ("test_p_resolve_the_female", test_data_the_female, resolve_nat_males_pattern),
]

test_dump_all = make_dump_test_name_data_callback(to_test, run_same=True)

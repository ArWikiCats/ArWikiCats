"""
Tests
"""

import pytest
from load_one_data import dump_diff, one_dump_test

from ArWikiCats.main_processers.nat_men_pattern import resolve_nat_men_pattern, resolve_nat_men_pattern_new

_mens_data = {
    # standard - {en_nat} people
    "welsh people": "أعلام ويلزيون",
    "yemeni people": "أعلام يمنيون",
    "africanamerican people": "أعلام أمريكيون أفارقة",
    "american people": "أعلام أمريكيون",
    "argentine people": "أعلام أرجنتينيون",
    "australian people": "أعلام أستراليون",
    "austrian people": "أعلام نمساويون",
    "barbadian people": "أعلام بربادوسيون",
    "bhutanese people": "أعلام بوتانيون",
    "bolivian people": "أعلام بوليفيون",
    "botswana people": "أعلام بوتسوانيون",
    "cameroonian people": "أعلام كاميرونيون",
    "cape verdean people": "أعلام أخضريون",
    "central american people": "أعلام أمريكيون أوسطيون",
    "dutch people": "أعلام هولنديون",
    "english people": "أعلام إنجليز",
    "gambian people": "أعلام غامبيون",
    "german people": "أعلام ألمان",
    "indian people": "أعلام هنود",
    "iraqi people": "أعلام عراقيون",
    "italian people": "أعلام إيطاليون",
    "latvian people": "أعلام لاتفيون",
    "malagasy people": "أعلام مدغشقريون",
    "malaysian people": "أعلام ماليزيون",
    "mexican people": "أعلام مكسيكيون",
    "moldovan people": "أعلام مولدوفيون",
    "mongolian people": "أعلام منغوليون",
    "polish people": "أعلام بولنديون",
    "rhodesian people": "أعلام رودوسيون",
    "romanian people": "أعلام رومانيون",
    "salvadoran people": "أعلام سلفادوريون",
    "scottish people": "أعلام إسكتلنديون",
    "serbian people": "أعلام صرب",
    "somalian people": "أعلام صوماليون",
    "south african people": "أعلام جنوب إفريقيون",
    "sri lankan people": "أعلام سريلانكيون",
    "sudanese people": "أعلام سودانيون",
    "swedish people": "أعلام سويديون",
    "tajikistani people": "أعلام طاجيك",
    "togolese people": "أعلام توغويون",
    "turkish cypriot people": "أعلام قبرصيون شماليون",
    "turkish people": "أعلام أتراك",
    "ukrainian people": "أعلام أوكرانيون",

    # {en_nat} lgbtq people
    "albanian lgbtq people": "أعلام إل جي بي تي كيو ألبان",
    "bangladeshi lgbtq people": "أعلام إل جي بي تي كيو بنغلاديشيون",
    "german lgbtq people": "أعلام إل جي بي تي كيو ألمان",
    "jamaican lgbtq people": "أعلام إل جي بي تي كيو جامايكيون",
    "norwegian lgbtq people": "أعلام إل جي بي تي كيو نرويجيون",
    "sierra leonean lgbtq people": "أعلام إل جي بي تي كيو سيراليونيون",
    "south african lgbtq people": "أعلام إل جي بي تي كيو جنوب إفريقيون",
    "thai lgbtq people": "أعلام إل جي بي تي كيو تايلنديون",
    "tunisian lgbtq people": "أعلام إل جي بي تي كيو تونسيون",
    "native american people": "أعلام أمريكيون أصليون",

    # {en_nat} political people
    "libyan political people": "ساسة ليبيون",
    "south african political people": "ساسة جنوب إفريقيون",
    "egyptian political people": "ساسة مصريون",

    # {en_nat} people by occupation
    "german people by occupation": "ألمان حسب المهنة",
    "egyptian people by occupation": "مصريون حسب المهنة",

    # {en_nat} sports-people
    "german sports-people": "رياضيون ألمان",
    "egyptian sports-people": "رياضيون مصريون",
    "brazilian sports-people": "رياضيون برازيليون",

    # {en_nat} men
    "german men": "رجال ألمان",
    "egyptian men": "رجال مصريون",

    # {en_nat} sportsmen
    "german sportsmen": "رياضيون رجال ألمان",
    "egyptian sportsmen": "رياضيون رجال مصريون",

    # {en_nat} people in sports
    "german people in sports": "ألمان في ألعاب رياضية",
    "egyptian people in sports": "مصريون في ألعاب رياضية",

    # {en_nat} people by ethnic or national origin
    "german people by ethnic or national origin": "ألمان حسب الأصل العرقي أو الوطني",
    "egyptian people by ethnic or national origin": "مصريون حسب الأصل العرقي أو الوطني",

    # {en_nat} expatriates
    "german expatriates": "ألمان مغتربون",
    "egyptian expatriates": "مصريون مغتربون",

    # {en_nat} men by occupation
    "german men by occupation": "رجال ألمان حسب المهنة",
    "egyptian men by occupation": "رجال مصريون حسب المهنة",

    # {en_nat} people by descent
    "german people by descent": "ألمان حسب الأصل العرقي أو الوطني",
    "egyptian people by descent": "مصريون حسب الأصل العرقي أو الوطني",

    # {en_nat} writers
    "german writers": "كتاب ألمان",
    "egyptian writers": "كتاب مصريون",

    # {en_nat} politicians
    "german politicians": "سياسيون ألمان",
    "egyptian politicians": "سياسيون مصريون",

    # {en_nat} sports-people by sport
    "german sports-people by sport": "رياضيون ألمان حسب الرياضة",
    "egyptian sports-people by sport": "رياضيون مصريون حسب الرياضة",

    # {en_nat} expatriate sports-people
    "german expatriate sports-people": "رياضيون ألمان مغتربون",
    "egyptian expatriate sports-people": "رياضيون مصريون مغتربون",

    # {en_nat} musicians
    "german musicians": "موسيقيون ألمان",
    "egyptian musicians": "موسيقيون مصريون",

    # {en_nat} people by religion
    "german people by religion": "ألمان حسب الدين",
    "egyptian people by religion": "مصريون حسب الدين",

    # {en_nat} expatriate sports-people by country of residence
    "german expatriate sports-people by country of residence": "رياضيون ألمان مغتربون حسب بلد الإقامة",
    "egyptian expatriate sports-people by country of residence": "رياضيون مصريون مغتربون حسب بلد الإقامة",

    # {en_nat} men's footballers
    "german men's footballers": "لاعبو كرة قدم ألمان",
    "egyptian men's footballers": "لاعبو كرة قدم مصريون",

    # {en_nat} diplomats
    "german diplomats": "دبلوماسيون ألمان",
    "egyptian diplomats": "دبلوماسيون مصريون",

    # {en_nat} emigrants
    "german emigrants": "ألمان مهاجرون",
    "egyptian emigrants": "مصريون مهاجرون",

    # {en_nat} expatriate men's footballers
    "german expatriate men's footballers": "لاعبو كرة قدم ألمان مغتربون",
    "egyptian expatriate men's footballers": "لاعبو كرة قدم مصريون مغتربون",

    # {en_nat} people by century
    "german people by century": "ألمان حسب القرن",
    "egyptian people by century": "مصريون حسب القرن",

    # {en_nat} people by political orientation
    "german people by political orientation": "ألمان حسب التوجه السياسي",
    "egyptian people by political orientation": "مصريون حسب التوجه السياسي",

    # {en_nat} military personnel
    "german military personnel": "عسكريون ألمان",
    "egyptian military personnel": "عسكريون مصريون",

    # {en_nat} activists
    "german activists": "ناشطون ألمان",
    "egyptian activists": "ناشطون مصريون",

    # {en_nat} lawyers
    "german lawyers": "محامون ألمان",
    "egyptian lawyers": "محامون مصريون",

    # {en_nat} athletes
    "german athletes": "لاعبو قوى ألمان",
    "egyptian athletes": "لاعبو قوى مصريون",

    # {en_nat} football managers
    "german football managers": "مدربو كرة قدم ألمان",
    "egyptian football managers": "مدربو كرة قدم مصريون",

    # {en_nat} martial artists
    "german martial artists": "ممارسو وممارسات فنون قتالية ألمان",
    "egyptian martial artists": "ممارسو وممارسات فنون قتالية مصريون",

    # {en_nat} prisoners and detainees
    "german prisoners and detainees": "سجناء ومعتقلون ألمان",
    "egyptian prisoners and detainees": "سجناء ومعتقلون مصريون",

    # {en_nat} scientists
    "german scientists": "علماء ألمان",
    "egyptian scientists": "علماء مصريون",

    # {en_nat} artists
    "german artists": "فنانون ألمان",
    "egyptian artists": "فنانون مصريون",

    # {en_nat} swimmers
    "german swimmers": "سباحون ألمان",
    "egyptian swimmers": "سباحون مصريون",

    # {en_nat} journalists
    "german journalists": "صحفيون ألمان",
    "egyptian journalists": "صحفيون مصريون",

    # {en_nat} runners
    "german runners": "عداؤون ألمان",
    "egyptian runners": "عداؤون مصريون",

    # {en_nat} poets
    "german poets": "شعراء ألمان",
    "egyptian poets": "شعراء مصريون",

    # {en_nat} people by occupation and century
    "german people by occupation and century": "ألمان حسب المهنة والقرن",
    "egyptian people by occupation and century": "مصريون حسب المهنة والقرن",

    # {en_nat} film directors
    "german film directors": "مخرجو أفلام ألمان",
    "egyptian film directors": "مخرجو أفلام مصريون",

    # {en_nat} educators
    "german educators": "معلمون ألمان",
    "egyptian educators": "معلمون مصريون",

    # {en_nat} competitors by sports event
    "german competitors by sports event": "منافسون ألمان حسب الحدث الرياضي",
    "egyptian competitors by sports event": "منافسون مصريون حسب الحدث الرياضي",

    # {en_nat} academics
    "german academics": "أكاديميون ألمان",
    "egyptian academics": "أكاديميون مصريون",

    # {en_nat} novelists
    "german novelists": "روائيون ألمان",
    "egyptian novelists": "روائيون مصريون",

    # {en_nat} sprinters
    "german sprinters": "عداؤون سريعون ألمان",
    "egyptian sprinters": "عداؤون سريعون مصريون",

    # {en_nat} criminals
    "german criminals": "مجرمون ألمان",
    "egyptian criminals": "مجرمون مصريون",

    # {en_nat} murder victims
    "german murder victims": "ضحايا قتل ألمان",
    "egyptian murder victims": "ضحايا قتل مصريون",

    # {en_nat} roman catholics
    "german roman catholics": "رومان كاثوليك ألمان",
    "egyptian roman catholics": "رومان كاثوليك مصريون",

    # {en_nat} religious leaders
    "german religious leaders": "قادة دينيون ألمان",
    "egyptian religious leaders": "قادة دينيون مصريون",

    # {en_nat} socialists
    "german socialists": "اشتراكيون ألمان",
    "egyptian socialists": "اشتراكيون مصريون",

    # {en_nat} judges
    "german judges": "قضاة ألمان",
    "egyptian judges": "قضاة مصريون",

    # {en_nat} victims of crime
    "german victims of crime": "ضحايا جرائم ألمان",
    "egyptian victims of crime": "ضحايا جرائم مصريون",

    # {en_nat} economists
    "german economists": "اقتصاديون ألمان",
    "egyptian economists": "اقتصاديون مصريون",

    # {en_nat} mass media people
    "german mass media people": "إعلاميون ألمان",
    "egyptian mass media people": "إعلاميون مصريون",

    # {en_nat} people by century and occupation
    "german people by century and occupation": "ألمان حسب القرن والمهنة",
    "egyptian people by century and occupation": "مصريون حسب القرن والمهنة",

    # {en_nat} writers by century
    "german writers by century": "كتاب ألمان حسب القرن",
    "egyptian writers by century": "كتاب مصريون حسب القرن",

    # {en_nat} freestyle swimmers
    "german freestyle swimmers": "سباحو تزلج حر ألمان",
    "egyptian freestyle swimmers": "سباحو تزلج حر مصريون",

    # {en_nat} politicians by century
    "german politicians by century": "سياسيون ألمان حسب القرن",
    "egyptian politicians by century": "سياسيون مصريون حسب القرن",

    # {en_nat} men's basketball players
    "german men's basketball players": "لاعبو كرة سلة ألمان",
    "egyptian men's basketball players": "لاعبو كرة سلة مصريون",

    # {en_nat} human rights activists
    "german human rights activists": "ألمان ناشطون في حقوق الإنسان",
    "egyptian human rights activists": "مصريون ناشطون في حقوق الإنسان",

    # {en_nat} composers
    "german composers": "ملحنون ألمان",
    "egyptian composers": "ملحنون مصريون",

    # {en_nat} physicians
    "german physicians": "أطباء ألمان",
    "egyptian physicians": "أطباء مصريون",

    # {en_nat} feminists
    "german feminists": "نسويون ألمان",
    "egyptian feminists": "نسويون مصريون",

    # {en_nat} historians
    "german historians": "مؤرخون ألمان",
    "egyptian historians": "مؤرخون مصريون",

    # {en_nat} communists
    "german communists": "شيوعيون ألمان",
    "egyptian communists": "شيوعيون مصريون",

    # {en_nat} people of german descent
    "american people of german descent": "أمريكيون من أصل ألماني",
    "brazilian people of german descent": "برازيليون من أصل ألماني",

    # executed {en_nat} people
    "executed german people": "ألمان معدومون",
    "executed egyptian people": "مصريون معدومون",

    # {en_nat} models
    "german models": "عارضو أزياء ألمان",
    "egyptian models": "عارضو أزياء مصريون",

    # {en_nat} painters
    "german painters": "رسامون ألمان",
    "egyptian painters": "رسامون مصريون",

    # {en_nat} bankers
    "german bankers": "مصرفيون ألمان",
    "egyptian bankers": "مصرفيون مصريون",

    # {en_nat} people with disabilities
    "german people with disabilities": "ألمان بإعاقات",
    "egyptian people with disabilities": "مصريون بإعاقات",

    # assassinated {en_nat} people
    "assassinated german people": "ألمان مغتالون",
    "assassinated egyptian people": "مصريون مغتالون",

    # {en_nat} jews
    "german jews": "يهود ألمان",
    "egyptian jews": "يهود مصريون",

    # {en_nat} theatre people
    "german theatre people": "مسرحيون ألمان",
    "egyptian theatre people": "مسرحيون مصريون",

    # {en_nat} anti-communists
    "german anti-communists": "ألمان مناهضون للشيوعية",
    "egyptian anti-communists": "مصريون مناهضون للشيوعية",

    # {en_nat} prisoners sentenced to death
    "german prisoners sentenced to death": "مسجونون ألمان حكم عليهم بالإعدام",
    "egyptian prisoners sentenced to death": "مسجونون مصريون حكم عليهم بالإعدام",

    # {en_nat} designers
    "german designers": "مصممون ألمان",
    "egyptian designers": "مصممون مصريون",

    # {en_nat} engineers
    "german engineers": "مهندسون ألمان",
    "egyptian engineers": "مهندسون مصريون",

    # {en_nat} short story writers
    "german short story writers": "كتاب قصة قصيرة ألمان",
    "egyptian short story writers": "كتاب قصة قصيرة مصريون",

    # {en_nat} actors by century
    "german actors by century": "ممثلون ألمان حسب القرن",
    "egyptian actors by century": "ممثلون مصريون حسب القرن",

    # {en_nat} murderers
    "german murderers": "قتلة ألمان",
    "egyptian murderers": "قتلة مصريون",

    # {en_nat} producers
    "german producers": "منتجون ألمان",
    "egyptian producers": "منتجون مصريون",

    # {en_nat} musicians by instrument
    "german musicians by instrument": "موسيقيون ألمان حسب الآلة",
    "egyptian musicians by instrument": "موسيقيون مصريون حسب الآلة",

    # {en_nat} architects
    "german architects": "معماريون ألمان",
    "egyptian architects": "معماريون مصريون",

    # {en_nat} generals
    "german generals": "جنرالات ألمان",
    "egyptian generals": "جنرالات مصريون",

    # {en_nat} long-distance runners
    "german long-distance runners": "عداؤو مسافات طويلة ألمان",
    "egyptian long-distance runners": "عداؤو مسافات طويلة مصريون",

    # {en_nat} middle-distance runners
    "german middle-distance runners": "عداؤو مسافات متوسطة ألمان",
    "egyptian middle-distance runners": "عداؤو مسافات متوسطة مصريون",

    # {en_nat} civil servants
    "german civil servants": "موظفو خدمة مدنية ألمان",
    "egyptian civil servants": "موظفو خدمة مدنية مصريون",

    # {en_nat} nationalists
    "german nationalists": "قوميون ألمان",
    "egyptian nationalists": "قوميون مصريون",

    # males with ذكور - {en_nat} male swimmers
    "german male swimmers": "سباحون ذكور ألمان",
    "egyptian male swimmers": "سباحون ذكور مصريون",

    # {en_nat} male freestyle swimmers
    "german male freestyle swimmers": "سباحو تزلج حر ذكور ألمان",
    "egyptian male freestyle swimmers": "سباحو تزلج حر ذكور مصريون",

    # {en_nat} male sprinters
    "german male sprinters": "عداؤون سريعون ذكور ألمان",
    "egyptian male sprinters": "عداؤون سريعون ذكور مصريون",

    # males without ذكور - {en_nat} male martial artists
    "german male martial artists": "ممارسو فنون قتالية ذكور ألمان",
    "egyptian male martial artists": "ممارسو فنون قتالية ذكور مصريون",

    # {en_nat} male boxers
    "german male boxers": "ملاكمون ذكور ألمان",
    "egyptian male boxers": "ملاكمون ذكور مصريون",

    # {en_nat} male athletes
    "german male athletes": "لاعبو قوى ذكور ألمان",
    "egyptian male athletes": "لاعبو قوى ذكور مصريون",

    # {en_nat} male actors
    "german male actors": "ممثلون ذكور ألمان",
    "egyptian male actors": "ممثلون ذكور مصريون",

    # {en_nat} male singers
    "german male singers": "مغنون ذكور ألمان",
    "egyptian male singers": "مغنون ذكور مصريون",

    # {en_nat} male writers
    "german male writers": "كتاب ذكور ألمان",
    "egyptian male writers": "كتاب ذكور مصريون",    # {en_nat} male film actors
    "german male film actors": "ممثلو أفلام ذكور ألمان",
    "egyptian male film actors": "ممثلو أفلام ذكور مصريون",

    # {en_nat} christians
    "german christians": "مسيحيون ألمان",
    "egyptian christians": "مسيحيون مصريون",
    "american christians": "مسيحيون أمريكيون",

    # {en_nat} muslims
    "german muslims": "مسلمون ألمان",
    "egyptian muslims": "مسلمون مصريون",
    "american muslims": "مسلمون أمريكيون",

    # {en_nat} diaspora in united states
    "german diaspora in united states": "أمريكيون ألمان",
    "egyptian diaspora in united states": "أمريكيون مصريون",
    "italian diaspora in united states": "أمريكيون إيطاليون",

    # {en_nat} sports coaches
    "german sports coaches": "مدربون رياضيون ألمان",
    "egyptian sports coaches": "مدربون رياضيون مصريون",
    "brazilian sports coaches": "مدربون رياضيون برازيليون",
}


@pytest.mark.parametrize("category,expected", _mens_data.items(), ids=_mens_data.keys())
def test_nat_pattern(category: str, expected: str) -> None:
    """Test all nat translation patterns."""
    result = resolve_nat_men_pattern(category)
    assert result == expected


to_test = [
    ("test_nat_pattern", _mens_data, resolve_nat_men_pattern),
    ("test_nat_pattern_new", _mens_data, resolve_nat_men_pattern_new),
]


@pytest.mark.parametrize("name,data,callback", to_test)
@pytest.mark.dump
def test_dump_all(name: str, data: dict[str, str], callback) -> None:
    expected, diff_result = one_dump_test(data, callback)
    dump_diff(diff_result, name)
    assert diff_result == expected, f"Differences found: {len(diff_result):,}, len all :{len(data):,}"

"""
Tests for army2 resolver - comprehensive coverage of all patterns and countries
"""

import pytest

from ArWikiCats.translations_resolvers_v2.army2 import resolve_secretaries_labels

fast_data = {
    # US specific pattern
    "United States secretaries of state": "وزراء خارجية أمريكيون",

    # Secretaries of state patterns - all countries from _all_country_with_nat
    "secretaries of state of eastern asian": "وزراء خارجية آسيويين شرقيون",
    "secretaries of state of eastern european": "وزراء خارجية أوروبيون شرقيون",
    "secretaries of state of ecuadorian": "وزراء خارجية إكوادوريون",
    "secretaries of state of egyptian": "وزراء خارجية مصريون",
    "secretaries of state of emirati": "وزراء خارجية إماراتيون",
    "secretaries of state of emiri": "وزراء خارجية إماراتيون",
    "secretaries of state of emirian": "وزراء خارجية إماراتيون",
    "secretaries of state of english": "وزراء خارجية إنجليز",
    "secretaries of state of equatoguinean": "وزراء خارجية غينيون استوائيون",
    "secretaries of state of equatorial guinean": "وزراء خارجية غينيون استوائيون",

    "secretaries of state for egyptian": "وزراء خارجية مصريون",
    "secretaries of state for emirati": "وزراء خارجية إماراتيون",
    "secretaries of state for english": "وزراء خارجية إنجليز",
    "secretaries of state for ecuadorian": "وزراء خارجية إكوادوريون",

    # Assistant secretaries patterns - multiple countries
    "egyptian assistant secretaries of defense": "مساعدو وزير الدفاع المصري",
    "emirati assistant secretaries of interior": "مساعدو وزير الداخلية الإماراتي",
    "english assistant secretaries of health": "مساعدو وزير الصحة الإنجليزي",
    "ecuadorian assistant secretaries of education": "مساعدو وزير التعليم الإكوادوري",
    "eastern asian assistant secretaries of finance": "مساعدو وزير المالية الآسيوي الشرقي",
    "eastern european assistant secretaries of defense": "مساعدو وزير الدفاع الأوروبي الشرقي",
    "equatorial guinean assistant secretaries of agriculture": "مساعدو وزير الزراعة الغيني الاستوائي",

    # Deputy secretaries patterns - multiple countries
    "egyptian deputy secretaries of defense": "نواب وزير الدفاع المصري",
    "emirati deputy secretaries of interior": "نواب وزير الداخلية الإماراتي",
    "english deputy secretaries of health": "نواب وزير الصحة الإنجليزي",
    "ecuadorian deputy secretaries of finance": "نواب وزير المالية الإكوادوري",
    "eastern asian deputy secretaries of economy": "نواب وزير الاقتصاد الآسيوي الشرقي",
    "eastern european deputy secretaries of culture": "نواب وزير الثقافة الأوروبي الشرقي",

    # Under secretaries patterns - multiple countries
    "egyptian under secretaries of defense": "نواب وزير الدفاع المصري",
    "emirati under secretaries of interior": "نواب وزير الداخلية الإماراتي",
    "english under secretaries of education": "نواب وزير التعليم الإنجليزي",
    "ecuadorian under secretaries of agriculture": "نواب وزير الزراعة الإكوادوري",
    "eastern asian under secretaries of transport": "نواب وزير النقل الآسيوي الشرقي",

    # Country secretaries of ministry patterns - Egyptian
    "egyptian secretaries of defense": "وزراء دفاع مصريون",
    "egyptian secretaries of interior": "وزراء داخلية مصريون",
    "egyptian secretaries of health": "وزراء صحة مصريون",
    "egyptian secretaries of education": "وزراء تعليم مصريون",
    "egyptian secretaries of agriculture": "وزراء زراعة مصريون",
    "egyptian secretaries of finance": "وزراء مالية مصريون",
    "egyptian secretaries of culture": "وزراء ثقافة مصريون",
    "egyptian secretaries of tourism": "وزراء سياحة مصريون",

    # Country secretaries of ministry patterns - Emirati
    "emirati secretaries of defense": "وزراء دفاع إماراتيون",
    "emirati secretaries of interior": "وزراء داخلية إماراتيون",
    "emirati secretaries of foreign affairs": "وزراء شؤون خارجية إماراتيون",
    "emirati secretaries of energy": "وزراء طاقة إماراتيون",
    "emirati secretaries of economy": "وزراء اقتصاد إماراتيون",

    # Country secretaries of ministry patterns - English
    "english secretaries of defense": "وزراء دفاع إنجليز",
    "english secretaries of health": "وزراء صحة إنجليز",
    "english secretaries of education": "وزراء تعليم إنجليز",
    "english secretaries of foreign affairs": "وزراء شؤون خارجية إنجليز",
    "english secretaries of justice": "وزراء عدل إنجليز",

    # Country secretaries of ministry patterns - Ecuadorian
    "ecuadorian secretaries of agriculture": "وزراء زراعة إكوادوريون",
    "ecuadorian secretaries of finance": "وزراء مالية إكوادوريون",
    "ecuadorian secretaries of defense": "وزراء دفاع إكوادوريون",
    "ecuadorian secretaries of environment": "وزراء بيئة إكوادوريون",

    # Country secretaries of ministry patterns - Eastern Asian
    "eastern asian secretaries of finance": "وزراء مالية آسيويين شرقيون",
    "eastern asian secretaries of defense": "وزراء دفاع آسيويين شرقيون",
    "eastern asian secretaries of economy": "وزراء اقتصاد آسيويين شرقيون",

    # Country secretaries of ministry patterns - Eastern European
    "eastern european secretaries of defense": "وزراء دفاع أوروبيون شرقيون",
    "eastern european secretaries of interior": "وزراء داخلية أوروبيون شرقيون",
    "eastern european secretaries of culture": "وزراء ثقافة أوروبيون شرقيون",

    # Country secretaries of ministry patterns - Equatorial Guinean
    "equatorial guinean secretaries of defense": "وزراء دفاع غينيون استوائيون",
    "equatorial guinean secretaries of agriculture": "وزراء زراعة غينيون استوائيون",
    "equatorial guinean secretaries of health": "وزراء صحة غينيون استوائيون",

    # Secretaries of ministry of country patterns
    "secretaries of defense of egyptian": "وزراء دفاع مصريون",
    "secretaries of interior of emirati": "وزراء داخلية إماراتيون",
    "secretaries of health of english": "وزراء صحة إنجليز",
    "secretaries of agriculture of ecuadorian": "وزراء زراعة إكوادوريون",
    "secretaries of finance of eastern asian": "وزراء مالية آسيويين شرقيون",
    "secretaries of culture of eastern european": "وزراء ثقافة أوروبيون شرقيون",
    "secretaries of education of egyptian": "وزراء تعليم مصريون",

    # Secretaries of ministry (no country) - all ministries
    "secretaries of defense": "وزراء دفاع",
    "secretaries of interior": "وزراء داخلية",
    "secretaries of health": "وزراء صحة",
    "secretaries of education": "وزراء تعليم",
    "secretaries of agriculture": "وزراء زراعة",
    "secretaries of navy": "وزراء بحرية",
    "secretaries of veterans affairs": "وزراء شؤون محاربين قدامى",
    "secretaries of veterans and military families": "وزراء شؤون محاربين قدامى",
    "secretaries of military affairs": "وزراء شؤون عسكرية",
    "secretaries of constitutional affairs": "وزراء شؤون دستورية",
    "secretaries of treasury": "وزراء خزانة",
    "secretaries of homeland security": "وزراء أمن داخلي",
    "secretaries of transportation": "وزراء نقل",
    "secretaries of energy": "وزراء طاقة",
    "secretaries of environment": "وزراء بيئة",
    "secretaries of finance": "وزراء مالية",
    "secretaries of commerce": "وزراء تجارة",
    "secretaries of trade": "وزراء تجارة",
    "secretaries of justice": "وزراء عدل",
    "secretaries of foreign affairs": "وزراء شؤون خارجية",
    "secretaries of foreign": "وزراء خارجية",
    "secretaries of culture": "وزراء ثقافة",
    "secretaries of economy": "وزراء اقتصاد",
    "secretaries of fisheries": "وزراء ثروة سمكية",
    "secretaries of human rights": "وزراء حقوق الإنسان",
    "secretaries of immigration": "وزراء هجرة",
    "secretaries of industry": "وزراء صناعة",
    "secretaries of information": "وزراء إعلام",
    "secretaries of infrastructure": "وزراء بنية تحتية",
    "secretaries of intelligence": "وزراء مخابرات",
    "secretaries of labor": "وزراء عمل",
    "secretaries of labour": "وزراء عمل",
    "secretaries of mining": "وزراء تعدين",
    "secretaries of oil": "وزراء بترول",
    "secretaries of security": "وزراء أمن",
    "secretaries of nuclear security": "وزراء أمن نووي",
    "secretaries of sports": "وزراء رياضة",
    "secretaries of technology": "وزراء تقانة",
    "secretaries of tourism": "وزراء سياحة",
    "secretaries of water": "وزراء مياه",
    "secretaries of army": "وزراء جيش",
    "secretaries of war": "وزراء حرب",
    "secretaries of construction": "وزراء بناء",
    "secretaries of communication": "وزراء اتصالات",
    "secretaries of communications": "وزراء اتصالات",
    "secretaries of climate change": "وزراء تغير المناخ",
    "secretaries of national defence": "وزراء دفاع وطني",
    "secretaries of defence": "وزراء دفاع",
    "secretaries of family": "وزراء أسرة",
    "secretaries of internal affairs": "وزراء شؤون داخلية",
    "secretaries of indigenous affairs": "وزراء شؤون سكان أصليين",
    "secretaries of maritime affairs": "وزراء شؤون بحرية",
    "secretaries of social security": "وزراء ضمان اجتماعي",
    "secretaries of social affairs": "وزراء شؤون اجتماعية",
    "secretaries of gender equality": "وزراء المساواة بين الجنسين",
    "secretaries of colonial": "وزراء إستعمار",
    "secretaries of broadcasting": "وزراء إذاعة",
    "secretaries of land management": "وزراء إدارة أراضي",
    "secretaries of housing": "وزراء إسكان",
    "secretaries of housing and urban development": "وزراء إسكان وتنمية حضرية",
    "secretaries of public safety": "وزراء سلامة عامة",
    "secretaries of planning": "وزراء تخطيط",
    "secretaries of diaspora": "وزراء شتات",
    "secretaries of urban development": "وزراء تخطيط عمراني",
    "secretaries of law": "وزراء قانون",
    "secretaries of prisons": "وزراء سجون",
    "secretaries of public works": "وزراء أشغال عامة",
    "secretaries of research": "وزراء أبحاث",
    "secretaries of science": "وزراء العلم",
    "secretaries of civil service": "وزراء خدمة مدنية",
    "secretaries of irrigation": "وزراء ري",
    "secretaries of natural resources": "وزراء موارد طبيعية",
    "secretaries of religious affairs": "وزراء شؤون دينية",
    "secretaries of foreign trade": "وزراء تجارة خارجية",
    "secretaries of transport": "وزراء نقل",
    "secretaries of women's": "وزراء شؤون المرأة",
    "secretaries of public service": "وزراء خدمة عامة",
    "secretaries of human services": "وزراء خدمات إنسانية",
    "secretaries of peace and reconciliation": "وزراء سلام ومصالحة",

    # State-level positions - multiple countries
    "state lieutenant governors of egypt": "نواب حكام الولايات في مصر",
    "state lieutenant governors of united arab emirates": "نواب حكام الولايات في الإمارات العربية المتحدة",
    "state lieutenant governors of ecuador": "نواب حكام الولايات في الإكوادور",
    "state lieutenant governors of england": "نواب حكام الولايات في إنجلترا",

    "state secretaries of state of egypt": "وزراء خارجية الولايات في مصر",
    "state secretaries of state of united arab emirates": "وزراء خارجية الولايات في الإمارات العربية المتحدة",
    "state secretaries of state of ecuador": "وزراء خارجية الولايات في الإكوادور",

    "state cabinet secretaries of egypt": "أعضاء مجلس وزراء مصر",
    "state cabinet secretaries of united arab emirates": "أعضاء مجلس وزراء الإمارات العربية المتحدة",
    "state cabinet secretaries of ecuador": "أعضاء مجلس وزراء الإكوادور",
    "state cabinet secretaries of england": "أعضاء مجلس وزراء إنجلترا",

    # Hyphenated patterns - multiple countries and ministries
    "United States secretaries-of war": "وزراء حرب أمريكيون",
    "egyptian secretaries-of defense": "وزراء دفاع مصريون",
    "emirati secretaries-of interior": "وزراء داخلية إماراتيون",
    "english secretaries-of health": "وزراء صحة إنجليز",
    "ecuadorian secretaries-of agriculture": "وزراء زراعة إكوادوريون",
    "eastern asian secretaries-of finance": "وزراء مالية آسيويين شرقيون",

    "secretaries-of defense of egyptian": "وزراء دفاع مصريون",
    "secretaries-of interior of emirati": "وزراء داخلية إماراتيون",
    "secretaries-of health of english": "وزراء صحة إنجليز",
    "secretaries-of war": "وزراء حرب",
    "secretaries-of defense": "وزراء دفاع",

    # Combined ministries (ministry1 and ministry2)
    "secretaries of health and human services": "وزراء صحة وخدمات إنسانية",
    "secretaries of communications and transportation": "وزراء اتصالات ونقل",
    "secretaries of environment and natural resources": "وزراء بيئة وموارد طبيعية",
    "secretaries of war and navy": "وزراء حرب وبحرية",

    # Combined ministries with countries
    "egyptian secretaries of health and human services": "وزراء صحة وخدمات إنسانية مصريون",
    "emirati secretaries of communications and transportation": "وزراء اتصالات ونقل إماراتيون",
    "english secretaries of environment and natural resources": "وزراء بيئة وموارد طبيعية إنجليز",

    # Case sensitivity tests
    "EGYPTIAN SECRETARIES OF DEFENSE": "وزراء دفاع مصريون",
    "Egyptian Secretaries Of Defense": "وزراء دفاع مصريون",
    "eMiRaTi SeCrEtArIeS oF iNtErIoR": "وزراء داخلية إماراتيون",

    # Testing with "the" prefix removal
    "secretaries of state of the egypt": "وزراء خارجية مصريون",
    "secretaries of state of the united arab emirates": "وزراء خارجية إماراتيون",
}


@pytest.mark.parametrize("category, expected", fast_data.items(), ids=list(fast_data.keys()))
@pytest.mark.fast
def test_fast_data(category: str, expected: str) -> None:
    label = resolve_secretaries_labels(category)
    assert label == expected

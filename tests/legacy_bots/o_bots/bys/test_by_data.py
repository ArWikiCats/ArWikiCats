"""

"""

import pytest
from load_one_data import dump_diff, dump_same_and_not_same, one_dump_test

from ArWikiCats.legacy_bots.o_bots.bys import by_people_bot
from ArWikiCats.new_resolvers.bys_new import resolve_by_labels

data_0 = {"by football team": "حسب فريق كرة القدم"}

by_data_peoples = {
    "by abraham lincoln": "بواسطة أبراهام لينكون",
    "by andrea mantegna": "بواسطة أندريا مانتينيا",
    "by benjamin britten": "بواسطة بنجامين بريتن",
    "by bob dylan": "بواسطة بوب ديلن",
    "by béla bartók": "بواسطة بيلا بارتوك",
    "by camille saint-saëns": "بواسطة كامي سان صانز",
    "by carl nielsen": "بواسطة كارل نيلسن",
    "by charles edward stuart": "بواسطة تشارلز إدوارد ستيوارت",
    "by charles mingus": "بواسطة شارليس مينغوس",
    "by don costa": "بواسطة دون كوستا",
    "by donald trump": "بواسطة دونالد ترمب",
    "by edgar degas": "بواسطة إدغار ديغا",
    "by edward elgar": "بواسطة إدوارد إلجار",
    "by edward iv": "بواسطة إدوارد الرابع ملك إنجلترا",
    "by edward viii": "بواسطة إدوارد الثامن ملك المملكة المتحدة",
    "by felix mendelssohn": "بواسطة فيلكس مندلسون",
    "by frank zappa": "بواسطة فرانك زابا",
    "by franklin pierce": "بواسطة فرانكلين بيرس",
    "by frederick douglass": "بواسطة فريدريك دوغلاس",
    "by george gershwin": "بواسطة جورج غيرشوين",
    "by george ii of great britain": "بواسطة جورج الثاني ملك بريطانيا العظمى",
    "by george vi": "بواسطة جورج السادس ملك المملكة المتحدة",
    "by gertrude stein": "بواسطة جيرترود شتاين",
    "by harvey kurtzman": "بواسطة هارفي كورتزمان",
    "by hieronymus bosch": "بواسطة هيرونيموس بوس",
    "by jack london": "بواسطة جاك لندن",
    "by jacob van ruisdael": "بواسطة جاكوب فان روسيدل",
    "by jacques offenbach": "بواسطة جاك أوفنباخ",
    "by jawaharlal nehru": "بواسطة جواهر لال نهرو",
    "by jerome robbins": "بواسطة جيرومي روبين",
    "by jimmy carter": "بواسطة جيمي كارتر",
    "by joe biden": "بواسطة جو بايدن",
    "by johannes brahms": "بواسطة يوهانس برامس",
    "by johannes vermeer": "بواسطة يوهانس فيرمير",
    "by john tyler": "بواسطة جون تايلر",
    "by louis xv": "بواسطة لويس الخامس عشر ملك فرنسا",
    "by louis xvi": "بواسطة لويس السادس عشر ملك فرنسا في فرنسا",
    "by m. r. james": "بواسطة إم. جيمس",
    "by matt damon": "بواسطة مات ديمون",
    "by muhammad": "بواسطة محمد",
    "by nadine gordimer": "بواسطة نادين غورديمير",
    "by napoleon": "بواسطة نابليون",
    "by nikolai rimsky-korsakov": "بواسطة نيكولاي ريمسكي كورساكوف",
    "by norman rockwell": "بواسطة نورمان روكويل",
    "by pablo picasso": "بواسطة بابلو بيكاسو",
    "by pope clement xiv": "بواسطة كليمنت الرابع عشر",
    "by pope gregory xvi": "بواسطة غريغوري السادس عشر",
    "by pope honorius iii": "بواسطة هونريوس الثالث",
    "by pope leo xiii": "بواسطة ليون الثالث عشر",
    "by pope paul vi": "بواسطة بولس السادس",
    "by pope pius xi": "بواسطة بيوس الحادي عشر",
    "by pyotr ilyich tchaikovsky": "بواسطة بيتر إليتش تشايكوفسكي",
    "by queen victoria": "بواسطة الملكة فيكتوريا",
    "by richard strauss": "بواسطة ريتشارد شتراوس",
    "by satyajit ray": "بواسطة ساتياجيت راي",
    "by sergei prokofiev": "بواسطة سيرغي بروكوفييف",
    "by sergei rachmaninoff": "بواسطة سيرجي رخمانينوف",
    "by theodore roosevelt": "بواسطة ثيودور روزفلت",
    "by titian": "بواسطة تيتيان",
    "by truman capote": "بواسطة ترومان كابوتي",
    "by warren g. harding": "بواسطة وارن جي. هاردينغ",
    "by will ferrell": "بواسطة ويل فيرل",
    "by william blake": "بواسطة وليم بليك",
    "by wolfgang amadeus mozart": "بواسطة فولفغانغ أماديوس موتسارت",
}

by_data_fast = {
    "by century": "حسب القرن",
    "by city": "حسب المدينة",
    "by conflict": "حسب النزاع",
    "by county": "حسب المقاطعة",
    "by decade": "حسب العقد",
    "by educational affiliation": "حسب الانتماء التعليمي",
    "by educational institution": "حسب الهيئة التعليمية",
    "by hanging": "بالشنق",
    "by high school": "حسب المدرسة الثانوية",
    "by interest": "حسب الاهتمام",
    "by law enforcement officers": "بواسطة ضباط إنفاذ القانون",
    "by league": "حسب الدوري",
    "by location": "حسب الموقع",
    "by month": "حسب الشهر",
    "by nationality": "حسب الجنسية",
    "by newspaper": "حسب الصحيفة",
    "by occupation": "حسب المهنة",
    "by organization": "حسب المنظمة",
    "by person": "حسب الشخص",
    "by populated place": "حسب المكان المأهول",
    "by province or territory": "حسب المقاطعة أو الإقليم",
    "by province": "حسب المقاطعة",
    "by school": "حسب المدرسة",
    "by stabbing": "بالطعن",
    "by subject": "حسب الموضوع",
    "by team": "حسب الفريق",
    "by university or college": "حسب الجامعة أو الكلية",
    "by violence": "بسبب العنف",
    "by year": "حسب السنة",
}


@pytest.mark.parametrize("category, expected", by_data_fast.items(), ids=by_data_fast.keys())
@pytest.mark.fast
def test_by_data(category: str, expected: str) -> None:
    label = resolve_by_labels(category)
    assert label == expected


@pytest.mark.parametrize("category, expected", by_data_peoples.items(), ids=by_data_peoples.keys())
@pytest.mark.fast
def test_by_data_peoples(category: str, expected: str) -> None:
    label = by_people_bot(category)
    assert label == expected


TEMPORAL_CASES = [
    ("test_by_data_1", by_data_fast, resolve_by_labels),
    ("test_by_data_peoples", by_data_peoples, by_people_bot),
]


@pytest.mark.dump
@pytest.mark.parametrize("name,data, callback", TEMPORAL_CASES)
def test_all_dump(name: str, data: dict[str, str], callback) -> None:
    expected, diff_result = one_dump_test(data, callback)

    dump_diff(diff_result, name)
    dump_same_and_not_same(data, diff_result, name)
    assert diff_result == expected, f"Differences found: {len(diff_result):,}, len all :{len(data):,}"

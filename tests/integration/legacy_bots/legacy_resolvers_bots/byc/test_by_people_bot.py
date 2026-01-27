""" """

import pytest
from utils.dump_runner import make_dump_test_name_data_callback

from ArWikiCats.legacy_bots.legacy_resolvers_bots.bys import by_people_bot

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


@pytest.mark.parametrize("category, expected", by_data_peoples.items(), ids=by_data_peoples.keys())
@pytest.mark.fast
def test_by_data_peoples(category: str, expected: str) -> None:
    label = by_people_bot(category)
    assert label == expected


TEMPORAL_CASES = [
    ("test_by_data_peoples", by_data_peoples, by_people_bot),
]

test_dump_all = make_dump_test_name_data_callback(TEMPORAL_CASES, run_same=True)

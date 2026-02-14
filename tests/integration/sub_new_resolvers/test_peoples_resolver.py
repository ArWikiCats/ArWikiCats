"""
Tests
"""

import pytest

from ArWikiCats.sub_new_resolvers.peoples_resolver import work_peoples

fast_data = {
    "adele video albums": "ألبومات فيديو أديل",
    "alanis morissette video albums": "ألبومات فيديو ألانيس موريسيت",
    "james taylor video albums": "ألبومات فيديو جيمس تايلور",
    "janet jackson video albums": "ألبومات فيديو جانيت جاكسون",
    "christina aguilera video albums": "ألبومات فيديو كريستينا أغيليرا",
    "andrew johnson administration cabinet members": "أعضاء مجلس وزراء إدارة أندرو جونسون",
    "andrew johnson administration personnel": "موظفو إدارة أندرو جونسون",
    "william henry harrison administration cabinet members": "أعضاء مجلس وزراء إدارة ويليام هنري هاريسون",
    "william henry harrison administration personnel": "موظفو إدارة ويليام هنري هاريسون",
    "woodrow wilson administration cabinet members": "أعضاء مجلس وزراء إدارة وودرو ويلسون",
    "woodrow wilson administration personnel": "موظفو إدارة وودرو ويلسون",
    "adriano celentano albums": "ألبومات أدريانو تشيلنتانو",
    "ai weiwei albums": "ألبومات آي ويوي",
    "akon albums": "ألبومات إيكون",
    "alanis morissette albums": "ألبومات ألانيس موريسيت",
    "aldous huxley albums": "ألبومات ألدوس هكسلي",
    "alexandra stan albums": "ألبومات ألكسندرا ستان",
    "alice cooper albums": "ألبومات أليس كوبر",
    "james brown albums": "ألبومات جيمس براون",
    "james taylor albums": "ألبومات جيمس تايلور",
    "jamie foxx albums": "ألبومات جيمي فوكس",
    "janet jackson albums": "ألبومات جانيت جاكسون",
    "janis joplin albums": "ألبومات جانيس جوبلين",
    "jason derulo albums": "ألبومات جيسون ديرولو",
    "jason mraz albums": "ألبومات جيسون مراز",
    "alicia keys albums": "ألبومات أليشيا كيز",
    "ed sheeran albums": "ألبومات إد شيران",
    "a. r. rahman albums": "ألبومات أي.أر. رحمان",
    "george h. w. bush administration cabinet members": "أعضاء مجلس وزراء إدارة جورج بوش الأب",
    "george h. w. bush administration personnel": "موظفو إدارة جورج بوش الأب",
    "george w. bush administration cabinet members": "أعضاء مجلس وزراء إدارة جورج بوش الابن",
    "george w. bush administration personnel": "موظفو إدارة جورج بوش الابن",
    "john quincy adams administration cabinet members": "أعضاء مجلس وزراء إدارة جون كوينسي آدامز",
    "john quincy adams administration personnel": "موظفو إدارة جون كوينسي آدامز",
    "lyndon b. johnson administration cabinet members": "أعضاء مجلس وزراء إدارة ليندون جونسون",
    "lyndon b. johnson administration personnel": "موظفو إدارة ليندون جونسون",
    "nusrat fateh ali khan albums": "ألبومات نصرت فتح علي خان",
}


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
    label = work_peoples(category)
    assert label == expected


@pytest.mark.parametrize("category, expected", fast_data.items(), ids=fast_data.keys())
@pytest.mark.fast
def test_fast_data(category: str, expected: str) -> None:
    label = work_peoples(category)
    assert label == expected

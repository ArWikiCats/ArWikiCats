""" """

import pytest

from load_one_data import dump_diff, one_dump_test

from ArWikiCats.make_bots.jobs_bots.relegin_jobs import try_religions_jobs_with_suffix
# from ArWikiCats.make_bots.jobs_bots.relegin_jobs_new import new_religions_jobs_with_suffix as try_religions_jobs_with_suffix
from ArWikiCats.make_bots.jobs_bots.jobs_mainbot import create_country_lab
from ArWikiCats.translations import RELIGIOUS_KEYS_PP

# new dict with only 10 items from RELIGIOUS_KEYS_PP
RELIGIOUS_KEYS_10 = {k: RELIGIOUS_KEYS_PP[k] for k in list(RELIGIOUS_KEYS_PP.keys())[:10]}

jobs_mens_data = {
    "scholars of islam": "باحثون عن الإسلام",
    "women's rights activists": "ناشطون في حقوق المرأة",
    "convicted-of-murder": "أدينوا بالقتل",
    "classical europop cheerleaders": "قادة تشجيع يوروبوب كلاسيكيون",
    "classical europop composers": "ملحنو يوروبوب كلاسيكيون",
    "abidat rma pianists": "عازفو بيانو عبيدات الرما",
    "abidat rma record producers": "منتجو تسجيلات عبيدات الرما",
    "historical objectivists": "موضوعيون تاريخيون",
    "historical opera authors": "مؤلفو أوبرا تاريخيون",
    "men's sailing (sport) power forwards": "مهاجمون أقوياء الجسم رياضة إبحار رجالية",
    "men's sailing (sport) quarterbacks": "أظهرة رباعيون رياضة إبحار رجالية",
    "men's sailing (sport) racing centers": "لاعبو وسط سباق رياضة إبحار رجالية",
    "ski-orienteering quarterbacks": "أظهرة رباعيون سباق تزلج موجه",
    "abidat rma saxophonists": "عازفو سكسفون عبيدات الرما",
    "abidat rma singer-songwriters": "مغنون وكتاب أغاني عبيدات الرما",
    "expatriates": "مغتربون",
}

expatriates_data = {}
for key, data in RELIGIOUS_KEYS_10.items():
    mens_label = data.get("males", "")
    if mens_label:
        for job_key, job_label in jobs_mens_data.items():
            label = create_country_lab(job_label, mens_label, job_key)
            expatriates_data[f"{key} {job_key}"] = label


# new dict with only 20 items from RELIGIOUS_KEYS_PP
RELIGIOUS_KEYS_20 = {k: RELIGIOUS_KEYS_PP[k] for k in list(RELIGIOUS_KEYS_PP.keys())[:20]}


@pytest.mark.parametrize(
    "key,data",
    RELIGIOUS_KEYS_20.items(),
    ids=[x for x in RELIGIOUS_KEYS_20],
)
def test_with_suffix(key: str, data: dict[str, str]) -> None:
    input2 = f"{key} historical house music bloggers"
    expected2 = f"مدونو هاوس تاريخيون {data['males']}"

    result2 = try_religions_jobs_with_suffix(input2)
    assert result2 == expected2, f"{expected2=}, {result2=}, {input2=}"


@pytest.mark.parametrize(
    "input_text,expected",
    expatriates_data.items(),
    ids=[x for x in expatriates_data],
)
@pytest.mark.slow
def test_with_suffix_expatriates(input_text: str, expected: str) -> None:
    result = try_religions_jobs_with_suffix(input_text)
    assert result == expected, f"{expected=}, {result=}, {input_text=}"


def test_one() -> None:
    # {"cate": "bahá'ís classical europop composers", "country_prefix": "bahá'ís", "category_suffix": "classical europop composers", "males": "بهائيون", "females": "بهائيات", "country_lab": "ملحنو يوروبوب كلاسيكيون بهائيون"}
    input_text = "bahá'ís classical europop composers"
    expected = "ملحنو يوروبوب كلاسيكيون بهائيون"

    result = try_religions_jobs_with_suffix(input_text)
    assert result == expected, f"{expected=}, {result=}, {input_text=}"


test_data_2 = {
    "nazi bloggers": "مدونون نازيون",
    "Anglican archbishops": "رؤساء أساقفة أنجليكيون",
    "Anglican biblical scholars": "علماء الكتاب المقدس أنجليكيون",
    "Anglican bishops": "أساقفة أنجليكيون",
    "Anglican clergy": "رجال دين أنجليكيون",
    "Anglican missionaries": "مبشرون أنجليكيون",
    "Anglican monks": "رهبان أنجليكيون",
    "Anglican pacifists": "دعاة سلام أنجليكيون",
    "Anglican philosophers": "فلاسفة أنجليكيون",
    "Anglican poets": "شعراء أنجليكيون",
    "Anglican priests": "كهنة أنجليكيون",
    "Anglican scholars": "دارسون أنجليكيون",
    "Anglican socialists": "اشتراكيون أنجليكيون",
    "Anglican theologians": "لاهوتيون أنجليكيون",
    "Anglican writers": "كتاب أنجليكيون",
    "Buddhist activists": "ناشطون بوذيون",
    "Buddhist apologists": "مدافعون بوذيون",
    "Buddhist artists": "فنانون بوذيون",
    "Buddhist clergy": "رجال دين بوذيون",
    "Buddhist feminists": "نسويون بوذيون",
    "Buddhist missionaries": "مبشرون بوذيون",
    "Buddhist monarchs": "ملكيون بوذيون",
    "Buddhist monks": "رهبان بوذيون",
    "Buddhist mystics": "متصوفون بوذيون",
    "Buddhist nationalists": "قوميون بوذيون",
    "Buddhist pacifists": "دعاة سلام بوذيون",
    "Buddhist poets": "شعراء بوذيون",
    "Buddhist priests": "كهنة بوذيون",
    "Buddhist religious leaders": "قادة دينيون بوذيون",
    "Buddhist socialists": "اشتراكيون بوذيون",
    "Buddhist translators": "مترجمون بوذيون",
    "Buddhist writers": "كتاب بوذيون",
    "Christian activists": "ناشطون مسيحيون",
    "Christian anarchists": "لاسلطويون مسيحيون",
    "Christian anthropologists": "علماء أنثروبولوجيا مسيحيون",
    "Christian apologists": "مدافعون مسيحيون",
    "Christian artists": "فنانون مسيحيون",
    "Christian astrologers": "منجمون مسيحيون",
    "Christian biblical scholars": "علماء الكتاب المقدس مسيحيون",
    "Christian bloggers": "مدونون مسيحيون",
    "Christian clergy": "رجال دين مسيحيون",
    "Christian comics creators": "مبتكرو قصص مصورة مسيحيون",
    "Christian communists": "شيوعيون مسيحيون",
    "Christian conspiracy theorists": "منظرو المؤامرة مسيحيون",
    "Christian country singers": "مغنو كانتري مسيحيون",
    "Christian fascists": "فاشيون مسيحيون",
    "Christian Hebraists": "مستعبرون مسيحيون",
    "Christian hermits": "متنسكون مسيحيون",
    "Christian libertarians": "ليبرتاريون مسيحيون",
    "Christian metal musicians": "موسيقيو ميتال مسيحيون",
    "Christian missionaries": "مبشرون مسيحيون",
    "Christian monarchs": "ملكيون مسيحيون",
    "Christian monks": "رهبان مسيحيون",
    "Christian music songwriters": "كتاب أغان موسيقى مسيحيون",
    "Christian mystics": "متصوفون مسيحيون",
    "Christian nationalists": "قوميون مسيحيون",
    "Christian novelists": "روائيون مسيحيون",
    "Christian occultists": "غموضيون مسيحيون",
    "Christian pacifists": "دعاة سلام مسيحيون",
    "Christian philosophers": "فلاسفة مسيحيون",
    "Christian poets": "شعراء مسيحيون",
    "Christian priests": "كهنة مسيحيون",
    "Christian religious leaders": "قادة دينيون مسيحيون",
    "Christian scholars": "دارسون مسيحيون",
    "Christian Science writers": "كتاب علم مسيحيون",
    "Christian Scientists": "علماء مسيحيون",
    "Christian socialists": "اشتراكيون مسيحيون",
    "Christian theologians": "لاهوتيون مسيحيون",
    "Christian writers": "كتاب مسيحيون",
    "Christian Zionists": "صهاينة مسيحيون",
    "Coptic artists": "فنانون أقباط",
    "Coptic businesspeople": "شخصيات أعمال أقباط",
    "Coptic Catholic bishops": "أساقفة كاثوليك أقباط",
    "Coptic Catholics": "كاثوليك أقباط",
    "Coptic chefs": "طباخون أقباط",
    "Coptic musicians": "موسيقيون أقباط",
    "Coptic politicians": "سياسيون أقباط",
    "Coptic writers": "كتاب أقباط",
    "Evangelical Anglican bishops": "أساقفة أنجليكيون إنجيليون",
    "Evangelical Anglican clergy": "رجال دين أنجليكيون إنجيليون",
    "Evangelical Anglican theologians": "لاهوتيون أنجليكيون إنجيليون",
    "Evangelical conspiracy theorists": "منظرو المؤامرة إنجيليون",
    "Evangelical missionaries": "مبشرون إنجيليون",
    "Evangelical theologians": "لاهوتيون إنجيليون",
    "Evangelical writers": "كتاب إنجيليون",
    "Hindu activists": "ناشطون هندوس",
    "Hindu apologists": "مدافعون هندوس",
    "Hindu astrologers": "منجمون هندوس",
    "Hindu feminists": "نسويون هندوس",
    "Hindu missionaries": "مبشرون هندوس",
    "Hindu monarchs": "ملكيون هندوس",
    "Hindu monks": "رهبان هندوس",
    "Hindu mystics": "متصوفون هندوس",
    "Hindu nationalists": "قوميون هندوس",
    "Hindu pacifists": "دعاة سلام هندوس",
    "Hindu poets": "شعراء هندوس",
    "Hindu priests": "كهنة هندوس",
    "Hindu religious leaders": "قادة دينيون هندوس",
    "Hindus cricketers": "لاعبو كريكت هندوس",
    "Hindu writers": "كتاب هندوس",
    "Islamic democracy activists": "ناشطو ديمقراطية إسلاميون",
    "Islamic economists": "اقتصاديون إسلاميون",
    "Islamic environmentalists": "بيئيون إسلاميون",
    "Islamic fiction writers": "كتاب روائيون إسلاميون",
    "Islamic philosophers": "فلاسفة إسلاميون",
    "Islamic religious leaders": "قادة دينيون إسلاميون",
    "Islamic scholars": "دارسون إسلاميون",
    "Jewish academics": "أكاديميون يهود",
    "Jewish activists": "ناشطون يهود",
    "Jewish actors": "ممثلون يهود",
    "Jewish anarchists": "لاسلطويون يهود",
    "Jewish anthropologists": "علماء أنثروبولوجيا يهود",
    "Jewish apologists": "مدافعون يهود",
    "Jewish archaeologists": "علماء آثار يهود",
    "Jewish architects": "معماريون يهود",
    "Jewish art collectors": "جامعو فنون يهود",
    "Jewish artists": "فنانون يهود",
    "Jewish astrologers": "منجمون يهود",
    "Jewish astronomers": "فلكيون يهود",
    "Jewish atheists": "ملحدون يهود",
    "Jewish bankers": "مصرفيون يهود",
    "Jewish baseball players": "لاعبو كرة قاعدة يهود",
    "Jewish basketball players": "لاعبو كرة سلة يهود",
    "Jewish biblical scholars": "علماء الكتاب المقدس يهود",
    "Jewish biologists": "علماء أحياء يهود",
    "Jewish bloggers": "مدونون يهود",
    "Jewish boxers": "ملاكمون يهود",
    "Jewish cabaret performers": "مؤدون في ملاهي ليلية يهود",
    "Jewish caricaturists": "رسامو كاريكاتير يهود",
    "Jewish centenarians": "مئويون يهود",
    "Jewish chemists": "كيميائيون يهود",
    "Jewish chess players": "لاعبو شطرنج يهود",
    "Jewish civil rights activists": "ناشطو حقوق مدنية يهود",
    "Jewish classical composers": "ملحنو كلاسيكية يهود",
    "Jewish classical musicians": "موسيقيو كلاسيكية يهود",
    "Jewish classical pianists": "عازفو بيانو كلاسيكية يهود",
    "Jewish classical violinists": "عازفو كمان كلاسيكية يهود",
    "Jewish clergy": "رجال دين يهود",
    "Jewish comedians": "كوميديون يهود",
    "Jewish comedy writers": "كتاب كوميدي يهود",
    "Jewish communists": "شيوعيون يهود",
    "Jewish composers": "ملحنون يهود",
    "Jewish country singers": "مغنو كانتري يهود",
    "Jewish cricketers": "لاعبو كريكت يهود",
    "Jewish dancers": "راقصون يهود",
    "Jewish dramatists and playwrights": "كتاب دراما ومسرح يهود",
    "Jewish economists": "اقتصاديون يهود",
    "Jewish educators": "معلمون يهود",
    "Jewish encyclopedists": "موسوعيون يهود",
    "Jewish engineers": "مهندسون يهود",
    "Jewish engravers": "نقاشون يهود",
    "Jewish entertainers": "فنانون ترفيهيون يهود",
    "Jewish Esperantists": "إسبرانتوين يهود",
    "Jewish fascists": "فاشيون يهود",
    "Jewish fashion designers": "مصممو أزياء يهود",
    "Jewish feminists": "نسويون يهود",
    "Jewish fencers": "مبارزون يهود",
    "Jewish folklorists": "فلكلوريون يهود",
    "Jewish folk singers": "مغنو فولك يهود",
    "Jewish footballers": "لاعبو كرة قدم يهود",
    "Jewish golfers": "لاعبو غولف يهود",
    "Jewish heavy metal musicians": "موسيقيو هيفي ميتال يهود",
    "Jewish historians": "مؤرخون يهود",
    "Jewish humorists": "فكاهيون يهود",
    "Jewish illustrators": "رسامون توضيحيون يهود",
    "Jewish jazz musicians": "موسيقيو جاز يهود",
    "Jewish journalists": "صحفيون يهود",
    "Jewish judges": "قضاة يهود",
    "Jewish legal scholars": "أساتذة قانون يهود",
    "Jewish lexicographers": "معجميون يهود",
    "Jewish linguists": "لغويون يهود",
    "Jewish martial artists": "ممارسو فنون قتالية يهود",
    "Jewish memoirists": "كتاب مذكرات يهود",
    "Jewish merchants": "تجار يهود",
    "Jewish military personnel": "أفراد عسكريون يهود",
    "Jewish mixed martial artists": "مقاتلو فنون قتالية مختلطة يهود",
    "Jewish models": "عارضو أزياء يهود",
    "Jewish monarchs": "ملكيون يهود",
    "Jewish musicians": "موسيقيون يهود",
    "Jewish musicologists": "علماء موسيقى يهود",
    "Jewish neuroscientists": "علماء أعصاب يهود",
    "Jewish non-fiction writers": "كتاب غير روائيون يهود",
    "Jewish novelists": "روائيون يهود",
    "Jewish opera composers": "ملحنو أوبرا يهود",
    "Jewish opera singers": "مغنو أوبرا يهود",
    "Jewish orientalists": "مستشرقون يهود",
    "Jewish pacifists": "دعاة سلام يهود",
    "Jewish painters": "رسامون يهود",
    "Jewish philosophers": "فلاسفة يهود",
    "Jewish physicians": "أطباء يهود",
    "Jewish physicists": "فيزيائيون يهود",
    "Jewish poets": "شعراء يهود",
    "Jewish politicians": "سياسيون يهود",
    "Jewish priests": "كهنة يهود",
    "Jewish professional wrestlers": "مصارعون محترفون يهود",
    "Jewish psychoanalysts": "معالجون نفسيون يهود",
    "Jewish rappers": "مغنو راب يهود",
    "Jewish rebels": "متمردون يهود",
    "Jewish religious leaders": "قادة دينيون يهود",
    "Jewish rock musicians": "موسيقيو روك يهود",
    "Jewish rugby league players": "لاعبو دوري رجبي يهود",
    "Jewish rugby union players": "لاعبو اتحاد رجبي يهود",
    "Jewish sailors (sport)": "بحارة رياضيون يهود",
    "Jewish scholars": "دارسون يهود",
    "Jewish scientists": "علماء يهود",
    "Jewish screenwriters": "كتاب سيناريو يهود",
    "Jewish sculptors": "نحاتون يهود",
    "Jewish singers": "مغنون يهود",
    "Jewish socialists": "اشتراكيون يهود",
    "Jewish social scientists": "مختصون بالعلوم الاجتماعية يهود",
    "Jewish sociologists": "علماء اجتماع يهود",
    "Jewish songwriters": "كتاب أغان يهود",
    "Jewish sport shooters": "لاعبو رماية يهود",
    "Jewish sports-people": "رياضيون يهود",
    "Jewish sport wrestlers": "مصارعون رياضيون يهود",
    "Jewish swimmers": "سباحون يهود",
    "Jewish tennis players": "لاعبو كرة مضرب يهود",
    "Jewish theatre directors": "مخرجو مسرح يهود",
    "Jewish theatre people": "مسرحيون يهود",
    "Jewish theologians": "لاهوتيون يهود",
    "Jewish trade unionists": "نقابيون يهود",
    "Jewish translators": "مترجمون يهود",
    "Jewish violinists": "عازفو كمان يهود",
    "Jewish volleyball players": "لاعبو كرة طائرة يهود",
    "Jewish weightlifters": "رباعون يهود",
    "Jewish wrestlers": "مصارعون يهود",
    "Jewish writers": "كتاب يهود",
    "Jewish YouTubers": "مشاهير يوتيوب يهود",
    "Methodist biblical scholars": "علماء الكتاب المقدس ميثوديون لاهوتيون",
    "Methodist bishops": "أساقفة ميثوديون لاهوتيون",
    "Methodist evangelists": "دعاة إنجيليون ميثوديون لاهوتيون",
    "Methodist missionaries": "مبشرون ميثوديون لاهوتيون",
    "Methodist Monarchs": "ملكيون ميثوديون لاهوتيون",
    "Methodist pacifists": "دعاة سلام ميثوديون لاهوتيون",
    "Methodist philosophers": "فلاسفة ميثوديون لاهوتيون",
    "Methodist scholars": "دارسون ميثوديون لاهوتيون",
    "Methodist socialists": "اشتراكيون ميثوديون لاهوتيون",
    "Methodist theologians": "لاهوتيون ميثوديون لاهوتيون",
    "Methodist writers": "كتاب ميثوديون لاهوتيون",
    "Muslim activists": "ناشطون مسلمون",
    "Muslim apologists": "مدافعون مسلمون",
    "Muslim artists": "فنانون مسلمون",
    "Muslim astrologers": "منجمون مسلمون",
    "Muslim clergy": "رجال دين مسلمون",
    "Muslim comedians": "كوميديون مسلمون",
    "Muslim missionaries": "مبشرون مسلمون",
    "Muslim models": "عارضو أزياء مسلمون",
    "Muslim monarchs": "ملكيون مسلمون",
    "Muslim mystics": "متصوفون مسلمون",
    "Muslim occultists": "غموضيون مسلمون",
    "Muslim pacifists": "دعاة سلام مسلمون",
    "Muslim poets": "شعراء مسلمون",
    "Muslim scholars": "دارسون مسلمون",
    "Muslims cricketers": "لاعبو كريكت مسلمون",
    "Muslim socialists": "اشتراكيون مسلمون",
    "Muslim theologians": "لاهوتيون مسلمون",
    "Muslim writers": "كتاب مسلمون",
    "Nazi assassins": "منفذو اغتيالات نازيون",
    "Nazi hunters": "صيادون نازيون",
    "Nazi politicians": "سياسيون نازيون",
    "Nazi propagandists": "مروّجون دعائيون نازيون",
    "Protestant bishops": "أساقفة بروتستانتيون",
    "Protestant clergy": "رجال دين بروتستانتيون",
    "Protestant missionaries": "مبشرون بروتستانتيون",
    "Protestant monarchs": "ملكيون بروتستانتيون",
    "Protestant mystics": "متصوفون بروتستانتيون",
    "Protestant philosophers": "فلاسفة بروتستانتيون",
    "Protestant priests": "كهنة بروتستانتيون",
    "Protestant religious leaders": "قادة دينيون بروتستانتيون",
    "Protestant theologians": "لاهوتيون بروتستانتيون",
    "Protestant writers": "كتاب بروتستانتيون",
    "Venerated Catholics": "كاثوليك مبجلون",
    "Venerated popes": "بابوات مبجلون"
}


@pytest.mark.parametrize("input_text,expected", test_data_2.items(), ids=test_data_2.keys())
def test_get_suffix_prefix(input_text: str, expected: tuple[str, str]) -> None:
    result = try_religions_jobs_with_suffix(input_text)
    assert result == expected, f"{expected=}, {result=}, {input_text=}"


MEN_WOMENS_WITH_NATO_data = {
    "Jewish eugenicists": "علماء يهود متخصصون في تحسين النسل",
    "Jewish politicians who committed suicide": "سياسيون يهود أقدموا على الانتحار",
    "Anglican contemporary artists": "فنانون أنجليكيون معاصرون",
}


@pytest.mark.parametrize("input_text,expected", MEN_WOMENS_WITH_NATO_data.items(), ids=MEN_WOMENS_WITH_NATO_data.keys())
def test_MEN_WOMENS_WITH_NATO(input_text: str, expected: tuple[str, str]) -> None:
    result = try_religions_jobs_with_suffix(input_text)
    assert result == expected, f"{expected=}, {result=}, {input_text=}"


TEMPORAL_CASES = [
    ("test_get_suffix_prefix", test_data_2, try_religions_jobs_with_suffix),
    ("test_MEN_WOMENS_WITH_NATO", MEN_WOMENS_WITH_NATO_data, try_religions_jobs_with_suffix),
    ("test_expatriates_data", expatriates_data, try_religions_jobs_with_suffix),
]


@pytest.mark.parametrize("name,data,callback", TEMPORAL_CASES)
@pytest.mark.dump
def test_all_dump(name: str, data: dict[str, str], callback) -> None:
    expected, diff_result = one_dump_test(data, callback)

    dump_diff(diff_result, name)
    assert diff_result == expected, f"Differences found: {len(diff_result):,}, len all :{len(data):,}"

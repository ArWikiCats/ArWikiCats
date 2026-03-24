"""
Static translations used for tennis and tournament related keys.
"""

from ..helps import len_print

TENNIS_KEYS: dict[str, str] = {
    "800 metres": "800 متر",
    "auto racing series": "سلسة سباق سيارات",
    "auto racing": "سباق سيارات",
    "brd năstase țiriac trophy": "بطولة بوخارست للتنس",
    "brisbane international": "بطولة برزبين للتنس",
    "cincinnati masters": "سنسيناتي للماسترز",
    "copa argentina": "كوبا أرجنتينا",
    "cycling competitions": "مسابقات الدراجات",
    "davis cup": "كأس ديفيز",
    "deaflympics": "ديفلمبياد",
    "delray beach international tennis championships": "بطولة دلراي بيتش الدولية للتنس",
    "dubai tennis championships": "بطولة دبي للتنس",
    "dutch tt": "كأس هولندا السياحية",
    "fed cup": "كأس فيد",
    "fed cups": "كأس فيد",
    "formula e": "فورمولا إي",
    "formula one": "فورمولا ون",
    "gcc champions league": "كأس الخليج للأندية",
    "german formula three championship": "بطولة فورمولا 3 الألمانية",
    "golf tournaments": "بطولات غولف",
    "grand prix hassan ii": "بطولة الدار البيضاء للتنس",
    "hopman cup": "كأس هوبمان",
    "horse races": "سباقات الخيل",
    "ice hockey tournaments": "منافسات هوكي للجليد",
    "indian wells masters": "إنديان ويلز للماسترز",
    "itf women's world tennis tour": "الجولة العالمية لتنس السيدات",
    "kremlin cup": "كأس الكرملين",
    "ligue 1": "الدوري الفرنسي الدرجة الأولى",
    "monte-carlo masters": "مونتي كارلو للماسترز",
    "motorcycle racing series": "سلسلة سباقات الدراجات النارية",
    "motorcycle racing": "سباق الدراجات النارية",
    "national championships": "بطولات وطنية",
    "open de nice côte d'azur": "بطولة نيس المفتوحة للتنس",
    "open sud de france": "بطولة مونبلييه المفتوحة للتنس",
    "paris masters": "باريس للماسترز",
    "portuguese grand prix": "جائزة البرتغال الكبرى",
    "racewalking": "سباق المشي",
    "rosmalen grass court championships": "بطولة روزمالين العشبية للتنس",
    "rowing competitions": "منافسات تجديف",
    "shanghai masters (tennis)": "شنغهاي للماسترز",
    "shanghai masters tennis": "شنغهاي للماسترز",
    "six nations championship": "بطولة الأمم الستة",
    "swiss cup": "كأس سويسرا لكرة القدم",
    "swiss indoors": "بطولة بازل للتنس",
    "sydney international": "بطولة سيدني للتنس",
    "tennis napoli cup": "كأس نابولي لكرة المضرب",
    "the championships, wimbledon": "بطولة ويمبلدون",
    "u.s. men's clay court championships": "بطولة هيوستن للتنس",
    "u.s. national indoor tennis championships": "بطولة ممفيس المفتوحة للتنس",
    "world baseball classic": "عالم البيسبول الكلاسيكي",
    "world champions": "أبطال العالم",
    "world championships": "بطولات العالم",
    "world touring car championship": "بطولة العالم لسيارات السياحة",
    "zagreb indoors": "بطولة زغرب للتنس",
}

OPEN_KEYS = {
    "barcelona open (tennis)": "بطولة برشلونة للتنس",
    "barcelona open tennis": "بطولة برشلونة للتنس",
    "madrid open tennis": "مدريد للماسترز",
    "madrid open (tennis)": "مدريد للماسترز",
    "miami open (tennis)": "ميامي للماسترز",
    "miami open tennis": "ميامي للماسترز",
    "citi open": "بطولة واشنطن المفتوحة",
    "french open": "دورة رولان غاروس الدولية",
    "chennai open": "بطولة تشيناي المفتوحة للتنس",
    "geneva open": "بطولة جنيف المفتوحة",
    "gerry weber open": "بطولة هالي المفتوحة",
    "istanbul open": "بطولة إسطنبول المفتوحة",
    "nottingham open": "بطولة نوتنغهام المفتوحة",
    "portugal open": "البرتغال المفتوحة",
    "rai open": "راي المفتوحة",
    "seoul open": "سول المفتوحة",
    "stockholm open": "بطولة ستوكهولم المفتوحة للتنس",
    "stuttgart open": "بطولة شتوتغارت المفتوحة",
    "swedish open": "بطولة السويد المفتوحة للتنس",
    "rio open": "بطولة ريو للتنس",
    "valencia open": "بطولة فالنسيا المفتوحة",
    "tunis open": "دورة تونس المفتوحة للتنس",
}

TENNIS_KEYS.update(OPEN_KEYS)

__all__ = [
    "TENNIS_KEYS",
]

len_print.data_len(
    "tennis.py",
    {
        "TENNIS_KEYS": TENNIS_KEYS,
    },
)

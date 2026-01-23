#
import pytest

from ArWikiCats import resolve_label_ar
from utils.dump_runner import make_dump_test_name_data

data_0 = {
    "organized crime films based on actual events": "",
    "western (genre) films based on actual events": "",
    "seafaring films based on actual events": "",
    "world war ii films based on actual events": "",
    "ballets based on actual events": "",
    "australian radio dramas based on actual events": "",
    "american civil war films based on actual events": "",
    "world war i films based on actual events": "",
}

slow_data = {
    "art based on actual events": "الفن مبنية على أحداث حقيقية",
    "musical drama films based on actual events": "أفلام موسيقية درامية مبنية على أحداث حقيقية",
    "lgbtq-related films based on actual events": "أفلام متعلقة بإل جي بي تي كيو مبنية على أحداث حقيقية",
    "literature based on actual events": "أدب مبنية على أحداث حقيقية",
    "games based on actual events": "ألعاب مبنية على أحداث حقيقية",
    "sports films based on actual events": "أفلام رياضية مبنية على أحداث حقيقية",
    "horror films based on actual events": "أفلام رعب مبنية على أحداث حقيقية",
    "czech films based on actual events": "أفلام تشيكية مبنية على أحداث حقيقية",
    "films based on actual events by country": "أفلام مبنية على أحداث حقيقية حسب البلد",
    "bangladeshi films based on actual events": "أفلام بنغلاديشية مبنية على أحداث حقيقية",
    "marathi-language films based on actual events": "أفلام باللغة الماراثية مبنية على أحداث حقيقية",
    "war films based on actual events": "أفلام حربية مبنية على أحداث حقيقية",
    "adventure films based on actual events": "أفلام مغامرات مبنية على أحداث حقيقية",
    "lists of films based on actual events": "قوائم أفلام مبنية على أحداث حقيقية",
    "nepalese films based on actual events": "أفلام نيبالية مبنية على أحداث حقيقية",
    "action drama films based on actual events": "أفلام حركة درامية مبنية على أحداث حقيقية",
    "operas based on actual events": "أوبيرات مبنية على أحداث حقيقية",
    "vietnam war films based on actual events": "أفلام حرب فيتنام مبنية على أحداث حقيقية",
    "comedy-drama films based on actual events": "أفلام كوميدية درامية مبنية على أحداث حقيقية",
    "romantic drama films based on actual events": "أفلام رومانسية درامية مبنية على أحداث حقيقية",
    "political thriller films based on actual events": "أفلام إثارة سياسية مبنية على أحداث حقيقية",
    "novels based on actual events": "روايات مبنية على أحداث حقيقية",
    "drama films based on actual events": "أفلام درامية مبنية على أحداث حقيقية",
    "argentine films based on actual events": "أفلام أرجنتينية مبنية على أحداث حقيقية",
    "spanish films based on actual events": "أفلام إسبانية مبنية على أحداث حقيقية",
    "disaster films based on actual events": "أفلام كوارثية مبنية على أحداث حقيقية",
    "spy films based on actual events": "أفلام تجسسية مبنية على أحداث حقيقية",
    "belgian films based on actual events": "أفلام بلجيكية مبنية على أحداث حقيقية",
    "works based on actual events": "أعمال مبنية على أحداث حقيقية",
    "video games based on actual events": "ألعاب فيديو مبنية على أحداث حقيقية",
    "romance films based on actual events": "أفلام رومانسية مبنية على أحداث حقيقية",
    "films based on actual events by genre": "أفلام مبنية على أحداث حقيقية حسب النوع الفني",
    "books based on actual events": "كتب مبنية على أحداث حقيقية",
    "american films based on actual events": "أفلام أمريكية مبنية على أحداث حقيقية",
    "hindi-language films based on actual events": "أفلام باللغة الهندية مبنية على أحداث حقيقية",
    "epic films based on actual events": "أفلام ملحمية مبنية على أحداث حقيقية",
    "political films based on actual events": "أفلام سياسية مبنية على أحداث حقيقية",
    "hong kong films based on actual events": "أفلام هونغ كونغية مبنية على أحداث حقيقية",
    "television shows based on actual events": "عروض تلفزيونية مبنية على أحداث حقيقية",
    "comedy films based on actual events": "أفلام كوميدية مبنية على أحداث حقيقية",
    "finnish films based on actual events": "أفلام فنلندية مبنية على أحداث حقيقية",
    "coming-of-age drama films based on actual events": "أفلام تقدم في العمر درامية مبنية على أحداث حقيقية",
    "television films based on actual events": "أفلام تلفزيونية مبنية على أحداث حقيقية",
    "songs based on actual events": "أغاني مبنية على أحداث حقيقية",
    "musical films based on actual events": "أفلام موسيقية مبنية على أحداث حقيقية",
    "political drama films based on actual events": "أفلام سياسية درامية مبنية على أحداث حقيقية",
    "japanese films based on actual events": "أفلام يابانية مبنية على أحداث حقيقية",
    "french films based on actual events": "أفلام فرنسية مبنية على أحداث حقيقية",
    "sports drama films based on actual events": "أفلام رياضية درامية مبنية على أحداث حقيقية",
    "war drama films based on actual events": "أفلام حربية درامية مبنية على أحداث حقيقية",
    "romantic comedy films based on actual events": "أفلام كوميدية رومانسية مبنية على أحداث حقيقية",
    "horror thriller films based on actual events": "أفلام رعب إثارة مبنية على أحداث حقيقية",
    "south korean films based on actual events": "أفلام كورية جنوبية مبنية على أحداث حقيقية",
    "television series based on actual events": "مسلسلات تلفزيونية مبنية على أحداث حقيقية",
    "action thriller films based on actual events": "أفلام إثارة حركة مبنية على أحداث حقيقية",
    "crime comedy films based on actual events": "أفلام جنائية كوميدية مبنية على أحداث حقيقية",
    "italian films based on actual events": "أفلام إيطالية مبنية على أحداث حقيقية",
    "thriller films based on actual events": "أفلام إثارة مبنية على أحداث حقيقية",
    "crime action films based on actual events": "أفلام جريمة حركة مبنية على أحداث حقيقية",
    "war comedy films based on actual events": "أفلام حربية كوميدية مبنية على أحداث حقيقية",
    "indian films based on actual events": "أفلام هندية مبنية على أحداث حقيقية",
    "crime thriller films based on actual events": "أفلام إثارة وجريمة مبنية على أحداث حقيقية",
    "australian films based on actual events": "أفلام أسترالية مبنية على أحداث حقيقية",
    "crime drama films based on actual events": "أفلام جريمة درامية مبنية على أحداث حقيقية",
    "british films based on actual events": "أفلام بريطانية مبنية على أحداث حقيقية",
    "films based on actual events": "أفلام مبنية على أحداث حقيقية",
    "children's books based on actual events": "كتب أطفال مبنية على أحداث حقيقية",
    "action films based on actual events": "أفلام حركة مبنية على أحداث حقيقية",
    "philippine films based on actual events": "أفلام فلبينية مبنية على أحداث حقيقية",
    "spy thriller films based on actual events": "أفلام تجسسية إثارة مبنية على أحداث حقيقية",
    "sports comedy films based on actual events": "أفلام رياضية كوميدية مبنية على أحداث حقيقية",
    "comics based on actual events": "قصص مصورة مبنية على أحداث حقيقية",
    "short stories based on actual events": "قصص قصيرة مبنية على أحداث حقيقية",
    "poems based on actual events": "قصائد مبنية على أحداث حقيقية",
    "plays based on actual events": "مسرحيات مبنية على أحداث حقيقية",
    "nigerian films based on actual events": "أفلام نيجيرية مبنية على أحداث حقيقية",
    "coming-of-age films based on actual events": "أفلام تقدم في العمر مبنية على أحداث حقيقية",
    "mystery films based on actual events": "أفلام غموض مبنية على أحداث حقيقية",
    "german films based on actual events": "أفلام ألمانية مبنية على أحداث حقيقية",
    "animated films based on actual events": "أفلام رسوم متحركة مبنية على أحداث حقيقية",
    "canadian films based on actual events": "أفلام كندية مبنية على أحداث حقيقية",
    "crime films based on actual events": "أفلام جريمة مبنية على أحداث حقيقية",
}


fast_data_3 = {
    "American television series based on children's books": "مسلسلات تلفزيونية أمريكية مبنية على كتب أطفال",
    "American television series based on telenovelas": "مسلسلات تلفزيونية أمريكية مبنية على تيلينوفيلا",
    "Animated television series based on Marvel Comics": "مسلسلات تلفزيونية رسوم متحركة مبنية على مارفال كومكس",
    "Anime television series based on video games": "مسلسلات أنمي متلفزة مبنية على ألعاب فيديو",
    "Bengali-language television series based on Tamil-language television series": "مسلسلات تلفزيونية باللغة البنغالية مبنية على مسلسلات تلفزيونية باللغة التاميلية",
    "Hindi-language television series based on Tamil-language television series": "مسلسلات تلفزيونية باللغة الهندية مبنية على مسلسلات تلفزيونية باللغة التاميلية",
    "Kannada-language television series based on Tamil-language television series": "مسلسلات تلفزيونية باللغة الكنادية مبنية على مسلسلات تلفزيونية باللغة التاميلية",
    "Lists of television series based on works": "قوائم مسلسلات تلفزيونية مبنية على أعمال",
    "Malayalam-language television series based on Bengali-language television series": "مسلسلات تلفزيونية باللغة الماليالامية مبنية على مسلسلات تلفزيونية باللغة البنغالية",
    "Malayalam-language television series based on Hindi-language television series": "مسلسلات تلفزيونية باللغة الماليالامية مبنية على مسلسلات تلفزيونية باللغة الهندية",
    "Malayalam-language television series based on Marathi-language television series": "مسلسلات تلفزيونية باللغة الماليالامية مبنية على مسلسلات تلفزيونية باللغة الماراثية",
    "Malayalam-language television series based on Tamil-language television series": "مسلسلات تلفزيونية باللغة الماليالامية مبنية على مسلسلات تلفزيونية باللغة التاميلية",
    "Malayalam-language television series based on Telugu-language television series": "مسلسلات تلفزيونية باللغة الماليالامية مبنية على مسلسلات تلفزيونية باللغة التيلوغوية",
    "Marathi-language television series based on Tamil-language television series": "مسلسلات تلفزيونية باللغة الماراثية مبنية على مسلسلات تلفزيونية باللغة التاميلية",
    "Parody television series based on Star Wars": "مسلسلات تلفزيونية ساخرة مبنية على حرب النجوم",
    "Philippine television series based on films": "مسلسلات تلفزيونية فلبينية مبنية على أفلام",
    "Philippine television series based on telenovelas": "مسلسلات تلفزيونية فلبينية مبنية على تيلينوفيلا",
    "Tamil-language television series based on American television series": "مسلسلات تلفزيونية باللغة التاميلية مبنية على مسلسلات تلفزيونية أمريكية",
    "Tamil-language television series based on British television series": "مسلسلات تلفزيونية باللغة التاميلية مبنية على مسلسلات تلفزيونية بريطانية",
    "Tamil-language television series based on Hindi-language television series": "مسلسلات تلفزيونية باللغة التاميلية مبنية على مسلسلات تلفزيونية باللغة الهندية",
    "Tamil-language television series based on Kannada-language television series": "مسلسلات تلفزيونية باللغة التاميلية مبنية على مسلسلات تلفزيونية باللغة الكنادية",
    "Tamil-language television series based on Malayalam-language television series": "مسلسلات تلفزيونية باللغة التاميلية مبنية على مسلسلات تلفزيونية باللغة الماليالامية",
    "Tamil-language television series based on Marathi-language television series": "مسلسلات تلفزيونية باللغة التاميلية مبنية على مسلسلات تلفزيونية باللغة الماراثية",
    "Tamil-language television series based on South Korean television series": "مسلسلات تلفزيونية باللغة التاميلية مبنية على مسلسلات تلفزيونية كورية جنوبية",
    "Tamil-language television series based on Telugu-language television series": "مسلسلات تلفزيونية باللغة التاميلية مبنية على مسلسلات تلفزيونية باللغة التيلوغوية",
    "Television series based on actual events": "مسلسلات تلفزيونية مبنية على أحداث حقيقية",
    "Television series based on adaptations": "مسلسلات تلفزيونية مبنية على تكييفات",
    "Television series based on Belgian comics": "مسلسلات تلفزيونية مبنية على قصص مصورة بلجيكية",
    "Television series based on books": "مسلسلات تلفزيونية مبنية على كتب",
    "Television series based on Brazilian comics": "مسلسلات تلفزيونية مبنية على قصص مصورة برازيلية",
    "Television series based on children's books": "مسلسلات تلفزيونية مبنية على كتب أطفال",
    "Television series based on Chinese mythology": "مسلسلات تلفزيونية مبنية على أساطير صينية",
    "Television series based on Egyptian mythology": "مسلسلات تلفزيونية مبنية على أساطير مصرية",
    "Television series based on French comics": "مسلسلات تلفزيونية مبنية على قصص مصورة فرنسية",
    "Television series based on literature": "مسلسلات تلفزيونية مبنية على أدب",
    "Television series based on mythology": "مسلسلات تلفزيونية مبنية على أساطير",
    "Television series based on plays": "مسلسلات تلفزيونية مبنية على مسرحيات",
    "Television series based on Pride and Prejudice": "مسلسلات تلفزيونية مبنية على كبرياء وتحامل (رواية)",
    "Television series based on the Mahabharata": "مسلسلات تلفزيونية مبنية على مهابهاراتا",
    "Television series based on the Ramayana": "مسلسلات تلفزيونية مبنية على رامايانا",
    "Television series based on works by Neil Gaiman": "مسلسلات تلفزيونية مبنية على أعمال نيل غيمان",
    "Television series based on works by Robert Louis Stevenson": "مسلسلات تلفزيونية مبنية على أعمال روبرت لويس ستيفنسون",
    "Television series based on works": "مسلسلات تلفزيونية مبنية على أعمال",
    "Telugu-language television series based on Tamil-language television series": "مسلسلات تلفزيونية باللغة التيلوغوية مبنية على مسلسلات تلفزيونية باللغة التاميلية",
}


to_test = [
    ("test_based_on_1", slow_data),
    ("test_based_on_2", fast_data_3),
]


@pytest.mark.parametrize("category, expected", slow_data.items(), ids=slow_data.keys())
@pytest.mark.slow
def test_based_on_1(category: str, expected: str) -> None:
    label = resolve_label_ar(category)
    assert label == expected


@pytest.mark.parametrize("category, expected", fast_data_3.items(), ids=fast_data_3.keys())
@pytest.mark.slow
def test_based_on_2(category: str, expected: str) -> None:
    label = resolve_label_ar(category)
    assert label == expected


test_dump_all = make_dump_test_name_data(to_test, resolve_label_ar, run_same=False)

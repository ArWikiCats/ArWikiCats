#
import pytest

from ArWikiCats.new_resolvers.films_resolvers.resolve_films_labels_and_time import fetch_films_by_category
from utils.dump_runner import make_dump_test_name_data_callback

data_to_fix1 = {
    "Lists of superhero films": "قوائم أفلام أبطال خارقين",
    "Superhero films about Asian Americans": "أفلام أبطال خارقين عن أمريكيون آسيويون",
    "Superhero television series by country": "مسلسلات تلفزيونية أبطال خارقين حسب البلد",
    "Superhero television series by genre": "مسلسلات تلفزيونية أبطال خارقين حسب النوع الفني",
    "Superhero comedy films by century": "أفلام أبطال خارقين كوميدية حسب القرن",
    "Animated superhero films by decade": "أفلام رسوم متحركة أبطال خارقين حسب العقد",
    "American superhero comedy television series by decade": "مسلسلات تلفزيونية أبطال خارقين كوميدية أمريكية حسب العقد",
    "Superhero films by century": "أفلام أبطال خارقين حسب القرن",
    "Superhero films by country": "أفلام أبطال خارقين حسب البلد",
    "Superhero films by decade": "أفلام أبطال خارقين حسب العقد",
    "Superhero films by genre": "أفلام أبطال خارقين حسب النوع الفني",
    "Superhero comedy films by decade": "أفلام أبطال خارقين كوميدية حسب العقد",
}

data_to_fix2 = {
    "1950s American superhero television series": "مسلسلات تلفزيونية أبطال خارقين أمريكية في عقد 1950",
    "1960s American superhero comedy television series": "مسلسلات تلفزيونية أبطال خارقين كوميدية أمريكية في عقد 1960",
    "1970s American superhero television series": "مسلسلات تلفزيونية أبطال خارقين أمريكية في عقد 1970",
    "1980s American superhero television series": "مسلسلات تلفزيونية أبطال خارقين أمريكية في عقد 1980",
    "1990s American superhero comedy television series": "مسلسلات تلفزيونية أبطال خارقين كوميدية أمريكية في عقد 1990",
    "1990s American superhero television series": "مسلسلات تلفزيونية أبطال خارقين أمريكية في عقد 1990",
    "1990s animated superhero films": "أفلام رسوم متحركة أبطال خارقين في عقد 1990",
    "2000s American superhero comedy television series": "مسلسلات تلفزيونية أبطال خارقين كوميدية أمريكية في عقد 2000",
    "2000s American superhero television series": "مسلسلات تلفزيونية أبطال خارقين أمريكية في عقد 2000",
    "2000s animated superhero films": "أفلام رسوم متحركة أبطال خارقين في عقد 2000",
    "2010s American superhero comedy television series": "مسلسلات تلفزيونية أبطال خارقين كوميدية أمريكية في عقد 2010",
    "2010s American superhero television series": "مسلسلات تلفزيونية أبطال خارقين أمريكية في عقد 2010",
    "2010s animated superhero films": "أفلام رسوم متحركة أبطال خارقين في عقد 2010",
    "2010s animated superhero television films": "أفلام تلفزيونية رسوم متحركة أبطال خارقين في عقد 2010",
    "2020s American superhero comedy television series": "مسلسلات تلفزيونية أبطال خارقين كوميدية أمريكية في عقد 2020",
    "2020s American superhero television series": "مسلسلات تلفزيونية أبطال خارقين أمريكية في عقد 2020",
    "2020s animated superhero films": "أفلام رسوم متحركة أبطال خارقين في عقد 2020",
    "2024 superhero films": "أفلام أبطال خارقين في 2024",
    "20th-century superhero comedy films": "أفلام أبطال خارقين كوميدية في القرن 20",
    "21st-century superhero comedy films": "أفلام أبطال خارقين كوميدية في القرن 21",
    "Adult animated superhero films": "أفلام رسوم متحركة للكبار أبطال خارقين",
    "African-American superhero films": "أفلام أبطال خارقين أمريكية إفريقية",
    "American adult animated superhero television series": "مسلسلات تلفزيونية رسوم متحركة للكبار أبطال خارقين أمريكية",
    "American animated superhero films": "أفلام رسوم متحركة أبطال خارقين أمريكية",
    "American animated superhero television series": "مسلسلات تلفزيونية رسوم متحركة أبطال خارقين أمريكية",
    "American black superhero television shows": "عروض تلفزيونية سوداء أبطال خارقين أمريكية",
    "American superhero comedy television series": "مسلسلات تلفزيونية أبطال خارقين كوميدية أمريكية",
    "American superhero television series": "مسلسلات تلفزيونية أبطال خارقين أمريكية",
    "Animated superhero films": "أفلام رسوم متحركة أبطال خارقين",
    "Animated superhero television series": "مسلسلات تلفزيونية رسوم متحركة أبطال خارقين",
    "Brazilian adult animated superhero television series": "مسلسلات تلفزيونية رسوم متحركة للكبار أبطال خارقين برازيلية",
    "British superhero films": "أفلام أبطال خارقين بريطانية",
    "British superhero television series": "مسلسلات تلفزيونية أبطال خارقين بريطانية",
    "Canadian superhero comedy television series": "مسلسلات تلفزيونية أبطال خارقين كوميدية كندية",
    "Canadian superhero films": "أفلام أبطال خارقين كندية",
    "Canadian superhero television series": "مسلسلات تلفزيونية أبطال خارقين كندية",
    "Chinese superhero films": "أفلام أبطال خارقين صينية",
    "French superhero films": "أفلام أبطال خارقين فرنسية",
    "German superhero films": "أفلام أبطال خارقين ألمانية",
    "Indian superhero films": "أفلام أبطال خارقين هندية",
    "Indian superhero television shows": "عروض تلفزيونية أبطال خارقين هندية",
    "Italian superhero films": "أفلام أبطال خارقين إيطالية",
    "Japanese adult animated superhero television series": "مسلسلات تلفزيونية رسوم متحركة للكبار أبطال خارقين يابانية",
    "Japanese animated superhero films": "أفلام رسوم متحركة أبطال خارقين يابانية",
    "Japanese animated superhero television series": "مسلسلات تلفزيونية رسوم متحركة أبطال خارقين يابانية",
    "LGBTQ-related superhero films": "أفلام أبطال خارقين متعلقة بإل جي بي تي كيو",
    "LGBTQ-related superhero television shows": "عروض تلفزيونية أبطال خارقين متعلقة بإل جي بي تي كيو",
    "Russian superhero films": "أفلام أبطال خارقين روسية",
    "Saudi Arabian superhero films": "أفلام أبطال خارقين سعودية",
    "Superhero comedy television series": "مسلسلات تلفزيونية أبطال خارقين كوميدية",
    "Superhero comic strips": "شرائط كومكس أبطال خارقين",
    "Superhero comics": "قصص مصورة أبطال خارقين",
    "Superhero film characters": "شخصيات أفلام أبطال خارقين",
    "Superhero games": "ألعاب أبطال خارقين",
    "Superhero horror comics": "قصص مصورة أبطال خارقين رعب",
    "Superhero horror films": "أفلام أبطال خارقين رعب",
    "Superhero horror television shows": "عروض تلفزيونية أبطال خارقين رعب",
    "Superhero novels": "روايات أبطال خارقين",
    "Superhero science fiction web series": "مسلسلات ويب أبطال خارقين خيال علمي",
    "Superhero television characters": "شخصيات تلفزيونية أبطال خارقين",
    "Superhero television episodes": "حلقات تلفزيونية أبطال خارقين",
    "Superhero television series": "مسلسلات تلفزيونية أبطال خارقين",
    "Superhero television shows": "عروض تلفزيونية أبطال خارقين",
    "Superhero thriller films": "أفلام أبطال خارقين إثارة",
    "Superhero video games": "ألعاب فيديو أبطال خارقين",
    "Superhero web series": "مسلسلات ويب أبطال خارقين",
    "Superhero webcomics": "ويب كومكس أبطال خارقين",
    "Teen superhero films": "أفلام مراهقة أبطال خارقين",
    "Teen superhero television series": "مسلسلات تلفزيونية مراهقة أبطال خارقين",
    "1940s superhero films": "أفلام أبطال خارقين في عقد 1940",
    "1960s superhero films": "أفلام أبطال خارقين في عقد 1960",
    "1970s superhero films": "أفلام أبطال خارقين في عقد 1970",
    "1980s superhero comedy films": "أفلام أبطال خارقين كوميدية في عقد 1980",
    "1980s superhero films": "أفلام أبطال خارقين في عقد 1980",
    "1990s superhero comedy films": "أفلام أبطال خارقين كوميدية في عقد 1990",
    "1990s superhero films": "أفلام أبطال خارقين في عقد 1990",
    "2000s superhero comedy films": "أفلام أبطال خارقين كوميدية في عقد 2000",
    "2000s superhero films": "أفلام أبطال خارقين في عقد 2000",
    "2010s superhero comedy films": "أفلام أبطال خارقين كوميدية في عقد 2010",
    "2010s superhero films": "أفلام أبطال خارقين في عقد 2010",
    "2020s superhero comedy films": "أفلام أبطال خارقين كوميدية في عقد 2020",
    "2020s superhero films": "أفلام أبطال خارقين في عقد 2020",
    "20th-century superhero films": "أفلام أبطال خارقين في القرن 20",
    "21st-century superhero films": "أفلام أبطال خارقين في القرن 21",
    "American superhero comedy films": "أفلام أبطال خارقين كوميدية أمريكية",
    "American superhero films": "أفلام أبطال خارقين أمريكية",
    "Czech superhero films": "أفلام أبطال خارقين تشيكية",
    "Hong Kong superhero films": "أفلام أبطال خارقين هونغ كونغية",
    "Indonesian superhero films": "أفلام أبطال خارقين إندونيسية",
    "Japanese superhero films": "أفلام أبطال خارقين يابانية",
    "Superhero adventure films": "أفلام أبطال خارقين مغامرات",
    "Superhero black comedy films": "أفلام أبطال خارقين كوميدية سوداء",
    "Superhero comedy-drama films": "أفلام أبطال خارقين كوميدية درامية",
    "Superhero comedy films": "أفلام أبطال خارقين كوميدية",
    "Superhero drama films": "أفلام أبطال خارقين درامية",
    # "Superhero films": "أفلام أبطال خارقين",
    "Superhero teams": "فرق أبطال خارقين",
}

data_to_fix3 = {
    "American children's animated superhero films": "أفلام رسوم متحركة أبطال خارقين أمريكية للأطفال",
    "American children's animated superhero television series": "مسلسلات تلفزيونية رسوم متحركة أبطال خارقين أمريكية للأطفال",
    "Australian children's animated superhero television series": "مسلسلات تلفزيونية رسوم متحركة أبطال خارقين أسترالية للأطفال",
    "British children's animated superhero television series": "مسلسلات تلفزيونية رسوم متحركة أبطال خارقين بريطانية للأطفال",
    "Canadian children's animated superhero television series": "مسلسلات تلفزيونية رسوم متحركة أبطال خارقين كندية للأطفال",
    "Danish children's animated superhero television series": "مسلسلات تلفزيونية رسوم متحركة أبطال خارقين دنماركية للأطفال",
    "French children's animated superhero television series": "مسلسلات تلفزيونية رسوم متحركة أبطال خارقين فرنسية للأطفال",
    "Italian children's animated superhero television series": "مسلسلات تلفزيونية رسوم متحركة أبطال خارقين إيطالية للأطفال",
    "Japanese children's animated superhero television series": "مسلسلات تلفزيونية رسوم متحركة أبطال خارقين يابانية للأطفال",
    "South Korean children's animated superhero television series": "مسلسلات تلفزيونية رسوم متحركة أبطال خارقين كورية جنوبية للأطفال",
    "Spanish children's animated superhero television series": "مسلسلات تلفزيونية رسوم متحركة أبطال خارقين إسبانية للأطفال",
}

to_test = [
    ("test_superhero_data_to_fix2", data_to_fix2, fetch_films_by_category),
    ("test_superhero_data_to_fix3", data_to_fix3, fetch_films_by_category),
]


@pytest.mark.parametrize("category, expected", data_to_fix2.items(), ids=data_to_fix2.keys())
def test_superhero_data_2(category: str, expected: str) -> None:
    result = fetch_films_by_category(category)
    assert result == expected


@pytest.mark.parametrize("category, expected", data_to_fix3.items(), ids=data_to_fix3.keys())
def test_superhero_data_3(category: str, expected: str) -> None:
    result = fetch_films_by_category(category)
    assert result == expected


test_dump_all = make_dump_test_name_data_callback(to_test, run_same=True)

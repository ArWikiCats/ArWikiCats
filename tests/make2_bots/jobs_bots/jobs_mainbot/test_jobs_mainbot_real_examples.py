import pytest

from ArWikiCats.make_bots.jobs_bots.jobs_mainbot import jobs_with_nat_prefix


def make_cate(item) -> str:
    return f"{item['prefix']} {item['suffix']}"


def error_show(item, result) -> str:
    country_prefix = item.get("prefix", "")
    category_suffix = item.get("suffix", "")
    expected = item.get("expected", "")
    cate = item.get("cate", "")

    return f"""
        ------------------ FAILED CASE ------------------
        Input cate:               {cate}
        Input Start(country):     {country_prefix}
        Input category_suffix:    {category_suffix}
        -------------------------------------------------
        Expected Output:
        {expected}

        Actual Output:
        {result}
        -------------------------------------------------
    """


EXAMPLES = [
    {"suffix": "athletics coaches", "prefix": "belgian", "expected": "مدربو ألعاب قوى بلجيكيون"},
    {"suffix": "award winners", "prefix": "american", "expected": "حائزو جوائز أمريكيون"},
    {"suffix": "basketball coaches", "prefix": "american", "expected": "مدربو كرة سلة أمريكيون"},
    {"suffix": "basketball players", "prefix": "american", "expected": "لاعبو كرة سلة أمريكيون"},
    {"suffix": "basketball players", "prefix": "ethiopian", "expected": "لاعبو كرة سلة إثيوبيون"},
    {"suffix": "cinema editors", "prefix": "american", "expected": "محررون سينمائون أمريكيون"},
    {"suffix": "competitors", "prefix": "afghan", "expected": "منافسون أفغان"},
    {"suffix": "competitors", "prefix": "moroccan", "expected": "منافسون مغاربة"},
    {"suffix": "cricketers", "prefix": "indian", "expected": "لاعبو كريكت هنود"},
    {"suffix": "defectors", "prefix": "italian", "expected": "إيطاليون منشقون"},
    {"suffix": "diplomats", "prefix": "afghan", "expected": "دبلوماسيون أفغان"},
    {"suffix": "editorial cartoonists", "prefix": "british", "expected": "محررون كارتونيون بريطانيون"},
    {"suffix": "emigrants", "prefix": "afghan", "expected": "أفغان مهاجرون"},
    {"suffix": "emigrants", "prefix": "ivorian", "expected": "إيفواريون مهاجرون"},
    {"suffix": "expatriate sprtspeople", "prefix": "turkish", "expected": "رياضيون أتراك مغتربون"},
    {"suffix": "expatriates", "prefix": "afghan", "expected": "أفغان مغتربون"},
    {"suffix": "expatriates", "prefix": "ivorian", "expected": "إيفواريون مغتربون"},
    {"suffix": "explorers", "prefix": "dutch", "expected": "مستكشفون هولنديون"},
    {"suffix": "figure skaters", "prefix": "norwegian", "expected": "متزلجون فنيون نرويجيون"},
    {"suffix": "football managers", "prefix": "cape verdean", "expected": "مدربو كرة قدم أخضريون"},
    {"suffix": "football managers", "prefix": "irish", "expected": "مدربو كرة قدم أيرلنديون"},
    {"suffix": "football managers", "prefix": "the republic-of ireland", "expected": "مدربو كرة قدم أيرلنديون"},
    {"suffix": "footballers", "prefix": "german", "expected": "لاعبو كرة قدم ألمان"},
    {"suffix": "healthcare managers", "prefix": "portuguese", "expected": "مدراء رعاية صحية برتغاليون"},
    {"suffix": "internet celebrities", "prefix": "australian", "expected": "مشاهير إنترنت أستراليون"},
    {"suffix": "male athletes", "prefix": "icelandic", "expected": "لاعبو قوى ذكور آيسلنديون"},
    {"suffix": "male middle-distance runners", "prefix": "moroccan", "expected": "عداؤو مسافات متوسطة ذكور مغاربة"},
    {"suffix": "male pair skaters", "prefix": "norwegian", "expected": "متزلجون فنيون على الجليد ذكور نرويجيون"},
    {"suffix": "male runners", "prefix": "icelandic", "expected": "عداؤون ذكور آيسلنديون"},
    {"suffix": "male single skaters", "prefix": "norwegian", "expected": "متزلجون فرديون ذكور نرويجيون"},
    {"suffix": "male sport shooters", "prefix": "egyptian", "expected": "لاعبو رماية ذكور مصريون"},
    {"suffix": "male sprinters", "prefix": "australian", "expected": "عداؤون سريعون ذكور أستراليون"},
    {"suffix": "male steeplechase runners", "prefix": "icelandic", "expected": "عداؤو موانع ذكور آيسلنديون"},
    {
        "suffix": "male wheelchair basketball players",
        "prefix": "canadian",
        "expected": "لاعبو كرة سلة على كراسي متحركة ذكور كنديون",
    },
    {
        "suffix": "men wheelchair racers",
        "prefix": "south african",
        "expected": "متسابقو كراسي متحركة رجال جنوب إفريقيون",
    },
    {"suffix": "men wheelchair racers", "prefix": "swiss", "expected": "متسابقو كراسي متحركة رجال سويسريون"},
    {"suffix": "men wheelchair racers", "prefix": "welsh", "expected": "متسابقو كراسي متحركة رجال ويلزيون"},
    {
        "suffix": "men's wheelchair basketball players",
        "prefix": "american",
        "expected": "لاعبو كرة سلة على كراسي متحركة رجالية أمريكيون",
    },
    {
        "suffix": "men's wheelchair basketball players",
        "prefix": "australian",
        "expected": "لاعبو كرة سلة على كراسي متحركة رجالية أستراليون",
    },
    {
        "suffix": "men's wheelchair basketball players",
        "prefix": "japanese",
        "expected": "لاعبو كرة سلة على كراسي متحركة رجالية يابانيون",
    },
    {"suffix": "multi-instrumentalists", "prefix": "argentine", "expected": "عازفون على عدة آلات أرجنتينيون"},
    {"suffix": "nuclear medicine physicians", "prefix": "american", "expected": "أطباء طب نووي أمريكيون"},
    {"suffix": "nuclear medicine physicians", "prefix": "canadian", "expected": "أطباء طب نووي كنديون"},
    {"suffix": "oncologists", "prefix": "egyptian", "expected": "أطباء أورام مصريون"},
    {"suffix": "oncologists", "prefix": "swedish", "expected": "أطباء أورام سويديون"},
    {"suffix": "pair skaters", "prefix": "norwegian", "expected": "متزلجون فنيون على الجليد نرويجيون"},
    {"suffix": "pan-africanists", "prefix": "south american", "expected": "وحدويون أفارقة أمريكيون جنوبيون"},
    {"suffix": "psychiatrists", "prefix": "pakistani", "expected": "أطباء نفسيون باكستانيون"},
    {"suffix": "short track speed skaters", "prefix": "norwegian", "expected": "متزلجون على مسار قصير نرويجيون"},
    {"suffix": "songwriters", "prefix": "argentine", "expected": "كتاب أغان أرجنتينيون"},
    {"suffix": "sport shooters", "prefix": "egyptian", "expected": "لاعبو رماية مصريون"},
    {"suffix": "sports businesspeople", "prefix": "canadian", "expected": "شخصيات أعمال رياضيون كنديون"},
    {"suffix": "sports coaches", "prefix": "albanian", "expected": "مدربو رياضة ألبان"},
    {"suffix": "television actors", "prefix": "peruvian", "expected": "ممثلو تلفزيون بيرويون"},
    {"suffix": "television chefs", "prefix": "british", "expected": "طباخو تلفاز بريطانيون"},
    {
        "suffix": "wheelchair basketball players",
        "prefix": "american",
        "expected": "لاعبو كرة سلة على كراسي متحركة أمريكيون",
    },
    {
        "suffix": "wheelchair basketball players",
        "prefix": "australian",
        "expected": "لاعبو كرة سلة على كراسي متحركة أستراليون",
    },
    {"suffix": "wheelchair curlers", "prefix": "american", "expected": "لاعبو كيرلنغ على الكراسي المتحركة أمريكيون"},
    {"suffix": "wheelchair curlers", "prefix": "british", "expected": "لاعبو كيرلنغ على الكراسي المتحركة بريطانيون"},
    {"suffix": "wheelchair curlers", "prefix": "canadian", "expected": "لاعبو كيرلنغ على الكراسي المتحركة كنديون"},
    {"suffix": "wheelchair curlers", "prefix": "chinese", "expected": "لاعبو كيرلنغ على الكراسي المتحركة صينيون"},
    {"suffix": "wheelchair curlers", "prefix": "danish", "expected": "لاعبو كيرلنغ على الكراسي المتحركة دنماركيون"},
    {"suffix": "wheelchair curlers", "prefix": "english", "expected": "لاعبو كيرلنغ على الكراسي المتحركة إنجليز"},
    {
        "suffix": "wheelchair curling champions",
        "prefix": "american",
        "expected": "أبطال الكيرلنغ على الكراسي المتحركة أمريكيون",
    },
    {
        "suffix": "wheelchair curling champions",
        "prefix": "canadian",
        "expected": "أبطال الكيرلنغ على الكراسي المتحركة كنديون",
    },
    {
        "suffix": "wheelchair discus throwers",
        "prefix": "american",
        "expected": "رماة قرص على الكراسي المتحركة أمريكيون",
    },
    {"suffix": "wheelchair fencers", "prefix": "spanish", "expected": "مبارزون على الكراسي المتحركة إسبان"},
    {"suffix": "wheelchair racers", "prefix": "american", "expected": "متسابقو كراسي متحركة أمريكيون"},
    {"suffix": "wheelchair racers", "prefix": "australian", "expected": "متسابقو كراسي متحركة أستراليون"},
    {"suffix": "wheelchair racers", "prefix": "french", "expected": "متسابقو كراسي متحركة فرنسيون"},
    {"suffix": "wheelchair rugby players", "prefix": "american", "expected": "لاعبو رجبي على كراسي متحركة أمريكيون"},
    {"suffix": "wheelchair rugby players", "prefix": "australian", "expected": "لاعبو رجبي على كراسي متحركة أستراليون"},
    {
        "suffix": "wheelchair tennis players",
        "prefix": "british",
        "expected": "لاعبو كرة مضرب على كراسي متحركة بريطانيون",
    },
    {"suffix": "wheelchair tennis players", "prefix": "turkish", "expected": "لاعبو كرة مضرب على كراسي متحركة أتراك"},
]


@pytest.mark.parametrize("item", EXAMPLES, ids=lambda x: make_cate(x))
@pytest.mark.dict
def test_jobs_real_examples(item) -> None:
    item["cate"] = f"{item['prefix']} {item['suffix']}"

    # Ensure clean cache per test
    jobs_with_nat_prefix.cache_clear()

    result = jobs_with_nat_prefix(item["cate"], item.get("prefix", ""), item.get("suffix", ""))

    assert result == item.get("expected", ""), error_show(item, result)


women_examples = [
    {"suffix": "female footballers", "prefix": "equatoguinean", "expected": "لاعبات كرة قدم غينيات استوائيات"},
    {"suffix": "female sport shooters", "prefix": "egyptian", "expected": "لاعبات رماية مصريات"},
    {"suffix": "women wheelchair racers", "prefix": "american", "expected": "متسابقات كراسي متحركة أمريكيات"},
    {"suffix": "women wheelchair racers", "prefix": "australian", "expected": "متسابقات كراسي متحركة أستراليات"},
    {"suffix": "women wheelchair racers", "prefix": "belgian", "expected": "متسابقات كراسي متحركة بلجيكيات"},
    {"suffix": "women wheelchair racers", "prefix": "brazilian", "expected": "متسابقات كراسي متحركة برازيليات"},
    {"suffix": "women wheelchair racers", "prefix": "british", "expected": "متسابقات كراسي متحركة بريطانيات"},
    {"suffix": "women wheelchair racers", "prefix": "canadian", "expected": "متسابقات كراسي متحركة كنديات"},
    {"suffix": "women wheelchair racers", "prefix": "chinese", "expected": "متسابقات كراسي متحركة صينيات"},
    {"suffix": "women wheelchair racers", "prefix": "dutch", "expected": "متسابقات كراسي متحركة هولنديات"},
    {"suffix": "women wheelchair racers", "prefix": "english", "expected": "متسابقات كراسي متحركة إنجليزيات"},
    {"suffix": "women wheelchair racers", "prefix": "finnish", "expected": "متسابقات كراسي متحركة فنلنديات"},
    {"suffix": "women wheelchair racers", "prefix": "irish", "expected": "متسابقات كراسي متحركة أيرلنديات"},
    {"suffix": "women wheelchair racers", "prefix": "japanese", "expected": "متسابقات كراسي متحركة يابانيات"},
    {"suffix": "women wheelchair racers", "prefix": "mexican", "expected": "متسابقات كراسي متحركة مكسيكيات"},
    {"suffix": "women wheelchair racers", "prefix": "scottish", "expected": "متسابقات كراسي متحركة إسكتلنديات"},
    {"suffix": "women wheelchair racers", "prefix": "swiss", "expected": "متسابقات كراسي متحركة سويسريات"},
    {"suffix": "women wheelchair racers", "prefix": "turkish", "expected": "متسابقات كراسي متحركة تركيات"},
    {"suffix": "women wheelchair racers", "prefix": "welsh", "expected": "متسابقات كراسي متحركة ويلزيات"},
    {"suffix": "women", "prefix": "european", "expected": "أوروبيات"},
    {"suffix": "women", "prefix": "polish", "expected": "بولنديات"},
    {
        "suffix": "women's wheelchair basketball players",
        "prefix": "american",
        "expected": "لاعبات كرة سلة على كراسي متحركة نسائية أمريكيات",
    },
    {
        "suffix": "women's wheelchair basketball players",
        "prefix": "australian",
        "expected": "لاعبات كرة سلة على كراسي متحركة نسائية أستراليات",
    },
    {
        "suffix": "women's wheelchair basketball players",
        "prefix": "british",
        "expected": "لاعبات كرة سلة على كراسي متحركة نسائية بريطانيات",
    },
    {
        "suffix": "women's wheelchair basketball players",
        "prefix": "canadian",
        "expected": "لاعبات كرة سلة على كراسي متحركة نسائية كنديات",
    },
    {
        "suffix": "women's wheelchair basketball players",
        "prefix": "dutch",
        "expected": "لاعبات كرة سلة على كراسي متحركة نسائية هولنديات",
    },
    {
        "suffix": "women's wheelchair basketball players",
        "prefix": "french",
        "expected": "لاعبات كرة سلة على كراسي متحركة نسائية فرنسيات",
    },
    {
        "suffix": "women's wheelchair basketball players",
        "prefix": "german",
        "expected": "لاعبات كرة سلة على كراسي متحركة نسائية ألمانيات",
    },
    {
        "suffix": "women's wheelchair basketball players",
        "prefix": "israeli",
        "expected": "لاعبات كرة سلة على كراسي متحركة نسائية إسرائيليات",
    },
    {
        "suffix": "women's wheelchair basketball players",
        "prefix": "turkish",
        "expected": "لاعبات كرة سلة على كراسي متحركة نسائية تركيات",
    },
]


@pytest.mark.parametrize("item", women_examples, ids=lambda x: make_cate(x))
@pytest.mark.dict
def test_womens(item) -> None:
    item["cate"] = f"{item['prefix']} {item['suffix']}"

    # Ensure clean cache per test
    jobs_with_nat_prefix.cache_clear()

    result = jobs_with_nat_prefix(item["cate"], item.get("prefix", ""), item.get("suffix", ""))

    assert result == item.get("expected", ""), error_show(item, result)

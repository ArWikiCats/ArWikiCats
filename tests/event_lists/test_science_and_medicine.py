#
from src import new_func_lab

data ={
    "Category:Egyptian oncologists": "تصنيف:أطباء أورام مصريون",
    "Category:Fish described in 1995": "تصنيف:أسماك وصفت في 1995",
    "Category:Mammals described in 2017": "تصنيف:ثدييات اكتشفت في 2017",
    "Category:Pakistani psychiatrists": "تصنيف:أطباء نفسيون باكستانيون",
    "Category:Research institutes established in 1900": "تصنيف:معاهد أبحاث أسست في 1900",
    "Category:Swedish oncologists": "تصنيف:أطباء أورام سويديون"
}


def ye_test_one_dataset(dataset):
    print(f"len of dataset: {len(dataset)}")
    org = {}
    diff = {}
    data = {x: v for x, v in dataset.items() if v}
    for cat, ar in data.items():
        result = new_func_lab(cat)
        if result == ar:
            assert result == ar
        else:
            org[cat] = ar
            diff[cat] = result

    assert org == diff

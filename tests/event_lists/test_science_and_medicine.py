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


def test_culture_and_mythology():
    print(f"len of data: {len(data)}")
    org, diff = ye_test_one_dataset(data, new_func_lab)
    assert org == diff

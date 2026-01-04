#
import pytest
from load_one_data import dump_diff, one_dump_test

from ArWikiCats import resolve_arabic_category_label

data1 = {

    "Category:Cultural depictions of American men": "تصنيف:تصوير ثقافي عن رجال أمريكيين",
    "Category:Cultural depictions of American people": "تصنيف:التصوير الثقافي للأمريكيين",
    "Category:Cultural depictions of Argentine men": "تصنيف:تصوير ثقافي عن رجال أرجنتينيين",
    "Category:Cultural depictions of Argentine people": "تصنيف:تصوير ثقافي عن أرجنتينيين",
    "Category:Cultural depictions of Assyrian people": "تصنيف:تصوير ثقافي عن آشوريين",
    "Category:Cultural depictions of Australian men": "تصنيف:تصوير ثقافي عن رجال أستراليين",
    "Category:Cultural depictions of Australian people": "تصنيف:تصوير ثقافي عن أستراليين",
    "Category:Cultural depictions of Austrian men": "تصنيف:تصوير ثقافي عن رجال نمساويين",
    "Category:Cultural depictions of Austrian people": "تصنيف:التصوير الثقافي للنمساويين",
    "Category:Cultural depictions of Bangladeshi people": "تصنيف:تصوير ثقافي عن أعلام بنغلاديشيين",
    "Category:Cultural depictions of Belgian men": "تصنيف:تصوير ثقافي عن رجال بلجيكيين",
    "Category:Cultural depictions of Belgian people": "تصنيف:تصوير ثقافي عن بلجيكيين",
    "Category:Cultural depictions of Bolivian men": "تصنيف:تصوير ثقافي عن رجال بوليفيين",
    "Category:Cultural depictions of Bolivian people": "تصنيف:تصوير ثقافي عن بوليفيين",
    "Category:Cultural depictions of Bosnia and Herzegovina people": "تصنيف:تصوير ثقافي عن بوسنيين",
    "Category:Cultural depictions of Brazilian people": "تصنيف:تصوير ثقافي عن برازيليين",
    "Category:Cultural depictions of British men": "تصنيف:تصوير ثقافي عن رجال بريطانيين",
    "Category:Cultural depictions of British people": "تصنيف:التصوير الثقافي للبريطانيين",
    "Category:Cultural depictions of Byzantine emperors": "تصنيف:تصوير ثقافي عن أباطرة بيزنطيين",
    "Category:Cultural depictions of Byzantine people": "تصنيف:تصوير ثقافي عن البيزنطيين",
    "Category:Cultural depictions of Canadian people": "تصنيف:تصوير ثقافي عن كنديين",
    "Category:Cultural depictions of Chilean people": "تصنيف:تصوير ثقافي عن تشيليين",
    "Category:Cultural depictions of Chinese men": "تصنيف:تصوير ثقافي عن رجال صينيين",
    "Category:Cultural depictions of Chinese monarchs": "تصنيف:تصوير ثقافي عن ملكيين صينيين",
    "Category:Cultural depictions of Chinese people": "تصنيف:تصوير ثقافي عن صينيين",
    "Category:Cultural depictions of Colombian people": "تصنيف:تصوير ثقافي لكولومبيين",
    "Category:Cultural depictions of Cuban people": "تصنيف:تصوير ثقافي لكوبيين",
    "Category:Cultural depictions of Czech people": "تصنيف:تصوير ثقافي عن تشيكيين",
    "Category:Cultural depictions of Danish monarchs": "تصنيف:تصوير ثقافي عن ملكيين دنماركيين",
    "Category:Cultural depictions of Danish people": "تصنيف:تصوير ثقافي عن دنماركيين",
    "Category:Cultural depictions of Dutch men": "تصنيف:تصوير ثقافي عن رجال هولنديين",
    "Category:Cultural depictions of Dutch people": "تصنيف:تصوير ثقافي لهولنديين",
    "Category:Cultural depictions of Egyptian men": "تصنيف:تصوير ثقافي لرجال مصريين",
    "Category:Cultural depictions of Egyptian people": "تصنيف:تصوير ثقافي لمصريين",
    "Category:Cultural depictions of Ethiopian people": "تصنيف:تصوير ثقافي عن إثيوبيين",
    "Category:Cultural depictions of Filipino people": "تصنيف:تصوير ثقافي عن الفلبينيين",
    "Category:Cultural depictions of French men": "تصنيف:تصوير ثقافي عن رجال فرنسيين",
    "Category:Cultural depictions of French people": "تصنيف:التصوير الثقافي للفرنسيين",
    "Category:Cultural depictions of Greek men": "تصنيف:تصوير ثقافي عن رجال يونانيين",
    "Category:Cultural depictions of Greek monarchs": "تصنيف:تصوير ثقافي عن ملكيين يونانيين",
    "Category:Cultural depictions of Greek people": "تصنيف:تصوير ثقافي ليونانيين",
    "Category:Cultural depictions of Hungarian men": "تصنيف:تصوير ثقافي عن رجال مجريين",
    "Category:Cultural depictions of Hungarian people": "تصنيف:تصوير ثقافي عن مجريين",
    "Category:Cultural depictions of Indian monarchs": "تصنيف:تصوير ثقافي عن ملكيين هنود",
    "Category:Cultural depictions of Iranian men": "تصنيف:تصوير ثقافي عن رجال إيرانيين",
    "Category:Cultural depictions of Iranian people": "تصنيف:تصوير ثقافي عن إيرانيين",
    "Category:Cultural depictions of Iraqi people": "تصنيف:تصوير ثقافي لعراقيين",
    "Category:Cultural depictions of Irish men": "تصنيف:تصوير ثقافي عن رجال أيرلنديين",
    "Category:Cultural depictions of Irish people": "تصنيف:تصوير ثقافي عن أيرلنديين",
    "Category:Cultural depictions of Israeli men": "تصنيف:تصوير ثقافي عن رجال إسرائيليين",
    "Category:Cultural depictions of Israeli people": "تصنيف:تصوير ثقافي للإسرائيليين",
    "Category:Cultural depictions of Italian men": "تصنيف:تصوير ثقافي عن رجال إيطاليين",
    "Category:Cultural depictions of Italian people": "تصنيف:تصوير ثقافي عن إيطاليين",
    "Category:Cultural depictions of Japanese men": "تصنيف:تصوير ثقافي عن رجال يابانيين",
    "Category:Cultural depictions of Japanese people": "تصنيف:التصوير الثقافي لليابانيين",
    "Category:Cultural depictions of Libyan people": "تصنيف:تصوير ثقافي لليبيين",
    "Category:Cultural depictions of Mexican men": "تصنيف:تصوير ثقافي عن رجال مكسيكيين",
    "Category:Cultural depictions of Mexican people": "تصنيف:تصوير ثقافي لمكسيكيين",
    "Category:Cultural depictions of Mongolian people": "تصنيف:تصوير ثقافي لمنغوليين",
    "Category:Cultural depictions of New Zealand people": "تصنيف:تصوير ثقافي عن نيوزيلنديين",
    "Category:Cultural depictions of North Korean people": "تصنيف:تصوير ثقافي عن كوريين شماليين",
    "Category:Cultural depictions of Norwegian men": "تصنيف:تصوير ثقافي عن رجال نرويجيين",
    "Category:Cultural depictions of Norwegian people": "تصنيف:تصوير ثقافي عن نرويجيين",
    "Category:Cultural depictions of Pakistani people": "تصنيف:تصوير ثقافي عن باكستانيين",
    "Category:Cultural depictions of Palestinian men": "تصنيف:تصوير ثقافي عن رجال فلسطينيين",
    "Category:Cultural depictions of Palestinian people": "تصنيف:تصوير ثقافي عن فلسطينيين",
    "Category:Cultural depictions of Polish men": "تصنيف:تصوير ثقافي عن رجال بولنديين",
    "Category:Cultural depictions of Polish people": "تصنيف:تصوير ثقافي لبولنديين",
    "Category:Cultural depictions of Portuguese people": "تصنيف:تصوير ثقافي عن البرتغاليين",
    "Category:Cultural depictions of Romanian people": "تصنيف:تصوير ثقافي عن رومانيين",
    "Category:Cultural depictions of Saudi Arabian men": "تصنيف:تصوير ثقافي عن رجال سعوديين",
    "Category:Cultural depictions of Saudi Arabian people": "تصنيف:تصوير ثقافي لسعوديين",
    "Category:Cultural depictions of Scottish men": "تصنيف:تصوير ثقافي عن رجال إسكتلنديين",
    "Category:Cultural depictions of Scottish people": "تصنيف:تصوير ثقافي عن إسكتلنديين",
    "Category:Cultural depictions of Serbian monarchs": "تصنيف:تصوير ثقافي عن ملكيين صرب",
    "Category:Cultural depictions of South African people": "تصنيف:تصوير ثقافي عن جنوب إفريقيين",
    "Category:Cultural depictions of South Korean people": "تصنيف:تصوير ثقافي عن كوريين جنوبيين",
    "Category:Cultural depictions of Sri Lankan people": "تصنيف:تصوير ثقافي عن أعلام سريلانكيين",
    "Category:Cultural depictions of Swedish men": "تصنيف:تصوير ثقافي عن رجال سويديين",
    "Category:Cultural depictions of Swedish people": "تصنيف:تصوير ثقافي عن سويديين",
    "Category:Cultural depictions of Swiss men": "تصنيف:تصوير ثقافي عن رجال سويسريين",
    "Category:Cultural depictions of Swiss people": "تصنيف:تصوير ثقافي عن سويسريين",
    "Category:Cultural depictions of Thai people": "تصنيف:تصوير ثقافي عن تايلنديين",
    "Category:Cultural depictions of Ugandan people": "تصنيف:تصوير ثقافي عن أوغنديين",
    "Category:Cultural depictions of Ukrainian men": "تصنيف:تصوير ثقافي عن رجال أوكرانيين",
    "Category:Cultural depictions of Ukrainian people": "تصنيف:تصوير ثقافي لأوكرانيين",
    "Category:Cultural depictions of Uruguayan people": "تصنيف:تصوير ثقافي عن أوروغويانيين",
    "Category:Cultural depictions of Venezuelan people": "تصنيف:تصوير ثقافي عن فنزويليين",
    "Category:Cultural depictions of Welsh men": "تصنيف:تصوير ثقافي عن رجال ويلزيين",
    "Category:Cultural depictions of Welsh people": "تصنيف:تصوير ثقافي عن ويلزيين",
    "Category:Cultural depictions of Yugoslav people": "تصنيف:تصوير ثقافي عن يوغسلافيين",
    "Category:Cultural depictions of ancient Greek people": "تصنيف:تصوير ثقافي ليونانيين قدماء",
    "Category:Cultural depictions of architects": "تصنيف:تصوير ثقافي لمعماريين",
    "Category:Cultural depictions of astronomers": "تصنيف:تصوير ثقافي عن فلكيين",
    "Category:Cultural depictions of chemists": "تصنيف:تصوير ثقافي عن كيميائيين",
    "Category:Cultural depictions of comedians": "تصنيف:تصوير ثقافي لكوميديين",
    "Category:Cultural depictions of diplomats": "تصنيف:تصوير ثقافي عن دبلوماسيين",
    "Category:Cultural depictions of economists": "تصنيف:تصوير ثقافي لاقتصاديين",
    "Category:Cultural depictions of journalists": "تصنيف:تصوير ثقافي لصحفيين",
    "Category:Cultural depictions of male monarchs": "تصنيف:تصوير ثقافي عن ملكيين ذكور",
    "Category:Cultural depictions of mathematicians": "تصنيف:تصوير ثقافي عن رياضياتيين",
    "Category:Cultural depictions of military officers": "تصنيف:تصوير ثقافي لضباط عسكريين",
    "Category:Cultural depictions of monarchs": "تصنيف:تصوير ثقافي عن ملكيين",
    "Category:Cultural depictions of musicians": "تصنيف:التصوير الثقافي للموسيقيين",
    "Category:Cultural depictions of occultists": "تصنيف:تصوير ثقافي لغموضيين",
    "Category:Cultural depictions of physicists": "تصنيف:تصوير ثقافي عن فيزيائيين",
    "Category:Cultural depictions of politicians": "تصنيف:تصوير ثقافي لسياسيين",
    "Category:Cultural depictions of religious leaders": "تصنيف:تصوير ثقافي لقادة دينيين",
    "Category:Cultural depictions of sports-people": "تصنيف:تصوير ثقافي لرياضيين",
    "Category:Cultural depictions of the Maccabees": "تصنيف:تصوير ثقافي عن مكابيين",
}

to_test = [
    ("text_to_fix_1", data1),
]


@pytest.mark.parametrize("name,data", to_test)
@pytest.mark.skip2
@pytest.mark.dump
def test_all_dump(name: str, data: dict[str, str]) -> None:
    expected, diff_result = one_dump_test(data, resolve_arabic_category_label)

    diff_result2 = {x: v for x, v in diff_result.items() if v}
    # dump_diff(diff_result2, name)

    expected2 = {x: v for x, v in expected.items() if v and x in diff_result2}
    # dump_diff(expected2, f"{name}_expected")

    save3 = [f"* [[:{v}]]>[[:{diff_result2[x]}]]" for x, v in expected.items() if v and x in diff_result2]
    dump_diff(save3, f"{name}_d", _sort=False)

    assert diff_result == expected, f"Differences found: {len(diff_result):,}, len all :{len(data):,}"

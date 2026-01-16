import pytest

from ArWikiCats.make_bots.countries_formats.p17_bot import get_p17_main

pop_format_test_data = {
}


@pytest.mark.parametrize("category, expected", pop_format_test_data.items(), ids=pop_format_test_data.keys())
@pytest.mark.fast
def test_get_p17_new(category: str, expected: str) -> None:
    result = get_p17_main(category)
    assert result == expected

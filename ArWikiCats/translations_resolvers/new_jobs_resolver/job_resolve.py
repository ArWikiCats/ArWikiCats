
import functools

from ...translations_formats import format_multi_data, MultiDataFormatterBase


class NatJobsResolver:
    def __init__(self, jobs_data, formatted_data, nats_data):
        self.formatted_data = formatted_data
        self.jobs_data = jobs_data
        self.nats_data = nats_data
        self._bot = None

    @functools.lru_cache(maxsize=1)
    def _create_bot(self) -> MultiDataFormatterBase:
        return format_multi_data(
            formatted_data=self.formatted_data,
            data_list=self.nats_data,
            key_placeholder="{en_nat}",
            value_placeholder="{ar_nat}",
            data_list2=self.jobs_data,
            key2_placeholder="{en_job}",
            value2_placeholder="{ar_job}",
            text_after="",
            text_before="the ",
            use_other_formatted_data=True,
            search_first_part=True,
        )

    @functools.lru_cache(maxsize=10000)
    def get_label(self, category: str) -> str:
        self._bot = self._create_bot()
        return self._bot.search_all(category)

    @functools.lru_cache(maxsize=10000)
    def search_all_category(self, category: str) -> str:
        self._bot = self._create_bot()
        return self._bot.search_all_category(category)

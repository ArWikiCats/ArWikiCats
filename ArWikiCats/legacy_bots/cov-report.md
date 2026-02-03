```pash
pytest tests/unit --cov ArWikiCats/legacy_bots/legacy_resolvers_bots
```

```cli
======================== tests coverage ===============================
____________________ coverage: platform win32, python 3.13.7-final-0 ____________

Name                                                                 Stmts   Miss  Cover
----------------------------------------------------------------------------------------
ArWikiCats\legacy_bots\__init__.py                                      17      5    71%
ArWikiCats\legacy_bots\common_resolver_chain.py                         46     16    65%
ArWikiCats\legacy_bots\data\__init__.py                                  3      0   100%
ArWikiCats\legacy_bots\data\mappings.py                                 29      0   100%
ArWikiCats\legacy_bots\end_start_bots\__init__.py                        4      0   100%
ArWikiCats\legacy_bots\end_start_bots\end_start_match.py                 4      0   100%
ArWikiCats\legacy_bots\end_start_bots\fax2.py                           36      3    92%
ArWikiCats\legacy_bots\end_start_bots\fax2_episodes.py                  19      0   100%
ArWikiCats\legacy_bots\end_start_bots\fax2_temp.py                      12      0   100%
ArWikiCats\legacy_bots\end_start_bots\utils.py                          27      2    93%
ArWikiCats\legacy_bots\legacy_resolvers_bots\__init__.py                 0      0   100%
ArWikiCats\legacy_bots\legacy_resolvers_bots\bot_2018.py                32      1    97%
ArWikiCats\legacy_bots\legacy_resolvers_bots\bys.py                     73      6    92%
ArWikiCats\legacy_bots\legacy_resolvers_bots\country2_label_bot.py     147     27    82%
ArWikiCats\legacy_bots\legacy_resolvers_bots\event_lab_bot.py          140     93    34%
ArWikiCats\legacy_bots\legacy_resolvers_bots\mk3.py                     90     73    19%
ArWikiCats\legacy_bots\legacy_resolvers_bots\with_years_bot.py         115     17    85%
ArWikiCats\legacy_bots\legacy_resolvers_bots\year_or_typeo.py          166    140    16%
ArWikiCats\legacy_bots\legacy_utils\__init__.py                          4      0   100%
ArWikiCats\legacy_bots\legacy_utils\data.py                              5      0   100%
ArWikiCats\legacy_bots\legacy_utils\fixing.py                           15      0   100%
ArWikiCats\legacy_bots\legacy_utils\joint_class.py                      40     12    70%
ArWikiCats\legacy_bots\legacy_utils\utils.py                            89     14    84%
ArWikiCats\legacy_bots\make_bots\__init__.py                             5      0   100%
ArWikiCats\legacy_bots\make_bots\bot.py                                 23      0   100%
ArWikiCats\legacy_bots\make_bots\check_bot.py                           20      7    65%
ArWikiCats\legacy_bots\make_bots\reg_result.py                          47      1    98%
ArWikiCats\legacy_bots\make_bots\table1_bot.py                          28      5    82%
ArWikiCats\legacy_bots\resolvers\__init__.py                             6      0   100%
ArWikiCats\legacy_bots\resolvers\arabic_label_builder.py               255     46    82%
ArWikiCats\legacy_bots\resolvers\country_resolver.py                   150     44    71%
ArWikiCats\legacy_bots\resolvers\factory.py                             27      1    96%
ArWikiCats\legacy_bots\resolvers\interface.py                           16     16     0%
ArWikiCats\legacy_bots\resolvers\separator_based_resolver.py            22      2    91%
ArWikiCats\legacy_bots\resolvers\sub_resolver.py                        22      1    95%
ArWikiCats\legacy_bots\tmp_bot.py                                       41      0   100%
ArWikiCats\legacy_bots\utils\__init__.py                                 3      0   100%
ArWikiCats\legacy_bots\utils\regex_hub.py                               14      0   100%
----------------------------------------------------------------------------------------
TOTAL                                                                 1792    532    70%
```

> write unit tests for these files

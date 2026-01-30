; isort ArWikiCats tests
; isort tests
; black ArWikiCats tests
; python -m cProfile -o profile_slow.prof -m pytest -m slow
; snakeviz profile_slow.prof
; python -m cProfile -o profile_slow.prof -s tottime -m pytest tests/event_lists/test_entertainment.py


# cd ArWikiCats/legacy_bots && pydeps . --only make2_new.ArWikiCats.legacy_bots

# Fix E402
```
autopep8 --in-place --recursive --select=E402 .
```

# Fix
```
ruff check --fix .
```

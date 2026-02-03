from pathlib import Path
import re

titles = [
    "Overview",
    "Getting-Started",
    "Architecture",
    "Resolution-Pipeline",
    "Data-Architecture",
    "Resolver-Chain-Priority-System",
    "Translation-Data",
    "Data-Aggregation-Pipeline",
    "Geographic-Data",
    "Jobs-and-Occupations",
    "Nationalities",
    "Sports-Data",
    "Films-and-Television",
    "Ministers-and-Political-Roles",
    "Resolver-System",
    "Time-Pattern-Resolvers",
    "Nationality-Resolvers",
    "Country-Name-Resolvers",
    "Job-Resolvers",
    "Sports-Resolvers",
    "Film-and-TV-Resolvers",
    "Legacy-Resolvers",
    "Formatting-System",
    "FormatDataBase-Architecture",
    "Single-Element-Formatters",
    "Multi-Element-Formatters",
    "Template-and-Placeholder-System",
    "Factory-Functions-and-Usage",
    "Utility-Systems",
    "Category-Normalization",
    "Suffix-Resolution-System",
    "Helper-Scripts",
    "Testing-and-Validation",
    "Test-Organization",
    "Domain-Specific-Test-Suites",
    "Test-Utilities",
    "Example-Data-and-Datasets",
    "Development-Guide",
    "Adding-Translation-Data",
    "Creating-New-Resolvers",
    "Code-Style-and-Standards",
    "Performance-Optimization"
]

replaces = {}

for i, title in enumerate(titles):
    replace_str = rf"[{title.replace('-', ' ')}]({i}.{title}.md)"

    # [Architecture](/ArWikiCats/ArWikiCats/3-architecture)
    find_str = rf"\[{title.replace("-", " ")}\]\(/ArWikiCats/ArWikiCats/[\d\.]+-{title.lower()}\)"
    replaces[find_str] = replace_str

    find_str2 = rf"\(/ArWikiCats/ArWikiCats/[\d\.]+-{title.lower()}\)"
    replaces[find_str2] = rf"({i}.{title}.md)"

work_dir = Path(__file__).parent

for md_file in work_dir.glob("*.md"):
    if md_file.name == "full.md":
        continue
    print(f"Processing file: {md_file.name}")
    file_text = md_file.read_text(encoding="utf-8")
    for find_str, replace_str in replaces.items():
        file_text = re.sub(find_str, replace_str, file_text)
    md_file.write_text(file_text, encoding="utf-8")

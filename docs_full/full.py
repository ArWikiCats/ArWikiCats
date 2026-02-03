from pathlib import Path

title = [
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

full_path = Path(__file__).parent / "full.md"

full_text = full_path.read_text(encoding="utf-8")

sections = full_text.split("<details>")

for i, section in enumerate(sections):
    section = f"<details>{section}" if i > 0 else section
    section_file = Path(__file__).parent / f"{title[i]}.md"
    section_file.write_text(section, encoding="utf-8")

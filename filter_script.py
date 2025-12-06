
import json

def filter_geographical_entries():
    input_filepath = 'ArWikiCats/translations/jsons/cities/yy2.json'
    non_geographical_filepath = 'ArWikiCats/translations/jsons/cities/yy2_non_geographical.json'

    # Define keywords to identify non-geographical entries
    non_geographical_keywords = [
        'university', 'institute', 'studios', 'clubs', 'school', 'college',
        'airlines', 'airport', 'company', 'association', 'society', 'organization',
        'magazine', 'journal', 'newspaper', 'film', 'series', 'music', 'band',
        'bridge', 'dam', 'station', 'stadium', 'museum', 'theatre', 'library',
        'hospital', 'clinic', 'center', 'centre', 'hotel', 'restaurant',
        'park', 'garden', 'zoo', 'monastery', 'cathedral', 'mosque', 'temple',
        'dynasty', 'empire', 'kingdom', 'war', 'battle', 'treaty', 'dynasty',
        'language', 'dialect', 'script', 'people', 'tribe', 'clan', 'family',
        'award', 'prize', 'medal', 'trophy', 'festival', 'championship',
        'party', 'movement', 'front', 'union', 'government', 'ministry',
        'department', 'agency', 'council', 'assembly', 'parliament',
        'court', 'prison', 'police', 'army', 'military', 'navy', 'air force'
    ]

    # Read the original JSON file
    with open(input_filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)

    geographical_entries = {}
    non_geographical_entries = {}

    # Separate entries based on keywords
    for key, value in data.items():
        is_non_geographical = False
        for keyword in non_geographical_keywords:
            if keyword in key.lower() or keyword in value.lower():
                is_non_geographical = True
                break

        if is_non_geographical:
            non_geographical_entries[key] = value
        else:
            geographical_entries[key] = value

    # Write the filtered geographical entries back to the original file
    with open(input_filepath, 'w', encoding='utf-8') as f:
        json.dump(geographical_entries, f, ensure_ascii=False, indent=4)

    # Write the non-geographical entries to a new file
    with open(non_geographical_filepath, 'w', encoding='utf-8') as f:
        json.dump(non_geographical_entries, f, ensure_ascii=False, indent=4)

    print(f"Filtering complete.")
    print(f"Geographical entries saved to: {input_filepath}")
    print(f"Non-geographical entries saved to: {non_geographical_filepath}")

if __name__ == '__main__':
    filter_geographical_entries()

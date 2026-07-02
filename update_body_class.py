import os

countries = [
    "australia",
    "canada",
    "japan",
    "new-zealand",
    "schengen",
    "south-korea",
    "uae",
    "uk",
    "usa"
]

for country in countries:
    filepath = f"{country}-visa/index.html"
    if not os.path.exists(filepath):
        print(f"File not found: {filepath}")
        continue
    
    with open(filepath, 'r') as f:
        content = f.read()

    # Replace <body> with <body class="country-page"> if not already there
    if '<body class="country-page">' not in content:
        new_content = content.replace('<body>', '<body class="country-page">')
        with open(filepath, 'w') as f:
            f.write(new_content)
        print(f"Updated {filepath}")
    else:
        print(f"Already updated {filepath}")

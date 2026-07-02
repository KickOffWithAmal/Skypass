import os
import re

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

    # 1. Remove the subtitle paragraph (done entirely from your home)
    content = re.sub(r'<p class="subtitle">done entirely from your home</p>\s*', '', content)

    # 2. Add id="checklist" to the services section if not present
    content = re.sub(
        r'<section class="services" style="padding-top: 60px;">', 
        r'<section id="checklist" class="services" style="padding-top: 60px;">', 
        content
    )

    # 3. Add View Checklist link below the Start New Application button
    # Find: <a href="#contact" class="btn-start-app">Start New Application</a>
    # Replace with: <a href="#contact" class="btn-start-app">Start New Application</a>\n        <a href="#checklist" class="view-checklist">View Checklist <i class="fa-solid fa-chevron-down"></i></a>
    button_pattern = r'<a href="#contact" class="btn-start-app">Start New Application</a>'
    new_links = (
        '<a href="#contact" class="btn-start-app">Start New Application</a>\n'
        '        <a href="#checklist" class="view-checklist">View Checklist <i class="fa-solid fa-chevron-down" style="margin-left: 5px;"></i></a>'
    )
    content = content.replace(button_pattern, new_links)

    with open(filepath, 'w') as f:
        f.write(content)
        
    print(f"Updated HTML for {country}")

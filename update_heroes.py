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

country_names = {
    "australia": "Australia",
    "canada": "Canada",
    "japan": "Japan",
    "new-zealand": "New Zealand",
    "schengen": "Schengen",
    "south-korea": "South Korea",
    "uae": "UAE",
    "uk": "UK",
    "usa": "USA"
}

images = {
    "australia": "australia.png",
    "canada": "canada.png",
    "japan": "japan.png",
    "new-zealand": "newzealand.png",
    "schengen": "europe.png",
    "south-korea": "korea.png",
    "uae": "dubai.png",
    "uk": "uk.png",
    "usa": "liberty.png"
}

for country in countries:
    filepath = f"{country}-visa/index.html"
    if not os.path.exists(filepath):
        print(f"File not found: {filepath}")
        continue
    
    with open(filepath, 'r') as f:
        content = f.read()

    # Find the current country-hero section
    # Usually it looks like: <section class="country-hero" style="...">\n<div class="section-header" ...>\n<h1>...</h1>\n<p>...</p>\n</div>\n</section>
    
    pattern = re.compile(r'<section class="country-hero" style="background-image: url\(\'\.\./assets/([^\']+)\'\);">(.*?)</section>', re.DOTALL)
    match = pattern.search(content)
    
    if match:
        image_name = match.group(1)
        name = country_names[country]
        
        replacement = f"""<section class="country-hero" style="background-image: url('../assets/{image_name}');">
    <div class="country-hero-content">
        <h1>{name} Visa for Indians</h1>
        <p class="subtitle">done entirely from your home</p>
        <div class="country-hero-stats">
            <div class="stat-item">
                <span class="stat-label">VALID</span>
                <span class="stat-value">UPTO 90 DAYS</span>
            </div>
            <div class="stat-item">
                <span class="stat-label">PURPOSE</span>
                <span class="stat-value">TOURISM</span>
            </div>
            <div class="stat-item">
                <span class="stat-label">TYPE</span>
                <span class="stat-value">STICKER</span>
            </div>
        </div>
        <a href="#contact" class="btn-start-app">Start New Application</a>
    </div>
</section>"""
        
        new_content = content[:match.start()] + replacement + content[match.end():]
        
        with open(filepath, 'w') as f:
            f.write(new_content)
        print(f"Updated {filepath}")
    else:
        print(f"Could not find hero section in {filepath}")

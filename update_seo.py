import os
import re

countries = {
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

for folder, name in countries.items():
    filepath = f"{folder}-visa/index.html"
    if not os.path.exists(filepath):
        print(f"File not found: {filepath}")
        continue
    
    with open(filepath, 'r') as f:
        content = f.read()

    new_title = f"{name} Visa for Indians | Apply Online - Skypass Visas"
    new_desc = f"Apply for your {name} Tourist and Visit Visa entirely from home. Skypass Visa Services offers expert {name} visa consultation for Indian passport holders with a 95%+ success rate."
    new_keywords = f"{name} visa for indians, {name} tourist visa, apply {name} visa online, {name} visa requirements, skypass visas"

    # Replace <title>
    content = re.sub(r'<title>.*?</title>', f'<title>{new_title}</title>', content, flags=re.IGNORECASE)
    
    # Replace <meta name="title" ...>
    content = re.sub(r'<meta name="title" content=".*?">', f'<meta name="title" content="{new_title}">', content, flags=re.IGNORECASE)
    
    # Replace <meta name="description" ...>
    content = re.sub(r'<meta name="description"\s*content=".*?">', f'<meta name="description"\n        content="{new_desc}">', content, flags=re.IGNORECASE | re.DOTALL)
    
    # Replace <meta name="keywords" ...>
    content = re.sub(r'<meta name="keywords"\s*content=".*?">', f'<meta name="keywords"\n        content="{new_keywords}">', content, flags=re.IGNORECASE | re.DOTALL)

    # Replace Open Graph title & desc
    content = re.sub(r'<meta property="og:title" content=".*?">', f'<meta property="og:title" content="{new_title}">', content, flags=re.IGNORECASE)
    content = re.sub(r'<meta property="og:description"\s*content=".*?">', f'<meta property="og:description"\n        content="{new_desc}">', content, flags=re.IGNORECASE | re.DOTALL)

    # Replace Twitter title & desc
    content = re.sub(r'<meta property="twitter:title" content=".*?">', f'<meta property="twitter:title" content="{new_title}">', content, flags=re.IGNORECASE)
    content = re.sub(r'<meta property="twitter:description"\s*content=".*?">', f'<meta property="twitter:description"\n        content="{new_desc}">', content, flags=re.IGNORECASE | re.DOTALL)

    with open(filepath, 'w') as f:
        f.write(content)
        
    print(f"Updated SEO for {name}")


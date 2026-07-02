import os
import re

categories = {
    "usa-visa": "B1/B2 (B2 for tourism)",
    "canada-visa": "Visitor Visa (TRV)",
    "australia-visa": "Subclass 600",
    "uk-visa": "Standard Visitor Visa",
    "schengen-visa": "Type C",
    "south-korea-visa": "C-3 (C-3-9 Tourism)",
    "japan-visa": "Temporary Visitor",
    "new-zealand-visa": "Visitor Visa",
    "uae-visa": "Tourist Visa"
}

for folder, value in categories.items():
    filepath = f"/Users/amal/Skypass/{folder}/index.html"
    if not os.path.exists(filepath):
        print(f"File not found: {filepath}")
        continue
        
    with open(filepath, 'r') as f:
        content = f.read()
        
    pattern = re.compile(
        r'(<span class="stat-label"><i class="fa-solid fa-tag"[^>]*></i>\s*)CATEGORY(\s*</span>\s*<span class="stat-value">)[^<]*(</span>)',
        re.IGNORECASE
    )
    
    content = pattern.sub(
        r'\g<1>CATEGORY\g<2>' + value + r'\g<3>',
        content
    )
    
    with open(filepath, 'w') as f:
        f.write(content)
        
    print(f"Updated Category for {folder} to: {value}")

import os
import re

visa_data = {
    "australia": {"valid": "UPTO 1 YEAR", "type": "E-VISA"},
    "canada": {"valid": "UPTO 10 YEARS", "type": "STICKER"},
    "japan": {"valid": "UPTO 90 DAYS", "type": "E-VISA"},
    "new-zealand": {"valid": "UPTO 2 YEARS", "type": "E-VISA"},
    "schengen": {"valid": "UPTO 6 MONTHS", "type": "STICKER"},
    "south-korea": {"valid": "UPTO 90 DAYS", "type": "STICKER"},
    "uae": {"valid": "UPTO 30/60 DAYS", "type": "E-VISA"},
    "uk": {"valid": "UPTO 6 MONTHS", "type": "STICKER"},
    "usa": {"valid": "UPTO 10 YEARS", "type": "STICKER"}
}

for country, data in visa_data.items():
    filepath = f"{country}-visa/index.html"
    if not os.path.exists(filepath):
        print(f"File not found: {filepath}")
        continue
    
    with open(filepath, 'r') as f:
        content = f.read()

    # We need to replace the stat-values. 
    # Because there might be some variations, we can use re.sub with a custom function or just replace blocks.
    
    # 1. Update VALID
    # Pattern to find: <span class="stat-label"><i ...></i> VALID</span>\s*<span class="stat-value">.*?</span>
    pattern_valid = re.compile(r'(<span class="stat-label">.*?VALID</span>\s*<span class="stat-value">)(.*?)(</span>)', re.IGNORECASE | re.DOTALL)
    content = pattern_valid.sub(r'\g<1>' + data["valid"] + r'\g<3>', content)
    
    # 2. Update PURPOSE
    pattern_purpose = re.compile(r'(<span class="stat-label">.*?PURPOSE</span>\s*<span class="stat-value">)(.*?)(</span>)', re.IGNORECASE | re.DOTALL)
    content = pattern_purpose.sub(r'\g<1>' + "VISIT/TOURISM" + r'\g<3>', content)

    # 3. Update TYPE
    pattern_type = re.compile(r'(<span class="stat-label">.*?TYPE</span>\s*<span class="stat-value">)(.*?)(</span>)', re.IGNORECASE | re.DOTALL)
    content = pattern_type.sub(r'\g<1>' + data["type"] + r'\g<3>', content)

    with open(filepath, 'w') as f:
        f.write(content)
    
    print(f"Updated {country} -> Valid: {data['valid']}, Type: {data['type']}")


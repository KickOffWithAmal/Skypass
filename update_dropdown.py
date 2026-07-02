import os
import re

folders = {
    "usa-visa": "USA",
    "canada-visa": "Canada",
    "australia-visa": "Australia",
    "uk-visa": "UK",
    "schengen-visa": "Schengen",
    "south-korea-visa": "South Korea",
    "japan-visa": "Japan",
    "new-zealand-visa": "New Zealand",
    "uae-visa": "UAE",
    ".": None # For root index.html
}

new_options = """<option value="" disabled>Select destination</option>
                                <option value="USA">USA</option>
                                <option value="Canada">Canada</option>
                                <option value="UK">United Kingdom</option>
                                <option value="Australia">Australia</option>
                                <option value="Schengen">Schengen Area</option>
                                <option value="South Korea">South Korea</option>
                                <option value="Japan">Japan</option>
                                <option value="New Zealand">New Zealand</option>
                                <option value="UAE">UAE</option>
                                <option value="Other">Other</option>"""

for folder, country_value in folders.items():
    if folder == ".":
        filepath = "/Users/amal/Skypass/index.html"
    else:
        filepath = f"/Users/amal/Skypass/{folder}/index.html"
        
    if not os.path.exists(filepath):
        print(f"Not found: {filepath}")
        continue
        
    with open(filepath, 'r') as f:
        content = f.read()

    # Replace the options inside <select id="country" ...> ... </select>
    pattern_options = re.compile(
        r'(<select\s+id="country"[^>]*>)\s*<option.*?</select>', 
        re.DOTALL
    )
    
    # We will replace the whole block up to </select> with the new options
    content = pattern_options.sub(
        r'\g<1>\n                                ' + new_options.replace('\n', '\n                                ').strip() + '\n                            </select>', 
        content
    )
    
    if country_value:
        # Check if the script block exists, if so update it. If not, maybe we can add it?
        # The user has the script block in the files already. Let's find it.
        script_pattern = re.compile(
            r"(if\s*\(\s*select\.options\[i\]\.value\s*===\s*')[^']*\1",
            re.DOTALL
        )
        if script_pattern.search(content):
            content = script_pattern.sub(f"if (select.options[i].value === '{country_value}'", content)
        else:
            # If script block doesn't exist, append it after </select>
            # Wait, let's see if the script block exists. Let's just do a specific replacement.
            script_pattern = re.compile(
                r"(if\s*\(\s*select\.options\[i\]\.value\s*===\s*')[^']*('\s*\))",
                re.DOTALL
            )
            content = script_pattern.sub(r"\g<1>" + country_value + r"\g<2>", content)

    with open(filepath, 'w') as f:
        f.write(content)
        
    print(f"Updated dropdown for {folder}")

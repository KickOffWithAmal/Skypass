import re

html = open('index.html', 'r').read()

flags = {
    'USA': '🇺🇸',
    'Canada': '🇨🇦',
    'Australia': '🇦🇺',
    'United Kingdom': '🇬🇧',
    'Schengen ': '🇪🇺', # Note space in original html
    'South Korea': '🇰🇷',
    'Japan': '🇯🇵',
    'New Zealand': '🇳🇿',
    'UAE': '🇦🇪'
}

def replace_card(match):
    country = match.group(1)
    flag = flags.get(country, '🏳️')
    
    new_content = f"""<div class="country-card-content">
                        <div class="card-hover-header">
                            <button class="apply-visa-btn">Apply for {country.strip()} Visa</button>
                        </div>
                        <div class="card-main-content">
                            <div class="country-title-container">
                                <div class="country-flag-icon">{flag}</div>
                                <h3>{country}</h3>
                            </div>
                            <div class="country-details">
                                <hr class="card-separator" />
                                <div class="specs-grid">
                                    <div class="spec-item">
                                        <span class="spec-label">TYPE</span>
                                        <span class="spec-value">E-VISA</span>
                                    </div>
                                    <div class="spec-item">
                                        <span class="spec-label">VALID</span>
                                        <span class="spec-value">90 DAYS</span>
                                    </div>
                                    <div class="spec-item">
                                        <span class="spec-label">FEES</span>
                                        <span class="spec-value">₹400</span>
                                    </div>
                                </div>
                                <div class="hover-extra-details">
                                    <hr class="card-separator" />
                                    <div class="docs-needed">
                                        <span class="spec-label">DOCUMENTS NEEDED:</span>
                                        <p>Passport</p>
                                    </div>
                                    <hr class="card-separator" />
                                    <button class="emergency-btn">
                                        <i class="far fa-clock"></i> Get emergency assistance
                                    </button>
                                </div>
                            </div>
                        </div>
                    </div>"""
    return new_content

# We want to replace `<div class="country-card-content">...</div>` with the new structure.
# The regex looks for `<div class="country-card-content">\s*<h3>(.*?)</h3>\s*<p class="ad-text">.*?</p>\s*</div>`
pattern = re.compile(r'<div class="country-card-content">\s*<h3>(.*?)</h3>\s*<p class="ad-text">.*?</p>\s*</div>', re.DOTALL)
new_html = pattern.sub(replace_card, html)

open('index.html', 'w').write(new_html)
print("Replaced!")

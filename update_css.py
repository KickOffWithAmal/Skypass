import re

css = open('css/styles.css', 'r').read()

# Replace existing .country-card-content to end of Countries section
# It is between `/* Card content styles */` and `/* Social Media Links */`

new_css = """/* Card content styles */
.country-card-content {
    position: absolute;
    bottom: 0;
    left: 0;
    right: 0;
    background: linear-gradient(to bottom, rgba(10,25,40,0) 0%, rgba(10,25,40,0.8) 30%, rgba(10,25,40,0.95) 100%);
    backdrop-filter: blur(10px);
    -webkit-backdrop-filter: blur(10px);
    -webkit-mask-image: linear-gradient(to bottom, transparent 0%, black 25%);
    mask-image: linear-gradient(to bottom, transparent 0%, black 25%);
    border-top: none;
    padding: 2rem 1.5rem 1.5rem 1.5rem;
    z-index: 2;
    box-sizing: border-box;
    display: flex;
    flex-direction: column;
}

.card-hover-header {
    max-height: 0;
    opacity: 0;
    overflow: hidden;
    transition: all 0.4s ease;
    text-align: right;
    margin-bottom: 0;
}

.country-card:hover .card-hover-header {
    max-height: 40px;
    opacity: 1;
    margin-bottom: 1rem;
}

.apply-visa-btn {
    background: rgba(255, 255, 255, 0.2);
    border: 1px solid rgba(255, 255, 255, 0.4);
    color: white;
    padding: 6px 12px;
    border-radius: 4px;
    font-size: 0.85rem;
    cursor: pointer;
    transition: all 0.2s ease;
}

.apply-visa-btn:hover {
    background: rgba(255, 255, 255, 0.4);
}

.country-title-container {
    text-align: center;
    transition: transform 0.4s ease;
    transform: translateY(10px);
}

.country-card:hover .country-title-container {
    transform: translateY(0);
}

.country-flag-icon {
    font-size: 1.8rem;
    margin-bottom: 0.5rem;
    display: inline-flex;
    justify-content: center;
    align-items: center;
    background: white;
    border-radius: 50%;
    width: 40px;
    height: 40px;
    box-shadow: 0 2px 5px rgba(0,0,0,0.2);
}

.country-card h3 {
    margin: 0;
    color: white;
    font-size: 1.6rem;
    font-weight: 700;
    font-family: 'Montserrat', sans-serif;
    letter-spacing: 1px;
}

.country-details {
    max-height: 0;
    opacity: 0;
    overflow: hidden;
    transition: all 0.5s cubic-bezier(0.4, 0, 0.2, 1);
}

.country-card:hover .country-details {
    max-height: 400px;
    opacity: 1;
    margin-top: 1rem;
}

.card-separator {
    border: none;
    border-top: 1px solid rgba(255, 255, 255, 0.15);
    margin: 1.2rem 0;
}

.specs-grid {
    display: flex;
    justify-content: space-between;
    text-align: center;
    padding: 0 0.5rem;
}

.spec-item {
    display: flex;
    flex-direction: column;
    gap: 0.4rem;
}

.spec-label {
    font-size: 0.75rem;
    color: rgba(255, 255, 255, 0.6);
    letter-spacing: 1.5px;
    font-weight: 600;
}

.spec-value {
    font-size: 1.05rem;
    color: white;
    font-weight: 700;
}

.hover-extra-details {
    /* Always show with details on hover based on mockup 2 */
}

.docs-needed {
    text-align: left;
    padding-left: 0.5rem;
}

.docs-needed p {
    margin: 0.4rem 0 0 0;
    color: white;
    font-weight: 600;
    font-size: 1rem;
}

.emergency-btn {
    width: 100%;
    background: rgba(255, 255, 255, 0.15);
    border: none;
    padding: 12px;
    color: white;
    border-radius: 20px;
    font-size: 0.95rem;
    font-weight: 600;
    cursor: pointer;
    transition: background 0.3s;
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 8px;
}

.emergency-btn:hover {
    background: rgba(255, 255, 255, 0.25);
}

"""

pattern = re.compile(r'/\* Card content styles \*/.*?/\* Social Media Links \*/', re.DOTALL)
new_content = pattern.sub(new_css + '\n/* Social Media Links */', css)

open('css/styles.css', 'w').write(new_content)
print("CSS updated!")

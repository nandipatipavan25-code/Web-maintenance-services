import re

# Read original main content
with open('main_content_extracted.html', 'r', encoding='utf-8') as f:
    raw_main = f.read()

# Split raw_main by <h2
h2_pattern = re.compile(r'(<h2[^>]*>.*?</h2>)', re.DOTALL | re.IGNORECASE)
parts = h2_pattern.split(raw_main)

# Parse FAQs from Part 58
faq_content = parts[58]
faq_intro_match = re.match(r'(\s*<p>[\s\S]*?</p>)', faq_content)
faq_intro = faq_intro_match.group(1) if faq_intro_match else ""
faq_pairs = re.findall(r'<button class="accordionc">([\s\S]*?)</button>\s*<div class="panelc">([\s\S]*?)</div>', faq_content)

# Parse Plans from Part 54
plans_full = parts[54]
row_start = plans_full.find('<div class="row"')
row_end = plans_full.find('</div>\n</div>\n</div>', row_start) + len('</div>\n</div>\n</div>')
plans_intro = plans_full[:row_start]
plans_closing = plans_full[row_end:]

# Deliverable tasks 1 to 10
deliv_data = [
    (7, 8, "01", "Software, Plugin & Theme Updates", "security"),
    (9, 10, "02", "Automated Daily Backups", "security"),
    (11, 12, "03", "Security & Malware Defense", "security"),
    (13, 14, "04", "24/7 Uptime Monitoring", "performance"),
    (15, 16, "05", "Performance & Speed Optimization", "performance"),
    (17, 18, "06", "Broken Link & Error Page Checks", "maintenance"),
    (19, 20, "07", "Content Updates & Freshness", "maintenance"),
    (21, 22, "08", "SSL Certificate Management", "security"),
    (23, 24, "09", "Database Optimization", "performance"),
    (25, 26, "10", "Analytics & Plain-English Reporting", "maintenance"),
]

# Read SVG logo
with open('gads_logo.svg', 'r', encoding='utf-8') as f:
    raw_svg_logo = f.read()
clean_svg_logo = re.sub(r'<\?xml[\s\S]*?\?>', '', raw_svg_logo).strip()

print("Base assets loaded. Ready to build 4 distinct high-converting versions.")

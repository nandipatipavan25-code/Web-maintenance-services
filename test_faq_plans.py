import re

with open('original_maintenance_page.html', 'r', encoding='utf-8') as f:
    full_html = f.read()

with open('modern_css.html', 'r', encoding='utf-8') as f:
    css_block = f.read()

with open('main_content_extracted.html', 'r', encoding='utf-8') as f:
    raw_main = f.read()

h2_pattern = re.compile(r'(<h2[^>]*>.*?</h2>)', re.DOTALL | re.IGNORECASE)
parts = h2_pattern.split(raw_main)

# Parse FAQs from Part 58
faq_raw = parts[58]
# Extract pairs of <button class="accordionc">...</button> and <div class="panelc">...</div>
faq_items = re.findall(r'<button class="accordionc">([\s\S]*?)</button>\s*<div class="panelc">([\s\S]*?)</div>', faq_raw)
print(f"Extracted FAQ items: {len(faq_items)}")

# Parse Plans from Part 54
plans_raw = parts[54]
# In plans_raw, there is intro, list, and the row with 3 panels
# Let's see the 3 panels
panel_items = re.findall(r'<div class="col-md-4">([\s\S]*?)</div>\s*</div>\s*</div>', plans_raw)
print(f"Extracted panel items: {len(panel_items)}")

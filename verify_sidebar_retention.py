import re

with open('main_content_extracted.html', 'r', encoding='utf-8') as f:
    orig_content = f.read()

with open('website-maintenance-sidebar-layout.html', 'r', encoding='utf-8') as f:
    sidebar_html = f.read()

orig_clean_words = re.findall(r'\b[A-Za-z0-9_]{3,}\b', orig_content)
print(f"Total words in original main content: {len(orig_clean_words)}")

missing = []
for w in set(orig_clean_words):
    if w not in sidebar_html:
        missing.append(w)

# Filter class names
missing = [w for w in missing if w not in ['accordionc', 'panelc']]
print(f"Unique words checked: {len(set(orig_clean_words))}")
print(f"Missing words: {len(missing)} (List: {missing})")

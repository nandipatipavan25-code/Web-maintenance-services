import re

with open('main_content_extracted.html', 'r', encoding='utf-8') as f:
    orig_content = f.read()

with open('unique-website-maintenance.html', 'r', encoding='utf-8') as f:
    unique_page = f.read()

orig_clean_words = re.findall(r'\b[A-Za-z0-9_]{3,}\b', orig_content)
print(f"Total words in original main content: {len(orig_clean_words)}")

missing = []
for w in set(orig_clean_words):
    if w not in unique_page:
        missing.append(w)

print(f"Unique words checked: {len(set(orig_clean_words))}")
print(f"Missing words: {len(missing)} (List: {missing})")

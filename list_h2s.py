import re

with open('main_content_extracted.html', 'r', encoding='utf-8') as f:
    raw = f.read()

h2s = re.findall(r'<h2[^>]*>(.*?)</h2>', raw, re.DOTALL | re.IGNORECASE)
for i, h in enumerate(h2s):
    print(f"{i+1}: {repr(h.strip())}")

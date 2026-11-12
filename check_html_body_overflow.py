with open('website-maintenance-variant-3.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
matches = re.findall(r'(\b(?:html|body)[^{]*\{[^}]*\})', text)
for m in matches:
    print('HTML/BODY RULE:')
    print(m)

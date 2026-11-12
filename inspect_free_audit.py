with open('website-maintenance-variant-3.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re

# Find the section with id="free-audit"
pos = text.find('id="free-audit"')
if pos != -1:
    print('FOUND free-audit section:')
    print(text[pos-100:pos+3500])
else:
    print('id="free-audit" not found, searching for "Fix Problems"')
    pos2 = text.find('Fix Problems')
    print(text[pos2-100:pos2+3500])

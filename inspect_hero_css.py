with open('website-maintenance-variant-3.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
for s in ['hero-banner-wrap', 'hero-banner-img', 'hero-bg-glow']:
    matches = re.findall(rf'(\.{s}\s*\{{[^}}]*\}})', text)
    print(f'=== {s} ===')
    for m in matches:
        print(m.strip())

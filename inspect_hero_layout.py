with open('website-maintenance-variant-3.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re

# Check where .sticky-right-sidebar is located in the HTML
pos = text.find('class="sticky-right-sidebar"')
print('Sidebar pos:', pos)
if pos != -1:
    print('Sidebar snippet:')
    print(text[pos-100:pos+300])

# Check where the hero section is located
pos_hero = text.find('hero-banner-wrap')
print('\nHero pos:', pos_hero)
if pos_hero != -1:
    print('Hero snippet:')
    print(text[pos_hero-100:pos_hero+300])

# Check CSS for .sticky-right-sidebar and .page-grid
for s in ['page-grid', 'sticky-right-sidebar', 'content-column']:
    m = re.findall(rf'(\.{s}\s*\{{[^}}]*\}})', text)
    print(f'\nCSS for {s} count: {len(m)}')
    for rule in m:
        print(rule.strip())

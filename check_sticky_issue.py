with open('website-maintenance-variant-3.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re

# 1. Find where sticky-subnav-bar is in the HTML
m = re.search(r'(.{0,100}<nav class="sticky-subnav-bar".*?</nav>.{0,100})', text, re.DOTALL)
if m:
    print('HTML Context:')
    print(m.group(1)[:500])

# 2. Check overflow on body, html, page-container, etc.
overflow_rules = re.findall(r'([^}]*overflow[^}]*\{[^}]*\})', text)
print(f'Overflow rules count: {len(overflow_rules)}')
for r in overflow_rules[:10]:
    print('---')
    print(r.strip())

# 3. Check all CSS rules for sticky-subnav-bar
subnav_rules = re.findall(r'([^}]*sticky-subnav-bar[^{]*\{[^}]*\})', text)
print(f'Sticky subnav rules count: {len(subnav_rules)}')
for r in subnav_rules:
    print('===')
    print(r.strip())

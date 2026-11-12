with open('website-maintenance-variant-3.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
scripts = re.findall(r'<script.*?</script>', text, re.DOTALL)
print(f"Total scripts: {len(scripts)}")
for i, s in enumerate(scripts):
    if 'subnav' in s.lower():
        print(f"=== Script {i+1} mentions subnav ===")
        print(s[:500])

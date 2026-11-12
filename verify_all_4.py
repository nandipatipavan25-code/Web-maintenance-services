import re, os

with open('main_content_extracted.html', 'r', encoding='utf-8') as f:
    orig_content = f.read()

orig_words = set(re.findall(r'\b[A-Za-z0-9_]{3,}\b', orig_content))
print(f"Total unique words to verify: {len(orig_words)}")

files = [
    'maintenance-v1-executive-trust.html',
    'maintenance-v2-cyber-sentinel.html',
    'maintenance-v3-interactive-quiz.html',
    'maintenance-v4-fast-action.html'
]

for fname in files:
    size = os.path.getsize(fname)
    with open(fname, 'r', encoding='utf-8') as f:
        html = f.read()
    
    missing = [w for w in orig_words if w not in html]
    # Filter out known class names that were replaced by clean tags
    missing = [w for w in missing if w not in ['accordionc', 'panelc']]
    
    has_logo = 'GADS%20LOGO-01.svg' in html or 'GADS LOGO-01.svg' in html
    has_hero_img = 'Website_Maintenance.jpg' in html
    
    print(f"File: {fname} | Size: {size:,} bytes | Missing words: {len(missing)} | Logo OK: {has_logo} | Hero Img OK: {has_hero_img}")

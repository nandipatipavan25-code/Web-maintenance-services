with open('website-maintenance-variant-3.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re

# Find hero-banner-wrap markup
pos = text.find('class="hero-banner-wrap"')
print(text[pos:pos+1500])

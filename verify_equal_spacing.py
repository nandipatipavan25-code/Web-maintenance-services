with open('website-maintenance.html', 'r', encoding='utf-8') as f:
    html = f.read()

import re
print("Has 170px fixed width:", 'width: 170px !important;' in html)
print("Has 28px margin (56px gap):", 'margin: 0 28px !important;' in html)
print("Has 150px max-width on img:", 'max-width: 150px !important;' in html)

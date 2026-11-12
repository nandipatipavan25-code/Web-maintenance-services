with open('website-maintenance.html', 'r', encoding='utf-8') as f:
    html = f.read()

import re
print('Has speed-odometer:', bool(re.search(r'id="speed-odometer"', html)))
print('Has odoUrlInput:', bool(re.search(r'id="odoUrlInput"', html)))
print('Has odoEnterBtn:', bool(re.search(r'id="odoEnterBtn"', html)))
print('Has odoResultsWrapper with display none:', 'id="odoResultsWrapper" style="display: none;' in html)

pos_odo = html.find('id="speed-odometer"')
pos_articles = html.find('id="related-articles"')
pos_main_end = html.find('</main>')

print('Pos speed-odometer:', pos_odo)
print('Pos related-articles:', pos_articles)
print('Pos </main>:', pos_main_end)
print('Correctly positioned as LAST element before </main>:', pos_articles < pos_odo < pos_main_end)

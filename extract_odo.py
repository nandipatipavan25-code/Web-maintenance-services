with open('website-maintenance.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
match = re.search(r'<section class="speed-odometer-box".*?</section>', text, re.DOTALL)
if match:
    print('Found section, length:', len(match.group(0)))
    with open('odo_snippet.html', 'w', encoding='utf-8') as out:
        out.write(match.group(0))
    print('Wrote to odo_snippet.html')

css_match = re.search(r'/\* =========================================================\s*INTERACTIVE WEBSITE SPEED ODOMETER STYLES.*?(?=/\* =========================================================|\n</style>)', text, re.DOTALL)
if css_match:
    print('Found CSS, length:', len(css_match.group(0)))
    with open('odo_css_snippet.css', 'w', encoding='utf-8') as out:
        out.write(css_match.group(0))
    print('Wrote to odo_css_snippet.css')

with open('odo_snippet.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
match = re.search(r'<svg class="gauge-svg".*?</svg>', text, re.DOTALL)
if match:
    print(match.group(0))

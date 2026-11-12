with open('website-maintenance.html', 'r', encoding='utf-8') as f:
    html = f.read()

import re
print("Has repeat(2, 1fr) for odo-metrics-grid:", 'grid-template-columns: repeat(2, 1fr) !important;' in html)
print("Has high-contrast Enter hint:", '⚡ Enter' in html)
print("Has emerald alert label:", 'Maintained by GA Digital' in html)
print("Has refined SVG needle pivot:", '<circle cx="135" cy="135" r="16"' in html)

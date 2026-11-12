with open('website-maintenance.html', 'r', encoding='utf-8') as f:
    html = f.read()

import re
print("Has audit-avatar-graphic (should be False in free-audit):", 'class="audit-avatar-graphic"' in html)
print("Has audit-inspection-matrix:", 'class="audit-inspection-matrix"' in html)
print("Has audit-guarantee-card:", 'class="audit-guarantee-card"' in html)
print("Has audit-form-inner:", 'class="audit-form-inner"' in html)

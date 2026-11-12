with open('website-maintenance.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()
for i, line in enumerate(lines):
    if 'id=' in line and ('section' in line or 'class="content-card' in line or 'class="audit-box' in line or 'class="speed-odometer' in line or 'class="clients' in line or '<nav' in line or '<div id=' in line):
        print(f'{i+1}: {line.strip()[:100]}')

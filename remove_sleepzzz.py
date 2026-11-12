import re

sleepzzz_block_pattern = r'\s*<a href="https://sleepzzz\.in/" target="_blank" rel="noopener noreferrer" class="client-logo-item" title="Sleepzzz Mattress">\s*<img src="images/clients/sleepzzz-mattress\.jpg" alt="Sleepzzz Mattress Logo" class="client-logo-img" loading="lazy">\s*</a>'

for fname in ['website-maintenance.html', 'website-maintenance-sidebar-layout.html']:
    with open(fname, 'r', encoding='utf-8') as f:
        content = f.read()

    matches = len(re.findall(sleepzzz_block_pattern, content))
    print(f"{fname}: found {matches} sleepzzz marquee blocks")
    content = re.sub(sleepzzz_block_pattern, '', content)

    with open(fname, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"Updated {fname}!")

# Update test_logos.html
with open('test_logos.html', 'r', encoding='utf-8') as f:
    t_content = f.read()

t_pattern = r'\s*<a href="https://sleepzzz\.in/".*?</a>'
t_content = re.sub(t_pattern, '', t_content, flags=re.DOTALL)

with open('test_logos.html', 'w', encoding='utf-8') as f:
    f.write(t_content)
print("Updated test_logos.html!")

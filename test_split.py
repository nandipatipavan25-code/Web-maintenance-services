import re

with open('main_content_extracted.html', 'r', encoding='utf-8') as f:
    raw = f.read()

# Let's split raw by <h2
h2_pattern = re.compile(r'(<h2[^>]*>.*?</h2>)', re.DOTALL | re.IGNORECASE)
parts = h2_pattern.split(raw)

print(f"Total parts after splitting by H2: {len(parts)}")
for i in range(0, min(15, len(parts))):
    print(f"Part {i} (len {len(parts[i])}): {parts[i][:80]!r}")

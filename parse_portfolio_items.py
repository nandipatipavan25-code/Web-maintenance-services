import re

with open('portfolio_raw.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Let's search for how portfolio items are structured
# Find all <a href="http... target="_blank">
external_links = re.findall(r'<a[^>]+href=["\'](https?://[^"\']+)["\'][^>]*>(.*?)</a>', html, re.DOTALL | re.IGNORECASE)
print(f"Total external links: {len(external_links)}")
for url, text in external_links:
    clean_text = re.sub(r'<[^>]+>', ' ', text).strip()
    if not any(k in url for k in ['facebook', 'instagram', 'twitter', 'linkedin', 'gadigitalsolutions', 'google', 'cdn', 'cdnjs', 'ajax', 'schema.org']):
        print(f"URL: {url} | Text: {clean_text[:60]}")

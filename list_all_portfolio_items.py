import re

with open('portfolio_raw.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Find all blocks in the page
items = re.findall(r'<div[^>]*class=["\'][^"\']*portfoliocenter[^"\']*["\'][^>]*>(.*?)</div>\s*</div>', html, re.DOTALL | re.IGNORECASE)
print(f"Total portfoliocenter blocks: {len(items)}")

results = []
for i, item in enumerate(items):
    img = re.search(r'<img[^>]+src=["\']([^"\']+)["\'][^>]*>', item)
    link = re.search(r'<a[^>]+href=["\']([^"\']+)["\'][^>]*>', item)
    title = re.search(r'<h[23][^>]*>(.*?)</h[23]>', item, re.DOTALL)
    
    src = img.group(1) if img else "None"
    href = link.group(1) if link else "None"
    t = re.sub(r'<[^>]+>', '', title.group(1)).strip() if title else "None"
    
    results.append((t, src, href))

print(f"Parsed {len(results)} items:")
for t, src, href in results:
    print(f"Title: {t:30} | Img: {src:55} | Link: {href}")

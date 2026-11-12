import re

with open('portfolio_raw.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Find all blocks with image3451 or in icons
icon_cards = re.findall(r'<div[^>]*class=["\'][^"\']*portfoliocenter[^"\']*bonclass[^"\']*["\'][^>]*>(.*?)</div>\s*</div>', html, re.DOTALL | re.IGNORECASE)
print(f"Total icon cards: {len(icon_cards)}")
for card in icon_cards:
    img = re.search(r'src=["\']([^"\']+)["\']', card)
    alt = re.search(r'alt=["\']([^"\']+)["\']', card)
    title = re.search(r'<h[23][^>]*>(.*?)</h[23]>', card, re.DOTALL)
    
    img_src = img.group(1) if img else "No img"
    alt_txt = alt.group(1) if alt else "No alt"
    title_txt = re.sub(r'<[^>]+>', '', title.group(1)).strip() if title else "No title"
    print(f"Title: {title_txt} | Alt: {alt_txt} | Src: {img_src}")

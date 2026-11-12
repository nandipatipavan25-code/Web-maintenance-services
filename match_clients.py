import re
import os

with open('portfolio_raw.html', 'r', encoding='utf-8') as f:
    html = f.read()

clients = [
    "PhiDimensions",
    "Tanatan",
    "Rasoi",
    "Deccan",
    "Teacher",
    "Bohemian",
    "Anish",
    "Himalaya",
    "Nivi",
    "GSM",
    "Healing Hastha",
    "Rajesh Reddy",
    "CPVIA",
    "Sleepzzz",
    "Duro Soft",
    "BNS"
]

print("=== SEARCHING IN PORTFOLIO_RAW.HTML ===")
for c in clients:
    matches = re.findall(rf'([^\n<]*{re.escape(c)}[^\n<]*)', html, re.IGNORECASE)
    # unique matches
    unique_m = list(set([m.strip() for m in matches if len(m.strip()) > 2]))[:5]
    print(f"\n--- Client: {c} ---")
    for um in unique_m:
        print(f"  {um}")

    # find img and links around match
    blocks = re.findall(rf'(<div[^>]*class=["\'][^"\']*portfoliocenter[^"\']*["\'][^>]*>.*?{re.escape(c)}.*?</div>\s*</div>)', html, re.DOTALL | re.IGNORECASE)
    if not blocks:
        # try any container
        blocks = re.findall(rf'(<div[^>]*>.*?{re.escape(c)}.*?</div>)', html, re.DOTALL | re.IGNORECASE)
    print(f"  Blocks found: {len(blocks)}")
    for b in blocks[:2]:
        img = re.search(r'<img[^>]+src=["\']([^"\']+)["\']', b, re.IGNORECASE)
        href = re.search(r'<a[^>]+href=["\']([^"\']+)["\']', b, re.IGNORECASE)
        print(f"    Img: {img.group(1) if img else 'None'} | Href: {href.group(1) if href else 'None'}")

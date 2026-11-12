import re
import json

with open('portfolio_raw.html', 'r', encoding='utf-8') as f:
    html = f.read()

clients = [
    "PhiDimensions",
    "Tanatan India",
    "Indian Rasoi",
    "Deccan Prime",
    "Teacher Plus",
    "Bohemian Soul",
    "Dr. Anish Anand",
    "Himalaya Exports",
    "Nivi Homes",
    "GSM Global",
    "Healing Hastha",
    "Dr. Rajesh Reddy",
    "CPVIA",
    "Sleepzzz Mattress",
    "Duro Soft Mattress",
    "BNS Development"
]

print("=== SEARCHING FOR CLIENTS IN PORTFOLIO HTML ===")
found_clients = {}

for client in clients:
    # search flexible regex
    words = client.split()
    pattern = r'\b' + r'\s*'.join(re.escape(w) for w in words)
    matches = list(re.finditer(pattern, html, re.IGNORECASE))
    print(f"{client}: {len(matches)} matches")
    
    # Check context around matches
    for m in matches[:2]:
        start = max(0, m.start() - 250)
        end = min(len(html), m.end() + 250)
        snippet = html[start:end]
        # find img tags in snippet
        imgs = re.findall(r'<img[^>]+>', snippet, re.IGNORECASE)
        print(f"  Context for {client}:")
        for img in imgs:
            print("    IMG:", img)

print("\n=== ALL IMAGES IN PORTFOLIO HTML ===")
all_imgs = re.findall(r'<img[^>]+src=["\']([^"\']+)["\'][^>]*>', html, re.IGNORECASE)
print(f"Total img tags: {len(all_imgs)}")
# print sample
for src in all_imgs[:30]:
    print(" ", src)

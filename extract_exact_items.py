import re

with open('portfolio_raw.html', 'r', encoding='utf-8') as f:
    html = f.read()

clients = [
    ("PhiDimensions", "phidimensions"),
    ("Tanatan India", "Tanatan"),
    ("Indian Rasoi", "India Rasoi"),
    ("Deccan Prime", "Deccan Prime"),
    ("Teacher Plus", "Teacher Plus"),
    ("Bohemian Soul", "Bohemian Soul"),
    ("Dr. Anish Anand", "Dr. Anish Anand"),
    ("Himalaya Exports", "Himalaya"),
    ("Nivi Homes", "Nivi Homes"),
    ("GSM Global", "GSM"),
    ("Healing Hastha", "Healing Hastha"),
    ("Dr. Rajesh Reddy", "Rajesh Reddy"),
    ("CPVIA", "CPVIA"),
    ("Sleepzzz Mattress", "Sleepzzz"),
    ("Duro Soft Mattress", "Duro Soft"),
    ("BNS Development", "BNS")
]

for name, kw in clients:
    pos = html.lower().find(kw.lower())
    if pos != -1:
        # get 500 chars before and after
        start = max(0, pos - 400)
        end = min(len(html), pos + 400)
        snippet = html[start:end]
        
        # find img src inside snippet
        imgs = re.findall(r'<img[^>]+src=["\']([^"\']+)["\']', snippet)
        links = re.findall(r'<a[^>]+href=["\']([^"\']+)["\']', snippet)
        print(f"=== {name} ===")
        print(f"  Img: {imgs}")
        print(f"  Links: {links}")
    else:
        print(f"=== {name} === NOT FOUND")

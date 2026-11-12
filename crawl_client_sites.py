import urllib.request
import re
import ssl
from urllib.parse import urljoin

ssl_ctx = ssl.create_default_context()
ssl_ctx.check_hostname = False
ssl_ctx.verify_mode = ssl.CERT_NONE

clients = [
    ("PhiDimensions", "https://phidimensions.com/"),
    ("Tanatan India", "https://tanatanindian.com/"),
    ("Indian Rasoi", "https://indiarasoi.co.uk/"),
    ("Deccan Prime", "https://www.deccanprime.com/"),
    ("Teacher Plus", "https://teacherplus.org/"),
    ("Bohemian Soul", "https://bohemiansoul.in/"),
    ("Dr. Anish Anand", "https://dranishanandphysician.com/"),
    ("Himalaya Exports", "https://himalaya-exports.com/"),
    ("Nivi Homes", "https://nivihomes.com.au/"),
    ("GSM Global", "https://gsmglobal.co.in/"),
    ("Healing Hastha", "https://healinghastha.com/"),
    ("Dr. Rajesh Reddy", "https://drrajeshreddy.com/"),
    ("CPVIA", "https://cpvia.com"),
    ("Sleepzzz Mattress", "https://sleepzzz.in/"),
    ("Duro Soft Mattress", "https://durosoftmattress.com/"),
    ("BNS Development", "https://bns-development.com/")
]

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

for name, url in clients:
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, context=ssl_ctx, timeout=8) as resp:
            html = resp.read().decode('utf-8', errors='ignore')
            # Look for logo imgs
            logos = re.findall(r'<img[^>]+src=["\']([^"\']*(?:logo|brand|header)[^"\']*)["\']', html, re.I)
            # Look for svg logos
            svg_logos = [l for l in re.findall(r'<img[^>]+src=["\']([^"\']+\.svg[^"\']*)["\']', html, re.I)]
            favs = re.findall(r'<link[^>]+rel=["\'][^"\']*(?:icon|shortcut)[^"\']*["\'][^>]+href=["\']([^"\']+)["\']', html, re.I)
            if not favs:
                favs = re.findall(r'<link[^>]+href=["\']([^"\']+)["\'][^>]+rel=["\'][^"\']*(?:icon|shortcut)[^"\']*["\']', html, re.I)
            
            clean_logos = [urljoin(url, l) for l in (logos + svg_logos)[:4]]
            clean_favs = [urljoin(url, f) for f in favs[:2]]
            print(f"=== {name} ({url}) ===")
            print(f"  Logos: {clean_logos}")
            print(f"  Favs:  {clean_favs}")
    except Exception as e:
        print(f"=== {name} ({url}) ERROR: {e} ===")

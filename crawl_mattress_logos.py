import urllib.request
import re
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5'
}

for site in ['https://sleepzzz.in/', 'https://durosoftmattress.com/']:
    try:
        req = urllib.request.Request(site, headers=headers)
        with urllib.request.urlopen(req, context=ctx, timeout=10) as r:
            html = r.read().decode('utf-8', errors='ignore')
            logos = re.findall(r'<img[^>]+src=["\']([^"\']*(?:logo|brand|header)[^"\']*)["\']', html, re.I)
            all_imgs = re.findall(r'<img[^>]+src=["\']([^"\']+)["\']', html, re.I)
            print(f"=== {site} ===")
            print("  Logos:", logos[:5])
            print("  First 5 imgs:", all_imgs[:5])
    except Exception as e:
        print(f"=== {site} ERROR: {e} ===")

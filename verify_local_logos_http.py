import urllib.request

logos = [
    "images/clients/phidimensions.png",
    "images/clients/tanatan-india.svg",
    "images/clients/indian-rasoi.svg",
    "images/clients/deccan-prime.svg",
    "images/clients/teacher-plus.png",
    "images/clients/bohemian-soul.png",
    "images/clients/dr-anish-anand.svg",
    "images/clients/himalaya-exports.webp",
    "images/clients/nivi-homes.webp",
    "images/clients/gsm-global.webp",
    "images/clients/healing-hastha.png",
    "images/clients/dr-rajesh-reddy.svg",
    "images/clients/cpvia.png",
    "images/clients/sleepzzz-mattress.jpg",
    "images/clients/duro-soft-mattress.jpg",
    "images/clients/bns-development.svg"
]

all_ok = True
for l in logos:
    url = f"http://localhost:8080/{l}"
    try:
        req = urllib.request.Request(url)
        with urllib.request.urlopen(req, timeout=5) as resp:
            code = resp.getcode()
            length = len(resp.read())
            print(f"[OK 200] {l:35} -> {length} bytes")
    except Exception as e:
        print(f"[FAIL]   {l:35} -> {e}")
        all_ok = False

print("\nAll 16 logos verified:", all_ok)

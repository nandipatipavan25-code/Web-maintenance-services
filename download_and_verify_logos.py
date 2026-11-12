import urllib.request
import urllib.parse
import os
import ssl

ssl_ctx = ssl.create_default_context()
ssl_ctx.check_hostname = False
ssl_ctx.verify_mode = ssl.CERT_NONE

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
}

client_sources = [
    {
        "id": "phidimensions",
        "name": "PhiDimensions",
        "website": "https://phidimensions.com/",
        "urls": [
            "https://phidimensions.com/wp-content/uploads/2025/06/logo-light-1024x256.png",
            "https://phidimensions.com/wp-content/uploads/2025/06/logo-light-1-1.png",
            "https://phidimensions.com/wp-content/uploads/2026/05/Phi-fav-icon.png"
        ],
        "filename": "phidimensions.png"
    },
    {
        "id": "tanatan",
        "name": "Tanatan India",
        "website": "https://tanatanindian.com/",
        "urls": ["https://gadigitalsolutions.com/images/portfolio/our-work-Images/Tanatan.jpg"],
        "filename": "tanatan-india.jpg"
    },
    {
        "id": "indian-rasoi",
        "name": "Indian Rasoi",
        "website": "https://indiarasoi.co.uk/",
        "urls": ["https://gadigitalsolutions.com/images/portfolio/our-work-Images/India%20Rasoi.jpg"],
        "filename": "indian-rasoi.jpg"
    },
    {
        "id": "deccan-prime",
        "name": "Deccan Prime",
        "website": "https://www.deccanprime.com/",
        "urls": ["https://gadigitalsolutions.com/images/portfolio/our-work-Images/Deccan%20Prime%20Solicators%20LLP.jpg"],
        "filename": "deccan-prime.jpg"
    },
    {
        "id": "teacher-plus",
        "name": "Teacher Plus",
        "website": "https://teacherplus.org/",
        "urls": ["https://gadigitalsolutions.com/images/portfolio/our-work-Images/Teacher%20Plus.jpg"],
        "filename": "teacher-plus.jpg"
    },
    {
        "id": "bohemian-soul",
        "name": "Bohemian Soul",
        "website": "https://bohemiansoul.in/",
        "urls": ["https://gadigitalsolutions.com/images/portfolio/our-work-Images/Bohemian%20Soul.jpg"],
        "filename": "bohemian-soul.jpg"
    },
    {
        "id": "dr-anish-anand",
        "name": "Dr. Anish Anand",
        "website": "https://dranishanandphysician.com/",
        "urls": ["https://gadigitalsolutions.com/images/portfolio/our-work-Images/Dr.%20Anish%20Anand.jpg"],
        "filename": "dr-anish-anand.jpg"
    },
    {
        "id": "himalaya-exports",
        "name": "Himalaya Exports",
        "website": "https://himalaya-exports.com/",
        "urls": ["https://gadigitalsolutions.com/images/portfolio/our-work-Images/Himalaya.webp"],
        "filename": "himalaya-exports.webp"
    },
    {
        "id": "nivi-homes",
        "name": "Nivi Homes",
        "website": "https://nivihomes.com.au/",
        "urls": ["https://gadigitalsolutions.com/images/portfolio/our-work-Images/Nivi%20Homes.jpg"],
        "filename": "nivi-homes.jpg"
    },
    {
        "id": "gsm-global",
        "name": "GSM Global",
        "website": "https://gsmglobal.co.in/",
        "urls": ["https://gadigitalsolutions.com/images/portfolio/our-work-Images/gsm.webp"],
        "filename": "gsm-global.webp"
    },
    {
        "id": "healing-hastha",
        "name": "Healing Hastha",
        "website": "https://healinghastha.com/",
        "urls": ["https://gadigitalsolutions.com/images/portfolio/our-work-Images/Healing%20Hastha.webp"],
        "filename": "healing-hastha.webp"
    },
    {
        "id": "dr-rajesh-reddy",
        "name": "Dr. Rajesh Reddy",
        "website": "https://drrajeshreddy.com/",
        "urls": ["https://gadigitalsolutions.com/images/portfolio/our-work-Images/Dr.%20Rajesh%20Reddy.jpg"],
        "filename": "dr-rajesh-reddy.jpg"
    },
    {
        "id": "cpvia",
        "name": "CPVIA",
        "website": "https://cpvia.com",
        "urls": ["https://gadigitalsolutions.com/images/portfolio/our-work-Images/CPVIA.webp"],
        "filename": "cpvia.webp"
    },
    {
        "id": "sleepzzz-mattress",
        "name": "Sleepzzz Mattress",
        "website": "https://sleepzzz.in/",
        "urls": ["https://gadigitalsolutions.com/images/portfolio/our-work-Images/Sleepzzz%20Mattress%20PVT%20LTD%20copy.jpg"],
        "filename": "sleepzzz-mattress.jpg"
    },
    {
        "id": "duro-soft-mattress",
        "name": "Duro Soft Mattress",
        "website": "https://durosoftmattress.com/",
        "urls": ["https://gadigitalsolutions.com/images/portfolio/our-work-Images/Duro%20Soft%20Mattress%20copy.jpg"],
        "filename": "duro-soft-mattress.jpg"
    },
    {
        "id": "bns-development",
        "name": "BNS Development",
        "website": "https://bns-development.com/",
        "urls": [
            "https://bns-development.com/logos/bns-logo-black.svg",
            "https://bns-development.com/logos/BNS%20LOGO-01.svg"
        ],
        "filename": "bns-development.svg"
    }
]

out_dir = os.path.join("images", "clients")
os.makedirs(out_dir, exist_ok=True)

success_count = 0
for client in client_sources:
    out_path = os.path.join(out_dir, client["filename"])
    downloaded = False
    for url in client["urls"]:
        try:
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req, context=ssl_ctx, timeout=15) as resp:
                data = resp.read()
                if len(data) > 100:  # Valid content
                    with open(out_path, "wb") as f:
                        f.write(data)
                    print(f"[OK] {client['name']:20} -> {client['filename']} ({len(data)} bytes) from {url}")
                    downloaded = True
                    success_count += 1
                    break
        except Exception as e:
            print(f"  Attempt failed for {url}: {e}")
    if not downloaded:
        print(f"[FAIL] Could not download logo for {client['name']}")

print(f"\nTotal downloaded: {success_count} / {len(client_sources)}")

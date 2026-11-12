import urllib.request
import os
import ssl

ssl_ctx = ssl.create_default_context()
ssl_ctx.check_hostname = False
ssl_ctx.verify_mode = ssl.CERT_NONE

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
}

client_logos = [
    {
        "name": "PhiDimensions",
        "url": "https://phidimensions.com/wp-content/uploads/2025/06/logo-light-1024x256.png",
        "file": "phidimensions.png"
    },
    {
        "name": "Tanatan India",
        "url": "https://tanatanindian.com/wp-content/uploads/2024/07/logo.svg",
        "file": "tanatan-india.svg"
    },
    {
        "name": "Indian Rasoi",
        "url": "https://indiarasoi.co.uk/wp-content/uploads/2024/08/Indain-Rasoi-Logo-01.svg",
        "file": "indian-rasoi.svg"
    },
    {
        "name": "Deccan Prime",
        "url": "https://deccanprime.com/wp-content/uploads/2024/08/Deccan-Prime-Solicitors-LLP-logo-1.svg",
        "file": "deccan-prime.svg"
    },
    {
        "name": "Teacher Plus",
        "url": "https://teacherplus.org/wp-content/uploads/2024/06/Teacher-Plus-logo-black.png",
        "file": "teacher-plus.png"
    },
    {
        "name": "Bohemian Soul",
        "url": "https://bohemiansoul.in/cdn/shop/files/Bohemian_soul_logo_final.png",
        "file": "bohemian-soul.png"
    },
    {
        "name": "Dr. Anish Anand",
        "url": "https://www.dranishanandphysician.com/wp-content/uploads/2024/06/DR-ANANDS-CLINIC-logo-2-01.svg",
        "file": "dr-anish-anand.svg"
    },
    {
        "name": "Himalaya Exports",
        "url": "https://gadigitalsolutions.com/images/portfolio/our-work-Images/Himalaya.webp",
        "file": "himalaya-exports.webp"
    },
    {
        "name": "Nivi Homes",
        "url": "https://nivihomes.com.au/assets/images/logo/logo.webp",
        "file": "nivi-homes.webp"
    },
    {
        "name": "GSM Global",
        "url": "https://gadigitalsolutions.com/images/portfolio/our-work-Images/gsm.webp",
        "file": "gsm-global.webp"
    },
    {
        "name": "Healing Hastha",
        "url": "https://healinghastha.com/wp-content/uploads/2025/06/Healing-Hastha-logo.png",
        "file": "healing-hastha.png"
    },
    {
        "name": "Dr. Rajesh Reddy",
        "url": "https://drrajeshreddy.com/images/Logo.svg",
        "file": "dr-rajesh-reddy.svg"
    },
    {
        "name": "CPVIA",
        "url": "https://cpvia.com/assets/images/header-logo.png",
        "file": "cpvia.png"
    },
    {
        "name": "Sleepzzz Mattress",
        "url": "https://gadigitalsolutions.com/images/portfolio/our-work-Images/Sleepzzz%20Mattress%20PVT%20LTD%20copy.jpg",
        "file": "sleepzzz-mattress.jpg"
    },
    {
        "name": "Duro Soft Mattress",
        "url": "https://gadigitalsolutions.com/images/portfolio/our-work-Images/Duro%20Soft%20Mattress%20copy.jpg",
        "file": "duro-soft-mattress.jpg"
    },
    {
        "name": "BNS Development",
        "url": "https://bns-development.com/logos/bns-logo-black.svg",
        "file": "bns-development.svg"
    }
]

out_dir = os.path.join("images", "clients")
os.makedirs(out_dir, exist_ok=True)

for item in client_logos:
    dest = os.path.join(out_dir, item["file"])
    try:
        req = urllib.request.Request(item["url"], headers=headers)
        with urllib.request.urlopen(req, context=ssl_ctx, timeout=15) as resp:
            data = resp.read()
            if len(data) > 100:
                with open(dest, "wb") as f:
                    f.write(data)
                print(f"[OK] {item['name']:20} -> {item['file']} ({len(data)} bytes)")
    except Exception as e:
        print(f"[FAIL] {item['name']:20} -> {e}")

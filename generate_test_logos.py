import os

logos = [
    {"name": "PhiDimensions", "file": "phidimensions.png", "url": "https://phidimensions.com/"},
    {"name": "Tanatan India", "file": "tanatan-india.svg", "url": "https://tanatanindian.com/"},
    {"name": "Indian Rasoi", "file": "indian-rasoi.svg", "url": "https://indiarasoi.co.uk/"},
    {"name": "Deccan Prime", "file": "deccan-prime.svg", "url": "https://www.deccanprime.com/"},
    {"name": "Teacher Plus", "file": "teacher-plus.png", "url": "https://teacherplus.org/"},
    {"name": "Bohemian Soul", "file": "bohemian-soul.png", "url": "https://bohemiansoul.in/"},
    {"name": "Dr. Anish Anand", "file": "dr-anish-anand.svg", "url": "https://dranishanandphysician.com/"},
    {"name": "Himalaya Exports", "file": "himalaya-exports.webp", "url": "https://himalaya-exports.com/"},
    {"name": "Nivi Homes", "file": "nivi-homes.webp", "url": "https://nivihomes.com.au/"},
    {"name": "GSM Global", "file": "gsm-global.webp", "url": "https://gsmglobal.co.in/"},
    {"name": "Healing Hastha", "file": "healing-hastha.png", "url": "https://healinghastha.com/"},
    {"name": "Dr. Rajesh Reddy", "file": "dr-rajesh-reddy.svg", "url": "https://drrajeshreddy.com/"},
    {"name": "CPVIA", "file": "cpvia.png", "url": "https://cpvia.com"},
    {"name": "Sleepzzz Mattress", "file": "sleepzzz-mattress.jpg", "url": "https://sleepzzz.in/"},
    {"name": "Duro Soft Mattress", "file": "duro-soft-mattress.jpg", "url": "https://durosoftmattress.com/"},
    {"name": "BNS Development", "file": "bns-development.svg", "url": "https://bns-development.com/"}
]

html = """<!DOCTYPE html>
<html>
<head>
<title>Our Clients - 16 Verified Logos</title>
<style>
body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; background: #f8fafc; padding: 40px; margin: 0; }
.container { max-width: 1200px; margin: 0 auto; }
h1 { font-size: 28px; color: #0f172a; text-align: center; margin-bottom: 8px; font-weight: 800; }
p.sub { text-align: center; color: #64748b; font-size: 15px; margin-bottom: 35px; }
.grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(240px, 1fr)); gap: 20px; }
.card { background: #ffffff; border: 1px solid #e2e8f0; border-radius: 12px; padding: 24px 20px; display: flex; flex-direction: column; align-items: center; justify-content: center; text-decoration: none; transition: all 0.25s ease; box-shadow: 0 1px 3px rgba(0,0,0,0.05); }
.card:hover { transform: translateY(-4px); box-shadow: 0 12px 24px -8px rgba(0,0,0,0.12); border-color: #cbd5e1; }
.logo-box { height: 75px; width: 100%; display: flex; align-items: center; justify-content: center; margin-bottom: 14px; }
.logo-box img { max-width: 85%; max-height: 65px; object-fit: contain; filter: grayscale(20%); transition: filter 0.25s ease; }
.card:hover .logo-box img { filter: grayscale(0%); }
.client-name { font-size: 14px; font-weight: 700; color: #1e293b; text-align: center; margin: 0; }
.client-badge { font-size: 11px; color: #0284c7; margin-top: 4px; font-weight: 500; display: flex; align-items: center; gap: 4px; }
</style>
</head>
<body>
<div class="container">
    <h1>Trusted by Industry Leaders</h1>
    <p class="sub">Delivering reliable website maintenance, security, and performance across 16+ growing enterprises.</p>
    <div class="grid">
"""

for item in logos:
    html += f"""
        <a href="{item['url']}" target="_blank" rel="noopener noreferrer" class="card">
            <div class="logo-box">
                <img src="images/clients/{item['file']}" alt="{item['name']} Logo" loading="lazy">
            </div>
            <div class="client-name">{item['name']}</div>
            <div class="client-badge">Visit Website ↗</div>
        </a>
    """

html += """
    </div>
</div>
</body>
</html>
"""

with open("test_logos.html", "w", encoding="utf-8") as f:
    f.write(html)
print("Updated test_logos.html successfully!")

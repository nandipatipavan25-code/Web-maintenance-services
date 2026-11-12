import re

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

def render_logo_items():
    out = ""
    for item in logos:
        out += f"""            <a href="{item['url']}" target="_blank" rel="noopener noreferrer" class="client-logo-item" title="{item['name']}">
              <img src="images/clients/{item['file']}" alt="{item['name']} Logo" class="client-logo-img" loading="lazy">
            </a>\n"""
    return out

# Generate Set A + Set B for seamless loop
logos_set_a = render_logo_items()
logos_set_b = render_logo_items()

new_clients_section = f"""<!-- OUR CLIENTS: AUTO HORIZONTAL SCROLLING MARQUEE (LOGO ONLY) -->
        <section class="clients-marquee-section" id="clients">
          <div class="clients-marquee-header">
            <span class="clients-marquee-badge">★ Proven Track Record</span>
            <h2 class="clients-marquee-title">Our Clients</h2>
            <p class="clients-marquee-sub">Trusted by fast-growing enterprises, healthcare leaders, e-commerce brands, and professional businesses.</p>
          </div>

          <!-- Infinite Auto-Horizontal Scrolling Logo Marquee -->
          <div class="clients-marquee-viewport">
            <div class="clients-marquee-track">
              <!-- Set A -->
{logos_set_a}
              <!-- Set B (Duplicate for continuous seamless marquee) -->
{logos_set_b}
            </div>
          </div>
        </section>"""

new_css = """
    /* =========================================================
       AUTO HORIZONTAL SCROLLING CLIENT LOGOS MARQUEE (LOGOS ONLY)
       ========================================================= */
    .clients-marquee-section {
      background: #ffffff;
      border: 1px solid #e2e8f0;
      border-radius: 14px;
      padding: 34px 0 28px;
      margin-top: 35px;
      margin-bottom: 35px;
      box-shadow: 0 4px 20px -2px rgba(15, 23, 42, 0.05);
      overflow: hidden;
      position: relative;
    }
    .clients-marquee-header {
      text-align: center;
      padding: 0 24px;
      margin-bottom: 24px;
    }
    .clients-marquee-badge {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      background: #e0f2fe;
      color: #0369a1;
      font-size: 11px;
      font-weight: 800;
      text-transform: uppercase;
      letter-spacing: 0.08em;
      padding: 4px 12px;
      border-radius: 9999px;
      margin-bottom: 10px;
    }
    .clients-marquee-title {
      font-size: 26px;
      font-weight: 800;
      color: #0f172a;
      margin: 0 0 8px 0;
      letter-spacing: -0.02em;
    }
    .clients-marquee-sub {
      font-size: 14.5px;
      color: #64748b;
      max-width: 620px;
      margin: 0 auto;
      line-height: 1.5;
    }
    .clients-marquee-viewport {
      position: relative;
      width: 100%;
      overflow: hidden;
      padding: 16px 0;
      background: #f8fafc;
      border-top: 1px solid #f1f5f9;
      border-bottom: 1px solid #f1f5f9;
      mask-image: linear-gradient(to right, transparent 0%, black 7%, black 93%, transparent 100%);
      -webkit-mask-image: linear-gradient(to right, transparent 0%, black 7%, black 93%, transparent 100%);
    }
    .clients-marquee-track {
      display: flex;
      align-items: center;
      width: max-content;
      animation: logoScrollHoriz 35s linear infinite;
    }
    .clients-marquee-track:hover {
      animation-play-state: paused;
    }
    @keyframes logoScrollHoriz {
      0% {
        transform: translateX(0);
      }
      100% {
        transform: translateX(-50%);
      }
    }
    .client-logo-item {
      display: inline-flex;
      align-items: center;
      justify-content: center;
      padding: 0 34px;
      height: 72px;
      text-decoration: none;
      cursor: pointer;
      flex-shrink: 0;
    }
    .client-logo-img {
      max-height: 52px;
      max-width: 165px;
      width: auto;
      height: auto;
      object-fit: contain;
      filter: grayscale(20%);
      opacity: 0.88;
      transition: all 0.25s cubic-bezier(0.16, 1, 0.3, 1);
    }
    .client-logo-item:hover .client-logo-img {
      filter: grayscale(0%);
      opacity: 1;
      transform: scale(1.09);
    }
    @media (max-width: 768px) {
      .client-logo-item {
        padding: 0 20px;
        height: 60px;
      }
      .client-logo-img {
        max-height: 42px;
        max-width: 130px;
      }
    }
"""

for filename in ['website-maintenance.html', 'website-maintenance-sidebar-layout.html']:
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Replace existing clients section
    old_section_pattern = r'<!-- OUR CLIENTS.*?-->\s*<section class="[^"]*" id="clients">.*?</section>'
    if re.search(old_section_pattern, content, re.DOTALL):
        content = re.sub(old_section_pattern, new_clients_section, content, flags=re.DOTALL)
        print(f"Replaced clients section in {filename}!")
    else:
        print(f"Warning: could not find old clients section in {filename}")

    # 2. Update CSS (replace .clients-section-card styles or append new)
    old_css_pattern = r'/\* =========================================================\s*OUR CLIENTS SECTION STYLES.*?(?=/\* =========================================================|\n</style>)'
    if re.search(old_css_pattern, content, re.DOTALL):
        content = re.sub(old_css_pattern, new_css + '\n', content, flags=re.DOTALL)
        print(f"Replaced clients CSS in {filename}!")
    else:
        # Append before </style>
        content = content.replace('</style>', new_css + '\n</style>', 1)
        print(f"Appended new clients CSS in {filename}!")

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"Saved {filename} successfully!")

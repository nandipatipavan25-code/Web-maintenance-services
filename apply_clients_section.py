import re

css_addition = """
    /* =========================================================
       OUR CLIENTS SECTION STYLES
       ========================================================= */
    .clients-section-card {
      background: #ffffff;
      border: 1px solid #e2e8f0;
      border-radius: 14px;
      padding: 34px 28px;
      margin-bottom: 35px;
      box-shadow: 0 4px 20px -2px rgba(15, 23, 42, 0.05);
    }
    .clients-header {
      text-align: center;
      margin-bottom: 28px;
    }
    .clients-badge {
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
    .clients-title {
      font-size: 26px;
      font-weight: 800;
      color: #0f172a;
      margin: 0 0 8px 0;
      letter-spacing: -0.02em;
    }
    .clients-subtitle {
      font-size: 14.5px;
      color: #64748b;
      max-width: 680px;
      margin: 0 auto;
      line-height: 1.55;
    }
    .clients-grid {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 16px;
    }
    @media (max-width: 992px) {
      .clients-grid {
        grid-template-columns: repeat(3, 1fr);
      }
    }
    @media (max-width: 640px) {
      .clients-grid {
        grid-template-columns: repeat(2, 1fr);
        gap: 12px;
      }
    }
    .client-card {
      background: #ffffff;
      border: 1px solid #e2e8f0;
      border-radius: 10px;
      padding: 18px 14px 14px 14px;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      text-decoration: none !important;
      transition: all 0.22s cubic-bezier(0.16, 1, 0.3, 1);
      box-shadow: 0 1px 3px rgba(0, 0, 0, 0.03);
      position: relative;
    }
    .client-card:hover {
      transform: translateY(-4px);
      border-color: #38bdf8;
      box-shadow: 0 10px 20px -5px rgba(2, 132, 199, 0.15);
    }
    .client-logo-wrap {
      width: 100%;
      height: 64px;
      display: flex;
      align-items: center;
      justify-content: center;
      margin-bottom: 10px;
    }
    .client-logo-img {
      max-width: 86%;
      max-height: 54px;
      object-fit: contain;
      transition: transform 0.22s ease, filter 0.22s ease;
      filter: grayscale(15%);
    }
    .client-card:hover .client-logo-img {
      filter: grayscale(0%);
      transform: scale(1.04);
    }
    .client-card-name {
      font-size: 12.5px;
      font-weight: 700;
      color: #1e293b;
      text-align: center;
      margin-top: 4px;
      line-height: 1.3;
    }
    .client-card-link-hint {
      font-size: 10.5px;
      color: #0284c7;
      font-weight: 600;
      margin-top: 3px;
      display: flex;
      align-items: center;
      gap: 3px;
      opacity: 0.85;
    }
    .client-card:hover .client-card-link-hint {
      opacity: 1;
      text-decoration: underline;
    }
"""

html_clients_section = """
        <!-- OUR CLIENTS -->
        <section class="clients-section-card" id="clients">
          <div class="clients-header">
            <span class="clients-badge">★ Proven Track Record</span>
            <h2 class="clients-title">Our Clients</h2>
            <p class="clients-subtitle">Delivering high-availability website maintenance, proactive security monitoring, and continuous optimization for industry leaders worldwide.</p>
          </div>
          <div class="clients-grid">
            <a href="https://phidimensions.com/" target="_blank" rel="noopener noreferrer" class="client-card" title="Visit PhiDimensions">
              <div class="client-logo-wrap">
                <img src="images/clients/phidimensions.png" alt="PhiDimensions Logo" class="client-logo-img" loading="lazy">
              </div>
              <div class="client-card-name">PhiDimensions</div>
              <div class="client-card-link-hint">Visit Site &rarr;</div>
            </a>
            <a href="https://tanatanindian.com/" target="_blank" rel="noopener noreferrer" class="client-card" title="Visit Tanatan India">
              <div class="client-logo-wrap">
                <img src="images/clients/tanatan-india.svg" alt="Tanatan India Logo" class="client-logo-img" loading="lazy">
              </div>
              <div class="client-card-name">Tanatan India</div>
              <div class="client-card-link-hint">Visit Site &rarr;</div>
            </a>
            <a href="https://indiarasoi.co.uk/" target="_blank" rel="noopener noreferrer" class="client-card" title="Visit Indian Rasoi">
              <div class="client-logo-wrap">
                <img src="images/clients/indian-rasoi.svg" alt="Indian Rasoi Logo" class="client-logo-img" loading="lazy">
              </div>
              <div class="client-card-name">Indian Rasoi</div>
              <div class="client-card-link-hint">Visit Site &rarr;</div>
            </a>
            <a href="https://www.deccanprime.com/" target="_blank" rel="noopener noreferrer" class="client-card" title="Visit Deccan Prime Solicitors">
              <div class="client-logo-wrap">
                <img src="images/clients/deccan-prime.svg" alt="Deccan Prime Logo" class="client-logo-img" loading="lazy">
              </div>
              <div class="client-card-name">Deccan Prime</div>
              <div class="client-card-link-hint">Visit Site &rarr;</div>
            </a>
            <a href="https://teacherplus.org/" target="_blank" rel="noopener noreferrer" class="client-card" title="Visit Teacher Plus">
              <div class="client-logo-wrap">
                <img src="images/clients/teacher-plus.png" alt="Teacher Plus Logo" class="client-logo-img" loading="lazy">
              </div>
              <div class="client-card-name">Teacher Plus</div>
              <div class="client-card-link-hint">Visit Site &rarr;</div>
            </a>
            <a href="https://bohemiansoul.in/" target="_blank" rel="noopener noreferrer" class="client-card" title="Visit Bohemian Soul">
              <div class="client-logo-wrap">
                <img src="images/clients/bohemian-soul.png" alt="Bohemian Soul Logo" class="client-logo-img" loading="lazy">
              </div>
              <div class="client-card-name">Bohemian Soul</div>
              <div class="client-card-link-hint">Visit Site &rarr;</div>
            </a>
            <a href="https://dranishanandphysician.com/" target="_blank" rel="noopener noreferrer" class="client-card" title="Visit Dr. Anish Anand">
              <div class="client-logo-wrap">
                <img src="images/clients/dr-anish-anand.svg" alt="Dr. Anish Anand Logo" class="client-logo-img" loading="lazy">
              </div>
              <div class="client-card-name">Dr. Anish Anand</div>
              <div class="client-card-link-hint">Visit Site &rarr;</div>
            </a>
            <a href="https://himalaya-exports.com/" target="_blank" rel="noopener noreferrer" class="client-card" title="Visit Himalaya Exports">
              <div class="client-logo-wrap">
                <img src="images/clients/himalaya-exports.webp" alt="Himalaya Exports Logo" class="client-logo-img" loading="lazy">
              </div>
              <div class="client-card-name">Himalaya Exports</div>
              <div class="client-card-link-hint">Visit Site &rarr;</div>
            </a>
            <a href="https://nivihomes.com.au/" target="_blank" rel="noopener noreferrer" class="client-card" title="Visit Nivi Homes">
              <div class="client-logo-wrap">
                <img src="images/clients/nivi-homes.webp" alt="Nivi Homes Logo" class="client-logo-img" loading="lazy">
              </div>
              <div class="client-card-name">Nivi Homes</div>
              <div class="client-card-link-hint">Visit Site &rarr;</div>
            </a>
            <a href="https://gsmglobal.co.in/" target="_blank" rel="noopener noreferrer" class="client-card" title="Visit GSM Global">
              <div class="client-logo-wrap">
                <img src="images/clients/gsm-global.webp" alt="GSM Global Logo" class="client-logo-img" loading="lazy">
              </div>
              <div class="client-card-name">GSM Global</div>
              <div class="client-card-link-hint">Visit Site &rarr;</div>
            </a>
            <a href="https://healinghastha.com/" target="_blank" rel="noopener noreferrer" class="client-card" title="Visit Healing Hastha">
              <div class="client-logo-wrap">
                <img src="images/clients/healing-hastha.png" alt="Healing Hastha Logo" class="client-logo-img" loading="lazy">
              </div>
              <div class="client-card-name">Healing Hastha</div>
              <div class="client-card-link-hint">Visit Site &rarr;</div>
            </a>
            <a href="https://drrajeshreddy.com/" target="_blank" rel="noopener noreferrer" class="client-card" title="Visit Dr. Rajesh Reddy">
              <div class="client-logo-wrap">
                <img src="images/clients/dr-rajesh-reddy.svg" alt="Dr. Rajesh Reddy Logo" class="client-logo-img" loading="lazy">
              </div>
              <div class="client-card-name">Dr. Rajesh Reddy</div>
              <div class="client-card-link-hint">Visit Site &rarr;</div>
            </a>
            <a href="https://cpvia.com" target="_blank" rel="noopener noreferrer" class="client-card" title="Visit CPVIA">
              <div class="client-logo-wrap">
                <img src="images/clients/cpvia.png" alt="CPVIA Logo" class="client-logo-img" loading="lazy">
              </div>
              <div class="client-card-name">CPVIA</div>
              <div class="client-card-link-hint">Visit Site &rarr;</div>
            </a>
            <a href="https://sleepzzz.in/" target="_blank" rel="noopener noreferrer" class="client-card" title="Visit Sleepzzz Mattress">
              <div class="client-logo-wrap">
                <img src="images/clients/sleepzzz-mattress.jpg" alt="Sleepzzz Mattress Logo" class="client-logo-img" loading="lazy">
              </div>
              <div class="client-card-name">Sleepzzz Mattress</div>
              <div class="client-card-link-hint">Visit Site &rarr;</div>
            </a>
            <a href="https://durosoftmattress.com/" target="_blank" rel="noopener noreferrer" class="client-card" title="Visit Duro Soft Mattress">
              <div class="client-logo-wrap">
                <img src="images/clients/duro-soft-mattress.jpg" alt="Duro Soft Mattress Logo" class="client-logo-img" loading="lazy">
              </div>
              <div class="client-card-name">Duro Soft Mattress</div>
              <div class="client-card-link-hint">Visit Site &rarr;</div>
            </a>
            <a href="https://bns-development.com/" target="_blank" rel="noopener noreferrer" class="client-card" title="Visit BNS Development">
              <div class="client-logo-wrap">
                <img src="images/clients/bns-development.svg" alt="BNS Development Logo" class="client-logo-img" loading="lazy">
              </div>
              <div class="client-card-name">BNS Development</div>
              <div class="client-card-link-hint">Visit Site &rarr;</div>
            </a>
          </div>
        </section>
"""

nav_link = '            <li><a href="#clients" class="side-nav-link"><span class="nav-num">★</span> Our Clients</a></li>\n'

for filename in ['website-maintenance.html', 'website-maintenance-sidebar-layout.html']:
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Add CSS before </style>
    if '.clients-section-card' not in content:
        content = content.replace('</style>', css_addition + '\n</style>', 1)

    # 2. Add sidebar nav item after #overview nav link
    if 'href="#clients"' not in content:
        overview_nav = '<li><a href="#overview" class="side-nav-link active"><span class="nav-num">01</span> Overview</a></li>'
        content = content.replace(overview_nav, overview_nav + '\n' + nav_link, 1)

    # 3. Add clients section before <!-- OVERVIEW -->
    if 'id="clients"' not in content:
        target_marker = '<!-- OVERVIEW -->'
        content = content.replace(target_marker, html_clients_section + '\n' + target_marker, 1)

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"Updated {filename} successfully!")

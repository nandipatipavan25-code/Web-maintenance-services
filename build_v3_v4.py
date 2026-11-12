import re
from builder_core import (
    parts, faq_intro, faq_pairs, plans_intro, plans_closing, 
    deliv_data, clean_svg_logo
)
from generate_4_versions import get_site_header, get_site_footer

# =========================================================================
# VERSION 3: THE "INTERACTIVE ASSESSMENT & GAMIFIED DIAGNOSTIC"
# Features live 45-sec interactive vulnerability quiz, dynamic risk calculator,
# category filter toolbar for deliverables, and gamified engagement.
# =========================================================================
def build_version_3():
    print("Building Version 3: Interactive Assessment & Gamified Diagnostic...")
    css = """
    :root {
      --primary: #2563eb;
      --primary-dark: #1d4ed8;
      --navy: #0f172a;
      --emerald: #10b981;
      --amber: #f59e0b;
      --red: #ef4444;
      --slate: #475569;
      --border: #e2e8f0;
    }
    * { box-sizing: border-box; margin: 0; padding: 0; }
    body { font-family: 'Plus Jakarta Sans', sans-serif; background: #ffffff; color: var(--navy); line-height: 1.7; font-size: 16px; }
    .wrap { max-width: 1180px; margin: 0 auto; padding: 0 20px; }
    h1 { font-size: 36px; font-weight: 800; line-height: 1.25; color: var(--navy); margin-bottom: 16px; }
    h2 { font-size: 24px; font-weight: 700; color: var(--navy); margin-bottom: 14px; }
    h3 { font-size: 19px; font-weight: 700; color: var(--navy); margin-bottom: 10px; }
    p { color: var(--slate); font-size: 16px; margin-bottom: 16px; }
    .card { background: #ffffff; border: 1px solid var(--border); border-radius: 14px; padding: 30px; margin-bottom: 30px; box-shadow: 0 4px 15px rgba(0,0,0,0.04); }
    
    /* Quiz Styling */
    .quiz-box { background: #0f172a; color: #ffffff; border-radius: 14px; padding: 28px; box-shadow: 0 10px 30px rgba(15, 23, 42, 0.15); border: 2px solid #38bdf8; }
    .quiz-box h3 { color: #38bdf8; font-size: 20px; margin-bottom: 8px; }
    .quiz-label { display: flex; align-items: center; gap: 10px; font-size: 13.5px; color: #e2e8f0; cursor: pointer; padding: 8px 10px; background: rgba(255,255,255,0.05); border-radius: 6px; margin-bottom: 8px; transition: background 0.2s; }
    .quiz-label:hover { background: rgba(255,255,255,0.1); }
    .quiz-label input { width: 16px; height: 16px; accent-color: #38bdf8; }
    .quiz-score-card { background: #1e293b; border-left: 4px solid #10b981; border-radius: 6px; padding: 12px 14px; margin: 15px 0; }
    
    .btn-quiz { background: #38bdf8; color: #0f172a !important; font-weight: 800; padding: 12px; border-radius: 6px; border: none; width: 100%; cursor: pointer; text-align: center; display: block; text-decoration: none; font-size: 14px; }
    .btn-quiz:hover { background: #7dd3fc; }

    /* Interactive Filterable Deliverables */
    .filter-pills { display: flex; gap: 8px; flex-wrap: wrap; margin: 15px 0 20px; }
    .filter-btn { background: #f1f5f9; border: 1px solid var(--border); border-radius: 20px; padding: 6px 14px; font-size: 13px; font-weight: 700; color: #475569; cursor: pointer; }
    .filter-btn.active, .filter-btn:hover { background: var(--primary); color: #ffffff; border-color: var(--primary); }
    .deliv-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(290px, 1fr)); gap: 20px; }
    .deliv-box { background: #ffffff; border: 1px solid var(--border); border-radius: 12px; padding: 22px; box-shadow: 0 2px 6px rgba(0,0,0,0.03); border-top: 4px solid var(--primary); }
    
    .plans-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(270px, 1fr)); gap: 20px; margin: 25px 0; }
    .plan-box { background: #ffffff; border: 1.5px solid var(--border); border-radius: 12px; display: flex; flex-direction: column; overflow: hidden; }
    .plan-header { background: #1e40af; color: #ffffff; padding: 16px; text-align: center; }
    .plan-header h3 { color: #ffffff !important; margin: 0; }
    .plan-body { padding: 20px; flex: 1; display: flex; flex-direction: column; }
    .plan-action { margin-top: auto; padding-top: 15px; }
    details { border: 1px solid var(--border); border-radius: 8px; margin-bottom: 10px; background: #ffffff; }
    summary { padding: 15px 20px; font-weight: 700; cursor: pointer; background: #f8fafc; list-style: none; display: flex; justify-content: space-between; }
    summary::-webkit-details-marker { display: none; }
    summary::after { content: '+'; color: var(--primary); font-size: 18px; }
    details[open] summary::after { content: '−'; }
    .faq-body { padding: 18px 20px; border-top: 1px solid var(--border); }
    """

    deliv_html = "".join([f"""
      <div class="deliv-box" data-cat="{cat}">
        <span style="font-size: 11px; font-weight: 800; color: #2563eb; background: #dbeafe; padding: 3px 8px; border-radius: 4px; display: inline-block; margin-bottom: 8px;">TASK #{num}</span>
        {re.sub(r'<h2[^>]*>', '<h2>', parts[h])}
        {parts[b]}
      </div>
    """ for h, b, num, _, cat in deliv_data])

    faq_html = "".join([f"""
      <details>
        <summary>{q.strip()}</summary>
        <div class="faq-body">{a.strip()}</div>
      </details>
    """ for q, a in faq_pairs])

    doc = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Website Maintenance Services | GA Digital Interactive Diagnostic Edition</title>
  <link rel="icon" href="https://www.gadigitalsolutions.com/images/logo.png" type="image/png">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;600;700;800&display=swap" rel="stylesheet">
  <style>{css}</style>
</head>
<body>
  {get_site_header("light")}

  <main class="wrap" style="margin-top: 35px;">
    <!-- HERO SECTION -->
    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 35px; align-items: start; margin-bottom: 40px;">
      <div>
        <div style="border-radius: 12px; overflow: hidden; margin-bottom: 20px; box-shadow: 0 4px 15px rgba(0,0,0,0.06); border: 1px solid #e2e8f0;">
          <img src="https://www.gadigitalsolutions.com/images/Website_Maintenance.jpg" width="820" height="460" alt="Website Maintenance" style="width: 100%; height: auto; display: block;">
        </div>
        {parts[0]}
        
        <div style="display: flex; flex-wrap: wrap; gap: 10px; margin: 18px 0 25px;">
          <span style="background: #f1f5f9; border: 1px solid #e2e8f0; padding: 6px 12px; border-radius: 6px; font-size: 12px; font-weight: 700;">🛡️ 24/7 Monitoring</span>
          <span style="background: #f1f5f9; border: 1px solid #e2e8f0; padding: 6px 12px; border-radius: 6px; font-size: 12px; font-weight: 700;">⚡ Staging Testing</span>
          <span style="background: #f1f5f9; border: 1px solid #e2e8f0; padding: 6px 12px; border-radius: 6px; font-size: 12px; font-weight: 700;">💾 Daily Cloud Backups</span>
          <span style="background: #f1f5f9; border: 1px solid #e2e8f0; padding: 6px 12px; border-radius: 6px; font-size: 12px; font-weight: 700;">⏱️ 30-Min SLA</span>
        </div>

        {parts[1]}
        {parts[2]}
      </div>

      <!-- INTERACTIVE 45-SECOND RISK QUIZ CARD -->
      <div class="quiz-box" style="position: sticky; top: 90px;">
        <span style="background: rgba(56, 189, 248, 0.2); color: #38bdf8; font-size: 11px; font-weight: 800; text-transform: uppercase; padding: 4px 8px; border-radius: 4px;">Self-Diagnostic</span>
        <h3>⚡ 45-Second Website Health Quiz</h3>
        <p style="font-size: 13px; color: #94a3b8; margin-bottom: 12px;">Select all that apply to your website right now:</p>
        
        <label class="quiz-label">
          <input type="checkbox" class="q-check" value="25" onchange="runQuiz()"> CMS or plugins haven't been updated in 30+ days
        </label>
        <label class="quiz-label">
          <input type="checkbox" class="q-check" value="25" onchange="runQuiz()"> No automated daily off-site cloud backups
        </label>
        <label class="quiz-label">
          <input type="checkbox" class="q-check" value="25" onchange="runQuiz()"> Mobile load speed takes longer than 3 seconds
        </label>
        <label class="quiz-label">
          <input type="checkbox" class="q-check" value="25" onchange="runQuiz()"> Nobody is monitoring if the site crashes at 2 AM
        </label>

        <div class="quiz-score-card" id="q-card">
          <strong id="q-score" style="color: #10b981; font-size: 13px;">STATUS: HEALTHY (0 Vulnerabilities)</strong>
          <p id="q-text" style="color: #cbd5e1; font-size: 12px; margin: 4px 0 0;">Check the boxes above to calculate your vulnerability level.</p>
        </div>

        <form onsubmit="event.preventDefault(); window.location.href='https://wa.me/919849574618?text=Diagnostic%20Result%20for:%20' + encodeURIComponent(this.site.value);">
          <input type="url" name="site" placeholder="Enter your website URL" required style="width: 100%; padding: 10px; border-radius: 6px; border: 1px solid #334155; background: #1e293b; color: #fff; margin-bottom: 8px;">
          <button type="submit" class="btn-quiz">Get Detailed Fix Recommendations &rarr;</button>
        </form>
      </div>
    </div>

    <!-- OVERVIEW -->
    <div class="card" id="overview" style="border-left: 5px solid #2563eb;">
      {parts[3]}
      {parts[4]}
    </div>

    <!-- 10 DELIVERABLES WITH INTERACTIVE FILTER PILLS -->
    <div id="deliverables" style="margin-bottom: 35px;">
      <div class="card" style="margin-bottom: 15px;">
        {parts[5]}
        {parts[6]}
        <div class="filter-pills">
          <button class="filter-btn active" onclick="filterBox('all', this)">All 10 Tasks</button>
          <button class="filter-btn" onclick="filterBox('security', this)">🛡️ Security &amp; Backups</button>
          <button class="filter-btn" onclick="filterBox('performance', this)">⚡ Speed &amp; Uptime</button>
          <button class="filter-btn" onclick="filterBox('maintenance', this)">🛠️ Content &amp; Health</button>
        </div>
      </div>
      <div class="deliv-grid">
        {deliv_html}
      </div>
    </div>

    <!-- WHY IT MATTERS -->
    <div class="card" id="why-matters">
      {parts[27]}
      {parts[28]}
      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 15px; margin-top: 18px;">
        <div style="border: 1px solid #e2e8f0; border-radius: 8px; padding: 18px; border-top: 3px solid #10b981;">{parts[29]}{parts[30]}</div>
        <div style="border: 1px solid #e2e8f0; border-radius: 8px; padding: 18px; border-top: 3px solid #ef4444;">{parts[31]}{parts[32]}</div>
        <div style="border: 1px solid #e2e8f0; border-radius: 8px; padding: 18px; border-top: 3px solid #f59e0b;">{parts[33]}{parts[34]}</div>
        <div style="border: 1px solid #e2e8f0; border-radius: 8px; padding: 18px; border-top: 3px solid #2563eb;">{parts[35]}{parts[36]}</div>
      </div>
    </div>

    <!-- COST OF NEGLECT -->
    <div class="card" style="border-left: 5px solid #f59e0b; background: #fffbeb;" id="cost-neglect">
      {parts[37]}
      {parts[38]}
    </div>

    <!-- SCHEDULE -->
    <div class="card">
      {parts[39]}
      {parts[40]}
    </div>

    <!-- DIY VS PRO -->
    <div class="card">
      {parts[41]}
      {parts[42]}
      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 15px; margin: 18px 0;">
        <div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 18px;">{parts[43]}{parts[44]}</div>
        <div style="background: #f0fdf4; border: 1px solid #bbf7d0; border-radius: 8px; padding: 18px;">{parts[45]}{parts[46]}</div>
      </div>
      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 15px; margin: 18px 0;">
        <div style="background: #fef2f2; border: 1px solid #fecaca; border-radius: 8px; padding: 18px;">{parts[47]}{parts[48]}</div>
        <div style="background: #eff6ff; border: 1px solid #bfdbfe; border-radius: 8px; padding: 18px;">{parts[49]}{parts[50]}</div>
      </div>
      <div style="margin-top: 25px; border-top: 1px solid #e2e8f0; padding-top: 20px;">
        {parts[51]}
        {parts[52]}
      </div>
    </div>

    <!-- PLANS & PRICING -->
    <div class="card" id="plans" style="background: #f8fafc;">
      {parts[53]}
      {plans_intro}
      <div class="plans-grid">
        <div class="plan-box">
          <div class="plan-header"><h3>Essential</h3></div>
          <div class="plan-body">
            <p><strong>For brochure websites and small business sites</strong></p>
            <p>Ideal for: standard websites with stable content and moderate visitor traffic</p>
            <div class="plan-action">
              <a href="https://wa.me/919849574618?text=Hi%20GA%20Digital,%20I%20am%20interested%20in%20the%20Essential%20Website%20Maintenance%20Plan" style="background:#2563eb; color:#fff; text-align:center; padding:10px; border-radius:6px; display:block; text-decoration:none; font-weight:700;" target="_blank" rel="noopener noreferrer">Enquire on WhatsApp &rarr;</a>
            </div>
          </div>
        </div>
        <div class="plan-box" style="border: 2px solid #2563eb; box-shadow: 0 4px 15px rgba(37, 99, 235, 0.15);">
          <div class="plan-header" style="background: #2563eb;"><h3>Growth</h3></div>
          <div class="plan-body">
            <p><strong>For websites actively generating leads</strong></p>
            <p>Ideal for: businesses relying on their website for consistent lead generation</p>
            <div class="plan-action">
              <a href="https://wa.me/919849574618?text=Hi%20GA%20Digital,%20I%20am%20interested%20in%20the%20Growth%20Website%20Maintenance%20Plan" style="background:#2563eb; color:#fff; text-align:center; padding:10px; border-radius:6px; display:block; text-decoration:none; font-weight:700;" target="_blank" rel="noopener noreferrer">Enquire on WhatsApp &rarr;</a>
            </div>
          </div>
        </div>
        <div class="plan-box">
          <div class="plan-header"><h3>Business</h3></div>
          <div class="plan-body">
            <p><strong>For e-commerce, booking platforms, and high-traffic sites</strong></p>
            <p>Ideal for: e-commerce stores and businesses with significant revenue dependence on their website</p>
            <div class="plan-action">
              <a href="https://wa.me/919849574618?text=Hi%20GA%20Digital,%20I%20am%20interested%20in%20the%20Business%20Website%20Maintenance%20Plan" style="background:#2563eb; color:#fff; text-align:center; padding:10px; border-radius:6px; display:block; text-decoration:none; font-weight:700;" target="_blank" rel="noopener noreferrer">Enquire on WhatsApp &rarr;</a>
            </div>
          </div>
        </div>
      </div>
      {plans_closing}
    </div>

    <!-- INDUSTRIES -->
    <div class="card">
      {parts[55]}
      {parts[56]}
    </div>

    <!-- FAQS -->
    <div id="faqs" style="margin-bottom: 35px;">
      <div class="card" style="margin-bottom: 15px;">
        {parts[57]}
        {faq_intro}
      </div>
      {faq_html}
    </div>

    <!-- AUDIT SECTION -->
    <div class="card" id="audit" style="background: #0f172a; color: #ffffff; padding: 40px;">
      {parts[59]}
      {parts[60]}
      
      <div style="background: rgba(255, 255, 255, 0.08); border: 1px solid rgba(255, 255, 255, 0.2); border-radius: 8px; padding: 24px; margin-top: 25px;">
        <h3 style="color: #38bdf8; margin-top: 0;">⚡ Enter Your Website for Your Free 20-Point Audit</h3>
        <p style="color: #cbd5e1; font-size: 14px; margin-bottom: 16px;">Direct engineer review with zero obligation.</p>
        <form onsubmit="event.preventDefault(); window.location.href='https://wa.me/919849574618?text=Free%20Audit%20Request:%20' + encodeURIComponent(this.audit_site.value);">
          <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 12px; margin-bottom: 14px;">
            <input type="url" name="audit_site" placeholder="https://yourwebsite.com" required style="padding: 10px; border-radius: 6px; border: 1px solid rgba(255,255,255,0.2); background: #0f172a; color: #fff;">
            <input type="text" name="audit_name" placeholder="Your Name" required style="padding: 10px; border-radius: 6px; border: 1px solid rgba(255,255,255,0.2); background: #0f172a; color: #fff;">
            <input type="tel" name="audit_phone" placeholder="WhatsApp / Phone" required style="padding: 10px; border-radius: 6px; border: 1px solid rgba(255,255,255,0.2); background: #0f172a; color: #fff;">
          </div>
          <button type="submit" style="background: #38bdf8; color: #0f172a; font-weight: 800; padding: 12px; border: none; border-radius: 6px; width: 100%; cursor: pointer;">Submit Free Audit Request &rarr;</button>
        </form>
      </div>
    </div>

    <!-- RELATED ARTICLES -->
    <div class="card">
      {parts[61]}
      {parts[62]}
      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 18px; margin-top: 15px;">
        <div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 16px;">{parts[63]}{parts[64]}</div>
        <div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 16px;">{parts[65]}{parts[66]}</div>
        <div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 16px;">{parts[67]}{parts[68]}</div>
        <div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 16px;">{parts[69]}{parts[70]}</div>
      </div>
    </div>
  </main>

  {get_site_footer()}

  <script>
    function runQuiz() {{
      let val = 0;
      document.querySelectorAll('.q-check:checked').forEach(c => val += parseInt(c.value));
      const card = document.getElementById('q-card');
      const score = document.getElementById('q-score');
      const text = document.getElementById('q-text');

      if (val === 0) {{
        card.style.borderLeftColor = '#10b981';
        score.style.color = '#10b981';
        score.innerText = 'STATUS: HEALTHY (0 Vulnerabilities)';
        text.innerText = 'Check the boxes above to calculate your vulnerability level.';
      }} else if (val <= 50) {{
        card.style.borderLeftColor = '#f59e0b';
        score.style.color = '#f59e0b';
        score.innerText = 'STATUS: MODERATE RISK (' + val + '% Vulnerability)';
        text.innerText = 'Your site has maintenance gaps that could lead to crashes or broken forms.';
      }} else {{
        card.style.borderLeftColor = '#ef4444';
        score.style.color = '#ef4444';
        score.innerText = 'STATUS: CRITICAL RISK (' + val + '% Vulnerability)';
        text.innerText = 'High probability of malware infection, database bloat, and lost customers.';
      }}
    }}

    function filterBox(cat, btn) {{
      document.querySelectorAll('.filter-btn').forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      document.querySelectorAll('.deliv-box').forEach(box => {{
        if (cat === 'all' || box.getAttribute('data-cat') === cat) {{
          box.style.display = 'block';
        }} else {{
          box.style.display = 'none';
        }}
      }});
    }}
  </script>
</body>
</html>
"""
    with open('maintenance-v3-interactive-quiz.html', 'w', encoding='utf-8') as f:
        f.write(doc)
    print("Version 3 written successfully.")


# =========================================================================
# VERSION 4: THE "FRICTIONLESS MOBILE-FIRST & DIRECT ACTION" ARCHETYPE
# Dual floating sticky action bar, quick 1-tap WhatsApp drawer, 
# expandable compact cards, rapid-conversion layout.
# =========================================================================
def build_version_4():
    print("Building Version 4: Frictionless Mobile-First & Direct Action...")
    css = """
    :root {
      --primary: #0284c7;
      --navy: #0f172a;
      --slate: #475569;
      --border: #e2e8f0;
      --wa: #25d366;
    }
    * { box-sizing: border-box; margin: 0; padding: 0; }
    body { font-family: 'Plus Jakarta Sans', sans-serif; background: #ffffff; color: var(--navy); line-height: 1.7; font-size: 16px; padding-bottom: 75px; }
    .wrap { max-width: 1140px; margin: 0 auto; padding: 0 20px; }
    h1 { font-size: 34px; font-weight: 800; line-height: 1.25; color: var(--navy); margin-bottom: 16px; }
    h2 { font-size: 23px; font-weight: 700; color: var(--navy); margin-bottom: 14px; }
    h3 { font-size: 18px; font-weight: 700; color: var(--navy); margin-bottom: 10px; }
    p { color: var(--slate); font-size: 16px; margin-bottom: 16px; }
    .card { background: #ffffff; border: 1px solid var(--border); border-radius: 12px; padding: 26px; margin-bottom: 25px; box-shadow: 0 2px 8px rgba(0,0,0,0.04); }
    
    .deliv-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(290px, 1fr)); gap: 18px; margin-top: 20px; }
    .deliv-box { background: #f8fafc; border: 1px solid var(--border); border-radius: 10px; padding: 20px; border-left: 4px solid var(--primary); }
    
    .plans-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(270px, 1fr)); gap: 20px; margin: 25px 0; }
    .plan-box { background: #ffffff; border: 1.5px solid var(--border); border-radius: 12px; display: flex; flex-direction: column; overflow: hidden; }
    .plan-header { background: #0f172a; color: #ffffff; padding: 16px; text-align: center; }
    .plan-header h3 { color: #ffffff !important; margin: 0; }
    .plan-body { padding: 20px; flex: 1; display: flex; flex-direction: column; }
    .plan-action { margin-top: auto; padding-top: 15px; }

    details { border: 1px solid var(--border); border-radius: 8px; margin-bottom: 10px; background: #ffffff; }
    summary { padding: 15px 20px; font-weight: 700; cursor: pointer; background: #f8fafc; list-style: none; display: flex; justify-content: space-between; }
    summary::-webkit-details-marker { display: none; }
    summary::after { content: '+'; color: var(--primary); font-size: 18px; }
    details[open] summary::after { content: '−'; }
    .faq-body { padding: 18px 20px; border-top: 1px solid var(--border); }

    /* Sticky Bottom Action Dock */
    .action-dock { position: fixed; bottom: 0; left: 0; width: 100%; background: rgba(255, 255, 255, 0.95); backdrop-filter: blur(12px); border-top: 1px solid #cbd5e1; padding: 10px 18px; z-index: 9999; box-shadow: 0 -4px 20px rgba(0,0,0,0.08); display: flex; gap: 12px; }
    .dock-btn { flex: 1; text-align: center; padding: 12px; font-size: 14px; font-weight: 700; border-radius: 8px; text-decoration: none !important; display: flex; align-items: center; justify-content: center; gap: 6px; }
    .dock-call { background: #f1f5f9; color: #0f172a !important; border: 1px solid #cbd5e1; }
    .dock-wa { background: #25d366; color: #ffffff !important; }
    """

    deliv_html = "".join([f"""
      <div class="deliv-box">
        <span style="font-size: 11px; font-weight: 800; color: #0284c7; margin-bottom: 6px; display: block;">TASK #{num}</span>
        {re.sub(r'<h2[^>]*>', '<h2>', parts[h])}
        {parts[b]}
      </div>
    """ for h, b, num, _, _ in deliv_data])

    faq_html = "".join([f"""
      <details>
        <summary>{q.strip()}</summary>
        <div class="faq-body">{a.strip()}</div>
      </details>
    """ for q, a in faq_pairs])

    doc = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Website Maintenance Services | GA Digital Fast Action Edition</title>
  <link rel="icon" href="https://www.gadigitalsolutions.com/images/logo.png" type="image/png">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;600;700;800&display=swap" rel="stylesheet">
  <style>{css}</style>
</head>
<body>
  {get_site_header("light")}

  <main class="wrap" style="margin-top: 35px;">
    <!-- HERO SECTION -->
    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 35px; align-items: start; margin-bottom: 35px;">
      <div>
        <div style="border-radius: 12px; overflow: hidden; margin-bottom: 20px; box-shadow: 0 4px 15px rgba(0,0,0,0.06); border: 1px solid #e2e8f0;">
          <img src="https://www.gadigitalsolutions.com/images/Website_Maintenance.jpg" width="820" height="460" alt="Website Maintenance" style="width: 100%; height: auto; display: block;">
        </div>
        {parts[0]}
        
        <div style="display: flex; flex-wrap: wrap; gap: 8px; margin: 15px 0 20px;">
          <span style="background: #f1f5f9; padding: 5px 10px; border-radius: 6px; font-size: 12px; font-weight: 700;">🛡️ 24/7 Monitoring</span>
          <span style="background: #f1f5f9; padding: 5px 10px; border-radius: 6px; font-size: 12px; font-weight: 700;">⚡ Staging Testing</span>
          <span style="background: #f1f5f9; padding: 5px 10px; border-radius: 6px; font-size: 12px; font-weight: 700;">💾 Daily Cloud Backups</span>
          <span style="background: #f1f5f9; padding: 5px 10px; border-radius: 6px; font-size: 12px; font-weight: 700;">⏱️ 30-Min SLA</span>
        </div>

        {parts[1]}
        {parts[2]}
      </div>

      <!-- DIRECT CONVERSION ACTION CARD -->
      <div style="background: #ffffff; border: 2px solid #0284c7; border-radius: 14px; padding: 26px; box-shadow: 0 10px 30px rgba(2, 132, 199, 0.15); position: sticky; top: 90px;">
        <span style="background: #e0f2fe; color: #0284c7; font-size: 11px; font-weight: 800; text-transform: uppercase; padding: 4px 10px; border-radius: 4px;">Fast Track</span>
        <h3 style="font-size: 20px; margin: 8px 0 6px;">Instant Website Health Audit</h3>
        <p style="font-size: 13px; color: #64748b; margin-bottom: 16px;">Direct submission — our technical team reviews your site within 24 hours.</p>
        
        <form onsubmit="event.preventDefault(); window.location.href='https://wa.me/919849574618?text=Fast%20Audit%20Request:%20' + encodeURIComponent(this.site.value);">
          <div style="margin-bottom: 12px;">
            <input type="url" name="site" placeholder="Website URL (e.g. yoursite.com) *" required style="width: 100%; padding: 12px; border: 1.5px solid #cbd5e1; border-radius: 6px; font-size: 14px;">
          </div>
          <div style="margin-bottom: 12px;">
            <input type="text" name="name" placeholder="Your Name *" required style="width: 100%; padding: 12px; border: 1.5px solid #cbd5e1; border-radius: 6px; font-size: 14px;">
          </div>
          <div style="margin-bottom: 14px;">
            <input type="tel" name="phone" placeholder="WhatsApp / Phone Number *" required style="width: 100%; padding: 12px; border: 1.5px solid #cbd5e1; border-radius: 6px; font-size: 14px;">
          </div>
          <button type="submit" style="background: #0284c7; color: #ffffff; font-weight: 800; padding: 13px; border: none; border-radius: 6px; width: 100%; cursor: pointer; font-size: 15px;">Claim My Free 20-Point Audit &rarr;</button>
          <a href="https://wa.me/919849574618?text=Hi%20GA%20Digital,%20I%20need%20website%20maintenance%20support" target="_blank" rel="noopener noreferrer" style="background: #25d366; color: #ffffff !important; display: block; text-align: center; padding: 11px; font-size: 13px; font-weight: 700; border-radius: 6px; margin-top: 8px; text-decoration: none;">💬 Fast Track via WhatsApp</a>
        </form>
      </div>
    </div>

    <!-- OVERVIEW -->
    <div class="card" id="overview" style="border-left: 5px solid #0284c7;">
      {parts[3]}
      {parts[4]}
    </div>

    <!-- 10 DELIVERABLES -->
    <div id="deliverables" style="margin-bottom: 35px;">
      <div class="card" style="margin-bottom: 15px;">
        {parts[5]}
        {parts[6]}
      </div>
      <div class="deliv-grid">
        {deliv_html}
      </div>
    </div>

    <!-- WHY IT MATTERS -->
    <div class="card" id="why-matters">
      {parts[27]}
      {parts[28]}
      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 15px; margin-top: 18px;">
        <div style="border: 1px solid #e2e8f0; border-radius: 8px; padding: 18px; border-top: 3px solid #10b981;">{parts[29]}{parts[30]}</div>
        <div style="border: 1px solid #e2e8f0; border-radius: 8px; padding: 18px; border-top: 3px solid #ef4444;">{parts[31]}{parts[32]}</div>
        <div style="border: 1px solid #e2e8f0; border-radius: 8px; padding: 18px; border-top: 3px solid #f59e0b;">{parts[33]}{parts[34]}</div>
        <div style="border: 1px solid #e2e8f0; border-radius: 8px; padding: 18px; border-top: 3px solid #0284c7;">{parts[35]}{parts[36]}</div>
      </div>
    </div>

    <!-- COST OF NEGLECT -->
    <div class="card" style="border-left: 5px solid #f59e0b; background: #fffbeb;" id="cost-neglect">
      {parts[37]}
      {parts[38]}
    </div>

    <!-- SCHEDULE -->
    <div class="card">
      {parts[39]}
      {parts[40]}
    </div>

    <!-- DIY VS PRO -->
    <div class="card">
      {parts[41]}
      {parts[42]}
      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 15px; margin: 18px 0;">
        <div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 18px;">{parts[43]}{parts[44]}</div>
        <div style="background: #f0fdf4; border: 1px solid #bbf7d0; border-radius: 8px; padding: 18px;">{parts[45]}{parts[46]}</div>
      </div>
      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 15px; margin: 18px 0;">
        <div style="background: #fef2f2; border: 1px solid #fecaca; border-radius: 8px; padding: 18px;">{parts[47]}{parts[48]}</div>
        <div style="background: #eff6ff; border: 1px solid #bfdbfe; border-radius: 8px; padding: 18px;">{parts[49]}{parts[50]}</div>
      </div>
      <div style="margin-top: 25px; border-top: 1px solid #e2e8f0; padding-top: 20px;">
        {parts[51]}
        {parts[52]}
      </div>
    </div>

    <!-- PLANS & PRICING -->
    <div class="card" id="plans" style="background: #f8fafc;">
      {parts[53]}
      {plans_intro}
      <div class="plans-grid">
        <div class="plan-box">
          <div class="plan-header"><h3>Essential</h3></div>
          <div class="plan-body">
            <p><strong>For brochure websites and small business sites</strong></p>
            <p>Ideal for: standard websites with stable content and moderate visitor traffic</p>
            <div class="plan-action">
              <a href="https://wa.me/919849574618?text=Hi%20GA%20Digital,%20I%20am%20interested%20in%20the%20Essential%20Website%20Maintenance%20Plan" style="background:#0f172a; color:#fff; text-align:center; padding:10px; border-radius:6px; display:block; text-decoration:none; font-weight:700;" target="_blank" rel="noopener noreferrer">Enquire on WhatsApp &rarr;</a>
            </div>
          </div>
        </div>
        <div class="plan-box" style="border: 2px solid #0284c7; box-shadow: 0 4px 15px rgba(2, 132, 199, 0.2);">
          <div class="plan-header" style="background: #0284c7;"><h3>Growth</h3></div>
          <div class="plan-body">
            <p><strong>For websites actively generating leads</strong></p>
            <p>Ideal for: businesses relying on their website for consistent lead generation</p>
            <div class="plan-action">
              <a href="https://wa.me/919849574618?text=Hi%20GA%20Digital,%20I%20am%20interested%20in%20the%20Growth%20Website%20Maintenance%20Plan" style="background:#0284c7; color:#fff; text-align:center; padding:10px; border-radius:6px; display:block; text-decoration:none; font-weight:700;" target="_blank" rel="noopener noreferrer">Enquire on WhatsApp &rarr;</a>
            </div>
          </div>
        </div>
        <div class="plan-box">
          <div class="plan-header"><h3>Business</h3></div>
          <div class="plan-body">
            <p><strong>For e-commerce, booking platforms, and high-traffic sites</strong></p>
            <p>Ideal for: e-commerce stores and businesses with significant revenue dependence on their website</p>
            <div class="plan-action">
              <a href="https://wa.me/919849574618?text=Hi%20GA%20Digital,%20I%20am%20interested%20in%20the%20Business%20Website%20Maintenance%20Plan" style="background:#0f172a; color:#fff; text-align:center; padding:10px; border-radius:6px; display:block; text-decoration:none; font-weight:700;" target="_blank" rel="noopener noreferrer">Enquire on WhatsApp &rarr;</a>
            </div>
          </div>
        </div>
      </div>
      {plans_closing}
    </div>

    <!-- INDUSTRIES -->
    <div class="card">
      {parts[55]}
      {parts[56]}
    </div>

    <!-- FAQS -->
    <div id="faqs" style="margin-bottom: 35px;">
      <div class="card" style="margin-bottom: 15px;">
        {parts[57]}
        {faq_intro}
      </div>
      {faq_html}
    </div>

    <!-- AUDIT SECTION -->
    <div class="card" id="audit" style="background: #0f172a; color: #ffffff; padding: 40px;">
      {parts[59]}
      {parts[60]}
      
      <div style="background: rgba(255, 255, 255, 0.08); border: 1px solid rgba(255, 255, 255, 0.2); border-radius: 8px; padding: 24px; margin-top: 25px;">
        <h3 style="color: #38bdf8; margin-top: 0;">⚡ Enter Your Website for Your Free 20-Point Audit</h3>
        <p style="color: #cbd5e1; font-size: 14px; margin-bottom: 16px;">Direct engineer review with zero obligation.</p>
        <form onsubmit="event.preventDefault(); window.location.href='https://wa.me/919849574618?text=Free%20Audit%20Request:%20' + encodeURIComponent(this.audit_site.value);">
          <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 12px; margin-bottom: 14px;">
            <input type="url" name="audit_site" placeholder="https://yourwebsite.com" required style="padding: 10px; border-radius: 6px; border: 1px solid rgba(255,255,255,0.2); background: #0f172a; color: #fff;">
            <input type="text" name="audit_name" placeholder="Your Name" required style="padding: 10px; border-radius: 6px; border: 1px solid rgba(255,255,255,0.2); background: #0f172a; color: #fff;">
            <input type="tel" name="audit_phone" placeholder="WhatsApp / Phone" required style="padding: 10px; border-radius: 6px; border: 1px solid rgba(255,255,255,0.2); background: #0f172a; color: #fff;">
          </div>
          <button type="submit" style="background: #0284c7; color: #fff; font-weight: 800; padding: 12px; border: none; border-radius: 6px; width: 100%; cursor: pointer;">Submit Free Audit Request &rarr;</button>
        </form>
      </div>
    </div>

    <!-- RELATED ARTICLES -->
    <div class="card">
      {parts[61]}
      {parts[62]}
      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 18px; margin-top: 15px;">
        <div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 16px;">{parts[63]}{parts[64]}</div>
        <div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 16px;">{parts[65]}{parts[66]}</div>
        <div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 16px;">{parts[67]}{parts[68]}</div>
        <div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 16px;">{parts[69]}{parts[70]}</div>
      </div>
    </div>
  </main>

  {get_site_footer()}

  <!-- STICKY BOTTOM ACTION DOCK -->
  <div class="action-dock">
    <a href="tel:9849574618" class="dock-btn dock-call">📞 Call Engineer (+91 98495 74618)</a>
    <a href="https://wa.me/919849574618?text=Hi%20GA%20Digital,%20I%20need%20website%20maintenance%20support" class="dock-btn dock-wa" target="_blank" rel="noopener noreferrer">💬 WhatsApp Fast-Track</a>
  </div>
</body>
</html>
"""
    with open('maintenance-v4-fast-action.html', 'w', encoding='utf-8') as f:
        f.write(doc)
    print("Version 4 written successfully.")

build_version_3()
build_version_4()

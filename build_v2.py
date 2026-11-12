import re
from builder_core import (
    parts, faq_intro, faq_pairs, plans_intro, plans_closing, 
    deliv_data, clean_svg_logo
)
from generate_4_versions import get_site_header, get_site_footer

# =========================================================================
# VERSION 2: THE "CYBERSECURITY & UPTIME COMMAND CENTER" (HIGH-TECH SENTINEL)
# Dark-mode terminal-inspired theme, live telemetry pulses, radar aesthetic
# =========================================================================
def build_version_2():
    print("Building Version 2: Cybersecurity & Uptime Command Center...")
    css = """
    :root {
      --bg: #070d18;
      --card-bg: #0d1527;
      --border: #1e293b;
      --border-glow: #0284c7;
      --cyan: #38bdf8;
      --emerald: #10b981;
      --text: #f1f5f9;
      --text-muted: #94a3b8;
    }
    * { box-sizing: border-box; margin: 0; padding: 0; }
    body { font-family: 'Plus Jakarta Sans', sans-serif; background: var(--bg); color: var(--text); line-height: 1.7; font-size: 16px; }
    .wrap { max-width: 1180px; margin: 0 auto; padding: 0 20px; }
    h1 { font-size: 36px; font-weight: 800; line-height: 1.25; color: #ffffff; margin-bottom: 16px; }
    h2 { font-size: 24px; font-weight: 700; color: var(--cyan); margin-bottom: 14px; }
    h3 { font-size: 19px; font-weight: 700; color: #ffffff; margin-bottom: 10px; }
    p { color: var(--text-muted); font-size: 16px; margin-bottom: 16px; }
    strong { color: #ffffff; }
    .terminal-card { background: var(--card-bg); border: 1px solid var(--border); border-radius: 14px; padding: 30px; margin-bottom: 30px; box-shadow: 0 10px 30px rgba(0,0,0,0.4); position: relative; }
    .terminal-card::before { content: ''; position: absolute; top: 0; left: 0; right: 0; height: 3px; background: linear-gradient(90deg, #0284c7, #38bdf8, #10b981); }
    .btn-cyber { background: linear-gradient(135deg, #0284c7, #0369a1); color: #ffffff !important; padding: 13px 20px; border-radius: 8px; font-weight: 700; text-decoration: none; display: block; text-align: center; border: none; cursor: pointer; width: 100%; box-shadow: 0 4px 20px rgba(2, 132, 199, 0.4); }
    .btn-cyber:hover { transform: translateY(-1px); box-shadow: 0 6px 25px rgba(2, 132, 199, 0.6); }
    .bento-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(290px, 1fr)); gap: 20px; margin-top: 20px; }
    .bento-box { background: #0b1322; border: 1px solid #1e293b; border-radius: 10px; padding: 22px; transition: all 0.2s; }
    .bento-box:hover { border-color: var(--cyan); transform: translateY(-3px); }
    .tag-mono { font-family: monospace; font-size: 11px; color: var(--cyan); background: rgba(56, 189, 248, 0.1); padding: 3px 8px; border-radius: 4px; display: inline-block; margin-bottom: 10px; }
    .plans-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(270px, 1fr)); gap: 20px; margin: 25px 0; }
    .plan-box { background: #0b1322; border: 1.5px solid #1e293b; border-radius: 12px; display: flex; flex-direction: column; overflow: hidden; }
    .plan-header { background: #111e38; color: #ffffff; padding: 18px; text-align: center; border-bottom: 1px solid #1e293b; }
    .plan-body { padding: 22px; flex: 1; display: flex; flex-direction: column; }
    .plan-action { margin-top: auto; padding-top: 15px; }
    details { border: 1px solid #1e293b; border-radius: 8px; margin-bottom: 10px; background: #0b1322; }
    summary { padding: 15px 20px; font-weight: 700; cursor: pointer; background: #0f1a30; list-style: none; display: flex; justify-content: space-between; color: #ffffff; }
    summary::-webkit-details-marker { display: none; }
    summary::after { content: '+'; color: var(--cyan); font-size: 18px; }
    details[open] summary::after { content: '−'; }
    .faq-body { padding: 18px 20px; border-top: 1px solid #1e293b; }
    """

    deliv_html = "".join([f"""
      <div class="bento-box">
        <span class="tag-mono">// TASK_{num}</span>
        {re.sub(r'<h2[^>]*>', '<h2 style="color:#ffffff;">', parts[h])}
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
  <title>Website Maintenance Services | GA Sentinel Cyber Center</title>
  <link rel="icon" href="https://www.gadigitalsolutions.com/images/logo.png" type="image/png">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;600;700;800&display=swap" rel="stylesheet">
  <style>{css}</style>
</head>
<body>
  {get_site_header("dark")}

  <main class="wrap" style="margin-top: 35px;">
    <!-- HERO SECTION -->
    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 35px; align-items: start; margin-bottom: 40px;">
      <div>
        <div style="border-radius: 12px; overflow: hidden; margin-bottom: 20px; box-shadow: 0 4px 20px rgba(0,0,0,0.5); border: 1px solid #1e293b;">
          <img src="https://www.gadigitalsolutions.com/images/Website_Maintenance.jpg" width="820" height="460" alt="Website Maintenance" style="width: 100%; height: auto; display: block;">
        </div>
        {parts[0]}
        
        <div style="display: flex; flex-wrap: wrap; gap: 10px; margin: 18px 0 25px;">
          <span style="background: rgba(56, 189, 248, 0.1); border: 1px solid #0284c7; color: #38bdf8; padding: 6px 12px; border-radius: 6px; font-size: 12px; font-weight: 700;">● 24/7 ACTIVE RADAR</span>
          <span style="background: rgba(16, 185, 129, 0.1); border: 1px solid #10b981; color: #10b981; padding: 6px 12px; border-radius: 6px; font-size: 12px; font-weight: 700;">✓ STAGING ISOLATION</span>
          <span style="background: rgba(56, 189, 248, 0.1); border: 1px solid #0284c7; color: #38bdf8; padding: 6px 12px; border-radius: 6px; font-size: 12px; font-weight: 700;">☁ DAILY CLOUD SNAPSHOTS</span>
          <span style="background: rgba(245, 158, 11, 0.1); border: 1px solid #f59e0b; color: #f59e0b; padding: 6px 12px; border-radius: 6px; font-size: 12px; font-weight: 700;">⚡ 30-MIN RAPID SLA</span>
        </div>

        {parts[1]}
        {parts[2]}
      </div>

      <!-- CYBER COMMAND FORM CARD (INTEGRATING EMBLEM) -->
      <div style="background: #0d1527; border: 1px solid #0284c7; border-radius: 14px; padding: 28px; box-shadow: 0 10px 40px rgba(2, 132, 199, 0.25); position: sticky; top: 90px;">
        <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 12px;">
          <div style="width: 36px; height: 36px; background: #ffffff; border-radius: 8px; padding: 3px; display: flex; align-items: center; justify-content: center;">
            {clean_svg_logo}
          </div>
          <div>
            <h3 style="font-size: 17px; margin: 0; color: #ffffff;">GA Sentinel Guardian</h3>
            <span style="font-size: 11px; font-weight: 700; color: #10b981; text-transform: uppercase;">Active Site Protection</span>
          </div>
        </div>

        <p style="font-size: 13px; color: #94a3b8; margin-bottom: 16px;">Run an instant 20-point diagnostic to detect hidden malware, plugin CVEs, and latency:</p>
        
        <form onsubmit="event.preventDefault(); window.location.href='https://wa.me/919849574618?text=Sentinel%20Audit%20Request:%20' + encodeURIComponent(this.site.value);">
          <div style="margin-bottom: 12px;">
            <label style="display:block; font-size: 11px; font-weight: 700; color: #94a3b8; margin-bottom: 4px; text-transform: uppercase;">WEBSITE URL *</label>
            <input type="url" name="site" placeholder="https://yourcompany.com" required style="width: 100%; padding: 11px; border: 1px solid #1e293b; border-radius: 6px; font-size: 14px; background: #070d18; color: #fff;">
          </div>
          <div style="margin-bottom: 12px;">
            <label style="display:block; font-size: 11px; font-weight: 700; color: #94a3b8; margin-bottom: 4px; text-transform: uppercase;">YOUR NAME *</label>
            <input type="text" name="name" placeholder="John Doe" required style="width: 100%; padding: 11px; border: 1px solid #1e293b; border-radius: 6px; font-size: 14px; background: #070d18; color: #fff;">
          </div>
          <div style="margin-bottom: 15px;">
            <label style="display:block; font-size: 11px; font-weight: 700; color: #94a3b8; margin-bottom: 4px; text-transform: uppercase;">WHATSAPP / PHONE *</label>
            <input type="tel" name="phone" placeholder="+91 98765 43210" required style="width: 100%; padding: 11px; border: 1px solid #1e293b; border-radius: 6px; font-size: 14px; background: #070d18; color: #fff;">
          </div>
          <button type="submit" class="btn-cyber">Run 20-Point Health Diagnostic &rarr;</button>
          <a href="https://wa.me/919849574618?text=EMERGENCY:%20My%20site%20is%20down%20or%20hacked!" target="_blank" rel="noopener noreferrer" style="background: #ef4444; color: #ffffff !important; display: block; text-align: center; padding: 10px; font-size: 13px; font-weight: 700; border-radius: 6px; margin-top: 8px; text-decoration: none;">🚨 24/7 Emergency Incident Hotline</a>
        </form>
      </div>
    </div>

    <!-- OVERVIEW -->
    <div class="terminal-card" id="overview">
      {parts[3]}
      {parts[4]}
    </div>

    <!-- 10 DELIVERABLES -->
    <div id="deliverables" style="margin-bottom: 35px;">
      <div class="terminal-card" style="margin-bottom: 20px;">
        {parts[5]}
        {parts[6]}
      </div>
      <div class="bento-grid">
        {deliv_html}
      </div>
    </div>

    <!-- WHY IT MATTERS -->
    <div class="terminal-card" id="why-matters">
      {parts[27]}
      {parts[28]}
      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 15px; margin-top: 18px;">
        <div style="background: #0b1322; border: 1px solid #1e293b; border-radius: 8px; padding: 18px; border-top: 3px solid #10b981;">{parts[29]}{parts[30]}</div>
        <div style="background: #0b1322; border: 1px solid #1e293b; border-radius: 8px; padding: 18px; border-top: 3px solid #ef4444;">{parts[31]}{parts[32]}</div>
        <div style="background: #0b1322; border: 1px solid #1e293b; border-radius: 8px; padding: 18px; border-top: 3px solid #f59e0b;">{parts[33]}{parts[34]}</div>
        <div style="background: #0b1322; border: 1px solid #1e293b; border-radius: 8px; padding: 18px; border-top: 3px solid #38bdf8;">{parts[35]}{parts[36]}</div>
      </div>
    </div>

    <!-- COST OF NEGLECT -->
    <div class="terminal-card" style="border-left: 5px solid #f59e0b;" id="cost-neglect">
      {parts[37]}
      {parts[38]}
    </div>

    <!-- SCHEDULE -->
    <div class="terminal-card">
      {parts[39]}
      {parts[40]}
    </div>

    <!-- DIY VS PRO -->
    <div class="terminal-card">
      {parts[41]}
      {parts[42]}
      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 15px; margin: 18px 0;">
        <div style="background: #0b1322; border: 1px solid #1e293b; border-radius: 8px; padding: 18px;">{parts[43]}{parts[44]}</div>
        <div style="background: #08201b; border: 1px solid #064e3b; border-radius: 8px; padding: 18px;">{parts[45]}{parts[46]}</div>
      </div>
      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 15px; margin: 18px 0;">
        <div style="background: #200808; border: 1px solid #4e0606; border-radius: 8px; padding: 18px;">{parts[47]}{parts[48]}</div>
        <div style="background: #081520; border: 1px solid #062b4e; border-radius: 8px; padding: 18px;">{parts[49]}{parts[50]}</div>
      </div>
      <div style="margin-top: 25px; border-top: 1px solid #1e293b; padding-top: 20px;">
        {parts[51]}
        {parts[52]}
      </div>
    </div>

    <!-- PLANS & PRICING -->
    <div class="terminal-card" id="plans">
      {parts[53]}
      {plans_intro}
      <div class="plans-grid">
        <div class="plan-box">
          <div class="plan-header"><h3>Essential</h3></div>
          <div class="plan-body">
            <p><strong>For brochure websites and small business sites</strong></p>
            <p>Ideal for: standard websites with stable content and moderate visitor traffic</p>
            <div class="plan-action">
              <a href="https://wa.me/919849574618?text=Hi%20GA%20Digital,%20I%20am%20interested%20in%20the%20Essential%20Website%20Maintenance%20Plan" class="btn-cyber" target="_blank" rel="noopener noreferrer">Enquire on WhatsApp &rarr;</a>
            </div>
          </div>
        </div>
        <div class="plan-box" style="border: 2px solid #0284c7; box-shadow: 0 0 25px rgba(2, 132, 199, 0.3);">
          <div class="plan-header" style="background: #0284c7;"><h3>Growth</h3></div>
          <div class="plan-body">
            <p><strong>For websites actively generating leads</strong></p>
            <p>Ideal for: businesses relying on their website for consistent lead generation</p>
            <div class="plan-action">
              <a href="https://wa.me/919849574618?text=Hi%20GA%20Digital,%20I%20am%20interested%20in%20the%20Growth%20Website%20Maintenance%20Plan" class="btn-cyber" style="background: #38bdf8; color: #0f172a !important;" target="_blank" rel="noopener noreferrer">Enquire on WhatsApp &rarr;</a>
            </div>
          </div>
        </div>
        <div class="plan-box">
          <div class="plan-header"><h3>Business</h3></div>
          <div class="plan-body">
            <p><strong>For e-commerce, booking platforms, and high-traffic sites</strong></p>
            <p>Ideal for: e-commerce stores and businesses with significant revenue dependence on their website</p>
            <div class="plan-action">
              <a href="https://wa.me/919849574618?text=Hi%20GA%20Digital,%20I%20am%20interested%20in%20the%20Business%20Website%20Maintenance%20Plan" class="btn-cyber" target="_blank" rel="noopener noreferrer">Enquire on WhatsApp &rarr;</a>
            </div>
          </div>
        </div>
      </div>
      {plans_closing}
    </div>

    <!-- INDUSTRIES -->
    <div class="terminal-card">
      {parts[55]}
      {parts[56]}
    </div>

    <!-- FAQS -->
    <div id="faqs" style="margin-bottom: 35px;">
      <div class="terminal-card" style="margin-bottom: 15px;">
        {parts[57]}
        {faq_intro}
      </div>
      {faq_html}
    </div>

    <!-- AUDIT SECTION -->
    <div class="terminal-card" id="audit" style="background: #080e1a; border: 2px solid #38bdf8; padding: 40px;">
      {parts[59]}
      {parts[60]}
      
      <div style="background: rgba(255, 255, 255, 0.05); border: 1px solid rgba(255, 255, 255, 0.15); border-radius: 8px; padding: 24px; margin-top: 25px;">
        <h3 style="color: #38bdf8; margin-top: 0;">⚡ Enter Your Website for Your Free 20-Point Audit</h3>
        <p style="color: #cbd5e1; font-size: 14px; margin-bottom: 16px;">Direct engineer review with zero obligation.</p>
        <form onsubmit="event.preventDefault(); window.location.href='https://wa.me/919849574618?text=Free%20Audit%20Request:%20' + encodeURIComponent(this.audit_site.value);">
          <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 12px; margin-bottom: 14px;">
            <input type="url" name="audit_site" placeholder="https://yourwebsite.com" required style="padding: 10px; border-radius: 6px; border: 1px solid #1e293b; background: #070d18; color: #fff;">
            <input type="text" name="audit_name" placeholder="Your Name" required style="padding: 10px; border-radius: 6px; border: 1px solid #1e293b; background: #070d18; color: #fff;">
            <input type="tel" name="audit_phone" placeholder="WhatsApp / Phone" required style="padding: 10px; border-radius: 6px; border: 1px solid #1e293b; background: #070d18; color: #fff;">
          </div>
          <button type="submit" class="btn-cyber" style="background: #38bdf8; color: #070d18 !important;">Submit Free Audit Request &rarr;</button>
        </form>
      </div>
    </div>

    <!-- RELATED ARTICLES -->
    <div class="terminal-card">
      {parts[61]}
      {parts[62]}
      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 18px; margin-top: 15px;">
        <div style="background: #0b1322; border: 1px solid #1e293b; border-radius: 8px; padding: 16px;">{parts[63]}{parts[64]}</div>
        <div style="background: #0b1322; border: 1px solid #1e293b; border-radius: 8px; padding: 16px;">{parts[65]}{parts[66]}</div>
        <div style="background: #0b1322; border: 1px solid #1e293b; border-radius: 8px; padding: 16px;">{parts[67]}{parts[68]}</div>
        <div style="background: #0b1322; border: 1px solid #1e293b; border-radius: 8px; padding: 16px;">{parts[69]}{parts[70]}</div>
      </div>
    </div>
  </main>

  {get_site_footer()}
</body>
</html>
"""
    with open('maintenance-v2-cyber-sentinel.html', 'w', encoding='utf-8') as f:
        f.write(doc)
    print("Version 2 written successfully.")

build_version_2()

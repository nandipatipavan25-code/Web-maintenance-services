import re
from builder_core import (
    parts, faq_intro, faq_pairs, plans_intro, plans_closing, 
    deliv_data, clean_svg_logo, raw_main
)

# Shared header snippet generator
def get_site_header(theme="light"):
    bg = "#ffffff" if theme == "light" else "#0a1120"
    border = "#e2e8f0" if theme == "light" else "#1e293b"
    tel_color = "#1e293b" if theme == "light" else "#e2e8f0"
    
    return f"""
    <header style="background: {bg}; border-bottom: 1px solid {border}; padding: 14px 0; position: sticky; top: 0; z-index: 100; backdrop-filter: blur(12px);">
      <div style="max-width: 1200px; margin: 0 auto; padding: 0 24px; display: flex; align-items: center; justify-content: space-between; gap: 20px;">
        <a href="https://www.gadigitalsolutions.com/">
          <img src="https://www.gadigitalsolutions.com/images/GADS%20LOGO-01.svg" alt="GA Digital Solutions Logo" height="46" style="display: block;">
        </a>
        <div style="display: flex; align-items: center; gap: 18px;">
          <a href="tel:9849574618" style="font-size: 14px; font-weight: 700; color: {tel_color}; text-decoration: none;">📞 +91 98495 74618</a>
          <a href="https://wa.me/919849574618?text=Hi%20GA%20Digital,%20I%20need%20website%20maintenance%20support" target="_blank" rel="noopener noreferrer" style="background: #25d366; color: #ffffff; font-size: 14px; font-weight: 700; padding: 8px 16px; border-radius: 6px; text-decoration: none; display: inline-flex; align-items: center; gap: 6px;">
            💬 WhatsApp
          </a>
        </div>
      </div>
    </header>
    """

def get_site_footer():
    return """
    <footer style="background: #0a1120; color: #94a3b8; padding: 40px 0; margin-top: 60px; border-top: 1px solid #1e293b; font-size: 14px;">
      <div style="max-width: 1200px; margin: 0 auto; padding: 0 24px; display: flex; flex-wrap: wrap; justify-content: space-between; align-items: center; gap: 20px;">
        <div style="display: flex; align-items: center; gap: 12px;">
          <img src="https://www.gadigitalsolutions.com/images/logo.png" alt="GA Logo" height="32" style="border-radius: 4px;">
          <div>
            <p style="color: #ffffff; font-weight: 700; margin: 0;">GA Digital Solutions</p>
            <p style="color: #64748b; font-size: 13px; margin: 0;">A Business Unit of Gunnam Associates | Hyderabad, India</p>
          </div>
        </div>
        <div>
          <p style="color: #64748b; font-size: 13px; margin: 0;">&copy; 2026 GA Digital Solutions. All rights reserved.</p>
        </div>
      </div>
    </footer>
    """

# =========================================================================
# VERSION 1: THE "EXECUTIVE B2B / HIGH-TRUST AGENCY" ARCHETYPE
# (Corporate White & Royal Navy, Credibility Metrics, Structured Navigation)
# =========================================================================
def build_version_1():
    print("Building Version 1: Executive B2B / High-Trust Agency...")
    css = """
    :root {
      --primary: #126db2;
      --primary-dark: #0d4e80;
      --navy: #0f172a;
      --slate: #475569;
      --border: #e2e8f0;
      --bg: #ffffff;
    }
    * { box-sizing: border-box; margin: 0; padding: 0; }
    body { font-family: 'Plus Jakarta Sans', sans-serif; color: var(--navy); background: #f8fafc; line-height: 1.7; font-size: 16px; }
    .wrap { max-width: 1180px; margin: 0 auto; padding: 0 20px; }
    h1 { font-size: 36px; font-weight: 800; line-height: 1.25; color: var(--navy); margin-bottom: 16px; }
    h2 { font-size: 24px; font-weight: 700; color: var(--navy); margin-bottom: 14px; }
    h3 { font-size: 19px; font-weight: 700; color: var(--navy); margin-bottom: 10px; }
    p { color: var(--slate); font-size: 16px; margin-bottom: 16px; }
    .card { background: #ffffff; border: 1px solid var(--border); border-radius: 12px; padding: 30px; margin-bottom: 30px; box-shadow: 0 2px 8px rgba(0,0,0,0.04); }
    .card-accent { border-left: 5px solid var(--primary); background: linear-gradient(180deg, #f0f9ff 0%, #ffffff 100%); }
    .card-warning { border-left: 5px solid #f59e0b; background: #fffbeb; }
    .btn-exec { background: var(--primary); color: #ffffff !important; padding: 12px 20px; border-radius: 6px; font-weight: 700; text-decoration: none; display: inline-block; text-align: center; border: none; cursor: pointer; width: 100%; }
    .btn-exec:hover { background: var(--primary-dark); }
    .deliv-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(290px, 1fr)); gap: 20px; margin-top: 20px; }
    .deliv-box { background: #ffffff; border: 1px solid var(--border); border-radius: 10px; padding: 22px; border-top: 4px solid var(--primary); }
    .deliv-num { font-size: 11px; font-weight: 800; color: var(--primary); background: #e0f2fe; padding: 3px 8px; border-radius: 4px; display: inline-block; margin-bottom: 8px; }
    .plans-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(270px, 1fr)); gap: 20px; margin: 25px 0; }
    .plan-box { background: #ffffff; border: 1.5px solid var(--border); border-radius: 12px; display: flex; flex-direction: column; overflow: hidden; }
    .plan-header { background: #1e529b; color: #ffffff; padding: 16px; text-align: center; }
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
      <div class="deliv-box">
        <span class="deliv-num">TASK #{num}</span>
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
  <title>Website Maintenance Services | GA Digital Solutions (Executive Trust Edition)</title>
  <link rel="icon" href="https://www.gadigitalsolutions.com/images/logo.png" type="image/png">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;600;700;800&display=swap" rel="stylesheet">
  <style>{css}</style>
</head>
<body>
  {get_site_header("light")}
  
  <div style="background: #ffffff; border-bottom: 1px solid #e2e8f0; padding: 10px 0; position: sticky; top: 75px; z-index: 90;">
    <div class="wrap" style="display: flex; gap: 10px; overflow-x: auto; white-space: nowrap;">
      <a href="#overview" style="font-size: 13px; font-weight: 600; padding: 6px 14px; background: #f1f5f9; border-radius: 20px; text-decoration: none; color: #475569;">Overview</a>
      <a href="#deliverables" style="font-size: 13px; font-weight: 600; padding: 6px 14px; background: #f1f5f9; border-radius: 20px; text-decoration: none; color: #475569;">10 Tasks Included</a>
      <a href="#why-matters" style="font-size: 13px; font-weight: 600; padding: 6px 14px; background: #f1f5f9; border-radius: 20px; text-decoration: none; color: #475569;">Why It Matters</a>
      <a href="#plans" style="font-size: 13px; font-weight: 700; padding: 6px 14px; background: #e0f2fe; border-radius: 20px; text-decoration: none; color: #0284c7;">Maintenance Plans</a>
      <a href="#faqs" style="font-size: 13px; font-weight: 600; padding: 6px 14px; background: #f1f5f9; border-radius: 20px; text-decoration: none; color: #475569;">FAQs</a>
      <a href="#audit" style="font-size: 13px; font-weight: 700; padding: 6px 14px; background: #126db2; color: #ffffff; border-radius: 20px; text-decoration: none;">Claim 20-Point Audit</a>
    </div>
  </div>

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

      <!-- EXECUTIVE LEAD CAPTURE CARD -->
      <div style="background: #ffffff; border: 2px solid #bae6fd; border-radius: 12px; padding: 28px; box-shadow: 0 10px 30px rgba(0,0,0,0.08); position: sticky; top: 130px;">
        <span style="background: #e0f2fe; color: #0284c7; font-size: 11px; font-weight: 800; text-transform: uppercase; padding: 4px 10px; border-radius: 4px;">Verified B2B Service</span>
        <h3 style="font-size: 20px; margin: 10px 0 6px;">Request Free 20-Point Site Audit</h3>
        <p style="font-size: 13px; color: #64748b; margin-bottom: 16px;">Comprehensive inspection of security vulnerabilities, plugin health &amp; mobile speed.</p>
        
        <form onsubmit="event.preventDefault(); window.location.href='https://wa.me/919849574618?text=Hi%20GA%20Digital,%20I%20would%20like%20a%20Free%20Audit%20for:%20' + encodeURIComponent(this.site.value);">
          <div style="margin-bottom: 12px;">
            <label style="display:block; font-size: 12px; font-weight: 700; color: #334155; margin-bottom: 4px;">WEBSITE URL *</label>
            <input type="url" name="site" placeholder="https://yourcompany.com" required style="width: 100%; padding: 10px; border: 1px solid #cbd5e1; border-radius: 6px; font-size: 14px;">
          </div>
          <div style="margin-bottom: 12px;">
            <label style="display:block; font-size: 12px; font-weight: 700; color: #334155; margin-bottom: 4px;">YOUR NAME *</label>
            <input type="text" name="name" placeholder="John Doe" required style="width: 100%; padding: 10px; border: 1px solid #cbd5e1; border-radius: 6px; font-size: 14px;">
          </div>
          <div style="margin-bottom: 15px;">
            <label style="display:block; font-size: 12px; font-weight: 700; color: #334155; margin-bottom: 4px;">WHATSAPP / PHONE *</label>
            <input type="tel" name="phone" placeholder="+91 98765 43210" required style="width: 100%; padding: 10px; border: 1px solid #cbd5e1; border-radius: 6px; font-size: 14px;">
          </div>
          <button type="submit" class="btn-exec">Get Free Health Audit &rarr;</button>
          <a href="https://wa.me/919849574618?text=Hi%20GA%20Digital,%20I%20need%20website%20maintenance%20support" target="_blank" rel="noopener noreferrer" style="background: #25d366; color: #ffffff !important; display: block; text-align: center; padding: 10px; font-size: 13px; font-weight: 700; border-radius: 6px; margin-top: 8px; text-decoration: none;">💬 WhatsApp Support</a>
        </form>
      </div>
    </div>

    <!-- OVERVIEW -->
    <div class="card card-accent" id="overview">
      {parts[3]}
      {parts[4]}
    </div>

    <!-- 10 DELIVERABLES -->
    <div id="deliverables" style="margin-bottom: 35px;">
      <div class="card" style="margin-bottom: 20px;">
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
        <div style="border: 1px solid #e2e8f0; border-radius: 8px; padding: 18px; border-top: 3px solid #126db2;">{parts[35]}{parts[36]}</div>
      </div>
    </div>

    <!-- COST OF NEGLECT -->
    <div class="card card-warning" id="cost-neglect">
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
              <a href="https://wa.me/919849574618?text=Hi%20GA%20Digital,%20I%20am%20interested%20in%20the%20Essential%20Website%20Maintenance%20Plan" class="btn-exec" target="_blank" rel="noopener noreferrer">Enquire on WhatsApp &rarr;</a>
            </div>
          </div>
        </div>
        <div class="plan-box" style="border: 2px solid #126db2;">
          <div class="plan-header" style="background: #126db2;"><h3>Growth</h3></div>
          <div class="plan-body">
            <p><strong>For websites actively generating leads</strong></p>
            <p>Ideal for: businesses relying on their website for consistent lead generation</p>
            <div class="plan-action">
              <a href="https://wa.me/919849574618?text=Hi%20GA%20Digital,%20I%20am%20interested%20in%20the%20Growth%20Website%20Maintenance%20Plan" class="btn-exec" target="_blank" rel="noopener noreferrer">Enquire on WhatsApp &rarr;</a>
            </div>
          </div>
        </div>
        <div class="plan-box">
          <div class="plan-header"><h3>Business</h3></div>
          <div class="plan-body">
            <p><strong>For e-commerce, booking platforms, and high-traffic sites</strong></p>
            <p>Ideal for: e-commerce stores and businesses with significant revenue dependence on their website</p>
            <div class="plan-action">
              <a href="https://wa.me/919849574618?text=Hi%20GA%20Digital,%20I%20am%20interested%20in%20the%20Business%20Website%20Maintenance%20Plan" class="btn-exec" target="_blank" rel="noopener noreferrer">Enquire on WhatsApp &rarr;</a>
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
    <div class="card" id="audit" style="background: linear-gradient(135deg, #0f172a, #1e293b); color: #ffffff; padding: 40px;">
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
          <button type="submit" class="btn-exec" style="background: #0284c7;">Submit Free Audit Request &rarr;</button>
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
</body>
</html>
"""
    with open('maintenance-v1-executive-trust.html', 'w', encoding='utf-8') as f:
        f.write(doc)
    print("Version 1 written successfully.")

build_version_1()

import re

css_refinements = """
    /* =========================================================
       FINE-TUNED SPEED ODOMETER STYLES (BALANCED 2X2 & HIGH CONTRAST)
       ========================================================= */
    .speed-odometer-box strong {
      color: #38bdf8 !important;
      font-weight: 800;
    }
    .odo-metrics-grid {
      display: grid !important;
      grid-template-columns: repeat(2, 1fr) !important;
      gap: 14px !important;
    }
    @media (max-width: 600px) {
      .odo-metrics-grid {
        grid-template-columns: 1fr !important;
      }
    }
    .odo-metric-card {
      background: rgba(255, 255, 255, 0.04) !important;
      border: 1px solid rgba(255, 255, 255, 0.1) !important;
      border-radius: 10px !important;
      padding: 14px 16px !important;
      display: flex;
      flex-direction: column;
      gap: 4px;
      transition: all 0.2s ease;
    }
    .odo-metric-card:hover {
      background: rgba(255, 255, 255, 0.065) !important;
      border-color: rgba(56, 189, 248, 0.3) !important;
    }
    .odo-metric-label {
      font-size: 10.5px !important;
      font-weight: 700 !important;
      text-transform: uppercase !important;
      letter-spacing: 0.06em !important;
      color: #94a3b8 !important;
    }
    .odo-metric-val {
      font-size: 22px !important;
      font-weight: 800 !important;
      color: #ffffff !important;
      line-height: 1.15 !important;
    }
    .odo-alert-box {
      background: rgba(14, 165, 233, 0.08) !important;
      border: 1px solid rgba(56, 189, 248, 0.3) !important;
      border-radius: 10px !important;
      padding: 14px 18px !important;
      margin-top: 16px !important;
      display: flex !important;
      align-items: center !important;
      justify-content: space-between !important;
      flex-wrap: wrap !important;
      gap: 14px !important;
    }
    .odo-alert-text {
      color: #f1f5f9 !important;
      font-size: 13.5px !important;
      line-height: 1.5 !important;
      display: flex !important;
      align-items: center !important;
      gap: 10px !important;
      flex: 1 !important;
      min-width: 260px !important;
    }
    .odo-alert-text strong {
      color: #38bdf8 !important;
    }
    .odo-score-num {
      font-size: 52px !important;
      font-weight: 900 !important;
      line-height: 1 !important;
      letter-spacing: -0.03em !important;
      color: #10b981;
      text-shadow: 0 0 24px rgba(16, 185, 129, 0.35) !important;
      margin-bottom: 2px !important;
    }
    .speed-toggle-btn {
      padding: 8px 18px !important;
    }
    .speed-toggle-btn.active {
      box-shadow: 0 2px 10px rgba(2, 132, 199, 0.45) !important;
    }
"""

refined_svg = """<svg class="gauge-svg" viewBox="0 0 270 160">
                  <defs>
                    <linearGradient id="gaugeArcGrad" x1="0%" y1="0%" x2="100%" y2="0%">
                      <stop offset="0%" stop-color="#ef4444" />
                      <stop offset="35%" stop-color="#f97316" />
                      <stop offset="65%" stop-color="#eab308" />
                      <stop offset="85%" stop-color="#10b981" />
                      <stop offset="100%" stop-color="#06b6d4" />
                    </linearGradient>
                    <filter id="needleGlow" x="-20%" y="-20%" width="140%" height="140%">
                      <feGaussianBlur stdDeviation="3" result="glow" />
                      <feComposite in="SourceGraphic" in2="glow" operator="over" />
                    </filter>
                  </defs>

                  <!-- Dial Background Track -->
                  <path d="M 30 135 A 105 105 0 0 1 240 135" fill="none" stroke="#1e293b" stroke-width="18" stroke-linecap="round" />

                  <!-- Color Performance Speed Arc -->
                  <path d="M 30 135 A 105 105 0 0 1 240 135" fill="none" stroke="url(#gaugeArcGrad)" stroke-width="14" stroke-linecap="round" stroke-dasharray="330" stroke-dashoffset="0" opacity="0.9" />

                  <!-- Tick Marks & Crisp Numerical Labels -->
                  <line x1="30" y1="135" x2="42" y2="135" stroke="#ffffff" stroke-width="2.5" opacity="0.8" />
                  <text x="26" y="154" fill="#ef4444" font-size="11" font-weight="800" text-anchor="middle">0</text>

                  <line x1="56" y1="68" x2="65" y2="76" stroke="#ffffff" stroke-width="1.8" opacity="0.6" />
                  <text x="58" y="58" fill="#f97316" font-size="10" font-weight="700" text-anchor="middle">25</text>

                  <line x1="135" y1="30" x2="135" y2="42" stroke="#ffffff" stroke-width="2.5" opacity="0.8" />
                  <text x="135" y="18" fill="#fbbf24" font-size="11" font-weight="800" text-anchor="middle">50</text>

                  <line x1="214" y1="68" x2="205" y2="76" stroke="#ffffff" stroke-width="1.8" opacity="0.6" />
                  <text x="212" y="58" fill="#38bdf8" font-size="10" font-weight="700" text-anchor="middle">75</text>

                  <line x1="240" y1="135" x2="228" y2="135" stroke="#ffffff" stroke-width="2.5" opacity="0.8" />
                  <text x="244" y="154" fill="#10b981" font-size="11" font-weight="800" text-anchor="middle">100</text>

                  <!-- Needle Pivot Center -->
                  <circle cx="135" cy="135" r="16" fill="#0f172a" stroke="#38bdf8" stroke-width="2.5" />
                  <circle cx="135" cy="135" r="7" fill="#38bdf8" />
                  <circle cx="135" cy="135" r="3" fill="#ffffff" />

                  <!-- Animated Needle Group (Starts at 0 / -90deg) -->
                  <g id="odoNeedleGroup" class="gauge-needle-poly" style="transform: rotate(-90deg); transition: transform 1.3s cubic-bezier(0.16, 1, 0.3, 1);">
                    <polygon points="132,135 138,135 136,32 134,32" fill="#38bdf8" filter="url(#needleGlow)" />
                    <circle cx="135" cy="32" r="4" fill="#ffffff" filter="url(#needleGlow)" />
                  </g>
                </svg>"""

old_hint = """<div style="font-size: 12px; color: #94a3b8; margin-top: 8px; display: flex; align-items: center; gap: 6px;">
            <span>ℹ️</span> <span>Enter your website URL and click <strong>Enter</strong> to launch the interactive speedometer.</span>
          </div>"""

new_hint = """<div style="font-size: 12.5px; color: #cbd5e1; margin-top: 10px; display: flex; align-items: center; gap: 7px;">
            <span>ℹ️</span> <span>Enter your website URL and click <strong style="color: #38bdf8 !important; font-weight: 800;">⚡ Enter</strong> to launch the interactive speedometer.</span>
          </div>"""

for fname in ['website-maintenance.html', 'website-maintenance-sidebar-layout.html']:
    with open(fname, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Update Hint text
    if old_hint in content:
        content = content.replace(old_hint, new_hint, 1)

    # 2. Update SVG
    old_svg_pattern = r'<svg class="gauge-svg".*?</svg>'
    if re.search(old_svg_pattern, content, re.DOTALL):
        content = re.sub(old_svg_pattern, refined_svg, content, count=1, flags=re.DOTALL)

    # 3. Append CSS refinements
    if 'FINE-TUNED SPEED ODOMETER STYLES' not in content:
        content = content.replace('</style>', css_refinements + '\n</style>', 1)

    # 4. Update JS alert text for crisp colors
    old_js_alert = """'<span>🚀</span> <span><strong>Maintained by GA Digital:</strong> Automated Redis caching, WebP image compression, and database indexing keep it running at top speed.</span>'"""
    new_js_alert = """'<span>🚀</span> <span><strong style="color: #34d399 !important;">Maintained by GA Digital:</strong> Automated Redis caching, WebP image compression, and database indexing keep it running at top speed.</span>'"""
    content = content.replace(old_js_alert, new_js_alert)

    old_js_alert_slow = """'<span>⚠️</span> <span><strong>High Risk:</strong> Uncompressed images, bloated WordPress plugins & lack of caching are hurting conversions.</span>'"""
    new_js_alert_slow = """'<span>⚠️</span> <span><strong style="color: #f87171 !important;">High Risk:</strong> Uncompressed images, bloated WordPress plugins & lack of caching are hurting conversions.</span>'"""
    content = content.replace(old_js_alert_slow, new_js_alert_slow)

    with open(fname, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"Updated {fname} successfully!")

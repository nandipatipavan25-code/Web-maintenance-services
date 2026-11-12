import re

new_marquee_css = """
    /* =========================================================
       AUTO HORIZONTAL SCROLLING CLIENT LOGOS MARQUEE (EQUAL SPACING)
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
      padding: 18px 0;
      background: #ffffff;
      border-top: 1px solid #f1f5f9;
      border-bottom: 1px solid #f1f5f9;
      mask-image: linear-gradient(to right, transparent 0%, black 6%, black 94%, transparent 100%);
      -webkit-mask-image: linear-gradient(to right, transparent 0%, black 6%, black 94%, transparent 100%);
    }
    .clients-marquee-track {
      display: flex;
      align-items: center;
      width: max-content;
      animation: logoScrollHoriz 32s linear infinite;
      will-change: transform;
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
    /* Fixed uniform slot dimensions for 100% equal visual spacing */
    .client-logo-item {
      width: 170px !important;
      min-width: 170px !important;
      max-width: 170px !important;
      height: 64px !important;
      display: inline-flex !important;
      align-items: center !important;
      justify-content: center !important;
      flex-shrink: 0 !important;
      margin: 0 28px !important;
      padding: 0 !important;
      box-sizing: border-box !important;
      text-decoration: none !important;
      cursor: pointer;
    }
    .client-logo-img {
      max-width: 150px !important;
      max-height: 48px !important;
      width: auto !important;
      height: auto !important;
      object-fit: contain !important;
      filter: grayscale(15%);
      opacity: 0.9;
      transition: all 0.25s cubic-bezier(0.16, 1, 0.3, 1);
    }
    .client-logo-item:hover .client-logo-img {
      filter: grayscale(0%);
      opacity: 1;
      transform: scale(1.08);
    }
    @media (max-width: 768px) {
      .client-logo-item {
        width: 130px !important;
        min-width: 130px !important;
        max-width: 130px !important;
        height: 52px !important;
        margin: 0 18px !important;
      }
      .client-logo-img {
        max-width: 115px !important;
        max-height: 38px !important;
      }
    }
"""

for fname in ['website-maintenance.html', 'website-maintenance-sidebar-layout.html']:
    with open(fname, 'r', encoding='utf-8') as f:
        content = f.read()

    # Replace marquee CSS
    pattern = r'/\* =========================================================\s*AUTO HORIZONTAL SCROLLING CLIENT LOGOS MARQUEE.*?(?=/\* =========================================================|\n</style>)'
    if re.search(pattern, content, re.DOTALL):
        content = re.sub(pattern, new_marquee_css.strip() + '\n', content, flags=re.DOTALL)
        print(f"Replaced marquee CSS in {fname}!")
    else:
        # Append before </style>
        content = content.replace('</style>', new_marquee_css + '\n</style>', 1)
        print(f"Appended marquee CSS in {fname}!")

    with open(fname, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"Saved {fname} successfully!")

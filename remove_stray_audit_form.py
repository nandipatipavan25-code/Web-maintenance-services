import re

stray_pattern = r'</section>\s*<div class="audit-form-inner">\s*<h3 style="color: #38bdf8; margin-top: 0; font-size: 19px;">⚡ Enter Your Website for Your Free 20-Point Audit</h3>.*?</div>\s*</div>\s*(?=<!-- RELATED ARTICLES -->)'

for fname in ['website-maintenance.html', 'website-maintenance-sidebar-layout.html']:
    with open(fname, 'r', encoding='utf-8') as f:
        content = f.read()

    match = re.search(stray_pattern, content, re.DOTALL)
    if match:
        print(f"Found stray audit-form-inner in {fname}!")
        content = content[:match.start()] + '</section>\n\n        ' + content[match.end():]
        with open(fname, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Removed stray block in {fname} successfully!")
    else:
        print(f"Pattern not found directly in {fname}, trying alternative match...")
        # Check if text is present
        pos = content.find('⚡ Enter Your Website for Your Free 20-Point Audit')
        if pos != -1:
            div_start = content.rfind('<div class="audit-form-inner">', 0, pos)
            rel_art = content.find('<!-- RELATED ARTICLES -->', pos)
            if div_start != -1 and rel_art != -1:
                content = content[:div_start] + content[rel_art:]
                with open(fname, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"Removed via index slicing in {fname}!")

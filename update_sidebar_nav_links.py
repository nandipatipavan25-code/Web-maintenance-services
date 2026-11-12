for filename in ['website-maintenance.html', 'website-maintenance-sidebar-layout.html']:
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # Target
    old_end = '<li><a href="#related-articles" class="side-nav-link"><span class="nav-num">11</span> Related Articles</a></li>'
    new_end = ('<li><a href="#related-articles" class="side-nav-link"><span class="nav-num">11</span> Related Articles</a></li>\n'
               '            <li><a href="#clients" class="side-nav-link"><span class="nav-num">12</span> Our Clients</a></li>\n'
               '            <li><a href="#speed-odometer" class="side-nav-link"><span class="nav-num">13</span> Speed Odometer</a></li>')

    if old_end in content:
        content = content.replace(old_end, new_end, 1)

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"Updated sidebar links in {filename}!")

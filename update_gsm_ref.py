for filename in ['website-maintenance.html', 'website-maintenance-sidebar-layout.html', 'test_logos.html']:
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    content = content.replace('images/clients/gsm-global.webp', 'images/clients/gsm-global.png')
    content = content.replace('gsm-global.webp', 'gsm-global.png')

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"Updated {filename} successfully!")

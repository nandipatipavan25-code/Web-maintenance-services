with open('website-maintenance.html', 'r', encoding='utf-8') as f:
    html = f.read()

import re
print("Has marquee track:", bool(re.search(r'class="clients-marquee-track"', html)))
print("Has client-logo-img:", bool(re.search(r'class="client-logo-img"', html)))
print("Has client-card-name (should be False):", bool(re.search(r'class="client-card-name"', html)))
print("Has client-card-link-hint (should be False):", bool(re.search(r'class="client-card-link-hint"', html)))

count_imgs = len(re.findall(r'images/clients/[^"]+', html))
print(f"Total client logo images in marquee (two sets of 16 for loop): {count_imgs}")

pos_rel = html.find('id="related-articles"')
pos_cli = html.find('id="clients"')
pos_odo = html.find('id="speed-odometer"')
pos_main = html.find('</main>')

print(f"Order check: Related ({pos_rel}) < Clients ({pos_cli}) < Odometer ({pos_odo}) < MainEnd ({pos_main})")
print("Positioning is correct:", pos_rel < pos_cli < pos_odo < pos_main)

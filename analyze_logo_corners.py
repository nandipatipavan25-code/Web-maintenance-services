import os
from PIL import Image

folder = "images/clients"
for f in sorted(os.listdir(folder)):
    if f.endswith('.svg'):
        continue
    p = os.path.join(folder, f)
    im = Image.open(p)
    w, h = im.size
    # sample corners
    c1 = im.getpixel((5, 5))
    c2 = im.getpixel((w - 5, 5))
    c3 = im.getpixel((5, h - 5))
    c4 = im.getpixel((w - 5, h - 5))
    print(f"{f:22} | size: {w}x{h} | corners: {c1[:3]} {c2[:3]} {c3[:3]} {c4[:3]}")

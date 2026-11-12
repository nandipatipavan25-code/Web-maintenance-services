import struct
import os

def get_image_size(fname):
    with open(fname, 'rb') as f:
        data = f.read(2)
        if data != b'\xff\xd8':
            return 'Not JPEG'
        while True:
            marker, = struct.unpack('>H', f.read(2))
            if marker in (0xffc0, 0xffc2):
                f.read(3)
                h, w = struct.unpack('>HH', f.read(4))
                return f'{w}x{h}'
            else:
                length, = struct.unpack('>H', f.read(2))
                f.read(length - 2)

images = [
    '3d-avatar-support-engineer.jpg',
    'banner-what-is-website-maintenance.jpg',
    'banner-10-maintenance-tasks.jpg',
    'banner-why-maintenance-matters.jpg',
    'banner-maintenance-schedule.jpg',
    'banner-diy-vs-professional.jpg',
    'banner-maintenance-plans.jpg',
    'banner-industries-served.jpg',
    'banner-faqs.jpg',
    'banner-choose-partner.jpg',
    'stressed-website-maintenance-owner.jpg'
]

for img in images:
    if os.path.exists(img):
        print(f'{img}: {get_image_size(img)}')

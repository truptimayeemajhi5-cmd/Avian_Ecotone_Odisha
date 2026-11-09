import os
from PIL import Image, ImageDraw

os.makedirs("figures", exist_ok=True)
search_dirs = [".", "vouchers", "figures", "raw_images", "data"]

def find_img(name):
    for d in search_dirs:
        p = os.path.join(d, name)
        if os.path.exists(p):
            return p
    return None

plate_1 = [
    ("139440.jpg", "A. Grey-headed Swamphen (nest & chicks)"),
    ("139457.jpg", "B. White-throated Kingfisher (frog prey)"),
    ("139450.jpg", "C. Bronze-winged Jacana (floating mats)"),
    ("139428.jpg", "D. Black-crowned Night Heron (juvenile)"),
    ("139476.jpg", "E. Indian Robin (male territorial perch)"),
    ("139471.jpg", "F. Indian Robin (female edge foraging)")
]

plate_2 = [
    ("139418.jpg", "A. Shikra (apex ambush vigilance)"),
    ("139395.jpg", "B. Black Kites (canopy roosting pair)"),
    ("139459.jpg", "C. Black-rumped Flameback (trunk bark-gleaner)"),
    ("139480.jpg", "D. Puff-throated Babbler (sub-canopy pair)"),
    ("139444.jpg", "E. Indian Golden Oriole (foliage pair)"),
    ("139478.jpg", "F. Jerdon's Bushlark (orthopteran prey)"),
    ("139355.jpg", "G. Scaly-breasted Munia (courtship display)"),
    ("139462.jpg", "H. Loten's Sunbird (canopy nectivory)"),
    ("139407.jpg", "I. Purple-rumped Sunbird (female dimorphism)")
]

def gen_plate(specs, cols, cw, ch, filename, title):
    rows = (len(specs) + cols - 1) // cols
    plate = Image.new("RGB", (cols * cw + 40, rows * ch + 70), (255, 255, 255))
    draw = ImageDraw.Draw(plate)
    
    for i, (fn, lbl) in enumerate(specs):
        r = i // cols
        c = i % cols
        x = 20 + c * cw
        y = 50 + r * ch
        p = find_img(fn)
        
        if p:
            im = Image.open(p).convert("RGB")
            w, h = im.size
            im = im.crop((0, 0, w, int(h * 0.92)))  # crop watermark area cleanly
            im = im.resize((cw - 10, ch - 35))
            plate.paste(im, (x + 5, y + 5))
        else:
            draw.rectangle([x + 5, y + 5, x + cw - 5, y + ch - 30], fill=(235, 235, 235), outline=(180, 180, 180))
            draw.text((x + 20, y + ch // 2 - 10), fn, fill=(100, 100, 100))
            
        draw.rectangle([x + 5, y + ch - 28, x + cw - 5, y + ch - 5], fill=(245, 245, 245))
        draw.text((x + 10, y + ch - 22), lbl, fill=(10, 10, 10))
        
    draw.text((25, 15), title, fill=(0, 0, 0))
    out_p = os.path.join("figures", filename)
    plate.save(out_p)
    print(f"SUCCESS: generated {out_p}")

gen_plate(plate_1, 2, 700, 480, "Plate_1_Wetland_Specialists.png", "Plate 1: Wetland & Water-Margin Avian Vouchers (Odisha Ecotones)")
gen_plate(plate_2, 3, 500, 380, "Plate_2_Canopy_Guilds.png", "Plate 2: Canopy Guilds & Apex Predators (Odisha Ecotones)")
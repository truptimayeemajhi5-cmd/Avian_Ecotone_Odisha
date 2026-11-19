import os
import pandas as pd
from PIL import Image, ImageDraw

VOUCHERS = [
    VOUCHERS = [
    ("V-01", "139440.jpg", "Dendrocygna javanica", "Lesser Whistling Duck", "Littoral Grassland Margin", "Adult pair resting and vigilant in dense littoral marsh grass"),
    ("V-02", "139457.jpg", "Alcedo atthis", "Common Kingfisher", "Littoral Bank / Boulder", "Adult perched on shoreline boulder scanning littoral water"),
    ("V-03", "139450.jpg", "Hydrophasianus chirurgus", "Pheasant-tailed Jacana", "Macrophyte Fringe", "Breeding adult foraging on floating lily pads with elongated toes"),
    ("V-04", "139428.jpg", "Nycticorax nycticorax", "Black-crowned Night Heron", "Woodland-Canal Buffer", "Juvenile plumage recruitment on shaded canal snag"),
    ("V-05", "139476.jpg", "Charadrius dubius", "Little Ringed Plover", "Exposed Mudflat Margin", "Conspecific shorebird territorial interaction along littoral sandbar"),
    ("V-06", "139459.jpg", "Halcyon smyrnensis", "White-throated Kingfisher", "Woodland-Marsh Edge", "Trophic subsidy: adult with amphibian prey on weathered snag"),
    ("V-07", "139478.jpg", "Ploceus philippinus", "Baya Weaver", "Grassland-Reed Margin", "Breeding-plumage male perched along reed-scrub edge stem"),
    ("V-08", "139480.jpg", "Milvus migrans", "Black Kite", "Deciduous Canopy", "Raptor pair perched in shaded mid-upper woodland buffer canopy"),
    ("V-09", "139444.jpg", "Eudynamys scolopaceus", "Western Koel", "Deciduous Canopy", "Female/immature brood parasite perched in upper canopy foliage"),
    ("V-10", "139418.jpg", "Lanius cristatus", "Brown Shrike", "Woodland-Scrub Edge", "Sit-and-wait predator perched on outer foliage scanning scrub border"),
    ("V-11", "139355.jpg", "Lonchura punctulata", "Scaly-breasted Munia", "Grassland-Reed Margin", "Granivore pair perched on dry twig along boundary margin"),
    ("V-12", "139546.jpg", "Psilopogon zeylanicus", "Brown-headed Barbet", "Deciduous Canopy", "Canopy frugivore perched on woodland branch scanning fruiting trees"),
    ("V-13", "139550.jpg", "Cinnyris asiaticus", "Purple Sunbird", "Woodland Understory", "Breeding male nectarivore perched in thorny shrub margin foliage"),
    ("V-14", "139855.jpg", "Psilopogon zeylanicus", "Brown-headed Barbet", "Deciduous Canopy", "Canopy frugivore perched along palm-woodland interface"),
    ("V-15", "139830.jpg", "Copsychus saularis", "Oriental Magpie-Robin", "Woodland Understory", "Adult male territorial perch bordering mango foliage"),
]
]

os.makedirs("data", exist_ok=True)
os.makedirs("figures", exist_ok=True)

df_v = pd.DataFrame(VOUCHERS, columns=["Voucher_ID", "Filename", "Scientific_Name_IOC_v14_1", "Common_Name", "Ecotone_Stratum", "Behavioral_Note"])
df_v.to_csv("data/voucher_catalog.csv", index=False)

def build_plate(voucher_subset, out_path, cols=3):
    imgs = []
    for vid, fname, sci, common, _, _ in voucher_subset:
        p = os.path.join("vouchers", fname)
        if os.path.exists(p):
            im = Image.open(p).convert("RGB").resize((420, 315))
            draw = ImageDraw.Draw(im)
            draw.rectangle([0, 282, 420, 315], fill=(15, 25, 35))
            draw.text((10, 291), f"{vid} | {sci} ({fname})", fill=(255, 255, 255))
            imgs.append(im)
    if not imgs:
        return
    rows = (len(imgs) + cols - 1) // cols
    canvas = Image.new("RGB", (cols * 430 + 10, rows * 325 + 10), (255, 255, 255))
    for idx, im in enumerate(imgs):
        r, c = divmod(idx, cols)
        canvas.paste(im, (10 + c * 430, 10 + r * 325))
    canvas.save(out_path, dpi=(300, 300))

build_plate([v for v in VOUCHERS if v[0] in ("V-01", "V-02", "V-03", "V-04", "V-12", "V-13")], "figures/Plate_1_Wetland_Specialists.png", cols=3)
build_plate([v for v in VOUCHERS if v[0] not in ("V-01", "V-02", "V-03", "V-04", "V-12", "V-13")], "figures/Plate_2_Canopy_Guilds.png", cols=3)
print("SUCCESS: Synchronized data/voucher_catalog.csv (15 vouchers) and updated composite plates!")

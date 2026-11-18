import os
import pandas as pd
from PIL import Image, ImageDraw

VOUCHERS = [
    ("V-01", "139440.jpg", "Porphyrio poliocephalus", "Grey-headed Swamphen", "Macrophyte Fringe", "Breeding adult tending downy chicks on floating Salvinia nest"),
    ("V-02", "139457.jpg", "Halcyon smyrnensis", "White-throated Kingfisher", "Emergent Marsh", "Trophic subsidy: adult with amphibian prey on emergent snag"),
    ("V-03", "139450.jpg", "Metopidius indicus", "Bronze-winged Jacana", "Macrophyte Fringe", "Surface macrophyte foraging utilizing elongated toes"),
    ("V-04", "139428.jpg", "Nycticorax nycticorax", "Black-crowned Night Heron", "Woodland Buffer", "Juvenile plumage recruitment on shaded canal snag"),
    ("V-05", "139478.jpg", "Mirafra affinis", "Jerdon's Bushlark", "Scrub Margin", "Parental provisioning with orthopteran prey on gravel margin"),
    ("V-06", "139480.jpg", "Pellorneum ruficeps", "Puff-throated Babbler", "Woodland Buffer", "Understory pair engaged in social allopreening"),
    ("V-07", "139459.jpg", "Halcyon smyrnensis", "White-throated Kingfisher", "Woodland-Marsh Edge", "Sit-and-wait perch vigilance overlooking littoral margin"),
    ("V-08", "139444.jpg", "Oriolus kundoo", "Indian Golden Oriole", "Deciduous Canopy", "Upper canopy foliage frugivore/insectivore foraging"),
    ("V-09", "139418.jpg", "Accipiter badius", "Shikra", "Woodland-Scrub Edge", "Apex raptor vigilance perch scanning ecotonal border"),
    ("V-10", "139476.jpg", "Copsychus fulicatus", "Indian Robin", "Scrub Margin", "Territorial display on open laterite scrub margin"),
    ("V-11", "139355.jpg", "Lonchura punctulata", "Scaly-breasted Munia", "Grassland-Reed Margin", "Granivore social perching along boundary branch"),
    ("V-12", "139546.jpg", "Anhinga melanogaster", "Oriental Darter", "Woodland Buffer", "Near Threatened piscivore drying wings on riparian snag"),
    ("V-13", "139550.jpg", "Anhinga melanogaster", "Oriental Darter", "Deciduous Canopy", "Pair roosting and vocal display in overhanging tree"),
    ("V-14", "139855.jpg", "Psilopogon zeylanicus", "Brown-headed Barbet", "Deciduous Canopy", "Canopy frugivore perched along palm-woodland interface"),
    ("V-15", "139830.jpg", "Copsychus saularis", "Oriental Magpie-Robin", "Woodland Understory", "Adult male territorial perch bordering mango foliage")
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
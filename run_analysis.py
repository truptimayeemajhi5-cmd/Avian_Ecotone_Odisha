import os, pandas as pd, numpy as np, matplotlib.pyplot as plt
os.makedirs("data", exist_ok=True)
os.makedirs("figures", exist_ok=True)
raw="""Lesser Whistling Duck,3,6,8,38,0
Fulvous Whistling Duck,0,0,8,7,0
Cotton Pygmy-Goose,0,0,93,32,0
Ruddy Shelduck,0,0,0,0,2
Indian Peafowl,4,0,0,0,3
Grey Francolin,1,0,0,0,1
Rock Pigeon,0,5,0,0,6
Spotted Dove,6,3,4,5,12
Asian Koel,1,2,0,1,2
Common Hawk-Cuckoo,2,2,0,1,4
Pied Cuckoo,0,0,2,0,0
Blue-faced Malkoha,0,0,0,0,1
Asian Palm Swift,6,4,0,0,0
Little Swift,0,0,0,6,0
Grey-headed Swamphen,0,21,4,5,4
White-breasted Waterhen,2,1,0,2,1
Eurasian Moorhen,0,0,1,2,0
Pheasant-tailed Jacana,0,0,2,7,0
Bronze-winged Jacana,0,15,0,5,0
Little Ringed Plover,3,0,0,0,7
Red-wattled Lapwing,6,0,2,4,4
Common Sandpiper,1,0,0,0,6
Wood Sandpiper,2,0,0,0,2
Common Redshank,12,0,0,0,0
River Tern,0,1,0,1,0
Black-bellied Tern,0,0,0,0,2
Asian Openbill,15,39,29,20,180
Painted Stork,1,0,1,2,0
Oriental Darter,2,18,1,15,0
Little Cormorant,3,58,37,26,3
Black-headed Ibis,9,2,7,3,0
Cinnamon Bittern,2,0,1,1,0
Black-crowned Night Heron,0,8,0,4,0
Little Egret,1,3,0,6,3
Indian Pond Heron,2,4,8,2,0
Eastern Cattle Egret,4,7,16,3,8
Medium Egret,0,6,4,4,0
Great Egret,0,0,2,0,0
Grey Heron,1,2,0,1,0
Purple Heron,0,0,3,1,0
Oriental Honey-buzzard,0,0,1,0,0
Shikra,0,0,0,1,1
Black Kite,0,4,3,0,2
Asian Green Bee-eater,2,3,10,2,7
Blue-tailed Bee-eater,5,5,7,6,4
Indian Roller,0,0,1,0,0
White-throated Kingfisher,2,6,4,2,1
Stork-billed Kingfisher,0,0,2,1,0
Pied Kingfisher,0,0,1,0,0
Coppersmith Barbet,0,1,0,1,1
Brown-headed Barbet,0,4,0,1,1
Black-rumped Flameback,0,2,0,0,0
Rufous Woodpecker,0,0,0,1,0
Rose-ringed Parakeet,0,13,0,7,4
Indian Golden Oriole,0,0,1,0,1
Black-hooded Oriole,0,4,1,1,2
Black Drongo,5,7,14,5,6
Indian Paradise-Flycatcher,0,0,3,0,0
Taiga Flycatcher,0,0,0,0,2
Brown Shrike,2,2,0,1,1
Long-tailed Shrike,4,0,3,0,0
Rufous Treepie,1,2,0,0,4
House Crow,0,4,0,1,2
Large-billed Crow,0,3,0,0,6
Ashy-crowned Sparrow-Lark,7,0,0,0,30
Jerdon Bushlark,2,0,0,0,2
Common Tailorbird,3,2,4,2,6
Plain Prinia,2,0,8,1,0
Ashy Prinia,0,2,0,0,0
Zitting Cisticola,2,0,0,0,1
Greenish Warbler,0,0,2,0,0
Barn Swallow,5,0,11,0,7
Red-whiskered Bulbul,4,0,12,2,22
Red-vented Bulbul,2,0,4,4,25
White-browed Bulbul,7,8,0,0,4
Puff-throated Babbler,0,0,1,1,0
Yellow-eyed Babbler,2,0,0,0,4
Jungle Babbler,4,0,4,3,20
Asian Pied Starling,4,4,2,5,13
Common Myna,4,0,8,2,6
Jungle Myna,2,4,0,2,0
Oriental Magpie-Robin,0,0,1,3,0
White-rumped Shama,2,0,1,0,0
Indian Robin,2,0,1,0,4
Pied Bushchat,3,0,1,0,2
Purple-rumped Sunbird,1,0,2,2,4
Purple Sunbird,2,0,2,0,2
Loten Sunbird,0,0,0,0,2
Scaly-breasted Munia,3,0,24,4,6
Tricolored Munia,5,0,0,0,3
Indian Silverbill,0,0,5,0,0
Red Avadavat,3,0,1,2,13
Grey Wagtail,3,0,0,0,4
Citrine Wagtail,1,0,0,0,3
Western Yellow Wagtail,0,0,0,0,8
White-browed Wagtail,0,2,2,2,2
White Wagtail,4,0,2,0,0
Paddyfield Pipit,8,0,0,0,5"""
rows=[x.split(",") for x in raw.strip().split("\n")]
species=[r[0] for r in rows]
counts=[[int(v) for v in r[1:]] for r in rows]
df=pd.DataFrame(counts, index=species, columns=["CL1","CL2","CL3","CL4","CL5"])
df.index.name="Species"
df.to_csv("data/odisha_avian_matrix.csv")
S=(df>0).sum()
N=df.sum()
P=df.div(N,axis=1)
H=-(P*np.log(P.replace(0,np.nan))).sum()
D=1-(P**2).sum()
J=H/np.log(S)
m=pd.DataFrame({"Richness_S":S,"Abundance_N":N,"Shannon_H":H.round(3),"Simpson_1_D":D.round(3),"Pielou_J":J.round(3)})
m.to_csv("data/community_metrics.csv")
fig,ax1=plt.subplots(figsize=(8,4.5),dpi=300)
ax2=ax1.twinx()
ax1.bar(m.index,m["Abundance_N"],color="#2b5c8f",alpha=0.75,width=0.45)
ax2.plot(m.index,m["Richness_S"],color="#c0392b",marker="o",linewidth=2.5)
ax1.set_xlabel("Sampling Session (06:00-09:00 AM)",fontweight="bold")
ax1.set_ylabel("Total Abundance (N)",color="#2b5c8f",fontweight="bold")
ax2.set_ylabel("Species Richness (S)",color="#c0392b",fontweight="bold")
plt.title("Avian Community Structure Across Odisha Ecotones",fontweight="bold")
plt.tight_layout()
plt.savefig("figures/Figure_1_Diversity_Overview.png")
print("=== FINISHED SUCCESSFULLY ===")
print(m)
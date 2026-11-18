import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.spatial.distance import pdist, squareform

# Stage 2: Read strictly from the matrix produced by make_matrix.py
df = pd.read_csv("data/odisha_avian_matrix.csv")
sites = ["CL1", "CL2", "CL3", "CL4", "CL5", "CL6"]
abund = df[sites].values.T  # shape: (6 checklists, N species)

# 1. Compute Alpha Diversity Metrics per Checklist + Pooled Regional Assemblage
alpha_rows = []
for idx, s in enumerate(sites):
    counts = df[s].values
    pos = counts[counts > 0]
    S = len(pos)
    N = int(pos.sum())
    p = pos / N
    H = -np.sum(p * np.log(p))
    simpson_1_d = 1.0 - np.sum(p ** 2)
    J = H / np.log(S)
    alpha_rows.append({
        "Checklist": s,
        "Richness_S": S,
        "Detections_N": N,
        "Shannon_H": round(float(H), 3),
        "Simpson_1_D": round(float(simpson_1_d), 3),
        "Evenness_J": round(float(J), 3)
    })

# Pooled Regional Totals
pooled = df[sites].sum(axis=1).values
pos_pool = pooled[pooled > 0]
S_pool = len(pos_pool)
N_pool = int(pos_pool.sum())
p_pool = pos_pool / N_pool
H_pool = -np.sum(p_pool * np.log(p_pool))
D_pool = 1.0 - np.sum(p_pool ** 2)
J_pool = H_pool / np.log(S_pool)
alpha_rows.append({
    "Checklist": "Pooled_Regional",
    "Richness_S": S_pool,
    "Detections_N": N_pool,
    "Shannon_H": round(float(H_pool), 3),
    "Simpson_1_D": round(float(D_pool), 3),
    "Evenness_J": round(float(J_pool), 3)
})

df_alpha = pd.DataFrame(alpha_rows)
df_alpha.to_csv("data/alpha_diversity_summary.csv", index=False)
print("\n--- Verified Alpha Diversity Summary ---")
print(df_alpha.to_string(index=False))

# 2. Pairwise Bray-Curtis Dissimilarity Matrix
bc_dist = squareform(pdist(abund, metric="braycurtis"))
df_bc = pd.DataFrame(np.round(bc_dist, 3), index=sites, columns=sites)
df_bc.to_csv("data/bray_curtis_matrix.csv")
print("\n--- Verified Pairwise Bray-Curtis Dissimilarity ---")
print(df_bc)

# 3. Hellinger-Transformed Principal Component Analysis (PCA)
row_sums = abund.sum(axis=1, keepdims=True)
hellinger = np.sqrt(abund / row_sums)
centered = hellinger - hellinger.mean(axis=0, keepdims=True)
U, s_vals, Vt = np.linalg.svd(centered, full_matrices=False)
coords = U * s_vals
var_explained = (s_vals ** 2) / np.sum(s_vals ** 2) * 100.0

df_pca = pd.DataFrame({
    "Checklist": sites,
    "PC1": np.round(coords[:, 0], 4),
    "PC2": np.round(coords[:, 1], 4)
})
df_pca.to_csv("data/pca_coordinates.csv", index=False)
print(f"\n--- Hellinger PCA Variance Explained ---")
print(f"PC1: {var_explained[0]:.1f}%, PC2: {var_explained[1]:.1f}% (Cumulative: {var_explained[0]+var_explained[1]:.1f}%)")

# 4. Generate Composite Statistical Figure (Diversity + Hellinger PCA Ordination)
fig, axes = plt.subplots(1, 2, figsize=(11, 4.5), dpi=300)

# Panel A: Richness & Shannon Diversity
sub_alpha = df_alpha[df_alpha["Checklist"].isin(sites)]
ax1 = axes[0]
bars = ax1.bar(sub_alpha["Checklist"], sub_alpha["Richness_S"], color="#2B5C8F", alpha=0.85, label="Species Richness (S)")
ax1.set_ylabel("Species Richness (S)", color="#2B5C8F", fontweight="bold")
ax1.set_ylim(0, 75)
ax1.set_title("A. Alpha Diversity Across Odisha Ecotone Checklists", fontsize=10, fontweight="bold")

ax1_twin = ax1.twinx()
ax1_twin.plot(sub_alpha["Checklist"], sub_alpha["Shannon_H"], color="#D95F02", marker="o", linewidth=2, label="Shannon Index (H')")
ax1_twin.set_ylabel("Shannon Index (H')", color="#D95F02", fontweight="bold")
ax1_twin.set_ylim(2.5, 4.3)

# Panel B: Hellinger-Transformed PCA Biplot
ax2 = axes[1]
ax2.axhline(0, color="#CCCCCC", linestyle="--", linewidth=0.8)
ax2.axvline(0, color="#CCCCCC", linestyle="--", linewidth=0.8)
ax2.scatter(coords[:, 0], coords[:, 1], color="#1B7837", s=90, zorder=3)
for i, txt in enumerate(sites):
    ax2.annotate(txt, (coords[i, 0], coords[i, 1]), xytext=(6, 5), textcoords="offset points", fontweight="bold", fontsize=9)
ax2.set_xlabel(f"PC1 ({var_explained[0]:.1f}% variance)")
ax2.set_ylabel(f"PC2 ({var_explained[1]:.1f}% variance)")
ax2.set_title("B. Hellinger-Transformed Community Ordination (PCA)", fontsize=10, fontweight="bold")

plt.tight_layout()
plt.savefig("figures/ecotone_diversity_ordination.png", dpi=300)
print("\nSUCCESS: Saved figures/ecotone_diversity_ordination.png and all verified CSV outputs!")
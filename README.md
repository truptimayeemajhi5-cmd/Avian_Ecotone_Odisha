# Microhabitat Partitioning, Trophic Guild Structure, and Avian Community Assembly Across Wetland–Minor Forest Ecotones in Odisha

**Author:** Truptimayee Majhi (Bhubaneswar, Odisha, India)  
**Primary Deliverable:** [Avian_Ecotone_Odisha_Monograph.pdf](Avian_Ecotone_Odisha_Monograph.pdf)

---

## Overview
This repository provides an end-to-end, reproducible field-to-code ecological workflow evaluating avian community structure across wetland basins and adjoining minor forests in Odisha, eastern India.

* **Empirical Dataset:** 293 raw field observations across 6 standardized transect checklists (`CL1`–`CL6`), reconciling to **1,853 individual detections** across **101 unique species** standardized to the **IOC World Bird List (v14.1)**.
* **Quantitative Analyses:** Checklist-level alpha diversity ($S$, $N$, Shannon $H'$, Simpson $1-D$, Pielou $J'$), pairwise Bray-Curtis compositional dissimilarity, and Hellinger-transformed Principal Component Analysis (PCA; PC1 = 43.8%, PC2 = 24.4%; cumulative 68.2%).
* **Photographic Vouchers:** 15 audited field vouchers (`V-01` to `V-15`) documenting breeding recruitment, aquatic–terrestrial trophic subsidies, and vertical canopy partitioning.

---

## Repository Structure
```text
Avian_Ecotone_Odisha/
├── data/
│   ├── raw_checklists_combined.csv    # Single-source-of-truth transcribed field records (293 rows)
│   ├── odisha_avian_matrix.csv        # Species-by-checklist abundance matrix (101 species × 6 surveys)
│   ├── alpha_diversity_summary.csv    # Computed alpha diversity indices per survey & regional pool
│   ├── bray_curtis_matrix.csv         # Pairwise Bray-Curtis compositional dissimilarity matrix
│   ├── pca_coordinates.csv            # Hellinger-transformed PCA ordination coordinates
│   └── voucher_catalog.csv            # Metadata & behavioral notes for all 15 photographic vouchers
├── figures/
│   ├── ecotone_diversity_ordination.png
│   ├── Plate_1_Wetland_Specialists.png
│   └── Plate_2_Canopy_Guilds.png
├── vouchers/                          # 15 verified field voucher photographs (.jpg)
├── build_pipeline.py                  # Generates authoritative raw dataset from field records
├── make_matrix.py                     # Stage 1: Builds species-by-site matrix from raw CSV
├── run_analysis.py                    # Stage 2: Computes diversity metrics, Bray-Curtis & Hellinger PCA
├── make_plates.py                     # Stage 3: Synchronizes 15-voucher catalog & composite plates
├── generate_avian_monograph.py        # Compiles final research monograph PDF
└── Avian_Ecotone_Odisha_Monograph.pdf # Final publication-ready research monograph

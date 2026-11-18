\# Microhabitat Partitioning, Trophic Guild Structure, and Avian Community Assembly Across Wetland–Minor Forest Ecotones in Odisha



\*\*Author:\*\* Truptimayee Majhi (Bhubaneswar, Odisha, India)  

\*\*Primary Deliverable:\*\* \[`Avian\_Ecotone\_Odisha\_Monograph.pdf`](Avian\_Ecotone\_Odisha\_Monograph.pdf)



\---



\## Overview

This repository provides an end-to-end, reproducible field-to-code ecological workflow evaluating avian community structure across wetland basins and adjoining minor forests in Odisha, eastern India.



\* \*\*Empirical Dataset:\*\* 293 raw field observations across 6 standardized transect checklists (`CL1`–`CL6`), reconciling to \*\*1,853 individual detections\*\* across \*\*101 unique species\*\* standardized to the \*\*IOC World Bird List (v14.1)\*\*.

\* \*\*Quantitative Analyses:\*\* Checklist-level alpha diversity ($S$, $N$, Shannon $H'$, Simpson $1-D$, Pielou $J'$), pairwise Bray-Curtis compositional dissimilarity, and Hellinger-transformed Principal Component Analysis (PCA; PC1 = 43.8%, PC2 = 24.4%; cumulative 68.2%).

\* \*\*Photographic Vouchers:\*\* 15 audited field vouchers (`V-01` to `V-15`) documenting breeding recruitment, aquatic–terrestrial trophic subsidies, and vertical canopy partitioning.



\---



\## Repository Structure

```text

Avian\_Ecotone\_Odisha/

├── data/

│   ├── raw\_checklists\_combined.csv    # Single-source-of-truth transcribed field records (293 rows)

│   ├── odisha\_avian\_matrix.csv        # Species-by-checklist abundance matrix (101 species × 6 surveys)

│   ├── alpha\_diversity\_summary.csv    # Computed alpha diversity indices per survey \& regional pool

│   ├── bray\_curtis\_matrix.csv         # Pairwise Bray-Curtis compositional dissimilarity matrix

│   ├── pca\_coordinates.csv            # Hellinger-transformed PCA ordination coordinates

│   └── voucher\_catalog.csv            # Metadata \& behavioral notes for all 15 photographic vouchers

├── figures/

│   ├── ecotone\_diversity\_ordination.png

│   ├── Plate\_1\_Wetland\_Specialists.png

│   └── Plate\_2\_Canopy\_Guilds.png

├── vouchers/                          # 15 verified field voucher photographs (.jpg)

├── build\_pipeline.py                  # Generates authoritative raw dataset from field records

├── make\_matrix.py                     # Stage 1: Builds species-by-site matrix from raw CSV

├── run\_analysis.py                    # Stage 2: Computes diversity metrics, Bray-Curtis \& Hellinger PCA

├── make\_plates.py                     # Stage 3: Synchronizes 15-voucher catalog \& composite plates

├── generate\_avian\_monograph.py        # Compiles final research monograph PDF

└── Avian\_Ecotone\_Odisha\_Monograph.pdf # Final publication-ready research monograph


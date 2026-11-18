import pandas as pd

# Stage 1: Read strictly from the authoritative raw checklist archive
df_raw = pd.read_csv("data/raw_checklists_combined.csv")

# Aggregate duplicate entries within the same checklist (e.g., species seen on outbound & return legs)
grouped = df_raw.groupby(
    ["Scientific_Name_IOC_v14_1", "Common_Name", "Family", "Trophic_Guild", "Microhabitat_Stratum", "Checklist_ID"],
    as_index=False
)["Count"].sum()

# Pivot into standardized species-by-checklist abundance matrix
matrix = grouped.pivot(
    index=["Scientific_Name_IOC_v14_1", "Common_Name", "Family", "Trophic_Guild", "Microhabitat_Stratum"],
    columns="Checklist_ID",
    values="Count"
).fillna(0).astype(int)

# Ensure chronological checklist column order
cols = ["CL1", "CL2", "CL3", "CL4", "CL5", "CL6"]
matrix = matrix[cols].reset_index()
matrix["Total_Abundance"] = matrix[cols].sum(axis=1)
matrix = matrix.sort_values(by=["Total_Abundance", "Scientific_Name_IOC_v14_1"], ascending=[False, True])

matrix.to_csv("data/odisha_avian_matrix.csv", index=False)
print(f"SUCCESS: Generated data/odisha_avian_matrix.csv ({len(matrix)} unique species, {matrix['Total_Abundance'].sum()} total detections)")
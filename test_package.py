import kegg_overlap
import os

print("Running kegg_overlap pipeline...")
kegg_overlap.run_pipeline()

expected_files = [
    "KEGG_crosstalk.csv",
    "gene_rank.csv",
    "top_genes_common_pathways.txt",
    "top_genes_venn.png"
]

print("\nVerifying outputs:")
for f in expected_files:
    if os.path.exists(f):
        print(f"✅ {f} exists.")
    else:
        print(f"❌ {f} missing.")

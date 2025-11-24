from . import downloader, parser, analysis, plotting

def run_pipeline():
    """
    Runs the full KEGG overlap analysis pipeline.
    """
    # 1. Download
    pathways_raw, gene2pw_raw, geneinfo_raw = downloader.download_kegg_data()

    # 2. Parse
    pathways = parser.parse_pathways(pathways_raw)
    gene2pw = parser.parse_gene2pw(gene2pw_raw)
    geneinfo = parser.parse_geneinfo(geneinfo_raw)

    # 3. Map
    mapping = analysis.create_mapping(gene2pw, geneinfo, pathways)
    print(f"   Pathways: {mapping['PATHWAY_ID'].nunique()}")
    print(f"   Genes: {mapping['GENE_SYMBOL'].nunique()}")

    # 4. Crosstalk
    crosstalk = analysis.compute_crosstalk(mapping, pathways)
    crosstalk.to_csv("KEGG_crosstalk.csv", index=False)
    print(f"Saved KEGG_crosstalk.csv ({len(crosstalk)} pairs)")

    # 5. Rank Genes
    gene_rank = analysis.rank_genes(mapping)
    gene_rank.to_csv("gene_rank.csv", index=False)
    print("Saved gene_rank.csv")

    # 6. Common Pathways
    top_genes, common, gene2path = analysis.find_common_pathways(mapping, gene_rank)
    
    with open("top_genes_common_pathways.txt", "w") as f:
        f.write("Top genes used: " + ", ".join(top_genes) + "\n")
        f.write(f"Common pathways ({len(common)}):\n")
        f.write("\n".join(sorted(common)))
    print("Saved top_genes_common_pathways.txt")

    # 7. Plot Venn
    gene_sets_dict = {g: gene2path[g] for g in top_genes}
    plotting.plot_venn(gene_sets_dict)

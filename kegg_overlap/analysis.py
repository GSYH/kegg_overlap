import pandas as pd
from itertools import combinations

def create_mapping(gene2pw, geneinfo, pathways):
    """
    Merges gene, pathway, and gene info dataframes.
    """
    mapping = (
        gene2pw.merge(geneinfo, on="GENE_ID", how="inner")
               .merge(pathways, on="PATHWAY_ID", how="inner")
               .drop_duplicates(subset=["PATHWAY_ID", "GENE_ID"])
    )
    mapping["GENE_SYMBOL"] = mapping["GENE_SYMBOL"].str.upper()
    return mapping

def compute_crosstalk(mapping, pathways):
    """
    Computes pairwise pathway overlaps.
    """
    print("Computing pathway overlaps...")
    pathway2genes = mapping.groupby("PATHWAY_ID")["GENE_SYMBOL"].apply(set).to_dict()
    pathway2name = dict(zip(pathways["PATHWAY_ID"], pathways["PATHWAY_NAME"]))

    records = []
    for p1, p2 in combinations(pathway2genes.keys(), 2):
        overlap = pathway2genes[p1].intersection(pathway2genes[p2])
        if overlap:
            records.append({
                "PATHWAY_ID1": p1,
                "PATHWAY_NAME1": pathway2name.get(p1, ""),
                "PATHWAY_ID2": p2,
                "PATHWAY_NAME2": pathway2name.get(p2, ""),
                "NUMBER_OF_OVERLAPPING_GENES": len(overlap),
                "LIST_OF_OVERLAPPING_GENES": ";".join(sorted(overlap))
            })

    crosstalk = pd.DataFrame(records)
    if not crosstalk.empty:
        crosstalk = crosstalk.sort_values("NUMBER_OF_OVERLAPPING_GENES", ascending=False)
    return crosstalk

def rank_genes(mapping):
    """
    Ranks genes by the number of pathways they are involved in.
    """
    gene_rank = (
        mapping.groupby("GENE_SYMBOL")["PATHWAY_ID"]
               .nunique()
               .reset_index(name="NUM_PATHWAYS")
               .sort_values("NUM_PATHWAYS", ascending=False)
    )
    return gene_rank

def find_common_pathways(mapping, gene_rank, top_n=4):
    """
    Finds common pathways for the top N genes.
    Returns:
        tuple: (top_genes_list, common_pathways_set, gene2path_dict)
    """
    top_genes = gene_rank.head(top_n)["GENE_SYMBOL"].tolist()
    gene2path = mapping.groupby("GENE_SYMBOL")["PATHWAY_ID"].apply(set).to_dict()

    sets = [gene2path[g] for g in top_genes]
    common = set.intersection(*sets)

    if not common and top_n > 2:
        # fallback to top N-1 if no common pathways
        print(f"No common pathways for top {top_n} genes, trying top {top_n-1}...")
        return find_common_pathways(mapping, gene_rank, top_n - 1)

    return top_genes, common, gene2path

import pandas as pd

def parse_pathways(pathways_raw):
    """Parses raw pathways data into a DataFrame."""
    return pd.DataFrame(
        [line.split("\t")[:2] for line in pathways_raw],
        columns=["PATHWAY_ID", "PATHWAY_NAME"]
    )

def parse_gene2pw(gene2pw_raw):
    """Parses raw gene-pathway mapping data into a DataFrame."""
    df = pd.DataFrame(
        [line.split("\t")[:2] for line in gene2pw_raw],
        columns=["GENE_ID", "PATHWAY_ID"]
    )
    # Strip 'path:' prefix if present
    df["PATHWAY_ID"] = df["PATHWAY_ID"].str.replace("path:", "", regex=False)
    return df

def extract_symbol(ginfo):
    """Extracts gene symbol from gene info string."""
    # "RNR1, MTRNR1, MT-RNR1; s-rRNA" -> "RNR1"
    if pd.isna(ginfo) or ginfo == "":
        return None
    symbol = ginfo.split(",")[0].split(";")[0].strip()
    return symbol

def parse_geneinfo(geneinfo_raw):
    """Parses raw gene info data into a DataFrame and extracts symbols."""
    parsed_geneinfo = []
    for line in geneinfo_raw:
        parts = line.split("\t")
        while len(parts) < 4:
            parts.append("")   # pad missing columns
        parsed_geneinfo.append(parts[:4])

    geneinfo = pd.DataFrame(
        parsed_geneinfo,
        columns=["GENE_ID", "TYPE", "TYPE_DESCRIPTION", "GENE_INFO"]
    )
    
    geneinfo["GENE_SYMBOL"] = geneinfo["GENE_INFO"].apply(extract_symbol)
    geneinfo = geneinfo.dropna(subset=["GENE_SYMBOL"])
    return geneinfo[["GENE_ID", "GENE_SYMBOL"]]

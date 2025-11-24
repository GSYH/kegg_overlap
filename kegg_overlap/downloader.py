import requests

def download_kegg_data():
    """
    Downloads raw data from KEGG API.
    
    Returns:
        tuple: (pathways_raw, gene2pw_raw, geneinfo_raw) as lists of strings.
    """
    url_pathways = "http://rest.kegg.jp/list/pathway/hsa"
    url_gene2pw  = "http://rest.kegg.jp/link/pathway/hsa"
    url_geneinfo = "http://rest.kegg.jp/list/hsa"

    print("Downloading data from KEGG...")
    pathways_raw = requests.get(url_pathways).text.strip().splitlines()
    gene2pw_raw  = requests.get(url_gene2pw).text.strip().splitlines()
    geneinfo_raw = requests.get(url_geneinfo).text.strip().splitlines()
    print("Download complete.")
    
    return pathways_raw, gene2pw_raw, geneinfo_raw

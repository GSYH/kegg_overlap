import kegg_overlap.downloader as downloader
import kegg_overlap.parser as parser
import kegg_overlap.analysis as analysis
import kegg_overlap.plotting as plotting

# 1. Download data only
print("Step 1: Downloading...")
pathways_raw, gene2pw_raw, geneinfo_raw = downloader.download_kegg_data()

# 2. Parse data
print("Step 2: Parsing...")
pathways = parser.parse_pathways(pathways_raw)
gene2pw = parser.parse_gene2pw(gene2pw_raw)
geneinfo = parser.parse_geneinfo(geneinfo_raw)

# 3. Create mapping (The foundation for all analysis)
print("Step 3: Mapping...")
mapping = analysis.create_mapping(gene2pw, geneinfo, pathways)

# --- Now you can run specific questions independently ---

# Question: What are the pathway overlaps?
print("\n--- Calculating Crosstalk ---")
crosstalk = analysis.compute_crosstalk(mapping, pathways)
print(crosstalk.head())

# Question: Which genes are in the most pathways?
print("\n--- Ranking Genes ---")
gene_rank = analysis.rank_genes(mapping)
print(gene_rank.head())

# Question: Plot Venn diagram for top genes?
print("\n--- Plotting Venn ---")
top_genes, common, gene2path = analysis.find_common_pathways(mapping, gene_rank)
gene_sets_dict = {g: gene2path[g] for g in top_genes}
plotting.plot_venn(gene_sets_dict, output_filename="my_custom_venn.png")

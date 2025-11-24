# KEGG Overlap Package
This package performs KEGG pathway overlap analysis, converting the logic from `kegg_overlap.ipynb` into a reusable Python module.

## Installation

### Option 1: Install from GitHub (Recommended for others)
You can install the package directly from GitHub without downloading the files manually:
```bash
pip install git+https://github.com/GSYH/kegg_overlap.git
```

### Option 2: Install Locally (For development)
If you have downloaded the source code, you can install it in editable mode:
```bash
cd kegg_package
pip install -e .
```

## Usage
You can run the full pipeline from Python:

```python
import kegg_overlap

# Run the analysis pipeline
kegg_overlap.run_pipeline()
```

This will generate the following files in your current working directory:
- `KEGG_crosstalk.csv`: Pairwise pathway overlaps.
- `gene_rank.csv`: Genes ranked by number of pathways.
- `top_genes_common_pathways.txt`: Common pathways for the top genes.
- `top_genes_venn.png`: Venn diagram of pathway overlaps.

## Modules
- `kegg_overlap.downloader`: Functions to download data from KEGG API.
- `kegg_overlap.parser`: Functions to parse raw data.
- `kegg_overlap.analysis`: Core analysis logic.
- `kegg_overlap.plotting`: Plotting functions.

## Step-by-Step Usage
If you want to run specific parts of the analysis (e.g., just get the gene ranking or just the crosstalk), you can import the modules individually:

```python
import kegg_overlap.downloader as downloader
import kegg_overlap.parser as parser
import kegg_overlap.analysis as analysis

# 1. Get the data
pathways_raw, gene2pw_raw, geneinfo_raw = downloader.download_kegg_data()
pathways = parser.parse_pathways(pathways_raw)
gene2pw = parser.parse_gene2pw(gene2pw_raw)
geneinfo = parser.parse_geneinfo(geneinfo_raw)

# 2. Create the master mapping
mapping = analysis.create_mapping(gene2pw, geneinfo, pathways)

# 3. Run specific analysis
# Example: Just get gene rankings
gene_rank = analysis.rank_genes(mapping)
print(gene_rank.head())

# Example: Just compute crosstalk
crosstalk = analysis.compute_crosstalk(mapping, pathways)
print(crosstalk.head())
```

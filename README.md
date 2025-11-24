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

# KEGG Overlap

![Python](https://img.shields.io/badge/python-3.6%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)

**KEGG Overlap** is a Python package for analyzing pathway overlaps using data from the KEGG database. It automates the retrieval of pathway and gene information, computes the "crosstalk" (gene overlap) between pathways, and ranks genes based on their pathway connectivity.

This tool is designed for bioinformaticians and researchers who need to programmatically explore the relationships between biological pathways.

## Installation

You can install `kegg_overlap` directly from GitHub using `pip`.

### Option 1: Install from GitHub (Recommended)
To install the latest version of the package:

```bash
pip install git+https://github.com/GSYH/kegg_overlap.git
```

### Option 2: Install Locally (For Development)
If you are developing or modifying the package, clone the repository and install in editable mode:

```bash
git clone https://github.com/GSYH/kegg_overlap.git
cd kegg_overlap
pip install -e .
```

## Usage

You can run the full analysis pipeline with a single command, or use individual modules for specific tasks.

### Quick Start
To run the complete analysis and generate all reports:

```python
import kegg_overlap

kegg_overlap.run_pipeline()
```

This will generate:
*   `KEGG_crosstalk.csv`: Pairwise pathway overlaps.
*   `gene_rank.csv`: Genes ranked by pathway frequency.
*   `top_genes_venn.png`: Venn diagram of top genes.

### Advanced Usage
For more granular control, import specific modules:

```python
import kegg_overlap.downloader as downloader
import kegg_overlap.analysis as analysis
import kegg_overlap.parser as parser

# 1. Download and Parse
raw_data = downloader.download_kegg_data()
pathways = parser.parse_pathways(raw_data[0])
gene2pw = parser.parse_gene2pw(raw_data[1])
geneinfo = parser.parse_geneinfo(raw_data[2])

# 2. Analyze
mapping = analysis.create_mapping(gene2pw, geneinfo, pathways)
gene_rank = analysis.rank_genes(mapping)

print(gene_rank.head())
```

## Documentation
For more details on the implementation, please refer to the source code in the `kegg_overlap` directory.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements
We would like to thank **Professor Cristina Mitrea** for her guidance in the **BIOINF 575: Programming Laboratory in Bioinformatics** course at the University of Michigan.

This package utilizes data from the **[KEGG API](http://rest.kegg.jp/)**. We acknowledge and thank the Kyoto Encyclopedia of Genes and Genomes for providing this resource.

# Welcome to KEGG Overlap

| | |
|---|---|
| **Author:** | Shuoyuan Gao |
| **Date:** | Nov 24, 2025 |
| **Version:** | 0.1.0 |
| **Python:** | 3.6+ |

**KEGG Overlap** is a Python package for analyzing pathway overlaps using data from the KEGG database.

## Features
- **Automated Download**: Fetches the latest pathway and gene data from the KEGG API.
- **Crosstalk Analysis**: Computes the number of overlapping genes between every pair of pathways.
- **Gene Ranking**: Identifies which genes are involved in the most pathways.
- **Visualization**: Generates Venn diagrams for top genes.

## Installation

```bash
pip install git+https://github.com/GSYH/kegg_overlap.git
```

## Quick Start

```python
import kegg_overlap
kegg_overlap.run_pipeline()
```

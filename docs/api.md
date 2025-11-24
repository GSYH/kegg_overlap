# API Reference

## Main Pipeline

### `kegg_overlap.run_pipeline()`
Runs the complete analysis workflow:
1. Downloads data.
2. Parses data.
3. Computes crosstalk.
4. Ranks genes.
5. Generates plots.

## Modules

### Downloader
**`kegg_overlap.downloader.download_kegg_data()`**
*   Downloads raw text data from KEGG API endpoints.
*   Returns: Tuple of `(pathways_raw, gene2pw_raw, geneinfo_raw)`.

### Parser
**`kegg_overlap.parser.parse_pathways(raw_data)`**
*   Converts raw pathway text into a DataFrame.

**`kegg_overlap.parser.parse_gene2pw(raw_data)`**
*   Converts raw gene-pathway mapping into a DataFrame.

### Analysis
**`kegg_overlap.analysis.compute_crosstalk(mapping, pathways)`**
*   Calculates the number of overlapping genes between all pathway pairs.

**`kegg_overlap.analysis.rank_genes(mapping)`**
*   Counts the number of pathways each gene belongs to.

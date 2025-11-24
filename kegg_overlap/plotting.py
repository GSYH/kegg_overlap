import matplotlib.pyplot as plt

def plot_venn(gene_sets_dict, output_filename="top_genes_venn.png"):
    """
    Plots a Venn diagram for the given gene sets.
    """
    try:
        from venn import venn
        venn(gene_sets_dict)
        plt.savefig(output_filename)
        print(f"Saved {output_filename}")
    except ImportError:
        print("Package 'venn' not installed — trying matplotlib-venn fallback.")
        try:
            from matplotlib_venn import venn3
            keys = list(gene_sets_dict.keys())
            sets = list(gene_sets_dict.values())
            
            if len(keys) > 3:
                print("matplotlib-venn only supports up to 3 sets. Using top 3.")
                keys = keys[:3]
                sets = sets[:3]
            
            if len(keys) == 3:
                venn3(subsets=sets, set_labels=keys)
                plt.savefig(output_filename)
                print(f"Saved {output_filename}")
            else:
                print(f"Need exactly 3 sets for venn3 fallback, got {len(keys)}. Skipping plot.")
        except ImportError:
             print("Package 'matplotlib-venn' also not installed. Skipping plot.")

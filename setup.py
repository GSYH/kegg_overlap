from setuptools import setup, find_packages

setup(
    name="kegg_overlap",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "requests",
        "pandas",
        "matplotlib",
        "matplotlib-venn",
        # "venn" # Optional, as per notebook logic
    ],
    author="Shuoyuan Gao",
    description="A package for KEGG pathway overlap analysis",
)

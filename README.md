# MGE_Finder

Please use the following command, and then replace the actual paths in `config.yaml` and `Snakefile`. This will automatically create the environments for Genomad, IntegronFinder, MobileOG, and ISEScan, and finally output the results to the directory you specified.
```Bash
conda install snakemake=5.26.0
snakemake -s /path/to/Snakefile -j 32 --cores 10 --use-conda
```

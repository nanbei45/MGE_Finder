import pandas as pd
from pathlib import Path

configfile: '/data/zqwangyansu/hl/human_gut_hdi/10442/find_mge/config.yaml'
PATHS = config["paths"]

rule all:
    input:
        PATHS['output_genomad_dir'],
        PATHS['output_isescan_dir'],
        PATHS['output_integron_dir'],
        PATHS['output_mobileOG_dir']
        
        

rule genomad:
    input:
        genomic_file = PATHS['input_genomic_file']
    output:
        output_genomad_dir = directory(PATHS['output_genomad_dir'])
    params:
        genomad_db = PATHS['genomad_db']
    conda:
        PATHS['genomad_env']
    shell:
        "python genomad.py "
        "--input_genomic_file {input.genomic_file} "
        "--output_dir {output.output_genomad_dir} "
        "--genomad_db {params.genomad_db}"

rule isescan:
    input:
        genomic_file = PATHS['input_genomic_file']
    output:
        output_isescan_dir = directory(PATHS['output_isescan_dir'])
    params:
        nthread = 10
    conda:
        PATHS['isescan_env']
    shell:
        "python isescan.py "
        "--input_genomic_file {input.genomic_file} "
        "--output_dir {output.output_isescan_dir} "
        "--nthread {params.nthread}"

rule integron:
    input:
        genomic_file = PATHS['input_genomic_file']
    output:
        output_integron_dir = directory(PATHS['output_integron_dir'])
    conda:
        PATHS['integron_env']
    shell:
        "python integron.py "
        "--input_genomic_file {input.genomic_file} "
        "--output_dir {output.output_integron_dir}"

rule mobileOG:
    input:
        genomic_file = PATHS['input_genomic_file']
    output:
        output_mobileOG_dir = directory(PATHS['output_mobileOG_dir'])
    params:
        diamond_mobileOG_db = PATHS['diamond_mobileOG_db']
    conda:
        PATHS['mobileog_env']
    shell:
        "python mobileOG.py "
        "--input_genomic_file {input.genomic_file} "
        "--diamond_mobileOG_db {params.diamond_mobileOG_db} "
        "--output_dir {output.output_mobileOG_dir}"




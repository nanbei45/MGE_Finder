import subprocess
from pathlib import Path
import argparse

def run_integron(input_genomic_file, output_dir):
    '''
        https://github.com/gem-pasteur/Integron_Finder
    '''
    subprocess.run([
        "integron_finder",
        "--local-max",
        "--func-annot",
        str(input_genomic_file),
        "--outdir", str(output_dir),
    ],check=True)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('--input_genomic_file', type=str, required=True)
    parser.add_argument('--output_dir', type=str, required=True)

    args = parser.parse_args()

    input_genomic_file = args.input_genomic_file
    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    run_integron(input_genomic_file, output_dir)

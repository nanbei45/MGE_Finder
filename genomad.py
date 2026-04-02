                              import subprocess
import argparse

def run_genomad(input_genomic_file, output_file,genomad_db):
    '''
        https://github.com/apcamargo/genomad/
    '''
    subprocess.run([
        "genomad", "end-to-end",
        "--cleanup",
        "--splits", "8",
        str(input_genomic_file),
        str(output_file),
        str(genomad_db)
    ],check=True)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('--input_genomic_file', type=str, required=True)
    parser.add_argument('--output_dir', type=str, required=True)
    parser.add_argument('--genomad_db', type=str, required=True)                               
    args = parser.parse_args()

    input_genomic_file = args.input_genomic_file
    output_dir = args.output_dir
    genomad_db = args.genomad_db

    run_genomad(input_genomic_file, output_dir,genomad_db)

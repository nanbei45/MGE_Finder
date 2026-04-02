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
    parser = argparse.ArgumentParser(description='使用ISEScan检测插入序列')
    parser.add_argument('--input_genomic_file', type=str, required=True)
    parser.add_argument('--output_dir', type=str, required=True)
    # 执行参数解析
    args = parser.parse_args()

    input_genomic_file = args.input_genomic_file
    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    run_integron(input_genomic_file, output_dir)
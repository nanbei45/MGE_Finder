import subprocess
import argparse

def run_isescan(input_genomic_file, output_dir,nthread):
    '''
        https://github.com/xiezhq/ISEScan
    '''
    subprocess.run([
        "isescan.py",
        "--seqfile", str(input_genomic_file),
        "--output", str(output_dir),
        "--nthread", str(nthread),
    ],check=True)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='使用ISEScan检测插入序列')
    parser.add_argument('--input_genomic_file', type=str, required=True)
    parser.add_argument('--output_dir', type=str, required=True)
    parser.add_argument('--nthread', type=int, required=True)
    # 执行参数解析
    args = parser.parse_args()

    input_genomic_file = args.input_genomic_file
    output_dir = args.output_dir
    nthread = args.nthread

    run_isescan(input_genomic_file, output_dir,nthread)
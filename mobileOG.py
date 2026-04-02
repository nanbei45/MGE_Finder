import argparse
import subprocess
from pathlib import Path

def run_prodigal(input_genomic_file, prodigal_file):
    subprocess.run([
        "prodigal",
        "-i", str(input_genomic_file),
        "-a", str(prodigal_file),
        "-p", "meta",
        "-f", "gff"
    ],check=True)

def run_diamond(prodigal_file, mobileOG_db, diamond_file):
    subprocess.run([
        "diamond",
        "blastp",
        "--query", str(prodigal_file),
        "--db", str(mobileOG_db),
        "--out", str(diamond_file),
        "--outfmt", "6",
        "stitle", "qtitle" ,"pident", "bitscore", "slen", "evalue", "qlen", "sstart", "send", "qstart", "qend",
        "--query-cover", "90",
        "-e", "1e-20",
        "-k", "15",
        "--id", "90"
    ], check=True)


def run_mobileOG(mobileOG_file,diamond_file,mobileOG_output_dir,mobileOG_db_csv):
    '''
        https://mobileogdb.flsi.cloud.vt.edu/
        https://zhuanlan.zhihu.com/p/688079390
    '''
    subprocess.run([
        "python3", str(mobileOG_file),
        "--i", str(diamond_file),
        "--o", str(mobileOG_output_dir),
        "-m",str(mobileOG_db_csv)

    ],check=True)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='使用ISEScan检测插入序列')
    parser.add_argument('--input_genomic_file', type=str, required=True)
    parser.add_argument('--diamond_mobileOG_db', type=str, required=True)
    parser.add_argument('--output_dir', type=str, required=True)

    # 执行参数解析
    args = parser.parse_args()

    input_genomic_file = args.input_genomic_file
    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    diamond_mobileOG_db = args.diamond_mobileOG_db

    #mobileOG_file = '/data/zqwangyansu/hl/software/mobileOG/mobileOG-db/mobileOG-pl/mobileOGs-pl-kyanite.py'
    #mobileOG_db_csv = '/data/zqwangyansu/hl/database/mobileOG-db/mobileOG-db-beatrix-1.6-All.csv'


    prodigal_file = output_dir / "prodigal.faa"
    diamond_file = output_dir / "diamond.txt"
    #mobileOG_output_file = output_dir / "mobileOG"

    run_prodigal(input_genomic_file, prodigal_file)
    run_diamond(prodigal_file,diamond_mobileOG_db,diamond_file)
    #run_mobileOG(mobileOG_file,diamond_file,mobileOG_output_file,mobileOG_db_csv)


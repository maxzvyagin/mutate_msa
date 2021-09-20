import os
from tqdm import tqdm

if __name__ == '__main__':
    all_files = os.listdir('mutations')
    done_files = os.listdir('alphafold_runs')
    for f in tqdm(all_files):
        if f.split('.fasta')[0] not in done_files:
            os.system('cp mutations/{} uncompleted_mutations/'.format(f))
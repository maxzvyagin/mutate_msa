import os
from tqdm import tqdm

def alphafold(path):
    # run alphafold
    os.system('bash /opt/alphafold/run.sh -d /lambda_stor/data/hsyoo/AlphaFoldData  -o ~/mutate_msa/folding_results/ '
              '-f {} -t 2020-05-01 -p casp14 -m model_1,'
              'model_2,model_3,model_4,model_5 -a 0,1,3,4,5,6,7'.format(path))


if __name__ == "__main__":
    files = os.listdir('mutations')
    for f in tqdm(files):
        alphafold('mutations/{}'.format(f))


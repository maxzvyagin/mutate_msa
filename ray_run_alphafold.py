import os
from tqdm import tqdm
import subprocess
import ray

@ray.remote(num_gpus=1, num_cpus=8)
def alphafold(path):
    # run alphafold
    print("Running for path {}...".format(path))
    subprocess.run(['bash', 'run.sh', '-d /lambda_stor/data/hsyoo/AlphaFoldData',
                    '-o ~/mutate_msa/folding_results/',
                    '-f {}'.format(path), '-t 2020-05-01', '-p casp14',
                    '-m model_1, model_2,model_3,model_4,model_5 -g'])


if __name__ == "__main__":
    ray.init()
    files = os.listdir('test_mutations')
    ray.get([alphafold._remote(args=[f]) for f in tqdm(files)])
    # for f in tqdm(files):
    #     alphafold('mutations/{}'.format(f))

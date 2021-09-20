import os
from tqdm import tqdm
import subprocess
import ray

@ray.remote(num_gpus=1, num_cpus=8)
def alphafold(path):
    # run alphafold
    print("Running for path {}...".format(path))
    # print(os.environ['CUDA_VISIBLE_DEVICES'])
    os.system('bash run.sh -d /lambda_stor/data/hsyoo/AlphaFoldData -o ~/mutate_msa/folding_results/ -f test_mutations/{} -t 2020-05-01 -p casp14 -m model_1,model_2,model_3,model_4,model_5 -a {}'.format(path, os.environ['CUDA_VISIBLE_DEVICES']))


if __name__ == "__main__":
    ray.init()
    files = os.listdir('mutations')
    ray.get([alphafold._remote(args=[f]) for f in tqdm(files)])
    # for f in tqdm(files):
    #     alphafold('mutations/{}'.format(f))

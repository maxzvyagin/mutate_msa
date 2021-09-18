import os
from tqdm import tqdm

def alphafold(path):
    # run alphafold



if __name__ == "__main__":
    files = os.listdir('mutatations')
    for f in tqdm(files):
        alphafold('mutations/{}'.format(f))


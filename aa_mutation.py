from argparse import ArgumentParser
from pathlib import Path
import random
import os
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
import sys
from tqdm import tqdm

# global variable definition
protein_alphabet = [
    "A",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "K",
    "L",
    "M",
    "N",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "V",
    "W",
    "Y",
]

ga98 = 'TTYKLILNLKQAKEEAIKELVDAGTAEKYFKLIANAKTVEGVWTLKDEIKTFTVTE'
gb98 = 'TTYKLILNLKQAKEEAIKELVDAGTAEKYFKLIANAKTVEGVWTYKDEIKTFTVTE'


def point_mutate(sequence):
    sequence = list(sequence)
    selected_index = random.randrange(len(sequence))
    mutation = random.choice(protein_alphabet)
    sequence[selected_index] = mutation
    return "".join(sequence)


def deletion(sequence):
    sequence = list(sequence)
    selected_index = random.randrange(len(sequence))
    sequence.pop(selected_index)
    return "".join(sequence)


def insertion(sequence):
    sequence = list(sequence)
    selected_index = random.randrange(len(sequence))
    mutation = random.choice(protein_alphabet)
    sequence.insert(selected_index, mutation)
    return "".join(sequence)


def generate_mutations(seq, mutation_func, num_seqs, base_id, base_name, out_dir):
    for i in tqdm(range(num_seqs)):
        a = Seq(mutation_func(seq))
        a_record = SeqRecord(
            a,
            id="{}.{}".format(base_id, i),
            name=base_name,
            description=base_name
        )
        with open(out_dir + "/{}_{}.fasta".format(base_id, i), "w") as output_handle:
            SeqIO.write(a_record, output_handle, "fasta")


if __name__ == '__main__':
    random.seed(777)
    # get command line settings
    parser = ArgumentParser()
    parser.add_argument('-n', '--num_seqs', help="Number of sequences to generate per mutation type.", default=200)
    parser.add_argument('-o', '--out_dir', help="Directory to store generated files", default="mutations")
    args = parser.parse_args()
    # create directory
    try:
        os.mkdir(args.out_dir)
    except OSError:
        print("WARNING: out_dir already exists, overwrite??")
        res = ""
        while True:
            res = input("yes/no:").strip()
            if res == "yes":
                break
            elif res == "no":
                sys.exit()
            else:
                continue
    # generate concatenated_mutations
    print("Generating point mutation sequences...")
    generate_mutations(ga98, point_mutate, args.num_seqs, "GA98_PM",
                       "GA98 Point Mutation Sequence", args.out_dir)
    # with open(args.out_dir+"/ga98_point_mutations.fasta", "w") as output_handle:
    #     SeqIO.write(point_mutation_sequences_ga98, output_handle, "fasta")

    generate_mutations(gb98, point_mutate, args.num_seqs, "GB98_PM",
                       "GB98 Point Mutation Sequence", args.out_dir)
    # with open(args.out_dir+"/gb98_point_mutations.fasta", "w") as output_handle:
    #     SeqIO.write(point_mutation_sequences_gb98, output_handle, "fasta")

    print("Generating insertion mutation sequences...")
    generate_mutations(ga98, insertion, args.num_seqs, "GA98_IM",
                       "GA98 Insertion Mutation Sequence", args.out_dir)
    # with open(args.out_dir+"/ga98_insertion_mutations.fasta", "w") as output_handle:
    #     SeqIO.write(insertion_sequences_ga98, output_handle, "fasta")

    generate_mutations(gb98, insertion, args.num_seqs, "GB98_IM",
                       "GB98 Insertion Mutation Sequence", args.out_dir)
    # with open(args.out_dir+"/gb98_insertion_mutations.fasta", "w") as output_handle:
    #     SeqIO.write(insertion_sequences_gb98, output_handle, "fasta")

    print("Generating deletion mutation sequences...")
    generate_mutations(ga98, deletion, args.num_seqs, "GA98_DM",
                       "GA98 Deletion Mutation Sequence", args.out_dir)
    # with open(args.out_dir+"/ga98_deletion_mutations.fasta", "w") as output_handle:
    #     SeqIO.write(deletion_sequences_ga98, output_handle, "fasta")

    generate_mutations(gb98, deletion, args.num_seqs, "GB98_DM",
                       "GB98 Deletion Mutation Sequence", args.out_dir)
    # with open(args.out_dir+"/gb98_deletion_mutations.fasta", "w") as output_handle:
    #     SeqIO.write(deletion_sequences_gb98, output_handle, "fasta")

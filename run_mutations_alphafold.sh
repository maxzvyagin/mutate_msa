#!/bin/bash
for FILE in ~/mutate_msa/mutations/*
do
	echo $FILE
#	bash /opt/alphafold/run.sh -d /lambda_stor/data/hsyoo/AlphaFoldData  -o ~/mutate_msa/alphafold_runs/ -f -mutations/GB98_PM_99.fasta -t 2020-05-01 -p casp14 -m model_1,model_2,model_3,model_4,model_5 -a 0,1,2,3,4,5,6,7
	bash run.sh -d /lambda_stor/data/hsyoo/AlphaFoldData  -o ~/mutate_msa/alphafold_runs/ -f $FILE -t 2020-05-01 -p casp14 -m model_1,model_2,model_3,model_4,model_5 -a 0,1,2,3,4,5,6,7
#	command2 on $OUTPUT
#	commandN
done
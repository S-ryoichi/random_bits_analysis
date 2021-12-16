#!/bin/sh

mkdir exec
mkdir bin_ascii_data
mkdir result

gcc -o ./exec/arrange_data ./program/arrange_data/file_update.c
gcc -o ./exec/markov_veryfy ./program/markov_model/The_Markov_model.c
gcc -o ./exec/prediction2 ./program/nextbit_prediction/2bit_prediction.c
gcc -o ./exec/prediction3 ./program/nextbit_prediction/3bit_prediction.c
gcc -o ./exec/markov_csv ./program/z-test/markov.c

for filename in ./data/*.txt; do
    basefile=$(basename $filename .txt)
    binfilename=./bin_ascii_data/${basefile}_out.txt
    dirname=./result/${basefile}
    
    mkdir $dirname

    ./exec/arrange_data $filename $binfilename
    ./exec/markov_veryfy $binfilename ${dirname}/${basename}_markov.txt
    ./exec/prediction2 $binfilename ${dirname}/${basename}_2predict.txt
    ./exec/prediction3 $binfilename ${dirname}/${basename}_3predict.txt
    ./exec/markov_csv $binfilename ${dirname}/${basename}_markov.csv
    python3 ./program/z-test/csv_analysis.py ${dirname}/${basename}_markov.csv ${dirname}/${basename}_z_test.csv
done



###############
# ls
# 
# cp ../log/rand01.txt ./data/rand01.txt
# 
# cd program
# 
# gcc -o ./out ./file_update.c
# 
# ./out
# 
# gcc -o ../exec/prediction ./2bit_prediction.c
# 
# ../exec/prediction
# 
# gcc -o ../exec/prediction ./3bit_prediction.c
# 
# ../exec/prediction
# 
# gcc -o ../exec/markov  ./The_Markov_model.c
# 
# ../exec/markov
# 
# gcc -o ../exec/markov_csv ./markov.c
# 
# ../exec/markov_csv
# 
# python3 csv_analysis.py ../markov_result.csv ../solve_p_value.csv
# 
# ./graph.sh
# 
# cd ..
# 
# mkdir ./result
# 
# mv ./*.txt ./*.csv ./*.png ./result
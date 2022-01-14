#!/bin/sh

mkdir exec
mkdir result
mkdir log

gcc -o ./exec/markov_veryfy ./program/markov_model/The_Markov_model.c
gcc -o ./exec/prediction2 ./program/nextbit_prediction/2bit_prediction.c
gcc -o ./exec/prediction3 ./program/nextbit_prediction/3bit_prediction.c
gcc -g -o ./exec/markov_csv ./program/z-test/markov_1000.c
# gcc -o ./exec/markov_csv ./program/z-test/markov.c

for filename in ./bin_ascii_data/*.txt; do
    basefile=$(basename $filename .txt)
    binfilename=./bin_ascii_data/${basefile}.txt
    dirname=./result/${basefile}
    
    mkdir $dirname
    mkdir $dirname/markov_csv
    mkdir ./result/z_test

    echo "./exec/markov_veryfy $binfilename ${dirname}/${basefile}_markov.txt"
    ./exec/markov_veryfy $binfilename ${dirname}/${basefile}_markov.txt > ./log/${basefile}_markov.log

    echo "./exec/prediction2 $binfilename ${dirname}/${basefile}_2predict.txt"
    ./exec/prediction2 $binfilename ${dirname}/${basefile}_2predict.txt > ./log/${basefile}_2predict.log

    echo "./exec/prediction3 $binfilename ${dirname}/${basefile}_3predict.txt"
    ./exec/prediction3 $binfilename ${dirname}/${basefile}_3predict.txt > ./log/${basefile}_3predict.log

    echo "./exec/markov_csv $binfilename ${dirname}/${basefile}_markov.csv"
    ./exec/markov_csv $binfilename ${dirname}/markov_csv/${basefile}_markov > ./log/${basefile}_markov.log

    # for csvfilename in ./
    python3 ./program/z-test/z_test.py ${dirname}/markov_csv/ ./result/z_test/${basefile}_z_test.csv
done

python3 ./program/z-test/z-test_result.py ./result/z_test/ ./result/z-test_result.csv


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

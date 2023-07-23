#!/bin/sh

mkdir exec
mkdir bin_ascii_data
mkdir result
mkdir log

gcc -o ./exec/arrange_data ./program/arrange_data/file_update.c
gcc -o ./exec/markov_verify ./program/markov_model/The_Markov_model.c
gcc -o ./exec/prediction2 ./program/nextbit_prediction/2bit_prediction.c
gcc -o ./exec/prediction3 ./program/nextbit_prediction/3bit_prediction.c
gcc -g -o ./exec/markov_csv ./program/t-test/markov_1000.c
# gcc -o ./exec/markov_csv ./program/t-test/markov.c

for filename in ./data/*.txt; do
    basefile=$(basename $filename .txt)
    binfilename=./bin_ascii_data/${basefile}.txt
    dirname=./result/${basefile}
    
    mkdir $dirname
    mkdir $dirname/markov_csv
    mkdir ./result/t-test
    mkdir ./result/chi2test

    echo "./exec/arrange_data $filename $binfilename"
    ./exec/arrange_data $filename $binfilename

    echo "./exec/markov_verify $binfilename ${dirname}/${basefile}_markov.txt"
    ./exec/markov_verify $binfilename ${dirname}/${basefile}_markov.txt > ./log/${basefile}_markov.log

    echo "./exec/prediction2 $binfilename ${dirname}/${basefile}_2predict.txt"
    ./exec/prediction2 $binfilename ${dirname}/${basefile}_2predict.txt > ./log/${basefile}_2predict.log

    echo "./exec/prediction3 $binfilename ${dirname}/${basefile}_3predict.txt"
    ./exec/prediction3 $binfilename ${dirname}/${basefile}_3predict.txt > ./log/${basefile}_3predict.log

    echo "./exec/markov_csv $binfilename ${dirname}/${basefile}_markov.csv"
    ./exec/markov_csv $binfilename ${dirname}/markov_csv/${basefile}_markov > ./log/${basefile}_markov.log

    python3 ./program/t-test/t-test.py ${dirname}/markov_csv/ ./result/t-test/${basefile}.csv
done

# python3 ./program/t-test/t-test_result.py ./result/t-test/ ./result/t-test_result.csv > ./result/t-test/t-test_result.txt
python3 ./program/t-test/t-test_result.py ./result/t-test/ ./result/t-test_result.csv

## fot the testing RO circuit
mkdir ./result/image
python3 ./program/t-test/graph.py ./result/t-test_result.csv ./result/image/

#
python3 ./program/t-test/chi2test.py ./result/t-test/ ./result/chi2test/
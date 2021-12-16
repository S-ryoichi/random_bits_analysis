#!/bin/sh

ls

cp ../log/rand01.txt ./data/rand01.txt

cd program

gcc -o ./out ./file_update.c

./out

gcc -o ../exec/prediction ./2bit_prediction.c

../exec/prediction

gcc -o ../exec/prediction ./3bit_prediction.c

../exec/prediction

gcc -o ../exec/markov  ./The_Markov_model.c

../exec/markov

gcc -o ../exec/markov_csv ./markov.c

../exec/markov_csv

python3 csv_analysis.py ../markov_result.csv ../solve_p_value.csv

./graph.sh

cd ..

mkdir ./result

mv ./*.txt ./*.csv ./*.png ./result
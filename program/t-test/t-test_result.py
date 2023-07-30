from fileinput import filename
import os
import sys
import pandas as pd
import tqdm

file_name = os.listdir(sys.argv[1])
csv_file = [s for s in file_name if ".csv" in s]
print("f_name is {}".format(csv_file))
csv_file_strip = []

def main():
    writecsv = []

    for f_name in tqdm.tqdm(csv_file):
        print(f_name)
        f_data = pd.read_csv(sys.argv[1] + str(f_name), engine="python")
        f_booldata = (f_data >= 0.005)
        # 確率誤差の条件
        print(f_booldata.sum())
        writecsv.append(f_booldata.sum())
        print("")
    fw = pd.DataFrame(writecsv, columns=["P(00)", "P(01)", "P(10)", "P(11)", "P(00|00)", "P(01|00)", "P(10|00)", "P(11|00)", "P(00|01)", "P(01|01)", "P(10|01)", "P(11|01)", "P(00|10)", "P(01|10)", "P(10|10)", "P(11|10)", "P(00|11)", "P(01|11)", "P(10|11)", "P(11|11)"])
    # fw = pd.DataFrame(writecsv, columns=["00", "01", "10", "11", "00->00", "00->01", "00->10", "00->11", "01->00", "01->01", "01->10", "01->11", "10->00", "10->01", "10->10", "10->11", "11->00", "11->01", "11->10", "11->11"])
    # fw = fw.rename(columns={"00": "state_00","01": "state_01","10": "state_10","11": "state_11"})
    csv_file_strip = [listname.replace(".csv", "") for listname in csv_file]
    fw.insert(0, "label", csv_file_strip)
    fw.to_csv(sys.argv[2])

if __name__ == "__main__":
    main()

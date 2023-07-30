import os
import sys
import pandas as pd
from scipy.special import gammainc, gammaincc

file_name = os.listdir(sys.argv[1])
csv_file = [s for s in file_name if ".csv" in s]
print("f_name is {}".format(csv_file))
csv_file_strip = []

class Data:
    def __init__(self):
        self.index = ""
        self.sum = 0
        self.distribute = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    def set_index(self, name):
        self.index = name
    def increment(self, area):
        self.distribute[area] = self.distribute[area] + 1
        self.sum = self.sum + 1
    def get_index(self):
        return self.index
    def get_dist(self):
        return self.distribute
    def get_sum(self):
        return self.sum
    def __del__(self):
        self.index = ""
        self.sum = 0
        self.distribute = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

def insert(data, num):
    if (num <= 0.1 and num >= 0.0):
        data.increment(0)
    elif (num <= 0.2 and num > 0.1):
        data.increment(1)
    elif (num <= 0.3 and num > 0.2):
        data.increment(2)
    elif (num <= 0.4 and num > 0.3):
        data.increment(3)
    elif (num <= 0.5 and num > 0.4):
        data.increment(4)
    elif (num <= 0.6 and num > 0.5):
        data.increment(5)
    elif (num <= 0.7 and num > 0.6):
        data.increment(6)
    elif (num <= 0.8 and num > 0.7):
        data.increment(7)
    elif (num <= 0.9 and num > 0.8):
        data.increment(8)
    elif (num <= 1.0 and num > 0.9):
        data.increment(9)
    else:
        print(num)
        print("error")
        exit(-1)

def chi2_test(data):
    chi2 = 0
    separate_data = data.get_dist()
    separate_mean = data.get_sum() / 10
    # print(separate_mean)
    for val in separate_data:
        chi2 = chi2 + (((val - separate_mean) ** 2) / separate_mean)
        # print(chi2)
    p_val = gammaincc((9 / 2), (chi2 / 2))
    return [p_val]
    # return float(p_val)

def main():
    for f_name in csv_file:
        linedata = []
        writecsv = []
        print(f_name)
        fr_data = pd.read_csv(sys.argv[1] + str(f_name), index_col=0, engine="python")
        # 以降修正予定
        for index, row in fr_data.items():
        # for index, row in fr_data.iteritems():
            data = Data()
            data.set_index(index)
            for n, d in enumerate(row):
                insert(data, d)
            linedata = [data.get_index()] + data.get_dist() + chi2_test(data)
            writecsv.append(linedata)
            linedata = []
            del data
        df_chi2 = pd.DataFrame(writecsv, columns=["label", "C1", "C2", "C3", "C4", "C5", "C6", "C7", "C8", "C9", "C10", "p-value"])
        df_chi2 = df_chi2.set_index("label")
        fw_data = df_chi2
        fw_data.to_csv(sys.argv[2] + "chi2test_" + str(f_name))

if __name__ == "__main__":
    main() 

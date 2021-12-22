import pandas as pd
import sys
from scipy import stats
import math
import glob

COUNT = 1000
MEAN = 0.25

class DB:
    def __init__(self, label, mean, var, std):
        self.label = label
        self.mean = mean
        self.var = var
        self.std = std
        self.z = (self.mean - MEAN) / (math.sqrt(self.var / COUNT))
        self.z_abs = abs(self.z)
        self.p_value = stats.norm.sf(self.z_abs)
    
    def calc_z(self):
        self.z = (self.mean - MEAN) / (math.sqrt(self.var / COUNT))
        self.z_abs = abs(self.z)

    def update(self, mean, var, std):
        self.mean = mean
        self.var = var
        self.std = std
    
    def get_label(self):
        return self.label

    def get_mean(self):
        return self.mean
  
    def get_var(self):
        return self.var
  
    def get_std(self):
        return self.std
  
    def get_z(self):
        return self.z
  
    def get_z_abs(self):
        return self.z_abs
    
    def get_p(self):
        return self.p_value


def get_filename():
    files = glob.glob(sys.argv[1] + "*")
    # for file in files:
    #     print(file)
    return files

def analysis(writedata, csvfilenames):
    for csvfilename in csvfilenames:
        csvfilename = csvfilename
        fr = pd.read_csv(csvfilename, sep=",")
        f_ave = fr.mean()
        f_var = fr.var()
        f_std = fr.std()

        db00 = DB("state 00", f_ave[1], f_var[1], f_std[1])
        db01 = DB("state 01", f_ave[2], f_var[2], f_std[2])
        db10 = DB("state 10", f_ave[3], f_var[3], f_std[3])
        db11 = DB("state 11", f_ave[4], f_var[4], f_std[4])

        for c in range(16):
            globals()["db_%s" % c] = DB("{:04b}".format(c), f_ave[5 + c], f_var[5 + c], f_std[5 + c])
        
        writedata.append([db00.get_p(), db01.get_p(), db10.get_p(), db11.get_p(), db_0.get_p(), db_1.get_p(), db_2.get_p(), db_3.get_p(), db_4.get_p(), db_5.get_p(), db_6.get_p(), db_7.get_p(), db_8.get_p(), db_9.get_p(), db_10.get_p(), db_11.get_p(), db_12.get_p(), db_13.get_p(), db_14.get_p(), db_15.get_p()])

        print("End the test of " + csvfilename + "file.")
    return writedata

def main():
    csvfilenames = get_filename()

    writedata = []

    writedata = analysis(writedata, csvfilenames)
    
    fw = pd.DataFrame(writedata, columns=["00", "01", "10", "11", "00->00", "00->01", "00->10", "00->11", "01->00", "01->01", "01->10", "01->11", "10->00", "10->01", "10->10", "10->11", "11->00", "11->01", "11->10", "11->11"])

    fw.to_csv(sys.argv[2])

if __name__ == "__main__":
    main()
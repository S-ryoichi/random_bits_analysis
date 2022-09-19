import pandas as pd
import sys
from scipy import stats
import math
import glob
import tqdm

COUNT = 1000
MEAN = 0.25

class DB:
    def __init__(self, label, data):
        self.label = label
        self.t, self.p_value = stats.ttest_1samp(data, popmean=MEAN)
        self.t_abs = abs(self.t)
            
    def get_label(self):
        return self.label

    def get_t(self):
        return self.t
  
    def get_t_abs(self):
        return self.t_abs
    
    def get_p(self):
        return self.p_value


def get_filename():
    files = glob.glob(sys.argv[1] + "*")
    # for file in files:
    #     print(file)
    return files

def analysis(writedata, csvfilenames):
    for csvfilename in tqdm.tqdm(csvfilenames):
        csvfilename = csvfilename
        fr = pd.read_csv(csvfilename, sep=",")
        listdata = fr.values.tolist()
        print(listdata)
        for c in range(16):
            globals()["db_%s" % c] = DB("{:04b}".format(c), listdata[5 + c])
        
        writedata.append([db00.get_p(), db01.get_p(), db10.get_p(), db11.get_p(), db_0.get_p(), db_1.get_p(), db_2.get_p(), db_3.get_p(), db_4.get_p(), db_5.get_p(), db_6.get_p(), db_7.get_p(), db_8.get_p(), db_9.get_p(), db_10.get_p(), db_11.get_p(), db_12.get_p(), db_13.get_p(), db_14.get_p(), db_15.get_p()])

        # print("End the test of " + csvfilename + "file.")
    return writedata

def main():
    csvfilenames = get_filename()

    writedata = []

    writedata = analysis(writedata, csvfilenames)
    
    fw = pd.DataFrame(writedata, columns=["state_00", "state_01", "state_10", "state_11", "00->00", "00->01", "00->10", "00->11", "01->00", "01->01", "01->10", "01->11", "10->00", "10->01", "10->10", "10->11", "11->00", "11->01", "11->10", "11->11"])

    fw.to_csv(sys.argv[2])

if __name__ == "__main__":
    main()
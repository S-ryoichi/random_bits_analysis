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
        # csvfilename = csvfilename
        fr = pd.read_csv(csvfilename, sep=",")

        db00 = DB("P(00)", fr["P(00)"].values.tolist())
        db01 = DB("P(01)", fr["P(01)"].values.tolist())
        db10 = DB("P(10)", fr["P(10)"].values.tolist())
        db11 = DB("P(11)", fr["P(11)"].values.tolist())

        # create the label "P(xx)" and "P(xx|yy)"
        db_label_list = []
        for count in range(4):
            db_label_list.append("P({:02b})".format(count))
        for count in range(16):
            count_strbin = "{:04b}".format(count)
            db_label_list.append("P({}|{})".format(count_strbin[2:4], count_strbin[0:2]))
        
        # print(db_label_list)
        db_list = [DB(label, fr[label].values.tolist()) for label in db_label_list]
        p_val_list = [db.get_p() for db in db_list]

        writedata.append(p_val_list)
        # writedata.append([db00.get_p(), db01.get_p(), db10.get_p(), db11.get_p(), db_0.get_p(), db_1.get_p(), db_2.get_p(), db_3.get_p(), db_4.get_p(), db_5.get_p(), db_6.get_p(), db_7.get_p(), db_8.get_p(), db_9.get_p(), db_10.get_p(), db_11.get_p(), db_12.get_p(), db_13.get_p(), db_14.get_p(), db_15.get_p()])

    return writedata

def main():
    csvfilenames = get_filename()

    writedata = []

    writedata = analysis(writedata, csvfilenames)
    
    fw = pd.DataFrame(writedata, columns=["P(00)", "P(01)", "P(10)", "P(11)", "P(00|00)", "P(01|00)", "P(10|00)", "P(11|00)", "P(00|01)", "P(01|01)", "P(10|01)", "P(11|01)", "P(00|10)", "P(01|10)", "P(10|10)", "P(11|10)", "P(00|11)", "P(01|11)", "P(10|11)", "P(11|11)"])

    fw.to_csv(sys.argv[2])

if __name__ == "__main__":
    main()
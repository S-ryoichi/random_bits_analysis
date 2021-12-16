import pandas as pd
import sys
import matplotlib as mpl
import matplotlib.pyplot as plt
# import seaborn as sns
from scipy import stats
import math

COUNT = 1001
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


def plot_hist(f):
    plt.figure()
    # sns.distplot([f["0000"], f["0001"]])
    f.plot(kind="hist", y=["0000", "0001", "0010", "0011"], bins=30, figsize=(7, 5), alpha=0.6, ylim=[0,200])
    plt.xlabel("Probability")
    plt.ylabel("Number of data")
    plt.savefig("./../00.png")
    f.plot(kind="hist", y=["0100", "0101", "0110", "0111"], bins=30, figsize=(7, 5), alpha=0.6, ylim=[0,200])
    plt.xlabel("Probability")
    plt.ylabel("Number of data")
    plt.savefig("./../01.png")
    f.plot(kind="hist", y=["1000", "1001", "1010", "1011"], bins=30, figsize=(7, 5), alpha=0.6, ylim=[0,200])
    plt.xlabel("Probability")
    plt.ylabel("Number of data")
    plt.savefig("./../10.png")
    f.plot(kind="hist", y=["1100", "1101", "1110", "1111"], bins=30, figsize=(7, 5), alpha=0.6, ylim=[0,200])
    plt.xlabel("Probability")
    plt.ylabel("Number of data")
    plt.savefig("./../11.png")
    plt.close("all")


# def plot_hist_sns(f):
#     plt.figure()
#     sns.distplot(f["0000"], bins=30, norm_hist=True, kde=True, label='\"00\"->\"00\"')
#     sns.distplot(f["0001"], bins=30, norm_hist=True, kde=True, label='\"00\"->\"01\"')
#     sns.distplot(f["0010"], bins=30, norm_hist=True, kde=True, label='\"00\"->\"10\"')
#     sns.distplot(f["0011"], bins=30, norm_hist=True, kde=True, label='\"00\"->\"11\"')
#     plt.xlabel("Probability")
#     plt.ylabel("Number of data")
#     plt.legend()
#     plt.savefig("./../state_transition_00.png")
    
#     plt.figure()
#     sns.distplot(f["0100"], bins=30, norm_hist=True, kde=True, label='\"01\"->\"00\"')
#     sns.distplot(f["0101"], bins=30, norm_hist=True, kde=True, label='\"01\"->\"01\"')
#     sns.distplot(f["0110"], bins=30, norm_hist=True, kde=True, label='\"01\"->\"10\"')
#     sns.distplot(f["0111"], bins=30, norm_hist=True, kde=True, label='\"01\"->\"11\"')
#     plt.xlabel("Probability")
#     plt.ylabel("Number of data")
#     plt.legend()
#     plt.savefig("./../state_transition_01.png")
    
#     plt.figure()
#     sns.distplot(f["1000"], bins=30, norm_hist=True, kde=True, label='\"10\"->\"00\"')
#     sns.distplot(f["1001"], bins=30, norm_hist=True, kde=True, label='\"10\"->\"01\"')
#     sns.distplot(f["1010"], bins=30, norm_hist=True, kde=True, label='\"10\"->\"10\"')
#     sns.distplot(f["1011"], bins=30, norm_hist=True, kde=True, label='\"10\"->\"11\"')
#     plt.xlabel("Probability")
#     plt.ylabel("Number of data")
#     plt.legend()
#     plt.savefig("./../state_transition_10.png")
    
#     plt.figure()
#     sns.distplot(f["1100"], bins=30, norm_hist=True, kde=True, label='\"11\"->\"00\"')
#     sns.distplot(f["1101"], bins=30, norm_hist=True, kde=True, label='\"11\"->\"01\"')
#     sns.distplot(f["1110"], bins=30, norm_hist=True, kde=True, label='\"11\"->\"10\"')
#     sns.distplot(f["1111"], bins=30, norm_hist=True, kde=True, label='\"11\"->\"11\"')
#     plt.xlabel("Probability")
#     plt.ylabel("Number of data")
#     plt.legend()
#     plt.savefig("./../state_transition_11.png")


def analysis(f):
    f_ave = f.mean()
    f_var = f.var()
    f_std = f.std()

    db00 = DB("state 00", f_ave[1], f_var[1], f_std[1])

    db01 = DB("state 01", f_ave[2], f_var[2], f_std[2])
    db10 = DB("state 10", f_ave[3], f_var[3], f_std[3])

    db11 = DB("state 11", f_ave[4], f_var[4], f_std[4])

    for c in range(16):
        globals()["db_%s" % c] = DB("{:04b}".format(c), f_ave[5 + c], f_var[5 + c], f_std[5 + c])
    
    tmp = []
    tmp.append([db00.get_label(), db00.get_mean(), db00.get_var(), db00.get_std(), db00.get_z(), db00.get_z_abs(), db00.get_p()])
    tmp.append([db01.get_label(), db01.get_mean(), db01.get_var(), db01.get_std(), db01.get_z(), db01.get_z_abs(), db01.get_p()])
    tmp.append([db10.get_label(), db10.get_mean(), db10.get_var(), db10.get_std(), db10.get_z(), db10.get_z_abs(), db10.get_p()])
    tmp.append([db11.get_label(), db11.get_mean(), db11.get_var(), db11.get_std(), db11.get_z(), db11.get_z_abs(), db11.get_p()])
    tmp.append([db_0.get_label(), db_0.get_mean(), db_0.get_var(), db_0.get_std(), db_0.get_z(), db_0.get_z_abs(), db_0.get_p()])
    tmp.append([db_1.get_label(), db_1.get_mean(), db_1.get_var(), db_1.get_std(), db_1.get_z(), db_1.get_z_abs(), db_1.get_p()])
    tmp.append([db_2.get_label(), db_2.get_mean(), db_2.get_var(), db_2.get_std(), db_2.get_z(), db_2.get_z_abs(), db_2.get_p()])
    tmp.append([db_3.get_label(), db_3.get_mean(), db_3.get_var(), db_3.get_std(), db_3.get_z(), db_3.get_z_abs(), db_3.get_p()])
    tmp.append([db_4.get_label(), db_4.get_mean(), db_4.get_var(), db_4.get_std(), db_4.get_z(), db_4.get_z_abs(), db_4.get_p()])
    tmp.append([db_5.get_label(), db_5.get_mean(), db_5.get_var(), db_5.get_std(), db_5.get_z(), db_5.get_z_abs(), db_5.get_p()])
    tmp.append([db_6.get_label(), db_6.get_mean(), db_6.get_var(), db_6.get_std(), db_6.get_z(), db_6.get_z_abs(), db_6.get_p()])
    tmp.append([db_7.get_label(), db_7.get_mean(), db_7.get_var(), db_7.get_std(), db_7.get_z(), db_7.get_z_abs(), db_7.get_p()])
    tmp.append([db_8.get_label(), db_8.get_mean(), db_8.get_var(), db_8.get_std(), db_8.get_z(), db_8.get_z_abs(), db_8.get_p()])
    tmp.append([db_9.get_label(), db_9.get_mean(), db_9.get_var(), db_9.get_std(), db_9.get_z(), db_9.get_z_abs(), db_9.get_p()])
    tmp.append([db_10.get_label(), db_10.get_mean(), db_10.get_var(), db_10.get_std(), db_10.get_z(), db_10.get_z_abs(), db_10.get_p()])
    tmp.append([db_11.get_label(), db_11.get_mean(), db_11.get_var(), db_11.get_std(), db_11.get_z(), db_11.get_z_abs(), db_11.get_p()])
    tmp.append([db_12.get_label(), db_12.get_mean(), db_12.get_var(), db_12.get_std(), db_12.get_z(), db_12.get_z_abs(), db_12.get_p()])
    tmp.append([db_13.get_label(), db_13.get_mean(), db_13.get_var(), db_13.get_std(), db_13.get_z(), db_13.get_z_abs(), db_13.get_p()])
    tmp.append([db_14.get_label(), db_14.get_mean(), db_14.get_var(), db_14.get_std(), db_14.get_z(), db_14.get_z_abs(), db_14.get_p()])
    tmp.append([db_15.get_label(), db_15.get_mean(), db_15.get_var(), db_15.get_std(), db_15.get_z(), db_15.get_z_abs(), db_15.get_p()])

    fw = pd.DataFrame(tmp, columns=["label", "mean", "var", "std", "z", "z_abs", "p-value"])

    fw.to_csv(sys.argv[2])
    

def main():
    f = pd.read_csv(sys.argv[1], sep=",")

    # z-test
    analysis(f)

    # histgram
    # plot_hist_sns(f)
    # plot_hist(f)



if __name__ == "__main__":
    # sns.set()
    main()
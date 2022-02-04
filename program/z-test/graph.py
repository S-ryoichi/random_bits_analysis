import sys
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt

def plot_graph(df, name):
    plt.figure()
    df.plot(x="label")
    plt.xlabel("The number of ring oscillator circuits")
    plt.ylabel("The number of passing test")
    plt.subplots_adjust(bottom=0.2)
    plt.xticks([num for num in range(25)], df["label"].to_list(), rotation=45)
    # plt.xticks([num for num in range(25)], [num for num in range(1, 26)], rotation=45)
    plt.savefig(sys.argv[2] + name)
    plt.close("all")


def main():
    csv_data = pd.read_csv(sys.argv[1], engine="python")
    
    out = csv_data[["label", "state_00", "state_01", "state_10", "state_11"]]
    plot_graph(out, "freq.png")
    
    out = csv_data[["label", "00->00", "00->01", "00->10", "00->11"]]
    plot_graph(out, "state_trans_00.png")
    
    out = csv_data[["label", "01->00", "01->01", "01->10", "01->11"]]
    plot_graph(out, "state_trans_01.png")
    
    out = csv_data[["label", "10->00", "10->01", "10->10", "10->11"]]
    plot_graph(out, "state_trans_10.png")
    
    out = csv_data[["label", "11->00", "11->01", "11->10", "11->11"]]
    plot_graph(out, "state_trans_11.png")


if __name__ == "__main__":
    main()
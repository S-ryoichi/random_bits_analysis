import numpy as np
import matplotlib as mpl
import sys

data = np.loadtxt(sys.argv[1], delimiter=",", skiprows=0, usecols=(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20))

x_axis[4] = []

x_axis[0] = data[:, 2]
x_axis[1] = data[:, 3]
x_axis[2] = data[:, 4]
x_axis[3] = data[:, 5]

state = (6, 10, 14, 18)
label = ("state00", "state01", "state10", "state11")

def plot(num):
    y1_data = [:, state[num]]
    y2_data = [:, state[num] + 1]
    y3_data = [:, state[num] + 2]
    y4_data = [:, state[num] + 3]

    fig = plt.figure()

    ax = fig.add_subplot(1, 1, 1)

    ax.scatter(x, y1_data, c="red", marker=".", label="state 00")
    ax.scatter(x, y2_data, c="blue", marker="o", label="state 01")
    ax.scatter(x, y3_data, c="green", marker="^", label="state 10")
    ax.scatter(x, y4_data, c="yellow", marker="s", label="state 11")

    ax.set_xlabel("probability of state")
    ax.set_ylabel("probability of next state")

    ax.grid(True)

    ax.legend(loc="upper left")
    # fig.show()
    fig.savefig(label[num] + ".png")

if __name__ == "__main__":
    plot(0)
    plot(1)
    plot(2)
    plot(3)


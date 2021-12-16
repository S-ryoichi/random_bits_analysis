from PIL import Image
import numpy as np
from matplotlib import pyplot as plt
import cv2

f1 = open('../data/image.txt', 'r')
# f2 = open('../data/img.png', 'w')

content = f1.read()
data = []
tmp = []
value = 0

for ch in content:
    if ch == "\n":
        data.append(tmp)
        tmp = []
    elif (ch == "0" or ch == "1"):
        tmp.append(int(ch))
    else:
        print("data is not '0' or '1'.")
        exit(-1)

def resize(data_def, size):
    data2 = [[0 for i in range (len(data) * size)] for i in range (len(data) * size)]
    for i in range(len(data_def)):
        for j in range(len(data_def[i])):
            for loop in range(size):    
                data2[i * size][(j * size) + loop] = data[i][j]
        for loop in range(size):
            data2[(i * size) + loop] = data2[i * size]
    # print(data2)
    # print(np.array(data2))
    return data2

def image_png():
    img = np.array(data)
    img_0_255 = (img >= 1) * 255
    # print(img_0_255)
    Image.fromarray(np.uint8(img_0_255)).save('../graph_cv2.png')
    
    data2 = resize(data, 16)
    # print(data2)
    img2 = np.array(data2)
    # print(img2)
    img2_0_255 = img2 * 255
    Image.fromarray(np.uint8(img2_0_255)).save('../graph2_cv2.png')

def graph_disp():
    img = np.array(data)

    plt.xlabel("i-th row of the matrix")
    plt.ylabel("j-th columns of the matrix")

    plt.imshow(img, cmap="Greys")
    plt.show()
    # print(img)
    plt.imsave("../graph.png", img, cmap="Greys")

if __name__ == "__main__":
    image_png()
    graph_disp()



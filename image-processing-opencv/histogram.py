import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("tobago.jpg")

histogram = cv2.calcHist([img], [0], None, [256], [0, 256])

#plot histogram
plt.hist(img.ravel(), 256, [0, 256])
plt.show()

colr = ('b', 'g', 'r')

for i, c in enumerate(colr):
    histogram2 = cv2.calcHist([img], [i], None, [256], [0, 256])
    plt.plot(histogram2, color = c)
    plt.xlim([0, 256])

plt.show()


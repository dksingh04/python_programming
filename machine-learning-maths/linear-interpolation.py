'''
 The linear interpolation assumes a straight line equation to interpolate the points between every 
 two given points in the data set.
 For example given (x1,y1) and (x2, y2), how to find corresponding y value of xh between x1 and x2.
  Since x is in between x1 and x2, hence y will be between y1 and y2 and we know the slope of line drawn between two point is 
  always same hence we can conclude something like this.

  y - y1 / x - x1 = y2 - y1 / x2 - x1 so y can be written be like this

  y = y1 + ((y2 - y1) / (x2 - x1)) * (x - x1)

  Let's say we have following data points x axis time in sec and y axis in tempereature.

  Time in sec = [0, 20, 40, 60, 80, 100]
  Tempreature = [26.0, 48.6, 61.6, 71.2, 74.8, 75.2]

'''
from numpy import array
import numpy as np

#Matplotlib

from matplotlib import pyplot as plt

sec = array([0, 20, 40, 60, 80, 100], float)
temp = array([26.0, 48.6, 61.6, 71.2, 74.8, 75.2], float)

def findY(xp, x, y):
    for i, xi in enumerate(x):
        if xp < xi:
            return y[i-1] + ((y[i] - y[i-1]) / (x[i] - x[i-1])) * (xp - x[i-1])
        else:
            print("Given point is out of range..")

# find temperature at 50 sec
res = findY(50, sec, temp)

print("the temperature = %.2f " %res)

plt.plot(sec, temp, "ro--")
plt.legend(["linear-interpolation"])
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Linear Interpolation")
plt.show()

# plot the graph using matplot lib




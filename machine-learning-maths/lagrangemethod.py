'''
 Lagrange's Method
 For n degree polynomial data point will be n+1, the Lagrange equation will look like below
 y(x) = y1*l1(x)+y2*l2(x)+.....+yn+1*ln+1(x) or in other word
 
 𝑦(𝑥) = ∑ 𝑦𝑖*l𝑖(𝑥) where   1 >= i <= n+1 and 

l𝑖(𝑥)=∏(𝑥−𝑥𝑗)/(𝑥𝑖 −𝑥𝑗)  where 𝑗=1 to n+1 and 𝑗≠𝑖 so complete formula will look like

𝑦(𝑥) = ∑ 𝑦𝑖 * (∏(𝑥−𝑥𝑗)/(𝑥𝑖 −𝑥𝑗))

'''

from numpy import array
import numpy as np

from matplotlib import pyplot as plt

sec = array([0, 20, 40, 60, 80, 100], float)
temp = array([26.0, 48.6, 61.6, 71.2, 74.8, 75.2], float)
xarray = np.linspace(sec[0], sec[-1], 50)
yarray = np.empty_like(xarray)

def findYp(xp, x, y):
    yp = 0
    #idx = 0
    for i in range(len(x)):
        L = 1
        for j in range(len(x)):
            if i != j:
                L *= (xp - x[j]) / (x[i] - x[j])
            
        yp += y[i] * L    
    
    print('For x = %.1f, y = %.1f' % (xp, yp))

    return yp

xp = input("Enter sec to find the temp : ")

findYp(50, sec, temp)
# plot the graph for linear vs lagrange
idx = 0
for xp in xarray:
    yp = findYp(xp, sec, temp)
    yarray[idx] = yp
    idx += 1

print(xarray)
plt.title("Lagrange vs Linear Interpolation")
plt.plot(sec, temp, "ro--", xarray, yarray)
plt.xlabel("X")
plt.ylabel("Y")
plt.legend(["linear", "lagrange"])
plt.show()

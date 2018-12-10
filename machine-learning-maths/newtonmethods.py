'''
 𝑦(𝑥)=𝑎0 +(𝑥−𝑥1)𝑎1 +(𝑥−𝑥1)(𝑥−𝑥2)𝑎2 +⋯+(𝑥−𝑥1)(𝑥−𝑥2)...(𝑥−𝑥𝑛)𝑎𝑛
 where a0 = y1^1, a1 = y2^2 .... an = yn+1^(n+1)
 yi^(j+1) = (yi^j - yj^j) / (xi - xj) where j = 1,2,3, 4 ... n and i = j+1 ... n+1

 for e.g. y2^2 = (y2^1 - y1^1) / (x2 - x1) and y1^1 = y1 and y2^1 = y2 so on.
 
 So in mathematical terms the Newton's formula can be written as 
 y(x) = a0 + ∑ [∏(x - xj)]ai where i = 1 .. n and j = 1 .. i+1

 Implementation of Newtons Method for Linear Interpolation
'''

import numpy as np 
from matplotlib import pyplot as plt

x = [0.0, 1.5, 2.8, 4.4, 6.1, 8.0] 
y = [0.0, 0.9, 2.5, 6.6, 7.7, 8.0]

def findYp(xp, x, y):
    n = len(x) - 1
    Dy = np.zeros((n+1, n+1))
    Dy[:,0] = y
    #calculate the values for rest of the matrix
    for j in range(n):
        for i in range(j+1, n+1):
            Dy[i, j+1] = (Dy[i,j] - Dy[j, j]) / (x[i] - x[j])
    yp = Dy[0,0]
    for i in range(n):
        xProd = 1
        for j in range(i+1):
            xProd *= (xp - x[j])
        
        yp += xProd * Dy[i+1, i+1]
    
    return yp


xp = float(input('Enter x: '))

yp = findYp(xp, x, y)

print('For x = %.1f, y = %.1f' %(xp, yp))

'''
 Output:
 Enter x: 2.4
 For x = 2.4, y = 1.72.4
'''

# Now plot a graph using matplotlib
xarray = np.linspace(x[0], x[-1], 50)
yarray = np.empty_like(xarray)
idx = 0
for xp in xarray:
    yp = findYp(xp, x, y)
    yarray[idx] = yp
    idx += 1

plt.plot(x, y, "ro--", xarray, yarray)
plt.xlabel("x")
plt.ylabel("Y")

plt.title("Newton's Method of Linear Interpolation")

plt.legend(["linear", "newton's polynomial method"])

plt.show()



'''
  𝑓(𝑥) = 𝑎0 + 𝑎1𝑥 + 𝑎2𝑥^2 + ⋯ + 𝑎𝑛𝑥^𝑛
  [𝐴]{𝑎} = {𝐵}
  Fitting with a Polynomial curve 

'''
from numpy import array
import numpy as np

from matplotlib import pyplot as plt 

x = np.arange(6)
y = np.array([2, 8, 14, 28, 39, 62])


#n degree of polynomial
def findCoefficient(x, y, n):
      A = np.zeros((n+1, n+1))
      B = np.zeros(n+1)
      a = np.zeros(n+1)
      m = len(x)
      for r in range(n+1):
            for c in range(n+1):
                 if r == 0 and c == 0:
                       A[r, c] = m
                       continue
                 A[r,c] = np.sum(x**(r+c))
            
            B[r] = np.sum(x**(r) * y)
      
      a = np.linalg.solve(A, B)

      #print(a)

      return a


def solve(xarray, a):
      yp = 0
      idx = 0
      yarray = np.empty_like(xarray)
      for i in range(0, len(xarray)):
          yp = a[0]
          for j in range(1, len(a)):
                yp += np.sum(a[j]*xarray[i]**(j))
          
          yarray[idx] = yp
          idx+=1

      return yarray

def printequation(c):
      print('The polynomial function is: \n')
      print('f(x) =\t %f \t'% c[0])
      for i in range(1, len(c)):
            print("\t %+f x^%d" %(c[i], i))
      
      print("\n")
      
      
xarray = np.linspace(x[0], x[-1], 50)      
c = findCoefficient(x, y, 2)
printequation(c)
yarray = solve(xarray, c)

#polynomial degree 3
c3 = findCoefficient(x, y, 3)
printequation(c3)
yarray1 = solve(xarray, c3)

#print(yarray)

#Now let's plot a graph using matplotlib

plt.title("Polynomial curve-fitting graph")

plt.plot(x, y, "or", xarray, yarray, "k", xarray, yarray1, "k--")

plt.xlabel("X")
plt.ylabel("Y")

plt.legend(["data-points", "Quadratic, n=2", "Cubic, n=3"])

plt.show()






            

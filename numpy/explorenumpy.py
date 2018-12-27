import numpy as np
x = [0.0, 1.5, 3.0, 4.5, 6.0, ]
y = [0.0, 0.86, 1.71, 2.57, 3.43, 4.29, 5.14, 6.0]

xx = np.array(x)
yy = np.array(y)
y = np.reshape(yy,(2,4)) # convert the matrix to 2x4


#print(y)

nx, ny = (3,2)

xg = np.linspace(0, 1, nx)
yg = np.linspace(0, 1, ny)

#print(x)
#print(y)
xv, yv = np.meshgrid(xg, yg, sparse=False)

print(xv)
print(yv)

x, y = np.meshgrid(xx, yy)

print(x)
print(y)

#x, y = np.meshgrid(xx, yy, sparse=True)

print(np.shape(x))
print(np.shape(y))
y[1,3] = np.nan ; y[4,4] = np.inf
print(y[1,3]) 
print(y[4,4])
print(np.isnan(y))

print(np.identity(3,int))

print(np.where(np.isnan(y)))
print(np.where(y>3))
print(np.eye(5,4, k=3))
A=3.0*( np.eye(5,4,k=4) + np.eye(5,4,k=-4) )
print(" A = \n {0}".format(A))
x = [0.0, 1.5, 3.0, 4.5, 6.0, ]
y = [0.0, 0.86, 1.71, 2.57, 3.43, 4.29, 5.14, 6.0]
def xy_mat(x, y):
    X, Y = np.meshgrid(y, x)
    return X*Y

print(xy_mat(x, y))

#transpose
temp = xy_mat(x, y)
tm = temp.T

print(tm)

Mlr = np.fliplr(temp)

print(Mlr)

Mup = np.flipud(temp)

print(Mup)

#Matrix multiplication
xy = np.dot(tm, temp)
print(xy)
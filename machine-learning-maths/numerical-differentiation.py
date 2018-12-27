f = lambda x : 0.1 * x**5 - 0.2 * x**3 + 0.1*x - 0.2
h = 0.05 #step
x = 0.1
#Forward differences approximation 
dff1 = (f(x+h) - f(x)) / h
dff2 = (f(x+h*2) - 2 * f(x+h) + f(x))/h**2
print('Solution by forward differences:')
print('f\'(%f) = %f'%(x,dff1)) 
print('f\'\'(%f) = %f'%(x,dff2))

#Central differences approximation
dfc1 = (f(x+h) - f(x-h)) / (2*h)
dfc2 = (f(x+h) - 2*f(x) + f(x-h)) / h**2

print('Solution by central differences:') 
print('f\'(%f) = %f'%(x,dfc1)) 
print('f\'\'(%f) = %f'%(x,dfc2))

#Backward differences approximation
dfb1 = (f(x) - f(x-h)) / h
dfb2 = (f(x) - 2 * f(x-h) + f(x-2*h)) / h**2

print('Solution by backward differences:') 
print('f\'(%f) = %f'%(x,dfb1)) 
print('f\'\'(%f) = %f'%(x,dfb2))

#Derivatives by using scipy library
from scipy.misc import derivative
y = derivative(f, 0.1, 0.05) #default n = 1
print(y)
y = derivative(f, 0.1, 0.05, 2) #default n = 2
print(y)
from scipy.optimize import bisect, newton, fsolve, root
# using different math functions from scipy library.
f = lambda x: 2*x**2 - 5*x + 3
print(newton(f,0))
print(newton(f,2))
print(bisect(f,0, 1.2))
print(bisect(f,1.1, 1.8))
print(fsolve(f,[-1, 0, 1, 2, 3]))
print(root(f,0).x)

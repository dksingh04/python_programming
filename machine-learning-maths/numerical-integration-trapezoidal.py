from math import sin, pi

def f(x): return x * sin(x)
l = 0
u = pi/2
n = 5 #Accuracy will improve as you increase the number of steps.
h = (u - l) / n
S = 0.5 * (f(l)+f(u))
for i in range(1, n):
    S += f(l + i*h)

integralResult = h * S

print('Integral = %f' % integralResult)

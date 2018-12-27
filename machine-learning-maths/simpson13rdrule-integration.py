from math import sin, pi

def f(x): return x * sin(x)

l = 0
u = pi/2
n = 20 #Accuracy will improve as you increase the number of steps.
h = (u - l) / n

S = f(l) + f(u)

for i in range(1, n, 2):
    S += 4 * f(l + i*h)

for i in range(2, n, 2):
    S += 2 * f(l + i*h)

integralResult = h/3 * S

print("Integral = %f" % integralResult)
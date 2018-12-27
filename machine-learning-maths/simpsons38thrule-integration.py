from math import sin, pi

def f(x): return x * sin(x)

l = 0
u = pi/2
n = 18 #Accuracy will improve as you increase the number of steps.
h = (u - l) / n

S = f(l) + f(u)

for i in range(1, n, 3):
    S += 3 * (f(l + i*h) + f(l + (i+1)*h))

for i in range(3, n, 3):
    S += 2 * f(l + i*h)

integralResult = (3/8 * h) * S

print("Integral = %f"% integralResult)
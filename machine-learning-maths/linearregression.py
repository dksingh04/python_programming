''' Straigt line equation 𝑓(𝑥) = 𝑎 + 𝑏𝑥
 finding a and b cofficient where b is the slope of line
 𝑎 = 𝑦̅ ∑ 𝑥𝑖^2 − 𝑥 ̅ ∑ 𝑥𝑖 𝑦𝑖 / ∑ 𝑥𝑖^2 − 𝑛𝑥 ̅^2
 𝑏 = ∑𝑥𝑖𝑦𝑖 −𝑥̅∑𝑦𝑖 / ∑ 𝑥𝑖^2 − 𝑛 𝑥 ̅^2 
 𝑎 = 𝑦̅ ∑ 𝑥𝑖^2 − 𝑥 ̅ ∑ 𝑥𝑖 𝑦𝑖 / ∑ 𝑥𝑖^2 − 𝑛𝑥 ̅^2
 𝑥 ̅ and 𝑦̅  are mean of given x and y's data points.

n is number of data points
𝑥̅ = ∑ 𝑥𝑖 / n
𝑦̅ =  ∑ 𝑦𝑖 / n
'''

from numpy import array, sum, mean, arange, ones

#Matplotlib

from matplotlib import pyplot as plt, pylab


x = array([3, 4, 5, 6, 7, 8])
y = array([0, 7, 17, 26, 35, 45])
n = len(x)
ym = mean(y)
xm = mean(x)
a = (ym * sum(x**2) - xm * sum(x*y))/(sum(x**2) - n * xm**2)
b = (sum(x * y) - xm * sum(y)) / (sum(x**2) - n * xm**2)

print('f(x) = %.3f + %.3fx' %(a, b))

# plot the linear regression line for the given datapoints using matplotlib
#generate line fit

line = a + b * x
#plt.scatter(x, y);
plt.plot(x, y,'o', x, line)

pylab.title("Linear Regression fit With Matplotlib")

plt.show()




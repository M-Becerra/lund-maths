import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import fmin
from scipy.integrate import quad


def f(x, y):
    return 8*x*y - 4*x**2*y - 2*x*y**2 + x**2*y**2


def f_wrapp(x0):
    return f(x0[0], x0[1])*-1


xvalues = np.linspace(0,3,100)
yvalues = np.linspace(0,3,100)

xx, yy = np.meshgrid(xvalues, yvalues)
zz = f(xx, yy)
#cs = plt.contour(zz, levels=100)

"""
init_g = [1,1]
solution, iterates = fmin(f_wrapp, init_g, retall=True)
x, y = zip(*iterates)
plt.plot(x, y, "ko")
plt.plot(x, y, "k:")
plt.clabel(cs)
"""
plt.show()


# TASK 2

gamma = lambda t: np.sqrt(4*t**2 + 9*t**4)
print(quad(gamma, -2,1))[0]

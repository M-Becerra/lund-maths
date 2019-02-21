import matplotlib.pyplot as plt
import numpy as np

def f(x, y):
    return 8*x*y - 4*x**2*y - 2*x*y**2 + x**2*y**2

def plot_contour():
    xvalues = np.linspace(-10,10,100)
    yvalues = np.linspace(-10,10,100)

    xx, yy = np.meshgrid(xvalues, yvalues)
    zz = f(xx, yy)

    plt.contour(zz, levels=200)
    plt.show()


def find_minima():
    from scipy.optimize import fmin

    def f_wrapp(x0):
        return f(x0[0], x0[1])*-1
    init_g = [0,0]

    return fmin(f_wrapp, init_g)


print(find_minima())

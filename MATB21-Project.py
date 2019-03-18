import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import quad
from mpl_toolkits.mplot3d import Axes3D


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

# TASK 3

def f1(k):
    return k**2

def f2(k):
    return k-1

def f3(k):
    return k**2+k

def f4(k):
    return np.sin(k)

def surface(x,y,fcn):
    z = x*fcn(y/x)
    return z

for fcn in [f1,f2,f3,f4]:
    # Plot arbitrary points on surface
    fig = plt.figure()
    ax = plt.axes(projection='3d')
    xcoord = 2*np.random.random(size=3) # draws 3 random floats between 0 and 2
    ycoord = 2*np.random.random(size=3)
    zcoord = [surface(xcoord[i],ycoord[i],fcn) for i in range(0,len(xcoord))]
    ax.scatter3D(xcoord, ycoord, zcoord)

    # Draw line between each point and origin
    for i in range(0,len(xcoord)):
        t = np.linspace(0,1,100)
        xline = xcoord[i]*t
        yline = ycoord[i]*t
        zline = zcoord[i]*t
        ax.plot3D(xline, yline, zline, 'gray')

    # Draw contour plot of surface
    x = np.linspace(-6, 6, 30)
    y = np.linspace(-6, 6, 30)

    X, Y = np.meshgrid(x, y)
    Z = surface(X, Y, fcn)
    ax.contour3D(X, Y, Z, 100, cmap='binary')

    plt.show()

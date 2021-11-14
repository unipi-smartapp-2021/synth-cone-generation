import numpy as np
import matplotlib.pyplot as plt
# This is for the (z+1)²=x²+y² cone
from plotly.matplotlylib.mplexporter._py3k_compat import xrange


def generate_cone(with_base=True):
    # set up the grid in polar
    theta = np.linspace(0, 2 * np.pi, 90)
    r = np.linspace(0, 5, 50)
    T, R = np.meshgrid(theta, r)

    # then calculate X, Y, and Z
    X = R * np.cos(T)
    Y = R * np.sin(T)
    Z = np.sqrt(X ** 2 + Y ** 2) - 1  # drop the '-1' if you want a full tip

    Z[Z < 0] = 0  # this "closes" the tip of the cone

    Z_base = Z.copy()
    Z[Z > 2.1] = np.nan  # this crop the cone at the base
    Z_base[Z_base > 2.1] = 2  # this creates a flat base for the cone

    if with_base:
        return X, Y, Z_base
    else:
        return X, Y, Z


def plot_cone(X, Y, Z, wireframe=True, points=30, axis=False):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    if wireframe:
        ax.plot_wireframe(X, Y, Z, rcount=points, ccount=points)
    else:
        ax.plot_surface(X, Y, Z, rcount=30, ccount=30)

    ax.invert_zaxis()

    if not axis:
        ax.axis("off")

    for ii in xrange(0, 360, 1):
        ax.view_init(elev=130., azim=ii)
        plt.show()


def rotate_cone(X, Y, Z):
    pass


X, Y, Z = generate_cone()
plot_cone(X, Y, Z, points=1000, wireframe=False)
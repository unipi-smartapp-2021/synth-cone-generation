import matplotlib.pyplot as plt
import numpy as np

CONE_HEIGHT = 3

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Setup the grid using polar coordinates
theta = np.linspace(2 * np.pi, 0, 100)
r = np.linspace(CONE_HEIGHT, 0, 100)
T, R = np.meshgrid(theta, r)


# Calculate the cartesian coordinates
X = R * np.cos(T)
Y = R * np.sin(T)
Z = np.sqrt(X ** 2 + Y ** 2)

# Set the Z values outside our range to NaNs so they are not populated
ax.plot_surface(X, Y, Z, antialiased=True, linewidth=1)

ax.set_zlim(0, 3)
plt.axis('off')
plt.show()

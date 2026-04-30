import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colormaps

K = 4
N = 1000
M = 5

center = [np.pi, 0]
size = np.pi/4

theta0 = np.linspace(center[0] - size/2, center[0] + size/2, M)
p0 = np.linspace(center[1] - size/2, center[1] + size/2, M)

nx = 1000
ny = 1000

img = np.zeros((ny, nx, 3))
powerCoeff = np.ones((ny, nx, 1))

counter = 0

cmap = plt.get_cmap('hsv')

for i in range(M):
    for j in range(M):

        counter += 1
        if counter % M*M/10000 == 0:
            print('Generating image: ' + str(counter/(M*M)*100) + '%')

        theta = theta0[i]
        p = p0[j]

        col = np.random.random()

        for k in range(N):

            p = (p + K*np.sin(theta))
            theta = (theta + p) % (2*np.pi)

            if theta > center[0] + size/2 or theta < center[0] - size/2:
                continue

            if p > center[1] + size/2 or p < center[1] - size/2:
                continue

            xi = int((theta - center[0] + size/2)/(size) * (nx-1))
            yi = int((p - center[1] + size/2)/(size) * (ny-1))


            if 0 <= yi < ny and 0 <= xi < nx:
                img[yi, xi] = img[yi, xi] + cmap(col)[:3]
                powerCoeff[yi, xi] = powerCoeff[yi, xi] + 1

img = img / powerCoeff

fig, ax = plt.subplots(dpi=300)
ax.imshow(img, origin="lower")

ax.set_xlabel("θ")
ax.set_ylabel("P")
title = "K = " + str(K)

ax.set_xticks([0, 500, 1000])
ax.set_xticklabels([f"{(center[0]-size/2):.3f}", f"{(center[0]):.3f}", f"{(center[0]+size/2):.3f}"])

ax.set_yticks([0, 500, 1000])
ax.set_yticklabels([f"{(center[1]-size/2):.3f}", f"{(center[1]):.3f}", f"{(center[1]+size/2):.3f}"])

plt.subplots_adjust(left=0.1, right=0.95, top=0.9, bottom=0.1)

plt.show()

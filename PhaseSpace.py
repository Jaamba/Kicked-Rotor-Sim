import numpy as np
import matplotlib.pyplot as plt

K = 0.9
N = 1000
M = 50

theta0 = np.linspace(0, 2*np.pi, M)
p0 = np.linspace(-np.pi, np.pi, M)

nx = 1000
ny = 1000

img = np.zeros((ny, nx, 3))
powerCoeff = np.ones((ny, nx, 1))

cmap = plt.cm.viridis

counter = 0

for i in range(M):
    for j in range(M):

        counter += 1
        if counter % M*M/10000 == 0:
            print('Generating image: ' + str(counter/(M*M)*100) + '%')

        theta = theta0[i]
        p = p0[j]

        color = np.random.rand()

        for k in range(N):

            p = p + K*np.sin(theta)
            theta = (theta + p) % (2*np.pi)

            xi = int(theta/(2*np.pi) * (nx-1))
            yi = int((p + np.pi)/(2*np.pi) * (ny-1))

            if 0 <= yi < ny:
                img[yi, xi] = img[yi, xi] + [(i%10)/10, (j%10)/10, color]
                powerCoeff[yi, xi] = powerCoeff[yi, xi] + 1

img = img / np.pow(powerCoeff,1/1.4)

fig, ax = plt.subplots(dpi=300)
ax.imshow(img, origin="lower")

ax.set_xlabel("θ")
ax.set_ylabel("P")
title = "K = " + str(K)

ax.set_xticks([0, 500, 1000])
ax.set_xticklabels(["0", "π", "2π"])

ax.set_yticks([0, 500, 1000])
ax.set_yticklabels(["-π", "0", "π"])

plt.subplots_adjust(left=0.1, right=0.95, top=0.9, bottom=0.1)

plt.show()

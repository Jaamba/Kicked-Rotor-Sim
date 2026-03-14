import numpy as np
import matplotlib.pyplot as plt

K = 1.2
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

plt.figure(dpi=300)
plt.imshow(img, origin="lower")
plt.xlabel("theta")
plt.ylabel("p")
plt.title("Kicked Rotor Phase Space")

plt.show()

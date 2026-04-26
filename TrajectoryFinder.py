import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# Chaos parameter
K = 1.2

def DrawTrajectory(theta, p, N, col):

    thetaList = []
    pList = []

    for k in range(N):

        # Appends values to list
        thetaList.append(theta)
        pList.append(p)

        # Computes standard map
        p = p + K*np.sin(theta)
        theta = (theta + p) % (2*np.pi)

        plt.plot(thetaList, pList, color=col)


theta = 2.84
p = -0.18

DrawTrajectory(theta, p, 10, "red")
#DrawTrajectory(theta-0.04, p, 10, "blue")

# carica immagine
img = mpimg.imread("sfondo.png")

# mostra immagine come sfondo
plt.imshow(img, extent=[0, 2*np.pi, -np.pi, np.pi], aspect='auto')

# Limits
plt.xlim(0, 2*np.pi)
plt.ylim(-np.pi, np.pi)

plt.show()

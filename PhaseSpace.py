import numpy as np
import matplotlib.pyplot as plt

# parametro di caos
K = 1.2

# numero di iterazioni
N = 1000

# numero di tentativi
M = 20

# Crea una griglia di valori iniziali
theta0 = np.linspace(0, 2*np.pi, M)
p0 = np.linspace(-np.pi, np.pi, M)

# Colormap per bellezza
cmap = plt.cm.viridis

# aumenta la risoluzione
plt.figure(dpi=300)

# Cicla sulle condizioni inizali
for i in range(M):
    for j in range(M):

        theta_list = []
        p_list = []

        # Condizione iniziale
        theta = theta0[i]
        p = p0[j]

        # Fa evolvere la ij-esima traiettoria
        for k in range(N):
        
            p = p + K*np.sin(theta)
            theta = theta + p
        
            theta = theta % (2*np.pi)
        
            theta_list.append(theta)
            p_list.append(p)

        # normalizza theta0 in [0,1] per la colormap
        col = cmap(theta0[i] / (2*np.pi))

        # Disegna la j-esima traiettoria con un colore casuale
        plt.scatter(theta_list, p_list, s = 0.1, color=col)

plt.xlabel("theta")
plt.ylabel("p")
plt.title("Kicked Rotor Phase Space")

plt.show()
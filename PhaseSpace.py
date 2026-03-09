import numpy as np
import matplotlib.pyplot as plt

# parametro di caos
K = 1.2

# numero di iterazioni
N = 10000

# numero di tentativi
M = 30

theta0 = np.linspace(0, np.pi, M)
p0 = np.random.uniform(-3, 3, M)

cmap = plt.cm.viridis

for j in range(M):

    theta_list = []
    p_list = []

    # Sceglie casualmente la condizione iniziale
    theta = theta0[j]
    p = p0[j]

    # Fa evolvere la j-esima traiettoria
    for i in range(N):
    
        p = p + K*np.sin(theta)
        theta = theta + p
    
        theta = theta % (2*np.pi)
    
        theta_list.append(theta)
        p_list.append(p)

    # normalizza theta0 in [0,1] per la colormap
    col = cmap(theta0[j] / (2*np.pi))

    # Disegna la j-esima traiettoria con un colore casuale
    plt.scatter(theta_list, p_list, s = 1, color=col)

plt.xlabel("theta")
plt.ylabel("p")
plt.title("Kicked Rotor Phase Space")

plt.show()
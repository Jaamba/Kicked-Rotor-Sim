import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Computes Lyapunov coeff. for a trajectory starting at (theta0, dp0), after N kicks and time t.
def computeLyapunov(initialCondition, dx, N, K):
    
    # Initial conditions for both trajectories
    theta1 = initialCondition[0]
    p1 = initialCondition[1]
    theta2 = theta1 + dx[0]
    p2 = p1 + dx[1]

    for i in range(N):
            
        # Applies standard map
        p1 = p1 + K*np.sin(theta1)
        theta1 = (theta1 + p1) % (2*np.pi)
        p2 = p2 + K*np.sin(theta2)
        theta2 = (theta2 + p2) % (2*np.pi)

    # Computes distance after N kicks
    dtheta = (theta1 - theta2 + np.pi) % (2*np.pi) - np.pi
    d = np.sqrt(dtheta**2 + (p1 - p2)**2)
    d0 = np.sqrt( dx[0]**2 + dx[1]**2 )

    # Returns local lyapunov coefficent
    return np.log(d/d0)/(N)

K = 0.9
N = 100
M = 500

theta0 = np.linspace(0, 2*np.pi, M)
p0 = np.linspace(-np.pi, np.pi, M)

# For 2 directions in the phase space, Lyapunov exponents are computed. The maximum is then chosen
dx0 = 0.0001

# Lyapunov coefficents for each initial condition
lyapunovCoeff = np.zeros((M,M))

# Cicles on a grid of initial conditions
counter = 0
for i in range(M):
    for j in range(M):
        theta = theta0[i]
        p = p0[j]

        # Computes lyap. coeff
        lyap1 = computeLyapunov( (theta, p), [dx0, 0], N, K)
        lyap2 = computeLyapunov( (theta, p), [0, dx0], N, K)
        lyap = lyap1
        
        # Choses maximum lyap. coeff
        if(lyap1 < lyap2):
            lyap = lyap2
            
        lyapunovCoeff[j,i] = lyap

        # Prints progress
        counter = counter + 1
        if counter % ((M*M)/100) == 0:
            print("Computing coefficients: " + str(counter/(M*M)*100) + "%")

fig, ax = plt.subplots(dpi=300)

im = ax.imshow(lyapunovCoeff, origin="lower")  # salva l'immagine

ax.set_xlabel("θ")
ax.set_ylabel("P")
title = "K = " + str(K)

ax.set_xticks([0, M/2, M])
ax.set_xticklabels(["0", "π", "2π"])

ax.set_yticks([0, M/2, M])
ax.set_yticklabels(["-π", "0", "π"])

fig.colorbar(im, ax=ax)  # aggiungi la colorbar

plt.subplots_adjust(left=0.1, right=0.95, top=0.9, bottom=0.1)
plt.show()



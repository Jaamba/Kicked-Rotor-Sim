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
    return np.log(d/d0)/(N*K)

K = 1.2
N = 100
M = 500

theta0 = np.linspace(0, 2*np.pi, M)
p0 = np.linspace(-np.pi, np.pi, M)

# For L directions in the phase space, Lyapunov exponents are computed. The maximum is then chosen
L = 10
dx0 = 0.0001

# Lyapunov coefficents for each initial condition
lyapunovCoeff = np.zeros((M,M))

# Cicles on a grid of initial conditions
counter = 0
for i in range(M):
    for j in range(M):
        theta = theta0[i]
        p = p0[j]

        lyap = 0
        for k in range(L):
            phi = np.linspace(0, 2*np.pi, L)
            dx = [dx0*np.cos(phi[k]), dx0*np.sin(phi[k])]

            # Choses maximum lyap. coeff
            lyapNew = computeLyapunov( (theta, p), dx, N, K)
            if(lyap < lyapNew):
                lyap = lyapNew
            
        lyapunovCoeff[i,j] = lyap

        # Prints progress
        counter = counter + 1
        if counter % ((M*M)/100) == 0:
            print("Computing coefficients: " + str(counter/(M*M)*100) + "%")


# Plots Lyapunov coefficients
fig2 = plt.figure()

plt.imshow(lyapunovCoeff, origin='lower', cmap='viridis')
plt.colorbar()
plt.show()



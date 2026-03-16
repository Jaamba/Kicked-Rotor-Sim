import numpy as np
import matplotlib.pyplot as plt

K = 0.7

dtheta0 = 0.1
dp0 = 0.1

# Distanza iniziale nello spazio delle fasi tra le due traiettorie da simulare
dx0 = (dtheta0, dp0)

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
    d = np.sqrt( (theta1 - theta2)**2 + (p1 - p2)**2 )
    d0 = np.sqrt( dtheta0**2 + dp0**2 )

    # Returns local lyapunov coefficent
    return np.log(d/d0)/(N*K)

print(computeLyapunov( (0,0), (0.0, 0.14), 100, 1.2))



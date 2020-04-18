# Basic SEIR Model: Uses code from https://towardsdatascience.com/social-distancing-to-slow-the-coronavirus-768292f04296
import numpy as np
import matplotlib.pyplot as plt

# Define parameters
t_max = 100
dt = .05
t = np.linspace(0, t_max, int(t_max/dt) + 1)
N = 10000
init_vals = 1 - 1/N, 1/N
init_valsp = 1, 0
alpha = 0.5
beta = 0.05
gamma = 0.1
params = alpha, beta, gamma

def sir(init_vals, init_valsp, params, t):
    S_0, I_0 = init_vals
    S, I = [S_0], [I_0]

    Sp_0, Ip_0 = init_valsp
    Sp, Ip = [Sp_0], [Ip_0]

    alpha, beta, gamma = params
    dt = t[1] - t[0]
    for k in t[1:]:
        next_S = S[-1] - (alpha*S[-1]*I[-1] + alpha*gamma*S[-1]*Ip[-1] + beta*I[-1])*dt
        next_Sp = Sp[-1] - (alpha*Sp[-1]*Ip[-1] + alpha*gamma*Sp[-1]*I[-1] + beta*Ip[-1])*dt
        next_I = I[-1] + (alpha*S[-1]*I[-1] + alpha*gamma*S[-1]*Ip[-1] - beta*I[-1])*dt
        next_Ip = Ip[-1] + (alpha*Sp[-1]*Ip[-1] + alpha*gamma*Sp[-1]*I[-1] - beta*Ip[-1])*dt
        S.append(next_S)
        I.append(next_I)
        Sp.append(next_Sp)
        Ip.append(next_Ip)

    return np.stack([Sp, Ip]).T

# Run simulation
results = sir(init_vals, init_valsp, params, t)
# Plot results
plt.figure(figsize=(12,8))
plt.plot(results)
plt.title('Basic SEIR Model')
plt.legend(['Susceptible', 'Infected'])
plt.xlabel('Time Steps')
plt.ylabel('Fraction of Population')
plt.show()

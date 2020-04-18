# Basic SEIR Model: Uses code from https://towardsdatascience.com/social-distancing-to-slow-the-coronavirus-768292f04296
import numpy as np
import matplotlib.pyplot as plt

# Define parameters
t_max = 100
dt = .05
t = np.linspace(0, t_max, int(t_max/dt) + 1)
N = 10000
init_vals = 1 - 1/N, 1/N, 0
init_valsp = 1, 0, 0
alpha = 0.5
beta = 0.05

def sir(init_vals, init_valsp, params, t):
    S_0, I_0, R_0 = init_vals
    S, I, R = [S_0], [I_0], [R_0]

    Sp_0, Ip_0, Rp_0 = init_valsp
    Sp, Ip, Rp = [Sp_0], [Ip_0], [Rp_0]

    alpha, beta, gamma = params
    dt = t[1] - t[0]
    for k in t[1:]:
        next_S = S[-1] - (alpha*S[-1]*I[-1] + alpha*gamma*S[-1]*Ip[-1])*dt
        next_Sp = Sp[-1] - (alpha*Sp[-1]*Ip[-1] + alpha*gamma*Sp[-1]*I[-1])*dt
        next_I = I[-1] + (alpha*S[-1]*I[-1] + alpha*gamma*S[-1]*Ip[-1] - beta*I[-1])*dt
        next_Ip = Ip[-1] + (alpha*Sp[-1]*Ip[-1] + alpha*gamma*Sp[-1]*I[-1] - beta*Ip[-1])*dt
        next_R = R[-1] + (beta*I[-1])*dt
        next_Rp = Rp[-1] + (beta*Ip[-1])*dt
        S.append(next_S)
        I.append(next_I)
        R.append(next_R)
        Sp.append(next_Sp)
        Ip.append(next_Ip)
        Rp.append(next_Rp)

    return max(Ip)

# Run simulation
#results = []
#for i in range(1, 501):
#    params = alpha, beta, i / 1000
#    results.append((sir(init_vals, init_valsp, params, t)))

params = alpha, beta, 0.1 
print((sir(init_vals, init_valsp, params, t)))

# Plot results
#plt.figure(figsize=(12,8))
#plt.plot(results)
#plt.title('Basic SEIR Model')
#plt.legend(['Susceptible', 'Infected', 'Recovered'])
#plt.xlabel('Time Steps')
#plt.ylabel('Fraction of Population')
plt.show()

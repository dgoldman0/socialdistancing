#Scan through various social distancing coefficients and plot the various graphs

import numpy as np
import matplotlib.pyplot as plt

# Define parameters
t_max = 1000
dt = .05
t = np.linspace(0, t_max, int(t_max/dt) + 1)
N = 20000
init_vals = 0.84 - 0.5/N, 0.16 - 0.5/N, 0.5/N, 0.5/N, 0, 0, 0, 0, 0, 0
alpha = 0.2
beta1 = 1.75
beta2 = 1.75
beta3 = 1.75
gamma = 0.5
#rho1 = 0.5  # Contact rate between young people
rho2 = 0.5 # Contact rate between young and old people
rho3 = 0.5 # Contact rate between old people
mo1 = 0.001
mo2 = 0.1

def model(init_vals, params, t):
    SY_0, SO_0, EY_0, EO_0, IY_0, IO_0, RY_0, RO_0, MY_0, MO_0 = init_vals
    SY, EY, IY, RY, MY = [SY_0], [EY_0], [IY_0], [RY_0], [MY_0]
    SO, EO, IO, RO, MO = [SO_0], [EO_0], [IO_0], [RO_0], [MO_0]
    alpha, beta1, beta2, beta3, gamma, mo1, mo2, rho1, rho2, rho3, t_stop = params
    dt = t[1] - t[0]
    for k in t[1:]:
        if k < t_stop:
            _rho1 = rho1
            _rho2 = rho2
            _rho3 = rho3
        else:
            _rho1 = 1
            _rho2 = 1
            _rho3 = 1
        next_SY = SY[-1] - (_rho1*beta1*SY[-1]*IY[-1] + _rho2*beta2*SY[-1]*IO[-1])*dt
        next_SO = SO[-1] - (_rho3*beta3*SO[-1]*IO[-1] + _rho2*beta2*SO[-1]*IY[-1])*dt
        next_EY = EY[-1] + (_rho1*beta1*SY[-1]*IY[-1] + _rho2*beta2*SY[-1]*IO[-1] - alpha*EY[-1])*dt
        next_EO = EO[-1] + (_rho3*beta3*SO[-1]*IO[-1] + _rho2*beta2*SO[-1]*IY[-1] - alpha*EO[-1])*dt
        next_IY = IY[-1] + (alpha*EY[-1] - gamma*IY[-1])*dt
        next_IO = IO[-1] + (alpha*EO[-1] - gamma*IO[-1])*dt
        next_RY = RY[-1] + (gamma*IY[-1])*dt
        next_RO = RO[-1] + (gamma*IO[-1])*dt
        next_MY = MY[-1] + (mo1*IY[-1])*dt
        next_MO = MO[-1] + (mo2*IO[-1])*dt
        SY.append(next_SY)
        SO.append(next_SO)
        EY.append(next_EY)
        EO.append(next_EO)
        IY.append(next_IY)
        IO.append(next_IO)
        RY.append(next_RY)
        RO.append(next_RO)
        MY.append(next_MY)
        MO.append(next_MO)
    return MO, next_MO

# Run simulation
curves = []
values = []
for rho1 in range(2, 11):
    t_stop = 200
    params = alpha, beta1, beta2, beta3, gamma, mo1, mo2, rho1/10, rho2, rho3, t_stop
    curves.append(model(init_vals, params, t)[0])
    values.append(rho1/10)
# Plot results
plt.figure(figsize=(12,8))
plt.plot(np.stack(curves).T)
plt.legend(values)
plt.xlabel('Time Steps')
plt.show()

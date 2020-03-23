# Scan through various social distancing values and plot the relative mortality rates
import numpy as np
import matplotlib.pyplot as plt

# Define parameters
t_max = 1000
dt = .05
t = np.linspace(0, t_max, int(t_max/dt) + 1)
N = 20000
init_vals = 0.84 - 0.84/N, 0.16 - 0.16/N, 0.84/N, 0.16/N, 0, 0, 0, 0, 0, 0
alpha = 0.2
beta1 = 1.75
beta2 = 1       # Assumes a smaller contact rate between young and old people than between people in the same age group
beta3 = 1.75
gamma = 0.5
rho2 = 0.5      # Contact rate between young and old people
rho3 = 0.5      # Contact rate between old people
m11 = 0.001     # Mortality rate is very low for young people
m21 = 0.1       # And the mortality rate is quite high for older people
m12 = 0.0015    # Low risk mortality rate with over-capacity adjustment
m22 = 0.3       # High risk mortality rate with over-capacity adjustment
k = 0.001       # Hospital bed capacity

def model(init_vals, params, t):
    SY_0, SO_0, EY_0, EO_0, IY_0, IO_0, RY_0, RO_0, MY_0, MO_0 = init_vals
    SY, EY, IY, RY, MY = [SY_0], [EY_0], [IY_0], [RY_0], [MY_0]
    SO, EO, IO, RO, MO = [SO_0], [EO_0], [IO_0], [RO_0], [MO_0]
    alpha, beta1, beta2, beta3, gamma, m11, m21, m12, m22, k, rho1, rho2, rho3, t_start, t_stop = params
    dt = t[1] - t[0]
    for l in t[1:]:
        if l > t_start and l < t_stop:
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
        if (IY[-1] + IO[-1] < k):
            next_MY = MY[-1] + (m11*IY[-1])*dt
            next_MO = MO[-1] + (m21*IO[-1])*dt
        else:
            next_MY = MY[-1] + (m12*IY[-1])*dt
            next_MO = MO[-1] + (m22*IO[-1])*dt
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
    return MO+MY, next_MO+next_MY

# Run simulation
deaths = []
values = []
for rho1 in range(2, 30):
    t_start = 15
    t_stop = 105
    params = alpha, beta1, beta2, beta3, gamma, m11, m21, m12, m22, k, rho1/20, rho2, rho3, t_start, t_stop
    deaths.append(model(init_vals, params, t)[1])
    values.append(rho1/20)
print(min(deaths))
deaths = deaths / max(deaths)
# Plot results
plt.figure(figsize=(12,8))
plt.scatter(values, deaths)
plt.xlabel('ρ')
plt.ylabel('Mortality Rate Relative to Max')
plt.title('Impact of Social Distancing on Mortality')
plt.show()

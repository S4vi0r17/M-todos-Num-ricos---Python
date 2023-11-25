import numpy as np
from scipy import integrate

# Definir la función a integrar
def f(x):
    return 2 * x * np.exp(x**2)

# Definir límites de integración
lim_inf = 0
lim_sup = 1

# Aproximación usando el método del trapecio
approx_trapz = integrate.trapz(f(np.linspace(lim_inf, lim_sup, 1000)), np.linspace(lim_inf, lim_sup, 1000))

# Aproximación usando el método de Simpson
approx_simpson = integrate.simps(f(np.linspace(lim_inf, lim_sup, 1000)), np.linspace(lim_inf, lim_sup, 1000))

print(f"Aproximación con el método del trapecio: {approx_trapz}")
print(f"Aproximación con el método de Simpson: {approx_simpson}")

import numpy as np
from scipy.interpolate import barycentric_interpolate

# Implemente un programa en Python que aproxime el valor de f(0.2), a partir de la
# con n nodos equidistantes en el intervalo [—1; 1] empleando las función f(x) = e^(-x^2)
# raices de un polinomio de TChevichev.

# Función f(x) = e^(-x^2)
def f(x):
    return np.exp(-x**2)

# Número de nodos
n = 10

# Calcular las raíces de los polinomios de Chebyshev de primer tipo en el intervalo [-1, 1]
cheb_roots = np.cos(np.pi * (2*np.arange(1, n+1) - 1) / (2*n))

# Transformar las raíces al intervalo [0, 1]
x_values = 0.5 * (cheb_roots + 1)

# Calcular los valores de f(x) en los nodos
f_values = f(x_values)

# Puntos de interpolación
x_interpolation = 0.2

# Realizar la interpolación de Lagrange
approximation = barycentric_interpolate(x_values, f_values, x_interpolation)

print(f"Aproximación de f(0.2): {approximation}")

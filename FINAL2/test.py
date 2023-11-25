# import numpy as np
# from fractions import Fraction

# # Centeno

# # Función a integrar
# def f(x):
#     return (np.exp(-x**2))**2 * np.pi
#     # return (np.exp(-x**2))**2

# # Regla del trapecio compuesta
# def trapezoidal_rule_composite(f, a, b, n):
#     h = Fraction(b - a, n)
#     result = 0.5 * (f(a) + f(b))

#     x_values = [Fraction(a + i * h) for i in range(n + 1)]
#     y_values = [f(float(x)) for x in x_values]

#     sum_values = sum(y_values[1:-1])  # Suma de los valores en posiciones intermedias

#     for i in range(1, n):
#         result += f(float(a + i * h))

#     result *= h
#     return result, x_values, y_values, sum_values

# # Regla de Simpson compuesta
# def simpson_rule_composite(f, a, b, n):
#     if n % 2 != 0:
#         raise ValueError("El número de subintervalos debe ser par para la regla compuesta de Simpson")

#     h = Fraction(b - a, n)
#     result = f(a) + f(b)

#     x_values = [Fraction(a + i * h) for i in range(n + 1)]
#     y_values = [f(float(x)) for x in x_values]

#     sum_odd = sum(y_values[1:-1:2])  # Suma de los valores en posiciones impares
#     sum_even = sum(y_values[2:-1:2])  # Suma de los valores en posiciones pares

#     for i in range(1, n, 2):
#         result += 4 * f(float(a + i * h))

#     for i in range(2, n - 1, 2):
#         result += 2 * f(float(a + i * h))

#     result *= h / 3
#     return result, x_values, y_values, sum_odd, sum_even

# # Límites de integración
# a = 0
# b = 2

# # Número de subintervalos y nodos
# num_intervals = 6  # n = 6 subintervalos
# num_nodes = 7  # N = 7 nodos
# # Entre más nodos, más exacta es la aproximación
# # numero_intervalos = num_nodes - 1

# # Fórmula de la regla del trapecio compuesta
# formula_trapezoidal = "Integral[a, b] f(x) dx ≈ (h/2) * [f(a) + f(b) + 2 * Σ f(xi_intermedios)]"

# # Fórmula de la regla de Simpson compuesta
# formula_simpson = "Integral[a, b] f(x) dx ≈ (h/3) * [f(a) + f(b) + 4 * Σ f(xi_impar) + 2 * Σ f(xi_par)]"

# # Aproximación usando la regla del trapecio compuesta
# approximation_trapezoidal, x_values_trapz, y_values_trapz, sum_values_trapz = trapezoidal_rule_composite(f, a, b, num_intervals)

# # Aproximación usando la regla de Simpson compuesta
# approximation_simpson, x_values_simpson, y_values_simpson, sum_odd, sum_even = simpson_rule_composite(f, a, b, num_intervals)

# # Crear tabla con los valores
# print("Tabla de valores:")
# print("{:<20} {:<20} {:<20}".format("xi", "yi", " "))
# for xi, yi in zip(x_values_simpson, y_values_simpson):
#     print("{:<20} {:<20}".format(str(xi), yi))

# # Crear tabla con los valores para la regla del trapecio compuesta
# print("Fórmula para la regla del trapecio compuesta:\n", formula_trapezoidal)
# print("\nFórmula con valores reemplazados y listo para resolver:")
# print(f"h = {b}-{a}/{num_intervals} = {Fraction(b - a, num_intervals)}")
# print("f(a) =", f(a))
# print("f(b) =", f(b))
# print("Suma de valores en Σ f(xi_intermedios):", sum_values_trapz)
# print("\nAproximación con la regla del trapecio compuesta:", approximation_trapezoidal)

# # Crear tabla con los valores para la regla de Simpson compuesta
# print("\nFórmula para la regla de Simpson compuesta:\n", formula_simpson)
# print("\nFórmula con valores reemplazados y listo para resolver:")
# print(f"h = {b}-{a}/{num_intervals} = {Fraction(b - a, num_intervals)}")
# print("f(a) =", f(a))
# print("f(b) =", f(b))
# print("Suma de valores en Σ f(xi_impar):", sum_odd)
# print("Suma de valores en Σ f(xi_par):", sum_even)
# print("\nAproximación con la regla de Simpson compuesta:", approximation_simpson)

import numpy as np
from fractions import Fraction

# Centeno

# Función a integrar
def f(x):
    return np.sqrt(1 - x**2)

# Regla del trapecio compuesta
def trapezoidal_rule_composite(f, a, b, n):
    h = Fraction(b - a, n)
    result = 0.5 * (f(a) + f(b))

    x_values = [Fraction(a + i * h) for i in range(n + 1)]
    y_values = [f(float(x)) for x in x_values]

    sum_values = sum(y_values[1:-1])  # Suma de los valores en posiciones intermedias

    for i in range(1, n):
        result += f(float(a + i * h))

    result *= h
    return result, x_values, y_values, sum_values

# Regla de Simpson compuesta
def simpson_rule_composite(f, a, b, n):
    if n % 2 != 0:
        raise ValueError("El número de subintervalos debe ser par para la regla compuesta de Simpson")

    h = Fraction(b - a, n)
    result = f(a) + f(b)

    x_values = [Fraction(a + i * h) for i in range(n + 1)]
    y_values = [f(float(x)) for x in x_values]

    sum_odd = sum(y_values[1:-1:2])  # Suma de los valores en posiciones impares
    sum_even = sum(y_values[2:-1:2])  # Suma de los valores en posiciones pares

    for i in range(1, n, 2):
        result += 4 * f(float(a + i * h))

    for i in range(2, n - 1, 2):
        result += 2 * f(float(a + i * h))

    result *= h / 3
    return result, x_values, y_values, sum_odd, sum_even

# Límites de integración
a = -1
b = 1

# Número de subintervalos y nodos
num_intervals = 6  # n = 6 subintervalos
num_nodes = 7  # N = 7 nodos
# Entre más nodos, más exacta es la aproximación
# numero_intervalos = num_nodes - 1

# Fórmula de la regla del trapecio compuesta
formula_trapezoidal = "Integral[a, b] f(x) dx ≈ (h/2) * [f(a) + f(b) + 2 * Σ f(xi_intermedios)]"

# Fórmula de la regla de Simpson compuesta
formula_simpson = "Integral[a, b] f(x) dx ≈ (h/3) * [f(a) + f(b) + 4 * Σ f(xi_impar) + 2 * Σ f(xi_par)]"

# Aproximación usando la regla del trapecio compuesta
approximation_trapezoidal, x_values_trapz, y_values_trapz, sum_values_trapz = trapezoidal_rule_composite(f, a, b, num_intervals)

# Aproximación usando la regla de Simpson compuesta
approximation_simpson, x_values_simpson, y_values_simpson, sum_odd, sum_even = simpson_rule_composite(f, a, b, num_intervals)

# Crear tabla con los valores
print("Tabla de valores:")
print("{:<20} {:<20} {:<20}".format("xi", "yi", " "))
for xi, yi in zip(x_values_simpson, y_values_simpson):
    print("{:<20} {:<20}".format(str(xi), yi))

# Crear tabla con los valores para la regla del trapecio compuesta
print("Fórmula para la regla del trapecio compuesta:\n", formula_trapezoidal)
print("\nFórmula con valores reemplazados y listo para resolver:")
print(f"h = {b}-{a}/{num_intervals} = {Fraction(b - a, num_intervals)}")
print("f(a) =", f(a))
print("f(b) =", f(b))
print("Suma de valores en Σ f(xi_intermedios):", sum_values_trapz)
print("\nAproximación con la regla del trapecio compuesta:", approximation_trapezoidal)

# Crear tabla con los valores para la regla de Simpson compuesta
print("\nFórmula para la regla de Simpson compuesta:\n", formula_simpson)
print("\nFórmula con valores reemplazados y listo para resolver:")
print(f"h = {b}-{a}/{num_intervals} = {Fraction(b - a, num_intervals)}")
print("f(a) =", f(a))
print("f(b) =", f(b))
print("Suma de valores en Σ f(xi_impar):", sum_odd)
print("Suma de valores en Σ f(xi_par):", sum_even)
print("\nAproximación con la regla de Simpson compuesta:", approximation_simpson)

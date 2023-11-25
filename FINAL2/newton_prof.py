import numpy as np
from scipy.integrate import quad


def f(x):
    return 2 * x * np.exp(x**2)


def integrate_trapezoidal_formula(f, a, b):
    h = b - a
    y0 = f(a)
    y1 = f(b)
    result = (h / 2) * (y0 + y1)
    return result, y0, y1


def integrate_simpson_formula(f, a, b):
    h = (b - a) / 2
    y0 = f(a)
    y1 = f((a + b) / 2)
    y2 = f(b)
    result = (h / 3) * (y0 + 4 * y1 + y2)
    return result, y0, y1, y2

# Límites de integración
a = 0
b = 1

# Aproximación usando el método del trapecio con la fórmula directa
approx_trapz, y0_trapz, y1_trapz = integrate_trapezoidal_formula(f, a, b)

# Aproximación usando el método de Simpson con la fórmula directa
approx_simpson, y0_simpson, y1_simpson, y2_simpson = integrate_simpson_formula(f, a, b)

# Valor exacto de la integral
exact_value, _ = quad(f, a, b)

print("Datos utilizados:")
print(f"Límites de integración: [{a}, {b}]\n")

print("Aproximación con el método del trapecio utilizando la fórmula directa:")
print(f"Resultado aproximado: {approx_trapz}")
print(f"y0: {y0_trapz}, y1: {y1_trapz}\n")

print("Aproximación con el método de Simpson utilizando la fórmula directa:")
print(f"Resultado aproximado: {approx_simpson}")
print(f"y0: {y0_simpson}, y1: {y1_simpson}, y2: {y2_simpson}\n")

print(f"Valor exacto de la integral: {exact_value}")

import numpy as np

# Función a integrar
def f(x):
    return 2 * x * np.exp(x**2)

# Regla del trapecio compuesta
def trapezoidal_rule_composite(f, a, b, n):
    h = (b - a) / n
    result = 0.5 * (f(a) + f(b))

    for i in range(1, n):
        result += f(a + i * h)

    result *= h
    return result

# Regla de Simpson compuesta
def simpson_rule_composite(f, a, b, n):
    if n % 2 != 0:
        raise ValueError("El número de subintervalos debe ser par para la regla compuesta de Simpson")

    h = (b - a) / n
    result = f(a) + f(b)

    for i in range(1, n, 2):
        result += 4 * f(a + i * h)

    for i in range(2, n - 1, 2):
        result += 2 * f(a + i * h)

    result *= h / 3
    return result

# Límites de integración
a = 0
b = 1

# Número de subintervalos
num_intervals = 1000

# Aproximación usando la regla del trapecio compuesta
approximation_trapezoidal = trapezoidal_rule_composite(f, a, b, num_intervals)

# Aproximación usando la regla de Simpson compuesta
approximation_simpson = simpson_rule_composite(f, a, b, num_intervals)

print("Aproximación con la regla del trapecio compuesta:", approximation_trapezoidal)
print("Aproximación con la regla de Simpson compuesta:", approximation_simpson)

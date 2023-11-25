import numpy as np

# Función a integrar (f(x))
def f(x):
    return np.exp(-x**2)

# Regla de Simpson compuesta para el cálculo de la integral
def simpson_composite(f, a, b, n):
    h = (b - a) / n
    integral = f(a) + f(b)
    for i in range(1, n):
        if i % 2 == 0:
            integral += 2 * f(a + i * h)
        else:
            integral += 4 * f(a + i * h)
    integral *= h / 3
    return integral

# Límites de integración
a = 0
b = 2

# Número de nodos
nodos = 7

# Aproximación del volumen utilizando la regla de Simpson compuesta
volumen = np.pi * simpson_composite(f, a, b, nodos)

# Mostrar el resultado
print(f"Aproximación del volumen del sólido de revolución: {volumen}")

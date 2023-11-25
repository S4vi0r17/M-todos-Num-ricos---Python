import numpy as np

# Función a integrar
def f(x):
    return 2 * x * np.exp(x**2)

# Método del trapecio
def integrate_trapezoidal(f, a, b, n):
    h = (b - a) / n
    result = 0.5 * (f(a) + f(b))
    integral_sum = result

    for i in range(1, n):
        xi = a + i * h
        result += f(xi)
        integral_sum += f(xi)

    result *= h
    return result, integral_sum

# Método de Simpson
def integrate_simpson(f, a, b, n):
    if n % 2 != 0:
        raise ValueError("El número de intervalos debe ser par para el método de Simpson")

    h = (b - a) / n
    result = f(a) + f(b)
    integral_sum = result

    for i in range(1, n, 2):
        xi = a + i * h
        result += 4 * f(xi)
        integral_sum += 4 * f(xi)

    for i in range(2, n - 1, 2):
        xi = a + i * h
        result += 2 * f(xi)
        integral_sum += 2 * f(xi)

    result *= h / 3
    return result, integral_sum

# Límites de integración
a = 0
b = 1

# Número de subintervalos
num_intervals = 1000

# Aproximación usando el método del trapecio
approx_trapz, sum_trapz = integrate_trapezoidal(f, a, b, num_intervals)

# Aproximación usando el método de Simpson
approx_simpson, sum_simpson = integrate_simpson(f, a, b, num_intervals)

print("Datos utilizados:")
print(f"Límites de integración: [{a}, {b}]")
print(f"Número de subintervalos: {num_intervals}\n")

print("Aproximación con el método del trapecio:")
print(f"Resultado aproximado: {approx_trapz}")
print(f"Suma de los valores evaluados: {sum_trapz}\n")

print("Aproximación con el método de Simpson:")
print(f"Resultado aproximado: {approx_simpson}")
print(f"Suma de los valores evaluados: {sum_simpson}\n")

import numpy as np
import math

# Datos proporcionados
# xi = np.array([1, 2, 3, 4, 5])
# fx = np.array([1, 1.08, 2.08, 1.91, 0.12])

xi = np.array([0, 0.5, 0.6, 1])
fx = np.array([0, 0.4794, 0.5646, 0.8415])

# Punto donde deseas aproximar f(x)
x_aprox = 0.55


# Función para calcular el polinomio de Lagrange
def lagrange_interpolation(xi, fx, x):
    n = len(xi)
    result = 0.0
    table = np.zeros((n, n + 1))

    # Inicializa la tabla con los valores conocidos
    for i in range(n):
        table[i][0] = xi[i]
        table[i][1] = fx[i]

    # Calcula las diferencias divididas
    for j in range(2, n + 1):
        for i in range(n - j + 1):
            table[i][j] = (table[i + 1][j - 1] - table[i][j - 1]) / (table[i + j - 1][0] - table[i][0])

    # Calcula el resultado utilizando el polinomio interpolante de Lagrange
    for i in range(n):
        term = table[0][i + 1]
        for j in range(i):
            term *= (x - table[j][0])
        result += term

    return result, table


# Calcula el valor aproximado de f(x_aprox) y muestra la tabla de diferencias divididas
valor_aproximado, tabla_diferencias_divididas = lagrange_interpolation(xi, fx, x_aprox)

# Imprime el resultado con 6 cifras decimales
print(f"Aproximación de f({x_aprox}): {valor_aproximado}")

# Imprime la tabla de diferencias divididas con 6 cifras decimales
print("\nTabla de Diferencias Divididas:")
for row in tabla_diferencias_divididas:
    for value in row:
        print(f"{value:.6f}", end="\t")
    print()

# Para el valor exacto
print()
print(f"Valor Exacto de f({x_aprox}): {math.sin(x_aprox)}")

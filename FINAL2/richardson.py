import numpy as np
import pandas as pd

# Definir la función f(x) = e^(-x^2)
def f(x):
    return np.exp(-x ** 2)

h = 1 # Tamaño de paso
N = 4 # Número de iteraciones
x0 = 1 # Punto en el que se evalúa la derivada

# Aproximación usando la fórmula progresiva
D = np.zeros((N, N))
for i in range(N):
    D[i, 0] = (f(x0 + h) - f(x0)) / h
    h /= 2

# Esquema iterativo de extrapolación de Richardson
for j in range(N - 1):
    for i in range(N - j - 1):
        D[i, j + 1] = (2 ** (j + 1) * D[i + 1, j] - D[i, j]) / (2 ** (j + 1) - 1)

# Convertir la matriz a un DataFrame de Pandas para mostrarla como tabla
richardson_table = pd.DataFrame(D, columns=[f"Iteración {i+1}" for i in range(N)])

# Imprimir la tabla
print("Matriz de extrapolación de Richardson:")
print(richardson_table)

# Definir la derivada exacta de f(x) = e^(-x^2)
df = lambda x: -2 * x * np.exp(-x ** 2)

# Obtener la aproximación de la derivada en x = 1
approx_derivative = D[0, -1]
print("\nAproximación de la derivada en x = 1:", approx_derivative)

# Calcular el valor exacto de la derivada en x = 1
exact_derivative = df(1)
print("Valor exacto de la derivada en x = 1:", exact_derivative)

# https://chat.openai.com/share/e29c7f57-959c-4658-9c77-17242dfa901f
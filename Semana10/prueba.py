import numpy as np
import matplotlib.pyplot as plt

# Función f(x) = e^(-x^2)
def f(x):
    return np.exp(-x**2)

# Intervalo [0, 2]
a, b = 0, 2

# Número de puntos
N1 = 10
N2 = 20

# Crear una lista de valores equidistantes en el intervalo [0, 2]
x_values = np.linspace(a, b, N1)
h = (b - a) / (N1 - 1)

# Calcular las derivadas numéricas utilizando las fórmulas de diferencia hacia adelante y centrada
forward_derivative = [(f(x + h) - f(x)) / h for x in x_values]
central_derivative = [(f(x + h) - f(x - h)) / (2 * h) for x in x_values]

# Crear una lista de valores equidistantes en el intervalo [0, 2] con N2 puntos
x_values2 = np.linspace(a, b, N2)
h2 = (b - a) / (N2 - 1)

# Calcular las derivadas numéricas utilizando las fórmulas de diferencia hacia adelante y centrada
forward_derivative2 = [(f(x + h2) - f(x)) / h2 for x in x_values2]
central_derivative2 = [(f(x + h2) - f(x - h2)) / (2 * h2) for x in x_values2]

# Crear una lista de valores de la función f(x)
f_values = [f(x) for x in x_values]
f_values2 = [f(x) for x in x_values2]

# Graficar la función y las derivadas numéricas
plt.figure(figsize=(10, 6))
plt.plot(x_values, f_values, label='f(x) = e^(-x^2)', color='blue')
plt.plot(x_values, forward_derivative, label=f'Derivada Hacia Adelante (N={N1})', color='red')
plt.plot(x_values, central_derivative, label=f'Derivada Centrada (N={N1})', color='green')
plt.plot(x_values2, forward_derivative2, label=f'Derivada Hacia Adelante (N={N2})', linestyle='--', color='red')
plt.plot(x_values2, central_derivative2, label=f'Derivada Centrada (N={N2})', linestyle='--', color='green')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Función y Derivadas Numéricas de f(x) = e^(-x^2)')
plt.legend()
plt.grid(True)

plt.show()

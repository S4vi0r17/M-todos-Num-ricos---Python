import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return np.exp(-x**2)

# Nodos
x_nodes = [0, 0.5, 0.8, 1]
f_values = [f(x) for x in x_nodes]

# Punto de interpolación
x_interpolation = 0.2

# Polinomio de Lagrange
def lagrange(x, x_nodes, f_values):
    result = 0
    for i in range(len(x_nodes)):
        term = f_values[i]
        for j in range(len(x_nodes)):
            if i != j:
                term *= (x - x_nodes[j]) / (x_nodes[i] - x_nodes[j])
        result += term
    return result

# Crear un rango de valores de x para la gráfica
x_range = np.linspace(-0.2, 1.2, 400)
y_range = [f(x) for x in x_range]

# Calcular los valores de interpolación en el rango
interpolation_values = [lagrange(x, x_nodes, f_values) for x in x_range]

# Gráfica
plt.figure(figsize=(8, 6))
plt.plot(x_range, y_range, label="f(x) = e^(-x^2)", color="blue")
plt.plot(x_range, interpolation_values, label="Polinomio de Lagrange", color="red")
plt.scatter(x_nodes, f_values, label="Nodos", color="green", marker="o")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Comparación de f(x) y el Polinomio de Lagrange")
plt.legend()
plt.grid(True)

# Mostrar la gráfica
plt.show()

import numpy as np

# Es posible implementar un programa en Python que aproxime el valor de f(0.2), a partir de la función f(x) = e^(-x^2) y los nodos {x0 = 0; x1 = 0.5; x2= 0.8;x4 = 1) ?

def f(x):
    return np.exp(-x**2)

# Nodos: de preferencia usar nodos. O sea esta :v
x_nodes = [0, 0.5, 0.8, 1]
f_values = [f(x) for x in x_nodes]

# Punto de interpolación
x_interpolation = 0.2

# Función para calcular el polinomio de Lagrange
def lagrange(x, x_nodes, f_values):
    result = 0
    for i in range(len(x_nodes)):
        term = f_values[i]
        for j in range(len(x_nodes)):
            if i != j:
                term *= (x - x_nodes[j]) / (x_nodes[i] - x_nodes[j])
        result += term
    return result

# Calcular la aproximación de f(0.2) utilizando el polinomio de Lagrange
approximation = lagrange(x_interpolation, x_nodes, f_values)

print(f"Aproximación de f(0.2): {approximation}")

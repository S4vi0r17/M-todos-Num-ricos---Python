import numpy as np
from scipy.optimize import minimize_scalar

# Función a aproximar
def f(x):
    return np.exp(x)

# Polinomio interpolante de Lagrange de tercer grado
def lagrange_interpolation(x, nodes, values):
    result = 0.0
    n = len(nodes)
    
    for i in range(n):
        term = values[i]
        for j in range(n):
            if i != j:
                term *= (x - nodes[j]) / (nodes[i] - nodes[j])
        result += term
    
    return result

# Definir nodos y valores correspondientes
nodes = [0, 0.2, 0.5, 1]
values = [f(x) for x in nodes]

# Función para encontrar el máximo de |f(x) - P(x)| en el intervalo [0, 1]
def max_error(coefficients):
    error_func = lambda x: abs(f(x) - lagrange_interpolation(x, nodes, coefficients))
    result = minimize_scalar(error_func, bounds=(0, 1), method='bounded')
    return -result.fun

# Encontrar los coeficientes del polinomio de interpolación de tercer grado
coefficients = np.polyfit(nodes, values, 3)

# Calcular el máximo error
max_error_value = max_error(coefficients)

print(f'Máximo error posible: {max_error_value:.10f}')

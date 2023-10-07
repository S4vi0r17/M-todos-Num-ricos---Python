import numpy as np
from scipy.interpolate import lagrange
import math

# Define la función f(x) = e^x
def f(x):
    return math.exp(-x**2)

# Nodos dados
x_nodos = np.array([0, 0.1, 0.5, 0.7, 1])
y_nodos = np.array([f(x) for x in x_nodos])

# Punto donde deseas aproximar f(x)
x_aprox = 0.2

# Calcula el valor exacto de f(x_aprox)
valor_exacto = f(x_aprox)

# Inicializa una lista para almacenar los resultados
resultados = []

# Calcula el error para polinomios de grado 1 a 3
for grado in range(1, 4):
    # Interpola los nodos con un polinomio de Lagrange de grado 'grado'
    polinomio_interpolante = lagrange(x_nodos[:grado+1], y_nodos[:grado+1])
    
    # Calcula el valor aproximado de f(x_aprox) usando el polinomio interpolante
    valor_aproximado = polinomio_interpolante(x_aprox)
    
    # Calcula el error absoluto
    error = abs(valor_exacto - valor_aproximado)
    
    resultados.append({
        'Grado del Polinomio': grado,
        'Valor Aproximado': valor_aproximado,
        'Error': error
    })

# Ordena los resultados por grado del polinomio
resultados = sorted(resultados, key=lambda x: x['Grado del Polinomio'])

# Imprime los resultados
print(f"Valor exacto de f({x_aprox}): {valor_exacto}")
print("\nResultados para diferentes grados de polinomios interpolantes:")
for resultado in resultados:
    print(f"Grado del Polinomio: {resultado['Grado del Polinomio']}")
    print(f"Valor Aproximado: {resultado['Valor Aproximado']}")
    print(f"Error: {resultado['Error']}")
    print("-" * 30)

# Encuentra el máximo error
max_error = max(resultados, key=lambda x: x['Error'])

print(f"Máximo error posible (grado {max_error['Grado del Polinomio']}): {max_error['Error']}")
